# GitHub Dorks for AI/ML Secret Discovery

> 🔑 **`KEYWORD` convention (v1.3.0):** these queries are for auditing code you
> own or are authorized to assess. Scope every search with an org/owner/repo
> qualifier **and/or** a `"KEYWORD"` term:
>
> ```
> org:YOUR_ORG   user:YOUR_USERNAME   repo:owner/name
> ```
>
> Key prefixes (`sk-proj-`, `sk-ant-api03-`) and env-var names are **detection
> fingerprints** and stay — they describe the format, not a specific victim's
> secret. Scoping turns a credential dragnet into a legitimate self-audit.
>
> ⚠️ **Syntax (verified Jun 2026):** GitHub web Code Search uses `path:`. Legacy
> `filename:`/`extension:` survive only via REST API v3. `in:file` is implied.
>
> 📊 **Scale:** GitGuardian 2026 found AI credential leaks surged **81% YoY** to
> 1,275,105 leaked AI secrets. Claude Code commits leaked at **3.2%** — double
> the human baseline.

---

## OpenAI Keys
```
"sk-proj-" path:*.env "KEYWORD"
"sk-proj-" path:*.py "KEYWORD"
"OPENAI_API_KEY" path:*.env NOT "your_key" NOT "example" NOT "placeholder" "KEYWORD"
"openai.api_key" path:*.py "KEYWORD"
```

## Anthropic Keys
> Anthropic became a GitHub secret scanning partner Aug 20, 2024. New commits trigger push protection, but **historical commits remain searchable**. OAuth tokens use `sk-ant-oat01-` prefix.
```
"sk-ant-api03" path:*.env "KEYWORD"
"sk-ant-oat01" path:*.env "KEYWORD"
"ANTHROPIC_API_KEY" path:*.env NOT "your_key" "KEYWORD"
"CLAUDE_API_KEY" path:*.env "KEYWORD"
"anthropic" "api_key" path:*.yaml "KEYWORD"
"anthropic" "api_key" path:*.json "KEYWORD"
```

## Claude Code Configs
> Claude Code uses ~/.claude/ for configs. May contain API keys and project hooks.
```
path:.claude/settings.json "KEYWORD"
path:.claude.json "api_key" "KEYWORD"
"ANTHROPIC_API_KEY" path:*.sh "claude" "KEYWORD"
"claude-code" path:docker-compose.yml "KEYWORD"
path:.claude/CLAUDE.md "KEYWORD"
```

## Google AI / Gemini
> ⚠️ `AIzaSy` prefix is shared across ALL Google Cloud APIs. A Maps key can silently access Gemini if the Generative Language API is enabled.
```
"AIzaSy" path:*.env "generativelanguage" "KEYWORD"
"AIzaSy" path:*.env "gemini" "KEYWORD"
"GOOGLE_API_KEY" path:*.env "gemini" "KEYWORD"
"GOOGLE_AI_API_KEY" path:*.env "KEYWORD"
```

## HuggingFace Tokens
```
"hf_" path:*.env "KEYWORD"
"HUGGINGFACE_TOKEN" path:*.env "KEYWORD"
"HF_TOKEN" path:*.env "KEYWORD"
```

## Replicate
```
"r8_" path:*.env "KEYWORD"
"REPLICATE_API_TOKEN" path:*.env "KEYWORD"
```

## Cohere / Mistral / Groq / Together / DeepSeek
```
"COHERE_API_KEY" path:*.env "KEYWORD"
"MISTRAL_API_KEY" path:*.env "KEYWORD"
"gsk_" path:*.env "KEYWORD"
"GROQ_API_KEY" path:*.env "KEYWORD"
"TOGETHER_API_KEY" path:*.env "KEYWORD"
"DEEPSEEK_API_KEY" path:*.env "KEYWORD"
```

