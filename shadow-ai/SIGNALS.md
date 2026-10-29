# Shadow AI External Signals — queries by surface

Replace `DOMAIN`, `ORGNAME`, `ASN`, `NET`, `GH_ORG`, `GH_USER`, `KEYWORD` with the scoped values from `README.md`. Never run a query without a scope.

---

## S1 — Self-hosted AI on owned infrastructure (Shodan / Censys)

Fingerprints are banner- or software-based, never port-only: more than 25% of exposed Ollama instances run on non-default ports, and bare ports are dominated by unrelated services.

| ID | Product | Shodan | Censys Platform | Context |
|---|---|---|---|---|
| S1-01 | **Ollama** | `"Ollama" port:11434 asn:ASN` · `"Ollama" ssl.cert.subject.cn:DOMAIN` | `host.services: (endpoints.endpoint_type: "OLLAMA") and host.autonomous_system.asn: ASN` | 175K hosts over 293 days (SentinelLABS/Censys); 18.8% actively serving models (Cisco Talos) |
| S1-02 | **MCP servers** | — (protocol-level; use Censys) | `web.endpoints.endpoint_type: "MCP" and host.autonomous_system.asn: ASN` | 12,520 → 21,000+ services (Censys ARC, Apr–May 2026); ~90 expose `run_command`/`shell_exec` tools |
| S1-03 | **n8n** | `http.title:"n8n.io - Workflow Automation" asn:ASN` | `(host.services: (software.product: "n8n") or web.software: (product: "n8n")) and host.autonomous_system.asn: ASN` | CVE-2026-21858 Ni8mare, CVSS 10.0 — 26,512 vulnerable hosts (Censys) |
| S1-04 | **Langflow** | `http.title:"Langflow" asn:ASN` | `web.software: (vendor: "Langflow" and product: "Langflow") and host.autonomous_system.asn: ASN` | CVE-2025-3248, CISA KEV — 1,156 exposed (Censys); CVE-2026-5027 ~7,000 |
| S1-05 | **Open WebUI** | `http.title:"Open WebUI" asn:ASN` | `web.software: (product: "Open WebUI") and host.autonomous_system.asn: ASN` | CVE-2025-64496 (account takeover via Direct Connections) |
| S1-06 | **Flowise** | `http.title:"Flowise" asn:ASN` | `web.software: (product: "Flowise") and host.autonomous_system.asn: ASN` | CVE-2025-26319 pre-auth upload, exploited in the wild |

Swap `asn:ASN` for `net:NET`, `org:"ORGNAME"` or `ssl.cert.subject.cn:DOMAIN` to cover on-prem and cloud-hosted assets. Run all scopes; they overlap rarely.

**Not included by design:** LiteLLM and ComfyUI (scan results are dominated by honeypots), and products with no banner fingerprint (vLLM, llama.cpp, LM Studio, GPT4All, Dify, AnythingLLM, LibreChat, Jan, LocalAI, Langfuse, SD-WebUI, Ray, Triton, MLflow). A port-only match is not a finding.

---

## S2 — Certificate Transparency (crt.sh + Cert Spotter)

One query per domain and per source, merged and filtered locally. crt.sh often returns 502 under load; Cert Spotter covers the gap.

```
https://crt.sh/?q=%25.DOMAIN&output=json
https://api.certspotter.com/v1/issuances?domain=DOMAIN&include_subdomains=true&expand=dns_names
```

| Tier | Labels in the subdomain | Use |
|---|---|---|
| Product names | `ollama` `n8n` `flowise` `langflow` `openwebui` `open-webui` `litellm` `mcp` `dify` `langfuse` `anythingllm` `librechat` `comfyui` `jupyter` `mlflow` `ray` `vllm` | Report. Cross-reference with S1 under `ssl.cert.subject.cn:DOMAIN`: name + banner = confirmed exposure; name alone = intent |
| Generic | `ai` `gpt` `llm` `chat` `bot` `assistant` `agent` `copilot` | Context only — support chat, pre-LLM bots and "agent" in other senses produce noise |

`scripts/shadow_ai_footprint.py` implements this.

---

## S3 — AI-agent configuration in public code (GitHub Code Search)

