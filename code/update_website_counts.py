#!/usr/bin/env python3
"""Hourly website-count updater for the 'Merica-L Boundless Ecosystem OS page.

Counts (from TRACKED files only, so the number matches what is deployed):
  main sites     = <li> items in the sites list on the main OS page
                   (the list is unnumbered; its size is NEVER printed as
                   its own count anywhere — it only feeds the network total)
  per-artifact   = DB websites + file websites + mix websites (main pages only):
    DB    = db/*/website/index.html
    files = db/*/records/*.html, excluding /accessible/ and /mirror/
    mixes = db/*/mixes/*/index.html, excluding /accessible/ and /mirror/
          + db/marijuana-supplies-set/index.html
          + db/marijuana-supplies-set/complete-grinder-system/index.html
          (Wave 1 set master + grinder mix)
  mirrors        = mirrors/<slug>/index.html (main pages only — filtered by
                   path shape, since git's pathspec `*` crosses `/` and the
                   bare glob would also match /accessible/ and /mirror/ pages)
  database pages = db/<slug>/index.html (main pages only, shape-filtered),
                   excluding the Wave 1 set page counted above
                   (marijuana-supplies-set)
  group websites = the Seven Website Groups pages, same definition as
                   code/build_all_websites.py (the All websites directory
                   builder — the two formulas must agree):
                     groups/<key>/g[2-7]-*/index.html (6 per subject)
                   + seven-groups.html (the uniting Internets page)
                   + services/coffee/index.html (coffee Group 1 site)
                   Subject homes (groups/<key>/index.html) are NOT counted.
  service sites  = services/<slug>/index.html (main pages only,
                   shape-filtered), excluding services/coffee/index.html,
                   which is counted as a group website above, never twice.
  combo websites = the Combo Router (combos/index.html, a service
                   website) + each stored combo page
                   (combos/<slug>/index.html, a file website).
                   On-demand combos have no stored page and are never
                   counted; the Router's accessible mirror
                   (combos/accessible/index.html) is not a website.
                   Same definition as code/build_all_websites.py —
                   the two formulas must agree.
  hub            = 1 (the database hub itself, JAH Databases)

  TOTAL = main sites + per-artifact + mirrors + database pages
          + group websites + service sites + combo websites + hub.
  Only the TOTAL is ever printed, committed, or stamped anywhere: no
  per-kind counts appear in any output, message, or page.
  The TOTAL is the one website count shown anywhere; it is also the
  total on the All websites list page (all-websites.html), which the
  OS page and the front door link to.

Re-stamps the OS pages (main + accessible mirror) and the 'Merica-L
Virtual Internet front-door pages (main + accessible mirror):
  - hero: "browse all {TOTAL} websites in the network — the full list
    is on the All websites page"
  - stats tile: "Websites + hub" number -> {TOTAL}, with today's count date
  - numbers-table Websites row -> "{TOTAL}, including the database hub"
  - per-artifact count line: "Per-artifact websites live so far: {N}."
  - front door: "{TOTAL} websites", counted today, with the All websites
    link; the "Counts:" notes; "not counted as a website in that {TOTAL}"

Safety: pulls --ff-only first; skips the run if the working tree has ANY
uncommitted changes (another agent's work in progress); commits + pushes
(main + gh-pages) only when the stamped numbers actually changed; never
stamps a LOWER per-artifact count or a LOWER total than the one already
on the page (a drop means a counting error, not progress). Prints one
STATUS line.
"""
import datetime
import os
import re
import subprocess
import sys

try:
    from zoneinfo import ZoneInfo
    USER_TZ = ZoneInfo("America/Los_Angeles")
except Exception:
    USER_TZ = datetime.timezone(datetime.timedelta(hours=-8))


def today_user():
    """Today's date on the user's clock (America/Los_Angeles), never the VM's."""
    return datetime.datetime.now(USER_TZ).date().isoformat()

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAIN = os.path.join(ROOT, "the-merica-l-boundless-ecosystem-os.html")
MIRROR = os.path.join(ROOT, "accessible", "the-merica-l-boundless-ecosystem-os.html")
FRONT_MAIN = os.path.join(ROOT, "the-merica-l-virtual-internet.html")
FRONT_ACC = os.path.join(ROOT, "accessible", "the-merica-l-virtual-internet.html")

