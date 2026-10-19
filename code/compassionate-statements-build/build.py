#!/usr/bin/env python3
"""Build the Compassionate Statements databases for JAH Databases
(Manon's 2026-10-17 16:15 fun/social batch).

Two NEW databases, 34 ladder-ordered records each:

  compassionate-statements            - The Compassionate Statements Database
                                        (public-harvest: real, generatable
                                        comfort craft - words of comfort,
                                        empathy, and support for grief,
                                        hardship, illness, and struggle;
                                        each record a statement WITH
                                        guidance on when and how to say it
                                        genuinely; tender and sincere only,
                                        never platitudes, never minimizing)
  compassionate-statements-signature  - The Compassionate Statements
                                        Signature Database
                                        (compassion as covenant: the comfort
                                        given is a promise kept, tenderness
                                        is strength, presence is the
                                        Signature vow; src signature,
                                        titles suffixed " (Signature
                                        Edition)", never presented as
                                        authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced): simple comfort ->
hardship and illness -> deep grief support. The shard index is written
in ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-CSTT- (public) and JAH-CSTTS- (signature), verified
free in the manifest id_prefix values and in every shard index of
jah-databases-data-1 (zero hits, 2026-10-17).

Dedupe: all 68 titles (34 public + 34 signature variants) run through
code/dedupe_gate.py against the WHOLE system before authoring - zero
collisions, zero refusals.

Demos: 34 distinct demo programs (statement pickers, situation
matchers, minimizing-language scanners, warmth/specificity/continuity
metrics, follow-up cadence, readability), each analyzing its own
record's statement text verbatim. All machine-executed by this build:
each prints real computed values, asserts tight bounds (never float
exact-equality), ends with the OK marker. build_records cross-checks
that each entry's statement appears verbatim in its demo program.

CONCURRENCY: this build NEVER touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and never git commits or
pushes. A merger handles those from the fragment written to
~/workspace/hidden_files/missing-builds/fragments/.

Never the words "bat belt" anywhere. No website references. No
Facebook. No religious talk. Screened: nothing hate-adjacent,
profane, or inappropriate.
"""
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
FRAG_PATH = "/home/hatch/workspace/hidden_files/missing-builds/fragments/compassionate-statements.json"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_compassionate_statements import ENTRIES, SIG_TAIL
from demos_compassionate_statements import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - compassion as covenant: the comfort "
                "given is a promise kept, tenderness is strength, and "
                "presence is the Signature vow, from simple comfort "
                "through hardship and illness to deep grief support. "
                "Clearly labeled Signature-made, never presented as "
                "authentic public record.")
    pub_line = ("Public records - real, generatable comfort craft: words "
                "of comfort, empathy, and support for grief, hardship, "
                "illness, and struggle, each record a statement with "
                "guidance on when and how to say it genuinely - tender "
                "and sincere, never platitudes, never minimizing, "
                "organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(simple presence, naming what you see, permission to feel, "
              "honest admission, listening first, hard days, honoring "
              "effort, disappointment, visiting the sick, comfort after "
              "mistakes, fear, exhaustion, pain without fixing, "
              "loneliness, caregivers, shattered plans) -> Compounded "
              "(first hours of grief, job loss, difficult diagnosis, "
              "separation, returning grief, comforting children, "
              "financial hardship, chronic illness, anger in grief, "
              "regret, unworthiness, the long goodbye) -> Advanced "
              "(sudden loss, supporting survivors, loss of a child, "
              "complicated grief, when words run out, the long "
              "companion).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: the statement, when to say it, how to say it, "
                  "description, how it works, key points, requirements, standards, citations, and a working "
                  "demonstration program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search comfort for grief, loss, illness, fear, exhaustion, loneliness, job loss, diagnosis, anger, regret, presence...",
        "chat_ph": "Ask about comforting someone...",
        "archive_blurb": ("Seeded %s compassionate statement records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, statement, when_to_say, how_to_say, description, how_it_works, "
                   "key_points, requirements, standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled compassionate statement studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about comforting someone - from simple presence, naming hard things, permission to feel, honest admission, and listening first, through hard days, effort, disappointment, visiting the sick, mistakes, fear, exhaustion, unfixable pain, loneliness, caregivers, and shattered plans, through first grief, job loss, diagnosis, separation, returning grief, children, money trouble, chronic illness, anger, regret, unworthiness, and the long goodbye, to sudden loss, survivors, the loss of a child, complicated grief, silence, and the long companion." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "compassionate-statement-study", "gen_demo_kind": "compassionate-statement-demo",
        "source": source,
    }

CIT_PUB = ("Comfort and grief communication (standard references: Rogers "
           "CR. On Becoming a Person. Houghton Mifflin; 1961; Kubler-Ross "
           "E, Kessler D. On Grief and Grieving. Scribner; 2014; Worden JW. "
           "Grief Counseling and Grief Therapy. 5th ed. Springer; 2018; "
           "Neimeyer RA, ed. Techniques of Grief Therapy. Routledge; 2012; "
           "Crowe K, McDowell E. There Is No Good Card for This. Dey "
           "Street; 2017; Goldman S. Ring Theory: comfort in, dump out. "
           "Los Angeles Times; 2013; VitalTalk serious illness "
           "communication curriculum: NURSE statements; American "
           "Psychological Association. Grief: Coping with the loss of "
           "your loved one.).")
CIT_SIG = CIT_PUB + (" Signature editions are compassion as covenant - the "
                     "comfort given is a promise kept, tenderness is "
                     "strength, presence is the Signature vow - clearly "
                     "labeled Signature-made.")

DBCFG = {}
DBCFG["compassionate-statements"] = _cfg(
    "compassionate-statements", "The Compassionate Statements Database",
    "Words of comfort, empathy, and support for grief, hardship, illness, "
    "and struggle: real, generatable compassionate statements, each with "
    "guidance on when and how to say it genuinely. Tender and sincere, "
    "never platitudes, never minimizing - taught progressively along the "
    "ladder.",
    "compassionate statement record", "JAH-CSTT-", "JAH Compassionate Statements Archivist",
    "compassionate statements archivist - words of comfort, empathy, and "
    "support for grief, hardship, illness, and struggle; teaching when and "
    "how to say each statement genuinely, from simple presence through "
    "illness and hardship to deep grief support; answers from many angles "
    "- definition, example, analogy, application, history, how-to - using "
    "only archive data from this system",
    CIT_PUB, "public")
DBCFG["compassionate-statements-signature"] = _cfg(
    "compassionate-statements-signature", "The Compassionate Statements Signature Database",
    "Compassion as covenant: the comfort given is a promise kept, "
    "tenderness is strength, and presence is the Signature vow. The full "
    "ladder from simple presence through hardship and illness to deep "
    "grief support, reframed as Signature science. Clearly labeled "
    "Signature-made, never presented as authentic public record.",
    "compassionate statement record", "JAH-CSTTS-", "JAH Compassionate Statements Archivist (Signature)",
    "compassionate statements archivist - Signature editions: compassion "
    "as covenant, the comfort given a promise kept and presence the "
    "Signature vow, clearly labeled Signature-made and never presented as "
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
            "statement": e["statement"],
            "when_to_say": e["when_to_say"],
            "how_to_say": e["how_to_say"],
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
                          e["key_points"], "; ".join(e["requirements"]),
                          e["statement"])
        assert e["statement"] in program, \
            "demo/statement cross-check failed for %s" % rid
        rec["demo"] = {"kind": "python", "language": "python",
                       "program": program,
                       "note": "Working demonstration program (real, runnable Python)."}
        base.GATE.admit(slug, title, rid)
        recs.append(rec)
    ranks = [r["ladder_rank"] for r in recs]
    assert ranks == sorted(ranks), "records not in ladder order for %s" % slug
    return recs


def node_check_js(label, code):
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as f:
        f.write(code)
        path = f.name
    p = subprocess.run(["node", "--check", path],
                       capture_output=True, text=True, timeout=60)
    os.unlink(path)
    assert p.returncode == 0, "node --check failed for %s: %s" % (label, p.stderr[-800:])
    return True


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
    for slug in ("compassionate-statements", "compassionate-statements-signature"):
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
            for k in ("id", "t", "g", "name", "title", "statement", "when_to_say",
                      "how_to_say", "description", "how_it_works",
                      "key_points", "requirements", "standards", "citations",
                      "src", "ladder_rank", "ladder_tier", "demo"):
                assert k in r, "missing %s in %s" % (k, r["id"])
            prog = r["demo"].get("program")
            assert prog and len(r["description"]) > 200, "stub in %s" % r["id"]
            assert len(r["statement"]) > 5, "empty statement in %s" % r["id"]
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

    # JS hygiene: node --check on every inline page script and both gen files
    # (skips non-JS blocks like application/ld+json)
    for slug in built:
        ppath = os.path.join(REPO, "db", slug, "index.html")
        with open(ppath, "r", encoding="utf-8") as f:
            page = f.read()
        scripts = []
        for m in re.finditer(r"<script([^>]*)>(.*?)</script>", page, flags=re.S | re.I):
            attrs, code = m.group(1), m.group(2)
            if re.search(r"\bsrc\b", attrs, re.I):
                continue
            typ = re.search(r'type\s*=\s*"([^"]*)"', attrs, re.I)
            if typ and not re.search(r"javascript|ecmascript|module", typ.group(1), re.I):
                continue
            if code.strip():
                scripts.append(code)
        assert scripts, "no inline JS found in %s" % slug
        for i, code in enumerate(scripts):
            node_check_js("%s inline script %d" % (slug, i), code)
        gen_path = os.path.join(REPO, "db", slug, "gen-%s.js" % slug)
        with open(gen_path, "r", encoding="utf-8") as f:
            node_check_js("gen-%s.js" % slug, f.read())
    print("js hygiene: node --check clean on all page scripts and gen files", flush=True)

    # merger fragment (the merger owns manifest/api/hub updates - never touched here)
    def frag_entry(slug, n, source):
        c = DBCFG[slug]
        return {
            "slug": slug, "name": c["name"], "tagline": c["tagline"],
            "record_kind": c["record_kind"], "id_prefix": c["prefix"],
            "ai_name": c["ai"], "local_index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
            "record_count": n, "status": "live", "full_records": n,
            "index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
            "chunk_pattern": "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz",
            "source": source,
        }
    frag = {
        "public": frag_entry("compassionate-statements", 34, "public-harvest"),
        "signature": frag_entry("compassionate-statements-signature", 34, "signature"),
    }
    os.makedirs(os.path.dirname(FRAG_PATH), exist_ok=True)
    with open(FRAG_PATH, "w", encoding="utf-8") as f:
        json.dump(frag, f, indent=1, ensure_ascii=False)
        f.write("\n")
    print("fragment: %s" % FRAG_PATH, flush=True)
    print("DONE: 68 records, 68 demos OK, pages + shards + fragment written. "
          "Manifest/api/hub untouched for the merger.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
