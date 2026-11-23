# AI Code Reader

The AI Code Reader inspects source code and explains it in plain words: what each function does, what each class holds, what the program imports, and how data flows through it. A user who did not write the code can still understand it and change it safely. The reader never runs untrusted code: it reads the text of the file, and only runs code the user has approved.

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

The reader reads code text only and never executes untrusted code. It never sends code anywhere, never stores a user's private code, and never claims to understand a language it cannot parse.

## Attribution

Program #7 of the 100 Most Useful Website Programs (catalog pasted 2026-11-17; another AI's words, source NOT confirmed). Live.
