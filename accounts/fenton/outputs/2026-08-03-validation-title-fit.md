# Title-fit validation — the 862 Bounce records against the three personas

*Run 2026-08-03, closing the bounce red-team's dimension-3 finding ("contact-to-persona
title fit on the 862 records is unvalidated") and the parallel white-label audit note.
Read-only: no record was modified. Source: Airtable base `apppSIWMEemeoaCdv`
(QuickBooks Lead Capture) → `Contacts` (`tbl1TtoJs93jkrjJQ`), 862 records confirmed by
query metadata.*

## Verdict: title fit is not unvalidated — it is unvalidatable from the data layer

The audit suspected the titles had never been checked against the personas. The ground truth
is one step worse and more useful: **the Contacts table carries no title or role field at
all.** The full field list is Company, First Name, Last Name, Email, Direct Phone, City,
State, Products, Customer Type, Customer Lifetime, and the scoring/segment fields
(Spending_Score, ICP_Score, Score_Source, Timezone, Campaign_Role, Spend_Band, ICP_Tier,
Contact_Window, Motive_Segment, Suppress_Price_Fatigue, and as of today
Repriced_Bill_Confirmed). Nothing in it says what the named person does at the company.

`Customer Type` is not a role field: sampled values are Intuit customer-type codes (`dtm`,
`nttf`, `nttt`, `ntff`, `ntsf`, `ntlf`, `nsdf`, `etm`, `upgrader`, `sdf`), plus
`No data yet`, `Unavailable`, and blanks. Useful for product-side segmentation; silent on
title.

## What this means for the personas

1. **Persona assignment cannot be a per-contact routing fact today.** The three personas
   (`context/personas/owner-operator.md`, `office-ops-manager.md`, `firm-owner.md`) are
   message-design lenses. Any claim that a specific contact *is* the owner-operator is an
   inference from company size and product holdings, not a data fact — and copy must not
   assert a recipient's role.
2. **The existing per-contact role work stands on its own method.** The top-20 call sheet
   researched each contact individually and already flags the unconfirmable ones
   ("Makeba's officer role unconfirmable"; "'Polly' is public admin of ESD 1, not confirmed
   ESD 6"). That per-account research is the only title verification path the current data
   supports, and it does not scale past hand-researched heads.
3. **Segmentation is unaffected.** Motive segments (switcher / diy / no-data) read Products,
   not titles; the 505/335/22 split and the suppression logic stay valid.

## The closure rule (what a session may and may not do)

- **May:** use personas to choose angle and tone for a segment; keep hand-researching heads
  of list per the account-research skill; treat researched, flagged roles as the only
  verified ones.
- **May not:** write copy that names or assumes the recipient's role; claim persona routing
  is data-backed; backfill a Title column by guessing from first names or company names.

## If per-title routing is ever actually wanted

The path is a **Clay title enrichment pass** (Clay is wired to this workspace) scoped to
Tier 1 only, writing a real `Title` field with a per-row provenance marker, then a re-run of
this validation against actual titles. Cost applies per enriched row; nothing justifies
enriching all 862 for a campaign whose sends are tier-ordered. Until that exists, this
report is the standing answer to "was title fit validated": it cannot be, and copy is
written so it does not need to be.
