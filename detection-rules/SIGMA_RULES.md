# Sigma Detection Rules for AI Infrastructure

---

## 1. Exposed Ollama Instance

```yaml
title: External Access to Ollama LLM Server
id: a1b2c3d4-e5f6-4a5b-9c0d-1e2f3a4b5c6d
status: experimental
description: Detects inbound connections to Ollama default port from non-RFC1918 sources
author: 7WaySecurity
date: 2026/04/07
references:
  - https://blogs.cisco.com/security/detecting-exposed-llm-servers-shodan-case-study-on-ollama
tags:
  - attack.initial_access
  - attack.t1190
logsource:
  category: firewall
detection:
  selection:
    dst_port: 11434
    direction: inbound
  filter_internal:
    src_ip|cidr:
      - '10.0.0.0/8'
      - '172.16.0.0/12'
      - '192.168.0.0/16'
      - '127.0.0.0/8'
  condition: selection and not filter_internal
level: high
falsepositives:
  - Legitimate remote access via VPN or authenticated proxy
```

## 2. AI API Key in Logs

```yaml
title: AI Provider API Key Detected in Logs
id: b2c3d4e5-f6a7-4b5c-0d1e-2f3a4b5c6d7e
status: experimental
description: Detects AI API key prefixes appearing in application log output
author: 7WaySecurity
date: 2026/04/07
tags:
  - attack.credential_access
  - attack.t1552.001
logsource:
  category: application
detection:
  sel_openai:
    message|contains: 'sk-proj-'
  sel_anthropic:
    message|contains: 'sk-ant-api03-'
  sel_hf:
    message|contains: 'hf_'
  sel_groq:
    message|contains: 'gsk_'
  sel_replicate:
    message|contains: 'r8_'
  sel_google:
    message|re: 'AIzaSy[A-Za-z0-9_-]{33}'
  condition: 1 of sel_*
level: critical
falsepositives:
  - Debug logging in dev environments
```

## 3. Unauthorized LLM API Access

```yaml
title: Unauthenticated LLM API Request
id: c3d4e5f6-a7b8-4c5d-1e2f-3a4b5c6d7e8f
status: experimental
description: Detects API calls to LLM endpoints without Bearer token
author: 7WaySecurity
date: 2026/04/07
tags:
  - attack.initial_access
  - attack.t1190
logsource:
  category: webserver
detection:
  sel_endpoints:
    cs-uri-stem|contains:
      - '/api/generate'
      - '/api/chat'
      - '/v1/chat/completions'
      - '/v1/completions'
      - '/api/tags'
      - '/v1/models'
  sel_ports:
    dst_port:
      - 11434
      - 8000
      - 8080
      - 1234
      - 4891
  filter_auth:
    cs-Authorization|contains: 'Bearer'
  condition: sel_endpoints and sel_ports and not filter_auth
level: high
falsepositives:
  - Internal dev environments without auth
```

## 4. MCP Server Without Auth

```yaml
title: Exposed MCP Server — No Authentication
id: d4e5f6a7-b8c9-4d5e-2f3a-4b5c6d7e8f9a
status: experimental
description: Detects externally accessible MCP endpoints responding without auth
author: 7WaySecurity
date: 2026/04/07
references:
  - https://vulnerablemcp.info/
tags:
  - attack.initial_access
  - attack.t1190
logsource:
  category: webserver
detection:
  selection:
    cs-uri-stem|contains:
      - '/api/v1/status'
      - '/api/v1/health'
      - '/sse'
    dst_port:
      - 18789
      - 3000
  sel_ok:
    sc-status: 200
  condition: selection and sel_ok
level: critical
falsepositives:
  - Public health check endpoints by design
```

## 5. Vector DB Unauthorized Access

```yaml
title: Vector Database Enumeration Without Auth
id: e5f6a7b8-c9d0-4e5f-3a4b-5c6d7e8f9a0b
status: experimental
description: Detects external access to vector database collection listing endpoints
author: 7WaySecurity
date: 2026/04/07
tags:
  - attack.collection
  - attack.t1530
logsource:
  category: webserver
detection:
  sel_qdrant:
    dst_port: 6333
    cs-uri-stem|contains: '/collections'
  sel_weaviate:
    dst_port: 8080
    cs-uri-stem|contains: '/v1/schema'
  sel_chroma:
    dst_port: 8000
    cs-uri-stem|contains: '/api/v2/collections'
  condition: 1 of sel_*
level: high
falsepositives:
  - Authorized internal access
```

## 6. LLMjacking — Anomalous Inference

