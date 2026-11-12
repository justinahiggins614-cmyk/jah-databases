# FIX 5 — MCP Tool Specs (16 tools)

**Pilot scope:** the 10 FULL-CANON biofonics databases, 160 records, live
data-2 indexes. Every worked example below is a **real output captured from
the pilot harness** (`mcp-test-harness/captured-examples.json`); long text
fields are cut with `[…]` and marked as cut. Response shape is the MCP tool
result: `{"content": [{"type": "text", "text": "<JSON string>"}],
"structuredContent": <payload>, "isError": false}`. Error shape (tool
errors): `{"content": [{"type": "text", "text": "{\"error\": {...}}"}],
"structuredContent": {"error": {"code": "...", "message": "..."}},
"isError": true}`.

Route per tool: **EXISTS** = described by an `ai-mcp-server` pair record
(schema here is the EXPAND); **NEW** = no pair record covers it.

Common rules: `limit` 1–100, default 25. `cursor` is an opaque resume
string (`null` = done). No tool ever returns a whole database, index, or
manifest.

---

## 1. `jah_list_databases` — database discovery — EXISTS (JAH-AMCP-000010)

**Input schema**
```json
{"type": "object",
 "properties": {
   "query": {"type": "string",
             "description": "Substring match over name + slug + record_kind"},
   "limit": {"type": "integer", "default": 25, "minimum": 1, "maximum": 100},
   "cursor": {"type": "string"}},
 "additionalProperties": false}
```

**Response shape**
```json
{"databases": [{"slug": "string", "name": "string", "record_kind": "string",
                "record_count": "integer",
                "manifest_record_count": "integer", "ai_name": "string",
                "source": "string"}],
 "total": "integer", "next_cursor": "string|null",
 "pilot_scope": "string"}
```

**Worked example** — `{"limit": 3}` (real output):
```json
{"databases": [
  {"slug": "biofonics", "name": "The Biofonics Database",
   "record_kind": "biofonics record", "record_count": 16,
   "manifest_record_count": 16, "ai_name": "Keeper of Biofonics",
   "source": "assistant-built"},
  {"slug": "biofonics-signature", "name": "The Biofonics Database (Signature)",
   "record_kind": "biofonics record", "record_count": 16,
   "manifest_record_count": 16, "ai_name": "Keeper of Biofonics",
   "source": "assistant-built"},
  {"slug": "biophony-soundscapes", "name": "The Biophony Soundscapes Database",
   "record_kind": "biophony soundscape record", "record_count": 16,
   "manifest_record_count": 16, "ai_name": "Keeper of the Biophony",
   "source": "assistant-built"}],
 "total": 10, "next_cursor": "3",
 "pilot_scope": "10 biofonics databases (FULL-CANON pilot)"}
```
`{"query": "soundscape"}` returns `total: 4` (the four soundscape slugs).

**Errors:** none in the pilot (empty query result is `total: 0`, not an error).

---

## 2. `jah_search_database` — database search — EXISTS (JAH-AMCP-000002)

**Input schema**
```json
{"type": "object",
 "properties": {
   "slug": {"type": "string"},
   "query": {"type": "string"},
   "limit": {"type": "integer", "default": 25, "minimum": 1, "maximum": 100},
   "cursor": {"type": "string"}},
 "required": ["slug", "query"], "additionalProperties": false}
```

**Response shape**
```json
{"slug": "string", "query": "string", "total_hits": "integer",
 "next_cursor": "string|null",
 "results": [{"id": "string", "title": "string", "snippet": "string"}]}
```

**Worked example** — `{"slug": "biofonics", "query": "echolocation"}` (real):
```json
{"slug": "biofonics", "query": "echolocation", "total_hits": 2,
 "next_cursor": null,
 "results": [
  {"id": "JAH-BIOF-000007", "title": "Bat Echolocation",
   "snippet": "Bats that hunt in darkness navigate and find prey by echolocation: they emit ultrasonic pulses, mostly above the range of human hearing, and listen to the returning echoes to build a picture of their […]"},
  {"id": "JAH-BIOF-000016", "title": "Biofonics Field Guide Index",
   "snippet": "[…] frog choruses, insect sound, bat echolocation, whale song, elephant infrasound, […]"}]}
```

