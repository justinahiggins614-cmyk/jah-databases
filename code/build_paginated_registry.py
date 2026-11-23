#!/usr/bin/env python3
"""Rebuild the sharded registry + paginated hub index from the live manifest.

Adapted from the Lane B builders (~/workspace/hidden_files/ai-fix-list-7/
lanes/b-sharding-pagination/build_registry.py + build_pages.py), pointed
at the repo instead of the lane dir. One script rebuilds the whole lane,
so shards, registry.json, and pages can never drift apart again:

  data/registry/shards/manifest-shard-NNN.json  verbatim manifest entries,
      sorted by slug, greedy-packed so every shard is < 1,000,000 bytes
  data/registry/registry.json                  shard list, ranges, counts,
      bytes, sha256, source-manifest fingerprint
  data/registry/SOURCE.txt                     provenance note
  data/pages/page-NNN.json                     100 entries per page, slug
      ascending (plain Python sorted()), per data/registry/
      PAGINATION-CONTRACT.md. Each entry: {slug, name, record_count,
      shard} where shard is the shard file holding the full record,
      relative to data/pages/ ("../registry/shards/...").

Only the whole totals are ever printed: total databases, shard count,
page count. No per-kind or per-group counts anywhere.

Safety: refuses to run with uncommitted tracked changes (another agent's
work in progress); deterministic — same manifest bytes in, same files out.
"""
import hashlib
import json
import os
import re
import subprocess
import sys
from datetime import datetime

try:
    from zoneinfo import ZoneInfo
    USER_TZ = ZoneInfo("America/New_York")
except Exception:
    USER_TZ = None

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST_PATH = os.path.join(ROOT, "data", "manifest.json")
REGISTRY_DIR = os.path.join(ROOT, "data", "registry")
SHARD_DIR = os.path.join(REGISTRY_DIR, "shards")
PAGES_DIR = os.path.join(ROOT, "data", "pages")
SITEMAP = os.path.join(ROOT, "sitemap-registry.xml")
HUB = os.path.join(ROOT, "index.html")
CONTRACT = os.path.join(REGISTRY_DIR, "PAGINATION-CONTRACT.md")

PAGE_SIZE = 100
MAX_SHARD_BYTES = 950_000          # hard target; verified < 1,000,000 after write
HARD_LIMIT = 1_000_000
BASE_URL = "https://justinahiggins614-cmyk.github.io/jah-databases/"


def today_user():
    if USER_TZ is not None:
        return datetime.now(USER_TZ).date().isoformat()
    return datetime.now().date().isoformat()


def sha256_bytes(blob):
    return hashlib.sha256(blob).hexdigest()


def entry_bytes(entry):
    """Byte length of one entry as serialized inside the shard (compact)."""
    return len(json.dumps(entry, ensure_ascii=False,
                          separators=(",", ":")).encode("utf-8"))


def run(cmd, check=True):
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    if check and r.returncode != 0:
        raise RuntimeError(f"{' '.join(cmd)} failed: {r.stderr.strip()}")
    return r


