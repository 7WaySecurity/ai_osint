# Resources & References

## Research (verified sources)

| Source | Finding | Link |
|---|---|---|
| SentinelOne + Censys (Jan 2026) | 175,108 exposed Ollama hosts, 130 countries, 293-day study | [SecurityWeek](https://www.securityweek.com/175000-exposed-ollama-hosts-could-enable-llm-abuse/) |
| Cisco Talos (Sep 2025) | 1,100+ Ollama servers in 10 min, 20% serving models without auth | [Cisco Blog](https://blogs.cisco.com/security/detecting-exposed-llm-servers-shodan-case-study-on-ollama) |
| FuzzingLabs (Jul 2025) | 270,988 Ollama instances via Shodan | [FuzzingLabs](https://fuzzinglabs.com/ollama-vulnerable-instances/) |
| Pillar Security (Jan 2026) | Operation Bizarre Bazaar: 35K LLMjacking attacks | [Pillar](https://www.pillar.security/) |
| GitGuardian (2026) | AI credential leaks +81% YoY; 29M secrets on GitHub | [Report](https://blog.gitguardian.com/the-state-of-secrets-sprawl-2026/) |
| AuthZed (Nov 2025) | Complete MCP breaches timeline | [Blog](https://authzed.com/blog/timeline-mcp-breaches) |
| Pangea (Aug 2025) | Sensitive data in ChatGPT indexed histories | [Blog](https://pangea.cloud/blog/mining-the-index-uncovering-sensitive-data-in-public-chatgpt-histories-via-google-search/) |
| Resonance Security (Aug 2025) | Google indexing ChatGPT conversations analysis | [Blog](https://www.resonance.security/blog-posts/how-google-is-indexing-chatgpt-conversations-when-sharing-becomes-leaking) |
| Fortune (Aug 2025) | 370K+ Grok conversations indexed by Google | [Fortune](https://fortune.com/2025/08/22/xai-grok-chats-public-on-google-search-elon-musk/) |
| Trail of Bits (Oct 2024) | 8 high-severity vulnerabilities in Gradio 5 audit | [Blog](https://blog.trailofbits.com/2024/10/10/auditing-gradio-5-hugging-faces-ml-gui-framework/) |
| Red Hat (Nov 2025) | MCP security risks and controls analysis | [Blog](https://www.redhat.com/en/blog/model-context-protocol-mcp-understanding-security-risks-and-controls) |
| Pivot Point Security (Mar 2026) | 22% MCP servers allow file access outside scope; 5% seeded with tool poisoning | [Blog](https://www.pivotpointsecurity.com/what-is-the-model-context-protocol-mcp-in-ai-and-why-does-it-scare-cybersecurity-pros/) |
| CloudSEK (Mar 2026) | 60+ Iranian groups using AI for ICS recon post-Iran-US escalation | [Blog](https://www.cloudsek.com/blog/ai-the-iran-us-conflict-and-the-threat-to-us-critical-infrastructure) |
| Forbes (Sep 2025) | ~600 Claude conversations indexed by Google despite crawler blocking | [Article](https://www.forbes.com/sites/iainmartin/2025/09/08/hundreds-of-anthropic-chatbot-transcripts-showed-up-in-google-search/) |
| Obsidian Security (2025) | 143K+ LLM conversations (Claude, ChatGPT, Copilot, Grok) on Archive.org | [Blog](https://www.obsidiansecurity.com/resource/143k-claude-copilot-chatgpt-chats-publicly-accessible-were-you-exposed) |
| Oasis Security (Mar 2026) | "Claudy Day" — 3 vulns chained: open redirect + prompt injection + Files API exfil | [Blog](https://www.oasis.security/blog/claude-ai-prompt-injection-data-exfiltration-vulnerability) |
| TechRadar (Mar 2026) | Claude Code 512K lines leaked via npm source map in v2.1.88 | [Article](https://www.techradar.com/pro/security/anthropic-confirms-it-leaked-512-000-lines-of-claude-code-source-code-spilling-some-of-its-biggest-secrets) |
| Penligent (Apr 2026) | Claude Code source map leak deep analysis | [Blog](https://www.penligent.ai/hackinglabs/claude-code-source-map-leak-what-was-exposed-and-what-it-means/) |
| Geol.ai (Jan 2026) | Claude transcript privacy risk analysis | [Blog](https://geol.ai/briefing/anthropics-claude-conversations-exposed-privacy-implications-in-ai-chatbots) |
| Aqua Security | Jupyter targeted by botnets; first Python ransomware on Jupyter | [Blog](https://blog.aquasec.com/python-ransomware-jupyter-notebook) |
| CSO Online | MLflow critical flaw leading to server compromise | [Article](https://www.csoonline.com/article/574831/critical-flaw-in-ai-testing-framework-mlflow-can-lead-to-server-and-data-compromise.html) |

## Standards & Frameworks

| Resource | Link |
|---|---|
| OWASP Top 10 for LLM Applications 2025 | [owasp.org](https://owasp.org/www-project-top-10-for-large-language-model-applications/) |
| OWASP Top 10 for Agentic Applications 2026 | [owasp.org](https://owasp.org/www-project-top-10-for-agentic-applications/) |
| MITRE ATLAS | [atlas.mitre.org](https://atlas.mitre.org/) |
| MCP Security Best Practices | [modelcontextprotocol.io](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices) |
| NIST AI Risk Management Framework | [nist.gov](https://www.nist.gov/artificial-intelligence) |
| EU AI Act | [artificialintelligenceact.eu](https://artificialintelligenceact.eu/) |
| Vulnerable MCP Project | [vulnerablemcp.info](https://vulnerablemcp.info/) |

## Conferences

| Event | Focus |
|---|---|
| DEF CON AI Village | AI security research, CTFs |
| Black Hat | Enterprise AI security |
| GrrCON | Midwest security — AI track |
| OWASP Global AppSec | LLM/AI Top 10 |

---

## 🆕 v1.2.0 Resource Additions (April 2026)

---

### Reports & Research

| Resource | Description | Date |
|----------|-------------|------|
| [Cisco State of AI Security 2026](https://blogs.cisco.com/ai/cisco-state-of-ai-security-2026-report) | AI threat landscape: prompt injection evolution, AI supply chain, MCP risks, agentic AI. Open-source MCP/A2A/pickle scanners. | Feb 2026 |
| [IBM X-Force Threat Intelligence Index 2026](https://www.ibm.com/think/insights/more-2026-cyberthreat-trends) | 300K+ ChatGPT creds on dark web, supply chain attacks 4x in 5 years, AI agents as attack surface. | Mar 2026 |
| [Claude Mythos Preview System Card](https://red.anthropic.com/2026/mythos-preview/) | Autonomous 0-day discovery — thousands of vulns in major OS/browsers. Sandbox escape. 89% severity agreement. | Apr 2026 |
| [Reverse Engineering Claude's CVE-2026-2796 Exploit](https://red.anthropic.com/2026/exploit/) | How Claude Opus 4.6 built a Firefox JIT exploit — type confusion → file read/write from JS shell. | Mar 2026 |
| [Claude Code Security](https://www.anthropic.com/news/claude-code-security) | AI-powered static analysis. Research preview for Enterprise/Team. Free for OSS maintainers. | Feb 2026 |
| [Ox Security: Mother of All AI Supply Chains](https://www.ox.security/blog/the-mother-of-all-ai-supply-chains-critical-systemic-vulnerability-at-the-core-of-the-mcp/) | Systemic MCP STDIO RCE — 150M+ downloads, 200K instances, 10+ CVEs. 9/11 marketplaces poisoned. | Apr 2026 |
| [Ox Security: MCP Supply Chain Advisory](https://www.ox.security/blog/mcp-supply-chain-advisory-rce-vulnerabilities-across-the-ai-ecosystem) | Full disclosure — all CVEs, affected platforms, PoCs. Windsurf, Agent Zero, Jaaz, Flowise, LiteLLM, LangChain. | Apr 2026 |
| [Zscaler ThreatLabz: Claude Code Leak](https://www.zscaler.com/blogs/security-research/anthropic-claude-code-leak) | 59.8 MB source map leak analysis + Vidar/GhostSocks malware lure. 50-subcommand bypass. | Apr 2026 |
| [SecurityWeek: Claude Code Vulnerability](https://www.securityweek.com/critical-vulnerability-in-claude-code-emerges-days-after-source-leak/) | Adversa AI — deny rule bypass when pipeline exceeds 50 subcommands. | Apr 2026 |
| [Check Point: ChatGPT DNS Exfiltration](https://blog.checkpoint.com/research/when-ai-trust-breaks-the-chatgpt-data-leakage-flaw-that-redefined-ai-vendor-security-trust/) | DNS side channel in ChatGPT code execution sandbox. Silent leakage. Patched Feb 20, 2026. | Mar 2026 |
| [CSA: Mythos and the Exploit Gap](https://www.helpnetsecurity.com/2026/04/15/anthropic-claude-mythos-ai-vulnerability-discovery/) | Time-to-exploit now under 20 hours. Priority actions: immediate/45-day/90-day. | Apr 2026 |
| [Wiz: Claude Mythos Analysis](https://www.wiz.io/blog/claude-mythos) | "Y2K moment" for cybersecurity. Prepare for AI-led vulnerability wave. Invest in AI AppSec. | Apr 2026 |
| [LeakIX: Ollama Exposed](https://blog.leakix.net/2026/02/ollama-exposed/) | 12,269 exposed instances. Critique of Ollama's auth PR rejections. | Feb 2026 |
| [Logicalis Global CIO Report 2026](https://www.webanditnews.com/2026/04/16/ais-shadow-side-cios-grapple-with-mounting-security-threats-in-2026/) | 57% employees expose data via AI, 76% uneasy about unchecked AI, only 37% visibility into AI tools. | Apr 2026 |
| [Wiz: DeepSeek ClickHouse Exposure](https://www.wiz.io/blog/wiz-research-uncovers-exposed-deepseek-database-leak) | 1M+ log entries with plaintext chats, API keys, backend details. No authentication. | Jan 2025 |

### Academic Papers

| Paper | Key Finding | Link |
|-------|-------------|------|
| MCP Safety Audit | MCPSafetyScanner tool; MCP security risk assessment | [arXiv](https://arxiv.org/pdf/2504.03767) |
| Breaking the Protocol | PROTOAMP framework; ATTESTMCP reduces attacks 52.8% → 12.4% across 847 scenarios | [arXiv](https://arxiv.org/pdf/2601.17549) |
| MCP Threat Modeling | STRIDE/DREAD of 5 MCP components; tool poisoning taxonomy | [arXiv](https://arxiv.org/pdf/2603.22489) |

### CVE Databases & Trackers

| Resource | Description | Link |
|----------|-------------|------|
| Vulnerable MCP Database | **UPDATED:** 50 vulns, 13 critical, 32 researchers. 67,057 servers analyzed across 6 registries. | [vulnerablemcp.info](https://vulnerablemcp.info/) |
| ChatGPT Data Leaks Timeline | 2023-2026 timeline: DNS exfil, SVG XSS, Deep Research zero-click, Mixpanel breach. | [wald.ai](https://wald.ai/blog/chatgpt-data-leaks-and-security-incidents-20232024-a-comprehensive-overview) |
| AI Coding Security Stats 2026 | 45% AI code has vulns, 73% systems exposed to prompt injection, 300K+ creds on dark web. | [SQ Magazine](https://sqmagazine.co.uk/ai-coding-security-vulnerability-statistics/) |

### Key Statistics (April 2026)

| Metric | Value | Source |
|--------|-------|--------|
| Exposed Ollama instances | 187,000+ combined | SentinelOne/Censys + LeakIX |
| ChatGPT credentials on dark web | 300,000+ | IBM X-Force 2026 |
| MCP supply chain affected | 150M+ downloads | Ox Security |
| MCP vulnerabilities tracked | 50 (13 critical) | vulnerablemcp.info |
| MCP marketplaces poisoned | 9 of 11 | Ox Security |
| Average time-to-exploit | < 20 hours | CSA / Zero Day Clock |
| AI-generated code with vulnerabilities | 45% | Veracode |
| AI systems exposed to prompt injection | 73% | 2026 security audits |
| AI credential leaks YoY increase | +81% | GitGuardian 2026 |
| Grok conversations indexed | 370,000+ | Fortune |
| CIOs boosting AI investments | 94% | Logicalis 2026 |
| Employees exposing data via AI | 57% | Logicalis 2026 |

---

## 🆕 v1.4.0 Resource Additions (June 2026)

### Reports & Research
- **Koi Security** — ClawHub audit (341 malicious of 2,857 skills)
- **Antiy CERT** — ClawHavoc analysis (1,184 skills, Trojan/OpenClaw.PolySkill)
- **Snyk ToxicSkills** — 3,984 skills audited; 13.4% with critical issues
- **OX Security** — MCP Supply Chain Advisory (10 CVEs; 9 of 11 marketplaces poisoned)
- **BlueRock** — 7,000+ MCP servers, 36.7% SSRF-vulnerable
- **Censys** — ~12,520 Internet-accessible MCP services
- **Trend Micro** — Network-exposed MCP servers as backdoors

### Academic Papers
- **"Agent Skills in the Wild" (Liu et al., 2026)** — 42,447 skills; 26.1% vulnerable, 5.2% malicious
- **SkillSieve** — hierarchical triage for malicious skill detection (arXiv 2604.06550)
- **Skill-Inject (Schmotz et al., 2026)** — benchmark for skill-file attacks
- **VIPER-MCP** — 106 zero-days / 67 CVEs across ~40,000 MCP repos

### Detection & Frameworks
- **Agent Threat Rules (ATR)** — 425 open detection rules for agents
- **SAFE-MCP (OpenSSF)** — Secure-MCP technique catalog
- **NSA MCP design-considerations guidance** (June 2026)
- **OWASP Agentic Top 10 (2026)** — ASI04 (agent registry poisoning)

### Government / Advisories
- **CERT-Bund** WID-SEC-2026-0856 (OpenClaw)
- **CISA KEV / BOD 26-04** — accelerated 3-day patch mandate context

### Key Statistics (June 2026)
- 135,000+ exposed OpenClaw instances (63%–93% without auth)
- 1,184 malicious skills historically on ClawHub
- ~40% of remote MCP servers expose tools with no authentication
- 138 CVEs associated with OpenClaw in five months
