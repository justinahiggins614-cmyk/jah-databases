#!/usr/bin/env python3
"""Build the whole-system dedupe index for JAH Databases (his standing rule:
every generator checks the WHOLE system before generating).

Reads every database's index file, normalizes each title
EXACTLY like core/jahdb-dedupe.js, hashes with FNV-1a 64, and writes
256 hash-prefix shards:

  <out>/bloom/<xx>.json.gz  — Bloom filter per shard (browser runtime check)
  <out>/exact/<xx>.json.gz  — exact map hashhex -> [[slug, id], ...]
  <out>/manifest.json       — build metadata

Index resolution per manifest entry (code/index_paths):
  manifest URL -> local path; <X> templates glob-expanded;
  fallback data/<slug>/<basename> for entries whose manifest index URL
  names a file living under the database's own directory;
  {"shards": {...}} pointer files are followed.
Row formats: dict rows (t/title/name + id), list rows (id/title found
heuristically), plain-text .txt (one title per line).

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
    """Single-path resolution (kept for backward compatibility)."""
    ps = index_paths(repo, entry)
    return ps[0] if ps else None


def index_paths(repo, entry):
    """All local index files for a manifest entry.

    Resolution order:
      1. The manifest URL mapped to its local path (same as before).
      2. If the URL holds a <X> template (e.g. az-<L>.json.gz), glob-expand it
         in both the literal directory and data/<slug>/.
      3. Fallback: data/<slug>/<basename> when the manifest URL names a file
         that exists under the database's own directory (covers manifest
         entries whose index URL was written against a wrong directory).
    """
    import glob as _glob
    url = entry.get("index") or entry.get("local_index") or ""
    slug = entry.get("slug") or ""
    m = re.match(r"https://justinahiggins614-cmyk\.github\.io/([^/]+)/data/([^/]+)/(.+)", url)
    if m:
        c = os.path.expanduser("~/workspace/%s/data/%s/%s" % (m.group(1), m.group(2), m.group(3)))
    elif url and not url.startswith("http"):
        c = os.path.join(repo, url)
    else:
        return []
    if "<" in c and ">" in c:
        base = os.path.basename(re.sub(r"<[^>]+>", "*", c))
        out, seen = [], set()
        for d in (os.path.dirname(c), os.path.join(repo, "data", slug)):
            for h in sorted(_glob.glob(os.path.join(d, base))):
                if h not in seen:
                    seen.add(h)
                    out.append(h)
        return out
    if os.path.exists(c):
        return [c]
    fb = os.path.join(repo, "data", slug, os.path.basename(c))
    if os.path.exists(fb):
        return [fb]
    return []


ID_RE = re.compile(r"^[A-Z][A-Z0-9_.-]*-\d")

ROW_KEYS = ("rows", "records", "items", "entries", "mixes", "maps",
            "articles", "data")


def _follow_files(base, files):
    """Yield rows from relative shard/chunk files, tolerating the files
    living one level down (measures/, chunks/, shards/)."""
    for fp in files:
        if not isinstance(fp, str):
            continue
        hit = None
        for cand in (os.path.join(base, fp),
                     os.path.join(base, "measures", fp),
                     os.path.join(base, "chunks", fp),
                     os.path.join(base, "shards", fp)):
            if os.path.exists(cand):
                hit = cand
                break
        if hit:
            for r in _read_json_rows(hit):
                yield r


def _list_row_title_id(r):
    """Best-effort (title, id) from a list row, e.g. [id, title, ...],
    [seq, title, id], ["JAH-SONG-0000001", "Amber Harbor", "song"]."""
    strs = [x for x in r if isinstance(x, str)]
    ids = [x for x in strs if ID_RE.match(x)]
    title = next((x for x in strs if x not in ids and x.strip()), None)
    rid = ids[0] if ids else None
    if rid is None:
        cands = [x for x in strs if x != title]
        rid = cands[-1] if cands else None
    if rid is None:
        ints = [x for x in r if isinstance(x, int)]
        rid = str(ints[0]) if ints else None
    return title, rid


def _read_json_rows(path):
    """Yield raw rows from a .json.gz / .gz / .json index file.

    Handles: JSON array files, JSONL (dict or list rows), plain JSON
    objects, and pointer objects {"shards": {name: {"file": relpath}}}
    whose relative shard files are followed recursively.
    """
    opener = gzip.open if path.endswith(".gz") else open
    try:
        with opener(path, "rt", encoding="utf-8", errors="replace") as f:
            text = f.read()
    except OSError:
        return
    text = text.strip()
    if not text:
        return
    rows = None
    if text.startswith("[") or text.startswith("{"):
        try:
            data = json.loads(text)
        except ValueError:
            data = None  # not a single JSON value -> line-by-line below
        if data is not None:
            if isinstance(data, dict) and isinstance(data.get("shards"), dict):
                base = os.path.dirname(path)
                for spec in data["shards"].values():
                    fp = spec.get("file") if isinstance(spec, dict) else None
                    if fp:
                        for r in _follow_files(base, [fp]):
                            yield r
                return
            if isinstance(data, dict):
                for k in ROW_KEYS:
                    v = data.get(k)
                    if isinstance(v, list):
                        rows = v
                        break
                else:
                    ch = data.get("chunks")
                    if isinstance(ch, list):
                        for r in _follow_files(os.path.dirname(path), ch):
                            yield r
                        return
                    rows = [data]
            else:
                rows = data if isinstance(data, list) else [data]
    if rows is None:
        for line in text.splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                yield json.loads(line)
            except ValueError:
                pass
        return
    for r in rows:
        yield r


def iter_index_rows(path):
    """Yield (title, id) from an index file: .json.gz/.gz/.json (array,
    JSONL, or shards-pointer) or .txt (one title per line, id = title)."""
    if path.endswith(".txt"):
        try:
            with open(path, encoding="utf-8", errors="replace") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        yield line, line
        except OSError:
            return
        return
    for r in _read_json_rows(path):
        if isinstance(r, dict):
            t = r.get("t") or r.get("title") or r.get("name")
            i = r.get("id")
            if t:
                yield t, i
        elif isinstance(r, list):
            t, i = _list_row_title_id(r)
            if t:
                yield t, i
        # other row shapes are skipped


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
        ps = index_paths(repo, e)
        if not ps:
            missing += 1
            continue
        for p in ps:
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
