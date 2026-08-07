# Play: Social Engagement Signal

People researching a purchase educate themselves in public: they follow, like, and comment on
professional-network content about the problem space. The play monitors engagement on a
curated set of creators, competitor voices, and company pages in the account's category,
extracts the engagers, filters the decision-makers from the merely curious, and gives sellers
a self-refreshing pool of people demonstrably paying attention to the topic. It reaches
buyers during the education phase — earlier than intent data, later than cold.

---

## The signal

**What fires:** a person engages (comment, reaction, follow) with content about the
account's problem space — on posts by tracked category creators, by competitors' visible
employees, or on the account's own company page. One engagement is weak; repeated engagement
across tracked sources is the real event. The engagement-count threshold that separates
"noted" from "fired" is set in the account's `context/scoring-model.md`.

**Where it comes from:** a social-engagement scraping tool (Trigify or similar) monitoring a
tracked list — typically a couple dozen creators and pages, chosen because the account's
buyers actually read them — feeding an enrichment orchestrator such as Clay.

**Decay:** moderate. Topic interest persists longer than a website visit but is not durable;
someone engaging weekly is in an education arc that ends. The account's `signal-library.md`
records this as a **Behavioral / Intent** signal, weekly refresh, with the recency window and
per-engagement point values in the account's `scoring-model.md`.

---

## Why it works

Engagement is costly attention. Scrolling past is free; commenting on a post about a niche
operational problem is evidence the problem is currently on that person's desk. Aggregated
across a tracked list, the engagers form a map of who is educating themselves on the topic
right now — and self-education is what buyers do immediately before they buy.

Two structural advantages: the pool refreshes itself as long as the tracked creators keep
posting, and engagement is public, so referencing the topic (never the surveillance) is
natural. The limits are equally structural: the play only works where the account's buyers
are actually active on the platform; engagement skews toward the platform-native (marketers,
salespeople, recruiters) and undercounts quieter buyer types; and most engagers are peers,
students, and vendors — the filter step is the play, not a detail of it.

---

## The build

1. **Curate the tracked list.** Pick the creators, competitor voices, and pages whose
   audience is the account's buyer, not merely its industry. Record the list and its
   rationale in the account's `signal-library.md` entry; review it on a cadence, because
   creators drift off-topic.
2. **Scrape engagement.** The social-signal tool collects engagers per post into the
   orchestrator, with the post topic and engagement type attached.
3. **Filter decision-makers from spectators.** Enrich each engager to title, company, and
   seniority; hold them against the account's `context/icp-definition.md` and personas.
   This step typically discards most of the pool — that is the step working, not failing.
4. **Accumulate, don't react.** Log engagements per person over time. Single-touch
   engagers sit in a monitor state; repeat engagers cross the firing threshold the
   account's `scoring-model.md` defines.
5. **Suppress and score.** Check the CRM and the account's `optouts.md`, then run
   `skills/icp-scoring/SKILL.md` — engagement is one input among the account's other
   signals, and the combination bonuses live in the `scoring-model.md`.
6. **Route to a topic-matched sequence.** Via `skills/signal-to-sequence/SKILL.md`, with
   the sequence keyed to the *topic* engaged with, not to the fact of engagement. Where
   the platform is the natural channel, a social-touch step (connect, engage, then
   message) can precede email; any social automation must stay within humane, low-volume
   limits the account records in its context.

---

## The message frame

Never open with "I saw your comment on…" — public or not, it reads as surveillance and
spends the first line on you watching them rather than helping them. The frame: enter the
conversation they are already having. Open with a sharpened claim, a counterpoint, or a
piece of evidence on the exact topic they have been engaging with — the message should feel
like the best comment they read that week, arriving as a note. The topic match *is* the
personalization. Strip the CTA and it must stand as a contribution to their self-education:
the PVP standard from `docs/standards.md`. The datable "why now" is the observable
discussion arc in the space, not the individual's click history.

---

## Measurement

- Pool quality: share of scraped engagers surviving the ICP filter (a collapsing share
  means the tracked list has drifted)
- Threshold validation: reply rate of repeat engagers versus single-touch engagers — if
  they perform the same, the accumulation threshold is decoration
- Reply and meeting rates versus the account's cold baseline, read against the benchmarks
  in `docs/standards.md`
- Pipeline attributed to the signal, logged in the account's `signal-library.md`
  performance log; campaign gates in `docs/standards.md` govern any sequence built on it

---

## When NOT to run it

- **Buyers are not on the platform.** If the account's personas do not spend attention
  there, the pool will be full of adjacent professionals who look plausible and never buy.
- **The category has no content scene.** Thin or absent creator coverage means the tracked
  list monitors noise.
- **The filter is skipped.** Run without seniority and ICP filtering, this play becomes
  spraying everyone who liked a post — worse than cold, because the list is biased toward
  vendors and job-seekers.
- **Tempted toward engagement-stalking copy.** If the sequence cannot resist citing the
  prospect's specific likes and comments, the play damages the brand it runs under.
