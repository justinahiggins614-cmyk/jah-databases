# Pagination Contract — JAH Databases registry (Lane B, Fix 2)

**Status: LIVE — deployed on GitHub Pages (merged 2026-11-12).** The page files live in
`data/pages/` (631 pages, 100 entries each).

## Why this exists

The outside AI's "400-database exhaustive-search ceiling" is its own
rounding/behavior, most likely its own context/behavior limit after ~400
entries (see `../STEP-0-1-VERIFICATION.md` §1b) — the paginated registry
itself imposes no 400-database ceiling. But be clear: the in-browser search DOES cap index
search — `core/jahdb-search.js:15-17` caps it at Quick 12 / Deep 40 /
Exhaustive 400 database indexes per search. This contract does not claim to
remove that cap. What it does is make an exhaustive pass *feasible for a
text-fetch reader* anyway: instead of one 50.8 MB manifest or one 444-entry
`llms.txt`, the reader fetches small plain files one at a time, each pointing
at the next, and can stop and resume at any point without losing its place —
the paginated registry is the path to full coverage.

## The contract (v1)

| Rule | Value |
|---|---|
| Ordering | **Slug ascending, byte order** (plain Python `sorted()` on the slug string). Stable: the same source registry always yields the same pages. A new database inserted later shifts later pages — pages are a snapshot, stamped with the source registry fingerprint (see below). |
| Page size | **100 entries per page**, except the last page (47 entries). |
| Page count | **631 pages** for 63,047 entries at build time (630 × 100 + 47). |
| Page identity | `pages/page-NNN.json`, NNN zero-padded (001–631). |
| Cursor | The cursor IS the page number: `page:<n>`. No server, no session, no expiry. To resume, fetch `page-<n>.json` for the next unprocessed page. The cursor is printed in every page as `next_cursor` (null on the last page). |
| Entry format | Each entry: `{"slug", "name", "record_count", "shard"}` — `shard` is the manifest-shard file (`shards/manifest-shard-NNN.json`) holding the entry's full manifest record. Nothing else is in the entry: the page is an index, the shard is the record. |
| Totals | Every page carries `total_items` (63,047), `total_pages` (631), `page_size` (100), `items_on_page`, and `remaining_after_this_page` so the reader always knows how far along it is. |
| Navigation | Every page carries `prev_page` and `next_page` (file names, null at the ends) AND `next_cursor`. A reader needs only the current page to find the next one. |
| Source stamp | Every page carries `source_registry_sha256` (the registry.json source fingerprint) and `generated_date`, so a reader can tell whether the pages match the registry it is also reading. If the manifest moves, regenerate pages; do not mix snapshots. |

## Page file format (exact)

```json
{
  "page": 1,
  "page_size": 100,
  "total_items": 63047,
  "total_pages": 631,
  "items_on_page": 100,
  "first_slug": "15-minute-cities",
  "last_slug": "ai-build-...",
  "prev_page": null,
  "next_page": "page-002.json",
  "next_cursor": "page:2",
  "remaining_after_this_page": 62947,
  "source_registry_sha256": "<sha256 of source manifest>",
  "generated_date": "2026-11-02",
  "entries": [
    {"slug": "15-minute-cities", "name": "Signature 15 Minute Cities Database",
     "record_count": 98, "shard": "shards/manifest-shard-001.json"},
    ...
  ]
}
```

Notes:

- Files are compact JSON (no pretty-printing) — plain text, no JavaScript,
  no decompression. A text-fetch reader can read any single page directly.
- `record_count` may be `null` for entries whose manifest record carries
  `null` (57,188 api.json entries carry null; the manifest is the source of
  truth — the page copies the manifest value verbatim, it does not invent
  one). Do not treat null as zero.
- Page size is fixed at 100 by contract. A reader that wants fewer entries
  per fetch can still fetch a page and read only its first N entries; the
  cursor still advances a whole page. Do not invent a `?page_size=` parameter
  — there is no server.
- The last page's `next_page` and `next_cursor` are both `null`: that is the
  defined end-of-list signal. A reader that reaches a page with
  `next_cursor: null` has the complete set.

## How a text-fetch AI does an exhaustive pass

1. Fetch `pages/page-001.json`. Note `total_items` (63,047) and
   `total_pages` (631).
2. Record the 100 slugs. Fetch `next_page` (`page-002.json`). Repeat.
3. If interrupted: the last page fully read gives `next_cursor`, e.g.
   `page:315`. Fetch `page-315.json` and continue — no re-reading, no gaps.
4. Done when a page has `next_cursor: null`. Verify: slugs collected =
   `total_items`, all unique.

## Resume points (verified)

- Resume from **page 315** (mid-point): pages 315–631 complete the set
  started by pages 1–314 with no gaps and no dupes (see `verify_pagination.py`).
- Independent re-check resumes from **page 500** instead and reaches the
  same result (see LANE-REPORT.md, Validation section).

## Honest limits

- **The 400 ceiling is not ours.** If an outside AI stops after ~400
  entries, pagination gives it a resumable path, but nothing in this
  contract can force a reader to keep going. The fix removes the *excuse*
  (one giant file), not the reader's own limit.
- Pages are a **snapshot**: they match the manifest as measured at build
  time (50,845,023 bytes, sha256 in `registry.json`). If the manifest
  grows, pages go stale until regenerated — the `source_registry_sha256`
  on every page is how a reader detects that.
- Page files are **not a server API**: there is no filtering, sorting, or
  search endpoint. A reader that wants a subset still walks pages (or uses
  `resolve.py` for a single known slug).
- The `.gz` index files behind `raw_index_url` remain gzip-compressed
  (Step 1c): pagination solves *finding* every database, not *reading*
  gzipped records. That is a different fix's job.
