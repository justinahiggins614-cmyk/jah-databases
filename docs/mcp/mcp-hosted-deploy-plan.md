# FIX 5 — MCP Hosted Deploy Plan (DESIGN ONLY — do not deploy)

**Status:** design + deploy plan only. No endpoint exists. Nothing here is
deployed, and nothing is deployed until Manon approves the deploy.
**Live manifest at design time:** 63,047 databases.

## 1. Target shape

A hosted MCP endpoint that an outside AI (ChatGPT, Gemini, Copilot, or any
MCP client) can connect to directly, without downloading indexes or reading
`.gz` files through a text fetch. It is the hosted twin of the stdio pilot
(`mcp-test-harness/mcp_server.py`): same 16 tools, same JSON Schemas
(`mcp-tool-specs.md`), same pagination contract, same error shape.

## 2. Hosting choice

**Cloudflare Worker** (free tier), following the standing 2026-10-08
reversal: one provider key as an encrypted backend secret serves all users;
users never enter/save/see any key; **never bake any key into public Pages
source**.

- Worker name (proposed): `jah-mcp`.
- Routes:
  - `POST https://mcp.jah-databases.workers.dev/mcp` — JSON-RPC 2.0
    (initialize / tools/list / tools/call).
  - `GET https://mcp.jah-databases.workers.dev/mcp` — SSE stream for
    server-initiated messages (MCP HTTP transport).
  - `GET https://mcp.jah-databases.workers.dev/health` — plain JSON health
    (same payload as `jah_health`, no auth needed).
- Why a Worker and not GitHub Pages: Pages serves static files only; an MCP
  endpoint needs a live process to decompress `.gz` indexes per call, run
  searches, and enforce rate limits. The Worker is the compute; Pages stays
  the data store (manifest + indexes fetched by the Worker from the Pages
  URLs it already serves).
- Data path per call: Worker fetches the needed index file(s) from the
  public Pages data repos (`jah-databases-data-1`, `jah-databases-data-2`,
  main `jah-databases/data/`), gunzips in the Worker, answers from the
  decompressed records. Nothing is stored in the Worker between calls
  except a short-lived cache (see §5).

## 3. Auth — read-only, no key baked in

- **Server side:** the Worker holds no user credentials and needs none.
  If any upstream key is ever required (none is, for read-only data), it
  lives as an encrypted Worker secret, never in source.
- **Client side:** per-client bearer tokens, issued out of band by Manon
  (or by a tiny issuance flow he approves). Token format: `jahmcp_<random>`.
  The Worker checks `Authorization: Bearer <token>` on `/mcp` only.
  `/health` is public.
- **No anonymous tier at launch:** tokens are free, but they exist so abuse
  can be revoked per client without taking the endpoint down. This matches
  the standing rule (users never see a provider key) and the pair records
  JAH-AMCP-000017 (MCP Authentication Service) and JAH-AMCP-000018 (MCP
  Permission Registry).
- **Permissions:** one permission — `read`. There is no write tool, no
  generation-into-storage, no edit path. A token cannot do more than read,
  by design, not by policy.
- **What is NOT done:** no token in any public HTML/JS; no token in
  `llms.txt`, the manifest, or any database record; no Google sign-in gate
  (God Mode's Google-verified gate is for editing site content, not for
  this read API).

## 4. Rate limits

- Per token: **60 tool calls/minute, 1,000/hour, 10,000/day**, enforced in
  the Worker (in-memory per-isolate counters + KV for cross-isolate
  accounting). Over-limit returns JSON-RPC error `-32029` with
  `retry_after_seconds`.
- Per call: `limit` capped at 100 records; response bodies capped at
  ~256 KB (a `jah_get_record` on the largest stored record is well under
  this; if a record ever exceeds it, the tool returns the record truncated
  with `truncated: true` and a resume pointer — never a silent cut).
- Global: Worker free-tier CPU/time limits are the backstop; if the
  endpoint ever approaches them, the honest response is to throttle, not
  to silently degrade answers.
- `jah_search_all` at full scale is the most expensive tool (63,047
  databases). Live rule: it searches the **sharded manifest + per-database
  index metadata first** and only decompresses indexes for the top matching
  databases (bounded fan-out, e.g. 20 indexes per call), returning
  `per_database` hit counts from the metadata layer. It never scans all
  indexes in one call. This depends on the Fix 1 manifest-sharding lane.

## 5. Caching

- Manifest: cached in the Worker for **10 minutes**; re-fetched on expiry
  or on hard-stop trip (§6).
- Per-database index: cached **per call only** (decompress, answer,
  discard), except the 100 most-called databases, cached up to 1 hour in
  KV. Cache keys include the file's ETag/sha so a changed index is never
  served stale.
- No user data is cached. No tool-call log keeps arguments beyond 24h
  operational logs (counts only, no query text).

## 6. Hard stop — regenerate if the manifest count moves

- At Worker startup (and every manifest re-fetch), the Worker records
  `database_count` from the manifest.
- On each manifest re-fetch, if `database_count` differs from the recorded
  value, the Worker:
  1. stops answering new `tools/call` requests with error code
     `manifest_changed` ("manifest count moved from N to M; regenerating");
  2. re-fetches the manifest and any cached index metadata;
  3. resumes only after a fresh `jah_health` self-check passes
     (manifest loads, counts agree, pilot smoke call succeeds).
- `jah_health` always reports the live `manifest_database_count` so a
  client can see the move itself. This is the same rule the stdio pilot
  states in its health note; the hosted version enforces it.

## 7. Deploy steps (for Manon to approve — NOT run now)

1. Manon approves this plan (endpoint, auth, limits).
2. Create the Cloudflare Worker (`jah-mcp`) from the pilot server code,
   ported to the Worker runtime (same tool functions; stdio transport
   replaced by the HTTP/SSE transport; `gzip` via DecompressionStream).
3. Smoke test against the live Pages data: `initialize`, `tools/list`,
   one call per tool, `jah_health` showing 63,047.
4. Issue the first client token(s); publish the endpoint URL + setup
   instructions in the MCP Setup Guide record's live location
   (JAH-AMCP-000023 covers setup; the live URL goes there, not here).
5. Announce in the next "update on all" only after step 3 passes on the
   live endpoint.
6. **Do not** deploy before the Fix 1 sharded manifest exists — the
   unsharded 50.8 MB manifest makes `jah_list_databases` and
   `jah_search_all` slow and expensive at full scale.

## 8. What this plan deliberately does NOT include

- No write/edit tools, no God Mode path, no user-data storage.
- No billing, no paywall, no usage charge (standing rule: everything free).
- No claim that any outside AI endorses or is affiliated with the network
  (per the pair's honesty notes).
- No ChatGPT/GPT-specific server behaviour beyond the existing pair records
  (JAH-AMCP-000019–000022); the endpoint speaks MCP, and any MCP client
  can use it.
