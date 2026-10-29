#!/usr/bin/env python3
"""
shadow_ai_footprint.py — passive Shadow AI external footprint collector.

Queries third-party indexes only:
  S2  crt.sh / Cert Spotter (no key)       -> AI-product subdomain labels
  S3  GitHub Code Search (gh CLI, signed in) -> AI-agent config files in org/user repos
  S1  Shodan facets      (optional API key)  -> AI products on the org's ASN / cert names

It NEVER connects to a discovered host, resolves names, or opens share links.
Google (S4/S5) is intentionally not automated: run those queries by hand with
your scope, as the repository's CONTRIBUTING requires.

Usage:
  python3 shadow_ai_footprint.py --domain example.com --gh-org example-corp \
      [--gh-user jdoe ...] [--asn AS12345] [--orgname "Example Corp"] \
      [--shodan-key $SHODAN_API_KEY] [--out report.md]

Requires: Python 3.10+, `requests`; `gh` CLI authenticated for S3; shodan key for S1.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone

try:
    import requests
except ImportError:
    sys.exit("pip install requests  (use --break-system-packages on Homebrew Python)")

PRODUCT_LABELS = [
    "ollama", "n8n", "flowise", "langflow", "openwebui", "open-webui", "litellm",
    "mcp", "dify", "langfuse", "anythingllm", "librechat", "comfyui", "jupyter",
    "mlflow", "ray", "vllm",
]
GENERIC_LABELS = ["ai", "gpt", "llm", "chat", "bot", "assistant", "agent", "copilot"]

GH_FILES = [
    ("S3-01", "mcp.json", None),
    ("S3-02", "mcp.json", ".cursor"),
    ("S3-03", "claude_desktop_config.json", None),
    ("S3-04", "CLAUDE.md", None),
    ("S3-04", "settings.json", ".claude"),
    ("S3-05", "AGENTS.md", None),
    ("S3-06", "GEMINI.md", None),
    ("S3-07", "copilot-instructions.md", ".github"),
    ("S3-08", ".cursorrules", None),
    ("S3-08", ".windsurfrules", None),
    ("S3-08", ".clinerules", None),
    ("S3-09", ".aider.conf.yml", None),
    ("S3-09", "config.json", ".continue"),
]
GH_ENV_KEYS = ["ANTHROPIC_API_KEY", "OPENAI_API_KEY", "GEMINI_API_KEY", "N8N_ENCRYPTION_KEY"]

SHODAN_QUERIES = {
    "S1-01 Ollama": '"Ollama" port:11434',
    "S1-03 n8n": 'http.title:"n8n.io - Workflow Automation"',
    "S1-04 Langflow": 'http.title:"Langflow"',
    "S1-05 Open WebUI": 'http.title:"Open WebUI"',
    "S1-06 Flowise": 'http.title:"Flowise"',
}

UA = {"User-Agent": "ai_osint-shadow-ai-footprint/2.0 (+https://github.com/7WaySecurity/ai_osint)"}


# ------------------------------------------------- S2 Certificate Transparency
def _crtsh_names(domain: str) -> list[str]:
    """crt.sh JSON. Frequently returns 502/503 under load, so retry with backoff."""
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    for attempt in range(3):
        try:
            r = requests.get(url, headers=UA, timeout=30)
            if r.status_code == 200:
                out = []
                for row in r.json():
                    out += str(row.get("name_value", "")).split("\n")
                return out
        except (requests.RequestException, ValueError):
            pass
        if attempt == 2:
            break
        wait = 5 * (attempt + 1)
        print(f"     crt.sh busy, retry in {wait}s ({attempt + 1}/2)", file=sys.stderr)
        time.sleep(wait)
    raise RuntimeError("crt.sh unavailable")


def _certspotter_names(domain: str) -> list[str]:
    """SSLMate Cert Spotter public API (no key, rate-limited). Paginates with `after`."""
    base = "https://api.certspotter.com/v1/issuances"
    params = {"domain": domain, "include_subdomains": "true", "expand": "dns_names"}
    out, after = [], None
    for _ in range(20):
        if after:
            params["after"] = after
        r = requests.get(base, params=params, headers=UA, timeout=60)
        if r.status_code != 200:
            break
        page = r.json()
        if not page:
            break
        for iss in page:
            out += iss.get("dns_names", [])
        after = page[-1].get("id")
    if not out:
        raise RuntimeError("Cert Spotter unavailable or empty")
    return out


def s2_crtsh(domain: str) -> dict:
    """Query both CT sources and merge; either one alone is enough."""
    raw, sources = [], []
    for label, fn in (("crt.sh", _crtsh_names), ("Cert Spotter", _certspotter_names)):
        try:
            got = fn(domain)
            raw += got
            sources.append(f"{label} ({len(got)})")
        except (RuntimeError, requests.RequestException, ValueError):
            print(f"     {label} unavailable, continuing", file=sys.stderr)
    source = " + ".join(sources) if sources else "unavailable"
    names: set[str] = set()
    for n in raw:
        n = str(n).strip().lower().lstrip("*.")
        if n == domain or n.endswith("." + domain):
            names.add(n)
    def labels_of(n: str) -> list[str]:
        host = n[: -len(domain)].rstrip(".")
        return [p for p in re.split(r"[.\-_]", host) if p]
    product, generic = [], []
    for n in sorted(names):
        labs = labels_of(n)
        if any(l in PRODUCT_LABELS for l in labs):
            product.append(n)
        elif any(l in GENERIC_LABELS for l in labs):
            generic.append(n)
    return {"source": source, "total_names": len(names), "product": product, "generic": generic}


# ---------------------------------------------------- S3 GitHub Code Search
GH_DELAY = 7  # GitHub Code Search allows ~10 requests/minute per user


def _gh_search(scope: str, filename: str, path: str | None, extra: str | None,
               errors: list[str]) -> list[dict]:
    """One `gh search code` call. Retries once on rate limit; records real errors."""
    cmd = ["gh", "search", "code", "--limit", "50", "--json", "repository,path,url",
           "--owner", scope, "--filename", filename]
    if extra:
        cmd.append(extra)
    label = f"{scope}:{filename}" + (f" {extra}" if extra else "")
    for attempt in range(2):
        time.sleep(GH_DELAY)
        try:
            out = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        except subprocess.TimeoutExpired:
            errors.append(f"{label}: timeout")
            return []
        if out.returncode == 0:
            try:
                hits = json.loads(out.stdout or "[]")
            except json.JSONDecodeError:
                errors.append(f"{label}: unreadable response")
                return []
            if path:
                hits = [h for h in hits if h.get("path", "").startswith(path + "/")
                        or f"/{path}/" in "/" + h.get("path", "")]
            return hits
        err = (out.stderr or "").strip().splitlines()[-1:] or ["unknown error"]
        if "rate limit" in err[0].lower() and attempt == 0:
            print("     GitHub rate limit, waiting 60s", file=sys.stderr)
            time.sleep(60)
            continue
        errors.append(f"{label}: {err[0]}")
        return []
    errors.append(f"{label}: rate limited")
    return []


def s3_github(gh_org: str | None, gh_users: list[str]) -> dict:
    findings: dict[str, list[dict]] = {}
    errors: list[str] = []
    if not shutil.which("gh"):
        return {"findings": findings, "errors": ["gh CLI not installed"], "queries": 0}
    if subprocess.run(["gh", "auth", "status"], capture_output=True).returncode != 0:
        return {"findings": findings, "errors": ["gh not authenticated (run: gh auth login)"], "queries": 0}
    scopes = ([gh_org] if gh_org else []) + gh_users
    jobs = [(sid, f, p, None) for sid, f, p in GH_FILES] + [("S3-10", ".env", None, k) for k in GH_ENV_KEYS]
    total = len(scopes) * len(jobs)
    n = 0
    for scope in scopes:
        for sid, fname, path, key in jobs:
            n += 1
            print(f"     [{n}/{total}] {scope} {fname}" + (f" {key}" if key else ""), file=sys.stderr)
            for h in _gh_search(scope, fname, path, key, errors):
                row = {"scope": scope, **h}
                if key:
                    row["key"] = key
                findings.setdefault(sid, []).append(row)
    return {"findings": findings, "errors": errors, "queries": total}


# --------------------------------------------------------- S1 Shodan facets
def s1_shodan(key: str, asn: str | None, domain: str, orgname: str | None) -> dict:
    scopes = []
    if asn:
        scopes.append(f"asn:{asn}")
    scopes.append(f"ssl.cert.subject.cn:{domain}")
    if orgname:
        scopes.append(f'org:"{orgname}"')
    results: dict[str, dict] = {}
    for label, q in SHODAN_QUERIES.items():
        for sc in scopes:
            full = f"{q} {sc}"
            r = requests.get(
                "https://api.shodan.io/shodan/host/count",
                params={"key": key, "query": full, "facets": "ip:20"},
                headers=UA, timeout=60,
            )
            if r.status_code != 200:
                results[f"{label} | {sc}"] = {"error": r.status_code}
                continue
            d = r.json()
            results[f"{label} | {sc}"] = {
                "query": full,
                "total": d.get("total", 0),
                "ips": [f["value"] for f in d.get("facets", {}).get("ip", [])],
            }
    return results


# --------------------------------------------------------------- reporting
def render(args, s2, s3, s1) -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    L = [f"# Shadow AI external footprint — {args.domain}", "", f"Generated: {now} · passive only · ai_osint v2.0.0", ""]

    L += ["## S1 — Self-hosted AI on owned infrastructure (Shodan)", ""]
    if s1 is None:
        L.append("_Skipped (no --shodan-key)._")
    else:
        L += ["| Query | Total | Sample IPs |", "|---|---|---|"]
        for k, v in s1.items():
            if "error" in v:
                L.append(f"| {k} | error {v['error']} | |")
            elif v["total"]:
                L.append(f"| `{v['query']}` | **{v['total']}** | {', '.join(v['ips'][:10])} |")
        if not any(v.get("total") for v in s1.values()):
            L.append("| — | 0 | no AI product fingerprints on the provided scope |")
    L.append("")

    L += ["## S2 — Certificate Transparency", "", f"Source: {s2['source']} · names observed: {s2['total_names']}", ""]
    L += ["**Product-name labels (cross-check with S1):**", ""]
    L += [f"- `{n}`" for n in s2["product"]] or ["- none"]
    L += ["", "**Generic labels (context only, low confidence):**", ""]
    L += [f"- `{n}`" for n in s2["generic"][:50]] or ["- none"]
    L.append("")

    L += ["## S3 — AI-agent configuration in public code (GitHub)", ""]
    f3, e3 = s3["findings"], s3["errors"]
    L.append(f"Queries run: {s3['queries']} · with errors: {len(e3)}")
    L.append("")
    if not f3 and not e3 and s3["queries"]:
        L += ["No AI-agent configuration files found in the public repositories of the scope.", ""]
    for sid in sorted(f3):
        L += [f"### {sid} ({len(f3[sid])} hits)", ""]
        for h in f3[sid][:30]:
            repo = h.get("repository", {}).get("nameWithOwner", "?")
            L.append(f"- `{repo}` / `{h.get('path','')}`" + (f" — key name: `{h['key']}`" if "key" in h else ""))
        L.append("")
    if e3:
        L += ["**Queries that did not complete (re-run later):**", ""]
        L += [f"- {e}" for e in e3[:30]]
        L.append("")

    L += ["## S4 / S5 — Google (run manually with your scope)", "",
          "```",
          f'"chatgpt.com/share/" "{args.orgname or args.domain}"',
          f'"claude.ai/share/" "{args.orgname or args.domain}"',
          f'"claude.ai/public/artifacts/" "{args.orgname or args.domain}"',
          f'"gemini.google.com/share/" "{args.orgname or args.domain}"',
          f'"grok.com/share/" "{args.orgname or args.domain}"',
          f'"copilot.microsoft.com/shares/" "{args.orgname or args.domain}"',
          f'"chat.deepseek.com/share/" "{args.orgname or args.domain}"',
          f'site:lovable.app "{args.orgname or args.domain}"',
          f'site:chatgpt.com inurl:/g/ "{args.orgname or args.domain}"',
          "```", "",
          "Add the hits to the report with the page where each link was posted.", ""]

    L += ["## Boundaries", "", "No host was contacted, no name resolved, no share link opened. "
          "Validate ownership and sanction status before reporting; subtract sanctioned tools.", ""]
    return "\n".join(L)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--domain", required=True)
    p.add_argument("--gh-org")
    p.add_argument("--gh-user", action="append", default=[])
    p.add_argument("--asn", help="AS12345")
    p.add_argument("--orgname", help='Exact Shodan org: string, e.g. "Example Corp"')
    p.add_argument("--shodan-key")
    p.add_argument("--out", default=None)
    args = p.parse_args()

    print(f"[S2] Certificate Transparency for {args.domain}", file=sys.stderr)
    s2 = s2_crtsh(args.domain)
    print("[S3] GitHub code search (~7s per query to respect rate limits)", file=sys.stderr)
    s3 = s3_github(args.gh_org, args.gh_user)
    s1 = None
    if args.shodan_key:
        print(f"[S1] Shodan count/facets (1 credit per query)", file=sys.stderr)
        s1 = s1_shodan(args.shodan_key, args.asn, args.domain, args.orgname)

    md = render(args, s2, s3, s1)
    out = args.out or f"shadow_ai_{args.domain.replace('.', '_')}.md"
    with open(out, "w", encoding="utf-8") as f:
        f.write(md)
    print(f"Report written to {out}", file=sys.stderr)


if __name__ == "__main__":
    main()
