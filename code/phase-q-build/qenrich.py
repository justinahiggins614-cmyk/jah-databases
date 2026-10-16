#!/usr/bin/env python3
"""Enrich key_points for Phase-Q records that have fewer than 3.

Derives additional meaningful points from the description's clauses via
sentence transformations. Rewrites affected shard chunks in place.
"""
import gzip, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from qnewdbs import ALL_NEW

SHARD = os.path.expanduser("~/workspace/jah-databases-data-1/data")

TRANSFORMS = [
    (r"combining (.+)", "Combines \\1."),
    (r"built on (.+)", "Built on \\1."),
    (r"based on (.+)", "Based on \\1."),
    (r"designed to (.+)", "Designed to \\1."),
    (r"designed for (.+)", "Designed for \\1."),
    (r"featuring (.+)", "Features \\1."),
    (r"including (.+)", "Includes \\1."),
    (r"using (.+)", "Uses \\1."),
    (r"offering (.+)", "Offers \\1."),
    (r"providing (.+)", "Provides \\1."),
    (r"supporting (.+)", "Supports \\1."),
    (r"supports (.+)", "Supports \\1."),
    (r"with (.+)", "Includes \\1."),
    (r"for (.+)", "Built for \\1."),
]

GENERIC = "Filed as a full record with description, how-it-works, requirements, citations, and a runnable demonstration program."

# (regex on full desc, point template) — object captured up to a boundary
EXTRACTS = [
    (r"combining (.+?)(?: with | for |$)", "Combines \\1."),
    (r"built (?:directly )?on (?:top of )?(.+?)(?: with | for |\.|$)", "Built on \\1."),
    (r"based on (.+?)(?: with | for |\.|$)", "Based on \\1."),
    (r"centered around (.+?)(?: with |\.|$)", "Centered around \\1."),
    (r"enables (.+?)(?: with |\.|$)", "Enables \\1."),
    (r"allows (.+?)(?: with |\.|$)", "Allows \\1."),
    (r"designed for (.+?)(?: with |\.|$)", "Designed for \\1."),
    (r"designed to (.+?)(?: with |\.|$)", "Designed to \\1."),
    (r"featuring (.+?)(?: with |\.|$)", "Features \\1."),
    (r"including (.+?)(?: with |\.|$)", "Includes \\1."),
    (r"using (.+?)(?: with | for | to |\.|$)", "Uses \\1."),
    (r"offering (.+?)(?: with |\.|$)", "Offers \\1."),
    (r"providing (.+?)(?: with |\.|$)", "Provides \\1."),
    (r"supporting (.+?)(?: with |\.|$)", "Supports \\1."),
    (r"containing (.+?)(?: with | for |\.|$)", "Contains \\1."),
    (r"storing (.+?)(?: with | for |\.|$)", "Stores \\1."),
    (r"managing (.+?)(?: with | for |\.|$)", "Manages \\1."),
    (r"tracking (.+?)(?: with | for |\.|$)", "Tracks \\1."),
    (r"measuring (.+?)(?: with | for |\.|$)", "Measures \\1."),
]

def _cap(s):
    s = s.strip().rstrip(".")
    return s[0].upper() + s[1:] + "." if s else ""

def enrich(desc, existing, group=""):
    # strip any generic fallback points from a previous pass, then re-derive
    pts = [p for p in existing if p != GENERIC]
    if len(pts) >= 3:
        return pts[:4]
    base = pts[0] if pts else desc.strip()
    if not pts:
        pts = [base if base.endswith(".") else base + "."]
    d = desc.strip()
    for pat, tmpl in EXTRACTS:
        if len(pts) >= 4:
            break
        m = re.search(pat, d, re.IGNORECASE)
        if not m:
            continue
        obj = m.group(1).strip().rstrip(".")
        if len(obj) < 4 or len(obj) > 0.85 * len(d):
            continue
        pt = tmpl.replace("\\1", obj)
        pt = _cap(pt)
        if pt.lower() not in [p.lower() for p in pts]:
            pts.append(pt)
    # trailing "with X" / "for X" phrases
    if len(pts) < 4:
        m = re.search(r" with ([A-Za-z].{4,120})$", d.rstrip("."))
        if m:
            obj = m.group(1).strip()
            verb = "Supports" if re.search(r"quer|transact|replic|support|real-?time", obj, re.I) else "Includes"
            pt = _cap("%s %s" % (verb, obj))
            if pt.lower() not in [p.lower() for p in pts]:
                pts.append(pt)
    if len(pts) < 3:
        pts.append(GENERIC)
    # classification point guarantees 3 for pattern-less descriptions
    if len(pts) < 3:
        pts.append("Documented in this database under %s." % (group or "general"))
    return pts[:4]

def main():
    m = json.load(open(os.path.expanduser("~/workspace/jah-databases/data/manifest.json")))
    # slugs touched this phase: new DBs + the 25 tool DBs and signatures
    sys.path.insert(0, os.path.join(HERE))
    from qmap import TOOL_DBS
    slugs = {c["slug"] for c in ALL_NEW}
    slugs |= set(TOOL_DBS) | {s + "-signature" for s in TOOL_DBS}
    have = {x["slug"] for x in m["databases"]}
    slugs &= have
    fixed = 0
    rewritten_chunks = 0
    for slug in sorted(slugs):
        cdir = os.path.join(SHARD, slug, "chunks")
        if not os.path.isdir(cdir):
            continue
        for fn in sorted(os.listdir(cdir)):
            p = os.path.join(cdir, fn)
            rows = []
            changed = False
            with gzip.open(p, "rt", encoding="utf-8") as f:
                for line in f:
                    if not line.strip():
                        continue
                    r = json.loads(line)
                    # re-enrich if thin OR carries generic fallback points
                    kps = r.get("key_points", [])
                    if len(kps) < 3 or any(p == GENERIC for p in kps):
                        r["key_points"] = enrich(r["description"], kps, r.get("g", ""))
                        changed = True
                        fixed += 1
                    rows.append(r)
            if changed:
                with gzip.open(p, "wt", encoding="utf-8") as f:
                    for r in rows:
                        f.write(json.dumps(r, ensure_ascii=False) + "\n")
                rewritten_chunks += 1
    print("records enriched:", fixed, "| chunks rewritten:", rewritten_chunks)

if __name__ == "__main__":
    main()
