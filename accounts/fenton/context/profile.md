# Company Profile

*High-level context about your company, product, and GTM motion. This is the first thing Claude reads when working on anything in this repo.*

*See example: `examples/sample-company/context/profile.md`*

---

## The Company

**Name:** Fenton Bookkeeping (formerly doing business as "Fenton Tax & Bookkeeping Services" — fentontaxandbookkeepingservices.com still redirects to the current site)
**Founded:** [inferred: not disclosed publicly — founder cites 30+ years of accounting experience, business itself may be younger]
**HQ:** [inferred: Southern California — Riverside County area code (951) on contact line]
**Website:** fentonbookkeeping.com (fentontaxandbookkeepingservices.com redirects here)

**What we do:**
We do QuickBooks bookkeeping — cleanup, ongoing monthly bookkeeping, and payroll — for small business owners who are done managing their own books. One experienced human (QuickBooks Certified ProAdvisor, 30+ years in the field) does the work, reconciles it, and stands behind it. No junior staff rotation, no AI guessing at your transactions.

**What makes us different:**
Right now, our edge is timing and trust: QuickBooks Online is raising prices again on 2026-08-01 (Essentials $75→$85, Plus $115→$140, Advanced $275→$340) on top of an earlier 2026 rise, and has pushed a forced AI layer (Intuit Assist) that a lot of small business owners don't trust with their books. We're the alternative — a human who reads the numbers instead of a subscription that keeps getting more expensive and less predictable.

---

## Product

**Core service:** Outsourced QuickBooks bookkeeping (human-delivered, not software)

**Key capabilities:**
- QuickBooks Cleanup — fixing miscoded transactions, reconciling backlogs, correcting DIY or AI-introduced errors
- QuickBooks Bookkeeping — ongoing monthly reconciliation and bookkeeping
- QuickBooks Payroll — payroll processing and management inside QuickBooks

**Pricing model:** Monthly retainer plus a one-time cleanup fee, **quoted case-by-case, never published.** Confirmed as deliberate 2026-07-25: no blanket rate card exists because every book arrives in a different state, and the quote is Miriam's conversation with the customer. See the ACV note below for the internal planning figure.
**Free tier or trial:** [inferred: No — services business, not software]

**What matters for the GTM conversation:**
- Every target account is already a paying QuickBooks Online subscriber — no platform migration required, which lowers the switching cost for them versus adopting a new tool.
- QuickBooks Certified ProAdvisor credential is the trust signal that substitutes for case studies/logos, which the business doesn't yet have publicly.

---

## GTM Motion

