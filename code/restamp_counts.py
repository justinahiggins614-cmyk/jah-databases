#!/usr/bin/env python3
"""code/restamp_counts.py — keep every JAH Databases counter always current.

Standing order (2026-10-14, his words): "Make always updating the counts."
Source of truth: data/manifest.json `databases` list. The count is DERIVED,
never hand-typed, so it cannot drift.

What it stamps, all from n = len(manifest["databases"]):
  1. data/manifest.json["database_count"] = n
  2. api.json["database_count"]          = n
  3. index.html static fallbacks (the no-JS snapshot crawlers and his phone
     see before the live JS overwrites them):
       - every <span class="live-db-count">NNN</span>
       - every <b class="live-db-count">NNN</b>
       - meta[name=description] "JAH Databases: NNN connected databases,
         NNN boundless generators, NNN archive-aware AIs."

  4. AUDIT: every db/*/index.html must wire the live archive count via
     id="stCount" filled from archiveIdx.length (JS reads the record index
     at page load, so per-page record counts are always current by
     construction). Any page missing that wiring is reported and the
     script exits 1.

  7. README.md + docs/AI_ACCESS.md count stamping: the same three counters
     (connected databases, boundless generators, archive-aware AIs) and the
     "N-database registry" / "the other N-1 databases" phrases are re-derived
     from n on every run, with fail-loud assertions — these doc files went
     stale at "37" for weeks while the manifest marched past 2300.

Per-database record counts need no stamping: they come from the actual
archive index at page load ($('stCount').textContent = archiveIdx.length...).

HOOK (never one-run-behind): run this script at the END of any commit that
adds databases or grows the manifest, and the 6h cron `jah-databases-count-restamp`
catches anything missed. `python3 code/restamp_counts.py` then commit the
changed files.

Usage: python3 code/restamp_counts.py
Exit 0: counts stamped (or already current); prints what changed.
Exit 1: audit failure (a db page missing live-count wiring) or an unreadable
        source — never stamps partial numbers.
"""
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f), open(path, "r", encoding="utf-8").read()


def dump_canonical(data, raw):
    """Re-dump in the file's own format (indent=1, trailing newline)."""
    out = json.dumps(data, indent=1, ensure_ascii=False)
    out += "\n" if raw.endswith("\n") else ""
    if raw.endswith("\n") and not out.endswith("\n"):
        out += "\n"
    return out


