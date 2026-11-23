#!/usr/bin/env python3
"""Independent verifier for the sharded registry + paginated hub index.

Does NOT import code/build_paginated_registry.py. Re-reads
data/registry/registry.json and every shard file from disk, re-reads the
source manifest fresh, and walks the page FILES on disk exactly as a
text-fetch reader would (following each page's own next_page pointer).
Checks:
  Registry (Fix 1):
    1. Every shard parses as JSON and is < 1,000,000 bytes (measured on disk).
    2. Per-shard counts sum to the manifest total and agree with
       registry.json totals and with the manifest's database_count field.
    3. Every slug appears exactly once across all shards (no gaps, no
       dupes) and the slug set equals the manifest slug set.
    4. Shard entries are equal (same fields, same values) to the manifest
       entries, and sorted by slug within each shard; shard ranges are
       contiguous across shards.
    5. Spot-check >= 20 slugs through the resolver's own binary-search
       logic (first + last slug of every shard, plus a fixed seeded-random
       sample): each resolves to its correct shard and its entry matches
       the manifest exactly.
    6. registry.json sha256 values match the shard files on disk, and the
       recorded source-manifest sha256/bytes match the manifest on disk.
  Pages (Fix 2):
    7. Page file count matches contract arithmetic (100/page).
    8. Page chain integrity: page 1..N linked by prev_page/next_page,
       page numbers sequential, totals consistent on every page, first/last
       slugs match the entries, remaining_after_this_page arithmetic
       correct, last page has next_page/next_cursor null, all other pages
       non-null, source stamp matches the manifest on disk.
    9. Exhaustive pass: following next_page from page 1 recovers every
       slug exactly once; slug order strictly ascending; the walked set
       equals the registry slug set.
   10. Resume from mid-point cursors (--resume N, default 315; a second
       resume at 500 is run automatically): walking from page N to the end
       recovers exactly the slugs NOT covered by pages 1..N-1, with no gaps
       and no dupes; union with the head pass = the full set.
   11. Every page entry's shard pointer names a real shard file whose
       range contains the slug, and the entry's name/record_count match
       the shard.
Exit 0 = all checks pass. Prints a PASS/FAIL line per check.
Usage: python3 code/verify_paginated_registry.py [--resume N]
"""
import argparse
import bisect
import hashlib
import json
import os
import random
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REGISTRY_DIR = os.path.join(ROOT, "data", "registry")
PAGES_DIR = os.path.join(ROOT, "data", "pages")
MANIFEST_PATH = os.path.join(ROOT, "data", "manifest.json")
HARD_LIMIT = 1_000_000
PAGE_SIZE = 100

failures = []


def check(name, ok, detail=""):
    print(f"[{'PASS' if ok else 'FAIL'}] {name}"
          + (f" — {detail}" if detail else ""))
    if not ok:
        failures.append(name)


def load_page(n):
    with open(os.path.join(PAGES_DIR, f"page-{n:03d}.json")) as f:
        return json.load(f)


