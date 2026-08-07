# Play: Champion Job Change

People who loved the product carry it with them. When a past champion — someone who used,
chose, or advocated for the offering at a previous employer — moves to a new company that
fits the ICP, they arrive with budget influence, a mandate to show early impact, and a
pre-formed opinion in your favor. The play watches a curated list of real relationships for
job changes and routes each one, at the moment it happens, to the specific person who holds
the relationship. It reaches the warmest audience outbound can construct: buyers who already
believe.

---

## The signal

**What fires:** a person on the champion watchlist starts a role at a new company, and that
company matches the account's ICP. Both halves are required — a move to a non-fit company is
logged, not actioned.

**Where it comes from:** profile monitoring against a deliberately curated list. The list is
built by hand: for each existing or former customer, the few people who *actually* carried
the relationship — not every contact ever logged. Monitoring compares current role data
against the stored record on a scheduled cadence; the change detection runs in an enrichment
orchestrator (Clay or a Claude-based pipeline — mechanically one of the simpler builds in
this library).

**Decay:** the window is the new-role honeymoon — the early period when the mover is
assembling their toolkit and vendor slate, before habits and budgets set. The account's
`signal-library.md` records this as an **Organizational** signal, weekly-to-monthly refresh,
Tier 1 treatment; the recency window and point value live in the account's
`context/scoring-model.md`.

---

## Why it works

New leaders import their trusted stack. It is one of the most reliable patterns in
relationship-driven B2B: the executive who valued a vendor brings that vendor into the new
role, because proven tools reduce their personal risk during the period they most need
early wins. In relationship-heavy industries this single pattern accounts for a major share
of new business, and the same mechanism drives expansion in high-ticket product markets.

The play's real leverage is *routing*, not detection. The value is not "someone moved" — it
is "the person who knows them gets told while the window is open." A warm signal delivered
to a stranger becomes a cold call with a memory attached; delivered to the relationship
holder, it becomes a natural congratulation between people who already trust each other.

The limits: the pattern holds only where a genuine relationship existed — a champion who was
merely a logged contact confers nothing; the mover may not champion you at a company whose
context is different (their new stack, team, or constraints may not fit); and job-change
data lags reality, sometimes by weeks.

---

## The build

1. **Curate the watchlist by hand.** Customer by customer, name the handful of people with
   a real relationship to the account — chosen by the humans who hold those relationships,
   not exported by filter. Record each person alongside *who owns the relationship*. The
   watchlist lives in the account's context; its size stays small on purpose.
2. **Monitor on a cadence.** The pipeline checks each watchlist member's current employer
   and role against the stored values — weekly or monthly, per the account's
   `scoring-model.md`. A mismatch, or a role started within the freshness window, fires.
3. **Qualify the destination.** Score the new company against
   `accounts/<slug>/context/icp-definition.md` via `skills/icp-scoring/SKILL.md`. Fit
   proceeds; non-fit logs for the performance record.
4. **Suppress.** If the new company is already a customer or an open opportunity, route the
   alert to the owning seller as account intelligence instead of outreach. The account's
   `optouts.md` applies to the individual as always.
5. **Alert the relationship owner — a human, by name.** A notification (chat message or
   equivalent) to the specific seller mapped to that champion, carrying the who, the
   where, the when, and the relationship history. The activation is deliberately manual:
   this play forbids auto-sequencing its targets, because automation is precisely what
   would burn the warmth that makes it work.
6. **Log the outcome.** Reach-out made, conversation opened, pipeline created — into the
   account's `signal-library.md` performance log, so the watchlist earns its maintenance.

---

## The message frame

Written by the relationship owner in their own voice — the play supplies the moment, not
the words. The frame: congratulate genuinely, reference the shared history specifically
(the project, the result, the thing you actually did together), and offer something useful
for their new seat — a relevant observation about the company they just joined, an
introduction, a resource for their first-quarter problem. No pitch in the first touch: the
prior relationship makes the eventual commercial conversation inevitable if the reconnection
lands, and premature selling is the one way to lose it. Even here the PVP instinct from
`docs/standards.md` holds — the note should be worth receiving from someone they never buy
from. The new role is the datable "why now," and it is entirely natural to name.

---

## Measurement

- Watchlist coverage: share of customer accounts with named champions and owners
- Detection latency: days between actual role change and alert
- Action rate: share of qualified alerts where the relationship owner reached out inside
  the window — the number this play lives or dies on
- Conversion: alerts → conversations → pipeline, held against the account's other sources
  (this play should sit at the top of that comparison; if it does not, the "relationships"
  on the watchlist were not real)
- Volumes are watchlist-sized, so read rates with the same small-sample caution as
  `playbooks/plays/06-one-to-one-abm.md`; the campaign gates in `docs/standards.md` apply
  only if an account ever runs a sequenced variant

---

## When NOT to run it

- **A young customer base.** Too few genuine champions to watch; revisit after the account
  has accumulated real relationship history.
- **Transactional products.** Where customers feel nothing at renewal, movers carry nothing
  with them. The play needs a product people are proud to have chosen.
- **A watchlist built by export.** Auto-populating "champions" from every CRM contact
  produces a monitoring list of strangers and turns warm outreach into cold outreach with
  presumption added.
- **Automated first touches.** If the org cannot resist wiring alerts straight into a
  sequence tool, it should not build the detection. The manual activation is not an
  implementation detail; it is the play.
