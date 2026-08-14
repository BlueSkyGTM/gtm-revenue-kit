# Isolation — the account boundary

The rule that makes this repo multi-account instead of one company's repo with folders.

## 1. Core never names an account

Core is `skills/`, `workflows/`, `playbooks/`, `docs/`, `tools/`, `sync/`, and the root
files. No file there may contain a company name, a customer's industry, a product's SKU,
a price, a persona's real title, or a numeric threshold tuned to one buyer.

**The swap test.** Read any core sentence as if a different account were using it. If it
is still true, it is core. If it needs an edit, it is account content sitting in the wrong
folder — move it to `accounts/<slug>/`, do not generalize it into vagueness.

Two exceptions, both narrow:
- `examples/` holds Relay, the upstream reference instance. It names a fictional company
  on purpose, and it is read-only.
- Provenance and topology files — `DIVERGENCE.md`, `NOTICE.md`, `docs/deployments.md`,
  `accounts/_index.md`, and `README.md`'s provenance sections — name real repos and
  accounts because *which copy holds what* is their subject. Permitted there and nowhere
  else; never as an example inside a method (`docs/deployments.md` §6).

## 2. Numbers live in the account, mechanism lives in core

The most load-bearing consequence of rule 1, and the thing that makes the engine
genuinely multi-tenant.

A core skill says *how* a score is composed — which dimensions exist, how they combine,
what a tier band means procedurally. It never says what a dimension is worth. Every point
value, weight, threshold, band boundary, and decay multiplier lives in
`accounts/<slug>/context/scoring-model.md`.

Consequence worth stating plainly: **two accounts may score the same company differently
and both be right.** That is the design, not a bug. It is also why a core skill can never
be "fixed" by tuning a number — if a number is wrong, it is wrong in one account.

## 3. Accounts never read each other

No file under `accounts/<a>/` may reference a path under `accounts/<b>/`. Not for
examples, not for "see how they did it," not for shared lists.

When something learned in one account should apply everywhere, **promote the pattern into
core** — the method, stripped of every fact — and leave the fact where it was. A pattern
that cannot survive being stripped of its facts was never a pattern.

## 4. Suppression is per-account

Each account's `optouts.md` governs that account's sends and nothing else. One account's
opt-out list is never checked against another's campaign, and never merged.

This is a legal boundary, not an organizational one: consent given (or withdrawn) toward
one sender does not transfer to another. An account that sends on behalf of a client
declares that client's roster in its `ACCOUNT.md`; that roster is also account-scoped.

## 5. One home per fact

A fact appears in exactly one file. Other files point at it; they do not restate it. A
number that appears twice will disagree with itself within a month, and the session that
finds the disagreement cannot tell which copy is stale.

When a fact must be visible in two places, the second place gets a pointer with the path,
never a copy of the value.

## 6. The same line, one repo up

This file governs the boundary inside a copy of the kit. `docs/deployments.md` governs it
across copies: core travels to every deployment, an account travels to none, and upstream
decides when copies disagree. Read it when a fact seems to live in more than one repo.

## Checking compliance

Before committing core changes:

```bash
# Core must not name accounts or deployments. Add each real slug to the pattern.
# The §1 exceptions are excluded by name, not by leaving folders unscanned.
grep -riE "fenton|albatross|revenue-engineering|<other-account-slugs>" \
    skills/ workflows/ playbooks/ tools/ sync/ examples/ docs/ accounts/_template/ *.md \
  | grep -vE "^(docs/deployments\.md|DIVERGENCE\.md|NOTICE\.md|README\.md):" \
  | grep -v '<other-account-slugs>'   # drops this command quoting itself

# No path may escape the repo, and no account may reference another.
grep -rn "\.\./\.\./\.\." . --include="*.md" | grep -v '^./.git'
```

Both should return nothing. When a new slug becomes real, add it to the pattern — and
resist the easier fix of dropping a folder from the scan, which turns the check green
without making it true. The excluded files are reviewed by eye
(`docs/deployments.md` §Checking compliance).
