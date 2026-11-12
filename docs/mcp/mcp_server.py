#!/usr/bin/env python3
"""JAH MCP pilot server — stdio transport, stdlib only, read-only.

Serves the 10 FULL-CANON biofonics databases (160 records, live data-2
indexes) as 16 MCP-style tools over JSON-RPC 2.0 on stdin/stdout
(one JSON object per line). Package-only pilot: no network, no writes,
no deploy. Data is loaded once at startup from the local data-2 clone.

Usage:
    python3 mcp_server.py [--data2 DIR] [--manifest PATH]

Protocol (per line on stdin):
    {"jsonrpc":"2.0","id":1,"method":"initialize","params":{...}}
    {"jsonrpc":"2.0","id":2,"method":"tools/list"}
    {"jsonrpc":"2.0","id":3,"method":"tools/call",
     "params":{"name":"jah_search_database",
               "arguments":{"slug":"biofonics","query":"echolocation"}}}
    {"jsonrpc":"2.0","method":"notifications/initialized"}   (ignored)

Tool results follow the MCP shape:
    {"content":[{"type":"text","text":"<JSON string>"}],
     "structuredContent":{...}, "isError":false}
"""
import argparse
import gzip
import json
import math
import os
import re
import sys

PILOT_SLUGS = [
    "biofonics", "biofonics-signature",
    "biophony-soundscapes", "biophony-soundscapes-signature",
    "soundscape-ecology", "soundscape-ecology-signature",
    "animal-vocal-communication", "animal-vocal-communication-signature",
    "bioacoustic-recording-analysis", "bioacoustic-recording-analysis-signature",
]

HOME = os.path.expanduser("~")
DEFAULT_DATA2 = os.path.join(HOME, "workspace", "jah-databases-data-2", "data")
DEFAULT_MANIFEST = os.path.join(HOME, "workspace", "jah-databases",
                                 "data", "manifest.json")

# ---------------------------------------------------------------- data load
class PilotData:
    def __init__(self, data2_dir, manifest_path):
        self.data2_dir = data2_dir
        self.databases = {}   # slug -> {"meta": {...}, "records": [...]}
        self.by_id = {}       # record id -> (slug, record)
        self.manifest_count = None
        self.manifest_loaded = False
        try:
            with open(manifest_path, "r", encoding="utf-8") as fh:
                manifest = json.load(fh)
            entries = {e["slug"]: e for e in manifest.get("databases", [])}
            self.manifest_count = manifest.get("database_count")
            self.manifest_loaded = True
        except Exception as exc:  # manifest unreadable: pilot still serves
            entries = {}
            self.manifest_error = str(exc)
        for slug in PILOT_SLUGS:
            path = os.path.join(data2_dir, slug, "index.jsonl.gz")
            records = []
            with gzip.open(path, "rt", encoding="utf-8") as fh:
                for line in fh:
                    line = line.strip()
                    if line:
                        records.append(json.loads(line))
            meta = dict(entries.get(slug, {}))
            meta.setdefault("slug", slug)
            meta.setdefault("record_count", len(records))
            self.databases[slug] = {"meta": meta, "records": records}
            for rec in records:
                self.by_id[rec["id"]] = (slug, rec)

    @property
    def total_records(self):
        return sum(len(d["records"]) for d in self.databases.values())

    def search(self, records, query):
        """Case-insensitive substring search over title+description+body."""
        q = query.lower()
        hits = []
        for rec in records:
            hay = " ".join(str(rec.get(k, "")) for k in
                           ("title", "description", "body")).lower()
            if q in hay:
                hits.append(rec)
        return hits

    def snippet(self, rec, query, width=240):
        text = (rec.get("description") or "") + " " + (rec.get("body") or "")
        text = re.sub(r"<[^>]+>", "", text)
        text = re.sub(r"\s+", " ", text).strip()
        idx = text.lower().find(query.lower())
        if idx < 0:
            return text[:width]
        start = max(0, idx - 60)
        return ("..." if start else "") + text[start:start + width] + "..."

