# GTM Revenue Kit

**A complete outbound engine, written as files.** Fifteen plays, four channel guides, six
skills an agent runs end to end, and the scoring and suppression rules that gate them. It
decides who gets contacted, what they get sent, and what has to be true before anything sends.

Every rule is a document you can open, read, and disagree with. Nothing is buried in a
settings screen. Start with [`examples/sample-company/`](examples/sample-company/): a produced
campaign and the folder it came out of.

## The fifteen plays

A play is a buying moment plus everything needed to act on it. Each one names what fires the
signal and where the data comes from, how fast the window decays, why it works, the message
frame, the build, what to measure, and **when not to run it**. About 120 lines each, 1,849
across the set.

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

## Channels and situations

| [Channel guide](motions/channels/) | What it covers |
|---|---|
| [Cold email](motions/channels/cold-email.md) | the economics, the testing discipline, deliverability and warmup |
| [Cold calls](motions/channels/cold-calls.md) | when calling pays, the three numbers that run the channel, dialing method |
| [LinkedIn ABM](motions/channels/linkedin-abm.md) | when to automate, who to target, what to send |
| [Micro-lists](motions/channels/micro-lists.md) | very small, sharply segmented lists worked by hand |

Four [situation playbooks](motions/playbooks/) sit alongside them: competitor switch,
deliverability and warmup, impact positioning, and new signal response.

## The six skills

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

## How it composes

This is what makes it an engine rather than a folder of documents. A play activates through
the account's signal library, routes to a named skill, draws its numbers from that account's
scoring model, clears the suppression ledger, and sends through one of the four channels.
Every connection is written down, so any sent message traces back to the signal that caused it.

## The rules underneath

**Mechanism in core, numbers in the account.** Core states how a score composes and never what
a dimension is worth. Two accounts can score the same company differently and both be right,
which is what lets one engine serve many clients without forking.

**One home per fact.** A number written twice will disagree with itself within a month, so
scoring values, thresholds, and buyer facts each live in exactly one file.

**Core never names an account.** Every rule must read correctly for any client. Enforced by
search rather than by convention.

**Suppression before every send.** Per-account, append-only, checked before every batch. There
is no send capability in this repository and there is not meant to be.

## Why files

Most go-to-market logic lives inside configuration screens where nobody can read it, review
it, or say why an account was contacted. Here the state is files, so the reason a prospect was
contacted, or excluded, is a document you can open and argue with. The tradeoff is real: this
suits sequential, human-reviewed, repeatable work, and it loses at high-concurrency serving
and automated mid-pipeline branching, which genuinely need framework code.

The [`foundations/`](foundations/) wing holds the why-layer in 13 files, including an
append-only record of rulings and the failure modes this kind of system falls into.
[`CONTEXT.md`](CONTEXT.md) is the task router: every job and the one file that holds it.

## Scope

**Built and documented; operating history still ahead of it.** The method library, the account
stamp, and the doctrine layer are complete and routed. The first campaign has not run, which
means the feedback loop that rewrites scoring from results is designed rather than exercised.

**Reach is built out; capture is partial.** The plays, channels, and reply handling all ship.
Landing pages and forms belong to a separate machine by design and are not here.

**The market-mapping pipeline runs stages 1 and 2 of 6.** Folders are created as content is
briefed rather than in advance, so the shape of the work stays visible.

**The runtime is specified, not wired.** [`runtime-spec.md`](runtime-spec.md) describes the kit
executing motions against a live tool estate. It waits on account credentials and a datastore,
neither of which belongs in a public repository.

## Provenance

[`NOTICE.md`](NOTICE.md) records every inherited element: what came from where, under what
licence, and what was checked when. [`decisions/`](decisions/) carries the reasoning behind
construction calls, including the ones later revised. Licence: [MIT](LICENSE), covering this
repository's own work.