# Wave 1 set page counted as a per-artifact website, never as a database page.
# (The two marijuana database websites moved to db/<slug>/website/ at the
# 2026-11-22 Batch G merge, so they are counted by the general db/*/website/
# pattern now; their hub catalog pages at db/<slug>/index.html count as
# database pages.)
DBPAGE_EXCLUDE = {"marijuana-supplies-set"}


def run(cmd, check=True):
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    if check and r.returncode != 0:
        raise RuntimeError(f"{' '.join(cmd)} failed: {r.stderr.strip()}")
    return r


def ls_files(*patterns):
    out = run(["git", "ls-files"] + list(patterns)).stdout.splitlines()
    return [p for p in out if p]


def count_main_sites():
    html = open(MAIN, encoding="utf-8").read()
    m = re.search(r'<ul class="sites">(.*?)</ul>', html, re.S)
    if not m:
        m = re.search(r'<ol class="sites">(.*?)</ol>', html, re.S)
    if not m:
        raise RuntimeError("no sites list on main OS page")
    return m.group(1).count("<li")


def count_per_artifact():
    db = [p for p in ls_files("db/*/website/index.html")
          if re.fullmatch(r"db/[^/]+/website/index\.html", p)]
    files = [p for p in ls_files("db/*/records/*.html")
             if re.fullmatch(r"db/[^/]+/records/[^/]+\.html", p)]
    mixes = [p for p in ls_files("db/*/mixes/*/index.html")
             if re.fullmatch(r"db/[^/]+/mixes/[^/]+/index\.html", p)]
    mixes += ls_files("db/marijuana-supplies-set/index.html",
                      "db/marijuana-supplies-set/complete-grinder-system/index.html")
    return len(db), len(files), len(mixes), len(db) + len(files) + len(mixes)


def count_mirrors():
    # Main pages only: exactly mirrors/<slug>/index.html. NOTE: git's
    # pathspec `*` crosses `/`, so "mirrors/*/index.html" ALSO matches
    # mirrors/<slug>/accessible/index.html and mirrors/<slug>/mirror/
    # index.html — filter by shape instead of trusting the glob.
    return len([p for p in ls_files("mirrors/*/index.html")
                if re.fullmatch(r"mirrors/[^/]+/index\.html", p)])


def count_dbpages():
    pages = [p for p in ls_files("db/*/index.html")
             if re.fullmatch(r"db/[^/]+/index\.html", p)]
    return len([p for p in pages if p.split("/")[1] not in DBPAGE_EXCLUDE])


def count_groups():
    # Same definition as code/build_all_websites.py: the 6 group pages
    # per subject (g2..g7), plus the uniting Internets page and the
    # coffee Group 1 site. Subject homes (groups/<key>/index.html)
    # are NOT websites in this count. The two extra pages count only
    # when tracked (both are live and tracked today).
    group = [p for p in ls_files("groups/*/g*/index.html")
             if re.fullmatch(r"groups/[^/]+/g[2-7]-[a-z0-9-]+/index\.html", p)]
    extra = [p for p in ("seven-groups.html", "services/coffee/index.html")
             if p in ls_files(p)]
    return len(group) + len(extra)


def count_services():
    # Same definition as code/build_all_websites.py: every service site's
    # main page, except coffee, which is a group website (counted in
    # count_groups). The accessible mirrors (services/<slug>/accessible/)
    # are NOT websites in this count.
    paths = [p for p in ls_files("services/*/index.html")
             if re.fullmatch(r"services/[^/]+/index\.html", p)]
    return len([p for p in paths if p != "services/coffee/index.html"])


def count_combos():
    # Same definition as code/build_all_websites.py: the Combo Router
    # (combos/index.html, counted as a service website) plus each stored
    # combo page (combos/<slug>/index.html, counted as a file website).
    # The Router's accessible mirror (combos/accessible/index.html) is
    # NOT a website, and on-demand combos have no stored page and are
    # never counted.
    n = 1 if "combos/index.html" in ls_files("combos/index.html") else 0
    stored = [p for p in ls_files("combos/*/index.html")
              if re.fullmatch(r"combos/[^/]+/index\.html", p)
              and p != "combos/accessible/index.html"]
    return n + len(stored)


