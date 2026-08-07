# The Exit Practice — one service, all industries

*Written 2026-07-26. Operator thesis, specified and stress-tested. This is a proposal, not a decision.*

**The claim:** stop selling bookkeeping. Sell getting off QuickBooks and fixing what it broke. One service, priced per file, sold to both small businesses and accounting firms. It unifies the two campaigns, it is the only part of this business with hard numbers, and it matches what Intuit's own pricing has done to the market.

---

## The numbers, corrected

An earlier version of the WL-2 report said the sellable unit was "cleanup at $2,000-$5,000 for 20-40 hours." **That merged two separate rows of the source table and was wrong.** The actual economics, from `xero-migration-research.md`:

| Line | Market rate | Notes |
|---|---|---|
| The migration itself | **~$0-$399** | Xero subsidises it. Q2X is free. WOW BookSwitch charges $399. Do not sell this. |
| Data validation and cleanup | **20-40 hours** | Sourced at $1,000-$2,000, but on a $50/hour generic contractor rate |
| **Integration setup and testing consulting** | **$2,000-$5,000** | Advisory, not production |
| Fixing a failed migration | **~$4,000** | Remedial, urgent, low price sensitivity |
| Realistic timeline | 2-3 weeks per file | |

**The $50/hour anchor is the wrong rate and the research doc says so.** It is a generic contractor number, not what a Certified ProAdvisor with 30 years commands.

**This session produced the right comp.** Christina Rea, a competing bookkeeping firm on WL-1, publishes **$125/hour for historical bookkeeping cleanup** on her own pricing page. That is a public price from a direct competitor for exactly this work.

At $125/hour, 20-40 hours of cleanup is **$2,500-$5,000 per file.** Same range, honestly derived.

**Why this correction matters more than it looks:** quoting $2-5K while budgeting at $50/hour means booking $1,000-$2,000 of revenue against a $2,500-$5,000 promise. The rate is not a detail. It is the business model.

---

## The stack

Three paid lines around one free event. They are sequential, they sell to the same file, and each is a natural upsell from the last.

```
   [ free ]         [ $2,500-5,000 ]      [ $2,000-5,000 ]        [ ~$4,000 ]
  the migration  →  pre-move cleanup  →  integration consulting  →  repair a
   (don't sell)      (QuickBooks work)     (advisory)              failed move
```

**Pre-move cleanup is the anchor and it is pure QuickBooks work.** Getting a messy QuickBooks file into a state where it can migrate correctly is corrective cleanup on a QuickBooks file. That is Miriam's exact 30-year credential — ProAdvisor, audit support, corrective cleanup. No new certification required to sell or deliver it.

**Integration consulting is the highest-value line and the one the operator wants to lead with.** Note what it is: advisory work on how the new system should be set up, tested and connected. It is not production bookkeeping. A 30-year practitioner is worth more per hour giving that judgment than doing data entry, and it is not capped by hours the way cleanup is. The operator's read is that this line is what will appeal to Miriam, and that she will certify on Xero within a week if it does.

**That resolves the biggest objection to this thesis.** The repo records Miriam as QuickBooks-certified with no Xero credential anywhere. If she certifies, the whole stack is available and the "we can't service where we send them" problem disappears.

**Failed-migration repair is the sleeper.** ~$4,000, remedial, and the buyer has already failed once. Price sensitivity is at its lowest when something is broken and visible. It also needs no lead generation of its own — it arrives as a referral or a panic search.

---

## Why it unifies the two campaigns

The Copyhackers framing the operator raised: a **generalist** serves one industry with every service; a **specialist** serves every industry with one service. This is the specialist play. One service, any industry, two buyer types.

| | Small business (Bounce list) | Accounting firm (WL lists) |
|---|---|---|
| **Who they are** | 863 QuickBooks subscribers, price-shocked or AI-burned | Firms whose clients are asking to leave |
| **What they buy** | The exit, done for them | The exit, done behind their name |
| **Who Miriam talks to** | The owner | The firm only, never their client |
| **Same delivery work** | Yes | Yes |

**The same file, the same hours, the same skill.** Only the invoice changes. That is what makes it a single service rather than two businesses, and it is the strongest argument for the thesis.

---

## The Bounce contradiction this fixes

The Bounce campaign's premise is that people are angry at Intuit over price rises and AI errors. Its offer is a human bookkeeper **inside QuickBooks**.

