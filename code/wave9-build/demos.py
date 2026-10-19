#!/usr/bin/env python3
"""Working demo archetype library for wave 9. Every demo is real, runnable,
stdlib-only Python that computes genuine results and prints an OK: marker.
Templates use __TOKEN__ replacement (no % / .format on outer templates)."""
import json

def _hdr(name, rid, group):
    return ('#!/usr/bin/env python3\n"""' + name.replace('"', "'") + ' — working demonstration.\n'
            'Record ' + rid + ' [' + group + ']. Property of Justin Addam Higgins (JAH).\n"""\n')

def _fill(tpl, **kw):
    for k, v in kw.items():
        tpl = tpl.replace('__' + k + '__', str(v))
    return tpl

# ---------------- DIY ----------------
def demo_project_planner(name, rid, group, P):
    mats = P.get('materials', [])
    mat_lines = "\n".join('    {"name": %s, "qty": %s, "cost": %.2f},' % (json.dumps(m[0]), json.dumps(m[1]), float(m[2])) for m in mats)
    return _fill(_hdr(name, rid, group) + '''\
MATERIALS = [
__MAT_LINES__
]
HOURS = __HOURS__
def main():
    total = sum(m["cost"] for m in MATERIALS)
    print("Project: __SAFE_NAME__")
    print("Materials (%d items):" % len(MATERIALS))
    for m in MATERIALS:
        print("  %-28s %-14s $%6.2f" % (m["name"], m["qty"], m["cost"]))
    print("  %-28s %-14s $%6.2f" % ("TOTAL", "", total))
    sessions = max(1, round(HOURS / 3))
    print("Time budget: %.1f h across %d session(s) of ~%.1f h" % (HOURS, sessions, HOURS / sessions))
    print("Material cost per build-hour: $%.2f" % (total / HOURS if HOURS else 0))
    assert total >= 0 and HOURS > 0
    print("OK: project plan computed — $%.2f materials, %.1f h" % (total, HOURS))
if __name__ == "__main__":
    main()
''', MAT_LINES=mat_lines, HOURS=P.get('hours', 4), SAFE_NAME=name.replace('"', "'"))

def demo_cutlist(name, rid, group, P):
    return _fill(_hdr(name, rid, group) + '''\
STOCK = __STOCK__  # inches per board
CUTS = __CUTS__
def main():
    cuts = sorted(CUTS, reverse=True)
    boards = []
    for c in cuts:
        placed = False
        for b in boards:
            if sum(b) + c <= STOCK:
                b.append(c); placed = True; break
        if not placed:
            boards.append([c])
    waste = sum(STOCK - sum(b) for b in boards)
    print("Cut list optimizer: %d cuts from %.0f-inch stock" % (len(cuts), STOCK))
    for i, b in enumerate(boards, 1):
        print("  board %d: %s (used %.0f, waste %.0f)" % (i, b, sum(b), STOCK - sum(b)))
    print("Boards needed: %d, total waste: %.0f in (%.1f%%)" % (len(boards), waste, 100 * waste / (len(boards) * STOCK)))
    assert all(sum(b) <= STOCK for b in boards)
    print("OK: cut list fits in %d boards" % len(boards))
if __name__ == "__main__":
    main()
''', STOCK=P.get('stock', 96), CUTS=json.dumps(P.get('cuts', [24, 24, 36, 12])))

def demo_wax_calc(name, rid, group, P):
    return _fill(_hdr(name, rid, group) + '''\
WAX_OZ = __WAX__; FRAG_PCT = __FRAG__; VESSELS = __VESSELS__
def main():
    frag_oz = WAX_OZ * FRAG_PCT / 100.0
    per_vessel = WAX_OZ / VESSELS
    print("Candle batch: %.1f oz wax across %d vessel(s)" % (WAX_OZ, VESSELS))
    print("Fragrance load %.1f%% -> %.2f oz fragrance oil" % (FRAG_PCT, frag_oz))
    print("Per vessel: %.2f oz wax" % per_vessel)
    print("Process: melt to 170F, add fragrance at 150F, pour at 130F, cure 48h")
    assert 0 < FRAG_PCT <= 10, "fragrance load out of safe range"
    print("OK: batch formula computed — %.2f oz fragrance" % frag_oz)
if __name__ == "__main__":
    main()
''', WAX=P.get('wax_oz', 16), FRAG=P.get('frag_pct', 8), VESSELS=P.get('vessels', 3))

