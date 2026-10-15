#!/usr/bin/env python3
"""Build the whole-system dedupe index for JAH Databases (his standing rule:
every generator checks the WHOLE system before generating).

Reads every database's index file (11.65M records), normalizes each title
EXACTLY like core/jahdb-dedupe.js, hashes with FNV-1a 64, and writes
256 hash-prefix shards:

  <out>/bloom/<xx>.json.gz  — Bloom filter per shard (browser runtime check)
  <out>/exact/<xx>.json.gz  — exact map hashhex -> [[slug, id], ...]
  <out>/manifest.json       — build metadata

Normalization + hashing MUST stay identical to core/jahdb-dedupe.js:
  NFKD -> strip U+0300-U+036F -> lowercase -> keep [a-z0-9] ->
  collapse whitespace -> trim -> UTF-16 code units -> FNV-1a 64.

Self-test: FNV-1a64("foobar") == 85944171f73967e8 (asserted on start).

Usage:
  python3 build_global_dedupe.py [--repo PATH] [--out DIR] [--limit-dbs N]
                                 [--shard-repos dir,dir]
  Default --out: <this-dir>/../dedupe-out  (staging; the parent copies the
  result to the data-1 shard as data/dedupe/ and commits it.)

Read-only w.r.t. the repo clone: only reads manifest + index files.
Writes only to --out.
"""
import base64
import gzip
import json
import math
import os
import re
import sys
import unicodedata
from collections import defaultdict

REPO = os.path.expanduser("~/workspace/jah-databases")
MASK64 = 0xFFFFFFFFFFFFFFFF
FNV_OFFSET = 0xCBF29CE484222325
FNV_PRIME = 0x100000001B3
BLOOM_P = 0.01


def norm_title(t):
    s = str(t or "")
    s = unicodedata.normalize("NFKD", s)
    s = re.sub(r"[\u0300-\u036f]", "", s)
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def fnv1a64_hex(s):
    h = FNV_OFFSET
    import struct
    units = struct.unpack("<%dH" % (len(s.encode("utf-16-le")) // 2),
                          s.encode("utf-16-le"))
    for unit in units:
        h ^= unit
        h = (h * FNV_PRIME) & MASK64
    return "%016x" % h


assert fnv1a64_hex("foobar") == "85944171f73967e8", "FNV-1a64 self-test failed"


def local_index_path(repo, entry):
    url = entry.get("index") or entry.get("local_index") or ""
    m = re.match(r"https://justinahiggins614-cmyk\.github\.io/([^/]+)/data/([^/]+)/(.+)", url)
    if m:
        return os.path.expanduser("~/workspace/%s/data/%s/%s" % (m.group(1), m.group(2), m.group(3)))
    if url and not url.startswith("http"):
        return os.path.join(repo, url)
    return None


def iter_index_rows(path):
    """Yield (title, id) from a .json.gz index (JSONL rows or a JSON array)."""
    try:
        with gzip.open(path, "rt", encoding="utf-8") as f:
            head = f.read(2)
            f.seek(0)
            if head.lstrip().startswith("["):
                data = json.load(f)
                rows = data if isinstance(data, list) else []
            else:
                rows = []
                for line in f:
                    line = line.strip()
                    if line:
                        try:
                            rows.append(json.loads(line))
                        except ValueError:
                            pass
    except OSError:
        return
    for r in rows:
        if not isinstance(r, dict):
            continue
        t = r.get("t") or r.get("title") or r.get("name")
        i = r.get("id")
        if t:
            yield t, i


def build_bloom(hashes):
    n = len(hashes)
    if n == 0:
        return {"n": 0, "m": 8, "k": 1,
                "bits": base64.b64encode(b"\x00").decode()}
    m = max(64, int(math.ceil(-n * math.log(BLOOM_P) / (math.log(2) ** 2))))
    k = max(1, min(12, int(round((m / n) * math.log(2)))))
    bits = bytearray((m + 7) // 8)
    h2const = 0x9E3779B97F4A7C15
    for hx in hashes:
        h1 = int(hx, 16)
        h2 = (h1 ^ h2const) & MASK64
        for i in range(k):
            idx = (h1 + i * h2) & MASK64
            idx %= m
            bits[idx >> 3] |= 1 << (idx & 7)
    return {"n": n, "m": m, "k": k,
            "bits": base64.b64encode(bytes(bits)).decode()}


def main():
    repo, out, limit, offset = REPO, None, None, 0
    args = sys.argv[1:]
    i = 0
    while i < len(args):
        if args[i] == "--repo":
            repo = args[i + 1]; i += 2
        elif args[i] == "--out":
            out = args[i + 1]; i += 2
        elif args[i] == "--limit-dbs":
            limit = int(args[i + 1]); i += 2
        elif args[i] == "--offset":
            offset = int(args[i + 1]); i += 2
        else:
            i += 1
    if not out:
        out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "..", "dedupe-out")
    os.makedirs(os.path.join(out, "bloom"), exist_ok=True)
    os.makedirs(os.path.join(out, "exact"), exist_ok=True)

    manifest = json.load(open(os.path.join(repo, "data", "manifest.json")))
    dbs = manifest["databases"][offset:]
    if limit:
        dbs = dbs[:limit]
    print("databases to scan:", len(dbs), flush=True)

    shards = defaultdict(list)   # xx -> list of hashhex
    exact = defaultdict(lambda: defaultdict(list))  # xx -> hashhex -> [[slug,id]]
    total, missing = 0, 0
    for n, e in enumerate(dbs):
        slug = e["slug"]
        p = local_index_path(repo, e)
        if not p or not os.path.exists(p):
            missing += 1
            continue
        for t, i in iter_index_rows(p):
            nt = norm_title(t)
            if not nt:
                continue
            hx = fnv1a64_hex(nt)
            xx = hx[:2]
            shards[xx].append(hx)
            exact[xx][hx].append([slug, i])
            total += 1
        if (n + 1) % 200 == 0:
            print("  scanned %d dbs, %d records" % (n + 1, total), flush=True)
    print("total records indexed: %d (missing index files: %d)" % (total, missing))

    import datetime
    for xx in sorted(shards):
        hs = shards[xx]
        bloom = build_bloom(hs)
        with gzip.open(os.path.join(out, "bloom", xx + ".json.gz"), "wt") as f:
            json.dump(bloom, f)
        with gzip.open(os.path.join(out, "exact", xx + ".json.gz"), "wt") as f:
            json.dump({"m": dict(exact[xx])}, f)
    # empty shards still get an (empty) bloom file so the browser never 404s
    for v in range(256):
        xx = "%02x" % v
        if xx not in shards:
            with gzip.open(os.path.join(out, "bloom", xx + ".json.gz"), "wt") as f:
                json.dump(build_bloom([]), f)
            with gzip.open(os.path.join(out, "exact", xx + ".json.gz"), "wt") as f:
                json.dump({"m": {}}, f)
    with open(os.path.join(out, "manifest.json"), "w") as f:
        json.dump({
            "built_at": datetime.datetime.now(
                datetime.timezone.utc).isoformat(),
            "total_records": total,
            "total_hashes": sum(len(v) for v in shards.values()),
            "unique_hashes": sum(len(v) for v in exact.values()),
            "shards": 256,
            "hash": "fnv1a64(utf16-units(nfkd-strip-lower-alnum))",
            "bloom_p": BLOOM_P,
            "version": 1,
        }, f, indent=1)
    print("wrote", out)


if __name__ == "__main__":
    main()
