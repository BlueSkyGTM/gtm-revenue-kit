# Evaluation — the kit walked cold, before publication

*Evaluation by the construction session, 2026-08-22, run as an independent pass with no memory of
the work it was checking. Method: full reference extraction — 1,106 path-like citations across 96
non-archive `.md` files — resolved source-relative with `<slug>`→`_template` and basename fallback,
plus heading-level validation of every `file.md §section` citation, plus contract checks on all six
skills against the shelf contract in `motions/skills/CONTEXT.md`. Trigger: the repo is about to be
published, and a claim that is only true from the inside is not true. **Findings are recorded, not
all fixed** — what was corrected is marked; what stands open is a Room-for-growth item.*

---

## The finding that matters most

**The pass that wrote the README introduced three false claims into it, and the walk test is what
caught them.** That is the instrument working on its owner, which is the only way a diagnostic
earns the right to be pointed at anyone else (`rulings.md` 2026-08-21, the two-arm test). A
detector that flatters its owner is not a detector.

| Introduced error | Reality | Status |
|---|---|---|
| `decisions/` holds "6 records" | Five, plus `CONTEXT.md` — which is the wing contract, not a record, as `decisions/CONTEXT.md` says outright | **Corrected.** This record is the sixth, so the count is now true by fact rather than by miscount |
| "25 inherited files" audited | 15 plays + 4 channels + skeleton + enrichment + 5 dormant = **26**. The audit miscounted its own stated scope, in five places, and `NOTICE.md` inherited the error | **Corrected** in both files |
| `accounts/_template/` is "Complete" | `brand/README.md` says "Status: empty slots"; `voice.md`, `offer-map.md` and `brand-psychology.md` do not exist, and `setup/SKILL.md` says to leave `brand/` alone | **Corrected** to name the empty slots |

Two further defects in the same pass, both corrected: the README omitted `playbooks/` (4) and
`dormant/` (5) from the motions inventory, and `CLAUDE.md` still carried the pre-rename title and
folder-map root while `estate.md` recorded the rename.

## Corrected in this pass — defects older than the README work

- **Two transposed principle citations, exactly swapped.** `accounts/_template/optouts.md` cited
  §4 (one home per fact) as the authority for suppression being account-scoped; `brand/README.md`
  cited §5 (suppression) as the authority for one-home-per-fact. The opt-out ledger — the file
  `CLAUDE.md` calls the legal floor — cited the wrong rule for its own existence. Now §5 and §4
  respectively.
- **Ten play files were not valid UTF-8.** A bare latin-1 `0xa7` where a UTF-8 `§` belonged, 15
  occurrences, inside section citations like `scoring-model.md §8`. They would have mangled in any
  strict renderer, GitHub included, in a repo about to be public. Repaired at byte level with the
  substitution proved reversible — **an encoding repair, not a content edit; no mechanism was
  touched**, which the fidelity ruling requires.
- **A stale section anchor** in the 08-21 Duality ruling, pointing at a heading name that no longer
  matched.

## Open — recorded, not fixed

These need either the operator or more context than a reference scan has. They are the substance
of the README's `## Room for growth`.

- **The copy linter has no rules file to gate against.** `tools/CONTEXT.md` states the linter
  checks copy against `accounts/<slug>/brand/voice.md`; `setup/SKILL.md` writes nine context files
  and explicitly leaves `brand/` alone. **No account this kit can create satisfies the gate** the
  router calls "a gate, not a review." Twelve references across the repo treat the three `brand/`
  slots as live files. Either `setup` grows the slots, or the linter's contract names what it
  actually reads today.
- **The router and a skill disagree on where output lands.** Three router statements send
  account-research output to `outputs/account-research/`; the skill's own contract writes flat to
  `outputs/[date]-[account]-research.md`, and the shipped worked example follows the skill. The
  skill contract is authoritative on its own output; the router rows are the ones to correct.
- **Two skills violate their shelf contract.** `motions/skills/CONTEXT.md` requires every
  `SKILL.md` to carry an `## Inputs` block naming exactly the files it reads. `setup/` has none;
  `weekly-update/` has `## What Claude Reads` instead. That file's own rule — the rule file wins
  and the skill file gets fixed — decides the direction.
- **Four of six skills carry no step-level time budget**, against `task-craft.md` rule 5. Their
  header durations are unverifiable rather than wrong.
- **`playbooks/` and `dormant/` are unreachable from the task router.** Nine files, findable only
  by already knowing they exist. `CLAUDE.md`'s folder map names them; `CONTEXT.md` has no row.
- **Four dead references:** `tam-campaign.md` (cited by `pain-based-segmentation.md`, exists
  nowhere), `.env.example` (cited by `sync/CONTEXT.md`, never shipped), a deployment-only path
  reached from a core evaluation file, and an `offer-map` citation missing its extension.
- **Fourteen loose-but-resolvable anchors** — `§taxonomy`, `§copy`, `§mapping`, `§Tier` — citing
  table rows or paraphrased headings rather than exact ones. A human resolves them; a string match
  does not.

## What this changes

**It supplies the README's gap list.** Every open item above belongs in `## Room for growth`,
stated rather than discovered by a reader.

**It does not change any mechanism.** The only files under `motions/` touched were the ten
encoding repairs, and those changed bytes, not method.

**It sets a precedent worth keeping:** run the cold walk before publishing, not after. Every error
in the first table was invisible from inside the work that made it.

## What would reverse this

- **The "corrected" rows** reverse if a later pass reintroduces a count — which is the argument for
  deriving counts by script at commit time rather than typing them.
- **The linter finding** closes the moment either `setup` writes `brand/voice.md` or the linter's
  contract is rewritten to name a file that exists. Until one happens, the gate is decorative, and
  a decorative gate is worse than a declared absence.
- **The UTF-8 repair** would reverse if an editor without an encoding declaration writes to those
  files again. A `.gitattributes` or an encoding check in the swap-test grep would prevent it;
  neither exists yet.
