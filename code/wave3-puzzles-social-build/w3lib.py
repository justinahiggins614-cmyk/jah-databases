#!/usr/bin/env python3
"""Wave 3 (puzzles-brain + social-relationships) shared build helpers.

Each topic module defines CFG + TOPICS (34 dicts). build_one(mod) runs the
whole-system dedupe gate, builds the public+signature pair via
_pairbuild12/lib.py, optionally overwrites the generator JS with a REAL
working generator for GENERATOR-class items, and stages a manifest fragment.

Property of Justin Addam Higgins (JAH).
"""
import gzip
import json
import os
import random
import re
import subprocess
import sys

REPO = os.path.expanduser("~/workspace/jah-databases")
DATAREPO = os.path.expanduser("~/workspace/jah-databases-data-1")
FRAGDIR = os.path.expanduser("~/workspace/hidden_files/missing-builds/fragments")
DATAHOST = "https://justinahiggins614-cmyk.github.io/jah-databases-data-1"

sys.path.insert(0, os.path.join(REPO, "code"))
sys.path.insert(0, os.path.join(REPO, "code", "_pairbuild12"))
from dedupe_gate import DedupeGate
import lib as pairlib

_GATE = None


def gate():
    global _GATE
    if _GATE is None:
        _GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))
    return _GATE


def _py(v):
    return repr(v)


# ---------------------------------------------------------------- demo factory
def make_demo(kind, data, title):
    """Return a Python source string that runs real logic and prints results."""
    head = "# %s\n# Property of Justin Addam Higgins (JAH).\n" % title.replace("\n", " ")
    tail = '\nprint("DEMO OK")\n'
    if kind == "check":
        lines = [head]
        if data.get("preamble"):
            lines.append(data["preamble"])
        for stmt in data.get("code", []):
            lines.append(stmt)
        for label, expr in data["checks"]:
            lines.append("_v = (%s)" % expr)
            lines.append("print(%s + ': ' + repr(_v))" % _py(label))
            lines.append("assert _v, %s" % _py("check failed: " + label))
        return "\n".join(lines) + tail
    if kind == "compute":
        lines = [head]
        if data.get("preamble"):
            lines.append(data["preamble"])
        for stmt in data["code"]:
            lines.append(stmt)
        for name in data.get("show", []):
            lines.append("print(%s + ' = ' + repr(%s))" % (_py(name), name))
        for label, expr in data.get("asserts", []):
            lines.append("assert (%s), %s" % (expr, _py("assert failed: " + label)))
        return "\n".join(lines) + tail
    if kind == "render":
        lines = [head,
                 "import random",
                 "_rng = random.Random(%d)" % int(data.get("seed", 7)),
                 "_tpl = %s" % _py(data["template"]),
                 "_slots = %s" % _py(data["slots"]),
                 "_outs = []",
                 "for _i in range(%d):" % int(data.get("n", 3)),
                 "    _s = _tpl",
                 "    _used = {}",
                 "    for _k, _opts in _slots.items():",
                 "        _pick = _rng.choice(_opts)",
                 "        _used[_k] = _pick",
                 "        _s = _s.replace('{' + _k + '}', _pick)",
                 "    assert '{' not in _s and '}' not in _s, 'unfilled slot in: ' + _s",
                 "    _outs.append(_s)",
                 "    print('VARIANT %d: %s' % (_i + 1, _s))",
                 "assert len(set(_outs)) == len(_outs), 'duplicate variants'",
                 "print('variants_ok=%d' % len(_outs))"]
        return "\n".join(lines) + tail
    if kind == "deck":
        lines = [head,
                 "import random",
                 "_rng = random.Random(%d)" % int(data.get("seed", 11)),
                 "_cards = %s" % _py(data["cards"]),
                 "_rng.shuffle(_cards)",
                 "_deal = _cards[:%d]" % int(data.get("deal", 5)),
                 "print('DEALT %d CARDS:' % len(_deal))",
                 "for _c in _deal: print(' - ' + _c)",
                 "assert len(_deal) == %d" % int(data.get("deal", 5)),
                 "assert len(set(_deal)) == len(_deal), 'duplicate cards dealt'"]
        return "\n".join(lines) + tail
    if kind == "score":
        lines = [head,
                 "_answers = %s" % _py(data["answers"]),
                 "_key = %s" % _py(data["key"]),
                 "_hits = sum(1 for _q in _key if _answers.get(_q) == _key[_q])",
                 "_pct = round(100.0 * _hits / len(_key), 1)",
                 "print('score: %d/%d = %s%%' % (_hits, len(_key), _pct))",
                 "assert _pct == %s, 'score mismatch'" % _py(data["expected"])]
        return "\n".join(lines) + tail
    if kind == "rules":
        lines = [head,
                 "_phrases = %s" % _py(data["phrases"]),
                 "_must = %s" % _py([w.lower() for w in data.get("must", [])]),
                 "_must_not = %s" % _py([w.lower() for w in data.get("must_not", [])]),
                 "_allok = True",
                 "for _p in _phrases:",
                 "    _low = _p.lower()",
                 "    _okm = all(_w in _low for _w in _must)",
                 "    _okn = not any(_w in _low for _w in _must_not)",
                 "    print(('PASS' if (_okm and _okn) else 'FAIL') + ': ' + _p)",
                 "    _allok = _allok and _okm and _okn",
                 "assert _allok, 'a phrase failed the checklist'"]
        return "\n".join(lines) + tail
    if kind == "custom":
        prog = data["program"]
        if "DEMO OK" not in prog:
            prog = prog.rstrip() + tail
        return prog
    raise ValueError("unknown demo kind %r" % kind)


