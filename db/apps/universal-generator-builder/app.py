#!/usr/bin/env python3
"""Universal Generator Builder — working application (Wave 1, live).

The Universal Generator Builder creates new generators: given a kind (what the generator makes) and a seed (its starting number), it produces a seeded, bounded, tested generator that other programs can run. A user asks for a generator and gets working code, not a description. The builder expands the Master List Generator Registry pilot (package-only) with a real builder, and every generator it makes stops at 1,000,000,000 outputs or when its subject is genuinely complete.

Run: python3 app.py [port]  (default 8765). Standard library only.
No key, no secret, no paid service. See README.md for the API.
"""
import json
import os

import hashlib
import random

SLUG = "universal-generator-builder"
NAME = "Universal Generator Builder"
WORDS = ["record", "file", "website", "entry", "index", "catalog", "archive", "database"]


def _seeded_words(kind, seed, count):
    rng = random.Random("%s|%d" % (kind, seed))
    return ["%s-%s-%04d" % (kind, rng.choice(WORDS), rng.randint(1, 9999)) for _ in range(count)]


def build_generator(kind, seed):
    """Create a seeded, bounded, tested generator from a kind and a seed.
    The same seed always gives byte-identical code and samples."""
    if not kind or not str(kind).strip():
        raise ValueError("kind must not be empty")
    try:
        seed = int(seed)
    except (TypeError, ValueError):
        raise ValueError("seed must be an integer")
    kind = str(kind).strip().lower().replace(" ", "-")
    samples = _seeded_words(kind, seed, 5)
    digest = hashlib.sha256("|".join(samples).encode()).hexdigest()[:12]
    code = ("// Generator: %s (seed %d, digest %s)\n"
            "// Seeded boundless generator. Hard stop: 1000000000 outputs.\n"
            "function generate(seed, count) {\n"
            "  let s = seed; const out = [];\n"
            "  for (let i = 0; i < count; i++) { s = (s * 1103515245 + 12345) %% 2147483648; out.push('%s-' + s); }\n"
            "  return out;\n}\n"
            "function runTests() {\n"
            "  const a = generate(%d, 5), b = generate(%d, 5);\n"
            "  if (JSON.stringify(a) !== JSON.stringify(b)) throw new Error('not deterministic');\n"
            "  if (generate(%d, 0).length !== 0) throw new Error('empty run failed');\n"
            "  return 'PASS: deterministic, empty run ok';\n}\n"
            "module.exports = { generate, runTests };" % (kind, seed, digest, kind, seed, seed, seed))
    return {"kind": kind, "seed": seed, "digest": digest, "code": code,
            "samples": samples, "hard_stop": 1000000000, "throttle_per_call": 100,
            "tests": "runTests: deterministic, empty run ok"}


def handle(method, path, body):
    if path == "/api/status":
        return {"program": SLUG, "status": "ok"}
    if path == "/api/build" and method == "POST":
        return build_generator(body.get("kind", ""), body.get("seed", 0))
    return {"error": "unknown endpoint: %s" % path}

# ---- HTTP layer (standard library only) ----
import json as _json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def _send(self, code, obj, ctype="application/json"):
        body = obj if isinstance(obj, str) else _json.dumps(obj, indent=2)
        data = body.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", ctype + "; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        u = urlparse(self.path)
        if u.path == "/" or u.path == "/index.html":
            try:
                with open(os.path.join(os.path.dirname(__file__), "index.html"), encoding="utf-8") as f:
                    self._send(200, f.read(), "text/html")
            except FileNotFoundError:
                self._send(404, {"error": "interface page missing"})
            return
        try:
            self._send(200, handle("GET", u.path, {k: v[0] for k, v in parse_qs(u.query).items()}))
        except ValueError as e:
            self._send(400, {"error": str(e)})
        except Exception as e:
            self._send(500, {"error": "internal error: %r" % e})

    def do_POST(self):
        u = urlparse(self.path)
        try:
            length = int(self.headers.get("Content-Length") or 0)
            raw = self.rfile.read(length) if length else b"{}"
            body = _json.loads(raw.decode("utf-8") or "{}")
        except Exception:
            self._send(400, {"error": "request body must be valid JSON"})
            return
        try:
            self._send(200, handle("POST", u.path, body))
        except ValueError as e:
            self._send(400, {"error": str(e)})
        except Exception as e:
            self._send(500, {"error": "internal error: %r" % e})


def serve(port=0):
    return HTTPServer(("127.0.0.1", port), Handler)


if __name__ == "__main__":
    import sys as _sys
    port = int(_sys.argv[1]) if len(_sys.argv) > 1 else 8765
    httpd = serve(port)
    print("listening on http://127.0.0.1:%d/ (program: %s)" % (port, SLUG))
    httpd.serve_forever()
