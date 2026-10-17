#!/usr/bin/env python3
"""Build the Botany field databases for JAH Databases (field #4, taxonomy order).

Verified 2026-10-17: the manifest holds an `everything-biology` database
with 12 records, only ONE of which is botany ("Botany: Photosynthesis and
Plant Structure") — thin, single-record coverage, not the discipline. So
this build creates two NEW databases:

  botany              — The Botany Database (public-harvest: real,
                        fact-checked botany — plant anatomy/morphology,
                        photosynthesis, plant physiology, taxonomy and
                        systematics (APG IV), plant ecology, plant
                        genetics, plant pathology, economic botany,
                        bryophytes, ferns, gymnosperms, angiosperms)
  botany-signature    — The Botany Signature Database (his original
                        Signature interpretation; src signature, titles
                        suffixed " (Signature Edition)", never presented as
                        authentic public record)

36 records each, ordered by the teaching ladder (ladder_rank 1-10, ladder_tier
foundations/compounded/advanced); the shard index is written in ladder order so
pages present simple -> compounded -> complex.

Every record: description + how-it-works + key points + requirements + standards
+ citations + working demonstration code (real, runnable, stdlib-only Python;
machine-executed OK).

Never the words "bat belt" anywhere. No website references. No Facebook.
"""
import importlib.util
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = "/home/hatch/workspace/jah-databases"
SHARD = "/home/hatch/workspace/jah-databases-data-1"
SHARD_BASE = "https://justinahiggins614-cmyk.github.io/jah-databases-data-1"
TEMPLATE = os.path.join(REPO, "db", "public-synthetic-intelligence", "index.html")

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base

