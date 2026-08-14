# ACCOUNT.md — [Account name]

The summary layer for this account. Claude reads this when the account is named: enough to
execute most tasks without opening anything else, with pointers to the deeper files.

**Fill this in once. Keep it updated when things change.** Everything here is a fact about
*this* account. Nothing here is a rule about how the engine works — those live in core
(`foundations/`), and they are the same for every account.

---

## Identity

**Slug:** `[folder-name]` — must match this folder's name exactly
**Tier:** [operator / engineer] — which surface this account's principal works from
**Status:** [scaffolded / configured / live / paused]
**Operator:** [who runs this account day to day]
**Principal:** [who approves a send, if not the operator]

---

## Company

**[Company name]** helps [specific customer type] [specific outcome] — without [the
alternative they use today, or the pain they live with].

Stage: [bootstrapped / Series A / B / C] — [X] employees, [Y] in GTM
HQ: [City] | Website: [domain.com]

GTM motion: [Sales-led / PLG + Sales / Community-led / Owner-led]
ACV: [$X – $Y] | Sales cycle: [X days median]
Primary channels: [in order of volume]

---

## ICP

Full definition: `context/icp-definition.md`

**Who we sell to:** [One sentence. Size, industry, stage, and what they already have in
place that makes them ready.]

**Tier 1:** [the tightest filter — what makes an account a dream account]
**Tier 2:** [one step looser — still strong fit, signal-triggered]
**Tier 3:** [minimum criteria — automated outreach only]

**Never target:**
- [Exclusion + one-line reason]
- [Exclusion + one-line reason]

---

## Tracks

*Delete this section if this account sells one thing to one buyer.*

An account with two buyers keeps each in `context/tracks/<slug>/`. **Never blend them** —
separate ICP, positioning, radar, and messaging is the entire point.

| Track | Buyer | Offer | Status |
|---|---|---|---|
| `[slug]` | [who] | [what they buy] | [live / drafted / paused] |

---

## Personas

Full profiles: `context/personas/`

| Role | Title(s) | Primary concern | Best channel |
|---|---|---|---|
| Champion | [title] | [pain they own] | [Email / LinkedIn] |
| Economic buyer | [title] | [what they are measured on] | [channel] |

*At an owner-led account these are one person. Say so rather than inventing a committee.*

---

## Positioning

Full document: `context/positioning.md` · Voice and copy rules: `brand/voice.md`

**We win when:** [the condition where we are the obvious choice]
**We lose when:** [be honest — price, timing, a specific competitor]

vs. [Competitor A]: [edge in one line]
vs. [Competitor B]: [edge in one line]

---

## Signals

Full library: `context/signal-library.md` · Every point value: `context/scoring-model.md`

**Act immediately (Tier 1):**
1. [Signal] — [what fires it, where it comes from, why it predicts]
2. [Signal] — [...]

**Add to sequence (Tier 2):**
1. [Signal]

---

## Sending

**Send tool:** [tool name, or "none wired"]
**Config:** the operator's own `.mcp.json` (gitignored) — see `.mcp.json.example`. **Never
committed**, and never shared between accounts.

**Suppression, checked before every batch:**
- `optouts.md` in this folder — append-only, permanent, legal
- [Client roster, if this account sends on behalf of someone: name the source here. Names
  and domains only — never their figures.]

---

## Stack

CRM: [ ] | Enrichment: [ ] | Signals: [ ] | Outbound: [ ] | Call intel: [ ] | Intent: [ ]

---

## Account overlays

*Instance facts that a core skill would otherwise have to hardcode. A skill says "read the
account's tenure field"; this table says which field that is here. Add a row only when a
core skill genuinely needs a local name for something.*

| Skill | What it needs | Where it is, in this account |
|---|---|---|
| `account-research` | [e.g. tenure, plan tier, directory listing] | [the actual field or source] |
| `icp-scoring` | every value | `context/scoring-model.md` |

---

## Current priorities

- [ ] [Specific and actionable]
- [ ] [ ]
