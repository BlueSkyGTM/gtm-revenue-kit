# Playbook: LinkedIn & ABM (Channel Strategy)

*How to use LinkedIn as a precision channel — when to automate, who to target, and two
campaign architectures that treat the platform as what it is: a small number of high-value
shots, not a second email channel.*

---

## Trigger

Any of:
- Adding LinkedIn to an account's channel mix
- Connection requests are going out but acceptance or reply rates are poor
- The account's TAM is small and high-value enough that email volume is the wrong shape
- Executives at the account have large networks nobody is working

---

## First decision: automate or don't

One rule before any tooling: **if a profile has genuine organic traction — real inbound
leads from posting and presence — do not put automation on it.** The organic motion is worth
more than the automated one, and it is the one automation puts at risk. Automate the
profiles that have reach but no motion.

When automating, use a dedicated LinkedIn automation platform (tools in the HeyReach
category): sequenced connection requests, messages, profile visits, and InMails across many
seats, in the way a sending platform sequences email. Platform automation always operates
inside LinkedIn's tolerance rather than its rules — the risk level shifts with LinkedIn's
enforcement, so verify the current state before connecting an account, and treat which
profiles are enrolled as an account-level decision recorded in `ACCOUNT.md`.

---

## The channel's physics: a sniper's budget

LinkedIn allows each profile a small weekly budget of connection requests. That single
constraint defines the strategy: **email scales, LinkedIn aims.** Every request spent on an
inactive profile is budget burned for nothing — the message sits unread in an account its
owner abandoned.

So the core targeting rule: **contact only demonstrably active users.** The workable proxy is
network size — enrich each contact and filter for a high connection count. The reasoning: a
large network is not accidental; it indicates someone who deliberately built a presence and
is likely still logging in. The account sets its own floor in `context/scoring-model.md`
(with the common platform heuristic sitting around the level where the profile's connection
count stops being publicly precise), and this one filter typically multiplies reply rates by
itself.

The second consequence of the small budget: the *ask* has to be worth a shot. Plain pitches
waste the channel. The anchors that work are creative and specific:

- An interview for a research project
- A podcast invitation
- A micro-event, online or offline
- A visit or small gathering tied to their company or city

---

## Architecture 1: The recognition-asset ABM campaign

The pattern: manufacture a piece of industry recognition the target persona *wants to be in*,
then make outreach an invitation rather than a pitch.

**Preconditions — all three, or don't run it:** a small TAM, a high average deal size, and a
deeply understood ICP. This is a high-touch motion; its economics only work when each
converted prospect is worth a lot and the audience is small enough to treat individually.

**Mechanism:**

1. **Create the asset.** A ranked list, market research report, interview series, or similar
   recognition vehicle whose subjects are exactly the buying persona. The design insight is
   frank: the asset trades on professional pride — being featured in front of the industry's
   top companies is an offer the persona finds hard to refuse.
2. **Invite on LinkedIn first.** Two short touches: the invitation, then one elaboration of
   what the asset is and why they specifically fit. Personalized, no pitch — the ask is
   participation.
3. **Email only on LinkedIn non-response, anchored to the LinkedIn attempt.** The email
   opens by referencing the LinkedIn message ("not everyone is active there") — the anchor
   makes the second channel feel like diligence instead of a second cold touch. Two or three
   touches, ending with a clean, non-bitter break-up.
4. **Deliver the asset, then convert the relationship.** Participation (the interview, the
   feature) warms the prospect; a defined follow-up process turns the relationship into a
   sales conversation. The asset must actually ship — a recognition vehicle that never
   publishes poisons the well for every future campaign.

Sequence copy is written fresh per account against the account's brand files — the
architecture transfers; the words never do.

---

## Architecture 2: The executive-network campaign

The pattern: the account's executives already hold large first-degree networks, and a message
from a COO lands categorically better than the same message from an unknown SDR. This
campaign works those networks systematically without consuming executive time.

**Mechanism:**

1. **Export each executive's first-degree connections.** Name, company, and profile URL are
   enough as input.
2. **Enrich and segment in the orchestration platform.** Profile enrichment, email, role,
   geography, company size; tier the results against the account's ICP
   (`context/icp-definition.md`).
3. **Disqualify before anyone is touched.** Connect the CRM and cross-check: existing
   clients, named accounts, and open opportunities are removed; profile URLs are deduplicated
   across executives so a prospect connected to two of them is contacted once, by one. This
   step is where the campaign is won or lost — an executive pitching an existing client is
   the failure mode that ends the program.
4. **Record once, personalize at scale.** Each executive records a small number of short
   videos; a personalized-video tool (in the Vidyard category) produces per-prospect versions.
5. **Send from the executives' profiles via the automation platform; staff the inboxes
   centrally.** One SDR manages all executive inboxes through the automation platform's
   unified view, books the meetings, and makes follow-up calls explicitly "on behalf of"
   the executive — the borrowed authority survives the handoff when it is named honestly.

**The named risks:** executives will not triage inboxes (staff it or it fails), and the
disqualification pass in step 3 is mandatory, not best-effort. Suppression against
`accounts/<slug>/optouts.md` runs before any enrollment, as everywhere.

---

## Related

- `playbooks/channels/micro-lists.md` — the same high-touch economics applied to hand-sent
  1:1 outreach; the two playbooks share preconditions
- `playbooks/channels/cold-email.md` — the volume channel these architectures deliberately
  are not; also the anchor-email mechanics
- `workflows/tam-campaign.md` — people-finding and enrichment for the target lists
- `docs/standards.md` — the verification standard; a wrong personalization in a high-touch
  channel costs more than in any other
