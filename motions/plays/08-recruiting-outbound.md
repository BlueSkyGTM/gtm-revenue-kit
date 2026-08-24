# Play: Recruiting Outbound

The engine pointed at a different market: candidates instead of customers. Recruiting is
structurally an outbound motion — define the ideal profile, source at scale, filter hard,
reach out personally, manage a pipeline — and the same sourcing-enrichment-sequencing
machinery that fills a sales pipeline fills a hiring one, with a stronger offer to make
(a job) than any product pitch. It reaches the candidates who never visit job boards: the
employed, non-searching people who are usually the best ones.

---

## The signal

**What fires:** internally, a hard-to-fill role opens — the play activates on hiring need,
not on a market event. Per candidate, the "signal" is *profile fit*: the observable match
between a person's history and the role's requirement set. Optional event overlays sharpen
timing — employer instability, a tenure length that historically precedes moves, public
signals of openness — and behave like any other signal row.

**Where it comes from:** professional-network and profile data via a people-search source
and an enrichment orchestrator (Clay or similar) — the same category of stack as customer
sourcing, filtered on skills, years of experience, languages, industry background, and
location instead of firmographics.

**Decay:** fit decays slowly; *availability* decays fast — good candidates leave the market
in weeks. If the account tracks candidate work in its `signal-library.md`, role-fit is a
standing attribute while any openness or instability overlay carries a short recency window;
weighting lives in the account's `context/scoring-model.md`.

---

## Why it works

Job boards sample only active searchers — a minority of the market, skewed away from people
whose employers fight to keep them. Outbound reaches the whole population, and it arrives
with the best cold offer in existence: meaningful work and money, personally relevant to the
recipient. Reply economics that would be fantasy in sales are routine in recruiting when the
targeting is right.

The efficiency mechanism is the same as the sales side: most of a recruiter's day is
sourcing and filtering, which is exactly the work the engine automates, leaving the human
for the part that actually persuades — the conversation. One recruiter running this machinery
covers the ground of several working manually, before counting the platform-seat costs a
manual team multiplies.

The limits: candidate outreach is personal in a way B2B outreach is not — a clumsy automated
touch damages employer brand with the exact population it targets; profile data overstates
and understates real skill in both directions, so the filter shortlists but cannot judge;
and messaging-channel automation rides platform terms-of-service risk that the account must
weigh deliberately.

---

## The build

1. **Write the profile like an ICP.** Requirements as filterable attributes: must-have
   skills, experience bands, languages, industry exposure, location. Separate hard
   requirements from preferences — the same discipline as
   `accounts/<slug>/context/icp-definition.md`, applied to a role.
2. **Source at scale.** Query the people-data source on the hard requirements. Err
   inclusive; the scoring pass narrows.
3. **Enrich and score.** Fill the preference attributes and rank — the logic of
   `motions/skills/icp-scoring/SKILL.md` with role-fit dimensions; weights and shortlist cutoffs
   belong to the account's `scoring-model.md`. Overlay timing signals where available.
4. **Human-review the shortlist.** A recruiter reads the top of the ranked list before
   anything sends. This is the judgment step automation cannot do, and it is cheap at
   shortlist size.
5. **Sequence with restraint.** Personalized first touches through a LinkedIn-automation
   tool (HeyReach or similar) or direct email, at conservative daily volumes ramped
   slowly — candidate channels punish volume harder than email does. Suppression applies:
   current employees, recent declines, and anyone in the account's `optouts.md`.
6. **Route replies to a human immediately.** From first response onward this is a
   relationship, not a sequence — the recruiter manages the pipeline exactly as an AE
   manages open conversations.

---

## The message frame

The first touch must prove the targeting was real: name the specific intersection of their
background that fits — the skill pair, the industry-plus-stack combination — so the reader
sees a person chose them for a reason. Then give the honest shape of the opportunity: the
problem the role owns, the team context, the range of what is on offer, without demanding
interest as the price of the details. The PVP standard translates directly from
the PVP standard (`foundations/pvp.md`): stripped of the ask, the message should still tell the candidate
something true and useful about their own market position. Never bait-and-switch a candidate
frame into a sales pitch; the reverse of this play is a scam.

---

## Measurement

- Sourcing precision: share of sourced profiles surviving recruiter review (low precision
  means the profile definition or the filters are wrong)
- Reply and screen-booking rates per role and per message variant — read with the funnel
  diagnostics from the account's `scoring-model.md` §8: low reply is the message, replies-but-no-screens is
  the role pitch or the targeting
- Pipeline velocity: days from role opening to shortlist, versus the manual baseline
- Quality through the funnel: interview pass rate of engine-sourced candidates versus
  board-sourced — the play's core claim, tested
- Cost per hire against the fully loaded manual-recruiting baseline

---

## When NOT to run it

- **Commodity or high-churn roles.** Where applicant volume is already abundant, sourcing
  outbound solves a problem the account does not have.
- **A weak or unclear offer.** Outbound amplifies the offer it carries; if the role,
  compensation, or employer story cannot survive a candidate's first question, fix that
  before scaling the outreach.
- **One-off hires.** The build pays back across repeated searches. For a single role, run
  the discipline manually.
- **Anywhere automation would impersonate care.** Fake-personalized candidate outreach at
  volume is employer-brand self-harm, and platform enforcement risk compounds it. If the
  team cannot staff the reply-handling, do not generate the replies.
