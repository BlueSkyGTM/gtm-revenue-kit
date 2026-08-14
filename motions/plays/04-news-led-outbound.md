---
type: play
provenance: michael-course
maturity: standard
---

# Play: News-Led Outbound

Public news coverage announces buying moments before buyers ever enter a vendor's funnel — a
new location opening, an expansion, a launch, a relocation. The play monitors news sources
for the specific event pattern that precedes purchase of the account's product, extracts the
company behind each story, enriches it, and hands sellers a stream of prospects who are
provably mid-decision. It reaches buyers at the moment their need exists but their vendor
shortlist may not.

---

## The signal

**What fires:** a news item matching an event pattern the account has identified as
purchase-preceding. The pattern is account-specific by definition — the right event is the
one that creates first-time need for *this* product. The generic shape: an observable,
dated, public event after which the prospect must soon acquire something in the account's
category.

**Where it comes from:** news aggregation — a news API or aggregator feed (Google News,
a news-monitoring API, or similar) queried on keyword patterns, typically event-phrase plus
geography. Local and trade press catch what national wires miss.

**Decay:** governed by the event's own timeline. An event that implies a decision within
weeks makes the signal worthless once that window closes. The account's `signal-library.md`
records this as an **Intent** (or **Firmographic**, depending on the event) signal with a
daily refresh cadence and a recency window matched to the event's decision timeline; scoring
weight and decay live in the account's `context/scoring-model.md`.

---

## Why it works

Timing beats targeting. The event creates a first-time need, which means the buyer is often
pre-shortlist — no incumbent to displace, no renewal to wait out — and whoever arrives first
frames the evaluation. The news item also hands the outreach a legitimate, datable "why now"
(`foundations/pvp.md` requires) that the prospect themselves would agree is real:
you are writing to them *because* something happened, and both of you know what.

The limits: news coverage is incomplete and late for some events, keyword monitoring drags
in false positives (announcements that will not close, events misclassified), and the same
news is visible to every competitor who thinks to look. The moat is operational — extraction
speed and enrichment quality — not access to the signal.

---

## The build

1. **Define the event pattern.** Work backwards from the product: what public event forces
   a purchase in this category? Write the pattern and its keyword queries into the
   account's `signal-library.md` entry, including the geographies monitored.
2. **Monitor.** Schedule the news source query on a daily cadence into an enrichment
   orchestrator (Clay or a Claude-based pipeline).
3. **Extract and verify.** Parse each article for the company name, location, and event
   date — an LLM extraction step handles the unstructured text. Verify the company resolves
   to a real domain; discard stories where extraction is ambiguous rather than guessing.
4. **Deduplicate and suppress.** The same event gets covered more than once. Dedupe on
   company + event, then check the CRM and the account's `optouts.md`.
5. **Enrich and find the decision-maker.** Standard enrichment to firmographics and the
   persona-matching contact — for small businesses this is usually the owner; for larger
   ones, the persona in the account's `context/personas/`.
6. **Score and route.** Run `motions/skills/icp-scoring/SKILL.md`; the event's point value and the
   tier bands come from the account's `scoring-model.md`. Fresh, high-fit events route to
   sellers immediately; the rest enter a signal-specific sequence via
   `motions/skills/signal-to-sequence/SKILL.md`.

---

## The message frame

The event is nameable — this signal is public, so unlike a website visit, referencing it is
expected rather than unsettling. The frame: congratulate briefly or acknowledge the event in
one clause, then immediately spend the message on an insight about what people in their
situation typically get wrong or overlook *next* — the decision the event forces them into.
The value is a preview of a mistake they have not made yet. Strip the CTA and the message
still functions as useful advice from someone who has watched this event pattern play out
before: the PVP standard (`foundations/pvp.md`), with the event date as the built-in
datable "why now."

---

## Measurement

- Stream volume and precision: events surfaced per week, and the share that survive
  verification and ICP filtering (precision below the account's tolerance means the
  keyword pattern needs tightening)
- Speed: event date to first touch, held against the recency window
- Reply and meeting rates versus the account's cold baseline — the timing advantage should
  show up plainly, per the account's benchmarks (`scoring-model.md` �8)
- Win rate on news-sourced deals versus other sources, logged in the account's
  `signal-library.md` performance log

---

## When NOT to run it

- **No purchase-preceding event exists.** Some products follow no public moment. If the
  honest answer to "what news story means they need us" is "none," this play has no fuel —
  do not force a weak event pattern into service.
- **The event is covered too late.** If press coverage reliably lands after the purchase
  decision, the stream is a list of companies who already bought.
- **Extraction quality is unproven.** Sending outreach based on a misread article — wrong
  company, wrong event — fails the verify-specifics standard in `foundations/pvp.md` in the
  most public way possible. Gate the play on a human-audited extraction sample first.
- **Sensitive events.** Some newsworthy events (layoffs, disasters, litigation) create real
  need but make congratulatory or opportunistic framing repugnant. If the account runs on
  such events, the message frame needs its own review — see the restraint rules in
  `motions/plays/12-competitor-crisis-response.md`.
