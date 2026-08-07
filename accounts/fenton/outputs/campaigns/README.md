# Campaigns

Fenton runs multiple outbound campaigns off the same context layer (`context/`) and the same repo skills. Each campaign is its own folder here; each has its own namespaced lead lists under `outputs/lists/<campaign>/`.

| Campaign | Status | Folder | Target | Offer |
|----------|--------|--------|--------|-------|
| **QuickBooks Bounce** | Active (built, pre-launch). **Two offer tracks as of 2026-07-27:** bookkeeping (standing) and **migration** (QB→Xero, drafted + audited, awaiting the principal's test decision) | `2026-07-12-quickbooks-bounce/` | Small business owners on QuickBooks Online / QuickBooks Live who are unhappy with the AI and the price climb | Ongoing bookkeeping + payroll (payers) / one-time cleanup (non-payers) / **guided exit to Xero + the books after** |
| **White-Label Accounting** | Lists built and scored (2026-07-26); **full positioning set built 2026-07-27** (`context/positioning-white-label.md`, `messaging-house-white-label.md`, `competitor-radar-white-label.md`) — copy still deferred until Bounce is live and pricing is decided | `white-label-accounting/` | Accounting / CPA firms with capacity constraints who want to outsource QuickBooks delivery behind the scenes | Retained capacity (Package B structure) + white-label cleanup / migration files |
| Churches | Parked | — | Churches / religious nonprofits on QuickBooks (a recurring vertical already visible in the lead list) | TBD |

## Notes

- **QuickBooks Bounce** is the current push. It targets the small-business owner directly. See its `brief.md`.
- **White-Label Accounting** groundwork is laid: own ICP (`context/icp-definition-white-label.md`), persona (`context/personas/firm-owner.md`), signals (white-label section of the signal library), a sourcing waterfall (ProAdvisor directory + Google Maps free breadth → Clay-credit depth, 50-firm pilot gate), and — as of 2026-07-27 — the full seven-artifact positioning set per `playbooks/impact-positioning.md` (positioning, messaging house, own competitor radar; beachhead = capacity-trapped delivery firms). Copy waits for the Bounce test to be live **and the principal's pricing decision** (every WL dollar figure pends it). Do not reuse the Bounce ICP or list — channel-conflict suppression applies both ways.
- **Churches** can wait. Flagged here so it is not lost; a chunk of the existing list is churches/nonprofits, so this is a real adjacency.

---

## Research and reference docs

**Every research doc lives here so it stops being invisible.** Four docs in this tree had zero inbound references before 2026-07-26, including a launch-ready call sheet. Anything written under a campaign folder gets a line in this table on the same commit.

### QuickBooks Bounce

| Doc | What it is |
|---|---|
| `2026-07-12-quickbooks-bounce/brief.md` | The campaign brief. Start here. |
| `2026-07-12-quickbooks-bounce/call-sheet-research-head-20.md` | **The 20 highest-ICP accounts as a working call sheet** — phone, local call window, a dated why-now line, and an outcome field per account. Built for the free phone play while a sending domain warms. |
| `outputs/account-research/` | **Per-account research briefs**, one file per account (24 from the Bounce batch), feeding the call sheet above. This is what real account research looks like in this repo, per `skills/account-research/SKILL.md`. |
| `2026-07-12-quickbooks-bounce/segmentation-audit.md` | **Does Bounce hide multiple markets the way WL-1 did? Yes.** Three motive segments plus two cross-cutting ones, live counts off Airtable. Flags that 19% of the list has been a customer for two months or less and is being sent a price-fatigue message, and documents the `LIVE_SERVICES_PREMIUM` filter trap. |
| `2026-07-12-quickbooks-bounce/metrics.md` · `results.md` | Targets and what actually happened. |
| `2026-07-12-quickbooks-bounce/sequences/` | Copy. `rollout-a.md` is the live sequence (restricted 2026-08-03 to verified switchers), `rollout-b-diy-draft.md` the DIY conversion track (draft, second wave), `test.md` the variants, `instantly-live-snapshot-2026-07-25.md` the sending state. |
| `2026-07-12-quickbooks-bounce/sequences/migration-track-draft.md` | **The migration offer track: three drafted variants, one shipper (`paid-exit`), nothing loaded.** Per-account eligibility gate, reply-handling overlay, per-offer results scaffold. Built via `playbooks/impact-positioning.md`. |
| `outputs/2026-07-27-xero-motion-debrief.md` (deleted 2026-07-29) | **The commercial case for the migration motion**, two-model reviewed. Its settled facts were absorbed into the migration specs and `context/pricing-strategy.md`; the memo itself is gone. |
| `outputs/audits/2026-07-27-positioning-redteam-migration-track.md` | Step-7 audit of the migration track. Three real findings, incl. one variant held for promising a capability the practice lacks. **Self-run** (codex quota) — flagged for cross-model re-run. |
| `outputs/2026-07-14-pricing-recommendations-flagship-services.md` (deleted 2026-07-29) | Internal planning figures only. Never a quote, never in copy. Superseded by `context/pricing-strategy.md`. |

### White-Label Accounting

**Two lists, two different offers. Do not merge them.** WL-1 is QuickBooks-native firms pitched on overflow capacity. WL-2 is Xero-directory firms pitched on migration. Different buyer fear, different proof required.

| Doc | What it is |
|---|---|
| `white-label-accounting/strategy.md` | The governing doc — two fears, the wedge, the 1-1-1 frame. Start here. |
| `white-label-accounting/brief.md` | Campaign brief. |
| `white-label-accounting/report-wl1-overflow-top20.md` | **WL-1 market read — the one report for this side of the table.** Built from individual site visits to the top 20. Finds the list is four different markets, only one of which is the overflow buyer, and that 15% of the top-scoring records are dead, rebranded or brand new. Ends in recommendations. |
| `white-label-accounting/report-wl2-migration-feasibility.md` | **WL-2 market read — the one report for that side.** The category is real, but badge-holders are the supply side, not the demand side. Ends in recommendations, including a 14-conversation test that costs nothing. |
| `white-label-accounting/migration-cleanup-thesis.md` | **The Exit Practice — operator thesis, specified and stress-tested.** One service (get off QuickBooks, fix what it broke), sold to both SMBs and firms. Carries the corrected pricing stack and the two things standing between it and revenue. |
| `white-label-accounting/alternative-model-capacity-subscription.md` | **The counter-proposal.** Sell firms a standing monthly block of hours instead of per-file projects. Recurring by construction, no certification needed. Ends by recommending the two be sequenced rather than chosen between. |
| `white-label-accounting/xero-migration-research.md` | Migration economics. The migration is near-free. Three separate paid lines sit around it: cleanup (20-40 hrs), integration consulting ($2-5K), failed-migration repair (~$4K). |
| `white-label-accounting/wl2-enrichment-runbook.md` | How WL-2 was enriched, what each Clay run cost and yielded, and the traps. Read before spending another credit. |
| `white-label-accounting/wl2-xero-directory-list.md` | Where WL-2 came from and what the Xero directory fields mean. |
| `white-label-accounting/scoring-and-sourcing.md` · `abm-research-play.md` | Scoring model and the ABM play. |

**WL-1 per-account evidence:** `outputs/account-research/2026-07-26-mattingly-ott-research.md`, `outputs/account-research/2026-07-26-christina-rea-bookkeeping-research.md`, `outputs/account-research/2026-07-26-hale-bookkeeping-solutions-research.md`, `outputs/account-research/2026-07-26-smartup-accounting-research.md`. Four briefs backing the WL-1 market read, written to `skills/account-research/SKILL.md` adapted for owner-operated practices.

**Builder:** the WL-2 enrichment CSV builder (`tools/build-wl2-clay-csv.py`) was deleted 2026-07-29 with the rest of `practice/tools/`; regenerating the CSVs means rebuilding from `wl2-enrichment-runbook.md`, which documents the method.

---

## Session reports

| Doc | What it is |
|---|---|
| `2026-07-26-session-report.md` / `.pdf` (both deleted 2026-07-29) | **Capstone report for 2026-07-26.** Its durable findings were absorbed into the positioning sets and the scoring model; the dated report itself is gone. |

---

## Convention

New campaign = new folder with `brief.md`, `sequences/`, `metrics.md`, `results.md` (per `workflows/campaign-build.md`). Lead lists (PII, gitignored) go in `outputs/lists/<campaign>/`.

**Any new research or reference doc gets a row in the tables above on the same commit that creates it.** A doc nothing links to does not exist.

- `../2026-07-27-pricing-briefing.md` (deleted 2026-07-29) — two-reviewer pricing packages (A entry-safe / B credential-priced); its structure survives in `context/positioning-white-label.md` → Pricing posture and `context/pricing-strategy.md`
