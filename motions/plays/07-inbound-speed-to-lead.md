---
type: play
provenance: michael-course
maturity: standard
---

# Play: Inbound Speed-to-Lead

Inbound is a signal the prospect fires at you — and most teams waste it twice, first with a
long form that drives away submitters, then with a response delay that lets interest cool.
The play inverts both: collect the minimum at the form (an email address), reconstruct
everything else through enrichment, score automatically, and respond to qualified leads
within minutes through parallel channels. It reaches hand-raisers — the highest-intent
population the engine will ever touch — at the moment their intent peaks.

---

## The signal

**What fires:** a prospect submits a form, signs up for the product, or books time — any
volunteered contact event. This is the only signal in the library the prospect generates on
purpose, which puts it at the top of whatever point scale the account's
`context/scoring-model.md` defines.

**Where it comes from:** the account's own properties, via whatever integration path fits
its stack — a form tool's native webhook, the marketing platform's integration (HubSpot,
Salesforce, Marketo, or similar), or a custom webhook, roughly in that order of build cost.

**Decay:** the fastest in the library — measured in minutes, not days. Buyer attention peaks
at submission and falls off within the hour; response-time research has shown order-of-
magnitude differences in contact and conversion rates between minutes-fast and hours-slow
responses. The account's `signal-library.md` records this as a **Behavioral (declared
intent)** signal, real-time refresh, with the response-time target in its Tier 1 action.

---

## Why it works

Three stacked mechanisms. **Friction:** every form field taxes conversion; a long
qualification form makes prospects pay the data-entry cost that enrichment could pay
instead, and some walk away rather than pay it. **Speed:** the submitter is at their desk,
thinking about the problem, often with competitor tabs open — the first substantive response
frames the comparison, and delay hands that framing away. **Qualification:** automated
scoring keeps sellers off low-value sign-ups, so speed is spent only where it earns.

The limits: enrichment cannot reconstruct everyone (personal email domains resolve poorly —
route those to a graceful manual path), an instant-but-generic reply squanders the speed
advantage, and a misfiring score that fast-tracks the wrong leads just automates waste.

---

## The build

1. **Cut the form.** Ask what enrichment cannot answer — usually just the email, plus at
   most the one question that routes intent. Every removed field is recovered conversion.
2. **Stream to enrichment.** The submission webhooks into the orchestrator (Clay or
   similar), which enriches from the email domain outward: company, size, industry, role,
   and the fit attributes the account's `context/icp-definition.md` cares about.
3. **Score instantly.** Run the logic of `motions/skills/icp-scoring/SKILL.md` inline. Tier bands
   from the account's `scoring-model.md` split the stream: qualified leads to the fast
   path, non-fits to a courteous automated path, unresolvable domains to human review.
4. **Respond in parallel, fast.** For qualified leads, two things fire at once: a
   personalized email from a named seller — referencing what the enrichment learned, with
   a direct scheduling link — and an internal alert (a chat-channel notification) that
   prompts a human call while the prospect is still warm. The response-time target lives
   in the account's `signal-library.md` Tier 1 action.
5. **Confirm-path automation.** For leads who book, an automated confirmation-and-reminder
   arc across the channels the account uses (email, SMS, messaging) protects show-up rate.
6. **Close the loop to acquisition.** Feed final outcomes — qualified, opportunity,
   closed — back to the ad platforms' conversion APIs so paid acquisition optimizes on
   real revenue events, not form fills. Log the same outcomes in the account's
   `signal-library.md` performance log.

---

## The message frame

The prospect asked to hear from you — the frame is *earned response*, not outreach. Answer
as the person they hoped would reply: acknowledge the specific thing they came for, show one
piece of understanding about their situation the enrichment made possible (their industry's
version of the problem, the use case that fits their shape), and make the next step
effortless — a direct link, a concrete time. The PVP standard (`foundations/pvp.md`) still
applies: even a hand-raiser should learn something from the reply beyond "we got your
form." The submission itself is the datable "why now," and it is one of the few signals
polite to reference directly.

---

## Measurement

- Form conversion rate before and after the field cut — the friction mechanism, verified
- Median submission-to-first-response time, against the target in the signal library
- Enrichment resolution rate on submissions (unresolvable share governs how much manual
  fallback the play needs)
- Contact rate and meeting rate by response-time bucket — this play's core claim is that
  faster converts better; the buckets prove or refute it for this account
- Scoring accuracy: sellers' post-call verdicts versus the automated tier, feeding
  corrections back into the account's `scoring-model.md`
- Funnel diagnostics per the account's benchmarks (`scoring-model.md` �8) for the response sequence itself

---

## When NOT to run it

- **Trivial inbound volume.** Below a steady flow, build the manual habit of fast response
  instead; the automation cost is not yet earning.
- **When qualification questions carry legal or routing weight.** Some industries must ask
  at the form (licensing, geography, compliance). Cut what enrichment can recover, keep
  what the law or the routing genuinely requires.
- **Speed without substance.** If the fast response is a generic autoresponder, the play
  becomes a spam-flavored acknowledgment. The speed only wins when the content is worth
  reading; a slower personal reply beats an instant hollow one.
- **When sellers are not staffed to answer the alert.** An instant email plus a call that
  never comes trains prospects that the responsiveness was theater. Match the promise to
  real coverage hours, and say so in the reply.
