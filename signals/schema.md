# The signal record — four dimensions, four fields, one gate

The anatomy every signal in this system carries. The four-dimension split and the
per-signal field set are adapted from the MIT-licensed `icp-intelligence-mcp` skeleton
(attribution: `NOTICE.md`); the admission gate is this kit's own (principle 1).

**Adoption status: ADOPTED** — second-brain verdict 08-13, **operator-confirmed 08-14**.
Two notes travel with the adoption. Provenance caution: the source repo ships
no tests or eval harness, so its weights (fit 40 · intent 30 · relationship 15 ·
timing 15) are reported, not verified — starting values at most, and values live in the
account regardless. And what the split fixes on the record: the old model had
relationship and timing as play triggers only, invisible to the score — a warm and a
cold account with identical firmographics tiered identically. Here they are scored
dimensions with decay classes, while the plays remain the event-response layer on top:
dimension feeds the score, play handles the firing.

## The four dimensions

Every signal feeds exactly one dimension. The old flat "signal bucket" lumped these;
splitting them matters because they have different sources, different decay, and
different actions when they fire.

| Dimension | What it evidences | Typical decay |
|---|---|---|
| **Fit** | They match who we serve (firmographic, technographic, organizational) | slow — structure changes slowly |
| **Intent** | They are actively looking (content, search, evaluation behavior) | fast — intent expires in weeks |
| **Relationship** | A path exists (past champion, mutual, prior conversation) | slow, event-refreshed |
| **Timing** | A window just opened (funding, hire, expansion, renewal, crisis) | fast, dated by the event |

## The record

```markdown
### [Signal name]

- **Dimension:** fit | intent | relationship | timing
- **Trigger:** [the event or condition, stated plainly]
- **What fires:** [detection — where it is observed, what exact change]
- **Why it matters:** [REQUIRED — the buying mechanism, the reason this predicts anything.
  A signal that cannot fill this field does not enter the library.]
- **How to track:** [sources and alerts, named]
- **Decay class:** [fast | slow | event-dated — the CLASS; multipliers are account values]
- **Provenance:** [course-reasoned | operator-proven | upstream-verified — per principle 1]
```

## The gate, stated once

**"Why it matters" is required, and it is the whole point.** The previous signal set was
discarded not because the signals were wrong but because nobody could say why they were
right — backstory-free signals produce campaigns nobody can debug. The schema makes that
mistake structurally impossible: no why, no entry.

## Where values live

Point values, weights, and decay multipliers are account values
(`accounts/<slug>/context/scoring-model.md`, principle 3). A core signal record carries
mechanism and backstory only. An account adopts a signal by copying its record into
`context/signal-library.md` and assigning its numbers there.
