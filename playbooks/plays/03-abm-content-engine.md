# Play: ABM Content Engine

A generation pipeline that turns a stakeholder map into persona-specific sales enablement
content on demand, collapsing the request-write-approve-return loop between sellers and the
content team from days to minutes. The "signal" is internal: a live multi-stakeholder deal
needs materials that speak to each decision-maker's own incentives. It reaches the buying
committee of an active opportunity — the one audience where generic content measurably
stalls revenue.

---

## The signal

**What fires:** an opportunity at a large account reaches the stage where more than one
stakeholder must say yes — and the personas differ enough (finance, operations, technical,
executive) that one deck cannot serve them all. The trigger is a seller's request tied to a
named deal, not a market event.

**Where it comes from:** the CRM's opportunity stage plus the seller's discovery notes. If
the account also runs buyer-group mapping (`playbooks/dormant/buyer-group-mapping.md`), that
map is this play's input.

**Decay:** tied to the deal clock. Content that arrives after the internal review meeting it
was built for has zero value regardless of quality. The account's `signal-library.md` does
not usually carry this as a scored row — it is a deal-stage trigger, not a prospecting
signal — but an account that wants stalled-deal detection can record "multi-stakeholder deal
with no per-persona materials" as an internal signal with the recency window its
`scoring-model.md` sets.

---

## Why it works

Committee deals stall in the rooms the seller is not in. Each stakeholder weighs the purchase
against their own scoreboard — cost for finance, risk for IT, workload for operations — and a
single generic asset forces every one of them to translate the pitch into their own terms.
Most will not bother. Content built per persona does the translation for them, which is what
"aligning incentives" actually means in practice.

The mechanism that makes automation viable: enablement content is structural. A case study, a
one-pager, an objection memo each follow a stable shape that can be expressed as a template
over two kinds of input — standing inputs (brand voice, positioning, proof library) and
per-deal inputs (this company, these stakeholders, these pains). Stable structure plus
variable inputs is exactly what a generation pipeline is good at.

The limit: generated content is only as true as the proof library behind it. A pipeline that
invents claims produces polished damage. Every factual claim must trace to the account's
sourced materials — the "verify specifics" standard in `docs/standards.md` applies to
enablement content exactly as it applies to outbound.

---

## The build

1. **Codify the standing inputs.** The account's `context/positioning.md`,
   `context/messaging-house.md`, `brand/voice.md`, and a case-study/proof library live as
   files the generator reads every run. This is the single-source pattern from
   `playbooks/impact-positioning.md` — the engine renders *from* the house, never freelances.
2. **Capture the per-deal inputs.** The seller supplies the company, the stakeholders (or
   their profiles), and the problems surfaced in discovery — a fixed short intake, the same
   questions every time. Anything not asked for is not used.
3. **Map stakeholders to pains.** For each stakeholder, an agentic generation setup (a
   Claude-based pipeline or similar) matches persona to pain to the proof assets that
   address it, using the account's `context/personas/` as the frame. Unknown personas get
   flagged for a human, not guessed.
4. **Generate against templates.** Each content type has a fixed structure; the pipeline
   fills it per stakeholder. Claims must quote the proof library or carry an explicit gap
   marker — the `[PROOF GAP]` convention from `playbooks/impact-positioning.md`.
5. **Human review, repositioned.** Editors stop being the bottleneck between draft and
   seller and become reviewers of a finished draft — the review step shrinks; it does not
   disappear. Nothing generated reaches a buyer unreviewed.
6. **Deliver and log.** Output lands in the deal's folder under
   `accounts/<slug>/outputs/`, dated per the naming standard, so the next similar deal can
   reuse the structure (never the company-specific content).

---

## The message frame

The frame is per-stakeholder translation: each asset opens inside *that stakeholder's*
scoreboard — the metric they are judged on — connects the identified pain to that metric,
and then shows evidence from a comparable situation. The seller's pitch appears only as the
resolution of the stakeholder's own problem, never as the opening. The PVP standard from
`docs/standards.md` transfers cleanly: strip the product and the asset should still teach
the stakeholder something about their own operation worth forwarding to a colleague.

---

## Measurement

- Turnaround: request-to-usable-asset time, versus the pre-pipeline baseline
- Utilization: share of generated assets sellers actually put in front of buyers (unused
  output means the intake or the quality is wrong)
- Deal effect: stage-conversion and stall rates on committee deals with per-persona
  materials versus without — the only measure that justifies the play
- Review burden: editor time per asset, which should fall without the rejection rate rising
- Content produced per head on the content team, versus baseline

---

## When NOT to run it

- **Single-stakeholder sales.** A one-decider deal needs one good asset, not an engine.
- **No proof library.** With nothing sourced to cite, the pipeline can only generate
  assertion. Build the case files first; the engine amplifies what exists.
- **Positioning unsettled.** If `context/positioning.md` and the messaging house are not
  stable, the engine mass-produces drift. Run `playbooks/impact-positioning.md` to
  completion first.
- **As a replacement for discovery.** The pipeline renders what the seller learned; it
  cannot learn for them. Garbage intake produces confident, personalized garbage.
