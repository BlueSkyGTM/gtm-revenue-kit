# outputs/ — Fenton Bookkeeping LLC (the product layer)

**New every run.** Everything here is a run artifact: what a session emitted, dated, kept as
the record. The factory it read from is `../context/`, and **nothing here writes back into
that folder** without a human promotion.

This file describes the folder's *shape and conventions*, deliberately not its contents — a
hand-maintained file list would be stale within a week, and the filesystem is the state
machine. To know what exists, look; to know where a new thing goes, read below.

## Where a new artifact goes

| Kind of thing | Home | Named |
|---|---|---|
| A dated one-off: briefing, debrief, evaluation, proposal, coverage report | this folder, top level | `YYYY-MM-DD-[type]-[name].md` |
| Per-account research, one file per company | `account-research/` | `YYYY-MM-DD-[company]-research.md` |
| A red-team or positioning audit | `audits/` | `YYYY-MM-DD-[type]-[subject].md` |
| Anything belonging to one campaign — sequences, metrics, results, the loaded list | `campaigns/[YYYY-MM-DD-campaign-name]/` | per that campaign's own README |
| A scored or segmented list | `lists/` | dated |

**The top level is for durable one-offs only.** If a kind of artifact starts arriving in
batches, it gets a subfolder — that is what happened to `account-research/` on 2026-07-29,
when 28 files from one July research batch were sitting in the same flat list as the
strategy documents and made the folder unreadable.

## The two files that are not dated, and why

- `inbound-handoff.md` — the live inbound-reply handoff. Current state, not a snapshot, so a
  date on it would lie.
- `README.md` — this file.

Everything else carries its date in the filename. A dated artifact is never edited to stay
current; a new dated artifact supersedes it and says so.

---

## A note on paths in the older files

Everything here predates this engine: it was written inside a host repo where the GTM
workspace sat beside a bookkeeping workspace, and where the second buyer was expressed as
`-white-label` filename suffixes rather than a track folder.

**Those files were not rewritten.** They are dated run records — evidence of what was true
and what was believed on the day they were written — and editing them to look current would
destroy the one property that makes them worth keeping. The live `context/` files were
rewired; these were not.

So when an older output points at `context/icp-definition-white-label.md`, read
`context/tracks/white-label/icp-definition.md`. When it points anywhere outside this account
— `books/`, another workspace, `_archive/`, `tasks/` — that path belongs to the host repo,
and some of those targets were already deleted there before this transfer. Treat such a
reference as a citation to a document that existed on the date of the file, not as a live
link. Do not go looking for it here.
