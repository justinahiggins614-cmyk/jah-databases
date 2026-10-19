#!/usr/bin/env python3
"""Build the Pickup Lines databases for JAH Databases
(Manon 16:15 orders, fun/social batch).

The Pickup Lines Database (pickup-lines) and The Pickup Lines Signature
Database (pickup-lines-signature): clean, clever, wholesome pickup lines -
bookish, science-themed, kind, funny - each record a pickup line WITH
context notes (when it works, why it works, delivery tips). WHOLESOME AND
RESPECTFUL ONLY: clever and kind, never crude, never objectifying, nothing
profane, no religious talk; every line screened against the
wholesome-respect canon (2026-10-17).

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced): simple clean kind openers ->
bookish and science lines with wordplay -> clever multi-line
constructions. The shard index is written in ladder order so pages present
simple -> compounded -> complex.

ID prefixes: JAH-PKUP- (public) and JAH-PKUPS- (signature), verified free
in the manifest id_prefix values and in every shard index file
(zero hits, 2026-10-17). All 68 titles pre-checked against the whole
system via code/dedupe_gate.py: zero collisions, zero refusals.

Numerical cores: hand-computed 2026-10-17, machine-verified by the demos
(see demos_pickup_lines.py). Every demo prints its real computed values
(word counts, delivery-time estimates, line-of-the-day hash picks, context
matcher scores), asserts tight bounds (never float exact-equality), ends
with the OK marker, and is cross-checked against its entry text; the build
machine-executes all 68 demos.

CONCURRENCY: this build never touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and never commits or pushes.
A merger handles those.

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
from entries_pickup_lines import ENTRIES, SIG_TAIL
from demos_pickup_lines import DEMOS

LINES = {e["key"]: e["line"] for e in ENTRIES}
LINES_BY_ID = {}

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Kindness "
                "Method: every line a covenant of respect, spoken once and "
                "honestly, the speaker bringing the best of himself and "
                "leaving the other person brighter than he found them. "
                "Clearly labeled Signature-made, never presented as "
                "authentic public record.")
    pub_line = ("Public records - clean, clever, wholesome pickup lines, "
                "screened against the wholesome-respect canon: bookish "
                "lines, science-themed lines, kind openers, and funny "
                "wordplay - every record carrying the line itself with "
                "context notes on when it works, why it works, and delivery "
                "tips, organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(simple clean kind openers - the warm hello, the genuine "
              "compliment, the shared moment, the helpful question, the "
              "honest introduction, the bright smile, the kind observation, "
              "the coffee invitation, the bookstore hello, the music note) "
              "-> Compounded (bookish lines - the library book, the great "
              "gatsby, the plot twist, the well-read heart, the dog-eared "
              "page, the unfinished chapter - and science lines - copper "
              "tellurium, gravity, the sun compliment, the bunsen burner "
              "smile, the noble gas, the hypothesis) -> Advanced (clever "
              "multi-line constructions - the dictionary definition, the "
              "star chart, the periodic table serenade, the algorithm of "
              "us, the constellation map, the time traveler, the librarian "
              "permission slip, the chemistry equation, the odyssey opener, "
              "the astronomer wish, the poet proof, the kindness theorem).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: the pickup line, "
                  "context notes, how it works, key points, delivery "
                  "requirements, respect standards, citations, and a working "
                  "demonstration program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search kind openers, bookish lines, science lines, library lines, chemistry lines, delivery tips, context notes...",
        "chat_ph": "Ask about pickup lines...",
        "archive_blurb": ("Seeded %s clean wholesome pickup line records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Kind Openers \u00b7 Bookish Lines \u00b7 Science Lines \u00b7 Witty Multi-Liners - each field opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled wholesome pickup line studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about pickup lines - from simple kind openers through bookish lines and science lines to clever multi-line constructions, each with context notes on when it works, why it works, and delivery tips." % ai,
        "gen_fields": ["Kind Openers", "Bookish Lines", "Science Lines", "Witty Multi-Liners"],
        "gen_kind": "pickup-line-study", "gen_demo_kind": "pickup-line-demo",
        "source": source,
    }

CIT_PUB = ("Pickup-line genre (traditional lines screened; wording original "
           "to this archive) screened against the JAH Databases "
           "wholesome-respect canon (2026-10-17): clean, kind, respectful, "
           "non-objectifying; nothing crude, nothing profane, no religious "
           "talk. Literary echoes: Fitzgerald FS. The Great Gatsby. "
           "Scribner; 1925; Homer. The Odyssey. Trans. Wilson E. Norton; "
           "2017.")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature "
                     "Kindness Method - every line a covenant of respect, "
                     "clearly labeled Signature-made.")

DBCFG = {}
DBCFG["pickup-lines"] = _cfg(
    "pickup-lines", "The Pickup Lines Database",
    "Clean, clever, wholesome pickup lines - bookish, science-themed, kind, "
    "funny - each record a pickup line WITH context notes on when it works, "
    "why it works, and delivery tips. Wholesome and respectful only: clever "
    "and kind, never crude, never objectifying, nothing profane.",
    "pickup line record", "JAH-PKUP-", "JAH Pickup Line Archivist",
    "pickup line archivist - clean clever wholesome pickup lines: bookish "
    "lines, science-themed lines, kind openers, funny wordplay; every "
    "record carrying the line with context notes on when it works, why it "
    "works, and delivery tips; teaching progressively along the ladder "
    "from foundations through compounded to advanced; answers from many "
    "angles - definition, example, analogy, application, history, how-to - "
    "using only archive data from this system",
    CIT_PUB, "public")
DBCFG["pickup-lines-signature"] = _cfg(
    "pickup-lines-signature", "The Pickup Lines Signature Database",
    "His original Signature Kindness Method: every line a covenant of "
    "respect, spoken once and honestly, the speaker bringing the best of "
    "himself and leaving the other person brighter than he found them. The "
    "full ladder from simple kind openers through bookish and science "
    "lines to clever multi-line constructions, reframed as Signature "
    "science. Clearly labeled Signature-made, never presented as authentic "
    "public record.",
    "pickup line record", "JAH-PKUPS-", "JAH Pickup Line Archivist (Signature)",
    "pickup line archivist - Signature editions: his original Signature "
    "Kindness Method, every line a covenant of respect, clearly labeled "
    "Signature-made and never presented as authentic public record; teaches "
    "progressively along the ladder from foundations through compounded to "
    "advanced; answers from many angles - definition, example, analogy, "
    "application, history, how-to - using only archive data from this "
    "system",
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
        LINES_BY_ID[rid] = e["line"]
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
    for slug in ("pickup-lines", "pickup-lines-signature"):
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
            assert LINES_BY_ID[r["id"]] in p.stdout, "demo/entry text mismatch %s" % r["id"]
    print("demo execution: all %d demos ran OK, entry text cross-checked" % total, flush=True)

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

    print("records: 34 public + 34 signature, ladder-ordered, shards + pages written")
    print("NOTE: manifest/api.json untouched per concurrency rules - merger handles.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
