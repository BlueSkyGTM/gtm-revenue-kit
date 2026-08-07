# Signal Library

*Signals are observable events that predict pipeline conversion 30–90 days in advance. This library is the source of truth for all signal-based outreach. Every campaign in this repo traces back to at least one signal here.*

Last updated: 2026-07-12

*See example: `examples/sample-company/context/signal-library.md`*

---

## Signal Scoring Model

> **Point values live in `context/scoring-model.md` §3 (Intent) — not here.** Per-signal
> "Points" lines below are historical context for detection and decay only; where they disagree
> with the scoring model, the scoring model wins. One scoring authority, one home for values.

Accounts accumulate points as signals fire. Thresholds determine outreach intensity.

| Score | Tier | Action |
|-------|------|--------|
| 70–100 | Hot | Outreach within 24–48 hours, personalized to the specific signal(s) fired |
| 45–69 | Warm | Add to active sequence, referencing the general 2026 QBO price increase |
| 20–44 | Cool | Lower-touch sequence, general messaging |
| 0–19 | Cold | Log and monitor, no outreach yet |

---

## Spending_Score — moved

The per-SKU point map, bands, and normalization rules now live in
**`context/scoring-model.md` §1** — the single home for every scoring value. This library keeps
signal *definitions, detection methods, and decay rules*; it holds no point values.

---

## Tier 1 Signals — Act Immediately

*High predictive power. When a Tier 1 signal fires: outreach within 24–48 hours, personalized copy.*

### Signal: Existing QuickBooks Live / Expert Assisted Customer
**Category:** Technographic / Firmographic — directly in the lead data, no enrichment needed
**Points:** 40
**Source:** Airtable base "QuickBooks Lead Capture" → `Contacts` table → `Products` field
**Refresh cadence:** Static per record; re-check if the list is refreshed

**Definition:** The account's `Products` field contains a QuickBooks Live / Expert Assisted SKU — `QBLIVE_EXPERT_SERVICES`, `QBLIVE_ASSISTED`, `Intuit Expert Assisted`, `QuickBooks Live Assisted Incorp/Unincorp Taxes`, `QuickBooks Live Full Service Incorp Taxes`, `QuickBooks Live One Time Services Expert`, or a data-entry variant of these (`OBLIVE_*`, `QBOLIVE_*` — same SKUs, typo'd prefix). **477 of 863 records (55.3%) match this today.**

**Why it predicts fit:** This is the single strongest signal in the entire list — the account is *already paying Intuit* for done-for-you bookkeeping help, which means budget is proven and the pitch isn't "start outsourcing," it's "switch who's doing it." Every QuickBooks Live weakness in `context/competitor-radar.md` (inconsistent bookkeeper, 4–5 months behind, cleanup fees to fix their own errors) is a live objection-handler here, not a hypothetical one.

**Detection method:**
```
Filter Contacts table where Products field contains any of:
QBLIVE_EXPERT_SERVICES, QBLIVE_ASSISTED, Intuit Expert Assisted,
QuickBooks Live Assisted Incorp Taxes, QuickBooks Live Assisted Unincorp Taxes,
QuickBooks Live Full Service Incorp Taxes, QuickBooks Live One Time Services Expert
(and the OBLIVE_ / QBOLIVE_ typo'd variants of the same SKUs — the Products field
has known data-entry noise, worth normalizing before a full scoring pass).
Note: LIVE_SERVICES_PREMIUM (510 records, 59%) is excluded from this signal — it's
a separate, more ambiguous tag (likely a bundled support tier, not confirmed as a
bookkeeping SKU) and shouldn't be conflated with the clearly-named Live SKUs above.
```

**Message hook:** "Looks like you're already using QuickBooks Live for your bookkeeping — worth knowing you don't always get the same bookkeeper twice with that service. We're one person, every month, who actually knows your books."

---

