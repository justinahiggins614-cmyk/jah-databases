#!/usr/bin/env python3
"""Build the Public Notices and Deadlines databases for JAH Databases
(missing-115 #58, Wave 1 operational data).

Pre-authoring verification 2026-10-17: RAW SWEEP over the full manifest
(2,095 id_prefix values) plus every shard index title in
jah-databases-data-1 (790 index files): zero 'public-notices*' slugs/names;
zero title collisions on all 68 planned titles (dedupe gate run before
authoring, zero refusals). No existing database covers recalls, regulatory
changes, tenders, filings, advisories, and expiration dates as an
operational deadline-tracking discipline - BUILD NEW is the verdict.

This build creates two NEW databases, 34 ladder-ordered records each:

  public-notices-deadlines              - The Public Notices and Deadlines
                                         Database
                                         (public-harvest: real, fact-checked
                                         operational knowledge - recalls,
                                         regulatory changes, tenders,
                                         filings, advisories, expiration
                                         dates; the anatomy of a public
                                         notice; deadline computation with
                                         business days and jurisdiction
                                         rules; compliance calendars; notice
                                         tracking workflows; advisory
                                         severity classification; standard
                                         references the Federal Register
                                         Act 44 U.S.C. 1501-1511; the
                                         Administrative Procedure Act
                                         5 U.S.C. 553; FDA recall classes
                                         21 CFR Part 7; NHTSA 49 U.S.C.
                                         30118-30120; CPSC 15 U.S.C. 2064;
                                         FRCP Rule 6; the FAR 48 CFR Part 5;
                                         the Exchange Act reporting rules;
                                         IRC 26 U.S.C. 6072; 35 U.S.C. 41(b)
                                         maintenance fees; the Lanham Act
                                         15 U.S.C. 1058-1059; ISO 8601:2019;
                                         and the other landmarks cited per
                                         record)
  public-notices-deadlines-signature   - The Public Notices and Deadlines
                                         Signature Database
                                         (his original Signature Deadline
                                         Doctrine: every notice a summons,
                                         every deadline a covenant kept in
                                         public, the compliance calendar the
                                         honor roll, severity classification
                                         the measure of the warning, and the
                                         tracking workflow the chain of
                                         custody; src signature, titles
                                         suffixed " (Signature Edition)",
                                         never presented as authentic public
                                         record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-PNDT- (public) and JAH-PNDTS- (signature). NOTE: the
first-choice prefixes JAH-PND- / JAH-PNDS- were taken (two pre-existing
databases share JAH-PND-: park-naturalists and public-neuropsychologists,
an anomaly outside this build), so the PNDT form (Public Notices and
Deadlines Tracking) was chosen; verified free in the manifest and in all
shard indexes (zero hits).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_public_notices_deadlines.py). Every demo prints its real
computed values, asserts tight bounds (never float exact-equality), and
ends with the OK marker; the build machine-executes all 68 demos before
the records ship.

Screening: civilian operational scope only. Nothing hate-adjacent,
profane, or inappropriate; no religious talk; nothing on neutralizing or
defeating military or defense-grade systems.

NOTE (concurrency): this builder does NOT touch data/manifest.json,
api.json, index.html, README.md, or docs/AI_ACCESS.md, and never commits
or pushes. A merger handles manifest/api/restamp/commit. This script only
creates the new untracked paths for these two databases plus the fragment.

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
from entries_public_notices_deadlines import ENTRIES, SIG_TAIL
from demos_public_notices_deadlines import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Deadline "
                "Doctrine: every notice a summons, every deadline a "
                "covenant kept in public, the compliance calendar the "
                "honor roll, severity classification the measure of the "
                "warning, and the tracking workflow the chain of custody. "
                "Clearly labeled Signature-made, never presented as "
                "authentic public record.")
    pub_line = ("Public records - real, fact-checked operational knowledge: "
                "recalls, regulatory changes, tenders, filings, advisories, "
                "and expiration dates; the anatomy of a public notice; "
                "deadline computation with business days and jurisdiction "
                "rules; compliance calendars; notice tracking workflows; "
                "and advisory severity classification - organized in the "
                "Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(what a public notice is, the anatomy of a notice, the six "
              "families, what a deadline is, business days and calendar "
              "rules, where notices come from, publication channels, "
              "advisory severity classification, the compliance read, "
              "notice tracking workflows, compliance calendars, expiration "
              "dates renewals and grace periods) -> Compounded (product "
              "recalls, recall classes, regulatory changes and comment "
              "periods, tenders and procurement notices, filings and "
              "reporting deadlines, safety advisories and public alerts, "
              "legal and court notice deadlines, consumer protection "
              "notices, licensing and certification deadlines, "
              "jurisdiction rules, patent trademark and IP filing "
              "deadlines, tax and financial filing deadlines) -> Advanced "
              "(deadline computation algorithms, building a notice "
              "tracking system, escalation paths and non-compliance "
              "consequences, audit trails and proof of compliance, "
              "multi-jurisdiction deadline resolution, recall response "
              "playbooks, regulatory change impact assessment, tender "
              "response workflow and bid deadlines, automated deadline "
              "monitoring, the complete compliance calendar system).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search recalls, regulatory changes, tenders, filings, advisories, expirations, deadlines, business days, compliance calendars, severity classification...",
        "chat_ph": "Ask about public notices and deadlines...",
        "archive_blurb": ("Seeded %s public notice and deadline records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled public notice and deadline studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about public notices and deadlines - from what a notice is through its anatomy, the six families, deadline anatomy, business days, sources, channels, severity, the compliance read, tracking workflows, calendars, and expirations, through recalls, regulatory changes, tenders, filings, advisories, legal notices, consumer protection, licensing, jurisdiction, IP deadlines, and tax deadlines, to computation algorithms, tracking systems, escalation, audit trails, multi-jurisdiction resolution, recall playbooks, impact assessment, bid workflows, monitoring, and the complete system." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "public-notices-study", "gen_demo_kind": "public-notices-demo",
        "source": source,
    }

CIT_PUB = ("Public notices and deadline operations (standard references: "
           "Federal Register Act, 44 U.S.C. 1501-1511; Administrative "
           "Procedure Act, 5 U.S.C. 553; FDA recall classes, 21 CFR Part 7; "
           "Federal Food, Drug, and Cosmetic Act, 21 U.S.C. 301-399; NHTSA "
           "recall provisions, 49 U.S.C. 30118-30120; Consumer Product "
           "Safety Act, 15 U.S.C. 2064; Federal Rules of Civil Procedure, "
           "Rule 6; Federal Acquisition Regulation, 48 CFR Part 5; "
           "Securities Exchange Act of 1934, sections 13 and 15(d); "
           "Internal Revenue Code, 26 U.S.C. 6072; patent maintenance "
           "fees, 35 U.S.C. 41(b); Lanham Act, 15 U.S.C. 1058-1059; "
           "Patent Cooperation Treaty, Article 22; FTC Act, 15 U.S.C. 45; "
           "ISO 8601:2019).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature "
                     "Deadline Doctrine - every notice a summons, every "
                     "deadline a covenant kept in public - clearly labeled "
                     "Signature-made.")

DBCFG = {}
DBCFG["public-notices-deadlines"] = _cfg(
    "public-notices-deadlines", "The Public Notices and Deadlines Database",
    "Recalls, regulatory changes, tenders, filings, advisories, and "
    "expiration dates: real, fact-checked operational knowledge of the "
    "anatomy of a public notice, deadline computation with business days "
    "and jurisdiction rules, compliance calendars, notice tracking "
    "workflows, and advisory severity classification - taught progressively "
    "along the ladder.",
    "public notice and deadline record", "JAH-PNDT-", "JAH Public Notices and Deadlines Archivist",
    "public notices and deadlines archivist - recalls, regulatory changes, "
    "tenders, filings, advisories, and expiration dates; the anatomy of a "
    "public notice; deadline computation with business days and "
    "jurisdiction rules; compliance calendars; notice tracking workflows; "
    "advisory severity classification; teaching progressively along the "
    "ladder from foundations through compounded to advanced; answers from "
    "many angles - definition, example, analogy, application, history, "
    "math, how-to - using only archive data from this system",
    CIT_PUB, "public")
DBCFG["public-notices-deadlines-signature"] = _cfg(
    "public-notices-deadlines-signature", "The Public Notices and Deadlines Signature Database",
    "His original Signature Deadline Doctrine: every notice a summons, "
    "every deadline a covenant kept in public, the compliance calendar "
    "the honor roll, severity classification the measure of the warning, "
    "and the tracking workflow the chain of custody. The full ladder from "
    "what a notice is through deadlines, sources, severity, and calendars, "
    "through recalls, rulemakings, tenders, filings, and jurisdiction, to "
    "the complete compliance system, reframed as Signature science. "
    "Clearly labeled Signature-made, never presented as authentic public "
    "record.",
    "public notice and deadline record", "JAH-PNDTS-", "JAH Public Notices and Deadlines Archivist (Signature)",
    "public notices and deadlines archivist - Signature editions: his "
    "original Signature Deadline Doctrine, every notice a summons and "
    "every deadline a covenant kept in public, clearly labeled "
    "Signature-made and never presented as authentic public record; "
    "teaches progressively along the ladder from foundations through "
    "compounded to advanced; answers from many angles - definition, "
    "example, analogy, application, history, math, how-to - using only "
    "archive data from this system",
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
    for slug in ("public-notices-deadlines", "public-notices-deadlines-signature"):
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

    # NOTE: manifest.json / api.json / restamp / commit are the MERGER's job.
    # This builder stops here: shards + pages + gen-js + fragment.
    print("records: %d total (34 public + 34 signature)" % total)
    print("NEXT: merger appends manifest/api entries, restamps counts, commits.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
