# Play: Go-To-Network

A systematized referral motion: recruit well-connected partners, analyze their networks
against the ICP, and run a weekly loop that turns the overlap into warm, one-to-one
introductions — compensated by referral fee, and operated with the same discipline as an
outbound sequence. The premise it rests on is worth stating: as automated outreach floods
every channel, replies concentrate on senders the recipient already knows or recognizes.
This play buys access to "already knows" through the people who hold it. It reaches
high-value accounts through the one channel volume cannot commoditize — a trusted person's
personal vouch.

---

## The signal

**What fires:** a *network-overlap match* — the analysis of a partner's connections
surfaces a person who fits the account's ICP **and** whom the partner genuinely knows well
enough to introduce. Both conditions are required; the second is verified by the partner,
not inferred from the connection graph, because connection lists are full of strangers.

**Where it comes from:** the partner exports their professional-network connections (a
capability the platform provides its users) and shares the export under the terms of the
partner agreement. The list runs through an enrichment and matching flow (an orchestrator
like Clay or a Claude-based pipeline) that scores each connection against
`accounts/<slug>/context/icp-definition.md`. The weekly candidate list goes back to the
partner, who marks the real relationships.

**Decay:** relationships decay slowly; the *matching* decays with the export — people
change jobs, so a network snapshot goes stale like any list, and re-exports happen on a
cadence the account's `context/scoring-model.md` sets. The account's `signal-library.md`
records "partner-confirmed overlap match" as a **Relationship** row at the warm end of its
scale; an introduction made is Tier 1 treatment by definition.

---

## Why it works

An introduction converts the coldest variable in outbound — sender trust — into a solved
problem: the message arrives pre-vouched by someone whose judgment the recipient already
values, which no volume of copy optimization can replicate. For six- and seven-figure
offerings, where a single closed deal is transformative and buyers are the most
outreach-saturated people alive, the economics support paying meaningfully for that vouch.

The incentive design carries the play. A referral fee proportional to a large contract
value makes a single successful introduction genuinely significant money for the partner —
the fee percentage is the account's decision, recorded in its `scoring-model.md`, and the
generosity is the point: an underpaid connector is an inactive one. Early-stage accounts
can compound the incentive with equity or advisory roles, which converts a transactional
connector into someone with a stake in the account's success.

The honest limits: throughput is structurally low (each partner has finitely many real
relationships, and burning one on a bad introduction costs the partner reputation, so they
ration carefully); the motion lives or dies on partner-management discipline — untended
partners go quiet within weeks; and the play cannot be the whole engine, because its
volume ceiling is the sum of its partners' genuine networks.

---

## The build

1. **Recruit partners deliberately.** The profile: people whose networks are dense in the
   account's ICP — industry veterans, advisors, adjacent-service founders. The pitch is
   the referral structure itself: the fee, the process, what the partner actually has to
   do (very little, by design).
2. **Formalize the agreement.** The fee terms, and a small enablement kit: a partner
   guide, instructions for exporting their network, and a contract where formality is
   wanted. Equity or advisory variants per the account's decision.
3. **Ingest and match.** The exported network runs through the matching flow against the
   ICP definition. Matching criteria and thresholds live in the account's
   `scoring-model.md`; suppression against the account's `optouts.md` and current
   customer list runs here as everywhere.
4. **Weekly candidate loop.** Send each partner a short list of their ICP-matching
   connections. The partner marks who they genuinely know and makes the introductions —
   with scripts the account provides, because "what do I even write" is the number-one
   silent killer of willing referrers.
5. **Staff the partner motion like outbound.** A named person (SDR or equivalent) owns
   partner follow-up: keeping the loop running, answering questions, celebrating paid
   fees visibly, and recruiting new partners continuously. Partners are the pipeline;
   this role is the sequence.
6. **Receive introductions as Tier 1.** Every introduction gets researched
   (`skills/account-research/SKILL.md`) and handled with bespoke care — a fumbled
   introduction damages the partner relationship that produced it, which is the play's
   real capital. Outcomes log to the account's `signal-library.md` performance log, and
   fees get paid fast and visibly.

---

## The message frame

Two frames, because two audiences.

**To the partner (the weekly touch):** short, concrete, zero-pressure — here are the
matches, mark who you know, here is the script if you want it, here is the fee status on
prior introductions. The partner is a volunteer with upside; the frame respects their time
and rations the asks.

**Through the introduction:** the partner's own voice, aided by a script the account
supplies — one line of vouch, one line of why-this-is-relevant-to-you, handoff. The
account's first direct message then has to earn the vouch it arrived on: it opens with
substance specific to the introduced person's situation and satisfies the PVP standard
from `docs/standards.md` like any first touch — the introduction bought attention, not a
free pass to pitch. The datable "why now" is whatever made the partner think of them, and
the follow-up sequence discipline of `docs/standards.md` applies from there.

---

## Measurement

- Partner activation: share of signed partners who made at least one introduction inside
  the account's review horizon — the motion's true health metric; a roster of inactive
  partners is a list, not a network
- Loop throughput: candidate lists sent, relationships confirmed, introductions made,
  per partner per period
- Conversion: introductions → conversations → pipeline → closed, priced against fees
  paid — this play is judged on unit economics, not on rate benchmarks; volumes sit far
  below the campaign-gate thresholds in `docs/standards.md`, deliberately
- Time-to-first-fee per partner (the moment a partner gets paid is the moment they
  believe the program; shortening it compounds activation)
- Network freshness: age of each partner's last export against the refresh cadence

---

## When NOT to run it

- **Low-ticket offerings.** The fee math only motivates partners when deals are large;
  below that, the same energy put into direct motions returns more.
- **No partner-management capacity.** An untended referral program decays into a signed
  agreement and silence. If nobody owns the weekly loop, the play does not exist —
  whatever the paperwork says.
- **As a replacement for outbound rather than a layer.** The volume ceiling is
  structural. Accounts that need pipeline breadth run this alongside the direct plays,
  not instead of them.
- **With partners who spray.** A connector willing to introduce anyone to anyone is
  spending reputation they do not have; their introductions arrive pre-discounted. The
  partner's own rationing instinct is a feature — recruit people who have it.
- **Where network-data sharing is restricted.** The export-and-analyze step must sit
  inside the platform's terms and the jurisdiction's data rules, and inside the
  partner's own comfort — a partner uneasy about sharing their network is telling you
  something; listen.
