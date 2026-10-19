#!/usr/bin/env python3
"""Build all 42 fantasy-worlds slugs x public+signature editions (84 databases).

Writes (builder scope ONLY - a merger handles manifest/api):
  main repo : db/<slug>/index.html + gen-<slug>.js
              db/<slug>-signature/index.html + gen-<slug>-signature.js
  shard repo: data/<slug>/index.jsonl.gz + chunks/chunk-0000.jsonl.gz (x2 editions)
  build dirs: code/fantasy-worlds-build/ (shared engine)
              code/<slug>-build/build.py (per-slug rebuild shim)
  fragments : ~/workspace/hidden_files/missing-builds/fragments/<slug>.json

NEVER touches: data/manifest.json, api.json, index.html, README.md,
docs/AI_ACCESS.md. NEVER git commits or pushes.

Gates: dedupe (whole-system exact-title gate) before writing each record;
every demo program machine-executed and passing; node --check + smoke
test on every gen script; ID prefixes pre-verified collision-free.
"""
import gzip
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = "/home/hatch/workspace/jah-databases"
SHARD = "/home/hatch/workspace/jah-databases-data-1"
SHARD_BASE = "https://justinahiggins614-cmyk.github.io/jah-databases-data-1"
FRAGDIR = "/home/hatch/workspace/hidden_files/missing-builds/fragments"

sys.path.insert(0, HERE)
import lore
import engine
import page_gen

sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate

GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

FIRST_RELEASE = ["gen-world-builder", "gen-kingdom-generator", "gen-dragon-creator",
                 "gen-superpower-laboratory", "gen-spell-creator", "gen-quest-generator",
                 "gen-fantasy-map-generator", "gen-space-fleet-creator",
                 "gen-starship-interior-designer", "gen-infinite-tunnel"]


def ordered_slugs():
    by_slug = {s["slug"]: s for s in lore.SLUGS}
    rest = [s for s in lore.SLUGS if s["slug"] not in FIRST_RELEASE]
    return [by_slug[s] for s in FIRST_RELEASE] + rest


def ai_name_for(cfg, edition):
    base = "JAH " + cfg["ai_short"] + (" Engine" if cfg["class"] == "GENERATOR" else " Archivist")
    return base + (" (Signature)" if edition == "signature" else "")


def edition_name(cfg, edition):
    if edition == "public":
        return cfg["item_name"]
    n = cfg["item_name"]
    if n.endswith(" Database"):
        return n[:-len(" Database")] + " Signature Database"
    return n + " Signature Database"


def run_demo(program):
    p = subprocess.run([sys.executable, "-c", program], capture_output=True,
                       text=True, timeout=30)
    return p.returncode == 0 and "OK" in p.stdout, (p.stdout + p.stderr)[-400:]


def node_check(path):
    p = subprocess.run(["node", "--check", path], capture_output=True, text=True, timeout=30)
    return p.returncode == 0, p.stderr[-400:]


def node_smoke(path):
    js = ("var g=require(%s);var r=g.generate(7,{});var v=g.validate(r);"
          "var d=g.driftCheck(r,[]);"
          "if(!v.ok)throw new Error('validate: '+v.errors.join(','));"
          "if(!d.ok)throw new Error('drift');"
          "if(!r.demo||!r.demo.program||r.demo.program.indexOf('assert')<0)throw new Error('demo');"
          "console.log('smoke-ok '+r.id);" % json.dumps(path))
    p = subprocess.run(["node", "-e", js], capture_output=True, text=True, timeout=30)
    return p.returncode == 0 and "smoke-ok" in p.stdout, (p.stdout + p.stderr)[-400:]


def write_gz(path, lines):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with gzip.open(path, "wt", encoding="utf-8") as f:
        for ln in lines:
            f.write(ln + "\n")


