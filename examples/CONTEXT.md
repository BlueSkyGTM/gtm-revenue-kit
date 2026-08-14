# examples/ — the reference instance contract

`sample-company/` is Relay, a fictional workflow-automation company inherited from the
upstream kit with every file populated: the six context files, personas, a research brief,
a full campaign with sequences and results, and a weekly log.

## What it is for

- **The picture of "done."** When filling an account's context files, Relay shows what a
  mature, data-backed version looks like — especially its signal library, which carries
  detection methods, decay logic, and performance tracking.
- **The one company core may name.** The swap test (`foundations/principles.md`) bans real names
  from core; Relay is the deliberate, fictional exception every example can lean on.
- **A smoke-test fixture.** New or changed core skills can be exercised against Relay
  without touching a real account.

## Rules

- **Read-only.** Nothing here is edited in normal operation. If the engine's shape changes
  (as it did when accounts/ was introduced), Relay is updated deliberately, as product
  work, to stay a faithful reference — never incidentally.
- **Relay is not an account.** It lives outside `accounts/` on purpose: it has no index
  row, no lifecycle status, and no suppression obligations. Do not stamp accounts from it —
  `accounts/_template/` is the stamp; Relay is the worked illustration.
- Its internal `CLAUDE.md` is the upstream single-tenant entry file, kept as part of the
  illustration — it is an instance document, not a second map for this repo.

## Human check

If Relay's shape and `accounts/_template/`'s shape drift apart, the template is the truth
and Relay needs the deliberate update — file it as product work rather than editing in
passing.
