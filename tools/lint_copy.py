#!/usr/bin/env python3
"""lint_copy.py - enforce an account's mechanical copy rules on its outbound surfaces.

Core carries the mechanism and a set of conservative defaults. Every rule an account
actually cares about is read from that account's brand file:

    accounts/<slug>/brand/voice.md

inside a fenced block tagged ``copy-rules``. See tools/README.md for the format.

Usage:
    python tools/lint_copy.py --account <slug> [path ...]
    python tools/lint_copy.py --account <slug> --rules

With no paths, the files listed under ``paths:`` in the account's config are linted,
resolved relative to the account folder. Paths given on the command line are resolved
relative to the current directory and may be globs.

Exit codes: 0 clean, 1 violations found, 2 usage or configuration error.

Standard library only, on purpose. This runs as a gate.
"""
import argparse
import glob
import html
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CONFIG_FENCE = "copy-rules"

# Conservative core defaults. They encode the failures that are wrong in any voice:
# the two dashes and the emoji that mark machine-written copy. Everything stylistic
# (semicolons, percentages, attribution) is off until an account turns it on.
DEFAULTS = {
    "banned_characters": ["U+2014", "U+2013"],
    "banned_words": [
        "delve", "leverage", "elevate", "streamline", "robust", "seamless", "unlock",
        "empower", "navigate", "landscape", "realm", "tapestry", "testament",
        "in today's", "fast-paced", "at the end of the day", "it's worth noting",
        "rest assured", "game-changer", "cutting-edge", "when it comes to",
        "that said", "moreover", "furthermore", "additionally", "crucial", "vital",
        "pivotal", "myriad", "plethora", "not just", "whether you're",
    ],
    "allow_emoji": False,
    "require_dollars_not_percentages": False,
    "attributed_claim_terms": [],
    "attribution_cues": [],
    "attribution_exemptions": [],
    "paths": [],
    "js_paths": [],
}

LIST_KEYS = {k for k, v in DEFAULTS.items() if isinstance(v, list)}
BOOL_KEYS = {k for k, v in DEFAULTS.items() if isinstance(v, bool)}

CHAR_NAMES = {0x2014: "em dash", 0x2013: "en dash", 0x3B: "semicolon",
              0x2026: "ellipsis", 0x201C: "curly quote", 0x201D: "curly quote"}

# Real emoji only. Typographic arrows (U+2190-U+21FF) are UI affordances such as
# down/left arrows in a nav, not emoji, so they are deliberately not matched.
EMOJI = re.compile(
    "[\U0001F300-\U0001FAFF\U0001F1E6-\U0001F1FF\U00002700-\U000027BF"
    "\U00002600-\U000026FF\U0000FE0F]"
)

TRUE = {"true", "yes", "on", "1"}
FALSE = {"false", "no", "off", "0"}


# ---------------------------------------------------------------- configuration

class ConfigError(Exception):
    pass


