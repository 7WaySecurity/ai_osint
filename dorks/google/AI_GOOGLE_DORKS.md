# Google Dorks for AI/ML OSINT

> 🔑 **`KEYWORD` convention (v1.3.0):** secret-seeking value strings have been
> replaced with a `"KEYWORD"` placeholder. Replace `KEYWORD` with a term you are
> **authorized** to search for — your own brand, an owned domain, an internal
> project name, or an engagement scope. Service fingerprints (titles, paths,
> ports, env-var names, key prefixes) are kept as-is because they identify the
> *service*, not a secret. See the repo README for the rationale.
>
> ⚠️ **Status notes** reflect **June 2026** verification.

---

## AI Chat Platforms — Exposed Conversations

### Grok (xAI) — 🟢 HIGHLY EFFECTIVE (verified Jun 2026)
> 370,000+ conversations indexed; historically no opt-out for indexing. Confirmed still broadly indexed in June 2026. Scope with your own brand/domain.

```
site:grok.com/share "KEYWORD"
site:grok.com/share intext:"KEYWORD"
site:grok.com/share "KEYWORD" "internal"
```

### ChatGPT (OpenAI) — 🟡 DEGRADED (re-verified Jun 2026)
> Discoverability feature removed Aug 1, 2025; OpenAI is de-indexing shares with Google. **Cached and third-party-archived copies persist** and spot checks still return occasional live results — degraded, not dead. Bing/DuckDuckGo sometimes retain more than Google.

```
site:chatgpt.com/share "KEYWORD"
site:chatgpt.com/share intext:"KEYWORD"
```

### Perplexity AI — 🟢 ACTIVE

```
site:perplexity.ai/search "KEYWORD"
```

### Claude (Anthropic) — 🟢 ACTIVE
> ~600 Claude conversations indexed by Google (Forbes, Sep 2025). 143,000+ LLM conversations (incl. Claude) archived on Archive.org. Published artifacts are publicly accessible and indexable.

```
# Published Artifacts — publicly accessible apps, tools, code
# 🔥 Original dork by 7WaySecurity
site:claude.ai "public/artifacts" "KEYWORD"

# Shared conversations — scope to your own brand/domain
site:claude.ai/share "KEYWORD"

# Artifact catalog — public directory of published artifacts
site:claude.ai/catalog "KEYWORD"

# Archive.org Wayback Machine — enumerate captures for YOUR OWN domain
# curl "https://web.archive.org/cdx/search/cdx?url=claude.ai/share/*&output=json&limit=10000"
site:web.archive.org "claude.ai/share" "KEYWORD"
```

---

## HuggingFace — 🟢 ACTIVE (verified Jun 2026)
> Spaces source code is in public Git repos. Despite the Secrets mechanism, developers sometimes hardcode keys in app.py. Scope with your own org/project as `KEYWORD`.

```
site:huggingface.co/spaces "OPENAI_API_KEY" "KEYWORD"
site:huggingface.co/spaces "ANTHROPIC_API_KEY" "KEYWORD"
site:huggingface.co/spaces "os.environ" "KEYWORD"
site:huggingface.co/spaces "st.secrets" "KEYWORD"
site:huggingface.co/spaces "API_KEY" "KEYWORD"
site:huggingface.co ".env" "KEYWORD"
site:huggingface.co "training data" "KEYWORD"
site:huggingface.co "fine-tuned" "KEYWORD"
```

---

## Exposed AI Dashboards — 🟢 ACTIVE
> Product titles/ports are fingerprints and stay. Add `site:yourdomain.com` (or set `KEYWORD` via an extra term) to scope to your own assets.

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

> ⚠️ `intitle:"Stable Diffusion" inurl:":7860"` — Limited effectiveness. Google rarely indexes URLs with non-standard ports. Use Shodan instead: `http.title:"Stable Diffusion" port:7860`.

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
> Env-var names are file fingerprints and stay. `KEYWORD` scopes to your own org/domain so this stays a self-audit, not a third-party dragnet.

```
filetype:env "OPENAI_API_KEY" "KEYWORD"
filetype:env "ANTHROPIC_API_KEY" "KEYWORD"
filetype:env "HUGGINGFACE_TOKEN" "KEYWORD"
filetype:env "HF_TOKEN" "KEYWORD"
filetype:env "REPLICATE_API_TOKEN" "KEYWORD"
filetype:env "COHERE_API_KEY" "KEYWORD"
filetype:env "MISTRAL_API_KEY" "KEYWORD"
filetype:env "GROQ_API_KEY" "KEYWORD"
filetype:env "ELEVENLABS_API_KEY" "KEYWORD"
filetype:env "STABILITY_API_KEY" "KEYWORD"
filetype:env "DEEPSEEK_API_KEY" "KEYWORD"
filetype:env "TOGETHER_API_KEY" "KEYWORD"
filetype:env "PINECONE_API_KEY" "KEYWORD"
filetype:env "QDRANT_API_KEY" "KEYWORD"
filetype:env "WANDB_API_KEY" "KEYWORD"
filetype:env "OPENROUTER_API_KEY" "KEYWORD"
filetype:yaml "openai" "api_key" "KEYWORD"
filetype:json "openai" "api_key" "KEYWORD"
filetype:toml "openai" "api_key" "KEYWORD"
filetype:json "mcpServers" "apiKey" "KEYWORD"
```

