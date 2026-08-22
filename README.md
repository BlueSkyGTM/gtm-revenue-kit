# GTM Revenue Kit

**A complete outbound engine, written as files.** Fifteen plays, four channel guides, six
skills an agent runs end to end, and the scoring and suppression rules that gate them. It
decides who gets contacted, what they get sent, and what has to be true before anything sends.

Every rule is a document you can open, read, and disagree with. Nothing is buried in a
settings screen. Start with [`examples/sample-company/`](examples/sample-company/): a produced
campaign and the folder it came out of.

## The Fifteen Plays

A play is a buying moment plus everything needed to act on it. Each one names what fires the
signal and where the data comes from, how fast the window decays, why it works, the message
frame, the build, what to measure, and **when not to run it**.

| Play | Fires when |
|---|---|
| [Inbound-Led Outbound](motions/plays/01-inbound-led-outbound.md) | an identified company hits a high-intent page, not just the homepage |
| [Inbound Speed-to-Lead](motions/plays/07-inbound-speed-to-lead.md) | a prospect volunteers contact: a form, a signup, a booking |
| [News-Led Outbound](motions/plays/04-news-led-outbound.md) | a news event matching a pattern this account has found to precede purchase |
| [Champion Job Change](motions/plays/10-champion-job-change.md) | someone who championed the product lands at a new company that fits the ICP |
| [Renewal Window Targeting](motions/plays/11-renewal-window-targeting.md) | a competitor's customer enters an estimated renewal window |
| [Competitor Crisis Response](motions/plays/12-competitor-crisis-response.md) | a verified negative public event at a named competitor |
| [Social Engagement Signal](motions/plays/05-social-engagement-signal.md) | a person engages with content about the problem space |
| [Go-To-Network](motions/plays/15-go-to-network.md) | a partner's connections hold a real fit they know well enough to introduce |
| [One-to-One ABM](motions/plays/06-one-to-one-abm.md) | the operator names a person as worth bespoke treatment |
| [One-to-Many ABM Gifting](motions/plays/14-one-to-many-abm-gifting.md) | a top-tier contact shows a personal affinity evidenced from public traces |
| [ABM Content Engine](motions/plays/03-abm-content-engine.md) | a deal reaches the point where several different personas must each say yes |
| [Executive Channel Outreach](motions/plays/13-executive-channel-outreach.md) | another play needs an executive to carry the message |
| [Recruiting Outbound](motions/plays/08-recruiting-outbound.md) | a hard-to-fill role opens internally and a candidate's history matches it |
| [CRM Enrichment and Reactivation](motions/plays/09-crm-enrichment-reactivation.md) | records go stale, or a closed-lost reason expires |
| [TAM Sourcing and Tiering](motions/plays/02-tam-sourcing-and-tiering.md) | nothing. This one builds the list the others fire against |

That last row is the point rather than an oversight. Play 02 states outright that it has no
buying-moment trigger and that pretending otherwise would be dishonest.

## Channels and Situations

| [Channel guide](motions/channels/) | What it covers |
|---|---|
| [Cold email](motions/channels/cold-email.md) | the economics, the testing discipline, deliverability and warmup |
| [Cold calls](motions/channels/cold-calls.md) | when calling pays, the three numbers that run the channel, dialing method |
| [LinkedIn ABM](motions/channels/linkedin-abm.md) | when to automate, who to target, what to send |
| [Micro-lists](motions/channels/micro-lists.md) | very small, sharply segmented lists worked by hand |

Four [situation playbooks](motions/playbooks/) sit alongside them: competitor switch,
deliverability and warmup, impact positioning, and new signal response.

## The Six Skills

An agent runs these end to end. Each names the files it reads, its steps, and how long it
should take.

| [Skill](motions/skills/) | Job | Time |
|---|---|---|
| [`setup`](motions/skills/setup/) | stamp a new account from the template | 15 to 30 min |
| [`account-research`](motions/skills/account-research/) | one account researched to a written brief | 20 to 40 min |
| [`icp-scoring`](motions/skills/icp-scoring/) | score and tier an account, or a batch | 15 to 30 min |
| [`signal-to-sequence`](motions/skills/signal-to-sequence/) | turn a fired signal into a built campaign | 2 to 4 hrs |
| [`reply-handling`](motions/skills/reply-handling/) | triage a reply from any campaign | on trigger |
| [`weekly-update`](motions/skills/weekly-update/) | the operating review | 10 to 15 min |

Six [workflows](motions/workflows/) carry the connective work: campaign build, enrichment,
signal routing, and pain-based segmentation.

## How It Composes

This is what makes it an engine rather than a folder of documents. A play activates through
the account's signal library, routes to a named skill, draws its numbers from that account's
scoring model, clears the suppression ledger, and sends through one of the four channels.
Every connection is written down, so any sent message traces back to the signal that caused it.

