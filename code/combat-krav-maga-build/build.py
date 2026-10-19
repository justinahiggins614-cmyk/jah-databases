#!/usr/bin/env python3
"""Build the Krav Maga Combat databases for JAH Databases (combat batch 2).

See entries_combat_krav_maga.py for the verification record.
Builds two databases, 34 ladder-ordered records each:

  combat-krav-maga              - Krav Maga Combat Database
  combat-krav-maga-signature    - Krav Maga Combat Signature Database

ID prefixes: JAH-CBKM- (public) and JAH-CBKMS- (signature), verified free
in the manifest id_prefix values and zero hits in every shard index file.

This build does NOT touch data/manifest.json, api.json, index.html,
README.md, or docs/AI_ACCESS.md, and never commits or pushes - a merger
handles those. It only creates: db/<slug>/{index.html,gen-<slug>.js},
the shard files under jah-databases-data-1, and the merger fragment.

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

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_combat_krav_maga import ENTRIES, SIG_TAIL
from demos_combat_krav_maga import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Combat Method: "
                "every defense a covenant of the body, the burst the oath of "
                "forward motion, retzev the signature written in continuous "
                "combat. Clearly labeled Signature-made, never presented as "
                "authentic public record.")
    pub_line = ("Public records - real, fact-checked krav maga: the Israeli "
                "self-defense system - simultaneous defense and attack, "
                "defenses against grabs, chokes, and weapon threats, "
                "striking, and ground survival - every record carrying "
                "step-by-step how-to body mechanics, organized in the "
                "Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(fighting stance, footwork and movement, punch combatives, "
              "palm-heel strike, elbow strikes, knee strikes, front kick to "
              "the groin, hammerfist strike) -> Compounded (inside defense "
              "against a straight punch, wrist grab defense, 360-degree "
              "outside defense, front choke pluck, side headlock escape, "
              "shirt grab defense, bear hug defenses arms free and arms "
              "pinned, hair grab defense, rear choke defense, ground "
              "survival and the technical stand-up, kicking from the ground, "
              "clinch fighting, bursting) -> Advanced (retzev continuous "
              "combat motion, knife threats on the live side and dead side, "
              "stick attack defense, slashing knife defense, overhead stab "
              "defense, handgun threats from the front and behind, multiple "
              "attacker defense, long gun threat defense, third-party "
              "protection, stress drills and scenario training).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search fighting stance, footwork, punches, palm-heel, elbows, knees, groin kick, hammerfist, inside defense, 360 defense, wrist grabs, chokes, headlocks, bear hugs, ground survival, clinch, bursting, retzev, knife defenses, stick defense, handgun defenses, multiple attackers...",
        "chat_ph": "Ask about krav maga technique...",
        "archive_blurb": ("Seeded %s krav maga combat records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled krav maga technique studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about krav maga - from the fighting stance, footwork, punches, palm-heel strikes, elbows, knees, the front kick to the groin, and the hammerfist, through inside defense, the 360 defense, wrist grab releases, the front choke pluck, headlocks, shirt grabs, bear hugs, hair grabs, rear chokes, ground survival, kicking from the ground, the clinch, and bursting, to retzev, knife threats, stick attacks, handgun and long gun threats, multiple attackers, third-party protection, and stress drills." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "krav-maga-study", "gen_demo_kind": "krav-maga-demo",
        "source": source,
    }

CIT_PUB = ("Krav maga technique (standard references: Levine D, Whitman J. "
           "Complete Krav Maga: The Ultimate Guide to Over 230 Self-Defense "
           "and Combative Techniques. Ulysses Press; 2007; Kahn D. Krav "
           "Maga: An Essential Guide to the Renowned Method - for Fitness "
           "and Self-Defense. St. Martin's Griffin; 2004; Krav Maga "
           "Worldwide. Official Krav Maga Curriculum: Yellow through Black "
           "Belt. Los Angeles, California; International Krav Maga "
           "Federation. Krav Maga Grading Syllabus: Practitioner through "
           "Expert Levels; Federation Europeenne de Krav-Maga. Official "
           "Krav Maga Program and Grading System; Lichtenfeld I, founder of "
           "krav maga, 1940s-1960s).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature Combat "
                     "Method - every defense a covenant of the body, the "
                     "burst the oath of forward motion, retzev the signature "
                     "written in continuous combat - clearly labeled "
                     "Signature-made.")

DBCFG = {}
DBCFG["combat-krav-maga"] = _cfg(
    "combat-krav-maga", "Krav Maga Combat Database",
    "Simultaneous defense and attack, defenses against grabs, chokes, and "
    "weapon threats, striking, and ground survival: real, fact-checked "
    "Israeli krav maga taught step by step from the fighting stance to "
    "advanced defenses along the teaching ladder.",
    "combat technique record", "JAH-CBKM-", "JAH Krav Maga Combat Archivist",
    "krav maga combat archivist - simultaneous defense and attack, defenses "
    "against grabs, chokes, and weapon threats, striking, and ground "
    "survival with step-by-step how-to body mechanics; teaching "
    "progressively along the ladder from foundations through compounded to "
    "advanced; answers from many angles - definition, example, analogy, "
    "application, history, math, how-to - using only archive data from this "
    "system",
    CIT_PUB, "public")
DBCFG["combat-krav-maga-signature"] = _cfg(
    "combat-krav-maga-signature", "Krav Maga Combat Signature Database",
    "His original Signature Combat Method: every defense a covenant of the "
    "body, the burst the oath of forward motion, retzev the signature "
    "written in continuous combat. The full ladder from stance and "
    "combatives through grabs, chokes, and ground survival to weapon "
    "threats, multiple attackers, and stress drills, reframed as Signature "
    "science. Clearly labeled Signature-made, never presented as authentic "
    "public record.",
    "combat technique record", "JAH-CBKMS-", "JAH Krav Maga Combat Archivist (Signature)",
    "krav maga combat archivist - Signature editions: his original "
    "Signature Combat Method, every defense a covenant of the body and "
    "retzev the signature written in continuous combat, clearly labeled "
    "Signature-made and never presented as authentic public record; teaches "
    "progressively along the ladder from foundations through compounded to "
    "advanced; answers from many angles - definition, example, analogy, "
    "application, history, math, how-to - using only archive data from this "
    "system",
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
    frag = {"public": {}, "signature": {}}
    for slug, recs in built.items():
        sig = slug.endswith("-signature")
        cfg = DBCFG[slug]
        entry = {
            "slug": slug, "name": cfg["name"], "tagline": cfg["tagline"],
            "record_kind": cfg["record_kind"], "id_prefix": cfg["prefix"],
            "ai_name": cfg["ai"],
            "local_index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
            "record_count": len(recs), "status": "live", "full_records": len(recs),
            "index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
            "chunk_pattern": "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz",
            "source": cfg["source"],
        }
        frag["signature" if sig else "public"] = entry
    p = "/home/hatch/workspace/hidden_files/missing-builds/fragments/combat-krav-maga.json"
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        json.dump(frag, f, indent=1, ensure_ascii=False)
        f.write("\n")
    print("fragment: %s" % p, flush=True)


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
    for slug in ("combat-krav-maga", "combat-krav-maga-signature"):
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

    write_fragment(built)
    print("manifest/api.json untouched (merger handles those).")
    print("DONE: 2 databases, %d records total. No commit, no push." % total)
    return 0


if __name__ == "__main__":
    sys.exit(main())
