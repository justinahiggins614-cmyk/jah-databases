#!/usr/bin/env python3
"""Build The Fear Emotion Database (emotion-fear) and its Signature edition
(emotion-fear-signature) for JAH Databases.

Manon's 2026-10-17 16:15 order: one database per emotion — describe and
simulate the emotion of fear and human behavior. 34 ladder-ordered records
per edition, following the shared emotion template (description ->
first-person simulation -> body signals -> facial expression -> triggers ->
behavior -> healthy expression -> recognizing it in others -> mixes -> full
behavioral simulation).

Public edition: real, fact-checked psychology knowledge — descriptive and
educational only. Never diagnoses real people, never labels any real person,
no clinical language, no diagnostic labels, general safe everyday guidance
only.

Signature edition: the same ladder reframed through the Signature lens —
fear as the early-warning instrument of the Signature system. Titles carry
" (Signature Edition)", src is "signature", clearly labeled Signature-made,
never presented as authentic public record.

Dedupe: every title (public + Signature, 68 total) is checked against the
WHOLE system via DedupeGate before any record is written; zero collisions
required. ID prefixes JAH-EMFE- / JAH-EMFES- verified free in the manifest
id_prefix values and in every shard index file (zero hits) before use.

Pipeline (mirrors component-parts-catalog-build exactly, minus the manifest
and api.json appends which the merger owns):
  records -> shard data (index.jsonl.gz + chunks/chunk-0000.jsonl.gz) ->
  machine-execute all 68 demos -> db pages (index.html + gen-*.js) ->
  merger fragment.

NEVER touches data/manifest.json, api.json, index.html, README.md, or
docs/AI_ACCESS.md. NEVER git commits or pushes.
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
FRAGMENTS = "/home/hatch/workspace/hidden_files/missing-builds/fragments"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_emotion_fear import ENTRIES, SIG_TAIL
from demos_emotion_fear import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, source):
    sig_line = ("Signature originals - his original Signature reading of fear: "
                "fear as the early-warning instrument of the human system, the "
                "first bell in the Signature watchtower, answered with a chosen "
                "move. Clearly labeled Signature-made, never presented as "
                "authentic public record.")
    pub_line = ("Public records - real, fact-checked psychology of fear: what "
                "fear is, how it feels from the inside, body signals, the face "
                "of fear, triggers, behavior, healthy expression, recognizing "
                "fear in others, emotion blends, and full behavioral "
                "simulation - descriptive and educational, organized in the "
                "Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(what fear is, the emotion family, fear at three volumes, "
              "myths, first-person simulation, the arc of fear, low versus "
              "high fear, the fear-anger blend) -> Compounded (a day with "
              "fear, body signals, posture, sleep appetite and energy, "
              "individual differences, the face of fear, face at intensities, "
              "hiding and faking, artist notes, classic triggers, personal "
              "triggers, surprise triggers, chain reactions) -> Advanced "
              "(fear in behavior, words and voice, decisions, escalation, "
              "healthy expression, unhealthy expression, everyday practices, "
              "reading fear in others, supportive responses, mistakes to "
              "avoid, the related-emotions map, blends, full behavioral "
              "simulation).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working scenario-simulator "
                  "demonstration program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search fear, unease, terror, body signals, fight or flight, facial expression, triggers, startle, healthy expression, recognizing fear, emotion blends, behavioral simulation...",
        "chat_ph": "Ask about fear and human behavior...",
        "archive_blurb": ("Seeded %s fear emotion records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled fear emotion studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about fear - what it is, how it feels, body signals, the face of fear, triggers, behavior, healthy expression, reading fear in others, blends with other emotions, and full behavioral simulation." % ai,
        "gen_fields": ["What Fear Is", "How Fear Feels", "Body Signals", "Facial Expression",
                       "Triggers", "Fear in Behavior", "Healthy Expression",
                       "Recognizing Fear in Others", "Emotion Mixes and Simulation"],
        "gen_kind": "fear-emotion-study", "gen_demo_kind": "fear-emotion-demo",
        "source": source,
    }

DBCFG = {}
DBCFG["emotion-fear"] = _cfg(
    "emotion-fear", "The Fear Emotion Database",
    "Understand fear completely: what it is, how it feels from the inside, "
    "the body signals, the face of fear, what triggers it, how it shows in "
    "behavior, how to express it well, how to recognize it in others, how it "
    "blends with other emotions, and full behavioral simulations - real, "
    "fact-checked psychology, descriptive and educational, taught "
    "progressively along the ladder.",
    "emotion record", "JAH-EMFE-", "JAH Fear Emotion Archivist",
    "fear emotion archivist - describing and simulating fear and human behavior "
    "across what fear is, how it feels, body signals, facial expression, "
    "triggers, behavior, healthy expression, recognition in others, emotion "
    "blends, and full behavioral simulation; teaching progressively along the "
    "ladder from foundations through compounded to advanced; answers from many "
    "angles - definition, example, analogy, application, history, how-to - "
    "using only archive data from this system; descriptive and educational "
    "only, never diagnosing any person",
    "public")
DBCFG["emotion-fear-signature"] = _cfg(
    "emotion-fear-signature", "The Fear Emotion Signature Database",
    "His original Signature reading of fear: fear as the early-warning "
    "instrument of the human system, the first bell in the Signature "
    "watchtower. The full ladder - what fear is, how it feels, body signals, "
    "the face, triggers, behavior, healthy expression, recognition, blends, "
    "and full simulation - reframed as Signature science: the alarm is read, "
    "the threat is measured, and the answer is always a chosen move. Clearly "
    "labeled Signature-made, never presented as authentic public record.",
    "emotion record", "JAH-EMFES-", "JAH Fear Emotion Archivist (Signature)",
    "fear emotion archivist - Signature editions: his original Signature "
    "reading of fear as the early-warning instrument of the human system, "
    "clearly labeled Signature-made and never presented as authentic public "
    "record; teaches progressively along the ladder from foundations through "
    "compounded to advanced; answers from many angles - definition, example, "
    "analogy, application, history, how-to - using only archive data from this "
    "system; descriptive and educational only, never diagnosing any person",
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
                       "note": "Working scenario-simulator demonstration program (real, runnable Python)."}
        base.GATE.admit(slug, title, rid)
        recs.append(rec)
    ranks = [r["ladder_rank"] for r in recs]
    assert ranks == sorted(ranks), "records not in ladder order for %s" % slug
    return recs


def write_fragment(built):
    os.makedirs(FRAGMENTS, exist_ok=True)

    def entry(slug, n):
        c = DBCFG[slug]
        is_sig = slug.endswith("-signature")
        return {
            "slug": slug,
            "name": c["name"],
            "tagline": c["tagline"],
            "record_kind": c["record_kind"],
            "id_prefix": c["prefix"],
            "ai_name": c["ai"],
            "local_index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
            "record_count": n,
            "status": "live",
            "full_records": n,
            "index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
            "chunk_pattern": "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz",
            "source": "signature" if is_sig else "public-harvest",
        }

    frag = {
        "public": entry("emotion-fear", len(built["emotion-fear"])),
        "signature": entry("emotion-fear-signature", len(built["emotion-fear-signature"])),
    }
    # task-specified ai_name for the signature edition
    frag["signature"]["ai_name"] = "JAH Fear Emotion Archivist (Signature)"
    path = os.path.join(FRAGMENTS, "emotion-fear.json")
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
    sspec = importlib.util.spec_from_file_location("sweep", sweep_path)
    sweep = importlib.util.module_from_spec(sspec)
    sspec.loader.exec_module(sweep)

    built = {}
    for slug in ("emotion-fear", "emotion-fear-signature"):
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
        assert "component-parts" not in page, "field leftover in %s" % slug
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
        assert "synthetic intelligence" not in gen_js.lower(), "template leftover in gen js %s" % slug
        with open(os.path.join(ddir, "gen-%s.js" % slug), "w", encoding="utf-8") as f:
            f.write(gen_js)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)

    frag_path = write_fragment(built)
    print("fragment: %s" % frag_path, flush=True)
    print("done: 2 databases, %d records. manifest/api.json left for the merger; no commit, no push." % total)
    return 0


if __name__ == "__main__":
    sys.exit(main())
