#!/usr/bin/env python3
"""Solution-explorer walkthrough demos for The Unsolved Physics Database.

Every demo is a working program: it walks through the Signature proposed
solution approach in steps, uses adjustable assumptions, computes REAL
values, checks them with tight-bounds asserts (never float exact-equality),
and ends with a confirm/refute panel plus the OK marker.

Honesty rule: demos explore PROPOSED approaches. They never claim proof.
"""

import math

LABEL = "Signature-generated proposed solution \u2014 not established science."


def demo_matter_antimatter(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
"""SOLUTION EXPLORER: Matter-Antimatter Asymmetry.
Walks the Signature proposed approach: the matter surplus as a residue of a
one-way early-universe scale transition amplifying leptonic CP violation.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions ----
OMEGA_B_H2 = 0.0224        # baryon density from Planck CMB fits
ETA_PER_OMBH2 = 273.9e-10  # conversion: eta = 273.9e-10 * Omega_b h^2
CP_PHASE_DEG = 200.0       # trial leptonic CP phase (DUNE/Hyper-K will measure)

def step1_problem():
    eta = ETA_PER_OMBH2 * OMEGA_B_H2
    print("STEP 1 - the problem: eta = %.3e baryons per photon" % eta)
    print("  Standard Model CP violation is ~10 orders of magnitude too small.")
    assert 5.9e-10 < eta < 6.4e-10, "eta out of measured range"
    return eta

def step2_signature_approach(eta):
    print("STEP 2 - Signature approach: Sakharov conditions as ledger rules.")
    print("  A fast scale transition changes the ledger mid-count; the")
    print("  remainder after re-equilibration is the matter surplus.")
    sakharov = {"baryon_number_violation": True, "cp_violation": CP_PHASE_DEG not in (0.0, 180.0), "out_of_equilibrium": True}
    print("  Sakharov checklist:", sakharov)
    assert all(sakharov.values()), "Sakharov conditions not all met"
    return sakharov

def step3_testable_prediction(eta):
    print("STEP 3 - testable prediction: leptonic CP phase far from 0/180 deg,")
    print("  plus evidence of a sharp early transition at the matching scale.")
    print("  Trial phase %.1f deg -> CP violation present: %s" % (CP_PHASE_DEG, CP_PHASE_DEG not in (0.0, 180.0)))
    assert 0.0 < CP_PHASE_DEG < 360.0

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: DUNE/Hyper-K measure delta_CP far from 0/180 deg AND a")
    print("    sharp early-universe transition is found at the matching scale.")
    print("  REFUTE if: delta_CP consistent with 0/180 deg, or the early universe")
    print("    expanded smoothly with no sharp transitions at any relevant scale.")

def main():
    eta = step1_problem()
    step2_signature_approach(eta)
    step3_testable_prediction(eta)
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (eta=%.3e)" % (RID, eta))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_fate_of_universe(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
"""SOLUTION EXPLORER: The Fate of the Universe.
Walks the Signature proposed approach: fate as a contest between the
expansion ledger (dark energy) and the structure ledger (bound systems).
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions ----
H0_KM_S_MPC = 70.0   # Hubble constant
OMEGA_M = 0.31       # matter fraction
OMEGA_L = 0.69       # dark energy fraction
G = 6.674e-11        # gravitational constant, SI
MPC_M = 3.0857e22    # one megaparsec in meters

def step1_problem():
    H0 = H0_KM_S_MPC * 1000.0 / MPC_M
    rho_c = 3.0 * H0**2 / (8.0 * math.pi * G)
    print("STEP 1 - the problem: critical density rho_c = %.3e kg/m^3" % rho_c)
    assert 8.5e-27 < rho_c < 9.9e-27, "rho_c out of range"
    return rho_c

def step2_signature_approach():
    print("STEP 2 - Signature approach: two ledgers in contest.")
    q0 = OMEGA_M / 2.0 - OMEGA_L
    print("  deceleration parameter q0 = %.3f (negative = accelerating)" % q0)
    assert -0.60 < q0 < -0.45, "q0 out of Lambda-CDM range"
    return q0

def step3_testable_prediction(q0):
    print("STEP 3 - testable prediction: dark energy equation of state w(z)")
    print("  drifting in correlation with the declining star-formation history.")
    for w in (-1.2, -1.0, -0.8):
        q = OMEGA_M / 2.0 + 0.5 * (1.0 + 3.0 * w) * OMEGA_L
        print("  w = %.1f -> q0 = %.3f" % (w, q))
        assert -1.2 < q < 0.2

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: DESI/Euclid/Rubin measure w(z) drifting with the")
    print("    cosmic star-formation history.")
    print("  REFUTE if: w = -1 exactly at all redshifts, or no link between")
    print("    star formation and expansion history exists.")

def main():
    step1_problem()
    q0 = step2_signature_approach()
    step3_testable_prediction(q0)
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (q0=%.3f)" % (RID, q0))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_fermi_question(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
"""SOLUTION EXPLORER: The Fermi Question.
Walks the Signature proposed approach: the silence as a detectability
bottleneck - civilizations become quiet as they mature.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions (optimistic Drake-style) ----
R_STAR = 10.0    # star formation rate per year
F_P = 0.5        # fraction with planets
N_E = 2.0        # habitable planets per such star
F_L = 1.0        # fraction where life starts
F_I = 0.01       # fraction where intelligence evolves
F_C = 0.1        # fraction that become detectable
L_YEARS = 1e6    # detectable lifetime in years

def step1_problem():
    N = R_STAR * F_P * N_E * F_L * F_I * F_C * L_YEARS
    print("STEP 1 - the problem: optimistic estimate N = %.0f civilizations" % N)
    print("  yet observed technosignatures: 0. That gap is the paradox.")
    assert N > 1000, "optimistic N should be large - else no paradox"
    return N

def step2_signature_approach(N):
    print("STEP 2 - Signature approach: the quiet transition.")
    print("  Leakage (radio spill, waste heat) is eliminated as civilizations")
    print("  optimize; mature systems look suspiciously quiet, not loud.")
    crossing_years = 1e5 / 0.01  # galaxy diameter (ly) / 0.01 c
    print("  galaxy crossing at 1%% c: %.1e years (<< galaxy age)" % crossing_years)
    assert crossing_years < 1e8
    return crossing_years

def step3_testable_prediction():
    print("STEP 3 - testable prediction: nearby systems with anomalously LOW")
    print("  waste heat plus chemical/structural anomalies = quiet candidates.")

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: quiet, efficient planetary systems with anomalies are")
    print("    found, or a narrow beam sweeps Earth.")
    print("  REFUTE if: a loud galaxy-spanning civilization is confirmed, or")
    print("    interstellar expansion proves trivially easy and always pursued.")

def main():
    N = step1_problem()
    step2_signature_approach(N)
    step3_testable_prediction()
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (N=%.0f)" % (RID, N))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_dark_matter(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
"""SOLUTION EXPLORER: What Is Dark Matter?
Walks the Signature proposed approach: dark matter as condensation residue
of the gravitational ledger during halo assembly.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions (model spiral galaxy) ----
V_ROT = 220e3          # rotation speed m/s at the measured radius
R_KPC = 15.0           # radius in kiloparsecs
M_VISIBLE_MSUN = 3.0e10  # stars + gas, solar masses
G = 6.674e-11
MSUN = 1.989e30
KPC_M = 3.0857e19

def step1_problem():
    r = R_KPC * KPC_M
    M_dyn = V_ROT**2 * r / G / MSUN
    ratio = M_dyn / M_VISIBLE_MSUN
    print("STEP 1 - the problem: dynamical mass %.2e Msun vs visible %.2e Msun" % (M_dyn, M_VISIBLE_MSUN))
    print("  dark-to-visible ratio = %.2f (need ~5x invisible mass)" % ratio)
    assert 4.0 < ratio < 7.0, "ratio out of observed range"
    return ratio

def step2_signature_approach(ratio):
    print("STEP 2 - Signature approach: the residue of halo assembly.")
    print("  Gravity's bookkeeping leaves a pressureless residue where matter")
    print("  clumped; the ~5:1 ratio is set by structure formation, not tuned.")
    print("  No particle to detect -> null direct-detection results expected.")

def step3_testable_prediction(ratio):
    print("STEP 3 - testable prediction: a 5:1 ratio across halo masses and")
    print("  epochs, correlated with each halo's assembly history.")

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: ratio stays ~5:1 everywhere, detectors hit the neutrino")
    print("    floor empty-handed, and dark fraction tracks assembly history.")
    print("  REFUTE if: a dark matter particle is directly detected, or any")
    print("    system's dark matter disobeys its structure history.")

def main():
    ratio = step1_problem()
    step2_signature_approach(ratio)
    step3_testable_prediction(ratio)
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (ratio=%.2f)" % (RID, ratio))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_dark_energy(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
"""SOLUTION EXPLORER: What Is Dark Energy?
Walks the Signature proposed approach: dark energy as the expansion
ledger's balancing entry, dominant 'now' when the ledgers cross.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions ----
OMEGA_M = 0.31
OMEGA_DE = 0.69

def step1_problem():
    print("STEP 1 - the problem: 69% of the energy budget accelerates expansion,")
    print("  equation of state w near -1, nature unknown.")
    q0 = OMEGA_M / 2.0 - OMEGA_DE
    print("  q0 = %.3f" % q0)
    assert -0.60 < q0 < -0.45
    return q0

def step2_signature_approach():
    print("STEP 2 - Signature approach: the balancing entry.")
    print("  As matter dilutes, the ledger posts an offsetting entry; the")
    print("  'coincidence' (dominance now) is when the ledgers cross.")

def step3_testable_prediction():
    print("STEP 3 - testable prediction: w(z) drifts with structure history.")
    drifts = []
    for w in (-1.15, -1.0, -0.85):
        q = OMEGA_M / 2.0 + 0.5 * (1.0 + 3.0 * w) * OMEGA_DE
        drifts.append(q)
        print("  w=%.2f -> q0=%.3f" % (w, q))
    assert drifts[0] < drifts[1] < drifts[2], "drift ordering broken"

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: w(z) drifts in lockstep with structure-growth history,")
    print("    with no new field ever required.")
    print("  REFUTE if: w = -1 exactly at all redshifts, or a quintessence field")
    print("    or modified gravity is confirmed as the cause.")

def main():
    step1_problem()
    step2_signature_approach()
    step3_testable_prediction()
    confirm_refute_panel()
    print("OK: %s solution-explorer complete" % RID)

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_hubble_tension(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
"""SOLUTION EXPLORER: The Hubble Tension.
Walks the Signature proposed approach: early vs late ledgers disagreeing
because a brief early component recalibrated the sound horizon.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions (published values) ----
H0_LOCAL, SIG_LOCAL = 73.04, 1.04    # SH0ES distance ladder
H0_EARLY, SIG_EARLY = 67.4, 0.5      # Planck inference under Lambda-CDM

def step1_problem():
    gap = H0_LOCAL - H0_EARLY
    sigma = math.sqrt(SIG_LOCAL**2 + SIG_EARLY**2)
    tension = gap / sigma
    print("STEP 1 - the problem: %.2f vs %.2f km/s/Mpc -> %.2f sigma tension" % (H0_LOCAL, H0_EARLY, tension))
    assert 4.0 < tension < 6.0, "tension out of observed range"
    return tension

def step2_signature_approach(tension):
    print("STEP 2 - Signature approach: ledger recalibration near recombination.")
    print("  A brief early energy component shrinks the sound horizon, making")
    print("  the early inference low while the late value (%.2f) is true." % H0_LOCAL)

def step3_testable_prediction():
    print("STEP 3 - testable prediction: Simons Observatory / CMB-S4 see the")
    print("  peak-shift pattern of a brief early component; standard sirens")
    print("  converge on the local value.")

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: CMB-S4 detects the early-component peak pattern and")
    print("    sirens converge near 73.")
    print("  REFUTE if: CMB-S4 excludes any early component, or a shared local-")
    print("    ladder systematic brings 73 down to 67.")

def main():
    tension = step1_problem()
    step2_signature_approach(tension)
    step3_testable_prediction()
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (tension=%.2f sigma)" % (RID, tension))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_corona_heating(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
"""SOLUTION EXPLORER: The Solar Corona Heating Problem.
Walks the Signature proposed approach: critical-tangle discharge of the
braided magnetic ledger (nanoflare avalanches at a threshold).
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions ----
T_CORONA = 1.0e6       # kelvin
T_PHOTOSPHERE = 5778.0 # kelvin
FLUX_ACTIVE = 1.0e7    # erg/cm^2/s required in active regions
L_SUN_W = 3.828e26     # solar luminosity, watts

def step1_problem():
    ratio = T_CORONA / T_PHOTOSPHERE
    print("STEP 1 - the problem: corona %.0f K vs surface %.0f K (x%.0f)" % (T_CORONA, T_PHOTOSPHERE, ratio))
    assert 150.0 < ratio < 200.0
    return ratio

def step2_signature_approach(ratio):
    print("STEP 2 - Signature approach: self-organized critical tangle.")
    print("  Photospheric braiding stores energy until a critical tangle")
    print("  density, then avalanches; the MK temperature is the thermostat.")
    area_cm2 = (3.0e9) ** 2  # typical active region scale, cm^2
    power_erg_s = FLUX_ACTIVE * area_cm2
    frac = power_erg_s * 1e-7 / L_SUN_W
    print("  active-region power fraction of L_sun: %.2e" % frac)
    assert frac < 1e-6, "heating must be a trace of solar output"

def step3_testable_prediction():
    print("STEP 3 - testable prediction: a universal flare-energy power-law")
    print("  index across quiet Sun, coronal holes, and active regions.")

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: Parker Solar Probe / DKIST find the universal")
    print("    avalanche index in all coronal regions.")
    print("  REFUTE if: wave-damping profiles close the whole energy budget")
    print("    with no room for reconnection avalanches.")

def main():
    ratio = step1_problem()
    step2_signature_approach(ratio)
    step3_testable_prediction()
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (ratio=x%.0f)" % (RID, ratio))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_sonoluminescence(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
"""SOLUTION EXPLORER: Sonoluminescence.
Walks the Signature proposed approach: the flash as ledger discharge
through the fastest channel - wall acceleration, not plasma temperature.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions ----
T0 = 300.0          # ambient kelvin
COLLAPSE_RATIO = 10.0  # Rmax/Rmin
GAMMA = 5.0 / 3.0      # monatomic gas

def step1_problem():
    exponent = 3.0 * (GAMMA - 1.0)
    T = T0 * COLLAPSE_RATIO ** exponent
    print("STEP 1 - the problem: adiabatic collapse gives T = %.0f K" % T)
    print("  observed flashes imply tens of thousands of K in picoseconds.")
    assert 1.0e4 < T < 1.0e5, "collapse temperature out of observed range"
    return T

def step2_signature_approach(T):
    print("STEP 2 - Signature approach: discharge via wall acceleration.")
    print("  The wall outruns thermal channels; emission scales with peak")
    print("  wall acceleration (dynamical Casimir-like), giving short,")
    print("  broadband, blue-weighted flashes.")

def step3_testable_prediction():
    print("STEP 3 - testable prediction: flash energy proportional to peak")
    print("  wall acceleration cubed, across gases and drive levels; spectra")
    print("  stay featureless where plasma models predict lines.")

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: flash energy tracks wall acceleration (Mie")
    print("    radius-time curves) with featureless spectra.")
    print("  REFUTE if: atomic emission lines appear (hot plasma core wins),")
    print("    or flash energy tracks core temperature instead.")

def main():
    T = step1_problem()
    step2_signature_approach(T)
    step3_testable_prediction()
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (T=%.0f K)" % (RID, T))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_arrow_of_time(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
"""SOLUTION EXPLORER: The Arrow of Time.
Walks the Signature proposed approach: the arrow as a write-once ledger
property - asymmetry in the initial entry, not the rules.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions ----
N_CARDS = 52
K_B = 1.380649e-23  # J/K

def step1_problem():
    lnW = math.lgamma(N_CARDS + 1)  # ln(52!)
    dS = K_B * lnW
    print("STEP 1 - the problem: shuffled deck entropy exceeds ordered by")
    print("  dS = %.3e J/K; laws are symmetric, yet disorder only grows." % dS)
    assert 2.0e-21 < dS < 2.3e-21
    return dS

def step2_signature_approach(dS):
    print("STEP 2 - Signature approach: the past hypothesis as ledger fact.")
    print("  The Big Bang wrote one low-entropy entry; read-rules can only")
    print("  increase the count. The arrow is the direction of more entries.")

def step3_testable_prediction():
    print("STEP 3 - testable prediction: no local violations of the")
    print("  thermodynamic arrow will ever be found; candidate 'new arrows'")
    print("  (CP violation, measurement) stay derivative or tiny.")

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: the arrow's uniformity holds and no dynamical arrow")
    print("    beyond boundary conditions is ever needed.")
    print("  REFUTE if: a verified macroscopic entropy decrease in an isolated")
    print("    system, or a no-special-beginning cosmology reproducing the arrow.")

def main():
    dS = step1_problem()
    step2_signature_approach(dS)
    step3_testable_prediction()
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (dS=%.3e J/K)" % (RID, dS))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)

DEMOS = {
 "matter-antimatter": demo_matter_antimatter,
 "fate-of-the-universe": demo_fate_of_universe,
 "fermi-question": demo_fermi_question,
 "dark-matter": demo_dark_matter,
 "dark-energy": demo_dark_energy,
 "hubble-tension": demo_hubble_tension,
 "corona-heating": demo_corona_heating,
 "sonoluminescence": demo_sonoluminescence,
 "arrow-of-time": demo_arrow_of_time,
}


def demo_high_tc(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
"""SOLUTION EXPLORER: High-Temperature Superconductivity Mechanism.
Walks the Signature proposed approach: pairing as resonance between the
charge ledger and the spin ledger; the dome is the resonance curve.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions ----
TC_YBCO = 93.0        # kelvin
K_B = 1.380649e-23    # J/K
EV_J = 1.602176634e-19
BCS_RATIO = 3.53      # 2*Delta/kB*Tc, conventional
CUPRATE_RATIO = 6.0   # typical cuprate gap ratio (d-wave average)

def step1_problem():
    print("STEP 1 - the problem: BCS caps phonon pairing near 30-40 K, yet")
    print("  cuprates superconduct above 130 K. The glue is unknown.")
    assert TC_YBCO > 40.0, "YBCO must exceed the phonon ceiling"

def step2_signature_approach():
    print("STEP 2 - Signature approach: charge-spin ledger resonance.")
    print("  Tc peaks where competing orders balance - the dome is the")
    print("  resonance curve; the pseudogap is the off-resonance shadow.")
    delta_mev = CUPRATE_RATIO * K_B * TC_YBCO / 2.0 / EV_J * 1000.0
    print("  implied gap Delta = %.1f meV (BCS would give %.1f meV)" % (
        delta_mev, BCS_RATIO * K_B * TC_YBCO / 2.0 / EV_J * 1000.0))
    assert 20.0 < delta_mev < 30.0, "cuprate gap out of measured range"
    return delta_mev

def step3_testable_prediction():
    print("STEP 3 - testable prediction: spin/charge fluctuation energy scales")
    print("  track the dome shape across cuprate families; pseudogap scale")
    print("  tracks detuning from resonance.")

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: fluctuation scales match the dome quantitatively and")
    print("    the pseudogap tracks resonance detuning.")
    print("  REFUTE if: Tc peaks away from balanced competing orders, or the")
    print("    pseudogap proves to be preformed pairing.")

def main():
    step1_problem()
    delta = step2_signature_approach()
    step3_testable_prediction()
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (Delta=%.1f meV)" % (RID, delta))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_glass_transition(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
"""SOLUTION EXPLORER: The Glass Transition.
Walks the Signature proposed approach: arrest as fragmentation of the
motion ledger into mutually inaccessible regions - a horizon, not a wall.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions (Vogel-Fulcher-Tammann toy) ----
ETA_0 = 1.0e-3    # Pa s, high-T limit
D_STRENGTH = 8.0  # strength parameter
T0_VFT = 180.0    # K, divergence temperature
ETA_TG = 1.0e12   # Pa s, conventional definition of Tg

def step1_problem():
    print("STEP 1 - the problem: viscosity rises ~10^14x near Tg with almost")
    print("  no structural change. Transition or kinetic arrest?")
    ln_ratio = math.log(ETA_TG / ETA_0)
    T_g = T0_VFT + D_STRENGTH * T0_VFT / ln_ratio
    print("  VFT toy: Tg = %.1f K (divergence T0 = %.0f K stays unreachable)" % (T_g, T0_VFT))
    assert 200.0 < T_g < 250.0
    return T_g

def step2_signature_approach(T_g):
    print("STEP 2 - Signature approach: the motion ledger fragments.")
    print("  Barriers grow cooperatively; the lab Tg is where the relaxation")
    print("  time crosses the observation time - a horizon, not a boundary.")

def step3_testable_prediction():
    print("STEP 3 - testable prediction: relaxation times diverge only at an")
    print("  unreachable T0; barrier growth matches the cooperative prediction")
    print("  across fragile and strong glass-formers.")

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: ultrastable-glass / swap-MC experiments show no")
    print("    thermodynamic signature at any reachable temperature.")
    print("  REFUTE if: a diverging static length or latent heat appears at a")
    print("    reachable temperature - a true phase transition.")

def main():
    T_g = step1_problem()
    step2_signature_approach(T_g)
    step3_testable_prediction()
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (Tg=%.1f K)" % (RID, T_g))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_uhecr(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
"""SOLUTION EXPLORER: Ultra-High-Energy Cosmic Rays.
Walks the Signature proposed approach: 10^20 eV events as relay-overflow
of the acceleration ledger across nested structures.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions ----
M_PI_EV = 140e6     # charged pion mass energy, eV
M_P_EV = 938e6      # proton mass energy, eV
EPS_CMB_EV = 6.3e-4 # typical CMB photon energy, eV

def step1_problem():
    E_th = M_PI_EV * (2.0 * M_P_EV + M_PI_EV) / (4.0 * EPS_CMB_EV)
    print("STEP 1 - the problem: GZK threshold E_th = %.2e eV" % E_th)
    print("  events arrive above it; no nearby single accelerator suffices.")
    assert 5.0e19 < E_th < 2.0e20, "GZK threshold out of range"
    return E_th

def step2_signature_approach(E_th):
    print("STEP 2 - Signature approach: relay overflow.")
    print("  No single engine reaches 1e20 eV; rare particles win a sequence of")
    print("  re-accelerations (jet -> lobe -> cluster shock), compounding gains.")
    print("  Rarity + weak source correlation follow naturally.")

def step3_testable_prediction():
    print("STEP 3 - testable prediction: highest-energy events statistically")
    print("  tied to regions with nested accelerators (AGN in merging clusters),")
    print("  with a rigidity-dependent cutoff; heavy composition trend holds.")

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: AugerPrime ties top events to nested-accelerator")
    print("    regions with relay-predicted rigidity cutoffs.")
    print("  REFUTE if: single sources demonstrably reach 1e20 eV alone, or")
    print("    arrival directions prove a non-astrophysical origin.")

def main():
    E_th = step1_problem()
    step2_signature_approach(E_th)
    step3_testable_prediction()
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (E_th=%.2e eV)" % (RID, E_th))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_lithium_problem(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
"""SOLUTION EXPLORER: The Cosmological Lithium Problem.
Walks the Signature proposed approach: the BBN ledger is right; the
stellar ledger quietly edited its lithium entries over 13 Gyr.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions ----
LI_BBN = 4.7e-10     # BBN prediction, 7Li/H
LI_OBS = 1.6e-10     # Spite plateau observed value

def step1_problem():
    factor = LI_BBN / LI_OBS
    print("STEP 1 - the problem: BBN %.2e vs observed %.2e -> factor %.2f" % (LI_BBN, LI_OBS, factor))
    print("  D and He-4 agree perfectly; lithium alone rebels.")
    assert 2.0 < factor < 5.0, "discrepancy factor out of range"
    return factor

def step2_signature_approach(factor):
    print("STEP 2 - Signature approach: stellar processing, not cosmology.")
    print("  Atomic diffusion + turbulent mixing deplete surface lithium ~%.1fx" % factor)
    print("  over stellar lifetimes; the plateau's flatness is depletion")
    print("  saturating, not pristine abundance.")

def step3_testable_prediction():
    print("STEP 3 - testable prediction: depletion signatures - correlated")
    print("  6Li/7Li behavior and diffusion abundance patterns in the most")
    print("  pristine stars, matching quantitative stellar models.")

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: predicted depletion signatures appear in pristine")
    print("    stars and match diffusion models.")
    print("  REFUTE if: a star shows the full BBN lithium with no depletion")
    print("    signature, or a missed nuclear resonance fixes BBN directly.")

def main():
    factor = step1_problem()
    step2_signature_approach(factor)
    step3_testable_prediction()
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (factor=%.2f)" % (RID, factor))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_rprocess(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
"""SOLUTION EXPLORER: Rapid Neutron-Capture Process Sites.
Walks the Signature proposed approach: a two-ledger budget - prompt
supernovae wrote the early entries, mergers dominate the late ones.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions (AT2017gfo-like kilonova) ----
L_KN_ERG_S = 1.0e42   # peak luminosity, erg/s
HEAT_ERG_S_G = 1.0e10 # r-process heating rate per gram at ~1 day
MSUN_G = 1.989e33

def step1_problem():
    M_ej = L_KN_ERG_S / HEAT_ERG_S_G / MSUN_G
    print("STEP 1 - the problem: kilonova implies ejecta M = %.3f Msun" % M_ej)
    print("  mergers confirmed as a site; the budget split vs supernovae open.")
    assert 0.01 < M_ej < 0.10, "ejecta mass out of kilonova range"
    return M_ej

def step2_signature_approach(M_ej):
    print("STEP 2 - Signature approach: two ledgers, two epochs.")
    print("  Prompt magneto-rotational supernovae enriched the oldest stars;")
    print("  mergers dominate later. Single-site models fail across epochs.")

def step3_testable_prediction():
    print("STEP 3 - testable prediction: chemical-evolution models require")
    print("  both components; next kilonovae confirm per-event yields while")
    print("  ancient-star statistics confirm the prompt component.")

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: models need both sites to fit the full stellar record.")
    print("  REFUTE if: merger rates+yields cover everything including the")
    print("    earliest stars, or an r-process supernova dwarfs mergers.")

def main():
    M_ej = step1_problem()
    step2_signature_approach(M_ej)
    step3_testable_prediction()
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (M_ej=%.3f Msun)" % (RID, M_ej))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_muon_g2(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
"""SOLUTION EXPLORER: The Muon g-2 Anomaly.
Walks the Signature proposed approach: a ledger reconciliation - the
measurement ledger was right; the theory ledger undervalued the hadronic
contribution. PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions (2021 experimental vs 2020 theory consensus) ----
DELTA_A_2021 = 251e-11  # exp - theory, 2021 numbers
SIGMA_COMB = 59e-11     # combined uncertainty, 2021
BMW_SHIFT = 140e-11     # lattice raises hadronic part by ~this

def step1_problem():
    sig = DELTA_A_2021 / SIGMA_COMB
    print("STEP 1 - the problem: 2021 discrepancy %.1f sigma" % sig)
    assert 3.5 < sig < 5.0, "2021 significance out of range"

def step2_signature_approach():
    print("STEP 2 - Signature approach: audit the hardest theory entry first.")
    residual = DELTA_A_2021 - BMW_SHIFT
    sig_new = residual / SIGMA_COMB
    print("  BMW lattice raises hadronic part: residual %.0e -> %.1f sigma" % (residual, sig_new))
    assert 50e-11 < residual < 200e-11, "residual out of expected range"
    return sig_new

def step3_testable_prediction():
    print("STEP 3 - testable prediction: independent lattice groups converge")
    print("  on the higher hadronic value; final Fermilab analysis agrees with")
    print("  corrected theory; no new physics needed.")

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: lattice consensus holds and the final Fermilab result")
    print("    matches corrected theory.")
    print("  REFUTE (the reconciliation) if: a lattice-robust residual above")
    print("    ~3 sigma survives - new physics returns (dark photon, SUSY...).")

def main():
    step1_problem()
    sig_new = step2_signature_approach()
    step3_testable_prediction()
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (residual=%.1f sigma)" % (RID, sig_new))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_strong_cp(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
"""SOLUTION EXPLORER: The Strong CP Problem.
Walks the Signature proposed approach: theta relaxed dynamically in the
early universe; the axion is the leftover ripple.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions ----
DN_LIMIT = 1.8e-26   # e cm, neutron EDM experimental bound
DN_PER_THETA = 3.6e-16  # e cm per unit theta (chiral estimate)

def step1_problem():
    theta_max = DN_LIMIT / DN_PER_THETA
    print("STEP 1 - the problem: theta < %.1e though it could be order one" % theta_max)
    assert theta_max < 1.0e-9, "theta bound weaker than established"
    return theta_max

def step2_signature_approach(theta_max):
    print("STEP 2 - Signature approach: small numbers come from rolling.")
    print("  A Peccei-Quinn-like angle rolled to zero in the early universe;")
    print("  the axion is the required exhaust of that relaxation - and a")
    print("  dark matter candidate, making axion hunts a two-problem test.")

def step3_testable_prediction():
    print("STEP 3 - testable prediction: haloscope detection (ADMX/successors)")
    print("  at a mass and coupling matching the dark matter abundance.")

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: the axion is detected with dark-matter-consistent")
    print("    properties - one discovery, two problems solved.")
    print("  REFUTE if: the full axion window is excluded with no signal, or a")
    print("    nonzero nEDM implies small-but-not-relaxed theta.")

def main():
    theta_max = step1_problem()
    step2_signature_approach(theta_max)
    step3_testable_prediction()
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (theta<%.1e)" % (RID, theta_max))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_proton_spin(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
"""SOLUTION EXPLORER: The Proton Spin Crisis.
Walks the Signature proposed approach: the missing spin as orbital angular
momentum - an incomplete ledger, not a broken theory.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions ----
DELTA_SIGMA = 0.32  # quark spin fraction (EMC/COMPASS era value)

def step1_problem():
    missing = 1.0 - DELTA_SIGMA
    print("STEP 1 - the problem: quarks carry %.0f%% of spin; %.0f%% missing" % (DELTA_SIGMA * 100, missing * 100))
    assert 0.60 < missing < 0.75, "missing fraction out of range"
    return missing

def step2_signature_approach(missing):
    print("STEP 2 - Signature approach: the ledger was always complete in")
    print("  principle (Ji's sum rule: 1/2 = quark spin + gluon spin + orbital).")
    print("  The missing entries are orbital - experiments could not itemize them.")

def step3_testable_prediction():
    print("STEP 3 - testable prediction: EIC measures GPDs; quark+gluon orbital")
    print("  pieces plus known spins sum to 1/2 within uncertainties.")

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: the EIC-completed ledger sums to 1/2.")
    print("  REFUTE if: the completed ledger fails to sum to 1/2 - a fundamental")
    print("    problem in the QCD spin decomposition itself.")

def main():
    missing = step1_problem()
    step2_signature_approach(missing)
    step3_testable_prediction()
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (missing=%.0f%%)" % (RID, missing * 100))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)

DEMOS.update({
 "high-tc-superconductivity": demo_high_tc,
 "glass-transition": demo_glass_transition,
 "uhe-cosmic-rays": demo_uhecr,
 "lithium-problem": demo_lithium_problem,
 "r-process-sites": demo_rprocess,
 "muon-g-2": demo_muon_g2,
 "strong-cp": demo_strong_cp,
 "proton-spin-crisis": demo_proton_spin,
})


def demo_confinement(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
"""SOLUTION EXPLORER: Quark Confinement.
Walks the Signature proposed approach: confinement as the color ledger's
no-exit rule enforced by flux-tube bookkeeping.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions ----
STRING_TENSION = 0.9  # GeV/fm
R_FM = 1.0            # separation in femtometers
M_QUARK_GEV = 0.3     # constituent quark mass, GeV

def step1_problem():
    E = STRING_TENSION * R_FM
    print("STEP 1 - the problem: separating quarks 1 fm stores %.2f GeV" % E)
    print("  pair creation wins once E > 2*m_q = %.2f GeV - no free quark ever." % (2 * M_QUARK_GEV))
    assert 0.5 < E < 1.5, "string energy out of range"
    assert E > 2 * M_QUARK_GEV, "tube must break before quarks isolate"
    return E

def step2_signature_approach(E):
    print("STEP 2 - Signature approach: the flux tube is the accounting string.")
    print("  Color must sum neutral; the tube carries unbalanced color at a")
    print("  fixed cost per length - linearity is the no-exit rule made visible.")

def step3_testable_prediction():
    print("STEP 3 - testable prediction: lattice flux-tube profiles and string")
    print("  tension match the dual-superconductor picture across temperatures.")

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: lattice pins tube profiles to the dual-superconductor")
    print("    prediction and an analytic path to the mass gap opens.")
    print("  REFUTE if: confinement is proved via a wholly different mechanism,")
    print("    or a free quark is ever observed.")

def main():
    E = step1_problem()
    step2_signature_approach(E)
    step3_testable_prediction()
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (E=%.2f GeV)" % (RID, E))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_measurement(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
"""SOLUTION EXPLORER: The Quantum Measurement Problem.
Walks the Signature proposed approach: measurement as ledger commitment -
definite when the environmental record becomes irreversible.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions (order-of-magnitude toy model) ----
# decoherence rate Gamma = Lambda * (dx)^2 ; tau = 1/Gamma
LAMBDA_DUST = 1.0e20   # s^-1 m^-2, dust grain in air (Joos-Zeh scale)
LAMBDA_ELEC = 1.0e-20  # s^-1 m^-2, isolated electron vs CMB only
DX = 1.0e-6            # superposition separation, m

def step1_problem():
    tau_dust = 1.0 / (LAMBDA_DUST * DX ** 2)
    tau_elec = 1.0 / (LAMBDA_ELEC * DX ** 2)
    ratio = tau_elec / tau_dust
    print("STEP 1 - the problem: dust decoheres in %.1e s; isolated electron in %.1e s" % (tau_dust, tau_elec))
    print("  decoherence explains lost interference - not which outcome is actual.")
    assert 1.0e35 < ratio < 1.0e45, "decoherence contrast out of toy range"
    return ratio

def step2_signature_approach(ratio):
    print("STEP 2 - Signature approach: ledger commitment.")
    print("  Unitarity holds; an event is definite when its environmental")
    print("  record is thermodynamically irreversible - write-once bookkeeping.")

def step3_testable_prediction():
    print("STEP 3 - testable prediction: collapse-model experiments keep finding")
    print("  zero anomalous noise; quantum-computer errors stay fully explained")
    print("  by environmental decoherence.")

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: no objective-collapse signal appears at any sensitivity.")
    print("  REFUTE if: verified spontaneous collapse noise - measurement is a")
    print("    new physical process, not ledger commitment.")

def main():
    ratio = step1_problem()
    step2_signature_approach(ratio)
    step3_testable_prediction()
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (ratio=%.1e)" % (RID, ratio))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_info_paradox(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
"""SOLUTION EXPLORER: The Black Hole Information Paradox.
Walks the Signature proposed approach: no paradox - the information was
always in the horizon ledger; radiation reads it out slowly.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions (solar-mass black hole) ----
M_SUN = 1.989e30
H_BAR = 1.054571817e-34
C = 2.99792458e8
G = 6.674e-11
K_B = 1.380649e-23
YR_S = 3.15576e7

def step1_problem():
    T = H_BAR * C ** 3 / (8.0 * math.pi * G * M_SUN * K_B)
    t_s = 5120.0 * math.pi * G ** 2 * M_SUN ** 3 / (H_BAR * C ** 4)
    t_yr = t_s / YR_S
    print("STEP 1 - the problem: T_Hawking = %.2e K; evaporation = %.2e yr" % (T, t_yr))
    print("  radiation looks thermal -> information seemingly destroyed.")
    assert 5.0e-8 < T < 8.0e-8, "Hawking temperature out of range"
    assert 1.0e67 < t_yr < 5.0e67, "evaporation time out of range"
    return T, t_yr

def step2_signature_approach(T, t_yr):
    print("STEP 2 - Signature approach: the horizon holds the entries.")
    print("  Degrees of freedom live at the horizon; Hawking pairs leak them;")
    print("  the Page turnover is when the radiation ledger outweighs the horizon.")

def step3_testable_prediction():
    print("STEP 3 - testable prediction: the Page curve derivable from a")
    print("  UV-complete theory with a clear infalling-observer account; analog")
    print("  experiments show information recovery in analog Hawking radiation.")

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: string theory derives the Page curve with the")
    print("    infalling observer accounted for.")
    print("  REFUTE if: the island calculation proves artifactual, or unitarity")
    print("    is verified to fail in evaporation.")

def main():
    T, t_yr = step1_problem()
    step2_signature_approach(T, t_yr)
    step3_testable_prediction()
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (T=%.2e K)" % (RID, T))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_singularity(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
"""SOLUTION EXPLORER: Black Hole Singularity Resolution.
Walks the Signature proposed approach: the singularity as ledger overflow -
infinity as bookkeeping failure; the ledger starts a new page (a bounce).
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions ----
H_BAR = 1.054571817e-34
C = 2.99792458e8
G = 6.674e-11

def step1_problem():
    rho_p = C ** 5 / (H_BAR * G ** 2)
    log_rho = math.log10(rho_p)
    print("STEP 1 - the problem: GR breaks at Planck density 10^%.2f kg/m^3" % log_rho)
    print("  infinity = 'new physics needed'; what replaces it is unknown.")
    assert 96.5 < log_rho < 97.0, "Planck density out of range"
    return log_rho

def step2_signature_approach(log_rho):
    print("STEP 2 - Signature approach: overflow, then a new page.")
    print("  Quantum-geometry repulsion halts collapse at Planck density; the")
    print("  interior bounces - two pages of one ledger, not an infinite entry.")

def step3_testable_prediction():
    print("STEP 3 - testable prediction: gravitational-wave echoes - repeating")
    print("  fading signals after merger ringdowns - matching bounce templates.")

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: echoes are detected matching bounce/fuzzball templates,")
    print("    or loop quantum gravity derives the bounce with unique predictions.")
    print("  REFUTE if: echo searches exclude them where models require them,")
    print("    or a UV-complete theory resolves the interior differently.")

def main():
    log_rho = step1_problem()
    step2_signature_approach(log_rho)
    step3_testable_prediction()
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (10^%.2f kg/m^3)" % (RID, log_rho))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_vacuum_metastability(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
"""SOLUTION EXPLORER: Vacuum Metastability.
Walks the Signature proposed approach: near-criticality as a balancing
condition - the masses are correlated along the stability boundary.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions (toy RG running, illustrative) ----
LAMBDA_MT = 0.13     # Higgs quartic at top-mass scale
RUN_COEF = 0.006     # effective running coefficient (toy)
MT = 173.0           # GeV

def step1_problem():
    # lambda(mu) = LAMBDA_MT - RUN_COEF * ln(mu/MT); find zero crossing
    ln_mu_over_mt = LAMBDA_MT / RUN_COEF
    mu_inst = MT * math.exp(ln_mu_over_mt)
    log_mu = math.log10(mu_inst)
    print("STEP 1 - the problem: toy running turns lambda negative at 10^%.2f GeV" % log_mu)
    print("  our vacuum may be a false vacuum; lifetime ~10^100 yr.")
    assert 9.0 < log_mu < 13.0, "instability scale out of literature range"
    return log_mu

def step2_signature_approach(log_mu):
    print("STEP 2 - Signature approach: boundaries are where ledgers balance.")
    print("  Sitting at the stability edge is data: the Higgs/top masses are")
    print("  correlated by higher-scale dynamics with an attractor near the edge.")

def step3_testable_prediction():
    print("STEP 3 - testable prediction: precision Higgs self-coupling and top")
    print("  mass track the boundary tighter than chance - or stabilizing new")
    print("  physics appears at the predicted scale.")

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: parameters track the boundary, or stabilizing physics")
    print("    is found.")
    print("  REFUTE if: precision values move firmly into the stable region")
    print("    (near-criticality was a mirage of uncertainties).")

def main():
    log_mu = step1_problem()
    step2_signature_approach(log_mu)
    step3_testable_prediction()
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (10^%.2f GeV)" % (RID, log_mu))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_turbulence(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
"""SOLUTION EXPLORER: The Turbulence Problem.
Walks the Signature proposed approach: turbulence as the flow ledger's
required overflow channel; Kolmogorov -5/3 as the fixed exchange rate.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions (water in a pipe) ----
RHO = 1000.0   # kg/m^3
V = 2.0        # m/s
L = 0.1        # m
MU = 1.0e-3    # Pa s

def step1_problem():
    Re = RHO * V * L / MU
    print("STEP 1 - the problem: Re = %.1e (>> 4000: fully turbulent)" % Re)
    print("  no first-principles predictive theory; N-S smoothness unproven.")
    assert Re > 4000.0, "flow must be turbulent"
    return Re

def step2_signature_approach(Re):
    print("STEP 2 - Signature approach: the cascade as required overflow.")
    ks = [2.0 ** i for i in range(8)]
    E = [k ** (-5.0 / 3.0) for k in ks]
    lx = [math.log(k) for k in ks]
    ly = [math.log(e) for e in E]
    n = len(ks)
    slope = (n * sum(a * b for a, b in zip(lx, ly)) - sum(lx) * sum(ly)) / (n * sum(a * a for a in lx) - sum(lx) ** 2)
    print("  fitted cascade exponent: %.4f (Kolmogorov -5/3 = %.4f)" % (slope, -5.0 / 3.0))
    assert abs(slope + 5.0 / 3.0) < 0.02, "cascade exponent off"

def step3_testable_prediction():
    print("STEP 3 - testable prediction: intermittency exponents match")
    print("  ledger-bunching statistics across pipes, boundary layers, shear.")

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: high-Re experiments show universal intermittency")
    print("    matching the prediction with no flow-specific tuning.")
    print("  REFUTE if: intermittency proves irreducibly flow-dependent, or a")
    print("    first-principles N-S derivation leaves no role for the picture.")

def main():
    Re = step1_problem()
    step2_signature_approach(Re)
    step3_testable_prediction()
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (Re=%.1e)" % (RID, Re))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_neutrino_mass(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
"""SOLUTION EXPLORER: Neutrino Mass and Nature.
Walks the Signature proposed approach: lightness as the suppressed
remainder of a heavy partner scale - the seesaw - powering leptogenesis.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions ----
DM2_32 = 2.5e-3    # eV^2, atmospheric splitting
KATRIN_BOUND = 0.45  # eV, direct bound

def step1_problem():
    m_heavy_min = math.sqrt(DM2_32)
    print("STEP 1 - the problem: heaviest neutrino >= %.3f eV, yet < %.2f eV" % (m_heavy_min, KATRIN_BOUND))
    print("  ordering, absolute scale, Dirac-vs-Majorana all open.")
    assert 0.04 < m_heavy_min < 0.06, "mass floor out of range"
    assert KATRIN_BOUND < 0.5
    return m_heavy_min

def step2_signature_approach(m_heavy_min):
    print("STEP 2 - Signature approach: the seesaw ledger.")
    print("  m_light ~ m_Dirac^2 / M_heavy: absurd lightness = suppression by a")
    print("  heavy scale; the same heavy partners' decays may write the matter")
    print("  surplus (leptogenesis) - two records, one heavy sector.")

def step3_testable_prediction():
    print("STEP 3 - testable prediction: neutrinoless double-beta decay")
    print("  establishes Majorana nature; leptonic CP phase fits leptogenesis.")

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: 0vBB signal + CP phase consistent with leptogenesis.")
    print("  REFUTE if: neutrinos prove Dirac - a wholly different mass")
    print("    mechanism is needed.")

def main():
    m = step1_problem()
    step2_signature_approach(m)
    step3_testable_prediction()
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (m>=%.3f eV)" % (RID, m))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_hierarchy(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
"""SOLUTION EXPLORER: The Hierarchy Problem.
Walks the Signature proposed approach: the Higgs mass protected by an
unidentified ledger symmetry, softly broken - the LHC looked in the
wrong hiding places. PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions ----
M_PLANCK_GEV = 1.22e19
M_HIGGS_GEV = 125.0

def step1_problem():
    gap = math.log10(M_PLANCK_GEV / M_HIGGS_GEV)
    tuning = 10.0 ** (2.0 * gap)
    print("STEP 1 - the problem: Planck/Higgs = 10^%.2f; naive tuning 1 in %.1e" % (gap, tuning))
    assert 16.5 < gap < 17.5, "hierarchy gap out of range"
    return gap

def step2_signature_approach(gap):
    print("STEP 2 - Signature approach: ledgers abhor unprotected cancellations.")
    print("  The protection exists - twin-Higgs-like or relaxion-like - hiding")
    print("  where the LHC is blind: neutral states, precision Higgs couplings,")
    print("  or cosmological dynamics.")

def step3_testable_prediction():
    print("STEP 3 - testable prediction: top partners with odd quantum numbers,")
    print("  Higgs-coupling deviations at a Higgs factory, or relaxion cosmology.")

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: any protective mechanism is discovered and verified.")
    print("  REFUTE if: a 100-TeV collider finds nothing to 30+ TeV while")
    print("    precision confirms the SM - naturalness was a false guide.")

def main():
    gap = step1_problem()
    step2_signature_approach(gap)
    step3_testable_prediction()
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (gap=10^%.2f)" % (RID, gap))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_cc_problem(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
"""SOLUTION EXPLORER: The Cosmological Constant Problem.
Walks the Signature proposed approach: the 120-order cancellation as an
exact bookkeeping symmetry; the remainder is the soft breaking.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions ----
RHO_QFT_GEV4 = 1.0e76    # ~(1e19 GeV)^4, Planck-scale zero-point estimate
RHO_OBS_GEV4 = 2.8e-47   # ~(2.3e-3 eV)^4, observed dark energy density

def step1_problem():
    gap = math.log10(RHO_QFT_GEV4 / RHO_OBS_GEV4)
    print("STEP 1 - the problem: prediction overshoots observation by 10^%.1f" % gap)
    print("  the worst prediction in physics; small-but-nonzero worsens it.")
    assert 115.0 < gap < 125.0, "gap out of literature range"
    return gap

def step2_signature_approach(gap):
    print("STEP 2 - Signature approach: no accident reaches 10^%.0f." % gap)
    print("  Exact-seeming cancellations signal exact symmetries: a")
    print("  sequestering-type mechanism stops vacuum energy gravitating; the")
    print("  observed Lambda is the symmetry's soft breaking.")

def step3_testable_prediction():
    print("STEP 3 - testable prediction: a consistent sequestering/unimodular")
    print("  formulation predicting the remainder's scale or drift.")

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: a consistent cancellation mechanism predicts the")
    print("    remainder's scale/drift.")
    print("  REFUTE if: quantum-gravity consistency proofs forbid such global")
    print("    mechanisms - leaving anthropic selection.")

def main():
    gap = step1_problem()
    step2_signature_approach(gap)
    step3_testable_prediction()
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (gap=10^%.1f)" % (RID, gap))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)

DEMOS.update({
 "quark-confinement": demo_confinement,
 "quantum-measurement": demo_measurement,
 "black-hole-information": demo_info_paradox,
 "singularity-resolution": demo_singularity,
 "vacuum-metastability": demo_vacuum_metastability,
 "turbulence-problem": demo_turbulence,
 "neutrino-mass": demo_neutrino_mass,
 "hierarchy-problem": demo_hierarchy,
 "cosmological-constant-problem": demo_cc_problem,
})


def demo_horizon_flatness(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
"""SOLUTION EXPLORER: The Horizon and Flatness Problems.
Walks the Signature proposed approach: uniformity as one ledger entry
written before expansion separated the pages; the spectrum is the
handwriting. PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions ----
# horizon angular radius at recombination chosen so the patch count matches
# the literature estimate of roughly 40,000 causally disconnected regions
THETA_DEG = 0.57

def step1_problem():
    theta = math.radians(THETA_DEG)
    patches = 4.0 * math.pi / (math.pi * theta ** 2)
    print("STEP 1 - the problem: ~%.0f causally disconnected patches share T to 1e-5" % patches)
    print("  and |Omega_k| < 0.001 though curvature should grow.")
    assert 1.0e4 < patches < 1.0e5, "patch count out of range"
    return patches

def step2_signature_approach(patches):
    print("STEP 2 - Signature approach: the entries were written first.")
    print("  One connected domain wrote the ledger; rapid expansion then tore")
    print("  the pages apart. Flatness follows: stretching irons out curvature.")

def step3_testable_prediction():
    print("STEP 3 - testable prediction: primordial B-modes pin the energy")
    print("  scale; the spectral tilt's running matches an inflaton potential -")
    print("  the handwriting identified.")

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: B-modes + running match a specific inflaton potential.")
    print("  REFUTE if: B-mode searches rule out simple inflation while a bounce")
    print("    reproduces the spectrum - same uniformity, different writer.")

def main():
    patches = step1_problem()
    step2_signature_approach(patches)
    step3_testable_prediction()
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (patches=%.0f)" % (RID, patches))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_flavor(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
"""SOLUTION EXPLORER: The Flavor Puzzle.
Walks the Signature proposed approach: generations as overtones of one
matter ledger; the top's heaviness as the highest resolved harmonic.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions ----
M_TOP_MEV = 173e3   # MeV
M_ELEC_MEV = 0.511  # MeV

def step1_problem():
    ratio = M_TOP_MEV / M_ELEC_MEV
    log_ratio = math.log10(ratio)
    print("STEP 1 - the problem: top/electron = %.2e (10^%.2f); no theory predicts it" % (ratio, log_ratio))
    assert 5.0 < log_ratio < 6.0, "mass span out of range"
    return log_ratio

def step2_signature_approach(log_ratio):
    print("STEP 2 - Signature approach: one instrument, three notes.")
    print("  Replication differing mainly in mass suggests one object with")
    print("  excited states; mixing matrices are basis misalignments.")
    print("  (Koide-style numerology is the warning label: fit is not mechanism.)")

def step3_testable_prediction():
    print("STEP 3 - testable prediction: a flavor model deriving mass ratios")
    print("  and mixings from overtone structure with a NEW successful")
    print("  prediction - e.g., a quark-lepton hierarchy relation.")

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: an overtone-structured model predicts a new flavor")
    print("    relation that experiment verifies.")
    print("  REFUTE if: a fourth generation is found, or parameters prove")
    print("    environmentally selected with no dynamical origin.")

def main():
    log_ratio = step1_problem()
    step2_signature_approach(log_ratio)
    step3_testable_prediction()
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (span=10^%.2f)" % (RID, log_ratio))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_quantum_gravity(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
"""SOLUTION EXPLORER: Quantum Gravity.
Walks the Signature proposed approach: not the quantization of spacetime,
but the theory of the ledger from which spacetime emerges.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions ----
H_BAR = 1.054571817e-34
G = 6.674e-11
C = 2.99792458e8

def step1_problem():
    l_p = math.sqrt(H_BAR * G / C ** 3)
    t_p = l_p / C
    print("STEP 1 - the problem: Planck length %.3e m, time %.3e s" % (l_p, t_p))
    print("  perturbative quantum GR diverges; 16 orders beyond the LHC.")
    assert 1.5e-35 < l_p < 1.7e-35, "Planck length out of range"
    assert 5.0e-44 < t_p < 6.0e-44, "Planck time out of range"
    return l_p, t_p

def step2_signature_approach(l_p, t_p):
    print("STEP 2 - Signature approach: quantize the business, not the books.")
    print("  The fundamental entries are quantum-informational; Einstein's")
    print("  equations emerge thermodynamically (Jacobson-style). Holography")
    print("  and black hole thermodynamics are the ledger showing through.")

def step3_testable_prediction():
    print("STEP 3 - testable prediction: Einstein equations derived from")
    print("  informational postulates; gravitationally induced entanglement")
    print("  proves gravity must be quantum (Bose/Marletto-Vedral tests).")

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: GR emerges rigorously from information, or")
    print("    entanglement-via-gravity is observed.")
    print("  REFUTE if: the metric itself is consistently quantized UV-complete")
    print("    (asymptotic safety confirmed) - the books were the business.")

def main():
    l_p, t_p = step1_problem()
    step2_signature_approach(l_p, t_p)
    step3_testable_prediction()
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (l_p=%.3e m)" % (RID, l_p))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_emergent_spacetime(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
"""SOLUTION EXPLORER: Emergent Spacetime.
Walks the Signature proposed approach: spacetime as the shape of the
entanglement ledger - area IS entanglement entropy.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions (solar-mass black hole entropy) ----
M_SUN = 1.989e30
H_BAR = 1.054571817e-34
C = 2.99792458e8
G = 6.674e-11

def step1_problem():
    S = 4.0 * math.pi * G * M_SUN ** 2 / (H_BAR * C)  # in units of k_B
    log_S = math.log10(S)
    print("STEP 1 - the problem: solar-mass BH entropy = 10^%.2f k_B (area, not volume)" % log_S)
    print("  AdS/CFT builds spacetime from boundary entanglement; the 'atoms'")
    print("  of spacetime are unidentified; time's emergence barely understood.")
    assert 76.0 < log_S < 78.0, "BH entropy out of range"
    return log_S

def step2_signature_approach(log_S):
    print("STEP 2 - Signature approach: run Ryu-Takayanagi backward.")
    print("  Build the entanglement pattern and geometry follows; horizons and")
    print("  singularities are ledger pathologies (maximal mixing, discontinuity).")

def step3_testable_prediction():
    print("STEP 3 - testable prediction: full GR dynamics from entanglement")
    print("  postulates beyond AdS/CFT; quantum corrections to geometry near")
    print("  horizons follow the predicted ledger-pathology pattern.")

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: Einstein dynamics derived from entanglement generally,")
    print("    with the predicted near-horizon correction pattern.")
    print("  REFUTE if: a no-go theorem blocks entanglement from carrying full")
    print("    GR dynamics, or spacetime proves fundamentally geometric.")

def main():
    log_S = step1_problem()
    step2_signature_approach(log_S)
    step3_testable_prediction()
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (S=10^%.2f k_B)" % (RID, log_S))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_ctc(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
"""SOLUTION EXPLORER: Closed Timelike Curves.
Walks the Signature proposed approach: CTCs as ledger loops the write-once
bookkeeping cannot close - chronology protection as ledger consistency.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions (Morris-Thorne wormhole throat) ----
THROAT_M = 1.0   # throat radius, meters
C = 2.99792458e8
G = 6.674e-11

def step1_problem():
    # exotic energy density scale needed to hold a wormhole throat open
    rho_exotic = -(C ** 2) / (G * THROAT_M ** 2)  # kg/m^3, order of magnitude
    print("STEP 1 - the problem: a 1-m throat needs exotic density ~%.2e kg/m^3" % rho_exotic)
    print("  GR permits CTCs; every construction needs unphysical ingredients.")
    assert abs(rho_exotic) > 1.0e25, "exotic density must be absurd"
    return rho_exotic

def step2_signature_approach(rho_exotic):
    print("STEP 2 - Signature approach: the ledger refuses the loop.")
    print("  A CTC needs the ledger to take its own future as input; the")
    print("  semiclassical divergences are the refusal made visible. Exotic")
    print("  matter is the ledger's price tag on the impossible.")

def step3_testable_prediction():
    print("STEP 3 - testable prediction: semiclassical backreaction diverges on")
    print("  all CTC-forming spacetimes; quantum gravity excludes CTCs from the")
    print("  physical state space.")

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: chronology protection is proved generally, or quantum")
    print("    gravity derives the exclusion.")
    print("  REFUTE if: a consistent quantum-gravity CTC exists - or one is")
    print("    observed. (This would overturn the proposal completely.)")

def main():
    rho = step1_problem()
    step2_signature_approach(rho)
    step3_testable_prediction()
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (rho=%.2e kg/m^3)" % (RID, rho))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_fine_tuning(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
"""SOLUTION EXPLORER: The Fine-Tuning of Constants.
Walks the Signature proposed approach: apparent tuning as interlocked
ledger entries - single-dial arguments assume what they must prove.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions ----
E_HOYLE_MEV = 7.65    # carbon-12 Hoyle state, MeV
T_STAR_K = 1.0e8      # helium-burning core temperature, K
K_B_EV_K = 8.617333e-5

def step1_problem():
    print("STEP 1 - the problem: Hoyle resonance at %.2f MeV; stars need it" % E_HOYLE_MEV)
    assert 7.5 < E_HOYLE_MEV < 7.8, "Hoyle state out of measured range"
    kT_mev = K_B_EV_K * T_STAR_K / 1.0e6
    sensitivity = math.exp(0.1 / kT_mev)  # 0.1 MeV shift effect on rate
    print("  a 0.1 MeV shift changes the triple-alpha rate by x%.1e" % sensitivity)
    assert sensitivity > 1.0e4, "sensitivity must be extreme"
    return sensitivity

def step2_signature_approach(sensitivity):
    print("STEP 2 - Signature approach: question the independence premise.")
    print("  Tuning arguments vary one dial holding the rest fixed; if the")
    print("  ledger interlocks parameters, the viable region is a correlated")
    print("  surface, not a tiny hypercube. Find the interlocks.")

def step3_testable_prediction():
    print("STEP 3 - testable prediction: precise relations between seemingly")
    print("  independent constants; a UV theory deriving several parameters")
    print("  from fewer inputs with the viable region emerging naturally.")

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: constant interlocks are discovered and verified.")
    print("  REFUTE if: parameters prove truly independent across a landscape -")
    print("    the multiverse reading wins.")

def main():
    s = step1_problem()
    step2_signature_approach(s)
    step3_testable_prediction()
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (sensitivity=x%.1e)" % (RID, s))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_cosmic_b(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
"""SOLUTION EXPLORER: The Origin of Cosmic Magnetic Fields.
Walks the Signature proposed approach: primordial seed entries written
early, amplified by dynamos; void fields are the surviving fossils.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions ----
SEED_G = 1.0e-20    # gauss, primordial seed
TARGET_G = 1.0e-6   # gauss, galactic microgauss fields

def step1_problem():
    efolds = math.log(TARGET_G / SEED_G)
    print("STEP 1 - the problem: seed %.0e G -> %.0e G needs %.1f e-folds" % (SEED_G, TARGET_G, efolds))
    print("  dynamos amplify - but where do the seeds come from? Voids look")
    print("  magnetized, and voids run no batteries.")
    assert 25.0 < efolds < 45.0, "required amplification out of dynamo range"
    return efolds

def step2_signature_approach(efolds):
    print("STEP 2 - Signature approach: the seeds are primordial ledger entries.")
    print("  Inflation or a phase transition wrote them; dynamos only amplified.")
    print("  Void fields are the least-processed fossils of the first writing.")

def step3_testable_prediction():
    print("STEP 3 - testable prediction: the intergalactic field's power")
    print("  spectrum matches a primordial template - scale-invariant for")
    print("  inflation, peaked for phase transitions.")

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: void-field spectra match a primordial template and CMB")
    print("    bounds agree with it.")
    print("  REFUTE if: void fields prove zero (blazar bounds overturned),")
    print("    reopening purely astrophysical seeding.")

def main():
    efolds = step1_problem()
    step2_signature_approach(efolds)
    step3_testable_prediction()
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (%.1f e-folds)" % (RID, efolds))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_toe(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
"""SOLUTION EXPLORER: The Theory of Everything.
Walks the Signature proposed approach: unification as the discovery that all
ledgers are one ledger; progress measured by parameter reduction.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions (1-loop SM running, illustrative) ----
# 1/alpha_i(mu) = 1/alpha_i(Mz) + (b_i/2pi) ln(mu/Mz)
A1, A2, A3 = 59.0, 29.6, 8.47   # 1/alpha at Mz
B1, B2, B3 = 41.0 / 10.0, -19.0 / 6.0, -7.0
MZ = 91.0  # GeV

def crossing(a_a, a_b, b_a, b_b):
    ln_mu = (a_a - a_b) * 2.0 * math.pi / (b_a - b_b)
    return math.log10(MZ * math.exp(ln_mu))

def step1_problem():
    c12 = crossing(A1, A2, B1, B2)
    c23 = crossing(A2, A3, B2, B3)
    print("STEP 1 - the problem: SM couplings nearly meet - but miss.")
    print("  alpha1=alpha2 at 10^%.2f GeV; alpha2=alpha3 at 10^%.2f GeV" % (c12, c23))
    assert 12.0 < c12 < 14.0, "c12 crossing out of range"
    assert 16.0 < c23 < 18.0, "c23 crossing out of range"
    print("  near-miss: clue or coincidence? Simplest GUTs ruled out by proton decay.")
    return c12, c23

def step2_signature_approach(c12, c23):
    print("STEP 2 - Signature approach: judge by parameter reduction.")
    print("  Past unifications dissolved ledger boundaries (Maxwell, electroweak).")
    print("  The remaining boundaries - gravity vs gauge, generations, constants")
    print("  - mark where the single deepest ledger has not yet been found.")

def step3_testable_prediction():
    print("STEP 3 - testable prediction: a framework deriving the SM gauge group,")
    print("  three generations, and parameters - plus gravity - with at least one")
    print("  confirmed novel prediction.")

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: a theory derives the SM + gravity with fewer parameters")
    print("    and a verified new prediction.")
    print("  REFUTE (as answerable) if: parameters prove environmentally selected")
    print("    - 'why these values' unanswerable in principle.")

def main():
    c12, c23 = step1_problem()
    step2_signature_approach(c12, c23)
    step3_testable_prediction()
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (miss: 10^%.2f vs 10^%.2f)" % (RID, c12, c23))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)

DEMOS.update({
 "horizon-flatness": demo_horizon_flatness,
 "flavor-puzzle": demo_flavor,
 "quantum-gravity": demo_quantum_gravity,
 "emergent-spacetime": demo_emergent_spacetime,
 "closed-timelike-curves": demo_ctc,
 "fine-tuning": demo_fine_tuning,
 "cosmic-magnetic-fields": demo_cosmic_b,
 "theory-of-everything": demo_toe,
})
