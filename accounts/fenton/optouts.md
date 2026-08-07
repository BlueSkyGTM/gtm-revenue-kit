# Opt-outs — permanent suppression list

**Append-only. Never edit or delete a row.** An opt-out is honored forever, across every future
campaign, including ones that do not exist yet. This is the one suppression record with
statutory weight.

**Open this before every send batch.** It is written for a human reading it under time pressure,
not for an agent parsing it. If it ever gets long enough that scanning it is impractical, that is
the signal to move it — not to stop checking it.

## How to use it

1. **Before a send:** suppress every address in this file, and every address at a domain listed
   here where the request covered the company rather than the person.
2. **On a reply asking to be removed:** append a row the same day. The `optout-reply` trigger in
   `../CONTEXT.md` offers to do this; it still needs a yes.
3. **Never remove a row**, even if the person later re-engages. If they opt back in, that is a
   new consent recorded elsewhere, not a deletion here.

## What does NOT belong here

| Not this | Where it lives | Why |
|---|---|---|
| Bounces, dead domains | the send tool's bounce state; Airtable `Campaign_Role = dropped` | Both sit closer to the send. A third copy in git would be the stalest of the three. |
| Existing clients | derived from `../../clients/clients/*/` at send time | The roster is already the source; copying it would drift. |
| "Not interested" replies | the campaign's `results.md` | A soft no is a campaign outcome, not a legal suppression. |

## The ledger

| Email | Domain | Date | Campaign | How |
|---|---|---|---|---|
| | | | | |

**Columns.** `Email` — the address that asked, lowercase. `Domain` — fill when the request covers
everyone at the company, blank when it covers only the person. `Date` — YYYY-MM-DD, the day the
request arrived, not the day it was logged. `Campaign` — the campaign slug that prompted it.
`How` — reply / unsubscribe link / phone / forwarded, in a few words.

*Empty because nothing has been sent yet. The first campaign will change that.*
