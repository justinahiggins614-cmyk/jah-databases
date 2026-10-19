#!/usr/bin/env python3
"""Build the Sadness Emotion databases for JAH Databases
(Manon's 2026-10-17 16:15 order, emotion series batch 1).

The archive must be able to describe and simulate emotions and human
behavior. This database covers sadness: what it is, how it feels from the
inside (first-person simulation), body signals, the sad face, triggers,
behavior, healthy expression, reading it in others, related emotions and
mixes, and a full trigger-to-resolution behavioral simulation.
Descriptive and educational ONLY - never diagnosing real people.

Dedupe: 2026-10-17 - all 68 titles checked against the whole system via
code/dedupe_gate.py (manifest databases + global exact shards): zero
collisions, zero refusals.

Two NEW databases, 34 ladder-ordered records each:

  emotion-sadness              - The Sadness Emotion Database
                                 (public-harvest: real, fact-checked
                                 psychology of sadness - definition,
                                 emotion-family placement, intensity
                                 volumes, myths, first-person passages,
                                 timelines, body signals, posture, sleep,
                                 facial expression, triggers, cascades,
                                 behavior, speech, decisions, escalation,
                                 healthy expression, practices, reading
                                 others, support, relatives, mixes, full
                                 simulation; standard references Darwin
                                 1872; Ekman 2003; Plutchik 1991; Lazarus
                                 1991; Izard 1991; Frijda 1986; Panksepp
                                 1998; Barrett 2017; Bonanno 2009; Gross
                                 2007; Keltner 2019; Fredrickson 2009)
  emotion-sadness-signature    - The Sadness Emotion Signature Database
                                 (his original Signature emotional
                                 science: sadness as the archive's signal
                                 of lost value, the mind weighing what
                                 mattered and marking the record; src
                                 signature, titles suffixed " (Signature
                                 Edition)", never presented as authentic
                                 public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-EMSA- (public) and JAH-EMSAS- (signature), verified free
in the manifest id_prefix values and with zero hits in every shard index
file.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_emotion_sadness.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos.

Concurrency: this builder writes ONLY its own new untracked paths -
db/emotion-sadness/, db/emotion-sadness-signature/,
code/emotion-sadness-build/, the data-1 shard dirs, and the fragment
file. It never touches data/manifest.json, api.json, index.html,
README.md, docs/AI_ACCESS.md, and never commits or pushes. A merger
handles those.

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
from entries_emotion_sadness import ENTRIES, SIG_TAIL
from demos_emotion_sadness import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature emotional "
                "science: sadness as the archive's signal of lost value, "
                "the mind weighing what mattered, measuring the gap, and "
                "marking the record so the lesson is kept. Clearly labeled "
                "Signature-made, never presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked psychology of sadness: "
                "what the emotion is, where it sits in the emotion family, "
                "intensity volumes, myths, first-person feeling, timelines, "
                "body signals, posture, sleep, the sad face, triggers, "
                "cascades, behavior, speech, decisions, escalation, healthy "
                "expression, everyday practices, reading others, support, "
                "relatives, mixes, and the full trigger-to-resolution "
                "simulation - descriptive and educational only, never "
                "diagnosing real people; organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(what sadness is, the emotion family, intensity volumes, "
              "myths, the inside-the-feeling passage, the timeline, "
              "low-versus-high snapshots, the loneliness blend, the "
              "ordinary-day vignette, body signals, posture, sleep, no two "
              "bodies alike) -> Compounded (the sad face, the face at "
              "different intensities, hiding and leakage, drawing sadness, "
              "classic triggers, personal triggers, surprise triggers, "
              "chain reactions, sad actions, the sad voice, sad decisions, "
              "escalation) -> Advanced (healthy expression, the two costly "
              "exits, everyday practices, reading others, what helps, what "
              "backfires, the relatives map, the four blends, the full "
              "simulation).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search sadness, feeling sad, emotion family, intensity, body signals, sad face, triggers, behavior, healthy expression, reading others, grief, disappointment, melancholy, emotion mixes, simulations...",
        "chat_ph": "Ask about the sadness emotion...",
        "archive_blurb": ("Seeded %s sadness emotion records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled sadness emotion studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about sadness - from what it is and where it sits in the emotion family through intensity volumes, the inside-the-feeling passage, timelines, body signals, posture, sleep, the sad face, hiding and leakage, triggers, cascades, behavior, the sad voice, decisions, and escalation, to healthy expression, everyday practices, reading others, support, relatives, blends, and the full trigger-to-resolution simulation." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "emotion-sadness-study", "gen_demo_kind": "emotion-sadness-demo",
        "source": source,
    }

CIT_PUB = ("Psychology of emotion (standard references: Darwin C. The "
           "Expression of the Emotions in Man and Animals. John Murray; "
           "1872; Ekman P. Emotions Revealed. Times Books; 2003; Plutchik "
           "R. The Emotions. Rev. ed. University Press of America; 1991; "
           "Lazarus RS. Emotion and Adaptation. Oxford University Press; "
           "1991; Izard CE. The Psychology of Emotions. Plenum Press; "
           "1991; Frijda NH. The Emotions. Cambridge University Press; "
           "1986; Panksepp J. Affective Neuroscience. Oxford University "
           "Press; 1998; Barrett LF. How Emotions Are Made. Houghton "
           "Mifflin Harcourt; 2017; Bonanno GA. The Other Side of Sadness. "
           "Basic Books; 2009; Gross JJ, editor. Handbook of Emotion "
           "Regulation. Guilford Press; 2007; Keltner D, Oatley K, Jenkins "
           "JM. Understanding Emotions. 4th ed. Wiley; 2019; Fredrickson "
           "BL. Positivity. Crown Publishers; 2009). Descriptive and "
           "educational only; never diagnosing real people.")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature "
                     "emotional science - sadness as the archive's signal "
                     "of lost value - clearly labeled Signature-made.")

DBCFG = {}
DBCFG["emotion-sadness"] = _cfg(
    "emotion-sadness", "The Sadness Emotion Database",
    "Describe and simulate sadness: what it is, how it feels from the "
    "inside, body signals, the sad face, triggers, behavior, healthy "
    "expression, reading it in others, related emotions and mixes, and a "
    "full trigger-to-resolution simulation - real, fact-checked psychology "
    "taught progressively along the ladder, descriptive and educational "
    "only.",
    "emotion record", "JAH-EMSA-", "JAH Sadness Emotion Archivist",
    "sadness emotion archivist - describing and simulating the sadness "
    "emotion: what it is, the emotion family, intensity volumes, myths, "
    "first-person feeling, timelines, body signals, posture, sleep, facial "
    "expression, triggers, cascades, behavior, speech, decisions, "
    "escalation, healthy expression, everyday practices, reading others, "
    "support, relatives, mixes, and full simulation; teaching progressively "
    "along the ladder from foundations through compounded to advanced; "
    "answers from many angles - definition, example, analogy, application, "
    "history, how-to - using only archive data from this system",
    CIT_PUB, "public")
DBCFG["emotion-sadness-signature"] = _cfg(
    "emotion-sadness-signature", "The Sadness Emotion Signature Database",
    "His original Signature emotional science of sadness: the archive's "
    "signal of lost value, the mind weighing what mattered and marking "
    "the record. The full ladder from what sadness is through the "
    "inside-the-feeling passages, body signals, the sad face, triggers, "
    "and behavior, to healthy expression, reading others, relatives, "
    "blends, and the full simulation, reframed as Signature science. "
    "Clearly labeled Signature-made, never presented as authentic public "
    "record.",
    "emotion record", "JAH-EMSAS-", "JAH Sadness Emotion Archivist (Signature)",
    "sadness emotion archivist - Signature editions: his original "
    "Signature emotional science of sadness as the archive signal of "
    "lost value, clearly labeled Signature-made and never presented as "
    "authentic public record; teaches progressively along the ladder from "
    "foundations through compounded to advanced; answers from many angles "
    "- definition, example, analogy, application, history, how-to - using "
    "only archive data from this system",
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
        side = "signature" if slug.endswith("-signature") else "public"
        frag[side] = {
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
            "source": "signature" if side == "signature" else "public-harvest",
        }
    path = "/home/hatch/workspace/hidden_files/missing-builds/fragments/emotion-sadness.json"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(frag, f, indent=1, ensure_ascii=False)
        f.write("\n")
    print("fragment: %s" % path, flush=True)


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
    for slug in ("emotion-sadness", "emotion-sadness-signature"):
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
    print("records: %d public + %d signature = %d total" %
          (len(built["emotion-sadness"]),
           len(built["emotion-sadness-signature"]), total))
    print("NOTE: manifest.json / api.json / restamp left to the merger; no commit, no push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
