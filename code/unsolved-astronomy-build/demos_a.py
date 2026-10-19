#!/usr/bin/env python3
"""Solution-explorer walkthrough demos, ranks 1-9.

Every demo: numbered walkthrough steps, adjustable assumptions, real computed
values printed, tight-bounds asserts (never float exact-equality), a
CONFIRM panel and a REFUTE panel, and the OK marker. All stdlib-only Python.
"""


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + "import math\n" + body.replace(
        "NAME", __import__("json").dumps(name))


def demo_usa_mars_life(hdr, name, rid, group, P):
    pinject = "P = %s\n" % __import__("json").dumps(P)
    return _wrap(hdr, name, rid, group, pinject + '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: Frame the question as a subsurface energy-budget problem.")
    print("Step 2: Require three independent tests per sample: metabolic, molecular, morphological.")
    print("Step 3: Combine the false-positive rates of independent lines of evidence.")
    fp = P["fp_rates"]
    joint = 1.0
    for i, r in enumerate(fp, 1):
        joint *= r
        print("  line %d: false-positive rate %.2f" % (i, r))
    print("Step 4: Joint false-positive rate for all three: %.4f" % joint)
    assert 0.0059 < joint < 0.0061
    print("Step 5: A claim needs all three lines; any single line is insufficient.")
    print("CONFIRM if: the same deep sample passes all three independent tests")
    print("  while sterilized control samples fail them.")
    print("CONFIRM if: seasonal methane spikes correlate with a metabolic signal")
    print("  in a drilled aquifer sample.")
    print("REFUTE if: deep-drilling campaigns find organics and energy sources")
    print("  but zero correlated metabolic or structural signals.")
    print("REFUTE if: every candidate biosignature is reproduced in the lab by")
    print("  abiotic perchlorate and UV chemistry.")
    print("OK: %s explored the Mars life decision tree" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usa_wow_signal(hdr, name, rid, group, P):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: Take the 1977 printout at face value: 30-sigma narrowband, 72 s drift.")
    print("Step 2: Compute how unlikely a 30-sigma noise spike is under Gaussian noise.")
    sigma = 30.0
    p_one_sided = math.erfc(sigma / math.sqrt(2.0)) / 2.0
    print("  P(>=30 sigma, Gaussian noise) = %.3e" % p_one_sided)
    assert p_one_sided < 1e-190
    print("Step 3: Note the beam profile matched a fixed celestial source exactly.")
    print("Step 4: Design the decisive test: two-station coincident stare, full polarization.")
    print("Step 5: Score outcomes in advance: repeat = artificial candidate;")
    print("  natural reproducer = case closed as natural.")
    print("CONFIRM (artificial) if: a repeat detection shows the same drift profile,")
    print("  narrow bandwidth, and sidereal repeatability at both stations.")
    print("CONFIRM (natural) if: a transient hydrogen maser reproduces the exact")
    print("  6EQUJ5 intensity profile.")
    print("REFUTE (1977 record) if: 1970s interference is demonstrated to mimic the")
    print("  printout, including the beam-drift shape.")
    print("REFUTE (interest) if: deep stares reach far below the 1977 flux with no")
    print("  repeat - the event stays unexplained but singular.")
    print("OK: %s explored the Wow! decision tree" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usa_oumuamua(hdr, name, rid, group, P):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: List the constraints: elongated, tumbling, reddish, accelerating, no coma.")
    print("Step 2: Convert the 2.5-magnitude light-curve swing to an axis ratio.")
    dm = 2.5
    axis_ratio = 10.0 ** (dm / 2.5)
    print("  axis ratio a/b = 10^(%.1f/2.5) = %.2f" % (dm, axis_ratio))
    assert 9.99 < axis_ratio < 10.01
    print("Step 3: Record the non-gravitational acceleration: %.2e m/s^2" % 4.92e-6)
    print("Step 4: Score each composition against shape + acceleration + no-dust simultaneously.")
    print("Step 5: The winner must satisfy all three; partial fits are rejected.")
    print("CONFIRM (natural) if: a future interstellar object shows the same")
    print("  acceleration-without-coma signature and spectroscopy identifies the ice.")
    print("CONFIRM (nitrogen ice) if: the acceleration magnitude matches N2 sublimation")
    print("  models within the dust non-detection limits.")
    print("REFUTE (a candidate) if: laboratory data shows no known ice can supply the")
    print("  observed acceleration under the observed non-detection limits.")
    print("REFUTE (artificial) if: natural models converge - extraordinary claims")
    print("  require the natural ledger to fail first.")
    print("OK: %s explored the Oumuamua constraint ledger" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usa_planet_nine(hdr, name, rid, group, P):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: Assume the ETNO orbital clustering is a real dynamical signal.")
    print("Step 2: Compute the orbital period for the predicted semimajor axis.")
    a = 460.0
    period_yr = a ** 1.5
    print("  a = %.0f AU -> P = a^1.5 = %.0f years" % (a, period_yr))
    assert 9860.0 < period_yr < 9875.0
    print("Step 3: Grid the allowed mass-orbit space with N-body ensembles.")
    print("Step 4: Score each grid cell against the observed clustering strength.")
    print("Step 5: Publish the probability map; surveys point at the peak first.")
    print("CONFIRM if: direct imaging or a multi-year parallax track matches a bound orbit.")
    print("CONFIRM if: a newly discovered ETNO falls exactly on the predicted shepherded track.")
    print("REFUTE if: Rubin Observatory completes its census with no candidate and a")
    print("  bias-corrected analysis shows the clustering was a survey artifact.")
    print("REFUTE if: the clustering is reproduced by a massive debris disk with no planet.")
    print("OK: %s explored the Planet Nine search box" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usa_corona_heating(hdr, name, rid, group, P):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: Write the energy ledger: active regions need ~10,000 W/m^2.")
    required = 1.0e4
    print("Step 2: Compute the Alfven-wave energy flux for measured parameters.")
    rho, v, vA = 1.0e-12, 2.0e4, 1.0e6
    f_wave = rho * v * v * vA
    print("  F_wave = rho v^2 vA = %.1f W/m^2" % f_wave)
    assert 399.0 < f_wave < 401.0
    print("Step 3: Compare: wave flux covers %.1f%% of the active-region budget." % (100.0 * f_wave / required))
    assert f_wave < required
    print("Step 4: At these parameters waves alone fall short - count nanoflare bursts next.")
    print("Step 5: Close the ledger per active region with in-situ + magnetic maps.")
    print("CONFIRM (waves) if: measured wave flux meets the required flux within")
    print("  uncertainties across multiple regions and solar conditions.")
    print("CONFIRM (nanoflares) if: burst statistics integrate to the missing flux.")
    print("REFUTE (a candidate) if: a complete ledger shows its maximum possible flux")
    print("  falls an order of magnitude short of the requirement.")
    print("REFUTE (single mechanism) if: no one mechanism closes the budget - the answer is a mix.")
    print("OK: %s balanced the coronal energy ledger" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usa_saturn_hexagon(hdr, name, rid, group, P):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: Model the hexagon as a Rossby wave on the 78-degree-N jet.")
    print("Step 2: Compute the jet circumference at that latitude.")
    r, lat = 58232.0, math.radians(78.0)
    circ = 2.0 * math.pi * r * math.cos(lat)
    print("  circumference at 78 N: %.0f km" % circ)
    assert 76000.0 < circ < 76200.0
    print("Step 3: Six wave crests divide the circumference into six sides.")
    side = circ / 6.0
    width_pp = 2.0 * side
    print("  point-to-point width: %.0f km (Earth: 12742 km)" % width_pp)
    assert 25300.0 < width_pp < 25420.0
    print("Step 4: The resonance test: wavenumber six must emerge from the measured")
    print("  jet profile with no fine-tuning, and no polygon at the south pole.")
    print("Step 5: A decade of monitoring checks the shape against wave-model drift limits.")
    print("CONFIRM if: the measured jet profile predicts wavenumber six at 78 N and no")
    print("  stable polygon at the south pole.")
    print("CONFIRM if: laboratory rotating-tank analogues reproduce the hexagon at the")
    print("  matching dimensionless parameters.")
    print("REFUTE if: the profile predicts wavenumber five or seven at the hexagon latitude.")
    print("REFUTE if: long-term monitoring shows drift the wave model forbids.")
    print("OK: %s explored the hexagon resonance" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usa_fast_radio_bursts(hdr, name, rid, group, P):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: Split the population: repeaters with structure vs one-off cannon shots.")
    print("Step 2: Compute the isotropic energy of a typical localized burst.")
    z = 0.193
    d_mpc = 987.0
    d_m = d_mpc * 3.085677581e22
    fluence = 1.0 * 1e-26 * 1e-3
    bw = 400.0e6
    e_j = 4.0 * math.pi * d_m ** 2 * fluence * bw
    e_erg = e_j * 1e7
    print("  E_iso = %.2e erg" % e_erg)
    assert 4.0e38 < e_erg < 5.5e38
    print("Step 3: Compare with the Sun: this burst equals %.1e seconds of solar output." % (e_erg / 3.828e33))
    assert 1.0e5 < e_erg / 3.828e33 < 1.5e5
    print("Step 4: Test each engine class against energy, repetition, and host environment.")
    print("Step 5: A class survives only if its budget covers its bursts.")
    print("CONFIRM (magnetar) if: a repeater is caught simultaneously in radio and X-rays")
    print("  with flare energy ratios matching magnetar physics.")
    print("CONFIRM (merger) if: a one-off burst coincides with a gravitational-wave chirp.")
    print("REFUTE (magnetar, one-offs) if: a one-off localized to an old elliptical exceeds")
    print("  any magnetar budget with no young stellar population present.")
    print("REFUTE (single engine) if: the energy span exceeds what one object class can supply.")
    print("OK: %s balanced the FRB energy ledger" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usa_fermi_paradox(hdr, name, rid, group, P):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: Hold the now-measured Drake factors fixed; isolate longevity L.")
    r_star, fp, ne = 1.5, 0.9, 0.4
    fl, fi, fc = 0.5, 0.2, 0.2
    base = r_star * fp * ne * fl * fi * fc
    print("Step 2: N = %.4f x L, with L in years." % base)
    assert 0.0107 < base < 0.0109
    for L in (1e3, 1e6, 1e9):
        print("  L = %.0e yr -> N = %.1f detectable civilizations" % (L, base * L))
    assert 10.7 < base * 1e3 < 10.9
    assert 1.07e7 < base * 1e9 < 1.09e7
    print("Step 3: Compare against SETI search completeness: a tiny slice of the haystack.")
    print("Step 4: The paradox becomes a bound: which longevities are already ruled out?")
    print("Step 5: Longevity is the decisive unknown - measure it or bound it.")
    print("CONFIRM (short-lived) if: statistics show technological civilizations self-limit")
    print("  on thousand-year timescales.")
    print("CONFIRM (long-lived) if: a confirmed technosignature proves longevity is possible.")
    print("REFUTE (paradox framing) if: a deep all-sky survey at Breakthrough Listen")
    print("  sensitivity finds zero candidates - pushing the bound toward rarity, not brevity.")
    print("REFUTE (we searched enough) if: completeness analysis shows under 0.001%% of the")
    print("  parameter space has been covered - the silence is expected, not paradoxical.")
    print("OK: %s isolated the longevity term" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usa_exoplanet_biosignatures(hdr, name, rid, group, P):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: Adopt the three-rung ladder: disequilibrium pair + context + confirmation.")
    print("Step 2: Compute the transits needed for a 5-sigma molecular detection.")
    snr1, req = 1.2, 5.0
    n = (req / snr1) ** 2
    print("  transits for SNR %.1f at %.1f per transit: %.2f -> %d" % (req, snr1, n, math.ceil(n)))
    assert 17.3 < n < 17.4
    assert math.ceil(n) == 18
    print("Step 3: Price each rung: detection, context modeling, independent confirmation.")
    print("Step 4: No claim clears without all three rungs and abiotic nulls excluded.")
    print("Step 5: Publish the ladder BEFORE the next candidate, not after.")
    print("CONFIRM (life) if: a target clears all three rungs with abiotic null models")
    print("  quantitatively excluded.")
    print("CONFIRM (rung 1) if: an O2+CH4 pair is detected at 5 sigma in the same atmosphere.")
    print("REFUTE (a candidate) if: any single abiotic pathway reproduces the spectrum within")
    print("  the measurement uncertainties.")
    print("REFUTE (single gas) if: the claimed biosignature gas is shown to build up")
    print("  abiotically under the target star - back to the ladder.")
    print("OK: %s priced the biosignature ladder" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS_A = {
    "mars-life": demo_usa_mars_life,
    "wow-signal": demo_usa_wow_signal,
    "oumuamua": demo_usa_oumuamua,
    "planet-nine": demo_usa_planet_nine,
    "corona-heating": demo_usa_corona_heating,
    "saturn-hexagon": demo_usa_saturn_hexagon,
    "fast-radio-bursts": demo_usa_fast_radio_bursts,
    "fermi-paradox": demo_usa_fermi_paradox,
    "exoplanet-biosignatures": demo_usa_exoplanet_biosignatures,
}
