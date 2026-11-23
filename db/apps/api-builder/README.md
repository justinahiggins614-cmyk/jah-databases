# API Builder

The API Builder creates interfaces for software systems: given a list of resources (things the system holds) and their fields, it produces a machine-readable contract — the OpenAPI specification — plus working server code, documentation, and tests. A user describes the system and gets a working interface, not a description of one. The builder uses the ai-build REST and GraphQL API builder record databases as its pattern library and never rebuilds them.

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

The builder never bakes in a key, secret, or credential, and never handles payments or card data. Interfaces are public contracts; access control is a separate, defensive decision.

## Attribution

Program #27 of the 100 Most Useful Website Programs (catalog pasted 2026-11-17; another AI's words, source NOT confirmed). Live.
