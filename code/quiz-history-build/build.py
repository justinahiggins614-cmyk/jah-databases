#!/usr/bin/env python3
"""Build the History Quiz databases for JAH Databases
(Manon's 2026-10-17 16:15 order: test then quiz databases with answers
at the bottom).

Two NEW databases, 34 ladder-ordered records each. Every record is ONE
complete quiz: 10 fact-checked history questions, then the 10 answers at
the bottom of the record (his explicit requirement). Ladder order:
easy (ranks 1-3, foundations) -> medium (ranks 4-6, compounded) ->
hard (ranks 7-10, advanced).

  quiz-history              - The History Quiz Database
                              (public-harvest: real, fact-checked history
                              quizzes - ancient, medieval, modern, and
                              world history)
  quiz-history-signature    - The History Quiz Signature Database
                              (his original Signature reading of history:
                              every era a signature mark, every quiz a
                              covenant of memory; src signature, titles
                              suffixed " (Signature Edition)", clearly
                              labeled Signature-made, never presented as
                              authentic public record)

ID prefixes: JAH-QZHI- (public) and JAH-QZHIS- (signature), verified free
in the manifest id_prefix values (zero hits across 2,442 databases) and
in every shard index file in jah-databases-data-1 (zgrep zero hits,
2026-10-17). Slug quiz-history verified free in the manifest.

All 68 titles are run through the whole-system dedupe gate BEFORE
authoring (pre-pass below); zero collisions.

68 demos machine-executed, ALL OK: each demo is a real quiz runner over
the record's own 10 questions and answers (embedded verbatim, so entry
text and demo output always agree), with a deterministic simulated
taker, tight-bounds score asserts (never float exact-equality), and the
full answer reveal. Build asserts the demo printed the question count
and the OK marker.

CONCURRENCY: this build NEVER touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and NEVER git commits or
pushes. A merger handles those. It writes only: db/quiz-history/ and
db/quiz-history-signature/ (index.html + gen-*.js), the shard dirs under
jah-databases-data-1, and the fragment under hidden_files.

Never the words "bat belt" anywhere. No website references. No Facebook.
Screened: nothing hate-adjacent, profane, or inappropriate; no religious
talk - questions are factual history only.
"""
import gzip
import importlib.util
import json
import os
import re
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = "/home/hatch/workspace/jah-databases"
SHARD = "/home/hatch/workspace/jah-databases-data-1"
SHARD_BASE = "https://justinahiggins614-cmyk.github.io/jah-databases-data-1"
TEMPLATE = os.path.join(REPO, "db", "public-synthetic-intelligence", "index.html")
FRAGMENT = "/home/hatch/workspace/hidden_files/missing-builds/fragments/quiz-history.json"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_quiz_history import ENTRIES, SIG_TAIL
from demos_quiz_history import DEMOS

