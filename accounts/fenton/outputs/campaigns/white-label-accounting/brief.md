# Campaign Brief: White-Label Accounting

Status: **Strategy set 2026-07-25. Sourcing done and oversized. Runs AFTER the Bounce campaign, never alongside it.**

> **`strategy.md` is the governing document for this campaign.** It defines the two fears the buyer
> actually has, the 1-1-1 definition, the autumn buying window, and what would falsify the whole thing.
> `abm-research-play.md` holds the tactics. This brief covers sourcing mechanics and history.
Owner: GTM | Delivery: Miriam | Buyer: accounting/CPA firm principals (see `context/personas/firm-owner.md`)

---

## The motion

Sell Fenton's bookkeeping capacity to **accounting / CPA firms** as white-label, behind-the-scenes delivery — cleanup, ongoing bookkeeping, payroll — resold under the firm's own brand. This is the motion the public site already describes ("not client-facing, we don't compete for relationships"). Different buyer from Bounce; nothing is shared except the delivery engine and the Copy Rules.

**Groundwork artifacts (done):**
- ICP: `context/icp-definition-white-label.md`
- Persona: `context/personas/firm-owner.md`
- Signals: "White-Label Signals" section in `context/signal-library.md`

## Lead sourcing (the waterfall — per `workflows/enrichment.md`: don't pay for what's free)

**Why this works where Bounce's enrichment didn't:** Bounce's micro-businesses live on personal Gmail, below Clay's coverage floor. Firms have websites, LinkedIn pages, directory listings, and licenses — Clay prospecting's home turf. Validated capability: the Clay MCP's `search-companies` supports industry="Accounting", size buckets, US locations, revenue bands; `search-contacts` finds Owner/Partner/Principal; Email enrichment on top.

| Layer | Source | Cost | What it yields |
|---|---|---|---|
| 1 — breadth | **Intuit Find-a-ProAdvisor directory** (scrape via gstack `/scrape`) — QB-native firms, also a Tier-2 signal | Free | Firm name, location, services, credentials |
| 1 — breadth | **Google Maps** metro sweeps ("CPA firm," "bookkeeping firm") via `/browse` | Free | Small firms with weak LinkedIn; site + phone |
| 1 — optional | State Board of Accountancy rosters / CPAverify | Free | Volume fallback only if 1a/1b under-deliver |
| 2 — screen | Dedupe (domain/phone), US, 2–50 staff, drop franchises, drop offshore-delivery firms | Free | The qualified subset |
| 3 — depth | **Clay credits:** firmographics cross-check → decision-maker contact → verified email, screened firms only | ~2–4 credits/contact (assumed) | Send-ready contacts |
| 4 — signals | Job-posting sweep + site language per screened firm | Free | Tier-1 signal flags |

**Credit budget:** 2,000 available, **expiring 2026-07-27**. Working split: cap 1,500 for sourcing (the Maps sweep below), hold 500 reserve for the contact-enrichment waterfall on whatever the sweep qualifies. **The pilot sets the real numbers** — measure credits-per-contact and email-hit-rate on real data before any scale spend. There is no free path around Clay for the depth layer; the free/paid split above is the entire cost control.

**Google Maps sweep — the sourcing mechanism (session 2026-07-24):** Clay's native Google Maps enrichment bills per business record returned. Workaround: an HTTP API column calling SerperDev's Maps API directly (1 credit per call, returns a page of ~10 results) chained to a "write to other table" (WTOR) action that explodes each response into rows for free. Net cost is ~1 credit per page of results, not per business. Table 1 = search rows (`City/State/Country + Keyword` → `PLACE`/`KEY` formulas → up to 5 paginated `Page N` API calls, each with a `Page N WTOR` explode). Table 2 = the resulting business records (name, address, phone, website).

Forensic/signal AI columns (capacity signals, awareness stage, personalized payload) are explicitly **out of scope for this pass** — this sweep buys volume/coverage only, not insight into which firms are understaffed or at capacity. That comes later, as a cheap gate applied to the qualified subset, not to the raw sweep.

**Keyword set:** `CPA firm`, `bookkeeping firm`, `accounting firm`, `tax & accounting services` — literal Maps business-category terms, not consumer search phrasing. (Google Trends was tested as a way to prioritize geography first, but state-level Trends rankings turned out to be too noisy for this — small-population states (Wyoming, and previously Alaska) spike to the top of the index off a handful of searches because Trends normalizes by regional volume, not raw count. Dropped as a geography-picker; kept only for confirming which phrases have real sustained search volume.)