```yaml
title: Potential LLMjacking — Inference Spike
id: f6a7b8c9-d0e1-4f5a-4b5c-6d7e8f9a0b1c
status: experimental
description: Detects unusual spikes in LLM API requests indicating unauthorized use
author: 7WaySecurity
date: 2026/04/07
references:
  - https://www.pillar.security/
tags:
  - attack.impact
  - attack.t1496
logsource:
  category: application
detection:
  selection:
    endpoint|contains:
      - '/v1/chat/completions'
      - '/api/generate'
      - '/api/chat'
  timeframe: 1h
  condition: selection | count() > 500
level: high
falsepositives:
  - Batch processing workloads
  - Load testing
```

## 7. AI Agent RCE via Prompt Injection

```yaml
title: Suspicious Tool Execution in AI Agent
id: a7b8c9d0-e1f2-4a5b-5c6d-7e8f9a0b1c2d
status: experimental
description: Detects tool calls to shell/filesystem that may indicate prompt injection
author: 7WaySecurity
date: 2026/04/07
tags:
  - attack.execution
  - attack.t1059
logsource:
  category: application
detection:
  sel_tools:
    tool_name|contains:
      - 'bash'
      - 'shell'
      - 'python_repl'
      - 'fs_read'
      - 'fs_write'
      - 'execute'
  sel_sus:
    tool_input|contains:
      - '/etc/passwd'
      - '.env'
      - 'reverse shell'
      - 'nc -e'
      - 'bash -i'
      - 'curl | sh'
      - 'base64 -d'
      - 'subprocess'
      - 'eval('
      - 'exec('
  condition: sel_tools and sel_sus
level: critical
falsepositives:
  - Legitimate sysadmin via AI agents
```
---

## 🆕 v1.2.0 Detection Rules (April 2026)

---

### Rule 8: MCP STDIO Arbitrary Command Execution

> Detects the systemic MCP STDIO command injection vulnerability discovered by Ox Security affecting 150M+ downloads.

```yaml
title: MCP STDIO Arbitrary Command Execution
id: 8a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d
status: experimental
description: >
  Detects potential MCP STDIO command injection via crafted server configuration.
  MCP's STDIO transport allows spawning subprocesses with arbitrary OS commands.
  Attackers exploit this to achieve RCE through MCP adapter UIs or via prompt
  injection in AI IDEs.
references:
  - https://www.ox.security/blog/the-mother-of-all-ai-supply-chains-critical-systemic-vulnerability-at-the-core-of-the-mcp/
  - https://www.ox.security/blog/mcp-supply-chain-advisory-rce-vulnerabilities-across-the-ai-ecosystem
  - CVE-2026-30615
  - CVE-2026-30624
  - CVE-2026-30616
  - CVE-2026-40933
author: 7WaySecurity
date: 2026/04/20
tags:
  - attack.execution
  - attack.t1059
  - attack.t1059.004
  - attack.supply_chain
logsource:
  category: process_creation
  product: windows
detection:
  selection_parent:
    ParentImage|endswith:
      - '\node.exe'
      - '\npx.cmd'
      - '\npx.exe'
      - '\python.exe'
      - '\python3.exe'
  selection_mcp_context:
    CommandLine|contains:
      - 'stdio'
      - 'mcp'
      - 'mcpServers'
  selection_suspicious_cmd:
    CommandLine|contains:
      - 'curl '
      - 'wget '
      - 'powershell'
      - 'cmd /c'
      - 'cmd.exe /c'
      - '/bin/sh'
      - '/bin/bash'
      - 'bash -c'
      - 'npx -c'
      - 'python -c'
      - 'node -e'
  condition: selection_parent AND (selection_mcp_context OR selection_suspicious_cmd)
falsepositives:
  - Legitimate MCP server installations via npx
  - Development environments with MCP testing
level: high
```

---

### Rule 9: VS Code Copilot YOLO Mode Activation (CVE-2025-53773)

> Detects modification of VS Code settings to enable autoApprove — disables all user confirmations for Copilot, enabling arbitrary command execution via prompt injection.

```yaml
title: VS Code Copilot YOLO Mode Activation
id: 9b2c3d4e-5f6a-7b8c-9d0e-1f2a3b4c5d6e
status: experimental
description: >
  Detects modification of VS Code settings.json to enable chat.tools.autoApprove
  (YOLO mode). CVE-2025-53773 exploits this via prompt injection to achieve
  wormable RCE across developer workstations.
references:
  - https://nvd.nist.gov/vuln/detail/CVE-2025-53773
  - https://embracethered.com/blog/posts/2025/github-copilot-remote-code-execution-via-prompt-injection/
  - https://www.persistent-security.net/post/part-iii-vscode-copilot-wormable-command-execution-via-prompt-injection
author: 7WaySecurity
date: 2026/04/20
tags:
  - attack.defense_evasion
  - attack.t1562.001
  - attack.execution
  - attack.t1059
logsource:
  category: file_change
  product: windows
detection:
  selection_file:
    TargetFilename|endswith: '\settings.json'
    TargetFilename|contains:
      - '.vscode'
      - 'Code\User'
  selection_content:
    - 'chat.tools.autoApprove'
    - 'autoApprove'
  condition: selection_file AND selection_content
falsepositives:
  - Developer intentionally enabling auto-approve for trusted workspaces
level: high
```

