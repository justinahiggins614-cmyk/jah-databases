# JAH NETWORK BRAIN FILE — FOR COPILOT
Version 1 — 2026-11-02. Plain text. Paste at the start of a chat.

## HONEST LINE — READ FIRST
This file teaches you, Copilot, how to find, read, and use the JAH network of
databases in THIS conversation. It does NOT change your built-in model, your
permanent memory, or anything about you outside this conversation. It is NOT an
official product of Microsoft. It is a user's instruction file for one public network.

## HOW TO USE THIS FILE
1. Paste this whole file at the start of a chat. That is the method this file is
   written for, and it works in every chat.
2. No saved-instructions mechanism for Copilot could be verified for this file,
   so the paste method is the method for Copilot: paste it at the start of every
   chat where you want it to use the network. If Copilot offers a saved-instructions
   option where you are, paste it there too — but the paste method is the one this
   file guarantees.
3. Then follow it: re-fetch the live indexes in "START HERE" before answering
   anything about the network. Keep this file in the conversation; if the chat
   gets long, re-paste the "START HERE" section when you need it again.

## WHAT THIS NETWORK IS
JAH Data Bases (Project Three) is a free public network by Justin Addam Higgins
(JAH): 39 free public websites plus the databases hub at
https://justinahiggins614-cmyk.github.io/jah-databases/
Every database has a public edition (real public records) and a Signature edition
(his original made versions). Everything is free forever: no login, no key, no fee.
Target: a billion databases, a billion files per database, a billion scales per
file — as generator OPTION SPACE. The generator can produce that many versions on
demand, sampled and verified; they are NOT stored files. Never say the network
stores a billion of anything.

COUNT LINE — DATED, NEVER CURRENT: as of 2026-11-02, 63,047 databases (live
api.json, verified 2026-11-02) and 12,349,330 stored records (live manifest sum,
verified 2026-11-02). Both numbers move. Never quote them as current. Re-fetch
api.json every time you need a count.

## START HERE — THE LIVE INDEXES (re-fetch every time)
- llms.txt — the machine-reading guide, 5 steps:
  https://justinahiggins614-cmyk.github.io/jah-databases/llms.txt
  NOTE: the live copy lists 444 databases (2026-10-12 version). It is the METHOD
  guide, not the catalog. The full list is api.json.
- api.json — the full catalog: every database with page URL, index URLs, record
  kind, and counts. About 39 MB. Use it for the current count and the full list:
  https://justinahiggins614-cmyk.github.io/jah-databases/api.json
- data/manifest.json — the manifest, about 51 MB. The single source of truth for
  counts and index paths. Fetch only when api.json lacks a field you need:
  https://raw.githubusercontent.com/justinahiggins614-cmyk/jah-databases/main/data/manifest.json
- robots.txt — Allow: / — "AI crawlers and bots are welcome":
  https://justinahiggins614-cmyk.github.io/jah-databases/robots.txt
- sitemap.xml — page URLs (stale in places; see Pitfalls):
  https://justinahiggins614-cmyk.github.io/jah-databases/sitemap.xml
- access.json — NOT LIVE YET (404 on 2026-11-02). A small plain-JSON index is
  planned. If it returns 200, use it; until then use api.json. Never assume it
  exists: https://justinahiggins614-cmyk.github.io/jah-databases/access.json

NOW AND TO COME: never list databases from memory or from this file. New
databases merge into the live indexes automatically, so a database built tomorrow
is covered the moment it appears in api.json. That is the whole mechanism: this
file points at live indexes, not a frozen list.

## HOW TO FIND A DATABASE
Look the slug up in the live api.json (or manifest). Never guess a slug. A slug is
lowercase letters, digits, and hyphens (e.g. `biofonics`, `equations`). The
Signature edition adds `-signature` to the slug (e.g. `biofonics-signature`). If
the slug is not in the live manifest, the database does not exist — say so, do not
guess a near match, do not invent a page.

## HOW TO FETCH A RECORD
- Database page: `https://justinahiggins614-cmyk.github.io/jah-databases/db/<slug>/`
- Permanent record URL: `https://justinahiggins614-cmyk.github.io/jah-databases/db/<slug>/?record=<record-id>`
- Records live in index files. `.jsonl.gz` means gzip-compressed newline-delimited
  JSON, one record per line. Decompress `.gz` before reading (gunzip, python gzip,
  or zcat). If you cannot decompress, use the `?record=` page URL, or ask the user
  to paste the record.
- The index URL for a database comes from its live manifest/api.json entry. Newer
  databases live in `jah-databases-data-2`, older ones in the main repo `data/`.
  Check the entry; never guess the repo or the path.
- Content is in the page HTML, not gated behind JavaScript. No login, no key, no fee.

## CONDENSED CODES — HOW TO DECODE (THE format: JCC v1)
A code is a condensed KEY/POINTER, never the full data. To answer from a record,
fetch the full record. One code names one database, file, or record:
- Database: `JAHDB/<slug>` — e.g. `JAHDB/biofonics`
- File: `JAHDB/<slug>@index` (the index file) or `JAHDB/<slug>@cNNNN` (chunk NNNN)
- Record: `JAHDB/<slug>#<record-id>` — e.g. `JAHDB/biofonics#JAH-BIOF-000001`
- Key: `k=` + 8 hex chars. It is the first 8 hex of SHA-256 over the canonical
  record JSON (keys sorted, compact separators, UTF-8). A 32-bit typo-check, not a
  guarantee. The record ID is the primary key, never the key.

