# How any AI reads every patent / file in JAH Databases

Everything in this project is **public and open**: no login, no API key, no fee.
Any AI (ChatGPT, Claude, Gemini, Groq, an open-source model — anything) and any
bot can read every database, every index, every record. `robots.txt` allows all
crawlers and CORS is `Access-Control-Allow-Origin: *` on every file.

Base URL: `https://justinahiggins614-cmyk.github.io/jah-databases`

## The 60-second path

1. Read the catalog: `/data/manifest.json` — every database, its slug, record kind, AI librarian name, ID prefix.
2. Pick a database and fetch its index file in `/data/<slug>/` (e.g. `/data/patents/patents.idx.json.gz`).
3. Read rows. `.gz` files are gzip-compressed newline-delimited JSON — one record per line.

## Finding a database without downloading the 50 MB manifest

- Start at `/data/registry/registry.json` — the paginated registry index (63,047 databases, 49 shards).
- Walk the pages: `/data/pages/page-001.json` through `/data/pages/page-631.json`, 100 databases per page (last page 47). Each page lists slugs and names plus `next_page` / `next_cursor`, so a reader can stop and resume.
- Need a database's full record? Each page entry names its shard (`shards/manifest-shard-NNN.json` under `/data/registry/`), which carries the complete manifest entry — fetch one shard (under 1 MB) instead of the whole manifest.
- The full files still exist — `/data/manifest.json` (50,845,023 bytes) and `/api.json` (39,221,262 bytes) — but you do not need them for discovery.

## Reading a compressed index (curl + python)

```bash
# download one index
curl -s https://justinahiggins614-cmyk.github.io/jah-databases/data/patents/patents.idx.json.gz -o patents.idx.json.gz

# read the first 3 records
python3 -c "
import gzip, json
with gzip.open('patents.idx.json.gz', 'rt') as fh:
    for i, line in enumerate(fh):
        if i == 3: break
        print(json.loads(line).keys())
"

# count all rows in an index
zcat patents.idx.json.gz | wc -l
```

## Reading the machine-readable catalog

`/api.json` lists every database with its page URL, index file URLs, record kind,
and row counts where available — built for AI agents to traverse programmatically:

```bash
curl -s https://justinahiggins614-cmyk.github.io/jah-databases/api.json | python3 -c "
import json, sys
d = json.load(sys.stdin)
for b in d['databases']:
    print(b['name'], '->', b['page_url'])
"
```

## Generating / re-deriving any record

`/core/jahdb.js` is the deterministic generator engine. Any record N in any
archive can be reproduced from its seed — the million-record archives are fully
addressable without storing every file. The JAHDB framework on each database page
(`db/<slug>/`) exposes the generators in the browser.

## Per-record deep links

Every database page supports `?record=<id>`:

```
https://justinahiggins614-cmyk.github.io/jah-databases/db/patents/?record=JAH-PAT-000123
https://justinahiggins614-cmyk.github.io/jah-databases/db/specs/?record=JAH-SPEC-000123
```

ID prefixes per database are in `/data/manifest.json` (`id_prefix`).

## ChatGPT-style instructions

> To read any JAH Data Base, paste this URL:
> `https://justinahiggins614-cmyk.github.io/jah-databases/llms.txt`
> It lists all 63047 databases with page URLs and index file URLs.
> (count re-stamped from data/manifest.json by code/restamp_counts.py)
> Fetch `api.json` at the same base for the machine-readable catalog.
> Every `.gz` index is gzip-compressed newline-delimited JSON, one record per line.
> Per-record pages: `/db/<slug>/?record=<id>`. No key or login is ever needed.

## Root discovery files

- `/robots.txt` — all crawlers allowed, sitemap declared
- `/sitemap.xml` — every database page and every data file
- `/llms.txt` — llmstxt.org-style map for LLMs
- `/api.json` — machine-readable catalog of all 63047 databases
- `/data/manifest.json` — the database catalog itself

## Record API (api/v1) — one record as ordinary JSON

- Record JSON: `/api/v1/record/<database-slug>/<record-id>.json`
- Citable URL: `/api/v1/record/<database-slug>/<record-id>` (same JSON, no extension) — cite it as `JAHDB/<database-slug>#<record-id>`.
- Every record JSON carries a `citation` block: `api_url`, `code`, `database`, `database_name`, `file`, `file_sha256`, `file_url`, `key`, `record_kind`, `record_url`, and a `version` pin (retrieval date + manifest database count).
- Example: `curl -s https://justinahiggins614-cmyk.github.io/jah-databases/api/v1/record/animal-vocal-communication/JAH-AVC-000001.json`
- Full endpoint contract: `/docs/api-v1-endpoint-contract.md`
- Coverage (2026-11-12): pilot — 160 records across 10 databases. Plain-text mirrors of the full indexes live beside every data-2 `.gz` file as `.jsonl`; the record API grows with the mirror rollout.
