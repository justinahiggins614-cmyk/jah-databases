#!/usr/bin/env python3
"""Build the Describing Solves databases for JAH Databases
(Manon's 2026-10-17 17:55 order: "All types of describing solves
databases" - solution-description databases: how problems and their
solutions are described and worked through, across every type).

So this build creates two NEW databases, 34 ladder-ordered records each:

  describing-solves                - The Describing Solves Database
                                     (public-harvest: real, documented
                                     descriptive-solution knowledge -
                                     worked examples, solution schemas
                                     and templates, proof and explanation
                                     write-ups, diagnostic narratives,
                                     repair walkthroughs, how-to-describe
                                     methods, solution presentations for
                                     math, science, engineering, craft,
                                     and everyday problems, explanation
                                     best practices, describing partial
                                     solutions and dead ends, solution
                                     storytelling; src public-harvest)
  describing-solves-signature      - The Describing Solves Signature
                                     Database (his original Signature
                                     lens: solution-describing as his own
                                     original craft - the Signature way
                                     of walking a problem from statement
                                     to worked-through answer; src
                                     signature, titles suffixed
                                     " (Signature Edition)", clearly
                                     labeled Signature-made, never
                                     presented as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
non-decreasing; tiers foundations/compounded/advanced); the shard index is
written in ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-DSV- (public) and JAH-DSVS- (signature), verified free:
zero hits across ALL data/manifest.json id_prefix values, zero hits in all
jah-databases-data-1/data record IDs, and zero topical overlap (no existing
"describing solves" / "solution description" database names), 2026-10-17.

Every demo is a solution-description checker or simulator: real, runnable,
stdlib-only Python that performs the actual computation for its record,
prints the real computed values, asserts tight bounds (never float
exact-equality), and ends with the OK marker (see
demos_describing_solves.py). All are machine-executed by this build before
writing.

CONCURRENCY: this builder NEVER touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md and NEVER runs git commit or
git push. A merger handles those. It writes ONLY: db/describing-solves/ +
db/describing-solves-signature/ (index.html + gen-*.js), the shard dirs
under ~/workspace/jah-databases-data-1/data/, and the fragment JSON for the
merger at ~/workspace/hidden_files/missing-builds/fragments/.

No website references. No Facebook. Screened: nothing hate-adjacent,
profane, or inappropriate.
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
FRAGMENTS = "/home/hatch/workspace/hidden_files/missing-builds/fragments"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_describing_solves import ENTRIES, SIG_TAIL
from demos_describing_solves import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, source):
    sig_line = ("Signature originals - his original Signature craft of "
                "solution-describing: his own way of walking a problem "
                "from statement to worked-through answer, framed as the "
                "Signature method - the seal on the work, the witness of "
                "every step. Clearly labeled Signature-made, never "
                "presented as authentic public record.")
    pub_line = ("Public records - real, documented descriptive-solution "
                "knowledge: worked examples, solution schemas and "
                "templates, proof and explanation write-ups, diagnostic "
                "narratives, repair walkthroughs, how-to-describe "
                "methods, solution presentations for math, science, "
                "engineering, craft, and everyday problems, explanation "
                "best practices, describing partial solutions and dead "
                "ends, and solution storytelling.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(what a described solution is, stating the problem first, "
              "worked examples, showing the work, step ordering, naming "
              "tools, given-find-plan, labeling moves, the check step, "
              "think-aloud lines, pointing at the work, reading "
              "direction) -> Compounded (solution schemas, fill-in "
              "templates, critical reading, dead ends, partial "
              "solutions, diagnostic narratives, repair walkthroughs, "
              "and written presentations for math, science, engineering, "
              "craft, and everyday problems) -> Advanced (proof "
              "write-ups, how-to-describe methods, solution "
              "storytelling, trade-offs, comparing two solutions, the "
              "rubric view, best practices, presenting to a group, the "
              "debugging log pattern, and the full worked-through "
              "solution system).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search worked examples, solution schemas, proof write-ups, diagnostic narratives, repair walkthroughs, templates, presentations, best practices...",
        "chat_ph": "Ask about describing solutions...",
        "archive_blurb": ("Seeded %s solution-description records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced. "
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled solution-description studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about describing solutions - worked examples, schemas and templates, proof and explanation write-ups, diagnostic narratives, repair walkthroughs, how-to-describe methods, presentations for math science engineering craft and everyday problems, best practices, partial solutions, dead ends, and solution storytelling." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "describing-solve-study", "gen_demo_kind": "describing-solve-demo",
        "source": source,
    }

DBCFG = {}
DBCFG["describing-solves"] = _cfg(
    "describing-solves", "The Describing Solves Database",
    "All types of describing solves: how problems and their solutions are "
    "described and worked through, across every type - worked examples, "
    "solution schemas and templates, proof and explanation write-ups, "
    "diagnostic narratives, repair walkthroughs, how-to-describe methods, "
    "and solution presentations for math, science, engineering, craft, and "
    "everyday problems. Real, documented knowledge, taught progressively "
    "along the ladder.",
    "solution-description record", "JAH-DSV-", "JAH Describing Solves Archivist",
    "describing solves archivist - solution-description types: worked "
    "examples, schemas and templates, proof and explanation write-ups, "
    "diagnostic narratives, repair walkthroughs, how-to-describe methods, "
    "solution presentations for math science engineering craft and everyday "
    "problems, best practices, partial solutions, dead ends, solution "
    "storytelling; teaching progressively along the ladder from foundations "
    "through compounded to advanced; answers from many angles - definition, "
    "example, analogy, application, history, how-to - using only archive "
    "data from this system",
    "public")
DBCFG["describing-solves-signature"] = _cfg(
    "describing-solves-signature", "The Describing Solves Signature Database",
    "His original Signature craft of solution-describing: his own way of "
    "walking a problem from statement to worked-through answer across every "
    "type - worked examples, schemas, write-ups, narratives, walkthroughs, "
    "presentations, best practices, storytelling. Clearly labeled "
    "Signature-made, never presented as authentic public record.",
    "solution-description record", "JAH-DSVS-", "JAH Describing Solves Archivist (Signature)",
    "describing solves archivist - Signature editions: his original "
    "Signature craft of solution-describing, the Signature way of walking a "
    "problem from statement to worked-through answer - clearly labeled "
    "Signature-made and never presented as authentic public record; teaches "
    "progressively along the ladder from foundations through compounded to "
    "advanced; answers from many angles - definition, example, analogy, "
    "application, history, how-to - using only archive data from this system",
    "signature")

base.DBCFG = DBCFG

assert set(DEMOS) == {e["key"] for e in ENTRIES}, "demo map misses entries"


def preflight_dedupe():
    """Whole-system title check BEFORE authoring records: all 68 titles."""
    refused = []
    for slug in ("describing-solves", "describing-solves-signature"):
        sig = slug.endswith("-signature")
        for e in ENTRIES:
            title = e["name"] + " (Signature Edition)" if sig else e["name"]
            hits = [h for h in base.GATE.check(slug, title) if h[0] != slug]
            if hits:
                refused.append((title, hits))
    if refused:
        for title, hits in refused:
            print("REFUSED: %r already in %s" % (title, hits), flush=True)
        raise SystemExit("dedupe preflight refused %d titles" % len(refused))
    print("dedupe preflight: 68 titles checked vs whole system, zero collisions", flush=True)


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
                       "note": "Working demonstration program (real, runnable Python) - solution-description checker and simulator."}
        base.GATE.admit(slug, title, rid)
        recs.append(rec)
    ranks = [r["ladder_rank"] for r in recs]
    assert ranks == sorted(ranks), "records not in ladder order for %s" % slug
    return recs


def write_fragment(built):
    pub = {
        "slug": "describing-solves",
        "name": "The Describing Solves Database",
        "tagline": DBCFG["describing-solves"]["tagline"],
        "record_kind": "solution-description record",
        "id_prefix": "JAH-DSV-",
        "ai_name": "JAH Describing Solves Archivist",
        "local_index": SHARD_BASE + "/data/describing-solves/index.jsonl.gz",
        "record_count": len(built["describing-solves"]),
        "status": "live",
        "full_records": len(built["describing-solves"]),
        "index": SHARD_BASE + "/data/describing-solves/index.jsonl.gz",
        "chunk_pattern": "data/describing-solves/chunks/chunk-NNNN.jsonl.gz",
        "source": "public-harvest",
    }
    sig = {
        "slug": "describing-solves-signature",
        "name": "The Describing Solves Signature Database",
        "tagline": DBCFG["describing-solves-signature"]["tagline"],
        "record_kind": "solution-description record",
        "id_prefix": "JAH-DSVS-",
        "ai_name": "JAH Describing Solves Archivist (Signature)",
        "local_index": SHARD_BASE + "/data/describing-solves-signature/index.jsonl.gz",
        "record_count": len(built["describing-solves-signature"]),
        "status": "live",
        "full_records": len(built["describing-solves-signature"]),
        "index": SHARD_BASE + "/data/describing-solves-signature/index.jsonl.gz",
        "chunk_pattern": "data/describing-solves-signature/chunks/chunk-NNNN.jsonl.gz",
        "source": "signature",
    }
    os.makedirs(FRAGMENTS, exist_ok=True)
    fpath = os.path.join(FRAGMENTS, "describing-solves.json")
    with open(fpath, "w", encoding="utf-8") as f:
        json.dump({"public": pub, "signature": sig}, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print("fragment: %s" % fpath, flush=True)
    return fpath


def node_check_js(path):
    """node --check every <script> block except ld+json (JSON, not JS)."""
    with open(path, encoding="utf-8") as f:
        html = f.read()
    blocks = re.findall(r'<script(?![^>]*type="application/ld\+json")[^>]*>(.*?)</script>',
                        html, flags=re.S)
    assert blocks, "no script blocks found in %s" % path
    import tempfile
    for i, b in enumerate(blocks):
        if not b.strip():
            continue
        with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as tf:
            tf.write(b)
            tpath = tf.name
        p = subprocess.run(["node", "--check", tpath],
                           capture_output=True, text=True, timeout=60)
        os.unlink(tpath)
        assert p.returncode == 0, "node --check failed block %d in %s: %s" % (i, path, p.stderr[:500])
    # gen js files
    ddir = os.path.dirname(path)
    for fn in sorted(os.listdir(ddir)):
        if fn.startswith("gen-") and fn.endswith(".js"):
            gp = os.path.join(ddir, fn)
            p = subprocess.run(["node", "--check", gp], capture_output=True, text=True, timeout=60)
            assert p.returncode == 0, "node --check failed %s: %s" % (gp, p.stderr[:500])
    print("node --check clean: %s (+gen js)" % path, flush=True)


def main():
    if not os.path.exists("/home/hatch/workspace/hidden_files/db-writer-free.marker"):
        raise SystemExit("db-writer-free.marker absent - STOPPING")
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

    preflight_dedupe()

    built = {}
    for slug in ("describing-solves", "describing-solves-signature"):
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
            if slug.endswith("-signature"):
                assert "(signature edition)" in r["title"].lower(), "sig title missing suffix"
                assert r["src"] == "signature"
            else:
                assert r["src"] == "public-harvest"
        total += len(recs)
        n = base.write_shard_db(slug, recs)
        print("shard: %-32s %d records" % (slug, n), flush=True)

    # machine-execute all 68 demos
    for slug, recs in built.items():
        for r in recs:
            prog = r["demo"]["program"]
            p = subprocess.run([sys.executable, "-c", prog],
                               capture_output=True, text=True, timeout=180)
            assert p.returncode == 0, "demo failed %s: %s" % (r["id"], p.stderr[-800:])
            assert "OK:" in p.stdout, "demo no OK marker %s" % r["id"]
    print("demo execution: all %d demos ran OK" % total, flush=True)

    # cross-check: demo OK-line names match entry titles
    for slug, recs in built.items():
        sig = slug.endswith("-signature")
        for r in recs:
            p = subprocess.run([sys.executable, "-c", r["demo"]["program"]],
                               capture_output=True, text=True, timeout=60)
            ok_line = [l for l in p.stdout.splitlines() if l.startswith("OK:")][0]
            assert r["title"] in ok_line or r["name"] in ok_line, \
                "demo/title mismatch in %s" % r["id"]
    print("cross-check: all demo OK lines match entry titles", flush=True)

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
        # apostrophe-free JS strings: role/ai/greet/search_ph
        for key in ("role", "ai", "greet", "search_ph"):
            assert "'" not in DBCFG[slug][key], "apostrophe in %s.%s" % (slug, key)
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
        assert "solv" in gen_js.lower(), "field leftover in gen js %s" % slug
        with open(os.path.join(ddir, "gen-%s.js" % slug), "w", encoding="utf-8") as f:
            f.write(gen_js)
        node_check_js(ppath)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)

    fpath = write_fragment(built)
    print("DONE: %d databases, %d records. manifest/api/index.html untouched; no git run." % (len(built), total))
    print("fragment: %s" % fpath)
    print("NEXT (merger): merge fragment, run code/restamp_counts.py, commit + push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
