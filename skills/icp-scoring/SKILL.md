# Skill: ICP Scoring

**Duration:** 15–30 minutes per account (or run in batch)
**Output:** ICP score + tier assignment saved to CRM or `accounts/<slug>/outputs/scoring/`

> **Runs against one named account.** Every `accounts/<slug>/` path below resolves inside
> that account's folder. If the account was not named in the request, ask before reading
> anything — loading one account's context under another's name produces confident answers
> from the wrong buyer's facts, and nothing about the output looks wrong.
>
> **Read exactly what Inputs names, and nothing else.** Never bulk-load `context/` or
> `outputs/` (`docs/loading.md`). Every number this skill needs lives in the account's
> `context/scoring-model.md`, never in this file (`docs/isolation.md` §2).

---

## Quick Start

Single account:
```
Read skills/icp-scoring/SKILL.md and score [company.com] against our ICP
```

Batch:
```
Read skills/icp-scoring/SKILL.md and accounts/<slug>/context/icp-definition.md.
Score these companies and output a table sorted by score, Tier 1 flagged:
[paste list of company names or domains]
```

---

## Purpose

Score any account against your ICP and assign it to the right tier. Replaces gut feel with a repeatable model. When run at scale, it tells you which accounts to prioritize this week, which to monitor, and which to skip entirely.

---

## When to Run This Skill

- New accounts entering the pipeline — score before assigning to a rep
- Enrichment run complete — re-score the full account list
- ICP definition updated — re-score to find newly qualified accounts
- Preparing a campaign list — score to determine sequence tier
- Quarterly pipeline review — re-score all open opportunities

## Re-scoring Cadence

Scores go stale. Set a recurring schedule:

| Segment | Frequency | Why |
|---------|-----------|-----|
| Full account list | Quarterly | ICP drift, new signal data |
| Tier 1 accounts | Monthly | High-value; worth tracking closely |
| Active pipeline | After each campaign | Campaign results reveal scoring gaps |
| After ICP change | Immediately | Find newly qualified or disqualified accounts |

After a quarterly re-score, pull the delta: which accounts moved tiers? Accounts that dropped from Tier 1 to Tier 2 need to be removed from AE pipelines. Accounts that moved up need to be activated.

---

## Inputs

- Account name, domain, and available firmographic/technographic data
- `accounts/<slug>/context/scoring-model.md` — **every number this skill uses**: dimension weights, per-attribute points, signal values, tier bands, decay, reachability
- `accounts/<slug>/context/icp-definition.md` — what each criterion means for this buyer
- `accounts/<slug>/context/signal-library.md` — signal definitions, detection, which signals are exempt from decay

---

## Scoring Model

**This section is mechanism. It contains no values on purpose** (`docs/isolation.md` §2).
Read the account's `context/scoring-model.md` for every number, and score from that file —
never from the defaults shown here, and never from memory of another account.

Two accounts may score the same company differently and both be right. That is the design.

### Step 0: Reachability, before anything else

Read `scoring-model.md` §7. An account whose state is `dead` is not scored — it is excluded
with the cause recorded. A brief on a dead account is worse than no brief: it is expensive,
it looks authoritative, and it sends.

### Step 1: Fit dimensions

The composite is the sum of the fit dimensions plus the signal dimension. The account's
`scoring-model.md` §1 defines which dimensions exist and each one's maximum contribution;
§2 defines the per-attribute points inside them.

*Typical shape, for orientation only — the account file governs:*

| Dimension | Common max | Measures |
|---|---|---|
| Firmographic | 30 | size, geography, industry, stage |
| Technographic | 20 | what they run on, at what level |
| Organizational | 20 | team shape, who owns the problem |
| Signal / intent | 30 | dated events predicting readiness |

For each attribute, award the points the account's map assigns to the observed value. Where
a value is unknown, award nothing and mark the field unenriched — never estimate. An
inferred point is indistinguishable from an observed one once it is in the total, and the
whole list inherits the error.

### Step 2: Signal score

Award the values in `scoring-model.md` §3 for each active signal, then apply the decay
multiplier from §6 based on the signal's age. Signals the account marks as standing states
rather than dated events do not decay — `signal-library.md` says which.

Apply combination bonuses from §3 only where the account defines them. Two signals firing
is not automatically worth more than the sum.

### Step 3: Tier

Read the bands from `scoring-model.md` §4. A tier is a budget decision before it is a
priority decision: it sets research depth and touch count (`docs/standards.md`).

Then read §5. If the account defines motive segments, the segment sets the message frame
and the rank never does — and a message class the account marks suppressed for that segment
must not be used, whatever the score.

---

## Running at Scale (Batch Scoring)

When scoring a large list (50+ accounts), structure the output as a table:

```
| Account | Domain | Firmographic | Technographic | Org | Signal | Total | Tier | Action |
```

Instruct Claude:
```
Read skills/icp-scoring/SKILL.md and accounts/<slug>/context/icp-definition.md.
Score the accounts in [file or pasted list].
Output a scored table sorted by total score descending.
Flag any accounts scoring 80+ for immediate follow-up.
```

---

## Scoring Output Format

```markdown
# ICP Score: [Company Name]
Date scored: [YYYY-MM-DD]
Scored by: [Claude / Name]

## Score Breakdown

| Category | Score | Max | Notes |
|----------|-------|-----|-------|
| Firmographic fit | X | 30 | [Key observations] |
| Technographic fit | X | 20 | [Key observations] |
| Organizational fit | X | 20 | [Key observations] |
| Active signals | X | 30 | [Signals present] |
| **Total** | **X** | **100** | |

## Tier Assignment: [Tier 1 / 2 / 3 / 4 / Exclude]

## What Qualifies Them
- [Specific reason 1]
- [Specific reason 2]

## What Disqualifies or Reduces Score
- [Gap 1 — what would need to change for this to be a higher tier]

## Recommended Next Action
[Specific: which skill to run next, which sequence to assign, or what to monitor]

## Re-score Trigger
[Condition that should trigger re-scoring — e.g., "If they raise a new round" or "If they hire a VP of Ops"]
```

---

## Calibration Notes

*Update this section when you find scoring gaps — accounts that scored high but churned, or accounts that scored low but converted.*

| Date | Account | Scored | Actual outcome | What the model missed |
|------|---------|--------|---------------|----------------------|
| | | | | |

Run a calibration review quarterly: pull the last 90 days of scored accounts and compare predicted tier to actual outcome. Adjust point values where the model is consistently wrong.
