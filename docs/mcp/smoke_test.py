#!/usr/bin/env python3
"""Package-alone smoke test for the JAH MCP pilot server.

Spawns the bundled mcp_server.py against the bundled data/ + manifest.json
(no live repo clones needed) and checks real data comes back through the
server, not just a unit test: initialize, tools/list (16), one search,
one get-record, one citation, one health check.

Usage: python3 smoke_test.py
Exit 0 + "SMOKE OK" means the package works from this folder alone.
"""
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("%s %s%s" % ("PASS" if ok else "FAIL", name,
                       (" — " + detail) if detail else ""))


def main():
    proc = subprocess.Popen(
        [sys.executable, os.path.join(HERE, "mcp_server.py"),
         "--data2", os.path.join(HERE, "data"),
         "--manifest", os.path.join(HERE, "manifest.json")],
        stdin=subprocess.PIPE, stdout=subprocess.PIPE,
        stderr=subprocess.PIPE, text=True, bufsize=1)
    n = 0

    def call(method, params=None):
        nonlocal n
        n += 1
        req = {"jsonrpc": "2.0", "id": n, "method": method}
        if params is not None:
            req["params"] = params
        proc.stdin.write(json.dumps(req) + "\n")
        proc.stdin.flush()
        line = proc.stdout.readline()
        if not line:
            raise RuntimeError("server closed stdout (stderr: %s)"
                               % proc.stderr.read()[:500])
        return json.loads(line)

    def tool(name, arguments):
        resp = call("tools/call", {"name": name, "arguments": arguments})
        return resp.get("result", {}), resp.get("error")

    try:
        r = call("initialize", {"protocolVersion": "2025-06-18",
                                 "capabilities": {},
                                 "clientInfo": {"name": "smoke", "version": "0"}})
        check("initialize",
              r.get("result", {}).get("serverInfo", {}).get("name") == "jah-mcp-pilot",
              str(r.get("result", {}).get("serverInfo")))

        r = call("tools/list")
        tools = r.get("result", {}).get("tools", [])
        check("tools/list (16 tools)", len(tools) == 16, "%d tools" % len(tools))

        res, err = tool("jah_search_database",
                        {"slug": "biofonics", "query": "echolocation"})
        sc = res.get("structuredContent", {})
        ids = [x["id"] for x in sc.get("results", [])]
        check("jah_search_database (real data)",
              not err and "JAH-BIOF-000007" in ids,
              "hits=%s ids=%s" % (sc.get("total_hits"), ids))

        res, err = tool("jah_get_record", {"id": "JAH-BIOF-000001"})
        sc = res.get("structuredContent", {})
        rec = sc.get("record", {})
        check("jah_get_record (real data)",
              not err and rec.get("title") == "What Is Biofonics"
              and len(rec.get("body", "")) == 2102,
              "title=%s body_len=%s" % (rec.get("title"),
                                        len(rec.get("body", ""))))

        res, err = tool("jah_cite", {"id": "JAH-BIOF-000001"})
        sc = res.get("structuredContent", {})
        code = sc.get("citation", {}).get("code")
        check("jah_cite (JCC v1)",
              not err and code == "JAHDB/biofonics#JAH-BIOF-000001+k=32d2ef75",
              "code=%s" % code)

        res, err = tool("jah_health", {})
        sc = res.get("structuredContent", {})
        check("jah_health",
              not err and sc.get("status") == "ok"
              and sc.get("pilot_records") == 160
              and sc.get("records_match") is True,
              "records=%s manifest=%s"
              % (sc.get("pilot_records"), sc.get("manifest_database_count")))
    finally:
        proc.stdin.close()
        proc.wait(timeout=10)

    failed = [n for n, ok in CHECKS if not ok]
    print("\n%d checks, %d passed, %d failed"
          % (len(CHECKS), len(CHECKS) - len(failed), len(failed)))
    if failed:
        print("FAILED: " + ", ".join(failed))
        return 1
    print("SMOKE OK: %d checks passed" % len(CHECKS))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
