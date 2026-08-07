# The Signal-Play Library

Each file in this folder is one **play**: a recipe that pairs an observable signal with the
buying moment it predicts and the motion that converts it. Plays are core — they hold
mechanism only, pass the swap test (`docs/isolation.md`), and carry no company names,
prices, or thresholds. Every number a play needs lives in the running account's
`context/scoring-model.md`.

**A play is a composition, not a new skill.** Each one orchestrates the kit's existing
skills — `icp-scoring` decides who qualifies, `account-research` builds the brief,
`signal-to-sequence` turns the signal into touches — under the standards in
`docs/standards.md` (PVP, tiers, campaign gates, datable "why now").

**To activate a play for an account:** add its signal as a row in that account's
`context/signal-library.md` — category, source, refresh cadence, recency window — and set
its weights in `context/scoring-model.md`. A play with no signal-library row is dormant for
that account; the same play can be live in one account and dormant in another, tuned
differently in each. Response mechanics from detection to first touch:
`playbooks/new-signal-response.md`.

## Catalog

| # | Play | Signal | Buyer moment | Maturity |
|---|------|--------|--------------|----------|
| 01 | [Inbound-Led Outbound](01-inbound-led-outbound.md) | Identified ICP company visits a high-intent page | Actively researching the category, pre-contact | Complete |
| 02 | [TAM Sourcing and Tiering](02-tam-sourcing-and-tiering.md) | None — foundational; fires on tier drift | All of them; this is the map the other plays land on | Complete (foundation) |
| 03 | [ABM Content Engine](03-abm-content-engine.md) | Multi-stakeholder deal needs per-persona materials | Committee evaluation in progress | Complete |
| 04 | [News-Led Outbound](04-news-led-outbound.md) | Public news event that precedes first-time purchase | Need just created, shortlist not yet formed | Complete |
| 05 | [Social Engagement Signal](05-social-engagement-signal.md) | Repeated engagement with category content by a decision-maker | Self-education phase, pre-evaluation | Complete |
| 06 | [One-to-One ABM](06-one-to-one-abm.md) | Operator names a bespoke-worthy individual | Whenever the account decides one person is worth real cost | Method solid; message frame and measurement flagged for operator input |
| 07 | [Inbound Speed-to-Lead](07-inbound-speed-to-lead.md) | Form submit / signup — declared intent | Hand raised, attention peaking, minutes matter | Complete |
| 08 | [Recruiting Outbound](08-recruiting-outbound.md) | Role-fit match against an open requisition | Candidate not searching; employer needs to move first | Complete (non-sales audience) |
| 09 | [CRM Enrichment and Reactivation](09-crm-enrichment-reactivation.md) | Refreshed record reveals a dormant lead now fits | Situation changed since last touch; familiarity intact | Complete |
| 10 | [Champion Job Change](10-champion-job-change.md) | Watchlisted champion starts at an ICP-fit company | New-role honeymoon; importing a trusted stack | Complete |
| 11 | [Renewal Window Targeting](11-renewal-window-targeting.md) | Derived: incumbent's estimated contract renewal approaches | Keep-or-replace decision reopening | Complete |
| 12 | [Competitor Crisis Response](12-competitor-crisis-response.md) | Verified negative public event at a competitor | Status quo broken; customers involuntarily re-evaluating | Complete |
| 13 | [Executive Channel Outreach](13-executive-channel-outreach.md) | Channel play; fires on connection accept / open-profile status | Any — changes who the message comes from, not when | Complete (channel, not signal) |
| 14 | [One-to-Many ABM Gifting](14-one-to-many-abm-gifting.md) | Verified personal affinity + gift-delivery event | Manufactured moment: gift in hand, attention held | Complete |
| 15 | [Go-To-Network](15-go-to-network.md) | Partner-confirmed network overlap with the ICP | Reachable only through a trusted vouch | Complete |

## Reading the table

- **Signal** is what the account's `signal-library.md` row records. Three entries (02, 06,
  13) are honest exceptions — a foundation, an operator judgment, and a channel — and each
  file says so in its first section rather than dressing up as an event play.
- **Buyer moment** is the state the signal predicts; it is why the play beats cold, and
  the thing to re-verify if a play stops performing.
- **Maturity** reports how fully the method specifies each section. Where a play's source
  method was thin, the file marks the gap explicitly instead of padding it.

Plays combine. The common stacks: 02 is the substrate everything else filters against;
11 and 12 share technographic machinery and both route into
`playbooks/competitor-switch.md`; 13 can carry the sends of most other plays; 06 is the
escalation tier for any play that surfaces a person worth bespoke treatment.
