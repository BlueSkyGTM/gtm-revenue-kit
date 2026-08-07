# White-Label — Lead Scoring & Sourcing Strategy

*Written 2026-07-24. Standalone: you should not need to read the chat log. Operational pipeline state lived in `tasks/todo.md`, deleted 2026-07-29 (the 2026-07-24 snapshot survives at `../../../_archive/kit-HANDOFF.md`); this covers how leads are scored and where the next ones should come from.*

---

## Where the list stands

**The load is finished. 617 contacts are in Airtable, every one scored.** (2026-07-24, one duplicate removed 2026-07-25)

| | |
|---|---|
| Contacts in Airtable | **617**, all scored, no backlog |
| Every contact has | A LinkedIn profile URL. Email is **not** collected — this is a LinkedIn campaign |
| Base / table | `appEWdrpe1eIGB1cD` / `tblafsL94yxtXp9fa` (WL-1) |
| Verified | 0 missing LinkedIn, 0 missing Score, **0 duplicate LinkedIn URLs** across all 617 (re-checked 2026-07-25 with a stricter key, see below) |

The final 314 came from `_load2.json` (227, `Source_Batch = tier34-2026-07-24`) and `_load3.json` (87, `tier5-2026-07-24`). 359 rows were queued; 45 were already in Airtable and were skipped on a normalised-LinkedIn-URL match.

**Verification method, because a count alone would not have caught a bad write.** The Score formula was reimplemented independently in Python and run against all 314 inputs, then compared cell-by-cell to what Airtable actually computed: **0 mismatches**. That checks the formula itself, not just that rows arrived. Numbers here are read back from Airtable, never from a tool's own success message — a lesson from repeat write-verification failures logged in the since-deleted `tasks/todo.md` (2026-07-29).

**Channel reality check:** LinkedIn caps connection requests at ~100/week per account (identical on Free, Premium and Sales Navigator — paying does not raise it). That is ~430/month. **617 contacts is far more than a 3-client goal can consume.** Working the whole list is not the objective and will not happen: at ~50 meaningful touches a month, three clients arrive somewhere around month 4 to 6 having used 150 to 250 contacts. Sourcing more firms does not move any constraint that matters.

---

## The scoring model

Implemented as an Airtable **formula field** named `Score` (`fldAGvTJNDeV9WZW6`). Self-maintaining: every existing record is scored, and anything added later scores itself. There is no batch job to re-run.

**Score = Authority + Capacity-gap shape + Service fit. Range 40-100.**

### 1. Decision authority (40 / 30 / 15)

| Points | Matches in `Title` |
|---|---|
| 40 | owner, founder, chief executive, ceo, president, managing partner, managing member, proprietor |
| 30 | partner, principal, shareholder, managing director |
| 15 | anything else |

Rationale: at a small firm the owner *is* the buying committee. A Partner can champion but may need consensus. Everything else is an influencer at best.

### 2. Capacity-gap shape (30 / 20 / 10)

| Points | Test |
|---|---|
| 30 | Contact's surname appears in the firm name (eponymous) |
| 20 | Firm name contains `&`, `Associates`, `LLP`, or `PLLC` |
| 10 | Everything else |

**This is the most important component and the least obvious.** A firm named after the person you are writing to is the one most likely to be capacity-constrained: one principal, no bench, every new client competes directly with their own billable hours. That is precisely the pain Fenton's white-label capacity removes. A branded multi-partner firm usually already has a back office and does not feel the squeeze.

### 3. Service fit (30 / 20 / 15)

| Points | Firm name contains |
|---|---|
| 30 | bookkeep / booxkeep |
| 20 | accounting / accountan |
| 15 | CPA or tax only |

Rationale: a firm that calls itself a *bookkeeping* firm sells the exact service Fenton delivers, so the handoff is clean. A tax-first CPA shop may not have bookkeeping volume to outsource at all.

### Distribution across all scored people

Read directly out of Airtable 2026-07-24, after the final load. Totals 618 here; one duplicate was removed the next day, so the current total is 617 and the 90-100 band is 39.

| Band | Count | Share |
|---|---|---|
| 90-100 | 40 | 6% |
| 75-89 | 249 | 40% |
| 60-74 | 251 | 41% |
| 45-59 | 61 | 10% |
| under 45 | 17 | 3% |

