# The Playbook Shelf

One engine, many doors. Every playbook composes the same skills — scoring, research, sequencing — and what changes is the situation that opens it. This file is the selection layer: it tells you which door, then points at the file; it never restates what the file holds.

Contents: Selection · Root situation guides · The signal plays · The channels · The dormant shelf · Composing playbooks

Each entry carries its lineage tag inline (`upstream` · `operator` · `imported` — the model is `docs/lineages.md`). The catalog tables live where they belong: the plays in `plays/README.md` (with maturity ratings), the channels in `channels/README.md`.

## Selection

Ask one question first: **what just happened?**

| The situation is… | Go to |
|---|---|
| a signal fired on a qualified account | `new-signal-response.md` — then the play that owns that signal (`plays/README.md`) |
| no signal yet, only a market to map | `plays/02-tam-sourcing-and-tiering.md` (build) via `workflows/tam-campaign.md` |
| a competitor is in the picture | `competitor-switch.md` — timed by `plays/11-*`, triggered by `plays/12-*` |
| a new buyer needs positioning before any copy exists | `impact-positioning.md` |
| choosing or tuning an outreach channel | `channels/README.md` — the four-channel family below |
| sending infrastructure is not ready (or just got flagged) | `deliverability-and-warmup.md` |
| a niche motion: hiring, gifting, referrals, executive-voiced sends | `plays/08-*`, `plays/14-*`, `plays/15-*`, `plays/13-*` |
| no active motion fits, but the method should exist somewhere | `dormant/` — read each file's `Activate when:` line |

Two families behind the table: the four **root guides** handle situations (a signal, a competitor, a buyer, an inbox); the **plays** each own one signal or buyer moment and compose the kit's skills around it. Channels decide *how* a touch travels; plays and guides decide *why now*.

## Root situation guides

### New Signal Response `upstream`

The spine of the whole signal motion: what happens between a signal firing and a first touch. Validate the signal, score the account, then run the tier-appropriate response — bespoke research and a hand-written touch at the top, a personalized sequence entry in the middle, automation below. Every play in the library hands off to this file once its signal fires.

**Defining moves:**
- Validation before anything: genuine, ICP-qualified, unsuppressed, fresh — any failure logs and stops.
- Tier decides the treatment; the bands live in the account's `context/scoring-model.md`, never here.
- Tier-one touches are written, not templated, under the PVP standard; tier-two gets one personalized element minimum.
- Everything logs to the CRM, because the log is what calibrates the signal library later.

**Watch for:**
- Skipping validation because the signal "looks obviously real" — duplicates and stale fires are exactly the ones that look real.
- Tier-one treatment applied at tier-two volume; the time budgets exist to prevent it.

### Competitor Switch `upstream`

Four competitive scenarios, four different games: they use a competitor and have never heard of you; they are actively comparing; they just reviewed the competitor negatively; they are locked under contract. The playbook routes each to its own angle, all drawing on the account's battlecards in `context/competitor-radar.md`.

**Defining moves:**
- Identify the scenario before writing a word — the four motions are not interchangeable.
- Lead with insight, never with the comparison; the competitor goes unnamed in first touches.
- Under-contract accounts get the long game: plant a flag, no pitch, resurface near renewal.
- Battlecards update after every competitive win or loss, or they rot into fiction.

**Watch for:**
- "I saw you use [Competitor] and we're better" — combative openings that read as an attack on the prospect's own past decision.
- Stale battlecards: a card describing deals from years ago is misleading, not merely old.

### IMPACT Positioning `operator`

The six construction steps that take a new buyer from "we should sell to them" to a complete, campaign-ready positioning set — alternatives, beachhead, champions, pinpointed value, messaging house, per-channel translation — plus a step-seven audit run against positioning that is already settled. A buyer who is not the primary ICP is a track, with its own full set.

**Defining moves:**
- Run the steps in order; a message crafted before value is pinpointed is a slogan.
- Every step fills a named file under `accounts/<slug>/context/`; the playbook holds no facts of its own.
- Unproven claims carry an explicit `[PROOF GAP]` marker, never silent omission.
- The audit is run by a reviewer who did not write the positioning; findings go to the operator, who decides what ships.

**Watch for:**
- The discount version: an ICP file plus one persona is two of seven artifacts, not positioning.
- Campaigns that source and score hundreds of contacts for a buyer whose positioning does not exist yet — every downstream artifact inherits the gap.

### Deliverability & Warmup `operator`

