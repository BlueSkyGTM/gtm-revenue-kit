# Estate — what this kit is, owns, and reads

The context map, seeded small. Subject: where this machinery sits in the operator's
estate, what it owns, and what it deliberately does not. Grows only when a sibling
machine becomes real.

## What this kit is

Connective machinery for **revenue engineering**. GTM motions are not the heart of a
business OS — they are the tissue that prevents waste between what a business offers and
who needs it: signal → offer → conversation → won work, with nothing leaking between.
The kit owns the motions; the things the motions connect live in their own machines.

## Owns / reads

| | What | Home |
|---|---|---|
| **Owns** | motion method (skills, plays, channels, workflows, the TAM pipeline) | `motions/` |
| **Owns** | the signal record schema and admitted signal records | `signals/` |
| **Owns** | the experiment protocol and open tests | `experiments/` |
| **Owns** | the account stamp and the rules (`foundations/`) | `accounts/_template/` |
| **Reads (future siblings)** | offers / SKUs — what is actually sold | not built; squats today in `accounts/<slug>/brand/offer-map` |
| **Reads (future siblings)** | funnel machinery — where conversations convert | not built (ClickFunnels connector exists, unwired) |
| **Reads (future siblings)** | brand voice + copywriting system | not built; squats today in `accounts/<slug>/brand/` + `tools/lint_copy.py` |

**The squatting is declared, not resolved:** brand voice, the offer map, and the copy
linter live in this kit today because nowhere better exists. When the sibling machines
are built, those move out and the kit reads them — an estate-level application of
one-home-per-fact. Until then they stay, and nothing new of that kind is added here.

## Deployments — which copy holds what

Core is copied identically into every deployment; an account lives in exactly one
(principle 6). This table is the map; `accounts/_index.md` is the per-account catalog.

| Copy | Core | Accounts | State |
|---|---|---|---|
| `gtm-kit-pro` (this repo, upstream) | **authoritative** | `_template/` only | under reconstruction (this branch) |
| `fenton-bookkeeping-os/machinery/gtm-kit/` | vendored | `fenton` | **shelved 2026-08-13** — re-vendors core on resume |
| `albatross-engineering-os/machinery/gtm-kit/` | vendored | `revenue-engineering` | active front |

**Plan of record:** albatross runs GTM as a service; fenton becomes its first client
account — the dry run of the service model with a client that cannot be burned. When that
happens, the account moves and this table plus `accounts/_index.md` record it; nothing
else in core changes (that portability is what principle 6 buys).

## The second brain

A Claude Cowork workspace, pointed at this repo, is the operation's second brain: it
holds the operator's improved TAM framework and the revenue-engineering definition in
progress. It evaluates what is built here; the operator briefs the changes in. Its
content reaches this repo through commits — anything not committed here does not exist
here (principle 6's history rule applies to it too).
