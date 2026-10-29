# Shadow AI External Footprint

> **What this section answers:** *"What unsanctioned AI is my organization already exposing to the public internet — without touching a single internal system?"*

Shadow AI is the use of AI tools, accounts, models or agents by employees outside the organization's visibility, policy and control. Most vendors sell it as an **inside** problem (proxy, CASB, endpoint). This section documents the part that is visible from **outside**, using only passive OSINT: public search indexes, internet-scan engines, certificate-transparency logs and public code.

Everything here follows the repository rules: `KEYWORD` placeholders, no live secret-harvesting regexes, and no interaction with discovered systems.

---

## Why it matters (sourced)

| Fact | Source |
|---|---|
| 20% of breached organizations reported a breach caused by shadow AI; high-shadow-AI orgs paid ~$670K more per breach | IBM Cost of a Data Breach 2025 |
| 47% of genAI users at work use personal, unmanaged accounts; 223 genAI data-policy violations per org per month on average | Netskope Cloud & Threat Report 2026 |
| 1,275,105 AI-service secrets leaked on public GitHub in 2025 (+81% YoY); 24,008 secrets inside MCP configuration files | GitGuardian State of Secrets Sprawl 2026 |
| 175,000 Ollama hosts exposed across 4,032 ASNs over 293 days | SentinelLABS + Censys, Jan 2026 |
| 12,520 → 21,000+ internet-exposed MCP services (Apr–May 2026) | Censys ARC |
| 26,512 n8n hosts vulnerable to Ni8mare (CVE-2026-21858, CVSS 10.0) | Censys advisory, Jan 2026 |
| 370,000+ Grok shared chats indexed by Google (Aug 2025); ~600 Claude chats (Sep 2025); 4,500+ ChatGPT shares (Jul 2025) | Forbes, Fast Company |

Links in [`SIGNALS.md`](SIGNALS.md) and `../resources/RESOURCES.md`.

---

## The five external surfaces

Each surface is independent. Correlating them per organization is what no public project does today.

| # | Surface | What it reveals | Primary engine | Weight |
|---|---|---|---|---|
| S1 | **Self-hosted AI on owned infrastructure** | Someone deployed Ollama / n8n / Langflow / MCP / Open WebUI on corporate IP space or under a corporate certificate | Shodan, Censys | 5 |
| S2 | **Certificate Transparency names** | Subdomains issued for AI products (`ollama.`, `n8n.`, `langflow.`, `mcp.`, `openwebui.`…) | crt.sh, Cert Spotter | 3 |
| S3 | **AI-agent configuration in public code** | Which AI coding tools and MCP servers employees run, and against which internal hosts | GitHub Code Search | 4 |
| S4 | **Chat shares referenced on third-party sites** | Employees pasted ChatGPT/Claude/Gemini/Grok share links on forums, LinkedIn, Medium, Reddit with the company name | Google (quoted literal) | 2 |
| S5 | **Employee-built AI apps** | Vibe-coded apps and Custom GPTs branded with the company name | Google | 2 |

### What is **not** visible from outside (say so in your report)

Private browser use of consumer accounts, installed extensions, prompts never shared. That is proxy/CASB/EDR territory — see [`INTERNAL_ANNEX.md`](INTERNAL_ANNEX.md), which only links existing public detections.

---

## Scoping to one organization

Every query takes the same inputs. Collect them first; never guess.

| Input | Example | How to obtain (passive) |
|---|---|---|
| `DOMAIN` | `example.com` | Known |
| `ORGNAME` | `"Example Corp"` | Exact registrant string as it appears in Shodan `org:` — check with `org:"Example"` facet first |
| `ASN` | `AS12345` | bgp.he.net, whois |
| `NET` | `203.0.113.0/24` | whois / RIR (LACNIC for LATAM) |
| `GH_ORG` | `example-corp` | GitHub org page |
| `GH_USERS` | `jdoe` | Public org members list; commit-author emails `@DOMAIN` |

**Scoping rule:** on-prem assets → `asn:`/`net:`; cloud-hosted assets presenting the corporate name → `ssl.cert.subject.cn:`/`hostname:`. Use both; `org:` alone misses cloud.

---

## Scoring model (per finding)

```
score = surface_weight × attribution × sanction
```

| Factor | Values |
|---|---|
| `surface_weight` | from the table above (S1 = 5, S3 = 4, S2 = 3, S4 = 2, S5 = 2) |
| `attribution` | 1.0 = owned ASN / corporate cert / org repo · 0.6 = employee personal repo or post · 0.3 = name match only |
| `sanction` | 1.0 = tool not in the org's published stack · 0.0 = tool is sanctioned (vendor customer story, official job posting, public policy) |

Report **Shadow AI Footprint = Σ score**, grouped by surface, with the sanctioned-use subtraction shown explicitly. Vendor customer stories (OpenAI, Anthropic, Microsoft) are *not* Shadow AI — they tell you what to subtract.

---

## Hard boundaries (read before running anything)

Passive means **querying third-party indexes only**. The following are active interaction with someone else's system and are **out of scope** for this repository and, in Colombia, may fall under Ley 1273/2009 art. 269A (acceso abusivo a un sistema informático):

- Sending prompts to a discovered endpoint
- Calling `/api/tags`, `/object_info`, `/v1/models` or any API path on a discovered host
- Trying default keys (e.g., LiteLLM `sk-1234`)
- Reading Supabase tables behind a vibe-coded app
- Opening discovered share links beyond confirming they exist in the index
- Resolving DNS names you enumerated from CT logs against the target

Findings that include credentials go to the affected organization through coordinated disclosure. *This is not legal advice.*

---

## Files

| File | Purpose |
|---|---|
| `SIGNALS.md` | All queries by surface, with context and expected noise |
| `INTERNAL_ANNEX.md` | Links to public internal detections (Splunk, Microsoft Defender, Sigma) — no duplication |
| `scripts/shadow_ai_footprint.py` | Passive collector: crt.sh + Cert Spotter + GitHub Code Search + optional Shodan facets → Markdown report |
| `scripts/README.md` | Setup and usage |
