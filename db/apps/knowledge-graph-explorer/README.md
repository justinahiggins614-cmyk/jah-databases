# Knowledge Graph Explorer

The Knowledge Graph Explorer walks relationships between concepts: starting from one concept, it follows links — a program depends on another, a database records a subject, a website belongs to the network — and shows the path it took. A user explores how things connect instead of reading lists. The explorer builds on the advdb-universal-knowledge-graph and cross-database-knowledge-graph record databases and the Master List ai-kg pilot (package-only), and never rebuilds them.

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

The graph shows relationships that exist in the records. It never invents a link, and a suggested link is labeled as a suggestion with its basis, never as a fact.

## Attribution

Program #19 of the 100 Most Useful Website Programs (catalog pasted 2026-11-17; another AI's words, source NOT confirmed). Live.
