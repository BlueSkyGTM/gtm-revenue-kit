# Stage 2 — Refinement (exclusion hardening)

**Cost:** cheap by design — the whole stage is classification passes priced per row, and
the cost logic lives in `../../workflows/enrichment-techniques.md`. *Step budgets land
after the first operated run (`operator-proven`); the qualitative contract — cheap
passes, never bespoke research — is the honest pre-operation statement.*
**Output:** the refined TAM artifact — every company in exactly one tier including the
below-threshold tier nobody works, one auditable verdict column, the exclusion rules
tested and their catches recorded. Saved to
`accounts/<slug>/outputs/YYYY-MM-DD-tam-map/` beside the broad map it refines. *(The
artifact is finished for this cycle's purposes, not permanently: stages 3–6 consume it
and the refresh pass re-runs both stages.)*

*Provenance: mechanics from Michael's series (`../skeleton.md` §Stage 2,
`michael-course`); the exclusion-hardening delta from the operator's improvement
(`../BRIEF.md` §1 — "Stage 2 gains exclusion hardening"); drafted by the construction
session, then self-evaluated against `foundations/failure-modes.md` §The self-check —
verdict AMEND, three items applied (`EVALUATION-2026-08-14.md`).*

---

## Quick Start

```
Read motions/tam/02-refinement/CONTEXT.md and refine the map for account [slug]
```

## Purpose

The broad, dirty map from Stage 1 becomes the finished artifact: companies that actually
match, companies that don't — **with the reasoning recorded per row** — and the negative
space hardened from rules-on-paper into rules-that-fired.

The goal is *not* a re-research pass: refinement is cheap classification, and any row
that needs a human hour belongs in Stage 3's head-of-list work, not here. And the goal
is not a clean-looking list: **a refinement pass that rejected nothing is a failed
pass** — either the sourcing was implausibly perfect or the rules are decoration
(`../BRIEF.md`: an exclusion produces signal when it binds).

**Waste this stage prevents** (`foundations/revenue-engineering.md` §taxonomy):
identification waste — every dollar of Stage 3 enrichment and research spent on a row
that a one-cent classification pass should have cut.

## Inputs

- The Stage 1 artifact (v0): the broad table, the ICP and anti-ICP rule sets, the
  suppression columns
- `accounts/<slug>/context/icp-definition.md` — the exclusion list the rules were
  drafted from, for reconciling any rule the pass proves wrong
- `accounts/<slug>/context/scoring-model.md` — every numeric boundary (employee floor,
  revenue band, tier thresholds) reads from here; this file holds none
- `../../workflows/enrichment-techniques.md` — the cost model for choosing each
  question's cheapest tool

## Step 1: Write each rule as a question a machine can answer

One disqualifier, one yes/no question, answerable from public data: "Does this company
sell physical products?" · "Is it in an industry on the exclusion list?" · "Does its
site show [the disqualifying practice]?" The anti-ICP rules from Stage 1 arrive already
reasoned; this step only makes them mechanical. A rule that cannot become a question a
machine can answer goes back to Stage 1 for rewriting — it was never a rule.

## Step 2: Answer each question with the cheapest tool that can answer it

Free formatting functions where the answer is mechanical; a low-cost classification pass
(an LLM through your own API key, never platform credits) where judgment is needed. One
column per question — never one mega-prompt for all of them, because per-column answers
are what make the verdict auditable.

## Step 3: Combine into one verdict column — and record what each rule caught

A single ICP verdict per row, derived from the columns, so a human can audit *why* a
company was kept or cut. Then the hardening, which is this stage's addition to the
mechanics: **per exclusion rule, count what it caught.**

- A rule that caught nothing: flag it — decoration, or the sourcing pre-filtered it.
  Either is information; neither is silently fine.
- A rule that caught a large share of the map: information about the sourcing — Stage
  1's source selection gets that feedback before the next map refresh.
- The below-threshold tier is **drawn, not discarded**: every company lands in exactly
  one tier, including the one nobody works. Tier boundaries come from the account's
  `scoring-model.md`; the map records membership, never invents the numbers.

## Step 4: Carry suppression forward

The suppression columns from Stage 1 survive refinement untouched — a suppressed row
keeps its mark whatever tier it lands in, and the suppressed count is recorded alongside
the exclusion catch counts (a suppression pass that kills a large share of a sourced list
is information about the sourcing — `../BRIEF.md` §1).

## Output contract → Stage 3

The finished map: tiered rows (below-threshold tier included) · per-question columns ·
one auditable verdict column · exclusion rules with their catch counts · suppression
carried. Stage 3 works the map top-down and never re-derives who is in it.

## Human gate

The operator reads the catch counts before Stage 3 spends money: which rules bound,
which caught nothing, whether the suppression rate says the sourcing is off. This is the
gate where the anti-ICP stops being prose — a map whose exclusions all fired plausibly
is hardened; one whose exclusions never fired goes back a stage. The output is also
*judged*, not only checked: identify's criteria,
`foundations/conceptual-framework.md` §1.
