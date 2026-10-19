#!/usr/bin/env python3
"""Build the Kalaripayattu Combat databases for JAH Databases (combat batch 3).

Two NEW databases, 34 ladder-ordered records each:

  combat-kalaripayattu              - The Kalaripayattu Combat Database
  combat-kalaripayattu-signature    - The Kalaripayattu Combat Signature Database

See entries_combat_kalaripayattu.py for the full verified build notes.

CONCURRENCY: this builder must NOT touch data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and must NOT git commit or
push. It writes only: db/combat-kalaripayattu/ + db/combat-kalaripayattu-signature/
(index.html + gen-*.js each), the shard data under
~/workspace/jah-databases-data-1/data/combat-kalaripayattu[-signature]/
(index.jsonl.gz + chunks/chunk-0000.jsonl.gz), the fragment JSON under
~/workspace/hidden_files/missing-builds/fragments/, and the code in this
directory. A merger handles the manifest, api.json, counts, and push.

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
from entries_combat_kalaripayattu import ENTRIES, SIG_TAIL
from demos_combat_kalaripayattu import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature combat method: "
                "every technique a covenant of body and breath, the vadivu "
                "the oath of the animal, the weapon the signature of the "
                "hand, and the kalari the archive of the ancestors written "
                "in motion. Clearly labeled Signature-made, never presented "
                "as authentic public record.")
    pub_line = ("Public records - real, fact-checked kalaripayattu knowledge: "
                "the Indian martial art of Kerala - vanakkam salutation, the "
                "eight ashtavadivu animal postures, chuvadukal footwork, "
                "kalugal leg conditioning, meyyorukkam body control, "
                "meippayattu body forms, swasam breath control, kolthari "
                "wooden weapons (muchan, otta, kol), angathari metal weapons "
                "(kadhara, kuntham, vaal, paricha, valum parichayum, gada, "
                "madu, urumi), verumkai empty-hand combat, kaal adikal "
                "kicks, uzhichil oil massage, marma sthana vital-point "
                "knowledge taught as traditional heritage, and kalari "
                "chikitsa bone-setting tradition - each record a full "
                "technique with step-by-step body mechanics, organized in "
                "the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(vanakkam salutation, gaja simha ashva varaha sarpam marjjara "
              "kukkuda and matsya vadivu postures, chuvadukal footwork, "
              "kalugal leg conditioning, meyyorukkam body control, "
              "meippayattu body forms, swasam breath control) -> Compounded "
              "(muchan short stick, otta curved stick, kol long staff, "
              "kolthari wooden-weapon forms, kadhara dagger, kuntham spear, "
              "vaal sword, paricha shield, valum parichayum sword and "
              "shield, verumkai empty-hand combat, kaal adikal kicks, gada "
              "mace) -> Advanced (madu twin horn dagger, urumi flexible "
              "sword, uzhichil oil massage, marma sthana vital-point "
              "knowledge, kalari chikitsa bone-setting tradition, angathari "
              "metal-weapon forms, verumkai uttama advanced empty-hand, "
              "sarva shastra prayogam mastery of the full arsenal).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search vadivus, stances, chuvadukal, meippayattu, muchan, otta, kol, kadhara, kuntham, vaal, paricha, urumi, verumkai, marma, uzhichil, kalari chikitsa...",
        "chat_ph": "Ask about kalaripayattu techniques...",
        "archive_blurb": ("Seeded %s kalaripayattu combat records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled kalaripayattu technique studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about kalaripayattu - from vanakkam, the eight vadivus, chuvadukal, kalugal, meyyorukkam, meippayattu, and swasam, through muchan, otta, kol, kolthari, kadhara, kuntham, vaal, paricha, valum parichayum, verumkai, kaal adikal, and gada, to madu, urumi, uzhichil, marma sthana, kalari chikitsa, angathari, verumkai uttama, and sarva shastra prayogam." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "kalaripayattu-technique-study", "gen_demo_kind": "kalaripayattu-technique-demo",
        "source": source,
    }

CIT_PUB = ("Kalaripayattu technique and tradition (standard references: "
           "Zarrilli P. When the Body Becomes All Eyes: Paradigms, Discourses "
           "and Practices of Power in Kalarippayattu, a South Indian Martial "
           "Art. Oxford University Press; 1998; Draeger D, Smith R. Asian "
           "Fighting Arts. Kodansha International; 1969; Reid H, Croucher "
           "M. The Way of the Warrior: The Paradox of the Martial Arts. "
           "Overlook Press; 1983; Green T, Svinth J, editors. Martial Arts "
           "of the World: An Encyclopedia of History and Innovation. "
           "ABC-CLIO; 2010; Frawley D, Ranade S, Lele A. Ayurveda and Marma "
           "Therapy: Energy Points in Yogic Healing. Lotus Press; 2003; "
           "Indian Kalarippayattu Federation technical syllabus and "
           "competition rules).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature combat "
                     "method - every technique a covenant of body and breath, "
                     "the vadivu the oath of the animal, the weapon the "
                     "signature of the hand - clearly labeled Signature-made.")

DBCFG = {}
DBCFG["combat-kalaripayattu"] = _cfg(
    "combat-kalaripayattu", "The Kalaripayattu Combat Database",
    "Every stance, weapon form, and empty-hand technique of kalaripayattu, "
    "the Indian martial art of Kerala - the eight ashtavadivu animal "
    "postures, chuvadukal footwork, meippayattu body forms, kolthari wooden "
    "weapons, angathari metal weapons, verumkai empty-hand combat, and the "
    "marma body knowledge taught as traditional heritage - each record a "
    "full technique with step-by-step body mechanics, taught progressively "
    "along the ladder from the salutation to the full arsenal.",
    "kalaripayattu technique record", "JAH-CBKP-", "JAH Kalaripayattu Combat Archivist",
    "kalaripayattu combat archivist - every stance, weapon form, and "
    "empty-hand technique of the Indian martial art of Kerala, each with "
    "step-by-step body mechanics; teaching progressively along the ladder "
    "from foundations through compounded to advanced; answers from many "
    "angles - definition, example, analogy, application, history, math, "
    "how-to - using only archive data from this system",
    CIT_PUB, "public")
DBCFG["combat-kalaripayattu-signature"] = _cfg(
    "combat-kalaripayattu-signature", "The Kalaripayattu Combat Signature Database",
    "His original Signature combat method: every technique a covenant of "
    "body and breath, the vadivu the oath of the animal, the weapon the "
    "signature of the hand, the kalari the archive of the ancestors written "
    "in motion. The full ladder from vanakkam through the eight animal "
    "postures, body forms, wooden and metal weapons, and empty-hand combat "
    "to sarva shastra prayogam, reframed as Signature science. Clearly "
    "labeled Signature-made, never presented as authentic public record.",
    "kalaripayattu technique record", "JAH-CBKPS-", "JAH Kalaripayattu Combat Archivist (Signature)",
    "kalaripayattu combat archivist - Signature editions: his original "
    "Signature combat method, every technique a covenant of body and breath "
    "and the kalari the archive of the ancestors written in motion, clearly "
    "labeled Signature-made and never presented as authentic public record; "
    "teaches progressively along the ladder from foundations through "
    "compounded to advanced; answers from many angles - definition, example, "
    "analogy, application, history, math, how-to - using only archive data "
    "from this system",
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
    for slug in ("combat-kalaripayattu", "combat-kalaripayattu-signature"):
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
        assert "karate" not in page.lower(), "field leftover (karate) in %s" % slug
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
        assert "karate" not in gen_js.lower(), "field leftover (karate) in gen js %s" % slug
        with open(os.path.join(ddir, "gen-%s.js" % slug), "w", encoding="utf-8") as f:
            f.write(gen_js)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)

    # NOTE: manifest.json / api.json updates are the merger's job - this
    # builder never touches them (concurrency rule).
    print("built %d databases, %d records; manifest/api left for the merger." % (len(built), total))
    return 0


if __name__ == "__main__":
    sys.exit(main())
