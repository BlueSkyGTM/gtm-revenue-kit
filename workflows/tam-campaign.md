---
type: workflow
lineage: imported
maturity: standard
---

# Workflow: TAM Campaign

*How we go from a market definition to a running outbound program — the list-construction
half of campaign work, end to end: map the market, refine it to ICP, find the people, write
and test, personalize, send.*

---

## Purpose

`workflows/campaign-build.md` starts from a defined segment and a signal: an audience already
exists, and the work is turning it into a live campaign. This workflow covers the motion that
comes *before* that, or instead of it — the **market-led** motion, where the starting point is
"every company we could conceivably sell to" and the list itself is the strategic work.

Use this workflow when:
- Opening a new market or segment where no signal library exists yet
- The account's ICP describes a market you have never fully enumerated
- Reply rates suggest the problem is the list, not the copy

Use `workflows/campaign-build.md` instead when a specific signal already defines the audience.
The two meet at the same place: a scored, enriched list feeding a sequence.

The premise of the whole workflow: **speed comes from ordering, not from shortcuts.** Each
stage exists to make the next one cheaper. A broad map makes refinement mechanical; a refined
list makes people-finding targeted; a clean contact list makes copy testing meaningful.

---

## Stage 1: TAM Mapping

**Goal:** one table containing, in broad strokes, every company in the addressable market.

The entire stage reduces to one question, answered before any tool is opened:

> **What is the best place on the internet to find the complete list of these businesses?**

The answer follows from incentives: where is this *kind* of business most motivated to be
listed, visible, or indexed? A company shows up completely and accurately only in places it
benefits from being.

| If the target sells... | It is probably best enumerated in... |
|---|---|
| B2B services or software | A professional network's company graph — these businesses are incentivized to maintain a presence there |
| Physical products online | A store-intelligence database (platforms such as Storeleads index e-commerce stores directly) — small stores often have no professional-network presence at all |
| Locally, from a physical location | A maps platform — restaurants, gyms, clinics, and trades live on maps, not on B2B networks |
| Into a licensed or credentialed niche | A vertical directory — broker registries, school databases, marketplace seller indexes, association member lists |

Two consequences of that table:

1. **Roughly half of markets come straight from professional-network data** — the "Company"
   and "People" sources inside a data orchestration platform (such as Clay) are pulling from
   that graph. When your target lives there, mapping is a filter exercise and this stage is
   fast.
2. **The other half each need a bespoke source**, and finding it is genuine research: deep
   search for directories, registries, and databases specific to the vertical. The scraping
   patterns for directories, maps, news, and ad libraries are in
   `workflows/enrichment-techniques.md` — read that before concluding a market can't be mapped.

**Map broad, filter later.** Do not encode ICP nuance into the source query. Pulling too
narrow at this stage silently excludes companies you can never get back; pulling broad costs
only a cheap classification pass in Stage 2. The output of this stage is allowed to be dirty.

---

## Stage 2: TAM Refinement

**Goal:** the broad map filtered down to companies that actually match the account's ICP,
with the reasoning recorded per row.

The raw map always contains companies that look right and aren't: the service business inside
an e-commerce dataset, the industry the account can't sell to, the technology that
disqualifies, the observable practice that signals "not our buyer." Refinement is a series of
cheap classification passes, one column per question:

1. **Write each disqualifier as a yes/no question a machine can answer from public data.**
   "Does this company sell physical products?" "Is it in an industry on the exclusion list in
   `accounts/<slug>/context/icp-definition.md`?" "Does its site show [the disqualifying
   practice]?"
2. **Answer each question with the cheapest tool that can answer it** — free formatting
   functions where the answer is mechanical, a low-cost AI classification pass (an LLM run
   through your own API key, not platform credits) where judgment is needed. The cost logic
   is in `workflows/enrichment-techniques.md`.
3. **Combine the answers into a single ICP verdict column.** One column, one verdict per row,
   derived from the individual checks — so a human can audit *why* a company was kept or cut.

Which filters exist and where the cut lines sit are account facts: the ICP definition lives in
`accounts/<slug>/context/icp-definition.md`, and any numeric boundary (employee floor, revenue
band, score threshold) lives in `accounts/<slug>/context/scoring-model.md`. This workflow only
fixes the *shape*: broad map in, per-question columns, one auditable verdict out.

---

## Stage 3: Find People & Enrich

