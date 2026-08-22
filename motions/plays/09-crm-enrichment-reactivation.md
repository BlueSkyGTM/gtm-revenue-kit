---
type: play
provenance: michael-course
maturity: standard
---

# Play: CRM Enrichment and Reactivation

The CRM is a signal source pointed inward: it is full of people who already raised a hand
once, and it decays continuously — job changes, stale titles, dead emails, duplicate
accounts — until acting on it embarrasses the sender. The play establishes a standing
enrichment loop that keeps records true, and then mines the refreshed data for reactivation
moments: the dormant lead whose situation just changed into fit. It reaches an audience
cheaper than any net-new list, because acquisition already paid for it.

---

## The signal

**What fires:** two distinct events, one hygienic and one commercial.

1. **Record decay detected** — a contact's data no longer matches reality (changed job,
   bounced email, missing fields blocking automation). This fires workflow, not outreach.
2. **Refresh reveals fit** — re-enrichment shows a dormant record now matches the ICP in a
   way it did not at last touch: the company crossed a size band, adopted a relevant
   technology, entered a target industry, or the contact moved into a persona-matching
   role. This is the outreach signal.

**Where it comes from:** the CRM itself (HubSpot, Salesforce, or similar), synced with an
enrichment orchestrator such as Clay — either through a native integration or a plain
export-enrich-reimport loop. Job-change detection compares current profile data against the
stored record.

**Decay:** the underlying problem *is* decay — within a couple of years, a large fraction of
any B2B contact base has changed jobs. Fit-reveal events carry the standard recency window;
the account's `signal-library.md` records "dormant record regains fit" and "known contact
changed jobs" as **Firmographic / Organizational** rows with a scheduled refresh cadence,
weights in the account's `context/scoring-model.md`.

---

## Why it works

A dormant lead is not a dead lead — it is a person who once cared, filed under a snapshot of
who they used to be. When the snapshot is refreshed, some fraction of the base turns out to
have grown into the ICP, and outreach to them compounds two advantages: prior familiarity
(they have heard of you) and current fit (they now look like your buyers). That combination
reliably outperforms cold.

The hygiene half works by subtraction: every wrong field is a future failed automation, a
bounced send, a seller's wasted click, or a personalization error waiting to detonate. Clean
data does not create revenue directly; it stops the quiet leak of it — and it is what makes
segment-level automation (matching use cases or products to each record's industry, role,
and history) possible at all.

The limit: enrichment providers disagree with each other and with reality; a refresh loop
that overwrites human-verified truth with a vendor's guess makes records *worse*. Field-level
precedence rules — what may be auto-overwritten, what needs review — are the difference
between hygiene and vandalism. And consent ages: a hand raised years ago is not a standing
invitation; the reactivation touch must respect suppression and current law, checked against
the account's `optouts.md`.

---

## The build

1. **Agree the loop with the CRM owner.** Every sync is an input list and an output list —
   which objects, which fields, who resolves conflicts. The precedence rules (enriched
   value versus human-entered value, per field) are written down before the first run.
2. **One-time backfill.** Enrich the existing base: fill missing company data, contact
   channels, and the fit attributes the account scores on; merge duplicates (company
   domain is the usual join key); flag undeliverable emails.
3. **Standing refresh.** New records enrich on entry (the inbound play,
   `motions/plays/07-inbound-speed-to-lead.md`, handles the real-time path); the full
   base re-enriches on the cadence the account's `scoring-model.md` sets, with job-change
   detection on the contacts worth watching.
4. **Score the deltas.** Each refresh, diff against the prior state and run changed
   records through `motions/skills/icp-scoring/SKILL.md`. Band crossings from the account's
   `scoring-model.md` are the reactivation candidates; a known contact's job change may
   also route to `motions/plays/10-champion-job-change.md`.
5. **Suppress, then route.** Current customers, open opportunities, unsubscribes, and
   consent-expired records exit. Survivors enter a reactivation sequence via
   `motions/skills/signal-to-sequence/SKILL.md`, segmented by what changed — per the
   segment-by-signal discipline (the account's `scoring-model.md` §5).
6. **Feed marketing automation.** The refreshed attributes power segment-matched content —
   the right use case or product per industry, role, and history — for the records not yet
   warm enough for a seller.

---

## The message frame

Reactivation is a re-introduction, not a cold open and not a guilt trip ("you downloaded our
whitepaper in [year]" serves nobody). The frame: acknowledge the prior connection in at most
a clause, then lead with what is true *now* — the observable change that makes the
conversation newly relevant, and an insight about what that change typically means for
businesses like theirs. The change event is the datable "why now" that `foundations/pvp.md`
requires; the prior relationship is only the excuse for warmth. PVP applies in full: strip
the CTA and the message should still brief them usefully on their own new situation.

---

## Measurement

- Base health: field completeness, deliverability rate, and duplicate rate over time — the
  hygiene half's scoreboard
- Reveal yield: dormant records crossing into fit per refresh cycle (a collapsing yield
  means the base is mined out; a huge one means the scoring changed, not the world)
- Reactivation performance versus the account's cold baseline — familiarity-plus-fit should
  visibly outperform; read against the account's benchmarks (`scoring-model.md` §8)
- Automation unblocked: sends and workflows previously failing on missing fields, now
  executing
- The account's campaign gates (`scoring-model.md` §8) govern any reactivation sequence; results log to
  the account's `signal-library.md` performance log

---

## When NOT to run it

- **A tiny or young base.** Nothing to mine; run the acquisition plays first.
- **No CRM owner at the table.** An enrichment loop imposed on a CRM without its
  administrator becomes a turf war fought with field overwrites, and the humans will win by
  abandoning the system.
- **Consent has lapsed.** Where the legal basis for contact has aged out, no reactivation
  frame fixes it. Suppression law beats pipeline math, every time.
- **Overwrite-everything syndrome.** If precedence rules cannot be enforced, run
  enrichment as suggestions routed to review, not as writes. A CRM the team distrusts is
  worse than an incomplete one.
