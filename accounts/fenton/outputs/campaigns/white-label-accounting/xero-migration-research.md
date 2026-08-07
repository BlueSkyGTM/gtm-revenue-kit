# Xero migration as an offer — research findings

*Researched 2026-07-25 after Miriam confirmed she has Xero capability and considers Xero the more ethical platform. The question asked: is QuickBooks-to-Xero migration a big-ticket item and a niche worth owning?*

**Short answer: the migration is not the product. The cleanup around it is, and that is a better outcome than the question assumed.**

---

## 1. Migration itself is a commodity racing to zero. Do not sell it.

| Provider | Price |
|---|---|
| **Xero's own conversion** | **Free.** Xero subsidises current plus prior fiscal year. Extra years may cost |
| **Q2X** (Xero's preferred partner) | **Free** for QuickBooks Online to Xero. Base conversion subsidised, described as a $250 value |
| **Xero professional services** | Handles firms converting **5+ clients**, including financial settings and a custom chart of accounts |
| **WOW BookSwitch** | **$399 flat** per conversion, 3 years of data, $100 per additional year |
| **JetConvert** | Automated historical migration, also Xero-subsidised |

**The platform vendor gives the conversion away to win the customer.** Fenton cannot sell a service that Xero performs for free, and should not try. Any pitch built on "we will migrate you" competes with the vendor's own subsidised offer and loses on price to zero.

Note also that **Xendoo is Xero's preferred migration partner** and Xendoo already sits on this campaign's out-of-ICP exclusion list as a competitor. The migration lane has established, better-capitalised occupants.

---

## 2. The money is in what the migration does not cover

This is the finding that matters. From the research, on a QuickBooks-to-online migration:

> the data transfer itself is hours, but pre-cleanup, validation, and bank feed reconnection take the rest

Published cost ranges for that surrounding work:

| Work | Cost |
|---|---|
| Data validation and cleanup | **20-40 hours**, quoted at $1,000-$2,000 at a $50/hour rate |
| Consultant for integration setup and testing | **$2,000-$5,000** |
| Fixing a failed migration | **~$4,000** |
| Realistic timeline done properly | **2-3 weeks** per file |

Two observations.

**The $50/hour anchor is low.** That is a generic contractor rate, not what a QuickBooks Certified ProAdvisor with 30 years commands. The hours are the real datum; the rate is Miriam's to set.

**One number needs a health warning.** The widely repeated "free tools have a 43% error rate, average cleanup $4,000" statistic comes from a vendor selling a competing paid conversion service. It is directionally plausible and consistent with the 2-3 week timeline, but it is marketing, not independent research. Do not put it in copy as fact.

---

## 3. The forcing events are real, dated, and hit firms rather than end users

This is what makes it a niche rather than a nice idea.

| Event | Date | Who it hits |
|---|---|---|
| Intuit stopped selling new Pro Plus, Premier Plus, Mac Plus subscriptions | 2024-09-30 | Desktop users |
| **QuickBooks Desktop 2023 support ends** | **2026-05-31** (passed) | Firms with Desktop clients |
| **Accountant-billed QBO prices rise** | **2026-08-01** | **Firms directly, on wholesale margin** |
| **Desktop 2024, the last non-Enterprise version, loses support** | **2027-09-30** | Firms with Desktop clients |

Losing support means no security patches, no payroll, no bank feeds, no payment processing. The file still opens, but a practice cannot responsibly run client books on it.

The research described the effect plainly: Desktop end-of-life dates combined with pricing pressure are **"turning what used to be a gradual discussion about Xero vs QuickBooks into an active project for a lot of practices."**

**The 2026-08-01 increase applying to accountant-billed subscriptions is the sharpest fact here.** Every other price story in this repo is about an SMB's own bill. This one lands on the firm's own margin, on the subscriptions it resells. It gives a firm owner a reason to reconsider platform at the practice level, not client by client.

---

## 4. Firm-scale migration is a genuinely different shape from one-file migration

For a practice moving a book of clients:

- Firms with **50+ clients** hit a bottleneck doing conversions one at a time
- Batch processing can compress a **6-month** sequential project into **4-6 weeks**
- Xero's professional services engages at **5+ clients**

A firm moving 30 client files does not need 30 conversions. It needs 30 files **validated, reconciled, chart-of-accounts mapped, bank feeds reconnected, and opening balances proved.** At 20-40 hours each that is not a project a small practice can absorb alongside its own client work, and it is precisely the work it would want to hand to someone else.

**That is the big-ticket item the original question was reaching for.** Not the migration. The migration's aftermath, at book scale.

---

## 4b. The Xero directory sweep killed the Xero framing, and pointed at a better one

The same cross-reference was run against Xero's advisor directory (Coveo-backed).

**The decisive number, taken from the directory's own country facet rather than inferred: there are 617 Xero advisors in the entire United States.**

| Country | Xero advisors | Note |
|---|---|---|
| Australia | 5,925 | ~26m people |
| Great Britain | 4,799 | ~68m people |
| New Zealand | 1,481 | ~5m people |
| **United States** | **617** | **~335m people** |
| Canada | 245 | |

Xero has nine times the advisor base in Australia that it has in the United States, from a population thirteen times smaller. This is a real structural fact about Xero's US professional channel, not a quirk of one query.

For contrast, the Intuit sweep returned **11,351 unique ProAdvisors across 197 metro areas (22,393 raw listings before de-duplicating advisors who fall inside more than one 25-mile radius)**, and several large cities hit the pagination cap at 300, so the true Intuit figure is higher still. The units differ slightly (Intuit lists individual advisors, Xero lists practices), but no reasonable adjustment closes a gap that size.

### Per-contact result: 14 of our 617 firms are listed Xero advisors

Written to Airtable as `Xero_Advisor`: **10 Confirmed** (matched on website domain, which is much stronger than name matching) and **4 Probable** (firm-name match only, spot-check before use).

**Method matters here, because the first attempt got this badly wrong.** The initial sweep queried the directory city by city and found 1 match. That method was ~85% lossy. The correct approach, used for the number above, was to pull the **complete** US advisor list in one go using the directory's own `@adcountries==US` filter (617 records, each with a website) and match all of them against all 617 of our firms. Domain matching then does most of the work and location never enters into it.

Two bugs were caught and fixed while matching: `certified`, `public`, `accountancy` and `corporation` were not in the stop-word list, so eight of our firms were matching a single listing called "ASN Group | Certified Public Accountants"; and `sites.google.com` was being treated as a firm domain, which matched two unrelated businesses sharing that host.

**Three firms are certified in BOTH QuickBooks and Xero: Acuity, Bottom Line Accounting, and Profitwise Accounting.** That is the straddling segment, and it is the most interesting one in the whole list for this offer, because a firm holding both credentials is the one actually running clients on two platforms and therefore the one with live migration work. Three is too few to build a campaign on, but they are worth a hand-written approach.

### Correction to an earlier version of this section

An earlier draft reported "95 Xero listings, a ratio of 236 to 1." That comparison was unfair and the number should not be reused. The ProAdvisor sweep used a proper 25-mile geospatial search; the Xero sweep used a full-text query on the city name, which only returns listings whose text happens to contain that city. It found 95 of the 617 US advisors, so it was roughly 85% lossy. The corrected national figures above are drawn from the directory's country facet and do not depend on the sweep's method.

The conclusion is unchanged, and firmer.

### What "1 match" does and does not mean

It means at most one of our firms is a **publicly listed Xero partner**. It does **not** mean only one has a Xero licence. The directory is opt-in and lists practices in Xero's partner programme, so a firm could hold licences, or use Xero for a client or two, without appearing. Name-based matching adds its own miss rate on top.

The useful signal is not the 1. It is the 617.

### Two readings, and the honest weighing

**Against the Xero niche:** almost no US firms are Xero advisors, which is evidence that very few are actively moving client books to Xero. A niche needs buyers, and 95 advisors nationally is not a market with 617 addressable firms behind it.

**For it:** no competition. A firm that does decide to move to Xero has almost nobody local to call, and Miriam would be one of very few.

**The against reading wins**, because reading B only pays if demand exists, and the 236-to-1 ratio is the best available evidence that it does not, at least not yet in the US.

### What the sweep pointed at instead

The Desktop end-of-life deadlines force firms to move their Desktop clients **somewhere**. Intuit is actively driving them to QuickBooks Online, and the path of least resistance for a QuickBooks-native practice is Desktop to QBO, not Desktop to a platform 236 times less represented among its peers.

**So the migration volume is QuickBooks to QuickBooks, and that is where the cleanup work is.**

This is a better answer than the Xero framing, for three reasons:

1. **It is where the forced volume actually is**, driven by a vendor with every incentive to push it.
2. **It matches Miriam's existing credential exactly.** She is a QuickBooks Certified ProAdvisor, which is the relevant qualification for a Desktop-to-QBO cleanup, and 77 firms in the list hold the same certification and will read it instantly.
3. **It needs no platform argument.** Selling Xero means first persuading a conservative practice to change platforms, which is a second sale on top of the first. Desktop-to-QBO cleanup sells into a decision the firm has already been forced to make.

**Xero's role changes from the basis of the offer to a differentiator inside a conversation.** Miriam can migrate to Xero, and rates it the more ethical platform. That is a genuine and unusual thing to be able to say to a firm owner who is unhappy about being pushed around by Intuit's pricing. It earns trust in the room. It should not be what the campaign leads with.

---

## 5. What this means for the strategy

**It does not violate 1-1-1. It sharpens it.** The chosen offer is already QuickBooks cleanup. Migration cleanup is the same skill, the same buyer, and the same fear, with a dated forcing event attached and a clearer scope. Treat it as the sharpest version of the existing offer rather than a second offer competing for the same touches.

**It supplies the niche the strategy was missing.** "QuickBooks cleanup for small firms" is a category. **"We clean up and validate your client files when you move a practice off QuickBooks"** is a niche, with an identifiable trigger, a deadline, and few credible providers who are one accountable human rather than a platform.

**It fits every structural constraint already set:**

- **Project work, not a retainer.** It does not consume the scarce retainer capacity that White-Label is meant to sell.
- **Zero poaching risk.** The engagement ends. You finish and leave, which is the most credible possible answer to fear 2.
- **It is cleanup, so it is low-trust.** No firm has to restructure or hand over an ongoing relationship to try it.
- **Miriam believes in it.** She rates Xero the more ethical platform. Selling something the deliverer actually believes is worth more than any positioning exercise, and it will show in the conversations.

**It also improves the research play.** The capacity interview can carry one more question that is now clearly worth asking: *what are you doing about the Desktop clients before support runs out?* That is a live, dated problem a firm owner is already thinking about, and the answer qualifies them instantly.

---

## 6. What is still unknown

- **Miriam's Xero certification status specifically.** She has capability and conviction. Whether she is a certified Xero advisor is a different question, and the Xero advisor directory is public, so it is checkable.
- **Whether she wants project work.** Migration cleanup is intense, deadline-bound and lumpy, which is a different rhythm from steady monthly bookkeeping. Worth asking before it becomes the pitch.
- **Real pricing.** All figures here are market benchmarks, not Fenton quotes. Pricing stays case-by-case per the standing decision.
- **Xero's partner programme.** Certified advisors may get referral flow and listing placement. That is a potential inbound channel, not just a service line, and it has not been investigated.

---

## Sources

All third-party and, where noted, vendor-published rather than independent.

- [Xero: convert from QuickBooks](https://www.xero.com/us/accounting-software/convert-from-quickbooks/) and [Xero: convert clients to Xero](https://www.xero.com/us/accountants-bookkeepers/convert-clients-to-xero/)
- [Q2X, Xero preferred migration partner](https://q2x.app/)
- [WOW BookSwitch pricing and firm migration checklist](https://wowbookswitch.com/blog/qbd-to-xero-migration-checklist-2026) — sells a competing paid service, treat its error-rate statistics as marketing
- [Method: QuickBooks Desktop discontinued](https://www.method.me/blog/quickbooks-desktop-discontinued/) and [SDO CPA: Desktop discontinuation dates](https://www.sdocpa.com/quickbooks-desktop-discontinued/)
- [Intuit Firm of the Future: QuickBooks Online pricing changes](https://www.firmofthefuture.com/product-update/quickbooks-price-changes/)
- [Webgility: switching from QuickBooks to Xero](https://www.webgility.com/blog/switch-from-quickbooks-to-xero)
