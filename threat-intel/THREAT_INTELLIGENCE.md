# AI Security Threat Intelligence

## Active Threats & Campaigns (2025-2026)

---

### 1. Operation Bizarre Bazaar — Large-Scale LLMjacking

**Period:** December 2025 — January 2026
**Source:** Pillar Security Research Team
**Stats:** 35,000 attack sessions, 972/day average

Systematic campaign targeting exposed LLM and MCP endpoints. Three-actor supply chain: scanner infrastructure → endpoint validation → commercial resale via `silver.inc` marketplace on Discord/Telegram.

**Targets:** Ollama (port 11434), OpenAI-compatible APIs (port 8000), MCP servers, production chatbots — all without authentication or rate limiting.

**Impact:** Victims losing $46,000–$100,000/day in unauthorized inference charges. Access to 30+ LLM providers resold at 40-60% discount.

**MITRE ATT&CK:** T1190, T1496, T1530

---

### 2. OpenClaw/Clawdbot Shodan Exposure

**Period:** January 24-25, 2026 (peak)
**CVE:** CVE-2026-24061 ("Localhost Trust")
**Sources:** Penligent, SlowMist, Flare

4,000+ instances on Shodan, 923 with zero authentication. Flare reported 312,000+ on default port with 30,000+ compromised. The "Localhost Trust" vulnerability assumed any request from 127.0.0.1 was the owner — exploitable behind reverse proxies with improper header validation.

**Attack chain:** Shodan discovery → health endpoint check → identify `auth_mode: none` → read `.env` via `fs_read` tool → steal API keys → execute reverse shell via `python_repl`

**MITRE ATT&CK:** T1190, T1059, T1552.001, T1133

---

### 3. 175,000 Exposed Ollama Servers

**Period:** Ongoing (definitive study Jan 2026)
**Source:** SentinelOne SentinelLABS + Censys (293-day study)

175,108 unique hosts across 130 countries and 4,032 autonomous systems. ~48% have tool-calling capabilities. ~23,000 persistent hosts (13%) generate 76% of observations with 87% average uptime. 201+ running "uncensored" configurations with safety guardrails removed.

**Timeline:** Wiz found 1,000 (Jun 2024) → Cisco Talos 1,100 (Sep 2025) → FuzzingLabs 270,988 (Jul 2025) → SentinelOne 175,108 verified (Jan 2026)

**Root cause:** Ollama ships with zero authentication by default.

---

### 4. ChatGPT & Grok Conversation Indexing

**ChatGPT:** ~4,500 conversations indexed by Google via "Make this chat discoverable" toggle. Contained API keys, source code, PII, PHI-like data, infrastructure details. OpenAI CISO removed feature Aug 1, 2025.

**Grok (xAI):** 370,000+ conversations indexed. NO opt-out mechanism. xAI FAQ states shared links "may be subject to indexing by a search engine." Still active as of April 2026. Exposed passwords, medical queries, and worse.

**DuckDuckGo** continued surfacing ChatGPT results after Google de-indexed them, making it the primary engine for this content.

---

### 5. MCP Supply Chain Attack Timeline

| Date | Incident | Impact |
|---|---|---|
| Mid-2025 | WhatsApp MCP tool poisoning (Invariant Labs) | Full WhatsApp history exfiltration |
| 2025 | Smithery Registry path traversal (GitGuardian) | Fly.io token → control of 3,000+ MCP servers |
| 2025 | mcp-remote CVE-2025-6514 (JFrog) | RCE on 437K+ installs |
| 2025 | Postmark MCP supply chain compromise | Email traffic exfiltration |
| 2025 | Grafana MCP server default bind 0.0.0.0 | Unauthenticated dashboard control |
| 2025 | Cursor IDE MCP trust issue (<=1.2.4) | Persistent RCE (CVSS 7.2-8.8) |
| 2025 | Jira MCP prompt injection | JWT token exfiltration |
| 2025 | Neo4j MCP DNS rebinding (0.2.2-0.3.1) | Database takeover (CVSS 7.4) |
| 2026 | Claude Code CVE-2025-59536 | Arbitrary code execution via hooks |
| 2026 | Claude Code CVE-2026-21852 | API key exfiltration during project load |

**Scale:** 24,008 unique secrets exposed in MCP configs in its first year (GitGuardian 2026).

---

### 6. AI Credential Leak Explosion

**Source:** GitGuardian State of Secrets Sprawl 2026

- AI-service credential leaks surged **81% YoY** to 1,275,105
- 29 million total secrets found on public GitHub in 2025
- Claude Code-assisted commits leaked at **3.2%** — double the 1.5% human baseline
- **64% of secrets from 2022 were still valid/unrevoked** in 2026

---

### 7. AI-Assisted Critical Infrastructure Targeting

**Period:** February-March 2026
**Source:** CloudSEK

Following Feb 28, 2026 Iran-US escalation, 60+ Iranian-aligned hacktivist groups used AI tools (LLMs) to generate Shodan queries for exposed ICS devices, analyze SCADA interfaces, and identify vulnerabilities — without prior ICS expertise. Combined with 40,000+ internet-exposed US control systems.

---

### 8. Claude Conversation Indexing & Archive Exposure

**Period:** September 2025 — ongoing
**Sources:** Forbes, Obsidian Security, Geol.ai

~600 Claude conversations indexed by Google despite Anthropic claiming to block crawlers and not provide sitemaps. Forbes reported conversations contained staff names, emails, internal tasks, and excerpts of uploaded documents.

