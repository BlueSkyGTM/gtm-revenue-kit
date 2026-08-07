# Pricing Strategy

*Single source of truth for how Fenton prices. Reference before writing any pricing into copy, a proposal, or a discovery script. The reasoning lives here, not in a memo.*

Last updated: 2026-07-14

---

## Status

Fenton's **actual** prices are not yet confirmed. The tiers below are anchored recommendations, not locked numbers. Move them from recommendation to real once Miriam confirms the five inputs at the bottom. Until then, do not assert a specific Fenton price as fact in outbound copy (the campaign copy rules already forbid unverified numbers).

## The six pricing principles

1. **Anchor to their Intuit bill, not the cheapest bookkeeper.** Every target already pays Intuit; the switch is "who does the work," not "start spending."
2. **Trust premium, never cheapest.** One accountable ProAdvisor. We lose pure price-shoppers on purpose (`positioning.md`).
3. **Flat and predictable vs. an escalating subscription** (Pillar 2).
4. **Tier by volume, not one flat fee.** WTP spans ~50x across the list.
5. **Cleanup-first ladder:** land on a one-time fix, expand to monthly, attach payroll.
6. **Copy discipline:** dollars not percentages, no "cheaper than $X," verified numbers only, no blanket hire-comparison.

## Verified anchors (Jul 2026, from `competitor-radar.md`)

- **QBO subscription:** Simple Start $38 · Essentials $85 · Plus $140 · Advanced $340 (post Aug 1).
- **QuickBooks Live Full-Service:** $300-$700/mo by expense volume, + the QBO sub; mandatory $500-$800 cleanup to start (one case: $1,500).
- **QuickBooks Live Expert Assisted:** ~$59/mo, guidance only (the floor; reframe anyone comparing us to it).
- **Bench:** ~$189-$499+/mo, platform-not-person, D- BBB post-shutdown.

## How account scoring sets the price

Both scores are deterministic from the `Products` field + state + tenure (`skills/icp-scoring/SKILL.md`, `context/signal-library.md`). They pre-band the quote and pick the pitch before the call.

- **Spending_Score** = per-SKU point sum (e.g. QBO Advanced 40, QBO Plus 20, Payroll Core 5). Bands: Standard 10-14 · Mid-High 15-39 · High 40+. → **Standard → Solo tier · Mid-High → Solo/Growth · High → Growth/Complex.**
- **ICP Score (0-100)** = spend-fit (30, a sweet-spot curve that *down-weights* the 71+ band as above solo capacity) + offer-intent (20) + serviceability (20) + signal score (30). Tiers: 80-100 T1 · 60-79 T2 · 40-59 T3 · 20-39 T4 · <20 exclude.
- **Offer-intent** = Segment A (pays Intuit for bookkeeping, 20 pts) → anchor to their Live/Expert bill, sell the switch, price at/above QB Live. Segment B (QBO only, 12 pts) → open on Cleanup or AI-Error Audit, expand later.
- **Signals → the pitch:** QBO Plus/Advanced (+8) → price-hike angle · existing Live/Expert payer (+15) → bill-to-bill anchor · public AI complaint (+12) → AI-Error Audit offer · renewal window (+6) → urgency · payroll stacked (+4) → payroll attach warm.

Caveat: Spending_Score is a spend/complexity proxy, not a confirmed budget. It pre-bands; the discovery question confirms.

## Recommended structure (ratify before locking)

**Cleanup (one-time entry):** diagnostic first (free or $149 credited), then Light $450-750 · Standard $900-2,400 · Deep $2,500-5,000+. Rule of thumb: ~one month of the eventual monthly tier per month of backlog.

**Monthly Bookkeeping (recurring core), tiered by monthly expense volume:** Solo (<$25K/mo) $350-450 · Growth ($25-75K/mo) $550-750 · Complex (>$75K/mo) $850-1,200 (custom above).

**Payroll (attach only):** $75/mo base + $10/employee, base waived on Growth+ plans.

## Packaging

- **A — Good/Better/Best** monthly packages (for a future pricing page).
- **B — Land-and-expand ladder (default motion):** Cleanup or AI-Error Audit → Monthly → +Payroll. Credit the entry fee toward the first months.
- **C — Flat all-in line item:** one blended monthly number, for the nonprofit/church/government segment that buys predictability (7 of the top 20).

## New service lines under consideration

