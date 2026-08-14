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
use. That extension history is recorded in
`_archive/2026-08-13-framework/DIVERGENCE.md` and in git history.

Both paths trace to the same MIT-licensed origin. Account content is the operator's own
work product and carries no upstream claim.

## Michael's coursework

The signal-play library (`motions/plays/`, all 15), the channel playbooks
(`motions/channels/`, all 4), the TAM pipeline skeleton (`motions/tam/skeleton.md`), and
`motions/workflows/enrichment-techniques.md` derive from coursework by **Michael**,
curated and licensed by the operator. The present files are method abstractions produced
2026-08-08; the operator's improved TAM framework (their own work, building on the
course) is replacing the skeleton as it is briefed in. Reasoning, examples, and
attribution travel with future revisions rather than being stripped — that is a standing
rule of this reconstruction.

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

> The upstream launch article (marketing for the original kit) is preserved at
> `_archive/upstream/ARTICLE.md` — provenance material, not part of the product.
