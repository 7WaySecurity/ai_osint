# GitHub Dorks for AI/ML Secret Discovery

> ⚠️ **Modern GitHub Code Search syntax** used throughout. Legacy `filename:` and `extension:` replaced with `path:*.ext`. Legacy `in:file` dropped (implied in new search).
>
> 📊 **Scale:** GitGuardian 2026 report found AI credential leaks surged **81% YoY** to 1,275,105 leaked AI secrets. Claude Code commits leaked at **3.2%** — double the human baseline.

---

## OpenAI Keys
```
"sk-proj-" path:*.env
"sk-proj-" path:*.py
"sk-proj-" path:*.js
"sk-proj-" path:*.ts
"sk-proj-" path:*.yaml
"OPENAI_API_KEY" path:*.env NOT "your_key" NOT "example" NOT "placeholder"
"openai.api_key" path:*.py
```

## Anthropic Keys
> Anthropic became a GitHub secret scanning partner Aug 20, 2024. New commits trigger push protection, but **historical commits remain searchable**. OAuth tokens use `sk-ant-oat01-` prefix.
```
"sk-ant-api03" path:*.env
"sk-ant-api03" path:*.py
"sk-ant-api03" path:*.js
"sk-ant-api03" path:*.ts
"sk-ant-oat01" path:*.env
"ANTHROPIC_API_KEY" path:*.env NOT "your_key"
"CLAUDE_API_KEY" path:*.env
"claude" "api_key" path:*.py NOT "example"
"anthropic" "api_key" path:*.yaml
"anthropic" "api_key" path:*.json
```

## Claude Code Configs
> Claude Code uses ~/.claude/ for configs. May contain API keys and project hooks.
```
path:.claude/settings.json
path:.claude.json "api_key"
"ANTHROPIC_API_KEY" path:*.sh "claude"
"claude-code" path:docker-compose.yml
path:.claude/CLAUDE.md
```

## Google AI / Gemini
> ⚠️ `AIzaSy` prefix is shared across ALL Google Cloud APIs. A Maps key can silently access Gemini if the Generative Language API is enabled.
```
"AIzaSy" path:*.env "generativelanguage"
"AIzaSy" path:*.env "gemini"
"GOOGLE_API_KEY" path:*.env "gemini"
"GOOGLE_AI_API_KEY" path:*.env
```

## HuggingFace Tokens
```
"hf_" path:*.env
"HUGGINGFACE_TOKEN" path:*.env
"HF_TOKEN" path:*.env
```

## Replicate
```
"r8_" path:*.env
"REPLICATE_API_TOKEN" path:*.env
```

## Cohere
```
"COHERE_API_KEY" path:*.env
```

## Mistral
```
"MISTRAL_API_KEY" path:*.env
```

## ElevenLabs
```
"ELEVENLABS_API_KEY" path:*.env
"xi-api-key" path:*.py
```

## Groq
```
"gsk_" path:*.env
"GROQ_API_KEY" path:*.env
```

## Together AI
```
"TOGETHER_API_KEY" path:*.env
```

## DeepSeek
```
"DEEPSEEK_API_KEY" path:*.env
```

## Vector Databases
```
"PINECONE_API_KEY" path:*.env
"QDRANT_API_KEY" path:*.env
"WEAVIATE_API_KEY" path:*.env
```

## MLOps
```
"WANDB_API_KEY" path:*.env
"MLFLOW_TRACKING_URI" path:*.env
"NEPTUNE_API_TOKEN" path:*.env
"COMET_API_KEY" path:*.env
```

## OpenRouter
```
"OPENROUTER_API_KEY" path:*.env
```

## Stability AI
```
"STABILITY_API_KEY" path:*.env
```

---

## MCP & AI Agent Config Leaks
> 📊 24,008 unique secrets exposed in MCP configs in its first year (GitGuardian 2026).
```
path:mcp.json "api_key"
path:mcp.json "token"
path:mcp.json "secret"
path:openclaw.json "api_key"
path:.cursor/mcp.json
"mcpServers" path:*.json "apiKey"
"mcpServers" path:*.json "OPENAI_API_KEY"
"mcpServers" path:*.json "token"
```

