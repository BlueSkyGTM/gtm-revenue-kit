# ICP Definition

*This is the canonical ICP document. All campaigns, scoring models, and outreach sequences reference this file. Update it when your understanding of the ideal customer evolves — and note the date of each change.*

Last updated: 2026-07-12

*See example: `examples/sample-company/context/icp-definition.md`*

---

## Ideal Customer Profile

### Firmographics

| Dimension | Ideal Range | Notes |
|-----------|-------------|-------|
| Employee count | 1–20 is the delivery *sweet spot*, NOT a cap | Sole proprietors up to small teams are the easiest solo-delivery fit. **Miriam services accounts into the millions in revenue — size is never a disqualifier.** Larger QuickBooks accounts stay fully in-ICP; they are down-weighted only as a soft preference inside the `icp-scoring` spend-fit curve, never removed. |
| Revenue (if known) | [inferred: roughly $100k–$5M/yr] | Enough transaction volume to make outsourced bookkeeping worth the spend |
| Funding stage | N/A | Not a funded-startup motion — owner-operated small businesses, bootstrapped by default |
| Industry | [inferred: services, retail, contractors/trades, professional services — any QuickBooks-heavy small-business vertical] | No single vertical confirmed in the lead data; QuickBooks usage is the unifying signal, not industry |
| Geography | United States, nationwide | Confirmed from the 863-record lead list: 52 distinct states represented. Top states by volume: CA (140), TX (90), FL (86), NY (29), VA (28), GA (27), IL (23), NC (22), OH (22). Not regionally concentrated — treat as a national list. |
| Business model | Small business, owner-managed | Owner is typically both the buyer and the day-to-day books manager pre-outsourcing |

### Technographics

*What does their current stack tell us about fit? Confirmed directly from the `Products` field in the Airtable lead list ("QuickBooks Lead Capture" base → `Contacts` table, 863 records) — not inferred.*

**Strong fit indicators (with real counts from the current list):**
- Actively paying for QuickBooks Online (any tier) — baseline qualifier; `QBO_SIMPLE_START` (227), `QBO_PLUS` (199), `QBO_ESSENTIALS` (156), `QBO_ADVANCED` (140)
- **Already a QuickBooks Live / Expert Assisted customer** — 477 of 863 (55.3%) carry a Live/Expert-Assisted product tag. This is the single strongest fit indicator in the list: proven budget for done-for-you bookkeeping, direct displacement opportunity. See `context/signal-library.md`.
- On QuickBooks Online Plus or Advanced specifically — 339 of 863 (39%) — the tiers taking the largest dollar increases on 2026-08-01 (Plus $115→$140, Advanced $275→$340; verified table in `scoring-model.md` §3 / the migration debrief)
- Has QuickBooks Payroll active (`PR_CORE`/`PR_PREMIUM`/`PR_ELITE`/`PR_CONTR`/Workforce tags) — roughly 260 of 863 (30%) — stacks additional cost on top of the base subscription
- No internal bookkeeper/accountant on staff — owner or a generalist admin is managing books directly inside QBO [inferred — not a field in the current lead data, confirm in discovery]

**Weak fit indicators:**
- Not on QuickBooks at all (Xero, Wave, Sage, spreadsheets) — no shared pain point, different sales motion entirely. N/A for the current list — every record is a confirmed QuickBooks account by construction.
- Recently migrated away from QuickBooks — signals they've already solved for the pain differently

**Data quality note:** The `Products` field has known data-entry noise — typo'd variants of the same SKUs appear (`OBLIVE_EXPERT_SERVICES`, `QBOLIVE_ASSISTED`, `OBO_PLUS`, etc., an O/Q swap or prefix drift on the real codes). 23 of 863 records have no usable `Products` data (blank or unparseable). Worth a normalization pass before running a full scoring campaign, but not blocking — the signal is strong even without cleanup.

### Organizational signals

*What does their team structure tell us?*

- No dedicated bookkeeper, accountant, or controller role — the owner or an admin/office manager is absorbing bookkeeping as part of a broader role
- Single decision-maker structure (owner approves spend directly) — short, low-friction sales cycle
- [inferred] Hiring for a bookkeeping/admin role — may signal they're trying to solve the problem by hiring rather than outsourcing, worth testing a cost-comparison angle

---

## Tier Definitions

### Tier 1 — Dream Accounts (from the lead list)

QuickBooks Online subscribers showing an active, confirmed pain and/or displacement signal — directly readable from the Airtable data, no enrichment required. Highest-probability conversions in the current outbound push.

**Criteria:**
- Already an existing QuickBooks Live / Expert Assisted customer (`Products` field — 477 of 863 records, 55.3%), **and/or**
- Currently paying for QuickBooks Online Plus or Advanced (`Products` field — 339 of 863 records, 39%, took the largest 2026 price hikes)
- Bonus: 2+ years `Customer Lifetime`, or `Customer Type` = `upgrader`
- 1–20 employees, no internal bookkeeper [inferred — confirm in discovery]

**Outreach approach:** Direct outbound (phone/email), personalized to the specific signal — lead with the QuickBooks Live consistency angle for existing Live customers, the price-hike angle for Plus/Advanced-only accounts.

---

### Tier 2 — High-Fit Accounts

QuickBooks Online subscribers on the list who match firmographically but don't carry the strongest Tier 1 product signals.

**Criteria:**
- Currently paying for QuickBooks Online Essentials (`QBO_ESSENTIALS` — 156 of 863 records, 18%), or has QuickBooks Payroll active without a Live/Plus/Advanced tag
- No confirmed public AI complaint, but plan tier and renewal timing make the 2026 price increase relevant to them