## ElevenLabs / Stability / OpenRouter
```
"ELEVENLABS_API_KEY" path:*.env "KEYWORD"
"xi-api-key" path:*.py "KEYWORD"
"STABILITY_API_KEY" path:*.env "KEYWORD"
"OPENROUTER_API_KEY" path:*.env "KEYWORD"
```

## Vector Databases
```
"PINECONE_API_KEY" path:*.env "KEYWORD"
"QDRANT_API_KEY" path:*.env "KEYWORD"
"WEAVIATE_API_KEY" path:*.env "KEYWORD"
```

## MLOps
```
"WANDB_API_KEY" path:*.env "KEYWORD"
"MLFLOW_TRACKING_URI" path:*.env "KEYWORD"
"NEPTUNE_API_TOKEN" path:*.env "KEYWORD"
"COMET_API_KEY" path:*.env "KEYWORD"
```

---

## MCP & AI Agent Config Leaks
> 📊 24,008 unique secrets exposed in MCP configs in its first year (GitGuardian 2026).
```
path:mcp.json "api_key" "KEYWORD"
path:mcp.json "token" "KEYWORD"
path:openclaw.json "api_key" "KEYWORD"
path:.cursor/mcp.json "KEYWORD"
"mcpServers" path:*.json "apiKey" "KEYWORD"
"mcpServers" path:*.json "OPENAI_API_KEY" "KEYWORD"
```

## System Prompts
```
"system_prompt" path:*.py "you are" "KEYWORD"
"SYSTEM_PROMPT" path:*.env "KEYWORD"
"system_message" path:*.py "you are a" "KEYWORD"
path:prompts.yaml "system" "KEYWORD"
path:prompts.json "system" "KEYWORD"
```

## AI Infrastructure Configs
```
path:docker-compose.yml "ollama" "KEYWORD"
path:docker-compose.yml "chromadb" "KEYWORD"
path:docker-compose.yml "qdrant" "KEYWORD"
path:docker-compose.yml "weaviate" "KEYWORD"
path:docker-compose.yml "milvus" "KEYWORD"
path:docker-compose.yml "vllm" "KEYWORD"
```

---

## 🆕 MCP Configuration Leaks (v1.2.0)
> Systemic RCE in MCP STDIO transport affects every SDK language. 10+ High/Critical CVEs issued (Ox Security, April 2026).
```
path:*.json "mcpServers" "command" "args" "KEYWORD"
path:.cursor/mcp.json "apiKey" "KEYWORD"
path:mcp.json "stdio" "env" "KEYWORD"
path:*.json "mcp_servers" "OPENAI_API_KEY" "KEYWORD"

# Windsurf IDE (CVE-2026-30615)
path:*.json "windsurf" "mcpServers" "KEYWORD"
```

---

## 🆕 Claude Code & Anthropic Token Patterns (v1.2.0)
> Claude Code source map leaked March 31, 2026. New token prefix `sk-ant-oat01-` for OAuth.
```
"sk-ant-api03-" NOT "example" NOT "test" NOT "xxx" "KEYWORD"
"sk-ant-oat01-" NOT "example" "KEYWORD"
"@anthropic-ai/claude-code" "source" "map"

# CLAUDE.md permission files (attack vector for 50-subcommand bypass)
"CLAUDE.md" "permission" "allow" "KEYWORD"
path:CLAUDE.md "bash" "allow" "KEYWORD"
```

---

## 🆕 AI IDE YOLO Mode / Config Exploitation (v1.2.0)
> CVE-2025-53773: Copilot modifies `.vscode/settings.json` to enable autoApprove via prompt injection.
```
path:.vscode/settings.json "chat.tools.autoApprove" "true" "KEYWORD"
path:.vscode/settings.json "github.copilot" "autoApprove" "KEYWORD"
path:.vscode/tasks.json "mcp" "command" "KEYWORD"
```

---

