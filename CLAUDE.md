# GTM Kit Pro

A multi-account GTM console. One shared engine, many bounded accounts.

**This file is the map — it routes, it does not hold account facts.** In the upstream
starter kit this file held one company's ICP, personas, and signals. Here it cannot: this
repo serves several. Every company fact lives in exactly one place —
`accounts/<slug>/` — and this file tells you which one to open.

## The one rule

**Every session names its account first.** Before any skill runs, the account is decided:
the operator says it, or you ask. A skill that runs without an account resolves nothing —
`context/` is ambiguous, `outputs/` has no home, and suppression cannot be checked. If the
account is not obvious from the request, ask before doing anything else.

## Folder map

```
gtm-kit-pro/
├── CLAUDE.md         ← you are here (the map, always loaded)
├── CONTEXT.md        ← the router: "what's your task? → go here"
├── DIVERGENCE.md     ← what this repo changed from upstream, and why
├── NOTICE.md         ← upstream attribution (MIT) and the two lineages
│
│  ── CORE: the engine. Account-agnostic, shared by every account. ──
├── skills/           ← what Claude executes: setup · account-research · icp-scoring
│                       · signal-to-sequence · reply-handling · weekly-update
├── workflows/        ← how a team operates: enrichment · signal-routing · campaign-build
├── playbooks/        ← situation guides; playbooks/dormant/ holds unactivated methods
├── docs/             ← the rule shelf: isolation, loading, tiers, standards
├── tools/            ← the copy linter and other account-agnostic scripts
├── sync/             ← scripts pulling live campaign data into an account
├── examples/         ← Relay, the upstream reference instance. Read-only.
│
│  ── ACCOUNTS: the tenants. Each is one instance of the engine. ──
└── accounts/
    ├── _index.md     ← the catalog: one line per account, slug + tier + status.
    │                   The declared source of truth for what accounts exist.
    ├── _template/    ← the tenant scaffold. Copy it; never work inside it.
    └── <slug>/       ← one folder per account, each the same shape.
```

**An account is a kit instance.** `accounts/<slug>/` has the shape the upstream kit's root
had — `ACCOUNT.md` where its `CLAUDE.md` was, the same `context/` files, its own
`outputs/`. Nothing about the engine changed; it just stopped assuming there was only one
of you.

## Core vs. account — the line that must not blur

| | Core | Account |
|---|---|---|
| Holds | mechanism, method, standards | facts, values, copy, results |
| Names a company? | **never** (except Relay, in `examples/`) | always — that is its job |
| Numbers? | none — no thresholds, no point values | all of them, in `context/scoring-model.md` |
| Changed by | product work | operating work |

**The swap test governs core.** Any core file must read correctly for a different account
with nothing edited. If a sentence stops being true when you swap the account, it is
account content in the wrong folder. Move it, do not soften it.

**Accounts never read each other.** No file in one account may reference another account's
path. Cross-account learning travels by promoting the *pattern* into core, never by
pointing at a neighbor's facts.

Full rules: `docs/isolation.md` · What to load and what never to co-load: `docs/loading.md`

## Working in an account

Every skill resolves its paths inside the named account:

```
accounts/<slug>/context/      ← the factory: configured once, read every run
accounts/<slug>/outputs/      ← the product: new every run, dated
accounts/<slug>/optouts.md    ← append-only suppression. Checked before every send.
accounts/<slug>/brand/        ← voice, psychology, offers (the branding lab fills these)
```

Invocation carries the account:

```
Read skills/account-research/SKILL.md and research [company.com] for account [slug]
```

## Sending

The send tool is **not wired in this repo**. `.mcp.json.example` shows the shape; each
operator wires their own `.mcp.json`, which is gitignored and never committed. A product
repo that ships a live send tool is a product repo that can mail from someone else's
account by accident.

**Suppression runs first, every batch** — the account's `optouts.md` plus any client
roster that account declares in its `ACCOUNT.md`. This is a legal obligation, not a
preference, and it is per-account: one account's opt-out never suppresses another's list,
and one account's list is never checked against another's.

## Tiers

**Operator tier** — brand, case files, campaign views, playbooks. **Engineer tier** —
scoring internals, signal mechanics, sequence architecture, linter config, dormant
playbooks. Which surface a buyer gets: `docs/tiers.md`.
