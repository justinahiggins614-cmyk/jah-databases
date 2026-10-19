#!/usr/bin/env python3
"""Build The Holistic OTC and Natural Cures Database for JAH Databases
(Manon's order 2026-10-17 17:55 EDT).

Holistic over-the-counter and natural cures for sickness and injuries:
established OTC products and their documented uses, traditionally-documented
natural remedies (honey, ginger, chamomile, aloe, saline, and others) with
HONEST evidence framing (documented vs traditional vs not established), plus
his original Signature holistic regimen frameworks as the Signature half.

Dedupe: 2026-10-17 - ID prefixes JAH-HOC- / JAH-HOCS- verified free across
all 2,590 manifest id_prefix values and zero hits across every shard record
ID in ~/workspace/jah-databases-data-1/data/*/index.jsonl.gz. Whole-system
title gate via code/dedupe_gate.py. The only "holistic" hits in shards are
"HELM holistic evaluation" (AI benchmark, unrelated) - zero topical overlap.
No existing holistic/OTC/natural-cures database in the manifest.

Two NEW databases, 34 ladder-ordered records each:

  holistic-otc-natural-cures            - The Holistic OTC and Natural Cures Database
                                          (public-harvest: real documented
                                          remedies with honest evidence
                                          framing)
  holistic-otc-natural-cures-signature  - The Holistic OTC and Natural Cures
                                          Signature Database (his original
                                          Signature holistic regimen
                                          frameworks; src signature, titles
                                          suffixed " (Signature Edition)",
                                          never presented as authentic
                                          public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-34):
foundations 1-12 (common minor ailments) -> compounded 13-24 (injuries and
moderate ailments) -> advanced 25-34 (wellness practices, literacy, the
red-flag record).

STRICT CONTENT RULES ENFORCED BY THIS BUILD:
(1) Every record carries "not medical advice - consult a healthcare
    professional" framing (machine-audited).
(2) NEVER a cure claim for any serious disease (machine-audited: every
    occurrence of cure/cures/cured must sit inside a negation context).
(3) Documented vs traditional vs not-established labeled per record.
(4) NO dosage instructions anywhere (machine-audited regex for mg,
    teaspoons, drops, tablets, etc.).
(5) Descriptive/educational only; screened per standing rules.

Concurrency: this builder writes ONLY its own new untracked paths -
db/holistic-otc-natural-cures/, db/holistic-otc-natural-cures-signature/,
code/holistic-otc-natural-cures-build/, the data-1 shard dirs, and the
fragment file. It never touches data/manifest.json, api.json, index.html,
README.md, docs/AI_ACCESS.md, and never commits or pushes. A merger
handles those.
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
from entries_holistic_otc_natural_cures import ENTRIES, SIG_ENTRIES, SIG_TAIL
from demos_holistic_otc_natural_cures import DEMOS_ALL

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature holistic "
                "regimen frameworks: morning and evening rituals, comfort "
                "protocols, evidence-honesty tools, and a whole-person "
                "wellness charter. Clearly labeled Signature-made, never "
                "presented as authentic public record.")
    pub_line = ("Public records - real documented remedies with honest "
                "evidence framing: established OTC products and their "
                "documented uses, traditionally-documented natural remedies "
                "(honey, ginger, chamomile, aloe, saline, and others), each "
                "labeled documented, traditional, or not established. "
                "Educational information only, not medical advice.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(honey for cough, salt-water gargle, ginger for nausea, "
              "chamomile ritual, fluids and rest for colds, cold compress, "
              "acetaminophen and ibuprofen label literacy, antihistamines, "
              "saline nasal care, aloe for minor sunburn, RICE for sprains) "
              "-> Compounded (wound cleaning, moist wound covering, Epsom "
              "soak, turmeric, peppermint for tension headache, steam "
              "safety, oral rehydration, heat for cramps, lavender, "
              "echinacea and vitamin C evidence reviews, arnica) -> "
              "Advanced (sleep hygiene, slow breathing, gentle walking, "
              "fermented foods, red-flag literacy, evidence literacy, home "
              "wellness kit, recovery nutrition, sun protection, rest as "
              "medicine).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": ("%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder)),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search honey, ginger, chamomile, OTC label literacy, wound care, rehydration, sleep hygiene, red flags, evidence tiers...",
        "chat_ph": "Ask about holistic OTC and natural cures...",
        "archive_blurb": ("Seeded %s holistic OTC and natural cures records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "minor-ailments · injury-and-recovery-care · wellness-practices - each group opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled holistic cures studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about holistic over-the-counter and natural approaches - from honey, ginger, and chamomile through OTC label literacy, wound care, and rehydration, to sleep hygiene, red-flag literacy, and reading remedy claims honestly." % ai,
        "gen_fields": ["minor-ailments", "injury-and-recovery-care", "wellness-practices"],
        "gen_kind": "holistic-otc-natural-cures-study", "gen_demo_kind": "holistic-cures-demo",
        "source": source,
    }

CIT_PUB = ("Documented and traditional remedy literature (representative: "
           "Paul IM et al. on honey and cough, Archives of Pediatrics and "
           "Adolescent Medicine 2007; Ernst E, Pittler MH on ginger, British "
           "Journal of Anaesthesia 2000; Zick SM et al. on chamomile, BMC "
           "Complementary and Alternative Medicine 2011; King D et al. on "
           "saline nasal irrigation, Cochrane 2015; Maenthaisong R et al. on "
           "aloe and burns, Burns 2007; Fernandez R, Griffiths R on wound "
           "cleansing, Cochrane 2012; Winter GD on moist wound healing, "
           "Nature 1962; Karsch-Volk M et al. on echinacea, Cochrane 2014; "
           "Hemila H, Chalker E on vitamin C, Cochrane 2013; Gobel H et al. "
           "on peppermint oil and tension headache, Cephalalgia; Zaccaro A "
           "et al. on slow breathing, Frontiers in Human Neuroscience 2018; "
           "FDA OTC labeling for acetaminophen, NSAIDs, and antihistamines; "
           "WHO oral rehydration guidance; NCCIH fact sheets; American Red "
           "Cross first-aid guidance). Evidence status labeled per claim: "
           "documented, traditional, or not established.")
CIT_SIG = (CIT_PUB + " Signature editions are his original holistic regimen "
                     "frameworks - clearly labeled Signature-made, never "
                     "presented as authentic public record.")

DBCFG = {}
DBCFG["holistic-otc-natural-cures"] = _cfg(
    "holistic-otc-natural-cures", "The Holistic OTC and Natural Cures Database",
    "Holistic over-the-counter and natural approaches for sickness and "
    "injuries: established OTC products and their documented uses, "
    "traditionally-documented natural remedies with honest evidence "
    "framing, and wellness practices - taught progressively along the "
    "ladder, educational information only, never medical advice.",
    "holistic OTC and natural cures record", "JAH-HOC-", "JAH Holistic OTC and Natural Cures Archivist",
    "holistic OTC and natural cures archivist - documented and traditional "
    "remedies with honest evidence framing, from minor ailments through "
    "injury care to wellness practices and red-flag literacy; teaches "
    "progressively along the ladder from foundations through compounded to "
    "advanced; answers from many angles - definition, example, analogy, "
    "application, history, how-to - using only archive data from this system",
    CIT_PUB, "public")
DBCFG["holistic-otc-natural-cures-signature"] = _cfg(
    "holistic-otc-natural-cures-signature", "The Holistic OTC and Natural Cures Signature Database",
    "His original Signature holistic regimen frameworks and wellness-"
    "completion content: morning and evening rituals, comfort protocols, "
    "evidence-honesty tools, and a whole-person wellness charter. Clearly "
    "labeled Signature-made, never presented as authentic public record.",
    "holistic OTC and natural cures record", "JAH-HOCS-", "JAH Holistic OTC and Natural Cures Archivist (Signature)",
    "holistic OTC and natural cures archivist - Signature editions: his "
    "original Signature holistic regimen frameworks, clearly labeled "
    "Signature-made and never presented as authentic public record; teaches "
    "progressively along the ladder from foundations through compounded to "
    "advanced; answers from many angles - definition, example, analogy, "
    "application, history, how-to - using only archive data from this system",
    CIT_SIG, "signature")

base.DBCFG = DBCFG

ALL_KEYS = [e["key"] for e in ENTRIES] + [e["key"] for e in SIG_ENTRIES]
assert set(DEMOS_ALL) == set(ALL_KEYS), "demo map misses entries: %s" % (
    set(ALL_KEYS) - set(DEMOS_ALL))

# ------------------------------------------------------- safety audit

DOSAGE_RE = re.compile(
    r"\b\d+(\.\d+)?\s*(mg|milligrams?|grams?\b|teaspoons?|tablespoons?|drops?|"
    r"capsules?|tablets?|pills?|ounces?\b|fluid ounces?)\b", re.I)
CURE_RE = re.compile(r"\bcure[sd]?\b", re.I)
NEG_RE = re.compile(r"\b(not|no|never|without|against|isnt|isn|honest|limited|nothing|fallacy)\b", re.I)
SERIOUS_RE = re.compile(
    r"(cancer|diabetes|heart disease|pneumonia|antibiotic|tumor|stroke)\w*\s+"
    r"(cure[sd]?|treatment)|cure[sd]?\s+(for\s+)?(cancer|diabetes|heart)", re.I)

def safety_audit(recs, slug):
    for r in recs:
        blob = json.dumps(r, ensure_ascii=False)
        low = blob.lower()
        assert "facebook" not in low, "facebook ref in %s" % r["id"]
        assert "not medical advice" in low, "safety framing missing in %s" % r["id"]
        assert "healthcare professional" in low, "professional-care direction missing in %s" % r["id"]
        m = DOSAGE_RE.search(blob)
        assert not m, "dosage-like instruction in %s: %r" % (r["id"], m.group(0))
        m = SERIOUS_RE.search(blob)
        assert not m, "serious-disease cure claim in %s: %r" % (r["id"], m.group(0))
        for cm in CURE_RE.finditer(blob):
            ctx = blob[max(0, cm.start() - 60):cm.end() + 60]
            assert NEG_RE.search(ctx), (
                "cure claim outside negation context in %s: ...%s..." % (r["id"], ctx))
    print("safety audit: %d records clean in %s (no cure claims, no dosages, framing present)"
          % (len(recs), slug), flush=True)


def build_records(slug, source):
    cfg = DBCFG[slug]
    sig = source == "signature"
    entries = SIG_ENTRIES if sig else ENTRIES
    ordered = sorted(enumerate(entries), key=lambda p: (p[1]["ladder_rank"], p[0]))
    recs = []
    for _, e in ordered:
        name = e["name"]
        title = name + " (Signature Edition)" if sig else name
        if [h for h in base.GATE.check(slug, title) if h[0] != slug]:
            print("  gate refused (cross-db dupe): %s" % title, flush=True)
            continue
        rid = "%s%06d" % (cfg["prefix"], len(recs) + 1)
        if sig:
            description = ("Signature original framework. " + e["description"])
            how = e["how_it_works"]
            citations = list(e["citations"])
            assert SIG_TAIL in citations[0], "sig tail missing in %s" % e["key"]
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
        demo_fn = DEMOS_ALL[e["key"]]
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
    path = "/home/hatch/workspace/hidden_files/missing-builds/fragments/holistic-otc-natural-cures.json"
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
    for slug in ("holistic-otc-natural-cures", "holistic-otc-natural-cures-signature"):
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
            assert 1 <= r["ladder_rank"] <= 34, "ladder_rank out of range in %s" % r["id"]
            assert r["ladder_tier"] in ("foundations", "compounded", "advanced"), \
                "bad ladder_tier in %s" % r["id"]
            compile(prog, r["id"], "exec")
            if slug.endswith("-signature"):
                assert "(signature edition)" in r["title"].lower(), "sig title missing suffix"
                assert r["src"] == "signature"
                assert r["description"].startswith("Signature original framework. "), \
                    "sig framing missing in %s" % r["id"]
            else:
                assert r["src"] == "public-harvest"
        safety_audit(recs, slug)
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
        assert "facebook" not in gen_js.lower()
        assert "universal build" not in gen_js.lower(), "field leftover in gen js %s" % slug
        gpath = os.path.join(ddir, "gen-%s.js" % slug)
        with open(gpath, "w", encoding="utf-8") as f:
            f.write(gen_js)
        nc = subprocess.run(["node", "--check", gpath], capture_output=True, text=True)
        assert nc.returncode == 0, "node --check failed %s: %s" % (gpath, nc.stderr[-500:])
        print("page:  db/%s/index.html + gen-%s.js [%s] node-check clean"
              % (slug, slug, ", ".join(notes)), flush=True)

    write_fragment(built)
    print("records: %d public + %d signature = %d total" %
          (len(built["holistic-otc-natural-cures"]),
           len(built["holistic-otc-natural-cures-signature"]), total))
    print("NOTE: manifest.json / api.json / restamp left to the merger; no commit, no push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
