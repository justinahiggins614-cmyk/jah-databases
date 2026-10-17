#!/usr/bin/env python3
"""Build the Shapes Basics databases for JAH Databases (fundamentals #9).

Replicates code/component-parts-catalog-build/build.py exactly for page
structure and pipeline, EXCEPT: this builder never touches
data/manifest.json, api.json, index.html, README.md, or docs/AI_ACCESS.md
(a merger handles those), and never git commits or pushes.

Verified 2026-10-17 (fundamentals order #9): roster check - zero
'shapes-basics*' slugs and zero 'shapes basics' database names in the
manifest; zero 'shapes basics' title collisions across all
jah-databases-data-1 shard indexes; ID prefixes JAH-SHPB- (public) and
JAH-SHPBS- (signature) verified free in the manifest id_prefix values
AND in all 812 shard data dirs.

Two NEW databases, 34 ladder-ordered records each:

  shapes-basics            - The Shapes Basics Database
                             (public-harvest: real, fact-checked
                             foundational geometry - 2D shapes (circle,
                             triangle, square, rectangle, polygons) and
                             3D shapes (cube, sphere, cylinder, cone,
                             pyramid); names, properties,
                             sides/vertices/faces, real-world examples,
                             introduction to symmetry)
  shapes-basics-signature  - The Shapes Basics Signature Database
                             (his original Signature Geometry: every shape
                             a covenant of form, the circle the oath of
                             return, the triangle the threefold witness;
                             src signature, titles suffixed " (Signature
                             Edition)", never presented as authentic public
                             record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_shapes_basics.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos before writing.

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

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_shapes_basics import ENTRIES, SIG_TAIL
from demos_shapes_basics import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Geometry: "
                "every shape a covenant of form, the circle the oath of "
                "return, the triangle the threefold witness, and the "
                "ladder the ascent from flat to solid. Clearly labeled "
                "Signature-made, never presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked foundational geometry: "
                "2D shapes (circle, triangle, square, rectangle, polygons) "
                "and 3D shapes (cube, sphere, cylinder, cone, pyramid) - "
                "names, properties, sides/vertices/faces, real-world "
                "examples, and introduction to symmetry, organized in the "
                "Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(what a shape is, points lines and angles, counting sides "
              "vertices and corners, circle, triangle, square, rectangle, "
              "other quadrilaterals, measuring length, shapes in the world "
              "around us) -> Compounded (pentagon and hexagon, heptagon "
              "through decagon and the n-gon, regular and irregular "
              "polygons, perimeter, area of rectangles and squares, area "
              "of triangles, circumference and area of the circle, from "
              "flat to solid, cube and rectangular prism, sphere, "
              "cylinder, cone, pyramid, volume of prisms and cylinders) -> "
              "Advanced (surface area, volume of pyramids cones and "
              "spheres, angles inside polygons, the number pi, reflectional "
              "symmetry, rotational symmetry, nets, Euler formula, "
              "congruence and similarity, transformations).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search circles, triangles, squares, rectangles, polygons, cubes, spheres, cylinders, cones, pyramids, perimeter, area, volume, symmetry, pi, nets, Euler...",
        "chat_ph": "Ask about shapes...",
        "archive_blurb": ("Seeded %s shapes basics records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled shapes basics studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about shapes - from what a shape is through points, lines, angles, sides, vertices, circles, triangles, squares, rectangles, quadrilaterals, measuring, and shapes in the world, through pentagons, hexagons, polygons, perimeter, area, circumference, solids, cubes, spheres, cylinders, cones, pyramids, and volumes, to surface area, pi, symmetry, nets, Euler, congruence, similarity, and transformations." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "shapes-basics-study", "gen_demo_kind": "shapes-basics-demo",
        "source": source,
    }

CIT_PUB = ("Foundational geometry (standard references: Euclid. Elements. "
           "Translated by Heath TL. 2nd ed. Dover; 1956; National Council "
           "of Teachers of Mathematics. Principles and Standards for "
           "School Mathematics. Reston, VA; 2000; National Governors "
           "Association Center for Best Practices. Common Core State "
           "Standards for Mathematics. Washington, DC; 2010; Archimedes. "
           "On the Sphere and Cylinder and Measurement of a Circle. "
           "Translated by Heath TL. Dover; 2002).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature "
                     "Geometry - every shape a covenant of form - clearly "
                     "labeled Signature-made.")

DBCFG = {}
DBCFG["shapes-basics"] = _cfg(
    "shapes-basics", "The Shapes Basics Database",
    "Names, properties, sides, vertices, faces, real-world examples, and "
    "symmetry for 2D shapes (circle, triangle, square, rectangle, polygons) "
    "and 3D shapes (cube, sphere, cylinder, cone, pyramid) - real, "
    "fact-checked foundational geometry taught progressively along the "
    "ladder.",
    "shapes basics record", "JAH-SHPB-", "JAH Shapes Basics Archivist",
    "shapes basics archivist - naming shapes and teaching their properties "
    "across 2D shapes (circle, triangle, square, rectangle, polygons) and "
    "3D shapes (cube, sphere, cylinder, cone, pyramid): sides, vertices, "
    "faces, measurement, real-world examples, and symmetry; teaching "
    "progressively along the ladder from foundations through compounded "
    "to advanced; answers from many angles - definition, example, analogy, "
    "application, history, math, how-to - using only archive data from "
    "this system",
    CIT_PUB, "public")
DBCFG["shapes-basics-signature"] = _cfg(
    "shapes-basics-signature", "The Shapes Basics Signature Database",
    "His original Signature Geometry: every shape a covenant of form, the "
    "circle the oath of return, the triangle the threefold witness, the "
    "ladder the ascent from flat to solid. The full ladder from what a "
    "shape is through points, lines, angles, circles, triangles, squares, "
    "rectangles, and measurement, through polygons, solids, and volumes, "
    "to pi, symmetry, nets, Euler, and transformations, reframed as "
    "Signature science. Clearly labeled Signature-made, never presented "
    "as authentic public record.",
    "shapes basics record", "JAH-SHPBS-", "JAH Shapes Basics Archivist (Signature)",
    "shapes basics archivist - Signature editions: his original Signature "
    "Geometry, every shape a covenant of form and the ladder the ascent "
    "from flat to solid, clearly labeled Signature-made and never "
    "presented as authentic public record; teaches progressively along "
    "the ladder from foundations through compounded to advanced; answers "
    "from many angles - definition, example, analogy, application, "
    "history, math, how-to - using only archive data from this system",
    CIT_SIG, "signature")

base.DBCFG = DBCFG

assert set(DEMOS) == {e["key"] for e in ENTRIES}, "demo map misses entries"


def build_records(slug, source):
    cfg = DBCFG[slug]
    sig = source == "signature"
    ordered = sorted(enumerate(ENTRIES), key=lambda p: (p[1]["ladder_rank"], p[0]))
    recs = []
    refused = []
    for _, e in ordered:
        name = e["name"]
        title = name + " (Signature Edition)" if sig else name
        if [h for h in base.GATE.check(slug, title) if h[0] != slug]:
            refused.append(title)
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
    return recs, refused


def node_check(path, label):
    p = subprocess.run(["node", "--check", path], capture_output=True,
                       text=True, timeout=60)
    assert p.returncode == 0, "node --check failed %s: %s" % (label, p.stderr[-800:])
    print("node --check clean: %s" % label, flush=True)


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
    all_refused = {}
    for slug in ("shapes-basics", "shapes-basics-signature"):
        source = "signature" if slug.endswith("-signature") else "public"
        built[slug], all_refused[slug] = build_records(slug, source)

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
        gpath = os.path.join(ddir, "gen-%s.js" % slug)
        with open(gpath, "w", encoding="utf-8") as f:
            f.write(gen_js)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)
        # JS hygiene: node --check on extracted page scripts and gen js
        scripts = re.findall(r"<script>(.*?)</script>", page, re.S)
        tmp = "/tmp/shapes_basics_scripts.js"
        with open(tmp, "w", encoding="utf-8") as f:
            for i, s in enumerate(scripts):
                f.write("// --- script block %d ---\n%s\n" % (i, s))
        node_check(tmp, "db/%s/index.html scripts (%d blocks)" % (slug, len(scripts)))
        node_check(gpath, "db/%s/gen-%s.js" % (slug, slug))

    # cross-check: every demo's computed numbers must appear in its entry text
    mismatched = []
    for slug, recs in built.items():
        for r in recs:
            p = subprocess.run([sys.executable, "-c", r["demo"]["program"]],
                               capture_output=True, text=True, timeout=120)
            text = (r["description"] + " " + r["how_it_works"]).replace(",", "")
            hits = 0
            for num in set(re.findall(r"\d+\.\d+|\d+", p.stdout)):
                if num in text or num.rstrip("0").rstrip(".") in text:
                    hits += 1
            if hits == 0:
                mismatched.append(r["id"])
    assert not mismatched, "demo numbers missing from entry text: %s" % mismatched
    print("entry/demo cross-check: all %d demos share computed values with entry text" % total, flush=True)

    # NOTE: manifest.json and api.json updates are the merger's job; this
    # builder never touches them, and never git commits or pushes.
    print("manifest + api.json: SKIPPED (merger handles). %d databases, %d records built." % (len(built), total))
    if any(all_refused.values()):
        print("REFUSALS: %s" % all_refused)
    else:
        print("dedupe: zero cross-db title collisions across all 68 titles.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