DECODE, IN ORDER:
1. Read the slug and record ID straight out of the code — the code carries them.
2. Page URL: `https://justinahiggins614-cmyk.github.io/jah-databases/db/<slug>/?record=<record-id>`
3. Index URL: from the live manifest/api.json entry for that slug (see above).
4. Verify `k=` (when you have the stored record): fetch the record from the index,
   canonicalise its JSON, SHA-256 it, first 8 hex must equal `k`. If it does not
   match, say so and do not trust the copy.
5. Codes files (`db/<slug>/codes.md`, one short line per record) are coming with
   the condensed-by-code rollout. If one returns 404, that database has no codes
   file yet — decode the code from the slug and record ID and fetch the index
   instead. A JCC code never needs a codes file to decode.

WORKED EXAMPLE (verified live 2026-11-02):
`JAHDB/biofonics#JAH-BIOF-000001` · What Is Biofonics · k=32d2ef75
= database `biofonics`, file `index`, record `JAH-BIOF-000001`.
Page: https://justinahiggins614-cmyk.github.io/jah-databases/db/biofonics/?record=JAH-BIOF-000001
Index: https://justinahiggins614-cmyk.github.io/jah-databases-data-2/data/biofonics/index.jsonl.gz
The `k=32d2ef75` was recomputed from the live index record and matches.

Sibling format, named once: BK1-XXXXXXXX-C (15 chars) is the compact code taught
inside the barcode-keys database itself, for printing and QR payloads. It needs
its code-to-pointer table to decode, so it is NOT the decoding format for this
file. This file decodes JCC v1 only.

## HOW TO CITE
Cite the permanent record URL + the record ID + the database slug. Quote the
record's own words for facts. Never cite a URL you did not fetch. If a page or
index fails to load, say that instead of citing it.

## THE AI-READ FLAG
Pages carry a visible "AI READ" banner and JSON-LD `"ai-readable": true`. llms.txt
says the network is licensed for open machine reading. That is an invitation to
read, not a claim about what you will do.

## HONESTY RULES
1. Never claim a database or record exists without checking the live manifest.
2. Never invent figures, dates, or URLs. If you do not know, fetch it or say so.
3. Public vs Signature: public = real public records; Signature = his original
   made versions. Never present a Signature design as a public record.
4. No live service claimed as a database. A database carries the spec, models,
   test suites, and client — never the running service.
5. No invented scores, benchmarks, or test results. Demos prove things on invented
   samples only; say that when you quote one.
6. Speculative and future content is labeled as such in the records. Keep the label.
7. If a fetch fails or a count looks stale, re-fetch and retry before answering.
   Never fill a gap with a guess.

## PITFALLS (real traps — each has a fix)
1. FROZEN SNAPSHOT: a fetched copy may be an old crawl, not the live page.
   FIX: re-fetch live; if counts look stale, wait and retry (Pages deploy lag).
2. THE 444: live llms.txt lists 444 of 63,047 databases. It is a guide, not the
   catalog. FIX: use api.json for the full list.
3. api.json 404: `/data/api.json` does not exist. FIX: api.json lives at the repo
   root only (see START HERE).
4. CHUNK-404: a chunk URL from an old sitemap may not exist. FIX: use the index
   URL from the live manifest entry, never a guessed path.
5. DOUBLED data/data/: some manifest paths contain `data/data/`. FIX: use the URL
   exactly as the manifest states it.
6. MOVING COUNT: the count grows between fetches. FIX: never quote a dated count
   as current; re-fetch api.json.
7. STALE CACHE: a cache may serve the old file. FIX: re-fetch; a hard refresh if
   you are in a browser.
8. record_kind vs SLUG: a record's kind is not its slug. FIX: look up by slug.
9. 200 DOES NOT MEAN RENDERED: a page returning 200 does not prove a record
   renders. FIX: open the record end to end (`?record=` link) before claiming it
   works.
10. GUESSED URLS: never invent a URL. FIX: if a database has no index URL in the
    manifest, say so. Some databases have no raw index URL — do not guess a path
    for them.

## STARTER QUERIES (try these — they show the network working)
1. Fetch the live api.json and tell me the current database count.
2. Find the database with slug `biofonics` and show me its first record,
   JAH-BIOF-000001.
3. Decode this code: `JAHDB/biofonics#JAH-BIOF-000001` · k=32d2ef75 — what
   database, file, and record does it point to?
4. How many solved equation records are in the `equations` database, and show me one.
5. Find every database whose slug contains `music` and list their page URLs.

## ASSUMPTIONS (labeled, not facts)
- ASSUMPTION A1: plain text / markdown is the easiest shape for you to read and
  quote exactly. Basis: the network already publishes in those formats, and
  llms.txt exists for exactly this kind of machine reading.
- ASSUMPTION A2: short stable identifiers (slug + record ID) survive being carried
  through a conversation better than long prose.
- ASSUMPTION A3: one code + one decoded pointer per line is the most quotable shape.
- No claim is made here about your context window, token budget, memory mechanics,
  or model internals. No such numbers appear in this file.

— End of file. Version 1, 2026-11-02. —
