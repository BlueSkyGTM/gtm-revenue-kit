# Standards — the bar every account's work is held to

Core standards. These are method and measurement, so they are the same for every account.
Where a standard has a number attached, core carries the **default**; the account's
`context/scoring-model.md` is authoritative if it sets a different one.

## PVP — the permissionless value prop

**Strip the CTA. If the message still teaches the prospect something about their own
business, it passes. If it is pointless without the ask, it is a pitch.**

Mandatory for Tier 1 and Tier 2 first touches. The test is mechanical: delete the last
line, read what remains, and ask whether a stranger would be glad they read it.

What fails the test, reliably:
- A fact they already know, said back to them ("I see you use [their obvious tool]")
- A compliment as an opener
- A question whose only purpose is to start a reply chain
- Anything whose value is contingent on them booking a call

## Tiers set effort, not just order

| Tier | Default band | Research | Touches |
|---|---|---|---|
| 1 | 80–100 | bespoke brief, capped at the top N | personalized, multi-touch |
| 2 | 60–79 | signal + segment data, no bespoke brief | sequenced |
| 3 | 40–59 | none until enrichment promotes | light touch |
| — | below 40 | none | no send |

The research pass is the scarce resource. A tier is a budget decision before it is a
priority decision.

## Campaign gates

Checked before launch, not after:

| Gate | Threshold | Why |
|---|---|---|
| Audience size | **≥ 50 accounts** | below this, no reply rate means anything |
| Enrichment coverage | **≥ 80%** | gaps become generic copy, which drags the whole variant |
| Variant kill | **pause under 1% reply after 50 sends** | keeping it running costs domain reputation |

## Benchmarks

Industry reference, for reading results rather than setting targets:

| Metric | Strong | Average | Weak |
|---|---|---|---|
| Reply rate | > 5% | 2–5% | < 2% |
| Positive reply | > 3% | 1–3% | < 1% |
| Meeting rate | > 2% | 0.5–2% | < 0.5% |

**Diagnostics — read the funnel, not the total:**

| Pattern | The problem is |
|---|---|
| Low open | the subject line |
| High open, low reply | the body or the CTA |
| High reply, low meeting | the ICP — you are reaching the wrong people well |

## Sequences, not one-offs

A campaign is a series. Email-only lands roughly on touches 1, 3, 4, 6, and **most replies
come from touches 3 and 4**. A lone first touch is not a small campaign; it is an
unfinished one, and it will read as weak evidence that the angle failed.

## Segment by signal and persona

Distinct pains get distinct copy. Blending two segments to reach the audience-size gate
wastes the signal that justified the campaign — a bigger, blander audience is worse than a
smaller sharp one that waits a week for more accounts.

## "Why now" is datable

Every outreach names a specific, observable trigger with a date or an observable condition.
If the "why now" cannot be dated or pointed at, the account is not ready — monitor it.

## Verify specifics

Any factual claim about a prospect must be sourced, especially in a 1:1. **A wrong detail
reads worse than no detail**: generic copy is forgettable, but a confidently wrong fact
tells the reader you are automated and careless in the same sentence.

## Output naming

```
accounts/<slug>/outputs/YYYY-MM-DD-[type]-[name].md
accounts/<slug>/outputs/campaigns/YYYY-MM-DD-[name]/
accounts/<slug>/outputs/account-research/YYYY-MM-DD-[name].md
```

Dated, because staleness is a property you need to see without opening the file.
