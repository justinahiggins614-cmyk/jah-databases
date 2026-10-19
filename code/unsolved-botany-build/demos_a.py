#!/usr/bin/env python3
"""Solution-explorer walkthrough demos, ranks 1-9.

Every demo: numbered walkthrough steps, adjustable assumptions, real computed
values printed, tight-bounds asserts (never float exact-equality), a
CONFIRM panel and a REFUTE panel, and the OK marker. All stdlib-only Python.
"""


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + "import math\n" + body.replace(
        "NAME", __import__("json").dumps(name))


def demo_autumn_colors(hdr, name, rid, group, P):
    pinject = "P = %s\n" % __import__("json").dumps(P)
    return _wrap(hdr, name, rid, group, pinject + '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: Frame the photoprotection hypothesis as a nitrogen budget.")
    print("Step 2: Compare nitrogen recovery of red vs yellow leaves.")
    red = P["red_gain"]; yellow = P["yellow_gain"]; n = P["n_reps"]
    print("  red-leaf N recovery gain: %.2f, yellow: %.2f (n=%d)" % (red, yellow, n))
    diff = red - yellow
    print("Step 3: Difference in recovery: %.2f" % diff)
    assert 0.07 < diff < 0.09
    print("Step 4: Test the light-dependence: bagged leaves should lose the gap.")
    bagged_diff = diff * 0.1
    print("  bagged-leaf gap shrinks to: %.3f" % bagged_diff)
    assert bagged_diff < 0.01
    print("Step 5: Photoprotection predicts the gap tracks light, not chemistry.")
    print("CONFIRM if: anthocyanin content correlates with N recovery and the")
    print("  correlation vanishes under light exclusion.")
    print("REFUTE if: red and yellow leaves recover identical nitrogen under")
    print("  identical light, or insect exclusion changes nothing about herbivory.")
    print("OK: %s explored the autumn color decision tree" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_flytrap_counts(hdr, name, rid, group, P):
    pinject = "P = %s\n" % __import__("json").dumps(P)
    return _wrap(hdr, name, rid, group, pinject + '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: Model the calcium register: each touch adds, then decays.")
    inc = P["increment"]; tau = P["decay_tau_s"]; thr = P["closure_threshold"]
    level = 0.0
    for touch in (1, 2):
        level = level * math.exp(-5.0 / tau) + inc
        print("  after touch %d: register = %.3f" % (touch, level))
    print("Step 2: Register after two quick touches: %.3f vs threshold %.1f" % (level, thr))
    assert level > thr
    print("Step 3: After 60 s of silence the register should reset.")
    level = level * math.exp(-60.0 / tau)
    print("  register after 60 s: %.3f" % level)
    assert level < thr
    print("Step 4: Digestion needs ~5 touches: register must reach higher rungs.")
    print("CONFIRM if: touch-count thresholds for closure, jasmonate, digestion")
    print("  all shift quantitatively with perturbed calcium dynamics.")
    print("REFUTE if: downstream thresholds move independently of the calcium")
    print("  register, implying parallel counting circuits.")
    print("OK: %s explored the flytrap counting register" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_phototropism(hdr, name, rid, group, P):
    pinject = "P = %s\n" % __import__("json").dumps(P)
    return _wrap(hdr, name, rid, group, pinject + '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: A blue-light gradient hits one side of the hypocotyl.")
    ang = P["light_angle_deg"]; ratio = P["auxin_ratio"]; rate = P["bend_rate"]
    print("  light at %.0f deg, shaded:lit auxin ratio %.1f" % (ang, ratio))
    print("Step 2: Auxin asymmetry drives differential growth.")
    bend = rate * math.log(ratio) * (ang / 90.0)
    print("  predicted bend rate: %.3f deg/min" % bend)
    assert 0.2 < bend < 0.6
    print("Step 3: Knock out the candidate kinase: relocation should stall.")
    print("Step 4: Map the full time-ordered chain phototropin -> PIN -> auxin.")
    print("CONFIRM if: a complete time-ordered chain is mapped with each step")
    print("  necessary for bending.")
    print("REFUTE if: bending persists when candidate phosphorylation steps are")
    print("  blocked, forcing the search toward unknown components.")
    print("OK: %s explored the phototropism wiring" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_seed_dormancy(hdr, name, rid, group, P):
    pinject = "P = %s\n" % __import__("json").dumps(P)
    return _wrap(hdr, name, rid, group, pinject + '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: Model dormancy as a leaky integrator over cold days.")
    days = P["cold_days"]; aba = P["aba"]; ga = P["ga"]; thr = P["threshold"]
    ratio = ga / aba
    score = 0.0
    for _ in range(days):
        score = score * 0.97 + 0.03 * ratio
    print("  ABA %.1f, GA %.1f, ratio %.3f" % (aba, ga, ratio))
    print("  integrated score after %d cold days: %.3f (threshold %.2f)" % (days, score, thr))
    print("Step 2: Germination fires when the score crosses threshold.")
    print("Step 3: The same parameters must predict across winters.")
    assert score < thr
    print("  score below threshold: seed correctly stays dormant at this ratio.")
    print("Step 4: Germination fires only when the ratio itself shifts (cold, light).")
    print("CONFIRM if: one integrator parameter set predicts germination timing")
    print("  across different winters and genotypes.")
    print("REFUTE if: decisions depend on signal sequences the integrator cannot")
    print("  represent, implying a more complex state machine.")
    print("OK: %s explored the seed dormancy integrator" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_florigen(hdr, name, rid, group, P):
    pinject = "P = %s\n" % __import__("json").dumps(P)
    return _wrap(hdr, name, rid, group, pinject + '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: FT protein travels leaf -> apex; repressors oppose it.")
    ft = P["ft_dose"]; rep = P["repressor"]; crit = P["critical_ratio"]
    ratio = ft / rep
    print("  FT dose %.1f, repressor %.1f, ratio %.2f (critical %.1f)" % (ft, rep, ratio, crit))
    print("Step 2: Flowering fires when ratio crosses the critical value.")
    assert ratio >= crit
    print("Step 3: The ratio - not absolute FT - should predict flowering.")
    print("CONFIRM if: a single critical FT:repressor ratio predicts flowering")
    print("  across day lengths, temperatures, and plant ages.")
    print("REFUTE if: flowering occurs at wildly different ratios under different")
    print("  conditions, implying parallel decisive pathways.")
    print("OK: %s explored the florigen ratio switch" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_carnivory(hdr, name, rid, group, P):
    pinject = "P = %s\n" % __import__("json").dumps(P)
    return _wrap(hdr, name, rid, group, pinject + '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: Carnivory evolved >=%d times; test for convergent rewiring." % P["origins"])
    shared = P["shared_genes"]; bc = P["benefit_cost"]
    print("  shared repurposed genes: %d, benefit:cost ratio %.1f" % (shared, bc))
    assert shared > 20
    print("Step 2: Benefit must exceed cost only in nutrient-poor, sunny, wet sites.")
    assert bc > 1.0
    print("Step 3: Activate candidate regulators in a non-carnivorous relative.")
    print("CONFIRM if: the same regulatory rewiring appears at multiple independent")
    print("  origins and produces trap-like structures when activated.")
    print("REFUTE if: each origin uses entirely different genetic routes with no")
    print("  shared regulatory logic.")
    print("OK: %s explored the carnivory switch" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_plant_warning(hdr, name, rid, group, P):
    pinject = "P = %s\n" % __import__("json").dumps(P)
    return _wrap(hdr, name, rid, group, pinject + '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: Communication requires the EMITTER to gain fitness.")
    kin = P["kin_gain"]; stranger = P["stranger_gain"]; wind = P["wind_loss"]
    print("  emitter gain with kin receivers: %.2f, strangers: %.2f" % (kin, stranger))
    net = kin * (1.0 - wind)
    print("Step 2: Net emitter gain after wind loss (%.0f%%): %.3f" % (wind * 100, net))
    assert net > stranger
    print("Step 3: Volatile-blocking controls isolate the airborne channel.")
    print("CONFIRM if: emitters leave more offspring when surrounded by responding")
    print("  kin than by non-responding strangers.")
    print("REFUTE if: no emitter fitness difference in any arrangement - the")
    print("  phenomenon reduces to eavesdropping.")
    print("OK: %s explored the warning-vs-eavesdropping test" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_vernalization(hdr, name, rid, group, P):
    pinject = "P = %s\n" % __import__("json").dumps(P)
    return _wrap(hdr, name, rid, group, pinject + '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: Each cell flips FLC off independently with probability p.")
    weeks = P["cold_weeks"]; p = P["switch_prob"]; cells = P["cells"]
    frac = 1.0 - (1.0 - p) ** weeks
    silenced = int(cells * frac)
    print("  after %d cold weeks: %.1f%% of %d cells silenced (%d cells)" % (weeks, frac * 100, cells, silenced))
    assert 0.85 < frac < 0.95
    print("Step 2: Whole-plant memory = silenced fraction -> flowering time.")
    print("Step 3: Perturb Polycomb: the switching threshold should move.")
    print("CONFIRM if: flowering time is predicted quantitatively by the silenced")
    print("  cell fraction across cold durations and genotypes.")
    print("REFUTE if: coordinated all-or-nothing switching implies a tissue-level")
    print("  signal instead of cell-autonomous memory.")
    print("OK: %s explored the winter memory switch" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bristlecone_longevity(hdr, name, rid, group, P):
    pinject = "P = %s\n" % __import__("json").dumps(P)
    return _wrap(hdr, name, rid, group, pinject + '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: A %d-year-old tree shows no reproductive decline." % P["age_years"])
    mut = P["mutation_rate"]; rep = P["repair_genes"]
    print("  meristem mutation rate: %.2f/yr, repair genes: %d" % (mut, rep))
    total = mut * P["age_years"]
    print("Step 2: Naive accumulation over %d years: %.0f mutations." % (P["age_years"], total))
    assert 90 < total < 110
    print("Step 3: If repair works, observed load should be far below naive.")
    print("CONFIRM if: expanded repair gene families plus near-zero mutation")
    print("  buildup in millennia-old meristems.")
    print("REFUTE if: mutation loads rise with age like short-lived trees -")
    print("  longevity would be ecological luck, not genomic program.")
    print("OK: %s explored the bristlecone longevity program" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS_A = {
    "autumn-colors": demo_autumn_colors,
    "flytrap-counts": demo_flytrap_counts,
    "phototropism": demo_phototropism,
    "seed-dormancy": demo_seed_dormancy,
    "florigen": demo_florigen,
    "carnivory": demo_carnivory,
    "plant-warning": demo_plant_warning,
    "vernalization": demo_vernalization,
    "bristlecone-longevity": demo_bristlecone_longevity,
}
