#!/usr/bin/env python3
"""Build the Hydrology field databases for JAH Databases (field #14, taxonomy order).

Verified 2026-10-17: NO database covers hydrology as a discipline.
- 'water-systems' (10,001 records): water cycles, treatment, infrastructure,
  conservation - utility engineering, not the science of water.
- 'oceanography' (10,000 records): ocean processes.
- 'rivers' (56 records): short river entries.
- 'climatology' (34 records, field #12): covers the water cycle at climate
  scale - not discipline machinery.
- 'atmospheric-science' (36 records, field #13): precipitation physics,
  cloud processes - not surface/groundwater hydrology.
- occupation DBs ('hydrologists', 'hydrologic-technicians',
  'water-resource-specialists', 'water-wastewater-engineers'): 4-5-record
  occupation cards.

So this build creates two NEW databases:

  hydrology             — The Hydrology Database
                          (public-harvest: real, fact-checked hydrology)
  hydrology-signature   — The Hydrology Signature Database
                          (his original Signature interpretation;
                          src signature, titles suffixed
                          " (Signature Edition)", never presented
                          as authentic public record)

36 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

Every record: description + how-it-works + key points + requirements +
standards + citations + working demonstration code (real, runnable,
stdlib-only Python; machine-executed OK).

Never the words "bat belt" anywhere. No website references. No Facebook.
"""
import importlib.util
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = "/home/hatch/workspace/jah-databases"
SHARD = "/home/hatch/workspace/jah-databases-data-1"
SHARD_BASE = "https://justinahiggins614-cmyk.github.io/jah-databases-data-1"
TEMPLATE = os.path.join(REPO, "db", "public-synthetic-intelligence", "index.html")

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
# Whole-system dedupe gate against the FRESH data/dedupe/exact/ index in the
# main repo (rebuilt 2026-10-17: 8,590,108 records, 256 shards).
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_hydrology import ENTRIES, SIG_TAIL

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature interpretation of hydrology: "
                "clearly labeled Signature-made, never presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked hydrology: what hydrology is; the water "
                "budget equation; watersheds and drainage basins; measuring precipitation; "
                "infiltration and soil water; evapotranspiration; measuring streamflow; the "
                "rating curve; the hydrograph; rainfall-runoff and the unit hydrograph; soil "
                "moisture and the vadose zone; Darcy's law; aquifers, wells, and the water "
                "table; groundwater recharge and discharge; springs and seeps; snow hydrology; "
                "glacier mass balance; lakes and reservoirs; wetlands hydrology; flood-"
                "frequency analysis; drought hydrology; water quality in rivers; Manning's "
                "equation; sediment transport; urban hydrology; stormwater detention design; "
                "reservoir operation and yield; hydropower hydrology; irrigation hydrology; "
                "groundwater modeling; karst hydrology; tracer and isotope hydrology; "
                "ecohydrology and environmental flows; flood inundation modeling; hydrologic "
                "forecasting; frontiers of hydrology, organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations (what hydrology is, "
              "the water budget, watersheds, precipitation measurement, infiltration, "
              "evapotranspiration, streamflow measurement, the rating curve) -> Compounded "
              "(the hydrograph, unit hydrograph, the vadose zone, Darcy's law, aquifers and "
              "wells, recharge and discharge, springs, snow hydrology, glaciers, lakes and "
              "reservoirs, wetlands, flood frequency, drought, water quality) -> Advanced "
              "(Manning's equation, sediment transport, urban hydrology, detention design, "
              "reservoir yield, hydropower, irrigation, groundwater modeling, karst, "
              "isotopes, ecohydrology, inundation modeling, forecasting, frontiers).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search Darcy, Manning, hydrograph, unit hydrograph, SWE, SPI, Theis, SWMM...",
        "chat_ph": "Ask about hydrology...",
        "archive_blurb": ("Seeded %s hydrology records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled structural hydrology studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about hydrology - from water budgets and hydrographs to Darcy's law, Manning's equation, and flood forecasting." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "hydrology-study", "gen_demo_kind": "hydrology-demo",
        "source": source,
    }

CIT_PUB = "Hydrology (peer-reviewed literature and standard textbooks)."
CIT_SIG = CIT_PUB + " " + SIG_TAIL

DBCFG = {}
DBCFG["hydrology"] = _cfg(
    "hydrology", "The Hydrology Database",
    "Real, fact-checked hydrology: the water budget, watersheds, precipitation, infiltration, "
    "evapotranspiration, streamflow, the rating curve, hydrographs, the unit hydrograph, the "
    "vadose zone, Darcy's law, aquifers and wells, recharge, springs, snow, glaciers, lakes, "
    "wetlands, flood frequency, drought, water quality, Manning's equation, sediment, urban "
    "hydrology, detention, reservoir yield, hydropower, irrigation, groundwater modeling, karst, "
    "isotopes, ecohydrology, inundation modeling, forecasting, and frontiers.",
    "hydrology record", "JAH-HYD-", "JAH Hydrology Archivist",
    "hydrology archivist - the water budget equation, watersheds and drainage basins, "
    "precipitation measurement, infiltration and soil water, evapotranspiration, streamflow "
    "measurement, the rating curve, hydrographs, the unit hydrograph, the vadose zone, "
    "Darcy's law, aquifers and wells, recharge and discharge, springs and seeps, snow "
    "hydrology, glacier mass balance, lakes and reservoirs, wetlands, flood-frequency "
    "analysis, drought hydrology, water quality, Manning's equation, sediment transport, "
    "urban hydrology, detention design, reservoir yield, hydropower, irrigation, groundwater "
    "modeling, karst, tracer isotopes, ecohydrology, inundation modeling, hydrologic "
    "forecasting; teaching progressively along the ladder from foundations through compounded "
    "to advanced; answers from many angles - definition, example, analogy, application, "
    "history, math, how-to - using only the system's own archive data",
    CIT_PUB, "public")
DBCFG["hydrology-signature"] = _cfg(
    "hydrology-signature", "The Hydrology Signature Database",
    "His original Signature interpretation of hydrology: the full ladder from water budgets "
    "and hydrographs to Darcy's law, Manning's equation, and flood forecasting, reframed "
    "as Signature science. Clearly labeled Signature-made, never presented as authentic "
    "public record.",
    "hydrology record", "JAH-HYDS-", "JAH Hydrology Archivist (Signature)",
    "hydrology archivist - Signature editions: his original Signature interpretation "
    "of hydrology, clearly labeled Signature-made and never presented as authentic "
    "public record; teaches progressively along the ladder from foundations through "
    "compounded to advanced; answers from many angles - definition, example, analogy, "
    "application, history, math, how-to - using only the system's own archive data",
    CIT_SIG, "signature")

base.DBCFG = DBCFG

# ---------------------------------------------------------------- demos
# Every demo is real, runnable, stdlib-only Python performing the actual
# hydrologic calculation for its record. All are machine-executed by main().

_PREAMBLE = """import math
import re
"""

def _wrap(name, rid, group, body):
    return (base._hdr(name, rid, group) + _PREAMBLE + body.replace("NAME", json.dumps(name)))

