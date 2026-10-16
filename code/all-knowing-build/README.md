# All-Knowing Databases build (PHASE N)

The master omniscient index of the JAH Databases network — one database
indexing every database (slug, name, scope, record counts, key records,
AI archivist, generator), plus its Signature edition carrying the original
Signature knowledge-organization framework.

## Regen (keeps the index in sync with the manifest)

```sh
cd ~/workspace/jah-databases
python3 code/all-knowing-build/build.py
python3 code/restamp_counts.py
```

The build is **deterministic and idempotent**: every database in
`data/manifest.json` becomes exactly one record per edition, in manifest
order, with sequential IDs (`JAH-AK-%06d` / `JAH-AKS-%06d`). Re-running
regenerates everything from the current manifest — new databases appear as
new records, record counts refresh, manifest/api.json entries are upserted
(not duplicated).

## Files

- `build.py` — the builder (records, demos, shard chunks, pages, upserts).
- `themes.py` — the Signature theme taxonomy: `theme_of(manifest_entry)`
  maps a database to exactly one browse theme via ordered first-match
  keyword rules over the slug (name tokens as fallback). Deterministic —
  the same manifest always yields the same browse groups.

## Edge cases (deterministic)

- **Duplicate database names** (the manifest has a few, e.g. two slugs
  named "Public Movies Database"): the record title is disambiguated as
  `Name [slug]` (Signature edition: `Name [slug] (Signature Edition)`),
  so every database still becomes exactly one record per edition.
- **Banned strings in sampled key-record titles** (build canon: no
  Facebook references): offending titles are skipped during sampling;
  the record is still built with the remaining titles.

## What a run does

1. Collision-checks the `all-knowing-databases` /
   `all-knowing-databases-signature` slugs and the `JAH-AK-` / `JAH-AKS-`
   ID prefixes against the manifest.
2. Samples up to 6 key-record titles from each database's own light index
   (best effort; unresolved indexes yield an empty list, never a failure).
3. Builds full-canon records (description, scope, how-it-works, key points,
   requirements, standards, citations, key_records, runnable stdlib demo),
   whole-system dedupe-gated via `code/dedupe_gate.py`.
4. Rewrites the shard data (`jah-databases-data-1/data/<slug>/index.jsonl.gz`
   + 100-record `chunks/chunk-NNNN.jsonl.gz`), the `db/<slug>/index.html`
   pages + `gen-<slug>.js` generators (template family + sweep-db-pages.py),
   and upserts the manifest/api.json entries.
