# Documentation Generator

The Documentation Generator produces technical documentation from code and a specification: given a program's name, purpose, interfaces, and tests, it writes the full document — purpose in plain words, every interface with its inputs and outputs, every term defined on first use, and every test with what it proves. A user gets documentation that matches the program, because it is generated from the program itself, not written from memory.

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

Documentation is generated from the program itself. It never describes a feature the program does not have, and never copies text from another site without naming the source.

## Attribution

Program #30 of the 100 Most Useful Website Programs (catalog pasted 2026-11-17; another AI's words, source NOT confirmed). Live.
