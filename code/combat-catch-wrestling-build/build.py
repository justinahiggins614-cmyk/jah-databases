#!/usr/bin/env python3
"""Build the Catch Wrestling Combat databases for JAH Databases
(combat batch 3).

Two NEW databases, 34 ladder-ordered records each:

  combat-catch-wrestling            - Catch Wrestling Combat Database
                                      (public-harvest: real, fact-checked
                                      catch-as-catch-can wrestling -
                                      stance and base, ties and hand
                                      fighting, takedowns, rides and
                                      turns, hooks and submissions,
                                      pinning combinations - every record
                                      a technique with HOW TO DO IT
                                      step-by-step body mechanics;
                                      standard references Shannon J. Say
                                      Uncle! (ECW Press; 2005);
                                      Hackenschmidt G. The Way to Live
                                      (1908); Burns M. Lessons in
                                      Wrestling and Physical Culture
                                      (1914); the Robinson/Gotch catch
                                      coaching lineage; UWW international
                                      wrestling rules; USA Wrestling
                                      coaching materials)
  combat-catch-wrestling-signature  - Catch Wrestling Combat Signature
                                      Database
                                      (his original Signature Combat
                                      Method: the hook is the oath, the
                                      ride is the watch, and the pin is
                                      the seal - every technique a
                                      covenant of leverage; src
                                      signature, titles suffixed
                                      " (Signature Edition)", never
                                      presented as authentic public
                                      record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written
in ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-CBCW- (public) and JAH-CBCWS- (signature), verified free
in the manifest (zero exact/substring hits) and in every shard index
(zero hits); the dedupe gate check on all 68 titles returned zero
refusals.

Safety: civilian martial-arts instruction only - cooperative partners,
qualified supervision, early taps, extra control on neck and leg
attacks. Nothing on neutralizing/defeating military or defense-grade
systems.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_catch_wrestling.py). Every demo prints its real
computed values, asserts tight bounds (never float exact-equality), and
ends with the OK marker; the build machine-executes all 68 demos.

CONCURRENCY: this build NEVER touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and NEVER commits or
pushes. The merger handles manifest/api/restamp. Only writes:
  db/combat-catch-wrestling[/-signature]/
  ~/workspace/jah-databases-data-1/data/combat-catch-wrestling[/-signature]/
  ~/workspace/hidden_files/missing-builds/fragments/combat-catch-wrestling.json

Never the words "bat belt" anywhere. No website references. No Facebook.
"""
import importlib.util
import json
import os
import re
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
from entries_catch_wrestling import ENTRIES, SIG_TAIL
from demos_catch_wrestling import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Combat Method: "
                "the hook is the oath, the ride is the watch, and the pin is "
                "the seal. Every technique is a covenant of leverage - the "
                "wrestler swears the position, the partner keeps it honest, "
                "and the hold is the signature. Clearly labeled "
                "Signature-made, never presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked catch-as-catch-can "
                "wrestling: stance and base, ties and hand fighting, "
                "takedowns and throws, rides and turns, hooks and "
                "submissions, pinning combinations - every record a "
                "technique with HOW TO DO IT step-by-step body mechanics, "
                "taught progressively along the ladder.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(stance and base, posture and level changes, hand fighting, "
              "wrist control and the two-on-one, snap-down and go-behind, "
              "front headlock, sprawl, hip bump and sit-out escapes, "
              "Granby roll, bridging, tight waist and crossface ride, half "
              "nelson) -> Compounded (bar arm and chicken wing, double-leg "
              "takedown, double wrist lock, key lock, figure-four toe hold, "
              "straight ankle lock, straight arm bar, guillotine, "
              "single-leg finishes, firemans carry, hip throws, near-side "
              "cradle, far-side and inside-out cradles, head-and-arm "
              "choke, can opener, banana split) -> Advanced (heel hook, "
              "Japanese necktie, power half nelson and leg-ride chains, "
              "scarf-hold arm bar, submission chains, the catch chain "
              "ride-hook-pin flow).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search stance, ties, takedowns, snap-down, front headlock, sprawl, half nelson, cradle, double wrist lock, key lock, arm bar, guillotine, toe hold, ankle lock, heel hook, necktie, power half, submission chains...",
        "chat_ph": "Ask about catch wrestling techniques...",
        "archive_blurb": ("Seeded %s catch wrestling technique records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled catch wrestling technique studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about catch wrestling - from stance and base through ties, takedowns, rides, and turns, through hooks, locks, and pinning combinations, to advanced chains and the full ride-hook-pin flow." % ai,
        "gen_fields": ["Foundations", "Rides and Turns", "Takedowns and Throws", "Hooks and Submissions", "Pinning Combinations", "Advanced Hooks and Chains"],
        "gen_kind": "catch-wrestling-technique", "gen_demo_kind": "catch-wrestling-demo",
        "source": source,
    }

