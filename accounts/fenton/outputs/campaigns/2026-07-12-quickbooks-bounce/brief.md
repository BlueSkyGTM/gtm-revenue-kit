# Campaign Brief: QuickBooks Bounce → Winner Rollout

**Campaign:** QuickBooks Bounce (campaign 1 of the Fenton GTM program). The play: bounce dissatisfied QuickBooks Online / QuickBooks Live customers off Intuit and onto a human bookkeeper. Sister campaigns tracked in `outputs/campaigns/README.md` — White-Label Accounting (planned) and Churches (parked).
**Lists:** `outputs/lists/quickbooks-bounce/` (namespaced to this campaign).

Date: 2026-07-12
Owner: GTM (send via Instantly) | Delivery: Miriam
Status: Copy approved for review — NOT launched

---

## Strategy in one paragraph

Test 3 hooks on the lowest-priority slice of the list, then send ONLY the winner to everyone else. The message is not primarily price: owners have been posting about QuickBooks' Intuit Assist AI miscoding transactions, and Intuit's paid bookkeeping help lives in the same product from the same company, so subscribers pay a lot without stepping outside the system that creates the problem. The ongoing subscription price increases are the supporting pinch. Two offers by funnel stage: proven Intuit-bookkeeping payers get the ongoing bookkeeping + payroll offer; QBO-only non-payers get a one-time cleanup offer, with the ongoing pitch made only after the cleanup work completes. No calls — email only.

---

## Segments (from Airtable "QuickBooks Lead Capture" → Contacts, pulled 2026-07-12, 863 records)

| Segment | Definition | Count | Offer | Role |
|---|---|---|---|---|
| A — Ongoing | Any Intuit bookkeeping-service tag (`QBLIVE_*`, `Intuit Expert Assisted`, Live Assisted variants) | 505 | Ongoing bookkeeping + payroll | Prime — winner only |

> **Count reconciliation:** Segment A = **505** (any Intuit bookkeeping-service tag, the broad definition this campaign targets, including `QBLIVE_ASSISTED`). The `context/` files cite **477 / 55.3%** for a narrower "QuickBooks Live / Expert Assisted" definition set earlier. Both are correct for their own definition; 505 ⊇ 477. This campaign uses 505.
| A-priority: Full-Service | `FULL_SERVICES_BOOKKEEPING` | 3 active firms (5 records: New Life New You is duplicated; JB Carts dropped — dead contact) | Ongoing | Hand-written 1:1, researched |
| A-first: PENDING_CANCEL | tag inside Assisted records | 4 | Ongoing | First emails in rollout |
| B — Cleanup | QBO tag present, no bookkeeping-service tag | 330 (all have emails) | One-time cleanup; ongoing offer only after completed work | Test bed |
| Unsegmented | No/unparseable Products data | 23 | — | Enrich later |

**Test bed:** bottom half of Segment B by ICP-lite score (tenure, payroll add-ons, plan tier, upgrader flag, contactability) = **165 leads, ~55 sends/variant**. Top half (165) held out — receives the winner alongside Segment A.

