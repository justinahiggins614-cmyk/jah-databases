#!/usr/bin/env python3
"""Build the Reference Images and Technical Illustrations pair (gap-audit part 2).

Verified 2026-10-17: NO database covers technical illustration as a discipline
(component reference images, schematic libraries, exploded views,
drawing-relationship graphs). Manifest keyword search (technical-illustration,
reference-image): zero hits. Nearest neighbors are drawing-adjacent study items
only. ZERO full-record coverage.

Two NEW databases, 34 ladder-ordered records each:
  reference-images-technical-illustrations            (public-harvest)
  reference-images-technical-illustrations-signature  (signature)

Never any website references. No Facebook.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, "/home/hatch/workspace/jah-databases/code/gapaudit-p2")
import driver
from entries_reference_images import ENTRIES

RK = "technical illustration record"
CIT_PUB = ("Technical illustration (standard references: ISO 128 (technical drawings - "
           "general principles); ASME Y14.5-2018 'Dimensioning and Tolerancing'; "
           "Giesecke et al. 'Technical Drawing with Engineering Graphics' 15th ed. 2016; "
           "ISO 2768 general tolerances; Jensen et al. 'Engineering Drawing and Design'; "
           "IEEE 315 / IEC 60617 schematic symbols; ISO 2553 welding symbols; "
           "ISO 1302 surface texture; ASME Y14.38 abbreviations).")
CIT_SIG = CIT_PUB + " Signature editions are his original Signature treatment of technical illustration."
STANDARDS = ["Drawing practice per ISO 128 / ASME Y14.5 as cited",
             "Teaching-ladder order: foundations, compounded, advanced"]

cfg_pub, cfg_sig = driver.pair_cfgs(
    slug_base="reference-images-technical-illustrations", name_base="Reference Images and Technical Illustrations",
    tagline=("Component reference images, the schematic library, exploded views, and "
             "drawing-relationship graphs: how engineers draw exactly what they mean, from "
             "line types and orthographic projection through dimensioning, schematics, and "
             "GD&T to the master drawing index - taught progressively along the ladder."),
    record_kind=RK, prefix_pub="JAH-RITI-", prefix_sig="JAH-RITIS-",
    ai_base="JAH Illustration Archivist",
    role_pub=("technical illustration archivist - reference images, drawing standards, "
              "projection, dimensioning, schematics, exploded views, BOMs, GD&T, "
              "drawing-relationship graphs; teaching progressively along the ladder from "
              "foundations through compounded to advanced; answers from many angles - "
              "definition, example, procedure, math, standards - using only the system's "
              "own archive data"),
    role_sig=("technical illustration archivist - Signature editions: his original Signature "
              "treatment of technical illustration, clearly labeled Signature-made and never "
              "presented as authentic public record; teaches progressively along the ladder; "
              "answers from many angles using only the system's own archive data"),
    search_ph="Search orthographic, dimensioning, schematic, exploded view, GD&T, BOM...",
    chat_ph="Ask about technical illustration...",
    archive_topic="technical-illustration records",
    gen_kind="technical-illustration",
    standards=STANDARDS, cit_pub=CIT_PUB, cit_sig=CIT_SIG,
    hero_pub=("Public records - real, fact-checked technical illustration: what a technical "
              "drawing is, orthographic projection, line types, scales, paper sizes, title "
              "blocks, dimensioning, schematic symbols, pictorial views, reference images, "
              "sketching, ISO vs ASME, sections, detail views, dimensioning methods, "
              "tolerances, electrical schematics, P&ID, exploded views, BOMs, surface finish, "
              "welding symbols, symbol libraries, revision control, GD&T, stack-up analysis, "
              "drawing-relationship graphs, model-based definition, image libraries, "
              "cross-referencing, configuration management, digitization, printable reference "
              "models, and the master drawing index - organized in the Signature system. "
              "Every record carries the full entry: description, how it works, key points, "
              "requirements, standards, citations, and a working demonstration program. "
              "Records are ordered by the teaching ladder: Foundations -> Compounded -> Advanced."),
    hero_sig=("Signature originals - his original Signature treatment of technical "
              "illustration: the full ladder from line types and projection through "
              "dimensioning, schematics, exploded views, and GD&T to the master drawing "
              "index, reframed as Signature science. Clearly labeled Signature-made, never "
              "presented as authentic public record. Every record carries the full entry: "
              "description, how it works, key points, requirements, standards, citations, "
              "and a working demonstration program."))

DEMOS = {}


def _reg(key):
    def deco(fn):
        DEMOS[key] = fn
        return fn
    return deco


import json as _json


@_reg("ri_scale")
def d_scale(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # drawing scale 1:50 -> real size; measured 34 mm on the sheet
    scale = 50.0
    measured_mm = 34.0
    real_mm = measured_mm * scale
    print("scale 1:%.0f, measured %.1f mm -> real %.0f mm = %.2f m" % (scale, measured_mm, real_mm, real_mm / 1000.0))
    assert abs(real_mm - 1700.0) < 1e-9
    # reverse: a 2.5 m wall at 1:50 draws as 50 mm
    assert abs(2500.0 / scale - 50.0) < 1e-9
    print("OK: %s converted drawing scale both directions" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("ri_paper")
def d_paper(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
import math
def main():
    # A-series: A0 = 1 m^2, aspect ratio sqrt(2); each step halves the area
    w, h = 841.0, 1189.0  # A0 in mm
    print("A0: %d x %d mm, area %.4f m^2, ratio %.4f" % (w, h, w * h / 1e6, h / w))
    assert abs(w * h / 1e6 - 1.0) < 0.001
    assert abs(h / w - math.sqrt(2)) < 0.001
    sizes = {"A0": (841, 1189)}
    for i in range(1, 5):
        pw, ph = sizes["A%d" % (i - 1)]
        sizes["A%d" % i] = (ph // 2, pw)  # halve along the long side, swap
    for k in ("A1", "A2", "A3", "A4"):
        pw, ph = sizes[k]
        print("  %s: %d x %d mm" % (k, pw, ph))
    assert sizes["A4"] == (210, 297), sizes["A4"]
    print("OK: %s derived the A-series from the 1 m^2 rule" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("ri_tol")
def d_tol(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
import math
def main():
    # tolerance stack: three plates 25+/-0.1, 40+/-0.15, 10+/-0.05 in series
    dims = [(25.0, 0.10), (40.0, 0.15), (10.0, 0.05)]
    nominal = sum(d for d, t in dims)
    worst = sum(t for d, t in dims)
    rss = math.sqrt(sum(t ** 2 for d, t in dims))
    print("nominal %.1f worst-case +/-%.2f RSS +/-%.3f" % (nominal, worst, rss))
    assert abs(nominal - 75.0) < 1e-9
    assert abs(worst - 0.30) < 1e-9
    assert abs(rss - 0.1871) < 1e-3, rss
    print("OK: %s stacked tolerances worst-case and RSS" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("ri_bom")
def d_bom(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # indented BOM -> flattened total quantities (explode the product tree)
    BOM = {
        "WIDGET-A": [("BOLT-M6", 4), ("HOUSING", 1)],
        "HOUSING": [("BOLT-M6", 2), ("GASKET", 1)],
    }
    totals = {}
    def explode(part, qty):
        totals[part] = totals.get(part, 0) + qty
        for sub, q in BOM.get(part, []):
            explode(sub, qty * q)
    explode("WIDGET-A", 1)
    for p in sorted(totals):
        print("  %s: %d" % (p, totals[p]))
    assert totals == {"WIDGET-A": 1, "BOLT-M6": 6, "HOUSING": 1, "GASKET": 1}, totals
    print("OK: %s exploded the BOM to total quantities" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("ri_proj")
def d_proj(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # orthographic projection: a 3D corner (x right, y up, z out) -> three views
    pt = (30.0, 20.0, 10.0)
    front = (pt[0], pt[1])   # x, y
    top = (pt[0], pt[2])     # x, z
    side = (pt[2], pt[1])    # z, y
    print("3D point %s" % (pt,))
    print("  front view (x,y): %s" % (front,))
    print("  top view   (x,z): %s" % (top,))
    print("  side view  (z,y): %s" % (side,))
    assert front == (30.0, 20.0) and top == (30.0, 10.0) and side == (10.0, 20.0)
    # alignment check: front/top share x, front/side share y
    assert front[0] == top[0] and front[1] == side[1]
    print("OK: %s projected a 3D point to three aligned views" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("ri_dim")
def d_dim(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # chain vs baseline: feature positions and accumulated tolerance
    features = [25.0, 40.0, 30.0]   # segment lengths
    tols = [0.10, 0.15, 0.10]
    # chain: overall tolerance = sum
    chain_tol = sum(tols)
    # baseline from datum: each feature +/- its own only
    base_tol_each = tols
    overall_nom = sum(features)
    print("segments %s nominal overall %.1f" % (features, overall_nom))
    print("  chain overall tolerance: +/-%.2f" % chain_tol)
    print("  baseline: each feature keeps its own %s" % (base_tol_each,))
    assert abs(overall_nom - 95.0) < 1e-9 and abs(chain_tol - 0.35) < 1e-9
    print("OK: %s compared chain and baseline dimensioning" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("ri_line")
def d_line(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # ISO 128 line-type dash patterns: (dash, gap) segments in mm
    patterns = {
        "visible": [(10.0, 0.0)],            # continuous
        "hidden": [(3.0, 1.5)],              # dashed
        "center": [(12.0, 1.5), (1.0, 1.5)], # long-short chain
        "cutting": [(12.0, 1.5), (1.0, 1.5), (1.0, 1.5)],
    }
    for lt, segs in patterns.items():
        total = sum(d + g for d, g in segs)
        print("  %-8s pattern length %.1f mm over %d segments" % (lt, total, len(segs)))
    assert patterns["hidden"] == [(3.0, 1.5)]
    assert len(patterns["center"]) == 2
    print("OK: %s encoded ISO 128 line-type patterns" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("ri_gdt")
def d_gdt(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
import math
def main():
    # position tolerance: hole axis must lie within a cylindrical zone of diameter t
    t = 0.10  # position tolerance diameter, mm
    r = t / 2.0
    zone_area = math.pi * r ** 2
    # measured hole center offset from true position
    dx, dy = 0.030, 0.040
    dev = math.hypot(dx, dy)
    print("position zone dia %.2f mm (area %.4f mm^2); measured deviation %.3f mm" % (t, zone_area, dev))
    print("  -> %s" % ("ACCEPT" if dev <= r else "REJECT"))
    assert dev <= r, "hole fails position"
    assert abs(zone_area - 0.007854) < 1e-5
    print("OK: %s checked a position tolerance zone" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("ri_explode")
def d_explode(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # exploded view: parts offset along the assembly axis (+z) in disassembly order
    parts = [("base", 0.0), ("gasket", 8.0), ("housing", 12.0), ("bolt", 20.0)]
    gap = 25.0
    exploded = [(p, i * gap) for i, (p, z) in enumerate(parts)]
    for p, z in exploded:
        print("  %-8s exploded z = %.0f" % (p, z))
    zs = [z for _, z in exploded]
    assert zs == sorted(zs) and len(set(zs)) == len(zs), "parts must separate in order"
    assert exploded[-1][1] == 75.0
    print("OK: %s laid out an exploded view along the assembly axis" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("ri_graph")
def d_graph(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # drawing-relationship graph: where-used query for part P-101
    refs = {  # drawing -> drawings it references
        "ASM-001": ["P-101", "P-102", "SUB-010"],
        "SUB-010": ["P-101", "P-103"],
        "ASM-002": ["SUB-010", "P-104"],
    }
    target = "P-101"
    users = [d for d, rs in refs.items() if target in rs]
    print("where-used %s: %s" % (target, users))
    assert users == ["ASM-001", "SUB-010"], users
    # transitive: what references the users?
    affected = set(users)
    for d, rs in refs.items():
        if any(u in rs for u in users):
            affected.add(d)
    print("change blast radius: %s" % sorted(affected))
    assert "ASM-002" in affected
    print("OK: %s answered a where-used query on the drawing graph" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("ri_thumb")
def d_thumb(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
import hashlib
def main():
    # reference-image catalog entry: metadata + integrity checksum
    entry = {
        "subject": "connector pin fretting corrosion, 2019 set",
        "viewpoint": "macro, 5x",
        "date": "2019-06-14",
        "scale_ref": "mm ruler in frame",
        "bytes": 2457600,
    }
    fake_pixels = ("PIXELDATA:" + entry["subject"]).encode()
    entry["sha256"] = hashlib.sha256(fake_pixels).hexdigest()[:16]
    for k in ("subject", "viewpoint", "date", "scale_ref", "sha256"):
        print("  %s: %s" % (k, entry[k]))
    assert len(entry["sha256"]) == 16
    assert entry["bytes"] > 0
    print("OK: %s cataloged a reference image with integrity checksum" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("ri_svg")
def d_svg(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
import xml.etree.ElementTree as ET
def main():
    # generate a schematic fragment: resistor symbol between two terminals
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" width="200" height="60">'
           '<line x1="10" y1="30" x2="60" y2="30" stroke="black"/>'
           '<polyline points="60,30 70,15 90,45 110,15 130,45 140,30" fill="none" stroke="black"/>'
           '<line x1="140" y1="30" x2="190" y2="30" stroke="black"/>'
           '<text x="100" y="55" text-anchor="middle">R12</text></svg>')
    root = ET.fromstring(svg)  # validates well-formed XML
    ns = "{http://www.w3.org/2000/svg}"
    elems = [e.tag.replace(ns, "") for e in root.iter() if e.tag != root.tag]
    print("schematic fragment elements: %s" % elems)
    assert "polyline" in elems and "text" in elems
    print("OK: %s generated a valid schematic SVG fragment" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("ri_print")
def d_print(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # 3D-printable reference model: estimate print time, DISCLOSED as estimate
    # model: 120 mm demo gearbox housing section, 0.2 mm layers, 15% infill
    volume_cm3 = 16.4          # sliced model volume from the STL
    speed_mm3_s = 15.0         # volumetric print speed of the profile
    t_min = volume_cm3 * 1000.0 / speed_mm3_s / 60.0
    t_min *= 1.2               # +20% travel/retraction overhead
    print("model volume %.1f cm^3 at %.0f mm^3/s -> ESTIMATED print time %.0f min" % (volume_cm3, speed_mm3_s, t_min))
    print("DISCLOSED ESTIMATE ONLY: real time varies with printer, material, settings.")
    assert 18.0 < t_min < 26.0, t_min
    print("directions: PLA, 0.2 mm layers, 15%% infill, supports on overhangs only, critical faces up")
    print("OK: %s estimated print time and disclosed it as an estimate" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


def main():
    return driver.run_pair(HERE, cfg_pub, cfg_sig, ENTRIES, DEMOS)


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
