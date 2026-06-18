# AI OSINT — Tools & Frameworks

> **AI-specific only.** Generic OSINT tools (Shodan, Censys, etc.) → [cloud_osint](https://github.com/7WaySecurity/cloud_osint).
> Every link verified April 2026.

---

## LLM Vulnerability Scanners

| Tool | Description | By | Link |
|---|---|---|---|
| **Garak** | "nmap for LLMs" — probes for hallucination, data leakage, prompt injection, jailbreaks, toxicity. 4.7k+ ⭐ | NVIDIA | [GitHub](https://github.com/NVIDIA/garak) |
| **promptfoo** | LLM pentesting CLI. 133+ attack plugins, OWASP/MITRE mapping, CI/CD integration. Now part of OpenAI. 13k+ ⭐ | OpenAI | [GitHub](https://github.com/promptfoo/promptfoo) |
| **DeepTeam** | 50+ vulnerabilities, 20+ attack methods. Maps to OWASP Top 10, MITRE, NIST. Built on DeepEval. | Confident AI | [GitHub](https://github.com/confident-ai/deepteam) |

## AI Red Teaming Frameworks

| Tool | Description | By | Link |
|---|---|---|---|
| **PyRIT** | Python Risk Identification Tool. Multi-turn attacks (Crescendo, TAP). Battle-tested in 100+ Microsoft red team ops. | Microsoft | [GitHub](https://github.com/microsoft/PyRIT) |
| **AI Red Teaming Labs** | 13+ hands-on challenge labs with PyRIT integration. | Microsoft | [GitHub](https://github.com/microsoft/AI-Red-Teaming-Playground-Labs) |

## AI API Key Detection

| Tool | Description | Link |
|---|---|---|
| **API Radar** | Real-time dashboard monitoring GitHub for leaked AI keys (OpenAI, Anthropic, Gemini). 9,200+ repos scanned. | [apiradar.live](https://apiradar.live/) |
| **KeyLeak Detector** | Web scanner with 200+ patterns including 15+ AI/LLM providers. Headless browser + network interception. | [GitHub](https://github.com/Amal-David/keyleak-detector) |
| **KeySentry** | Scans GitHub repos for 25+ API key formats including AI providers. CLI + web. | [GitHub](https://github.com/AdityaBhatt3010/KeySentry) |
| **KeyHacks** | Validation commands to verify if discovered API keys are live/active. | [GitHub](https://github.com/streaak/keyhacks) |

## AI Chat & MCP OSINT

| Tool | Description | Link |
|---|---|---|
| **promptmap** | ChatGPT Google dorks and prompt injection testing. Source of `site:chatgpt.com/share` dorks. | [GitHub](https://github.com/utkusen/promptmap) |
| **Vulnerable MCP Project** | Comprehensive MCP vulnerability database with CVEs, CVSS, PoCs, remediation. | [vulnerablemcp.info](https://vulnerablemcp.info/) |
| **MCP Landscape** | Academic MCP security research — attack surfaces, PoC servers, lifecycle threats. | [GitHub](https://github.com/security-pride/MCP_Landscape) |
| **OSINT MCP Server** | 37 OSINT tools across 12 data sources via MCP for AI-assisted recon. | [Glama](https://glama.ai/mcp/servers/Krisparenthetic284/osint-mcp-server) |

## AI Security Knowledge Bases

| Resource | Description | Link |
|---|---|---|
| **AI Red Teaming Guide** | OWASP Gen AI Red Teaming Guide with tool catalogs and MITRE ATLAS mapping. | [GitHub](https://github.com/requie/AI-Red-Teaming-Guide) |
| **LLM Security Guide** | OWASP LLM Top 10 2025 + Agentic Top 10 2026. Updated Feb 2026. | [GitHub](https://github.com/requie/LLMSecurityGuide) |
| **AI Red Team Handbook** | 46-chapter curriculum with automated test runner. | [GitHub](https://github.com/Shiva108/ai-llm-red-team-handbook) |
| **AI Pentesting Toolkit** | Attack catalogs for ChatGPT, Claude, LLaMA. | [GitHub](https://github.com/Mr-Infect/AI-penetration-testing) |

## Standards & Databases

| Resource | Link |
|---|---|
| OWASP Top 10 for LLM Applications 2025 | [owasp.org](https://owasp.org/www-project-top-10-for-large-language-model-applications/) |
| OWASP Top 10 for Agentic Applications 2026 | [owasp.org](https://owasp.org/www-project-top-10-for-agentic-applications/) |
| MITRE ATLAS | [atlas.mitre.org](https://atlas.mitre.org/) |
| MCP Security Best Practices | [modelcontextprotocol.io](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices) |
| NIST AI Risk Management Framework | [nist.gov](https://www.nist.gov/artificial-intelligence) |

---

## 🆕 v1.2.0 Tool Additions (April 2026)

---

### MCPSafetyScanner

| Field | Details |
|-------|---------|
| **URL** | [github.com/johnhalloran321/mcpSafetyScanner](https://github.com/johnhalloran321/mcpSafetyScanner) |
| **Purpose** | Audit MCP server configurations for security vulnerabilities |
| **By** | Academic Research (Leidos) |
| **AI-Specific** | ✅ Purpose-built for MCP security auditing |

Tool from the "MCP Safety Audit" paper (arXiv). Evaluates MCP server definitions for prompt injection vectors, tool poisoning, and excessive permissions. Integrates with the PROTOAMP framework for bridging agent security benchmarks to MCP infrastructure.

---

### Cisco AI Supply Chain Scanners

| Field | Details |
|-------|---------|
| **URL** | Cisco Talos GitHub (open source) |
| **Purpose** | Security scanning for MCP, A2A, agentic skill files, pickle files |
| **By** | Cisco AI Threat Intelligence & Security Research |
| **AI-Specific** | ✅ Purpose-built for AI supply chain security |

Released with Cisco State of AI Security 2026 report:
- **Structure-aware pickle fuzzer** — adversarial pickle file generation
- **MCP server scanner** — MCP implementation vulnerability detection
- **A2A (Agent-to-Agent) scanner** — Google A2A protocol security
- **Agentic skill file scanner** — malicious skill definition detection

---

### DorkEye

| Field | Details |
|-------|---------|
| **URL** | GitHub (search "DorkEye OSINT framework") |
| **Purpose** | Automated Google Dorking with multi-agent analysis pipeline |
| **By** | Open Source Community |
| **AI-Specific** | ⚡ Configurable for AI infrastructure dorking |

Python OSINT framework: interactive wizard, dork generator, multi-agent analysis (SQLi detection, secrets scanning, security analysis), HTML report export. Can be configured with AI-specific dork sets from this repository.

---

### Claude Code Security

| Field | Details |
|-------|---------|
| **URL** | [claude.com/solutions/claude-code-security](https://claude.com/solutions/claude-code-security) |
| **Purpose** | AI-powered static analysis — finds context-dependent vulnerabilities that rule-based tools miss |
| **By** | Anthropic |
| **AI-Specific** | ✅ AI model performing security analysis |

Limited research preview for Enterprise/Team. Free for OSS maintainers. Built on Claude Opus 4.6 (500+ vulns found in production OSS). Reads code like a human researcher — traces data flows, catches business logic flaws.

> ⚠️ Defensive capability that Red Team operators should be aware of.

---

### ATTESTMCP

| Field | Details |
|-------|---------|
| **URL** | Academic (arXiv: "Breaking the Protocol") |
| **Purpose** | MCP protocol extension: capability attestation + message authentication |
| **By** | Academic Research |
| **AI-Specific** | ✅ MCP protocol hardening |

Reduces MCP attack success from 52.8% → 12.4% with 8.3ms overhead. Adds capability attestation, message authentication, and trust propagation controls. Backward-compatible.

---

### Vulnerable MCP Database (UPDATE)

| Field | Details |
|-------|---------|
| **URL** | [vulnerablemcp.info](https://vulnerablemcp.info/) |
| **Status** | **UPDATED:** 50 vulnerabilities, 13 critical, 32 researchers |

New entries: CVE-2026-25536 (TypeScript SDK), CVE-2026-30615/30624/30616/40933 (Ox batch), CVE-2026-33032 (nginx-ui MCPwn), CVE-2026-27825/27826 (Atlassian). Academic analysis of 67,057 MCP servers across 6 registries.

---

## 🆕 v1.4.0 Tool Additions (June 2026)

> All AI-specific, open-source, and verified against their repos (June 2026).
> Theme: MCP / agent-skill auditing — the defensive response to the OpenClaw crisis.

### Agent Threat Rules (ATR)
| Field | Details |
|---|---|
| **URL** | [github.com/Agent-Threat-Rule/agent-threat-rules](https://github.com/Agent-Threat-Rule/agent-threat-rules) |
| **What** | Open detection standard — "like Sigma, but for AI agents." 425 rules covering skill compromise, MCP abuse, prompt injection, exfiltration. Maps to OWASP Agentic Top 10, MITRE ATLAS, NIST. |
| **By** | Community / OWASP A-S-R-H; shipped in Microsoft AGT, Cisco AI Defense, MISP |
| **AI-Specific** | ✅ Purpose-built detection format for agent/skill/MCP threats |

### Cisco DefenseClaw (governance suite)
| Field | Details |
|---|---|
| **URL** | [github.com/cisco-ai-defense/defenseclaw](https://github.com/cisco-ai-defense/defenseclaw) |
| **What** | Open-source agentic governance layer: admission control that scans skills, MCP servers, plugins, and generated code before they run. Bundles skill-scanner, mcp-scanner, a2a-scanner, CodeGuard static analysis, and an AI-BOM generator. |
| **By** | Cisco AI Defense (Apache 2.0) |
| **AI-Specific** | ✅ Built for OpenClaw / agent ecosystems |

### Cisco MCP Scanner
| Field | Details |
|---|---|
| **URL** | [github.com/cisco-ai-defense/mcp-scanner](https://github.com/cisco-ai-defense/mcp-scanner) |
| **What** | Standalone CLI / REST scanner for MCP servers using YARA + LLM-as-judge + Cisco inspect API. Static/offline mode for CI/CD and air-gapped use; pip-audit integration for vulnerable Python deps. |
| **By** | Cisco AI Defense |
| **AI-Specific** | ✅ MCP-specific |

### Cisco Skill Scanner
| Field | Details |
|---|---|
| **URL** | via [cisco-ai-defense](https://github.com/cisco-ai-defense) org |
| **What** | Detects prompt injection, exfiltration, and malicious patterns in agent skills (Cursor, Claude Code, Codex). |
| **By** | Cisco AI Defense (Apache 2.0) |
| **AI-Specific** | ✅ Agent-skill-specific |

### AgentAuditKit
| Field | Details |
|---|---|
| **Install** | `pip install agent-audit-kit` |
| **What** | 77 rules across 13 scanners auditing 13 AI agent platforms (Claude Code, Cursor, Copilot, Windsurf, Amazon Q, Gemini CLI). Checks MCP config exposure, hardcoded keys, invisible-Unicode tool-description hijacking, taint analysis. Maps to OWASP MCP Top 10. |
| **By** | Independent (Sattyam Jain) |
| **AI-Specific** | ✅ |

### mcp-audit
| Field | Details |
|---|---|
| **What** | Offline MCP config auditor across 8 MCP clients; cross-server attack paths, IDE extension security, SAST for Python/TypeScript (37 rules). Maps findings to OWASP MCP Top 10. |
| **By** | Independent (Adam Dudley) |
| **AI-Specific** | ✅ |

### SkillSpector
| Field | Details |
|---|---|
| **What** | Agent-skill security scanner — 64 vulnerability patterns across 16 categories; 0–100 risk score with severity labels. Audits skills before deployment. |
| **By** | Independent |
| **AI-Specific** | ✅ |

### VIPER-MCP
| Field | Details |
|---|---|
| **What** | Combined static + dynamic (taint-style) analysis framework for MCP servers. Ran across ~40,000 server repos → 106 zero-days / 67 CVEs. |
| **By** | Academic research |
| **AI-Specific** | ✅ MCP-specific |

> Other defensive references worth tracking (knowledge bases, not tools):
> [awesome-agent-skills-security](https://github.com/LLMSecurity/awesome-agent-skills-security),
> SAFE-MCP (OpenSSF), and the NSA MCP design-considerations guidance (June 2026).
