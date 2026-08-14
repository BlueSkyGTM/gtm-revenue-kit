# Opt-out ledger — [Account name]

**Append-only. Permanent. Never delete a row.** A removed row is a person who asked not to
be contacted and then was.

Checked before every send batch for this account, alongside any client roster declared in
`ACCOUNT.md`. Scoped to this account only — see `foundations/principles.md` §4.

## How a row gets here

1. A reply asks to be removed, in any wording — "unsubscribe," "take me off," "not
   interested, stop," or a bare "no."
2. The row is appended below **before** the next batch goes out.
3. The address and the domain are both recorded. One person asking usually means the
   company asked.

Ambiguous cases resolve toward suppression. "Not right now" is not an opt-out, but it is
not a reason to keep sending the same sequence either — route it, do not re-send it.

## Ledger

| Date | Address | Domain | Source | Scope |
|---|---|---|---|---|
| | | | | |

**Scope values:** `address` — this person only · `domain` — everyone at the company ·
`list` — remove from a named campaign but not permanently

## Standing suppressions

*Categories suppressed by rule rather than by request. One row each, with the reason.*

| Suppression | Source of truth | Reason |
|---|---|---|
| Existing clients of this account | [where the roster lives — names and domains only] | Never cold-pitch someone already paying |
| [ ] | [ ] | [ ] |
