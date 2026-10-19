#!/usr/bin/env python3
"""Build the Loving Statements databases for JAH Databases
(2026-10-17 16:15 fun/social batch).

The Loving Statements Database - loving statements: expressions of love,
devotion, and appreciation for partners, family, and friends. Every record
is a statement WITH context guidance: when to say it, and how to
personalize it. Warm and sincere only.

Creates two NEW databases, 34 ladder-ordered records each:

  loving-statements            - The Loving Statements Database (public-harvest)
  loving-statements-signature  - The Loving Statements Signature Database
                                 (Signature Edition, src signature)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced): everyday affection ->
heartfelt devotion -> profound devotion.

ID prefixes: JAH-LVST- (public) and JAH-LVSTS- (signature), verified free
in the manifest (zero hits) and in all 831 shard index files in
jah-databases-data-1 (zero hits).

Demo cores: statement-of-the-day picker, occasion matcher,
personalization engine, card/letter formatters, ledgers, schedules -
all real stdlib-only Python, machine-executed here, tight-bounds asserts
(never float exact-equality), each ending with the OK marker.

CONCURRENCY: this builder NEVER touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and NEVER commits or
pushes. The merger handles manifest/api/restamp/commit. This script only
creates: db/loving-statements/ + db/loving-statements-signature/
(index.html + gen-*.js each), the shard files under
jah-databases-data-1/data/loving-statements[-signature]/, and the
missing-builds fragment JSON.

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
FRAG_DIR = "/home/hatch/workspace/hidden_files/missing-builds/fragments"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_loving_statements import ENTRIES, SIG_TAIL
from demos_loving_statements import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Devotion Method: "
                "every loving statement a stamped covenant, love declared "
                "deliberately and on the record, affection treated as eternal "
                "data, devotion as engineering. Clearly labeled Signature-made, "
                "never presented as authentic public record.")
    pub_line = ("Public records - real, generatable expressions of love, "
                "devotion, and appreciation for partners, family, and friends: "
                "everyday affection, partner devotion, family gratitude, "
                "friendship loyalty, and profound devotion - each record a "
                "full statement plus when-to-say-it and how-to-personalize "
                "guidance, organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(everyday affection - mattering, thanks, noticing, morning "
              "words, presence, pride, home, blessing, sensory devotion, "
              "daily choosing, small-things gratitude, safety, admired "
              "becoming, the way they love, favorite person, patience) -> "
              "Compounded (heartfelt devotion - hard seasons, belief, "
              "apology and repair, life-changing love, teammate alliance, "
              "family sacrifice, loyal friendship, forgiveness, witnessed "
              "beauty, anniversary vows, the seen heart, lifetime gratitude) "
              "-> Advanced (profound devotion - covenant, greatest work, "
              "long promise, remaking love, until the end, legacy letter).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search loving statements, devotion, appreciation, affection, partner love, family gratitude, friendship, forgiveness, vows, legacy letters...",
        "chat_ph": "Ask about loving statements...",
        "archive_blurb": ("Seeded %s loving statement records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled loving statement studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about loving statements - everyday affection, partner devotion, family gratitude, friendship loyalty, forgiveness and repair, vows, and legacy letters - from the simplest daily words through heartfelt devotion to profound devotion." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "loving-statement-study", "gen_demo_kind": "loving-statement-demo",
        "source": source,
    }

CIT_PUB = ("Loving statements (reference landmarks: Shakespeare W. Sonnet 116. "
           "1609, public domain; Browning EB. Sonnets from the Portuguese. "
           "1850, public domain; Gibran K. The Prophet. 1923, public domain; "
           "Chapman G. The 5 Love Languages. 1992; Gottman JM. The Seven "
           "Principles for Making Marriage Work. 1999; Rosenberg MB. "
           "Nonviolent Communication. 1999; Fromm E. The Art of Loving. 1956; "
           "Lewis CS. The Four Loves. 1960).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature Devotion "
                     "Method - every loving statement a stamped covenant, "
                     "clearly labeled Signature-made.")

DBCFG = {}
DBCFG["loving-statements"] = _cfg(
    "loving-statements", "The Loving Statements Database",
    "Loving statements for partners, family, and friends: expressions of "
    "love, devotion, and appreciation, each record a full statement with "
    "when-to-say-it and how-to-personalize guidance - warm and sincere, "
    "taught progressively along the ladder.",
    "loving statement record", "JAH-LVST-", "JAH Loving Statements Archivist",
    "loving statements archivist - expressions of love, devotion, and "
    "appreciation for partners, family, and friends, each record a full "
    "statement with when-to-say-it and how-to-personalize guidance; warm "
    "and sincere only; teaching progressively along the ladder from "
    "foundations through compounded to advanced; answers from many angles - "
    "definition, example, analogy, application, history, how-to - using only "
    "archive data from this system",
    CIT_PUB, "public")
DBCFG["loving-statements-signature"] = _cfg(
    "loving-statements-signature", "The Loving Statements Signature Database",
    "His original Signature Devotion Method: every loving statement a "
    "stamped covenant, love declared deliberately and on the record, "
    "affection treated as eternal data, devotion as engineering. The full "
    "ladder from everyday affection through heartfelt devotion to profound "
    "devotion, reframed as Signature science. Clearly labeled "
    "Signature-made, never presented as authentic public record.",
    "loving statement record", "JAH-LVSTS-", "JAH Loving Statements Archivist (Signature)",
    "loving statements archivist - Signature editions: his original "
    "Signature Devotion Method, every loving statement a stamped covenant "
    "and devotion as engineering, clearly labeled Signature-made and never "
    "presented as authentic public record; teaches progressively along the "
    "ladder from foundations through compounded to advanced; answers from "
    "many angles - definition, example, analogy, application, history, "
    "how-to - using only archive data from this system",
    CIT_SIG, "signature")

base.DBCFG = DBCFG

assert set(DEMOS) == {e["key"] for e in ENTRIES}, "demo map misses entries"


def _statement_of(e):
    d = e["description"]
    return d[1:d.index('."') + 1]


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
        statement = _statement_of(e)
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
                          e["key_points"], "; ".join(e["requirements"]), statement)
        rec["demo"] = {"kind": "python", "language": "python",
                       "program": program,
                       "note": "Working demonstration program (real, runnable Python)."}
        base.GATE.admit(slug, title, rid)
        recs.append(rec)
    ranks = [r["ladder_rank"] for r in recs]
    assert ranks == sorted(ranks), "records not in ladder order for %s" % slug
    return recs


def write_fragment(built):
    frag = {}
    for slug in ("loving-statements", "loving-statements-signature"):
        cfg = DBCFG[slug]
        sig = slug.endswith("-signature")
        frag["signature" if sig else "public"] = {
            "slug": slug,
            "name": cfg["name"],
            "tagline": cfg["tagline"],
            "record_kind": cfg["record_kind"],
            "id_prefix": cfg["prefix"],
            "ai_name": cfg["ai"],
            "local_index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
            "record_count": len(built[slug]),
            "status": "live",
            "full_records": len(built[slug]),
            "index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
            "chunk_pattern": "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz",
            "source": "signature" if sig else "public-harvest",
        }
    os.makedirs(FRAG_DIR, exist_ok=True)
    path = os.path.join(FRAG_DIR, "loving-statements.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(frag, f, indent=1, ensure_ascii=False)
        f.write("\n")
    print("fragment: %s" % path, flush=True)
    return path


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
    for slug in ("loving-statements", "loving-statements-signature"):
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
        assert "universal build" not in page.lower(), "field leftover in %s" % slug
        assert "universal-build" not in page, "slug leftover in %s" % slug
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
        assert "universal build" not in gen_js.lower(), "field leftover in gen js %s" % slug
        with open(os.path.join(ddir, "gen-%s.js" % slug), "w", encoding="utf-8") as f:
            f.write(gen_js)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)

    frag_path = write_fragment(built)

    print("records built: %d (34 public + 34 signature)" % total)
    print("MERGER NEXT: manifest/api/restamp/commit/push are the merger's job - not done here.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
