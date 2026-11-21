#!/usr/bin/env python3
"""Assemble the uniting Internets page from the seven-groups fragments.

Placed in the repo at merge time (2026-11-21) from the staging builder in
~/workspace/hidden_files/seven-website-groups/assembled/. It is NOT wired
into the hourly job (that freshness decision is still open) -- run it by
hand after code/build_all_websites.py, which it reads for the whole-network
total. Run order: build_all_websites.py first (it counts the group pages),
then this builder (it stamps the total the directory just confirmed).

Sources: pilot/*/internets-fragment.html (3) + core/wave-*/**/internets-fragment.html (60),
read from the staging tree (FRAGMENTS, default below).
Outputs (repo root):
  seven-groups.html            main page (DESIGN §7)
  seven-groups.json            search/lazy-load index, generated alongside
  accessible/seven-groups.html plain mirror, no JS

DESIGN §7 (binding) as applied:
- Seven collapsed <details>, one per group, closed by default, group order 1-7.
  Each lists its subjects alphabetically: subject name + link.
- Group 1 entries link to the subject HOME (groups/<key>/) per DESIGN §7's
  parenthetical ("or to the subject home for Group 1"). The fragment's own
  Group 1 link (the full website) is kept in seven-groups.json as
  "full_website" so the record is not lost; one-line change flips Group 1
  to the direct link if Manon overrules.
- Counts rule: ONLY the whole-network total (re-derived from
  all-websites.json at each run). No record counts anywhere on the page or
  in the JSON. Fragments' record counts are NOT carried over (that also keeps
  known stale fragment counts off the page: word-processors 25 vs live 1,988;
  password-generators 20 vs live 1,803).
- Search: client-side filter over seven-groups.json, filters as you type.
- Lazy: group entries are injected from the JSON when a group is first
  opened; only opened groups are in the DOM.
- F1 re-key applied at assembly: pilot spell-check links
  services/spell-check-g<N>-*/ -> groups/service-spell-check/g<N>-*/.
  Coffee was CORRECTED at merge time (2026-11-21): its fragment's flat
  services/coffee/<group>/ paths were re-pointed to the fixed scheme
  (Group 1 services/coffee/, Groups 2-7 groups/coffee/g<N>-*/) before
  assembly, so the fragment on disk now carries the corrected paths.
- Fragments are read verbatim; nothing in any wave folder is edited.
"""
import html
import json
import re
import sys
from datetime import date, datetime
from pathlib import Path

BASE = "https://justinahiggins614-cmyk.github.io/jah-databases"
# The fragments live in the staging tree, not in this repo.
FRAGMENTS = Path.home() / "workspace/hidden_files/seven-website-groups"
ROOT = FRAGMENTS  # fragment tree root (was __file__'s parent in staging)
REPO = Path(__file__).resolve().parent.parent  # jah-databases/
OUT = REPO


def derived_totals():
    """Whole-network total from the directory builder's output (run
    code/build_all_websites.py first), today's date in the user's timezone,
    and the live database count from the manifest. Nothing is hardcoded:
    a stale total here would re-stamp every group page wrong."""
    directory = json.loads((REPO / "all-websites.json").read_text())
    total = int(directory["total"])
    manifest = json.loads((REPO / "data/manifest.json").read_text())
    db_total = len(manifest["databases"])
    try:
        from zoneinfo import ZoneInfo
        today = datetime.now(ZoneInfo("America/New_York")).date().isoformat()
    except Exception:
        today = date.today().isoformat()
    return f"{total:,}", total, today, f"{db_total:,}"

# Pilot order first, then waves 1-13 in order, alphabetical within a wave.
PILOT_ORDER = ["spell-check", "r-programming", "coffee"]
REKEY = {"spell-check": "service-spell-check"}


def fragment_paths():
    paths = []
    for key in PILOT_ORDER:
        p = ROOT / "pilot" / key / "internets-fragment.html"
        assert p.exists(), f"missing pilot fragment {p}"
        paths.append((f"pilot/{key}", p))
    for wave in range(1, 14):
        wdir = ROOT / "core" / f"wave-{wave}"
        found = sorted(wdir.rglob("internets-fragment.html"))
        for p in found:
            # key = subject folder name (parent dir of the fragment)
            paths.append((f"wave-{wave}/{p.parent.name}", p))
    return paths


