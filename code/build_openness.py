#!/usr/bin/env python3
"""Build the root-level openness files for JAH Data Bases.

Regenerates: robots.txt, sitemap.xml, llms.txt, api.json
Everything is derived from data/manifest.json + a live scan of data/,
so newly added databases are picked up automatically.

Run: python3 code/build_openness.py
"""
import json, gzip, os, re, datetime, xml.sax.saxutils as sax

BASE = "https://justinahiggins614-cmyk.github.io/jah-databases"
TODAY = datetime.date.today().isoformat()
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAN = json.load(open(os.path.join(ROOT, "data", "manifest.json")))
DBS = MAN["databases"]


def url(path):
    return f"{BASE}/{path}"


def data_files():
    """All files under data/, sorted, relative."""
    out = []
    for dirpath, _dirs, files in os.walk(os.path.join(ROOT, "data")):
        for f in sorted(files):
            if f.startswith("."):
                continue
            rel = os.path.relpath(os.path.join(dirpath, f), ROOT)
            out.append(rel.replace(os.sep, "/"))
    return sorted(out)


def index_for(slug):
    """Actual index file(s) living in data/<slug>/ — prefer *.idx.* or index*."""
    d = os.path.join(ROOT, "data", slug)
    if not os.path.isdir(d):
        return []
    files = [f for f in sorted(os.listdir(d)) if os.path.isfile(os.path.join(d, f))]
    ranked = [f for f in files if ".idx." in f] or \
             [f for f in files if f.startswith("index")] or files
    return [f"data/{slug}/{f}" for f in ranked]


def row_count(path):
    """Cheap record count for json-lines / newline-delimited indexes."""
    try:
        fp = os.path.join(ROOT, path)
        if path.endswith(".gz"):
            n = 0
            with gzip.open(fp, "rt", encoding="utf-8", errors="replace") as fh:
                for _ in fh:
                    n += 1
            return n
        if path.endswith(".json"):
            with open(fp, encoding="utf-8", errors="replace") as fh:
                d = json.load(fh)
            if isinstance(d, list):
                return len(d)
            if isinstance(d, dict):
                for k in ("count", "total", "records", "articles", "count_total"):
                    if k in d and isinstance(d[k], (int,)):
                        return d[k]
        if path.endswith(".txt"):
            with open(fp, encoding="utf-8", errors="replace") as fh:
                return sum(1 for _ in fh)
    except Exception:
        pass
    return None


def build_robots():
    return "\n".join([
        "User-agent: *",
        "Allow: /",
        f"Sitemap: {url('sitemap.xml')}",
        "",
        "# JAH Data Bases — Project Three.",
        "# Everything here is public and open: AI crawlers and bots are welcome.",
        "",
    ])


def build_sitemap(df):
    urls = []
    urls.append("index.html")
    urls.append("llms.txt")
    urls.append("api.json")
    urls.append("docs/AI_ACCESS.md")
    urls.append("docs/LIMITS.md")
    for x in DBS:
        urls.append(f"db/{x['slug']}/")
    for c in ("jahdb.js", "standard-1.0.js", "guide-conv.js", "apex-2.0.js"):
        urls.append(f"core/{c}")
    urls.extend(df)
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for p in urls:
        lines.append("  <url>")
        lines.append(f"    <loc>{sax.escape(url(p))}</loc>")
        lines.append(f"    <lastmod>{TODAY}</lastmod>")
        lines.append("  </url>")
    lines.append("</urlset>")
    return "\n".join(lines) + "\n"


