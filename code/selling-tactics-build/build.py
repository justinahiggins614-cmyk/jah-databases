#!/usr/bin/env python3
"""Build the Selling Tactics databases for JAH Databases
(order #4b, 2026-10-17 15:32 EDT).

Dedupe pre-check (whole-system DedupeGate over data/dedupe/exact):
68 planned titles checked; 1 refusal ("Negotiation Fundamentals" already in
the university database) -> renamed to "Fundamentals of Sales Negotiation",
re-checked clean. All other 67 clean on first pass.

This build creates two NEW databases, 34 ladder-ordered records each:

  selling-tactics             - The Selling Tactics Database
                                (public-harvest: real, fact-checked sales
                                knowledge - prospecting, pitches, negotiation,
                                objection handling, closing techniques,
                                follow-up systems, relationship selling, and
                                the ethics of selling; standard references
                                Carnegie How to Win Friends and Influence
                                People 1936; Cialdini Influence rev ed 2021;
                                Rackham SPIN Selling 1988; Ziglar Secrets of
                                Closing the Sale 1984; Miller and Heiman
                                Strategic Selling 1985; Dixon and Adamson The
                                Challenger Sale 2011; Gitomer The Sales Bible
                                1994; Tracy The Psychology of Selling 2004;
                                Sandler 1995; Harvard Business Review sales
                                research; and the other landmarks cited per
                                record)
  selling-tactics-signature   - The Selling Tactics Signature Database
                                (his original Signature Selling Method: every
                                tactic a covenant between seller and buyer,
                                prospecting the search, the pitch the promise,
                                negotiation the balance, the close the
                                handshake, follow-up the bond; src signature,
                                titles suffixed " (Signature Edition)", never
                                presented as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-SELL- (public) and JAH-SELLS- (signature), verified free
in the manifest and in every shard index (zero hits; JAH-SLT- belongs to
the unrelated Software Labs Taxonomy database, so the SELL form was chosen).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_selling_tactics.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with the
OK marker; the build machine-executes all 68 demos.

Screening: all tactics are ethical persuasion - no deception, manipulation,
or pressure techniques; nothing hate-adjacent, profane, inappropriate, or
religious; nothing on neutralizing or defeating military or defense-grade
systems. Never the words "bat belt" anywhere. No website references.
No Facebook.

CONCURRENCY: this build never touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and never commits or pushes.
It writes only new untracked paths; a merger handles manifest/api/counts.
It writes the fragment at
~/workspace/hidden_files/missing-builds/fragments/selling-tactics.json
for the merger.
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
FRAGMENT = "/home/hatch/workspace/hidden_files/missing-builds/fragments/selling-tactics.json"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_selling_tactics import ENTRIES, SIG_TAIL
from demos_selling_tactics import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Selling Method: "
                "every tactic a covenant between seller and buyer, "
                "prospecting the search, the pitch the promise, negotiation "
                "the balance, the close the handshake, and follow-up the "
                "bond. Clearly labeled Signature-made, never presented as "
                "authentic public record.")
    pub_line = ("Public records - real, fact-checked sales knowledge: "
                "prospecting, pitches, negotiation, objection handling, "
                "closing techniques, follow-up systems, relationship "
                "selling, and the ethics of selling - every record carrying "
                "description, how it works, key points, requirements, "
                "standards, citations, and a working demonstration program, "
                "organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(what selling is, the psychology of buying, prospecting, "
              "qualifying, rapport, discovery questions, product knowledge, "
              "listening, features versus benefits, goals, time management) "
              "-> Compounded (elevator pitches, presentations, storytelling, "
              "objection handling, price objections, think-it-over, "
              "negotiation, trial closes, closing techniques, follow-up "
              "systems, referrals, upselling) -> Advanced (SPIN selling, "
              "value-based selling, enterprise cycles, multi-stakeholder "
              "consensus, key accounts, pipeline and forecasting, CRM "
              "discipline, ethics, win-loss analysis, challenger insight "
              "selling, the relationship and referral engine).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search prospecting, pitches, negotiation, objections, closing, follow-up, referrals, SPIN, value selling, pipeline, CRM, ethics...",
        "chat_ph": "Ask about selling tactics...",
        "archive_blurb": ("Seeded %s selling tactic records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled selling tactic studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about selling tactics - from what selling is through the psychology of buying, prospecting, qualifying, rapport, discovery, product knowledge, listening, features versus benefits, goals, and time management, through pitches, presentations, storytelling, objection handling, negotiation, trial closes, closing, follow-up, referrals, and upselling, to SPIN selling, value-based selling, enterprise cycles, consensus, key accounts, pipeline, CRM, ethics, win-loss, challenger insight selling, and the relationship engine." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "selling-tactic-study", "gen_demo_kind": "selling-tactic-demo",
        "source": source,
    }

CIT_PUB = ("Sales knowledge (standard references: Carnegie D. How to Win "
           "Friends and Influence People. Simon and Schuster; 1936; Cialdini "
           "RB. Influence: The Psychology of Persuasion. Revised ed. Harper "
           "Business; 2021; Rackham N. SPIN Selling. McGraw-Hill; 1988; "
           "Ziglar Z. Secrets of Closing the Sale. Berkley Books; 1984; "
           "Miller RB, Heiman SE. Strategic Selling. William Morrow; 1985; "
           "Dixon M, Adamson B. The Challenger Sale. Portfolio; 2011; "
           "Gitomer J. The Sales Bible. William Morrow; 1994; Tracy B. The "
           "Psychology of Selling. Harper Business; 2004; Sandler D. You "
           "Cant Teach a Kid to Ride a Bike at a Seminar. Dutton; 1995; "
           "Harvard Business Review sales and negotiation research archive).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature Selling "
                     "Method - every tactic a covenant between seller and "
                     "buyer - clearly labeled Signature-made.")

DBCFG = {}
DBCFG["selling-tactics"] = _cfg(
    "selling-tactics", "The Selling Tactics Database",
    "Tactics of selling: prospecting, pitches, negotiation, objection "
    "handling, closing techniques, follow-up systems, relationship selling, "
    "and the ethics of selling - real, fact-checked sales knowledge taught "
    "progressively along the ladder.",
    "selling tactic record", "JAH-SELL-", "JAH Selling Tactics Archivist",
    "selling tactics archivist - the knowledge of selling tactics: "
    "prospecting, pitches, negotiation, objection handling, closing "
    "techniques, follow-up systems, relationship selling, and the ethics of "
    "selling; teaching progressively along the ladder from foundations "
    "through compounded to advanced; answers from many angles - definition, "
    "example, analogy, application, history, math, how-to - using only "
    "archive data from this system",
    CIT_PUB, "public")
DBCFG["selling-tactics-signature"] = _cfg(
    "selling-tactics-signature", "The Selling Tactics Signature Database",
    "His original Signature Selling Method: every tactic a covenant between "
    "seller and buyer - prospecting the search, the pitch the promise, "
    "negotiation the balance, the close the handshake, follow-up the bond. "
    "The full ladder from what selling is through discovery, pitches, "
    "objections, negotiation, and closing, to SPIN, value selling, "
    "enterprise cycles, ethics, and the relationship engine, reframed as "
    "Signature science. Clearly labeled Signature-made, never presented as "
    "authentic public record.",
    "selling tactic record", "JAH-SELLS-", "JAH Selling Tactics Archivist (Signature)",
    "selling tactics archivist - Signature editions: his original Signature "
    "Selling Method, every tactic a covenant between seller and buyer, "
    "clearly labeled Signature-made and never presented as authentic public "
    "record; teaches progressively along the ladder from foundations through "
    "compounded to advanced; answers from many angles - definition, example, "
    "analogy, application, history, math, how-to - using only archive data "
    "from this system",
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


def fragment_entry(slug, n, source):
    c = DBCFG[slug]
    return {
        "slug": slug, "name": c["name"], "tagline": c["tagline"],
        "record_kind": c["record_kind"], "id_prefix": c["prefix"],
        "ai_name": c["ai"], "local_index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
        "record_count": n, "status": "live", "full_records": n,
        "index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
        "chunk_pattern": "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz",
        "source": c["source"],
    }


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
    for slug in ("selling-tactics", "selling-tactics-signature"):
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

    frag = {
        "public": fragment_entry("selling-tactics", len(built["selling-tactics"]), "public"),
        "signature": fragment_entry("selling-tactics-signature", len(built["selling-tactics-signature"]), "signature"),
    }
    os.makedirs(os.path.dirname(FRAGMENT), exist_ok=True)
    with open(FRAGMENT, "w", encoding="utf-8") as f:
        json.dump(frag, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print("fragment: %s" % FRAGMENT)
    print("DONE: 2 databases, %d records. Manifest/api/counts/commit left to the merger." % total)
    return 0


if __name__ == "__main__":
    sys.exit(main())