# ---------------------------------------------------------------- errors
class ToolError(Exception):
    def __init__(self, code, message):
        super().__init__(message)
        self.code = code
        self.message = message

def err_result(code, message):
    return {"content": [{"type": "text",
                         "text": json.dumps({"error": {"code": code,
                                                       "message": message}})}],
            "structuredContent": {"error": {"code": code, "message": message}},
            "isError": True}

def ok_result(payload):
    return {"content": [{"type": "text", "text": json.dumps(payload)}],
            "structuredContent": payload,
            "isError": False}

def require(args, *names):
    for name in names:
        if name not in args or args[name] in (None, ""):
            raise ToolError("missing_argument",
                            "required argument %r is missing" % name)

def check_slug(data, slug):
    if slug not in data.databases:
        raise ToolError(
            "unknown_database",
            "slug %r is not in this pilot server (10 biofonics databases "
            "only)" % slug)

def paginate(items, limit, cursor):
    """Cursor = integer offset encoded as a string; returns page + next."""
    limit = max(1, min(int(limit), 100))
    offset = int(cursor) if cursor not in (None, "") else 0
    page = items[offset:offset + limit]
    nxt = str(offset + limit) if offset + limit < len(items) else None
    return page, nxt, len(items)

# ---------------------------------------------------------------- tool impls
def t_list_databases(data, a):
    limit = a.get("limit", 25)
    cursor = a.get("cursor")
    query = (a.get("query") or "").lower()
    dbs = []
    for slug in PILOT_SLUGS:
        meta = data.databases[slug]["meta"]
        entry = {"slug": slug,
                 "name": meta.get("name", slug),
                 "record_kind": meta.get("record_kind"),
                 "record_count": len(data.databases[slug]["records"]),
                 "manifest_record_count": meta.get("record_count"),
                 "ai_name": meta.get("ai_name"),
                 "source": meta.get("source")}
        if query and query not in (entry["name"] + " " + slug +
                                   " " + (entry["record_kind"] or "")).lower():
            continue
        dbs.append(entry)
    page, nxt, total = paginate(dbs, limit, cursor)
    return {"databases": page, "total": total, "next_cursor": nxt,
            "pilot_scope": "10 biofonics databases (FULL-CANON pilot)"}

def t_search_database(data, a):
    require(a, "slug", "query")
    check_slug(data, a["slug"])
    limit = a.get("limit", 25)
    cursor = a.get("cursor")
    hits = data.search(data.databases[a["slug"]]["records"], a["query"])
    page, nxt, total = paginate(hits, limit, cursor)
    return {"slug": a["slug"], "query": a["query"], "total_hits": total,
            "next_cursor": nxt,
            "results": [{"id": r["id"], "title": r["title"],
                         "snippet": data.snippet(r, a["query"])}
                        for r in page]}

def t_get_file(data, a):
    require(a, "location")
    loc = a["location"]
    m = re.match(r"^data-2/data/([^/]+)/index\.jsonl\.gz$", loc)
    if not m or m.group(1) not in data.databases:
        raise ToolError("unknown_file",
                        "pilot serves only data-2/data/<pilot-slug>/"
                        "index.jsonl.gz; got %r" % loc)
    slug = m.group(1)
    limit = a.get("limit", 25)
    cursor = a.get("cursor")
    recs = data.databases[slug]["records"]
    page, nxt, total = paginate(recs, limit, cursor)
    return {"location": loc, "slug": slug, "total_records": total,
            "next_cursor": nxt,
            "records": [{"id": r["id"], "title": r["title"],
                         "record_kind": r.get("record_kind"),
                         "description": (r.get("description") or "")[:400]}
                        for r in page]}

def t_get_record(data, a):
    require(a, "id")
    hit = data.by_id.get(a["id"])
    if not hit:
        raise ToolError("record_not_found",
                        "record %r is not in the pilot data" % a["id"])
    slug, rec = hit
    return {"slug": slug, "record": rec}

