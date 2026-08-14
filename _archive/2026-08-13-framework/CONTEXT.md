# docs/ — the rule shelf contract

One rule, one home, loaded on demand. Nothing here loads automatically; a session reads the
one rule file its situation cites. These files are **factory** — stable across every account
and every run — and they outrank any skill, playbook, or workflow that disagrees with them.

## The shelf

| File | The rule it owns | Load when |
|---|---|---|
| `isolation.md` | The core/account boundary: the swap test, values-in-the-account, accounts never read each other, per-account suppression, one home per fact | Editing core, moving facts, or any cross-account question |
| `loading.md` | What loads with what: the account gate, factory vs product, never co-load two tracks or two campaign workflows | Session start confusion, or before bulk-reading anything |
| `standards.md` | The bar: PVP, tier effort, campaign gates, benchmarks, sequences, datable why-now, output naming | Building or judging outbound work |
| `lineages.md` | Parallel method traditions: the three tags, the conflict register (C1–C4), resolution protocol | Two methods disagree, or any import lands |
| `tiers.md` | Operator vs engineer surfaces — views, never forks | Packaging or buyer-surface questions |
| `deployments.md` | The boundary across repos: core travels to every deployment, an account to none; the lookup map; upstream-decides | Something cannot be found, or a vendored copy is about to be edited |
| `CONTEXT.md` | This contract | — |

## Rules about the rules

- **A rule lives here or it is not a rule.** Skills and playbooks cite; they never restate.
  If a number or doctrine appears in two places, this shelf is the home and the other place
  becomes a pointer.
- **Additions need a vacancy.** A new file joins only when a rule has no home — check
  `lineages.md` (doctrine disputes) and `standards.md` (quality bars) before creating one.
- **Resolutions are dated.** Changing a rule that a lineage conflict touches goes through
  `lineages.md` rule 2 first.

## Human check

If a session quotes a rule from memory instead of citing a file here, verify against the
file — the shelf is authoritative, memory is not.
