#!/usr/bin/env python3
"""Build the Master Generator Registry from real repo data.

Phase A4 of the 2026-11-18 fix+build program. The review paste that ordered
this registry was another AI's draft (source unconfirmed); every number here
is counted fresh from the repo itself, never copied from that draft.

Sources (exact match only, never substring):
  1. data/manifest.json -- one database entry per slug (63,047 entries).
  2. db/*/gen-*.js -- one generator script per database, counted by script.
     The comics database carries TWO generator scripts (gen-comics.js and
     gen-comics-full.js, the full 22-page issue renderer), so the script
     count is one higher than the database count.
  3. data/generators/engine.js + data/generators/index.json.gz -- the
     Boundless Generator Archive engine and its indexed outputs, listed
     separately as a featured entry (not a per-database row).
  4. data/universal-generator/ -- the Universal Generator database; it is
     one of the 63,047 manifest entries and appears as a normal row, and is
     also featured on the page.

Outputs:
  generator-registry.json          -- small index: totals, counts by status
                                      and edition, per-letter counts, shard
                                      list, featured entries.
  generator-registry/<letter>.json -- one shard per first letter of slug
                                      ("0-9" for digit-leading slugs),
                                      one row per generator script.
  generator-registry.html          -- restamped counts (data-stamp spans).
  accessible/generator-registry.html -- restamped counts + letter table.

Row fields: slug, name, id_prefix, record_kind, edition, status,
record_count, generator_script, db_page, note (only where needed).
Edition is derived from the slug-suffix convention: a slug ending in
"-signature" is the Signature edition, anything else is the Public edition.

Usage: python3 code/build_generator_registry.py   (run from the repo root)
No network, no keys, no commits. Safe to re-run: outputs are regenerated.
"""

import gzip
import json
import re
import sys
from collections import Counter, OrderedDict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "data" / "manifest.json"
DB_DIR = ROOT / "db"
OUT_DIR = ROOT / "generator-registry"
INDEX_JSON = ROOT / "generator-registry.json"
HTML = ROOT / "generator-registry.html"
ACCESSIBLE_HTML = ROOT / "accessible" / "generator-registry.html"
ARCHIVE_ENGINE = ROOT / "data" / "generators" / "engine.js"
ARCHIVE_INDEX = ROOT / "data" / "generators" / "index.json.gz"
BASE_URL = "https://justinahiggins614-cmyk.github.io/jah-databases"

# Slugs spot-checked by exact match after every build.
SPOT_CHECK_SLUGS = [
    "equations",
    "patents",
    "universal-generator",
    "comics",
    "soundscape-ecology-signature",
]


def letter_of(slug):
    c = slug[0]
    if c.isdigit():
        return "0-9"
    if c.isalpha():
        return c.lower()
    return "#"


def count_gz_lines(path):
    n = 0
    with gzip.open(path, "rt", encoding="utf-8", errors="replace") as f:
        for _ in f:
            n += 1
    return n


