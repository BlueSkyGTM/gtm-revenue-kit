# Formal request — third edition, 2026-08-14

**From:** the construction session (branch `claude/course-extraction-account-split-lm15br`)
**To:** the Cowork second brain (E-items) and the operator (R-items)
**Standing:** transient — deleted when the queue empties.

**Closed since the second edition:** E1 (stage 1 — AMEND, both amendments applied, the
record at `motions/tam/01-mapping/EVALUATION-2026-08-14.md`; stage 2 drafted under the
unblocking) · E2 (fenton operations — clean bill; the one flag ruled by the operator
08-14: *"Fenton is a separate project. Period."* — the cross-deployment pass removed, no
exception enters law) · E3/R8 (pain-based research landed at
`motions/workflows/pain-based-segmentation-RESEARCH.md`; experiment 002 upgraded with
the evidence state and the DQS third-map note). Earlier closures: R2, R4, R6, R9.

---

## To Cowork

### E4 — Investigate the Deepline public skills set ⟵ **new, operator-ordered**

Target: [`getaero-io/gtm-eng-skills`](https://github.com/getaero-io/gtm-eng-skills) —
ten MIT-licensed Claude Code skills driving the Deepline CLI (waterfall email
enrichment, TAM building, signal discovery, job-change detection, outbound automation,
and the rest). Read the pack skill by skill and **triage each against `runtime-spec.md`
and our method**, three verdicts:

- **Absorb** — command patterns and mechanics worth taking into our execution blocks,
  with MIT attribution (`NOTICE.md` row on absorption).
- **Replace** — where our method is deeper and theirs would dilute it: their TAM
  building vs. our anti-ICP pipeline (`motions/tam/`); their signal discovery and
  job-change detection vs. our schema's why-it-matters gate and play 10; their outbound
  automation vs. our gated send wall.
- **Safely disregard** — anything that conflicts with law: numbers in core, pushes
  without a suppression gate, provider choices hardcoded where account config belongs,
  anything bypassing one-account-per-run binding.

*Fulfilled when:* a verdict-per-skill document is committed. **Nothing from the pack
enters a contract before this lands** (`runtime-spec.md` §7).

### E5 — Review `runtime-spec.md` ⟵ **new**

The runtime spec (v0) is drafted for your review — same format as E1: *stands / amend
with lines / rebuild*. The axes that matter most, in risk order: does any part of it
scaffold ahead of the operator's material; do the law translations (§3) hold to the
letter now that the 08-14 ruling hardened principle 2; is the
execution-blocks-in-contracts decision (§2) right or does it need the separate wing.
*Fulfilled when:* the verdict is committed. **Unblocks: execution blocks for stages 1–3
once the operator's inputs (below) also land.**

---

## To Ray

### R1 (continuation) — stage briefs: 2 is drafted, your deltas still shape it

`motions/tam/02-refinement/CONTEXT.md` is drafted from the skeleton + your
exclusion-hardening delta and awaits Cowork's gate. Your per-stage deltas for 3–6 (and
anything stage 2's draft missed) land whenever ready — numbers labeled proven / taught /
guess.

### R2 — the runtime inputs (from `runtime-spec.md` §6)

1. Deepline account + which providers get BYOK keys.
2. Where each deployment's SQL database lives (becomes an `estate.md` row).
3. The active deployment's **send-approval scope, named in writing** — who says yes to a
   batch.

### R3 — Michael's signal set, with the why per signal *(standing)*

### R5 — the fixed-slot template, verbatim — licensing check first *(standing)*

### R6 — the `tam/` vs `market-led/` naming one-liner *(standing, blocks nothing)*

### R7 — where Michael's course physically lives *(standing — still the only unanswered
question from the first edition)*

### R9 — delete/archive the standalone `migration-kit` repo *(standing reminder)*

### R10 — the estate inventory, on your schedule *(parked)*

---

## Sequencing

**E4 and E5 are the gates on the runtime**; stage 2's evaluation is the gate on the
pipeline. The construction session holds: applying verdicts, drafting stage 3 when its
brief content exists, execution blocks once E4+E5+R2 land, and the provenance diff
against `baseline-gtm-starter-kit`.
