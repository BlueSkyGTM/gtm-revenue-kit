# WL-2 enrichment runbook — finding the missing decision-makers

*Written 2026-07-25. The file to upload is `clay-import-wl2-findcontacts.csv` in this folder (gitignored, local only).*

---

## What the file is

**334 Xero-advisor firms that have no named contact**, ready for Clay's `Find Contacts at Company`.

Getting from 618 to 334 took four filters, and three of them are free savings:

| Step | Count | Why |
|---|---|---|
| WL-2 total | 618 | |
| Already have a named contact on the listing | −240 | The directory published staff profiles. **Work these first, they cost nothing.** |
| Already in WL-1 with a contact (domain match) | −7 | We already have a human at these firms |
| National firms, franchises, known competitors | −11 | Scrubbed, Aprio, Paperchase, Bench, Pilot, Xendoo, Bookkeeper360, Reconciled, Acuity and similar |
| No usable domain, so Find Contacts cannot run | −15 | Shared hosts or blank websites. Parked, not lost |
| Duplicate domains within the set | −11 | **Deduped before enriching, per the rule the last run learned the hard way** |
| **Ready to enrich** | **334** | |

**Estimated cost: ~167 Clay credits** at the measured 0.5 credits/row.

Rows are sorted by `score` descending, so if the run is cut short for any reason the best firms are already done.

### Columns

`listing_id` · `firm` · `domain` · `website` · `city` · `state` · `phone` · `partner_tier` · `partner_since` · `score` · `migration_specialist`

**`listing_id` is the join key back to Airtable.** Keep it through the whole round trip or the enriched contacts cannot be matched to their records.

---

## Read this before spending anything

**The 240 firms that already have names are free and unworked.** Enrichment is not the bottleneck; conversations are. At roughly 50 meaningful touches a month against a 3-client goal, 240 contactable firms is already several months of outreach. Running Clay first is optional, not required.

**WL-2 is the weaker-matched list.** The chosen offer is QuickBooks Desktop-to-Online cleanup, and WL-1 is 617 QuickBooks-native firms with a named contact and personal LinkedIn URL on **every** record. WL-2 firms committed to Xero. They are a genuinely different population and worth having, but do not spend credits here on the assumption it is the primary list. It is not.

**The honest case for running it anyway:** credits expire and LinkedIn profiles do not. 167 credits is cheap, and a banked contact keeps. If the balance is about to lapse, this is a better use of it than sourcing more firms nobody will contact.

---

## The enrichment

**One column only: `Find Contacts at Company`.** No email waterfall.

This campaign is LinkedIn outreach, so an email address is not needed and the waterfall is where the money went last time: it bills every provider it tries, hit or miss, so a row that finds nobody ran all nine providers and cost **31.3 credits** against 0.5 for this column. The waterfall was deleted on 2026-07-24 and should stay deleted.

**Settings:**

| Setting | Value | Why |
|---|---|---|
| Company Identifier | **`domain`** column | Cleaner than the firm name and it is already deduped |
| Job title keywords | Owner, Partner, Principal, President, Managing Partner, Managing Director, Founder, CEO | Matches the authority tiers in both scoring models |
| Seniority floor | **Leave loose** | Solo practitioners are frequently not tagged at owner seniority by data providers, and solo is precisely the segment we want |
| `Limit` | **2** | Costs nothing extra. Expect ~1.01 contacts per firm in practice, so plan on one |
| **Auto-run** | **OFF**, per column and at table level | Non-negotiable. Auto-run once burned 300 credits unattended when deleted rows freed slots and paywalled rows moved up as "new" |

**Run in batches of 50** and export after each. Do not queue the whole file and walk away.

---

## The loop

1. Upload the CSV to the Clay table.
2. Confirm auto-run is OFF everywhere before touching anything.
3. Run `Find Contacts at Company` on 50 rows.
4. **Export to CSV.** Verify the file exists on disk.
5. Load into Airtable, matching on `listing_id`, writing `Contact_Name`, `Contact_Title` and `LinkedIn`.
6. Verify the Airtable count matches the tranche.
7. Only then clear those rows in Clay and take the next 50.

