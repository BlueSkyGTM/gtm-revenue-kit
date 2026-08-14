# Runtime spec — the kit as the GTM motion runtime, v0

*Status: SPEC ONLY — nothing is wired, no keys exist in any repo, no scaffolding until
the operator supplies the runtime inputs (§6). Provenance: the
operator's direction (08-13 disclosure, 08-14 conversation — "instead of a string of API
integrations, use Deepline to turn the kit into the GTM motion runtime; multiple calls
in one prompt"); Deepline's surface verified against its public docs 08-13/14; design by
the construction session. The operator is the gate on it.*

---

## 1. Thesis — the ICM structure IS the runtime program

The kit does not grow an orchestration framework. The runtime is three existing things
composed:

1. **The method** — stage and skill contracts (`motions/`), already task-routed, already
   gated. They say *what* a motion does and *when a human reads before it proceeds*.
2. **The executor** — a Claude session (later: unattended runs), which already executes
   contracts by task routing.
3. **The tool surface** — the Deepline CLI: one command surface over ~87 GTM
   integrations (enrichment waterfalls with provider failover, validation, dedupe, CRM
   writes, sequencer pushes), BYOK, every call writing to a SQL database the deployment
   owns.

A motion becomes executable when its contract carries an **execution block** — the
Deepline commands that perform the step — beside the method prose. Claude reads the
contract, runs the block, and the human gates stay exactly where the contracts put them.
Same work, same tools, different execution: the pattern already proven on the
migration kit.

## 2. The design decision, and its reversal condition

**Execution blocks live inside the stage/skill contracts**, not in a separate `runtime/`
wing. Grounds: one home per fact — a stage's method and its
execution are the same fact at two altitudes, and a parallel runtime tree would drift
from the contracts the way every parallel structure drifts. The alternative (a
`runtime/` wing holding motion scripts that cite the contracts) is cleaner only if
execution blocks grow beyond what a contract can carry — revisit then, not before.

## 3. The laws, translated (all already on the record)

| Law | Runtime form |
|---|---|
| Account named first | **The account binds once per run** — the run starts by binding one account's config and cannot touch another's data afterward (the ledger-server realm pattern: wrong-account execution impossible by shape, not procedure) |
| Values live in the account (principle 3) | BYOK provider keys, the SQL database DSN, caps, and provider choices are **account/deployment config** — env or config outside git, never core, never the repo |
| Raw contact data never in git | **The people live in the owned SQL database** (Deepline's write-through). Git keeps method, config shape, and state summaries — never rows |
| The send wall (estate doctrine) | **A mechanical gate in front of every sequencer push**: the suppression check runs as a query against the account's ledger + declared rosters *in the runtime*, caps enforced *in the runtime*, and a **named approval scope** — who says yes to a batch, recorded per account — checked before send. A push path without these checks is not wired; it is torn open |
| Spending a finite resource (`chain-of-operations.md` §constraints) | **A second, separate gate on cost:** pilot one row → show the preview and expected spend → explicit approval → full run. Absorbed from the public skills pack, which proves it works in a Claude-driven session (`decisions/2026-08-14-deepline-skills-triage.md`). It is *not* the consent gate and never substitutes for it — the pack ships this one and no consent layer at all |
| Suppression per-account, append-only (principle 5) | The ledger stays the account's file, append-only; the runtime *reads* it into the gate query, never merges ledgers, never writes one |
| Accounts never read each other (principle 2, operator-affirmed 08-14) | One account per run binding makes cross-account reads structurally impossible, not just forbidden |
| Known-why admission + waste naming | An execution block enters a contract only with the method it executes — no orphan automation. The block inherits the contract's waste claim |

## 4. First executable motion

**The TAM pipeline, stages 1–3** (map → refine → find-people-&-enrich), for the active
deployment's own account (`estate.md` names it): read-only against the tool estate — no
sequencer pushes — and its output is the first real TAM artifact, which the pipeline
build needs anyway. Enrichment waterfall, validation, and classification passes are
exactly Deepline's home turf, and the anti-ICP columns land in the owned database from
day one.

Sends (stage 6) are explicitly **out of the first motion**: they wait for the approval
scope to be named in writing and the gate query to exist and be tested against the
ledger. The two warming addresses lose nothing by this wait.

## 5. What the runtime is NOT

- Not a daemon: runs are invoked, complete, and stop. Unattended scheduling is a later
  decision with its own gate design.
- Not a data platform: the SQL database is the deployment's; the kit specifies the
  minimal schema the motions need (map table with anti-ICP and suppression columns,
  enrichment results, send log) and owns nothing else.
- Not a replacement for the deployments' minimal manual seams — a shelved deployment's
  declared integrations stay as declared; the runtime is for deployments running motions.

## 6. Open inputs (the operator's, before any wiring)

1. Deepline account + which providers get keys (BYOK — the operator's bill either way).
2. Where each deployment's SQL database lives (becomes an `estate.md` row).
3. The active deployment's **send-approval scope, named in writing** — who says yes to
   a batch.
4. *(Closed 08-14: the public-pack triage is done — §7. Nothing else gates the spec but
   items 1–3.)*

## 7. Relationship to the public skills set — triaged 2026-08-14

The MIT skills pack ([getaero-io/gtm-eng-skills](https://github.com/getaero-io/gtm-eng-skills))
was read and triaged; the record with the evidence is
`decisions/2026-08-14-deepline-skills-triage.md`. The short form:

- **Absorbed:** the pilot→preview→approve→scale cost gate (now §3's second gate);
  companies-before-people discovery order; provider playbooks as level-3 docs an
  execution block cites rather than carries; their documentation hierarchy and no-loss
  rule, which are one-home-per-fact arrived at independently.
- **Replaced by our method:** their TAM building (a provider pull, no map declaration, no
  anti-ICP, no tiering), their outreach sequence default (it would silently settle
  `experiments/001`), and their meta-skill's claim to govern the session (our contracts
  route; Deepline is a tool surface).
- **Absorbed with a condition:** their won/lost lift analysis is a genuine *discovery*
  instrument, never an admission path — a lift score is not a buying mechanism, and
  `signals/schema.md` still requires one.
- **Disregarded:** their approval gate as a *send* gate. The pack has no suppression,
  opt-out, or consent concept anywhere; adopting its gate model would leave the send wall
  demolished while the session felt governed.

Absorbed patterns travel with MIT attribution (`NOTICE.md`).
