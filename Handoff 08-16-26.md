# Handoff — 08/16/26

*A session artifact, not method. Like `estate.md`, it names deployments and is
therefore outside the swap test; it should not be re-vendored into a deployment's
copy of the kit.*

---

## Bearings — do this before forming an opinion

```bash
cd /home/user/gtm-kit-pro
git branch --show-current      # claude/course-extraction-account-split-lm15br
git log --oneline -5
git status --short             # expect empty
```

Read in this order: `CLAUDE.md` (the map, routes only) → `CONTEXT.md` (the task router)
→ the one file your task names. **Do not bulk-load `foundations/`** — it is a shelf, and
loading it wholesale is the documented failure it warns about.

Three repositories are in play:

| Repo | Path | Role | Branch |
|---|---|---|---|
| `gtm-kit-pro` | `/home/user/gtm-kit-pro` | The **portable GTM engine** — doctrine + method only. Travels to every deployment | `claude/course-extraction-account-split-lm15br`, merged to `main` |
| `albatross-engineering-os` | `/workspace/albatross-engineering-os` | **The banner.** The business OS: accounts, products, the corpus wing. Where operating facts live | `master` |
| `fenton-bookkeeping-os` | `/workspace/fenton-bookkeeping-os` | A shelved sibling deployment. Holds an archive only | `main` |

The split matters and is enforced: **core carries no account fact, price, SKU, or
client name** (the swap test, `foundations/principles.md` §2). Those live in the OS.

## The task

