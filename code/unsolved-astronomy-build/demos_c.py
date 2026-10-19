#!/usr/bin/env python3
"""Solution-explorer walkthrough demos, ranks 18-26."""


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + "import math\n" + body.replace(
        "NAME", __import__("json").dumps(name))


def demo_usa_final_parsec(hdr, name, rid, group, P):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: Compute the gravitational-wave merger time from a 1-parsec separation.")
    m1 = 1.0e8 * 1.98847e30
    m2 = 3.0e7 * 1.98847e30
    a = 3.085677581e16
    G, c = 6.67430e-11, 2.99792458e8
    t = (5.0 / 256.0) * c ** 5 * a ** 4 / (G ** 3 * m1 * m2 * (m1 + m2))
    t_yr = t / 3.15576e7
    print("  t_merge(1 pc) = %.2e years" % t_yr)
    assert 1.0e15 < t_yr < 2.0e15
    print("Step 2: That is 100,000 Hubble times - gravitational waves alone cannot finish the job.")
    print("Step 3: Score each rescue: triaxial refilling, gas-disk torques, triple interactions.")
    print("Step 4: A rescue wins only if it brings the merger time under a Hubble time.")
    print("Step 5: Pulsar-timing spectra test the surviving binary population.")
    print("CONFIRM (a mechanism) if: the gravitational-wave background spectrum matches that")
    print("  mechanism's predicted binary population.")
    print("CONFIRM (gas disks) if: parsec-scale binaries are found embedded in massive gas disks")
    print("  with measured inward torques.")
    print("REFUTE (stalling picture) if: a large population of parsec-scale binaries is imaged")
    print("  that have sat unmerged for billions of years.")
    print("REFUTE (loss-cone depletion) if: stellar kinematics show loss cones stay full in")
    print("  realistic triaxial remnants - the problem was miscalculated.")
    print("OK: %s timed the final parsec" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usa_missing_baryons(hdr, name, rid, group, P):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: Write the cosmic baryon ledger from BBN and the CMB.")
    omega_b = 0.049
    observed = 0.55
    missing = omega_b * (1.0 - observed)
    print("  Omega_b=%.3f; observed fraction=%.2f -> missing density %.4f" % (omega_b, observed, missing))
    assert 0.0220 < missing < 0.0221
    print("Step 2: The cosmic census is now closed by FRB dispersion - the action moved to halos.")
    print("Step 3: Per halo mass bin: expected baryons minus stars minus cold minus hot gas.")
    print("Step 4: Test whether feedback models eject exactly the residual.")
    print("Step 5: X-ray and UV absorption must find the warm-hot halo mass per bin.")
    print("CONFIRM (feedback) if: absorption measurements find the predicted warm-hot halo mass")
    print("  around galaxies of each mass.")
    print("CONFIRM (FRB census) if: more localized FRBs keep the cosmic ledger balanced at")
    print("  higher redshifts.")
    print("REFUTE (missing) if: deep halo censuses find the baryons were never missing - hidden")
    print("  in cold molecular gas or low-mass stars.")
    print("REFUTE (WHIM) if: the intergalactic dispersion is shown to come from a different")
    print("  phase - the ledger reopens.")
    print("OK: %s balanced the baryon ledger" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usa_small_scale_crises(hdr, name, rid, group, P):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: Quantify the missing-satellites gap.")
    pred, obs = 500.0, 60.0
    print("  predicted subhalos: %.0f; observed dwarfs: %.0f; gap factor %.2f" % (pred, obs, pred / obs))
    assert 8.0 < pred / obs < 9.0
    print("Step 2: Compute the feedback energy available per halo from its stellar mass.")
    print("Step 3: Compare the cusp mass deficit against the maximum feedback can move.")
    print("Step 4: Where feedback falls short, test self-interacting dark matter cross-sections")
    print("  against cluster-scale constraints.")
    print("Step 5: Isolated field dwarfs are the cleanest test - no tides to confuse the signal.")
    print("CONFIRM (baryonic) if: ultra-faint discoveries complete the predicted count and measured")
    print("  cores match feedback-only simulations.")
    print("CONFIRM (SIDM) if: a single cross-section explains dwarf cores without breaking")
    print("  cluster lensing constraints.")
    print("REFUTE (baryonic) if: isolated field dwarfs show cores no feedback budget can produce.")
    print("REFUTE (all CDM) if: the gap factor grows with better completeness instead of shrinking.")
    print("OK: %s quantified the small-scale gaps" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usa_dark_matter_nature(hdr, name, rid, group, P):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: Compute the thermal-relic cross-section from the observed abundance.")
    omega_h2 = 0.12
    sigma_v = 3.0e-26
    omega_pred = 0.1 * 3.0e-26 / sigma_v
    print("  <sigma v>=%.1e cm^3/s -> Omega h^2 = %.3f (observed %.2f)" % (sigma_v, omega_pred, omega_h2))
    assert 0.09 < omega_pred < 0.11
    print("Step 2: This is the WIMP miracle: weak-scale physics gives the right abundance.")
    print("Step 3: Overlay direct-detection exclusions, collider limits, and indirect searches.")
    print("Step 4: Map the surviving island per candidate class: WIMP, axion, sterile neutrino, PBH.")
    print("Step 5: Assign each island to the upcoming experiment that covers it.")
    print("CONFIRM (a candidate) if: a direct-detection signal with annual modulation is seen in")
    print("  two independent targets, or a haloscope signal is confirmed at a second facility.")
    print("CONFIRM (axion) if: the signal lands in the mass window predicted by misalignment")
    print("  production with the right relic density.")
    print("REFUTE (WIMP paradigm) if: the full thermal-relic cross-section range is excluded with")
    print("  no signal - the miracle was a coincidence.")
    print("REFUTE (a class) if: its surviving island is fully covered by a null result.")
    print("OK: %s audited the dark matter candidates" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usa_lithium_problem(hdr, name, rid, group, P):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: Compute the discrepancy factor: predicted over observed.")
    pred, obs = 4.7e-10, 1.6e-10
    factor = pred / obs
    print("  predicted %.2e vs Spite plateau %.2e -> factor %.3f" % (pred, obs, factor))
    assert 2.9 < factor < 3.0
    print("Step 2: Every solution must supply exactly this factor while sparing H and He.")
    print("Step 3: Test nuclear channels: does any resonance destroy Be-7 at BBN energies?")
    print("Step 4: Test stellar channels: diffusion and mixing models vs parameter trends.")
    print("Step 5: Test new physics: decaying particles that photodisintegrate Be-7 only.")
    print("CONFIRM (stellar) if: lithium trends with stellar parameters match diffusion models")
    print("  across many halo stars.")
    print("CONFIRM (nuclear) if: a laboratory cross-section measurement at BBN energies shows the")
    print("  needed enhancement.")
    print("REFUTE (a nuclear solution) if: the relevant cross-sections are measured and show no")
    print("  enhancement - the loophole closes.")
    print("REFUTE (uniform depletion) if: the plateau shows scatter or trends no single")
    print("  depletion factor can explain.")
    print("OK: %s quantified the lithium gap" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usa_cmb_anomalies(hdr, name, rid, group, P):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: Take the Cold Spot at face value: -70 microK over 5 degrees.")
    rms_5deg = 20.0
    z_naive = 70.0 / rms_5deg
    print("  naive significance: %.1f sigma" % z_naive)
    assert 3.4 < z_naive < 3.6
    print("Step 2: Price in the look-elsewhere effect: how many independent 5-degree patches?")
    n_patches = 525.0
    p_naive = math.erfc(z_naive / math.sqrt(2.0)) / 2.0
    p_corr = 1.0 - (1.0 - p_naive) ** n_patches
    print("  naive p=%.2e; corrected over %.0f patches: p=%.3f" % (p_naive, n_patches, p_corr))
    assert 0.10 < p_corr < 0.13
    print("Step 3: The anomaly deflates from 3.5 sigma toward ~1.2 sigma once looking is priced in.")
    print("Step 4: Rank all anomalies by corrected significance; only survivors earn modeling.")
    print("Step 5: Independent datasets - polarization, large-scale structure - are the jury.")
    print("CONFIRM (physical) if: an independent dataset shows the same preferred direction or the")
    print("  supervoid at the required depth.")
    print("CONFIRM (bubble collision) if: a predicted circular imprint with the right profile is")
    print("  found blind in polarization.")
    print("REFUTE (as physics) if: corrected significance falls below 2 sigma for every anomaly.")
    print("REFUTE (a claim) if: a foreground systematic is shown to reproduce the feature.")
    print("OK: %s priced the look-elsewhere effect" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usa_hubble_tension(hdr, name, rid, group, P):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: Compute the tension significance from the published values.")
    hl, el, hc, ec = 73.0, 1.0, 67.4, 0.5
    tension = (hl - hc) / math.sqrt(el ** 2 + ec ** 2)
    print("  (%.1f-%.1f)/sqrt(%.2f+%.2f) = %.2f sigma" % (hl, hc, el ** 2, ec ** 2, tension))
    assert 4.99 < tension < 5.02
    print("Step 2: A 5-sigma gap survived JWST's Cepheid cross-check - both sides look solid.")
    print("Step 3: Score early-universe fixes by their shift in the sound horizon.")
    print("Step 4: Score late-universe fixes by their damage to supernova and BAO fits.")
    print("Step 5: A solution must move one side 5 sigma without breaking other datasets.")
    print("CONFIRM (new physics) if: an early-universe modification raises the CMB-inferred H0 to")
    print("  73 while keeping all other fits intact.")
    print("CONFIRM (systematic) if: a distance-ladder or CMB-analysis error is found that moves")
    print("  either side by the full 5 sigma.")
    print("REFUTE (early dark energy) if: CMB polarization data excludes the required sound-horizon")
    print("  shift at high significance.")
    print("REFUTE (crisis framing) if: independent local methods converge on 67 - the ladder was")
    print("  the outlier.")
    print("OK: %s quantified the Hubble tension" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usa_cosmic_magnetism(hdr, name, rid, group, P):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: Compute the weakest seed a dynamo can amplify to observed strengths.")
    b_obs = 1.0e-6
    seed = b_obs / math.exp(30.0)
    print("  1 microG / e^30 = %.2e G required seed" % seed)
    assert 9.0e-20 < seed < 9.8e-20
    print("Step 2: Compare against astrophysical batteries: Biermann, outflows, stellar seeds.")
    print("Step 3: The void fields (~1e-16 G) sit far above any astrophysical seed.")
    print("Step 4: Where astrophysical seeds fall short, the case for primordial fields hardens.")
    print("Step 5: The spectrum of the field distinguishes inflationary from causal origins.")
    print("CONFIRM (primordial) if: void fields are measured well above any outflow-transport model")
    print("  with a spectrum matching inflationary predictions.")
    print("CONFIRM (dynamo) if: high-redshift galaxies show fields growing exactly on the")
    print("  predicted amplification curve from tiny seeds.")
    print("REFUTE (primordial need) if: a transport mechanism carries galactic fields into voids at")
    print("  the observed strengths.")
    print("REFUTE (void fields) if: the blazar lower bounds are shown to be modeling artifacts -")
    print("  the key measurement must be rock solid.")
    print("OK: %s computed the magnetic seed budget" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usa_antimatter_asymmetry(hdr, name, rid, group, P):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: State the measured asymmetry: eta = 6.1e-10 baryons per photon.")
    eta = 6.1e-10
    print("Step 2: The Standard Model's best effort falls short by a factor ~1e10.")
    sm_eta = eta / 1.0e10
    print("  SM prediction ~ %.1e vs measured %.1e" % (sm_eta, eta))
    assert 6.0e-20 < sm_eta < 6.2e-20
    print("Step 3: Run the Sakharov checklist on each candidate: B violation, CP violation,")
    print("  out-of-equilibrium - all three, quantitatively.")
    print("Step 4: Score leptogenesis with measured neutrino parameters; score electroweak")
    print("  baryogenesis against the Higgs mass window.")
    print("Step 5: Testability decides: which candidate predicts something we can measure?")
    print("CONFIRM (leptogenesis) if: neutrino CP violation is measured at the strength the")
    print("  mechanism requires, with a consistent seesaw scale.")
    print("CONFIRM (electroweak) if: a strong first-order phase transition signature is found")
    print("  compatible with collider data.")
    print("REFUTE (a candidate) if: a parameter measurement closes its viable window - the")
    print("  Higgs mass already squeezed electroweak baryogenesis hard.")
    print("REFUTE (need for new physics) if: none - the shortfall is robust; the question is")
    print("  which new physics, not whether.")
    print("OK: %s ran the Sakharov checklist" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS_C = {
    "final-parsec": demo_usa_final_parsec,
    "missing-baryons": demo_usa_missing_baryons,
    "small-scale-crises": demo_usa_small_scale_crises,
    "dark-matter-nature": demo_usa_dark_matter_nature,
    "lithium-problem": demo_usa_lithium_problem,
    "cmb-anomalies": demo_usa_cmb_anomalies,
    "hubble-tension": demo_usa_hubble_tension,
    "cosmic-magnetism": demo_usa_cosmic_magnetism,
    "antimatter-asymmetry": demo_usa_antimatter_asymmetry,
}
