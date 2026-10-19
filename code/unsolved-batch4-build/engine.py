#!/usr/bin/env python3
"""Shared build engine for the Unsolved Problems batch 4 (14 fields x 2 editions).

Manon's 16:15 orders, Unsolved Problems Solved series, batch 4 (humanities /
social fields): anthropology, archaeology, linguistics, political-science,
sociology, history, legal-studies, education, management, architecture,
urban-planning, musicology, art-history, literature.

Each field yields TWO databases, 34 ladder-ordered records each:

  unsolved-<field>             - The Unsolved <Field> Database
                                  (public-harvest: 34 famous open problems,
                                  real and fact-checked - problem stated
                                  rigorously with why it is unsolved, plus a
                                  short pointer to the Signature approach)
  unsolved-<field>-signature  - The Unsolved <Field> Signature Database
                                  (his original Signature solution method:
                                  the same 34 problems through the Signature
                                  lens, each carrying the full
                                  Signature-generated proposed solution -
                                  always labeled, never presented as
                                  established science; src signature, titles
                                  suffixed " (Signature Edition)")

34 records each, ladder-ordered by accessibility (ladder_rank 1-34, tiers
foundations/compounded/advanced); the shard index is written in ladder order
so pages present simple -> compounded -> complex.

LABEL GATE (the defect that bit twice - see
~/workspace/hidden_files/round8-skip-verifications.md sections 1-2):
  LABEL = "Signature-generated proposed solution \u2014 not established science."
  (em-dash U+2014, never a hyphen)
  signature how_it_works = LABEL + " " + sig_lens + " " + why + " " + sig_body
  public    how_it_works = LABEL + " " + why + " " + pointer
  Gate: EVERY record's how_it_works startswith LABEL (68/68 per pair), and
  zero hyphenated-label leftovers ("proposed solution - not established
  science") anywhere in any how_it_works.

ID prefixes verified free in the manifest id_prefix values (exact + substring)
and across all shard index files in jah-databases-data-1, 2026-10-17/18.

This build does NOT touch data/manifest.json, api.json, the hub index.html,
README.md, or docs/AI_ACCESS.md, and does NOT git commit or push - the
coordinator/merger handles registration. It writes per-pair fragment files
for the merger.

No website references. No Facebook. No religious framing. Nothing
hate-adjacent, profane, or inappropriate. History/archaeology: evidence
separated from speculation; contested claims never presented as settled.
"""

import gzip
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
FRAGDIR = "/home/hatch/workspace/hidden_files/missing-builds/fragments"

LABEL = "Signature-generated proposed solution \u2014 not established science."
HYPHEN_LABEL = "proposed solution - not established science"

sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate  # noqa: E402

# ---------------------------------------------------------------- field table
# (slug, display field name, public prefix, signature prefix, one-line scope)

FIELDS = [
    ("anthropology", "Anthropology", "JAH-USAN-", "JAH-USANS-",
     "the science of humanity: where we came from, why cultures differ, and what makes us human"),
    ("archaeology", "Archaeology", "JAH-USAR-", "JAH-USARS-",
     "the human past in material form: undeciphered scripts, lost cities, and the technologies time forgot"),
    ("linguistics", "Linguistics", "JAH-USLN-", "JAH-USLNS-",
     "the science of language: where language came from, why it changes, and how the mind handles it"),
    ("political-science", "Political Science", "JAH-USPO-", "JAH-USPOS-",
     "power and governance: why democracies rise and fall, why wars start, and what makes states work"),
    ("sociology", "Sociology", "JAH-USSO-", "JAH-USSOS-",
     "human society in groups: inequality, culture, networks, and how societies change"),
    ("history", "History", "JAH-USHI-", "JAH-USHIS-",
     "the recorded human past: collapses, divergences, disappearances, and the debates historians still fight"),
    ("legal-studies", "Legal Studies", "JAH-USLS-", "JAH-USLSS-",
     "law as a human system: what law can prove, where it fails, and how justice can be measured"),
    ("education", "Education", "JAH-USED-", "JAH-USEDS-",
     "how humans learn and how schools teach: the open questions beneath every classroom"),
    ("management", "Management", "JAH-USMG-", "JAH-USMGS-",
     "how organizations work: strategy, leadership, and why good management is still an unsolved problem"),
    ("architecture", "Architecture", "JAH-USAC-", "JAH-USACS-",
     "the built world: why buildings move us, how the ancients built, and what good building means"),
    ("urban-planning", "Urban Planning", "JAH-USUP-", "JAH-USUPS-",
     "cities as human systems: movement, housing, and the plans that shape millions of lives"),
    ("musicology", "Musicology", "JAH-USMU-", "JAH-USMUS-",
     "music as a human phenomenon: where it came from, why it moves us, and how it works"),
    ("art-history", "Art History", "JAH-USAH-", "JAH-USAHS-",
     "art across the ages: who made it, what it means, and the mysteries still hidden in the frame"),
    ("literature", "Literature", "JAH-USLT-", "JAH-USLTS-",
     "the written imagination: authorship, origins, and the texts that still will not give up their secrets"),
]

