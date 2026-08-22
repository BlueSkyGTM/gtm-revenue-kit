# GTM Revenue Kit

**Revenue pipelines as file architecture.** The rules that decide who gets contacted, what they
get sent, and what must be true before anything sends — written down as files, in version control,
where a person can read them and disagree with them.

One agent walks the folder structure, loads the one contract its task names, and stops. There is
no framework to install and no orchestration layer to reason about: **the structure is the
program.**

**The argument.** The failure this is built against is *unreadable state* — systems where nobody
can look and see what the thing will do next, and where connection count gets mistaken for
capability. Here the state **is** files.

This is where the field has landed, not a private preference. Anthropic's published engineering
guidance on building agents reaches it from the model side: simple composable patterns over
frameworks, and systems transparent enough that a person can see *why* the thing did what it did.
**This kit is that principle applied to revenue work** — the reason a prospect was contacted, or
excluded, is a file you can open and argue with.

**The boundary, in the same breath:** this loses at real-time multi-agent collaboration,
high-concurrency serving, and automated mid-pipeline branching, which need framework code. It
suits sequential, human-reviewed, repeatable work — most revenue work, but not all of it.

## Read it in five minutes

[`examples/sample-company/`](examples/sample-company/) — a produced campaign and the folder it came
out of; start here, the argument is downstream of the artifact. Then
[`CONTEXT.md`](CONTEXT.md), the task router: every job and the one file that holds it. Then
[`foundations/principles.md`](foundations/principles.md) — the six rules, one page.

## What this is

| Wing | What it holds | State |
|---|---|---|
| [`foundations/`](foundations/) | The why-layer: the discipline's definition, the eight revenue functions, the six-rung chain of operations, failure modes, lexicon, and an append-only ruling record | **Complete** — 13 files |
| [`motions/`](motions/) | What runs: 6 account-gated skills, 15 signal plays, 4 channel playbooks, 4 situation playbooks, 6 workflows, 5 shelved methods, and the market-mapping pipeline | **Skills, plays, channels live.** Pipeline stages 1–2 of 6 drafted and evaluated; 3–6 unbriefed |
| [`accounts/_template/`](accounts/) | The stamp every operating account is copied from. Mechanism in core, every number in the account | **Context files ship; `brand/` slots empty by design** — voice, offer-map and brand-psychology wait on the branding sibling |
| [`signals/`](signals/) | The record schema a signal must satisfy to exist | **Schema written; library deliberately empty** — no record enters without its buying mechanism stated |
| [`experiments/`](experiments/) | Open method conflicts, queued as tests rather than resolved by preference | **2 queued, 0 run** |
| [`decisions/`](decisions/) | Construction-level calls with their evidence, including the ones that were wrong | **6 records** |

## What it is not

Not a multi-agent framework, not a SaaS product, not a sequencer. **There is no send capability in
this repository and there is not meant to be** — suppression is checked before every batch, per
account, append-only, and the wall between method and sending is a design decision rather than a
missing feature.

## Technical achievements

**Inherited proven, not claimed.** The upstream kit supplied the multi-account architecture, the
account gate carried inline by all six skills, per-account append-only suppression, and the
send-tool wall. The plays and channel playbooks came from coursework and **their mechanisms are
unchanged** — with no campaign run there is no evidence on which to claim an improvement, and
saying otherwise is the kind of thing this repo exists to catch.

**What this repo built:** the doctrine layer — an admission test nothing enters without passing, a
swap test making account contamination mechanically checkable, a conceptual framework on the FASB
pattern so a session derives a treatment from the pillars when method is silent instead of
improvising or stalling, and a six-question self-check before anything commits. Plus the wiring
that turns a shelf of documents into an ecosystem: a play activates through the account's signal
library, routes to a named skill, takes its numbers from that account's scoring model, and clears
suppression before anything sends.

## Room for growth

1. **Nothing has been sent.** Zero campaigns, zero prospects contacted. `learn` is structurally
   present and empty in practice — the flywheel exists on paper and has never turned.
2. **Capture is half-built.** Reply handling and intake are live; the page-and-form half is
   declared out of scope and not built ([`estate.md`](estate.md)).
3. **The runtime is specified, not wired.** [`runtime-spec.md`](runtime-spec.md) is v0 and marked
   SPEC ONLY; three operator inputs gate every execution block.
4. **Pipeline stages 3–6 have no briefs**, and **no instrument yet declares which of the eight
   functions it serves** — a rule written after the material it governs
   ([audit](decisions/2026-08-22-inherited-material-retention-audit.md)). Folders are created as
   content is briefed, never before, so both gaps stay visible.
5. **Known internal inconsistencies**, found by walking the kit cold before publishing and
   recorded in full ([the walk test](decisions/2026-08-22-cold-walk-test.md)): the copy linter
   contracts against a `brand/voice.md` no account setup produces, so that gate is currently
   decorative; the router and the account-research skill disagree on where output lands; two of six
   skills lack the `## Inputs` block their shelf contract requires; `playbooks/` and `dormant/` are
   unreachable from the task router.
6. **Open questions belong to the operator**, listed in
   [`foundations/rulings.md`](foundations/rulings.md) §Open. A session that needs one asks; it
   does not decide.

## Rules of the road

Name the account before anything loads · core never names an account · every number lives in the
account · one home per fact · suppression before every send · load the one file the task names,
never a whole folder. Full text: [`foundations/principles.md`](foundations/principles.md).

## Provenance

[`NOTICE.md`](NOTICE.md) records every inherited element — what came from where, under what
licence, what was checked and when. It also records a credential mistake this project made
assessing a source, and its retraction. Both are kept on purpose: [`decisions/`](decisions/) is a
record of reasoning, including reasoning that turned out to be wrong. Licence:
[MIT](LICENSE), covering this repository's own work.
