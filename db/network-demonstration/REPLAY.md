# REPLAY.md — Reproducing the Network Demonstration

The Network Demonstration Database proves the JAH Databases network by doing,
not by claiming: a real request goes in, the live databases are queried, the
archive-aware generators compose a full result, every claim is verified against
the source records, and the result is saved for reuse.

## The pipeline (5 stages)

1. **Intake** — the request is taken as typed, or from a preset request.
2. **Database access** — the live manifest is searched; the matching databases'
   real record indexes are fetched over the network. The page shows exactly
   which databases were consulted, with links to each one.
3. **Specialized generation** — the demonstration generator composes a full,
   useful artifact (blueprint spec, history report, workout plan, recipe,
   how-it-works guide, research brief) from the cited records.
4. **Verification** — every cited record ID is confirmed present in its live
   index; quoted text is matched character-for-character against the source
   record; any arithmetic is recomputed independently. Pass/fail per check.
5. **Saved** — the artifact downloads as a JSON file; a made-with entry
   (what was made, which databases were used, the result, verification) is
   prepared for the Made-With Databases Archive pattern; the run is appended
   to the replay log (this device) for step-by-step replay.

## The five canonical presets (deterministic)

| Preset | Request | Databases consulted |
|---|---|---|
| `solar-workshop` | Design a blueprint spec for a small solar workshop | blueprints, solar-energy-systems-engineers, architecture |
| `boeing-747` | Give me the history and key specs of the Boeing 747 | aircraft-boeing-747, aviation |
| `bodyweight-workout` | Build me a beginner bodyweight workout plan | exercise, fitness |
| `bread-recipe` | Give me a full bread recipe with step-by-step instructions | cookbook |
| `printer-guide` | Explain how a 3D printer works and what I need to start | public-3d-print-archive, signature-3d-print |

Preset requests are deterministic: same request → same databases → same checks.

## Reproduce in the browser

1. Open `db/network-demonstration/` (live: the JAH Databases hub → this database).
2. Press any preset button (or type your own request and press **Run demonstration**).
3. Watch the five stages render: intake → database access (with links) →
   generation → verification table → saved artifact.
4. Deep-link a preset: `?demo=solar-workshop` (also `boeing-747`,
   `bodyweight-workout`, `bread-recipe`, `printer-guide`).
5. Open the **Replay Log** tab: every run is recorded with its steps.
   Export it as JSON.

## Reproduce headlessly

```bash
cd ~/workspace/jah-databases
python3 code/demo_replay.py               # replay all five presets
python3 code/demo_replay.py solar-workshop # replay one preset
python3 code/demo_replay.py --list         # list presets
```

The script reads the local `data/manifest.json` and the real database index
files (both the main repo `data/` and the `jah-databases-data-1` shard),
asserts every pipeline stage, and exits 0 only if all checks pass.
Expected result: `TOTAL: 41/41 checks passed`, exit 0.

## What "verified" means here

- Cited record IDs are looked up in the live-fetched index of the database
  that supposedly holds them — not trusted from a label.
- Quoted excerpts (Boeing 747 run) are matched as substrings of the fetched
  source record descriptions.
- The solar sizing arithmetic is recomputed from scratch in the verifier and
  compared value-by-value (daily load, panel count, array wattage, battery Ah,
  roof fit).
- Free-text (non-preset) requests use the same keyword scoring over the live
  manifest, so any request is answerable and checkable the same way.

## Files

- `db/network-demonstration/index.html` — the interactive demonstration page
- `db/network-demonstration/gen-network-demonstration.js` — the boundless generator (jahdb-network-demonstration-1.0)
- `db/network-demonstration/REPLAY.md` — this file
- `code/demo_replay.py` — headless replay + assertions
- Data: `jah-databases-data-1/data/network-demonstration/` (index + chunks)

Property of Justin Addam Higgins (JAH).
