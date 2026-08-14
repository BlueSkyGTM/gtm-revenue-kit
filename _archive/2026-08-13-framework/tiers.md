# Tiers — which surface a buyer gets

Two audiences buy this engine, and they need different amounts of it. The tiers are how
the same repo serves both without overwhelming one or starving the other.

**Status: descriptive, not enforced.** Tiers are labels and routing today — an engineer
tier file is not locked, it is simply not surfaced to an operator-tier buyer. Enforcement,
if it ever comes, is a packaging concern, not a code one.

## Operator tier

For the person running a business who wants the machine to work. They do not want to tune
a decay curve; they want to know who to contact and what to say.

| Gets | Where |
|---|---|
| Brand — voice, psychology, offers | `accounts/<slug>/brand/` |
| Case files — per-account research briefs | `accounts/<slug>/outputs/account-research/` |
| Campaigns — briefs, sequences, results | `accounts/<slug>/outputs/campaigns/` |
| Their own context files, in plain language | `accounts/<slug>/context/` |
| Situation playbooks | `playbooks/` (excluding `dormant/`) |
| Skills, run by prompt | `skills/` — invoked, not read |
| Suppression | `accounts/<slug>/optouts.md` |

What they never have to open: `scoring-model.md` internals, the signal decay tables, the
linter config, `docs/isolation.md`.

## Engineer tier

For the person building or operating the engine itself — the buyer who will tune it, or
run it on behalf of several accounts.

| Adds | Where |
|---|---|
| Scoring internals — dimensions, weights, bands, calibration | `accounts/<slug>/context/scoring-model.md` |
| Signal mechanics — detection, decay, combinations | `accounts/<slug>/context/signal-library.md` |
| Sequence architecture | `skills/signal-to-sequence/SKILL.md`, `workflows/campaign-build.md` |
| Linter configuration | `tools/lint_copy.py` + the account's rule block |
| Dormant playbooks — methods awaiting a motion | `playbooks/dormant/` |
| The multi-account rules themselves | `docs/isolation.md`, `docs/loading.md` |
| Sync scripts | `sync/` |

## The rule that keeps tiers honest

A tier is a **view**, never a fork. There is one engine; both tiers run the same skills
against the same account structure. The moment an operator-tier buyer gets a different
`icp-scoring` skill than an engineer-tier buyer, there are two products to maintain and
the cheaper one rots.

If an operator needs something from the engineer surface, they get it by asking for that
file, not by being sold a different repo.
