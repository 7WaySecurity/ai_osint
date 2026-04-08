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
