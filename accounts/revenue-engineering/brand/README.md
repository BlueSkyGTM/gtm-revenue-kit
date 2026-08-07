# brand/ — [Account name]

The account's voice and belief layer: how it sounds, what it stands against, what it sells.
These are the files an operator feels immediately, and the ones the copy linter enforces
mechanically.

**Status: empty slots.** The **branding lab** skill fills this folder through an interview.
Until that skill ships, these files can be written by hand — the contract below is what
they must contain either way.

## The slots

| File | Holds | Read by |
|---|---|---|
| `voice.md` | how this account writes: rhythm, vocabulary, banned words and constructions, the mechanical copy rules | `tools/lint_copy.py`, every copy skill |
| `brand-psychology.md` | beliefs, symbols, the enemy, the narrative the buyer is inside | `signal-to-sequence`, positioning work |
| `offer-map.md` | what is sold, to whom, what it promises, what it explicitly does not | `account-research`, `reply-handling` |

## The contract with `context/`

**The brand layer feeds the context files; it never duplicates them.** One home per fact
(`docs/isolation.md` §5):

- `brand/offer-map.md` holds the offer's *promise and shape*. Prices, if this account keeps
  them in the repo at all, live in one file and are pointed at, not restated.
- `brand/brand-psychology.md` holds beliefs and narrative. The buyer's *firmographics* stay
  in `context/icp-definition.md`; the buyer's *worldview* lives here.
- `brand/voice.md` holds mechanical rules. Strategic positioning — pillars, proof, what we
  never claim — stays in `context/positioning.md`.

When the two would overlap, the context file wins on facts and the brand file wins on
expression.

## The standard these outputs are held to

Copy built from this layer still passes the kit's own bar (`docs/standards.md`): a first
touch teaches the prospect something about their own business with the ask removed. A voice
file that produces charming copy with nothing in it has failed, not succeeded.
