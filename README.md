# GTM Kit Pro

**Machinery** — the multi-account go-to-market engine, running out of hand-readable
markdown: one shared engine, many bounded accounts. In the four-point business-OS model
(trade wing · GTM Motions wing · ABM/Won wing · machinery), this repo is machinery for the
**GTM Motions** (Revenue & Growth) and **ABM/Won** (Clients & VIP) wings: the tools that enable trade, usable by whoever points
them at their own prospects, and built to embed into an OS chassis's `machinery/` folder
the way ledger servers embed into the bookkeeping OS.

This README is the repo's **design document**: the full promise of what the codebase offers,
what is already proven (with evidence), and the honest gap between the two. The gap section
is the backlog — when the codebase catches up to a promise, the item moves from Growth to
Achievements, and that movement is the completion metric.

New here? **`START-HERE.md`**. Working in it? The map is **`CLAUDE.md`**, the router is
**`CONTEXT.md`**. What accounts exist: **`accounts/_index.md`**.

---

## The problem and the position

GTM tooling either lives in SaaS (opaque, per-seat, your methodology trapped in someone
else's schema) or in documents nobody executes. This kit is the third option: the entire
engine — ICP definitions, signal libraries, scoring models, sequence construction, reply
handling, suppression — as folders an AI coding agent executes and a human can read, audit,
and own outright.

And it is **multi-tenant by architecture, not by copy-paste**: one engine, many accounts,
where an account is a client business, each bounded so strictly that one account's facts
cannot reach another's campaign. The operator who runs GTM for several businesses — the
agency case, the revenue-engineering case — works every account from one console without
the engine forking underneath them.

## Architecture

**Form** (per the ICM five-forms model): an **Umbrella composed with a Record library**.
The root is a map, not a sequence; the engine's skills, workflows, playbooks, and docs are
the shared factory; and `accounts/` is a record library — `_template/` is the stamp, every
account the same internal shape, `_index.md` the one-line-per-record catalog with a status
lifecycle (`scaffolded → configured → live → paused`). The umbrella is what makes the
architecture **asynchronous**: an agency of doors, each account active or dormant
independently, none blocking another.

```
gtm-kit-pro/
├── CLAUDE.md · CONTEXT.md · START-HERE.md      map · router · front door
├── DIVERGENCE.md · NOTICE.md                   what changed from upstream · attribution
│
├── skills/          six skills Claude executes from a one-line prompt
├── workflows/       how a team operates — human process docs
├── playbooks/       situation guides + dormant/ for methods awaiting a motion
├── docs/            the rule shelf: isolation · loading · tiers · standards
├── tools/           the copy linter (reads each account's own rules)
├── sync/            pull campaign results back into an account
├── examples/        Relay — the reference instance, read-only
│
└── accounts/        the record library
    ├── _index.md                the catalog — the source of truth for what exists
    ├── _template/               the stamp; a new account is a copy, never a blank page
    ├── fenton/                  account one — live (see its EXTRACTION.md for lineage)
    └── revenue-engineering/     account two — scaffolded
```

**An account is a kit instance.** `accounts/<slug>/` has the shape the upstream kit's root
had: `ACCOUNT.md` where its CLAUDE.md was, the same six context files, its own outputs,
plus what multi-tenancy required — `scoring-model.md` (every number), `optouts.md`
(suppression), `brand/` (voice slots), `context/tracks/` (multiple buyers without
blending). The engine did not change shape; it stopped assuming there was one of you.

Three rules carry the design (full text in `docs/isolation.md`):

1. **Core never names an account** — the swap test decides what may live in core.
2. **Numbers live in the account, mechanism lives in core** — two accounts may score the
   same company differently and both be right. This is the multi-tenancy enabler.
3. **Accounts never read each other** — learning crosses accounts only by promoting the
   pattern into core, stripped of its facts.

## Technical achievements

What is built and proven, with the evidence.

**Core-only upstream, proven by two live deployments (2026-08-10).** The factory/product
split completed its last step: every operating account moved into the business OS that
runs it (each OS vendors this kit and holds its own accounts and targets), and this repo
holds only the shared engine plus the `_template/` stamp. Two deployments consume it —
a bookkeeping practice's OS and the product company's own — which is the multi-account
architecture's claim demonstrated across repos, not just folders.

**The multi-account restructure, with history preserved.** The single-tenant upstream was
converted by moving the tenant surface (`CLAUDE.md`, `context/`, `outputs/`) into
`accounts/_template/` via `git mv` — the kit's file history survives intact under the new
paths, and the pristine upstream is tagged (`baseline-gtm-starter-kit`) so every divergence
is a reviewable diff.

**The account gate on all six skills.** Every skill opens with the same block: the account
is named before anything loads, paths resolve inside it, and a skill asks rather than
guesses — because context loaded under the wrong account produces confident answers from
the wrong buyer's facts, and nothing about the output looks wrong.

**The values/mechanism split.** `icp-scoring` was rewritten to hold mechanism and zero
numbers; every weight, point value, tier band, decay multiplier, and reachability rule lives
in the account's `context/scoring-model.md` with a calibration log. This is the single
change that makes one engine genuinely serve many accounts.

**Per-account suppression as a legal boundary.** Each account's `optouts.md` is append-only
with standing suppressions and a scope column, and ledgers are never merged — consent
withdrawn toward one sender does not transfer to another. The reply-handling skill routes
class-A replies to the ledger before anything else happens.

**Tracks instead of filename suffixes.** The vendored copy expressed a second buyer as four
`-white-label.md` files; the kit makes multi-buyer first-class (`context/tracks/<slug>/`)
with the one hard rule that matters (never load two tracks in one session) and a
channel-conflict clause for when two tracks could reach the same organization.

**The generalized copy linter.** `tools/lint_copy.py` reads each account's mechanical rules
from its own `brand/voice.md` (with defensible defaults), takes `--account`, and keeps
gate-grade exit codes: 0 pass, 1 violations, 2 config error. Proven catching em dashes and
banned vocabulary in test copy, and it stays stdlib-only.

**The send-tool wall.** No live `.mcp.json` exists or can be committed — `.mcp.json.example`
only, real config gitignored. The reasoning is recorded in `DIVERGENCE.md` E2: the send
tool's API key is set machine-wide on the author's machine, so a committed wiring would
hand every session of this repo a live, authenticated sender. The wall is what keeps
writing *about* the send tool separate from being able to *use* someone's.

**`DIVERGENCE.md` as product spec.** Every change from the upstream, classified
(ADOPT/ADAPT/DROP/RESTORE) with reasoning — simultaneously the changelog a buyer is owed
and the enumeration of what the commercial engine is that a free clone is not.

**Six skills, restored and extended.** The kit ships the upstream five plus
`reply-handling` — the seam where a campaign becomes pipeline, previously the one
unproceduralized moment: six reply classes, mechanical routing per class, a five-dimension
qualification rubric, and a four-question discovery spine. `weekly-update`, deleted in the
vendored copy, is restored so the context files have a maintenance loop again.

**A real account transferred with zero leakage.** Account one carries the operating history
of a real bookkeeping practice's GTM engine — nine context files, two full campaign tracks,
29 research briefs, three red-team audits, 59 markdown outputs — with zero CSVs, zero
contact data, zero credentials crossing, verified by sweep. Dated outputs were preserved
as evidence (annotated, never rewritten) per the records-are-evidence discipline.

**The playbook library — 21 method documents, built not imported.** Fifteen signal plays
(`playbooks/plays/`: renewal-window targeting, champion job-change, news-led outbound,
competitor-crisis response, inbound speed-to-lead, and eleven more), four channel playbooks
(`playbooks/channels/`), the market-led TAM campaign workflow, and an enrichment-techniques
reference — all method-abstracted from operator-curated source material into original,
swap-test-clean core documents. Every play states its signal, its mechanism, its honest
failure modes, and where the numbers live (the account's `scoring-model.md`, never core);
plays that are infrastructure or channel rather than event-signal say so instead of
dressing up. Verified by sweep: zero source-author traces, zero external links, zero
hardcoded values.

## Room for growth

The promise gap, ranked. Each item names what closes it.

0. **Segment-agnostic, pain-based signal support.** The doctrine landed
   (`workflows/pain-based-segmentation.md`, conflict C4 recorded): segments defined by an
   Existential Data Point, the signal dimension fed pain-based signals, firmographics
   demoted to messaging context. What remains is the tooling catching up — EDP-keyed
   signal templates in the `_template/` stamp and a worked pain-map example — so an
   account can adopt the doctrine by copying, not by authoring.

1. **The branding lab.** The slots and contract exist (`accounts/<slug>/brand/` — voice,
   brand psychology, offer map — with the linter already reading the voice file); the
   interview skill that fills them does not. This is the layman-facing layer of the
   product: what a $147 context-pack competitor ships as static files, done as a live
   interview to kit standards. Closes with `skills/branding-lab/SKILL.md` plus a worked
   Relay example.
2. **Playbook library depth.** The library landed (see Achievements) — the remaining gap is
   what the abstraction pass marked "needs operator input": the thin sections in
   one-to-one ABM's messaging and measurement, the video-only technique demos, and the
   per-ad-library scraping specifics. Each is flagged in place; closing them is operator
   experience flowing back into the documents, not more importing.
3. **The revenue-engineering deployment, configured.** The account is scaffolded in its
   own OS (see the accounts index — no operating account lives upstream anymore). Closes
   by running `skills/setup` there and its first campaign — which doubles as the product's
   first self-referential case study, since that account runs inside the engine it pushes.
4. **Sync scripts proven against live data.** `sync/` was restored from upstream but has
   never run against a real outbound tool's results. Closes with the first live campaign:
   results flow back into the account's signal-performance log and the scoring calibration
   loop stops being theoretical.
5. **Campaign-gate automation.** The gates are documented standards (audience ≥50,
   enrichment ≥80%, pause under 1% reply after 50 sends) enforced by discipline. Closes
   with a preflight script in `tools/` that reads a campaign brief and refuses the way the
   migration verifier refuses — problem, cause, fix.
6. **Account-level Offer Triggers.** The engine is reactive (skills run when invoked); the
   host-OS pattern of proactive offers (detect → offer → wait) has no home here yet.
   Closes with an Offer Triggers table in the account template plus a session-open scan
   convention.
7. **Tier enforcement beyond labels.** Operator/engineer tiers are documentation and
   routing today. If the kit is sold tiered, enforcement is packaging (what ships per SKU),
   not code — but the split needs a build script that can emit an operator-tier subset.
8. **The chassis embed.** This machinery's destination is a business-OS chassis's
   `machinery/` folder — the qb-server pattern: this repo stays the upstream, the chassis
   vendors it with a documented re-vendor loop. The operator's own OS chassis does not
   exist yet; `accounts/fenton/EXTRACTION.md` records the cross-repo contracts (Won
   handoff, suppression reads) the embed will formalize. Sibling machinery still to
   arrive in the estate: the operator's funnel tools and virtual-assistant tools.

## Conventions

- **Name the account first.** Nothing loads until it is known.
- **Core never names an account.** The swap test decides (`docs/isolation.md`).
- **Numbers live in the account.** Core holds mechanism only.
- **One home per fact.** Everything else points at it.
- **Factory and product never mix.** `context/` is configured once and read every run;
  `outputs/` is new every run and dated.
- **Outputs are evidence.** Annotate, never rewrite.
- **The index is the account authority.** `accounts/_index.md` — one line per account, and
  it never describes an account's internals.

## What never enters this repo

Contact data and lists · API keys and credentials · raw transcripts · a live `.mcp.json` ·
another account's facts.

## Provenance

Built on [gtm-starter-kit](https://github.com/KarlRaf/gtm-starter-kit) (MIT — attribution
in `NOTICE.md`), which is preserved verbatim at tag `baseline-gtm-starter-kit`. The
upstream project ended roughly five months before this repo was created and its working
assets are gone; this is a fork-and-diverge with no upstream to track, and everything after
the baseline tag is original work. The second lineage — the same kit vendored into a live
bookkeeping practice, operated for weeks, and transferred here as account one — is
documented in `NOTICE.md` §2 and `accounts/fenton/EXTRACTION.md`. Every divergence from
upstream, with reasoning: `DIVERGENCE.md`.
