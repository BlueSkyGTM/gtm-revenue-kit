# practice/context/ — the GTM factory

**Configured once, read every run.** This is the stable half of the practice workspace: who
we sell to, how we position, what a signal means, what things cost. `../outputs/` is the
other half — new every run.

**Generated output never writes here.** Promotion from `outputs/` into `context/` requires a
human cut, and a promoted field carries a provenance marker (`[inferred: …]` or
`[mcp: tool YYYY-MM-DD]`). That rule is the whole reason the two folders are separate:
without it, last run's guess becomes next run's ground truth.

Load the file the task names, never the folder. `../CONTEXT.md` routes.

## Two audiences, paired files

Most of this shelf exists twice — once for the SMB motion, once for the white-label
(bookkeeper-to-bookkeeper) motion. **The `-white-label` suffix is the audience, and mixing
the pair produces copy aimed at nobody.**

| Subject | SMB | White-label |
|---|---|---|
| Who we sell to | `icp-definition.md` | `context/tracks/white-label/icp-definition.md` |
| How we position | `positioning.md` | `context/tracks/white-label/positioning.md` |
| What we say | `messaging-house.md` | `context/tracks/white-label/messaging-house.md` |
| Who else is out there | `competitor-radar.md` | `context/tracks/white-label/competitor-radar.md` |

## Single-home files

| File | It answers |
|---|---|
| `profile.md` | The firm itself — what it is, what it does, what it will not do |
| `scoring-model.md` | **The one scoring authority.** Both fit scores, the routing matrix, offer eligibility, and the calibration log. A second scorer anywhere else is a rule violation |
| `signal-library.md` | What each signal means, how it decays, and which are dated |
| `pricing-strategy.md` | Every price and the reasoning under it, including the migration block and the evidence ladder |
| `personas/` | The people inside the ICP |

## Rules for this folder

- **Copy Rules live in `positioning.md`** and are enforced mechanically by
  `../web/lint_copy.py` on anything in `web/`. No em dashes, no banned vocabulary, dollars
  never percentages, verified numbers only.
- Unverified numbers do not enter copy. `[UNTIMED]` and `[pending the principal]` are real
  markers, not placeholders to quietly fill.
- When a fact here changes, the calibration log in `scoring-model.md` §8 records why.
