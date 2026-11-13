# Fix 3 — Universal Read-Only API: Endpoint Contract v1

**Status: RE-ISSUED by Lane 2, 2026-11-12 (Manon-approved deploy
staging).** This re-issue replaces the pagination section with Lane B's
contract (see §Pagination) and points the base URL at the real Pages
host. Everything else is Lane C's contract unchanged. The static pilot
package implements this contract for 10 databases / 160 records and is
staged at `jah-databases/api/v1/` for deploy. The live Worker is
STAGED, NOT DEPLOYED (see `worker/DEPLOY-COMMANDS.md`).

**Date:** 2026-11-02 (Lane C) / re-issued 2026-11-12 (Lane 2).
**Version pin at re-issue:** manifest 63,047 databases
(`manifest.json` 50,845,023 bytes, sha256
`f23795d147b5a6e1e9ccd06c0aef6394690978f9eedf44e63ab610960d34a104`;
`api.json` 39,221,262 bytes; 57,188 `api.json` entries carry
`record_count: null` — manifest sum 12,349,330 is the source of
truth). Manifest count verified unchanged from the Lane C build
(63,047), so no regeneration for count reasons was needed; the package
was regenerated only for the real host + the Lane B pagination.

## Why this exists

Verified 2026-11-02: a text-fetch reader (e.g. an outside AI) **cannot**
read `.jsonl.gz` records — GitHub Pages serves them as
`Content-Type: application/gzip` with no `Content-Encoding`, and the reader
receives binary gzip bytes ("no extractable content"). The records exist;
only the transport hides them. This API returns the same records as
**ordinary readable JSON**, one record per response, so any text reader can
fetch and quote them.

## Relation to existing work — EXISTS / EXPAND (no rebuild)

| Existing work | Routing | Evidence |
|---|---|---|
| Paste A Wave 1 `ai-retrieval-api` pair (24 + 24 records) | **EXISTS** (conceptual design) | `~/workspace/hidden_files/ai-access-1000/wave1/ai-retrieval-api/` — records cover AI Discovery API, Database/File Lookup, Universal AI Query Endpoint, AI Retrieval Endpoint, Record-Based Retrieval (`JAH-ARAPI-000019`), Universal Database Gateway (`JAH-ARAPI-000020`). Those records DESCRIBE endpoints; they do not implement one. |
| This lane | **EXPAND** | Concrete v1 contract below + a working static implementation + verification. No record of the pair was rebuilt or altered. |
| Paste A Wave 1 `ai-citation-system` pair | **EXISTS** (conceptual design) | 24 + 24 records on citation standards. See `CITATION-FORMAT.md` for the concrete machine format this lane adds. |

## Base URL

- Live (Pages static location, staged 2026-11-12):
  `https://justinahiggins614-cmyk.github.io/jah-databases/api/v1`
  — the citation `api_url` values in the staged package use this host.
  The static files live in the hub repo at `jah-databases/api/v1/...`,
  so a reader can fetch any record as ordinary JSON with no server.
- Worker route (staged, NOT deployed): the same paths served by the
  `jah-api` Worker (host assigned at deploy, e.g.
  `https://jah-api.<subdomain>.workers.dev/api/v1/...`), which also
  adds the on-demand gunzip route for databases outside the pilot.
  The Worker host is an alternate serving route, not the citation host:
  citations keep pointing at the permanent Pages URL above.
- Static pilot (this package): `api/v1/...` file paths mirror the
  live paths exactly: `GET /api/v1/record/biofonics/JAH-BIOF-000001` ↔
  `api/v1/record/biofonics/JAH-BIOF-000001.json`.

## Endpoints (all GET, all read-only)

### 1. One record — `GET /api/v1/record/{slug}/{id}`

Returns one record as ordinary JSON. This is the core endpoint.

Response (200), `Content-Type: application/json`:

```json
{
  "api_version": "v1",
  "endpoint": "/api/v1/record/biofonics/JAH-BIOF-000001",
  "record": { "...the full record, verbatim, all fields..." },
  "citation": { "...see CITATION-FORMAT.md..." }
}
```

