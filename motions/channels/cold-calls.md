---
type: channel
provenance: michael-course
maturity: standard
---

# Playbook: Cold Calls (Channel Strategy)

*When calling pays, the three numbers that run the channel, how to choose dialing
infrastructure, and how to source phone numbers at scale. Calling is both a direct channel
and the fastest harvester of hand-raisers from the email channel.*

---

## Trigger

Any of:
- Deciding whether cold calling belongs in an account's channel mix
- Interested email replies are sitting unworked (`motions/channels/cold-email.md` says
  call them first)
- A calling motion exists but meetings aren't materializing
- Choosing or replacing dialing infrastructure

---

## The economics: calling is expensive, so the deal must carry it

A calling motion carries real per-conversation costs — callers' time, dialing software,
phone-number data — that email does not. The channel is profitable only when the account's
average deal size clears those costs; below that line, calling survives only in its cheap
role as the follow-up to warm email replies. The account records its own line in
`context/scoring-model.md`, reasoning from fully loaded cost per booked meeting against deal
value and close rate. The main lever for lowering the line is labor cost — offshore SDR
hiring is a legitimate and common move, but it is an operational project of its own (hiring,
training, QA), not a setting to toggle.

Even where the direct math is marginal, keep the capability: a call placed within hours of
an interested email reply converts far better than the next email would, and that hybrid use
alone can justify a small calling operation.

---

## Three KPIs run the channel

Track exactly these, and read them as diagnostics — each points at a different fix:

| KPI | Definition | If it's low, the problem is... |
|---|---|---|
| **Contactability** | Prospects who answer ÷ prospects called | The data or the infrastructure — wrong/stale numbers (mobile coverage problem) or a dialer that burns time between calls |
| **Dials per rep per day** | Raw activity, tracked religiously | Activity management — verify actual dialing before assuming anything else; undercounting here quietly explains most "the channel doesn't work" claims |
| **Conversion** | Meetings booked ÷ prospects who answered | The conversation — invest in dedicated cold-calling training; this is a trainable skill with specialist trainers, not a talent lottery |

Targets for each are account values (`context/scoring-model.md`). The channel is genuinely
more complex than three numbers, but these three localize almost every failure fast, and
that is what an operating metric is for.

---

## Choosing dialing infrastructure: TAM size × deal size

The dialer question is really a motion question. Place the account on this matrix first:

| Account shape | Motion | Infrastructure |
|---|---|---|
| Small TAM, high deal size | Full-cycle seller working 1:1, thinking hard about each account | **CRM-native or sales-engagement dialing** |
| Large TAM, smaller deal size | SDR velocity — volume of conversations per day | **Power dialer** |
| Very large TAM, low contactability | Parallel dialing to manufacture conversations | **Predictive dialer** |

**CRM-native / sales-engagement dialing** (dialers built into CRMs or platforms in the
Outreach/Salesloft category): slowest per dial, but every call happens inside full account
context, and the platform covers the omnichannel motion — email, tasks, social touches —
around the call. Often already included in an existing CRM plan. Right when each conversation
is high-stakes and research-backed.

**Power dialers** (tools in the PhoneBurner/Apollo-dialer category): purpose-built calling
UI, dramatically faster prospect-to-prospect, usually bundling SMS and voice/message drops
for an omnichannel feel. Right when rep productivity is the constraint and the list is deep
enough to justify the pace.

**Predictive dialers** (tools in the Nooks/Salesfinity category): dial several numbers
simultaneously and connect the rep to whoever answers first — at the cost of a connection
delay the prospect can hear, per-seat pricing at the top of the market, and a minimum team
size to make the parallelism pay. Right only when contactability is structurally low (some
industries answer one call in fifty or worse) and the TAM is large enough to absorb
aggressive dialing.

Prices are deliberately absent: they shift constantly, and the selection logic doesn't. Cost
the shortlist at current rates against the account's cost-per-meeting model.

---

## Sourcing phone numbers

Two regimes, split by target size:

**Small organizations** (owner-operated businesses, small e-commerce, local trades): the
company's public phone number *is* the decision maker's number. Scrape it from the website
with an AI agent in the orchestration platform, format the numbers consistently, export to
the dialer. Cheap, high-coverage, and covered by the small-company variant in
`motions/tam/skeleton.md` Stage 3.

**Larger organizations**: the switchboard is a wall — contactability on company mains is
near zero, so the motion needs personal mobile numbers. The sequence: map the full TAM,
identify decision makers per account (Stage 3 of the TAM workflow), then run a **mobile-number
waterfall** — multiple phone-data providers tried in succession per contact, as the
orchestration platform's waterfall feature implements. Mobile data is priced per successful
find and is among the most expensive data in the stack, so the account budgets it
deliberately (`ACCOUNT.md`), reasoning from cost-per-mobile against the value of a
conversation with that persona. Coverage is generally excellent, and a working mobile number
is one of the highest-leverage data points outbound can buy.

---

## Related

- `motions/channels/cold-email.md` — the channel whose interested replies this channel
  calls first
- `motions/tam/skeleton.md` — TAM mapping and people-finding upstream of any call list
- `motions/workflows/enrichment-techniques.md` — the scraping and waterfall mechanics for number
  sourcing
- the account's `context/scoring-model.md` §8 — its declared diagnostics; the "high reply, low meeting" pattern applies to
  calls as "high contact, low conversion"
