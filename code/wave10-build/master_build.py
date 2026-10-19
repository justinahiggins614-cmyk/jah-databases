#!/usr/bin/env python3
"""Wave 10 master builder: versus-rankings (36) + learning (26) = 62 items.

For each item builds a public + Signature database pair (124 databases), 34
full records each:

  db page : ~/workspace/jah-databases/db/<slug>/index.html
  gen js  : ~/workspace/jah-databases/db/<slug>/gen-<slug>.js
  data    : ~/workspace/jah-databases-data-1/data/<slug>/index.jsonl.gz + chunks/chunk-0000.jsonl.gz

Staged only. NEVER touches data/manifest.json or api.json - the coordinator
merges. A manifest-entry.json fragment is staged in each item's build dir for
the coordinator.

Usage: python3 master_build.py [item-slug ...]
       (no args = build everything)
"""
import importlib.util
import json
import os
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = "/home/hatch/workspace/jah-databases"
SHARD = "/home/hatch/workspace/jah-databases-data-1"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate

spec = importlib.util.spec_from_file_location(
    "nb_build", os.path.join(REPO, "code", "numbering-build", "build.py"))
nb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(nb)

sweep_path = "/home/hatch/workspace/goals/database-quality-audit/hidden_files/patches/sweep-db-pages.py"
sspec = importlib.util.spec_from_file_location("sweep", sweep_path)
sweep = importlib.util.module_from_spec(sspec)
sspec.loader.exec_module(sweep)

sys.path.insert(0, HERE)
import compose
try:
    from items_versus import ITEMS as VERSUS_ITEMS
except ImportError:
    VERSUS_ITEMS = []
try:
    from items_learning import ITEMS as LEARNING_ITEMS
except ImportError:
    LEARNING_ITEMS = []

ALL_ITEMS = {it["slug"]: it for it in VERSUS_ITEMS + LEARNING_ITEMS}
_pm = "/tmp/prefix_map.json"
if not os.path.exists(_pm):  # /tmp gets wiped without warning; workspace copy is canonical
    _pm = os.path.join(HERE, "prefix_map.json")
PREFIXES = json.load(open(_pm))

GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

with open(os.path.join(REPO, "db", "public-synthetic-intelligence", "index.html"),
          encoding="utf-8") as f:
    TEMPLATE = f.read()

BANNED = ["facebook", "bat belt"]