Sort `Score` descending and work top-down. The 90s are eponymous bookkeeping firms run by their owner.

**The top two bands are ~288 people.** Against a 3-client goal the list below 75 will almost certainly never be worked, so treat 60-74 as reserve rather than queue.

*(An earlier version of this table reported 677 people and bands of 43/251/279/84/20. That was wrong on both the total and the distribution — it was never reconciled against the table. The numbers above are a direct read.)*

---

## QuickBooks certification — enriched 2026-07-25, deliberately NOT in the score

The list was cross-referenced against Intuit's public ProAdvisor directory: **197 locations swept, 22,393 raw listings scanned covering 11,351 unique advisors, 77 of 617 firms matched (12.5%)** and written to `QB_ProAdvisor` (`Confirmed` 49 / `Probable` 28) with the matched listing kept in `QB_Directory_Listing` so every value is auditable.

**Match quality is good.** In a 12-record spot check, **7 had the directory's certified advisor as the exact same person** as our contact (David Lutz at Lutz Tax Services, Wayne Higdon at 25th Hour, Steven Graber, Lee Kidder, Alex Pacso, Kristy Gadson, Gisselle FeQuiere). Person-level agreement is much stronger evidence than firm-name agreement, and it says the matching worked.

**Blank does not mean "not certified."** The directory lists individual advisors under a company name, so a certified person at a firm trading under a different name will not match. Treat blank as unknown.

### Why it is not folded into `Score`

**It is uncorrelated with the existing score, which makes it genuinely new information:**

| | Mean `Score` |
|---|---|
| Certified (n=77) | **70.5** |
| Not matched (n=540) | **71.4** |

Certification rate by band shows no trend either: 17.5% at 90-100, 10.0% at 75-89, 13.9% at 60-74, 14.1% below 60.

So it adds signal the model does not already have. It is still kept out of the formula, for two reasons:

1. **There is no outcome data.** Zero clients exist, so any weight attached to certification would be invented rather than fitted. The repo has been burned before by numbers that were assumed and then quoted as if measured.
2. **It plausibly cuts both ways.** Shared tooling makes Miriam's ProAdvisor credential instantly legible to a certified firm and removes a layer of explanation. But a firm that holds the certification has demonstrable in-house QuickBooks capability, which is an argument it needs *less* outside help, not more.

**Use it as a filter and a tiebreaker, not a ranking input.** The first real conversations will settle which direction it points, and that is the moment to reconsider putting it in the formula.

---

## What the score does NOT measure — read before trusting it

**It measures fit, not intent.** Nothing in it indicates the firm is currently over capacity, hiring, turning work away, or unhappy with a current provider. A 95 is a firm that *would* benefit; it is not a firm that is *looking*. Closing that gap is the single biggest available improvement, and option 1 below is how.

Other known limits:

- **Only two inputs**: `Title` and `Firm`. No headcount, revenue, client count or tenure.
- **The eponymous heuristic over-credits some large firms.** "Larson & Company" scores as eponymous for a Larson but is a 60+ person firm. It also under-credits a solo operator trading under a brand name.
- **Titles come from third-party data and go stale.** Several in this list were captured wrong by Clay — credentials landed in the surname field (`CPAPFS`, `MST`, `QKA`, `CITP`). Assume some noise remains.
- **The surname bug silently under-scores the best leads, so it is worth fixing on every load.** The eponymous test asks whether the surname appears in the firm name, so a credential sitting in that field can only ever fail it. In the final 314-row batch, 21 surnames were contaminated and 18 were recovered from the LinkedIn slug; **4 of those turned out to be eponymous firms** (Sheppard at Rolleri & Sheppard, Pompo at F. J. Pompo & Co., Lipkin at Lipkin CPA, Moreno at Sonya Moreno CPA), each jumping 20 to 30 on the capacity-gap component. Left alone they would have ranked as ordinary partnerships. `sync/load-white-label-contacts.py` does this repair automatically.
- **2 surnames were not recoverable** and are still initials or a credential: Oriana A. (SVA Certified Public Accountants) and Marcelino CFS (Cash Tracks Financial) — the latter's LinkedIn is a company handle, not a person.
- **Service fit reads the firm name only.** A CPA firm doing heavy bookkeeping behind a tax-branded name scores 15 when it deserves 30.
- **No suppression against the QuickBooks Bounce list.** Different buyer, but worth a channel-conflict check before outreach.