**Errors:** `missing_argument` (slug or query absent),
`unknown_database` (slug not in the pilot set).

---

## 3. `jah_get_file` — file retrieval — EXISTS (JAH-AMCP-000003)

**Input schema**
```json
{"type": "object",
 "properties": {
   "location": {"type": "string",
                "description": "Pilot form: data-2/data/<slug>/index.jsonl.gz"},
   "limit": {"type": "integer", "default": 25, "minimum": 1, "maximum": 100},
   "cursor": {"type": "string"}},
 "required": ["location"], "additionalProperties": false}
```

**Response shape**
```json
{"location": "string", "slug": "string", "total_records": "integer",
 "next_cursor": "string|null",
 "records": [{"id": "string", "title": "string", "record_kind": "string",
              "description": "string (first 400 chars)"}]}
```

**Worked example** — `{"location": "data-2/data/biofonics/index.jsonl.gz", "limit": 2}` (real):
```json
{"location": "data-2/data/biofonics/index.jsonl.gz", "slug": "biofonics",
 "total_records": 16, "next_cursor": "2",
 "records": [
  {"id": "JAH-BIOF-000001", "title": "What Is Biofonics",
   "record_kind": "biofonics record",
   "description": "Biofonics is the study of the sounds of living things: the calls, songs, clicks, buzzes, and rustles that organisms make, and the way those sounds travel through air, water, and ground. […]"},
  {"id": "JAH-BIOF-000002", "title": "The Dawn Chorus",
   "record_kind": "biofonics record",
   "description": "The dawn chorus is the burst of bird song that rises just before and after sunrise, most famously in spring in temperate regions, when many male birds sing at once to defend territory and attract mates. […]"}]}
```

**Errors:** `missing_argument`, `unknown_file` (anything outside the pilot
`data-2/data/<pilot-slug>/index.jsonl.gz` form).

---

## 4. `jah_get_record` — record retrieval — EXISTS (JAH-AMCP-000005)

**Input schema**
```json
{"type": "object",
 "properties": {"id": {"type": "string"}},
 "required": ["id"], "additionalProperties": false}
```

**Response shape**
```json
{"slug": "string", "record": "<full stored record object>"}
```
The record object is returned whole, exactly as stored. Biofonics record
keys: `ai_name, body, cross_links, demo, description, edition,
expected_output, generator, id, ladder_rank, layers, math_proof,
record_kind, science_proof, slug, source, source_quality, src, status,
title`. Note: `demo` is an object `{language, code, expected_output}`;
there is no `program` key and no image key in this pilot (the missing
FULL-CANON step).

**Worked example** — `{"id": "JAH-BIOF-000001"}` (real, abridged fields noted):
```json
{"slug": "biofonics",
 "record": {"id": "JAH-BIOF-000001", "title": "What Is Biofonics",
  "slug": "biofonics", "record_kind": "biofonics record",
  "src": "public-harvest", "edition": "public", "status": "built",
  "ladder_rank": "simple", "source_quality": "published-reference",
  "source": "Bernie Krause, The Great Animal Orchestra (2012), and standard acoustics references for the speed of sound in air at 20 degrees Celsius; figures as published October 2026",
  "description": "Biofonics is the study of the sounds of living things: […]",
  "body": "<p>Biofonics is the study of the sounds of living things: […] (2,102 chars)",
  "demo": {"language": "python",
   "code": "v = 343.0\nfor f in (440, 1000, 20000):\n    print('%d Hz: wavelength %.2f m' % (f, v / f))\n",
   "expected_output": "440 Hz: wavelength 0.78 m\n1000 Hz: wavelength 0.34 m\n20000 Hz: wavelength 0.02 m\n"},
  "generator": {"type": "seeded boundless generator",
   "hard_stop": 1000000000000000, "throttle_per_call": 100,
   "gen_id_prefix": "JAH-BIOF-GEN-"},
  "cross_links": ["db-animal-sounds", "future-whale-song-archives",
   "apexcreate-adaptive-music-and-soundscape-composer"],
  "science_proof": "Science proof: sound is a pressure wave […]",
  "math_proof": "Math proof: wavelength equals speed divided by frequency, so 343 / 440 = 0.7795 metres, about 0.78 metres. […]"}}
```

**Errors:** `missing_argument`, `record_not_found`.

