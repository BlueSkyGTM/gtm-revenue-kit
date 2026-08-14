# Start here

## What this is

A go-to-market engine that runs out of folders you can read.

There is no application to log into and no database. The whole system is markdown: what you
know about your buyers, the methods for acting on it, and the record of what you did. An AI
coding agent (Claude Code) reads those folders and does the work — research an account,
score a list, build a campaign, handle a reply — without you re-explaining your business
every session.

It serves **several accounts at once**. One shared engine, one folder per client or
business, and nothing leaks between them.

## What it does

| You say | It produces |
|---|---|
| "Set up an account for acme.com" | Six context files written from public research: who they sell to, what signals matter, how they are positioned, who the competitors are |
| "Research northwind.com" | A full brief ending in the angle: why now, why us, the hook, who to contact |
| "Score this list" | Every account scored against that account's own model, tiered, sorted, with the ones worth real effort flagged |
| "Build a campaign for [signal]" | Segments, a multi-touch sequence, the copy, and how it will be measured |
| "Here is a reply" | Classified, routed, qualified, and prepped for the call |
| "Run the weekly update" | Stale context found, changes drafted, results logged |

## What it never does

- **It never sends.** No send tool is wired in this repo, on purpose. You wire your own, and
  a human decides every batch.
- **It never holds contact data.** Lists, exports, and enrichment files stay out of git by
  rule and by pattern. The methodology is tracked; the people are not.
- **It never mixes accounts.** One account's facts cannot reach another's campaign, and one
  account's opt-out list never suppresses another's.
- **It never invents a fact to fill a slot.** Unknowns are marked as unknown. A confident
  wrong detail about a prospect is worse than no detail.
- **It never decides for you.** Every proactive action is offered and waits for a yes.

## How to start

**1. Read the map.** `CLAUDE.md` — the folder layout and the one rule (name the account
first). Two minutes.

**2. Create your first account.**

```
Read skills/setup/SKILL.md and set up an account for [your-domain.com] as [slug]
```

It researches your company and writes the account from public data. You review, then
sharpen the handful of things only you know.

**3. Run something real.**

```
Read skills/account-research/SKILL.md and research [a-real-prospect.com] for account [slug]
```

Your context is already there. The output is a brief, not a summary.

## Where things live

| | |
|---|---|
| The map | `CLAUDE.md` |
| "What's my task? Where do I go?" | `CONTEXT.md` |
| Your accounts | `accounts/<slug>/` — context, outputs, brand, opt-outs |
| What the engine can do | `skills/` (Claude runs these), `workflows/` and `playbooks/` (you read these) |
| The rules | `docs/` — isolation, loading, tiers, standards |
| A fully worked example | `examples/sample-company/` — Relay, a fictional company with every file filled in |
| What this changed from the open-source original | `DIVERGENCE.md` |

## The two habits that make it work

**Name the account before anything else.** Every session, every skill. Context loaded under
the wrong account produces answers that look right and are not.

**Put each fact in exactly one place.** When something is true, it goes in the one file that
owns it, and everything else points there. A number written down twice will disagree with
itself within a month, and you will not know which copy is stale.
