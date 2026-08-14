# decisions/ — the construction record contract

A record library whose records are **construction-level decisions**: calls the
construction session made and the evidence behind them. One file per decision, dated
(`YYYY-MM-DD-slug.md`).

## What belongs here — and what does not

| This folder | Not this folder |
|---|---|
| Decisions the construction session made under delegated authority | The operator's rulings → `foundations/rulings.md` (append-only, outranks anything here) |
| Triage of external material: what is absorbed, replaced, disregarded, and why | Open questions with a test that would settle them → `experiments/` |
| Evaluations of one thing against the method, where the thing has no folder of its own | Evaluations of a stage or artifact → beside it (e.g. `motions/tam/01-mapping/EVALUATION-*.md`) |

## Reads / does / writes

- **Reads:** whatever the decision is about, plus `foundations/` — a decision that
  contradicts a ruling is not a decision, it is a finding.
- **Does:** records the call *and its evidence*, so a later session can re-open it on new
  evidence rather than re-deriving it from scratch.
- **Writes:** one dated file per decision. Records are revised only to record a reversal,
  and a reversal says what changed.

## The rule that makes a record worth keeping

**State what would reverse it.** A decision recorded without its evidence is an opinion
with a date; a decision recorded with its evidence can be checked when the evidence
moves. External material especially — a pack that lacks something today may ship it next
quarter.
