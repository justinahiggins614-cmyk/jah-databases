#!/usr/bin/env python3
"""Build the Eskrima Kali Arnis Combat databases for JAH Databases
(combat batch 2).

Verified 2026-10-17 (combat batch 2): RAW SWEEP over the full manifest
plus every shard index title in jah-databases-data-1: zero
'combat-eskrima*' slugs/names; zero title collisions on all 34 public
titles and all 34 Signature-suffixed titles (dedupe_gate whole-system
check before authoring, 0 refusals). Civilian training scope only.

This build creates two NEW databases, 34 ladder-ordered records each:

  combat-eskrima-kali-arnis            - The Eskrima Kali Arnis Combat
                                        Database
  combat-eskrima-kali-arnis-signature - The Eskrima Kali Arnis Combat
                                        Signature Database

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-CBEKA- (public) and JAH-CBEKAS- (signature), verified free
in the manifest id_prefix values and in every shard index (zero hits).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_eskrima_kali_arnis.py). Every demo prints its real
computed values, asserts tight bounds (never float exact-equality), and
ends with the OK marker; the build machine-executes all 68 demos.

CONCURRENCY: this builder never touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md and never commits or pushes.
It writes only: db/<slug>/, code/combat-eskrima-kali-arnis-build/,
jah-databases-data-1 data dirs, and the merger fragment. The merger owns
manifest/api/hub integration.

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
FRAGMENT = "/home/hatch/workspace/hidden_files/missing-builds/fragments/combat-eskrima-kali-arnis.json"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_eskrima_kali_arnis import ENTRIES, SIG_TAIL
from demos_eskrima_kali_arnis import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Combat Method: "
                "the weapon as the teacher, the angle as the lesson, the "
                "triangle as the path. Clearly labeled Signature-made, never "
                "presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked Filipino martial arts: "
                "single and double stick, blade work, empty-hand translation "
                "(panantukan), disarms, triangle footwork - every record a "
                "technique with how-to body mechanics, real Filipino "
                "terminology with translations, and working training "
                "calculators, organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(what the art is, the stick, the grip, stance and handa, the "
              "five basic angles, angles six through twelve, the forward "
              "triangle, the twelve basic strikes, the retreat triangle, "
              "blocking, the abaniko fan strike, solo shadow drills) -> "
              "Compounded (sinawali double-stick weave, heaven six, redonda, "
              "hubud-lubud, sombrada, tapi-tapi, espada y daga, sidestepping "
              "and the female triangle, panantukan, gunting, knife grips and "
              "angles, snaking disarms, strips and punyo work) -> Advanced "
              "(live-blade awareness, cadena de mano, dumog grappling, the "
              "live hand, advanced espada y daga, protected sparring, "
              "free-flow sparring, multiple opponents, mastery).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search eskrima, kali, arnis, angles, sinawali, hubud, sombrada, disarms, panantukan, dumog, footwork, daga, espada y daga, sparring...",
        "chat_ph": "Ask about eskrima, kali, and arnis...",
        "archive_blurb": ("Seeded %s eskrima kali arnis combat records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled eskrima kali arnis combat studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about eskrima, kali, and arnis - from what the art is through the stick, grip, stance, angles, triangles, strikes, blocks, and shadow drills, through sinawali, heaven six, redonda, hubud-lubud, sombrada, tapi-tapi, espada y daga, sidestepping, panantukan, gunting, knife work, and disarms, to live-blade awareness, cadena de mano, dumog, the live hand, sparring, multiple opponents, and mastery." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "eskrima-kali-arnis-study", "gen_demo_kind": "eskrima-kali-arnis-demo",
        "source": source,
    }

CIT_PUB = ("Filipino martial arts (standard references: Wiley MV. Filipino "
           "Martial Culture. Charles E. Tuttle Company; 1997; Wiley MV. "
           "Filipino Fighting Arts: Theory and Practice. Unique Publications; "
           "2000; Inosanto D. The Filipino Martial Arts. Know Now "
           "Publishing; 1980; Presas R. Modern Arnis: The Filipino Art of "
           "Stick Fighting. Black Belt Books; 1983; Sulite EG. Masters of "
           "Arnis, Kali and Eskrima. Paladin Press; 1994; Galang R. Complete "
           "Sinawali: Filipino Double Weapon Fighting. Charles E. Tuttle "
           "Company; 2000). Civilian training scope: technique instruction "
           "with body mechanics only.")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature Combat "
                     "Method - the weapon as the teacher, the angle as the "
                     "lesson, the triangle as the path - clearly labeled "
                     "Signature-made.")

DBCFG = {}
DBCFG["combat-eskrima-kali-arnis"] = _cfg(
    "combat-eskrima-kali-arnis", "The Eskrima Kali Arnis Combat Database",
    "Filipino martial arts, taught weapon-first: single and double stick, "
    "blade work, empty-hand translation, disarms, and triangle footwork - "
    "every record a technique with how-to body mechanics, real Filipino "
    "terminology with translations, and working training calculators, "
    "taught progressively along the ladder.",
    "combat technique record", "JAH-CBEKA-", "JAH Eskrima Kali Arnis Combat Archivist",
    "eskrima kali arnis combat archivist - Filipino martial arts taught "
    "weapon-first: single and double stick, blade work, empty-hand "
    "translation, disarms, and triangle footwork; teaching progressively "
    "along the ladder from foundations through compounded to advanced; "
    "answers from many angles - definition, example, analogy, application, "
    "history, math, how-to - using only archive data from this system",
    CIT_PUB, "public")
DBCFG["combat-eskrima-kali-arnis-signature"] = _cfg(
    "combat-eskrima-kali-arnis-signature", "The Eskrima Kali Arnis Combat Signature Database",
    "His original Signature Combat Method: the weapon as the teacher, the "
    "angle as the lesson, the triangle as the path. The full ladder from "
    "what the art is through the stick, grip, stance, angles, and "
    "triangles, through the double-stick weaves, traps, translations, and "
    "disarms, to blade awareness, the chain of hands, grappling, sparring, "
    "and mastery, reframed as Signature science. Clearly labeled "
    "Signature-made, never presented as authentic public record.",
    "combat technique record", "JAH-CBEKAS-", "JAH Eskrima Kali Arnis Combat Archivist (Signature)",
    "eskrima kali arnis combat archivist - Signature editions: his original "
    "Signature Combat Method, the weapon as the teacher and the angle as "
    "the lesson, clearly labeled Signature-made and never presented as "
    "authentic public record; teaches progressively along the ladder from "
    "foundations through compounded to advanced; answers from many angles - "
    "definition, example, analogy, application, history, math, how-to - "
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
    frag = {}
    for slug, recs in built.items():
        cfg = DBCFG[slug]
        entry = base.manifest_entry(slug, len(recs))
        entry["chunk_pattern"] = "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz"
        key = "signature" if slug.endswith("-signature") else "public"
        frag[key] = entry
    os.makedirs(os.path.dirname(FRAGMENT), exist_ok=True)
    with open(FRAGMENT, "w", encoding="utf-8") as f:
        json.dump(frag, f, indent=1, ensure_ascii=False)
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
    for slug in ("combat-eskrima-kali-arnis", "combat-eskrima-kali-arnis-signature"):
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
    print("records: %d total (34 public + 34 signature)" % total)
    print("NOTE: manifest.json / api.json / hub pages untouched by design - merger owns them.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