def demo_lye_calc(name, rid, group, P):
    oils = P.get('oils', [('olive', 16, 0.134)])
    oil_lines = "\n".join('    {"name": %s, "oz": %.1f, "sap": %.4f},' % (json.dumps(o[0]), o[1], o[2]) for o in oils)
    return _fill(_hdr(name, rid, group) + '''\
# SAP values: NaOH oz per oz of oil. Lye = sum(oz*sap) * (1 - superfat/100).
OILS = [
__OIL_LINES__
]
SUPERFAT = __SUPERFAT__
def main():
    oil_oz = sum(o["oz"] for o in OILS)
    lye_full = sum(o["oz"] * o["sap"] for o in OILS)
    lye = lye_full * (1 - SUPERFAT / 100.0)
    water = oil_oz * 0.33
    print("Cold-process recipe (NaOH):")
    for o in OILS:
        print("  %-12s %5.1f oz" % (o["name"], o["oz"]))
    print("NaOH needed: %.2f oz (%.1f%% superfat)" % (lye, SUPERFAT))
    print("Distilled water: %.2f oz (33 percent of oils)" % water)
    print("SAFETY: add lye TO water, never reverse. Goggles + gloves. Cure 4-6 weeks.")
    assert lye > 0
    print("OK: lye calculation complete — %.2f oz NaOH" % lye)
if __name__ == "__main__":
    main()
''', OIL_LINES=oil_lines, SUPERFAT=P.get('superfat', 5))

def demo_bead_pattern(name, rid, group, P):
    return _fill(_hdr(name, rid, group) + '''\
ROWS, COLS = __ROWS__, __COLS__
COLORS = __COLORS__
def main():
    print("Bead pattern chart (%dx%d), colors %s:" % (ROWS, COLS, ",".join(COLORS)))
    for r in range(ROWS):
        line = "".join(COLORS[(r * 3 + c * 2) % len(COLORS)] for c in range(COLS))
        print("  row %2d: %s" % (r + 1, line))
    total = ROWS * COLS
    per = {}
    for c in COLORS:
        per[c] = sum(1 for r in range(ROWS) for cc in range(COLS) if COLORS[(r * 3 + cc * 2) % len(COLORS)] == c)
    print("Bead counts:", per, "total %d (+10%% spare = %d)" % (total, int(total * 1.1)))
    print("OK: pattern chart generated")
if __name__ == "__main__":
    main()
''', ROWS=P.get('rows', 8), COLS=P.get('cols', 12), COLORS=json.dumps(P.get('colors', ['A', 'B', 'C'])))

def demo_terrarium_calc(name, rid, group, P):
    return _fill(_hdr(name, rid, group) + '''\
VOL_L = __VOL__; PLANTS = __PLANTS__
def main():
    drainage_cm = 2.5
    soil_cm = max(4.0, VOL_L ** (1/3) * 1.2)
    water_ml = VOL_L * 30
    print("Terrarium build (%.1f L, %d plants):" % (VOL_L, PLANTS))
    print("  drainage layer: %.1f cm pebbles" % drainage_cm)
    print("  charcoal layer: 0.5 cm horticultural charcoal")
    print("  soil layer: %.1f cm" % soil_cm)
    print("  initial misting: %d ml distilled water" % water_ml)
    print("  ongoing: mist when soil surface dries; ventilate 10 min weekly")
    assert water_ml > 0
    print("OK: terrarium layers computed")
if __name__ == "__main__":
    main()
''', VOL=P.get('vol_l', 8), PLANTS=P.get('plants', 3))