## 🆕 AI Agent Secrets (v1.2.0)
```
"DEEPSEEK_API_KEY" NOT "your_key" NOT "example" "KEYWORD"
"gsk_" path:*.py NOT "example" "KEYWORD"
"MISTRAL_API_KEY" path:*.yaml "KEYWORD"
"COHERE_API_KEY" path:*.env "KEYWORD"

# Ollama remote configs
path:*.yaml "ollama" "OLLAMA_HOST" "KEYWORD"
path:*.env "OLLAMA_HOST" "0.0.0.0" "KEYWORD"
```

---

## 🆕 Vulnerable MCP Server Implementations (v1.2.0)
> These are code-pattern fingerprints for vulnerable implementations. Scope with `org:`/`KEYWORD` to your own codebases.
```
# MCP TypeScript SDK vulnerable pattern (CVE-2026-25536)
"McpServer" "StreamableHTTPServerTransport" language:typescript "KEYWORD"

# MCP STDIO with arbitrary commands
"mcp" "stdio" "command" "npx" language:json "KEYWORD"
"mcp" "stdio" "command" "python" language:json "KEYWORD"

# Flowise MCP adapter (CVE-2026-40933)
"flowise" "mcp" "adapter" language:typescript "KEYWORD"

# Agent Zero MCP (CVE-2026-30624)
"agent-zero" "mcp_servers" language:json "KEYWORD"

# nginx-ui MCP endpoint (CVE-2026-33032 — actively exploited)
"nginx-ui" "mcp" "mcp_message" language:go "KEYWORD"
```

---

## 🆕 ChatGPT Credential Patterns (v1.2.0)
> IBM X-Force 2026: 300,000+ ChatGPT credentials found on dark web. Audit your own org for accidental commits.
```
"chatgpt" "session" "token" path:*.json "KEYWORD"
"openai" "access_token" path:*.env "KEYWORD"
"codex" "GITHUB_TOKEN" path:*.env "KEYWORD"
"codex" "installation" "access_token" "KEYWORD"
```

## Training Data
```
path:train.jsonl "prompt" "completion" "KEYWORD"
path:dataset.jsonl "instruction" "output" "KEYWORD"
path:fine_tune.jsonl "KEYWORD"
```

---

## Defender Tip
GitHub **Secret Scanning** + **Push Protection** (free for public repos) catch most provider key formats before commit. Enable both org-wide; these dorks find what predates that or lives in forks/gists outside push protection.

---

## 🆕 Agent Skill & MCP Exposure (v1.4.0)

> 🔑 `KEYWORD` convention applies. Scope with `org:`/`user:`/`repo:` to your own
> code. These audit agent-capability files and MCP configs for exposure — the
> surface behind the OpenClaw / ClawHavoc crisis.

```
# Agent capability / skill manifests in your repos
path:SKILL.md "KEYWORD"
path:AGENTS.md "mcp" "KEYWORD"
path:CLAUDE.md "allow" "bash" "KEYWORD"
path:.cursor/rules "KEYWORD"

# OpenClaw / Clawdbot configs with embedded secrets
path:.clawdbot "KEYWORD"
path:.clawdbot/.env "KEYWORD"
"openclaw" "skills" path:*.json "KEYWORD"

# MCP auto-approve / over-permissioning (the consent-gap risk)
path:*.json "enableAllProjectMcpServers" "true" "KEYWORD"
path:.vscode/settings.json "chat.tools.autoApprove" "true" "KEYWORD"
```

---

## 🆕 Skill-Injection Indicators (v1.4.0)

> Audit your own skill content for the patterns flagged by Snyk ToxicSkills /
> ATR. Scope with `org:`/`KEYWORD`.

```
# Encoded prerequisite commands (ClickFix 2.0 pattern)
path:SKILL.md "base64 -d" "KEYWORD"
path:SKILL.md "prerequisite" "curl" "KEYWORD"

# Read-and-exfiltrate compound in skill scripts
"id_rsa" "curl" path:SKILL.md "KEYWORD"
"wallet.dat" path:*.sh "KEYWORD"
```

> 📌 These find the *pattern* for self-audit. Do not use them to enumerate or
> redistribute third-party malicious skills.
