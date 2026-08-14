# accounts/ — the record library contract

One folder per account; an account is a kit instance and the repeating unit of this repo.
Form: Record library — the stamp is `_template/`, the catalog is `_index.md`, and every
record has the same internal shape.

## Reads / does / writes

- **Reads:** nothing on its own. A session enters through a named account's `ACCOUNT.md`,
  then only the files the task names (`foundations/principles.md`).
- **Does:** holds every account-specific fact in the repo — context (factory), outputs
  (product), brand, suppression, identity. Core holds mechanism; this folder holds facts.
- **Writes:** each account writes only inside itself. `_index.md` gets one line per account
  and status updates — a catalog line, never content.

## The rules that define the form

1. **A new account is a copy, never a blank page.** Copy `_template/` → `<slug>/`, fill
   `ACCOUNT.md`'s identity block, add the index row (`motions/skills/setup` Step 0 does all three).
   Never work inside `_template/` — editing the stamp corrupts every future account.
2. **`_index.md` is the declared source of truth** for what accounts exist: slug · tier ·
   status over `scaffolded → configured → live → paused`. It never describes an account's
   internals — it links down and stops.
3. **Accounts never read each other** (`foundations/principles.md` §2). Cross-account learning
   promotes a pattern into core, stripped of its facts — and the promoted pattern then
   reaches every deployment, while the facts stay put (`estate.md`).
   Upstream this folder holds the stamp and the catalog only; populated `<slug>/` folders
   live in the business OS that operates them.
4. **Records can recurse:** an account holds tracks (`context/tracks/`), campaigns
   (`outputs/campaigns/`), and its own factory/product split. Uniform shape across accounts
   is what keeps the library navigable.

## Human checks

- Before a send: the account's `optouts.md` and declared rosters were checked, and the
  principal named in `ACCOUNT.md` said yes.
- After setup: the index row exists and the tier label is deliberate.
- Anything that would edit `_template/`: stop — that is a product change, not account work.
