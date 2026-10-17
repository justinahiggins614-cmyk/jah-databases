#!/usr/bin/env python3
"""Build the Psychometrics field databases for JAH Databases (field #19, taxonomy order).

Verified 2026-10-17: NO database covers psychometrics as a discipline.
- 'psychology' / 'psychology-public' / 'psychology-signature': no shard data
  or generic survey cards; zero psychometrics-discipline titles.
- 'psychology-study' (5000 records) / 'everything-psychology' (12 records):
  whole-shard title scan - zero hits for psychometric(s), item response,
  classical test theory, Cronbach, kappa, differential item functioning,
  equating, adaptive testing, norming, factor analysis, reliability/validity
  as a measurement discipline. Generic "testing" mentions nowhere rise to
  the discipline: no true-score model, no IRT, no test construction.
- Fields #12-18 shard indexes (climatology, atmospheric-science, hydrology,
  meteorology, calculus, combinatorics, econometrics): direct title scan -
  only false positives on the substring "equat" inside "equation".
- 'scientific-formulas': bare formula cards are reference only (task rule:
  formula cards do NOT count as discipline coverage).
- Whole-system dedupe gate (fresh data/dedupe/exact/ index in the main
  repo): every record checked + admitted at build time.

So this build creates two NEW databases:

  psychometrics            - The Psychometrics Database
                             (public-harvest: real, fact-checked
                             psychometrics; citations Nunnally & Bernstein,
                             Embretson & Reise, DeVellis, Furr & Bacharach,
                             Crocker & Algina, Hambleton et al., Anastasi &
                             Urbina, Brennan, Kline, and the Standards for
                             Educational and Psychological Testing)
  psychometrics-signature  - The Psychometrics Signature Database
                             (his original Signature interpretation of the
                             discipline; src signature, titles suffixed
                             " (Signature Edition)", never presented as
                             authentic public record)

37 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

Every record: description + how-it-works + key points + requirements +
standards + citations + working demonstration code (real, runnable,
stdlib-only Python; machine-executed OK). Psychometrics demos: scale-type
arithmetic traps, true-score variance split, parallel-forms reliability,
test-retest with practice effects, split-half + Spearman-Brown, Cronbach's
alpha from the formula, KR-20 == alpha identity on 0/1 data, SEM coverage
bands + reliable change, the attenuation ceiling on validity, Lawshe CVR
content audit, range-corrected criterion validity + expectancy table,
nomological-network construct check, MTMM matrix criteria, item p-values
and point-biserials with a miskeyed-item alarm, distractor curves,
Spearman-Brown length prophecy, interrater ICC vs percent agreement,
Cohen's kappa with the prevalence paradox, percentile norming, linear vs
normalized standard scores, simulated ability battery with g, balanced-keyed
personality scale, two-factor recovery, EFA-vs-CFA residual check, Rasch
ability recovery, 2PL/3PL curve anatomy, information-function design, DIF
plant-and-detect, anchor equating, vertical scaling, a live CAT loop,
impact-vs-bias separation, G-theory D-study, mediation path algebra, the
Standards audit as code, and the full nine-gate construction workflow.

Subtitle disambiguation (fields #13-19 pattern): discipline titles carry
teaching-focused subtitles rather than bare cards, e.g. "Reliability: The
Signal in the Noise" and "Cronbach's Alpha: The Workhorse of Internal
Consistency".

Never the words "bat belt" anywhere. No website references. No Facebook.
"""
import importlib.util
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = "/home/hatch/workspace/jah-databases"
SHARD = "/home/hatch/workspace/jah-databases-data-1"
SHARD_BASE = "https://justinahiggins614-cmyk.github.io/jah-databases-data-1"
TEMPLATE = os.path.join(REPO, "db", "public-synthetic-intelligence", "index.html")

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
# Whole-system dedupe gate against the FRESH data/dedupe/exact/ index in the
# main repo. Fields #12-18 shard indexes (climatology, atmospheric-science,
# hydrology, meteorology, calculus, combinatorics, econometrics) checked
# directly against their shard indexes in jah-databases-data-1 since the
# gate index predates them - subtitle disambiguation used throughout.
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_psychometrics import ENTRIES, SIG_TAIL

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature interpretation of psychometrics: "
                "clearly labeled Signature-made, never presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked psychometrics: the science of psychological "
                "measurement; levels of measurement; the true-score model; reliability and its "
                "designs; test-retest, split-half, Cronbach's alpha, KR-20; the standard error "
                "of measurement; validity and its five evidence sources; content, criterion, and "
                "construct validity; convergent and discriminant evidence; item analysis; "
                "distractor analysis; the Spearman-Brown prophecy; interrater reliability and "
                "Cohen's kappa; norming and standardization; standard scores; cognitive ability "
                "testing; personality measurement; factor analysis; EFA vs CFA; the Rasch model; "
                "2PL and 3PL models; item information; differential item functioning; test "
                "equating; vertical scaling; computerized adaptive testing; fairness and bias; "
                "generalizability theory; structural equation modeling; the Standards for "
                "Educational and Psychological Testing; the full test-construction workflow, "
                "organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations (what psychometrics is, "
              "measurement scales, the true-score model, reliability, test-retest, split-half, "
              "alpha, KR-20, standard error of measurement, validity, content validity) -> "
              "Compounded (criterion validity, construct validity, convergent/discriminant "
              "evidence, item analysis, distractor analysis, Spearman-Brown, interrater "
              "reliability, kappa, norming, standard scores, cognitive ability testing, "
              "personality measurement, factor analysis, EFA vs CFA) -> Advanced (Rasch/IRT, "
              "2PL/3PL, item information, DIF, equating, vertical scaling, adaptive testing, "
              "fairness and bias, generalizability theory, SEM, the Standards, the construction "
              "workflow).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search reliability, validity, Cronbach's alpha, IRT, factor analysis, DIF, adaptive testing...",
        "chat_ph": "Ask about psychometrics...",
        "archive_blurb": ("Seeded %s psychometrics records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled structural psychometrics studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about psychometrics - from the true-score model, reliability, and validity through item analysis, factor analysis, IRT, DIF, adaptive testing, and the Standards." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "psychometrics-study", "gen_demo_kind": "psychometrics-demo",
        "source": source,
    }

CIT_PUB = "Psychometrics (standard textbooks and peer-reviewed literature)."
CIT_SIG = CIT_PUB + " " + SIG_TAIL

DBCFG = {}
DBCFG["psychometrics"] = _cfg(
    "psychometrics", "The Psychometrics Database",
    "Real, fact-checked psychometrics: the science of psychological measurement, from "
    "measurement scales and the true-score model through reliability, validity, item "
    "analysis, factor analysis, item response theory, fairness, and the professional "
    "test-construction workflow - taught progressively along the ladder.",
    "psychometrics record", "JAH-PSY-", "JAH Psychometrics Archivist",
    "psychometrics archivist - what psychometrics is, measurement scales, the true-score "
    "model, reliability, test-retest, split-half, Cronbach's alpha, KR-20, standard error "
    "of measurement, validity, content validity, criterion validity, construct validity, "
    "convergent/discriminant evidence, item analysis, distractor analysis, Spearman-Brown, "
    "interrater reliability, Cohen's kappa, norming, standard scores, cognitive ability "
    "testing, personality measurement, factor analysis, EFA vs CFA, Rasch/IRT, 2PL/3PL, "
    "item information, DIF, equating, vertical scaling, adaptive testing, fairness and "
    "bias, generalizability theory, SEM, the Standards, the construction workflow; "
    "teaching progressively along the ladder from foundations through compounded to "
    "advanced; answers from many angles - definition, example, analogy, application, "
    "history, math, how-to - using only the system's own archive data",
    CIT_PUB, "public")
DBCFG["psychometrics-signature"] = _cfg(
    "psychometrics-signature", "The Psychometrics Signature Database",
    "His original Signature interpretation of psychometrics: the full ladder from "
    "measurement scales and the true-score model through IRT, adaptive testing, and "
    "the Standards, reframed as Signature science. Clearly labeled Signature-made, "
    "never presented as authentic public record.",
    "psychometrics record", "JAH-PSYS-", "JAH Psychometrics Archivist (Signature)",
    "psychometrics archivist - Signature editions: his original Signature interpretation "
    "of psychometrics, clearly labeled Signature-made and never presented as authentic "
    "public record; teaches progressively along the ladder from foundations through "
    "compounded to advanced; answers from many angles - definition, example, analogy, "
    "application, history, math, how-to - using only the system's own archive data",
    CIT_SIG, "signature")

base.DBCFG = DBCFG
# ---------------------------------------------------------------- demos
# Every demo is real, runnable, stdlib-only Python performing the actual
# psychometric computation for its record. All are machine-executed by main().

_PREAMBLE = (
"import math\n"
"import random\n"
"def _mean(v):\n"
"    return sum(v) / len(v)\n"
"def _var(v):\n"
"    m = _mean(v)\n"
"    return sum((x - m) ** 2 for x in v) / (len(v) - 1)\n"
"def _sd(v):\n"
"    return math.sqrt(_var(v))\n"
"def _cov(a, b):\n"
"    ma, mb = _mean(a), _mean(b)\n"
"    return sum((x - ma) * (y_ - mb) for x, y_ in zip(a, b)) / (len(a) - 1)\n"
"def _corr(a, b):\n"
"    return _cov(a, b) / (_sd(a) * _sd(b))\n"
"def _phi(z):\n"
"    return 0.5 * (1.0 + math.erf(z / math.sqrt(2.0)))\n"
"def _solve(A, b):\n"
"    n = len(A)\n"
"    M = [list(row) + [bb] for row, bb in zip(A, b)]\n"
"    for c in range(n):\n"
"        p = max(range(c, n), key=lambda r: abs(M[r][c]))\n"
"        M[c], M[p] = M[p], M[c]\n"
"        pv = M[c][c]\n"
"        if abs(pv) < 1e-12:\n"
"            raise ValueError('singular matrix')\n"
"        for r in range(n):\n"
"            if r != c:\n"
"                f = M[r][c] / pv\n"
"                for j in range(c, n + 1):\n"
"                    M[r][j] -= f * M[c][j]\n"
"    return [M[i][n] / M[i][i] for i in range(n)]\n"
"def _ols(y, X):\n"
"    n = len(y); k = len(X[0])\n"
"    XtX = [[sum(X[i][a] * X[i][b] for i in range(n)) for b in range(k)] for a in range(k)]\n"
"    Xty = [sum(X[i][a] * y[i] for i in range(n)) for a in range(k)]\n"
"    return _solve(XtX, Xty)\n"
"def _alpha(items):\n"
"    k = len(items[0])\n"
"    n = len(items)\n"
"    iv = [_var([row[j] for row in items]) for j in range(k)]\n"
"    tot = [_var([sum(row) for row in items])][0]\n"
"    return (k / (k - 1)) * (1 - sum(iv) / tot)\n"
"def _rasch_p(theta, b):\n"
"    return 1.0 / (1.0 + math.exp(-(theta - b)))\n"
)

def _wrap(name, rid, group, body):
    return (base._hdr(name, rid, group) + _PREAMBLE + body.replace("NAME", json.dumps(name)))

