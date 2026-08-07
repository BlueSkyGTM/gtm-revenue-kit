# Positioning red-team — Migration offer track (built and audited same day)

*Run 2026-07-27 per `playbooks/impact-positioning.md` step 7, against the migration offer track
built earlier today: the fenced messaging-house section, the alternatives set, the signal class,
scoring §2a/§4a, the pricing block, and the three draft variants.*

> **Independence caveat, stated up front.** The two prior audits today were run cross-model via
> `/codex`. That run **failed on an API quota limit**, so this audit is self-run by the same
> session that wrote the material. Mechanical checks (Copy Rules, word counts, price accuracy)
> are objective and reported as measured. The judgment dimensions carry an author's-own-work
> bias that a cross-model pass would not. **Re-run this audit via `/codex` when quota resets,
> before anything here is loaded** — the findings below are a floor, not a ceiling.

> *[2026-08-03: the cross-model re-run was attempted and failed the same way — the OpenAI
> account has no API credits. It stays owed; the operator adding credits is the unblock.
> Addressed today regardless: **F6** resolved (`Repriced_Bill_Confirmed` field created in
> Airtable with a re-query-at-send-time rule, `scoring-model.md` §4a) and **F7** resolved
> (`competitor-radar.md` gained the independent local bookkeeper and the dual-platform
> QuickBooks-native bookkeeper as mapped alternatives). Other findings unchanged.]*

**Verdict: the mechanical dimensions pass clean. Three real findings, one of them serious
enough that it would have shipped a promise the practice cannot currently keep.**

## Mechanical checks (objective, measured)

| Check | paid-exit | origin-knowledge | one-bill |
|---|---|---|---|
| Under 120 words | 103 ✓ | 106 ✓ | 92 ✓ |
| Exactly one CTA | 1 ✓ | **0** (see F4) | 1 ✓ |
| No percentages | ✓ | ✓ | ✓ |
| No em/en dashes in body | ✓ | ✓ | ✓ |
| No banned vocabulary | ✓ | ✓ | ✓ |
| No tool names | ✓ | ✓ | ✓ |
| No deadline framing | ✓ | ✓ | ✓ |
| Prices match the settled table | $140 / $340 / $25–$90 ✓ | n/a | n/a |

Repo linter (`repo-hygiene` step 2) over all sequence files and `web/`: **clean**.
*[2026-08-03: the `repo-hygiene` skill was deleted 2026-07-29; this pass result stands as recorded but is no longer reproducible by that method. See HANDOFF.md.]*

## Findings

### F1 — HIGH: `one-bill` promises a capability the practice will not have at test time

The variant says *"we carry the subscription ourselves"* and *"the subscription transfers
straight back to you."* Both require Fenton to be a **Xero partner** — and the motion's own
resequencing decision (debrief §4) deliberately **defers partner signup until the first real
engagement is near**, precisely to keep the principal's initial ask small. The free-transfer
promise additionally depends on engagement-letter clauses that do not exist yet.

So this variant, as drafted, would promise at test time something the practice cannot deliver.
That is the exact failure class the eligibility dimension exists to catch.

**Fix:** hold `one-bill` out of the test entirely. It becomes eligible only once partner status
and the three engagement-letter clauses (pass-through, free exit transfer, transparent
bundling) are both real. Marked in the draft file.

### F2 — HIGH: `paid-exit` quotes tier prices that are not the recipient's

The eligibility gate admits **Essentials, Plus, and Advanced** accounts, but the copy hardcodes
*"Plus moved to $140 a month, Advanced to $340."* An Essentials account (whose own increase was
$75 → $85) reads two numbers that are not theirs — which contradicts the discipline the whole
positioning rests on: **anchor on the recipient's own invoice**, never a market figure.

**Fix (either, prefer the first):** merge-field the tier line per account, so each recipient
sees only their own plan's movement (the plan tier is already in the `Products` field, so this
is a mail-merge task, not new research); or narrow the variant's predicate to Plus and Advanced
holders only and write a separate Essentials line.

### F3 — MEDIUM: `origin-knowledge` leads with a fact most recipients cannot use

The lead claim is *"payroll year to date does not transfer at all."* True, well-sourced, and
genuinely useful — **to the 283 of 862 accounts that are payroll-stacked.** For the majority it
is a fact about someone else's migration, which weakens exactly the thing the PVP standard
tests: is this worth reading if they never reply?