Sending infrastructure without risking the account's real domain: the separate-sending-domain rule, the free/safe/scaled tradeoff, the warmup arc, and the standing caps and bounce ceilings. Upstream of every email send in the system — no inbox, no touch.

**Defining moves:**
- Cold outbound never leaves the primary domain; a lookalike domain forwards to the real site.
- Free, safe, and scaled: pick two. The path that survives is separate-domain, warmed, then automated.
- Warmup weeks are not dead time — work the top of the list by phone while the domain ripens.
- The already-litigated decisions stand: no marketplace pre-warmed domains, no personal free-mail sending.

**Watch for:**
- A big automated blast from a domain new to sending — the precise pattern spam filters exist to catch.
- Re-litigating the rejected shortcuts every time warmup feels slow.

## The signal plays

All fifteen are `imported` (contract and C3 caveat: `plays/CONTEXT.md`; catalog with maturity column: `plays/README.md`). Each pairs one observable signal with the buyer moment it predicts. Grouped here by that moment.

### Intent plays — the buyer is paying attention right now

**01 · Inbound-Led Outbound.** An identified ICP company visits a high-intent page; de-anonymization turns existing traffic into a behavioral signal, and outreach lands while the research window is open. Reaches problem-aware buyers pre-contact.

**Defining moves:**
- The page visited is part of the signal — pricing depth qualifies; a homepage bounce does not.
- ICP-filter and suppress before anyone sees the stream; junk identifications kill the play operationally.
- Message on the problem the visited page addresses, never on the visit itself.

**Watch for:**
- Low traffic or no high-intent pages: the signal fires too rarely, or cannot distinguish researcher from buyer.
- Anyone tempted to write "noticed you checked us out" — if the team cannot resist, do not arm them.

**05 · Social Engagement Signal.** Repeated engagement with category content by a decision-maker, scraped from a curated creator list — a self-refreshing pool of people educating themselves toward a purchase. Reaches buyers earlier than intent data, later than cold.

**Defining moves:**
- The filter is the play: enrich engagers to title and seniority and discard most of the pool.
- Accumulate, don't react — single engagements monitor, repeat engagement fires.
- Enter the conversation they are already having; the topic match is the personalization.

**Watch for:**
- Buyers who are not platform-native: the pool fills with plausible-looking peers and vendors who never buy.
- Engagement-stalking copy — citing their specific likes and comments damages the brand it runs under.

**07 · Inbound Speed-to-Lead.** A form submit or signup — the only signal the prospect fires on purpose. Cut the form to the minimum, reconstruct the rest by enrichment, score inline, and respond to qualified leads in minutes through parallel channels, at the moment intent peaks.

**Defining moves:**
- Every form field enrichment can answer is a field removed and conversion recovered.
- Qualified leads get two things at once: a personalized reply from a named seller and a human alert prompting a call.
- Close the loop to acquisition — real revenue outcomes feed the ad platforms, not form fills.

**Watch for:**
- Speed without substance: an instant generic autoresponder squanders the one advantage the play buys.
- Alerts nobody is staffed to answer — promised responsiveness that turns out to be theater.

### Market-event plays — something changed around the buyer

**04 · News-Led Outbound.** Public news coverage announces buying moments — an opening, an expansion, a launch — before buyers enter any funnel. Monitor for the account's purchase-preceding event pattern, extract and verify the company, and arrive pre-shortlist with a datable "why now" both sides agree is real.

**Defining moves:**
- Work backwards from the product to the event pattern; the right event is the one that creates first-time need.
- Discard ambiguous extractions rather than guessing; dedupe on company plus event.
- Name the event, then spend the message on what people in that situation get wrong next.

**Watch for:**
- No honest purchase-preceding event exists, or coverage lands after the purchase — the stream becomes a list of people who already bought.
- Sensitive events (layoffs, disasters): real need, repugnant framing — route through play 12's restraint rules.

**09 · CRM Enrichment and Reactivation.** The CRM as a signal source pointed inward: a standing refresh loop keeps records true, and the refresh reveals dormant leads whose situation has changed into fit. Familiarity plus current fit, at an audience acquisition already paid for.

**Defining moves:**
- Two distinct fires: record decay (workflow, not outreach) and fit revealed (the outreach signal).
- Field-level precedence rules, agreed with the CRM owner before the first run — hygiene, not vandalism.
- Reactivation is a re-introduction: prior contact gets one clause; what is true *now* carries the message.