def parse_fragment(path):
    text = path.read_text(encoding="utf-8")
    m = re.search(r"<h[23][^>]*>(.*?)</h[23]>", text, re.S)
    assert m, f"{path}: no heading"
    name = html.unescape(re.sub(r"<[^>]+>", "", m.group(1)).strip())
    name = re.sub(r"\s+— all seven website groups$", "", name)
    name = re.sub(r"\s+", " ", name)
    # Group links may live in a <ul> or an <ol> (wave-12 uses <ol>; the
    # databases list is a separate <ul>). Classify every <li> in the
    # fragment: only group items match a group marker or the "Group 1" label.
    items = re.findall(r"<li>(.*?)</li>", text, re.S)
    if not items:
        items = [p for p in re.split(r"<li>", text) if p.strip()]
    groups = {}
    for item in items:
        hrefs = re.findall(r'href="([^"]+)"', item)
        if not hrefs:
            continue
        href = hrefs[0]
        plain = re.sub(r"<[^>]+>", "", item).strip()
        for n, marker in ((7, "g7-v2"), (6, "g6-signature"), (5, "g5-data"),
                          (4, "g4-generator"), (3, "g3-ai"), (2, "g2-static")):
            if marker in href:
                assert n not in groups, f"{path}: two group-{n} links"
                groups[n] = href
                break
        else:
            # Group 1: the li labeled Group 1. If two are labeled so (wave-4
            # mirrors list both the live mirror and a groups/.../g1 path),
            # prefer the one that is NOT under /groups/ (the real full site).
            if plain.startswith("Group 1"):
                if 1 not in groups or "/groups/" not in href:
                    groups[1] = href
    assert sorted(groups) == [1, 2, 3, 4, 5, 6, 7], \
        f"{path}: groups found {sorted(groups)}"
    return name, [groups[i] for i in range(1, 8)]


def absolutize(href):
    if href.startswith("http"):
        return href
    return BASE + "/" + href.lstrip("/")