**Step 4 is not optional.** A tranche of ~15 enriched contacts was deleted before export on 2026-07-24 and was unrecoverable: Clay keeps no copy, and the credits that bought it were gone too.

---

## What to expect

Prior measured rates on this pipeline, on Maps-sourced data:

- **~41% of firms yielded a contact at all**
- ~1.01 contacts per firm where one was found
- Roughly 2.2 credits per contact acquired, all-in

Applied here: **334 rows → very roughly 135 contacts**, though WL-2 firms are Xero-directory listed with real websites, which may find better than a Maps sweep. Treat 41% as the planning floor, not a forecast.

**Kill threshold:** if the first 50 rows yield fewer than 15 contacts, stop and reassess rather than grinding through all seven batches. That is a materially worse rate than the pipeline has produced before and would mean something is wrong with the inputs.

---

## Screen on the way in

The last run learned this the expensive way. Two checks before any contact is recorded:

**Does the person plausibly belong to that firm?** Enrichment returns wrong-person matches. WL-1 has a live example: Pennington & Associates, where the contact reads Aaron Pennington but the LinkedIn URL belongs to Bob Cerros. One survived into the table and is flagged for review.

**Is this a buyer or a competitor?** 74 of the 334 hold Xero's Migration specialist badge, and a solo practice is Fenton's own shape. A one-person Xero shop is simultaneously the sharpest capacity pain and the most likely competitor. Set `ICP_Flag` as you go rather than promising to do it later.

---

## The 15 with no domain

Parked, not discarded. They have a firm name, phone and address but no usable website, so `Find Contacts at Company` has nothing to key on. If they are ever wanted, the route is a manual LinkedIn company search by firm name and city, which is cheap at that volume and costs no credits.


---

## Batch 1 results (50 rows, run 2026-07-26)

**50% returned a person, which beats the pipeline's 41% benchmark. The run is not underperforming.** But the usable number is lower and that is the figure to plan against.

| Outcome | Count | Retryable |
|---|---|---|
| Returned 1-2 people | **25 (50%)** | — |
| **No Profile Found** — company resolved, no person exists | 17 (34%) | **No.** Same enrichment, same provider, same answer. Drop them. |
| **Company Not Found** — the domain did not resolve | 8 (16%) | **Worth one cheap test.** This is a lookup failure, not an absence. |

### The 8 "Company Not Found" are worth one retry, the 17 are not

Re-run only the 8 with **firm name + city** as the Company Identifier instead of `domain`. Several have visibly broken domains: `wwww.bnguru.com` carries a typo'd `wwww`, and `theheroesgroup.com` does not match the firm name "DiMercurio Advisors". That is 4 credits to find out. If it recovers fewer than 3, drop them permanently.

The 17 "No Profile Found" get the standing drop-don't-chase treatment. Delete and move on.

### The real attrition is in the hits, not the blanks

Of the 25 that returned somebody, **only 17 are clean, usable decision-makers**:

- **4 have a credential in the surname** (Mohamed **ABV**, Steve **CFF**, Laura **CAM**, Edwin **CITP**). Identical to the WL-1 bug. `sync/load-white-label-contacts.py` repairs this automatically from the LinkedIn slug, so it costs nothing as long as the loader is used.
- **3 are the wrong person at the right firm** — Head of Marketing, HR Business Partner, Director of Sales Marketing. Not buyers.
- **2 were national firms that slipped the exclusion screen** — Armanino LLP and Analytix Solutions.
- **4 have a first name absent from the LinkedIn slug**, which is the wrong-person signature. `Accounting with Confidence` returned Beth Whitworth at `/in/asg-stl/`. Flag these `Review` rather than loading them blind.

**Plan against ~34% clean contacts per batch, not 50%.** Across the full 334 rows that is roughly 115 usable people for about 167 credits, or **~1.5 credits per usable contact** — better than the 2.2 the previous run averaged.