**Goal:** for each qualified company, the right human beings with usable contact data.

`workflows/enrichment.md` owns the enrichment waterfall and quality gates; this stage is about
the step it assumes — getting from a list of company URLs to a list of people. There are three
routes, and they are a waterfall, not alternatives:

| Route | Cost | Coverage | Use it... |
|---|---|---|---|
| Platform-native people finder (the orchestration platform's own people-at-company source) | Free | Partial — only publicly open profiles | First, always |
| AI research agent per row | Very low per row | Partial, complements the above | Second, on the rows route 1 missed |
| Contact-database export (providers such as Apollo) | Paid, slower | Best available | Last, on what's still missing |

Order matters because each route is strictly cheaper than the next: exhaust the free coverage
before paying, and let the paid provider work only the residue.

Then, for every person found: **enrich the work email and validate it** — one contact-data
API can do both (see the minimal-stack pattern in `workflows/enrichment-techniques.md`).
Unvalidated emails are not contacts; they are future bounces, and the bounce ceiling in
`playbooks/deliverability-and-warmup.md` is easy to blow with one unvalidated batch.

**The small-company variant.** When the account sells to very small businesses, the
named-contact model partially inverts: scrape the generic inbox (`info@`, `hello@`) and the
phone number straight off the company website with an AI agent. At owner-operated scale, the
owner reads that inbox — a "generic" address is a direct line, and the phone number feeds the
cold-call channel (`playbooks/channels/cold-calls.md`).

---

## Stage 4: Copywriting & Testing

**Goal:** a value proposition proven against this list — not a polished email.

Cold email testing is not consumer A/B testing: the audience is thousands, not millions, so
there is test budget for one or two variables, not ten. The two variables that actually move
results are **the value proposition and the list**. Everything else — subject line, CTA,
phrasing, personalization depth — is second-order and gets tested only after a value prop
wins.

The discipline that enforces this is a **fixed template with slots**. Every first touch has
the same skeleton:

1. Greeting by first name
2. One personalized line (built in Stage 5)
3. One sentence carrying the entire test: the **outcome** you produce, the **distinctive
   mechanism** that produces it, a **proof point**, and a plain question asking whether it's
   worth a conversation
4. Sign-off — a name, nothing else

The template is deliberately plain and deliberately hard to write in. Because the structure
never changes, the only way to make variant B differ from variant A is to change the value
proposition itself — which is exactly the thing worth testing. Rewriting the same offer in
nicer words is no longer possible, and that is the point.

**Test mechanics:**
- Run several value propositions against the same list in parallel — enough variants to give
  the market a real choice, few enough that each gets a meaningful send count. The variant
  count and per-variant send volume are account decisions
  (`accounts/<slug>/context/scoring-model.md`); the reasoning is that each variant needs
  enough sends that "zero interested replies" is evidence rather than noise, and the total
  must stay inside the account's sending capacity.
- The winner is defined by **interested replies per send** — a yield, not a feeling. The
  account sets its yield bar; the reasoning is to work backward from deal economics: what a
  meeting is worth against what a send costs in list burn and domain reputation.
- Once a variant clears the bar: promote it, and only *then* A/B the secondaries — subject
  line, CTA, personalization depth, creative format — to compress the yield further.
- Once yield is known, infrastructure sizing becomes arithmetic: replies needed → sends
  needed → mailboxes and domains needed (`playbooks/deliverability-and-warmup.md`).

**Doctrine note (conflict C1, `docs/lineages.md`).** The fixed-slot template above and the
kit's PVP standard (`docs/standards.md`) are **parallel copy doctrines from different
lineages, and the conflict between them is recorded, not resolved.** By PVP's own test the
template is a pitch — deliberately, because it optimizes a different regime: yield discovery
at volume rather than per-message value delivery. A tier split (this template for the broad
market, PVP for the researched head of the list) is one **proposed** reconciliation — an
account may adopt it in its own files, but core has not settled it. What IS settled: the two
doctrines are never blended inside one campaign.

---

## Stage 5: AI Personalization

**Goal:** a personalized first line for every row — produced cheaply, expected to matter
marginally.

The uncomfortable, load-bearing fact: **personalization is not what drives results.** The
value proposition and the list drive results; personalization earns the read. So the rule for
this stage has two gates: personalize only if it is **cheap** and only if it is **fast to
build**. If a personalization idea fails either gate, skip it — the test in Stage 4 will not
notice the difference, and the budget is better spent on another value proposition.

When stuck for an angle, work down this schema — five repeatable patterns, each generable at
scale from data already in the table:

| Pattern | Mechanism |
|---|---|
| **Reference how the list was built** | Name the observable fact that put them on the list — the platform they run on, the directory they're in. Honest, specific, and free: the data already exists in the mapping columns |
| **Pose the problem as a question** | Ask about a cost or risk the ICP predictably carries — a question they recognize as *their* question |
| **Point at comparable companies** | Note what similar companies (same platform, same model, same size band) are doing that they are not — the comparison does the persuading |
| **Name the absence** | The observable thing they *don't* have — no team for X, no presence on Y — when that absence is precisely what the account sells into |
| **Use proximity** | For local businesses: a nearby customer, landmark, or geography-specific observation. Needs operator input: the source material names this pattern without developing it — validate locally before scaling it |

Every pattern must survive the verification standard in `docs/standards.md`: a confidently
wrong personalized line is worse than no line. Generate from data actually in the row, never
from model guesswork.

---

## Stage 6: Deliverability & Send Setup

**Goal:** infrastructure that gets the tested message into inboxes — set up before launch,
not debugged after.

The durable home for infrastructure decisions is `playbooks/deliverability-and-warmup.md`
(domains, warmup, the free/safe/scaled tradeoff, decisions already made) and
`workflows/enrichment.md` (the standing setup rules applied during list build). Read those;
this stage adds only the send-hygiene checklist for the high-volume motion this workflow
feeds:

**Message hygiene — cold sends carry nothing but text:**
- No links in body or signature — links are the classic spam-filter trigger, and a cold
  first touch has no earned right to ask for a click
- No images, no video, no HTML formatting — plain text, in the signature too
- Short — the account sets its word cap; the reasoning is that filters and readers both
  punish long cold email, and the template in Stage 4 doesn't need length
- No spam-trigger vocabulary — run copy through a spam-word check before loading it
- Signature is a bare name — every extra element is another filter feature
- Do not track clicks (tracking rewrites links — see rule one); open tracking is a
  judgment call, worth having only while diagnosing subject lines

**Sending posture:**
- Every address is warmed before it carries campaign volume — warmup is measured in weeks,
  not days (verify current guidance from the sending platform)
- Per-address daily caps and ramp schedules, and the addresses-per-domain ceiling, are
  account values (`accounts/<slug>/ACCOUNT.md`); the reasoning is that a new address earns
  trust by behaving like a human, and humans do not send at machine volume from day one
- Only validated emails are enrolled — "valid" beats "catch-all," and the account's bounce
  ceiling (with the defaults and rationale in `playbooks/deliverability-and-warmup.md`)
  gates every batch
- SPF, DKIM, and DMARC configured on every sending domain — a technical requirement, not a
  preference (verify with a DNS-check tool before the first send)

One flag on a common tactic: high-volume senders sometimes omit the unsubscribe link to look
hand-written. Whether an unsubscribe mechanism is legally required depends on the account's
jurisdictions and message classification — that is an account-level compliance decision
recorded in `accounts/<slug>/ACCOUNT.md`, not a default this workflow sets. Suppression via
`accounts/<slug>/optouts.md` runs before every batch regardless.

---

## Where the numbers live

Every threshold this workflow needs — refinement cut lines, variant counts, per-variant send
volumes, the interested-reply yield bar, word caps, daily caps, bounce ceilings — lives in
`accounts/<slug>/context/scoring-model.md` or `accounts/<slug>/ACCOUNT.md`. This file holds
the reasoning for how to pick each one, never the value. Two accounts running this same
workflow with different numbers are both running it correctly.

---

## Related

- `workflows/campaign-build.md` — the signal-led motion; also the QA, launch, and
  iterate/retire machinery that this workflow's output feeds into
- `workflows/enrichment.md` — the enrichment waterfall and data-quality gates for Stage 3
- `workflows/enrichment-techniques.md` — cost model, API/webhook patterns, and the scraping
  patterns Stage 1 depends on
- `playbooks/deliverability-and-warmup.md` — the infrastructure under Stage 6
- `playbooks/channels/` — channel strategy for what runs on the finished list
- `docs/standards.md` — PVP, tiers, benchmarks, and the verification standard