Requires a signed-in session (`gh auth login`). Scope with `org:GH_ORG` or `user:GH_USER`. GitGuardian counted 24,008 secrets inside MCP configuration files in 2025, and Claude Code co-authored commits leak secrets at 3.2% vs. a 1.5% human baseline.

| ID | Artifact | Query | Reveals |
|---|---|---|---|
| S3-01 | MCP config (generic) | `org:GH_ORG path:**/mcp.json` | MCP servers wired to agents, often internal hosts |
| S3-02 | Cursor MCP | `org:GH_ORG path:.cursor/mcp.json` | Cursor + MCP targets |
| S3-03 | Claude Desktop | `org:GH_ORG filename:claude_desktop_config.json` | Claude Desktop + MCP targets |
| S3-04 | Claude Code | `org:GH_ORG path:CLAUDE.md` · `org:GH_ORG path:.claude/settings.json` | Claude Code adoption, allowed tools, hooks |
| S3-05 | Codex / generic agents | `org:GH_ORG path:AGENTS.md` | Codex and multi-agent tooling |
| S3-06 | Gemini CLI | `org:GH_ORG path:GEMINI.md` | Gemini CLI adoption |
| S3-07 | GitHub Copilot | `org:GH_ORG path:.github/copilot-instructions.md` | Copilot customization (often sanctioned — check) |
| S3-08 | IDE agent rules | `org:GH_ORG path:.cursorrules` · `path:.cursor/rules` · `path:.windsurfrules` · `path:.clinerules` | Cursor / Windsurf / Cline in use |
| S3-09 | Aider / Continue | `org:GH_ORG path:.aider.conf.yml` · `path:.continue/config.json` | Model endpoints configured |
| S3-10 | AI keys in env | `org:GH_ORG path:*.env "ANTHROPIC_API_KEY"` · `"OPENAI_API_KEY"` · `"GEMINI_API_KEY"` · `"N8N_ENCRYPTION_KEY"` | Unsanctioned API consumption. Report existence; never extract values |

Repeat every row with `user:GH_USER` for employees found through public org membership or `@DOMAIN` commit emails. Personal repositories are personal data — attribute, don't dump.

`gh` form: `gh search code --owner GH_ORG --filename mcp.json --json repository,path`

---

## S4 — Chat shares referenced on third-party sites (Google)

Share hosts carry `noindex` or are robots-blocked, so `site:` against them is unreliable. The durable form is the **quoted literal of the canonical share-URL prefix**, which finds share links employees posted on forums, LinkedIn, Medium, Reddit and blogs.

| ID | Provider | Query |
|---|---|---|
| S4-01 | ChatGPT | `"chatgpt.com/share/" "ORGNAME"` |
| S4-02 | Claude chats | `"claude.ai/share/" "ORGNAME"` |
| S4-03 | Claude artifacts | `"claude.ai/public/artifacts/" "ORGNAME"` |
| S4-04 | Gemini (chats and Gems) | `"gemini.google.com/share/" "ORGNAME"` · `"g.co/gemini/share" "ORGNAME"` |
| S4-05 | Grok | `"grok.com/share/" "ORGNAME"` |
| S4-06 | Copilot (consumer) | `"copilot.microsoft.com/shares/" "ORGNAME"` |
| S4-07 | DeepSeek | `"chat.deepseek.com/share/" "ORGNAME"` · `"chat.deepseek.com/a/chat" "ORGNAME"` |

Run a second pass replacing `"ORGNAME"` with a product name, an internal project name and `DOMAIN`. Counts are low by nature; one hit is one incident.

**Not included by design:** Microsoft 365 Copilot Chat shares (tenant-scoped, never public) and providers whose share path is not stable (Mistral, Qwen, Perplexity, Meta AI, Kimi, Manus, Poe, Character.ai).

---

## S5 — Employee-built AI apps (Google)

| ID | Platform | Query | Context |
|---|---|---|---|
| S5-01 | Lovable | `site:lovable.app "ORGNAME"` | CVE-2025-48757: 10.3% of sampled apps exposed data through missing Supabase RLS. Brand match only — never probe the backend |
| S5-02 | Custom GPTs | `site:chatgpt.com inurl:/g/ "ORGNAME"` | Store listings branded with the company name |

Copilot Studio agents are detected in-tenant with Microsoft's Advanced Hunting query (see `INTERNAL_ANNEX.md`), not from outside.
