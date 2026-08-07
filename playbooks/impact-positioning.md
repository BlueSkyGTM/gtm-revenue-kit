# Playbook: IMPACT Positioning — build a buyer's full positioning set

*The six construction steps that take a new buyer from "we should sell to them" to a complete,
campaign-ready positioning set, plus the step-7 audit run against positioning that is already
settled. Mined from a commercial GTM tool suite during an evaluation whose verdict was **wire
nothing, own the methodology** — this file is the owned methodology.*

*This playbook is core. It holds no account facts: every step names the account file it fills,
and every value it needs is read from `accounts/<slug>/context/`. When a campaign's buyer is not
the account's primary ICP, that buyer is a **track** — its artifacts live in
`accounts/<slug>/context/tracks/<track-slug>/`, separate on purpose, never mixed
(`accounts/_template/context/tracks/README.md`).*

---

## Trigger

One of the following:
- A campaign targets a **buyer who is not the primary ICP** (different title, different firm
  type, different reason to buy) — run all six steps before any copy is written.
- The Pre-Campaign Checklist in `workflows/campaign-build.md` fails on "is the value prop
  differentiated" or "is the ICP tier and persona defined" — that is the positioning gate, and
  it routes here.
- The operator asks for a positioning red-team → skip to **Step 7** only.

**The rule, stated once:** a different buyer needs its own full set. An ICP file plus one persona
is two of seven steps, not a discount version of positioning. The failure this playbook prevents
is the common one: a campaign sources and scores hundreds of contacts for a new buyer before that
buyer's positioning exists, and every downstream artifact inherits the gap.

---

## The six construction steps

Run in order. Each step's output is a section or file under `accounts/<slug>/context/`; each
later step reads the earlier ones. Do not skip forward: a message crafted before value is
pinpointed is a slogan.

Where a step names a file below, a **track** writes the same artifact under
`accounts/<slug>/context/tracks/<track-slug>/` instead, and states at the top of the file what it
overrides.

### Step 1 — Map alternatives

**Question:** if this buyer never hears of us, what do they actually do?

