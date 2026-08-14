# motions/ — the operating layer contract

What actually runs. Everything in this wing either executes (skills), composes execution
around a situation (plays, playbooks, channels), documents the human process (workflows),
or is the campaign pipeline itself (`tam/`). Written to `foundations/task-craft.md`, held
to `foundations/principles.md`.

## The shelves

| Shelf | Form | What it is | Provenance |
|---|---|---|---|
| `motions/skills/` | executable tasks | the six account-gated skills a session runs from a one-line prompt | upstream craft, account gate added |
| `plays/` | record library, 15 | Michael's signal plays — one buyer moment each, composing the skills | course-reasoned (`NOTICE.md`) |
| `channels/` | record library, 4 | how each outreach medium works as a system | course-reasoned |
| `tam/` | **pipeline, under construction** | the market-led campaign pipeline — Michael's skeleton, being rebuilt from the operator's improved framework | course skeleton + operator's second brain |
| `motions/workflows/` | process docs | signal-led campaign build, signal routing, enrichment pair, pain-based segmentation | mixed, marked per file |
| `motions/playbooks/` | situation guides, 4 | new-signal response, competitor switch, impact positioning, deliverability & warmup | upstream ×2, operator ×2 |
| `dormant/` | shelved methods | methods no active motion uses yet — found, not rebuilt, when needed | operator |

## Load discipline (the part sessions get wrong)

- Name the account first; nothing loads until it is named.
- **One campaign workflow per session:** have a signal → `motions/workflows/campaign-build.md`;
  have only a market → `tam/`. Never both.
- `motions/workflows/pain-based-segmentation.md` loads at segmentation time and replaces the
  market-mapping step it competes with — the campaign brief says which map drew the
  audience (`experiments/002`).
- The enrichment pair (`enrichment.md` + `enrichment-techniques.md`) loads together by
  design.

## First-touch copy

Two instruments, account's choice, never blended in one campaign: `foundations/pvp.md`
holds both the PVP test and the relation to the fixed-slot template
(`experiments/001` is the open test).

## Human check

A new play, channel doc, or workflow enters with its provenance stated in its header and
passes `foundations/principles.md` §1. If it carries a number, the number moves to the
account template with a "default, recalibrate" mark before merge.
