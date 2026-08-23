# motions/playbooks/ — the situation library contract

Four step-by-step procedures for situations that recur across accounts and do not belong to
any one play or channel. A play answers *when to act*; a channel answers *how a medium
works*; a playbook answers *what to do in this situation, in order*.

| File | Carries | Provenance |
|---|---|---|
| `new-signal-response.md` | Detection to first touch, step by step, when any signal fires | Upstream |
| `competitor-switch.md` | Accounts on a competitor: evaluating, unhappy, or at renewal | Upstream |
| `deliverability-and-warmup.md` | Standing up sending infrastructure without risking the domain | Operator |
| `impact-positioning.md` | Six construction steps from "we should sell to them" to a complete positioning set | Operator |

## What they read and what they touch

Every one reads the account's `context/` before it runs, and none of them holds a number:
thresholds, volumes and tier bands live in the account's `scoring-model.md`
(`foundations/principles.md` §3). `new-signal-response.md` reads the account's
`signal-library.md` and routes into a skill; `impact-positioning.md` writes into the
account's positioning files; `deliverability-and-warmup.md` touches sending infrastructure
only, never a list.

## The boundary

A playbook is a procedure, not an authority. It never overrides the suppression ledger, the
account's copy instrument, or send approval. Where one would send, the account's `optouts.md`
gate runs first (§5), and that ordering is not the playbook's to change.

## Adding one

A fifth playbook enters the way anything enters core: a stated, categorised why
(`foundations/principles.md` §1), the swap test passed, no figures, and provenance in its
header. If the situation belongs to a single signal it is a play; if it belongs to a single
medium it is a channel guide. A playbook is what is left.