# ---------------------------------------------------------------- DB config
# NOTE: JS hygiene - role/ai_name/greet/search strings are apostrophe-free.

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, source):
    sig_line = ("Signature originals - his original Signature reading of "
                "history: every era a signature mark, every quiz a covenant "
                "of memory, every answer a seal on what was learned. Clearly "
                "labeled Signature-made, never presented as authentic public "
                "record.")
    pub_line = ("Public records - real, fact-checked history quizzes: "
                "ancient history (Egypt, Greece, Rome, Mesopotamia, China, "
                "Persia), medieval history (early Middle Ages, Vikings, "
                "Byzantium, Crusades, feudalism, Mongols, the Black Death, "
                "the Hundred Years War, the Ottomans, late medieval "
                "culture), modern history (Renaissance, exploration, "
                "Reformation, the American and French revolutions, the "
                "Industrial Revolution, the World Wars, the Cold War), and "
                "world history (the Silk Road, the Americas, African "
                "kingdoms, world revolutions, twentieth century milestones) "
                "- every record a full 10-question quiz with the answers at "
                "the bottom, organized in the Signature system.")
    ladder = (" Quizzes are ordered by the teaching ladder: Foundations "
              "(easy quizzes - ancient Egypt basics, Greek origins, Roman "
              "foundations, Mesopotamia, pharaohs and pyramids, Athens and "
              "Sparta, the Renaissance) -> Compounded (medium quizzes - the "
              "Roman Republic, the early Middle Ages, Vikings, the age of "
              "exploration, ancient China, Persia, Byzantium, the "
              "Reformation, the Roman emperors, the Crusades, feudalism, "
              "the American Revolution, the Silk Road) -> Advanced (hard "
              "quizzes - the Mongols, the Black Death, the French "
              "Revolution, the empires of the Americas, the Hundred Years "
              "War, the Ottoman rise, the Industrial Revolution, African "
              "kingdoms, late medieval culture, World War I, world "
              "revolutions, World War II, the Cold War, twentieth century "
              "milestones).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record is one complete quiz: ten questions, "
                  "then the ten answers at the bottom of the record. Take "
                  "each quiz from memory, score yourself, and climb the "
                  "ladder.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search ancient Egypt, Greece, Rome, Mesopotamia, China, Persia, Vikings, Byzantium, Crusades, Mongols, Renaissance, revolutions, world wars, Silk Road...",
        "chat_ph": "Ask about history quizzes...",
        "archive_blurb": ("Seeded %s history quiz records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced. "
                          "Every record is a complete 10-question quiz with answers at the bottom."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, questions, "
                   "answers, standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled history quiz studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about history quizzes - from ancient Egypt, Greece, Rome, Mesopotamia, China, and Persia through the Vikings, Byzantium, the Crusades, feudalism, the Mongols, the Renaissance, the age of exploration, the Reformations and revolutions, to the world wars, the Cold War, the Silk Road, and the great kingdoms of the world." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "quiz", "gen_demo_kind": "quiz-demo",
        "source": source,
    }


DBCFG = {}
DBCFG["quiz-history"] = _cfg(
    "quiz-history", "The History Quiz Database",
    "Test yourself on real history: every record is a complete 10-question "
    "quiz - ancient, medieval, modern, and world history - with the answers "
    "at the bottom. Ladder-ordered from easy to hard.",
    "quiz record", "JAH-QZHI-", "JAH History Quizmaster",
    "history quizmaster - testing knowledge with complete 10-question "
    "history quizzes, answers at the bottom of every record; teaching "
    "progressively along the ladder from foundations through compounded "
    "to advanced; answers from many angles - definition, example, "
    "analogy, application, history, math, how-to - using only archive "
    "data from this system",
    "public")
DBCFG["quiz-history-signature"] = _cfg(
    "quiz-history-signature", "The History Quiz Signature Database",
    "His original Signature reading of history: every era a signature "
    "mark, every quiz a covenant of memory. The full ladder of history "
    "quizzes - ancient, medieval, modern, world - reframed as Signature "
    "science, answers at the bottom of every record. Clearly labeled "
    "Signature-made, never presented as authentic public record.",
    "quiz record", "JAH-QZHIS-", "JAH History Quizmaster (Signature)",
    "history quizmaster - Signature editions: his original Signature "
    "reading of history, every era a signature mark and every quiz a "
    "covenant of memory, clearly labeled Signature-made and never "
    "presented as authentic public record; tests with complete "
    "10-question quizzes, answers at the bottom; teaches progressively "
    "along the ladder from foundations through compounded to advanced; "
    "answers from many angles using only archive data from this system",
    "signature")

base.DBCFG = DBCFG

assert set(DEMOS) == {e["key"] for e in ENTRIES}, "demo map misses entries"


def prepass_dedupe():
    """Whole-system dedupe gate on ALL 68 titles BEFORE authoring."""
    titles = []
    for e in ENTRIES:
        titles.append(("quiz-history", e["name"]))
        titles.append(("quiz-history-signature", e["name"] + " (Signature Edition)"))
    refused = []
    for slug, title in titles:
        hits = [h for h in base.GATE.check(slug, title) if h[0] != slug]
        if hits:
            refused.append((title, hits))
    if refused:
        for title, hits in refused:
            print("  PREPASS REFUSED: %s -> %s" % (title, hits), flush=True)
        raise SystemExit("dedupe pre-pass refused %d titles" % len(refused))
    print("dedupe pre-pass: all 68 titles clear of the whole system", flush=True)


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
            "questions": list(e["questions"]),
            "answers": list(e["answers"]),
            "standards": list(e["standards"]),
            "citations": citations,
            "src": "signature" if sig else "public-harvest",
            "ladder_rank": e["ladder_rank"],
            "ladder_tier": e["ladder_tier"],
        }
        demo_fn = DEMOS[e["key"]]
        program = demo_fn(base._hdr, title, rid, e["group"],
                          e["questions"], e["answers"])
        rec["demo"] = {"kind": "python", "language": "python",
                       "program": program,
                       "note": "Working demonstration program (real, runnable Python): "
                               "runs this quiz, scores a simulated taker, and reveals the answers."}
        base.GATE.admit(slug, title, rid)
        recs.append(rec)
    ranks = [r["ladder_rank"] for r in recs]
    assert ranks == sorted(ranks), "records not in ladder order for %s" % slug
    return recs


