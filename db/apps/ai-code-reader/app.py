#!/usr/bin/env python3
"""AI Code Reader — working application (Wave 1, live).

The AI Code Reader inspects source code and explains it in plain words: what each function does, what each class holds, what the program imports, and how data flows through it. A user who did not write the code can still understand it and change it safely. The reader never runs untrusted code: it reads the text of the file, and only runs code the user has approved.

Run: python3 app.py [port]  (default 8765). Standard library only.
No key, no secret, no paid service. See README.md for the API.
"""
import json
import os

import ast

SLUG = "ai-code-reader"
NAME = "AI Code Reader"


def read_code(source):
    """Read source code text (never execute it) and explain it in plain words."""
    if not isinstance(source, str) or not source.strip():
        raise ValueError("source code must be a non-empty string")
    lines = source.splitlines()
    result = {"lines": len(lines), "functions": [], "classes": [], "imports": [],
              "warnings": [], "explanation": ""}
    try:
        tree = ast.parse(source)
    except SyntaxError as e:
        result["warnings"].append("syntax error at line %s: %s" % (e.lineno, e.msg))
        result["explanation"] = "This file does not parse as Python, so only a line count is reported."
        return result
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            doc = (ast.get_docstring(node) or "").strip()
            result["functions"].append({"name": node.name, "line": node.lineno,
                                        "args": [a.arg for a in node.args.args],
                                        "doc": doc[:200]})
        elif isinstance(node, ast.ClassDef):
            result["classes"].append({"name": node.name, "line": node.lineno,
                                      "methods": [n.name for n in node.body if isinstance(n, ast.FunctionDef)]})
        elif isinstance(node, ast.Import):
            result["imports"].extend(a.name for a in node.names)
        elif isinstance(node, ast.ImportFrom):
            result["imports"].append(node.module or "")
    result["functions"].sort(key=lambda f: f["line"])
    result["classes"].sort(key=lambda c: c["line"])
    if "eval(" in source or "exec(" in source:
        result["warnings"].append("risky pattern: eval/exec runs text as code")
    if "os.system" in source or "subprocess" in source:
        result["warnings"].append("risky pattern: runs outside programs")
    parts = ["This file has %d lines." % len(lines)]
    if result["functions"]:
        parts.append("It defines %d function(s): %s." % (
            len(result["functions"]), ", ".join(f["name"] for f in result["functions"])))
    if result["classes"]:
        parts.append("It defines %d class(es): %s." % (
            len(result["classes"]), ", ".join(c["name"] for c in result["classes"])))
    if result["imports"]:
        parts.append("It imports: %s." % ", ".join(sorted(set(result["imports"])) or "nothing"))
    parts.append("Data flows from the inputs of each function through its body to its return value.")
    result["explanation"] = " ".join(parts)
    return result


def handle(method, path, body):
    if path == "/api/status":
        return {"program": SLUG, "status": "ok"}
    if path == "/api/read" and method == "POST":
        return read_code(body.get("code", ""))
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
