# Metrics & Decision Rule — QuickBooks Bounce

Date set: 2026-07-12 (before launch, per `workflows/campaign-build.md`)

## Phase 1 — Test (Segment B test bed, 165 leads, 3 variants)

| Metric | Target (Tier 3-equivalent) | Investigate below |
|---|---|---|
| Open rate | ≥ 30% | < 30% → subject line problem |
| Reply rate | ≥ 2% | < 1% after 50 sends → pause that variant |
| Positive reply rate | ≥ 1% | — |

**Winner rule:** highest reply rate once every surviving variant has ≥50 sends (ideally full 55); tiebreak on positive-reply rate. If ALL variants are under 1% reply, do not roll anything out — rewrite hooks and re-test on the remaining test-bed budget before touching Segment A.

**Timeline:** first read at 1 week, decision at 2 weeks.

## Phase 2 — Rollout (Segment A 501 + B hold-out, winner only, ordered by ICP score)

Tier 1 (80+, 320 accounts) is one tier running one sequence, but two effort levels — so it carries **two targets**, not the kit's blended Tier-1 ≥8% default (re-anchored 2026-07-13):

| Slice | Definition | Reply target | Positive target |
|---|---|---|---|
| **T1 research head** | Top 20 of Tier 1 by score (tie-break: signal score, then offer-intent A over B) — account-research brief + manually personalized touch 1 | ≥ 8% | ≥ 5% |
| **T1 tail** | Remaining ~300 of Tier 1 — same tier-1 sequence, signal/segment personalization only | ≥ 5% | ≥ 2.5% |
| Tier 2 (60–79) | Signal-triggered sequence | ≥ 4% | ≥ 2% |
| Tier 3 (40–59) | Automated sequence | ≥ 2% | ≥ 1% |

Track the head and tail **separately** in `results.md`. The head doubles as the live test of the research brief's value: if head reply rate doesn't beat the tail by ≥3 points, the 20–40 min/account research cost isn't earning its keep — don't extend N beyond 20; if it clears it, consider raising N.

## Tracking

- Log per-variant sends/replies/positive replies weekly into `results.md` and the Signal Performance Log in `context/signal-library.md`.
- Follow-up task: Instantly API adapter writing `results-sync.json` per `tools/README.md` schema so `skills/weekly-update` reads live numbers.
  *[2026-08-03: `practice/tools/` and `skills/weekly-update` were deleted 2026-07-29; this follow-up is void — results are logged by hand from the Instantly dashboard. See HANDOFF.md.]*
- Suppression before every send batch: existing **Fenton clients** (keys on Fenton's client list — NOT Intuit Live payers, who are prime targets; zero Fenton clients today so this suppresses nothing yet), prior opt-outs, the 3 Full-Service firms (hand-send track), the 4 PENDING_CANCEL (rollout-first track).

## Campaign economics — carried over from the retired GERU simulation

The GERU funnel-simulation file (`outputs/2026-07-14-geru-funnel-simulations.md`) was
deleted 2026-07-25 as stale: it modelled a 835-lead universe, four packaging models and a
Smartlead-era channel mix, none of which match the current state (861 Airtable records,
141 loaded in Instantly, White-Label moved to LinkedIn). Its conclusions still hold and
are preserved here so the file itself is not needed.

**1. This campaign is a proof-point engine, not a book-filler.** At average benchmark
rates the list yields roughly **2 recurring clients plus ~1.6 cleanups, about $17K
first-year revenue**. Even the strong band lands near 4.5 clients against a delivery
ceiling above 15. Plan around it producing *references*, not capacity utilisation.

**2. The list is the binding constraint, not Miriam's capacity.** Every scenario ran out
of leads long before it ran out of delivery hours. Growth spend belongs in list
acquisition, not in delivery capability.

**3. Break-even is ~0.14% reply rate**, roughly 10x below the weak benchmark band. The
real risk in this campaign is **burning the list**, not losing money. That is why the
copy linter and the suppression rules matter more than send volume does.

**4. Packaging: run the simple recurring offer as the spine.** Ranking was M3 >= M1 ~ M4
> M2 with the top three inside assumption noise, so the tiebreak is operational
simplicity. Overlay the bundle on the ~35 nonprofit/gov accounts, A/B a paid audit later,
skip the fourth model.

**5. Channel CAC ladder (2026 industry benchmarks):** owned list ~**$54** · Clay-sourced
cold email ~**$254** · Facebook ~**$1,000** · Google ~**$1,778**. This is the argument for
staying on cold email off an owned list and scaling via sourcing rather than paid ads.

**Known gap in that analysis, unresolved:** it only ever compared *cold* channels against
each other. It never priced a warm path — referral, Miriam's own 30-year professional
network, local business associations. For an operator with zero public proof points, a
warm introduction may reach the first referenceable client faster and cheaper than any
number in the ladder above. Nothing in the repo has tested this.