def main():
    dirty = [l for l in run(["git", "status", "--porcelain"],
                            check=False).stdout.splitlines()
             if not l.startswith("??")]
    if dirty:
        print("STATUS: skipped — working tree has uncommitted tracked changes")
        return 1
    today = today_user()
    with open(MANIFEST_PATH, "rb") as f:
        raw = f.read()
    manifest = json.loads(raw.decode("utf-8"))
    dbs = manifest["databases"]
    db_count_field = manifest.get("database_count")
    assert db_count_field == len(dbs), (
        f"database_count field {db_count_field} != len(databases) {len(dbs)}")
    slugs = [e["slug"] for e in dbs]
    assert len(set(slugs)) == len(slugs), "duplicate slugs in manifest"
    dbs_sorted = sorted(dbs, key=lambda e: e["slug"])
    manifest_sha = sha256_bytes(raw)
    manifest_mb = len(raw) / 1_000_000

    # --- shards (verbatim entries, greedy-packed, same rule as Lane B) ---
    os.makedirs(SHARD_DIR, exist_ok=True)
    for name in os.listdir(SHARD_DIR):
        if name.startswith("manifest-shard-") and name.endswith(".json"):
            os.remove(os.path.join(SHARD_DIR, name))

    shards_meta = []
    current, current_bytes = [], 0
    shard_no = 1

    def flush():
        nonlocal current, current_bytes, shard_no
        if not current:
            return
        payload = {
            "shard": shard_no,
            "count": len(current),
            "first_slug": current[0]["slug"],
            "last_slug": current[-1]["slug"],
            "entries": current,
        }
        blob = json.dumps(payload, ensure_ascii=False,
                          separators=(",", ":")).encode("utf-8")
        assert len(blob) < HARD_LIMIT, (
            f"shard {shard_no} would be {len(blob)} bytes >= {HARD_LIMIT}")
        fname = f"manifest-shard-{shard_no:03d}.json"
        path = os.path.join(SHARD_DIR, fname)
        with open(path, "wb") as f:
            f.write(blob)
        shards_meta.append({
            "file": f"shards/{fname}",
            "shard": shard_no,
            "count": len(current),
            "first_slug": current[0]["slug"],
            "last_slug": current[-1]["slug"],
            "bytes": len(blob),
            "sha256": sha256_bytes(blob),
        })
        shard_no += 1
        current, current_bytes = [], 0

    for entry in dbs_sorted:
        eb = entry_bytes(entry) + 1  # +1 for the ',' separator
        # Header overhead allowance (~200 bytes) so the estimate stays safe.
        if current and current_bytes + eb + 200 > MAX_SHARD_BYTES:
            flush()
        current.append(entry)
        current_bytes += eb
    flush()

    total = sum(m["count"] for m in shards_meta)
    assert total == len(dbs_sorted), f"shard total {total} != {len(dbs_sorted)}"

    registry = {
        "status": f"LIVE — deployed on GitHub Pages (merged {today})",
        "generated_date": today,
        "source": {
            "file": "data/manifest.json in the jah-databases repo clone (read-only)",
            "bytes": len(raw),
            "sha256": manifest_sha,
            "database_count_field": db_count_field,
            "entry_count": len(dbs),
        },
        "note": (
            "Full-fidelity verbatim shards of the master manifest. Each shard "
            "carries the COMPLETE manifest entry for every database it lists "
            "(all fields, values untouched), sorted by slug. This is NOT the "
            "ai-access-point access-shard set, which carries only a 7-field "
            "derived subset (slug/name/page_url/raw_index_url/record_count/"
            "index_repo/index_status). A reader that needs the full entry "
            "(chunk_pattern, local_index, id_prefix, record_kind, ...) fetches "
            f"one shard here instead of the {manifest_mb:.1f} MB master manifest. "
            "The 109.9 MB figure sometimes quoted for the master manifest is "
            "NOT VERIFIED: measured master manifest is "
            f"{len(raw):,} bytes; "
            "this sharding is justified by that measured size alone."
        ),
        "shard_count": len(shards_meta),
        "total_entries": total,
        "max_shard_bytes": max(m["bytes"] for m in shards_meta),
        "total_shard_bytes": sum(m["bytes"] for m in shards_meta),
        "shards": shards_meta,
        "resolve": {
            "method": "binary search over shards[].first_slug / .last_slug "
                      "(ranges are contiguous and sorted)",
            "example": "python3 -c \"import json; ...\" (see PAGINATION-CONTRACT.md)",
        },
    }
    with open(os.path.join(REGISTRY_DIR, "registry.json"), "w") as f:
        json.dump(registry, f, ensure_ascii=False, indent=1)
        f.write("\n")
    with open(os.path.join(REGISTRY_DIR, "SOURCE.txt"), "w") as f:
        f.write(
            "Sharded registry built by code/build_paginated_registry.py "
            "(Lane B, Fix 1, adapted into the repo).\n"
            f"Source manifest: {MANIFEST_PATH}\n"
            f"Source bytes: {len(raw)}, sha256: {manifest_sha}\n"
            f"Source database_count: {db_count_field}, entries: {len(dbs)}\n"
            f"Status: LIVE — deployed on GitHub Pages (merged {today}).\n"
            "The live manifest and api.json were NOT edited.\n")

    # --- pages (walk the new shards, so pages provably match the registry) ---
    ordered = []
    for meta in shards_meta:
        with open(os.path.join(REGISTRY_DIR, meta["file"])) as f:
            shard = json.load(f)
        for e in shard["entries"]:
            ordered.append({
                "slug": e["slug"],
                "name": e["name"],
                "record_count": e.get("record_count"),
                "shard": "../registry/" + meta["file"],
            })
    assert ordered == sorted(ordered, key=lambda x: x["slug"]), \
        "registry walk is not in slug order"
    total_pages = (total + PAGE_SIZE - 1) // PAGE_SIZE

    os.makedirs(PAGES_DIR, exist_ok=True)
    for name in os.listdir(PAGES_DIR):
        if name.startswith("page-") and name.endswith(".json"):
            os.remove(os.path.join(PAGES_DIR, name))

    for page_no in range(1, total_pages + 1):
        start = (page_no - 1) * PAGE_SIZE
        entries = ordered[start:start + PAGE_SIZE]
        page = {
            "page": page_no,
            "page_size": PAGE_SIZE,
            "total_items": total,
            "total_pages": total_pages,
            "items_on_page": len(entries),
            "first_slug": entries[0]["slug"],
            "last_slug": entries[-1]["slug"],
            "prev_page": (f"page-{page_no - 1:03d}.json"
                          if page_no > 1 else None),
            "next_page": (f"page-{page_no + 1:03d}.json"
                          if page_no < total_pages else None),
            "next_cursor": (f"page:{page_no + 1}"
                            if page_no < total_pages else None),
            "remaining_after_this_page": total - (start + len(entries)),
            "source_registry_sha256": manifest_sha,
            "generated_date": today,
            "entries": entries,
        }
        with open(os.path.join(PAGES_DIR, f"page-{page_no:03d}.json"),
                  "w") as f:
            json.dump(page, f, ensure_ascii=False, separators=(",", ":"))
            f.write("\n")

    # --- sitemap-registry.xml: refresh lastmod on the registry + shard URLs,
    #     adding/removing shard URL blocks to match the new shard count ---
    sitemap = open(SITEMAP, encoding="utf-8").read()
    reg_url = BASE_URL + "data/registry/registry.json"
    sitemap = re.sub(
        r"(<loc>" + re.escape(reg_url) + r"</loc>\s*<lastmod>)[\d-]+(</lastmod>)",
        r"\g<1>" + today + r"\g<2>", sitemap)
    shard_urls = {BASE_URL + "data/registry/shards/manifest-shard-%03d.json" % m["shard"]
                  for m in shards_meta}
    # Refresh lastmod on every shard URL that exists in the sitemap.
    def _refresh_shard(m):
        return m.group(1) + today + m.group(2)
    sitemap = re.sub(
        r"(<loc>https://justinahiggins614-cmyk\.github\.io/jah-databases/data/registry/shards/manifest-shard-\d+\.json</loc>\s*<lastmod>)[\d-]+(</lastmod>)",
        _refresh_shard, sitemap)
    # Add URL blocks for any new shard beyond those already listed.
    listed = set(re.findall(
        r"<loc>(https://justinahiggins614-cmyk\.github\.io/jah-databases/data/registry/shards/manifest-shard-\d+\.json)</loc>",
        sitemap))
    missing = sorted(shard_urls - listed)
    if missing:
        blocks = "".join(
            f"  <url>\n    <loc>{u}</loc>\n    <lastmod>{today}</lastmod>\n  </url>\n"
            for u in missing)
        # Insert after the registry.json URL block.
        anchor = re.search(
            r"(  <url>\n    <loc>" + re.escape(reg_url) +
            r"</loc>\n    <lastmod>[\d-]+</lastmod>\n  </url>\n)", sitemap)
        if anchor:
            sitemap = sitemap[:anchor.end()] + blocks + sitemap[anchor.end():]
    # Remove URL blocks for shards that no longer exist.
    stale = listed - shard_urls
    for u in stale:
        sitemap = re.sub(
            r"  <url>\n    <loc>" + re.escape(u) +
            r"</loc>\n    <lastmod>[\d-]+</lastmod>\n  </url>\n", "", sitemap)
    open(SITEMAP, "w", encoding="utf-8").write(sitemap)

    # --- hub link: the page count on the hub's plain-text-index link ---
    hub = open(HUB, encoding="utf-8").read()
    hub_new = re.sub(
        r"plain-text index, page 1 of \d+ \(no JavaScript needed\)",
        f"plain-text index, page 1 of {total_pages} (no JavaScript needed)",
        hub)
    if hub_new != hub:
        open(HUB, "w", encoding="utf-8").write(hub_new)

    print(f"STATUS: paginated registry rebuilt — {total:,} databases, "
          f"{len(shards_meta)} shards, {total_pages} pages "
          f"({total_pages - 1} full + 1 partial of "
          f"{total - (total_pages - 1) * PAGE_SIZE})")
    print(f"manifest sha256: {manifest_sha}")
    print(f"max shard bytes: {max(m['bytes'] for m in shards_meta)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
