# Loading — what to read, and what never to read together

Nothing in this repo loads automatically except `CLAUDE.md`. Every skill names its inputs;
read exactly those.

## The account gate

Before any file loads: **the account is named.** Loading `context/` without knowing whose
context it is produces confident answers from the wrong buyer's facts — the most expensive
failure mode this repo has, because nothing about the output looks wrong.

## Factory and product

| | What it is | How to read it |
|---|---|---|
| `accounts/<slug>/context/` | the **factory** — configured once, read every run | one named file at a time |
| `accounts/<slug>/outputs/` | the **product** — new every run | only the specific dated file the task names |

**Never bulk-load either.** An account with a year of operating history has hundreds of
outputs; reading them all to answer one question fills the session with detail it cannot
act on and crowds out the file that actually held the answer.

## Never co-load

Two rule systems that produce nonsense when both are in the room:

| Rule system | Governs | Lives in | Never load while doing |
|---|---|---|---|
| Copy discipline | outbound copy, sequences, positioning | the account's `positioning.md`, `brand/voice.md` | scoring or list mechanics |
| Scoring discipline | tiers, weights, thresholds, decay | the account's `scoring-model.md`, `signal-library.md` | writing copy |

The failure is subtle in both directions: copy rules loaded during a scoring pass make the
model argue for what sounds good, and scoring values loaded during a copy pass produce
emails that read like a rubric. Do one, then the other.

**Delivery rules from a host system never load here at all.** If an account's operator also
runs a delivery system with its own approval gates (a ledger, a filing queue, a production
pipeline), those rules govern that system, not this one. A GTM session that loads a write
gate starts asking permission to send an email; a delivery session that loads copy rules
starts editing records for tone.

## Tracks

An account running two buyers keeps them in `context/tracks/<track>/`. **Load one track per
session.** The whole point of a track is that its ICP, positioning, radar, and messaging
disagree with the other track's — that is why they are separate. Loaded together they
average into copy that fits neither buyer.

## What never enters the repo

- Contact data, send lists, enrichment exports — gitignored by pattern, and the pattern is
  not the only defense: do not paste them into a file either
- API keys, tokens, credentials — environment only, never a committed file
- Raw meeting transcripts — synthesize into the relevant context file, then discard
- Another account's facts (see `docs/isolation.md`)
