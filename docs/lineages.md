# Lineages — parallel method traditions, kept parallel on purpose

This engine carries methods from more than one tradition, and some of them disagree. That is
by design. **A lineage is never overwritten by another, and a conflict between lineages is
recorded, not silently resolved.** This file is the model; each folder's `CONTEXT.md`
carries the per-file tags.

## Why parallel instead of merged

Merging two method traditions produces a third thing nobody proved. Each lineage earned its
shape somewhere — a doctrine that looks "wrong" by another lineage's test is usually
optimizing a different regime, and the disagreement itself is information. The engine keeps
both, states where they conflict, and leaves the choice where it belongs: **an account picks
its doctrine per track, in its own files**, and core revises a conflict only as a deliberate,
recorded decision — never as a side effect of importing or editing.

## The three lineages

| Tag | Origin | What carries it |
|---|---|---|
| `upstream` | The original open-source kit (preserved at tag `baseline-gtm-starter-kit`) | The six skills' skeletons, the six context files, `workflows/campaign-build.md`, `enrichment.md`, `signal-routing.md`, `playbooks/new-signal-response.md`, `competitor-switch.md`, the **PVP copy standard** in `docs/standards.md` |
| `operator` | Built or proven in live operation of the engine (the vendored era and this repo's own work) | The multi-account architecture, values/mechanism split, `reply-handling`, `impact-positioning`, `deliverability-and-warmup`, the dormant shelf, the linter, the rule shelf itself |
| `imported` | Operator-curated external method material, abstracted into original core docs (arrival 2026-08-08) | `playbooks/plays/` (all 15), `playbooks/channels/` (all 4), `workflows/tam-campaign.md`, `workflows/enrichment-techniques.md` |

Tags live in each folder's `CONTEXT.md`, per file. A new import gets a new tag and a new
arrival date; nothing about this table is closed.

## Known doctrinal conflicts (recorded, unresolved)

**C1 — First-touch copy doctrine: PVP vs the fixed-slot template.**
- `upstream` (PVP, `docs/standards.md`): strip the CTA; if the message still teaches the
  prospect something about their own business, it passes. A message pointless without the
  ask is a pitch. Mandatory for Tier 1–2 first touches under that standard.
- `imported` (fixed-slot, `workflows/tam-campaign.md` §copy, used by
  `playbooks/channels/cold-email.md`): a deliberately plain, never-rewritten template —
  personalized line, "if I could {outcome} via {unique system}, {social proof}" and a direct
  interest question — where the ONLY things ever tested are the value proposition and the
  list. By PVP's own test this is a pitch, deliberately: it optimizes yield discovery at
  volume, not per-message value delivery.
- **Status: parallel.** A tier-based reconciliation (volume-template for the broad market,
  PVP for the researched head of the list) is **proposed** in `tam-campaign.md` and marked
  there as a proposal from the import pass — an account may adopt it, and core has NOT
  settled it. What is settled: never blend the two doctrines inside one campaign.

**C2 — List construction: signal-led vs market-led.** `campaign-build.md` (upstream) starts
from a fired signal; `tam-campaign.md` (imported) starts from the market and works down.
**Not a conflict — complements.** Recorded here only because readers keep asking; the two
cross-reference each other and cover different starting conditions.

**C3 — Import-pass normalization of the plays.** The 15 plays' message-frame sections were
written against the PVP standard during abstraction, while their source tradition leaned
fixed-slot. The *mechanisms* (signals, builds, measurement) are faithful; the frames carry
an upstream accent. Recorded so a future revision knows the frames are the import pass's
rendering, not the source tradition's own voice.

## Rules

1. **No lineage overwrites another.** An imported method that overlaps a native one lands
   beside it, tagged, cross-referenced — like `tam-campaign.md` beside `campaign-build.md`.
2. **Conflicts are recorded here, resolutions happen deliberately.** A resolution is a
   dated entry in this file plus the edit, never an inline blend.
3. **Accounts choose.** `ACCOUNT.md` or a track's files may declare which doctrine a
   campaign runs under. The engine serves both; the linter enforces the account's own copy
   rules either way.
4. **New imports get their own tag.** Curated material from a new source is a new lineage
   row with an arrival date, and its overlaps get recorded in the conflict table on arrival.
