#!/usr/bin/env python3
"""Hourly website-count updater for the 'Merica-L Boundless Ecosystem OS page.

Counts (from TRACKED files only, so the number matches what is deployed):
  main sites      = <li> items in <ol class="sites"> on the main OS page
  per-artifact    = DB websites + file websites + mix websites (main pages only):
    DB    = db/*/website/index.html
          + db/marijuana-supplies/index.html
          + db/marijuana-supplies-signature/index.html   (Wave 1 pre-merge placement)
    files = db/*/records/*.html, excluding /accessible/ and /mirror/
    mixes = db/*/mixes/*/index.html, excluding /accessible/ and /mirror/
          + db/marijuana-supplies-set/index.html
          + db/marijuana-supplies-set/complete-grinder-system/index.html
          (Wave 1 set master + grinder mix)

Re-stamps both OS pages (main + accessible mirror):
  - hero: "browse its {M} main sites and {N} per-artifact websites"
  - every stale "39 websites" -> "{M} main sites"
  - every "N main sites" -> current M
  - artifact summary: "(Waves 1-2, {N} websites)"
  - stats tile: "Websites + hub" number -> {M} + {N} total websites,
    with today's count date (main page tile + mirror table row)

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

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAIN = os.path.join(ROOT, "the-merica-l-boundless-ecosystem-os.html")
MIRROR = os.path.join(ROOT, "accessible", "the-merica-l-boundless-ecosystem-os.html")


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


def stamp(path, m_sites, n_art):
    text = open(path, encoding="utf-8").read()
    orig = text
    total = m_sites + n_art
    today = datetime.date.today().isoformat()
    # Hero clause (covers old "39 websites", bare "N main sites", and number updates).
    text = re.sub(
        r"browse its (?:\d+ websites|\d+ main sites(?: and [\d,]+ per-artifact websites)?)",
        f"browse its {m_sites} main sites and {n_art:,} per-artifact websites",
        text)
    # Any other stale "39 websites" phrasing for the main-sites list.
    text = re.sub(r"39 websites", f"{m_sites} main sites", text)
    # Keep every other "N main sites" in step with the list.
    text = re.sub(r"\d+ main sites", f"{m_sites} main sites", text)
    # Per-artifact drop-down summary number.
    text = re.sub(
        r"First live per-artifact websites \(Waves 1–2, [\d,]+ websites\)",
        f"First live per-artifact websites (Waves 1–2, {n_art} websites)",
        text)
    # Stats tile: total websites (main sites + per-artifact), hub listed separately.
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
    # Never stamp a lower per-artifact count than the page already shows.
    hero_now = open(MAIN, encoding="utf-8").read()
    prev = re.search(r"and ([\d,]+) per-artifact websites", hero_now)
    if prev and n_art < int(prev.group(1).replace(",", "")):
        print(f"STATUS: REFUSED — count dropped {prev.group(1)} -> {n_art}; not stamping")
        return 1
    prev_tile = re.search(
        r'<div class="n">([\d,]+)</div><div class="l">Websites \+ hub</div>', hero_now)
    if prev_tile and m_sites + n_art < int(prev_tile.group(1).replace(",", "")):
        print(f"STATUS: REFUSED — websites total dropped {prev_tile.group(1)} "
              f"-> {m_sites + n_art:,}; not stamping")
        return 1
    changed = stamp(MAIN, m_sites, n_art) | stamp(MIRROR, m_sites, n_art)
    if not changed:
        print(f"STATUS: unchanged — {m_sites} main sites, {n_art} per-artifact "
              f"websites (db {n_db} + files {n_files} + mixes {n_mixes})")
        return 0
    # Commit + push only the two OS pages.
    run(["git", "config", "user.name", "JAH System"], check=False)
    run(["git", "config", "user.email", "jah@system.local"], check=False)
    run(["git", "add", "the-merica-l-boundless-ecosystem-os.html",
         "accessible/the-merica-l-boundless-ecosystem-os.html"])
    run(["git", "commit", "-qm",
         f"Hourly website counts: {m_sites} main sites, {n_art} per-artifact websites"])
    try:
        run(["git", "push", "-q", "origin", "main"])
        run(["git", "push", "-q", "origin", "main:gh-pages"])
    except RuntimeError as e:
        run(["git", "reset", "--soft", "HEAD~1"], check=False)
        print(f"STATUS: push failed, commit reset: {e}")
        return 1
    print(f"STATUS: updated + pushed — {m_sites} main sites, {n_art} per-artifact "
          f"websites (db {n_db} + files {n_files} + mixes {n_mixes})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
