# Scoring Model — [Account name]

**The one scoring authority for this account.** Every number the engine uses lives here:
weights, point values, band boundaries, decay multipliers, eligibility gates. Core skills
hold the mechanism and read their values from this file.

Why the split: `foundations/principles.md` §3. Short version — mechanism is the same for
every account, values never are. Two accounts may score the same company differently and
both be right.

**Defaults in this template** are the upstream kit's original working rubric
(`baseline-gtm-starter-kit`), restored so a new account starts from a runnable model
instead of a blank form. They are unverified against your market — treat every one as a
day-one hypothesis and recalibrate through §8.

Last updated: [YYYY-MM-DD]

---

## 1. Fit dimensions and weights

The composite score is 0–100. Dimensions and their maximum contributions:

| Dimension | Max points | What it measures | Source |
|---|---|---|---|
| Firmographic | 30 | size, geography, industry, stage | [where this is read from] |
| Technographic | 20 | what they run on, at what level | [ ] |
| Organizational | 20 | team shape, who owns the problem | [ ] |
| Signal / intent | 30 | dated events predicting readiness | `signal-library.md` |

*Weights are a reversible hypothesis until reply data lands. Re-tune from results, and log
the change below.*

## 2. Per-attribute point map

*The values behind dimension 1–3. One row per attribute the scorer can observe. The rows
below are the upstream defaults — replace the bracketed placeholders with this account's
specifics and re-tune the points from results.*

| Attribute | Value | Points |
|---|---|---|
| Employee count in range | [your ICP range] | 0–10 |
| Industry match | primary / secondary / other | 10 / 5 / 0 |
| Funding stage match | ideal / adjacent / outside | 10 / 5 / 0 |
| Uses [key integration tool] | confirms workflow match | 0–10 |
| Uses [secondary tool] | confirms sophistication level | 0–5 |
| No [disqualifying tool] | absence of competitive blocker | 0–5 |
| Has [key role/function] | decision-maker exists | 0–10 |
| [Role] hired in last 12 months | new leader = change appetite | 0–5 |
| Hiring for [relevant role] | active investment in the function | 0–5 |

**Normalization:** [how raw values map onto the bands — rounding, caps, what happens to
missing data]

## 3. Signal point values

*The intent dimension. Signal definitions, detection, and decay live in
`signal-library.md`; only the numbers live here.*

| Signal | Points | Notes |
|---|---|---|
| [signal name] | [+N] | [any condition on the award] |

**Combination bonuses:**

| Combination | Bonus | Why it is more than the sum |
|---|---|---|
| [signal A + signal B] | [+N] | [ ] |

## 4. Tier bands

*Upstream defaults; the actions column is the upstream rubric's, worth keeping.*

| Score | Tier | What it buys |
|---|---|---|
| 80–100 | 1 | bespoke research (full research skill), personalized touch, immediate |
| 60–79 | 2 | sequenced, signal-keyed copy within 48 hours of the trigger |
| 40–59 | 3 | light touch, general framing, automated sequence |
| 20–39 | — | monitor only, re-score in 90 days, no send |
| 0–19 | — | excluded from active lists |

**Research cap:** the top [N] of Tier 1 get a bespoke brief. The 20–40 minute research pass
is the scarce resource, not the sequence.

## 5. Segments and message classes

*If this account's buyers split by motive — already buying this elsewhere vs. not — the
frame changes even at identical scores. Segment sets the frame; rank never does.*

| Segment | Condition | Frame |
|---|---|---|
| [ ] | [ ] | [switching / conversion / other] |

**Suppressed classes:** a message class that is factually false for a segment must never
send to it. List each here with the condition that suppresses it.

| Message class | Suppressed when | Why it would be false |
|---|---|---|
| [ ] | [ ] | [ ] |

## 6. Decay

| Signal age | Multiplier |
|---|---|
| 0–30 days | 100% |
| 31–60 days | 75% |
| 61–90 days | 50% |
| 91–180 days | 25% |
| 180+ days | 0% — expired |

*Standing states (a plan tier, a headcount) are facts, not events, and do not decay. Mark
which signals are exempt in `signal-library.md`.*

## 7. Reachability

Checked before a score is trusted, because a brief on a dead account is worse than no
brief — it is expensive, it looks authoritative, and it sends.

| State | Condition | Effect |
|---|---|---|
| verified | site resolves, business matches the record, contact route live | scorable |
| unverified | not yet checked | no send |
| dead | [dead domain / rebranded out of scope / wrong stage of life] | excluded, with cause recorded |

## 8. Campaign gates and benchmarks

*Launch and kill criteria, set deliberately before the first send. The former core
defaults (audience ≥ 50 · enrichment ≥ 80% · pause under 1% reply after 50 sends) were
retired as unverifiable provenance — if you adopt them, you adopt them as your own
hypothesis and log it below. Micro-list motions (`motions/channels/micro-lists.md`)
exempt themselves from volume gates by design.*

| Gate | Threshold | Action when failed |
|---|---|---|
| Minimum audience before launch | [N] | build on, don't send |
| Enrichment coverage before launch | [N%] | return to enrichment |
| Pause trigger | [reply rate over first N sends] | pause, diagnose list vs. copy |

**Benchmark stance (ruling 08-13, operator confirmation pending):** the kit runs
**benchmark-free until its own campaign data lands** — the first campaigns' results seed
this section with provenance `operator-proven`, the only provenance that closes it. The
diagnostic *shapes* are mechanism and apply without numbers:

| Pattern | Suspect |
|---|---|
| Low open rate | the subject line (or deliverability) |
| High open, low reply | the body / the CTA |
| High reply, low meeting | the wrong people, reached well |

## 9. Calibration log

*Every change to a number, with the evidence. This log is worth more than the current
values after a year.*

| Date | What changed | Evidence | Effect |
|---|---|---|---|
| [YYYY-MM-DD] | [initial values set] | [inferred / from data] | — |
