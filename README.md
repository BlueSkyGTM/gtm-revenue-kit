# GTM Revenue Kit

**Revenue pipelines as file architecture.** The rules that decide who gets contacted, what they
get sent, and what must be true before anything sends. Written as files, in version control, where
a person can read them and disagree with them.

One agent walks the folder structure, loads the one contract its task names, and stops. There is
no framework to install and no orchestration layer to reason about. **The structure is the
program.**

## The argument

Most go-to-market logic lives inside SaaS configuration screens, where nobody can read it, review
it, or say why an account was contacted. The failure that produces is *unreadable state*: systems
where no one on the team can look and see what the thing will do next, and where connection count
gets mistaken for capability.

Here the state **is** files. The reason a prospect was contacted, or excluded, is a document you
can open and argue with.

This is where the field has landed rather than a private preference. Anthropic's published
engineering guidance on building agents reaches the same conclusion from the model side: simple
composable patterns over frameworks, and systems transparent enough that a person can see *why*
the thing did what it did. This kit applies that to revenue work.

**The boundary, stated in the same breath.** This approach loses at real-time multi-agent
collaboration, high-concurrency serving, and automated mid-pipeline branching, all of which need
framework code. It suits sequential, human-reviewed, repeatable work, which is most revenue work
but not all of it.

## Read it in five minutes

[`examples/sample-company/`](examples/sample-company/) holds a produced campaign and the folder it
came out of. Start there; the argument is downstream of the artifact. Then
[`CONTEXT.md`](CONTEXT.md), the task router: every job and the one file that holds it. Then
[`foundations/principles.md`](foundations/principles.md), the six rules, one page.

## What it holds

| Wing | What it does |
|---|---|
| [`motions/`](motions/) | What runs: 6 account-gated skills, 15 signal plays, 4 channel playbooks, 4 situation playbooks, 6 workflows, and a staged market-mapping pipeline |
| [`foundations/`](foundations/) | The why-layer, 13 files: the discipline's definition, the eight revenue functions, a six-rung chain of operations, failure modes, a lexicon, and an append-only ruling record |
| [`accounts/_template/`](accounts/) | The stamp every operating account is copied from. Mechanism lives in core, every number lives in the account |
| [`signals/`](signals/) | The record schema a signal must satisfy to exist. No record enters without its buying mechanism stated |
| [`experiments/`](experiments/) | Method conflicts queued as tests rather than settled by preference |
| [`decisions/`](decisions/) | Construction-level calls with their evidence, and the condition that would reverse each one |

## How it is built

**Mechanism separated from values.** Core states how a score composes, never what a dimension is
worth. Two accounts can score the same company differently and both be right, which is what makes
one engine serve many tenants without forking.

**A swap test that runs.** Every rule must read correctly for any account, or it is instance data
filed in the wrong place. Enforced by search rather than by convention.

**One home per fact.** A number written twice will disagree with itself within a month, so scoring
values, thresholds, and buyer facts each live in exactly one file and everything else points at it.

**Admission before entry.** Nothing joins the method library without a stated, categorised
justification. What cannot state one is reference, not standard.

**Suppression as a gate.** Opt-out ledgers are per-account and append-only, checked before every
batch. There is no send capability in this repository and there is not meant to be; the wall
between method and sending is a design decision.

**Composable, not a shelf.** A play activates through the account's signal library, routes to a
named skill, takes its numbers from that account's scoring model, and clears suppression before
anything sends. The connections are written down rather than held in someone's head.

## Scope

**Built and documented; operating history still ahead of it.** The method library, the account
stamp, and the doctrine layer are complete and routed. The first campaign has not run, which means
the feedback loop that rewrites scoring from results is designed rather than exercised.

**Reach is built out; capture is partial.** Four channel playbooks, fifteen signal plays, and
reply handling all ship. Landing pages and forms belong to a separate machine by design and are
not here.

**The market-mapping pipeline runs stages 1 and 2 of 6.** Folders are created as content is
briefed rather than in advance, so the shape of the work is always visible.

**The runtime is specified, not wired.** [`runtime-spec.md`](runtime-spec.md) describes the kit
executing motions against a live tool estate. It waits on account credentials and a datastore,
neither of which belongs in a public repository.

## Rules of the road

Name the account before anything loads · core never names an account · every number lives in the
account · one home per fact · suppression before every send · load the one file the task names,
never a whole folder. Full text: [`foundations/principles.md`](foundations/principles.md).

## Provenance

[`NOTICE.md`](NOTICE.md) records every inherited element: what came from where, under what licence,
and what was checked when. [`decisions/`](decisions/) carries the reasoning behind construction
calls, including the ones that were later revised. Licence: [MIT](LICENSE), covering this
repository's own work.