def demo_hydro_branches(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
BRANCHES = {
    "surface-water hydrology": "rivers, lakes, floods - water you can see",
    "groundwater hydrology": "aquifers, wells, springs - water underground",
    "snow and ice hydrology": "snowpacks and glaciers - water in storage",
    "urban hydrology": "pavement, pipes, stormwater - water in cities",
    "ecohydrology": "water and life shaping each other",
    "water-resources hydrology": "reservoirs, yield, allocation - water decided",
}
def main():
    assert len(BRANCHES) == 6
    assert BRANCHES["groundwater hydrology"].startswith("aquifers")
    for branch, focus in BRANCHES.items():
        print("%-24s -> %s" % (branch, focus))
    print("plus observation (gauges, wells, snow pillows) and models that turn it into forecasts")
    print("rule: the water budget P = ET + Q + dS binds every branch - mass is always conserved")
    print("OK: %s mapped the branches" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_water_budget(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def budget(P_mm, ET_mm, Q_mm):
    # P = ET + Q + dS  ->  dS = P - ET - Q
    return P_mm - ET_mm - Q_mm
def main():
    dS = budget(1200.0, 700.0, 450.0)
    assert abs(dS - 50.0) < 1e-9, dS
    assert abs(budget(1200.0, 700.0, 500.0) - 0.0) < 1e-9
    # long-term mean: dS -> 0, so mean Q = P - ET
    Qmean = 1200.0 - 700.0
    assert abs(Qmean - 500.0) < 1e-9
    print("basin: P=1200 mm, ET=700 mm, Q=450 mm -> storage change dS = %+.0f mm" % dS)
    print("long-term mean streamflow = P - ET = %.0f mm/yr" % Qmean)
    print("global: ~47,000 km3/yr rides the atmosphere from ocean to land - the world's river supply")
    print("rule: a budget that will not close is pointing at hidden water - find it")
    print("OK: %s balanced the basin" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_watershed(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def strahler(joins):
    # joins: list of (order_a, order_b) for each confluence, processed upstream-first
    out = []
    for a, b in joins:
        out.append(a + 1 if a == b else max(a, b))
    return out
def drainage_density_km_per_km2(total_length_km, area_km2):
    return total_length_km / area_km2
def main():
    # headwaters (1,1)->2 ; (2,1)->2 ; (2,2)->3 ; (3,1)->3
    orders = strahler([(1, 1), (2, 1), (2, 2), (3, 1)])
    assert orders == [2, 2, 3, 3], orders
    dd_clay = drainage_density_km_per_km2(180.0, 60.0)
    dd_sand = drainage_density_km_per_km2(30.0, 60.0)
    assert abs(dd_clay - 3.0) < 1e-9 and abs(dd_sand - 0.5) < 1e-9
    assert dd_clay > dd_sand
    print("network orders after joins: %s" % orders)
    print("drainage density: clay basin %.1f km/km2 vs sand basin %.1f km/km2" % (dd_clay, dd_sand))
    print("high density = impermeable geology; low density = permeable")
    print("rule: Strahler - equal orders join to order+1, unequal keep the max")
    print("OK: %s delineated the basin" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_precip_gauge(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def tipping_bucket_mm(tips, mm_per_tip=0.2):
    return tips * mm_per_tip
def thiessen_avg(depths_mm, areas_km2):
    return sum(d * a for d, a in zip(depths_mm, areas_km2)) / sum(areas_km2)
def main():
    storm = tipping_bucket_mm(137)
    assert abs(storm - 27.4) < 1e-9, storm
    p = thiessen_avg([27.4, 41.0, 18.5], [12.0, 20.0, 8.0])
    assert abs(p - 32.42) < 0.01, p
    simple = sum([27.4, 41.0, 18.5]) / 3.0
    assert abs(simple - 28.97) < 0.01
    print("137 tips x 0.2 mm = %.1f mm at the gauge" % storm)
    print("Thiessen basin average: %.2f mm (simple mean would say %.2f mm)" % (p, simple))
    print("weight by area, not by gauge count - each gauge speaks for its polygon")
    print("rule: wind undercatch is the dominant error - shield gauges in snow country")
    print("OK: %s averaged the storm" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_infiltration(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def horton(t_h, f0, fc, k):
    return fc + (f0 - fc) * math.exp(-k * t_h)
def cumulative(t_h, f0, fc, k, n=200):
    dt = t_h / n
    return sum(horton((i + 0.5) * dt, f0, fc, k) * dt for i in range(n))
def main():
    f0, fc, k = 60.0, 8.0, 2.5
    f_start = horton(0.0, f0, fc, k)
    f_late = horton(4.0, f0, fc, k)
    assert abs(f_start - 60.0) < 1e-9
    assert abs(f_late - 8.0) < 0.1, f_late
    F = cumulative(2.0, f0, fc, k)
    assert 25.0 < F < 60.0, F
    print("Horton: %.0f mm/h at t=0 decaying to %.1f mm/h at t=4 h" % (f_start, f_late))
    print("cumulative infiltration in 2 h: %.1f mm" % F)
    print("rain harder than the curve allows -> Hortonian overland flow -> flash flood")
    print("rule: dry soil drinks fast, wet soil sips - capacity decays exponentially")
    print("OK: %s timed the soaking" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_evapotranspiration(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def et0_fao56(T_C, RH_pct, u2_ms, Rs_MJ, z_m=100.0, lat_rad=0.7):
    # FAO-56 Penman-Monteith reference ET, mm/day (daily step)
    es = 0.6108 * math.exp(17.27 * T_C / (T_C + 237.3))
    ea = es * RH_pct / 100.0
    delta = 4098.0 * es / (T_C + 237.3) ** 2
    P = 101.3 * ((293.0 - 0.0065 * z_m) / 293.0) ** 5.26
    gamma = 0.000665 * P
    Rn = 0.77 * Rs_MJ - 2.0     # simplified net radiation proxy
    G = 0.0
    num = 0.408 * delta * (Rn - G) + gamma * 900.0 / (T_C + 273.0) * u2_ms * (es - ea)
    den = delta + gamma * (1.0 + 0.34 * u2_ms)
    return num / den
def main():
    et = et0_fao56(25.0, 60.0, 2.0, 25.0)
    assert 3.0 < et < 9.0, et
    et_windy = et0_fao56(25.0, 60.0, 5.0, 25.0)
    assert et_windy > et, (et, et_windy)
    et_dry = et0_fao56(25.0, 30.0, 2.0, 25.0)
    assert et_dry > et, (et, et_dry)
    print("reference ET0 (25 C, RH 60%%, 2 m/s, Rs 25 MJ/m2/d): %.2f mm/day" % et)
    print("windier (5 m/s): %.2f mm/day; drier air (RH 30%%): %.2f mm/day" % (et_windy, et_dry))
    print("crops: ETc = ET0 x Kc(stage); irrigation dose = ETc - effective rain")
    print("rule: energy supplies the latent heat, dry wind carries the vapor away")
    print("OK: %s ran the sky-pump" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_streamflow(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def midsection_Q(panels):
    # panels: (width_m, depth_m, velocity_m_s)
    return sum(w * d * v for w, d, v in panels)
def main():
    panels = [(2.0, 0.8, 0.9), (2.0, 1.4, 1.3), (2.0, 1.6, 1.5),
              (2.0, 1.2, 1.1), (2.0, 0.6, 0.5)]
    Q = midsection_Q(panels)
    assert abs(Q - 13.12) < 0.01, Q
    A = sum(w * d for w, d, v in panels)
    Vmean = Q / A
    assert abs(A - 11.2) < 1e-9 and abs(Vmean - 1.171) < 0.005, (A, Vmean)
    print("5 panels: area %.1f m2, discharge Q = %.2f m3/s, mean velocity %.2f m/s" % (A, Q, Vmean))
    print("fastest at mid-channel near the surface; near zero at banks and bed")
    print("rule: slice the section, measure each panel, sum - Q = sum(w d v)")
    print("OK: %s gauged the river" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_rating_curve(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def fit_rating(h, Q, h0):
    # log-log fit of Q = a (h - h0)^b
    xs = [math.log(hh - h0) for hh in h]
    ys = [math.log(q) for q in Q]
    n = len(h)
    mx, my = sum(xs) / n, sum(ys) / n
    b = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    a = math.exp(my - b * mx)
    return a, b
def q_rating(hh, a, b, h0):
    return a * (hh - h0) ** b
def main():
    a_true, b_true, h0 = 12.5, 2.1, 0.3
    hs = [0.5, 0.8, 1.2, 1.8, 2.6, 3.5]
    Qs = [q_rating(hh, a_true, b_true, h0) for hh in hs]
    a, b = fit_rating(hs, Qs, h0)
    assert abs(a - a_true) / a_true < 0.01, (a, a_true)
    assert abs(b - b_true) / b_true < 0.01, (b, b_true)
    q2m = q_rating(2.0, a, b, h0)
    print("fitted rating: Q = %.2f (h - %.1f)^%.2f" % (a, h0, b))
    print("stage 2.0 m -> discharge %.1f m3/s" % q2m)
    print("scour lowers the curve, fill raises it - remeasure, or the record lies")
    print("rule: log-log turns the power law into a straight line - fit that")
    print("OK: %s built the rating" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hydrograph(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def separate_baseflow(Q, i_rise, i_peak, i_end):
    # straight-line separation from rise point to end point
    n = len(Q)
    base = []
    for i in range(n):
        if i <= i_rise:
            base.append(Q[i_rise])
        elif i >= i_end:
            base.append(Q[i_end])
        else:
            f = (i - i_rise) / (i_end - i_rise)
            base.append(Q[i_rise] + f * (Q[i_end] - Q[i_rise]))
    return base
def main():
    Q = [5.0, 5.2, 6.0, 12.0, 28.0, 45.0, 38.0, 25.0, 15.0, 9.0, 6.5, 5.8, 5.4]
    dt_h = 1.0
    base = separate_baseflow(Q, 1, 5, 10)
    direct = [max(0.0, q - b) for q, b in zip(Q, base)]
    assert all(d >= 0.0 for d in direct)
    vol_direct = sum(direct) * dt_h * 3600.0
    area_km2 = 50.0
    runoff_mm = vol_direct / (area_km2 * 1e6) * 1000.0
    rain_mm = 40.0
    coeff = runoff_mm / rain_mm
    assert 0.05 < coeff < 0.9, coeff
    # recession constant from falling limb (hours 6..9, positive direct runoff)
    import math as m
    ks = []
    for i in range(6, 9):
        a, b = direct[i], direct[i + 1]
        if a > 0 and b > 0:
            ks.append(-m.log(b / a) / dt_h)
    k = sum(ks) / len(ks)
    assert k > 0
    print("peak %.0f m3/s; direct-runoff volume %.0f m3 -> %.1f mm over %d km2" %
          (max(Q), vol_direct, runoff_mm, area_km2))
    print("runoff coefficient %.2f; recession constant k = %.3f /h" % (coeff, k))
    print("the recession constant fingerprints the feeding aquifer")
    print("rule: peel baseflow off first - the storm's signature is what remains")
    print("OK: %s read the pulse" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_unit_hydrograph(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def scs_runoff_mm(P_mm, CN):
    S = 25400.0 / CN - 254.0
    Ia = 0.2 * S
    if P_mm <= Ia:
        return 0.0
    return (P_mm - Ia) ** 2 / (P_mm - Ia + S)
def convolve(excess, uh):
    n = len(excess) + len(uh) - 1
    out = [0.0] * n
    for i, e in enumerate(excess):
        for j, u in enumerate(uh):
            out[i + j] += e * u
    return out
def main():
    r1 = scs_runoff_mm(80.0, 75.0)
    assert abs(r1 - 26.92) < 0.05, r1
    assert scs_runoff_mm(10.0, 75.0) == 0.0   # below initial abstraction
    uh_raw = [0.0, 12.0, 30.0, 22.0, 10.0, 4.0, 1.0]  # m3/s per 10 mm (shape)
    # normalize so the ordinates integrate to exactly 10 mm over the basin
    area_km2, dt_h = 50.0, 1.0
    target_vol = 10.0 / 1000.0 * area_km2 * 1e6
    uh = [x * target_vol / (sum(uh_raw) * dt_h * 3600.0) for x in uh_raw]
    q1 = convolve([10.0 / 10.0], uh)
    q2 = convolve([20.0 / 10.0], uh)
    assert abs(max(q2) - 2.0 * max(q1)) < 1e-9   # proportionality
    vol = sum(q1) * dt_h * 3600.0
    depth = vol / (area_km2 * 1e6) * 1000.0
    assert abs(depth - 10.0) < 0.05, depth        # volume conserved
    print("SCS: 80 mm rain on CN75 -> %.1f mm effective" % r1)
    print("unit hydrograph peak %.0f m3/s per 10 mm; double the rain -> double the peak" % max(q1))
    print("convolution conserves volume: %.1f mm in = %.1f mm out" % (10.0, depth))
    print("rule: proportionality + superposition - the basin as a linear system")
    print("OK: %s convolved the storm" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_vadose(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def van_genuchten(h_cm, thr=0.08, ths=0.43, alpha=0.036, n=1.56):
    # water content at suction h (cm, positive); m = 1 - 1/n
    m = 1.0 - 1.0 / n
    Se = 1.0 / (1.0 + (alpha * h_cm) ** n) ** m
    return thr + (ths - thr) * Se
def main():
    th_sat = van_genuchten(0.0)
    assert abs(th_sat - 0.43) < 1e-9, th_sat
    th_100 = van_genuchten(100.0)
    th_1000 = van_genuchten(1000.0)
    assert th_sat > th_100 > th_1000 > 0.08, (th_100, th_1000)
    paw = van_genuchten(330.0) - van_genuchten(15000.0)  # field capacity - wilting point
    assert 0.05 < paw < 0.30, paw
    print("theta: saturated %.2f, at 100 cm suction %.2f, at 1000 cm %.2f" % (th_sat, th_100, th_1000))
    print("plant-available water (FC - WP): %.2f m3/m3" % paw)
    print("the retention curve is the soil's master characteristic - measure it, don't guess it")
    print("rule: suction holds the water, gravity pulls it - Richards' equation keeps score")
    print("OK: %s profiled the unsaturated zone" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_darcy(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def darcy_Q(K_m_d, A_m2, dh_m, dl_m):
    return K_m_d * A_m2 * (dh_m / dl_m)   # magnitude; flow runs down-gradient
def pore_velocity(v_darcy_m_d, porosity):
    return v_darcy_m_d / porosity
def main():
    K, A, dh, dl = 25.0, 2000.0, 4.0, 1000.0
    Q = darcy_Q(K, A, dh, dl)
    assert abs(Q - 200.0) < 1e-9, Q
    v = Q / A
    vp = pore_velocity(v, 0.25)
    assert abs(v - 0.1) < 1e-9 and abs(vp - 0.4) < 1e-9, (v, vp)
    days_per_km = 1000.0 / vp
    assert abs(days_per_km - 2500.0) < 1e-6
    print("K=25 m/d, A=2000 m2, gradient 4/1000 -> Q = %.0f m3/d" % Q)
    print("Darcy flux %.2f m/d; pore velocity %.2f m/d -> 1 km takes %.0f days" % (v, vp, days_per_km))
    print("plumes travel at pore velocity - meters per year is why pollution is generational")
    print("rule: Q = K A (dh/dl), downhill in head, always")
    print("OK: %s timed the seepage" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_theis(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
EULER = 0.5772156649015329
def W(u):
    # Theis well function, series for small u, continued approximation
    if u <= 1.0:
        s, term, k = -EULER - math.log(u), u, 1
        while abs(term) > 1e-12:
            s += term
            k += 1
            term = ((-1) ** (k + 1)) * (u ** k) / (k * math.factorial(k))
        return s
    # asymptotic for larger u
    return math.exp(-u) / u * (1.0 - 1.0 / u)
def theis_drawdown(Q_m3_d, T_m2_d, S, r_m, t_d):
    u = r_m * r_m * S / (4.0 * T_m2_d * t_d)
    return Q_m3_d / (4.0 * math.pi * T_m2_d) * W(u)
def main():
    assert abs(W(1.0) - 0.219383934) < 1e-6, W(1.0)
    s = theis_drawdown(1200.0, 500.0, 0.001, 100.0, 1.0)
    assert s > 0
    s_late = theis_drawdown(1200.0, 500.0, 0.001, 100.0, 30.0)
    assert s_late > s   # cone keeps expanding
    print("W(1) = %.6f (textbook value)" % W(1.0))
    print("drawdown at 100 m: day 1 = %.2f m, day 30 = %.2f m" % (s, s_late))
    print("early water comes from storage near the well; later the cone hunts for boundaries")
    print("rule: match the data to the type curve - T and S fall out of the fit")
    print("OK: %s pumped the test" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_recharge(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def wtf_recharge_mm(rise_m, Sy):
    return rise_m * Sy * 1000.0
def chloride_recharge_mm(P_mm, Cl_rain_mg_L, Cl_gw_mg_L):
    return P_mm * Cl_rain_mg_L / Cl_gw_mg_L
def main():
    R_wtf = wtf_recharge_mm(1.2, 0.15)
    assert abs(R_wtf - 180.0) < 1e-9, R_wtf
    R_cl = chloride_recharge_mm(800.0, 2.0, 20.0)
    assert abs(R_cl - 80.0) < 1e-9, R_cl
    print("water-table rise 1.2 m x Sy 0.15 -> recharge %.0f mm" % R_wtf)
    print("chloride mass balance: 800 mm rain, 2->20 mg/L -> recharge %.0f mm" % R_cl)
    print("two independent methods, same order of magnitude - that is how recharge earns trust")
    print("rule: recharge concentrates in coarse soils, fractures, losing reaches, wet years")
    print("OK: %s banked the recharge" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_springs(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def recession_Q(Q0_L_s, alpha_per_d, t_d):
    return Q0_L_s * math.exp(-alpha_per_d * t_d)
def storage_m3(Q0_L_s, alpha_per_d):
    return Q0_L_s / 1000.0 * 86400.0 / alpha_per_d
def main():
    Q0, alpha = 850.0, 0.02
    q30 = recession_Q(Q0, alpha, 30.0)
    assert abs(q30 - 850.0 * math.exp(-0.6)) < 0.01, q30
    assert q30 < Q0
    S = storage_m3(Q0, alpha)
    assert abs(S - 3672000.0) < 1000.0, S
    print("spring: Q0=850 L/s, alpha=0.02/d -> 30 d later %.0f L/s" % q30)
    print("dynamic storage above the outlet: %.2f million m3" % (S / 1e6))
    print("flashy multi-component recession = karst; smooth single = porous aquifer")
    print("rule: the spring is the aquifer's gauged outlet - read its recession")
    print("OK: %s metered the spring" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_snow(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def swe_mm(depth_m, density_frac):
    return depth_m * density_frac * 1000.0
def degree_day_melt_mm(tmean_C, melt_factor=3.5, t_thresh=0.0):
    return melt_factor * max(0.0, tmean_C - t_thresh)
def main():
    swe = swe_mm(1.4, 0.32)
    assert abs(swe - 448.0) < 1e-9, swe
    melt = degree_day_melt_mm(8.0)
    assert abs(melt - 28.0) < 1e-9, melt
    assert degree_day_melt_mm(-3.0) == 0.0
    days = swe / melt
    print("1.4 m snow at 0.32 density -> SWE %.0f mm" % swe)
    print("8 C day melts %.0f mm -> pack gone in %.0f such days" % (melt, days))
    print("a ripe pack is isothermal at 0 C and saturated - then every joule becomes runoff")
    print("rule: SWE is the account balance; degree-days are the withdrawal schedule")
    print("OK: %s weighed the snowpack" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_glacier(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def band_balance(area_km2, b_mwe):
    return area_km2 * b_mwe   # million m3 water equiv ~ (km2 * m = 1e6 m3)
def main():
    bands = [(2.0, 1.2), (3.0, 0.4), (2.5, -0.6), (1.5, -2.1)]  # (area, balance m w.e.)
    total = sum(band_balance(a, b) for a, b in bands)
    total_area = sum(a for a, _ in bands)
    b_mean = total / total_area
    assert abs(total - (-1.05)) < 1e-9, total
    assert abs(b_mean - (-0.1167)) < 0.001, b_mean
    ela_band = next(i for i, (a, b) in enumerate(bands) if b < 0)
    assert ela_band == 2
    print("glacier: %.1f km2, net balance %+.2f m w.e. (negative year - paying deglaciation discharge)" % (total_area, b_mean))
    print("equilibrium line sits in band %d - accumulation above, ablation below" % ela_band)
    print("negative balance pays 'deglaciation discharge' - a bonus that ends with the ice")
    print("rule: stakes and pits in, DEM differences check - mass balance is a ledger")
    print("OK: %s audited the glacier" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_reservoir(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def residence_time_d(volume_m3, outflow_m3_s):
    return volume_m3 / outflow_m3_s / 86400.0
def level_pool_step(S, I, O, dt_s):
    return S + (I - O) * dt_s
def main():
    T = residence_time_d(5e8, 120.0)
    assert abs(T - 48.2) < 0.5, T
    S0 = 4.0e8
    S1 = level_pool_step(S0, 300.0, 120.0, 86400.0)
    assert abs(S1 - (S0 + 180.0 * 86400.0)) < 1.0, S1
    print("500 Mm3 / 120 m3/s -> residence time %.0f days" % T)
    print("one day at +180 m3/s net inflow: storage %.3f -> %.3f Mm3" % (S0 / 1e6, S1 / 1e6))
    print("rule curves spend flood season low and supply season high - the operator's calendar")
    print("rule: storage change = (inflow - outflow) x dt - the reservoir's only arithmetic")
    print("OK: %s operated the pool" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_wetland(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def hydroperiod_stats(stage_m, dt_d=1.0, thresh_m=0.0):
    wet = [s > thresh_m for s in stage_m]
    days = sum(wet) * dt_d
    mean_depth = sum(max(0.0, s) for s in stage_m) / len(stage_m)
    # longest continuous wet spell
    best = cur = 0
    for w in wet:
        cur = cur + 1 if w else 0
        best = max(best, cur)
    return days, mean_depth, best * dt_d
def main():
    stage = [0.25, 0.30, 0.28, 0.10, -0.05, -0.12, -0.08, 0.05, 0.22, 0.31, 0.27, 0.15]
    days, mean_d, longest = hydroperiod_stats(stage, dt_d=30.0)
    assert abs(days - 270.0) < 1e-9, days
    assert abs(mean_d - 0.158) < 0.005, mean_d
    assert abs(longest - 150.0) < 1e-9, longest
    print("monthly stage: inundated %.0f days/yr, mean depth %.2f m, longest spell %.0f d" %
          (days, mean_d, longest))
    print("millimeters of level decide marsh vs meadow - survey to the centimeter")
    print("rule: get the hydroperiod right and the biology follows the water")
    print("OK: %s timed the wetland" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_flood_freq(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def gumbel_fit(annual_max):
    n = len(annual_max)
    mean = sum(annual_max) / n
    var = sum((x - mean) ** 2 for x in annual_max) / (n - 1)
    sd = math.sqrt(var)
    beta = sd * math.sqrt(6.0) / math.pi
    mu = mean - 0.5772156649 * beta
    return mu, beta
def gumbel_quantile(mu, beta, T_yrs):
    p = 1.0 - 1.0 / T_yrs
    return mu - beta * math.log(-math.log(p))
def main():
    # synthetic Gumbel sample with known parameters (seeded LCG for determinism)
    mu_t, beta_t = 500.0, 120.0
    s = 987654321
    sample = []
    for _ in range(60):
        s = (1103515245 * s + 12345) % 2 ** 31
        u = (s + 0.5) / 2 ** 31
        sample.append(mu_t - beta_t * math.log(-math.log(u)))
    mu, beta = gumbel_fit(sample)
    assert abs(mu - mu_t) / mu_t < 0.10, (mu, mu_t)
    assert abs(beta - beta_t) / beta_t < 0.15, (beta, beta_t)
    q100 = gumbel_quantile(mu, beta, 100.0)
    q2 = gumbel_quantile(mu, beta, 2.0)
    assert q100 > q2 > 0, (q100, q2)
    assert max(sample) > q2                    # the sample's biggest flood tops the 2-yr level
    assert 800.0 < q100 < 1400.0, q100         # sane range for this climate
    print("fitted Gumbel: mu=%.0f beta=%.0f (true 500/120)" % (mu, beta))
    print("Q100 = %.0f m3/s; 30-yr exceedance chance = %.0f%%" % (q100, 100 * (1 - 0.99 ** 30)))
    print("the '100-year flood' is a 1%% annual chance - not a schedule")
    print("rule: rank history, fit the tail, price the risk - then distrust stationarity")
    print("OK: %s priced the flood" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_drought(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def spi_gamma(precip_mm, x_mm):
    # SPI via gamma fit (Thom approximation) -> standard normal (Acklam approx)
    n = len(precip_mm)
    mean = sum(precip_mm) / n
    ln_mean = sum(math.log(p) for p in precip_mm) / n
    A = math.log(mean) - ln_mean
    alpha = (1.0 + math.sqrt(1.0 + 4.0 * A / 3.0)) / (4.0 * A)
    beta = mean / alpha
    # gamma CDF via regularized lower incomplete gamma (series)
    z = x_mm / beta
    term, ssum, k = 1.0 / alpha, 1.0 / alpha, 1
    while abs(term) > 1e-12 and k < 500:
        term *= z / (alpha + k)
        ssum += term
        k += 1
    cdf = ssum * math.exp(-z + alpha * math.log(z) - math.lgamma(alpha))
    cdf = min(max(cdf, 1e-10), 1 - 1e-10)
    # inverse normal (Acklam)
    a1, a2, a3 = -3.969683028665376e+01, 2.209460984245205e+02, -2.759285104469687e+02
    a4, a5 = 1.383577518672690e+02, -3.066479806614716e+01
    b1, b2, b3 = -5.447609879822406e+01, 1.615858368580409e+02, -1.556989798598866e+02
    b4, b5 = 6.680131188771972e+01, -1.328068155288572e+01
    c1, c2 = -7.784894002430293e-03, -3.223964580411365e-01
    c3, c4 = -2.400758277161838e+00, -2.549732539343734e+00
    c5, c6 = 4.374664141464968e+00, 2.938163982698783e+00
    d1, d2 = 7.784695709041462e-03, 3.224671290700398e-01
    d3, d4 = 2.445134137142996e+00, 3.754408661907416e+00
    plow, phigh = 0.02425, 1 - 0.02425
    if cdf < plow:
        q = math.sqrt(-2 * math.log(cdf))
        return (((((c1 * q + c2) * q + c3) * q + c4) * q + c5) * q + c6) / ((((d1 * q + d2) * q + d3) * q + d4) * q + 1)
    if cdf > phigh:
        q = math.sqrt(-2 * math.log(1 - cdf))
        return -(((((c1 * q + c2) * q + c3) * q + c4) * q + c5) * q + c6) / ((((d1 * q + d2) * q + d3) * q + d4) * q + 1)
    q = cdf - 0.5
    r = q * q
    return (((((a1 * r + a2) * r + a3) * r + a4) * r + a5) * q) / (((((b1 * r + b2) * r + b3) * r + b4) * r + b5) * r + 1)
def main():
    rain = [95.0, 110.0, 88.0, 120.0, 105.0, 92.0, 115.0, 100.0, 108.0, 97.0,
            112.0, 90.0, 118.0, 102.0, 96.0, 109.0, 93.0, 114.0, 99.0, 107.0,
            91.0, 116.0, 103.0, 98.0, 111.0, 94.0, 117.0, 101.0, 106.0, 89.0]
    spi_med = spi_gamma(rain, 103.0)
    spi_dry = spi_gamma(rain, 60.0)
    spi_wet = spi_gamma(rain, 140.0)
    assert abs(spi_med) < 0.35, spi_med
    assert spi_dry < -1.5, spi_dry
    assert spi_wet > 1.5, spi_wet
    print("SPI: median-season rain -> %+.2f; 60 mm -> %.2f (severe drought); 140 mm -> %+.2f" %
          (spi_med, spi_dry, spi_wet))
    print("1-month SPI tracks flash drought; 12-month SPI tracks the hydrological kind")
    print("rule: standardize the deficit - minus 2 is extreme, whatever 'normal' was")
    print("OK: %s measured the drought" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_water_quality(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def streeter_phelps(x_d, L0, D0, k1, k2):
    # D(x): oxygen deficit downstream; L0 ultimate BOD, D0 initial deficit
    if abs(k2 - k1) < 1e-9:
        return D0 * math.exp(-k1 * x_d) + k1 * L0 * x_d * math.exp(-k1 * x_d)
    return (k1 * L0 / (k2 - k1)) * (math.exp(-k1 * x_d) - math.exp(-k2 * x_d)) + D0 * math.exp(-k2 * x_d)
def main():
    L0, D0, k1, k2, DOsat = 25.0, 1.0, 0.35, 0.9, 9.0
    xs = [i * 0.25 for i in range(41)]
    defs = [streeter_phelps(x, L0, D0, k1, k2) for x in xs]
    imax = max(range(len(defs)), key=lambda i: defs[i])
    Dmax = defs[imax]
    DOmin = DOsat - Dmax
    assert 0.0 < xs[imax] < 10.0, xs[imax]
    assert DOmin < DOsat - D0, DOmin     # sag below the starting DO
    assert defs[-1] < Dmax              # recovery downstream
    print("oxygen sag: max deficit %.1f mg/L at %.1f d travel; minimum DO %.1f mg/L" %
          (Dmax, xs[imax], DOmin))
    print("shallow swift water reaerates fast and shallows the sag - k2 is the healer")
    print("rule: deoxygenation vs reaeration - the race decides where the sag bottoms out")
    print("OK: %s traced the sag" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_manning(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def trapezoid_A_R(b_m, y_m, z):
    A = (b_m + z * y_m) * y_m
    P = b_m + 2.0 * y_m * math.sqrt(1.0 + z * z)
    return A, A / P
def manning_Q(n, A, R, S):
    return (1.0 / n) * A * (R ** (2.0 / 3.0)) * math.sqrt(S)
def main():
    A, R = trapezoid_A_R(6.0, 2.0, 1.5)
    assert abs(A - 18.0) < 1e-9 and abs(R - 1.3625) < 0.005, (A, R)
    Q = manning_Q(0.030, A, R, 0.001)
    assert abs(Q - 23.4) < 0.5, Q
    Q_smooth = manning_Q(0.022, A, R, 0.001)
    assert Q_smooth > Q
    print("trapezoid b=6 m, y=2 m: A=%.1f m2, R=%.2f m" % (A, R))
    print("n=0.030, S=0.001 -> Q=%.1f m3/s; smoother n=0.022 -> Q=%.1f m3/s" % (Q, Q_smooth))
    print("Froude check and compound splitting come next - this is uniform-flow ground truth")
    print("rule: gravity down the slope vs friction on the boundary - Manning settles the score")
    print("OK: %s solved the channel" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_sediment(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def shields_critical_tau(d_mm, rho_s=2650.0):
    theta_c = 0.045
    return theta_c * (rho_s - 1000.0) * 9.81 * (d_mm / 1000.0)
def boundary_tau(depth_m, slope):
    return 1000.0 * 9.81 * depth_m * slope
def mpm_bedload(tau, tau_c, d_mm):
    # Meyer-Peter & Mueller volumetric rate per unit width (m2/s), simplified
    if tau <= tau_c:
        return 0.0
    s = 1.65
    return 8.0 * ((tau - tau_c) / (1000.0 * 9.81 * s * d_mm / 1000.0)) ** 1.5 * math.sqrt(s * 9.81 * (d_mm / 1000.0) ** 3)
def main():
    tau_c = shields_critical_tau(20.0)
    assert abs(tau_c - 14.56) < 0.1, tau_c
    tau = boundary_tau(2.0, 0.002)
    assert abs(tau - 39.24) < 0.1, tau
    assert tau > tau_c
    qb = mpm_bedload(tau, tau_c, 20.0)
    assert qb > 0
    assert mpm_bedload(tau_c * 0.5, tau_c, 20.0) == 0.0
    print("20-mm gravel: critical shear %.1f Pa; flow shear %.1f Pa -> bedload %.2e m2/s" % (tau_c, tau, qb))
    print("below critical the bed sleeps; above it the river rebuilds itself")
    print("rule: Exner continuity - transport divergence becomes bed-elevation change")
    print("OK: %s moved the bedload" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_urban(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def rational_Q(C, i_mm_h, A_ha):
    # Q (m3/s) = C * i(mm/h) * A(ha) / 360
    return C * i_mm_h * A_ha / 360.0
def main():
    q_meadow = rational_Q(0.10, 80.0, 5.0)
    q_lot = rational_Q(0.95, 80.0, 5.0)
    assert abs(q_meadow - 0.1111) < 0.001, q_meadow
    assert abs(q_lot - 1.0556) < 0.001, q_lot
    assert abs(q_lot / q_meadow - 9.5) < 0.01
    print("5 ha, 80 mm/h storm: meadow (C=0.10) -> %.2f m3/s; parking lot (C=0.95) -> %.2f m3/s" %
          (q_meadow, q_lot))
    print("same rain, 9.5x the peak - that is the urban stream syndrome in one number")
    print("LID answer: bioretention sized for the first 25 mm, permeable pavement over stone")
    print("rule: intensity at the time of concentration x area x C - size the pipe, then tame the peak")
    print("OK: %s paved the numbers" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_detention(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def orifice_Q(Cd, A_m2, h_m):
    return Cd * A_m2 * math.sqrt(2.0 * 9.81 * h_m)
def puls_route(I, dt_s, S_of_h, O_of_h, h0):
    # storage-indication routing; S_of_h/O_of_h: lists over stage index
    S = S_of_h[h0]
    out, h = [], h0
    for qin in I:
        # solve S2 = S1 + (I1+I2)/2*dt - (O1+O2)/2*dt by stage iteration
        o1 = O_of_h[h]
        best, bh = None, h
        for hh in range(len(S_of_h)):
            o2 = O_of_h[hh]
            s2 = S_of_h[hh]
            lhs = s2 + o2 * dt_s / 2.0
            rhs = S + (qin + qin) / 2.0 * dt_s - o1 * dt_s / 2.0
            err = abs(lhs - rhs)
            if best is None or err < best:
                best, bh = err, hh
        h = bh
        S = S_of_h[h]
        out.append(O_of_h[h])
    return out
def main():
    stages = [i * 0.25 for i in range(13)]          # 0..3 m
    S_of_h = [1200.0 * h ** 1.4 for h in stages]    # stage-storage
    O_of_h = [orifice_Q(0.6, 0.5, h) for h in stages]
    I = [2.0, 6.0, 14.0, 22.0, 18.0, 10.0, 5.0, 3.0, 2.0]
    O = puls_route(I, 600.0, S_of_h, O_of_h, 0)
    assert max(O) < max(I), (max(O), max(I))
    assert O[-1] > 0
    print("inflow peak %.0f m3/s -> outflow peak %.1f m3/s (attenuated)" % (max(I), max(O)))
    print("the basin stores the volume above the allowable release, then meters it out")
    print("rule: dS/dt = I - O - route it, don't guess it")
    print("OK: %s tamed the peak" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_reservoir_yield(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def sequent_peak(inflow, demand):
    # max cumulative deficit of (demand - inflow); = required storage
    cum, peak, worst = 0.0, 0.0, 0
    for i, (q, d) in enumerate(zip(inflow, demand)):
        cum += d - q
        if cum > peak:
            peak, worst = cum, i
    return max(0.0, peak), worst
def main():
    inflow = [120.0, 95.0, 60.0, 35.0, 25.0, 30.0, 55.0, 90.0, 130.0, 150.0, 140.0, 125.0]
    demand = [80.0] * 12
    req, worst = sequent_peak(inflow, demand)
    assert req > 0 and 0 <= worst < 12
    # verify: simulate with storage = req, never negative
    S, minS = req, req
    for q, d in zip(inflow, demand):
        S = min(req, S + q - d)
        S = max(0.0, S)
        minS = min(minS, S)
    assert abs(minS) < 1e-9, minS
    print("12-month test: required storage %.0f units to meet demand %.0f through the dry spell" % (req, demand[0]))
    print("worst deficit ends month %d; simulation with that storage just touches empty" % (worst + 1))
    print("firm yield = the demand this storage meets through the drought of record")
    print("rule: Rippl's mass curve - the biggest cumulative deficit sizes the dam")
    print("OK: %s firmed the yield" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hydropower(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def power_MW(Q_m3_s, H_m, eff=0.90):
    return 1000.0 * 9.81 * Q_m3_s * H_m * eff / 1e6
def exceedance_Q(sorted_desc, pct):
    idx = min(len(sorted_desc) - 1, int(pct / 100.0 * len(sorted_desc)))
    return sorted_desc[idx]
def main():
    flows = sorted([42.0, 18.0, 95.0, 60.0, 25.0, 130.0, 75.0, 33.0, 52.0, 88.0,
                    21.0, 110.0, 47.0, 66.0, 29.0, 102.0, 58.0, 36.0, 80.0, 15.0], reverse=True)
    q90 = exceedance_Q(flows, 90.0)
    q50 = exceedance_Q(flows, 50.0)
    assert q90 <= q50, (q90, q50)
    P_firm = power_MW(q90, 85.0)
    P_med = power_MW(q50, 85.0)
    assert abs(P_firm - 1000 * 9.81 * q90 * 85 * 0.9 / 1e6) < 1e-9
    assert P_med > P_firm
    print("flow-duration: Q90=%.0f m3/s (dependable), Q50=%.0f m3/s (median)" % (q90, q50))
    print("head 85 m: firm power %.1f MW, median-flow power %.1f MW" % (P_firm, P_med))
    print("Pelton for high head, Francis for middle, Kaplan for low head and big flow")
    print("rule: P = rho g Q H eta - every term is hydrology")
    print("OK: %s spun the turbine" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_irrigation(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def net_requirement_mm(ET0, Kc, Peff_mm):
    return max(0.0, ET0 * Kc - Peff_mm)
def gross_requirement_mm(net_mm, eff):
    return net_mm / eff
def main():
    stages = [("initial", 0.4, 25.0, 20.0), ("mid", 1.15, 180.0, 40.0), ("late", 0.7, 90.0, 30.0)]
    total_net = 0.0
    for name_s, Kc, ET0, Pe in stages:
        nr = net_requirement_mm(ET0, Kc, Pe)
        total_net += nr
        print("  %-8s: Kc=%.2f ETc=%.0f mm - Peff %.0f -> net %.0f mm" % (name_s, Kc, ET0 * Kc, Pe, nr))
    assert abs(total_net - 200.0) < 1.0, total_net
    gross_flood = gross_requirement_mm(total_net, 0.45)
    gross_drip = gross_requirement_mm(total_net, 0.90)
    assert abs(gross_flood - 444.4) < 1.0 and abs(gross_drip - 222.2) < 1.0
    print("season net %.0f mm -> gross: flood %.0f mm vs drip %.0f mm (half the water)" %
          (total_net, gross_flood, gross_drip))
    print("add a leaching fraction in arid lands - salts stay behind when crops drink")
    print("rule: schedule at management-allowed depletion; deliver ETc minus effective rain")
    print("OK: %s watered the field" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_gw_model(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def solve_1d_steady(n, h_left, h_right):
    # Laplace: h[i] = (h[i-1]+h[i+1])/2 -> linear profile; iterate to converge
    h = [h_left + (h_right - h_left) * i / (n - 1) for i in range(n)]
    for _ in range(1000):
        mx = 0.0
        for i in range(1, n - 1):
            new = 0.5 * (h[i - 1] + h[i + 1])
            mx = max(mx, abs(new - h[i]))
            h[i] = new
        if mx < 1e-10:
            break
    return h
def main():
    h = solve_1d_steady(11, 100.0, 80.0)
    for i, hh in enumerate(h):
        assert abs(hh - (100.0 - 2.0 * i)) < 1e-6, (i, hh)
    grad = (h[0] - h[-1]) / 10.0
    assert abs(grad - 2.0) < 1e-9
    print("11 cells, heads 100->80 m: solved profile linear, gradient %.1f m/cell" % grad)
    print("add a pumping well = a specified-flux cell; a river = a head-dependent boundary")
    print("rule: calibrate to heads AND fluxes - many parameter sets fit the past")
    print("OK: %s solved the aquifer" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_karst(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def two_component(t_d, Qf0, Qs0, af, as_):
    return Qf0 * math.exp(-af * t_d) + Qs0 * math.exp(-as_ * t_d)
def dye_velocity_km_d(distance_km, travel_h):
    return distance_km / (travel_h / 24.0)
def main():
    Qf0, Qs0, af, as_ = 1200.0, 300.0, 0.8, 0.03
    q1 = two_component(1.0, Qf0, Qs0, af, as_)
    q20 = two_component(20.0, Qf0, Qs0, af, as_)
    assert q1 > q20 > 0
    assert abs(q1 - (1200 * math.exp(-0.8) + 300 * math.exp(-0.03))) < 0.01
    # after 20 d the conduit component is essentially gone
    assert 1200 * math.exp(-0.8 * 20) < 1.0
    v = dye_velocity_km_d(8.5, 14.0)
    assert abs(v - 14.57) < 0.05, v
    print("karst spring recession: day 1 = %.0f L/s, day 20 = %.0f L/s (conduit drained, matrix remains)" % (q1, q20))
    print("dye: 8.5 km in 14 h -> conduit velocity %.1f km/d" % v)
    print("sinkhole to spring with zero filtration - zone protection by travel time")
    print("rule: Darcy fails in conduits - trace it, don't assume it")
    print("OK: %s traced the conduits" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_isotopes(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def delta_permil(R_sample, R_std):
    return (R_sample / R_std - 1.0) * 1000.0
def two_component_mix(d_stream, d_gw, d_rain):
    # fraction of event (rain) water
    f = (d_stream - d_gw) / (d_rain - d_gw)
    return f
def main():
    d = delta_permil(0.001997, 0.0020052)   # ~ VSMOW 18O ratio
    assert abs(d - (-4.09)) < 0.05, d
    # stormflow split: stream -8.5, groundwater -10.0, rain -5.0 per mil
    f_event = two_component_mix(-8.5, -10.0, -5.0)
    assert abs(f_event - 0.30) < 1e-9, f_event
    print("sample 18O ratio -> delta = %.2f per mil vs VSMOW" % d)
    print("stormflow: %.0f%% event rain, %.0f%% old groundwater pushed out" % (100 * f_event, 100 * (1 - f_event)))
    print("the classic result: floods are mostly old water - the rain just shoves it out")
    print("rule: heavy isotopes prefer liquid - every phase change writes the biography")
    print("OK: %s read the water's biography" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ecohydrology(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def tennant_flow(MAF_m3_s, pct):
    return MAF_m3_s * pct / 100.0
def alteration_pct(natural, altered):
    return [(a - n) / n * 100.0 for n, a in zip(natural, altered)]
def main():
    MAF = 60.0
    fair = tennant_flow(MAF, 30.0)
    outstanding = tennant_flow(MAF, 60.0)
    assert abs(fair - 18.0) < 1e-9 and abs(outstanding - 36.0) < 1e-9
    nat = [40.0, 55.0, 80.0, 95.0, 70.0, 45.0]
    alt = [35.0, 40.0, 45.0, 50.0, 45.0, 38.0]
    alt_pct = alteration_pct(nat, alt)
    assert all(p < 0 for p in alt_pct)
    assert abs(alt_pct[3] - (-47.37)) < 0.01, alt_pct[3]
    print("MAF 60 m3/s: Tennant 'fair' habitat = %.0f m3/s, 'outstanding' = %.0f m3/s" % (fair, outstanding))
    print("spring freshet altered %+.0f%% - the cue fish spawn on is half gone" % alt_pct[3])
    print("building blocks: baseflows + maintenance floods + floodplain floods, each with timing")
    print("rule: the flow regime is the master variable - magnitude, timing, duration, frequency")
    print("OK: %s reserved the river's share" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_inundation(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def manning_Q(n, A, R, S):
    return (1.0 / n) * A * (R ** (2.0 / 3.0)) * math.sqrt(S)
def compound_Q(sections, S):
    # sections: (n, A, R)
    return sum(manning_Q(n, A, R, S) for n, A, R in sections)
def main():
    main_ch = (0.035, 120.0, 3.0)
    floodplain = (0.080, 400.0, 1.2)
    S = 0.0008
    Q = compound_Q([main_ch, floodplain], S)
    Q_ch = manning_Q(*main_ch, S)
    assert Q > Q_ch > 0
    assert abs(Q - (Q_ch + manning_Q(*floodplain, S))) < 1e-9
    print("compound section: main channel %.0f m3/s + floodplain %.0f m3/s = %.0f m3/s" %
          (Q_ch, Q - Q_ch, Q))
    print("depth AND velocity get mapped - deep-slow and shallow-fast are different hazards")
    print("rule: split the section, convey each part, sum - then calibrate to high-water marks")
    print("OK: %s mapped the floodplain" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_forecasting(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def exceedance_prob(ensemble, threshold):
    return sum(1 for x in ensemble if x >= threshold) / len(ensemble)
def crps_proxy(ensemble, observed):
    # mean absolute error of ensemble mean vs observed (simplified skill proxy)
    mean = sum(ensemble) / len(ensemble)
    return abs(mean - observed)
def main():
    ens = [3.1, 3.4, 2.8, 3.9, 3.2, 4.1, 3.0, 3.6, 2.9, 3.8,
           3.3, 3.5, 4.3, 3.0, 3.7, 2.7, 3.9, 3.4, 3.2, 3.6]
    p = exceedance_prob(ens, 3.8)
    assert abs(p - 0.25) < 1e-9, p
    assert exceedance_prob(ens, 2.0) == 1.0
    assert exceedance_prob(ens, 5.0) == 0.0
    err = crps_proxy(ens, 3.45)
    assert err < 0.05, err
    print("20-member crest ensemble: P(crest >= 3.8 m) = %.0f%%" % (100 * p))
    print("ensemble-mean error vs observed 3.45 m: %.3f m" % err)
    print("'30%% chance of exceeding flood stage' beats any single deterministic crest")
    print("rule: assimilate to the present, ensemble the future, verify against the past")
    print("OK: %s called the crest" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_frontiers(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def grace_groundwater_anomaly(tws_mm, soil_mm, swe_mm):
    # total water storage minus soil moisture minus snow = groundwater (+ surface water)
    return tws_mm - soil_mm - swe_mm
def swot_discharge_m3s(width_m, slope, n=0.03, depth_m=3.0):
    A = width_m * depth_m
    R = A / (width_m + 2.0 * depth_m)
    return (1.0 / n) * A * (R ** (2.0 / 3.0)) * math.sqrt(slope)
def main():
    gw = [grace_groundwater_anomaly(t, s, w) for t, s, w in
          [(-40.0, -10.0, -5.0), (-55.0, -12.0, -6.0), (-70.0, -15.0, -8.0)]]
    assert all(g < 0 for g in gw), gw
    trend = (gw[-1] - gw[0]) / 2.0
    assert trend < 0
    Q = swot_discharge_m3s(220.0, 0.00012)
    assert Q > 100.0, Q
    print("GRACE: groundwater anomaly trend %+.1f mm/yr (depletion watched from orbit)" % trend)
    print("SWOT: 220-m-wide river, slope 1.2e-4 -> discharge ~%.0f m3/s, no gauge needed" % Q)
    print("PUB regionalization brings the science to the ungauged majority")
    print("rule: weigh it from orbit, slope it from the surface, fuse it all")
    print("OK: %s weighed the planet's water" % NAME)
if __name__ == "__main__":
    main()
''')

DEMOS = {
    "hydro_branches": demo_hydro_branches, "water_budget": demo_water_budget,
    "watershed": demo_watershed, "precip_gauge": demo_precip_gauge,
    "infiltration": demo_infiltration, "evapotranspiration": demo_evapotranspiration,
    "streamflow": demo_streamflow, "rating_curve": demo_rating_curve,
    "hydrograph": demo_hydrograph, "unit_hydrograph": demo_unit_hydrograph,
    "vadose": demo_vadose, "darcy": demo_darcy,
    "theis": demo_theis, "recharge": demo_recharge,
    "springs": demo_springs, "snow": demo_snow,
    "glacier": demo_glacier, "reservoir": demo_reservoir,
    "wetland": demo_wetland, "flood_freq": demo_flood_freq,
    "drought": demo_drought, "water_quality": demo_water_quality,
    "manning": demo_manning, "sediment": demo_sediment,
    "urban": demo_urban, "detention": demo_detention,
    "reservoir_yield": demo_reservoir_yield, "hydropower": demo_hydropower,
    "irrigation": demo_irrigation, "gw_model": demo_gw_model,
    "karst": demo_karst, "isotopes": demo_isotopes,
    "ecohydrology": demo_ecohydrology, "inundation": demo_inundation,
    "forecasting": demo_forecasting, "frontiers": demo_frontiers,
}

# ---------------------------------------------------------------- records

def build_records(slug, source):
    cfg = DBCFG[slug]
    sig = source == "signature"
    # Teaching-ladder order: stable sort by ladder_rank (entries are already
    # in ladder order in entries_hydrology.py).
    ordered = sorted(enumerate(ENTRIES), key=lambda p: (p[1]["ladder_rank"], p[0]))
    recs = []
    for _, e in ordered:
        name = e["name"]
        title = name + " (Signature Edition)" if sig else name
        # Whole-system dedupe gate (his standing rule: every record, never a sample).
        if [h for h in base.GATE.check(slug, title) if h[0] != slug]:
            print("  gate refused (cross-db dupe): %s" % title, flush=True)
            continue
        rid = "%s%06d" % (cfg["prefix"], len(recs) + 1)
        if sig:
            description = ("Signature original interpretation. " + e["sig_lens"] + " "
                           + e["description"])
            how = e["sig_lens"] + " " + e["how_it_works"]
            citations = list(e["citations"]) + [SIG_TAIL]
        else:
            description = e["description"]
            how = e["how_it_works"]
            citations = list(e["citations"])
        rec = {
            "id": rid, "t": title, "g": e["group"], "name": name, "title": title,
            "description": description,
            "how_it_works": how,
            "key_points": list(e["key_points"]),
            "requirements": list(e["requirements"]),
            "standards": list(e["standards"]),
            "citations": citations,
            "src": "signature" if sig else "public-harvest",
            "ladder_rank": e["ladder_rank"],
            "ladder_tier": e["ladder_tier"],
        }
        demo_fn = DEMOS[e["demo_kind"]]
        program = demo_fn(name if not sig else title, rid, e["group"],
                          e["key_points"], "; ".join(e["requirements"]))
        rec["demo"] = {"kind": "python", "language": "python",
                       "program": program,
                       "note": "Working demonstration program (real, runnable Python)."}
        base.GATE.admit(slug, title, rid)
        recs.append(rec)
    # Ladder order guarantee: ids were assigned in ladder order; re-verify.
    ranks = [r["ladder_rank"] for r in recs]
    assert ranks == sorted(ranks), "records not in ladder order for %s" % slug
    return recs


def main():
    sys.path.insert(0, os.path.join(REPO, "code", "numbering-build"))
    spec = importlib.util.spec_from_file_location(
        "nb_build", os.path.join(REPO, "code", "numbering-build", "build.py"))
    nb = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(nb)
    nb.DBCFG = DBCFG

    sweep_path = "/home/hatch/workspace/goals/database-quality-audit/hidden_files/patches/sweep-db-pages.py"
    sspec = importlib.util.spec_from_file_location("sweep", sweep_path)
    sweep = importlib.util.module_from_spec(sspec)
    sspec.loader.exec_module(sweep)

    built = {}
    for slug in ("hydrology", "hydrology-signature"):
        source = "signature" if slug.endswith("-signature") else "public"
        built[slug] = build_records(slug, source)

    # sanity: ids unique + prefix + required keys + ALL demo programs compile
    # + banned-content scan + ladder fields present
    total = 0
    for slug, recs in built.items():
        cfg = DBCFG[slug]
        ids = [r["id"] for r in recs]
        assert len(ids) == len(set(ids)), "dup ids in %s" % slug
        assert all(i.startswith(cfg["prefix"]) for i in ids), "prefix drift in %s" % slug
        assert len(recs) >= 30, "fewer than 30 records in %s" % slug
        for r in recs:
            for k in ("id", "t", "g", "name", "title", "description", "how_it_works",
                      "key_points", "requirements", "standards", "citations",
                      "src", "ladder_rank", "ladder_tier", "demo"):
                assert k in r, "missing %s in %s" % (k, r["id"])
            prog = r["demo"].get("program")
            assert prog and len(r["description"]) > 200, "stub in %s" % r["id"]
            assert 1 <= r["ladder_rank"] <= 10, "ladder_rank out of range in %s" % r["id"]
            assert r["ladder_tier"] in ("foundations", "compounded", "advanced"), \
                "bad ladder_tier in %s" % r["id"]
            compile(prog, r["id"], "exec")
            blob = json.dumps(r).lower()
            assert "facebook" not in blob, "facebook ref in %s" % r["id"]
            assert "bat belt" not in blob, "banned phrase in %s" % r["id"]
            if slug.endswith("-signature"):
                assert "(signature edition)" in r["title"].lower(), "sig title missing suffix"
                assert r["src"] == "signature"
            else:
                assert r["src"] == "public-harvest"
        total += len(recs)
        n = base.write_shard_db(slug, recs)
        print("shard: %-38s %d records" % (slug, n), flush=True)

    # machine-execute EVERY demo (canon: runnable demo, machine-executed OK)
    for slug, recs in built.items():
        for r in recs:
            prog = r["demo"]["program"]
            p = subprocess.run([sys.executable, "-c", prog],
                               capture_output=True, text=True, timeout=60)
            assert p.returncode == 0, "demo failed %s: %s" % (r["id"], p.stderr[-500:])
            assert "OK:" in p.stdout, "demo no OK marker %s" % r["id"]
    print("demo execution: all %d demos ran OK" % total, flush=True)

    with open(TEMPLATE, "r", encoding="utf-8") as f:
        template = f.read()
    for slug, recs in built.items():
        page = nb.build_page(slug, template)
        page = page.replace(
            "Generate structural synthetic intelligence studies. Seeded archive records are the authoritative entries.",
            DBCFG[slug]["gen_desc"])
        assert 'id="stCount"' in page and "var SLUG='%s';" % slug in page
        assert "minmax(120px,1fr)" in page and "pre.codeblock" in page
        assert "facebook" not in page.lower()
        assert "synthetic intelligence" not in page.lower(), "template leftover in %s" % slug
        assert "bat belt" not in page.lower(), "banned phrase in page %s" % slug
        ddir = os.path.join(REPO, "db", slug)
        os.makedirs(ddir, exist_ok=True)
        ppath = os.path.join(ddir, "index.html")
        with open(ppath, "w", encoding="utf-8") as f:
            f.write(page)
        changed, notes = sweep.process_page(ppath)
        topics = {}
        for r in recs:
            topics.setdefault(r["g"], []).append("%s - %s" % (r["t"], r["g"]))
        gen_js = nb.build_gen_js(slug, topics, DBCFG[slug])
        assert "facebook" not in gen_js.lower() and "bat belt" not in gen_js.lower()
        with open(os.path.join(ddir, "gen-%s.js" % slug), "w", encoding="utf-8") as f:
            f.write(gen_js)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)

    entries_m = [base.manifest_entry(s, len(built[s])) for s in built]
    base.update_json_list(os.path.join(REPO, "data", "manifest.json"), entries_m)
    entries_a = [base.api_entry(s, len(built[s])) for s in built]
    base.update_json_list(os.path.join(REPO, "api.json"), entries_a)
    print("manifest + api.json: appended %d databases, %d records" % (len(built), total))
    print("NEXT: run python3 code/restamp_counts.py, then commit + push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
