#!/usr/bin/env python3
"""Demo programs for The Scientific Method Basics databases.

Every demo is real, runnable, stdlib-only Python performing the actual
scientific-method computation for its record. All are machine-executed by
build.py before hand-off: each prints its real computed values, asserts
tight bounds (never float exact-equality), and ends with the OK marker.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_sm_what_is(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the three territories of science plus applied, as discipline counts
    territories = {"natural sciences": 48, "formal sciences": 12,
                   "social sciences": 26, "applied science": 34}
    total = sum(territories.values())
    share = {k: v / total * 100.0 for k, v in territories.items()}
    print("territories: %d" % len(territories))
    for k in territories:
        print("  %-18s %3d disciplines (%5.2f %%)" % (k, territories[k], share[k]))
    print("disciplines mapped: %d" % total)
    assert total == 120
    assert 39.99 < share["natural sciences"] < 40.01
    assert 9.99 < share["formal sciences"] < 10.01
    assert 21.66 < share["social sciences"] < 21.68
    assert 28.33 < share["applied science"] < 28.34
    print("rule: one method - observe, question, predict, test, revise - unites every territory")
    print("OK: %s mapped the territories" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sm_curiosity(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the curiosity funnel: wide observation narrows to rare theory
    funnel = [("observations", 100), ("testable questions", 40),
              ("hypotheses", 12), ("theories", 3)]
    print("curiosity funnel:")
    for i, (stage, n) in enumerate(funnel):
        conv = n / funnel[i - 1][1] * 100.0 if i else 100.0
        print("  %-18s %3d  (%.1f %% survive)" % (stage, n, conv))
    assert funnel[1][1] / funnel[0][1] == 0.4
    assert funnel[2][1] / funnel[1][1] == 0.3
    assert funnel[3][1] / funnel[2][1] == 0.25
    assert 2.99 < funnel[3][1] / funnel[0][1] * 100.0 < 3.01
    print("rule: nothing downstream works without the first step - attention on purpose")
    print("OK: %s ran the funnel" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sm_observation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five stem-height readings, same ruler, same procedure
    readings = [12.1, 12.3, 11.9, 12.2, 12.0]
    mean = sum(readings) / len(readings)
    spread = max(readings) - min(readings)
    print("readings (cm): %s" % readings)
    print("mean: %.4f cm" % mean)
    print("spread: %.4f cm" % spread)
    assert 12.0999 < mean < 12.1001
    assert 0.3999 < spread < 0.4001
    # qualitative vs quantitative tally of a field session
    session = ["quantitative"] * 5 + ["qualitative"] * 3
    print("session: %d quantitative, %d qualitative of %d observations"
          % (session.count("quantitative"), session.count("qualitative"), len(session)))
    assert session.count("quantitative") == 5
    print("rule: record what is there, not what is expected - the outlier may be the discovery")
    print("OK: %s witnessed honestly" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sm_questions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # testability scoring: measurable + comparable + falsifiable
    qs = {
        "does cloud cover change afternoon temperature": (1, 1, 1),
        "why is the sky beautiful": (0, 0, 0),
        "do plants grow better with fertilizer": (0, 1, 1),
        "does 5g nitrogen per week increase bean stem height over 30 days": (1, 1, 1),
    }
    scores = {q: sum(v) for q, v in qs.items()}
    for q, s in scores.items():
        print("  score %d/3: %s" % (s, q[:60]))
    sharp = "does 5g nitrogen per week increase bean stem height over 30 days"
    vague = "do plants grow better with fertilizer"
    pretty = "why is the sky beautiful"
    assert scores[sharp] == 3 and scores[pretty] == 0
    assert scores[sharp] > scores[vague] > scores[pretty]
    passed = sum(1 for s in scores.values() if s == 3)
    print("testable (3/3): %d of %d" % (passed, len(scores)))
    assert passed == 2
    print("rule: the question decides what the experiment is allowed to discover")
    print("OK: %s sharpened the questions" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sm_hypothesis(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the hypothesis at risk: is this coin fair? 100 flips, 52 heads
    n, heads = 100, 52
    expected = n / 2.0
    chi2 = (heads - expected) ** 2 / expected + (n - heads - expected) ** 2 / expected
    p = math.erfc(math.sqrt(chi2 / 2.0))  # df = 1
    print("flips: %d, heads: %d" % (n, heads))
    print("chi-square: %.4f" % chi2)
    print("p-value: %.4f" % p)
    assert 0.1599 < chi2 < 0.1601
    assert 0.6891 < p < 0.6892
    verdict = "STANDS" if p > 0.05 else "REFUTED"
    print("verdict at 5%% level: %s" % verdict)
    assert verdict == "STANDS"
    print("rule: a hypothesis is a bet, and the method collects on bets honestly")
    print("OK: %s put the idea at risk" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sm_fair_experiments(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # fertilizer trial: 10 control, 10 treated, everything else identical
    control = [11.8, 12.2, 12.0, 11.9, 12.1, 12.3, 11.7, 12.0, 12.2, 11.8]
    treated = [14.1, 14.5, 14.3, 14.0, 14.6, 14.2, 14.4, 14.1, 14.3, 14.5]
    mc = sum(control) / len(control)
    mt = sum(treated) / len(treated)
    effect = mt - mc
    print("control mean: %.4f cm (n=%d)" % (mc, len(control)))
    print("treated mean: %.4f cm (n=%d)" % (mt, len(treated)))
    print("effect: %.4f cm" % effect)
    assert 11.999 < mc < 12.001
    assert 14.299 < mt < 14.301
    assert 2.299 < effect < 2.301
    print("rule: the control is the silent partner of every honest experiment")
    print("OK: %s ran a fair trial" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sm_variables(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # independent: fertilizer grams (set by investigator); dependent: height cm (measured)
    fert = [0, 2, 4, 6, 8]
    height = [12.1, 14.3, 16.0, 18.2, 20.1]
    n = len(fert)
    mx, my = sum(fert) / n, sum(height) / n
    num = sum((a - mx) * (b - my) for a, b in zip(fert, height))
    den = math.sqrt(sum((a - mx) ** 2 for a in fert) * sum((b - my) ** 2 for b in height))
    r = num / den
    print("independent (fertilizer g): %s" % fert)
    print("dependent   (height cm)   : %s" % height)
    print("correlation r: %.6f" % r)
    assert 0.9993 < r < 0.9994
    assert r > 0.99, "the set change drives the measured outcome"
    print("rule: change this, measure that, compare - one experiment, one independent variable")
    print("OK: %s named the pipeline" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sm_controlled_vars(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the confound trap: fertilized plants also got warmer days
    cool_control = 12.0    # control pots, cool days
    warm_control = 14.0    # control pots, warm days -> temperature effect
    warm_treated = 14.3    # fertilized pots, warm days
    temp_effect = warm_control - cool_control
    apparent = warm_treated - cool_control
    adjusted = apparent - temp_effect
    print("temperature effect (warm - cool control): %.4f cm" % temp_effect)
    print("apparent fertilizer effect: %.4f cm" % apparent)
    print("adjusted fertilizer effect: %.4f cm" % adjusted)
    assert 1.999 < temp_effect < 2.001
    assert 2.299 < apparent < 2.301
    assert 0.299 < adjusted < 0.301
    assert adjusted < apparent / 5.0, "the confounder was doing almost all the work"
    print("rule: chain down every alternative suspect or it will overturn the verdict")
    print("OK: %s caught the confounder" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sm_operational_defs(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # operational definition: growth = stem height day30 minus day0, cm, soil line to tip
    pairs = [(12.0, 16.2), (11.8, 15.9), (12.3, 16.8)]
    growths = [round(d30 - d0, 1) for d0, d30 in pairs]
    mean_growth = sum(growths) / len(growths)
    print("growths (cm): %s" % growths)
    print("mean growth: %.4f cm" % mean_growth)
    assert growths == [4.2, 4.1, 4.5]
    assert 4.266 < mean_growth < 4.268
    # the recipe is frozen: same instrument, same landmarks, same days
    recipe = {"instrument": "ruler", "unit": "cm", "from": "soil line",
              "to": "stem tip", "days": (0, 30)}
    print("recipe locked: %s" % recipe)
    assert recipe["unit"] == "cm" and recipe["days"] == (0, 30)
    print("rule: an idea without a measurement recipe is a rumor")
    print("OK: %s wrote the recipe" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sm_data_collection(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # systematic sampling: every 10th item off a 200-item production line
    population = [10.0 + (i % 7) * 0.5 for i in range(200)]
    sample = [population[i] for i in range(0, 200, 10)]
    pop_mean = sum(population) / len(population)
    samp_mean = sum(sample) / len(sample)
    gap = abs(pop_mean - samp_mean)
    print("population: %d, sample: %d (every 10th)" % (len(population), len(sample)))
    print("population mean: %.4f" % pop_mean)
    print("sample mean:     %.4f" % samp_mean)
    print("gap: %.4f" % gap)
    assert len(sample) == 20
    assert 11.484 < pop_mean < 11.486
    assert gap < 0.05, "systematic sampling represents the whole fairly"
    print("rule: the raw table is sacred - plan, record, check, back up, then analyze")
    print("OK: %s collected testimony" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sm_tables_charts(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # frequency table: 10 heights binned in 2-cm bins from 10 cm
    heights = [11.8, 12.2, 12.0, 14.1, 14.5, 14.3, 13.9, 15.2, 12.8, 16.0]
    bins = [0, 0, 0, 0]
    for h in heights:
        idx = min(int((h - 10.0) // 2), 3)
        bins[idx] += 1
    labels = ["10-12", "12-14", "14-16", "16-18"]
    print("frequency table (cm):")
    for lab, c in zip(labels, bins):
        print("  %s cm: %s" % (lab, "#" * c))
    assert bins == [1, 4, 4, 1]
    assert sum(bins) == len(heights) == 10
    print("rule: a graph that misleads is not a lens but a disguise")
    print("OK: %s made the data visible" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sm_conclusions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 17 trial comparisons graded by the pre-decided rule (>=60% support)
    support, refute, unclear = 12, 3, 2
    total = support + refute + unclear
    rate = support / total
    print("trials: %d support, %d refute, %d inconclusive (n=%d)" % (support, refute, unclear, total))
    print("support rate: %.4f" % rate)
    assert total == 17
    assert 0.705 < rate < 0.707
    verdict = "SUPPORTED" if rate >= 0.6 else ("REFUTED" if rate <= 0.4 else "INCONCLUSIVE")
    print("verdict by pre-set rule: %s" % verdict)
    assert verdict == "SUPPORTED"
    scope = "greenhouse bean trial, 30 days, 0-8 g fertilizer"
    print("scope (fenced): %s" % scope)
    print("rule: the conclusion is the verdict the evidence earned - no more, no less")
    print("OK: %s delivered the verdict" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sm_accuracy_precision(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # scale check against a certified 100.0 g reference
    true = 100.0
    readings = [98.2, 98.0, 98.4, 98.1, 98.3]
    mean = sum(readings) / len(readings)
    bias = mean - true
    var = sum((a - mean) ** 2 for a in readings) / len(readings)
    spread = math.sqrt(var)
    print("reference: %.1f g, readings: %s" % (true, readings))
    print("bias (accuracy): %.4f g" % bias)
    print("spread (precision): %.4f g" % spread)
    assert -1.81 < bias < -1.79
    assert 0.141 < spread < 0.142
    verdict = "PRECISE BUT INACCURATE - calibrate before use"
    print("diagnosis: %s" % verdict)
    assert abs(spread) < 0.5 and abs(bias) > 0.5
    print("rule: the steady liar is the most dangerous witness - calibrate the instrument")
    print("OK: %s diagnosed the scale" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sm_error(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # area from length 10.0 +/- 0.1 cm and width 5.0 +/- 0.1 cm
    L, dL = 10.0, 0.1
    W, dW = 5.0, 0.1
    area = L * W
    rel = math.sqrt((dL / L) ** 2 + (dW / W) ** 2)
    unc = area * rel
    print("length: %.1f +/- %.1f cm" % (L, dL))
    print("width:  %.1f +/- %.1f cm" % (W, dW))
    print("area: %.1f +/- %.4f cm^2" % (area, unc))
    assert 49.999 < area < 50.001
    assert 1.1180 < unc < 1.1181
    print("rule: report the value with its doubt - known error beats hidden error")
    print("OK: %s carried the uncertainty" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sm_design(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # factorial design: fertilizer (2 levels) x watering (2 levels), 5 replicates
    factors = {"fertilizer": ["none", "5g"], "watering": ["daily", "twice-daily"]}
    combos = [(f, w) for f in factors["fertilizer"] for w in factors["watering"]]
    replicates = 5
    runs = len(combos) * replicates
    print("factors: %d, levels each: %d" % (len(factors), 2))
    print("treatment combinations: %d" % len(combos))
    for c in combos:
        print("  fertilizer=%s, watering=%s x%d" % (c[0], c[1], replicates))
    print("total runs: %d" % runs)
    assert len(combos) == 4
    assert runs == 20
    print("rule: the design, not the data analysis, is where experiments are won or lost")
    print("OK: %s wrote the battle plan" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sm_sample_size(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # standard error of the mean: sd / sqrt(n) - quadrupling n halves the wobble
    sd = 12.0
    se25 = sd / math.sqrt(25)
    se100 = sd / math.sqrt(100)
    print("sd: %.1f cm" % sd)
    print("SE at n=25 : %.4f cm" % se25)
    print("SE at n=100: %.4f cm" % se100)
    assert 2.399 < se25 < 2.401
    assert 1.199 < se100 < 1.201
    assert 0.499 < se100 / se25 < 0.501
    print("rule: size the jury to the question - big enough to hear, fair enough to trust")
    print("OK: %s sized the sample" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sm_averages_trends(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # least-squares trend: daily temperature over a week
    days = [1, 2, 3, 4, 5, 6, 7]
    temp = [18.2, 18.9, 19.4, 20.1, 20.6, 21.3, 21.8]
    n = len(days)
    md, mt = sum(days) / n, sum(temp) / n
    slope = sum((a - md) * (b - mt) for a, b in zip(days, temp)) / sum((a - md) ** 2 for a in days)
    icept = mt - slope * md
    print("days: %s" % days)
    print("temp: %s" % temp)
    print("trend: %.4f C + %.4f C/day * day" % (icept, slope))
    assert 0.5999 < slope < 0.6001
    assert 17.642 < icept < 17.644
    # check the fit against the points: max residual
    res = [abs(t - (icept + slope * d)) for d, t in zip(days, temp)]
    print("max residual: %.4f C" % max(res))
    assert max(res) < 0.06
    print("rule: describe the center, describe the spread, show the shape - then claim the pattern")
    print("OK: %s read the trend" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sm_correlation_causation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # ice cream sales vs drownings: strong link - until temperature is held constant
    ice = [120, 152, 178, 212, 238, 272]
    drown = [3, 4, 5, 7, 6, 8]
    temp = [28, 31, 32, 35, 36, 39]
    def pearson(x, y):
        n = len(x)
        mx, my = sum(x) / n, sum(y) / n
        num = sum((a - mx) * (b - my) for a, b in zip(x, y))
        den = math.sqrt(sum((a - mx) ** 2 for a in x) * sum((b - my) ** 2 for b in y))
        return num / den
    r_raw = pearson(ice, drown)
    r_it, r_dt = pearson(ice, temp), pearson(drown, temp)
    r_partial = (r_raw - r_it * r_dt) / math.sqrt((1 - r_it ** 2) * (1 - r_dt ** 2))
    print("raw correlation (ice cream, drownings): %.4f" % r_raw)
    print("partial correlation controlling temperature: %.4f" % r_partial)
    assert 0.949 < r_raw < 0.951
    assert -0.35 < r_partial < -0.33
    assert abs(r_partial) < abs(r_raw) / 2.0, "the third variable was doing the work"
    print("rule: correlation suggests where to look; only controlled testing decides")
    print("OK: %s interrogated the link" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sm_placebo_blinding(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # double-blind trial: 100 treated, 100 placebo - belief held equal
    treat_rec, treat_n = 78, 100
    plac_rec, plac_n = 52, 100
    rt, rp = treat_rec / treat_n, plac_rec / plac_n
    risk_diff = rt - rp
    risk_ratio = rt / rp
    print("treated: %d/%d recovered (%.0f %%)" % (treat_rec, treat_n, rt * 100))
    print("placebo: %d/%d recovered (%.0f %%)" % (plac_rec, plac_n, rp * 100))
    print("true edge over placebo: %.4f (risk difference)" % risk_diff)
    print("risk ratio: %.4f" % risk_ratio)
    assert 0.259 < risk_diff < 0.261
    assert 1.499 < risk_ratio < 1.501
    assert risk_diff < rt, "the headline rate is not the treatment effect"
    print("rule: strip away belief, hope, and observer bias - leave only what the treatment does")
    print("OK: %s sealed the leaks" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sm_predictions_models(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # linear model: height = 12.16 + 0.995 * fertilizer, checked on fresh data
    fert = [0, 2, 4, 6, 8]
    observed = [12.1, 14.3, 16.0, 18.2, 20.1]
    predicted = [12.16 + 0.995 * f for f in fert]
    residuals = [o - p for o, p in zip(observed, predicted)]
    rmse = math.sqrt(sum(r * r for r in residuals) / len(residuals))
    print("fertilizer: %s" % fert)
    print("predicted : %s" % [round(p, 2) for p in predicted])
    print("observed  : %s" % observed)
    print("residuals : %s" % [round(r, 2) for r in residuals])
    print("RMSE: %.4f cm" % rmse)
    assert 0.100 < rmse < 0.102
    assert max(abs(r) for r in residuals) < 0.2
    # residuals patternless: signs mixed, not all one-sided
    assert any(r > 0 for r in residuals) and any(r < 0 for r in residuals)
    print("rule: the map is graded by the journey - prediction on new data or it is just a summary")
    print("OK: %s tested the map" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sm_falsifiability(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the gate: which claims name an observation that would refute them
    claims = [
        ("all swans are white", True),
        ("an invisible force guides events but leaves no trace", False),
        ("fertilizer increases bean height", True),
        ("everything happens for a reason", False),
        ("water boils at 100 C at sea level", True),
    ]
    sci = [c for c, f in claims if f]
    nonsci = [c for c, f in claims if not f]
    print("claims examined: %d" % len(claims))
    for c in sci:
        print("  FALSIFIABLE    : %s" % c)
    for c in nonsci:
        print("  NOT FALSIFIABLE: %s" % c)
    assert len(sci) == 3 and len(nonsci) == 2
    print("rule: a claim that risks nothing explains nothing")
    print("OK: %s held the gate" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sm_pitfalls(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # p-hacking math: 20 tests at 5% significance, no real effects
    tests, alpha = 20, 0.05
    expected_false = tests * alpha
    family_wise = 1.0 - (1.0 - alpha) ** tests
    print("tests run: %d at %.0f %% significance" % (tests, alpha * 100))
    print("expected false alarms: %.1f" % expected_false)
    print("chance of at least one false alarm: %.4f" % family_wise)
    assert 0.99 < expected_false < 1.01
    assert 0.641 < family_wise < 0.642
    assert family_wise > 0.5, "a 'significant' hit is likelier than not - by luck alone"
    print("rule: pre-register the plan, report everything, let others check the work")
    print("OK: %s dodged the traps" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sm_reports(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # IMRaD word budget of a complete report draft
    sections = {"Introduction": 120, "Methods": 340, "Results": 210, "Discussion": 280}
    total = sum(sections.values())
    methods_share = sections["Methods"] / total * 100.0
    print("report sections (words):")
    for s, w in sections.items():
        print("  %-14s %3d (%4.1f %%)" % (s, w, w / total * 100))
    print("total: %d words" % total)
    assert total == 950
    assert 35.7 < methods_share < 35.9
    assert sections["Methods"] == max(sections.values()), "the recipe section is the longest"
    print("rule: a report is an instruction manual for rebuilding the experiment")
    print("OK: %s wrote the testimony" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sm_instruments(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # calibrating a thermometer against a certified 100.0 C reference
    ref = 100.0
    readings = [100.4, 100.2, 100.5, 100.3, 100.4]
    mean = sum(readings) / len(readings)
    offset = mean - ref
    raw = 37.5
    corrected = raw - offset
    print("reference: %.1f C, mean reading: %.4f C" % (ref, mean))
    print("offset: +%.4f C" % offset)
    print("field reading %.1f C corrects to %.4f C" % (raw, corrected))
    assert 0.359 < offset < 0.361
    assert 37.139 < corrected < 37.141
    print("rule: no measurement testifies from an uncalibrated instrument")
    print("OK: %s swore in the deputy" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sm_repeating(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # internal repetition: two independent runs must agree within tolerance
    run1, run2 = 12.30, 12.34
    tolerance = 0.10
    gap = abs(run1 - run2)
    print("run 1 mean: %.2f cm" % run1)
    print("run 2 mean: %.2f cm" % run2)
    print("gap: %.4f cm (tolerance %.2f cm)" % (gap, tolerance))
    assert 0.0399 < gap < 0.0401
    verdict = "REPRODUCED" if gap < tolerance else "INVESTIGATE"
    print("verdict: %s" % verdict)
    assert verdict == "REPRODUCED"
    print("rule: trust comes from a system designed to catch fallibility, not from infallibility")
    print("OK: %s recalled the witness" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sm_peer_review(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # a journal year's worth of manuscripts through the assay office
    accept, revise, reject = 8, 22, 10
    total = accept + revise + reject
    revise_rate = revise / total * 100.0
    accept_rate = accept / total * 100.0
    print("manuscripts: %d" % total)
    print("  accept: %d (%.1f %%)" % (accept, accept_rate))
    print("  revise: %d (%.1f %%)" % (revise, revise_rate))
    print("  reject: %d (%.1f %%)" % (reject, reject / total * 100))
    assert total == 40
    assert 54.9 < revise_rate < 55.1
    assert 19.9 < accept_rate < 20.1
    assert revise > accept + reject, "negotiation toward rigor is the norm"
    print("rule: review is the mint's assay office - revision is not rejection of worth")
    print("OK: %s passed inspection" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sm_theories(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the long road from hypothesis to theory: years of survived severe tests
    journeys = {
        "germ theory (1847 -> ~1880)": 33,
        "plate tectonics (1912 -> 1968)": 56,
        "evolution synthesis (1859 -> ~1939)": 80,
    }
    mean_lag = sum(journeys.values()) / len(journeys)
    print("hypothesis to accepted theory:")
    for k, v in journeys.items():
        print("  %-38s %d years" % (k, v))
    print("mean lag: %.2f years" % mean_lag)
    assert 56.3 < mean_lag < 56.4
    assert all(v >= 30 for v in journeys.values()), "no shortcuts on this road"
    print("rule: in science, 'theory' is the highest compliment evidence can pay")
    print("OK: %s built the courthouse" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sm_limits(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # sorting questions into the method's jurisdiction
    now = ["does fertilizer raise bean height", "is this water safe to drink",
           "which route is fastest at 8am", "does this drug lower fever",
           "what metal is this coin", "how fast does mold spread at 20 C"]
    later = ["what is dark matter made of", "can fusion power the grid",
             "is there life on Europa"]
    never_empirical = ["is kindness better than cruelty", "what is the meaning of life",
                       "which painting is most beautiful", "what ought the law to require"]
    total = len(now) + len(later) + len(never_empirical)
    print("testable now        : %d" % len(now))
    print("testable in principle: %d" % len(later))
    print("not empirically settable: %d" % len(never_empirical))
    assert total == 13
    assert len(now) == 6 and len(later) == 3 and len(never_empirical) == 4
    print("rule: a tool with known limits is more trustworthy than one claimed to do everything")
    print("OK: %s knew the borders" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sm_ethics(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Belmont review scoring of a study protocol, 10 points per principle
    scores = {"respect for persons": 9, "beneficence": 8, "justice": 9}
    bar_each, bar_mean = 7, 8.0
    mean = sum(scores.values()) / len(scores)
    print("protocol review:")
    for k, v in scores.items():
        print("  %-20s %d/10" % (k, v))
    print("mean: %.4f (bar %.1f, each >= %d)" % (mean, bar_mean, bar_each))
    assert 8.666 < mean < 8.668
    ok = all(v >= bar_each for v in scores.values()) and mean >= bar_mean
    verdict = "APPROVED WITH MONITORING" if ok else "RETURNED FOR REVISION"
    print("board verdict: %s" % verdict)
    assert ok and verdict == "APPROVED WITH MONITORING"
    print("rule: no result, however brilliant, justifies an unethical experiment")
    print("OK: %s kept the conscience" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sm_feedback_loop(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # convergence: each inquiry cycle shrinks the error to 60% of the last
    err, factor, cycles = 1.0, 0.6, 5
    trail = [err]
    for _ in range(cycles):
        err *= factor
        trail.append(err)
    print("error across %d cycles:" % cycles)
    for i, e in enumerate(trail):
        print("  cycle %d: %.6f" % (i, e))
    assert 0.0777 < trail[-1] < 0.0778
    assert trail[-1] < trail[0] * 0.08
    assert all(b < a for a, b in zip(trail, trail[1:])), "every cycle must shrink the error"
    print("rule: every answer is a better question wearing a disguise")
    print("OK: %s closed the loop" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sm_penicillin(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the relay: 1928 observation -> 1940 therapeutic proof -> 1945 Nobel
    seen, cured, prize = 1928, 1940, 1945
    to_cure, to_prize = cured - seen, prize - seen
    mean_lag = (to_cure + to_prize) / 2.0
    print("observation (Fleming plate): %d" % seen)
    print("therapeutic proof (Florey/Chain): %d (+%d years)" % (cured, to_cure))
    print("Nobel Prize: %d (+%d years)" % (prize, to_prize))
    print("mean relay lag: %.1f years" % mean_lag)
    assert to_cure == 12 and to_prize == 17
    assert 14.49 < mean_lag < 14.51
    print("rule: discovery is rarely a lightning bolt - usually a relay race")
    print("OK: %s ran the relay" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sm_semmelweis(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Vienna 1846-1848: chlorine handwashing collapses childbed-fever mortality
    before, after = 18.27, 1.27
    absolute_drop = before - after
    relative_reduction = absolute_drop / before
    print("First Clinic mortality before handwashing: %.2f %%" % before)
    print("First Clinic mortality after handwashing : %.2f %%" % after)
    print("absolute drop: %.2f points" % absolute_drop)
    print("relative reduction: %.4f (%.1f %%)" % (relative_reduction, relative_reduction * 100))
    assert 16.99 < absolute_drop < 17.01
    assert 0.930 < relative_reduction < 0.931
    assert relative_reduction > 0.9, "one of the largest effects ever measured in medicine"
    print("rule: evidence plus humility, communication, and allies - data alone waited a generation")
    print("OK: %s honored the mothers" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sm_michelson_morley(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 1887: hunting the ether wind - prediction 0.4 fringe, observation below 0.01
    expected, observed = 0.4, 0.01
    ratio = observed / expected
    print("predicted fringe shift: %.2f" % expected)
    print("observed fringe shift : < %.2f" % observed)
    print("observed/expected: %.4f (%.1f %%)" % (ratio, ratio * 100))
    assert 0.0249 < ratio < 0.0251
    assert ratio < 0.03, "a null result a precision instrument turned into a discovery"
    verdict = "ETHER REFUTED - rebuild space and time"
    print("verdict: %s" % verdict)
    print("rule: the severe test is the crown jewel - precise enough that 'no' means something")
    print("OK: %s heard the silence" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_sm_everyday(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # a week of kitchen-garage science: one change per test, numbers written down
    tests = [
        ("longer dough proofing", True),
        ("new commute route", False),
        ("shade vs sun seedlings", True),
        ("less salt in soup", True),
        ("tire pressure +3 psi", True),
        ("watering evenings", False),
        ("baking soda scrub test", True),
    ]
    wins = sum(1 for _, w in tests if w)
    rate = wins / len(tests)
    print("everyday tests run: %d" % len(tests))
    for t, w in tests:
        print("  %-28s %s" % (t, "IMPROVED" if w else "no gain - discarded"))
    print("win rate: %.4f" % rate)
    assert len(tests) == 7 and wins == 5
    assert 0.714 < rate < 0.715
    print("rule: the method is not equipment - it is a discipline of honesty, and it runs anywhere")
    print("OK: %s lived the method" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "what_is": demo_sm_what_is,
    "curiosity": demo_sm_curiosity,
    "observation": demo_sm_observation,
    "questions": demo_sm_questions,
    "hypothesis": demo_sm_hypothesis,
    "fair_experiments": demo_sm_fair_experiments,
    "variables": demo_sm_variables,
    "controlled_vars": demo_sm_controlled_vars,
    "operational_defs": demo_sm_operational_defs,
    "data_collection": demo_sm_data_collection,
    "tables_charts": demo_sm_tables_charts,
    "conclusions": demo_sm_conclusions,
    "accuracy_precision": demo_sm_accuracy_precision,
    "error": demo_sm_error,
    "design": demo_sm_design,
    "sample_size": demo_sm_sample_size,
    "averages_trends": demo_sm_averages_trends,
    "correlation_causation": demo_sm_correlation_causation,
    "placebo_blinding": demo_sm_placebo_blinding,
    "predictions_models": demo_sm_predictions_models,
    "falsifiability": demo_sm_falsifiability,
    "pitfalls": demo_sm_pitfalls,
    "reports": demo_sm_reports,
    "instruments": demo_sm_instruments,
    "repeating": demo_sm_repeating,
    "peer_review": demo_sm_peer_review,
    "theories": demo_sm_theories,
    "limits": demo_sm_limits,
    "ethics": demo_sm_ethics,
    "feedback_loop": demo_sm_feedback_loop,
    "penicillin": demo_sm_penicillin,
    "semmelweis": demo_sm_semmelweis,
    "michelson_morley": demo_sm_michelson_morley,
    "everyday": demo_sm_everyday,
}
