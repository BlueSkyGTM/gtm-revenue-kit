# tools/ — account-agnostic scripts

Core scripts. They carry mechanism and a conservative default, and read every value that
could differ between accounts out of `accounts/<slug>/`. Standard library only: a gate that
needs an install step is a gate someone skips.

| Script | Does | Reads its rules from |
|---|---|---|
| `lint_copy.py` | checks outbound copy against the account's mechanical copy rules | `accounts/<slug>/brand/voice.md` |

---

# lint_copy.py

The mechanical half of the copy standard. `docs/standards.md` holds the judgment half — the
PVP test, whether a first touch teaches the reader anything — and no script can check that.
This checks the part that is decidable: banned vocabulary, the characters that mark
machine-written prose, emoji, and whatever else the account has decided it never says.

**It is a gate, not a review.** It exits non-zero on any violation, so it can sit in front of
a send, in a pre-commit hook, or in CI without further wiring.

## Usage

```bash
# Lint the files the account declared in its own config
python tools/lint_copy.py --account <slug>

# Lint specific files or globs instead (resolved from the current directory)
python tools/lint_copy.py --account <slug> accounts/<slug>/outputs/campaigns/**/*.md

# Show the rules that would apply, and where they came from, without linting
python tools/lint_copy.py --account <slug> --rules
```

`--account` is always required. There is no default account and there will not be one: a
linter that guesses which account's voice to enforce will eventually enforce the wrong one
quietly.

**Exit codes:** `0` clean · `1` violations found · `2` usage or configuration error (no such
account, malformed config, nothing to lint).

## What it reads

Per file type, the linter checks only what a reader would see:

| Extension | Treated as |
|---|---|
| `.html`, `.htm`, `.xhtml` | markup — tags, `<style>`, `<script>`, `<head>`, and comments stripped |
| anything listed under `js_paths` | markup **plus** every JS string literal, `\uXXXX` escapes decoded — for pages whose copy is built in script |
| everything else (`.md`, `.txt`) | prose as written, HTML comments stripped |

---

## How an account defines its rules

The rules live in a fenced block tagged `copy-rules` inside
`accounts/<slug>/brand/voice.md` — the file the brand layer already designates as the home
for mechanical copy rules. Prose around it is for humans; the block is for the linter. Keep
exactly one such block per file; two is a configuration error, because a rule with two homes
disagrees with itself within a month.

If the file or the block is absent, the linter runs on core defaults and says so. That is a
valid state, not a warning to silence — a new account is worth linting before its voice
interview happens.

### The format

Scalars are `key: value`. Lists are a bare `key:` followed by `- item` lines. A line whose
first non-space character is `#` is a comment. Quotes around a value are optional and are
stripped.

Every list key also accepts `<key>_add` and `<key>_remove`, so an account extends the core
defaults instead of restating them. Restating the whole list is allowed but rarely right: you
then own every future improvement to the default list by hand.

```copy-rules
# Words this account never uses, on top of the core list
banned_words_add:
  - synergy
  - circle back
  - reach out

# Core bans this, but this account's copy legitimately uses it
banned_words_remove:
  - navigate

# Core bans the em and en dash. This account also bans the semicolon in prose.
banned_characters_add:
  - ";"

# This account quantifies outcomes in money, never in percentages
require_dollars_not_percentages: true

# Claims about a third party's behaviour must report an observation,
# never assert it about the reader's own account
attributed_claim_terms:
  - the built in ai
  - the vendor
attribution_cues:
  - owners have
  - customers report
  - reviews report
attribution_exemptions:
  - no automation
  - without someone

# What gets linted when no paths are passed on the command line.
# Relative to accounts/<slug>/. Globs allowed, ** included.
paths:
  - outputs/campaigns/**/*.md
  - site/*.html

# Of those, the pages whose copy lives in JS string literals
js_paths:
  - site/calculator.html
```

### Every key

| Key | Type | Core default | Checks |
|---|---|---|---|
| `banned_characters` | list | `U+2014`, `U+2013` | each character, anywhere in visible prose. Write a literal character or a `U+XXXX` code point. |
| `banned_words` | list | 32 common tells (`delve`, `leverage`, `seamless`, `in today's`, …) | whole-word or whole-phrase match, case-insensitive |
| `allow_emoji` | bool | `false` | emoji and pictographic symbols. Typographic arrows are not matched — they are UI affordances, not emoji. |
| `require_dollars_not_percentages` | bool | `false` | flags `30%` and the word `percent` |
| `attributed_claim_terms` | list | empty | sentences containing one of these terms must also contain an `attribution_cues` entry or an `attribution_exemptions` entry |
| `attribution_cues` | list | empty | phrases that make a claim an attributed observation |
| `attribution_exemptions` | list | empty | phrases marking a sentence as a statement about the account's own service, so the attribution rule does not apply |
| `paths` | list | empty | files linted when none are passed on the command line |
| `js_paths` | list | empty | which of those get JS string-literal extraction |

Run `--rules` after editing. It prints the merged result, which is the fastest way to catch an
`_add` that silently duplicated an entry already in the default list.

### Why the defaults are set where they are

Core defaults ban only what is wrong in any voice: the em dash, the en dash, the emoji, and a
vocabulary list of tells that read as machine-written regardless of who is writing. Everything
stylistic — semicolons, dollars over percentages, attribution — ships **off**, because those
are voice decisions and core does not have a voice. An account turns them on.

This is the isolation rule doing its job (`docs/isolation.md`): the mechanism for "some claims
must be attributed" is core and identical everywhere; *which* claims, and what counts as
attribution, is a fact about one account and lives in that account's `brand/voice.md`. Two
accounts can hold opposite rules and both be correctly linted.

## Wiring it as a gate

Copy passes the linter before it is sent, not after. Two places worth putting it:

```bash
# Before a batch goes out, as the last step of campaign build
python tools/lint_copy.py --account <slug> || exit 1
```

```bash
# In CI or a pre-commit hook, for every configured account
for account in accounts/*/; do
  slug=$(basename "$account")
  [ "$slug" = "_template" ] && continue
  python tools/lint_copy.py --account "$slug" || fail=1
done
exit ${fail:-0}
```

A clean run is not a claim that the copy is good. It is a claim that the copy does not break
the rules this account wrote down. The bar in `docs/standards.md` is a separate pass, done by
a person or a model reading the message with the ask removed.
