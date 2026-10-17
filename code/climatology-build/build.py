#!/usr/bin/env python3
"""Build the Climatology field databases for JAH Databases (field #12, taxonomy order).

Verified 2026-10-17: NO database covers climatology as a science. The
'weather-climate' database (10,000 records) is a deterministic weather
observation catalog - synthetic station readings (JAH-WX ids with
temperature, humidity, precipitation, wind) with no climate-system science:
no forcings, no feedbacks, no general circulation, no Koeppen
classification, no paleoclimate, no climate modeling, no climate-change
science. So this build creates two NEW databases:

  climatology              — The Climatology Database (public-harvest: real,
                             fact-checked climatology - what climatology is;
                             weather vs climate; Earth's energy balance; the
                             greenhouse effect; albedo; latitude, tilt, and
                             the seasons; layers of the atmosphere; the water
                             cycle; pressure gradients and wind; the Coriolis
                             effect; the three-cell circulation; jet
                             streams; ocean currents and heat transport; the
                             Koeppen climate classification; monsoons;
                             El Nino and La Nina (ENSO); the North Atlantic
                             Oscillation and teleconnections; climate
                             forcings; climate feedbacks; climate
                             sensitivity; the carbon cycle; the ozone layer;
                             urban heat islands; dendroclimatology (tree
                             rings); ice cores; general circulation models;
                             paleoclimate: the ice ages; Milankovitch
                             cycles; the thermohaline circulation;
                             attribution of climate change; climate tipping
                             points; sea level rise; geoengineering;
                             frontiers of climatology)
  climatology-signature    — The Climatology Signature Database (his original
                             Signature interpretation; src signature, titles
                             suffixed " (Signature Edition)", never presented
                             as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
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
from entries_climatology import ENTRIES, SIG_TAIL

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature interpretation of climatology: "
                "clearly labeled Signature-made, never presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked climatology: what climatology is; "
                "weather vs climate; Earth's energy balance; the greenhouse effect; albedo; "
                "latitude, tilt, and the seasons; layers of the atmosphere; the water cycle; "
                "pressure gradients and wind; the Coriolis effect; the three-cell circulation; "
                "jet streams; ocean currents and heat transport; the Koeppen climate "
                "classification; monsoons; El Nino and La Nina (ENSO); the North Atlantic "
                "Oscillation and teleconnections; climate forcings; climate feedbacks; climate "
                "sensitivity; the carbon cycle; the ozone layer; urban heat islands; "
                "dendroclimatology (tree rings); ice cores; general circulation models; "
                "paleoclimate: the ice ages; Milankovitch cycles; the thermohaline "
                "circulation; attribution of climate change; climate tipping points; sea level "
                "rise; geoengineering; frontiers of climatology, organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations (what climatology "
              "is, weather vs climate, Earth's energy balance, the greenhouse effect, albedo, "
              "latitude/tilt/seasons, atmospheric layers, the water cycle, pressure gradients "
              "and wind, the Coriolis effect, the three-cell circulation, jet streams, ocean "
              "heat transport, the Koeppen classification) -> Compounded (monsoons, ENSO, the "
              "NAO and teleconnections, climate forcings, climate feedbacks, climate "
              "sensitivity, the carbon cycle, the ozone layer, urban heat islands, tree rings, "
              "ice cores) -> Advanced (general circulation models, the ice ages, Milankovitch "
              "cycles, the thermohaline circulation, attribution, tipping points, sea level "
              "rise, geoengineering, frontiers of climatology).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search greenhouse, Koeppen, ENSO, Milankovitch, feedback, sea level...",
        "chat_ph": "Ask about climatology...",
        "archive_blurb": ("Seeded %s climatology records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled structural climatology studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about climatology - from the greenhouse effect and the Koeppen map up to Milankovitch cycles, tipping points, and sea level rise." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "climatology-study", "gen_demo_kind": "climatology-demo",
        "source": source,
    }

CIT_PUB = "Climatology (peer-reviewed literature and standard textbooks)."
CIT_SIG = CIT_PUB + " " + SIG_TAIL

DBCFG = {}
DBCFG["climatology"] = _cfg(
    "climatology", "The Climatology Database",
    "Real, fact-checked climatology: Earth's energy balance, the greenhouse effect, "
    "albedo, seasons, atmospheric layers, the water cycle, winds and the Coriolis "
    "effect, the general circulation, jet streams, ocean heat transport, the Koeppen "
    "classification, monsoons, ENSO, teleconnections, forcings, feedbacks, climate "
    "sensitivity, the carbon cycle, the ozone layer, urban heat islands, tree rings, "
    "ice cores, climate models, ice ages, Milankovitch cycles, the thermohaline "
    "circulation, attribution, tipping points, sea level rise, geoengineering, and "
    "frontiers.",
    "climatology record", "JAH-CL-", "JAH Climatology Archivist",
    "climatology archivist - Earth's energy balance, the greenhouse effect, albedo, "
    "latitude and seasons, atmospheric layers, the water cycle, pressure-gradient wind, "
    "the Coriolis effect, the three-cell circulation, jet streams, ocean heat transport, "
    "the Koeppen classification, monsoons, ENSO, the NAO and teleconnections, climate "
    "forcings, feedbacks, climate sensitivity, the carbon cycle, the ozone layer, urban "
    "heat islands, dendroclimatology, ice cores, general circulation models, the ice "
    "ages, Milankovitch cycles, the thermohaline circulation, attribution of climate "
    "change, tipping points, sea level rise, geoengineering, frontiers; teaching "
    "progressively along the ladder from foundations through compounded to advanced; "
    "answers from many angles - definition, example, analogy, application, history, "
    "math, how-to - using only the system's own archive data",
    CIT_PUB, "public")
DBCFG["climatology-signature"] = _cfg(
    "climatology-signature", "The Climatology Signature Database",
    "His original Signature interpretation of climatology: the full ladder from the "
    "greenhouse effect and the Koeppen map to Milankovitch cycles, tipping points, and "
    "sea level rise, reframed as Signature science. Clearly labeled Signature-made, "
    "never presented as authentic public record.",
    "climatology record", "JAH-CSG-", "JAH Climatology Archivist (Signature)",
    "climatology archivist - Signature editions: his original Signature interpretation of "
    "climatology, clearly labeled Signature-made and never presented as authentic public "
    "record; teaches progressively along the ladder from foundations through compounded "
    "to advanced; answers from many angles - definition, example, analogy, application, "
    "history, math, how-to - using only the system's own archive data",
    CIT_SIG, "signature")

base.DBCFG = DBCFG

# ---------------------------------------------------------------- demos
# Every demo is real, runnable, stdlib-only Python performing the actual
# climatological calculation for its record. All are machine-executed by main().

_PREAMBLE = """import math
import re
"""

def _wrap(name, rid, group, body):
    return (base._hdr(name, rid, group) + _PREAMBLE + body.replace("NAME", json.dumps(name)))

def demo_climate_branches(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
BRANCHES = {
    "physical climatology": "energy budgets and radiation",
    "dynamic climatology": "the general circulation",
    "synoptic climatology": "weather systems and their statistics",
    "paleoclimatology": "climate of the deep past",
    "applied climatology": "climate services for people",
    "climate modeling": "the physics as running code",
}
def main():
    assert len(BRANCHES) == 6
    assert BRANCHES["paleoclimatology"] == "climate of the deep past"
    for branch, focus in BRANCHES.items():
        print("%-22s -> %s" % (branch, focus))
    print("rule: observations describe the pattern, physics explains it, models project it")
    print("OK: %s mapped the branches" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_weather_climate(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
MONTHLY = [2.1, 2.8, 6.4, 10.2, 14.8, 18.1, 20.4, 20.0, 16.2, 11.5, 6.3, 3.0]
def normal(temps):
    return sum(temps) / len(temps)
def anomaly(obs_annual, temps):
    return obs_annual - normal(temps)
def main():
    n = normal(MONTHLY)
    assert abs(n - 10.98) < 0.01, n
    a = anomaly(12.4, MONTHLY)
    assert abs(a - 1.42) < 0.01, a
    print("30-year normal annual mean: %.2f C" % n)
    print("a 12.4 C year -> anomaly %+.2f C (climate signal, not weather)" % a)
    print("rule: climate is the statistics; a single warm day is weather, a warm decade is climate")
    print("OK: %s separated weather from climate" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_energy_balance(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
S0, ALBEDO = 1361.0, 0.30
def absorbed(s0, albedo):
    return s0 * (1.0 - albedo) / 4.0
def main():
    q = absorbed(S0, ALBEDO)
    assert abs(q - 238.2) < 0.5, q
    print("solar constant %.0f W/m2 / 4 = %.1f W/m2 average input" % (S0, S0 / 4.0))
    print("minus %.0f%% reflected -> %.1f W/m2 absorbed" % (100 * ALBEDO, q))
    print("the planet must radiate %.1f W/m2 back out, or warm until it does" % q)
    print("rule: divide by four (disc in, sphere out), subtract the albedo")
    print("OK: %s balanced the planet" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_greenhouse_effect(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
SIGMA = 5.67e-8
def effective_temp(absorbed_w_m2):
    return (absorbed_w_m2 / SIGMA) ** 0.25
def main():
    Te = effective_temp(238.2)
    assert abs(Te - 254.5) < 0.6, Te
    surface = 288.15
    gap = surface - Te
    print("effective radiating temperature: %.1f K = %.1f C" % (Te, Te - 273.15))
    print("observed surface: %.1f K = %.1f C" % (surface, surface - 273.15))
    print("greenhouse gap: %.1f C - the natural blanket" % gap)
    assert 32.0 < gap < 35.0
    print("rule: sigma T^4 - the surface warms until outgoing matches incoming")
    print("OK: %s measured the blanket" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_albedo(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
SURF = {"ocean": (0.71, 0.06), "ice_snow": (0.10, 0.80), "land": (0.19, 0.25)}
def surface_albedo():
    return sum(frac * alb for frac, alb in SURF.values())
def main():
    sa = surface_albedo()
    assert abs(sa - 0.170) < 0.005, sa
    clouds = 0.13
    total = sa + clouds
    assert abs(total - 0.30) < 0.01, total
    print("surface albedo: %.3f (ocean 6%%, ice 80%%, land 25%%, area-weighted)" % sa)
    print("+ cloud reflection ~%.2f -> planetary albedo %.2f" % (clouds, total))
    print("melt ice (0.80) to ocean (0.06): each %% of Earth darkened absorbs ~3.4 W/m2 more")
    print("rule: albedo is the (1 - alpha) multiplier on the whole solar input")
    print("OK: %s weighed the mirrors" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_seasons(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def declination(day_of_year):
    return -23.44 * math.cos(2.0 * math.pi * (day_of_year + 10) / 365.0)
def day_length_hours(lat_deg, dec_deg):
    lat, dec = math.radians(lat_deg), math.radians(dec_deg)
    cosH = -math.tan(lat) * math.tan(dec)
    cosH = max(-1.0, min(1.0, cosH))
    return 2.0 * math.degrees(math.acos(cosH)) / 15.0
def main():
    d = declination(172)          # June 21
    assert abs(d - 23.44) < 0.05, d
    dl = day_length_hours(40.0, d)
    assert abs(dl - 14.84) < 0.05, dl
    print("June 21: declination %+.2f deg" % d)
    print("day length at 40 N: %.2f h; at 40 S: %.2f h" %
          (dl, day_length_hours(-40.0, d)))
    print("equator gets ~2.5x the annual sun per m2 that the poles do")
    print("rule: tilt, not distance - the lean makes the seasons")
    print("OK: %s tilted the planet" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_atmosphere_layers(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
LAYERS = [("troposphere", 0, 12), ("stratosphere", 12, 50),
          ("mesosphere", 50, 85), ("thermosphere", 85, 600)]
def main():
    assert [b for _, b, _ in LAYERS] == sorted(b for _, b, _ in LAYERS)
    assert LAYERS[0][2] == 12 and LAYERS[1][1] == 12, "tropopause must join the layers"
    for name_, lo, hi in LAYERS:
        print("%-13s %4d - %4d km" % (name_, lo, hi))
    print("weather lives in the troposphere; ozone heats the stratosphere above it")
    print("rule: layers are defined by where the temperature lapse rate changes sign")
    print("OK: %s stacked the sky" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_water_cycle(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def residence_days(storage_km3, flux_km3_yr):
    return storage_km3 / flux_km3_yr * 365.0
def clausius_clapeyron_pct(dT):
    return 100.0 * (math.exp(0.07 * dT) - 1.0)
def main():
    rt = residence_days(12900.0, 505000.0)
    assert 9.0 < rt < 10.0, rt
    cc = clausius_clapeyron_pct(1.0)
    assert abs(cc - 7.25) < 0.1, cc
    print("atmospheric water: %.1f days from evaporation to rain" % rt)
    print("+1 C -> +%.1f%% water vapor (Clausius-Clapeyron)" % cc)
    print("P minus E: tropics positive (wet), subtropics negative (deserts)")
    print("rule: storage/flux is residence time; warming speeds the whole cycle")
    print("OK: %s ran the water cycle" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pressure_wind(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
RHO = 1.225
def coriolis_param(lat_deg):
    return 2.0 * 7.2921e-5 * math.sin(math.radians(lat_deg))
def geostrophic(dp_pa, dn_m, lat_deg):
    return dp_pa / (RHO * coriolis_param(lat_deg) * dn_m)
def main():
    f = coriolis_param(45.0)
    assert abs(f - 1.0313e-4) < 1e-6, f
    ug = geostrophic(400.0, 100000.0, 45.0)
    assert 31.0 < ug < 33.0, ug
    print("4 hPa over 100 km at 45 N -> geostrophic wind %.1f m/s" % ug)
    print("tight isobars = strong wind; the map is the forecast")
    print("surface friction turns it ~30 deg inward - feeding the low")
    print("rule: Ug = (1/rho f) dP/dn - wind along the isobars")
    print("OK: %s read the isobars" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_coriolis(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
OMEGA = 7.2921e-5
def f(lat_deg):
    return 2.0 * OMEGA * math.sin(math.radians(lat_deg))
def deflect(lat_deg):
    return "right" if f(lat_deg) > 0 else ("left" if f(lat_deg) < 0 else "none")
def main():
    assert abs(f(45.0) - 1.0313e-4) < 1e-6
    assert abs(f(0.0)) < 1e-12
    assert f(-30.0) < 0.0
    for lat in (60.0, 30.0, 0.0, -30.0, -60.0):
        print("lat %+5.0f: f = %+.2e /s -> deflect %s" % (lat, f(lat), deflect(lat)))
    print("hurricanes spin CCW north, CW south - and none form at the equator")
    print("rule: f = 2 Omega sin(lat) - rotation's signature on every wind")
    print("OK: %s spun the frame" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_circulation_cells(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
CELLS = [("Hadley", 0, 30, "rises at equator, sinks in subtropics - deserts"),
         ("Ferrel", 30, 60, "eddy-driven - westerlies and storm tracks"),
         ("Polar", 60, 90, "sinks at pole - polar easterlies")]
def main():
    assert CELLS[0][1] == 0 and CELLS[2][2] == 90
    assert all(lo < hi for _, lo, hi, _ in CELLS)
    for cell, lo, hi, job in CELLS:
        print("%-7s %2d-%2d deg: %s" % (cell, lo, hi, job))
    print("the cells exist to move excess tropical heat poleward")
    print("rule: hot air rises at the equator and must come down somewhere - at 30 deg")
    print("OK: %s looped the atmosphere" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_jet_streams(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
JETS = {"subtropical": {"lat": 30, "alt_km": 12, "speed_ms": 40},
        "polar": {"lat": 55, "alt_km": 10, "speed_ms": 60}}
def thermal_wind_shear(dTdy_K_per_m, T_K=250.0, f=1.0e-4):
    return -(9.81 / (f * T_K)) * dTdy_K_per_m
def main():
    shear = thermal_wind_shear(-1.0e-5)
    assert abs(shear - 3.92e-3) < 0.05e-3, shear
    jet_speed = shear * 10000.0
    assert 35.0 < jet_speed < 45.0, jet_speed
    for jet, d in JETS.items():
        print("%-11s jet: %d deg lat, %d km up, ~%d m/s" %
              (jet, d["lat"], d["alt_km"], d["speed_ms"]))
    print("20 K over 2000 km of contrast -> shear %.2e /s -> ~%.0f m/s over 10 km" %
          (shear, jet_speed))
    print("rule: thermal wind - temperature contrast with latitude becomes wind with height")
    print("OK: %s rode the jet" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ocean_currents(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
RHO, CP = 1025.0, 3990.0
def heat_pw(sv, dT_K):
    return RHO * CP * sv * 1.0e6 * dT_K / 1.0e15
def main():
    pw = heat_pw(30.0, 10.0)
    assert 1.1 < pw < 1.4, pw
    print("Gulf Stream: 30 Sv x 10 K of cooling -> %.2f PW poleward" % pw)
    print("the ocean and atmosphere split the heat-transport job roughly half and half")
    print("upwelling zones: cold water up, nutrients up, fisheries boom")
    print("rule: heat = rho cp V delta-T - the pipeline equation")
    print("OK: %s metered the current" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_koppen(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def classify(t_cold, t_warm, dry):
    if t_warm <= 10.0:
        return "E (polar)"
    if dry:
        return "B (arid)"
    if t_cold >= 18.0:
        return "A (tropical)"
    if t_cold >= -3.0:
        return "C (temperate)"
    return "D (continental)"
def main():
    cases = [((26.0, 29.0, False), "A (tropical)"), ((12.0, 8.0, False), "E (polar)"),
             ((20.0, 35.0, True), "B (arid)"), ((5.0, 22.0, False), "C (temperate)"),
             ((-15.0, 20.0, False), "D (continental)")]
    for (tc, tw, dry), want in cases:
        got = classify(tc, tw, dry)
        assert got == want, ((tc, tw, dry), got)
        print("coldest %+.0f C, warmest %+.0f C, dry=%s -> %s" % (tc, tw, dry, got))
    print("rule: temperature picks the letter, aridity can override to B")
    print("OK: %s lettered the climates" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_monsoon(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def monsoon_flow(t_land, t_ocean):
    dT = t_land - t_ocean
    return ("onshore moist flow - rains" if dT > 0 else
            "offshore dry flow - dry season"), dT
def main():
    summer, dTs = monsoon_flow(35.0, 28.0)
    winter, dTw = monsoon_flow(10.0, 22.0)
    assert dTs == 7.0 and dTw == -12.0
    assert summer.startswith("onshore") and winter.startswith("offshore")
    print("summer: land-ocean contrast %+.0f C -> %s" % (dTs, summer))
    print("winter: land-ocean contrast %+.0f C -> %s" % (dTw, winter))
    print("latent-heat feedback amplifies the summer low beyond the raw contrast")
    print("rule: land swings with the seasons, the ocean barely moves - the wind follows")
    print("OK: %s turned the monsoon" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_enso(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def classify_oni(series):
    run_hot = run_cold = 0
    for v in series[-5:]:
        run_hot = run_hot + 1 if v >= 0.5 else 0
        run_cold = run_cold + 1 if v <= -0.5 else 0
    if run_hot >= 5:
        return "El Nino"
    if run_cold >= 5:
        return "La Nina"
    return "neutral"
def main():
    el = [0.6, 0.8, 1.1, 1.3, 1.0, 0.7]
    la = [-0.6, -0.9, -1.2, -1.0, -0.8, -0.6]
    nu = [0.2, -0.1, 0.3, -0.2, 0.1, 0.0]
    assert classify_oni(el) == "El Nino"
    assert classify_oni(la) == "La Nina"
    assert classify_oni(nu) == "neutral"
    print("ONI >= +0.5 C x5 seasons -> El Nino; <= -0.5 C x5 -> La Nina")
    print("Bjerknes feedback: weak trades -> warm east -> weaker trades")
    print("teleconnections: the tropical nudge reorganizes weather worldwide")
    print("rule: the ocean remembers - subsurface heat predicts the flip months ahead")
    print("OK: %s read the Pacific" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nao(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def nao_index(p_azores, p_iceland, ref_az=1020.0, ref_ic=1000.0, sd=5.0):
    return (p_azores - ref_az) / sd - (p_iceland - ref_ic) / sd
def phase(idx):
    return "positive" if idx > 0.5 else ("negative" if idx < -0.5 else "neutral")
def main():
    pos = nao_index(1026.0, 994.0)
    neg = nao_index(1014.0, 1006.0)
    assert phase(pos) == "positive" and phase(neg) == "negative", (pos, neg)
    print("Azores 1026 / Iceland 994 hPa -> NAO %+.2f (%s): jet aimed at N. Europe" % (pos, phase(pos)))
    print("Azores 1014 / Iceland 1006 hPa -> NAO %+.2f (%s): storms sag south" % (neg, phase(neg)))
    print("Rossby waveguides carry tropical heating anomalies across the globe")
    print("rule: the pressure gradient steers the jet, the jet steers the storms")
    print("OK: %s weighed the Atlantic" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_forcings(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def co2_forcing(c, c0=278.0):
    return 5.35 * math.log(c / c0)
def main():
    d2x = co2_forcing(556.0)
    assert abs(d2x - 3.71) < 0.02, d2x
    now = co2_forcing(420.0)
    assert abs(now - 2.21) < 0.02, now
    print("doubled CO2 (278->556 ppm): %+.2f W/m2" % d2x)
    print("today (278->420 ppm):       %+.2f W/m2" % now)
    print("net human forcing ~+2.7 W/m2; solar ~+0.1; Pinatubo briefly -3")
    print("rule: 5.35 ln(C/C0) - logarithmic, each doubling adds the same")
    print("OK: %s posted the forcings" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_feedbacks(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
FEEDBACKS = {"water vapor": 1.6, "lapse rate": -0.6, "surface albedo": 0.3,
             "clouds": 0.4, "Planck": -3.2}   # W/m2 per K
def gain(total_f):
    return 1.0 / (1.0 - total_f)
def main():
    planck_only = -3.2
    others = sum(v for k, v in FEEDBACKS.items() if k != "Planck")
    f = -others / planck_only        # feedback factor convention
    assert abs(f - 0.53) < 0.02, f
    g = gain(f)
    dT = 1.2 * g
    assert abs(dT - 2.56) < 0.1, dT
    for k, v in FEEDBACKS.items():
        print("%-14s %+.1f W/m2/K" % (k, v))
    print("feedback factor %.2f -> gain %.2f -> 1.2 C becomes %.2f C" % (f, g, dT))
    print("rule: dT = dT0/(1-f) - the echo chamber equation; clouds are the wild card")
    print("OK: %s closed the loop" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_climate_sensitivity(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def ecs(forcing_2x=3.71, lam=1.2):
    return forcing_2x / lam
def main():
    e = ecs()
    assert 3.0 < e < 3.2, e
    print("ECS = 3.71 W/m2 / 1.2 W/m2/K = %.2f C per doubling" % e)
    print("TCR ~1.8 C (deep ocean lags); Charney 1979 already said 1.5-4.5 C")
    print("models + instruments + paleoclimate all converge near 3 C")
    print("rule: forcing divided by the feedback parameter - one number, whole planet")
    print("OK: %s set the dial" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_carbon_cycle(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
GT_PER_PPM = 2.13
def budget(emissions, ocean_sink, land_sink):
    airborne = emissions - ocean_sink - land_sink
    return airborne, airborne / emissions
def main():
    air, frac = budget(10.9, 2.8, 3.2)
    assert abs(frac - 0.45) < 0.02, frac
    ppm_yr = air / GT_PER_PPM
    assert 2.2 < ppm_yr < 2.5, ppm_yr
    print("emissions 10.9 GtC/yr - sinks 6.0 -> airborne %.1f GtC/yr (%.0f%%)" % (air, 100 * frac))
    print("= +%.1f ppm/yr on the Keeling curve" % ppm_yr)
    print("isotopes fingerprint it: falling C-13 and C-14 = fossil carbon")
    print("rule: what the sinks cannot take, the air keeps - about 45%")
    print("OK: %s balanced the carbon" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ozone(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def du_to_mm(du):
    return du / 100.0
def main():
    assert abs(du_to_mm(300.0) - 3.0) < 1e-9
    hole = du_to_mm(95.0)
    print("normal column 300 DU = %.1f mm at surface pressure" % du_to_mm(300.0))
    print("ozone-hole column 95 DU = %.2f mm - the shield worn paper-thin" % hole)
    print("one chlorine atom destroys ~100,000 ozone molecules (catalytic)")
    print("Montreal Protocol 1987 -> chlorine falling -> healing by mid-century")
    print("rule: Cl + O3 -> ClO + O2, ClO + O -> Cl + O2 - the catalyst survives")
    print("OK: %s patched the shield" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_uhi(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def island_intensity(t_urban, t_rural):
    return t_urban - t_rural
def main():
    nights = [("downtown", 24.5, "suburb", 20.8), ("city park", 21.9, "suburb", 20.8),
              ("cool-roof block", 22.6, "suburb", 20.8)]
    vals = []
    for un, ut, rn, rt in nights:
        d = island_intensity(ut, rt)
        vals.append(d)
        print("%-15s %+.1f C vs %s" % (un, d, rn))
    assert max(vals) > 3.0 and min(vals) < 2.0, vals
    print("trees and cool roofs shave degrees off the island")
    print("global records homogenize this out - the trend is not urban")
    print("rule: dark mass stores the day and returns it at night")
    print("OK: %s cooled the block" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tree_rings(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def detrend(widths):
    n = len(widths)
    xs = list(range(n))
    mx, my = sum(xs) / n, sum(widths) / n
    b = sum((x - mx) * (y - my) for x, y in zip(xs, widths)) / sum((x - mx) ** 2 for x in xs)
    a = my - b * mx
    return [a + b * x for x in xs]
def standardize(widths):
    trend = detrend(widths)
    return [w / t for w, t in zip(widths, trend)]
def main():
    widths = [3.2, 2.8, 2.5, 2.2, 2.0, 2.1, 1.9, 2.3, 2.0, 1.8]
    idx = standardize(widths)
    mean_idx = sum(idx) / len(idx)
    assert abs(mean_idx - 1.0) < 0.05, mean_idx
    assert idx[7] > 1.1, idx   # the wide ring stands out after detrending
    print("ring-width index: " + " ".join("%.2f" % v for v in idx))
    print("mean index %.3f - the age trend removed, the climate signal kept" % mean_idx)
    print("cross-dating fixes the exact year; bristlecones reach 5,000+ years")
    print("rule: divide out the age curve - what remains is weather's handwriting")
    print("OK: %s read the rings" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ice_cores(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def temp_from_d18o(delta, ref=-35.0):
    return (delta - ref) / 0.67
def main():
    dT = temp_from_d18o(-40.36)
    assert abs(dT - (-8.0)) < 0.15, dT
    print("delta-18O shift of -5.36 permil -> %.1f C colder" % dT)
    print("Vostok: CO2 180 ppm (ice age) <-> 280 ppm (warm) over 420,000 years")
    print("Dansgaard-Oeschger: up to 10 C swings within decades")
    print("bubbles are ancient air; ash layers date the depth")
    print("rule: heavy water condenses first - the colder the trip, the lighter the snow")
    print("OK: %s drilled the past" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_gcm(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def courant_dt(dx_m, c_ms):
    return dx_m / c_ms
def main():
    dt = courant_dt(100000.0, 300.0)
    assert abs(dt - 333.3) < 0.5, dt
    cells = 360 * 180 * 30
    assert cells == 1944000, cells
    print("100 km grid, 300 m/s waves -> max stable step %.0f s" % dt)
    print("grid: 360 x 180 x 30 levels = %d boxes" % cells)
    print("historical runs match 20th-century warming only with human forcings")
    print("rule: no signal may cross a box in one step - the Courant condition")
    print("OK: %s gridded the planet" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ice_ages(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def cycle_phase(years_ago, period=100000.0):
    return (years_ago % period) / period
def main():
    ph = cycle_phase(21000.0)
    assert abs(ph - 0.21) < 0.01, ph
    print("21,000 years ago: phase %.2f of the 100k-year cycle - the Last Glacial Maximum" % ph)
    print("LGM: ~6 C colder, ice miles thick, seas 120 m lower")
    print("pacemaker: 65 N summer insolation; amplifiers: ice-albedo, CO2, dust")
    print("early Pleistocene ran 41k-year cycles; the 100k rhythm took over ~1 Myr ago")
    print("rule: orbital wobble sets the beat, feedbacks play the music")
    print("OK: %s timed the ice" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_milankovitch(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
CYCLES = {"precession": 21000.0, "obliquity": 41000.0, "eccentricity": 100000.0}
def main():
    order = sorted(CYCLES, key=CYCLES.get)
    assert order == ["precession", "obliquity", "eccentricity"], order
    for cyc, per in CYCLES.items():
        print("%-12s period %6.0f years" % (cyc, per))
    print("tilt 22.1-24.5 deg; precession picks which summer sits at perihelion")
    print("sediment spectra show exactly these frequencies - prediction confirmed")
    print("rule: three gears, one sunlight dial, hundred-thousand-year time")
    print("OK: %s wound the clockwork" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_thermohaline(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
RHO, CP = 1025.0, 3990.0
def amoc_heat_pw(sv, dT_K):
    return RHO * CP * sv * 1.0e6 * dT_K / 1.0e15
def main():
    pw = amoc_heat_pw(17.0, 15.0)
    assert 0.9 < pw < 1.2, pw
    print("AMOC: 17 Sv x 15 K -> %.2f PW northward - Europe's warmth" % pw)
    print("full loop: ~1,000 years - the ocean's longest memory")
    print("Stommel 1961: two stable states - strong overturning or collapsed")
    print("Greenland meltwater is the lever that could flip it")
    print("rule: cold plus salty sinks; the deep sea returns the favor in a millennium")
    print("OK: %s sank the water" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_attribution(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def attribute(observed, natural, human):
    residual = observed - natural - human
    return residual
def main():
    r = attribute(1.2, 0.0, 1.2)
    assert abs(r) < 0.3, r
    print("observed +1.2 C = natural ~0.0 + human ~1.2 (residual %+.2f)" % r)
    print("fingerprint: troposphere warms while the stratosphere cools - greenhouse only")
    print("natural-only models stay flat after 1970; human forcings track the rise")
    print("isotopes: falling C-13/C-14 = fossil carbon")
    print("rule: three witnesses - budget, fingerprints, models - one verdict")
    print("OK: %s closed the case" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tipping_points(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def run(F_series, thresh_up=2.0, thresh_down=1.2):
    state = "cold"
    for F in F_series:
        if state == "cold" and F > thresh_up:
            state = "warm"
        elif state == "warm" and F < thresh_down:
            state = "cold"
    return state
def main():
    up = run([0.5, 1.0, 1.5, 2.1, 2.5])
    down = run([0.5, 1.0, 1.5, 2.1, 2.5, 1.8, 1.5])
    assert up == "warm" and down == "warm", (up, down)
    print("forcing ramps 0.5 -> 2.5: system tips warm at F=2.0")
    print("forcing falls back to 1.5: system STAYS warm - hysteresis")
    print("candidates: West Antarctica, AMOC, Amazon, permafrost, Arctic sea ice")
    print("early warning: critical slowing down - rising variance before the jump")
    print("rule: past the fold, the old state is gone - reversal does not reverse")
    print("OK: %s found the edge" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_sea_level(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
BUDGET = {"thermal expansion": 1.3, "glaciers": 0.7,
          "Greenland": 0.8, "Antarctica": 0.5}   # mm/yr
def total(budget):
    return sum(budget.values())
def main():
    t = total(BUDGET)
    assert abs(t - 3.3) < 0.05, t
    for src, rate in BUDGET.items():
        print("%-18s %4.1f mm/yr" % (src, rate))
    print("total: %.1f mm/yr - double the 20th-century rate" % t)
    print("~2 m committed per degree, over centuries - the least reversible change")
    print("rule: expansion plus melt, measured by tide gauges and satellites since 1993")
    print("OK: %s read the tide gauge" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_geoengineering(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def srm_cooling_c(mt_so2):
    return -0.025 * mt_so2     # Pinatubo-calibrated: 20 Mt -> -0.5 C
def cdr_ppm_per_yr(gtc_per_yr):
    return gtc_per_yr / 2.13
def main():
    cool = srm_cooling_c(20.0)
    assert abs(cool - (-0.5)) < 1e-9
    ppm = cdr_ppm_per_yr(10.0)
    assert abs(ppm - 4.69) < 0.02, ppm
    print("20 Mt SO2/yr in the stratosphere -> %.1f C cooling (Pinatubo scale)" % cool)
    print("10 GtC/yr removed -> -%.1f ppm/yr off the atmosphere" % ppm)
    print("SRM: fast, treats the symptom; side effects - rainfall shifts, ozone, termination shock")
    print("CDR: slow, treats the cause; ocean acidification continues under SRM alone")
    print("rule: the ledger always balances - no intervention replaces cutting emissions")
    print("OK: %s priced the thermostat" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_frontiers(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
FRONTIERS = {
    "cloud feedback": "storm-resolving models simulate clouds directly",
    "aerosol-cloud": "the next-largest forcing uncertainty",
    "deep-ocean heat": "sets the pace and the pipeline of warming",
    "ice-sheet physics": "marine ice-cliff instability may redraw sea level",
    "compound extremes": "heat+drought, rain-on-snow, biosphere feedbacks",
}
def main():
    assert len(FRONTIERS) == 5
    assert "cloud feedback" in FRONTIERS
    for topic, why in FRONTIERS.items():
        print("%-18s: %s" % (topic, why))
    print("kilometer grids let storms emerge; ML emulates the expensive physics")
    print("rule: observe, model, test - every generation scored on the same observations")
    print("OK: %s scouted the horizon" % NAME)
if __name__ == "__main__":
    main()
''')

DEMOS = {
    "climate_branches": demo_climate_branches, "weather_climate": demo_weather_climate,
    "energy_balance": demo_energy_balance, "greenhouse_effect": demo_greenhouse_effect,
    "albedo": demo_albedo, "seasons": demo_seasons,
    "atmosphere_layers": demo_atmosphere_layers, "water_cycle": demo_water_cycle,
    "pressure_wind": demo_pressure_wind, "coriolis": demo_coriolis,
    "circulation_cells": demo_circulation_cells, "jet_streams": demo_jet_streams,
    "ocean_currents": demo_ocean_currents, "koppen": demo_koppen,
    "monsoon": demo_monsoon, "enso": demo_enso, "nao": demo_nao,
    "forcings": demo_forcings, "feedbacks": demo_feedbacks,
    "climate_sensitivity": demo_climate_sensitivity, "carbon_cycle": demo_carbon_cycle,
    "ozone": demo_ozone, "uhi": demo_uhi, "tree_rings": demo_tree_rings,
    "ice_cores": demo_ice_cores, "gcm": demo_gcm, "ice_ages": demo_ice_ages,
    "milankovitch": demo_milankovitch, "thermohaline": demo_thermohaline,
    "attribution": demo_attribution, "tipping_points": demo_tipping_points,
    "sea_level": demo_sea_level, "geoengineering": demo_geoengineering,
    "frontiers": demo_frontiers,
}

# ---------------------------------------------------------------- records

def build_records(slug, source):
    cfg = DBCFG[slug]
    sig = source == "signature"
    # Teaching-ladder order: stable sort by ladder_rank (entries are already
    # in ladder order in entries_climatology.py).
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
    for slug in ("climatology", "climatology-signature"):
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
