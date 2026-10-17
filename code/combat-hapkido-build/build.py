#!/usr/bin/env python3
"""Build the Hapkido Combat databases for JAH Databases (combat batch 2).

Dedupe sweep 2026-10-17: DedupeGate over the whole system for all 68
candidate titles (34 public + 34 Signature editions) - zero collisions,
zero refusals. ID prefixes JAH-CBHAP- / JAH-CBHAPS- verified free in the
manifest id_prefix values and in every shard index file (zero hits).

Creates two NEW databases, 34 ladder-ordered records each:

  combat-hapkido               - Hapkido Combat Database (public-harvest:
                                  real, fact-checked Korean hapkido -
                                  joint locks, throws, kicks, pressure
                                  points, weapon defenses, and the
                                  circular-motion principles, each record
                                  carrying real Korean terminology with
                                  translations and step-by-step body
                                  mechanics; standard references Tedeschi
                                  M. Hapkido: Traditions, Philosophy,
                                  Technique. Weatherhill; 2000; Shaw S.
                                  Hapkido: Korean Art of Self-Defense.
                                  Tuttle; 1996; Kimm HY. Hapkido. H-Y
                                  Kimm; 2000; Kreighbaum E, Barthels KM.
                                  Biomechanics. Allyn and Bacon; 1996)
  combat-hapkido-signature     - Hapkido Combat Signature Database
                                  (his original Signature Hapkido Method:
                                  every technique a covenant of body and
                                  circle, the circle the shield, the lock
                                  the oath, defense the open hand; src
                                  signature, titles suffixed " (Signature
                                  Edition)", never presented as authentic
                                  public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written
in ladder order so pages present simple -> compounded -> complex.

Civilian training scope only. No website references. No Facebook.
Never the words "bat belt" anywhere.

NOTE: this build does NOT touch data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and does NOT commit or
push. A merger handles those. It writes: db/combat-hapkido/ and
db/combat-hapkido-signature/ (index.html + gen-*.js), the shard data
files under jah-databases-data-1, and the missing-builds fragment.
"""
import importlib.util
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = "/home/hatch/workspace/jah-databases"
SHARD_BASE = "https://justinahiggins614-cmyk.github.io/jah-databases-data-1"
TEMPLATE = os.path.join(REPO, "db", "public-synthetic-intelligence", "index.html")

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_combat_hapkido import ENTRIES, SIG_TAIL
from demos_combat_hapkido import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Hapkido "
                "Method: every technique a covenant of body and circle, "
                "the circle the shield, the lock the oath, defense the open "
                "hand. Clearly labeled Signature-made, never presented as "
                "authentic public record.")
    pub_line = ("Public records - real, fact-checked Korean hapkido: joint "
                "locks (sonmok kkokki, palkkumchi kkokki, eokkae kkokki), "
                "throws (eokkae mechi, heori mechi), kicks (ap chagi, "
                "dollyeo chagi, yeop chagi, dwi chagi), pressure points "
                "(gyeonghyeol chigi), weapon defenses (dando daebi, "
                "jangbong daebi, danbong sul, geom sul), and the "
                "circular-motion principles (wonui, yu) - every record "
                "carrying real Korean terminology with translations and "
                "step-by-step body mechanics, organized in the Signature "
                "system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(stances, breakfalls, footwork, punches, basic kicks, blocks, "
              "circular motion, breathing, softness, wrist escapes, basic "
              "wrist locks) -> Compounded (elbow locks, side kicks, finger "
              "locks, knife-hand strikes, shoulder locks, back kicks, leg "
              "sweeps, lapel grab defense, shoulder throws, hip throws, "
              "elbow strikes, knee strikes, leg hook takedowns, choke "
              "defense) -> Advanced (pressure point strikes, spinning "
              "kicks, jump kicks, knife defense, staff defense, short "
              "stick, sword basics, breaking).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search stances, breakfalls, joint locks, wrist locks, elbow locks, throws, kicks, front kick, roundhouse, side kick, pressure points, knife defense, staff defense, circular motion, nakbeop, kkokki, chagi...",
        "chat_ph": "Ask about hapkido techniques...",
        "archive_blurb": ("Seeded %s hapkido combat technique records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled hapkido technique studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about hapkido - from stances, breakfalls, footwork, punches, kicks, blocks, circular motion, breathing, softness, escapes, and wrist locks, through elbow locks, side kicks, finger locks, knife-hand strikes, shoulder locks, back kicks, sweeps, grab defenses, throws, elbow and knee strikes, takedowns, and choke defense, to pressure points, spinning and jump kicks, knife and staff defense, the short stick, the sword, and breaking." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "hapkido-technique-study", "gen_demo_kind": "hapkido-technique-demo",
        "source": source,
    }

CIT_PUB = ("Hapkido technique (standard references: Tedeschi M. Hapkido: "
           "Traditions, Philosophy, Technique. Weatherhill; 2000; Shaw S. "
           "Hapkido: Korean Art of Self-Defense. Tuttle; 1996; Kimm HY. "
           "Hapkido. H-Y Kimm; 2000; Kreighbaum E, Barthels KM. "
           "Biomechanics: A Qualitative Approach for Studying Human "
           "Movement. Allyn and Bacon; 1996).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature "
                     "Hapkido Method - every technique a covenant of body "
                     "and circle - clearly labeled Signature-made.")

DBCFG = {}
DBCFG["combat-hapkido"] = _cfg(
    "combat-hapkido", "Hapkido Combat Database",
    "Korean hapkido, taught step by step: real joint locks, throws, kicks, "
    "pressure points, and weapon defenses - every record carrying real "
    "Korean terminology with translations and step-by-step body mechanics, "
    "from the first stance through the circular-motion principles to "
    "advanced weapon work, taught progressively along the ladder.",
    "combat technique record", "JAH-CBHAP-", "JAH Hapkido Combat Archivist",
    "hapkido combat archivist - teaching Korean hapkido step by step: "
    "stances, breakfalls, footwork, strikes, kicks, blocks, the circular "
    "motion principles, joint locks, throws, takedowns, pressure points, "
    "and weapon defenses; teaching progressively along the ladder from "
    "foundations through compounded to advanced; answers from many angles "
    "- definition, example, analogy, application, history, math, how-to - "
    "using only archive data from this system",
    CIT_PUB, "public")
DBCFG["combat-hapkido-signature"] = _cfg(
    "combat-hapkido-signature", "Hapkido Combat Signature Database",
    "His original Signature Hapkido Method: every technique a covenant of "
    "body and circle, the circle the shield, the lock the oath, defense "
    "the open hand. The full ladder from stances and breakfalls through "
    "locks, throws, kicks, and takedowns to pressure points and weapon "
    "work, reframed as Signature science. Clearly labeled Signature-made, "
    "never presented as authentic public record.",
    "combat technique record", "JAH-CBHAPS-", "JAH Hapkido Combat Archivist (Signature)",
    "hapkido combat archivist - Signature editions: his original Signature "
    "Hapkido Method, every technique a covenant of body and circle, "
    "clearly labeled Signature-made and never presented as authentic "
    "public record; teaches progressively along the ladder from "
    "foundations through compounded to advanced; answers from many angles "
    "- definition, example, analogy, application, history, math, how-to - "
    "using only archive data from this system",
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


def write_fragment(built):
    frag = {
        "public": {
            "slug": "combat-hapkido",
            "name": "Hapkido Combat Database",
            "tagline": DBCFG["combat-hapkido"]["tagline"],
            "record_kind": "combat technique record",
            "id_prefix": "JAH-CBHAP-",
            "ai_name": "JAH Hapkido Combat Archivist",
            "local_index": SHARD_BASE + "/data/combat-hapkido/index.jsonl.gz",
            "record_count": len(built["combat-hapkido"]),
            "status": "live",
            "full_records": len(built["combat-hapkido"]),
            "index": SHARD_BASE + "/data/combat-hapkido/index.jsonl.gz",
            "chunk_pattern": "data/combat-hapkido/chunks/chunk-NNNN.jsonl.gz",
            "source": "public-harvest",
        },
        "signature": {
            "slug": "combat-hapkido-signature",
            "name": "Hapkido Combat Signature Database",
            "tagline": DBCFG["combat-hapkido-signature"]["tagline"],
            "record_kind": "combat technique record",
            "id_prefix": "JAH-CBHAPS-",
            "ai_name": "JAH Hapkido Combat Archivist (Signature)",
            "local_index": SHARD_BASE + "/data/combat-hapkido-signature/index.jsonl.gz",
            "record_count": len(built["combat-hapkido-signature"]),
            "status": "live",
            "full_records": len(built["combat-hapkido-signature"]),
            "index": SHARD_BASE + "/data/combat-hapkido-signature/index.jsonl.gz",
            "chunk_pattern": "data/combat-hapkido-signature/chunks/chunk-NNNN.jsonl.gz",
            "source": "signature",
        },
    }
    path = "/home/hatch/workspace/hidden_files/missing-builds/fragments/combat-hapkido.json"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(frag, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print("fragment: %s" % path, flush=True)


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
    for slug in ("combat-hapkido", "combat-hapkido-signature"):
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

    write_fragment(built)
    print("manifest/api/index.html untouched; merger handles them. No commit, no push.")
    print("DONE: 68 records (34 public + 34 signature).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