# ---------------------------------------------------------------- topic helper
def topic(tier, title, desc_pub, desc_sig, how_pub, how_sig, keys, demo,
          reqs=None, stds=None, cites=None):
    return {
        "tier": tier, "title": title,
        "desc_pub": desc_pub, "desc_sig": desc_sig,
        "how_pub": how_pub, "how_sig": how_sig,
        "keys": list(keys), "demo": demo,
        "reqs": reqs, "stds": stds, "cites": cites,
    }


def _fill_topic(t, cfg):
    t = dict(t)
    if t.get("reqs") is None:
        t["reqs"] = cfg["reqs_default"]
    if t.get("stds") is None:
        t["stds"] = cfg["stds_default"]
    if t.get("cites") is None:
        t["cites"] = list(cfg["cites_default"])
    return t


CFG_KEYS = ["slug", "prefix_pub", "prefix_sig", "name_pub", "name_sig",
            "tagline_pub", "tagline_sig", "ai_pub", "ai_sig", "role_pub",
            "role_sig", "greet_pub", "greet_sig", "record_kind",
            "record_kind_plural", "demo_kind", "demo_title", "search_ph",
            "chat_ph", "gen_blurb", "about_archive", "reqs_default",
            "stds_default", "cites_default"]


def build_one(mod, custom_gen=None):
    """Build one public+signature pair from a topic module."""
    cfg = mod.CFG
    missing = [k for k in CFG_KEYS if k not in cfg]
    assert not missing, "CFG missing: %s" % missing
    topics = [_fill_topic(t, cfg) for t in mod.TOPICS]
    assert len(topics) == 34, "need 34 topics, got %d" % len(topics)
    tiers = [t["tier"] for t in topics]
    assert tiers.count("Foundations") == 11, tiers.count("Foundations")
    assert tiers.count("Compounded") == 12, tiers.count("Compounded")
    assert tiers.count("Advanced") == 11, tiers.count("Advanced")
    for t in topics:
        assert t["keys"] and t["demo"] and len(t["demo"]) == 2, t["title"]
        assert len(t["desc_pub"]) > 60, t["title"]

    # whole-system dedupe gate BEFORE writing anything
    g = gate()
    for t in topics:
        for title in (t["title"], t["title"] + " (Signature Edition)"):
            hits = g.check(cfg["slug"], title)
            if hits:
                raise ValueError("dedupe hit for %r: %s" % (title, hits[:3]))
    for t in topics:
        g.admit(cfg["slug"], t["title"], cfg["prefix_pub"])
        g.admit(cfg["slug"] + "-signature", t["title"] + " (Signature Edition)",
                cfg["prefix_sig"])

    lib_cfg = {
        "slug": cfg["slug"],
        "prefix_pub": cfg["prefix_pub"], "prefix_sig": cfg["prefix_sig"],
        "name_pub": cfg["name_pub"], "name_sig": cfg["name_sig"],
        "tagline_pub": cfg["tagline_pub"], "tagline_sig": cfg["tagline_sig"],
        "ai_pub": cfg["ai_pub"], "ai_sig": cfg["ai_sig"],
        "role_pub": cfg["role_pub"], "role_sig": cfg["role_sig"],
        "greet_pub": cfg["greet_pub"], "greet_sig": cfg["greet_sig"],
        "record_kind": cfg["record_kind"],
        "record_kind_plural": cfg["record_kind_plural"],
        "demo_kind": cfg["demo_kind"], "demo_title": cfg["demo_title"],
        "search_ph": cfg["search_ph"], "chat_ph": cfg["chat_ph"],
        "gen_blurb": cfg["gen_blurb"], "about_archive": cfg["about_archive"],
    }
    if cfg.get("gen_sample_extra"):
        lib_cfg["gen_sample_extra"] = cfg["gen_sample_extra"]

    def demo_builder(t, edition):
        kind, data = t["demo"]
        return make_demo(kind, data, t["title"])

    built = pairlib.build_pair(lib_cfg, topics, demo_builder)

    gen_kind = custom_gen or getattr(mod, "CUSTOM_GEN", None)
    if gen_kind:
        from realgen import write_real_generators
        write_real_generators(cfg, gen_kind)

    write_fragment(cfg)
    return built


