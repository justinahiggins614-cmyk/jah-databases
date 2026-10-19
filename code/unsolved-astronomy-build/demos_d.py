#!/usr/bin/env python3
"""Solution-explorer walkthrough demos, ranks 27-34."""


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + "import math\n" + body.replace(
        "NAME", __import__("json").dumps(name))


def demo_usa_dark_energy(hdr, name, rid, group, P):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: Write the cosmic budget: dark energy owns 69 percent of everything.")
    omega_l = 0.69
    print("Step 2: Confront the vacuum-energy prediction: off by 10^%.0f." % 120.0)
    assert abs(math.log10(1.0e120) - 120.0) < 1e-9
    print("Step 3: Branch the possibilities: constant, evolving field, modified gravity.")
    print("Step 4: Score each against supernova + BAO + CMB, tracking fine-tuning cost.")
    print("Step 5: DESI's evolution hint is the live wire - convergence across probes decides.")
    print("CONFIRM (evolving) if: DESI full survey plus independent supernova data converge on")
    print("  w different from -1 at high significance.")
    print("CONFIRM (constant) if: all probes converge on w = -1 with no evolution - the")
    print("  fine-tuning problem remains, but the model stands.")
    print("REFUTE (vacuum energy) if: the naive quantum value is fixed with no cancellation")
    print("  mechanism - the discrepancy becomes a disproof, not a puzzle.")
    print("REFUTE (modified gravity) if: growth-of-structure measurements match general")
    print("  relativity exactly where modified models predict deviations.")
    print("OK: %s scored the dark energy branches" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usa_reionization(hdr, name, rid, group, P):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: Convert the baryon density to a number density.")
    h0_si = 70.0e3 / 3.085677581e22
    rho_c = 3.0 * h0_si ** 2 / (8.0 * math.pi * 6.67430e-11)
    n_b = 0.049 * rho_c / 1.6726219e-27
    print("  comoving baryon number density: %.2e m^-3" % n_b)
    assert 2.5e-1 < n_b < 2.9e-1
    print("Step 2: Each baryon needs ~3 ionizing photons after recombinations.")
    need = 3.0 * n_b
    print("  required ionizing photon density: %.2e m^-3" % need)
    assert 8.0e-1 < need < 8.8e-1
    print("Step 3: Integrate galaxy luminosity functions times escape fraction, add quasars.")
    print("Step 4: Find the redshift range where the budget fails to close.")
    print("Step 5: Direct Lyman-continuum leakage measurements are the decisive input.")
    print("CONFIRM (galaxies) if: measured escape fractions close the budget at redshift 7-8.")
    print("CONFIRM (quasars help) if: faint-quasar counts supply the missing fraction exactly")
    print("  where galaxies fall short.")
    print("REFUTE (galaxy-only) if: 21-cm neutral-fraction timelines contradict the galaxy")
    print("  emissivity - the sources are wrong.")
    print("REFUTE (budget closed) if: recombinations were underestimated - the requirement rises")
    print("  and the ledger reopens.")
    print("OK: %s counted the reionization photons" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usa_dark_ages(hdr, name, rid, group, P):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: Map redshift to observing frequency for the 21-cm line.")
    z = 20.0
    nu = 1420.4 / (1.0 + z)
    print("  z=%.0f -> nu = 1420.4/21 = %.2f MHz" % (z, nu))
    assert 67.5 < nu < 67.8
    print("Step 2: The standard model predicts an absorption depth near 200 mK.")
    print("Step 3: EDGES reported ~500 mK - a factor 2.5 deeper.")
    ratio = 500.0 / 200.0
    print("  excess factor: %.2f" % ratio)
    assert 2.49 < ratio < 2.51
    print("Step 4: That depth needs extra cooling - exotic physics or systematics.")
    print("Step 5: Two independent instruments with different systematics must agree.")
    print("CONFIRM (new physics) if: two independent instruments measure the same anomalous")
    print("  depth and timing - e.g. dark matter cooling the gas.")
    print("CONFIRM (standard) if: HERA's power spectrum matches standard predictions at the")
    print("  corresponding redshifts.")
    print("REFUTE (EDGES) if: the signal is traced to foreground modeling or an instrumental")
    print("  artifact - SARAS already voted no.")
    print("REFUTE (easy detection) if: lunar far-side measurements show the global signal is")
    print("  buried deeper than planned sensitivities - the epoch stays dark longer.")
    print("OK: %s mapped the dark-ages signal" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usa_giant_structures(hdr, name, rid, group, P):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: Compare the Huge Large Quasar Group to the homogeneity scale.")
    size_mpc = 1240.0
    hom_mpc = 370.0
    ratio = size_mpc / hom_mpc
    print("  1240 Mpc / 370 Mpc = %.2f homogeneity scales" % ratio)
    assert 3.3 < ratio < 3.4
    print("Step 2: A structure 3.4x the homogeneity scale is either a real challenge or a")
    print("  rare fluctuation - statistics alone cannot tell without blind searches.")
    print("Step 3: Run the same detection algorithm blind on mocks and on data.")
    print("Step 4: Count structures in each; only a significant excess challenges the principle.")
    print("Step 5: Pre-register the search - no tuning the algorithm to the data.")
    print("CONFIRM (violation) if: blind searches find multiple super-homogeneity structures at")
    print("  a rate the mocks cannot reproduce.")
    print("CONFIRM (compatible) if: mocks produce such structures just as often - rare but allowed.")
    print("REFUTE (a claim) if: blind reanalysis dissolves the structure or shows the detection")
    print("  algorithm was tuned to find it.")
    print("REFUTE (principle intact, trivially) if: the community keeps moving the homogeneity")
    print("  scale post-hoc - the test must be fixed in advance.")
    print("OK: %s ran the homogeneity blind test" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usa_bh_information(hdr, name, rid, group, P):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: Count the information capacity of a 10-solar-mass black hole.")
    G, hbar, c = 6.67430e-11, 1.054571817e-34, 2.99792458e8
    M = 10.0 * 1.98847e30
    s_over_k = 4.0 * math.pi * G * M ** 2 / (hbar * c)
    print("  Bekenstein-Hawking entropy: %.2e k_B" % s_over_k)
    assert 1.0e79 < s_over_k < 1.1e79
    print("Step 2: The paradox as counting: radiation entropy must start decreasing at the Page")
    print("  time, but Hawking's calculation says it never does.")
    print("Step 3: Compute the evaporation timescale for context.")
    t_evap = 5120.0 * math.pi * G ** 2 * M ** 3 / (hbar * c ** 4)
    print("  evaporation time: %.2e years" % (t_evap / 3.15576e7))
    assert 2.0e70 < t_evap / 3.15576e7 < 2.2e70
    print("Step 4: Audit each resolution against three requirements: Page curve, smooth horizon,")
    print("  microscopic derivation.")
    print("Step 5: Only a model meeting all three - with a distinct prediction - counts.")
    print("CONFIRM (a resolution) if: a microscopic model meets all three requirements and its")
    print("  distinct prediction, such as gravitational-wave echoes, is observed.")
    print("CONFIRM (islands) if: the island derivation is extended to realistic collapse black")
    print("  holes with the Page curve intact.")
    print("REFUTE (island program) if: a proof shows the derivation cannot extend beyond its")
    print("  simplified models.")
    print("REFUTE (complementarity) if: an infalling observer experiment - even in principle -")
    print("  exposes a contradiction the framework cannot absorb.")
    print("OK: %s counted the black hole information" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usa_singularities(hdr, name, rid, group, P):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: Locate where known physics ends: the Schwarzschild radius of Sgr A*.")
    G, c = 6.67430e-11, 2.99792458e8
    M = 4.3e6 * 1.98847e30
    rs = 2.0 * G * M / c ** 2
    print("  r_s = %.3e m (%.2f AU)" % (rs, rs / 1.495978707e11))
    assert 1.26e10 < rs < 1.28e10
    print("Step 2: Compare with the Planck length, where quantum gravity must take over.")
    lp = 1.616255e-35
    print("  r_s / l_Planck = %.2e - known physics spans 45 orders of magnitude inward." % (rs / lp))
    assert 7.8e44 < rs / lp < 8.0e44
    print("Step 3: Each proposal - bounce, fuzzball, regular core - modifies the picture at a")
    print("  specific radius; extract its observable consequence.")
    print("Step 4: Test against horizon-scale data: EHT imaging, ringdown overtones.")
    print("Step 5: Planck-scale storytelling without an accessible prediction is not a solution.")
    print("CONFIRM (a picture) if: a repeatable horizon-scale observation, such as echoes in")
    print("  merger ringdowns, matches one proposal's quantitative prediction.")
    print("CONFIRM (regular core) if: EHT-resolution imaging rules out the classical shadow")
    print("  shape at the predicted deviation level.")
    print("REFUTE (a proposal) if: its predicted deviations are ruled out by EHT or LIGO data at")
    print("  the relevant precision.")
    print("REFUTE (observability hope) if: all proposals converge on identical exterior")
    print("  predictions - the interior stays hidden even in principle.")
    print("OK: %s mapped the singularity scale ladder" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usa_eternal_inflation(hdr, name, rid, group, P):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: State the e-fold requirement: 50-60 to solve the horizon problem.")
    ef = 60.0
    expansion = math.exp(ef)
    print("  e^60 = %.2e linear expansion" % expansion)
    assert 1.1e26 < expansion < 1.2e26
    print("Step 2: In most potentials inflation then never ends globally - bubbles nucleate forever.")
    print("Step 3: With infinite bubbles, every observation occurs somewhere: probabilities need")
    print("  a measure, a way of counting infinities.")
    print("Step 4: Audit each proposed measure for cutoff-independent predictions.")
    print("Step 5: The program's status is judged by progress on the measure, not popularity.")
    print("CONFIRM (scientific multiverse) if: a measure-independent prediction - such as a")
    print("  specific bubble-collision signature - is observed.")
    print("CONFIRM (eternal) if: a model predicts eternal inflation AND a unique measure that")
    print("  reproduces our observed cosmological constant.")
    print("REFUTE (scientific status) if: all measures diverge or depend on arbitrary cutoffs")
    print("  for every observable.")
    print("REFUTE (need for eternal) if: a compelling non-eternal inflation model fits all data")
    print("  with fewer assumptions - Occam applies.")
    print("OK: %s audited the measure problem" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usa_fate_universe(hdr, name, rid, group, P):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: The fate is controlled by one number: the dark-energy equation of state w.")
    print("Step 2: w = -1 -> heat death; w < -1 -> Big Rip; decaying w -> possible recollapse.")
    print("Step 3: Compute the Big Rip time for a representative phantom value, w = -1.5.")
    h0_si = 70.0e3 / 3.085677581e22
    omega_l = 0.69
    t_rip = 2.0 / (3.0 * 0.5 * h0_si * math.sqrt(omega_l))
    t_rip_gyr = t_rip / 3.15576e7 / 1e9
    print("  time to the Rip from today: %.1f billion years" % t_rip_gyr)
    assert 22.0 < t_rip_gyr < 23.0
    print("Step 4: Map current and projected DESI-era constraints on w onto the fate diagram.")
    print("Step 5: Each fate implies a different ultimate limit on life and computation.")
    print("CONFIRM (heat death) if: w converges to exactly -1 with no evolution across all probes.")
    print("CONFIRM (Rip) if: w is definitively measured below -1 - the finite-time singularity")
    print("  becomes the forecast.")
    print("REFUTE (heat death) if: time evolution of dark energy is confirmed - the constant is")
    print("  dead and dynamical fates take over.")
    print("REFUTE (any forecast) if: a late-time phase transition is possible in principle -")
    print("  far-future extrapolation is then conditional, and honesty requires saying so.")
    print("OK: %s ran the fate decision tree" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS_D = {
    "dark-energy": demo_usa_dark_energy,
    "reionization": demo_usa_reionization,
    "dark-ages": demo_usa_dark_ages,
    "giant-structures": demo_usa_giant_structures,
    "bh-information": demo_usa_bh_information,
    "singularities": demo_usa_singularities,
    "eternal-inflation": demo_usa_eternal_inflation,
    "fate-universe": demo_usa_fate_universe,
}
