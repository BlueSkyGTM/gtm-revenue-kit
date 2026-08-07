# Scoring model — instance values

*Every number, SKU, threshold, and segment definition the scoring mechanism reads. The
**mechanism** lives in `../skills/icp-scoring/SKILL.md` and contains no values; this file
contains no mechanism. Swap this file (with the rest of `context/`) and the same skill scores a
different company.*

Last updated: 2026-07-27 · Calibration state: **zero reply data — every value is a hypothesis**

---

## 1. Spend input — the per-SKU point map

The Spending_Score is a deterministic per-SKU point sum over the account's `Products` field.
Reverse-engineered from Clay's export, validated 99.2% exact against 613 Clay-scored leads.
Typo/prefix variants (`OBO_`, `OBLIVE_`, `QBOLIVE_`) normalize to the same SKU.

| Points | SKUs |
|--------|------|
| 40 | QBO Advanced · Full-Service Bookkeeping · Payroll Elite · QuickBooks Live Full Service |
| 22 | QBO Expert Services · QBO Full Service |
| 20 | QBO Plus |
| 15 | Payroll Premium · Time / TSheets Elite |
| 10 | QBO Essentials |
| 5 | Simple Start · Live Services Premium · Live Assisted · Live Expert Services · Payroll Core · Live Expert Cleanup Lite |
| 2 | Contractor Filing · Money (any) · Payroll Contractor · Inventory Standard · Sales Tax Essentials |
| 1 | Bill Pay (Basic / Premium / Elite) |

**Bands:** Standard 10–14 · Mid-High 15–39 · High 40+.

## 2. Fit values (feeds the skill's Fit component, 0–40)

**Spend-fit curve (0–24) — sweet-spot, NOT monotonic.** Peak at mid-spend on the untested belief
that mid-spend converts best on a cleanup-first offer. The single tuning knob for that hypothesis.

| Spending_Score | Fit points |
|---|---|
| 12–29 | 24 (peak) |
| 30–49 | 21 |
| 10–11 | 13 |
| 50–70 | 16 |
| 71+ | 10 (down-weighted preference — never a cap; size is not a disqualifier) |
| unscored | 6 |

**Offer-fit (0–10):** Segment A (holds a human-service SKU — see §4) = 10 · Segment B (QBO only)
= 6 · not on QuickBooks = 0 (anti-ICP).

### 2a. Motion-conditional spend weight (added 2026-07-27)

**Two offers now run against the same beachhead, and spend predicts them differently.** The
curve above is the **bookkeeping** motion's: a sweet-spot shape, because willingness to hire a
bookkeeper peaks at mid-spend and the largest accounts tend to have someone already. The
**migration** motion inverts that logic — the pain *is* the bill, so it rises monotonically with
tier, and the biggest spender has the most to save.

One scoring authority still holds: the same `icp-scoring` skill computes both, reading whichever
column the motion names. This is a second **weight**, never a second model.

| Spending_Score | Bookkeeping fit (0–24) | Migration fit (0–24) |
|---|---|---|
| 71+ | 10 (down-weighted preference) | **24** (Advanced-tier spend, widest Xero delta) |
| 50–70 | 16 | **21** |
| 30–49 | 21 | **17** |
| 12–29 | 24 (peak) | **12** |
| 10–11 | 13 | **7** |
| unscored | 6 | 6 |

**Named columns (canonized 2026-07-27 from Addendum A of the strategy handoff):** these are
`bookkeeping_fit` and `migration_fit` — two computed columns from THIS one model, applied by the
one `icp-scoring` skill. The addendum's phrase "replace the single-score model" means exactly
this structure and nothing more; a second scorer anywhere else remains a Hard-Rule violation.

**`migration_fit` has components beyond spend** (the spend column above is its largest input,
not its whole). All values are hypotheses, zero reply data:

| Component | Points | Detection |
|---|---|---|
| Tier-increase magnitude | 0–24 (the migration column above) | `Spending_Score` / plan tier |
| **User-cap pressure** | 0–10: headcount implies >5 seats = 10 · 4–5 seats = 6 · ≤3 = 0 | enrichment headcount. Weighted deliberately high — forced-Advanced ($4,080/yr vs Xero Growing $660) frequently exceeds the increase itself |
| Multi-entity multiplier | +4 per additional QBO company, cap +8 | enrichment / discovery |
| Payroll-active | **−6 (negative)** | `PR_*` / `Workforce` / `Payroll` SKUs. Small-headcount payroll narrows the Gusto margin enough that switching stops being obviously worth the disruption — those accounts are **stayers** and route to bookkeeping. Payroll YTD rebuild stays a billable *delivery* fact when a migration proceeds; it is no longer a targeting positive |
| Serviceability | 0–6 (same as bookkeeping) | same |

