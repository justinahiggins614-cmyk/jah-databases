# Meta-Generator Builder

The Meta-Generator Builder creates systems that build generators: given a generator kind (what the built generators will make), it produces a builder — a program that, when run, creates seeded, bounded, tested generators of that kind. A user asks for a way to make generators and gets a working builder, not a description. It sits one level above the Universal Generator Builder (#91): the meta-builder builds the builder, the builder builds the generator, the generator builds the records.

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

Meta-generation stays inside the same rules as generation: seeded, bounded, tested, labeled where required, and never presented as an authentic public record.

## Attribution

Program #92 of the 100 Most Useful Website Programs (catalog pasted 2026-11-17; another AI's words, source NOT confirmed). Live.
