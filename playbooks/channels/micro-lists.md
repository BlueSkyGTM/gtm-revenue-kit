# Playbook: Micro-Lists & 1:1 Outreach (Channel Strategy)

*The high-touch end of outbound: very small, sharply segmented lists worked with deep
research, long-form personal messages, and hand-sent delivery. For accounts whose market is
too small — or whose deals are too large — for the volume motion.*

---

## Trigger

Any of:
- The account's addressable market is small: the volume math in
  `playbooks/channels/cold-email.md` doesn't have room to run
- Deal sizes are large enough that a single prospect justifies hours of effort
- Volume outbound is landing in spam or reading as automated to a sophisticated audience
- A creative, high-touch play is wanted for a named-account tier

---

## The thesis: outbound is splitting in two

Two outbound approaches keep working as filtering gets smarter, and they sit at opposite
poles:

1. **High-volume, high-tech, 1-to-many.** Very large TAM, industrial sending volume,
   real-time deliverability analytics, offer optimization by reply rate. Effectively a
   direct-response operation — and increasingly the province of specialized teams, because
   the infrastructure burden is heavy and rising.
2. **Super-personalized, creative, high-touch, 1:1.** Small TAM, high deal value, deep
   research per prospect, messages composed for one reader and **sent by hand from real
   accounts** — a plain personal mailbox and a real LinkedIn profile, not a sending platform.

The pressure creating the split: mail providers keep getting better at detecting
platform-sent mail, so the middle — modest volume, modest personalization, machine-sent —
is the band that dies first. And the strategic fact that decides which pole most accounts
belong to: **most TAMs are not big.** The volume motion assumes an audience most accounts
simply do not have. Where the account's own line sits is recorded in
`context/scoring-model.md`, reasoning from TAM size and deal value: a small market of
high-value buyers is micro-list territory; a huge market of small buyers is volume territory.

AI does not disappear at this pole — it moves upstream. The orchestration platform does the
deep research (the account, the person, shared history, common angles); the human does the
final composition and the send.

---

## Building the micro-list

Start from the account's mapped TAM (`workflows/tam-campaign.md`) and cut it into **small,
sharp segments** — narrow enough that one specific message is true for everyone in the
segment. Useful cutting dimensions, combinable:

- **Sub-vertical** — one business model within the ICP, not the whole ICP
- **Buyer characteristic** — a demographic or situational trait of the customer base that
  shapes the pain
- **Technology** — one named system in the stack that the account's offer touches
- **Moment** — an observable event (an opening, a launch, a hire) that dates the outreach

A micro-list segment is deliberately tiny — tens of prospects, not hundreds. The segment
definition *is* the personalization: when the segment is sharp enough, one well-researched
message reads as 1:1 to every member.

---

## The message

Long-form is allowed here — this is the one channel where it works, because the research
earns it. The working anatomy:

1. **A researched common-ground angle** — something genuinely specific: their expansion,
   their stack, a shared city, a dated observable event. This is the line that proves a
   human did the work.
2. **A concrete, unusual ask** — not "a quick call": an invitation to a small event or
   dinner, an assessment, a feedback exchange on work relevant to them, a conference invite.
   The ask should be something a peer might plausibly propose.
3. **Optionally, a tangible incentive** — a gift card or gift attached to the feedback
   exchange. This can work strikingly well, and it carries real caveats: budget per prospect
   is an account decision (`ACCOUNT.md`), reasoning from deal value; and whether incentives
   are appropriate at all depends on the prospect's industry and the account's compliance
   posture — many regulated buyers cannot accept gifts, and an incentive that reads as
   payment-for-meeting damages trust. Decide per account, record the decision.
4. **A human sign-off that sounds like the sender** — including, where true, the plain
   admission that the message was written personally. Authenticity claims must be true:
   never write "this isn't automated" on an automated send.

Every specific must survive the verification standard in `docs/standards.md` — in this
channel a wrong detail is fatal, because the entire premise of the message is that someone
did the homework.

---

## Operations

The daily loop, staffed by the operator or a trained assistant:

1. **Research runs in the orchestration platform** — segment membership, per-prospect
   angles, contact data, all prepared into a working table
2. **A small daily batch of emails is sent by hand** from a real personal mailbox — composed
   or final-edited by the sender, no sending platform in the path
3. **A matching daily batch of LinkedIn messages** goes from a real profile
4. **Replies are worked like the high-value conversations they are** — same-day response,
   phone where possible (`playbooks/channels/cold-calls.md`)

Daily batch sizes are account values (`ACCOUNT.md`). The reasoning constrains them twice
over: small enough to stay within what one human can genuinely personalize to quality, and
small enough to look like what it is — a person corresponding, not a system sending.

**Measurement changes at this pole.** Yield-per-send is the volume channel's metric; here
the list is too small for rates to mean much. Track absolute outcomes per segment — replies,
conversations, meetings — and treat each segment as one experiment: the segment-plus-ask
combination either produced conversations or it didn't.

Suppression still runs first: `accounts/<slug>/optouts.md` and any declared client roster,
before every batch, hand-sent or not.

---

## Related

- `playbooks/channels/linkedin-abm.md` — the same economics with LinkedIn as the spine;
  the recognition-asset architecture is a natural micro-list ask
- `playbooks/channels/cold-email.md` — the opposite pole; read both before choosing
- `workflows/tam-campaign.md` — the TAM map the segments are cut from
- `playbooks/deliverability-and-warmup.md` — why hand-sent mail from a real mailbox plays
  by different rules than platform volume
- `docs/standards.md` — verification and the "why now" standard, at their strictest here
