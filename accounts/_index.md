# Account index

> **CORE-ONLY FINALIZATION (2026-08-10):** this upstream repo is authoritative for CORE
> only — foundations, motions, signals, experiments, tools, the `_template/` stamp, and the
> re-vendor loop. **No operating account lives here anymore.** Each account lives inside
> the business OS that runs it (vendored kit, `machinery/gtm-kit/accounts/<slug>/`);
> the rows below are deployment pointers, and the account folders were removed 2026-08-10
> (full content preserved in this repo's git history — provenance, not a copy: never read
> a removed account folder out of history to answer a live question). The rule this note
> applies, and the full which-copy-holds-what map, is `estate.md`.

The catalog: one line per account, the declared source of truth for what accounts exist,
their tier, and where each stands. Lifecycle: `scaffolded → configured → live → paused`.

A new account gets its row when `_template/` is copied (setup Step 0); the row's status moves
as the account does. The index is a catalog, not a record — one line each, details live in
the account's own `ACCOUNT.md`, and this file never describes an account's internals.

| Slug | Business | Tier | Status | Since | Operates in |
|---|---|---|---|---|---|
| `fenton` | Fenton Bookkeeping LLC | engineer | **shelved 2026-08-13** | 2026-08-06 | `fenton-bookkeeping-os` (private, dormant) — resumes after albatross; planned to become albatross's client account #1 (`estate.md`) |
| `revenue-engineering` | Albatross Revenue Engineering | engineer | scaffolded | 2026-08-07 | `albatross-engineering-os` (private) — the product company's own motions |
