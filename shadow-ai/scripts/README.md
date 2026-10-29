# shadow_ai_footprint.py

Passive collector for the five Shadow AI external surfaces. It only queries third-party indexes (crt.sh, Cert Spotter, GitHub Code Search, Shodan count API). If one Certificate Transparency source is down, the other covers it. It never contacts a discovered host.

## Setup (macOS, Homebrew Python)

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install requests
gh auth login            # needed for S3 (GitHub Code Search requires a session)
export SHODAN_API_KEY=…  # optional, S1 — 1 query credit per product × scope
```

## Run

```bash
python3 shadow_ai_footprint.py \
  --domain example.com \
  --gh-org example-corp --gh-user jdoe --gh-user asmith \
  --asn AS12345 --orgname "Example Corp" \
  --shodan-key "$SHODAN_API_KEY" \
  --out shadow_ai_example_com.md
```

Without `--shodan-key` the script runs S2 + S3 only (free). Google queries for S4/S5 are printed at the end of the report for you to run by hand with your scope.

## Credit budget (Shodan `dev` plan)

5 products × up to 3 scopes = max **15 query credits** per organization. Use `--asn` and `--orgname` only when you have them; `ssl.cert.subject.cn` always runs.

## Output

A Markdown report with one section per surface, ready to paste into an assessment.