---

## 5. `jah_search_all` — cross-database search — EXISTS (JAH-AMCP-000015)

**Input schema**
```json
{"type": "object",
 "properties": {
   "query": {"type": "string"},
   "limit": {"type": "integer", "default": 25, "minimum": 1, "maximum": 100},
   "cursor": {"type": "string"}},
 "required": ["query"], "additionalProperties": false}
```

**Response shape**
```json
{"query": "string", "total_hits": "integer", "next_cursor": "string|null",
 "per_database": [{"slug": "string", "hits": "integer"}],
 "results": [{"slug": "string", "id": "string", "title": "string",
              "snippet": "string"}]}
```

**Worked example** — `{"query": "whale", "limit": 3}` (real):
```json
{"query": "whale", "total_hits": 21, "next_cursor": "3",
 "per_database": [
  {"slug": "biofonics", "hits": 3},
  {"slug": "biofonics-signature", "hits": 2},
  {"slug": "biophony-soundscapes", "hits": 5},
  {"slug": "biophony-soundscapes-signature", "hits": 3},
  {"slug": "soundscape-ecology", "hits": 3},
  {"slug": "soundscape-ecology-signature", "hits": 1},
  {"slug": "animal-vocal-communication", "hits": 3},
  {"slug": "animal-vocal-communication-signature", "hits": 1},
  {"slug": "bioacoustic-recording-analysis", "hits": 0},
  {"slug": "bioacoustic-recording-analysis-signature", "hits": 0}],
 "results": [
  {"slug": "biofonics", "id": "JAH-BIOF-000008",
   "title": "Whale Song and Ocean Bioacoustics",
   "snippet": "Humpback whales produce long, structured songs that can last tens of minutes and be repeated for hours, built from units grouped into phrases and themes […]"},
  {"slug": "biofonics", "id": "JAH-BIOF-000013",
   "title": "Noise Pollution and the Anthrophony Layer",
   "snippet": "…n, shipping noise overlaps the low-frequency calls of large whales, and documented responses include louder calling and altered call rates. […]"},
  {"slug": "biofonics", "id": "JAH-BIOF-000016",
   "title": "Biofonics Field Guide Index",
   "snippet": "…ng learning, frog choruses, insect sound, bat echolocation, whale song, elephant infrasound, the acoustic niche hypothesis, soundscape indices, […]"}]}
```

**Errors:** `missing_argument`. Live note: at full scale this tool searches
the sharded manifest/indexes, never a whole-network scan in one call; the
per-database hit counts are the resume-friendly summary.

---

## 6. `jah_read_document` — document reading — EXISTS (JAH-AMCP-000012, partial)

**Input schema**
```json
{"type": "object",
 "properties": {
   "doc": {"type": "string",
           "enum": ["record", "database-spec", "manifest"]},
   "id": {"type": "string", "description": "required when doc=record"},
   "slug": {"type": "string", "description": "required when doc=database-spec"}},
 "required": ["doc"], "additionalProperties": false}
```

**Response shape** — `{"doc": "record|database-spec|manifest",
"id"|"slug": "string", "title": "string" (record only),
"text": "string"}`. Record text is description + plain-text body (HTML
tags stripped).

**Worked example** — `{"doc": "record", "id": "JAH-BIOF-000007"}` (real,
2,858 chars; opening shown):
```json
{"doc": "record", "id": "JAH-BIOF-000007", "slug": "biofonics",
 "title": "Bat Echolocation",
 "text": "Bats that hunt in darkness navigate and find prey by echolocation: they emit ultrasonic pulses, mostly above the range of human hearing, and listen to the returning echoes to build a picture of their surroundings. Pulse design varies by hunting style. […]"}
```
`{"doc": "database-spec", "slug": "biofonics"}` returns the manifest entry
as JSON text. `{"doc": "manifest"}` returns: `"Live manifest
database_count: 63047. Pilot scope: 10 biofonics databases, 160 records.
Full manifest is 50.8 MB and is served paginated, never whole."`

**Errors:** `missing_argument`, `record_not_found`, `unknown_database`,
`unknown_document`.

---

## 7. `jah_cite` — citation generation — EXISTS (JAH-AMCP-000013)