List every real alternative **including the status quo** ("does nothing / keeps doing it
in-house") — most competitor sets omit the one option that wins most deals. For each: what it
costs, where it genuinely wins, where it genuinely loses, and what event makes a buyer leave it.

**Fills:** `accounts/<slug>/context/competitor-radar.md`. A different buyer almost always has a
different alternative set; reusing the primary radar for a new buyer is the most common way this
step is silently faked.

### Step 2 — Anchor market (beachhead)

**Question:** of everyone who *could* buy, which narrow segment do we win **first**, given real
constraints (capacity, credibility, proof points on hand)?

Choose one beachhead segment and write down *why it loses least* against the step-1 alternatives.
The choice is constraint-driven, not size-driven: an account picks the segment it can actually
serve today, not the biggest addressable market. Name what is deliberately deferred.

**Fills:** the *Core Positioning Statement* and the market-choice rationale in
`accounts/<slug>/context/positioning.md`.

### Step 3 — Identify champions

**Question:** who inside the buying account feels the pain first and can say yes?

Write the persona: title(s), decision role, what a good and a bad month look like, how they buy,
what gets their attention, what gets ignored. If a committee decides, map who champions vs. who
signs.

**Fills:** `accounts/<slug>/context/personas/<persona>.md`, using the shape in
`accounts/<slug>/context/personas/template.md`. One file per persona, tagged with the campaign it
belongs to.

### Step 4 — Pinpoint value

**Question:** what can this buyer get from us that they cannot get from any step-1 alternative —
stated as *their* outcome, not our feature?

Draft the "only statement": *For [beachhead], we are the only [category] that [differentiated
value], unlike [leading alternative], which [its structural limit].* Every clause must trace to a
step-1 fact or a verifiable credential. Value claims with no evidence get an explicit
`[PROOF GAP]` marker, never silent omission.

**Fills:** the *Value Pillars* of `accounts/<slug>/context/positioning.md`.

### Step 5 — Craft message

**Question:** how does the value survive translation into words a skeptical buyer reads?

Build the messaging house: one value proposition sentence, three (or fewer) pillars, checkable
proof under each, known gaps recorded rather than papered over. Run the ladder-up check: every
pillar must prove the value proposition, and no pillar is an orphan.

**Fills:** `accounts/<slug>/context/messaging-house.md` — a track writes the same artifact as
`accounts/<slug>/context/tracks/<track-slug>/messaging.md`.

### Step 6 — Translate execution

**Question:** does every surface say the same thing at its own length?

Project the house per channel: hero line, email angles, call opener, one-pager. One position, N
renderings — generated *from* the house, never written fresh per channel. That single-source
pattern is the point: a generic sequence generator that writes copy without reading the house is
firewalled out of the copy path, because it produces renderings that no longer share a position.
Message match is testable: a lead who clicks an angle must land on the same claim.

**Fills:** the *Per-channel projection* table of `accounts/<slug>/context/messaging-house.md`.
Channel assets in `accounts/<slug>/outputs/` are cut from that table.

---

## Step 7 — The audit checklist (red-team settled positioning)

Run against positioning that is **already settled** — pre-launch, after a pivot, or on a fixed
review cadence. Two different things, kept straight: a **dated audit run must exist** for a set
to be complete (artifact 7 below — the campaign gate checks its existence), but the audit's
**findings never block by themselves** — they go to the operator, who decides what ships.

Mechanism: run the audit with a reviewer who did not write the positioning — a different model,
or a different person. A red-team by the author is a proofread.

For the buyer's positioning set, verify:

- [ ] **Alternatives** — the competitor set includes the status quo, and each battlecard names
      where the alternative *genuinely wins* (a radar with no honest weaknesses is marketing,
      not intelligence)
- [ ] **Beachhead** — a narrow first segment is named, with constraint-driven rationale;
      "everyone who uses X" is not a beachhead
- [ ] **Buyer** — the champion persona exists as a file, and titles on the actual contact list
      match it
- [ ] **Differentiated value** — the only-statement survives a swap against each named
      alternative (would the claim still be true if a competitor said it?)
- [ ] **Message consistency** — pillars ladder up to the value prop; no orphan pillar, no orphan
      proof point
- [ ] **Channel translation** — every live surface (site, sequences, call track) renders the same
      pillars; message match holds from click to landing
- [ ] **Evidence quality** — every proof point is sourced or marked `[PROOF GAP]` /
      `[inferred]`; no unverified number appears in any outbound surface (the account's copy
      rules in `accounts/<slug>/brand/voice.md`, enforced by `tools/lint_copy.py`)
- [ ] **Segment purity** — no copy, competitor, or persona from a *different* buyer's set has
      leaked into this one (the two-set rule: never mix, and never load two tracks in one
      session)
- [ ] **Per-claim eligibility** — every record the campaign will touch is factually eligible for
      every claim it will receive (tenure, incumbent product, motive) — a claim that is false for
      a subset is a suppression rule waiting to be written
- [ ] **Operational consistency** — phone numbers, URLs, CTA destinations, and offer names are
      identical across every surface (a mismatch on a conversion-critical fact is a silent leak)
- [ ] **Change-control drift** — every downstream artifact was regenerated after the most recent
      positioning decision (name the decision dates and diff the artifact dates)
- [ ] **Source standard** — "sourced" means claim + source + access date, not a generic sources
      paragraph at the bottom of the file

Findings land in
`accounts/<slug>/outputs/audits/YYYY-MM-DD-positioning-redteam-<buyer>.md`. Each finding names
the file it faults and the fix. The operator decides what ships.

---

## Definition of done

A buyer's positioning set is complete when all seven artifacts exist and cross-reference. Paths
below are relative to `accounts/<slug>/`; a track writes items 1, 2, 4, 5, and 6 under
`accounts/<slug>/context/tracks/<track-slug>/` instead.

| # | Artifact | Home |
|---|---|---|
| 1 | Alternative map / battlecards | `accounts/<slug>/context/competitor-radar.md` |
| 2 | Beachhead + core statement | `accounts/<slug>/context/positioning.md` |
| 3 | Champion persona(s) | `accounts/<slug>/context/personas/` |
| 4 | Value pillars w/ proof or `[PROOF GAP]` | `accounts/<slug>/context/positioning.md` |
| 5 | Messaging house | `accounts/<slug>/context/messaging-house.md` |
| 6 | Per-channel projection | `accounts/<slug>/context/messaging-house.md` → assets in `outputs/` |
| 7 | A dated audit run | `outputs/audits/` |

Anything less, and `workflows/campaign-build.md` fails the campaign back here before Phase 1.