def main():
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    dbs = manifest["databases"]
    by_slug = {}
    for d in dbs:
        slug = d["slug"]
        if slug in by_slug:
            raise SystemExit(f"DUPLICATE slug in manifest: {slug}")
        by_slug[slug] = d

    # Count generator scripts by script: db/<slug>/gen-*.js, exact dir match.
    scripts = sorted(DB_DIR.glob("*/gen-*.js"))
    rows = []
    missing_manifest = []
    missing_file = []
    for script in scripts:
        slug = script.parent.name
        entry = by_slug.get(slug)
        if entry is None:
            missing_manifest.append(str(script))
            continue
        note = ""
        if script.name == "gen-comics-full.js":
            note = ("Second generator script for the comics database: "
                    "full 22-page issue renderer (JAHComicsFull).")
        rows.append({
            "slug": slug,
            "name": entry.get("name") or slug,
            "id_prefix": entry.get("id_prefix"),
            "record_kind": entry.get("record_kind"),
            "edition": "Signature" if slug.endswith("-signature") else "Public",
            "status": entry.get("status"),
            "record_count": entry.get("record_count"),
            "generator_script": f"db/{slug}/{script.name}",
            "db_page": f"db/{slug}/",
            "note": note,
        })
    if missing_manifest:
        raise SystemExit(f"gen scripts with NO manifest entry: {missing_manifest[:10]}")

    # Every manifest slug must have at least one generator script.
    slugs_with_script = {r["slug"] for r in rows}
    no_script = sorted(set(by_slug) - slugs_with_script)
    if no_script:
        raise SystemExit(f"manifest slugs with NO gen script: {no_script[:10]}")

    # Verification: every row's script file exists on disk (exact path).
    for r in rows:
        if not (ROOT / r["generator_script"]).is_file():
            missing_file.append(r["generator_script"])
    if missing_file:
        raise SystemExit(f"row script files missing on disk: {missing_file[:10]}")

    # Spot-checks by exact slug match against the manifest.
    for slug in SPOT_CHECK_SLUGS:
        got = [r for r in rows if r["slug"] == slug]
        want = by_slug.get(slug)
        assert want is not None, f"spot-check slug missing from manifest: {slug}"
        assert got, f"spot-check slug missing from rows: {slug}"
        assert got[0]["name"] == want.get("name"), f"name mismatch: {slug}"
        assert got[0]["id_prefix"] == want.get("id_prefix"), f"id_prefix mismatch: {slug}"
        assert got[0]["record_kind"] == want.get("record_kind"), f"record_kind mismatch: {slug}"
    comics_rows = [r for r in rows if r["slug"] == "comics"]
    assert len(comics_rows) == 2, f"expected 2 comics rows, got {len(comics_rows)}"
    assert sorted(r["generator_script"] for r in comics_rows) == [
        "db/comics/gen-comics-full.js", "db/comics/gen-comics.js"]

    rows.sort(key=lambda r: (r["slug"], r["generator_script"]))

    shards = OrderedDict()
    for r in rows:
        shards.setdefault(letter_of(r["slug"]), []).append(r)
    shard_letters = sorted(shards, key=lambda L: (L == "0-9", L == "#", L))

    OUT_DIR.mkdir(exist_ok=True)
    for letter in shard_letters:
        shard_rows = shards[letter]
        (OUT_DIR / f"{letter}.json").write_text(
            json.dumps({"letter": letter, "count": len(shard_rows),
                        "rows": shard_rows}, ensure_ascii=False), encoding="utf-8")

    archive_outputs = count_gz_lines(ARCHIVE_INDEX) if ARCHIVE_INDEX.is_file() else None
    uni = by_slug.get("universal-generator", {})
    today = date.today().isoformat()
    index = {
        "title": "Master Generator Registry — index",
        "generated": today,
        "source": ("data/manifest.json + db/*/gen-*.js, counted fresh by "
                   "code/build_generator_registry.py"),
        "attribution": ("Ordered by the 2026-11-18 fix+build program review "
                        "paste (another AI's draft, source unconfirmed); "
                        "all counts below are counted from the repo, not "
                        "copied from that draft."),
        "total_generator_scripts": len(rows),
        "total_databases": len(by_slug),
        "total_records": sum((d.get("record_count") or 0) for d in dbs),
        "by_status": dict(Counter(r["status"] or "unstated" for r in rows)),
        "by_edition": dict(Counter(r["edition"] for r in rows)),
        "by_letter": {L: len(shards[L]) for L in shard_letters},
        "shards": [f"generator-registry/{L}.json" for L in shard_letters],
        "featured": {
            "universal_generator": {
                "slug": "universal-generator",
                "name": uni.get("name"),
                "id_prefix": uni.get("id_prefix"),
                "record_kind": uni.get("record_kind"),
                "record_count": uni.get("record_count"),
                "generator_script": "db/universal-generator/gen-universal-generator.js",
                "db_page": "db/universal-generator/",
            },
            "boundless_generator_archive": {
                "name": "The Signature Boundless Generator Archive",
                "engine": "data/generators/engine.js",
                "index": "data/generators/index.json.gz",
                "indexed_outputs": archive_outputs,
                "note": ("Archive-level deterministic engine, not a "
                         "per-database generator. Its outputs are "
                         "simulated/Signature-generated, never presented "
                         "as authentic public record."),
            },
        },
    }
    INDEX_JSON.write_text(json.dumps(index, indent=1, ensure_ascii=False),
                          encoding="utf-8")

    stamp_html(HTML, index, today)
    stamp_accessible(ACCESSIBLE_HTML, index, today)

    print(f"databases: {len(by_slug)}")
    print(f"generator scripts (rows): {len(rows)}")
    print(f"shards: {len(shard_letters)} -> {OUT_DIR}/")
    print(f"archive indexed outputs: {archive_outputs}")
    print(f"by_status: {index['by_status']}")
    print(f"by_edition: {index['by_edition']}")
    print("spot-checks passed (exact slug match): " + ", ".join(SPOT_CHECK_SLUGS))
    print("comics has 2 rows: gen-comics.js + gen-comics-full.js")


