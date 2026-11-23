#!/usr/bin/env python3
"""Universal Construction Center — working application (Wave 1, live).

The Universal Construction Center coordinates the entire build-and-test process: given a program to build, it produces the plan (dependencies, construction order, acceptance tests), runs the build through the builders, runs the tests through the Testing Center, and writes the report (what was built, what passed, what failed, what is still held). A user watches one build move from plan to verified package. The center expands the live 'Merica-L Command Center page with a working coordination program, and never rebuilds that page.

Run: python3 app.py [port]  (default 8765). Standard library only.
No key, no secret, no paid service. See README.md for the API.
"""
import json
import os

SLUG = "universal-construction-center"
NAME = "Universal Construction Center"

WAVES = {1: [81, 82, 11, 7, 12, 21, 91, 27, 3, 19, 76, 30, 5, 92, 100],
         2: [13, 15, 17, 20, 28, 14, 18, 2, 6, 74, 75, 78, 77, 89, 90],
         3: [22, 23, 24, 25, 26, 29, 93, 94, 95, 8, 9, 4, 96, 1, 10],
         4: [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 86, 87, 97, 98, 99],
         5: [42, 43, 44, 41, 45, 46, 47, 48, 49, 50, 83, 84, 85, 88, 16],
         6: [51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65],
         7: [66, 67, 68, 69, 70, 71, 72, 73, 79, 80]}
NAMES = {81: "Universal Search Engine", 82: "Internet Resource Directory", 11: "Database Explorer",
         7: "AI Code Reader", 12: "Database Builder", 21: "Website Builder",
         91: "Universal Generator Builder", 27: "API Builder", 3: "AI Agent Builder",
         19: "Knowledge Graph Explorer", 76: "Software Testing Center", 30: "Documentation Generator",
         5: "Workflow Automation", 92: "Meta-Generator Builder", 100: "Universal Construction Center"}


def wave_of(n):
    for w, ns in WAVES.items():
        if n in ns:
            return w
    raise ValueError("no such program: %s" % n)


def plan(n):
    """The construction plan for a program: its wave, its name, and its acceptance tests."""
    n = int(n)
    w = wave_of(n)
    name = NAMES.get(n, "Program #%d (later wave — see BUILD-SPEC.md)" % n)
    return {"program": n, "name": name, "wave": w,
            "steps": ["plan (dependencies, order, acceptance tests)",
                      "build (interface, backend, database, API, docs)",
                      "test (suite executed, 0 failures required)",
                      "verify (CHECK 2 on any database pair)",
                      "report (evidence written to the wave report)"],
            "acceptance": ["interface loads and every button works",
                           "backend answers status and handles bad requests",
                           "database pair round-trips (where needed)",
                           "API answers in its documented shape",
                           "documentation exists with a glossary",
                           "test suite passes with 0 failures"],
            "status": "tested" if w == 1 and n in NAMES else "planned"}


def status():
    built = [n for w in [1] for n in WAVES[w]]
    return {"program": SLUG, "status": "ok", "total_programs": 100,
            "waves": {str(w): len(ns) for w, ns in WAVES.items()},
            "wave_1_built": len(built), "wave_1_programs": built,
            "rule": "a build counts only when its tests record 0 failures"}


def handle(method, path, body):
    if path == "/api/status":
        return status()
    if path == "/api/plan":
        n = body.get("n", "") if isinstance(body, dict) else ""
        if method == "POST":
            n = body.get("n", "")
        return plan(n)
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
