#!/usr/bin/env python3
"""Filing plan + record assembly for Phase-Q (imported by build.py)."""
import json, os, re
from qentries import load_all
from qmap import map_tool
from qnewdbs import ALL_NEW, BY_SLUG, GROUP_DOMAIN

HIDDEN = os.path.expanduser("~/workspace/hidden_files")

TAXON_SECTION_DB = {
    "LABS (Environments, Workspaces, Testing Grounds)": "software-labs-taxonomy",
    "CORE & ENGINE CATEGORIES (Substrates, Runtimes, Stacks)": "core-engine-taxonomy",
    "STORAGE & REPOSITORY CATEGORIES (Data, Vaults, Inventories)": "storage-repository-taxonomy",
    "NETWORK & INTERCONNECTIVITY CATEGORIES (Bridges, Nodes, Streams)": "network-interconnect-taxonomy",
    "HARDWARE, FABRICATION & PHYSICAL SYSTEM TYPES": "hardware-fabrication-taxonomy",
}

TAXON_GLOSS = {
    "APPS (Applications, Programs, Software)": "It describes how application software is packaged, executed, and delivered to users.",
    "TOOLS (Utilities, Instruments, Engines, Mechanisms)": "It describes software utilities and instruments that perform specific tasks on a computer.",
    "LABS (Environments, Workspaces, Testing Grounds)": "It describes environments where software is built, tested, and run.",
    "CORE & ENGINE CATEGORIES (Substrates, Runtimes, Stacks)": "It describes the underlying substrates and runtimes that execute software.",
    "STORAGE & REPOSITORY CATEGORIES (Data, Vaults, Inventories)": "It describes where and how data is kept, organized, and retrieved.",
    "NETWORK & INTERCONNECTIVITY CATEGORIES (Bridges, Nodes, Streams)": "It describes how systems connect, communicate, and move data.",
    "HARDWARE, FABRICATION & PHYSICAL SYSTEM TYPES": "It describes physical devices and fabrication processes that software runs on.",
}

def taxon_desc(term, group, sub):
    gloss = TAXON_GLOSS.get(group, "It describes a category in the software taxonomy.")
    subbit = (" Classified under %s." % sub) if sub else ""
    return "%s — a taxonomy term in %s.%s %s" % (term, group.split("(")[0].strip().lower(), subbit, gloss)

def target_for(entry):
    """Return (public_slug, kind) for an entry. kind in dbprod/dtype/tool/taxon/bizarre."""
    fam = entry["family"]
    if fam == "dbprod":
        return "production-databases", "dbprod"
    if fam == "dtype":
        return GROUP_DOMAIN[entry["group"]], "dtype"
    if fam == "tool":
        s = map_tool(entry["name"], entry["desc"])
        return (s or "bizarre-software"), "tool"
    if fam == "taxon":
        g = entry["group"]
        if g.startswith("APPS"):
            return "computer-utilities", "taxon"
        if g.startswith("TOOLS"):
            s = map_tool(entry["name"], "")
            return (s or "computer-utilities"), "taxon"
        return TAXON_SECTION_DB.get(g, "software-labs-taxonomy"), "taxon"
    if fam == "bizarre":
        s = map_tool(entry["name"], entry["desc"])
        return (s or "bizarre-software"), "bizarre"
    raise ValueError(fam)

def build_plan():
    bizarre = json.load(open(os.path.join(HIDDEN, "bizarre-entries.json")))
    entries = load_all([]) + bizarre
    plan = {}
    stats = {}
    unmapped_tool = []
    for e in entries:
        slug, kind = target_for(e)
        if e["family"] in ("tool", "bizarre") and slug == "bizarre-software" and e["family"] == "tool":
            unmapped_tool.append(e["name"])
        plan.setdefault(slug, []).append((e, kind))
        stats[e["family"]] = stats.get(e["family"], 0) + 1
    return plan, stats, unmapped_tool

if __name__ == "__main__":
    plan, stats, unmapped = build_plan()
    print("families:", stats)
    print("target slugs:", len(plan))
    from collections import Counter
    c = Counter()
    for slug, items in plan.items():
        c[slug] = len(items)
    for slug, n in c.most_common():
        print("%4d  %s" % (n, slug))
    print("unmapped tool->bizarre-software:", len(unmapped))