---

### Rule 10: nginx-ui MCP Endpoint Exploitation (CVE-2026-33032)

> Detects unauthenticated access to nginx-ui MCP endpoints. Actively exploited in the wild (CVSS 9.8).

```yaml
title: nginx-ui MCP Endpoint Unauthenticated Access (MCPwn)
id: 0c3d4e5f-6a7b-8c9d-0e1f-2a3b4c5d6e7f
status: experimental
description: >
  Detects exploitation of nginx-ui MCP endpoints (/mcp, /mcp_message) without
  authentication. CVE-2026-33032 allows full Nginx takeover in 2 HTTP requests.
  Listed among 31 actively exploited vulnerabilities in March 2026.
references:
  - https://thehackernews.com/2026/04/critical-nginx-ui-vulnerability-cve.html
  - CVE-2026-33032
  - CVE-2026-27944
author: 7WaySecurity
date: 2026/04/20
tags:
  - attack.initial_access
  - attack.t1190
  - attack.privilege_escalation
  - attack.t1068
logsource:
  category: webserver
  product: nginx
detection:
  selection_uri:
    cs-uri-stem|contains:
      - '/mcp'
      - '/mcp_message'
  filter_authenticated:
    cs-Authorization|exists: true
  condition: selection_uri AND NOT filter_authenticated
falsepositives:
  - Legitimate MCP client connections with alternative auth methods
level: critical
```

---

### Rule 11: DNS-Based Data Exfiltration from AI Sandbox

> Detects unusually long DNS queries matching the ChatGPT DNS exfiltration pattern discovered by Check Point.

```yaml
title: DNS-Based Data Exfiltration from AI Code Execution Environment
id: 1d4e5f6a-7b8c-9d0e-1f2a-3b4c5d6e7f8a
status: experimental
description: >
  Detects unusually long DNS queries that may indicate data exfiltration via DNS
  side channel from AI code execution sandboxes. ChatGPT vulnerability (patched
  Feb 20, 2026) used DNS resolution to encode and transmit sensitive user data.
references:
  - https://blog.checkpoint.com/research/when-ai-trust-breaks-the-chatgpt-data-leakage-flaw-that-redefined-ai-vendor-security-trust/
  - https://thehackernews.com/2026/03/openai-patches-chatgpt-data.html
author: 7WaySecurity
date: 2026/04/20
tags:
  - attack.exfiltration
  - attack.t1048.003
  - attack.t1071.004
logsource:
  category: dns_query
detection:
  selection_long_query:
    query|re: '.{100,}'
  selection_encoded_subdomains:
    query|re: '[a-z0-9]{30,}\.[a-z0-9]{30,}\.'
  selection_source_ai_sandbox:
    src_ip|cidr:
      - '10.0.0.0/8'
      - '172.16.0.0/12'
      - '192.168.0.0/16'
  condition: (selection_long_query OR selection_encoded_subdomains) AND selection_source_ai_sandbox
falsepositives:
  - CDN queries with long domain names
  - Analytics with encoded identifiers
level: medium
```

---

### Rule 12: Claude Code 50+ Subcommand Pipeline Bypass

> Detects command pipelines exceeding 50 subcommands, which bypass Claude Code's deny rules.

```yaml
title: Claude Code 50+ Subcommand Pipeline Deny Rule Bypass
id: 2e5f6a7b-8c9d-0e1f-2a3b-4c5d6e7f8a9b
status: experimental
description: >
  Detects command pipelines with unusually high subcommand counts that may exploit
  the Claude Code vulnerability where deny rules are bypassed when a pipeline
  exceeds 50 subcommands. Found after the March 31, 2026 source map leak.
references:
  - https://www.securityweek.com/critical-vulnerability-in-claude-code-emerges-days-after-source-leak/
  - https://www.zscaler.com/blogs/security-research/anthropic-claude-code-leak
author: 7WaySecurity
date: 2026/04/20
tags:
  - attack.defense_evasion
  - attack.t1562.001
  - attack.execution
  - attack.t1059
logsource:
  category: process_creation
  product: windows
detection:
  selection_claude:
    ParentImage|endswith:
      - '\claude.exe'
      - '\node.exe'
    ParentCommandLine|contains: 'claude'
  selection_long_pipeline:
    CommandLine|re: '(&&|;|\|){49,}'
  condition: selection_claude AND selection_long_pipeline
falsepositives:
  - Legitimate build scripts with many sequential steps
level: high
```