Rules:
- `record` is the FULL stored record, byte-identical (canonical JSON) to
  the record in the source `.gz` index. No summarising, no trimming, no
  field dropping. (Pilot: 160/160 byte-match — see `LANE-REPORT.md`.)
- `record.id`, `record.slug` always match the URL path. A mismatch is a
  server bug, not a client error.
- Unknown slug or unknown id → 404 (error format below), never an empty 200.
- Pilot slugs are served from the pre-generated files. Any other slug
  with the standard single-index layout (`data/{slug}/index.jsonl.gz`)
  is served by the Worker's on-demand gunzip route with the same
  envelope and citation. Databases with chunked indexes (e.g.
  equations) are not read by this route yet and return a 404 that
  says so.

### 2. One database — `GET /api/v1/databases/{slug}`

Metadata + record list pointer: name, record_kind, record_count, id_prefix,
file URL + file SHA-256, and the records-list endpoint. Static form in the
pilot: `api/v1/databases/{slug}/records.json`.

### 3. Database records (list) — `GET /api/v1/databases/{slug}/records`

Paginated list of record summaries `{id, title, code, key, url}`.
Pagination per §Pagination below. Static form returns all 16 on one page
(the pilot databases have 16 records each, below one page of 100).

### 4. Databases (list) — `GET /api/v1/databases`

Paginated list of database summaries `{slug, name, record_count,
record_kind}`. Pilot scope: the staged list covers the 10 pilot
databases on one page; the full list is 63,047 entries and lives in
the manifest / `api.json` and the Lane B sharded registry. The Worker
serving the full list is a later phase, not this deploy.

### 5. Search — `GET /api/v1/search?q={text}`

Full-text match over record titles (and, live, over descriptions/bodies).
Response: paginated `{id, title, slug, code, key, url}` matches, most
relevant first; `q` is required (empty `q` → the page reports that `q`
is required; a static host cannot return HTTP 400). Static form
(live since the L2 fix, 2026-11-12): `api/v1/search.html` with its
extensionless twin `api/v1/search` — the page matches in the reader's
browser over `api/v1/search-index.json`, the full 160-entry title index;
a text-only reader fetches `search-index.json` and matches titles
client-side. There is no server-side matching on GitHub Pages. Pilot
search covers the 10 pilot databases' titles only.

## Versioning

- Version is in the path: `/api/v1/...`. A breaking change ships as `/v2/`
  alongside `/v1/`; `/v1/` is never silently changed.
- Every response carries `"api_version": "v1"`.
- No version strings of the form `X.Y` appear anywhere in record content
  (network standing rule); the API version lives only in the path and the
  `api_version` field.

## Pagination (Lane B contract — re-issued 2026-11-12)

This section REPLACES Lane C's provisional pagination spec
(page_size default 25, opaque id/slug cursor). Lane B's Pagination
Contract (`lanes/b-sharding-pagination/PAGINATION-CONTRACT.md`) is the
standard for the whole network, and this API follows it exactly:

| Rule | Value |
|---|---|
| Ordering | Stable and documented per endpoint: records by id ascending; databases by slug ascending; search by relevance, ties by id ascending. |
| Page size | **100 entries per page, fixed.** There is no `page_size` parameter. A request that sends one gets a 400 (`bad_request`): the client must know its request was not honoured as written. |
| Cursor | The cursor IS the page number: **`page:<n>`**. No server session, no expiry. The cursor is printed in every page as `next_cursor` (null on the last page) and `prev_cursor` (null on the first). To resume, fetch the same endpoint with `cursor=page:<n>`. |
| Page identity | List endpoints are page-addressed: page 1 is the request with no `cursor` (or `cursor=page:1`). |
| Totals | Every paginated response carries `page`, `page_size` (100), `total_items`, `total_pages`, `items_on_page`, and `remaining_after_this_page`, so the reader always knows how far along it is. |
| Navigation | Every paginated response carries `prev_cursor` and `next_cursor` (null at the ends). A reader needs only the current page to find the next one. |
| Source stamp | Every response carries the retrieval-time `version` pin (date + `manifest_database_count` 63,047 at staging). If the manifest moves, the package is regenerated; do not mix snapshots. |

