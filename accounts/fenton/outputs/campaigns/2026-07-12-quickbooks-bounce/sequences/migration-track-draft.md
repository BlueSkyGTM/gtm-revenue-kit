# Migration offer track: DRAFT variants (nothing loaded, nothing sent)

**Status: DRAFT ONLY.** Written 2026-07-27 as IMPACT step 6 for the migration offer track
(`playbooks/impact-positioning.md`; house: `context/messaging-house.md`, Migration offer
track). Three things must happen before any of this is loaded, in order:

1. **The principal's yes** on testing the offer at all.
2. **Per-account eligibility.** A record receives migration copy only after **its own first
   bill at the new price has landed** (`context/signal-library.md`, Migration-Intent Signals).
   This is what keeps the motion inside the standing no-urgency rule; it is not optional.
3. **The step-7 red-team** of this track (`outputs/audits/`), per Phase 0.

**Test design (decided):** this replaces the suspended `paying-more-getting-software` variant
in the rollout rather than becoming a fourth cell. 141 accounts across four cells is roughly 35
each, under the 50-account audience gate. Top the batch up by at least nine qualified accounts
from the scored rollout list, or label the read explicitly directional. Results are tracked
**per-offer**, not just per-account.

**Which variant ships (step-7 audit, 2026-07-27):** one slot, three drafts, so only one ships.
**`paid-exit` is the shipper**, with its tier line merge-fielded (below). `origin-knowledge` is
round two or a payroll-gated cell. **`one-bill` is held entirely** until Fenton is a Xero
partner and the three engagement-letter clauses exist, because it currently promises a
capability the practice deliberately will not have at test time. Full findings:
`outputs/audits/2026-07-27-positioning-redteam-migration-track.md`.

**Copy Rules applied throughout** (`context/positioning.md`): destination dollars only, never a
percentage, never a deadline; no em or en dashes; no banned vocabulary; no links; one CTA; under
120 words; claims attributed. **No tool names ever appear.** Not the conversion vendors, not any
software we use. "The conversion is free and we handle it" is the ceiling.

---

## Angle: paid-exit  ← THE TEST-SLOT VARIANT

**Suggested subject:** the cheaper way out of that price increase

**Word count:** 103

**PVP:** strip the final line and it still tells them something true they likely do not know,
that a vendor-funded exit exists.

**Merge field required (audit F2).** `{{tier_line}}` renders the recipient's OWN plan movement,
never another tier's. The plan is already in the `Products` field, so this is a merge task, not
research. Three values, and no account gets a number that is not its own:

| Plan | `{{tier_line}}` |
|---|---|
| Essentials | `Essentials moved from $75 to $85 a month.` |
| Plus | `Plus moved from $115 to $140 a month.` |
| Advanced | `Advanced moved from $275 to $340 a month.` |

*A record whose plan cannot be resolved is not eligible for this variant. Unaffected plans
(Simple Start, Solopreneur, Ledger) are ineligible for the whole track.*

```
Hi {{first_name}},

your QuickBooks bill went up this cycle. {{tier_line}}

Here is the part most owners have not heard: Xero is paying for businesses to leave. The
conversion is free, it carries your transaction history, and it takes days rather than weeks.
Their prices run $25 to $90 a month with unlimited users, where QuickBooks caps users by plan.

We handle the move, check every balance on both sides, and can keep your books after. After 30
years in small business books, I would rather you saw the numbers than took my word.

Worth a short call?

Regards,
Miriam
```

## Angle: origin-knowledge  ← round two, or a payroll-gated cell

**Suggested subject:** what does not transfer when you leave QuickBooks

**Word count:** 104

**PVP:** every claim applies to every recipient (audit F3 fix: the universal facts now lead, and
the payroll sentence is conditional).

**Conditional line (audit F3).** `{{payroll_line}}` renders **only for `payroll-active`
accounts** and is empty otherwise: `Payroll year to date does not transfer at all, so that gets
rebuilt by hand.` Roughly a third of the list is payroll-stacked; for the rest, leading with
payroll was a fact about someone else's migration.

```
Hi {{first_name}},

if the price increase has you looking at Xero, one thing to know before you start: the
conversion tools move your data, not your accounting. How your chart of accounts maps across is
a judgment call somebody has to make. Anything connected to QuickBooks has to be reconnected on
the other side. {{payroll_line}}

None of that is hard if someone who knows QuickBooks from the inside handles it and then proves
the balances match on both sides. That is the part the free tools leave to you.

Want me to look at your file first?

Regards,
Miriam
```

## Angle: one-bill  ← HELD. Do not send. Do not load.

**Suggested subject:** books and software on one invoice

**Word count:** 92

> **Blocked by the step-7 audit (F1).** This variant promises that Fenton carries the
> subscription and transfers it back free on exit. Both require **Xero partner status**, which
> the motion deliberately defers until the first real engagement is near. The transfer promise
> also requires engagement-letter clauses that do not exist yet. Sending it would promise a
> capability the practice does not have.
>
> **Unblocks when:** partner status is live **and** the three clauses are written
> (transparent pass-through, free exit transfer, transparent bundling; see
> `context/pricing-strategy.md`). Kept here because the packaging is genuinely strong, not
> because it is queued.

```
Hi {{first_name}},

after this increase, plenty of owners tell me the frustrating part is not the amount, it is that
the number keeps moving.

There is a version where that stops. We move you to Xero, the conversion is free, and we carry
the subscription ourselves. You get one invoice from us each month for the bookkeeping and the
software together, and no software bill of your own. If we ever part ways, the subscription
transfers straight back to you.

Thirty years of small business books behind it.

Want the numbers for your setup?

Regards,
Miriam
```

---

## Reply-handling overlay (migration track)

Replies route through the same six classes in `skills/reply-handling/SKILL.md`, with no new
machinery. The discovery structure gains four migration-specific questions, asked in this order
after the standard opener:

1. **Which plan are you on, and how many people are in the file?** (sets the dollar comparison
   and reveals user-cap pressure)
2. **What is connected to QuickBooks?** (payment processors, payroll, POS, time tracking: each
   is a reconnection task)
3. **Do you run payroll through it?** (the year-to-date work, and the pro-Xero cost comparison)
4. **How far back do you need the history?** (decides the tooling path and whether historical
   reconstruction is a separate line)

Then the standing four: how far behind, what broke last, who touches the file, what has to be
true in 90 days.

**Class F applies with force here.** If a reply says any version of *"my price did not go up"* or
*"I am on Simple Start,"* the eligibility gate failed. That is a copy defect: flag it to the
operator same-day, and do not argue the claim.

**Never quote a price on call one.** Structure exists (`context/pricing-strategy.md`, Migration
motion pricing); every number is `[UNTIMED]` until one real file is timed. Close on the audit,
not the engagement.

## Results scaffold (per-offer, filled after any send)

| Angle | Sends | Opens | Replies | Positive | Meetings | Notes |
|---|---|---|---|---|---|---|
| `paid-exit` | | | | | | |
| `origin-knowledge` | | | | | | |
| `one-bill` | | | | | | |

**Read this against the bookkeeping track's numbers, not on its own.** The question the test
answers is not "does migration copy work" but "does the migration offer beat the bookkeeping
offer on the same people." Benchmarks: `workflows/campaign-build.md`. Pause any variant under
1% reply after 50 sends.