### Signal: QBO Price Hike Impact (Plus / Advanced tier)
**Category:** Firmographic / Intent — directly in the lead data
**Points:** 35
**Source:** Airtable "QuickBooks Lead Capture" → `Contacts` → `Products` field (`QBO_PLUS`, `QBO_ADVANCED` tags); cross-referenced against 2026 Intuit pricing changes
**Refresh cadence:** Static per record (plan tier doesn't change often), re-check at renewal

**Definition:** The account's `Products` field shows `QBO_PLUS` (199 of 863 records, 23%) or `QBO_ADVANCED` (140 records, 16%) — the two tiers hit hardest by the Aug 1, 2026 QuickBooks price increase. **Verified figures (Jul 2026):** Plus rises $115→$140/mo and Advanced $275→$340/mo on Aug 1 (Essentials $75→$85; Simple Start $38 unchanged). Earlier scattered figures ("$90→$110", "$200→$250", "70%/83%") were wrong or stale and have been replaced. Re-confirm at quickbooks.intuit.com/pricing before quoting in a new context.

**Why it predicts fit:** A real, unavoidable cost increase already hit their monthly bill with no corresponding value they asked for — and unlike the industry-wide version of this signal, it's directly confirmed per-account from the lead data, not inferred.

**Detection method:**
```
Filter Contacts table where Products field contains QBO_PLUS or QBO_ADVANCED.
Directly queryable in Airtable — no external enrichment needed.
```

**Message hook:** "Noticed you're on QuickBooks Plus/Advanced — that's the tier that just took the biggest price jump this year. A lot of owners are realizing they're now paying more for the software than it'd cost to have someone actually do the books."

---

### Signal: Public Intuit Assist / AI Complaint
**Category:** Behavioral / Intent
**Points:** 40
**Source:** Manual social listening — QuickBooks Community forum, Reddit (r/QuickBooks, r/smallbusiness, r/Bookkeeping), G2/Trustpilot reviews, X/Twitter mentions
**Refresh cadence:** Weekly sweep during active campaign

**Definition:** The account owner or a staff member has posted a public complaint about Intuit Assist or QuickBooks' AI features — specifically: miscoded transactions, unauthorized/unwanted changes to records, unreliable reports, or inability to turn AI features off.

**Why it predicts fit:** This is a direct, first-person expression of the exact pain the service solves — trust in automated bookkeeping has broken down for this specific account, and they've said so publicly. Far stronger than an inferred signal.

**Detection method:**
```
Search QuickBooks Community forum, Reddit, and review sites for company name
(or owner name) + keywords: "Intuit Assist," "AI," "miscoded," "wrong,"
"can't turn off," "changed without," "unreliable report."
Manual process today — no automated social listening tool confirmed in stack.
```

**Message hook:** "Saw your post about QuickBooks' AI changing transactions without asking — that's the exact reason people come to us. A human reads the numbers; nothing gets recoded behind your back."

---

### Signal: QBO Renewal Window Approaching
**Category:** Behavioral / Intent
**Points:** 30
**Source:** [inferred: billing/renewal date if known from discovery or account history]
**Refresh cadence:** Weekly

**Definition:** The account's QuickBooks Online annual renewal or next billing cycle falls within the next 30–60 days.

**Why it predicts fit:** This is the moment the price increase becomes a real, felt decision rather than an abstract complaint — the highest-urgency window to have the outsourcing conversation before they renew on autopilot.

**Detection method:**
```
[inferred: renewal date not typically public — this would come from discovery
conversation or prior billing history if account was referred/known. Flag as
a signal to capture during first contact, not a pre-outreach filter.]
```

**Message hook:** "Your QuickBooks renewal is coming up in the next few weeks — before you pay that increase again, worth 15 minutes to see what it'd cost to have someone just handle it instead?"

---

## Tier 2 Signals — Add to Active Sequences

*Moderate predictive power. Use to prioritize within existing sequences or trigger lighter outreach.*

### Signal: Long Customer Lifetime (2+ years)
**Category:** Firmographic — directly in the lead data
**Points:** 20
**Source:** Airtable "QuickBooks Lead Capture" → `Contacts` → `Customer Lifetime` field

**Definition:** The account's `Customer Lifetime` field shows 2+ years as a QuickBooks customer. Distribution across the list: 1 year (163), 2 years (105), 3 years (48), 11 years (36), plus a long tail out to 11+ years — roughly 40% of the list has 2+ years of tenure.

**Why it predicts fit:** Longer tenure means the cumulative QBO price increases since 2021 (repeated and well documented; confirm current figures before quoting any number) are fully felt, not just this year's jump — the pain compounds with time on the platform.

---

### Signal: "Upgrader" Customer Type
**Category:** Behavioral — directly in the lead data
**Points:** 20
**Source:** Airtable "QuickBooks Lead Capture" → `Contacts` → `Customer Type` field (value: `upgrader`)

**Definition:** The account's `Customer Type` field is tagged `upgrader` (72 of 863 records, 8%) — meaning they recently moved to a higher QBO plan tier.

**Why it predicts fit:** An upgrade is a fresh, recent price-increase event on top of whatever base plan increase already applies — this account just committed to paying more, making the cost conversation timely. Note: most `Customer Type` values in the list (`nttf` – 371 records, `dtm` – 285 records, plus scattered variants) are unlabeled internal codes with unconfirmed meaning — don't build messaging on them until confirmed. `upgrader` is the one value with a clear, actionable meaning.

---

### Signal: Hiring for Bookkeeping/Admin Role
**Category:** Organizational
**Points:** 20
**Source:** Job posting sites (Indeed, LinkedIn), manual check

**Definition:** The business has an open job posting for a bookkeeper, accounting clerk, or admin role with "QuickBooks" listed as a requirement.

**Why it predicts fit:** They've recognized the bookkeeping workload is too much for the current setup and are actively trying to solve it — worth testing an outsourcing alternative before they complete a hire.

---

### Signal: QuickBooks Payroll Active
**Category:** Technographic — directly in the lead data
**Points:** 15
**Source:** Airtable "QuickBooks Lead Capture" → `Contacts` → `Products` field (`PR_CORE`, `PR_PREMIUM`, `PR_ELITE`, `PR_CONTR`, or `Intuit QuickBooks Workforce *` tags)

**Definition:** The account is running QuickBooks Payroll in addition to the base QBO subscription. Roughly 260 of 863 records (30%) carry a payroll tag.

**Why it predicts fit:** Payroll is an additional recurring cost stacking on top of the base subscription increase, deepening the overall price pain and adding a second service line (payroll) we can bundle into the offer.

---

## Tier 3 Signals — Monitor

*Weak signals on their own. Valuable in combination with Tier 1 or 2 signals.*

- No internal bookkeeper/accountant role visible on team page or LinkedIn (+10) — owner or generalist is likely doing books directly, meaning the pain is felt personally
- Business is 1–20 employees (+5) — baseline firmographic fit for the service model
- Account has `QBO_SIMPLE_START` or `QBO_ESSENTIALS` only, no Live/payroll add-ons (+5) — smallest, lowest-urgency segment (383 of 863 records, 44%), but still worth a lighter-touch sequence

---

## Signal Combinations

*Certain combinations of signals are stronger predictors than any single signal.*

| Combination | Combined Score | What it means | Action |
|-------------|----------------|---------------|--------|
| Existing QuickBooks Live Customer + QBO Plus/Advanced tier | +15 bonus | Already paying for done-for-you bookkeeping AND on the tier hit hardest by the 2026 price increase — proven budget plus maximum price pain | Highest-priority segment in the entire list — lead with the QB Live consistency angle, close with the price comparison |
| QBO Price Hike Impact + Public AI Complaint | +15 bonus (on top of individual scores) | Both budget pain and product-trust pain are active at once — the strongest possible entry point | Move to Tier 1 hot outreach immediately, reference both pain points directly in the first message |
| QBO Renewal Window + Hiring for Bookkeeping/Admin Role | +10 bonus | Urgency (renewal) plus active intent to solve the problem (hiring) — they're deciding between a hire and an alternative right now | Prioritize for immediate outreach with a direct cost comparison: outsourced monthly cost vs. a new hire's salary + benefits |

---

## White-Label Signals (firm campaign ONLY — see `context/tracks/white-label/icp-definition.md`)

*Apply to accounting/CPA firms, never to the Bounce SMB list. Detection is scrape/manual until Clay Audiences is live on the new account.*

### Tier 1 — act on sight
- **Hiring for delivery roles** (+40): open posting for bookkeeper / staff accountant / "CAS associate," QuickBooks in requirements. Detection: Indeed/LinkedIn search per screened firm. The purest capacity-constraint signal, and it decays fast — act within the posting window.
- **Waitlist / "not accepting new clients" language** (+35): on the firm site or GBP profile. Detection: site scrape during screening. Demand exceeds delivery, today.

### Tier 2 — sequence
- **ProAdvisor directory listing** (+20): QB-native practice, filterable by location/service. Detection: proadvisor.intuit.com scrape (the Layer-1 source doubles as a signal).
- **Seasonal proximity** (+15): Nov–Dec ("capacity for next season") and May ("never again" window). Calendar-driven, applies list-wide.
- **Firm growth mentions** (+10): new office, merger, partner announcement — client load grows before delivery staff does.

### Suppression (white-label specific)
- Firm is an existing Fenton white-label partner → suppress cold outreach
- Firm's clients overlap the Bounce list → channel-conflict review before ANY outreach (never pitch an SMB direct and its firm simultaneously)

---

## Migration-Intent Signals (the MIGRATION offer track — same Bounce buyer, different offer)

*Added 2026-07-27. These apply to the **same** Bounce SMB accounts, but they predict a
different first transaction: leaving QuickBooks rather than hiring help inside it. Offer
eligibility and the motion-conditional spend weight live in `scoring-model.md` (§2, §4); this
section holds definitions, detection, and decay only. **Never mix these with the bookkeeping
track's copy** — the two offers have opposite mechanisms (`positioning.md` promises no
migration; this offer is the migration).*

