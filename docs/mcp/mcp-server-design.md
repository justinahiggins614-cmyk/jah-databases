# FIX 5 — MCP Server: Design Document

**Lane D (fixes 5 + 6), ai-fix-list-7. Package-only. No deploy, no merge, no push.**
**Date:** 2026-11-02. **Pilot data:** the 10 FULL-CANON biofonics databases,
160 records, live data-2 indexes (read-only). **Live manifest at design time:
63,047 databases.**

## 1. What this is

A Model Context Protocol server that exposes the JAH Databases network as
tools an outside AI can call. An outside AI lists the tools, calls one by
name with arguments, and gets structured data back — instead of trying to
read a 50.8 MB manifest or a `.gz` index through a text fetch (which cannot
decompress gzip — verified in STEP-0-1-VERIFICATION.md, §1c).

This document is the **design**. The live server is **design + deploy plan
only** until Manon approves a deploy (see §8 and `mcp-hosted-deploy-plan.md`).
What actually runs today is the local pilot harness in `mcp-test-harness/`
(stdio, stdlib-only Python, 29/29 tests passing — see `TEST-RESULTS.md`).

## 2. Relationship to the existing MCP database pair — EXISTS / EXPAND

The Paste A Wave 1 pair `ai-mcp-server` / `ai-mcp-server-signature`
(48 records, JAH-AMCP-000001–000024, package-only, NOT live) already covers
the MCP **database side**: it describes the server and its tools as records.
This design **builds on it and does not rebuild it**:

| This design's tool | Pair record | Route |
|---|---|---|
| `jah_list_databases` (discovery) | JAH-AMCP-000010 MCP Resource Discovery Tool | EXISTS — schema is the EXPAND (the record is prose; the JSON Schema in `mcp-tool-specs.md` is new) |
| `jah_search_database` | JAH-AMCP-000002 MCP Database Search Tool | EXISTS — schema EXPAND |
| `jah_get_file` | JAH-AMCP-000003 MCP File Retrieval Tool | EXISTS — schema EXPAND |
| `jah_get_record` | JAH-AMCP-000005 MCP Record Query Tool | EXISTS — schema EXPAND |
| `jah_search_all` | JAH-AMCP-000015 MCP Cross-Database Search Tool | EXISTS — schema EXPAND |
| `jah_read_document` | JAH-AMCP-000012 MCP Documentation Tool | EXISTS (partial) — EXPAND: record full text + database spec + manifest summary as three `doc` kinds |
| `jah_cite` | JAH-AMCP-000013 MCP Citation Tool | EXISTS — schema EXPAND; citation code is JCC v1 (verified, see §6) |
| `jah_compare_databases` | — none — | **NEW** |
| `jah_knowledge_graph` | JAH-AMCP-000007 MCP Knowledge Graph Tool | EXISTS — schema EXPAND |
| `jah_lookup_encyclopedia` | — none — | **NEW** |
| `jah_calculate` | — none — | **NEW** |
| `jah_research` | JAH-AMCP-000016 MCP Database AI Gateway | EXISTS (partial) — EXPAND: pilot answers from the source record's own description, verbatim; no synthesis |
| `jah_generate` | JAH-AMCP-000008 MCP Database Generator Tool + JAH-AMCP-000009 MCP File Generator Tool | EXISTS — schema EXPAND; pilot returns a deterministic simulated record, labelled `simulated: true` |
| `jah_browse_archive` | JAH-AMCP-000006 MCP Archive Search Tool | EXISTS — schema EXPAND |
| `jah_get_media` | — none — | **NEW** (file retrieval covers files, not image/video/metadata per record) |
| `jah_health` | JAH-AMCP-000011 MCP Network Status Tool | EXISTS — schema EXPAND |
| Server itself | JAH-AMCP-000001 Model Context Protocol Server | EXISTS as a record; this design is the runnable server spec for it |
| Auth / permissions | JAH-AMCP-000017 MCP Authentication Service + JAH-AMCP-000018 MCP Permission Registry | EXISTS as records; the hosted auth design in §7 follows them |
| Client setup | JAH-AMCP-000023 MCP Setup Guide + JAH-AMCP-000024 MCP Troubleshooting Guide + JAH-AMCP-000019/20/21/22 (ChatGPT Action / OpenAPI / GPT connector / function-calling schema) | EXISTS — not rebuilt; the hosted plan references them |

