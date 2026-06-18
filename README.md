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
  <img src="https://img.shields.io/badge/Updated-June%202026-blue.svg" alt="Updated">
  <a href="CONTRIBUTING.md"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs"></a>
  <img src="https://img.shields.io/github/stars/7WaySecurity/ai_osint?style=social" alt="Stars">
</p>

<p align="center">
  <code>`187,000+ Ollama servers exposed`</code> · <code>`370,000+ Grok conversations indexed`</code> · <code>`AI credential leaks up 81% YoY`</code> · <code>`150M+ MCP downloads affected by systemic RCE`</code> · <code>`300K+ ChatGPT creds on dark web`</code>
</p>

---

> **AI OSINT** is a curated collection of Google dorks, Shodan queries, GitHub dorks, Censys queries, Sigma detection rules, threat intelligence, and security tools for finding exposed artificial intelligence infrastructure on the internet. It covers LLM endpoints (Ollama, vLLM, LM Studio), AI chatbot conversation leaks (ChatGPT, Grok, Perplexity), vector databases (Qdrant, Weaviate, ChromaDB, Milvus, Pinecone), AI agent gateways (OpenClaw, MCP servers), MLOps platforms (MLflow, Jupyter, Kubeflow), leaked AI API keys (OpenAI, Anthropic, Google Gemini, HuggingFace, Groq, Replicate, Cohere, Mistral, DeepSeek, ElevenLabs), and AI image generation services (Stable Diffusion, ComfyUI). Designed for Red Team operators, penetration testers, bug bounty hunters, and OSINT researchers working in AI/ML security.

It now also covers MCP supply chain attacks (systemic STDIO RCE, marketplace poisoning), AI IDE exploitation (Copilot YOLO mode, Windsurf zero-click), AI model leak incidents (Claude Code source map, DeepSeek ClickHouse exposure), AI-assisted vulnerability discovery (Mythos/Glasswing), and ChatGPT data exfiltration techniques.

---

## Why This Exists

Organizations are deploying LLMs, vector databases, and AI agents faster than they can secure them. The result:

- **Ollama, vLLM, Gradio** — shipped with zero authentication by default
- **ChatGPT, Grok** — shared conversations indexed by search engines with API keys, passwords, PII
- **MCP servers** — exposed agent gateways with shell access, file system access, and stored credentials
- **Qdrant, ChromaDB, MLflow** — no auth out of the box, exposing embeddings, models, and experiments
- **AI IDEs (Copilot, Cursor, Windsurf)** — prompt injection enables YOLO mode activation, wormable RCE across developer workstations
- **MCP supply chain** — 9 of 11 MCP marketplaces poisoned in proof-of-concept; 150M+ downloads affected by systemic RCE
- **AI code execution sandboxes** — DNS side channels bypass outbound network guardrails, enabling silent data exfiltration

This repository gives Red Team operators and OSINT professionals the exact queries to find it all.

