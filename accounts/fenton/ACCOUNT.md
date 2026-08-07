# ACCOUNT.md — Fenton Bookkeeping

The summary layer for this account. Read when the account is named; deeper files are
pointed at, not restated.

---

## Identity

**Slug:** `fenton`
**Tier:** engineer — the operator tunes the model, not just the campaigns (`docs/tiers.md`)
**Status:** live — context configured, two campaigns loaded, **nothing sent yet**
**Operator:** Raymond — go-to-market and the machinery
**Principal:** Miriam — **sole approver of a send.** Her yes is required no matter who is at
the keyboard.

> **Origin.** This account's context and outputs were operated inside a host repo
> (`fenton-bookkeeping-os/workspaces/practice/`) before this engine existed, and were
> transferred here as account one. Provenance: `NOTICE.md` §2, `DIVERGENCE.md`.

---

## Company

**Fenton Bookkeeping LLC** does QuickBooks cleanup, monthly bookkeeping, and payroll for
small businesses — one certified accountant owning the books start to finish, instead of a
rotating pool or a platform.

Stage: bootstrapped, founder-led — one delivering practitioner
GTM motion: owner-led outbound, plus an inbound application form
Primary channels: email (sequenced), phone for the researched head of the list

**The delivery constraint that governs targeting:** one person delivers. Winning a handful
of firm-sized accounts fills capacity. This is why the research pass is capped and why the
top of the list is worked by hand rather than by volume.

---

## Tracks

Two buyers, deliberately separated. **Never blend them** (`context/tracks/README.md`).

| Track | Buyer | Offer | Where | Status |
|---|---|---|---|---|
| Bounce (primary) | small businesses on QuickBooks Online | done-for-you bookkeeping | root `context/` | loaded, not sent |
| `white-label` | accounting and CPA firms | delivery capacity resold under the firm's brand | `context/tracks/white-label/` | loaded, not sent |

**Channel conflict is real here and suppression runs both ways.** A small business reached
directly must never also be reached through its accounting firm, and a firm must never be
pitched while one of its clients is on the direct list. Check before either track sends.

The root `context/` files are the account-wide layer *and* the Bounce track. The white-label
track overrides ICP, positioning, competitor radar, and messaging; everything else
(`profile`, `signal-library`, `scoring-model`, `personas/`, `pricing-strategy`) is shared,
with track-scoped sections inside.

---

## ICP

Full definition: `context/icp-definition.md` · White-label:
`context/tracks/white-label/icp-definition.md`

**Who we sell to (Bounce):** US small businesses actively paying for QuickBooks Online,
owner-managed, with no internal bookkeeper — the owner or a generalist admin is doing the
books today. Size is a delivery preference, never a filter: large QuickBooks accounts stay
in-ICP.

**Tier 1:** already paying Intuit for done-for-you help (Live / Expert Assisted), and/or on
the plan tiers that took the largest 2026 increases
**Tier 2:** mid-tier plans, or payroll active without the stronger product signals
**Tier 3:** entry plan only, no add-ons

**Never target:** businesses not on QuickBooks · businesses genuinely off on a true ERP ·
businesses with an internal bookkeeper or finance team · non-US · pre-revenue.

**Accounting and CPA firms are anti-ICP for Bounce and the *target* for white-label** — the
clearest reason the two tracks cannot share a list.

---

## Personas

`context/personas/` — `owner-operator.md` and `office-ops-manager.md` (Bounce),
`firm-owner.md` (white-label).

Bounce accounts are owner-led: champion, economic buyer, and the person touching the books
are usually one person. Do not manufacture a committee to fill a table.

---

## Positioning

`context/positioning.md` (Copy Rules live here) · `context/messaging-house.md` ·
white-label variants under `context/tracks/white-label/`

**We win when** the buyer has felt a specific event — a price increase on their own invoice,
an error they had to fix, months lost being behind — and wants one accountable person rather
than a platform or a rotating pool.

**We lose when** the buyer is a pure price-shopper, or has a local bookkeeper they trust.
The honest differentiator against a good independent bookkeeper is the *provable* floor —
certification, documented process, the client owning their own file — never the category.

---

## Signals

`context/signal-library.md` · every point value in `context/scoring-model.md`

**Act immediately:** already paying for done-for-you help inside the incumbent platform ·
on the plan tiers that took the largest increases · a public complaint about the platform's
automation · renewal window inside 30–60 days.

**Sequence:** long tenure on the platform · recently upgraded plan · hiring for a
bookkeeping or admin role · payroll active.

**White-label Tier 1:** the firm is hiring delivery staff, or publishes waitlist / "not
accepting new clients" language. Both decay fast — act inside the posting window.

---

## Sending

**Send tool:** Instantly (remote hosted MCP). **Not wired in this repo.**
**Config:** the operator's own `.mcp.json`, gitignored, never committed
(`.mcp.json.example` shows the shape; `DIVERGENCE.md` E2 explains why the wall exists).

**Sending is the principal's decision, every time.** Sending to a list is not a different
kind of act than sending one email; it is the same act at scale.

**Suppression, before every batch:**
1. `optouts.md` in this folder — append-only, permanent, legal
2. The client roster in the host repo — **names and domains only**, never figures, so a
   paying client never receives a cold campaign
3. The other track's live audience (channel conflict, above)

> **Opt-out authority, while both copies exist.** The host repo's ledger remains the live
> one until its migration completes. This file is the transferred copy. Append to **both**
> until the host repo's GTM workspace is retired, then delete the host copy and record the
> date here. Two ledgers that silently disagree is the one failure mode this note exists to
> prevent. (`DIVERGENCE.md` G3.)

---

## Stack

Lead data: Airtable ("QuickBooks Lead Capture" → `Contacts`, 863 records)
Enrichment: Clay | Outbound: Instantly | Site and inbound form: host repo

---

## Account overlays

Instance facts a core skill would otherwise have to hardcode. Relocated here from inside the
skills, which is what their own re-export markers prescribed (`DIVERGENCE.md` D8).

| Skill | What it needs | Where it is, in this account |
|---|---|---|
| `account-research` | what they run on, and at what level | the Airtable `Products` field — the SKU mix is the strongest single fact about an account |
| `account-research` | tenure with the incumbent | the Airtable `Customer Lifetime` field |
| `account-research` | firm-buyer evidence (white-label track) | ProAdvisor directory listing, published delivery promises, open delivery-role postings |
| `icp-scoring` | every value | `context/scoring-model.md` |
| `reply-handling` | motive segment, and whether a claim is suppressed for this record | Airtable `Motive_Segment` and `Suppress_Price_Fatigue`; semantics in `context/scoring-model.md` §5 |

**Segment note for reply handling:** a buyer already paying for human help hears a
comparative conversation (turnaround, consistency, who answers); one doing it themselves
hears a diagnostic one, where the review *is* the product on call one.

---

## Current priorities

- [ ] Nothing has sent. Warmup and the principal's go decide the first batch.
- [ ] Pricing: hours × rate on approved engagements only — no fixed-fee quote until one real
      file has been timed (`context/pricing-strategy.md`).
- [ ] White-label positioning has an open question: the offer was reframed from capacity
      relief to market entry, which conflicts with the earlier decision to deprioritize
      tax-led firms. Reconcile before that track sends.