Net: **12 of 16 tools EXIST as pair records** (schema is the new EXPAND work);
**4 are NEW** (`jah_compare_databases`, `jah_lookup_encyclopedia`,
`jah_calculate`, `jah_get_media`). No new database pair is needed for this
lane.

## 3. Transport

Two transports, one tool set, one implementation behind both:

### 3a. stdio (local use) — BUILT (pilot harness)

- JSON-RPC 2.0, one JSON object per line on stdin, one response per line on
  stdout. Server logs go to stderr only (stdout is pure protocol).
- Methods: `initialize`, `ping`, `tools/list`, `tools/call`, and
  `notifications/*` (accepted, ignored).
- `initialize` returns `protocolVersion: "2025-06-18"`,
  `capabilities: {"tools": {}}`, `serverInfo: {name: "jah-mcp-pilot",
  version: "1.0.0"}`.
- Startup: loads the pilot indexes once, prints a one-line ready message to
  stderr (`jah-mcp-pilot ready: 10 databases, 160 records,
  manifest_count=63047`), then serves until stdin closes.
- No network, no writes, no credentials. The pilot reads only the local
  data-2 clone and the local manifest.

### 3b. HTTP / SSE (hosted) — DESIGN ONLY

- One endpoint per the MCP HTTP transport: `POST /mcp` (JSON-RPC 2.0) with
  `GET /mcp` as the SSE stream for server-initiated messages. Same
  `initialize` / `tools/list` / `tools/call` methods as stdio; the tool
  implementations are transport-agnostic.
- Read-only by construction: the server has no tool that writes, generates
  into storage, or edits anything. Generation (`jah_generate`) returns a
  simulated record in the response; it stores nothing.
- No key baked into any client or page. Auth is a per-client token issued by
  the Worker (see §7 and the deploy plan). A token is never embedded in
  public Pages source.
- Full hosted design + deploy plan: `mcp-hosted-deploy-plan.md`. **Not
  deployed. No endpoint exists yet.**

## 4. Tool list (16)

Names are stable and prefixed `jah_`. Full JSON Schema, response shape,
error shape, and a worked example against real pilot data for each tool:
`mcp-tool-specs.md`.

1. `jah_list_databases` — list databases, paginated, optional name/kind query.
2. `jah_search_database` — keyword search inside one database.
3. `jah_get_file` — fetch a data file by location, paginated records.
4. `jah_get_record` — one record by ID, in full.
5. `jah_search_all` — keyword search across databases, per-database hit counts.
6. `jah_read_document` — read a document: a record's full text, a database
   spec, or the manifest summary.
7. `jah_cite` — citation for a record, with JCC v1 condensed code.
8. `jah_compare_databases` — compare ≥2 databases (counts, field coverage,
   median body length). **NEW.**
9. `jah_knowledge_graph` — a record's cross-links and term neighbours.
10. `jah_lookup_encyclopedia` — encyclopedia / dictionary lookup for a term.
    **NEW.**
11. `jah_calculate` — calculator connection: safe arithmetic evaluation.
    **NEW.**
12. `jah_research` — research assistant: best-matching record's own
    description as the answer, verbatim, or an honest no-answer.
13. `jah_generate` — generator connection: deterministic simulated record
    from a seed, labelled `simulated: true`.
14. `jah_browse_archive` — browse a database's archive, paginated with a
    resume cursor.
15. `jah_get_media` — image / video / metadata retrieval for a record.
    **NEW.**
16. `jah_health` — health-check: manifest count, databases/records loaded,
    read-only status.

## 5. Pagination and resumable batches (the Fix 2 contract, applied here)

Every list-shaped tool takes `limit` (1–100, default 25) and `cursor`
(an opaque string; in the pilot it is the integer offset). Every response
carries `next_cursor` (`null` when done) and a `total` where it is cheap to
compute. **Nothing in this server ever returns a whole database, a whole
index, or the whole manifest.** The largest single response in the pilot is
one record (`jah_get_record` on JAH-BIOF-000001: ~5 KB). This is the direct
answer to the outside AI's "400-database exhaustive-search ceiling": the
ceiling is not ours (verified: no such limit exists in our code; `llms.txt`
lists 444 databases), but a paginated contract with resume points is the
honest remedy, and this server implements it on every tool.