**Input schema**
```json
{"type": "object",
 "properties": {"id": {"type": "string"}},
 "required": ["id"], "additionalProperties": false}
```

**Response shape**
```json
{"citation": {"code": "string (JCC v1)",
              "record_id": "string", "title": "string",
              "database": "string", "slug": "string",
              "record_kind": "string", "source": "string",
              "src": "string", "source_quality": "string",
              "live_url": "string", "text": "string"}}
```
Code form: `JAHDB/<slug>#<record-id>+k=<key>`; `key` = first 8 hex of
SHA-256 over canonical record JSON (keys sorted, compact separators,
UTF-8). Verified against the condensed-by-code pilot
(`pilot/biofonics/codes.md`; `decode.py demo` 10,693/10,693 PASS).

**Worked example** — `{"id": "JAH-BIOF-000007"}` (real):
```json
{"citation": {
  "code": "JAHDB/biofonics#JAH-BIOF-000007+k=0e71b537",
  "record_id": "JAH-BIOF-000007", "title": "Bat Echolocation",
  "database": "The Biofonics Database", "slug": "biofonics",
  "record_kind": "biofonics record",
  "source": "Published bat echolocation literature (Griffin and Galambos foundational experiments; modern call-identification surveys); speed of sound 343 m/s at 20 degrees Celsius, as published October 2026",
  "src": "public-harvest", "source_quality": "published-reference",
  "live_url": "https://justinahiggins614-cmyk.github.io/jah-databases-data-2/data/biofonics/index.jsonl.gz",
  "text": "Bat Echolocation. The Biofonics Database (biofonics record). Published bat echolocation literature (Griffin and Galambos foundational experiments; modern call-identification surveys); speed of sound 343 m/s at 20 degrees Celsius, as published October 2026, record JAH-BIOF-000007. Condensed code JAHDB/biofonics#JAH-BIOF-000007+k=0e71b537."}}
```
Also verified: `JAH-BIOF-000001` →
`JAHDB/biofonics#JAH-BIOF-000001+k=32d2ef75`.

**Errors:** `missing_argument`, `record_not_found`.

---

## 8. `jah_compare_databases` — database comparison — NEW

**Input schema**
```json
{"type": "object",
 "properties": {"slugs": {"type": "array", "minItems": 2,
                          "items": {"type": "string"}}},
 "required": ["slugs"], "additionalProperties": false}
```

**Response shape**
```json
{"compared": ["string"], "same_record_kind": "boolean",
 "record_kinds": ["string"],
 "profiles": [{"slug": "string", "record_count": "integer",
               "median_body_chars": "integer",
               "field_fractions": {"body": "number", "demo": "number",
                 "program": "number", "image": "number",
                 "science_proof": "number", "math_proof": "number",
                 "generator": "number"},
               "record_kind": "string"}],
 "notes": "string"}
```
Field fractions are measured over the stored records (fraction of records
carrying the field).

**Worked example** — `{"slugs": ["biofonics", "biophony-soundscapes"]}` (real):
```json
{"compared": ["biofonics", "biophony-soundscapes"],
 "profiles": [
  {"slug": "biofonics", "record_count": 16, "median_body_chars": 2031,
   "field_fractions": {"body": 1.0, "demo": 1.0, "program": 0.0,
    "image": 0.0, "science_proof": 1.0, "math_proof": 1.0, "generator": 1.0},
   "record_kind": "biofonics record"},
  {"slug": "biophony-soundscapes", "record_count": 16, "median_body_chars": 1825,
   "field_fractions": {"body": 1.0, "demo": 1.0, "program": 0.0,
    "image": 0.0, "science_proof": 1.0, "math_proof": 1.0, "generator": 1.0},
   "record_kind": "biophony soundscape record"}],
 "same_record_kind": false,
 "record_kinds": ["biofonics record", "biophony soundscape record"],
 "notes": "Field fractions are measured over stored records; image is 0.0 across the biofonics pilot (the one missing FULL-CANON step)."}
```

**Errors:** `missing_argument`, `invalid_argument` (< 2 slugs or not a
list), `unknown_database`.

---

## 9. `jah_knowledge_graph` — knowledge-graph lookup — EXISTS (JAH-AMCP-000007)

**Input schema**
```json
{"type": "object",
 "properties": {"id": {"type": "string"}},
 "required": ["id"], "additionalProperties": false}
```

