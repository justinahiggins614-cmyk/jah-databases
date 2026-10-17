#!/usr/bin/env python3
"""Build the Volcanology field databases for JAH Databases (field #11, taxonomy order).

Verified 2026-10-17: NO database covers volcanology as a science. The broad
'geology' database is a specimen-style catalog with no magma-system science,
no eruption styles, no VEI scale, no volcano monitoring, no volcanic-hazard
analysis, and no historic-eruption science. 'geology-public' carries only
generic volcano overviews. The 'volcanoes' database (28 topics) is
stub-grade - one-line topic briefs with content_completeness 'stub' - and
'volcano-energy' covers only geothermal energy use. So this build creates
two NEW databases:

  volcanology              — The Volcanology Database (public-harvest: real,
                             fact-checked volcanology - what volcanology is;
                             magma formation; lava; plate tectonics and
                             volcanic settings; the Ring of Fire; shield
                             volcanoes; stratovolcanoes; cinder cones;
                             craters and calderas; magma chambers and
                             plumbing; viscosity and gas control; the
                             basalt-to-rhyolite scale; Hawaiian and
                             Strombolian styles; Vulcanian and Plinian
                             styles; pyroclastic flows; lahars; tephra and
                             ashfall; volcanic gases and climate; the VEI
                             scale; pahoehoe, aa, and lava tubes; seismic
                             monitoring; ground deformation; gas monitoring;
                             eruption forecasting and alert levels;
                             supervolcanoes; magma chamber dynamics; crystal
                             fractionation; hazard maps and risk; PDC
                             modeling; volcano tsunamis; geothermal energy;
                             magma mixing; Vesuvius 79 AD; Tambora and
                             Krakatau; St. Helens and Pinatubo; frontiers)
  volcanology-signature    — The Volcanology Signature Database (his original
                             Signature interpretation; src signature, titles
                             suffixed " (Signature Edition)", never presented
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
from entries_volcanology import ENTRIES, SIG_TAIL

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature interpretation of volcanology: "
                "clearly labeled Signature-made, never presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked volcanology: what volcanology is; "
                "magma formation; lava; plate tectonics and volcanic settings; the Ring of "
                "Fire; shield volcanoes; stratovolcanoes; cinder cones; craters and calderas; "
                "magma chambers and plumbing; viscosity and gas control; the basalt-to-"
                "rhyolite composition scale; Hawaiian and Strombolian eruption styles; "
                "Vulcanian and Plinian styles; pyroclastic flows; lahars; tephra and ashfall; "
                "volcanic gases and climate; the VEI scale; pahoehoe, aa, and lava tubes; "
                "seismic monitoring; ground deformation; gas monitoring; eruption "
                "forecasting and alert levels; supervolcanoes; magma chamber dynamics; "
                "crystal fractionation; volcanic hazard maps and risk; pyroclastic-flow "
                "modeling; volcano tsunamis; geothermal energy; magma mixing; Vesuvius "
                "79 AD; Tambora and Krakatau; St. Helens and Pinatubo; frontiers of "
                "volcanology, organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations (what volcanology "
              "is, how magma forms, lava, plate-tectonic settings, the Ring of Fire, "
              "shield volcanoes, stratovolcanoes, cinder cones, craters and calderas, "
              "magma chambers and plumbing, viscosity and gas control, the "
              "basalt-to-rhyolite scale) -> Compounded (Hawaiian and Strombolian styles, "
              "Vulcanian and Plinian styles, pyroclastic flows, lahars, tephra and "
              "ashfall, volcanic gases and climate, the VEI scale, pahoehoe/aa/lava "
              "tubes, seismic monitoring, ground deformation, gas monitoring, eruption "
              "forecasting and alert levels) -> Advanced (supervolcanoes, magma chamber "
              "dynamics, crystal fractionation, hazard maps and risk, pyroclastic-flow "
              "modeling, volcano tsunamis, geothermal energy, magma mixing, Vesuvius "
              "79 AD, Tambora and Krakatau, St. Helens and Pinatubo, frontiers of "
              "volcanology).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search magma, VEI, pyroclastic, caldera, monitoring, Pinatubo...",
        "chat_ph": "Ask about volcanology...",
        "archive_blurb": ("Seeded %s volcanology records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled structural volcanology studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about volcanology - from magma and shield volcanoes up to VEI 8 super-eruptions and eruption forecasting." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "volcanology-study", "gen_demo_kind": "volcanology-demo",
        "source": source,
    }

CIT_PUB = "Volcanology (peer-reviewed literature and standard textbooks)."
CIT_SIG = CIT_PUB + " " + SIG_TAIL

DBCFG = {}
DBCFG["volcanology"] = _cfg(
    "volcanology", "The Volcanology Database",
    "Real, fact-checked volcanology: magma formation, lava, volcanic settings, "
    "volcano types, eruption styles, pyroclastic flows, lahars, ashfall, volcanic "
    "gases and climate, the VEI scale, volcano monitoring, eruption forecasting, "
    "supervolcanoes, magma chamber dynamics, hazard maps, volcano tsunamis, "
    "geothermal energy, and the great historic eruptions.",
    "volcanology record", "JAH-VOL-", "JAH Volcanology Archivist",
    "volcanology archivist - magma formation, lava, plate-tectonic settings, the Ring "
    "of Fire, shield/stratovolcano/cinder-cone types, craters and calderas, magma "
    "chambers, viscosity and gas control, the basalt-to-rhyolite scale, Hawaiian, "
    "Strombolian, Vulcanian and Plinian eruption styles, pyroclastic flows, lahars, "
    "tephra and ashfall, volcanic gases and climate, the VEI scale, lava-tube systems, "
    "seismic monitoring, ground deformation, gas monitoring, eruption forecasting and "
    "alert levels, supervolcanoes, magma chamber dynamics, crystal fractionation, "
    "hazard maps and risk, PDC modeling, volcano tsunamis, geothermal energy, magma "
    "mixing, Vesuvius 79 AD, Tambora, Krakatau, St. Helens, Pinatubo, frontiers; "
    "teaching progressively along the ladder from foundations through compounded to "
    "advanced; answers from many angles - definition, example, analogy, application, "
    "history, math, how-to - using only the system's own archive data",
    CIT_PUB, "public")
DBCFG["volcanology-signature"] = _cfg(
    "volcanology-signature", "The Volcanology Signature Database",
    "His original Signature interpretation of volcanology: the full ladder from "
    "magma formation and shield volcanoes to VEI 8 super-eruptions and eruption "
    "forecasting, reframed as Signature science. Clearly labeled Signature-made, "
    "never presented as authentic public record.",
    "volcanology record", "JAH-VSG-", "JAH Volcanology Archivist (Signature)",
    "volcanology archivist - Signature editions: his original Signature interpretation of "
    "volcanology, clearly labeled Signature-made and never presented as authentic public "
    "record; teaches progressively along the ladder from foundations through compounded "
    "to advanced; answers from many angles - definition, example, analogy, application, "
    "history, math, how-to - using only the system's own archive data",
    CIT_SIG, "signature")

base.DBCFG = DBCFG

# ---------------------------------------------------------------- demos
# Every demo is real, runnable, stdlib-only Python performing the actual
# volcanological calculation for its record. All are machine-executed by main().

_PREAMBLE = """import math
import re
"""

def _wrap(name, rid, group, body):
    return (base._hdr(name, rid, group) + _PREAMBLE + body.replace("NAME", json.dumps(name)))

def demo_volcano_branches(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
BRANCHES = {
    "physical volcanology": "eruption processes and deposits",
    "volcanic petrology": "chemistry and crystals of lavas",
    "volcano monitoring": "seismic, deformation, and gas surveillance",
    "volcanic hazards": "forecasting, alert levels, and risk",
    "tephrochronology": "dating the past with ash layers",
    "volcano-climate": "eruptions and the atmosphere",
}
def main():
    assert len(BRANCHES) == 6
    assert BRANCHES["tephrochronology"] == "dating the past with ash layers"
    for branch, focus in BRANCHES.items():
        print("%-22s -> %s" % (branch, focus))
    print("rule: deposits record the past, monitoring reads the present, models forecast")
    print("OK: %s mapped the branches" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_partial_melting(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
SOLIDUS, LIQUIDUS = 1100.0, 1700.0   # deg C, peridotite at depth
def melt_fraction(T):
    if T <= SOLIDUS:
        return 0.0
    if T >= LIQUIDUS:
        return 1.0
    return (T - SOLIDUS) / (LIQUIDUS - SOLIDUS)
def main():
    assert abs(melt_fraction(1400.0) - 0.5) < 1e-9
    assert melt_fraction(1000.0) == 0.0 and melt_fraction(1800.0) == 1.0
    for T in (1200.0, 1400.0, 1600.0):
        print("mantle at %4.0f C -> melt fraction %4.1f%%" % (T, 100 * melt_fraction(T)))
    print("rule: melt grows linearly between solidus and liquidus - partial, never total")
    print("OK: %s melted the mantle" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_lava_temperature(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def cool(T0, Ta, tau, t):
    return Ta + (T0 - Ta) * math.exp(-t / tau)
def main():
    T = cool(1150.0, 25.0, 3600.0, 3600.0)
    assert abs(T - 438.8) < 0.5, T
    for hrs in (0, 1, 3, 6):
        print("after %d h: surface %.0f C" % (hrs, cool(1150.0, 25.0, 3600.0, hrs * 3600.0)))
    print("rule: the crust chills fast and insulates - the interior stays molten for weeks")
    print("OK: %s cooled the lava" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_volcano_settings(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
SETTINGS = {
    "divergent": {"melting": "decompression", "magma": "fluid basalt",
                  "example": "Mid-Atlantic Ridge, East African Rift"},
    "convergent": {"melting": "flux (water from slab)", "magma": "explosive andesite-rhyolite",
                   "example": "Andes, Cascades, Japan, Indonesia"},
    "hotspot": {"melting": "plume heat", "magma": "basalt (or crustal rhyolite)",
                "example": "Hawaii, Iceland, Yellowstone"},
}
def main():
    assert set(SETTINGS) == {"divergent", "convergent", "hotspot"}
    assert SETTINGS["convergent"]["melting"].startswith("flux")
    for s, d in SETTINGS.items():
        print("%-10s | %-20s | %s (%s)" % (s, d["melting"], d["magma"], d["example"]))
    print("rule: setting predicts chemistry, chemistry predicts eruption style")
    print("OK: %s placed the volcanoes" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ring_stats(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
LENGTH_KM, VOLCANOES = 40000.0, 450
def main():
    spacing = LENGTH_KM / VOLCANOES
    assert abs(spacing - 88.9) < 0.1, spacing
    print("Ring of Fire: %.0f km of subduction, ~%d active volcanoes" % (LENGTH_KM, VOLCANOES))
    print("one volcano every %.0f km of trench, on average" % spacing)
    print("hosts the great majority of Earth's largest earthquakes (Chile 1960 M9.5)")
    print("rule: a shrinking ocean subducts on all sides - arcs ring the Pacific")
    print("OK: %s circled the Pacific" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_shield_slope(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def slope_deg(rise_km, half_width_km):
    return math.degrees(math.atan(rise_km / half_width_km))
def main():
    s1 = slope_deg(9.0, 50.0)     # Mauna Loa, seafloor base to summit
    s2 = slope_deg(4.17, 60.0)    # above sea level profile
    assert abs(s1 - 10.2) < 0.1 and abs(s2 - 4.0) < 0.1, (s1, s2)
    print("Mauna Loa full edifice: slope %.1f deg" % s1)
    print("Mauna Loa subaerial:    slope %.1f deg" % s2)
    print("shield slopes run 4-10 deg - a warrior's shield lying flat")
    print("rule: fluid basalt spreads far before it freezes - low slopes, huge volumes")
    print("OK: %s profiled the shield" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_strat_layers(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def build_cone(n_pairs):
    layers, total = [], 0.0
    for i in range(n_pairs):
        lava, ash = 3.0 + (i % 4), 1.5 + (i % 3)   # meters, deterministic
        layers += [("lava", lava), ("ash", ash)]
        total += lava + ash
    return layers, total
def main():
    layers, total = build_cone(20)
    assert len(layers) == 40
    assert all(layers[i][0] != layers[i + 1][0] for i in range(39)), "must alternate"
    assert abs(total - sum(t for _, t in layers)) < 1e-9
    print("20 eruption pairs -> %d alternating layers, %.0f m of cone" % (len(layers), total))
    print("rule: lava, ash, lava, ash - the layer cake that builds the icon")
    print("OK: %s stacked the cone" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_cone_angle(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
REPOSE_DEG = 33.0
def cone_height(radius_m):
    return radius_m * math.tan(math.radians(REPOSE_DEG))
def main():
    h = cone_height(200.0)
    assert abs(h - 129.9) < 0.2, h
    print("cinder cone, basal radius 200 m -> height %.0f m at angle of repose" % h)
    print("Paricutin grew ~150 m in its first year - loose cinders stack steep and fast")
    print("rule: loose fragments rest at ~33 deg - the cone's slope is physics, not chance")
    print("OK: %s piled the cinders" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_caldera_area(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def caldera_area(d_km):
    return math.pi * (d_km / 2.0) ** 2
def main():
    a = caldera_area(10.0)     # Crater Lake / Mazama scale
    assert abs(a - 78.54) < 0.1, a
    print("10 km caldera -> collapse area %.1f km^2" % a)
    print("Mazama's collapse ~7,700 years ago left Crater Lake in the scar")
    print("rule: caldera area scales with the chamber volume withdrawn - size is the signature")
    print("OK: %s measured the collapse" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_chamber_volume(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def ellipsoid_volume(a, b, c):
    return 4.0 / 3.0 * math.pi * a * b * c
def main():
    v = ellipsoid_volume(5.0, 3.0, 2.0)   # km semi-axes
    assert abs(v - 125.66) < 0.01, v
    print("chamber 10 x 6 x 4 km -> %.1f km^3 of mush zone" % v)
    print("chambers are crystal mush with melt, not vats of liquid")
    print("rule: volume sets the eruption budget - the chamber is the fuel tank")
    print("OK: %s sized the chamber" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_viscosity_scale(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
MU = {"basalt": 1e2, "andesite": 1e5, "dacite": 1e7, "rhyolite": 1e10}  # Pa s
def main():
    orders = math.log10(MU["rhyolite"]) - math.log10(MU["basalt"])
    assert orders == 8.0
    for rock, mu in MU.items():
        print("%-8s: 10^%.0f Pa s" % (rock, math.log10(mu)))
    print("rhyolite is 10^8 times stickier than basalt - eight orders of magnitude")
    print("rule: viscosity spans 10^8; gas trapped in sticky melt is what explodes")
    print("OK: %s scaled the stickiness" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_silica_classify(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def classify(sio2):
    if sio2 < 52.0:
        return "basalt"
    if sio2 < 63.0:
        return "andesite"
    if sio2 < 69.0:
        return "dacite"
    return "rhyolite"
def main():
    cases = [(49.0, "basalt"), (58.0, "andesite"), (66.0, "dacite"), (72.0, "rhyolite")]
    for sio2, want in cases:
        got = classify(sio2)
        assert got == want, (sio2, got)
        print("SiO2 %4.1f%% -> %s" % (sio2, got))
    print("rule: silica polymerizes the melt - the scale is an explosivity scale")
    print("OK: %s graded the rocks" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_fountain_height(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
G = 9.81
def fountain_height(v):
    return v * v / (2.0 * G)
def main():
    h = fountain_height(100.0)
    assert abs(h - 509.7) < 0.2, h
    v_iki = math.sqrt(2 * G * 580.0)   # Kilauea Iki 1959, ~580 m fountain
    print("exit velocity 100 m/s -> fountain %.0f m" % h)
    print("Kilauea Iki's 580 m fountain needed ~%.0f m/s exit velocity" % v_iki)
    assert abs(v_iki - 106.7) < 0.2
    print("rule: h = v^2/2g - fountains are ballistics")
    print("OK: %s jetted the fountain" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_plinian_column(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def column_height_km(mer_kg_s):
    return 0.32 * mer_kg_s ** 0.25     # Morton-type scaling (illustrative)
def main():
    h = column_height_km(1.0e8)        # Pinatubo-scale mass eruption rate
    assert 30.0 < h < 45.0, h
    print("MER 1e8 kg/s -> column %.0f km (Pinatubo scale)" % h)
    print("MER 1e7 kg/s -> column %.0f km" % column_height_km(1.0e7))
    print("column height ~ MER^1/4: taller columns mean vastly larger eruptions")
    print("rule: if the column goes too dense to stay buoyant, it collapses to pyroclastic flows")
    print("OK: %s raised the column" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pdc_runout(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
G = 9.81
HEIM = 0.2   # energy-cone slope
def base_velocity(drop_m):
    return math.sqrt(2 * G * drop_m)
def runout(drop_m):
    return drop_m / HEIM
def main():
    v = base_velocity(1000.0)
    assert abs(v - 140.0) < 1.0, v
    print("1000 m column collapse -> basal speed %.0f m/s (%.0f km/h)" % (v, v * 3.6))
    print("energy-cone runout: %.1f km" % (runout(1000.0) / 1000.0))
    assert abs(runout(1500.0) - 7500.0) < 1e-9
    print("rule: the flow stops where its energy is spent - runout is an energy budget")
    print("OK: %s ran the flow" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_lahar_velocity(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def manning_v(n, R, S):
    return (1.0 / n) * R ** (2.0 / 3.0) * math.sqrt(S)
def main():
    v = manning_v(0.05, 3.0, 0.10)   # rough channel, 3 m hydraulic radius, 10% slope
    assert abs(v - 13.2) < 0.2, v
    print("lahar in confined valley: %.1f m/s = %.0f km/h" % (v, v * 3.6))
    print("denser than water, so it carries meter-scale boulders")
    print("rule: confinement keeps lahars fast and deep tens of km from the volcano")
    print("OK: %s timed the mudflow" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tephra_fallout(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def thickness(t0_cm, decay_km, x_km):
    return t0_cm * math.exp(-x_km / decay_km)
def main():
    t20 = thickness(100.0, 20.0, 20.0)
    assert abs(t20 - 36.79) < 0.1, t20
    print("100 cm at vent -> %.1f cm at 20 km, %.1f cm at 60 km" %
          (t20, thickness(100.0, 20.0, 60.0)))
    print("isopach thinning with distance encodes column height and wind")
    print("rule: T(x) = T0 e^(-x/lambda) - integrate the isopachs to get the volume")
    print("OK: %s mapped the ashfall" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_aerosol_cooling(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def cooling_c(so2_mt):
    return -0.025 * so2_mt     # illustrative linear scaling
def main():
    dT = cooling_c(20.0)       # Pinatubo 1991, ~20 Mt SO2
    assert abs(dT - (-0.5)) < 1e-9
    print("Pinatubo ~20 Mt SO2 -> about %.1f C global cooling for 2-3 years" % dT)
    print("Tambora ~60 Mt SO2 -> about %.1f C (illustrative): the Year Without a Summer" %
          cooling_c(60.0))
    print("rule: stratospheric sulfur reflects sunlight - tropospheric sulfur just rains out")
    print("OK: %s cooled the planet" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_vei_table(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
BINS = [(1e-4, 0), (1e-3, 1), (1e-2, 2), (0.1, 3), (1.0, 4),
        (10.0, 5), (100.0, 6), (1000.0, 7), (float("inf"), 8)]
def vei(dre_km3):
    for hi, v in BINS:
        if dre_km3 < hi:
            return v
    return 8
def main():
    cases = [(1.0, 5, "St. Helens 1980"), (10.0, 6, "Pinatubo 1991"),
             (150.0, 7, "Tambora 1815"), (2500.0, 8, "Huckleberry Ridge")]
    for vol, want, label in cases:
        got = vei(vol)
        assert got == want, (label, got)
        print("%-18s %6.0f km^3 -> VEI %d" % (label, vol, got))
    print("rule: each VEI step is ~10x the volume - logarithmic, like magnitude")
    print("OK: %s rated the eruptions" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_lava_morphology(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def morphology(visc_pa_s, crystal_frac):
    if visc_pa_s > 1e4 or crystal_frac > 0.4:
        return "aa (torn clinker)"
    return "pahoehoe (smooth ropy)"
def main():
    cases = [(1e2, 0.05, "pahoehoe (smooth ropy)"), (5e4, 0.3, "aa (torn clinker)"),
             (1e3, 0.5, "aa (torn clinker)")]
    for mu, x, want in cases:
        got = morphology(mu, x)
        assert got == want, (mu, x, got)
        print("viscosity 10^%.0f Pa s, crystals %d%% -> %s" % (math.log10(mu), 100 * x, got))
    print("rule: cooling vs. shear decides - the crust tears when it can no longer flow smooth")
    print("OK: %s read the flow surface" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_rsam_alarm(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def alarm_index(rsam, baseline, thresh=3.0, need=3):
    run = 0
    for i, a in enumerate(rsam):
        run = run + 1 if a > thresh * baseline else 0
        if run >= need:
            return i - need + 1
    return None
def main():
    baseline = 100.0
    rsam = [95, 102, 98, 105, 99, 420, 510, 480, 530, 120, 98]
    idx = alarm_index(rsam, baseline)
    assert idx == 5, idx
    print("RSAM baseline %.0f; alarm trips at sample %d (3x baseline, 3 in a row)" % (baseline, idx))
    print("rule: one spike is noise; a sustained climb is magma")
    print("OK: %s watched the heartbeat" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_mogi_uplift(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def mogi_dh(dV, depth_m, r_m):
    return (3.0 * dV / (4.0 * math.pi)) * depth_m / (depth_m ** 2 + r_m ** 2) ** 1.5
def main():
    dh0 = mogi_dh(1.0e7, 5000.0, 0.0)      # 0.01 km^3 intruded at 5 km depth
    assert abs(dh0 - 0.0955) < 0.001, dh0
    print("0.01 km^3 at 5 km depth -> summit uplift %.1f cm" % (100 * dh0))
    print("uplift 5 km out: %.1f cm" % (100 * mogi_dh(1.0e7, 5000.0, 5000.0)))
    print("rule: the uplift pattern gives depth and volume - inflation locates magma")
    print("OK: %s measured the swelling" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_so2_flux(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def flux_t_per_day(conc_kg_m3, wind_m_s, plume_area_m2):
    return conc_kg_m3 * wind_m_s * plume_area_m2 * 86.4
def main():
    f = flux_t_per_day(1.0e-5, 5.0, 1.0e6)
    assert abs(f - 4320.0) < 1.0, f
    print("plume 10 mg/m^3 SO2, 5 m/s wind, 1 km^2 cross-section -> %.0f t/day" % f)
    print("rising flux against baseline = fresh gas-rich magma ascending")
    print("rule: flux = concentration x wind x area - the volcano's exhalation metered")
    print("OK: %s sniffed the plume" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_alert_logic(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def alert(seismic, deformation, gas):
    score = sum((seismic, deformation, gas))
    if score >= 3:
        return "Warning / Red"
    if score == 2:
        return "Watch / Orange"
    if score == 1:
        return "Advisory / Yellow"
    return "Normal / Green"
def main():
    cases = [((0, 0, 0), "Normal / Green"), ((1, 0, 0), "Advisory / Yellow"),
             ((1, 1, 0), "Watch / Orange"), ((1, 1, 1), "Warning / Red")]
    for flags, want in cases:
        got = alert(*flags)
        assert got == want, (flags, got)
        print("seismic=%d deformation=%d gas=%d -> %s" % (flags + (got,)))
    print("rule: no single parameter triggers Warning - independent streams must agree")
    print("OK: %s set the alert level" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_supervolcano_scale(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
VOLS = {"Huckleberry Ridge (Yellowstone)": 2500.0, "Toba": 2800.0,
        "Oruanui (Taupo)": 1170.0, "Pinatubo 1991": 10.0}   # km^3
def main():
    ratio = VOLS["Huckleberry Ridge (Yellowstone)"] / VOLS["Pinatubo 1991"]
    assert abs(ratio - 250.0) < 1e-9
    for label, v in VOLS.items():
        print("%-32s %6.0f km^3  (= %.0f Pinatubos)" % (label, v, v / VOLS["Pinatubo 1991"]))
    print("rule: VEI 8 means >1000 km^3 - hundreds of Pinatubos in one eruption")
    print("OK: %s weighed the giants" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_rayleigh_number(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def rayleigh(alpha, g, dT, d, kappa, nu):
    return alpha * g * dT * d ** 3 / (kappa * nu)
def main():
    Ra = rayleigh(5.0e-5, 9.81, 100.0, 1000.0, 1.0e-6, 0.037)
    assert Ra > 1e12, Ra
    print("km-scale basaltic chamber: Ra = %.2e (convection starts at ~1708)" % Ra)
    print("chambers stir themselves - recharge mixes, crystals stay suspended")
    print("rule: buoyancy beats viscosity by twelve orders of magnitude - the mush convects")
    print("OK: %s stirred the chamber" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_rayleigh_fractionation(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def enrich(F, D):
    return F ** (D - 1.0)     # C/C0, Rayleigh fractionation
def main():
    inc = enrich(0.5, 0.1)    # incompatible element, half the melt left
    comp = enrich(0.5, 5.0)   # compatible element
    assert abs(inc - 1.8667) < 0.01 and abs(comp - 0.0625) < 1e-9, (inc, comp)
    print("F=0.5: incompatible element enriched x%.2f; compatible depleted to %.3f" % (inc, comp))
    print("this is how basalt differentiates toward rhyolite")
    print("rule: C = C0 F^(D-1) - the petrologist's tape recorder")
    print("OK: %s refined the magma" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hazard_probability(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def prob_in_years(rate, years):
    return 1.0 - math.exp(-rate * years)
def main():
    p = prob_in_years(0.002, 50.0)   # 1-in-500-year event, 50-year exposure
    assert abs(p - 0.0952) < 0.001, p
    print("annual rate 0.002 -> P(50 yr) = %.1f%%" % (100 * p))
    print("risk = hazard x exposure x vulnerability - the map is only the first factor")
    print("rule: probability, never a date - hazard is a rate turned into odds")
    print("OK: %s priced the risk" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_energy_cone(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
HEIM = 0.2
def runout(collapse_m):
    return collapse_m / HEIM
def main():
    L = runout(2000.0)
    assert abs(L - 10000.0) < 1e-9
    print("2000 m collapse height -> energy-cone runout %.0f km" % (L / 1000.0))
    print("terrain above the cone is safe; below it is inundated")
    print("rule: L = H/0.2 - the zoning workhorse, calibrated on real deposits")
    print("OK: %s drew the energy cone" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tsunami_wave(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def initial_wave_m(slide_km3):
    return 8.0 * math.sqrt(slide_km3)   # illustrative scaling
def main():
    h1 = initial_wave_m(0.3)    # Anak Krakatau 2018 scale
    h2 = initial_wave_m(10.0)   # Krakatau 1883 scale
    assert abs(h1 - 4.38) < 0.05 and abs(h2 - 25.3) < 0.2, (h1, h2)
    print("0.3 km^3 flank collapse -> ~%.0f m initial wave (Anak Krakatau 2018 scale)" % h1)
    print("10 km^3 collapse        -> ~%.0f m initial wave (Krakatau 1883 scale)" % h2)
    print("rule: even sub-km^3 collapses make deadly local waves - and they arrive in minutes")
    print("OK: %s raised the wave" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_geothermal_power(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
EFF = 0.15
def electric_mw(thermal_mw):
    return EFF * thermal_mw
def main():
    Pe = electric_mw(300.0)
    assert abs(Pe - 45.0) < 1e-9
    print("300 MW of volcanic heat -> %.0f MW electricity at 15%% efficiency" % Pe)
    print("enough for ~%.0f homes; Iceland runs ~25-30%% of its grid this way" % (Pe * 1e6 / 1000.0))
    print("rule: manage the reservoir with reinjection - mine the heat, not the steam")
    print("OK: %s tapped the heat" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_mixing_line(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def mix(f, c1, c2):
    return f * c1 + (1.0 - f) * c2
def main():
    m = mix(0.5, 50.0, 72.0)   # basalt + rhyolite SiO2
    assert abs(m - 61.0) < 1e-9
    for f in (0.25, 0.5, 0.75):
        print("f=%.2f basalt -> SiO2 %.1f%% (lever rule on the mixing line)" % (f, mix(f, 50.0, 72.0)))
    print("rule: binary mixing draws a straight line - the mixture is the weighted average")
    print("OK: %s blended the magmas" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_plinian_dispersal(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def cone_volume_km3(t0_m, area_m2):
    return t0_m * area_m2 / 2.0 / 1.0e9
def main():
    v = cone_volume_km3(2.0, 5.0e8)
    assert abs(v - 0.5) < 1e-9, v
    print("2 m max thickness over 500 km^2 -> %.1f km^3 (cone integration)" % v)
    print("integrate the isopachs, convert to dense-rock equivalent, read the VEI")
    print("rule: V = T0*A/2 - the deposit is the eruption's receipt")
    print("OK: %s integrated the isopachs" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_climate_impact(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def cooling_c(so2_mt):
    return -0.025 * so2_mt     # illustrative linear scaling
def main():
    tambora = cooling_c(60.0)
    assert abs(tambora - (-1.5)) < 1e-9
    print("Tambora ~60 Mt SO2 -> about %.1f C cooling (illustrative)" % tambora)
    print("1816: the Year Without a Summer - snow in July, failed harvests")
    print("rule: tropical sulfur spreads to both hemispheres; ice cores keep the receipts")
    print("OK: %s read the cold year" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_blast_energy(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
MT_TO_J = 4.184e15
def main():
    E = 24.0 * MT_TO_J          # St. Helens lateral blast, ~24 Mt TNT equivalent
    assert abs(E - 1.00416e17) / 1e17 < 0.01, E
    print("lateral blast energy: %.2e J over 600 km^2" % E)
    print("energy density: %.1e J/km^2 - forest flattened, soil stripped" % (E / 600.0))
    print("rule: the landslide depressurized the system in seconds - the blast was the uncorking")
    print("OK: %s measured the blast" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_forecast_bayes(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def posterior(prior, like_erupt, like_quiet):
    num = like_erupt * prior
    return num / (num + like_quiet * (1.0 - prior))
def main():
    p = posterior(0.01, 0.8, 0.05)
    assert abs(p - 0.1391) < 0.001, p
    print("prior 1%% -> with strong precursors, posterior %.1f%%" % (100 * p))
    print("each new datum updates the odds - Bayes' rule as an operational tool")
    print("rule: forecasts are probabilities that move with the data, never fixed dates")
    print("OK: %s updated the odds" % NAME)
if __name__ == "__main__":
    main()
''')

DEMOS = {
    "volcano_branches": demo_volcano_branches, "partial_melting": demo_partial_melting,
    "lava_temperature": demo_lava_temperature, "volcano_settings": demo_volcano_settings,
    "ring_stats": demo_ring_stats, "shield_slope": demo_shield_slope,
    "strat_layers": demo_strat_layers, "cone_angle": demo_cone_angle,
    "caldera_area": demo_caldera_area, "chamber_volume": demo_chamber_volume,
    "viscosity_scale": demo_viscosity_scale, "silica_classify": demo_silica_classify,
    "fountain_height": demo_fountain_height, "plinian_column": demo_plinian_column,
    "pdc_runout": demo_pdc_runout, "lahar_velocity": demo_lahar_velocity,
    "tephra_fallout": demo_tephra_fallout, "aerosol_cooling": demo_aerosol_cooling,
    "vei_table": demo_vei_table, "lava_morphology": demo_lava_morphology,
    "rsam_alarm": demo_rsam_alarm, "mogi_uplift": demo_mogi_uplift,
    "so2_flux": demo_so2_flux, "alert_logic": demo_alert_logic,
    "supervolcano_scale": demo_supervolcano_scale, "rayleigh_number": demo_rayleigh_number,
    "rayleigh_fractionation": demo_rayleigh_fractionation,
    "hazard_probability": demo_hazard_probability, "energy_cone": demo_energy_cone,
    "tsunami_wave": demo_tsunami_wave, "geothermal_power": demo_geothermal_power,
    "mixing_line": demo_mixing_line, "plinian_dispersal": demo_plinian_dispersal,
    "climate_impact": demo_climate_impact, "blast_energy": demo_blast_energy,
    "forecast_bayes": demo_forecast_bayes,
}

# ---------------------------------------------------------------- records

def build_records(slug, source):
    cfg = DBCFG[slug]
    sig = source == "signature"
    # Teaching-ladder order: stable sort by ladder_rank (entries are already
    # in ladder order in entries_volcanology.py).
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
    for slug in ("volcanology", "volcanology-signature"):
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
