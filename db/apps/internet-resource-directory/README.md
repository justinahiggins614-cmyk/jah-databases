# Internet Resource Directory

The Internet Resource Directory catalogs useful websites and services — every site in the JAH Network and every trusted outside resource — with a name, an address, a plain-words description, and the subjects it covers. A user finds the right site by keyword instead of remembering addresses. Every entry is checked: an address that no longer answers is marked unreachable with the reason, never silently kept.

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

The directory lists resources and links to them; it never copies a site's content, brand, logo, or trademark, and never lists a resource Manon has not approved for the catalog.

## Attribution

Program #82 of the 100 Most Useful Website Programs (catalog pasted 2026-11-17; another AI's words, source NOT confirmed). Live.