def parse_rules_block(text):
    """Parse the simple key/value + list format used inside the copy-rules fence.

    Scalars are ``key: value``. Lists are ``key:`` followed by ``- item`` lines.
    A line whose first non-space character is ``#`` is a comment.
    """
    rules = {}
    current = None
    for lineno, raw in enumerate(text.splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("-"):
            if current is None:
                raise ConfigError(f"line {lineno}: list item before any key: {line!r}")
            item = line[1:].strip()
            if len(item) >= 2 and item[0] == item[-1] and item[0] in "\"'":
                item = item[1:-1]
            if item:
                rules[current].append(item)
            continue
        if ":" not in line:
            raise ConfigError(f"line {lineno}: expected 'key: value' or '- item', got {line!r}")
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        if value == "":
            rules[key] = []
            current = key
        else:
            rules[key] = value
            current = None
    return rules


def extract_rules_block(voice_text):
    """Return the body of the ```copy-rules fence, or None if the file has none."""
    pattern = re.compile(
        r"^[ \t]*```+[ \t]*" + CONFIG_FENCE + r"[ \t]*\n(.*?)^[ \t]*```+[ \t]*$",
        re.S | re.M,
    )
    matches = pattern.findall(voice_text)
    if len(matches) > 1:
        raise ConfigError(
            f"{len(matches)} ```{CONFIG_FENCE} blocks found. One home per fact: keep exactly one."
        )
    return matches[0] if matches else None


def decode_char(token):
    """Accept a literal character or a U+XXXX code point."""
    token = token.strip()
    if re.fullmatch(r"[Uu]\+[0-9a-fA-F]{4,6}", token):
        return chr(int(token[2:], 16))
    if len(token) == 1:
        return token
    raise ConfigError(f"banned_characters entry must be one character or U+XXXX, got {token!r}")


def coerce_bool(key, value):
    if isinstance(value, bool):
        return value
    text = str(value).strip().lower()
    if text in TRUE:
        return True
    if text in FALSE:
        return False
    raise ConfigError(f"{key}: expected true or false, got {value!r}")


def resolve_config(raw):
    """Merge parsed account rules over the core defaults.

    Every list key also accepts ``<key>_add`` and ``<key>_remove`` so an account can
    extend the defaults without restating them. One home per fact: if an account only
    wants two extra banned words, it writes two lines, not the whole list.
    """
    config = {k: (list(v) if isinstance(v, list) else v) for k, v in DEFAULTS.items()}
    known = set(DEFAULTS) | {f"{k}_add" for k in LIST_KEYS} | {f"{k}_remove" for k in LIST_KEYS}

    unknown = sorted(set(raw) - known)
    if unknown:
        raise ConfigError("unknown key(s) in copy-rules block: " + ", ".join(unknown))

    for key in LIST_KEYS:
        if key in raw:
            if not isinstance(raw[key], list):
                raise ConfigError(f"{key}: expected a list of '- item' lines")
            config[key] = list(raw[key])
        for item in raw.get(f"{key}_add", []) or []:
            if item not in config[key]:
                config[key].append(item)
        for item in raw.get(f"{key}_remove", []) or []:
            config[key] = [x for x in config[key] if x != item]

    for key in BOOL_KEYS:
        if key in raw:
            config[key] = coerce_bool(key, raw[key])

    config["banned_characters"] = [decode_char(c) for c in config["banned_characters"]]
    config["banned_words"] = [w.lower() for w in config["banned_words"]]
    config["attributed_claim_terms"] = [t.lower() for t in config["attributed_claim_terms"]]
    config["attribution_cues"] = [c.lower() for c in config["attribution_cues"]]
    config["attribution_exemptions"] = [e.lower() for e in config["attribution_exemptions"]]
    return config


def load_account_config(slug):
    """Return (config, account_dir, note). The note explains where the rules came from."""
    account_dir = REPO_ROOT / "accounts" / slug
    if not account_dir.is_dir():
        raise ConfigError(
            f"no account '{slug}' at {account_dir}. "
            f"Copy accounts/_template to accounts/{slug} first."
        )
    voice = account_dir / "brand" / "voice.md"
    if not voice.exists():
        return resolve_config({}), account_dir, f"core defaults ({voice} not present)"
    block = extract_rules_block(voice.read_text(encoding="utf-8"))
    if block is None:
        return resolve_config({}), account_dir, f"core defaults (no ```{CONFIG_FENCE} block in {voice})"
    return resolve_config(parse_rules_block(block)), account_dir, str(voice)


# ------------------------------------------------------------------- extraction

def visible_text(raw):
    """Return only what a reader sees in a markup file."""
    text = re.sub(r"<!--.*?-->", " ", raw, flags=re.S)
    text = re.sub(r"<style\b.*?</style>", " ", text, flags=re.S | re.I)
    text = re.sub(r"<script\b.*?</script>", " ", text, flags=re.S | re.I)
    text = re.sub(r"<head\b.*?</head>", " ", text, flags=re.S | re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    text = html.unescape(text)
    return re.sub(r"\s+", " ", text).strip()


def js_string_text(raw):
    """Visible copy for a JS-built page: markup prose plus every JS string literal.

    Literals are joined in source order, \\uXXXX escapes decoded, then tags stripped
    the same way as markup. Use this for pages whose copy lives in script strings,
    where stripping <script> would blind the linter to nearly all the prose.
    """
    markup = visible_text(raw)
    script = " ".join(re.findall(r"<script\b.*?</script>", raw, flags=re.S | re.I))
    script = re.sub(r"//[^\n]*", " ", script)          # line comments are not copy
    literals = re.findall(r"'((?:[^'\\]|\\.)*)'", script)
    literals += re.findall(r'"((?:[^"\\]|\\.)*)"', script)
    joined = " ".join(literals)
    joined = re.sub(r"\\u([0-9a-fA-F]{4})", lambda m: chr(int(m.group(1), 16)), joined)
    joined = joined.replace("\\'", "'").replace('\\"', '"')
    joined = re.sub(r"<[^>]+>", " ", joined)
    return re.sub(r"\s+", " ", markup + " " + joined).strip()


def plain_text(raw):
    """Markdown and plain text: only HTML comments are invisible to the reader."""
    text = re.sub(r"<!--.*?-->", " ", raw, flags=re.S)
    return re.sub(r"\s+", " ", text).strip()


def extractor_for(path, js_patterns, account_dir):
    suffix = path.suffix.lower()
    for pattern in js_patterns:
        if path in set(resolve_pattern(pattern, account_dir)):
            return js_string_text
    if suffix in (".html", ".htm", ".xhtml"):
        return visible_text
    return plain_text


# ---------------------------------------------------------------------- linting

def word_pattern(term):
    """Word-boundary match that still works for phrases and apostrophes."""
    prefix = r"\b" if term[:1].isalnum() else ""
    suffix = r"\b" if term[-1:].isalnum() else ""
    return prefix + re.escape(term) + suffix


def snippet(prose, index, width=42):
    return "..." + prose[max(0, index - width):index + width] + "..."


def lint(path, config, text_fn):
    prose = text_fn(path.read_text(encoding="utf-8"))
    lower = prose.lower()
    errors = []

    for ch in config["banned_characters"]:
        label = CHAR_NAMES.get(ord(ch), f"character U+{ord(ch):04X}")
        for m in re.finditer(re.escape(ch), prose):
            errors.append(f"{label}: {snippet(prose, m.start())}")

    for word in config["banned_words"]:
        for m in re.finditer(word_pattern(word), lower):
            errors.append(f"banned vocabulary '{word}': {snippet(prose, m.start(), 40)}")

    if not config["allow_emoji"]:
        for m in EMOJI.finditer(prose):
            errors.append(f"emoji/symbol: {m.group()!r}")

    if config["require_dollars_not_percentages"]:
        for m in re.finditer(r"\d+\s*%|\bpercent\b", lower):
            errors.append(f"percentage instead of dollars: {snippet(prose, m.start(), 40)}")

    # Every sentence naming a third party's behaviour must carry an attribution cue,
    # so the copy reports what was observed rather than asserting it about the reader.
    terms = config["attributed_claim_terms"]
    if terms:
        cues = config["attribution_cues"]
        exemptions = config["attribution_exemptions"]
        for sentence in re.split(r"(?<=[.!?])\s+", prose):
            s = sentence.lower()
            if any(term in s for term in terms):
                if not any(cue in s for cue in cues) and not any(ok in s for ok in exemptions):
                    errors.append(f"unattributed claim: {sentence.strip()}")

    return errors


# -------------------------------------------------------------------- file sets

def resolve_pattern(pattern, base):
    """Resolve one path or glob against a base directory. Returns sorted Paths."""
    candidate = Path(pattern)
    if not candidate.is_absolute():
        candidate = base / pattern
    matches = [Path(p) for p in glob.glob(str(candidate), recursive=True)]
    return sorted({m.resolve() for m in matches if m.is_file()})


def collect_targets(cli_paths, config, account_dir):
    patterns = cli_paths if cli_paths else config["paths"]
    base = Path.cwd() if cli_paths else account_dir
    targets, missing = [], []
    for pattern in patterns:
        found = resolve_pattern(pattern, base)
        if found:
            targets.extend(found)
        else:
            missing.append(pattern)
    seen, ordered = set(), []
    for path in targets:
        if path not in seen:
            seen.add(path)
            ordered.append(path)
    return ordered, missing


# ------------------------------------------------------------------------- main

def print_rules(config, source):
    print(f"Rules for this run, from: {source}\n")
    for key in sorted(config):
        value = config[key]
        if isinstance(value, list):
            if key == "banned_characters":
                value = [f"U+{ord(c):04X}" for c in value]
            print(f"  {key} ({len(value)}):")
            for item in value:
                print(f"    - {item}")
        else:
            print(f"  {key}: {value}")


def main(argv=None):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

    parser = argparse.ArgumentParser(
        description="Lint an account's outbound copy against its own mechanical rules.")
    parser.add_argument("--account", required=True, metavar="SLUG",
                        help="account slug under accounts/")
    parser.add_argument("paths", nargs="*",
                        help="files or globs to lint. Defaults to the account's 'paths:' config.")
    parser.add_argument("--rules", action="store_true",
                        help="print the resolved rules and exit without linting")
    args = parser.parse_args(argv)

    try:
        config, account_dir, source = load_account_config(args.account)
    except ConfigError as exc:
        print(f"CONFIG ERROR {exc}")
        return 2

    if args.rules:
        print_rules(config, source)
        return 0

    targets, missing = collect_targets(args.paths, config, account_dir)

    if not targets and not missing:
        print(f"No files to lint for account '{args.account}'.")
        print(f"Pass paths on the command line, or add a 'paths:' list to the "
              f"```{CONFIG_FENCE} block in {account_dir / 'brand' / 'voice.md'}.")
        return 2

    print(f"account: {args.account}   rules: {source}\n")

    total = len(missing)
    for pattern in missing:
        print(f"MISSING {pattern}")

    js_patterns = config["js_paths"]
    for path in targets:
        try:
            errors = lint(path, config, extractor_for(path, js_patterns, account_dir))
        except OSError as exc:
            print(f"UNREADABLE {path}: {exc}")
            total += 1
            continue
        try:
            shown = path.relative_to(REPO_ROOT)
        except ValueError:
            shown = path
        if errors:
            print(f"\n=== {shown}: {len(errors)} violation(s) ===")
            for error in errors:
                print(f"  ERROR {error}")
            total += len(errors)
        else:
            print(f"PASS {shown}")

    if total:
        print(f"\n{total} violation(s). Copy rules are a gate, not a review.")
        return 1
    print(f"\nAll files pass the copy rules for account '{args.account}'.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
