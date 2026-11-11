#!/usr/bin/env python3
"""Hourly website-count updater for the 'Merica-L Boundless Ecosystem OS page.

Counts (from TRACKED files only, so the number matches what is deployed):
  websites = <li> items in <ol class="sites"> on the main OS page
  per-artifact    = DB websites + file websites + mix websites (main pages only):
    DB    = db/*/website/index.html
          + db/marijuana-supplies/index.html
          + db/marijuana-supplies-signature/index.html   (Wave 1 pre-merge placement)
    files = db/*/records/*.html, excluding /accessible/ and /mirror/
    mixes = db/*/mixes/*/index.html, excluding /accessible/ and /mirror/
          + db/marijuana-supplies-set/index.html
          + db/marijuana-supplies-set/complete-grinder-system/index.html
          (Wave 1 set master + grinder mix)
  mirrors = mirrors/*/index.html (main pages only, excluding /accessible/
          and /mirror/ — Signature mirrors of real websites online)

Re-stamps the OS pages (main + accessible mirror) and the 'Merica-L
Virtual Internet front-door pages (main + accessible mirror):
  - hero: "browse its {M} websites and {N} per-artifact websites"
    (+ ", and {K} mirror websites" once mirrors are live)
  - every stale "39 websites" -> "{M} websites"
  - every "N websites" -> current M
  - artifact summary: "(Waves 1-2, {N} websites)"
  - stats tile: "Websites + hub" number -> {M} + {N} + {K} total websites,
    with today's count date (main page tile + mirror table row)
  - front door: "{T} websites — {M} websites and {N} per-artifact
    websites" (+ ", and {K} mirror websites" once mirrors are live),
    with today's count date, on both front-door pages

Safety: pulls --ff-only first; skips the run if the working tree has ANY
uncommitted changes (another agent's work in progress); commits + pushes
(main + gh-pages) only when the stamped numbers actually changed; never
stamps a LOWER per-artifact count than the one already on the page (a drop
means a counting error, not progress). Prints one STATUS line.
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
    m = re.search(r'<ol class="sites">(.*?)</ol>', html, re.S)
    if not m:
        raise RuntimeError("no <ol class=\"sites\"> on main OS page")
    return m.group(1).count("<li")


def count_per_artifact():
    db = ls_files("db/*/website/index.html")
    db += ls_files("db/marijuana-supplies/index.html",
                   "db/marijuana-supplies-signature/index.html")
    files = [p for p in ls_files("db/*/records/*.html")
             if "/accessible/" not in p and "/mirror/" not in p]
    mixes = [p for p in ls_files("db/*/mixes/*/index.html")
             if "/accessible/" not in p and "/mirror/" not in p]
    mixes += ls_files("db/marijuana-supplies-set/index.html",
                      "db/marijuana-supplies-set/complete-grinder-system/index.html")
    return len(db), len(files), len(mixes), len(db) + len(files) + len(mixes)


def count_mirrors():
    # Main pages only: the glob mirrors/*/index.html cannot match
    # mirrors/<slug>/accessible/index.html or mirrors/<slug>/mirror/index.html.
    return len(ls_files("mirrors/*/index.html"))


def hero_clause(m_sites, n_art, n_mir):
    if n_mir:
        return (f"browse its {m_sites} websites, {n_art:,} per-artifact websites, "
                f"and {n_mir} mirror websites")
    return f"browse its {m_sites} websites and {n_art:,} per-artifact websites"


def stamp(path, m_sites, n_art, n_mir=0):
    text = open(path, encoding="utf-8").read()
    orig = text
    total = m_sites + n_art + n_mir
    today = today_user()
    # Hero clause (covers old "39 websites", bare "N websites", the
    # two-part form, and the three-part mirror form). The regex must
    # consume the optional mirror tail, or re.sub duplicates it.
    text = re.sub(
        r"browse its (?:\d+ websites(?:, [\d,]+ per-artifact websites, and \d+ mirror websites| and [\d,]+ per-artifact websites)?|\d+ (?:main sites|original websites)(?: and [\d,]+ per-artifact websites)?)",
        hero_clause(m_sites, n_art, n_mir),
        text)
    # Any other stale "39 websites" phrasing for the main-sites list.
    text = re.sub(r"39 websites", f"{m_sites} websites", text)
    # Keep every other "N websites" in step with the list.
    text = re.sub(r"\d+ (?:main sites|original websites)", f"{m_sites} websites", text)
    # Per-artifact drop-down summary number.
    text = re.sub(
        r"First live per-artifact websites \(Waves 1–2, [\d,]+ websites\)",
        f"First live per-artifact websites (Waves 1–2, {n_art} websites)",
        text)
    # Stats tile: total websites (websites + per-artifact), hub listed separately.
    text = re.sub(
        r'<div class="stat"><div class="n">[\d,]+</div><div class="l">Websites \+ hub</div>'
        r'<div class="s">counted [\d-]+</div></div>',
        f'<div class="stat"><div class="n">{total:,}</div><div class="l">Websites + hub</div>'
        f'<div class="s">counted {today}</div></div>',
        text)
    # Numbers-table Websites row (mirror: plain <td>; main page: <td class="num">).
    def _web_row(m):
        cls = m.group(1) or ""
        return (f'<tr><td>Websites</td><td{cls}>{total:,}, plus the database hub</td>'
                f'<td>{today}</td></tr>')
    text = re.sub(
        r'<tr><td>Websites</td><td( class="num")?>[\d,]+, plus the database hub</td>'
        r'<td>[\d-]+</td></tr>',
        _web_row, text)
    if text != orig:
        open(path, "w", encoding="utf-8").write(text)
    return text != orig


def count_phrase(m_sites, n_art, n_mir):
    total = m_sites + n_art + n_mir
    if n_mir:
        return (f"{total:,} websites — {m_sites} websites, {n_art:,} per-artifact "
                f"websites, and {n_mir} mirror websites")
    return (f"{total:,} websites — {m_sites} websites and {n_art:,} per-artifact "
            f"websites")


def stamp_front_door(path, m_sites, n_art, n_mir):
    """Re-stamp the website-count phrases on a virtual-internet front-door
    page (main or accessible). Only the website-count sentences are touched:
    the database-hub count ("63,047 databases ... counted 2026-11-09") is
    never rewritten here. The front door itself is never counted."""
    text = open(path, encoding="utf-8").read()
    orig = text
    total = m_sites + n_art + n_mir
    today = today_user()
    phrase = count_phrase(m_sites, n_art, n_mir)
    # The count phrase, in all its forms (two-part and three-part).
    text = re.sub(
        r"[\d,]+ websites — \d+ websites(?:, [\d,]+ per-artifact websites, and \d+ mirror websites| and [\d,]+ per-artifact websites)",
        phrase, text)
    # The count date on the website-count sentences only (they end with
    # ", the same count the 'Merica-L Boundless Ecosystem OS page shows",
    # or, in the hero, with ". This front door page itself is not counted").
    text = re.sub(
        r"counted [\d-]+(, the same count the 'Merica-L Boundless Ecosystem OS page shows)",
        f"counted {today}\\1", text)
    text = re.sub(
        r"counted [\d-]+(\. This front door page itself is not counted)",
        f"counted {today}\\1", text)
    # "not counted as a website in that N" (hero, notes, and the file-name comment).
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
    total = m_sites + n_art + n_mir
    # Never stamp a lower per-artifact count than the page already shows.
    hero_now = open(MAIN, encoding="utf-8").read()
    prev = re.search(r"and ([\d,]+) per-artifact websites", hero_now)
    if prev and n_art < int(prev.group(1).replace(",", "")):
        print(f"STATUS: REFUSED — count dropped {prev.group(1)} -> {n_art}; not stamping")
        return 1
    prev_tile = re.search(
        r'<div class="n">([\d,]+)</div><div class="l">Websites \+ hub</div>', hero_now)
    if prev_tile and total < int(prev_tile.group(1).replace(",", "")):
        print(f"STATUS: REFUSED — websites total dropped {prev_tile.group(1)} "
              f"-> {total:,}; not stamping")
        return 1
    front_now = open(FRONT_MAIN, encoding="utf-8").read()
    prev_front = re.search(
        r"([\d,]+) websites — \d+ websites(?:, [\d,]+ per-artifact websites, "
        r"and \d+ mirror websites| and [\d,]+ per-artifact websites)", front_now)
    if prev_front and total < int(prev_front.group(1).replace(",", "")):
        print(f"STATUS: REFUSED — front-door total dropped {prev_front.group(1)} "
              f"-> {total:,}; not stamping")
        return 1
    changed = (stamp(MAIN, m_sites, n_art, n_mir)
               | stamp(MIRROR, m_sites, n_art, n_mir)
               | stamp_front_door(FRONT_MAIN, m_sites, n_art, n_mir)
               | stamp_front_door(FRONT_ACC, m_sites, n_art, n_mir))
    if not changed:
        print(f"STATUS: unchanged — {m_sites} websites, {n_art} per-artifact "
              f"websites (db {n_db} + files {n_files} + mixes {n_mixes}), "
              f"{n_mir} mirror websites")
        return 0
    # Commit + push only the two OS pages and the two front-door pages.
    run(["git", "config", "user.name", "JAH System"], check=False)
    run(["git", "config", "user.email", "jah@system.local"], check=False)
    run(["git", "add", "the-merica-l-boundless-ecosystem-os.html",
         "accessible/the-merica-l-boundless-ecosystem-os.html",
         "the-merica-l-virtual-internet.html",
         "accessible/the-merica-l-virtual-internet.html"])
    run(["git", "commit", "-qm",
         f"Hourly website counts: {m_sites} websites, {n_art} per-artifact websites, "
         f"{n_mir} mirror websites"])
    try:
        run(["git", "push", "-q", "origin", "main"])
        run(["git", "push", "-q", "origin", "main:gh-pages"])
    except RuntimeError as e:
        run(["git", "reset", "--soft", "HEAD~1"], check=False)
        print(f"STATUS: push failed, commit reset: {e}")
        return 1
    print(f"STATUS: updated + pushed — {m_sites} websites, {n_art} per-artifact "
          f"websites (db {n_db} + files {n_files} + mixes {n_mixes}), "
          f"{n_mir} mirror websites")
    return 0


if __name__ == "__main__":
    sys.exit(main())
