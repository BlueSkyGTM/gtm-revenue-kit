# Positioning red-team — QuickBooks Bounce (pre-launch)

*Run 2026-07-27 per `playbooks/impact-positioning.md` step 7, via `/codex` (GPT-5.6-sol,
high reasoning, read-only sandbox) against the settled Bounce set: `context/positioning.md`,
`messaging-house.md`, `competitor-radar.md`, both personas, `web/index.html`, and
`sequences/rollout-a.md`. Conformance check, not a quality gate — the operator decides what
ships. Verbatim reviewer findings condensed; every claim cites its file.*

**Verdict: 1 of 8 dimensions passes clean (cross-buyer segment purity). Seven carry findings.
Pre-launch is exactly when this is cheap — after 505 sends it is an autopsy.**

## Per-dimension findings

| # | Dimension | Verdict | Core finding |
|---|---|---|---|
| 1 | Alternatives | FINDING | The radar omits **the independent local bookkeeper** — the alternative most able to copy the "one accountable person" claim. Its absence artificially protects the differentiation. |
| 2 | Beachhead | FINDING | The audience is an ICP envelope, not a beachhead. The session report names the 452 verified human-service switchers as the strongest segment; the positioning never adopted them as the first market (switching sale ≠ conversion sale, §1.1). *[2026-08-03: the cited session report was deleted 2026-07-29; the §1.1 reference survives only in git history.]* |
| 3 | Buyer | FINDING | Personas are well-formed, but **contact-to-persona title fit on the 862 records is unvalidated** (the audit analyzed product holdings, not titles; one research-head contact's role is explicitly unconfirmed). |
| 4 | Differentiated value | FINDING | The value prop is a strong **QuickBooks Live battle claim**, not an only-statement: it never names DIY's structural limit, and against an independent bookkeeper nearly every clause is swappable. |
| 5 | Message consistency | FINDING | `messaging-house.md` still projects the **August 1 numbers as Pillar 2's carrier** (lines 43, 71–78) after the 2026-07-25 no-urgency direction; the site hero says "one certified accountant" while the body drifts to "the same people"; payroll closes every rollout email yet is no pillar (283 payroll-stacked records). |
| 6 | Channel translation | FINDING | The price-hook email variant was pulled 07-25, but `web/index.html` still runs a major "THE AUGUST 1 INCREASE" section and `inbound-handoff.md` §1 still leads Pillar 2 with it — the withdrawn narrative survives after the click. **Operational: the site publishes (480) 791-5619; the one-pager publishes (480) 732-4388.** One of these is wrong on a live surface. |
| 7 | Evidence quality | FINDING | Competitor-radar dollar/behavior claims (QB Live prices, 4–5-month delays, Bench's 12,000, BBB rating) carry a generic sources paragraph, not claim-level cites; the live site's "went up twice in a single year" is unsupported and unmarked; the Aug-1 date's visual emphasis on the site conflicts with the no-urgency direction's intent. |
| 8 | Segment purity | SPLIT | **Cross-buyer purity passes** (no WL language in Bounce, no Bounce arguments in the new WL set). **Within-list motive purity fails:** rollout-A assumes recipients already pay for human help, but the eligible pool holds only 452 verified switchers, ~388 DIY, and 165 ≤2-month customers for whom price-fatigue claims are factually wrong. |

*[2026-08-03 status pass, second sweep — all eight dimensions now addressed, audit body
unchanged: **dim 1** resolved (independent local bookkeeper battlecarded in
`competitor-radar.md`); **dim 2** resolved (`positioning.md` → Beachhead: the ~452 verified
switchers adopted as the first market); **dim 3** closed (title fit is *unvalidatable* — no
title field exists; closure rule in `outputs/2026-08-03-validation-title-fit.md`); **dim 4**
resolved (`positioning.md` only-statement naming DIY's structural limit and the provable
floor); **dim 5** resolved (`messaging-house.md` Pillar 2 date-neutral); **dim 6** resolved —
the phone finding was already stale when written: (480) 791-5619 was corrected across all
live surfaces on 2026-07-25 (`_archive/kit-tasks/todo.md`, commit 9551b52), and
`inbound-handoff.md` §1 was made date-neutral 2026-08-03; **dim 7** resolved (claim-level
sources table in `competitor-radar.md`; the "twice in a single year" claim replaced in
`web/index.html` source — live-site deploy still pending); **dim 8** executed (rollout-A
restricted to verified switchers minus suppressed, re-queried at send time; DIY conversion
track drafted at `sequences/rollout-b-diy-draft.md`).]*

## The reviewer's top 5 fixes, ranked (verbatim in substance)

1. **Motive-based rollout eligibility before any further send** — restrict current variants to
   verified switchers; separate DIY copy; suppress ≤2-month customers from price-fatigue claims
   (`sequences/rollout-a.md`). *This is the Airtable `Motive_Segment`/`Suppress_Price_Fatigue`
   write-back plus a list split — the work is already validated and waiting on a yes.*
2. **De-center August 1 on the site; kill the unsupported "twice in one year" claim**
   (`web/index.html:89–136`) — re-anchor on the cleanup review, the accountable person, the
   current-file mechanism.
3. **Rebuild positioning around a real beachhead** — verified QB Live / Expert Assisted payers
   as the first switching segment; DIY as a deferred conversion motion (`context/positioning.md`).
4. **Regenerate the messaging house post-07-25/07-26 decisions** — remove stale Aug-1
   projections, add switcher-vs-DIY translations, resolve "one person" vs "same people"
   (`context/messaging-house.md`).
5. **Fix the call track/leave-behind now** — reconcile the phone number, drop the deadline-led
   pillar, branch the opener on whether the buyer already pays for human help
   (`outputs/inbound-handoff.md`).

## Checklist gaps the reviewer found in the playbook itself

Adopted into `playbooks/impact-positioning.md` as future amendments (not silently, recorded
here first): per-claim **eligibility** (is each record factually eligible for each claim —
tenure, incumbent, motive), **operational consistency** (phone/URL/CTA/offer-name identity
across surfaces), **change-control drift** (was every downstream artifact regenerated after the
last positioning decision), **alternative completeness** (does the radar omit the alternative
best able to copy the differentiation), a defined **source standard** (claim + source + access
date), and **capacity truth** (are all promises simultaneously deliverable by a solo practice).

## Applied now vs. awaiting the operator

**Applied in-session (conformance to decisions already made):** a dated amendment on
`messaging-house.md` marking the Aug-1 projections as market context only, per the standing
2026-07-25 operator direction. Nothing else — items 1–5 change live copy, list eligibility, or
strategy, and those ship on the operator's word, not the auditor's.

**Awaiting the operator, in the reviewer's priority order:** the five fixes above, plus one
question the audit cannot answer: **which phone number is correct — (480) 791-5619 (site) or
(480) 732-4388 (one-pager)?**
