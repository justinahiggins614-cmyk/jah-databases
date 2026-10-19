#!/usr/bin/env python3
"""Solution-explorer walkthrough demos, ranks 10-17."""


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + "import math\n" + body.replace(
        "NAME", __import__("json").dumps(name))


def demo_usa_hot_jupiters(hdr, name, rid, group, P):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: Assume core accretion beyond the ice line; the planet must have moved.")
    print("Step 2: Recover the orbital period from Kepler's third law.")
    a, m = 0.0527, 1.06
    p_yr = math.sqrt(a ** 3 / m)
    p_d = p_yr * 365.25
    print("  a=%.4f AU, M*=%.2f Msun -> P=%.3f days" % (a, m, p_d))
    assert 4.28 < p_d < 4.31
    print("Step 3: The migration channels predict different spin-orbit alignments.")
    print("Step 4: Compute the tidal realignment timescale for each system in the sample.")
    print("Step 5: Misaligned survivors with long realignment times = violent scattering.")
    print("CONFIRM (disk migration) if: aligned systems outnumber the tidal-realignment prediction.")
    print("CONFIRM (scattering) if: misaligned systems are exactly those whose stars cannot")
    print("  tidally realign them within their ages.")
    print("REFUTE (a channel) if: misaligned systems have realignment times far shorter than")
    print("  their ages - the misalignment must then be primordial.")
    print("REFUTE (migration-only) if: a hot Jupiter is found with a composition proving")
    print("  in-situ formation beyond doubt.")
    print("OK: %s tested the migration channels" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usa_earth_water(hdr, name, rid, group, P):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: Treat D/H as a provenance fingerprint; write the two-source mixing equation.")
    dh_e, dh_a, dh_c = 1.56e-4, 1.50e-4, 3.10e-4
    f_comet = (dh_e - dh_a) / (dh_c - dh_a)
    print("  ocean D/H=%.2e, asteroid=%.2e, comet=%.2e" % (dh_e, dh_a, dh_c))
    print("  maximum cometary fraction: %.4f (%.2f%%)" % (f_comet, 100.0 * f_comet))
    assert 0.037 < f_comet < 0.038
    print("Step 2: The ocean value sits near the asteroidal end - comets are a small admixture at most.")
    print("Step 3: Propagate measurement uncertainties to bound the allowed range.")
    print("Step 4: Fold in the deep-mantle reservoir as a third source.")
    print("Step 5: Returned asteroid samples give the decisive D/H anchor.")
    print("CONFIRM (asteroid dominance) if: returned carbonaceous samples match ocean D/H")
    print("  within tight bounds across multiple bodies.")
    print("CONFIRM (endogenous) if: mantle water D/H matches the surface, requiring no late veneer.")
    print("REFUTE (comet minority) if: a survey shows most Jupiter-family comets share Earth's")
    print("  D/H, not just Hartley 2.")
    print("REFUTE (two-source) if: no mixing of measured reservoirs reproduces the ocean value -")
    print("  a missing source is required.")
    print("OK: %s solved the isotope mixing ledger" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usa_moon_formation(hdr, name, rid, group, P):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: Write the two-column ledger: isotopes and angular momentum.")
    L_tot, L_spin = 3.41e34, 5.86e33
    frac = L_spin / L_tot
    print("  Earth spin share of system angular momentum: %.3f" % frac)
    assert 0.171 < frac < 0.173
    print("Step 2: Score each impact variant on both columns quantitatively.")
    print("Step 3: Canonical impact balances momentum but strains on isotopes.")
    print("Step 4: Synestia and fast-spinning variants trade one column for the other.")
    print("Step 5: The winner matches both with no tuned parameters.")
    print("CONFIRM (a variant) if: a simulation simultaneously matches isotopic identity and")
    print("  angular momentum with no tuned parameters.")
    print("CONFIRM (mixing) if: a post-impact process is shown to homogenize isotopes while")
    print("  preserving the momentum budget.")
    print("REFUTE (canonical) if: a refractory-element isotopic difference is confirmed that no")
    print("  mixing scenario can erase.")
    print("REFUTE (all giant impacts) if: lunar samples demand a composition no impact model")
    print("  can produce - back to capture or fission scenarios.")
    print("OK: %s balanced the Moon-formation ledger" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usa_kuiper_cliff(hdr, name, rid, group, P):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: Extrapolate the smooth-disk size distribution beyond 48 AU.")
    expected = 14.0
    observed = 0.0
    print("  expected detections beyond the cliff: %.0f; observed: %.0f" % (expected, observed))
    print("Step 2: Compute the Poisson probability of seeing zero when expecting %.0f." % expected)
    p_zero = math.exp(-expected)
    print("  P(0 | %.0f) = %.2e" % (expected, p_zero))
    assert p_zero < 1e-6
    print("Step 3: The shortfall is real - a truncation mechanism must reproduce the sharpness.")
    print("Step 4: Test stellar encounter, Neptune migration, and unseen planet against")
    print("  both the cliff location and its sharpness.")
    print("Step 5: The edge's sharpness is the decisive clue.")
    print("CONFIRM (stellar encounter) if: solar siblings are identified whose trajectories")
    print("  converge on a close pass at the right epoch.")
    print("CONFIRM (planet) if: a distant planet is found whose resonances carve exactly this edge.")
    print("REFUTE (truncation) if: a deep survey finds a smooth continuation of small objects")
    print("  beyond the cliff - the edge is then size-sorting, not truncation.")
    print("REFUTE (encounter) if: no plausible birth-cluster history permits a close enough pass.")
    print("OK: %s quantified the Kuiper shortfall" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usa_uhecr(hdr, name, rid, group, P):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: Compute the photopion threshold for protons on CMB photons.")
    m_p, m_pi = 938.0e6, 140.0e6
    eps = 6.3e-4
    e_th = (2.0 * m_p * m_pi + m_pi ** 2) / (4.0 * eps)
    print("  head-on threshold: %.2e eV" % e_th)
    assert 1.0e20 < e_th < 1.2e20
    print("Step 2: Above threshold the mean free path is megaparsecs - sources must be local.")
    print("Step 3: Audit every candidate accelerator inside ~50 Mpc against the Hillas criterion.")
    print("Step 4: Fold in composition: heavier nuclei shrink the horizon further.")
    print("Step 5: The suspect list is short - test each against arrival directions.")
    print("CONFIRM (a source class) if: arrival directions correlate with that class above chance")
    print("  after correcting for magnetic deflection, with matching composition.")
    print("CONFIRM (nearby AGN) if: the Amaterasu-class events trace back to local accelerators")
    print("  once deflections are modeled.")
    print("REFUTE (proton astronomy) if: composition proves heavy at the highest energies -")
    print("  horizons shrink and deflections grow, deepening the mystery.")
    print("REFUTE (known accelerators) if: no local object passes the Hillas audit - new physics")
    print("  of acceleration is required.")
    print("OK: %s computed the GZK horizon budget" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usa_grb_engine(hdr, name, rid, group, P):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: Correct the isotropic energy for beaming using the jet break angle.")
    e_iso = 8.8e54
    theta = math.radians(5.0)
    f_b = 1.0 - math.cos(theta)
    e_true = e_iso * f_b
    print("  E_iso=%.2e erg, theta=5 deg -> beaming fraction %.4f" % (e_iso, f_b))
    print("  true energy: %.2e erg" % e_true)
    assert 3.2e52 < e_true < 3.5e52
    print("Step 2: Compare against the magnetar ceiling: ~1e52 erg of rotation energy.")
    print("  This burst exceeds it by a factor %.1f -> requires a black hole engine." % (e_true / 1e52))
    assert e_true > 1e52
    print("Step 3: Apply the ceiling test burst by burst across the sample with jet breaks.")
    print("Step 4: Sort engines by budget: magnetar below ceiling, black hole above.")
    print("Step 5: Mixed populations are allowed - the test is per burst, not per class.")
    print("CONFIRM (black hole) if: burst energy exceeds the magnetar ceiling plus a late X-ray")
    print("  plateau inconsistent with magnetar spin-down.")
    print("CONFIRM (magnetar) if: a burst under the ceiling shows the magnetar's predicted")
    print("  spin-down light curve.")
    print("REFUTE (magnetar, broadly) if: a population analysis shows most bursts exceed its budget.")
    print("REFUTE (beaming correction) if: jet breaks are shown to mismeasure opening angles")
    print("  systematically - the ledger must be redone.")
    print("OK: %s applied the engine energy ceiling" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usa_first_stars(hdr, name, rid, group, P):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: With only H2 cooling, find the Jeans mass at the cooling floor.")
    T, n = 200.0, 1.0e4
    k, G, mp, mu = 1.380649e-16, 6.67430e-8, 1.6726219e-24, 1.22
    rho = n * mu * mp
    mj = (math.pi / 6.0) * (k * T / (G * mu * mp)) ** 1.5 * rho ** -0.5
    mj_sun = mj / 1.98847e33
    print("  T=%.0f K, n=%.0e cm^-3 -> Jeans mass = %.1f solar masses" % (T, n, mj_sun))
    assert 165.0 < mj_sun < 172.0
    print("Step 2: Fragmentation sets the characteristic mass near a hundred suns - the classic")
    print("  massive Population III picture.")
    print("Step 3: Cross-check against nucleosynthesis: metal-poor stars record supernova yields.")
    print("Step 4: Pair-instability yields = ~150 Msun progenitors; core-collapse = lower masses.")
    print("Step 5: JWST hunts He II 1640 emission and pair-instability supernovae.")
    print("CONFIRM (massive) if: metal-poor stars show abundance patterns matching")
    print("  pair-instability yields of ~150-solar-mass progenitors.")
    print("CONFIRM (ordinary) if: JWST first-galaxy light requires only ordinary-mass stars.")
    print("REFUTE (monolithic monsters) if: simulations with full physics converge on")
    print("  fragmentation to tens of solar masses with no 100+ Msun tail.")
    print("REFUTE (detectability soon) if: rate calculations show Pop III supernovae are")
    print("  centuries apart in any survey volume - patience, not new physics, is needed.")
    print("OK: %s computed the first-star mass scale" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usa_smbh_seeds(hdr, name, rid, group, P):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: Count the e-foldings from a stellar seed to a billion suns.")
    seed, final = 100.0, 1.0e9
    efolds = math.log(final / seed)
    print("  ln(%.0e/%.0f) = %.2f e-foldings" % (final, seed, efolds))
    assert 16.1 < efolds < 16.2
    print("Step 2: Multiply by the Salpeter time at the Eddington limit.")
    t = efolds * 45.0
    print("  growth time: %.1f Myr vs universe age at z=7.5: ~700 Myr" % t)
    assert 720.0 < t < 730.0
    print("Step 3: The margin is zero or negative - stellar seeds need help.")
    print("Step 4: Compute the minimum seed mass each quasar requires; test seed channels.")
    print("Step 5: Where seeds fail, quantify the super-Eddington duty cycle required.")
    print("CONFIRM (heavy seeds) if: intermediate-mass black holes are found at high redshift")
    print("  with no stellar-seed pathway.")
    print("CONFIRM (super-Eddington) if: sustained super-Eddington accretion is demonstrated")
    print("  in simulations with realistic feedback.")
    print("REFUTE (crisis) if: revised mass estimates shrink the high-z monsters by an order")
    print("  of magnitude - the clock then has room.")
    print("REFUTE (direct collapse) if: pristine atomic-cooling halos are shown to always")
    print("  fragment - the heavy-seed channel closes.")
    print("OK: %s raced the black-hole growth clock" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS_B = {
    "hot-jupiters": demo_usa_hot_jupiters,
    "earth-water": demo_usa_earth_water,
    "moon-formation": demo_usa_moon_formation,
    "kuiper-cliff": demo_usa_kuiper_cliff,
    "uhecr": demo_usa_uhecr,
    "grb-engine": demo_usa_grb_engine,
    "first-stars": demo_usa_first_stars,
    "smbh-seeds": demo_usa_smbh_seeds,
}
