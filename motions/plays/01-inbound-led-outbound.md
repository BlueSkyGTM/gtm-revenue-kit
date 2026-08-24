# Play: Inbound-Led Outbound

A visitor identification service turns anonymous website traffic into named accounts, and
the engine treats an identified ICP visit as a behavioral signal. The people it reaches are
already problem-aware — they found the site, chose a page, and read it — so outbound to them
is closer to a follow-up than a cold open. The play converts existing marketing spend
(search, ads, events) into a second harvest the sales side runs.

---

## The signal

**What fires:** an identified company visits the account's website — and specifically a
high-intent page (pricing, integrations, a solution page), not just the homepage. The page
visited is part of the signal, not decoration on it.

**Where it comes from:** a visitor de-anonymization service (RB2B, Leadfeeder, Warmly, or
similar) resolving traffic to companies and, where the service supports it, to individuals.
Coverage is partial by nature — a meaningful share of traffic never resolves, and resolution
is materially better for some geographies than others.

**Decay:** fast. A pricing-page visit is a statement about this week, not this quarter. The
account's `signal-library.md` records this as a **Behavioral** signal with a near-real-time
refresh cadence and a short recency window; the point value and the decay curve live in the
account's `context/scoring-model.md`, per `foundations/principles.md`.

---

## Why it works

The visitor has already done the hardest part of outbound for you: self-selection. They know
the category exists, they know this vendor exists, and they spent attention on a specific
problem page. Outreach that lands inside that window meets a warm brain instead of a cold one.

The honest limits: the visitor is not always the buyer (researchers, students, competitors,
and existing customers all browse), the company-level match tells you the account but not the
individual who visited, and resolution coverage means the play sees a slice of traffic, never
all of it. This play needs real traffic volume to matter — below a floor the account's
`scoring-model.md` should state, the signal fires too rarely to justify the build.

---

## The build

1. **Source.** Wire the de-anonymization service to stream identified visits into an
   enrichment orchestrator (Clay or similar). Capture company, page visited, and timestamp —
   the page is the qualification evidence.
2. **Filter for ICP.** Score each identified company against the account's
   `context/icp-definition.md`. Discard non-fits before anyone sees them; the volume of junk
   identifications is what kills this play operationally.
3. **Suppress.** Check the CRM and the account's `optouts.md` before anything else: existing
   customers, open opportunities, and recent contacts exit here. A customer receiving a cold
   pitch for a product they already pay for is this play's signature failure.
4. **Enrich and pick the contact.** Where the service resolved a person, verify them against
   the account's personas. Where it resolved only the company, find the persona-matching
   contact through standard enrichment. Layer corroborating data points — open roles, recent
   job changes, title match — to sharpen priority; the combination bonuses live in the
   account's `scoring-model.md`.
5. **Score and route.** Run `motions/skills/icp-scoring/SKILL.md`. Tier bands (set in the account's
   `scoring-model.md`) decide the treatment: top-tier visits get a human first touch fast;
   mid-tier visits enter a signal-specific sequence via `motions/skills/signal-to-sequence/SKILL.md`.
6. **Speed matters.** The whole pipeline should complete inside the recency window the
   account's `signal-library.md` defines for this signal. A visit acted on late is a cold
   email wearing a warm signal's clothes.

---

## The message frame

Do **not** say "I saw you were on our website." It is true, it is creepy, and it teaches the
prospect nothing. The visit is targeting intelligence, not a hook.

The frame: open with an insight about the problem *the visited page addresses* — something a
person researching that topic would be glad to learn, sourced and specific to their situation.
The visit told you which problem they are shopping; the message proves you understand that
problem better than the page they read did. Strip the CTA and the message must still teach
them something about their own business — the PVP standard (`foundations/pvp.md`) applies in
full, and the "why now" is the observable condition that made them search (name it if research
surfaces it; never name the visit itself).

---

## Measurement

- Identified-visit → qualified-lead conversion (how much of the stream survives ICP filtering)
- Reply and meeting rates for visit-triggered outreach versus the account's cold baseline —
  this play should clearly beat cold; if it does not, the filter or the speed is broken
- Time from visit to first touch, measured against the recency window
- The the account's declared campaign gates (`context/scoring-model.md` §8) govern launch and kill
  decisions; the signal's actual pipeline contribution is logged in the account's
  `signal-library.md` performance log

---

## When NOT to run it

- **Low traffic.** Below the traffic floor the account sets, the build costs more than the
  meetings it yields. Fix demand generation first.
- **No high-intent pages.** If the site cannot distinguish a researcher from a buyer (one
  page, no pricing, no solution depth), the signal has no qualification power.
- **Privacy posture.** De-anonymization sits differently across jurisdictions and audiences.
  An account selling to privacy-sensitive buyers may correctly judge the signal source
  off-brand even where it is legal. This is an account-level decision recorded in the
  account's context, not a core default.
- **Anyone tempted to reference the visit in copy.** If the team cannot resist "noticed you
  checked us out," do not arm them with this data.
