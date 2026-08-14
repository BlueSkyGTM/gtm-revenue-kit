# The 2026-08-13 framework retirement

Never load anything in this folder. It is the record of a governance layer that was
retired whole, on the operator's decision, during the reconstruction.

## Why it was retired

This layer — a six-file rule shelf, a lineage system with a conflict register, a product
shell, a 338-line shelf selector — was built to referee two bodies of knowledge whose
reasoning the builder did not hold. Its parallel-doctrine museum (C1–C4) formalized
not-knowing: conflicts were curated because nobody in the loop could decide them. The
operator can decide them, and the ones that need data are now **tests**, not doctrine.

## Where the living parts went

| Retired file | What survived, and where |
|---|---|
| `isolation.md` | the swap test, values-in-account, one-home, per-account suppression → `foundations/principles.md` §2–5 |
| `standards.md` | §PVP → `foundations/pvp.md`. Gates/benchmarks: numbers of unknown provenance — retired; accounts set their own (principle 3) |
| `lineages.md` | conflicts C1/C4 → `experiments/001`, `002`. The tag taxonomy → a one-line provenance header per file |
| `loading.md` | → `foundations/principles.md` §Load discipline |
| `deployments.md` | the travel rule → principle 6; the map → `estate.md` |
| `tiers.md` | retired without successor — the kit is internal machinery; there are no kit SKUs. **Named reversal condition (08-13):** if the kit ever ships inside a SKU to buyers, tiers-as-views (never forks) comes back from this shelf |
| `DIVERGENCE.md` | provenance summary → `NOTICE.md`; the change record → git history (`baseline-gtm-starter-kit` tag) |
| `START-HERE.md` | retired without successor — there is no buyer front door |
| `REFERENCES.md` | selection → the router (`CONTEXT.md`) |
| `CONTEXT.md`, `playbooks-CONTEXT.md` | folder contracts of the retired shape |

History is provenance, not a location (principle 6): cite these files as record, never as
rules.
