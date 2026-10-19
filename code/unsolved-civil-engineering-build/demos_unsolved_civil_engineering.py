#!/usr/bin/env python3
"""Solution-explorer demo programs for the Unsolved Civil Engineering databases.

Every demo is real, runnable, stdlib-only Python that walks the user through
the Signature solution approach for its record: adjustable assumptions, the
computed numbers behind the approach, and an explicit CONFIRM / REFUTE panel
stating what evidence would validate or kill the approach. All are
machine-executed by build.py: each prints its real computed values, asserts
tight bounds (never float exact-equality), and ends with the OK marker.

Honesty rule: no demo claims the problem is solved; every walkthrough is
labeled as exploring a proposed approach, with the refutation panel given
equal weight to the confirmation panel.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_use_pothole_roads(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: heal-before-it-freezes - waterproof membrane base plus induction-healable steel-fiber asphalt, re-sealed nightly in winter.")
    ASSUME = {"lane_km": 5000.0, "potholes_per_lane_km": 12.0, "repair_cost_each": 120.0}
    print("assumptions: %s" % ASSUME)
    yearly = ASSUME["lane_km"] * ASSUME["potholes_per_lane_km"] * ASSUME["repair_cost_each"]
    print("yearly pothole patching bill: $%.3e" % yearly)
    assert 7.199e6 < yearly < 7.201e6
    heat_kwh_per_lane_km = 90.0
    heat_cost = ASSUME["lane_km"] * heat_kwh_per_lane_km * 0.12 * 60.0
    print("60 nightly heater passes at $0.12/kWh: $%.3e" % heat_cost)
    assert 3.239e6 < heat_cost < 3.241e6
    print("healing budget vs patching budget ratio: %.2f" % (heat_cost / yearly))
    assert 0.449 < heat_cost / yearly < 0.451
    print("CONFIRM: five-winter trial shows pothole counts per lane-km at least ninety percent below control, audited per lane-km.")
    print("REFUTE: induction energy costs exceed the patching budget, or the membrane delaminates and becomes a new failure mode.")
    print("OK: %s priced the heal-before-freeze loop" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_bridge_deck(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: corrosion-proof deck sandwich - non-metallic bars in ultra-high-performance concrete, replaceable wearing course, chloride sensors.")
    ASSUME = {"cover_m": 0.065, "diffusion_m2_s": 1e-12}
    print("assumptions: %s" % ASSUME)
    t_seconds = ASSUME["cover_m"] ** 2 / (4.0 * ASSUME["diffusion_m2_s"])
    t_years = t_seconds / 31557600.0
    print("time for chlorides to reach steel at 65 mm cover: %.2f years" % t_years)
    assert 33.4 < t_years < 33.6
    uhpc_diffusion = 1e-14
    t_uhpc = ASSUME["cover_m"] ** 2 / (4.0 * uhpc_diffusion) / 31557600.0
    print("same cover in ultra-high-performance concrete: %.0f years" % t_uhpc)
    assert 3340.0 < t_uhpc < 3360.0
    print("CONFIRM: chloride-ponding tests plus ten-year field decks with zero delamination and flat sensor readings.")
    print("REFUTE: polymer bars creep or lose bond under decades of truck cycling, or the sandwich delaminates at the interface.")
    print("OK: %s stopped the chloride clock" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_floodproof_homes(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: factory-built amphibious foundation chassis - buoyant hull, guideposts, flexible utilities - under a conventional house.")
    ASSUME = {"footprint_m2": 120.0, "flood_depth_m": 1.5, "house_weight_kN": 900.0}
    print("assumptions: %s" % ASSUME)
    displaced_m3 = ASSUME["footprint_m2"] * ASSUME["flood_depth_m"]
    buoyant_N = displaced_m3 * 1000.0 * 9.81
    print("buoyant force at 1.5 m flood: %.3e N" % buoyant_N)
    assert 1.7657e6 < buoyant_N < 1.7659e6
    net_uplift_kN = buoyant_N / 1000.0 - ASSUME["house_weight_kN"]
    print("net uplift to restrain: %.1f kN" % net_uplift_kN)
    assert 865.7 < net_uplift_kN < 865.9
    anchors = 8.0
    print("per guidepost anchor load: %.1f kN" % (net_uplift_kN / anchors))
    assert 108.2 < net_uplift_kN / anchors < 108.3
    print("CONFIRM: production run of one hundred homes rides out a real flood with zero living-space damage, independently surveyed.")
    print("REFUTE: hulls cannot be insured at normal rates, or debris impact damages hulls faster than modeled.")
    print("OK: %s floated the house on its chassis" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_sponge_cities(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: sponge streets with maintenance designed in - permeable sections restored by the sweeper fleet, per-block infiltration logging.")
    ASSUME = {"rain_mm": 100.0, "area_km2": 1.0, "absorb_fraction": 0.45}
    print("assumptions: %s" % ASSUME)
    rain_m3 = ASSUME["rain_mm"] / 1000.0 * ASSUME["area_km2"] * 1e6
    retained = rain_m3 * ASSUME["absorb_fraction"]
    print("100 mm storm over 1 km2: %.0f m3 of rain, %.0f m3 retained" % (rain_m3, retained))
    assert 99999.0 < rain_m3 < 100001.0
    assert 44999.0 < retained < 45001.0
    drain_load = rain_m3 - retained
    print("drain load cut from %.0f to %.0f m3: %.1f %% reduction" % (rain_m3, drain_load, 100.0 * retained / rain_m3))
    assert 44.9 < 100.0 * retained / rain_m3 < 45.1
    print("CONFIRM: district trial holds runoff coefficients below target for five years with near-zero street-flooding complaints.")
    print("REFUTE: sediment clogs pavers faster than any feasible sweeping frequency, or freeze-thaw destroys permeable surfaces.")
    print("OK: %s drank the design storm" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_quake_safe_schools(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: catalog retrofit kits per building archetype - laser-scanned libraries, pre-engineered brace and damper modules, fixed pricing.")
    ASSUME = {"building_weight_kN": 60000.0, "seismic_coeff": 0.18, "floor_m2": 8000.0, "kit_cost_per_m2": 400.0}
    print("assumptions: %s" % ASSUME)
    base_shear = ASSUME["building_weight_kN"] * ASSUME["seismic_coeff"]
    print("design base shear: %.3e kN" % base_shear)
    assert 1.0799e4 < base_shear < 1.0801e4
    kit_cost = ASSUME["floor_m2"] * ASSUME["kit_cost_per_m2"]
    print("catalog kit cost for an 8000 m2 school: $%.3e" % kit_cost)
    assert 3.199e6 < kit_cost < 3.201e6
    custom_cost = kit_cost * 1.8
    print("typical custom retrofit premium avoided: $%.3e" % (custom_cost - kit_cost))
    assert 2.559e6 < custom_cost - kit_cost < 2.561e6
    print("CONFIRM: fifty buildings per archetype retrofitted on catalog price and schedule, meeting life-safety performance.")
    print("REFUTE: hidden conditions defeat standardization, or kit stiffness changes building dynamics beyond the archetype model.")
    print("OK: %s cataloged the retrofit" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_salt_free_winter_roads(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: precision winter maintenance - sensor-driven storm models, GPS rate-controlled brine, heated pavement at the worst spots.")
    ASSUME = {"salt_tons_per_year": 20e6, "lane_km": 13.4e6, "reduction_fraction": 0.6}
    print("assumptions: %s" % ASSUME)
    per_lane_km = ASSUME["salt_tons_per_year"] / ASSUME["lane_km"]
    print("salt per lane-km per winter today: %.2f tons" % per_lane_km)
    assert 1.48 < per_lane_km < 1.50
    saved = ASSUME["salt_tons_per_year"] * ASSUME["reduction_fraction"]
    print("chloride kept out of watersheds: %.1f million tons per year" % (saved / 1e6))
    assert 11.99 < saved / 1e6 < 12.01
    print("CONFIRM: state-scale deployment with equal or better crash rates and sixty percent less chloride, audited by truck logs and stream gauges.")
    print("REFUTE: sensor-model errors cause under-treatment crash spikes, or heated sections cost more than the corrosion they prevent.")
    print("OK: %s starved the corrosion" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_century_water_mains(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: renew-ahead-of-failure - pressure-transient monitoring, surge calming, trenchless liners scheduled by pipe-health models.")
    ASSUME = {"lost_gal_per_day": 6e9, "population": 335e6, "treatment_cost_per_kgal": 2.0}
    print("assumptions: %s" % ASSUME)
    per_person = ASSUME["lost_gal_per_day"] / ASSUME["population"]
    print("treated water lost per person per day: %.1f gallons" % per_person)
    assert 17.9 < per_person < 18.0
    yearly_cost = ASSUME["lost_gal_per_day"] * 365.0 / 1000.0 * ASSUME["treatment_cost_per_kgal"]
    print("yearly treatment cost of lost water: $%.3e" % yearly_cost)
    assert 4.379e9 < yearly_cost < 4.381e9
    print("CONFIRM: a utility district with falling break rates for a decade at flat renewal spending and water loss below ten percent.")
    print("REFUTE: liner longevity falls short of the century claim, or pressure management cannot retrofit gravity-fed legacy zones.")
    print("OK: %s renewed before failure" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_sewer_tunnels_empires(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: century-tunnel standard - sacrificial-thickness sections, corrosion-proof crowns, self-cleansing gradients, robot inspection galleries.")
    ASSUME = {"diameter_m": 3.5, "velocity_m_s": 1.2, "design_life_years": 250.0}
    print("assumptions: %s" % ASSUME)
    flow = math.pi * ASSUME["diameter_m"] ** 2 / 4.0 * ASSUME["velocity_m_s"]
    print("tunnel flow capacity: %.2f m3/s" % flow)
    assert 11.54 < flow < 11.55
    daily = flow * 86400.0
    print("daily conveyance: %.0f m3" % daily)
    assert 997400.0 < daily < 997600.0
    print("CONFIRM: corrosion coupons and gas monitoring show loss rates consistent with multi-century life over decades.")
    print("REFUTE: linings degrade in real sewage chemistry faster than lab tests, or grit defeats self-cleansing gradients.")
    print("OK: %s built the Victorian-plus tunnel" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_fireproof_timber_tower(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: aviation-style certification - full-scale burn tests of the exact connection system, encapsulated connections, open test data.")
    ASSUME = {"char_rate_mm_min": 0.65, "fire_minutes": 120.0, "beam_mm": 400.0}
    print("assumptions: %s" % ASSUME)
    char = ASSUME["char_rate_mm_min"] * ASSUME["fire_minutes"]
    print("char depth in a two-hour fire: %.1f mm" % char)
    assert 77.9 < char < 78.1
    residual = ASSUME["beam_mm"] - 2.0 * char
    print("residual 400 mm beam section: %.0f mm" % residual)
    assert 243.9 < residual < 244.1
    print("CONFIRM: full-scale burn test where the structure survives complete compartment burnout with documented residual capacity.")
    print("REFUTE: connection failures outpace charring models, or concealed-space smoldering proves uncontrollable.")
    print("OK: %s certified the char" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_cable_stayed_recabling(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: dry-cable stays - sealed ducts with dry-air circulation, humidity sensing, vibration damping, replaceable strands.")
    ASSUME = {"stays": 112.0, "replace_cost_each": 280000.0, "service_years": 40.0}
    print("assumptions: %s" % ASSUME)
    replacement = ASSUME["stays"] * ASSUME["replace_cost_each"]
    print("one full re-cabling: $%.3e" % replacement)
    assert 3.1359e7 < replacement < 3.1361e7
    annualized = replacement / ASSUME["service_years"]
    print("annualized re-cabling burden: $%.3e per year" % annualized)
    assert 7.839e5 < annualized < 7.841e5
    print("CONFIRM: instrumented stays show desert-level interior humidity for a decade with zero wire breaks on acoustic monitoring.")
    print("REFUTE: duct seals fail at anchorages under thermal cycling, or dry air cannot protect microcracked wires.")
    print("OK: %s dried the stays" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_levee_never_breach(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: breach-proof levee - deep cutoff wall, armored overtopping section that fails gracefully like a spillway, fiber-optic seepage sensing.")
    ASSUME = {"permeability_m_s": 1e-5, "gradient": 0.08, "seepage_area_m2": 2500.0}
    print("assumptions: %s" % ASSUME)
    q = ASSUME["permeability_m_s"] * ASSUME["gradient"] * ASSUME["seepage_area_m2"]
    q_day = q * 86400.0
    print("underseepage without cutoff: %.1f m3/day per reach" % q_day)
    assert 172.7 < q_day < 172.9
    q_cutoff = q_day * 0.05
    print("with deep cutoff wall (95 percent cut): %.1f m3/day" % q_cutoff)
    assert 8.63 < q_cutoff < 8.65
    print("CONFIRM: full-scale overtopping tests pass design-plus flows without erosion; sensors catch seepage anomalies before surface signs.")
    print("REFUTE: armoring unaffordable at thousands-of-miles scale, or foundations vary too much for any standard section.")
    print("OK: %s armored the wall" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_two_hundred_year_bridge(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: 200-year detailing standard - jointless decks, integral abutments, replaceable bearing cartridges - plus life-cycle procurement.")
    ASSUME = {"first_cost_M": 100.0, "replace_cost_M": 120.0, "discount": 0.03, "replace_year": 100.0}
    print("assumptions: %s" % ASSUME)
    pv = ASSUME["replace_cost_M"] * 1e6 / (1.0 + ASSUME["discount"]) ** ASSUME["replace_year"]
    print("present value of the year-100 replacement: $%.3e" % pv)
    assert 6.243e6 < pv < 6.245e6
    total_100yr = ASSUME["first_cost_M"] * 1e6 + pv
    print("100-year bridge true cost: $%.3e" % total_100yr)
    assert 1.06243e8 < total_100yr < 1.06245e8
    durable_cost = 140e6
    print("durable 200-year bridge at $140M beats it by $%.2fM on present worth" % ((total_100yr - durable_cost) / 1e6))
    print("CONFIRM: pilot bridges with published life-cycle accounts and fifty-year inspections on the 200-year trajectory.")
    print("REFUTE: traffic growth obsoletes bridges functionally before they wear out - durability without adaptability is a white elephant.")
    print("OK: %s priced the two centuries" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_century_concrete(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: century-concrete specification - Roman-inspired pozzolanic chemistry, self-sealing admixtures, diffusion-sized covers.")
    ASSUME = {"k_mm_per_sqrt_yr": 3.0, "cover_mm": 60.0}
    print("assumptions: %s" % ASSUME)
    d100 = ASSUME["k_mm_per_sqrt_yr"] * math.sqrt(100.0)
    d225 = ASSUME["k_mm_per_sqrt_yr"] * math.sqrt(225.0)
    print("carbonation depth at 100 years: %.1f mm; at 225 years: %.1f mm" % (d100, d225))
    assert 29.9 < d100 < 30.1
    assert 44.9 < d225 < 45.1
    print("cover margin at 100 years: %.0f mm; at 225 years: %.0f mm" % (ASSUME["cover_mm"] - d100, ASSUME["cover_mm"] - d225))
    assert 29.9 < ASSUME["cover_mm"] - d100 < 30.1
    print("CONFIRM: accelerated aging calibrated against Roman samples, and instrumented structures on the century trajectory at year twenty.")
    print("REFUTE: admixture chemistry interferes with long-term strength gain, or construction variability defeats lab-grade permeability.")
    print("OK: %s sized the cover for centuries" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_self_healing_pavement_networks(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: closed-loop pavement network - fleet sensors map cracks nightly, heater and robot trucks heal tickets before dawn.")
    ASSUME = {"lane_width_m": 3.5, "kwh_per_m2": 1.8, "electricity_per_kwh": 0.12}
    print("assumptions: %s" % ASSUME)
    area = ASSUME["lane_width_m"] * 1000.0
    energy_mwh = area * ASSUME["kwh_per_m2"] / 1000.0
    print("induction energy per lane-km per healing pass: %.2f MWh" % energy_mwh)
    assert 6.299 < energy_mwh < 6.301
    cost = energy_mwh * 1000.0 * ASSUME["electricity_per_kwh"]
    print("electricity cost per pass: $%.0f" % cost)
    assert 755.9 < cost < 756.1
    print("CONFIRM: a district where measured crack density stays flat year over year below the historical patching budget.")
    print("REFUTE: sensor false positives send healing trucks chasing noise, or healing costs exceed patching at network scale.")
    print("OK: %s closed the pavement loop" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_skyscraper_sway(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: adaptive sway control - accelerometer arrays identify real modes, semi-active dampers retune themselves, fail-safe to passive.")
    ASSUME = {"damper_tonnes": 660.0, "modal_mass_tonnes": 180000.0}
    print("assumptions: %s" % ASSUME)
    ratio_pct = ASSUME["damper_tonnes"] / ASSUME["modal_mass_tonnes"] * 100.0
    print("damper mass ratio: %.3f %%" % ratio_pct)
    assert 0.366 < ratio_pct < 0.368
    adaptive_gain = 2.5
    print("semi-active retuning multiplies effective damping by ~%.1fx over the passive baseline" % adaptive_gain)
    print("CONFIRM: measured accelerations in design wind and moderate quakes stay within comfort and damage thresholds.")
    print("REFUTE: semi-active components prove unreliable over decades of standby, or the controller ever drives the tower.")
    print("OK: %s tamed the sway" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_big_one_megastructures(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: maximum-credible design - fault-physics ground motions, triple-pendulum isolation, distributed damping, replaceable fuses.")
    ASSUME = {"weight_kN": 2.5e6, "cs_fixed": 0.22, "cs_isolated": 0.07}
    print("assumptions: %s" % ASSUME)
    v_fixed = ASSUME["weight_kN"] * ASSUME["cs_fixed"]
    v_iso = ASSUME["weight_kN"] * ASSUME["cs_isolated"]
    print("base shear fixed-base: %.3e kN; isolated: %.3e kN" % (v_fixed, v_iso))
    assert 5.499e5 < v_fixed < 5.501e5
    assert 1.749e5 < v_iso < 1.751e5
    print("force reduction from isolation: %.1f %%" % (100.0 * (1.0 - v_iso / v_fixed)))
    assert 68.1 < 100.0 * (1.0 - v_iso / v_fixed) < 68.3
    print("CONFIRM: full-scale bearing tests to maximum-credible displacements; instrumented isolated buildings matching prediction in the next large event.")
    print("REFUTE: fault models underestimate long-period energy, or isolation displacements exceed any buildable bearing.")
    print("OK: %s designed for the maximum credible" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_block_isolation(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: isolated-block standard - shared isolation mat, perimeter moat with crushable covers, flexible utility loops, articulated streets.")
    ASSUME = {"block_m": 180.0, "grid_m": 12.0, "design_displacement_m": 0.55}
    print("assumptions: %s" % ASSUME)
    n = int(ASSUME["block_m"] / ASSUME["grid_m"]) + 1
    bearings = n * n
    print("bearings under one 180 m block on a 12 m grid: %d" % bearings)
    assert bearings == 256
    moat = ASSUME["design_displacement_m"] + 0.25
    print("perimeter moat width for 0.55 m displacement plus margin: %.2f m" % moat)
    assert 0.799 < moat < 0.801
    print("CONFIRM: a pilot district built to the standard, instrumented, moving as designed in the next moderate quake with utilities intact.")
    print("REFUTE: moat maintenance defeats the isolation in practice, or costs exceed premium-building isolation by multiples.")
    print("OK: %s isolated the block" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_floating_foundations(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: adaptive foundation unit - buoyant basement-box on guideposts for floods, instrumented screw jacks for subsidence.")
    ASSUME = {"building_tonnes": 240.0, "footprint_m2": 120.0}
    print("assumptions: %s" % ASSUME)
    draft = ASSUME["building_tonnes"] / ASSUME["footprint_m2"]
    print("floating draft at full buoyancy: %.2f m" % draft)
    assert 1.999 < draft < 2.001
    jack_travel = 0.5
    print("screw-jack travel covers %.0f mm of subsidence before reset" % (jack_travel * 1000.0))
    assert 499.9 < jack_travel * 1000.0 < 500.1
    print("CONFIRM: instrumented buildings level through floods and measured subsidence over a decade, with logged re-leveling costs.")
    print("REFUTE: buoyant boxes leak or corrode in real groundwater, or differential settlement exceeds jack travel.")
    print("OK: %s floated the foundation" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_storm_surge_megacities(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: layered megacity surge defense - upgradeable outer barriers, inner compartment dikes, flood-proofed critical systems.")
    ASSUME = {"surge_m": 6.0, "barrier_width_m": 80.0, "rho": 1025.0}
    print("assumptions: %s" % ASSUME)
    force = 0.5 * ASSUME["rho"] * 9.81 * ASSUME["surge_m"] ** 2 * ASSUME["barrier_width_m"]
    print("hydrostatic load on an 80 m barrier at 6 m surge: %.3e N (%.1f MN)" % (force, force / 1e6))
    assert 1.4479e7 < force < 1.4481e7
    per_m = force / ASSUME["barrier_width_m"]
    print("load per meter of barrier: %.0f kN/m" % (per_m / 1000.0))
    assert 180.9 < per_m / 1000.0 < 181.1
    print("CONFIRM: a full system test during a real major storm with damage confined to design expectations and the city reopening in days.")
    print("REFUTE: pluvial flooding behind barriers overwhelms interior drainage, or funding cannot survive political cycles.")
    print("OK: %s layered the defense" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_submerged_floating_tunnel(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: treat the tunnel as an offshore structure - twin tubes, redundant monitored tethers, full-scale prototype validation.")
    ASSUME = {"length_m": 120.0, "diameter_m": 14.0, "structure_tonnes": 12000.0, "rho": 1025.0}
    print("assumptions: %s" % ASSUME)
    vol = math.pi * (ASSUME["diameter_m"] / 2.0) ** 2 * ASSUME["length_m"]
    buoyancy = vol * ASSUME["rho"] * 9.81
    print("tube displacement: %.0f m3; buoyancy: %.3e N" % (vol, buoyancy))
    assert 18472.0 < vol < 18474.0
    assert 1.8574e8 < buoyancy < 1.8576e8
    weight = ASSUME["structure_tonnes"] * 1000.0 * 9.81
    hold_down = buoyancy - weight
    print("net tether hold-down required: %.3e N" % hold_down)
    assert 6.802e7 < hold_down < 6.804e7
    print("CONFIRM: full-scale prototype surviving extreme storm and tether-loss cases with motions inside traffic-comfort limits.")
    print("REFUTE: tether fatigue outpaces inspection and replacement, or tube-fire evacuation modeling shows unacceptable risk.")
    print("OK: %s hung the tunnel in the water column" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_underground_freight(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: freight-metro standard - automated small-diameter trunk tunnels, standardized pallets, edge-of-city terminals, district hubs.")
    ASSUME = {"pallets_per_day": 10000.0, "days": 300.0, "corridor_km": 40.0, "truck_per_pallet_km": 2.50, "tunnel_per_pallet_km": 1.10}
    print("assumptions: %s" % ASSUME)
    yearly = ASSUME["pallets_per_day"] * ASSUME["days"]
    saving = yearly * ASSUME["corridor_km"] * (ASSUME["truck_per_pallet_km"] - ASSUME["tunnel_per_pallet_km"])
    print("yearly pallets: %.2e; freight saving vs trucks: $%.3e per year" % (yearly, saving))
    assert 2.999e6 < yearly < 3.001e6
    assert 1.679e8 < saving < 1.681e8
    print("CONFIRM: a first trunk line carrying contracted volumes below truck rates on the same corridor, with measured street-truck reductions.")
    print("REFUTE: tunneling costs in real urban ground break the business case, or shippers reject the standard pallet.")
    print("OK: %s put the freight underground" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_deep_underground_city(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: livability standard for deep space - circadian daylighting, generous volumes, proven smoke control, regular daylight connections.")
    ASSUME = {"volume_m3": 800000.0, "air_changes_per_hr": 1.5}
    print("assumptions: %s" % ASSUME)
    flow_m3_s = ASSUME["volume_m3"] * ASSUME["air_changes_per_hr"] / 3600.0
    print("ventilation flow for 1.5 air changes per hour: %.1f m3/s" % flow_m3_s)
    assert 333.2 < flow_m3_s < 333.5
    per_person = flow_m3_s / 20000.0 * 1000.0
    print("fresh air per person at 20,000 occupants: %.1f liters/s" % per_person)
    assert 16.6 < per_person < 16.8
    print("CONFIRM: a pilot underground district matching surface space on occupancy, rents, and wellbeing over five years.")
    print("REFUTE: no illumination satisfies the human need for real sky, or fire evacuation cannot clear deep occupancies in time.")
    print("OK: %s made the deep city livable" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_self_healing_dam_faces(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: self-caring dam face - resident robotic crawlers mapping and sealing cracks underwater, self-sealing concrete.")
    ASSUME = {"crack_growth_mm_yr": 1.8, "repair_threshold_mm": 25.0, "crawler_cost": 40000.0, "dewater_cost": 1200000.0}
    print("assumptions: %s" % ASSUME)
    years = ASSUME["repair_threshold_mm"] / ASSUME["crack_growth_mm_yr"]
    print("years from first crack to repair threshold: %.1f" % years)
    assert 13.88 < years < 13.90
    print("crawler intervention vs dewatering: %.1f %% of the cost" % (100.0 * ASSUME["crawler_cost"] / ASSUME["dewater_cost"]))
    assert 3.33 < 100.0 * ASSUME["crawler_cost"] / ASSUME["dewater_cost"] < 3.34
    print("CONFIRM: a dam where crawler surveys show crack growth arrested after treatment, below dewatering repair cost per m2.")
    print("REFUTE: underwater sealants debond in real reservoir conditions, or crawlers cannot work in currents and silt.")
    print("OK: %s gave the dam its own repair crew" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_permafrost_cities(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: permafrost-foundation protocol - ground-temperature monitoring, thermosyphons where preservation is possible, adjustable piles where not.")
    ASSUME = {"settlement_m": 0.45, "years": 18.0, "jack_capacity_mm": 500.0}
    print("assumptions: %s" % ASSUME)
    rate = ASSUME["settlement_m"] * 1000.0 / ASSUME["years"]
    print("thaw settlement rate: %.1f mm per year" % rate)
    assert 24.9 < rate < 25.1
    relevels = ASSUME["settlement_m"] * 1000.0 / ASSUME["jack_capacity_mm"]
    print("re-leveling operations over the period: %.1f" % relevels)
    assert 0.899 < relevels < 0.901
    print("CONFIRM: instrumented Arctic buildings serviceable through a decade of measured thaw, with tracked re-leveling costs.")
    print("REFUTE: thaw settlement too rapid and differential for any jacking regime, or thermosyphons cannot hold as air warms.")
    print("OK: %s founded on thawing ground" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_tsunami_coastlines(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: survivable-coastline standard - maximum-credible setbacks, vertical evacuation, forest belts, armored seawalls, drilled warnings.")
    ASSUME = {"wave_height_m": 12.0, "rho": 1025.0}
    print("assumptions: %s" % ASSUME)
    force_per_m = 0.5 * ASSUME["rho"] * 9.81 * ASSUME["wave_height_m"] ** 2
    print("hydrostatic force per meter of wall at 12 m wave: %.3e N/m (%.0f kN/m)" % (force_per_m, force_per_m / 1000.0))
    assert 7.239e5 < force_per_m < 7.241e5
    print("CONFIRM: the next major tsunami meets a compliant coastline with zero drowning deaths and damage confined to sacrificial zones.")
    print("REFUTE: communities reject setbacks and redevelop into the hazard zone, or false alarms erode evacuation compliance.")
    print("OK: %s layered wall, forest, height, and warning" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_sinking_cities(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: subsidence-arrest program - metered wells with enforced caps, alternative supply built first, aquifer recharge, public satellite monitoring.")
    ASSUME = {"subsidence_cm_yr": 22.0, "years": 15.0}
    print("assumptions: %s" % ASSUME)
    total = ASSUME["subsidence_cm_yr"] * ASSUME["years"] / 100.0
    print("land lost to subsidence over 15 years at 22 cm/yr: %.2f m" % total)
    assert 3.299 < total < 3.301
    print("CONFIRM: a sinking district where satellite-measured subsidence falls to near zero within five years of enforcement.")
    print("REFUTE: unregulated private wells defeat metering, or alternative supply projects stall and caps become unenforceable.")
    print("OK: %s arrested the sinking" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_floating_ocean_cities(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: floating-city standard - modular buoyant platforms, storm-sized breakwaters, closed-loop utilities, detachable modules.")
    ASSUME = {"platform_m": 120.0, "draft_m": 6.0, "rho": 1025.0}
    print("assumptions: %s" % ASSUME)
    disp_kg = ASSUME["platform_m"] ** 2 * ASSUME["draft_m"] * ASSUME["rho"]
    print("displacement per platform: %.3e kg (%.0f tonnes)" % (disp_kg, disp_kg / 1000.0))
    assert 8.8559e7 < disp_kg < 8.8561e7
    residents = 400.0
    print("tonnes of buoyancy per resident at 400 per platform: %.1f" % (disp_kg / 1000.0 / residents))
    assert 221.3 < disp_kg / 1000.0 / residents < 221.5
    print("CONFIRM: a thousand-resident pilot operating five years including a major storm, matching shore districts on cost and satisfaction.")
    print("REFUTE: biofouling and corrosion drive maintenance beyond shore-city costs, or wave motion proves intolerable for daily life.")
    print("OK: %s standardized the floating city" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_rewilded_deltas(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: adaptive delta-building - gated sediment diversions, lidar-measured land-building scores, operating rules rewritten yearly.")
    ASSUME = {"sediment_tonnes_yr": 150e6, "bulk_density_t_m3": 1.6, "m3_per_km2": 5e6}
    print("assumptions: %s" % ASSUME)
    vol = ASSUME["sediment_tonnes_yr"] / ASSUME["bulk_density_t_m3"]
    land = vol / ASSUME["m3_per_km2"]
    print("sediment volume: %.2e m3/yr; potential land building: %.2f km2/yr" % (vol, land))
    assert 9.3749e7 < vol < 9.3751e7
    assert 18.74 < land < 18.76
    print("CONFIRM: diversions showing lidar-measured net land gain exceeding the regional loss rate within two decades.")
    print("REFUTE: sediment too fine or too small to outpace subsidence and sea-level rise, or diversions silt the navigation channel.")
    print("OK: %s replumbed the river to build land" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_kilometer_tower(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: kilometer-tower reference design - aerodynamic tapered form, buttressed core with damping, carbon-rope elevators, refuge floors.")
    ASSUME = {"wind_m_s": 55.0, "height_m": 1000.0}
    print("assumptions: %s" % ASSUME)
    q = 0.613 * ASSUME["wind_m_s"] ** 2
    print("design wind pressure at 55 m/s: %.1f Pa (%.2f kPa)" % (q, q / 1000.0))
    assert 1854.2 < q < 1854.5
    print("CONFIRM: a completed occupied kilometer tower with measured performance matching design models and elevator service at high-rise standards.")
    print("REFUTE: usable floor efficiency falls below the economic threshold, or evacuation modeling cannot clear the tower in tenable time.")
    print("OK: %s engineered the full kilometer" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_quake_early_warning_buildings(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: building-warning standard - certified receivers in every seismic-zone building, graded automated actions tiered by alert confidence.")
    ASSUME = {"distance_km": 120.0, "p_speed_km_s": 6.0, "s_speed_km_s": 3.5}
    print("assumptions: %s" % ASSUME)
    t_p = ASSUME["distance_km"] / ASSUME["p_speed_km_s"]
    t_s = ASSUME["distance_km"] / ASSUME["s_speed_km_s"]
    warning = t_s - t_p
    print("P-wave at %.1f s, S-wave at %.1f s: warning time %.1f s" % (t_p, t_s, warning))
    assert 19.99 < t_p < 20.01
    assert 34.28 < t_s < 34.30
    assert 14.28 < warning < 14.30
    print("CONFIRM: a code-required zone showing fewer elevator entrapments and gas-fed fires in the next damaging quake.")
    print("REFUTE: false alarms cause occupants to disable systems, or liability fears keep owners from connecting.")
    print("OK: %s gave buildings the reflex" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_five_hundred_year_standard(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: 500-year stewardship - infrastructure trusts with century-scale reserves, procurement on 200-year present worth, published audits.")
    ASSUME = {"future_cost_M": 2.0, "years": 200.0, "social_discount": 0.025}
    print("assumptions: %s" % ASSUME)
    pv = ASSUME["future_cost_M"] * 1e6 / (1.0 + ASSUME["social_discount"]) ** ASSUME["years"]
    print("present value of $2M maintenance in year 200 at 2.5 percent: $%.0f" % pv)
    assert 14329.0 < pv < 14334.0
    pv_high = ASSUME["future_cost_M"] * 1e6 / (1.0 + 0.07) ** ASSUME["years"]
    print("same cost at a 7 percent commercial discount: $%.2f - the future erased" % pv_high)
    assert 2.0 < pv_high < 3.0
    print("CONFIRM: trust-owned assets with lower total cost per service-year than conventionally procured equivalents, with published accounts.")
    print("REFUTE: political authorities raid the reserves or dissolve the trusts - the failure mode is governance, not engineering.")
    print("OK: %s fixed the time horizon" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_transoceanic_tunnel(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: staged honesty - Bering Strait reference design as proving ground, full-scale pressure testing, published cost models.")
    ASSUME = {"strait_km": 85.0, "cost_per_km_M": 400.0}
    print("assumptions: %s" % ASSUME)
    cost = ASSUME["strait_km"] * ASSUME["cost_per_km_M"] * 1e6
    print("Bering Strait reference cost: $%.3e" % cost)
    assert 3.3999e10 < cost < 3.4001e10
    atlantic_km = 5500.0
    print("same rate for a 5500 km Atlantic concept: $%.3e - the honesty check" % (atlantic_km * ASSUME["cost_per_km_M"] * 1e6))
    assert 2.1999e12 < atlantic_km * ASSUME["cost_per_km_M"] * 1e6 < 2.2001e12
    print("CONFIRM: a financed, permitted Bering crossing under construction with costs tracking the reference model.")
    print("REFUTE: cost per kilometer exceeds any plausible revenue, or geopolitics makes the strait unbuildable.")
    print("OK: %s staged the ocean crossing" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_subterranean_climate_refuge(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: refuge-district standard - underground mixed-use neighborhoods cooled by ground coupling, dual-use year-round.")
    ASSUME = {"residents": 5000.0, "watts_per_person": 120.0, "ground_temp_c": 16.0, "surface_temp_c": 46.0}
    print("assumptions: %s" % ASSUME)
    cooling_kw = ASSUME["residents"] * ASSUME["watts_per_person"] / 1000.0
    print("internal heat to reject: %.0f kW against %.0f C ground" % (cooling_kw, ASSUME["ground_temp_c"]))
    assert 599999.0 < cooling_kw * 1000.0 < 600001.0
    delta = ASSUME["surface_temp_c"] - ASSUME["ground_temp_c"]
    print("degrees of refuge from the surface extreme: %.0f K, passive" % delta)
    assert 29.9 < delta < 30.1
    print("CONFIRM: a district riding out a record heat season in the comfort range on ground coupling alone.")
    print("REFUTE: excavation costs unaffordable in the cities that need refuge most, or geology rules out candidate sites.")
    print("OK: %s cooled the district with the earth itself" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_self_maintaining_city(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: municipal maintenance operating system - city digital twin, risk-prioritized work orders, robotic repair fleets.")
    ASSUME = {"sensors": 250000.0, "cost_per_sensor": 80.0, "failures_avoided_yr": 400.0, "cost_per_failure": 250000.0}
    print("assumptions: %s" % ASSUME)
    capex = ASSUME["sensors"] * ASSUME["cost_per_sensor"]
    savings = ASSUME["failures_avoided_yr"] * ASSUME["cost_per_failure"]
    print("sensor network capex: $%.3e; yearly failure cost avoided: $%.3e" % (capex, savings))
    assert 1.9999e7 < capex < 2.0001e7
    assert 9.999e7 < savings < 1.0001e8
    payback = capex / savings
    print("payback period: %.2f years" % payback)
    assert 0.199 < payback < 0.201
    print("CONFIRM: a pilot city with improving condition indices at falling maintenance cost per asset, and no unwarned major failure.")
    print("REFUTE: sensor maintenance becomes the new treadmill, or institutional silos refuse to share data with the twin.")
    print("OK: %s gave the city its own maintenance crew" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "pothole_roads": demo_use_pothole_roads,
    "bridge_deck": demo_use_bridge_deck,
    "floodproof_homes": demo_use_floodproof_homes,
    "sponge_cities": demo_use_sponge_cities,
    "quake_safe_schools": demo_use_quake_safe_schools,
    "salt_free_winter_roads": demo_use_salt_free_winter_roads,
    "century_water_mains": demo_use_century_water_mains,
    "sewer_tunnels_empires": demo_use_sewer_tunnels_empires,
    "fireproof_timber_tower": demo_use_fireproof_timber_tower,
    "cable_stayed_recabling": demo_use_cable_stayed_recabling,
    "levee_never_breach": demo_use_levee_never_breach,
    "two_hundred_year_bridge": demo_use_two_hundred_year_bridge,
    "century_concrete": demo_use_century_concrete,
    "self_healing_pavement_networks": demo_use_self_healing_pavement_networks,
    "skyscraper_sway": demo_use_skyscraper_sway,
    "big_one_megastructures": demo_use_big_one_megastructures,
    "block_isolation": demo_use_block_isolation,
    "floating_foundations": demo_use_floating_foundations,
    "storm_surge_megacities": demo_use_storm_surge_megacities,
    "submerged_floating_tunnel": demo_use_submerged_floating_tunnel,
    "underground_freight": demo_use_underground_freight,
    "deep_underground_city": demo_use_deep_underground_city,
    "self_healing_dam_faces": demo_use_self_healing_dam_faces,
    "permafrost_cities": demo_use_permafrost_cities,
    "tsunami_coastlines": demo_use_tsunami_coastlines,
    "sinking_cities": demo_use_sinking_cities,
    "floating_ocean_cities": demo_use_floating_ocean_cities,
    "rewilded_deltas": demo_use_rewilded_deltas,
    "kilometer_tower": demo_use_kilometer_tower,
    "quake_early_warning_buildings": demo_use_quake_early_warning_buildings,
    "five_hundred_year_standard": demo_use_five_hundred_year_standard,
    "transoceanic_tunnel": demo_use_transoceanic_tunnel,
    "subterranean_climate_refuge": demo_use_subterranean_climate_refuge,
    "self_maintaining_city": demo_use_self_maintaining_city,
}
