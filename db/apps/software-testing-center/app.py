#!/usr/bin/env python3
"""Software Testing Center — working application (Wave 1, live).

The Software Testing Center executes test suites and records every pass and fail: given a list of tests — each a small program plus the output it should produce — it runs each one, compares actual output with expected output, and reports the result with the evidence. A user proves a program works instead of believing it does. The center is the verification arm of the whole 100-program build: no program counts as built until this center records 0 failures for it.

Run: python3 app.py [port]  (default 8765). Standard library only.
No key, no secret, no paid service. See README.md for the API.
"""
import json
import os

import io
from contextlib import redirect_stdout

SLUG = "software-testing-center"
NAME = "Software Testing Center"


def run_one(test):
    """Run one test: execute its code, compare stdout with expected output."""
    name = test.get("name", "unnamed")
    code = test.get("code", "")
    expected = test.get("expected", "")
    buf = io.StringIO()
    try:
        with redirect_stdout(buf):
            exec(compile(code, "<test:%s>" % name, "exec"), {"__name__": "__main__"})
    except Exception as e:
        return {"name": name, "passed": False, "expected": expected, "actual": "",
                "evidence": "test raised %r" % e}
    actual = buf.getvalue()
    passed = actual == expected
    return {"name": name, "passed": passed, "expected": expected, "actual": actual,
            "evidence": ("output matched expected output byte for byte"
                         if passed else "output differed: expected %r, got %r" % (expected, actual))}


def run_tests(tests):
    """Execute a whole suite in isolation: one failure never stops the others."""
    if not isinstance(tests, list):
        raise ValueError("tests must be a list")
    results = [run_one(t) for t in tests]
    passed = sum(1 for r in results if r["passed"])
    return {"suite": len(results), "passed": passed, "failed": len(results) - passed,
            "results": results,
            "verdict": "pass" if passed == len(results) else "fail"}


def handle(method, path, body):
    if path == "/api/status":
        return {"program": SLUG, "status": "ok"}
    if path == "/api/run" and method == "POST":
        return run_tests(body.get("tests", []))
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