def build_edition(cfg, edition):
    slug = cfg["slug"] + ("-signature" if edition == "signature" else "")
    prefix = cfg["prefix_sig"] if edition == "signature" else cfg["prefix"]
    src = "signature" if edition == "signature" else "public-harvest"
    name = edition_name(cfg, edition)
    ai = ai_name_for(cfg, edition)
    gen_id = "jahdb-" + slug + "-1.0"
    gen_file = "gen-" + slug + ".js"

    # ---- records (dedupe gate first, demos executed)
    records = []
    for spec in cfg["specs"]:
        rec = engine.build_record(cfg, spec, edition, prefix, src)
        hits = GATE.check(slug, rec["title"])
        if hits:
            raise RuntimeError("DEDUPE HIT %s title=%r hits=%r" % (slug, rec["title"], hits[:3]))
        ok, tail = run_demo(rec["demo"]["program"])
        if not ok:
            raise RuntimeError("DEMO FAILED %s %s\n%s" % (slug, rec["id"], tail))
        records.append(rec)
        GATE.admit(slug, rec["title"], rec["id"])

    # ---- shard data
    ddir = os.path.join(SHARD, "data", slug)
    write_gz(os.path.join(ddir, "index.jsonl.gz"),
             [json.dumps(engine.index_row(r), ensure_ascii=False) for r in records])
    write_gz(os.path.join(ddir, "chunks", "chunk-0000.jsonl.gz"),
             [json.dumps(r, ensure_ascii=False) for r in records])

    # ---- page
    f1, f2, f3 = cfg["fields"]
    if edition == "public":
        type_str = "Public records organized in the Signature system"
        descriptor = ("Public records - 34 fully-formed original %s, ladder-ordered %s (1-11) -> %s (12-22) -> %s (23-34). "
                      "Every record carries the full entry: description, how it works, key points, requirements, standards, "
                      "citations, and a working demonstration program." % (cfg["plural"], f1, f2, f3))
    else:
        type_str = "Signature originals organized in the Signature system"
        descriptor = ("Signature originals - his original Signature treatment of %s, ladder-ordered %s (1-11) -> %s (12-22) -> %s (23-34). "
                      "Every record carries the full entry: description, how it works, key points, requirements, standards, "
                      "citations, and a working demonstration program. Clearly labeled Signature-made, never presented as "
                      "authentic public record." % (cfg["plural"], f1, f2, f3))
    greet = ("I am the %s. Ask me about %s - from %s through %s to %s." %
             (ai, cfg["plural"], f1.lower(), f2.lower(), f3.lower()))
    html = page_gen.page_html(
        slug, name, cfg["tagline"], descriptor, cfg["record_kind"], prefix, ai,
        cfg["role"], gen_id, gen_file,
        "Search %s, %s, lore..." % (cfg["plural"], cfg["noun"]),
        "Ask about %s..." % cfg["plural"], greet, type_str,
        "Seeded %s %s, marching toward one million records. Presented in teaching-ladder order: %s, %s, %s." %
        ("Signature-original" if edition == "signature" else "public-record",
         cfg["record_kind"] + "s", f1.lower(), f2.lower(), f3.lower()),
        "%s · %s · %s - each tier opens on demand and loads only what you open" % (f1, f2, f3),
        "%s — Generate clearly-labeled %s samples. Seeded archive records are the authoritative entries." % (gen_id, cfg["record_kind"]),
        "%s — %s — and aware of the whole JAH Databases network through cross-database reasoning. "
        "On-device Standard 1.0, no key needed; uses the shared Signature backend automatically when configured." % (ai, cfg["role"]),
    )
    pdir = os.path.join(REPO, "db", slug)
    os.makedirs(pdir, exist_ok=True)
    with open(os.path.join(pdir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)

    # ---- generator js
    js = page_gen.gen_js(cfg, slug, prefix, gen_id, gen_id)
    jsp = os.path.join(pdir, gen_file)
    with open(jsp, "w", encoding="utf-8") as f:
        f.write(js)
    ok, tail = node_check(jsp)
    if not ok:
        raise RuntimeError("node --check FAILED %s\n%s" % (jsp, tail))
    ok, tail = node_smoke(jsp)
    if not ok:
        raise RuntimeError("node smoke FAILED %s\n%s" % (jsp, tail))

    return {"slug": slug, "name": name, "tagline": cfg["tagline"],
            "record_kind": cfg["record_kind"], "id_prefix": prefix,
            "ai_name": ai,
            "local_index": "%s/data/%s/index.jsonl.gz" % (SHARD_BASE, slug),
            "index": "%s/data/%s/index.jsonl.gz" % (SHARD_BASE, slug),
            "chunk_pattern": "data/%s/chunks/chunk-NNNN.jsonl.gz" % slug,
            "record_count": 34, "full_records": 34, "status": "staged",
            "source": src}


def write_fragment(cfg, pub_meta, sig_meta):
    os.makedirs(FRAGDIR, exist_ok=True)
    with open(os.path.join(FRAGDIR, cfg["slug"] + ".json"), "w", encoding="utf-8") as f:
        json.dump({"public": pub_meta, "signature": sig_meta}, f, indent=1,
                  ensure_ascii=False)


def write_shim(cfg):
    d = os.path.join(REPO, "code", cfg["slug"] + "-build")
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "build.py"), "w", encoding="utf-8") as f:
        f.write("#!/usr/bin/env python3\n"
                '"""Rebuild %s (public + signature) via the shared fantasy-worlds builder."""\n'
                "import os, sys\n"
                "sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),\n"
                "                                '..', 'fantasy-worlds-build'))\n"
                "import build_all\n"
                "if __name__ == '__main__':\n"
                "    build_all.build_slug('%s')\n" % (cfg["slug"], cfg["slug"]))


def build_slug(slug_name):
    cfg = next(s for s in lore.SLUGS if s["slug"] == slug_name)
    pub = build_edition(cfg, "public")
    sig = build_edition(cfg, "signature")
    write_fragment(cfg, pub, sig)
    write_shim(cfg)
    return slug_name


def main():
    os.makedirs(FRAGDIR, exist_ok=True)
    done, failed = [], []
    for cfg in ordered_slugs():
        try:
            build_slug(cfg["slug"])
            done.append(cfg["slug"])
            print("OK  %-32s (68 records, 2 pages, 2 generators)" % cfg["slug"], flush=True)
        except Exception as e:
            failed.append((cfg["slug"], str(e)[:300]))
            print("FAIL %-32s %s" % (cfg["slug"], str(e)[:200]), flush=True)
    print("\nbuilt=%d failed=%d" % (len(done), len(failed)))
    for s, e in failed:
        print("FAILED:", s, e)
    with open(os.path.join(HERE, "build-report.json"), "w") as f:
        json.dump({"built": done, "failed": failed}, f, indent=1)


if __name__ == "__main__":
    main()