### Exclusion screen tightened, 2026-07-26

The original screen was 11 name matches and let Armanino through. It is now 26 records flagged `Excluded`, catching H&R Block (10 separate franchise listings), PricewaterhouseCoopers, CliftonLarsonAllen, Marcum, Forvis Mazars, Carr Riggs & Ingram, Armanino, Analytix, Xendoo, Bookkeeper360, botkeeper, Scrubbed, Aprio, Paperchase and Liberty Tax.

**A note on how it is matched, because this bit three times in one session.** Short brand tokens must be matched on word boundaries, never as substrings. Screening for `ey ` (Ernst & Young) as a substring falsely caught Chan**ey**, Car**ey**, Stac**ey**, Journ**ey** and She**ey** — seven good firms nearly excluded. Multi-word brands are safe as substrings; anything under about five characters needs `(?<![a-z])token(?![a-z])`.


---

## v2 file, 2026-07-26 — after the franchise purge

**Use `clay-import-wl2-findcontacts-v2.csv`. The v1 file is deleted; do not run it.**

### What changed and why

Testing salvage paths on the records with no contact turned up the real reason so many are unreachable: **a chunk of them are not independent practices at all.** Of the original 378 unnamed records, 32 were franchise branches or national outsourcers, including **12 separate Padgett Business Services locations** and 10 H&R Block listings. They have no named staff because they are branch listings, not firms.

53 franchise and national records were deleted from WL-2 entirely (archived to `~/wl2-deleted-archive.json`, outside the repo). **WL-2 is now 565 records**, verified by re-read.

| | |
|---|---|
| WL-2 after the purge | **565** |
| Already have a named contact | 240 |
| Enriched in batch 1 | 50 |
| No usable domain, parked | 15 |
| **In the v2 file** | **275** |
| Estimated cost | **~138 credits** |
| Expected clean contacts at the measured 34% | **~94** |

### Salvage paths that were tested and rejected

Three free routes to the missing contacts were tried on live samples before recommending Clay. None is worth the labour:

| Path | Measured yield |
|---|---|
| Scrape firm websites for a name beside an owner-type title | 45% raw, **~15% clean**. The rest were place names and page furniture: "Sterling Heights", "Key Industries", "Blog The" |
| Scrape firm websites for a personal LinkedIn URL | **7%**. Small practice sites rarely link them |
| Derive a person from an eponymous firm name | ~105 candidates before the purge, heavily polluted by franchise names like "Padgett Denver" |

15% clean on a name-scrape means eyeballing roughly 300 sites to salvage perhaps 50 people, every one needing manual verification because a regex cannot tell a person from a place. Clay at 0.5 credits a row is both cheaper and more reliable.

**The one manual exception worth taking:** genuinely eponymous firms where the name *is* the person, such as Peter Holtz CPA, Stull CPA, DeLucia CPA. A LinkedIn search on name plus city takes seconds and costs nothing. Perhaps 60 to 80 firms qualify once franchises are stripped out.

### Standing reminder

**The 240 firms that already have a named contact are still completely unworked.** At roughly 50 meaningful touches a month against a 3-client goal, that alone is several months of outreach. Enrichment remains optional.


---

## Full run complete, 2026-07-26 — 325 rows, and what is actually left

The v2 file is finished. Batch 1 (50) plus v2 (275) is **325 unique rows**, which is the entire enrichable set. There is no unrun remainder.

### Results

| Outcome | Count | Share |
|---|---|---|
| Returned a person | **160** | 49% |
| No Profile Found — company resolved, nobody matched the title filter | 106 | 33% |
| Company Not Found — the domain never resolved to a LinkedIn company | 59 | 18% |

**49% beat the 41% planning floor and held across all seven batches**, not just batch 1. Two hits pointed at records deleted in the franchise purge, so **158 were written to Airtable**.

Of those 158: **120 clean**, 30 flagged `Review`, 8 flagged `Excluded`. That is a **37% clean rate against rows attempted**, slightly better than the 34% batch 1 predicted.