Response envelope for list/search endpoints:

```json
{
  "api_version": "v1",
  "endpoint": "/api/v1/databases/biofonics/records",
  "pagination": {
    "page": 1,
    "page_size": 100,
    "total_items": 16,
    "total_pages": 1,
    "items_on_page": 16,
    "remaining_after_this_page": 0,
    "prev_cursor": null,
    "next_cursor": null
  },
  "records": [ "..." ]
}
```

- `next_cursor: null` means "last page". A client that ignores the cursor
  and re-requests page 1 gets page 1 again (idempotent, resumable).
- Unknown `cursor` (wrong format, page 0, or past the last page) → 400
  with `code: "bad_cursor"`.
- A cursor is only valid for the same endpoint + same query. A reader
  that wants fewer entries per fetch can still fetch a page and read
  only its first N entries; the cursor still advances a whole page.
- Static pilot lists are single pages (16 records < 100), so their
  `next_cursor` is `null`.

## Error format

Every error is JSON, never an HTML error page, with HTTP status matching
the code:

```json
{
  "api_version": "v1",
  "error": {
    "code": "not_found",
    "message": "No record JAH-BIOF-999999 in database biofonics.",
    "endpoint": "/api/v1/record/biofonics/JAH-BIOF-999999",
    "hint": "Check the record ID against /api/v1/databases/biofonics/records, or cite the database code JAHDB/biofonics."
  }
}
```

| HTTP | `code` | Meaning |
|---|---|---|
| 400 | `bad_request` / `bad_cursor` / `bad_page_size` | Malformed request; `message` says what was wrong. (`bad_page_size` is retained for clients that send a `page_size` parameter; the fixed size is 100.) |
| 404 | `not_found` | Unknown slug, id, or endpoint. `hint` points at the list endpoint that can settle it. For a non-pilot slug the message also says when no single index file was found (chunked-index databases are not read by the gunzip route yet). |
| 405 | `method_not_allowed` | Anything other than GET. The API is read-only by design; POST/PUT/DELETE are never accepted. |
| 429 | `rate_limited` | Per-IP throttle tripped (live Worker only; see deploy plan). `Retry-After` header set. |
| 500 | `internal_error` | Server-side failure; `message` carries no stack trace. (The Worker returns this, contract-shaped, when its on-demand source fetch fails — a read failure, never a disguised not-found.) |

## Read-only guarantee

- GET only. No endpoint writes, edits, deletes, or creates anything.
- No authentication is required to read. (The 2026-10-08 one-provider-key
  rule governs the AI backend, not this read path — see deploy plan.)
- Responses are cacheable: `Cache-Control: public, max-age=3600` on record
  responses (records are immutable once filed; a changed record is a new
  version, cited as such — see `CITATION-FORMAT.md`).
- `Access-Control-Allow-Origin: *` so any outside AI or browser can fetch.

## Static pilot package (what is staged)

```
api/
  v1/
    index.json            # API root: endpoints, pilot scope, version pin
    router.json           # slug -> {records: {id -> file, title, code, key}}
    databases.json        # the 10 pilot databases
    search-index.json     # 160-entry title index (static search form)
    record/<slug>/<id>.json   # 160 files, one per record
    databases/<slug>/records.json  # 10 list files
```

Target on Pages (hub repo `jah-databases`): `api/v1/...` at
`https://justinahiggins614-cmyk.github.io/jah-databases/api/v1/...`.

Every per-record file is ordinary JSON a text-fetch reader can read
directly — that is the whole point: the `.gz` barrier disappears without
any server at all, and the live Worker (when deployed) serves these same
files behind the contract above, plus the on-demand gunzip route for
the rest of the network.
