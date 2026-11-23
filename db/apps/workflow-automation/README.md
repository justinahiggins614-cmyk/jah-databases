# Workflow Automation

Workflow Automation runs repeatable multi-step work: given a list of steps — search, build, test, document — it runs each step in order, passes each step's result to the next, records every step's outcome, and stops with a clear report at the first step that fails. A user automates work they do often instead of repeating it by hand. Every run is logged, and no step runs without approval when the step changes, builds, or publishes anything.

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

Automation runs approved steps only. A step that changes, builds, or publishes anything waits for approval, and no workflow ever touches a key, secret, payment, or locked live record.

## Attribution

Program #5 of the 100 Most Useful Website Programs (catalog pasted 2026-11-17; another AI's words, source NOT confirmed). Live.
