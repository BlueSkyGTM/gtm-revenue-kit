# Channel Playbooks

Strategy per outbound channel. Each playbook answers the same three questions for its
channel: when does it pay, what runs it day to day, and which numbers govern it — with every
threshold living in the account (`context/scoring-model.md` or `ACCOUNT.md`), never here.

All four assume a list already exists: `motions/tam/skeleton.md` builds it,
`motions/workflows/enrichment.md` qualifies it, and suppression against the account's `optouts.md`
runs before any channel touches anyone.

| Playbook | Channel | Use when |
|---|---|---|
| [cold-email.md](cold-email.md) | Cold email at volume | The TAM is large; the work is yield-testing value propositions and running the inbox process that converts replies to pipeline |
| [cold-calls.md](cold-calls.md) | Cold calling | Deal size carries the cost of conversations — or email replies need same-day harvesting by phone |
| [linkedin-abm.md](linkedin-abm.md) | LinkedIn + ABM plays | The audience is precise and active on the platform; includes the recognition-asset and executive-network campaign architectures |
| [micro-lists.md](micro-lists.md) | Hand-sent 1:1 outreach | The TAM is small and deals are large; tiny sharp segments, deep research, real mailboxes |

The channels compose rather than compete: email finds hand-raisers, calls harvest them,
LinkedIn and micro-lists take the accounts too valuable to leave to volume. Which mix an
account runs is an account decision, recorded in its `ACCOUNT.md`.

Related: `motions/playbooks/deliverability-and-warmup.md` is upstream of any email send — no inbox,
no touch.
