#!/usr/bin/env python3
"""Build The Event Streams Database and The Event Streams Signature
Database (missing-115 program, Wave 1 - operational data, item 48).

Pipeline replicates code/component-parts-catalog-build/build.py exactly
for page structure and pipeline, with two deliberate differences owned
by the missing-115 program:
  - NO writes to data/manifest.json or api.json (a merger handles those).
  - Writes the merger fragment to
    ~/workspace/hidden_files/missing-builds/fragments/event-streams.json.

Verified 2026-10-17: RAW SWEEP over the full manifest (2,390 databases),
prefix check of every id_prefix value, and a full grep of every shard
index in jah-databases-data-1 for '"id":"JAH-EVS': zero 'event-streams'
slugs/names; zero title collisions across all 68 titles through the
whole-system dedupe gate before authoring. ID prefixes JAH-EVS- (public)
and JAH-EVSS- (signature) verified free in manifest id_prefix values
and in every shard index.

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written
in ladder order so pages present simple -> compounded -> complex.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""
import importlib.util
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = "/home/hatch/workspace/jah-databases"
SHARD = "/home/hatch/workspace/jah-databases-data-1"
SHARD_BASE = "https://justinahiggins614-cmyk.github.io/jah-databases-data-1"
TEMPLATE = os.path.join(REPO, "db", "public-synthetic-intelligence", "index.html")
FRAGMENTS = "/home/hatch/workspace/hidden_files/missing-builds/fragments"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_event_streams import ENTRIES, SIG_TAIL
from demos_event_streams import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Stream Method: "
                "every event a signed testimony carrying its lineage stamp, "
                "the log the ledger of testimony, the stream the river, "
                "replay the return, ordering the oath of sequence, "
                "partitioning the allotment, exactly-once the pledge of "
                "single delivery. Clearly labeled Signature-made, never "
                "presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked event-stream "
                "engineering: events, timestamps, the append-only log, "
                "schemas, ordering and causality, partitioning, delivery "
                "semantics, change data capture, the outbox pattern, event "
                "stores, snapshots, consumer offsets, event sourcing, "
                "stream processing, schema evolution, replay, observability, "
                "and recovery - every record carrying description, how it "
                "works, key points, requirements, standards, citations, and "
                "a working demonstration program, organized in the Signature "
                "system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(what an event is, commands events and state, event time vs "
              "processing time, the append-only log, schemas, ordering and "
              "causality, partitioning, serialization, consumers and groups, "
              "delivery semantics) -> Compounded (change data capture, the "
              "outbox pattern, event store design, snapshotting, consumer "
              "offsets, event sourcing, stateful stream processing, "
              "windows, pub-sub, schema evolution, correlation ids, "
              "projections, replay and reprocessing, dead letters, "
              "watermarks, routing and filtering) -> Advanced (sagas, "
              "end-to-end exactly-once, compaction retention and archiving, "
              "governance and the schema registry, observability, "
              "multi-region replication, security and redaction, temporal "
              "queries).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search events, timestamps, logs, schemas, causality, partitions, delivery semantics, CDC, outbox, event stores, snapshots, offsets, sourcing, windows, replay, sagas, watermarks...",
        "chat_ph": "Ask about event streams...",
        "archive_blurb": ("Seeded %s event stream records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled event stream studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about event streams - from what an event is through commands, timestamps, logs, schemas, causality, partitions, serialization, consumers, and delivery semantics, through CDC, outbox, event stores, snapshots, offsets, sourcing, stream processing, windows, pub-sub, schema evolution, correlation, projections, replay, dead letters, watermarks, and routing, to sagas, exactly-once, compaction, governance, observability, multi-region replication, security, and temporal queries." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "event-stream-study", "gen_demo_kind": "event-stream-demo",
        "source": source,
    }

CIT_PUB = ("Event-stream engineering (standard references: Kleppmann M. "
           "Designing Data-Intensive Applications. OReilly Media; 2017; "
           "Kreps J. The Log: What every software engineer should know "
           "about real-time data's unifying abstraction. LinkedIn "
           "Engineering blog; 2013; Fowler M. Event Sourcing. "
           "martinfowler.com/bliki; 2005; Fowler M. CQRS. "
           "martinfowler.com/bliki; 2011; Young G. writings on event "
           "stores and CQRS; Helland P. Life beyond Distributed "
           "Transactions: an Apostate's Opinion. CIDR; 2007; Lamport L. "
           "Time, Clocks, and the Ordering of Events in a Distributed "
           "System. CACM; 1978; Garcia-Molina H, Salem K. Sagas. ACM "
           "SIGMOD; 1987; CloudEvents Specification. CNCF; v1.0; Apache "
           "Avro Specification 1.11 schema resolution; Protocol Buffers "
           "field numbering; W3C Trace Context; OpenTelemetry "
           "Specification; and the other landmarks cited per record).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature Stream "
                     "Method - every event a signed testimony carrying its "
                     "lineage stamp - clearly labeled Signature-made.")

DBCFG = {}
DBCFG["event-streams"] = _cfg(
    "event-streams", "The Event Streams Database",
    "Sequences of events, their timestamps, processing state, and replay: real, "
    "fact-checked event-stream engineering across events, logs, schemas, ordering "
    "and causality, partitioning, delivery semantics, change data capture, event "
    "stores, snapshots, offsets, event sourcing, stream processing, replay, and "
    "recovery - every record carrying description, how it works, key points, "
    "requirements, standards, citations, and a working demonstration program, "
    "taught progressively along the ladder.",
    "event stream record", "JAH-EVS-", "JAH Event Streams Archivist",
    "event streams archivist - sequences of events, event timestamps, "
    "processing state, and replay across schemas, ordering and causality, "
    "partitioning, delivery semantics, change data capture, event stores, "
    "snapshots, offsets, sourcing, stream processing, replay, and recovery; "
    "teaching progressively along the ladder from foundations through "
    "compounded to advanced; answers from many angles - definition, example, "
    "analogy, application, history, math, how-to - using only archive data "
    "from this system",
    CIT_PUB, "public")
DBCFG["event-streams-signature"] = _cfg(
    "event-streams-signature", "The Event Streams Signature Database",
    "His original Signature Stream Method: every event a signed testimony "
    "carrying its lineage stamp, the log the ledger of testimony, the stream "
    "the river, replay the return. The full ladder from what an event is "
    "through timestamps, logs, schemas, causality, partitions, and delivery "
    "semantics, through CDC, outbox, event stores, snapshots, offsets, "
    "sourcing, processing, and replay, to sagas, exactly-once, governance, "
    "observability, and time travel, reframed as Signature science. Clearly "
    "labeled Signature-made, never presented as authentic public record.",
    "event stream record", "JAH-EVSS-", "JAH Event Streams Archivist (Signature)",
    "event streams archivist - Signature editions: his original Signature "
    "Stream Method, every event a signed testimony carrying its lineage "
    "stamp, clearly labeled Signature-made and never presented as authentic "
    "public record; teaches progressively along the ladder from foundations "
    "through compounded to advanced; answers from many angles - definition, "
    "example, analogy, application, history, math, how-to - using only "
    "archive data from this system",
    CIT_SIG, "signature")

base.DBCFG = DBCFG

assert set(DEMOS) == {e["key"] for e in ENTRIES}, "demo map misses entries"


def build_records(slug, source):
    cfg = DBCFG[slug]
    sig = source == "signature"
    ordered = sorted(enumerate(ENTRIES), key=lambda p: (p[1]["ladder_rank"], p[0]))
    recs = []
    for _, e in ordered:
        name = e["name"]
        title = name + " (Signature Edition)" if sig else name
        if [h for h in base.GATE.check(slug, title) if h[0] != slug]:
            print("  gate refused (cross-db dupe): %s" % title, flush=True)
            continue
        rid = "%s%06d" % (cfg["prefix"], len(recs) + 1)
        if sig:
            description = ("Signature original interpretation. " + e["sig_lens"] + " "
                           + e["description"])
            how = e["sig_lens"] + " " + e["how_it_works"]
            citations = list(e["citations"]) + [SIG_TAIL]
        else:
            description = e["description"]
            how = e["how_it_works"]
            citations = list(e["citations"])
        rec = {
            "id": rid, "t": title, "g": e["group"], "name": name, "title": title,
            "description": description,
            "how_it_works": how,
            "key_points": list(e["key_points"]),
            "requirements": list(e["requirements"]),
            "standards": list(e["standards"]),
            "citations": citations,
            "src": "signature" if sig else "public-harvest",
            "ladder_rank": e["ladder_rank"],
            "ladder_tier": e["ladder_tier"],
        }
        demo_fn = DEMOS[e["key"]]
        program = demo_fn(base._hdr, name if not sig else title, rid, e["group"],
                          e["key_points"], "; ".join(e["requirements"]))
        rec["demo"] = {"kind": "python", "language": "python",
                       "program": program,
                       "note": "Working demonstration program (real, runnable Python)."}
        base.GATE.admit(slug, title, rid)
        recs.append(rec)
    ranks = [r["ladder_rank"] for r in recs]
    assert ranks == sorted(ranks), "records not in ladder order for %s" % slug
    return recs


def fragment_entry(slug, n):
    c = DBCFG[slug]
    base_url = SHARD_BASE + "/data/" + slug + "/index.jsonl.gz"
    return {
        "slug": slug, "name": c["name"], "tagline": c["tagline"],
        "record_kind": c["record_kind"], "id_prefix": c["prefix"],
        "ai_name": c["ai"], "local_index": base_url,
        "record_count": n, "status": "live", "full_records": n,
        "index": base_url,
        "chunk_pattern": "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz",
        "source": "public-harvest" if c["source"] == "public" else "signature",
    }


def main():
    sys.path.insert(0, os.path.join(REPO, "code", "numbering-build"))
    spec = importlib.util.spec_from_file_location(
        "nb_build", os.path.join(REPO, "code", "numbering-build", "build.py"))
    nb = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(nb)
    nb.DBCFG = DBCFG

    sweep_path = "/home/hatch/workspace/goals/database-quality-audit/hidden_files/patches/sweep-db-pages.py"
    sspec = importlib.util.spec_from_file_location("sweep", sweep_path)
    sweep = importlib.util.module_from_spec(sspec)
    sspec.loader.exec_module(sweep)

    built = {}
    for slug in ("event-streams", "event-streams-signature"):
        source = "signature" if slug.endswith("-signature") else "public"
        built[slug] = build_records(slug, source)

    total = 0
    for slug, recs in built.items():
        cfg = DBCFG[slug]
        ids = [r["id"] for r in recs]
        assert len(ids) == len(set(ids)), "dup ids in %s" % slug
        assert all(i.startswith(cfg["prefix"]) for i in ids), "prefix drift in %s" % slug
        assert len(recs) == 34, "expected 34 records in %s, got %d" % (slug, len(recs))
        for r in recs:
            for k in ("id", "t", "g", "name", "title", "description", "how_it_works",
                      "key_points", "requirements", "standards", "citations",
                      "src", "ladder_rank", "ladder_tier", "demo"):
                assert k in r, "missing %s in %s" % (k, r["id"])
            prog = r["demo"].get("program")
            assert prog and len(r["description"]) > 200, "stub in %s" % r["id"]
            assert 1 <= r["ladder_rank"] <= 10, "ladder_rank out of range in %s" % r["id"]
            assert r["ladder_tier"] in ("foundations", "compounded", "advanced"), \
                "bad ladder_tier in %s" % r["id"]
            compile(prog, r["id"], "exec")
            blob = json.dumps(r).lower()
            assert "facebook" not in blob, "facebook ref in %s" % r["id"]
            assert "bat belt" not in blob, "banned phrase in %s" % r["id"]
            if slug.endswith("-signature"):
                assert "(signature edition)" in r["title"].lower(), "sig title missing suffix"
                assert r["src"] == "signature"
            else:
                assert r["src"] == "public-harvest"
        total += len(recs)
        n = base.write_shard_db(slug, recs)
        print("shard: %-38s %d records" % (slug, n), flush=True)

    for slug, recs in built.items():
        for r in recs:
            prog = r["demo"]["program"]
            p = subprocess.run([sys.executable, "-c", prog],
                               capture_output=True, text=True, timeout=180)
            assert p.returncode == 0, "demo failed %s: %s" % (r["id"], p.stderr[-800:])
            assert "OK:" in p.stdout, "demo no OK marker %s" % r["id"]
    print("demo execution: all %d demos ran OK" % total, flush=True)

    with open(TEMPLATE, "r", encoding="utf-8") as f:
        template = f.read()
    for slug, recs in built.items():
        page = nb.build_page(slug, template)
        page = page.replace(
            "Generate structural synthetic intelligence studies. Seeded archive records are the authoritative entries.",
            DBCFG[slug]["gen_desc"])
        assert 'id="stCount"' in page and "var SLUG='%s';" % slug in page
        assert "minmax(120px,1fr)" in page and "pre.codeblock" in page
        assert "pill-ex" in page and "qmerge" in page, "Exhaustive pill / merger button missing"
        assert "dataset.p" in page, "tab-handler guard missing"
        assert "facebook" not in page.lower()
        assert "synthetic intelligence" not in page.lower(), "template leftover in %s" % slug
        assert "public-synthetic-intelligence" not in page, "slug leftover in %s" % slug
        assert "bat belt" not in page.lower(), "banned phrase in page %s" % slug
        ddir = os.path.join(REPO, "db", slug)
        os.makedirs(ddir, exist_ok=True)
        ppath = os.path.join(ddir, "index.html")
        with open(ppath, "w", encoding="utf-8") as f:
            f.write(page)
        changed, notes = sweep.process_page(ppath)
        topics = {}
        for r in recs:
            topics.setdefault(r["g"], []).append("%s - %s" % (r["t"], r["g"]))
        gen_js = nb.build_gen_js(slug, topics, DBCFG[slug])
        assert "facebook" not in gen_js.lower() and "bat belt" not in gen_js.lower()
        assert "synthetic intelligence" not in gen_js.lower(), "field leftover in gen js %s" % slug
        with open(os.path.join(ddir, "gen-%s.js" % slug), "w", encoding="utf-8") as f:
            f.write(gen_js)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)

    # merger fragment (NO manifest.json / api.json writes - the merger owns those)
    os.makedirs(FRAGMENTS, exist_ok=True)
    frag = {
        "public": fragment_entry("event-streams", len(built["event-streams"])),
        "signature": fragment_entry("event-streams-signature", len(built["event-streams-signature"])),
    }
    frag["public"]["tagline"] = DBCFG["event-streams"]["tagline"]
    frag["signature"]["tagline"] = DBCFG["event-streams-signature"]["tagline"]
    fpath = os.path.join(FRAGMENTS, "event-streams.json")
    with open(fpath, "w", encoding="utf-8") as f:
        json.dump(frag, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print("fragment: %s" % fpath, flush=True)
    print("DONE: 2 databases, %d records. Merger owns manifest/api.json + restamp." % total)
    return 0


if __name__ == "__main__":
    sys.exit(main())
