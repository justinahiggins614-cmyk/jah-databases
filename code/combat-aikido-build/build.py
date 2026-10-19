#!/usr/bin/env python3
"""Build the Aikido Combat databases for JAH Databases (Manon's combat
orders 2026-10-17, combat batch 2).

Dedupe pre-verified 2026-10-17: all 68 titles (34 public + 34 Signature
Edition) run through DedupeGate against the WHOLE system before authoring:
zero collisions, zero refusals.

Two NEW databases, 34 ladder-ordered records each:

  combat-aikido              - The Aikido Combat Database
                               (public-harvest: real, fact-checked aikido -
                               tai-sabaki movement, ukemi, wrist controls
                               ikkyo through gokyo, throws irimi-nage,
                               shiho-nage, kotegaeshi and the rest, pins,
                               randori, weapons disarms - real Japanese
                               terminology with translations, step-by-step
                               body mechanics; standard references the
                               Aikikai Foundation syllabus, Morihei Ueshiba
                               (O-Sensei, 1883-1969), Budo (1938), and the
                               kyo-waza teaching sequence)
  combat-aikido-signature    - The Aikido Combat Signature Database
                               (his original Signature Aiki Method: every
                               technique a covenant of movement, the art the
                               armory of harmony, blending the oath, the
                               throw the handshake, the pin the honor hold;
                               src signature, titles suffixed " (Signature
                               Edition)", never presented as authentic
                               public record)

34 records each, teaching ladder ranks 1-10 non-decreasing
(foundations/compounded/advanced). Shard index written in ladder order.

ID prefixes: JAH-CBAIK- (public) and JAH-CBAIKS- (signature), verified free
in the manifest (2,410 databases, zero hits) and in every shard index file
(zero hits).

Numerical cores: hand-computed 2026-10-17, machine-verified by the demos.
Every demo prints real computed values, asserts tight bounds (never float
exact-equality), ends with the OK marker; this build machine-executes all
68 demos.

Civilian martial-arts instruction only. Nothing on neutralizing or
defeating military or defense-grade systems.

NOTE: this build does NOT touch data/manifest.json, api.json, index.html,
README.md, or docs/AI_ACCESS.md and does NOT commit or push - a merger
handles those. It writes only: db/combat-aikido[/-signature]/ (index.html
+ gen-*.js), the shard data dirs, and the fragment JSON.

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
TEMPLATE = os.path.join(REPO, "db", "public-synthetic-intelligence", "index.html")
FRAG = "/home/hatch/workspace/hidden_files/missing-builds/fragments/combat-aikido.json"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_combat_aikido import ENTRIES, SIG_TAIL
from demos_combat_aikido import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Aiki Method: "
                "every technique a covenant of movement, the art the armory "
                "of harmony, blending the oath, the throw the handshake, "
                "and the pin the honor hold. Clearly labeled Signature-made, "
                "never presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked aikido: tai-sabaki "
                "movement (ashi-sabaki, tenkan, irimi), ukemi safe falling "
                "(mae-ukemi, ushiro-ukemi, yoko-ukemi), the five wrist "
                "controls (ikkyo through gokyo), throws (irimi-nage, "
                "shiho-nage, kotegaeshi, jujinage, kaiten-nage, sumi-otoshi, "
                "aiki-otoshi, koshi-nage, udekime-nage), pins (katame-waza), "
                "randori and jiyu-waza, knife/sword/staff disarms, counter "
                "techniques, seated forms, and aiki-ken/aiki-jo - each "
                "record carrying real Japanese terminology with "
                "translations and step-by-step body-mechanics instruction, "
                "organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(what aikido is, the founder, dojo etiquette, shisei and "
              "hanmi, ashi-sabaki footwork, tenkan and irimi movement, "
              "forward/back/side ukemi, kuzushi, awase and musubi, ma-ai "
              "and atemi, grip fundamentals) -> Compounded (ikkyo, nikyo, "
              "sankyo, yonkyo, gokyo, irimi-nage, shiho-nage, kotegaeshi, "
              "jujinage, kaiten-nage, sumi-otoshi, aiki-otoshi) -> Advanced "
              "(koshi-nage, udekime-nage, katame-waza pins, randori, "
              "jiyu-waza, tanto-dori, tachi-dori and jo-dori, kaeshi-waza, "
              "hanmi-handachi and suwari-waza, aiki-ken and aiki-jo).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search tai-sabaki, ukemi, ikkyo, nikyo, sankyo, yonkyo, gokyo, irimi-nage, shiho-nage, kotegaeshi, pins, randori, tanto-dori, kaeshi-waza...",
        "chat_ph": "Ask about aikido techniques...",
        "archive_blurb": ("Seeded %s aikido combat records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled aikido technique studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about aikido - from what the art is, the founder, dojo etiquette, posture and hanmi, footwork, tenkan and irimi, ukemi in all directions, kuzushi, blending and connection, distance and atemi, and grips, through the five wrist controls and the great throws, to hip throws, pins, randori, free techniques, knife sword and staff disarms, counters, seated forms, and the wooden sword and staff." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "aikido-study", "gen_demo_kind": "aikido-demo",
        "source": source,
    }

CIT_PUB = ("Aikido technique (standard references: Ueshiba M. Budo: "
           "Teachings of the Founder of Aikido. Kodansha International; "
           "1991 (orig. 1938); Aikikai Foundation grading and technique "
           "syllabus tradition, Hombu Dojo, Tokyo; Westbrook A, Ratti O. "
           "Aikido and the Dynamic Sphere. Charles E. Tuttle; 1970; "
           "Shioda G. Aikido Shugyo: Harmony in Confrontation. Shindensha; "
           "2002; Saotome M. Aikido and the Harmony of Nature. Shambhala; "
           "1993; Pranin S. (ed.) Aikido Masters: Prewar Students of "
           "Morihei Ueshiba. Aiki News; 1993).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature Aiki "
                     "Method - every technique a covenant of movement, the "
                     "art the armory of harmony - clearly labeled "
                     "Signature-made.")

DBCFG = {}
DBCFG["combat-aikido"] = _cfg(
    "combat-aikido", "The Aikido Combat Database",
    "Learn aikido technique by technique: real, fact-checked instruction "
    "across tai-sabaki movement, ukemi safe falling, the five wrist "
    "controls, the great throws, pins, randori, and weapons disarms - "
    "every record carrying real Japanese terminology with translations "
    "and step-by-step body mechanics, taught progressively along the "
    "ladder from movement basics to advanced throws.",
    "combat technique record", "JAH-CBAIK-", "JAH Aikido Combat Archivist",
    "aikido combat archivist - teaching aikido technique by technique: "
    "tai-sabaki movement, ukemi, wrist controls, throws, pins, randori, "
    "and disarms; real Japanese terminology with translations; "
    "step-by-step body mechanics; teaching progressively along the ladder "
    "from foundations through compounded to advanced; answers from many "
    "angles - definition, example, analogy, application, history, math, "
    "how-to - using only archive data from this system",
    CIT_PUB, "public")
DBCFG["combat-aikido-signature"] = _cfg(
    "combat-aikido-signature", "The Aikido Combat Signature Database",
    "His original Signature Aiki Method: every technique a covenant of "
    "movement, the art the armory of harmony, blending the oath, the "
    "throw the handshake, the pin the honor hold. The full ladder from "
    "what aikido is through movement, ukemi, principles, and grips, "
    "through the five wrist controls and the great throws, to hip "
    "throws, pins, randori, disarms, counters, seated forms, and the "
    "wooden sword and staff, reframed as Signature science. Clearly "
    "labeled Signature-made, never presented as authentic public record.",
    "combat technique record", "JAH-CBAIKS-", "JAH Aikido Combat Archivist (Signature)",
    "aikido combat archivist - Signature editions: his original Signature "
    "Aiki Method, every technique a covenant of movement and the art the "
    "armory of harmony, clearly labeled Signature-made and never presented "
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


def write_fragment(built):
    frag = {"public": {}, "signature": {}}
    for slug, recs in built.items():
        sig = slug.endswith("-signature")
        cfg = DBCFG[slug]
        base_url = ("https://justinahiggins614-cmyk.github.io/jah-databases-data-1"
                    "/data/%s/index.jsonl.gz" % slug)
        entry = {
            "slug": slug,
            "name": cfg["name"],
            "tagline": cfg["tagline"],
            "record_kind": cfg["record_kind"],
            "id_prefix": cfg["prefix"],
            "ai_name": cfg["ai"],
            "local_index": base_url,
            "record_count": len(recs),
            "status": "live",
            "full_records": len(recs),
            "index": base_url,
            "chunk_pattern": "data/%s/chunks/chunk-NNNN.jsonl.gz" % slug,
            "source": "signature" if sig else "public-harvest",
        }
        frag["signature" if sig else "public"] = entry
    os.makedirs(os.path.dirname(FRAG), exist_ok=True)
    with open(FRAG, "w", encoding="utf-8") as f:
        json.dump(frag, f, indent=2)
    print("fragment: %s" % FRAG, flush=True)


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
    for slug in ("combat-aikido", "combat-aikido-signature"):
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
            field = r["ladder_tier"].capitalize()  # Foundations/Compounded/Advanced
            topics.setdefault(field, []).append("%s - %s" % (r["t"], r["g"]))
        gen_js = nb.build_gen_js(slug, topics, DBCFG[slug])
        assert "facebook" not in gen_js.lower() and "bat belt" not in gen_js.lower()
        assert "universal build" not in gen_js.lower(), "field leftover in gen js %s" % slug
        with open(os.path.join(ddir, "gen-%s.js" % slug), "w", encoding="utf-8") as f:
            f.write(gen_js)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)

    write_fragment(built)
    print("manifest/api/index.html/README/AI_ACCESS untouched (merger handles).")
    print("DONE: %d databases, %d records. No commit, no push." % (len(built), total))
    return 0


if __name__ == "__main__":
    sys.exit(main())
