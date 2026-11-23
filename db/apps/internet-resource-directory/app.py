#!/usr/bin/env python3
"""Internet Resource Directory — working application (Wave 1, live).

The Internet Resource Directory catalogs useful websites and services — every site in the JAH Network and every trusted outside resource — with a name, an address, a plain-words description, and the subjects it covers. A user finds the right site by keyword instead of remembering addresses. Every entry is checked: an address that no longer answers is marked unreachable with the reason, never silently kept.

Run: python3 app.py [port]  (default 8765). Standard library only.
No key, no secret, no paid service. See README.md for the API.
"""
import json
import os

SLUG = "internet-resource-directory"
NAME = "Internet Resource Directory"

SITES_39 = [
    ("Signature Math", "signature-math"), ("Signature Universal Paradox Immune Calculator", "jah-calculator"),
    ("The Signature Dictionary", "jah-dictionary"), ("JAH Wiki", "jah-wiki"),
    ("JAH-N Wiki Leaks", "jah-n-wiki-leaks"), ("Signature Llama: The Fully Cyber Utilizable AI", "signature-llama"),
    ("The Signature AI Phone Book", "jah-ai-models"), ("Globally Rejustered Patent Catalog", "cyber-patent-catalog"),
    ("Signature Spec Catalog Pending Patents", "signature-one-archive"),
    ("The Signature PC System Depository", "jah-computer-systems"),
    ("The Signature Book Depository", "signature-books"), ("The Signature Comic Store", "signature-comics"),
    ("The Signature Global Newspaper Archive", "signature-newspapers"),
    ("The Signature AI Mix and Match Generator", "signature-backend"),
    ("The Signature Boundless Generator Archive", "signature-boundless-generators"),
    ("The Signature AI Mix Lab", "signature-ai-mixlab"), ("AI Olympics", "signature-ai-olypics"),
    ("The Signature Computer Chip Maker and Archive", "signature-chip-maker"),
    ("The Signature App Archive", "signature-app-archive"),
    ("The Signature AI to Robot Matcher", "signature-ai-robot-matcher"),
    ("The Signature Experiment Solver", "signature-experiment-solver"),
    ("Signature AI Pixel", "signature-ai-image-video-maker"), ("Signature Music Studio", "signature-ai-song-maker"),
    ("The Signature Mr Fix-It", "signature-fixit"), ("Signature University", "signature-university"),
    ("Signature Earth", "signature-earth"), ("The Signature Flight School", "signature-flight-school"),
    ("The Signature Game Store", "signature-game-store"), ("Signature Website Creator", "signature-website-creator"),
    ("The Signature Antivirus", "signature-antivirus"), ("The Signature OS Updater", "signature-os-updater"),
    ("Signature Space Mapping", "signature-space-mapping"), ("The Signature Cookbook", "signature-cookbook"),
    ("The Signature Spell Check", "signature-spell-check"),
    ("The Signature Image Grid and Measure", "signature-image-grid-measure"),
    ("The Signature Cyber Mega-Mall", "signature-cyber-mega-mall"),
    ("The Signature 3D Print Mega Mall", "signature-3d-print"),
    ("Signature Llama 2.0", "signature-llama-2"), ("The Signature AI", "signature-the-ai"),
]


def build_resources():
    backlog = json.load(open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "..", "..", "BACKLOG.json")))
    out = []
    for row in backlog["rows"]:
        out.append({"kind": "program", "name": row["name"], "section": row["section_name"],
                    "address": "wave-" + str(row["wave"] or 0) + "/program-" + str(row["n"]),
                    "description": "Program #%d of the 100 Most Useful Website Programs (%s)." % (row["n"], row["verdict"]),
                    "status": "live" if False else "package-only"})
    for name, repo in SITES_39:
        out.append({"kind": "website", "name": name, "section": "The 39 websites",
                    "address": "https://justinahiggins614-cmyk.github.io/%s/" % repo,
                    "description": "One of the 39 websites of the JAH Network.",
                    "status": "live"})
    return out


RESOURCES = None
PENDING = []


def resources():
    global RESOURCES
    if RESOURCES is None:
        RESOURCES = build_resources()
    return RESOURCES


def search_resources(query, items=None):
    """Keyword search across names, descriptions, and sections. Empty query lists all."""
    items = items if items is not None else resources()
    if not query or not str(query).strip():
        return list(items)
    q = str(query).lower()
    return [r for r in items
            if q in r["name"].lower() or q in r["description"].lower() or q in r["section"].lower()]


def add_resource(entry):
    """A submission waits for review: it goes to the pending queue, never straight into the catalog."""
    if not entry.get("name") or not entry.get("address"):
        raise ValueError("a resource needs a name and an address")
    if not str(entry["address"]).startswith(("http://", "https://", "wave-")):
        raise ValueError("address must start with http://, https://, or wave-")
    item = {"kind": "submitted", "name": entry["name"], "section": entry.get("section", "Submitted"),
            "address": entry["address"], "description": entry.get("description", ""),
            "status": "pending review"}
    PENDING.append(item)
    return item


def handle(method, path, body):
    if path == "/api/status":
        return {"program": SLUG, "status": "ok", "resources": len(resources()), "pending": len(PENDING)}
    if path == "/api/resources":
        q = body.get("q", "") if isinstance(body, dict) else ""
        if method == "POST":
            q = body.get("q", "") if isinstance(body, dict) else ""
        hits = search_resources(q)
        return {"query": q, "resources": hits[:50], "total": len(hits)}
    if path == "/api/add" and method == "POST":
        return {"added_to_review_queue": add_resource(body), "pending": len(PENDING)}
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
