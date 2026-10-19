#!/usr/bin/env python3
"""Master builder for the 100-future-tech worker (items 1-50, public + Signature pairs).
Usage: python3 build_all.py [slug ...]   # builds listed slugs (one edition each); default: all loaded
Each slug dir: code/<slug>-build/build.py calls build_slug(slug).
Property of Justin Addam Higgins (JAH).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ftcommon import build_pair  # noqa: E402

TECHS = {}


def _load():
    if TECHS:
        return
    import importlib
    for mod, attr in [("content_01", "TECHS_01"), ("content_02", "TECHS_02"),
                      ("content_03", "TECHS_03"), ("content_04", "TECHS_04"),
                      ("content_05", "TECHS_05")]:
        try:
            m = importlib.import_module(mod)
        except ImportError:
            continue
        for t in getattr(m, attr, []):
            TECHS[t["slug"]] = (t, t["slug"], "public")
            TECHS[t["slug"] + "-signature"] = (t, t["slug"] + "-signature", "signature")


def build_slug(slug, execute_demos=True):
    _load()
    if slug not in TECHS:
        raise SystemExit("unknown slug: %s" % slug)
    t, _, edition = TECHS[slug]
    from ftcommon import build_pair as bp
    stats = bp(t, t["milestones"], execute_demos=execute_demos, editions=(edition,))
    print("BUILT %s: public=%d signature=%d demos_ok=%d" %
          (slug, stats["public"], stats["signature"], stats["demos_ok"]))
    return stats


def main(argv):
    _load()
    slugs = argv[1:] or sorted(TECHS)
    results = {}
    for s in slugs:
        results[s] = build_slug(s)
    print("TOTAL slugs built: %d" % len(results))
    return results


if __name__ == "__main__":
    main(sys.argv)