Treat the score as a work-ordering tool, not a qualification gate. Nothing below 45 should be discarded on score alone.

---

## Sourcing: why the current method is exhausted

The pipeline is Clay + Serper.dev Google Maps (mechanics in `../../../_archive/kit-HANDOFF.md`). Sourcing costs ~1 Serper credit per 10 businesses; `Find Contacts at Company` costs ~0.5 Clay credits and appears to bill **per contact returned, not per row attempted** — misses look free.

**Yield decay across the runs:**

| Run | Rows | New people | Yield |
|---|---|---|---|
| Tier 2 (20 metros) | 756 | 172 | 23% |
| Tiers 3-4 (batch II) | 1,700 | 276 | 16% |
| Later batch (18 files) | 900 | **88** | **10%** |

Roughly 90 metros have been swept with two keywords (`CPA firm`, `bookkeeping firm`). Maps now returns firms already in the table regardless of which city is queried. **More metros at the same two keywords is not worth running.**

---

## Four options for the next extraction method

### Option 1 — Job postings (highest quality, needs a new build)

Scrape Indeed / LinkedIn job ads for firms hiring **bookkeepers, staff accountants, or accounting associates**, then enrich the firm.

- **Why it wins:** a firm advertising for a bookkeeper has a capacity gap *right now* and is already spending money to close it. White-label is a faster, cheaper answer than a hire. This converts a fit list into an intent list, which is exactly what the score cannot give you.
- **Cost:** unknown; needs a new scraper (Serper supports a jobs endpoint, or Indeed via HTTP column).
- **Volume:** low. Tens per metro, not hundreds. That is fine — intent beats volume.
- **Note:** this was in the original brief as a Tier-1 signal and was never built.

### Option 2 — Intuit ProAdvisor directory (best list source)

`proadvisor.intuit.com` lists QuickBooks-certified firms, searchable by location.

- **Why it wins:** perfect platform overlap. Fenton is a QuickBooks ProAdvisor; so is everyone in the directory. No retooling for the client, and the shared-tooling angle is a real opening line. Maps never surfaces this list.
- **Cost:** scraping only, no Clay enrichment needed for firm discovery.
- **Risk:** check the directory's terms before scraping at volume.

### Option 3 — Source natively from LinkedIn (best channel fit)

Search LinkedIn by title + industry (Accounting) + headcount 1-50 and pull profiles directly.

- **Why it wins:** the campaign *is* LinkedIn. Sourcing from Maps and then inferring a LinkedIn profile is a detour that loses 55% of rows at the matching step. Sourcing from LinkedIn gives the profile URL natively with no miss rate.
- **Cost:** Clay can enrich from a LinkedIn search URL; Sales Navigator improves filtering but is not required for the invite cap.
- **Risk:** LinkedIn scraping is against their User Agreement and can restrict the account you actually need for sending. Weigh carefully — the sending account is the asset here.

### Option 4 — New keyword axes on Maps (cheapest, do this first)

Same table, same config, different keyword values. Swap geography for service language:

`QuickBooks ProAdvisor` · `outsourced accounting` · `client accounting services` · `fractional CFO` · `virtual bookkeeping` · `small business accountant` · `payroll services`

- **Why it wins:** zero new build. The pipeline exists and works. Different vocabulary surfaces different firms *in metros already swept*, because Maps ranks on business category and description text.
- **`QuickBooks ProAdvisor` is the standout** — it is both a service term and a certification signal, and it overlaps Option 2's list without needing a scraper.
- **Cost:** same as before, ~0.5 credits per contact found.

---

## RUNBOOK — executing the keyword swap (Option 4)

**Ready to go: `clay-import-keywordswap-A.csv`** in this folder. 40 rows = **10 already-swept metros × 4 new keywords.**

### What changes and what does not

**Change only the `Keywords 1` values. Keep the metros.** The 10 cities in this file (New York, LA, Chicago, Dallas, Houston, Atlanta, Miami, Phoenix, Philadelphia, Denver) have all been swept already with `CPA firm` and `bookkeeping firm`.

