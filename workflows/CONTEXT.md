# workflows/ — contract and lineage tags

How a team operates, end to end: human process docs, not execution instructions for Claude
(`README.md` at root explains the skills/workflows split). This file is the folder's
contract: what each doc is, which lineage it carries, and what may load together.

Lineage model: `docs/lineages.md`. Tags: `upstream` · `operator` · `imported`.

## Files

| File | Lineage | What it is | Pairs with / diverges from |
|---|---|---|---|
| `campaign-build.md` | `upstream` | The **signal-led** campaign process: a fired signal → audience → launch → measurement | Complements `tam-campaign.md` (C2 — not a conflict; different starting conditions) |
| `tam-campaign.md` | `imported` | The **market-led** process: map the market → refine → find people → test value props on a fixed template | Carries conflict **C1** (fixed-slot copy vs PVP) — see its doctrine note |
| `enrichment.md` | `upstream` | The data waterfall: free sources → orchestrator → proprietary | Extended by `enrichment-techniques.md`; carries core's sanctioned defaults |
| `enrichment-techniques.md` | `imported` | Technique patterns: action cost model, own-API-key, webhooks, four scraping patterns | Points at `enrichment.md` for defaults rather than restating |
| `signal-routing.md` | `upstream` | Signal fires → what happens next (the decision tree) | Routes into `playbooks/plays/` since the library landed |
| `pain-based-segmentation.md` | `imported` (2026-08-10) | The **segment-agnostic** targeting doctrine: segments defined by a shared Existential Data Point, not firmographics — the fundamental question moves from "who can we service" to "what pain can we resolve" | Carries conflict **C4** (pain map vs firmographic map) — keeps the four-dimension scoring mechanism, changes what feeds it |

## Loading

Load ONE campaign workflow per session — signal-led or market-led, decided by the starting
condition (have a signal → `campaign-build.md`; have only a market definition →
`tam-campaign.md`). Loading both invites blending doctrines the lineage rules keep apart.
The enrichment pair loads together by design (reference + techniques).
`pain-based-segmentation.md` loads at segmentation time: with `tam-campaign.md` it
REPLACES the market-mapping step (C4 — pick one segment definition and say which); with
`campaign-build.md` it defines what counts as a signal.

## Revision rule

An edit that would make one lineage's doc agree with another's doctrine is a **conflict
resolution** and follows `docs/lineages.md` rule 2: dated entry there first, then the edit.
Additions within a doc's own lineage are ordinary edits.
