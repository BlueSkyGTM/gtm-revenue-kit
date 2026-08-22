# Notice — provenance and attribution

## Upstream

This repository began as a clone of **[gtm-starter-kit](https://github.com/KarlRaf/gtm-starter-kit)**,
built by [The Revenue Architects](https://www.the-revenue-architects.com) and released
under the **MIT License** (stated at `README.md` in the upstream repo, License section).

The pristine upstream state is preserved in this repo's git history at tag
**`baseline-gtm-starter-kit`** (upstream commit `735b256`). Everything after that tag is
this project's own work. There is no tracked remote — this is a fork-and-diverge, not a
synced fork, and nothing here waits on upstream.

MIT permits use, modification, and commercial distribution provided the copyright notice
and permission notice travel with the work. Retain this file, and retain any upstream
`LICENSE` file, in any distribution of this repo or a product derived from it.

> **Open item:** the upstream repo states MIT in its README but ships no `LICENSE` file,
> so there is no copyright line to reproduce verbatim. Before commercial distribution,
> confirm the intended copyright holder with the upstream author and add a proper
> `LICENSE` file here. Recorded rather than assumed.

## Second lineage — the vendored engine

Independently of the clone above, GTM material came by a second path: the same upstream
kit was scaffolded into a private repo (`BlueSkyGTM/fb-gtm-kit`, archived 2026-07-27),
then vendored into `fenton-bookkeeping-os/workspaces/practice/`, where it was extended in
use. That extension history is recorded in this repo's git history — superseded material is
retained there rather than in the working tree.

Both paths trace to the same MIT-licensed origin. Account content is the operator's own
work product and carries no upstream claim.

## Michael's coursework

The signal-play library (`motions/plays/`, all 15), the channel playbooks
(`motions/channels/`, all 4), the TAM pipeline skeleton (`motions/tam/skeleton.md`), and
`motions/workflows/enrichment-techniques.md` derive from coursework by **Michael**,
curated and licensed by the operator.

**What was done: the plays were compiled into executable instruments.** The source is
coursework, written to be read by a person who then remembers how to apply it. What ships here
is the same method expressed as software whose runtime is the filesystem. All fifteen carry an
identical contract: the signal, why it works, the message frame, the build, the measurement,
and a **When NOT to run it** guard. Thirteen fire on a trigger they declare themselves, with its
data source and decay window; the remaining two are activated by the library rather than by an
outside event, one building the list the others fire against and one being the send channel
they route through. Numbers are
parameterised out to the tenant, so the same instrument serves any account. Activation is a declared condition against the account's signal library rather than a
human deciding it is time, and the suppression check is a precondition that runs before the
side effect.

That is the contribution, and it is a translation rather than an improvement. The library was
fifteen documents somebody had to hold the wiring for; it is now fifteen instruments that fire
on conditions and compose with the scoring model, the channels, and the gates.

**Why the mechanisms stay faithful.** A translation that changes semantics is a broken
translation. Keeping each mechanism exactly as taught is the correctness property of the
compilation step, not deference to the source, which is why extensive restructuring and strict
fidelity are not in tension. A second reason holds independently: this kit has run no
campaigns, so there is no evidence on which to claim an inherited mechanism has been improved.
That half is revisited when a campaign produces results, which is what `experiments/` exists
to generate. **[operator ruling, 2026-08-21; rationale extended 2026-08-22]**

**What else changed, and what did not.** Voice stripped, abstracted to method 2026-08-08,
every number moved out to the account template. The curated set is not used in its entirety.
The operator's own TAM framework replaces the skeleton stage by stage as each is briefed,
which is replacement rather than alteration of what remains.

**Status, checked 2026-08-22 `[V]`.** All 26 inherited files were audited against the whole of
`foundations/`, not just the eight functions
(`decisions/2026-08-22-inherited-material-retention-audit.md`). Result: clean on the swap test,
on one-home-per-fact, and on values-live-in-the-account — zero figures, in digits or words,
across the set. One systemic gap: no instrument yet declares which of the eight functions it
serves, a rule written after this material landed. Nothing was dropped.

Reasoning, examples, and attribution travel with future revisions rather than being stripped —
that is a standing rule of this reconstruction.

## Pain-based segmentation

`motions/workflows/pain-based-segmentation.md` abstracts a doctrine from **Cannonball
GTM / Doug Bell** (arrival 2026-08-10). It is one instrument of the open test in
`experiments/002-segment-definition.md`.

## The role definition

`foundations/revenue-engineering.md`'s definition tracks **Jake Bivens, "Rise of the
Revenue Engineer (vs. GTM Engineer)"** (QC Growth, 13 Jan 2026) item for item; Bivens in
turn credits Benjamin Reed (RevyOps). Compared against **Matt McDonagh** (Mastering
Revenue Operations, 18 Apr 2024, partially paywalled) and **Doug Bell** (Cannonball GTM,
31 Jan 2026) in `foundations/revenue-engineering-SOURCES.md` — an operator-synthesized
comparative briefing, since the originals are unreachable from this session.

## The eight functions (revenue engineering)

The eight-verb definition quoted verbatim in `foundations/revenue-engineering.md` is
from **PRSC Whitley, "A Rough Start Guide to Building a Go-To-Market System"** —
operator-designated as the source of the laws. Quotation with attribution; the
surrounding derivation is the operator's and the second brain's.

## The van der Kooij / Winning by Design books

Two books the operator holds and is reading, both credited to **Jacco van der Kooij
with Winning by Design** (the firm is a co-credited author on the covers —
**verified 2026-08-15 from publisher cover credits**, after the reference was found in
this repo inherited and unchecked):

- **"Revenue Architecture"** — the discipline the ladder's rung 2 is named for.
  `foundations/revenue-architecture.md` holds the construction session's rendering of
  its published framework, marked `[R]` throughout, superseded line by line by the
  operator's own reading.
- **"The SaaS Sales Method: Sales as a Science"** (Sales Blueprints book 1, with
  Fernando Pizarro, Dominique Levin, and Dan Smith) — `foundations/sales-method.md`,
  abstracted from the two pages the operator supplied. The **bowtie** carried in
  `foundations/chain-of-operations.md` is this book's six-stage model — held in the
  kit rather than adopted, and attributed regardless of adoption status.

The **flywheel**'s general form traces to Jim Collins' popularization; the kit adopts
its revenue-specific rendering. Framework names and structure with attribution; **no
text from either book is reproduced** — the method is abstracted, the stages are
named, quoted fragments are short and attributed.

## Runtime patterns

Patterns absorbed from **[getaero-io/gtm-eng-skills](https://github.com/getaero-io/gtm-eng-skills)**
(Deepline, MIT License) into `runtime-spec.md`: the pilot→preview→approve→scale cost
gate, the companies-before-people discovery order, and the level-3 provider-playbook
pattern. Patterns and structure only — no code or text is carried. What was declined, and
why, is recorded in `decisions/2026-08-14-deepline-skills-triage.md`.

## Signal schema skeleton

The four-dimension signal decomposition and per-signal field anatomy in
`signals/schema.md` are adapted from
**[icp-intelligence-mcp](https://github.com/shashwatgtm/icp-intelligence-mcp)** by
Shashwat Ghosh (Helix GTM Consulting), MIT License. The schema borrows the skeleton —
dimensions and fields — not the package's code or workflow.

> The upstream launch article (marketing for the original kit) is preserved in this repo's
> git history — provenance material, not part of the product, and not redistributed in the
> working tree.