**Primary motion:** Direct outbound to a static list
**Lead source:** Airtable base "QuickBooks Lead Capture" → `Contacts` table — 863 records (company, contact, email, phone, city/state, and each account's actual QuickBooks product mix). Referred to as "the 1,000-lead list" but the confirmed live count is 863.
**Typical deal flow:** Outbound (phone/email) → discovery of current QuickBooks pain (price, AI reliability, or QuickBooks Live dissatisfaction) → cleanup engagement or direct-to-monthly bookkeeping → close
**Pricing is case-by-case by design. There is no blanket rate card, and that is deliberate.** Every book arrives in a different state, so the quote is a conversation Miriam has directly with the customer. Do not publish numbers, do not put them in copy, and do not treat the absence of a rate card as an unresolved gap — earlier notes in this repo made that mistake.

**For internal planning only:** assume industry standard at the high end, ~**$14,400/year** ongoing (~$1,200/mo) and ~**$3,000** for a one-time cleanup (operator direction, 2026-07-25). Use it for funnel maths and for judging what a channel is worth. Never as a quote.

There are **no past contracts**, so that figure is a planning assumption rather than observed data. The wider industry band for solo/small-practice bookkeeping serving sub-20-employee businesses runs roughly $3,600–$14,400/yr ongoing plus $500–$3,000 cleanup, and planning at the top of it is a choice. Two things to keep in view:

- Any figure derived from it inherits the assumption. At the bottom of the band the same funnel produces roughly a quarter of the revenue.
- It is **revenue, not margin.** Miriam's delivery hours are unpriced, and at roughly 10-15 hrs/client/month on cleanup-heavy work, her capacity is the real constraint. That is why retainer slots are treated as scarce and why cleanup-only work is welcome (see `_archive/kit-HANDOFF.md` → Decisions Locked).
**Sales cycle:** [inferred: short — single decision-maker (the owner), likely days not weeks]
**Expansion motion:** [inferred: cleanup engagement → upsell to ongoing monthly bookkeeping → upsell to payroll]

---

## Team

**GTM team size:** [inferred: 1–2 people — Miriam (delivery) plus whoever is running this outbound motion]
**Founder / Lead bookkeeper:** Miriam [Fenton] — QuickBooks Certified ProAdvisor, 30+ years in bookkeeping, payroll, reconciliations, audit support, and corrective cleanup work
**Key GTM contacts:**

| Name | Title | Owns |
|------|-------|------|
| Miriam [Fenton] | Founder / Lead Bookkeeper | Service delivery, QuickBooks expertise |
| [You] | GTM | Outbound to the 1,000-lead list, signal-based targeting |

---

## Current GTM Priorities

*Update monthly. Shapes how Claude prioritizes tasks.*

**This quarter's focus:**
1. Work the existing list of ~1,000 leads — QuickBooks Online subscribers, targeted specifically because they're likely feeling the 2026 price hikes and/or Intuit Assist AI reliability problems
2. Convert on the "unhappy QuickBooks subscriber" signal before white-label (accounting-firm) positioning becomes the focus
3. Build proof points (first reference customers, testimonials) from this initial push — currently the site has none

**Key campaigns active:**
- Outbound to the 863-record Airtable lead list — signal: QBO price increase impact + AI/Intuit Assist dissatisfaction + existing QuickBooks Live incumbency (55.3% of the list is already a QuickBooks Live/Expert Assisted customer — see `context/signal-library.md`)

**Blockers:**
- No CRM for outreach tracking beyond the Airtable lead table itself — sequencing, reply tracking, and outcome logging are likely manual today. [inferred — confirm actual outbound tooling in refinement]
- No public pricing, case studies, or reference customers yet, which limits proof points in outbound copy
- `Products` field in the lead list has data-entry noise (typo'd SKU variants) — worth a normalization pass before a full scoring run, see `context/icp-definition.md`

---

## Market Context

**Category:** Outsourced small-business bookkeeping (QuickBooks-specialist)
**Market size:** [inferred: not sized — highly fragmented local/independent bookkeeper market plus a handful of national outsourced-bookkeeping brands]
**Key trends driving demand:**
- Intuit raised QuickBooks Online prices twice in 2026: an earlier phase, then again effective **2026-08-01** (Essentials $75→$85, Plus $115→$140, Advanced $275→$340; Simple Start / Solopreneur / Ledger unchanged, new customers price-protected 6 months). Cumulative drift since 2021 is much larger than any single step. *Subscriber-count claims ("3M+ on Plus") are unverified and banned from any use — see the banned-figures list in the migration debrief.*
- Intuit Assist (QBO's AI layer) has drawn sustained complaints about miscoded transactions, unauthorized changes to records, and unreliable reports — with no easy opt-out, pushing trust-sensitive small business owners to look for a human alternative
- Bench Accounting — one of the largest outsourced-bookkeeping brands — shut down abruptly in December 2024, leaving 12,000+ businesses without access to their books; its 2026 relaunch under Employer.com carries a D- BBB rating and ongoing service complaints, which has left a trust gap in the outsourced-bookkeeping category that a stable, human-led alternative can point to

**Primary competitors:**
| Competitor | Their strength | Our edge |
|------------|---------------|----------|
| Status quo (DIY in QuickBooks) | Zero switching cost, "already paying for it" | We remove the price hikes and the AI-error cleanup work entirely |
| QuickBooks Live (Intuit's own bookkeeping add-on) | Bundled with QBO, brand trust of Intuit | Same company causing the price/AI pain; reviews cite bookkeepers 4–5 months behind and a different person every month — we offer one consistent, experienced bookkeeper. **This isn't hypothetical — 55.3% of our own lead list is already a QuickBooks Live customer.** |
| Bench Accounting | Brand recognition, national scale | Reliability trust gap post-shutdown (D- BBB rating in 2026); we're a known, accountable single provider |

---

## Reference Customers

*Customers Claude can reference in outreach (with permission) or use as proof of ICP fit.*

| Customer | Industry | Why they bought | Can reference publicly? |
|----------|----------|----------------|------------------------|
| [None yet] | — | — | — |

*No public case studies or named customers yet. This is the first gap to close — capture and log reference customers here as the 1,000-lead campaign converts.*