**The eligibility gate that governs the whole class — read before any send.** A record is
eligible for migration outreach **only after its own first bill at the new price has landed.**
The 2026-08-01 increase reaches each subscriber on their next billing date, so eligibility is
per-account and rolling, not campaign-wide. Before that date the message is a deadline warning,
which the standing no-urgency rule (`positioning.md` → Copy Rules, 2026-07-25) forbids; after
it, the message is a statement of fact about something that already happened to them. Detection:
tenure + billing-cycle inference from enrichment, or the reply itself confirming it.

### Tier 1 — act within 48h of eligibility
- **`qbo-advanced-spend`** — account holds QBO Advanced. The largest dollar increase
  ($275 → $340) and the widest gap against Xero Established ($90). Detection: existing SKU tags
  in `Products`.
- **`user-cap-pressure`** — headcount/team size implies more than 5 users, which forces
  Advanced on QBO while Xero includes unlimited users on every plan. The structural argument
  that has nothing to do with the increase. Detection: employee count from enrichment.

### Tier 2 — sequence
- **`qbo-plus-spend`** — QBO Plus ($115 → $140), the largest affected population.
- **`multi-entity`** — more than one company file means more than one subscription, so the
  increase multiplies. Detection: enrichment / site evidence of multiple entities.

### Routing signal — negative migration weight (reclassified 2026-07-27, Addendum A)
- **`payroll-active`** — QuickBooks Payroll present. **No longer `complexity+`** (that was the
  parent handoff's classification; the addendum overrides it). The verified economics: Xero
  Growing + Gusto ≈ $134/mo at 5 employees vs QBO Essentials + Payroll ≈ $165/mo — Xero usually
  cheaper, so payroll is never a blocker, but the margin narrows enough at small headcounts
  that switching stops being obviously worth the disruption. Those accounts are **stayers**:
  `migration_fit` takes a **−6 weight** (`scoring-model.md` §2a) and they route toward the
  bookkeeping offer. Two things survive the reclassification unchanged: payroll YTD rebuild is
  skilled, billable *delivery* work when a migration does proceed (pricing context, not
  targeting), and any migration-track outreach that reaches a payroll account still carries the
  cost comparison — a pro-Xero point, never a "this makes it hard" line.

### Migration-track suppression (in addition to the standing rules below)
- **First new-price bill has not landed yet** → not eligible, full stop (the gate above).
- Account is on **Simple Start / Solopreneur / Ledger** → unaffected by the increase; the
  migration hook is factually false for them.
- Account already **moved off QuickBooks** → the standing rule removes them anyway.
- **Reachability `dead`** → same gate as every other send (`scoring-model.md` §6).

### Decay
Unlike the bookkeeping signals, the migration trigger is **dated per account**: freshness runs
~30 days from that account's first new-price bill, not from campaign start. The plan-tier
signals themselves (Advanced/Plus/user-cap) are standing states and do not decay — they are
facts about the account, not events.

---

## Suppression Rules

*Signals that should pause or cancel outreach regardless of score.*

- Account is an existing **Fenton client** (already buying from us) → suppress all outreach. This keys on *Fenton's* client list, NOT on paying Intuit for Live/Expert Assisted — an Intuit Live payer is our strongest positive signal (+15 in scoring) and a prime target, never suppressed for it. (Fenton has zero clients today, so this suppresses nothing yet; it activates as conversions land.)
- Contact has explicitly declined or asked not to be contacted → suppress permanently
- Account has moved off QuickBooks entirely → remove from active list, doesn't fit current signal set
- Account is an accounting/CPA firm → suppress from current small-business motion, flag separately for the future white-label list

---

## Signal Decay

Signal scores reduce over time. A signal from 150 days ago is not the same as one from 10 days ago — score them differently.

| Signal age | Score multiplier |
|------------|-----------------|
| 0–30 days | 100% |
| 31–60 days | 75% |
| 61–90 days | 50% |
| 91–180 days | 25% |
| 180+ days | 0% (signal expires) |

Note: "QBO Price Hike Impact" is an exception — it's tied to a plan tier, not a dated event, so it doesn't decay the same way. Re-evaluate it only if the account's plan tier changes or Intuit announces a further increase.

---

## Signal Performance Log

*Track which signals are actually generating pipeline. Update after every campaign.*

| Signal | Outreach sent | Replies | Meetings | Pipeline | Notes |
|--------|--------------|---------|----------|----------|-------|
| Existing QuickBooks Live / Expert Assisted Customer | | | | | 477 of 863 leads match (55.3%) — campaign not yet launched |
| QBO Price Hike Impact (Plus/Advanced) | | | | | 339 of 863 leads match (39%) — campaign not yet launched |
| Long Customer Lifetime (2+ years) | | | | | ~40% of list — not yet launched |
| "Upgrader" Customer Type | | | | | 72 of 863 leads (8%) — not yet launched |
| Public Intuit Assist / AI Complaint | | | | | Requires manual social listening, not yet run against this list |
| QBO Renewal Window Approaching | | | | | Renewal date not in current Airtable schema — capture during first contact |
