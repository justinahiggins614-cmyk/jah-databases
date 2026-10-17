#!/usr/bin/env python3
"""Build The Colors Basics Database and its Signature edition (Manon's
fundamentals order #9, 2026-10-17).

Replicates code/component-parts-catalog-build/build.py page structure and
pipeline exactly. Differences from the template: this builder NEVER touches
data/manifest.json, api.json, index.html, README.md, or docs/AI_ACCESS.md,
never commits, never pushes - a merger handles those. It writes the fragment
~/workspace/hidden_files/missing-builds/fragments/colors-basics.json for the
merger instead.

Dedupe pre-check 2026-10-17: 68 titles vs the whole system BEFORE authoring;
2 collisions renamed ("Opposites on the Wheel: Complementary Colors",
"Neighbors on the Wheel: Analogous Colors"); all 68 final titles FREE.
ID prefixes JAH-COLB- / JAH-COLBS-: zero hits in manifest id_prefix values
and in all 810 shard index files.

34 records each, ladder-ordered (ranks 1-10 non-decreasing;
foundations 10 / compounded 18 / advanced 6). All 68 demos machine-executed
before page writing; every demo prints real computed values, asserts tight
bounds (never float exact-equality), ends with the OK marker.

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
from entries_colors_basics import ENTRIES, SIG_TAIL
from demos_colors_basics import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Color Method: "
                "every hue a signature of light, the wheel the covenant of "
                "families, mixing the oath between maker and material, and "
                "tints and shades the honor margins of brightness. Clearly "
                "labeled Signature-made, never presented as authentic public "
                "record.")
    pub_line = ("Public records - real, fact-checked foundational color "
                "knowledge: color families, primary secondary and tertiary "
                "colors, color mixing, the color wheel, shades tints and "
                "tones, color names, and how eyes see color - every record "
                "carrying description, how it works, key points, "
                "requirements, standards, citations, and a working "
                "demonstration program, organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(what color is, how the eye sees color, hue value and "
              "chroma, light and pigment, primary colors, secondary "
              "colors, tertiary colors, warm and cool colors, tints "
              "shades and tones, neutral colors) -> Compounded (the color "
              "wheel, subtractive mixing, additive mixing, complementary "
              "colors, analogous colors, triadic schemes, color "
              "temperature, saturation, brightness and lightness, the red "
              "blue green yellow purple and orange families, brown, gray, "
              "black and white) -> Advanced (color harmonies and schemes, "
              "hex and RGB codes, CMYK for print, color vision "
              "differences, color and emotion, the spectrum and beyond).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search color families, primaries, secondaries, tertiaries, mixing, color wheel, tints, shades, tones, hex, RGB, CMYK, cones, saturation, harmonies...",
        "chat_ph": "Ask about color basics...",
        "archive_blurb": ("Seeded %s color basics records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled color basics studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about color basics - from what color is through how eyes see color, hue value and chroma, light and pigment, primaries, secondaries, tertiaries, warm and cool, tints shades and tones, and neutrals, through the color wheel, mixing, complements, analogs, triads, temperature, saturation, brightness, the color families, brown, gray, black and white, to harmonies, hex and RGB, CMYK, vision differences, emotion, and the spectrum beyond." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "color-basics-study", "gen_demo_kind": "color-basics-demo",
        "source": source,
    }

CIT_PUB = ("Color science foundations (standard references: Munsell AH. A "
           "Color Notation. Munsell Color Company; 1905; Itten J. The Art of "
           "Color. Reinhold; 1961; Albers J. Interaction of Color. Yale "
           "University Press; 1963; Wyszecki G, Stiles WS. Color Science: "
           "Concepts and Methods, Quantitative Data and Formulae. 2nd ed. "
           "Wiley; 1982; Kuehni RG, Schwarz A. Color Ordered. Oxford "
           "University Press; 2008; Fairchild MD. Color Appearance Models. "
           "3rd ed. Wiley; 2013; CIE 15:2004 Colorimetry; Solomon SG, Lennie "
           "P. The machinery of colour vision. Nature Reviews Neuroscience. "
           "2007;8(4):276-286; Hecht E. Optics. 5th ed. Pearson; 2017; "
           "Elliot AJ, Maier MA. Color psychology. Annual Review of "
           "Psychology. 2014;65:95-120; ASTM D1535-18; IEC 61966-2-1 sRGB; "
           "W3C CSS Color Module).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature Color "
                     "Method - every hue a signature of light, the wheel "
                     "the covenant of families - clearly labeled "
                     "Signature-made.")

DBCFG = {}
DBCFG["colors-basics"] = _cfg(
    "colors-basics", "The Colors Basics Database",
    "Learn color from the ground up: real, fact-checked foundational color "
    "knowledge - color families, primary secondary and tertiary colors, "
    "color mixing, the color wheel, shades tints and tones, color names, "
    "and how eyes see color - taught progressively along the ladder from "
    "simple foundations to compounded families to advanced codes and "
    "harmonies.",
    "colors basics record", "JAH-COLB-", "JAH Colors Basics Archivist",
    "colors basics archivist - teaching foundational color knowledge from "
    "what color is through how eyes see color, hue value and chroma, light "
    "and pigment, primaries, secondaries, tertiaries, warm and cool, tints "
    "shades and tones, and neutrals, through the color wheel, mixing, "
    "complements, analogs, triads, temperature, saturation, brightness, "
    "the color families, brown, gray, black and white, to harmonies, hex "
    "and RGB, CMYK, vision differences, emotion, and the spectrum beyond; "
    "teaching progressively along the ladder from foundations through "
    "compounded to advanced; answers from many angles - definition, "
    "example, analogy, application, history, math, how-to - using only "
    "archive data from this system",
    CIT_PUB, "public")
DBCFG["colors-basics-signature"] = _cfg(
    "colors-basics-signature", "The Colors Basics Signature Database",
    "His original Signature Color Method: every hue a signature of light, "
    "the wheel the covenant of families, mixing the oath between maker "
    "and material, tints and shades the honor margins of brightness. The "
    "full ladder from what color is through how eyes see it, hue value "
    "and chroma, light and pigment, and the primary secondary tertiary "
    "ascent, through the wheel, mixing, complements, analogs, triads, "
    "temperature, saturation, brightness, and every color family, to "
    "harmonies, codes, CMYK, vision differences, emotion, and the spectrum "
    "beyond, reframed as Signature science. Clearly labeled "
    "Signature-made, never presented as authentic public record.",
    "colors basics record", "JAH-COLBS-", "JAH Colors Basics Archivist (Signature)",
    "colors basics archivist - Signature editions: his original Signature "
    "Color Method, every hue a signature of light and the wheel the "
    "covenant of families, clearly labeled Signature-made and never "
    "presented as authentic public record; teaches progressively along the "
    "ladder from foundations through compounded to advanced; answers from "
    "many angles - definition, example, analogy, application, history, "
    "math, how-to - using only archive data from this system",
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


def write_fragment(built):
    os.makedirs(FRAG_DIR, exist_ok=True)
    frag = {}
    for slug, recs in built.items():
        sig = slug.endswith("-signature")
        cfg = DBCFG[slug]
        key = "signature" if sig else "public"
        frag[key] = {
            "slug": slug,
            "name": cfg["name"],
            "tagline": cfg["tagline"],
            "record_kind": cfg["record_kind"],
            "id_prefix": cfg["prefix"],
            "ai_name": cfg["ai"],
            "local_index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
            "record_count": len(recs),
            "status": "live",
            "full_records": len(recs),
            "index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
            "chunk_pattern": "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz",
            "source": cfg["source"],
        }
    path = os.path.join(FRAG_DIR, "colors-basics.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(frag, f, indent=2, ensure_ascii=False)
        f.write("\n")
    return path


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

    built = {}
    all_refused = []
    for slug in ("colors-basics", "colors-basics-signature"):
        source = "signature" if slug.endswith("-signature") else "public"
        recs, refused = build_records(slug, source)
        built[slug] = recs
        all_refused.extend(refused)

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
        assert "colors basics" in page.lower(), "field name missing in %s" % slug
        ddir = os.path.join(REPO, "db", slug)
        os.makedirs(ddir, exist_ok=True)
        ppath = os.path.join(ddir, "index.html")
        with open(ppath, "w", encoding="utf-8") as f:
            f.write(page)
        notes = []
        if sweep is not None:
            _, notes = sweep.process_page(ppath)
        topics = {}
        for r in recs:
            topics.setdefault(r["g"], []).append("%s - %s" % (r["t"], r["g"]))
        gen_js = nb.build_gen_js(slug, topics, DBCFG[slug])
        assert "facebook" not in gen_js.lower() and "bat belt" not in gen_js.lower()
        assert "universal build" not in gen_js.lower(), "field leftover in gen js %s" % slug
        assert "synthetic intelligence" not in gen_js.lower(), "template leftover in gen js %s" % slug
        with open(os.path.join(ddir, "gen-%s.js" % slug), "w", encoding="utf-8") as f:
            f.write(gen_js)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)

    frag_path = write_fragment(built)
    print("fragment: %s" % frag_path, flush=True)
    print("manifest/api.json/index.html/README/docs untouched (merger owns them).")
    print("gate refusals: %d %s" % (len(all_refused), all_refused if all_refused else "(none)"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
