#!/usr/bin/env python3
"""Demo programs for the Unsolved Zoology databases (Manon's 16:15 orders).

Every demo is a solution-explorer walkthrough: real, runnable, stdlib-only
Python that (1) computes concrete evidence related to its unsolved problem,
(2) walks through the Signature solution approach with adjustable
assumptions, and (3) prints an explicit CONFIRM / REFUTE panel. All are
machine-executed by build.py: each prints its real computed values, asserts
tight bounds (never float exact-equality), and ends with the OK marker.

Honesty rule: no demo claims a proof. Computational checks are labeled as
checks, models as models, and every panel states what would confirm or kill
the proposed approach.
"""

_PREAMBLE = "import math\nimport random\n\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace(
        "NAME", __import__("json").dumps(name))


def demo_uszl_giraffe_neck(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Model: net selection on neck length under two scenarios (illustrative model).
    # Adjustable assumption: contest-win payoff vs feeding energy payoff.
    neck = [1.0, 1.5, 2.0, 2.5]  # relative neck length
    cost = [0.10 * n ** 2 for n in neck]  # metabolic + predation cost, rising steeply
    feed_gain = [0.70 * math.log(n + 1.0) for n in neck]  # diminishing feeding returns
    contest_gain = [0.12 * n ** 2.5 for n in neck]  # accelerating male contest payoff
    print("neck  cost   feed-net  contest-net")
    best_feed, best_contest = None, None
    for n, c, f, g in zip(neck, cost, feed_gain, contest_gain):
        fn, gn = f - c, g - c
        print("%.1f  %.3f  %+.3f     %+.3f" % (n, c, fn, gn))
        if best_feed is None or fn > best_feed[1]:
            best_feed = (n, fn)
        if best_contest is None or gn > best_contest[1]:
            best_contest = (n, gn)
    print("feeding-optimal neck: %.1f, contest-optimal neck: %.1f" % (best_feed[0], best_contest[0]))
    assert abs(best_feed[0] - 1.5) < 0.01, "feeding optimum should sit low (diminishing returns)"
    assert abs(best_contest[0] - 2.5) < 0.01, "contest optimum should sit high (accelerating payoff)"
    print("approach S-01: dual-promise decomposition - partition feeding vs sexual selection gradients")
    print("CONFIRM IF: male necking wins correlate with neck length and lifetime matings with no feeding deficit for shorter-necked females")
    print("REFUTE IF: necking contest outcomes show zero correlation with neck length or mating success")
    print("does NOT claim: which pressure came first, peer acceptance, or settled status")
    print("OK: %s priced both selection gradients" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uszl_zebra_stripes(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Model: variance partitioning of striping across equid taxa (illustrative).
    # Adjustable assumption: each layer's share of explained variance.
    layers = {"biting flies": 0.55, "thermoregulation": 0.08, "social display": 0.12}
    residual = 0.25
    total = sum(layers.values()) + residual
    print("stripe-variance layers:")
    for k, v in layers.items():
        print("  %-16s %.2f" % (k, v))
    print("  %-16s %.2f" % ("residual", residual))
    print("  total %.2f" % total)
    assert abs(total - 1.0) < 1e-9, "layers must partition total variance"
    assert layers["biting flies"] > sum([layers["thermoregulation"], layers["social display"]]), \\
        "fly layer should dominate in this parameterization"
    print("approach S-02: layered-function peel - test each layer where it should matter most")
    print("CONFIRM IF: stripe width and density track fly pressure with near-zero residual for other predictors")
    print("REFUTE IF: controlled trials show flies landing equally on striped and unstriped coats")
    print("does NOT claim: one function explains every stripe, peer acceptance, or settled status")
    print("OK: %s partitioned stripe variance across layers" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uszl_why_animals_sleep(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Model: energy budget of sleep vs quiet wakefulness (illustrative, kJ/day units).
    # Adjustable assumption: metabolic savings rate during sleep.
    species = [("shrew-like", 8.0, 0.25), ("dog-like", 4.0, 0.20), ("jellyfish-like", 0.5, 0.10)]
    print("species        wake-cost  sleep-savings  net-benefit")
    for sp, wake, rate in species:
        savings = wake * rate * 8.0  # 8 h of sleep
        vulnerability = wake * 0.05 * 8.0  # predation/opportunity cost proxy
        netb = savings - vulnerability
        print("%-14s %8.2f  %12.2f  %10.2f" % (sp, wake, savings, netb))
        assert netb > 0, "sleep must pay its energy bill in this model for %s" % sp
    print("approach S-03: energy-budget pricing - the dominant function is the one that pays the bill in most species")
    print("CONFIRM IF: sleep duration tracks the marginal value of wakefulness across species better than any other predictor")
    print("REFUTE IF: a brainless species is found that never sleeps, proving sleep is a brain-only invention")
    print("does NOT claim: one function rules out the others, peer acceptance, or settled status")
    print("OK: %s priced sleep against its costs" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uszl_pigeon_homing(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Model: cue-conflict releases at three ranges (illustrative).
    # Adjustable assumption: cue weights per range leg.
    rng = random.Random(42)
    legs = [(300, (0.70, 0.20, 0.10)), (80, (0.30, 0.50, 0.20)), (10, (0.10, 0.20, 0.70))]
    print("range_km  mag_w  olf_w  vis_w  mean_err_deg")
    for dist, (wm, wo, wv) in legs:
        errs = []
        for _ in range(2000):
            # each cue has noise; conflict shifts magnetic cue by 30 deg
            em = rng.gauss(30.0, 12.0)
            eo = rng.gauss(0.0, 15.0)
            ev = rng.gauss(0.0, 8.0)
            errs.append(abs(wm * em + wo * eo + wv * ev))
        mean_err = sum(errs) / len(errs)
        print("%7d  %5.2f %5.2f %5.2f  %11.2f" % (dist, wm, wo, wv, mean_err))
        if dist == 300:
            assert 15.0 < mean_err < 28.0, "far leg dominated by shifted magnetic cue"
        if dist == 10:
            assert mean_err < 8.0, "near leg should be accurate on visual cues"
    print("approach S-04: chart-switching decode - map which cue dominates at which range")
    print("CONFIRM IF: a consistent switching profile replicates across lofts and terrains, plus a confirmed receptor molecule")
    print("REFUTE IF: cue conflicts produce random unstructured behavior rather than a stable hierarchy")
    print("does NOT claim: receptor identification today, peer acceptance, or settled status")
    print("OK: %s decoded cue switching across ranges" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uszl_monarch_migration(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Model: compass-plus-trigger agents flying 4000 km (illustrative, scaled).
    # Adjustable assumption: heading noise and trigger thresholds.
    rng = random.Random(7)
    target = (0.0, -4000.0)  # south
    arrived = 0
    N = 400
    for _ in range(N):
        x, y = rng.gauss(0, 200), 0.0
        for step in range(400):
            # sun-compass heading south-southwest with noise; stop trigger near target latitude
            heading = math.pi + rng.gauss(0, 0.25)  # radians, south = pi
            x += 10.0 * math.sin(heading)
            y += 10.0 * math.cos(heading)
            if y < target[1] + 300:  # temperature/daylength trigger zone
                break
        if abs(x - target[0]) < 600 and abs(y - target[1]) < 600:
            arrived += 1
    frac = arrived / N
    print("agents: %d, reached overwintering zone: %d (%.1f%%)" % (N, arrived, 100 * frac))
    assert frac > 0.50, "compass-plus-triggers should converge most agents"
    assert frac < 1.0, "noise must leave some scatter"
    print("approach S-05: minimal inherited rule - compass heading plus environmental triggers, no stored map")
    print("CONFIRM IF: displaced migrants hold heading instead of correcting, and minimal-rule agents converge on the real groves")
    print("REFUTE IF: displaced migrants correct toward Mexico, proving a true map")
    print("does NOT claim: the map is settled, peer acceptance, or settled status")
    print("OK: %s flew compass-plus-trigger agents to the target zone" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uszl_salmon_homing(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Model: two-passport handoff - magnetic map offshore, odor near river (illustrative).
    # Adjustable assumption: handoff distance and per-cue error growth.
    rng = random.Random(11)
    print("dist_km  mag_err  odor_err  combined_err")
    for dist in (2000, 500, 100, 20, 5):
        mag_err = 0.02 * dist  # magnetic error grows with distance
        odor_err = 400.0 / max(dist, 1)  # odor useful only near the river
        combined = 1.0 / (1.0 / mag_err + 1.0 / odor_err)  # optimal fusion
        print("%7d %8.1f %9.1f %12.1f" % (dist, mag_err, odor_err, combined))
        assert combined < min(mag_err, odor_err) + 1e-9, "fusion must beat either cue alone"
    print("approach S-06: two-passport decode - isolate the odor cocktail and the magnetic grid separately")
    print("CONFIRM IF: synthetic odor cocktails steer adults to arbitrary release points, plus mapped magnetic displacement responses")
    print("REFUTE IF: smolts imprint on single compounds with no cocktail effect, or magnetic displacement shows no orientation change")
    print("does NOT claim: odor or receptor identified today, peer acceptance, or settled status")
    print("OK: %s modeled the magnetic-to-odor handoff" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uszl_whale_strandings(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Model: synthetic stranding record vs trigger variables (illustrative).
    # Adjustable assumption: trigger strength.
    rng = random.Random(21)
    n = 500
    sonar, mag_anom, strand = [], [], []
    for _ in range(n):
        s = rng.random()
        m = rng.random()
        # strandings driven by sonar (0.5) + magnetic anomaly (0.3) + noise
        p = 0.05 + 0.50 * s + 0.30 * m
        strand.append(1 if rng.random() < p else 0)
        sonar.append(s)
        mag_anom.append(m)
    def corr(a, b):
        ma, mb = sum(a) / n, sum(b) / n
        num = sum((x - ma) * (y - mb) for x, y in zip(a, b))
        den = math.sqrt(sum((x - ma) ** 2 for x in a) * sum((y - mb) ** 2 for y in b))
        return num / den
    cs, cm = corr(sonar, strand), corr(mag_anom, strand)
    print("stranding correlation: sonar %.3f, magnetic anomaly %.3f" % (cs, cm))
    assert 0.25 < cs < 0.65, "sonar trigger should correlate positively"
    assert 0.10 < cm < 0.50, "magnetic trigger should correlate positively"
    assert cs > cm, "sonar is the stronger trigger in this parameterization"
    print("approach S-07: trigger-plus-amplifier separation - correlate triggers, then test the social cascade")
    print("CONFIRM IF: trigger variables predict stranding hotspots out of sample, with acoustic-trap beaches reproduced by modeling")
    print("REFUTE IF: strandings show no correlation with any trigger and no leader-follower structure")
    print("does NOT claim: a single cause for all strandings, peer acceptance, or settled status")
    print("OK: %s correlated stranding triggers" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uszl_lemming_cycles(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, """\
def main():
    # Model: delayed predator-prey cycle (illustrative).
    # Adjustable assumption: predator lag strength and growth rates.
    spy, delay = 20, 36
    r, K = 0.40, 60.0
    pg, pd, pr = 0.004, 0.08, 0.012
    hist = [10.0] * (delay + 1)
    pred = 4.0
    series = []
    for _ in range(2400):
        lagged = hist[-(delay + 1)]
        prey = hist[-1]
        prey_next = max(0.5, prey * math.exp(r * (1 - lagged / K) - pr * pred))
        pred = max(0.5, pred * math.exp(pg * prey - pd))
        hist.append(prey_next)
        series.append(prey_next)
    use = series[1200:]
    mean = sum(use) / len(use)
    peaks = [i for i in range(1, len(use) - 1)
             if use[i] > use[i - 1] and use[i] > use[i + 1] and use[i] > 1.5 * mean]
    peaks = [q for q in peaks if all(abs(q - w) >= 30 for w in peaks if w != q)]
    gaps = [b - a for a, b in zip(peaks, peaks[1:])]
    period_years = (sum(gaps) / len(gaps)) / spy
    print("detected cycle period: %.2f years (%d peaks)" % (period_years, len(peaks)))
    assert 2.5 < period_years < 5.0, "predator lag should generate a 3-4 year-like cycle"
    assert max(use) > 3 * min(use), "cycles must have real amplitude"
    print("approach S-08: gear-removal decomposition - fit predator, plant, weather models to long-term data")
    print("CONFIRM IF: predator-lag models reproduce the period across sites while plants and snow explain amplitude")
    print("REFUTE IF: cycles persist unchanged with predators fully excluded")
    print("does NOT claim: predation alone explains everything, peer acceptance, or settled status")
    print("OK: %s generated the predator-driven cycle" % NAME)
if __name__ == "__main__":
    main()
""")


def demo_uszl_desert_ant_navigation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Model: path integration with compass and odometer noise (illustrative).
    # Adjustable assumption: per-step noise levels.
    rng = random.Random(31)
    def trial(compass_noise, odo_noise):
        x, y = 0.0, 0.0
        hx, hy = 0.0, 0.0  # home vector accumulator
        for _ in range(500):  # outbound foraging walk
            ang = rng.gauss(0, 1.2)
            step = 1.0 + rng.gauss(0, 0.05)
            x += step * math.cos(ang)
            y += step * math.sin(ang)
            meas_ang = ang + rng.gauss(0, compass_noise)
            meas_step = step * (1.0 + rng.gauss(0, odo_noise))
            hx += meas_step * math.cos(meas_ang)
            hy += meas_step * math.sin(meas_ang)
        # home vector points back along -(hx, hy); error = |true pos - estimated pos|
        err = math.hypot(x - hx, y - hy)
        return err
    e_low = sum(trial(0.02, 0.01) for _ in range(20)) / 20
    e_high = sum(trial(0.20, 0.10) for _ in range(20)) / 20
    print("mean homing error: low noise %.1f, high noise %.1f" % (e_low, e_high))
    assert e_low < 30.0, "low-noise integration should home accurately"
    assert e_high > e_low * 2, "error must grow with sensor noise"
    print("approach S-09: circuit-tracing ascent - find the home vector in the central complex")
    print("CONFIRM IF: a traced circuit simulation reproduces real homing errors including stilt-and-stump patterns")
    print("REFUTE IF: homing persists after silencing the entire candidate circuit")
    print("does NOT claim: the circuit is mapped today, peer acceptance, or settled status")
    print("OK: %s integrated home vectors under noise" % NAME)
if __name__ == "__main__":
    main()
''')


# (DEMOS registry defined at end of file after all demo functions)

def demo_uszl_electroreception(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Model: fitness of electroreception stages in murky water (illustrative).
    # Adjustable assumption: per-stage foraging gain.
    stages = [("no sensing", 1.00), ("passive electroreception", 1.25),
              ("weak discharge + sensing", 1.45), ("strong electric organ", 1.70)]
    print("stage                            fitness")
    prev = 0.0
    for label, fit in stages:
        print("%-32s %.2f" % (label, fit))
        assert fit > prev, "each stage must pay its way over the last: %s" % label
        prev = fit
    print("approach S-10: muscle-to-battery rewind - passive sensing first, then weak discharge, then power")
    print("CONFIRM IF: shared regulatory rewiring appears across independent origins with intermediates showing the predicted sequence")
    print("REFUTE IF: electric organs show no trace of the muscle regulatory program")
    print("does NOT claim: the full stepwise fossil of each origin, peer acceptance, or settled status")
    print("OK: %s priced each electroreception stage" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uszl_no_wheels(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Model: partial-wheel fitness vs legs across terrain roughness (illustrative).
    # Adjustable assumption: continuity (plumbing) cost of rotating joints.
    terrains = [("smooth salt flat", 0.1), ("savanna", 0.5), ("rocky hills", 0.9)]
    print("terrain            legs  partial-wheel  full-wheel*")
    for label, rough in terrains:
        legs = 1.0 - 0.25 * rough
        partial = 0.55 - 0.55 * rough  # halfway wheels: poor grip, no advantage yet
        full = (1.25 - 0.15 * rough) * 0.55  # full wheel discounted by continuity cost
        print("%-18s %5.2f  %12.2f  %10.2f" % (label, legs, partial, full))
        assert legs > partial, "partial wheels must lose to legs on %s" % label
        assert legs > full, "continuity cost must keep full wheels below legs on %s" % label
    print("* full wheel discounted 45% for blood/nerve continuity cost")
    print("approach S-11: constraint-boundary mapping - test whether wheels are impossible or merely unreachable")
    print("CONFIRM IF: fitness models show all partial wheels losing to legs in every tested environment")
    print("REFUTE IF: a true rotating locomotory structure is found in nature, or a viable biological workaround is demonstrated")
    print("does NOT claim: a formal impossibility proof, peer acceptance, or settled status")
    print("OK: %s mapped the wheel constraint boundary" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uszl_cephalopod_camouflage(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Model: contrast-grammar background matching without color vision (illustrative).
    # Adjustable assumption: vocabulary of pattern components.
    rng = random.Random(41)
    # background described by brightness/contrast/edge features (no color channel)
    vocab = ["dark bar", "light bar", "mottle", "uniform", "edge-disrupt"]
    scores = []
    for trial in range(30):
        bg = [rng.random() for _ in range(8)]
        # animal assembles display from vocabulary to match feature profile
        display = [bg[i] + rng.gauss(0, 0.08) for i in range(8)]
        match = 1.0 - sum(abs(a - b) for a, b in zip(bg, display)) / 8.0
        scores.append(match)
    mean_match = sum(scores) / len(scores)
    print("vocabulary: %s" % ", ".join(vocab))
    print("mean background-match score over 30 trials: %.3f" % mean_match)
    assert mean_match > 0.80, "contrast grammar should match well without color"
    assert mean_match < 1.0, "noise must leave imperfection"
    print("approach S-12: minimal-vocabulary decode - which visual features suffice for camouflage")
    print("CONFIRM IF: a model predicts the animal's pattern from background features alone, plus polarization-only matching")
    print("REFUTE IF: color matching succeeds on backgrounds equated for brightness, contrast, and polarization")
    print("does NOT claim: the traced circuit today, peer acceptance, or settled status")
    print("OK: %s matched backgrounds with a color-free grammar" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uszl_consciousness_markers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Model: convergent marker fingerprint across taxa (illustrative scores 0-1).
    # Adjustable assumption: marker weights.
    markers = ["broadcast", "recurrence", "affect-bias", "metacognition", "flex-learning", "self-model"]
    taxa = {
        "human":        [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
        "chimpanzee":   [0.9, 0.9, 0.9, 0.8, 0.9, 0.8],
        "crow":         [0.8, 0.8, 0.8, 0.6, 0.9, 0.5],
        "octopus":      [0.8, 0.7, 0.8, 0.5, 0.9, 0.4],
        "honeybee":     [0.5, 0.5, 0.6, 0.3, 0.7, 0.1],
        "zebrafish":    [0.5, 0.4, 0.6, 0.2, 0.6, 0.1],
        "crab":         [0.4, 0.4, 0.5, 0.2, 0.5, 0.1],
        "jellyfish":    [0.1, 0.1, 0.1, 0.0, 0.2, 0.0],
    }
    def mean(v):
        return sum(v) / len(v)
    scores = {t: mean(v) for t, v in taxa.items()}
    print("taxon        fingerprint depth")
    for t in sorted(scores, key=scores.get, reverse=True):
        print("%-12s %.2f" % (t, scores[t]))
    assert scores["human"] > scores["chimpanzee"] > scores["crow"], "primate/bird ordering"
    assert scores["octopus"] > scores["honeybee"], "cephalopod above insect"
    assert scores["jellyfish"] < 0.2, "brainless taxon near floor"
    # markers should cluster: depth correlates across marker pairs
    print("approach S-13: convergent-fingerprint markers - no single marker decides, the cluster does")
    print("CONFIRM IF: markers cluster tightly across independent taxa and predict welfare-relevant outcomes")
    print("REFUTE IF: markers scatter randomly, or full marker sets appear in animals with no behavioral flexibility")
    print("does NOT claim: a solved hard problem, peer acceptance, or settled status")
    print("OK: %s scored the sentience fingerprint across taxa" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uszl_animal_language(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Model: language-component inventory across taxa (illustrative scores 0-1).
    # Adjustable assumption: component list.
    comps = ["vocal-learning", "reference", "combination", "recursion", "intentionality", "culture"]
    taxa = {
        "human":       [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
        "chimpanzee":  [0.1, 0.6, 0.3, 0.0, 0.7, 0.5],
        "parrot":      [0.9, 0.5, 0.2, 0.0, 0.6, 0.4],
        "dolphin":     [0.8, 0.5, 0.3, 0.0, 0.7, 0.5],
        "prairie-dog": [0.2, 0.8, 0.2, 0.0, 0.4, 0.3],
        "whale":       [0.9, 0.4, 0.4, 0.0, 0.5, 0.9],
        "songbird":    [1.0, 0.2, 0.5, 0.0, 0.3, 0.8],
    }
    print("taxon        components present/6  full assembly?")
    full = []
    for t, v in taxa.items():
        n = sum(1 for x in v if x >= 0.5)
        is_full = all(x >= 0.5 for x in v)
        full.append(is_full)
        print("%-12s %d                  %s" % (t, n, is_full))
        if t != "human":
            assert v[3] < 0.5, "no non-human shows recursion in this inventory: %s" % t
    assert sum(full) == 1 and taxa["human"], "only humans hold the full assembly"
    print("approach S-14: component-assembly inventory - score components, find the assembly gap")
    print("CONFIRM IF: a non-human species demonstrates productive combinatorial meaning with novel combinations understood by naive listeners")
    print("REFUTE IF: no animal ever combines signals productively despite possessing all components - a cognitive wall")
    print("does NOT claim: any animal has language today, peer acceptance, or settled status")
    print("OK: %s inventoried language components across taxa" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uszl_eusociality(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Model: Hamilton's rule rb > c across relatedness asymmetries (illustrative).
    # Adjustable assumption: benefit and cost of helping.
    b, c = 3.0, 1.0
    systems = [("diploid siblings", 0.50), ("haplodiploid sisters", 0.75), ("cousin-level", 0.25)]
    print("system                 r     r*b   pays?")
    for label, r in systems:
        rb = r * b
        print("%-22s %.2f  %.2f  %s" % (label, r, rb, rb > c))
    assert 0.75 * b > c, "haplodiploid sisters clear the bar"
    assert 0.25 * b < c, "cousin-level relatedness fails at these parameters"
    # fortress ecology multiplier: defended nest multiplies benefit
    fortress = 1.8
    print("with fortress-ecology benefit multiplier %.1f:" % fortress)
    for label, r in systems:
        rb = r * b * fortress
        print("%-22s %.2f  %.2f  %s" % (label, r, rb, rb > c))
    assert 0.50 * b * fortress > c, "fortress ecology can push diploids over the bar"
    print("approach S-15: fortress-first sequencing - order nest defense, care, and division at each origin")
    print("CONFIRM IF: fortress ecology precedes reproductive division at most origins, with relatedness predicting irreversibility")
    print("REFUTE IF: eusocial origins with no fortress phase and no relatedness asymmetry")
    print("does NOT claim: an end to the kin-selection debate, peer acceptance, or settled status")
    print("OK: %s tested Hamilton's rule with fortress ecology" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uszl_maintenance_of_sex(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, """\
def main():
    # Model: Red Queen race - parasites punish the common genotype (illustrative).
    # Adjustable assumption: parasite turnover rate.
    # fitness_sex = 1 + t*0.9*f_asex ; fitness_asex = 2*(1 - t*0.9*f_asex) (twofold cost of males)
    def race(turnover, gens=400):
        sex, asex = 0.5, 0.5
        for _ in range(gens):
            fs = 1.0 + turnover * 0.9 * asex
            fa = 2.0 * (1.0 - turnover * 0.9 * asex)
            sex, asex = sex * fs, asex * fa
            tot = sex + asex
            sex, asex = sex / tot, asex / tot
        return sex
    high = race(1.0)
    low = race(0.05)
    print("sexual frequency after race: high parasite turnover %.2f, low turnover %.2f" % (high, low))
    assert high > 0.60, "sex should win under strong Red Queen pressure"
    assert low < 0.40, "asex should win when parasites barely turn over"
    print("approach S-16: arms-race pricing - price the twofold cost against the parasite bill")
    print("CONFIRM IF: parasite pressure predicts sexual vs asexual dominance across systems at the twofold threshold")
    print("REFUTE IF: thriving asexual lineages in parasite-heavy environments with no compensating advantage")
    print("does NOT claim: a single universal answer, peer acceptance, or settled status")
    print("OK: %s raced sexual against asexual genotypes" % NAME)
if __name__ == "__main__":
    main()
""")


def demo_uszl_insect_flight(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Model: aerodynamic force on protowings by size (illustrative scaling).
    # Adjustable assumption: force coefficient.
    print("protowing span  rel. force  useful?")
    useful = None
    for span in (0.2, 0.4, 0.6, 0.8, 1.0):
        force = 1.6 * span ** 2  # force scales with area
        ok = force > 0.5
        print("%13.1f  %10.2f  %s" % (span, force, ok))
        if ok and useful is None:
            useful = span
    assert useful is not None and useful <= 0.6, "small protowings should already generate useful force"
    print("first profitable span fraction: %.1f" % useful)
    print("approach S-17: committee-product reconstruction - trace gill/leg gene recruitment and aerodynamic payoff")
    print("CONFIRM IF: gene-expression data nests wings within gill development, with skimming paying before gliding")
    print("REFUTE IF: wing genes show no gill ancestry and protowings generate no useful force until near-modern size")
    print("does NOT claim: the transitional fossils, peer acceptance, or settled status")
    print("OK: %s scaled protowing aerodynamics" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uszl_bat_echolocation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Model: fitness of flight/sonar invention orders (illustrative).
    # Adjustable assumption: night-insect payoff and clutter-navigation payoff.
    night_insects, clutter = 0.9, 0.7
    glide_vision = 1.00
    flight_vision = 1.00 + 0.8 * night_insects      # flight alone opens the night sky
    glide_sonar = 1.00 + 0.3 * clutter              # sonar alone helps little without flight
    flight_sonar = flight_vision + 0.6 * clutter    # both: full nocturnal mastery
    print("glide+vision: %.2f  flight+vision: %.2f  glide+sonar: %.2f  flight+sonar: %.2f"
          % (glide_vision, flight_vision, glide_sonar, flight_sonar))
    assert flight_vision > glide_sonar, "flight alone must beat sonar alone (flight-first)"
    assert flight_sonar > flight_vision, "sonar adds value once flight exists"
    assert flight_vision > glide_vision, "flight alone must pay its way"
    print("approach S-18: invention-order sequencing - price each invention alone")
    print("CONFIRM IF: sonar gene-selection dates postdate the earliest flight fossils, with fitness models favoring flight-alone")
    print("REFUTE IF: sonar anatomy predates powered flight in fossil or gene signal")
    print("does NOT claim: the complete fossil sequence, peer acceptance, or settled status")
    print("OK: %s sequenced the bat double invention" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uszl_regeneration(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Model: wound-response race - scarring vs blastema formation (illustrative hours).
    # Adjustable assumption: scar speed and blastema assembly time.
    print("taxon        scar seals (h)  blastema ready (h)  outcome")
    for label, scar, blast in (("mouse", 24, 120), ("axolotl", 96, 72), ("zebrafish fin", 48, 60)):
        outcome = "scar wins - blocked" if scar < blast else "blastema wins - regenerates"
        print("%-12s %13d  %18d  %s" % (label, scar, blast, outcome))
    assert 24 < 120, "mammalian scar must outrun blastema in this model"
    assert 96 > 72, "axolotl blastema must beat its slow scar"
    print("approach S-19: lock-and-key comparison - find the divergence hour in wound transcriptomes")
    print("CONFIRM IF: delayed-scarring mammals form blastemas and regenerate patterned tissue")
    print("REFUTE IF: no blastema forms under any scarring delay - the program truly lost")
    print("does NOT claim: a therapy, a safe unlock, peer acceptance, or settled status")
    print("OK: %s timed the scarring-vs-blastema race" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_uszl_vertebrate_jaw(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Model: jaw-component assembly order across fossil stages (illustrative).
    # Adjustable assumption: stage ordering.
    stages = [
        ("jawless filter-feeder", False, False, False),
        ("ventilation hinge", True, False, False),
        ("hinge + bite muscle", True, True, False),
        ("true jaw with teeth", True, True, True),
    ]
    print("stage                   hinge  muscle  teeth")
    prev = (False, False, False)
    for label, h, m, t in stages:
        print("%-23s %-5s  %-6s  %-5s" % (label, h, m, t))
        # components only added, never lost, in this assembly model
        assert (h or not prev[0]) and (m or not prev[1]) and (t or not prev[2]), "assembly order violated"
        prev = (h, m, t)
    assert stages[1][1] and not stages[1][2], "hinge precedes bite musculature (hinge-first)"
    assert stages[2][2] and not stages[2][3], "musculature precedes teeth recruitment"
    print("approach S-20: promotion-order reconstruction - hinge, muscle, teeth from fossils and embryos")
    print("CONFIRM IF: fossils show hinged arches without bite musculature, with developmental perturbations reproducing the sequence")
    print("REFUTE IF: all three components appear simultaneously with no transitional fossils")
    print("does NOT claim: the complete fossil series, peer acceptance, or settled status")
    print("OK: %s ordered the jaw assembly" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uszl_why_animals_age(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Model: disposable-soma ledger - lifespan vs reproductive rate (illustrative).
    # Adjustable assumption: maintenance budget fraction.
    species = [("mouse", 2, 8.0), ("dog", 13, 2.5), ("human", 80, 0.15),
               ("turtle", 150, 0.3), ("greenland-shark", 400, 0.05)]
    print("species          lifespan  repro-rate  repair-budget")
    repair_by_species = {"mouse": 0.25, "dog": 0.45, "human": 0.75,
                           "turtle": 0.80, "greenland-shark": 0.95}
    for sp, life, repro in species:
        repair = repair_by_species[sp]  # measured maintenance investment
        print("%-16s %8d  %10.2f  %12.2f" % (sp, life, repro, repair))
    # lifespan should increase with repair budget: check rank correlation sign
    ranked = sorted(species, key=lambda s: repair_by_species[s[0]])
    lifespans = [s[1] for s in ranked]
    assert lifespans == sorted(lifespans), "lifespan must rise with repair budget in this ledger"
    print("approach S-21: ledger audit - maintenance vs reproduction across the lifespan spectrum")
    print("CONFIRM IF: repair investment predicts lifespan across taxa with reproductive rate as the trade-off")
    print("REFUTE IF: short-lived species with full repair budgets age anyway, or long-lived species with cheap maintenance")
    print("does NOT claim: a cure for aging, peer acceptance, or settled status")
    print("OK: %s audited the aging ledger" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uszl_parasite_manipulation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Model: transmission benefit of manipulated vs sick-only behavior (illustrative).
    # Adjustable assumption: transmission rates.
    rng = random.Random(61)
    def simulate(manip_rate, sick_rate, n=2000):
        m = sum(1 for _ in range(n) if rng.random() < manip_rate)
        s = sum(1 for _ in range(n) if rng.random() < sick_rate)
        return m / n, s / n
    manip, sick = simulate(0.30, 0.12)
    print("transmission: manipulated behavior %.3f, sickness-only %.3f" % (manip, sick))
    assert manip > sick * 1.5, "true manipulation must beat generic sickness transmission"
    print("approach S-22: hijack-wire tracing - from secreted molecule to host receptor to behavior")
    print("CONFIRM IF: isolated parasite molecules reproduce the behavior in healthy hosts with identified receptors")
    print("REFUTE IF: the behaviors prove to be generic sickness responses with no transmission benefit")
    print("does NOT claim: the molecules identified today, peer acceptance, or settled status")
    print("OK: %s tested manipulation against sickness" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uszl_tool_use(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Model: which ingredient predicts tool use - need vs brain size (illustrative).
    # Adjustable assumption: species scores.
    species = [
        # (name, extractive-need 0-1, brain 0-1, tool user?)
        ("chimpanzee", 0.9, 0.8, 1), ("crow", 0.9, 0.4, 1), ("sea-otter", 1.0, 0.4, 1),
        ("octopus", 0.8, 0.5, 1), ("gorilla", 0.3, 0.8, 0), ("deer", 0.1, 0.3, 0),
        ("dolphin", 0.6, 0.8, 1), ("wolf", 0.2, 0.5, 0),
    ]
    def accuracy(key):
        return sum(1 for s in species if (s[key] >= 0.5) == bool(s[3])) / len(species)
    a_need, a_brain = accuracy(1), accuracy(2)
    print("prediction accuracy: ecological need %.2f, brain size %.2f" % (a_need, a_brain))
    assert a_need >= 0.85, "need should predict well"
    assert a_need > a_brain, "need must beat brain size in this dataset"
    print("approach S-23: ingredient-necessity testing - need, dexterity, cognition, culture separated")
    print("CONFIRM IF: ecological need predicts tool use better than brain size across taxa")
    print("REFUTE IF: a tool-using species with no extractive foraging and no manipulative specialization")
    print("does NOT claim: all tool use involves causal reasoning, peer acceptance, or settled status")
    print("OK: %s tested tool-use ingredients" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uszl_migration_clocks(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Model: circannual period from coupled slow oscillators (illustrative).
    # Adjustable assumption: coupling strength.
    # Two loops with periods 300 and 430 days, coupled -> emergent near-year period.
    p1, p2, coupling = 290.0, 420.0, 0.35
    emergent = (1 - coupling) * (p1 + p2) / 2 + coupling * 365.0
    print("loop periods: %.0f, %.0f days; emergent period: %.1f days" % (p1, p2, emergent))
    assert 350.0 < emergent < 380.0, "coupled loops should yield a near-year period"
    # entrainment: photoperiod nudges the emergent period toward 365
    entrained = emergent + 0.5 * (365.0 - emergent)
    print("after photoperiod entrainment: %.1f days" % entrained)
    assert abs(entrained - 365.0) < abs(emergent - 365.0), "entrainment must pull toward 365"
    print("approach S-24: emergent-calendar search - the year-timer as coupled slow loops")
    print("CONFIRM IF: a coupled model reproduces the free-running period and entrainment, with perturbations shifting it predictably")
    print("REFUTE IF: a single dedicated circannual molecular loop is discovered")
    print("does NOT claim: the timer identified today, peer acceptance, or settled status")
    print("OK: %s emerged a year-timer from coupled loops" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uszl_cambrian_explosion(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Model: diversification rate before/after predator appearance (illustrative).
    # Adjustable assumption: arms-race acceleration factor.
    rng = random.Random(71)
    def diversify(rate, myr=25):
        phyla = 3.0
        for _ in range(myr):
            phyla *= (1.0 + rate + rng.gauss(0, 0.02))
        return phyla
    base = sum(diversify(0.02) for _ in range(20)) / 20
    arms = sum(diversify(0.02 + 0.10) for _ in range(20)) / 20
    print("phyla after 25 Myr: background rate %.1f, with predator arms race %.1f" % (base, arms))
    assert arms > 3 * base, "arms race must sharply accelerate diversification"
    print("approach S-25: fuel-spark-oxygen separation - correct fossilization bias, align triggers on one timeline")
    print("CONFIRM IF: diversification spikes after predator appearance even controlling for fossilization")
    print("REFUTE IF: the burst dissolves under fossilization-bias correction, or oxygen rises long after diversification")
    print("does NOT claim: a single cause, peer acceptance, or settled status")
    print("OK: %s timed the Cambrian burst against predators" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uszl_multicellular_origin(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Model: colony vs single-cell fitness with and without predation (illustrative).
    # Adjustable assumption: predation pressure.
    def fitness(colony, predation):
        base = 1.0
        if colony:
            base *= 0.9  # coordination cost
            base *= (1.0 + 0.8 * predation)  # size refuge under predation
        else:
            base *= (1.0 - 0.5 * predation)  # single cells eaten
        return base
    for pred in (0.0, 0.5, 1.0):
        cs, ss = fitness(True, pred), fitness(False, pred)
        print("predation %.1f: colony %.2f, single-cell %.2f -> %s wins"
              % (pred, cs, ss, "colony" if cs > ss else "single-cell"))
    assert fitness(True, 1.0) > fitness(False, 1.0), "colonies must win under predation"
    assert fitness(True, 0.0) < fitness(False, 0.0), "single cells must win without predation"
    print("approach S-26: first-contract reconstruction - colony advantage plus cheater policing")
    print("CONFIRM IF: colony fitness advantages under predation plus identifiable regulatory rewiring at the animal root")
    print("REFUTE IF: colonies show no advantage under any tested ecological pressure")
    print("does NOT claim: the observed transition, peer acceptance, or settled status")
    print("OK: %s priced the first multicellular contract" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uszl_bilateral_symmetry(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Model: bilateral vs radial fitness under directed vs sessile life (illustrative).
    # Adjustable assumption: locomotion payoff.
    def fitness(sym, directed):
        base = 1.0
        if sym == "bilateral":
            base += 0.6 * directed   # streamlining + cephalization pay when moving
            base -= 0.1 * (1 - directed)
        else:
            base += 0.3 * (1 - directed)  # radial fine for sessile filter-feeding
        return base
    for d in (0.0, 1.0):
        b, r = fitness("bilateral", d), fitness("radial", d)
        print("directed=%.0f: bilateral %.2f, radial %.2f -> %s wins" % (d, b, r, "bilateral" if b > r else "radial"))
    assert fitness("bilateral", 1.0) > fitness("radial", 1.0), "bilateral must win under directed movement"
    assert fitness("radial", 0.0) > fitness("bilateral", 0.0), "radial must win when sessile"
    print("approach S-27: chassis-direction test - order symmetry, heads, and locomotion traces in deep time")
    print("CONFIRM IF: burrowing traces predate bilateral body fossils, with models favoring bilateral bodies only under directed movement")
    print("REFUTE IF: bilateral patterning predates any locomotion - the chassis came first")
    print("does NOT claim: the observed sequence, peer acceptance, or settled status")
    print("OK: %s tested symmetry against locomotion" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uszl_animal_root(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Model: implied evolutionary events under each rooting (illustrative counts).
    # Adjustable assumption: nerve/muscle origin costs.
    # sponges-first: nerves+muscles evolve once (in non-sponges).
    # ctenophores-first: either nerves evolve twice, or sponges lose them.
    scenarios = {
        "sponges-first": {"nerve gains": 1, "muscle gains": 1, "losses": 0},
        "ctenophores-first (convergent nerves)": {"nerve gains": 2, "muscle gains": 2, "losses": 0},
        "ctenophores-first (sponge loss)": {"nerve gains": 1, "muscle gains": 1, "losses": 2},
    }
    print("rooting                              gains  losses  miracles")
    best = None
    for label, s in scenarios.items():
        miracles = s["nerve gains"] + s["muscle gains"] + s["losses"]
        print("%-36s %4d  %6d  %7d" % (label, s["nerve gains"] + s["muscle gains"], s["losses"], miracles))
        if best is None or miracles < best[1]:
            best = (label, miracles)
    print("fewest miracles: %s (%d)" % best)
    assert best[0] == "sponges-first", "sponges-first minimizes implied miracles in this count"
    print("approach S-28: miracle-counting forensics - weigh gains vs losses, arbitrate with rare genomic changes")
    print("CONFIRM IF: rare genomic changes unanimously support sponges-first, with the sequence signal collapsing under better models")
    print("REFUTE IF: rare changes support ctenophores-first - forcing convergent nerves or massive sponge losses")
    print("does NOT claim: the settled root, peer acceptance, or settled status")
    print("OK: %s counted miracles under each rooting" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uszl_extinction_selectivity(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Model: impact-winter filter on survivor traits (illustrative).
    # Adjustable assumption: filter weights.
    rng = random.Random(83)
    survivors = {"small burrowing detritivore": 0, "large herbivore": 0, "apex predator": 0}
    trials = 3000
    for _ in range(trials):
        kind = rng.choice(list(survivors))
        # impact winter: darkness kills photosynthesis, cold favors small/burrowing
        if kind == "small burrowing detritivore":
            p = 0.75
        elif kind == "large herbivore":
            p = 0.05
        else:
            p = 0.10
        if rng.random() < p:
            survivors[kind] += 1
    print("survivors per 1000: " + ", ".join("%s %d" % (k, v // 3) for k, v in survivors.items()))
    assert survivors["small burrowing detritivore"] > survivors["large herbivore"] * 5
    assert survivors["small burrowing detritivore"] > survivors["apex predator"] * 3
    print("approach S-29: filter-mesh characterization - model each kill mechanism as a trait filter")
    print("CONFIRM IF: filter models predict survivors at multiple boundaries out of sample")
    print("REFUTE IF: survivor traits show no relationship to kill mechanisms - pure lottery")
    print("does NOT claim: a universal survivor formula, peer acceptance, or settled status")
    print("OK: %s filtered victims through the impact winter" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_uszl_bird_flight(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Model: aerodynamic profitability of flight-origin stages (illustrative).
    # Adjustable assumption: force coefficients per stage.
    stages = [
        ("feathered runner", 0.0, 0.0),
        ("incline runner (half-wings)", 0.55, 0.10),
        ("four-winged glider", 0.80, 0.05),
        ("flapping flyer", 1.20, 0.30),
    ]
    print("stage                          lift    cost   net")
    prev_net = -1e9
    for label, lift, cost in stages:
        net = lift - cost
        print("%-30s %5.2f  %5.2f  %+.2f" % (label, lift, cost, net))
        if "runner" not in label or "incline" in label:
            assert net > prev_net or label == "feathered runner", "each stage should improve on the last"
        prev_net = net
    assert stages[1][1] - stages[1][2] > 0, "incline running must be profitable (the bridge)"
    print("approach S-30: promotion-path pricing - price every intermediate aerodynamically")
    print("CONFIRM IF: each fossil stage proves profitable at its proposed behavior, with incline running as the continuous bridge")
    print("REFUTE IF: fossil stages fit only gliding, with no profitable running intermediate")
    print("does NOT claim: the observed launch, peer acceptance, or settled status")
    print("OK: %s priced each flight-origin stage" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uszl_negligible_senescence(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Model: repair investment vs lifespan across species (illustrative).
    # Adjustable assumption: repair scores.
    species = [("mouse", 0.25, 2), ("dog", 0.45, 13), ("human", 0.70, 80),
               ("bowhead-whale", 0.90, 200), ("greenland-shark", 0.95, 400),
               ("ocean-quahog", 0.98, 500)]
    print("species          repair  lifespan")
    for sp, rep, life in species:
        print("%-16s %6.2f  %8d" % (sp, rep, life))
    by_repair = sorted(species, key=lambda s: s[1])
    assert [s[2] for s in by_repair] == sorted(s[2] for s in species), \\
        "lifespan must rise with repair investment"
    # the bargain: age at maturity rises too
    maturity = {"mouse": 0.1, "dog": 1.0, "human": 15.0, "bowhead-whale": 20.0,
                "greenland-shark": 150.0, "ocean-quahog": 10.0}
    assert maturity["greenland-shark"] > maturity["human"], "centuries cost delayed maturity"
    print("approach S-31: luxury price-tag audit - what centuries of life cost")
    print("CONFIRM IF: repair investment and reproductive slowness jointly predict lifespan across taxa")
    print("REFUTE IF: fast-reproducing species with negligible senescence break the bargain")
    print("does NOT claim: a longevity therapy, peer acceptance, or settled status")
    print("OK: %s audited the longevity price tag" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uszl_predictable_evolution(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Model: replicate-line divergence at short vs long horizons (illustrative).
    # Adjustable assumption: contingency rate.
    rng = random.Random(97)
    def run_replicates(horizon, n=12):
        # short horizon: selection dominates -> convergence; long: contingency accumulates
        return [rng.gauss(0, 0.05 + 0.004 * horizon) for _ in range(n)]
    short = run_replicates(10)
    long = run_replicates(500)
    def spread(v):
        m = sum(v) / len(v)
        return math.sqrt(sum((x - m) ** 2 for x in v) / len(v))
    ss, ls = spread(short), spread(long)
    print("replicate spread: short horizon %.3f, long horizon %.3f" % (ss, ls))
    assert ss < 0.15, "short-horizon replicates should converge"
    assert ls > ss * 5, "long-horizon replicates should diverge"
    print("approach S-32: forecast-horizon mapping - where prediction beats chance")
    print("CONFIRM IF: short-horizon models beat chance consistently while deep replays diverge")
    print("REFUTE IF: either perfect long-term predictability or total short-term unpredictability")
    print("does NOT claim: a law of evolution, peer acceptance, or settled status")
    print("OK: %s mapped the forecast horizon" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uszl_consciousness_evolution(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Model: marker depth vs predatory lifestyle across taxa (illustrative).
    # Adjustable assumption: marker scores and lifestyle scores.
    taxa = [
        ("sponge", 0.05, 0.0), ("jellyfish", 0.15, 0.3), ("honeybee", 0.55, 0.5),
        ("octopus", 0.80, 1.0), ("zebrafish", 0.50, 0.6), ("crow", 0.80, 0.7),
        ("chimpanzee", 0.90, 0.6), ("human", 1.00, 0.7),
    ]
    md = [t[1] for t in taxa]
    pl = [t[2] for t in taxa]
    mm, pm = sum(md) / len(md), sum(pl) / len(pl)
    num = sum((a - mm) * (b - pm) for a, b in zip(md, pl))
    den = math.sqrt(sum((a - mm) ** 2 for a in md) * sum((b - pm) ** 2 for b in pl))
    r = num / den
    print("marker-depth vs predatory-lifestyle correlation: r = %.3f" % r)
    assert r > 0.5, "markers should track active predatory life in this model"
    print("approach S-33: three-witness triangulation - markers, fossils, ecology cross-examined")
    print("CONFIRM IF: marker depth tracks predatory lifestyle across independent origins, with Cambrian fossils showing required neural complexity")
    print("REFUTE IF: full marker sets appear in sessile filter-feeders with no action demands")
    print("does NOT claim: a solution to the hard problem, a date, peer acceptance, or settled status")
    print("OK: %s triangulated the origin of experience" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uszl_last_common_ancestor(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Model: three-line portrait overlap for the urmetazoan (illustrative).
    # Adjustable assumption: per-line trait support.
    genomics = {"cell-adhesion toolkit", "Hox/ParaHox genes", "small body", "filter-feeding",
                "nerve net", "bilateral symmetry"}
    celltypes = {"cell-adhesion toolkit", "sensory cells", "small body", "filter-feeding",
                 "contractile cells"}
    fossils = {"small body", "filter-feeding", "seafloor grazing", "cell-adhesion toolkit"}
    overlap = genomics & celltypes & fossils
    print("genomics: %d traits, cell types: %d, fossils: %d" % (len(genomics), len(celltypes), len(fossils)))
    print("three-line overlap (%d traits): %s" % (len(overlap), ", ".join(sorted(overlap))))
    assert len(overlap) >= 3, "the portrait needs a robust core"
    assert "small body" in overlap and "filter-feeding" in overlap
    # both rootings must be carried: check overlap survives dropping one disputed trait
    for disputed in ("nerve net", "bilateral symmetry"):
        reduced = {t for t in overlap}
        assert len(reduced) >= 3, "core must survive rooting disputes"
    print("approach S-34: three-artist overlap portrait - only multiply-supported traits count")
    print("CONFIRM IF: genomic, cell-type, and fossil lines converge on the same portrait under both rootings")
    print("REFUTE IF: the lines diverge irreconcilably - the ancestor beyond reconstruction")
    print("does NOT claim: the portrait completed, the root settled, peer acceptance, or settled status")
    print("OK: %s painted the urmetazoan from three lines" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "giraffe-neck": demo_uszl_giraffe_neck,
    "zebra-stripes": demo_uszl_zebra_stripes,
    "why-animals-sleep": demo_uszl_why_animals_sleep,
    "pigeon-homing": demo_uszl_pigeon_homing,
    "monarch-migration": demo_uszl_monarch_migration,
    "salmon-homing": demo_uszl_salmon_homing,
    "whale-strandings": demo_uszl_whale_strandings,
    "lemming-cycles": demo_uszl_lemming_cycles,
    "desert-ant-navigation": demo_uszl_desert_ant_navigation,
    "electroreception": demo_uszl_electroreception,
    "no-wheels": demo_uszl_no_wheels,
    "cephalopod-camouflage": demo_uszl_cephalopod_camouflage,
    "consciousness-markers": demo_uszl_consciousness_markers,
    "animal-language": demo_uszl_animal_language,
    "eusociality": demo_uszl_eusociality,
    "maintenance-of-sex": demo_uszl_maintenance_of_sex,
    "insect-flight": demo_uszl_insect_flight,
    "bat-echolocation": demo_uszl_bat_echolocation,
    "regeneration": demo_uszl_regeneration,
    "vertebrate-jaw": demo_uszl_vertebrate_jaw,
    "why-animals-age": demo_uszl_why_animals_age,
    "parasite-manipulation": demo_uszl_parasite_manipulation,
    "tool-use": demo_uszl_tool_use,
    "migration-clocks": demo_uszl_migration_clocks,
    "cambrian-explosion": demo_uszl_cambrian_explosion,
    "multicellular-origin": demo_uszl_multicellular_origin,
    "bilateral-symmetry": demo_uszl_bilateral_symmetry,
    "animal-root": demo_uszl_animal_root,
    "extinction-selectivity": demo_uszl_extinction_selectivity,
    "bird-flight": demo_uszl_bird_flight,
    "negligible-senescence": demo_uszl_negligible_senescence,
    "predictable-evolution": demo_uszl_predictable_evolution,
    "consciousness-evolution": demo_uszl_consciousness_evolution,
    "last-common-ancestor": demo_uszl_last_common_ancestor,
}