def node_check(path, label):
    with open(path, "r", encoding="utf-8") as f:
        src = f.read()
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as tf:
        tf.write(src)
        tmp = tf.name
    p = subprocess.run(["node", "--check", tmp], capture_output=True, text=True, timeout=60)
    os.unlink(tmp)
    assert p.returncode == 0, "node --check failed for %s: %s" % (label, p.stderr[-500:])
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

    # JS hygiene pre-check: apostrophe-free cfg strings
    for slug, cfg in DBCFG.items():
        for k in ("ai", "role", "greet", "search_ph", "chat_ph"):
            assert "'" not in cfg[k], "apostrophe in %s.%s" % (slug, k)

    prepass_dedupe()

    built = {}
    for slug in ("quiz-history", "quiz-history-signature"):
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
                      "questions", "answers", "standards", "citations",
                      "src", "ladder_rank", "ladder_tier", "demo"):
                assert k in r, "missing %s in %s" % (k, r["id"])
            prog = r["demo"].get("program")
            assert prog and len(r["description"]) > 200, "stub in %s" % r["id"]
            assert len(r["questions"]) == 10 and len(r["answers"]) == 10, \
                "not 10+10 in %s" % r["id"]
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

    # machine-execute all 68 demos; cross-check entry text vs demo output
    for slug, recs in built.items():
        for r in recs:
            prog = r["demo"]["program"]
            p = subprocess.run([sys.executable, "-c", prog],
                               capture_output=True, text=True, timeout=180)
            assert p.returncode == 0, "demo failed %s: %s" % (r["id"], p.stderr[-800:])
            assert "OK:" in p.stdout, "demo no OK marker %s" % r["id"]
            assert "questions: 10" in p.stdout, "demo question-count mismatch %s" % r["id"]
            assert "answers at the bottom" in p.stdout, "demo reveal missing %s" % r["id"]
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
            tier = {"foundations": "Foundations", "compounded": "Compounded",
                    "advanced": "Advanced"}[r["ladder_tier"]]
            topics.setdefault(tier, []).append("%s - %s" % (r["t"], r["g"]))
        gen_js = nb.build_gen_js(slug, topics, DBCFG[slug])
        assert "facebook" not in gen_js.lower() and "bat belt" not in gen_js.lower()
        assert "universal build" not in gen_js.lower(), "field leftover in gen js %s" % slug
        gpath = os.path.join(ddir, "gen-%s.js" % slug)
        with open(gpath, "w", encoding="utf-8") as f:
            f.write(gen_js)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)

    # node --check on extracted page scripts + gen js
    for slug in built:
        ppath = os.path.join(REPO, "db", slug, "index.html")
        with open(ppath, "r", encoding="utf-8") as f:
            page = f.read()
        scripts = re.findall(
            r'<script(?![^>]*type="application/ld\+json")[^>]*>(.*?)</script>',
            page, flags=re.S)
        assert scripts, "no page scripts found in %s" % slug
        for i, s in enumerate(scripts):
            if s.strip():
                node_check_content(s, "db/%s/index.html script#%d" % (slug, i))
        node_check(os.path.join(REPO, "db", slug, "gen-%s.js" % slug),
                   "gen-%s.js" % slug)

    # fragment for the merger
    frag = {"public": {
                "slug": "quiz-history",
                "name": "The History Quiz Database",
                "tagline": DBCFG["quiz-history"]["tagline"],
                "record_kind": "quiz record",
                "id_prefix": "JAH-QZHI-",
                "ai_name": "JAH History Quizmaster",
                "local_index": SHARD_BASE + "/data/quiz-history/index.jsonl.gz",
                "record_count": 34, "status": "live", "full_records": 34,
                "index": SHARD_BASE + "/data/quiz-history/index.jsonl.gz",
                "chunk_pattern": "data/quiz-history/chunks/chunk-NNNN.jsonl.gz",
                "source": "public-harvest"},
            "signature": {
                "slug": "quiz-history-signature",
                "name": "The History Quiz Signature Database",
                "tagline": DBCFG["quiz-history-signature"]["tagline"],
                "record_kind": "quiz record",
                "id_prefix": "JAH-QZHIS-",
                "ai_name": "JAH History Quizmaster (Signature)",
                "local_index": SHARD_BASE + "/data/quiz-history-signature/index.jsonl.gz",
                "record_count": 34, "status": "live", "full_records": 34,
                "index": SHARD_BASE + "/data/quiz-history-signature/index.jsonl.gz",
                "chunk_pattern": "data/quiz-history-signature/chunks/chunk-NNNN.jsonl.gz",
                "source": "signature"}}
    os.makedirs(os.path.dirname(FRAGMENT), exist_ok=True)
    with open(FRAGMENT, "w", encoding="utf-8") as f:
        json.dump(frag, f, indent=1, ensure_ascii=False)
        f.write("\n")
    print("fragment: %s" % FRAGMENT, flush=True)

    print("manifest/api.json/index.html/README/AI_ACCESS untouched (merger handles).")
    print("DONE: 2 databases, %d records, 68 demos OK, node --check clean." % total)
    return 0


def node_check_content(src, label):
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as tf:
        tf.write(src)
        tmp = tf.name
    p = subprocess.run(["node", "--check", tmp], capture_output=True, text=True, timeout=60)
    os.unlink(tmp)
    assert p.returncode == 0, "node --check failed for %s: %s" % (label, p.stderr[-500:])
    print("node --check clean: %s" % label, flush=True)


if __name__ == "__main__":
    sys.exit(main())
