# Triage — the public Deepline skills pack

*Decision by the construction session, 2026-08-14, on the operator's delegation. Source:
[`getaero-io/gtm-eng-skills`](https://github.com/getaero-io/gtm-eng-skills), MIT, read at
clone depth 1 on 08-14 — 17 skills, a meta-skill (`deepline-gtm`), ~80 provider
playbooks, and worked examples. Verdicts are per capability, not per file.*

---

## The finding that decides most of it — *corrected 2026-08-14*

**The pack's skills carry no consent discipline of their own**, and its approval gate
(`deepline-gtm` §4) is a **cost** gate: pilot one row, show the preview and expected
spend, get approval, then scale. That gate is good and worth having.

> **Correction.** This section first concluded the pack "has no consent concept anywhere"
> and that adopting its model "would leave the send wall demolished." That overstated it.
> The pack pushes into Instantly, Smartlead, and Lemlist, and those platforms ship
> unsubscribe handling and suppression natively — a pack routing into them inherits
> platform-level compliance. Reporting absence-of-word as absence-of-thing is the
> word-search failure (`foundations/failure-modes.md` §3), committed here.
>
> **The narrower claim, which holds:** the pack has no **operator-owned, account-scoped
> ledger independent of the platform**. Suppression lives wherever the sequencer keeps it,
> so changing platforms loses the record and no single file can be audited. That is a real
> reason to keep our own ledger — and a much smaller claim than the one first made.

**Cost approval and consent approval are two different gates.** Keep both; do not let
either stand in for the other.

## Absorb

| What | Why it earns entry |
|---|---|
| **Pilot → preview → approve → scale** (`--rows 0` one-row pilot, CSV preview, explicit approval, full run) | A gate that binds mechanically and is *countable*. Maps onto TAM stage 2's cheapest-tool-that-answers rule and onto every paid enrichment step. Adopt as the cost gate — **beside** the consent gate, never instead of it |
| **Companies first, then people** | Their stated discovery order, and independent confirmation of our stage split (stage 1 maps companies; stage 3 finds people). Not new to us; worth citing as convergent evidence |
| **Provider playbooks as level-3 docs** — per-provider quirks, cost, fallback, kept out of the decision layer | The shape our execution blocks should reference rather than inline. One home per provider fact |
| **Their documentation hierarchy + "no-loss rule"** (L1 decision model → L2 phase docs → L2.5 recipes → L3 provider detail; moved guidance stays canonical at its level and is linked) | This is one-home-per-fact arrived at independently, and it is ICM-compatible. Confirms the contract structure we already run |
| **Waterfall/failover command mechanics** | The actual `deepline enrich` patterns. Pure tool knowledge, no doctrine attached |

## Replace — ours is the method, theirs is the pull

| Theirs | Ours | The gap |
|---|---|---|
| `build-tam` — "source accounts and contacts from Crustdata, Dropleads, PDL" | `motions/tam/` (stages 1–2) | Theirs is stage 1 step 2 — *pick a provider and pull*. It has no map declaration, no anti-ICP, no exclusion hardening, no tiering, and no below-threshold tier. It sources a list; ours produces an artifact whose negative space is first-class |
| `writing-outreach` — a strict 4-step sequence with rationale | `foundations/pvp.md` + the fixed-slot instrument | Theirs is a third instrument arriving as a default. Adopting it would silently settle `experiments/001` |
| `deepline-gtm` "governs the entire session" | `CONTEXT.md` routes | A competing router. Deepline is a tool surface reached *from* our contracts; a tool skill that claims session governance inverts the architecture |

## Absorb-with-condition — the one that is neither

**`niche-signal-discovery`** computes Laplace-smoothed lift between Closed-Won and
Closed-Lost accounts to find differential signals (site content, job listings, tech
stack). The statistics are real and the instrument is genuinely useful — but a lifted
correlation is **not** a buying mechanism, and `signals/schema.md` admits nothing without
one.

**Verdict: absorb as a discovery instrument, never as an admission path.** It proposes
candidates; the "why it matters" is still supplied by the operator or by operation before
a record enters the library. Recorded here so a future session does not mistake a lift
score for a mechanism.

## Disregard

- **Their approval gate as a substitute for our ledger** (the finding above, as
  corrected — a narrower objection than first stated, and still a real one).
- **Provider defaults as doctrine.** The pack names preferred providers per task; those
  are account/deployment config here, never core (principle 3).
- **The install/auth boilerplate** repeated at the head of every skill. Runtime setup
  belongs in one place, not in every contract.

## What this means for `runtime-spec.md`

Nothing in the pack changes the spec's shape; two things sharpen it. §3's send-wall row
gains a companion: **the cost gate is a second, separate mechanical gate** (pilot →
preview → approve → scale) — cheap to implement, and the pack proves it works in a
Claude-driven session. And §2's execution-blocks-in-contracts decision is reinforced:
their level-3 provider playbooks are exactly what an execution block should *cite*
instead of carrying.

Absorbed patterns travel with MIT attribution (`NOTICE.md`).
