#!/usr/bin/env python3
"""Build the Pencak Silat Combat databases for JAH Databases (combat batch 3).

Two NEW databases, 34 ladder-ordered records each:

  combat-pencak-silat            - The Pencak Silat Combat Database
  combat-pencak-silat-signature  - The Pencak Silat Combat Signature Database

See entries_combat_pencak_silat.py for the full verified build notes.

CONCURRENCY: this builder must NOT touch data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and must NOT git commit or
push. It writes only: db/combat-pencak-silat/ + db/combat-pencak-silat-signature/
(index.html + gen-*.js each), the shard data under
~/workspace/jah-databases-data-1/data/combat-pencak-silat[-signature]/
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
from entries_combat_pencak_silat import ENTRIES, SIG_TAIL
from demos_combat_pencak_silat import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature silat method: "
                "every technique a covenant of body and breath, the kuda-kuda "
                "the oath of the earth, the jurus the archive of the "
                "ancestors written in motion, and the langkah the signature "
                "of the path. Clearly labeled Signature-made, never presented "
                "as authentic public record.")
    pub_line = ("Public records - real, fact-checked Indonesian pencak silat "
                "knowledge: kuda-kuda stances, sikap guard postures, langkah "
                "footwork, pukulan punches, tendangan kicks, tangkisan "
                "blocks, elakan evasions, tangkapan catches, sapuan sweeps, "
                "bantingan throws, kuncian joint locks, guntingan scissors, "
                "jurus forms, kembangan flow, tanding sport rules, and the "
                "toya, golok, karambit, and keris blade heritage - each "
                "record a full technique with step-by-step body mechanics, "
                "organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(kuda-kuda stances, sikap pasang guard, langkah stepping "
              "patterns, pernapasan breathing, pukulan lurus straight punch, "
              "tendangan lurus front kick, tangkisan dalam inside block, "
              "elakan evasions, tepisan parries, tangkapan catches, kembangan "
              "flow dance) -> Compounded (tendangan sabit crescent kick, "
              "tendangan T side kick, siku elbows, lutut knees, pukulan "
              "bandul swinging punch, sapuan sweeps, bantingan throws, "
              "kuncian joint locks, tendangan belakang back kick, guntingan "
              "scissors, jurus tunggal solo form) -> Advanced (sambutan "
              "planned counters, jarak dan tempo distance and timing, toya "
              "staff, tanding sport rules, golok machete, karambit curved "
              "blade, main bawah ground fighting, keris dagger, jurus "
              "senjata weapon form, patahan controlled locking study, aliran "
              "lineage study, ujian grading and mastery).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search kuda-kuda, sikap pasang, langkah, pukulan, tendangan, tangkisan, elakan, sapuan, bantingan, kuncian, guntingan, jurus, kembangan, tanding, toya, golok, karambit, keris...",
        "chat_ph": "Ask about pencak silat techniques...",
        "archive_blurb": ("Seeded %s pencak silat combat records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled pencak silat technique studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about pencak silat - from kuda-kuda stances, sikap pasang guard, langkah stepping, pernapasan breathing, pukulan lurus, tendangan lurus, tangkisan dalam, elakan, tepisan, tangkapan, and kembangan, through tendangan sabit, tendangan T, siku, lutut, pukulan bandul, sapuan, bantingan, kuncian, tendangan belakang, guntingan, and jurus tunggal, to sambutan counters, jarak dan tempo, toya, tanding, golok, karambit, main bawah, keris, jurus senjata, patahan, aliran, and ujian." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "pencak-silat-technique-study", "gen_demo_kind": "pencak-silat-technique-demo",
        "source": source,
    }

CIT_PUB = ("Pencak silat technique, forms, and heritage (standard references: "
           "Draeger D.F. Weapons and Fighting Arts of Indonesia. Charles E. "
           "Tuttle; 1972; Maryono O. Pencak Silat in the Indonesian "
           "Archipelago. Yayasan Galang; 1998; Ikatan Pencak Silat Indonesia "
           "(IPSI) Peraturan Pertandingan Pencak Silat, current edition; "
           "Persekutuan Pencak Silat Antarbangsa (PERSILAT) international "
           "competition regulations; UNESCO inscription of the Traditions of "
           "Pencak Silat on the Representative List of the Intangible "
           "Cultural Heritage of Humanity; 2019).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature silat "
                     "method - every technique a covenant of body and breath, "
                     "the kuda-kuda the oath of the earth, the jurus the "
                     "archive of the ancestors written in motion - clearly "
                     "labeled Signature-made.")

DBCFG = {}
DBCFG["combat-pencak-silat"] = _cfg(
    "combat-pencak-silat", "Pencak Silat Combat Database",
    "Indonesian pencak silat - jurus forms, sweeps, joint locks, and blade "
    "heritage: kuda-kuda stances, sikap guard, langkah footwork, punches, "
    "kicks, blocks, evasions, catches, sapuan sweeps, bantingan throws, "
    "kuncian locks, guntingan scissors, jurus forms, kembangan flow, tanding "
    "sport rules, and the toya, golok, karambit, and keris heritage - each "
    "record a full technique with step-by-step body mechanics, taught "
    "progressively along the ladder from foundations to mastery.",
    "combat technique record", "JAH-CBPS-", "JAH Pencak Silat Combat Archivist",
    "pencak silat combat archivist - Indonesian pencak silat: jurus forms, "
    "sweeps, joint locks, and blade heritage, each technique with "
    "step-by-step body mechanics; teaching progressively along the ladder "
    "from foundations through compounded to advanced; answers from many "
    "angles - definition, example, analogy, application, history, math, "
    "how-to - using only archive data from this system",
    CIT_PUB, "public")
DBCFG["combat-pencak-silat-signature"] = _cfg(
    "combat-pencak-silat-signature", "Pencak Silat Combat Signature Database",
    "His original Signature silat method: every technique a covenant of "
    "body and breath, the kuda-kuda the oath of the earth, the jurus the "
    "archive of the ancestors written in motion, and the langkah the "
    "signature of the path. The full ladder from stances, guard, footwork, "
    "and breathing through strikes, sweeps, throws, locks, and forms to "
    "counters, strategy, blade heritage, lineage, and mastery, reframed as "
    "Signature science. Clearly labeled Signature-made, never presented as "
    "authentic public record.",
    "combat technique record", "JAH-CBPSS-", "JAH Pencak Silat Combat Archivist (Signature)",
    "pencak silat combat archivist - Signature editions: his original "
    "Signature silat method, every technique a covenant of body and breath "
    "and the jurus the archive of the ancestors written in motion, clearly "
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


def write_fragment(built):
    frag = {"public": {}, "signature": {}}
    for slug, recs in built.items():
        cfg = DBCFG[slug]
        sig = slug.endswith("-signature")
        idx = "%s/data/%s/index.jsonl.gz" % (SHARD_BASE, slug)
        frag["signature" if sig else "public"] = {
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
            "chunk_pattern": "data/%s/chunks/chunk-NNNN.jsonl.gz" % slug,
            "source": "signature" if sig else "public-harvest",
        }
    out = "/home/hatch/workspace/hidden_files/missing-builds/fragments/combat-pencak-silat.json"
    with open(out, "w", encoding="utf-8") as f:
        json.dump(frag, f, ensure_ascii=False)
    print("fragment: %s" % out, flush=True)


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
    for slug in ("combat-pencak-silat", "combat-pencak-silat-signature"):
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
        assert "karate" not in page.lower(), "sibling leftover in %s" % slug
        assert "combat-karate" not in page, "sibling slug leftover in %s" % slug
        assert "universal build" not in page.lower(), "field leftover in %s" % slug
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
        assert "karate" not in gen_js.lower(), "sibling leftover in gen js %s" % slug
        assert "universal build" not in gen_js.lower(), "field leftover in gen js %s" % slug
        with open(os.path.join(ddir, "gen-%s.js" % slug), "w", encoding="utf-8") as f:
            f.write(gen_js)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)

    write_fragment(built)

    # NOTE: manifest.json / api.json updates are the merger's job - this
    # builder never touches them (concurrency rule).
    print("built %d databases, %d records; manifest/api left for the merger." % (len(built), total))
    return 0


if __name__ == "__main__":
    sys.exit(main())
