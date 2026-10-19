#!/usr/bin/env python3
"""Build the Muay Boran Combat databases for JAH Databases
(combat batch 3, 2026-10-17).

Scope verified before authoring 2026-10-17: RAW check over the full manifest
(2,442 databases) plus every shard index in jah-databases-data-1: zero
'combat-muay-boran*' slugs/names; zero Muay Boran combat technique catalog
databases of this kind. The sibling 'combat-muay-thai' (JAH-CBMT-) covers
modern ring Muay Thai; this build covers Muay Boran proper - the ancient
Thai battlefield boxing, predecessor of Muay Thai, organized around the
nine weapons (naw arwut). Distinct capability - BUILD NEW is the verdict.
Dedupe gate check of all 68 planned titles (34 public + 34 Signature) vs
the whole exact index: zero collisions, zero refusals. ID prefixes
JAH-CBMB- and JAH-CBMBS- verified free in the manifest id_prefix values
and every shard index file (zero hits).

So this build creates two NEW databases, 34 ladder-ordered records each:

  combat-muay-boran               - Muay Boran Combat Database
                                    (public-harvest: real, fact-checked
                                    Muay Boran knowledge - the ancient Thai
                                    battlefield boxing: the nine weapons
                                    (naw arwut), the five regional styles,
                                    wai khru ram muay, mongkon and prajioud,
                                    card chuek hemp wraps, stance footwork
                                    and guard, the four limb strikes plus
                                    the head as ninth weapon, clinch sweeps
                                    throws and grappling, the mae mai
                                    master tricks and luk mai complementary
                                    tricks - every record carrying the Thai
                                    name with translation, step-by-step
                                    body mechanics, key points,
                                    requirements, standards, and citations;
                                    standard references Kraitus P, Kraitus
                                    P. Muay Thai: The Most Distinguished
                                    Art of Fighting 1988; Delp C. Muay Thai
                                    Basics 2004; traditional Muay Boran
                                    teaching lineage)
  combat-muay-boran-signature     - Muay Boran Combat Signature Database
                                    (his original Signature Nine-Weapons
                                    Method: every weapon a covenant of
                                    mechanics, the stance the oath of the
                                    feet, footwork the geometry of the
                                    triangle, the guard the walls of the
                                    temple, the wai khru the oath before
                                    the storm; src signature, titles
                                    suffixed " (Signature Edition)", never
                                    presented as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-CBMB- (public) and JAH-CBMBS- (signature), verified free
in the manifest and in every shard index (zero hits).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_combat_muay_boran.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos (34 x 2 editions).

CONCURRENCY: this builder never touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and never commits or pushes.
A merger handles manifest/api/restamp. This script writes only:
db/combat-muay-boran[-signature]/, the shard data dirs, its own code dir,
and the merger fragment.

Never the words "bat belt" anywhere. No website references. No Facebook.
Civilian martial-arts sport instruction only. Nothing on neutralizing or
defeating military or defense-grade systems.
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
FRAGMENT = "/home/hatch/workspace/hidden_files/missing-builds/fragments/combat-muay-boran.json"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_combat_muay_boran import ENTRIES, SIG_TAIL
from demos_combat_muay_boran import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, source):
    sig_line = ("Signature originals - his original Signature Nine-Weapons "
                "Method: every weapon a covenant of mechanics, the stance "
                "the oath of the feet, footwork the geometry of the "
                "triangle, the guard the walls of the temple, and the wai "
                "khru the oath before the storm. Clearly labeled "
                "Signature-made, never presented as authentic public "
                "record.")
    pub_line = ("Public records - real, fact-checked Muay Boran knowledge: "
                "the ancient Thai battlefield boxing that preceded modern "
                "Muay Thai - the nine weapons (naw arwut), the five "
                "regional styles (Muay Thasao, Muay Lopburi, Muay Chaiya, "
                "Muay Korat, Muay Uttaradit), the wai khru ram muay rite, "
                "mongkon and prajioud, card chuek hemp wraps, stance "
                "footwork and guard, the four limb strikes plus the head "
                "as ninth weapon, clinch sweeps throws and grappling, and "
                "the mae mai master tricks with luk mai complementary "
                "tricks - every record carrying the Thai name with "
                "translation and step-by-step body mechanics, organized in "
                "the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(fighting stance, footwork, the nine weapons, wai khru ram "
              "muay, mongkon and prajioud, card chuek wraps, the long "
              "guard, body conditioning, triangular stepping, forms "
              "practice, the five regional styles) -> Compounded "
              "(straight punch, hook, uppercut, horizontal and upward "
              "elbows, straight and curved knees, low cutting kick, "
              "diagonal roundhouse, front push kick, clinch entry and "
              "control, sweeps, the ninth weapon headbutt) -> Advanced "
              "(mae mai master tricks, luk mai complementary tricks, "
              "spinning back elbow, Hanuman Tawai Waen, Kwang Liow Lang, "
              "hap liuk grappling, clinch throws, flying knee, "
              "combination systems, the kru teaching lineage).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search stance, footwork, nine weapons, wai khru, mongkon, card chuek, punches, elbows, knees, kicks, clinch, sweeps, mae mai, luk mai, regional styles...",
        "chat_ph": "Ask about Muay Boran techniques...",
        "archive_blurb": ("Seeded %s Muay Boran combat technique records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled Muay Boran combat technique studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about Muay Boran - from the fighting stance, footwork, the nine weapons, wai khru, mongkon and prajioud, card chuek, guard, conditioning, triangular stepping, forms, and the five regional styles, through punches, elbows, knees, kicks, clinch, sweeps, and the ninth weapon, to the mae mai master tricks, luk mai, spinning elbow, Hanuman Tawai Waen, the deer looks back, grappling, throws, flying knee, combinations, and the kru lineage." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "muay-boran-study", "gen_demo_kind": "muay-boran-demo",
        "source": source,
    }

DBCFG = {}
DBCFG["combat-muay-boran"] = _cfg(
    "combat-muay-boran", "Muay Boran Combat Database",
    "Ancient Thai battlefield boxing: the nine weapons of Muay Boran, every "
    "technique taught step by step from the fighting stance through the "
    "compounded weapons to the advanced master tricks.",
    "combat technique record", "JAH-CBMB-", "JAH Muay Boran Combat Archivist",
    "Muay Boran combat archivist - teaching the ancient Thai battlefield "
    "boxing: the nine weapons, the regional styles, the wai khru rite, the "
    "strikes of all four limbs plus the head, clinch and throws, and the "
    "mae mai and luk mai classical systems; teaching progressively along "
    "the ladder from foundations through compounded to advanced; answers "
    "from many angles - definition, example, analogy, application, "
    "history, math, how-to - using only archive data from this system",
    "public")
DBCFG["combat-muay-boran-signature"] = _cfg(
    "combat-muay-boran-signature", "Muay Boran Combat Signature Database",
    "His original Signature Nine-Weapons Method: every weapon a covenant "
    "of mechanics, the stance the oath of the feet, footwork the geometry "
    "of the triangle, the guard the walls of the temple, the wai khru the "
    "oath before the storm. The full ladder from stance and the nine "
    "weapons through the compounded strikes to the mae mai, luk mai, and "
    "the kru lineage, reframed as Signature science. Clearly labeled "
    "Signature-made, never presented as authentic public record.",
    "combat technique record", "JAH-CBMBS-", "JAH Muay Boran Combat Archivist (Signature)",
    "Muay Boran combat archivist - Signature editions: his original "
    "Signature Nine-Weapons Method, every weapon a covenant of mechanics "
    "and the wai khru the oath before the storm, clearly labeled "
    "Signature-made and never presented as authentic public record; "
    "teaches progressively along the ladder from foundations through "
    "compounded to advanced; answers from many angles - definition, "
    "example, analogy, application, history, math, how-to - using only "
    "archive data from this system",
    "signature")

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
        sig = slug.endswith("-signature")
        key = "signature" if sig else "public"
        idx = SHARD_BASE + "/data/" + slug + "/index.jsonl.gz"
        frag[key] = {
            "slug": slug,
            "name": cfg["name"],
            "tagline": cfg["tagline"],
            "record_kind": cfg["record_kind"],
            "id_prefix": cfg["prefix"],
            "ai_name": cfg["ai"],
            "local_index": idx,
            "record_count": len(recs),
            "status": "live",
            "full_records": len(recs),
            "index": idx,
            "chunk_pattern": "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz",
            "source": "signature" if sig else "public-harvest",
        }
    os.makedirs(os.path.dirname(FRAGMENT), exist_ok=True)
    with open(FRAGMENT, "w", encoding="utf-8") as f:
        json.dump(frag, f, indent=2, ensure_ascii=False)
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
    for slug in ("combat-muay-boran", "combat-muay-boran-signature"):
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
    print("manifest/api.json untouched (merger handles those). No commit, no push.")
    print("built: 2 databases, %d records total" % total)
    return 0


if __name__ == "__main__":
    sys.exit(main())
