# JAH MCP Server — downloadable stdio package

**What this is:** a Model Context Protocol (MCP) server that lets an AI
(ChatGPT, Claude, Gemini, Copilot, or any MCP client) search and read
records from The 'Merica-L Internet / JAH Databases network — instead of
trying to read a 50 MB manifest or a `.gz` index through a text fetch.

**Status:** pilot package. It serves **10 databases / 160 records** (the
biofonics set) from the data bundled in `data/`. That is the verified
pilot scope — it proves the interface, the 16 tools, and the citation
format against real records. The full network (63,047 databases at
packaging time) is served by the hosted endpoint once it is deployed;
this package does not pretend to serve it.

**Free, read-only, no account, no key.** The server never writes, never
stores anything, and never needs a credential. It runs on your own
computer and reads only the files in this folder.

## Requirements

- Python 3.8 or newer (no extra packages — standard library only).
- This folder, unzipped, with `data/` and `manifest.json` beside
  `mcp_server.py`.

## Run it (stdio transport)

From inside this folder:

```bash
python3 mcp_server.py --data2 ./data --manifest ./manifest.json
```

The server prints one line to stderr when ready:

```
jah-mcp-pilot ready: 10 databases, 160 records, manifest_count=63047
```

Then it reads one JSON-RPC 2.0 object per line on stdin and writes one
response per line on stdout. Logs go to stderr only — stdout is pure
protocol. Press Ctrl-C or close stdin to stop it.

## Try it (smoke test — no AI client needed)

```bash
python3 smoke_test.py
```

Expected output ends with: `SMOKE OK: 6 checks passed` — it runs
`initialize`, `tools/list` (16 tools), one search, one record fetch,
one citation, and a health check, all against the bundled data, and
prints real record titles back.

The full 29-check suite (`test_mcp.py`) is also included. It was
verified 29/29 on the build machine, but it points the server at the
live repo clones by default, so outside this build it only runs where
those clones exist. `smoke_test.py` is the package-alone check.

## Connect your AI

**Claude Desktop** — add to your Claude Desktop config file
(`claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "jah-mcp": {
      "command": "python3",
      "args": ["/full/path/to/this/folder/mcp_server.py",
               "--data2", "/full/path/to/this/folder/data",
               "--manifest", "/full/path/to/this/folder/manifest.json"]
    }
  }
}
```

Replace `/full/path/to/this/folder` with the real folder path. Restart
Claude Desktop. The 16 `jah_*` tools appear in the tools list.

**ChatGPT (Developer Mode / MCP)** — ChatGPT's MCP support varies by
plan and app version. In the ChatGPT app, go to Settings → Apps / MCP
servers (or Developer Mode), add a new **local / stdio** server with
command `python3` and the same arguments as above. If your ChatGPT
version only accepts remote (HTTP) servers, use the hosted endpoint
once it is live instead — see `mcp-hosted-deploy-plan.md`; there is
no hosted endpoint yet.

**Gemini (Gemini CLI / MCP)** — add to your Gemini CLI settings
(`~/.gemini/settings.json`, `mcpServers` section) the same way:

```json
{
  "mcpServers": {
    "jah-mcp": {
      "command": "python3",
      "args": ["/full/path/to/this/folder/mcp_server.py",
               "--data2", "/full/path/to/this/folder/data",
               "--manifest", "/full/path/to/this/folder/manifest.json"]
    }
  }
}
```

**Any other MCP client** — same command and arguments; the server
speaks JSON-RPC 2.0 over stdio, protocol version `2025-06-18`,
server name `jah-mcp-pilot`, version `1.0.0`.

## The 16 tools

| Tool | What it does |
|---|---|
| `jah_list_databases` | List databases, paginated, optional name/kind search |
| `jah_search_database` | Keyword search inside one database |
| `jah_get_file` | Fetch a data file by location, paginated records |
| `jah_get_record` | One record by ID, in full |
| `jah_search_all` | Keyword search across databases, with per-database hit counts |
| `jah_read_document` | Read a record's full text, a database spec, or the manifest summary |
| `jah_cite` | Citation for a record, with JCC v1 condensed code (`JAHDB/<slug>#<id>+k=<key>`) |
| `jah_compare_databases` | Compare 2+ databases: counts, field coverage, median body length |
| `jah_knowledge_graph` | A record's cross-links and term neighbours |
| `jah_lookup_encyclopedia` | Encyclopedia / dictionary lookup for a term |
| `jah_calculate` | Safe arithmetic (no code execution, ever) |
| `jah_research` | Research assistant: best-matching record's own description, verbatim — or an honest "no answer" |
| `jah_generate` | Deterministic *simulated* record from a seed (labelled `simulated: true`, never stored) |
| `jah_browse_archive` | Browse a database's archive, paginated with a resume cursor |
| `jah_get_media` | Image / video / metadata for a record (pilot records carry no media — metadata is the live part) |
| `jah_health` | Health check: manifest count, databases/records loaded, read-only status |

Every list-shaped tool takes `limit` (1–100, default 25) and `cursor`
(a resume string; `null` = done). **No tool ever returns a whole
database, a whole index, or the whole manifest.** Errors use one shape:
`{"error": {"code": "...", "message": "..."}}` with `isError: true`.

Full JSON Schema, response shape, error shape, and one worked example
per tool (all against real pilot data): `mcp-tool-specs.md`.
Design document: `mcp-server-design.md`.
Hosted-endpoint plan: `mcp-hosted-deploy-plan.md` (design only — no
endpoint exists yet).

## What the pilot does NOT do (honest limits)

- Serves only the 10 bundled biofonics databases (160 records). Asking
  for any other slug returns `unknown_database` — that is correct
  behaviour for this pilot, not a bug.
- `jah_calculate` is local safe arithmetic, not the live Signature
  Calculator. `jah_lookup_encyclopedia` searches pilot records only,
  not the live Wiki/Dictionary. `jah_generate` returns a simulated
  record, not a run of a live boundless generator. `jah_research`
  never invents an answer.
- `jah_health` reports `manifest_database_count: 63047` (the live count
  at packaging time). If the live network count moves, the hosted
  server refuses new calls until regenerated — the pilot states the
  rule; the hosted server enforces it.

## Files in this package

- `mcp_server.py` — the server (Python, stdlib only).
- `smoke_test.py` — package-alone smoke test (6 checks).
- `test_mcp.py` — the full 29-check suite (needs the live repo clones).
- `data/<slug>/index.jsonl.gz` — the 10 pilot database indexes (160 records).
- `manifest.json` — the 10 pilot database entries; `database_count`
  pinned to the live network count at packaging time.
- `mcp-tool-specs.md`, `mcp-server-design.md`,
  `mcp-hosted-deploy-plan.md` — specs, design, hosted plan.
- `hosted/` — the hosted (Cloudflare Worker) server, staged for deploy.
- `MANIFEST.md` — this package's staging manifest and verification evidence.

## Troubleshooting

- `pilot data load failed` — run from inside the folder, or pass
  `--data2` / `--manifest` with full paths.
- `unknown_database` — the slug is outside the 10-database pilot set.
- `record_not_found` — the record ID is not in the pilot data.
- Server prints nothing on stdout until it gets a request — that is
  normal; stdout is protocol only. The ready line goes to stderr.