def demo_aquarium_calc(name, rid, group, P):
    fish = P.get('fish', [('neon tetra', 1.0, 6)])
    fish_lines = "\n".join('    {"name": %s, "in": %.1f, "n": %d},' % (json.dumps(f[0]), f[1], f[2]) for f in fish)
    return _fill(_hdr(name, rid, group) + '''\
GALLONS = __GAL__
FISH = [
__FISH_LINES__
]
def main():
    inches = sum(f["in"] * f["n"] for f in FISH)
    print("Aquarium stocking (%.0f gal):" % GALLONS)
    for f in FISH:
        print("  %-16s %d x %.1f in" % (f["name"], f["n"], f["in"]))
    print("Total adult inches: %.1f (rule of thumb: 1 in per gallon -> %.0f max)" % (inches, GALLONS))
    pct = 100 * inches / GALLONS
    print("Stocking level: %.0f%% %s" % (pct, "OK" if pct <= 85 else "OVERSTOCKED — reduce"))
    print("Water change: 25%% weekly = %.1f gal" % (GALLONS * 0.25))
    assert pct <= 100, "overstocked"
    print("OK: stocking plan validated at %.0f%%" % pct)
if __name__ == "__main__":
    main()
''', GAL=P.get('gallons', 10), FISH_LINES=fish_lines)

def demo_frame_calc(name, rid, group, P):
    return _fill(_hdr(name, rid, group) + '''\
SECONDS = __SECS__; FPS = __FPS__
def main():
    frames = SECONDS * FPS
    shoot_min = frames * 0.75
    print("Stop-motion plan: %d s at %d fps" % (SECONDS, FPS))
    print("Frames required: %d" % frames)
    print("Estimated shoot time: %.1f h (45 s/frame)" % (shoot_min / 60))
    print("Storage: ~%.0f MB at 2 MB/frame" % (frames * 2))
    print("Tip: shoot in passes (background, main, foreground) for complex scenes.")
    assert frames > 0
    print("OK: %d frames planned" % frames)
if __name__ == "__main__":
    main()
''', SECS=P.get('seconds', 30), FPS=P.get('fps', 12))

def demo_schedule(name, rid, group, P):
    sessions = P.get('sessions', [('setup', 1.0), ('build', 2.0)])
    ses_lines = "\n".join('    {"name": %s, "h": %.1f},' % (json.dumps(s[0]), s[1]) for s in sessions)
    return _fill(_hdr(name, rid, group) + '''\
SESSIONS = [
__SES_LINES__
]
def main():
    t = 9.0
    print("Workshop schedule (start 9:00 AM):")
    for s in SESSIONS:
        h1, m1 = int(t), int((t % 1) * 60)
        t += s["h"]
        h2, m2 = int(t), int((t % 1) * 60)
        print("  %02d:%02d-%02d:%02d  %s (%.1f h)" % (h1, m1, h2, m2, s["name"], s["h"]))
    print("Total: %.1f h" % (t - 9.0))
    print("OK: schedule planned")
if __name__ == "__main__":
    main()
''', SES_LINES=ses_lines)

def demo_paint_coverage(name, rid, group, P):
    return _fill(_hdr(name, rid, group) + '''\
SQFT = __SQFT__; COATS = __COATS__; COVERAGE = 350
def main():
    gal = SQFT * COATS / COVERAGE
    buy = int(gal) + (1 if gal % 1 else 0)
    print("Paint estimate: %.0f sqft x %d coats" % (SQFT, COATS))
    print("Paint needed: %.2f gal -> buy %d gal" % (gal, buy))
    print("Primer: same area x 1 coat = %.2f gal" % (SQFT / COVERAGE))
    print("OK: paint quantity computed")
if __name__ == "__main__":
    main()
''', SQFT=P.get('sqft', 200), COATS=P.get('coats', 2))

