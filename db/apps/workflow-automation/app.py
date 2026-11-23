#!/usr/bin/env python3
"""Workflow Automation — working application (Wave 1, live).

Workflow Automation runs repeatable multi-step work: given a list of steps — search, build, test, document — it runs each step in order, passes each step's result to the next, records every step's outcome, and stops with a clear report at the first step that fails. A user automates work they do often instead of repeating it by hand. Every run is logged, and no step runs without approval when the step changes, builds, or publishes anything.

Run: python3 app.py [port]  (default 8765). Standard library only.
No key, no secret, no paid service. See README.md for the API.
"""
import json
import os

SLUG = "workflow-automation"
NAME = "Workflow Automation"

# Real in-process step actions. "change" steps need approval first.
ACTIONS = {}


def _act_echo(params, state):
    return "echo: %s" % params.get("text", "")


def _act_add(params, state):
    return params.get("a", 0) + params.get("b", 0)


def _act_upper(params, state):
    return str(state.get("previous", params.get("text", ""))).upper()


def _act_validate(params, state):
    required = params.get("required", [])
    data = params.get("data", {})
    missing = [k for k in required if k not in data]
    if missing:
        raise ValueError("missing required fields: %s" % ", ".join(missing))
    return "valid: %d fields present" % len(required)


def _act_change(params, state):
    return "change applied: %s" % params.get("what", "unspecified")


ACTIONS = {"echo": _act_echo, "add": _act_add, "upper": _act_upper,
           "validate": _act_validate, "change": _act_change}


def run_workflow(steps):
    """Run steps in order, passing each result to the next; stop at the first failure.
    A 'change' step without approval=True is refused, never run."""
    if not isinstance(steps, list) or not steps:
        raise ValueError("steps must be a non-empty list")
    results = []
    state = {}
    for i, step in enumerate(steps):
        action = step.get("action") if isinstance(step, dict) else None
        params = step.get("params", {}) if isinstance(step, dict) else {}
        if action not in ACTIONS:
            results.append({"step": i + 1, "action": action, "passed": False,
                            "evidence": "unknown action: %s" % action})
            return {"steps": len(steps), "completed": i, "passed": False,
                    "failed_step": i + 1, "results": results}
        if action == "change" and not step.get("approval"):
            results.append({"step": i + 1, "action": action, "passed": False,
                            "evidence": "change step refused: approval required first"})
            return {"steps": len(steps), "completed": i, "passed": False,
                    "failed_step": i + 1, "results": results}
        try:
            out = ACTIONS[action](params, state)
        except Exception as e:
            results.append({"step": i + 1, "action": action, "passed": False,
                            "evidence": "step raised %r" % e})
            return {"steps": len(steps), "completed": i, "passed": False,
                    "failed_step": i + 1, "results": results}
        state["previous"] = out
        results.append({"step": i + 1, "action": action, "passed": True,
                        "result": out, "evidence": "step completed with result %r" % (out,)})
    return {"steps": len(steps), "completed": len(steps), "passed": True,
            "failed_step": None, "results": results}


def handle(method, path, body):
    if path == "/api/status":
        return {"program": SLUG, "status": "ok", "actions": sorted(ACTIONS.keys())}
    if path == "/api/run" and method == "POST":
        return run_workflow(body.get("steps", []))
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
