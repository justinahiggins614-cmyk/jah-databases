#!/usr/bin/env python3
"""Build the AI Reasoning databases for JAH Databases
(Manon's order 2026-10-18 22:37 EDT, refined 22:38 + 22:59 EDT).

One database per AI reasoning/communication ability, public + Signature
edition, 34 full ladder-ordered records each, LAST = the UNITED master
synthesizing all 24 abilities.

Roster (25 abilities x 2 = 50 databases, 1700 records):
  session-memory, long-term-memory, episodic-memory, semantic-memory,
  procedural-memory, chain-of-thought, planning-decomposition, tool-use,
  rag-retrieval, summarization, question-answering, self-correction,
  multi-agent, persona-communication, code-reasoning, math-reasoning,
  multimodal, working-memory, explanation, instruction-following,
  context-window-management, negotiation, teaching-explanation,
  uncertainty-handling, united (LAST, the master).

ID prefixes: JAH-AIR-<CODE>- (public) / JAH-AIR-<CODE>S- (signature),
verified free in the manifest id_prefix values and with zero hits in
every shard index file (checked 2026-10-18).

Demos: 14 archetype generators in demos_ai_reasoning.py, parameterized
by record rank; every demo is real, runnable, stdlib-only Python that
computes real values from rank-derived data, prints them, asserts tight
bounds (never float exact-equality), and ends with the OK marker.
The build machine-executes all 1700 demos.

Honesty: public records teach established methods (src public-harvest);
Signature editions are his original Signature method, clearly labeled
(src signature, SIG_TAIL citation, titles suffixed " (Signature
Edition)"), never presented as authentic public record.

Concurrency: this builder writes ONLY its own new untracked paths -
db/ai-reasoning-*/, the data-1 shard dirs, code/ai-reasoning-build/,
and fragment files under hidden_files/missing-builds/fragments/.
It never touches data/manifest.json, api.json, index.html, README.md,
and never commits or pushes. A merger handles those.

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
FRAGDIR = "/home/hatch/workspace/hidden_files/missing-builds/fragments"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_ai_reasoning import ENTRIES, ORDER, CODES, ABILITIES, SIG_TAIL
from demos_ai_reasoning import DEMOS

# ---------------------------------------------------------------- DB config

SCHEMA = ("id, t, g, name, title, description, how_it_works, key_points, "
          "requirements, standards, citations, src, ladder_rank, ladder_tier, demo")
FIELDS = ("Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on "
          "demand and loads only what you open")


def _ladder_sentence(ability):
    parts = []
    for tier, label in (("foundations", "Foundations"),
                        ("compounded", "Compounded"),
                        ("advanced", "Advanced")):
        items = [e["name"] for e in ENTRIES[ability]
                 if e["ladder_tier"] == tier]
        parts.append("%s (%s)" % (label, ", ".join(items)))
    return (" Records are ordered by the teaching ladder: "
            + " -> ".join(parts) + ".")


def _cfg(ability, source):
    prof = ABILITIES[ability]
    code = CODES[ability]
    sig = source == "signature"
    prefix = "JAH-AIR-%s%s-" % (code, "S" if sig else "")
    name = ("The AI %s Signature Database" % prof["name"] if sig
            else "The AI %s Database" % prof["name"])
    ai = prof["ai"] + (" (Signature)" if sig else "")
    return {
        "name": name,
        "tagline": prof["tagline"],
        "record_kind": prof["record_kind"],
        "prefix": prefix,
        "ai": ai,
        "role": prof["role"],
        "hero_p": "%s - %s Every record carries the full entry: description, "
                  "how it works, key points, requirements, standards, "
                  "citations, and a working demonstration program.%s"
                  % (prof["tagline"],
                     prof["sig_line"] if sig else prof["pub_line"],
                     _ladder_sentence(ability)),
        "sig_type": ("Signature originals organized in the Signature system"
                     if sig else
                     "Public records organized in the Signature system"),
        "search_ph": prof["search_ph"],
        "chat_ph": prof["chat_ph"],
        "archive_blurb": ("Seeded %s AI %s records, marching toward one "
                          "million records. Presented in teaching-ladder "
                          "order: foundations, compounded, advanced."
                          % ("Signature-original" if sig else "public-record",
                             prof["name"].lower())),
        "schema": SCHEMA,
        "fields": FIELDS,
        "gen_desc": prof["gen_desc"],
        "greet": prof["greet"].replace("%s", ai, 1),
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": prof["gen_kind"],
        "gen_demo_kind": prof["gen_demo_kind"],
        "source": source,
        "ability": ability,
    }


DBCFG = {}
SLUGS = []
for _ability in ORDER:
    for _src, _sfx in (("public", ""), ("signature", "-signature")):
        _slug = "ai-reasoning-%s%s" % (_ability, _sfx)
        DBCFG[_slug] = _cfg(_ability, _src)
        SLUGS.append(_slug)

base.DBCFG = DBCFG

_all_keys = [e["demo_key"] for _k in ORDER for e in ENTRIES[_k]]
assert len(_all_keys) == 850 and len(set(_all_keys)) == 850
assert set(DEMOS) == set(_all_keys), "demo map misses entries"


def build_records(slug, source):
    cfg = DBCFG[slug]
    ability = cfg["ability"]
    sig = source == "signature"
    entries = ENTRIES[ability]
    ordered = sorted(enumerate(entries),
                     key=lambda p: (p[1]["ladder_rank"], p[0]))
    recs = []
    skipped = []
    for _, e in ordered:
        name = e["name"]
        title = name + " (Signature Edition)" if sig else name
        if [h for h in base.GATE.check(slug, title) if h[0] != slug]:
            skipped.append(title)
            continue
        rid = "%s%06d" % (cfg["prefix"], len(recs) + 1)
        if sig:
            description = ("Signature original interpretation. "
                           + e["sig_lens"] + " " + e["description"])
            how = e["sig_lens"] + " " + e["how_it_works"]
            citations = list(e["citations"]) + [SIG_TAIL]
        else:
            description = e["description"]
            how = e["how_it_works"]
            citations = list(e["citations"])
        rec = {
            "id": rid, "t": title, "g": e["group"], "name": name,
            "title": title,
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
        demo_fn = DEMOS[e["demo_key"]]
        program = demo_fn(base._hdr, name if not sig else title, rid,
                          e["group"],
                          {"rank": e["ladder_rank"],
                           "code": e["demo_key"].split("-")[0]})
        rec["demo"] = {"kind": "python", "language": "python",
                       "program": program,
                       "note": "Working demonstration program (real, runnable Python)."}
        base.GATE.admit(slug, title, rid)
        recs.append(rec)
    ranks = [r["ladder_rank"] for r in recs]
    assert ranks == sorted(ranks), "records not in ladder order for %s" % slug
    return recs, skipped


def write_fragment(ability, built):
    pub_slug = "ai-reasoning-%s" % ability
    sig_slug = pub_slug + "-signature"
    frag = {}
    for slug, side in ((pub_slug, "public"), (sig_slug, "signature")):
        cfg = DBCFG[slug]
        recs = built[slug]
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
    path = os.path.join(FRAGDIR, "ai-reasoning-%s.json" % ability)
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

    sweep_path = ("/home/hatch/workspace/goals/database-quality-audit/"
                  "hidden_files/patches/sweep-db-pages.py")
    sspec = importlib.util.spec_from_file_location("sweep", sweep_path)
    sweep = importlib.util.module_from_spec(sspec)
    sspec.loader.exec_module(sweep)

    built = {}
    all_skipped = {}
    for slug in SLUGS:
        source = "signature" if slug.endswith("-signature") else "public"
        recs, skipped = build_records(slug, source)
        built[slug] = recs
        all_skipped[slug] = skipped
        print("records: %-42s %d (skipped %d)" % (slug, len(recs), len(skipped)),
              flush=True)

    total = 0
    for slug, recs in built.items():
        cfg = DBCFG[slug]
        ids = [r["id"] for r in recs]
        assert len(ids) == len(set(ids)), "dup ids in %s" % slug
        assert all(i.startswith(cfg["prefix"]) for i in ids), \
            "prefix drift in %s" % slug
        assert len(recs) == 34, \
            "expected 34 records in %s, got %d" % (slug, len(recs))
        for r in recs:
            for k in ("id", "t", "g", "name", "title", "description",
                      "how_it_works", "key_points", "requirements",
                      "standards", "citations", "src", "ladder_rank",
                      "ladder_tier", "demo"):
                assert k in r, "missing %s in %s" % (k, r["id"])
            prog = r["demo"].get("program")
            assert prog and len(r["description"]) > 200, "stub in %s" % r["id"]
            assert 1 <= r["ladder_rank"] <= 34, \
                "ladder_rank out of range in %s" % r["id"]
            assert r["ladder_tier"] in ("foundations", "compounded",
                                        "advanced"), \
                "bad ladder_tier in %s" % r["id"]
            compile(prog, r["id"], "exec")
            blob = json.dumps(r).lower()
            assert "facebook" not in blob, "facebook ref in %s" % r["id"]
            assert "bat belt" not in blob, "banned phrase in %s" % r["id"]
            if slug.endswith("-signature"):
                assert "(signature edition)" in r["title"].lower(), \
                    "sig title missing suffix"
                assert r["src"] == "signature"
            else:
                assert r["src"] == "public-harvest"
        total += len(recs)
        n = base.write_shard_db(slug, recs)
        print("shard: %-42s %d records" % (slug, n), flush=True)

    for slug, recs in built.items():
        for r in recs:
            prog = r["demo"]["program"]
            p = subprocess.run([sys.executable, "-c", prog],
                               capture_output=True, text=True, timeout=180)
            assert p.returncode == 0, \
                "demo failed %s: %s" % (r["id"], p.stderr[-800:])
            assert "OK:" in p.stdout, "demo no OK marker %s" % r["id"]
    print("demo execution: all %d demos ran OK" % total, flush=True)

    with open(TEMPLATE, "r", encoding="utf-8") as f:
        template = f.read()
    node = None
    for slug, recs in built.items():
        page = nb.build_page(slug, template)
        page = page.replace(
            "Generate structural synthetic intelligence studies. Seeded archive "
            "records are the authoritative entries.",
            DBCFG[slug]["gen_desc"])
        assert 'id="stCount"' in page and "var SLUG='%s';" % slug in page
        assert "minmax(120px,1fr)" in page and "pre.codeblock" in page
        assert "pill-ex" in page and "qmerge" in page, \
            "Exhaustive pill / merger button missing"
        assert "dataset.p" in page, "tab-handler guard missing"
        assert "facebook" not in page.lower()
        assert "synthetic intelligence" not in page.lower(), \
            "template leftover in %s" % slug
        assert "universal build" not in page.lower(), \
            "field leftover in %s" % slug
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
        assert "universal build" not in gen_js.lower(), \
            "field leftover in gen js %s" % slug
        gpath = os.path.join(ddir, "gen-%s.js" % slug)
        with open(gpath, "w", encoding="utf-8") as f:
            f.write(gen_js)
        print("page:  db/%s/index.html + gen-%s.js [%s]"
              % (slug, slug, ", ".join(notes)), flush=True)

    # node --check every generated gen file
    import shutil
    node = shutil.which("node")
    if node:
        bad = []
        for slug in SLUGS:
            gpath = os.path.join(REPO, "db", slug, "gen-%s.js" % slug)
            p = subprocess.run([node, "--check", gpath],
                               capture_output=True, text=True, timeout=60)
            if p.returncode != 0:
                bad.append((slug, p.stderr[-400:]))
        assert not bad, "node --check failures: %s" % bad
        print("node --check: all %d gen files OK" % len(SLUGS), flush=True)
    else:
        print("node not found; skipped node --check", flush=True)

    for ability in ORDER:
        write_fragment(ability, built)

    nskip = sum(len(v) for v in all_skipped.values())
    print("records: %d databases x 34 = %d total (gate-skipped: %d)"
          % (len(SLUGS), total, nskip))
    print("NOTE: manifest.json / api.json / restamp left to the merger; "
          "no commit, no push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
