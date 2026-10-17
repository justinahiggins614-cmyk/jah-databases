#!/usr/bin/env python3
"""Build the Meteorology field databases for JAH Databases (field #15, taxonomy order).

Verified 2026-10-17: NO database covers meteorology as a discipline.
- 'weather-climate' (10,000 records): raw station observations - no science.
- 'weather' (38 records): thin stubs ('Weather Forecasting (overview)',
  'Cold Fronts (examples)', 'Hurricanes (detailed)' style cards).
- 'weather-control' (150 records): Signature fun/futures weather-control
  creations - speculative, not the discipline.
- 'climatology' (34 records, field #12): long-term climate - not forecasting
  practice. Covers 'Jet Streams' as a climate feature only.
- 'atmospheric-science' (36 records, field #13): physics/chemistry of air -
  covers thunderstorms (life cycle), air masses & fronts, mid-latitude
  cyclones, CAPE/CIN soundings, lightning electrification, Doppler radar,
  satellites, NWP, and tropical-cyclone structure as PHYSICAL SYSTEMS.
  Missing as forecaster PRACTICE: synoptic chart analysis, sounding
  interpretation as a daily tool, radar/satellite image interpretation,
  the Dvorak technique, forecast methods, ensembles, MOS, verification,
  the warning process, and aviation/marine/mountain/fire/agricultural
  meteorology, tornadoes, winter-storm and lake-effect forecasting.

So this build creates two NEW databases:

  meteorology             — The Meteorology Database
                            (public-harvest: real, fact-checked meteorology)
  meteorology-signature   — The Meteorology Signature Database
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

Subtitle disambiguation (field #13 pattern): where a related record card
exists in atmospheric-science/climatology, titles carry a practice-focused
subtitle, e.g. "Numerical Weather Prediction in Practice: Models, Grids,
and Spin-Up" rather than bare "Numerical Weather Prediction".

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
# main repo (8,590,108 records, 256 shards; titles from fields #12-14
# cross-checked directly against their shard indexes since the gate index
# predates them - subtitle disambiguation used throughout).
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_meteorology import ENTRIES, SIG_TAIL

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature interpretation of meteorology: "
                "clearly labeled Signature-made, never presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked meteorology: what meteorology is; weather "
                "instruments; the observing network; surface analysis; air masses; fronts; the "
                "Norwegian cyclone model; upper-air charts; jet streams; the diurnal cycle and "
                "local winds; the Skew-T diagram; thunderstorm forecasting; tornadoes; hail, "
                "damaging winds, and derechos; lightning practice; fog forecasting; winter "
                "storms; lake-effect snow; mountain weather; marine meteorology; tropical "
                "meteorology; hurricane forecasting; heat and cold extremes; fire weather; "
                "agricultural meteorology; radar interpretation; satellite interpretation and "
                "the Dvorak technique; nowcasting; numerical weather prediction in practice; "
                "ensemble forecasting; statistical post-processing; forecast verification; "
                "aviation meteorology; hydrologic outlooks; weather communication; frontiers, "
                "organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations (what meteorology is, "
              "instruments, the observing network, surface analysis, air masses, fronts, the "
              "Norwegian cyclone, upper-air charts, jet streams, the diurnal cycle) -> "
              "Compounded (Skew-T soundings, thunderstorm forecasting, tornadoes, hail and "
              "derechos, lightning practice, fog, winter storms, lake-effect snow, mountain "
              "weather, marine meteorology, tropical meteorology, hurricane forecasting, heat "
              "and cold, fire weather, agricultural meteorology, radar interpretation, "
              "satellite interpretation, nowcasting) -> Advanced (NWP in practice, ensembles, "
              "statistical post-processing, verification, aviation meteorology, hydrologic "
              "outlooks, weather communication, frontiers).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search fronts, Skew-T, CAPE, dBZ, Dvorak, ensembles, METAR, watches, warnings...",
        "chat_ph": "Ask about meteorology...",
        "archive_blurb": ("Seeded %s meteorology records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled structural meteorology studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about meteorology - from surface analysis and Skew-T soundings to ensembles, radar, and warnings." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "meteorology-study", "gen_demo_kind": "meteorology-demo",
        "source": source,
    }

CIT_PUB = "Meteorology (peer-reviewed literature and standard textbooks)."
CIT_SIG = CIT_PUB + " " + SIG_TAIL

DBCFG = {}
DBCFG["meteorology"] = _cfg(
    "meteorology", "The Meteorology Database",
    "Real, fact-checked meteorology: the discipline, instruments, the observing network, "
    "surface analysis, air masses, fronts, the Norwegian cyclone, upper-air charts, jet "
    "streams, the diurnal cycle, Skew-T soundings, thunderstorm forecasting, tornadoes, "
    "hail and derechos, lightning practice, fog, winter storms, lake-effect snow, mountain "
    "weather, marine meteorology, tropical meteorology, hurricane forecasting, heat and "
    "cold extremes, fire weather, agricultural meteorology, radar and satellite "
    "interpretation, nowcasting, NWP in practice, ensembles, post-processing, verification, "
    "aviation meteorology, hydrologic outlooks, weather communication, and frontiers.",
    "meteorology record", "JAH-MET-", "JAH Meteorology Archivist",
    "meteorology archivist - what meteorology is, weather instruments, the observing "
    "network, surface analysis, air masses, fronts, the Norwegian cyclone model, "
    "upper-air charts, jet streams in practice, the diurnal cycle and local winds, the "
    "Skew-T log-P diagram, thunderstorm forecasting ingredients, tornadoes and the EF "
    "scale, hail and derechos, lightning detection and safety, fog forecasting, winter "
    "storm forecasting, lake-effect snow, mountain weather, marine meteorology and the "
    "Beaufort scale, tropical meteorology, hurricane track and intensity forecasting, "
    "heat index and wind chill, fire weather and the Haines index, agricultural "
    "meteorology, radar interpretation, satellite interpretation and the Dvorak "
    "technique, nowcasting, NWP in practice, ensemble forecasting, MOS post-processing, "
    "forecast verification, aviation meteorology, hydrologic outlooks, weather "
    "communication and the warning process, frontiers; teaching progressively along "
    "the ladder from foundations through compounded to advanced; answers from many "
    "angles - definition, example, analogy, application, history, math, how-to - using "
    "only the system's own archive data",
    CIT_PUB, "public")
DBCFG["meteorology-signature"] = _cfg(
    "meteorology-signature", "The Meteorology Signature Database",
    "His original Signature interpretation of meteorology: the full ladder from surface "
    "analysis and Skew-T soundings to ensembles, radar interpretation, and the warning "
    "process, reframed as Signature science. Clearly labeled Signature-made, never "
    "presented as authentic public record.",
    "meteorology record", "JAH-METS-", "JAH Meteorology Archivist (Signature)",
    "meteorology archivist - Signature editions: his original Signature interpretation "
    "of meteorology, clearly labeled Signature-made and never presented as authentic "
    "public record; teaches progressively along the ladder from foundations through "
    "compounded to advanced; answers from many angles - definition, example, analogy, "
    "application, history, math, how-to - using only the system's own archive data",
    CIT_SIG, "signature")

base.DBCFG = DBCFG

# ---------------------------------------------------------------- demos
# Every demo is real, runnable, stdlib-only Python performing the actual
# meteorological calculation for its record. All are machine-executed by main().

_PREAMBLE = """import math
import re
"""

def _wrap(name, rid, group, body):
    return (base._hdr(name, rid, group) + _PREAMBLE + body.replace("NAME", json.dumps(name)))

def demo_meteo_branches(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
BRANCHES = {
    "synoptic meteorology": "continental weather maps, fronts, cyclones",
    "mesoscale meteorology": "storms, boundaries, lake-effect snow",
    "microscale meteorology": "turbulence, fog, the lowest meters",
    "aviation meteorology": "METAR, TAF, in-flight hazards",
    "marine meteorology": "Beaufort, waves, gale warnings",
    "tropical meteorology": "ITCZ, waves, monsoons, hurricanes",
}
def main():
    assert len(BRANCHES) == 6
    assert "weather maps" in BRANCHES["synoptic meteorology"]
    for branch, focus in BRANCHES.items():
        print("%-24s -> %s" % (branch, focus))
    print("one loop binds them: observe, analyze, diagnose, predict, verify, communicate")
    print("rule: the scale picks the tools, the loop never changes")
    print("OK: %s mapped the discipline" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_unit_conversions(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def c_to_f(c): return c * 9.0 / 5.0 + 32.0
def f_to_c(f): return (f - 32.0) * 5.0 / 9.0
def hpa_to_inhg(h): return h * 0.02953
def inhg_to_hpa(i): return i / 0.02953
def kt_to_ms(k): return k * 0.514444
def kt_to_mph(k): return k * 1.15078
def main():
    assert abs(c_to_f(0.0) - 32.0) < 1e-9
    assert abs(f_to_c(212.0) - 100.0) < 1e-9
    assert abs(hpa_to_inhg(1013.25) - 29.92) < 0.01, hpa_to_inhg(1013.25)
    assert abs(inhg_to_hpa(29.92) - 1013.25) < 0.5
    assert abs(kt_to_ms(10.0) - 5.14444) < 1e-4
    assert abs(kt_to_mph(100.0) - 115.078) < 0.01
    print("0 C = 32 F; 1013.25 hPa = 29.92 inHg; 10 kt = 5.14 m/s; 100 kt = 115 mph")
    print("wind is reported FROM the direction it blows, in knots or m/s")
    print("rule: convert first, compare second - mixed units sink forecasts")
    print("OK: %s converted the toolkit" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_network_coverage(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
EARTH_KM2 = 510.1e6
def mean_spacing_km(area_km2, n):
    return math.sqrt(area_km2 / n)
def main():
    s_surface = mean_spacing_km(EARTH_KM2, 10000.0)
    s_upper = mean_spacing_km(EARTH_KM2, 900.0)
    assert 200.0 < s_surface < 260.0, s_surface
    assert 700.0 < s_upper < 820.0, s_upper
    # reports per day: ASOS every minute, sondes twice daily
    asos_reports = 10000 * 24 * 60
    sonde_reports = 900 * 2
    assert asos_reports > sonde_reports * 1000
    print("10,000 surface stations -> mean spacing ~%.0f km" % s_surface)
    print("900 radiosonde sites -> mean spacing ~%.0f km; launches at 00 and 12 UTC" % s_upper)
    print("surface reports per day: %d vs %d sonde profiles - the surface network is the dense one" %
          (asos_reports, sonde_reports))
    print("rule: the analysis can only be as good as the spacing - gaps are where models guess")
    print("OK: %s surveyed the network" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_station_model(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def wind_from_feathers(feathers):
    # feathers: list like ['long','long','short'] ; long=10kt, short=5kt, pennant=50kt
    val = {"long": 10, "short": 5, "pennant": 50}
    return sum(val[f] for f in feathers)
def decode(plot):
    # plot: dict with the station-model fields
    wind = wind_from_feathers(plot["feathers"])
    return {
        "temp_C": plot["t"], "dewpoint_C": plot["td"],
        "slp_hPa": plot["slp"], "wind_dir": plot["wdir"],
        "wind_kt": wind, "sky_octas": plot["sky"],
    }
def main():
    plot = {"t": 22.0, "td": 18.0, "slp": 1013.2, "wdir": 240,
            "feathers": ["long", "short"], "sky": 6}
    d = decode(plot)
    assert d["wind_kt"] == 15, d
    assert abs(d["temp_C"] - d["dewpoint_C"] - 4.0) < 1e-9
    assert d["sky_octas"] == 6
    print("station: T 22 C, Td 18 C, SLP 1013.2 hPa, wind 240 deg at 15 kt, 6/8 sky")
    print("spread 4 C and falling pressure ahead of the front - rain by evening")
    print("rule: the model packs a dozen numbers around one dot - read it at a glance")
    print("OK: %s decoded the plot" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_airmass_classify(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def classify(t_C, rh_pct):
    if t_C >= 20.0:
        return "mT" if rh_pct >= 55.0 else "cT"
    if t_C >= 0.0:
        return "mP" if rh_pct >= 55.0 else "cP"
    return "cA" if t_C < -15.0 else "cP"
def main():
    assert classify(28.0, 75.0) == "mT"
    assert classify(32.0, 20.0) == "cT"
    assert classify(5.0, 80.0) == "mP"
    assert classify(-5.0, 40.0) == "cP"
    assert classify(-25.0, 50.0) == "cA"
    cases = [(28.0, 75.0), (32.0, 20.0), (5.0, 80.0), (-5.0, 40.0)]
    for t, rh in cases:
        print("T=%d C RH=%d%% -> %s air mass" % (t, rh, classify(t, rh)))
    print("track the dew point, not just the temperature - moisture is the fingerprint")
    print("rule: source region writes the label; the trajectory rewrites it")
    print("OK: %s typed the air masses" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_frontal_slope(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def margules_slope(f, T0_K, dv_ms, dT_K, g=9.81):
    # tan(alpha) = f * T0 * dv / (g * dT)
    return f * T0_K * dv_ms / (g * dT_K)
def main():
    f = 1.0e-4  # Coriolis at mid-latitudes, 1/s
    cold = margules_slope(f, 280.0, 15.0, 8.0)
    warm = margules_slope(f, 285.0, 8.0, 10.0)
    assert 0.0 < cold < 0.02, cold
    assert 0.0 < warm < 0.02, warm
    assert cold > warm  # cold fronts steeper than warm fronts
    print("cold front slope 1:%.0f ; warm front slope 1:%.0f" % (1.0 / cold, 1.0 / warm))
    print("steeper wedge -> sharper lift -> narrower, more violent weather band")
    print("rule: density contrast plus shear sets the slope; the slope sets the weather")
    print("OK: %s sloped the fronts" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_cyclone_stages(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
STAGES = [
    ("frontal wave", 12, "wave on the stationary front, pressure begins to fall"),
    ("deepening", 24, "cold/warm fronts sharpen, comma cloud, strongest deepening"),
    ("occlusion", 18, "cold front catches warm front, heaviest precipitation wraps"),
    ("decay", 24, "cut off from warm fuel, low fills and drifts away"),
]
def main():
    names = [s[0] for s in STAGES]
    assert names == ["frontal wave", "deepening", "occlusion", "decay"], names
    total = sum(s[1] for s in STAGES)
    assert 48.0 < total < 120.0, total
    t = 0
    for name_s, hrs, desc in STAGES:
        print("hour %2d-%2d: %-12s - %s" % (t, t + hrs, name_s, desc))
        t += hrs
    print("bomb criterion: 24 hPa deepening in 24 h at 60 N - the explosive ones")
    print("rule: stage sets the weather for a thousand kilometers around")
    print("OK: %s ran the cyclone's life" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_geostrophic_wind(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
OMEGA = 7.2921159e-5
def coriolis(lat_deg):
    return 2.0 * OMEGA * math.sin(math.radians(lat_deg))
def geostrophic_ms(dZ_m, dn_m, lat_deg, g=9.81):
    return (g / coriolis(lat_deg)) * (dZ_m / dn_m)
def main():
    f = coriolis(45.0)
    assert abs(f - 1.031e-4) < 1e-6, f
    vg = geostrophic_ms(60.0, 200000.0, 45.0)
    assert abs(vg - 28.5) < 0.5, vg
    vg_tight = geostrophic_ms(120.0, 200000.0, 45.0)
    assert abs(vg_tight - 2.0 * vg) < 0.5
    print("60 m height fall over 200 km at 45 N -> geostrophic wind %.1f m/s (%.0f kt)" %
          (vg, vg * 1.94384))
    print("double the gradient -> double the wind; low heights to the left in the N. Hemisphere")
    print("rule: contours are streamlines aloft - packing is speed")
    print("OK: %s balanced the wind" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_jet_core(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def find_core(profile):
    # profile: list of (pressure_hPa, wind_kt)
    return max(profile, key=lambda p: p[1])
def thermal_wind_shear(u2, u1, z2_km, z1_km):
    return (u2 - u1) / (z2_km - z1_km)
def main():
    profile = [(850, 25), (700, 35), (500, 55), (300, 95), (250, 120), (200, 90), (100, 40)]
    p_core, v_core = find_core(profile)
    assert p_core == 250 and v_core == 120, (p_core, v_core)
    shear = thermal_wind_shear(120.0, 55.0, 10.4, 5.5)  # kt per km, 250mb~10.4km, 500mb~5.5km
    assert 10.0 < shear < 17.0, shear
    print("jet core: %d kt at %d hPa (~10.4 km)" % (v_core, p_core))
    print("thermal-wind shear 500->250 mb: %.1f kt/km - the temperature contrast made visible" % shear)
    print("entrance/exit quadrants: divergence in left-exit and right-entrance deepens surface lows")
    print("rule: find the core, read the quadrants, place the storm")
    print("OK: %s rode the jet" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_diurnal_breeze(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def diurnal_temp_C(hour, tmean=22.0, amp=8.0):
    # max at 15h, min at 3h
    return tmean + amp * math.sin(2.0 * math.pi * (hour - 9.0) / 24.0)
def breeze_state(land_C, water_C):
    if land_C - water_C > 3.0:
        return "sea breeze"
    if water_C - land_C > 1.0:
        return "land breeze"
    return "calm transition"
def main():
    t15 = diurnal_temp_C(15.0)
    t03 = diurnal_temp_C(3.0)
    assert abs(t15 - 30.0) < 1e-9 and abs(t03 - 14.0) < 1e-9, (t15, t03)
    assert t15 == max(diurnal_temp_C(h) for h in range(24))
    assert breeze_state(28.0, 20.0) == "sea breeze"
    assert breeze_state(16.0, 20.0) == "land breeze"
    assert breeze_state(21.0, 20.0) == "calm transition"
    print("diurnal range: %.0f C at 03h to %.0f C at 15h" % (t03, t15))
    print("15h land 28 C vs water 20 C -> sea breeze; 03h land 16 C -> land breeze")
    print("sea-breeze front by mid-afternoon can fire the day's thunderstorms")
    print("rule: land heats fast, water holds steady - the contrast is the engine")
    print("OK: %s breathed with the day" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_parcel_lcl(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def tlcl_K(t_K, rh_pct):
    # Bolton (1980) LCL temperature
    return 1.0 / (1.0 / (t_K - 55.0) - math.log(rh_pct / 100.0) / 2840.0) + 55.0
def lcl_height_km(t_C, rh_pct):
    t_K = t_C + 273.15
    return (t_K - tlcl_K(t_K, rh_pct)) / 8.0  # ~8 K/km dry-adiabatic
def main():
    tlcl = tlcl_K(293.15, 70.0)
    assert abs(tlcl - 286.1) < 0.5, tlcl
    z = lcl_height_km(20.0, 70.0)
    assert abs(z - 0.89) < 0.05, z
    z_dry = lcl_height_km(20.0, 30.0)
    assert z_dry > z  # drier surface -> higher cloud base
    print("T=20 C RH=70%% -> LCL temperature %.1f C, cloud base ~%.0f m" % (tlcl - 273.15, z * 1000))
    print("drier surface (RH 30%%) -> cloud base ~%.0f m - desert cumulus rides high" % (z_dry * 1000))
    print("lift the parcel dry-adiabatically to the LCL, moist above - the Skew-T made arithmetic")
    print("rule: the spread sets the base - small spread, low clouds")
    print("OK: %s lifted the parcel" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_storm_ingredients(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def score_ingredient(value, thresholds):
    # thresholds: (low, high) -> 0/1/2
    lo, hi = thresholds
    return 0 if value < lo else (1 if value < hi else 2)
def assess(cape, shear_kt, td_C, lift):
    s = (score_ingredient(cape, (500, 2500)) +
         score_ingredient(shear_kt, (20, 35)) +
         score_ingredient(td_C, (13, 18)) +
         (2 if lift in ("front", "dryline", "outflow") else (1 if lift == "heating" else 0)))
    return s, ("high" if s >= 7 else ("moderate" if s >= 5 else ("low" if s >= 3 else "none")))
def main():
    s, lvl = assess(2800, 40, 21.0, "dryline")
    assert s == 8 and lvl == "high", (s, lvl)
    s2, lvl2 = assess(800, 15, 12.0, "none")
    assert lvl2 in ("low", "none"), (s2, lvl2)
    s3, lvl3 = assess(2600, 25, 16.0, "heating")
    assert s3 == 5 and lvl3 == "moderate", (s3, lvl3)
    print("CAPE 2800, shear 40 kt, Td 21 C, dryline -> score %d/8: %s severe potential" % (s, lvl))
    print("missing lift or shear caps the day no matter how juicy the air")
    print("rule: moisture + instability + lift + shear - all four, or no severe")
    print("OK: %s mixed the ingredients" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ef_scale(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
EF = [("EF0", 65, 85), ("EF1", 86, 110), ("EF2", 111, 135),
      ("EF3", 136, 165), ("EF4", 166, 200), ("EF5", 201, 400)]
def ef_from_wind(mph):
    for rating, lo, hi in EF:
        if lo <= mph <= hi:
            return rating
    return "out of range"
def main():
    assert ef_from_wind(70) == "EF0"
    assert ef_from_wind(120) == "EF2"
    assert ef_from_wind(170) == "EF4"
    assert ef_from_wind(210) == "EF5"
    for rating, lo, hi in EF:
        print("%s: %d-%d mph 3-second gusts" % (rating, lo, hi if hi < 400 else 200))
    print("rated from 28 damage indicators AFTER the survey - never from radar alone")
    print("rule: damage writes the rating; the survey reads it back")
    print("OK: %s rated the damage" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hail_updraft(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def terminal_velocity_ms(d_m, rho_ice=900.0, Cd=0.6, rho_air=1.1, g=9.81):
    return math.sqrt(4.0 * g * d_m * rho_ice / (3.0 * Cd * rho_air))
def ms_to_kt(v): return v * 1.94384
def main():
    v_pea = terminal_velocity_ms(0.01)    # 1 cm
    v_golf = terminal_velocity_ms(0.043)  # golf ball
    v_soft = terminal_velocity_ms(0.10)   # softball
    assert abs(ms_to_kt(v_pea) - 26.0) < 3.0, ms_to_kt(v_pea)
    assert abs(ms_to_kt(v_golf) - 54.0) < 6.0, ms_to_kt(v_golf)
    assert ms_to_kt(v_soft) > 80.0, ms_to_kt(v_soft)
    print("updraft needed to suspend: 1-cm stone %.0f kt, golf ball %.0f kt, softball %.0f kt" %
          (ms_to_kt(v_pea), ms_to_kt(v_golf), ms_to_kt(v_soft)))
    print("softball hail means a 100-kt updraft - only the strongest supercells qualify")
    print("rule: the updraft must beat gravity, or the stone falls")
    print("OK: %s weighed the hailstones" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_flash_bang(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def miles(sec): return sec / 5.0
def km(sec): return sec / 3.0
def thirty_thirty(sec_since_flash):
    return "SHELTER NOW" if sec_since_flash < 30 else "caution"
def main():
    assert abs(miles(12.0) - 2.4) < 1e-9
    assert abs(km(12.0) - 4.0) < 1e-9
    assert thirty_thirty(12.0) == "SHELTER NOW"
    assert thirty_thirty(45.0) == "caution"
    print("12 s flash-to-bang -> strike %.1f miles (%.0f km) away -> %s" %
          (miles(12.0), km(12.0), thirty_thirty(12.0)))
    print("wait 30 minutes after the last thunder - half of deaths come after the rain ends")
    print("rule: hear thunder, you are in range - substantial building or hard-topped vehicle")
    print("OK: %s timed the lightning" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_fog_point(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def hours_to_fog(t_C, td_C, cooling_C_per_h):
    return max(0.0, (t_C - td_C) / cooling_C_per_h)
def fog_expected(t_low_C, td_C):
    return t_low_C <= td_C
def main():
    h = hours_to_fog(12.0, 9.0, 2.0)
    assert abs(h - 1.5) < 1e-9, h
    assert fog_expected(7.0, 9.0) is True
    assert fog_expected(11.0, 9.0) is False
    print("evening T 12 C, Td 9 C, cooling 2 C/h -> saturation in %.1f h" % h)
    print("forecast low 7 C <= fog point 9 C -> fog; low 11 C -> no fog")
    print("wind under ~5 kt lets it form; 5-10 kt mixes it to stratus; stronger kills it")
    print("rule: the spread is the fuse - cooling lights it")
    print("OK: %s forecast the fog" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_snow_ratio(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def snow_ratio(t850_C):
    if t850_C > 0.0: return 0.0  # rain
    if t850_C <= -10.0: return 20.0
    if t850_C <= -5.0: return 15.0
    return 10.0
def snow_inches(liquid_in, t850_C):
    return liquid_in * snow_ratio(t850_C)
def main():
    assert snow_ratio(-12.0) == 20.0
    assert snow_ratio(-7.0) == 15.0
    assert snow_ratio(-2.0) == 10.0
    assert snow_ratio(2.0) == 0.0
    assert abs(snow_inches(1.0, -12.0) - 20.0) < 1e-9
    assert abs(snow_inches(0.5, -2.0) - 5.0) < 1e-9
    print("1.0 in liquid at T850 -12 C -> %.0f in snow (20:1 dendritic powder)" % snow_inches(1.0, -12.0))
    print("same liquid at -2 C -> %.0f in (10:1); wet spring snow runs 5:1 and snaps lines" %
          snow_inches(1.0, -2.0))
    print("rule: 10:1 is the average, not the forecast - the profile sets the ratio")
    print("OK: %s ratioed the snow" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_lake_effect_check(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def lake_effect(lake_T_C, t850_C, fetch_km, wind_align_deg):
    delta_T = lake_T_C - t850_C
    ok = (delta_T >= 13.0 and fetch_km >= 100.0 and abs(wind_align_deg) <= 30.0)
    return ok, delta_T
def main():
    ok, dT = lake_effect(8.0, -12.0, 250.0, 10.0)
    assert ok is True and abs(dT - 20.0) < 1e-9, (ok, dT)
    ok2, _ = lake_effect(8.0, -2.0, 250.0, 10.0)
    assert ok2 is False   # delta-T too small
    ok3, _ = lake_effect(8.0, -12.0, 40.0, 10.0)
    assert ok3 is False   # fetch too short
    ok4, _ = lake_effect(8.0, -12.0, 250.0, 60.0)
    assert ok4 is False   # wind across the short axis
    print("lake 8 C, 850 mb -12 C -> delta-T %.0f C (>=13), fetch 250 km, aligned -> LAKE EFFECT" % dT)
    print("kill any one leg - delta-T, fetch, alignment - and the machine stops")
    print("rule: 20-degree wind shift moves the band off the city - nowcast the band, not the county")
    print("OK: %s fired the snow machine" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_orographic_lift(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def windward_cooling_C(ascent_m, moist=True):
    rate = 6.0 if moist else 9.8  # C per km
    return ascent_m / 1000.0 * rate
def chinook_warming_C(descent_m):
    return descent_m / 1000.0 * 9.8
def main():
    cool = windward_cooling_C(1500.0)
    assert abs(cool - 9.0) < 1e-9, cool
    warm = chinook_warming_C(2000.0)
    assert abs(warm - 19.6) < 0.01, warm
    warm_F = warm * 9.0 / 5.0
    assert 30.0 < warm_F < 40.0, warm_F
    print("1500 m moist ascent -> %.0f C cooling to saturation - windward deluge" % cool)
    print("2000 m lee descent -> +%.1f C (+%.0f F) - the chinook snow-eater" % (warm, warm_F))
    print("moisture lost windward never comes back - that is the rain shadow's arithmetic")
    print("rule: up moist and slow, down dry and fast")
    print("OK: %s crossed the range" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_beaufort_waves(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
BEAUFORT = [(0, 1, "calm"), (1, 3, "light air"), (4, 6, "light breeze"),
            (7, 10, "gentle breeze"), (11, 16, "moderate breeze"),
            (17, 21, "fresh breeze"), (22, 27, "strong breeze"),
            (28, 33, "near gale"), (34, 40, "gale"),
            (41, 47, "strong gale"), (48, 55, "storm"),
            (56, 63, "violent storm"), (64, 200, "hurricane force")]
def beaufort(kt):
    for lo, hi, desc in BEAUFORT:
        if lo <= kt <= hi:
            return desc
    return "beyond scale"
def sig_wave_height_m(u_ms, g=9.81):
    # fully developed sea approximation
    return 0.21 * u_ms * u_ms / g
def main():
    assert beaufort(38) == "gale"
    assert beaufort(70) == "hurricane force"
    assert beaufort(9) == "gentle breeze"
    h = sig_wave_height_m(20.0)
    assert abs(h - 8.56) < 0.05, h
    h2 = sig_wave_height_m(10.0)
    assert h2 < h / 3.0  # height grows with wind squared
    print("38 kt -> %s; 70 kt -> %s" % (beaufort(38), beaufort(70)))
    print("20 m/s sustained -> fully developed seas ~%.1f m; 10 m/s -> ~%.1f m" % (h, h2))
    print("warnings: small craft 25-33 kt, gale 34-47, storm 48+, hurricane-force 64+")
    print("rule: wind speed, duration, fetch - the sea keeps all three accounts")
    print("OK: %s read the sea state" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_wave_track(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def wave_position_nm(lon0_deg, hours, speed_kt=12.0):
    # westward motion; 60 nm per degree at the equator-ish tropics
    return lon0_deg - (speed_kt * hours) / 60.0
def main():
    lon48 = wave_position_nm(-20.0, 48.0)
    assert abs(lon48 - (-29.6)) < 0.01, lon48
    lon120 = wave_position_nm(-20.0, 120.0, 15.0)
    assert abs(lon120 - (-50.0)) < 0.01, lon120
    print("wave off Africa at 20 W, 12 kt -> 48 h later at %.1f W (%.0f nm traveled)" %
          (-lon48, 12.0 * 48))
    print("at 15 kt for 5 days: %.0f W - approaching the Lesser Antilles window" % (-lon120))
    print("the wave's east side holds the convection; a closed low marks cyclogenesis")
    print("rule: track every wave - most hurricanes start as one")
    print("OK: %s tracked the wave" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hurricane_scale(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
SAFFIR_SIMPSON = [(74, 95, 1), (96, 110, 2), (111, 129, 3), (130, 156, 4), (157, 300, 5)]
def category(mph):
    for lo, hi, cat in SAFFIR_SIMPSON:
        if lo <= mph <= hi:
            return cat
    return 0
def main():
    assert category(80) == 1
    assert category(100) == 2
    assert category(120) == 3
    assert category(140) == 4
    assert category(160) == 5
    for lo, hi, cat in SAFFIR_SIMPSON:
        print("Category %d: %d-%d mph sustained" % (cat, lo, hi if hi < 300 else 157))
    print("the scale rates WIND only - surge and rain kill on their own schedules")
    print("rule: never judge a hurricane by its category alone")
    print("OK: %s scaled the hurricane" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_feels_like(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def heat_index_F(T_F, RH):
    # Rothfusz regression
    T, R = T_F, RH
    hi = (-42.379 + 2.04901523 * T + 10.14333127 * R - 0.22475541 * T * R
          - 0.00683783 * T * T - 0.05481717 * R * R + 0.00122874 * T * T * R
          + 0.00085282 * T * R * R - 0.00000199 * T * T * R * R)
    return hi
def wind_chill_F(T_F, V_mph):
    return (35.74 + 0.6215 * T_F - 35.75 * (V_mph ** 0.16)
            + 0.4275 * T_F * (V_mph ** 0.16))
def main():
    hi = heat_index_F(90.0, 70.0)
    assert 100.0 < hi < 112.0, hi
    wc = wind_chill_F(20.0, 30.0)
    assert -5.0 < wc < 8.0, wc
    assert heat_index_F(90.0, 40.0) < hi   # drier -> lower apparent temp
    assert wind_chill_F(20.0, 5.0) > wc   # calmer -> warmer feel
    print("90 F at 70%% humidity feels like %.0f F - sweat cannot evaporate" % hi)
    print("20 F in 30 mph wind feels like %.0f F - frostbite in ~30 min on exposed skin" % wc)
    print("heat waves kill more than any other weather hazard - warn on thresholds, not records")
    print("rule: humidity rewrites heat, wind rewrites cold")
    print("OK: %s felt the extremes" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_haines_index(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def haines(t850_C, t700_C, td850_C):
    lapse = t850_C - t700_C
    A = 1 if lapse < 4.0 else (2 if lapse < 8.0 else 3)
    dd = t850_C - td850_C
    B = 1 if dd < 6.0 else (2 if dd < 13.0 else 3)
    return A + B, A, B
def main():
    h, A, B = haines(20.0, 8.0, 2.0)
    assert (A, B, h) == (3, 3, 6), (A, B, h)
    h2, _, _ = haines(17.0, 14.0, 13.0)
    assert h2 == 2, h2  # stable + moist = low
    h3, _, _ = haines(21.0, 14.0, 13.0)
    assert h3 == 4, h3
    print("lapse 12 C + dewpoint depression 18 C -> Haines %d (very high - plume-dominated fire)" % h)
    print("stable moist profile -> Haines %d (low); marginal -> %d" % (h2, h3))
    print("scale 2-6: 2-3 low, 4 moderate, 5 high, 6 very high")
    print("rule: unstable plus dry aloft - the fire builds its own weather")
    print("OK: %s scored the fire air" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_gdd_accumulate(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def daily_gdd_F(tmax_F, tmin_F, tbase=50.0):
    tmax = min(tmax_F, 86.0)
    tmin = max(tmin_F, 50.0)
    return max(0.0, (tmax + tmin) / 2.0 - tbase)
def main():
    assert abs(daily_gdd_F(86.0, 66.0) - 26.0) < 1e-9
    assert abs(daily_gdd_F(100.0, 70.0) - 28.0) < 1e-9  # heat capped at 86
    assert daily_gdd_F(45.0, 38.0) == 0.0
    week = [(84, 64), (88, 68), (79, 61), (90, 70), (82, 63), (77, 59), (85, 66)]
    total = sum(daily_gdd_F(h, l) for h, l in week)
    assert abs(total - 165.0) < 0.01, total
    print("week's accumulation: %.0f GDD (base 50 F, cap 86 F)" % total)
    print("corn needs ~2700 GDD to mature - thermal time, not calendar time")
    print("frost side: 28 F kills blossoms; forecast the low against the crop, not the record")
    print("rule: crops and insects both run on degree days")
    print("OK: %s banked the heat units" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_dbz_rainrate(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def dbz_to_Z(dbz):
    return 10.0 ** (dbz / 10.0)
def rainrate_mmh(dbz, a=300.0, b=1.4):
    return (dbz_to_Z(dbz) / a) ** (1.0 / b)
def couplet_shear_kt(v_in, v_out, dist_nm):
    return abs(v_out - v_in) / dist_nm
def main():
    r = rainrate_mmh(50.0)
    assert 50.0 < r < 80.0, r
    assert rainrate_mmh(20.0) < 1.0
    assert rainrate_mmh(65.0) > 150.0  # hail core territory
    shear = couplet_shear_kt(-60.0, 55.0, 2.0)
    assert abs(shear - 57.5) < 0.01, shear
    print("50 dBZ -> ~%.0f mm/h rain; 20 dBZ -> drizzle; 65 dBZ -> hail core" % r)
    print("velocity couplet -60/+55 kt over 2 nm -> shear %.0f kt/nm - rotation" % shear)
    print("Z sums the sixth power of drop size - a few hailstones out-shout a field of rain")
    print("rule: reflectivity is anatomy, velocity is physiology - read both")
    print("OK: %s interrogated the echo" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ir_cloudtop(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def cloudtop_km(t_bright_C, surface_C=20.0, lapse_C_per_km=6.5):
    return (surface_C - t_bright_C) / lapse_C_per_km
DVORAK = {2.0: 35, 2.5: 40, 3.0: 45, 3.5: 55, 4.0: 65, 4.5: 77,
          5.0: 90, 5.5: 102, 6.0: 115, 6.5: 127, 7.0: 140, 7.5: 155, 8.0: 170}
def dvorak_wind_kt(ci):
    return DVORAK.get(round(ci * 2.0) / 2.0)
def main():
    z = cloudtop_km(-60.0)
    assert 10.0 < z < 15.0, z
    assert cloudtop_km(-30.0) < z
    assert dvorak_wind_kt(4.0) == 65
    assert dvorak_wind_kt(6.5) == 127
    assert dvorak_wind_kt(2.5) == 40
    print("IR brightness -60 C -> cloud top ~%.1f km - overshooting into the stratosphere" % z)
    print("Dvorak CI 4.0 -> %d kt; CI 6.5 -> %d kt - pattern to number since the 1970s" %
          (dvorak_wind_kt(4.0), dvorak_wind_kt(6.5)))
    print("water-vapor dark slots mark descending dry air - the cyclone's dry slot")
    print("rule: visible shows the face, IR the height, water vapor the machinery")
    print("OK: %s read the satellite" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_storm_extrapolate(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def extrapolate(lat, lon, dir_deg, speed_kt, minutes):
    # simple flat-earth extrapolation; 60 nm per degree
    nm = speed_kt * minutes / 60.0
    r = math.radians(dir_deg)
    dlat = nm * math.cos(r) / 60.0
    dlon = nm * math.sin(r) / (60.0 * math.cos(math.radians(lat)))
    return lat + dlat, lon + dlon
def main():
    lat, lon = extrapolate(35.0, -97.5, 250.0, 30.0, 30.0)
    # 15 nm toward 250 deg from (35.0, -97.5)
    assert abs(lat - (35.0 + 15.0 * math.cos(math.radians(250.0)) / 60.0)) < 1e-9
    assert lon < -97.5  # moving west-ish (250 deg)
    lat2, lon2 = extrapolate(35.0, -97.5, 90.0, 20.0, 60.0)
    assert abs(lon2 - (-97.5 + 20.0 / (60.0 * math.cos(math.radians(35.0))))) < 1e-9
    print("storm at 35.0N 97.5W moving 250 deg at 30 kt -> 30 min later %.2fN %.2fW" % (lat, -lon))
    print("extrapolation is the best 0-60 min forecast - then diagnosis adjusts for the environment")
    print("rule: advect the echo, interrogate the air it is moving into")
    print("OK: %s extrapolated the storm" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_cfl_timestep(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def max_dt_s(dx_m, c_ms):
    return dx_m / c_ms
def main():
    dt_sound = max_dt_s(3000.0, 300.0)
    assert abs(dt_sound - 10.0) < 1e-9, dt_sound
    dt_adv = max_dt_s(3000.0, 50.0)
    assert abs(dt_adv - 60.0) < 1e-9
    dt_global = max_dt_s(13000.0, 300.0)
    assert abs(dt_global - 43.33) < 0.01
    print("3-km grid, 300 m/s waves -> timestep <= %.0f s; advection only -> %.0f s" %
          (dt_sound, dt_adv))
    print("13-km global grid -> <= %.0f s per step; finer grids cost superlinearly" % dt_global)
    print("violate CFL and the solution blows up - the numerics are non-negotiable")
    print("rule: information cannot cross more than one grid cell per step")
    print("OK: %s stepped the model" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ensemble_prob(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def probability(members, threshold):
    return sum(1 for m in members if m >= threshold) / len(members)
def spread(members):
    mean = sum(members) / len(members)
    return math.sqrt(sum((m - mean) ** 2 for m in members) / len(members))
def main():
    ens = [0.8, 1.2, 0.5, 2.1, 1.5, 0.9, 1.8, 0.3, 1.1, 2.4,
           0.7, 1.6, 1.0, 0.4, 1.9, 1.3, 0.6, 2.0, 1.4, 0.9]
    p = probability(ens, 1.5)
    assert abs(p - 0.35) < 1e-9, p
    assert probability(ens, 0.0) == 1.0
    assert probability(ens, 5.0) == 0.0
    s = spread(ens)
    assert 0.4 < s < 0.9, s
    print("20 members, 7 at/above 1.5 in -> P(rain >= 1.5 in) = %.0f%%; spread %.2f in" % (100 * p, s))
    print("tight bundle = confidence; spray = the atmosphere has not decided")
    print("rule: the fraction IS the forecast - probabilities are decidable, determinism is a story")
    print("OK: %s priced the uncertainty" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_mos_regression(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def linfit(xs, ys):
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    b = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    return my - b * mx, b
def main():
    # model runs 3 F warm with slope 0.9: obs = 0.9*model + 1.0 + noise-free
    model = [40.0, 45.0, 50.0, 55.0, 60.0, 65.0, 70.0, 75.0]
    obs = [0.9 * m + 1.0 for m in model]
    a, b = linfit(model, obs)
    assert abs(a - 1.0) < 1e-9 and abs(b - 0.9) < 1e-9, (a, b)
    corrected = a + b * 68.0
    assert abs(corrected - 62.2) < 1e-9
    print("MOS learned: observed = %.1f + %.2f x model (model runs warm, slope < 1)" % (a, b))
    print("raw model says 68 F -> MOS corrects to %.1f F" % corrected)
    print("rebuilt after every model upgrade, per station, per lead time")
    print("rule: the model's history is the model's confession - regress it")
    print("OK: %s corrected the model" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_verify_scores(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def scores(hits, misses, fa, cn):
    pod = hits / (hits + misses)
    far = fa / (hits + fa) if (hits + fa) else 0.0
    csi = hits / (hits + misses + fa)
    bias = (hits + fa) / (hits + misses)
    return pod, far, csi, bias
def brier(forecasts, observed):
    return sum((f - o) ** 2 for f, o in zip(forecasts, observed)) / len(forecasts)
def main():
    pod, far, csi, bias = scores(8, 2, 3, 87)
    assert abs(pod - 0.8) < 1e-9, pod
    assert abs(far - 3.0 / 11.0) < 1e-9, far
    assert abs(csi - 8.0 / 13.0) < 1e-9, csi
    assert abs(bias - 1.1) < 1e-9, bias
    bs = brier([0.1, 0.8, 0.6], [0, 1, 1])
    assert abs(bs - 0.07) < 1e-9, bs
    print("hits 8, misses 2, false alarms 3: POD %.2f, FAR %.2f, CSI %.2f, bias %.2f" %
          (pod, far, csi, bias))
    print("Brier score on 3 probability forecasts: %.3f (perfect = 0)" % bs)
    print("POD rewards catching; FAR punishes crying wolf; CSI balances; bias exposes lean")
    print("rule: a forecast never scored is a story - verify everything")
    print("OK: %s graded the forecasts" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_metar_decode(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
METAR_RE = re.compile(
    r"^(\\w{4})\\s+(\\d{2})(\\d{2})(\\d{2})Z\\s+(\\d{3}|VRB)(\\d{2,3})(G(\\d{2,3}))?KT\\s+"
    r"(\\d+|M?\\d/\\d)?SM\\s+(.*?)\\s+(M?\\d+)/(M?\\d+)\\s+A(\\d{4})$")
def p_temp(s):
    return -int(s[1:]) if s.startswith("M") else int(s)
def decode(metar):
    m = METAR_RE.match(metar.strip())
    assert m, "unparseable METAR"
    g = m.groups()
    return {"station": g[0], "day": int(g[1]), "hour": int(g[2]), "min": int(g[3]),
            "wind_dir": g[4], "wind_kt": int(g[5]), "gust_kt": int(g[7]) if g[7] else None,
            "vis_sm": g[8], "sky": g[9].strip(), "temp_C": p_temp(g[10]),
            "dew_C": p_temp(g[11]), "altim_inhg": int(g[12]) / 100.0}
def main():
    d = decode("KJFK 171651Z 28012KT 10SM FEW045 SCT250 22/14 A2992")
    assert d["station"] == "KJFK" and d["wind_kt"] == 12 and d["wind_dir"] == "280"
    assert d["temp_C"] == 22 and d["dew_C"] == 14
    assert abs(d["altim_inhg"] - 29.92) < 1e-9
    assert d["sky"] == "FEW045 SCT250"
    d2 = decode("KDEN 172353Z 34018G26KT 1SM -SN BKN008 M02/M05 A2980")
    assert d2["gust_kt"] == 26 and d2["temp_C"] == -2 and d2["dew_C"] == -5
    print("KJFK: wind 280/12 kt, vis 10 SM, %s, T/Td 22/14 C, altimeter %.2f" %
          (d["sky"], d["altim_inhg"]))
    print("KDEN: gusts 26 kt, light snow, T/Td M02/M05 - winter ops in effect")
    print("rule: the code is terse because the cockpit is busy - decode it cold")
    print("OK: %s decoded the METAR" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_spi_category(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def zscore(series, x):
    n = len(series)
    mean = sum(series) / n
    sd = math.sqrt(sum((v - mean) ** 2 for v in series) / (n - 1))
    return (x - mean) / sd
def spi_category(z):
    if z <= -2.0: return "extreme drought"
    if z <= -1.5: return "severe drought"
    if z <= -1.0: return "moderate drought"
    if z < 1.0: return "near normal"
    if z < 1.5: return "moderately wet"
    if z < 2.0: return "very wet"
    return "extremely wet"
def main():
    rain = [95.0, 110.0, 88.0, 120.0, 105.0, 92.0, 115.0, 100.0, 108.0, 97.0,
            112.0, 90.0, 118.0, 102.0, 96.0, 109.0, 93.0, 114.0, 99.0, 107.0]
    z_med = zscore(rain, 103.0)
    assert abs(z_med) < 0.3, z_med
    assert spi_category(z_med) == "near normal"
    z_dry = zscore(rain, 60.0)
    assert z_dry < -2.0, z_dry
    assert spi_category(z_dry) == "extreme drought"
    z_wet = zscore(rain, 140.0)
    assert spi_category(z_wet) == "extremely wet"
    print("season 103 mm -> SPI %+.2f (%s)" % (z_med, spi_category(z_med)))
    print("season 60 mm -> SPI %.2f (%s); 140 mm -> %s" %
          (z_dry, spi_category(z_dry), spi_category(z_wet)))
    print("1-month SPI for flash drought, 12-month for reservoirs - match the scale to the user")
    print("rule: standardize the deficit - minus 2 is extreme, whatever normal was")
    print("OK: %s indexed the drought" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_warn_decision(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def decide(couplet_kt_per_nm, debris_sig, spotter, lightning_jump):
    score = 0
    if couplet_kt_per_nm >= 40: score += 2
    elif couplet_kt_per_nm >= 25: score += 1
    if debris_sig: score += 3
    if spotter in ("funnel", "tornado"): score += 3
    elif spotter == "wall cloud": score += 1
    if lightning_jump: score += 1
    if score >= 5: return "TORNADO WARNING"
    if score >= 3: return "SEVERE THUNDERSTORM WARNING"
    if score >= 1: return "SPECIAL WEATHER STATEMENT"
    return "MONITOR"
def main():
    assert decide(55, True, "tornado", True) == "TORNADO WARNING"
    assert decide(45, False, "funnel", False) == "TORNADO WARNING"
    assert decide(45, False, "none", True) == "SEVERE THUNDERSTORM WARNING"
    assert decide(10, False, "none", False) == "MONITOR"
    assert decide(45, False, "wall cloud", False) == "SEVERE THUNDERSTORM WARNING"
    cases = [(55, True, "tornado", True), (45, False, "none", True), (10, False, "none", False)]
    for c in cases:
        print("couplet %d, debris %s, spotter %s -> %s" % (c[0], c[1], c[2], decide(*c)))
    print("polygon the threat, not the county - warn the path, spare the rest")
    print("rule: evidence in, decision out - and every warn gets verified")
    print("OK: %s made the call" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nowcast_trend(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def persistence(last, steps):
    return [last] * steps
def trend_extrapolate(series, steps):
    # linear trend from last two points
    slope = series[-1] - series[-2]
    return [series[-1] + slope * (i + 1) for i in range(steps)]
def mae(pred, actual):
    return sum(abs(p - a) for p, a in zip(pred, actual)) / len(pred)
def main():
    tops_C = [-40.0, -45.0, -52.0]          # cloud tops cooling: developing storm
    actual = [-60.0, -68.0]
    e_persist = mae(persistence(tops_C[-1], 2), actual)
    e_trend = mae(trend_extrapolate(tops_C, 2), actual)
    assert e_trend < e_persist, (e_trend, e_persist)
    print("cloud tops -40 -> -45 -> -52 C; persistence says -52, trend says -59/-66")
    print("actual -60/-68: persistence error %.1f C, trend error %.1f C" % (e_persist, e_trend))
    print("a tower cooling 10+ C in 15 min is about to become a thunderstorm")
    print("rule: nowcast the tendency, not the snapshot")
    print("OK: %s caught the trend" % NAME)
if __name__ == "__main__":
    main()
''')

DEMOS = {
    "meteo_branches": demo_meteo_branches, "unit_conversions": demo_unit_conversions,
    "network_coverage": demo_network_coverage, "station_model": demo_station_model,
    "airmass_classify": demo_airmass_classify, "frontal_slope": demo_frontal_slope,
    "cyclone_stages": demo_cyclone_stages, "geostrophic_wind": demo_geostrophic_wind,
    "jet_core": demo_jet_core, "diurnal_breeze": demo_diurnal_breeze,
    "parcel_lcl": demo_parcel_lcl, "storm_ingredients": demo_storm_ingredients,
    "ef_scale": demo_ef_scale, "hail_updraft": demo_hail_updraft,
    "flash_bang": demo_flash_bang, "fog_point": demo_fog_point,
    "snow_ratio": demo_snow_ratio, "lake_effect_check": demo_lake_effect_check,
    "orographic_lift": demo_orographic_lift, "beaufort_waves": demo_beaufort_waves,
    "wave_track": demo_wave_track, "hurricane_scale": demo_hurricane_scale,
    "feels_like": demo_feels_like, "haines_index": demo_haines_index,
    "gdd_accumulate": demo_gdd_accumulate, "dbz_rainrate": demo_dbz_rainrate,
    "ir_cloudtop": demo_ir_cloudtop, "storm_extrapolate": demo_storm_extrapolate,
    "cfl_timestep": demo_cfl_timestep, "ensemble_prob": demo_ensemble_prob,
    "mos_regression": demo_mos_regression, "verify_scores": demo_verify_scores,
    "metar_decode": demo_metar_decode, "spi_category": demo_spi_category,
    "warn_decision": demo_warn_decision, "nowcast_trend": demo_nowcast_trend,
}

# ---------------------------------------------------------------- records

def build_records(slug, source):
    cfg = DBCFG[slug]
    sig = source == "signature"
    # Teaching-ladder order: stable sort by ladder_rank (entries are already
    # in ladder order in entries_meteorology.py).
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
    for slug in ("meteorology", "meteorology-signature"):
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
