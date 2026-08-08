<!--
ROUTER — describes how to clone and use the coupled workbook `pipeline-tracker.xlsx`.
This is the firm's internal lead tracker (the `practice/` workspace, not a client deliverable).
Adapted from the operator's licensed "Sales Pipeline" reference for a bookkeeping firm's
recurring-fee model. Keep this router and the workbook in sync.
-->

# Pipeline Tracker (practice)

The firm's internal view of who's in the funnel and what the pipeline is worth. Unlike a
one-off project shop, our value is **recurring** — so the tracker weighs monthly fee plus
any one-time setup, and rolls up a weighted value by stage. Two coupled files:

- **`pipeline-tracker.xlsx`** — the working tracker (internal).
- **`pipeline-tracker.md`** — this router.

## How to use it

1. **Copy the workbook once** to your own working file the first time:
   `pipeline/pipeline-tracker_active.xlsx` (keep the original blank as the template).
   After that, keep updating the active copy — it's a living document, not a per-lead file.
2. **One row per lead** on the Pipeline tab. Move a lead through the stages by changing
   its Stage; the Summary tab re-totals automatically.
3. **Fill `Lead source` when the row is created** — the campaign slug that produced the reply
   (e.g. `2026-07-12-quickbooks-bounce`), or `referral` / `inbound` / `direct`. This is the only
   field that says *why this deal exists*; nothing upstream records it, so a blank here is
   permanently blank.
4. **When a lead is won**, mark it Won here, then copy `clients/_template/` to a real
   client folder (see `../business-dev/CONTEXT.md`, pipeline stages). **Carry `Lead source`,
   `Monthly fee`, and `Setup fee` into the client profile's Engagement block** — the tracker
   keeps the history; the client folder becomes the source of truth from that point, and
   without those three the funnel is severed exactly where it starts paying.

## The tabs

| Tab | What goes in it |
|---|---|
| **Pipeline** | One row per lead: opportunity/business, contact, email, stage, monthly fee, one-time setup fee, expected close date, status, next touch date, and **lead source**. Stages carry a probability the workbook uses to weight the value. Rows 5–104 — **100 leads**, raised from the original 15 because a 5% reply rate on the 490-account rollout is roughly 25 deals, and the old cap would have truncated silently. |
| **Summary** | Auto-rolled metrics: count and weighted value by stage, total pipeline value, expected monthly recurring revenue if the open pipeline closes, and a simple close rate (won ÷ closed). Nothing to type here — it reads the Pipeline tab. |

## Stages (match `../business-dev/CONTEXT.md`)

`Lead` → `Outreach sent` → `In conversation` → `Proposal sent` → `Won` / `Lost`.
The probability weights live on the Summary tab and can be tuned to the firm's real
close rates over time.

## Rules

- **Internal only.** A lead is not a client and has no `clients/` folder until Won
  (`../business-dev/CONTEXT.md`).
- **No cross-client data.** Don't paste one prospect's numbers as leverage on another.
- Keep the original workbook blank; work in the `_active` copy.
