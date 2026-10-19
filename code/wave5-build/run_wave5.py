#!/usr/bin/env python3
"""Wave 5 runner: allocate prefixes, write thin drivers, build all 49 items.

Usage:
  python3 run_wave5.py allocate          # allocate prefixes -> prefixes.json
  python3 run_wave5.py drivers           # write code/<slug>-build/build.py drivers
  python3 run_wave5.py build [SLUG ...]  # build items (all if none given)
  python3 run_wave5.py trial             # build one small item end-to-end
"""
import sys, os, json, time, traceback

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
os.chdir(HERE)

import content_all
from content_all import family_for
from lib import (ITEMS, ORDER, finalize_registry, load_existing_prefixes,
                 alloc_prefix, build_item)

PREFIX_FILE = os.path.join(HERE, "prefixes.json")
PROGRESS_FILE = os.path.join(HERE, "progress.jsonl")


def existing_taken():
    taken = load_existing_prefixes()
    p = os.path.expanduser("~/workspace/wave5-prefixes-existing.json")
    if os.path.isfile(p):
        taken |= set(json.load(open(p)))
    return taken


def cmd_allocate():
    finalize_registry()
    taken = existing_taken()
    prefixes = {}
    for slug in ORDER:
        item = ITEMS[slug]
        pub, sig = alloc_prefix(family_for(slug), item["name"], taken)
        prefixes[slug] = [pub, sig]
    json.dump(prefixes, open(PREFIX_FILE, "w"), indent=1)
    print("allocated %d prefix pairs -> %s" % (len(prefixes), PREFIX_FILE))
    for slug in ORDER:
        print("  %-40s %s / %s" % (slug, prefixes[slug][0], prefixes[slug][1]))


DRIVER = '''#!/usr/bin/env python3
"""Thin build driver for %(slug)s (wave 5 of 1000-list). Re-runnable: rebuilds the
public + Signature pair from the wave-5 content registry."""
import sys, os
sys.path.insert(0, os.path.expanduser("~/workspace/jah-databases/code/wave5-build"))
os.chdir(os.path.expanduser("~/workspace/jah-databases/code/wave5-build"))
import content_all  # noqa: F401  (registers all 49 items)
from lib import finalize_registry, build_item

SLUG = "%(slug)s"
PREFIXES = ("%(pub)s", "%(sig)s")

def main():
    finalize_registry()
    build_item(SLUG, PREFIXES, set())

if __name__ == "__main__":
    main()
'''


def cmd_drivers():
    finalize_registry()
    prefixes = json.load(open(PREFIX_FILE))
    assert set(prefixes) == set(ITEMS), "prefix/item mismatch"
    n = 0
    for slug in ORDER:
        ddir = os.path.expanduser("~/workspace/jah-databases/code/%s-build" % slug)
        os.makedirs(ddir, exist_ok=True)
        pub, sig = prefixes[slug]
        with open(os.path.join(ddir, "build.py"), "w") as f:
            f.write(DRIVER % {"slug": slug, "pub": pub, "sig": sig})
        n += 1
    print("wrote %d drivers" % n)


def log_progress(slug, ok, detail=""):
    with open(PROGRESS_FILE, "a") as f:
        f.write(json.dumps({"t": time.time(), "slug": slug, "ok": ok,
                            "detail": detail}) + "\n")


def already_built(slug):
    if not os.path.isfile(PROGRESS_FILE):
        return False
    ok = set()
    for line in open(PROGRESS_FILE):
        try:
            d = json.loads(line)
        except Exception:
            continue
        if d.get("slug") == slug and d.get("ok"):
            ok.add(slug)
    return slug in ok


def cmd_build(slugs):
    finalize_registry()
    prefixes = json.load(open(PREFIX_FILE))
    if not slugs:
        slugs = [s for s in ORDER if not already_built(s)]
    failed = []
    for slug in slugs:
        if slug not in ITEMS:
            print("SKIP unknown slug %s" % slug)
            continue
        t0 = time.time()
        try:
            build_item(slug, tuple(prefixes[slug]), set())
            log_progress(slug, True, "%.1fs" % (time.time() - t0))
        except Exception as e:
            tb = traceback.format_exc(limit=8)
            print("FAILED %s: %s\n%s" % (slug, e, tb), flush=True)
            log_progress(slug, False, "%s" % e)
            failed.append(slug)
    print("done: %d ok, %d failed" % (len(slugs) - len(failed), len(failed)))
    if failed:
        print("failed:", " ".join(failed))


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "build"
    if cmd == "allocate":
        cmd_allocate()
    elif cmd == "drivers":
        cmd_drivers()
    elif cmd == "trial":
        cmd_build(["db-unusual-footprint"])
    elif cmd == "build":
        cmd_build(sys.argv[2:])
    else:
        sys.exit("unknown command %s" % cmd)