**Metro list — Tier 1 (top 30 US metros by population, priority coverage across all 4 keywords):** New York-Newark-Jersey City NY-NJ; Los Angeles-Long Beach-Anaheim CA; Chicago-Naperville-Elgin IL-IN-WI; Dallas-Fort Worth-Arlington TX; Houston-The Woodlands-Sugar Land TX; Washington-Arlington-Alexandria DC-VA-MD; Philadelphia-Camden-Wilmington PA-NJ-DE-MD; Atlanta-Sandy Springs-Alpharetta GA; Miami-Fort Lauderdale-Pompano Beach FL; Phoenix-Mesa-Chandler AZ; Boston-Cambridge-Newton MA-NH; Riverside-San Bernardino-Ontario CA; San Francisco-Oakland-Berkeley CA; Detroit-Warren-Dearborn MI; Seattle-Tacoma-Bellevue WA; Minneapolis-St. Paul-Bloomington MN-WI; San Diego-Chula Vista-Carlsbad CA; Tampa-St. Petersburg-Clearwater FL; Denver-Aurora-Lakewood CO; Baltimore-Columbia-Towson MD; St. Louis MO-IL; Orlando-Kissimmee-Sanford FL; Charlotte-Concord-Gastonia NC-SC; San Antonio-New Braunfels TX; Portland-Vancouver-Hillsboro OR-WA; Sacramento-Roseville-Folsom CA; Pittsburgh PA; Las Vegas-Henderson-Paradise NV; Austin-Round Rock-Georgetown TX; Cincinnati OH-KY-IN.

**Tier 2 (next 20, expansion capacity only if the pilot's real credit cost leaves room):** Kansas City; Columbus; Indianapolis; Cleveland; Nashville; Virginia Beach; Providence; Jacksonville; Milwaukee; Raleigh; Richmond VA; Memphis; Oklahoma City; Louisville; New Orleans; Salt Lake City; Hartford; Buffalo; Birmingham; Grand Rapids.

**Pilot gate (staged — runs when the operator calls it):** Run metro #1 (New York-Newark-Jersey City) across all 4 keywords first, alone — confirm real credits-per-page-call in this Clay plan before committing the rest of Tier 1. Once that number is known, calculate how many of the remaining 29 Tier 1 metros (and whether any Tier 2) fit inside the 1,500 sourcing cap while still leaving the 500-credit reserve untouched for contact enrichment (email find/verify on whatever the sweep qualifies). Then: 50 firms end-to-end (source → screen → Airtable → enrich) → report firms sourced, % passing screen, % with decision-maker found, % with verified email, credits consumed → operator sets the scale-up budget.

**Destination:** separate Airtable base/table ("White-Label Firms"). Never mixed into the Bounce `Contacts` table. Channel-conflict check against the Bounce list before any outreach (see suppression rules in the signal library).

## Operator checkpoint (recommendation, not a block)

**Recommended order: white-label funnel live → then scale sourcing.** Enriched decision-makers with no destination go stale. Operator's call to run the pilot ahead of it. Note the kit nuance: Copy Rules mandate no links and reply-only CTAs, so the funnel is a destination for later touches, reply follow-ups, and warm traffic — not touch-1. The pilot and first sends are kit-legal without it if the funnel timeline slips.

## Build checklist

- [x] ICP (firm-level, separate file)
- [x] Persona (firm owner / managing partner)
- [x] Signals (white-label section, with detection methods)
- [x] Lead source architecture (this brief) — NOT the Bounce list, by construction
- [ ] Pilot source run (50 firms) — staged, operator-called
- [ ] Scale sourcing per pilot-measured credit economics
- [ ] Positioning addendum: re-anchor on reliability + invisibility (not price/AI) — reuse `context/positioning.md` Copy Rules verbatim
- [ ] Sequences/copy — **after the Bounce test is live** (standing directive)
- [ ] Scoring adaptation: white-label fit dims in `skills/icp-scoring` (after pilot data exists)

## Timing note

Cold-start windows for firm outreach: **Nov–Dec** ("capacity for next season") and **May** (post-season exhaustion). Avoid cold starts Jan 15–Apr 15. Today is mid-July: sourcing + pilot now, copy after Bounce test, first sends targeting the Sep–Oct extension-season pain or the Nov–Dec window — the timeline is comfortable, no rush spend needed.
