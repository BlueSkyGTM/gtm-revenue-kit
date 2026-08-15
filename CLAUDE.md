# GTM Kit

Machinery for **revenue engineering**: the connective layer that turns signals into won
work without waste. One shared engine, vendored into each business OS that runs it; every
operating account lives in its deployment, never here (`estate.md`). Form: four method
wings — foundations · motions · signals · experiments — over the account template.

**This file is the map — it routes, it holds no content.**

> **Stages arriving:** the TAM pipeline runs six stages; 1–2 are drafted and evaluated,
> 3–6 land as the operator briefs them. `motions/tam/CONTEXT.md` states what is real
> vs. arriving.

## The one rule

**Name the account first.** Nothing loads until it is known; context loaded under the
wrong account produces confident answers from the wrong buyer's facts. If unclear, ask.

## Folder map

```
gtm-kit/
├── CLAUDE.md · CONTEXT.md   ← this map · the task router
├── README.md · NOTICE.md    ← build state · attribution
├── estate.md                ← what the kit owns vs reads; the deployments map
│
├── foundations/   the why-layer: revenue-engineering · revenue-architecture ·
│                  chain-of-operations · principles · failure-modes ·
│                  conceptual-framework · lexicon · rulings ·
│                  task-craft · pvp                               → its CONTEXT.md
├── motions/       the operating layer: skills · plays (15, Michael's) ·
│                  channels · tam/ (pipeline, under construction) ·
│                  workflows · playbooks · dormant                → its CONTEXT.md
├── signals/       the signal library: schema + admitted records  → its CONTEXT.md
├── experiments/   open instrument tests, queued and closed       → its CONTEXT.md
├── decisions/     construction-level calls with their evidence
│                  (triage + audit records)                       → its CONTEXT.md
│
├── accounts/      the stamp (_template/) + catalog (_index.md) — operating
│                  accounts live in deployments, never here       → its CONTEXT.md
├── tools/ · sync/ · examples/   linter · result-pull · Relay (read-only)
└── _archive/      superseded material, never load
```

## Routing

| You need | Read |
|---|---|
| "What's my task? → which file?" | `CONTEXT.md` |
| What revenue engineering IS — the definition, laws, waste taxonomy | `foundations/revenue-engineering.md` |
| The rules (admission, swap test, values, one-home, suppression, travel) | `foundations/principles.md` |
| Before any structural decision — what layer am I at | `foundations/chain-of-operations.md` |
| How a revenue system is designed — the architecture layer | `foundations/revenue-architecture.md` |
| Before drafting for core, and before committing it | `foundations/failure-modes.md` — the tells and the self-check |
| Method is silent on your case — or: is this output *good*? | `foundations/conceptual-framework.md` — the pillars as tools |
| A term could go two ways | `foundations/lexicon.md` |
| Has the operator already settled this? | `foundations/rulings.md` — a ruling outranks an inference |
| First-touch copy doctrine | `foundations/pvp.md` — both instruments, `experiments/001` |
| How to write a skill/play/stage | `foundations/task-craft.md` |
| What a signal must carry to exist | `signals/schema.md` |
| Two methods disagree | `experiments/` — queued tests, not curated doctrine |
| A construction-level call and its evidence (absorb/replace/disregard, audits) | `decisions/` |
| Which copy of the kit holds what | `estate.md` |

## Authority — what outranks what

1. **The operator's ruling**, live in the session, outranks everything below it.
2. **`foundations/rulings.md`** — the dated record of past rulings. Outranks any inference
   a session makes. Append-only; a contradiction with core is a finding to surface, not to
   blend away.
3. **`foundations/` doctrine** — principles, chain-of-operations, failure-modes, lexicon.
   Authoritative over method files, and each carries its provenance.
4. **Method** (`motions/`, `signals/`, `accounts/_template/`) — cites doctrine, never
   restates it.
5. **A session's own reasoning** — lowest. Where it conflicts with anything above, the
   above wins; where it fills a gap none of them cover, it is marked as the drafter's
   rendering.

Doctrine is *checked against*, not narrated through. A draft that keeps announcing which
rule it is obeying has produced the ceremony corruption `failure-modes.md` §3 describes.

## Hard lines

- Core never names an account — the swap test (`foundations/principles.md` §2).
- Every number lives in the account's `context/scoring-model.md` (§3).
- Suppression before every send, per account, append-only (§5) — legal floor, not
  architecture.
- No live `.mcp.json` in this repo; no send tool in core, ever.