def t_search_all(data, a):
    require(a, "query")
    limit = a.get("limit", 25)
    cursor = a.get("cursor")
    per_db = []
    all_hits = []
    for slug in PILOT_SLUGS:
        hits = data.search(data.databases[slug]["records"], a["query"])
        per_db.append({"slug": slug, "hits": len(hits)})
        for r in hits:
            all_hits.append((slug, r))
    page, nxt, total = paginate(all_hits, limit, cursor)
    return {"query": a["query"], "total_hits": total, "next_cursor": nxt,
            "per_database": per_db,
            "results": [{"slug": s, "id": r["id"], "title": r["title"],
                         "snippet": data.snippet(r, a["query"])}
                        for s, r in page]}

def t_read_document(data, a):
    require(a, "doc")
    doc = a["doc"]
    if doc == "record":
        require(a, "id")
        hit = data.by_id.get(a["id"])
        if not hit:
            raise ToolError("record_not_found",
                            "record %r is not in the pilot data" % a["id"])
        slug, rec = hit
        body = re.sub(r"<[^>]+>", "", rec.get("body") or "")
        return {"doc": "record", "id": rec["id"], "slug": slug,
                "title": rec["title"],
                "text": (rec.get("description") or "") + "\n\n" + body}
    if doc == "database-spec":
        require(a, "slug")
        check_slug(data, a["slug"])
        meta = data.databases[a["slug"]]["meta"]
        return {"doc": "database-spec", "slug": a["slug"],
                "text": json.dumps(meta, indent=2, ensure_ascii=False)}
    if doc == "manifest":
        return {"doc": "manifest",
                "text": "Live manifest database_count: %s. Pilot scope: "
                        "10 biofonics databases, %d records. Full manifest "
                        "is 50.8 MB and is served paginated, never whole."
                        % (data.manifest_count, data.total_records)}
    raise ToolError("unknown_document",
                    "doc must be record | database-spec | manifest")

def t_cite(data, a):
    require(a, "id")
    hit = data.by_id.get(a["id"])
    if not hit:
        raise ToolError("record_not_found",
                        "record %r is not in the pilot data" % a["id"])
    slug, rec = hit
    # JCC v1 condensed code (condensed-by-code standard, verified against
    # pilot/biofonics/codes.md): JAHDB/<slug>#<record-id> + k= + first 8
    # hex of SHA-256 over the canonical record JSON (keys sorted, compact
    # separators, UTF-8). The key is a 32-bit typo-check; the record ID is
    # the primary key. Verified: JAH-BIOF-000001 -> k=32d2ef75,
    # JAH-BIOF-000007 -> k=0e71b537 (pilot codes.md + decode.py demo
    # 10,693/10,693 PASS).
    import hashlib
    canon = json.dumps(rec, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=False).encode("utf-8")
    key = hashlib.sha256(canon).hexdigest()[:8]
    code = "JAHDB/%s#%s+k=%s" % (slug, rec["id"], key)
    citation = {
        "code": code,
        "record_id": rec["id"],
        "title": rec["title"],
        "database": data.databases[slug]["meta"].get("name", slug),
        "slug": slug,
        "record_kind": rec.get("record_kind"),
        "source": rec.get("source"),
        "src": rec.get("src"),
        "source_quality": rec.get("source_quality"),
        "live_url": ("https://justinahiggins614-cmyk.github.io/"
                     "jah-databases-data-2/data/%s/index.jsonl.gz" % slug),
        "text": "%s. %s (%s). %s, record %s. Condensed code %s."
                % (rec["title"],
                   data.databases[slug]["meta"].get("name", slug),
                   rec.get("record_kind"), rec.get("source") or "JAH Databases",
                   rec["id"], code),
    }
    return {"citation": citation}

