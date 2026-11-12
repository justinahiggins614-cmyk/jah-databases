# Review — `18th-century`

**Verdict: USABLE** (usable / partial / broken)

**Date:** 2026-11-02. **Mode:** package-only review; nothing merged, pushed, or deployed. **Manifest at review time:** 63047 databases.

## Specification

- Name: 18th Century Database &mdash; JAH Databases
- Record kind: `century record` — AI: JAH 18th Century Archivist
- Tagline: The 1700s in full: Enlightenment, revolution, and the steam-powered start of the modern world - every major event, movement, invention, and turning point of the 18th century, ladder-ordered from foundations to advanced. Property of Justin Addam Higgins.
- ID prefix: `JAH-18THC-` — manifest record_count: 34 — source: public-harvest
- Full-file-check census class: **THIN** (read: READABLE, org: ORGANIZED, steps 2/7, median body 690 chars)
- Index: `/home/hatch/workspace/jah-databases-data-1/data/18th-century/index.jsonl.gz`
- Primary sample source: chunks (1 files) (1 chunk files, 5 records sampled)

## Checks (evidence per check)

| Check | Result | Evidence |
|---|---|---|
| spec_present | PASS | manifest entry: name='18th Century Database &mdash; JAH Databases' record_kind='century record' ai_name='JAH 18th Century Archivist' id_prefix='JAH-18THC-'; missing fields: none |
| index_loads | PASS | url->local: 34 records parsed from /home/hatch/workspace/jah-databases-data-1/data/18th-century/index.jsonl.gz |
| count_agrees | PASS | manifest record_count=34, index lines=34, chunk records=34 |
| records_parse | PASS | sampled 5 records (chunks (1 files), positions [0, 1, 2, 3, 4]); unparseable=none; with title=5/5; id-prefix mismatches=none |
| readable | PASS | readable 5/5 sampled (prose >=200 chars, garbled-token fraction <0.35); median sampled prose 868 chars; garbled 0 |
| demos_run | PASS | demos present in 5/5 sampled; all ran (ok=5, skipped=0); JAH-18THC-000001: ran, exit 0 (no expected output to compare); JAH-18THC-000002: ran, exit 0 (no expected output to compare); JAH-18THC-000003: ran, exit 0 (no expected output to compare); JAH-18THC-000004: ran, exit 0 (no expected output to compare); JAH-18THC-000005: ran, exit 0 (no expected output to compare) |
| links_resolve | PASS | page exists; markers exhaustive=True merger=True stCount=True old_loader=False; index file present locally (/home/hatch/workspace/jah-databases-data-1/data/18th-century/index.jsonl.gz) |
| citations_present | PASS | source/citations/src present in 5/5 sampled; JCC v1 code formable, e.g. JAHDB/18th-century#JAH-18THC-000001+k=04714e73 |

Demo totals (sampled): present 5, ran OK 5, output mismatch 0, failed 0, skipped 0.

## Notes

- index rows are title-only (id/t/g); full records live in 1 chunk file(s) — index-enrichment gap, not a missing-data gap
- images: 0/5 sampled records carry an image field
- Census class is THIN (2/7 steps) while review says usable: the verdict covers retrievability, not the 7-step canon — canon steps still missing per census.

## What this verdict means

Usable as-is: spec present, index loads, counts agree, records parse and read, demos run, links resolve, citations present. No remediation needed from review mode; the full-file-check program's own verification still applies before anything is called done.

## How this extends the full-file-check program

The census assigns this database a class from a network-wide scan; review mode reads this one database end to end — spec, real files, executed demos, resolved links, per-record citations — and gives a verdict with evidence. It does not replace the census, the priority queue, or the fill waves.
