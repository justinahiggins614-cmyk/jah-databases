#!/usr/bin/env python3
"""Build the Vale Tudo Combat databases for JAH Databases
(combat batch 3, 2026-10-17).

Verified 2026-10-17 (combat batch 3): RAW SWEEP over the full manifest
(2,442 databases) PLUS the whole-system dedupe exact shards
(data/dedupe/exact): zero 'vale-tudo' / 'vale tudo' slug or title
collisions - all 68 titles (34 public + 34 Signature Edition) checked one
by one against the whole system with zero refusals. Near-hits reviewed by
name/purpose/record schema/capabilities: the MMA database teaches modern
unified-rules mixed martial arts as general technique; the Brazilian
jiu-jitsu database teaches gi/no-gi grappling; the wrestling database
teaches takedowns and control. None teaches the Brazilian vale tudo
lineage itself - the anything-goes challenge-fighting roots, the
Portuguese technique names, the old-rules heritage, the challenge-match
history - as its subject. BUILD NEW is the verdict.

So this build creates two NEW databases, 34 ladder-ordered records each:

  combat-vale-tudo             - Vale Tudo Combat Database
                                 (public-harvest: real, fact-checked
                                 Brazilian vale tudo - the anything-goes
                                 challenge-fighting roots of modern MMA -
                                 every record a technique with HOW TO DO IT
                                 in step-by-step body mechanics, ladder-
                                 ordered from stance and breakfalls through
                                 strikes, clinch, takedowns, ground control
                                 and submissions to heritage, combinations,
                                 strategy, and the code of the art;
                                 civilian sport-training scope; standard
                                 references Snowden Total MMA 2008; Krauss
                                 Brawl 2004; Gentry No Holds Barred 2002;
                                 Gracie and Gracie Brazilian Jiu-Jitsu:
                                 Theory and Technique 2001; Penn Mixed
                                 Martial Arts: The Book of Knowledge 2007)
  combat-vale-tudo-signature  - Vale Tudo Combat Signature Database
                                 (his original Signature Combat Method:
                                 every technique a covenant of discipline,
                                 the fighter the armory of the Signature
                                 system, training the oath between student
                                 and craft, defense the honor guard, and
                                 fight craft the strategy of the Signature
                                 mind; src signature, titles suffixed
                                 " (Signature Edition)", never presented
                                 as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-CBVT- (public) and JAH-CBVTS- (signature), verified free
in the manifest id_prefix values and in every shard index of
jah-databases-data-1 (zero hits for JAH-CBVT anywhere).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_combat_vale_tudo.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos before the merge.

CONCURRENCY: this build never touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and never commits or pushes.
It writes only db/combat-vale-tudo[/-signature]/, code/combat-vale-tudo-
build/, the data-1 shard dirs, and the merger fragment. The merger handles
manifest/api/restamp/commit.

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
FRAGMENT = "/home/hatch/workspace/hidden_files/missing-builds/fragments/combat-vale-tudo.json"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_combat_vale_tudo import ENTRIES, SIG_TAIL
from demos_combat_vale_tudo import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Combat "
                "Method: every technique a covenant of discipline, the "
                "fighter the armory of the Signature system, training the "
                "oath between student and craft, defense the honor guard, "
                "and fight craft the strategy of the Signature mind. "
                "Clearly labeled Signature-made, never presented as "
                "authentic public record.")
    pub_line = ("Public records - real, fact-checked Brazilian vale tudo: "
                "the anything-goes challenge-fighting roots of modern MMA "
                "- stance, footwork, breakfalls, punches, low kicks, "
                "elbows, knees, the clinch, takedowns and takedown "
                "defense, guard play, passing, side control, mount, "
                "submissions, sweeps, heritage, combinations, strategy, "
                "and the code of the art - every record a technique with "
                "how to do it in step-by-step body mechanics, organized "
                "in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(what vale tudo is, the open stance, breakfalls, footwork, "
              "the jab, the cross, the lead hook, the low kick, the clinch "
              "tie, the sprawl, closed guard, the hip escape) -> Compounded "
              "(the uppercut, elbow strikes, knee strikes, the double leg "
              "takedown, the single leg takedown, the whizzer and takedown "
              "defense chains, pressure passing, side control and the "
              "crossface, mount control, the armbar, the rear naked choke, "
              "the guillotine) -> Advanced (the triangle choke, the "
              "kimura, sweeps, the flying knee, chaining submissions, "
              "bottom survival, heritage techniques and the old rules, "
              "combinations, fight strategy, the vale tudo code).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works "
                  "step by step, key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search vale tudo techniques, stance, footwork, breakfalls, jab, cross, hook, low kick, elbows, knees, clinch, sprawl, guard, takedowns, whizzer, submissions, sweeps, heritage, combinations...",
        "chat_ph": "Ask about vale tudo...",
        "archive_blurb": ("Seeded %s vale tudo combat records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled vale tudo combat studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about vale tudo - from what the art is through stance, breakfalls, footwork, punches, low kicks, elbows, knees, the clinch, the sprawl, guard play, and escapes, through takedowns, defense chains, passing, side control, mount, the armbar, the rear naked choke, and the guillotine, to the triangle, the kimura, sweeps, the flying knee, submission chains, survival, heritage, combinations, strategy, and the code." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "vale-tudo-study", "gen_demo_kind": "vale-tudo-demo",
        "source": source,
    }

CIT_PUB = ("Brazilian vale tudo - the anything-goes challenge-fighting "
           "roots of modern MMA (standard references: Snowden J. Total "
           "MMA: Inside Ultimate Fighting. ECW Press; 2008; Krauss E. "
           "Brawl: A Behind-the-Scenes Look at Mixed Martial Arts "
           "Competition. ECW Press; 2004; Gentry C. No Holds Barred: "
           "Ultimate Fighting and the Martial Arts Revolution. Milo "
           "Books; 2002; Gracie R, Gracie R. Brazilian Jiu-Jitsu: Theory "
           "and Technique. Invisible Cities Press; 2001; Penn BJ. Mixed "
           "Martial Arts: The Book of Knowledge. Victory Belt Publishing; "
           "2007). Civilian sport-training scope.")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature "
                     "Combat Method - every technique a covenant of "
                     "discipline, the fighter the armory of the Signature "
                     "system - clearly labeled Signature-made.")

DBCFG = {}
DBCFG["combat-vale-tudo"] = _cfg(
    "combat-vale-tudo", "Vale Tudo Combat Database",
    "Brazilian vale tudo - the anything-goes challenge-fighting roots of "
    "modern MMA - every record a technique with how to do it in step-by-"
    "step body mechanics, ladder-ordered from stance and breakfalls through "
    "strikes, clinch, takedowns, ground control, and submissions to "
    "heritage, combinations, strategy, and the code of the art.",
    "combat technique record", "JAH-CBVT-", "JAH Vale Tudo Combat Archivist",
    "vale tudo combat archivist - teaching Brazilian vale tudo, the "
    "anything-goes challenge-fighting roots of modern MMA, every record a "
    "technique with how to do it in step-by-step body mechanics; teaching "
    "progressively along the ladder from foundations through compounded to "
    "advanced; answers from many angles - definition, example, analogy, "
    "application, history, math, how-to - using only archive data from "
    "this system",
    CIT_PUB, "public")
DBCFG["combat-vale-tudo-signature"] = _cfg(
    "combat-vale-tudo-signature", "Vale Tudo Combat Signature Database",
    "His original Signature Combat Method: every technique a covenant of "
    "discipline, the fighter the armory of the Signature system, training "
    "the oath between student and craft, defense the honor guard, and "
    "fight craft the strategy of the Signature mind. The full ladder from "
    "what vale tudo is through stance, strikes, clinch, takedowns, ground "
    "control, and submissions to heritage, combinations, strategy, and "
    "the code, reframed as Signature science. Clearly labeled "
    "Signature-made, never presented as authentic public record.",
    "combat technique record", "JAH-CBVTS-", "JAH Vale Tudo Combat Archivist (Signature)",
    "vale tudo combat archivist - Signature editions: his original "
    "Signature Combat Method, every technique a covenant of discipline and "
    "the fighter the armory of the Signature system, clearly labeled "
    "Signature-made and never presented as authentic public record; teaches "
    "progressively along the ladder from foundations through compounded to "
    "advanced; answers from many angles - definition, example, analogy, "
    "application, history, math, how-to - using only archive data from "
    "this system",
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
    frag = {}
    for slug, recs in built.items():
        cfg = DBCFG[slug]
        source = "signature" if slug.endswith("-signature") else "public-harvest"
        key = "signature" if slug.endswith("-signature") else "public"
        frag[key] = {
            "slug": slug, "name": cfg["name"], "tagline": cfg["tagline"],
            "record_kind": cfg["record_kind"], "id_prefix": cfg["prefix"],
            "ai_name": cfg["ai"],
            "local_index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
            "record_count": len(recs), "status": "live", "full_records": len(recs),
            "index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
            "chunk_pattern": "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz",
            "source": source,
        }
    os.makedirs(os.path.dirname(FRAGMENT), exist_ok=True)
    with open(FRAGMENT, "w", encoding="utf-8") as f:
        json.dump(frag, f, indent=None, sort_keys=True, ensure_ascii=False)
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
    for slug in ("combat-vale-tudo", "combat-vale-tudo-signature"):
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
    print("manifest/api/index/README/docs untouched - merger handles those.")
    print("NEXT: merger verifies, then runs restamp + commit + push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
