# Google Dorks for AI/ML OSINT

> ⚠️ **Status notes** indicate current effectiveness based on April 2026 verification.

---

## AI Chat Platforms — Exposed Conversations

### Grok (xAI) — 🟢 HIGHLY EFFECTIVE
> 370,000+ conversations indexed. No opt-out for search engine indexing. xAI treats this as expected behavior.

```
site:grok.com/share "password"
site:grok.com/share "API key"
site:grok.com/share "secret"
site:grok.com/share "token"
site:grok.com/share "credentials"
site:grok.com/share "sk-proj"
site:grok.com/share "AWS"
site:grok.com/share "database"
site:grok.com/share "mongodb://"
site:grok.com/share "postgres://"
site:grok.com/share "private key"
site:grok.com/share "admin"
```

### ChatGPT (OpenAI) — 🟡 DEGRADED
> OpenAI removed discoverability feature Aug 1, 2025. Google de-indexed most results. **Try DuckDuckGo** which continued surfacing content after Google stopped.

```
site:chatgpt.com/share "API key"
site:chatgpt.com/share "sk-proj"
site:chatgpt.com/share "sk-ant"
site:chatgpt.com/share "password"
site:chatgpt.com/share "secret"
site:chatgpt.com/share "token"
site:chatgpt.com/share "AWS_SECRET"
site:chatgpt.com/share "connection string"
site:chatgpt.com/share ".env"
site:chatgpt.com/share "private key"
site:chatgpt.com/share "ssh-rsa"
site:chatgpt.com/share "jdbc:"
site:chatgpt.com/share "mongodb://"
site:chatgpt.com/share "stripe" "sk_live"
site:chatgpt.com/share "firebase"
site:chatgpt.com/share "supabase"
site:chatgpt.com/share "internal" "architecture"
site:chatgpt.com/share "vpn" "credentials"
```

### Perplexity AI — 🟢 ACTIVE

```
site:perplexity.ai/search "API key"
site:perplexity.ai/search "password"
site:perplexity.ai/search "sk-proj"
site:perplexity.ai/search "credentials"
site:perplexity.ai/search "internal"
```

---

## HuggingFace — 🟢 ACTIVE
> Spaces source code is in public Git repos. Despite Secrets mechanism, developers hardcode keys in app.py.

```
site:huggingface.co/spaces "sk-proj"
site:huggingface.co/spaces "OPENAI_API_KEY"
site:huggingface.co/spaces "ANTHROPIC_API_KEY"
site:huggingface.co/spaces "password"
site:huggingface.co/spaces "secret"
site:huggingface.co/spaces "token"
site:huggingface.co/spaces "os.environ"
site:huggingface.co/spaces "st.secrets"
site:huggingface.co/spaces "API_KEY"
site:huggingface.co "AWS_ACCESS_KEY_ID"
site:huggingface.co ".env" "KEY"
site:huggingface.co "database_url"
site:huggingface.co "training data" "internal"
site:huggingface.co "fine-tuned" "proprietary"
```

---

## Exposed AI Dashboards — 🟢 ACTIVE

```
intitle:"MLflow" inurl:"/mlflow"
intitle:"MLflow" "experiments"
intitle:"Label Studio" inurl:"/projects"
intitle:"Jupyter Notebook" inurl:"/tree" -"Login" -"Password"
intitle:"JupyterLab"
intitle:"Kubeflow" inurl:"/pipeline"
intitle:"Airflow - DAGs"
intitle:"Gradio" inurl:":7860"
intitle:"Streamlit" inurl:":8501"
intitle:"Open WebUI" "ollama"
intitle:"LobeChat"
intitle:"LibreChat"
intitle:"text-generation-webui"
intitle:"LiteLLM" "proxy"
intitle:"ComfyUI"
intitle:"InvokeAI"
intitle:"Fooocus"
intitle:"Qdrant Dashboard"
```

> ⚠️ `intitle:"Stable Diffusion" inurl:":7860"` — Limited effectiveness. Google rarely indexes URLs with non-standard ports. Use Shodan instead: `http.title:"Stable Diffusion" port:7860`

---

## OpenAI-Compatible API Endpoints — 🟢 ACTIVE

```
inurl:"/v1/models" "openai" -site:openai.com
inurl:"/v1/chat/completions" -site:openai.com
inurl:"/api/tags" "ollama"
inurl:"/v1/models" inurl:":8000"
inurl:"/v1/models" inurl:":1234"
```

---

## AI Config Files — 🟢 ACTIVE

```
filetype:env "OPENAI_API_KEY"
filetype:env "ANTHROPIC_API_KEY"
filetype:env "HUGGINGFACE_TOKEN"
filetype:env "HF_TOKEN"
filetype:env "REPLICATE_API_TOKEN"
filetype:env "COHERE_API_KEY"
filetype:env "MISTRAL_API_KEY"
filetype:env "GROQ_API_KEY"
filetype:env "ELEVENLABS_API_KEY"
filetype:env "STABILITY_API_KEY"
filetype:env "DEEPSEEK_API_KEY"
filetype:env "TOGETHER_API_KEY"
filetype:env "PINECONE_API_KEY"
filetype:env "QDRANT_API_KEY"
filetype:env "WANDB_API_KEY"
filetype:env "OPENROUTER_API_KEY"
filetype:yaml "openai" "api_key"
filetype:json "openai" "api_key"
filetype:toml "openai" "api_key"
filetype:json "mcpServers" "apiKey"
```

---

## AI Model & Training Data — 🟡 MIXED

> ⚠️ `filetype:gguf` does NOT work — Google doesn't index binary model files. Use `intitle:"index of" .gguf` for open directory listings instead.

```
# Works for text-based formats
filetype:jsonl "prompt" "completion"
filetype:jsonl "instruction" "output"
filetype:csv "prompt" "response"
filetype:parquet "train"

# Open directory listings for model files
intitle:"index of" .gguf
intitle:"index of" .safetensors
intitle:"index of" "pytorch_model"
```

---

## Cloud-Hosted AI — 🟢 ACTIVE

```
site:*.amazonaws.com "jupyter"
site:*.amazonaws.com "sagemaker"
site:*.fly.dev "ollama"
site:*.fly.dev "mcp"
site:*.railway.app "ollama"
site:*.render.com "gradio"
site:*.hf.space
```
