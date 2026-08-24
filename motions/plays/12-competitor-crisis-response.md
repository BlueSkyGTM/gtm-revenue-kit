# Play: Competitor Crisis Response

Most urgency in outbound is manufactured; this play waits for the real thing. When a direct
competitor suffers a public crisis — a breach, litigation, an outage, a reputational event —
their customers involuntarily re-open the vendor decision. The play maintains standing
monitoring for such events, pre-builds the ability to identify the competitor's customers
inside the account's TAM, and moves a coordinated multi-channel motion within days, carrying
an offer engineered to remove switching cost. It reaches an audience whose status quo just
broke, in the brief period before it re-forms.

---

## The signal

**What fires:** a verified negative public event at a named competitor, material enough
that the competitor's customers would plausibly reconsider — the bar is "would their buyer
forward this article to a colleague with a question mark," not "any bad press."

**Where it comes from:** standing news and web monitoring of the account's competitor set —
an agentic monitoring flow (built in an orchestrator like Clay or a Claude-based pipeline)
scanning on a regular cadence, firing an internal alert (chat notification) for human
verification. The second data dependency is pre-built: technographic identification of which
TAM companies run the affected competitor, via an index such as HG Insights or BuiltWith —
strongest for enterprise, where such indexes draw on job postings and event data as well as
site scraping. Out of thousands of mapped accounts, the affected slice is typically small —
and it is the highest-priority list the account will hold all year.

**Decay:** exceptional — days, not weeks. Attention tracks the news cycle; early movers get
the meetings, late movers join the noise. The account's `signal-library.md` records this as
an **Intent (event-driven)** signal, weekly-or-faster refresh, top-of-scale weight per the
account's `context/scoring-model.md`, and the shortest recency window in the library.

---

## Why it works

Switching inertia is the strongest force in B2B retention, and a crisis is one of the few
events that dissolves it from the inside: the customer's own risk calculus flips, and
"nobody got fired for staying" briefly becomes "someone might get fired for staying."
Outreach arriving in that window meets a buyer who has already, involuntarily, started the
evaluation. At enterprise scale, single deals caught this way justify the entire standing
apparatus.

The offer mechanics matter as much as the timing. The two objections that survive even a
crisis are switching cost and the unexpired incumbent contract; an offer that neutralizes
both — migration handled at no cost, plus free use until the existing contract runs out —
answers the whole remaining objection stack at once. Contract-term concessions of that size
are priced by the account, never by this playbook.

The limits are ethical and legal, and they are hard edges. Publicly gloating over a
competitor's breach reads as ambulance-chasing and stains the brand that does it; naming
the competitor's crisis in outbound copy or public content invites legal exposure
(defamation risk if any detail is wrong) and buyer disgust even where accurate. The play's
voice is *the safe alternative*, never *the vulture*. And crises pass: if the affected
customers' pain was transient, urgency evaporates mid-motion.

---

## The build

1. **Stand up monitoring before any crisis.** The competitor set from
   `accounts/<slug>/context/competitor-radar.md` feeds the monitoring flow; alerts route
   to a human who verifies the event and judges materiality. This play cannot be built
   after the trigger — the window is too short.
2. **Pre-wire the customer identification.** Keep the technographic mapping of
   incumbent-per-TAM-account current (shared machinery with
   `motions/plays/11-renewal-window-targeting.md`), so the affected segment is one
   filter away, not one project away.
3. **On verified trigger: cut the segment.** Filter the TAM to companies on the affected
   competitor, run `motions/skills/icp-scoring/SKILL.md`, apply the account's `optouts.md`, and
   rank by tier. Speed target: segment in hand within a day or two of verification.
4. **Air cover: executive-voiced content.** A senior leader records short video content
   positioning the account's offering as the stable, safe choice — *without naming the
   competitor or the event*. Seed it organically through many employee profiles, watch
   which version earns engagement, then amplify the winner with paid thought-leader
   distribution targeted precisely at the affected segment's people.
5. **Ground game: executive 1:1 outreach.** Executives (not SDRs — see
   `motions/plays/13-executive-channel-outreach.md`) reach the segment's
   decision-makers directly through a LinkedIn-automation tool such as HeyReach, sharing
   the video and, where the account has approved it, the switching offer.
6. **Route conversations into the competitive motion.** Replies flow into
   `motions/playbooks/competitor-switch.md` (Scenario B, active evaluation) with battlecards
   current. Log everything to the account's `signal-library.md` performance log.

---

## The message frame

The crisis is never named; the *decision criteria it activated* are. The frame: open on the
question the buyer's own leadership is now asking (continuity, security posture, vendor
stability — whichever the event made urgent), deliver a genuinely useful evaluation frame
for it, and present the account's offering as the answer to that criteria, not as the
incumbent's obituary. The switching offer — migration and contract-bridge terms as the
account defines them — appears as the answer to the objection the reader is already
rehearsing. Strip the CTA and the message is a usable vendor-risk checklist: the PVP
standard (`foundations/pvp.md`). The "why now" is datable but deliberately unstated;
the reader supplies it themselves, which is stronger than saying it.

---

## Measurement

- Trigger-to-segment and trigger-to-first-touch latency — the play's defining metrics
- Content engagement within the targeted segment versus outside it (the air cover only
  counts where the ground game is aimed)
- Reply, meeting, and evaluation-entry rates for the affected segment versus the
  account's baseline competitive outreach, read against the account's benchmarks (`scoring-model.md` §8)
- Deal outcomes and offer economics: what the migration-plus-bridge concession cost
  against what the displaced deals returned — reviewed per event, priced by the account
- False-alarm rate at the verification step (a noisy monitor trains the team to ignore it)

---

## When NOT to run it

- **The event is human tragedy.** Layoffs with visible harm, safety incidents, anything
  with victims: capitalizing reads as ghoulish because it is. Sit those out entirely.
- **The account cannot absorb the offer.** Free-until-expiry terms against long incumbent
  contracts are a real financial commitment; without priced approval in advance, the
  ground game writes checks the account has not agreed to cash.
- **Unverified or exaggerated events.** Moving on a rumor imports the defamation risk
  directly into outbound copy. Verification is a human gate, not a formality.
- **No standing apparatus.** Discovering the crisis in the trade press and then starting
  to build the customer map means arriving after the window shut. If the monitoring and
  mapping are not pre-built, this is next quarter's play, not this week's.
