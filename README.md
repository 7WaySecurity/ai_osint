<p align="center">
  <img src="assets/logo.png" alt="AI OSINT" width="400">
</p>

<h1 align="center">AI OSINT</h1>

<p align="center">
  <b>Curated OSINT resources for discovering exposed AI infrastructure — dorks, queries, tools, and techniques for LLM, AI agent, and ML pipeline reconnaissance.</b>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT"></a>
  <a href="https://creativecommons.org/licenses/by-sa/4.0/"><img src="https://img.shields.io/badge/Data-CC%20BY--SA%204.0-lightgrey.svg" alt="CC BY-SA 4.0"></a>
  <img src="https://img.shields.io/badge/Updated-April%202026-blue.svg" alt="Updated">
  <a href="CONTRIBUTING.md"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs"></a>
  <img src="https://img.shields.io/github/stars/7WaySecurity/ai_osint?style=social" alt="Stars">
</p>

<p align="center">
  <code>175,000+ Ollama servers exposed</code> · <code>370,000+ Grok conversations indexed</code> · <code>AI credential leaks up 81% YoY</code>
</p>

---

> **AI OSINT** is a curated collection of Google dorks, Shodan queries, GitHub dorks, Censys queries, Sigma detection rules, threat intelligence, and security tools for finding exposed artificial intelligence infrastructure on the internet. It covers LLM endpoints (Ollama, vLLM, LM Studio), AI chatbot conversation leaks (ChatGPT, Grok, Perplexity), vector databases (Qdrant, Weaviate, ChromaDB, Milvus, Pinecone), AI agent gateways (OpenClaw, MCP servers), MLOps platforms (MLflow, Jupyter, Kubeflow), leaked AI API keys (OpenAI, Anthropic, Google Gemini, HuggingFace, Groq, Replicate, Cohere, Mistral, DeepSeek, ElevenLabs), and AI image generation services (Stable Diffusion, ComfyUI). Designed for Red Team operators, penetration testers, bug bounty hunters, and OSINT researchers working in AI/ML security.

---

## Why This Exists

Organizations are deploying LLMs, vector databases, and AI agents faster than they can secure them. The result:

- **Ollama, vLLM, Gradio** — shipped with zero authentication by default
- **ChatGPT, Grok** — shared conversations indexed by search engines with API keys, passwords, PII
- **MCP servers** — exposed agent gateways with shell access, file system access, and stored credentials
- **Qdrant, ChromaDB, MLflow** — no auth out of the box, exposing embeddings, models, and experiments

This repository gives Red Team operators and OSINT professionals the exact queries to find it all.