There is a real tension in that. If the diagnosis is "I hate this company," then "keep paying them, but hire me too" is an incomplete answer. The complete answer is "leave, and I'll fix the mess on the way out."

That said, do not overstate it. Some of the 863 are angry at the *price* and would be perfectly happy on cheaper QuickBooks with a human. Others are angry at *Intuit* and want out. **Those are different offers to different people, and nobody has segmented the Bounce list to find out which is which.** The exit offer is likely a subset of that list, not a replacement for it.

---

## What the evidence actually supports

**Strong:**

- Intuit's price rises are dated, verified and repeated. QBO Plus $115→$140/mo, Advanced $275→$340/mo, accountant-billed rise 2026-08-01.
- QuickBooks Desktop 2023 hit end of life 2026-05-31. Desktop 2024 follows 2027-09-30.
- Xero certifies migration as a named specialism, and 28% of enriched WL-2 records hold the badge. A platform vendor does not badge work that does not exist.
- Christina Rea's public $125/hour for cleanup is a real market price from a real competitor.
- The WL-1 site visits found the buyer's constraint is **time against a commitment**, not exhaustion and not poaching. Mattingly & Ott promise the 30th across 40+ books. Merritt promise $250/month across thousands of clients. A fixed-scope project that removes a spike is exactly what that buyer needs.
- Miriam prefers not to face end clients. The white-label version of this offer means she never does.

**Weak, and it should be said plainly:**

- **Zero proof points.** Miriam has never delivered a migration cleanup engagement. There is no case study, no reference, no before-and-after. The first sale is the hardest one this business will ever make and nothing shortens it.
- **The rate is unvalidated for Fenton.** $125/hour is what a competitor charges. It is not what anyone has yet paid Miriam.
- **The Desktop deadlines are softer than they sound.** Desktop 2023 EOL has already passed. Desktop 2024 is 14 months out. The sharpest dated trigger is the **2026-08-01 accountant-billed price rise, which is five days away** — and that is a cost trigger, not a platform-exit trigger.
- **Automation is unproven.** "Streamline it with Claude Code" is plausible for data transformation, duplicate detection and reconciliation checking. It is not plausible for deciding what a miscoded transaction actually was, which is the judgment half of a 20-40 hour cleanup. **Do not price a fixed fee against assumed automation until one file has been done manually and timed.**

---

## Recommendations

**1. Price on the rate, not on the range.** Quote from hours × $125, and let the number land where it lands. Quoting "$2,500-$5,000" before a single file has been timed invites a fixed-fee loss on the first engagement.

**2. Do one file manually and time it before productising anything.** Everything downstream — the fixed fee, the automation, the capacity math, whether this is a business at all — depends on whether a real file takes 20 hours or 40. That number does not exist yet and it is the single most valuable thing to learn.

**3. Lead with integration consulting if that is what gets Miriam moving.** It is the highest-value line, it is advisory rather than production, and operator conviction on the delivery side is worth more than a marginally better-optimised offer she is lukewarm about. The certification is a week.

**4. Sell the failed-migration repair first if any lands.** ~$4,000, urgent, low price sensitivity, and it produces the case study that everything else lacks. A rescue is also a better story than a smooth job.

**5. Do not retire the Bounce campaign for this.** Segment it instead. Some of the 863 want cheaper QuickBooks with a human; some want out. The exit offer is a segment of that list, not a replacement for it, and Bounce is already built and warming.

**6. The firm relationship is the retainer, the files are the units.** This is the answer to "cleanup is one-time revenue." One firm sending two files a quarter is recurring without a single ongoing bookkeeping engagement, and Miriam never meets the end client. That is the shape to aim at, and it makes the WL lists more valuable than the SMB list.

**7. Run the 14-conversation test first, unchanged.** Fourteen WL-1 firms are also Xero-certified. Ask whether migration cleanup is work they turn away, and what they charge when they do it. That validates demand and price together, costs nothing, and if three say yes the first firm relationship comes with it.

---

## The honest summary

The thesis is sound and it is the most concrete thing this business has. One service across all industries is a real positioning, the numbers are the only hard ones in the repo, and the unification of the two lists is genuine rather than convenient.

Two things stand between it and revenue, and neither is strategic: **no proof point, and no timed file.** Both are solved by doing one engagement. Everything in this document is a hypothesis until then.