# ---------------- GADGET ----------------
def demo_battery_life(name, rid, group, P):
    return _fill(_hdr(name, rid, group) + '''\
MAH = __MAH__; DRAW_MA = __DRAW__
def main():
    hours = MAH / DRAW_MA * 0.85
    print("Battery: %.0f mAh, draw %.0f mA" % (MAH, DRAW_MA))
    print("Estimated runtime: %.1f h (85%% usable capacity)" % hours)
    assert hours > 0
    print("OK: runtime estimate %.1f h" % hours)
if __name__ == "__main__":
    main()
''', MAH=P.get('mah', 10000), DRAW=P.get('ma', 500))

def demo_cost_breakdown(name, rid, group, P):
    parts = P.get('parts', [('case', 4.0), ('board', 12.0)])
    part_lines = "\n".join('    {"name": %s, "cost": %.2f},' % (json.dumps(p[0]), p[1]) for p in parts)
    return _fill(_hdr(name, rid, group) + '''\
PARTS = [
__PART_LINES__
]
def main():
    bom = sum(p["cost"] for p in PARTS)
    print("Bill of materials (%d parts):" % len(PARTS))
    for p in PARTS:
        print("  %-22s $%7.2f" % (p["name"], p["cost"]))
    print("BOM total: $%.2f" % bom)
    for vol, disc in ((1, 1.0), (100, 0.7), (1000, 0.5)):
        print("  at %4d units: $%7.2f/unit (volume pricing)" % (vol, bom * disc))
    print("Suggested retail (4x BOM): $%.2f" % (bom * 4))
    assert bom > 0
    print("OK: cost breakdown complete — BOM $%.2f" % bom)
if __name__ == "__main__":
    main()
''', PART_LINES=part_lines)

def demo_feasibility(name, rid, group, P):
    scores = P.get('scores', {'parts': 8, 'skill': 7, 'cost': 6, 'safety': 9})
    score_lines = "\n".join('    %s: %d,' % (json.dumps(k), v) for k, v in scores.items())
    return _fill(_hdr(name, rid, group) + '''\
SCORES = {
__SCORE_LINES__
}
def main():
    avg = sum(SCORES.values()) / len(SCORES)
    print("Feasibility assessment (1-10):")
    for k, v in SCORES.items():
        print("  %-10s %d/10 %s" % (k, v, "#" * v))
    verdict = "BUILD IT" if avg >= 7 else ("PROTOTYPE FIRST" if avg >= 5 else "RETHINK")
    print("Average: %.1f -> %s" % (avg, verdict))
    weakest = min(SCORES, key=SCORES.get)
    print("Improve first: %s (%d/10)" % (weakest, SCORES[weakest]))
    print("OK: feasibility scored %.1f" % avg)
if __name__ == "__main__":
    main()
''', SCORE_LINES=score_lines)

def demo_gear_ratio(name, rid, group, P):
    return _fill(_hdr(name, rid, group) + '''\
T_IN, T_OUT, RPM_IN = __TIN__, __TOUT__, __RPM__
def main():
    ratio = T_OUT / T_IN
    rpm_out = RPM_IN / ratio
    print("Gear pair: %dT -> %dT, input %.0f rpm" % (T_IN, T_OUT, RPM_IN))
    print("Ratio: %.2f:1  |  output: %.1f rpm  |  torque x%.2f" % (ratio, rpm_out, ratio))
    print("Direction: reversed (external gears)")
    assert ratio > 0
    print("OK: gear ratio %.2f:1 computed" % ratio)
if __name__ == "__main__":
    main()
''', TIN=P.get('t_in', 12), TOUT=P.get('t_out', 60), RPM=P.get('rpm', 100))