## The Rules Underneath

**Mechanism in core, numbers in the account.** Core states how a score composes and never what
a dimension is worth. Two accounts can score the same company differently and both be right,
which is what lets one engine serve many clients without forking.

**One master copy of every fact.** A number written twice will disagree with itself within a
month, so scoring values, thresholds, and buyer facts each live in exactly one file. The
kit's own name for this rule is one home per fact.

**Core never names an account.** Every rule must read correctly for any client. Enforced by
search rather than by convention.

**Suppression before every send.** Per-account, append-only, checked before every batch. There
is no send capability in this repository and there is not meant to be.

## The Chain of Operations

Every rule above sits at a level, and the levels are ordered. Composition runs down, so each
rung is made of the one below it. Construction runs up, because instruments cohere into
systems, running systems reveal an architecture, and architecture distils into principles.

| Rung | Layer | What lives there |
|---|---|---|
| 1 | The eight functions | what a revenue system must do |
| 2 | Revenue architecture | design doctrine, plus this kit's principles |
| 3 | Systems architecture | the design layer; models are its vocabulary |
| 4 | Systems | the built backbone, one per business |
| **5** | **Instruments** | **skills, plays, workflows, connectors. This kit** |
| 6 | Operations | campaigns running; output is pipeline, then revenue |

**This kit is rung 5, organised to serve rung 4, executed at rung 6.** Its method files are
instruments, its account template is a system's shape, and its motions are what operations
run. Nothing in core belongs at rungs 1 to 3 except the files that state them.

Rung 1 is the eight functions, and they are the load-bearing columns of any revenue system
rather than a description of this one. **No tool appears in any of them**, which is why
swapping the stack never takes you out of the discipline, and why the same eight describe a
software company and a bookkeeping practice equally well.

| Function | What it governs | Examples of what fills it |
|---|---|---|
| **Identify** | who is worth contacting at all, and who is ruled out | a scoring model, a target market map, intent signals, an exclusion list |
| **Offer** | what is being sold, to whom, on what terms | positioning, pricing, packaging, the messaging house |
| **Reach** | how a first touch actually gets made | cold email, calls, LinkedIn, events, partner referrals, ads |
| **Capture** | what happens the moment someone raises a hand | forms, reply handling, speed to lead, routing to an owner |
| **Move** | how interest becomes a signed customer | sequences, meetings, proposals, tier-based treatment |
| **Retain** | how a customer stays one | the CRM record, renewal tracking, delivery, account reviews |
| **Follow up** | everyone who has not said yes yet | nurture timing, re-approach rules, do-not-contact checks |
| **Learn** | how results feed back and change the system | win/loss review, campaign results, rescoring, the calibration log |

**The columns are fixed and what fills them is not.** Reach is a requirement; which channel
answers it is the account's choice. The scoring mechanism lives in core; the weights and
thresholds live in the account. Refusing to fix the filling is what lets one frame connect
businesses that share nothing, and it is the values-in-the-account rule one level up.

Two things stop this being decoration. **The frame is labelled as chosen rather than
discovered**: [`chain-of-operations.md`](foundations/chain-of-operations.md) dates the check
and states where the strong form of the claim fails, since "fails one, fails as a revenue
system" holds for identify, offer, reach, capture and move but is too strong for retain and
learn, which businesses neglect for years while still making money. Those two are what
separates a system that compounds from one that merely repeats. **And corrections stay in
place rather than being edited away**: the same file carries a dated reversal of its own
source on whether capture is an unbounded function.

[`conceptual-framework.md`](foundations/conceptual-framework.md) turns the eight into judgment
instruments for the grey areas, which is what the kit reaches for when method is silent and
when the question is whether an output is any good.

## Orchestrating the Providers

The kit is not a data source. It is the layer that decides which provider gets called, in
what order, and whether the call is worth paying for. Claude Code drives that directly from
the files: a session reads the contract for the job, walks the provider order it names, and
writes results back into the account. No integration platform sits in the middle holding the
logic.

**Discovery and enrichment run as a waterfall, never as a menu.** Providers fire in sequence
with failover, cheapest rung first, and a paid call has to justify why the free rung could
not answer:

| Rung | Providers | What it answers |
|---|---|---|
| Free | company site, LinkedIn, Crunchbase and PitchBook free tiers, BuiltWith, Wappalyzer, GitHub | headcount, funding history, tech stack, hiring |
| Orchestrated | Clay, running Clearbit then People Data Labs | firmographics, contacts, seniority |
| Paid lookup | Apollo, Hunter, NeverBounce | email discovery, validation, verification fallback |
| Search API | SerperDev and similar, called over plain HTTP | whole-market enumeration, far cheaper at volume than credit-per-row integrations |

