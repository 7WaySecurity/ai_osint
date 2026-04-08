# Contributing

PRs welcome! Guidelines:

## Adding Dorks/Queries
- **Verify it works** before submitting
- Include status indicator: 🟢 Active / 🟡 Degraded / 🔴 Dead
- Place in the correct file under `dorks/`
- Use modern GitHub Code Search syntax (`path:` not `filename:`)

## Adding Tools
- Must be **AI/ML-specific** — no generic OSINT tools
- Verify the repo exists and is actively maintained
- Include: name, description, maintainer, link

## Threat Intelligence
- Include dates, sources, and verifiable references
- Map to MITRE ATT&CK where applicable

## Detection Rules
- Follow Sigma format
- Include `falsepositives` section

## Process
1. Fork → 2. Branch → 3. Commit → 4. PR with description

## Rules
- No active credentials, real API keys, or PII
- Authorized testing and legitimate research only
- Responsible disclosure

Contact: septimus@7waysecurity.co