def demo_print_estimate(name, rid, group, P):
    return _fill(_hdr(name, rid, group) + '''\
# Print-time model: volumetric flow ~ 8 mm^3/s typical for 0.4mm nozzle PLA.
# ESTIMATES ONLY — actual time varies with printer, slicer, material, geometry.
VOL_CM3 = __VOL__; LAYER = __LAYER__; INFILL = __INFILL__
def main():
    vol_mm3 = VOL_CM3 * 1000 * (0.35 + 0.65 * INFILL / 100)
    secs = vol_mm3 / 8.0
    h = secs / 3600
    filament_g = VOL_CM3 * 1.24 * (0.35 + 0.65 * INFILL / 100)
    print("3D print estimate (DISCLOSED ESTIMATE, not a validated print job):")
    print("  part volume: %.1f cm^3, layer %.2f mm, infill %d%%" % (VOL_CM3, LAYER, INFILL))
    print("  estimated print time: %.1f h" % h)
    print("  estimated filament: %.0f g PLA" % filament_g)
    print("  suggested: 0.2mm layers, 3 walls, %d%% infill, brim if small base" % INFILL)
    print("  unmodeled: supports add 15-40%%; wall thickness, nozzle temp, printer motion vary")
    assert h > 0
    print("OK: print estimate %.1f h (estimate)" % h)
if __name__ == "__main__":
    main()
''', VOL=P.get('vol_cm3', 50), LAYER=P.get('layer', 0.2), INFILL=P.get('infill', 20))

def demo_power_budget(name, rid, group, P):
    comps = P.get('comps', [('mcu', 0.5), ('leds', 2.0)])
    comp_lines = "\n".join('    {"name": %s, "w": %.2f},' % (json.dumps(c[0]), c[1]) for c in comps)
    return _fill(_hdr(name, rid, group) + '''\
COMPS = [
__COMP_LINES__
]
def main():
    total = sum(c["w"] for c in COMPS)
    print("Power budget:")
    for c in COMPS:
        print("  %-14s %5.2f W" % (c["name"], c["w"]))
    print("Total: %.2f W" % total)
    wh = total * 8
    print("8-hour energy: %.1f Wh -> battery >= %.0f Wh (20%% margin)" % (wh, wh * 1.2))
    print("OK: power budget %.2f W" % total)
if __name__ == "__main__":
    main()
''', COMP_LINES=comp_lines)

# ---------------- MACHINE ----------------
def demo_marble_physics(name, rid, group, P):
    return _fill(_hdr(name, rid, group) + '''\
import math
DROP_M = __DROP__; G = 9.81
def main():
    v = math.sqrt(2 * G * DROP_M)
    t = math.sqrt(2 * DROP_M / G)
    print("Marble drop: %.2f m" % DROP_M)
    print("Theoretical speed at bottom: %.2f m/s (frictionless)" % v)
    print("Fall time: %.2f s" % t)
    print("Real speed ~70-80%% of theory (rolling + track friction)")
    print("Loop-the-loop: for r=0.1m need v_top > %.2f m/s" % math.sqrt(G * 0.1))
    assert v > 0
    print("OK: drop physics computed — v=%.2f m/s" % v)
if __name__ == "__main__":
    main()
''', DROP=P.get('drop_m', 1.0))

def demo_domino_timing(name, rid, group, P):
    return _fill(_hdr(name, rid, group) + '''\
N = __N__; SPACING_M = __SPACING__
def main():
    wave = 1.2  # m/s empirical topple wave
    length = N * SPACING_M
    t = length / wave
    print("Domino chain: %d dominoes, %.1f cm spacing" % (N, SPACING_M * 100))
    print("Chain length: %.1f m" % length)
    print("Topple wave ~%.1f m/s -> run time ~%.1f s" % (wave, t))
    print("Setup time estimate: %d min at 20/min" % (N // 20))
    assert t > 0
    print("OK: chain timing ~%.1f s fall, %d min setup" % (t, N // 20))
if __name__ == "__main__":
    main()
''', N=P.get('count', 100), SPACING=P.get('spacing_m', 0.05))

def demo_pendulum(name, rid, group, P):
    return _fill(_hdr(name, rid, group) + '''\
import math
L = __LEN__; G = 9.81
def main():
    T = 2 * math.pi * math.sqrt(L / G)
    print("Pendulum length %.2f m -> period %.2f s" % (L, T))
    print("Beats per minute: %.1f" % (60 / T))
    print("Seconds pendulum: L=%.3f m gives T=2.00 s" % (G / math.pi ** 2))
    assert T > 0
    print("OK: period %.2f s" % T)
if __name__ == "__main__":
    main()
''', LEN=P.get('length_m', 1.0))

