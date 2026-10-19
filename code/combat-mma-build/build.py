#!/usr/bin/env python3
"""Build the Mixed Martial Arts Combat databases for JAH Databases
(combat batch 2).

Verified 2026-10-17: RAW SWEEP over the full manifest (2,410 databases)
PLUS every shard index title in jah-databases-data-1 (zero hits for the
CBMMA id prefixes): zero 'combat-mma*' slugs/names; zero title collisions
for all 68 candidate titles (34 public + 34 Signature Edition) against the
whole-system exact dedupe gate. The 'summarization-pairs' slug is a
substring false positive ('mma' inside 'summarization'), not a combat
database. No existing boxing/fighting/wrestling database carries these
titles - BUILD NEW is the verdict.

So this build creates two NEW databases, 34 ladder-ordered records each:

  combat-mma              - Mixed Martial Arts Combat Database
                            (public-harvest: real, fact-checked MMA
                            knowledge - stance, footwork, striking,
                            defense, takedowns, ground survival,
                            combinations, clinch, submissions,
                            ground-and-pound, guard passing, takedown
                            defense, cage wrestling, submission defense,
                            transitions, feints, elbows, sweeps, escapes,
                            fight planning - every record carrying the
                            full technique: description, how to do it
                            (step-by-step body mechanics), key points,
                            requirements, standards, citations, and a
                            working demonstration program)
  combat-mma-signature    - Mixed Martial Arts Combat Signature Database
                            (his original Signature Combat Method: the
                            stance as sworn ground, the strike as a
                            signature struck in motion, wrestling as the
                            handshake of bodies, submissions as the sealed
                            agreement; src signature, titles suffixed
                            " (Signature Edition)", never presented as
                            authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-CBMMA- (public) and JAH-CBMMAS- (signature), verified free
in the manifest id_prefix values and in every shard index file (zero hits).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_combat_mma.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos before writing
pages.

MERGER NOTE: this build does NOT touch data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and does NOT git commit or
push. It writes the fragment
~/workspace/hidden_files/missing-builds/fragments/combat-mma.json for the
merger to consume.

Never the words "bat belt" anywhere. No website references. No Facebook.
Civilian martial-arts instruction only.
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
FRAGMENT = "/home/hatch/workspace/hidden_files/missing-builds/fragments/combat-mma.json"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_combat_mma import ENTRIES, SIG_TAIL
from demos_combat_mma import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Combat Method: "
                "the stance as sworn ground, the strike as a signature "
                "struck in motion, wrestling as the handshake of bodies, "
                "and submissions as the sealed agreement. Clearly labeled "
                "Signature-made, never presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked mixed martial arts "
                "knowledge: stance and footwork, punches, kicks, head "
                "movement, blocking, takedowns, takedown defense, ground "
                "survival, combinations, the clinch, submissions, ground "
                "and pound, guard passing, cage wrestling, submission "
                "defense, transitions, feints, elbows, sweeps, escapes, "
                "and fight planning - every record carrying the full "
                "technique with step-by-step body mechanics, organized in "
                "the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(the MMA stance, footwork and cage angles, the jab, the "
              "cross, the lead hook, the rear uppercut, the low kick, "
              "head movement and evasion, blocking and parrying, the "
              "double leg takedown, the sprawl, the hip escape, the bridge "
              "and roll escape) -> Compounded (striking combinations, "
              "checking leg kicks, the single leg takedown, the clinch, "
              "the Thai clinch and knees, the guillotine choke, the rear "
              "naked choke, the armbar from mount, ground and pound "
              "fundamentals, guard passing, takedown defense, cage "
              "wrestling, submission defense) -> Advanced (submission "
              "chains and transitions, feints and striking setups, elbows "
              "and close range striking, sweeps and reversals, escaping "
              "side control, the triangle choke, cage takedowns and trips, "
              "fight game planning).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how to do it "
                  "(step-by-step body mechanics), key points, requirements, "
                  "standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search stance, footwork, jab, cross, hook, uppercut, low kick, sprawl, double leg, single leg, clinch, guillotine, rear naked choke, armbar, triangle, guard passing, takedown defense, cage wrestling, submissions, sweeps, escapes, game planning...",
        "chat_ph": "Ask about mixed martial arts technique...",
        "archive_blurb": ("Seeded %s mixed martial arts combat records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled mixed martial arts technique studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about mixed martial arts - from stance and footwork through the jab, cross, hook, uppercut, and low kick, head movement, blocking, the double leg, the sprawl, the hip escape, and the bridge and roll, through combinations, checking kicks, the single leg, the clinch, knees, the guillotine, the rear naked choke, the armbar, ground and pound, guard passing, takedown defense, cage wrestling, and submission defense, to submission chains, feints, elbows, sweeps, escapes, the triangle, cage takedowns, and fight planning." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "mma-technique-study", "gen_demo_kind": "mma-technique-demo",
        "source": source,
    }

CIT_PUB = ("Mixed martial arts technique (standard references: Dempsey J. "
           "Championship Fighting: Explosive Punching and Aggressive "
           "Defense. 1950; Gracie R, Gracie R. Brazilian Jiu-Jitsu: Theory "
           "and Technique. Invisible Cities Press; 2001; Gracie H. Gracie "
           "Jiu-Jitsu Basics instructional series; Kodokan. Kodokan Judo: "
           "Throwing Techniques. Kodansha; 2014; Sheridan S. The "
           "Fighters Mind: Inside the Mental Game. Grove Press; 2010; "
           "Danaher J. Enter the System instructional series; Association "
           "of Boxing Commissions. Unified Rules of Mixed Martial Arts).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature "
                     "Combat Method - the stance as sworn ground, the "
                     "strike as a signature struck in motion - clearly "
                     "labeled Signature-made.")

DBCFG = {}
DBCFG["combat-mma"] = _cfg(
    "combat-mma", "Mixed Martial Arts Combat Database",
    "Mixed martial arts, taught as a ladder: real, fact-checked technique "
    "from the stance and footwork through striking, takedowns, and ground "
    "survival, through the clinch, submissions, and ground and pound, to "
    "transitions, cage craft, and fight planning - every record carrying "
    "step-by-step body mechanics.",
    "combat technique record", "JAH-CBMMA-", "JAH Mixed Martial Arts Combat Archivist",
    "mixed martial arts combat archivist - teaching MMA technique "
    "progressively along the ladder from stance and footwork through "
    "striking, takedowns, and ground survival, through the clinch, "
    "submissions, and ground and pound, to transitions, cage craft, and "
    "fight planning; answers from many angles - definition, example, "
    "analogy, application, history, math, how-to - using only archive data "
    "from this system",
    CIT_PUB, "public")
DBCFG["combat-mma-signature"] = _cfg(
    "combat-mma-signature", "Mixed Martial Arts Combat Signature Database",
    "His original Signature Combat Method: the stance as sworn ground, "
    "the strike as a signature struck in motion, wrestling as the "
    "handshake of bodies, submissions as the sealed agreement. The full "
    "ladder from stance and footwork through striking, takedowns, and "
    "ground survival, through the clinch, submissions, and ground and "
    "pound, to transitions, cage craft, and fight planning, reframed as "
    "Signature science. Clearly labeled Signature-made, never presented "
    "as authentic public record.",
    "combat technique record", "JAH-CBMMAS-", "JAH Mixed Martial Arts Combat Archivist (Signature)",
    "mixed martial arts combat archivist - Signature editions: his original "
    "Signature Combat Method, the stance as sworn ground and the strike as "
    "a signature struck in motion, clearly labeled Signature-made and "
    "never presented as authentic public record; teaches progressively "
    "along the ladder from foundations through compounded to advanced; "
    "answers from many angles - definition, example, analogy, application, "
    "history, math, how-to - using only archive data from this system",
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
    pub = {
        "slug": "combat-mma",
        "name": "Mixed Martial Arts Combat Database",
        "tagline": DBCFG["combat-mma"]["tagline"],
        "record_kind": "combat technique record",
        "id_prefix": "JAH-CBMMA-",
        "ai_name": "JAH Mixed Martial Arts Combat Archivist",
        "local_index": SHARD_BASE + "/data/combat-mma/index.jsonl.gz",
        "record_count": 34, "status": "live", "full_records": 34,
        "index": SHARD_BASE + "/data/combat-mma/index.jsonl.gz",
        "chunk_pattern": "data/combat-mma/chunks/chunk-NNNN.jsonl.gz",
        "source": "public-harvest",
    }
    sig = {
        "slug": "combat-mma-signature",
        "name": "Mixed Martial Arts Combat Signature Database",
        "tagline": DBCFG["combat-mma-signature"]["tagline"],
        "record_kind": "combat technique record",
        "id_prefix": "JAH-CBMMAS-",
        "ai_name": "JAH Mixed Martial Arts Combat Archivist (Signature)",
        "local_index": SHARD_BASE + "/data/combat-mma-signature/index.jsonl.gz",
        "record_count": 34, "status": "live", "full_records": 34,
        "index": SHARD_BASE + "/data/combat-mma-signature/index.jsonl.gz",
        "chunk_pattern": "data/combat-mma-signature/chunks/chunk-NNNN.jsonl.gz",
        "source": "signature",
    }
    os.makedirs(os.path.dirname(FRAGMENT), exist_ok=True)
    with open(FRAGMENT, "w", encoding="utf-8") as f:
        json.dump({"public": pub, "signature": sig}, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print("fragment: %s" % FRAGMENT, flush=True)


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
    for slug in ("combat-mma", "combat-mma-signature"):
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

    # cross-check: entry how_it_works key claims vs demo printed outputs
    for slug, recs in built.items():
        for r in recs:
            prog = r["demo"]["program"]
            p = subprocess.run([sys.executable, "-c", prog],
                               capture_output=True, text=True, timeout=60)
            out = p.stdout
            assert r["id"] in out or r["t"][:20] in out, "demo output not tied to record %s" % r["id"]
    print("cross-check: all %d demo outputs tied to their records" % total, flush=True)

    write_fragment(built)

    # node --check on extracted page scripts and gen files
    import re as _re
    for slug in built:
        ppath = os.path.join(REPO, "db", slug, "index.html")
        html = open(ppath, encoding="utf-8").read()
        scripts = _re.findall(r"<script>(.*?)</script>", html, flags=_re.S)
        for i, s in enumerate(scripts):
            if "var SLUG" in s or "JAHDB" in s:
                with open("/tmp/cmma-check-%s-%d.js" % (slug, i), "w") as f:
                    f.write(s)
                p = subprocess.run(["node", "--check", "/tmp/cmma-check-%s-%d.js" % (slug, i)],
                                   capture_output=True, text=True)
                assert p.returncode == 0, "node --check failed page %s script %d: %s" % (slug, i, p.stderr[:500])
        for gf in ("gen-%s.js" % slug,):
            gp = os.path.join(REPO, "db", slug, gf)
            p = subprocess.run(["node", "--check", gp], capture_output=True, text=True)
            assert p.returncode == 0, "node --check failed %s: %s" % (gp, p.stderr[:500])
    print("node --check: page scripts and gen files clean", flush=True)

    print("DONE: 68 records, 68 demos OK, pages + shards + fragment written.")
    print("MERGER: manifest/api.json/index.html/README/docs NOT touched; no commit, no push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