**Response shape**
```json
{"node": {"id": "string", "slug": "string", "title": "string"},
 "edges": [{"to": "string", "relation": "cross_link", "note": "string"}],
 "term_neighbours": [{"id": "string", "slug": "string", "title": "string",
                      "shared_title_words": ["string"]}],
 "neighbour_count": "integer"}
```
Edges are the record's stored `cross_links`. Term neighbours are other
pilot records sharing a title word (≥4 chars).

**Worked example** — `{"id": "JAH-BIOF-000007"}` (real):
```json
{"node": {"id": "JAH-BIOF-000007", "slug": "biofonics",
         "title": "Bat Echolocation"},
 "edges": [
  {"to": "db-animal-sounds", "relation": "cross_link",
   "note": "record-level cross-link as stored"},
  {"to": "future-whale-song-archives", "relation": "cross_link",
   "note": "record-level cross-link as stored"},
  {"to": "apexcreate-adaptive-music-and-soundscape-composer",
   "relation": "cross_link", "note": "record-level cross-link as stored"}],
 "term_neighbours": [
  {"id": "JAH-AVC-000008", "slug": "animal-vocal-communication",
   "title": "Bat Echolocation: Calls That Come Back",
   "shared_title_words": ["echolocation"]},
  {"id": "JAH-AVCS-000008", "slug": "animal-vocal-communication-signature",
   "title": "Signature Echolocation: Designed Calls That Return",
   "shared_title_words": ["echolocation"]}],
 "neighbour_count": 2}
```

**Errors:** `missing_argument`, `record_not_found`.

---

## 10. `jah_lookup_encyclopedia` — encyclopedia / dictionary lookup — NEW

**Input schema**
```json
{"type": "object",
 "properties": {"term": {"type": "string"}},
 "required": ["term"], "additionalProperties": false}
```

**Response shape**
```json
{"term": "string", "found": "boolean",
 "definition": "string|null",
 "source_record": {"id": "string", "slug": "string", "title": "string"},
 "other_matches": [{"id": "string", "slug": "string", "title": "string"}],
 "total_matches": "integer", "note": "string"}
```

**Worked example** — `{"term": "echolocation"}` (real; definition cut):
```json
{"term": "echolocation", "found": true,
 "definition": "Bats that hunt in darkness navigate and find prey by echolocation: they emit ultrasonic pulses, mostly above the range of human hearing, and listen to the returning echoes to build a picture of their surroundings. […]",
 "source_record": {"id": "JAH-BIOF-000007", "slug": "biofonics",
                   "title": "Bat Echolocation"},
 "other_matches": [{"id": "JAH-BIOF-000016", "slug": "biofonics",
                    "title": "Biofonics Field Guide Index"},
                   {"id": "JAH-BIOFS-000007", "slug": "biofonics-signature",
                    "title": "Signature: Bat Pulse Model"},
                   {"id": "JAH-AVC-000008", "slug": "animal-vocal-communication",
                    "title": "Bat Echolocation: Calls That Come Back"},
                   {"id": "JAH-AVCS-000008",
                    "slug": "animal-vocal-communication-signature",
                    "title": "Signature Echolocation: Designed Calls That Return"}],
 "total_matches": 5,
 "note": "Pilot definition drawn from biofonics records only; live lookup also consults JAH Wiki / Dictionary."}
```
Miss example — `{"term": "zzzqqq"}` → `{"term": "zzzqqq", "found": false,
"definition": null, "note": "No pilot record defines 'zzzqqq'. Live lookup
routes to the JAH Wiki and Dictionary indexes; those indexes are outside
this 10-database pilot."}`

**Live routing (design-only):** the live tool consults the JAH Wiki and
Dictionary indexes first, then falls back to database records. The pilot
proves the interface and the honest-miss behaviour only.

**Errors:** `missing_argument`.

---

## 11. `jah_calculate` — calculator connection — NEW

**Input schema**
```json
{"type": "object",
 "properties": {"expression": {"type": "string",
   "description": "Arithmetic only: numbers, + - * / % ** ( ), math functions sqrt/sin/cos/tan/log/log10/exp/abs, pi, e"}},
 "required": ["expression"], "additionalProperties": false}
```