**Inspired by:** [7WaySecurity/cloud_osint](https://github.com/7WaySecurity/cloud_osint)

---

## 🔑 The `KEYWORD` Convention — Read This First

As of **v1.3.0**, every dork and query in this repository uses a **`KEYWORD` placeholder** in place of the secret-seeking value strings (passwords, tokens, credentials, etc.) that used to be hard-coded.

**Replace `KEYWORD` with a term you are authorized to search for:**

- your **company / brand / product name**
- a **domain you own** (often via an extra `site:` / `hostname:` / `org:` filter)
- an **internal project codename**
- a scope identifier from an **authorized engagement**

```
# Examples of scoping KEYWORD to your own assets:
site:grok.com/share "acme-corp"
intitle:"MLflow" site:acme.com
"OPENAI_API_KEY" path:*.env org:acme-corp
"Ollama is running" port:11434 org:"Acme Inc"
```

**What stays:** service fingerprints (product titles, API paths, ports, env-var names like `OPENAI_API_KEY`, key prefixes like `sk-proj-`) are kept as-is — they identify the *service or format*, not a specific victim's secret.

**Why:** documenting *that* a class of system is commonly misconfigured, and *how* to check your own exposure, is legitimate defensive and red-team work. Shipping copy-paste queries whose only function is to maximize the yield of *other people's* live secrets is not. The `KEYWORD` convention keeps every technique here useful for authorized testing without being a turnkey harvesting kit.

If a hit surfaces a **third party's** secret, that is not your finding to act on — [report it responsibly](#-disclaimer) and move on.

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
site:grok.com/share "KEYWORD"

# ChatGPT — Feature removed Aug 2025, cached results diminishing
# Try on DuckDuckGo which continued indexing after Google stopped
site:chatgpt.com/share "KEYWORD"

# Perplexity AI
site:perplexity.ai/search "KEYWORD"

# Claude (Anthropic) — ~600 convos indexed by Google, 143K+ on Archive.org
# 🔥 Original dork by 7WaySecurity
site:claude.ai "public/artifacts" "KEYWORD"
site:claude.ai/share "KEYWORD"
site:web.archive.org "claude.ai/share" "KEYWORD"

# HuggingFace Spaces — keys hardcoded in public Git repos
site:huggingface.co/spaces "KEYWORD"
site:huggingface.co/spaces "OPENAI_API_KEY" "KEYWORD"
site:huggingface.co/spaces "os.environ" "KEYWORD"
site:huggingface.co/spaces "st.secrets" "KEYWORD"
```

### Exposed AI Dashboards

```
intitle:"MLflow" inurl:"/mlflow" "KEYWORD"
intitle:"Label Studio" inurl:"/projects" "KEYWORD"
intitle:"Jupyter Notebook" inurl:"/tree" -"Login" "KEYWORD"
intitle:"Kubeflow" inurl:"/pipeline" "KEYWORD"
intitle:"Airflow - DAGs" "KEYWORD"
intitle:"Gradio" inurl:":7860" "KEYWORD"
intitle:"Streamlit" inurl:":8501" "KEYWORD"
intitle:"Open WebUI" "ollama" "KEYWORD"
intitle:"Qdrant Dashboard" "KEYWORD"
intitle:"ComfyUI" "KEYWORD"
intitle:"Stable Diffusion" "KEYWORD"
intitle:"LiteLLM" "proxy" "KEYWORD"
```

### AI Config & Credential Files

```
filetype:env "OPENAI_API_KEY" "KEYWORD"
filetype:env "ANTHROPIC_API_KEY" "KEYWORD"
filetype:env "HUGGINGFACE_TOKEN" "KEYWORD"
filetype:env "GROQ_API_KEY" "KEYWORD"
filetype:env "PINECONE_API_KEY" "KEYWORD"
filetype:env "WANDB_API_KEY" "KEYWORD"
filetype:env "DEEPSEEK_API_KEY" "KEYWORD"
filetype:env "OPENROUTER_API_KEY" "KEYWORD"
filetype:yaml "openai" "api_key" "KEYWORD"
filetype:json "anthropic" "api_key" "KEYWORD"
```

### MCP Server Config Exposure (v1.2.0)

```
# MCP server configs with embedded secrets (systemic RCE — Ox Security, April 2026)
site:github.com "mcpServers" "args" filetype:json "KEYWORD"
site:github.com "mcp.config" "apiKey" "KEYWORD"
site:github.com ".cursor" "mcpServers" filetype:json "KEYWORD"
site:github.com "windsurf" "mcp" "config" filetype:json "KEYWORD"

# Claude Code leak artifacts
site:github.com "claude-code" "leaked" "source" "KEYWORD"

# VS Code YOLO mode (CVE-2025-53773)
site:github.com "chat.tools.autoApprove" "true" filetype:json "KEYWORD"
```
---

## 🐙 GitHub Dorks

> Full collection: [`dorks/github/`](dorks/github/AI_GITHUB_DORKS.md)
>
> ⚠️ **Syntax note:** GitHub migrated to new Code Search. Use `path:*.env` instead of legacy `filename:.env`. Queries below use modern syntax where applicable.

### AI API Keys on GitHub

```
# OpenAI (project keys — current format since April 2024)
"sk-proj-" path:*.env "KEYWORD"
"sk-proj-" path:*.py "KEYWORD"
"OPENAI_API_KEY" path:*.env NOT "your_key" NOT "example" "KEYWORD"

# Anthropic
"sk-ant-api03" path:*.env "KEYWORD"
"ANTHROPIC_API_KEY" path:*.env "KEYWORD"

# Google AI / Gemini
"AIzaSy" path:*.env "generativelanguage" "KEYWORD"
"GOOGLE_API_KEY" path:*.env "gemini" "KEYWORD"

# HuggingFace
"hf_" path:*.env "KEYWORD"
"HF_TOKEN" path:*.env

# Groq
"gsk_" path:*.env "KEYWORD"
"GROQ_API_KEY" path:*.env "KEYWORD"

# Replicate
"r8_" path:*.env "KEYWORD"
"REPLICATE_API_TOKEN" path:*.env "KEYWORD"

# Vector DBs & MLOps
"PINECONE_API_KEY" path:*.env "KEYWORD"
"QDRANT_API_KEY" path:*.env "KEYWORD"
"WANDB_API_KEY" path:*.env "KEYWORD"
```

### MCP & Agent Config Leaks

```
path:mcp.json "api_key" "KEYWORD"
path:mcp.json "KEYWORD"
path:.cursor/mcp.json "KEYWORD"
"mcpServers" path:*.json "apiKey" "KEYWORD"
"mcpServers" path:*.json "OPENAI_API_KEY" "KEYWORD"
```

### System Prompts & Training Data

```
"system_prompt" path:*.py "you are" "KEYWORD"
"SYSTEM_PROMPT" path:*.env "KEYWORD"
path:prompts.yaml "system" "KEYWORD"
path:train.jsonl "prompt" "completion" "KEYWORD"
path:dataset.jsonl "instruction" "output" "KEYWORD"
```

### MCP & AI IDE Config Exploitation (v1.2.0)

```
# MCP STDIO configs (systemic RCE — 10+ CVEs)
path:*.json "mcpServers" "command" "args" "KEYWORD"
path:.vscode/settings.json "chat.tools.autoApprove" "true" "KEYWORD"

# Claude Code attack vectors
"CLAUDE.md" "permission" "allow"

# DeepSeek keys
path:*.env "DEEPSEEK_API_KEY" "KEYWORD"
"DEEPSEEK_API_KEY" NOT "your_key" NOT "example"
```
---

## 🔭 Shodan Queries

> Full collection: [`dorks/shodan/`](dorks/shodan/AI_SHODAN_DORKS.md)

### Self-Hosted LLMs

```
# Ollama — 240,000+ exposed instances worldwide
port:11434 product:"Ollama" "KEYWORD"
port:11434 http.html:"Ollama" "KEYWORD"
port:11434 "api/tags" "KEYWORD"

# vLLM / OpenAI-compatible
port:8000 "openai" "model" "KEYWORD"
http.title:"FastAPI" port:8000 "/v1/models" "KEYWORD"

# LM Studio
port:1234 "/v1/models" "KEYWORD"

# llama.cpp
port:8080 "llama" "completion" "KEYWORD"
```

### AI Agent Gateways — CRITICAL

```
# OpenClaw/Clawdbot — 4,000+ on Shodan, many with zero auth
# Enables RCE via prompt injection, API key theft, reverse shells
http.title:"Clawdbot Control" port:18789 "KEYWORD"
http.title:"OpenClaw" port:18789 "KEYWORD"
port:18789 "api/v1/status" "KEYWORD"
port:18789 "auth_mode" "KEYWORD"
```

### Gradio & Streamlit Apps

```
http.title:"Gradio" port:7860 "KEYWORD"
http.title:"Streamlit" port:8501 "KEYWORD"
http.title:"Stable Diffusion" port:7860 "KEYWORD"
http.title:"ComfyUI" "KEYWORD"
```

### Vector Databases

```
# Qdrant — NO auth by default
port:6333 "qdrant" "KEYWORD"
port:6333 "/collections" "KEYWORD"

# Weaviate
port:8080 "weaviate" "KEYWORD"

# Milvus
port:19530 "milvus" "KEYWORD"
```

### MLOps & Notebooks

```
# MLflow — CVE-2026-0545 (CVSS 9.1) RCE, no auth by default
http.title:"MLflow" port:5000 "KEYWORD"

# Jupyter — ~10,000+ on Shodan, targeted by botnets
http.title:"Jupyter Notebook" port:8888 -"Login" "KEYWORD"
http.title:"JupyterLab" port:8888 "KEYWORD"

# TensorBoard
http.title:"TensorBoard" port:6006 "KEYWORD"
```

### MCP & AI Agent Gateways (v1.2.0)

```
# MCP endpoints (systemic RCE — Ox Security)
http.html:"mcp" "tools" port:3000 "KEYWORD"
http.html:"Model Context Protocol" port:8080 "KEYWORD"

# nginx-ui MCP (CVE-2026-33032 — actively exploited, CVSS 9.8)
http.title:"Nginx UI" port:443 "KEYWORD"

# Flowise (CVE-2026-40933)
http.title:"Flowise" port:3000 "KEYWORD"

# vLLM (LLMjacking target)
http.html:"vLLM" port:8000 "KEYWORD"

# Open WebUI
http.title:"Open WebUI" port:3000 "KEYWORD"

# LiteLLM Proxy
http.title:"LiteLLM" port:4000 "KEYWORD"

# DeepSeek-style ClickHouse exposure
product:"ClickHouse" port:8123
```
---

## 🌐 Censys Queries

> Full collection: [`dorks/censys/`](dorks/censys/AI_CENSYS_QUERIES.md)

```
# Ollama (Censys found 25%+ on non-default ports)
services.port=11434 AND services.http.response.body:"Ollama" "KEYWORD"

# Gradio
services.port=7860 AND services.http.response.html_title:"Gradio" "KEYWORD"

# OpenClaw
services.port=18789 AND services.http.response.body:"Clawdbot" "KEYWORD"

# Vector DBs
services.port=6333 AND services.http.response.body:"qdrant" "KEYWORD"
services.port=8080 AND services.http.response.body:"weaviate" "KEYWORD"

# MLOps
services.port=5000 AND services.http.response.html_title:"MLflow" "KEYWORD"
services.port=8888 AND services.http.response.html_title:"Jupyter" "KEYWORD"

### MCP & New AI Infrastructure (v1.2.0)

# MCP endpoints
services.http.response.body:"Model Context Protocol" AND services.port=3000 "KEYWORD"

# Flowise (CVE-2026-40933)
services.http.response.html_title:"Flowise" AND services.port=3000 "KEYWORD"

# vLLM (LLMjacking target)
services.http.response.body:"vLLM" AND services.port=8000 "KEYWORD"

# nginx-ui MCP (CVE-2026-33032 — actively exploited)
services.http.response.html_title:"Nginx UI" AND services.port=443 "KEYWORD"

# ClickHouse exposure (DeepSeek-style)
services.port=8123 AND services.http.response.body:"ClickHouse" "KEYWORD"

# Open WebUI
services.http.response.html_title:"Open WebUI" "KEYWORD"

# LiteLLM
services.http.response.html_title:"LiteLLM" "KEYWORD"
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
| **Flowise** | 3000 | ❌ None | 🔴 Critical |
| **LiteLLM Proxy** | 4000 | ❌ None | 🔴 Critical |
| **Open WebUI** | 3000/8080 | ✅ Auth (default) | 🟡 High |
| **nginx-ui** | 443/9000 | ✅ Auth (bypassable) | 🔴 Critical |
| **ClickHouse** | 8123/9000 | ❌ None | 🔴 Critical |
| **TGI (HuggingFace)** | 8080 | ❌ None | 🟡 High |
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
port:18789 "api/v1" "KEYWORD"
http.title:"Clawdbot" OR http.title:"OpenClaw" "KEYWORD"

# GitHub
path:mcp.json "apiKey" "KEYWORD"
path:.cursor/mcp.json "KEYWORD"
"mcpServers" path:*.json "KEYWORD"
```

### Key Incidents

| Incident | Date | Impact |
|---|---|---|
| OpenClaw Shodan Exposure | Jan 2026 | 4,000+ agent gateways, many with zero auth and RCE |
| Operation Bizarre Bazaar | Dec 2025–Jan 2026 | 35,000 attacks on LLM/MCP endpoints; commercial resale |
| Smithery Registry Breach | 2025 | Fly.io token → control of 3,000+ MCP servers |
| mcp-remote CVE-2025-6514 | 2025 | Command injection in 437K+ installs |
| Cursor IDE MCP Trust Issue | 2025 | Persistent RCE via shared repo configs (CVSS 7.2-8.8) |
| MCP Systemic RCE (Ox Security) | Apr 2026 | 150M+ downloads, 200K servers, 10+ CVEs, 9/11 marketplaces poisoned |
| nginx-ui MCPwn (CVE-2026-33032) | Mar 2026 | CVSS 9.8, actively exploited, full Nginx takeover in 2 requests |
| Atlassian MCPwnfluence | Apr 2026 | CVE-2026-27825/27826 — RCE chain from LAN, no auth required |
| MCP TypeScript SDK Data Leak | Apr 2026 | CVE-2026-25536 — cross-client data leak in shared McpServer instances |
| Windsurf Zero-Click RCE | Apr 2026 | CVE-2026-30615 — zero-click prompt injection → local RCE via MCP |

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
- **Claude Mythos Preview / Project Glasswing** — Anthropic's unreleased model autonomously discovered thousands of 0-days in major OS/browsers. Limited to ~50 organizations. CVE-2026-4747 (OpenBSD 27-year RCE).
- **Claude Code Source Leak** — 59.8 MB source map published to npm (Mar 31, 2026). Critical 50-subcommand bypass vulnerability. Fake repos distributing Vidar/GhostSocks malware.
- **MCP "Mother of All Supply Chains"** — Ox Security found architectural RCE in MCP SDKs: 150M+ downloads, 10+ CVEs, 9/11 marketplaces poisoned. Anthropic declined protocol fix.
- **ChatGPT DNS Exfiltration** — Check Point discovered silent data leakage via DNS side channel in code execution sandbox. Patched Feb 20, 2026.
- **CVE-2025-53773: Copilot Wormable RCE** — Prompt injection enables YOLO mode, wormable across repositories. Patched Aug 2025.
- **OpenAI Codex CLI Command Injection** — Branch injection → lateral movement → codebase access. Patched Feb 2026.
- **300K+ ChatGPT Credentials on Dark Web** — IBM X-Force 2026: AI chatbot credentials are emerging infostealer target.
- **Ollama: 12,269 More Exposed** — LeakIX found additional exposed instances; maintainers continue rejecting auth PRs.
- **nginx-ui MCPwn** — CVE-2026-33032 actively exploited. Full Nginx takeover in 2 HTTP requests.
- **DeepSeek ClickHouse Exposure** — Wiz found 1M+ log entries with plaintext chats, API keys, backend details (Jan 2025).

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
| [**MCPSafetyScanner**](https://github.com/johnhalloran321/mcpSafetyScanner) | MCP server security auditing tool | Academic (Leidos) |
| [**Cisco AI Supply Chain Scanners**](https://blogs.cisco.com/ai/cisco-state-of-ai-security-2026-report) | Scanners for MCP, A2A, pickle files, agentic skill files | Cisco Talos |
| [**DorkEye**](https://github.com/search?q=DorkEye+OSINT) | Automated Google Dorking with multi-agent analysis pipeline | Open Source |

---

## 🚨 Detection Rules

> Full Sigma rules: [`detection-rules/SIGMA_RULES.md`](detection-rules/SIGMA_RULES.md)

12 Sigma detection rules covering:
- External access to Ollama (port 11434)
- AI API keys appearing in application logs
- Unauthorized LLM API access without Bearer tokens
- Exposed MCP servers with `auth_mode: none`
- Vector database unauthorized enumeration
- LLMjacking — anomalous inference spikes (>500 requests/hour)
- AI agent RCE via prompt injection (suspicious tool calls to bash/python_repl)
- MCP STDIO arbitrary command execution (CVE-2026-30615/30624/30616/40933)
- VS Code Copilot YOLO mode activation (CVE-2025-53773)
- nginx-ui MCP endpoint unauthenticated access (CVE-2026-33032, actively exploited)
- DNS-based data exfiltration from AI code execution sandboxes
- Claude Code 50+ subcommand pipeline deny rule bypass

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
| Ox Security | 150M+ MCP downloads affected by systemic RCE, 10+ CVEs, 9/11 marketplaces poisoned | [Blog](https://www.ox.security/blog/the-mother-of-all-ai-supply-chains-critical-systemic-vulnerability-at-the-core-of-the-mcp/) |
| Anthropic Red Team | Claude Mythos: thousands of 0-days, CVE-2026-4747, sandbox escape | [red.anthropic.com](https://red.anthropic.com/2026/mythos-preview/) |
| IBM X-Force | 300K+ ChatGPT creds on dark web, supply chain attacks 4x in 5 years | [Report](https://www.ibm.com/think/insights/more-2026-cyberthreat-trends) |
| Check Point | ChatGPT DNS exfiltration — silent data leakage via side channel | [Blog](https://blog.checkpoint.com/research/when-ai-trust-breaks-the-chatgpt-data-leakage-flaw-that-redefined-ai-vendor-security-trust/) |
| Zscaler ThreatLabz | Claude Code source leak + Vidar/GhostSocks malware lure | [Blog](https://www.zscaler.com/blogs/security-research/anthropic-claude-code-leak) |
| Cisco AI | State of AI Security 2026 — MCP, A2A, agentic AI scanners | [Report](https://blogs.cisco.com/ai/cisco-state-of-ai-security-2026-report) |
| LeakIX | 12,269 additional exposed Ollama instances, auth PR rejection critique | [Blog](https://blog.leakix.net/2026/02/ollama-exposed/) |
| CSA | Time-to-exploit now under 20 hours (Mythos briefing) | [HelpNetSecurity](https://www.helpnetsecurity.com/2026/04/15/anthropic-claude-mythos-ai-vulnerability-discovery/) |
| Wiz | Claude Mythos practical guidance — "Y2K moment" for cybersecurity | [Blog](https://www.wiz.io/blog/claude-mythos) |
| Wiz | DeepSeek ClickHouse exposure — 1M+ log entries with plaintext chats | [Blog](https://www.wiz.io/blog/wiz-research-uncovers-exposed-deepseek-database-leak) |

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

<p align="center"><b>Maintained by <a href="https://7waysecurity.co">7WaySecurity</a></b> · Last updated June 2026 · v1.3.0</p>
