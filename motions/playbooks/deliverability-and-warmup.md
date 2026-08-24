# Playbook: Deliverability & Warmup

*How to stand up sending infrastructure that lands in the inbox without risking the account's
real domain. Read this before launching any cold-email campaign, or before spending a dollar on
sending tools.*

This is the durable home for warmup knowledge. `motions/workflows/enrichment.md` holds the same standing
infrastructure rules as part of the list-building pass; this playbook is where the reasoning
behind them lives, plus the tradeoffs and the decisions that should not be re-litigated. An
account's live sending status — which domain, which mailboxes, how far into warmup — is an
account fact and lives in `accounts/<slug>/ACCOUNT.md` and the sending tool's own dashboard,
never here.

---

## Trigger

Any of:
- About to launch a cold-email sequence for the first time
- Deciding whether and how to pay for sending infrastructure
- A domain or mailbox is getting spam-flagged, bouncing, or landing in spam
- Scaling send volume up (new mailbox, bigger list, faster ramp)

---

## The core rule: never send cold from the primary domain

Cold outbound goes from a **separate sending domain**, never from the domain the business runs on.
The account's primary domain is named in `accounts/<slug>/context/profile.md`; whatever it is, it
is not the one you send from. If a sending domain gets spam-flagged, you want the damage
contained to a throwaway, not spread to the principal's real inbox and the site's application
form.

Use a lookalike domain that forwards to the real site, so a curious prospect who types it in
still lands on the real business. The pattern: take the brand name and vary the suffix or add a
short prefix (`<brand>books.co`, `get<brand>.com`, `<brand>financial.co`), then set its
forwarding target to the primary domain. Keep it recognizably the same business — a domain a
prospect cannot connect to the sender is worse than no lookalike at all.

---

## The free / safe / scaled tradeoff (you can have two)

There is no way to run cold email at list scale that is simultaneously free, safe for the primary
domain, and automated. Name which constraint gives:

| Combination | What it is | Verdict |
|---|---|---|
| **Free + scaled** | Blast the full list from the primary domain | **Rejected** — one spam-flag breaks the real inbox and the site's lead form |
| **Free + safe** | Send a handful a day by hand from the real mailbox | Doesn't scale — fine for testing the top couple dozen accounts, not for a full list |
| **Safe + scaled** | Separate sending domain + mailbox, warmed, then automated | **The path.** Costs about one domain registration to start |

The floor to scale *safely* is a lookalike domain for a year plus a mailbox. Price both before
assuming: a domain is usually the cost of a cheap lunch, and a mailbox is often a few dollars a
month, sometimes addable to hosting the account already pays for, rather than a full seat on a
major productivity suite. Below that floor, either the domain's safety or the scale has to give.

Bigger list = stronger argument for the paid domain, not weaker. The more leads, the more you
need real infrastructure and the more it matters that it is off the business domain.

---

## Standing setup rules

These are the same rules `motions/workflows/enrichment.md` applies during list build. If an account's
`ACCOUNT.md` sets a different limit, that number wins for that account.

**Domain setup:**
- Dedicated sending domain or subdomain, never the primary
- SPF, DKIM, and DMARC configured on every sending domain — verify with
  [MXToolbox](https://mxtoolbox.com/) before sending
- Warm new domains **4–6 weeks** before sending at volume: start at 10–20 emails/day, increase
  20–30% per week

**Sending limits (per mailbox):**
- Warmed mailbox: 40–50 emails/day max; ramp new ones far below that, starting around 5–10/day
- Multiple signals or tiers = multiple mailboxes, rotated across
- Enforce the daily cap in the outbound tool, not by hand

**Mailbox rotation:**
- Tier 1: dedicated mailboxes, manually monitored for replies
- Tier 2/3: shared pool, sends rotated evenly
- Immediately pull any mailbox with reply rate < 1% or bounce rate > 3%

**Bounce management:**
- Verify emails before enrolling (a verification service, or the sending tool's built-in verifier
  on import)
- Target < 2% hard bounce per campaign
- Bounce rate > 5% = immediate pause and domain review

---

## Warm while you wait — don't burn the weeks

Warmup is dead time only if you let it be. During it:

- Work the highest-ICP accounts by **phone**. Zero domain risk, fastest feedback, and a
  principal's own experience lands better on a call than in a first email. The account's research
  output already carries direct phone numbers and a best-time-to-call window where enrichment
  found them.
- Draft and verify the remaining account-research briefs, so the sequence has something to say
  the day the domain is ready.
- The first customers landed by phone can fund the paid infrastructure for the rest of the list.

---

## Decisions already made — do not re-litigate

- **Pre-warmed / marketplace domains are rejected.** The vendor SKUs that let you skip warmup do
  it by selling you a generic, non-branded domain, which undercuts any positioning built on a
  named accountable person or firm. They also lock the domain to the vendor's platform: read the
  terms and you will usually find the vendor retains ownership and will not transfer it, so
  leaving the platform means losing the sending asset you warmed. Use the free built-in warmup on
  a domain *you own* instead.
- **No sending from a personal free-mail account, ever.** A personal mailbox on a consumer mail
  provider is not a sending channel for a cold motion. It cannot be authenticated properly, it
  cannot be rotated, and there is nothing to throw away when it burns.
- **Slow is free; a damaged domain is not.** Low, human-looking volume from a real mailbox does
  not trip spam filters. A large automated blast from a domain new to sending is exactly what
  does.

---

## Related

- `motions/workflows/enrichment.md` — the same standing infrastructure rules, applied during list build
- `motions/playbooks/new-signal-response.md` — what to do once a signal fires. This playbook is upstream
  of it: no inbox, no touch.
- `accounts/<slug>/context/positioning.md` — if the account's positioning rests on being a named,
  accountable person or firm, that is the claim a generic vendor domain contradicts
- `accounts/<slug>/ACCOUNT.md` — the send tool and suppression sources for this account. The tool
  itself is not wired in this repo; each operator wires their own `.mcp.json`.