def cfg_for(slug, item, sig):
    source = "signature" if sig else "public"
    if sig:
        name = item["name"].replace(" Database", " Signature Database")
    else:
        name = item["name"]
    tagline = item["tagline"]
    hero_p = "%s - %s Every record carries the full entry: description, how it works, " \
             "key points, requirements, standards, citations, and a working demonstration " \
             "program. Records are ordered by the teaching ladder: simple foundations first, " \
             "then compounded applications, then the most complex mastery material." % (
                 tagline,
                 ("Signature originals - clearly labeled Signature-made originals, never presented "
                  "as authentic public record.") if sig else
                 ("Public records - real, fact-checked material organized in the Signature system."))
    return {
        "name": name, "tagline": tagline, "record_kind": item["record_kind"],
        "prefix": PREFIXES[item["slug"]][1 if sig else 0],
        "ai": item["ai"] + (" (Signature)" if sig else ""),
        "role": item["role"] + (" Clearly labeled Signature-made; never presented as authentic "
                                "public record." if sig else ""),
        "hero_p": hero_p,
        "sig_type": ("Signature originals organized in the Signature system" if sig else
                     "Public records organized in the Signature system"),
        "search_ph": item["search_ph"], "chat_ph": item["chat_ph"],
        "archive_blurb": ("Seeded %s %s records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if sig else "public-record", item["record_kind"])),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": " \u00b7 ".join(item["groups"]) + " - each tier opens on demand and loads only what you open",
        "gen_desc": item["gen_desc"],
        "greet": item["greet"],
        "gen_fields": item["groups"],
        "gen_kind": item["gen_kind"], "gen_demo_kind": item["gen_demo_kind"],
        "source": source,
    }


def build_records(item, sig):
    prefix = PREFIXES[item["slug"]][1 if sig else 0]
    kind = item["kind"]
    recs = []
    assert len(item["topics"]) == 34, "item %s has %d topics" % (item["slug"], len(item["topics"]))
    for idx, topic in enumerate(item["topics"]):
        if kind in ("versus", "gen-versus", "gen-tree"):
            if kind == "gen-tree":
                r = compose_tree_record(item, topic, idx, sig, prefix)
            else:
                r = compose.compose_versus(item, topic, idx, sig, prefix)
        else:
            r = compose.compose_learning(item, topic, idx, sig, prefix)
        slug = item["slug"] + ("-signature" if sig else "")
        dupes = [h for h in GATE.check(slug, r["title"]) if h[0] != slug]
        if dupes:
            print("  gate refused (cross-db dupe): %s" % r["title"], flush=True)
            continue
        GATE.admit(slug, r["title"], r["id"])
        recs.append(r)
    return recs


def compose_tree_record(item, topic, idx, sig, prefix):
    """Skill-tree sample record: full record describing one generated tree."""
    rid = prefix + "%06d" % (idx + 1)
    title = topic["t"] + (" (Signature Edition)" if sig else "")
    nodes = topic["nodes"]  # [(name, tier, xp, prereq)]
    desc = (topic["n"] + "\nThis sample skill tree maps '" + topic["skill"] + "' as " +
            str(len(nodes)) + " unlockable nodes across " + str(max(n[1] for n in nodes)) +
            " tiers. Total XP to master: " + str(sum(n[2] for n in nodes)) + ".")
    if sig:
        desc = compose.SIG_LABEL + " " + desc
    how = ("The generator builds the tree in three passes. First it names the skill's core "
           "loop - the one action everything else serves. Then it fans out foundations: the "
           "prerequisites with no prerequisites. Then each tier unlocks only when its "
           "prerequisites are complete, with XP costs rising so the tree teaches "
           "simple-to-complex by construction. The sample tree here: " +
           "; ".join("%s (tier %d, %d XP, needs %s)" % (nm, tr, xp, pr or "nothing")
                     for nm, tr, xp, pr in nodes) + ".")
    kp = (["%d nodes, %d tiers, %d total XP." % (len(nodes), max(n[1] for n in nodes),
                                                sum(n[2] for n in nodes))] +
          list(topic["facts"])[:4])
    rec = {
        "id": rid, "t": title, "g": topic["g"], "name": topic["t"], "title": title,
        "description": desc, "how_it_works": how,
        "key_points": kp,
        "requirements": ["Pick one skill you actually want.", "Do the tier-1 nodes in order - no skipping.",
                         "Log XP honestly: a node counts when you can demo it.", "Revisit mastered nodes monthly."],
        "standards": ["Every node names something you can DO, not just know.",
                      "No node unlocks before its prerequisites.", "XP costs rise with tier.",
                      "The tree ends at a capstone: a real finished thing."],
        "citations": list(topic.get("cite", [])) + [item["cite_pool"]],
        "src": "signature" if sig else "public-harvest",
        "ladder_rank": 1 + (idx * 10) // 34,
        "ladder_tier": ("foundations" if idx < 12 else "compounded" if idx < 24 else "advanced"),
        "demo": {"kind": "python", "language": "python",
                 "program": demo_tree(topic, title, rid, topic["g"]),
                 "note": "Working demonstration program (real, runnable Python)."},
    }
    return rec


_TREE_TEMPLATE = r'''def main():
    skill = __SKILL__
    nodes = [
__NODES__
    ]
    print("SKILL TREE: %s" % skill)
    tiers = {}
    for name, tier, xp, prereq in nodes:
        tiers.setdefault(tier, []).append((name, xp, prereq))
    total = 0
    for t in sorted(tiers):
        print("  tier %d:" % t)
        for name, xp, prereq in tiers[t]:
            total += xp
            need = ("needs: " + prereq) if prereq else "no prerequisite"
            print("    [ ] %-34s %4d XP (%s)" % (name[:34], xp, need))
    print("total XP to master: %d" % total)
    assert total == __TOTAL__, (total, __TOTAL__)
    # prerequisite integrity: every prereq names an earlier-tier node
    names = {n[0]: n[1] for n in nodes}
    for name, tier, xp, prereq in nodes:
        if prereq:
            assert prereq in names, "missing prereq %r" % prereq
            assert names[prereq] < tier, "prereq %r not earlier tier" % prereq
    print("prerequisite chain: valid")
    print("OK: __TITLE__ tree generated clean")

if __name__ == "__main__":
    main()
'''


def demo_tree(topic, title, rid, group):
    nlines = "\n".join("        (%s, %d, %d, %s)," % (json.dumps(nm), tr, xp,
                       "None" if pr is None else json.dumps(pr))
                       for nm, tr, xp, pr in topic["nodes"])
    total = sum(n[2] for n in topic["nodes"])
    prog = _TREE_TEMPLATE.replace("__SKILL__", json.dumps(topic["skill"]))
    prog = prog.replace("__NODES__", nlines).replace("__TOTAL__", str(total))
    prog = prog.replace("__TITLE__", str(topic["t"]).replace('"', "'"))
    return compose._hdr(title, rid, group) + prog


def sanity(recs, slug, cfg):
    ids = [r["id"] for r in recs]
    assert len(ids) == 34, "want 34 records, got %d in %s" % (len(ids), slug)
    assert len(ids) == len(set(ids)), "dup ids in %s" % slug
    assert all(i.startswith(cfg["prefix"]) for i in ids), "prefix drift in %s" % slug
    for r in recs:
        for k in ("id", "t", "g", "name", "title", "description", "how_it_works",
                  "key_points", "requirements", "standards", "citations",
                  "src", "ladder_rank", "ladder_tier", "demo"):
            assert k in r, "missing %s in %s" % (k, r["id"])
        assert len(r["description"]) > 200, "stub description in %s" % r["id"]
        assert len(r["how_it_works"]) > 200, "stub how_it_works in %s" % r["id"]
        assert len(r["key_points"]) >= 3 and len(r["citations"]) >= 1
        assert 1 <= r["ladder_rank"] <= 10
        assert r["ladder_tier"] in ("foundations", "compounded", "advanced")
        compile(r["demo"]["program"], r["id"], "exec")
        blob = json.dumps(r).lower()
        for b in BANNED:
            assert b not in blob, "banned %r in %s" % (b, r["id"])
        if slug.endswith("-signature"):
            assert "(signature edition)" in r["title"].lower()
            assert r["src"] == "signature"
        else:
            assert r["src"] == "public-harvest"


def run_demos(recs):
    def one(r):
        p = subprocess.run([sys.executable, "-c", r["demo"]["program"]],
                           capture_output=True, text=True, timeout=120)
        if p.returncode != 0 or "OK:" not in p.stdout:
            return "demo failed %s: %s" % (r["id"], (p.stderr or p.stdout)[-500:])
        return None
    with ThreadPoolExecutor(max_workers=8) as ex:
        for err in ex.map(one, recs):
            if err:
                raise AssertionError(err)


CUSTOM_GENS = {}


def register_custom_gen(key, fn):
    CUSTOM_GENS[key] = fn


def build_page_and_gen(slug, item, recs, sig):
    cfg = cfg_for(slug, item, sig)
    nb.DBCFG = {slug: cfg}
    page = nb.build_page(slug, TEMPLATE)
    page = page.replace(
        "Generate structural synthetic intelligence studies. Seeded archive records are the authoritative entries.",
        cfg["gen_desc"])
    assert 'id="stCount"' in page and ("var SLUG='%s';" % slug) in page
    assert "minmax(120px,1fr)" in page and "pre.codeblock" in page
    assert "pill-ex" in page and "qmerge" in page, "Exhaustive pill / merger missing"
    assert "dataset.p" in page, "tab guard missing"
    assert "facebook" not in page.lower()
    assert "synthetic intelligence" not in page.lower(), "template leftover in %s" % slug
    for b in BANNED:
        assert b not in page.lower(), "banned in page %s" % slug
    ddir = os.path.join(REPO, "db", slug)
    os.makedirs(ddir, exist_ok=True)
    ppath = os.path.join(ddir, "index.html")
    with open(ppath, "w", encoding="utf-8") as f:
        f.write(page)
    changed, notes = sweep.process_page(ppath)
    if item.get("custom_gen"):
        gen_js = CUSTOM_GENS[item["custom_gen"]](slug, item, recs, cfg)
    else:
        topics = {}
        for r in recs:
            topics.setdefault(r["g"], []).append("%s - %s" % (r["t"], r["g"]))
        gen_js = nb.build_gen_js(slug, topics, cfg)
    for b in BANNED:
        assert b not in gen_js.lower()
    gpath = os.path.join(ddir, "gen-%s.js" % slug)
    with open(gpath, "w", encoding="utf-8") as f:
        f.write(gen_js)
    p = subprocess.run(["node", "--check", gpath], capture_output=True, text=True)
    assert p.returncode == 0, "node --check failed %s: %s" % (gpath, p.stderr[-500:])
    return notes


def manifest_fragment(slug, item, sig, n):
    cfg = cfg_for(slug, item, sig)
    return {
        "slug": slug, "name": cfg["name"], "tagline": cfg["tagline"],
        "record_kind": cfg["record_kind"], "id_prefix": cfg["prefix"],
        "ai_name": cfg["ai"], "local_index": base.SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
        "record_count": n, "status": "live", "full_records": n,
        "index": base.SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
        "chunk_pattern": "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz",
        "source": cfg["source"],
    }


def thin_build_script(item):
    bdir = os.path.join(REPO, "code", item["slug"] + "-build")
    os.makedirs(bdir, exist_ok=True)
    with open(os.path.join(bdir, "build.py"), "w", encoding="utf-8") as f:
        f.write('#!/usr/bin/env python3\n"""Thin builder for %s (public + Signature pair).\nDelegates to the wave-10 master builder. Staged only; the coordinator merges.\n"""\nimport os, sys\nsys.path.insert(0, "/home/hatch/workspace/jah-databases/code/wave10-build")\nimport master_build\nsys.exit(master_build.build_item("%s"))\n' % (item["slug"], item["slug"]))
    return bdir


def build_item(item_slug):
    item = ALL_ITEMS[item_slug]
    thin_build_script(item)
    staged = []
    for sig in (False, True):
        slug = item_slug + ("-signature" if sig else "")
        if os.path.exists(os.path.join(REPO, "db", slug, "index.html")) and \
           os.path.exists(os.path.join(SHARD, "data", slug, "index.jsonl.gz")):
            print("skip (already staged): %s" % slug, flush=True)
            continue
        cfg = cfg_for(slug, item, sig)
        recs = build_records(item, sig)
        sanity(recs, slug, cfg)
        run_demos(recs)
        n = base.write_shard_db(slug, recs)
        notes = build_page_and_gen(slug, item, recs, sig)
        frag = manifest_fragment(slug, item, sig, n)
        with open(os.path.join(REPO, "code", item_slug + "-build",
                               "manifest-entry-%s.json" % slug), "w", encoding="utf-8") as f:
            json.dump(frag, f, indent=1, ensure_ascii=False)
        print("staged: %-42s %d records [%s]" % (slug, n, ", ".join(notes)), flush=True)
        staged.append(slug)
    return 0


import gen_custom  # noqa: E402  (three real client-side generators)
# Explicit registration into THIS module's CUSTOM_GENS. (gen_custom also tries
# to self-register, but under `python3 master_build.py` it imports a second
# copy of this module as "master_build" while we run as __main__ - so the
# self-registration lands on the wrong instance. Registering here is correct
# whether we run as __main__ or are imported by a thin build script.)
for _k, _fn in (("human-vs-machine", gen_custom.gen_human_vs_machine),
               ("ultimate-showdown", gen_custom.gen_ultimate_showdown),
               ("skill-tree", gen_custom.gen_skill_tree)):
    CUSTOM_GENS[_k] = _fn
del _k, _fn


def main():
    targets = sys.argv[1:] or sorted(ALL_ITEMS)
    for t in targets:
        assert t in ALL_ITEMS, "unknown item %s" % t
    for t in targets:
        print("=== %s ===" % t, flush=True)
        build_item(t)
    print("wave10: all requested items staged")


if __name__ == "__main__":
    sys.exit(main() or 0)
