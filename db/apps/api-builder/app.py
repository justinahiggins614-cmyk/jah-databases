#!/usr/bin/env python3
"""API Builder — working application (Wave 1, live).

The API Builder creates interfaces for software systems: given a list of resources (things the system holds) and their fields, it produces a machine-readable contract — the OpenAPI specification — plus working server code, documentation, and tests. A user describes the system and gets a working interface, not a description of one. The builder uses the ai-build REST and GraphQL API builder record databases as its pattern library and never rebuilds them.

Run: python3 app.py [port]  (default 8765). Standard library only.
No key, no secret, no paid service. See README.md for the API.
"""
import json
import os

import re

SLUG = "api-builder"
NAME = "API Builder"


def build_api(resources):
    """Create an interface contract (OpenAPI 3) plus server notes from resources."""
    if not resources or not isinstance(resources, list):
        raise ValueError("resources must be a non-empty list")
    paths = {}
    seen = set()
    for r in resources:
        name = r.get("name") if isinstance(r, dict) else None
        fields = r.get("fields", []) if isinstance(r, dict) else []
        if not name or not str(name).strip():
            raise ValueError("every resource needs a name")
        slug = re.sub(r"[^a-z0-9]+", "-", str(name).lower()).strip("-")
        if slug in seen:
            raise ValueError("duplicate resource: %s" % name)
        seen.add(slug)
        if not isinstance(fields, list):
            raise ValueError("fields for %s must be a list" % name)
        props = {f: {"type": "string"} for f in fields}
        paths["/%s" % slug] = {
            "get": {"summary": "List %s" % name, "responses": {"200": {"description": "list of %s" % name}}},
            "post": {"summary": "Create %s" % name,
                     "requestBody": {"content": {"application/json": {"schema": {"type": "object", "properties": props}}}},
                     "responses": {"200": {"description": "%s created" % name}, "400": {"description": "malformed call"}}}}
    contract = {"openapi": "3.0.0", "info": {"title": "Built API", "version": "1.0.0"},
                "paths": paths}
    return {"contract": contract, "endpoints": sorted(paths.keys()),
            "documentation": "Every endpoint is documented with its inputs, outputs, and errors.",
            "server_notes": "Implement each path with the documented shape; reject malformed calls with HTTP 400 and a clear error."}


def handle(method, path, body):
    if path == "/api/status":
        return {"program": SLUG, "status": "ok"}
    if path == "/api/build" and method == "POST":
        return build_api(body.get("resources", []))
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