**Response shape**
```json
{"expression": "string", "result": "number", "note": "string"}
```

**Worked example** — `{"expression": "343/440"}` (real; the biofonics demo
value — wavelength of a 440 Hz tone in air):
```json
{"expression": "343/440", "result": 0.7795454545454545,
 "note": "Pilot calculator: local safe arithmetic. Live routing delegates to the Signature Calculator database/site; this pilot proves the interface, not the live route."}
```

**Errors:** `missing_argument`, `invalid_expression` (unparsable, or a
name/operator outside the whitelist — `__import__('os')` is rejected with
`isError: true`), `calculation_error` (e.g. division by zero).
Implementation: AST-whitelisted evaluation, never `eval` on raw input.

**Live routing (design-only):** the live tool delegates to the Signature
Calculator (site `jah-calculator` / equations database); the pilot's local
evaluator is the interface proof.

---

## 12. `jah_research` — research assistant — EXISTS (JAH-AMCP-000016, partial)

**Input schema**
```json
{"type": "object",
 "properties": {"question": {"type": "string"}},
 "required": ["question"], "additionalProperties": false}
```

**Response shape**
```json
{"question": "string", "answer": "string|null",
 "source_record": {"id": "string", "slug": "string", "title": "string"},
 "match_score": "integer", "note": "string"}
```

