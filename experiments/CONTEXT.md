# experiments/ — the backlog contract

A record library whose records are open questions with a way to close them. This replaces
the retired conflict register: where two instruments genuinely disagree, the disagreement
is not curated as doctrine — it is queued as a test, named where it runs, and closed by a
dated verdict.

## Reads / does / writes

- **Reads:** nothing on its own; each record names its instrument docs.
- **Does:** holds one file per experiment, numbered in arrival order (`NNN-slug.md`).
- **Writes:** a record's `Status` and `Verdict` move as the test does. A verdict is a
  dated entry plus the follow-on edits it licenses — never a silent blend of the
  instruments (the losing instrument is retired or scoped, on the record).

## The record

```markdown
# NNN — [question, stated as a choice]

- **Instruments:** [doc A] vs [doc B]
- **Hypothesis:** [what the operator currently expects, and why]
- **Runs in:** [which deployment / which account / which campaign]
- **Decision gate:** [what measurement closes it]
- **Status:** queued | running | closed
- **Verdict:** [dated, or —]
```

## Rules

1. **Instruments stay parallel until the verdict.** An account declares which instrument
   a campaign runs under; the two are never blended inside one campaign.
2. **A test runs somewhere real.** An experiment with no `Runs in` is a shower thought —
   it can sit here, but it cannot be cited.
3. **Closing is an edit event.** The verdict licenses specific changes to specific files,
   listed in the record when it closes.

## Human check

Before opening a record: is this a genuine instrument conflict, or just a preference?
Preferences get decided by the operator now, for free — only questions that need data
earn a queue slot.