**Signals come in the same way, from sources the account declares.** Funding rounds from
Crunchbase or PitchBook, job postings from LinkedIn, Ashby or Otta, engagement from Common
Room or Trigify, tech-stack movement from a BuiltWith delta, intent from 6sense, G2 or
Bombora. Each one lands in the account's signal library with its detection method and decay
recorded, which is what a play activates against.

**A provider gateway sits under the paid rungs, and it does not get to drive.** Deepline is
the surface the kit reaches through for provider access on the operator's own keys. Its public
skills pack was read and triaged in
[`decisions/`](decisions/2026-08-14-deepline-skills-triage.md): the cost gate and the
companies-before-people discovery order were absorbed, and its meta-skill's claim to govern
the session was refused, because the contracts route and a tool surface that claims session
governance inverts the architecture.

**Two gates sit in front of the calls, and neither substitutes for the other.** A cost gate
runs pilot, then preview, then approve, then scale before any paid rows are bought. A consent
gate runs before every push to a sequencer. Keys are the operator's own, per account, so the
bill and the data both stay with whoever owns the account.

The rule underneath is that provider choice is account configuration rather than doctrine. The
kit names the order and the criteria; which vendors hold keys is declared per deployment, so
a block that cannot say which criterion picked its tool has an undeclared setting rather than
a preference. [`runtime-spec.md`](runtime-spec.md) holds the execution model and
[`enrichment-techniques.md`](motions/workflows/enrichment-techniques.md) holds the cost model.

## Why File Architecture

The kit is a folder tree, not an application. That is a deliberate choice about where a
revenue system's state should live, and this is what it buys.

**The filesystem is the shared memory.** State lives on disk rather than inside a context
window, so the session is disposable and the work is not. An agent can stop mid-campaign, hit
its limit, or be a different model next week, and the next one resumes from files that record
what happened and what is still owed. Nothing has to be held in memory or passed between
agents through a protocol.

**Work is split across agents deliberately, and not for speed.** The load rules are strict
about what may share a session: one campaign workflow at a time, and never two rule systems
that judge each other's output. Copy discipline and scoring discipline in the same session
produce nonsense in both directions. Keeping them apart is a correctness property, which is
what makes this a multi-agent design rather than one assistant holding a very large prompt.

**Contracts are the interface.** Seventeen `CONTEXT.md` files each name what their folder
takes in and what it hands on. An agent loads the one contract its task names and stops,
which is what keeps a library this size usable by a model that can hold only a fraction of it
at once. A handoff is a file at a known path, not a message.

**Accounts do not contend.** Every number lives in its own account, and outputs are written
new each run, dated, never rewritten. Agents working different accounts share no mutable
state, and the suppression ledger, the one thing that must stay correct under concurrent
writes, is append-only.

**And a person can read all of it**, which is the part that matters when the work is
reviewed. Most go-to-market logic lives in configuration screens where nobody can say why an
account was contacted. Here that reason is a document you can open and disagree with.

The honest boundary: handoffs are sequential and human-gated. Several agents running at once
against the same object, with shared mutable state and automated mid-pipeline branching, is
what framework code is for and is not what this is.

The [`foundations/`](foundations/) wing holds the why-layer in 13 files, including an
append-only record of rulings and the failure modes this kind of system falls into.
[`CONTEXT.md`](CONTEXT.md) is the task router: every job and the one file that holds it.

## Scope

**Built and documented; operating history still ahead of it.** The method library, the account
stamp, and the doctrine layer are complete and routed. The first campaign has not run, which
means the feedback loop that rewrites scoring from results is designed rather than exercised.

**Reach is built out; capture is partial.** The plays, channels, and reply handling all ship.
Landing pages and forms belong to a separate machine by design and are not here.

**The instruments do not declare their functions yet.** Doctrine requires every skill, play
and workflow to name which of the eight it serves. An audit on 2026-08-22 found that none of
the 19 inherited instruments does, and recorded it rather than back-filling it blind. Open, in
[`decisions/`](decisions/).

**The market-mapping pipeline runs stages 1 and 2 of 6.** Folders are created as content is
briefed rather than in advance, so the shape of the work stays visible.

**The provider orchestration is specified, not yet wired.** The waterfall order, the cost
gate, the criteria and the signal sources are all written down and routed. What is still open
is operator input rather than design: a Deepline account and which providers get keys, where
each deployment's database lives, and who holds send-approval authority in writing.
[`runtime-spec.md`](runtime-spec.md) §6 names all three. Credentials do not belong in a
public repository, so nothing here carries one.

## Provenance

[`NOTICE.md`](NOTICE.md) records every inherited element: what came from where, under what
licence, and what was checked when. [`decisions/`](decisions/) carries the reasoning behind
construction calls, including the ones later revised. Licence: [MIT](LICENSE), covering this
repository's own work.