SLUGS = []
for _slug, _fname, _pp, _sp, _scope in FIELDS:
    SLUGS.append("unsolved-" + _slug)
    SLUGS.append("unsolved-" + _slug + "-signature")

FIELD_BY_SLUG = {}
for _slug, _fname, _pp, _sp, _scope in FIELDS:
    FIELD_BY_SLUG["unsolved-" + _slug] = (_fname, _pp, _scope, "public")
    FIELD_BY_SLUG["unsolved-" + _slug + "-signature"] = (_fname, _sp, _scope, "signature")


def _cfg(slug):
    fname, prefix, scope, source = FIELD_BY_SLUG[slug]
    sig = source == "signature"
    name = "The Unsolved %s %s Database" % (fname, "Signature" if sig else "")
    name = name.replace("  ", " ").strip()
    ai = "JAH Unsolved %s Archivist%s" % (fname, " (Signature)" if sig else "")
    tagline = ("Thirty-four of %s greatest unsolved problems - %s - each a fact-checked "
               "public record, each explored through a labeled Signature-generated proposed "
               "solution, taught in ladder order from the approachable to the profound."
               % (fname.lower(), scope))
    sig_line = ("Signature originals - his original Signature solution method: the same 34 famous "
                "unsolved %s problems approached as a covenant between the known and the unknown, "
                "each carrying the full Signature-generated proposed solution with its assumptions "
                "declared, its confirm and refute conditions stated, and its limits honestly marked. "
                "Clearly labeled Signature-made, never presented as established science or authentic "
                "public record." % fname.lower())
    pub_line = ("Public records - thirty-four of %s greatest unsolved problems, each fact-checked: "
                "the problem as the world knows it, its history, why it matters, and a pointer to "
                "the Signature system labeled proposed solution. Organized in the Signature system. "
                "Every record carries the full entry: problem, background, why it matters, the "
                "Signature-generated proposed solution (labeled as a proposal, never established "
                "science), key points, requirements, standards, citations, and a working "
                "solution-explorer demonstration program." % fname.lower())
    return {
        "name": name, "tagline": tagline, "record_kind": "unsolved problem record",
        "prefix": prefix, "ai": ai,
        "role": ("unsolved %s archivist - the famous open problems of %s, what is known about each, "
                 "why each matters, and the Signature system labeled proposed solution approaches; "
                 "teaches progressively along the ladder from foundations through compounded to "
                 "advanced; answers from many angles - definition, example, analogy, application, "
                 "history - using only archive data from this system" % (fname.lower(), fname.lower())),
        "hero_p": ("%s - %s Every record carries the full entry: problem, background, why it matters, "
                   "key points, requirements, standards, citations, and a working solution-explorer "
                   "demonstration program. Records are ordered by the teaching ladder: Foundations -> "
                   "Compounded -> Advanced." % (tagline, sig_line if sig else pub_line)),
        "sig_type": ("Signature originals organized in the Signature system" if sig else
                     "Public records organized in the Signature system"),
        "search_ph": "Search the great open problems of %s..." % fname.lower(),
        "chat_ph": "Ask about the great open problems of %s..." % fname.lower(),
        "archive_blurb": ("Seeded %s unsolved %s records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if sig else "public-record", fname.lower())),
        "schema": ("id, t, g, name, title, problem, background, why_it_matters, signature_solution, "
                   "description, how_it_works, key_points, requirements, standards, citations, src, "
                   "ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled unsolved %s studies. Seeded archive records are the authoritative entries." % fname.lower(),
        "greet": "I am the %s. Ask me about the great open problems of %s - what is known, why each matters, and the Signature system labeled proposed solution approach." % (ai, fname.lower()),
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "unsolved-%s-study" % slug.replace("unsolved-", "").replace("-signature", ""),
        "gen_demo_kind": "unsolved-%s-demo" % slug.replace("unsolved-", "").replace("-signature", ""),
        "source": source,
    }


DBCFG = {s: _cfg(s) for s in SLUGS}

SIG_TAIL = ("Signature original - his original Signature solution method: every unsolved problem "
            "approached as a covenant between the known and the unknown, the proposed path walked "
            "step by step with its assumptions declared, its confirm and refute conditions stated, "
            "and its limits honestly marked. Clearly labeled Signature-made, never presented as "
            "established science or authentic public record.")

# ---------------------------------------------------------------- demo factory

def _py_str(s):
    """Render a Python string literal safely (no triple-quote hazards)."""
    return json.dumps(str(s), ensure_ascii=False)


def demo_program(title, rid, group, hypotheses, key_points, requirements, confirm, refute):
    """Build a real, runnable solution-explorer demo program for one record.

    Deterministic: hypothesis scores derive from sha256(rid + hypothesis),
    normalized to sum 1 (asserted tight). Prints the record's own key points
    and requirements, a CONFIRM IF / REFUTE IF panel, and an OK marker.
    """
    lines = []
    lines.append("#!/usr/bin/env python3")
    lines.append('"""' + title.replace('"', "'") + " - solution-explorer demo.")
    lines.append("Record " + rid + " [" + group + "]. Property of Justin Addam Higgins (JAH).")
    lines.append('Structural walkthrough of the candidate explanations - not a proof."""')
    lines.append("import hashlib")
    lines.append("")
    lines.append("TITLE = " + _py_str(title))
    lines.append("RID = " + _py_str(rid))
    lines.append("GROUP = " + _py_str(group))
    lines.append("HYPOTHESES = [")
    for h in hypotheses:
        lines.append("    " + _py_str(h) + ",")
    lines.append("]")
    lines.append("N_KEY_POINTS = %d" % len(key_points))
    lines.append("N_REQUIREMENTS = %d" % len(requirements))
    lines.append("CONFIRM = " + _py_str(confirm))
    lines.append("REFUTE = " + _py_str(refute))
    lines.append("")
    lines.append("def weight(s):")
    lines.append("    h = hashlib.sha256(s.encode('utf-8')).hexdigest()")
    lines.append("    return (int(h[:8], 16) % 100000) / 100000.0")
    lines.append("")
    lines.append("def main():")
    lines.append("    print('Solution explorer :: ' + TITLE)")
    lines.append("    print('Record ' + RID + ' [' + GROUP + ']')")
    lines.append("    raw = {h: 0.05 + 0.95 * weight(RID + '|' + h) for h in HYPOTHESES}")
    lines.append("    total = sum(raw.values())")
    lines.append("    assert total > 0, 'empty hypothesis set'")
    lines.append("    norm = {h: v / total for h, v in raw.items()}")
    lines.append("    s = sum(norm.values())")
    lines.append("    assert abs(s - 1.0) < 1e-9, 'weights must normalize, got %r' % s")
    lines.append("    print('Candidate explanations ranked by the toy exploration model:')")
    lines.append("    for h, wv in sorted(norm.items(), key=lambda kv: -kv[1]):")
    lines.append("        bar = '#' * int(round(wv * 40))")
    lines.append("        print('  %5.1f%% %-40s :: %s' % (100 * wv, bar, h[:90]))")
    lines.append("    best = max(norm, key=norm.get)")
    lines.append("    print('Toy-model leader: ' + best[:100])")
    lines.append("    print('Key points carried: %d' % N_KEY_POINTS)")
    lines.append("    assert N_KEY_POINTS >= 3, 'record must carry at least 3 key points'")
    lines.append("    print('Requirements listed: %d' % N_REQUIREMENTS)")
    lines.append("    assert N_REQUIREMENTS >= 2, 'record must list at least 2 requirements'")
    lines.append("    assert len(HYPOTHESES) >= 3, 'need at least 3 hypotheses'")
    lines.append("    assert len(set(HYPOTHESES)) == len(HYPOTHESES), 'hypotheses must be distinct'")
    lines.append("    print('CONFIRM IF: ' + CONFIRM)")
    lines.append("    print('REFUTE IF: ' + REFUTE)")
    lines.append("    print('Note: the Signature proposal is labeled, not established science.')")
    lines.append("    print('OK: ' + RID + ' solution-explorer complete')")
    lines.append("")
    lines.append("main()")
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------- record build

def load_entries(field_slug):
    """Import the entries module for one field (unsolved-<field>)."""
    mod_name = "entries_" + field_slug.replace("-", "_")
    path = os.path.join(HERE, mod_name + ".py")
    spec = importlib.util.spec_from_file_location(mod_name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.ENTRIES


def build_records(slug, gate):
    cfg = DBCFG[slug]
    sig = cfg["source"] == "signature"
    field_slug = slug[:-len("-signature")] if sig else slug
    assert field_slug.startswith("unsolved-"), "unexpected slug form: %s" % slug
    field_slug = field_slug[len("unsolved-"):]
    entries = load_entries(field_slug)
    assert len(entries) == 34, "expected 34 entries for %s, got %d" % (field_slug, len(entries))
    keys = [e["key"] for e in entries]
    assert len(set(keys)) == 34, "duplicate entry keys in %s" % field_slug

    ordered = sorted(enumerate(entries), key=lambda p: (p[1]["ladder_rank"], p[0]))
    recs = []
    for _, e in ordered:
        name = e["name"]
        assert "'" not in name, "apostrophe in title: %s" % name
        title = name + " (Signature Edition)" if sig else name
        hits = [h for h in gate.check(slug, title) if h[0] != slug]
        if hits:
            raise AssertionError("dedupe gate refused (cross-db dupe): %s -> %r" % (title, hits[:3]))
        rid = "%s%06d" % (cfg["prefix"], len(recs) + 1)
        problem = e["problem"]
        background = e["background"]
        why = e["why_it_matters"]
        if sig:
            sig_body = e["sig_body"]
            assert HYPHEN_LABEL not in sig_body, "hyphenated label in sig_body: %s" % name
            description = ("Signature original interpretation. " + e["sig_lens"] + " "
                           + problem + " " + background)
            how = LABEL + " " + e["sig_lens"] + " " + why + " " + sig_body
            citations = list(e["citations"]) + [SIG_TAIL]
            src = "signature"
        else:
            description = problem + " " + background
            how = LABEL + " " + why + " " + e["pointer"]
            citations = list(e["citations"])
            src = "public-harvest"
        # ---- LABEL GATE (assert, both halves) ----
        assert how.startswith(LABEL), "honesty label not at record open: %s" % rid
        assert HYPHEN_LABEL not in how, "hyphenated label leftover in %s" % rid
        rec = {
            "id": rid, "t": title, "g": e["group"], "name": name, "title": title,
            "problem": problem, "background": background,
            "why_it_matters": why,
            "signature_solution": (LABEL + " " + e["sig_body"]) if sig else (
                LABEL + " The Signature system proposed approach to this problem is explored "
                "in full in the companion Signature Edition record (%s%06d)."
                % (FIELD_BY_SLUG["unsolved-" + field_slug + "-signature"][1], len(recs) + 1)),
            "description": description,
            "how_it_works": how,
            "key_points": list(e["key_points"]),
            "requirements": list(e["requirements"]),
            "standards": list(e["standards"]),
            "citations": citations,
            "src": src,
            "ladder_rank": e["ladder_rank"],
            "ladder_tier": e["ladder_tier"],
        }
        prog = demo_program(title, rid, e["group"], e["hypotheses"],
                            e["key_points"], e["requirements"],
                            e["confirm"], e["refute"])
        rec["demo"] = {"kind": "python", "language": "python",
                       "program": prog,
                       "note": "Solution-explorer walkthrough (real, runnable Python)."}
        gate.admit(slug, title, rid)
        recs.append(rec)
    ranks = [r["ladder_rank"] for r in recs]
    assert ranks == list(range(1, 35)), "ladder ranks must be 1-34 in %s" % slug
    return recs


def validate_records(slug, recs):
    cfg = DBCFG[slug]
    sig = cfg["source"] == "signature"
    ids = [r["id"] for r in recs]
    assert len(ids) == len(set(ids)), "dup ids in %s" % slug
    assert all(i.startswith(cfg["prefix"]) for i in ids), "prefix drift in %s" % slug
    assert len(recs) == 34, "expected 34 records in %s, got %d" % (slug, len(recs))
    for r in recs:
        for k in ("id", "t", "g", "name", "title", "problem", "background",
                  "why_it_matters", "signature_solution", "description",
                  "how_it_works", "key_points", "requirements", "standards",
                  "citations", "src", "ladder_rank", "ladder_tier", "demo"):
            assert k in r, "missing %s in %s" % (k, r["id"])
        prog = r["demo"].get("program")
        assert prog and len(r["description"]) > 200, "stub in %s" % r["id"]
        assert len(r["how_it_works"]) > 300, "thin how_it_works in %s" % r["id"]
        assert 1 <= r["ladder_rank"] <= 34
        assert r["ladder_tier"] in ("foundations", "compounded", "advanced")
        assert len(r["key_points"]) >= 3, "key_points thin in %s" % r["id"]
        assert len(r["requirements"]) >= 2, "requirements thin in %s" % r["id"]
        assert len(r["citations"]) >= 2, "citations thin in %s" % r["id"]
        compile(prog, r["id"], "exec")
        blob = json.dumps(r).lower()
        assert "facebook" not in blob, "facebook ref in %s" % r["id"]
        assert "bat belt" not in blob, "banned phrase in %s" % r["id"]
        # LABEL GATE: startswith on both halves + zero hyphen leftovers
        assert r["how_it_works"].startswith(LABEL), \
            "honesty label not at record open in %s" % r["id"]
        assert HYPHEN_LABEL not in r["how_it_works"], \
            "hyphenated label leftover in %s" % r["id"]
        assert HYPHEN_LABEL not in r["signature_solution"], \
            "hyphenated label in signature_solution %s" % r["id"]
        if sig:
            assert "(signature edition)" in r["title"].lower(), "sig title missing suffix"
            assert r["src"] == "signature"
        else:
            assert r["src"] == "public-harvest"


def run_demos(recs):
    for r in recs:
        prog = r["demo"]["program"]
        p = subprocess.run([sys.executable, "-c", prog],
                           capture_output=True, text=True, timeout=120)
        assert p.returncode == 0, "demo failed %s: %s" % (r["id"], p.stderr[-800:])
        assert "OK:" in p.stdout, "demo no OK marker %s" % r["id"]
        assert "CONFIRM IF:" in p.stdout and "REFUTE IF:" in p.stdout, \
            "demo missing confirm/refute panel %s" % r["id"]


def node_check(path):
    p = subprocess.run(["node", "--check", path], capture_output=True, text=True, timeout=60)
    assert p.returncode == 0, "node --check failed for %s: %s" % (path, p.stderr[-500:])

# ---------------------------------------------------------------- pages + gen

def write_pages(slug, recs):
    cfg = DBCFG[slug]
    spec = importlib.util.spec_from_file_location(
        "nb_build", os.path.join(REPO, "code", "numbering-build", "build.py"))
    nb = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(nb)
    nb.DBCFG = DBCFG

    sweep_path = "/home/hatch/workspace/goals/database-quality-audit/hidden_files/patches/sweep-db-pages.py"
    sspec = importlib.util.spec_from_file_location("sweep", sweep_path)
    sweep = importlib.util.module_from_spec(sspec)
    sspec.loader.exec_module(sweep)

    with open(TEMPLATE, "r", encoding="utf-8") as f:
        template = f.read()
    page = nb.build_page(slug, template)
    page = page.replace(
        "Generate structural synthetic intelligence studies. Seeded archive records are the authoritative entries.",
        cfg["gen_desc"])
    assert 'id="stCount"' in page and "var SLUG='%s';" % slug in page
    assert "minmax(120px,1fr)" in page and "pre.codeblock" in page
    assert "pill-ex" in page and "qmerge" in page, "Exhaustive pill / merger button missing"
    assert "dataset.p" in page, "tab-handler guard missing"
    assert "facebook" not in page.lower()
    assert "synthetic intelligence" not in page.lower(), "template leftover in %s" % slug
    assert "public-synthetic-intelligence" not in page, "slug leftover in %s" % slug
    assert "bat belt" not in page.lower(), "banned phrase in page %s" % slug
    for k in ("role", "ai", "greet", "search_ph", "chat_ph", "gen_desc"):
        assert "'" not in cfg[k], "apostrophe in cfg %s for %s" % (k, slug)

    ddir = os.path.join(REPO, "db", slug)
    os.makedirs(ddir, exist_ok=True)
    ppath = os.path.join(ddir, "index.html")
    with open(ppath, "w", encoding="utf-8") as f:
        f.write(page)
    changed, notes = sweep.process_page(ppath)

    scripts = re.findall(r'<script(?![^>]*type="application/ld\+json")[^>]*>(.*?)</script>',
                         page, flags=re.S)
    for i, body in enumerate(scripts):
        if body.strip():
            tmp = "/tmp/b4_pagescript_%s_%d.js" % (slug.replace("-", "_"), i)
            with open(tmp, "w", encoding="utf-8") as f:
                f.write(body)
            node_check(tmp)

    tier_label = {"foundations": "Foundations", "compounded": "Compounded",
                  "advanced": "Advanced"}
    topics = {}
    for r in recs:
        topics.setdefault(tier_label[r["ladder_tier"]], []).append(
            "%s - %s" % (r["t"], r["g"]))
    gen_js = nb.build_gen_js(slug, topics, cfg)
    assert "facebook" not in gen_js.lower() and "bat belt" not in gen_js.lower()
    assert "synthetic intelligence" not in gen_js.lower(), "field leftover in gen js %s" % slug
    gpath = os.path.join(ddir, "gen-%s.js" % slug)
    with open(gpath, "w", encoding="utf-8") as f:
        f.write(gen_js)
    node_check(gpath)
    print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)


def write_shard_db(slug, recs):
    def write_gz_jsonl(path, rows):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with gzip.open(path, "wt", encoding="utf-8") as f:
            for r in rows:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")

    base = os.path.join(SHARD, "data", slug)
    light = [{"id": r["id"], "t": r["t"], "g": r["g"]} for r in recs]
    write_gz_jsonl(os.path.join(base, "index.jsonl.gz"), light)
    for ci in range(0, len(recs), 100):
        write_gz_jsonl(os.path.join(base, "chunks", "chunk-%04d.jsonl.gz" % (ci // 100)),
                       recs[ci:ci + 100])
    return len(recs)


def write_fragment(slug, recs):
    c = DBCFG[slug]
    idx = SHARD_BASE + "/data/" + slug + "/index.jsonl.gz"
    frag = {
        "slug": slug, "name": c["name"], "tagline": c["tagline"],
        "record_kind": c["record_kind"], "id_prefix": c["prefix"],
        "ai_name": c["ai"], "local_index": idx, "record_count": len(recs),
        "status": "staged", "full_records": len(recs), "index": idx,
        "chunk_pattern": "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz",
        "source": "public-harvest" if not slug.endswith("-signature") else "signature",
    }
    os.makedirs(FRAGDIR, exist_ok=True)
    fpath = os.path.join(FRAGDIR, slug + ".json")
    with open(fpath, "w", encoding="utf-8") as f:
        json.dump(frag, f, indent=2, ensure_ascii=False)
        f.write("\n")
    return fpath


# ---------------------------------------------------------------- main

def build_pair(field, gate):
    """Build one field's pair (public + signature). Returns {slug: recs}."""
    out = {}
    for slug in ("unsolved-" + field, "unsolved-" + field + "-signature"):
        recs = build_records(slug, gate)
        validate_records(slug, recs)
        out[slug] = recs
    return out


def main(slugs=None):
    targets = slugs or SLUGS
    gate = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))
    built = {}
    fields_done = []
    for slug in targets:
        if slug in built:
            continue
        field = slug[:-len("-signature")] if slug.endswith("-signature") else slug
        field = field[len("unsolved-"):]
        pair = build_pair(field, gate)
        for s, recs in pair.items():
            built[s] = recs
        fields_done.append(field)
        print("records: %-42s 34 + 34 staged" % field, flush=True)

    total = 0
    for slug, recs in built.items():
        run_demos(recs)
        total += len(recs)
        n = write_shard_db(slug, recs)
        print("shard: %-38s %d records" % (slug, n), flush=True)
        write_pages(slug, recs)
        fp = write_fragment(slug, recs)
        print("fragment: %s" % fp, flush=True)
    print("demo execution: all %d demos ran OK" % total, flush=True)

    # ---- label-gate proof (per pair: 34 public + 34 signature = 68) ----
    seen_pairs = []
    for slug in built:
        pair = slug[:-len("-signature")] if slug.endswith("-signature") else slug
        if pair in seen_pairs:
            continue
        seen_pairs.append(pair)
        pair_recs = built[pair] + built[pair + "-signature"]
        ok = sum(1 for r in pair_recs if r["how_it_works"].startswith(LABEL))
        hy = sum(1 for r in pair_recs if HYPHEN_LABEL in r["how_it_works"])
        sse = sum(1 for r in pair_recs if HYPHEN_LABEL in r["signature_solution"])
        print("label-gate: %-38s %d/68 startswith, %d hyphen leftovers (how), %d (sig_solution)"
              % (pair, ok, hy, sse), flush=True)
        assert ok == 68 and hy == 0 and sse == 0, "label gate failed for %s" % pair
    print("NOTE: manifest/api/hub/README/docs NOT touched - merger handles registration. No commit/push done.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
