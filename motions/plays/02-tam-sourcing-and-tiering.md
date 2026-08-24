# Play: TAM Sourcing and Tiering

Not an event play — the foundation the event plays stand on. The whole addressable market is
mapped once, scored, cut into tiers, and assigned, so that every selling day starts with a
prioritized list instead of a research session. The signal, such as it is, is *drift*: the
map decays continuously, and the play's recurring work is keeping the tiers true. It reaches
everyone the account could ever sell to, which is exactly why it must be built before the
sharper plays run.

---

## The signal

**What fires:** this play has no buying-moment trigger, and pretending otherwise would be
dishonest. Two conditions activate work:

1. **The map does not exist** — sellers are choosing their own targets, which means the
   account's ICP definition is being re-derived daily, badly, by everyone independently.
2. **Tier drift** — a mapped company's score changes enough to cross a band boundary
   (growth, funding, tech change, shrinkage), or new companies enter the market.

The account's `signal-library.md` does not record this play as a signal row; instead, this
play is what makes every other signal row *land somewhere* — a firing signal adjusts the
score of a company that already exists on the map. The refresh cadence for the map itself
is set in the account's `context/scoring-model.md`.

---

## Why it works

Seller time is the most expensive input in the system, and list-building is its least
valuable use. A meaningful fraction of a typical SDR day disappears into deciding who to
contact — sourcing, deduplicating, judging account worth — none of which requires a human.
Moving that work into the engine returns whole hours per seller per day to actual
conversations.

The second mechanism is alignment. One shared map, one scoring model, one tier table means
marketing targets the same companies sales calls, and sales closes the kinds of accounts the
delivery side can serve. Most "sales and marketing misalignment" is two teams holding two
different implicit TAMs; making the map explicit dissolves the argument.

The limit: a map is only as good as the ICP definition under it. Tiering garbage produces
confidently ranked garbage. And a static map rots — the play is a subscription, not a
purchase.

---

## The build

1. **Define the universe.** From the account's `context/icp-definition.md`, derive the
   hard boundaries (industry, size band, geography, must-have attributes) and pull every
   matching company from a B2B data provider (Clay, Apollo, ZoomInfo, Crunchbase, or
   similar). Err inclusive at this step; the scoring pass does the excluding.
2. **Enrich to scoreable.** Fill the attributes the account's `scoring-model.md` actually
   scores on — nothing more. Enrichment coverage below the account's enrichment gate
   (`scoring-model.md` §8) means the scores are fiction; fix coverage before tiering.
3. **Score and tier.** Run `motions/skills/icp-scoring/SKILL.md` across the map. Band boundaries
   come from the account's `scoring-model.md`. The output is every company in exactly one
   tier, including an explicit below-threshold tier that nobody works.
4. **Assign territories.** Divide the tiered map across sellers — by segment, geography,
   or round-robin, whichever the account records in its context. The end state: each
   seller's day starts inside an already-built, already-prioritized slice. Where a dialer
   or sequencer is in use, load the slices directly into it.
5. **Suppress.** Existing customers, open opportunities, and the account's `optouts.md`
   are marked on the map itself, so every downstream play inherits the suppression.
6. **Schedule the refresh.** On the cadence the account sets: re-enrich changed fields,
   re-score, log band crossings. An upward crossing is worth a notification; it is the
   closest thing this play has to a firing event.

---

## The message frame

This play does not send messages — it decides who receives the messages other plays write.
The one frame-adjacent rule it owns: a seller working a tier slice must still satisfy the
"why now is datable" standard in `foundations/pvp.md` before any first touch. Tier rank is a
budget decision, not a reason to reach out — "you scored well on our model" teaches the
prospect nothing. Pair the tier with a live signal from the account's `signal-library.md`,
or run the light-touch treatment the tier's band prescribes.

---

## Measurement

- Seller time reclaimed: share of the day spent in conversations versus list work, before
  and after
- Conversations per seller per day — the number this play exists to raise
- Map health: enrichment coverage and staleness (time since last refresh), held against the account's
  gates (`scoring-model.md` §8)
- Tier honesty: win rate by tier should slope the way the model predicts. A flat slope
  means the scoring model is not discriminating and needs recalibration in the account's
  `scoring-model.md`
- Churn from off-map deals: deals closed outside the map's serviceable definition should be
  rare and reviewed

---

## When NOT to run it

- **The ICP is unvalidated.** A pre-product-market-fit account mapping its imagined TAM
  bakes guesses into infrastructure. Run discovery, not tiering.
- **A tiny market.** When the addressable universe is small enough to hold in one
  spreadsheet and one head, the tooling overhead outweighs the return — though the tier
  discipline still applies.
- **As a one-off project.** A map without a scheduled refresh is a snapshot that will be
  quietly wrong within a quarter and trusted anyway — worse than no map, because it wears
  the costume of rigor.
- **To dodge the segment-purity rule.** Tiers are budget bands, not audiences. Blending
  tiers into one campaign to hit the audience-size gate violates the segmentation discipline
  (the account's `scoring-model.md` §5).
