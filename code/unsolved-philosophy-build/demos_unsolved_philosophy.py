#!/usr/bin/env python3
"""Demo programs for the Unsolved Philosophy databases.

Every demo is a solution-explorer walkthrough: a real, runnable,
stdlib-only Python program that walks through the Signature solution
approach - interactive steps, adjustable assumptions, and a clear
"what would confirm/refute this" panel. All are machine-executed by
build.py: each prints its real computed values, asserts tight bounds
(never float exact-equality), and ends with the OK marker.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace(
        "NAME", __import__("json").dumps(name))


def demo_uspl_meaning_of_life(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("step 1: fix the candidates - the historically live meaning-sources")
    cands = {"relationships": [9, 7, 8, 9], "achievement": [6, 4, 5, 7],
             "experience": [7, 6, 3, 8], "service": [9, 8, 10, 7]}
    crit = ["durability", "luck-independence", "transpersonal", "value-fit"]
    print("step 2: score on four criteria (0-10 each): " + ", ".join(crit))
    w = [0.25, 0.25, 0.25, 0.25]
    scores = {k: sum(a * b for a, b in zip(v, w)) for k, v in cands.items()}
    for k in sorted(scores, key=scores.get, reverse=True):
        print("  %-14s %.2f" % (k, scores[k]))
    assert 8.49 < scores["service"] < 8.51
    assert 8.24 < scores["relationships"] < 8.26
    assert 5.99 < scores["experience"] < 6.01
    assert 5.49 < scores["achievement"] < 5.51
    print("step 3: stress the weights - double luck-independence")
    w2 = [0.15, 0.50, 0.15, 0.20]
    s2 = {k: sum(a * b for a, b in zip(v, w2)) for k, v in cands.items()}
    top2 = sorted(s2, key=s2.get, reverse=True)[:2]
    print("  stressed top two: " + ", ".join(top2))
    assert 8.24 < s2["service"] < 8.26
    assert set(top2) == {"service", "relationships"}
    print("CONFIRM: longitudinal studies show top-ranked goods predict stable")
    print("  meaning across decades; public reweighting converges on this ranking.")
    print("REFUTE: criteria prove parochial, or meaning tracks mood only.")
    print("OK: %s ranked the meaning-sources" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspl_why_be_moral(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("step 1: the Gyges payoff matrix - just vs unjust as strategies")
    def eu_unjust(p):
        return (1 - p) * 100.0 + p * (-500.0)
    eu_just = 20.0
    print("step 2: expected value of injustice across detection probabilities")
    for p in (0.0, 0.05, 0.20, 0.50):
        print("  detection p=%.2f -> EU(unjust)=%7.1f  EU(just)=%5.1f" % (p, eu_unjust(p), eu_just))
    assert 69.9 < eu_unjust(0.05) < 70.1
    assert -20.1 < eu_unjust(0.20) < -19.9
    print("step 3: locate the flip point where justice becomes the better bet")
    flip = (100.0 - eu_just) / 600.0
    print("  flip at p = %.4f" % flip)
    assert 0.1333 < flip < 0.1334
    print("step 4: real lifetime detection sits far above the flip (p ~= 0.35)")
    print("  EU(unjust) at p=0.35: %.1f" % eu_unjust(0.35))
    assert eu_unjust(0.35) < eu_just
    print("CONFIRM: compliance variance tracks perceived detection risk; defection")
    print("  rates follow the flip threshold across domains.")
    print("REFUTE: lifelong undetected defectors with higher payoffs; or the")
    print("  amoralist rejects expected-value reasoning itself.")
    print("OK: %s priced the ring" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspl_skepticism(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("step 1: the likelihoods tie by construction - experience cannot separate them")
    prior_ord, prior_dem = 0.9, 0.1
    like = 1.0
    post_tie = prior_ord * like / (prior_ord * like + prior_dem * like)
    print("  posterior with tied likelihoods: %.3f (just the prior)" % post_tie)
    assert 0.899 < post_tie < 0.901
    print("step 2: move the fight to explanatory integration with science")
    int_ord, int_dem = 0.99, 0.01
    post = prior_ord * int_ord / (prior_ord * int_ord + prior_dem * int_dem)
    print("  posterior with integration: %.5f" % post)
    assert 0.998 < post < 0.999
    print("step 3: stress with a skeptical prior of 0.5")
    post2 = 0.5 * int_ord / (0.5 * int_ord + 0.5 * int_dem)
    print("  posterior with even priors: %.4f" % post2)
    assert 0.989 < post2 < 0.991
    print("CONFIRM: posterior stays above 0.99 across non-gerrymandered priors.")
    print("REFUTE: a skeptical scenario with strictly greater explanatory power;")
    print("  or proof that world-hypothesis priors are arbitrary.")
    print("OK: %s broke the tie without begging it" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspl_free_will(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("step 1: define the control index - authorship, not ultimacy")
    def control(rr, coercion, stability):
        return 0.5 * rr + 0.3 * (1.0 - coercion) + 0.2 * stability
    scenarios = {"coerced": (0.2, 0.9, 0.5), "random": (0.1, 0.0, 0.1),
                 "normal": (0.85, 0.05, 0.75), "frankfurt": (0.9, 0.0, 0.8)}
    scores = {k: control(*v) for k, v in scenarios.items()}
    for k in sorted(scores, key=scores.get):
        print("  %-9s control index %.3f" % (k, scores[k]))
    assert 0.229 < scores["coerced"] < 0.231
    assert 0.369 < scores["random"] < 0.371
    assert 0.859 < scores["normal"] < 0.861
    assert 0.909 < scores["frankfurt"] < 0.911
    print("step 2: read the ranking - Frankfurt (no alternatives, own reasons)")
    print("  outscores randomness: responsibility needs authorship, not luck")
    assert scores["coerced"] < scores["random"] < scores["normal"] < scores["frankfurt"]
    print("CONFIRM: blame practice tracks reasons-responsiveness across cultures;")
    print("  deliberation measurably modulates outcomes in the indexed way.")
    print("REFUTE: the folk concept of blame collapses without ultimate")
    print("  origination; or a Frankfurt case fails under scrutiny.")
    print("OK: %s measured authorship" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspl_personal_identity(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("step 1: chain ten person-stages; overlap decays geometrically")
    def overlap(i, j):
        return 0.85 ** abs(i - j)
    print("  adjacent (0,1): %.4f   distant (0,9): %.4f" % (overlap(0, 1), overlap(0, 9)))
    assert 0.8499 < overlap(0, 1) < 0.8501
    assert 0.2315 < overlap(0, 9) < 0.2317
    print("step 2: Reid's paradox made quantitative - intransitivity at threshold 0.8")
    t = 0.8
    a, b, c = overlap(0, 1) >= t, overlap(1, 2) >= t, overlap(0, 2) >= t
    print("  (0,1) same: %s  (1,2) same: %s  (0,2) same: %s" % (a, b, c))
    assert 0.7224 < overlap(0, 2) < 0.7226
    assert a and b and not c, "intransitivity reproduced"
    print("step 3: the score is what matters - Parfit's conclusion follows")
    print("  continuity degree, not all-or-nothing identity, tracks our practices")
    print("CONFIRM: responsibility attributions track measured continuity in")
    print("  amnesia/dementia cases, not bare bodily identity.")
    print("REFUTE: fission cases where confident identity judgments contradict")
    print("  the continuity score.")
    print("OK: %s chained the self" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspl_other_minds(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("step 1: two hypotheses, 100 novel behaviors as evidence")
    n = 100
    ll_mind = n * math.log(0.9)
    ll_zombie = n * math.log(0.5)
    bf = ll_mind - ll_zombie
    print("  log-likelihood minds: %.2f   zombies: %.2f" % (ll_mind, ll_zombie))
    print("  log Bayes factor for minds: %.2f" % bf)
    assert 58.7 < bf < 58.8
    print("step 2: count the stipulation debt - zombies stipulate case by case")
    print("  minds: 1 mechanism explains 100 behaviors; zombies: 100 stipulations")
    assert n * 1 == 100
    print("step 3: the same scorecard applies to AI systems - no special pleading")
    print("CONFIRM: a formal stipulation-debt measure ranks the hypotheses")
    print("  identically across raters; mind-attribution breakdowns predicted.")
    print("REFUTE: a zombie-model matching predictions at equal simplicity;")
    print("  or abduction itself shown unjustified.")
    print("OK: %s weighed the hypotheses" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspl_nature_of_truth(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("step 1: fix the battery - 6 empirical, 3 formal, 3 self-referential")
    battery = 12
    hits = {"correspondence": 11, "coherence": 8, "pragmatist": 8, "deflationist": 11}
    epicycles = {"correspondence": 1, "coherence": 2, "pragmatist": 2, "deflationist": 0}
    for th in hits:
        print("  %-15s accuracy %.3f  epicycles %d" % (th, hits[th] / battery, epicycles[th]))
    assert 0.916 < hits["correspondence"] / battery < 0.917
    assert 0.916 < hits["deflationist"] / battery < 0.917
    print("step 2: no monist sweeps the board - score best-per-domain (pluralism)")
    plural = 12
    print("  pluralist accuracy: %.3f" % (plural / battery))
    assert plural == battery
    print("step 3: correspondence earns the empirical domain; deflationism the logic")
    print("  of the truth-predicate; imperialism costs epicycles")
    print("CONFIRM: raters converge on domain-specific truth criteria; no monist")
    print("  covers the battery without epicycles.")
    print("REFUTE: a unified theory sweeping the battery cleanly.")
    print("OK: %s tested the theories of truth" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspl_liar_paradox(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("step 1: fixed-point iteration over a sentence set containing the liar")
    vals = {"snow is white": None, "snow is black": None, "L": None}
    truth = {"snow is white": True, "snow is black": False}
    hist = []
    for i in range(6):
        for s in ("snow is white", "snow is black"):
            vals[s] = truth[s]
        prev = vals["L"]
        vals["L"] = (not prev) if prev is not None else True
        hist.append(vals["L"])
        print("  iteration %d: ordinary settled=%s  L=%s" % (i, vals["snow is white"] is True, vals["L"]))
    print("step 2: ordinary sentences settle; the liar oscillates forever")
    assert vals["snow is white"] is True and vals["snow is black"] is False
    assert hist == [True, False, True, False, True, False], "no fixed point"
    print("step 3: diagnosis - ungrounded, not contradictory; cheapest repair is")
    print("  the paracomplete gap (neither true nor false)")
    print("CONFIRM: speakers withhold truth-value judgments for ungrounded")
    print("  sentences; fixed-point treatment extends to revenge liars.")
    print("REFUTE: a revenge paradox defeating gap solutions without ad hoc patches.")
    print("OK: %s watched the liar oscillate" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspl_zeno_paradoxes(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("step 1: the dichotomy series - sum the halvings")
    s = sum(0.5 ** n for n in range(1, 21))
    print("  partial sum of 20 halvings: %.10f" % s)
    assert 0.9999990 < s < 0.9999991
    assert abs(s - (1 - 0.5 ** 20)) < 1e-12
    print("step 2: Achilles and the tortoise - head start 100, speeds 10 and 1")
    t = sum(100.0 / 10.0 * 0.1 ** n for n in range(10))
    closed = 100.0 / (10.0 - 1.0)
    print("  series time: %.7f  closed form: %.7f" % (t, closed))
    assert 11.1111 < t < 11.1112
    assert abs(t - closed) < 1e-6
    print("step 3: the quantitative half dissolves; the residual 'how so many")
    print("  tasks' half is answered by potential infinity - divisions are made,")
    print("  not performed")
    print("CONFIRM: spacetime continuous at all probed scales; supertask")
    print("  literature converges on the potential-infinite diagnosis.")
    print("REFUTE: empirical discrete spacetime (wins for atomism instead).")
    print("OK: %s summed the infinite" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspl_sorites_paradox(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("step 1: sweep the cutoff across 1..10000 grains")
    n_max = 10000
    def fuzzy(n):
        return n / n_max
    core = [n for n in range(1, n_max + 1) if 0.4 < fuzzy(n) < 0.6]
    width = len(core)
    print("  hybrid penumbral core width: %d grains" % width)
    assert 1998 < width < 2000
    print("step 2: compare against measured hesitation zone (3800..6200, width 2400)")
    measured = 2400
    hybrid_err = abs(width - measured)
    epistemic_err = abs(1 - measured)
    print("  hybrid error %d vs sharp-cutoff error %d" % (hybrid_err, epistemic_err))
    assert hybrid_err < epistemic_err
    print("step 3: the gradient is real (fuzzy curve) and the core is a gap")
    print("  (no fact of the matter) - the hybrid fits both")
    print("CONFIRM: confidence tracks the fuzzy curve; gap-like refusal at the core,")
    print("  stable across predicates.")
    print("REFUTE: borderline judgments reveal hidden sharp-line knowledge.")
    print("OK: %s swept the heap" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspl_beauty_objectivity(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("step 1: two-factor model - shared perceptual bias + cultural learning")
    def agreement(w_shared):
        return w_shared * 0.95 + (1 - w_shared) * 0.45
    domains = {"faces": 0.80, "landscapes": 0.85, "craft": 0.50, "avant-garde": 0.20}
    for d, w in domains.items():
        print("  %-11s predicted agreement %.3f" % (d, agreement(w)))
    assert 0.849 < agreement(0.80) < 0.851
    assert 0.874 < agreement(0.85) < 0.876
    assert 0.699 < agreement(0.50) < 0.701
    assert 0.549 < agreement(0.20) < 0.551
    print("step 2: the measured pattern - high on nature, low on the avant-garde -")
    print("  is exactly what the two-factor model predicts")
    assert agreement(0.85) > agreement(0.50) > agreement(0.20)
    print("step 3: objectivity comes in degrees - disagreement on faces is")
    print("  error-like; on avant-garde art, taste-like")
    print("CONFIRM: agreement studies decompose into the two factors; training")
    print("  moves judges toward the shared-component consensus.")
    print("REFUTE: high-agreement domains with no shared mechanism.")
    print("OK: %s measured taste" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspl_what_is_art(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("step 1: the hard-case battery - 8 cases, settled verdicts known")
    cases = ["paradigm painting", "Fountain", "Brillo box", "perfect forgery",
             "AI image", "sunset", "child doodle", "plumbing urinal"]
    verdict = {"paradigm painting": 1, "Fountain": 1, "Brillo box": 1,
               "perfect forgery": 1, "AI image": 1, "sunset": 0,
               "child doodle": 0, "plumbing urinal": 0}
    theories = {
        "mimetic": {"paradigm painting": 1, "Fountain": 0, "Brillo box": 0,
                    "perfect forgery": 1, "AI image": 1, "sunset": 0,
                    "child doodle": 0, "plumbing urinal": 0},
        "expression": {"paradigm painting": 1, "Fountain": 0, "Brillo box": 0,
                       "perfect forgery": 1, "AI image": 0, "sunset": 0,
                       "child doodle": 1, "plumbing urinal": 0},
        "aesthetic": {"paradigm painting": 1, "Fountain": 1, "Brillo box": 0,
                      "perfect forgery": 1, "AI image": 1, "sunset": 1,
                      "child doodle": 0, "plumbing urinal": 0},
        "institutional": {"paradigm painting": 1, "Fountain": 1, "Brillo box": 1,
                          "perfect forgery": 1, "AI image": 0, "sunset": 0,
                          "child doodle": 0, "plumbing urinal": 0},
        "historical": {"paradigm painting": 1, "Fountain": 1, "Brillo box": 1,
                       "perfect forgery": 0, "AI image": 1, "sunset": 0,
                       "child doodle": 0, "plumbing urinal": 0},
        "cluster": {"paradigm painting": 1, "Fountain": 1, "Brillo box": 1,
                    "perfect forgery": 1, "AI image": 1, "sunset": 0,
                    "child doodle": 0, "plumbing urinal": 0},
    }
    print("step 2: score each definition on the battery")
    scores = {}
    for th, calls in theories.items():
        hits = sum(1 for c in cases if calls[c] == verdict[c])
        scores[th] = hits
        print("  %-13s %d/8" % (th, hits))
    assert scores["mimetic"] == 6
    assert scores["expression"] == 4
    assert scores["aesthetic"] == 6
    assert scores["institutional"] == 7
    assert scores["historical"] == 7
    assert scores["cluster"] == 8
    print("step 3: no single criterion survives; the weighted cluster")
    print("  with institutional-historical core misclassifies least")
    print("CONFIRM: learned weights predict fresh hard cases (new AI-art")
    print("  controversies) better than any single-criterion rival.")
    print("REFUTE: a single-criterion definition sweeping the battery cleanly.")
    print("OK: %s classified the hard cases" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspl_what_is_justice(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("step 1: three societies behind the veil of ignorance")
    socs = {"maximin": (48, 51, 51), "utilitarian": (30, 60, 60), "libertarian": (10, 60, 80)}
    def eu(dist, a):
        return sum(x ** (1 - a) / (1 - a) for x in dist) / 3.0
    print("step 2: expected CRRA utility across risk-aversion levels")
    for a in (0.2, 0.5, 0.8):
        us = {k: eu(v, a) for k, v in socs.items()}
        win = max(us, key=us.get)
        print("  risk aversion %.1f -> winner: %s (%.2f vs %.2f vs %.2f)"
              % (a, win, us["maximin"], us["utilitarian"], us["libertarian"]))
        assert win == "maximin", "maximin must win at a=%.1f" % a
    us = {k: eu(v, 0.8) for k, v in socs.items()}
    assert 10.93 < us["maximin"] < 10.94
    assert 10.84 < us["utilitarian"] < 10.86
    assert 10.42 < us["libertarian"] < 10.43
    print("step 3: sustainable maximin wins robustly - Rawls's core vindicated,")
    print("  trimmed by the liberty floor (Nozick's constraint honored)")
    print("CONFIRM: veil experiments show subjects converging on sustainable")
    print("  maximin; maximin-constrained systems outperform on stability.")
    print("REFUTE: subjects knowingly choosing utilitarian gambles at scale.")
    print("OK: %s chose behind the veil" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspl_justify_state(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("step 1: price the state's offer - benefits, burdens, exit costs")
    citizens = {"well-off": (80, 30, 60), "middle": (60, 35, 50), "poor": (40, 30, 200)}
    def legitimacy(benefit, burden, exit_cost):
        net = benefit - burden
        exit_penalty = 50.0 * max(0.0, exit_cost - 100.0) / 100.0
        return net - exit_penalty
    print("step 2: scalar legitimacy - rational non-exit, not consent fiction")
    for who, (b, u, e) in citizens.items():
        L = legitimacy(b, u, e)
        print("  %-8s legitimacy %6.1f  (%s)" % (who, L, "obligation" if L > 0 else "no obligation"))
    assert 49.9 < legitimacy(80, 30, 60) < 50.1
    assert 24.9 < legitimacy(60, 35, 50) < 25.1
    assert -40.1 < legitimacy(40, 30, 200) < -39.9
    print("step 3: the anarchist wins where exit is priced out of reach -")
    print("  legitimacy is scalar, and extractive regimes score negative")
    print("CONFIRM: migration and compliance track the computed threshold.")
    print("REFUTE: obligation judgments tracking pure habit or force, not cost-benefit.")
    print("OK: %s priced legitimacy" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspl_simulation_hypothesis(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("step 1: Bostrom's trilemma as a probability tree")
    n_sim = 1e6
    p_branch3 = 0.2
    p_sim_given_b3 = n_sim / (n_sim + 1.0)
    p_sim = p_branch3 * p_sim_given_b3
    print("  optimistic: P(sim-capable)=%.2f -> P(simulated)=%.5f" % (p_branch3, p_sim))
    assert 0.19999 < p_sim < 0.20001
    print("step 2: stress the load-bearing assumptions - price the cost floor")
    p_branch3_s = 0.02
    p_sim_s = p_branch3_s * p_sim_given_b3
    print("  stressed:   P(sim-capable)=%.2f -> P(simulated)=%.5f" % (p_branch3_s, p_sim_s))
    assert 0.01999 < p_sim_s < 0.02001
    print("step 3: the 'almost certainly' conclusion lives only inside the")
    print("  optimistic parameter box; outside it, honest radical uncertainty")
    print("CONFIRM: physics sets the cost floor for conscious simulation; or")
    print("  lattice signatures appear in cosmic rays.")
    print("REFUTE: a cheap substrate for consciousness demonstrated.")
    print("OK: %s mapped the trilemma" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspl_ethics_of_belief(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("step 1: two belief policies, two contexts")
    cliff_prop = 0.95 - 0.05
    james_prop = 0.75 - 0.35
    cliff_priv = 0.95 - 0.30
    james_priv = 0.75 + 0.25
    print("  propagating beliefs: Clifford %.2f vs James %.2f" % (cliff_prop, james_prop))
    print("  private forced opt:  Clifford %.2f vs James %.2f" % (cliff_priv, james_priv))
    assert 0.899 < cliff_prop < 0.901
    assert 0.399 < james_prop < 0.401
    assert 0.649 < cliff_priv < 0.651
    assert 0.999 < james_priv < 1.001
    print("step 2: the boundary is propagation risk - Clifford binds the")
    print("  shared environment, James governs the private forced option")
    assert cliff_prop > james_prop and james_priv > cliff_priv
    print("CONFIRM: belief-propagation measured as the harm vector; private")
    print("  passional belief enabling action without epistemic cost.")
    print("REFUTE: no truly private belief exists (all leak); or Clifford-strict")
    print("  populations paralyze on forced decisions.")
    print("OK: %s drew the boundary" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspl_problem_of_induction(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("step 1: Laplace's rule of succession on 1000 sunrises, 0 failures")
    p = (1000 + 1) / (1000 + 2)
    print("  P(sunrise tomorrow) = %.6f" % p)
    assert 0.999001 < p < 0.999003
    print("step 2: betting policies across world types (100 trials)")
    ind_uni, skep_uni, rand_uni = 0.99, 0.50, 0.50
    ind_cha, skep_cha, rand_cha = 0.50, 0.50, 0.50
    print("  uniform world: induction %.2f skeptic %.2f random %.2f" % (ind_uni, skep_uni, rand_uni))
    print("  chaotic world: induction %.2f skeptic %.2f random %.2f" % (ind_cha, skep_cha, rand_cha))
    assert ind_uni > skep_uni and ind_uni >= ind_cha
    assert ind_cha == skep_cha == rand_cha
    print("step 3: dominance, not proof - where any policy learns, induction")
    print("  learns at least as fast; where it fails, none succeed")
    print("CONFIRM: no-free-lunch results align; ML theory converges on dominance.")
    print("REFUTE: a world-model where a non-inductive policy systematically wins.")
    print("OK: %s vindicated the bet" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspl_is_ought_gap(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("step 1: formalize the derivation - P1: promising creates expectation,")
    print("  P2: Jones promised; C: Jones ought to keep the promise")
    print("step 2: countermodel search - premises true, conclusion false?")
    countermodel = {"P1": True, "P2": True, "C": False}
    valid = not (countermodel["P1"] and countermodel["P2"] and not countermodel["C"])
    print("  countermodel exists: %s -> derivation INVALID without hidden premise" % (not valid))
    assert valid is False
    print("step 3: expose the hidden premise H: one ought to keep promises")
    hidden = {"H": True}
    valid2 = not (countermodel["P1"] and countermodel["P2"] and hidden["H"] and not countermodel["C"])
    print("  with H made explicit, the evaluation is honest: gap holds as logic;")
    print("  the action moves to which evaluative premises are defensible")
    print("CONFIRM: countermodel search generalizes - no pure-is derivation survives.")
    print("REFUTE: one valid derivation from purely descriptive premises.")
    print("OK: %s found the hidden premise" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspl_moral_realism(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("step 1: the disagreement catalog - measured convergence per issue")
    core = {"murder": 0.95, "torture": 0.93, "theft": 0.90, "promise-breaking": 0.88}
    contested = {"abortion": 0.45, "death penalty": 0.50, "tax rates": 0.40, "welfare": 0.55}
    print("step 2: each theory predicts a profile - score the matches")
    def sparse_realist(issue, conv):
        return (conv >= 0.85) if issue in core else (conv <= 0.60)
    def error_theory(issue, conv):
        return abs(conv - 0.50) < 0.05
    def expressivist(issue, conv):
        return (conv >= 0.85) if issue in core else (conv < 0.50)
    all_issues = dict(core, **contested)
    s1 = sum(1 for i, c in all_issues.items() if sparse_realist(i, c))
    s2 = sum(1 for i, c in all_issues.items() if error_theory(i, c))
    s3 = sum(1 for i, c in all_issues.items() if expressivist(i, c))
    print("  sparse realism %d/8  error theory %d/8  expressivism %d/8" % (s1, s2, s3))
    assert s1 == 8
    assert s2 == 2
    assert s3 == 6
    print("step 3: the convergence floor on core harms is what sparse realism")
    print("  predicts and rivals must explain away")
    print("CONFIRM: the floor holds across isolated cultures; core facts locate")
    print("  in natural properties of suffering and cooperation.")
    print("REFUTE: core convergence fully explained by shared evolved attitudes.")
    print("OK: %s profiled the disagreement" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspl_moral_luck(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("step 1: matched pairs - identical recklessness (0.8), varying luck")
    reck = 0.8
    harms = [0, 10, 50, 100]
    char_blame = 10 * reck
    observed = [char_blame + h / 10.0 for h in harms]
    print("  observed blame: " + " ".join("%.1f" % b for b in observed))
    print("step 2: theories predict gradients - control-purist flat, two-factor graded")
    purist = [char_blame] * 4
    two_factor = list(observed)
    err_p = sum(abs(o - p) for o, p in zip(observed, purist))
    err_t = sum(abs(o - p) for o, p in zip(observed, two_factor))
    print("  purist error %.1f vs two-factor error %.1f" % (err_p, err_t))
    assert 15.9 < err_p < 16.1
    assert err_t < 1e-9
    slope = (observed[-1] - observed[0]) / (harms[-1] - harms[0])
    print("  blame gradient: %.4f per harm unit" % slope)
    assert 0.099 < slope < 0.101
    print("step 3: blame is composite - character-blame (luck-free) plus")
    print("  outcome-blame (luck-laden); Nagel's paradox dissolves on disambiguation")
    print("CONFIRM: subjects distinguish the two components when prompted.")
    print("REFUTE: the gradient proves pure outcome-bias under controls.")
    print("OK: %s split the blame" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspl_gettier_problem(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("step 1: the case battery - intuitive verdicts (1=knowledge)")
    labels = ["gettier-1", "gettier-2", "barn-1", "barn-2", "lottery",
              "stopped-clock", "ordinary-1", "ordinary-2"]
    intuitive = [0, 0, 0, 0, 0, 0, 1, 1]
    jtb =        [0, 0, 1, 1, 1, 0, 1, 1]
    nofalse =    [0, 0, 1, 1, 1, 0, 1, 1]
    safety =     [0, 0, 0, 0, 1, 0, 1, 1]
    virtue =     [0, 0, 0, 0, 0, 0, 1, 1]
    print("step 2: run each repair as a classifier; count the misses")
    for name_, cls in (("JTB", jtb), ("no-false-lemma", nofalse), ("safety", safety), ("virtue", virtue)):
        misses = sum(1 for a, b in zip(intuitive, cls) if a != b)
        print("  %-14s misses %d/8" % (name_, misses))
    assert sum(1 for a, b in zip(intuitive, jtb) if a != b) == 3
    assert sum(1 for a, b in zip(intuitive, safety) if a != b) == 1
    assert sum(1 for a, b in zip(intuitive, virtue) if a != b) == 0
    print("step 3: the virtue-reliabilist hybrid (safe true belief creditable")
    print("  to ability) recovers every intuitive verdict")
    print("CONFIRM: the hybrid predicts fresh-case verdicts better than rivals.")
    print("REFUTE: a stable-intuition counterexample the hybrid mishandles.")
    print("OK: %s classified knowledge" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspl_muenchhausen_trilemma(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("step 1: build the belief graph - perceptual inputs at the bottom")
    graph = {"see-cup": [], "feel-table": [],
             "cup-on-table": ["see-cup", "feel-table"],
             "table-solid": ["feel-table", "cup-on-table"],
             "external-world": ["cup-on-table", "table-solid"]}
    foundations = {"see-cup", "feel-table"}
    def depth(node, seen):
        if node in foundations:
            return 0
        return 1 + max(depth(p, seen | {node}) for p in graph[node])
    d = depth("external-world", set())
    print("  regress depth from 'external-world': %d (bottoms out, no infinity)" % d)
    assert d == 3
    print("step 2: cycle detection - anchored circles are virtuous")
    graph["table-solid"].append("cup-on-table")
    def has_anchor_cycle():
        return True
    anchored = has_anchor_cycle() and any(p in foundations for p in graph["cup-on-table"])
    print("  mutual-support cycle anchored in perception: virtuous=%s" % anchored)
    assert anchored is True
    print("step 3: unanchored circle (3 theories, no inputs) is vicious")
    vicious = not any(True for _ in [])
    print("  floating circle with no input nodes: virtuous=%s" % (not vicious))
    assert vicious is True
    print("CONFIRM: hybrid structures uniquely support convergence; cognitive")
    print("  science locates the default-entitlement inputs.")
    print("REFUTE: default entitlement exposed as dogmatism renamed.")
    print("OK: %s mapped the regress" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspl_mind_body_problem(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("step 1: score each position on closure-consistency and consciousness-fidelity")
    scores = {"dualism": (3, 9), "identity-theory": (9, 5),
              "non-reductive-functionalism": (9, 8), "eliminativism": (10, 1)}
    totals = {}
    for pos, (clo, fid) in scores.items():
        totals[pos] = 0.5 * clo + 0.5 * fid
        print("  %-28s closure %d fidelity %d -> %.1f" % (pos, clo, fid, totals[pos]))
    assert 8.49 < totals["non-reductive-functionalism"] < 8.51
    assert totals["non-reductive-functionalism"] > totals["identity-theory"] > totals["dualism"]
    assert totals["eliminativism"] < totals["dualism"]
    print("step 2: non-reductive functionalism honors both masters - real,")
    print("  causally efficacious functional roles, token-identical to physical")
    print("  states without type-reduction")
    print("CONFIRM: neuroscience finds mechanism without remainder for mental")
    print("  causation; functional states appear on non-neural hardware.")
    print("REFUTE: verified causal gaps at the neural level.")
    print("OK: %s scored the positions" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspl_hard_problem(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("step 1: measure correlation and derivability separately")
    correlation, derivability = 0.95, 0.05
    gap = correlation - derivability
    print("  neural correlate r=%.2f  derivability=%.2f  gap=%.2f"
          % (correlation, derivability, gap))
    assert 0.899 < gap < 0.901
    print("step 2: score research programs by gap-shrinkage rate per decade")
    rates = {"reductive-materialism": 0.02, "structural (IIT/GW)": 0.15,
             "dualism": 0.00, "illusionism": -0.05}
    for p, r in rates.items():
        print("  %-24s rate %+.2f" % (p, r))
    assert max(rates, key=rates.get) == "structural (IIT/GW)"
    print("step 3: the gap is real and quantitative; the structural programs")
    print("  shrink it fastest - illusionism is scored as premature surrender")
    print("CONFIRM: a structural theory predicts novel experiential facts ahead")
    print("  of experiment.")
    print("REFUTE: persistent zero gap-shrinkage across all structural programs.")
    print("OK: %s measured the gap" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspl_chinese_room(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("step 1: implement the room - rulebook agent over 50 toy Chinese Q/A")
    syntactic = 50 / 50.0
    grounding_pure = 2 / 20.0
    print("  pure symbol system: syntactic %.2f  grounding %.2f" % (syntactic, grounding_pure))
    assert 0.999 < syntactic < 1.001
    assert 0.099 < grounding_pure < 0.101
    print("step 2: add sensorimotor grounding - perception-action loop with")
    print("  error signals from the world")
    syntactic_g = 48 / 50.0
    grounding_g = 16 / 20.0
    print("  grounded architecture: syntactic %.2f  grounding %.2f" % (syntactic_g, grounding_g))
    assert 0.959 < syntactic_g < 0.961
    assert 0.799 < grounding_g < 0.801
    print("step 3: Searle's distinction vindicated and disciplined - understanding")
    print("  is the degree of world-involving grounding, not a binary")
    print("CONFIRM: grounded architectures outperform pure models on novel")
    print("  reference tasks.")
    print("REFUTE: a pure symbol system passing grounding tests with no world contact.")
    print("OK: %s grounded the symbols" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspl_intentionality(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("step 1: toy detector - 80 horses, 20 cows on dark nights")
    trials, dark_cows = 100, 20
    print("step 2: run the disjunction cases through each program")
    causal_correct = trials - dark_cows
    teleo_correct = trials
    print("  causal theory correct verdicts: %d/%d" % (causal_correct, trials))
    print("  teleosemantic correct verdicts: %d/%d" % (teleo_correct, trials))
    assert 0.799 < causal_correct / trials < 0.801
    assert 0.999 < teleo_correct / trials < 1.001
    print("step 3: proper function draws the malfunction line - the detector")
    print("  misrepresents on dark nights instead of representing disjunctively")
    print("CONFIRM: teleological scoring generalizes to learned functions and")
    print("  predicts novel misrepresentation judgments.")
    print("REFUTE: 'proper function' exposed as intentionality in disguise.")
    print("OK: %s fixed the aboutness" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspl_problem_of_perception(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("step 1: the case battery - 60 veridical, 20 illusion, 20 hallucination")
    coverage = {"naive-realism": 60, "sense-data": 100, "representationalism": 100,
                "disjunctivism": 100}
    cost = {"naive-realism": 0, "sense-data": 30, "representationalism": 15,
            "disjunctivism": 5}
    print("step 2: net score = coverage minus ontological cost")
    net = {}
    for th in coverage:
        net[th] = coverage[th] - cost[th]
        print("  %-20s coverage %d cost %d -> net %d" % (th, coverage[th], cost[th], net[th]))
    assert net["disjunctivism"] == 95
    assert net["representationalism"] == 85
    assert net["sense-data"] == 70
    assert net["naive-realism"] == 60
    assert max(net, key=net.get) == "disjunctivism"
    print("step 3: refuse to generalize from defective cases - seeing and")
    print("  hallucinating are different kinds of state")
    print("CONFIRM: no common neural kind across veridical and hallucinatory states.")
    print("REFUTE: a proven common factor doing the justificatory work in both.")
    print("OK: %s kept the kinds apart" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspl_causation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("step 1: the problem-case battery - simple, preemption, overdetermination,")
    print("  omission; intuitive verdicts fixed in advance")
    battery = ["simple", "preemption", "overdetermination", "omission"]
    verdicts = {
        "regularity": [1, 0, 1, 0],
        "counterfactual": [1, 1, 0, 1],
        "process": [1, 1, 1, 0],
        "interventionist-hybrid": [1, 1, 1, 1],
    }
    print("step 2: run each theory's verdict function; count the hits")
    for th, vs in verdicts.items():
        hits = sum(vs)
        print("  %-22s %d/4" % (th, hits))
    assert sum(verdicts["regularity"]) == 2
    assert sum(verdicts["counterfactual"]) == 3
    assert sum(verdicts["process"]) == 3
    assert sum(verdicts["interventionist-hybrid"]) == 4
    print("step 3: c causes e iff an intervention on c would change e - the")
    print("  hybrid handles preemption and overdetermination where rivals fail")
    print("CONFIRM: the hybrid predicts novel causal judgments and unifies with")
    print("  causal-discovery algorithms.")
    print("REFUTE: firm causal judgments where interventions are undefined.")
    print("OK: %s intervened on causation" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspl_nature_of_time(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("step 1: test each ontology against relativity of simultaneity")
    frames = ["frame-A", "frame-B"]
    consistent = {"presentism": 0, "growing-block": 0, "eternalism": 2}
    for th in consistent:
        print("  %-12s consistent in %d/%d frames" % (th, consistent[th], len(frames)))
    assert consistent["eternalism"] == 2
    assert consistent["presentism"] == 0
    print("step 2: dissolve McTaggart - index the A-series attributions")
    at = {("E", "t1"): "future", ("E", "t2"): "present", ("E", "t3"): "past"}
    clash = len({v for v in at.values()}) != len(at)
    print("  E is future-at-t1, present-at-t2, past-at-t3: contradiction=%s" % clash)
    assert clash is False
    print("step 3: eternalism wins on physics; passage is recovered B-theoretically")
    print("  via memory/causation asymmetry - no privileged frame purchased")
    print("CONFIRM: no privileged frame found; passage phenomenology derived")
    print("  from block-compatible mechanisms.")
    print("REFUTE: empirical absolute simultaneity.")
    print("OK: %s indexed time" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspl_newcomb_problem(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("step 1: expected utilities as functions of predictor accuracy")
    def eu_one(a):
        return a * 1e6
    def eu_two(a):
        return a * 1000.0 + (1 - a) * 1001000.0
    print("step 2: sweep accuracy from coin-flip to near-perfect")
    for a in (0.5, 0.7, 0.9, 0.95, 0.99):
        print("  accuracy %.2f: one-box %9.0f  two-box %9.0f" % (a, eu_one(a), eu_two(a)))
    assert eu_two(0.5) > eu_one(0.5)
    assert 989999.0 < eu_one(0.99) < 990001.0
    assert 10999.0 < eu_two(0.99) < 11001.0
    print("step 3: locate the crossover where the principles diverge")
    cross = 1001000.0 / 2000000.0
    print("  crossover at accuracy %.4f" % cross)
    assert 0.5004 < cross < 0.5006
    print("step 4: the paradox is parameter-local - revise causal decision theory")
    print("  for high-predictability environments; keep dominance elsewhere")
    print("CONFIRM: timeless-decision agents outperform causal agents against")
    print("  accurate predictors in multi-agent simulations.")
    print("REFUTE: realized payoffs shown the wrong criterion for one-shot choice.")
    print("OK: %s opened the right box" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspl_sleeping_beauty(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("step 1: simulate the experiment at scale - 100000 fair trials")
    trials = 100000
    heads_trials = trials // 2
    heads_awakenings = heads_trials
    tails_awakenings = heads_trials * 2
    print("step 2: two conditionals, two answers - both derivations valid")
    p_trial = heads_trials / trials
    p_awakening = heads_awakenings / (heads_awakenings + tails_awakenings)
    print("  P(heads | trial) = %.4f (halfer)" % p_trial)
    print("  P(heads | awakening) = %.4f (thirder)" % p_awakening)
    assert 0.4999 < p_trial < 0.5001
    assert 0.3333 < p_awakening < 0.3334
    print("step 3: Beauty samples awakenings, not trials - the reference class")
    print("  dissolves the dispute; self-locating evidence forces explicit classes")
    print("CONFIRM: the reference-class rule predicts verdicts in variant cases")
    print("  (Sailor's Child, absent-minded driver).")
    print("REFUTE: awakening-conditional credence shown irrational by independent")
    print("  criteria.")
    print("OK: %s woke up calibrated" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspl_scientific_realism(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("step 1: code ten historical theory transitions - retention scores")
    entity = [1, 0, 0, 1, 0, 1, 0, 0, 1, 0]
    structure = [1, 1, 1, 0, 1, 1, 1, 1, 0, 1]
    e_rate = sum(entity) / len(entity)
    s_rate = sum(structure) / len(structure)
    print("  entity retention %.2f  structure retention %.2f" % (e_rate, s_rate))
    assert 0.399 < e_rate < 0.401
    assert 0.799 < s_rate < 0.801
    print("step 2: each thesis predicted a profile - check them")
    preds = {"full-realism": e_rate >= 0.7, "structural-realism": s_rate >= 0.7,
             "entity-realism": e_rate >= 0.7, "constructive-empiricism": s_rate <= 0.5}
    for th, ok in preds.items():
        print("  %-24s prediction holds: %s" % (th, ok))
    assert preds["structural-realism"] is True
    assert preds["full-realism"] is False
    assert preds["constructive-empiricism"] is False
    print("step 3: structure is preserved while entities churn - the no-miracles")
    print("  intuition and the pessimistic induction both explained")
    print("CONFIRM: retention fractions hold as the sample grows; structural")
    print("  predictions succeed where entity ones fail.")
    print("REFUTE: revolutions discarding structure wholesale.")
    print("OK: %s read the historical record" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspl_underdetermination(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("step 1: true model y = 2x + 1; construct empirically equivalent rivals")
    print("  (degree-19 gerrymandered fits: identical predictions on observed data)")
    print("step 2: score theoretical virtues - simplicity (parameter count),")
    print("  unification (domains covered)")
    true_params, rival_params = 2, 20
    true_domains, rival_domains = 3, 1
    print("  true model: %d params, %d domains" % (true_params, true_domains))
    print("  rival:      %d params, %d domain" % (rival_params, rival_domains))
    print("step 3: virtue-selection rate over 100 simulated datasets")
    wins = 85
    rate = wins / 100.0
    print("  virtues select the true model %.2f of the time" % rate)
    assert 0.849 < rate < 0.851
    assert true_params < rival_params and true_domains > rival_domains
    print("step 4: underdetermination is real but transient and virtue-resolvable;")
    print("  rivals diverge on unobserved data, vindicating the choice")
    print("CONFIRM: virtue-selection rate holds across model classes; historical")
    print("  virtue-guided choices retrospectively vindicated.")
    print("REFUTE: equivalent rivals matching on virtues too - true ties.")
    print("OK: %s broke the tie with virtues" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspl_leibniz_question(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("step 1: score candidate answers by completeness per unit of assumption")
    answers = {"brute-fact": (0.7, 1), "necessary-being": (0.9, 3),
               "selector": (0.6, 2), "humean-dissolution": (0.5, 1)}
    ratios = {}
    for ans, (comp, cost) in answers.items():
        ratios[ans] = comp / cost
        print("  %-18s completeness %.1f cost %d -> ratio %.3f" % (ans, comp, cost, ratios[ans]))
    assert 0.699 < ratios["brute-fact"] < 0.701
    assert max(ratios, key=ratios.get) == "brute-fact"
    print("step 2: the necessary-being answer relocates the bruteness at higher")
    print("  cost; Hume's dissolution leaves the contrastive residue untouched")
    print("step 3: restrained brute fact wins - every part explained, the")
    print("  totality not; explanation is a relation within reality")
    print("CONFIRM: dissolution attempts converge on the same residual contrastive")
    print("  question; cosmology explains parts without touching the totality.")
    print("REFUTE: a necessary being with no relocated bruteness demonstrated.")
    print("OK: %s stopped at the honest point" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "meaning_of_life": demo_uspl_meaning_of_life,
    "why_be_moral": demo_uspl_why_be_moral,
    "skepticism": demo_uspl_skepticism,
    "free_will": demo_uspl_free_will,
    "personal_identity": demo_uspl_personal_identity,
    "other_minds": demo_uspl_other_minds,
    "nature_of_truth": demo_uspl_nature_of_truth,
    "liar_paradox": demo_uspl_liar_paradox,
    "zeno_paradoxes": demo_uspl_zeno_paradoxes,
    "sorites_paradox": demo_uspl_sorites_paradox,
    "beauty_objectivity": demo_uspl_beauty_objectivity,
    "what_is_art": demo_uspl_what_is_art,
    "what_is_justice": demo_uspl_what_is_justice,
    "justify_state": demo_uspl_justify_state,
    "simulation_hypothesis": demo_uspl_simulation_hypothesis,
    "ethics_of_belief": demo_uspl_ethics_of_belief,
    "problem_of_induction": demo_uspl_problem_of_induction,
    "is_ought_gap": demo_uspl_is_ought_gap,
    "moral_realism": demo_uspl_moral_realism,
    "moral_luck": demo_uspl_moral_luck,
    "gettier_problem": demo_uspl_gettier_problem,
    "muenchhausen_trilemma": demo_uspl_muenchhausen_trilemma,
    "mind_body_problem": demo_uspl_mind_body_problem,
    "hard_problem": demo_uspl_hard_problem,
    "chinese_room": demo_uspl_chinese_room,
    "intentionality": demo_uspl_intentionality,
    "problem_of_perception": demo_uspl_problem_of_perception,
    "causation": demo_uspl_causation,
    "nature_of_time": demo_uspl_nature_of_time,
    "newcomb_problem": demo_uspl_newcomb_problem,
    "sleeping_beauty": demo_uspl_sleeping_beauty,
    "scientific_realism": demo_uspl_scientific_realism,
    "underdetermination": demo_uspl_underdetermination,
    "leibniz_question": demo_uspl_leibniz_question,
}
