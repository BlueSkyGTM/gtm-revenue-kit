# Deployments — which copies exist, and what travels between them

`isolation.md` draws the core/account line inside one repo. This file draws it *across*
repos: the same line, one level up. It owns one rule — **core is copied to every
deployment; an account is copied to none** — and the lookup map that follows from it.

Load this when you cannot find something, when you are about to edit a vendored copy, or
when a fact seems to exist in more than one repo.

## 1. The two directions of travel

The engine is a factory; a deployment is a production line. What the factory makes travels
to every line. What a line produces stays on that line.

| | Travels | Lives in |
|---|---|---|
| **Core** — `skills/` `workflows/` `playbooks/` `docs/` `tools/` `sync/` `examples/`, the root files, and `accounts/_template/` | Yes, to every deployment | Every copy, identically |
| **Accounts** — `accounts/<slug>/`: context, outputs, brand, opt-outs | Never | Exactly one deployment |

The `_template/` stamp is core: it is the shape of an account, not an account. That is why
it is the only thing left under `accounts/` upstream.

## 2. Where each thing lives

This repo is **upstream and core-only**. Two deployments vendor it; each holds its own
accounts and nothing of the other's.

| Copy | Holds core | Holds accounts |
|---|---|---|
| `gtm-kit-pro` (this repo, upstream) | **authoritative** | none — `_template/` only |
| `fenton-bookkeeping-os/machinery/gtm-kit/` | vendored copy | `accounts/fenton/` |
| `albatross-engineering-os/machinery/gtm-kit/` | vendored copy | `accounts/revenue-engineering/` |

The catalog of accounts and their deployment pointers is `accounts/_index.md`; this table
never grows an account column beyond what that file declares.

**The lookup rule.** Looking for a method — a play, a channel playbook, a workflow, a
rule, a skill? Any of the three copies has it, and they should agree; upstream decides if
they do not. Looking for facts — a campaign, a research brief, a scored list, a signal
library, an opt-out ledger, a pipeline tracker? Exactly one deployment has it, named
above, and no other copy ever will.

## 3. Upstream decides; a vendored edit does not survive on its own

Core flows one way: **upstream → deployment.** A fix made directly in a vendored
`machinery/gtm-kit/` is overwritten at the next re-vendor unless the same change lands
upstream. This is not a warning about carelessness — it is what makes one engine serve
several deployments instead of quietly forking into several engines.

So: **method improvements go upstream first, then re-vendor.** A pattern learned while
operating one account is promoted the way `isolation.md` §3 already requires — stripped of
its facts, into core here — and it reaches the other deployment as a consequence rather
than as a second act of authorship.

## 4. What this means for the imported material

The course-extracted method — `playbooks/plays/` (all 15), `playbooks/channels/` (all 4),
`workflows/tam-campaign.md`, `enrichment-techniques.md`, `pain-based-segmentation.md`, all
tagged `imported` in `docs/lineages.md` — is core. It passed the swap test during
abstraction, which is precisely why it travels: **it exists in all three copies, and the
business whose operation prompted the import has no more claim on it than any other
deployment.**

The counterpart is exact. The facts that material was abstracted *away from* — that
business's ICP, campaigns, research, opt-outs, tracker — went to one account in one
deployment and are unreachable from here. The extraction and the account split are the
same event seen from the two sides of the swap test.

## 5. History is not a location

The account folders that once lived upstream were removed 2026-08-10 and survive in this
repo's git history. History is provenance, not a copy: **never read a removed account
folder out of git history to answer a live question.** It is stale by construction, and the
account's real home has moved on without it. Go to the deployment named in §2.

## 6. The naming exception

`isolation.md` §1 forbids core from naming an account. This file, `accounts/_index.md`,
`DIVERGENCE.md`, `NOTICE.md`, and `README.md`'s provenance sections are the exceptions:
deployment topology and provenance cannot be recorded without naming the deployments they
describe. The exception is narrow and does not travel — naming a real deployment is
permitted only where *which copy holds what* is the subject, never as an example inside a
method.

## Checking compliance

```bash
# Strict zone: no deployment or account may be named. Must return nothing.
grep -riE "fenton|albatross|revenue-engineering" \
    skills/ workflows/ playbooks/ tools/ sync/ examples/ docs/ accounts/_template/ *.md \
  | grep -vE "^(docs/deployments\.md|DIVERGENCE\.md|NOTICE\.md|README\.md):" \
  | grep -v '<other-account-slugs>'   # drops isolation.md's copy of this command

# Review zone: the §6 exceptions. Hits are expected — read each one.
grep -rn "fenton\|albatross\|revenue-engineering" README.md accounts/_index.md

# accounts/ upstream holds the stamp and the catalog only.
ls accounts/            # expect: CONTEXT.md  _index.md  _template/
```

The strict zone returning nothing is the gate. Review-zone hits are not automatically
fine: each must be a statement about *which copy holds what* or about provenance. A real
deployment named anywhere else — as an example, a default, a sample value — is an account
fact that escaped, and it belongs in that deployment instead.