---

## AI Model & Training Data — 🟡 MIXED

> ⚠️ `filetype:gguf` does NOT work — Google doesn't index binary model files. Use `intitle:"index of" .gguf` for open directory listings instead.

```
# Works for text-based formats
filetype:jsonl "prompt" "completion" "KEYWORD"
filetype:jsonl "instruction" "output" "KEYWORD"
filetype:csv "prompt" "response" "KEYWORD"
filetype:parquet "train" "KEYWORD"

# Open directory listings for model files
intitle:"index of" .gguf "KEYWORD"
intitle:"index of" .safetensors "KEYWORD"
intitle:"index of" "pytorch_model" "KEYWORD"
```

---

## Cloud-Hosted AI — 🟢 ACTIVE

```
site:*.amazonaws.com "jupyter" "KEYWORD"
site:*.amazonaws.com "sagemaker" "KEYWORD"
site:*.fly.dev "ollama" "KEYWORD"
site:*.fly.dev "mcp" "KEYWORD"
site:*.railway.app "ollama" "KEYWORD"
site:*.render.com "gradio" "KEYWORD"
site:*.hf.space "KEYWORD"
```

---

## 🆕 MCP Server Configuration Exposure (v1.2.0)

> MCP supply chain now constitutes 150M+ downloads. Ox Security found systemic RCE across MCP SDKs (April 2026).

```
site:github.com "mcp_servers" "command" filetype:json "KEYWORD"
site:github.com "mcpServers" "args" filetype:json "KEYWORD"
site:github.com path:*.json "stdio" "mcp" "command" "KEYWORD"
site:github.com "mcp.config" "apiKey" "KEYWORD"
site:github.com ".cursor" "mcpServers" filetype:json "KEYWORD"

# Windsurf IDE configs (CVE-2026-30615 — zero-click RCE)
site:github.com "windsurf" "mcp" "config" filetype:json "KEYWORD"
site:github.com ".windsurf" "mcpServers" "KEYWORD"
```

---

## 🆕 Claude Code Source Leak Artifacts (v1.2.0)

> On March 31, 2026 Anthropic accidentally published a 59.8 MB source map for Claude Code v2.1.88 to npm. Fake repos are distributing Vidar/GhostSocks malware.

```
# Legitimate source analysis
site:npm.io "@anthropic-ai/claude-code"
site:github.com "@anthropic-ai/claude-code" ".map"

# ⚠️ Malware lure detection — fake leaked repos
site:github.com "claude-code" "leaked" "source"
site:github.com "claude code" "unlocked" "enterprise"
```

---

## 🆕 AI Agent Configuration Leaks (v1.2.0)

```
# Agent Zero configs (CVE-2026-30624 — RCE via MCP config)
site:github.com "agent-zero" "mcp" filetype:json "KEYWORD"

# Flowise configs (CVE-2026-40933 — RCE via MCP adapters)
site:github.com "flowise" "mcp" "stdio" "KEYWORD"

# Provider keys in various formats — scope with KEYWORD to your org
site:github.com "CLAUDE_API_KEY" filetype:env "KEYWORD"
site:github.com "ANTHROPIC_API_KEY" filetype:yaml "KEYWORD"

# Codex (OpenAI) tokens
site:github.com "codex" "GITHUB_TOKEN" filetype:env "KEYWORD"

# DeepSeek exposure
site:github.com "deepseek" "DEEPSEEK_API_KEY" "KEYWORD"
site:github.com "deepseek" filetype:env "KEYWORD"
```

---

## 🆕 AI IDE YOLO Mode Detection (v1.2.0)

> CVE-2025-53773 (CVSS 7.8): Prompt injection enables GitHub Copilot to activate "YOLO mode" and execute arbitrary commands.

```
# VS Code autoApprove configs
site:github.com "chat.tools.autoApprove" "true" filetype:json "KEYWORD"
site:github.com "settings.json" "autoApprove" "copilot" "KEYWORD"
```

---

## 🆕 DeepSeek Infrastructure Exposure (v1.2.0)

> Wiz found a publicly accessible ClickHouse database with 1M+ log entries, plaintext chat histories, and API keys (Jan 2025).

```
site:github.com "deepseek" "DEEPSEEK_API_KEY" "KEYWORD"
site:github.com "deepseek" filetype:env "KEYWORD"
site:github.com "deepseek" "ClickHouse" "oauth2callback" "KEYWORD"
```

---

## 🆕 Project Glasswing / Mythos References (v1.2.0)

> Claude Mythos Preview autonomously found thousands of 0-days including a 27-year-old OpenBSD RCE.

```
site:github.com "mythos" "vulnerability" "exploit" "KEYWORD"
site:github.com "glasswing" "anthropic" "KEYWORD"
site:github.com "mcpSafetyScanner" "KEYWORD"
```