**Watch for:**
- Consent that has aged out — suppression law beats pipeline math, every time.
- Overwrite-everything syndrome: a refresh loop that clobbers human-verified truth makes the CRM worse, and the team abandons it.

**11 · Renewal Window Targeting.** A derived signal: the technographic first-detected date approximates the incumbent's contract start, and standard renewal cycles project forward to the window when switching is actually on the table. A calendar for the account's competitive outreach.

**Defining moves:**
- Treat the estimate as honest guesswork — roughly-right concentration beats even spreading, and that is the whole claim.
- Sell the *question* (what re-evaluators discover), never the estimated date.
- This is the timing layer under `competitor-switch.md`; Scenario D covers the between-windows long game.

**Watch for:**
- "Your renewal is coming up in [month]" — a guess presented as surveillance, wrong at scale.
- An empty battlecard for the target incumbent: timing gets you into an evaluation only the battlecards can win.

**12 · Competitor Crisis Response.** A verified negative public event at a competitor breaks their customers' status quo for a few days. Standing monitoring plus pre-built customer identification lets a coordinated motion — executive air cover, executive 1:1 ground game, a switching-cost-removing offer — move before the window re-forms.

**Defining moves:**
- Build before the trigger: monitoring and incumbent mapping cannot be assembled inside a news cycle.
- Never name the crisis; voice the decision criteria it activated. Safe alternative, never vulture.
- The offer neutralizes the two surviving objections — migration cost and the unexpired contract — priced by the account, never by the playbook.

**Watch for:**
- Human tragedy as trigger: events with victims are sat out entirely.
- Unverified events — moving on a rumor imports defamation risk directly into outbound copy.

### Relationship plays — warmth is the asset

**06 · One-to-One ABM** *(maturity: message frame and measurement flagged for operator input — see `plays/README.md`).* The operator names one person worth bespoke cost; one-pass enrichment plus deep research feeds a hand-chosen channel and gesture. Costly signaling at the top of the market, where the effort is the message.

**Defining moves:**
- One sentence on why this person is worth bespoke cost; if it cannot be written, they belong in a sequence.
- Research-to-ready collapses into one action, or the motion stays too slow to run consistently.
- Sent as a person, from a person; follow-ups written, never scheduled.

**Watch for:**
- Disguised volume: dozens of "bespoke" targets a week is a sequence with expensive props, and recipients at this level detect the fraud.
- A half-verified fact in a bespoke touch — the worst single failure the system can produce.

**10 · Champion Job Change.** A hand-curated watchlist of people who genuinely carried past relationships; when one starts at an ICP-fit company, the alert routes to the specific human who holds the relationship, inside the new-role honeymoon window.

**Defining moves:**
- The watchlist is built by hand, by the relationship holders — never exported by filter.
- Both halves required: real relationship and ICP-fit destination; non-fit moves log, not action.
- Activation is deliberately manual: the play forbids auto-sequencing its targets.

**Watch for:**
- A watchlist of logged contacts rather than real champions — warm outreach becomes cold outreach with presumption added.
- Wiring alerts into a sequence tool: automation is precisely what burns the warmth that makes it work.

**14 · One-to-Many ABM Gifting.** Play 06's psychology run across a researched sublist: a genuinely desirable gift, sent only where personal affinity is verified, shipped to research-resolved office addresses (no surprise-killing address ask), followed up in the hours the recipient is holding it.

**Defining moves:**
- Gift first, audience second — chosen for desirability, then filtered to genuine affinity, never the reverse.
- No evidence, no package; the affinity research is spot-audited because it is the foundation.
- Follow-up fires on *delivered* — the carrier's tracking flip, not a schedule.

**Watch for:**
- Below tier-one economics, or unfiltered lists: the play degrades into expensive merch distribution.
- Compliance and privacy: regulated recipients cannot accept gifts, and researched-address shipping unsettles privacy-sensitive audiences.

**15 · Go-To-Network.** A systematized referral motion: recruit well-connected partners, match their exported networks against the ICP, and run a weekly loop that converts confirmed overlap into compensated warm introductions — the one channel volume cannot commoditize.

**Defining moves:**
- Both conditions verified: ICP fit *and* the partner genuinely knows them — confirmed by the partner, never inferred from the graph.
- A named person staffs the partner motion like outbound; partners are the pipeline.
- Every introduction lands as tier-one: researched, bespoke, fees paid fast and visibly.