## 6. Citations — JCC v1 (verified, not assumed)

`jah_cite` returns the JCC v1 condensed code
`JAHDB/<slug>#<record-id>+k=<key>`, where `key` is the first 8 hex chars of
SHA-256 over the canonical record JSON (keys sorted, compact separators,
UTF-8). Verified against the condensed-by-code pilot
(`~/workspace/hidden_files/condensed-by-code-rollout/pilot/biofonics/codes.md`
and `code/decode.py demo`: **10,693/10,693 PASS**):

- `JAH-BIOF-000001` → `JAHDB/biofonics#JAH-BIOF-000001+k=32d2ef75`
- `JAH-BIOF-000007` → `JAHDB/biofonics#JAH-BIOF-000007+k=0e71b537`

The key is a 32-bit typo-check, not a cryptographic guarantee; the record ID
is the primary key. The harness computes the key from the stored record at
call time (same canonicalization as `decode.py`), so a citation can never
drift from the stored data. **Correction made during this lane:** an early
draft of the harness used the record kind as `k=`; that was wrong, caught
against the pilot codes, and fixed before the test run (see LANE-REPORT.md).

## 7. Errors

One error shape everywhere, in both transports:

```json
{"error": {"code": "record_not_found",
           "message": "record 'JAH-NOPE-000001' is not in the pilot data"}}
```

In MCP terms this is returned as a tool result with `isError: true` (the
JSON-RPC call itself succeeds), except for protocol errors (`-32700` parse
error, `-32601` method not found), which are JSON-RPC errors. Error codes
used: `unknown_tool`, `unknown_database`, `unknown_file`,
`unknown_document`, `record_not_found`, `missing_argument`,
`invalid_argument`, `invalid_expression`, `calculation_error`,
`internal_error`. All five error paths are exercised in the test suite.

## 8. What the live server still needs (design-only items)

- **Scale-up:** the pilot serves 10 databases / 160 records from local
  `.gz` indexes. Live serves 63,047 databases. The index layout the server
  reads is the same (manifest + per-database `index.jsonl.gz`, chunked
  where chunks exist); the server must stream/decompress per call and never
  hold the manifest in memory whole. Sharded manifest (Fix 1 lane) is the
  prerequisite for a fast `jah_list_databases` at full scale.
- **Hosted endpoint + auth + rate limits:** see `mcp-hosted-deploy-plan.md`.
- **Hard stop:** the server records the manifest `database_count` at
  startup. If a live re-read finds the count moved, the server refuses new
  tool calls with `manifest_changed` until it is regenerated/reloaded. The
  pilot reports the count in `jah_health` (`manifest_database_count:
  63047` at test time).
- **Live routing for the four NEW tools:** `jah_lookup_encyclopedia` must
  consult the JAH Wiki / Dictionary indexes (pilot: biofonics records only,
  and it says so); `jah_calculate` must delegate to the Signature Calculator
  (pilot: local safe arithmetic, and it says so); `jah_get_media` must serve
  real record images/video where they exist (pilot: biofonics has none, and
  it says so — the one missing FULL-CANON step); `jah_compare_databases`
  needs no live routing beyond scale.
- **Approval:** Manon approves the deploy before any endpoint exists.

## 9. Files in this lane (Fix 5)

- `mcp-server-design.md` — this document.
- `mcp-tool-specs.md` — JSON Schema + response/error shape + one worked
  example per tool, all against real pilot data.
- `mcp-test-harness/mcp_server.py` — stdio pilot server (stdlib only).
- `mcp-test-harness/test_mcp.py` — 29-check test suite (29/29 PASS).
- `mcp-test-harness/captured-examples.json` — raw captured tool outputs
  used for the worked examples.
- `mcp-test-harness/TEST-RESULTS.md` — test run record.
- `mcp-hosted-deploy-plan.md` — hosted endpoint, auth, rate limits,
  hard stop. Design + deploy plan only.
