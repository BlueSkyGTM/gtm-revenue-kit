# Skill: Reply Handling

**Trigger:** A reply lands from any outbound campaign, or an inbound application arrives
**Duration:** 5 minutes per reply to classify and route; discovery prep is per-call
**Output:** A classified reply, the action it routes to, and — for qualified interest — a
pipeline row and a discovery prep sheet

> **Runs against one named account.** Every `accounts/<slug>/` path below resolves inside
> that account's folder. If the account was not named in the request, ask before reading
> anything — loading one account's context under another's name produces confident answers
> from the wrong buyer's facts, and nothing about the output looks wrong.
>
> **Read exactly what Inputs names, and nothing else.** Never bulk-load `context/` or
> `outputs/` (`foundations/principles.md`). Every number this skill needs lives in the account's
> `context/scoring-model.md`, never in this file (`foundations/principles.md` §3).

---

## Quick Start

```
Read motions/skills/reply-handling/SKILL.md. Account [slug]. Here is the reply: [paste].
Classify and route it.
```

---

## Purpose

Replies are the scarcest artifact the engine produces, and the seam where a campaign becomes
pipeline. Most GTM repos stop at send, which leaves the highest-value moment in the whole
motion to improvisation.

This skill is that missing middle: what to do with each kind of reply, in what order,
without inventing qualification on the fly. It **routes** — it does not restate intel that
lives elsewhere.

---

## Inputs

- The reply, verbatim
- `accounts/<slug>/ACCOUNT.md` — where this account's pipeline lives, who approves a send,
  what its suppression sources are
- `accounts/<slug>/context/icp-definition.md` — the fit test in Step 3 (the matching
  `context/tracks/<track>/` file if the campaign belongs to a track)
- `accounts/<slug>/optouts.md` — for class A
- The campaign's `brief.md`, for what was actually claimed in the copy

---

## Step 1: Classify — every reply is exactly one of six

| Class | Looks like | Route (Step 2) |
|---|---|---|
| **A. Opt-out** | "take me off your list", "unsubscribe", any removal request however phrased | **Immediately**: append to `accounts/<slug>/optouts.md`. Append-only, permanent, honored on every future send. Nothing else happens with this reply. |
| **B. Qualified interest** | Asks about the offer, the price, availability, or some version of "tell me more" / "call me" | Pipeline row + discovery prep (Steps 3–4) |
| **C. Soft signal** | Positive but deferring: "not now, try me after [season]", "just signed with someone" | Log verbatim in the campaign's `results.md`; pipeline row at the earliest stage with a **next touch date**; no sequence re-entry before that date |
| **D. Referral** | "Not me, but talk to [name]" | New lead row, lead source = the original campaign slug + `-referral`. If the referrer is offering to route business rather than buy, that is a partnership conversation, not a pitch |
| **E. Negative / hostile** | "Not interested", or worse | Log verbatim in `results.md`. No response. Not an opt-out unless removal is actually requested — but when in doubt, treat as A |
| **F. Question-with-teeth** | Challenges a claim the copy made | Log verbatim **and** flag to the operator same-day: this is copy-defect evidence, and it means the claim reached someone it is false for. Never argue the claim |

**Bounces and auto-replies are not replies.** They belong to the send tool and the
enrichment record; they never produce a row here.

## Step 2: Route — the mechanical action per class

**A** is immediate and unconditional: the row goes in the ledger before the next batch
sends. Nothing about it waits for a decision.

**B–D** produce a pipeline row, and the row is **offered, then created on the operator's
yes** — the same posture as every other proactive effect in this engine:

> *"[Lead] replied [class] — add them to the pipeline at [stage]?"*

On yes, create or update the row wherever this account keeps its pipeline (`ACCOUNT.md`
names it), with the **lead source filled at creation**. A lead source left blank at creation
is permanently blank: nothing downstream can reconstruct which campaign produced a reply,
and the whole funnel loses its attribution at the one moment it was knowable.

**E–F** produce no row.

**Speed, by class:** B is same-day, because outbound interest decays in hours. A is same-day
because it is a legal obligation. F is same-day because a live campaign is making a false
claim to someone. C, D, and E can batch to end of day.

## Step 3: Qualify — the rubric, before any call is booked

Score what the reply plus the record already show. This is a routing rubric, not a gate: a
qualified stranger gets a call, and an unqualified one gets a polite close rather than a
slow fade.

| Dimension | Qualified when | Disqualified when |
|---|---|---|
| **Fit** | Matches the campaign's ICP file | An anti-ICP row applies |
| **Authority** | The person replying can decide, or names who does | No path to the decision (ask once: "who else would weigh in?") |
| **Need shape** | Names or implies a real state the offer addresses | Wants something the account refuses to sell |
| **Timing** | Anything from "now" to a datable later (→ class C) | Vague "someday" with no event attached |
| **Channel integrity** | — | Reaching them conflicts with another track's relationship (`context/tracks/README.md`) — suppress both ways |

**Two of five failing → close politely.** The close is also copy: short, no pitch, leaves the
door open once.

## Step 4: Discovery prep (class B only)

Four questions are the call's spine, in order, after the opener. They localize the standard
frameworks to any account's trade:

1. **How bad is it, in numbers?** — the current state, measured. This sizes the work.
2. **What broke last?** — the pain in their words. This line is the whole reason they
   replied; read it back to them.
3. **Who else touches this?** — the decision process, plus whoever is doing the job today
   (themselves, a vendor, a competitor).
4. **What must be true in 90 days?** — the compelling event: a deadline, a filing, a lender,
   a sale. Sets urgency honestly, without manufacturing it.

**Price is asked, never answered, on call one** unless this account has published pricing
that the operator has approved for quoting. Close on the diagnostic, not the retainer.

If the account defines motive segments (`context/scoring-model.md` §5), read the segment
before the call: a buyer already paying someone else hears a comparative conversation; one
who is not hears a diagnostic one. Same call structure, different center of gravity.

## Step 5: Log and loop

Every classified reply gets one line in the campaign's `results.md`: verbatim quote, class,
action taken, date.

Reply data is what eventually validates the scoring weights and the copy angles — it is the
only evidence that turns the model from a hypothesis into a measurement. A reply that
changed your read of a segment is a **note for the next campaign build**, not an inline edit
to `context/`. Generated learning never writes into the factory layer directly; promotion is
a human cut with a provenance marker.

---

## What this skill never does

- **Never sends.** Drafting a response is fine; sending is the operator's, through the send
  tool, suppression first.
- **Never quotes a price** the account has not approved for quoting.
- **Never books the principal's calendar without offering first.** "Want me to propose two
  slots?" is the shape.
- **Never edits `context/` from a reply.** One reply is an anecdote; the factory layer
  changes on evidence, by a human, with the reason recorded.
