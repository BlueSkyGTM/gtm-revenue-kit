# Stage 1 — Mapping

**Cost:** fast when the market lives on the professional-network graph (a filter
exercise); genuine research when it needs a bespoke source — budget the research, not the
pull. *Step budgets land after the first operated run (`operator-proven`); the
qualitative split above is the honest pre-operation contract — inventing minutes now
would be fabricated specificity.*
**Output:** the TAM artifact, v0 — one broad table with its rules and suppression
columns, saved to `accounts/<slug>/outputs/YYYY-MM-DD-tam-map/` (dated; the map is
product, refreshed by re-running this stage, never edited in place).

*Provenance: mechanics from Michael's series (`../skeleton.md` §Stage 1,
`michael-course`); the anti-ICP output from the operator's improvement (`../BRIEF.md` §1);
drafted by the construction session under the brief's stage-1 authorization.
**Evaluated 2026-08-14: AMEND, applied** — clean on fabricated-specificity, anti-ICP
rendering, and law; both amendments (map declaration first; the budget slot declared)
are in this text. The record: `EVALUATION-2026-08-14.md`.*

---

## Quick Start

```
Read motions/tam/01-mapping/CONTEXT.md and map the market for account [slug]
```

## Purpose

One table containing, in broad strokes, every company in the addressable market — **with
the negative space named on the same artifact**: who is excluded and why, as rules that
can bind.

The goal is *not* a scored list, and not an ICP-narrowed pull — narrowing at the source
silently excludes companies you can never get back (skeleton: map broad, filter later;
the output is allowed to be dirty). And the goal is not a list whose exclusions exist
only as absence: an exclusion that isn't written down cannot be debugged, and an
anti-ICP rule that never rejects anyone is decoration (`../BRIEF.md` — an exclusion
produces signal when it binds).

**Waste this stage prevents** (`foundations/revenue-engineering.md` §taxonomy):
identification waste — research spent outside the map or below threshold — and reach
waste, both killed *at the map*, before any downstream stage spends a dollar.

## Inputs

- `accounts/<slug>/context/icp-definition.md` — the raw material for the rules in Step 4
  (who we sell to, and the exclusion list that becomes anti-ICP rules). **Under a pain
  map (Step 1), the raw material is the segment definitions from
  `motions/workflows/pain-based-segmentation.md` instead** — pains at thresholds, not
  firmographic brackets. *(Found on the first operated run, 2026-08-14: the line above
  assumed the firmographic case.)*
- `accounts/<slug>/optouts.md` + the account's declared rosters (`ACCOUNT.md`) — to mark
  suppression on the map in Step 5
- `motions/workflows/enrichment-techniques.md` — the scraping patterns, when Step 1 lands
  on a bespoke source
- `experiments/002-segment-definition.md` — the open segment-definition test Step 1
  declares under

## Step 1: Declare which map draws the audience

Firmographic map or pain map — state it in the run's brief before anything else
(`experiments/002` is open; the two are never blended in one campaign). This declaration
comes first because it governs everything after it: it decides what "these businesses"
*means*. Under a pain map, the addressable market is defined by the shared pain
condition rather than corporate structure — and the enumeration source can change with
it, because a professional graph enumerates by structure while a pain condition may need
a different source entirely.

## Step 2: Pick the enumeration source

The entire step reduces to one question, answered before any tool is opened — with
"these businesses" meaning whatever Step 1 declared:

> **What is the best place on the internet to find the complete list of these
> businesses?**

The answer follows from incentives — a company shows up completely and accurately only
in places it benefits from being listed:

| If the target sells... | It is probably best enumerated in... |
|---|---|
| B2B services or software | A professional network's company graph |
| Physical products online | A store-intelligence database (e-commerce stores often have no professional-network presence at all) |
| Locally, from a physical location | A maps platform — restaurants, gyms, clinics, and trades live on maps |
| Into a licensed or credentialed niche | A vertical directory — registries, association lists, marketplace indexes |

Roughly half of markets come straight from the professional graph (mapping is fast); the
other half each need a bespoke source, and finding it is genuine research — read the
scraping patterns before concluding a market can't be mapped.

## Step 3: Pull broad

Do not encode ICP nuance into the source query — pulling too narrow silently loses
companies forever; pulling broad costs only a cheap classification pass in Stage 2.
Dirty is acceptable; missing is not recoverable.

## Step 4: Write the rules — ICP and anti-ICP together

Two rule sets, drafted side by side from the account's ICP definition, each written so a
machine could apply it and a human could argue with it:

- **ICP rules** — who is in, stated positively.
- **Anti-ICP rules** — who is *out on fit grounds*, stated positively, **with the reason
  in the rule**: "we do not sell to X because Y." Not a low score — a stated rejection.

The anti-ICP is first-class output, not hygiene: it is where avoided-cost lives, and
Stage 2 will test whether each rule actually binds against the sourced list. A rule
nobody can imagine rejecting a real company gets rewritten now, not shipped.

## Step 5: Mark suppression on the map

Columns on the artifact itself — opt-outs (the account's `optouts.md`), existing
customers, others' open opportunities — so stages 2–6 and every play inherit suppression
for free instead of re-deriving it per send. Suppression stays per-account and
append-only (principle 5); the map *reads* the ledger, never becomes it.

## Output contract → Stage 2

The TAM artifact v0: the broad table · the ICP rule set · the anti-ICP rule set with
reasons · suppression columns marked. **Every company will end up in exactly one tier,
including the below-threshold tier nobody works** — the tiering itself is Stage 2's job;
this stage's job is that nothing reaching Stage 2 is unaccounted for.

## Human gate

The operator reads the anti-ICP rules before Stage 2 runs. The check: could each rule
plausibly reject a real company this account would otherwise have pursued? Rules that
can't bind are decoration; rules that would bind on half the map are information about
the sourcing. Numeric thresholds, if any emerged, moved to
`accounts/<slug>/context/scoring-model.md` — this file holds none. The output is also
*judged*, not only checked: identify's criteria,
`foundations/conceptual-framework.md` §1.
