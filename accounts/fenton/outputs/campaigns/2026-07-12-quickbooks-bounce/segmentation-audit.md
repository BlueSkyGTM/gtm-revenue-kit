# QuickBooks Bounce — segmentation audit

*2026-07-26. Counts read live from `QuickBooks Lead Capture` / `Contacts` (`apppSIWMEemeoaCdv` / `tbl1TtoJs93jkrjJQ`), 862 records.*

> **Status update 2026-07-27 — this audit's finding is now a field, not a proposal.**
> `Motive_Segment` (`switcher` / `diy` / `no-data`) and `Suppress_Price_Fatigue` are live on all
> 862 records, verified by re-query: **505 switchers · 335 diy · 22 no-data · 145 suppressed.**
> Two deliberate deltas from the counts below: switchers came in at 505 rather than 452 because
> the write-back also matched the typo SKUs (`OBLIVE_`, `QBOLIVE_`), the July import's
> human-readable product names, and the Live *tax*-assist SKUs — someone paying Intuit for human
> tax help has still accepted paying Intuit for a human. Suppression came in at 145 rather than
> 165 because the live tenure predicate (days / "1 month" / "2 months") returns 145. The
> `LIVE_SERVICES_PREMIUM` decoy was never matched. **Do not re-derive the segmentation** — filter
> the field. Full record in `/tasks/todo.md`.
> *[2026-08-03: `tasks/todo.md` was deleted 2026-07-29; the full record survives only in git history. See HANDOFF.md.]*

**Question:** the WL-1 research found one list hiding four markets. Does Bounce have the same problem?

**Answer: yes. There are three honest motive segments and two cross-cutting ones, and the campaign currently addresses them with a single message. One of those segments — 19% of the list — is being told something factually untrue about their own experience.**

---

## What is a segment and what is not

The table has five fields that look like segmentation. Three of them are not.

| Field | Values | Is it a segment? |
|---|---|---|
| `Campaign_Role` | rollout-A, test-bed, holdout, handsend, research-head, dropped, unscored | **No.** Experiment arms. Operational assignment, tells you nothing about motive. |
| `ICP_Tier` | 1, 2, 3, 4 | **No.** A ranking. Tier 1 and Tier 4 can want the same thing for the same reason. |
| `Spend_Band` | High, Mid-High, Standard | **No.** A ranking. Correlates with budget, not with why they would leave. |
| `Products` | SKU mix | **Yes.** This is where motive actually lives. |
| `Customer Lifetime` | 1 day to 11 years | **Yes,** and it is the one nobody has used. |

---

## The honest segments

### 1. Already paying Intuit for a human — **452 (52%)**

Holds `QBLIVE_EXPERT_SERVICES`, `QBLIVE_ASSISTED`, `Intuit Expert Assisted`, `FULL_SERVICES_BOOKKEEPING` or `Full Service`.

**These people have already decided they need help and are already buying it.** The sale is a switch, not a conversion. Price, quality and continuity are the levers. This is the strongest segment in the list and it roughly matches the 477 figure in `CLAUDE.md`, with minor drift.

### 2. DIY, no human — **~388 (45%)**

On QuickBooks Online with no human-service SKU.

**Completely different sale.** They have not conceded they need a bookkeeper. Before price or quality matters, they have to accept the premise. A switching message aimed at these people is answering a question they have not asked.

### 3. No product data — **22 (3%)**

Unusable for any product-based targeting. Should be excluded or enriched, not messaged.

---

## The two cross-cutting segments

These cut across 1 and 2 and change the message independently.

### 4. Payroll-stacked — **283 (33%)**

Holds `PR_CORE`, `PR_PREMIUM`, `PR_ELITE`, `Workforce` or `Payroll`.

Payroll is not bookkeeping. It has **statutory deadlines and financial penalties for lateness**. The urgency is externally imposed and dated, which is a fundamentally different pressure from "my books are messy." A third of the list carries it and the campaign does not speak to it.

### 5. Brand new customers — **165 (19%)**

`Customer Lifetime` of two months or less. Includes records reading **1 day**, **7 days**, **15 days**, **30 days**.

**This is the finding that matters.** The Bounce premise is that these people have absorbed escalating Intuit pricing and are worn down by it. Someone who signed up eight days ago has absorbed nothing. They are in the honeymoon window, they have not seen a renewal, and they have not been burned by the AI yet.

**Sending a price-fatigue message to 19% of the list is not a weak message. It is a wrong one**, and it is the kind of error that gets a reply of "I just started using this."

---

## The decoded-codes problem

`Customer Type` carries: **dtm, nttf, nttt, ntsf, ntlf, sdf, upgrader**, plus "Unavailable" and "No data yet".

Only `upgrader` is documented anywhere in the repo — `CLAUDE.md` lists it as a Tier 2 signal. The rest are Intuit internal codes that nobody has decoded, and they are sitting in a field being treated as a segmentation input.

Some are guessable from shape (`nttf` / `nttt` / `ntsf` / `ntlf` share an `nt` prefix and differ in the last two characters, which looks like a two-axis code). **Guessing is not decoding.** Either work out what they mean or stop treating the field as signal.

---

## The trap in the Products field

**Do not filter on `LIVE`.**

`LIVE_SERVICES_PREMIUM` appears on **823 of 862 records (95%)** and co-occurs with the genuine bookkeeping SKUs rather than replacing them. It is almost certainly a support or care tier bundled broadly, not the QuickBooks Live bookkeeping service.

A naive `contains "LIVE"` filter returns 823 and makes it look like 95% of the list is paying for a human bookkeeper. The real number is **452**. Anyone building a segment on that string will overstate the strongest signal in the campaign by 83%.

---

## Recommendations

**1. Suppress the 165 new customers from any price-fatigue message.** This is the cheapest correction available and it prevents a message that is verifiably wrong about the recipient. They are not disqualified — they are wrongly timed. Re-approach at first renewal.

**2. Split segment 1 from segment 2 before sending anything else.** 452 switchers and 388 DIY prospects need different first lines. Right now they get the same one, and the DIY half is being sold on a comparison they are not making.

**3. Give payroll its own thread.** 283 records with statutory deadlines is enough volume to justify a separate message, and deadline-driven pain converts faster than dissatisfaction-driven pain.

**4. Decode the Customer Type codes or drop the field.** A signal nobody can read is not a signal.

**5. Add a `LIVE_SERVICES_PREMIUM` warning wherever the Products field is documented.** This is a live trap that will be stepped on again.

**6. The same audit is owed to the tier bands.** `ICP_Tier` and `Spend_Band` are rankings being used where segments are needed. That is not wrong, but it means the campaign has been prioritising by *value* while assuming everyone shares one *motive*, which is exactly the error the WL-1 research surfaced.
