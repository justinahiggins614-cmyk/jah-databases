# Site limits and the preset workarounds

Manon ordered: stay within GitHub's site limits, with workarounds preset so the
project is always safe. These are the limits and what is already in place.

## The limits (GitHub)

| Limit | Value | Guard |
|---|---|---|
| Repo size (soft cap) | ~850 MB per repo | stop pushing at **800 MB** |
| Single file | < 100 MB | drip/guard scripts refuse > 90 MB files |
| GitHub Pages site | < 1 GB total | hub repo stays lean; data grows sideways |
| Git objects | prefer shallow, append-only chunks | never rewrite history to "make room" |

Manon's standing rule: growth goes **sideways** — new shard repos — never by
deleting real data. Only exact duplicate writes from a bug are ever repaired, by
re-IDing, never by losing records.

## Workarounds already preset

1. **Per-database data sharding** — every database keeps its archive under
   `data/<slug>/` (e.g. `data/patents/`, `data/wiki/shards/`). A database can
   be moved out without touching the others.
2. **Compact gz JSON-line indexes** — indexes are gzip-compressed,
   newline-delimited JSON (one record per line). ~millions of rows compress to
   tens of MB. No index file may exceed 90 MB; splits happen automatically.
3. **Lazy per-chunk loading** — database pages fetch only the index, then load
   record chunks on demand. A giant archive never renders everything at once
   (this also keeps Manon's phone fast).
4. **Deterministic generators** — record N is computable from its seed via
   `core/jahdb.js`. The million is *addressable* without storing every record;
   the archive stores indexes + chunks, and the generator fills the rest.
5. **Data shard repos** — when a database outgrows the main repo,
   `jah-databases-data-N` shard repos are created (public, Pages-enabled) and
   listed in the manifest's shard map. Same pattern already proven on the
   website projects (e.g. `signature-one-archive-shard-*`).
6. **`code/guard.py`** — exits non-zero if `data/` exceeds 800 MB or any single
   file under `data/` exceeds 90 MB. Drips run it before pushing.

## What "every file accessible" means within these limits

Every vendored archive index is a real, public, crawlable file under `/data/`
(listed in `/sitemap.xml`, fetchable with plain HTTP, CORS open). Full-record
detail texts that would exceed the repo cap stream invisibly from the project's
own shard data files — no login, no key, no off-site branding. AIs reading the
archives never hit a paywall, a 403, or a login screen.
