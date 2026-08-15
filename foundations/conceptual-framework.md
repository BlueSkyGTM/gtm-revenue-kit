# The conceptual framework — the eight pillars, made into tools

*Provenance: the pillars are PRSC Whitley's Eight Pillars of Go-To-Market Systems — the
same eight stated verbatim in `revenue-engineering.md` §The laws (one home; this file
never restates them). The tool form is the operator's design (08-14), on the FASB
pattern: when the codification fails to recognize a case, the practitioner derives the
treatment from the conceptual framework — the principles made into tools. The pillars
sit in the GTM-engineering lineage, which revenue engineering contains — interchangeable
at the frame level per the definition; no contradiction. Operator-ordered.*

**Load this file when** the method files are silent on your case, or when you must judge
whether an output is *good* — not merely whether it breaks a rule. The guardrails
(`principles.md`, `failure-modes.md`) catch what is wrong; this file is how the kit says
what is right.

## The pattern, stated once

The method files — skills, plays, stages, workflows — are the codification: the official
treatment for known cases. When a case has no treatment, a session does not improvise
from nothing and does not stall. It derives one, the way an accountant derives a
grey-area filing from the framework behind GAAP. The derivation is written down, cites
its pillars, and can be argued with.

## The judgment protocol

1. **Name the pillar(s) the thing serves — and the subsystem that embodies each.** The
   rung-4 map (`chain-of-operations.md` §The subsystem map) is the pillars embodied:
   Targeting, Offer, Channel, Intake, Sales process, Records, Follow-up, Feedback.
   Naming the pillar places the judgment; naming the subsystem places the fix. What can
   name neither is mis-filed or a gap — both are findings.
2. **Derive what each named pillar demands of it** — the tools below.
3. **Check the guardrails.** The framework decides *within* the hard lines, never over
   them: no account named in core, no number outside the account, no send without
   suppression, nothing enters core without its why.
4. **Write the derivation down as the drafter's rendering, pillar chain shown.**
   Reasoning generated here is inspectable or it is nothing — the next session must be
   able to argue with it, not inherit it as fact.

## The eight pillars, tooled

Per pillar: the demand · the question that generates reasoning when method is silent ·
what good looks like, pointed at its home. Criteria marked **(r)** are the drafter's
rendering — argue with them.

**1. Identify** — know who the buyer is, completely, before spending on anyone.
*When method is silent:* which buyers does this help find or disqualify — and would a
stranger holding the artifact reach the same list?
*Good looks like:* exclusion rules that bind (`motions/tam/BRIEF.md` — a rule that never
rejects anyone is decoration) · mapped broad, filtered later
(`motions/tam/01-mapping/CONTEXT.md`) · the negative space named on the artifact, not
implied · **(r)** an identify output you cannot audit is a mood, not a map.

**2. Offer** — present something the buyer's pain actually prices.
*When method is silent:* which named pain does the sellable thing resolve, and is that
stated before volume is spent?
*Good looks like:* the pain named and the offer mapped to it (under a pain map,
`motions/workflows/pain-based-segmentation.md`; under either map, the account's
positioning file) · positioning decided before sends scale (waste row 2,
`revenue-engineering.md` §taxonomy).

**3. Reach** — get in front of the buyer where they actually are, welcome.
*When method is silent:* would this touch land — and would the buyer be glad it did?
*Good looks like:* the declared first-touch instrument's own test passes — PVP's
strip-the-CTA (`pvp.md`) or the fixed-slot discipline (`motions/tam/skeleton.md` §copy)
— never blended · the why-now is datable (`pvp.md`) · deliverability treated as capital
(`motions/playbooks/deliverability-and-warmup.md`).

**4. Capture** — take interest the moment it shows, at the speed it decays.
*When method is silent:* if this works, who catches the response, in what window, with
what next step?
*Good looks like:* speed-to-lead treated as a capacity constraint, not a virtue
(`chain-of-operations.md` §constraints) · every reply classified and routed, none parked
(`motions/skills/reply-handling/SKILL.md`).

**5. Move** — advance the buyer with effort matched to their worth.
*When method is silent:* what does this cost per account, and does the tier justify it?
*Good looks like:* tier honored as a budget decision (`lexicon.md` §Tier) · sequences,
not one-offs (waste row 7) · **(r)** every advance has a named next step with a date,
or it is drift.

**6. Retain (data)** — keep what the operation learns where it can be found again.
*When method is silent:* where does this fact live, and will a stranger find it from
the router?
*Good looks like:* one home per fact (`principles.md` §4) · outputs dated, never
rewritten to mean something else (`principles.md` §Load discipline) · **(r)** a fact
you must remember a conversation to find is not retained.

**7. Follow up** — no warm thread goes cold by neglect.
*When method is silent:* who touches this next, when, and does suppression clear it?
*Good looks like:* suppression checked before every touch (`principles.md` §5) · warm
replies sequenced, not left to memory (`motions/skills/reply-handling/SKILL.md`) ·
**(r)** "circle back" without an owner and a date is follow-up waste already happening.

**8. Learn** — results rewrite the model, or the system only repeats.
*When method is silent:* what would this run teach, and where does the lesson land?
*Good looks like:* results re-enter the scoring model and the signal library (waste
row 8; the flywheel, `chain-of-operations.md` §Rung 3) · evaluations recorded beside
the thing evaluated (the stage-evaluation gate, `rulings.md`) · **(r)** a run that
updated no file taught nothing on the record, whatever it taught in someone's head.

## The overall test

An output is good when the pillar it serves can hand a clean input to the next pillar.
Quality is the seam working; the waste taxonomy (`revenue-engineering.md` §taxonomy) is
this same test's negative image — one names the flow, the other names the leak.

The eight are standing, not sequential: every account has all eight problems at once,
and declares what serves each (`accounts/_template/ACCOUNT.md` §Pillar coverage).
Judging any output starts with which of the eight it claims to serve.
