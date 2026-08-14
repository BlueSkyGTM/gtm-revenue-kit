# Pain-based segmentation — the segment-agnostic targeting doctrine

**Provenance: Cannonball GTM / Doug Bell (arrival 2026-08-10, `NOTICE.md`).** Source: "Beyond the ICP: A Guide to
Pain-Based Segmentation" — Cannonball GTM / Doug Bell
(cannonballgtm.substack.com/p/beyond-the-icp-a-guide-to-pain-based). Abstracted into an
original core doc; one instrument of the open test `experiments/002-segment-definition.md`
at the bottom before applying this anywhere a firmographic-first model already operates.

> **Series note (research, 08-14):** the recorded source sits inside a moving Cannonball
> series, and the current formulation is **dual-path** — Pain-Derived Segments (this
> doc's EDP method, trailing indicators) plus Demand-Qualified Segments (leading
> indicators, "load pulling away from capacity," years ahead of the RFP). DQS is a
> *third* map type, not a variant of this one. Evidence state, corpus map, and the
> DISCO worked case: `pain-based-segmentation-RESEARCH.md`.

---

## The doctrine in one move

Traditional segmentation asks *"which customers are best for us?"* — and answers with
firmographics: size, industry, geography, stage. That is seller-centric: it finds the
companies most convenient to serve, not the prospects most desperate to buy. Pain-based
segmentation flips the fundamental question:

> **Not "who can we service, given our TAM" — "what pain can we resolve?"**

A **pain-based segment** is a group of potential buyers unified by a common, significant,
*measurable* business problem — grouped by the intensity and specificity of what they are
experiencing, not by what they look like on a firmographic filter. Two companies identical
on paper can sit in different segments; two companies nothing alike can sit in the same
one, because one metric is bleeding in both.

## Why now: signal decay

Firmographic signals are becoming commonplace and generic — every vendor sees the same
funding rounds, the same job posts, the same tech installs, at the same time. And signal
freshness cannot keep up with CRM decay: by the time a traditional signal is actioned, the
org chart it described has churned. Pain endures where structure decays — a company's
existential metric stays diagnostic long after its headcount data has gone stale. That is
the theoretical case for a pain-based system: it keys on the condition, not the census.

## The Existential Data Point (EDP)

The cornerstone of the method: for each category, identify the **one metric that separates
success from failure** — the number a business in that category cannot survive getting
wrong. (Source examples: revenue-leakage rate × gross margin in healthcare practices;
utilization below 60% in equipment rental.) The EDP is what a pain-based segment is
*defined by*; everything else about the company is circumstance.

## The three-step process

1. **Identify the EDP(s)** for the category — research work: what metric, at what
   threshold, makes the problem existential rather than annoying.
2. **Map the market on the EDP**, not on firmographics — quadrant or grid the prospects by
   where they sit against the threshold. The segment boundaries fall out of the metric.
3. **Score the segments** for pursuit order:
   `Segment ARR forecast = TAM × pain-intensity factor × conversion rate × ACV ×
   sales-efficiency factor` — pain intensity is a first-class scoring input, not a tiebreak.

## How it composes with this engine's mechanism

**The scoring mechanism does not change.** The account scoring model
(`accounts/<slug>/context/scoring-model.md`) keeps its four-dimension composite —
firmographic · technographic · organizational · signal/intent — and its decay,
bands, and gates. What this doctrine changes is **what the dimensions are fed and how
the weight sits**:

- The **signal/intent dimension is fed pain-based signals** — dated evidence that the
  EDP is breaching (leakage, utilization, churn-of-necessity events) — rather than
  generic activity signals.
- The **firmographic dimension demotes** from segment-definer to context: it no longer
  decides *who is in the market*, only how to speak to them once pain puts them there.
- `signal-library.md` gains EDP-keyed signal definitions; `icp-definition.md` becomes a
  pain map (which pains, at which thresholds) rather than a firmographic profile.

An account adopting this doctrine records the adoption in its own context files, per
track. The weights are the account's; this doc holds no numbers (swap test).

## Doctrine note — the segment-definition conflict (read before adopting)

This doctrine directly contradicts the firmographic-first assumptions carried by the
`imported` market-led workflow (`tam-campaign.md` — map the market from structure down)
and the fit-dimension ordering the scoring template defaults to. That conflict is
**queued, not resolved**: `experiments/002-segment-definition.md`. What is settled: never blend the two
segment definitions inside one campaign — a campaign's audience is drawn either from a
firmographic map or from a pain map, and says which.