def build_llms(df, counts):
    L = []
    L.append("# JAH Data Bases")
    L.append("")
    L.append("> A public, open network of JAH databases — every record archive, index, and")
    L.append("> generator is published and readable by anyone and any AI. No login, no key,")
    L.append("> no fee. Licensed for open machine reading.")
    L.append("")
    L.append("## How any AI reads every record")
    L.append("")
    L.append("1. **Catalog**: fetch `data/manifest.json` — lists every database, its slug,")
    L.append("   record kind, AI librarian name, and ID prefix.")
    L.append("2. **Archive indexes**: each database keeps its index file(s) in")
    L.append("   `data/<slug>/`. `.gz` files are gzip-compressed newline-delimited JSON —")
    L.append("   one record per line. Plain `.json` indexes are ordinary JSON.")
    L.append("   (Index paths per database are listed in api.json and below.)")
    L.append("3. **Deterministic generator**: `core/jahdb.js` exposes the JAHDB generator")
    L.append("   engine. Any record N can be reproduced from its seed — the million-record")
    L.append("   archives are fully addressable without storing every file.")
    L.append("4. **Per-record pages**: every database page (`db/<slug>/`) supports the")
    L.append("   `?record=<id>` deep link, e.g. `db/patents/?record=JAH-PAT-000123`.")
    L.append("5. **Full manifest map**: `api.json` at the root lists every database with")
    L.append("   page URL, index file URLs, record kind, and record counts.")
    L.append("")
    L.append("## The databases")
    L.append("")
    for x in DBS:
        slug = x["slug"]
        L.append(f"### {x['name']} ({slug})")
        L.append(f"- Page: {url('db/' + slug + '/')}")
        for p in index_for(slug):
            c = counts.get(p)
            cstr = f" (~{c:,} rows)" if c else ""
            L.append(f"- Index: {url(p)}{cstr}")
        L.append(f"- Records: {x.get('record_kind', 'records')} · AI: {x.get('ai_name', '—')}")
        L.append(f"- {x.get('tagline', '').strip()}")
        L.append("")
    L.append("## Project-level files")
    L.append("")
    L.append(f"- Manifest: {url('data/manifest.json')}")
    L.append(f"- API catalog: {url('api.json')}")
    L.append(f"- Sitemap: {url('sitemap.xml')}")
    L.append(f"- Engine: {url('core/jahdb.js')}")
    L.append("- Reading guide: docs/AI_ACCESS.md")
    L.append("")
    return "\n".join(L)


def build_api(df, counts):
    dbs = []
    for x in DBS:
        slug = x["slug"]
        idx = index_for(slug)
        dbs.append({
            "slug": slug,
            "name": x["name"],
            "tagline": x.get("tagline", ""),
            "record_kind": x.get("record_kind", "records"),
            "id_prefix": x.get("id_prefix", ""),
            "ai_name": x.get("ai_name", ""),
            "page_url": url(f"db/{slug}/"),
            "index_files": [url(p) for p in idx],
            "record_counts": {p: counts[p] for p in idx if p in counts},
            "status": x.get("status", "live"),
        })
    return {
        "project": "JAH Data Bases",
        "tagline": "Public, open databases — every record readable by any AI or bot.",
        "database_count": len(dbs),
        "open_policy": {
            "login_required": False,
            "api_key_required": False,
            "robots": "all crawlers allowed",
            "cors": "Access-Control-Allow-Origin: *",
        },
        "project_files": {
            "manifest": url("data/manifest.json"),
            "sitemap": url("sitemap.xml"),
            "llms": url("llms.txt"),
            "robots": url("robots.txt"),
            "engine": url("core/jahdb.js"),
            "ai_access_guide": url("docs/AI_ACCESS.md"),
            "limits_guide": url("docs/LIMITS.md"),
        },
        "databases": dbs,
    }


def main():
    df = data_files()
    counts = {}
    for p in df:
        base = os.path.basename(p)
        if ".idx." in base or base.startswith("index") or p == "data/wiki/articles.json":
            c = row_count(p)
            if c:
                counts[p] = c
    files = {
        "robots.txt": build_robots(),
        "sitemap.xml": build_sitemap(df),
        "llms.txt": build_llms(df, counts),
        "api.json": json.dumps(build_api(df, counts), indent=2) + "\n",
    }
    for name, content in files.items():
        with open(os.path.join(ROOT, name), "w", encoding="utf-8") as fh:
            fh.write(content)
        print(f"wrote {name}: {len(content):,} chars, {len(content.encode())/1024:.1f} KB")
    sm = files["sitemap.xml"]
    nurls = sm.count("<loc>")
    print(f"sitemap URLs: {nurls}, size {len(sm.encode())/1024/1024:.2f} MB")


if __name__ == "__main__":
    main()