**Watch for:**
- The volume ceiling is structural — this layers over direct motions, never replaces them.
- Partners who spray: introductions from an undiscriminating connector arrive pre-discounted.

### Infrastructure and channel plays — not event plays, and honest about it

**02 · TAM Sourcing and Tiering** *(foundation, not an event play — its own first section says so).* The whole addressable market mapped once, scored, tiered, and assigned, so every selling day starts with a prioritized list. The signal, such as it is, is drift: the map decays, and the recurring work is keeping the tiers true. The substrate every other play filters against.

**Defining moves:**
- Err inclusive at sourcing; the scoring pass excludes. Every company lands in exactly one tier, including a worked-by-nobody tier.
- Suppression is marked on the map itself, so downstream plays inherit it.
- The refresh is scheduled or the play does not exist; an upward band crossing is its closest thing to a firing event.

**Watch for:**
- Tiering an unvalidated ICP — confidently ranked garbage, baked into infrastructure.
- The one-off map: a snapshot quietly wrong within a quarter and trusted anyway, wearing the costume of rigor.

**03 · ABM Content Engine.** A generation pipeline turning a stakeholder map into persona-specific enablement content for live committee deals — standing inputs (positioning, voice, proof library) plus per-deal intake, rendered through fixed templates, human-reviewed, delivered inside the deal clock.

**Defining moves:**
- The engine renders *from* the messaging house — the single-source pattern from `impact-positioning.md` — and never freelances claims.
- Every asset opens inside that stakeholder's own scoreboard; the pitch appears only as the resolution of their problem.
- Claims quote the proof library or carry a `[PROOF GAP]` marker; nothing reaches a buyer unreviewed.

**Watch for:**
- No proof library or unsettled positioning: the pipeline mass-produces polished assertion, or drift.
- Treating it as a substitute for discovery — garbage intake yields confident, personalized garbage.

**08 · Recruiting Outbound.** The engine pointed at a different market: candidates instead of customers. Profile fit against an open requisition plays the role of ICP fit; the same source-enrich-score-sequence machinery fills a hiring pipeline, reaching the employed, non-searching candidates job boards never sample.

**Defining moves:**
- Write the role like an ICP: hard requirements as filters, preferences as scoring dimensions.
- A recruiter reads the shortlist before anything sends — the judgment step automation cannot do.
- From the first reply onward it is a relationship, managed by a human, not a sequence.

**Watch for:**
- Commodity roles or a weak offer: outbound amplifies whatever offer it carries.
- Fake-personalized candidate outreach at volume — employer-brand self-harm with platform-enforcement risk compounding it.

**13 · Executive Channel Outreach** *(a channel, not a signal play — stated in its first section).* The same message converts differently depending on whose face sends it: professional-network outreach runs through executive profiles, operated centrally, with the executive stepping into live conversations. Mostly rides other plays' signals; connection-accepted and open-profile status fire natively.

**Defining moves:**
- The executive lends the identity, not the hours — but must know, approve, and actually take over live threads.
- Ramp like a human; bursts are what platform enforcement pattern-matches on.
- Two beats: the connection request carries no pitch; the pitch enters only an already-live exchange.

**Watch for:**
- Borrowed identity without genuine takeover — impersonation with extra steps, collateralized by the executive's reputation.
- Volume ambitions: this channel punishes scale by design, and a platform policy change can reprice it overnight.

## The channels

All four `imported` (contract: `channels/CONTEXT.md`; use-when table: `channels/README.md`). A channel playbook says how the medium works as a system; it never overrides the account's copy doctrine, suppression ledger, or send authority.

### Cold Email `imported`

Cold email at volume, run as an ad network: a message in front of a defined audience, measured on yield. Fits a large addressable market with room to burn test variants; carries the fixed-slot template side of conflict C1 (`workflows/tam-campaign.md`).

**Defining moves:**
- Test value proposition and list first; subject lines and phrasing are second-order, compressed only after a variant clears the bar.
- A three-tool stack — sender, data API, orchestrator — and consolidation is the point.
- The inbox process is where the channel's value is won: every reply triaged daily, interested replies called first, angry replies into `optouts.md`.

**Watch for:**
- Replies generated and then lost to slow, inconsistent handling — the channel's signature leak.
- A TAM too small for the volume math: that is micro-list territory, not a reason to burn the audience faster.

### Cold Calls `imported`