def demo_stability(name, rid, group, P):
    return _fill(_hdr(name, rid, group) + '''\
import math
BASE = __BASE__; HEIGHT = __HEIGHT__
def main():
    tip_deg = math.degrees(math.atan((BASE / 2) / (HEIGHT / 2)))
    print("Tower: base %.2f m, height %.2f m" % (BASE, HEIGHT))
    print("Tip-over angle: %.1f degrees from vertical" % tip_deg)
    print("Rule: keep center of mass over middle third; tip angle > 10 deg is comfortable")
    print("Wind note: double the base or guy-wire above 3 m outdoors")
    assert tip_deg > 0
    print("OK: stability angle %.1f deg" % tip_deg)
if __name__ == "__main__":
    main()
''', BASE=P.get('base_m', 0.5), HEIGHT=P.get('height_m', 2.0))

def demo_energy_chain(name, rid, group, P):
    steps = P.get('steps', [('drop', 0.9), ('lever', 0.8)])
    step_lines = "\n".join('    {"name": %s, "eff": %.2f},' % (json.dumps(s[0]), s[1]) for s in steps)
    return _fill(_hdr(name, rid, group) + '''\
STEPS = [
__STEP_LINES__
]
def main():
    e = 1.0
    print("Energy chain (%d transfers):" % len(STEPS))
    for s in STEPS:
        e *= s["eff"]
        print("  %-16s eff %.0f%% -> cumulative %.1f%%" % (s["name"], s["eff"]*100, e*100))
    print("Overall efficiency: %.1f%%" % (e * 100))
    print("Lesson: every transfer loses energy — few links beat clever links.")
    assert 0 < e <= 1
    print("OK: chain efficiency %.1f%%" % (e * 100))
if __name__ == "__main__":
    main()
''', STEP_LINES=step_lines)

# ---------------- MONEY ----------------
def demo_valuation(name, rid, group, P):
    items = P.get('items', [('item A', 20, 40)])
    item_lines = "\n".join('    {"name": %s, "lo": %.0f, "hi": %.0f},' % (json.dumps(i[0]), i[1], i[2]) for i in items)
    return _fill(_hdr(name, rid, group) + '''\
ITEMS = [
__ITEM_LINES__
]
def main():
    lo = sum(i["lo"] for i in ITEMS); hi = sum(i["hi"] for i in ITEMS)
    print("Collection valuation (%d items):" % len(ITEMS))
    for i in ITEMS:
        print("  %-24s $%6.0f - $%6.0f" % (i["name"], i["lo"], i["hi"]))
    print("Range total: $%.0f - $%.0f (mid $%.0f)" % (lo, hi, (lo + hi) / 2))
    print("Note: condition moves items within range; insurance uses high end.")
    assert hi >= lo
    print("OK: valuation range $%.0f-$%.0f" % (lo, hi))
if __name__ == "__main__":
    main()
''', ITEM_LINES=item_lines)

def demo_compound(name, rid, group, P):
    return _fill(_hdr(name, rid, group) + '''\
P0 = __P0__; R = __R__; YRS = __YRS__
def main():
    print("Compound growth: $%.0f at %.1f%% for %d years" % (P0, R * 100, YRS))
    bal = P0
    for y in range(1, YRS + 1):
        bal *= (1 + R)
        if y % 5 == 0 or y == YRS:
            print("  year %2d: $%9.0f" % (y, bal))
    print("Final: $%.0f (%.1fx)" % (bal, bal / P0))
    print("Rule of 72: doubles every %.1f years" % (72 / (R * 100)))
    assert bal > P0
    print("OK: compound projection $%.0f" % bal)
if __name__ == "__main__":
    main()
''', P0=P.get('principal', 1000), R=P.get('rate', 0.07), YRS=P.get('years', 10))