def hero_text(total, prefix=""):
    return (f"browse all {total:,} websites in the network — the full list is on the "
            f"<a href=\"{prefix}all-websites.html\">All websites</a> page")


def stamp(path, total, n_art, prefix=""):
    text = open(path, encoding="utf-8").read()
    orig = text
    today = today_user()
    # Hero clause, new phrasing (either link prefix) — stamp the total.
    def _hero(m):
        return hero_text(total, m.group(1) or "")
    text = re.sub(
        r"browse all [\d,]+ websites in the network — the full list is on the "
        r"<a href=\"(\.\./)?all-websites\.html\">All websites</a> page",
        _hero, text)
    # Hero clause, OLD phrasing (pre-2026-11-19) — convert to the new one.
    text = re.sub(
        r"browse its (?:\d+ websites(?:, [\d,]+ per-artifact websites, and \d+ mirror websites| and [\d,]+ per-artifact websites)?|\d+ (?:main sites|original websites)(?: and [\d,]+ per-artifact websites)?)",
        lambda m: hero_text(total, prefix), text)
    # Per-artifact count line (main page <li>, mirror <p> — same sentence).
    text = re.sub(
        r"Per-artifact websites live so far: [\d,]+\.",
        f"Per-artifact websites live so far: {n_art:,}.", text)
    # Stats tile: total websites, hub included in the total now.
    text = re.sub(
        r'<div class="stat"><div class="n">[\d,]+</div><div class="l">Websites \+ hub</div>'
        r'<div class="s">counted [\d-]+</div></div>',
        f'<div class="stat"><div class="n">{total:,}</div><div class="l">Websites + hub</div>'
        f'<div class="s">counted {today}</div></div>',
        text)
    # Numbers-table Websites row (mirror: plain <td>; main page: <td class="num">).
    def _web_row(m):
        cls = m.group(1) or ""
        return (f'<tr><td>Websites</td><td{cls}>{total:,}, including the database hub</td>'
                f'<td>{today}</td></tr>')
    text = re.sub(
        r'<tr><td>Websites</td><td( class="num")?>[\d,]+(?:, plus the database hub|, including the database hub)</td>'
        r'<td>[\d-]+</td></tr>',
        _web_row, text)
    if text != orig:
        open(path, "w", encoding="utf-8").write(text)
    return text != orig


def front_hero(total, today, prefix=""):
    return (f"<b>{total:,} websites</b>, counted {today} — the full list is on the "
            f"<a href=\"{prefix}all-websites.html\">All websites</a> page. "
            f"This front door page itself is not counted as a website in that {total:,}.")


def stamp_front_door(path, total, prefix=""):
    """Re-stamp the website-count phrases on a virtual-internet front-door
    page (main or accessible). Only the website-count sentences are touched:
    the database-hub count is never rewritten here. The front door itself
    is never counted."""
    text = open(path, encoding="utf-8").read()
    orig = text
    today = today_user()
    # Hero count phrase, new phrasing (either link prefix) — stamp total + date.
    def _hero(m):
        return front_hero(total, today, m.group(1) or "")
    text = re.sub(
        r"<b>[\d,]+ websites</b>, counted [\d-]+ — the full list is on the "
        r"<a href=\"(\.\./)?all-websites\.html\">All websites</a> page\. "
        r"This front door page itself is not counted as a website in that [\d,]+\.",
        _hero, text)
    # Hero count phrase, OLD phrasing (pre-2026-11-19) — convert to the new one.
    text = re.sub(
        r"<b>[\d,]+ websites — \d+ websites(?:, [\d,]+ per-artifact websites, and \d+ mirror websites| and [\d,]+ per-artifact websites)</b>, counted [\d-]+\. This front door page itself is not counted as a website in that [\d,]+\.",
        lambda m: front_hero(total, today, prefix), text)
    # "Counts:" notes — new phrasing (total + date; the tail is stamped below).
    text = re.sub(
        r"Counts: [\d,]+ websites — counted [\d-]+,",
        f"Counts: {total:,} websites — counted {today},", text)
    text = re.sub(
        r"Counts on this page: [\d,]+ websites — counted [\d-]+,",
        f"Counts on this page: {total:,} websites — counted {today},", text)
    # "Counts:" notes, OLD phrasing — convert to the new one.
    text = re.sub(
        r"Counts: [\d,]+ websites — \d+ websites(?:, [\d,]+ per-artifact websites, and \d+ mirror websites| and [\d,]+ per-artifact websites) — counted [\d-]+,",
        f"Counts: {total:,} websites — counted {today},", text)
    text = re.sub(
        r"Counts on this page: [\d,]+ websites — \d+ websites(?:, [\d,]+ per-artifact websites, and \d+ mirror websites| and [\d,]+ per-artifact websites) — counted [\d-]+,",
        f"Counts on this page: {total:,} websites — counted {today},", text)
    # "not counted as a website in that N" (hero, notes) — stamp the total.
    text = re.sub(
        r"not counted as a website in that [\d,]+",
        f"not counted as a website in that {total:,}", text)
    if text != orig:
        open(path, "w", encoding="utf-8").write(text)
    return text != orig


