# Router — what's your task?

Start here when you know what you want to do but not which file holds it. The map is
`CLAUDE.md`; this is the index.

**First, name the account.** Every row below assumes one has been named. `<slug>` in a
path means the named account's folder under `accounts/`.

## By task

| Your task | Go here | Notes |
|---|---|---|
| Stand up a brand-new account | `skills/setup/SKILL.md` + copy `accounts/_template/` | Writes the six context files from public research |
| Research one account before outreach | `skills/account-research/SKILL.md` | Output: `accounts/<slug>/outputs/account-research/` |
| Score, tier, or re-score a list | `skills/icp-scoring/SKILL.md` | Mechanism only — every number lives in `accounts/<slug>/context/scoring-model.md` |
| Turn a signal into a campaign | `skills/signal-to-sequence/SKILL.md` | Output: `accounts/<slug>/outputs/campaigns/` |
| A reply or inbound application landed | `skills/reply-handling/SKILL.md` | Classify → route → qualify → discovery prep |
| Refresh stale context, log results | `skills/weekly-update/SKILL.md` | Run it Mondays; writes a dated weekly log |
| Who we sell to · how we position · what a signal means | `accounts/<slug>/context/` — the one file the task names | Never bulk-load this folder |
| A second buyer with different copy | `accounts/<slug>/context/tracks/<track>/` | Tracks are how one account runs two campaigns without blending them |
| Someone asked to be removed | `accounts/<slug>/optouts.md` | Append-only, permanent, legal. Never delete a row |
| Check copy against the account's rules | `tools/lint_copy.py` | Reads the account's own rules; a gate, not a review |
| How the team operates end to end | `workflows/` | Human process docs, not execution instructions |
| Build a list from the market down (no signal yet) | `workflows/tam-campaign.md` | The market-led complement to signal-led `campaign-build.md` |
| Enrichment and scraping technique patterns | `workflows/enrichment-techniques.md` | Extends `workflows/enrichment.md`; cost model, API patterns, four scraping patterns |
| Pick a play for a signal or a buyer moment | `playbooks/plays/README.md` | The signal-play library — 15 recipes; a play activates for an account by adding its signal to that account's `signal-library.md` |
| Choose or tune an outreach channel | `playbooks/channels/README.md` | Cold email · cold calls · LinkedIn ABM · micro-lists |
| A specific situation (signal fired, competitor switch, positioning build) | `playbooks/` | `playbooks/dormant/` holds methods no active motion uses yet |
| What may load with what | `docs/loading.md` | The two-rule-systems discipline |
| Why core may not name a company | `docs/isolation.md` | The swap test and the account boundary |
| Which surface a buyer sees | `docs/tiers.md` | Operator vs engineer |
| The standards work is held to | `docs/standards.md` | PVP, tier bands, campaign gates, benchmarks |
| What changed from upstream | `DIVERGENCE.md` | Also the product spec |

## By artifact

| You have | It belongs in |
|---|---|
| A research brief | `accounts/<slug>/outputs/account-research/YYYY-MM-DD-[name].md` |
| A campaign | `accounts/<slug>/outputs/campaigns/YYYY-MM-DD-[name]/` |
| A scored list | `accounts/<slug>/outputs/YYYY-MM-DD-scoring-[name].md` |
| A durable fact about the buyer | the matching `accounts/<slug>/context/` file — never an output |
| A method that would work for any account | `playbooks/` or `skills/` — core, and strip every account fact first |
| Raw contact data, lists, exports | nowhere in git. Gitignored by pattern; keep it in the enrichment tool |

## The load discipline

`context/` is a **factory** — configured once, read one file at a time, every run.
`outputs/` is **product** — new every run, dated, never edited in place to mean something
else. Never bulk-load either. Reading an account's whole `outputs/` folder to answer one
question is how a session runs out of room and starts inventing.

Detail: `docs/loading.md`.
