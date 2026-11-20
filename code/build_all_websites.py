#!/usr/bin/env python3
"""Build the all-websites list for The 'Merica-L Internet.

Generates, from TRACKED files only (git ls-files, so the list matches
what is deployed on GitHub Pages):
  all-websites.json          — compact list: [name, url, kind] per website
  all-websites.html          — the list page: search + kind filter +
                               one collapsed drop-down per first letter
                               (a letter's links are built only when opened)
  accessible/all-websites.html — plain static list, no JavaScript needed

Classification — every live website main page, counted exactly once:
  main   — the main sites from the OS page's own sites list, plus the
           database hub itself (JAH Databases)
  mirror — mirrors/<slug>/index.html
  dbweb  — db/*/website/index.html, plus the two Wave 1 database pages
           (db/marijuana-supplies, db/marijuana-supplies-signature)
  file   — db/*/records/*.html, excluding /accessible/ and /mirror/
  mix    — db/*/mixes/*/index.html (excluding /accessible/ and /mirror/),
           plus the Wave 1 set master and grinder mix
  dbpage — db/*/index.html, excluding the pages counted above

NOTE: no group on the page carries its own count, and the main-sites
group is never counted out loud anywhere in this output — the page
shows one total for the whole network only.
"""
import html
import json
import os
import re
import subprocess
import sys
from datetime import date, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://justinahiggins614-cmyk.github.io/"
OS_PAGE = os.path.join(ROOT, "the-merica-l-boundless-ecosystem-os.html")
MANIFEST = os.path.join(ROOT, "data", "manifest.json")

KINDS = {
    "main": "Main site",
    "mirror": "Mirror",
    "dbweb": "Database website",
    "file": "File website",
    "mix": "Mix website",
    "dbpage": "Database page",
}
# Wave 1 pages that double as a per-artifact website (counted there, never twice).
DBWEB_EXTRA = {"marijuana-supplies", "marijuana-supplies-signature"}
MIX_EXTRA = {"db/marijuana-supplies-set/index.html",
             "db/marijuana-supplies-set/complete-grinder-system/index.html"}
DBPAGE_EXCLUDE = {"marijuana-supplies", "marijuana-supplies-signature",
                  "marijuana-supplies-set"}


def run(cmd):
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"{' '.join(cmd)} failed: {r.stderr.strip()}")
    return r.stdout.splitlines()


def ls_files(*patterns):
    return [p for p in run(["git", "ls-files"] + list(patterns)) if p]


def unescape_stable(s):
    """html.unescape until stable — page titles and manifest names are
    sometimes double-encoded (&amp;mdash; / &amp;hellip;)."""
    for _ in range(3):
        t = html.unescape(s)
        if t == s:
            return t
        s = t
    return s


def page_title(path):
    """<title> of a tracked HTML file on disk, unescaped, or ''."""
    try:
        with open(os.path.join(ROOT, path), encoding="utf-8", errors="ignore") as f:
            chunk = f.read(4096)
    except OSError:
        return ""
    m = re.search(r"<title>(.*?)</title>", chunk, re.S | re.I)
    if not m:
        return ""
    t = unescape_stable(m.group(1))
    t = re.sub(r"<[^>]+>", "", t)
    return " ".join(t.split())


def clean_name(t, suffixes=()):
    """Strip a known ' — <suffix>' tail and stray wrapping quotes."""
    for suf in suffixes:
        if suf and t.endswith(" — " + suf):
            t = t[: -len(" — " + suf)]
            break
    t = t.strip().strip("\"'“”").strip()
    if len(t) > 140:
        t = t[:137].rstrip() + "…"
    return t


def letter_of(name):
    # ASCII letters only, to match the page's JavaScript letterOf exactly:
    # a name starting with a non-ASCII letter groups under its first
    # ASCII letter, or '#' if it has none.
    s = name.lstrip("\"'“”‘([{")
    for ch in s:
        if "A" <= ch <= "Z" or "a" <= ch <= "z":
            return ch.upper()
        if ch.isdigit():
            return "0-9"
    return "#"


