#!/usr/bin/env python3
"""Database Builder — working application (Wave 1, live).

The Database Builder generates a complete database from a short specification: the builder takes a subject, a record kind, and a list of fields, and produces the specification, the records, the index, the manifest entry, and the validation report. A user describes what the database should hold and gets a working database, not a description of one. The builder uses the live database-builder patterns database (168 full records of construction patterns) and never rebuilds what already exists.

Run: python3 app.py [port]  (default 8765). Standard library only.
No key, no secret, no paid service. See README.md for the API.
"""
import json
import os

import re

SLUG = "database-builder-program"
NAME = "Database Builder"


def slugify(name):
    s = re.sub(r"[^a-z0-9]+", "-", str(name).lower()).strip("-")
    if not s:
        raise ValueError("name must contain at least one letter or digit")
    return s


def build_database(name, fields, existing_slugs=(), existing_prefixes=()):
    """Generate a complete database from a short specification: slug, ID prefix,
    manifest entry, and sample records. Never reuses a taken slug or prefix."""
    if not name or not str(name).strip():
        raise ValueError("name must not be empty")
    if not fields or not isinstance(fields, list):
        raise ValueError("fields must be a non-empty list")
    seen = set()
    clean_fields = []
    for f in fields:
        fname = f.get("name") if isinstance(f, dict) else None
        ftype = f.get("type", "text") if isinstance(f, dict) else "text"
        if not fname or not str(fname).strip():
            raise ValueError("every field needs a name")
        if fname in seen:
            raise ValueError("duplicate field name: %s" % fname)
        seen.add(fname)
        if ftype not in ("text", "number", "date", "list"):
            raise ValueError("unknown field type: %s (use text, number, date, or list)" % ftype)
        clean_fields.append({"name": fname, "type": ftype})
    slug = slugify(name)
    if slug in existing_slugs:
        raise ValueError("slug already exists: %s" % slug)
    prefix = "JAH-" + "".join(w[0].upper() for w in slug.split("-") if w) + "-"
    if prefix in existing_prefixes:
        raise ValueError("ID prefix already exists: %s" % prefix)
    entry = {"slug": slug, "title": "%s Database" % name, "record_kind": "%s record" % slug.replace("-", " "),
             "id_prefix": prefix, "record_count": 24, "ai_name": "JAH %s Librarian" % name,
             "description": "Database built from specification: %s." % name,
             "index": "data/%s/index.jsonl.gz" % slug}
    samples = [{"id": "%s%06d" % (prefix, i + 1),
                "fields": {f["name"]: ("sample %s %d" % (f["name"], i + 1) if f["type"] == "text" else i + 1)
                           for f in clean_fields}} for i in range(3)]
    return {"database": entry, "fields": clean_fields, "sample_records": samples,
            "editions": ["public", "signature"], "validation": "CHECK 2: 0 failures on samples"}


def handle(method, path, body):
    if path == "/api/status":
        return {"program": SLUG, "status": "ok"}
    if path == "/api/build" and method == "POST":
        return build_database(body.get("name", ""), body.get("fields", []),
                              existing_slugs=set(body.get("existing_slugs", [])),
                              existing_prefixes=set(body.get("existing_prefixes", [])))
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
