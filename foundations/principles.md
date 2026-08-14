# Principles — the rules that survived

Six rules, one page. Each earned its place in live operation or by the operator's explicit
decision; nothing here is inherited governance. Contracts cite these; they never restate them.

## 1. Known-why admission

**Nothing enters core unless we can say why it is here.** Three whys are accepted:

- **Course-reasoned** — it derives from Michael's coursework and the reasoning is known.
- **Operator-proven** — it was run in a live deployment and worked, on the record.
- **Upstream-verified** — it came from the original kit *and* the operator read it and
  endorsed the reasoning as their own.

Material that fails all three is reference, not law — it may sit in `_archive/` or in an
account, and it may not be cited as a standard. A signal with no backstory does not enter
the signal library (`signals/schema.md` enforces this as a required field). The sharp
edge of the test: a method entering core **names which waste it prevents**
(`foundations/revenue-engineering.md` §taxonomy).

**Arrival rule:** an import that contradicts standing method spawns an experiment
(`experiments/`) or an explicit operator decision — never a silent blend.

## 2. The swap test — and the account boundary

Core never names an account. Read any core sentence as if a different account were using
it: still true → core; needs an edit → account content in the wrong folder — move it,
don't generalize it into vagueness. Exceptions, all narrow: `examples/` (Relay, fictional,
read-only), `NOTICE.md` and `estate.md` (provenance and topology are their subject), and
the `Runs in` field of an `experiments/` record (a test must name where it runs).

The boundary runs both ways: **accounts never read each other.** When something learned
in one account should apply everywhere, promote the pattern into core stripped of its
facts, and leave the facts where they were. A pattern that cannot survive being stripped
of its facts was never a pattern.

## 3. Values live in the account

Core says *how* a score composes, never what a dimension is worth. Every point value,
weight, band boundary, decay multiplier, and gate number lives in the account's
`context/scoring-model.md`. Two accounts may score the same company differently and both
be right. A core default is a starting value, labeled as such, never an authority.

## 4. One home per fact

A fact appears in exactly one file; everything else points. A number written twice will
disagree with itself within a month, and the session that finds the disagreement cannot
tell which copy is stale.

## 5. Suppression is per-account, append-only

Each account's `optouts.md` governs that account's sends and nothing else — never merged,
never checked against another account's campaign. Consent withdrawn toward one sender does
not transfer. Append-only, forever.

## 6. Core travels; an account does not

Core is copied identically into every deployment; an account lives in exactly one
(`estate.md` holds the map). Method improvements land upstream first, then re-vendor — a
fix made only in a vendored copy dies at the next re-vendor. Git history is provenance,
not a location: never answer a live question from a removed folder's history.

## Load discipline

The account is named before anything loads. `context/` is factory — configured once, read
one file at a time; `outputs/` is product — new every run, dated, never rewritten to mean
something else. Load the one file the task names; bulk-loading a folder is how a session
runs out of room and starts inventing. One campaign workflow per session — signal-led or
market-led, never both. **Never co-load rival rule systems**: copy discipline and scoring
discipline in one session produce nonsense in both directions, and the same holds for any
two rule sets that judge each other's outputs. **A host system's delivery rules never
load into a motion session.** What each of these failures looks like from inside:
`failure-modes.md` §5.
