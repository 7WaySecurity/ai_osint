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

## Training Data
```
path:train.jsonl "prompt" "completion"
path:dataset.jsonl "instruction" "output"
path:fine_tune.jsonl
```
