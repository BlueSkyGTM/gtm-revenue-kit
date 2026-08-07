# GTM Kit Pro

A multi-account go-to-market engine that runs out of hand-readable markdown. One shared
engine, many bounded accounts.

New here? Read **`START-HERE.md`**. Working in it? The map is **`CLAUDE.md`**, the router is
**`CONTEXT.md`**.

Built on [gtm-starter-kit](https://github.com/KarlRaf/gtm-starter-kit) (MIT) — see
`NOTICE.md` for attribution and `DIVERGENCE.md` for everything that changed and why.

---

## What's inside

```
gtm-kit-pro/
├── CLAUDE.md · CONTEXT.md · START-HERE.md      ← map · router · front door
├── DIVERGENCE.md · NOTICE.md                   ← what changed from upstream · attribution
│
├── skills/          six skills Claude executes from a one-line prompt
├── workflows/       how a team operates — human process docs
├── playbooks/       situation guides, plus dormant/ for unactivated methods
├── docs/            the rule shelf: isolation · loading · tiers · standards
├── tools/           the copy linter (reads each account's own rules)
├── sync/            pull campaign results back into an account
├── examples/        Relay — the upstream reference instance, read-only
│
└── accounts/        the tenants
    ├── _template/               the scaffold. Copy it; never work inside it.
    ├── fenton/                  account one — configured, operating
    └── revenue-engineering/     account two — scaffolded
```

**An account is a kit instance.** `accounts/<slug>/` has the shape the upstream kit's root
had: `ACCOUNT.md` where its `CLAUDE.md` was, the same context files, its own outputs. The
engine did not change — it stopped assuming there was only one of you.

## Status

| Area | State |
|---|---|
| Multi-account infrastructure — core/tenant split, isolation rules, tenant contract | 🟢 Built |
| Six skills, account-aware — setup · account-research · icp-scoring · signal-to-sequence · reply-handling · weekly-update | 🟢 Ported and gated |
| Values/mechanism split — core carries no numbers | 🟢 Enforced in `icp-scoring`; `scoring-model.md` is the account's authority |
| Playbooks — impact-positioning, deliverability, competitor-switch, new-signal-response, 5 dormant | 🟢 Ported, swap-test clean |
| Copy linter — reads rules from the account's `brand/voice.md` | 🟢 Generalized, stdlib only |
| Rule shelf — isolation · loading · tiers · standards | 🟢 Written |
| Account one (`fenton`) — context, two tracks, 59 markdown outputs | 🟢 Transferred |
| Account two (`revenue-engineering`) | 🟡 Scaffolded, context not yet written |
| **Branding lab** — the interview skill filling `accounts/<slug>/brand/` | 🔴 Next phase. Slots and contract exist; the skill does not |
| Tier enforcement | 🔴 Descriptive only — labels and routing, not access control |
| Send tool | ⛔ Deliberately unwired. `.mcp.json.example` only |

## Conventions

- **Name the account first.** Nothing loads until it is known.
- **Core never names an account.** The swap test decides: if a core sentence stops being
  true for a different account, it is account content in the wrong folder (`docs/isolation.md`).
- **Numbers live in the account.** Core holds mechanism; every value lives in that account's
  `context/scoring-model.md`. Two accounts may score the same company differently and both
  be right.
- **One home per fact.** Everything else points at it.
- **Factory and product never mix.** `context/` is configured once and read every run;
  `outputs/` is new every run and dated.
- **Outputs are evidence.** When one turns out wrong, annotate it in place. A run record
  edited to look correct is worse than one that was wrong.

## What never enters this repo

Contact data and lists · API keys and credentials · raw transcripts · a live `.mcp.json` ·
another account's facts.

## Working in it

```bash
# Lint an account's copy against its own rules
python tools/lint_copy.py --account <slug> <files>

# What changed from upstream, and why
cat DIVERGENCE.md
```

The pristine upstream state is at tag `baseline-gtm-starter-kit`; every commit after it is
this project's own work.