def _profile(data, slug):
    recs = data.databases[slug]["records"]
    keys = ("body", "demo", "program", "image", "science_proof",
            "math_proof", "generator")
    frac = {}
    bodies = []
    for k in keys:
        present = sum(1 for r in recs if r.get(k))
        frac[k] = round(present / len(recs), 3) if recs else 0.0
    for r in recs:
        b = re.sub(r"<[^>]+>", "", r.get("body") or "")
        bodies.append(len(b))
    bodies.sort()
    median = bodies[len(bodies) // 2] if bodies else 0
    return {"slug": slug,
            "record_count": len(recs),
            "median_body_chars": median,
            "field_fractions": frac,
            "record_kind": data.databases[slug]["meta"].get("record_kind")}

def t_compare_databases(data, a):
    require(a, "slugs")
    slugs = a["slugs"]
    if not isinstance(slugs, list) or len(slugs) < 2:
        raise ToolError("invalid_argument",
                        "slugs must be a list of at least 2 pilot slugs")
    for s in slugs:
        check_slug(data, s)
    profiles = [_profile(data, s) for s in slugs]
    kinds = {p["record_kind"] for p in profiles}
    return {"compared": slugs, "profiles": profiles,
            "same_record_kind": len(kinds) == 1,
            "record_kinds": sorted(k for k in kinds if k),
            "notes": "Field fractions are measured over stored records; "
                     "image is 0.0 across the biofonics pilot (the one "
                     "missing FULL-CANON step)."}

def t_knowledge_graph(data, a):
    require(a, "id")
    hit = data.by_id.get(a["id"])
    if not hit:
        raise ToolError("record_not_found",
                        "record %r is not in the pilot data" % a["id"])
    slug, rec = hit
    edges = []
    for link in rec.get("cross_links") or []:
        edges.append({"to": link, "relation": "cross_link",
                      "note": "record-level cross-link as stored"})
    # Term neighbours: other pilot records sharing a title word (>=4 chars).
    words = {w.lower() for w in re.findall(r"[A-Za-z]{4,}", rec["title"])}
    neighbours = []
    for other_slug, other in data.by_id.values():
        if other["id"] == rec["id"]:
            continue
        ow = {w.lower() for w in re.findall(r"[A-Za-z]{4,}", other["title"])}
        shared = sorted(words & ow)
        if shared:
            neighbours.append({"id": other["id"], "slug": other_slug,
                               "title": other["title"],
                               "shared_title_words": shared})
    return {"node": {"id": rec["id"], "slug": slug, "title": rec["title"]},
            "edges": edges,
            "term_neighbours": neighbours[:10],
            "neighbour_count": len(neighbours)}

def t_lookup_encyclopedia(data, a):
    require(a, "term")
    term = a["term"]
    hits = []
    for slug in PILOT_SLUGS:
        for r in data.search(data.databases[slug]["records"], term):
            hits.append((slug, r))
    if not hits:
        return {"term": term, "found": False,
                "definition": None,
                "note": "No pilot record defines %r. Live lookup routes to "
                        "the JAH Wiki and Dictionary indexes; those indexes "
                        "are outside this 10-database pilot." % term}
    slug, best = hits[0]
    return {"term": term, "found": True,
            "definition": re.sub(r"<[^>]+>", "",
                                  best.get("description") or "")[:800],
            "source_record": {"id": best["id"], "slug": slug,
                              "title": best["title"]},
            "other_matches": [{"id": r["id"], "slug": s, "title": r["title"]}
                              for s, r in hits[1:6]],
            "total_matches": len(hits),
            "note": "Pilot definition drawn from biofonics records only; "
                    "live lookup also consults JAH Wiki / Dictionary."}

def t_calculate(data, a):
    require(a, "expression")
    expr = a["expression"]
    # Safe arithmetic only: numbers, + - * / % ** ( ) and math functions.
    allowed_names = {k: getattr(math, k) for k in
                     ("sqrt", "sin", "cos", "tan", "log", "log10", "exp",
                      "pi", "e", "floor", "ceil")}
    allowed_names["abs"] = abs
    import ast
    try:
        tree = ast.parse(expr, mode="eval")
    except SyntaxError as exc:
        raise ToolError("invalid_expression", "cannot parse %r: %s"
                        % (expr, exc))
    for node in ast.walk(tree):
        if isinstance(node, ast.Name) and node.id not in allowed_names:
            raise ToolError("invalid_expression",
                            "name %r is not allowed" % node.id)
        if isinstance(node, (ast.Call, ast.BinOp, ast.UnaryOp, ast.Constant,
                             ast.Expression, ast.Load, ast.Add, ast.Sub,
                             ast.Mult, ast.Div, ast.Mod, ast.Pow, ast.USub,
                             ast.UAdd, ast.FloorDiv)):
            continue
        raise ToolError("invalid_expression",
                        "operator/node %s is not allowed"
                        % type(node).__name__)
    try:
        value = eval(compile(tree, "<calc>", "eval"), {"__builtins__": {}},
                     allowed_names)  # noqa: S307 - AST-whitelisted above
    except Exception as exc:
        raise ToolError("calculation_error", str(exc))
    return {"expression": expr, "result": value,
            "note": "Pilot calculator: local safe arithmetic. Live routing "
                    "delegates to the Signature Calculator database/site; "
                    "this pilot proves the interface, not the live route."}

def t_research(data, a):
    require(a, "question")
    q = a["question"]
    words = [w for w in re.findall(r"[A-Za-z]{3,}", q.lower())]
    best = None
    best_score = 0
    for slug in PILOT_SLUGS:
        for r in data.databases[slug]["records"]:
            hay = (r["title"] + " " + (r.get("description") or "")).lower()
            score = sum(1 for w in words if w in hay)
            if score > best_score:
                best_score, best = score, (slug, r)
    if not best or best_score == 0:
        return {"question": q, "answer": None,
                "note": "No pilot record answers this question. A live "
                        "research call would escalate to the database AI / "
                        "off-site Signature Web AI; the pilot does not "
                        "invent an answer."}
    slug, rec = best
    return {"question": q,
            "answer": re.sub(r"<[^>]+>", "",
                             rec.get("description") or "")[:1200],
            "source_record": {"id": rec["id"], "slug": slug,
                              "title": rec["title"]},
            "match_score": best_score,
            "note": "Answer is the source record's own description, "
                    "verbatim; no synthesis added in the pilot."}

def t_generate(data, a):
    require(a, "slug")
    check_slug(data, a["slug"])
    seed = a.get("seed", 1)
    try:
        seed = int(seed)
    except (TypeError, ValueError):
        raise ToolError("invalid_argument", "seed must be an integer")
    recs = data.databases[a["slug"]]["records"]
    gen = recs[0].get("generator") or {}
    base = recs[seed % len(recs)]
    new_id = "%s%06d" % (gen.get("gen_id_prefix", "JAH-GEN-"),
                         100000 + (seed % 900000))
    return {"generated": {
                "id": new_id,
                "title": "Generated variation on: %s" % base["title"],
                "slug": a["slug"],
                "record_kind": base.get("record_kind"),
                "seed": seed,
                "simulated": True,
                "text": "Simulated generated record seeded from %s "
                        "(seed %d). Content is generated, not stored; "
                        "verify before use." % (base["id"], seed)},
            "generator": {"type": gen.get("type"),
                          "hard_stop": gen.get("hard_stop"),
                          "throttle_per_call": gen.get("throttle_per_call"),
                          "gen_id_prefix": gen.get("gen_id_prefix")},
            "note": "Generator connection proof only: the pilot derives a "
                    "deterministic simulated record from the seed. Live "
                    "generation runs the database's own boundless generator."}

def t_browse_archive(data, a):
    require(a, "slug")
    check_slug(data, a["slug"])
    limit = a.get("limit", 25)
    cursor = a.get("cursor")
    recs = data.databases[a["slug"]]["records"]
    page, nxt, total = paginate(recs, limit, cursor)
    return {"slug": a["slug"], "total_records": total, "next_cursor": nxt,
            "entries": [{"id": r["id"], "title": r["title"],
                         "ladder_rank": r.get("ladder_rank"),
                         "description": (r.get("description") or "")[:200]}
                        for r in page]}

def t_get_media(data, a):
    require(a, "id")
    hit = data.by_id.get(a["id"])
    if not hit:
        raise ToolError("record_not_found",
                        "record %r is not in the pilot data" % a["id"])
    slug, rec = hit
    media = []
    for key in ("image", "image_url", "video", "video_url", "audio"):
        if rec.get(key):
            media.append({"kind": key, "url": rec[key]})
    metadata = {k: rec.get(k) for k in
                ("id", "title", "slug", "record_kind", "src", "source",
                 "source_quality", "edition", "status", "ladder_rank")}
    return {"id": rec["id"], "slug": slug, "media": media,
            "media_count": len(media), "metadata": metadata,
            "note": "Biofonics pilot records carry no image/video fields "
                    "(the one missing FULL-CANON step); metadata retrieval "
                    "is the live part of this tool in the pilot."}

def t_health(data, a):
    return {"status": "ok",
            "server": "jah-mcp-pilot/1.0 (stdio, package-only)",
            "manifest_database_count": data.manifest_count,
            "manifest_loaded": data.manifest_loaded,
            "pilot_databases": len(data.databases),
            "pilot_records": data.total_records,
            "expected_records": 160,
            "records_match": data.total_records == 160,
            "read_only": True,
            "note": "Health only. Live endpoint adds manifest-count "
                    "hard stop: regenerate if the count moves."}

TOOLS = [
    ("jah_list_databases", t_list_databases,
     "List databases in the network (paginated).",
     {"type": "object",
      "properties": {"query": {"type": "string"},
                     "limit": {"type": "integer", "default": 25,
                               "minimum": 1, "maximum": 100},
                     "cursor": {"type": "string"}},
      "additionalProperties": False}),
    ("jah_search_database", t_search_database,
     "Keyword search inside one database.",
     {"type": "object",
      "properties": {"slug": {"type": "string"},
                     "query": {"type": "string"},
                     "limit": {"type": "integer", "default": 25,
                               "minimum": 1, "maximum": 100},
                     "cursor": {"type": "string"}},
      "required": ["slug", "query"], "additionalProperties": False}),
    ("jah_get_file", t_get_file,
     "Fetch a data file by location (paginated records).",
     {"type": "object",
      "properties": {"location": {"type": "string"},
                     "limit": {"type": "integer", "default": 25,
                               "minimum": 1, "maximum": 100},
                     "cursor": {"type": "string"}},
      "required": ["location"], "additionalProperties": False}),
    ("jah_get_record", t_get_record,
     "Fetch one record by ID, in full.",
     {"type": "object",
      "properties": {"id": {"type": "string"}},
      "required": ["id"], "additionalProperties": False}),
    ("jah_search_all", t_search_all,
     "Keyword search across databases (pilot: 10).",
     {"type": "object",
      "properties": {"query": {"type": "string"},
                     "limit": {"type": "integer", "default": 25,
                               "minimum": 1, "maximum": 100},
                     "cursor": {"type": "string"}},
      "required": ["query"], "additionalProperties": False}),
    ("jah_read_document", t_read_document,
     "Read a document: a record's full text, a database spec, or the manifest summary.",
     {"type": "object",
      "properties": {"doc": {"type": "string",
                             "enum": ["record", "database-spec",
                                      "manifest"]},
                     "id": {"type": "string"},
                     "slug": {"type": "string"}},
      "required": ["doc"], "additionalProperties": False}),
    ("jah_cite", t_cite,
     "Generate a citation (with JCC v1 condensed code) for a record.",
     {"type": "object",
      "properties": {"id": {"type": "string"}},
      "required": ["id"], "additionalProperties": False}),
    ("jah_compare_databases", t_compare_databases,
     "Compare two or more databases: counts, field coverage, median body.",
     {"type": "object",
      "properties": {"slugs": {"type": "array", "minItems": 2,
                               "items": {"type": "string"}}},
      "required": ["slugs"], "additionalProperties": False}),
    ("jah_knowledge_graph", t_knowledge_graph,
     "Knowledge-graph lookup: a record's cross-links and term neighbours.",
     {"type": "object",
      "properties": {"id": {"type": "string"}},
      "required": ["id"], "additionalProperties": False}),
    ("jah_lookup_encyclopedia", t_lookup_encyclopedia,
     "Encyclopedia / dictionary lookup for a term.",
     {"type": "object",
      "properties": {"term": {"type": "string"}},
      "required": ["term"], "additionalProperties": False}),
    ("jah_calculate", t_calculate,
     "Calculator connection: safe arithmetic evaluation.",
     {"type": "object",
      "properties": {"expression": {"type": "string"}},
      "required": ["expression"], "additionalProperties": False}),
    ("jah_research", t_research,
     "Research assistant: best-matching record's own description as answer.",
     {"type": "object",
      "properties": {"question": {"type": "string"}},
      "required": ["question"], "additionalProperties": False}),
    ("jah_generate", t_generate,
     "Generator connection: deterministic simulated record from a seed.",
     {"type": "object",
      "properties": {"slug": {"type": "string"},
                     "seed": {"type": "integer", "default": 1}},
      "required": ["slug"], "additionalProperties": False}),
    ("jah_browse_archive", t_browse_archive,
     "Browse a database's archive, paginated with a resume cursor.",
     {"type": "object",
      "properties": {"slug": {"type": "string"},
                     "limit": {"type": "integer", "default": 25,
                               "minimum": 1, "maximum": 100},
                     "cursor": {"type": "string"}},
      "required": ["slug"], "additionalProperties": False}),
    ("jah_get_media", t_get_media,
     "Image / video / metadata retrieval for a record.",
     {"type": "object",
      "properties": {"id": {"type": "string"}},
      "required": ["id"], "additionalProperties": False}),
    ("jah_health", t_health,
     "Health-check: manifest count, pilot load, read-only status.",
     {"type": "object", "properties": {},
      "additionalProperties": False}),
]
TOOL_MAP = {name: (fn, desc, schema) for name, fn, desc, schema in TOOLS}

# ---------------------------------------------------------------- JSON-RPC loop
def handle(data, req):
    method = req.get("method")
    rid = req.get("id")
    if method == "initialize":
        return {"jsonrpc": "2.0", "id": rid,
                "result": {"protocolVersion": "2025-06-18",
                           "capabilities": {"tools": {}},
                           "serverInfo": {"name": "jah-mcp-pilot",
                                          "version": "1.0.0"}}}
    if method == "ping":
        return {"jsonrpc": "2.0", "id": rid, "result": {}}
    if method == "tools/list":
        return {"jsonrpc": "2.0", "id": rid,
                "result": {"tools": [
                    {"name": n, "description": d, "inputSchema": s}
                    for n, _, d, s in TOOLS]}}
    if method == "tools/call":
        params = req.get("params") or {}
        name = params.get("name")
        args = params.get("arguments") or {}
        if name not in TOOL_MAP:
            return {"jsonrpc": "2.0", "id": rid,
                    "result": err_result("unknown_tool",
                                         "no tool named %r" % name)}
        fn = TOOL_MAP[name][0]
        try:
            result = ok_result(fn(data, args))
        except ToolError as exc:
            result = err_result(exc.code, exc.message)
        except Exception as exc:  # never crash the loop on a bad call
            result = err_result("internal_error", str(exc))
        return {"jsonrpc": "2.0", "id": rid, "result": result}
    if method and method.startswith("notifications/"):
        return None
    return {"jsonrpc": "2.0", "id": rid,
            "error": {"code": -32601, "message": "method not found: %s"
                      % method}}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data2", default=DEFAULT_DATA2)
    ap.add_argument("--manifest", default=DEFAULT_MANIFEST)
    args = ap.parse_args()
    try:
        data = PilotData(args.data2, args.manifest)
    except Exception as exc:
        sys.stderr.write("pilot data load failed: %s\n" % exc)
        return 1
    sys.stderr.write("jah-mcp-pilot ready: %d databases, %d records, "
                     "manifest_count=%s\n"
                     % (len(data.databases), data.total_records,
                        data.manifest_count))
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
        except json.JSONDecodeError:
            sys.stdout.write(json.dumps(
                {"jsonrpc": "2.0", "id": None,
                 "error": {"code": -32700, "message": "parse error"}}) + "\n")
            sys.stdout.flush()
            continue
        resp = handle(data, req)
        if resp is not None:
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