The 8 exclusions are all the same failure: the firm's listed website is a national brand's domain, so the enrichment dutifully returned that brand's executive. `JBBS, LLC` lists `hrblock.com` and came back with H&R Block's President and CEO. Also caught: Block Advisors, Marcum, Squar Milner, Kaufman Rossin, HBK, ATAX, and one firm whose listed website is literally `xero.com`. **A domain-level franchise screen belongs in the pipeline before Clay runs, not after.**

### Verified coverage, read directly from Airtable 2026-07-26

**Do not compute coverage from a cached `list_records_for_table` dump.** Those responses only contain the `fieldIds` that were requested. The dump used earlier in this session carried six fields and no `LinkedIn` column, which made every record look like it had no profile URL and produced a badly wrong "158 of 565" figure. The numbers below come from filtered queries against the live table.

| | Count | Share of 565 |
|---|---|---|
| Has a LinkedIn URL of any kind | 359 | 64% |
| — of those, a **company page**, not a person | 113 | 20% |
| — of those, a **personal profile** | **246** | **44%** |
| No LinkedIn URL, but has a contact name | 79 | 14% |
| No LinkedIn URL and no name | 127 | 22% |

**The Xero directory's own LinkedIn field was already loaded in a prior session.** There is no untapped pool of free profile URLs. The directory has been squeezed on that axis.

### What the directory still had, and what was taken from it

Two things came out of re-reading the raw pull, and only one was worth much.

**Staff rosters, partially used.** The directory publishes a staff list, not just one name: **322 people across 219 firms**. The original load took one person per firm and dropped the rest. On inspection the discarded 103 are overwhelmingly non-buyers — Client Services Manager, CAS Accounting Manager, Client Service Specialist — because the decision-maker was usually the one already loaded. Only 6 firms hold an extra decision-maker beyond their primary, which is not enough to justify second-contact fields on the table.

**Ten primaries were the wrong person, and the roster names the right one.** This was the real find and it is now applied. MATAX was pointed at a Lead Accounting Technologist while the Managing Partner sat in the same roster. Two of the ten also resolved an existing name/URL mismatch: the record read Gladys Godfirnon while the LinkedIn URL was already `/in/tomnbass/`, and the same pattern at GPS CONTADOR.

| Firm | Was | Now |
|---|---|---|
| MATAX | Dan Quigley | Julie DeVincenzi, Managing Partner |
| SimpliNumbers | Elena Rowland | Pamela Matthews, CEO |
| Gineris & Associates | Kellen P. Leone | Patrick Gineris, Managing Principal |
| Alavita Business Solutions | Pamela Mae Olave | Karen Brady, CEO |
| Polay Clark & Co. | Catrice Swann | Robert Polay, Founding Partner |
| Asendant, LLC | Sharon Graves | Edgar Rollins, Partner |
| Strategic Business Alliance | Kristina FitzSimons | Ken Aurigemma, Owner |
| Accountable Solutions | Gladys Godfirnon | Tom Bass, President |
| Patricia A Frame, CPA | Gary Frame | Patricia Frame, Owner |
| GPS CONTADOR | Lucia Stagnetto | Pablo Goyenechea, CEO |

### The three gaps that remain, and the right tool for each

**113 records point at a company page instead of a person.** This is the best-positioned group. A LinkedIn company URL is a *stronger* Clay input than a domain, and it structurally cannot produce the "Company Not Found" failure that killed 59 rows — the company is already identified. Re-keying on the company URL is the highest-confidence spend available.

**79 records have a name but no profile URL.** Name plus firm plus city resolved to a profile is a lookup, not a search, and it converts records already owned rather than finding new ones.

**127 records have neither.** The hardest group and the only one where a widened title filter is the right move: on a one-person shop the owner's headline is "Bookkeeper" or "CPA", never "Managing Partner", so the original filter was screening out the exact person wanted. Where the firm name *is* a person — `Kemp CPA PLLC`, `R Frank Miller CPA`, `Will Crook CPA PA` — people-search beats company-search, and the franchise purge finally made that viable.