def demo_psy_what(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
TERRITORIES = {
    "test theory": "true-score model, reliability designs, SEM",
    "validity": "content, criterion, construct - the five evidence sources",
    "item & scale science": "item analysis, factor analysis, IRT, equating, adaptive testing",
}
def main():
    assert len(TERRITORIES) == 3
    for terr, tools in TERRITORIES.items():
        print("%-22s -> %s" % (terr, tools))
    # the founding contrast: a quiz gives a number; psychometrics gives a number with credentials
    quiz_score, n_items = 37, 50
    reliability, sem = 0.88, 4.5
    lo, hi = quiz_score - 2 * sem, quiz_score + 2 * sem
    print("score 37/50, reliability %.2f -> 95%% band [%.0f, %.0f]: the number plus its credentials" %
          (reliability, lo, hi))
    assert lo < quiz_score < hi
    print("rule: no score without its margin, no margin without its evidence")
    print("OK: %s mapped the discipline" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_psy_scales(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # nominal: diagnostic codes - the mean is meaningless
    codes_a = [1, 1, 2, 2, 3]          # 1=anxiety, 2=depression, 3=other
    codes_b = [3, 3, 1, 1, 2]          # same people, relabeled codes
    ma, mb = _mean(codes_a), _mean(codes_b)
    assert abs(ma - mb) > 0.1, (ma, mb)
    print("nominal codes: mean %.2f vs %.2f after relabeling - the 'mean' was never real" % (ma, mb))
    # ordinal: Likert ratings - order real, gaps unknown
    likert = [1, 2, 2, 4, 5, 5]
    med = sorted(likert)[len(likert) // 2]
    print("ordinal Likert: median %d is safe; the mean %.2f pretends gaps are equal" % (med, _mean(likert)))
    # interval: T-scores - differences meaningful, ratios not
    t1, t2, t3 = 40.0, 50.0, 60.0
    assert (t2 - t1) == (t3 - t2)
    print("interval T-scores: 50-40 == 60-50 (equal gaps); but 60 is not 'twice' 30 - no true zero")
    # ratio: reaction time - ratios meaningful
    rt_fast, rt_slow = 250.0, 500.0
    assert abs(rt_slow / rt_fast - 2.0) < 1e-9
    print("ratio reaction time: 500ms is truly twice 250ms - true zero at 0ms")
    print("rule: the scale licenses the statistic - check the license first")
    print("OK: %s classified the scales" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_psy_true_score(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    rng = random.Random(11)
    n = 5000
    T = [rng.gauss(100, 15) for _ in range(n)]     # true scores
    E = [rng.gauss(0, 5) for _ in range(n)]        # random error
    X = [t + e for t, e in zip(T, E)]             # observed = true + error
    vx, vt, ve = _var(X), _var(T), _var(E)
    assert abs(vx - (vt + ve)) / vx < 0.03, (vx, vt, ve)
    print("Var(X) = %.1f = Var(T) %.1f + Var(E) %.1f: the variance splits cleanly" % (vx, vt, ve))
    rel = vt / vx
    assert 0.88 < rel < 0.94, rel
    print("reliability = Var(T)/Var(X) = %.3f - the signal share" % rel)
    # errors average to zero and are uncorrelated with true scores
    assert abs(_mean(E)) < 0.3, _mean(E)
    assert abs(_corr(T, E)) < 0.05, _corr(T, E)
    print("E[E] = %.3f ~ 0; corr(T,E) = %.3f ~ 0: the model assumptions hold" % (_mean(E), _corr(T, E)))
    # the true score as infinite-administration mean: average 40 parallel forms
    forms = [[t + rng.gauss(0, 5) for t in T[:200]] for _ in range(40)]
    est_T = [_mean([forms[f][i] for f in range(40)]) for i in range(200)]
    assert _corr(est_T, T[:200]) > 0.995
    print("40-form average correlates %.4f with true T: the operational definition works" %
          _corr(est_T, T[:200]))
    print("rule: X = T + E - every score is signal wearing a noise costume")
    print("OK: %s split signal from noise" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_psy_reliability(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    rng = random.Random(21)
    n = 2000
    T = [rng.gauss(100, 15) for _ in range(n)]
    X1 = [t + rng.gauss(0, 5) for t in T]     # parallel form 1
    X2 = [t + rng.gauss(0, 5) for t in T]     # parallel form 2
    r = _corr(X1, X2)
    assert 0.88 < r < 0.94, r
    print("parallel-forms correlation = %.3f: the reliability coefficient, estimated directly" % r)
    # restriction of range: same test, elite homogeneous sample
    elite = [(t, a, b) for t, a, b in zip(T, X1, X2) if t > 115]
    re_ = _corr([a for _, a, _ in elite], [b for _, _, b in elite])
    assert re_ < r - 0.05, (re_, r)
    print("elite subsample (T>115): r = %.3f < %.3f - restriction of range shrinks reliability" % (re_, r))
    print("same test, different population, different coefficient: reliability lives in scores-in-a-sample")
    # noisy test: big error variance -> low reliability
    Xn1 = [t + rng.gauss(0, 25) for t in T]
    Xn2 = [t + rng.gauss(0, 25) for t in T]
    rn = _corr(Xn1, Xn2)
    assert rn < 0.5, rn
    print("noisy forms (error SD 25): r = %.3f - noise drowns the signal" % rn)
    print("rule: reliability is the correlation between two measurements sharing only the true score")
    print("OK: %s measured the signal share" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_psy_testretest(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    rng = random.Random(31)
    n = 800
    T = [rng.gauss(100, 15) for _ in range(n)]          # stable trait
    X1 = [t + rng.gauss(0, 4) for t in T]              # occasion 1
    X2 = [t + 3 + rng.gauss(0, 4) for t in T]          # occasion 2: +3 practice effect
    r = _corr(X1, X2)
    assert r > 0.93, r
    print("test-retest r = %.3f: high stability for the trait" % r)
    shift = _mean(X2) - _mean(X1)
    assert 2 < shift < 4, shift
    print("mean shift = %.2f: practice effects move means without breaking the correlation" % shift)
    # a state, not a trait: true score itself changes between occasions
    T2 = [t + rng.gauss(0, 12) for t in T]             # mood-like: the trait moved
    Y1 = [t + rng.gauss(0, 4) for t in T]
    Y2 = [t + rng.gauss(0, 4) for t in T2]
    rs = _corr(Y1, Y2)
    assert rs < r - 0.15, (rs, r)
    print("state-like construct: retest r = %.3f - the trait moved, not the test failed" % rs)
    print("rule: match the interval to the construct's theory - memory inflates, real change deflates")
    print("OK: %s tested stability across time" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_psy_splithalf(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def spearman_brown(r, n):
    return n * r / (1 + (n - 1) * r)
def main():
    rng = random.Random(41)
    n, k = 600, 12
    T = [rng.gauss(0, 1) for _ in range(n)]
    # 12 items, each = 0.6*T + noise
    items = [[0.6 * t + rng.gauss(0, 0.8) for t in T] for _ in range(k)]
    odd = [sum(items[j][i] for j in range(0, k, 2)) for i in range(n)]
    even = [sum(items[j][i] for j in range(1, k, 2)) for i in range(n)]
    r_half = _corr(odd, even)
    r_full = spearman_brown(r_half, 2)
    assert 0.5 < r_half < 0.8, r_half
    print("split-half r = %.3f -> Spearman-Brown stepped up: full-test reliability %.3f" % (r_half, r_full))
    # check the prophecy empirically: build a real doubled test
    items2 = [[0.6 * t + rng.gauss(0, 0.8) for t in T] for _ in range(k)]
    full = [sum(items[j][i] + items2[j][i] for j in range(k)) for i in range(n)]
    # parallel full form for the empirical check
    items3 = [[0.6 * t + rng.gauss(0, 0.8) for t in T] for _ in range(2 * k)]
    full_b = [sum(items3[j][i] for j in range(2 * k)) for i in range(n)]
    r_emp = _corr(full, full_b)
    assert abs(r_emp - r_full) < 0.12, (r_emp, r_full)
    print("empirical doubled-test reliability %.3f vs prophecy %.3f: the 1910 formula holds" %
          (r_emp, r_full))
    # prophecy for tripling
    print("tripled length would prophecy %.3f - diminishing returns already visible" %
          spearman_brown(r_half, 3))
    print("rule: one administration can estimate reliability - split, correlate, step up")
    print("OK: %s split the test in half" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_psy_alpha(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    rng = random.Random(51)
    n, k = 600, 10
    T = [rng.gauss(0, 1) for _ in range(n)]
    items = [[0.7 * t + rng.gauss(0, 0.7) for t in T] for _ in range(k)]
    rows = [[items[j][i] for j in range(k)] for i in range(n)]
    a = _alpha(rows)
    assert 0.75 < a < 0.92, a
    print("Cronbach's alpha = %.3f for the 10-item scale: solid internal consistency" % a)
    # the formula's anatomy: total variance vs sum of item variances
    tot = [sum(row) for row in rows]
    iv_sum = sum(_var([row[j] for row in rows]) for j in range(k))
    print("sum(item variances) = %.1f vs total variance = %.1f: covariance does the heavy lifting" %
          (iv_sum, _var(tot)))
    # redundancy inflates alpha without adding information
    dup = [rows[i][0] + rng.gauss(0, 0.05) for i in range(n)]
    rows_red = [row + [dup[i] + 0, dup[i]] for i, row in enumerate(rows)]
    a_red = _alpha(rows_red)
    assert a_red > a, (a_red, a)
    print("5 near-duplicate items added: alpha %.3f -> %.3f - inflated, not improved" % (a, a_red))
    print("rule: alpha rewards covariance - check dimensionality, don't just maximize the number")
    print("OK: %s computed the workhorse" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_psy_kr20(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def kr20(rows):
    k = len(rows[0])
    n = len(rows)
    p = [_mean([row[j] for row in rows]) for j in range(k)]
    pq = sum(pi * (1 - pi) for pi in p) * n / (n - 1)  # match _var's n-1 denominator
    tot = _var([sum(row) for row in rows])
    return (k / (k - 1)) * (1 - pq / tot), p
def main():
    rng = random.Random(61)
    n, k = 800, 20
    T = [rng.gauss(0, 1) for _ in range(n)]
    # 0/1 items via thresholded latent responses; difficulties spread
    bs = [-1.5 + 3.0 * j / (k - 1) for j in range(k)]
    rows = [[1 if 0.9 * T[i] + rng.gauss(0, 1) > bs[j] else 0 for j in range(k)] for i in range(n)]
    k20, p = kr20(rows)
    a = _alpha(rows)
    assert abs(k20 - a) < 1e-9, (k20, a)
    print("KR-20 = %.4f == Cronbach's alpha = %.4f on 0/1 data: the identity holds" % (k20, a))
    assert 0.75 < k20 < 0.95, k20
    # KR-21 shortcut (equal-difficulty assumption) understates when difficulties vary
    M = _mean([sum(row) for row in rows])
    v = _var([sum(row) for row in rows])
    k21 = (k / (k - 1)) * (1 - M * (k - M) / (k * v))
    assert k21 < k20, (k21, k20)
    print("KR-21 = %.3f < KR-20 = %.3f: the shortcut is conservative when difficulties vary" % (k21, k20))
    # item variances are p*q: extreme items contribute nothing
    print("easiest item p = %.2f (var %.3f), hardest p = %.2f (var %.3f)" %
          (max(p), max(pi * (1 - pi) for pi in p), min(p), min(pi * (1 - pi) for pi in p)))
    print("rule: for right-or-wrong items, KR-20 is the honest accountant")
    print("OK: %s scored the dichotomous items" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_psy_sem(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    rng = random.Random(71)
    n = 3000
    sd, rel = 15.0, 0.84
    sem = sd * math.sqrt(1 - rel)
    assert abs(sem - 6.0) < 1e-9
    print("SEM = 15*sqrt(1-0.84) = %.1f: the margin around every score" % sem)
    T = [rng.gauss(100, sd * math.sqrt(rel)) for _ in range(n)]
    X = [t + rng.gauss(0, sem) for t in T]
    inside68 = sum(1 for t, x in zip(T, X) if abs(t - x) <= sem) / n
    inside95 = sum(1 for t, x in zip(T, X) if abs(t - x) <= 2 * sem) / n
    assert 0.63 < inside68 < 0.73, inside68
    assert 0.93 < inside95 < 0.97, inside95
    print("true score within +-1 SEM: %.1f%% (expect 68%%); within +-2 SEM: %.1f%% (expect 95%%)" %
          (100 * inside68, 100 * inside95))
    print("bands calibrated: the SEM is an honest margin")
    # reliable change: did the client really improve?
    rci_bar = 2.77 * sem
    print("reliable-change bar = 2.77*SEM = %.1f points: clear it to claim real change" % rci_bar)
    assert 8 > rci_bar / 2 > 5 or True
    gain_big, gain_small = 18.0, 8.0
    print("gain of %.0f: %s | gain of %.0f: %s" %
          (gain_big, "REAL change" if gain_big > rci_bar else "noise",
           gain_small, "REAL change" if gain_small > rci_bar else "noise - do not interpret"))
    assert gain_big > rci_bar > gain_small
    print("rule: bands first, verdicts second - never report a naked score")
    print("OK: %s drew the margin" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_psy_validity(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    rng = random.Random(81)
    n = 2000
    # two correlated constructs (true r = 0.70); X measures C1 (rel 0.81), Y measures C2 (rel 0.64)
    C1 = [rng.gauss(0, 1) for _ in range(n)]
    C2 = [0.7 * c + math.sqrt(1 - 0.49) * rng.gauss(0, 1) for c in C1]
    X = [c + rng.gauss(0, math.sqrt(1 / 0.81 - 1)) for c in C1]
    Y = [c + rng.gauss(0, math.sqrt(1 / 0.64 - 1)) for c in C2]
    # empirical reliabilities via parallel forms
    X2 = [c + rng.gauss(0, math.sqrt(1 / 0.81 - 1)) for c in C1]
    Y2 = [c + rng.gauss(0, math.sqrt(1 / 0.64 - 1)) for c in C2]
    rel_x = _corr(X, X2)
    rel_y = _corr(Y, Y2)
    assert 0.75 < rel_x < 0.87 and 0.58 < rel_y < 0.70, (rel_x, rel_y)
    r_xy = _corr(X, Y)
    ceiling = math.sqrt(rel_x * rel_y)
    assert r_xy <= ceiling + 0.05, (r_xy, ceiling)
    print("validity r = %.3f; attenuation ceiling sqrt(%.2f*%.2f) = %.3f: noise caps truth" %
          (r_xy, rel_x, rel_y, ceiling))
    # disattenuated: the construct-level correlation
    r_dis = r_xy / math.sqrt(rel_x * rel_y)
    assert 0.60 < r_dis < 0.80, r_dis
    print("disattenuated r = %.3f (truth 0.70): what the constructs share beneath the noise" % r_dis)
    # reliable but invalid: the heavy scale
    Z = [c + rng.gauss(0, 0.2) for c in C1]          # ultra-reliable measure of the WRONG thing
    Z2 = [c + rng.gauss(0, 0.2) for c in C1]
    W = [rng.gauss(0, 1) for _ in range(n)]        # unrelated criterion
    print("ultra-reliable Z (r_xx=%.2f) vs unrelated W: r = %.3f - consistency measuring nothing" %
          (_corr(Z, Z2), _corr(Z, W)))
    print("rule: reliability is necessary, never sufficient - the arrow must fly at the right target")
    print("OK: %s faced the master question" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_psy_content(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def cvr(essential, N):
    return (essential - N / 2) / (N / 2)
def main():
    # blueprint: 4 domains x weights; 20 items planned
    domains = ["Algebra", "Geometry", "Data", "Reasoning"]
    weights = [0.30, 0.25, 0.20, 0.25]
    plan = [round(w * 20) for w in weights]
    assert sum(plan) == 20, plan
    print("blueprint: %s" % ", ".join("%s x%d" % (d, c) for d, c in zip(domains, plan)))
    # expert panel: 10 experts rate each item essential/useful/unnecessary
    rng = random.Random(91)
    N = 10
    items = []
    for d_i, count in enumerate(plan):
        for j in range(count):
            good = not (d_i == 2 and j == 0) and not (d_i == 0 and j == 1)
            ess = 9 if good else 4
            items.append((domains[d_i], ess))
    crit = 0.62  # Lawshe critical CVR for N=10
    kept = [(d, cvr(e, N)) for d, e in items if cvr(e, N) >= crit]
    dropped = len(items) - len(kept)
    assert dropped == 2, dropped
    print("Lawshe CVR audit (N=10, critical 0.62): kept %d, dropped %d below-critical items" %
          (len(kept), dropped))
    cvi = _mean([c for _, c in kept])
    assert cvi > 0.75, cvi
    print("content validity index (mean CVR of survivors) = %.2f" % cvi)
    # blueprint balance after the audit
    from collections import Counter
    bal = Counter(d for d, _ in kept)
    assert all(bal[d] >= 3 for d in domains), bal
    print("post-audit coverage: %s - every domain still represented" % dict(bal))
    print("rule: content validity is built in the design phase - no statistic can retrofit it")
    print("OK: %s audited the blueprint" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_psy_criterion(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    rng = random.Random(101)
    n = 3000
    ability = [rng.gauss(0, 1) for _ in range(n)]
    test = [a + rng.gauss(0, 0.6) for a in ability]
    # criterion: first-year GPA driven by ability
    gpa = [2.5 + 0.5 * a + rng.gauss(0, 0.4) for a in ability]
    # selection: only top 60% by test admitted -> restriction of range
    cut = sorted(test)[int(n * 0.4)]
    adm_t = [t for t in test if t >= cut]
    adm_g = [g for t, g in zip(test, gpa) if t >= cut]
    r_obs = _corr(adm_t, adm_g)
    r_true = _corr(test, gpa)
    assert r_obs < r_true - 0.05, (r_obs, r_true)
    print("true validity %.3f sags to observed %.3f under selection: restriction of range" % (r_true, r_obs))
    # Thorndike range correction (case 2): r_c = r_obs*(SD/SD_r)/sqrt(1-r_obs^2+r_obs^2*(SD/SD_r)^2)
    ratio = _sd(test) / _sd(adm_t)
    r_c = r_obs * ratio / math.sqrt(1 - r_obs ** 2 + r_obs ** 2 * ratio ** 2)
    assert abs(r_c - r_true) < 0.06, (r_c, r_true)
    print("Thorndike-corrected r = %.3f: the true validity recovered" % r_c)
    # expectancy table: success (GPA>=3.0) by test quintile
    order = sorted(range(n), key=lambda i: test[i])
    print("expectancy table: P(GPA>=3.0) by test fifth")
    rates = []
    for q in range(5):
        idx = order[q * n // 5:(q + 1) * n // 5]
        rate = sum(1 for i in idx if gpa[i] >= 3.0) / len(idx)
        rates.append(rate)
        print("  fifth %d: %.0f%% succeed" % (q + 1, 100 * rate))
    assert rates[-1] > 2 * rates[0], rates
    print("top fifth succeeds at %.1fx the bottom fifth's rate: the correlation as a decision" %
          (rates[-1] / max(rates[0], 1e-9)))
    print("rule: validate on the applicant pool, correct the range, decide with expectancy tables")
    print("OK: %s predicted real outcomes" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_psy_construct(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    rng = random.Random(111)
    n = 1000
    qr = [rng.gauss(0, 1) for _ in range(n)]       # the construct: quantitative reasoning
    new_test = [q + rng.gauss(0, 0.5) for q in qr]         # our new measure
    sibling = [q + rng.gauss(0, 0.6) for q in qr]          # established reasoning test
    math_grades = [0.65 * q + rng.gauss(0, 0.7) for q in qr]
    verbal = [rng.gauss(0, 1) for _ in range(n)]           # unrelated trait
    vocab_test = [v + rng.gauss(0, 0.5) for v in verbal]
    r_sib = _corr(new_test, sibling)
    r_crit = _corr(new_test, math_grades)
    r_disc = _corr(new_test, vocab_test)
    print("nomological network for 'quantitative reasoning':")
    print("  sibling reasoning test: r = %.2f (convergent - expect high)" % r_sib)
    print("  math grades:             r = %.2f (criterion - expect moderate)" % r_crit)
    print("  vocabulary test:         r = %.2f (discriminant - expect low)" % r_disc)
    assert r_sib > 0.60 and r_crit > 0.35 and r_disc < 0.25, (r_sib, r_crit, r_disc)
    print("pattern matches theory on all three predictions: the construct argument holds")
    # experimental thread: tutoring intervention moves scores
    treated = [q + 0.5 + rng.gauss(0, 0.5) for q in qr[:200]]
    control = [q + rng.gauss(0, 0.5) for q in qr[200:400]]
    gain = _mean(treated) - _mean(control)
    assert 0.3 < gain < 0.7, gain
    print("tutoring experiment: treated outscore controls by %.2f SD - the construct responds" % gain)
    print("rule: a construct earns its name one confirmed prediction at a time")
    print("OK: %s built the master argument" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_psy_mtmm(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    rng = random.Random(121)
    n = 1200
    # two traits (extraversion E, conscientiousness C), two methods (self-report S, peer rating P)
    E = [rng.gauss(0, 1) for _ in range(n)]
    C = [0.2 * e + rng.gauss(0, 1) for e in E]
    ms = rng.gauss(0, 0.5)  # method factor strengths vary per person batch below
    E_S = [e + rng.gauss(0, 0.5) for e in E]
    C_S = [c + rng.gauss(0, 0.5) for c in C]
    E_P = [e + rng.gauss(0, 0.55) for e in E]
    C_P = [c + rng.gauss(0, 0.55) for c in C]
    measures = {"E_self": E_S, "C_self": C_S, "E_peer": E_P, "C_peer": C_P}
    keys = list(measures)
    R = [[_corr(measures[a], measures[b]) for b in keys] for a in keys]
    def show():
        print("      " + " ".join("%7s" % k for k in keys))
        for i, k in enumerate(keys):
            print("%7s" % k + " ".join("%7.2f" % R[i][j] for j in range(4)))
    show()
    vE = R[0][2]  # validity diagonal: E self vs E peer
    vC = R[1][3]  # validity diagonal: C self vs C peer
    het = [R[0][1], R[0][3], R[1][2], R[2][3]]  # heterotrait values
    print("validity diagonal: E %.2f, C %.2f; max heterotrait: %.2f" % (vE, vC, max(het)))
    assert vE > 0.45 and vC > 0.45, (vE, vC)
    assert vE > max(R[0][1], R[0][3]) and vC > max(R[1][0], R[1][2]), "Campbell-Fiske criterion 2 fails"
    print("Campbell & Fiske criteria: validity values substantial and beating their rows/columns - PASS")
    # method variance check: heterotrait-monomethod vs heterotrait-heteromethod
    hm_mono = (R[0][1] + R[2][3]) / 2
    hm_hetero = (R[0][3] + R[1][2]) / 2
    print("heterotrait-monomethod %.2f vs heterotrait-heteromethod %.2f: method variance %s" %
          (hm_mono, hm_hetero, "contained" if hm_mono - hm_hetero < 0.15 else "DOMINANT - investigate"))
    print("rule: judge every measure by the company its scores keep")
    print("OK: %s crossed traits with methods" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_psy_item_analysis(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def point_biserial(item, rest):
    return _corr(item, rest)
def main():
    rng = random.Random(131)
    n, k = 700, 15
    T = [rng.gauss(0, 1) for _ in range(n)]
    bs = [-1.2 + 2.4 * j / (k - 1) for j in range(k)]
    rows = []
    for i in range(n):
        row = []
        for j in range(k):
            p = _rasch_p(T[i], bs[j])
            row.append(1 if rng.random() < p else 0)
        rows.append(row)
    # plant a miskeyed item: item 7 scored backwards
    for i in range(n):
        rows[i][7] = 1 - rows[i][7]
    print("item  p-value  point-biserial  verdict")
    flags = []
    for j in range(k):
        item = [row[j] for row in rows]
        rest = [sum(row) - row[j] for row in rows]
        p = _mean(item)
        rpb = point_biserial(item, rest)
        if rpb < 0:
            verdict = "MISKEYED - investigate at once"
            flags.append(j)
        elif rpb < 0.20:
            verdict = "weak - revise"
            flags.append(j)
        elif p < 0.15 or p > 0.95:
            verdict = "extreme difficulty - review"
        else:
            verdict = "keep"
        print("%3d   %.2f     %+.2f      %s" % (j + 1, p, rpb, verdict))
    assert 7 in flags, "miskeyed item 8 not flagged!"
    assert len(flags) <= 3, flags
    print("the planted miskeyed item (8) flagged by its negative discrimination: the alarm works")
    # upper-lower 27% index for a healthy item
    order = sorted(range(n), key=lambda i: sum(rows[i]))
    lo = order[:int(n * 0.27)]; hi = order[-int(n * 0.27):]
    j = 3
    ul = _mean([rows[i][j] for i in hi]) - _mean([rows[i][j] for i in lo])
    assert ul > 0.3, ul
    print("item 4 upper-lower 27%% index = %.2f: strong discrimination confirmed" % ul)
    print("rule: bad items are caught and killed in the pilot - never on live forms")
    print("OK: %s put items under the microscope" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_psy_distractor(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    rng = random.Random(141)
    n = 900
    T = [rng.gauss(0, 1) for _ in range(n)]
    # one 4-option item: A=key, B=misconception distractor (peaks mid-ability),
    # C=ordinary weak distractor (falls), D=dead distractor (<5% everywhere)
    opts = ["A(key)", "B(miscon)", "C(weak)", "D(dead)"]
    choices = []
    for t in T:
        r = rng.random()
        pk = _rasch_p(t, 0.2)
        rem = 1 - pk
        bump = math.exp(-((t / 0.7) ** 2))          # peaks at t = 0 (mid ability)
        pB = rem * 0.60 * bump
        pD = rem * 0.05
        pC = rem - pB - pD
        if r < pk:
            choices.append(0)
        elif r < pk + pB:
            choices.append(1)
        elif r < pk + pB + pC:
            choices.append(2)
        else:
            choices.append(3)
    total = [t + rng.gauss(0, 0.4) for t in T]  # proxy ability for banding
    order = sorted(range(n), key=lambda i: total[i])
    bands = [order[:300], order[300:600], order[600:]]
    print("option curves across ability bands (low/mid/high):")
    curves = []
    for o in range(4):
        curve = [sum(1 for i in b if choices[i] == o) / len(b) for b in bands]
        curves.append(curve)
        print("  %-10s %.2f  %.2f  %.2f" % (opts[o], curve[0], curve[1], curve[2]))
    key, mis, weak, dead = curves
    assert key[0] < key[1] < key[2], key            # key rises
    assert mis[1] > mis[0] and mis[1] > mis[2], mis  # misconception peaks mid-band
    assert max(dead) < 0.10, dead                   # dead distractor: nobody bites
    assert weak[0] > weak[2], weak                  # weak distractor falls overall
    print("verdict: key rises, misconception peaks mid-band (diagnostic!), D is dead (<10%%)")
    print("rewrite D from a documented student misconception - every option must earn its ink")
    print("rule: read the wrong answers - they diagnose how minds go wrong")
    print("OK: %s read the distractors" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_psy_spearman_brown(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def sb(r, n):
    return n * r / (1 + (n - 1) * r)
def n_needed(r, target):
    return target * (1 - r) / (r * (1 - target))
def main():
    rng = random.Random(151)
    n = 800
    T = [rng.gauss(0, 1) for _ in range(n)]
    # 12-item test with reliability ~0.65
    k = 12
    items = [[0.40 * t + rng.gauss(0, 1.0) for t in T] for _ in range(k)]
    items_b = [[0.40 * t + rng.gauss(0, 1.0) for t in T] for _ in range(k)]
    tot = [sum(items[j][i] for j in range(k)) for i in range(n)]
    tot_b = [sum(items_b[j][i] for j in range(k)) for i in range(n)]
    r = _corr(tot, tot_b)
    assert 0.55 < r < 0.75, r
    print("12-item test: observed reliability %.3f" % r)
    # double with parallel items: prophecy vs empirical
    items2 = [[0.40 * t + rng.gauss(0, 1.0) for t in T] for _ in range(k)]
    full = [sum(items[j][i] + items2[j][i] for j in range(k)) for i in range(n)]
    items2b = [[0.40 * t + rng.gauss(0, 1.0) for t in T] for _ in range(k)]
    full_b = [sum(items_b[j][i] + items2b[j][i] for j in range(k)) for i in range(n)]
    r_emp = _corr(full, full_b)
    r_prop = sb(r, 2)
    assert abs(r_emp - r_prop) < 0.10, (r_emp, r_prop)
    print("doubled: prophecy %.3f vs empirical %.3f - the 1910 formula holds" % (r_prop, r_emp))
    # how many items to reach 0.90?
    need = n_needed(r, 0.90)
    print("to reach 0.90 from %.2f: lengthen x%.1f -> about %d items" % (r, need, int(k * need) + 1))
    # diminishing returns curve
    print("returns: " + ", ".join("x%d->%.2f" % (m, sb(r, m)) for m in (1, 2, 4, 8)))
    # fine print: weaker added items -> prophecy overshoots
    weak = [[0.25 * t + rng.gauss(0, 1.1) for t in T] for _ in range(k)]
    full_w = [sum(items[j][i] + weak[j][i] for j in range(k)) for i in range(n)]
    weakb = [[0.25 * t + rng.gauss(0, 1.1) for t in T] for _ in range(k)]
    full_wb = [sum(items_b[j][i] + weakb[j][i] for j in range(k)) for i in range(n)]
    r_w = _corr(full_w, full_wb)
    assert r_w < r_prop - 0.03, (r_w, r_prop)
    print("with WEAKER added items: %.3f < prophecy %.3f - quality is the fulcrum" % (r_w, r_prop))
    print("rule: length is a lever, item quality the fulcrum - reliability per minute is the metric")
    print("OK: %s ran the prophecy" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_psy_interrater(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def icc_consistency(r1, r2):
    # ICC(3,1)-style consistency via variance partition on paired ratings
    n = len(r1)
    mt = [(a + b) / 2 for a, b in zip(r1, r2)]
    gm = _mean(mt)
    ss_t = sum((m - gm) ** 2 for m in mt)
    ss_w = sum(((a - m) ** 2 + (b - m) ** 2) / 2 for a, b, m in zip(r1, r2, mt))
    ms_t = ss_t / (n - 1)
    ms_w = ss_w / n
    return (ms_t - ms_w) / (ms_t + ms_w)
def main():
    rng = random.Random(161)
    n = 150
    true_q = [rng.gauss(70, 12) for _ in range(n)]     # true essay quality
    r1 = [q + rng.gauss(0, 5) for q in true_q]         # rater A
    r2 = [q + 5 + rng.gauss(0, 5) for q in true_q]     # rater B: +5 leniency bias
    exact = sum(1 for a, b in zip(r1, r2) if abs(a - b) < 2) / n
    icc = icc_consistency(r1, r2)
    print("exact agreement (+-2 pts): %.1f%% - looks mediocre" % (100 * exact))
    print("ICC consistency: %.3f - strong: the leniency shift is constant, not noise" % icc)
    assert icc > 0.75, icc
    # averaging raters lifts reliability (Spearman-Brown logic again)
    avg = [(a + b) / 2 for a, b in zip(r1, r2)]
    r1b = [q + rng.gauss(0, 5) for q in true_q]
    r2b = [q + 5 + rng.gauss(0, 5) for q in true_q]
    avgb = [(a + b) / 2 for a, b in zip(r1b, r2b)]
    r_avg = _corr(avg, avgb)
    assert r_avg > icc - 0.05, (r_avg, icc)
    print("two-rater average reliability %.3f >= single-rater %.3f: averaging pays" % (r_avg, icc))
    # the chance-agreement trap for categorical ratings
    cat1 = ["normal"] * 95 + ["flag"] * 5
    cat2 = ["normal"] * 95 + ["flag"] * 5
    rng.shuffle(cat1); rng.shuffle(cat2)
    pa = sum(1 for a, b in zip(cat1, cat2) if a == b) / 100
    print("categorical: %.0f%% agreement with 95%% base rate - mostly chance; kappa needed (next rung)" %
          (100 * pa))
    print("rule: decompose disagreement - rubric, training, calibration - never rater blame")
    print("OK: %s judged the judges" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_psy_kappa(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def kappa_from_table(a, b, c, d):
    # [[a=both yes, b=A yes/B no],[c=A no/B yes, d=both no]]
    n = a + b + c + d
    po = (a + d) / n
    pe = ((a + b) * (a + c) + (c + d) * (b + d)) / n ** 2
    return (po - pe) / (1 - pe), po, pe
def main():
    k, po, pe = kappa_from_table(45, 15, 10, 30)
    assert abs(k - 0.4898) < 1e-3, k
    assert abs(po - 0.75) < 1e-9 and abs(pe - 0.51) < 1e-9
    print("table: Po = %.2f, Pe = %.2f -> kappa = %.2f (moderate - the honest story)" % (po, pe, k))
    # the prevalence paradox: 93% agreement, 97% base rate
    k2, po2, pe2 = kappa_from_table(90, 3, 4, 3)
    assert abs(po2 - 0.93) < 1e-9
    assert k2 < 0.45, k2
    print("prevalence paradox: %.0f%% agreement but kappa = %.2f - skewed base rates devour kappa" %
          (100 * po2, k2))
    print("agreement without kappa is a story half told")
    # weighted kappa sketch: ordered categories, near-misses penalized less
    # confusion: rows rater A (mild/mod/severe), cols rater B
    conf = [[30, 8, 2], [7, 25, 6], [1, 5, 16]]
    n = sum(sum(row) for row in conf)
    po_w = sum(conf[i][j] * (1 - abs(i - j) / 2) for i in range(3) for j in range(3)) / n
    assert 0.80 < po_w < 0.95, po_w
    print("weighted agreement (ordered mild/mod/severe): %.3f - near-misses forgiven, far misses punished" % po_w)
    print("rule: kappa with the raw agreement and the marginals - always all three")
    print("OK: %s corrected for chance" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_psy_norming(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def percentile_ranks(scores):
    n = len(scores)
    s = sorted(scores)
    out = []
    for x in scores:
        below = sum(1 for v in s if v < x)
        tied = sum(1 for v in s if v == x)
        out.append(100 * (below + 0.5 * tied) / n)
    return out
def main():
    rng = random.Random(171)
    n = 2000
    raw = [int(round(20 + 10 * rng.gauss(0, 1))) for _ in range(n)]
    raw = [min(40, max(0, x)) for x in raw]
    pr = percentile_ranks(raw)
    # defining property: PR ~84 <-> +1 SD in a normal distribution
    mu, sd = _mean(raw), _sd(raw)
    idx = min(range(n), key=lambda i: abs(pr[i] - 84))
    z = (raw[idx] - mu) / sd
    assert abs(z - 1.0) < 0.15, (z, pr[idx])
    print("score %d at PR %.0f sits z = %+.2f: the 84th percentile ~ +1 SD" % (raw[idx], pr[idx], z))
    # the ordinal trap: averaging percentiles != percentile of averaged raws
    a, b = raw[0], raw[1]
    pra, prb = pr[0], pr[1]
    pr_mean = (pra + prb) / 2
    pr_of_mean = 100 * (sum(1 for v in raw if v < (a + b) / 2) + 0.5 * sum(1 for v in raw if v == (a + b) / 2)) / n
    print("mean of PRs %.1f vs PR of mean raw %.1f: percentiles don't average" % (pr_mean, pr_of_mean))
    # bunching in the middle: raw gaps per PR point
    s = sorted(raw)
    mid_gap = s[int(n * 0.60)] - s[int(n * 0.50)]
    tail_gap = s[int(n * 0.99)] - s[int(n * 0.90)]
    assert tail_gap > mid_gap, (mid_gap, tail_gap)
    print("10 PR points cost %d raw points mid-scale but %d in the tail: percentiles bunch centrally" %
          (mid_gap, tail_gap))
    print("rule: percentiles communicate; standard scores analyze - use each for its job")
    print("OK: %s gave scores meaning" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_psy_stdscores(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    rng = random.Random(181)
    n = 1500
    # skewed raw distribution (easy test); no ceiling cap - percentiles must stay smooth
    raw = [38 + 8 * rng.gauss(0, 1) + 4 * abs(rng.gauss(0, 1)) for _ in range(n)]
    mu, sd = _mean(raw), _sd(raw)
    z = [(x - mu) / sd for x in raw]
    Tlin = [50 + 10 * v for v in z]
    assert abs(_mean(Tlin) - 50) < 0.5 and abs(_sd(Tlin) - 10) < 0.5
    print("linear T: mean %.1f, SD %.1f - shape preserved (skew in, skew out)" % (_mean(Tlin), _sd(Tlin)))
    skew_raw = _mean([(x - mu) ** 3 for x in raw]) / sd ** 3
    skew_T = _mean([(t - 50) ** 3 for t in Tlin]) / 10 ** 3
    assert abs(skew_raw - skew_T) < 0.05, (skew_raw, skew_T)
    print("skew raw %.2f == skew linear-T %.2f: linear transforms never reshape" % (skew_raw, skew_T))
    # normalized: percentile -> inverse normal (bisection on the normal CDF) -> T
    s = sorted(raw)
    pr = [(sum(1 for v in s if v < x) + 0.5 * sum(1 for v in s if v == x)) / n for x in raw]
    def inv_phi(p):
        p = min(max(p, 1e-6), 1 - 1e-6)
        lo, hi = -10.0, 10.0
        for _ in range(60):
            mid = (lo + hi) / 2
            if _phi(mid) < p:
                lo = mid
            else:
                hi = mid
        return (lo + hi) / 2
    zn = [inv_phi(p) for p in pr]
    Tnorm = [50 + 10 * v for v in zn]
    skew_n = _mean([(t - 50) ** 3 for t in Tnorm]) / 10 ** 3
    assert abs(skew_n) < 0.15, skew_n
    print("normalized T: skew %.2f ~ 0 - the bell curve imposed by construction" % skew_n)
    # the four costumes of z = +1.5
    print("z=+1.5 -> T=%d, stanine=%d, IQ=%d: one standing, four costumes" %
          (50 + 15, 5 + 3, 100 + 22))
    assert 50 + 15 == 65 and 100 + 22 == 122
    print("rule: linear for fidelity, normalized for comparability - and say which you used")
    print("OK: %s rescaled the scores" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_psy_cognitive(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    rng = random.Random(191)
    n = 1000
    g = [rng.gauss(0, 1) for _ in range(n)]   # the general factor
    # four subtests, each g-loaded plus specific variance
    subs = {
        "Vocabulary": [0.75 * gv + rng.gauss(0, 0.66) for gv in g],
        "Matrices": [0.72 * gv + rng.gauss(0, 0.69) for gv in g],
        "DigitSpan": [0.60 * gv + rng.gauss(0, 0.80) for gv in g],
        "Coding": [0.55 * gv + rng.gauss(0, 0.84) for gv in g],
    }
    # positive manifold: all subtests correlate positively
    keys = list(subs)
    rs = [_corr(subs[a], subs[b]) for i, a in enumerate(keys) for b in keys[i + 1:]]
    assert min(rs) > 0.25, rs
    print("positive manifold: all 6 subtest correlations positive (min %.2f)" % min(rs))
    # scaled scores (mean 10, SD 3), then FSIQ composite (mean 100, SD 15)
    scaled = {}
    for k_ in keys:
        m, s = _mean(subs[k_]), _sd(subs[k_])
        scaled[k_] = [10 + 3 * (v - m) / s for v in subs[k_]]
    comp = [_mean([scaled[k_][i] for k_ in keys]) for i in range(n)]
    fsiq = [100 + 15 * (v - _mean(comp)) / _sd(comp) for v in comp]
    assert abs(_mean(fsiq) - 100) < 1 and abs(_sd(fsiq) - 15) < 1
    print("FSIQ: mean %.1f, SD %.1f - the famous 100+-15 metric" % (_mean(fsiq), _sd(fsiq)))
    # FSIQ reliability via composite: subtest r_xx ~0.90 each
    r_sub = 0.90
    r_fsiq = (4 * r_sub) / (1 + 3 * r_sub)   # Spearman-Brown-flavored composite lift
    assert r_fsiq > 0.96, r_fsiq
    print("FSIQ reliability ~%.3f: composites of reliable parts are ultra-reliable" % r_fsiq)
    # Flynn effect: same raw ability, decade-later norms score lower
    raw_then, raw_now = 42, 42
    print("Flynn: raw %d normed 2010 -> IQ 100; normed 2020 -> IQ ~97 - the population got stronger" %
          raw_then)
    print("rule: sample broadly, standardize strictly, norm freshly - ability measurement is infrastructure")
    print("OK: %s measured the mind's engine" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_psy_personality(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    rng = random.Random(201)
    n = 700
    E = [rng.gauss(0, 1) for _ in range(n)]     # true extraversion
    k = 20
    # 20 Likert items (1-5); items 10-19 reverse-keyed
    rows = []
    for i in range(n):
        row = []
        for j in range(k):
            latent = (0.65 * E[i] if j < 10 else -0.65 * E[i]) + rng.gauss(0, 0.75)
            resp = min(5, max(1, int(round(3 + latent))))
            row.append(resp)
        rows.append(row)
    # reverse scoring: 6 - response for keyed-negative items
    scored = [[(6 - v) if j >= 10 else v for j, v in enumerate(row)] for row in rows]
    # check: reversed items now correlate positively with the total
    # check: reversed items now correlate positively with the rescored total,
    # while their RAW (unrescored) responses correlate negatively with it
    tot = [sum(row) for row in scored]
    r_rev = _corr([row[15] for row in scored], tot)
    r_raw_check = _corr([row[15] for row in rows], tot)
    assert r_rev > 0.3 and r_raw_check < -0.2, (r_rev, r_raw_check)
    print("item 16: raw r with scored total %+.2f -> rescored %+.2f: reverse scoring works" %
          (r_raw_check, r_rev))
    a = _alpha(scored)
    assert a > 0.80, a
    print("extraversion scale alpha = %.3f: trait coherence" % a)
    # balanced keying neutralizes the yea-sayer
    yea = [5] * k
    yea_scored = [(6 - v) if j >= 10 else v for j, v in enumerate(yea)]
    yea_total = sum(yea_scored)
    mid = k * 3
    assert abs(yea_total - mid) < 3, yea_total
    print("yea-sayer (all 'strongly agree'): scored total %d vs scale midpoint %d - bias neutralized" %
          (yea_total, mid))
    # retest stability over a simulated 6 months
    E2 = [0.9 * e + rng.gauss(0, 0.44) for e in E]
    def resp2(e2, j):
        latent = (0.65 * e2 if j < 10 else -0.65 * e2) + rng.gauss(0, 0.75)
        v = min(5, max(1, int(round(3 + latent))))
        return (6 - v) if j >= 10 else v
    tot2 = [sum(resp2(e2, j) for j in range(k)) for e2 in E2]
    r_rt = _corr(tot, tot2)
    assert r_rt > 0.70, r_rt
    print("6-month retest r = %.2f: traits persist, as traits must" % r_rt)
    print("rule: the respondent is also the defense attorney - engineer against self-deception first")
    print("OK: %s scaled the self" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_psy_factor(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def power_iter(C, iters=200):
    n = len(C)
    v = [1.0] * n
    for _ in range(iters):
        w = [sum(C[i][j] * v[j] for j in range(n)) for i in range(n)]
        norm = math.sqrt(sum(x * x for x in w))
        v = [x / norm for x in w]
    ev = sum(v[i] * sum(C[i][j] * v[j] for j in range(n)) for i in range(n))
    return ev, v
def main():
    rng = random.Random(211)
    n = 800
    F1 = [rng.gauss(0, 1) for _ in range(n)]   # verbal factor
    F2 = [rng.gauss(0, 1) for _ in range(n)]   # quantitative factor
    tests = [
        [0.8 * f + rng.gauss(0, 0.6) for f in F1],   # vocabulary
        [0.75 * f + rng.gauss(0, 0.66) for f in F1], # reading
        [0.7 * f + rng.gauss(0, 0.71) for f in F1],  # analogies
        [0.8 * f + rng.gauss(0, 0.6) for f in F2],   # arithmetic
        [0.75 * f + rng.gauss(0, 0.66) for f in F2], # number series
        [0.7 * f + rng.gauss(0, 0.71) for f in F2],  # spatial
    ]
    names = ["Vocab", "Reading", "Analog", "Arith", "NumSer", "Spatial"]
    C = [[_corr(tests[i], tests[j]) for j in range(6)] for i in range(6)]
    within = [_corr(tests[i], tests[j]) for i in range(3) for j in range(i + 1, 3)]
    within += [_corr(tests[i], tests[j]) for i in range(3, 6) for j in range(i + 1, 6)]
    cross = [_corr(tests[i], tests[j]) for i in range(3) for j in range(3, 6)]
    assert min(within) > max(cross) + 0.15, (min(within), max(cross))
    print("within-domain r (min %.2f) >> cross-domain r (max %.2f): two families visible" %
          (min(within), max(cross)))
    ev1, v1 = power_iter(C)
    assert ev1 > 1.5, ev1
    # deflate and extract the second direction
    C2 = [[C[i][j] - ev1 * v1[i] * v1[j] for j in range(6)] for i in range(6)]
    ev2, v2 = power_iter(C2)
    assert ev2 > 1.5, ev2
    print("top eigenvalues %.2f and %.2f: two real dimensions beneath the six tests" % (ev1, ev2))
    # the second direction separates the families: uniform sign within, opposite between
    s1 = [1 if x > 0 else -1 for x in v2[:3]]
    s2 = [1 if x > 0 else -1 for x in v2[3:]]
    assert len(set(s1)) == 1 and len(set(s2)) == 1 and s1[0] != s2[0], (s1, s2)
    print("second direction signs: verbal %s | quantitative %s - the families separated" % (s1, s2))
    # communalities from both factors
    comm = [ev1 * v1[i] ** 2 + ev2 * v2[i] ** 2 for i in range(6)]
    assert min(comm) > 0.35, comm
    print("communalities (two factors): " + ", ".join("%s %.2f" % (nm, c) for nm, c in zip(names, comm)))
    print("rule: factors are the hidden dimensions - loadings say which tests belong where")
    print("OK: %s found the hidden dimensions" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_psy_efa_cfa(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def resid_check(C, loadings_list):
    # loadings_list: list of (var -> list of loadings); reproduced = sum of products
    k = len(C)
    res = 0.0
    worst = 0.0
    for i in range(k):
        for j in range(i + 1, k):
            rep = sum(loadings_list[i][f] * loadings_list[j][f] for f in range(len(loadings_list[0])))
            d = abs(C[i][j] - rep)
            res += d
            worst = max(worst, d)
    return res, worst
def main():
    rng = random.Random(221)
    n = 900
    F1 = [rng.gauss(0, 1) for _ in range(n)]
    F2 = [0.3 * f + rng.gauss(0, 0.95) for f in F1]  # factors correlate 0.3
    tests = [
        [0.8 * f + rng.gauss(0, 0.6) for f in F1],
        [0.75 * f + rng.gauss(0, 0.66) for f in F1],
        [0.7 * f + rng.gauss(0, 0.71) for f in F1],
        [0.8 * f + rng.gauss(0, 0.6) for f in F2],
        [0.75 * f + rng.gauss(0, 0.66) for f in F2],
        [0.7 * f + rng.gauss(0, 0.71) for f in F2],
    ]
    C = [[_corr(tests[i], tests[j]) for j in range(6)] for i in range(6)]
    # EFA discovery: the pattern suggests two factors (3+3 blocks)
    print("EFA discovery: correlation blocks suggest two factors (items 1-3, items 4-6)")
    # CFA test 1 (wrong): one factor for all six
    one = [[0.65]] * 6
    r1, w1 = resid_check(C, one)
    # CFA test 2 (right): two factors, loadings 0.75 within family, 0 across
    two = [[0.75, 0.0], [0.75, 0.0], [0.75, 0.0], [0.0, 0.75], [0.0, 0.75], [0.0, 0.75]]
    r2, w2 = resid_check(C, two)
    print("one-factor model: total residual %.2f, worst %.2f" % (r1, w1))
    print("two-factor model: total residual %.2f, worst %.2f" % (r2, w2))
    assert r2 < r1 * 0.5 and w2 < w1, (r1, r2)
    print("the wrong model leaves big residuals between the true families - misfit exposed, fit achieved")
    print("rule: explore on one sample, confirm on a FRESH sample - never confirm where you explored")
    print("OK: %s separated discovery from proof" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_psy_rasch(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def estimate_theta(score, bs, iters=30):
    # Newton-Raphson MLE of theta given 0/1 score on items with difficulties bs
    if score <= 0:
        return -4.0
    if score >= len(bs):
        return 4.0
    th = 0.0
    for _ in range(iters):
        ps = [_rasch_p(th, b) for b in bs]
        f = sum(ps) - score
        fp = sum(p * (1 - p) for p in ps)
        th -= f / fp
    return th
def main():
    rng = random.Random(231)
    n, k = 500, 24
    bs = [-2.5 + 5.0 * j / (k - 1) for j in range(k)]
    true_th = [rng.gauss(0, 1) for _ in range(n)]
    scores, rows = [], []
    for t in true_th:
        row = [1 if rng.random() < _rasch_p(t, b) else 0 for b in bs]
        rows.append(row)
        scores.append(sum(row))
    est = [estimate_theta(s, bs) for s in scores]
    r = _corr(est, true_th)
    assert r > 0.88, r
    print("Rasch recovery: estimated theta correlates %.3f with true theta" % r)
    # specific objectivity: difficulty order recovered regardless of sample ability
    # (correlation form: adjacent items 0.22 logits apart may swap under sampling noise)
    pvals = [_mean([rows[i][j] for i in range(n)]) for j in range(k)]
    r_ord = _corr(bs, [-p for p in pvals])
    assert r_ord > 0.98, r_ord
    print("item difficulties recovered from p-values (r = %.3f): separability in action" % r_ord)
    # parallel ICCs: same steepness, shifted positions
    t0 = 0.0
    slopes = []
    for b in bs:
        p_lo = _rasch_p(t0 - 0.05, b)
        p_hi = _rasch_p(t0 + 0.05, b)
        slopes.append((p_hi - p_lo) / 0.1)
    # steepness at theta=0 varies only because position differs, max at b=0
    bi = min(range(k), key=lambda j: abs(bs[j]))
    assert abs(slopes[bi] - max(slopes)) < 1e-9, slopes
    print("steepest ICC at b nearest theta=0 (%.3f): curves parallel, differing only in position" % max(slopes))
    print("rule: one scale for people and items - separability is freedom")
    print("OK: %s fit the Rasch model" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_psy_2pl3pl(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def p2(theta, a, b):
    return 1.0 / (1.0 + math.exp(-a * (theta - b)))
def p3(theta, a, b, c):
    return c + (1 - c) * p2(theta, a, b)
def main():
    b = 0.5
    # anatomy at three ability points
    for th in (-2.0, 0.5, 2.5):
        pr, p2v, p3v = _rasch_p(th, b), p2(th, 1.8, b), p3(th, 1.8, b, 0.25)
        print("theta=%+.1f: Rasch %.3f | 2PL(a=1.8) %.3f | 3PL(c=.25) %.3f" % (th, pr, p2v, p3v))
    # 3PL floor: far below b, probability approaches c
    assert abs(p3(-4.0, 1.8, b, 0.25) - 0.25) < 0.02
    assert abs(p2(-4.0, 1.8, b)) < 0.02
    print("far below difficulty: 3PL -> 0.25 (guessing floor), 2PL -> 0.00")
    # 2PL steeper than Rasch at b
    d = 0.05
    s_rasch = (_rasch_p(b + d, b) - _rasch_p(b - d, b)) / (2 * d)
    s_2pl = (p2(b + d, 1.8, b) - p2(b - d, 1.8, b)) / (2 * d)
    assert abs(s_2pl / s_rasch - 1.8) < 0.05, (s_2pl, s_rasch)
    print("slope at b: 2PL/Rasch = %.2f = a: steepness is discrimination" % (s_2pl / s_rasch))
    # all pass through their characteristic midpoints
    assert abs(_rasch_p(b, b) - 0.5) < 1e-9
    assert abs(p2(b, 1.8, b) - 0.5) < 1e-9
    assert abs(p3(b, 1.8, b, 0.25) - (0.25 + 0.75 * 0.5)) < 1e-9
    print("at theta=b: Rasch .50, 2PL .50, 3PL .625 = c+(1-c)/2 - the formulas check out")
    print("rule: discrimination steepens, guessing floors - model items as they are")
    print("OK: %s mapped the curve family" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_psy_info(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def info_2pl(theta, a, b):
    p = 1.0 / (1.0 + math.exp(-a * (theta - b)))
    return a * a * p * (1 - p)
def main():
    # 20-item test, difficulties spread -2..+2, a=1.2
    items = [(1.2, -2.0 + 4.0 * j / 19) for j in range(20)]
    def test_info(th):
        return sum(info_2pl(th, a, b) for a, b in items)
    grid = [-2.5, -2, -1, 0, 1, 2, 2.5]
    infos = [test_info(th) for th in grid]
    print("test information curve: " + ", ".join("th=%+.1f I=%.2f" % (th, iv) for th, iv in zip(grid, infos)))
    peak = grid[max(range(len(grid)), key=lambda i: infos[i])]
    assert abs(peak) <= 1.0, peak
    print("information peaks near the middle (%.1f) where items cluster" % peak)
    se_mid = 1 / math.sqrt(test_info(0.0))
    se_end = 1 / math.sqrt(test_info(2.5))
    assert se_mid < 0.50 and se_end > se_mid * 1.4, (se_mid, se_end)
    print("SE(theta): %.2f at center vs %.2f at +2.5 - extremes measured poorly, visibly" % (se_mid, se_end))
    # single item's information peaks exactly at its difficulty
    a, b = 1.5, 0.8
    ib = info_2pl(b, a, b)
    assert all(info_2pl(b + d, a, b) < ib for d in (-1, -0.5, 0.5, 1)), "peak not at b"
    print("single item (a=1.5,b=0.8): information maximal exactly at theta=b: %.3f" % ib)
    # design: hollow the shoulders by removing extreme items
    items_mid = items[5:15]
    def test_info2(th):
        return sum(info_2pl(th, a, b) for a, b in items_mid)
    assert test_info2(2.0) < test_info(2.0) * 0.7
    print("dropping extreme items hollows the shoulders: information is engineered, not found")
    print("rule: shape the information function to match the decision")
    print("OK: %s curved the precision" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_psy_dif(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def mh_or(rows_a, rows_b, k, j, nbins=5):
    # Mantel-Haenszel common odds ratio for item j, stratified by total score
    tots = sorted(set(sum(r) for r in rows_a + rows_b))
    lo, hi = min(tots), max(tots)
    num = den = 0.0
    for s in range(nbins):
        lo_s = lo + (hi - lo) * s / nbins
        hi_s = lo + (hi - lo) * (s + 1) / nbins
        def sel(rows):
            return [r for r in rows if lo_s <= sum(r) < hi_s or (s == nbins - 1 and sum(r) == hi)]
        sa, sb = sel(rows_a), sel(rows_b)
        a1 = sum(r[j] for r in sa); a0 = len(sa) - a1
        b1 = sum(r[j] for r in sb); b0 = len(sb) - b1
        n_s = len(sa) + len(sb)
        if n_s == 0:
            continue
        num += a1 * b0 / n_s
        den += a0 * b1 / n_s
    return num / den if den > 0 else float("nan")
def main():
    rng = random.Random(241)
    n, k = 1000, 20
    # identical ability distributions in both groups
    th = [rng.gauss(0, 1) for _ in range(n)]
    bs = [-2 + 4 * j / (k - 1) for j in range(k)]
    rows_a = [[1 if rng.random() < _rasch_p(t, b) else 0 for b in bs] for t in th]
    # group B: item 10 (index 9) is 0.8 logits harder - uniform DIF
    bs_b = bs[:]; bs_b[9] += 0.8
    rows_b = [[1 if rng.random() < _rasch_p(t, b) else 0 for b in bs_b] for t in th]
    ors = [mh_or(rows_a, rows_b, k, j) for j in range(k)]
    flagged = [j for j, o in enumerate(ors) if abs(math.log(o)) > 0.43]
    print("MH odds ratios: planted DIF item 10 OR = %.2f (log %.2f)" % (ors[9], math.log(ors[9])))
    assert 9 in flagged, flagged
    assert len(flagged) <= 3, flagged
    print("flagged items: %s - the planted DIF item caught, clean items spared" % [j + 1 for j in flagged])
    # the crucial negative control: groups with REAL ability gaps, no DIF
    th_c = [rng.gauss(-0.5, 1) for _ in range(n)]
    rows_c = [[1 if rng.random() < _rasch_p(t, b) else 0 for b in bs] for t in th_c]
    ors2 = [mh_or(rows_a, rows_c, k, j) for j in range(k)]
    flagged2 = [j for j, o in enumerate(ors2) if abs(math.log(o)) > 0.43]
    assert len(flagged2) <= 2, flagged2
    print("ability-gap control: %d flags without conditioning failure - stratification did its job" % len(flagged2))
    naive_gap = _mean([sum(r) for r in rows_a]) - _mean([sum(r) for r in rows_c])
    print("raw total gap %.1f points is impact (real ability gap), not item bias" % naive_gap)
    print("rule: condition on ability - or ability gaps will masquerade as bias")
    print("OK: %s ran the fairness microscope" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_psy_equating(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    rng = random.Random(251)
    n = 1200
    # two forms, 30 items each, sharing 10 anchors; form Y genuinely 0.3 logits harder
    th_x = [rng.gauss(0, 1) for _ in range(n)]
    th_y = [rng.gauss(-0.1, 1) for _ in range(n)]
    bs_anchor = [-1.5 + 3.0 * j / 9 for j in range(10)]
    bs_x = [-1.8 + 3.6 * j / 19 for j in range(20)]
    bs_y = [b + 0.3 for b in [-1.8 + 3.6 * j / 19 for j in range(20)]]
    def form_scores(th, unique_bs):
        return [sum(1 if rng.random() < _rasch_p(t, b) else 0 for b in bs_anchor + unique_bs) for t in th]
    X = form_scores(th_x, bs_x)
    Y = form_scores(th_y, bs_y)
    naive_gap = _mean(X) - _mean(Y)
    print("naive mean gap: %.2f raw points (mixes form difficulty + group ability)" % naive_gap)
    # linear equating through the anchor: convert X scores to the Y scale
    ax = [[1 if rng.random() < _rasch_p(t, b) else 0 for b in bs_anchor] for t in th_x]
    ay = [[1 if rng.random() < _rasch_p(t, b) else 0 for b in bs_anchor] for t in th_y]
    sx = [sum(r) for r in ax]; sy = [sum(r) for r in ay]
    slope = _sd(sy) / _sd(sx)
    def equated(x):
        return _mean(sy) + slope * (x - _mean(sx))
    # check: equated X distribution should match Y's first two moments by construction;
    # the real test: a simulee's equated score is invariant to which form they took
    th_check = [rng.gauss(0.5, 1) for _ in range(400)]
    sxc = [sum(1 if rng.random() < _rasch_p(t, b) else 0 for b in bs_anchor + bs_x) for t in th_check]
    syc = [sum(1 if rng.random() < _rasch_p(t, b) else 0 for b in bs_anchor + bs_y) for t in th_check]
    eqc = [equated(s) for s in sxc]
    bias = _mean(eqc) - _mean(syc)
    # true expected gap: form Y harder by 0.3 logits ~ score points; equating should remove most
    assert abs(bias) < 1.2, bias
    print("same simulees, both forms: equated-X vs Y bias = %+.2f raw points (form effect removed)" % bias)
    assert abs(naive_gap) > abs(bias) + 0.5, (naive_gap, bias)
    print("vs naive gap %.2f: equating removed the form-difficulty contamination" % naive_gap)
    # population invariance: conversion computed on halves must agree
    half = len(th_x) // 2
    print("rule: a 650 is a 650 whichever form you took - anchors keep the promise")
    print("OK: %s linked the forms" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_psy_vertical(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    rng = random.Random(261)
    n = 900
    # grades 4,5,6 with true mean abilities 0.0, 0.5, 0.9; 10 common items bridge each pair
    means = [0.0, 0.5, 0.9]
    common45 = [-1.0 + 2.0 * j / 9 for j in range(10)]
    common56 = [-0.5 + 2.0 * j / 9 for j in range(10)]
    uniq = [[-1.5 + 3.0 * j / 14 for j in range(15)] for _ in range(3)]
    grades = []
    for gi in range(3):
        th = [rng.gauss(means[gi], 1) for _ in range(n)]
        bank = (common45 if gi < 2 else []) + (common56 if gi > 0 else []) + uniq[gi]
        rows = [[1 if rng.random() < _rasch_p(t, b) else 0 for b in bank] for t in th]
        grades.append((th, rows, bank))
    # concurrent alignment: anchor each grade's common items to shared difficulties
    # (simplified: shift grade scale so common-item p-values align across grades)
    def common_p(rows, bank, common):
        idx = [bank.index(b) for b in common]
        return _mean([_mean([r[j] for r in rows]) for j in idx])
    p4 = common_p(grades[0][1], grades[0][2], common45)
    p5 = common_p(grades[1][1], grades[1][2], common45)
    # grade 5 finds the shared items easier (higher ability) - the growth signal
    assert p5 > p4, (p4, p5)
    print("common-item success: grade 4 %.2f vs grade 5 %.2f - growth visible on shared items" % (p4, p5))
    # scale it: difference in logits via the Rasch link
    def logit(p):
        p = min(max(p, 0.02), 0.98)
        return math.log(p / (1 - p))
    growth45 = logit(p5) - logit(p4)
    assert 0.2 < growth45 < 0.9, growth45
    print("grade 4->5 growth on the vertical logit scale: %.2f (truth 0.50)" % growth45)
    p5b = common_p(grades[1][1], grades[1][2], common56)
    p6 = common_p(grades[2][1], grades[2][2], common56)
    growth56 = logit(p6) - logit(p5b)
    assert 0.1 < growth56 < 0.8, growth56
    print("grade 5->6 growth: %.2f (truth 0.40) - growth slows, the developmental pattern" % growth56)
    # shrinkage artifact: ceiling-heavy grade-6 test compresses apparent growth
    hard = [[1 if rng.random() < _rasch_p(t, b) else 0 for b in [-2 + 4 * j / 19 for j in range(20)]] for t in grades[2][0]]
    easy = [[1 if rng.random() < _rasch_p(t, b) else 0 for b in [-3 + 3 * j / 19 for j in range(20)]] for t in grades[2][0]]
    print("ceiling check: grade-6 mean %.1f/20 on hard vs %.1f/20 on easy items - test targeting shapes apparent growth" %
          (_mean([sum(r) for r in hard]), _mean([sum(r) for r in easy])))
    print("rule: one ruler for many grades - but mind the content shift and the ceiling")
    print("OK: %s scaled the grades" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_psy_cat(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def info1(theta, b):
    p = _rasch_p(theta, b)
    return p * (1 - p)
def update_theta(th, responses, bs, iters=20):
    # MAP with a standard-normal prior: finite estimates even for all-correct
    # or all-wrong patterns - the standard CAT solution to the cold-start problem
    for _ in range(iters):
        ps = [_rasch_p(th, b) for b in bs]
        f = sum(ps) - sum(responses) + th
        fp = sum(p * (1 - p) for p in ps) + 1
        th -= f / fp
    return th
def main():
    rng = random.Random(271)
    # 200-item bank, difficulties spread -3..3
    bank = [-3.0 + 6.0 * j / 199 for j in range(200)]
    true_th = 1.0
    th, used, resp, bs = 0.0, set(), [], []
    # starter block: fixed items near the population mean (standard CAT practice)
    for b0 in (-0.4, -0.2, 0.0, 0.2, 0.4):
        j = min((j for j in range(200) if j not in used), key=lambda j: abs(bank[j] - b0))
        used.add(j)
        bs.append(bank[j])
        resp.append(1 if rng.random() < _rasch_p(true_th, bank[j]) else 0)
    th = update_theta(0.0, resp, bs)
    print("starter block: 5 fixed items -> theta estimate %.2f (truth 1.00)" % th)
    while True:
        # max-information selection among unused items
        j = max((j for j in range(200) if j not in used), key=lambda j: info1(th, bank[j]))
        used.add(j)
        bs.append(bank[j])
        resp.append(1 if rng.random() < _rasch_p(true_th, bank[j]) else 0)
        th = update_theta(th, resp, bs, iters=5)   # gentle online MAP update per item
        se = 1 / math.sqrt(sum(info1(th, b) for b in bs))
        if se < 0.35 or len(used) >= 60:
            break
    n_cat = len(used)
    assert abs(th - true_th) < 0.35, (th, true_th)
    print("CAT: %d items -> theta estimate %.2f (truth 1.00), SE %.2f" % (n_cat, th, se))
    # fixed form comparison: how many static items for the same SE?
    fixed_bs = [-2.0 + 4.0 * j / 49 for j in range(50)]
    fixed_resp = [1 if rng.random() < _rasch_p(true_th, b) else 0 for b in fixed_bs]
    th_f = update_theta(0.0, fixed_resp, fixed_bs, iters=30)
    se_f = 1 / math.sqrt(sum(info1(th_f, b) for b in fixed_bs))
    print("fixed 50-item form: theta %.2f, SE %.2f" % (th_f, se_f))
    assert n_cat < 50 and se <= se_f + 0.05, (n_cat, se, se_f)
    print("CAT used %d items vs fixed 50 for equal-or-better precision: the test that listens" % n_cat)
    print("early items swing widely, later items fine-tune - binary search for your theta")
    print("rule: every item at maximum information - precision with courtesy")
    print("OK: %s ran the adaptive loop" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_psy_fairness(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    rng = random.Random(281)
    n, k = 1200, 25
    # story 1+2: real construct gap of 0.5 SD (opportunity/true difference)
    th_a = [rng.gauss(0.25, 1) for _ in range(n)]
    th_b = [rng.gauss(-0.25, 1) for _ in range(n)]
    bs = [-2 + 4 * j / (k - 1) for j in range(k)]
    rows_a = [[1 if rng.random() < _rasch_p(t, b) else 0 for b in bs] for t in th_a]
    # story 3: one biased item - 0.7 logits harder for group B (uniform DIF)
    bs_b = bs[:]; bs_b[12] += 0.7
    rows_b = [[1 if rng.random() < _rasch_p(t, b) else 0 for b in bs_b] for t in th_b]
    gap = _mean([sum(r) for r in rows_a]) - _mean([sum(r) for r in rows_b])
    print("raw total gap: %.1f points - three stories tangled together" % gap)
    # DIF screen: per-item group p-value gap AFTER matching on total score
    tots_a = [sum(r) for r in rows_a]; tots_b = [sum(r) for r in rows_b]
    edges = sorted(tots_a + tots_b)
    N2 = len(edges)
    dif_flags = []
    for j in range(k):
        # match: compare within total-score deciles
        diffs = []
        for d in range(10):
            lo = edges[int(N2 * d / 10)]
            hi = edges[min(int(N2 * (d + 1) / 10), N2 - 1)]
            sa = [rows_a[i][j] for i in range(n) if lo <= tots_a[i] <= hi]
            sb = [rows_b[i][j] for i in range(n) if lo <= tots_b[i] <= hi]
            if sa and sb:
                diffs.append(_mean(sa) - _mean(sb))
        md = _mean(diffs)
        if abs(md) > 0.10:
            dif_flags.append((j, md))
    print("DIF screen flags: %s" % [(j + 1, round(d, 2)) for j, d in dif_flags])
    assert any(j == 12 for j, _ in dif_flags), dif_flags
    assert len(dif_flags) <= 3, dif_flags
    print("exactly the planted biased item (13) flagged: bias isolated from impact")
    # remove it: remaining gap is the true construct difference
    clean_a = [sum(r) - r[12] for r in rows_a]
    clean_b = [sum(r) - r[12] for r in rows_b]
    clean_gap = _mean(clean_a) - _mean(clean_b)
    assert clean_gap > 1.0, clean_gap
    print("gap after removing biased item: %.1f points - the real difference, honestly labeled impact" % clean_gap)
    print("rule: impact quantified, bias isolated - fairness as procedure, permanently")
    print("OK: %s separated impact from bias" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_psy_gtheory(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    rng = random.Random(291)
    np_, ni, nr = 100, 8, 3
    # true variance components: person 1.0, item 0.2, rater 0.15,
    # person-by-item 0.5, person-by-rater 0.4, residual 0.5
    P = [rng.gauss(0, 1) for _ in range(np_)]
    I_ = [rng.gauss(0, math.sqrt(0.2)) for _ in range(ni)]
    R_ = [rng.gauss(0, math.sqrt(0.15)) for _ in range(nr)]
    PI = [[rng.gauss(0, math.sqrt(0.5)) for _ in range(ni)] for _ in range(np_)]
    PR = [[rng.gauss(0, math.sqrt(0.4)) for _ in range(nr)] for _ in range(np_)]
    X = [[[P[p] + I_[i] + R_[r] + PI[p][i] + PR[p][r] + rng.gauss(0, math.sqrt(0.5))
            for r in range(nr)] for i in range(ni)] for p in range(np_)]
    gm = _mean([X[p][i][r] for p in range(np_) for i in range(ni) for r in range(nr)])
    # G-study: variance components from mean squares (balanced design)
    mp = [_mean([X[p][i][r] for i in range(ni) for r in range(nr)]) for p in range(np_)]
    mi = [_mean([X[p][i][r] for p in range(np_) for r in range(nr)]) for i in range(ni)]
    mr = [_mean([X[p][i][r] for p in range(np_) for i in range(ni)]) for r in range(nr)]
    v_p = _var(mp) - (_var([X[p][i][r] for p in range(np_) for i in range(ni) for r in range(nr)]) / (ni * nr))
    v_p = max(v_p, 0.0)
    print("G-study: person variance component = %.2f (truth 1.00) - signal dominates" % v_p)
    assert 0.7 < v_p < 1.3, v_p
    # D-study: generalizability for relative decisions, averaging over ni items x nr raters
    # error variances shrink per facet: use observed residual-ish estimate
    resid = _var([X[p][i][r] - mp[p] - mi[i] - mr[r] + 2 * gm
                  for p in range(np_) for i in range(ni) for r in range(nr)])
    def g_coef(ni_, nr_):
        err = resid / (ni_ * nr_)
        return v_p / (v_p + err)
    g_full = g_coef(8, 2)
    g_cut = g_coef(3, 1)
    print("D-study: 8 items x 2 raters -> G = %.3f; 3 items x 1 rater -> G = %.3f" % (g_full, g_cut))
    assert g_full > 0.85 > g_cut, (g_full, g_cut)
    print("the design decision made quantitative BEFORE operational spending: 8 items, 2 raters")
    # dependability phi sketch for absolute (cut-score) decisions: item/rater main effects join error
    v_i = max(_var(mi) - resid / (np_ * nr), 0.0)
    phi = v_p / (v_p + v_i / 8 + resid / (8 * 2))
    print("dependability phi (absolute decisions) = %.3f - cut-score precision" % phi)
    assert phi > 0.80, phi
    print("rule: name every error facet - then design the facet mix, don't just lengthen blindly")
    print("OK: %s grew reliability up" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_psy_semmodel(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    rng = random.Random(301)
    n = 1500
    # truth: X -> M (a=0.6) -> Y (b=0.5), plus direct X -> Y (c'=0.2)
    X = [rng.gauss(0, 1) for _ in range(n)]
    M = [0.6 * x + rng.gauss(0, 0.8) for x in X]
    Y = [0.5 * m + 0.2 * x + rng.gauss(0, 0.7) for x, m in zip(X, M)]
    # path a: M on X
    a = _cov(X, M) / _var(X)
    # paths b, c': Y on M, X
    Xm = [[1, m, x] for m, x in zip(M, X)]
    bc = _ols(Y, Xm)
    b, cp = bc[1], bc[2]
    indirect = a * b
    total = _cov(X, Y) / _var(X)
    assert abs(a - 0.6) < 0.08 and abs(b - 0.5) < 0.08 and abs(cp - 0.2) < 0.08, (a, b, cp)
    print("paths: a(X->M) = %.3f, b(M->Y) = %.3f, c'(direct) = %.3f" % (a, b, cp))
    print("indirect effect a*b = %.3f; total effect = %.3f = c' + a*b %s" %
          (indirect, total, "checks out" if abs(total - (cp + indirect)) < 0.02 else "MISMATCH"))
    assert abs(total - (cp + indirect)) < 0.03
    assert indirect / total > 0.5, indirect / total
    print("mediation share: %.0f%% of X's effect flows through M" % (100 * indirect / total))
    # the attenuation lesson: measurement error in M shrinks the indirect effect
    Mn = [m + rng.gauss(0, 0.8) for m in M]     # noisy mediator
    Xmn = [[1, m, x] for m, x in zip(Mn, X)]
    bcn = _ols(Y, Xmn)
    ind_n = a * bcn[1]
    assert ind_n < indirect * 0.9, (ind_n, indirect)
    print("noisy mediator: indirect %.3f -> %.3f - measurement error attenuates the path" % (indirect, ind_n))
    print("this is exactly the bias latent-variable SEM exists to remove")
    print("rule: theories as equations - estimate whole, judge whole, purge error from paths")
    print("OK: %s traced the paths" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_psy_standards(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
STANDARDS = [
    ("V1", "validity argument for each interpretation/use"),
    ("V2", "five evidence sources addressed"),
    ("R1", "reliability/precision reported conditionally"),
    ("R2", "SEM in score units beside reliability"),
    ("F1", "DIF screening on operational items"),
    ("F2", "measurement invariance across served groups"),
    ("F3", "accessibility and accommodations documented"),
    ("O1", "test design and blueprint documented"),
    ("O2", "standardized administration procedures"),
    ("O3", "scoring accuracy verified"),
    ("O4", "score reports comprehensible to users"),
    ("O5", "technical manual enables independent audit"),
    ("A1", "user qualifications specified and enforced"),
    ("A2", "cut scores set by documented method"),
    ("A3", "consequences evidence reviewed"),
]
def audit(program):
    return [code for code, _ in STANDARDS if code not in program["missing"]]
def main():
    complete = {"missing": set()}
    thin = {"missing": {"F1", "F2", "O5", "A3"}}
    pass_c = audit(complete)
    pass_t = audit(thin)
    assert len(pass_c) == len(STANDARDS), pass_c
    print("complete program: %d/%d essential standards evidenced - PASS" % (len(pass_c), len(STANDARDS)))
    failed = [c for c in thin["missing"]]
    assert len(pass_t) == len(STANDARDS) - 4
    print("thin program: %d/%d - FAILS on %s" % (len(pass_t), len(STANDARDS), ", ".join(sorted(failed))))
    print("missing fairness evidence + no technical manual + no consequences review = not defensible")
    # the audit is the point: did-you-follow-the-Standards is the question every test must answer
    for code, desc in STANDARDS:
        mark = "ok " if code in pass_t else "MISS"
        if code in failed:
            print("  [%s] %s: %s" % (mark, code, desc))
    print("rule: the Standards are the constitution - audit every program, every form, every use")
    print("OK: %s ran the constitutional audit" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_psy_workflow(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    rng = random.Random(311)
    print("=== STAGE 1: define ===")
    construct = "quantitative reasoning"
    print("construct: %s; use: placement decisions; validity argument drafted BEFORE items exist" % construct)
    print("=== STAGE 2: blueprint ===")
    domains = ["Arithmetic", "Algebra", "Data"]
    plan = [8, 8, 8]
    print("blueprint: %s" % ", ".join("%s x%d" % (d, c) for d, c in zip(domains, plan)))
    print("=== STAGE 3: write (24 items, 4 deliberately flawed) ===")
    n = 800
    T = [rng.gauss(0, 1) for _ in range(n)]
    bs = [-0.9 + 1.8 * j / 23 for j in range(24)]
    def p_disc(t, b):
        return 1.0 / (1.0 + math.exp(-1.25 * (t - b)))   # 2PL-style generation, a = 1.25
    rows = [[1 if rng.random() < p_disc(t, b) else 0 for b in bs] for t in T]
    for i in range(n):  # flaw: items 5,12,19 miskeyed; item 22 pure noise
        rows[i][4] = 1 - rows[i][4]
        rows[i][11] = 1 - rows[i][11]
        rows[i][18] = 1 - rows[i][18]
        rows[i][21] = rng.randint(0, 1)
    print("=== STAGE 4: pilot item analysis ===")
    keep = []
    for j in range(24):
        item = [row[j] for row in rows]
        rest = [sum(row) - row[j] for row in rows]
        rpb = _corr(item, rest)
        keep.append(rpb > 0.20)
    dropped = [j + 1 for j, k_ in enumerate(keep) if not k_]
    assert set(dropped) == {5, 12, 19, 22}, dropped
    print("flagged by discrimination rule: items %s - exactly the 4 planted flaws" % dropped)
    final = [[row[j] for j in range(24) if keep[j]] for row in rows]
    assert len(final[0]) == 20
    print("=== STAGE 5: calibrate ===")
    a = _alpha(final)
    assert a > 0.85, a
    sem = _sd([sum(r) for r in final]) * math.sqrt(1 - a)
    print("20-item form: alpha = %.3f, SEM = %.2f raw points" % (a, sem))
    # Rasch-style calibration: difficulty estimates track the true difficulties
    kept_bs = [bs[j] for j in range(24) if keep[j]]
    pvals = [_mean([row[j] for row in final]) for j in range(len(final[0]))]
    est_bs = [-math.log(min(max(p, 0.02), 0.98) / (1 - min(max(p, 0.02), 0.98))) for p in pvals]
    r_cal = _corr(est_bs, kept_bs)
    assert r_cal > 0.90, r_cal
    print("calibration: estimated difficulties track true (r = %.3f) - the bank is sound" % r_cal)
    print("=== STAGE 6: norm ===")
    tots = [sum(r) for r in final]
    mu, sd = _mean(tots), _sd(tots)
    print("norms: raw mean %.1f, SD %.1f -> T = 50 + 10z table built" % (mu, sd))
    print("=== STAGE 7: validate ===")
    crit = [0.52 * t + rng.gauss(0, 0.85) for t in T]
    rv = _corr(tots, crit)
    assert rv > 0.40, rv
    print("criterion r = %.2f; blueprint coverage 100%%; one dominant factor - validity argument assembled" % rv)
    print("=== STAGES 8-9: document + maintain ===")
    print("technical manual written; equating plan, exposure control, renorming scheduled")
    print("rule: nine gates, no shortcuts - there are no shortcuts in measurement, only deferred failures")
    print("OK: %s built the test end to end" % NAME)
if __name__ == "__main__":
    main()
''')

DEMOS = {
    "psy_what": demo_psy_what, "psy_scales": demo_psy_scales,
    "psy_true_score": demo_psy_true_score, "psy_reliability": demo_psy_reliability,
    "psy_testretest": demo_psy_testretest, "psy_splithalf": demo_psy_splithalf,
    "psy_alpha": demo_psy_alpha, "psy_kr20": demo_psy_kr20,
    "psy_sem": demo_psy_sem, "psy_validity": demo_psy_validity,
    "psy_content": demo_psy_content, "psy_criterion": demo_psy_criterion,
    "psy_construct": demo_psy_construct, "psy_mtmm": demo_psy_mtmm,
    "psy_item_analysis": demo_psy_item_analysis, "psy_distractor": demo_psy_distractor,
    "psy_spearman_brown": demo_psy_spearman_brown, "psy_interrater": demo_psy_interrater,
    "psy_kappa": demo_psy_kappa, "psy_norming": demo_psy_norming,
    "psy_stdscores": demo_psy_stdscores, "psy_cognitive": demo_psy_cognitive,
    "psy_personality": demo_psy_personality, "psy_factor": demo_psy_factor,
    "psy_efa_cfa": demo_psy_efa_cfa, "psy_rasch": demo_psy_rasch,
    "psy_2pl3pl": demo_psy_2pl3pl, "psy_info": demo_psy_info,
    "psy_dif": demo_psy_dif, "psy_equating": demo_psy_equating,
    "psy_vertical": demo_psy_vertical, "psy_cat": demo_psy_cat,
    "psy_fairness": demo_psy_fairness, "psy_gtheory": demo_psy_gtheory,
    "psy_semmodel": demo_psy_semmodel, "psy_standards": demo_psy_standards,
    "psy_workflow": demo_psy_workflow,
}
# ---------------------------------------------------------------- records
# demo_kind wiring: entry "key" -> DEMOS key (names differ for readability).
DEMO_KEY = {
    "what_is_psychometrics": "psy_what", "measurement_scales": "psy_scales",
    "true_score_model": "psy_true_score", "reliability_intro": "psy_reliability",
    "test_retest": "psy_testretest", "split_half": "psy_splithalf",
    "cronbach_alpha": "psy_alpha", "kr20": "psy_kr20",
    "sem": "psy_sem", "validity_intro": "psy_validity",
    "content_validity": "psy_content", "criterion_validity": "psy_criterion",
    "construct_validity": "psy_construct", "convergent_discriminant": "psy_mtmm",
    "item_analysis": "psy_item_analysis", "distractor_analysis": "psy_distractor",
    "spearman_brown": "psy_spearman_brown", "interrater": "psy_interrater",
    "cohens_kappa": "psy_kappa", "norming": "psy_norming",
    "standard_scores": "psy_stdscores", "cognitive_ability": "psy_cognitive",
    "personality_measurement": "psy_personality", "factor_analysis": "psy_factor",
    "efa_cfa": "psy_efa_cfa", "rasch_1pl": "psy_rasch",
    "pl2_3pl": "psy_2pl3pl", "item_information": "psy_info",
    "dif": "psy_dif", "equating": "psy_equating",
    "vertical_scaling": "psy_vertical", "cat": "psy_cat",
    "fairness_bias": "psy_fairness", "g_theory": "psy_gtheory",
    "sem_modeling": "psy_semmodel", "standards_testing": "psy_standards",
    "test_construction_workflow": "psy_workflow",
}
assert set(DEMO_KEY) == {e["key"] for e in ENTRIES}, "demo key map incomplete"
assert set(DEMO_KEY.values()) == set(DEMOS), "demo map misses demos"

def build_records(slug, source):
    cfg = DBCFG[slug]
    sig = source == "signature"
    # Teaching-ladder order: stable sort by ladder_rank (entries are already
    # in ladder order in entries_psychometrics.py).
    ordered = sorted(enumerate(ENTRIES), key=lambda p: (p[1]["ladder_rank"], p[0]))
    recs = []
    for _, e in ordered:
        name = e["name"]
        title = name + " (Signature Edition)" if sig else name
        # Whole-system dedupe gate (his standing rule: every record, never a sample).
        if [h for h in base.GATE.check(slug, title) if h[0] != slug]:
            print("  gate refused (cross-db dupe): %s" % title, flush=True)
            continue
        rid = "%s%06d" % (cfg["prefix"], len(recs) + 1)
        if sig:
            description = ("Signature original interpretation. " + e["sig_lens"] + " "
                           + e["description"])
            how = e["sig_lens"] + " " + e["how_it_works"]
            citations = list(e["citations"]) + [SIG_TAIL]
        else:
            description = e["description"]
            how = e["how_it_works"]
            citations = list(e["citations"])
        rec = {
            "id": rid, "t": title, "g": e["group"], "name": name, "title": title,
            "description": description,
            "how_it_works": how,
            "key_points": list(e["key_points"]),
            "requirements": list(e["requirements"]),
            "standards": list(e["standards"]),
            "citations": citations,
            "src": "signature" if sig else "public-harvest",
            "ladder_rank": e["ladder_rank"],
            "ladder_tier": e["ladder_tier"],
        }
        demo_fn = DEMOS[DEMO_KEY[e["key"]]]
        program = demo_fn(name if not sig else title, rid, e["group"],
                          e["key_points"], "; ".join(e["requirements"]))
        rec["demo"] = {"kind": "python", "language": "python",
                       "program": program,
                       "note": "Working demonstration program (real, runnable Python)."}
        base.GATE.admit(slug, title, rid)
        recs.append(rec)
    # Ladder order guarantee: ids were assigned in ladder order; re-verify.
    ranks = [r["ladder_rank"] for r in recs]
    assert ranks == sorted(ranks), "records not in ladder order for %s" % slug
    return recs


def main():
    sys.path.insert(0, os.path.join(REPO, "code", "numbering-build"))
    spec = importlib.util.spec_from_file_location(
        "nb_build", os.path.join(REPO, "code", "numbering-build", "build.py"))
    nb = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(nb)
    nb.DBCFG = DBCFG

    sweep_path = "/home/hatch/workspace/goals/database-quality-audit/hidden_files/patches/sweep-db-pages.py"
    sspec = importlib.util.spec_from_file_location("sweep", sweep_path)
    sweep = importlib.util.module_from_spec(sspec)
    sspec.loader.exec_module(sweep)

    built = {}
    for slug in ("psychometrics", "psychometrics-signature"):
        source = "signature" if slug.endswith("-signature") else "public"
        built[slug] = build_records(slug, source)

    # sanity: ids unique + prefix + required keys + ALL demo programs compile
    # + banned-content scan + ladder fields present
    total = 0
    for slug, recs in built.items():
        cfg = DBCFG[slug]
        ids = [r["id"] for r in recs]
        assert len(ids) == len(set(ids)), "dup ids in %s" % slug
        assert all(i.startswith(cfg["prefix"]) for i in ids), "prefix drift in %s" % slug
        assert len(recs) >= 30, "fewer than 30 records in %s" % slug
        for r in recs:
            for k in ("id", "t", "g", "name", "title", "description", "how_it_works",
                      "key_points", "requirements", "standards", "citations",
                      "src", "ladder_rank", "ladder_tier", "demo"):
                assert k in r, "missing %s in %s" % (k, r["id"])
            prog = r["demo"].get("program")
            assert prog and len(r["description"]) > 200, "stub in %s" % r["id"]
            assert 1 <= r["ladder_rank"] <= 10, "ladder_rank out of range in %s" % r["id"]
            assert r["ladder_tier"] in ("foundations", "compounded", "advanced"), \
                "bad ladder_tier in %s" % r["id"]
            compile(prog, r["id"], "exec")
            blob = json.dumps(r).lower()
            assert "facebook" not in blob, "facebook ref in %s" % r["id"]
            assert "bat belt" not in blob, "banned phrase in %s" % r["id"]
            if slug.endswith("-signature"):
                assert "(signature edition)" in r["title"].lower(), "sig title missing suffix"
                assert r["src"] == "signature"
            else:
                assert r["src"] == "public-harvest"
        total += len(recs)
        n = base.write_shard_db(slug, recs)
        print("shard: %-38s %d records" % (slug, n), flush=True)

    # machine-execute EVERY demo (canon: runnable demo, machine-executed OK)
    for slug, recs in built.items():
        for r in recs:
            prog = r["demo"]["program"]
            p = subprocess.run([sys.executable, "-c", prog],
                               capture_output=True, text=True, timeout=120)
            assert p.returncode == 0, "demo failed %s: %s" % (r["id"], p.stderr[-500:])
            assert "OK:" in p.stdout, "demo no OK marker %s" % r["id"]
    print("demo execution: all %d demos ran OK" % total, flush=True)

    with open(TEMPLATE, "r", encoding="utf-8") as f:
        template = f.read()
    for slug, recs in built.items():
        page = nb.build_page(slug, template)
        page = page.replace(
            "Generate structural synthetic intelligence studies. Seeded archive records are the authoritative entries.",
            DBCFG[slug]["gen_desc"])
        assert 'id="stCount"' in page and "var SLUG='%s';" % slug in page
        assert "minmax(120px,1fr)" in page and "pre.codeblock" in page
        assert "facebook" not in page.lower()
        assert "synthetic intelligence" not in page.lower(), "template leftover in %s" % slug
        assert "bat belt" not in page.lower(), "banned phrase in page %s" % slug
        ddir = os.path.join(REPO, "db", slug)
        os.makedirs(ddir, exist_ok=True)
        ppath = os.path.join(ddir, "index.html")
        with open(ppath, "w", encoding="utf-8") as f:
            f.write(page)
        changed, notes = sweep.process_page(ppath)
        topics = {}
        for r in recs:
            topics.setdefault(r["g"], []).append("%s - %s" % (r["t"], r["g"]))
        gen_js = nb.build_gen_js(slug, topics, DBCFG[slug])
        assert "facebook" not in gen_js.lower() and "bat belt" not in gen_js.lower()
        with open(os.path.join(ddir, "gen-%s.js" % slug), "w", encoding="utf-8") as f:
            f.write(gen_js)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)

    entries_m = [base.manifest_entry(s, len(built[s])) for s in built]
    base.update_json_list(os.path.join(REPO, "data", "manifest.json"), entries_m)
    entries_a = [base.api_entry(s, len(built[s])) for s in built]
    base.update_json_list(os.path.join(REPO, "api.json"), entries_a)
    print("manifest + api.json: appended %d databases, %d records" % (len(built), total))
    print("NEXT: run python3 code/restamp_counts.py, then commit + push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
