# Software Testing Center

The Software Testing Center executes test suites and records every pass and fail: given a list of tests — each a small program plus the output it should produce — it runs each one, compares actual output with expected output, and reports the result with the evidence. A user proves a program works instead of believing it does. The center is the verification arm of the whole 100-program build: no program counts as built until this center records 0 failures for it.

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

The center runs tests on code the user has approved, in isolation. It never runs untrusted code with access to keys, secrets, or the network, and never marks a program built on an unexecuted test.

## Attribution

Program #76 of the 100 Most Useful Website Programs (catalog pasted 2026-11-17; another AI's words, source NOT confirmed). Live.
