# AI Agent Builder

The AI Agent Builder creates specialized AI agents: given a name and a list of duties, it produces the agent's specification, its plain-words instructions, its tools, and its tests. A user describes the specialist they need and gets a working agent, not a description of one. Every agent it builds is registered in the Signature AI Phone Book (63,500 registered AIs), which stays the canonical identity source — the builder adds to it, never rebuilds it.

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

Agents are built from reusable components and registered honestly. No agent claims a capability it has not passed a test for, and no agent touches a key, secret, or payment.

## Attribution

Program #3 of the 100 Most Useful Website Programs (catalog pasted 2026-11-17; another AI's words, source NOT confirmed). Live.
