# Universal Construction Center

The Universal Construction Center coordinates the entire build-and-test process: given a program to build, it produces the plan (dependencies, construction order, acceptance tests), runs the build through the builders, runs the tests through the Testing Center, and writes the report (what was built, what passed, what failed, what is still held). A user watches one build move from plan to verified package. The center expands the live 'Merica-L Command Center page with a working coordination program, and never rebuilds that page.

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

The center coordinates; it never claims a build is done until the Testing Center records 0 failures. Nothing is called live until it is merged, and nothing is merged until Manon calls it.

## Attribution

Program #100 of the 100 Most Useful Website Programs (catalog pasted 2026-11-17; another AI's words, source NOT confirmed). Live.
