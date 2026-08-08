---
type: play
lineage: imported
maturity: standard
---

# Play: Renewal Window Targeting

Most competitive outbound fails on timing: the prospect renewed their incumbent contract
months ago and is locked in, indifferent, unreachable. This play reverse-engineers when each
target's contract likely renews — using the date a technographic index first detected the
incumbent product on their site as a proxy for contract start — and concentrates outreach
into the narrow pre-renewal window when switching is actually on the table. It reaches
companies already paying for the category at the one moment they re-decide.

---

## The signal

**What fires:** a company using a competitor's product enters its estimated renewal window —
a derived signal, computed from data the account already gathers, rather than an observed
event.

**Where it comes from:** a technographic index (BuiltWith, HG Insights, or similar) provides
two facts per company: the incumbent technology is present, and the date it was *first
detected*. First-detected approximates install date, which approximates contract start.
Because subscription contracts renew on standard cycles — annual most commonly, sometimes
semi-annual or quarterly — candidate renewal dates project forward from that anchor.
Alternatively, a technographic intelligence platform can seed the list directly from a
product name.

**Decay:** the signal is a *scheduled window*, not a decaying event — it opens some weeks
before each projected renewal date and closes at it, then recurs next cycle. The account's
`signal-library.md` records this as a **Technographic (derived)** signal, refreshed as the
index refreshes, with the window length, the cycle assumptions, and the confidence handling
in the account's `context/scoring-model.md`.

---

## Why it works

Switching decisions are made in the pre-renewal window and almost never outside it. Between
renewals, even a dissatisfied customer treats switching as unbudgeted work; approaching
renewal, someone in the building is explicitly asking "keep or replace?" Outreach that lands
inside that question joins an evaluation already underway — the difference between proposing
a decision and joining one.

The estimate is honest guesswork, and the play must treat it that way. First-detected dates
carry noise (detection lag, site rebuilds, products present before the tracked snippet
appeared), and the renewal-cycle assumption is probabilistic. The play does not need
precision to work: being roughly right concentrates effort into windows where readiness is
elevated, which beats spreading the same effort evenly across the calendar. What the
estimate can never do is masquerade as knowledge in copy — "your renewal is coming up in
[month]" is a guess presented as surveillance, and it fails the verify-specifics standard
in `docs/standards.md` the moment it is wrong.

---

## The build

1. **Map incumbent users.** From the account's TAM
   (`playbooks/plays/02-tam-sourcing-and-tiering.md`), run the technographic enrichment
   inside the orchestrator (Clay or similar) and filter to companies where the target
   competitor technology is present.
2. **Extract the anchor date.** Pull first-detected into its own field and normalize it to
   a real date type — downstream math needs a date, not a string.
3. **Project renewal candidates.** Compute forward from the anchor on the standard cycle
   assumptions (annual, semi-annual, quarterly), keeping only future dates. An LLM
   enrichment step returning structured output (labeled fields per cycle assumption) makes
   this parse cleanly at scale; plain date arithmetic works too.
4. **Window filter.** A boolean per company: does any projected date fall within the
   outreach window currently being built? The window length and how far ahead the account
   plans live in its `scoring-model.md`. The output is a small, high-priority segment per
   planning period — this play is a *calendar* for the account's competitive outreach.
5. **Score, suppress, enrich contacts.** The window segment runs through
   `skills/icp-scoring/SKILL.md` and the account's `optouts.md`, then persona-matched
   contact enrichment as usual.
6. **Route to the competitive motion.** Sequence entry via
   `skills/signal-to-sequence/SKILL.md`, with angles drawn from the battlecards in
   `accounts/<slug>/context/competitor-radar.md` — this play is the timing layer under
   `playbooks/competitor-switch.md`, Scenario D of which handles the between-windows
   long game.

---

## The message frame

Never claim to know their renewal date. The frame sells the *question*, not the estimate:
open with an insight about what companies at their stage tend to discover when they
re-evaluate this category — the cost that grew quietly, the capability gap that widened,
the benchmark worth checking before signing for another cycle. The message equips the
reader for the keep-or-replace decision they are (probably) approaching, and it is valuable
even if the timing guess missed, because the decision recurs. Strip the CTA and it should
read as a genuinely useful evaluation checklist — the PVP standard from `docs/standards.md`.
The datable "why now" is the observable incumbency and its age, both verifiable facts.

---

## Measurement

- Estimate validation: where a real renewal date is eventually learned (from calls and
  closed deals), log estimated versus actual — the error distribution calibrates the
  window length in the account's `scoring-model.md`
- In-window versus out-of-window performance on otherwise-matched accounts: the play's
  entire thesis is that this split is large; if it is not, the anchor data is too noisy
  for this account's market
- Standard funnel metrics against the benchmarks and campaign gates in
  `docs/standards.md`; results log to the account's `signal-library.md` performance log
- Coverage: share of the incumbent-user map with a usable anchor date

---

## When NOT to run it

- **The incumbent is not web-detectable.** Products that leave no client-side trace give
  the index nothing; first-detected dates will be missing or meaningless.
- **Non-cyclical or perpetual contracts.** No renewal rhythm, no window to project.
- **As a surveillance flex.** If the copy cannot resist citing the estimated date, the
  play produces confidently wrong messages at scale — the exact failure the
  verify-specifics standard names.
- **Without a competitive story.** Timing gets you into an evaluation; only the
  battlecards win it. If `competitor-radar.md` is empty for the target incumbent, build
  it first or the window opens onto nothing.