**Full-Service firms (hand-send list, 3 active):** Power Forward Solutionz LLC (Reston, VA — Alberto), New Life New You Counseling (Schererville, IN — Becky), Marathon Plumbing LLC (Commerce City, CO — Peter, via Dez's inbox).

**Dropped:** JB Carts LLC (Fort Worth, TX) — the only contact on file (`jacob@frenzeldossani.com`) is a dead domain that bounces, and no reachable decision-maker was found publicly. Removed from outreach rather than chased. Research retained at `outputs/account-research/2026-07-12-jb-carts-research.md` if a valid contact surfaces later.

**PENDING_CANCEL (email first in rollout):** Nova Design Build (Karina), K & M Broussard Co (Kelly), Pet Assistance Foundation (Bob), Triangle Park Chapter of The Links, Inc. (Makeba).

**Data notes:** 60 Segment A + 80 Segment B records missing first name — use Instantly first-name fallback ("there"); verify exact fallback syntax in the Instantly UI before launch. 1 Segment A record missing email → enrichment pass (`workflows/enrichment.md`).

---

## Methodology (updated 2026-07-12 — PVP across the board, hardened copy rules)

- **PVP everywhere.** All copy — test bed, rollout, and hand-sends — passes the Permissionless Value Prop test from `skills/signal-to-sequence/SKILL.md`: delete the CTA and the body still states something true about *their* books. The operator's Clay Operator pitch template is retired at the operator's direction ("insider knowledge trumps cold pitch").
- **Hardened copy rules** (now in `context/positioning.md` → Copy Rules, enforced by the generator linter): no em/en dashes, no AI-tell vocabulary, no semicolons/emoji, AI claims attributed, prices as dollars not percentages, one CTA, under 120 words. The build fails on any violation.
- **What the test measures:** the same three angles (AI-in-books, price, experts-lean-on-AI) run PVP-style in both places, so the winning **angle** transfers cleanly. The only structural difference left is the offer itself (cleanup for Segment B vs. ongoing for Segment A), which is inherent to the two-offer funnel — so cross-segment reply-rate comparison is close but not identical.
- **Follow-up touches (T3/T4/T6):** deferred until the test names a winner, so we don't write sequences for two losing angles.

## The tested variable

The hook (the opening insight paragraph) is the ONLY tested variable. Fixed within each segment: the offer line, the social-proof line, the CTA, the signature. The CTA is **"would a cleanup be worth a short conversation?"** for Segment B and **"would that be worth a short conversation?"** for Segment A. The same three angles run in both segments so the winning angle transfers across offers.

| Variant | Hook concept | Grounding |
|---|---|---|
| ai-in-the-books | Owners publicly report Intuit Assist recoding transactions / marking unpaid invoices paid | `context/positioning.md` Pillar 3 quotes (attributed: "owners have been posting/flagging"; the recipient's own books are never asserted to be affected) |
| paying-more-getting-software | The Aug 1 QuickBooks increase (Plus $115→$140, Advanced $275→$340); you pay more for software, not for help | **Verified:** current list price is Plus $115 / Advanced $275; effective Aug 1, 2026 they rise to $140 / $340 (Essentials $75→$85, Simple Start unchanged). Codex's "$115/$275" and the earlier "$140/$340" were the before/after of the same increase. Copy names the tiers that jump most but stays true for any tier ("whatever tier you are on, the direction is the same"). Sources: NerdWallet, Fit Small Business, Intuit pricing coverage (Jul 2026). |
| experts-lean-on-it | Intuit's paid bookkeeping help and its Intuit Assist AI are the same company in the same product; escalating to their team does not step outside that system | Verifiable framing only (same-company/same-product). Does NOT claim the human experts rely on or review the AI — that was unsourced and was removed. |

Binding copy rules (enforced by the generator linter): PVP survives CTA removal; no em/en dashes; no AI-tell vocabulary; no semicolons/emoji; AI-behavior claims attributed, never asserted about the recipient's account; no unverified numbers; "months behind" only in Full-Service hand-sends; no percentages; no "cheaper than $X"; no links; one CTA; ≤120 words (scripted — actual range 94–111).

---

## Prioritization update (2026-07-13) — composite ICP score

Lists are ordered by the **composite ICP score (0–100)** from `skills/icp-scoring/SKILL.md`, not raw spend. It combines: **spend-fit** (a sweet-spot curve over the Spending_Score that peaks at Mid-High / upper-Standard and *down-weights the 85–96 top band in points* — those accounts stay fully in the list, they just rank lower), **offer-intent** (Segment A payers score higher), **serviceability** (timezone-fit + tenure), and the **signal score** (a Live payer earns signal points that lift them regardless of the spend curve, so proven intent is never buried). **No account is capped or removed for size** — Miriam services accounts into the millions; the sweet-spot is a soft preference in the points.

**840 of 863 leads scored:** 613 from Clay's Spending_Score export, 227 scored locally by the same per-SKU formula (validated 99.2% exact vs Clay; per-SKU map in `context/signal-library.md`). Tier spread: T1=320, T2=375, T3=143, T4=2, none excluded. The 23 with no product data stay unscored. Master with all component columns: `outputs/lists/quickbooks-bounce/_all-scored-master.csv`. **Proper ongoing scoring moves to Clay Audiences once the account switch is done.** Every weight is a reversible zero-data hypothesis — re-tune from the signal-performance log once replies land, then re-score.

**Schedule fit:** every lead is timezone-tagged from State and matched to Miriam's availability windows (outside her 7am–3pm PT work block). Only **4 of 607 are unfit** (Hawaii, US Virgin Islands, 2 blank state) → `outputs/lists/schedule-unfit-review.csv`. The value is the send/booking windows now attached per lead so Instantly can schedule by timezone and booked calls land in Miriam's hours. Fit distribution: Eastern 256, Central 164, Pacific 145, Mountain 38. Note: **Arizona = Pacific right now** (summer, no DST); if the campaign runs past early November, AZ shifts to Mountain windows.

Client-local windows by zone (weekday early / weekday evening / weekend): Pacific 5–7 AM / 3–8 PM / 5 AM–8 PM · Mountain 6–8 AM / 4–9 PM / 6 AM–9 PM · Central 7–9 AM / 5–10 PM / 7 AM–10 PM · Eastern 8–10 AM / 6–11 PM / 8 AM–11 PM. Recommend sending at the start of each zone's early window.

## Test → rollout sequence

1. **Phase 1 — Test:** Instantly campaign, 3 variants (cleanup assembly), on the bottom ~150 of `outputs/lists/quickbooks-bounce/test-bed-cleanup-by-icp-score.csv` (Segment B, schedule-fit, sorted ICP score **ascending** → lowest-priority cleanup leads tested first; ≈50/variant). Higher-scoring cleanup leads are protected. Fields: `first_name`, `qbo_tier`, `timezone`. Schedule sends by `timezone` to the early window.
2. **Decision rule:** pause any variant <1% reply after 50 sends; winner = highest reply rate (tiebreak: positive-reply rate). Expected call within 2 weeks.
3. **Phase 2 — Rollout:** winning hook, Segment A assembly (`sequences/rollout-a.md`) to `outputs/lists/quickbooks-bounce/rollout-A-by-icp-score.csv` (490, sorted ICP score **descending**). Mid-High payers rank top (best sweet-spot fit); the very-high-spend accounts rank mid-pack but stay fully in — down-weighted in points, not filtered. PENDING_CANCEL first within that. Then the winner to the high-scoring B hold-out. Full-Service hand-writes (`sequences/fullservice-handsends.md`, 3 firms) send any time, not gated on the test.

**Broken-email cleanup (2026-07-13):** 36 records had hard-truncated emails from a source export bug. Sent through Clay for recovery; the rule applied was strict — no result found, or only a bare personal-Gmail name-pattern guess (not tied to a real business domain), both count as unrecoverable. Net: **12 recovered** with real business-domain emails and folded back into their original lists (roles/counts above already reflect this); **22 permanently dropped**, including two accounts that mattered — **HoseWorks LLC (ICP 93)** and **Harvest Church (ICP 83)** — both lost for good with no valid email found. Full detail was in `tasks/todo.md`, deleted 2026-07-29; git history holds it.
4. **Funnel rule (B):** cleanup replies are worked to completed delivery before any ongoing pitch.

---

## Files

- `sequences/test.md` — 3 test emails (Segment B assembly)
- `sequences/rollout-a.md` — same 3 hooks, Segment A assembly (rollout-ready; **eligibility restricted 2026-08-03 to verified switchers minus price-fatigue-suppressed, re-queried at send time**)
- `sequences/rollout-b-diy-draft.md` — the DIY segment's own conversion copy (draft 2026-08-03, second wave, never blended with switcher copy)
- `sequences/fullservice-handsends.md` — 4 researched 1:1 emails
- `metrics.md` — targets + decision rule
- `results.md` — fill as the campaign runs, by hand (the planned Instantly adapter and `practice/tools/` were deleted 2026-07-29; results are read from the Instantly dashboard and typed in)
- Research briefs: `outputs/2026-07-12-[account]-research.md` (4 files)

**Send lists (gitignored `outputs/lists/quickbooks-bounce/`, composite-ICP ordered, cleaned 2026-07-13):**
- `phase1-test-send.csv` (148) — **launch-ready**, bottom of the test bed by ICP score (+3 recovered from the broken-email cleanup)
- `research-head-20.csv` (20) — the top 20 of Tier 1 (tie-break: signal score → offer-intent → email A→Z) that get the account-research hand-brief before touch 1; the rest of Tier 1 runs the same tier-1 sequence without a brief. HoseWorks LLC (was #1) permanently lost to the broken-email issue — PUMPKIN MOON backfilled the slot.
- `test-bed-cleanup-by-icp-score.csv` (320) — Segment B, ICP ascending
- `rollout-A-by-icp-score.csv` (490) — Phase 2 winner target, ICP descending
- `_all-scored-master.csv` (822) — full universe with all score component columns (spend_fit, offer_fit, serviceability, signals, icp_score, tier)
- `broken-emails-for-clay-enrichment.csv` / `-v2.csv` / `broken-emails-suppressed.csv` — historical record of the truncation bug, the Clay recovery attempt, and the keep/trash decision. Not used for sending.
- `new-leads-clay-batch{1,2}.csv` (200 + 31) — the not-yet-on-Clay leads, split for the 200-cap
- `schedule-unfit-review.csv` (4) — set aside, manual review
- *(superseded: the earlier `test-bed-165.csv` / `rollout-segmentA-505.csv` were pre-spend-score)*
