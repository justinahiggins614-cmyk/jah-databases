#!/usr/bin/env python3
"""Build the Personality databases for JAH Databases
(Manon's 16:15 orders, 2026-10-17, fun/social batch).

Verified 2026-10-17: RAW SWEEP over the full manifest (2,410 databases)
PLUS every shard index title in jah-databases-data-1 PLUS the main-repo
data dir: zero 'personality*' slugs/names. The dedupe-gate pre-check over
the whole system refused 3 plain trait titles - "Conscientiousness",
"Extraversion", "Agreeableness" - each already an entry title in the
dictionary 'words' database and in the 'wiki' database. Those three
records were renamed to disambiguated titles
("Conscientiousness: The Big Five Discipline Domain",
"Extraversion: The Big Five Energy Domain",
"Agreeableness: The Big Five Warmth Domain"); all 68 final titles
(34 public + 34 signature) re-checked CLEAR. Zero collisions shipped.

So this build creates two NEW databases, 34 ladder-ordered records each:

  personality            - The Personality Database
                           (public-harvest: real, fact-checked personality
                           psychology - the Big Five, HEXACO, facets,
                           measurement, nature/nurture, the major type
                           systems, profiles, work, relationships, teams,
                           lifespan development, decision-making, ethics,
                           leadership, culture, conflict, deliberate
                           growth, and the integrated view - every record
                           carrying trait/type description, behaviors,
                           strengths, growth edges, and how to work with
                           it; standard references Costa & McCrae
                           NEO-PI-R 1992; Ashton & Lee HEXACO 2007;
                           Goldberg 1990; John & Srivastava 1999; McCrae
                           & Costa 1999; Eysenck 1967; Jung 1921; Myers
                           & Briggs 1980; Riso & Hudson 1996; Marston
                           1928; Allport 1937; Cattell 16PF 1993;
                           Roberts & Mroczek 2008; Mischel 1968; Mischel
                           & Shoda 1995; McCrae et al. 2005; APA
                           Dictionary; and the other landmarks cited per
                           record)
  personality-signature  - The Personality Signature Database
                           (his original Signature Personality Method:
                           every trait a signature frequency, every
                           profile a chord of frequencies, growth the
                           deliberate retuning of the chord; src
                           signature, titles suffixed " (Signature
                           Edition)", never presented as authentic public
                           record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-PRSL- (public) and JAH-PRSLS- (signature), verified free
in the manifest id_prefix values and in every shard index (zero hits).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_personality.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos.

Screening: nothing hate-adjacent, profane, or inappropriate; no religious
talk; no diagnosis of real people and no clinical disorder content -
normal-range personality psychology only.

Never the words "bat belt" anywhere. No website references. No Facebook.

CONCURRENCY: this build never touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and never commits or pushes.
It writes only db/personality/, db/personality-signature/,
code/personality-build/, the shard data dirs, and the merger fragment.
The merger handles manifest/api/restamp/commit.
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
FRAGMENT = "/home/hatch/workspace/hidden_files/missing-builds/fragments/personality.json"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_personality import ENTRIES, SIG_TAIL
from demos_personality import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Personality "
                "Method: every trait a signature frequency, every profile a "
                "chord of frequencies, and growth the deliberate retuning "
                "of the chord. Clearly labeled Signature-made, never "
                "presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked personality "
                "psychology: the Big Five, HEXACO, facets, measurement "
                "sources, nature and nurture, the major type systems "
                "(Jung/MBTI, Enneagram, DISC, temperaments, 16PF), reading "
                "full profiles, personality at work and in relationships, "
                "reliability and validity, the person-situation debate, "
                "team chemistry, lifespan stability and change, the "
                "maturity principle, decision-making, ethical reading of "
                "others, leadership, culture, conflict styles, deliberate "
                "growth, and the integrated view - every record carrying "
                "the full entry: trait/type description, behaviors, "
                "strengths, growth edges, and how to work with it, "
                "organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(what personality is, traits vs states vs types, the Big "
              "Five, the five domains, HEXACO, honesty-humility, facets, "
              "measurement sources, nature and nurture) -> Compounded "
              "(Jung and Myers-Briggs, introversion and ambiversion, the "
              "Enneagram, DISC, the four temperaments, the sixteen "
              "personality factors, reading full profiles, personality at "
              "work, personality in relationships, reliability and "
              "validity, the person-situation debate, team chemistry) -> "
              "Advanced (stability and change across the lifespan, the "
              "maturity principle, decision-making, reading others "
              "ethically, leadership, culture, conflict styles, deliberate "
              "growth, the integrated view).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search Big Five, HEXACO, honesty-humility, openness, conscientiousness, extraversion, introversion, agreeableness, neuroticism, facets, MBTI, Enneagram, DISC, temperaments, 16PF, profiles, teams, leadership, conflict styles, growth...",
        "chat_ph": "Ask about personality traits and types...",
        "archive_blurb": ("Seeded %s personality records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled personality studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about personality - the Big Five, HEXACO, facets, type systems, profiles, work, relationships, teams, growth across the lifespan, leadership, and reading people well and ethically." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "personality-study", "gen_demo_kind": "personality-demo",
        "source": source,
    }

CIT_PUB = ("Personality psychology (standard references: Costa PT, McCrae "
           "RR. The Revised NEO Personality Inventory (NEO-PI-R); "
           "Professional Manual; 1992; Ashton MC, Lee K. The HEXACO model "
           "of personality structure; 2007; Goldberg LR. The Big-Five "
           "factor structure; 1990; John OP, Srivastava S. The Big Five "
           "trait taxonomy; 1999; McCrae RR, Costa PT. The five-factor "
           "theory of personality; 1999; Eysenck HJ. The Biological Basis "
           "of Personality; 1967; Jung CG. Psychological Types; 1921; "
           "Myers IB, Myers PB. Gifts Differing; 1980; Riso DR, Hudson R. "
           "Personality Types; 1996; Marston WM. Emotions of Normal "
           "People; 1928; Allport GW. Personality: A Psychological "
           "Interpretation; 1937; Cattell RB. The 16PF Personality "
           "Questionnaire; 1993; Roberts BW, Mroczek DK. Personality trait "
           "change in adulthood; 2008; Mischel W. Personality and "
           "Assessment; 1968; Mischel W, Shoda Y. CAPS; 1995; McCrae RR "
           "et al. Universal features of personality traits; 2005; APA "
           "Dictionary of Psychology).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature "
                     "Personality Method - every trait a signature "
                     "frequency, every profile a chord, growth the "
                     "deliberate retuning of the chord - clearly labeled "
                     "Signature-made.")

DBCFG = {}
DBCFG["personality"] = _cfg(
    "personality", "The Personality Database",
    "Understand personality: the major trait models (Big Five, HEXACO), "
    "personality types, how traits show up in behavior, and how to "
    "understand your own personality and the personalities of others - each record a "
    "full entry with behaviors, strengths, growth edges, and how to work "
    "with it, taught progressively along the ladder.",
    "personality record", "JAH-PRSL-", "JAH Personality Archivist",
    "personality archivist - the major trait models, personality types, "
    "how traits show up in behavior, and how to understand your own and "
    "the personalities of others; teaching progressively along the "
    "ladder from foundations through compounded to advanced; answers from "
    "many angles - definition, example, analogy, application, history, "
    "math, how-to - using only archive data from this system",
    CIT_PUB, "public")
DBCFG["personality-signature"] = _cfg(
    "personality-signature", "The Personality Signature Database",
    "His original Signature Personality Method: every trait a signature "
    "frequency, every profile a chord of frequencies, growth the "
    "deliberate retuning of the chord. The full ladder from what "
    "personality is through the Big Five, HEXACO, facets, and type "
    "systems, to profiles, work, relationships, teams, lifespan change, "
    "leadership, and the integrated view, reframed as Signature science. "
    "Clearly labeled Signature-made, never presented as authentic public "
    "record.",
    "personality record", "JAH-PRSLS-", "JAH Personality Archivist (Signature)",
    "personality archivist - Signature editions: his original Signature "
    "Personality Method, every trait a signature frequency and every "
    "profile a chord, clearly labeled Signature-made and never presented "
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
    for slug in ("personality", "personality-signature"):
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
        assert "mergePanel" in page, "merge panel missing"
        assert "dataset.p" in page, "tab-handler guard missing"
        assert DBCFG[slug]["search_ph"] in page, "field-specific search placeholder missing"
        assert "facebook" not in page.lower()
        assert "synthetic intelligence" not in page.lower(), "template leftover in %s" % slug
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

    # Merger fragment (the merger owns manifest/api/restamp/commit).
    frag = {}
    for slug, recs in built.items():
        cfg = DBCFG[slug]
        is_sig = slug.endswith("-signature")
        frag["signature" if is_sig else "public"] = {
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
            "source": "signature" if is_sig else "public-harvest",
        }
    os.makedirs(os.path.dirname(FRAGMENT), exist_ok=True)
    with open(FRAGMENT, "w", encoding="utf-8") as f:
        json.dump(frag, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print("fragment: %s" % FRAGMENT)
    print("DONE: 2 databases, %d records. Manifest/api/restamp/commit left to the merger." % total)
    return 0


if __name__ == "__main__":
    sys.exit(main())
