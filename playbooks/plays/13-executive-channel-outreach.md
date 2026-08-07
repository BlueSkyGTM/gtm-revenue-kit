# Play: Executive Channel Outreach

A channel play more than a signal play, stated honestly: the same outreach converts at a
different rate depending on whose face sends it. Messages from a company's executives get
opened, accepted, and answered where identical messages from an SDR title get reflexively
filtered — so the play runs the account's professional-network outreach *through executive
profiles*, with the operational load carried centrally. It reaches audiences that are native
to the platform, and it works best where the executives have real presence there.

---

## The signal

**What fires:** this play mostly rides other plays' signals — it is the *send channel* for
motions like `playbooks/plays/12-competitor-crisis-response.md` or any sequence built by
`skills/signal-to-sequence/SKILL.md` where the account chooses the executive channel. Two
channel-native events do fire on their own:

1. **Connection accepted** — the prospect opted into the relationship; the follow-up window
   opens and decays quickly.
2. **Open-profile status detected** — the prospect's profile accepts free direct messages
   from non-connections, which changes the available motion for that contact (message
   directly instead of connect-first). Only a minority of profiles are open, and status is
   not visible at scale without tooling — a profile-status scraping actor (via an
   automation marketplace such as Apify) enriches it in bulk inside the orchestrator.

The account's `signal-library.md` records "connection accepted" as a **Behavioral** row
with a short recency window, and open-profile status as a routing *attribute* rather than
a scored signal; weights and windows live in the account's `context/scoring-model.md`.

---

## Why it works

Sender identity is the first filter. A visible SDR title telegraphs "pitch incoming" and
gets shut down before the first sentence; a senior title from a known company triggers the
opposite reflex — people accept and answer executives because the connection itself carries
perceived value. The message has not changed; the prior against it has.

The economics work because the executive lends the *identity*, not the hours: a single
operator manages sourcing, sequencing, and inbox triage across several executive profiles
through a LinkedIn-automation tool (HeyReach or similar), with the executive stepping in
once a conversation is genuinely alive. Executives with an active content presence compound
the effect — the profile that messages you is one you may already have seen in the feed.

The limits are structural. The whole play operates inside another platform's tolerance:
automation on personal profiles carries account-restriction risk, mitigated (not
eliminated) by using the platform's own paid sales product on every profile — which also
signals sales intent to the platform in a sanctioned way — and by keeping volumes inside
humane ramps. There is also an authenticity debt: a prospect who discovers they were
warmed up by an operator wearing an executive's face feels deceived, and the executive's
reputation is the collateral. The executive must know, approve, and actually take over
live conversations.

---

## The build

1. **Enroll the executives.** Explicit consent, the platform's paid sales product on every
   participating profile, and an agreement about who answers what. Their profiles get a
   presence pass — a credible profile is the landing page of this play.
2. **Wire the automation.** Connect the profiles to the LinkedIn-automation tool; one
   operator (SDR or equivalent) runs all inboxes from a unified view.
3. **Enrich the routing attribute.** For each target list, run the open-profile-status
   scraper in the orchestrator. Open profiles route to the direct-message motion (free
   messages, no connection required — effectively multiplying daily reachable volume
   without paid message credits, which are scarce and expensive). Closed profiles route to
   the connect-first motion.
4. **Ramp like a human.** Connection volume starts low — a handful per day per profile —
   and rises slowly to a modest ceiling; the exact ramp lives in the account's
   `scoring-model.md`. Bursts are what platform enforcement pattern-matches on.
5. **Sequence as conversation, not broadcast.** The connect-first motion sends a blank or
   minimal connection request, then, after acceptance, a short question that opens a
   dialogue — the pitch only enters an already-live exchange. Suppression against the
   account's `optouts.md` runs before every batch, as always.
6. **Hand off live conversations.** The operator triages; the executive (or an AE, if
   disclosed) carries real conversations forward. Route qualified threads into the
   account's standard motion via `playbooks/new-signal-response.md` conventions.

---

## The message frame

Two beats, deliberately asymmetric. **Beat one earns the channel:** the connection request
itself carries no pitch — blank, or one line of genuine context. **Beat two opens with a
question the recipient is well placed to answer** — about their approach, their market,
their stated position — sincere enough that answering it is easy and slightly flattering.
Only inside the resulting exchange does relevance to the account's offering surface, and by
then it must satisfy the PVP standard from `docs/standards.md` like any first touch: the
prospect should learn something about their own business even if the thread dies there.
Executive voice is mandatory throughout — an executive profile sending SDR boilerplate is
the worst of both worlds, and the "why now," when the pitch arrives, must still be datable
per the standard.

---

## Measurement

- Acceptance rate per profile (the executive-versus-SDR delta is this play's thesis — if
  an executive profile accepts no better than a rep profile, the profile needs work or the
  audience is wrong)
- Open-profile hit rate on target lists, and direct-message versus connect-first
  conversion, to validate the routing attribute's value
- Reply and meeting rates per profile and per motion, read against the benchmarks in
  `docs/standards.md`
- Handoff integrity: share of live conversations actually carried by the named human —
  the authenticity debt, audited
- Platform health per profile (restrictions, warnings) — a leading indicator that the
  ramp is too aggressive, and grounds to pause regardless of performance

---

## When NOT to run it

- **The audience is not platform-native.** If the account's buyers do not live on the
  professional network, the channel advantage has no one to work on.
- **Executives who will not participate.** Borrowed identity without genuine takeover is
  impersonation with extra steps; the first prospect who realizes it converts the play's
  asset (executive credibility) into its liability.
- **Volume ambitions.** This channel punishes scale by design. If the plan requires
  hundreds of daily touches per profile, the plan is a ban, scheduled.
- **As the whole strategy.** Platform dependence means the play can be repriced or
  terminated by a policy change overnight. It layers over the account's owned channels;
  it never replaces them.
