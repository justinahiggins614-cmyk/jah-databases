# Review — `biofonics`

**Verdict: USABLE** (usable / partial / broken)

**Date:** 2026-11-02. **Mode:** package-only review; nothing merged, pushed, or deployed. **Manifest at review time:** 63047 databases.

## Specification

- Name: The Biofonics Database
- Record kind: `biofonics record` — AI: Keeper of Biofonics
- Tagline: Sixteen full biofonics record records: What Is Biofonics; The Dawn Chorus; Bernie Krause and the Biophony Concept; Birdsong: Learning and Repertoire; Frog Choruses and Amphibian Calls; Insect Sound: Crickets and Cicadas; Bat Echolocation; Whale Song and Ocean Bioacoustics; Elephant Infrasound; The Acoustic Niche Hypothesis; Soundscape Indices: NDSI and ACI; Bioacoustics Field Recording Methods; Noise Pollution and the Anthrophony Layer; Coral Reef Soundscapes; Biofonics Conservation: Listening as Monitoring; Biofonics Field Guide Index.
- ID prefix: `JAH-BIOF-` — manifest record_count: 16 — source: assistant-built
- Full-file-check census class: **FULL-CANON** (read: READABLE, org: ORGANIZED, steps 6/7, median body 2102 chars)
- Index: `/home/hatch/workspace/jah-databases-data-2/data/biofonics/index.jsonl.gz`
- Primary sample source: index (0 chunk files, 5 records sampled)

## Checks (evidence per check)

| Check | Result | Evidence |
|---|---|---|
| spec_present | PASS | manifest entry: name='The Biofonics Database' record_kind='biofonics record' ai_name='Keeper of Biofonics' id_prefix='JAH-BIOF-'; missing fields: none |
| index_loads | PASS | url->local: 16 records parsed from /home/hatch/workspace/jah-databases-data-2/data/biofonics/index.jsonl.gz |
| count_agrees | PASS | manifest record_count=16, index lines=16 |
| records_parse | PASS | sampled 5 records (index, positions [0, 1, 2, 3, 4]); unparseable=none; with title=5/5; id-prefix mismatches=none |
| readable | PASS | readable 5/5 sampled (prose >=200 chars, garbled-token fraction <0.35); median sampled prose 2994 chars; garbled 0 |
| demos_run | PASS | demos present in 5/5 sampled; all ran (ok=5, skipped=0); JAH-BIOF-000001: ran, stdout byte-matches expected_output; JAH-BIOF-000002: ran, stdout byte-matches expected_output; JAH-BIOF-000003: ran, stdout byte-matches expected_output; JAH-BIOF-000004: ran, stdout byte-matches expected_output; JAH-BIOF-000005: ran, stdout byte-matches expected_output |
| links_resolve | PASS | page exists; markers exhaustive=True merger=True stCount=True old_loader=False; index file present locally (/home/hatch/workspace/jah-databases-data-2/data/biofonics/index.jsonl.gz) |
| citations_present | PASS | source/citations/src present in 5/5 sampled; JCC v1 code formable, e.g. JAHDB/biofonics#JAH-BIOF-000001+k=32d2ef75 |

Demo totals (sampled): present 5, ran OK 5, output mismatch 0, failed 0, skipped 0.

## Notes

- images: 0/5 sampled records carry an image field

## What this verdict means

Usable as-is: spec present, index loads, counts agree, records parse and read, demos run, links resolve, citations present. No remediation needed from review mode; the full-file-check program's own verification still applies before anything is called done.

## How this extends the full-file-check program

The census assigns this database a class from a network-wide scan; review mode reads this one database end to end — spec, real files, executed demos, resolved links, per-record citations — and gives a verdict with evidence. It does not replace the census, the priority queue, or the fill waves.
