# signals/ — the signal library contract

A record library whose records are signals, kept deliberately small: `schema.md` defines
the record, and this shelf holds only signals that pass the admission gate (a filled
"why it matters" with known provenance).

## Reads / does / writes

- **Reads:** `schema.md` — the record shape and the four dimensions.
- **Does:** holds core signal records: mechanism + backstory, zero numbers.
- **Writes:** one file per signal family as they are admitted. An account adopts a signal
  by copying the record into its own `context/signal-library.md` and assigning values
  there (principle 3).

## Why this shelf is empty right now — on purpose

The previous kit's signal set was discarded on the operator's decision: no backstory, no
entry. Records enter from three directions, in this order of expectation:

1. **The plays** — each of the 15 plays names its signal with the buying mechanism
   already stated; those graduate to records here as plays are adopted by an account.
2. **The operator's brief** — the second-brain workspace holds the improved TAM
   framework; its signal layer lands here as it is briefed in.
3. **New observation** — a signal proven in a live campaign writes its record with
   `operator-proven` provenance.

## Human check

Before admitting a record: is "why it matters" a mechanism (would survive being asked
*"so what?"* twice), or a restatement of the trigger? Restatements bounce.
