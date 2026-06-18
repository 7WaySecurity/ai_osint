# Censys Queries for AI/ML Infrastructure

> 🔑 **`KEYWORD` convention (v1.3.0):** service fingerprints stay; append a scope
> clause so you only assess assets you own or are authorized to test. Censys's
> native scope fields are the cleanest replacement for `KEYWORD`:
>
> ```
> and autonomous_system.organization: "Your Company"
> and ip: 198.51.100.0/24
> and dns.names: yourcompany.com
> ```
>
> Replace the trailing `and KEYWORD` in each query with one of those.
>
> Censys found 25%+ of Ollama instances on non-default ports (443, 80, 8080).
> Port-only scanning misses a significant fraction.

## Self-Hosted LLMs
```
services.port=11434 AND services.http.response.body:"Ollama" and KEYWORD
services.port=11434 AND services.http.response.html_title:"Ollama" and KEYWORD
services.port=8000 AND services.http.response.body:"v1/models" and KEYWORD
services.port=1234 AND services.http.response.body:"lmstudio" and KEYWORD
services.port=8080 AND services.http.response.body:"llama" and KEYWORD
```

## AI Agents
```
services.port=18789 AND services.http.response.body:"Clawdbot" and KEYWORD
services.port=18789 AND services.http.response.body:"OpenClaw" and KEYWORD
services.port=18789 AND services.http.response.body:"auth_mode" and KEYWORD
```

## Web UIs
```
services.port=7860 AND services.http.response.html_title:"Gradio" and KEYWORD
services.port=8501 AND services.http.response.html_title:"Streamlit" and KEYWORD
services.http.response.html_title:"Stable Diffusion" and KEYWORD
services.http.response.html_title:"ComfyUI" and KEYWORD
```

## Vector Databases
```
services.port=6333 AND services.http.response.body:"qdrant" and KEYWORD
services.port=6333 AND services.http.response.body:"collections" and KEYWORD
services.port=8080 AND services.http.response.body:"weaviate" and KEYWORD
services.port=19530 and KEYWORD
services.port=9091 AND services.http.response.body:"milvus" and KEYWORD
```

## MLOps
```
services.port=5000 AND services.http.response.html_title:"MLflow" and KEYWORD
services.port=8888 AND services.http.response.html_title:"Jupyter" and KEYWORD
services.port=8888 AND services.http.response.html_title:"JupyterLab" and KEYWORD
services.http.response.html_title:"Kubeflow" and KEYWORD
services.http.response.html_title:"Label Studio" and KEYWORD
services.port=6006 AND services.http.response.html_title:"TensorBoard" and KEYWORD
```

## Scope Clauses (use these as your KEYWORD replacement)
```
autonomous_system.organization: "Your Company"
ip: 198.51.100.0/24
dns.names: yourcompany.com
```

> Cloud-provider AS names (`autonomous_system.name:"AMAZON"`, `"HETZNER"`,
> `"DIGITALOCEAN"`, `"GOOGLE"`, `"MICROSOFT"`) narrow by host but are **not** an
> authorization scope on their own — tie scope to assets you own/are authorized
> to test.

---

## 🆕 MCP & AI Agent Infrastructure (v1.2.0)

> MCP ecosystem: 7,000+ publicly accessible servers, up to 200,000 vulnerable instances (Ox Security, April 2026).

```
services.http.response.body:"Model Context Protocol" AND services.port=3000 and KEYWORD
services.http.response.body:"mcpServers" AND services.port=8080 and KEYWORD
services.http.response.body:"mcp_message" AND services.port=443 and KEYWORD

# Flowise (CVE-2026-40933)
services.http.response.html_title:"Flowise" AND services.port=3000 and KEYWORD
services.http.response.html_title:"FlowiseAI" and KEYWORD

# LiteLLM Proxy
services.http.response.html_title:"LiteLLM" and KEYWORD
services.http.response.body:"litellm" AND services.port=4000 and KEYWORD

# nginx-ui MCP (CVE-2026-33032 — actively exploited)
services.http.response.html_title:"Nginx UI" AND services.port=443 and KEYWORD
services.http.response.html_title:"Nginx UI" AND services.port=9000 and KEYWORD
```

---

## 🆕 vLLM / LLMjacking Targets (v1.2.0)

> Operation Bizarre Bazaar targets vLLM and OpenAI-compatible APIs for commercial resale.

```
services.http.response.body:"vLLM" AND services.port=8000 and KEYWORD
services.http.response.body:"OpenAI-compatible" AND services.port=8000 and KEYWORD
services.http.response.body:"/v1/models" AND services.port=8000 and KEYWORD
```

---

## 🆕 DeepSeek-Style ClickHouse Exposure (v1.2.0)

> Wiz found DeepSeek's ClickHouse exposed — no authentication, 1M+ logs.

```
services.port=8123 AND services.http.response.body:"ClickHouse" and KEYWORD
services.port=9000 AND services.http.response.body:"ClickHouse" and KEYWORD
services.port=8123 AND services.http.response.body:"play" and KEYWORD
```

---

## 🆕 Open WebUI & Ollama Frontends (v1.2.0)

```
services.http.response.html_title:"Open WebUI" and KEYWORD
services.http.response.html_title:"Open WebUI" AND services.port=3000 and KEYWORD

# Ollama without TLS (higher risk)
services.port=11434 AND services.http.response.body:"Ollama" AND NOT services.tls and KEYWORD
```

---

## 🆕 Additional AI Infrastructure (v1.2.0)

```
# Text Generation Inference (HuggingFace TGI)
services.http.response.body:"text-generation-inference" AND services.port=8080 and KEYWORD

# Langflow
services.http.response.html_title:"Langflow" and KEYWORD

# GPT Researcher
services.http.response.html_title:"GPT Researcher" and KEYWORD

# TabbyAPI (self-hosted coding assistant)
services.http.response.html_title:"Tabby" AND services.port=8080 and KEYWORD

# LocalAI
services.http.response.html_title:"LocalAI" and KEYWORD
```