**Why that still returns new firms:** Google Maps ranks on business category and listing description text, not just on the literal business name. A firm that describes itself as *"outsourced accounting"* or *"fractional CFO"* may never surface for `CPA firm` even in a city you have swept ten times. You are not re-querying the same index — you are querying a different slice of it in the same geography.

**The four new keywords, and why each:**

| Keyword | Why |
|---|---|
| `QuickBooks ProAdvisor` | The standout. Both a service term and a certification signal, and it overlaps the Intuit directory (Option 2) without needing a scraper. Direct platform match with Fenton. |
| `outsourced accounting` | Firms already comfortable with the outsourcing concept — no education needed on the model. |
| `client accounting services` | Industry term (CAS) for exactly the function Fenton delivers. Firms using it have a named service line and therefore volume. |
| `fractional CFO` | Advisory-led firms that typically push compliance work down or out. Strong capacity-gap shape. |

### Why 41 lines / 40 rows per file

The CSV is 41 lines — one header plus **40 data rows** — and that is deliberate, not arbitrary. Three separate limits stack:

1. **Destination table ceiling: 1,000 rows.** At 4 keywords × 2 pages × ~10 results, 40 search rows produces ~800 business records. That fits under the ceiling with headroom for the duplicates that always slip through. Go much past 40 rows and the table fills mid-run and silently drops results.
2. **Serper rate limiting.** Firing all 40 rows at once trips a `429`, which cascades: no response means no `places` array, so the adjacent WTOR throws `Invalid routing inputs` and writes nothing. **Run ~10 rows at a time**, letting each chunk finish. The 40-row file is sized so that is four clean passes.
3. **Enrichment batch cap: 50 rows.** `Find Contacts at Company` processes 50 at a time regardless of table size, so a ~800-record destination becomes ~16 enrichment runs. Sizing the import at 40 keeps that number manageable in one sitting.

**Cap pages at 2.** Pages 3-5 attract nearly all the 429s and mostly repeat pages 1-2.

### Step by step

