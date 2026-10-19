#!/usr/bin/env python3
"""Build the Snake Kung Fu Combat databases for JAH Databases
(combat batch 4, final round).

Shequan (snake fist) - snake hand and finger strikes, coiling evasions,
low stances, vital-point striking theory in educational anatomy context,
snake forms in sequence, chi development exercises, applications - each
record a technique with HOW TO DO IT (step-by-step body mechanics),
ladder-ordered from basics to advanced. Civilian traditional-art scope.

Concurrency: this builder verified ~/workspace/hidden_files/db-writer-free.marker
exists before writing. It NEVER touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and never git commits or
pushes - a merger handles those. It only creates:
  db/combat-snake-kung-fu/ + db/combat-snake-kung-fu-signature/
      (index.html + gen-*.js each)
  code/combat-snake-kung-fu-build/{build.py, entries_*.py, demos_*.py}
  jah-databases-data-1/data/combat-snake-kung-fu/ + -signature/
      (index.jsonl.gz + chunks/chunk-0000.jsonl.gz)
  ~/workspace/hidden_files/missing-builds/fragments/combat-snake-kung-fu.json

Dedupe: all 68 titles (34 public + 34 Signature Edition) checked against
the DedupeGate over the whole system before authoring - zero refusals.
ID prefixes JAH-CBSNK- / JAH-CBSNKS- verified free in the manifest
id_prefix values and in all shard index files of jah-databases-data-1
(zero hits for "JAH-CBSNK"). Slugs verified absent from the manifest.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_snake_kung_fu.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos.

Never the words "bat belt" anywhere. No website references. No Facebook.
No religious talk. Civilian traditional-art instruction only.
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
FRAGMENT = "/home/hatch/workspace/hidden_files/missing-builds/fragments/combat-snake-kung-fu.json"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_snake_kung_fu import ENTRIES, SIG_TAIL
from demos_snake_kung_fu import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Serpent "
                "Method: every coil a signed circuit, every strike a "
                "signature written in motion, the serpent the seal of "
                "the system. Clearly labeled Signature-made, never "
                "presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked snake style kung fu "
                "(She Quan): the salute and resting posture, the snake "
                "tongue hand and snake head palm, waist coiling, finger "
                "conditioning, gliding footwork, coiling deflections, the "
                "low snake stance, darting strikes, coiling evasions, "
                "four snake forms in sequence, vital-point theory as "
                "educational anatomy, chi development exercises, and "
                "partner-safe applications - every record a full "
                "technique with step-by-step how-to, taught "
                "progressively along the ladder.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(the snake salute, resting posture, tongue hand, snake "
              "head palm, waist warmup, finger conditioning, snake step, "
              "coiling deflection, low snake stance, double tongue "
              "strike, tail whip, precision eye flicks) -> Compounded "
              "(coiling arm strike, creep-down transitions, darting head "
              "strike, entwining the branch, rising serpent, vital-point "
              "theory I and II, snake forms one and two, snake breathing, "
              "coiling evasion, double-headed snake, snake against the "
              "crane) -> Advanced (snake form three, iron finger "
              "conditioning, coiling silk energy, spear hand, serpent "
              "strikes the water, vital-point partner-safe drills, "
              "python coils, snake form four, the master sequence).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search snake tongue hand, snake head palm, coiling deflection, low snake stance, darting head strike, vital-point theory, snake breathing, iron finger, spear hand, python coils, nine-bend serpent...",
        "chat_ph": "Ask about snake style kung fu...",
        "archive_blurb": ("Seeded %s snake style kung fu combat records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled snake style kung fu studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about snake style kung fu - from the salute, tongue hand, and coiling basics through the four snake forms, vital-point theory, and chi development, to the advanced spear hand, python coils, and the master sequence." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "snake-kung-fu-study", "gen_demo_kind": "snake-kung-fu-demo",
        "source": source,
    }

CIT_PUB = ("Snake style kung fu, She Quan (standard references: Shahar M. "
           "The Shaolin Monastery: History, Religion, and the Chinese "
           "Martial Arts. University of Hawaii Press; 2008; Wong Kiew Kit. "
           "The Art of Shaolin Kung Fu. Tuttle Publishing; 2002; Yang "
           "Jwing-Ming. Shaolin Long Fist Kung Fu. YMAA Publication "
           "Center; 2008; Yang Jwing-Ming. The Root of Chinese Qigong. "
           "YMAA Publication Center; 1997; Chow D, Spangler R. Kung Fu: "
           "History, Philosophy, and Technique. Unique Publications; "
           "1982; Smith RW. Chinese Boxing: Masters and Methods. Kodansha "
           "International; 1974; Clark R. Pressure Point Fighting: A "
           "Guide to the Secret Heart of Asian Martial Arts. Tuttle "
           "Publishing; 2001; Reid H, Croucher M. The Way of the "
           "Warrior: The Paradox of the Martial Arts. Overlook Press; "
           "1983).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature "
                     "Serpent Method - every coil a signed circuit, every "
                     "strike a signature written in motion - clearly "
                     "labeled Signature-made.")

DBCFG = {}
DBCFG["combat-snake-kung-fu"] = _cfg(
    "combat-snake-kung-fu", "Snake Kung Fu Combat Database",
    "Snake style kung fu (She Quan): snake hand and finger strikes, "
    "coiling evasions, low stances, vital-point striking theory in "
    "educational anatomy context, snake forms in sequence, chi "
    "development exercises, and applications. Real, fact-checked "
    "traditional martial arts knowledge with Chinese terminology and "
    "translations, every record a full technique with step-by-step "
    "how-to, taught progressively along the ladder from basic hand "
    "shapes to the master sequence.",
    "combat technique record", "JAH-CBSNK-", "JAH Snake Kung Fu Combat Archivist",
    "snake style kung fu combat archivist - teaching the salute and "
    "resting posture, snake tongue hand and snake head palm, waist "
    "coiling, finger conditioning, gliding footwork, coiling "
    "deflections, low stances, darting strikes, coiling evasions, the "
    "four snake forms in sequence, vital-point theory as educational "
    "anatomy, chi development, and partner-safe applications with "
    "step-by-step how-to; teaching progressively along the ladder from "
    "foundations through compounded to advanced; answers from many "
    "angles - definition, example, analogy, application, history, math, "
    "how-to - using only archive data from this system",
    CIT_PUB, "public")
DBCFG["combat-snake-kung-fu-signature"] = _cfg(
    "combat-snake-kung-fu-signature", "Snake Kung Fu Combat Signature Database",
    "His original Signature Serpent Method: every coil a signed circuit, "
    "every strike a signature written in motion, the serpent the seal of "
    "the system. The full ladder from the salute and hand shapes through "
    "coiling evasions, the four snake forms, and chi development to the "
    "spear hand, python coils, and the master sequence, reframed as "
    "Signature science. Clearly labeled Signature-made, never presented "
    "as authentic public record.",
    "combat technique record", "JAH-CBSNKS-", "JAH Snake Kung Fu Combat Archivist (Signature)",
    "snake style kung fu combat archivist - Signature editions: his "
    "original Signature Serpent Method, every coil a signed circuit and "
    "every strike a signature written in motion, clearly labeled "
    "Signature-made and never presented as authentic public record; "
    "teaches progressively along the ladder from foundations through "
    "compounded to advanced; answers from many angles - definition, "
    "example, analogy, application, history, math, how-to - using only "
    "archive data from this system",
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
    for slug in ("combat-snake-kung-fu", "combat-snake-kung-fu-signature"):
        cfg = DBCFG[slug]
        key = "signature" if slug.endswith("-signature") else "public"
        frag[key] = {
            "slug": slug, "name": cfg["name"], "tagline": cfg["tagline"],
            "record_kind": cfg["record_kind"], "id_prefix": cfg["prefix"],
            "ai_name": cfg["ai"],
            "local_index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
            "record_count": len(built[slug]), "status": "live",
            "full_records": len(built[slug]),
            "index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
            "chunk_pattern": "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz",
            "source": cfg["source"],
        }
    os.makedirs(os.path.dirname(FRAGMENT), exist_ok=True)
    with open(FRAGMENT, "w", encoding="utf-8") as f:
        json.dump(frag, f, ensure_ascii=False, sort_keys=True)
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
    for slug in ("combat-snake-kung-fu", "combat-snake-kung-fu-signature"):
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
    # NOTE (concurrency): manifest.json, api.json, index.html, README.md,
    # docs/AI_ACCESS.md are NEVER touched here, and nothing is committed
    # or pushed - the merger handles those.
    print("built 2 databases, %d records total; merger handles manifest/api/pages." % total)
    return 0


if __name__ == "__main__":
    sys.exit(main())
