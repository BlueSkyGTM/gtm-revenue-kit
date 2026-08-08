# sync/ — result-pull contract

Scripts that pull live campaign results from an outbound tool or CRM into an account. Run
before `skills/weekly-update` so the context refresh works from fresh numbers instead of
manual entry.

- **Reads:** the operator's API credentials from the environment (never committed) and the
  named account's campaign identifiers.
- **Writes:** sync JSON **inside the named account** (`accounts/<slug>/outputs/campaigns/
  <campaign>/results-sync.json`, `accounts/<slug>/context/signal-performance-sync.json`) —
  gitignored by pattern; the durable summary is written into the campaign's `results.md`
  by the weekly-update pass, as an edit surface, not by these scripts.
- **Human check:** synced numbers feed the calibration log only after the operator has seen
  them in the weekly update — a script never edits `scoring-model.md`.
- **Status (`upstream` lineage):** restored from the original kit; not yet proven against a
  live tool (`README.md` → Room for Growth). Treat output paths as the contract; the
  script internals may need updating on first real use.

---

## Scripts

| Script | What it pulls | Configure |
|--------|--------------|-----------|
| `sync-campaign-results.py` | Reply rates, meeting rates, pipeline by campaign | Apollo / Outreach / Instantly API |
| `sync-signal-performance.py` | Signal performance by send volume | Outbound tool + CRM |

---

## Setup

```bash
cp .env.example .env
# Fill in your API keys — never commit .env to git
pip install -r sync/requirements.txt
```

Run manually:
```bash
python3 sync/sync-campaign-results.py
python3 sync/sync-signal-performance.py
```

Then run the weekly-update skill. Claude will read the freshly synced data automatically.

---

## Automating with OpenClaw

[OpenClaw](https://openclaw.ai) can trigger these scripts on a schedule, update the repo files, and message you on Slack when the update is ready for review. See the OpenClaw skill registry for a pre-built GTM repo skill.

---

## Output Format

Each script writes to a structured file that the weekly-update skill reads:

- `sync-campaign-results.py` → `outputs/campaigns/[campaign-name]/results-sync.json`
- `sync-signal-performance.py` → `context/signal-performance-sync.json`

These JSON files are gitignored by default (they contain live data). The weekly-update skill reads them and incorporates the numbers into its drafted updates.

### results-sync.json schema

```json
{
  "tool": "apollo | instantly | outreach",
  "campaign_id": "string",
  "campaign_name": "string",
  "synced_at": "ISO 8601 datetime",
  "sends": 0,
  "replies": 0,
  "meetings_booked": 0,
  "reply_rate": 0.0,
  "meeting_rate": 0.0
}
```

Note: `meetings_booked` and `meeting_rate` may be `null` for tools that don't track meetings natively (e.g., Instantly). The weekly-update skill handles nulls gracefully.

### signal-performance-sync.json schema

```json
{
  "synced_at": "ISO 8601 datetime",
  "signals": {
    "Signal Name": {
      "sends_90d": 0,
      "replies": 0,
      "meetings_booked": 0,
      "reply_rate": 0.0,
      "meeting_rate": 0.0,
      "source_campaigns": ["campaign-folder-name"]
    }
  }
}
```

### If a script fails

Common failure modes and fixes:

| Error | Likely cause | Fix |
|-------|-------------|-----|
| `API key not set` | Missing `.env` entry | Copy `.env.example` to `.env` and fill in keys |
| `No campaign found matching...` | Campaign name mismatch | Update `CAMPAIGN_TO_SIGNAL_MAP` in `sync-signal-performance.py` |
| `No results-sync.json files found` | `sync-campaign-results.py` hasn't run | Run campaign sync first, then signal sync |
| `HTTP 401 / 403` | API key invalid or expired | Regenerate key in your outbound tool |

If the weekly-update skill runs without fresh sync data, it will note which numbers are stale rather than use incorrect data.
