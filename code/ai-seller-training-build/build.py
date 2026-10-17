#!/usr/bin/env python3
"""Build the AI Seller Training databases for JAH Databases
(Manon's order 2026-10-17 15:32 EDT, order #4a).

Training data so an AI learns to sell: sales conversation corpora
(discovery dialogues, objection-handling exchanges, closing
conversations), sales personas and playbooks, evaluation rubrics for
sales skill, and scenario drills with ideal responses. Distinct from
the selling-tactics database (tactics as knowledge) - this one is
training material for an AI.

Dedupe: 2026-10-17 - all 68 titles checked against the whole system
via code/dedupe_gate.py (manifest 2,390 databases + global exact
shards): zero collisions, zero refusals.

Two NEW databases, 34 ladder-ordered records each:

  ai-seller-training              - The AI Seller Training Database
                                    (public-harvest: real, fact-checked,
                                    ethical sales practice from established
                                    sales literature - AIDA (Lewis 1898),
                                    SPIN (Rackham 1988), Challenger
                                    (Dixon and Adamson 2011), Sandler,
                                    Solution Selling (Bosworth 1995), SNAP
                                    (Konrath 2010), BANT (IBM), MEDDIC,
                                    consultative selling, Dale Carnegie,
                                    Getting to Yes (Fisher and Ury 1981))
  ai-seller-training-signature    - The AI Seller Training Signature Database
                                    (his original Signature Sales Method:
                                    the sale as a covenant between seller
                                    and buyer, value proven before price is
                                    named, every promise kept; src
                                    signature, titles suffixed " (Signature
                                    Edition)", never presented as authentic
                                    public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-SLR- (public) and JAH-SLRS- (signature), verified free
in the manifest id_prefix values and with zero hits in every shard index
file.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_ai_seller_training.py). Every demo prints its real
computed values, asserts tight bounds (never float exact-equality), and
ends with the OK marker; the build machine-executes all 68 demos.

Concurrency: this builder writes ONLY its own new untracked paths -
db/ai-seller-training/, db/ai-seller-training-signature/,
code/ai-seller-training-build/, the data-1 shard dirs, and the fragment
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
from entries_ai_seller_training import ENTRIES, SIG_TAIL
from demos_ai_seller_training import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Sales Method: "
                "the sale as a covenant between seller and buyer, value "
                "proven before price is named, every promise kept, and "
                "pressure tactics excluded by design. Clearly labeled "
                "Signature-made, never presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked, ethical sales practice "
                "from established sales literature: AIDA, SPIN selling, the "
                "Challenger sale, Sandler, solution selling, SNAP selling, "
                "BANT and MEDDIC qualification, consultative selling, "
                "objection handling, closing conversations, negotiation, "
                "and evaluation rubrics - organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(what an AI seller is, the AIDA model, features advantages "
              "benefits, open and closed questions, active listening, "
              "rapport, needs analysis, the one-sentence value proposition, "
              "BANT qualification, the conversation arc, trial closes, "
              "follow-up discipline) -> Compounded (SPIN selling, the full "
              "discovery call corpus, feel-felt-found objection handling, "
              "price objections, the Challenger sale, consultative selling, "
              "SNAP selling, storytelling closes, stall handling, the "
              "summary close, choice and assumptive closes, negotiation) -> "
              "Advanced (MEDDIC, multi-stakeholder selling, the evaluation "
              "rubric, the angry-buyer drill, the expert-buyer drill, the "
              "consultative and challenger AI seller personas, the "
              "full-cycle playbook, the ethical guardrails, self-review).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search AIDA, SPIN, discovery calls, objection handling, trial closes, closing, BANT, MEDDIC, negotiation, rubrics, drills, personas...",
        "chat_ph": "Ask about AI seller training...",
        "archive_blurb": ("Seeded %s AI seller training records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled AI seller training studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about AI seller training - from what an AI seller is through AIDA, features and benefits, questions, listening, rapport, needs analysis, value propositions, BANT, the conversation arc, trial closes, and follow-up, through SPIN, discovery calls, objection handling, price objections, the Challenger sale, consultative selling, SNAP, storytelling, stalls, closes, and negotiation, to MEDDIC, buying committees, rubrics, drills, seller personas, the full-cycle playbook, guardrails, and self-review." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "ai-seller-training-study", "gen_demo_kind": "ai-seller-training-demo",
        "source": source,
    }

CIT_PUB = ("Ethical sales practice (standard references: Lewis E. St. Elmo. "
           "Catch-Line and Argument. The Book-Keeper; 1899 - early AIDA "
           "formulation; Strong E. The Psychology of Selling and Advertising. "
           "McGraw-Hill; 1925; Carnegie D. How to Win Friends and Influence "
           "People. Simon and Schuster; 1936; Rogers C, Farson R. Active "
           "Listening. University of Chicago; 1957; Fisher R, Ury W. Getting "
           "to Yes. Houghton Mifflin; 1981; Hopkins T. How to Master the Art "
           "of Selling. Warner Books; 1980; Rackham N. SPIN Selling. "
           "McGraw-Hill; 1988; Sandler D. You Cannot Teach a Kid to Ride a "
           "Bike at a Seminar. Dutton; 1995; Bosworth M. Solution Selling. "
           "McGraw-Hill; 1995; Green C, Howe H, Maister D. The Trusted "
           "Advisor. Free Press; 2000; Heath C, Heath D. Made to Stick. "
           "Random House; 2007; Moore G. Crossing the Chasm. HarperBusiness; "
           "1991; Konrath J. SNAP Selling. Portfolio; 2010; Dixon M, Adamson "
           "B. The Challenger Sale. Portfolio; 2011; IBM BANT qualification "
           "framework; MEDDIC/MEDDICC enterprise qualification framework).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature Sales "
                     "Method - the sale as a covenant between seller and "
                     "buyer, value proven before price is named, every "
                     "promise kept - clearly labeled Signature-made.")

DBCFG = {}
DBCFG["ai-seller-training"] = _cfg(
    "ai-seller-training", "The AI Seller Training Database",
    "Training data so an AI learns to sell: sales conversation corpora "
    "(discovery dialogues, objection-handling exchanges, closing "
    "conversations), sales personas and playbooks, evaluation rubrics for "
    "sales skill, and scenario drills with ideal responses - real, "
    "fact-checked, ethical sales practice taught progressively along the "
    "ladder.",
    "AI seller training record", "JAH-SLR-", "JAH AI Seller Training Archivist",
    "AI seller training archivist - training data so an AI learns to sell: "
    "discovery dialogues, objection-handling exchanges, closing "
    "conversations, sales personas, playbooks, evaluation rubrics, and "
    "scenario drills with ideal responses; teaching progressively along the "
    "ladder from foundations through compounded to advanced; answers from "
    "many angles - definition, example, analogy, application, history, math, "
    "how-to - using only archive data from this system",
    CIT_PUB, "public")
DBCFG["ai-seller-training-signature"] = _cfg(
    "ai-seller-training-signature", "The AI Seller Training Signature Database",
    "His original Signature Sales Method as AI training data: the sale as "
    "a covenant between seller and buyer, value proven before price is "
    "named, every promise kept. The full ladder - foundations, compounded, "
    "advanced - reframed as Signature science. Clearly labeled "
    "Signature-made, never presented as authentic public record.",
    "AI seller training record", "JAH-SLRS-", "JAH AI Seller Training Archivist (Signature)",
    "AI seller training archivist - Signature editions: his original "
    "Signature Sales Method as AI training data, the sale as a covenant "
    "between seller and buyer, clearly labeled Signature-made and never "
    "presented as authentic public record; teaches progressively along the "
    "ladder from foundations through compounded to advanced; answers from "
    "many angles - definition, example, analogy, application, history, math, "
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
    path = "/home/hatch/workspace/hidden_files/missing-builds/fragments/ai-seller-training.json"
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
    for slug in ("ai-seller-training", "ai-seller-training-signature"):
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
          (len(built["ai-seller-training"]),
           len(built["ai-seller-training-signature"]), total))
    print("NOTE: manifest.json / api.json / restamp left to the merger; no commit, no push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
