# Universal Generator Builder

The Universal Generator Builder creates new generators: given a kind (what the generator makes) and a seed (its starting number), it produces a seeded, bounded, tested generator that other programs can run. A user asks for a generator and gets working code, not a description. The builder expands the Master List Generator Registry pilot (package-only) with a real builder, and every generator it makes stops at 1,000,000,000 outputs or when its subject is genuinely complete.

## Run

```
python3 app.py [port]   # default port 8765; standard library only
```

Open http://127.0.0.1:8765/ for the interface, or call the API directly.

## API

- `GET /api/status` — the program answers with its name, status, and counts.
- See `app.py` `handle()` for the program's working calls; each one is documented there.
- A malformed call is answered with HTTP 400 and a clear error naming the problem.

## Tests

```
python3 -m unittest discover -s tests -v
```

Every test names what it proves. All tests must pass (0 failures).

## Boundary

Generators make real data for their database and follow its standards. Generated content is labeled simulated where the standing rules require it, and never presented as an authentic public record.

## Attribution

Program #91 of the 100 Most Useful Website Programs (catalog pasted 2026-11-17; another AI's words, source NOT confirmed). Live.