CIT_PUB = ("Catch-as-catch-can wrestling technique (standard references: "
           "Shannon J. Say Uncle! Catch-As-Catch-Can Wrestling. ECW Press; "
           "2005; Hackenschmidt G. The Way to Live: In Health and Physical "
           "Fitness. Athletic Publications; 1908; Burns M. Lessons in "
           "Wrestling and Physical Culture. Farmer Burns School of "
           "Wrestling; 1914; Robinson B, Gotch K. Catch-as-catch-can "
           "wrestling coaching lineage (Lancashire tradition through the "
           "20th century); United World Wrestling. International Wrestling "
           "Rules; USA Wrestling. Coaching materials: stance, ties, "
           "escapes, and pinning combinations). Civilian martial-arts "
           "instruction: trained with cooperative partners under qualified "
           "supervision, early taps, extra control on neck and leg "
           "attacks.")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature Combat "
                     "Method - the hook is the oath, the ride is the watch, "
                     "and the pin is the seal - clearly labeled "
                     "Signature-made.")

DBCFG = {}
DBCFG["combat-catch-wrestling"] = _cfg(
    "combat-catch-wrestling", "Catch Wrestling Combat Database",
    "Catch-as-catch-can wrestling - hooks, rides, submissions, pinning "
    "combinations: real, fact-checked technique knowledge, every record a "
    "technique with HOW TO DO IT step-by-step body mechanics, taught "
    "progressively along the ladder from foundations through compounded "
    "to advanced.",
    "combat technique record", "JAH-CBCW-", "JAH Catch Wrestling Combat Archivist",
    "catch wrestling combat archivist - hooks, rides, submissions, and "
    "pinning combinations of catch-as-catch-can wrestling, every record a "
    "technique with step-by-step body mechanics; teaching progressively "
    "along the ladder from foundations through compounded to advanced; "
    "answers from many angles - definition, example, analogy, application, "
    "history, math, how-to - using only archive data from this system",
    CIT_PUB, "public")