Separately, security researcher dead1nfluence discovered **143,000+ LLM conversations** (including Claude, ChatGPT, Copilot, Grok, Mistral, Qwen) publicly accessible on **Archive.org** via the Wayback Machine CDX API. Exposed content included AWS Access Key IDs and a Replicate API token.

**Enumeration technique:**
```bash
curl "https://web.archive.org/cdx/search/cdx?url=claude.ai/share/*&output=json&limit=10000"
```

**Key details:**
- Published Claude artifacts (Free/Pro/Max plans) are fully public web pages — indexable by default
- Team/Enterprise artifacts can only be shared within the organization
- Anthropic changed its privacy policy in Sep 2025 to use chats for training unless users opt out

---

### 9. "Claudy Day" — Triple Vulnerability Chain in Claude.ai

**Date:** March 19, 2026 (disclosed)
**Source:** Oasis Security
**Status:** Fixed by Anthropic

Three vulnerabilities chained for a complete attack pipeline — targeted delivery → invisible prompt injection → silent data exfiltration:

1. **Open Redirect on claude.com** — `claude.com/redirect/<target>` redirected without validation, including to attacker-controlled domains. Combined with Google Ads for precision targeting by location, industry, or even specific email addresses.

2. **Prompt Injection via pre-filled prompts** — Hidden instructions injected into Claude sessions instructing it to search conversation history and memory for sensitive data.

3. **Data Exfiltration via Anthropic Files API** — Claude's sandbox blocks outbound network but allows `api.anthropic.com`. Attacker embeds their own API key in the prompt, Claude writes victim data to a file and uploads it to the attacker's Anthropic account via the Files API.

**Impact:** In basic sessions: conversation history, memory, business strategy, health data, PII. With MCP/integrations enabled: file access, messaging, API interactions on behalf of the victim.

---

### 10. Claude Code Source Map Leak — 512,000 Lines Exposed

**Date:** March 30-31, 2026
**Sources:** Penligent, TechRadar
**Package:** @anthropic-ai/claude-code v2.1.88

Anthropic's npm-distributed CLI exposed a `.map` file (source map) enabling outsiders to reconstruct readable TypeScript source. Multiple public GitHub mirrors appeared within hours claiming 512,000 lines reconstructed from `cli.js.map`. An `r2.dev/src.zip` path was also reported as publicly accessible.

**Also in March 2026:**
- **ShadowPrompt** (Koi Security, Mar 27) — Zero-click attack via Claude Code Chrome extension enabling data exfiltration
- **CVE-2025-59536** — Arbitrary code execution through malicious project hooks
- **CVE-2026-21852** — API key exfiltration during project-load flow

---

## Key CVEs

| CVE | Product | Description | CVSS |
|---|---|---|---|
| CVE-2026-24061 | OpenClaw | Localhost Trust bypass | Critical |
| CVE-2026-25253 | OpenClaw | WebSocket hijacking | High |
| CVE-2026-0545 | MLflow | Unauthenticated RCE via FastAPI jobs | 9.1 |
| CVE-2025-59536 | Claude Code | Code execution via malicious hooks | High |
| CVE-2026-21852 | Claude Code | API key exfiltration during project load | High |
| CVE-2025-6514 | mcp-remote | OS command injection | Critical |
| CVE-2024-37032 | Ollama | RCE "Probllama" | High |
| CVE-2025-64513 | Milvus | Auth bypass via forged headers | Critical |
| CVE-2023-1177 | MLflow | Arbitrary file read | 10.0 |
| Claudy Day | claude.ai | Open redirect + prompt injection + Files API exfil chain | High |
| ShadowPrompt | Claude Code Chrome ext | Zero-click data exfiltration | High |
| Source Map Leak | Claude Code v2.1.88 | 512K lines exposed via npm .map file | Medium |

---

## References

- [SentinelOne — 175K Ollama Hosts](https://www.securityweek.com/175000-exposed-ollama-hosts-could-enable-llm-abuse/)
- [AuthZed — MCP Breaches Timeline](https://authzed.com/blog/timeline-mcp-breaches)
- [GitGuardian — State of Secrets Sprawl 2026](https://blog.gitguardian.com/the-state-of-secrets-sprawl-2026/)
- [Penligent — Clawdbot Post-Mortem](https://www.penligent.ai/hackinglabs/clawdbot-shodan-technical-post-mortem-and-defense-architecture-for-agentic-ai-systems-2026/)
- [Forbes — Claude Conversations in Google Search](https://www.forbes.com/sites/iainmartin/2025/09/08/hundreds-of-anthropic-chatbot-transcripts-showed-up-in-google-search/)
- [Obsidian Security — 143K LLM Chats on Archive.org](https://www.obsidiansecurity.com/resource/143k-claude-copilot-chatgpt-chats-publicly-accessible-were-you-exposed)
- [Oasis Security — Claudy Day Vulnerabilities](https://www.oasis.security/blog/claude-ai-prompt-injection-data-exfiltration-vulnerability)
- [TechRadar — Claude Code 512K Source Leak](https://www.techradar.com/pro/security/anthropic-confirms-it-leaked-512-000-lines-of-claude-code-source-code-spilling-some-of-its-biggest-secrets)
- [Penligent — Source Map Leak Analysis](https://www.penligent.ai/hackinglabs/claude-code-source-map-leak-what-was-exposed-and-what-it-means/)
- [vulnerablemcp.info](https://vulnerablemcp.info/)
- [OWASP Top 10 for LLMs 2025](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [MITRE ATLAS](https://atlas.mitre.org/)
