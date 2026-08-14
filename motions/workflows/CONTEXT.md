# motions/workflows/ — the process-doc contract

How a team operates, end to end: human process docs, not execution instructions for
Claude (the skills execute; these describe). This file is the folder's contract: what
each doc is, where it came from, and what may load together.

## Files

| File | Provenance | What it is | Pairs with / competes with |
|---|---|---|---|
| `campaign-build.md` | upstream | The **signal-led** campaign process: a fired signal → audience → launch → measurement | Complements the TAM pipeline (different starting condition, not a conflict) |
| `enrichment.md` | upstream | The data waterfall: free sources → orchestrator → proprietary | Extended by `enrichment-techniques.md`; carries the sanctioned defaults |
| `enrichment-techniques.md` | Michael (`NOTICE.md`) | Technique patterns: action cost model, own-API-key, webhooks, four scraping patterns | Points at `enrichment.md` for defaults rather than restating |
| `signal-routing.md` | upstream | Signal fires → what happens next (the decision tree) | Routes into `motions/plays/` |
| `pain-based-segmentation.md` | Cannonball GTM / Doug Bell (`NOTICE.md`) | Segments defined by a shared Existential Data Point, not firmographics | One instrument of `experiments/002-segment-definition.md` |

The market-led campaign process lives at `motions/tam/` (its own pipeline, under
construction) — not in this folder.

## Loading

Load ONE campaign process per session — signal-led (`campaign-build.md`) or market-led
(`motions/tam/`), decided by the starting condition. The enrichment pair loads together
by design. `pain-based-segmentation.md` loads at segmentation time and replaces the
market-mapping step it competes with; the campaign brief states which map drew the
audience.

## Revision rule

An edit that would make one instrument agree with its competitor is a verdict, and
verdicts belong to `experiments/` — dated record first, then the edit. Additions within a
doc's own method are ordinary edits, provenance stated.