**The two fits are NOT inversely related.** An Advanced account with eight users is high on
both — a heavy bill AND an excellent bookkeeping client. Never model them as a tradeoff.

**Both columns are hypotheses with zero reply data** (§8's standing caveat). The migration
column is additionally untested by anyone — no reply, no engagement, no delivered file. The
per-offer results scaffold in the campaign folder is what will move these numbers; until then,
treat a migration Priority as a sort order, not a probability.

**Offer eligibility gates the score, it does not shade it.** An account ineligible for the
migration offer (bill not yet at the new price, unaffected plan tier, already off QuickBooks)
has no migration Priority at all — the same way reachability `dead` has no send, regardless of
rank. Predicates: `signal-library.md` → Migration-Intent Signals.

**Serviceability (0–6):** US + active subscription baseline 2 · timezone schedule-fit
(PT/MT/CT/ET incl. AZ) +4. Schedule-unfit (HI/AK/territories) = lower score, never removed.

## 3. Intent signals (feeds Intent, 0–30; cap at 30)

| Signal | Points | Dated? |
|---|---|---|
| Holds a human-service SKU (Live/Expert/Full-Service — the §4 list, NOT the decoy) | 15 | no — standing state |
| Public Intuit Assist / AI complaint, found and linkable | 12 | yes — decays per `signal-library.md` |
| On QBO Plus or Advanced (2026 price-hike tiers) | 8 | no |
| Renewal window inside 30–60 days | 6 | yes |
| QuickBooks Payroll stacked | 4 | no |
| Tenure ≥ 2 years, or `Customer Type` = `upgrader` | 4 | no |

Proven intent is deliberately credited in both Offer-fit and here — that double credit is how a
Live payer survives the spend curve.

## 4. Motive segments (categorical — selects the MESSAGE, never the rank)

From the 2026-07-26 segmentation audit, **canonized as the live `Motive_Segment` field written
to Airtable 2026-07-27 (operator decision: broad predicate)** — 862 records, verified by
re-query. The broad predicate extends the audit's strict five-token rule three ways, all
consistent with §1's normalization stance: typo/prefix variants (`OBLIVE_`, `QBOLIVE_`)
normalize to their SKU; the July import's human-readable names count (`QuickBooks Live
Assisted`, `Live Experts Service Assisted`, `One Time Services Expert`); and **Live tax-assist
SKUs count as switcher** — someone paying Intuit for human *tax* help has accepted paying
Intuit for a human, which is the premise the switching sale needs. Strict-core count for
continuity with the audit: 452. Predicates are authoritative; counts are snapshots.

| Segment | Definition (checkable — matches the live field) | Count | First-line frame |
|---|---|---|---|
| **Switcher** | holds ≥1 human-service SKU: `QBLIVE_EXPERT_SERVICES`, `QBLIVE_ASSISTED`, `Intuit Expert Assisted`, `FULL_SERVICES_BOOKKEEPING`, `Full Service` — incl. normalized variants, the July human-readable names, and Live tax-assist SKUs | 505 | switching sale — "same service, one person, less" |
| **DIY** | QBO SKU present, none of the above | 335 | conversion sale — "what you cannot see in your own books" |
| **No-data** | `Products` blank or unparseable | 22 | do not message; enrich or exclude |

Cross-cutting overlays (a record can hold both a segment and an overlay):

| Overlay | Definition | Count | Effect |
|---|---|---|---|
| **Payroll-stacked** | holds `PR_CORE` / `PR_PREMIUM` / `PR_ELITE` / `PR_CONTR` / `Workforce` / `Payroll` | 283 | statutory-deadline message thread available |
| **New customer** | `Customer Lifetime` ≤ 2 months (days, "1 month", or "2 months" — the live `Suppress_Price_Fatigue` field) | 145 | see suppressors, §5 |

**Decoy:** `LIVE_SERVICES_PREMIUM` appears on 95% of records and co-occurs with real SKUs — a
bundled support tier, **never** evidence of a human service. A naive `contains "LIVE"` filter
overstates the switcher segment by 83%.

### 4a. Offer eligibility (added 2026-07-27) — which first transaction is on the table

Motive segments answer *what to say*. Offer eligibility answers *which offer may be said at
all*. One account can be eligible for both, and then Priority under each motion's weight (§2a)
decides which track it enters first.

| Offer | Eligible when | Ineligible when |
|---|---|---|
| **Bookkeeping** (the standing motion) | on QuickBooks, reachability `verified`, not an existing client | off QuickBooks · anti-ICP · reachability `dead` |
| **Migration** (added 2026-07-27) | on an affected plan (Essentials / Plus / Advanced) **AND its first bill at the new price has landed** **AND** reachability `verified` | unaffected tier (Simple Start / Solopreneur / Ledger) · bill not yet repriced · already off QuickBooks · reachability `dead` |

**The two offers must never appear in the same message.** Their mechanisms are opposites — the
bookkeeping offer promises nothing changes but who does the work; the migration offer moves
them to another platform. An account eligible for both gets one track, not a blend
(`positioning.md` mechanism vs. the migration track in `messaging-house.md`).

### 4b. The routing matrix (canonized 2026-07-27, Addendum A) — which offer leads

Routing comes from the **pair** of fit scores, never from either alone:

| | High `bookkeeping_fit` | Low `bookkeeping_fit` |
|---|---|---|
| **High `migration_fit`** | **Paid diagnostic first** — resolves stay/leave at the client's expense and lands revenue either way. These are the best accounts on the list; route them first | Migration offer — conversion + archive; the books may go elsewhere |
| **Low `migration_fit`** | Bookkeeping offer — the majority, and the recurring prize | Tier 3/4 nurture, bookkeeping copy |

**The high/high cell is the key insight: the diagnostic is a router, not just a product.** Its
deliverable answers "should you move?" and a *stay* answer is a complete finding (plan
right-sizing, pre-year-end cleanup list, what to fix in the current file) that ends inside a
bookkeeping conversation. Cover-page line, required: *"We work in both systems. We'd bill you
either way, so the finding follows your books, not our preference."*

**Nothing is excluded by routing.** Low/low stays a bookkeeping prospect at Tier 3/4. The
migration motion adds a lane; it removes none. And the routing composition matters for testing:
the 141 test batch is Segment B (low scores ascending), so **the high/high diagnostic play
lives in rollout-A, not the test bed.**

Where this lives when it goes live: Airtable fields beside `Motive_Segment` — both fit columns
plus the routing value, written the same way (predicate documented here, value written once,
verified by re-query). The eligibility field `Repriced_Bill_Confirmed` was created 2026-08-03
(see §4a); **the fit and routing columns are still not created and wait on the principal's
test decision.**

**The eligibility field exists as of 2026-08-03: `Repriced_Bill_Confirmed`**
(`fld2bhMZHwTnp4X9b`, date, on the Contacts table beside `Motive_Segment`) — created per the
migration red-team's F6, which held that the no-urgency rule is only real as a re-queryable
field. Its contract: the field carries the **date the account's own repriced bill was verified
to have landed**, or it carries nothing; **empty = ineligible**. A migration send list must be
**re-queried against the field at send time** — never built from a cached export — and no
session writes a value without verification evidence.

**"Its first bill at the new price has landed" is a fact to establish, not a date to assume.**
The increase took effect 2026-08-01 (verified 2026-08-03), and existing subscribers see it on
their **next billing date on or after** that day. Therefore:

- **Eligible accounts remain zero until verified per account.** The pool fills in a rolling
  trickle from mid-August and is not complete until late September; every entry into it is a
  written `Repriced_Bill_Confirmed` date, not an assumption.
- **Elapsed time is not evidence.** "30 days have passed" does not mean their bill repriced —
  annual plans, mid-cycle dates, promotional periods, and the 6-month new-customer price
  protection all break the inference. The field records a *verified* repricing, or it records
  nothing; where verification is impossible, the honest value is `unknown`, and `unknown` is
  not eligible.
- **The rolling-freshness idea stays internal.** It may rank the queue; it must never reach copy
  as "while this is fresh" or "your window" — that is the deadline pressure the no-urgency rule
  bans, re-entering through the back door.

## 5. Timing suppressors (per message-class, never per record)

| Condition | Suppresses | Still eligible for | Re-approach |
|---|---|---|---|
| Tenure ≤ 2 months (the `Suppress_Price_Fatigue` field) | `price-fatigue` class (cumulative-increase claims, "years of price rises") | onboarding-cleanup angle, payroll-deadline thread | first renewal |
| Renewal > 11 months out (annual plans) | renewal-urgency class | everything else | 60 days before renewal |

A wrong message is worse than a weak one: a 2-month customer told they absorbed years of
increases replies "I just started using this" — the claim is factually false for them.

## 6. Reachability states (gate — a score never sends)

| State | Meaning | Send? |
|---|---|---|
| `verified` | site resolves, business matches the record, contact route live, checked ≤ 30 days ago | yes |
| `unverified` | not yet checked | only after verification for head-of-list sends |
| `dead` | domain gone, rebrand out of the work, "grand opening" (no capacity pain), bounced hard | no — archive with cause |

Evidence for the gate: 3 of WL-1's top 20 scored 90–100 and were dead (rebrand / grand opening /
dead domain) — a 15% failure rate at the head. Verification is mandatory for any slice getting
the research-brief treatment; batch sends verify at minimum the domain resolves.

## 7. Tier bands and rollout (unchanged from v1)

| Priority total | Tier | Action |
|---|---|---|
| 80–100 | 1 | Tier-1 sequence; top 20 by score get the research hand-brief |
| 60–79 | 2 | Signal-triggered sequence within 48h |
| 40–59 | 3 | Automated sequence (test bed lives here) |
| 20–39 | 4 | Monitor; re-score after enrichment |
| 0–19 | Exclude | off-motion |

Rollout order = priority descending · test bed = ascending · tie-break: signal score, then
offer-fit (A over B), then email A→Z (deterministic).

## 8. Calibration log

| Date | Pattern observed | Value changed |
|---|---|---|
| 2026-07-13 | Baseline sweet-spot hypothesis set; zero reply data | — |
| 2026-07-27 | v2 split: values extracted here from the skill and `signal-library.md`; motive/suppressor/reachability added from the segmentation audit | structure, not weights |
| 2026-07-27 | §4 canonized to the broad live predicate (505/335/22, operator decision). Score-drift check on the 53 broad-only switchers: **47 were already A-scored** (v1's normalization caught the variants), 5 unmatched-but-A by score shape, **1 true flip re-scored**: `ghoshsnacks@gmail.com` 34 → 57 (offer 12→20, human-service signal 0→15; Tier 4 → 3). Verified by re-query. | one record's `ICP_Score` |
| 2026-07-27 | Migration offer track added: §2a motion-conditional spend weight (migration reads monotonic where bookkeeping reads sweet-spot), §4a offer eligibility. Nothing re-scored — the migration column is unused until the principal approves the test, and no Airtable field exists yet. | new weight column + eligibility predicate, no values changed |
| 2026-07-27 | Addendum A canonized: §2a became the two-fit model (`bookkeeping_fit` unchanged; `migration_fit` gains user-cap 0–10, multi-entity +4/+8, **payroll −6** — reclassified from `complexity+` per the addendum, overriding the parent handoff); §4b routing matrix added (high/high → paid diagnostic). All hypothesis values, zero reply data. | migration_fit components + routing; bookkeeping values untouched |
| 2026-08-03 | Eligibility field `Repriced_Bill_Confirmed` created on Contacts (`fld2bhMZHwTnp4X9b`, date, empty = ineligible, re-query at send time) per migration red-team F6, under the operator's decision delegation. No record values written — the field starts empty by design. | new field, zero values; no scores changed |

After the first ~50 replies: reply rate by band vs the curve; move the peak or flatten. This
file and nothing else is where values change.

### Reserved — the fourth axis

The mined taxonomy is **Fit / Intent / Relationship / Timing** (`skills/icp-scoring/SKILL.md`
lineage note; the source evaluation was deleted 2026-07-29). Three are built.
**Relationship is deliberately absent, not overlooked** — with zero delivered clients and no
prior-touch data it would be a column of zeros pretending to be a signal.

| | |
|---|---|
| **Activates when** | retained relationships exist and the prior-touch data is real — the first delivered clients, referral chains, or existing-client adjacency |
| **Would hold** | prior touches, warm intro path, referral source, adjacency to an existing client |
| **Enters as** | a Priority component alongside Fit and Intent; add its row to §7's band arithmetic in the same edit |
| **Do not** | add it early as an all-zero column — an axis that never varies is noise that dilutes the two axes that do |

This block is the reserved home the scoring skill's lineage note points at. Filling it is a
value change like any other: it happens here, and nowhere else.
