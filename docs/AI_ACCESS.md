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
> It lists all 37 databases with page URLs and index file URLs.
> Fetch `api.json` at the same base for the machine-readable catalog.
> Every `.gz` index is gzip-compressed newline-delimited JSON, one record per line.
> Per-record pages: `/db/<slug>/?record=<id>`. No key or login is ever needed.

## Root discovery files

- `/robots.txt` — all crawlers allowed, sitemap declared
- `/sitemap.xml` — every database page and every data file
- `/llms.txt` — llmstxt.org-style map for LLMs
- `/api.json` — machine-readable catalog of all 37 databases
- `/data/manifest.json` — the database catalog itself
