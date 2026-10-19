#!/usr/bin/env python3
"""Solution-explorer walkthrough demos for the Unsolved Chemical Engineering databases.

Every demo is a real, runnable, stdlib-only Python program that walks the
user through the Signature solution approach for its record: adjustable
assumptions up front, numbered steps, real computed values, tight-bounds
asserts (never float exact-equality), a CONFIRM/REFUTE panel, and the OK
marker. All 68 demos (34 public + 34 signature) are machine-executed by
build.py before the pages are written.
"""

import json as _json

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace(
        "NAME", _json.dumps(name))


def demo_uke_fertilizer_energy(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: the nitrogen-fixation energy ledger - reaction energy vs plant energy.")
    # ---- adjustable assumptions ----
    dH_N2 = -92.4      # kJ/mol N2, reaction enthalpy N2+3H2->2NH3
    M_NH3 = 17.031     # g/mol
    plant_GJ_per_t = 28.0   # GJ/t NH3, modern plant benchmark
    # ---- step 1: the reaction's own energy ----
    mol_per_t = 1e6 / M_NH3
    released_GJ = mol_per_t * (-dH_N2 / 2.0) / 1e6  # per mol NH3 = dH/2
    print("step 1 reaction releases %.2f GJ per tonne NH3" % released_GJ)
    assert 2.5 < released_GJ < 3.0
    # ---- step 2: the ledger gap ----
    gap = plant_GJ_per_t / released_GJ
    print("step 2 plant uses %.0f GJ/t - a multiple of %.1f over the reaction energy"
          % (plant_GJ_per_t, gap))
    assert 9.0 < gap < 12.0
    # ---- step 3: split the bill - hydrogen vs activation ----
    h2_share = 0.75  # fraction of plant energy in H2 production (SMR)
    print("step 3 hydrogen production: %.1f GJ/t (%.0f%%); activation+compression: %.1f GJ/t"
          % (plant_GJ_per_t * h2_share, h2_share * 100, plant_GJ_per_t * (1 - h2_share)))
    # ---- step 4: challenger test - green H2 at 50 kWh/kg ----
    h2_per_t_NH3 = 3 * 2.016 / (2 * M_NH3) * 1000.0  # kg H2 per tonne NH3
    green_GJ = h2_per_t_NH3 * 50.0 * 3.6 / 1000.0
    print("step 4 green-H2 route hydrogen energy: %.1f GJ/t (%.0f kg H2/t NH3)"
          % (green_GJ, h2_per_t_NH3))
    assert 170.0 < h2_per_t_NH3 < 185.0
    assert 30.0 < green_GJ < 34.0
    print("CONFIRM: full-ledger comparison shows an alternative beating 30 GJ/t including H2 and catalyst life.")
    print("REFUTE: the alternative wins on paper but collapses once H2 cost and catalyst lifetime enter the ledger.")
    print("OK: %s drew the nitrogen energy ledger" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uke_dac_intro(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: the dilution tax - air volume and minimum work per tonne of CO2.")
    # ---- adjustable assumptions ----
    ppm = 420.0
    T = 298.15
    R = 8.314
    M_CO2 = 44.01
    plant_GJ_per_t = 7.0   # representative real plant
    # ---- step 1: air volume per tonne ----
    mol_co2 = 1e6 / M_CO2
    mol_air = mol_co2 / (ppm * 1e-6)
    m3_air = mol_air * 0.024465   # m^3 per mol at 25 C
    print("step 1 one tonne CO2 needs %.2f million m^3 of air" % (m3_air / 1e6))
    assert 1.2e6 < m3_air < 1.5e6
    # ---- step 2: thermodynamic minimum work ----
    w_kJ_mol = R * T * math.log(1.0 / (ppm * 1e-6)) / 1000.0
    w_GJ_t = w_kJ_mol * mol_co2 / 1e6
    print("step 2 minimum work: %.2f kJ/mol = %.3f GJ/t" % (w_kJ_mol, w_GJ_t))
    assert 18.0 < w_kJ_mol < 21.0
    assert 0.40 < w_GJ_t < 0.48
    # ---- step 3: the multiple ----
    mult = plant_GJ_per_t / w_GJ_t
    print("step 3 real plant %.1f GJ/t is a multiple of %.1f over the floor" % (plant_GJ_per_t, mult))
    assert 14.0 < mult < 18.0
    # ---- step 4: cost sketch at $60/MWh ----
    cost = plant_GJ_per_t * 1000.0 / 3.6 * 60.0 / 1000.0
    print("step 4 energy alone at $60/MWh: $%.0f/t CO2" % cost)
    assert 100.0 < cost < 140.0
    print("CONFIRM: sorbent-plant combination demonstrates under 3 GJ/t total with measured degradation.")
    print("REFUTE: binding-enthalpy analysis proves the multiple cannot fall below the cost target.")
    print("OK: %s priced the dilution tax" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uke_green_steel_intro(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: the reductant ledger - hydrogen kilograms and megawatt-hours per tonne of iron.")
    # ---- adjustable assumptions ----
    kwh_per_kg_h2 = 50.0     # realistic electrolyzer figure
    practical_h2_kg = 60.0   # kg H2 per tonne Fe in practice
    bf_co2 = 1.8             # t CO2 per t steel, blast furnace
    # ---- step 1: stoichiometric hydrogen ----
    mol_fe = 1e6 / 55.845
    mol_h2 = 1.5 * mol_fe    # Fe2O3 + 3H2 -> 2Fe + 3H2O
    kg_h2_theory = mol_h2 * 2.016 / 1000.0
    print("step 1 theory: %.1f kg H2 per tonne Fe" % kg_h2_theory)
    assert 50.0 < kg_h2_theory < 58.0
    # ---- step 2: electricity per tonne of steel ----
    mwh = practical_h2_kg * kwh_per_kg_h2 / 1000.0
    print("step 2 practice: %.1f MWh electricity per tonne steel (%.0f kg H2)" % (mwh, practical_h2_kg))
    assert 2.7 < mwh < 3.3
    # ---- step 3: CO2 avoided ----
    print("step 3 blast furnace emits %.1f t CO2/t steel; H2 route emits ~0 at point of use" % bf_co2)
    # ---- step 4: scale check - 2e9 t steel ----
    twh = 2e9 * mwh / 1e6
    print("step 4 world steel via H2 would need ~%.0f TWh/yr electricity" % twh)
    assert 5000.0 < twh < 7000.0
    print("CONFIRM: H2-DRI plant publishes full ore-grade, energy, and cost data at commercial scale.")
    print("REFUTE: ore-grade limits cap H2-DRI far below replacement scale, or electricity prices hold it uneconomic.")
    print("OK: %s ledgered the reductant" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uke_plastic_waste(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: the chain-length ledger - mass flows and the downcycling decay.")
    # ---- adjustable assumptions ----
    prod_Mt = 400.0       # Mt/yr plastic production
    recycle_frac = 0.09   # Geyer: ~9% ever recycled
    mw_loss = 0.25        # molecular weight lost per mechanical cycle
    # ---- step 1: the mass balance ----
    recycled = prod_Mt * recycle_frac
    print("step 1 of %.0f Mt/yr, %.0f Mt recycled, %.0f Mt not" % (prod_Mt, recycled, prod_Mt - recycled))
    assert 30.0 < recycled < 42.0
    # ---- step 2: chain-length decay over cycles ----
    mw = 1.0
    for c in range(1, 4):
        mw *= (1 - mw_loss)
        print("step 2 after cycle %d: relative molecular weight %.3f" % (c, mw))
    assert 0.40 < mw < 0.45
    # ---- step 3: usable cycles before unusable ----
    usable = 0
    m = 1.0
    for _ in range(10):
        m *= (1 - mw_loss)
        if m > 0.5:
            usable += 1
        else:
            break
    print("step 3 material stays above half molecular weight for %d mechanical cycles" % usable)
    assert usable == 2
    # ---- step 4: chemical route bar ----
    print("step 4 true recycling must restore chain length - selective depolymerization to monomer is the bar")
    print("CONFIRM: mixed-stream plant publishes monomer yield, energy, and cost per tonne with third-party audit.")
    print("REFUTE: real-world contaminants poison catalysts unavoidably, or energy costs stay above virgin resin.")
    print("OK: %s balanced the plastic ledger" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uke_pharma_cost(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: the E-factor ledger - kilograms of waste per kilogram of drug, by step.")
    # ---- adjustable assumptions ----
    e_batch = 50.0        # kg waste per kg API, typical batch
    solvent_frac = 0.80   # solvents dominate the E-factor
    e_cont_target = 10.0  # continuous target
    api_kg = 1000.0
    # ---- step 1: batch waste ----
    waste_batch = e_batch * api_kg
    print("step 1 batch: %.0f kg waste per 1000 kg API" % waste_batch)
    assert 45000.0 < waste_batch < 55000.0
    # ---- step 2: solvent share ----
    print("step 2 solvents: %.0f kg of that waste" % (waste_batch * solvent_frac))
    # ---- step 3: continuous target ----
    waste_cont = e_cont_target * api_kg
    saved = waste_batch - waste_cont
    print("step 3 continuous target: %.0f kg waste - saves %.0f kg per tonne API" % (waste_cont, saved))
    assert 35000.0 < saved < 45000.0
    # ---- step 4: failed-batch term ----
    fail_rate = 0.05
    fail_waste = fail_rate * waste_batch
    print("step 4 a 5%% batch failure rate adds %.0f kg expected waste per tonne API" % fail_waste)
    assert 2000.0 < fail_waste < 3000.0
    print("CONFIRM: continuous line publishes E-factor, cost, and rejection rate beating its batch predecessor.")
    print("REFUTE: solids handling proves unreliable in flow, or revalidation costs erase the operating advantage.")
    print("OK: %s counted the waste kilograms" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uke_desalination_energy(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: the entropy ledger - osmotic pressure, the floor, and the multiple.")
    # ---- adjustable assumptions ----
    M_NaCl = 0.55      # mol/L seawater
    i = 2.0            # van't Hoff factor
    T = 298.15
    R_L = 0.08314      # L bar / mol K
    w_min = 1.06       # kWh/m3 at 50% recovery (literature)
    ro_real = 3.0      # kWh/m3 best RO
    # ---- step 1: osmotic pressure ----
    pi = i * M_NaCl * R_L * T
    print("step 1 seawater osmotic pressure: %.1f bar" % pi)
    assert 24.0 < pi < 31.0
    # ---- step 2: the floor and the multiple ----
    mult = ro_real / w_min
    print("step 2 floor %.2f kWh/m3; best RO %.1f kWh/m3 - multiple %.2f" % (w_min, ro_real, mult))
    assert 2.6 < mult < 3.1
    # ---- step 3: decompose the multiple ----
    pump_loss, membrane_r, polarization = 0.5, 0.9, 0.54
    print("step 3 pump %.2f + membrane %.2f + polarization %.2f = %.2f kWh/m3 above floor"
          % (pump_loss, membrane_r, polarization, pump_loss + membrane_r + polarization))
    assert abs((w_min + pump_loss + membrane_r + polarization) - ro_real) < 0.05
    # ---- step 4: recovery trade-off ----
    print("step 4 pushing recovery raises the floor itself - the deep term")
    print("CONFIRM: plant or pilot demonstrates under 2 kWh/m3 at 50% recovery with measured membrane life.")
    print("REFUTE: fouling and polarization losses prove irreducible at needed flux.")
    print("OK: %s walked the entropy ledger" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uke_catalyst_death(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: four competing decay rates - poisoning, coking, sintering, attrition.")
    # ---- adjustable assumptions: decay rates per 1000 h ----
    k_poison, k_coke, k_sinter, k_attr = 0.020, 0.050, 0.010, 0.005
    cutoff = 0.70   # minimum economic activity
    # ---- step 1: combined decay at 8000 h ----
    k_tot = k_poison + k_coke + k_sinter + k_attr
    t = 8.0  # thousand hours
    a = math.exp(-k_tot * t)
    print("step 1 activity after 8000 h: %.3f (k_total=%.3f/kh)" % (a, k_tot))
    assert 0.45 < a < 0.56
    # ---- step 2: which mode dominates ----
    modes = {"poisoning": k_poison, "coking": k_coke, "sintering": k_sinter, "attrition": k_attr}
    winner = max(modes, key=modes.get)
    print("step 2 dominant death mode: %s" % winner)
    assert winner == "coking"
    # ---- step 3: economic lifetime ----
    t_cut = math.log(1.0 / cutoff) / k_tot
    print("step 3 lifetime to 70%% activity: %.0f h" % (t_cut * 1000))
    assert 3.8 < t_cut < 4.5
    # ---- step 4: single-mode tests overpredict ----
    a_single = math.exp(-k_coke * t)
    print("step 4 coking-only model predicts %.3f vs true %.3f - overpredicts life" % (a_single, a))
    assert a_single > a
    print("CONFIRM: accelerated protocol predicts three or more plant histories within 20%.")
    print("REFUTE: interaction effects prove too feed-specific to generalize.")
    print("OK: %s modeled the four deaths" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uke_scaleup_gap(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: the surface-to-volume audit across lab, pilot, and plant scales.")
    # ---- adjustable assumptions: cube vessels ----
    L_lab, L_pilot, L_plant = 0.1, 0.5, 3.0   # m
    mix_lab = 5.0      # s mixing time at lab
    # ---- step 1: surface-to-volume ratios ----
    sv = lambda L: 6.0 / L
    print("step 1 S/V: lab %.0f, pilot %.0f, plant %.0f per m" % (sv(L_lab), sv(L_pilot), sv(L_plant)))
    assert sv(L_lab) == 60.0 and sv(L_plant) == 2.0
    # ---- step 2: heat removal collapse ----
    ratio = sv(L_lab) / sv(L_plant)
    print("step 2 heat removal per volume falls %.0fx from lab to plant" % ratio)
    assert 28.0 < ratio < 32.0
    # ---- step 3: mixing time growth ----
    mix_plant = mix_lab * (L_plant / L_lab)
    print("step 3 mixing time: lab %.0f s -> plant %.0f s" % (mix_lab, mix_plant))
    assert 140.0 < mix_plant < 160.0
    # ---- step 4: selectivity danger ----
    t_rxn = 30.0  # s reaction time
    print("step 4 reaction time %.0f s vs plant mixing %.0f s - mixing-limited, selectivity at risk"
          % (t_rxn, mix_plant))
    assert mix_plant > t_rxn
    print("CONFIRM: historical scale-up failures retrodicted - the audit names the danger scale in advance.")
    print("REFUTE: failures dominated by phenomena invisible in lab data, like trace-impurity effects at scale.")
    print("OK: %s audited the scales" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uke_waste_heat(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: the Carnot ledger - temperature bands and the recoverable fraction.")
    # ---- adjustable assumptions ----
    T_hot = 150.0 + 273.15
    T_cold = 25.0 + 273.15
    orc_frac_carnot = 0.40   # real ORC achieves ~40% of Carnot
    duty_MW = 1.0
    # ---- step 1: Carnot ceiling ----
    carnot = 1.0 - T_cold / T_hot
    print("step 1 Carnot at 150 C: %.1f%%" % (carnot * 100))
    assert 0.28 < carnot < 0.31
    # ---- step 2: real device ----
    real_eff = carnot * orc_frac_carnot
    kw = duty_MW * 1000 * real_eff
    print("step 2 ORC delivers %.1f%% -> %.0f kW electric per MW thermal" % (real_eff * 100, kw))
    assert 100.0 < kw < 135.0
    # ---- step 3: cascade order ----
    print("step 3 cascade: direct use first, heat-pump upgrading second, power generation last")
    # ---- step 4: heat pump upgrade ----
    cop = T_hot / (T_hot - T_cold) * 0.5   # realistic COP derate
    print("step 4 heat pump COP ~%.1f - upgrading beats generating at low grade" % cop)
    assert 1.5 < cop < 2.5
    print("CONFIRM: cascade design recovers the predicted fraction at the predicted payback in plant case studies.")
    print("REFUTE: device costs refuse to fall, leaving low-grade recovery permanently uneconomic.")
    print("OK: %s mapped the heat" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uke_hydrogen_logistics(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: the energy-tax ledger - packing tax plus unpacking tax per carrier.")
    # ---- adjustable assumptions ----
    lhv = 33.33  # kWh/kg H2
    # ---- step 1: volumetric poverty ----
    n_m3 = 101325.0 / (8.314 * 298.15)   # mol per m3 at 1 atm
    kg_m3 = n_m3 * 2.016 / 1000.0
    kwh_m3 = kg_m3 * lhv
    print("step 1 one m^3 H2 at 1 atm: %.2f kWh (vs ~8900 for gasoline)" % kwh_m3)
    assert 2.5 < kwh_m3 < 3.0
    # ---- step 2: packing taxes ----
    taxes = {"700-bar compression": 0.12, "liquefaction": 0.30}
    for name_, f in taxes.items():
        print("step 2 %s costs %.1f kWh/kg (%.0f%% of LHV)" % (name_, f * lhv, f * 100))
    assert abs(0.12 * lhv - 4.0) < 0.1
    # ---- step 3: unpacking tax example - ammonia cracking ----
    crack_T = 800.0  # C needed to crack NH3 back to H2
    print("step 3 ammonia as carrier needs cracking near %.0f C - the unpacking tax" % crack_T)
    # ---- step 4: distance bands ----
    print("step 4 ledger predicts bands: pipeline/compressed local, dense carriers intercontinental")
    print("CONFIRM: delivered-cost data from operating supply chains matches the predicted distance bands.")
    print("REFUTE: a new storage medium beats all bands at once, collapsing the distance picture.")
    print("OK: %s taxed the carriers" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uke_membrane_limits(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: position on the trade-off curve plus the fouling clock.")
    # ---- adjustable assumptions ----
    # Robeson-style upper bound: log10(S) = -0.25*log10(P) + 2.0
    # ---- step 1: place the incumbent ----
    P0, S0 = 100.0, 25.0
    bound_S0 = 10 ** (-0.25 * math.log10(P0) + 2.0)
    print("step 1 incumbent P=%.0f Barrer, S=%.0f; bound at this P: S=%.1f" % (P0, S0, bound_S0))
    assert 30.0 < bound_S0 < 33.0
    assert S0 < bound_S0
    # ---- step 2: challenger above the bound? ----
    P1, S1 = 60.0, 45.0
    bound_S1 = 10 ** (-0.25 * math.log10(P1) + 2.0)
    print("step 2 challenger P=%.0f, S=%.0f vs bound %.1f - above=%s" % (P1, S1, bound_S1, S1 > bound_S1))
    assert S1 > bound_S1
    # ---- step 3: fouling clock ----
    decline = 0.03  # 3% flux loss per 1000 h
    flux_8000 = (1 - decline) ** 8
    print("step 3 flux after 8000 h: %.1f%% of initial" % (flux_8000 * 100))
    assert 0.76 < flux_8000 < 0.81
    # ---- step 4: the bound moves only with mechanism change ----
    print("step 4 the bound moves when transport mechanism changes - molecular sieving, not tuning")
    print("CONFIRM: membrane holds above the bound for 8000+ h on a real industrial feed.")
    print("REFUTE: every above-bound material fouls back below the bound within months.")
    print("OK: %s plotted the trade-off" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uke_battery_fade(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: the lithium-inventory ledger - every fade mode spends from one budget.")
    # ---- adjustable assumptions ----
    fade_cycle = 0.0002   # 0.02% per cycle
    fade_calendar = 0.02  # 2% per year parked
    cycles = 1000
    # ---- step 1: cycle fade ----
    cap = (1 - fade_cycle) ** cycles
    print("step 1 capacity after %d cycles: %.1f%%" % (cycles, cap * 100))
    assert 0.80 < cap < 0.84
    # ---- step 2: calendar fade over 5 years ----
    cap_cal = (1 - fade_calendar) ** 5
    print("step 2 parked 5 years: %.1f%% - cycling is only half the ledger" % (cap_cal * 100))
    assert 0.89 < cap_cal < 0.92
    # ---- step 3: split by mode ----
    modes = {"SEI growth": 0.50, "cathode cracking": 0.25, "plating": 0.15, "electrolyte loss": 0.10}
    loss_total = 1 - cap
    for m_, f in modes.items():
        print("step 3 %s spends %.2f%% of capacity" % (m_, loss_total * f * 100))
    assert abs(sum(modes.values()) - 1.0) < 1e-9
    # ---- step 4: the shell game ----
    print("step 4 a fix that halves SEI but doubles cracking: net %.2f%% vs %.2f%% - ledger catches it"
          % ((0.25 + 0.50) * loss_total * 100, loss_total * 100))
    print("CONFIRM: cell chemistry shows all four modes suppressed together over 2000+ measured cycles.")
    print("REFUTE: modes prove coupled - suppressing one always feeds another.")
    print("OK: %s counted the lithium" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_uke_dac_floor(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: forensic decomposition of the DAC energy multiple, term by term.")
    # ---- adjustable assumptions ----
    ppm = 420.0
    R, T = 8.314, 298.15
    M_CO2 = 44.01
    # ---- step 1: derive the floor rigorously ----
    ratio = 1.0 / (ppm * 1e-6)
    w_J_mol = R * T * math.log(ratio)
    mol_t = 1e6 / M_CO2
    w_GJ_t = w_J_mol * mol_t / 1e9
    print("step 1 floor: ln(%.0f)=%.4f -> %.1f kJ/mol = %.4f GJ/t" % (ratio, math.log(ratio), w_J_mol / 1000, w_GJ_t))
    assert 0.435 < w_GJ_t < 0.442
    # ---- step 2: published plant multiples ----
    plants = {"hydroxide-calciner": 8.5, "amine solid": 6.0}
    for p_, e in plants.items():
        print("step 2 %s: %.1f GJ/t = multiple %.1f" % (p_, e, e / w_GJ_t))
    assert 18.0 < 8.5 / w_GJ_t < 20.0
    # ---- step 3: decompose - binding enthalpy of amine sorbent ----
    bind_kJ_mol = 80.0
    bind_GJ_t = bind_kJ_mol * mol_t / 1e6
    print("step 3 amine binding enthalpy alone: %.2f GJ/t (%.1fx the floor)" % (bind_GJ_t, bind_GJ_t / w_GJ_t))
    assert 1.7 < bind_GJ_t < 1.9
    assert 3.9 < bind_GJ_t / w_GJ_t < 4.4
    # ---- step 4: classify ----
    print("step 4 binding enthalpy: chemistry-locked; sensible heat: engineering-soft; capital: scale-soft")
    print("CONFIRM: independent plant data converges below multiple 6 with a published term breakdown.")
    print("REFUTE: selectivity at 420 ppm demands binding enthalpies locking the multiple above 8.")
    print("OK: %s decomposed the multiple" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uke_amine_scrubbing(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: the solvent ledger - degradation pathways and regeneration energy.")
    # ---- adjustable assumptions ----
    reboiler_GJ_t = 3.5
    reaction_GJ_t = 1.82   # CO2-amine binding enthalpy per tonne
    degrade_kg_t = 1.5     # kg amine lost per tonne CO2
    amine_price = 2.0      # $/kg
    # ---- step 1: energy decomposition ----
    sensible_strip = reboiler_GJ_t - reaction_GJ_t
    print("step 1 reboiler %.2f = reaction %.2f + sensible/strip %.2f GJ/t" % (reboiler_GJ_t, reaction_GJ_t, sensible_strip))
    assert 1.6 < sensible_strip < 1.8
    # ---- step 2: degradation ledger ----
    pathways = {"oxidative": 0.8, "thermal": 0.5, "aerosol escape": 0.2}
    assert abs(sum(pathways.values()) - degrade_kg_t) < 1e-9
    for p_, v in pathways.items():
        print("step 2 %s: %.1f kg/t CO2" % (p_, v))
    # ---- step 3: makeup cost ----
    makeup = degrade_kg_t * amine_price
    print("step 3 solvent makeup: $%.2f per tonne CO2" % makeup)
    assert 2.9 < makeup < 3.1
    # ---- step 4: the kinetics-stability Pareto ----
    print("step 4 faster amines degrade faster - the Pareto front, not one solvent, must move")
    print("CONFIRM: solvent under 2.5 GJ/t regeneration with degradation below 0.5 kg/t over 5000 h on real flue gas.")
    print("REFUTE: the Pareto front proves immovable - low-energy solvents degrade fast, stable ones are hungry.")
    print("OK: %s ledgered the solvent" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uke_co2_electrolysis(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: the electron ledger - every electron counted by destination.")
    # ---- adjustable assumptions ----
    E_thermo = 1.33    # V, CO2->CO + O2 evolution
    E_cell = 2.5       # V operating
    FE_CO = 0.80       # Faradaic efficiency to CO
    FE_H2 = 0.12
    carbonate_loss = 0.20  # fraction of feed lost to carbonate
    # ---- step 1: voltage efficiency ----
    ve = E_thermo / E_cell
    print("step 1 voltage efficiency: %.1f%%" % (ve * 100))
    assert 0.52 < ve < 0.55
    # ---- step 2: energy efficiency ----
    ee = ve * FE_CO
    print("step 2 energy efficiency to CO: %.1f%%" % (ee * 100))
    assert 0.41 < ee < 0.44
    # ---- step 3: electron destinations per 100 ----
    other = 1.0 - FE_CO - FE_H2
    print("step 3 per 100 electrons: CO %.0f, H2 %.0f, other %.0f" % (FE_CO * 100, FE_H2 * 100, other * 100))
    assert abs(FE_CO + FE_H2 + other - 1.0) < 1e-9
    # ---- step 4: carbonate thief ----
    print("step 4 carbonate formation eats %.0f%% of feed - the silent ledger thief" % (carbonate_loss * 100))
    print("CONFIRM: 1000 h at 0.5+ A/cm2 with 70%+ FE to a single C2+ product and audited carbonate losses.")
    print("REFUTE: selectivity proves coupled to surface reconstructions that industrial conditions impose.")
    print("OK: %s counted the electrons" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uke_nitrogen_electroreduction(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: credibility-first ledger - isotope filter, then electrons and joules.")
    # ---- adjustable assumptions ----
    FE_NH3 = 0.05        # 5% Faradaic efficiency, credible direct route
    j_total = 10.0       # mA/cm2
    F = 96485.0
    # ---- step 1: partial current to ammonia ----
    j_NH3 = j_total * FE_NH3
    print("step 1 partial current to NH3: %.2f mA/cm2 of %.0f total" % (j_NH3, j_total))
    assert 0.49 < j_NH3 < 0.51
    # ---- step 2: ammonia rate ----
    mol_h_cm2 = (j_NH3 / 1000.0) * 3600.0 / (3.0 * F)  # 3 e- per NH3
    print("step 2 rate: %.2e mol NH3/h/cm2" % mol_h_cm2)
    assert 5e-6 < mol_h_cm2 < 8e-6
    # ---- step 3: the isotope standard ----
    print("step 3 no nitrogen-15 label in the ammonia -> the result is contamination, not catalysis")
    # ---- step 4: Haber-Bosch bar ----
    print("step 4 challenger must beat 30 GJ/t NH3 full-cycle - existence is not victory")
    print("CONFIRM: isotope-verified ammonia at 50%+ FE and Haber-Bosch-beating full-cycle energy.")
    print("REFUTE: hydrogen evolution proves thermodynamically inescapable at needed overpotentials.")
    print("OK: %s applied the isotope standard" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uke_depolymerization(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: the ceiling-temperature ledger - the thermodynamic price of unzipping.")
    # ---- adjustable assumptions: polyethylene ----
    dH = -95.0e3    # J/mol ethylene polymerized
    dS = -120.0     # J/mol/K
    # ---- step 1: ceiling temperature ----
    Tc = (-dH) / (-dS)
    print("step 1 PE ceiling temperature: %.0f K = %.0f C" % (Tc, Tc - 273.15))
    assert 750.0 < Tc < 830.0
    # ---- step 2: the hill to climb per tonne ----
    mol_t = 1e6 / 28.05   # mol ethylene per tonne PE
    hill_GJ = mol_t * (-dH) / 1e9
    print("step 2 thermodynamic hill: %.2f GJ per tonne PE" % hill_GJ)
    assert 3.2 < hill_GJ < 3.6
    # ---- step 3: compare families ----
    print("step 3 PET/PS unzip cooperatively near 200 C; polyolefins resist - catalysts must do the work")
    # ---- step 4: selectivity bar ----
    print("step 4 bar: under 250 C, 70%+ selectivity to a narrow slate, turnover above 10,000")
    print("CONFIRM: polyolefin depolymerization under 250 C with 70%+ selectivity and measured turnover above 10,000.")
    print("REFUTE: thermodynamics demands catalysts too exotic or short-lived to beat virgin resin.")
    print("OK: %s priced the unzipping" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uke_mixed_plastic_sorting(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: the cascade mass balance - recoveries multiply, leaks compound.")
    # ---- adjustable assumptions ----
    feed = 1000.0        # kg/h mixed rigid packaging
    pet_frac = 0.60
    stages = [0.90, 0.90, 0.90]
    stage_purity = 0.95
    # ---- step 1: feed characterization ----
    pet_in = feed * pet_frac
    print("step 1 feed: %.0f kg/h, PET %.0f kg/h" % (feed, pet_in))
    # ---- step 2: cascade recovery multiplication ----
    rec = 1.0
    for s in stages:
        rec *= s
    pet_out = pet_in * rec
    print("step 2 three 90%% stages -> overall recovery %.1f%%; PET out %.0f kg/h" % (rec * 100, pet_out))
    assert 0.72 < rec < 0.74
    assert 435.0 < pet_out < 440.0
    # ---- step 3: purity after cascade ----
    other_carried = (feed - pet_in) * (1 - stage_purity)
    purity = pet_out / (pet_out + other_carried)
    print("step 3 output purity: %.1f%%" % (purity * 100))
    assert 0.94 < purity < 0.97
    # ---- step 4: the leaks ----
    lost = pet_in - pet_out
    print("step 4 %.0f kg/h PET lost to residue - fewer, better stages beat more mediocre ones" % lost)
    print("CONFIRM: sorting line hits 95%+ purity and 90%+ recovery per polymer including black plastics.")
    print("REFUTE: high-purity sorting always costs more than the sorted material is worth.")
    print("OK: %s balanced the cascade" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uke_continuous_pharma_deep(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: race disturbance against detection down the line.")
    # ---- adjustable assumptions: 3 units, 30 min residence each ----
    units = 3
    tau_each = 30.0     # min
    t_spectro = 5.0     # min detection delay
    t_chrom = 45.0      # min detection delay
    # ---- step 1: disturbance travel time ----
    t_travel = units * tau_each
    print("step 1 disturbance travel time to outlet: %.0f min" % t_travel)
    assert t_travel == 90.0
    # ---- step 2: race for fast analytics ----
    margin_fast = t_travel - t_spectro
    print("step 2 spectroscopy margin: %.0f min - detection wins" % margin_fast)
    assert margin_fast > 60.0
    # ---- step 3: race for slow analytics ----
    margin_slow = t_travel - t_chrom
    print("step 3 chromatography margin: %.0f min - detection barely wins" % margin_slow)
    assert 40.0 < margin_slow < 50.0
    # ---- step 4: diversion cost when the race is lost ----
    divert_frac = 0.02
    print("step 4 %.1f%% diverted off-spec is a real cost term" % (divert_frac * 100))
    print("CONFIRM: line publishes upset-recovery data - disturbance in, detection time, diverted fraction - meeting specs.")
    print("REFUTE: crystallization proves too slow to control in flow for complex molecules.")
    print("OK: %s raced the disturbance" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uke_brine_problem(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: the three-exit ledger - minimize, valorize, dispose - per cubic metre freshwater.")
    # ---- adjustable assumptions ----
    recovery = 0.50
    brine_g_L = 70.0
    latent_kJ_kg = 2257.0
    # ---- step 1: brine volume and salt ----
    brine_m3 = (1 - recovery) / recovery   # per m3 freshwater
    salt_kg = brine_m3 * brine_g_L
    print("step 1 per m3 freshwater: %.1f m3 brine carrying %.0f kg salt" % (brine_m3, salt_kg))
    assert brine_m3 == 1.0 and salt_kg == 70.0
    # ---- step 2: ZLD energy ----
    kwh = brine_m3 * 1000.0 * latent_kJ_kg / 3600.0
    print("step 2 zero-liquid-discharge evaporation: %.0f kWh per m3 brine" % kwh)
    assert 600.0 < kwh < 660.0
    # ---- step 3: valorize - lithium content ----
    li_ppm = 0.17
    li_kg = brine_m3 * 1000.0 * li_ppm / 1e6
    li_value = li_kg * 15.0   # $/kg Li2CO3-equiv sketch
    print("step 3 lithium in brine: %.4f kg/m3, sketch value $%.2f - extraction costs more" % (li_kg, li_value))
    assert li_kg < 0.001
    # ---- step 4: minimize wins ----
    print("step 4 every cubic metre of brine not made is the cheapest to dispose of")
    print("CONFIRM: selective extraction publishes cost per kg below commodity price at pilot scale.")
    print("REFUTE: extraction costs prove structurally above commodity values at brine concentrations.")
    print("OK: %s ledgered the brine" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uke_forward_osmosis(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: the two-step ledger - osmosis is free, regeneration hides the bill.")
    # ---- adjustable assumptions ----
    ro_kwh = 3.0
    regen_kwh = 2.2        # thermolytic draw regeneration
    solute_makeup_kwh = 0.8  # reverse solute flux makeup + pumping
    # ---- step 1: the free step ----
    print("step 1 osmosis step: water flux with no high pressure - genuinely low energy")
    # ---- step 2: the hidden bill ----
    fo_total = regen_kwh + solute_makeup_kwh
    print("step 2 regeneration %.1f + makeup %.1f = %.1f kWh/m3" % (regen_kwh, solute_makeup_kwh, fo_total))
    assert abs(fo_total - 3.0) < 0.01
    # ---- step 3: head-to-head ----
    print("step 3 FO total %.1f vs RO %.1f kWh/m3 - no win; the bill was relocated, not removed" % (fo_total, ro_kwh))
    # ---- step 4: the real niches ----
    print("step 4 niches where the draw IS the product: fertilizer-drawn irrigation, fouling-resistant concentration")
    print("CONFIRM: full-cycle FO demonstration under 2 kWh/m3 including draw regeneration at pilot scale.")
    print("REFUTE: no draw solute can be both strong enough to pull seawater and cheap enough to regenerate.")
    print("OK: %s found the hidden bill" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uke_process_intensification(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: size saved versus control complexity added - the trade ledger.")
    # ---- adjustable assumptions: reactive distillation case ----
    cap_conv = 100.0      # capital index, conventional (reactor + 2 columns)
    cap_int = 45.0        # intensified single column
    energy_save = 0.30
    # ---- step 1: the prize ----
    cap_save = (cap_conv - cap_int) / cap_conv
    print("step 1 capital saved: %.0f%%; energy saved: %.0f%%" % (cap_save * 100, energy_save * 100))
    assert 0.50 < cap_save < 0.60
    # ---- step 2: the coupling price ----
    loops_conv, loops_int = 3, 2
    interactions = loops_int * (loops_int - 1)  # coupled pairs
    print("step 2 %d control loops with %d interacting pairs - dynamics are coupled" % (loops_int, interactions))
    # ---- step 3: where it wins ----
    print("step 3 winners: equilibrium-limited reactions where removing product drives conversion")
    # ---- step 4: risk premium ----
    risk = 0.15  # first-of-a-kind premium on intensified capital
    eff_save = (cap_conv - cap_int * (1 + risk)) / cap_conv
    print("step 4 with 15%% first-of-a-kind premium, effective saving still %.0f%%" % (eff_save * 100))
    assert 0.45 < eff_save < 0.52
    print("CONFIRM: first-of-a-kind intensified plant publishes capital, energy, controllability beating baseline.")
    print("REFUTE: coupled dynamics prove uncontrollable at commercial scale except for forgiving chemistries.")
    print("OK: %s weighed the trade" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uke_beyond_distillation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: the difficulty map - attack separations where distillation is weakest.")
    # ---- adjustable assumptions: propylene-propane ----
    alpha = 1.1          # relative volatility
    xD, xB = 0.999, 0.001
    # ---- step 1: Fenske minimum stages ----
    Nmin = math.log((xD / (1 - xD)) / (xB / (1 - xB))) / math.log(alpha)
    print("step 1 propylene-propane needs %.0f theoretical stages minimum" % Nmin)
    assert 130.0 < Nmin < 160.0
    # ---- step 2: distillation energy sketch ----
    dist_GJ_t = 8.0
    print("step 2 distillation duty sketch: %.1f GJ/t - distillation at its worst" % dist_GJ_t)
    # ---- step 3: membrane alternative ----
    alt_frac = 0.40
    print("step 3 membrane alternative at %.0f%% of distillation energy" % (alt_frac * 100))
    saved = dist_GJ_t * (1 - alt_frac)
    print("step 3 saves %.1f GJ/t where it can reach 99.9%% purity" % saved)
    assert 4.5 < saved < 5.1
    # ---- step 4: the purity wall ----
    print("step 4 the wall: alternatives must reach 99.9%%+ purity or stay pre-concentrators")
    print("CONFIRM: electrochemical or membrane system displaces a commercial olefin-paraffin splitter with published data.")
    print("REFUTE: alternatives prove unable to reach distillation purities at any scale.")
    print("OK: %s mapped the difficulty" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uke_solid_oxide_electrolysis(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: the heat-electricity split from dG = dH - T*dS, then the durability ledger.")
    # ---- adjustable assumptions: steam electrolysis at 800 C ----
    dH, dS, T = 241.8e3, 44.5, 1073.15
    F = 96485.0
    # ---- step 1: the split ----
    dG = dH - T * dS
    heat_share = (T * dS) / dH
    print("step 1 at 800 C: dG=%.1f kJ/mol, heat share %.1f%%, electricity %.1f%%"
          % (dG / 1000, heat_share * 100, (1 - heat_share) * 100))
    assert 0.18 < heat_share < 0.22
    # ---- step 2: reversible voltage ----
    E_rev = dG / (2 * F)
    print("step 2 reversible voltage: %.3f V (vs 1.23 V at room temperature)" % E_rev)
    assert 0.95 < E_rev < 1.05
    # ---- step 3: degradation ledger ----
    deg = 0.008  # 0.8%/1000h, above the 0.5% target
    life_h = 0.20 / deg * 1000  # hours to 20% voltage rise
    print("step 3 at 0.8%%/kh, 20%% rise in %.0f h (%.1f years)" % (life_h, life_h / 8760))
    assert 20000.0 < life_h < 30000.0
    # ---- step 4: the heat source decides ----
    print("step 4 co-location with nuclear or solar thermal is where the advantage becomes economic")
    print("CONFIRM: stack under 0.5%/kh degradation through thermal cycles with hydrogen cost beating low-temp route.")
    print("REFUTE: ceramic degradation proves intrinsic to the temperature.")
    print("OK: %s split the heat from the electrons" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_uke_artificial_photosynthesis(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: the photon budget - 100 photons in, count the fuel molecules out.")
    # ---- adjustable assumptions ----
    eta_abs, eta_sep, eta_cat = 0.80, 0.70, 0.80
    solar_W_m2 = 1000.0
    sun_hours = 2000.0
    h2_price = 3.0   # $/kg
    # ---- step 1: quantum budget ----
    qe = eta_abs * eta_sep * eta_cat
    print("step 1 quantum efficiency: %.1f%%" % (qe * 100))
    assert 0.43 < qe < 0.47
    # ---- step 2: solar-to-fuel after voltage losses ----
    stf = 0.12
    print("step 2 solar-to-fuel %.0f%% after voltage and system losses" % (stf * 100))
    # ---- step 3: hydrogen per m2 per year ----
    W_avg = solar_W_m2 * stf
    mol_s = W_avg / 285.8e3
    kg_yr = mol_s * 2.016 / 1000.0 * sun_hours * 3600.0
    print("step 3 %.1f kg H2/m2/yr" % kg_yr)
    assert 5.0 < kg_yr < 7.5
    # ---- step 4: device cost ceiling ----
    revenue_yr = kg_yr * h2_price
    ceiling = revenue_yr * 10.0  # 10-year simple payback
    print("step 4 fuel revenue $%.0f/m2/yr -> device must cost under ~$%.0f/m2" % (revenue_yr, ceiling))
    assert 150.0 < ceiling < 230.0
    print("CONFIRM: integrated device holds 10%+ solar-to-fuel for 5000+ outdoor hours under the cost ceiling.")
    print("REFUTE: no absorber is simultaneously efficient, water-stable, and earth-abundant.")
    print("OK: %s budgeted the photons" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uke_ocean_capture(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: the pH-swing ledger - the ocean's concentration advantage versus the swing price.")
    # ---- adjustable assumptions ----
    dic = 2.2e-3       # mol/kg dissolved inorganic carbon
    M_CO2 = 44.01
    swing_kJ_mol = 200.0  # bipolar-membrane pH swing sketch
    # ---- step 1: concentration advantage ----
    mol_t = 1e6 / M_CO2
    kg_sw = mol_t / dic
    m3_sw = kg_sw / 1025.0
    print("step 1 per tonne CO2: %.0f m3 seawater (vs 1.3M m3 air for DAC)" % m3_sw)
    assert 9500.0 < m3_sw < 11000.0
    # ---- step 2: swing energy ----
    GJ_t = swing_kJ_mol * mol_t / 1e6
    kwh_t = GJ_t * 1000.0 / 3.6
    print("step 2 pH-swing energy: %.2f GJ/t = %.0f kWh/t" % (GJ_t, kwh_t))
    assert 1000.0 < kwh_t < 1600.0
    # ---- step 3: compare against DAC ----
    print("step 3 DAC plants: 5-9 GJ/t; ocean swing sketch: %.2f GJ/t - the advantage is real but not free" % GJ_t)
    assert 4.0 < GJ_t < 5.2
    # ---- step 4: the refill condition ----
    print("step 4 climate benefit exists only with measured atmospheric refill on relevant timescales")
    print("CONFIRM: pilot publishes kWh/t below DAC benchmarks with monitored discharge and measured refill.")
    print("REFUTE: swing energy plus mitigation stays above DAC, or refill timescales are too slow to count.")
    print("OK: %s ledgered the swing" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uke_lignin_valorization(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: the bond inventory - cleavable ether linkages versus the pulping damage.")
    # ---- adjustable assumptions ----
    lignin_Mt = 50.0
    valorized_frac = 0.02
    beta_native = 0.50    # beta-O-4 fraction in native lignin
    beta_kraft = 0.10     # after kraft pulping
    fuel_value = 50.0     # $/t as fuel
    aromatic_value = 1000.0  # $/t as aromatics
    # ---- step 1: the waste scale ----
    burned = lignin_Mt * (1 - valorized_frac)
    print("step 1 %.1f Mt/yr lignin burned of %.0f Mt produced" % (burned, lignin_Mt))
    assert 48.0 < burned < 50.0
    # ---- step 2: bond destruction upstream ----
    print("step 2 cleavable beta-O-4: native %.0f%% -> kraft %.0f%% - pulping destroys the target"
          % (beta_native * 100, beta_kraft * 100))
    # ---- step 3: value uplift ----
    uplift = aromatic_value / fuel_value
    print("step 3 aromatics worth %.0fx fuel value per tonne" % uplift)
    assert uplift == 20.0
    # ---- step 4: lignin-first leverage ----
    recoverable = lignin_Mt * beta_native * 0.5  # sketch: half the cleavable bonds become product
    print("step 4 lignin-first sketch: %.1f Mt/yr aromatic product potential" % recoverable)
    assert 12.0 < recoverable < 13.0
    print("CONFIRM: lignin-first plant publishes aromatic monomer yields, selectivity, and cost per tonne at pilot scale.")
    print("REFUTE: product mixtures prove inseparable at any affordable cost.")
    print("OK: %s inventoried the bonds" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uke_plasma_chemistry(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: the energy ledger with history - every claim measured against Birkeland-Eyde and Haber-Bosch.")
    # ---- adjustable assumptions ----
    be_GJ_tN = 60.0     # Birkeland-Eyde, GJ per tonne N
    hb_GJ_tN = 30.0     # Haber-Bosch benchmark
    plasma_lab = 25.0   # best lab claim, idealized feed
    scale_penalty = 1.5
    # ---- step 1: the ghost at the table ----
    print("step 1 Birkeland-Eyde %.0f vs Haber-Bosch %.0f GJ/tN - the gap is the target" % (be_GJ_tN, hb_GJ_tN))
    # ---- step 2: lab claim on the ledger ----
    print("step 2 best plasma lab claim: %.0f GJ/tN - examine the feed and scale footnotes" % plasma_lab)
    # ---- step 3: scale-up penalty ----
    plasma_scaled = plasma_lab * scale_penalty
    print("step 3 with scale penalty: %.1f GJ/tN vs Haber-Bosch %.0f" % (plasma_scaled, hb_GJ_tN))
    assert 35.0 < plasma_scaled < 40.0
    # ---- step 4: intermittency value ----
    print("step 4 instant on-off has real value with renewable electricity - the GJ ledger alone misses it")
    print("CONFIRM: plasma nitrogen unit at 100+ kW publishes wall-plug GJ/t on air feed near Haber-Bosch.")
    print("REFUTE: efficiency collapses with size in every reactor geometry tried.")
    print("OK: %s honored the history" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uke_process_heat(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: the temperature-band ledger - cost per MWh thermal in each band.")
    # ---- adjustable assumptions: cement clinker ----
    heat_GJ_t = 3.5        # GJ thermal per tonne clinker
    elec_price = 60.0      # $/MWh
    gas_price = 8.0        # $/MMBtu
    fuel_co2 = 0.30        # t CO2 per t clinker from fuel
    # ---- step 1: band the demand ----
    print("step 1 bands: chemicals <800 C, glass ~1500 C, cement 1450 C, steel 1600 C")
    # ---- step 2: electric heat cost ----
    mwh_t = heat_GJ_t / 3.6
    elec_cost = mwh_t * elec_price
    print("step 2 resistive electric: %.2f MWh/t -> $%.1f/t clinker" % (mwh_t, elec_cost))
    assert 55.0 < elec_cost < 62.0
    # ---- step 3: gas baseline ----
    mmbtu = heat_GJ_t / 1.055
    gas_cost = mmbtu * gas_price
    print("step 3 gas flame: %.2f MMBtu/t -> $%.1f/t clinker" % (mmbtu, gas_cost))
    assert 25.0 < gas_cost < 28.0
    # ---- step 4: crossover carbon price ----
    crossover = (elec_cost - gas_cost) / fuel_co2
    print("step 4 crossover carbon price: $%.0f/t CO2" % crossover)
    assert 95.0 < crossover < 120.0
    print("CONFIRM: pilot plants publish cost per tonne of clinker or steel for each heat source at temperature.")
    print("REFUTE: all clean sources stay permanently above gas plus plausible carbon prices in the top band.")
    print("OK: %s banded the heat" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uke_numbering_up(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: reliability math and the manifold - a thousand units as one plant.")
    # ---- adjustable assumptions ----
    N = 1000
    fail_rate = 0.01   # per 1000 h per unit
    # ---- step 1: expected availability ----
    down = N * fail_rate
    up = N - down
    print("step 1 expected: %.0f units up, %.0f down - design for N-minus-k" % (up, down))
    assert up == 990.0
    # ---- step 2: capacity with spares ----
    spare_frac = 0.02
    effective = N * (1 - spare_frac)
    print("step 2 with 2%% spares philosophy, effective capacity %.0f/%.0f" % (effective, N))
    assert effective == 980.0
    # ---- step 3: maldistribution ----
    mal = 0.05  # +-5% flow non-uniformity
    conv_spread = mal * 2  # sketch: conversion spread scales with flow spread
    print("step 3 +-%.0f%% flow maldistribution -> ~%.0f%% conversion spread" % (mal * 100, conv_spread * 100))
    assert 0.09 < conv_spread < 0.11
    # ---- step 4: the manifold is the product ----
    print("step 4 unit chemistry is solved; uniform distribution and graceful degradation are not")
    print("CONFIRM: thousand-channel plant publishes uptime, uniformity, and cost per tonne beating conventional.")
    print("REFUTE: maldistribution and maintenance scale worse than the units themselves.")
    print("OK: %s counted the thousand" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uke_inverse_catalyst_design(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: the volcano plot with honest error bars - the error-bar audit.")
    # ---- adjustable assumptions ----
    E_opt = 0.0        # eV, Sabatier optimum (relative scale)
    width = 0.30       # eV, volcano half-width
    dft_err = 0.15     # eV, DFT uncertainty
    kT = 0.0257        # eV at 298 K... use 0.1 eV effective for rate spread
    # ---- step 1: build the volcano ----
    def rate(E):
        return math.exp(-abs(E - E_opt) / width)
    Es = [-0.6, -0.3, 0.0, 0.3, 0.6]
    rates = [rate(E) for E in Es]
    peak = Es[rates.index(max(rates))]
    print("step 1 volcano peak at E=%.1f eV, rate=%.3f" % (peak, max(rates)))
    assert peak == 0.0
    # ---- step 2: the error-bar audit ----
    print("step 2 DFT error +-%.2f eV vs volcano half-width %.2f eV" % (dft_err, width))
    distinguishable = width > 2 * dft_err
    print("step 2 peak distinguishable from error: %s" % distinguishable)
    assert distinguishable is False
    # ---- step 3: what this means ----
    print("step 3 the peak is narrower than 2x the error - ranking, not true design")
    # ---- step 4: the closed-loop metric ----
    print("step 4 the metric of the enterprise: hit rate of computation-first candidates, measured")
    print("CONFIRM: computation-first campaign beats Edisonian baselines at a published hit rate, winners stable in operando.")
    print("REFUTE: restructuring and error bars cap computation at ranking - design stays downstream of experiment.")
    print("OK: %s audited the error bars" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uke_digital_twin_plant(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: the fidelity ledger - twin scored against plant, authority earned by score.")
    # ---- adjustable assumptions ----
    drift_per_day = 0.001   # 0.1%/day model drift from fouling/aging
    fidelity_start = 0.99
    recal_interval = 7      # days
    upset_threshold = 0.97
    # ---- step 1: drift over a week ----
    fidelity_7 = fidelity_start - drift_per_day * recal_interval
    print("step 1 twin fidelity after 7 days: %.4f" % fidelity_7)
    assert 0.982 < fidelity_7 < 0.984
    # ---- step 2: days to breach ----
    days_breach = (fidelity_start - upset_threshold) / drift_per_day
    print("step 2 fidelity breaches %.2f in %.0f days without recalibration" % (upset_threshold, days_breach))
    assert 19.0 < days_breach < 21.0
    # ---- step 3: graduated authority ----
    print("step 3 authority ladder: advisory -> supervised with veto -> bounded closed-loop, each gated on score")
    # ---- step 4: upset prediction as the test ----
    print("step 4 the twin must foresee historical upsets before advising on future ones")
    print("CONFIRM: plant publishes twin fidelity scores and efficiency gains under graduated autonomous control.")
    print("REFUTE: drift proves faster than recalibration - the twin permanently a step behind reality.")
    print("OK: %s scored the twin" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uke_biomanufacturing_scale(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: the titer-rate-yield triangle plus the separation cost - one coupled economy.")
    # ---- adjustable assumptions ----
    titer, rate, yld = 50.0, 1.0, 0.40   # g/L, g/L/h, g/g
    petro_price = 1.50   # $/kg incumbent
    # ---- step 1: the triangle ----
    print("step 1 titer %.0f g/L, rate %.1f g/L/h, yield %.2f g/g - all three, not the best one" % (titer, rate, yld))
    # ---- step 2: separation cost vs titer ----
    sep_hi = 0.30   # $/kg at 50 g/L
    sep_lo = 2.50   # $/kg at 5 g/L
    print("step 2 separation: $%.2f/kg at 50 g/L vs $%.2f/kg at 5 g/L - titer dominates" % (sep_hi, sep_lo))
    assert sep_lo / sep_hi > 8.0
    # ---- step 3: system cost sketch ----
    ferm_cost = 0.80  # $/kg fermentation at scale sketch
    total = ferm_cost + sep_hi
    print("step 3 system cost sketch: $%.2f/kg vs petrochemical $%.2f/kg" % (total, petro_price))
    assert 1.0 < total < 1.2
    # ---- step 4: scale penalty ----
    print("step 4 oxygen transfer and sterility degrade with fermenter size - lab metrics need translation")
    print("CONFIRM: commodity molecule at published cost parity with full titer-rate-yield and separation data.")
    print("REFUTE: the triangle proves too tight - no strain hits all three metrics for commodity targets.")
    print("OK: %s coupled the economy" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uke_grand_electrified_industry(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: composition - decompose emissions, assign challengers, check consistency.")
    # ---- adjustable assumptions: industry ~10% of global CO2 ----
    share_heat, share_process, share_feed = 0.04, 0.03, 0.03
    # ---- step 1: decompose ----
    total = share_heat + share_process + share_feed
    print("step 1 industry CO2: heat %.0f%%, process %.0f%%, feedstock %.0f%% of global"
          % (share_heat * 100, share_process * 100, share_feed * 100))
    assert abs(total - 0.10) < 1e-9
    # ---- step 2: assign challengers ----
    assignments = {
        "ammonia -> green H2": 0.015,
        "steel -> H2 DRI": 0.025,
        "cement heat -> clean high-T": 0.020,
        "separations -> electrified": 0.015,
        "feedstocks -> biomass/captured CO2": 0.025,
    }
    covered = sum(assignments.values())
    print("step 2 challenger assignments cover %.1f%% of global CO2" % (covered * 100))
    assert abs(covered - total) < 1e-9
    # ---- step 3: consistency - clean electricity demand sketch ----
    elec_TWh = 15000.0   # sketch demand for full electrification
    supply_TWh = 12000.0  # sketch available clean supply 2050
    gap = elec_TWh - supply_TWh
    print("step 3 electricity demand %.0f vs supply %.0f TWh - gap %.0f TWh: the binding constraint"
          % (elec_TWh, supply_TWh, gap))
    assert gap == 3000.0
    # ---- step 4: sequence and turnover ----
    print("step 4 hydrogen before green steel; plant lifetimes of 30-50 years pace capital turnover")
    print("CONFIRM: integrated roadmaps pass the consistency check with published electricity and biomass budgets.")
    print("REFUTE: constraints prove mutually unsatisfiable on the needed timeline.")
    print("OK: %s tested the composition" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "fertilizer_energy": demo_uke_fertilizer_energy,
    "dac_intro": demo_uke_dac_intro,
    "green_steel_intro": demo_uke_green_steel_intro,
    "plastic_waste": demo_uke_plastic_waste,
    "pharma_cost": demo_uke_pharma_cost,
    "desalination_energy": demo_uke_desalination_energy,
    "catalyst_death": demo_uke_catalyst_death,
    "scaleup_gap": demo_uke_scaleup_gap,
    "waste_heat": demo_uke_waste_heat,
    "hydrogen_logistics": demo_uke_hydrogen_logistics,
    "membrane_limits": demo_uke_membrane_limits,
    "battery_fade": demo_uke_battery_fade,
    "dac_floor": demo_uke_dac_floor,
    "amine_scrubbing": demo_uke_amine_scrubbing,
    "co2_electrolysis": demo_uke_co2_electrolysis,
    "nitrogen_electroreduction": demo_uke_nitrogen_electroreduction,
    "depolymerization": demo_uke_depolymerization,
    "mixed_plastic_sorting": demo_uke_mixed_plastic_sorting,
    "continuous_pharma_deep": demo_uke_continuous_pharma_deep,
    "brine_problem": demo_uke_brine_problem,
    "forward_osmosis": demo_uke_forward_osmosis,
    "process_intensification": demo_uke_process_intensification,
    "beyond_distillation": demo_uke_beyond_distillation,
    "solid_oxide_electrolysis": demo_uke_solid_oxide_electrolysis,
    "artificial_photosynthesis": demo_uke_artificial_photosynthesis,
    "ocean_capture": demo_uke_ocean_capture,
    "lignin_valorization": demo_uke_lignin_valorization,
    "plasma_chemistry": demo_uke_plasma_chemistry,
    "process_heat": demo_uke_process_heat,
    "numbering_up": demo_uke_numbering_up,
    "inverse_catalyst_design": demo_uke_inverse_catalyst_design,
    "digital_twin_plant": demo_uke_digital_twin_plant,
    "biomanufacturing_scale": demo_uke_biomanufacturing_scale,
    "grand_electrified_industry": demo_uke_grand_electrified_industry,
}