Building the operating system for **Albatross Revenue Engineering** — the operator's
(Raymond's) product company. The engine (`gtm-kit-pro`) was reconstructed from an
upstream fork after a prior session turned it into an unusable framework; that
reconstruction is complete and merged. Current work is downstream of it: the firm's
**offer architecture**, a diagnostic product called the health check, and an intake
wing for the operator's own product assets, which he is about to hand over in batches.

## State — verified 2026-08-16

**All three repos are clean and pushed.** Checked with `git status --short` (empty in
each) and by comparing local to `origin`:

- `gtm-kit-pro`: branch HEAD `cb11492` == `origin/claude/...`; `main` `baa5cb8` ==
  `origin/main`.
- `albatross-engineering-os`: `master` `dc6bf73` == `origin/master`. The vendored kit
  at `machinery/gtm-kit/` matches core `main` @ `baa5cb8` (vendor record:
  `docs/machinery.md`).
- `fenton-bookkeeping-os`: `main` `4f3d6eb`, pushed. Shelved — nothing pending.

**Finished and verified**

- **The engine's foundations** — 12 doctrine files plus `CONTEXT.md` in
  `foundations/` (`ls foundations/*.md | wc -l` → 13). Every folder is routed from
  `CLAUDE.md`.
- **The corpus wing** — `albatross:workspaces/corpus/`. `build_manifest.py` regenerates
  `MANIFEST.md` from record frontmatter and validates it; run 2026-08-16, **exit 0, 1
  record, 0 problems**. Its checks are real — they were smoke-tested with deliberately
  broken records and all three fired.
- **One TAM stage-1 run**, by hand, recorded at
  `albatross:machinery/gtm-kit/accounts/revenue-engineering/outputs/2026-08-14-tam-map/RUN.md`.
  It produced a dependency chain, not a map — which was the honest output.

**Half-done — drafts awaiting the operator, not code**

- The **health check** (`albatross:.../outputs/2026-08-15-health-check/DRAFT.md`):
  questionnaire, scoring rubric, report skeleton, delivery flow. **Never run on a real
  business.** Needs a name (see Open questions).
- The **landing page** (same folder, `landing-page-draft.md`). Never published.
- **EDP discovery** (`.../outputs/2026-08-14-edp-discovery/DRAFT.md`) — candidate
  segments per SKU, every threshold marked `guess`. **Parked on the operator's word**
  ("the EDP can wait"). Not dropped; the TAM re-run depends on it.
- The **offer architecture** (`.../outputs/2026-08-15-offer-architecture/`) — the
  diagnostic-led ladder. Current and authoritative for offer questions.

**Not started**

Nothing has been sold, sent, published, or wired. Zero prospects contacted. No
HighLevel configuration exists (declared as the platform; no credentials anywhere).
TAM stages 3–6 have no briefs. The signal library is deliberately empty.

## Decisions and why

**The banner is the OS, not the engine.** Everything the operator hands over lands in
`albatross-engineering-os`; `gtm-kit-pro` stays a portable engine that both deployments
vendor. Rejected: consolidating everything into the kit — it would break the vendoring
model with fenton and destroy the factory/product split.

**The identity: a revenue engineering agency, not an AI one.** It sells revenue
solutions with AI's help and GTM engineering baked in; it never sells AI or GTM
engineering as the offer. The equation, in the operator's words: **revenue architecture
+ GTM engineering = revenue engineering** — and owning the stack means the capability to
*deliver* any subsystem, never the obligation to operate every motion family
("delivering ad systems, not running ads").

**"Not the funnel guy."** The $500 site was demoted from identity-offer to
door-opener wedge. The defensible seat is **diagnosing where a business's eight systems
are disconnected and installing the connection** — so the health check is the front
door of the ladder, and everything below it is prescribed by a diagnosis rather than
pitched.

**Diagnose in eight, treat in bundles.** The eight functions find and name gaps;
treatments cross several pillars at once. The one-server-per-pillar reading was the
kit's own rendering error, corrected after comparing a competitor's asset model.

**The eight pillars are the kit's conceptual framework** (`foundations/conceptual-framework.md`),
on the FASB pattern the operator supplied: when method is silent, judgment derives a
treatment from the pillars rather than improvising or stalling. It is *routed* — from
the map, the router, both TAM stage gates, and the self-check's closing line — because
the failure it fixes was reasoning that existed as documentation nobody's task pointed
at.

**Three registers, one discipline** (`foundations/lexicon.md`): buyers hear *revenue
solutions*; the market hears *GTM engineers*; the house thinks in *revenue engineering*.
The house word never leads in public copy.

**HighLevel is the account's platform** — CRM, forms, funnels, sequences, voice.
Config is operator-local and never in git; the account's `optouts.md`, not the
platform's list, is the auditable suppression source.

## Traps — read this section twice

These are the operator's corrections from this session, written as instructions. They
cost the most to rediscover and survive nowhere else.

**Never invoke "the construction law."** It is **retired** (`foundations/rulings.md`,
08-15). The rule said *transcribe from operation, never author ahead of it*; it was the
prior tooling's accountability device, not the operator's law. I used it to argue that
the build was over-doctrined and was corrected. Do not use it — or any variant — to
argue against building. Sequencing is the operator's call. What protects against
invented method is principle 1 (known-why admission) and `failure-modes.md` §1, both of
which can actually fail.

**The foundations exist because a session does not arrive knowing this discipline.**
They are context engineering for the agent, not a doctrine museum. **Do not measure
their line count against campaigns run** — that comparison was made in this session and
was wrong. It is now written into `foundations/CONTEXT.md` so it is not repeated.

**The material the operator is handing over is his own product assets, not third-party
doctrine.** Cataloguing your own inventory is not absorption and is **never** gated
behind a triage queue. The corpus wing has two tracks: track ① (own assets) stops after
the inventory pass and places each asset against an offer rung; track ② (sources) keeps
the admission test. Copy `_templates/own-asset.md` for track ①. I initially proposed
pausing intake — that was backwards and was rejected.

**Verify an attribution before repeating it.** "Winning by Design" sat in the kit
inherited and unchecked; rather than question it I amplified it into a NOTICE section
and a whole doctrine file. It turned out correct (the firm co-credits both books) but
the *process* was wrong, and the operator caught it as knowledge drift. The standing
rule: every source line states **what was checked and when**. Mark `[V]` for verified,
`[R]` for reported-only. This session also once claimed verification from search
snippets and was caught — do not do it.

**Do not reflexively suggest buying tools, coaching, or subscriptions.** The operator
raised guilt about not paying $200/mo for creator access; the answer was that he bought
the books and that coaching pays only when there are operating questions to ask. Advise
on the merits, not the impulse.

**No roadmap from outside has survived triage.** The operator builds his own. A
competitor's playbook was bought, read in full, and **not adopted** — only its
deliverable skeleton and pricing intelligence were absorbed
(`albatross:.../outputs/2026-08-14-offer-research/`).

**Do not create speculative workspaces or folders.** Structure follows material. Run
`/icm-architect` and get the operator's yes before building a room.

**The foundations are checks, not a lens.** A draft that keeps announcing which rule it
is obeying has produced the ceremony corruption `failure-modes.md` §3 describes.

**Six hosts are egress-blocked** and must not be retried:
`the-revenue-architects.com`, `masteringrevenueoperations.com`,
`cannonballgtm.substack.com`, `qcgrowth.com`, `bebee.com`, `cremanski.com`. The
operator can paste content or widen the environment's network policy.

**Reading PDFs requires manual extraction.** `pdftoppm` is absent and `pypdf` is broken
in this environment. A working extractor is at
`/tmp/claude-0/-home-user-gtm-kit-pro/dc16854c-b833-5a3c-becf-37d0c560625d/scratchpad/extract_playbook.py`
— it decompresses content streams and decodes CID fonts via ToUnicode CMaps. Adapt the
`PDF` constant. **Scratchpad contents do not survive session teardown** — copy it into a
repo if it will be needed again.

## Next actions, in order

1. **Receive the operator's product-asset batch** into
   `albatross:workspaces/corpus/01-staging/<date>-<domain>/`, then run the track ①
   inventory pass: one record per asset from `_templates/own-asset.md`, each naming
   what it is *as a sellable thing* and which offer rung it serves. Regenerate
   `MANIFEST.md` (`python3 workspaces/corpus/build_manifest.py`; exit 0 = clean) and
   commit. Expect the highest-value finding to be **overlaps** — two assets serving one
   rung is a bundling decision better made now than at delivery.
2. **Then, and separately: get the health check run on a real business.** It needs no
   form, no landing page, and no paid traffic — the questions can be asked on a call and
   the report written by hand from the existing skeleton. This is the only thing that
   converts drafts into operating history, and it is also the sales conversation.

Each fits one context window. Do not attempt both in one session.

## Open questions — the operator decides, never guess

- **The health check's name.** "Expert Maturity Index" is a competitor's trademark and
  is unavailable. Blocks publishing, not a hand-run.
- **Wedge pricing:** hold the site at $500 as a deliberate wedge, or move toward the
  $750–1,500 band that positioned competitors charge (evidence on file in the offer
  research).
- **VR flow bundling:** all-in (appointments, follow-back, interactive IG) versus
  as-is. Session recommendation on record: bundle, because the $30–40k/yr salary anchor
  only holds end-to-end.
- **The first five businesses** for the health check. Warm beats cold for the first
  five — the goal is learning what the instrument does in a real conversation.
- **EDP draft confirmation** (parked by the operator). Unblocks the TAM re-run.
- **Cross-deployment suppression**, still open from 08-14: the isolation ruling removed
  the cross-account audience check; the same-day audit argued the removal may be wrong
  where one operator owns both businesses. Ledgers stay separate until he rules.
- **Waste-taxonomy ruling amendment** — flagged, awaiting his word.

## Environment honesty

- **The tag `reconstruction-2026-08-14` exists locally at `baa5cb8` but cannot be
  pushed.** Verified: the push returns HTTP 403 after four retries with backoff, and the
  GitHub API confirms no `reconstruction` tag on the remote — this session's credential
  allows branch pushes, not tag pushes. The operator can push it from his own machine:
  `git fetch origin main && git tag -f reconstruction-2026-08-14 baa5cb8 && git push -f
  origin reconstruction-2026-08-14`. Nothing depends on the tag; `main` is the reference
  point.
- **Dates in `rulings.md` read 08-14 and 08-15 while the system date is 08-16.** The
  entries were written on the days the decisions were made in-session; the lag is
  cosmetic and the ordering is correct.
- Nothing is running. No servers, no migrations, no watchers, no scheduled jobs.
- The plan file from this session is at
  `/root/.claude/plans/sunny-mapping-stroustrup.md`. Its last content is a *rejected*
  proposal (the pause-intake plan) — **do not execute it**; it is superseded by the
  corrections in Traps.
