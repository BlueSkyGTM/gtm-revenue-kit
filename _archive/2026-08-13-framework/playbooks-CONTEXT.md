# playbooks/ — contract and lineage tags

Situation guides and method libraries. This file is the folder's contract: the shelf map,
the lineage tag per file, and the revision rule that keeps parallel traditions parallel.

Lineage model: `docs/lineages.md`. Tags: `upstream` · `operator` · `imported`.

## Shelf map

| Where | What | Lineage |
|---|---|---|
| `new-signal-response.md` | Signal fires: validate → score → research → send | `upstream` |
| `competitor-switch.md` | Four competitive scenarios | `upstream` |
| `impact-positioning.md` | Six-step positioning construction + audit | `operator` |
| `deliverability-and-warmup.md` | Sending infrastructure and domain safety | `operator` |
| `plays/` | The 15-recipe signal-play library (own `CONTEXT.md`) | `imported` |
| `channels/` | Four channel playbooks (own `CONTEXT.md`) | `imported` |
| `dormant/` | Methods with no active motion yet (own `README.md`) | `operator` (shelf) — contents individually tagged in their headers as they accrue |

## The one conflict that crosses this folder

**C1 (copy doctrine)**: `channels/cold-email.md` builds on the imported fixed-slot template;
`new-signal-response.md` and the plays' message frames lean on upstream PVP. Both are
correct within their lineage. Never blend them in one campaign; never "fix" one to match
the other outside the `docs/lineages.md` resolution process.

## Revision rule

- A new method from outside lands **beside** what exists, tagged, cross-referenced — never
  over it. If it overlaps a native doc, both stand, and the overlap gets a row in
  `docs/lineages.md`.
- Within a lineage, edit freely. Across lineages, record first (`docs/lineages.md` rule 2).
- Activating a dormant method is a core change (it goes live for every account) — localize
  by pointing at `accounts/<slug>/context/`, never by writing values in.
