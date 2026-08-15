# GTM Kit — build state

Machinery for revenue engineering: one shared engine, vendored into each business OS that
runs it, holding the motions that connect signals to won work. The map is `CLAUDE.md`;
the router is `CONTEXT.md`; where the kit sits in the estate is `estate.md`. **This file
is the build state** — what is real, what is arriving, and in what order.

## The reconstruction, and why

The kit was rebuilt on this branch (2026-08-13) around one rule
(`foundations/principles.md` §1): **nothing enters core unless we can say why it is
here.** Three whys are accepted — course-reasoned (Michael's), operator-proven (ran live),
upstream-verified (read and endorsed). The prior governance layer — a rule shelf, a
lineage system with a curated conflict register, a product shell — was retired whole to
`_archive/2026-08-13-framework/` (its README maps where each living part went). What
replaced it is smaller: one principles page, one experiments queue, one estate map.

Provenance of every part: `NOTICE.md`. The pristine upstream is tagged
(`baseline-gtm-starter-kit`), so what came from where is a diff, not an assertion.

## Status at a glance

| | Piece | State |
|---|---|---|
| 🟢 | **Foundations** (11 files) | The discipline (08-13) plus the operation's judgment layer (08-14): the six-rung ladder, the failure modes with their tells and the six-step self-check, the lexicon, and `rulings.md` — append-only, the standing channel for what the operator has settled. Audited 08-14 with retractions on the record (`decisions/2026-08-14-foundations-audit.md`). **When operation catches up, foundations get a clean-eyes review that purges stale material and assumptions — nothing grandfathered [operator, 08-14]** |
| 🟢 | **Skills** (6) — account-gated, upstream craft | Carried over working; icp-scoring's upstream defaults restored; sequence-shape mechanism restored to signal-to-sequence |
| 🟢 | **Plays** (15, Michael's) — the operating play library | Mechanisms faithful; backstory returns incrementally as plays are exercised |
| 🟢 | **Channels** (4, Michael's) | Carried over |
| 🟡 | **TAM pipeline** — the centerpiece | Stages 1 and 2 drafted and evaluated (AMEND both, applied; records beside each stage). Stage 3 waits on its brief — the construction law, not a scheduling gap. Stage briefs 3–6 owed |
| 🟡 | **Signal library** | Schema written; F/I/R/T **adopted, operator-confirmed 08-14**; shelf deliberately empty until records earn their why |
| 🟡 | **Experiments** — 001 first-touch formula, 002 segment definition | Queued; both run in the albatross deployment's own `revenue-engineering` account. 002 upgraded 08-14: the overwrite-prediction is argued-not-evidenced (research on file) — 002 would generate some of the field's first real evidence; DQS recorded as a distinct third map type |
| 🟢 | **Account stamp** (`accounts/_template/`) | Upstream scoring defaults restored; benchmark-free stance recorded (own campaign data seeds §8, `operator-proven`) |
| 🟡 | **Runtime** — the kit as the GTM motion runtime over Deepline | **Spec v0 + the public-pack triage, both 08-14** (`runtime-spec.md`, `decisions/2026-08-14-deepline-skills-triage.md`): ICM-as-program, execution blocks in contracts, two mechanical gates (consent and cost). Wiring waits on the operator's runtime inputs — nothing else |
| ⚪ | **Estate siblings** — offers/SKUs, funnel, brand voice, copywriting | Not built; their material squats here, declared in `estate.md` |

🟢 real · 🟡 under construction, honestly labeled · ⚪ future machinery

## What happens next, in order

The order leads with operating — the audit's one standing correction is that the fix
for doctrine written ahead of operation is to run the pipeline, not to write more
(`decisions/2026-08-14-foundations-audit.md`). Items 2–4 wait on the operator;
`foundations/rulings.md` §Open is the live queue.

1. **Operate — run TAM stages 1–2 for the active deployment's own account** (`estate.md`
   names it), manually if the runtime inputs are not yet in hand. The map is the first
   real artifact; benchmarks, signal whys, and stage evaluation in anger all feed from
   it.
2. **The runtime inputs** — the API account and providers, the datastore per deployment,
   the send-approval scope named in writing (`runtime-spec.md` §6). These unblock
   execution blocks for TAM stages 1–3.
3. **Stage briefs 3–6** — per-stage mechanics and deltas. Folders wait; empty is visible.
4. **The signal set, the verbatim template (licensing first), the course's location.**
5. **Albatross runs it** — the first campaigns execute experiments 001 and 002 in its own
   `revenue-engineering` account (two addresses warming through the pause).
6. **Re-vendor** — deployments pull the rebuilt core when it stabilizes.

## Deployments

Two, both founder-owned; the kit is internal machinery, not a retail product. Core
travels to both; each account lives in exactly one. The map and the plan of record:
`estate.md`.

## Working in this repo

- Rules: `foundations/principles.md` (one page — read it before editing core).
- Writing a skill, play, or stage: `foundations/task-craft.md`.
- Core compliance check: the swap test grep in `foundations/principles.md` §2 — core
  outside `NOTICE.md`/`estate.md`/`examples/` names no account and holds no tuned number.
- Before committing anything here: `foundations/failure-modes.md` §The self-check.
