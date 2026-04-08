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
