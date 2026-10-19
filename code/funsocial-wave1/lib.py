#!/usr/bin/env python3
"""Shared build core for the 1000 fun/social list, wave 1.

61 items (wow-facts x33, internet-humor x28) -> 122 databases (public +
Signature pair each), 34 ladder-ordered full records each = 4,148 records.

Mirrors the merged pair structure (db/language-pashto/): pages are rendered
with code/numbering-build's build_page from the public-synthetic-intelligence
template, swept with the quality-audit sweep script, generators via
build_gen_js (custom hand-authored JS for the 4 GENERATOR-class items), shard
data as data/<slug>/index.jsonl.gz (light) + chunks/chunk-0000.jsonl.gz
(full records), and coordinator-merge fragments in
~/workspace/hidden_files/missing-builds/fragments/<slug>.json.

NEVER touches: data/manifest.json, api.json, index.html, README.md,
docs/AI_ACCESS.md. NEVER git commits or pushes.

Content gates: nothing hate-adjacent/profane/inappropriate; jokes are clean
and good-natured, never punching down at protected groups; no religious
framing. Never the words "bat belt". No website references. No Facebook.
"""
import gzip
import importlib.util
import io
import json
import os
import re
import sys
import unicodedata
from contextlib import redirect_stdout

REPO = "/home/hatch/workspace/jah-databases"
SHARD = "/home/hatch/workspace/jah-databases-data-1"
SHARD_BASE = "https://justinahiggins614-cmyk.github.io/jah-databases-data-1"
TEMPLATE = os.path.join(REPO, "db", "public-synthetic-intelligence", "index.html")
FRAGDIR = "/home/hatch/workspace/hidden_files/missing-builds/fragments"
OWNER = "Justin Addam Higgins (JAH)"
WAVE = "funsocial-wave1"

sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "nb_build", os.path.join(REPO, "code", "numbering-build", "build.py"))
nb = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(nb)

_sspec = importlib.util.spec_from_file_location(
    "sweep", "/home/hatch/workspace/goals/database-quality-audit/hidden_files/patches/sweep-db-pages.py")
sweep = importlib.util.module_from_spec(_sspec)
_sspec.loader.exec_module(sweep)

GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

BANNED = ("facebook", "bat belt")


def check_banned(blob, where):
    low = blob.lower()
    for b in BANNED:
        assert b not in low, "banned content %r in %s" % (b, where)


# ---------------------------------------------------------------- prefixes
def load_existing_prefixes():
    m = json.load(open(os.path.join(REPO, "data", "manifest.json")))
    out = set()
    for e in m["databases"]:
        p = e.get("id_prefix")
        if p:
            out.add(p)
    return out


def initialism(name, n=3):
    words = re.findall(r"[A-Za-z]+", name)
    stop = {"the", "of", "a", "an", "and", "vs", "s", "to", "for", "in", "on",
            "from", "with", "by", "is", "it", "as", "at", "or", "de", "la"}
    letters = "".join(w[0].upper() for w in words
                      if w.lower() not in stop and len(w) > 1)
    return (letters[:n] or "X").ljust(min(n, 3), "X")[:n]


def alloc_prefix(family_letter, name, taken):
    """Allocate a collision-free prefix. Checks exact + substring both ways
    against every manifest id_prefix and every prefix taken in this run."""
    code = initialism(name, 3)
    i = 0
    while True:
        cand = "JAH-%s%s%s-" % (family_letter, code, "" if i == 0 else str(i))
        clash = False
        for p in taken:
            if cand == p or cand in p or p in cand:
                clash = True
                break
        if not clash:
            taken.add(cand)
            sig = cand[:-1] + "S-"
            for p in taken:
                if sig == p or sig in p or p in sig:
                    clash = True
                    break
            if not clash:
                taken.add(sig)
                return cand, sig
        i += 1
        assert i < 50, "prefix allocation failed for %s" % name


# ---------------------------------------------------------------- item registry
ITEMS = {}          # slug -> item cfg dict
ORDER = []          # build order (first-release picks first)


def register(item):
    assert item["slug"] not in ITEMS, "duplicate item %s" % item["slug"]
    assert len(item["seeds"]) == 17, \
        "item %s has %d seeds, need 17" % (item["slug"], len(item["seeds"]))
    assert item.get("citation"), "item %s missing citation" % item["slug"]
    assert item.get("pub_line"), "item %s missing pub_line" % item["slug"]
    keys = [s["key"] for s in item["seeds"]]
    assert len(set(keys)) == 17, "dup seed keys in %s" % item["slug"]
    for s in item["seeds"]:
        for f in ("t", "g", "fact", "mechanism", "evidence", "sig_angle",
                  "sig_do", "points"):
            assert s.get(f), "seed %s missing %s" % (s.get("key"), f)
        assert 3 <= len(s["points"]) <= 6, "seed %s points" % s["key"]
        s.setdefault("cite", [item["citation"]])
        s.setdefault("req", item.get("req_default") or
                     "Reading only - no equipment needed.")
        s.setdefault("demo", item.get("demo_default") or "report")
    ITEMS[item["slug"]] = item


def finalize_registry():
    # global seed-key uniqueness across all 61 items
    seen = {}
    for slug, item in ITEMS.items():
        for s in item["seeds"]:
            assert s["key"] not in seen, \
                "seed key %r reused in %s and %s" % (s["key"], seen.get(s["key"]), slug)
            seen[s["key"]] = slug
    # build order: first-release picks first
    picks = [s for s in ITEMS if ITEMS[s].get("first_pick")]
    rest = [s for s in ITEMS if not ITEMS[s].get("first_pick")]
    ORDER[:] = picks + rest
    return len(ITEMS), len(seen)
