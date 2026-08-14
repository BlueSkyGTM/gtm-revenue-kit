---
type: channel
provenance: michael-course
maturity: standard
---

# Playbook: Cold Email (Channel Strategy)

*How to run cold email as a channel — the economics, the testing discipline, the stack shape,
and the inbox process that most teams skip. This is strategy for the channel; the mechanics
of building the list live in `motions/tam/skeleton.md` and the sending infrastructure in
`motions/playbooks/deliverability-and-warmup.md`.*

---

## Trigger

Any of:
- Deciding whether cold email is the right primary channel for an account
- A campaign is sending but replies are not converting to pipeline
- Designing the reply-handling process before a first launch
- Results plateaued and the question is "test more copy or fix the process?"

---

## The mindset: cold email is an ad network

At volume, cold email behaves like a paid advertising platform, not like correspondence: you
put a message in front of a defined audience and measure yield. The channel fits best when
the account's addressable market is large — thousands of companies at minimum — because a
volume channel needs room to burn test variants without exhausting the audience. Below that,
the micro-list motion (`motions/channels/micro-lists.md`) fits better; the account's
`context/scoring-model.md` records where its own line sits.

The governing question for the channel is a yield question:

> **What value proposition produces one interested reply per N sends — and what does the
> account need N to be?**

The account sets its target yield in `context/scoring-model.md`, reasoning backward from deal
economics: what a meeting is worth, times conversion, against what a send costs in list burn
and domain reputation. Once real yield is measured, capacity planning is arithmetic — replies
needed per month → sends needed → mailboxes and domains needed
(`motions/playbooks/deliverability-and-warmup.md`).

---

## The testing discipline: value proposition and list, nothing else first

Two variables move cold email results: **what you offer** and **who you send it to**. Subject
lines, CTAs, phrasing, and personalization depth are second-order. The testing order is
therefore fixed:

1. **Phase one — find a winning value proposition.** Run a handful of distinct value
   propositions against the same list in the fixed template from
   `motions/tam/skeleton.md` Stage 4, each with enough sends that zero interested replies
   is evidence rather than noise. Per-variant send volume is an account value; the reasoning
   is statistical honesty — a variant judged on too few sends is judged on luck.
2. **Phase two — compress.** Only after a variant clears the account's yield bar, A/B the
   secondaries: subject line, CTA, creative format, personalization depth. This is where
   yield improves incrementally.
3. **Keep the copy short throughout** — the account sets its word cap
   (`motions/playbooks/deliverability-and-warmup.md` for why filters and readers both punish length).

A value proposition that never clears the bar is information, not failure: either the offer
or the list is wrong, and the account's benchmark table (`context/scoring-model.md` §8) says which to suspect.

---

## The stack: one sender, one data API, one orchestrator

The channel needs exactly three tools, and consolidation is the point:

| Role | Category | Example |
|---|---|---|
| Sending | A sending platform that bundles mailbox procurement, warmup, and campaign sending | Smartlead |
| Data | One contact-data API for email finding, validation, and enrichment | Lead Magic |
| Orchestration | The data platform that builds the list and pushes rows + custom variables into the sender | Clay |

Wire the orchestrator directly to the sender so enriched rows and personalization variables
flow without manual export. Every additional tool in this path is another sync to break and
another bill; add one only when a named gap justifies it.

---

## Inbox management: where most of the channel's value is won or lost

The strategic claim, and the reason this section exists: **most teams running cold email lose
a large fraction of the channel's results after the reply arrives** — not in copy, not in
deliverability, but in slow, inconsistent handling of the replies they paid to generate. The
fix is a process, staffed.

**Triage — every reply, labeled, daily.** One person (an SDR or AE can typically cover many
mailboxes' worth) works the sending platform's unified inbox:

- **Interested** → into the follow-up process below, same day
- **Not interested** → labeled and left — no argument, no "just checking back"
- **Out of office** → labeled so automation ignores it
- **Angry or unsubscribe** → blocked in the sending platform *and* appended to
  `accounts/<slug>/optouts.md` — the platform block stops the sequence; the optouts file is
  the durable, account-scoped suppression record that survives tool changes

**Follow-through — the four process rules:**

1. **Call interested replies first.** The fastest touch after a positive reply is a phone
   call, and speed here converts better than any copy improvement
   (`motions/channels/cold-calls.md`).
2. **Give outbound its own CRM pipeline.** Outbound-sourced contacts behave differently from
   inbound and need their own stages and conversion tracking; most sending platforms
   integrate directly with the CRM so an "interested" label creates the record automatically.
3. **Run a long-horizon nurture subsequence** for interested-but-not-now: short touches
   spread over many months, each pointing to one substantial piece of content. The
   first-touch hygiene rules relax here — once a thread exists and the recipient has
   engaged, links and images no longer carry the same deliverability risk.
4. **Recover ghosts with a concrete proposal.** When an interested reply goes silent, follow
   up after a few days by proposing a specific date and time (or sending a calendar
   invitation naming one). A concrete time forces a yes/no/counter where "just bumping this"
   invites silence. Use judgment on formality — an unsolicited invite reads as presumptuous
   in some segments; the account's brand voice files decide.

---

## Suppression

Non-negotiable and per-account: before every batch, the list is checked against
`accounts/<slug>/optouts.md` and any client roster declared in the account's `ACCOUNT.md`.
The inbox triage above is one of the feeds that keeps `optouts.md` current.

---

## Related

- `motions/tam/skeleton.md` — building the list and the copy-testing template this
  channel runs on
- `motions/playbooks/deliverability-and-warmup.md` — infrastructure: domains, warmup, caps, bounce
  ceilings
- `motions/channels/cold-calls.md` — the channel that harvests this channel's hand-raisers
- `motions/channels/micro-lists.md` — the alternative when the TAM is too small for volume
- the account's `context/scoring-model.md` §8 — its declared benchmarks for reading results
