# tracks/ — one account, more than one buyer

A **track** is a second buyer with its own ICP, positioning, competitors, and copy, run by
the same account. Use one when the same operator sells two different things, or the same
thing to two audiences who do not share a pain.

**Delete this folder if the account has one buyer.** An empty tracks/ folder invites
someone to fill it.

## When a track is the right answer

| Situation | Track? |
|---|---|
| Same buyer, different signal fired | No — that is a segment, handled in `scoring-model.md` §5 |
| Same buyer, different message class | No — segment again |
| Different buyer entirely, different offer | **Yes** |
| Same offer, audience whose pain is unrelated | **Yes** |

The test: would the two share a competitor radar? If a competitor to one is irrelevant to
the other, they are tracks.

## Shape

```
context/tracks/<track-slug>/
├── icp-definition.md      ← who this track sells to
├── positioning.md         ← how it is framed for them
├── competitor-radar.md    ← who else they would consider
└── messaging.md           ← value prop → pillars → per-channel copy
```

The account's root `context/` files still hold what is true for the whole account —
`profile.md`, `signal-library.md`, `scoring-model.md`, `personas/`. A track overrides only
what differs, and states at the top of each file what it is overriding.

## The hard rule

**Never load two tracks in one session** (`docs/loading.md`). Their positioning disagrees
on purpose. Loaded together, they average into copy that fits neither buyer, and the
failure is invisible in the output — it just quietly underperforms.

## Channel conflict

If two tracks could reach the same organization from different angles — one selling to a
company directly, another selling to that company's advisor — say so in `ACCOUNT.md` and
define which side takes precedence. Reaching both at once is how one account competes with
itself.
