# Shodan Dorks for AI/ML Infrastructure

> 🔑 **`KEYWORD` convention (v1.3.0):** service fingerprints (titles, ports,
> html markers) are kept — they identify the service. Append a scope so you only
> assess assets you own or are authorized to test. Shodan's native filters are
> the cleanest scope:
>
> ```
> org:"Your Company"    net:198.51.100.0/24    hostname:yourcompany.com
> ```
>
> Where a query below ends in `KEYWORD`, replace it with one of those filters.
>
> All ports verified against official documentation (Jun 2026). Exposure counts
> from SentinelOne, Cisco Talos, and Censys research (2025–2026).

---

## Self-Hosted LLMs

### Ollama — 175,000+ exposed (SentinelOne/Censys Jan 2026)
```
"Ollama is running" port:11434 KEYWORD
port:11434 http.html:"Ollama" KEYWORD
port:11434 "api/tags" KEYWORD
port:11434 http.status:200 KEYWORD
```

### vLLM / OpenAI-Compatible (Port 8000)
```
port:8000 "openai" "model" KEYWORD
http.title:"FastAPI" port:8000 "v1/models" KEYWORD
"/v1/chat/completions" port:8000 KEYWORD
"/v1/models" port:8000 KEYWORD
```

### llama.cpp / LM Studio / GPT4All / LocalAI / KoboldCpp
```
port:8080 "llama" "completion" KEYWORD
port:1234 "/v1/models" KEYWORD
port:4891 "/v1/models" KEYWORD
http.title:"LocalAI" port:8080 KEYWORD
http.title:"KoboldAI" KEYWORD
```

---

## AI Agent Gateways — CRITICAL

### OpenClaw / Clawdbot — 4,000+ on Shodan
```
http.title:"Clawdbot Control" port:18789 KEYWORD
http.title:"OpenClaw" port:18789 KEYWORD
port:18789 "api/v1/status" KEYWORD
port:18789 "auth_mode" KEYWORD
port:18789 "agent_id" KEYWORD
```

### Open WebUI / LobeChat / LibreChat / LiteLLM
```
http.title:"Open WebUI" KEYWORD
http.title:"LobeChat" KEYWORD
http.title:"LibreChat" KEYWORD
http.title:"LiteLLM" KEYWORD
port:4000 "litellm" KEYWORD
```

---

## Gradio & Streamlit

```
http.title:"Gradio" port:7860 KEYWORD
port:7860 http.status:200 KEYWORD
http.title:"Streamlit" port:8501 KEYWORD
http.title:"Stable Diffusion" port:7860 KEYWORD
http.title:"AUTOMATIC1111" KEYWORD
http.title:"ComfyUI" KEYWORD
http.title:"Fooocus" KEYWORD
http.title:"InvokeAI" KEYWORD
```

---

## Vector Databases

```
# Qdrant — No auth by default
port:6333 "qdrant" KEYWORD
port:6333 "/collections" KEYWORD
port:6334 "qdrant" KEYWORD

# Weaviate
port:8080 "weaviate" KEYWORD

# Milvus
port:19530 "milvus" KEYWORD
port:9091 "milvus" KEYWORD

# ChromaDB (v2 API, /api/v2; no auth by default, binds localhost)
port:8000 "chroma" KEYWORD
http.html:"chromadb" port:8000 KEYWORD
```

---

## MLOps

```
# MLflow — No auth by default, CVE-2026-0545 (CVSS 9.1)
http.title:"MLflow" port:5000 KEYWORD
port:5000 "/mlflow" KEYWORD

# Jupyter — ~10,000+ on Shodan, targeted by botnets
http.title:"Jupyter Notebook" port:8888 KEYWORD
http.title:"JupyterLab" port:8888 KEYWORD

# Kubeflow / Label Studio / Airflow / TensorBoard
http.title:"Kubeflow" port:8080 KEYWORD
http.title:"Label Studio" KEYWORD
http.title:"Airflow" "DAGs" KEYWORD
http.title:"TensorBoard" port:6006 KEYWORD
```

---

## Scope Filters (use these as your KEYWORD replacement)

```
# By organization / netblock / host — your authorized scope
org:"Your Company"
net:198.51.100.0/24
hostname:yourcompany.com

# Cloud provider (combine with the above)
org:"Amazon"   org:"Google"   org:"Microsoft"
org:"DigitalOcean"   org:"Hetzner"   org:"OVH"

# Unauthenticated narrowing (EXCLUSION filter — finds services that do NOT
# present auth challenges; the quoted words are negated, not sought)
http.status:200 -"401" -"403" -"login"
```

> ⚠️ Country filters (`country:"US"`, etc.) are **not** a valid authorization
> scope by themselves — scoping must tie to assets you own/are authorized to test.

---

## 🆕 MCP Servers & AI Agent Gateways (v1.2.0)

> MCP architecture has systemic RCE — 200,000 vulnerable instances estimated (Ox Security, April 2026).

```
http.html:"mcp" "tools" port:3000 KEYWORD
http.html:"Model Context Protocol" port:8080 KEYWORD
http.html:"mcp_message" port:443 KEYWORD

# nginx-ui with MCP (CVE-2026-33032 — CVSS 9.8, actively exploited)
http.title:"Nginx UI" port:443 KEYWORD
http.title:"nginx ui" port:9000 KEYWORD
http.title:"Nginx UI" "/mcp" KEYWORD
```

---

## 🆕 AI Coding Assistants & IDE Backends (v1.2.0)

```
http.title:"Open WebUI" port:3000 KEYWORD
http.title:"Flowise" port:3000 KEYWORD
http.title:"FlowiseAI" KEYWORD
http.title:"LiteLLM" port:4000 KEYWORD
http.html:"litellm" "proxy" port:4000 KEYWORD
http.title:"GPT Researcher" KEYWORD
http.title:"Langflow" port:7860 KEYWORD
```

---

## 🆕 vLLM Servers — LLMjacking Targets (v1.2.0)

> Operation Bizarre Bazaar actively targets vLLM servers and OpenAI-compatible APIs for commercial resale (Pillar Security).

```
http.html:"vLLM" port:8000 KEYWORD
"vllm" port:8000 "model" KEYWORD
http.html:"vllm" "/v1/models" port:8000 KEYWORD
```

---

## 🆕 DeepSeek-Style ClickHouse Exposure (v1.2.0)

> Wiz Research found DeepSeek's ClickHouse DB exposed with 1M+ log entries including plaintext chat histories and API keys.

```
product:"ClickHouse" port:8123 KEYWORD
product:"ClickHouse" port:9000 -"Login" KEYWORD
http.html:"ClickHouse" "play" port:8123 KEYWORD
```

---

## 🆕 Additional LLM Inference Servers (v1.2.0)

```
# Text Generation Inference (HuggingFace TGI)
http.html:"text-generation-inference" port:8080 KEYWORD
http.html:"tgi" "/generate" port:80 KEYWORD

# TabbyAPI / Tabby (self-hosted coding assistant)
http.title:"Tabby" port:8080 KEYWORD
http.html:"tabbyAPI" port:5000 KEYWORD

# LocalAI
http.title:"LocalAI" port:8080 KEYWORD
```