def _replace_stamp_span(text, key, value):
    pat = re.compile(
        r'(<span data-stamp="' + re.escape(key) + r'">)[^<]*(</span>)')
    new, n = pat.subn(r'\g<1>' + str(value) + r'\g<2>', text)
    if n < 1:
        raise SystemExit(f"stamp span data-stamp=\"{key}\" not found")
    return new


def stamp_html(path, index, today):
    if not path.is_file():
        print(f"NOTE: {path.name} not found; skipping HTML restamp")
        return
    text = path.read_text(encoding="utf-8")
    total = index["total_generator_scripts"]
    text = _replace_stamp_span(text, "total-generators", f"{total:,}")
    text = _replace_stamp_span(text, "total-databases", f"{index['total_databases']:,}")
    text = _replace_stamp_span(text, "total-records", f"{index['total_records']:,}")
    text = _replace_stamp_span(text, "live-generators",
                               f"{index['by_status'].get('live', 0):,}")
    text = _replace_stamp_span(text, "signature-generators",
                               f"{index['by_edition'].get('Signature', 0):,}")
    text = _replace_stamp_span(text, "public-generators",
                               f"{index['by_edition'].get('Public', 0):,}")
    text = _replace_stamp_span(text, "archive-outputs",
                               f"{index['featured']['boundless_generator_archive']['indexed_outputs']:,}")
    text = _replace_stamp_span(text, "stamp-date", today)
    text = re.sub(r"(<!-- REGISTRY-STAMP:)[^-]*?( -->)",
                  r"\g<1> total=" + str(total) +
                  " databases=" + str(index["total_databases"]) +
                  " generated=" + today + r"\g<2>", text, count=1)
    path.write_text(text, encoding="utf-8")


def stamp_accessible(path, index, today):
    if not path.is_file():
        print(f"NOTE: {path.name} not found; skipping accessible restamp")
        return
    text = path.read_text(encoding="utf-8")
    total = index["total_generator_scripts"]
    text = _replace_stamp_span(text, "total-generators", f"{total:,}")
    text = _replace_stamp_span(text, "total-databases", f"{index['total_databases']:,}")
    text = _replace_stamp_span(text, "live-generators",
                               f"{index['by_status'].get('live', 0):,}")
    text = _replace_stamp_span(text, "stamp-date", today)
    rows_html = []
    for letter, count in index["by_letter"].items():
        label = "0–9" if letter == "0-9" else letter.upper()
        rows_html.append(
            f'<tr><td>{label}</td><td>{count:,}</td>'
            f'<td><a href="../generator-registry/{letter}.json">'
            f'generator-registry/{letter}.json</a></td></tr>')
    table = "\n".join(rows_html)
    new_text, n = re.subn(
        r"(<!-- LETTER-TABLE -->).*?(<!-- /LETTER-TABLE -->)",
        r"\g<1>\n" + table + r"\n\g<2>", text, count=1, flags=re.S)
    if n != 1:
        raise SystemExit("letter-table markers not found in accessible page")
    new_text = re.sub(r"(<!-- REGISTRY-STAMP:)[^-]*?( -->)",
                      r"\g<1> total=" + str(total) +
                      " databases=" + str(index["total_databases"]) +
                      " generated=" + today + r"\g<2>", new_text, count=1)
    path.write_text(new_text, encoding="utf-8")


if __name__ == "__main__":
    main()