When calling pays, three KPIs run it — contactability, dials per day, conversion — each pointing at a different fix. Both a direct channel where deal size carries the cost, and the fastest harvester of the email channel's hand-raisers.

**Defining moves:**
- Place the account on the TAM-size-by-deal-size matrix before choosing dialing infrastructure.
- Two phone-sourcing regimes: small companies' public numbers scraped directly; larger targets need a mobile-number waterfall.
- Keep the capability even when direct math is marginal — a call within hours of an interested reply out-converts the next email.

**Watch for:**
- "The channel doesn't work" claims that dissolve on checking actual dials per day.
- Treating conversion as a talent lottery instead of a trainable skill.

### LinkedIn & ABM `imported`

A precision channel: a small weekly connection budget means email scales, LinkedIn aims. Two campaign architectures — the recognition asset that trades on professional pride, and the executive-network campaign that works large first-degree networks without consuming executive time.

**Defining moves:**
- Never automate a profile with genuine organic traction; automate reach that has no motion.
- Contact only demonstrably active users — the connection-count filter alone multiplies reply rates.
- The CRM disqualification pass before any enrollment is mandatory: an executive pitching an existing client ends the program.

**Watch for:**
- Plain pitches spent against a sniper's budget — the ask must be worth a shot.
- A recognition asset that never ships, poisoning the well for every future campaign.

### Micro-Lists & 1:1 `imported`

The high-touch pole of a splitting channel landscape: tiny, sharply cut segments, deep research per prospect, long-form messages sent by hand from real accounts. For markets too small — or deals too large — for volume; volume gates in `docs/standards.md` explicitly do not apply at these list sizes.

**Defining moves:**
- The segment definition *is* the personalization: cut until one specific message is true for everyone in it.
- AI moves upstream — research in the orchestrator, composition and send by a human.
- Measure absolute outcomes per segment, not rates; each segment-plus-ask is one experiment.

**Watch for:**
- The dying middle band: modest volume, modest personalization, machine-sent.
- One wrong detail is fatal here — the message's entire premise is that someone did the homework.

## The dormant shelf `operator`

Method skeletons awaiting a motion that needs them — real frameworks no account currently runs, each opening with an `Activate when:` line that is the whole index. Do not load them in a working session; activation is a core change, spelled out in `dormant/README.md`. Engineer tier.

- **account-planning.md** — per-account strategy with power maps, entry and expansion paths, for multi-stakeholder deals whose size justifies it.
- **buyer-group-mapping.md** — the committee mapped slot by slot: economic buyer, champion, user, blocker, influencer.
- **champion-enablement.md** — arm the person who must sell the purchase internally; materials written for forwarding, not reading.
- **demo-scripting.md** — timed beats, not features; every beat names what the audience should feel.
- **mutual-action-plan.md** — co-owned milestones and dates; a buyer who will not co-own dates is qualification signal.

## Composing playbooks

The shelf composes because every playbook exits into the same skills. The stacks that recur:

- **Signal → response → channel.** A play detects the moment, `new-signal-response.md` validates and tiers it, `skills/signal-to-sequence` builds the touches, and a channel playbook carries them — all under one copy doctrine per campaign.
- **The map under everything.** `plays/02-*` (via `workflows/tam-campaign.md`) seeds the tiered market that plays 01, 04, 11, and 12 filter against and the channels draw lists from; its suppression marks propagate downstream for free.
- **The competitive stack.** `plays/11-*` and `plays/12-*` share technographic machinery, and both route their conversations into `competitor-switch.md` — timing layer, trigger layer, and conversation layer of one motion.
- **The high-touch cluster.** `plays/06-*`, `plays/14-*`, and `channels/micro-lists.md` share economics and research discipline; 14 industrializes 06's gifting mechanism, and 06 is the escalation tier for any play that surfaces a person worth bespoke treatment.
- **The executive carrier.** `plays/13-*` can carry the sends of most other plays — most visibly the ground game of `plays/12-*` — and `channels/linkedin-abm.md` Architecture 2 is the same borrowed-authority pattern at network scale.
- **Positioning before volume.** `impact-positioning.md` gates any campaign for a new buyer; `plays/03-*` then renders from the messaging house it produced. `deliverability-and-warmup.md` gates any email send at all.

One caveat governs every stack: **composition never blends the two copy doctrines in one campaign.** A play's PVP-rendered frame and cold-email's fixed-slot template are parallel traditions (conflict C1, `docs/lineages.md`); the account picks one doctrine per campaign and the stack runs under it end to end.
