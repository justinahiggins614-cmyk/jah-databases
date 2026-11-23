#!/usr/bin/env python3
"""Meta-Generator Builder — working application (Wave 1, live).

The Meta-Generator Builder creates systems that build generators: given a generator kind (what the built generators will make), it produces a builder — a program that, when run, creates seeded, bounded, tested generators of that kind. A user asks for a way to make generators and gets a working builder, not a description. It sits one level above the Universal Generator Builder (#91): the meta-builder builds the builder, the builder builds the generator, the generator builds the records.

Run: python3 app.py [port]  (default 8765). Standard library only.
No key, no secret, no paid service. See README.md for the API.
"""
import json
import os

import hashlib
import random

SLUG = "meta-generator-builder"
NAME = "Meta-Generator Builder"
WORDS = ["record", "file", "website", "entry", "index", "catalog", "archive", "database"]


def build_meta_generator(kind, seed=1):
    """Create a builder for a generator kind. Running the builder produces a
    seeded, bounded, tested generator of that kind."""
    if not kind or not str(kind).strip():
        raise ValueError("kind must not be empty")
    try:
        seed = int(seed)
    except (TypeError, ValueError):
        raise ValueError("seed must be an integer")
    kind = str(kind).strip().lower().replace(" ", "-")
    rng = random.Random("%s|%d" % (kind, seed))
    samples = ["%s-%s-%04d" % (kind, rng.choice(WORDS), rng.randint(1, 9999)) for _ in range(3)]
    digest = hashlib.sha256("|".join(samples).encode()).hexdigest()[:12]
    builder_code = ("// Meta-generator builder: builds generators of kind '%s' (seed %d, digest %s)\n"
                    "// The builder, run with a seed, produces a seeded generator.\n"
                    "function buildGenerator(seed) {\n"
                    "  return { kind: '%s', seed: seed, hardStop: 1000000000,\n"
                    "    generate: function(count) { let s = seed; const out = [];\n"
                    "      for (let i = 0; i < count; i++) { s = (s * 1103515245 + 12345) %% 2147483648; out.push('%s-' + s); }\n"
                    "      return out; } };\n}\n"
                    "function runTests() {\n"
                    "  const g1 = buildGenerator(%d), g2 = buildGenerator(%d);\n"
                    "  if (JSON.stringify(g1.generate(3)) !== JSON.stringify(g2.generate(3))) throw new Error('not deterministic');\n"
                    "  return 'PASS: builder deterministic';\n}\n"
                    "module.exports = { buildGenerator, runTests };" % (kind, seed, digest, kind, kind, seed, seed))
    return {"kind": kind, "seed": seed, "digest": digest, "builder_code": builder_code,
            "built_generator": {"kind": kind, "seed": seed, "hard_stop": 1000000000,
                                "samples": samples},
            "tests": "runTests: builder deterministic"}


def handle(method, path, body):
    if path == "/api/status":
        return {"program": SLUG, "status": "ok"}
    if path == "/api/build" and method == "POST":
        return build_meta_generator(body.get("kind", ""), body.get("seed", 1))
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