**Worked example** — `{"question": "How do bats use echolocation?"}` (real;
answer is the source record's own description, verbatim, cut here):
```json
{"question": "How do bats use echolocation?",
 "answer": "Bats that hunt in darkness navigate and find prey by echolocation: they emit ultrasonic pulses, mostly above the range of human hearing, and listen to the returning echoes to build a picture of their surroundings. […]",
 "source_record": {"id": "JAH-BIOF-000007", "slug": "biofonics",
                   "title": "Bat Echolocation"},
 "match_score": 3,
 "note": "Answer is the source record's own description, verbatim; no synthesis added in the pilot."}
```
No-answer example — `{"question": "zzzqqq www"}` → `{"answer": null,
"note": "No pilot record answers this question. A live research call would
escalate to the database AI / off-site Signature Web AI; the pilot does not
invent an answer."}`

**Errors:** `missing_argument`.

---

## 13. `jah_generate` — generator connection — EXISTS (JAH-AMCP-000008/000009)

**Input schema**
```json
{"type": "object",
 "properties": {"slug": {"type": "string"},
                "seed": {"type": "integer", "default": 1}},
 "required": ["slug"], "additionalProperties": false}
```

**Response shape**
```json
{"generated": {"id": "string", "title": "string", "slug": "string",
               "record_kind": "string", "seed": "integer",
               "simulated": true, "text": "string"},
 "generator": {"type": "string", "hard_stop": "integer",
               "throttle_per_call": "integer", "gen_id_prefix": "string"},
 "note": "string"}
```

**Worked example** — `{"slug": "biofonics", "seed": 7}` (real; deterministic
— same seed returns the same ID):
```json
{"generated": {
  "id": "JAH-BIOF-GEN-100007",
  "title": "Generated variation on: Whale Song and Ocean Bioacoustics",
  "slug": "biofonics", "record_kind": "biofonics record", "seed": 7,
  "simulated": true,
  "text": "Simulated generated record seeded from JAH-BIOF-000008 (seed 7). Content is generated, not stored; verify before use."},
 "generator": {"type": "seeded boundless generator",
               "hard_stop": 1000000000000000, "throttle_per_call": 100,
               "gen_id_prefix": "JAH-BIOF-GEN-"},
 "note": "Generator connection proof only: the pilot derives a deterministic simulated record from the seed. Live generation runs the database's own boundless generator."}
```

**Errors:** `missing_argument`, `unknown_database`, `invalid_argument`
(non-integer seed). Live note: generation never writes to storage through
this server; the returned record is a response only.

---

## 14. `jah_browse_archive` — archive browsing — EXISTS (JAH-AMCP-000006)

**Input schema**
```json
{"type": "object",
 "properties": {
   "slug": {"type": "string"},
   "limit": {"type": "integer", "default": 25, "minimum": 1, "maximum": 100},
   "cursor": {"type": "string"}},
 "required": ["slug"], "additionalProperties": false}
```

**Response shape**
```json
{"slug": "string", "total_records": "integer",
 "next_cursor": "string|null",
 "entries": [{"id": "string", "title": "string", "ladder_rank": "string",
              "description": "string (first 200 chars)"}]}
```

**Worked example** — `{"slug": "biofonics", "limit": 3}` (real):
```json
{"slug": "biofonics", "total_records": 16, "next_cursor": "3",
 "entries": [
  {"id": "JAH-BIOF-000001", "title": "What Is Biofonics",
   "ladder_rank": "simple",
   "description": "Biofonics is the study of the sounds of living things: the calls, songs, clicks, buzzes, and rustles that organisms make, and the way those sounds travel through air, water, and ground. […]"},
  {"id": "JAH-BIOF-000002", "title": "The Dawn Chorus",
   "ladder_rank": "simple",
   "description": "The dawn chorus is the burst of bird song that rises just before and after sunrise, most famously in spring in temperate regions, when many male birds sing at once to defend territory and attract mate[…]"},
  {"id": "JAH-BIOF-000003", "title": "Bernie Krause and the Biophony Concept",
   "ladder_rank": "simple",
   "description": "Bernie Krause, an American musician turned field recordist and soundscape ecologist, gave soundscape ecology its central vocabulary. […]"}]}
```
Resume proven in the test suite: page 1 (`limit: 10`, cursor `"10"`) +
page 2 returns the remaining 6 with `next_cursor: null`, no overlap.

**Errors:** `missing_argument`, `unknown_database`.

---

## 15. `jah_get_media` — image / video / metadata retrieval — NEW

**Input schema**
```json
{"type": "object",
 "properties": {"id": {"type": "string"}},
 "required": ["id"], "additionalProperties": false}
```

**Response shape**
```json
{"id": "string", "slug": "string",
 "media": [{"kind": "image|image_url|video|video_url|audio", "url": "string"}],
 "media_count": "integer",
 "metadata": {"id": "string", "title": "string", "slug": "string",
              "record_kind": "string", "src": "string", "source": "string",
              "source_quality": "string", "edition": "string",
              "status": "string", "ladder_rank": "string"},
 "note": "string"}
```

**Worked example** — `{"id": "JAH-BIOF-000007"}` (real):
```json
{"id": "JAH-BIOF-000007", "slug": "biofonics", "media": [], "media_count": 0,
 "metadata": {"id": "JAH-BIOF-000007", "title": "Bat Echolocation",
  "slug": "biofonics", "record_kind": "biofonics record",
  "src": "public-harvest",
  "source": "Published bat echolocation literature (Griffin and Galambos foundational experiments; modern call-identification surveys); speed of sound 343 m/s at 20 degrees Celsius, as published October 2026",
  "source_quality": "published-reference", "edition": "public",
  "status": "built", "ladder_rank": "compounded"},
 "note": "Biofonics pilot records carry no image/video fields (the one missing FULL-CANON step); metadata retrieval is the live part of this tool in the pilot."}
```
Honest limit, stated in the response itself: the pilot proves metadata
retrieval; image/video serving is unproven here because the pilot records
have no media fields. Live: the tool reads the record's image/video fields
where they exist (databases with images) and returns their URLs; it never
invents media.

**Errors:** `missing_argument`, `record_not_found`.

---

## 16. `jah_health` — health-check — EXISTS (JAH-AMCP-000011)

**Input schema**
```json
{"type": "object", "properties": {}, "additionalProperties": false}
```

**Response shape**
```json
{"status": "ok", "server": "string",
 "manifest_database_count": "integer|null",
 "manifest_loaded": "boolean",
 "pilot_databases": "integer", "pilot_records": "integer",
 "expected_records": "integer", "records_match": "boolean",
 "read_only": true, "note": "string"}
```

**Worked example** — `{}` (real):
```json
{"status": "ok", "server": "jah-mcp-pilot/1.0 (stdio, package-only)",
 "manifest_database_count": 63047, "manifest_loaded": true,
 "pilot_databases": 10, "pilot_records": 160, "expected_records": 160,
 "records_match": true, "read_only": true,
 "note": "Health only. Live endpoint adds manifest-count hard stop: regenerate if the count moves."}
```

**Errors:** none (health never fails on a bad argument; it takes none).