DBCFG["combat-catch-wrestling-signature"] = _cfg(
    "combat-catch-wrestling-signature", "Catch Wrestling Combat Signature Database",
    "His original Signature Combat Method: the hook is the oath, the ride "
    "is the watch, and the pin is the seal. The full ladder from stance "
    "and base through ties, takedowns, rides, and turns, through hooks, "
    "locks, and pinning combinations, to advanced chains and the full "
    "ride-hook-pin flow, reframed as Signature science. Clearly labeled "
    "Signature-made, never presented as authentic public record.",
    "combat technique record", "JAH-CBCWS-", "JAH Catch Wrestling Combat Archivist (Signature)",
    "catch wrestling combat archivist - Signature editions: his original "
    "Signature Combat Method, the hook the oath, the ride the watch, and "
    "the pin the seal, clearly labeled Signature-made and never presented "
    "as authentic public record; teaches progressively along the ladder "
    "from foundations through compounded to advanced; answers from many "
    "angles - definition, example, analogy, application, history, math, "
    "how-to - using only archive data from this system",
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


def node_check(path):
    p = subprocess.run(["node", "--check", path], capture_output=True,
                       text=True, timeout=60)
    assert p.returncode == 0, "node --check failed %s: %s" % (path, p.stderr[-800:])
    print("node --check OK: %s" % path, flush=True)


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
    for slug in ("combat-catch-wrestling", "combat-catch-wrestling-signature"):
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
        gen_path = os.path.join(ddir, "gen-%s.js" % slug)
        with open(gen_path, "w", encoding="utf-8") as f:
            f.write(gen_js)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)

    # node --check on extracted page scripts + gen-*.js (JS hygiene)
    for slug in built:
        ddir = os.path.join(REPO, "db", slug)
        ppath = os.path.join(ddir, "index.html")
        with open(ppath, "r", encoding="utf-8") as f:
            html = f.read()
        scripts = []
        for m in re.finditer(r"<script([^>]*)>(.*?)</script>",
                             html, flags=re.DOTALL | re.IGNORECASE):
            attrs, body = m.group(1), m.group(2)
            if re.search(r'\bsrc\s*=', attrs, flags=re.IGNORECASE):
                continue
            t = re.search(r'\btype\s*=\s*["\']?([^"\'\s>]+)', attrs,
                          flags=re.IGNORECASE)
            # only real JavaScript: no type, or an explicit JS type
            if t and t.group(1).lower() not in (
                    "text/javascript", "application/javascript", "module"):
                continue
            if body.strip():
                scripts.append(body)
        for i, body in enumerate(scripts):
            tmp = "/tmp/cw_check_%s_%d.js" % (slug.replace("-", "_"), i)
            with open(tmp, "w", encoding="utf-8") as f:
                f.write(body)
            node_check(tmp)
        assert scripts, "no JS script blocks found in %s" % ppath
        node_check(os.path.join(ddir, "gen-%s.js" % slug))

    # merger fragment (the merger owns manifest/api/restamp)
    os.makedirs(FRAG_DIR, exist_ok=True)
    frag = {
        "public": {
            "slug": "combat-catch-wrestling",
            "name": "Catch Wrestling Combat Database",
            "tagline": DBCFG["combat-catch-wrestling"]["tagline"],
            "record_kind": "combat technique record",
            "id_prefix": "JAH-CBCW-",
            "ai_name": "JAH Catch Wrestling Combat Archivist",
            "local_index": SHARD_BASE + "/data/combat-catch-wrestling/index.jsonl.gz",
            "record_count": 34, "status": "live", "full_records": 34,
            "index": SHARD_BASE + "/data/combat-catch-wrestling/index.jsonl.gz",
            "chunk_pattern": "data/combat-catch-wrestling/chunks/chunk-NNNN.jsonl.gz",
            "source": "public-harvest",
        },
        "signature": {
            "slug": "combat-catch-wrestling-signature",
            "name": "Catch Wrestling Combat Signature Database",
            "tagline": DBCFG["combat-catch-wrestling-signature"]["tagline"],
            "record_kind": "combat technique record",
            "id_prefix": "JAH-CBCWS-",
            "ai_name": "JAH Catch Wrestling Combat Archivist (Signature)",
            "local_index": SHARD_BASE + "/data/combat-catch-wrestling-signature/index.jsonl.gz",
            "record_count": 34, "status": "live", "full_records": 34,
            "index": SHARD_BASE + "/data/combat-catch-wrestling-signature/index.jsonl.gz",
            "chunk_pattern": "data/combat-catch-wrestling-signature/chunks/chunk-NNNN.jsonl.gz",
            "source": "signature",
        },
    }
    with open(os.path.join(FRAG_DIR, "combat-catch-wrestling.json"), "w",
              encoding="utf-8") as f:
        json.dump(frag, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print("fragment: %s/combat-catch-wrestling.json" % FRAG_DIR)
    print("NEXT: merger handles data/manifest.json, api.json, restamp, commit + push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
