# Censys Queries for AI/ML Infrastructure

> Censys found 25%+ of Ollama instances on non-default ports (443, 80, 8080). Port-only scanning misses a significant fraction.

## Self-Hosted LLMs
```
services.port=11434 AND services.http.response.body:"Ollama"
services.port=11434 AND services.http.response.html_title:"Ollama"
services.port=8000 AND services.http.response.body:"v1/models"
services.port=1234 AND services.http.response.body:"lmstudio"
services.port=8080 AND services.http.response.body:"llama"
```

## AI Agents
```
services.port=18789 AND services.http.response.body:"Clawdbot"
services.port=18789 AND services.http.response.body:"OpenClaw"
services.port=18789 AND services.http.response.body:"auth_mode"
```

## Web UIs
```
services.port=7860 AND services.http.response.html_title:"Gradio"
services.port=8501 AND services.http.response.html_title:"Streamlit"
services.http.response.html_title:"Stable Diffusion"
services.http.response.html_title:"ComfyUI"
```

## Vector Databases
```
services.port=6333 AND services.http.response.body:"qdrant"
services.port=6333 AND services.http.response.body:"collections"
services.port=8080 AND services.http.response.body:"weaviate"
services.port=19530
services.port=9091 AND services.http.response.body:"milvus"
```

## MLOps
```
services.port=5000 AND services.http.response.html_title:"MLflow"
services.port=8888 AND services.http.response.html_title:"Jupyter"
services.port=8888 AND services.http.response.html_title:"JupyterLab"
services.http.response.html_title:"Kubeflow"
services.http.response.html_title:"Label Studio"
services.port=6006 AND services.http.response.html_title:"TensorBoard"
```

## By Cloud Provider
```
services.port=11434 AND autonomous_system.name:"AMAZON"
services.port=11434 AND autonomous_system.name:"HETZNER"
services.port=11434 AND autonomous_system.name:"DIGITALOCEAN"
services.port=11434 AND autonomous_system.name:"GOOGLE"
services.port=11434 AND autonomous_system.name:"MICROSOFT"
```
---

## 🆕 MCP & AI Agent Infrastructure (v1.2.0)

> MCP ecosystem: 7,000+ publicly accessible servers, up to 200,000 vulnerable instances (Ox Security, April 2026).

```
# MCP HTTP/SSE endpoints
services.http.response.body:"Model Context Protocol" AND services.port=3000
services.http.response.body:"mcpServers" AND services.port=8080
services.http.response.body:"mcp_message" AND services.port=443

# Flowise (CVE-2026-40933)
services.http.response.html_title:"Flowise" AND services.port=3000
services.http.response.html_title:"FlowiseAI"

# LiteLLM Proxy
services.http.response.html_title:"LiteLLM"
services.http.response.body:"litellm" AND services.port=4000

# nginx-ui MCP (CVE-2026-33032 — actively exploited)
services.http.response.html_title:"Nginx UI" AND services.port=443
services.http.response.html_title:"Nginx UI" AND services.port=9000
```

---

## 🆕 vLLM / LLMjacking Targets (v1.2.0)

> Operation Bizarre Bazaar targets vLLM and OpenAI-compatible APIs for commercial resale via silver[.]inc.

```
services.http.response.body:"vLLM" AND services.port=8000
services.http.response.body:"OpenAI-compatible" AND services.port=8000
services.http.response.body:"/v1/models" AND services.port=8000
```

---

## 🆕 DeepSeek-Style ClickHouse Exposure (v1.2.0)

> Wiz found DeepSeek's ClickHouse at oauth2callback.deepseek.com:9000 — no authentication, 1M+ logs exposed.

```
services.port=8123 AND services.http.response.body:"ClickHouse"
services.port=9000 AND services.http.response.body:"ClickHouse"
services.port=8123 AND services.http.response.body:"play"
```

---

## 🆕 Open WebUI & Ollama Frontends (v1.2.0)

```
services.http.response.html_title:"Open WebUI"
services.http.response.html_title:"Open WebUI" AND services.port=3000

# Ollama without TLS (higher risk)
services.port=11434 AND services.http.response.body:"Ollama" AND NOT services.tls
```

---

## 🆕 Additional AI Infrastructure (v1.2.0)

```
# Text Generation Inference (HuggingFace TGI)
services.http.response.body:"text-generation-inference" AND services.port=8080

# Langflow
services.http.response.html_title:"Langflow"

# GPT Researcher
services.http.response.html_title:"GPT Researcher"

# TabbyAPI (self-hosted coding assistant)
services.http.response.html_title:"Tabby" AND services.port=8080

# LocalAI
services.http.response.html_title:"LocalAI"
```
