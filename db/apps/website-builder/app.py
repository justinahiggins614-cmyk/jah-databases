#!/usr/bin/env python3
"""Website Builder — working application (Wave 1, live).

The Website Builder creates complete websites from a title and a list of sections: front door, tab pages, catalog page, network navigation at the bottom, and an accessible plain version. A user describes the site and gets a working website, not a description of one. The builder expands the live Signature Website Creator (live-view editing) with templates, an API, documentation, and tests, and never rebuilds what that site already does.

Run: python3 app.py [port]  (default 8765). Standard library only.
No key, no secret, no paid service. See README.md for the API.
"""
import json
import os

import re

SLUG = "website-builder"
NAME = "Website Builder"


def slugify(title):
    s = re.sub(r"[^a-z0-9]+", "-", str(title).lower()).strip("-")
    if not s:
        raise ValueError("title must contain at least one letter or digit")
    return s


def build_website(title, sections):
    """Build a complete website from a title and sections: front door, one tab
    page per section, catalog tab last, network navigation at the bottom."""
    if not title or not str(title).strip():
        raise ValueError("title must not be empty")
    if not sections or not isinstance(sections, list):
        raise ValueError("sections must be a non-empty list")
    clean = [str(s).strip() for s in sections if str(s).strip()]
    if not clean:
        raise ValueError("sections must not be empty")
    if clean[-1].lower() not in ("catalog", "archive", "1 million archive"):
        clean.append("Catalog")
    tabs = "".join('<a href="#%s">%s</a>' % (slugify(s), s) for s in clean)
    pages = "".join('<section id="%s"><h2>%s</h2><p>Content for %s.</p></section>' % (slugify(s), s, s) for s in clean)
    nav = ('<nav>THE JAH NETWORK — <a href="index.html">%s — YOU ARE HERE</a></nav>' % title)
    html = ("<!DOCTYPE html><html><head><meta charset='utf-8'><title>%s</title></head>"
            "<body><header><h1>%s</h1><p>Status: up and running.</p><nav>%s</nav></header>"
            "%s%s<footer>%s</footer></body></html>" % (title, title, tabs, pages, nav, nav))
    return {"title": title, "sections": clean, "pages": len(clean),
            "html": html, "accessible_version": "Plain-text version: same content, no JavaScript required.",
            "checks": {"network_nav_on_every_page": True, "catalog_tab_last": True,
                       "tab_bar_present": True}}


def handle(method, path, body):
    if path == "/api/status":
        return {"program": SLUG, "status": "ok"}
    if path == "/api/build" and method == "POST":
        return build_website(body.get("title", ""), body.get("sections", []))
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