**Outreach approach:** Sequenced outbound referencing the industry-wide price increase (doesn't require an account-specific signal — the 2026 hike applies broadly to the QBO base).

---

### Tier 3 — Good-Fit Accounts

Remaining accounts on the lead list that meet minimum criteria but carry only the lowest-urgency product signal.

**Criteria:**
- QuickBooks Online Simple Start only, no Live/Payroll add-ons (`QBO_SIMPLE_START` with no other tags — smallest, lowest-urgency segment)
- 23 of 863 records with no usable `Products` data (blank or unparseable) — treat as unscored until enriched

**Outreach approach:** Lower-touch, general messaging (price/AI framing) until enrichment fills in a stronger signal.

---

### Tier 4 — Monitor Only

Accounts that don't fit the current motion but may fit the future white-label motion.

**Criteria:**
- Accounting or CPA firms — not a current target (white-label is a future goal), but worth tracking separately so they aren't mixed into the small-business list
- Businesses that have genuinely outgrown QuickBooks for a true ERP (NetSuite/Sage Intacct) — a different software depth, not a size line. A large business still *on* QuickBooks is in-ICP.

---

## Anti-ICP

*Accounts we explicitly exclude. Being clear about who we don't sell to saves time and protects pipeline quality.*

| Exclusion | Reason |
|-----------|--------|
| Businesses not on QuickBooks (Xero, Wave, Sage, spreadsheets) | No shared pain point — the entire current signal (QBO price hikes, Intuit Assist AI complaints) doesn't apply. Different sales motion, not worth mixing into this list. |
| Businesses on a true ERP (NetSuite / Sage Intacct), i.e. genuinely off QuickBooks | Different software depth and motion — not a size exclusion. A large company still on QuickBooks is in-ICP; Miriam services accounts into the millions. |
| Businesses with an existing internal bookkeeper, controller, or finance team | No capacity gap to fill — outsourcing doesn't solve a problem they already have covered. |
| Non-US businesses | Service model assumes US tax, payroll, and QuickBooks Online US pricing context. |
| Pre-revenue or no real transaction volume | Nothing to bookkeep yet, and no budget for the service. |
| [inferred] Accounting/CPA firms | Current motion is small-business direct, not white-label — target these separately once the white-label motion is actually launched, don't mix into the current 1,000-lead push. |

---

## Qualification Framework

*Use in discovery calls to quickly determine ICP fit.*

### Must-have (deal-breaker if absent)
1. Actively paying for QuickBooks Online
2. US-based small business, 1–20 employees
3. Owner (or a single decision-maker) controls the spend decision

### Strong indicators (2+ = high confidence)
1. Already an existing QuickBooks Live / Expert Assisted customer (strongest single indicator — proven budget, direct displacement pitch)
2. On QuickBooks Online Plus or Advanced (largest 2026 price hikes)
3. Has expressed frustration with QuickBooks pricing or AI features (publicly or in conversation)
4. No internal bookkeeper — owner or generalist admin is doing the books today
5. QuickBooks renewal or billing date within the next 30–60 days

### Red flags (2+ = deprioritize)
1. Recently and happily adopted Intuit Assist / AI bookkeeping features with no complaints
2. Has a dedicated internal bookkeeper or accountant already
3. Actively price-shopping for the cheapest possible option, unwilling to pay for a human/quality difference

---

## ICP Evolution Log

*Track how your ICP has changed over time. This is the most valuable artifact in the repo after a year — the log tells you more than the current definition.*

**Review cadence:** Add an entry quarterly. Re-score the full account list after any ICP change to find newly qualified or disqualified accounts.

| Date | Change | Reason |
|------|--------|--------|
| 2026-07-12 | Initial ICP definition set: small business QuickBooks Online subscribers (1–20 employees, US), signaled by 2026 price hikes and Intuit Assist AI dissatisfaction. Accounting/CPA firms (white-label target) explicitly excluded from current motion and moved to Tier 4/monitor-only. | Founder confirmed the active motion is working a 1,000-lead list of unhappy QuickBooks subscribers; white-label to accounting firms is a future goal, not the current target. Site's public positioning (white-label, accounting-firm-facing) reflects the future state, not the current campaign — noted so future sessions don't default back to it. |
| 2026-07-13 | (1) **No size cap** — "1–20 employees" reframed as a delivery *preference*, not a limit; Miriam services accounts into the millions, nothing is excluded for size. Anti-ICP "enterprise/ERP" reframed as "genuinely off QuickBooks (true ERP)," a software-depth line, not a size line. (2) **Scoring model swapped** to spend / offer-intent / serviceability fit dims + signals (see `skills/icp-scoring/SKILL.md`), with the Spending_Score per-SKU map documented in `signal-library.md`. Spend-fit uses a sweet-spot curve that down-weights the 85–96 top band *in points* (never a filter). Re-scored the full list per cadence. | Operator direction: large/high-spend accounts are fully serviceable; the sweet-spot preference must live in the score, not as a cap or a sort-override. Proven intent (Live payers) is carried by the signal score so the curve can't bury it. Whole weight scheme is a reversible hypothesis to re-tune from reply data. |
| 2026-07-12 | Connected the actual lead list (Airtable base "QuickBooks Lead Capture" → `Contacts` table, 863 records — not exactly 1,000, close). Replaced inferred technographics/geography with real field data: 55.3% of the list are already QuickBooks Live/Expert Assisted customers (promoted to the top Tier 1 signal), geography confirmed nationwide (52 states, not regional), tier tiers rebuilt around actual `Products`/`Customer Type`/`Customer Lifetime` field values. | Direct data access changes several inferred assumptions — the strongest signal turned out to be existing QuickBooks Live incumbency, not public AI complaints, and the list is national rather than SoCal-concentrated as previously guessed from the founder's area code. |
