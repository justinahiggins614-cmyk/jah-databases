#!/usr/bin/env python3
"""Build the Compliments databases for JAH Databases
(Manon's 16:15 orders, 2026-10-17, fun/social batch).

Verified 2026-10-17: RAW checks over the full manifest (2,398 databases)
plus every shard index title in jah-databases-data-1 (831 index files):
zero 'compliment*' slugs/names; zero title collisions for all 68 titles
(34 public + 34 Signature Edition) against the whole-system dedupe gate.
ID prefixes JAH-CMPL- (public) and JAH-CMPLS- (signature) verified free:
zero hits in manifest id_prefix values, zero hits in all 831 shard index
files. BUILD NEW is the verdict.

So this build creates two NEW databases, 34 ladder-ordered records each:

  compliments            - The Compliments Database
                           (public-harvest: genuine compliments for every
                           occasion - character, effort, appearance
                           (tasteful), skills, kindness - each record a
                           compliment WITH delivery guidance: when to say
                           it, how to make it specific and sincere;
                           sincere and kind only - never backhanded, never
                           flirtatious)
  compliments-signature  - The Compliments Signature Database
                           (his original Signature Word of Recognition:
                           every compliment a stamped instrument of the
                           spoken word, recognition the covenant between
                           giver and receiver, sincerity the seal, timing
                           the delivery, and the remembered compliment the
                           kept record; src signature, titles suffixed
                           " (Signature Edition)", never presented as
                           authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present everyday kindness -> deep recognition.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_compliments.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos before the pages
are written.

Screened 2026-10-17: nothing hate-adjacent, profane, or inappropriate; no
religious talk; compliments sincere and kind only.

NOTE: this build does NOT touch data/manifest.json, api.json, index.html,
README.md, or docs/AI_ACCESS.md, and does NOT commit or push. A merger
handles those. It writes only: db/compliments/ + db/compliments-signature/
(index.html + gen-*.js each) and the shard data dirs.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""
import importlib.util
import json
import os
import re
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
from entries_compliments import ENTRIES, SIG_TAIL
from demos_compliments import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Word of "
                "Recognition: every compliment a stamped instrument of the "
                "spoken word, recognition the covenant between giver and "
                "receiver, sincerity the seal, timing the delivery, and the "
                "remembered compliment the kept record. Clearly labeled "
                "Signature-made, never presented as authentic public record.")
    pub_line = ("Public records - genuine compliments for every occasion: "
                "character, effort, appearance (tasteful), skills, and "
                "kindness. Each record is a compliment WITH delivery "
                "guidance - when to say it, how to make it specific and "
                "sincere. Sincere and kind only - never backhanded, never "
                "flirtatious - organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(the sincere thank-you, noticing small efforts, naming "
              "kindness, greeting by name, praising punctuality, praising "
              "good questions, acknowledging work in progress, calm under "
              "pressure, public thanks, consistency, listening, thanking "
              "for time) -> Compounded (craftsmanship, well-run meetings, "
              "everyday courage, clear writing, patience, tasteful "
              "appearance compliments, mentorship, integrity, "
              "behind-the-scenes work, problem solving, lifting humor, "
              "comebacks from mistakes) -> Advanced (whole character, "
              "lifetime achievement tributes, moral courage, a life's "
              "work, living tributes, mentor legacies, grace in hard "
              "times, unsung heroes, forgiveness, the compliment that "
              "changes a life).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search thank-yous, effort, kindness, character, skills, patience, courage, integrity, mentorship, tributes, recognition...",
        "chat_ph": "Ask about compliments for every occasion...",
        "archive_blurb": ("Seeded %s compliment records, marching toward one million records. "
                          "Presented in teaching-ladder order: everyday kindness to deep recognition."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled compliment studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about genuine compliments for every occasion - from everyday thank-yous through praise for effort, skill, and character to deep recognition of lifework and legacy." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "compliment-study", "gen_demo_kind": "compliment-demo",
        "source": source,
    }

CIT_PUB = ("Compliment and recognition craft (standard references: Dweck CS. "
           "Mindset: The New Psychology of Success. Random House; 2006; "
           "Henderlong J, Lepper MR. The effects of praise on children's "
           "intrinsic motivation. Psychological Bulletin. 2002;128(5):774-795; "
           "Gottman JM, Silver N. The Seven Principles for Making Marriage "
           "Work. Crown; 1999; Losada M, Heaphy E. The role of positivity "
           "and connectivity in the performance of business teams. American "
           "Behavioral Scientist. 2004;47(6):740-765; Deci EL, Ryan RM. "
           "Intrinsic Motivation and Self-Determination in Human Behavior. "
           "Plenum; 1985; Emmons RA, McCullough ME. Counting blessings "
           "versus burdens. Journal of Personality and Social Psychology. "
           "2003;84(2):112-127; Fredrickson BL. Positivity. Crown; 2009; "
           "Seligman MEP. Flourish. Free Press; 2011; Grant AM. Give and "
           "Take. Viking; 2013; Cialdini RB. Influence. Rev ed. Harper "
           "Business; 2021; Stone D, Heen S. Thanks for the Feedback. "
           "Viking; 2014).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature Word of "
                     "Recognition - every compliment a stamped instrument of "
                     "the spoken word - clearly labeled Signature-made.")

DBCFG = {}
DBCFG["compliments"] = _cfg(
    "compliments", "The Compliments Database",
    "Genuine compliments for every occasion - character, effort, appearance, "
    "skills, and kindness - each record a compliment WITH delivery guidance: "
    "when to say it and how to make it specific and sincere. Sincere and "
    "kind only, taught progressively along the ladder from everyday kindness "
    "to deep recognition.",
    "compliment record", "JAH-CMPL-", "JAH Compliments Archivist",
    "compliments archivist - genuine compliments for every occasion: "
    "character, effort, appearance, skills, and kindness; each record a "
    "compliment with delivery guidance on when to say it and how to make it "
    "specific and sincere; sincere and kind only, never backhanded, never "
    "flirtatious; teaching progressively along the ladder from everyday "
    "kindness through compounded recognition to deep recognition; answers "
    "from many angles - definition, example, analogy, application, how-to - "
    "using only archive data from this system",
    CIT_PUB, "public")
DBCFG["compliments-signature"] = _cfg(
    "compliments-signature", "The Compliments Signature Database",
    "His original Signature Word of Recognition: every compliment a "
    "stamped instrument of the spoken word, recognition the covenant "
    "between giver and receiver, sincerity the seal, timing the delivery, "
    "and the remembered compliment the kept record. The full ladder from "
    "everyday thank-yous through compounded recognition to deep "
    "recognition, reframed as Signature craft. Clearly labeled "
    "Signature-made, never presented as authentic public record.",
    "compliment record", "JAH-CMPLS-", "JAH Compliments Archivist (Signature)",
    "compliments archivist - Signature editions: his original Signature "
    "Word of Recognition, every compliment a stamped instrument of the "
    "spoken word, clearly labeled Signature-made and never presented as "
    "authentic public record; teaches progressively along the ladder from "
    "everyday kindness through compounded recognition to deep recognition; "
    "answers from many angles - definition, example, analogy, application, "
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
    for slug in ("compliments", "compliments-signature"):
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

    # NOTE: manifest.json / api.json are owned by the merger - not touched here.
    print("records built: %d databases, %d records" % (len(built), total))
    print("NEXT: merger runs restamp + commit + push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
