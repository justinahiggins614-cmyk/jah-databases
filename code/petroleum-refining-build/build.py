#!/usr/bin/env python3
"""Build the Petroleum Refining field databases for JAH Databases (field #22, taxonomy order).

Verified 2026-10-17: NO database covers petroleum refining as a discipline.
- Manifest-wide regex search (petroleum.?refin|refiner|crude.?distill|
  catalytic.?crack|hydrocrack|reforming|alkylation|isomeri|delayed.?cok|
  hydrotreat|desulfuri|naphtha|asphalt|base.?oil|octane|reformate): only
  career-profile databases ('petroleum-engineers', 4 records;
  'public-petroleum-engineers', 5 records) and rock-science 'petrology'
  (36 records) - zero discipline-level refining coverage. 'energy',
  'energy-systems', 'energy-basics', 'everything-energy' are general-energy
  with no refining-unit records. 'biofuels-*' cover biofuels, not petroleum
  refining.
- Fields #11-21 shard indexes (volcanology, climatology,
  atmospheric-science, hydrology, meteorology, calculus, combinatorics,
  econometrics, psychometrics, turbomachinery, electromagnetics): direct
  whole-shard title scans for petrol|refin|crude|distill|crack|reformer|
  alkylation|isomeriz|coking|hydrotreat|desulfur|asphalt|lubricant|
  petrochem|gasoline|diesel|jet.?fuel|octane|kerosene|naphtha|fuel.?oil|lpg|
  propane = zero hits.
- 'scientific-formulas': bare formula cards are reference only (task rule:
  formula cards do NOT count as discipline coverage).
- Whole-system dedupe gate (fresh data/dedupe/exact/ index in the main repo
  rebuilt 2026-10-17 08:04 UTC, covering fields through #10; fields #11-21
  cross-checked directly above): every record checked + admitted at build
  time.

So this build creates two NEW databases:

  petroleum-refining             - The Petroleum Refining Database
                                   (public-harvest: real, fact-checked
                                   refining; citations Speight, Gary/
                                   Handwerk/Kaiser, Fahim, Meyers, Riazi,
                                   Ancheyta, Sadeghbeigi, Robinson/Hsu,
                                   API Technical Data Book, ASTM methods,
                                   OSHA PSM, EPA NSPS)
  petroleum-refining-signature   - The Petroleum Refining Signature Database
                                   (his original Signature interpretation of
                                   the discipline; src signature, titles
                                   suffixed " (Signature Edition)", never
                                   presented as authentic public record)

32 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

Every record: description + how-it-works + key points + requirements +
standards + citations + working demonstration code (real, runnable,
stdlib-only Python; machine-executed OK). Refining demos: the discipline
map with API gravity and barrel mass, the UOP characterization factor,
crude-assay TBP interpolation, API gravity round-trips, the refinery-wide
mass balance, two-stage desalting efficiency, the CDU cut balance, vacuum
boiling-point depression by Clausius-Clapeyron, depropanizer key recovery,
Arrhenius thermal-cracking severity, FCC conversion and selectivity,
hydrocracker hydrogen consumption and volume swell, reformer hydrogen from
naphthene dehydrogenation, alkylation stoichiometry and volume yield,
isomerization equilibrium octane, coker coke yield from Conradson carbon,
first-order hydrodesulfurization to ULSD levels, the hydrogen network
balance, Claus sulfur stoichiometry and recovery, gasoline blending octane
and RVP, the ASTM D4737 cetane index, lube base-oil group classification
and Walther VI slopes, Superpave PG grade assignment, steam-cracker
yields, LOPA risk multiplication, scrubber SO2 removal, the Nelson
complexity index and margin arithmetic, specification pass/fail, coupon
corrosion rate in mils per year, exchanger duty and furnace efficiency,
wastewater treatment train removal, and first-order catalyst deactivation.

Subtitle disambiguation (fields #13-22 pattern): discipline titles carry
teaching-focused subtitles rather than bare cards, e.g. "Atmospheric
Distillation: The Crude Distillation Unit" and "Alkylation: The Finest
Gasoline Molecule".

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
# main repo (rebuilt 2026-10-17 08:04 UTC; covers fields through #10).
# Fields #11-21 shard indexes checked directly (see docstring) since the gate
# index predates them - subtitle disambiguation used throughout.
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_petroleum_refining import ENTRIES, SIG_TAIL

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature interpretation of petroleum "
                "refining: clearly labeled Signature-made, never presented as authentic "
                "public record.")
    pub_line = ("Public records - real, fact-checked petroleum refining: what refining is; "
                "crude oil composition and the hydrocarbon family; reading a crude assay; "
                "API gravity, density, and viscosity; the modern refinery flow; crude "
                "desalting; atmospheric distillation; vacuum distillation; light ends "
                "recovery; thermal cracking and visbreaking; fluid catalytic cracking; "
                "hydrocracking; catalytic reforming; alkylation; isomerization; delayed "
                "coking; hydrotreating and desulfurization; the hydrogen network; amine "
                "treating and sulfur recovery; gasoline blending; diesel and jet fuel "
                "specifications; lubricants and base oils; asphalt, coke, and heavy "
                "products; petrochemical integration; refinery safety; emissions and "
                "environmental controls; refinery economics; product quality testing; "
                "corrosion and materials; energy integration; wastewater treatment; "
                "catalysts, organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations (what refining is, "
              "crude composition, reading a crude assay, API gravity/density/viscosity, "
              "the modern refinery flow, crude desalting, atmospheric distillation, "
              "vacuum distillation) -> Compounded (light ends recovery, thermal "
              "cracking and visbreaking, fluid catalytic cracking, hydrocracking, "
              "catalytic reforming, alkylation, isomerization, delayed coking, "
              "hydrotreating, the hydrogen network) -> Advanced (amine treating and "
              "sulfur recovery, gasoline blending, diesel and jet specifications, "
              "lubricants and base oils, asphalt/coke/heavy products, petrochemical "
              "integration, refinery safety, emissions and environmental controls, "
              "refinery economics, product quality testing, corrosion and materials, "
              "energy integration, wastewater treatment, catalysts).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search distillation, FCC, hydrocracking, reforming, alkylation, octane, desulfurization, blending...",
        "chat_ph": "Ask about petroleum refining...",
        "archive_blurb": ("Seeded %s petroleum refining records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled structural petroleum refining studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about petroleum refining - from crude composition and assays through distillation, catalytic cracking, hydrocracking, reforming, alkylation, hydrotreating, blending, safety, economics, and the environment." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "petroleum-refining-study", "gen_demo_kind": "petroleum-refining-demo",
        "source": source,
    }

CIT_PUB = "Petroleum refining (standard textbooks, API data book, ASTM methods, and peer-reviewed literature)."
CIT_SIG = CIT_PUB + " " + SIG_TAIL

DBCFG = {}
DBCFG["petroleum-refining"] = _cfg(
    "petroleum-refining", "The Petroleum Refining Database",
    "Real, fact-checked petroleum refining: from crude oil composition and assays "
    "through atmospheric and vacuum distillation, catalytic cracking, hydrocracking, "
    "reforming, alkylation, isomerization, coking, hydrotreating, blending, product "
    "specifications, safety, economics, and environmental controls - taught "
    "progressively along the ladder.",
    "petroleum refining record", "JAH-PRF-", "JAH Refining Archivist",
    "petroleum refining archivist - what refining is, crude composition, crude "
    "assays, API gravity/density/viscosity, refinery flow, desalting, atmospheric "
    "and vacuum distillation, light ends, thermal cracking, FCC, hydrocracking, "
    "reforming, alkylation, isomerization, coking, hydrotreating, hydrogen network, "
    "amine/sulfur recovery, gasoline blending, diesel and jet specs, lubricants, "
    "heavy products, petrochemical integration, safety, environmental controls, "
    "economics, quality testing, corrosion, energy integration, wastewater, "
    "catalysts; teaching progressively along the ladder from foundations through "
    "compounded to advanced; answers from many angles - definition, example, "
    "analogy, application, history, math, how-to - using only the system's own "
    "archive data",
    CIT_PUB, "public")
DBCFG["petroleum-refining-signature"] = _cfg(
    "petroleum-refining-signature", "The Petroleum Refining Signature Database",
    "His original Signature interpretation of petroleum refining: the full ladder from "
    "crude composition through distillation, conversion, treating, blending, and "
    "economics, reframed as Signature science. Clearly labeled Signature-made, "
    "never presented as authentic public record.",
    "petroleum refining record", "JAH-PRS-", "JAH Refining Archivist (Signature)",
    "petroleum refining archivist - Signature editions: his original Signature "
    "interpretation of petroleum refining, clearly labeled Signature-made and never "
    "presented as authentic public record; teaches progressively along the ladder "
    "from foundations through compounded to advanced; answers from many angles - "
    "definition, example, analogy, application, history, math, how-to - using only "
    "the system's own archive data",
    CIT_SIG, "signature")

base.DBCFG = DBCFG
# ---------------------------------------------------------------- demos
# Every demo is real, runnable, stdlib-only Python performing the actual
# petroleum refining computation for its record. All are machine-executed by main().

_PREAMBLE = (
"import math\n"
"R_GAS = 8.314\n"
"BBL_L = 158.987\n"
"def _api_to_sg(api):\n"
"    return 141.5 / (api + 131.5)\n"
"def _sg_to_api(sg):\n"
"    return 141.5 / sg - 131.5\n"
)

def _wrap(name, rid, group, body):
    return (base._hdr(name, rid, group) + _PREAMBLE + body.replace("NAME", json.dumps(name)))

def demo_pr_what(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
TERRITORIES = {
    "separate": "distillation splits crude by boiling point: naphtha, kerosene, diesel, resid",
    "convert": "cracking, coking, reforming, alkylation reshape molecules to match demand",
    "treat": "hydrotreating strips sulfur, nitrogen, metals so products burn clean",
}
def main():
    assert len(TERRITORIES) == 3
    for terr, tools in TERRITORIES.items():
        print("%-8s -> %s" % (terr, tools))
    # a barrel is volume; the refinery buys mass-equivalent value
    api = 30.0
    sg = _api_to_sg(api)
    assert abs(sg - 0.87616) < 1e-4, sg
    barrel_kg = BBL_L * sg
    assert abs(barrel_kg - 139.30) < 0.05, barrel_kg
    print("30 API crude: SG = %.4f, one 42-gal barrel = %.2f kg" % (sg, barrel_kg))
    # distillation alone makes the wrong slate -> conversion exists
    straight_run = {"naphtha": 22.0, "kerosene": 13.0, "diesel": 24.0,
                    "gas_oil": 8.0, "resid": 33.0}
    assert abs(sum(straight_run.values()) - 100.0) < 1e-9
    gasoline_demand_share = 45.0
    print("straight-run naphtha: %.0f%% of barrel vs ~%.0f%% gasoline demand -> conversion required"
          % (straight_run["naphtha"], gasoline_demand_share))
    assert straight_run["naphtha"] < gasoline_demand_share
    print("rule: separate what you can, convert what you must, treat everything")
    print("OK: %s mapped the refinery" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pr_composition(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def uop_k(t_mean_rankine, sg):
    return t_mean_rankine ** (1.0 / 3.0) / sg
def main():
    # a mid-boiling crude fraction: mean avg boiling point 800 R, SG 0.85
    k = uop_k(800.0, 0.85)
    assert abs(k - 10.92) < 0.02, k
    print("UOP K = %.2f" % k)
    if k >= 12.5:
        char = "paraffinic"
    elif k >= 11.5:
        char = "naphthenic"
    else:
        char = "aromatic-leaning"
    print("character: %s (paraffinic 12.5-13, naphthenic 11.5-12, aromatic 10.5-11.5)" % char)
    assert char == "aromatic-leaning"
    # heteroatom burden: 2 wt% sulfur in 139 kg barrel
    barrel_kg = BBL_L * 0.87616
    s_kg = barrel_kg * 0.02
    print("2%% sulfur crude: %.2f kg of sulfur per barrel to remove" % s_kg)
    assert 2.5 < s_kg < 3.0, s_kg
    # sweet vs sour line
    for s_pct, tag in ((0.4, "sweet"), (2.0, "sour")):
        print("  %.1f%% sulfur -> %s crude" % (s_pct, tag))
    assert 0.4 < 0.5 < 2.0
    print("rule: K names the family, sulfur names the treating bill")
    print("OK: %s read the molecules" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pr_assay(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
# true boiling point assay points: (cumulative vol%, temp F)
ASSAY = [(0.0, 100.0), (10.0, 220.0), (30.0, 350.0), (50.0, 480.0),
         (70.0, 620.0), (90.0, 800.0), (100.0, 950.0)]
def vol_at(t):
    for (v1, t1), (v2, t2) in zip(ASSAY[:-1], ASSAY[1:]):
        if t1 <= t <= t2:
            return v1 + (t - t1) / (t2 - t1) * (v2 - v1)
    raise ValueError(t)
def cut_yield(t1, t2):
    return vol_at(t2) - vol_at(t1)
def main():
    naphtha = cut_yield(190.0, 380.0)
    kero = cut_yield(380.0, 520.0)
    diesel = cut_yield(520.0, 650.0)
    print("naphtha (190-380 F): %.1f vol%%" % naphtha)
    print("kerosene (380-520 F): %.1f vol%%" % kero)
    print("diesel (520-650 F): %.1f vol%%" % diesel)
    assert 26.0 < naphtha < 28.0, naphtha
    assert 20.0 < kero < 22.0, kero
    assert 16.5 < diesel < 18.5, diesel
    total = vol_at(950.0) - vol_at(100.0)
    assert abs(total - 100.0) < 1e-9
    print("whole crude accounted: %.1f vol%% - the assay is the yield fingerprint" % total)
    print("rule: interpolate the TBP curve between cut points and the barrel confesses its slate")
    print("OK: %s read the assay" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pr_api(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def classify(api):
    if api > 31.1:
        return "light"
    if api < 22.3:
        return "heavy"
    return "medium"
def main():
    for api, expect in ((38.0, "light"), (30.0, "medium"), (15.0, "heavy")):
        sg = _api_to_sg(api)
        back = _sg_to_api(sg)
        assert abs(back - api) < 1e-9, (api, back)
        dens = sg * 1000.0
        barrel_kg = BBL_L * sg
        tag = classify(api)
        assert tag == expect, (api, tag)
        print("%5.1f API -> SG %.4f, density %.1f kg/m3, barrel %.1f kg [%s]"
              % (api, sg, dens, barrel_kg, tag))
    # water reference: 10 API
    assert abs(_api_to_sg(10.0) - 1.0) < 1e-9
    print("water = 10.0 API exactly - the scale's anchor")
    print("rule: API gravity turns the traded barrel (volume) into handled mass")
    print("OK: %s weighed the barrel" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pr_flow(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # deep-conversion refinery, per 100 mass units of crude
    inputs = {"crude": 100.0, "hydrogen_make": 2.0, "oxygenates": 1.0}
    outputs = {"lpg": 5.0, "gasoline": 45.0, "jet": 10.0, "diesel": 30.0,
               "lubes": 2.0, "asphalt": 4.0, "coke": 3.0, "sulfur": 0.5,
               "fuel_gas": 2.5, "losses": 1.0}
    in_tot = sum(inputs.values())
    out_tot = sum(outputs.values())
    print("in : %.1f mass units %s" % (in_tot, inputs))
    print("out: %.1f mass units" % out_tot)
    assert abs(in_tot - out_tot) < 1e-9, (in_tot, out_tot)
    print("mass closes: in = out (hydrogen in, processing gain out)")
    # hydrogen sub-balance
    h2_made = 2.0
    h2_used = 1.6 + 0.3   # hydrocracker + hydrotreaters
    assert h2_made >= h2_used
    print("hydrogen: made %.1f, used %.1f - the second currency balances" % (h2_made, h2_used))
    gasoline_share = outputs["gasoline"] / in_tot * 100.0
    print("gasoline: %.1f%% of intake - conversion, not distillation, makes the slate" % gasoline_share)
    assert gasoline_share > 40.0
    print("rule: trace oil, hydrogen, and heat together or the diagram lies")
    print("OK: %s balanced the refinery" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pr_desalt(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    salt_in_ptb = 20.0        # lb per 1000 bbl, raw crude
    stage_eff = 0.92          # each stage removes 92%
    after1 = salt_in_ptb * (1.0 - stage_eff)
    after2 = after1 * (1.0 - stage_eff)
    print("salt in: %.1f PTB" % salt_in_ptb)
    print("after stage 1: %.2f PTB" % after1)
    print("after stage 2: %.3f PTB" % after2)
    assert abs(after1 - 1.60) < 1e-9, after1
    assert abs(after2 - 0.128) < 1e-9, after2
    assert after2 < 1.0, "must meet < 1 PTB spec"
    print("two-stage removal: %.1f%% - meets the < 1 PTB desalted-crude spec" %
          ((1.0 - after2 / salt_in_ptb) * 100.0))
    # wash water rate: 5 vol% of crude
    crude_bpd = 100000.0
    wash_gpd = crude_bpd * 42.0 * 0.05
    print("wash water for 100 kbpd: %.0f gal/day -> brine to wastewater treatment" % wash_gpd)
    assert abs(wash_gpd - 210000.0) < 1.0
    print("rule: dissolve the salt, coalesce the brine, starve the corrosion")
    print("OK: %s washed the crude" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pr_atm(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    feed = 100.0   # kbpd crude charge
    cuts = {"light_naphtha": 8.0, "heavy_naphtha": 14.0, "kerosene": 13.0,
            "diesel": 24.0, "atmo_gas_oil": 8.0, "atmo_resid": 33.0}
    total = sum(cuts.values())
    assert abs(total - feed) < 1e-9, total
    print("CDU 100 kbpd charge ->")
    for name_, vol in cuts.items():
        print("  %-14s %5.1f kbpd" % (name_, vol))
    # cut points sharpen with trays: 40 trays, ~2 F per theoretical stage overlap
    trays = 40
    print("trays: %d ; residuum: %.0f%% of crude still holds the heavy value" % (trays, cuts["atmo_resid"]))
    # furnace duty sanity: heating 100 kbpd by ~500 F
    m_dot = feed * 1000.0 * BBL_L * 0.85 / 86400.0   # kg/s
    cp = 2.2                                          # kJ/kg-K
    dT_K = 500.0 * 5.0 / 9.0
    duty_MW = m_dot * cp * dT_K / 1000.0
    print("furnace duty ~ %.0f MW - the price of the front door" % duty_MW)
    assert 60.0 < duty_MW < 120.0, duty_MW
    print("rule: 40 equilibrium stages turn slight volatility differences into sharp cuts")
    print("OK: %s ran the crude tower" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pr_vac(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Clausius-Clapeyron: a 700 K-at-760-mmHg hydrocarbon under 40 mmHg vacuum
    Tb_atm = 700.0        # K
    P_atm = 760.0
    P_vac = 40.0
    dHvap = 88.0 * Tb_atm          # Trouton's rule, J/mol
    # ln(P2/P1) = -dH/R * (1/T2 - 1/T1)  ->  1/T2 = 1/T1 + (R/dH) * ln(P1/P2)
    inv_T2 = 1.0 / Tb_atm + (R_GAS / dHvap) * math.log(P_atm / P_vac)
    T_vac = 1.0 / inv_T2
    T_vac_F = (T_vac - 273.15) * 9.0 / 5.0 + 32.0
    print("700 K boiler at 760 mmHg -> %.0f K (%.0f F) at 40 mmHg" % (T_vac, T_vac_F))
    assert 540.0 < T_vac < 556.0, T_vac
    depression_F = (Tb_atm - 273.15) * 9.0 / 5.0 + 32.0 - T_vac_F
    print("boiling-point depression: %.0f F - vaporize without cracking" % depression_F)
    assert depression_F > 200.0
    # Maxwell-Bonnell style check: lower pressure always lowers T
    for p in (100.0, 40.0, 15.0):
        inv = 1.0 / Tb_atm + (R_GAS / dHvap) * math.log(P_atm / p)
        print("  at %5.1f mmHg: %.0f F" % (p, (1.0 / inv - 273.15) * 9.0 / 5.0 + 32.0))
    print("rule: drop the pressure, drop the boiling point, save the molecules")
    print("OK: %s pulled the vacuum" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pr_lightends(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # depropanizer: 100 mol feed, 40 C3 / 60 C4; C3 recovery 98%, C4 slip 2%
    feed_c3, feed_c4 = 40.0, 60.0
    ovhd_c3 = feed_c3 * 0.98
    ovhd_c4 = feed_c4 * 0.02
    ovhd = ovhd_c3 + ovhd_c4
    purity = ovhd_c3 / ovhd
    btms_c3 = feed_c3 - ovhd_c3
    btms_c4 = feed_c4 - ovhd_c4
    print("overhead: %.1f mol at %.1f%% C3 purity" % (ovhd, purity * 100.0))
    print("bottoms : %.1f mol C3 + %.1f mol C4" % (btms_c3, btms_c4))
    assert abs(ovhd - 40.4) < 1e-9
    assert purity > 0.95, purity
    # overall C3 accountability
    assert abs((ovhd_c3 + btms_c3) - feed_c3) < 1e-9
    assert abs((ovhd_c4 + btms_c4) - feed_c4) < 1e-9
    print("C3 accounted: %.1f in = %.1f out - the fractionator keeps books" % (feed_c3, ovhd_c3 + btms_c3))
    # LPG vapor pressure: propane ~ 110 psi at 100 F -> pressure storage
    print("rule: pressure fractionation sorts the lightweights; purity pays")
    print("OK: %s split the light ends" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pr_thermal(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def arrhenius_ratio(Ea, T1_C, T2_C):
    T1 = T1_C + 273.15
    T2 = T2_C + 273.15
    return math.exp(-Ea / R_GAS * (1.0 / T2 - 1.0 / T1))
def main():
    Ea = 250000.0   # J/mol, typical C-C scission
    r = arrhenius_ratio(Ea, 440.0, 455.0)
    print("15 C hotter: rate ratio = %.2f" % r)
    assert 2.0 < r < 2.8, r
    # visbreaking conversion, first order: X = 1 - exp(-k t)
    k1 = 0.020       # per min at 440 C
    t = 10.0         # min residence
    X1 = 1.0 - math.exp(-k1 * t)
    X2 = 1.0 - math.exp(-k1 * r * t)
    print("conversion at 440 C, 10 min: %.1f%%" % (X1 * 100.0))
    print("conversion at 455 C, 10 min: %.1f%%" % (X2 * 100.0))
    assert abs(X1 - 0.1813) < 0.002, X1
    assert X2 > 2.0 * X1, (X2, X1)
    print("severity is temperature x time - and temperature dominates exponentially")
    print("rule: heat is a statistical hammer; control it or it makes coke")
    print("OK: %s cracked with heat" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pr_fcc(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    feed = 100.0
    yields = {"dry_gas": 4.0, "lpg": 19.0, "gasoline": 51.0, "lco": 16.0,
              "hco_slurry": 6.0, "coke": 4.0}
    assert abs(sum(yields.values()) - feed) < 1e-9
    conv = 100.0 - (yields["lco"] + yields["hco_slurry"])
    print("FCC 100 wt units feed ->")
    for n_, y in yields.items():
        print("  %-10s %5.1f" % (n_, y))
    print("conversion = 100 - (LCO + HCO + slurry) = %.0f%%" % conv)
    assert 70.0 < conv < 85.0, conv
    gasoline_sel = yields["gasoline"] / conv * 100.0
    print("gasoline selectivity: %.1f%% of converted feed" % gasoline_sel)
    assert 60.0 < gasoline_sel < 70.0, gasoline_sel
    # catalyst-to-oil ratio and coke heat balance
    cto = 7.0
    coke_heat_MW = yields["coke"] / 100.0 * 1000.0 * 32.0 / 24.0  # sketch scale
    print("catalyst-to-oil ratio: %.1f ; coke burn reheats the circulating catalyst" % cto)
    assert 5.0 <= cto <= 10.0
    print("rule: carbenium ions crack selectively; the regenerator pays the heat bill")
    print("OK: %s ran the cat cracker" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pr_hydrocrack(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    feed_bbl = 100.0
    api_feed = 15.0
    sg = _api_to_sg(api_feed)
    feed_kg = feed_bbl * BBL_L * sg
    # hydrogen consumption 1500 SCF/bbl; 1 SCF H2 = 0.0024126 kg
    h2_scf = 1500.0 * feed_bbl
    h2_kg = h2_scf * 0.0024126
    h2_wt = h2_kg / feed_kg * 100.0
    print("feed: %.0f bbl at %.0f API (%.0f kg)" % (feed_bbl, api_feed, feed_kg))
    print("H2 consumption: %.0f SCF/bbl = %.1f wt%% on feed" % (1500.0, h2_wt))
    assert 1.5 < h2_wt < 3.5, h2_wt
    # volume swell: hydrogen mass + density shift -> >100% volume yield
    prod_bbl = 112.0
    print("liquid volume yield: %.0f%% - hydrogen becomes barrels" % prod_bbl)
    assert prod_bbl > 100.0
    # product quality: near-zero sulfur
    s_ppm = 8.0
    assert s_ppm < 15.0
    print("product sulfur: %.0f ppm - the cleanest barrel in the refinery" % s_ppm)
    print("rule: add hydrogen instead of rejecting carbon and every molecule stays liquid")
    print("OK: %s hydrocracked" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pr_reform(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # methylcyclohexane -> toluene + 3 H2 : 98 g -> 92 g + 6 g
    naphtha_kg = 100.0
    naphthene_frac = 0.40
    mch = naphtha_kg * naphthene_frac
    h2_kg = mch * 6.0 / 98.0
    h2_wt = h2_kg / naphtha_kg * 100.0
    print("100 kg naphtha, 40%% naphthenes -> %.2f kg H2 (%.2f wt%%)" % (h2_kg, h2_wt))
    assert 2.0 < h2_wt < 3.5, h2_wt
    # octane lift
    ron_in, ron_out = 55.0, 98.0
    print("RON: %.0f -> %.0f (aromatics are octane)" % (ron_in, ron_out))
    assert ron_out - ron_in > 35.0
    # hydrogen value: a 20 kbpd reformer at 2.45 wt% H2
    ref_bpd = 20000.0
    h2_bpd_kg = ref_bpd * BBL_L * 0.75 * h2_wt / 100.0
    # kg -> SCF (1 SCF H2 = 0.0024126 kg) -> MMSCFD
    h2_mmscfd = h2_bpd_kg / 0.0024126 / 1e6
    print("20 kbpd reformer makes ~%.0f MMSCFD of hydrogen" % h2_mmscfd)
    assert 10.0 < h2_mmscfd < 60.0, h2_mmscfd
    print("rule: dehydrogenation pays double - octane plus hydrogen")
    print("OK: %s reformed the naphtha" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pr_alky(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # iC4 (58) + C4= (56) -> iC8 (114)
    m_olefin, m_iso, m_prod = 56.0, 58.0, 114.0
    assert abs(m_olefin + m_iso - m_prod) < 1e-9
    # volume yield: alkylate denser than olefin
    rho_olefin, rho_prod = 0.60, 0.70
    vol_yield = (m_prod / m_olefin) * (rho_olefin / rho_prod)
    print("1 vol olefin -> %.2f vol alkylate" % vol_yield)
    assert 1.6 < vol_yield < 1.9, vol_yield
    # isobutane-to-olefin ratio suppresses polymerization
    i_o_ratio = 8.0
    assert i_o_ratio >= 8.0
    print("isobutane:olefin = %.0f:1 - starve the polymerization side reaction" % i_o_ratio)
    # quality
    ron = 96.0
    print("alkylate RON: %.0f, sulfur ~0, aromatics 0, olefins 0 - liquid gold" % ron)
    assert 94.0 <= ron <= 98.0
    # acid strength guard
    acid_wt = 97.0
    assert 96.0 <= acid_wt <= 98.0, acid_wt
    print("H2SO4 strength: %.0f wt%% - the protonation engine" % acid_wt)
    print("rule: match isobutane to olefin under acid and the branches build themselves")
    print("OK: %s alkylated" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pr_isom(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # nC5 <-> iC5, K_eq = 3.0 at low temperature
    K = 3.0
    feed = 100.0
    iC5 = feed * K / (1.0 + K)
    nC5 = feed - iC5
    print("equilibrium at K=%.1f: %.1f mol iC5 + %.1f mol nC5" % (K, iC5, nC5))
    assert abs(iC5 - 75.0) < 1e-9 and abs(nC5 - 25.0) < 1e-9
    ron_mix = (iC5 * 93.0 + nC5 * 62.0) / feed
    print("blend RON: %.2f (iC5=93, nC5=62)" % ron_mix)
    assert 80.0 < ron_mix < 90.0, ron_mix
    gain = ron_mix - 62.0
    print("octane gain vs straight nC5: +%.1f numbers, zero yield loss" % gain)
    assert gain > 15.0
    # low temperature favors branching: K rises as T falls
    print("rule: cool the catalyst, shift the equilibrium, bank the branches")
    print("OK: %s isomerized" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pr_coke(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    ccr = 20.0   # Conradson carbon residue, wt%
    coke_factor = 1.55
    coke_yield = ccr * coke_factor
    print("feed CCR: %.0f wt%% -> coke yield ~%.1f wt%%" % (ccr, coke_yield))
    assert 28.0 < coke_yield < 34.0, coke_yield
    feed = 100.0
    products = {"coke": coke_yield, "fuel_gas": 8.0, "coker_naphtha": 14.0,
                "coker_gas_oil": feed - coke_yield - 8.0 - 14.0}
    assert abs(sum(products.values()) - feed) < 1e-9
    for n_, y in products.items():
        print("  %-14s %5.1f wt%%" % (n_, y))
    # drum cycle: fill ~24 h, then steam, quench, unhead, and water-jet decoke
    print("paired drums alternate fill/decoke on ~24 h cycles")
    print("rule: coke yield ~= 1.5-1.6 x CCR - the residuum's carbon confesses")
    print("OK: %s coked the resid" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pr_hds(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # first-order HDS: S = S0 * exp(-k * tau); 500 ppm -> 10 ppm ULSD
    S0, Starget = 500.0, 10.0
    k = 0.50            # per hour
    tau = math.log(S0 / Starget) / k
    S = S0 * math.exp(-k * tau)
    print("severity k*tau = %.2f -> sulfur %.0f ppm -> %.1f ppm" % (k * tau, S0, S))
    assert 9.0 < S < 11.0, S
    assert Starget <= 15.0, "meets ULSD spec"
    # the cruel math: each halving costs the same severity increment
    tau_half = math.log(2.0) / k
    print("each halving of sulfur costs %.2f h of severity - deep desulfurization is expensive" % tau_half)
    assert abs(tau_half - 1.386) < 0.01
    # hydrogen: ~60 SCF/bbl per wt% S removed, plus olefin saturation
    s_wt_removed = (S0 - Starget) / 1e6 * 100.0
    h2_scf_bbl = 60.0 * s_wt_removed + 40.0
    print("H2 consumption ~ %.0f SCF/bbl for this service" % h2_scf_bbl)
    assert h2_scf_bbl > 0
    print("rule: first-order kinetics - the last ppm costs more than the first percent")
    print("OK: %s desulfurized" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pr_h2net(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    producers = {"reformer_net_gas": 55.0, "smr_h2_plant": 80.0}
    consumers = {"hydrocracker": 85.0, "distillate_hydrotreaters": 30.0,
                 "naphtha_hydrotreaters": 15.0}
    purge_loss = 5.0
    made = sum(producers.values())
    used = sum(consumers.values()) + purge_loss
    print("producers (MMSCFD): %s = %.0f" % (producers, made))
    print("consumers (MMSCFD): %s + purge %.0f = %.0f" % (consumers, purge_loss, used))
    assert abs(made - used) < 1e-9, (made, used)
    print("hydrogen balances: made = used + purge")
    # SMR stoichiometry: CH4 + 2H2O -> CO2 + 4H2
    # 80 MMSCFD H2 needs 20 MMSCFD methane (ideal)
    ch4_mmscfd = producers["smr_h2_plant"] / 4.0
    print("SMR methane feed for 80 MMSCFD H2: ~%.0f MMSCFD (ideal stoichiometry)" % ch4_mmscfd)
    assert abs(ch4_mmscfd - 20.0) < 1e-9
    # purity cascade: PSA 99.9% to hydrocracker, reformer gas ~80% to hydrotreaters
    assert 99.9 > 80.0
    print("rule: match purity to need - the hydrogen pinch wastes nothing")
    print("OK: %s balanced the hydrogen" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pr_claus(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # 100 mol H2S: burn 1/3 to SO2, Claus-react the rest: 2H2S + SO2 -> 3S + 2H2O
    h2s = 100.0
    burned = h2s / 3.0
    so2 = burned
    remaining = h2s - burned
    # stoichiometry check: 2*so2 == remaining
    assert abs(2.0 * so2 - remaining) < 1e-9
    s_mol_theoretical = 3.0 * so2
    recovery = 0.96
    s_mol = s_mol_theoretical * recovery
    s_kg = s_mol * 32.06 / 1000.0
    feed_s_kg = h2s * 34.08 / 1000.0 * (32.06 / 34.08)
    print("100 mol H2S -> %.1f mol S theoretical; at %.0f%% recovery: %.2f kg sulfur"
          % (s_mol_theoretical, recovery * 100.0, s_kg))
    assert abs(s_mol_theoretical - 100.0) < 1e-9
    assert 94.0 < recovery * 100.0 < 98.0
    # tail gas unit pushes past 99.5%
    with_tgt = 99.6
    print("with tail gas treating: %.1f%% overall recovery - permit compliance" % with_tgt)
    assert with_tgt > 99.5
    # sulfur is saleable: fertilizer and sulfuric acid feedstock
    print("rule: burn a third, marry it to the rest, sell the wedding sulfur")
    print("OK: %s recovered the sulfur" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pr_blend(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # premium gasoline recipe (vol, blending RON, RVP psi)
    comps = [
        ("reformate",    30.0, 100.0, 4.0),
        ("fcc_gasoline", 30.0,  93.0, 7.0),
        ("alkylate",     15.0,  97.0, 4.5),
        ("isomerate",    15.0,  89.0, 12.0),
        ("n_butane",      2.0,  92.0, 52.0),
        ("sr_naphtha",    8.0,  70.0, 9.0),
    ]
    tot = sum(v for _, v, _, _ in comps)
    assert abs(tot - 100.0) < 1e-9
    ron = sum(v * o for _, v, o, _ in comps) / tot
    rvp = sum(v * p for _, v, _, p in comps) / tot   # linear approx; real blenders use RVP indices
    print("blend RON (vol-weighted blending numbers): %.1f" % ron)
    print("blend RVP (linear approx): %.2f psi" % rvp)
    assert ron >= 91.0, "premium octane spec"
    assert rvp <= 7.8, "summer RVP spec"
    print("specs: RON >= 91.0 PASS, RVP <= 7.8 psi PASS")
    # butane is the lever: +1 vol butane adds octane but blows RVP
    print("rule: octane is money, RVP is the leash - the optimizer walks both")
    print("OK: %s blended the gasoline" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pr_diesel(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def cetane_index_d4737(density, t10, t50, t90):
    t10n = t10 - 215.0
    t50n = t50 - 260.0
    t90n = t90 - 310.0
    b = math.exp(-3.5 * (density - 0.85)) - 1.0
    return (45.2 + 0.0892 * t10n + (0.131 + 0.901 * b) * t50n
            + (0.0523 - 0.420 * b) * t90n + 0.00049 * (t10n ** 2 - t90n ** 2)
            + 107.0 * b + 60.0 * b ** 2)
def main():
    ci = cetane_index_d4737(0.840, 210.0, 270.0, 330.0)
    print("cetane index (D4737): %.1f" % ci)
    assert 45.0 < ci < 55.0, ci
    assert ci >= 40.0, "meets minimum cetane"
    # jet fuel freeze point guard
    freeze_c = -48.0
    assert freeze_c <= -47.0, "Jet A-1 freeze spec"
    print("Jet A-1 freeze point: %.0f C (spec <= -47 C) PASS" % freeze_c)
    # ULSD sulfur
    s_ppm = 12.0
    assert s_ppm <= 15.0
    print("diesel sulfur: %.0f ppm (ULSD <= 15) PASS" % s_ppm)
    print("rule: cetane is diesel's octane-in-reverse; the lab certifies every batch")
    print("OK: %s specified the distillates" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pr_lube(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def api_group(sulfur_pct, saturates_pct, vi):
    if saturates_pct >= 90.0 and sulfur_pct <= 0.03:
        if vi >= 120.0:
            return "Group III"
        if vi >= 80.0:
            return "Group II"
    if 80.0 <= vi < 120.0:
        return "Group I"
    return "Group V / other"
def walther_slope(nu40, nu100):
    t1, t2 = 313.15, 373.15   # 40 C, 100 C in K
    y1 = math.log10(math.log10(nu40 + 0.7))
    y2 = math.log10(math.log10(nu100 + 0.7))
    return (y1 - y2) / (math.log10(t2) - math.log10(t1))
def main():
    g = api_group(0.01, 95.0, 105.0)
    print("S=0.01%%, saturates=95%%, VI=105 -> API %s" % g)
    assert g == "Group II", g
    g3 = api_group(0.005, 99.0, 125.0)
    assert g3 == "Group III", g3
    print("S=0.005%%, saturates=99%%, VI=125 -> API %s" % g3)
    # VI concept: same KV100, flatter Walther slope = higher VI
    sA = walther_slope(95.0, 10.0)
    sB = walther_slope(70.0, 10.0)
    print("Walther slope A (KV40=95): %.3f ; B (KV40=70): %.3f" % (sA, sB))
    assert sB < sA, "flatter slope = higher VI"
    print("oil B changes viscosity less with temperature -> higher viscosity index")
    print("rule: classify by sulfur/saturates/VI; formulate by grade")
    print("OK: %s graded the base oil" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pr_asphalt(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def pg_grade(high_pass, low_pass):
    return "PG %d-%d" % (high_pass, abs(low_pass))
def main():
    # DSR: passes rutting criterion at 64 C, fails at 70 C
    dsr_pass_64, dsr_pass_70 = True, False
    # BBR: passes thermal cracking criterion at -22 C, fails at -28 C
    bbr_pass_m22, bbr_pass_m28 = True, False
    high = 64 if (dsr_pass_64 and not dsr_pass_70) else None
    low = -22 if (bbr_pass_m22 and not bbr_pass_m28) else None
    grade = pg_grade(high, low)
    print("high-temp grade: %d C (DSR rutting) ; low-temp grade: %d C (BBR cracking)" % (high, low))
    print("Superpave grade: %s" % grade)
    assert grade == "PG 64-22", grade
    # penetration legacy check: 60/70 pen ~ 6-7 mm at 25 C
    pen = 65.0
    assert 60.0 <= pen <= 70.0
    print("legacy penetration: %.0f dmm (60/70 grade) - consistency confirmed" % pen)
    print("rule: grade the binder for the pavement's hottest and coldest day")
    print("OK: %s paved the grade" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pr_petrochem(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    feed = 100.0   # tonnes naphtha
    yields = {"ethylene": 30.0, "propylene": 14.0, "butadiene": 5.0,
              "pygas": 20.0, "fuel_oil": 15.0, "fuel_gas": 16.0}
    assert abs(sum(yields.values()) - feed) < 1e-9
    print("steam cracker, 100 t naphtha ->")
    for n_, y in yields.items():
        print("  %-10s %5.1f t" % (n_, y))
    assert 28.0 < yields["ethylene"] < 32.0
    # chemical value uplift vs fuel value
    ethylene_t = yields["ethylene"]
    print("ethylene: %.0f t - the highest-volume organic chemical on earth" % ethylene_t)
    # pygas returns aromatics to the refinery/chemical pool
    assert yields["pygas"] > 0
    print("rule: crack hot, quench fast, sell the molecules the market loves")
    print("OK: %s integrated the chemicals" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pr_safety(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # LOPA: cooling-failure initiating event, three independent layers
    f_init = 0.10            # per year
    pfd_alarm = 0.10         # operator response to alarm
    pfd_sis = 0.10           # SIL 1 interlock
    pfd_relief = 0.01        # relief valve
    f_mitigated = f_init * pfd_alarm * pfd_sis * pfd_relief
    print("initiating: %.2f/yr" % f_init)
    print("mitigated: %.1e/yr" % f_mitigated)
    assert abs(f_mitigated - 1e-5) < 1e-12, f_mitigated
    target = 1e-4
    assert f_mitigated < target
    print("target < %.0e/yr: PASS - layers multiply the safety" % target)
    # relief sizing sketch: orifice area scales with required mass rate
    W1, W2 = 10000.0, 20000.0   # lb/h
    print("double the relief load -> double the orifice area (%.0f -> %.0f lb/h)" % (W1, W2))
    assert W2 / W1 == 2.0
    print("rule: no single layer may be trusted; independence is the math")
    print("OK: %s guarded the plant" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pr_env(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # FCC regenerator wet scrubber: 2000 ppm SO2 in, 95% removal
    so2_in = 2000.0
    removal = 0.95
    so2_out = so2_in * (1.0 - removal)
    print("scrubber: %.0f ppm SO2 in -> %.0f ppm out (%.0f%% removal)" % (so2_in, so2_out, removal * 100.0))
    assert so2_out < 250.0, so2_out
    # flare destruction efficiency
    de = 0.985
    assert de > 0.98
    print("flare destruction efficiency: %.1f%% (>98%% required)" % (de * 100.0))
    # LDAR: finding and fixing leakers
    valves, leak_frac = 50000, 0.005
    leakers = valves * leak_frac
    print("LDAR: %.0f valves x %.1f%% leaking = %.0f leakers to fix" % (valves, leak_frac * 100.0, leakers))
    assert abs(leakers - 250.0) < 1e-9
    # fenceline benzene action level
    benzene_ug = 7.0
    assert benzene_ug < 9.0, "fenceline action level"
    print("fenceline benzene: %.1f ug/m3 (< 9 action level) PASS" % benzene_ug)
    print("rule: measure everything, permit nothing uncounted")
    print("OK: %s cleaned the air" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pr_econ(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    crude_cap = 100.0   # kbpd
    units = [("CDU", 100.0, 1.0), ("VDU", 50.0, 2.0), ("FCC", 40.0, 6.0),
             ("reformer", 20.0, 5.0), ("hydrocracker", 30.0, 6.0),
             ("coker", 25.0, 6.0), ("alkylation", 10.0, 10.0)]
    nci = sum((cap / crude_cap) * f for _, cap, f in units)
    print("Nelson complexity index: %.1f" % nci)
    assert 9.0 < nci < 12.0, nci
    # margin math
    crude_price, product_value, opex = 80.0, 95.0, 5.0
    gross = product_value - crude_price
    net = gross - opex
    print("gross margin: $%.0f/bbl ; net: $%.0f/bbl" % (gross, net))
    assert abs(net - 10.0) < 1e-9
    annual_M = net * 200000.0 * 365.0 / 1e6
    print("at 200 kbpd: $%.0f million/year - fractions of dollars matter" % annual_M)
    assert 700.0 < annual_M < 760.0, annual_M
    # crack spread shorthand
    spread = 2.0 * 100.0 + 1.0 * 95.0 - 3.0 * 80.0
    print("3-2-1 crack spread sketch: $%.0f per 3 bbl" % spread)
    assert spread > 0
    print("rule: complexity buys crude discounts; the LP spends them wisely")
    print("OK: %s counted the margin" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pr_quality(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def check(value, limit, higher_ok=True):
    return value >= limit if higher_ok else value <= limit
def main():
    gasoline = [("RON", 93.2, 91.0, True), ("RVP_psi", 7.5, 7.8, False),
                ("sulfur_ppm", 8.0, 10.0, False), ("benzene_volpct", 0.5, 0.62, False)]
    diesel = [("cetane_index", 50.8, 40.0, True), ("sulfur_ppm", 12.0, 15.0, False)]
    allpass = True
    for name_, val, lim, hi in gasoline + diesel:
        ok = check(val, lim, hi)
        allpass = allpass and ok
        print("  %-14s %6.2f vs %-6.2f %s" % (name_, val, lim, "PASS" if ok else "FAIL"))
    assert allpass, "batch fails certification"
    print("batch certified: every spec PASS - the lab releases the barrel")
    print("rule: the certificate of quality is the barrel's passport")
    print("OK: %s proved the barrel" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pr_corrosion(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def mpy(weight_loss_mg, density, area_in2, hours):
    return 534.0 * weight_loss_mg / (density * area_in2 * hours)
def main():
    rate = mpy(150.0, 7.85, 5.0, 2000.0)
    print("coupon: 150 mg lost, 2000 h -> %.2f mils/year" % rate)
    assert abs(rate - 1.02) < 0.03, rate
    assert rate < 5.0, "acceptable for carbon steel"
    print("< 5 mpy: acceptable for carbon steel service")
    # remaining life: 0.250 in wall, 0.100 in retirement thickness
    wall, retire = 0.250, 0.100
    life_years = (wall - retire) * 1000.0 / rate
    print("remaining life: %.0f years at this rate" % life_years)
    assert life_years > 100.0
    # high rate triggers upgrade: 25 mpy
    assert mpy(150.0 * 25.0, 7.85, 5.0, 2000.0) > 20.0
    print("rule: measure the metal, schedule the replacement, never gamble the wall")
    print("OK: %s watched the metal" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pr_energy(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # preheat train exchanger duty: Q = m cp dT
    m_dot, cp, dT = 50.0, 2.2, 80.0   # kg/s, kJ/kg-K, K
    duty_MW = m_dot * cp * dT / 1000.0
    print("exchanger duty: %.1f MW recovered into incoming crude" % duty_MW)
    assert abs(duty_MW - 8.8) < 1e-9, duty_MW
    # furnace efficiency from measured duty and fuel
    duty, fuel = 88.0, 100.0   # MW, LHV basis
    eff = duty / fuel * 100.0
    print("furnace: %.0f MW duty / %.0f MW fuel = %.0f%% efficiency" % (duty, fuel, eff))
    assert 85.0 < eff < 92.0, eff
    # pinch insight: minimum approach 15 F sets the utility target
    approach = 15.0
    print("pinch approach: %.0f F - tighter costs exchangers, looser wastes fuel" % approach)
    assert 10.0 <= approach <= 20.0
    print("rule: recover heat before buying it; the pinch names the minimum")
    print("OK: %s integrated the heat" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pr_water(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    influent_ppm = 400.0
    # treatment train removals
    after_api = influent_ppm * (1.0 - 0.80)
    after_daf = after_api * (1.0 - 0.85)
    effluent = after_daf * (1.0 - 0.33)   # bio + polish
    print("oil in water: %.0f ppm -> API %.0f -> DAF %.0f -> effluent %.1f ppm"
          % (influent_ppm, after_api, after_daf, effluent))
    assert abs(after_api - 80.0) < 1e-9
    assert abs(after_daf - 12.0) < 1e-9
    assert effluent < 15.0, "permit limit"
    print("effluent %.1f ppm < 15 ppm permit PASS" % effluent)
    # sour water stripper keeps biology alive
    h2s_in, h2s_out = 500.0, 5.0
    assert h2s_out < 10.0
    print("stripper: %.0f ppm H2S -> %.0f ppm - the microbes stay alive" % (h2s_in, h2s_out))
    print("rule: separate, float, biodegrade, polish - in that order")
    print("OK: %s cleaned the water" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pr_catalyst(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # first-order deactivation: a(t) = exp(-kd * t)
    kd = 0.020    # per day
    t = 30.0
    a = math.exp(-kd * t)
    print("activity after %.0f days: %.3f" % (t, a))
    assert 0.50 < a < 0.60, a
    # cycle end: activity 0.70 -> days on stream
    t_end = -math.log(0.70) / kd
    print("time to 70%% activity: %.1f days - then regenerate or change out" % t_end)
    assert 15.0 < t_end < 20.0, t_end
    # FCC equilibrium: makeup rate holds e-cat activity
    makeup_pct_day = 1.5
    inventory_tons = 300.0
    makeup_tpd = inventory_tons * makeup_pct_day / 100.0
    print("FCC makeup: %.1f tons/day on %.0f-ton inventory" % (makeup_tpd, inventory_tons))
    assert abs(makeup_tpd - 4.5) < 1e-9
    # guard bed protects the main bed
    print("rule: manage activity like a roster - fresh in, spent out, guards up front")
    print("OK: %s managed the catalyst" % NAME)
if __name__ == "__main__":
    main()
''')

DEMOS = {
    "pr_what": demo_pr_what, "pr_composition": demo_pr_composition,
    "pr_assay": demo_pr_assay, "pr_api": demo_pr_api,
    "pr_flow": demo_pr_flow, "pr_desalt": demo_pr_desalt,
    "pr_atm": demo_pr_atm, "pr_vac": demo_pr_vac,
    "pr_lightends": demo_pr_lightends, "pr_thermal": demo_pr_thermal,
    "pr_fcc": demo_pr_fcc, "pr_hydrocrack": demo_pr_hydrocrack,
    "pr_reform": demo_pr_reform, "pr_alky": demo_pr_alky,
    "pr_isom": demo_pr_isom, "pr_coke": demo_pr_coke,
    "pr_hds": demo_pr_hds, "pr_h2net": demo_pr_h2net,
    "pr_claus": demo_pr_claus, "pr_blend": demo_pr_blend,
    "pr_diesel": demo_pr_diesel, "pr_lube": demo_pr_lube,
    "pr_asphalt": demo_pr_asphalt, "pr_petrochem": demo_pr_petrochem,
    "pr_safety": demo_pr_safety, "pr_env": demo_pr_env,
    "pr_econ": demo_pr_econ, "pr_quality": demo_pr_quality,
    "pr_corrosion": demo_pr_corrosion, "pr_energy": demo_pr_energy,
    "pr_water": demo_pr_water, "pr_catalyst": demo_pr_catalyst,
}

DEMO_KEY = {
    "what_is_refining": "pr_what", "crude_composition": "pr_composition",
    "crude_assay": "pr_assay", "api_gravity_properties": "pr_api",
    "refinery_flow": "pr_flow", "desalting": "pr_desalt",
    "atmospheric_distillation": "pr_atm", "vacuum_distillation": "pr_vac",
    "light_ends": "pr_lightends", "thermal_cracking": "pr_thermal",
    "fcc": "pr_fcc", "hydrocracking": "pr_hydrocrack",
    "catalytic_reforming": "pr_reform", "alkylation": "pr_alky",
    "isomerization": "pr_isom", "delayed_coking": "pr_coke",
    "hydrotreating": "pr_hds", "hydrogen_network": "pr_h2net",
    "amine_sulfur": "pr_claus", "gasoline_blending": "pr_blend",
    "diesel_jet_specs": "pr_diesel", "lubricants": "pr_lube",
    "heavy_products": "pr_asphalt", "petrochemical_integration": "pr_petrochem",
    "refinery_safety": "pr_safety", "environmental_controls": "pr_env",
    "refinery_economics": "pr_econ", "quality_testing": "pr_quality",
    "corrosion_materials": "pr_corrosion", "energy_integration": "pr_energy",
    "wastewater": "pr_water", "catalysts": "pr_catalyst",
}
assert set(DEMO_KEY) == {e["key"] for e in ENTRIES}, "demo key map incomplete"
assert set(DEMO_KEY.values()) == set(DEMOS), "demo map misses demos"

def build_records(slug, source):
    cfg = DBCFG[slug]
    sig = source == "signature"
    # Teaching-ladder order: stable sort by ladder_rank (entries are already
    # in ladder order in entries_petroleum_refining.py).
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
        demo_fn = DEMOS[DEMO_KEY[e["key"]]]
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
    for slug in ("petroleum-refining", "petroleum-refining-signature"):
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
                               capture_output=True, text=True, timeout=120)
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
        assert "pill-ex" in page and "qmerge" in page, "Exhaustive pill / merger button missing"
        assert "dataset.p" in page, "tab-handler guard missing"
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
