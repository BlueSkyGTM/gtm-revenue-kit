# GTM Kit Pro

**Machinery**: the multi-account GTM engine — one shared engine, many bounded accounts —
built to embed into a business-OS chassis's `machinery/` the way ledger servers do
(standalone repo upstream, vendored downstream). It powers a chassis's **funnel wing**
(prospects and initiatives) and feeds its **ABM/Won wing** (case files that become client
records). Form: **Umbrella** (root routes; shared factory) composed with a **Record
library** (`accounts/`).

**This file routes; it holds no content.** Every fact lives in exactly one home below.

## The one rule

**Every session names its account first.** Nothing loads until it is known — a skill run
without an account resolves nothing, and context loaded under the wrong account produces
confident answers from the wrong buyer's facts. If unclear, ask before anything else.

## Folder map

```
gtm-kit-pro/
├── CLAUDE.md · CONTEXT.md      ← this map · the task router
├── README.md · START-HERE.md   ← design document · buyer front door
├── DIVERGENCE.md · NOTICE.md   ← product spec vs upstream · attribution
│
│  ── CORE: the shared engine. Account-agnostic. Contracts in each folder. ──
├── skills/       what Claude executes (6 skills)        → skills/CONTEXT.md
├── workflows/    how a team operates (5 docs)           → workflows/CONTEXT.md
├── playbooks/    the method shelf: guides · plays/ ·    → playbooks/CONTEXT.md
│                 channels/ · dormant/ · REFERENCES.md (selection)
├── docs/         the rule shelf (6 rules, one home each)→ docs/CONTEXT.md
├── tools/        the copy linter                        → tools/CONTEXT.md
├── sync/         result-pull scripts                    → sync/CONTEXT.md
├── examples/     Relay, the read-only reference instance→ examples/CONTEXT.md
├── _archive/     superseded material, never load
│
│  ── RECORDS: the tenants. One folder per account, same shape. ──
└── accounts/                                            → accounts/CONTEXT.md
    ├── _index.md     the catalog — what accounts exist, tier, status
    ├── _template/    the stamp — a new account is a copy, never a blank page
    └── <slug>/       ACCOUNT.md + context/ + outputs/ + brand/ + optouts.md
```

## Routing

| You need | Read |
|---|---|
| "What's my task? → which file?" | `CONTEXT.md` |
| Which playbook fits this situation | `playbooks/REFERENCES.md` |
| The core/account boundary, the swap test | `docs/isolation.md` |
| What may load with what | `docs/loading.md` |
| Two methods disagree | `docs/lineages.md` — parallel, recorded, account chooses |
| Standards (PVP, gates, benchmarks) | `docs/standards.md` |
| Sending and the send-tool wall | `DIVERGENCE.md` E2 · the account's `ACCOUNT.md` §Sending |
| Operator vs engineer surface | `docs/tiers.md` |

## Hard lines (full text where cited)

- Core never names an account — the swap test decides (`docs/isolation.md`).
- Every number lives in the account's `context/scoring-model.md`, never core.
- No live `.mcp.json` in this repo, ever (`DIVERGENCE.md` E2).
- Suppression before every send, per account (`accounts/<slug>/optouts.md`).
