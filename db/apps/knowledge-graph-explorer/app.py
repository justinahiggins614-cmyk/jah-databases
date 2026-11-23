#!/usr/bin/env python3
"""Knowledge Graph Explorer — working application (Wave 1, live).

The Knowledge Graph Explorer walks relationships between concepts: starting from one concept, it follows links — a program depends on another, a database records a subject, a website belongs to the network — and shows the path it took. A user explores how things connect instead of reading lists. The explorer builds on the advdb-universal-knowledge-graph and cross-database-knowledge-graph record databases and the Master List ai-kg pilot (package-only), and never rebuilds them.

Run: python3 app.py [port]  (default 8765). Standard library only.
No key, no secret, no paid service. See README.md for the API.
"""
import json
import os

from collections import deque

SLUG = "knowledge-graph-explorer"
NAME = "Knowledge Graph Explorer"

# Dependency edges from BUILD-SPEC.md: program -> programs it needs first.
EDGES = {
    81: [], 82: [81], 11: [], 7: [], 12: [11], 21: [12], 91: [12], 27: [],
    3: [91, 82], 19: [11], 76: [7], 30: [7], 5: [76, 27], 92: [91],
    100: [5, 76, 91, 92], 13: [11, 81], 15: [11], 17: [12], 20: [11, 15],
    28: [27], 14: [11, 20], 18: [19], 2: [81, 19], 6: [19, 81], 74: [],
    75: [76], 78: [], 77: [78], 89: [82], 90: [89, 5], 22: [21], 23: [21, 76],
    24: [23, 21], 25: [81, 13], 26: [21, 12], 29: [21, 27], 93: [21, 91],
    94: [12, 91], 95: [3, 91], 8: [7, 3], 9: [7, 76], 4: [3, 5], 96: [100, 5],
    1: [100, 3, 5], 10: [3, 19], 31: [2, 81], 32: [2, 31], 33: [76], 34: [33],
    35: [33], 36: [31], 37: [31], 38: [33], 39: [33], 40: [31, 39], 86: [82, 81],
    87: [81], 97: [2, 31], 98: [35, 33], 99: [100, 97], 42: [30], 43: [30],
    44: [42], 41: [42, 43, 44], 45: [42, 19], 46: [30], 47: [30], 48: [82, 81],
    49: [19], 50: [41, 45], 83: [82], 84: [81], 85: [81], 88: [], 16: [15, 11],
    51: [], 52: [5], 53: [33], 54: [53], 55: [52], 56: [52], 57: [53], 58: [20],
    59: [58], 60: [39, 81], 61: [], 62: [61], 63: [], 64: [63, 78], 65: [52, 61],
    66: [31], 67: [98, 35], 68: [64], 69: [65, 55], 70: [65, 87], 71: [78, 77],
    72: [71], 73: [7, 76], 79: [71], 80: [74, 78],
}


def neighbours(n):
    """Everything directly linked to program n: what it needs, and what needs it."""
    if n not in EDGES:
        raise ValueError("no such program: %s" % n)
    needs = list(EDGES[n])
    needed_by = sorted(m for m, ds in EDGES.items() if n in ds)
    return {"program": n, "depends_on": needs, "needed_by": needed_by}


def shortest_path(a, b):
    """Shortest path between two programs, link by link (undirected walk)."""
    if a not in EDGES or b not in EDGES:
        raise ValueError("unknown program in path request")
    if a == b:
        return [a]
    adj = {n: set(ds) | {m for m, ds in EDGES.items() if n in ds} for n, ds in EDGES.items()}
    prev = {a: None}
    queue = deque([a])
    while queue:
        cur = queue.popleft()
        for nxt in sorted(adj[cur]):
            if nxt not in prev:
                prev[nxt] = cur
                if nxt == b:
                    path = [b]
                    while path[-1] != a:
                        path.append(prev[path[-1]])
                    return list(reversed(path))
                queue.append(nxt)
    return []


def handle(method, path, body):
    if path == "/api/status":
        return {"program": SLUG, "status": "ok", "concepts": len(EDGES)}
    if path == "/api/neighbors":
        n = body.get("n", "") if isinstance(body, dict) else ""
        if method == "POST":
            n = body.get("n", "")
        return neighbours(int(n))
    if path == "/api/path":
        a = body.get("a", "") if isinstance(body, dict) else ""
        b = body.get("b", "") if isinstance(body, dict) else ""
        if method == "POST":
            a, b = body.get("a", ""), body.get("b", "")
        return {"path": shortest_path(int(a), int(b))}
    if path == "/api/graph":
        return {"edges": {str(k): v for k, v in EDGES.items()}}
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