def write_fragment(cfg):
    os.makedirs(FRAGDIR, exist_ok=True)
    frag = {}
    for ed, slug, name, tag, prefix, ai, src in (
        ("public", cfg["slug"], cfg["name_pub"], cfg["tagline_pub"],
         cfg["prefix_pub"], cfg["ai_pub"], "public-harvest"),
        ("signature", cfg["slug"] + "-signature", cfg["name_sig"],
         cfg["tagline_sig"], cfg["prefix_sig"], cfg["ai_sig"], "signature"),
    ):
        frag[ed] = {
            "slug": slug,
            "name": name,
            "tagline": tag,
            "record_kind": cfg["record_kind"],
            "id_prefix": prefix,
            "ai_name": ai,
            "local_index": "%s/data/%s/index.jsonl.gz" % (DATAHOST, slug),
            "record_count": 34,
            "status": "staged",
            "full_records": 34,
            "index": "%s/data/%s/index.jsonl.gz" % (DATAHOST, slug),
            "chunk_pattern": "data/%s/chunks/chunk-NNNN.jsonl.gz" % slug,
            "source": src,
        }
    path = os.path.join(FRAGDIR, cfg["slug"] + ".json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(frag, f, indent=2, ensure_ascii=False)
    print("fragment staged:", path)


def verify_all(slugs):
    """Final integrity + cross-pair dedupe across all built pairs."""
    all_built = {}
    for slug in slugs:
        for s in (slug, slug + "-signature"):
            p = os.path.join(DATAREPO, "data", s, "chunks", "chunk-0000.jsonl.gz")
            with gzip.open(p, "rt", encoding="utf-8") as f:
                recs = [json.loads(l) for l in f if l.strip()]
            assert len(recs) == 34, (s, len(recs))
            assert [r["ladder_rank"] for r in recs] == list(range(1, 35)), s
            all_built[s] = recs
            ip = os.path.join(DATAREPO, "data", s, "index.jsonl.gz")
            with gzip.open(ip, "rt", encoding="utf-8") as f:
                idx = [json.loads(l) for l in f if l.strip()]
            assert len(idx) == 34 and all(list(r.keys()) == ["id", "t", "g"] for r in idx), s
            for ed_slug in (s,):
                gp = os.path.join(REPO, "db", ed_slug, "gen-%s.js" % ed_slug)
                assert os.path.exists(gp), gp
                hp = os.path.join(REPO, "db", ed_slug, "index.html")
                assert os.path.exists(hp), hp
    pairlib.cross_pair_dedupe(all_built)
    n = sum(len(v) for v in all_built.values())
    print("verify_all OK: %d databases, %d records" % (len(all_built), n))
    return all_built


def mkcfg(d):
    """Compact CFG builder. d needs: slug, name, pfx (pub prefix), tagline_pub,
    tagline_sig, ai (short, e.g. 'Anagram Arena'), role_pub, role_sig,
    record_kind, record_kind_plural, demo_kind, demo_title, search_ph,
    chat_ph, gen_blurb, about_archive, reqs, stds, cites (list).
    greet_* optional."""
    sig_pfx = d["pfx"][:-1] + "S-"
    name, ai = d["name"], d["ai"]
    return {
        "slug": d["slug"],
        "prefix_pub": d["pfx"],
        "prefix_sig": sig_pfx,
        "name_pub": name + " Database",
        "name_sig": name + " Signature Database",
        "tagline_pub": d["tagline_pub"],
        "tagline_sig": d["tagline_sig"],
        "ai_pub": "JAH %s Archivist" % ai,
        "ai_sig": "JAH %s Signature Archivist" % ai,
        "role_pub": d["role_pub"],
        "role_sig": d["role_sig"],
        "greet_pub": d.get("greet_pub", "I am the JAH %s Archivist. Ask me anything about %s." % (ai, d["record_kind_plural"])),
        "greet_sig": d.get("greet_sig", "I am the JAH %s Signature Archivist. Ask me about the Signature edition." % ai),
        "record_kind": d["record_kind"],
        "record_kind_plural": d["record_kind_plural"],
        "demo_kind": d["demo_kind"],
        "demo_title": d["demo_title"],
        "search_ph": d["search_ph"],
        "chat_ph": d["chat_ph"],
        "gen_blurb": d["gen_blurb"],
        "about_archive": d["about_archive"],
        "reqs_default": d["reqs"],
        "stds_default": d["stds"],
        "cites_default": list(d["cites"]),
    }


T = topic
