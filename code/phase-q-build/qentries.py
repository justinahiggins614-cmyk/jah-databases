#!/usr/bin/env python3
"""Parse the 15 recovered paste files into structured entries.

Each entry: dict(family, group, name, desc, extra).
family: dbprod | dtype | tool | taxon | bizarre
"""
import os
import re

HF = "/home/hatch/workspace/hidden_files"


def _read(fn):
    with open(os.path.join(HF, fn), encoding="utf-8") as f:
        return f.read()


def _bullets(txt):
    """Parse '* Name: Description' bullets grouped by preceding header lines."""
    entries = []
    cur = "General"
    for line in txt.split("\n"):
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        if s.startswith("*"):
            m = re.match(r"\*\s*([^:]{2,80}):\s*(.+)", s)
            if m:
                entries.append((cur, m.group(1).strip(), m.group(2).strip()))
            continue
        if re.match(r"^[A-Za-z0-9][^:]*$", s) and len(s) < 90 and not s.startswith(("Here is", "Make sure", "Include all")):
            cur = s
    return entries


def parse_dbprod():
    out = []
    for fn in ("catalog-100-production.txt", "catalog-100-include-all-data.txt"):
        txt = _read(fn)
        cur = "General"
        for line in txt.split("\n"):
            s = line.strip()
            if not s or s.startswith("#"):
                continue
            if s.startswith("###"):
                cur = s.strip("# ").strip()
                continue
            m = re.match(r"\d+\.\s*\*\*(.+?)\*\*\s*[–\-]\s*(.+)", s)
            if m:
                out.append({"family": "dbprod", "group": cur,
                            "name": m.group(1).strip(), "desc": m.group(2).strip(),
                            "extra": {}})
    return out


def parse_dtype(fn):
    out = []
    txt = _read(fn)
    for group, name, desc in _bullets(txt):
        out.append({"family": "dtype", "group": group, "name": name,
                    "desc": desc, "extra": {}})
    return out


def parse_toolset(fn):
    out = []
    txt = _read(fn)
    for group, name, desc in _bullets(txt):
        out.append({"family": "tool", "group": "Toolset", "name": name,
                    "desc": desc, "extra": {}})
    return out


def parse_batbelt():
    out = []
    txt = _read("batbelt-matrix.txt")
    # entries: N. Title \n * Function Need: ... \n * Public Version: ... \n * Signature Version: ...
    parts = re.split(r"(?m)^\d+\.\s*", txt)
    for p in parts:
        p = p.strip()
        if not p or len(p) < 50:
            continue
        lines = p.split("\n")
        title = lines[0].strip()
        need = pub = sig = ""
        for ln in lines[1:]:
            s = ln.strip().lstrip("*").strip()
            if s.startswith("Function Need:"):
                need = s[len("Function Need:"):].strip()
            elif s.startswith("Public Version:"):
                pub = s[len("Public Version:"):].strip()
            elif s.startswith("Signature Version:"):
                sig = s[len("Signature Version:"):].strip()
        out.append({"family": "tool", "group": "Tool Matrix", "name": title,
                    "desc": need, "extra": {"pub": pub, "sig": sig, "need": need}})
    return out


def parse_compmodels():
    out = []
    txt = _read("dbtype-computational-models.txt")
    section = sub = "General"
    for line in txt.split("\n"):
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        if s.startswith("And add these"):
            continue
        m = re.match(r"^\d+\.\s*(.+)$", s)
        if m and len(s) < 80 and s.isupper():
            section = m.group(1).strip().title()
            sub = section
            continue
        if s.startswith("*"):
            name = s.lstrip("*").strip()
            if name:
                out.append({"family": "tool", "group": section + " / " + sub,
                            "name": name, "desc": "", "extra": {}})
            continue
        if len(s) < 70 and not s.startswith((" ", "\t")) and not re.match(r"^\d", s):
            # subsection header like "Abstract Machines & Formal Paradigms"
            if s[0].isupper():
                sub = s
    return out


def parse_taxonomy():
    out = []
    txt = _read("dbtype-apps-taxonomy.txt")
    section = sub = "General"
    for line in txt.split("\n"):
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        if s.startswith("Make sure"):
            continue
        m = re.match(r"^\d+\.\s*(.+)$", s)
        if m:
            section = m.group(1).strip()
            sub = section
            continue
        if s.startswith("*"):
            name = s.lstrip("*").strip()
            if name:
                out.append({"family": "taxon", "group": section, "sub": sub,
                            "name": name, "desc": "", "extra": {}})
            continue
        if len(s) < 70 and s[0].isupper() and not s.startswith(("By ",)):
            sub = s
        elif s.startswith("By "):
            sub = s
    return out


def parse_bizarre(bodies):
    """bodies: list of message body strings -> entries."""
    out = []
    for body in bodies:
        for m in re.finditer(r"\*\s*([^:*]{2,90}):\s*([^\n]{10,600})", body):
            name = m.group(1).strip()
            desc = m.group(2).strip()
            if name and desc and "http" not in desc:
                out.append({"family": "bizarre", "group": "Bizarre Software",
                            "name": name, "desc": desc, "extra": {}})
    # rename the non-PG entry per his order
    for e in out:
        if e["name"].lower() == "die with me":
            e["name"] = "Low Battery Lock-In"
    return out


def load_all(bizarre_bodies):
    entries = []
    entries += parse_dbprod()
    for fn in ("dbtype-healthcare-clinical.txt", "catalog-data-types.txt",
               "dbtype-education-academic.txt", "dbtype-neuromorphic-computing.txt",
               "dbtype-cosmological-simulation.txt", "dbtype-hardware-fabrication.txt"):
        entries += parse_dtype(fn)
    entries += parse_toolset("toolset-wifi-harvester-etc.txt")
    entries += parse_toolset("toolset-airgapped-diode-etc.txt")
    entries += parse_batbelt()
    entries += parse_compmodels()
    entries += parse_taxonomy()
    entries += parse_bizarre(bizarre_bodies)
    return entries


if __name__ == "__main__":
    es = load_all([])
    from collections import Counter
    c = Counter((e["family"]) for e in es)
    print(c, "total", len(es))