def main():
    try:
        run(["git", "pull", "--ff-only"])
    except RuntimeError as e:
        print(f"STATUS: skipped — pull failed: {e}")
        return 1
    # Only tracked-file changes block a run (another agent's in-progress
    # edits); untracked files (new build output, this script before its
    # first commit) do not.
    dirty = [l for l in run(["git", "status", "--porcelain"], check=False).stdout.splitlines()
             if not l.startswith("??")]
    if dirty:
        print("STATUS: skipped — working tree has uncommitted tracked changes")
        return 0
    m_sites = count_main_sites()
    n_db, n_files, n_mixes, n_art = count_per_artifact()
    n_mir = count_mirrors()
    n_dbpages = count_dbpages()
    n_grp = count_groups()
    n_svc = count_services()
    n_combos = count_combos()
    total = m_sites + n_art + n_mir + n_dbpages + n_grp + n_svc + n_combos + 1  # +1: the database hub
    # Never stamp a lower per-artifact count than the page already shows.
    hero_now = open(MAIN, encoding="utf-8").read()
    prev = re.search(r"Per-artifact websites live so far: ([\d,]+)\.", hero_now)
    if prev and n_art < int(prev.group(1).replace(",", "")):
        print(f"STATUS: REFUSED — per-artifact count dropped {prev.group(1)} -> {n_art}; not stamping")
        return 1
    prev_tile = re.search(
        r'<div class="n">([\d,]+)</div><div class="l">Websites \+ hub</div>', hero_now)
    if prev_tile and total < int(prev_tile.group(1).replace(",", "")):
        print(f"STATUS: REFUSED — websites total dropped {prev_tile.group(1)} "
              f"-> {total:,}; not stamping")
        return 1
    front_now = open(FRONT_MAIN, encoding="utf-8").read()
    prev_front = re.search(r"<b>([\d,]+) websites</b>, counted", front_now)
    if prev_front and total < int(prev_front.group(1).replace(",", "")):
        print(f"STATUS: REFUSED — front-door total dropped {prev_front.group(1)} "
              f"-> {total:,}; not stamping")
        return 1
    changed = (stamp(MAIN, total, n_art)
               | stamp(MIRROR, total, n_art, prefix="../")
               | stamp_front_door(FRONT_MAIN, total)
               | stamp_front_door(FRONT_ACC, total, prefix="../"))
    if not changed:
        print(f"STATUS: unchanged — {total:,} websites total")
        return 0
    # Commit + push only the two OS pages and the two front-door pages.
    run(["git", "config", "user.name", "JAH System"], check=False)
    run(["git", "config", "user.email", "jah@system.local"], check=False)
    run(["git", "add", "the-merica-l-boundless-ecosystem-os.html",
         "accessible/the-merica-l-boundless-ecosystem-os.html",
         "the-merica-l-virtual-internet.html",
         "accessible/the-merica-l-virtual-internet.html"])
    run(["git", "commit", "-qm",
         f"Hourly website counts: {total:,} websites total"])
    try:
        run(["git", "push", "-q", "origin", "main"])
        run(["git", "push", "-q", "origin", "main:gh-pages"])
    except RuntimeError as e:
        run(["git", "reset", "--soft", "HEAD~1"], check=False)
        print(f"STATUS: push failed, commit reset: {e}")
        return 1
    print(f"STATUS: updated + pushed — {total:,} websites total")
    return 0


if __name__ == "__main__":
    sys.exit(main())
