"""Demo archetypes for the Made-With Databases archives.

Real, runnable, stdlib-only Python. Each documents or analyzes the network's
own build history - real archive facts about things made with the databases.
"""
import json


def _q(s):
    return json.dumps(s)


def _hdr(name, rid, group):
    return ('#!/usr/bin/env python3\n"""' + name.replace('"""', '"') + ' - working demonstration.\n'
            'Record ' + rid + ' [' + group + ']. Property of Justin Addam Higgins (JAH).\n"""\n')


def demo_lineage(name, rid, group, pts, req, dbs):
    return _hdr(name, rid, group) + '''\
"""Traces what was made back to the databases it was made with."""
CREATION = {
    "title": ''' + _q(name) + ''',
    "record": ''' + _q(rid) + ''',
    "databases_used": ''' + _q(dbs) + ''',
}
def main():
    print("LINEAGE - what was made, and what made it:")
    print("  creation: %s [%s]" % (CREATION["title"], CREATION["record"]))
    print("  databases used (%d):" % len(CREATION["databases_used"]))
    for i, db in enumerate(CREATION["databases_used"], 1):
        print("    %d. %s" % (i, db))
    assert len(CREATION["databases_used"]) >= 1
    print("OK: %s traced to %d source database(s)" % (CREATION["title"], len(CREATION["databases_used"])))
if __name__ == "__main__":
    main()
'''


def demo_catalog(name, rid, group, pts, req, catalog):
    return _hdr(name, rid, group) + '''\
"""Searchable mini-catalog of the Made-With archive (network build history)."""
CATALOG = ''' + json.dumps(catalog, ensure_ascii=False, indent=1) + '''
def search(keyword):
    kw = keyword.lower()
    return [e for e in CATALOG
            if kw in e["title"].lower() or kw in " ".join(e["dbs"]).lower()]
def main():
    print("made-with archive: %d creations indexed" % len(CATALOG))
    for kw in ["language", "book"]:
        hits = search(kw)
        print("  search '%s' -> %d hit(s): %s" % (kw, len(hits),
              ", ".join(h["title"][:40] for h in hits[:3])))
    assert len(search("language")) >= 1
    assert len(CATALOG) == 34
    print("OK: %s searched the 34-entry creation catalog" % ''' + _q(name) + ''')
if __name__ == "__main__":
    main()
'''


def demo_stats(name, rid, group, pts, req, dbs=None):
    return _hdr(name, rid, group) + '''\
"""Network milestone statistics (archive facts, October 2026)."""
MILESTONES = [
    ("2026-10-12", "Signature language unified", 716, "words mapped"),
    ("2026-10-15", "databases live", 1827, "manifest count"),
    ("2026-10-17", "database target raised", 10000, "target databases"),
    ("2026-10-18", "databases live", 4326, "manifest count"),
    ("2026-10-18", "R39 wave merged", 134, "food/travel/animal databases"),
]
def growth(rows):
    counts = [r for r in rows if r[1] == "databases live"]
    first, last = counts[0][2], counts[-1][2]
    return last - first, 100.0 * (last - first) / first
def main():
    print("network milestones (archive facts):")
    for date, what, n, unit in MILESTONES:
        print("  %s  %-28s %6d %s" % (date, what, n, unit))
    delta, pct = growth(MILESTONES)
    print("  live-database growth Oct 15 -> Oct 18: +%d (+%.1f%%)" % (delta, pct))
    assert delta == 4326 - 1827
    print("OK: %s computed network growth from archive facts" % ''' + _q(name) + ''')
if __name__ == "__main__":
    main()
'''


def demo_report(name, rid, group, pts, req, dbs):
    return _hdr(name, rid, group) + '''\
"""Prints the creation file as a formatted made-with report."""
INFO = {
    "title": ''' + _q(name) + ''',
    "record": ''' + _q(rid) + ''',
    "group": ''' + _q(group) + ''',
    "databases_used": ''' + _q(dbs) + ''',
    "key_points": ''' + _q(pts) + ''',
}
def main():
    print("=" * 64)
    print("MADE WITH THE NETWORK: " + INFO["title"])
    print("Record %s [%s]" % (INFO["record"], INFO["group"]))
    print("=" * 64)
    print("Built with:")
''' + "".join(('    print("  - %s")' % db.replace('"', "'")) + "\n" for db in dbs) + '''    print("Key points:")
''' + "".join(('    print("  %d. %s")' % (i + 1, p.replace('"', "'"))) + "\n" for i, p in enumerate(pts)) + '''    print("OK: %s made-with report printed" % INFO["title"])
if __name__ == "__main__":
    main()
'''


DEMOS_MADEWITH = {
    "lineage": demo_lineage, "catalog": demo_catalog,
    "stats": demo_stats, "report": demo_report,
}
