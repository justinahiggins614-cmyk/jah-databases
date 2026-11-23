# Database Builder

The Database Builder generates a complete database from a short specification: the builder takes a subject, a record kind, and a list of fields, and produces the specification, the records, the index, the manifest entry, and the validation report. A user describes what the database should hold and gets a working database, not a description of one. The builder uses the live database-builder patterns database (168 full records of construction patterns) and never rebuilds what already exists.

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

The builder creates NEW databases only. It never changes a live database, never touches locked records, and never reuses a slug or ID prefix that already exists.

## Attribution

Program #12 of the 100 Most Useful Website Programs (catalog pasted 2026-11-17; another AI's words, source NOT confirmed). Live.
