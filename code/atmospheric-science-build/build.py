#!/usr/bin/env python3
"""Build the Atmospheric Science field databases for JAH Databases (field #13, taxonomy order).

Verified 2026-10-17: NO database covers atmospheric science as a discipline.
- 'weather-climate' (10,000 records): deterministic station-observation
  catalog (temperature, humidity, precipitation, wind) - raw observations,
  no science.
- 'weather' (38 records): short stubs ('Clouds (overview)', 'Weather Radar
  (history)') - no atmospheric science content.
- 'climate' (72 records): 'Essential knowledge: climate' stubs.
- 'climatology' (34 records, field #12): climate-system science (energy
  balance, the greenhouse effect, circulation, Koeppen, ENSO,
  forcings/feedbacks, paleoclimate). Genuine overlap is limited to
  atmospheric layers and the greenhouse effect at the climate level; none of
  the discipline machinery: thermodynamics, parcel theory, lapse rates,
  stability, cloud microphysics, precipitation processes, boundary-layer
  physics, atmospheric chemistry, air quality, optics, lightning,
  remote sensing, numerical weather prediction.
- 'weather-control' (150 records): weather-modification material, not science.

So this build creates two NEW databases:

  atmospheric-science            — The Atmospheric Science Database
                                   (public-harvest: real, fact-checked
                                   atmospheric science)
  atmospheric-science-signature  — The Atmospheric Science Signature Database
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
from entries_atmospheric_science import ENTRIES, SIG_TAIL

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature interpretation of atmospheric "
                "science: clearly labeled Signature-made, never presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked atmospheric science: what atmospheric "
                "science is; the composition of air; the scale of the sky; hydrostatic balance; "
                "the gas law; potential temperature; humidity; the boundary layer; the dry and "
                "moist adiabatic lapse rates; static stability; the lifting condensation level; "
                "cloud droplet growth; cloud types; warm rain; the Bergeron process; the "
                "thunderstorm life cycle; air masses and fronts; mid-latitude cyclones; "
                "scattering; atmospheric optics; CAPE and CIN; lightning; atmospheric chemistry; "
                "smog; aerosols; air quality; radiative transfer; the polar vortex; gravity "
                "waves; air-sea exchange; Doppler radar; weather satellites; numerical weather "
                "prediction; dispersion modeling; tropical cyclones, organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations (what atmospheric science "
              "is, composition, the scale of the sky, hydrostatic balance, the gas law, potential "
              "temperature, humidity, the boundary layer) -> Compounded (dry and moist adiabats, "
              "stability, the LCL, droplet growth, cloud types, warm rain, the Bergeron process, "
              "thunderstorms, fronts, cyclones, scattering, optics) -> Advanced (CAPE/CIN, "
              "lightning, atmospheric chemistry, smog, aerosols, air quality, radiative transfer, "
              "the polar vortex, gravity waves, air-sea exchange, radar, satellites, NWP, "
              "dispersion, tropical cyclones).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search lapse rate, CAPE, Bergeron, Kohler, AQI, polar vortex, NWP...",
        "chat_ph": "Ask about atmospheric science...",
        "archive_blurb": ("Seeded %s atmospheric science records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled structural atmospheric science studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about atmospheric science - from lapse rates and cloud physics to CAPE, lightning, and numerical weather prediction." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "atmospheric-science-study", "gen_demo_kind": "atmospheric-science-demo",
        "source": source,
    }

CIT_PUB = "Atmospheric science (peer-reviewed literature and standard textbooks)."
CIT_SIG = CIT_PUB + " " + SIG_TAIL

DBCFG = {}
DBCFG["atmospheric-science"] = _cfg(
    "atmospheric-science", "The Atmospheric Science Database",
    "Real, fact-checked atmospheric science: composition, hydrostatic balance, the gas law, "
    "potential temperature, humidity, adiabatic lapse rates, stability, cloud physics, "
    "precipitation processes, thunderstorms, fronts, cyclones, scattering, optics, CAPE, "
    "lightning, atmospheric chemistry, smog, aerosols, air quality, radiative transfer, "
    "the polar vortex, gravity waves, air-sea exchange, radar, satellites, NWP, dispersion, "
    "and tropical cyclones.",
    "atmospheric science record", "JAH-AT-", "JAH Atmospheric Science Archivist",
    "atmospheric science archivist - composition, hydrostatic balance, the gas law, "
    "potential temperature, humidity, the boundary layer, dry and moist adiabats, static "
    "stability, the LCL, cloud droplet growth, cloud types, warm rain, the Bergeron process, "
    "thunderstorms, air masses and fronts, mid-latitude cyclones, scattering, optics, "
    "CAPE/CIN, lightning, atmospheric chemistry, smog, aerosols, air quality, radiative "
    "transfer, the polar vortex, gravity waves, air-sea exchange, Doppler radar, weather "
    "satellites, numerical weather prediction, dispersion modeling, tropical cyclones; "
    "teaching progressively along the ladder from foundations through compounded to advanced; "
    "answers from many angles - definition, example, analogy, application, history, "
    "math, how-to - using only the system's own archive data",
    CIT_PUB, "public")
DBCFG["atmospheric-science-signature"] = _cfg(
    "atmospheric-science-signature", "The Atmospheric Science Signature Database",
    "His original Signature interpretation of atmospheric science: the full ladder from lapse "
    "rates and cloud physics to CAPE, lightning, and numerical weather prediction, reframed "
    "as Signature science. Clearly labeled Signature-made, never presented as authentic "
    "public record.",
    "atmospheric science record", "JAH-ATS-", "JAH Atmospheric Science Archivist (Signature)",
    "atmospheric science archivist - Signature editions: his original Signature interpretation "
    "of atmospheric science, clearly labeled Signature-made and never presented as authentic "
    "public record; teaches progressively along the ladder from foundations through "
    "compounded to advanced; answers from many angles - definition, example, analogy, "
    "application, history, math, how-to - using only the system's own archive data",
    CIT_SIG, "signature")

base.DBCFG = DBCFG

# ---------------------------------------------------------------- demos
# Every demo is real, runnable, stdlib-only Python performing the actual
# atmospheric-science calculation for its record. All are machine-executed by main().

_PREAMBLE = """import math
import re
"""

def _wrap(name, rid, group, body):
    return (base._hdr(name, rid, group) + _PREAMBLE + body.replace("NAME", json.dumps(name)))

def demo_atm_branches(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
BRANCHES = {
    "atmospheric dynamics": "the rotating-fluid equations behind the winds",
    "atmospheric physics": "radiation, thermodynamics, and cloud processes",
    "atmospheric chemistry": "trace gases, aerosols, and their reactions",
}
def main():
    assert len(BRANCHES) == 3
    assert BRANCHES["atmospheric dynamics"].startswith("the rotating-fluid")
    for branch, focus in BRANCHES.items():
        print("%-22s -> %s" % (branch, focus))
    print("plus observation (stations, balloons, radar, satellites) and numerical modeling")
    print("rule: mass, momentum, and energy conserved - applied to every parcel of air")
    print("OK: %s mapped the branches" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_composition(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
FRAC = {"N2": 0.7808, "O2": 0.2095, "Ar": 0.0093, "CO2": 0.000420}
P0 = 101325.0
def partials(frac, p0):
    return {g: f * p0 for g, f in frac.items()}
def mean_mw():
    return 0.7808 * 28.0134 + 0.2095 * 31.9988 + 0.0093 * 39.948 + 0.00042 * 44.01
def main():
    pp = partials(FRAC, P0)
    assert abs(sum(FRAC.values()) - 1.0) < 0.001, sum(FRAC.values())
    assert abs(pp["O2"] - 21227.6) < 1.0, pp["O2"]
    mw = mean_mw()
    assert abs(mw - 28.97) < 0.02, mw
    for g, p in pp.items():
        print("%-4s partial pressure %8.1f Pa" % (g, p))
    print("mean molecular weight of dry air: %.2f g/mol" % mw)
    print("rule: Dalton's law - each gas contributes its fraction of the total pressure")
    print("OK: %s mixed the air" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_scale_height(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
R, G = 287.05, 9.81
def scale_height(T_K):
    return R * T_K / G
def pressure(z_m, T_K, p0=101325.0):
    return p0 * math.exp(-z_m / scale_height(T_K))
def main():
    H = scale_height(288.15)
    assert abs(H - 8431.5) < 2.0, H
    p12 = pressure(12000.0, 288.15)
    assert 19000.0 < p12 < 24500.0, p12
    p_half = pressure(5500.0, 288.15)
    assert abs(p_half / 101325.0 - 0.52) < 0.03, p_half
    print("scale height at 288 K: %.0f m" % H)
    print("pressure at 12 km: %.0f Pa (about a quarter of sea level)" % p12)
    print("pressure at 5.5 km: %.3f of sea level - half the mass below" % (p_half / 101325.0))
    print("rule: p = p0 exp(-z/H) - every scale height thins the air to 37%%")
    print("OK: %s measured the sky" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hydrostatic(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
R, G = 287.05, 9.81
def thickness_m(p1_hpa, p2_hpa, Tmean_K):
    return (R * Tmean_K / G) * math.log(p1_hpa / p2_hpa)
def main():
    z = thickness_m(1000.0, 500.0, 273.15)
    assert abs(z - 5540.0) < 15.0, z
    warm = thickness_m(1000.0, 500.0, 283.15)
    assert abs((warm - z) - 202.8) < 5.0, warm - z
    print("1000-500 hPa thickness at 0 C mean: %.0f m (%.1f dam)" % (z, z / 10.0))
    print("+10 C of layer warming thickens it by %.0f m" % (warm - z))
    print("the 540-dam line separates rain from snow in winter storms")
    print("rule: warm layers are thick, cold layers thin - thickness charts are temperature maps")
    print("OK: %s weighed the column" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_gas_law(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
R = 287.05
def density(p_pa, T_K):
    return p_pa / (R * T_K)
def virtual_temp(T_K, q):
    return T_K * (1.0 + 0.61 * q)
def main():
    rho = density(101325.0, 288.15)
    assert abs(rho - 1.225) < 0.002, rho
    tv = virtual_temp(300.0, 0.020)
    assert abs(tv - 303.66) < 0.02, tv
    rho_moist = density(101325.0, tv)
    assert rho_moist < rho * 1.05 and rho_moist < 1.225, rho_moist
    print("sea-level density: %.3f kg/m3" % rho)
    print("30 C air with 20 g/kg vapor: Tv = %.2f K, density %.3f kg/m3" % (tv, rho_moist))
    print("humid air is LESS dense than dry air at the same temperature and pressure")
    print("rule: rho = p/RT, and vapor lightens the mix via virtual temperature")
    print("OK: %s applied the gas law" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_potential_temp(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
KAPPA = 0.286
def theta(T_K, p_hpa, p0=1000.0):
    return T_K * (p0 / p_hpa) ** KAPPA
def main():
    th = theta(250.0, 500.0)
    assert abs(th - 304.9) < 0.6, th
    th2 = theta(288.15, 1000.0)
    assert abs(th2 - 288.15) < 1e-9, th2
    print("parcel at 500 hPa, 250 K -> theta = %.1f K" % th)
    print("squeeze it adiabatically to 1000 hPa and it warms to %.1f K" % th)
    print("lift it dry-adiabatically and theta never changes - it is the parcel's label")
    print("rule: theta increasing with height = stable; decreasing = unstable")
    print("OK: %s labeled the parcel" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_humidity(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def es_hpa(T_C):
    return 6.112 * math.exp(17.67 * T_C / (T_C + 243.5))
def dewpoint_C(e_hpa):
    ln = math.log(e_hpa / 6.112)
    return 243.5 * ln / (17.67 - ln)
def main():
    e30 = es_hpa(30.0)
    e20 = es_hpa(20.0)
    assert abs(e30 - 42.43) < 0.1, e30
    assert abs(e30 / e20 - 1.81) < 0.02, e30 / e20   # ~7%/C compounded over 10 C
    rh = e20 / e30 * 100.0
    assert abs(rh - 55.2) < 0.5, rh
    td = dewpoint_C(e20)
    assert abs(td - 20.0) < 0.05, td
    print("saturation at 30 C: %.2f hPa; at 20 C: %.2f hPa (ratio %.2f)" % (e30, e20, e30 / e20))
    print("air at 30 C holding 20-C saturation vapor -> RH %.1f %%, dew point %.1f C" % (rh, td))
    print("rule: Clausius-Clapeyron - capacity grows ~7%% per degree, exponentially")
    print("OK: %s measured the moisture" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_boundary_layer(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
K = 0.4
def log_wind(z_m, ustar, z0_m):
    return (ustar / K) * math.log(z_m / z0_m)
def ekman_turn(z_m, h_m=1000.0):
    # fraction of the ~45-degree textbook surface-to-top turning reached
    return 45.0 * (1.0 - math.exp(-z_m / (h_m / 3.0)))
def main():
    u10 = log_wind(10.0, 0.3, 0.03)
    u2 = log_wind(2.0, 0.3, 0.03)
    assert abs(u10 - 4.35) < 0.1, u10
    assert u10 > u2 > 0
    print("u* = 0.3 m/s, grass z0 = 3 cm: wind at 2 m = %.2f m/s, at 10 m = %.2f m/s" % (u2, u10))
    for z in (10.0, 100.0, 500.0, 1000.0):
        print("  height %4.0f m: turned %.0f deg toward low pressure" % (z, ekman_turn(z)))
    print("rule: friction slows the surface wind and turns it; the spiral straightens with height")
    print("OK: %s profiled the boundary layer" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_dry_adiabat(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
GAMMA_D = 9.81 / 1004.0 * 1000.0   # K per km
def parcel_T(T0_C, z_km):
    return T0_C - GAMMA_D * z_km
def main():
    assert abs(GAMMA_D - 9.77) < 0.05, GAMMA_D
    T = parcel_T(20.0, 2.0)
    assert abs(T - 0.46) < 0.1, T
    Tback = parcel_T(T, -2.0)
    assert abs(Tback - 20.0) < 1e-9, Tback
    print("dry adiabatic lapse rate: %.2f C/km" % GAMMA_D)
    print("20 C parcel lifted 2 km -> %.1f C; sunk back -> %.1f C (reversible)" % (T, Tback))
    print("foehn winds are this in reverse: descent warms and desiccates")
    print("rule: Gamma-d = g/cp - expansion work costs temperature, exactly")
    print("OK: %s lifted the parcel" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_moist_adiabat(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def gamma_m_approx(T_C):
    # shallow in warm air (vapor-rich), steep in cold air - textbook curve fit
    return 9.8 - 5.4 / (1.0 + math.exp(-(T_C - 5.0) / 8.0))
def main():
    warm = gamma_m_approx(25.0)
    cold = gamma_m_approx(-20.0)
    assert 4.0 < warm < 6.0, warm
    assert 8.0 < cold < 9.8, cold
    assert warm < cold
    print("moist adiabatic lapse rate at 25 C: %.1f C/km" % warm)
    print("moist adiabatic lapse rate at -20 C: %.1f C/km" % cold)
    print("tropical ascent stays buoyant: condensation reheats the parcel as it climbs")
    print("rule: latent heat pays back part of the expansion cooling - more payback in warm air")
    print("OK: %s condensed the climb" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_stability(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
GAMMA_D, GAMMA_M = 9.8, 6.0
def buoyancy(Tp_C, Te_C):
    return 9.81 * (Tp_C - Te_C) / (Te_C + 273.15)
def regime(env_lapse):
    if env_lapse < GAMMA_M:
        return "absolutely stable"
    if env_lapse < GAMMA_D:
        return "conditionally unstable"
    return "absolutely unstable"
def main():
    assert regime(4.0) == "absolutely stable"
    assert regime(7.5) == "conditionally unstable"
    assert regime(11.0) == "absolutely unstable"
    b = buoyancy(12.0, 10.0)
    assert abs(b - 0.070) < 0.005, b
    print("lapse 4.0 C/km -> %s; 7.5 -> %s; 11.0 -> %s" %
          (regime(4.0), regime(7.5), regime(11.0)))
    print("parcel 2 C warmer than environment -> buoyancy %+.3f m/s^2" % b)
    print("conditional instability is the loaded spring behind most thunderstorms")
    print("rule: compare the environment to the adiabats - the parcel does the rest")
    print("OK: %s judged the layer" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_lcl(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def lcl_m(T_C, Td_C):
    return 125.0 * (T_C - Td_C)
def lcl_exact_m(T_C, Td_C):
    return 1000.0 * (T_C - Td_C) / (9.8 - 1.8)
def main():
    z = lcl_m(25.0, 15.0)
    assert abs(z - 1250.0) < 1e-9, z
    ze = lcl_exact_m(25.0, 15.0)
    assert abs(ze - z) < 1.0, ze
    print("T=25 C, Td=15 C -> cloud base near %.0f m" % z)
    print("the flat bottoms of fair-weather cumulus all sit at this one height")
    print("rule: parcel cools 9.8 C/km, dew point falls 1.8 C/km - where they meet, cloud")
    print("OK: %s found the cloud base" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_kohler(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def kohler_crit(r_nm, kappa=0.6):
    # critical supersaturation (%) for a dry nucleus of radius r (nm)
    A = 2.1e-9 / (r_nm * 1e-9) / 1000.0   # Kelvin term scaled
    # textbook approximation: S_c(%) ~= 0.35 * kappa^-0.5 * (r/100nm)^-1.5
    return 0.35 * (kappa ** -0.5) * ((r_nm / 100.0) ** -1.5)
def main():
    s_big = kohler_crit(200.0)
    s_small = kohler_crit(50.0)
    assert s_big < 0.3, s_big
    assert s_small > s_big
    assert abs(kohler_crit(100.0, 0.6) - 0.45) < 0.05
    print("200 nm salt nucleus: critical supersaturation %.2f %%" % s_big)
    print("50 nm nucleus: %.2f %% - smaller nuclei need stronger supersaturation" % s_small)
    print("updrafts easily supply 0.2-1%% - activation is routine, nucleation from nothing is not")
    print("rule: Kelvin fights growth, solute helps it - the Kohler peak decides who becomes cloud")
    print("OK: %s activated the droplet" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_cloud_types(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
GENERA = {
    "high": ["cirrus", "cirrostratus", "cirrocumulus"],
    "middle": ["altocumulus", "altostratus"],
    "low": ["stratus", "stratocumulus", "cumulus", "nimbostratus", "cumulonimbus"],
}
def etage(base_m):
    if base_m >= 6000:
        return "high (ice crystals)"
    if base_m >= 2000:
        return "middle (mixed phase)"
    return "low (liquid drops)"
def main():
    assert sum(len(v) for v in GENERA.values()) == 10
    assert etage(8000) == "high (ice crystals)" and etage(1000) == "low (liquid drops)"
    for fam, genera in GENERA.items():
        print("%-6s: %s" % (fam, ", ".join(genera)))
    print("layer clouds = stable air; heaped clouds = convection")
    print("rule: height sets the phase, texture reveals the mechanism")
    print("OK: %s named the clouds" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_warm_rain(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def fall_speed_ms(r_um):
    # Stokes regime approximation, m/s
    return 1.2e-2 * (r_um / 10.0) ** 2 if r_um < 70 else 0.27 * (r_um / 100.0)
def main():
    v10 = fall_speed_ms(10.0)
    v100 = fall_speed_ms(100.0)
    assert abs(v10 - 0.012) < 0.002, v10
    assert abs(v100 - 0.27) < 0.05, v100
    assert v100 / v10 > 15.0
    print("10-micron droplet falls %.1f cm/s; 100-micron drop falls %.0f cm/s" % (v10 * 100, v100 * 100))
    print("the 100-micron collector sweeps a cylinder of cloud ~%.0fx faster" % (v100 / v10))
    print("mergers accelerate: bigger, faster, hungrier - a millimeter drop in ~30 minutes")
    print("rule: differential fall speed is the engine; a broad spectrum is the fuel")
    print("OK: %s grew the raindrop" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_bergeron(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def es_water_hpa(T_C):
    return 6.112 * math.exp(17.67 * T_C / (T_C + 243.5))
def es_ice_hpa(T_C):
    return 6.112 * math.exp(22.46 * T_C / (T_C + 272.62))
def main():
    T = -15.0
    ew, ei = es_water_hpa(T), es_ice_hpa(T)
    assert ew > ei > 0
    gap = (ew - ei) / ew * 100.0
    assert 12.0 < gap < 20.0, gap
    print("at -15 C: saturation over water %.3f hPa, over ice %.3f hPa" % (ew, ei))
    print("air saturated for droplets is %.1f%% supersaturated for ice - crystals feast" % gap)
    print("one ice nucleus per liter can seed a shower; droplets evaporate to feed the crystal")
    print("rule: ice wins the vapor competition wherever both phases coexist")
    print("OK: %s seeded the snow" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_thunderstorm(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def w_max(cape):
    return math.sqrt(2.0 * cape)
def main():
    for cape in (500.0, 2000.0, 4000.0):
        w = w_max(cape)
        print("CAPE %4.0f J/kg -> theoretical updraft %.0f m/s (real: ~half)" % (cape, w))
    assert abs(w_max(2000.0) - 63.2) < 0.5
    stages = ["cumulus (pure updraft)", "mature (updraft + downdraft)",
              "dissipating (downdraft chokes the inflow)"]
    assert len(stages) == 3
    print("single-cell life: " + " -> ".join(stages))
    print("shear separates updraft from downdraft: the storm stops killing itself")
    print("rule: CAPE is the fuel, shear is the organization, the cold pool is the trigger")
    print("OK: %s ran the storm" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_fronts(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def margules_slope(dT_K, T_K, du_ms, f=1e-4):
    # Margules formula: frontal slope tan(alpha) = f*T*du / (g*dT)
    return f * T_K * abs(du_ms) / (9.81 * dT_K)
def main():
    cold = margules_slope(8.0, 280.0, 20.0)
    warm = margules_slope(8.0, 285.0, 12.0)
    assert 0.005 < cold < 0.010, cold
    assert 0.003 < warm < 0.006, warm
    assert cold > warm   # cold front steeper
    print("cold front slope ~1:%.0f (steep, violent lift)" % (1.0 / cold))
    print("warm front slope ~1:%.0f (shallow, broad rain shield)" % (1.0 / warm))
    print("air masses: mT warm-moist, cP cold-dry, mP cool-moist, cT hot-dry")
    print("rule: the steeper the frontal slope, the more violent the lift")
    print("OK: %s drew the front" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_cyclone(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
BELTS = {
    "warm conveyor belt": "rises 5-8 km along the warm front - the rain shield",
    "cold conveyor belt": "hugs the surface north of the warm front - freezing rain risk",
    "dry intrusion": "descends behind the cold front - the clearing slot",
}
def main():
    assert len(BELTS) == 3
    for belt, job in BELTS.items():
        print("%-19s: %s" % (belt, job))
    print("born on the polar front, fed by the equator-to-pole contrast, dead by occlusion")
    print("travels with the jet at 10-20 m/s; spans 1000-2000 km")
    print("rule: baroclinic instability converts the temperature gradient into wind")
    print("OK: %s tracked the cyclone" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_scattering(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def rayleigh_ratio(lam1_nm, lam2_nm):
    return (lam2_nm / lam1_nm) ** 4
def main():
    r = rayleigh_ratio(450.0, 650.0)
    assert abs(r - 4.35) < 0.05, r
    tau_blue = 0.14
    transmitted = math.exp(-tau_blue * 10.0)   # 10x path at sunset
    assert transmitted < 0.30, transmitted
    print("blue (450 nm) scatters %.2fx more strongly than red (650 nm)" % r)
    print("sunset: 10x the air path -> only %.0f%% of blue survives the beam" % (100 * transmitted))
    print("what is scattered away from the beam becomes the blue sky in every other direction")
    print("rule: lambda^-4 - molecules are picky, and blue pays the price")
    print("OK: %s scattered the sunlight" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_optics(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def rainbow_angle(n):
    # Descartes: minimum deviation for one internal reflection; the bow sits
    # at 4r - 2i from the antisolar point, with sin i = n sin r at the minimum
    x = math.sqrt((4.0 - n * n) / 3.0)
    dev = 4.0 * math.asin(x / n) - 2.0 * math.asin(x)
    return math.degrees(dev)
def halo_angle():
    # 60-degree ice prism, minimum deviation
    n = 1.31
    return math.degrees(2.0 * math.asin(n * math.sin(math.radians(30.0))) - math.radians(60.0))
def main():
    rb = rainbow_angle(1.331)
    assert abs(rb - 42.0) < 0.6, rb
    halo = halo_angle()
    assert abs(halo - 21.8) < 0.5, halo
    print("primary rainbow: %.1f deg from the antisolar point (red outside)" % rb)
    print("ice halo: %.1f deg - the 22-degree halo of cirrus" % halo)
    print("secondary bow: two reflections, 51 deg, colors reversed")
    print("rule: minimum deviation concentrates the light - geometry made visible")
    print("OK: %s bent the light" % NAME)
if __name__ == "__main__":
    main()
''')
def demo_cape_cin(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def integrate_buoyancy(levels):
    # levels: list of (dz_m, Tp_C, Te_C); returns (cape, cin)
    cape = cin = 0.0
    for dz, tp, te in levels:
        b = 9.81 * (tp - te) / (te + 273.15)
        if b > 0:
            cape += b * dz
        else:
            cin += b * dz
    return cape, cin
def main():
    sounding = [(500.0, 18.0, 20.0),   # capped near surface
                (500.0, 17.0, 18.0),
                (1500.0, 16.0, 11.0),  # free convection
                (1500.0, 6.0, 0.0),
                (1500.0, -6.0, -13.0)]
    cape, cin = integrate_buoyancy(sounding)
    assert cape > 800.0 and cin < 0.0, (cape, cin)
    print("CAPE %.0f J/kg, CIN %.0f J/kg" % (cape, cin))
    print("the cap holds until a front or outflow boundary supplies the lift")
    print("w_max = sqrt(2 CAPE) = %.0f m/s theoretical" % math.sqrt(2.0 * cape))
    print("rule: positive area is fuel, negative area is the lid - the sounding tells both")
    print("OK: %s read the sounding" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_lightning(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def leader_steps(height_m, step_m=50.0):
    return int(height_m / step_m)
def return_stroke_current_c(kA=30.0, dur_us=100.0):
    return kA * 1000.0 * dur_us * 1e-6   # coulombs
def main():
    steps = leader_steps(5000.0)
    assert steps == 100, steps
    q = return_stroke_current_c()
    assert abs(q - 3.0) < 0.01, q
    print("5 km leader: %d fifty-meter steps to ground" % steps)
    print("30 kA for 100 us moves %.1f coulombs at 30,000 K" % q)
    print("~100 ground strikes per second worldwide; intracloud outnumber them ~3:1")
    print("the ionosphere floats at +250 kV on thunderstorm current; fair weather leaks it back")
    print("rule: collisions separate the charge, the field breaks the air, the circuit closes globally")
    print("OK: %s discharged the cloud" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_chemistry(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def chapman_o3_o_ratio(j_o3=5e-4, k_form=6e-34, M=1e18, O2=2e17):
    # fast O <-> O3 interconversion: [O3]/[O] = k[O2][M] / j_O3
    return k_form * O2 * M / j_o3
def lifetime_yrs(burden_Tg, sink_Tg_yr):
    return burden_Tg / sink_Tg_yr
def main():
    ratio = chapman_o3_o_ratio()
    assert ratio > 1e3, ratio
    ch4 = lifetime_yrs(5400.0, 600.0)
    assert 8.0 < ch4 < 10.0, ch4
    print("Chapman steady state: O3 outnumbers free O by >1000:1 in the layer")
    print("methane burden 5400 Tg / 600 Tg-yr OH sink -> %.1f yr lifetime" % ch4)
    print("one Cl atom destroys ~100,000 O3: the catalyst regenerates every loop")
    print("rule: photolysis starts it, kinetics paces it, catalysts multiply it")
    print("OK: %s balanced the reactions" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_smog(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def leighton_o3_ppb(j_no2=8e-3, no2_ppb=20.0, k=1.8e-14, no_ppb=5.0):
    # [O3] = j[NO2] / (k[NO]) in molecules/cm3 -> ppb
    o3_molec = j_no2 * (no2_ppb * 2.5e10) / (k * no_ppb * 2.5e10)
    return o3_molec / 2.5e10
def main():
    o3 = leighton_o3_ppb()
    assert 60.0 < o3 < 85.0, o3
    print("null-cycle (Leighton) ozone: %.0f ppb for 20 ppb NO2 / 5 ppb NO" % o3)
    print("afternoon smog reads far above this - peroxy radicals from VOCs break the cycle")
    print("NOx-limited countryside vs VOC-limited city core: the control strategy must match")
    print("rule: sunlight + NOx + VOCs = ozone; stagnation + inversion = episode")
    print("OK: %s diagnosed the smog" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_aerosols(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def angstrom_od(od550, alpha, lam_nm):
    return od550 * (lam_nm / 550.0) ** (-alpha)
def main():
    dust = angstrom_od(0.5, 0.3, 870.0)    # coarse dust: weak wavelength dependence
    smoke = angstrom_od(0.5, 1.8, 870.0)   # fine smoke: strong dependence
    assert dust > smoke > 0
    assert abs(dust - 0.44) < 0.03 and abs(smoke - 0.22) < 0.03, (dust, smoke)
    print("AOD 0.50 at 550 nm -> at 870 nm: dust %.2f, smoke %.2f" % (dust, smoke))
    print("the Angstrom exponent fingerprints particle size: ~0.3 coarse, ~1.8 fine")
    print("Pinatubo 1991 spiked global AOD and cooled the planet ~0.5 C for two years")
    print("rule: size sets the color dependence; number sets the dimming")
    print("OK: %s sized the particles" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_aqi(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
PM25_BP = [(0.0, 12.0, 0, 50), (12.1, 35.4, 51, 100), (35.5, 55.4, 101, 150),
           (55.5, 150.4, 151, 200), (150.5, 250.4, 201, 300), (250.5, 500.0, 301, 500)]
def sub_index(conc, bps):
    for c_lo, c_hi, i_lo, i_hi in bps:
        if c_lo <= conc <= c_hi:
            return (i_hi - i_lo) / (c_hi - c_lo) * (conc - c_lo) + i_lo
    return 500.0
def main():
    assert abs(sub_index(12.0, PM25_BP) - 50.0) < 0.01
    assert abs(sub_index(35.4, PM25_BP) - 100.0) < 0.01
    assert 100.0 < sub_index(40.0, PM25_BP) < 150.0
    print("PM2.5 12.0 ug/m3 -> AQI %.0f (good/moderate boundary)" % sub_index(12.0, PM25_BP))
    print("PM2.5 35.4 ug/m3 -> AQI %.0f" % sub_index(35.4, PM25_BP))
    print("PM2.5 40 ug/m3 -> AQI %.0f (unhealthy for sensitive groups)" % sub_index(40.0, PM25_BP))
    print("the AQI is the worst sub-index: the worst pollutant rules")
    print("rule: piecewise linear through the breakpoints - know the table, read the air")
    print("OK: %s scored the air" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_radiative(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def transmittance(tau):
    return math.exp(-tau)
def co2_forcing(c_ppm, c0=278.0):
    return 5.35 * math.log(c_ppm / c0)
def main():
    assert abs(transmittance(0.0) - 1.0) < 1e-12
    assert abs(transmittance(3.0) - 0.0498) < 1e-4
    d2x = co2_forcing(556.0)
    assert abs(d2x - 3.71) < 0.02, d2x
    print("optical depth 3 -> transmittance %.3f: the band core is black" % transmittance(3.0))
    print("doubled CO2 (278->556 ppm): %+.2f W/m2 - the wings do the new work" % d2x)
    print("band saturation is why the forcing is logarithmic, not linear")
    print("rule: Beer's law per line, summed over millions of HITRAN lines")
    print("OK: %s traced the photons" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_polar_vortex(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def thermal_wind_shear(dTdy, T=220.0, f=1.4e-4):
    return -(9.81 / (f * T)) * dTdy
def main():
    shear = thermal_wind_shear(-1.0e-5)   # 10 K over 1000 km, pole colder
    assert shear > 0.002, shear
    jet = shear * 30000.0                  # over 30 km of stratosphere
    assert 60.0 < jet < 130.0, jet
    print("polar-night gradient 10 K/1000 km -> shear %.2e /s" % shear)
    print("over 30 km of stratosphere: vortex jet ~%.0f m/s" % jet)
    print("major warming = zonal wind at 60 N, 10 hPa reverses westerly -> easterly")
    print("weeks later: negative Arctic Oscillation, cold-air outbreaks loaded")
    print("rule: the temperature gradient builds the wheel; planetary waves break it")
    print("OK: %s spun the vortex" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_gravity_waves(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def brunt_vaisala(dtheta_dz, theta=300.0):
    return math.sqrt(9.81 / theta * dtheta_dz)
def intrinsic_freq(N, angle_deg):
    return N * math.cos(math.radians(angle_deg))
def main():
    N = brunt_vaisala(0.003)
    assert abs(N - 0.0099) < 0.0005, N
    period_min = 2.0 * math.pi / N / 60.0
    assert 9.0 < period_min < 12.0, period_min
    w = intrinsic_freq(N, 60.0)
    assert abs(w - N / 2.0) < 1e-9
    print("d(theta)/dz = 3 K/km -> N = %.4f /s, buoyancy period %.1f min" % (N, period_min))
    print("no gravity wave oscillates faster than N - the atmosphere's speed limit")
    print("mountain waves break at critical levels, dumping momentum into the stratosphere")
    print("rule: omega = N cos(theta) - buoyancy sets the tempo, geometry sets the tune")
    print("OK: %s rippled the sky" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_air_sea(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
RHO, CP, L = 1.225, 1004.0, 2.5e6
def bulk_fluxes(U, Ts_C, Ta_C, qs, qa, Cd=1.2e-3, Ch=1.1e-3, Ce=1.2e-3):
    tau = RHO * Cd * U * U
    H = RHO * CP * Ch * U * (Ts_C - Ta_C)
    LE = RHO * L * Ce * U * (qs - qa)
    return tau, H, LE
def main():
    tau, H, LE = bulk_fluxes(10.0, 28.0, 26.0, 0.023, 0.018)
    assert abs(tau - 0.147) < 0.01, tau
    assert abs(LE - 183.8) < 5.0, LE
    assert LE > H * 5.0
    print("10 m/s over 28 C water: stress %.3f N/m2" % tau)
    print("sensible %.0f W/m2, latent %.0f W/m2 - evaporation dominates the tropics" % (H, LE))
    print("WISHE: stronger winds -> more evaporation -> stronger storm")
    print("rule: flux = rho C U (sea minus air) - the interface ledger")
    print("OK: %s traded across the interface" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_radar(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def dbz(Z):
    return 10.0 * math.log10(Z)
def nyquist_vel(lam_m, prf_hz):
    return lam_m * prf_hz / 4.0
def rain_rate(Z):
    return (Z / 300.0) ** (1.0 / 1.4)
def main():
    assert abs(dbz(1000.0) - 30.0) < 1e-9
    vn = nyquist_vel(0.10, 1000.0)
    assert abs(vn - 25.0) < 1e-9, vn
    R = rain_rate(10000.0)
    assert 11.0 < R < 14.0, R
    print("Z=1000 -> %.0f dBZ (moderate rain); Z=10000 -> %.1f mm/h" % (dbz(1000.0), R))
    print("10-cm radar, PRF 1000 Hz -> Nyquist velocity %.0f m/s; faster winds alias" % vn)
    print("mesocyclone = adjacent inbound/outbound couplet; debris ball = dual-pol tornado signature")
    print("rule: D^6 rules the echo, phase shift rules the wind")
    print("OK: %s scanned the storm" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_satellites(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
G, M_EARTH = 6.674e-11, 5.972e24
def geo_altitude_km():
    T = 86164.0   # sidereal day, s
    r = (G * M_EARTH * T * T / (4.0 * math.pi ** 2)) ** (1.0 / 3.0)
    return r / 1000.0 - 6371.0
def orbital_period_min(alt_km):
    r = (6371.0 + alt_km) * 1000.0
    return 2.0 * math.pi * math.sqrt(r ** 3 / (G * M_EARTH)) / 60.0
def main():
    alt = geo_altitude_km()
    assert abs(alt - 35786.0) < 10.0, alt
    p = orbital_period_min(850.0)
    assert 100.0 < p < 105.0, p
    print("geostationary altitude: %.0f km - one sidereal day per orbit" % alt)
    print("850-km polar orbiter: %.1f min per orbit, global cover twice daily" % p)
    print("IR window: cloud-top temperature = storm height; water vapor: the jet's dry slots")
    print("rule: Kepler sets the perch, channels set the sight")
    print("OK: %s parked the satellite" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nwp(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def max_dt(dx_m, c_ms=300.0):
    return dx_m / c_ms
def error_growth_days(initial, days, doubling_days=2.0):
    return initial * 2.0 ** (days / doubling_days)
def main():
    dt = max_dt(9000.0)
    assert abs(dt - 30.0) < 0.5, dt
    e = error_growth_days(1.0, 14.0)
    assert abs(e - 128.0) < 0.01, e
    print("9-km grid, 300 m/s waves -> max stable step %.0f s (CFL)" % dt)
    print("unit error doubling every 2 days -> x%.0f in 14 days: the predictability wall" % e)
    print("ensembles map the uncertainty; the mean beats any single run")
    print("rule: the grid resolves, the parameterizations approximate, chaos limits")
    print("OK: %s integrated the atmosphere" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_plume(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def sigma_yz(x_m, stability="D"):
    table = {"A": (0.22, 0.20), "D": (0.08, 0.06), "F": (0.04, 0.016)}
    a, b = table[stability]
    return a * x_m / math.sqrt(1.0 + x_m / 1000.0), b * x_m / (1.0 + x_m / 1000.0)
def centerline_conc(Q_gs, u_ms, sy, sz, H_m):
    return Q_gs / (math.pi * u_ms * sy * sz) * math.exp(-H_m ** 2 / (2.0 * sz ** 2))
def main():
    sy, sz = sigma_yz(1000.0, "D")
    c = centerline_conc(100.0, 5.0, sy, sz, 100.0)
    assert c > 0
    syF, szF = sigma_yz(1000.0, "F")
    assert szF < sz
    cF = centerline_conc(100.0, 5.0, syF, szF, 100.0)
    print("1 km downwind, class D: sigma_y=%.0f m, sigma_z=%.0f m -> centerline %.1f ug/m3" %
          (sy, sz, c * 1e6))
    print("class F (stable night): sigma_z only %.0f m -> plume stays aloft, then fumigates at dawn" % szF)
    print("rule: concentration ~ Q/(u sigma_y sigma_z) - dilution is wind times spread")
    print("OK: %s tracked the plume" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tropical_cyclone(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def potential_intensity_ms(Ts_C=28.0, To_C=-70.0, dk=13000.0, ck_cd=1.0):
    # Emanuel PI: V^2 = (Ck/Cd) * (Ts-To)/To * (k*_s - k_a)
    Ts, To = Ts_C + 273.15, To_C + 273.15
    eff = (Ts - To) / To
    return math.sqrt(ck_cd * eff * dk)
def main():
    vmax = potential_intensity_ms()
    assert 70.0 < vmax < 95.0, vmax
    cool = potential_intensity_ms(Ts_C=26.0)
    assert cool < vmax
    print("28 C ocean, -70 C outflow: potential intensity %.0f m/s" % vmax)
    print("cool the ocean to 26 C -> %.0f m/s: the 26.5 C genesis threshold is thermodynamic" % cool)
    print("WISHE: wind -> evaporation -> heat -> wind; angular momentum does the spinning up")
    print("rule: the Carnot efficiency of the ocean-atmosphere engine sets the ceiling")
    print("OK: %s powered the hurricane" % NAME)
if __name__ == "__main__":
    main()
''')

DEMOS = {
    "atm_branches": demo_atm_branches, "composition": demo_composition,
    "scale_height": demo_scale_height, "hydrostatic": demo_hydrostatic,
    "gas_law": demo_gas_law, "potential_temp": demo_potential_temp,
    "humidity": demo_humidity, "boundary_layer": demo_boundary_layer,
    "dry_adiabat": demo_dry_adiabat, "moist_adiabat": demo_moist_adiabat,
    "stability": demo_stability, "lcl": demo_lcl,
    "kohler": demo_kohler, "cloud_types": demo_cloud_types,
    "warm_rain": demo_warm_rain, "bergeron": demo_bergeron,
    "thunderstorm": demo_thunderstorm, "fronts": demo_fronts,
    "cyclone": demo_cyclone, "scattering": demo_scattering,
    "optics": demo_optics, "cape_cin": demo_cape_cin,
    "lightning": demo_lightning, "chemistry": demo_chemistry,
    "smog": demo_smog, "aerosols": demo_aerosols,
    "aqi": demo_aqi, "radiative": demo_radiative,
    "polar_vortex": demo_polar_vortex, "gravity_waves": demo_gravity_waves,
    "air_sea": demo_air_sea, "radar": demo_radar,
    "satellites": demo_satellites, "nwp": demo_nwp,
    "plume": demo_plume, "tropical_cyclone": demo_tropical_cyclone,
}

# ---------------------------------------------------------------- records

def build_records(slug, source):
    cfg = DBCFG[slug]
    sig = source == "signature"
    # Teaching-ladder order: stable sort by ladder_rank (entries are already
    # in ladder order in entries_atmospheric_science.py).
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
    for slug in ("atmospheric-science", "atmospheric-science-signature"):
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
