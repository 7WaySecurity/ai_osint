# Changelog

## [2.0.0] — 2026-10-28 — Shadow AI External Footprint

**Why a major version:** the repository's scope changes from *"which AI surfaces are exposed on the internet"* to *"measure one organization's unsanctioned AI from outside"*. Every previous dork still works; the new section reuses them with organization scoping.

### Added
- `shadow-ai/README.md` — methodology: five external surfaces (S1 infrastructure, S2 CT logs, S3 agent configs in code, S4 shares on third-party sites, S5 employee-built apps), organization scoping inputs, scoring model with sanctioned-use subtraction, legal boundaries (passive vs. active; Colombia Ley 1273/2009).
- `shadow-ai/SIGNALS.md` — every query by surface with context and expected noise, plus what is left out by design and why.
- `shadow-ai/INTERNAL_ANNEX.md` — links to public internal detections (Splunk *Local LLM Framework DNS Query*, Microsoft *AI Agents – No Authentication Required*, Elastic/Splunk rule repos). No duplication.
- `shadow-ai/scripts/shadow_ai_footprint.py` — passive collector: crt.sh + Cert Spotter + GitHub Code Search (`gh`) + optional Shodan count/facets → Markdown report. Prints the S4/S5 Google queries for manual execution.
- README: Shadow AI section and link.

### Left out by design
- LiteLLM and ComfyUI scan fingerprints — honeypot-dominated (Wiz Sep 2026, Censys Apr 2026).
- Port-only fingerprints (vLLM, llama.cpp, LM Studio, GPT4All).
- Share paths for Mistral, Qwen, Perplexity, Meta AI, Kimi, Manus, Poe, Character.ai — no stable public share path.
- Copilot Studio no-auth agents — detected in-tenant with Microsoft's Advanced Hunting query, not from outside.

## [1.3.0] — 2026-06-16 — Verification Refresh + `KEYWORD` Convention

### Changed (breaking, intentional)
- **All ~400 dorks and queries across Google, GitHub, Shodan, and Censys now use a `KEYWORD` placeholder** (or a native scope filter: `org:`, `site:`, `hostname:`, `net:`, `autonomous_system.organization`) in place of hard-coded secret-seeking value strings.
- Service fingerprints (product titles, API paths, ports, env-var names, key prefixes) are intentionally **kept** — they identify the service/format, not a victim's secret.
- README opens with a new **"`KEYWORD` Convention — Read This First"** section.
- CONTRIBUTING makes the `KEYWORD` convention mandatory for new dorks.

### Verified / Corrected (June 2026 refresh)
- **Grok** `site:grok.com/share` — re-confirmed 🟢 still broadly indexed.
- **ChatGPT** `site:chatgpt.com/share` — kept 🟡 **degraded**; de-indexing ongoing since the Aug 2025 feature removal, but cached/third-party-archived copies persist and spot checks still return occasional live results. Bing/DuckDuckGo may retain more than Google.
- **HuggingFace Spaces** — re-confirmed 🟢 active.
- **GitHub syntax** — re-confirmed web Code Search uses `path:`; legacy `filename:` survives only via REST API v3.
- **ChromaDB** — re-confirmed `/api/v2`, port 8000, no auth by default, binds localhost.
- **Default ports & key prefixes** — re-verified against official docs.

### Notes
- Content scope (CVEs, threat-intel, tools, Sigma rules) carried forward unchanged from v1.2.0; this release is a parameterization + verification refresh, not a content expansion.
- A `KEYWORD_BANK.md` of the previous secret-seeking terms was preserved out-of-tree for upcoming tooling work (not published in the repo).

---

## [1.2.0] — 2026-04
- MCP systemic RCE (Ox Security, 10+ CVEs), Claude Code source-map leak, ChatGPT DNS exfiltration, GitHub Copilot wormable RCE (CVE-2025-53773), nginx-ui MCPwn (CVE-2026-33032), DeepSeek ClickHouse exposure, 300K+ ChatGPT creds, additional exposed Ollama instances, Mythos/Glasswing.

## [1.0.0] — 2026-04
- Initial public release.