**Fix:** either gate the variant to `payroll-active` accounts, or reorder so the universally
applicable facts lead (chart mapping is a judgment call; integrations must be reconnected) and
payroll becomes the third sentence, present only where relevant.

### F4 — MEDIUM: `origin-knowledge` has no question-form CTA

Its close is *"Happy to look at your file and tell you what it would actually involve."* That is
a single, low-friction ask, so it satisfies the one-CTA rule in substance, but it is softer than
the other two and gives the reader nothing to answer. Deliberate or not, it should be a choice.

**Fix:** confirm intent; if a reply is wanted, end on a question.

### F5 — MEDIUM: three variants drafted, one test slot

The test design says the migration variant **replaces** the suspended `paying-more-getting-
software` cell — one slot. Three variants were drafted against it. Internal inconsistency in my
own draft.

**Fix:** name the shipper. Recommend **`paid-exit` with the F2 merge fix** — it carries the
strongest permissionless value (most recipients do not know a vendor-funded exit exists), it
applies to every eligible account, and it needs no capability the practice lacks.
`origin-knowledge` becomes round two (or a payroll-gated cell); `one-bill` waits on partner
status.

### F6 — MEDIUM: the eligibility gate is documented but not yet enforced

The per-account rule ("only after their own first bill at the new price has landed") is what
keeps this motion inside the standing no-urgency rule. It currently exists as a **predicate in
prose** — there is no Airtable field marking it, and no verification step. Until one exists, a
send could reach an account whose bill has not repriced, which makes the claim both false and
pre-emptively urgent: the exact 2026-07-25 violation, reintroduced through the side door.

**Fix:** the field must exist and be verified by re-query before any send, exactly as
`Motive_Segment` was. Stated as a hard prerequisite in the draft, not an assumption.

**On the underlying question — is "your bill went up" deadline framing in disguise?** My read:
no, when the gate holds. It is past tense, about their own invoice, with no date, no scarcity,
and no "act before." The rule bans manufactured urgency; this reports a fact that already
happened to them. But that judgment depends entirely on F6 being enforced.

### F7 — LOW: the only-statement's durable differentiator is the unbuilt part

Tested against the four documented alternatives: it survives cleanly against the free tooling
(tools move data, they do not judge accounting, verify independently, or keep books) and against
a Xero-side firm (origin knowledge is the scarce half). It does **not** structurally survive
against *another QuickBooks-native bookkeeper who also learns Xero* — the same nearest-competitor
gap the White-Label audit found this morning. The only piece that is genuinely hard to copy is
the **independent verifier and proof packet**, and it is `[PROOF GAP]` until built.

**Fix:** none needed in copy (it already claims independence rather than exclusivity), but the
strategic read is worth stating: **the verifier is not a nice-to-have, it is the differentiation.**
That argues for building it during the rehearsal rather than after the first sale.

## Top 5 fixes, ranked

1. **Hold `one-bill` from the test** until partner status and the engagement-letter clauses
   exist (F1).
2. **Merge-field the tier prices in `paid-exit`** so each recipient sees their own number (F2).
3. **Create and verify the eligibility field** before any send; no send without it (F6).
4. **Name `paid-exit` as the single test-slot variant**; re-scope the other two (F5).
5. **Gate or reorder `origin-knowledge`** so its lead claim applies to its recipients (F3).

## Dimensions passing without finding

Alternatives (four documented, each with honest strengths and a named loss condition, including
the channel-capture risk) · Beachhead (inherited from Bounce, narrowed by eligibility, rationale
explicit) · Buyer (unchanged persona; same list) · Message consistency (M1–M3 ladder up, no
orphans, both proof gaps declared) · Segment purity (no White-Label language present; the two
Bounce tracks are fenced with an explicit never-mix rule) · Source standard (the debrief carries
claim-level provenance for the price table and tooling facts) · Operational consistency (no
canonical-fact conflicts introduced; nothing live to conflict with yet).

---

*Nothing in this track is loaded, sent, or shown to a client. The principal's decision is
upstream of all of it, and this audit's own caveat — that it wants a cross-model re-run — is
upstream of loading anything.*