def main():
    manifest = json.load(open(MANIFEST, encoding="utf-8"))
    # Manifest names sometimes carry literal entities ("&mdash;") and the
    # " — JAH Databases" title suffix — unescape and strip them here so
    # list names are clean plain text.
    names = {}
    for d in manifest["databases"]:
        nm = unescape_stable(d["name"])
        if nm.endswith(" — JAH Databases"):
            nm = nm[: -len(" — JAH Databases")]
        names[d["slug"]] = nm

    sites = []  # [name, url, kind]

    # --- main sites: the OS page's own sites list, in canonical order ---
    os_html = open(OS_PAGE, encoding="utf-8").read()
    m = re.search(r'<ol class="sites">(.*?)</ol>', os_html, re.S)
    if not m:
        m = re.search(r'<ul class="sites">(.*?)</ul>', os_html, re.S)
    if not m:
        raise RuntimeError("no sites list on the OS page")
    for href, text in re.findall(r'<a href="([^"]+)">([^<]+)</a>', m.group(1)):
        sites.append([html.unescape(text).strip(), href, "main"])
    # The database hub itself — a website too, listed with the main sites.
    sites.append(["JAH Databases — the database hub", BASE + "jah-databases/", "main"])

    # --- mirrors ---
    mirror_paths = [p for p in ls_files("mirrors/*/index.html")
                    if re.fullmatch(r"mirrors/[^/]+/index\.html", p)]
    for p in sorted(mirror_paths):
        t = page_title(p)
        name = clean_name(t.split(" — ")[0]) if t else p.split("/")[1].title()
        sites.append([name, p[:-len("index.html")], "mirror"])

    # --- database websites ---
    dbweb_paths = [p for p in ls_files("db/*/website/index.html")
                   if re.fullmatch(r"db/[^/]+/website/index\.html", p)]
    for slug in sorted(DBWEB_EXTRA):
        dbweb_paths.append(f"db/{slug}/index.html")
    for p in dbweb_paths:
        slug = p.split("/")[1]
        t = page_title(p)
        name = clean_name(t, ["Database website"]) if t else names.get(slug, slug)
        sites.append([name, p[:-len("index.html")], "dbweb"])

    # --- file websites ---
    file_paths = [p for p in ls_files("db/*/records/*.html")
                  if re.fullmatch(r"db/[^/]+/records/[^/]+\.html", p)]
    for p in sorted(file_paths):
        slug = p.split("/")[1]
        t = page_title(p)
        if t and slug in names and t.endswith(" — " + names[slug]):
            name = clean_name(t[: -len(" — " + names[slug])])
        elif t:
            name = clean_name(t.split(" — ")[0])
        else:
            name = os.path.basename(p)[:-len(".html")]
        sites.append([name, p, "file"])

    # --- mix websites ---
    mix_paths = [p for p in ls_files("db/*/mixes/*/index.html")
                 if re.fullmatch(r"db/[^/]+/mixes/[^/]+/index\.html", p)]
    mix_paths += sorted(MIX_EXTRA)
    for p in sorted(set(mix_paths)):
        slug = p.split("/")[1]
        t = page_title(p)
        if t.startswith("Flagship Mix"):
            name = (names.get(slug, slug) + " — Flagship Mix") if slug in names \
                else clean_name(t.split(" — ")[0])
        elif t:
            name = clean_name(t.split(" — ")[0])
        else:
            name = "Flagship Mix — " + names.get(slug, slug)
        sites.append([name, p[:-len("index.html")], "mix"])

    # --- database pages (one per database) ---
    # NOTE: git's pathspec `*` crosses `/`, so "db/*/index.html" also
    # matches db/<slug>/website/index.html, mixes, etc. — filter by shape.
    dbpage_paths = [p for p in ls_files("db/*/index.html")
                    if re.fullmatch(r"db/[^/]+/index\.html", p)]
    seen_slugs = set()
    for p in dbpage_paths:
        slug = p.split("/")[1]
        if slug in DBPAGE_EXCLUDE:
            continue
        seen_slugs.add(slug)
        sites.append([names.get(slug) or clean_name(page_title(p), ["JAH Databases"])
                      or slug.replace("-", " ").title(), p[:-len("index.html")], "dbpage"])
    missing = [s for s in names if s not in seen_slugs]
    if missing:
        print(f"WARNING: {len(missing)} manifest slugs have no db page: "
              f"{missing[:10]}", file=sys.stderr)

    # --- dedupe by URL (first classification wins), then sort ---
    by_url = {}
    for name, url, kind in sites:
        by_url.setdefault(url, [name, url, kind])
    sites = sorted(by_url.values(),
                   key=lambda s: (letter_of(s[0]), s[0].lower(), s[1]))

    counts = {}
    for _, _, kind in sites:
        counts[kind] = counts.get(kind, 0) + 1
    total = len(sites)
    # The user's date, never the VM's (the VM runs on UTC, a day ahead
    # of the user late at night).
    try:
        from zoneinfo import ZoneInfo
        today = datetime.now(ZoneInfo("America/New_York")).date().isoformat()
    except Exception:
        today = date.today().isoformat()

    data = {"generated": today, "total": total,
            "sites": [[n, u, k] for n, u, k in sites]}
    with open(os.path.join(ROOT, "all-websites.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, separators=(",", ":"))
    json_size = os.path.getsize(os.path.join(ROOT, "all-websites.json"))

    # --- the list page (search + kind filter + per-letter drop-downs) ---
    letters = []
    for name, _, _ in sites:
        L = letter_of(name)
        if L not in letters:
            letters.append(L)
    letters.sort(key=lambda L: (0, L) if len(L) == 1 and "A" <= L <= "Z"
                 else ((1, "") if L == "0-9" else (2, "")))
    page = PAGE_TEMPLATE.replace("__TOTAL__", f"{total:,}") \
        .replace("__DATE__", today) \
        .replace("__LETTERS__", json.dumps(letters))
    with open(os.path.join(ROOT, "all-websites.html"), "w", encoding="utf-8") as f:
        f.write(page)

    # --- plain static list (no JavaScript needed) ---
    groups = {}
    for name, url, kind in sites:
        groups.setdefault(letter_of(name), []).append((name, url, kind))
    parts = [ACC_HEAD.replace("__TOTAL__", f"{total:,}").replace("__DATE__", today)]
    for L in letters:
        items = groups[L]
        parts.append(f'  <details>\n    <summary>{html.escape(L)}</summary>\n    <ul>\n')
        for name, url, kind in items:
            parts.append(f'      <li><a href="{html.escape(url, quote=True)}">'
                         f'{html.escape(name)}</a> '
                         f'<span class="kind">{KINDS[kind]}</span></li>\n')
        parts.append('    </ul>\n  </details>\n')
    parts.append(ACC_TAIL)
    with open(os.path.join(ROOT, "accessible", "all-websites.html"),
              "w", encoding="utf-8") as f:
        f.write("".join(parts))
    acc_size = os.path.getsize(os.path.join(ROOT, "accessible", "all-websites.html"))

    print(f"STATUS: {total:,} websites total "
          f"(main+hub, mirrors {counts.get('mirror', 0)}, "
          f"database websites {counts.get('dbweb', 0)}, "
          f"file websites {counts.get('file', 0)}, "
          f"mix websites {counts.get('mix', 0)}, "
          f"database pages {counts.get('dbpage', 0)})")
    print(f"all-websites.json: {json_size:,} bytes; "
          f"accessible/all-websites.html: {acc_size:,} bytes")
    return 0


PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>All Websites — The 'Merica-L Internet</title>
<meta name="description" content="Every website in The 'Merica-L Internet — __TOTAL__ websites, one list. Main sites, mirrors, database websites, file websites, mix websites, and database pages.">
<style>
:root{--bg:#060a14;--panel:#0d1526;--line:#1d2c4d;--ink:#e8f1ff;--dim:#9fb3d8;--acc:#2f7bff;--ok:#00e5a0}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font-family:Arial,Helvetica,sans-serif;line-height:1.5}
.wrap{max-width:1100px;margin:0 auto;padding:16px}
.hero{background:linear-gradient(135deg,#0b1e3a 0%,#101a30 60%,#0a1428 100%);border:1px solid var(--line);border-radius:16px;padding:28px 22px;text-align:center;margin-bottom:14px}
.hero h1{margin:0;font-size:2em;letter-spacing:2px}
.hero p{color:var(--dim);max-width:640px;margin:10px auto}
.bigstat{background:rgba(13,21,38,.8);border:1px solid var(--line);border-radius:12px;padding:10px 18px;display:inline-block;margin-top:8px}
.bigstat b{font-size:1.6em;color:var(--ok);display:block}
.searchrow{display:flex;gap:8px;margin:14px 0}
.searchrow input{flex:1;font-size:1em;border-radius:10px;border:1px solid var(--line);background:#0a1120;color:var(--ink);padding:11px 12px}
.kinds{display:flex;gap:8px;flex-wrap:wrap;margin:0 0 6px}
.kindbtn{font-size:.85em;border-radius:20px;border:1px solid var(--line);background:#0a1120;color:var(--dim);padding:6px 14px;cursor:pointer}
.kindbtn.on{border-color:var(--ok);color:var(--ok);font-weight:bold}
.hint{font-size:.85em;color:var(--dim)}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:12px}
#grid details{grid-column:1/-1}
#grid details summary{cursor:pointer;font-weight:700;padding:10px 12px;background:var(--panel);border:1px solid var(--line);border-radius:12px;font-size:1.2em}
#grid details summary:hover{border-color:var(--acc)}
.letter-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:12px;margin-top:12px}
.card{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:12px;text-decoration:none;color:var(--ink);display:block}
.card:hover{border-color:var(--acc)}
.card h3{margin:0 0 4px;font-size:1em}
.card .k{font-size:.75em;color:var(--ok)}
.foot{margin-top:26px;padding-top:12px;border-top:1px solid var(--line);color:var(--dim);font-size:.85em;text-align:center}
.foot a{color:var(--acc)}
</style>
</head>
<body>
<div class="wrap">
  <div class="hero">
    <h1>ALL WEBSITES</h1>
    <p>Every website in The 'Merica-L Internet — main sites, mirrors, database websites, file websites, mix websites, and database pages. Each one is free to visit and free to use.</p>
    <div class="bigstat"><b id="total">__TOTAL__</b>websites</div>
    <p class="hint">List generated __DATE__ from the live files on this site. <a href="accessible/all-websites.html" style="color:var(--acc)">Plain list (no JavaScript needed)</a></p>
  </div>
  <div class="searchrow">
    <input id="q" placeholder="Search all websites by name…" aria-label="Search all websites">
  </div>
  <div class="kinds" id="kinds">
    <button class="kindbtn on" data-kind="">All kinds</button>
    <button class="kindbtn" data-kind="main">Main sites</button>
    <button class="kindbtn" data-kind="mirror">Mirrors</button>
    <button class="kindbtn" data-kind="dbweb">Database websites</button>
    <button class="kindbtn" data-kind="file">File websites</button>
    <button class="kindbtn" data-kind="mix">Mix websites</button>
    <button class="kindbtn" data-kind="dbpage">Database pages</button>
  </div>
  <p class="hint" id="status">Loading the full list…</p>
  <div class="grid" id="grid"></div>
  <div class="foot">
    <a href="https://justinahiggins614-cmyk.github.io/jah-databases/">JAH Databases — the database hub</a> ·
    <a href="the-merica-l-boundless-ecosystem-os.html">The 'Merica-L Boundless Ecosystem OS</a> ·
    <a href="the-merica-l-virtual-internet.html">The 'Merica-L Virtual Internet</a> ·
    <a href="command-center.html">Command Center</a><br>
    ✳ The 'Merica-L Internet. Everything free forever.
  </div>
</div>
<script>
(function(){
'use strict';
var KIND_LABELS = {"main":"Main site","mirror":"Mirror","dbweb":"Database website","file":"File website","mix":"Mix website","dbpage":"Database page"};
var LETTERS = __LETTERS__;
var sites = null, kindFilter = '', grid = document.getElementById('grid'),
    statusEl = document.getElementById('status'),
    qEl = document.getElementById('q');
function esc(s){ return String(s==null?'':s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;'); }
function letterOf(name){
  var s = String(name||'').replace(/^["'\\u201c\\u201d\\u2018\\u2019\\(\\[{]+/,'');
  for(var i=0;i<s.length;i++){ var c=s[i]; if(/[A-Za-z]/.test(c)) return c.toUpperCase(); if(/[0-9]/.test(c)) return '0-9'; }
  return '#';
}
function cardFor(s){
  var a=document.createElement('a');
  a.className='card'; a.href=s[1];
  a.innerHTML='<h3>'+esc(s[0])+'</h3><div class="k">'+esc(KIND_LABELS[s[2]]||s[2])+'</div>';
  return a;
}
function matchKind(s){ return !kindFilter || s[2]===kindFilter; }
function render(){
  grid.innerHTML='';
  var q=qEl.value.trim().toLowerCase();
  if(q){
    var hits=[], total=0;
    for(var i=0;i<sites.length;i++){
      var s=sites[i];
      if(!matchKind(s)) continue;
      if(s[0].toLowerCase().indexOf(q)<0) continue;
      total++;
      if(hits.length<300) hits.push(s);
    }
    statusEl.textContent = total ? ('Found '+total.toLocaleString()+' matching website'+(total===1?'':'s')+(total>300?' — showing the first 300':'')+'.') : 'No website matches that search.';
    var body=document.createElement('div'); body.className='letter-grid'; body.style.gridColumn='1/-1';
    hits.forEach(function(s){ body.appendChild(cardFor(s)); });
    grid.appendChild(body);
    return;
  }
  statusEl.textContent='Browse by first letter — tap a letter to open its websites. Or type in the search box above.';
  var groups={};
  sites.forEach(function(s){ if(!matchKind(s)) return; var L=letterOf(s[0]); (groups[L]=groups[L]||[]).push(s); });
  LETTERS.forEach(function(L){
    var list=groups[L]; if(!list) return;
    var det=document.createElement('details');
    var sum=document.createElement('summary'); sum.textContent=L;
    var body=document.createElement('div'); body.className='letter-grid';
    det.appendChild(sum); det.appendChild(body);
    det.addEventListener('toggle',function(){
      if(!det.open || det.dataset.loaded) return;
      det.dataset.loaded='1';
      list.forEach(function(s){ body.appendChild(cardFor(s)); });
    });
    grid.appendChild(det);
  });
}
fetch('all-websites.json').then(function(r){return r.json();}).then(function(d){
  sites=d.sites||[];
  var t=document.getElementById('total');
  if(d.total) t.textContent=Number(d.total).toLocaleString();
  render();
}).catch(function(e){
  statusEl.textContent='The website list failed to load: '+e.message+'. Try the plain list link above.';
});
qEl.addEventListener('input',function(){ if(sites) render(); });
document.getElementById('kinds').addEventListener('click',function(e){
  var b=e.target.closest ? e.target.closest('.kindbtn') : null;
  if(!b) return;
  kindFilter=b.getAttribute('data-kind')||'';
  var btns=document.querySelectorAll('.kindbtn');
  for(var i=0;i<btns.length;i++) btns[i].classList.remove('on');
  b.classList.add('on');
  if(sites) render();
});
})();
</script>
</body>
</html>
"""

ACC_HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>All Websites (plain list) — The 'Merica-L Internet</title>
</head>
<body>
<h1>All Websites — The 'Merica-L Internet</h1>
<p>Every website in the network — __TOTAL__ websites, one list. Main sites, mirrors, database websites, file websites, mix websites, and database pages. Plain list, no JavaScript needed. Generated __DATE__.</p>
<p><a href="../all-websites.html">Searchable list (with search box)</a> · <a href="../">JAH Databases — the database hub</a> · <a href="../the-merica-l-boundless-ecosystem-os.html">The 'Merica-L Boundless Ecosystem OS</a></p>
"""

ACC_TAIL = """<p>Everything free forever. The 'Merica-L Internet.</p>
</body>
</html>
"""

if __name__ == "__main__":
    sys.exit(main())
