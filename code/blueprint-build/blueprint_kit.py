#!/usr/bin/env python3
"""Shared kit for the blueprint-build worker (Manon's Project Three).

ASCII schematic plan renderer + demo-program builder + text helpers.
All plans are labeled schematic (not to construction scale); room dims in
key_points are the nominal design dimensions.
"""
import math

# ---------------------------------------------------------------- text helpers

def _r2(x):
    return int(x) if float(x) == int(float(x)) else round(float(x), 1)

def fmt_dim(w, d, unit="ft"):
    return "%s x %s %s" % (_r2(w), _r2(d), unit)

def scale_spaces(spaces, scale):
    out = []
    for name, w, d in spaces:
        out.append((name, round(w * scale * 2) / 2, round(d * scale * 2) / 2))
    return out

# ---------------------------------------------------------------- plan layout
# Simple strip layout: rooms sorted by area, packed into rows whose target
# width keeps the footprint roughly square. Positions are in the archetype's
# own units (feet for buildings, inches for tools, etc.).

def place_spaces(spaces):
    items = sorted(spaces, key=lambda r: -(r[1] * r[2]))
    total = sum(w * d for _, w, d in items)
    widest = max(w for _, w, _ in items)
    row_w = max(widest, math.sqrt(total * 1.3))
    rows, cur, curw = [], [], 0.0
    for name, w, d in items:
        if cur and curw + w > row_w * 1.03:
            rows.append(cur); cur, curw = [], 0.0
        cur.append((name, w, d)); curw += w
    if cur:
        rows.append(cur)
    placed, y, W = [], 0.0, 0.0
    for row in rows:
        rh = max(d for _, _, d in row)
        x = 0.0
        for name, w, d in row:
            placed.append({"name": name, "x": x, "y": y, "w": w, "d": d})
            x += w
        W = max(W, x); y += rh
    return placed, W, y


def render_plan(title, placed, W, D, unit="ft", ft_per_char=2.0,
                subtitle="Schematic plan - not to construction scale"):
    gw = max(8, int(round(W / ft_per_char)))
    gh = max(5, int(round(D / ft_per_char)))
    g = [[" "] * gw for _ in range(gh)]

    def hline(yy, x0, x1):
        for x in range(max(0, x0), min(gw, x1)):
            if g[yy][x] == " ":
                g[yy][x] = "-"

    def vline(xx, y0, y1):
        for y in range(max(0, y0), min(gh, y1)):
            if g[y][xx] == " ":
                g[y][xx] = "|"

    for r in placed:
        x0 = int(r["x"] / ft_per_char); y0 = int(r["y"] / ft_per_char)
        x1 = max(x0 + 2, int(round((r["x"] + r["w"]) / ft_per_char)))
        y1 = max(y0 + 2, int(round((r["y"] + r["d"]) / ft_per_char)))
        x0 = min(max(x0, 0), gw - 1); x1 = min(max(x1, x0 + 1), gw)
        y0 = min(max(y0, 0), gh - 1); y1 = min(max(y1, y0 + 1), gh)
        if x1 - x0 < 2 or y1 - y0 < 2:
            continue  # degenerate sliver (e.g. a 1-ft wall strip) - in schedule only
        hline(y0, x0, x1); hline(y1 - 1, x0, x1)
        vline(x0, y0, y1); vline(x1 - 1, y0, y1)
        for cx, cy in ((x0, y0), (x1 - 1, y0), (x0, y1 - 1), (x1 - 1, y1 - 1)):
            if 0 <= cy < gh and 0 <= cx < gw:
                g[cy][cx] = "+"
        label = r["name"][:max(1, x1 - x0 - 2)]
        ly = y0 + (y1 - y0) // 2
        lx = x0 + max(1, (x1 - x0 - len(label)) // 2)
        if ly > y0 and ly < y1 - 1:
            for i, ch in enumerate(label):
                if lx + i < x1 - 1:
                    g[ly][lx + i] = ch
    lines = ["".join(row).rstrip() for row in g]
    head = ["PLAN: %s" % title,
            "Overall %s x %s %s | 1 char = %s %s | %s"
            % (_r2(W), _r2(D), unit, _r2(ft_per_char), unit, subtitle)]
    return "\n".join(head + lines)


# ---------------------------------------------------------------- demo program

def demo_program(rid, title, plan_text, stats):
    """Build a runnable Python demo: prints the plan, prints stats, OK marker."""
    safe = plan_text.replace("\\", "\\\\")
    assert '"""' not in safe
    L = []
    L.append("# JAH Blueprint demo - prints the schematic plan, verifies dimensions.")
    L.append("# Record %s - %s" % (rid, title.replace('"', "'")))
    L.append('plan = """')
    L.append(safe)
    L.append('"""')
    L.append("print(plan)")
    for label, value in stats:
        L.append('print("%s: %s")' % (label.replace('"', "'"), str(value).replace('"', "'")))
    L.append('print("OK: %s blueprint verified")' % rid)
    return "\n".join(L) + "\n"


# ---------------------------------------------------------------- record text

DISCLAIMER_PUB = ("Representative blueprint study compiled from standard construction "
                  "practice and public code requirements. The schematic plan is a study "
                  "aid, not a stamped construction document; verify all dimensions, loads, "
                  "and code compliance with a licensed professional before building.")

DISCLAIMER_SIG = ("Signature original design by the JAH Signature system. Clearly labeled "
                  "Signature-made and never presented as an authentic public record. "
                  "Schematic plan is a study aid, not a stamped construction document.")

SIG_LENS = ("Signature lens: re-imagined from first principles for durability, daylight, "
            "and honest materials - thicker envelopes, simpler spans, repairable details.")


def variant_note(vkey, vlabel):
    return {
        "compact": ("The %s edition is the lean, economical build: smaller spans, fewer "
                    "materials, fastest permit path - every space earns its footprint." % vlabel),
        "standard": ("The %s edition is the balanced reference build: the dimensions most "
                     "builders actually construct, with comfortable clearances throughout." % vlabel),
        "grand": ("The %s edition is the generous build: larger spans, taller volumes, and "
                  "room to grow - engineered for the same structural logic at full scale." % vlabel),
    }[vkey]


def ladder_of(vkey):
    return {"compact": (2, "foundations"), "standard": (5, "compounded"),
            "grand": (8, "advanced")}[vkey]
