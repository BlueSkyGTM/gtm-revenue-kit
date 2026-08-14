# motions/tam/ — the market-led campaign pipeline (under construction)

The centerpiece of the operating layer: map the market → refine → find people → write →
personalize → send. Form: **pipeline** — numbered stages, each a gate a human reads
before the next stage runs.

## Construction state, honestly

- `skeleton.md` is the mechanism map of Michael's six-part TAM series — a ~270-line
  abstraction that preserved the stages and mechanics but stripped his text, examples,
  and reasoning. It is the map of what the pipeline covers, **not** the pipeline.
- The operator has improved on Michael's framework; the improved version lives in the
  operator's second-brain workspace and lands here as the operator briefs it in.
- **Stage folders are created when their content arrives, not before.** When the brief
  lands, each stage becomes `NN-<stage>/` with a contract per the ICM stage template,
  written to `foundations/task-craft.md`.

## The six stages (names fixed by the skeleton; content arriving)

1. TAM mapping — *the segment-definition question routes through `experiments/002`*
2. TAM refinement
3. Find people & enrich — *pairs with `../workflows/enrichment.md` + `-techniques.md`*
4. Copywriting & testing — *instrument choice routes through `experiments/001`*
5. AI personalization
6. Deliverability & send setup — *pairs with `../playbooks/deliverability-and-warmup.md`*

## Reads / does / writes

- **Reads:** `skeleton.md`; the account's `context/` files each stage names; the two
  experiment records where an instrument choice exists.
- **Does:** turns a market definition into a launched, measured campaign.
- **Writes:** everything into `accounts/<slug>/outputs/campaigns/<slug>/` — the pipeline
  itself stores nothing between runs.

## Human gate

The operator's brief is the gate on this folder's own construction: nothing in
`skeleton.md` is rewritten ahead of it, and Cowork evaluates each landed stage before the
next is built.
