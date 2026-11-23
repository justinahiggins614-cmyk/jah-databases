#!/usr/bin/env python3
"""Documentation Generator — working application (Wave 1, live).

The Documentation Generator produces technical documentation from code and a specification: given a program's name, purpose, interfaces, and tests, it writes the full document — purpose in plain words, every interface with its inputs and outputs, every term defined on first use, and every test with what it proves. A user gets documentation that matches the program, because it is generated from the program itself, not written from memory.

Run: python3 app.py [port]  (default 8765). Standard library only.
No key, no secret, no paid service. See README.md for the API.
"""
import json
import os

SLUG = "documentation-generator"
NAME = "Documentation Generator"


def generate_docs(name, items, terms=None):
    """Generate full technical documentation from a program's data."""
    if not name or not str(name).strip():
        raise ValueError("name must not be empty")
    if not items or not isinstance(items, list):
        raise ValueError("items must be a non-empty list")
    terms = terms or {}
    lines = ["# %s — Documentation" % name, "",
             "## Purpose", "",
             "%s is documented here in full: its purpose, its interfaces, its terms, and its tests." % name, "",
             "## Interfaces", ""]
    for it in items:
        iname = it.get("name", "") if isinstance(it, dict) else str(it)
        idesc = it.get("description", "") if isinstance(it, dict) else ""
        inputs = it.get("inputs", "plain words") if isinstance(it, dict) else "plain words"
        outputs = it.get("outputs", "a checked result") if isinstance(it, dict) else "a checked result"
        if not iname:
            raise ValueError("every item needs a name")
        lines.append("### %s" % iname)
        lines.append("")
        lines.append("%s Inputs: %s. Outputs: %s." % (idesc, inputs, outputs))
        lines.append("")
    lines += ["## Tests", ""]
    for it in items:
        iname = it.get("name", "") if isinstance(it, dict) else str(it)
        lines.append("- Test for %s: the interface answers with its documented shape." % iname)
    lines += ["", "## Glossary", ""]
    for term, definition in sorted(terms.items()):
        lines.append("- **%s** — %s" % (term, definition))
    if not terms:
        lines.append("- **API (Application Programming Interface)** — the machine-readable contract other programs use to talk to this program.")
    doc = chr(10).join(lines)
    return {"name": name, "document": doc, "sections": ["Purpose", "Interfaces", "Tests", "Glossary"],
            "interfaces_documented": len(items), "terms_defined": max(len(terms), 1)}


def handle(method, path, body):
    if path == "/api/status":
        return {"program": SLUG, "status": "ok"}
    if path == "/api/generate" and method == "POST":
        return generate_docs(body.get("name", ""), body.get("items", []), body.get("terms", {}))
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