sys.path.insert(0, HERE)
from entries_botany import ENTRIES, SIG_TAIL

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals — his original Signature interpretation of botany: "
                "clearly labeled Signature-made, never presented as authentic public record.")
    pub_line = ("Public records — real, fact-checked botany: plant anatomy and morphology, "
                "photosynthesis, plant physiology, taxonomy and systematics (APG IV), plant "
                "ecology, plant genetics, plant pathology, economic botany, bryophytes, "
                "ferns, gymnosperms, and angiosperms, organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations (what a plant is, "
              "the plant cell, roots, stems, leaves, the light reactions, the Calvin "
              "cycle, water transport, life cycles) -> Compounded (alternation of "
              "generations, bryophytes, ferns, gymnosperms, the flower, angiosperms, "
              "pollination, seed dispersal, germination, hormones, tropisms, C3/C4/CAM, "
              "Mendel, mycorrhizae and nitrogen fixation, plant ecology, APG IV taxonomy, "
              "carnivorous plants) -> Advanced (plant pathology, economic botany, "
              "secondary metabolites, drought physiology, tissue culture, grafting, "
              "dendrochronology, epiphytes, paleobotany, plant breeding).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s — %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search plants, photosynthesis, flowers, crops, techniques...",
        "chat_ph": "Ask about botany...",
        "archive_blurb": ("Seeded %s botany records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations · Compounded · Advanced — each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled structural botany studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about botany — from what a plant is up to crop improvement and plant medicine." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "botany-study", "gen_demo_kind": "botany-demo",
        "source": source,
    }

CIT_PUB = "Botany (peer-reviewed literature and standard textbooks)."
CIT_SIG = CIT_PUB + " " + SIG_TAIL

DBCFG = {}
DBCFG["botany"] = _cfg(
    "botany", "The Botany Database",
    "Real, fact-checked botany: plant anatomy and morphology, photosynthesis, "
    "plant physiology, taxonomy and systematics (APG IV), plant ecology, plant "
    "genetics, plant pathology, economic botany, bryophytes, ferns, gymnosperms, "
    "and angiosperms.",
    "botany record", "JAH-BOT-", "JAH Botany Archivist",
    "botany archivist — plant anatomy and morphology, photosynthesis, plant "
    "physiology, taxonomy and systematics (APG IV), plant ecology, plant genetics, "
    "plant pathology, economic botany, bryophytes, ferns, gymnosperms, angiosperms; "
    "teaching progressively along the ladder from foundations (what a plant is, the "
    "plant cell, roots, stems, leaves, light reactions, Calvin cycle, water "
    "transport, life cycles) through compounded (alternation of generations, "
    "bryophytes, ferns, gymnosperms, the flower, angiosperms, pollination, seed "
    "dispersal, germination, hormones, tropisms, C3/C4/CAM, Mendel, mycorrhizae, "
    "plant ecology, APG IV taxonomy, carnivorous plants) to advanced (plant "
    "pathology, economic botany, secondary metabolites, drought physiology, tissue "
    "culture, grafting, dendrochronology, epiphytes, paleobotany, plant breeding); "
    "answers from many angles — definition, example, analogy, application, "
    "history, math, how-to — using only the system's own archive data",
    CIT_PUB, "public")
DBCFG["botany-signature"] = _cfg(
    "botany-signature", "The Botany Signature Database",
    "His original Signature interpretation of botany: the full ladder from what a "
    "plant is to plant breeding, reframed as Signature engineering. Clearly "
    "labeled Signature-made, never presented as authentic public record.",
    "botany record", "JAH-BSG-", "JAH Botany Archivist (Signature)",
    "botany archivist — Signature editions: his original Signature interpretation of "
    "botany, clearly labeled Signature-made and never presented as authentic public "
    "record; teaches progressively along the ladder from foundations through compounded "
    "to advanced; answers from many angles — definition, example, analogy, application, "
    "history, math, how-to — using only the system's own archive data",
    CIT_SIG, "signature")

base.DBCFG = DBCFG

# ---------------------------------------------------------------- demos
# Every demo is real, runnable, stdlib-only Python performing the actual
# botanical calculation for its record. All are machine-executed by main().

_PREAMBLE = """import math
"""

def _wrap(name, rid, group, body):
    return (base._hdr(name, rid, group) + _PREAMBLE + body.replace("NAME", json.dumps(name)))

def demo_plant_diversity(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    vascular = 391000
    flowering = 295000
    share = flowering / vascular
    print("vascular plant species ~%d; flowering ~%d -> %.1f %% angiosperms" % (
        vascular, flowering, 100 * share))
    assert abs(share - 0.7545) < 0.01
    plant_C, total_C = 450.0, 550.0          # gigatonnes of carbon
    print("plant biomass %.0f Gt C of %.0f Gt total -> %.0f %%" % (
        plant_C, total_C, 100 * plant_C / total_C))
    assert abs(plant_C / total_C - 0.818) < 0.01
    new_per_year = 2000
    print("~%d new plant species described per year" % new_per_year)
    assert new_per_year > 0
    print("OK: %s counted the green kingdom" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_turgor_pressure(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def solute_potential(C_mol_L, T_K=298.0):
    R = 0.00831   # L*MPa / (mol*K)
    return -C_mol_L * R * T_K
def main():
    psi_s = solute_potential(0.30)
    print("cell sap 0.30 mol/L -> solute potential %.3f MPa" % psi_s)
    assert abs(psi_s - (-0.743)) < 0.01
    psi_p = 0.80                              # turgor pressure
    psi_leaf = psi_s + psi_p
    print("leaf water potential = %.3f + %.2f = %.3f MPa" % (psi_s, psi_p, psi_leaf))
    assert abs(psi_leaf - 0.057) < 0.01
    # wilted cell: turgor lost
    print("wilted: turgor -> 0, leaf potential = %.3f MPa (limp)" % psi_s)
    assert psi_s < -0.5
    print("OK: %s pressurized the plant cell" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_root_surface(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    r, L = 0.0005, 0.01                    # 1 cm of root, 0.5 mm radius (meters)
    cyl = 2 * math.pi * r * L
    hairs_per_cm = 10000
    hair_d, hair_L = 1e-5, 5e-4           # 10 um diameter, 0.5 mm long
    hair_area = hairs_per_cm * math.pi * hair_d * hair_L
    print("1 cm of bare root: %.2e m^2" % cyl)
    print("its %d root hairs: %.2e m^2" % (hairs_per_cm, hair_area))
    ratio = hair_area / cyl
    print("root hairs multiply absorptive area ~%.1fx" % ratio)
    assert abs(cyl - 3.1416e-5) / 3.1416e-5 < 0.01
    assert abs(ratio - 5.0) < 0.5
    print("OK: %s measured the root's reach" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_internode_growth(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    L0, rate, days = 2.0, 0.05, 30        # cm, per day, days
    L = L0 * (1 + rate) ** days
    print("internode %.1f cm growing %.0f %%/day for %d days -> %.2f cm" % (L0, 100 * rate, days, L))
    assert abs(L - 8.64) < 0.05
    # doubling time of the growing tip
    dbl = math.log(2) / math.log(1 + rate)
    print("tip length doubles every %.1f days" % dbl)
    assert abs(dbl - 14.2) < 0.3
    print("OK: %s grew the shoot" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_leaf_area_index(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def light_below(LAI, k=0.7):
    return math.exp(-k * LAI)              # Beer's law through the canopy
def main():
    leaves, area_each, ground = 30, 0.02, 0.2
    LAI = leaves * area_each / ground
    print("%d leaves x %.2f m^2 over %.1f m^2 ground -> LAI %.1f" % (leaves, area_each, ground, LAI))
    assert abs(LAI - 3.0) < 1e-9
    transmitted = light_below(LAI)
    print("light reaching the forest floor: %.1f %%" % (100 * transmitted))
    assert abs(transmitted - 0.1225) < 0.005
    assert light_below(6.0) < light_below(3.0) < light_below(0.0) == 1.0
    print("OK: %s shaded the canopy" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_photon_energy(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def photon_kJ_per_mol(wavelength_nm):
    h, c, NA = 6.626e-34, 3.0e8, 6.022e23
    E_J = h * c / (wavelength_nm * 1e-9)
    return E_J * NA / 1000.0
def main():
    e680 = photon_kJ_per_mol(680.0)        # red light, photosystem II peak
    e450 = photon_kJ_per_mol(450.0)        # blue light
    print("one mole of 680 nm photons carries %.1f kJ" % e680)
    print("one mole of 450 nm photons carries %.1f kJ" % e450)
    assert abs(e680 - 176.0) < 1.0
    assert e450 > e680
    per_O2 = 8 * e680
    print("minimum ~8 photons per O2 evolved -> ~%.0f kJ per mole of O2" % per_O2)
    assert abs(per_O2 - 1408.0) < 8.0
    print("OK: %s priced the photons" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_calvin_stoichiometry(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def calvin_cost(co2):
    # 3 ATP + 2 NADPH per CO2 fixed (9 ATP + 6 NADPH per 3 CO2 -> 1 net G3P)
    return 3 * co2, 2 * co2
def main():
    atp, nadph = calvin_cost(6)
    print("6 CO2 fixed -> costs %d ATP + %d NADPH -> 1 glucose equivalent" % (atp, nadph))
    assert (atp, nadph) == (18, 12)
    atp3, nadph3 = calvin_cost(3)
    print("3 CO2 fixed -> %d ATP + %d NADPH -> 1 net G3P (cycle turns on)" % (atp3, nadph3))
    assert (atp3, nadph3) == (9, 6)
    # overall photosynthesis equation balances
    print("net: 6CO2 + 6H2O --light--> C6H12O6 + 6O2")
    print("OK: %s balanced the Calvin cycle" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_transpiration_rate(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def tension_MPa(height_m):
    return 1000.0 * 9.81 * height_m / 1e6   # rho*g*h in MPa
def main():
    leaves, per_leaf_mL = 200000, 1.0
    liters = leaves * per_leaf_mL / 1000.0
    print("%d leaves x %.0f mL/day -> %.0f L/day transpired" % (leaves, per_leaf_mL, liters))
    assert liters == 200.0
    t100 = tension_MPa(100.0)
    print("100 m water column hangs under %.3f MPa of tension" % t100)
    assert abs(t100 - 0.981) < 0.02
    assert tension_MPa(10.0) < tension_MPa(100.0)
    print("OK: %s pulled the transpiration stream" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_life_cycle_table(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def classify(lifespan_days):
    if lifespan_days < 365:
        return "annual"
    if lifespan_days < 730:
        return "biennial"
    return "perennial"
def main():
    table = [("wheat", 120), ("marigold", 150), ("carrot", 400), ("foxglove", 500),
             ("oak", 36500), ("lavender", 4000)]
    for pname, days in table:
        print("  %-10s %6d days -> %s" % (pname, days, classify(days)))
    assert classify(120) == "annual"
    assert classify(400) == "biennial"
    assert classify(36500) == "perennial"
    assert classify(364) == "annual" and classify(729) == "biennial"
    print("OK: %s scheduled the plant lifetimes" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_alternation_table(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
DOMINANT = {"moss": "gametophyte (leafy green plant); sporophyte a dependent stalk",
            "fern": "sporophyte (frondy plant); gametophyte a tiny free-living prothallus",
            "pine": "sporophyte (tree); gametophyte microscopic inside pollen and ovule",
            "rose": "sporophyte (bush); gametophyte microscopic inside pollen and ovule"}
def main():
    print("sporophyte (2n) --meiosis--> spores (n) --mitosis--> gametophyte (n)")
    print("gametophyte (n) --mitosis--> gametes (n) --fertilization--> zygote (2n)")
    for plant, dom in DOMINANT.items():
        print("  %-6s dominant: %s" % (plant, dom))
    assert "gametophyte" in DOMINANT["moss"] and "dependent stalk" in DOMINANT["moss"]
    assert DOMINANT["fern"].startswith("sporophyte")
    assert "microscopic" in DOMINANT["pine"]
    print("evolutionary trend: sporophyte dominance rises, gametophyte shrinks")
    print("OK: %s alternated the generations" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_moss_water(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    dry_g, uptake_factor = 10.0, 20.0     # Sphagnum holds ~20x its dry weight
    water_g = dry_g * uptake_factor
    print("%.0f g of dry Sphagnum soaks up %.0f g of water" % (dry_g, water_g))
    assert water_g == 200.0
    # poikilohydry: revive after drying
    dried, revived = 0.05, 0.95           # 5% water content -> 95% photosynthetic recovery
    print("dried to %.0f %% water, rewetted -> %.0f %% function restored" % (100 * dried, 100 * revived))
    assert dried < 0.1 and revived > 0.9
    print("OK: %s wrung out the moss" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_spore_counts(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    per_sporangium = 64                    # typical leptosporangiate count
    per_sorus, sori_per_frond = 20, 50
    per_frond = per_sporangium * per_sorus * sori_per_frond
    print("sporangium %d spores x %d sporangia/sorus x %d sori = %d spores per frond" % (
        per_sporangium, per_sorus, sori_per_frond, per_frond))
    assert per_frond == 64000
    fronds = 100
    print("%d fronds -> %.1f million spores from one fern" % (fronds, per_frond * fronds / 1e6))
    assert per_frond * fronds == 6400000
    print("OK: %s counted the spore rain" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_cone_seeds(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    scales, ovules_per_scale = 100, 2
    max_seeds = scales * ovules_per_scale
    print("female cone: %d scales x %d ovules = %d potential seeds" % (
        scales, ovules_per_scale, max_seeds))
    assert max_seeds == 200
    fertilized = 0.80
    seeds = int(max_seeds * fertilized)
    print("at %.0f %% fertilization -> %d seeds per cone" % (100 * fertilized, seeds))
    assert seeds == 160
    # wind pollination waste: millions of grains per cone's worth of ovules
    grains = 2000000
    print("male cones shed ~%d pollen grains to fertilize those %d ovules (%.0f grains/ovule)" % (
        grains, max_seeds, grains / max_seeds))
    assert grains / max_seeds == 10000.0
    print("OK: %s audited the cone" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_flower_parts(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
ABC = {"A": "sepal", "A+B": "petal", "B+C": "stamen", "C": "carpel"}
def main():
    lily = {"tepals": 6, "stamens": 6, "carpels": 3}
    total = sum(lily.values())
    print("lily: %d tepals + %d stamens + %d carpels = %d floral organs" % (
        lily["tepals"], lily["stamens"], lily["carpels"], total))
    assert total == 15
    print("ABC model:")
    for genes, organ in ABC.items():
        print("  genes %-3s -> %s" % (genes, organ))
    assert ABC["A+B"] == "petal" and ABC["B+C"] == "stamen"
    assert ABC["A"] == "sepal" and ABC["C"] == "carpel"
    print("OK: %s dissected the flower" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_angiosperm_share(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    groups = {"angiosperms": 295000, "gymnosperms": 1100, "ferns": 10500,
              "bryophytes": 20000}
    total = 391000
    for gname, n in groups.items():
        print("  %-12s %6d species  %5.1f %%" % (gname, n, 100 * n / total))
    assert abs(100 * groups["angiosperms"] / total - 75.4) < 0.5
    assert abs(100 * groups["gymnosperms"] / total - 0.28) < 0.05
    others = groups["gymnosperms"] + groups["ferns"] + groups["bryophytes"]
    assert groups["angiosperms"] > 9 * others
    print("angiosperms outnumber all other vascular plants combined %.1fx over" % (
        groups["angiosperms"] / others))
    print("OK: %s measured the flowering takeover" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pollination_matrix(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
SYNDROMES = {
    "bee":   ("blue/yellow, nectar guides, landing platform", "day, sweet scent"),
    "moth":  ("white, tubular, night-opening", "night, strong sweet scent"),
    "bird":  ("red, tubular, odorless", "day, copious dilute nectar"),
    "bat":   ("large, pale, musky, night-opening", "night, sturdy flowers"),
    "wind":  ("small, green, scentless, huge pollen output", "feathery stigmas"),
}
def main():
    for courier, (look, reward) in SYNDROMES.items():
        print("  %-5s %-42s | %s" % (courier, look, reward))
    assert len(SYNDROMES) == 5
    assert SYNDROMES["bird"][0].startswith("red")
    assert "night" in SYNDROMES["moth"][0]
    assert "huge pollen" in SYNDROMES["wind"][0]
    print("OK: %s matched flowers to couriers" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_dispersal_range(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def ballistic_range(v, angle_deg, g=9.81):
    return v ** 2 * math.sin(2 * math.radians(angle_deg)) / g
def wind_carry(height_m, sink_m_s, wind_m_s):
    return height_m / sink_m_s * wind_m_s
def main():
    r = ballistic_range(5.0, 45.0)
    print("explosive pod: 5 m/s at 45 deg -> %.2f m" % r)
    assert abs(r - 2.55) < 0.02
    d = wind_carry(20.0, 1.0, 3.0)
    print("maple samara: 20 m fall at 1 m/s sink, 3 m/s wind -> %.0f m carried" % d)
    assert d == 60.0
    assert ballistic_range(5.0, 30.0) < ballistic_range(5.0, 45.0)
    print("OK: %s ranged the seed artillery" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_germination_test(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def germination_pct(germinated, total):
    return 100.0 * germinated / total
def viability(n0, k_per_year, years):
    return n0 * math.exp(-k_per_year * years)
def main():
    gp = germination_pct(87, 100)
    print("seed lot: 87 of 100 germinated -> %.0f %% (commercial bar: 85 %%)" % gp)
    assert gp == 87.0
    assert gp >= 85.0, "lot fails certification"
    v10 = viability(100.0, 0.05, 10.0)
    print("viability after 10 years at 5 %%/yr decay: %.1f %%" % v10)
    assert abs(v10 - 60.7) < 0.5
    print("OK: %s tested the seed lot" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_auxin_dose_response(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def inhibition(dose_uM, ic50_uM, n=1.0):
    return 1 / (1 + (ic50_uM / dose_uM) ** n)
def main():
    dose = 1.0   # uM auxin
    shoot = inhibition(dose, 10.0)     # shoots tolerate auxin
    root = inhibition(dose, 0.01)      # roots are ~1000x more sensitive
    print("at %.1f uM auxin: shoot growth inhibited %.1f %%, root growth inhibited %.1f %%" % (
        dose, 100 * shoot, 100 * root))
    assert abs(shoot - 0.0909) < 1e-4
    assert abs(root - 0.9901) < 1e-4
    print("same hormone, opposite outcome: response depends on tissue sensitivity")
    assert inhibition(10.0, 10.0) == 0.5
    print("OK: %s dosed the auxin" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_phototropism_angle(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    v_shade, v_lit, diameter = 1.2, 0.8, 2.0   # mm/h elongation, mm stem diameter
    curve_rad_per_h = (v_shade - v_lit) / diameter
    hours = 3.0
    angle_deg = curve_rad_per_h * hours * 57.2958
    print("shaded side %.1f mm/h vs lit side %.1f mm/h, stem %.0f mm wide" % (
        v_shade, v_lit, diameter))
    print("curvature rate %.2f rad/h -> after %.0f h the tip bends %.1f deg toward light" % (
        curve_rad_per_h, hours, angle_deg))
    assert abs(angle_deg - 34.4) < 0.5
    assert curve_rad_per_h > 0
    print("OK: %s steered the seedling" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_water_use_efficiency(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
WUE = {"C3": 2.0, "C4": 3.0, "CAM": 7.0}   # g biomass per kg water transpired
def water_for_kg(strategy):
    return 1000.0 / WUE[strategy]          # kg water per kg biomass
def main():
    for s in ("C3", "C4", "CAM"):
        print("  %-3s WUE %g g/kg -> %.0f kg water per kg of biomass" % (s, WUE[s], water_for_kg(s)))
    assert abs(water_for_kg("C3") - 500.0) < 1e-9
    assert abs(water_for_kg("C4") - 333.33) < 0.1
    assert abs(water_for_kg("CAM") - 142.86) < 0.1
    assert water_for_kg("CAM") < water_for_kg("C4") < water_for_kg("C3")
    print("OK: %s budgeted the water" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_mendel_chi_square(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def chi_square(observed, expected):
    return sum((o - e) ** 2 / e for o, e in zip(observed, expected))
def main():
    total = 1600
    expected = [9 / 16 * total, 3 / 16 * total, 3 / 16 * total, 1 / 16 * total]
    observed = [882, 313, 287, 118]
    print("dihybrid cross, n=%d: expected %s" % (total, [int(e) for e in expected]))
    print("observed %s" % observed)
    chi2 = chi_square(observed, expected)
    print("chi-square = %.4f (critical 7.815 at 3 df, 95 %%)" % chi2)
    assert abs(chi2 - 4.7267) < 0.01
    assert chi2 < 7.815, "deviation too big for chance"
    print("fits 9:3:3:1 — independent assortment holds")
    print("OK: %s tested Mendel's ratios" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nutrient_exchange(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    p_alone, boost = 10.0, 3.0            # mg phosphorus, mycorrhizal multiplier
    print("phosphorus uptake: %.0f mg alone -> %.0f mg with mycorrhizae" % (p_alone, p_alone * boost))
    assert p_alone * boost == 30.0
    n_fixed = 150.0                        # kg N / ha / year, good legume stand
    price_per_kg = 1.20                    # fertilizer nitrogen price
    value = n_fixed * price_per_kg
    print("legume fixes %.0f kg N/ha/yr ~ $%.0f/ha of free fertilizer" % (n_fixed, value))
    assert abs(value - 180.0) < 1e-9
    sugar_share = 0.12                     # plant pays ~12% of photosynthate
    print("the plant's payment: ~%.0f %% of its sugar to the fungal partner" % (100 * sugar_share))
    assert 0.04 <= sugar_share <= 0.20
    print("OK: %s settled the root trade" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_succession_richness(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def richness(t, K=120.0, r=0.08, t0=40.0):
    return K / (1 + math.exp(-r * (t - t0)))   # logistic rise of species count
def main():
    for t in (0, 20, 40, 80, 120):
        print("  year %3d -> %5.1f species" % (t, richness(t)))
    assert abs(richness(40) - 60.0) < 1e-9
    assert richness(0) < 6.0, "pioneers only at year 0"
    assert richness(120) > 115.0, "near climax by year 120"
    assert richness(20) < richness(40) < richness(80)
    print("pioneers facilitate, competitors sort, climax holds until disturbance resets")
    print("OK: %s watched the forest assemble" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_apg_clade_lookup(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
TREE = {
    "Amborellales": {"Amborellaceae": ["Amborella trichopoda"], "clade": "ANA grade"},
    "Nymphaeales": {"Nymphaeaceae": ["Nymphaea alba"], "clade": "ANA grade"},
    "Magnoliales": {"Magnoliaceae": ["Magnolia grandiflora"], "clade": "magnoliids"},
    "Poales": {"Poaceae": ["Triticum aestivum", "Zea mays"], "clade": "monocots"},
    "Asparagales": {"Orchidaceae": ["Phalaenopsis amabilis"], "clade": "monocots"},
    "Fagales": {"Fagaceae": ["Quercus alba"], "clade": "rosids (eudicots)"},
    "Fabales": {"Fabaceae": ["Pisum sativum"], "clade": "rosids (eudicots)"},
    "Asterales": {"Asteraceae": ["Helianthus annuus"], "clade": "asterids (eudicots)"},
    "Solanales": {"Solanaceae": ["Solanum tuberosum"], "clade": "asterids (eudicots)"},
}
def find(species):
    for order, fams in TREE.items():
        for fam, members in fams.items():
            if fam == "clade":
                continue
            if species in members:
                return order, fam, fams["clade"]
    return None
def main():
    for sp in ("Triticum aestivum", "Quercus alba", "Helianthus annuus", "Amborella trichopoda"):
        order, fam, clade = find(sp)
        print("  %-22s order %-13s family %-14s %s" % (sp, order, fam, clade))
    assert find("Triticum aestivum") == ("Poales", "Poaceae", "monocots")
    assert find("Quercus alba") == ("Fagales", "Fagaceae", "rosids (eudicots)")
    assert find("Amborella trichopoda")[2] == "ANA grade"
    assert find("not a plant") is None
    print("OK: %s climbed the APG IV tree" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_trap_economics(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def net_carbon(prey_count, cost_mg=50.0, mg_per_prey=30.0):
    # trap construction cost vs nitrogen payoff, in mg of carbon equivalent
    return prey_count * mg_per_prey - cost_mg
def main():
    for prey in (0, 1, 2, 3):
        net = net_carbon(prey)
        print("  %d prey/trap/season -> net %+.0f mg C (%s)" % (
            prey, net, "PROFITABLE" if net > 0 else "loss"))
    assert net_carbon(2) == 10.0
    assert net_carbon(1) < 0 < net_carbon(2)
    print("a trap must catch ~2+ prey to pay for itself — hence the two-touch rule")
    print("OK: %s balanced the trap budget" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_disease_triangle_epi(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def disease(host, pathogen, environment):
    return bool(host and pathogen and environment)   # the disease triangle
def severity(t, r=0.3, t0=20.0):
    return 1 / (1 + math.exp(-r * (t - t0)))         # logistic epidemic curve
def main():
    assert disease(True, True, True) is True
    assert disease(False, True, True) is False       # resistant host: no disease
    assert disease(True, False, True) is False       # clean seed: no disease
    assert disease(True, True, False) is False       # dry canopy: no disease
    print("disease triangle: remove any corner -> no epidemic")
    for t in (0, 20, 40):
        print("  day %2d -> severity %.1f %%" % (t, 100 * severity(t)))
    assert severity(0) < 0.01
    assert abs(severity(20) - 0.5) < 1e-9
    assert severity(40) > 0.99
    print("early spots look trivial until the exponential phase — scout early")
    print("OK: %s ran the epidemic" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_crop_calories(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def people_fed_per_ha(yield_t_ha, kcal_per_kg, kcal_per_person_day=2500.0):
    kcal = yield_t_ha * 1000.0 * kcal_per_kg
    return kcal / (kcal_per_person_day * 365.0)
def main():
    crops = [("wheat", 3.5, 3400), ("rice", 4.7, 3600), ("maize", 5.9, 3650),
             ("potato", 20.0, 770)]
    for cname, y, kcal in crops:
        print("  %-7s %4.1f t/ha -> feeds %.1f people/ha/yr" % (cname, y, people_fed_per_ha(y, kcal)))
    wheat = people_fed_per_ha(3.5, 3400)
    assert abs(wheat - 13.04) < 0.2
    assert people_fed_per_ha(5.9, 3650) > people_fed_per_ha(3.5, 3400)
    print("OK: %s fed the hectare" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_extraction_yield(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def doses(biomass_g, pct_active, dose_g):
    return biomass_g * (pct_active / 100.0) / dose_g
def main():
    d = doses(1000.0, 6.0, 0.6)           # 1 kg cinchona bark, 6% quinine, 0.6 g dose
    print("1 kg bark x 6 %% quinine / 0.6 g dose -> %.0f antimalarial doses" % d)
    assert abs(d - 100.0) < 1e-9
    d2 = doses(1000.0, 0.5, 0.01)          # 0.5% alkaloid, 10 mg dose
    print("1 kg dried leaf x 0.5 %% alkaloid / 10 mg dose -> %.0f doses" % d2)
    assert abs(d2 - 500.0) < 1e-6
    print("OK: %s ran the extraction math" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_water_potential(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def flows_to(psi_from, psi_to):
    return psi_from > psi_to              # water moves to more negative potential
def main():
    soil, leaf = -0.3, -0.5
    print("moist soil %.1f MPa, leaf %.1f MPa -> water flows to leaf: %s" % (soil, leaf, flows_to(soil, leaf)))
    assert flows_to(soil, leaf) is True
    dry_soil, stressed_leaf = -1.8, -1.2
    print("dry soil %.1f MPa, leaf %.1f MPa -> water flows to leaf: %s (uptake stops)" % (
        dry_soil, stressed_leaf, flows_to(dry_soil, stressed_leaf)))
    assert flows_to(dry_soil, stressed_leaf) is False
    # osmotic adjustment: accumulate solutes to lower leaf potential by 0.8 MPa
    adjusted = stressed_leaf - 0.8
    print("osmotic adjustment -> leaf %.1f MPa, flow restored: %s" % (adjusted, flows_to(dry_soil, adjusted)))
    assert flows_to(dry_soil, adjusted) is True
    print("OK: %s followed the water downhill" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_micropropagation_math(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    explants, shoots_per_cycle, cycles = 5, 4, 6
    plants = explants * shoots_per_cycle ** cycles
    print("%d explants x %d shoots/cycle for %d cycles -> %d plants" % (
        explants, shoots_per_cycle, cycles, plants))
    assert plants == 20480
    # one more cycle
    print("one more cycle -> %d plants" % (plants * shoots_per_cycle))
    assert plants * shoots_per_cycle == 81920
    # contamination check: 5% loss per cycle
    survivors = explants
    for _ in range(cycles):
        survivors = survivors * shoots_per_cycle * 0.95
    print("with 5 %% contamination loss per cycle: %.0f plants" % survivors)
    assert 14000 < survivors < 20480
    print("OK: %s cloned the crop" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_graft_compatibility(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def compatibility(scion, stock):
    # (species, genus, family) tuples
    if scion[0] == stock[0]:
        return "compatible"
    if scion[1] == stock[1]:
        return "compatible"
    if scion[2] == stock[2]:
        return "often compatible"
    return "incompatible"
def main():
    honeycrisp = ("Malus domestica", "Malus", "Rosaceae")
    crabapple = ("Malus sylvestris", "Malus", "Rosaceae")
    pear = ("Pyrus communis", "Pyrus", "Rosaceae")
    oak = ("Quercus alba", "Quercus", "Fagaceae")
    cases = [(honeycrisp, crabapple), (honeycrisp, pear), (honeycrisp, oak)]
    for scion, stock in cases:
        print("  %-16s on %-16s -> %s" % (scion[0], stock[0], compatibility(scion, stock)))
    assert compatibility(honeycrisp, crabapple) == "compatible"
    assert compatibility(honeycrisp, pear) == "often compatible"
    assert compatibility(honeycrisp, oak) == "incompatible"
    print("cambium must meet cambium, and kinship decides")
    print("OK: %s welded the graft" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ring_climate_corr(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def pearson(xs, ys):
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    den = math.sqrt(sum((x - mx) ** 2 for x in xs) * sum((y - my) ** 2 for y in ys))
    return num / den
def main():
    rainfall = [600, 400, 750, 300, 700]          # mm/yr
    widths = [1.2, 0.8, 1.5, 0.6, 1.4]            # mm ring width
    r = pearson(widths, rainfall)
    print("ring width vs rainfall: r = %.4f" % r)
    assert abs(r - 1.0) < 1e-9
    assert r > 0.6, "too weak for a cross-date"
    print("signature years (drought 300 mm -> 0.6 mm ring) anchor the chronology")
    print("OK: %s cross-dated the rings" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_canopy_tank_water(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def tank_volume_ml(radius_cm, depth_cm):
    return math.pi * radius_cm ** 2 * depth_cm   # 1 cm^3 = 1 mL
def main():
    v = tank_volume_ml(5.0, 10.0)
    print("bromeliad tank: r=5 cm, depth=10 cm -> %.1f mL impounded" % v)
    assert abs(v - 785.4) < 0.5
    # a frog nursery: 200 mL supports a tadpole pool
    pools = int(v // 200)
    print("that tank holds %d tadpole pools of 200 mL" % pools)
    assert pools == 3
    print("OK: %s filled the canopy tank" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_fossil_timeline(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
EVENTS = [
    (470, "first land plants (cryptospores)"),
    (425, "Cooksonia — first vascular plant"),
    (390, "first forests (progymnosperms)"),
    (360, "first seeds"),
    (300, "Carboniferous coal forests"),
    (140, "first angiosperms"),
    (66, "K-Pg asteroid: ~half of plant species lost"),
]
def main():
    for mya, what in EVENTS:
        print("  %3d mya  %s" % (mya, what))
    years = [e[0] for e in EVENTS]
    assert years == sorted(years, reverse=True), "timeline must run oldest-first"
    span = years[0] - years[-1]
    print("recorded plant history to the asteroid: %d million years" % span)
    assert span == 404
    assert len(EVENTS) == 7
    print("OK: %s walked deep time" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_breeders_equation(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def response(h2, S):
    return h2 * S                             # R = h^2 * S
def main():
    R = response(0.40, 10.0)
    print("heritability 0.40 x selection differential 10 units -> %.1f units gain/generation" % R)
    assert R == 4.0
    total = sum(response(0.40, 10.0) for _ in range(5))
    print("5 generations of steady selection -> %.0f units of gain" % total)
    assert total == 20.0
    # low heritability trait (yield itself): slow progress
    assert response(0.15, 10.0) < response(0.40, 10.0)
    print("high heritability + intense selection = fast gain")
    print("OK: %s predicted the selection response" % NAME)
if __name__ == "__main__":
    main()
''')

DEMOS = {
    "plant_diversity": demo_plant_diversity, "turgor_pressure": demo_turgor_pressure,
    "root_surface": demo_root_surface, "internode_growth": demo_internode_growth,
    "leaf_area_index": demo_leaf_area_index, "photon_energy": demo_photon_energy,
    "calvin_stoichiometry": demo_calvin_stoichiometry,
    "transpiration_rate": demo_transpiration_rate,
    "life_cycle_table": demo_life_cycle_table, "alternation_table": demo_alternation_table,
    "moss_water": demo_moss_water, "spore_counts": demo_spore_counts,
    "cone_seeds": demo_cone_seeds, "flower_parts": demo_flower_parts,
    "angiosperm_share": demo_angiosperm_share, "pollination_matrix": demo_pollination_matrix,
    "dispersal_range": demo_dispersal_range, "germination_test": demo_germination_test,
    "auxin_dose_response": demo_auxin_dose_response,
    "phototropism_angle": demo_phototropism_angle,
    "water_use_efficiency": demo_water_use_efficiency,
    "mendel_chi_square": demo_mendel_chi_square,
    "nutrient_exchange": demo_nutrient_exchange,
    "succession_richness": demo_succession_richness,
    "apg_clade_lookup": demo_apg_clade_lookup, "trap_economics": demo_trap_economics,
    "disease_triangle_epi": demo_disease_triangle_epi, "crop_calories": demo_crop_calories,
    "extraction_yield": demo_extraction_yield, "water_potential": demo_water_potential,
    "micropropagation_math": demo_micropropagation_math,
    "graft_compatibility": demo_graft_compatibility,
    "ring_climate_corr": demo_ring_climate_corr,
    "canopy_tank_water": demo_canopy_tank_water, "fossil_timeline": demo_fossil_timeline,
    "breeders_equation": demo_breeders_equation,
}

# ---------------------------------------------------------------- records

def build_records(slug, source):
    cfg = DBCFG[slug]
    sig = source == "signature"
    # Teaching-ladder order: stable sort by ladder_rank (entries are already
    # in ladder order in entries_botany.py).
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
    for slug in ("botany", "botany-signature"):
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
        # Exhaustive pill + red All Database Merger button ride along in the template
        assert 'id="qex"' in page and 'id="qmerge"' in page, "merger pattern missing in %s" % slug
        # tab-handler guard (1,470-page canon)
        assert "if(!t.dataset.p)return" in page, "tab guard missing in %s" % slug
        ddir = os.path.join(REPO, "db", slug)
        os.makedirs(ddir, exist_ok=True)
        ppath = os.path.join(ddir, "index.html")
        with open(ppath, "w", encoding="utf-8") as f:
            f.write(page)
        changed, notes = sweep.process_page(ppath)
        topics = {}
        for r in recs:
            topics.setdefault(r["g"], []).append("%s — %s" % (r["t"], r["g"]))
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
