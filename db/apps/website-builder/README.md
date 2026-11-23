# Website Builder

The Website Builder creates complete websites from a title and a list of sections: front door, tab pages, catalog page, network navigation at the bottom, and an accessible plain version. A user describes the site and gets a working website, not a description of one. The builder expands the live Signature Website Creator (live-view editing) with templates, an API, documentation, and tests, and never rebuilds what that site already does.

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

The builder copies layout structure only (layout inspiration). It never copies another site's brand name, logo, trademark, product names, or copyrighted images.

## Attribution

Program #21 of the 100 Most Useful Website Programs (catalog pasted 2026-11-17; another AI's words, source NOT confirmed). Live.
