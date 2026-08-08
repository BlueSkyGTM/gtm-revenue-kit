# EXTRACTION.md — the fenton account and its host repo

The mirror of the host repo's `REFERENCES.md`. That file documented how the GTM engine
*arrived* in `fenton-bookkeeping-os/workspaces/practice/`; this one documents how operations
*shift* to this account — and it is the runbook for the day the operator chooses to complete
the separation. It is prep, not a pending action.

> **MIGRATION COMPLETED 2026-08-08, on the operator's explicit order** ("complete the gtm
> kit migration"). The cut was executed against the seam map in §4: the host repo's
> `workspaces/practice/` was removed, the four non-GTM tenants were rehomed
> (pipeline tracker → this folder; revenue, business-dev, pricing-strategy →
> host `workspaces/clients/business-dev/`; the site → host `workspaces/clients/web/`),
> the ~20 doc seams and one code seam were rewired, and the Instantly block was stripped
> from the host's three `.mcp` variants, restoring its mechanical send guard. The
> dual-append opt-out rule ended the same day — this account's `optouts.md` is the sole
> ledger. Sections below are kept as the record of the operation's design; §1–2's
> "host copy" language is historical as of the completion date.

**The rule that governed until completion: nothing deleted in the host repo without the
operator's explicit decision.** That decision arrived 2026-08-08 and this file was its
runbook.

---

## 1. Transfer state

Content was copied from `fenton-bookkeeping-os/workspaces/practice/` on 2026-08-06/07 and
restructured to the tenant contract (the `-white-label` file quadruplet became
`context/tracks/white-label/`; instance overlays moved from core skills into `ACCOUNT.md`).

**Parity confirmed 2026-08-07:** the only host-side practice/ change after the copy was one
research brief (`2026-08-06-inventwealth-precision-bookkeeping-research.md`), which is
already in this account's `outputs/`. The transfer is current as of that date.

**If host-side GTM work ever resumes** (it should not — see the operating rule below), the
re-sync is copy-in only: diff `workspaces/practice/` against this account, bring changes
here, never write back.

## 2. The operating rule going forward

- **GTM work happens in this account.** Research briefs, scoring runs, campaigns, sequences,
  reply handling — all of it lands under `accounts/fenton/` in this repo.
- **The host repo keeps what is not GTM:** the books pipeline, the client folders and their
  delivery records, the ledger machinery, the Vault pointer. That split is the point of the
  separation: a books session and a GTM session should never have been in one loading
  surface.
- The host copy of the engine is **read-only reference** from now on. If something there
  turns out to be newer than this account, that is a re-sync event (§1), not a reason to
  work there.

## 3. The two cross-repo contracts (in force NOW)

These replace the in-repo seams the funnel used to cross, and they are deliberately thin —
names and fields, never figures.

**Won handoff (kit → host).** When a pipeline row in this account reaches **Won**, the
operator creates the client folder in the host repo (`workspaces/clients/clients/<slug>/`
from its `_template/`), carrying exactly the fields the host's template already names:
**Lead source** (this account's campaign slug), **Monthly fee**, **Setup / cleanup fee**,
plus the two suppression keys (contact email, domain). The application transcript lands in
the client's `intake/` per the host's intake README. Nothing else crosses.

**Suppression (host → kit).** Sends happen from this repo, so this account's `optouts.md` is
the ledger every batch checks — **and, while both copies exist, every opt-out is appended to
BOTH** this file and the host's `workspaces/practice/business-dev/optouts.md` (the standing
dual-append rule; two ledgers that silently disagree is the failure this prevents). The
second suppression source is the host's client roster at `workspaces/clients/clients/*/` —
read at send time, **names and domains only, never books, never figures** — so a paying
client never receives a cold campaign.

## 4. The seam map — for the day the operator chooses to cut

Catalogued from a full host-repo exploration (2026-08-06), so the future operation is
mechanical. None of this is executed now.

**Non-GTM tenants living inside practice/ that would need rehoming first:**

| What | Where it would go | Why there |
|---|---|---|
| `pipeline/pipeline-tracker.*` | this account | pipeline rows are GTM operating state; `reply-handling` already writes them where `ACCOUNT.md` says |
| `revenue/` (forecast, allocation) | host `workspaces/clients/business-dev/` | firm money-planning, Miriam-facing |
| `business-dev/` (incl. the opt-out ledger's archived copy) | host `workspaces/clients/business-dev/` | **heals pre-existing damage**: the host's clients/CONTEXT.md and seven email templates already reference a `clients/business-dev/` folder that has never existed on disk |
| `context/pricing-strategy.md` | host `workspaces/clients/business-dev/` | commercial terms; four books/docs files cite it and would be re-pointed |
| `web/` (site mirrors, WordPress assets) | host `workspaces/clients/web/` | the inbound form feeds clients' intake; the intake README already points at it |

**The one code seam:** host `workspaces/books/tools/verify-migration.py:1102` emits
`practice/context/pricing-strategy.md` into every proof packet. The fix (neutral caption, no
pointer) is already proven in the standalone migration-kit — apply the same one-line change.

**The ~20 doc seams** (file → what references practice/): host `CLAUDE.md` (folder map,
three-workspaces framing, the flow diagram, two tools-table rows) · `CONTEXT.md` (six routing
rows, workspace table, funnel section) · `CAPABILITIES.md` (the GTM section, lines ~80–101 —
would become one pointer to this repo) · `START-HERE.md` (the "winning clients" table, the
flow line) · `docs/loading.md` (the two-rule-systems table is *defined* by the GTM/ledger
split and needs rewriting, not deleting) · `docs/permissions.md` (the operator-division
line) · `docs/naming-and-placement.md` (the practice-output row) · `README.md` (four status
rows, the practice feature table, the lint command in the verification block) · four
`books/docs/*` citations of pricing-strategy.md.

**The Instantly block** sits in all three host `.mcp` variants, so the send tool loads in
every books session there — and `INSTANTLY_API_KEY` is set machine-wide, so it loads *live*
(host HANDOFF item 5). Removing the block from the host's three files restores the
mechanical guard and leaves the send tool existing only in this repo's operator-local
`.mcp.json`. That removal is a host-side decision, recorded here, not taken here.

**Post-cut gates, whenever the cut happens:** host-wide `grep -r "practice/"` returns only
historical/evidence mentions · all four host tool selftests green · `.mcp` files valid JSON ·
host README/HANDOFF verification blocks updated (the copy linter lives in this repo now) ·
finish with the host's self-diagnosis sweep — the same discipline that caught ~30 corruption
sites after the purge episode.

## 5. What this file is not

Not a deletion schedule, not a deadline, and not permission. The host repo is a live
operating system for a real practice; its shape changes on its operator's word and its own
handoff discipline, never as a side effect of work in this one.
