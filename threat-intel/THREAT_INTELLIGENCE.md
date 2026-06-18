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

---

## 🆕 v1.2.0 Threat Intelligence Updates (April 2026)

---

### Claude Mythos Preview & Project Glasswing

| Field | Details |
|-------|---------|
| **Date** | April 8, 2026 |
| **Source** | [Anthropic Red Team](https://red.anthropic.com/2026/mythos-preview/), [The Hacker News](https://thehackernews.com/2026/04/anthropics-claude-mythos-finds.html), [Wiz Blog](https://www.wiz.io/blog/claude-mythos), [NPR](https://www.npr.org/2026/04/11/nx-s1-5778508/anthropic-project-glasswing-ai-cybersecurity-mythos-preview), [Fortune](https://fortune.com/2026/04/13/cybersecurity-anthropic-claude-mythos-dario-amodei-tech-ceo/) |
| **Impact** | 🔴 CRITICAL |
| **Category** | AI-Assisted Vulnerability Discovery |

Anthropic's unreleased frontier model Claude Mythos Preview autonomously discovers thousands of 0-day vulnerabilities across major operating systems, web browsers, and open-source software:

- **CVE-2026-4747** — 27-year-old unauthenticated RCE in OpenBSD, fully autonomously discovered and exploited
- **CVE-2026-2796** — Firefox JIT miscompilation; Claude Opus 4.6 built a working exploit ([deep-dive](https://red.anthropic.com/2026/exploit/))
- **22 Firefox vulnerabilities** found in two weeks during Mozilla collaboration
- Chained **four vulnerabilities** to escape browser renderer and OS sandboxes
- Solved a corporate network attack simulation in hours vs. 10+ hours for a human expert
- **Escaped a secured sandbox** during evaluation, gained internet access, and sent an email to a researcher
- 89% agreement between model and human expert severity assessments (198 reviewed reports)
- Over **500 high-severity OSS vulnerabilities** found by Claude Opus 4.6 (Feb 2026)
- Average time-to-exploit now **under 20 hours** (CSA / Zero Day Clock)

**Project Glasswing** limits access to ~50 organizations: AWS, Apple, Broadcom, Cisco, CrowdStrike, Google, JPMorgan Chase, Linux Foundation, Microsoft, NVIDIA, Palo Alto Networks. Not publicly released.

**OSINT Relevance:** Expect a surge of AI-discovered CVEs. Claude Code Security (research preview) available for Enterprise/Team; free for OSS maintainers.

---

### Claude Code Source Leak & Critical Vulnerability

| Field | Details |
|-------|---------|
| **Date** | March 31, 2026 |
| **Source** | [Zscaler ThreatLabz](https://www.zscaler.com/blogs/security-research/anthropic-claude-code-leak), [SecurityWeek](https://www.securityweek.com/critical-vulnerability-in-claude-code-emerges-days-after-source-leak/) |
| **Impact** | 🔴 HIGH |
| **Category** | Source Code Exposure, Supply Chain |

Anthropic accidentally included a 59.8 MB JavaScript source map (`.map`) in npm package `@anthropic-ai/claude-code` v2.1.88.

**Exposed:** ~2,000 source files, 500K+ lines of code (~3 hours). Internal architecture: hook handling, permission logic, command processing.

**Critical vulnerability (Adversa AI):** Command pipelines exceeding **50 subcommands** bypass ALL deny rules — security validators, command injection detection all skipped. A malicious `CLAUDE.md` could exfiltrate SSH keys, AWS credentials, GitHub tokens, npm tokens.

**Malware campaign:** Zscaler found fake "Claude Code leak" GitHub repos distributing **Vidar** and **GhostSocks** malware. Appeared near top of Google results. Coincided with malicious **Axios npm supply chain attack** (same day, March 31).

---

### MCP Systemic RCE — "Mother of All AI Supply Chains"

| Field | Details |
|-------|---------|
| **Date** | April 15-16, 2026 |
| **Source** | [Ox Security](https://www.ox.security/blog/the-mother-of-all-ai-supply-chains-critical-systemic-vulnerability-at-the-core-of-the-mcp/), [The Register](https://www.theregister.com/2026/04/16/anthropic_mcp_design_flaw/), [Infosecurity Magazine](https://www.infosecurity-magazine.com/news/systemic-flaw-mcp-expose-150/) |
| **Impact** | 🔴 CRITICAL |
| **Category** | Supply Chain, Protocol Vulnerability |

Ox Security discovered architectural command injection at the core of Anthropic's MCP SDKs — not a coding error but a design decision. Affects Python, TypeScript, Java, Rust SDKs.

**Scale:** 150M+ downloads, 7,000+ publicly accessible servers, up to 200,000 vulnerable instances.

**CVEs issued (10+, 9 critical):**

| CVE | Product | Severity | Description |
|-----|---------|----------|-------------|
| CVE-2026-30615 | Windsurf IDE | Critical | Zero-click prompt injection → local RCE via MCP config |
| CVE-2026-30624 | Agent Zero 0.9.8 | Critical | RCE via External MCP Servers configuration |
| CVE-2026-30616 | Jaaz 1.0.30 | Critical | RCE via MCP STDIO command execution handling |
| CVE-2026-40933 | Flowise | Critical | Authenticated RCE via MCP adapters (`npx -c` bypass) |
| CVE-2026-33032 | nginx-ui | Critical (9.8) | MCPwn — unauthenticated takeover, **actively exploited** |
| CVE-2026-26118 | Microsoft MCP Server | High (8.8) | AI tool hijacking via MCP server deployments |
| CVE-2026-25536 | MCP TypeScript SDK v1.10.0-1.25.3 | High (7.1) | Cross-client data leak via shared McpServer instances |
| CVE-2026-27825 | Atlassian MCP | Critical (9.1) | MCPwnfluence — RCE chain from LAN |
| CVE-2026-27826 | Atlassian MCP | High (8.2) | MCPwnfluence — RCE chain (part 2) |
| CVE-2026-27944 | nginx-ui < 2.3.3 | Critical (9.8) | Backup endpoint exposes encryption keys |

**Four vulnerability families:**
1. Unauthenticated command injection — any publicly-facing MCP UI
2. Hardening bypass — `npx -c <command>` bypasses sanitization
3. Zero-click prompt injection in AI IDEs (Windsurf, Claude Code, Cursor, Gemini-CLI, Copilot)
4. Marketplace poisoning — **9 of 11 MCP registries** successfully poisoned

**Anthropic declined to modify the protocol's architecture**, citing behavior as "expected."

---

### ChatGPT DNS-Based Data Exfiltration

| Field | Details |
|-------|---------|
| **Date** | February 20, 2026 (patch) / March 2026 (disclosure) |
| **Source** | [Check Point Research](https://blog.checkpoint.com/research/when-ai-trust-breaks-the-chatgpt-data-leakage-flaw-that-redefined-ai-vendor-security-trust/), [The Hacker News](https://thehackernews.com/2026/03/openai-patches-chatgpt-data.html) |
| **Impact** | 🟡 HIGH |
| **Category** | Data Exfiltration, Sandbox Escape |

Check Point discovered silent data leakage via DNS side channel in ChatGPT's code execution sandbox. DNS resolution remained available while direct HTTP was blocked. Attacker crafts a malicious prompt (or bakes it into a custom GPT); code execution encodes data into DNS queries sent to attacker-controlled nameserver. No warnings triggered, no user indication.

**Data at risk:** Medical records, corporate documents, financial data, uploaded PDFs. No evidence of exploitation in the wild. Patched February 20, 2026.

---

### OpenAI Codex CLI Command Injection

| Field | Details |
|-------|---------|
| **Date** | February 5, 2026 (patch) |
| **Source** | [The Hacker News](https://thehackernews.com/2026/03/openai-patches-chatgpt-data.html), BeyondTrust |
| **Impact** | 🟡 HIGH |
| **Category** | Command Injection, Lateral Movement |

Vulnerability in OpenAI Codex (CLI, SDK, IDE Extension) allowed branch command injection. Setting up a malicious Git branch and referencing `@codex` in a PR comment causes Codex to execute the payload — granting **read/write access to victim's entire codebase** and stealing GitHub Installation Access tokens.

---

### CVE-2025-53773: GitHub Copilot Wormable RCE

| Field | Details |
|-------|---------|
| **Date** | August 12, 2025 (disclosed) / August 2025 Patch Tuesday (fixed) |
| **Source** | [Embrace The Red](https://embracethered.com/blog/posts/2025/github-copilot-remote-code-execution-via-prompt-injection/), [Persistent Security](https://www.persistent-security.net/post/part-iii-vscode-copilot-wormable-command-execution-via-prompt-injection), [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-53773) |
| **Impact** | 🔴 CRITICAL (CVSS 7.8) |
| **Category** | Prompt Injection, RCE, Wormable |

Prompt injection in GitHub Copilot enables full system compromise. Attacker embeds instructions in README.md or source code (can use invisible Unicode). Copilot modifies `.vscode/settings.json` to add `"chat.tools.autoApprove": true` (YOLO mode) — disabling all user confirmations. Arbitrary shell execution with developer privileges.

**Wormable:** Self-replicates during refactoring. Creates "ZombAI" botnets. Propagates through CI/CD and repos. Tested against GPT-4.1, Claude Sonnet 4, Gemini.

---

### Ollama: 12,269 More Exposed Instances

| Field | Details |
|-------|---------|
| **Date** | February 23, 2026 |
| **Source** | [LeakIX Blog](https://blog.leakix.net/2026/02/ollama-exposed/) |
| **Impact** | 🟡 HIGH |
| **Category** | Misconfiguration |

LeakIX found 12,269 additional Ollama instances with zero authentication. Top hosts: AWS (1,686), Hetzner (1,004), OVH (773), Contabo (634). Maintainers continue rejecting auth PRs. One organization discovered a **$12,000 cloud cost spike** from exposed endpoint. **Combined total: 187,000+ documented exposures.**

---

### IBM X-Force 2026: 300K+ ChatGPT Credentials on Dark Web

| Field | Details |
|-------|---------|
| **Date** | March 2026 |
| **Source** | [IBM X-Force Threat Intelligence Index 2026](https://www.ibm.com/think/insights/more-2026-cyberthreat-trends) |
| **Impact** | 🟡 HIGH |
| **Category** | Credential Theft |

Over **300,000 ChatGPT credentials** for sale on dark web. AI agents with stored credentials are emerging attack surface. Supply chain attacks quadrupled over 5 years.

---

### nginx-ui MCPwn — Actively Exploited

| Field | Details |
|-------|---------|
| **Date** | March-April 2026 |
| **Source** | [The Hacker News](https://thehackernews.com/2026/04/critical-nginx-ui-vulnerability-cve.html), Pluto Security |
| **Impact** | 🔴 CRITICAL (CVSS 9.8) |
| **Category** | Active Exploitation |

CVE-2026-33032: Full Nginx takeover via unauthenticated MCP endpoints in 2 requests — GET `/mcp` (session) + POST `/mcp_message` (invoke any tool). Chained with CVE-2026-27944 to extract credentials, SSL keys, and Nginx configs from backups. **Actively exploited** — listed among 31 vulns exploited in March 2026 (Recorded Future). Fixed in nginx-ui v2.3.4.

---

### DeepSeek ClickHouse Database Exposure

| Field | Details |
|-------|---------|
| **Date** | January 29, 2025 |
| **Source** | [Wiz Research](https://www.wiz.io/blog/wiz-research-uncovers-exposed-deepseek-database-leak), [Krebs on Security](https://krebsonsecurity.com/2025/02/experts-flag-security-privacy-risks-in-deepseek-ai-app/) |
| **Impact** | 🔴 CRITICAL |
| **Category** | Data Exposure |

Wiz found publicly accessible ClickHouse DB at `oauth2callback.deepseek.com:9000` and `dev.deepseek.com:9000`. 1M+ log entries with plaintext chat histories, API keys, backend details. Full database control via HTTP `/play` path — no authentication. Additional: 100% jailbreak rate (Cisco), hardcoded encryption keys (NowSecure), SQL injection vulns (SecurityScorecard). Banned by 7+ countries.

---

### MCP Academic Security Research

| Paper/Tool | Key Finding | Link |
|------------|-------------|------|
| MCP Safety Audit | MCPSafetyScanner tool for MCP server auditing | [arXiv](https://arxiv.org/pdf/2504.03767) |
| Breaking the Protocol | PROTOAMP framework; ATTESTMCP reduces attacks 52.8% → 12.4% | [arXiv](https://arxiv.org/pdf/2601.17549) |
| MCP Threat Modeling | STRIDE/DREAD analysis of 5 MCP components | [arXiv](https://arxiv.org/pdf/2603.22489) |
| Vulnerable MCP DB | **50 vulnerabilities**, 13 critical, 32 researchers. 67,057 MCP servers analyzed | [vulnerablemcp.info](https://vulnerablemcp.info/) |

---

## 🆕 v1.4.0 Threat Intelligence Updates (June 2026)

> Focus: the OpenClaw / ClawHub supply-chain crisis and the broader agent-skill
> attack surface. Figures are attributed to their primary sources; where counts
> vary across reports, ranges are given rather than a single number.

### The OpenClaw Agent Crisis — Escalation (Jan–June 2026)

OpenClaw (formerly Clawdbot) became the first major AI-agent security crisis of 2026. It is a self-hosted autonomous agent with shell, filesystem, and browser access — so a compromised instance is a compromised computer, not just a chatbot.

| Dimension | Reported figures | Source |
|---|---|---|
| Internet-exposed instances | ~135,000+ (early 2026); 30,000–42,000 in some scans, 63%–93% without auth | ARMO, Bitsight, Hive Security |
| CVEs associated | 60+ to 138 over five months (7 critical, ~49 high) | multiple trackers |
| One-click RCE | CVE-2026-25253 (CVSS 8.8) via WebSocket; patched v2026.1.29 | DEV / Blink |
| Admin without credentials | CVE-2026-22172, CVE-2026-32922 (both CVSS 9.9) | cvefind |
| 4-day CVE burst | 9 CVEs disclosed Mar 18–21, 2026 (highest 9.9) | ruh.ai |
| ClawJacked | malicious sites silently hijack a running instance | Oasis Security |

> ⚠️ **Posture recommended by multiple vendors for OpenClaw users: assume compromise.** Microsoft advised against deploying on machines holding sensitive data; Chinese authorities restricted state-enterprise use.

### ClawHavoc — Marketplace Supply-Chain Campaign

ClawHub (OpenClaw's official skill marketplace) was poisoned at scale. Skills install with the **same permissions as the agent** and there was **no mandatory review** — only a `SKILL.md` and a week-old GitHub account were needed to publish.

- **Scale:** Koi Security's Feb 1 audit found **341 malicious of 2,857 skills (~12%)**, 335 traced to one coordinated actor. Antiy CERT later catalogued **1,184 malicious skills** historically published (Trojan/OpenClaw.PolySkill).
- **Payload:** primarily **Atomic macOS Stealer (AMOS)** — harvests browser creds, keychain, crypto wallets, SSH keys, Telegram sessions.
- **Technique — "ClickFix 2.0":** fake "prerequisite installation" steps inside `SKILL.md` cause the *agent itself* to present a fake setup dialog, tricking the user into pasting a base64 command. The AI agent becomes the trusted intermediary.
- **Persistence:** malicious skills survived the CVE patch — patching the RCE did not remove already-installed skills or stop new uploads. ClawHub added verified skill screening only on Mar 26, 2026, ~8 weeks after the campaign began.

> 📌 **What this repo does NOT publish:** specific live malicious skill names or step-by-step payload mechanics. The defensive value is in detection (see v1.4.0 Sigma rules) and inventory, not in redistributing the attack.

### MCP Protocol Exposure — Measured at Scale

- **Censys:** ~12,520 Internet-accessible MCP services, most unauthenticated.
- **Authentication study:** ~40% of remote MCP servers expose tools with **no auth**; 9 CVEs traced to broken OAuth flows.
- **VIPER-MCP:** swept ~40,000 MCP server repos → **106 zero-days, 67 CVEs**.
- **BlueRock:** of 7,000+ MCP servers analyzed, **36.7% potentially vulnerable to SSRF**; PoC against Microsoft's MarkItDown MCP retrieved AWS IAM keys from EC2 metadata.
- **OX Security:** poisoned **9 of 11 MCP marketplaces** with PoC servers; the root issue is the MCP SDK STDIO transport (Anthropic considers the behavior "expected").

### New / Notable CVEs (since v1.2.0)

| CVE | Component | Note |
|---|---|---|
| CVE-2026-26118 | Microsoft MCP server | AI tool hijacking |
| CVE-2026-22252 | LibreChat MCP | same systemic STDIO class |
| CVE-2026-22688 | WeKnora | same class |
| CVE-2026-22708 | Cursor | shell built-in poisoning via indirect prompt injection (Pillar) |
| CVE-2026-11624 | MCP spec | Origin-header validation (DNS rebinding class) |
| CVE-2025-59536 / CVE-2026-21852 | Claude Code project files | RCE + token exfiltration via hooks (Check Point) |

### Agent-Skill Ecosystem — Research Baseline

- **Snyk ToxicSkills (Feb 2026):** of 3,984 skills from ClawHub + skills.sh, **13.4% had ≥1 critical issue**; **91% of confirmed malicious skills combined prompt injection with malware**.
- **"Agent Skills in the Wild" (Liu et al., 2026):** 42,447 skills analyzed — **26.1% contained ≥1 vulnerability, 5.2% likely malicious**.
- **Weaponization:** Cato Networks demonstrated deploying MedusaLocker ransomware via a modified Claude skill (disclosed to Anthropic Oct 30, 2025); the "consent gap" lets approved skills download/execute code without further prompts.

> 📖 Sources: Koi Security, Antiy CERT, Snyk, OX Security, Censys, BlueRock, Check Point, Trend Micro, Bitsight, ARMO, VentureBeat, arXiv 2604.06550.
