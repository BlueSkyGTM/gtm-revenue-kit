# ACCOUNT.md — Revenue Engineering (account two)

> **Status: scaffolded, not configured.** The folder exists and the contract is in place;
> the context files are still the blank template. Fill it by running:
>
> ```
> Read skills/setup/SKILL.md and set up an account for [domain] as revenue-engineering
> ```
>
> Skip Step 0's folder creation — this folder already exists. Everything from Step 1 on
> applies.

---

## Identity

**Slug:** `revenue-engineering`
**Tier:** engineer (`docs/tiers.md`)
**Status:** scaffolded
**Operator:** Raymond
**Principal:** Raymond — operator and principal are the same person here

---

## Company

**The business that sells GTM systems.** Where account one *uses* an engine to win
bookkeeping clients, this account sells the engine itself — the install, the configuration,
and the operating support around it.

**The meta-property, stated once so nobody trips on it later:** this account runs inside the
product it sells. That is not a paradox, it is the demonstration — every campaign run here
is a live proof artifact for the thing being sold, and every rough edge found while running
it is a defect report against the product written by its most demanding user.

It also means a discipline the other accounts do not need: **operating this account and
developing the engine are different jobs.** Work done here goes in `accounts/revenue-engineering/`.
Improvements to the engine go in core, deliberately, as product work. Fixing a core skill
mid-campaign because it annoyed you during a send is how a product acquires one customer's
assumptions.

---

## What to fill in at setup

Setup will research a domain and write the rest. Two things it cannot infer, worth deciding
before it runs:

1. **Who the buyer is.** The obvious candidates pull in different directions — operators who
   want the outcome and would buy an install, versus engineers who want the engine and would
   buy the repo. They are different ICPs with different objections, and if both are real they
   are **tracks**, not one blended audience (`context/tracks/README.md`).
2. **What is actually for sale.** Template, done-with-you install, trade modules, ongoing
   operator support — the SKU ladder decides the offer map and therefore the copy.

---

## Sending

**Send tool:** none wired.
**Config:** the operator's own `.mcp.json`, gitignored, never committed. See
`.mcp.json.example`.

**Suppression, before any batch:**
1. `optouts.md` in this folder
2. **Cross-account channel conflict** — no company that appears in another account's live
   audience may be contacted from this one, in either direction. Two accounts owned by the
   same operator writing to the same company in the same week is the failure this rule
   exists to prevent. Check by name and domain only, never by reading the other account's
   files (`docs/isolation.md` §3).

---

## Current priorities

- [ ] Decide the buyer and whether it is one audience or two tracks
- [ ] Run `skills/setup` to fill `context/`
- [ ] First campaign — which doubles as the product's first case file
