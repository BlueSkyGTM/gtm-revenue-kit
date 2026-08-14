# outputs/ — [Account name]

The **product** layer: new every run, dated, never edited in place to mean something else.
`context/` is the factory that produced it.

## Shape

```
outputs/
├── account-research/     ← one brief per researched account
├── campaigns/            ← one folder per campaign
│   └── YYYY-MM-DD-[name]/
│       ├── brief.md      ← audience, angle, decision rule
│       ├── sequences.md  ← the copy, as sent
│       └── results.md    ← what came back
├── audits/               ← red-teams, validation passes, reviews
├── lists/                ← gitignored. Raw contact data never enters git.
└── YYYY-MM-DD-[type]-[name].md    ← everything else, dated
```

## Rules

- **Dated names, always.** A file whose staleness you cannot see without opening it will be
  quoted forward as current.
- **A durable fact does not belong here.** If a research pass turns up something true about
  the *buyer type* rather than one company, it belongs in `context/` — the output records
  what happened; the context records what is now known.
- **Never bulk-load this folder** (`foundations/principles.md`). Read the dated file the task names.
- **Raw contact data never enters git.** `lists/` and `*.csv` are gitignored by pattern;
  the pattern is a backstop, not permission to try.
- **Outputs are evidence.** When one turns out to be wrong, annotate it in place with the
  correction and the date. Do not silently rewrite it — a run record that has been edited
  to look correct is worse than one that was wrong, because you can no longer tell which
  is which.