## System Prompts
```
"system_prompt" path:*.py "you are"
"SYSTEM_PROMPT" path:*.env
"system_message" path:*.py "you are a"
path:prompts.yaml "system"
path:prompts.json "system"
```

## AI Infrastructure Configs
```
path:docker-compose.yml "ollama"
path:docker-compose.yml "chromadb"
path:docker-compose.yml "qdrant"
path:docker-compose.yml "weaviate"
path:docker-compose.yml "milvus"
path:docker-compose.yml "vllm"
```

---

## 🆕 MCP Configuration Leaks (v1.2.0)

> Systemic RCE in MCP STDIO transport affects every SDK language. 10+ High/Critical CVEs issued (Ox Security, April 2026).

```
# MCP JSON configs with commands and args
path:*.json "mcpServers" "command" "args"
path:.cursor/mcp.json "apiKey"
path:mcp.json "stdio" "env"
path:*.json "mcp_servers" "OPENAI_API_KEY"

# Windsurf IDE (CVE-2026-30615)
path:*.json "windsurf" "mcpServers"
```

---

## 🆕 Claude Code & Anthropic Token Patterns (v1.2.0)

> Claude Code source map leaked March 31, 2026. New token prefix `sk-ant-oat01-` for OAuth.

```
# Active API keys (exclude examples/tests)
"sk-ant-api03-" NOT "example" NOT "test" NOT "xxx"
"sk-ant-oat01-" NOT "example"

# Claude Code artifacts
"@anthropic-ai/claude-code" "source" "map"

# CLAUDE.md permission files (attack vector for 50-subcommand bypass)
"CLAUDE.md" "permission" "allow"
path:CLAUDE.md "bash" "allow"
```

---

## 🆕 AI IDE YOLO Mode / Config Exploitation (v1.2.0)

> CVE-2025-53773: Copilot modifies `.vscode/settings.json` to enable autoApprove via prompt injection.

```
# VS Code YOLO mode activation
path:.vscode/settings.json "chat.tools.autoApprove" "true"
path:.vscode/settings.json "github.copilot" "autoApprove"

# Tasks.json MCP manipulation
path:.vscode/tasks.json "mcp" "command"
```

---

## 🆕 AI Agent Secrets (v1.2.0)

```
# DeepSeek
path:*.env "DEEPSEEK_API_KEY"
"DEEPSEEK_API_KEY" NOT "your_key" NOT "example"

# Groq (expanding existing)
path:*.env "GROQ_API_KEY" OR "gsk_"
"gsk_" path:*.py NOT "example"

# Mistral
path:*.env "MISTRAL_API_KEY"
"MISTRAL_API_KEY" path:*.yaml

# Cohere
path:*.env "COHERE_API_KEY"

# Ollama remote configs
path:*.yaml "ollama" "api_key" OR "OLLAMA_HOST"
path:*.env "OLLAMA_HOST" "0.0.0.0"
```

---

## 🆕 Vulnerable MCP Server Implementations (v1.2.0)

```
# MCP TypeScript SDK vulnerable pattern (CVE-2026-25536)
"McpServer" "StreamableHTTPServerTransport" language:typescript

# MCP STDIO with arbitrary commands
"mcp" "stdio" "command" "npx" language:json
"mcp" "stdio" "command" "python" language:json

# Flowise MCP adapter (CVE-2026-40933)
"flowise" "mcp" "adapter" language:typescript

# Agent Zero MCP (CVE-2026-30624)
"agent-zero" "mcp_servers" language:json

# nginx-ui MCP endpoint (CVE-2026-33032 — actively exploited)
"nginx-ui" "mcp" "mcp_message" language:go
```

---

## 🆕 ChatGPT Credential Harvesting Patterns (v1.2.0)

> IBM X-Force 2026: 300,000+ ChatGPT credentials found on dark web.

```
# ChatGPT session tokens
"chatgpt" "session" "token" path:*.json
"openai" "access_token" path:*.env

# Codex CLI tokens
"codex" "GITHUB_TOKEN" path:*.env
"codex" "installation" "access_token"
```
## Training Data
```
path:train.jsonl "prompt" "completion"
path:dataset.jsonl "instruction" "output"
path:fine_tune.jsonl
```