def demo_unit_price(name, rid, group, P):
    opts = P.get('options', [('small', 5.0, 10), ('bulk', 18.0, 50)])
    opt_lines = "\n".join('    {"name": %s, "price": %.2f, "qty": %.0f},' % (json.dumps(o[0]), o[1], o[2]) for o in opts)
    return _fill(_hdr(name, rid, group) + '''\
OPTS = [
__OPT_LINES__
]
def main():
    print("Unit-price comparison:")
    best = None
    for o in OPTS:
        unit = o["price"] / o["qty"]
        print("  %-12s $%6.2f / %3.0f = $%.3f each" % (o["name"], o["price"], o["qty"], unit))
        if best is None or unit < best[1]:
            best = (o["name"], unit)
    print("Best value: %s at $%.3f/unit" % best)
    print("Caveat: only a bargain if you will use it all.")
    print("OK: best value is %s" % best[0])
if __name__ == "__main__":
    main()
''', OPT_LINES=opt_lines)

def demo_revenue_model(name, rid, group, P):
    return _fill(_hdr(name, rid, group) + '''\
PRICE = __PRICE__; UNITS = __UNITS__; UNIT_COST = __COST__
def main():
    rev = PRICE * UNITS
    cogs = UNIT_COST * UNITS
    gross = rev - cogs
    margin = gross / rev * 100
    print("Revenue model: %d units at $%.2f" % (UNITS, PRICE))
    print("Revenue: $%.0f | COGS: $%.0f | Gross: $%.0f (%.0f%% margin)" % (rev, cogs, gross, margin))
    breakeven = 5000 / (PRICE - UNIT_COST) if PRICE > UNIT_COST else float('inf')
    print("Units to cover $5000 fixed costs: %.0f" % breakeven)
    assert gross > 0
    print("OK: model shows $%.0f gross" % gross)
if __name__ == "__main__":
    main()
''', PRICE=P.get('price', 29), UNITS=P.get('units', 100), COST=P.get('cost', 12))

def demo_grade_score(name, rid, group, P):
    crit = P.get('criteria', {'condition': 8, 'rarity': 7, 'demand': 6})
    crit_lines = "\n".join('    %s: %d,' % (json.dumps(k), v) for k, v in crit.items())
    return _fill(_hdr(name, rid, group) + '''\
CRIT = {
__CRIT_LINES__
}
def main():
    score = sum(CRIT.values()) / len(CRIT)
    print("Desirability score (1-10):")
    for k, v in CRIT.items():
        print("  %-12s %d/10" % (k, v))
    label = "highly desirable" if score >= 8 else ("solid" if score >= 6 else "common")
    print("Overall: %.1f/10 — %s" % (score, label))
    print("OK: scored %.1f" % score)
if __name__ == "__main__":
    main()
''', CRIT_LINES=crit_lines)

DEMOS = {
 'project_planner': demo_project_planner, 'cutlist': demo_cutlist,
 'wax_calc': demo_wax_calc, 'lye_calc': demo_lye_calc,
 'bead_pattern': demo_bead_pattern, 'terrarium_calc': demo_terrarium_calc,
 'aquarium_calc': demo_aquarium_calc, 'frame_calc': demo_frame_calc,
 'schedule': demo_schedule, 'paint_coverage': demo_paint_coverage,
 'battery_life': demo_battery_life, 'cost_breakdown': demo_cost_breakdown,
 'feasibility': demo_feasibility, 'gear_ratio': demo_gear_ratio,
 'print_estimate': demo_print_estimate, 'power_budget': demo_power_budget,
 'marble_physics': demo_marble_physics, 'domino_timing': demo_domino_timing,
 'pendulum': demo_pendulum, 'stability': demo_stability,
 'energy_chain': demo_energy_chain, 'valuation': demo_valuation,
 'compound': demo_compound, 'unit_price': demo_unit_price,
 'revenue_model': demo_revenue_model, 'grade_score': demo_grade_score,
}
