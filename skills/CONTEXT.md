# skills/ — the execution contract

What Claude executes from a one-line prompt. Each skill is a folder holding one `SKILL.md`
that is its own full contract (inputs, steps, output format, quality checks). This file is
the shelf-level contract: what is common to all six.

## The six

| Skill | One line | Writes to |
|---|---|---|
| `setup` | Stand up a new account from a domain (Step 0 stamps the folder) | `accounts/<slug>/` (whole tenant) |
| `account-research` | One company → a research brief ending in The Angle | `outputs/account-research/` |
| `icp-scoring` | Score and tier a list — mechanism only, values from the account | `outputs/` scoring files |
| `signal-to-sequence` | A signal → segments → sequence → copy | `outputs/campaigns/` |
| `reply-handling` | A reply → classify → route → qualify → discovery prep | campaign `results.md`, pipeline row |
| `weekly-update` | Diff stale context, log results, draft updates | the account's `context/` + weekly log |

All output paths resolve inside the named account.

## Common contract (every skill carries it inline)

- **The account gate:** the account is named before anything loads; a skill asks rather
  than guesses.
- **Inputs discipline:** each `SKILL.md` has an `## Inputs` block naming exactly the files
  it reads — never bulk-load `context/` or `outputs/` (`docs/loading.md`).
- **Values live in the account:** every number a skill needs comes from
  `accounts/<slug>/context/scoring-model.md` (`docs/isolation.md` §2).
- **Offered effects wait for a yes:** a skill drafts freely; anything with an external or
  permanent effect (a send, a permanent ledger row, a calendar hold) is offered first.

## Human checks

- A skill's output is an edit surface: the human reads and may edit the brief, the scored
  table, or the sequence before anything downstream consumes it.
- If a skill's `SKILL.md` and a rule file disagree, the rule file wins and the skill file
  gets fixed — contracts follow rules, not the reverse.
