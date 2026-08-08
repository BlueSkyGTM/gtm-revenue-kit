---
type: play
lineage: imported
maturity: standard
---

# Play: One-to-Many ABM Gifting

Gifting at segment scale, done the opposite of the branded-mug way: a genuinely desirable
gift, sent only to decision-makers whose *personal interest* in it is verified by research,
shipped without the surprise-killing address-request email, and followed up at the exact
moment of delivery. Where `playbooks/plays/06-one-to-one-abm.md` is one operator choosing
one person, this play runs the same psychology across a researched sublist of a
tier-one segment — small by campaign standards, large by gifting standards. It reaches
senior buyers who ignore every digital channel, through the one channel that still gets
unwrapped.

---

## The signal

**What fires:** a compound, researched condition — a contact at a top-tier account exhibits
a verifiable personal affinity matching the chosen gift. The affinity evidence comes from
public traces: posts about the hobby or interest, activity locations, stated history. The
gift is chosen first (for desirability), the audience is then filtered to genuine affinity —
never the reverse order, and never "everyone in the segment."

**Where it comes from:** an AI research agent (an agentic enrichment step in an
orchestrator like Clay, or a Claude-based research pipeline) cross-referencing the
account's tier-one contact list against public social and web traces for the affinity
pattern. A second research pass resolves each recipient's *office* shipping address from
public data — company and city in, deliverable address out — so no one has to ask the
prospect where to ship. A delivery-tracking integration (carrier API) supplies the
follow-up trigger.

**Decay:** the affinity itself is durable; the *delivery event* is the perishable part —
the follow-up window is the hours around the package landing. The account's
`signal-library.md` records the affinity as an enrichment attribute on tier-one contacts,
and "gift delivered" as a **Behavioral (manufactured)** trigger with the shortest recency
window in the account's `context/scoring-model.md`.

---

## Why it works

Three mechanisms, stacked. **Desirability:** most gifting fails at the object — merch
nobody wants creates the obligation of disposal, not reciprocity. The test is personal:
would the sender genuinely want to receive it? An object people actively covet transfers
real value, and reciprocity psychology does the rest. **Selectivity:** verified affinity
converts a generic gesture into a seen-and-understood one — the recipient infers, correctly,
that someone paid attention to them specifically. **Timing:** the delivery-triggered
follow-up reaches the recipient in the minutes they are holding the gift — measurably the
most receptive state outbound can engineer, and one conventional sequencing can never hit.

The address mechanism protects the second mechanism: the standard ask-for-your-address
email kills the surprise and loses most recipients before anything ships; researched
office-address shipping preserves both surprise and delivery rate.

The limits: cost per touch is high, so the play only prices against tier-one deal sizes
(the budget ceiling and per-gift spend live in the account's `scoring-model.md`); gift
compliance is a real constraint — many industries and public-sector roles cap or prohibit
gifts, and shipping researched addresses touches privacy expectations that vary by
geography; and the whole play collapses if the affinity research is sloppy — a golf gift
to someone who does not golf is a branded mug with better postage.

---

## The build

1. **Choose the gift first.** Something genuinely coveted by people with the target
   affinity, ideally scarce or hard to obtain — desirability is the gate. Handwritten
   notes from a named senior person ship with every package; the physical touch carries a
   human signature or it is cargo.
2. **Cut the affinity sublist.** Run the research agent across the tier-one contact list
   for verifiable affinity evidence. The output is deliberately small — the account's
   `scoring-model.md` sets the evidence bar and the batch cap. No evidence, no package.
3. **Compliance and suppression pass.** Check recipient-side gift rules (industry,
   role, jurisdiction), the account's `optouts.md`, and open-opportunity etiquette (a
   gift mid-negotiation reads differently than a gift cold — route those to the deal
   owner's judgment).
4. **Resolve shipping addresses by research.** The agent infers each recipient's office
   address from public data; ambiguous resolutions get human review, not a guess. Ship
   via a gifting platform or directly through a carrier — whichever the account records.
5. **Arm the delivery trigger.** The carrier's tracking API flips a status; the flip
   fires the seller notification. Follow-up launches on *delivered*, not on shipped and
   not on a schedule.
6. **Follow up multi-channel, immediately.** The assigned seller reaches out within the
   delivery window — the channels and their order per the account's context — referencing
   the gift naturally and moving to substance. Log outcomes to the account's
   `signal-library.md` performance log.

---

## The message frame

The gift bought the open; the message must justify it. The frame: a light, human
acknowledgment of the gift's context (the shared interest, the occasion — one line,
no "did you get my package" neediness), pivoting directly into a substantive reason this
company was worth the sender's effort — an insight about their business that stands on its
own. The PVP standard from `docs/standards.md` applies to the follow-up exactly as to any
first touch: strip the ask and the message still teaches them something; the gift is the
attention mechanism, never the value proposition. The datable "why now" is honest here —
the delivery event itself, plus whatever tier-one signal put the account on the list.

---

## Measurement

- Research precision: share of shipped gifts whose affinity evidence was correct
  (spot-audited — this is the play's foundation)
- Delivery rate on researched addresses (validates the no-ask shipping mechanism against
  the ask-first baseline it replaced)
- Follow-up latency: delivery-to-outreach time per seller, against the window
- Reply, meeting, and pipeline per batch, priced against fully loaded cost per package —
  the play justifies itself in return on spend, not in rate benchmarks; batch sizes sit
  below the campaign-gate audience threshold in `docs/standards.md`, so read rates with
  small-sample caution and judge on pipeline economics
- Compliance incidents: the acceptable number is zero

---

## When NOT to run it

- **Below tier-one economics.** The per-touch cost against mid-tier deal sizes is budget
  theater. The tier bands exist to price exactly this.
- **Regulated and public-sector recipients.** Where gift rules cap or prohibit, the
  package is a compliance incident with a bow on it. The compliance pass is a gate, not
  a formality.
- **Generic gifts to unfiltered lists.** Without verified affinity, the play degrades
  into expensive merch distribution — the exact failure it was designed against.
- **No follow-up capacity.** A delivered gift with a late or absent follow-up spends the
  entire mechanism and books nothing. If sellers cannot commit to the delivery window,
  do not ship.
- **Privacy-sensitive audiences.** Researched-address shipping delights most recipients
  and unsettles some; an account selling to privacy professionals should think hard
  before demonstrating inference capability as a greeting.
