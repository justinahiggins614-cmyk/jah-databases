#!/usr/bin/env python3
"""Test suite for the JAH MCP pilot server (mcp_server.py).

Spawns the server over stdio, runs initialize + tools/list + one
tools/call per tool against REAL pilot data, and asserts on real values
(record IDs/titles/counts read from the live data-2 indexes).
Prints PASS/FAIL per tool and exits non-zero if any test fails.

Usage: python3 test_mcp.py [--server PATH]
"""
import argparse
import json
import subprocess
import sys

sys.path.insert(0, ".")
import os
HERE = os.path.dirname(os.path.abspath(__file__))

RESULTS = []

def check(name, ok, detail=""):
    RESULTS.append((name, bool(ok), detail))
    print("%s %s%s" % ("PASS" if ok else "FAIL", name,
                       (" — " + detail) if detail else ""))

class Client:
    def __init__(self, server_path):
        self.proc = subprocess.Popen(
            [sys.executable, server_path],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE,
            stderr=subprocess.PIPE, text=True, bufsize=1)
        self.n = 0

    def call(self, method, params=None):
        self.n += 1
        req = {"jsonrpc": "2.0", "id": self.n, "method": method}
        if params is not None:
            req["params"] = params
        self.proc.stdin.write(json.dumps(req) + "\n")
        self.proc.stdin.flush()
        line = self.proc.stdout.readline()
        if not line:
            raise RuntimeError("server closed stdout (stderr: %s)"
                               % self.proc.stderr.read()[:500])
        return json.loads(line)

    def tool(self, name, arguments):
        resp = self.call("tools/call",
                         {"name": name, "arguments": arguments})
        if "error" in resp:
            return None, resp["error"]
        return resp["result"], None

    def close(self):
        self.proc.stdin.close()
        self.proc.wait(timeout=10)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--server", default=os.path.join(HERE, "mcp_server.py"))
    args = ap.parse_args()
    c = Client(args.server)
    try:
        # initialize + tools/list
        r = c.call("initialize", {"protocolVersion": "2025-06-18",
                                  "capabilities": {},
                                  "clientInfo": {"name": "test", "version": "0"}})
        check("initialize", r.get("result", {}).get("serverInfo", {}).get("name") == "jah-mcp-pilot",
              str(r.get("result", {}).get("serverInfo")))
        r = c.call("tools/list")
        tools = r.get("result", {}).get("tools", [])
        names = [t["name"] for t in tools]
        check("tools/list (16 tools)", len(tools) == 16, "%d tools" % len(tools))
        check("tools/list has inputSchema", all("inputSchema" in t for t in tools))

        # 1. list databases
        res, err = c.tool("jah_list_databases", {"limit": 5})
        sc = res["structuredContent"] if res else {}
        check("jah_list_databases", not err and sc.get("total") == 10
              and len(sc.get("databases", [])) == 5
              and sc["databases"][0]["slug"] == "biofonics",
              "total=%s first=%s" % (sc.get("total"),
                                     (sc.get("databases") or [{}])[0].get("slug")))
        res, err = c.tool("jah_list_databases", {"query": "soundscape"})
        sc = res["structuredContent"] if res else {}
        check("jah_list_databases query", not err and sc.get("total") == 4,
              "total=%s" % sc.get("total"))

        # 2. search one database — 'echolocation' must hit JAH-BIOF-000007
        res, err = c.tool("jah_search_database",
                          {"slug": "biofonics", "query": "echolocation"})
        sc = res["structuredContent"] if res else {}
        ids = [x["id"] for x in sc.get("results", [])]
        check("jah_search_database", not err and "JAH-BIOF-000007" in ids,
              "hits=%s ids=%s" % (sc.get("total_hits"), ids))

        # 3. get file
        res, err = c.tool("jah_get_file",
                          {"location": "data-2/data/biofonics/index.jsonl.gz",
                           "limit": 3})
        sc = res["structuredContent"] if res else {}
        check("jah_get_file", not err and sc.get("total_records") == 16
              and sc.get("next_cursor") == "3",
              "total=%s cursor=%s" % (sc.get("total_records"),
                                      sc.get("next_cursor")))

        # 4. get record
        res, err = c.tool("jah_get_record", {"id": "JAH-BIOF-000001"})
        sc = res["structuredContent"] if res else {}
        rec = sc.get("record", {})
        check("jah_get_record", not err and rec.get("title") == "What Is Biofonics"
              and rec.get("record_kind") == "biofonics record"
              and len(rec.get("body", "")) == 2102,
              "title=%s body_len=%s" % (rec.get("title"),
                                        len(rec.get("body", ""))))

        # 5. cross-database search
        res, err = c.tool("jah_search_all", {"query": "echolocation"})
        sc = res["structuredContent"] if res else {}
        per = {d["slug"]: d["hits"] for d in sc.get("per_database", [])}
        check("jah_search_all", not err and sc.get("total_hits", 0) >= 2
              and per.get("biofonics", 0) >= 1
              and per.get("animal-vocal-communication", 0) >= 1,
              "total=%s per=%s" % (sc.get("total_hits"), per))

        # 6. read document (record full text)
        res, err = c.tool("jah_read_document",
                          {"doc": "record", "id": "JAH-BIOF-000001"})
        sc = res["structuredContent"] if res else {}
        check("jah_read_document record", not err
              and "Biofonics is the study of the sounds of living things"
              in sc.get("text", ""),
              "chars=%s" % len(sc.get("text", "")))
        res, err = c.tool("jah_read_document",
                          {"doc": "database-spec", "slug": "biofonics"})
        sc = res["structuredContent"] if res else {}
        check("jah_read_document database-spec", not err
              and "biofonics" in sc.get("text", ""))

        # 7. citation — JCC v1 code
        res, err = c.tool("jah_cite", {"id": "JAH-BIOF-000001"})
        sc = res["structuredContent"] if res else {}
        cit = sc.get("citation", {})
        check("jah_cite", not err
              and cit.get("code") == "JAHDB/biofonics#JAH-BIOF-000001+k=32d2ef75",
              "code=%s" % cit.get("code"))

        # 8. compare databases
        res, err = c.tool("jah_compare_databases",
                          {"slugs": ["biofonics", "biophony-soundscapes"]})
        sc = res["structuredContent"] if res else {}
        profs = {p["slug"]: p for p in sc.get("profiles", [])}
        check("jah_compare_databases", not err
              and profs.get("biofonics", {}).get("record_count") == 16
              and profs.get("biofonics", {}).get("field_fractions", {}).get("image") == 0.0
              and sc.get("same_record_kind") is False,
              "profiles=%s" % sorted(profs))

        # 9. knowledge graph
        res, err = c.tool("jah_knowledge_graph", {"id": "JAH-BIOF-000001"})
        sc = res["structuredContent"] if res else {}
        check("jah_knowledge_graph", not err
              and sc.get("node", {}).get("id") == "JAH-BIOF-000001"
              and len(sc.get("edges", [])) == 3
              and sc.get("neighbour_count", 0) > 0,
              "edges=%d neighbours=%d" % (len(sc.get("edges", [])),
                                          sc.get("neighbour_count", 0)))

        # 10. encyclopedia lookup
        res, err = c.tool("jah_lookup_encyclopedia", {"term": "echolocation"})
        sc = res["structuredContent"] if res else {}
        check("jah_lookup_encyclopedia", not err and sc.get("found") is True
              and sc.get("source_record", {}).get("id") == "JAH-BIOF-000007",
              "source=%s" % sc.get("source_record"))
        res, err = c.tool("jah_lookup_encyclopedia", {"term": "zzzqqq"})
        sc = res["structuredContent"] if res else {}
        check("jah_lookup_encyclopedia miss", not err
              and sc.get("found") is False)

        # 11. calculator — 343/440 must be the biofonics demo value 0.78
        res, err = c.tool("jah_calculate", {"expression": "343/440"})
        sc = res["structuredContent"] if res else {}
        check("jah_calculate", not err
              and abs(sc.get("result", 0) - 0.7795454545454545) < 1e-9,
              "result=%s" % sc.get("result"))
        res, err = c.tool("jah_calculate", {"expression": "__import__('os')"})
        check("jah_calculate rejects code", err is None
              and res.get("isError") is True,
              "isError=%s" % (res or {}).get("isError"))

        # 12. research assistant
        res, err = c.tool("jah_research",
                          {"question": "How do bats use echolocation?"})
        sc = res["structuredContent"] if res else {}
        check("jah_research", not err
              and sc.get("source_record", {}).get("id") == "JAH-BIOF-000007",
              "source=%s" % sc.get("source_record"))
        res, err = c.tool("jah_research", {"question": "zzzqqq www"})
        sc = res["structuredContent"] if res else {}
        check("jah_research no-answer", not err
              and sc.get("answer") is None)

        # 13. generator connection — deterministic per seed
        res, err = c.tool("jah_generate", {"slug": "biofonics", "seed": 7})
        sc = res["structuredContent"] if res else {}
        gen = sc.get("generated", {})
        res2, _ = c.tool("jah_generate", {"slug": "biofonics", "seed": 7})
        same = res2["structuredContent"].get("generated", {}).get("id") == gen.get("id")
        check("jah_generate deterministic", not err
              and gen.get("simulated") is True
              and gen.get("id", "").startswith("JAH-BIOF-GEN-")
              and same,
              "id=%s same=%s" % (gen.get("id"), same))

        # 14. browse archive with resume cursor
        res, err = c.tool("jah_browse_archive",
                          {"slug": "biofonics", "limit": 10})
        sc = res["structuredContent"] if res else {}
        cur = sc.get("next_cursor")
        res2, _ = c.tool("jah_browse_archive",
                         {"slug": "biofonics", "limit": 10, "cursor": cur})
        sc2 = res2["structuredContent"]
        ids1 = [e["id"] for e in sc.get("entries", [])]
        ids2 = [e["id"] for e in sc2.get("entries", [])]
        check("jah_browse_archive resume", not err
              and len(ids1) == 10 and len(ids2) == 6
              and not set(ids1) & set(ids2)
              and sc2.get("next_cursor") is None,
              "page1=%d page2=%d" % (len(ids1), len(ids2)))

        # 15. media / metadata
        res, err = c.tool("jah_get_media", {"id": "JAH-BIOF-000001"})
        sc = res["structuredContent"] if res else {}
        check("jah_get_media", not err and sc.get("media_count") == 0
              and sc.get("metadata", {}).get("record_kind") == "biofonics record",
              "media=%s kind=%s" % (sc.get("media_count"),
                                    sc.get("metadata", {}).get("record_kind")))

        # 16. health
        res, err = c.tool("jah_health", {})
        sc = res["structuredContent"] if res else {}
        check("jah_health", not err and sc.get("status") == "ok"
              and sc.get("pilot_records") == 160
              and sc.get("records_match") is True
              and sc.get("manifest_database_count") == 63047,
              "records=%s manifest=%s" % (sc.get("pilot_records"),
                                          sc.get("manifest_database_count")))

        # Error paths
        res, err = c.tool("jah_get_record", {"id": "JAH-NOPE-000001"})
        check("error: unknown record", res.get("isError") is True
              and res["structuredContent"]["error"]["code"] == "record_not_found")
        res, err = c.tool("jah_search_database", {"slug": "nope", "query": "x"})
        check("error: unknown database", res.get("isError") is True
              and res["structuredContent"]["error"]["code"] == "unknown_database")
        res, err = c.tool("jah_search_database", {"slug": "biofonics"})
        check("error: missing argument", res.get("isError") is True
              and res["structuredContent"]["error"]["code"] == "missing_argument")
        r = c.call("tools/call", {"name": "jah_nope", "arguments": {}})
        check("error: unknown tool",
              r["result"].get("isError") is True
              and r["result"]["structuredContent"]["error"]["code"] == "unknown_tool")
        r = c.call("bogus/method")
        check("error: unknown method", "error" in r
              and r["error"]["code"] == -32601)
    finally:
        c.close()

    failed = [n for n, ok, _ in RESULTS if not ok]
    print("\n%d checks, %d passed, %d failed"
          % (len(RESULTS), len(RESULTS) - len(failed), len(failed)))
    if failed:
        print("FAILED: " + ", ".join(failed))
        return 1
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
