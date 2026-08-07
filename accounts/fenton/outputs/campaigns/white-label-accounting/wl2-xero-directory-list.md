# WL-2 — the Xero advisor directory list

*Built 2026-07-25. A second, independent source list for White-Label, sitting alongside WL-1.*

---

## The three tables, so they stop getting confused

| Table | Base | Records | Source | What it is |
|---|---|---|---|---|
| `Contacts` | `apppSIWMEemeoaCdv` (QuickBooks Lead Capture) | 861 | Purchased/captured list | **QuickBooks Bounce**. SMB owners, cold email. A different campaign and a different buyer. |
| **`WL-1 Firms (Google Maps)`** | `appEWdrpe1eIGB1cD` / `tblafsL94yxtXp9fa` (WL-1) | 617 | Clay + Serper Google Maps sweep | QuickBooks-native CPA and accounting firms. Has a **named contact and LinkedIn profile on every record**. |
| **`WL-2 Xero Advisors (Xero directory)`** | `appEWdrpe1eIGB1cD` / `tblJiapiwE1f3Mb0q` | 618 | Xero's public advisor directory | Practices that committed to Xero. Rich **firmographics and phone**, thinner on named people. |

WL-1 and WL-2 serve the same campaign and the same offer. They are different populations, sourced differently, with different strengths. Do not merge them.

---

## Why WL-2 exists

WL-1 came from Google Maps, so it is a geographic sweep of firms that happen to have a listing. WL-2 is the **entire US Xero professional channel** — not a sample, the whole thing, because there are only ~618 Xero advisors in the United States.

Two things make it worth having as a separate list:

**The contact data arrives free.** Phone on 91%, address on 99%, website on 97%, a description on 99%. No Clay credits, no enrichment waterfall, no scraping. WL-1 cost credits to build; WL-2 cost one API pull.

**It is a different population.** These firms chose a platform other than QuickBooks. Whatever else that says about them, it means they are not Intuit-locked and have already demonstrated willingness to move.

---

## What is on each record

| Field | Coverage | Note |
|---|---|---|
| Firm | 100% | |
| Website | 97% | |
| **Phone** | **91%** | Straight from the listing |
| Address / City / State / Postcode | 99 / 94 / 92 / 91% | |
| Description | 99% | The practice's own blurb. Raw material for personalising |
| **Partner_Tier** | **100%** | Platinum 62, Gold 89, Silver 242, Bronze 205, Starter 17 |
| **Partner_Since** | **100%** | Year they joined Xero, 2010 through 2026 |
| Industries | 76% | |
| LinkedIn | 50% | ~60% company pages, ~40% personal profiles. Check which before using |
| **Contact_Name / Title** | **39%** | 240 of 618 published staff profiles |
| Staff_Count | 100% | 0 means none published, not a solo practice |
| Migration_Specialist | 100% | 180 hold the badge |

---

## The big limitation, stated plainly

**378 of 618 records have no named human on them.** For those, this is a firm list, not a contact list. A LinkedIn ABM campaign needs a person, so those records need a decision-maker found before they can be worked.

That is the honest trade against WL-1, which has a named contact and a personal LinkedIn URL on every single record. **WL-1 is more immediately actionable; WL-2 is richer per firm and free.**

---

## Scoring

`Score` is a formula, 30-100, mirroring the WL-1 model so the lists stay comparable, but on better inputs. WL-1 has to infer firm shape from the company name; WL-2 publishes it.

**Practice size, 40/30/20/15 — the solopreneur test, weighted highest.** `Staff_Count = 1` scores 40: one practitioner, no bench, every new client competes directly with the owner's own billable hours. That is the same shape as Fenton itself and the sharpest capacity pain in the data. 2-3 staff scores 30, 4+ scores 15. Where no staff were published it falls back to Partner_Tier.

**Client volume, 30/20/10 — from Partner_Tier**, which Xero awards on the number of subscriptions a practice manages. Silver and Gold score highest: enough volume to have real overflow, small enough to lack a back office. Platinum scores lower because it probably has one. Starter scores lowest because a tiny book has nothing to hand out.

**Tenure, 20/10 — from Partner_Since.** 2018 or earlier means an established book.

**These weights are a considered heuristic with no outcome data behind them.** Fenton has zero clients, so nothing here is fitted. Same caveat as WL-1.

---

## Two flags to read before working the list

**Solo cuts both ways.** A solo practice is the sharpest capacity pain *and* the most likely to be a competitor rather than a buyer — it is Fenton's own shape. `Staff_Count = 1` is 181 records. Screen, do not just sort.

**`Migration_Specialist` is a competitor signal, not a buying signal.** 180 firms (29%) hold Xero's migration badge, and they sell that work themselves. It is deliberately excluded from `Score`.

Worth knowing before anyone reads the badge as proof of a hot market: badge holders mention migration in their description **5%** of the time against **4%** for non-holders, and only **1%** lead with it. Held widely, marketed by almost nobody. That is a credential people collect, not a flagship product — which is consistent with Xero giving the conversion away free.

**19 records are pre-flagged `ICP_Flag = Excluded`** on a name match against national firms, franchises and known competitors (Scrubbed, Aprio, Paperchase, Bench, Pilot, Xendoo, Bookkeeper360, Reconciled, Acuity and similar). That screen is a starting point, not a finished job.

---

## Rebuilding it

`sync/xero-directory-pull.py` re-pulls the whole US directory in about a minute. It uses the directory's own `@adcountries==US` filter rather than sweeping city by city, which is what makes it complete — an earlier city-text sweep found only 95 of the 618 and was roughly 85% lossy.

`Listing_ID` is Xero's stable UUID and is the dedupe key for any re-pull.