def find_shard(reg, slug):
    """Resolver logic: binary search over shard first/last ranges."""
    shards = reg["shards"]
    lasts = [s["last_slug"] for s in shards]
    i = bisect.bisect_left(lasts, slug)
    if i >= len(shards):
        return None
    s = shards[i]
    if s["first_slug"] <= slug <= s["last_slug"]:
        return s
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--resume", type=int, default=315,
                    help="mid-point page to resume from (default 315)")
    args = ap.parse_args()

    with open(os.path.join(REGISTRY_DIR, "registry.json")) as f:
        reg = json.load(f)
    with open(MANIFEST_PATH, "rb") as f:
        raw = f.read()
    manifest = json.loads(raw.decode("utf-8"))
    m_by_slug = {e["slug"]: e for e in manifest["databases"]}
    m_count_field = manifest.get("database_count")
    total = len(m_by_slug)

    # ---- Registry checks ----
    all_slugs, shard_total, max_bytes = [], 0, 0
    shard_entries = {}
    prev_last = None
    contiguous = True
    for meta in reg["shards"]:
        path = os.path.join(REGISTRY_DIR, meta["file"])
        size = os.path.getsize(path)
        max_bytes = max(max_bytes, size)
        if size >= HARD_LIMIT:
            check(f"shard {meta['shard']} < 1MB", False, f"{size} bytes")
        with open(path) as f:
            shard = json.load(f)
        if shard["count"] != len(shard["entries"]):
            check(f"shard {meta['shard']} count field", False,
                  f"field {shard['count']} != entries {len(shard['entries'])}")
        if shard["count"] != meta["count"]:
            check(f"shard {meta['shard']} registry count", False)
        if shard["first_slug"] != meta["first_slug"] or \
                shard["last_slug"] != meta["last_slug"]:
            check(f"shard {meta['shard']} registry ranges", False)
        if shard["first_slug"] != shard["entries"][0]["slug"] or \
                shard["last_slug"] != shard["entries"][-1]["slug"]:
            check(f"shard {meta['shard']} first/last match entries", False)
        if hashlib.sha256(open(path, "rb").read()).hexdigest() != meta["sha256"]:
            check(f"shard {meta['shard']} sha256", False)
        if meta["bytes"] != size:
            check(f"shard {meta['shard']} registry bytes", False,
                  f"registry {meta['bytes']} != disk {size}")
        slugs = [e["slug"] for e in shard["entries"]]
        if slugs != sorted(slugs):
            check(f"shard {meta['shard']} sorted by slug", False)
        if prev_last is not None and not (prev_last < shard["first_slug"]):
            contiguous = False
        prev_last = shard["last_slug"]
        all_slugs.extend(slugs)
        shard_total += len(slugs)
        shard_entries[meta["shard"]] = shard["entries"]
    check("all shards < 1,000,000 bytes", max_bytes < HARD_LIMIT,
          f"max {max_bytes} bytes over {len(reg['shards'])} shards")
    check("shard ranges contiguous across shards", contiguous)
    check("per-shard counts sum to manifest total",
          shard_total == total, f"sum={shard_total} total={total}")
    check("registry total_entries agrees", reg["total_entries"] == shard_total)
    check("registry shard_count agrees",
          reg["shard_count"] == len(reg["shards"]))
    check("manifest database_count field agrees",
          m_count_field == shard_total == total, f"field={m_count_field}")
    check("no duplicate slugs across shards",
          len(all_slugs) == len(set(all_slugs)),
          f"{len(all_slugs)} listed, {len(set(all_slugs))} unique")
    check("shard slug set == manifest slug set",
          set(all_slugs) == set(m_by_slug),
          f"missing={len(set(m_by_slug) - set(all_slugs))} "
          f"extra={len(set(all_slugs) - set(m_by_slug))}")
    mismatches = 0
    for entries in shard_entries.values():
        for e in entries:
            if e != m_by_slug.get(e["slug"]):
                mismatches += 1
    check("every shard entry == manifest entry verbatim",
          mismatches == 0, f"{mismatches} mismatches")

    # Resolver spot-check: first+last of every shard + 25 seeded-random.
    sample = set()
    for meta in reg["shards"]:
        sample.add(meta["first_slug"])
        sample.add(meta["last_slug"])
    rng = random.Random(20261102)  # fixed seed: reproducible sample
    sample.update(rng.sample(sorted(m_by_slug), 25))
    sample = sorted(sample)
    bad = []
    shard_by_slug = {}
    for meta in reg["shards"]:
        for e in shard_entries[meta["shard"]]:
            shard_by_slug[e["slug"]] = (meta["file"], e)
    for slug in sample:
        meta = find_shard(reg, slug)
        want = shard_by_slug.get(slug)
        if meta is None or want is None or meta["file"] != want[0] \
                or want[1] != m_by_slug[slug]:
            bad.append(slug)
    check(f"resolver spot-check ({len(sample)} slugs: first+last of every "
          "shard + 25 seeded-random)", not bad,
          f"{len(bad)} bad: {bad[:3]}" if bad else
          f"all {len(sample)} resolved to their correct shard")

    check("registry source sha256 matches manifest on disk",
          reg["source"]["sha256"] == hashlib.sha256(raw).hexdigest())
    check("registry source byte size matches manifest on disk",
          reg["source"]["bytes"] == len(raw), f"{len(raw)} bytes")

    # ---- Page checks ----
    files = sorted(n for n in os.listdir(PAGES_DIR)
                   if n.startswith("page-") and n.endswith(".json"))
    total_pages = len(files)
    check("page file count matches contract arithmetic",
          total_pages == (total + PAGE_SIZE - 1) // PAGE_SIZE,
          f"{total_pages} files for {total} entries at 100/page")

    seen, order_ok = [], True
    prev_slug = None
    chain_bad = []
    n = 1
    while True:
        page = load_page(n)
        if page["page"] != n:
            chain_bad.append(f"page file {n} says page {page['page']}")
        if page["page_size"] != PAGE_SIZE:
            chain_bad.append(f"page {n}: page_size {page['page_size']}")
        if page["total_items"] != total or page["total_pages"] != total_pages:
            chain_bad.append(f"page {n}: totals {page['total_items']}/"
                             f"{page['total_pages']}")
        if page["items_on_page"] != len(page["entries"]):
            chain_bad.append(f"page {n}: items_on_page mismatch")
        if page["entries"][0]["slug"] != page["first_slug"] or \
                page["entries"][-1]["slug"] != page["last_slug"]:
            chain_bad.append(f"page {n}: first/last slug mismatch")
        expect_prev = f"page-{n - 1:03d}.json" if n > 1 else None
        expect_next = (f"page-{n + 1:03d}.json"
                       if n < total_pages else None)
        if page["prev_page"] != expect_prev or \
                page["next_page"] != expect_next:
            chain_bad.append(f"page {n}: prev/next pointer mismatch")
        expect_cursor = f"page:{n + 1}" if n < total_pages else None
        if page["next_cursor"] != expect_cursor:
            chain_bad.append(f"page {n}: next_cursor {page['next_cursor']}")
        expect_remaining = total - n * PAGE_SIZE if n < total_pages else 0
        if page["remaining_after_this_page"] != expect_remaining:
            chain_bad.append(f"page {n}: remaining "
                             f"{page['remaining_after_this_page']} != "
                             f"{expect_remaining}")
        if page["source_registry_sha256"] != reg["source"]["sha256"]:
            chain_bad.append(f"page {n}: source sha mismatch")
        for e in page["entries"]:
            if prev_slug is not None and not (prev_slug < e["slug"]):
                order_ok = False
            prev_slug = e["slug"]
            seen.append(e["slug"])
            want = shard_by_slug.get(e["slug"])
            if want is None:
                chain_bad.append(f"page {n}: slug {e['slug']} not in "
                                 "registry")
            elif ("../registry/" + want[0] != e["shard"]
                    or want[1]["name"] != e["name"]
                    or want[1].get("record_count") != e["record_count"]):
                chain_bad.append(f"page {n}: entry {e['slug']} disagrees "
                                 "with its shard")
        if page["next_page"] is None:
            break
        n += 1
        if n > total_pages + 5:  # runaway guard
            chain_bad.append("chain did not terminate")
            break
    check("page chain integrity (pointers, totals, cursors, remaining, "
          "source stamp on every page)", not chain_bad,
          f"{len(chain_bad)} problems: {chain_bad[:3]}" if chain_bad else
          f"{total_pages} pages walked via next_page pointers")
    check(f"exhaustive pass recovers {total:,} unique slugs exactly once",
          len(seen) == total and len(set(seen)) == total,
          f"walked {len(seen)}, unique {len(set(seen))}")
    check("walk order strictly ascending by slug", order_ok)
    check("walked slug set == registry slug set",
          set(seen) == set(all_slugs),
          f"missing={len(set(all_slugs) - set(seen))} "
          f"extra={len(set(seen) - set(all_slugs))}")
    check("walk ended on last page with next_cursor null",
          n == total_pages and load_page(n)["next_cursor"] is None,
          f"ended at page {n} of {total_pages}")

    # Resume tests: default resume page + page 500 (if in range).
    for resume_page in sorted({args.resume, 500}):
        if not (1 < resume_page <= total_pages):
            print(f"resume page {resume_page} out of range 2..{total_pages}")
            continue
        head = set()
        for pn in range(1, resume_page):
            head.update(e["slug"] for e in load_page(pn)["entries"])
        tail = []
        m = resume_page
        while True:
            page = load_page(m)
            if page["next_cursor"] is not None:
                assert page["next_cursor"] == f"page:{m + 1}", \
                    f"resume walk: page {m} cursor wrong"
            tail.extend(e["slug"] for e in page["entries"])
            if page["next_page"] is None:
                break
            m += 1
        check(f"resume from page:{resume_page} completes the set",
              len(tail) == total - len(head)
              and len(set(tail)) == len(tail)
              and not (set(tail) & head)
              and (head | set(tail)) == set(all_slugs),
              f"head={len(head)} pages 1..{resume_page - 1}, "
              f"tail={len(tail)} pages {resume_page}..{total_pages}, "
              f"overlap={len(set(tail) & head)}, "
              f"union={len(head | set(tail))}")
        check(f"resume walk ends at page {total_pages} with next_cursor null",
              m == total_pages)

    print()
    if failures:
        print(f"VALIDATION FAILED: {len(failures)} check(s) failed: {failures}")
        return 1
    print("VALIDATION PASSED: all registry + pagination checks green")
    return 0


if __name__ == "__main__":
    sys.exit(main())
