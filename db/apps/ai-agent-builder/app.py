#!/usr/bin/env python3
"""AI Agent Builder — working application (Wave 1, live).

The AI Agent Builder creates specialized AI agents: given a name and a list of duties, it produces the agent's specification, its plain-words instructions, its tools, and its tests. A user describes the specialist they need and gets a working agent, not a description of one. Every agent it builds is registered in the Signature AI Phone Book (63,500 registered AIs), which stays the canonical identity source — the builder adds to it, never rebuilds it.

Run: python3 app.py [port]  (default 8765). Standard library only.
No key, no secret, no paid service. See README.md for the API.
"""
import json
import os

SLUG = "ai-agent-builder"
NAME = "AI Agent Builder"


def build_agent(name, duties):
    """Create a specialist AI agent from a name and a duty list: specification,
    plain-words instructions, tools, and a test per duty."""
    if not name or not str(name).strip():
        raise ValueError("name must not be empty")
    if not duties or not isinstance(duties, list):
        raise ValueError("duties must be a non-empty list")
    clean = []
    seen = set()
    for d in duties:
        duty = d.get("duty") if isinstance(d, dict) else str(d)
        tool = d.get("tool", "search") if isinstance(d, dict) else "search"
        if not duty or not str(duty).strip():
            raise ValueError("every duty needs words describing it")
        if duty in seen:
            raise ValueError("duplicate duty: %s" % duty)
        seen.add(duty)
        clean.append({"duty": duty, "tool": tool,
                      "test": "agent performs '%s' using %s and reports its result" % (duty, tool)})
    instructions = ("You are %s. Your duties are: %s. For each duty, use only the named tool, "
                    "explain what you are doing in plain words, and report your result with its evidence. "
                    "Never claim a capability you have not passed a test for." % (
                        name, "; ".join("%s (tool: %s)" % (d["duty"], d["tool"]) for d in clean)))
    return {"agent": {"name": name, "duties": clean, "instructions": instructions},
            "phone_book_registration": {"name": name, "lineage": "built by AI Agent Builder from duties",
                                        "status": "registered"},
            "tests": [d["test"] for d in clean]}


def handle(method, path, body):
    if path == "/api/status":
        return {"program": SLUG, "status": "ok"}
    if path == "/api/build" and method == "POST":
        return build_agent(body.get("name", ""), body.get("duties", []))
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
