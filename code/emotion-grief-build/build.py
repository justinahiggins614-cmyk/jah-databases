#!/usr/bin/env python3
"""Build The Grief Emotion Database (public) and The Grief Emotion
Signature Database (Signature edition) for JAH Databases.

Manon's 2026-10-17 16:15 order, emotion series batch 1: one database per
emotion; the archive must be able to describe or simulate emotions and
human behavior. Follows the shared emotion template
(~/workspace/hidden_files/new-orders-1540/emotion-template.md): what
grief IS -> first-person simulation -> body signals -> facial expression
-> triggers -> behavior -> healthy expression -> recognizing it in
others -> related emotions and mixes -> complex behavioral simulation.

Public records are real, fact-checked psychology knowledge - descriptive
and educational only: the archive describes and simulates the emotion of
grief; it never diagnoses real people and never labels any real person
with an emotional state. Handled with exceptional care, warmth, and
respect.

Signature records are the same 34-record ladder through the Signature
lens (his original Signature interpretation: grief as the covenant paid
in full measure, the torn thread and the reweaving). Titles suffixed
" (Signature Edition)", src "signature", SIG_TAIL marks them as
Signature-made, never presented as authentic public record.

ID prefixes: JAH-EMGR- (public) and JAH-EMGRS- (signature), verified free
in the manifest id_prefix values (zero hits) and in every shard index
file of jah-databases-data-1 (863 index.jsonl.gz files, zero hits).

34 records each, ordered by the teaching ladder (ladder_rank 1-10
non-decreasing, ladder_tier foundations/compounded/advanced); the shard
index is written in ladder order so pages present simple -> compounded
-> complex.

Demos are emotion-scenario simulators: real, runnable, stdlib-only
Python performing the actual simulation for each record. All 68 are
machine-executed by this build: each prints its real computed values,
asserts tight bounds (never float exact-equality), and ends with the OK
marker.

Never the words "bat belt" anywhere. No website references. No Facebook.
This build never touches data/manifest.json, api.json, index.html,
README.md, or docs/AI_ACCESS.md, and never commits or pushes - a merger
handles those. It only creates: db/emotion-grief/ +
db/emotion-grief-signature/ (index.html + gen-*.js each), the shard data
under jah-databases-data-1, and the missing-builds fragment.
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
FRAGMENT = "/home/hatch/workspace/hidden_files/missing-builds/fragments/emotion-grief.json"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_emotion_grief import ENTRIES, SIG_TAIL
from demos_emotion_grief import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature interpretation "
                "of grief: every loss a torn thread in the weave, every grief "
                "the price of a covenant kept, every healing a reweaving. "
                "Clearly labeled Signature-made, never presented as authentic "
                "public record.")
    pub_line = ("Public records - real, fact-checked psychology of grief: "
                "what grief is, how it feels from the inside, its body "
                "signals and facial expressions, its triggers, how it shows "
                "in behavior, healthy expression, recognizing it in others, "
                "and its related emotions and mixes - descriptive and "
                "educational only, never diagnosing any real person.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(what grief is, where it sits in the emotion family, its "
              "volumes, its myths, the first-person passage, its time "
              "course) -> Compounded (low vs high intensity snapshots, "
              "blends with partner emotions, a day in the life, body "
              "signals, posture, sleep appetite and energy, how bodies "
              "differ, the face of grief, expression intensity, hiding and "
              "faking, gallery notes, classic triggers) -> Advanced "
              "(personal triggers, surprise triggers, chain reactions, "
              "behavior, speech, decisions, escalation, healthy and "
              "unhealthy expression, everyday practices, reading the "
              "signs, supportive responses, mistakes to avoid, the related "
              "emotions map, emotion mixes, the full behavioral "
              "simulation).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working emotion-scenario "
                  "simulator program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search grief definition, first person, body signals, facial expression, triggers, behavior, healthy expression, recognizing grief, mixes, simulation...",
        "chat_ph": "Ask about grief...",
        "archive_blurb": ("Seeded %s grief emotion records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled grief emotion studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about grief - what it is, how it feels, its body signals and expressions, its triggers, its behavior, healthy expression, recognizing it in others, and its mixes." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "grief-emotion-study", "gen_demo_kind": "grief-emotion-demo",
        "source": source,
    }

CIT_PUB = ("Grief psychology (standard references: Kubler-Ross E. On Death "
           "and Dying. Macmillan; 1969; Bowlby J. Attachment and Loss, Vol. "
           "3. Basic Books; 1980; Stroebe M, Schut H. The dual process model "
           "of coping with bereavement. Death Studies; 1999; Worden JW. "
           "Grief Counseling and Grief Therapy. 4th ed. Springer; 2008; "
           "Bonanno GA. The Other Side of Sadness. Basic Books; 2009; "
           "Neimeyer RA, ed. Meaning Reconstruction and the Experience of "
           "Loss. APA; 2001; Parkes CM. Bereavement. 3rd ed. Routledge; "
           "1996; Shear MK. Complicated grief. NEJM; 2015; Ekman P. Emotions "
           "Revealed. Times Books; 2003; Plutchik R. Emotion: A "
           "Psychoevolutionary Synthesis. Harper and Row; 1980; American "
           "Psychological Association. APA Dictionary of Psychology. 2nd ed; "
           "2015). Descriptive and educational only; never diagnosing any "
           "real person.")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature "
                     "interpretation of grief - clearly labeled "
                     "Signature-made, never presented as authentic public "
                     "record.")

DBCFG = {}
DBCFG["emotion-grief"] = _cfg(
    "emotion-grief", "The Grief Emotion Database",
    "Grief, described and simulated: what it is, how it feels from the "
    "inside, its body signals and facial expressions, its triggers, how "
    "it shows in behavior, healthy expression, recognizing it in others, "
    "and its related emotions and mixes - 34 ladder-ordered records with "
    "working emotion-scenario simulators.",
    "emotion record", "JAH-EMGR-", "JAH Grief Emotion Archivist",
    "grief emotion archivist - describing and simulating the emotion of "
    "grief, teaching progressively along the ladder from foundations "
    "through compounded to advanced; answers from many angles - "
    "definition, example, analogy, application, history, psychology, "
    "how-to - using only archive data from this system; descriptive and "
    "educational only, never diagnosing any real person",
    CIT_PUB, "public")
DBCFG["emotion-grief-signature"] = _cfg(
    "emotion-grief-signature", "The Grief Emotion Signature Database",
    "His original Signature interpretation of grief: every loss a torn "
    "thread in the weave, every grief the price of a covenant kept, "
    "every healing a reweaving. The full ladder - what grief is, how it "
    "feels, body and face, triggers, behavior, healthy expression, "
    "recognition, mixes, and the full simulation - reframed as Signature "
    "science. Clearly labeled Signature-made, never presented as "
    "authentic public record.",
    "emotion record", "JAH-EMGRS-", "JAH Grief Emotion Archivist (Signature)",
    "grief emotion archivist - Signature editions: his original Signature "
    "interpretation of grief, clearly labeled Signature-made and never "
    "presented as authentic public record; teaches progressively along "
    "the ladder from foundations through compounded to advanced; answers "
    "from many angles - definition, example, analogy, application, "
    "history, psychology, how-to - using only archive data from this "
    "system; descriptive and educational only, never diagnosing any real "
    "person",
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
                       "note": "Working emotion-scenario simulator (real, runnable Python)."}
        base.GATE.admit(slug, title, rid)
        recs.append(rec)
    ranks = [r["ladder_rank"] for r in recs]
    assert ranks == sorted(ranks), "records not in ladder order for %s" % slug
    return recs


def write_fragment(built):
    frag = {"public": {}, "signature": {}}
    for slug, recs in built.items():
        cfg = DBCFG[slug]
        entry = {
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
            "source": cfg["source"] if cfg["source"] == "signature" else "public-harvest",
        }
        frag["signature" if slug.endswith("-signature") else "public"] = entry
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
    for slug in ("emotion-grief", "emotion-grief-signature"):
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
        needle = ("Generate structural synthetic intelligence studies. Seeded archive records "
                  "are the authoritative entries.")
        assert needle in page, "gen_desc needle missing in template"
        page = page.replace(needle, DBCFG[slug]["gen_desc"])
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
    print("built %d databases, %d records total" % (len(built), total))
    print("NOTE: manifest/api.json/index.html/README/docs untouched (merger handles); no commit, no push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
