# Estate — what this kit is, owns, and reads

The context map, seeded small. Subject: where this machinery sits in the operator's
estate, what it owns, and what it deliberately does not. Grows only when a sibling
machine becomes real.

## What this kit is

Connective machinery for **revenue engineering**. GTM motions are not the heart of a
business OS — they are the tissue that prevents waste between what a business offers and
who needs it: signal → offer → conversation → won work, with nothing leaking between.
The kit owns the motions; the things the motions connect live in their own machines.

This rendering is grounded, not asserted: `foundations/revenue-engineering.md` holds the
definition (revenue engineering owns the system; GTM engineering is its execution layer —
this kit), the eight laws, and the waste taxonomy the tissue metaphor names. The kit
keeps its name and scope on that file's subsume verdict. Why one repo holds both the
architecture layer and the execution layer — the seat no mainstream system serves — is
that file's §The thesis, sharpened.

## Owns / reads

| | What | Home |
|---|---|---|
| **Owns** | motion method (skills, plays, channels, workflows, the TAM pipeline) | `motions/` |
| **Owns** | the signal record schema and admitted signal records | `signals/` |
| **Owns** | the experiment protocol and open tests | `experiments/` |
| **Owns** | the account stamp and the rules (`foundations/`) | `accounts/_template/` |
| **Reads (future siblings)** | offers / SKUs — what is actually sold | not built; squats today in `accounts/<slug>/brand/offer-map` |
| **Reads (future siblings)** | funnel machinery — where conversations convert | not built (ClickFunnels connector exists, unwired) |
| **Reads (future siblings)** | brand voice + copywriting system | not built; squats today in `accounts/<slug>/brand/` + `tools/lint_copy.py` |

**The squatting is declared, not resolved:** brand voice, the offer map, and the copy
linter live in this kit today because nowhere better exists. When the sibling machines
are built, those move out and the kit reads them — an estate-level application of
one-home-per-fact. Until then they stay, and nothing new of that kind is added here.

## Deployments — which copy holds what

Core is copied identically into every deployment; an account lives in exactly one
(principle 6). This table is the map; `accounts/_index.md` is the per-account catalog.

| Copy | Core | Accounts | State |
|---|---|---|---|
| `gtm-kit-pro` (this repo, upstream) | **authoritative** | `_template/` only | under reconstruction (this branch) |
| `fenton-bookkeeping-os/machinery/gtm-kit/` | vendored | `fenton` | **shelved 2026-08-13** — re-vendors core on resume |
| `albatross-engineering-os/machinery/gtm-kit/` | vendored — re-vendored 2026-08-14 from `main` @ `ece884f` | `revenue-engineering` | active front; first operated run on record |

**Plan of record (operator ruling, 08-13):** the active front is the albatross
deployment's **own motion** — its `revenue-engineering` account, where experiments 001
and 002 run when its first campaigns launch. **Client 0 is the operation itself
[operator, 08-14]** — GTM motions are both a service and a business function, and that
account is where the machinery is proven before any client sees it. **The Fenton engagement is dropped for
now**: Albatross sells products, not GTM services (the recorded 08-10 pivot); the
fenton-as-first-client dry run is not built toward, and the service-model question stays
parked with it. Fenton runs its own GTM in its own OS, on its own resume schedule.

## Runtime direction — confirmed; spec drafted **[operator, 08-13/14]**

> **The spec exists:** `runtime-spec.md` (v0, 08-14) — the ICM structure as the runtime
> program, execution blocks in the stage contracts, the laws translated into two
> mechanical gates (consent and cost), TAM stages 1–3 as the first executable motion. The
> public skills pack is triaged (`decisions/2026-08-14-deepline-skills-triage.md`).
> **Wiring waits only on the operator's inputs** — the API account and providers, the
> datastore per deployment, the send-approval scope. The section below is the standing
> doctrine the spec implements.

**The kit will exist as a runtime** — not markdown instructing a session which
individually-wired tool to call, but a running system executing motions against the live
tool estate. The primary integration surface is **Deepline** (verified 08-13): a unified
GTM API, 86+ integrations under one bill, agent-native, covering enrichment, CRM writes,
sequencers (Instantly among them), waterfall enrichment, validation, and scoring — basic
tools are reached *through* the runtime, so "primarily Deepline" retires no channel.

What this changes, and what it must not:

- **The send wall translates; it does not retire.** "No live `.mcp.json`" was the
  markdown-era form of a runtime-era rule: sends execute only through gates that bind
  mechanically — suppression checked in the runtime before every batch, caps enforced in
  the runtime, approval scopes per account. A runtime without mechanical gates is the
  send wall torn down, not upgraded.
- **Values still live in the account** (principle 3) and **suppression stays per-account,
  append-only** (principle 5) — runtime requirements now, not just file conventions.
- **Do not scaffold wiring ahead of the operator's material.** The spec is written; the
  inputs are not in hand, and a spec is not a reason to start wiring.

## The second brain — retired from the loop, 2026-08-14

A Claude Cowork workspace held the operation's calibration record: the laws, the chain of
operations, the operator's rulings, the failure log. **Its distillate now lives in
`foundations/`** — chain-of-operations, failure-modes, lexicon, and rulings, stripped of
the operator's business facts (which never travel: core travels to every deployment, an
account travels to none).

Evaluation, research, and triage moved to the construction session; the operator remains
the gate (`foundations/rulings.md` §Authority). `rulings.md` is the standing channel: it
is appended to as rulings land, and it outranks any inference a session makes.
