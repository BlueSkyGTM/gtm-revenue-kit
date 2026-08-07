# Divergence — what this repo changed from upstream, and why

Upstream: [gtm-starter-kit](https://github.com/KarlRaf/gtm-starter-kit) (MIT), preserved in
this repo's history at tag `baseline-gtm-starter-kit` (commit `735b256`). Attribution:
`NOTICE.md`.

**This file is the product spec.** Every row is a decision about what the commercial engine
is that the open-source kit is not. It is also the changelog a buyer is owed: the honest
account of what they are paying for beyond a free clone.

Second source, and the reason most of these rows exist: the same kit was vendored into a
live bookkeeping practice (`fenton-bookkeeping-os/workspaces/practice/`) and operated for
several weeks. Everything marked **ADOPT** or **RESTORE** below was proven there first.
Provenance for that path: `NOTICE.md` §2.

**Classification:** `ADOPT` — generic upgrade, moved into core · `ADAPT` — reworked while
porting · `DROP` — instance or host-specific, not in the product · `RESTORE` — upstream
feature the vendored copy lost, kept here.

---

## A. Architecture — the change everything else hangs on

| # | Change | Class | Why |
|---|---|---|---|
| A1 | **Single-tenant → multi-account.** Tenant surface (`CLAUDE.md`, `context/`, `outputs/`) moved to `accounts/<slug>/`; core (`skills/`, `workflows/`, `playbooks/`) shared at root | ADAPT | Upstream assumes one company per clone. A firm running GTM for several clients had to clone per client, forking the engine every time and losing every improvement across copies. |
| A2 | **`CLAUDE.md` → router.** Company facts left it entirely; it holds the map, the account-first rule, and the core/account line | ADAPT | It cannot hold one company's ICP when it serves several. |
| A3 | **`ACCOUNT.md` per tenant** — the file the kit's `CLAUDE.md` used to be, plus identity, tier, send config, suppression sources, account overlays | ADAPT | Preserves the kit's best property (one summary layer Claude reads first) at the tenant level. |
| A4 | **`docs/` rule shelf** — `isolation.md`, `loading.md`, `tiers.md`, `standards.md` | ADOPT | Upstream carries these rules as prose scattered through the README. Multi-account makes them load-bearing, so each gets one home. |
| A5 | **The swap test** as the governing rule for core (`docs/isolation.md`) | ADOPT | Came from the vendored copy, where files were self-labeled "passes the swap test" by hand. Promoted from a habit to the rule that defines the core boundary. |
| A6 | **Suppression is per-account** and never merged | ADAPT | Consent toward one sender does not transfer to another. In a single-tenant kit this cannot even be expressed. |

**The property A1 protects:** an account is still exactly a kit instance. Nothing about the
engine's shape changed — it just stopped assuming there was one of you. Anyone who knows
the upstream kit can read this repo without relearning it.

## B. Core upgrades — proven in the vendored copy, promoted here

| # | Change | Class | Why |
|---|---|---|---|
| B1 | **Values/mechanism split.** Core skills hold mechanism and zero numbers; every point value, weight, band, and decay multiplier lives in the account's `context/scoring-model.md` | ADOPT | The single most important upgrade for a multi-tenant engine: it is what lets one `icp-scoring` skill serve accounts that score the same company differently and are both right. Upstream mixes values into the skill file. |
| B2 | **`## Inputs` block on every skill** — each names exactly the files it reads | ADOPT | Without it, a session bulk-loads `context/` and burns its window on files it will not use. Costs nothing; prevents the most common failure. |
| B3 | **`reply-handling` skill** — classify → route → qualify → discovery prep | ADOPT | Upstream stops at send. The reply is where a campaign becomes pipeline, and it was the one unproceduralized seam in the vendored copy until it was written. |
| B4 | **`impact-positioning` playbook** — six-step positioning construction plus a step-7 audit | ADOPT | Upstream has no method for building positioning for a *new* buyer, only a file to fill in. |
| B5 | **`deliverability-and-warmup` playbook** | ADOPT | Sending infrastructure is assumed by upstream and is the most common reason a good campaign produces no replies. |
| B6 | **`playbooks/dormant/`** — account planning, buyer-group mapping, champion enablement, demo scripting, mutual action plans | ADOPT | Methods with no active motion yet. Shelved deliberately rather than deleted, with a README saying so, so they are found when a motion needs them instead of rebuilt. |
| B7 | **Copy linter** (`tools/lint_copy.py`), generalized to read each account's rules from `brand/voice.md` | ADAPT | The vendored copy hardcoded one firm's rules. Mechanical enforcement of copy rules is a gate, not a review — but only if the rules are the account's own. |
| B8 | **Suppression ledger pattern** (`accounts/<slug>/optouts.md`) — append-only, standing suppressions, scope column | ADOPT | Upstream says "don't commit contact data" and stops. Opt-outs are a legal obligation and need a durable, auditable home. |
| B9 | **`context/tracks/<slug>/`** — first-class multi-buyer support | ADAPT | The vendored copy grew a second buyer and expressed it as filename suffixes (`icp-definition-white-label.md`, four files deep). That convention does not scale past two and gives no rule against loading both at once. Tracks make the boundary structural. |
| B10 | **`brand/` slots** — voice, brand psychology, offer map | ADOPT | New surface, filled by the branding lab skill (next phase). The layer an operator feels immediately, and the one the linter enforces. |
| B11 | **Reachability state** before a score is trusted (`scoring-model.md` §7) | ADOPT | Evidence from the vendored copy: 3 of one campaign's top 20 highest-scored accounts were unusable (dead domain, rebrand, brand-new business) — 15% failure at the head of the list, where the most expensive effort goes. |

## C. Restored from upstream

| # | Change | Class | Why |
|---|---|---|---|
| C1 | **`weekly-update` skill** | RESTORE | Dropped during the vendoring into the bookkeeping repo, which left the context files with no maintenance loop and no run record. The product ships the full six skills. |
| C2 | **`sync/` scripts** | RESTORE | Also dropped in the vendored copy. They belong after a send, feeding results back into scoring — the loop that makes the weights more than a guess. |
| C3 | **`examples/sample-company/` (Relay)** | RESTORE | Kept verbatim and read-only. It is the only company core may name, and the reference for what a fully populated account looks like. |

## D. Dropped — instance or host-specific, not in the product

| # | What | Where it went |
|---|---|---|
| D1 | All operating outputs — research briefs, campaigns, audits, sequences, metrics | `accounts/fenton/outputs/` — they are account content, not product |
| D2 | Raw lead data — CSVs, enrichment exports, send lists | Nowhere in git. Gitignored by pattern in both repos. |
| D3 | The website, WordPress theme, page mirrors, brand images | Stays in the host repo. A GTM engine does not ship someone's site. |
| D4 | Firm operations — pipeline tracker, revenue forecast, fee allocation workbooks | Stays in the host repo. Money engine, not GTM engine. |
| D5 | Business-development folder — outreach staging, case studies | Stays in the host repo; the reusable part (the opt-out ledger) was promoted (B8). |
| D6 | Pricing strategy content | Stays in the host repo. Upstream is explicit: commercial terms stay out of the repo. |
| D7 | Host-coupled offer triggers (`won-lead`, `pipeline-gap`, `handoff-fields-blank`) | Stay in the host repo — they read its client folders and workbooks. Only `optout-reply` was portable. |
| D8 | Instance overlay blocks inside two skills (`account-research`, `reply-handling`) | Relocated to `accounts/fenton/ACCOUNT.md` as account overlays — exactly what their own "drop on a kit re-export" markers prescribed. |
| D9 | Live `.mcp.json` with a wired send tool | Never in this repo. `.mcp.json.example` only — see E2. |

## E. Product decisions

| # | Decision | Reasoning |
|---|---|---|
| E1 | **Tiers are views, never forks** (`docs/tiers.md`) | Operator and engineer buyers run the same skills against the same structure. Two skill sets means two products, and the cheaper one rots. |
| E2 | **Send-tool wall.** No live `.mcp.json`, ever; `.mcp.json.example` only, gitignored real config | The API key that wires the send tool is set machine-wide on the author's machine. A committed wiring would hand every session of this product repo a live, authenticated sender pointed at a real account. This is the hard wall between writing *about* a send tool and being able to *use* someone's. |
| E3 | **Accounts never read each other** (`docs/isolation.md` §3) | Cross-account learning travels by promoting the pattern into core, never by pointing at a neighbor's facts. A pattern that cannot survive being stripped of its facts was never a pattern. |
| E4 | **The account is named before anything loads** | Loading `context/` without knowing whose it is produces confident answers from the wrong buyer's facts, and nothing about the output looks wrong. |

## F. Upstream defects noted, not silently fixed

| # | Defect | Status |
|---|---|---|
| F1 | `sync/.env.example` is documented in the upstream README tree but absent from the repo — the `.env.*` gitignore rule excludes it | Recorded. Fix by adding the file and narrowing the ignore rule, or by removing it from the documented tree. Not yet done. |
| F2 | Upstream states MIT in its README but ships no `LICENSE` file, so there is no copyright line to reproduce | Recorded in `NOTICE.md`. Confirm the intended holder with the upstream author before commercial distribution. |

## G. Open items

| # | Item |
|---|---|
| G1 | **Branding lab** — `skills/branding-lab/` filling `accounts/<slug>/brand/`. Next phase, deliberately after this infrastructure. |
| G2 | **Account two** (`accounts/revenue-engineering/`) is scaffolded, not configured. Fill it by running `skills/setup`. |
| G3 | **Opt-out authority.** The host repo's ledger remains the live one until the host migration completes. Recorded in `accounts/fenton/ACCOUNT.md` so the two cannot silently fork. |
| G4 | **Tier enforcement** is descriptive today — labels and routing, not access control. |