def main():
    TOTAL, TOTAL_INT, DATE, DB_TOTAL = derived_totals()
    paths = fragment_paths()
    assert len(paths) == 63, f"expected 63 fragments, got {len(paths)}"
    subjects = []
    seen_keys, seen_names = set(), set()
    for label, path in paths:
        key = path.parent.name
        key = REKEY.get(key, key)
        name, hrefs = parse_fragment(path)
        assert key not in seen_keys, f"duplicate key {key}"
        assert name not in seen_names, f"duplicate name {name}"
        seen_keys.add(key)
        seen_names.add(name)
        # spell-check re-key on its group links (g2-g7); g1 stays the full site
        links = []
        for i, h in enumerate(hrefs):
            url = absolutize(h)
            if path.parent.name == "spell-check" and i > 0:
                url = url.replace("/services/spell-check-g", "/groups/service-spell-check/g")
            links.append(url)
        home = f"{BASE}/groups/{key}/"
        subjects.append({
            "name": name,
            "key": key,
            "home": home,
            "full_website": links[0],
            "groups": [home] + links[1:],
        })
    subjects.sort(key=lambda s: s["name"].lower())

    data = {
        "generated": f"{DATE}, America/New_York",
        "source": "pilot + core waves 1-13 internets fragments (63 subjects)",
        "whole_network_total": TOTAL_INT,
        "subjects": subjects,
    }
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "seven-groups.json").write_text(
        json.dumps(data, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")

    group_blurbs = [
        ("Group 1 — The full website, with everything",
         "The subject's main website: the working tool or service, how it works, the records, the files — and a wiki section that gathers all of the subject's data from all seven groups, with every link."),
        ("Group 2 — The links list (static)",
         "A website that is solely a links list: every site, database and file for the subject, on one plain page. No JavaScript."),
        ("Group 3 — The AI only",
         "A website that is only the AI for the subject system — it answers from the subject's own records. The online fact-checking path is labeled honestly: it is blocked until the network's own key service is connected, and nobody is ever asked for a key."),
        ("Group 4 — The generator alone",
         "A website that is only the generator for the subject: it makes new records, deterministically, on the page."),
        ("Group 5 — The data alone",
         "The subject's public data alone, in plain readable words, no JavaScript — so public bodies, schools and libraries can use it."),
        ("Group 6 — The Signature data",
         "All Signature-created data on the subject, labeled Signature throughout — never presented as public record."),
        ("Group 7 — Version 2: advanced, creative, themed",
         "The second version of the subject's website: advanced and creative and themed, with images and tools and fun stuff — the whole world, with product lines. Free, as always."),
    ]

    style = """body{font-family:Georgia,serif;background:#fdfcf7;color:#222;margin:0;padding:0}
header{background:#1d3a2f;color:#fdfcf7;padding:28px 20px}
header h1{margin:0;font-size:28px}
header p{margin:8px 0 0;max-width:720px}
header a{color:#ffe9a8}
main{max-width:860px;margin:0 auto;padding:20px}
h2{border-bottom:2px solid #1d3a2f;padding-bottom:6px}
details{border:1px solid #d8d2c0;border-radius:6px;margin:10px 0;padding:10px 14px;background:#fff}
summary{cursor:pointer;font-weight:bold}
ul{line-height:1.7}
a{color:#1d5a3a}
input[type=search]{width:100%;padding:10px;font-size:16px;border:1px solid #999;border-radius:6px;box-sizing:border-box}
.note{background:#f4efe0;border-left:4px solid #b98a1d;padding:10px 14px;margin:16px 0}
footer{border-top:1px solid #d8d2c0;margin-top:30px;padding:16px 20px;font-size:14px}"""

    header_groups = "\n".join(
        f"<li><b>{html.escape(t)}</b> — {html.escape(d)}</li>" for t, d in group_blurbs)

    def group_details(idx):
        t, d = group_blurbs[idx]
        return (f'<details id="group-{idx + 1}"><summary>{html.escape(t)}</summary>\n'
                f"<p>{html.escape(d)}</p>\n"
                f'<ul data-group="{idx + 1}"></ul>\n</details>')

    main_page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>The Seven Groups — one Internets website uniting all seven lists</title>
<style>
{style}
</style>
</head>
<body>
<header>
<h1>The Seven Groups</h1>
<p>Every subject gets seven websites — one of each kind, built together, equally. All free forever, no sign-in, no payment.</p>
<ul>
{header_groups}
</ul>
<p>{TOTAL} websites total in The 'Merica-L Internet. This page unites all the built subjects — the three pilot subjects and the sixty core subjects, all seven groups each. More subjects join wave by wave. Nothing is listed here until it is built.</p>
<p>List generated {DATE}, America/New_York, from the live files (pilot + core waves 1–13 fragments, 63 subjects; live manifest {DB_TOTAL} databases).</p>
</header>
<main>
<p><label for="q">Find a subject:</label><br>
<input type="search" id="q" placeholder="Type to filter the lists below…" autocomplete="off"></p>
<noscript><p><b>This page needs JavaScript for the lists.</b> The plain version lists everything with no JavaScript: <a href="accessible/seven-groups.html">Plain accessible version of this page</a>.</p></noscript>

<h2>The seven groups</h2>
<p>Open a group to see its subjects. Only the opened group's entries are loaded — the lists stay fast.</p>
{chr(10).join(group_details(i) for i in range(7))}

<div class="note"><b>How it grows.</b> The pilot was three subjects. The core build added sixty more — all seven groups each, verified. The grander list is every database subject in the network. Nothing is listed here until it is built.</div>
<p><a href="accessible/seven-groups.html">Plain accessible version of this page (no JavaScript)</a></p>
</main>
<footer>
<p><a href="the-merica-l-boundless-ecosystem-os.html">The 'Merica-L Boundless Ecosystem OS</a> · <a href="the-merica-l-virtual-internet.html">The 'Merica-L Virtual Internet</a> · <a href="all-websites.html">All websites</a> · <a href="./">Database hub</a></p>
<p>The network holds {TOTAL} websites in total (re-derived {DATE} from the live manifest and directory).</p>
<p>JAH Databases. Public records organized in the Signature system. All free forever — no sign-in, no payment.</p>
</footer>
<script>
var DATA = null;
function esc(s){{ return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;'); }}
function renderGroup(n, filter) {{
  var ul = document.querySelector('ul[data-group="' + n + '"]');
  var items = DATA.subjects.filter(function(s) {{
    return !filter || s.name.toLowerCase().indexOf(filter) !== -1;
  }});
  ul.innerHTML = items.map(function(s) {{
    return '<li><a href="' + esc(s.groups[n-1]) + '">' + esc(s.name) + '</a></li>';
  }}).join('\\n') || '<li>No subjects match.</li>';
  ul.setAttribute('data-loaded', filter ? 'search' : 'all');
}}
function loadGroups(filter) {{
  for (var n = 1; n <= 7; n++) {{
    var d = document.getElementById('group-' + n);
    if (filter) {{ renderGroup(n, filter); d.open = true; }}
  }}
}}
fetch('seven-groups.json').then(function(r){{ return r.json(); }}).then(function(j) {{
  DATA = j;
  for (var n = 1; n <= 7; n++) {{
    (function(n) {{
      var d = document.getElementById('group-' + n);
      d.addEventListener('toggle', function() {{
        if (d.open) {{
          var ul = d.querySelector('ul');
          if (!ul.getAttribute('data-loaded')) renderGroup(n, '');
        }}
      }});
    }})(n);
  }}
  document.getElementById('q').addEventListener('input', function(e) {{
    var q = e.target.value.trim().toLowerCase();
    if (!q) {{
      for (var n = 1; n <= 7; n++) {{
        var d = document.getElementById('group-' + n);
        d.open = false;
        var ul = d.querySelector('ul');
        ul.innerHTML = '';
        ul.removeAttribute('data-loaded');
      }}
      return;
    }}
    loadGroups(q);
  }});
}});
</script>
</body>
</html>
"""
    (OUT / "seven-groups.html").write_text(main_page, encoding="utf-8")

    # Accessible mirror: plain, no JS, all seven groups fully listed, collapsed.
    acc_groups = []
    for idx, (t, d) in enumerate(group_blurbs):
        lis = "\n".join(
            f'<li><a href="{html.escape(s["groups"][idx])}">{html.escape(s["name"])}</a></li>'
            for s in subjects)
        acc_groups.append(
            f'<details><summary>{html.escape(t)}</summary>\n<p>{html.escape(d)}</p>\n<ul>\n{lis}\n</ul>\n</details>')
    acc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>The Seven Groups — one Internets website uniting all seven lists (plain version)</title>
</head>
<body>
<h1>The Seven Groups</h1>
<p>Every subject gets seven websites — one of each kind, built together, equally. All free forever, no sign-in, no payment.</p>
<ul>
{header_groups}
</ul>
<p>{TOTAL} websites total in The 'Merica-L Internet. This page unites all the built subjects — the three pilot subjects and the sixty core subjects, all seven groups each. More subjects join wave by wave. Nothing is listed here until it is built.</p>
<p>List generated {DATE}, America/New_York, from the live files (pilot + core waves 1–13 fragments, 63 subjects; live manifest {DB_TOTAL} databases).</p>
<p>This is the plain version of the page. It has no JavaScript. <a href="../seven-groups.html">The main version of this page</a>.</p>

<h2>The seven groups</h2>
{chr(10).join(acc_groups)}

<p><b>How it grows.</b> The pilot was three subjects. The core build added sixty more — all seven groups each, verified. The grander list is every database subject in the network. Nothing is listed here until it is built.</p>

<p><a href="the-merica-l-boundless-ecosystem-os.html">The 'Merica-L Boundless Ecosystem OS</a> · <a href="the-merica-l-virtual-internet.html">The 'Merica-L Virtual Internet</a> · <a href="all-websites.html">All websites</a> · <a href="../">Database hub</a></p>
<p>The network holds {TOTAL} websites in total (re-derived {DATE} from the live manifest and directory).</p>
<p>JAH Databases. Public records organized in the Signature system. All free forever — no sign-in, no payment.</p>
</body>
</html>
"""
    acc_dir = OUT / "accessible"
    acc_dir.mkdir(parents=True, exist_ok=True)
    (acc_dir / "seven-groups.html").write_text(acc, encoding="utf-8")

    print(f"subjects: {len(subjects)}")
    print(f"links per subject: 7 (home + g2-g7 from fragments; g1 full_website kept in JSON)")
    print(f"total links on page: {len(subjects) * 7}")
    print("wrote:", sorted(str(p.relative_to(REPO)) for p in
          [OUT / "seven-groups.json", OUT / "seven-groups.html", acc_dir / "seven-groups.html"]))


if __name__ == "__main__":
    main()