1. **Empty the destination table.** Delete the rows — do **not** duplicate the table or create a new one. Duplicating breaks the WTOR pointer and is what caused two separate "the copy never received anything" failures. An emptied table receives fine and the pointer never moves.
2. Upload `clay-import-keywordswap-A.csv` to the scraper table. Columns are `City,State,Country,Keywords 1` — full state names, `Country` always `United States`.
3. Confirm **Auto-run is OFF** on every enrichment column. Auto-run once burned 300 credits unattended.
4. Run `Page 1`, then `Page 2`, **~10 rows at a time.**
5. Watch the destination row count climb as the WTORs fire. If `Page N` shows 200s but the count stays at 0, stop — that is a genuine pointer problem, not rate limiting.
6. **Dedupe the destination by domain** before enriching. This is the step that doubles output per batch.
7. Run `Find Contacts at Company` (no email waterfall), 50 rows at a time, `Limit` = 2.
8. Export the **destination** table only. **Never export the scraper table** — the live Serper API key sits in a column on it.
9. Load to Airtable with `python sync/load-white-label-contacts.py <file.json>`. It dedupes against what is already there on a normalised LinkedIn URL, repairs credential-in-surname damage, and flags retired/non-buyer/company-page contacts for review. Safe to re-run: a partial load just resumes. Scores compute automatically. Needs `AIRTABLE_TOKEN` in `.env` (see the script's docstring); without it, the Airtable MCP connector works too but has to be driven in 50-record batches by hand.

### Expected yield

Two keywords across fresh metros returned 16-23%. These are **new keywords in swept metros**, so treat 10-20% as the planning range. If it comes back under 10%, Maps is genuinely exhausted for this ICP and the answer is Option 1 or 2, not more keywords.

---

## Recommendation

**Run Option 4 now, build Option 1 next.**

Option 4 costs nothing new and refills the well immediately — it is the only one runnable before the Clay credits expire. Option 1 is where the quality actually is, and it changes the campaign from "firms that would benefit" to "firms that are looking", which is the difference the score cannot make on its own.

Option 2 is a strong second if the directory scrape is permissible. Option 3 is tempting but puts the sending account at risk, and that account is the whole channel.

---

## Data audit, 2026-07-25 (all 618 records)

**The seven fields the LinkedIn campaign needs are 100% complete:** `Firm`, `LinkedIn`, `First Name`, `Last Name`, `Title`, `Score`, `Source_Batch`. **Zero duplicate LinkedIn URLs** across the whole table.

**Three columns are completely empty and should be deleted:**

| Column | Why |
|---|---|
| `Keyword` | The Clay destination table never carried which search term surfaced the firm. Not recoverable per-record. |
| `Synced_At` | Built for the parked Clay→Airtable HTTP sync. Never used. |
| `Lead_Score` | Superseded by the `Score` formula. |

**Sparse columns and their causes:**

| Column | Fill | Cause |
|---|---|---|
| `Email` / `Email_Status` | 18% / 49% | Only the first ~113 records came from the email era. Expected. |
| `Address` · `Metro` | 17% | Dropped from bulk loads to keep payloads small. Recoverable from the local CSVs. |
| `Website` | 78% | Same. Redundant with `Domain`, which is ~100%. |
| `Notes` | 24% | By design — written only where something needed flagging. |
| `ICP_Flag` | 50% | Records loaded without an explicit flag. |

### Backfill in progress — 150 of 500 done

A backfill was computed and **`_backfill.json` in this folder holds all 500 update payloads** (gitignored; local only). The first **150 records are already applied**. To finish, run the remaining 350 in chunks of 50 via `update_records_for_table` against base `appEWdrpe1eIGB1cD` / table `tblafsL94yxtXp9fa` — the file is a ready-made array of `{id, fields}` objects, so slices `[150:200]`, `[200:250]` … `[450:500]` are seven calls.

What it sets, and only where the cell is currently blank:
- `ICP_Flag` → `Fit` (records needing review were explicitly flagged, so blank means clean). **Existing `Review` values are preserved.**
- `Address` → matched from the local source CSVs by LinkedIn slug
- `Metro` → derived from City + State

**One trap worth knowing:** the metro lookup must key on **city *and* state**. A city-only key maps Portland ME to the Portland OR metro, and does the same to Brentwood (MO/TN), Arlington (VA/TX), Columbus (OH/GA), Richmond (VA/CA) and Salem (OR/MA). The generator in `_bf.py` already keys on both — do not simplify it.

### Review queue: 44 of 618 (7%)

Every one carries a note explaining why. They fall into four groups:

- **Identity unconfirmed** (~15) — LinkedIn slug or legacy email handle does not match the contact name
- **Too large for the ICP** (~8) — Doeren Mayhew, KLR, Freed Maxick (absorbed into Withum), Sorren
- **Wrong role** (~10) — HR, bank consulting, audit-side, "Entrepreneur" as a title
- **Competitor** (~4) — Maxim Liberty, Reconciled

Several score high despite the flag — Hill Bookkeeping is a 100, Raymond Lyle and Pennington are 85. Those deserve a manual look rather than staying parked.

## Open items

- **8 contacts are tagged `ICP_Flag = Review`** with the reason in `Notes`. Clear these before they get an invite. Two are real problems: **Pennington & Associates CPA** is a wrong-person match (contact reads Aaron Pennington, the LinkedIn URL belongs to Bob Cerros), and **Concannon Miller**'s contact is a *Retired* Managing Partner, who scores 40 for authority but cannot buy. The other six are LinkedIn URLs whose slug matches neither the first nor last name, so they may be company pages rather than people.
- **Delete the `Lead_Score` column in the Airtable UI.** It is renamed `Lead_Score (DEPRECATED - delete this field)` with an explanatory description, because the MCP surface has no delete-field operation. It holds hand-entered values for 50 records and **contradicts `Score` on 3 of them**; the formula is right in all 3 cases. One click in the UI.
- **Decide the LinkedIn sending account** before outreach starts. A new account is throttled to 20-50 invites/week and risks restriction; an established profile gets ~100 and possibly more.
- **The score still measures fit, not intent.** Option 1 (job postings) is the fix and is unbuilt. This is the single biggest available improvement to the list.

### Closed

- ~~313 contacts still to load~~ **Done 2026-07-24.** 314 loaded, verified at 618 total.
- ~~2 records did not match a score~~ **Done.** 0 records are missing a score.
- ~~Rotate the Serper API key~~ **Moot (operator, 2026-07-24):** the scraper table that carried the key in a column is being deleted, which retires the exposure.