def main():
    man, man_raw = load_json(os.path.join(ROOT, "data", "manifest.json"))
    api, api_raw = load_json(os.path.join(ROOT, "api.json"))

    dbs = man.get("databases") or []
    n = len(dbs)
    if n == 0:
        print("FATAL: manifest databases list is empty — refusing to stamp", file=sys.stderr)
        return 1

    changed = []

    # 1+2: enforce database_count = n in both files
    for path, data, raw, label in (
        ("data/manifest.json", man, man_raw, "manifest"),
        ("api.json", api, api_raw, "api.json"),
    ):
        cur = data.get("database_count")
        api_dbs = data.get("databases") if label == "api.json" else None
        if label == "api.json" and api_dbs is not None and len(api_dbs) != n:
            print(
                "FATAL: api.json lists %d databases but manifest lists %d — "
                "resolve the manifest drift by hand, not by stamping" % (len(api_dbs), n),
                file=sys.stderr,
            )
            return 1
        if cur != n:
            data["database_count"] = n
            new_raw = dump_canonical(data, raw)
            with open(os.path.join(ROOT, path), "w", encoding="utf-8") as f:
                f.write(new_raw)
            changed.append("%s database_count: %s -> %d" % (label, cur, n))
        else:
            changed.append("%s database_count already %d" % (label, n))

    # 3: re-stamp index.html static fallbacks
    idx_path = os.path.join(ROOT, "index.html")
    html = open(idx_path, "r", encoding="utf-8").read()
    orig = html

    span_subs = len(re.findall(r'class="live-db-count">\d+<', html))
    html = re.sub(r'(class="live-db-count">)\d+(<)', r"\g<1>%d\g<2>" % n, html)

    html, meta_subs = re.subn(
        r"JAH Databases: (\d+) connected databases, (\d+) boundless generators, (\d+) archive-aware AIs",
        lambda m: "JAH Databases: %d connected databases, %d boundless generators, %d archive-aware AIs"
        % (n, n, n),
        html,
    )

    if html != orig:
        with open(idx_path, "w", encoding="utf-8") as f:
            f.write(html)
        changed.append(
            "index.html restamped: %d live-db-count spans + %d meta description -> %d"
            % (span_subs, meta_subs, n)
        )
    else:
        changed.append("index.html static fallbacks already at %d" % n)

    # 4: audit — every db page must have the live-count wiring
    pages = sorted(glob.glob(os.path.join(ROOT, "db", "*", "index.html")))
    missing = [p for p in pages if 'id="stCount"' not in open(p, encoding="utf-8").read()]
    changed.append("db pages with live-count wiring: %d/%d" % (len(pages) - len(missing), len(pages)))
    if missing:
        print(
            "FATAL: %d db pages lack the id=\"stCount\" live-count wiring:" % len(missing),
            file=sys.stderr,
        )
        for p in missing[:20]:
            print("  " + os.path.relpath(p, ROOT), file=sys.stderr)
        return 1

    # 5: quality audit — dedupe+xdb tags on Track A pages; no contamination in generators
    track_a = [p for p in pages
               if '<script src="../../core/jahdb.js">' in open(p, encoding="utf-8").read()]
    no_dedupe = [p for p in track_a
                 if 'jahdb-dedupe.js' not in open(p, encoding="utf-8").read()]
    no_xdb = [p for p in track_a
              if 'jahdb-xdb.js' not in open(p, encoding="utf-8").read()]
    changed.append("Track A pages with dedupe tags: %d/%d" % (len(track_a) - len(no_dedupe), len(track_a)))
    changed.append("Track A pages with xdb tags: %d/%d" % (len(track_a) - len(no_xdb), len(track_a)))
    if no_dedupe:
        print("WARN: %d Track A pages lack dedupe tags" % len(no_dedupe), file=sys.stderr)
    # contamination regression: no gen-*.js may contain the filler strings
    bad_gens = []
    for g in glob.glob(os.path.join(ROOT, "db", "*", "gen-*.js")):
        try:
            src = open(g, encoding="utf-8").read()
        except Exception:
            continue
        if ("guide provides comprehensive coverage" in src
                and "content_completeness" not in src):
            bad_gens.append(g)
        if "Determine and formulate policies" in src and "contaminated overview" not in src:
            bad_gens.append(g)
    changed.append("generators with contamination/filler: %d" % len(bad_gens))
    if bad_gens:
        print("FATAL: %d generators contain unpatched contamination/filler:" % len(bad_gens),
              file=sys.stderr)
        for p in bad_gens[:20]:
            print("  " + os.path.relpath(p, ROOT), file=sys.stderr)
        return 1

    # 6: xdb contract — generators declaring xdbUses must be well-formed
    import re as _re
    xdb_bad = []
    for g in glob.glob(os.path.join(ROOT, "db", "*", "gen-*.js")):
        try:
            src = open(g, encoding="utf-8").read()
        except Exception:
            continue
        if "xdbUses" in src:
            # must be a non-empty array of {slug, fields} declarations
            if not _re.search(r"xdbUses:\s*\[\s*\{[^]]*slug\s*:", src):
                xdb_bad.append(g)
    changed.append("generators with malformed xdbUses: %d" % len(xdb_bad))
    if xdb_bad:
        print("FATAL: %d generators have malformed xdbUses:" % len(xdb_bad), file=sys.stderr)
        for p in xdb_bad[:20]:
            print("  " + os.path.relpath(p, ROOT), file=sys.stderr)
        return 1

    # 7: README.md + docs/AI_ACCESS.md — derived counts, fail-loud (2026-10-17:
    # his order "update the files and databases as go along"; these files sat
    # stale at "37" while the manifest marched past 2300)
    rm_path = os.path.join(ROOT, "README.md")
    rm = open(rm_path, "r", encoding="utf-8").read()
    rm_orig = rm

    rm, hero_subs = re.subn(
        r"^\d+ connected databases, \d+ boundless generators, \d+ archive-aware AIs\.$",
        "%d connected databases, %d boundless generators, %d archive-aware AIs." % (n, n, n),
        rm, flags=re.M)
    if hero_subs != 1:
        print("FATAL: README.md hero count line not found exactly once (subs=%d) — "
              "hand-fix the hero line, never hand-type a count" % hero_subs, file=sys.stderr)
        return 1
    rm = re.sub(r"sample the other \d+\n  databases",
                "sample the other %d\n  databases" % (n - 1), rm)
    rm = re.sub(r"hub front door, \d+ database cards\.",
                "hub front door, %d database cards." % n, rm)
    rm = re.sub(r"the \d+-database registry",
                "the %d-database registry" % n, rm)

    if rm != rm_orig:
        with open(rm_path, "w", encoding="utf-8") as f:
            f.write(rm)
        changed.append("README.md restamped -> %d" % n)
    else:
        changed.append("README.md counts already at %d" % n)

    aa_path = os.path.join(ROOT, "docs", "AI_ACCESS.md")
    aa = open(aa_path, "r", encoding="utf-8").read()
    aa_orig = aa
    aa, llms_subs = re.subn(
        r"It lists all \d+ databases with page URLs and index file URLs\.",
        "It lists all %d databases with page URLs and index file URLs." % n, aa)
    if llms_subs != 1:
        print("FATAL: docs/AI_ACCESS.md llms.txt count line not found exactly once "
              "(subs=%d)" % llms_subs, file=sys.stderr)
        return 1
    aa = re.sub(r"machine-readable catalog of all \d+ databases",
                "machine-readable catalog of all %d databases" % n, aa)

    if aa != aa_orig:
        with open(aa_path, "w", encoding="utf-8") as f:
            f.write(aa)
        changed.append("docs/AI_ACCESS.md restamped -> %d" % n)
    else:
        changed.append("docs/AI_ACCESS.md counts already at %d" % n)

    print("RESTAMP OK — n=%d databases" % n)
    for c in changed:
        print("  - " + c)
    return 0


if __name__ == "__main__":
    sys.exit(main())
