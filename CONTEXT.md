# Router — what's your task?

Start here when you know what you want to do but not which file holds it. The map is
`CLAUDE.md`; this is the index. **First, name the account** — `<slug>` below means the
named account's folder inside its deployment (`estate.md` says which deployment).

## By task

| Your task | Go here | Notes |
|---|---|---|
| Stand up a brand-new account | `motions/skills/setup/SKILL.md` + copy `accounts/_template/` | Writes the context files from public research |
| Research one account before outreach | `motions/skills/account-research/SKILL.md` | Output: `accounts/<slug>/outputs/account-research/` |
| Score, tier, or re-score a list | `motions/skills/icp-scoring/SKILL.md` | Mechanism only — every number lives in `accounts/<slug>/context/scoring-model.md` |
| Turn a signal into a campaign | `motions/skills/signal-to-sequence/SKILL.md` | Output: `accounts/<slug>/outputs/campaigns/` |
| A reply or inbound landed | `motions/skills/reply-handling/SKILL.md` | Classify → route → qualify → discovery prep |
| Refresh stale context, log results | `motions/skills/weekly-update/SKILL.md` | Mondays; writes a dated weekly log |
| Build market-led (no signal yet) | `motions/tam/` | **Under construction** — its CONTEXT.md states what is real |
| Build signal-led (a signal fired) | `motions/workflows/campaign-build.md` | One campaign workflow per session, never both |
| Pick a play for a buyer moment | `motions/plays/README.md` | Michael's 15 — a play activates via the account's `signal-library.md` |
| Choose or tune a channel | `motions/channels/README.md` | Cold email · cold calls · LinkedIn ABM · micro-lists |
| A signal needs to exist | `signals/schema.md` | No "why it matters," no entry |
| Define segments by pain, not structure | `motions/workflows/pain-based-segmentation.md` | Competing instrument — declare which map drew the audience (`experiments/002`) |
| First-touch copy question | `foundations/pvp.md` | Two instruments, account's choice, never blended (`experiments/001`) |
| Two methods disagree | `experiments/` | Queue a test or cite the open one — doctrine is not curated here |
| Write or revise a skill/play/stage | `foundations/task-craft.md` | The six rules; the self-check is the last gate |
| About to draft or commit anything to core | `foundations/failure-modes.md` | The tells, and the six-step self-check |
| The method files don't cover your case | `foundations/conceptual-framework.md` | Derive the treatment: pillar → demand → guardrails → recorded rendering |
| Judge whether an output is good, not just rule-clean | `foundations/conceptual-framework.md` | Its pillar's criteria, then the seam test |
| A structural or design decision | `foundations/chain-of-operations.md` | Which rung, and which way authority flows |
| A term could mean two things | `foundations/lexicon.md` | Ask rather than pick |
| "Has this already been decided?" | `foundations/rulings.md` | Append-only; a ruling outranks an inference |
| Someone asked to be removed | `accounts/<slug>/optouts.md` | Append-only, permanent, legal |
| Check copy against account rules | `tools/lint_copy.py` | A gate, not a review |
| Which tool or provider for a step | `runtime-spec.md` §8 Tool selection | Four criteria, in order; both gates before spend or send |
| Why was X absorbed, replaced, or disregarded? | `decisions/` | Construction-level calls with their evidence; audits live here |
| Where does X live — this repo or a deployment? | `estate.md` | Core travels; an account lives in exactly one |

## By artifact

| You have | It belongs in |
|---|---|
| A research brief | `accounts/<slug>/outputs/account-research/YYYY-MM-DD-[name].md` |
| A campaign | `accounts/<slug>/outputs/campaigns/YYYY-MM-DD-[name]/` |
| A durable buyer fact | the matching `accounts/<slug>/context/` file — never an output |
| A method any account could use | `motions/` — with provenance stated, numbers stripped to the template |
| A signal with a known why | `signals/` — as a schema record |
| An unresolved method conflict | `experiments/` — as a queued test |
| Raw contact data, lists, exports | nowhere in git — gitignored by pattern |

## The load discipline

`foundations/principles.md` §Load discipline. Short version: name the account, load the
one file the task names, one campaign workflow per session, never bulk-load a folder.