### Order of operations

1. Re-key the 113 company-page records. Best odds, and immune to the failure mode that killed 59 rows.
2. Resolve the 79 known names to profile URLs.
3. Widened title filter plus eponymous people-search on the 127.

**The 80 second contacts are gone.** The Clay rows were cleared per step 7 of the loop, and Clay keeps no copy. Recovering a second contact means re-running, which is why the files below exist and why the second-person columns must be mapped *before* the run, not after.

---

## Run 2 files, built 2026-07-26

Generated by `sync/build-wl2-clay-csv.py`, which is re-runnable and carries the franchise screen inline. Rows are sorted by `score` descending inside each file, so a run cut short still covers the best firms.

```bash
python sync/build-wl2-clay-csv.py --directory xero_us_full.json --clay-exports "clayexports/*.csv" --out outputs/campaigns/white-label-accounting/
```

| File | Rows | Company Identifier | Title filter |
|---|---|---|---|
| `clay-wl2-A_company_page.csv` | 107 | **`linkedin_company`** | Standard buyer titles |
| `clay-wl2-B_name_no_url.csv` | 79 | `domain` + `contact_name` | n/a, this is a person lookup |
| `clay-wl2-C_cold.csv` | 111 | `domain` | **Widened, see below** |
| `clay-wl2-D_no_domain.csv` | 10 | firm name + city, or leave parked | Standard |

**Cost: about 109 credits for A and C at the measured 0.5/row.** B is a different column type and unpriced on this pipeline, so run 10 rows and read the balance before committing the rest.

### Why A runs first

`A` already carries a LinkedIn company URL, so keying on `linkedin_company` instead of `domain` makes the "Company Not Found" failure structurally impossible. That failure mode cost 59 rows on run 1 and every one of them was a domain-resolution problem, not an absent company.

### The widened title filter, for C only

Run 1 filtered on Owner, Partner, Principal, President, Managing Partner, Managing Director, Founder, CEO. That produced 106 *No Profile Found* rows where the company page resolved but nobody matched. On a one-person practice the owner's LinkedIn headline is routinely **Bookkeeper, Accountant, CPA, EA, Tax Preparer or Consultant** — the buyer, wearing a title the filter rejected.

Add those to the keyword list for `C`. Keep the original terms too. Do **not** widen `A`, where the standard filter is working against firms that do have staff.

### Capture the second contact this time

`Limit` was already 2 on run 1 and Clay returned two people on 80 of 160 hits. All 80 were lost because the export template carried one set of person columns and silently kept the first.

**Before running anything, map a second set of columns to the second returned person** — `First Name People 2`, `Last Name People 2`, `Url People 2`, `Title People 2` — then run 10 rows and confirm both sets populate on a row that reports "Returned 2 People". If only the first fills, the mapping is wrong and running the full file will lose the second contact again for the second time.

One record per firm is the WL-2 shape, so a second contact has nowhere to live on the table yet. Either add `Contact_2_*` fields before loading, or hold the second contacts in the export until there is somewhere to put them. Do not discard them at load time.

### Screened out on the way in, 12 records

The franchise screen now runs on the **domain**, not just the firm name, which is the check that was missing on run 1. Dropped: 8 ATAX franchise locations, 2 Block Advisors, Meru Accounting, Amesto Global and IBN.

**MATAX was a false positive on the first build** and is now in the files. `atax` as a substring matches M-**ATAX**, a real Platinum-tier firm. This is the fourth time in this campaign a short brand token has been matched as a substring and caught good firms. `atax` now sits in `BRAND_TOKENS` with word-boundary matching, alongside `ey`, `pwc`, `cla`, `cri`.

### The 10 with no domain are parked, not dropped

`D` has a firm name, phone, city and no usable website, so a domain-keyed company search has nothing to work with. They are in their own file rather than silently cut. The cheap route is a manual LinkedIn company search on firm name plus city, which costs no credits at that volume.
