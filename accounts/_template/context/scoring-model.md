# Scoring Model — [Account name]

**The one scoring authority for this account.** Every number the engine uses lives here:
weights, point values, band boundaries, decay multipliers, eligibility gates. Core skills
hold the mechanism and read their values from this file.

Why the split: `docs/isolation.md` §2. Short version — mechanism is the same for every
account, values never are. Two accounts may score the same company differently and both be
right.

Last updated: [YYYY-MM-DD]

---

## 1. Fit dimensions and weights

The composite score is 0–100. Dimensions and their maximum contributions:

| Dimension | Max points | What it measures | Source |
|---|---|---|---|
| Firmographic | [30] | size, geography, industry, stage | [where this is read from] |
| Technographic | [20] | what they run on, at what level | [ ] |
| Organizational | [20] | team shape, who owns the problem | [ ] |
| Signal / intent | [30] | dated events predicting readiness | `signal-library.md` |

*Weights are a reversible hypothesis until reply data lands. Re-tune from results, and log
the change below.*

## 2. Per-attribute point map

*The values behind dimension 1–3. One row per attribute the scorer can observe.*

| Attribute | Value | Points |
|---|---|---|
| [attribute] | [observed value] | [+N] |

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

| Score | Tier | What it buys |
|---|---|---|
| [80]–100 | 1 | bespoke research, personalized touch |
| [60]–[79] | 2 | sequenced, signal-keyed copy |
| [40]–[59] | 3 | light touch, general framing |
| below [40] | — | monitor only, no send |

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

## 8. Calibration log

*Every change to a number, with the evidence. This log is worth more than the current
values after a year.*

| Date | What changed | Evidence | Effect |
|---|---|---|---|
| [YYYY-MM-DD] | [initial values set] | [inferred / from data] | — |
