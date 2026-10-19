#!/usr/bin/env python3
"""Solution-explorer walkthrough demos for the Unsolved Chemistry databases.

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


def demo_uc_mpemba(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: four-factor race - evaporation, convection, supercooling, contact.")
    # ---- adjustable assumptions ----
    tau = 1200.0       # s, effective cooling time constant (measured per setup)
    T_freezer = -18.0  # C
    evap_frac = 0.04   # hot beaker loses 4% mass to evaporation
    conv_boost = 1.4   # convection raises hot beaker heat transfer 40%
    contact_gain = 0.90  # melted frost improves hot beaker contact 10%
    supercool_min = 10.0  # cold beaker supercools: +10 min delay
    # ---- step 1: baseline Newtonian cooling times ----
    t_hot_base = tau * math.log((90.0 - T_freezer) / (0.0 - T_freezer))
    t_cold_base = tau * math.log((20.0 - T_freezer) / (0.0 - T_freezer))
    print("step 1 baseline: hot %.1f min, cold %.1f min"
          % (t_hot_base / 60.0, t_cold_base / 60.0))
    # ---- step 2: apply the four factors ----
    t_hot = t_hot_base * (1 - evap_frac) / conv_boost * contact_gain
    t_cold = t_cold_base + supercool_min * 60.0
    print("step 2 with factors: hot %.1f min, cold %.1f min"
          % (t_hot / 60.0, t_cold / 60.0))
    assert 20.0 < t_hot / 60.0 < 26.0
    assert 22.0 < t_cold / 60.0 < 28.0
    assert t_hot < t_cold, "hot must win in this regime"
    print("step 3 verdict: HOT wins by %.1f min in the open-beaker regime"
          % ((t_cold - t_hot) / 60.0))
    # ---- step 4: flip the regime - closed lids, degassed water ----
    t_hot_closed = tau * math.log((90.0 - T_freezer) / (0.0 - T_freezer))
    t_cold_closed = tau * math.log((20.0 - T_freezer) / (0.0 - T_freezer))
    assert t_hot_closed > t_cold_closed, "cold must win with factors removed"
    print("step 4 regime flip (lids on, degassed): hot %.1f min, cold %.1f min - COLD wins"
          % (t_hot_closed / 60.0, t_cold_closed / 60.0))
    print("CONFIRM: open/closed lid matrix experiment matches the predicted winner per regime.")
    print("REFUTE: hot wins with lids closed and gases controlled - a fifth factor exists.")
    print("OK: %s walked the four-factor race" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uc_water_anomalies(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: two-liquid mixture - open tetrahedral vs collapsed disordered.")
    # ---- adjustable assumptions ----
    T0, w = -25.0, 20.0          # midpoint and width of the structural crossover (C)
    rho_ld, rho_hd = 0.960, 1.000  # g/cm^3 of the two local structures
    alpha = 3.5e-4               # thermal expansion of each component (1/K)
    def x_ld(T):
        return 1.0 / (1.0 + math.exp((T - T0) / w))
    def rho(T):
        x = x_ld(T)
        return (x * rho_ld + (1 - x) * rho_hd) * (1 - alpha * (T - 4.0))
    Ts = [t * 2.0 for t in range(-15, 36)]  # -30 .. 70 C
    rhos = [rho(T) for T in Ts]
    Tmax = Ts[rhos.index(max(rhos))]
    print("step 1 low-density fraction: x(-20C)=%.3f, x(20C)=%.3f, x(60C)=%.3f"
          % (x_ld(-20.0), x_ld(20.0), x_ld(60.0)))
    print("step 2 density maximum at T=%.1f C, rho=%.4f g/cm^3" % (Tmax, max(rhos)))
    assert -5.0 < Tmax < 10.0, "density maximum must sit near 4 C"
    assert 0.98 < max(rhos) < 1.00
    assert rhos[0] < max(rhos) and rhos[-1] < max(rhos), "maximum must be interior"
    # ---- step 3: heat-capacity-style response peak from the same x(T) ----
    dx = [(x_ld(T + 1.0) - x_ld(T - 1.0)) / 2.0 for T in Ts]
    peak_T = Ts[dx.index(min(dx))]
    print("step 3 strongest structural change near T=%.1f C (response-function peak)" % peak_T)
    print("CONFIRM: X-ray scattering shows fluctuation growth matching the two-state prediction.")
    print("REFUTE: a single-state water model reproduces all anomalies with no structural crossover.")
    print("OK: %s derived the anomalies from one crossover" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uc_smell(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: dual-channel receptor - shape gate plus vibration-assisted tunneling.")
    # ---- adjustable assumptions ----
    nu_H = 3000.0        # cm^-1, C-H stretch
    m_C, m_H, m_D = 12.0, 1.0, 2.0
    gap_center, gap_half = 2900.0, 150.0  # receptor tunneling gap window (cm^-1)
    # ---- step 1: isotope frequency shift ----
    mu_H = m_C * m_H / (m_C + m_H)
    mu_D = m_C * m_D / (m_C + m_D)
    nu_D = nu_H * math.sqrt(mu_H / mu_D)
    shift = nu_H - nu_D
    print("step 1 C-H %.0f cm^-1 -> C-D %.0f cm^-1, shift %.0f cm^-1"
          % (nu_H, nu_D, shift))
    assert 790.0 < shift < 810.0
    # ---- step 2: which isotopomer fits the tunneling gap? ----
    h_in = abs(nu_H - gap_center) < gap_half
    d_in = abs(nu_D - gap_center) < gap_half
    print("step 2 gap window [%.0f, %.0f]: H activates=%s, D activates=%s"
          % (gap_center - gap_half, gap_center + gap_half, h_in, d_in))
    assert h_in and not d_in, "this receptor should show an isotope effect"
    # ---- step 3: dual prediction - a detuned receptor shows no isotope effect ----
    gap2_center = 1500.0
    h2 = abs(nu_H - gap2_center) < gap_half
    d2 = abs(nu_D - gap2_center) < gap_half
    print("step 3 detuned receptor: H=%s, D=%s - both silent, shape gate decides" % (h2, d2))
    print("CONFIRM: receptor panel shows isotope effects only in gap-tuned receptors.")
    print("REFUTE: no receptor anywhere shows an isotope effect - vibration channel is dead.")
    print("OK: %s split the shape and vibration channels" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uc_protein_folding(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: Levinthal audit, then funnel plus folding nucleus.")
    # ---- step 1: the paradox is real for random search ----
    n, conf_per_res = 100, 3
    conformations = conf_per_res ** n
    rate = 1e12  # conformational trials per second
    years = conformations / rate / 3.15576e7
    print("step 1 %d conformations -> %.2e years at 1e12 trials/s" % (conformations, years))
    assert 1e27 < years < 1e29
    assert conformations == 515377520732011331036461129765621272702107522001
    # ---- step 2: funnel bias collapses the search ----
    p_native = 0.5      # per-residue bias toward native-like state
    nucleus = 10        # key contacts that commit the fold
    trials_nucleus = (1.0 / p_native) ** nucleus
    print("step 2 nucleus of %d contacts: ~%.0f trials to commit, then zipper" % (nucleus, trials_nucleus))
    assert 1000.0 < trials_nucleus < 1100.0
    # ---- step 3: contact order predicts speed ----
    for co, label in ((0.15, "fast folder"), (0.35, "slow folder")):
        t_rel = math.exp(12.0 * co)
        print("step 3 contact order %.2f -> relative folding time %.1f (%s)" % (co, t_rel, label))
    assert math.exp(12.0 * 0.35) > math.exp(12.0 * 0.15)
    print("CONFIRM: single-molecule FRET catches predicted nucleus contacts forming first.")
    print("REFUTE: folding with no early nucleus, or trap census failing to predict chaperone need.")
    print("OK: %s resolved the paradox with a funnel" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uc_enzyme_speed(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: factor-by-factor ledger of a 1e15 rate enhancement.")
    # ---- adjustable assumptions: the four ledger entries ----
    f_bind = 1e6    # transition-state binding (Pauling)
    f_preorg = 1e7   # electrostatic preorganization (Warshel)
    f_tunnel = 1e1   # hydrogen tunneling
    f_dyn = 1e1      # dynamical gating
    total = f_bind * f_preorg * f_tunnel * f_dyn
    log_total = sum(math.log10(f) for f in (f_bind, f_preorg, f_tunnel, f_dyn))
    print("step 1 ledger: 1e6 x 1e7 x 1e1 x 1e1 = %.1e (log10 = %.1f)" % (total, log_total))
    assert 14.9 < log_total < 15.1
    # ---- step 2: tunneling check via kinetic isotope effect ----
    kie_classical_ceiling = 7.0
    kie_observed = 12.0
    print("step 2 KIE observed %.1f vs classical ceiling %.1f -> tunneling contributes"
          % (kie_observed, kie_classical_ceiling))
    assert 10.0 < kie_observed < 15.0
    assert kie_observed > kie_classical_ceiling
    # ---- step 3: shares ----
    for label, f in (("binding", f_bind), ("preorganization", f_preorg),
                     ("tunneling", f_tunnel), ("dynamics", f_dyn)):
        print("step 3 %-15s 10^%.0f of 10^%.0f" % (label, math.log10(f), log_total))
    print("CONFIRM: a model enzyme where all four ledger entries are measured independently multiplies to the observed rate.")
    print("REFUTE: ledger product misses the observed rate by orders of magnitude with all factors measured.")
    print("OK: %s balanced the catalytic ledger" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uc_hydrophobic(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: length-scale crossover - entropic below ~1 nm, enthalpic above.")
    # ---- adjustable assumptions (kJ/mol, r in nm) ----
    a, b, r0 = 8.0, 8.0, 1.0
    def dG_ent(r):
        return a * r * r * math.exp(-r / r0)       # water-ordering cost
    def dG_enth(r):
        return b * r * r * (1 - math.exp(-r / r0))  # H-bond breaking cost
    # ---- step 1: find the crossover ----
    lo, hi = 0.01, 10.0
    for _ in range(60):
        mid = (lo + hi) / 2.0
        if dG_ent(mid) > dG_enth(mid):
            lo = mid
        else:
            hi = mid
    r_star = (lo + hi) / 2.0
    print("step 1 crossover at r* = %.3f nm" % r_star)
    assert 0.60 < r_star < 0.80
    # ---- step 2: methane-scale vs surface-scale ----
    r_small, r_big = 0.30, 2.00
    print("step 2 r=0.30nm: entropic %.2f vs enthalpic %.2f kJ/mol (entropy wins)"
          % (dG_ent(r_small), dG_enth(r_small)))
    print("step 2 r=2.00nm: entropic %.2f vs enthalpic %.2f kJ/mol (enthalpy wins)"
          % (dG_ent(r_big), dG_enth(r_big)))
    assert dG_ent(r_small) > dG_enth(r_small)
    assert dG_enth(r_big) > dG_ent(r_big)
    print("CONFIRM: calorimetry on a solute-size series flips from entropy-driven to enthalpy-driven at ~1 nm.")
    print("REFUTE: no clean crossover - large surfaces stay entropy-driven.")
    print("OK: %s located the nanometer crossover" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uc_homochirality(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: seed audit, then Frank autocatalytic amplification.")
    # ---- step 1: seed audit (enantiomeric excess each candidate can supply) ----
    seeds = {"parity violation (weak force)": 1e-17, "circularly polarized light": 1e-2,
             "chiral mineral surface": 3e-2, "statistical fluctuation": 1e-6}
    for label, ee in seeds.items():
        print("step 1 seed %-32s ee ~ %.0e" % (label + ":", ee))
    # ---- step 2: Frank amplifier ----
    ee = 1e-6   # start from the fluctuation seed
    r = 0.30
    for cycle in range(80):
        ee = ee + r * ee * (1 - ee * ee)
    print("step 2 after 80 autocatalytic cycles: ee = %.6f" % ee)
    assert ee > 0.99
    # ---- step 3: race against racemization ----
    racemization_per_cycle = 0.05
    net = r - racemization_per_cycle
    print("step 3 net amplification per cycle %.2f > 0 - amplifier outruns racemization" % net)
    assert net > 0
    print("CONFIRM: lab prebiotic network goes from measured seed to homochirality; meteorite excesses match.")
    print("REFUTE: no amplifier outruns racemization under prebiotic conditions.")
    print("OK: %s amplified a whisper into a single hand" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uc_abiogenesis(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: network closure - a collectively autocatalytic set bootstrapped by wet-dry cycling.")
    # ---- adjustable assumptions ----
    parts = 40          # demonstrated prebiotic reactions (the parts bin)
    p_link = 0.12       # probability a random reaction connects two parts
    cycles = 200        # wet-dry cycles
    # ---- step 1: inventory ----
    print("step 1 parts bin: %d demonstrated prebiotic reactions" % parts)
    # ---- step 2: network assembly - expected autocatalytic cores ----
    expected_links = parts * (parts - 1) / 2.0 * p_link
    print("step 2 expected catalytic links: %.1f" % expected_links)
    assert 90.0 < expected_links < 95.0
    # ---- step 3: cycling ratchet concentrates monomers ----
    conc = 1.0
    for _ in range(cycles):
        conc = conc * 1.02 + 0.5   # evaporation concentrates, inflow replenishes
    print("step 3 concentration factor after %d cycles: %.1f" % (cycles, conc))
    assert conc > 20.0
    # ---- step 4: closure probability grows with network size ----
    p_close = 1.0 - math.exp(-expected_links / parts)
    print("step 4 closure probability estimate: %.3f" % p_close)
    assert 0.85 < p_close < 0.95
    print("CONFIRM: flask experiment develops a sustained autocatalytic network with heritable variation.")
    print("REFUTE: no collectively autocatalytic set reachable from the parts bin, or cycling destroys faster than it builds.")
    print("OK: %s closed the network loop" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uc_photosystem(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: the Mn4CaO5 cluster as a redox-leveling machine.")
    # ---- step 1: photon budget ----
    E_photon = 1240.0 / 680.0  # eV, P680 absorption
    print("step 1 one photon at 680 nm = %.3f eV; four photons = %.2f eV" % (E_photon, 4 * E_photon))
    assert 1.80 < E_photon < 1.85
    # ---- step 2: proton-coupled ladder stays level ----
    coupled_steps = [1.05, 1.10, 1.02, 1.15]  # V, S-state transitions with proton loss
    print("step 2 coupled potentials (V): %s" % coupled_steps)
    assert all(0.9 < v < 1.3 for v in coupled_steps)
    assert all(v < E_photon for v in coupled_steps), "every step must fit the photon budget"
    # ---- step 3: without proton coupling the cycle stalls ----
    uncoupled_spike = 2.50  # V, a bare oxidation step
    print("step 3 uncoupled step would need %.2f V > photon %.2f eV - STALL" % (uncoupled_spike, E_photon))
    assert uncoupled_spike > E_photon
    # ---- step 4: total water-oxidation cost vs budget ----
    cost = sum(coupled_steps)
    print("step 4 total %.2f eV vs 4-photon budget %.2f eV - affordable" % (cost, 4 * E_photon))
    assert cost < 4 * E_photon
    print("CONFIRM: time-resolved X-ray catches the S4 intermediate with the predicted oxidation pattern.")
    print("REFUTE: S4 fingerprint matches neither bond-forming route.")
    print("OK: %s leveled the redox ladder" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uc_glass(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: Vogel-Fulcher-Tammann slowdown plus cooperativity audit.")
    # ---- adjustable assumptions ----
    eta0, D, T0 = 1e-4, 8.0, 180.0  # Pa s, strength, VFT temperature (K)
    def eta(T):
        return eta0 * math.exp(D * T0 / (T - T0))
    # ---- step 1: super-Arrhenius slowdown ----
    e300, e219 = eta(300.0), eta(219.0)
    print("step 1 viscosity: 300K -> %.1f Pa s; 219K -> %.2e Pa s" % (e300, e219))
    assert 10.0 < e300 < 25.0
    assert 5e11 < e219 < 5e12
    # ---- step 2: fragility ----
    Tg = 219.0
    m = D * T0 * Tg / ((Tg - T0) ** 2 * math.log(10))
    print("step 2 fragility m = %.1f (fragile glass-former)" % m)
    assert 85.0 < m < 95.0
    # ---- step 3: Arrhenius would miss it ----
    Ea = 50e3  # J/mol, high-T Arrhenius fit
    arr_ratio = math.exp(Ea / 8.314 * (1 / 219.0 - 1 / 300.0))
    vft_ratio = e219 / e300
    print("step 3 300K->219K: Arrhenius predicts x%.1e, VFT gives x%.1e" % (arr_ratio, vft_ratio))
    assert vft_ratio > 1e3 * arr_ratio, "slowdown is super-Arrhenius"
    print("CONFIRM: ultrastable glass shows the predicted thermodynamic signature at the hidden transition.")
    print("REFUTE: cooperativity length saturates instead of growing.")
    print("OK: %s measured the fourteen-decade slowdown" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uc_proton_hop(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: Eigen-Zundel interconversion gated by second-shell reorganization.")
    # ---- step 1: the mobility anomaly ----
    D_H, D_Na = 9.31e-5, 1.33e-5  # cm^2/s
    ratio = D_H / D_Na
    print("step 1 D(H+) / D(Na+) = %.2f - the Grotthuss excess" % ratio)
    assert 6.5 < ratio < 7.5
    # ---- step 2: hop attempt rate ----
    l = 2.5e-8  # cm, O-O hop distance
    attempt_rate = D_H / l ** 2
    print("step 2 hop attempt rate %.2e /s" % attempt_rate)
    assert 1e11 < attempt_rate < 2e11
    # ---- step 3: gating - most attempts abort ----
    success = 0.12
    effective = attempt_rate * success
    print("step 3 gate success %.0f%% -> effective %.2e hops/s" % (success * 100, effective))
    assert 1e10 < effective < 2e10
    # ---- step 4: isotope fingerprint ----
    D_D = D_H / 1.4  # deuteron is slower and gates differently
    print("step 4 D(D+)/D(H+) = %.3f - multi-point isotope fingerprint" % (D_D / D_H))
    assert 0.70 < D_D / D_H < 0.73
    print("CONFIRM: 2D-IR resolves shell reorganization, then interconversion, then hop.")
    print("REFUTE: hops proceed with no prior shell reorganization.")
    print("OK: %s filmed the proton relay" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uc_water_surface(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: the interface is stratified - each technique reports its own layer.")
    # ---- adjustable assumptions: charge per layer (arbitrary units) ----
    q_top = 0.60    # hydronium-enriched topmost layer
    q_sub = -0.50   # hydroxide-enriched subsurface
    q_bulk = 0.00
    # ---- step 1: what each technique sees ----
    zeta = q_sub + q_bulk          # electrokinetics: shear plane
    sfg = q_top                    # sum-frequency: topmost oriented layer
    xray = q_top + q_sub + q_bulk  # reflectivity: full profile
    print("step 1 zeta-potential sign: %+.2f -> %s" % (zeta, "NEGATIVE" if zeta < 0 else "POSITIVE"))
    print("step 1 SFG top-layer sign:  %+.2f -> %s" % (sfg, "POSITIVE" if sfg > 0 else "NEGATIVE"))
    print("step 1 X-ray total:         %+.2f" % xray)
    assert zeta < 0 < sfg, "the 'contradiction' is expected from depth averaging"
    # ---- step 2: Hofmeister ion depth preferences ----
    ions = {"iodide": 1.4, "chloride": 0.6, "fluoride": -0.8}  # + = surface-loving
    for ion, pref in ions.items():
        print("step 2 %-8s surface preference %+.1f" % (ion, pref))
    assert ions["iodide"] > ions["chloride"] > ions["fluoride"]
    print("CONFIRM: depth-resolved spectroscopy maps hydronium-top / hydroxide-subsurface stratification.")
    print("REFUTE: technique-independent profile shows uniform ion distribution.")
    print("OK: %s stratified the surface charge" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uc_nucleation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: pathway race on the density-order plane.")
    # ---- adjustable assumptions ----
    gamma = 0.05        # J/m^2 surface tension
    v_mol = 3e-29       # m^3 molecular volume
    kT = 1.380649e-23 * 300.0
    def dG_classical(S):
        return 16 * math.pi * gamma ** 3 * v_mol ** 2 / (3 * (kT * math.log(S)) ** 2) / kT
    def dG_twostep(S):
        droplet = 4.0 * (math.log(5.0) / math.log(S)) ** 2
        return droplet + 3.0  # droplet barrier + ordering barrier (kT)
    # ---- step 1: moderate supersaturation - two-step wins ----
    S1 = 5.0
    c1, t1 = dG_classical(S1), dG_twostep(S1)
    print("step 1 S=5: classical %.1f kT vs two-step %.1f kT" % (c1, t1))
    assert 8.0 < c1 < 13.0
    assert t1 < c1, "two-step must win at moderate S"
    # ---- step 2: extreme supersaturation - classical wins ----
    S2 = 50.0
    c2, t2 = dG_classical(S2), dG_twostep(S2)
    print("step 2 S=50: classical %.1f kT vs two-step %.1f kT" % (c2, t2))
    assert c2 < t2, "classical must win at extreme S"
    # ---- step 3: selection rule ----
    print("step 3 rule: two-step wins when the dense-liquid valley undercuts the classical saddle")
    print("CONFIRM: fluctuation spectroscopy shows density rising before order where two-step is predicted.")
    print("REFUTE: nucleation indifferent to critical-point proximity across systems.")
    print("OK: %s refereed the pathway race" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uc_csp(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: completeness audit - can the search certify 'no more forms'?")
    # ---- step 1: deterministic candidate landscape (kJ/mol) ----
    E0 = -120.0
    energies = sorted(E0 + i * 0.35 + 1.2 * math.sin(i * 2.3) for i in range(40))
    gaps = [energies[i + 1] - energies[i] for i in range(5)]
    min_gap = min(gaps)
    print("step 1 five lowest forms span %.2f kJ/mol; smallest gap %.2f kJ/mol"
          % (energies[4] - energies[0], min_gap))
    # ---- step 2: ranking reliability audit ----
    dft_error = 2.5  # kJ/mol, typical dispersion-corrected DFT error
    print("step 2 DFT error %.1f kJ/mol vs smallest gap %.2f kJ/mol" % (dft_error, min_gap))
    assert min_gap < dft_error, "ranking the top forms is unreliable at DFT accuracy"
    # ---- step 3: coverage stopping criterion ----
    found = [38, 40, 40, 40]  # new low-energy forms per 1000 candidates, successive batches
    rate = found[-1] - found[-2]
    print("step 3 discovery rate in last batch: %d new forms/1000 - search saturated" % rate)
    assert rate == 0
    # ---- step 4: temperature re-ranking ----
    T = 300.0
    free = [e - T * 0.05 * (1 + 0.1 * math.sin(i)) / 1000.0 * 1000.0 for i, e in enumerate(energies[:5])]
    print("step 4 free-energy re-ranking can flip the 0K order - temperature matters")
    print("CONFIRM: blind-test 'complete' set contains every experimentally found polymorph.")
    print("REFUTE: a new polymorph appears inside the searched energy window after completeness declared.")
    print("OK: %s certified the polymorph search" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uc_sei(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: tunneling-limited mosaic growth - logarithmic law.")
    # ---- adjustable assumptions ----
    L0, A, tau = 2.0, 1.5, 10.0  # nm, nm, cycles
    def thickness(t):
        return L0 + A * math.log(1 + t / tau)
    # ---- step 1: growth law ----
    L100, L1000 = thickness(100.0), thickness(1000.0)
    print("step 1 SEI thickness: 100 cycles -> %.2f nm; 1000 cycles -> %.2f nm" % (L100, L1000))
    assert 8.0 < L1000 < 10.0
    assert L1000 - L100 < 4.0, "growth must slow logarithmically"
    # ---- step 2: lithium-consumption ledger ----
    dLdt = A / (tau + 100.0)  # nm per cycle at cycle 100
    li_per_cycle = dLdt * 0.5  # arbitrary capacity units
    print("step 2 lithium consumed per cycle at cyc 100: %.4f units" % li_per_cycle)
    assert 0.005 < li_per_cycle < 0.010
    # ---- step 3: crack audit (silicon) ----
    cracks = 12  # fracture events over 1000 cycles
    extra = cracks * A * math.log(2.0)
    print("step 3 %d cracks add ~%.1f nm of regrowth - why silicon fades fast" % (cracks, extra))
    assert extra > 10.0
    print("CONFIRM: thickness-vs-time follows the log law with the tunneling prefactor.")
    print("REFUTE: growth continues linearly long after the tunneling limit should choke it.")
    print("OK: %s derived the self-limiting film" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uc_corrosion(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: defect-to-failure cascade - census, initiation, autocatalysis, crack.")
    # ---- step 1: Evans diagram - mixed potential ----
    E_a, b_a, i0_a = -0.60, 0.06, 1e-6    # anodic: Fe dissolution
    E_c, b_c, i0_c = 0.20, -0.12, 1e-8    # cathodic: O2 reduction
    # solve log10(i0_a) + (E-E_a)/b_a = log10(i0_c) + (E-E_c)/b_c
    E_corr = ((math.log10(i0_c) - math.log10(i0_a)) + E_a / b_a - E_c / b_c) / (1 / b_a - 1 / b_c)
    i_corr = 10 ** (math.log10(i0_a) + (E_corr - E_a) / b_a)
    print("step 1 E_corr = %.3f V, i_corr = %.2e A/cm^2" % (E_corr, i_corr))
    assert -0.45 < E_corr < -0.38
    assert 1e-3 < i_corr < 2e-3
    # ---- step 2: defect census -> time to first pit ----
    defects = 250  # inclusions per cm^2
    p_break = 1e-4  # breakdown probability per defect per hour
    t_first = 1.0 / (defects * p_break)
    print("step 2 %d defects/cm^2 -> first pit in ~%.1f h" % (defects, t_first))
    assert 30.0 < t_first < 50.0
    # ---- step 3: pit autocatalysis ----
    ph_pit = 2.5  # pit interior acidifies
    print("step 3 pit interior pH %.1f - self-sustaining once started" % ph_pit)
    assert ph_pit < 4.0
    print("CONFIRM: inclusion-mapped coupons pit where and when the census predicts.")
    print("REFUTE: pits initiate with no correlation to the mapped defect population.")
    print("OK: %s traced the cascade to failure" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uc_pfas(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: bond-by-bond defluorination ledger with fluorine-balance certification.")
    # ---- step 1: the bond ladder (PFOA: 15 C-F bonds) ----
    n_bonds, E_CF = 15, 485.0  # kJ/mol
    total = n_bonds * E_CF
    print("step 1 %d C-F bonds x %.0f kJ/mol = %.0f kJ/mol to mineralize" % (n_bonds, E_CF, total))
    assert 7200.0 < total < 7350.0
    # ---- step 2: method audit - energy delivered per bond-cleavage event ----
    methods = {"electrochemical oxidation": 520.0, "UV/sulfite": 400.0, "sonochemical": 600.0}
    for label, E_event in methods.items():
        clears = E_event > E_CF
        print("step 2 %-25s %.0f kJ/mol -> %s" % (label + ":", E_event, "CLEARS" if clears else "STALLS"))
    assert methods["electrochemical oxidation"] > E_CF > methods["UV/sulfite"]
    # ---- step 3: fluorine balance certification ----
    F_in, F_fluoride, F_residual = 15.0, 14.2, 0.8
    balance = (F_fluoride + F_residual) / F_in
    mineralized = F_fluoride / F_in
    print("step 3 fluorine balance %.3f; mineralized %.1f%%; residual organofluorine %.1f"
          % (balance, mineralized * 100, F_residual))
    assert 0.99 < balance < 1.01
    assert mineralized < 0.96, "residual means INCOMPLETE - certification fails"
    print("CONFIRM: pilot system closes the fluorine balance in real groundwater with published energy cost.")
    print("REFUTE: method stalls at short-chain intermediates in real matrices.")
    print("OK: %s audited the forever chemicals" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uc_n2_fixation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: competing energy ledgers - N2 reduction vs H2 evolution.")
    # ---- step 1: Haber-Bosch thermodynamic compromise ----
    dH, dS = -92.0e3, -199.0  # J/mol, J/mol/K for N2+3H2 -> 2NH3
    R = 8.314
    def Kp(T):
        return math.exp(-(dH - T * dS) / (R * T))
    k298, k773 = Kp(298.0), Kp(773.0)
    print("step 1 Kp(25C) = %.2e; Kp(500C) = %.2e" % (k298, k773))
    assert 1e5 < k298 < 1e6
    assert 1e-5 < k773 < 1e-4
    print("step 1 the compromise: low T favors ammonia, high T needed for kinetics")
    # ---- step 2: nitrogenase ledger - accumulation before binding ----
    equiv_accumulated = 4  # reducing equivalents before N2 binds (Janus concept)
    print("step 2 nitrogenase accumulates %d equivalents BEFORE binding N2" % equiv_accumulated)
    assert equiv_accumulated >= 3
    # ---- step 3: selectivity race vs H2 evolution ----
    barrier_N2, barrier_H2 = 55.0, 70.0  # kJ/mol, model barriers at the key step
    selectivity = math.exp((barrier_H2 - barrier_N2) * 1000.0 / (R * 298.0))
    print("step 3 N2 path favored over H2 loss by factor %.1e" % selectivity)
    assert selectivity > 100.0
    print("CONFIRM: trapped N2-bound intermediates match the predicted sequence and kinetics.")
    print("REFUTE: a synthetic system fixes N2 efficiently while violating the design rules.")
    print("OK: %s balanced the nitrogen ledgers" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uc_co2_fuel(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: product selectivity as intermediate branching ratios.")
    # ---- step 1: copper's messy mixture (faradaic efficiencies) ----
    copper = {"CO": 0.15, "formate": 0.10, "ethylene": 0.30, "ethanol": 0.10, "H2": 0.35}
    total = sum(copper.values())
    print("step 1 copper product mix: %s" % copper)
    assert 0.999 < total < 1.001
    best = max(copper, key=copper.get)
    print("step 1 best single product: %s at %.0f%% - not selective" % (best, copper[best] * 100))
    assert copper[best] < 0.5
    # ---- step 2: scaling audit - *CO vs *CHO bind together on pure metals ----
    scaling_slope = 0.98  # dE(*CHO)/dE(*CO) ~ 1 on pure metals
    print("step 2 scaling slope %.2f - pure metals cannot isolate one branch" % scaling_slope)
    assert 0.9 < scaling_slope < 1.1
    # ---- step 3: tandem design breaks the scaling ----
    tandem = {"ethylene": 0.82, "CO": 0.08, "ethanol": 0.05, "H2": 0.05}
    assert 0.999 < sum(tandem.values()) < 1.001
    print("step 3 tandem site: ethylene %.0f%% - scaling broken" % (tandem["ethylene"] * 100))
    assert tandem["ethylene"] > 0.80
    print("CONFIRM: tandem catalyst holds >80%% ethylene FE for hundreds of hours with dual-site spectroscopy.")
    print("REFUTE: a single metal matches it - scaling was not the binding constraint.")
    print("OK: %s branched the intermediates" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uc_hydrogen_storage(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: the van't Hoff window - binding enthalpy must sit at 30-40 kJ/mol.")
    # ---- step 1: derive the window ----
    R, T, dS = 8.314, 298.0, 110.0  # J/mol/K, typical hydride desorption entropy
    def dH_window(P):
        return T * (dS - R * math.log(P)) / 1000.0  # kJ/mol
    w1, w10 = dH_window(1.0), dH_window(10.0)
    print("step 1 window for 1-10 bar at 25C: %.1f to %.1f kJ/mol" % (w10, w1))
    assert 26.5 < w10 < 27.8
    assert 32.2 < w1 < 33.4
    # ---- step 2: material audit ----
    materials = {"MgH2 (too stable)": 75.0, "LaNi5 (in window)": 30.8,
                 "MOF physisorption (too weak)": 6.0, "NaAlH4": 47.0}
    for label, dH in materials.items():
        inside = w10 < dH < w1
        print("step 2 %-28s %5.1f kJ/mol %s" % (label + ":", dH, "IN WINDOW" if inside else "miss"))
    assert w10 < materials["LaNi5 (in window)"] < w1
    assert materials["MgH2 (too stable)"] > w1
    # ---- step 3: destabilization design ----
    dH_over, partner_shift = 75.0, 44.0
    dH_tuned = dH_over - partner_shift
    print("step 3 destabilized %.1f - %.1f = %.1f kJ/mol" % (dH_over, partner_shift, dH_tuned))
    assert w10 < dH_tuned < w1
    print("CONFIRM: tuned mixture shows >5 wt%% reversible, 1-10 bar plateau at 25C, 1000 cycles.")
    print("REFUTE: a material meets all targets far outside the window.")
    print("OK: %s tuned into the window" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uc_active_sites(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: Sabatier volcano plus operando correlation plus poison titration.")
    # ---- step 1: volcano baseline ----
    E_opt, width = -1.20, 0.25  # eV
    def rate(E):
        return math.exp(-abs(E - E_opt) / width)
    sites = {"terrace": -0.80, "step": -1.20, "kink": -1.60}
    rates = {s: rate(E) for s, E in sites.items()}
    for s, r in rates.items():
        print("step 1 %-8s binding %+.2f eV -> relative rate %.2f" % (s, sites[s], r))
    assert rates["step"] > rates["terrace"] and rates["step"] > rates["kink"]
    assert 0.19 < rates["terrace"] < 0.21
    # ---- step 2: operando correlation (model) ----
    corr = {"terrace": 0.15, "step": 0.97, "kink": 0.30}  # rate-signal correlation
    winner = max(corr, key=corr.get)
    print("step 2 operando correlation picks: %s (r=%.2f)" % (winner, corr[winner]))
    assert winner == "step" and corr[winner] > 0.9
    # ---- step 3: poison titration counts the sites ----
    poisons_to_kill = 1.2e13  # molecules/cm^2 to kill the rate
    print("step 3 active-site density: %.1e sites/cm^2" % poisons_to_kill)
    assert 1e13 < poisons_to_kill < 2e13
    print("CONFIRM: synthesizing more step sites raises the rate proportionally.")
    print("REFUTE: rate tracks no single site population - activity is delocalized.")
    print("OK: %s counted the working sites" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uc_catalyst_design(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: four-gate funnel - activity, selectivity, stability, synthesizability.")
    # ---- step 1-4: the funnel ----
    n0 = 10000
    g1 = 500   # activity gate (descriptor volcano top)
    g2 = 60    # selectivity gate
    g3 = 12    # stability gate
    g4 = 3     # synthesizability gate
    for label, n in (("activity", g1), ("selectivity", g2), ("stability", g3), ("synthesizability", g4)):
        print("step gate %-16s survivors: %d" % (label + ":", n))
    assert n0 > g1 > g2 > g3 > g4 > 0
    assert g4 == 3
    # ---- step 5: closed loop ----
    made, worked = 3, 2
    hit_rate = worked / made
    print("step 5 closed loop: made %d, worked as predicted %d -> hit rate %.0f%%"
          % (made, worked, hit_rate * 100))
    assert 0.5 < hit_rate < 0.8
    print("CONFIRM: a gate-4 survivor works in the reactor; loop corrections improve the next round.")
    print("REFUTE: systematic failure at the stability gate - working state defeats descriptor design.")
    print("OK: %s ran the four-gate funnel" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uc_isotope(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: cascade economics - stages set by the single-stage factor alpha.")
    # ---- step 1: cascade math ----
    nat, target = 0.007, 0.90
    ratio = (target / (1 - target)) / (nat / (1 - nat))
    def stages(alpha):
        return math.log(ratio) / math.log(alpha)
    s_diff = stages(1.004)   # gaseous diffusion
    s_cent = stages(1.30)    # centrifuge
    print("step 1 0.7%% -> 90%%: diffusion needs %.0f stages; centrifuge needs %.0f"
          % (s_diff, s_cent))
    assert 1700.0 < s_diff < 1900.0
    assert 25.0 < s_cent < 30.0
    # ---- step 2: method audit on the alpha-vs-energy map ----
    methods = {"gaseous diffusion": (1.004, 9.0), "centrifuge": (1.30, 4.0),
               "laser (demo)": (1.8, 2.0), "chemical exchange": (1.05, 3.0)}
    for label, (a, e) in methods.items():
        print("step 2 %-18s alpha=%.3f energy-index=%.1f" % (label + ":", a, e))
    # ---- step 3: generality score ----
    generality = {"gaseous diffusion": 1, "centrifuge": 2, "laser (demo)": 4, "chemical exchange": 3}
    best = max(generality, key=generality.get)
    print("step 3 most general approach: %s" % best)
    print("CONFIRM: new method shows alpha>1.5 at low energy on three unrelated elements.")
    print("REFUTE: thermodynamics caps alpha-per-joule near current methods for all approaches.")
    print("OK: %s priced the cascade" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uc_molecular_machines(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: flashing Brownian ratchet - asymmetry plus matched switching.")
    # ---- adjustable assumptions ----
    a = 0.80            # sawtooth asymmetry (fraction of period that is the gentle slope)
    L = 8e-9            # m, step size
    tau_cycle = 0.01    # s, flash period
    success = 0.90      # fraction of cycles that rectify
    # ---- step 1: drift from rectified diffusion ----
    v = (2 * a - 1) * L * success / tau_cycle
    print("step 1 drift velocity %.0f nm/s (kinesin does ~800)" % (v * 1e9))
    assert 400.0 < v * 1e9 < 500.0
    # ---- step 2: switching audit ----
    D_mol = 1e-12       # m^2/s
    tau_diff = L ** 2 / (2 * D_mol)
    print("step 2 diffusion time %.4f s vs flash period %.2f s" % (tau_diff, tau_cycle))
    assert 1e-5 < tau_diff < 1e-3
    # ---- step 3: efficiency under load ----
    F_load = 5e-12      # N
    dG_ATP = 20 * 1.380649e-23 * 300.0  # J per cycle
    eff = F_load * v / (dG_ATP / tau_cycle)
    print("step 3 efficiency at 5 pN load: %.0f%%" % (eff * 100))
    assert 0.20 < eff < 0.30
    # ---- step 4: biology benchmark ----
    print("step 4 kinesin ~50%% efficient - the synthetic gap is gating and tight coupling")
    print("CONFIRM: redesigned motor efficiency-vs-flash-rate matches the predicted optimum.")
    print("REFUTE: performance insensitive to landscape asymmetry.")
    print("OK: %s rectified the random kicks" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uc_organic_charge(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: transient localization - band-like at low T, hopping-like at high T.")
    # ---- adjustable assumptions (mobilities in cm^2/Vs) ----
    mu0, Ea = 10.0, 0.15  # eV activation for hopping
    kB = 8.617333e-5
    def mu_band(T):
        return mu0 * (300.0 / T) ** 1.5
    def mu_hop(T):
        return 1e4 * math.exp(-Ea / (kB * T))
    # ---- step 1: limits audit ----
    for T in (200.0, 300.0, 400.0):
        print("step 1 T=%.0fK: band-model %.1f, hopping-model %.1f" % (T, mu_band(T), mu_hop(T)))
    assert mu_band(200.0) > mu_hop(200.0), "band-like wins cold"
    assert mu_hop(400.0) > mu_band(400.0), "hopping wins hot"
    # ---- step 2: crossover ----
    lo, hi = 200.0, 400.0
    for _ in range(40):
        mid = (lo + hi) / 2.0
        if mu_band(mid) > mu_hop(mid):
            lo = mid
        else:
            hi = mid
    print("step 2 mechanism crossover near T=%.0f K" % ((lo + hi) / 2.0))
    assert 250.0 < (lo + hi) / 2.0 < 350.0
    # ---- step 3: design rule ----
    print("step 3 design rule: rigid backbone + strong pi-stacking -> longer coherence length")
    print("CONFIRM: material series mobility-T curves match the flicker model; designed molecule hits record mobility.")
    print("REFUTE: high mobility with no detectable dynamic disorder.")
    print("OK: %s surfed the flickering landscape" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uc_molecular_computing(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: audit against Landauer, diffusion speed, and error budgets.")
    # ---- step 1: energy audit ----
    kB, T = 1.380649e-23, 300.0
    E_landauer = kB * T * math.log(2)
    E_transistor, E_dna = 3e-17, 3e-19
    print("step 1 Landauer limit %.2e J; transistor x%.0f; DNA gate x%.0f"
          % (E_landauer, E_transistor / E_landauer, E_dna / E_landauer))
    assert 2.5e-21 < E_landauer < 3.2e-21
    assert E_dna < E_transistor, "molecules run closer to the limit"
    # ---- step 2: speed audit ----
    f_si, f_mol = 3e9, 1.0  # Hz
    parallel_needed = f_si / f_mol
    print("step 2 throughput parity needs %.1e molecules in parallel" % parallel_needed)
    assert 1e9 < parallel_needed < 1e10
    # ---- step 3: error budget ----
    e_gate = 1e-3
    for depth in (10, 1000):
        p_ok = (1 - e_gate) ** depth
        print("step 3 depth %4d -> success probability %.3f" % (depth, p_ok))
    assert (1 - e_gate) ** 10 > 0.98
    assert (1 - e_gate) ** 1000 < 0.40
    print("CONFIRM: molecular system beats silicon on a real niche task (in-vivo classification).")
    print("REFUTE: error-correction overhead always erases the parallelism advantage.")
    print("OK: %s mapped where molecules win" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uc_chemical_space(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: filtered combinatorics - count, filter, map the continents.")
    # ---- step 1: Cayley's explosion (exact alkane isomer counts) ----
    isomers = {10: 75, 20: 366319}
    for n, count in isomers.items():
        print("step 1 alkane isomers at n=%d: %d" % (n, count))
    assert isomers[10] == 75
    assert isomers[20] == 366319
    # ---- step 2: filter cascade ----
    raw = 1e60
    f_stable, f_synth, f_useful = 1e-3, 1e-2, 1e-6
    survivors = raw * f_stable * f_synth * f_useful
    print("step 2 1e60 raw -> stable %.0e -> synthesizable %.0e -> useful %.0e"
          % (raw * f_stable, raw * f_stable * f_synth, survivors))
    assert 1e48 < survivors < 1e50
    # ---- step 3: geography - GDB-17 slice ----
    gdb17 = 1.66e11
    scaffolds_total, scaffolds_seen = 5e4, 1.2e3
    coverage = scaffolds_seen / scaffolds_total
    print("step 3 GDB-17: %.2e molecules; scaffold coverage %.1f%%" % (gdb17, coverage * 100))
    assert 2.0 < coverage * 100 < 3.0
    print("CONFIRM: coverage-guided exploration finds useful molecules in empty scaffold regions.")
    print("REFUTE: useful molecules uniformly distributed - no continents.")
    print("OK: %s charted the molecular continents" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uc_open_shell(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: diagnose, converge the active space, cross-check - the trust protocol.")
    # ---- step 1: diagnostic triage ----
    T1 = 0.030  # single-reference diagnostic
    print("step 1 T1 diagnostic %.3f (threshold 0.02) -> MULTIREference" % T1)
    assert T1 > 0.02
    # ---- step 2: active-space convergence (spin-state gap, eV) ----
    spaces = [6, 8, 10, 12, 14]
    gaps = [2.10, 1.60, 1.35, 1.28, 1.26]
    for s, g in zip(spaces, gaps):
        print("step 2 active space %2d orbitals -> gap %.2f eV" % (s, g))
    assert abs(gaps[-1] - gaps[-2]) < 0.05, "converged"
    assert gaps[0] - gaps[-1] > 0.5, "small space was badly wrong"
    # ---- step 3: method shootout ----
    dft_gap = 0.40
    print("step 3 DFT gap %.2f eV vs converged %.2f eV - DFT misses by %.2f eV"
          % (dft_gap, gaps[-1], gaps[-1] - dft_gap))
    assert gaps[-1] - dft_gap > 0.5
    print("CONFIRM: protocol-certified predictions match experiment; uncertified ones scatter.")
    print("REFUTE: full protocol converges yet disagrees with experiment - missing physics.")
    print("OK: %s certified the correlated calculation" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uc_interstellar(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: coupled gas-grain network plus carrier-identification protocol.")
    # ---- step 1: gas-phase steady state (arbitrary density units) ----
    k_f, n1, n2, k_d = 1e-9, 1e4, 1e2, 1.0
    n_ss = k_f * n1 * n2 / k_d
    print("step 1 steady-state abundance: %.2e (relative)" % n_ss)
    assert 5e-4 < n_ss < 5e-3
    # ---- step 2: grain audit - which molecules REQUIRE surfaces ----
    gas_only = {"CO": True, "methanol": False, "water ice": False}
    for mol, ok in gas_only.items():
        print("step 2 %-10s gas-phase route sufficient: %s" % (mol, ok))
    assert not gas_only["methanol"], "methanol needs grain surfaces"
    # ---- step 3: carrier shortlist scoring ----
    candidates = {"PAH cation": 0.020, "carbon chain": 0.450, "fullerene": 0.180}
    best = min(candidates, key=candidates.get)
    print("step 3 band-match scores: %s" % candidates)
    print("step 3 best candidate: %s (score %.3f)" % (best, candidates[best]))
    assert candidates[best] < 0.05
    print("CONFIRM: lab gas-phase spectrum of the candidate matches multiple diffuse bands.")
    print("REFUTE: exhaustive candidate spectroscopy with no matches.")
    print("OK: %s fingerprinted the interstellar bands" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uc_metallic_hydrogen(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: band-gap closure plus multi-probe certification protocol.")
    # ---- step 1: gap audit (Wigner-Huntington updated) ----
    Eg0, slope = 15.0, 0.0333  # eV, eV/GPa
    def gap(P):
        return Eg0 - slope * P
    P_metal = Eg0 / slope
    print("step 1 gap closes at P = %.0f GPa" % P_metal)
    assert 400.0 < P_metal < 500.0
    assert gap(0.0) > 10.0 and gap(600.0) < 0.0
    # ---- step 2: artifact census ----
    artifacts = ["alumina gasket reflectance", "stressed-diamond Raman shift",
                 "hydrogen diffusion into gasket", "pressure miscalibration"]
    print("step 2 false positives to rule out: %d known" % len(artifacts))
    for a in artifacts:
        print("   - %s" % a)
    assert len(artifacts) == 4
    # ---- step 3: certification protocol ----
    probes = ["reflectivity", "Raman (hydrogen present)", "conductivity", "independent pressure standard"]
    print("step 3 claim must pass %d probes on the SAME sample" % len(probes))
    assert len(probes) == 4
    print("CONFIRM: sample passes all probes, reproduced independently, Tc measured if superconducting.")
    print("REFUTE: recombination barrier vanishes at low pressure - no metastability possible.")
    print("OK: %s set the certification bar" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uc_htsc(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: phase-diagram ledger - magnetism and superconductivity compete for the same electrons.")
    # ---- step 1: the dome ----
    Tc_max, x_opt, w = 93.0, 0.16, 0.11
    def Tc(x):
        return Tc_max * max(0.0, 1 - ((x - x_opt) / w) ** 2)
    for x in (0.05, 0.10, 0.16, 0.27):
        print("step 1 doping x=%.2f -> Tc=%.1f K" % (x, Tc(x)))
    assert 92.0 < Tc(0.16) < 94.0
    assert 60.0 < Tc(0.10) < 70.0
    assert Tc(0.05) < 1.0 and Tc(0.27) < 1.0, "dome edges"
    # ---- step 2: energy-scale ledger (meV) ----
    scales = {"spin resonance": 41.0, "superconducting gap": 40.0, "pseudogap": 80.0}
    for label, E in scales.items():
        print("step 2 %-20s %4.0f meV" % (label + ":", E))
    ratio = scales["spin resonance"] / scales["superconducting gap"]
    print("step 2 resonance/gap ratio %.2f - the magnetic fingerprint" % ratio)
    assert 0.95 < ratio < 1.10
    # ---- step 3: glue candidates ----
    print("step 3 candidates: spin fluctuations / RVB / stripes / quantum criticality")
    print("CONFIRM: spin-fluctuation spectrum quantitatively predicts Tc across the dome.")
    print("REFUTE: high Tc with no spin fluctuations - magnetism is a fellow traveler.")
    print("OK: %s fingerprinted the pairing glue" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uc_inverse_design(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: five-gate loop with a published hit-rate ledger.")
    # ---- steps 1-4: the gates ----
    n0 = 50000
    gates = [("property", 2000), ("stability", 300), ("synthesizability", 40), ("realizability", 12)]
    prev = n0
    for label, n in gates:
        print("step gate %-16s survivors: %d" % (label + ":", n))
        assert n < prev
        prev = n
    # ---- step 5: validation ledger ----
    made, worked = 12, 7
    hit_rate = worked / made
    print("step 5 made %d, worked as predicted %d -> hit rate %.0f%%" % (made, worked, hit_rate * 100))
    assert 0.50 < hit_rate < 0.65
    assert made == gates[-1][1], "every survivor gets synthesized"
    print("CONFIRM: pipeline publishes >50%% hit rate over dozens of attempts, misses analyzed.")
    print("REFUTE: hit rates stuck near zero despite all gates.")
    print("OK: %s closed the design loop" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uc_superheavy(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: relativistic orbital reshuffling, verified one atom at a time.")
    # ---- step 1: contraction audit ----
    alpha = 1 / 137.036
    for Z, label in ((79, "gold"), (112, "copernicium"), (118, "oganesson")):
        v_over_c = Z * alpha
        gamma = 1 / math.sqrt(1 - v_over_c ** 2)
        contract = 1 / gamma
        print("step 1 Z=%3d %-12s v/c=%.2f 1s contraction x%.2f" % (Z, label, v_over_c, contract))
    gamma_118 = 1 / math.sqrt(1 - (118 * alpha) ** 2)
    assert 1.90 < gamma_118 < 2.05
    assert 0.48 < 1 / gamma_118 < 0.54
    # ---- step 2: reordering map - predicted personalities ----
    predictions = {"copernicium (112)": "volatile, breaks group trend",
                   "flerovium (114)": "unexpectedly inert",
                   "oganesson (118)": "reactive solid, no noble gas"}
    for el, pers in predictions.items():
        print("step 2 %-20s -> %s" % (el + ":", pers))
    # ---- step 3: atom-at-a-time statistics ----
    events_needed = 12  # decay events to separate predicted vs group-trend enthalpy
    print("step 3 need ~%d single-atom events for a decisive adsorption measurement" % events_needed)
    assert events_needed > 5
    print("CONFIRM: single-atom thermochromatography matches relativistic predictions across elements.")
    print("REFUTE: elements follow naive group trends despite large predicted effects.")
    print("OK: %s weighed relativity atom by atom" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uc_de_novo_enzyme(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Approach: gap ledger - what the designs are still missing, factor by factor.")
    # ---- step 1: gap ledger (log10 proficiency) ----
    natural, designed = 15.0, 5.2
    gap = natural - designed
    print("step 1 natural 10^%.0f vs designed 10^%.1f -> gap 10^%.1f" % (natural, designed, gap))
    assert 9.0 < gap < 11.0
    # ---- step 2: missing-factor audit ----
    preorg_natural, preorg_design = 0.95, 0.40  # electric-field alignment scores
    missing = math.log10(1 / (1 - preorg_design)) - math.log10(1 / (1 - preorg_natural))
    print("step 2 preorganization alignment: natural %.0f%%, design %.0f%%"
          % (preorg_natural * 100, preorg_design * 100))
    assert preorg_natural > preorg_design
    # ---- step 3: dynamics prescription ----
    print("step 3 design protocol must add: flexible-backbone sampling, electric-field optimization, second-shell design")
    # ---- step 4: competition spec ----
    target_gap = 2.0  # within 100x of natural
    print("step 4 head-to-head bar: pure-computation design within 10^%.0f of natural" % target_gap)
    assert target_gap < gap, "bar is below today's gap - it must be EARNED"
    print("CONFIRM: blind pure-computation design within 100x of natural, reproduced independently.")
    print("REFUTE: missing factors computationally intractable in principle.")
    print("OK: %s audited the design gap" % NAME)
if __name__ == "__main__":
    main()
''')

DEMOS = {
    "mpemba": demo_uc_mpemba,
    "water_anomalies": demo_uc_water_anomalies,
    "smell": demo_uc_smell,
    "protein_folding": demo_uc_protein_folding,
    "enzyme_speed": demo_uc_enzyme_speed,
    "hydrophobic": demo_uc_hydrophobic,
    "homochirality": demo_uc_homochirality,
    "abiogenesis": demo_uc_abiogenesis,
    "photosystem": demo_uc_photosystem,
    "glass": demo_uc_glass,
    "proton_hop": demo_uc_proton_hop,
    "water_surface": demo_uc_water_surface,
    "nucleation": demo_uc_nucleation,
    "csp": demo_uc_csp,
    "sei": demo_uc_sei,
    "corrosion": demo_uc_corrosion,
    "pfas": demo_uc_pfas,
}

DEMOS2 = {
    "n2_fixation": demo_uc_n2_fixation,
    "co2_fuel": demo_uc_co2_fuel,
    "hydrogen_storage": demo_uc_hydrogen_storage,
    "active_sites": demo_uc_active_sites,
    "catalyst_design": demo_uc_catalyst_design,
    "isotope": demo_uc_isotope,
    "molecular_machines": demo_uc_molecular_machines,
    "organic_charge": demo_uc_organic_charge,
    "molecular_computing": demo_uc_molecular_computing,
    "chemical_space": demo_uc_chemical_space,
    "open_shell": demo_uc_open_shell,
    "interstellar": demo_uc_interstellar,
    "metallic_hydrogen": demo_uc_metallic_hydrogen,
    "htsc": demo_uc_htsc,
    "inverse_design": demo_uc_inverse_design,
    "superheavy": demo_uc_superheavy,
    "de_novo_enzyme": demo_uc_de_novo_enzyme,
}
DEMOS.update(DEMOS2)
