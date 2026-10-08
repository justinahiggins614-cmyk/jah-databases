# JAH Data Bases — Project Three

37 connected databases, 37 boundless generators, 37 archive-aware AIs.
Property of Justin Addam Higgins (JAH).

## What this is

A brand-new STANDALONE project. Each of the 37 original websites keeps its own
million-record archive; this network turns each archive into a dedicated,
searchable database with:

- **The permanent archive** — the same records, same data, browsable fast
  (collapsible groups, lazy loading, never a full DOM dump).
- **A boundless generator** — produces NEW records in the archive's exact
  genre, schema, and output format. Deterministic: same seed + version ⇒ same
  record. Every record passes an independent validator before acceptance.
- **An archive-aware AI** — one per database, on-device Standard 1.0 (no key),
  cloud Apex backend when configured. It searches the archive, explains
  records, and drives the generator. Fresh session per user.
- **Validation + drift control** — schema checks, independent re-verification,
  and duplicate checks against archive samples. Chat output never enters the
  archive automatically; filing is deliberate.
- **Cross-database generation** — every generator can sample the other 36
  databases (`JAHDB.sampleOther`) and fold themes into its own genre.

The original 37 websites are NOT linked from here and this project is NOT
linked from them. Data is shared invisibly (same data files); navigation is
separate.

## Layout

- `index.html` — hub front door, 37 database cards.
- `data/manifest.json` — the 37-database registry (slug, name, source repo,
  index/chunk paths, id prefix, AI name, status).
- `core/jahdb.js` — shared framework (manifest, PRNG, emblems, gz fetch,
  generator registry, cross-db sampling, sessions, archive-aware AI).
- `core/standard-1.0.js`, `core/guide-conv.js`, `core/apex-2.0.js` — the
  Signature AI engines (his property, reused here).
- `db/<slug>/index.html` — one page per database (Archive / Generator /
  AI Chat / About tabs).
- `db/<slug>/gen-<slug>.js` — that database's generator; registers with
  `JAHDB.registerGenerator`.

## Generator contract

Each `gen-<slug>.js` registers:

```js
JAHDB.registerGenerator('<slug>', {
  version: 'jahdb-<slug>-1.0',
  generate(seed, opts, rnd) -> record,   // deterministic
  validate(record) -> {ok, errors[]},     // schema + independent re-verification
  driftCheck(record, archiveSample) -> {ok, errors[]},  // duplicates / contradictions
  themedGenerate(seed, opts, rnd, themeSamples) -> record  // optional cross-db
});
```

Harness-test every generator with node before shipping:
`JAHDB.batchGenerate('<slug>', 40, <seed>)` must yield 0 failures, determinism
must hold (same seed twice ⇒ identical record), and the independent verifier
must confirm every solution.

## Adding a database

1. Add the entry to `data/manifest.json` (status `building` → `live` when done).
2. Write `db/<slug>/gen-<slug>.js` per the contract above; harness-test it.
3. Copy `db/equations/index.html` as the page template; swap names, BASE URL,
   index/chunk patterns, groups, and schema text.
4. Verify the page in a real browser: archive loads, generator produces
   validated records, chat answers, no console errors.

## Rules (standing)

- Never change the look without his confirmation; invisible plumbing is fine.
- No large archives on main tabs; A–Z/groups always collapsible + lazy.
- Never invent archive records as existing — generated vs stored is always labeled.
- No API key required from users, ever.
