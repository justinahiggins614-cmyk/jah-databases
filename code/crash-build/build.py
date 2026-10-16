#!/usr/bin/env python3
"""PHASE M — crash/accident databases build.

Builds 4 new databases (public + signature pairs):
  crash-data-databases (+ -signature): plane/jet/car crash investigation records
  accidents-insurance-proven (+ -signature): accident records with verification tiers

Canon: template page, gzipped index chunks in jah-databases-data-1, unique ID
prefixes, manifest/api.json entries, dedupe/xdb script tags + generator handlers
from the template family, .kv grids minmax(120px,1fr). No website references,
no Facebook, no banned phrases. Dedupe-gated via code/dedupe_gate.py.
"""
import gzip
import importlib.util
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = "/home/hatch/workspace/jah-databases"
SHARD = "/home/hatch/workspace/jah-databases-data-1"
SHARD_BASE = "https://justinahiggins614-cmyk.github.io/jah-databases-data-1"
TEMPLATE = os.path.join(REPO, "db", "public-synthetic-intelligence", "index.html")

sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
GATE = DedupeGate(os.path.join(SHARD, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_crash_pub import ENTRIES as E_CRASH_PUB
from entries_crash_sig import ENTRIES as E_CRASH_SIG
from entries_acc_pub import ENTRIES as E_ACC_PUB
from entries_acc_sig import ENTRIES as E_ACC_SIG

# ============================================================ demo library
# Every demo is real, runnable, stdlib-only Python with an "OK:" marker.

def _hdr(name, rid, group):
    return ('#!/usr/bin/env python3\n"""%s — working demonstration.\n'
            'Record %s [%s]. Property of Justin Addam Higgins (JAH).\n"""\n'
            % (name, rid, group))

def demo_investigation(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
import json
SECTIONS = ["occurrence", "evidence", "analysis", "findings",
            "probable_cause", "recommendations"]
FINDINGS = ''' + json.dumps(points, ensure_ascii=False) + '''
def build_file():
    return {
        "occurrence": {"record_id": ''' + json.dumps(rid) + '''},
        "evidence": {"items": ["recorder_data", "wreckage", "witness_accounts"]},
        "analysis": {"factors": len(FINDINGS)},
        "findings": list(FINDINGS),
        "probable_cause": FINDINGS[0] if FINDINGS else "undetermined",
        "recommendations": ["rec_%d" % i for i in range(1, 4)],
    }
def main():
    rec = build_file()
    missing = [s for s in SECTIONS if s not in rec or not rec[s]]
    assert not missing, "missing sections: %s" % missing
    assert rec["findings"], "no findings recorded"
    assert rec["recommendations"], "no recommendations recorded"
    print("sections=%d findings=%d recommendations=%d"
          % (len(SECTIONS), len(rec["findings"]), len(rec["recommendations"])))
    print("probable cause:", rec["probable_cause"][:80])
    print("OK: %s investigation file validated end to end" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''

def demo_causetree(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
FACTORS = ''' + json.dumps(points, ensure_ascii=False) + '''
def build_tree():
    # root -> layer nodes -> factor leaves; every node traces to the root
    nodes = {"root": None}
    for i, f in enumerate(FACTORS):
        layer = "layer_%d" % (i % 3)
        nodes.setdefault(layer, "root")
        nodes["factor_%d" % i] = layer
    return nodes
def reaches_root(nodes, n):
    seen = set()
    while n is not None and n not in seen:
        seen.add(n); n = nodes[n]
    return n is None
def main():
    nodes = build_tree()
    assert all(reaches_root(nodes, n) for n in nodes), "orphan node in cause tree"
    leaves = [n for n in nodes if n.startswith("factor_")]
    layers = [n for n in nodes if n.startswith("layer_")]
    print("nodes=%d layers=%d factor_leaves=%d" % (len(nodes), len(layers), len(leaves)))
    assert len(leaves) == len(FACTORS)
    print("OK: %s cause tree traced to root (%d factors)" % (''' + json.dumps(name) + ''', len(leaves)))
if __name__ == "__main__":
    main()
'''

def demo_reclog(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
import sqlite3
RECS = ''' + json.dumps(points, ensure_ascii=False) + '''
STATUSES = ["open", "in_progress", "closed"]
def main():
    con = sqlite3.connect(":memory:")
    cur = con.cursor()
    cur.execute("CREATE TABLE recs (id TEXT PRIMARY KEY, text TEXT NOT NULL, "
                "status TEXT CHECK (status IN ('open','in_progress','closed')))")
    for i, r in enumerate(RECS):
        cur.execute("INSERT INTO recs VALUES (?,?,?)",
                    ("%s-R%d" % (''' + json.dumps(rid) + ''', i + 1), r, STATUSES[i % 3]))
    try:
        cur.execute("INSERT INTO recs VALUES (?,?,?)", ("bad", "x", "unknown"))
        print("ERROR: CHECK constraint did not fire")
    except sqlite3.IntegrityError as e:
        print("status constraint enforced:", e)
    cur.execute("SELECT status, COUNT(*) FROM recs GROUP BY status ORDER BY status")
    rows = cur.fetchall()
    total = sum(n for _, n in rows)
    for st, n in rows:
        print("  %-11s %d" % (st, n))
    assert total == len(RECS)
    print("OK: %s tracked %d recommendations with status integrity" % (''' + json.dumps(name) + ''', total))
if __name__ == "__main__":
    main()
'''

def demo_verify(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
TIERS = {
    "official-investigation": ["issuing_body", "final_report", "findings_section", "public_source"],
    "insurance-documented": ["claimant", "covered_event", "causation_link", "adjudication"],
    "publicly-reported": ["source_a", "source_b", "attribution", "correction_policy"],
}
EVIDENCE = {
    "official-investigation": ["issuing_body", "final_report", "findings_section", "public_source"],
    "insurance-documented": ["claimant", "covered_event", "causation_link"],
    "publicly-reported": ["source_a", "attribution"],
}
def check(tier, have):
    need = TIERS[tier]
    return [k for k in need if k not in have]
def main():
    for tier, have in EVIDENCE.items():
        missing = check(tier, have)
        verdict = "COMPLETE" if not missing else "INCOMPLETE (missing: %s)" % ", ".join(missing)
        print("  %-22s -> %s" % (tier, verdict))
    assert not check("official-investigation", EVIDENCE["official-investigation"])
    assert check("insurance-documented", EVIDENCE["insurance-documented"]) == ["adjudication"]
    print("OK: %s verification checklist enforced per tier" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''

def demo_timeline(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
from datetime import date
EVENTS = [
    ("occurrence", date(2020, 1, 15)),
    ("evidence_secured", date(2020, 1, 16)),
    ("preliminary_report", date(2020, 2, 20)),
    ("analysis_complete", date(2020, 8, 11)),
    ("final_report", date(2021, 3, 30)),
]
def main():
    ordered = all(EVENTS[i][1] <= EVENTS[i + 1][1] for i in range(len(EVENTS) - 1))
    assert ordered, "timeline out of order"
    span = (EVENTS[-1][1] - EVENTS[0][1]).days
    for label, d in EVENTS:
        print("  %-18s %s" % (label, d.isoformat()))
    print("span=%d days events=%d" % (span, len(EVENTS)))
    assert span == 440, span
    print("OK: %s timeline validated chronological (%d days)" % (''' + json.dumps(name) + ''', span))
if __name__ == "__main__":
    main()
'''

def demo_stats(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
import statistics
# SYNTHETIC SAMPLE — severity scores illustrating the statistics a crash
# analyst runs; not real casualty data.
SAMPLE = [3, 5, 4, 7, 2, 8, 5, 6, 4, 9, 3, 5, 7, 6, 4, 5, 8, 2, 6, 7,
          5, 4, 6, 3, 7, 5, 8, 4, 6, 5]
def main():
    mu = statistics.mean(SAMPLE)
    med = statistics.median(SAMPLE)
    sd = statistics.stdev(SAMPLE)
    hi = sum(1 for x in SAMPLE if x >= 7)
    print("n=%d mean=%.2f median=%.1f stdev=%.2f severe=%d" % (len(SAMPLE), mu, med, sd, hi))
    assert len(SAMPLE) == 30 and abs(mu - 5.30) < 0.01
    print("NOTE: synthetic sample severities — real analysis uses investigation data.")
    print("OK: %s computed severity statistics" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''

DEMOS = {
    "investigation": demo_investigation,
    "causetree": demo_causetree,
    "reclog": demo_reclog,
    "verify": demo_verify,
    "timeline": demo_timeline,
    "stats": demo_stats,
}

# ============================================================ records

def how_it_works_pub(name, desc, points):
    return ("This record is organized as a formal investigation file. It opens with occurrence "
            "data — the date, location, and vehicle or aircraft involved — then presents the "
            "factual sequence reconstructed from evidence. The analysis examines each causal "
            "factor, and the record closes with the cause determination and the safety outcomes "
            "and recommendations that followed. Key aspects include: " + "; ".join(points) + ".")

def how_it_works_sig(name, desc, points):
    return ("This is an original Signature framework, designed in the Signature system. It defines "
            "its concepts precisely, then gives a repeatable procedure: what to document, in what "
            "order, and how to score, verify, or apply each element. The framework is meant to be "
            "applied to real occurrences — each application produces the specified output. "
            "Key aspects include: " + "; ".join(points) + ".")

def build_record(title, name, group, desc, points, req, standards, citations,
                 src, demo_kind, rid, verification):
    if src == "signature":
        title = title + " (Signature Edition)"
        description = ("Signature original framework: " + desc +
                       " Key aspects include: " + "; ".join(points) + "." +
                       " Designed in the Signature system as an original framework.")
        hiw = how_it_works_sig(name, desc, points)
    else:
        description = desc + " Key aspects include: " + "; ".join(points) + "."
        hiw = how_it_works_pub(name, desc, points)
    rec = {
        "id": rid, "t": title, "g": group, "name": name, "title": title,
        "description": description, "how_it_works": hiw,
        "key_points": list(points), "requirements": req,
        "standards": list(standards), "citations": citations,
        "src": src,
    }
    if verification:
        rec["verification"] = verification
    prog = DEMOS[demo_kind](name, rid, group, points, req)
    rec["demo"] = {"kind": "python", "language": "python",
                   "program": prog,
                   "note": "Working demonstration program (real, runnable stdlib Python)."}
    return rec

def check_record(rec):
    for k in ("id", "t", "g", "name", "title", "description", "how_it_works",
              "key_points", "requirements", "standards", "citations", "src", "demo"):
        assert k in rec, "missing %s in %s" % (k, rec["id"])
    assert len(rec["description"]) > 60, "stub in %s" % rec["id"]
    prog = rec["demo"]["program"]
    assert prog
    compile(prog, rec["id"], "exec")
    blob = json.dumps(rec).lower()
    assert "facebook" not in blob, "facebook ref in %s" % rec["id"]
    assert "bat belt" not in blob, "banned phrase in %s" % rec["id"]
    if rec["src"] == "public-harvest":
        assert "verification" in rec or rec["g"] in (
            "aviation-investigations", "motor-vehicle-crash-data"), \
            "public accident record missing verification field: %s" % rec["id"]

# ============================================================ shard I/O

def write_gz_jsonl(path, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with gzip.open(path, "wt", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

def write_shard_db(slug, recs):
    base = os.path.join(SHARD, "data", slug)
    light = [{"id": r["id"], "t": r["t"], "g": r["g"]} for r in recs]
    write_gz_jsonl(os.path.join(base, "index.jsonl.gz"), light)
    for ci in range(0, len(recs), 100):
        write_gz_jsonl(os.path.join(base, "chunks", "chunk-%04d.jsonl.gz" % (ci // 100)),
                       recs[ci:ci + 100])
    return len(recs)

def update_json_list(path, entries):
    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()
    data = json.loads(raw)
    have = {d["slug"] for d in data["databases"]}
    for e in entries:
        if e["slug"] not in have:
            data["databases"].append(e)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=1, ensure_ascii=False)
        if raw.endswith("\n"):
            f.write("\n")

# ============================================================ DB configs

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, hero_p,
         search_ph, chat_ph, archive_blurb, gen_desc, greet, sig_type,
         schema, fields, gen_fields, gen_kind, source):
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role, "hero_p": hero_p,
        "search_ph": search_ph, "chat_ph": chat_ph,
        "archive_blurb": archive_blurb, "gen_desc": gen_desc, "greet": greet,
        "sig_type": sig_type, "source": source,
        "schema": schema, "fields": fields,
        "gen_fields": gen_fields, "gen_kind": gen_kind,
        "gen_demo_kind": "python",
    }

DBCFG = {
    "crash-data-databases": _cfg(
        "crash-data-databases",
        "The Plane, Jet and Car Crash Investigation Database",
        "Public crash investigation records: aircraft and vehicle occurrences, cause findings, safety outcomes, and recommendations.",
        "crash investigation record", "JAH-CRD-", "JAH Crash Investigation Archivist",
        "crash investigation archivist — aviation and motor-vehicle occurrences",
        "Public <b>crash investigation records</b> — <b>aviation occurrences</b> and "
        "<b>motor-vehicle crash data</b> documented from public investigation records. "
        "Every record carries the full entry: occurrence data, cause findings, safety outcomes, "
        "recommendations, citations, and a working demonstration program.",
        "Search crash investigations...", "Ask about crash investigations...",
        "Seeded public-record crash investigation archive (JAH-CRD- records), marching toward one million records.",
        "Generate clearly-labeled structural crash-investigation studies. Seeded archive records are the authoritative entries.",
        "I am the JAH Crash Investigation Archivist. Ask me about crash investigations.",
        "Public records organized in the Signature system",
        "id, t, g, name, title, description, how_it_works, key_points, requirements, standards, citations, src, demo",
        "aviation-investigations · motor-vehicle-crash-data",
        ["aviation-investigations", "motor-vehicle-crash-data"],
        "crash-investigation-study", "public"),
    "crash-data-databases-signature": _cfg(
        "crash-data-databases-signature",
        "The Plane, Jet and Car Crash Investigation Signature Database",
        "Original Signature crash-analysis frameworks and safety-design doctrines.",
        "Signature crash-analysis record", "JAH-CRDG-", "JAH Crash Analysis Architect (Signature)",
        "crash analysis architect — Signature causal and safety-design frameworks",
        "Original <b>Signature crash-analysis frameworks</b> — <b>causal-analysis methods</b> and "
        "<b>safety-design doctrines</b> created in the Signature system. "
        "Every record carries the full entry: framework definition, procedure, output specification, "
        "and a working demonstration program.",
        "Search Signature crash frameworks...", "Ask about Signature crash analysis...",
        "Seeded Signature-original crash-analysis archive (JAH-CRDG- records), marching toward one million records.",
        "Generate clearly-labeled structural Signature crash-analysis studies. Seeded archive records are the authoritative entries.",
        "I am the JAH Crash Analysis Architect. Ask me about Signature crash-analysis frameworks.",
        "Signature originals organized in the Signature system",
        "id, t, g, name, title, description, how_it_works, key_points, requirements, standards, citations, src, demo",
        "causal-analysis-frameworks · safety-design-frameworks",
        ["causal-analysis-frameworks", "safety-design-frameworks"],
        "signature-crash-analysis-study", "signature"),
    "accidents-insurance-proven": _cfg(
        "accidents-insurance-proven",
        "The All Accidents Insurance-Proven Documentation Database",
        "Accident records with verified documentation only — every record carries its verification level.",
        "verified accident record", "JAH-AIP-", "JAH Accident Documentation Archivist",
        "accident documentation archivist — verified accident records by tier",
        "Verified <b>accident documentation</b> — every record carries an explicit "
        "<b>verification level</b>: official-investigation, insurance-documented, or publicly-reported. "
        "Every record carries the full entry: occurrence data, findings, verification evidence, "
        "citations, and a working demonstration program.",
        "Search verified accident records...", "Ask about verified accidents...",
        "Seeded verified accident archive (JAH-AIP- records), marching toward one million records.",
        "Generate clearly-labeled structural accident-documentation studies. Seeded archive records are the authoritative entries.",
        "I am the JAH Accident Documentation Archivist. Ask me about verified accident records.",
        "Public records organized in the Signature system",
        "id, t, g, name, title, description, how_it_works, key_points, requirements, standards, citations, verification, src, demo",
        "official-investigation-records · insurance-documented-records · publicly-reported-records",
        ["official-investigation-records", "insurance-documented-records", "publicly-reported-records"],
        "verified-accident-study", "public"),
    "accidents-insurance-proven-signature": _cfg(
        "accidents-insurance-proven-signature",
        "The All Accidents Insurance-Proven Documentation Signature Database",
        "Original Signature accident-verification frameworks and documentation standards.",
        "Signature verification record", "JAH-AIPG-", "JAH Verification Architect (Signature)",
        "verification architect — Signature verification frameworks and documentation standards",
        "Original <b>Signature verification frameworks</b> — <b>evidence standards</b> and "
        "<b>documentation standards</b> created in the Signature system. "
        "Every record carries the full entry: framework definition, procedure, output specification, "
        "and a working demonstration program.",
        "Search Signature verification frameworks...", "Ask about Signature verification...",
        "Seeded Signature-original verification archive (JAH-AIPG- records), marching toward one million records.",
        "Generate clearly-labeled structural Signature verification studies. Seeded archive records are the authoritative entries.",
        "I am the JAH Verification Architect. Ask me about Signature verification frameworks.",
        "Signature originals organized in the Signature system",
        "id, t, g, name, title, description, how_it_works, key_points, requirements, standards, citations, src, demo",
        "verification-frameworks · documentation-standards",
        ["verification-frameworks", "documentation-standards"],
        "signature-verification-study", "signature"),
}

DB_SOURCES = {
    "crash-data-databases": (E_CRASH_PUB, "public-harvest"),
    "crash-data-databases-signature": (E_CRASH_SIG, "signature"),
    "accidents-insurance-proven": (E_ACC_PUB, "public-harvest"),
    "accidents-insurance-proven-signature": (E_ACC_SIG, "signature"),
}

def manifest_entry(slug, n):
    c = DBCFG[slug]
    return {"slug": slug, "name": c["name"], "tagline": c["tagline"],
            "record_kind": c["record_kind"], "id_prefix": c["prefix"],
            "ai_name": c["ai"], "local_index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
            "record_count": n, "status": "live", "full_records": n,
            "index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
            "chunk_pattern": "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz",
            "source": c["source"]}

def api_entry(slug, n):
    c = DBCFG[slug]
    return {"slug": slug, "name": c["name"], "tagline": c["tagline"],
            "record_kind": c["record_kind"], "record_count": n, "status": "live",
            "index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz"}

# ============================================================ main

def main():
    sys.path.insert(0, os.path.join(REPO, "code", "numbering-build"))
    spec = importlib.util.spec_from_file_location(
        "nb_build", os.path.join(REPO, "code", "numbering-build", "build.py"))
    nb = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(nb)
    nb.DBCFG = DBCFG

    sweep_path = "/home/hatch/workspace/goals/database-quality-audit/hidden_files/patches/sweep-db-pages.py"
    sweep = None
    if os.path.exists(sweep_path):
        sspec = importlib.util.spec_from_file_location("sweep", sweep_path)
        sweep = importlib.util.module_from_spec(sspec)
        sspec.loader.exec_module(sweep)

    # ---- step 1: build records (dedupe-gated, whole system)
    built = {}
    for slug, (entries, src) in DB_SOURCES.items():
        cfg = DBCFG[slug]
        recs = []
        for (key, egroup, title, desc, points, req, standards, citations,
             demo_kind, verification) in entries:
            ftitle = title + " (Signature Edition)" if src == "signature" else title
            hits = [h for h in GATE.check(slug, ftitle) if h[0] != slug]
            if hits:
                print("  gate refused (cross-db dupe): %s" % ftitle, flush=True)
                continue
            rid = "%s%06d" % (cfg["prefix"], len(recs) + 1)
            rec = build_record(title, title, egroup, desc, points, req, standards,
                               citations, src, demo_kind, rid, verification)
            check_record(rec)
            GATE.admit(slug, ftitle, rid)
            recs.append(rec)
        assert recs, "empty db " + slug
        ids = [r["id"] for r in recs]
        assert len(ids) == len(set(ids)), "dup ids in %s" % slug
        assert all(i.startswith(cfg["prefix"]) for i in ids), "prefix drift in %s" % slug
        built[slug] = recs
        print("records: %-42s %d" % (slug, len(recs)), flush=True)

    # ---- step 2: write shard data
    total = 0
    for slug, recs in built.items():
        n = write_shard_db(slug, recs)
        total += n
        print("shard:   %-42s %d records" % (slug, n), flush=True)

    # ---- step 3: execute one demo per archetype
    import subprocess
    markers = {"investigation": "investigation file validated",
               "causetree": "cause tree traced",
               "reclog": "recommendations with status",
               "verify": "verification checklist",
               "timeline": "timeline validated",
               "stats": "severity statistics"}
    done = set()
    for slug, recs in built.items():
        for r in recs:
            prog = r["demo"]["program"]
            for k, m in markers.items():
                if k not in done and m in prog:
                    done.add(k)
                    p = subprocess.run([sys.executable, "-c", prog],
                                       capture_output=True, text=True, timeout=60)
                    assert p.returncode == 0, "demo failed %s: %s" % (r["id"], p.stderr[-500:])
                    assert "OK:" in p.stdout, "demo no OK marker %s" % r["id"]
                    print("demo ok: %-14s %s" % (k, r["id"]), flush=True)
    assert len(done) == len(markers), "not all archetypes executed: %s" % (set(markers) - done)
    print("demo execution: %d archetypes ran OK" % len(done), flush=True)

    # ---- step 4: pages + generators
    with open(TEMPLATE, "r", encoding="utf-8") as f:
        template = f.read()
    for slug, recs in built.items():
        page = nb.build_page(slug, template)
        page = page.replace(
            "Generate structural synthetic intelligence studies. Seeded archive records are the authoritative entries.",
            DBCFG[slug]["gen_desc"])
        assert 'id="stCount"' in page and "var SLUG='%s';" % slug in page
        assert "minmax(120px,1fr)" in page and "pre.codeblock" in page
        assert "facebook" not in page.lower()
        assert "synthetic intelligence" not in page.lower(), "template leftover in %s" % slug
        assert "bat belt" not in page.lower(), "banned phrase in page %s" % slug
        assert "dedupe.js" in page and "jahdb-xdb.js" in page, "script tags missing in %s" % slug
        ddir = os.path.join(REPO, "db", slug)
        os.makedirs(ddir, exist_ok=True)
        ppath = os.path.join(ddir, "index.html")
        with open(ppath, "w", encoding="utf-8") as f:
            f.write(page)
        notes = []
        if sweep:
            _, notes = sweep.process_page(ppath)
        topics = {}
        for r in recs:
            topics.setdefault(r["g"], []).append("%s — %s" % (r["t"], r["g"]))
        gen_js = nb.build_gen_js(slug, topics, DBCFG[slug])
        assert "facebook" not in gen_js.lower() and "bat belt" not in gen_js.lower()
        with open(os.path.join(ddir, "gen-%s.js" % slug), "w", encoding="utf-8") as f:
            f.write(gen_js)
        print("page:    db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ",".join(notes)), flush=True)

    # ---- step 5: manifest + api.json
    entries_m = [manifest_entry(s, len(built[s])) for s in built]
    update_json_list(os.path.join(REPO, "data", "manifest.json"), entries_m)
    entries_a = [api_entry(s, len(built[s])) for s in built]
    update_json_list(os.path.join(REPO, "api.json"), entries_a)
    print("manifest + api.json: appended %d databases, %d records" % (len(built), total))
    print("NEXT: run python3 code/restamp_counts.py, then commit + push.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
