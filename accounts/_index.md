# Account index

> **OPERATING DEPLOYMENT NOTICE (2026-08-08):** accounts operate LIVE in the private
> `albatross-engineering-os` deployment (`machinery/gtm-kit/accounts/`). This upstream
> repo is authoritative for CORE only (skills, playbooks, docs, tools — the re-vendor
> loop); account content below is frozen at the vendor date and is historical here.

The catalog: one line per account, the declared source of truth for what accounts exist,
their tier, and where each stands. Lifecycle: `scaffolded → configured → live → paused`.

A new account gets its row when `_template/` is copied (setup Step 0); the row's status moves
as the account does. The index is a catalog, not a record — one line each, details live in
the account's own `ACCOUNT.md`, and this file never describes an account's internals.

| Slug | Business | Tier | Status | Since | Notes |
|---|---|---|---|---|---|
| `fenton` | Fenton Bookkeeping LLC | engineer | live | 2026-08-06 | Two tracks (Bounce, white-label), both loaded, nothing sent. Origin + host-repo relationship: `fenton/EXTRACTION.md` |
| `revenue-engineering` | Raymond's revenue-engineering business | engineer | scaffolded | 2026-08-07 | Context empty; fill via `skills/setup`. Buyer/track decision pending |