**Inspired by:** [7WaySecurity/cloud_osint](https://github.com/7WaySecurity/cloud_osint)

---

## 📋 Table of Contents

| Section | What You'll Find |
|---|---|
| [Google Dorks](#-google-dorks) | Queries for ChatGPT, Grok, HuggingFace, dashboards, config files |
| [GitHub Dorks](#-github-dorks) | Leaked API keys for 20+ AI providers, MCP configs, system prompts |
| [Shodan Queries](#-shodan-queries) | Ollama, vLLM, OpenClaw, Gradio, vector DBs, MLflow, Jupyter |
| [Censys Queries](#-censys-queries) | Alternative engine queries for all AI services |
| [AI Service Endpoints](#-ai-service-endpoints) | URL patterns, default ports, API fingerprinting |
| [API Key Patterns](#-api-key-patterns) | Prefixes, regex, validation for every major AI provider |
| [Vector DB Recon](#-vector-database-reconnaissance) | Endpoints to enumerate Qdrant, Weaviate, ChromaDB, Milvus |
| [MCP & Agent Exposure](#-mcp--ai-agent-exposure) | The most critical emerging attack surface in AI security |
| [Threat Intelligence](#-threat-intelligence) | Operation Bizarre Bazaar, Clawdbot crisis, MCP supply chain |
| [Tools](#-tools) | AI-specific only — scanners, red team frameworks, key detectors |
| [Detection Rules](#-detection-rules) | Sigma rules for monitoring AI infrastructure |

---

## 🔍 Google Dorks

> Full collection: [`dorks/google/`](dorks/google/AI_GOOGLE_DORKS.md)

### Exposed AI Conversations & Credentials

```
# Grok (xAI) — 370K+ conversations indexed, NO opt-out for indexing
site:grok.com/share "password"
site:grok.com/share "API key"
site:grok.com/share "secret"
site:grok.com/share "token"
site:grok.com/share "credentials"
site:grok.com/share "keyword"

# ChatGPT — Feature removed Aug 2025, cached results diminishing
# Try on DuckDuckGo which continued indexing after Google stopped
site:chatgpt.com/share "API key"
site:chatgpt.com/share "sk-proj"
site:chatgpt.com/share "password"
site:chatgpt.com/share "AWS_SECRET"

# Perplexity AI
site:perplexity.ai/search "API key"
site:perplexity.ai/search "password"

# Claude (Anthropic) — ~600 convos indexed by Google, 143K+ on Archive.org
# 🔥 Original dork by 7WaySecurity
site:claude.ai "public/artifacts"
site:claude.ai/share "API key"
site:claude.ai/share "sk-ant"
site:claude.ai/share "password"
site:claude.ai/share "AWS"
site:claude.ai/share ".env"
site:web.archive.org "claude.ai/share"

# HuggingFace Spaces — keys hardcoded in public Git repos
site:huggingface.co/spaces "sk-proj"
site:huggingface.co/spaces "OPENAI_API_KEY"
site:huggingface.co/spaces "os.environ"
site:huggingface.co/spaces "st.secrets"
```

### Exposed AI Dashboards

```
intitle:"MLflow" inurl:"/mlflow"
intitle:"Label Studio" inurl:"/projects"
intitle:"Jupyter Notebook" inurl:"/tree" -"Login"
intitle:"Kubeflow" inurl:"/pipeline"
intitle:"Airflow - DAGs"
intitle:"Gradio" inurl:":7860"
intitle:"Streamlit" inurl:":8501"
intitle:"Open WebUI" "ollama"
intitle:"Qdrant Dashboard"
intitle:"ComfyUI"
intitle:"Stable Diffusion"
intitle:"LiteLLM" "proxy"
```

### AI Config & Credential Files

```
filetype:env "OPENAI_API_KEY"
filetype:env "ANTHROPIC_API_KEY"
filetype:env "HUGGINGFACE_TOKEN"
filetype:env "GROQ_API_KEY"
filetype:env "PINECONE_API_KEY"
filetype:env "WANDB_API_KEY"
filetype:env "DEEPSEEK_API_KEY"
filetype:env "OPENROUTER_API_KEY"
filetype:yaml "openai" "api_key"
filetype:json "anthropic" "api_key"
```

---

## 🐙 GitHub Dorks

> Full collection: [`dorks/github/`](dorks/github/AI_GITHUB_DORKS.md)
>
> ⚠️ **Syntax note:** GitHub migrated to new Code Search. Use `path:*.env` instead of legacy `filename:.env`. Queries below use modern syntax where applicable.

### AI API Keys on GitHub

```
# OpenAI (project keys — current format since April 2024)
"sk-proj-" path:*.env
"sk-proj-" path:*.py
"OPENAI_API_KEY" path:*.env NOT "your_key" NOT "example"

# Anthropic
"sk-ant-api03" path:*.env
"ANTHROPIC_API_KEY" path:*.env

# Google AI / Gemini
"AIzaSy" path:*.env "generativelanguage"
"GOOGLE_API_KEY" path:*.env "gemini"

# HuggingFace
"hf_" path:*.env
"HF_TOKEN" path:*.env

# Groq
"gsk_" path:*.env
"GROQ_API_KEY" path:*.env

# Replicate
"r8_" path:*.env
"REPLICATE_API_TOKEN" path:*.env

# Vector DBs & MLOps
"PINECONE_API_KEY" path:*.env
"QDRANT_API_KEY" path:*.env
"WANDB_API_KEY" path:*.env
```

### MCP & Agent Config Leaks

```
path:mcp.json "api_key"
path:mcp.json "token"
path:.cursor/mcp.json
"mcpServers" path:*.json "apiKey"
"mcpServers" path:*.json "OPENAI_API_KEY"
```

### System Prompts & Training Data

```
"system_prompt" path:*.py "you are"
"SYSTEM_PROMPT" path:*.env
path:prompts.yaml "system"
path:train.jsonl "prompt" "completion"
path:dataset.jsonl "instruction" "output"
```

---

## 🔭 Shodan Queries

> Full collection: [`dorks/shodan/`](dorks/shodan/AI_SHODAN_DORKS.md)

### Self-Hosted LLMs

```
# Ollama — 175,000+ exposed instances worldwide
"Ollama is running" port:11434
port:11434 http.html:"Ollama"
port:11434 "api/tags"

# vLLM / OpenAI-compatible
port:8000 "openai" "model"
http.title:"FastAPI" port:8000 "/v1/models"

# LM Studio
port:1234 "/v1/models"

# llama.cpp
port:8080 "llama" "completion"
```

### AI Agent Gateways — CRITICAL

```
# OpenClaw/Clawdbot — 4,000+ on Shodan, many with zero auth
# Enables RCE via prompt injection, API key theft, reverse shells
http.title:"Clawdbot Control" port:18789
http.title:"OpenClaw" port:18789
port:18789 "api/v1/status"
port:18789 "auth_mode"
```

### Gradio & Streamlit Apps

```
http.title:"Gradio" port:7860
http.title:"Streamlit" port:8501
http.title:"Stable Diffusion" port:7860
http.title:"ComfyUI"
```

### Vector Databases

```
# Qdrant — NO auth by default
port:6333 "qdrant"
port:6333 "/collections"

# Weaviate
port:8080 "weaviate"

# Milvus
port:19530 "milvus"
```

### MLOps & Notebooks

```
# MLflow — CVE-2026-0545 (CVSS 9.1) RCE, no auth by default
http.title:"MLflow" port:5000

# Jupyter — ~10,000+ on Shodan, targeted by botnets
http.title:"Jupyter Notebook" port:8888 -"Login"
http.title:"JupyterLab" port:8888

# TensorBoard
http.title:"TensorBoard" port:6006
```

---

## 🌐 Censys Queries

> Full collection: [`dorks/censys/`](dorks/censys/AI_CENSYS_QUERIES.md)

```
# Ollama (Censys found 25%+ on non-default ports)
services.port=11434 AND services.http.response.body:"Ollama"

# Gradio
services.port=7860 AND services.http.response.html_title:"Gradio"

# OpenClaw
services.port=18789 AND services.http.response.body:"Clawdbot"

# Vector DBs
services.port=6333 AND services.http.response.body:"qdrant"
services.port=8080 AND services.http.response.body:"weaviate"

# MLOps
services.port=5000 AND services.http.response.html_title:"MLflow"
services.port=8888 AND services.http.response.html_title:"Jupyter"
```

---

## 🌍 AI Service Endpoints

### Major Provider APIs

| Provider | API Endpoint | Shared Content |
|---|---|---|
| **OpenAI** | `api.openai.com/v1/*` | `chatgpt.com/share/*` |
| **Anthropic** | `api.anthropic.com/v1/*` | — |
| **Google** | `generativelanguage.googleapis.com/v1beta/*` | — |
| **xAI** | `api.x.ai/v1/*` | `grok.com/share/*` |
| **Mistral** | `api.mistral.ai/v1/*` | — |
| **Cohere** | `api.cohere.ai/v1/*` | — |
| **DeepSeek** | `api.deepseek.com/v1/*` | — |
| **Groq** | `api.groq.com/openai/v1/*` | — |
| **HuggingFace** | `api-inference.huggingface.co/models/*` | `huggingface.co/spaces/*` |
| **ElevenLabs** | `api.elevenlabs.io/v1/*` | — |

### Default Ports (all verified against official docs)

| Service | Port | Auth Default | Risk Level |
|---|---|---|---|
| **Ollama** | 11434 | ❌ None | 🔴 Critical |
| **vLLM** | 8000 | ❌ None | 🔴 Critical |
| **OpenClaw** | 18789 | ❌ None (fixed in rebrand) | 🔴 Critical |
| **Gradio** | 7860 | ❌ None | 🔴 Critical |
| **Streamlit** | 8501 | ❌ None | 🟡 High |
| **MLflow** | 5000 | ❌ None | 🔴 Critical |
| **Qdrant** | 6333/6334 | ❌ None | 🔴 Critical |
| **Weaviate** | 8080 (+ gRPC 50051) | ❌ None | 🟡 High |
| **ChromaDB** | 8000 | ❌ None (binds localhost) | 🟡 High |
| **Milvus** | 19530 (+ mgmt 9091) | ❌ None | 🟡 High |
| **Jupyter** | 8888 | ✅ Token (often disabled) | 🟡 High |
| **LM Studio** | 1234 | ❌ None | 🟡 High |
| **GPT4All** | 4891 | ❌ None | 🟡 High |

---

## 🔑 API Key Patterns

### Prefix Reference (verified against official docs)

| Provider | Prefix | Length | Notes |
|---|---|---|---|
| **OpenAI** | `sk-proj-` | ~80+ chars | Current format since April 2024 |
| **Anthropic** | `sk-ant-api03-` | ~90+ chars | API keys |
| **Anthropic OAuth** | `sk-ant-oat01-` | — | OAuth tokens (Files API, etc.) |
| **Google AI** | `AIzaSy` | 39 chars | ⚠️ Same prefix for Maps AND Gemini |
| **HuggingFace** | `hf_` | ~34 chars | Read/write access tokens |
| **Replicate** | `r8_` | ~40 chars | — |
| **Groq** | `gsk_` | ~52 chars | — |

### Regex for Detection

```regex
# OpenAI project keys
sk-proj-[A-Za-z0-9_-]{80,}

# Anthropic
sk-ant-api03-[A-Za-z0-9_-]{90,}

# HuggingFace
hf_[A-Za-z0-9]{34}

# Replicate
r8_[A-Za-z0-9]{37}

# Groq
gsk_[A-Za-z0-9]{52}

# Google AI (⚠️ also matches Maps, YouTube, etc.)
AIzaSy[A-Za-z0-9_-]{33}
```

> ⚠️ **Google `AIzaSy` warning:** Google uses the same prefix for ALL Cloud APIs. A Maps API key embedded in public JavaScript can silently gain Gemini API access if the Generative Language API is enabled on the same project. This was documented as a significant issue in early 2026.

---

## 🗃️ Vector Database Reconnaissance

When exposed, vector databases leak proprietary embeddings, sensitive documents, and internal knowledge bases used in RAG systems.

### Enumeration Endpoints (verified against official API docs)

| Database | List Collections | Extract Data |
|---|---|---|
| **Qdrant** | `GET /collections` | `POST /collections/{name}/points/scroll` |
| **Weaviate** | `GET /v1/schema` | `GET /v1/objects?class={name}` |
| **ChromaDB** | `GET /api/v2/collections` ⚠️ | `POST /api/v2/collections/{id}/query` |
| **Milvus** | gRPC `ListCollections` | gRPC `Search/Query` |

> ⚠️ **ChromaDB API update:** v1.0.0+ migrated to `/api/v2`. The legacy `/api/v1/collections` now returns a deprecation error. Update your recon scripts accordingly.

---

## 🤖 MCP & AI Agent Exposure

The **Model Context Protocol (MCP)** is the most critical emerging attack surface in AI security (2025-2026).

### Why MCP is Dangerous

MCP servers connect AI models to shell access, file systems, databases, and APIs. Misconfigurations expose:
- **Shell/code execution** via prompt injection
- **API keys in plaintext** in `.env` files readable by agents
- **Tool poisoning** — hidden instructions in tool metadata
- **Supply chain attacks** — compromised MCP packages (24,000+ secrets leaked in MCP configs in its first year)

### Discovery Queries

```
# Shodan
port:18789 "api/v1"
http.title:"Clawdbot" OR http.title:"OpenClaw"

# GitHub
path:mcp.json "apiKey"
path:.cursor/mcp.json
"mcpServers" path:*.json "token"
```

### Key Incidents

| Incident | Date | Impact |
|---|---|---|
| OpenClaw Shodan Exposure | Jan 2026 | 4,000+ agent gateways, many with zero auth and RCE |
| Operation Bizarre Bazaar | Dec 2025–Jan 2026 | 35,000 attacks on LLM/MCP endpoints; commercial resale |
| Smithery Registry Breach | 2025 | Fly.io token → control of 3,000+ MCP servers |
| mcp-remote CVE-2025-6514 | 2025 | Command injection in 437K+ installs |
| Cursor IDE MCP Trust Issue | 2025 | Persistent RCE via shared repo configs (CVSS 7.2-8.8) |

> 📖 Full timeline: [`threat-intel/THREAT_INTELLIGENCE.md`](threat-intel/THREAT_INTELLIGENCE.md)

---

## 📊 Threat Intelligence

> Full entries: [`threat-intel/`](threat-intel/THREAT_INTELLIGENCE.md)

- **Operation Bizarre Bazaar** — First large-scale LLMjacking: 35K attacks, commercial marketplace selling stolen AI access
- **OpenClaw/Clawdbot Shodan Crisis** — CVE-2026-24061, "Localhost Trust" bypass
- **ChatGPT/Grok Conversation Indexing** — Google indexed thousands of conversations with credentials
- **Claude Conversation Indexing** — ~600 conversations indexed by Google (Forbes Sep 2025); 143K+ across all LLMs on Archive.org
- **"Claudy Day" Attack Chain** — Open redirect + prompt injection + Files API exfiltration in claude.ai (Oasis Security, Mar 2026)
- **Claude Code Source Map Leak** — 512K lines of source code exposed via npm package v2.1.88 (Mar 2026)
- **MCP Supply Chain Timeline** — 10+ major breaches in MCP ecosystem
- **175K Ollama Servers Exposed** — SentinelOne/Censys study across 130 countries
- **AI-Assisted ICS Targeting** — 60+ Iranian groups using LLMs for critical infrastructure recon (Feb 2026)

---

## 🛠️ Tools

> Only AI-specific tools. Full details: [`tools/TOOLS.md`](tools/TOOLS.md)
> For generic OSINT tools (Shodan, Censys, etc.) see [cloud_osint](https://github.com/7WaySecurity/cloud_osint).

| Tool | What It Does | By |
|---|---|---|
| [**Garak**](https://github.com/NVIDIA/garak) | LLM vulnerability scanner — "nmap for LLMs" | NVIDIA |
| [**PyRIT**](https://github.com/microsoft/PyRIT) | AI red teaming framework — Crescendo, jailbreaking, multi-turn | Microsoft |
| [**promptfoo**](https://github.com/promptfoo/promptfoo) | LLM pentesting CLI — 133+ attack plugins | OpenAI |
| [**DeepTeam**](https://github.com/confident-ai/deepteam) | 50+ vulns, 20+ attacks, OWASP/MITRE mapping | Confident AI |
| [**API Radar**](https://apiradar.live/) | Real-time leaked AI API key monitoring on GitHub | Independent |
| [**KeyLeak Detector**](https://github.com/Amal-David/keyleak-detector) | Web scanner for 200+ patterns incl. 15+ AI providers | Independent |
| [**promptmap**](https://github.com/utkusen/promptmap) | ChatGPT dorks & prompt injection testing | Utku Şen |
| [**Vulnerable MCP**](https://vulnerablemcp.info/) | MCP vulnerability database with CVEs and PoCs | Community |

---

## 🚨 Detection Rules

> Full Sigma rules: [`detection-rules/SIGMA_RULES.md`](detection-rules/SIGMA_RULES.md)

7 Sigma detection rules covering:
- External access to Ollama (port 11434)
- AI API keys appearing in application logs
- Unauthorized LLM API access without Bearer tokens
- Exposed MCP servers with `auth_mode: none`
- Vector database unauthorized enumeration
- LLMjacking — anomalous inference spikes (>500 requests/hour)
- AI agent RCE via prompt injection (suspicious tool calls to bash/python_repl)

---

## 📚 References

### Research

| Source | Finding | Link |
|---|---|---|
| SentinelOne + Censys | 175,108 exposed Ollama hosts across 130 countries | [SecurityWeek](https://www.securityweek.com/175000-exposed-ollama-hosts-could-enable-llm-abuse/) |
| Cisco Talos | 1,100+ Ollama servers, 20% serving models without auth | [Cisco Blog](https://blogs.cisco.com/security/detecting-exposed-llm-servers-shodan-case-study-on-ollama) |
| Pillar Security | Operation Bizarre Bazaar: 35,000 LLMjacking attacks | [Pillar Security](https://www.pillar.security/) |
| GitGuardian | AI credential leaks surged 81% YoY; 29M secrets on GitHub | [Report](https://blog.gitguardian.com/the-state-of-secrets-sprawl-2026/) |
| AuthZed | Complete MCP security breaches timeline | [Blog](https://authzed.com/blog/timeline-mcp-breaches) |
| Pangea | Sensitive data in indexed ChatGPT histories | [Blog](https://pangea.cloud/blog/mining-the-index-uncovering-sensitive-data-in-public-chatgpt-histories-via-google-search/) |
| Trail of Bits | 8 high-severity vulns in Gradio 5 audit | [Blog](https://blog.trailofbits.com/2024/10/10/auditing-gradio-5-hugging-faces-ml-gui-framework/) |
| Oasis Security | "Claudy Day" — 3 vulns chained for data exfiltration from Claude | [Blog](https://www.oasis.security/blog/claude-ai-prompt-injection-data-exfiltration-vulnerability) |
| Forbes | ~600 Claude conversations indexed by Google | [Article](https://www.forbes.com/sites/iainmartin/2025/09/08/hundreds-of-anthropic-chatbot-transcripts-showed-up-in-google-search/) |
| Obsidian Security | 143K+ LLM chats (incl. Claude) on Archive.org | [Blog](https://www.obsidiansecurity.com/resource/143k-claude-copilot-chatgpt-chats-publicly-accessible-were-you-exposed) |
| TechRadar | Claude Code 512K source lines leaked via npm | [Article](https://www.techradar.com/pro/security/anthropic-confirms-it-leaked-512-000-lines-of-claude-code-source-code-spilling-some-of-its-biggest-secrets) |
| Penligent | Claude Code source map leak analysis | [Blog](https://www.penligent.ai/hackinglabs/claude-code-source-map-leak-what-was-exposed-and-what-it-means/) |

### Standards

- [OWASP Top 10 for LLM Applications 2025](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [OWASP Top 10 for Agentic Applications 2026](https://owasp.org/www-project-top-10-for-agentic-applications/)
- [MITRE ATLAS](https://atlas.mitre.org/)
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices)
- [vulnerablemcp.info](https://vulnerablemcp.info/)

---

## ⚠️ Disclaimer

The resources in this repository are for **authorized security testing, education, and legitimate research only**.

1. **Obtain proper authorization** before testing infrastructure you do not own
2. **Follow applicable laws** (CFAA, GDPR, local equivalents)
3. **Report vulnerabilities responsibly** through appropriate disclosure channels
4. **Never exploit** discovered misconfigurations for unauthorized access

The authors assume no liability for misuse.

---

## 🤝 Contributing

PRs welcome! Please verify dorks/queries work before submitting. See [CONTRIBUTING.md](CONTRIBUTING.md).

---

## License

Code: [MIT](LICENSE) · Data & Documentation: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)

---

<p align="center"><b>Maintained by <a href="https://7waysecurity.co">7WaySecurity</a></b> · Last updated April 2026</p>