Nonprofit/Board Reporting package · AI-Error Audit ("second opinion," a paid version of the campaign's core hook) · QBO Setup/Migration onboarding · 1099/Contractor filing-season service · Controller-lite advisory add-on.

## Migration motion pricing (added 2026-07-27 — the QB→Xero offer track)

*Its own block, not a blend with the bookkeeping tiers above. Carried over from the standing
rule: **no fixed-fee quote before one real file is timed**, no included hours, never
discount urgency.*

| Line | Basis | Status |
|---|---|---|
| Migration engagement | Est. hours × rate, quoted **after** the audit. Market comp for expert conversions: **$500–$1,000+** | `[UNTIMED]` — see the evidence ladder below |
| Pre-migration cleanup | Hourly. Market band **$40–$120/hr**; ours positioned premium, justified by the verification report | `[UNTIMED]` + `[rate pending the principal]` |
| Historical reconstruction | Detail beyond what free tooling carries (Jet Convert: 2 fiscal years) — separate line, quoted post-audit | `[UNTIMED]` |
| Paid diagnostic | **$295** standalone written finding | **Adopted 2026-08-03** under operator delegation, resolving the anchor problem below: priced deliberately under the $470 four-year conversion so the precaution never costs more than the job it protects. Flagged for the principal's confirmation, not pending on it |

**The diagnostic is dual-outcome by definition (canonized 2026-07-27, Addendum A).** It answers
*"should you move?"* — and a **stay** answer is a complete, paid-for finding, never a failed
sale. Every finding ends with next steps in whichever direction it recommends:
- *Leave case:* what transfers, what doesn't, what it takes, estimated hours.
- *Stay case:* right-size the plan (Advanced → Plus where seats sit unused), cleanup items
  before year-end, what to fix in the current file — ending in a bookkeeping conversation that
  starts *inside the document*, not as a follow-up pitch.

Required on every diagnostic cover page (and closing the calculator CTA):

> *We work in both systems. We'd bill you either way, so the finding follows your books, not
> our preference.*

That sentence is the credibility mechanism for a paid opinion bought from a stranger — balanced
interest, not neutrality — and it is structurally unavailable to a QuickBooks-only firm, which
has to recommend staying. In the routing matrix (`scoring-model.md` §4b) the diagnostic is the
**first touch for high/high accounts**: it resolves stay/leave at the client's expense and
lands revenue either way.
| Ongoing bookkeeping after migration | The actual prize — the tiers above apply | — |

**The $495 anchor problem (surfaced 2026-07-29, operator's challenge — RESOLVED 2026-08-03).**
Provenance first, because it was queried and the answer is not what either party assumed:
$495 was **not** a vendor cost reference. It was authored here, as the "Package B" position —
$495 standalone and non-creditable, chosen over $250 creditable on the argument that *the
credential is the proof, so never enter as the cheap option.* Nothing about Jet Convert or
Q2X fed that number.

But the vendor's real prices sat beside it awkwardly (host repo, `fenton-bookkeeping-os` →
`workspaces/books/docs/ledger-archive-spec.md` §1.1): a client can buy the **entire conversion of four fiscal years for $470**, and each
further year for $150. Against that, a $495 written opinion cost more than the work it was
an opinion about — a comparison a price-shopping buyer wins against us every time.

**Resolution: $295, adopted 2026-08-03 under the operator's delegation of open decisions.**
Of the three ways out that were on the table (price below the conversion; keep $495 and sell
what conversion cannot buy; fold it into the engagement), the first was the standing
recommendation and the only one that needs no new proof to survive the comparison. The
non-creditable structure stays; only the number moved. Reversible by a word from the
principal — her confirmation is flagged in `HANDOFF.md`, and the $395 fallback tier is
retired with the $495 anchor.

**The evidence ladder — what each step actually licenses** (corrected 2026-07-27; an earlier
draft of this block said the sandbox rehearsal "sets the hours," which contradicts the standing
rule that no fixed fee is quoted before one **real** file is timed):

| Step | What it produces | What it licenses |
|---|---|---|
| Sandbox rehearsal | A **timed lower bound** on the billable phases (audit, baseline, mapping, verification, exception review, packet) and a working verifier | Hours × rate scoping that is no longer a guess. **Not** a fixed fee |
| First paid pilot, hourly or tightly capped | Real-file variance: dirty history, volume, payroll YTD, integrations | A defensible fixed-fee *range* for similar files |
| Three to five delivered files | Distribution, not an anecdote | Fixed-fee quoting with known margin |

The sandbox cannot price the conversion step at all (vendor-run, and vendors have not confirmed
they accept sandbox sources). What it *can* time is precisely the work Fenton bills for — which
is the useful half.

**The conversion itself is never a line item.** Q2X (Xero-subsidized, full history) and Jet
Convert (free, current + prior fiscal year) do it for nothing; selling what the vendor gives
away loses on price to zero. We charge for the judgment around it: the audit, the cleanup, the
verification, and the relationship after.

**Competitive honesty on the diagnostic.** Q2X gates with a *free* eligibility call. Ours must
be visibly deeper — a written, file-specific finding, not a screen — or it will not sell at any
price. If it cannot be made visibly deeper, it should not be sold.

**Partner-billed subscriptions (packaging, not a revenue line).** Where a migrated client opts
in, Fenton becomes the Xero subscriber and bundles software into one flat monthly invoice —
which makes "a flat fee instead of a bill that keeps climbing" literally true on the invoice.
Margin is a few dollars to ~$20/client/month: it pays for the admin, not the practice. Three
engagement-letter clauses are non-negotiable before offering it — **transparent pass-through**
(the software component moves with Xero's published list price, so a Xero increase is never
Fenton's number), **free exit transfer** (subscription hands back on request, no questions),
and **transparent bundling** (never a silent markup). Tier discount percentages sit behind the
partner login: `[verify at signup before modeling any margin]`.

**Banned from client-facing math, permanently:** the "$4,000 average failed-migration repair"
and "43% error rate" figures (vendor marketing), subscriber counts, and — per the standing Copy
Rules — **every percentage**. Price movement is quoted as destination dollars, anchored to the
recipient's own invoice.

## The discovery question that sets the price

> *"What are you paying Intuit today, the QuickBooks subscription plus any bookkeeping help like Live or Expert Assisted?"*

For Segment A, the Airtable `Products` field pre-loads this anchor before the call.

## The four inputs Miriam must confirm to lock numbers

1. Solo capacity (accounts serviceable at once) — sets tier ceilings.
2. Target effective rate / margin — sets the floors.
3. Real cleanup hours per backlog-month — sets the cleanup tiers.
4. Payroll attach-only or also standalone.

*(A fifth input was closed 2026-08-03: Facts 'n Figures' "$425/wk". It came from the
operator's own lead-capture note (record `recPh30NXqsCdmYB1`, `_archive/kit-tasks/todo.md`
2026-07-14 entry), not from Miriam, and its meaning is no longer reconstructable. Classified
**unverified — not usable in copy or calibration** per the verified-numbers Copy Rule. If the
operator ever recalls whether it was their current spend or a quote already made, one line
here reopens it.)*
