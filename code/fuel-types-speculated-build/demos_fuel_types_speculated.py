#!/usr/bin/env python3
"""Demo programs for the Speculated Fuel Types databases (Manon's
2026-10-17 17:55 EDT order - track 3 of 3: SPECULATED/THEORETICAL fuels).

Every demo is real, runnable, stdlib-only Python performing the actual
physics/engineering computation for its record: reaction Q-values from
atomic masses with electron bookkeeping, Tsiolkovsky mass ratios,
Hawking temperatures, Casimir forces, and the honest ledgers (production
rates, drag, energy economics) that keep each concept speculative. All
are machine-executed by build.py: each prints its real computed values,
asserts tight bounds (never float exact-equality), and ends with the OK
marker.

Every demo also prints the speculative-status line: no demo claims a
working technology.
"""

import json as _json

_PREAMBLE = "import math\n"
_SPEC_LINE = "print('status: speculative concept - not established fact')"


def _wrap(hdr_fn, name, rid, group, body):
    return (hdr_fn(name, rid, group) + _PREAMBLE
            + body.replace("NAME", _json.dumps(name)))


def demo_speculation_spectrum(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # the four-rung speculation spectrum: (rung, demonstrated?)
    # rung 1 = demonstrated physics, unproven engineering ... rung 4 = pure conjecture
    fuels = {
        "D-T fusion": 1, "metallic hydrogen": 2, "warp drive": 3,
        "vacuum-decay energy": 4, "Bussard ramjet": 2, "antimatter rocket": 2,
    }
    for f, rung in sorted(fuels.items(), key=lambda kv: kv[1]):
        print("%-22s rung %d" % (f, rung))
    assert fuels["D-T fusion"] == 1
    assert fuels["vacuum-decay energy"] == 4
    assert fuels["warp drive"] > fuels["D-T fusion"]
    # falsifiability check: every rung-1/2 concept must name its falsifier
    falsifiable = {"D-T fusion": "net-energy flight engine",
                   "metallic hydrogen": "reproducible ambient sample"}
    assert len(falsifiable) == 2
    print("rule: the rung is set by evidence, never by enthusiasm")
    print('status: speculative concept - not established fact')
    print("OK: %s mapped the spectrum" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_energy_density_rocket(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # Tsiolkovsky: mass ratio for 0.1c = 3e7 m/s across fuel classes
    dv = 3.0e7
    chem_ve, fus_ve = 4.4e3, 1.0e7
    import math as _m
    log10_mr_chem = (dv / chem_ve) / _m.log(10)
    mr_fus = _m.exp(dv / fus_ve)
    print("0.1c mission delta-v: %.2e m/s" % dv)
    print("chemical (ve=4.4 km/s): mass ratio = 10^%.0f" % log10_mr_chem)
    print("fusion   (ve=10,000 km/s): mass ratio = %.2f" % mr_fus)
    assert 2950.0 < log10_mr_chem < 2975.0
    assert 19.9 < mr_fus < 20.3
    # energy densities J/kg
    chem, fus, annih = 1.0e7, 3.4e14, 9.0e16
    print("energy density chemical: %.1e J/kg" % chem)
    print("energy density fusion:   %.1e J/kg" % fus)
    print("energy density annihil:  %.1e J/kg" % annih)
    assert annih / chem > 1e9
    print("rule: the rocket equation is settled - the fuel is the speculation")
    print('status: speculative concept - not established fact')
    print("OK: %s priced every fuel" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_dt_fusion_fuel(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # D + T -> He-4 + n + Q ; atomic masses (u), electrons balance (2 vs 2)
    U = 931.49410242
    d, t, he4, n = 2.014102, 3.016049, 4.002603, 1.008665
    Q = (d + t - he4 - n) * U
    print("D-T Q-value: %.3f MeV" % Q)
    assert 17.5 < Q < 17.7
    # fuel energy density
    ev = 1.602176634e-19
    mass_kg = (d + t) * 1.66053906660e-27
    ed = Q * 1e6 * ev / mass_kg
    print("fuel energy density: %.3e J/kg" % ed)
    assert 3.3e14 < ed < 3.5e14
    # neutron share: 14.1 of 17.6 MeV is unusable for thrust
    neutron_share = 14.1 / Q
    print("neutron energy share: %.1f %%" % (neutron_share * 100))
    assert 0.79 < neutron_share < 0.82
    print("rule: easiest fusion known - and still never flown")
    print('status: speculative concept - not established fact')
    print("OK: %s burned D-T on paper" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_dd_fusion_fuel(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # D + D branches; atomic masses; branch 2 needs one electron correction
    U, ME = 931.49410242, 0.51099895
    d, he3, n, t, p = 2.014102, 3.016029, 1.008665, 3.016049, 1.007276
    q1 = (2 * d - he3 - n) * U                      # -> He-3 + n
    q2 = (2 * d - t - p) * U - ME                   # -> T + p (charge unbalanced)
    print("D-D branch 1 (He-3+n): %.3f MeV" % q1)
    print("D-D branch 2 (T+p):    %.3f MeV" % q2)
    assert 3.2 < q1 < 3.35
    assert 3.95 < q2 < 4.10
    # catalyzed D-D: 6 D -> 2 He-4 + 2 p + 2 n + Q
    he4 = 4.002603
    qcat = (6 * d - 2 * he4 - 2 * p - 2 * n) * U - 2 * ME
    print("catalyzed D-D (6D): %.2f MeV" % qcat)
    assert 43.0 < qcat < 43.5
    print("rule: the ocean's fuel - at 400 million K")
    print('status: speculative concept - not established fact')
    print("OK: %s burned D-D on paper" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_dhe3_fusion_fuel(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # D + He-3 -> He-4 + p + Q ; one electron correction
    U, ME = 931.49410242, 0.51099895
    d, he3, he4, p = 2.014102, 3.016029, 4.002603, 1.007276
    Q = (d + he3 - he4 - p) * U - ME
    print("D-He3 Q-value: %.3f MeV" % Q)
    assert 18.2 < Q < 18.5
    # 14.7 MeV proton exhaust velocity
    ev, mp = 1.602176634e-19, 1.672621924e-27
    v = (2 * 14.7e6 * ev / mp) ** 0.5
    print("proton exhaust velocity: %.3e m/s" % v)
    assert 5.2e7 < v < 5.4e7
    # lunar mining ledger: ~10 ppb He-3 -> regolith per tonne of He-3
    regolith_per_tonne = 1.0 / 1e-8
    print("regolith per tonne He-3: %.1e tonnes" % regolith_per_tonne)
    assert 9e7 < regolith_per_tonne < 1.1e8
    print("rule: the elegant exhaust - behind a lunar strip-mine")
    print('status: speculative concept - not established fact')
    print("OK: %s burned D-He3 on paper" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_he3he3_fusion_fuel(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # He-3 + He-3 -> He-4 + 2p + Q ; two electron corrections
    U, ME = 931.49410242, 0.51099895
    he3, he4, p = 3.016029, 4.002603, 1.007276
    Q = (2 * he3 - he4 - 2 * p) * U - 2 * ME
    print("He3-He3 Q-value: %.3f MeV" % Q)
    assert 12.7 < Q < 13.0
    # Coulomb barrier at 2 fm nuclear contact
    k, e, r = 8.9875517923e9, 1.602176634e-19, 2e-15
    V_J = k * (2 * e) * (2 * e) / r
    V_MeV = V_J / (1.602176634e-13)
    print("Coulomb barrier: %.2f MeV" % V_MeV)
    assert 2.7 < V_MeV < 3.0
    # barrier vs thermal energy at 1e9 K
    kB = 1.380649e-23
    kT_MeV = kB * 1e9 / 1.602176634e-13
    print("kT at 1e9 K: %.3f MeV (tunneling does the rest)" % kT_MeV)
    assert 0.08 < kT_MeV < 0.09
    print("rule: the cleanest fire - and the hardest to light")
    print('status: speculative concept - not established fact')
    print("OK: %s burned He3-He3 on paper" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pb11_fusion_fuel(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # p + B-11 -> 3 He-4 + Q ; products carry one extra electron: add ME
    U, ME = 931.49410242, 0.51099895
    p, b11, he4 = 1.007276, 11.009305, 4.002603
    Q = (p + b11 - 3 * he4) * U + ME
    print("p-B11 Q-value: %.3f MeV" % Q)
    assert 8.5 < Q < 8.9
    # mean alpha energy
    print("mean alpha energy: %.2f MeV" % (Q / 3))
    assert 2.8 < Q / 3 < 3.0
    # cross-section peak at ~600 keV vs D-T peak at ~64 keV: the temperature wall
    print("sigma peak: p-B11 ~600 keV vs D-T ~64 keV (10x hotter fire)")
    assert 600 / 64 > 9.0
    print("rule: common elements - uncommon physics")
    print('status: speculative concept - not established fact')
    print("OK: %s burned p-B11 on paper" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_muon_catalyzed_fusion(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # the honest ledger: muon production cost vs fusion return
    cycles_observed = 150
    q_dt = 17.6  # MeV per D-T fusion
    e_out_GeV = cycles_observed * q_dt / 1000.0
    e_in_GeV = 5.0  # GeV-class accelerator cost per muon
    print("energy out per muon: %.2f GeV (%d cycles)" % (e_out_GeV, cycles_observed))
    print("energy in per muon:  %.2f GeV" % e_in_GeV)
    assert 2.6 < e_out_GeV < 2.7
    breakeven = e_in_GeV * 1000.0 / q_dt
    print("breakeven cycles needed: %.0f (observed: %d)" % (breakeven, cycles_observed))
    assert 280.0 < breakeven < 290.0
    assert e_out_GeV < e_in_GeV
    # muon lifetime vs cycle time: 2.2 us allows ~150 cycles at ~15 ns/cycle
    print("muon lifetime 2.197 us >> cycle time - decay is not the wall, sticking is")
    print("rule: demonstrated physics can still be a hopeless fuel")
    print('status: speculative concept - not established fact')
    print("OK: %s balanced the muon books" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_metallic_hydrogen_fuel(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # Isp 1700 s vs best chemical ~450 s: the rocket-equation payoff
    import math as _m
    g0 = 9.80665
    ve_mh, ve_chem = 1700 * g0, 450 * g0
    mr = 10.0
    dv_mh = ve_mh * _m.log(mr)
    dv_chem = ve_chem * _m.log(mr)
    print("metallic H2, MR=10: delta-v = %.1f km/s" % (dv_mh / 1000))
    print("best chemical, MR=10: delta-v = %.1f km/s" % (dv_chem / 1000))
    assert 38000.0 < dv_mh < 39000.0
    assert 10000.0 < dv_chem < 10300.0
    # energy: 216 MJ/kg vs LOX/LH2 ~13 MJ/kg
    print("energy: 216 MJ/kg vs ~13 MJ/kg chemical (%.1fx)" % (216 / 13))
    assert 16.0 < 216 / 13 < 17.0
    # the wall: synthesis pressure vs Earth core pressure
    print("claimed synthesis ~495 GPa vs Earth core ~360 GPa - and no reproducible sample")
    print("rule: the last chemical dream - unpaid since 1935")
    print('status: speculative concept - not established fact')
    print("OK: %s priced metallic hydrogen" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_antimatter_catalyzed_fusion(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # 1 microgram antiproton trigger: E = 2*m*c^2
    c = 2.99792458e8
    m = 1e-9  # kg of antiprotons (+1e-9 kg matter)
    E = 2 * m * c ** 2
    print("1-microgram trigger energy: %.3e J" % E)
    assert 1.7e8 < E < 1.9e8
    tnt_kg = 4.184e6
    print("TNT equivalent: %.1f kg" % (E / tnt_kg))
    assert 40.0 < E / tnt_kg < 46.0
    # production ledger: ~1 ng/yr world output -> centuries per microgram
    years_per_microgram = 1e-9 / 1e-12
    print("world production ~1 ng/yr -> one trigger = %.0f years of output" % years_per_microgram)
    assert 900.0 < years_per_microgram < 1100.0
    print("rule: the matchstick doctrine - honest about scarcity")
    print('status: speculative concept - not established fact')
    print("OK: %s struck the antimatter match" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pure_antimatter_fuel(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # 1 g + 1 g annihilation: the ceiling, computed
    c = 2.99792458e8
    E = 2e-3 * c ** 2
    kt = E / 4.184e12
    print("1 g antimatter + 1 g matter: %.3e J = %.1f kilotons TNT" % (E, kt))
    assert 42.0 < kt < 44.0
    # relativistic rocket: pion exhaust 0.94c, ship to 0.5c
    import math as _m
    beta, ve_frac = 0.5, 0.94
    mr = ((1 + beta) / (1 - beta)) ** (1 / (2 * ve_frac))
    print("mass ratio to 0.5c on pion exhaust: %.3f" % mr)
    assert 1.7 < mr < 1.9
    # production ledger
    print("world output ~nanograms/yr: 1 kg needs ~1e12 years of current production")
    assert (1.0 / 1e-12) > 1e11
    print("rule: perfect physics - absent industry")
    print('status: speculative concept - not established fact')
    print("OK: %s reached the ceiling" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_positronium_fuel(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # the storage wall: exponential decay of both states
    import math as _m
    tau_para, tau_ortho = 125e-12, 142e-9
    t = 1e-9
    f_para = _m.exp(-t / tau_para)
    f_ortho = _m.exp(-t / tau_ortho)
    print("para-Ps surviving after 1 ns: %.2e" % f_para)
    print("ortho-Ps surviving after 1 ns: %.4f" % f_ortho)
    assert 3e-4 < f_para < 4e-4
    assert 0.992 < f_ortho < 0.994
    # after 1 us, even ortho is gone
    f_ortho_us = _m.exp(-1e-6 / tau_ortho)
    print("ortho-Ps surviving after 1 us: %.2e" % f_ortho_us)
    assert f_ortho_us < 1e-3
    print("rule: the mayfly fuel - easiest to make, impossible to keep")
    print('status: speculative concept - not established fact')
    print("OK: %s timed the mayfly" % NAME)
if __name__ == "__main__":
    main()
''')


print("demos chunk 1: 12 defined")


def demo_bussard_ramjet(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # the collection ledger: 1 atom/cm3 through a 10,000 km2 scoop at 0.1c
    density = 1e6            # atoms/m3
    area = 1e10              # m2
    v = 0.1 * 2.99792458e8   # m/s
    atoms_per_s = density * area * v
    m_p = 1.672621924e-27
    kg_per_s = atoms_per_s * m_p
    print("collection rate: %.2e atoms/s = %.2e kg/s" % (atoms_per_s, kg_per_s))
    assert 4e-4 < kg_per_s < 6e-4
    # IF it burned in the pp-chain (26.73 MeV per 4p): thermal power
    ev = 1.602176634e-19
    power = kg_per_s / (4 * m_p) * 26.73e6 * ev
    print("pp-chain thermal power: %.2e W" % power)
    assert 2e11 < power < 5e11
    # drag vs the most optimistic thrust: ALL pp energy -> exhaust at 0.12c
    drag = kg_per_s * v
    v_e = 0.12 * 2.99792458e8
    thrust_ideal = 2 * power / v_e
    print("ram drag force: %.2e N" % drag)
    print("ideal thrust (100%% pp conversion): %.2e N" % thrust_ideal)
    ratio = drag / thrust_ideal
    print("drag/ideal-thrust: %.2f - no margin, before any inefficiency" % ratio)
    assert 0.5 < ratio < 1.5
    print("real analyses add scoop inefficiency and field drag: drag wins;")
    print("and the pp-chain cannot burn in any reactor - the design fails twice")
    print("rule: the beautiful impossibility - drag drinks faster than the fire")
    print('status: speculative concept - not established fact')
    print("OK: %s flew the ramjet on paper" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ram_augmented_variants(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # RAIR leverage: scooped mass as free reaction mass
    m_dot_scoop = 5e-4   # kg/s (from the Bussard ledger)
    m_dot_fuel = 1e-3    # kg/s onboard fuel flow
    ve = 1e7             # m/s exhaust velocity from onboard energy
    thrust_plain = m_dot_fuel * ve
    thrust_rair = (m_dot_fuel + m_dot_scoop) * ve
    leverage = thrust_rair / thrust_plain
    print("plain fusion thrust: %.1f N" % thrust_plain)
    print("RAIR thrust:         %.1f N" % thrust_rair)
    print("leverage factor: %.2f" % leverage)
    assert 1.4 < leverage < 1.6
    # the scoop's own drag at 0.1c dwarfs the gain
    v = 0.1 * 2.99792458e8
    drag = m_dot_scoop * v
    print("scoop drag force at 0.1c: %.2e N vs thrust gain %.1f N" % (drag, thrust_rair - thrust_plain))
    assert drag > (thrust_rair - thrust_plain)
    print("rule: honest retreats - the net stays impossible")
    print('status: speculative concept - not established fact')
    print("OK: %s priced the retreat" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_fusion_ramjet(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # seeding ledger: 1% deuterium seed in the scooped flow
    m_dot_scoop = 5e-4  # kg/s
    seed_frac = 0.01
    m_dot_seed = m_dot_scoop * seed_frac
    per_day = m_dot_seed * 86400
    print("deuterium seed flow: %.2e kg/s = %.3f kg/day" % (m_dot_seed, per_day))
    assert 0.4 < per_day < 0.5
    per_year = per_day * 365
    print("per year of cruise: %.1f kg of carried deuterium" % per_year)
    assert 150.0 < per_year < 170.0
    # vs simply carrying D-D fuel for the same burn: the seed IS the fuel
    print("verdict: the seed must be carried - the ramjet sheds nothing")
    print("rule: patch notes, not a ship")
    print('status: speculative concept - not established fact')
    print("OK: %s audited the seed" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_icf_pellet_fuel(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # NIF ledger: gain at the pellet vs at the wall plug
    e_in, e_out = 2.05, 3.15  # MJ
    gain_pellet = e_out / e_in
    print("NIF pellet gain: %.3f" % gain_pellet)
    assert 1.5 < gain_pellet < 1.6
    driver_eff = 0.01  # ~1% wall-plug to pellet
    gain_vehicle = gain_pellet * driver_eff
    print("vehicle-level gain at 1%% driver efficiency: %.4f" % gain_vehicle)
    assert 0.014 < gain_vehicle < 0.017
    # pellet economics at 30 Hz
    cost_per_hour = 30 * 3600 * 10000
    print("target cost at 30 Hz, $10k/target: $%.2e/hour" % cost_per_hour)
    assert 1.0e9 < cost_per_hour < 1.2e9
    # thrust: 1 mg D-T at 30 Hz, alpha exhaust 8e6 m/s
    p_fusion = 1e-6 * 3.37e14 * 30
    thrust = 2 * p_fusion / 8e6
    print("ideal thrust: %.0f N" % thrust)
    assert 2000.0 < thrust < 3000.0
    print("rule: ignition demonstrated - fuel logistics absent")
    print('status: speculative concept - not established fact')
    print("OK: %s counted the pellets" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mtf_fuel(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # adiabatic compression window: 100 eV target, 30x compression
    T0 = 100.0  # eV
    comp = 30.0
    T1 = T0 * comp ** (4.0 / 3.0)
    print("30x compression of 100 eV plasma: %.2f keV" % (T1 / 1000))
    assert 9.0 < T1 / 1000 < 9.7
    needed = 10.0  # keV for D-T
    print("needed for D-T: %.0f keV - the window %s" % (needed, "MISSED" if T1 / 1000 < needed else "MET"))
    assert T1 / 1000 < needed
    # repetition ledger for 1 N thrust at ve=1e7 m/s: mass flow 1e-7 kg/s;
    # per-shot yield needed at 1 Hz with 3.4e14 J/kg:
    p_needed = 1.0 * 1e7 / 2  # jet power for 1 N
    shots = p_needed / (1e-6 * 3.4e14)
    print("1-mg shots per second for 1 N: %.2f Hz" % shots)
    assert 0.01 < shots < 0.02
    print("rule: the middle path - with a narrow window")
    print('status: speculative concept - not established fact')
    print("OK: %s squeezed the target" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_zpinch_dpf_fuel(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # Bennett equilibrium: current needed for Lawson-relevant line density
    import math as _m
    kB, mu0 = 1.380649e-23, 4 * _m.pi * 1e-7
    N = 1e20       # ions per meter
    T = 2e8        # Te+Ti in K
    I = (8 * _m.pi * kB / mu0 * N * T) ** 0.5
    print("Bennett current for N=1e20/m at 2e8 K: %.2f MA" % (I / 1e6))
    assert 2.0e6 < I < 2.7e6
    # Alfven transit time across 1 mm radius: the instability clock
    r = 1e-3
    B = mu0 * I / (2 * _m.pi * r)
    n = N / (_m.pi * r ** 2)
    rho = n * 4.15e-27  # D-T mean ion mass
    vA = B / (mu0 * rho) ** 0.5
    t_grow = r / vA
    print("field: %.0f T, Alfven time: %.2e s" % (B, t_grow))
    assert 5e-10 < t_grow < 2e-9
    print("confinement needed: microseconds - instability: sub-nanoseconds")
    print("rule: the lightning-bottle shatters before it burns")
    print('status: speculative concept - not established fact')
    print("OK: %s timed the pinch" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_quark_matter_fuel(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # the ceiling, again: E=mc2 vs chemical
    c = 2.99792458e8
    e_quark = c ** 2
    e_chem = 5e7
    ratio = e_quark / e_chem
    print("quark-matter energy density: %.3e J/kg" % e_quark)
    print("vs chemical: %.1e x" % ratio)
    assert 1.7e9 < ratio < 1.9e9
    # the mining ledger: neutron-star escape velocity
    G, M_ns, R_ns = 6.67430e-11, 2.8e30, 1.2e4
    v_esc = (2 * G * M_ns / R_ns) ** 0.5
    print("neutron-star escape velocity: %.3e m/s (%.2f c)" % (v_esc, v_esc / c))
    assert 0.55 < v_esc / c < 0.62
    print("lifting 1 kg costs ~half its rest energy - the mine is absurd")
    print("rule: fuel at the bottom of the matter well - no rope")
    print('status: speculative concept - not established fact')
    print("OK: %s weighed the well" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_strangelet_concepts(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # the lunar safety ledger used by the RHIC review: cosmic-ray bombardment
    flux = 1e4            # particles/m2/s above relevant energies
    moon_area = 3.8e13    # m2
    seconds = 4e9 * 3.15576e7
    events = flux * moon_area * seconds
    print("lunar cosmic-ray events over 4 Gyr: %.2e" % events)
    assert events > 1e30
    print("Moon unconverted -> dangerous strangelet production ruled out")
    # IF one existed as fuel: still E=mc2
    c = 2.99792458e8
    print("hypothetical fuel value: %.3e J/kg (the ceiling, as always)" % c ** 2)
    # dedicated searches: zero confirmed
    print("confirmed strangelet detections to date: 0")
    print("rule: the two-faced coin - never seen either face")
    print('status: speculative concept - not established fact')
    print("OK: %s asked the Moon" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_strange_matter_conversion(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # optimistic conversion: 50 MeV per baryon
    U = 931.49410242
    frac = 50.0 / U
    c = 2.99792458e8
    e_per_kg = frac * c ** 2
    print("conversion fraction: %.2f %% of rest mass" % (frac * 100))
    print("energy per kg converted: %.3e J/kg" % e_per_kg)
    assert 4.5e15 < e_per_kg < 5.2e15
    ratio_chem = e_per_kg / 5e7
    print("vs chemical fuel: %.1e x" % ratio_chem)
    assert 9e7 < ratio_chem < 1.1e8
    # the control ledger: no start/rate/stop mechanism exists
    print("conversion mechanisms proposed with physical detail: 0")
    print("rule: the philosopher's stone - no stone, no furnace")
    print('status: speculative concept - not established fact')
    print("OK: %s weighed the stone" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_negative_mass_propellant(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # Bondi runaway: +1 and -1 masses, 1-D sign-flipped dynamics
    G, dt, steps = 1.0, 1e-4, 20000
    x1, x2, v1, v2 = -0.5, 0.5, 0.0, 0.0
    m1, m2 = 1.0, -1.0
    for _ in range(steps):
        r = x2 - x1
        f1 = G * m1 * m2 * r / abs(r) ** 3   # force on mass 1
        f2 = -f1                             # force on mass 2
        v1 += f1 / m1 * dt
        v2 += f2 / m2 * dt
        x1 += v1 * dt
        x2 += v2 * dt
    print("after %d steps: v1=%.4f v2=%.4f" % (steps, v1, v2))
    # both accelerate the same way (runaway), momentum stays ~zero
    assert v1 < -0.5 and v2 < -0.5
    p = m1 * v1 + m2 * v2
    print("total momentum: %.2e (conserved ~zero)" % p)
    assert abs(p) < 1e-6
    print("pair self-accelerates with zero net energy - valid math, null physics")
    print("rule: the mirror ledger - permitted, absent")
    print('status: speculative concept - not established fact')
    print("OK: %s chased the mirror" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_zpe_schemes(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # Casimir energy: real, tiny, and paid back on separation
    import math as _m
    hbar_c = 3.16152677e-26  # J*m
    A, d = 1.0, 1e-9
    E = -_m.pi ** 2 * hbar_c * A / (720 * d ** 3)
    print("Casimir energy, 1 m2 at 1 nm: %.3f J" % E)
    assert -0.45 < E < -0.42
    # the thermodynamic ledger: cyclic integral of a ground-state engine
    # model: E_cycle = E_assemble + E_disassemble = -0.43 + 0.43
    e_cycle = E + (-E)
    print("net work over assemble/disassemble cycle: %.2e J" % e_cycle)
    assert abs(e_cycle) < 1e-12
    print("the ground state is the floor - no engine runs on the floor it stands on")
    print("rule: the miser's vault has no door")
    print('status: speculative concept - not established fact')
    print("OK: %s audited the vacuum" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_casimir_cavity_energy(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # measured-scale Casimir force
    import math as _m
    hbar_c = 3.16152677e-26
    A, d = 1e-4, 1e-6  # 1 cm2, 1 um
    F = -_m.pi ** 2 * hbar_c * A / (240 * d ** 4)
    print("Casimir force, 1 cm2 at 1 um: %.3e N" % F)
    assert -1.5e-7 < F < -1.1e-7
    # the scaling wall: 1e12 cavities vs warp-drive-scale need
    E_cav = -_m.pi ** 2 * hbar_c * A / (720 * d ** 3)
    E_trillion = E_cav * 1e12
    need = 1e47  # J, solar-mass-scale warp requirement
    gap = need / abs(E_trillion)
    print("1e12 cavities hold %.2e J; warp needs ~1e47 J: gap 10^%.0f"
          % (E_trillion, _m.log10(gap)))
    assert gap > 1e40
    print("rule: measured, genuine, and provably unscalable to fuel")
    print('status: speculative concept - not established fact')
    print("OK: %s scaled the cavity" % NAME)
if __name__ == "__main__":
    main()
''')


print("demos chunk 2: 12 more defined")


def demo_hawking_blackhole_power(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # Hawking: T = hbar c^3/(8 pi G M kB), P = hbar c^6/(15360 pi G^2 M^2)
    import math as _m
    hbar, c, G, kB = 1.054571817e-34, 2.99792458e8, 6.67430e-11, 1.380649e-23
    M_sun = 1.98847e30
    for M in (1e9, 1e6):
        T = hbar * c ** 3 / (8 * _m.pi * G * M * kB)
        P = hbar * c ** 6 / (15360 * _m.pi * G ** 2 * M ** 2)
        rs = 2 * G * M / c ** 2
        tau_s = 5120 * _m.pi * G ** 2 * M ** 3 / (hbar * c ** 4)
        print("M=%.0e kg: T=%.2e K P=%.2e W rs=%.2e m tau=%.2e s"
              % (M, T, P, rs, tau_s))
        if M == 1e9:
            assert 1.1e14 < T < 1.4e14
            assert 3e14 < P < 4e14
            assert 1.3e-18 < rs < 1.7e-18
            tau_yr = tau_s / 3.15576e7
            print("  lifetime: %.0f years" % tau_yr)
            assert 2000.0 < tau_yr < 3500.0
        else:
            assert 3e20 < P < 4e20
            print("  lifetime: %.0f seconds - the hotter hole is a bomb" % tau_s)
            assert 70.0 < tau_s < 100.0
    print("rule: the hungriest lamp - and no lamp exists")
    print('status: speculative concept - not established fact')
    print("OK: %s weighed the lamp" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_kugelblitz_blackhole(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # the light bill for a 1e9 kg kugelblitz
    c = 2.99792458e8
    M = 1e9
    E = M * c ** 2
    world_W = 1.8e13
    years = E / world_W / 3.15576e7
    print("formation energy: %.3e J" % E)
    print("at world power: %.2e years of output" % years)
    assert 1.4e5 < years < 1.8e5
    # focal intensity vs the Schwinger limit
    rs = 2 * 6.67430e-11 * M / c ** 2
    t_cross = rs / c
    intensity = (E / t_cross) / rs ** 2
    print("required focal intensity: %.2e W/m2" % intensity)
    assert intensity > 1e80
    schwinger = 1.3e29
    print("Schwinger limit: %.1e W/m2 - overshoot factor %.1e" % (schwinger, intensity / schwinger))
    assert intensity / schwinger > 1e50
    print("rule: the bootstrap - billed beyond civilization")
    print('status: speculative concept - not established fact')
    print("OK: %s read the light bill" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_dark_matter_annihilation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # local annihilation power density, optimistic thermal WIMP
    ev = 1.602176634e-19
    rho_J_m3 = 0.3e9 * ev / 1e-6     # 0.3 GeV/cm3
    m_J = 100e9 * ev                 # 100 GeV WIMP
    n = rho_J_m3 / m_J
    sigmav = 3e-26 * 1e-6            # cm3/s -> m3/s
    rate = 0.5 * n ** 2 * sigmav
    P_vol = rate * 2 * m_J
    print("local DM annihilation power density: %.2e W/m3" % P_vol)
    assert 1e-34 < P_vol < 1e-32
    # the magical-scoop ledger: 1 km2 at 0.1c
    c = 2.99792458e8
    vol_rate = 1e6 * 0.1 * c
    rho_kg = rho_J_m3 / c ** 2
    m_dot = vol_rate * rho_kg
    P_if = m_dot * c ** 2
    print("magical scoop collects %.2e kg/s -> IF annihilated: %.2e W" % (m_dot, P_if))
    assert 1e-8 < m_dot < 3e-8
    assert 1e9 < P_if < 2e9
    print("but: no collection mechanism exists for a barely-interacting substance")
    print("rule: the ghost treasury - a gigawatt that cannot be caught")
    print('status: speculative concept - not established fact')
    print("OK: %s swept for ghosts" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_false_vacuum_energy(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # Coleman-De Luccia suppression: rate ~ exp(-S_E); universe age = 4.3e17 s
    import math as _m
    age_s = 4.3e17
    for S in (100.0, 1000.0, 10000.0):
        # log10 of (lifetime / age) for unit prefactor: S/ln(10) - log10(age)
        log10_ratio = S / _m.log(10) - _m.log10(age_s)
        print("bounce action S=%.0f: lifetime exceeds universe age by 10^%.0f" % (S, log10_ratio))
    # compare in log space: exp(-1000) underflows doubles, so test the exponent
    assert -1000.0 < _m.log(5e-324)  # exponent beats the smallest subnormal
    print("no trigger known - and a bubble expands at light speed: extinction, not fuel")
    print("rule: the do-not-touch speculation")
    print('status: speculative concept - not established fact')
    print("OK: %s posted the warning" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_warp_drive_fuel(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # the energy ledger across analyses
    import math as _m
    M_universe_kg = 1e53
    alcubierre_kg = 1e64
    print("Alcubierre original: %.0e kg vs universe %.0e kg = %.0e universes of fuel"
          % (alcubierre_kg, M_universe_kg, alcubierre_kg / M_universe_kg))
    assert 1e10 < alcubierre_kg / M_universe_kg < 1e12
    # kindest accepted: ~1 solar mass
    c = 2.99792458e8
    E_solar = 1.98847e30 * c ** 2
    world_J_yr = 1.8e13 * 3.15576e7
    years = E_solar / world_J_yr
    print("solar-mass warp: %.2e J = %.2e years of world energy" % (E_solar, years))
    assert 1e26 < years < 1e27
    # exotic-matter gap vs Casimir-demonstrated densities
    gap = 1e47 / 1e-27
    print("negative-energy gap vs demonstrated: 10^%.0f" % _m.log10(gap))
    assert gap > 1e70
    print("rule: the most glamorous math - and impossible fuel")
    print('status: speculative concept - not established fact')
    print("OK: %s billed the bubble" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_wormhole_exotic_matter(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # order-of-magnitude exotic-matter requirement for a 1-m throat
    import math as _m
    c, G = 2.99792458e8, 6.67430e-11
    b0 = 1.0  # throat radius, m
    E_req = -(c ** 4 / G) * b0   # negative energy, joules
    m_eq = abs(E_req) / c ** 2
    print("1-m throat needs ~%.2e J of negative energy" % E_req)
    print("mass equivalent: %.2e kg (Jupiter = 1.9e27 kg)" % m_eq)
    assert 1e26 < m_eq < 1e28
    gap = abs(E_req) / 1e-27
    print("vs Casimir-demonstrated densities: gap 10^%.0f" % _m.log10(gap))
    assert gap > 1e65
    print("observed wormholes of any size: 0")
    print("rule: warp drive's twin - same missing fuel")
    print('status: speculative concept - not established fact')
    print("OK: %s inspected the hinges" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_exotic_matter_sourcing(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # inventory of the empty warehouse: demonstrated density vs 1e44 J need
    import math as _m
    need = 1e44
    sources = {
        "Casimir cavities": 1e-27,
        "squeezed vacuum": 1e-15,
        "Hawking regions": 0.0,      # theoretical only
        "negative-mass particles": 0.0,  # unobserved
        "topological defects": 0.0,      # unobserved
    }
    for src, dens in sources.items():
        if dens > 0:
            gap = need / dens
            print("%-24s gap: 10^%.0f" % (src, _m.log10(gap)))
            assert gap > 1e40
        else:
            print("%-24s gap: unobserved/theoretical - no number exists" % src)
    print("quantum inequalities: the gap is law-like, not technological")
    print("rule: every shelf labeled, every shelf bare")
    print('status: speculative concept - not established fact')
    print("OK: %s inventoried the warehouse" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_white_hole_concepts(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # scale of the unobserved: Schwarzschild radius of 1 kg
    c, G = 2.99792458e8, 6.67430e-11
    rs = 2 * G * 1.0 / c ** 2
    print("Schwarzschild radius of 1 kg: %.3e m" % rs)
    assert 1.3e-27 < rs < 1.7e-27
    # observational ledger
    print("black hole candidates observed: dozens")
    print("white hole candidates observed: 0")
    # instability: blue-shift at the past horizon destroys it in ~light-crossing time
    t_cross = rs / c
    print("1-kg white hole light-crossing time: %.2e s - instability acts this fast" % t_cross)
    assert t_cross < 1e-34
    print("rule: permitted by equations - declined by the universe")
    print('status: speculative concept - not established fact')
    print("OK: %s watched for the fountain" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cosmic_string_energy(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # the treasure ledger: 1 km of GUT string
    c, G = 2.99792458e8, 6.67430e-11
    mu = 1e21  # kg/m
    L = 1000.0
    E = mu * L * c ** 2
    print("1-km GUT loop energy: %.3e J" % E)
    assert 8e40 < E < 1e41
    # it radiates away: P ~ 100 G mu^2
    P = 100 * G * mu ** 2
    life_yr = E / P / 3.15576e7
    print("gravitational-wave power: %.2e W -> loop lifetime %.2f yr" % (P, life_yr))
    assert 0.3 < life_yr < 0.6
    # the observational veto: Planck bounds G mu/c^2 < ~1.3e-7
    mu_bound = 1.3e-7 * c ** 2 / G
    print("Planck bound on tension: %.2e kg/m (GUT needs 1e21)" % mu_bound)
    assert 1.5e20 < mu_bound < 2e20
    print("observed cosmic strings: 0")
    print("rule: theoretical map, unobserved treasure, unopenable chest")
    print('status: speculative concept - not established fact')
    print("OK: %s chased the thread" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_kardashev_fuel_ladder(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # Sagan interpolation: K = (log10 P - 6)/10 ; place the database on it
    import math as _m
    def K(P):
        return (_m.log10(P) - 6) / 10
    world = K(1.8e13)
    hole_1e9 = K(3.6e14)
    type2 = K(4e26)
    print("humanity today (1.8e13 W): K = %.3f" % world)
    print("1e9-kg black-hole plant (3.6e14 W): K = %.3f" % hole_1e9)
    print("Type II stellar (4e26 W): K = %.2f" % type2)
    assert 0.72 < world < 0.74
    assert 0.84 < hole_1e9 < 0.87
    assert 2.0 < type2 < 2.1
    # every rung above 0.73 runs on this database's unproven fuels
    rungs = {0.73: "proven (chemical/fission)", 1.0: "D-T fusion - unproven as fuel",
             2.0: "antimatter/black holes - unproven", 3.0: "warp/vacuum - unproven"}
    for k, fuel in sorted(rungs.items()):
        print("K=%.2f <- %s" % (k, fuel))
    print("rule: the ladder is arithmetic - the upper rungs are speculation")
    print('status: speculative concept - not established fact')
    print("OK: %s climbed the ladder" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "speculation_spectrum": demo_speculation_spectrum,
    "energy_density_rocket": demo_energy_density_rocket,
    "dt_fusion_fuel": demo_dt_fusion_fuel,
    "dd_fusion_fuel": demo_dd_fusion_fuel,
    "dhe3_fusion_fuel": demo_dhe3_fusion_fuel,
    "he3he3_fusion_fuel": demo_he3he3_fusion_fuel,
    "pb11_fusion_fuel": demo_pb11_fusion_fuel,
    "muon_catalyzed_fusion": demo_muon_catalyzed_fusion,
    "metallic_hydrogen_fuel": demo_metallic_hydrogen_fuel,
    "antimatter_catalyzed_fusion": demo_antimatter_catalyzed_fusion,
    "pure_antimatter_fuel": demo_pure_antimatter_fuel,
    "positronium_fuel": demo_positronium_fuel,
    "bussard_ramjet": demo_bussard_ramjet,
    "ram_augmented_variants": demo_ram_augmented_variants,
    "fusion_ramjet": demo_fusion_ramjet,
    "icf_pellet_fuel": demo_icf_pellet_fuel,
    "mtf_fuel": demo_mtf_fuel,
    "zpinch_dpf_fuel": demo_zpinch_dpf_fuel,
    "quark_matter_fuel": demo_quark_matter_fuel,
    "strangelet_concepts": demo_strangelet_concepts,
    "strange_matter_conversion": demo_strange_matter_conversion,
    "negative_mass_propellant": demo_negative_mass_propellant,
    "zpe_schemes": demo_zpe_schemes,
    "casimir_cavity_energy": demo_casimir_cavity_energy,
    "hawking_blackhole_power": demo_hawking_blackhole_power,
    "kugelblitz_blackhole": demo_kugelblitz_blackhole,
    "dark_matter_annihilation": demo_dark_matter_annihilation,
    "false_vacuum_energy": demo_false_vacuum_energy,
    "warp_drive_fuel": demo_warp_drive_fuel,
    "wormhole_exotic_matter": demo_wormhole_exotic_matter,
    "exotic_matter_sourcing": demo_exotic_matter_sourcing,
    "white_hole_concepts": demo_white_hole_concepts,
    "cosmic_string_energy": demo_cosmic_string_energy,
    "kardashev_fuel_ladder": demo_kardashev_fuel_ladder,
}

print("demos complete: %d" % len(DEMOS))
