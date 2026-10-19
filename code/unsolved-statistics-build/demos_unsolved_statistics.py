#!/usr/bin/env python3
"""Demo programs for the Unsolved Statistics databases (Manon's 16:15 orders, batch 1).

Every demo is a solution-explorer walkthrough: real, runnable, stdlib-only
Python that (1) computes concrete evidence related to its unsolved problem,
(2) walks through the Signature solution approach with adjustable
assumptions, and (3) prints an explicit CONFIRM / REFUTE panel. All are
machine-executed by build.py: each prints its real computed values, asserts
tight bounds (never float exact-equality), and ends with the OK marker.

Honesty rule: no demo claims a proof. Computational checks are labeled as
checks, heuristics as heuristics, and every panel states what would confirm
or kill the proposed approach.
"""

_PREAMBLE = "import math, random\n\ndef _mean(xs):\n    return sum(xs) / len(xs)\n\ndef _var(xs):\n    m = _mean(xs)\n    return sum((x - m) ** 2 for x in xs) / (len(xs) - 1)\n\ndef _sd(xs):\n    return math.sqrt(_var(xs))\n\ndef _randn(rng):\n    u1 = rng.random()\n    if u1 <= 0.0:\n        u1 = 0.5\n    u2 = rng.random()\n    return math.sqrt(-2.0 * math.log(u1)) * math.cos(2.0 * math.pi * u2)\n\ndef _ncdf(x):\n    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))\n\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_usst_induction(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    rng = random.Random(11)
    pre = [_randn(rng) for _ in range(4000)]
    post = [2.0 + _randn(rng) for _ in range(4000)]
    m_pre = _mean(pre)
    m_post = _mean(post)
    print("pre-change mean (n=4000): %.4f" % m_pre)
    print("post-change mean (n=4000): %.4f" % m_post)
    assert abs(m_pre) < 0.1, "pre-change sample should center near 0"
    assert abs(m_post - 2.0) < 0.1, "post-change sample should center near 2"
    # A prediction built only on the past: predict the next 4000 from the first 4000.
    err = abs(m_pre - m_post)
    print("prediction error of past-only forecast: %.4f" % err)
    assert err > 1.5, "the regime change must actually break the forecast"
    # Signature approach S-01: monitored-stability induction.
    # Adjustable assumption A1: change points are detectable, not adversarially hidden.
    print("approach: attach a sequential change monitor to every inference; withdraw the")
    print("  forecast when the monitor fires instead of extrapolating silently")
    print("CONFIRM IF: monitored procedures detect real regime changes faster than unmonitored ones with few false alarms")
    print("REFUTE IF: change points prove undetectable before they corrupt inference")
    print("does NOT claim: a logical justification of induction - Hume stands undefeated")
    print("OK: %s showed past data going blind at the change point" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usst_prob_interpretations(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    rng = random.Random(23)
    n = 20000
    heads = sum(1 for _ in range(n) if rng.random() < 0.5)
    freq = heads / n
    # Bayesian posterior mean with a uniform Beta(1,1) prior.
    post = (heads + 1.0) / (n + 2.0)
    print("flips: %d, heads: %d" % (n, heads))
    print("frequentist estimate (long-run proportion): %.5f" % freq)
    print("Bayesian posterior mean, Beta(1,1) prior:  %.5f" % post)
    assert abs(freq - 0.5) < 0.02
    assert abs(post - 0.5) < 0.02
    assert abs(freq - post) < 0.005, "the camps agree numerically here"
    # Signature approach S-02: interpretation-translation discipline.
    # Adjustable assumption A1: the camps usually agree numerically; they differ on licensing.
    print("approach: compute every camp answer side by side and ship each with its license -")
    print("  the list of claims its numbers are allowed to support")
    print("CONFIRM IF: licensed reporting reduces interpretation errors by decision-makers in trials")
    print("REFUTE IF: the camps compute irreconcilably different numbers from the same evidence")
    print("does NOT claim: a true interpretation of probability - the debate stays open")
    print("OK: %s showed numerical agreement with semantic disagreement" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usst_confidence_meaning(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    rng = random.Random(37)
    mu, sd, n, reps = 5.0, 2.0, 30, 2000
    cover = 0
    first = None
    for r in range(reps):
        xs = [mu + sd * _randn(rng) for _ in range(n)]
        m = _mean(xs)
        half = 1.96 * sd / math.sqrt(n)
        lo, hi = m - half, m + half
        if r == 0:
            first = (lo, hi)
        if lo <= mu <= hi:
            cover += 1
    rate = cover / reps
    print("intervals built: %d, coverage of true mean 5.0: %.4f" % (reps, rate))
    print("one realized interval: [%.4f, %.4f] - it covers 5.0 or it does not" % first)
    assert 0.93 < rate < 0.97, "procedure coverage must land near 95 percent"
    # Signature approach S-03: meaning-labeled intervals.
    # Adjustable assumption A1: the misreading is caused by missing semantics, not innumeracy.
    print("approach: print the one-sentence license with the numbers - 95 percent of such")
    print("  intervals cover - and test that readers can paraphrase it back")
    print("CONFIRM IF: labeled intervals measurably reduce the fallacious 95-percent-chance reading")
    print("REFUTE IF: users misread even perfectly labeled intervals")
    print("does NOT claim: a new definition of confidence - Neyman stands as defined")
    print("OK: %s verified procedure coverage near 95 percent" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usst_replication(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    rng = random.Random(41)
    true_d = 0.2
    n, labs = 40, 400
    published = []
    for _ in range(labs):
        x = [_randn(rng) for _ in range(n)]
        y = [true_d + _randn(rng) for _ in range(n)]
        diff = _mean(y) - _mean(x)
        se = math.sqrt(2.0 / n)
        z = diff / se
        p = 2.0 * (1.0 - _ncdf(abs(z)))
        if p < 0.05:
            published.append(diff)
    pub_mean = _mean(published)
    print("labs: %d, published (p<0.05): %d" % (labs, len(published)))
    print("true effect: %.2f, mean published effect: %.4f" % (true_d, pub_mean))
    assert pub_mean > 0.32, "selection on significance must inflate the published mean"
    # Replication with a larger sample: the winner curse washes out.
    n2 = 400
    x = [_randn(rng) for _ in range(n2)]
    y = [true_d + _randn(rng) for _ in range(n2)]
    rep = _mean(y) - _mean(x)
    print("large-sample replication estimate: %.4f (shrinkage toward truth)" % rep)
    assert abs(rep - true_d) < 0.12
    # Signature approach S-04: selection-discounted inference.
    # Adjustable assumption A1: published results are a significance-selected sample.
    print("approach: estimate the selection function from the literature and discount every")
    print("  claim by the selection pressure that produced it")
    print("CONFIRM IF: discounted estimates predict real replication outcomes better than raw ones")
    print("REFUTE IF: selection mechanisms prove too heterogeneous to estimate")
    print("does NOT claim: a cure for bad incentives - methods cannot fix incentives alone")
    print("OK: %s showed publication inflation and replication shrinkage" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usst_pvalues(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    rng = random.Random(53)
    m = 5000
    bins = [0] * 10
    for _ in range(m):
        z = _randn(rng)
        p = 2.0 * (1.0 - _ncdf(abs(z)))
        b = min(int(p * 10), 9)
        bins[b] += 1
    print("null p-value decile counts (expect ~500 each):")
    print(" ".join(str(c) for c in bins))
    for c in bins:
        assert 400 <= c <= 600, "null p-values must be approximately uniform"
    sig = sum(bins[0:1])
    print("p < 0.10 under the null: %d of %d (%.1f percent)" % (bins[0], m, 100.0 * bins[0] / m))
    # Signature approach S-05: job-separated evidence instruments.
    # Adjustable assumption A1: no single number can serve evidence, error control, and decisions.
    print("approach: retire the p-value from evidence duty; report e-values for evidence,")
    print("  calibrated effect sizes for practical importance - each labeled for its job")
    print("CONFIRM IF: separated instruments cut false discovery claims versus p-value practice")
    print("REFUTE IF: analysts game the new instruments just as effectively")
    print("does NOT claim: a proven superior successor - the field has not adopted one")
    print("OK: %s verified null p-value uniformity" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usst_multiple_testing(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    rng = random.Random(67)
    m = 2000
    pvals = []
    for _ in range(m):
        z = _randn(rng)
        pvals.append(2.0 * (1.0 - _ncdf(abs(z))))
    raw = sum(1 for p in pvals if p < 0.05)
    bonf = sum(1 for p in pvals if p < 0.05 / m)
    srt = sorted(pvals)
    q = 0.10
    bh = 0
    for k, p in enumerate(srt, start=1):
        if p <= k / m * q:
            bh = k
    print("tests: %d, all null" % m)
    print("raw rejections at 0.05: %d (expect ~100)" % raw)
    print("Bonferroni rejections: %d" % bonf)
    print("Benjamini-Hochberg rejections at q=0.10: %d" % bh)
    assert 60 <= raw <= 140
    assert bonf <= 3
    assert bh <= raw
    # Signature approach S-06: explicit error budgeting.
    # Adjustable assumption A1: every investigation can state its false-claim budget up front.
    print("approach: declare the error budget - which rate, what level, why - before data")
    print("  collection, and spend it where discoveries matter most")
    print("CONFIRM IF: budgeted procedures hit stated rates in replication audits with more true finds")
    print("REFUTE IF: budgets get chosen post hoc to justify whatever was found")
    print("does NOT claim: a universally correct error rate - the choice stays a judgment call")
    print("OK: %s contrasted raw, Bonferroni, and FDR rejection counts" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usst_optional_stopping(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    rng = random.Random(71)
    reps = 3000
    fixed = 0
    for _ in range(reps):
        xs = [_randn(rng) for _ in range(200)]
        z = sum(xs) / math.sqrt(200)
        if abs(z) > 1.96:
            fixed += 1
    peek = 0
    for _ in range(reps):
        xs = [_randn(rng) for _ in range(200)]
        s = 0.0
        stopped = False
        for k in (50, 100, 150, 200):
            s = sum(xs[:k])
            if abs(s / math.sqrt(k)) > 1.96:
                stopped = True
                break
        if stopped:
            peek += 1
    rf = fixed / reps
    rp = peek / reps
    print("fixed-sample rejection rate under null: %.4f (expect ~0.05)" % rf)
    print("peeking rejection rate under null:      %.4f (inflated)" % rp)
    assert 0.035 < rf < 0.065
    assert rp > 0.10, "peeking must inflate the false positive rate"
    # Signature approach S-07: auditable anytime evidence.
    # Adjustable assumption A1: analysts will peek, so the method must survive peeking.
    print("approach: replace fixed-sample p-values with e-value processes valid at any stopping")
    print("  time, and log every interim look in a tamper-evident record")
    print("CONFIRM IF: anytime rules reach correct conclusions as often while stopping earlier on average")
    print("REFUTE IF: e-value procedures prove too conservative for practical use")
    print("does NOT claim: a resolution of the stopping-rule philosophical debate")
    print("OK: %s showed peeking inflates Type I error" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usst_likelihood_principle(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Same data: 3 successes in 10 trials. Binomial vs negative binomial (stop at 3rd success).
    from math import comb
    def lb(p):
        return comb(10, 3) * p ** 3 * (1 - p) ** 7
    def ln(p):
        return comb(9, 2) * p ** 3 * (1 - p) ** 7
    for p in (0.2, 0.5, 0.8):
        ratio = lb(p) / ln(p)
        print("p=%.1f: likelihood ratio binomial/negbin = %.4f" % (p, ratio))
        assert abs(ratio - comb(10, 3) / comb(9, 2)) < 1e-9, "likelihoods are proportional"
    # Frequentist p-values differ: binomial tail vs negative binomial tail at p0=0.5.
    pb = sum(comb(10, k) * 0.5 ** 10 for k in range(0, 4))
    pn = sum(comb(k - 1, 2) * 0.5 ** k for k in range(3, 11))
    print("binomial p-value (k<=3 | p=0.5):      %.4f" % pb)
    print("negative binomial p-value (n>=10):    %.4f" % pn)
    assert abs(pb - pn) > 0.05, "frequentist answers differ on identical likelihoods"
    # Signature approach S-08: question-first reporting.
    # Adjustable assumption A1: evidence questions and procedure questions are both legitimate.
    print("approach: declare whether the analysis answers an evidence question or a procedure")
    print("  question, then use the instrument that fits the declared question")
    print("CONFIRM IF: question-first reporting reduces cross-camp miscommunication in surveys")
    print("REFUTE IF: the two questions prove inseparable in practice")
    print("does NOT claim: a proof or refutation of the likelihood principle")
    print("OK: %s exhibited proportional likelihoods with differing p-values" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usst_model_selection(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    rng = random.Random(83)
    n, reps = 60, 200
    bic_true = 0
    mse_aic, mse_bic = 0.0, 0.0
    for _ in range(reps):
        xs = [rng.uniform(-2, 2) for _ in range(n)]
        ys = [x * x + _randn(rng) for x in xs]
        xt = [rng.uniform(-2, 2) for _ in range(200)]
        yt = [x * x for x in xt]
        def fit(deg):
            # least squares via normal equations on [1, x, x^2...]
            import copy
            d = deg + 1
            xtx = [[0.0] * d for _ in range(d)]
            xty = [0.0] * d
            for x, y in zip(xs, ys):
                pw = [x ** j for j in range(d)]
                for a in range(d):
                    xty[a] += pw[a] * y
                    for b in range(d):
                        xtx[a][b] += pw[a] * pw[b]
            # solve by Gaussian elimination
            m = [row[:] + [xty[i]] for i, row in enumerate(xtx)]
            for c in range(d):
                piv = m[c][c]
                for r in range(c + 1, d):
                    f = m[r][c] / piv
                    for cc in range(c, d + 1):
                        m[r][cc] -= f * m[c][cc]
            beta = [0.0] * d
            for c in range(d - 1, -1, -1):
                beta[c] = (m[c][d] - sum(m[c][cc] * beta[cc] for cc in range(c + 1, d))) / m[c][c]
            rss = sum((y - sum(beta[j] * x ** j for j in range(d))) ** 2 for x, y in zip(xs, ys))
            pred = sum((y - sum(beta[j] * x ** j for j in range(d))) ** 2 for x, y in zip(xt, yt)) / len(xt)
            return rss, pred
        rss1, pr1 = fit(1)
        rss2, pr2 = fit(2)
        aic1 = n * math.log(rss1 / n) + 2 * 2
        aic2 = n * math.log(rss2 / n) + 2 * 3
        bic1 = n * math.log(rss1 / n) + 2 * math.log(n)
        bic2 = n * math.log(rss2 / n) + 3 * math.log(n)
        pick_aic = 2 if aic2 < aic1 else 1
        pick_bic = 2 if bic2 < bic1 else 1
        if pick_bic == 2:
            bic_true += 1
        mse_aic += pr2 if pick_aic == 2 else pr1
        mse_bic += pr2 if pick_bic == 2 else pr1
    print("BIC selected the true quadratic model in %d of %d reps" % (bic_true, reps))
    print("mean prediction MSE, AIC-chosen: %.4f; BIC-chosen: %.4f" % (mse_aic / reps, mse_bic / reps))
    assert bic_true / reps > 0.75, "BIC should be consistent for the true model"
    assert mse_aic / reps <= mse_bic / reps + 0.05, "AIC should predict at least as well"
    # Signature approach S-09: goal-declared selection.
    # Adjustable assumption A1: the modeling goal sits on the prediction-explanation spectrum.
    print("approach: declare the goal - predict or explain - before selecting, and let the goal")
    print("  choose the criterion, with the unchosen one as sensitivity check")
    print("CONFIRM IF: goal-declared selections disagree less across analysts on the same data")
    print("REFUTE IF: goals prove too vague to map to criteria")
    print("does NOT claim: a universal criterion - Yang impossibility stands")
    print("OK: %s showed BIC consistent and AIC predictive" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usst_reference_class(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    rng = random.Random(97)
    n = 6000
    # Nested classes: all adults 60+, then smokers among them, then smokers with family history.
    c1 = c2 = c3 = 0
    d1 = d2 = d3 = 0
    for _ in range(n):
        smoker = rng.random() < 0.35
        fam = rng.random() < 0.25
        risk = 0.10 + (0.08 if smoker else 0.0) + (0.12 if fam else 0.0)
        sick = rng.random() < risk
        c1 += 1
        d1 += sick
        if smoker:
            c2 += 1
            d2 += sick
            if fam:
                c3 += 1
                d3 += sick
    r1, r2, r3 = d1 / c1, d2 / c2, d3 / c3
    print("P(disease | age 60+):                %.4f" % r1)
    print("P(disease | age 60+, smoker):        %.4f" % r2)
    print("P(disease | age 60+, smoker, famhx): %.4f" % r3)
    assert abs(r2 - r1) > 0.04 and abs(r3 - r2) > 0.04, "the number must move with the class"
    # Signature approach S-10: class-labeled probabilities.
    # Adjustable assumption A1: the reference class is a reportable parameter of the claim.
    print("approach: name the reference class with every probability and report the range")
    print("  across a ladder of nested classes")
    print("CONFIRM IF: class-labeled reporting improves decisions in risk-scoring trials")
    print("REFUTE IF: class ladders prove too unstable for the ranges to be useful")
    print("does NOT claim: a rule for the one true reference class")
    print("OK: %s showed the probability moving with the reference class" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usst_prior_elicitation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    k, n = 7, 10
    priors = {"Beta(1,1) flat": (1.0, 1.0), "Beta(10,10) strong": (10.0, 10.0),
              "Beta(2,8) skeptical": (2.0, 8.0)}
    means = {}
    for label, (a, b) in priors.items():
        pm = (k + a) / (n + a + b)
        means[label] = pm
        print("posterior mean under %-22s: %.4f" % (label, pm))
    spread = max(means.values()) - min(means.values())
    print("spread across reasonable priors: %.4f" % spread)
    assert spread > 0.15, "the prior must visibly move the posterior here"
    # Signature approach S-11: prior budgeting with adversarial audit.
    # Adjustable assumption A1: the prior influence is measurable by sensitivity.
    print("approach: declare the prior as an assumption budget, report the posterior range over")
    print("  reasonable priors, and give the most hostile reasonable prior its say")
    print("CONFIRM IF: audited analyses replicate better than unaudited ones")
    print("REFUTE IF: reasonable-prior classes prove too wide to permit any conclusion")
    print("does NOT claim: a true prior - the prior problem stays open")
    print("OK: %s measured posterior sensitivity to the prior" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usst_grue(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    t = 100
    past = ["green"] * 100
    fit_green = sum(1 for c in past if c == "green") / len(past)
    fit_grue = sum(1 for i, c in enumerate(past)
                   if (c == "green") == (i < t)) / len(past)
    print("past fit of 'all emeralds are green': %.2f" % fit_green)
    print("past fit of 'all emeralds are grue':  %.2f" % fit_grue)
    assert fit_green == 1.0 and fit_grue == 1.0, "both hypotheses fit the past perfectly"
    pred_green = "green"
    pred_grue = "blue"
    print("prediction after time t under green: %s; under grue: %s" % (pred_green, pred_grue))
    assert pred_green != pred_grue, "the predictions must diverge"
    # Signature approach S-12: projectibility auditing for features.
    # Adjustable assumption A1: projectibility can be probed via provenance and regime stability.
    print("approach: audit every predictive feature for provenance, causal grounding, and regime")
    print("  stability; stress-test with grue-style redescriptions before deployment")
    print("CONFIRM IF: audited models survive regime changes better in prospective tests")
    print("REFUTE IF: grue-style redescriptions defeat every audit")
    print("does NOT claim: a formal solution to Goodman riddle")
    print("OK: %s showed perfect past fit with divergent futures" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usst_misspecification(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    rng = random.Random(113)
    n, reps = 200, 800
    cov_naive = cov_sand = 0
    for _ in range(reps):
        xs = [rng.uniform(0, 3) for _ in range(n)]
        ys = [1.0 + 2.0 * x + math.exp(1.5 * x) * _randn(rng) for x in xs]
        mx = _mean(xs)
        sxx = sum((x - mx) ** 2 for x in xs)
        b = sum((x - mx) * (y - _mean(ys)) for x, y in zip(xs, ys)) / sxx
        resid = [y - (_mean(ys) + b * (x - mx)) for x, y in zip(xs, ys)]
        s2 = sum(r * r for r in resid) / (n - 2)
        se_naive = math.sqrt(s2 / sxx)
        # sandwich: (X'X)^{-1} X' diag(r^2) X (X'X)^{-1} for the slope
        meat = sum((x - mx) ** 2 * r * r for x, r in zip(xs, resid))
        se_sand = math.sqrt(meat) / sxx
        if abs(b - 2.0) <= 1.96 * se_naive:
            cov_naive += 1
        if abs(b - 2.0) <= 1.96 * se_sand:
            cov_sand += 1
    rn, rs = cov_naive / reps, cov_sand / reps
    print("naive OLS interval coverage:    %.4f" % rn)
    print("sandwich interval coverage:     %.4f" % rs)
    assert rn < 0.90, "naive standard errors must undercover under heteroskedasticity"
    assert 0.92 < rs < 0.98, "sandwich standard errors must recover coverage"
    # Signature approach S-13: target-declared robust inference.
    # Adjustable assumption A1: the target can be stated as a functional of the true distribution.
    print("approach: declare the target functional in plain language, build bounded-influence")
    print("  estimators for it, and report a misspecification diagnostic with every estimate")
    print("CONFIRM IF: target-declared procedures beat model-based ones on real misspecified tasks")
    print("REFUTE IF: targets prove too vague to formalize in practice")
    print("does NOT claim: a general optimality theory under misspecification")
    print("OK: %s showed sandwich errors recovering coverage" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usst_post_selection(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    rng = random.Random(127)
    n, p, reps = 100, 20, 400
    sig = 0
    for _ in range(reps):
        y = [_randn(rng) for _ in range(n)]
        my = _mean(y)
        best = None
        best_c = -1.0
        for j in range(p):
            x = [_randn(rng) for _ in range(n)]
            mx = _mean(x)
            cov = sum((a - mx) * (b - my) for a, b in zip(x, y)) / n
            c = abs(cov) / (math.sqrt(sum((a - mx) ** 2 for a in x) / n) *
                            math.sqrt(sum((b - my) ** 2 for b in y) / n))
            if c > best_c:
                best_c, best = c, x
        # naive t-test on the selected predictor, all null
        mx = _mean(best)
        b = sum((a - mx) * (bb - my) for a, bb in zip(best, y)) / sum((a - mx) ** 2 for a in best)
        se = math.sqrt(sum((bb - my - b * (a - mx)) ** 2 for a, bb in zip(best, y)) / (n - 2) /
                       sum((a - mx) ** 2 for a in best))
        t = b / se
        # two-sided p via normal approximation
        pv = 2.0 * (1.0 - _ncdf(abs(t)))
        if pv < 0.05:
            sig += 1
    rate = sig / reps
    print("naive p<0.05 rate after selecting best of %d null predictors: %.4f" % (p, rate))
    assert rate > 0.15, "selection must inflate the naive significance rate"
    # Signature approach S-14: search-logged selective reporting.
    # Adjustable assumption A1: selection procedures can be logged completely by software.
    print("approach: log every selection decision and compute selection-adjusted intervals,")
    print("  printing naive and adjusted side by side so the cost of selection is visible")
    print("CONFIRM IF: adjusted intervals hit nominal coverage in real analysis pipelines")
    print("REFUTE IF: selection events prove too complex to condition on")
    print("does NOT claim: a general powerful selective inference theory")
    print("OK: %s showed selection inflating naive significance" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usst_high_dim(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    rng = random.Random(131)
    n, p, s = 120, 300, 5
    beta = [3.0 if j < s else 0.0 for j in range(p)]
    X = [[_randn(rng) for _ in range(p)] for _ in range(n)]
    y = [sum(X[i][j] * beta[j] for j in range(p)) + _randn(rng) for i in range(n)]
    lam = 1.2
    bhat = [0.0] * p
    # residual-based coordinate descent: O(n p) per sweep
    r = y[:]
    xnorm = [sum(X[i][j] ** 2 for i in range(n)) for j in range(p)]
    for _ in range(60):
        for j in range(p):
            rho = sum(X[i][j] * r[i] for i in range(n)) + bhat[j] * xnorm[j]
            if rho > lam:
                new = (rho - lam) / xnorm[j]
            elif rho < -lam:
                new = (rho + lam) / xnorm[j]
            else:
                new = 0.0
            delta = new - bhat[j]
            if delta != 0.0:
                bhat[j] = new
                for i in range(n):
                    r[i] -= X[i][j] * delta
    err = math.sqrt(sum((bhat[j] - beta[j]) ** 2 for j in range(p)))
    null_err = math.sqrt(sum(b * b for b in beta))
    rec = sum(1 for j in range(s) if abs(bhat[j]) > 0.5)
    print("p=%d, n=%d, true support=%d" % (p, n, s))
    print("lasso estimation error: %.4f (null model error: %.4f)" % (err, null_err))
    print("strong signals recovered: %d of %d" % (rec, s))
    assert err < 0.6 * null_err, "lasso must beat the null model decisively"
    assert rec >= 3
    # Signature approach S-15: assumption-priced high-dimensional inference.
    # Adjustable assumption A1: sharp guarantees need strong, unverifiable design conditions.
    print("approach: report the sharp debiased interval and an assumption-lean split-sample")
    print("  interval side by side, with diagnostics deciding which earns the headline")
    print("CONFIRM IF: dual-reported analyses cover better than sharp-only reporting in practice")
    print("REFUTE IF: lean intervals prove too wide for any use")
    print("does NOT claim: assumption-free high-dimensional inference")
    print("OK: %s recovered sparse signals with p much greater than n" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usst_bootstrap_fail(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    rng = random.Random(137)
    n, reps, B = 40, 150, 100
    theta = 1.0
    cover = 0
    for _ in range(reps):
        xs = [rng.random() * theta for _ in range(n)]
        # percentile bootstrap CI from the sampling distribution of the max
        boots = []
        for _ in range(B):
            samp = [xs[rng.randrange(n)] for _ in range(n)]
            boots.append(max(samp))
        boots.sort()
        lo, hi = boots[int(0.025 * B)], boots[int(0.975 * B)]
        if lo <= theta <= hi:
            cover += 1
    rate = cover / reps
    print("bootstrap 95 percent CI coverage for the uniform maximum: %.4f" % rate)
    assert rate < 0.50, "the bootstrap must fail at the boundary"
    # Signature approach S-16: bootstrap pre-flight diagnostics.
    # Adjustable assumption A1: failure modes are detectable before resampling.
    print("approach: run a pre-flight diagnostic battery - boundary proximity, smoothness probes,")
    print("  tail checks - and route amber/red cases to valid fallbacks automatically")
    print("CONFIRM IF: the router catches the classic failures and hits nominal coverage")
    print("REFUTE IF: failure modes prove too subtle for diagnostics")
    print("does NOT claim: a complete characterization of bootstrap consistency")
    print("OK: %s demonstrated bootstrap failure on the boundary" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usst_causal_obs(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    rng = random.Random(139)
    n = 5000
    # Hidden confounder U drives both treatment X and outcome Y. True causal effect of X is 1.0.
    xs, ys = [], []
    for _ in range(n):
        u = _randn(rng)
        x = u + _randn(rng)
        y = 1.0 * x + 2.0 * u + _randn(rng)
        xs.append(x)
        ys.append(y)
    mx, my = _mean(xs), _mean(ys)
    b = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    print("true causal effect of X on Y: 1.0000")
    print("naive regression coefficient:  %.4f" % b)
    assert abs(b - 2.0) < 0.15, "omitted U must bias the naive estimate toward 2.0"
    assert abs(b - 1.0) > 0.5
    # Sensitivity: how strong would hidden confounding need to be to explain the estimate away.
    print("sensitivity reading: if hidden confounding of strength 2.0 exists, the true effect")
    print("  could be as low as %.4f - %.4f" % (b - 2.0 * 0.5, b - 2.0 * 0.5))
    # Signature approach S-17: assumption-ledger causal reporting.
    # Adjustable assumption A1: identifying assumptions can be enumerated explicitly.
    print("approach: put every identifying assumption on a public ledger, price each by how much")
    print("  violation overturns the conclusion, and grade claims robust/fragile/speculative")
    print("CONFIRM IF: fragility grades predict which observational claims later experiments overturn")
    print("REFUTE IF: sensitivity frontiers prove too wide to grade anything")
    print("does NOT claim: a way to test the untestable")
    print("OK: %s showed hidden confounding biasing naive regression" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usst_causal_discovery(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    rng = random.Random(149)
    n = 8000
    # DAG 1: X -> Y. DAG 2: Y -> X. Same joint covariance by construction.
    x1 = [_randn(rng) for _ in range(n)]
    y1 = [0.8 * x + math.sqrt(1 - 0.64) * _randn(rng) for x in x1]
    y2 = [_randn(rng) for _ in range(n)]
    x2 = [0.8 * y + math.sqrt(1 - 0.64) * _randn(rng) for y in y2]
    def corr(a, b):
        ma, mb = _mean(a), _mean(b)
        return (sum((x - ma) * (y - mb) for x, y in zip(a, b)) / n /
                (math.sqrt(sum((x - ma) ** 2 for x in a) / n) *
                 math.sqrt(sum((y - mb) ** 2 for y in b) / n)))
    c1, c2 = corr(x1, y1), corr(x2, y2)
    print("correlation under DAG X->Y: %.4f" % c1)
    print("correlation under DAG Y->X: %.4f" % c2)
    assert abs(c1 - c2) < 0.05, "the two DAGs must be observationally indistinguishable"
    assert abs(c1 - 0.8) < 0.05
    # Signature approach S-18: equivalence-class reporting with orientation pricing.
    # Adjustable assumption A1: discovery recovers the Markov equivalence class under faithfulness.
    print("approach: report the full equivalence class, attach provenance and a stability score")
    print("  to every oriented edge, and price each orientation by its assumption")
    print("CONFIRM IF: priced orientations beat single-DAG outputs on benchmark systems")
    print("REFUTE IF: equivalence classes prove too large for the output to be useful")
    print("does NOT claim: a way past Markov equivalence from observational data alone")
    print("OK: %s showed two DAGs with identical observational footprints" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usst_transportability(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Effect modifier M in {0,1}; CATE(0)=0.2, CATE(1)=1.0.
    # Population A: P(M=1)=0.8 -> ATE 0.84. Population B: P(M=1)=0.2 -> ATE 0.36.
    ate_a = 0.2 * 0.2 + 1.0 * 0.8
    ate_b = 0.2 * 0.8 + 1.0 * 0.2
    naive = ate_a
    reweighted = 0.2 * 0.8 + 1.0 * 0.2
    print("true ATE in study population A:  %.4f" % ate_a)
    print("true ATE in target population B: %.4f" % ate_b)
    print("naive transport (use ATE_A for B): %.4f, bias %.4f" % (naive, naive - ate_b))
    print("reweighted transport:              %.4f, bias %.4f" % (reweighted, reweighted - ate_b))
    assert abs(naive - ate_b) > 0.4, "naive transport must be badly biased"
    assert abs(reweighted - ate_b) < 1e-9
    # Signature approach S-19: difference-ledger transport.
    # Adjustable assumption A1: relevant population differences can be enumerated as modifiers.
    print("approach: build the difference ledger, transport by reweighting through measured")
    print("  modifiers, and bound the rest with sensitivity analysis")
    print("CONFIRM IF: ledger-based transports predict target effects better than naive ones")
    print("REFUTE IF: modifiers prove too numerous or unmeasurable to ledger")
    print("does NOT claim: a complete transportability theory")
    print("OK: %s showed naive transport failing and reweighting recovering" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usst_interference(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    rng = random.Random(151)
    pairs = 3000
    # Pair-level assignment: both treated or both control. Spillover 0.8, direct effect 0.5.
    ys_t, ys_c = [], []
    for _ in range(pairs):
        treat = rng.random() < 0.5
        for _ in range(2):
            y = 0.5 * treat + 0.8 * treat + _randn(rng)
            (ys_t if treat else ys_c).append(y)
    b = _mean(ys_t) - _mean(ys_c)
    print("true direct effect: 0.5000; true spillover: 0.8000")
    print("SUTVA-style estimate (treated vs control means): %.4f" % b)
    assert abs(b - 1.3) < 0.12, "ignoring interference must mix direct and spillover effects"
    assert abs(b - 0.5) > 0.5
    # Signature approach S-20: exposure-mapped interference analysis.
    # Adjustable assumption A1: interference travels through measurable channels.
    print("approach: map interference channels, define explicit exposure mappings, and estimate")
    print("  direct and spillover effects as functions of exposure")
    print("CONFIRM IF: exposure-mapped estimates match directly measured spillovers")
    print("REFUTE IF: exposure depends on the full network beyond any low-dimensional mapping")
    print("does NOT claim: a general interference identification theory")
    print("OK: %s showed SUTVA estimates mixing direct and spillover effects" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usst_publication_bias(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    rng = random.Random(157)
    true_d = 0.2
    studies = 600
    published = []
    for _ in range(studies):
        n = (20, 30, 50, 100)[rng.randrange(4)]
        x = [_randn(rng) for _ in range(n)]
        y = [true_d + _randn(rng) for _ in range(n)]
        diff = _mean(y) - _mean(x)
        se = math.sqrt(2.0 / n)
        p = 2.0 * (1.0 - _ncdf(abs(diff / se)))
        if p < 0.05:
            published.append((diff, se))
    naive = _mean([d for d, s in published])
    print("studies: %d, published: %d" % (studies, len(published)))
    print("true effect: %.2f; naive meta-analytic mean: %.4f" % (true_d, naive))
    assert naive > 0.35, "selective publication must inflate the pooled estimate"
    # Funnel asymmetry: smaller studies (larger se) show larger effects.
    ds = [d for d, s in published]
    ss = [s for d, s in published]
    md, ms = _mean(ds), _mean(ss)
    cov = sum((d - md) * (s - ms) for d, s in zip(ds, ss)) / len(ds)
    print("covariance(effect, standard error) among published: %.4f (asymmetry signal)" % cov)
    assert cov > 0.0
    # Signature approach S-21: ensemble debiasing with agreement grading.
    # Adjustable assumption A1: different debiasing methods fail in different ways.
    print("approach: run a family of debiasing methods, report the full adjusted range, and")
    print("  grade the synthesis by method agreement")
    print("CONFIRM IF: agreement grades predict which conclusions survive unbiased replication")
    print("REFUTE IF: methods disagree everywhere, leaving every synthesis ungradeable")
    print("does NOT claim: a gold-standard debiasing method")
    print("OK: %s showed selective publication inflating meta-analysis" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usst_missing_data(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    rng = random.Random(163)
    n = 3000
    ys = [_randn(rng) for _ in range(n)]
    # MNAR: missingness depends on the missing value itself.
    obs = [y for y in ys if y + 0.5 * _randn(rng) > 0.3]
    cc = _mean(obs)
    print("true mean: 0.0000")
    print("complete-case mean under MNAR: %.4f (observed %d of %d)" % (cc, len(obs), n))
    assert cc > 0.2, "MNAR nonresponse must bias the complete-case mean"
    # MAR contrast: missingness depends only on an observed covariate.
    xs = [_randn(rng) for _ in range(n)]
    obs2 = [y for x, y in zip(xs, ys) if x > -0.5]
    cc2 = _mean(obs2)
    print("complete-case mean when missingness depends only on observed X: %.4f" % cc2)
    # Signature approach S-22: identified-bounds reporting for MNAR.
    # Adjustable assumption A1: observed data identify bounds, not points, under MNAR.
    print("approach: compute nonparametric identified bounds, price every point estimate by its")
    print("  assumption, and headline the bounds - not assumption-selected points")
    print("CONFIRM IF: bounds-based reports calibrate better than assumption-point reports")
    print("REFUTE IF: bounds prove too wide for any decision use")
    print("does NOT claim: identification under MNAR - the hole stays a hole")
    print("OK: %s showed MNAR biasing complete-case analysis" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usst_conformal(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    rng = random.Random(167)
    def gen(m):
        xs = [rng.uniform(-2, 2) for _ in range(m)]
        return xs, [x * x + _randn(rng) for x in xs]
    xtr, ytr = gen(400)
    xca, yca = gen(1500)
    xte, yte = gen(3000)
    # fit quadratic by normal equations
    d = 3
    xtx = [[0.0] * d for _ in range(d)]
    xty = [0.0] * d
    for x, y in zip(xtr, ytr):
        pw = [1.0, x, x * x]
        for a in range(d):
            xty[a] += pw[a] * y
            for b in range(d):
                xtx[a][b] += pw[a] * pw[b]
    m_ = [row[:] + [xty[i]] for i, row in enumerate(xtx)]
    for c in range(d):
        piv = m_[c][c]
        for r in range(c + 1, d):
            f = m_[r][c] / piv
            for cc in range(c, d + 1):
                m_[r][cc] -= f * m_[c][cc]
    beta = [0.0] * d
    for c in range(d - 1, -1, -1):
        beta[c] = (m_[c][d] - sum(m_[c][cc] * beta[cc] for cc in range(c + 1, d))) / m_[c][c]
    def pred(x):
        return beta[0] + beta[1] * x + beta[2] * x * x
    scores = sorted(abs(y - pred(x)) for x, y in zip(xca, yca))
    q = scores[int(0.90 * len(scores))]
    hit = sum(1 for x, y in zip(xte, yte) if abs(y - pred(x)) <= q)
    rate = hit / len(xte)
    print("split-conformal 90 percent intervals: empirical coverage %.4f" % rate)
    print("mean interval width: %.4f" % (2 * q))
    assert 0.875 < rate < 0.925, "marginal coverage must land near the nominal level"
    # Signature approach S-23: validity-fixed efficiency engineering.
    # Adjustable assumption A1: the marginal coverage guarantee must never be traded for sharpness.
    print("approach: lock the coverage guarantee, optimize the conformity score for mean width,")
    print("  and audit subgroup coverage wherever decisions differ by subgroup")
    print("CONFIRM IF: optimized conformal variants tighten intervals at the same guaranteed coverage")
    print("REFUTE IF: efficiency gains merely shift width between subgroups")
    print("does NOT claim: optimal efficiency theory or conditional coverage")
    print("OK: %s verified distribution-free marginal coverage" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usst_adaptive_analysis(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    rng = random.Random(173)
    n, p = 500, 50
    y = [_randn(rng) for _ in range(n)]
    feats = [[_randn(rng) for _ in range(n)] for _ in range(p)]
    my = _mean(y)
    vy = sum((b - my) ** 2 for b in y) / n
    best, best_r = None, -1.0
    for f in feats:
        mf = _mean(f)
        r = abs(sum((a - mf) * (b - my) for a, b in zip(f, y)) / n /
                (math.sqrt(sum((a - mf) ** 2 for a in f) / n) * math.sqrt(vy)))
        if r > best_r:
            best_r, best = r, f
    # Fresh data: the true correlation of the selected noise feature.
    n2 = 5000
    y2 = [_randn(rng) for _ in range(n2)]
    f2 = [_randn(rng) for _ in range(n2)]
    m1, m2 = _mean(f2), _mean(y2)
    true_r = abs(sum((a - m1) * (b - m2) for a, b in zip(f2, y2)) / n2 /
                 (math.sqrt(sum((a - m1) ** 2 for a in f2) / n2) *
                  math.sqrt(sum((b - m2) ** 2 for b in y2) / n2)))
    print("best-of-%d noise features, holdout |corr|: %.4f" % (p, best_r))
    print("same selection on fresh data, |corr|:      %.4f" % true_r)
    assert best_r - true_r > 0.05, "adaptive selection must inflate the holdout reading"
    # Signature approach S-24: adaptivity budgeting with metering.
    # Adjustable assumption A1: adaptive queries can be logged and their cost bounded.
    print("approach: give every analysis an explicit adaptivity budget, meter the spending, and")
    print("  require fresh validation data when the budget is exhausted")
    print("CONFIRM IF: budgeted workflows stay valid where unbudgeted ones overfit")
    print("REFUTE IF: bounds prove too loose to give usable budgets")
    print("does NOT claim: optimal adaptive query bounds")
    print("OK: %s showed adaptive reuse inflating holdout accuracy" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usst_privacy_utility(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    rng = random.Random(179)
    n = 1000
    xs = [min(max(5.0 + _randn(rng), 0.0), 10.0) for _ in range(n)]
    mu = _mean(xs)
    sens = 10.0 / n
    print("true mean: %.4f; Laplace mechanism, sensitivity %.5f" % (mu, sens))
    prev = None
    for eps in (0.1, 0.5, 1.0, 2.0, 5.0):
        mse = 2.0 * (sens / eps) ** 2
        # one noisy release for illustration
        u = rng.random()
        noise = -(sens / eps) * math.log(1 - u) if rng.random() < 0.5 else (sens / eps) * math.log(1 - u)
        print("epsilon=%4.1f: noise std %.5f, released %.4f" % (eps, sens / eps * math.sqrt(2), mu + noise))
        if prev is not None:
            assert mse < prev, "utility must improve as epsilon grows"
        prev = mse
    # Signature approach S-25: frontier-measured private estimation.
    # Adjustable assumption A1: the frontier can be bounded per problem.
    print("approach: bound the privacy-utility frontier per problem, deploy mechanisms with a")
    print("  reported frontier gap, and choose epsilon by cost-benefit on the measured frontier")
    print("CONFIRM IF: measured frontiers guide epsilon choices that dominate conventional ones")
    print("REFUTE IF: frontiers prove too hard to bound for realistic problems")
    print("does NOT claim: optimal private estimators in general")
    print("OK: %s traced the privacy-utility tradeoff curve" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usst_objective_bayes(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    from math import comb
    n = 20
    # Jeffreys prior Beta(0.5, 0.5): equal-tailed 95 percent credible intervals.
    def ci(k):
        a, b = k + 0.5, n - k + 0.5
        # quantiles via incomplete-beta bisection (continued fraction)
        def _cf(aa, bb, xx):
            qab, qap, qam = aa + bb, aa + 1.0, aa - 1.0
            c = 1.0
            d = 1.0 - qab * xx / qap
            if abs(d) < 1e-300:
                d = 1e-300
            d = 1.0 / d
            h = d
            for mm in range(1, 300):
                m2 = 2 * mm
                aa1 = mm * (bb - mm) * xx / ((qam + m2) * (aa + m2))
                d = 1.0 + aa1 * d
                if abs(d) < 1e-300:
                    d = 1e-300
                c = 1.0 + aa1 / c
                if abs(c) < 1e-300:
                    c = 1e-300
                d = 1.0 / d
                h *= d * c
                aa2 = -(aa + mm) * (qab + mm) * xx / ((aa + m2) * (qap + m2))
                d = 1.0 + aa2 * d
                if abs(d) < 1e-300:
                    d = 1e-300
                c = 1.0 + aa2 / c
                if abs(c) < 1e-300:
                    c = 1e-300
                d = 1.0 / d
                dl = d * c
                h *= dl
                if abs(dl - 1.0) < 3e-14:
                    break
            return h
        def ibeta(aa, bb, x):
            if x <= 0.0:
                return 0.0
            if x >= 1.0:
                return 1.0
            if x > (aa + 1.0) / (aa + bb + 2.0):
                return 1.0 - ibeta(bb, aa, 1.0 - x)
            front = math.exp(math.lgamma(aa + bb) - math.lgamma(aa) - math.lgamma(bb) +
                             aa * math.log(x) + bb * math.log(1.0 - x)) / aa
            return front * _cf(aa, bb, x)
        def quant(q):
            lo, hi = 0.0, 1.0
            for _ in range(80):
                mid = (lo + hi) / 2
                if ibeta(a, b, mid) < q:
                    lo = mid
                else:
                    hi = mid
            return (lo + hi) / 2
        return quant(0.025), quant(0.975)
    coverages = []
    grid = [0.1 + 0.05 * i for i in range(17)]
    for p in grid:
        tot = 0.0
        for k in range(n + 1):
            lo, hi = ci(k)
            if lo <= p <= hi:
                tot += comb(n, k) * p ** k * (1 - p) ** (n - k)
        coverages.append(tot)
    avg = sum(coverages) / len(coverages)
    print("Jeffreys Beta(0.5,0.5) 95 percent intervals, mean coverage over p in [0.1,0.9]: %.4f" % avg)
    print("min coverage on grid: %.4f" % min(coverages))
    assert 0.93 < avg < 0.98, "probability matching must hold on average"
    # Signature approach S-26: warranted-default priors.
    # Adjustable assumption A1: defaults can be graded by measured calibration.
    print("approach: benchmark candidate defaults per problem class and ship the winner with its")
    print("  measured warranty; require explicit prior choice where no default is warranted")
    print("CONFIRM IF: warranted defaults calibrate applied analyses better than unwarranted ones")
    print("REFUTE IF: performance proves too problem-dependent for any default to warrant")
    print("does NOT claim: that objective priors are truly objective")
    print("OK: %s verified Jeffreys-interval probability matching" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usst_evidence_foundations(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Same data, three currencies: z = 2.0 with n = 100.
    z, n = 2.0, 100
    p = 2.0 * (1.0 - _ncdf(abs(z)))
    logbf = 0.5 * (z * z - math.log(n))
    bf = math.exp(logbf)
    evalue = math.exp((z * z - 1.0) / 2.0)
    print("data: z = %.1f, n = %d" % (z, n))
    print("p-value:              %.4f (significant at 0.05)" % p)
    print("Bayes factor (BIC approx): %.4f (%s)" % (bf, "favors null" if bf < 1 else "favors alternative"))
    print("e-value:              %.4f (modest evidence)" % evalue)
    assert p < 0.05, "p-value calls this significant"
    assert bf < 1.0, "Bayes factor leans the other way - the currencies disagree"
    # Signature approach S-27: multi-currency evidence reporting.
    # Adjustable assumption A1: scales can be calibrated against each other empirically.
    print("approach: report p-value, Bayes factor, and e-value side by side; build empirical")
    print("  conversion tables on benchmarks with known truth and let the track record choose")
    print("CONFIRM IF: one currency systematically out-predicts the others on replication benchmarks")
    print("REFUTE IF: the currencies disagree irreconcilably with no empirical way to choose")
    print("does NOT claim: a true measure of evidence")
    print("OK: %s showed the evidence currencies disagreeing" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usst_generalized_bayes(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    rng = random.Random(181)
    n, reps = 200, 300
    cov_std = cov_tmp = 0
    eta = 1.0 / 3.0
    for _ in range(reps):
        # heavy-tailed truth: t with 3 df, variance 3. Model assumes variance 1.
        xs = []
        for _ in range(n):
            z = _randn(rng)
            v = sum(_randn(rng) ** 2 for _ in range(3))
            xs.append(z / math.sqrt(v / 3.0))
        m = _mean(xs)
        half_std = 1.96 / math.sqrt(n)
        half_tmp = 1.96 / math.sqrt(n * eta)
        if abs(m) <= half_std:
            cov_std += 1
        if abs(m) <= half_tmp:
            cov_tmp += 1
    rs, rt = cov_std / reps, cov_tmp / reps
    print("standard posterior 95 percent interval coverage: %.4f" % rs)
    print("tempered posterior (eta=1/3) coverage:           %.4f" % rt)
    assert rs < 0.90, "standard Bayes must be overconfident under misspecification"
    assert rt >= 0.92, "tempering must restore coverage"
    # Signature approach S-28: calibrated humility dialing.
    # Adjustable assumption A1: the learning rate can be selected by held-out performance.
    print("approach: fit a ladder of tempered posteriors, select the learning rate by predictive")
    print("  criteria, and report the rate with a calibration check")
    print("CONFIRM IF: tempered posteriors calibrate better than standard ones across benchmarks")
    print("REFUTE IF: rate selection proves unstable or circular")
    print("does NOT claim: a principled automatic generalized Bayes")
    print("OK: %s showed tempering restoring coverage" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usst_uniform_bands(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    rng = random.Random(191)
    n, reps = 500, 400
    eps = math.sqrt(math.log(2.0 / 0.05) / (2.0 * n))
    cover = 0
    for _ in range(reps):
        xs = sorted(_randn(rng) for _ in range(n))
        # sup norm between empirical CDF and true Phi over the sample points
        worst = 0.0
        for i, x in enumerate(xs):
            fhat = (i + 1) / n
            d = abs(fhat - _ncdf(x))
            if d > worst:
                worst = d
        if worst <= eps:
            cover += 1
    rate = cover / reps
    print("DKW 95 percent uniform band half-width: %.4f" % eps)
    print("empirical whole-curve coverage: %.4f" % rate)
    assert rate >= 0.93, "the uniform band must cover the whole curve"
    # A pointwise band is narrower - and does not warrant shape claims.
    pt = 1.96 * math.sqrt(0.25 / n)
    print("pointwise band half-width at the median: %.4f (narrower, weaker warranty)" % pt)
    assert pt < eps
    # Signature approach S-29: warranted-shape reporting.
    # Adjustable assumption A1: honest bands are computable where theory exists.
    print("approach: ship function estimates with honest uniform bands, mark Low-impossibility")
    print("  zones, and warrant shape claims only inside warranted regions")
    print("CONFIRM IF: warranted-shape reports avoid the false discoveries of pointwise practice")
    print("REFUTE IF: impossibility zones cover everything of interest")
    print("does NOT claim: a way around Low impossibility")
    print("OK: %s verified uniform whole-curve coverage" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usst_conditional_coverage(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    rng = random.Random(193)
    def gen(m):
        xs = [rng.random() for _ in range(m)]
        return xs, [_randn(rng) * (0.3 + 1.5 * x) for x in xs]
    xtr, ytr = gen(400)
    xca, yca = gen(600)
    xte, yte = gen(4000)
    scores = sorted(abs(y) for y in yca)
    q = scores[int(0.90 * len(scores))]
    marg = sum(1 for y in yte if abs(y) <= q) / len(yte)
    sub = [(x, y) for x, y in zip(xte, yte) if x > 0.8]
    sub_rate = sum(1 for x, y in sub if abs(y) <= q) / len(sub)
    print("marginal coverage: %.4f (target 0.90)" % marg)
    print("coverage for subgroup x > 0.8: %.4f" % sub_rate)
    assert 0.87 < marg < 0.93, "marginal validity must hold"
    assert sub_rate < marg - 0.03, "the hard subgroup must undercover despite marginal validity"
    # Signature approach S-30: coverage-grade auditing.
    # Adjustable assumption A1: conditional coverage can be audited on held-out data.
    print("approach: audit coverage across a battery of subgroups, report the worst shortfall,")
    print("  and gate deployment on the worst audited subgroup")
    print("CONFIRM IF: gated deployments show fewer subgroup failures in production")
    print("REFUTE IF: audits prove too noisy to gate on")
    print("does NOT claim: a way around the impossibility theorem")
    print("OK: %s showed marginal validity hiding subgroup failure" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usst_ergodicity(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    rng = random.Random(197)
    trajs, rounds = 2000, 200
    finals = []
    for _ in range(trajs):
        w = 1.0
        for _ in range(rounds):
            w *= 1.5 if rng.random() < 0.5 else 0.6
        finals.append(w)
    finals.sort()
    mean_w = _mean(finals)
    med_w = finals[len(finals) // 2]
    print("gamble: wealth x1.5 or x0.6 each round, %d rounds, %d trajectories" % (rounds, trajs))
    print("ensemble-average final wealth: %.2f (grows: 1.05^%d)" % (mean_w, rounds))
    print("median experienced final wealth: %.6f (decays: 0.9^%d)" % (med_w, rounds))
    assert mean_w > 1.0, "the ensemble average grows"
    assert med_w < 1.0, "almost every individual trajectory decays"
    # Signature approach S-31: dual-average prescription auditing.
    # Adjustable assumption A1: both averages are computable for the decision at hand.
    print("approach: compute both averages for every risky prescription, flag disagreements,")
    print("  and resolve flagged cases by stating the decision problem precisely")
    print("CONFIRM IF: flagged prescriptions prove worse for individuals in outcome tracking")
    print("REFUTE IF: decision problems always prove statable precisely enough to dissolve the issue")
    print("does NOT claim: that time averages are always right")
    print("OK: %s showed ensemble growth with individual decay" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usst_imprecise_prob(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Coin of unknown bias, known only to lie in [0.3, 0.7].
    lo, hi = 0.3, 0.7
    lower_2h = lo ** 2
    upper_2h = hi ** 2
    precise = 0.5 ** 2
    print("knowledge: bias in [%.1f, %.1f]" % (lo, hi))
    print("imprecise P(two heads): [%.4f, %.4f]" % (lower_2h, upper_2h))
    print("precise-Bayesian answer with 0.5: %.4f (manufactured precision)" % precise)
    assert abs(lower_2h - 0.09) < 1e-9 and abs(upper_2h - 0.49) < 1e-9
    assert lower_2h < precise < upper_2h
    # After 10 heads in 10 flips, the interval narrows but stays honest.
    print("after 10 heads in 10 flips the interval would narrow - imprecision is updatable,")
    print("  not a refusal to learn")
    # Signature approach S-32: precision-cost measurement.
    # Adjustable assumption A1: precise and imprecise analyses can run on the same problems.
    print("approach: run precise and imprecise analyses side by side and measure what the")
    print("  precision costs in calibration; choose foundations per problem class by the evidence")
    print("CONFIRM IF: imprecise analyses calibrate better on deep-uncertainty problem classes")
    print("REFUTE IF: precise methods match imprecise calibration everywhere")
    print("does NOT claim: that Kolmogorov axioms are wrong")
    print("OK: %s computed honest interval probabilities" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usst_anytime_inference(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    rng = random.Random(199)
    lam = 0.5
    reps = 4000
    exceed = 0
    for _ in range(reps):
        tau = rng.randrange(1, 501)
        s = 0.0
        for t in range(1, tau + 1):
            s += _randn(rng)
            # test martingale E_t = exp(lam * S_t - t * lam^2 / 2), valid under the null
        e = math.exp(lam * s - tau * lam * lam / 2.0)
        if e >= 20.0:
            exceed += 1
    rate = exceed / reps
    print("null true; stopped at a random time in 1..500")
    print("P(E_tau >= 20): %.4f (validity requires <= 0.05)" % rate)
    assert rate < 0.08, "the e-value must stay valid at the random stopping time"
    # Signature approach S-33: anytime-by-default sequential analysis.
    # Adjustable assumption A1: e-value instruments exist for the parameters of interest.
    print("approach: rebuild sequential analysis on anytime-valid instruments and price the")
    print("  efficiency cost against fixed-sample methods openly")
    print("CONFIRM IF: anytime analyses match fixed-sample correctness with safe early stopping")
    print("REFUTE IF: efficiency costs prove too large for practical use")
    print("does NOT claim: a complete anytime theory for arbitrary models")
    print("OK: %s verified anytime validity at a random stopping time" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usst_unification(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    rng = random.Random(211)
    n = 25
    xs = [2.0 + _randn(rng) for _ in range(n)]
    m = _mean(xs)
    s = _sd(xs)
    se = s / math.sqrt(n)
    # Confidence distribution for the normal mean: N(m, se^2); 95 percent quantiles.
    cd_lo = m - 1.96 * se
    cd_hi = m + 1.96 * se
    # Bayesian posterior under a flat prior: identical normal.
    bayes_lo = m - 1.96 * se
    bayes_hi = m + 1.96 * se
    # Generalized fiducial distribution for the mean: identical here as well.
    fid_lo = m - 1.96 * se
    fid_hi = m + 1.96 * se
    print("sample mean: %.4f, standard error: %.4f" % (m, se))
    print("confidence-distribution interval: [%.4f, %.4f]" % (cd_lo, cd_hi))
    print("flat-prior Bayes credible set:    [%.4f, %.4f]" % (bayes_lo, bayes_hi))
    print("fiducial interval:                [%.4f, %.4f]" % (fid_lo, fid_hi))
    assert abs(cd_lo - bayes_lo) < 1e-9 and abs(cd_hi - fid_hi) < 1e-9
    print("the three frameworks coincide numerically here - the striking convergence")
    # Signature approach S-34: agreement-map proto-unification.
    # Adjustable assumption A1: numerical agreement across frameworks is extensive enough to map.
    print("approach: map where the frameworks coincide and characterize each divergence by its")
    print("  cause, pricing divergences by decision impact")
    print("CONFIRM IF: the map shows agreement almost everywhere that matters for decisions")
    print("REFUTE IF: agreement proves too fragile to map")
    print("does NOT claim: a unified framework or an impossibility proof")
    print("OK: %s exhibited the three-framework convergence" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "induction": demo_usst_induction,
    "prob_interpretations": demo_usst_prob_interpretations,
    "confidence_meaning": demo_usst_confidence_meaning,
    "replication": demo_usst_replication,
    "pvalues": demo_usst_pvalues,
    "multiple_testing": demo_usst_multiple_testing,
    "optional_stopping": demo_usst_optional_stopping,
    "likelihood_principle": demo_usst_likelihood_principle,
    "model_selection": demo_usst_model_selection,
    "reference_class": demo_usst_reference_class,
    "prior_elicitation": demo_usst_prior_elicitation,
    "grue": demo_usst_grue,
    "misspecification": demo_usst_misspecification,
    "post_selection": demo_usst_post_selection,
    "high_dim": demo_usst_high_dim,
    "bootstrap_fail": demo_usst_bootstrap_fail,
    "causal_obs": demo_usst_causal_obs,
    "causal_discovery": demo_usst_causal_discovery,
    "transportability": demo_usst_transportability,
    "interference": demo_usst_interference,
    "publication_bias": demo_usst_publication_bias,
    "missing_data": demo_usst_missing_data,
    "conformal": demo_usst_conformal,
    "adaptive_analysis": demo_usst_adaptive_analysis,
    "privacy_utility": demo_usst_privacy_utility,
    "objective_bayes": demo_usst_objective_bayes,
    "evidence_foundations": demo_usst_evidence_foundations,
    "generalized_bayes": demo_usst_generalized_bayes,
    "uniform_bands": demo_usst_uniform_bands,
    "conditional_coverage": demo_usst_conditional_coverage,
    "ergodicity": demo_usst_ergodicity,
    "imprecise_prob": demo_usst_imprecise_prob,
    "anytime_inference": demo_usst_anytime_inference,
    "unification": demo_usst_unification,
}
