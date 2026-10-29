# Internal detection annex — what to do with what you found

This repository measures the **external** footprint. Once you have it, the internal side closes the loop. This annex only links public, maintained detections; it does not duplicate them.

| Need | Public resource | Notes |
|---|---|---|
| Endpoint DNS queries to LLM/local-model providers (Sysmon EID 22) | Splunk Security Content — *Local LLM Framework DNS Query* (`research.splunk.com/endpoint/d7ceffc5-a45e-412b-b9fa-2ba27c284503/`) | Most complete public rule found: huggingface, ollama, lmstudio, openai, anthropic, openrouter, dashscope, modelscope, gpt4all, jan.ai, replicate; excludes browsers |
| Copilot Studio agents published without authentication | Microsoft Security Blog, *Copilot Studio agent security: top 10 risks* (12 Feb 2026) — Advanced Hunting query **"AI Agents – No Authentication Required"** | Authoritative in-tenant detection; replaces any external dork |
| Cloud LLM API abuse (Bedrock, Anthropic, Ollama, MCP) | Elastic `detection-rules` and Splunk `security_content` repos | Dozens of rules; search each repo for `bedrock`, `ollama`, `mcp` |
| Community Sigma for unapproved LLM API use via proxy | `github.com/Shubhmane9503/sigma-ai-abuse-detections` | **Community / unvetted** — review before deploying |
| Existing rules in this repo | `../detection-rules/SIGMA_RULES.md` (rules 1–16) | MCP config access, agent-skill abuse, OpenClaw |

What to do internally after an external assessment:

1. For every S1 host found on your ASN: who owns it, change ticket or not, patch state (Ni8mare, CVE-2025-3248, CVE-2025-64496, CVE-2025-26319).
2. For every S3 config found: rotate any key present, inventory the MCP servers named, and confirm the internal hosts referenced are not reachable from the internet.
3. For every S4 share found: request takedown from the provider's privacy channel and from the third-party site; classify the pasted content.
4. For every S5 app found: identify the author, verify RLS/auth on the backend **through the author**, not by probing.
