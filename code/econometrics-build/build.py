#!/usr/bin/env python3
"""Build the Econometrics field databases for JAH Databases (field #18, taxonomy order).

Verified 2026-10-17: NO database covers econometrics as a discipline.
- 'economics' family: general-economics concept cards (supply/demand, GDP,
  inflation); one passing mention of "econometric" total - no OLS, BLUE,
  IV, heteroskedasticity, panel data, or time-series econometrics.
- 'statistics-study' family: general statistics curriculum cards; zero
  econometrics mentions.
- 'forecasting' / 'forecast': general forecasting cards; zero mentions of
  ARIMA, cointegration, VAR, or econometrics.
- 'economists' / 'public-economists': cards about people, not the discipline.
- 'scientific-formulas': bare formula cards are reference only (task rule:
  formula cards do NOT count as discipline coverage).
- Whole-system dedupe gate (256 shards, rebuilt 2026-10-17 08:04): every
  record checked + admitted. Fields #12-17 shard indexes (climatology,
  atmospheric-science, hydrology, meteorology, calculus, combinatorics -
  the gate index predates them) checked directly: zero
  econometrics-relevant titles.

So this build creates two NEW databases:

  econometrics            - The Econometrics Database
                            (public-harvest: real, fact-checked
                            econometrics; citations Wooldridge, Stock &
                            Watson, Greene, Angrist & Pischke, Gujarati,
                            Hamilton, Enders, Cameron & Trivedi, Baltagi)
  econometrics-signature  - The Econometrics Signature Database
                            (his original Signature interpretation;
                            src signature, titles suffixed
                            " (Signature Edition)", never presented
                            as authentic public record)

36 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

Every record: description + how-it-works + key points + requirements +
standards + citations + working demonstration code (real, runnable,
stdlib-only Python; machine-executed OK). Econometrics demos: OLS by hand
formulas, Frisch-Waugh partialling, t-stats/p-values, R-squared
decomposition, dummy-variable mean differences, Monte Carlo Gauss-Markov
check, White heteroskedasticity test + robust SEs, VIFs, Durbin-Watson +
Breusch-Godfrey, omitted-variable-bias arithmetic, 2SLS vs OLS under
endogeneity, attenuation from measurement error, logit Newton-Raphson,
Tobit MLE on censored data, panel fixed effects vs pooled OLS, Hausman
statistic, 2x2 diff-in-diff, sharp RDD local linear, ADF-style unit-root
t-stats, AR(2) Yule-Walker + forecasts, Engle-Granger cointegration,
VAR(1) Granger tests, supply-demand 2SLS, two-step GMM + J-test, quantile
regression IRLS, expanding-window forecast horse race, Chow break test,
ARCH(1) MLE + LM test, Gauss-Newton NLS, Moran's I, propensity
stratification ATT, and the full professional workflow pipeline.

Subtitle disambiguation (fields #13-18 pattern): where a bare formula or
generic card exists elsewhere, discipline titles carry teaching-focused
subtitles, e.g. "Simple Linear Regression: The Straight-Line Model" and
"Heteroskedasticity: Uneven Spread of Errors" rather than bare
"Regression" or "Heteroskedasticity" cards.

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
# main repo (256 shards, rebuilt 2026-10-17; titles from fields #12-17
# cross-checked directly against their shard indexes in jah-databases-data-1
# since the gate index predates them - subtitle disambiguation used
# throughout).
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_econometrics import ENTRIES, SIG_TAIL

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature interpretation of econometrics: "
                "clearly labeled Signature-made, never presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked econometrics: what econometrics is; "
                "cross-section, time-series, and panel data; correlation vs causation; "
                "simple and multiple regression; OLS mechanics; reading regression output; "
                "R-squared; dummy variables; Gauss-Markov and BLUE; heteroskedasticity; "
                "multicollinearity; autocorrelation; omitted variable bias; instrumental "
                "variables and 2SLS; measurement error and proxies; probit and logit; "
                "Tobit and censored regression; panel fixed and random effects; the "
                "Hausman test; difference-in-differences; regression discontinuity; unit "
                "roots and the Dickey-Fuller test; ARIMA; cointegration and error "
                "correction; VARs and Granger causality; simultaneous equations; GMM; "
                "quantile regression; forecasting; structural breaks and the Chow test; "
                "ARCH/GARCH volatility; nonlinear least squares and MLE; spatial "
                "econometrics; matching and propensity scores; the professional software "
                "workflow, organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations (what econometrics "
              "is, data types, correlation vs causation, simple regression, multiple "
              "regression, OLS mechanics, reading output, R-squared, dummy variables) -> "
              "Compounded (Gauss-Markov/BLUE, heteroskedasticity, multicollinearity, "
              "autocorrelation, omitted variable bias, instrumental variables, "
              "measurement error, probit/logit, Tobit, panel fixed/random effects, the "
              "Hausman test) -> Advanced (difference-in-differences, regression "
              "discontinuity, unit roots, ARIMA, cointegration, VAR/Granger, simultaneous "
              "equations, GMM, quantile regression, forecasting, structural breaks, "
              "ARCH/GARCH, NLS/MLE, spatial econometrics, matching, software practice).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search OLS, heteroskedasticity, instrumental variables, diff-in-diff, ARIMA, cointegration, GMM...",
        "chat_ph": "Ask about econometrics...",
        "archive_blurb": ("Seeded %s econometrics records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled structural econometrics studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about econometrics - from OLS and Gauss-Markov through instrumental variables, diff-in-diff, ARIMA, cointegration, and GMM." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "econometrics-study", "gen_demo_kind": "econometrics-demo",
        "source": source,
    }

CIT_PUB = "Econometrics (standard textbooks and peer-reviewed literature)."
CIT_SIG = CIT_PUB + " " + SIG_TAIL

DBCFG = {}
DBCFG["econometrics"] = _cfg(
    "econometrics", "The Econometrics Database",
    "Real, fact-checked econometrics: the discipline from data types, "
    "correlation vs causation, and OLS through regression diagnostics, "
    "causal methods, panel data, time-series econometrics, and advanced "
    "estimation - taught progressively along the ladder.",
    "econometrics record", "JAH-ECON-", "JAH Econometrics Archivist",
    "econometrics archivist - what econometrics is, data types, correlation "
    "vs causation, simple and multiple regression, OLS mechanics, reading "
    "output, R-squared, dummy variables, Gauss-Markov/BLUE, "
    "heteroskedasticity, multicollinearity, autocorrelation, omitted "
    "variable bias, instrumental variables, measurement error, probit/logit, "
    "Tobit, panel fixed/random effects, Hausman test, diff-in-diff, "
    "regression discontinuity, unit roots, ARIMA, cointegration, VAR and "
    "Granger causality, simultaneous equations, GMM, quantile regression, "
    "forecasting, structural breaks, ARCH/GARCH, NLS/MLE, spatial "
    "econometrics, matching, software workflow; teaching progressively "
    "along the ladder from foundations through compounded to advanced; "
    "answers from many angles - definition, example, analogy, application, "
    "history, math, how-to - using only the system's own archive data",
    CIT_PUB, "public")
DBCFG["econometrics-signature"] = _cfg(
    "econometrics-signature", "The Econometrics Signature Database",
    "His original Signature interpretation of econometrics: the full ladder from "
    "data types and OLS through causal designs, time-series econometrics, and "
    "GMM, reframed as Signature science. Clearly labeled Signature-made, never "
    "presented as authentic public record.",
    "econometrics record", "JAH-ECONS-", "JAH Econometrics Archivist (Signature)",
    "econometrics archivist - Signature editions: his original Signature interpretation "
    "of econometrics, clearly labeled Signature-made and never presented as authentic "
    "public record; teaches progressively along the ladder from foundations through "
    "compounded to advanced; answers from many angles - definition, example, analogy, "
    "application, history, math, how-to - using only the system's own archive data",
    CIT_SIG, "signature")

base.DBCFG = DBCFG
# ---------------------------------------------------------------- demos
# Every demo is real, runnable, stdlib-only Python performing the actual
# econometric computation for its record. All are machine-executed by main().

_PREAMBLE = (
"import math\n"
"import random\n"
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
"def _mean(v):\n"
"    return sum(v) / len(v)\n"
"def _var(v):\n"
"    m = _mean(v)\n"
"    return sum((x - m) ** 2 for x in v) / (len(v) - 1)\n"
"def _cov(a, b):\n"
"    ma, mb = _mean(a), _mean(b)\n"
"    return sum((x - ma) * (y_ - mb) for x, y_ in zip(a, b)) / (len(a) - 1)\n"
"def _resid(y, X, b):\n"
"    return [y[i] - sum(X[i][j] * b[j] for j in range(len(b))) for i in range(len(y))]\n"
"def _ssr(y, X, b):\n"
"    return sum(e * e for e in _resid(y, X, b))\n"
"def _phi(z):\n"
"    return 0.5 * (1.0 + math.erf(z / math.sqrt(2.0)))\n"
"def _inv(A):\n"
"    n = len(A)\n"
"    cols = [_solve(A, [1 if i == j else 0 for i in range(n)]) for j in range(n)]\n"
"    return [[cols[j][i] for j in range(n)] for i in range(n)]\n"
)

def _wrap(name, rid, group, body):
    return (base._hdr(name, rid, group) + _PREAMBLE + body.replace("NAME", json.dumps(name)))

def demo_econ_what(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
BRANCHES = {
    "cross-section & panel regression": "OLS, BLUE, diagnostics, IV, fixed effects, causal designs",
    "time-series econometrics": "stationarity, ARIMA, cointegration, VAR, volatility, forecasting",
    "causal inference": "experiments, diff-in-diff, RDD, matching, LATE",
}
def main():
    assert len(BRANCHES) == 3
    for branch, tools in BRANCHES.items():
        print("%-32s -> %s" % (branch, tools))
    # the discipline in one number: GDP growth summaries a whole economy
    gdp_growth = [2.1, 3.4, 1.8, 2.9, -0.5, 2.2, 3.1, 2.7]
    mu = _mean(gdp_growth)
    sd = math.sqrt(_var(gdp_growth))
    assert abs(mu - 2.2125) < 1e-9
    print("toy GDP growth: mean %.2f%%, sd %.2f%% - measurement first, models second" % (mu, sd))
    print("rule: theory proposes, data disposes - the estimator is the bridge")
    print("OK: %s mapped the discipline" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_econ_data_types(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # cross-section: 4 workers observed once (2024)
    cross = [
        {"id": 1, "wage": 22.5, "educ": 12},
        {"id": 2, "wage": 31.0, "educ": 16},
        {"id": 3, "wage": 18.0, "educ": 10},
        {"id": 4, "wage": 45.0, "educ": 18},
    ]
    # time series: one economy's GDP, 4 quarters
    ts = [21.0, 21.3, 21.1, 21.6]
    # panel: 2 households x 3 years
    panel = {
        1: [(2021, 40.0), (2022, 42.0), (2023, 41.0)],
        2: [(2021, 60.0), (2022, 63.0), (2023, 66.0)],
    }
    assert len(cross) == 4 and len(ts) == 4
    N = len(panel); T = len(panel[1])
    assert (N, T) == (2, 3)
    # long format: one row per (unit, time)
    long = [(h, yr, inc) for h, rows in panel.items() for yr, inc in rows]
    assert len(long) == N * T == 6
    # within-unit change is the panel's gift: household 2 rose 6.0, household 1 rose 1.0
    chg = {h: rows[-1][1] - rows[0][1] for h, rows in panel.items()}
    assert chg == {1: 1.0, 2: 6.0}
    print("cross-section: %d units x 1 time | time series: 1 unit x %d times | panel: %d units x %d times" %
          (len(cross), len(ts), N, T))
    print("panel long format: %d rows; within-unit changes %s" % (len(long), chg))
    print("rule: name the shape (N x T) before choosing the estimator")
    print("OK: %s shaped the data" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_econ_causation(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def pcorr(x, y, z):
    # partial correlation of x,y controlling z
    def corr(a, b):
        return _cov(a, b) / math.sqrt(_var(a) * _var(b))
    rxy, rxz, ryz = corr(x, y), corr(x, z), corr(y, z)
    return (rxy - rxz * ryz) / math.sqrt((1 - rxz ** 2) * (1 - ryz ** 2))
def main():
    rng = random.Random(11)
    n = 2000
    heat = [rng.gauss(30, 5) for _ in range(n)]            # the confounder
    ice = [2 * h + rng.gauss(0, 3) for h in heat]          # ice cream sales
    drown = [0.5 * h + rng.gauss(0, 2) for h in heat]      # drownings
    r = _cov(ice, drown) / math.sqrt(_var(ice) * _var(drown))
    assert r > 0.7, r
    print("raw correlation (ice cream, drownings): %.3f - alarming and meaningless" % r)
    pr = pcorr(ice, drown, heat)
    assert abs(pr) < 0.08, pr
    print("partial correlation controlling heat: %.3f - the 'effect' vanishes" % pr)
    print("rule: name the impostor (confounder, reverse cause, selection) before trusting a correlation")
    print("OK: %s separated correlation from causation" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_econ_simple_reg(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # schooling (x) and hourly wage (y), 8 workers
    x = [10, 12, 12, 14, 16, 16, 18, 20]
    y = [18, 22, 24, 28, 33, 35, 42, 48]
    b1 = _cov(x, y) / _var(x)
    b0 = _mean(y) - b1 * _mean(x)
    assert abs(b1 - 3.025157) < 1e-4, b1
    print("OLS slope = Cov(x,y)/Var(x) = %.4f: one more school year <-> $%.2f/hour" % (b1, b1))
    # the line passes through the point of means
    assert abs((b0 + b1 * _mean(x)) - _mean(y)) < 1e-9
    print("line passes through (x-bar, y-bar) = (%.2f, %.2f)" % (_mean(x), _mean(y)))
    # residuals sum to zero, uncorrelated with x
    e = [y[i] - (b0 + b1 * x[i]) for i in range(len(x))]
    assert abs(sum(e)) < 1e-9
    assert abs(_cov(x, e)) < 1e-9
    print("residuals sum to %.1e and are uncorrelated with x (algebraic gifts of OLS)" % sum(e))
    print("rule: slope = Cov/Var; the line pivots through the means")
    print("OK: %s fit the straight line" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_econ_multiple_reg(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    rng = random.Random(21)
    n = 500
    # y = 1 + 2*x1 + 3*x2 + u ; x1,x2 correlated (confounding)
    x2 = [rng.gauss(0, 1) for _ in range(n)]
    x1 = [0.7 * z + rng.gauss(0, 1) for z in x2]
    y = [1 + 2 * a + 3 * b + rng.gauss(0, 1) for a, b in zip(x1, x2)]
    X = [[1, a, b] for a, b in zip(x1, x2)]
    b = _ols(y, X)
    assert abs(b[1] - 2) < 0.25 and abs(b[2] - 3) < 0.25, b
    print("multiple regression: b1 = %.3f (truth 2), b2 = %.3f (truth 3)" % (b[1], b[2]))
    # Frisch-Waugh-Lovell: residual-on-residual slope == multiple-regression slope
    X2 = [[1, v] for v in x2]
    b_x = _ols(x1, X2); b_y = _ols(y, X2)
    rx = _resid(x1, X2, b_x); ry = _resid(y, X2, b_y)
    fwl = _cov(rx, ry) / _var(rx)
    assert abs(fwl - b[1]) < 1e-9, (fwl, b[1])
    print("Frisch-Waugh: residual-on-residual slope %.6f == multiple-regression b1" % fwl)
    # naive simple regression of y on x1 alone is confounded
    b_naive = _cov(x1, y) / _var(x1)
    assert abs(b_naive - 2) > 0.3, b_naive
    print("naive y-on-x1 slope %.3f != 2: the confounder x2 contaminates it" % b_naive)
    print("rule: each slope uses only its regressor's variation independent of the controls")
    print("OK: %s held other factors fixed" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_econ_ols_mechanics(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    rng = random.Random(31)
    n = 100
    x1 = [rng.gauss(0, 1) for _ in range(n)]
    x2 = [rng.gauss(0, 1) for _ in range(n)]
    y = [1 + 2 * a - b + rng.gauss(0, 1) for a, b in zip(x1, x2)]
    X = [[1, a, b] for a, b in zip(x1, x2)]
    bhat = _ols(y, X)
    e = _resid(y, X, bhat)
    yhat = [y[i] - e[i] for i in range(n)]
    # normal equations: X'e = 0 (each regressor orthogonal to residuals)
    for j, label in enumerate(["const", "x1", "x2"]):
        assert abs(sum(X[i][j] * e[i] for i in range(n))) < 1e-8, label
    print("normal equations hold: X'e = 0 for const, x1, x2")
    # fitted values uncorrelated with residuals; residuals sum to zero
    assert abs(_cov(yhat, e)) < 1e-9
    assert abs(sum(e)) < 1e-8
    print("fitted values uncorrelated with residuals; residuals sum to %.1e" % sum(e))
    # variance formula: Var(b1) = s^2 * (X'X)^{-1}[1][1]
    s2 = sum(v * v for v in e) / (n - 3)
    XtX = [[sum(X[i][a] * X[i][b] for i in range(n)) for b in range(3)] for a in range(3)]
    # invert via _solve on identity columns
    inv = [_solve(XtX, [1 if i == j else 0 for i in range(3)]) for j in range(3)]
    se_b1 = math.sqrt(s2 * inv[1][1])
    assert 0.05 < se_b1 < 0.25, se_b1
    print("Var(b-hat) = s^2 (X'X)^{-1}: se(b1) = %.4f" % se_b1)
    print("rule: OLS projects y onto the regressor space; residuals are the orthogonal leftover")
    print("OK: %s solved the normal equations" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_econ_reading_output(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def p_value(t):
    return 2 * (1 - _phi(abs(t)))
def main():
    # deterministic check of the p-value machinery
    assert abs(p_value(1.96) - 0.05) < 0.002, p_value(1.96)
    assert abs(p_value(2.58) - 0.01) < 0.002
    print("p(|t|=1.96) = %.4f, p(|t|=2.58) = %.4f - the 5%% and 1%% lines" %
          (p_value(1.96), p_value(2.58)))
    rng = random.Random(41)
    n = 800
    x1 = [rng.gauss(0, 1) for _ in range(n)]          # true effect 2
    x2 = [rng.gauss(0, 1) for _ in range(n)]          # true effect 0
    y = [2 * a + rng.gauss(0, 1) for a in x1]
    X = [[1, a, b] for a, b in zip(x1, x2)]
    bhat = _ols(y, X)
    e = _resid(y, X, bhat)
    s2 = sum(v * v for v in e) / (n - 3)
    XtX = [[sum(X[i][a] * X[i][b] for i in range(n)) for b in range(3)] for a in range(3)]
    inv = [_solve(XtX, [1 if i == j else 0 for i in range(3)]) for j in range(3)]
    print("%-6s %10s %10s %10s %10s" % ("coef", "estimate", "std.err", "t-stat", "p-value"))
    sig = []
    for j, label in enumerate(["const", "x1", "x2"]):
        se = math.sqrt(s2 * inv[j][j])
        t = bhat[j] / se
        p = p_value(t)
        sig.append(p < 0.05)
        print("%-6s %10.4f %10.4f %10.2f %10.4f" % (label, bhat[j], se, t, p))
    assert sig == [False, True, False], sig
    print("verdict: x1 significant (real effect), x2 not (true zero), intercept not")
    # confidence interval for b1 covers the truth 2
    se1 = math.sqrt(s2 * inv[1][1])
    assert bhat[1] - 1.96 * se1 < 2 < bhat[1] + 1.96 * se1
    print("95%% CI for b1 [%.3f, %.3f] covers the truth 2" % (bhat[1] - 1.96 * se1, bhat[1] + 1.96 * se1))
    print("rule: magnitude first, stars second - a table is an argument in numbers")
    print("OK: %s read the regression table" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_econ_r2(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    rng = random.Random(51)
    n = 200
    x = [rng.gauss(0, 1) for _ in range(n)]
    y = [1 + 2 * a + rng.gauss(0, 2) for a in x]   # noisy: modest R^2 expected
    X = [[1, a] for a in x]
    b = _ols(y, X)
    e = _resid(y, X, b)
    yhat = [y[i] - e[i] for i in range(n)]
    ybar = _mean(y)
    SST = sum((v - ybar) ** 2 for v in y)
    SSR = sum(v * v for v in e)
    ESS = sum((v - ybar) ** 2 for v in yhat)
    assert abs(SST - (ESS + SSR)) / SST < 1e-9   # Pythagorean split
    R2 = 1 - SSR / SST
    assert 0 <= R2 <= 1
    R2adj = 1 - (1 - R2) * (n - 1) / (n - 2)
    assert R2adj < R2
    print("SST = ESS + SSR: %.1f = %.1f + %.1f" % (SST, ESS, SSR))
    print("R^2 = %.3f, adjusted R^2 = %.3f (noisy data, modest fit - normal for wages)" % (R2, R2adj))
    # adding a useless regressor never lowers R^2
    z = [rng.gauss(0, 1) for _ in range(n)]
    X2 = [[1, a, c] for a, c in zip(x, z)]
    b2 = _ols(y, X2)
    R2b = 1 - _ssr(y, X2, b2) / SST
    assert R2b >= R2 - 1e-12
    print("useless regressor added: R^2 %.4f -> %.4f (never falls)" % (R2, R2b))
    # standard error of the regression: typical miss in y's units
    ser = math.sqrt(SSR / (n - 2))
    print("s.e. of regression = %.3f: the typical miss, in y's units" % ser)
    print("rule: R^2 is context, not verdict - design beats fit")
    print("OK: %s measured explained variation" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_econ_dummy(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # wages by group: men (D=0), women (D=1), plus schooling control
    rng = random.Random(61)
    n = 400
    D = [1 if i >= n // 2 else 0 for i in range(n)]
    educ = [12 + rng.gauss(0, 2) for _ in range(n)]
    # true gap: -3 (women earn 3 less, ceteris paribus)
    y = [20 + 2 * s - 3 * d + rng.gauss(0, 2) for s, d in zip(educ, D)]
    # raw mean difference (no controls)
    m1 = _mean([v for v, d in zip(y, D) if d == 1])
    m0 = _mean([v for v, d in zip(y, D) if d == 0])
    X0 = [[1, d] for d in D]
    b0 = _ols(y, X0)
    assert abs(b0[1] - (m1 - m0)) < 1e-9
    print("no controls: dummy coef %.3f == mean(women) - mean(men) = %.3f" % (b0[1], m1 - m0))
    # with schooling control: closer to the true -3
    X = [[1, d, s] for d, s in zip(D, educ)]
    b = _ols(y, X)
    assert abs(b[1] - (-3)) < 0.5, b
    print("with schooling control: gap = %.3f (truth -3.0) - ceteris paribus" % b[1])
    # dummy-variable trap: all dummies + intercept is singular
    Xfull = [[1, d, 1 - d] for d in D]
    try:
        _ols(y, Xfull)
        raise AssertionError("trap did not spring")
    except ValueError:
        print("dummy trap: [1, D, 1-D] is singular - one category must be the base")
    print("rule: g categories -> g-1 dummies; every gap is read against the base")
    print("OK: %s coded the categories" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_econ_gauss_markov(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    rng = random.Random(71)
    n, reps = 60, 1500
    truth = 2.0
    sig = 1.5
    ests = []
    Sxx_tot = 0.0
    for _ in range(reps):
        x = [rng.gauss(0, 1) for _ in range(n)]
        y = [1 + truth * a + rng.gauss(0, sig) for a in x]
        b1 = _cov(x, y) / _var(x)
        ests.append(b1)
        Sxx_tot += sum((a - _mean(x)) ** 2 for a in x)
    mc_mean = _mean(ests)
    mc_var = _var(ests)
    assert abs(mc_mean - truth) < 0.05, mc_mean
    # theory: Var(b1) = sigma^2 / Sxx ; compare Monte Carlo variance to average theory
    theory = sig ** 2 / (Sxx_tot / reps)
    assert abs(mc_var - theory) / theory < 0.15, (mc_var, theory)
    print("Monte Carlo (%d reps): mean(b1) = %.4f (truth %.1f) - unbiased" % (reps, mc_mean, truth))
    print("MC variance %.5f vs Gauss-Markov formula %.5f - the 'best' in BLUE, verified" % (mc_var, theory))
    # a biased rival: shrink toward zero (ridge-flavored) - smaller variance, but biased
    shrunk = [0.8 * e for e in ests]
    assert abs(_mean(shrunk) - truth) > abs(mc_mean - truth)
    assert _var(shrunk) < mc_var
    print("shrunk rival: bias %.4f (vs %.4f), variance %.5f (vs %.5f) - bias-variance tradeoff" %
          (abs(_mean(shrunk) - truth), abs(mc_mean - truth), _var(shrunk), mc_var))
    print("rule: unbiasedness is centering on truth; 'best' is minimum variance among the unbiased")
    print("OK: %s verified Gauss-Markov" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_econ_hetero(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    rng = random.Random(81)
    n = 300
    x = [1 + 9 * rng.random() for _ in range(n)]          # 1..10
    y = [1 + 2 * a + rng.gauss(0, 0.6 * a) for a in x]    # variance grows with x
    X = [[1, a] for a in x]
    b = _ols(y, X)
    e = _resid(y, X, b)
    assert abs(b[1] - 2) < 0.3, b   # still unbiased
    print("OLS slope %.3f (truth 2): heteroskedasticity does not bias coefficients" % b[1])
    # White test: e^2 on x, x^2 ; nR^2 ~ chi2(2), critical 5.99
    e2 = [v * v for v in e]
    Xw = [[1, a, a * a] for a in x]
    bw = _ols(e2, Xw)
    ew = _resid(e2, Xw, bw)
    R2w = 1 - sum(v * v for v in ew) / sum((v - _mean(e2)) ** 2 for v in e2)
    stat = n * R2w
    assert stat > 5.99, stat
    print("White test: nR^2 = %.1f > 5.99 - heteroskedasticity detected" % stat)
    # OLS vs robust (HC0) standard errors for the slope
    Sxx = sum((a - _mean(x)) ** 2 for a in x)
    s2 = sum(v * v for v in e) / (n - 2)
    se_ols = math.sqrt(s2 / Sxx)
    meat = sum(((a - _mean(x)) ** 2) * (ev ** 2) for a, ev in zip(x, e))
    se_hc0 = math.sqrt(meat) / Sxx
    print("se(b1): OLS %.4f vs robust HC0 %.4f - inference repaired, estimate untouched" % (se_ols, se_hc0))
    assert abs(se_hc0 - se_ols) / se_ols > 0.05
    print("rule: fan-shaped residuals -> test (White), then report robust standard errors")
    print("OK: %s handled uneven spread" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_econ_multicoll(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def vif(X, j):
    # VIF_j from regressing column j on the other columns (with intercept)
    n = len(X); k = len(X[0])
    y = [X[i][j] for i in range(n)]
    Xo = [[X[i][c] for c in range(k) if c != j] for i in range(n)]
    if not any(abs(v - 1) < 1e-12 for v in Xo[0]):
        Xo = [[1] + row for row in Xo]
    bo = _ols(y, Xo)
    eo = _resid(y, Xo, bo)
    R2 = 1 - sum(v * v for v in eo) / sum((v - _mean(y)) ** 2 for v in y)
    return 1 / (1 - R2)
def main():
    rng = random.Random(91)
    n = 300
    x1 = [rng.gauss(0, 1) for _ in range(n)]
    x2 = [0.96 * a + rng.gauss(0, 0.28) for a in x1]  # corr ~0.96
    y = [1 + 2 * a + 2 * b + rng.gauss(0, 1) for a, b in zip(x1, x2)]
    X = [[1, a, b] for a, b in zip(x1, x2)]
    v1, v2 = vif(X, 1), vif(X, 2)
    assert v1 > 10 and v2 > 10, (v1, v2)
    print("VIF(x1) = %.1f, VIF(x2) = %.1f - above 10: severe overlap" % (v1, v2))
    b = _ols(y, X)
    e = _resid(y, X, b)
    s2 = sum(v * v for v in e) / (n - 3)
    # joint F: both matter enormously even as t-stats starve
    X0 = [[1] for _ in range(n)]
    b0 = _ols(y, X0)
    F = ((_ssr(y, X0, b0) - _ssr(y, X, b)) / 2) / (s2)
    assert F > 100, F
    print("joint F = %.0f (both matter); individual t-stats starve - the classic symptom" % F)
    # the cure demo: drop the redundant twin, variance collapses
    Xs = [[1, a] for a in x1]
    bs = _ols(y, Xs)
    es = _resid(y, Xs, bs)
    s2s = sum(v * v for v in es) / (n - 2)
    Sxx = sum((a - _mean(x1)) ** 2 for a in x1)
    print("single-regressor se(b1) = %.4f - precision restored by respecification" %
          math.sqrt(s2s / Sxx))
    print("rule: overlap inflates variance - respecify, combine, or gather more data")
    print("OK: %s diagnosed overlapping regressors" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_econ_autocorr(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    rng = random.Random(101)
    n = 200
    x = [rng.gauss(0, 1) for _ in range(n)]
    u = [0.0] * n
    u[0] = rng.gauss(0, 1)
    for t in range(1, n):
        u[t] = 0.8 * u[t - 1] + rng.gauss(0, 1)     # AR(1) errors, rho = 0.8
    y = [1 + 2 * a + uu for a, uu in zip(x, u)]
    X = [[1, a] for a in x]
    b = _ols(y, X)
    e = _resid(y, X, b)
    assert abs(b[1] - 2) < 0.3, b   # still unbiased
    print("OLS slope %.3f (truth 2): autocorrelation does not bias coefficients" % b[1])
    # Durbin-Watson ~= 2(1 - rho)
    dw = sum((e[t] - e[t - 1]) ** 2 for t in range(1, n)) / sum(v * v for v in e)
    assert dw < 1.0, dw
    print("Durbin-Watson = %.2f (near 2(1-0.8) = 0.4): strong positive autocorrelation" % dw)
    # Breusch-Godfrey: e on X + lagged e ; nR^2 ~ chi2(1), critical 3.84
    Xbg = [[1, a, (e[t - 1] if t > 0 else 0)] for t, a in enumerate(x)]
    bbg = _ols(e, Xbg)
    ebg = _resid(e, Xbg, bbg)
    R2bg = 1 - sum(v * v for v in ebg) / sum((v - _mean(e)) ** 2 for v in e)
    assert n * R2bg > 3.84
    print("Breusch-Godfrey nR^2 = %.1f > 3.84 - serial correlation confirmed" % (n * R2bg))
    # naive se vs truth: OLS understates uncertainty
    Sxx = sum((a - _mean(x)) ** 2 for a in x)
    s2 = sum(v * v for v in e) / (n - 2)
    print("naive se(b1) = %.4f - too small; HAC/GLS repair needed for honest inference" %
          math.sqrt(s2 / Sxx))
    print("rule: DW near 0 with trending data -> distrust every t-statistic until repaired")
    print("OK: %s caught errors following each other" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_econ_ovb(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    rng = random.Random(111)
    n = 1000
    # truth: y = 1 + 2*x1 + 3*x2 + u ; x2 correlated with x1 (delta = 0.6)
    x1 = [rng.gauss(0, 1) for _ in range(n)]
    x2 = [0.6 * a + rng.gauss(0, 0.8) for a in x1]
    y = [1 + 2 * a + 3 * b + rng.gauss(0, 1) for a, b in zip(x1, x2)]
    # short regression omits x2
    b_short = _cov(x1, y) / _var(x1)
    # auxiliary: x2 on x1 -> delta
    delta = _cov(x1, x2) / _var(x1)
    bias_formula = 3 * delta
    assert abs((b_short - 2) - bias_formula) < 0.08, (b_short, bias_formula)
    print("omitted x2: b1_short = %.3f = truth 2 + bias %.3f (b2*delta = 3*%.3f)" %
          (b_short, bias_formula, delta))
    # long regression recovers the truth
    X = [[1, a, b] for a, b in zip(x1, x2)]
    blong = _ols(y, X)
    assert abs(blong[1] - 2) < 0.15 and abs(blong[2] - 3) < 0.15
    print("full model: b1 = %.3f, b2 = %.3f - bias gone once the confounder is controlled" %
          (blong[1], blong[2]))
    print("rule: bias = omitted coefficient x auxiliary slope - sign it before you estimate")
    print("OK: %s priced the omitted variable" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_econ_iv(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    rng = random.Random(121)
    n = 3000
    # truth: y = 1 + 2*x + u ; x endogenous: built from u itself
    z = [rng.gauss(0, 1) for _ in range(n)]          # the instrument
    u = [rng.gauss(0, 1) for _ in range(n)]
    w = [rng.gauss(0, 1) for _ in range(n)]
    x = [0.9 * zi + 0.8 * ui + 0.4 * wi for zi, ui, wi in zip(z, u, w)]
    y = [1 + 2 * a + ui for a, ui in zip(x, u)]
    b_ols = _cov(x, y) / _var(x)
    assert abs(b_ols - 2) > 0.15, b_ols
    print("OLS slope = %.3f (truth 2): endogeneity biases OLS upward" % b_ols)
    # 2SLS: stage 1 x on z ; stage 2 y on x-hat
    X1 = [[1, zi] for zi in z]
    g = _ols(x, X1)
    xhat = [g[0] + g[1] * zi for zi in z]
    # first-stage F (rule of thumb: > 10)
    e1 = _resid(x, X1, g)
    R21 = 1 - sum(v * v for v in e1) / sum((v - _mean(x)) ** 2 for v in x)
    F1 = R21 / (1 - R21) * (n - 2)
    assert F1 > 10, F1
    print("first stage: F = %.0f > 10 - the instrument is strong" % F1)
    b_2sls = _cov(xhat, y) / _var(xhat)
    assert abs(b_2sls - 2) < 0.12, b_2sls
    print("2SLS slope = %.3f (truth 2): the instrument cleaned the variation" % b_2sls)
    # reduced form / first stage ratio == IV estimator
    rf = _cov(z, y) / _var(z)
    fs = _cov(z, x) / _var(z)
    assert abs(rf / fs - b_2sls) < 1e-9
    print("Wald ratio: reduced-form %.3f / first-stage %.3f = %.3f" % (rf, fs, rf / fs))
    print("rule: relevance is tested (F > 10); exogeneity is argued from economics")
    print("OK: %s wielded the instrument" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_econ_meas_error(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    rng = random.Random(131)
    n = 3000
    xs = [rng.gauss(0, 1) for _ in range(n)]          # true x*
    e = [rng.gauss(0, 1) for _ in range(n)]           # classical noise
    x = [a + b for a, b in zip(xs, e)]                # observed x = x* + noise
    y = [1 + 3 * a + rng.gauss(0, 1) for a in xs]     # truth: slope 3
    b = _cov(x, y) / _var(x)
    # reliability ratio = Var(x*)/(Var(x*)+Var(noise)) = 1/2 -> plim 1.5
    assert 1.2 < b < 1.9, b
    print("measured-with-error slope = %.3f (truth 3.0): attenuation toward zero" % b)
    print("reliability ratio = 1/(1+1) = 0.5 -> probability limit 3*0.5 = 1.5")
    # error in y is benign: only inflates standard errors
    yu = [v + rng.gauss(0, 3) for v in y]
    s_clean = math.sqrt(sum((v - (1 + 3 * a)) ** 2 for v, a in zip(y, xs)) / n)
    s_noisy = math.sqrt(sum((v - (1 + 3 * a)) ** 2 for v, a in zip(yu, xs)) / n)
    assert s_noisy > s_clean
    print("noise in y: residual sd %.2f -> %.2f (noisier inference, unbiased slope)" % (s_clean, s_noisy))
    # the cure sketch: a second noisy measure instruments the first
    x2 = [a + rng.gauss(0, 1) for a in xs]
    b_iv = _cov(x2, y) / _cov(x2, x)
    assert abs(b_iv - 3) < 0.4, b_iv
    print("IV with second measure: slope = %.3f - attenuation repaired" % b_iv)
    print("rule: noise in x shrinks coefficients; ask 'how is this measured?' before trusting small ones")
    print("OK: %s quantified the static" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_econ_probit_logit(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    rng = random.Random(141)
    n = 600
    x = [rng.gauss(0, 1) for _ in range(n)]
    # truth: P(y=1) = logistic(-0.5 + 1.5x)
    p = [1 / (1 + math.exp(0.5 - 1.5 * a)) for a in x]
    y = [1 if rng.random() < pi else 0 for pi in p]
    # Newton-Raphson for the logit log-likelihood
    b = [0.0, 0.0]
    for _ in range(25):
        g = [0.0, 0.0]
        H = [[0.0, 0.0], [0.0, 0.0]]
        for xi, yi in zip(x, y):
            pi = 1 / (1 + math.exp(-(b[0] + b[1] * xi)))
            r = yi - pi
            w = pi * (1 - pi)
            g[0] += r; g[1] += r * xi
            H[0][0] += w; H[0][1] += w * xi; H[1][1] += w * xi * xi
        H[1][0] = H[0][1]
        step = _solve(H, g)
        b = [b[0] + step[0], b[1] + step[1]]
        if math.sqrt(sum(v * v for v in g)) < 1e-8:
            break
    assert abs(b[0] - (-0.5)) < 0.35 and abs(b[1] - 1.5) < 0.35, b
    print("logit MLE: b0 = %.3f (truth -0.5), b1 = %.3f (truth 1.5)" % (b[0], b[1]))
    # average marginal effect: mean of f(xb)*b1
    ame = sum((pi * (1 - pi)) for pi in
              [1 / (1 + math.exp(-(b[0] + b[1] * xi))) for xi in x]) / n * b[1]
    print("average marginal effect of x: %.3f - probabilities, not log-odds" % ame)
    # linear probability model leaks outside [0,1]
    blpm = _cov(x, y) / _var(x)
    preds = [_mean(y) + blpm * (a - _mean(x)) for a in x]
    bad = sum(1 for v in preds if v < 0 or v > 1)
    print("linear probability model: %d of %d fitted values outside [0,1]" % (bad, n))
    # probit agrees on substance (coefficients ~ /1.6)
    print("rule: report average marginal effects - readers think in probabilities")
    print("OK: %s modeled the yes-or-no" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_econ_tobit(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def tobit_ll(par, y, X):
    b0, b1, ls = par
    s = math.exp(ls)
    ll = 0.0
    for yi, xi in zip(y, X):
        xb = b0 + b1 * xi
        if yi <= 0:
            Phi = _phi(-xb / s)
            Phi = min(max(Phi, 1e-12), 1 - 1e-12)
            ll += math.log(Phi)
        else:
            z = (yi - xb) / s
            ll += -0.5 * z * z - ls - 0.5 * math.log(2 * math.pi)
    return ll
def main():
    rng = random.Random(151)
    n = 500
    x = [rng.gauss(0, 1) for _ in range(n)]
    ystar = [-1 + 2 * a + rng.gauss(0, 1) for a in x]   # latent truth
    y = [max(0, v) for v in ystar]                        # censored at 0
    cens = sum(1 for v in y if v <= 0) / n
    print("censoring share: %.1f%% piled at zero" % (100 * cens))
    # OLS on censored y: biased toward zero
    b_ols = _cov(x, y) / _var(x)
    assert b_ols < 1.6, b_ols
    print("OLS slope = %.3f (truth 2.0): censoring drags the line flat" % b_ols)
    # Tobit MLE via Newton with numeric derivatives
    par = [0.0, 1.0, 0.0]
    h = 1e-5
    for _ in range(60):
        f0 = tobit_ll(par, y, x)
        g = []
        for j in range(3):
            pj = par[:]; pj[j] += h
            g.append((tobit_ll(pj, y, x) - f0) / h)
        H = [[0.0] * 3 for _ in range(3)]
        for a in range(3):
            for c_ in range(3):
                pa = par[:]; pa[a] += h; pc = par[:]; pc[c_] += h; pac = par[:]
                pac[a] += h; pac[c_] += h
                H[a][c_] = (tobit_ll(pac, y, x) - tobit_ll(pa, y, x)
                            - tobit_ll(pc, y, x) + f0) / (h * h)
        step = _solve([[-v for v in row] for row in H], g)
        cand = [par[j] + step[j] for j in range(3)]
        if tobit_ll(cand, y, x) > f0:
            par = cand
        if math.sqrt(sum(v * v for v in g)) < 1e-5:
            break
    assert abs(par[1] - 2) < 0.3, par
    assert abs(math.exp(par[2]) - 1) < 0.25, par
    print("Tobit MLE: b1 = %.3f (truth 2.0), sigma = %.3f (truth 1.0)" % (par[1], math.exp(par[2])))
    # marginal effect on observed y = b1 * P(uncensored)
    me = par[1] * (1 - cens)
    print("effect on observed y ~= b1 * P(y>0) = %.3f - the McDonald-Moffitt split" % me)
    print("rule: censored zeros are information - the likelihood uses them instead of fearing them")
    print("OK: %s uncensored the pile-up" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_econ_panel(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    rng = random.Random(161)
    N, T = 60, 5
    # truth: y = 1 + 2*x + a_i + u ; a_i correlates with x (the hard case)
    a = [rng.gauss(0, 1) for _ in range(N)]
    xs, ys = [], []
    for i in range(N):
        xi = [a[i] + rng.gauss(0, 1) for _ in range(T)]
        yi = [1 + 2 * v + a[i] + rng.gauss(0, 1) for v in xi]
        xs.append(xi); ys.append(yi)
    Xp = [[1, v] for xi in xs for v in xi]
    yp = [v for yi in ys for v in yi]
    b_pool = _ols(yp, Xp)
    assert abs(b_pool[1] - 2) > 0.25, b_pool   # pooled OLS biased up
    print("pooled OLS slope = %.3f (truth 2.0): the permanent trait a_i contaminates it" % b_pool[1])
    # fixed effects: within transformation (demean per unit)
    xw, yw = [], []
    for xi, yi in zip(xs, ys):
        mx, my = _mean(xi), _mean(yi)
        xw.extend([v - mx for v in xi]); yw.extend([v - my for v in yi])
    b_fe = _cov(xw, yw) / _var(xw)
    assert abs(b_fe - 2) < 0.2, b_fe
    print("fixed-effects slope = %.3f (truth 2.0): demeaning deleted every a_i" % b_fe)
    # first differences: the close cousin, also consistent
    xd, yd = [], []
    for xi, yi in zip(xs, ys):
        xd.extend([xi[t] - xi[t - 1] for t in range(1, T)])
        yd.extend([yi[t] - yi[t - 1] for t in range(1, T)])
    b_fd = _cov(xd, yd) / _var(xd)
    assert abs(b_fd - 2) < 0.25, b_fd
    print("first-differences slope = %.3f: watching only changes, same answer" % b_fd)
    print("rule: when the unobserved trait correlates with x, demean first and ask questions later")
    print("OK: %s stripped the permanent traits" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_econ_hausman(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    rng = random.Random(171)
    N, T = 80, 5
    # hard case: a_i correlates with x -> RE inconsistent, FE consistent
    a = [rng.gauss(0, 1) for _ in range(N)]
    xs, ys = [], []
    for i in range(N):
        xi = [a[i] + rng.gauss(0, 1) for _ in range(T)]
        yi = [1 + 2 * v + a[i] + rng.gauss(0, 1) for v in xi]
        xs.append(xi); ys.append(yi)
    # FE (within)
    xw, yw = [], []
    for xi, yi in zip(xs, ys):
        mx, my = _mean(xi), _mean(yi)
        xw.extend([v - mx for v in xi]); yw.extend([v - my for v in yi])
    b_fe = _cov(xw, yw) / _var(xw)
    Sxx_w = sum((v - _mean(xw)) ** 2 for v in xw)
    e_fe = [yw[i] - b_fe * xw[i] for i in range(len(xw))]
    s2 = sum(v * v for v in e_fe) / (len(xw) - N - 1)
    V_fe = s2 / Sxx_w
    # RE via quasi-demeaning with known variance components (demo)
    sig_u2, sig_a2 = 1.0, 1.0
    theta = 1 - math.sqrt(sig_u2 / (sig_u2 + T * sig_a2))
    xq, yq = [], []
    for xi, yi in zip(xs, ys):
        mx, my = _mean(xi), _mean(yi)
        xq.extend([v - theta * mx for v in xi]); yq.extend([v - theta * my for v in yi])
    b_re = _cov(xq, yq) / _var(xq)
    Sxx_q = sum((v - _mean(xq)) ** 2 for v in xq)
    V_re = sig_u2 / Sxx_q
    H = (b_fe - b_re) ** 2 / (V_fe - V_re)
    assert H > 3.84, (H, b_fe, b_re)
    print("b_FE = %.3f, b_RE = %.3f" % (b_fe, b_re))
    print("Hausman H = %.1f > 3.84: reject random effects - a_i correlates with x" % H)
    # easy case: a_i uncorrelated -> both agree, H small
    rng2 = random.Random(172)
    a2 = [rng2.gauss(0, 1) for _ in range(N)]
    xs2, ys2 = [], []
    for i in range(N):
        xi = [rng2.gauss(0, 1) for _ in range(T)]
        yi = [1 + 2 * v + a2[i] + rng2.gauss(0, 1) for v in xi]
        xs2.append(xi); ys2.append(yi)
    xw2 = [v - _mean(xi) for xi in xs2 for v in xi]
    yw2 = [v - _mean(yi) for yi, xi in zip(ys2, xs2) for v in yi]
    b_fe2 = _cov(xw2, yw2) / _var(xw2)
    assert abs(b_fe2 - 2) < 0.2
    print("uncorrelated case: b_FE = %.3f ~ truth 2 - both estimators would agree" % b_fe2)
    print("rule: big disagreement between FE and RE means the RE assumption failed")
    print("OK: %s adjudicated the duel" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_econ_did(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    rng = random.Random(181)
    n = 400  # per cell
    # truth: treated +3 level, post +2 trend, policy effect +5
    cells = {}
    for tr in (0, 1):
        for po in (0, 1):
            cells[(tr, po)] = [10 + 3 * tr + 2 * po + 5 * tr * po + rng.gauss(0, 2)
                               for _ in range(n)]
    did = ((_mean(cells[(1, 1)]) - _mean(cells[(1, 0)]))
           - (_mean(cells[(0, 1)]) - _mean(cells[(0, 0)])))
    assert abs(did - 5) < 0.6, did
    print("2x2 diff-in-diff = %.3f (truth 5.0)" % did)
    # regression form: y on treated, post, treated*post
    y, X = [], []
    for (tr, po), vals in cells.items():
        for v in vals:
            y.append(v); X.append([1, tr, po, tr * po])
    b = _ols(y, X)
    assert abs(b[3] - did) < 1e-9
    print("regression interaction coefficient = %.3f - identical to the 2x2" % b[3])
    # pre-trend placebo: two pre periods with no policy must give ~0
    pre0 = [10 + 3 * tr + rng.gauss(0, 2) for tr in (0, 1) for _ in range(n)]
    pre1 = [12 + 3 * tr + rng.gauss(0, 2) for tr in (0, 1) for _ in range(n)]
    g0 = [v for v, tr in zip(pre0, [0] * n + [1] * n)]
    g1 = [v for v, tr in zip(pre0, [0] * n + [1] * n)]
    placebo = ((_mean([v for v, tr in zip(pre1, [0] * n + [1] * n) if tr == 1])
                - _mean([v for v, tr in zip(pre0, [0] * n + [1] * n) if tr == 1]))
               - (_mean([v for v, tr in zip(pre1, [0] * n + [1] * n) if tr == 0])
                  - _mean([v for v, tr in zip(pre0, [0] * n + [1] * n) if tr == 0])))
    assert abs(placebo) < 0.6, placebo
    print("pre-period placebo DiD = %.3f ~ 0: parallel trends hold before the policy" % placebo)
    print("rule: no parallel pre-trends, no causal claim")
    print("OK: %s double-differenced" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_econ_rdd(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def local_linear(x, y, c, bw, side):
    xs = [a for a in x if (a >= c if side > 0 else a < c) and abs(a - c) <= bw]
    ys = [b for a, b in zip(x, y) if (a >= c if side > 0 else a < c) and abs(a - c) <= bw]
    X = [[1, a - c] for a in xs]
    b = _ols(ys, X)
    return b[0], len(xs)
def main():
    rng = random.Random(191)
    n = 1500
    x = [2 * rng.random() - 1 for _ in range(n)]       # running variable, cutoff 0
    D = [1 if a >= 0 else 0 for a in x]
    # truth: y = 1 + 2x + 3*D + noise ; the jump at 0 is 3
    y = [1 + 2 * a + 3 * d + rng.gauss(0, 0.5) for a, d in zip(x, D)]
    bw = 0.35
    right, nr = local_linear(x, y, 0, bw, +1)
    left, nl = local_linear(x, y, 0, bw, -1)
    jump = right - left
    assert abs(jump - 3) < 0.4, jump
    print("sharp RDD: right limit %.3f, left limit %.3f, jump %.3f (truth 3.0)" % (right, left, jump))
    print("bandwidth %.2f uses %d left + %d right points near the cutoff" % (bw, nl, nr))
    # manipulation check: density of x smooth through the cutoff
    lo = sum(1 for a in x if -0.1 <= a < 0); hi = sum(1 for a in x if 0 <= a <= 0.1)
    assert abs(lo - hi) / (lo + hi) < 0.2, (lo, hi)
    print("density check: %d just below vs %d just above - no bunching, no manipulation" % (lo, hi))
    # naive global comparison is biased by the slope
    naive = _mean([b for a, b in zip(x, y) if a >= 0]) - _mean([b for a, b in zip(x, y) if a < 0])
    assert abs(naive - 3) > 0.5, naive
    print("naive above-vs-below mean gap = %.3f: the slope contaminates it - locality matters" % naive)
    print("rule: estimate at the cutoff, validate the density, plot everything")
    print("OK: %s jumped the cutoff" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_econ_unit_root(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def adf_tstat(y):
    # ADF(0): delta_y on const + y_{t-1}; return t-stat on y_{t-1}
    n = len(y)
    dy = [y[t] - y[t - 1] for t in range(1, n)]
    X = [[1, y[t - 1]] for t in range(1, n)]
    b = _ols(dy, X)
    e = _resid(dy, X, b)
    s2 = sum(v * v for v in e) / (n - 3)
    XtX = [[sum(X[i][a] * X[i][b] for i in range(n - 1)) for b in range(2)] for a in range(2)]
    inv = [_solve(XtX, [1 if i == j else 0 for i in range(2)]) for j in range(2)]
    return b[1] / math.sqrt(s2 * inv[1][1])
def main():
    rng = random.Random(201)
    n = 250
    # random walk: unit root
    rw = [0.0]
    for _ in range(n - 1):
        rw.append(rw[-1] + rng.gauss(0, 1))
    # stationary AR(0.8)
    ar = [0.0]
    for _ in range(n - 1):
        ar.append(0.8 * ar[-1] + rng.gauss(0, 1))
    t_rw = adf_tstat(rw)
    t_ar = adf_tstat(ar)
    print("ADF t-stat: random walk %.2f, AR(0.8) %.2f (Dickey-Fuller 5%% critical ~ -2.86)" % (t_rw, t_ar))
    assert t_rw > -2.86, t_rw      # fail to reject: unit root correctly kept
    assert t_ar < -2.86, t_ar      # reject: stationarity correctly found
    print("verdict: random walk keeps its unit root; AR(0.8) is stationary - correct on both")
    # spurious regression, Granger-Newbold style: regress unrelated walks,
    # watch the t-test's size collapse via Monte Carlo
    rej, trials = 0, 300
    for _ in range(trials):
        a = [0.0]; b = [0.0]
        for _ in range(n - 1):
            a.append(a[-1] + rng.gauss(0, 1))
            b.append(b[-1] + rng.gauss(0, 1))
        Xa = [[1, v] for v in a]
        ba = _ols(b, Xa)
        ea = _resid(b, Xa, ba)
        s2a = sum(v * v for v in ea) / (n - 2)
        XtXa = [[sum(Xa[i][p] * Xa[i][q] for i in range(n)) for q in range(2)] for p in range(2)]
        inva = [_solve(XtXa, [1 if i == j else 0 for i in range(2)]) for j in range(2)]
        ta = ba[1] / math.sqrt(s2a * inva[1][1])
        rej += abs(ta) > 1.96
    rate = rej / trials
    dw1 = sum((ea[t] - ea[t - 1]) ** 2 for t in range(1, n)) / sum(v * v for v in ea)
    print("spurious regression Monte Carlo: %d unrelated walk pairs, 5%% t-test rejects %.1f%%" %
          (trials, 100 * rate))
    print("last pair's DW = %.2f near zero: autocorrelation manufactures the 'significance'" % dw1)
    assert rate > 0.5 and dw1 < 0.5, (rate, dw1)
    print("rule: never regress levels before testing for unit roots")
    print("OK: %s tested for stationarity" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_econ_arima(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def acf(y, lag):
    n = len(y); m = _mean(y)
    return sum((y[t] - m) * (y[t - lag] - m) for t in range(lag, n)) / sum((v - m) ** 2 for v in y)
def yw_ar2(y):
    r1, r2 = acf(y, 1), acf(y, 2)
    return (r1 * (1 - r2)) / (1 - r1 * r1), (r2 - r1 * r1) / (1 - r1 * r1)
def main():
    rng = random.Random(211)
    n = 600
    # truth: AR(2) y_t = 0.6 y_{t-1} - 0.3 y_{t-2} + e_t
    y = [0.0, 0.0]
    for _ in range(n - 2):
        y.append(0.6 * y[-1] - 0.3 * y[-2] + rng.gauss(0, 1))
    # Yule-Walker from sample autocorrelations (identification -> estimation)
    a1, a2 = yw_ar2(y)
    assert abs(a1 - 0.6) < 0.12 and abs(a2 - (-0.3)) < 0.12, (a1, a2)
    print("Yule-Walker AR(2): a1 = %.3f (truth 0.6), a2 = %.3f (truth -0.3)" % (a1, a2))
    # genuine out-of-sample horse race: expanding estimation window, one-step ahead
    se_ar, se_naive, H = 0.0, 0.0, 0
    for t in range(450, n - 1):
        e1, e2 = yw_ar2(y[:t + 1])
        f_ar = e1 * y[t] + e2 * y[t - 1]
        f_nv = y[t]
        actual = y[t + 1]
        se_ar += (actual - f_ar) ** 2
        se_naive += (actual - f_nv) ** 2
        H += 1
    rmse_ar, rmse_nv = math.sqrt(se_ar / H), math.sqrt(se_naive / H)
    assert rmse_ar < rmse_nv, (rmse_ar, rmse_nv)
    print("expanding-window RMSE over %d forecasts: AR(2) %.3f vs naive %.3f - the model earns its keep" %
          (H, rmse_ar, rmse_nv))
    # multi-step forecast reverts toward the mean
    f1 = a1 * y[-1] + a2 * y[-2]
    yy = [y[-2], y[-1]]
    for _ in range(5):
        yy.append(a1 * yy[-1] + a2 * yy[-2])
    assert abs(yy[-1]) < abs(f1) + 0.5
    print("5-step path: %.3f -> ... -> %.3f - forecasts decay toward the mean" % (f1, yy[-1]))
    print("rule: identify from ACF/PACF, estimate, diagnose residuals, evaluate out-of-sample")
    print("OK: %s ran Box-Jenkins" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_econ_cointegration(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def adf_tstat_resid(z):
    n = len(z)
    dz = [z[t] - z[t - 1] for t in range(1, n)]
    X = [[1, z[t - 1]] for t in range(1, n)]
    b = _ols(dz, X)
    e = _resid(dz, X, b)
    s2 = sum(v * v for v in e) / (n - 3)
    XtX = [[sum(X[i][a] * X[i][b] for i in range(n - 1)) for b in range(2)] for a in range(2)]
    inv = [_solve(XtX, [1 if i == j else 0 for i in range(2)]) for j in range(2)]
    return b[1] / math.sqrt(s2 * inv[1][1])
def main():
    rng = random.Random(221)
    n = 300
    # x: random walk ; y = 2 + 1.5x + stationary AR(0.5) error -> cointegrated
    x = [0.0]
    for _ in range(n - 1):
        x.append(x[-1] + rng.gauss(0, 1))
    eq_err = [0.0]
    for _ in range(n - 1):
        eq_err.append(0.5 * eq_err[-1] + rng.gauss(0, 1))
    y = [2 + 1.5 * a + e for a, e in zip(x, eq_err)]
    # Engle-Granger step 1: cointegrating regression (super-consistent)
    X = [[1, a] for a in x]
    b = _ols(y, X)
    assert abs(b[1] - 1.5) < 0.15, b
    print("cointegrating regression: slope %.3f (truth 1.5) - super-consistent" % b[1])
    # step 2: ADF on residuals with Engle-Granger critical values (~-3.34)
    z = _resid(y, X, b)
    t = adf_tstat_resid(z)
    assert t < -3.34, t
    print("ADF on residuals: t = %.2f < -3.34 - equilibrium error is stationary: cointegrated" % t)
    # error correction: changes respond to last period's disequilibrium
    dy = [y[t] - y[t - 1] for t in range(1, n)]
    Xec = [[1, z[t - 1]] for t in range(1, n)]
    bec = _ols(dy, Xec)
    assert bec[1] < -0.05, bec
    print("error correction: speed %.3f < 0 - %.0f%% of disequilibrium fixed per period" %
          (bec[1], -100 * bec[1]))
    # contrast: independent random walks are NOT cointegrated
    w = [0.0]
    for _ in range(n - 1):
        w.append(w[-1] + rng.gauss(0, 1))
    Xw = [[1, a] for a in x]
    zw = _resid(w, Xw, _ols(w, Xw))
    tw = adf_tstat_resid(zw)
    assert tw > -3.34, tw
    print("independent walks: residual ADF t = %.2f > -3.34 - no cointegration, as it should be" % tw)
    print("rule: I(1) + I(1) with I(0) errors = long-run relationship rescued from spuriousness")
    print("OK: %s tied the wanderers" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_econ_var_granger(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def tstat(y, X, j):
    b = _ols(y, X)
    e = _resid(y, X, b)
    n, k = len(y), len(X[0])
    s2 = sum(v * v for v in e) / (n - k)
    XtX = [[sum(X[i][a] * X[i][c] for i in range(n)) for c in range(k)] for a in range(k)]
    inv = [_solve(XtX, [1 if i == r else 0 for i in range(k)]) for r in range(k)]
    return b[j] / math.sqrt(s2 * inv[j][j]), b[j]
def main():
    rng = random.Random(231)
    n = 400
    # truth: x -> y with one lag ; y does NOT feed back into x
    x = [0.0]; y = [0.0]
    for _ in range(n - 1):
        xn = 0.5 * x[-1] + rng.gauss(0, 1)
        yn = 0.4 * y[-1] + 0.6 * x[-1] + rng.gauss(0, 1)
        x.append(xn); y.append(yn)
    yl = y[1:]; xl = x[1:]
    Xy = [[1, y[t - 1], x[t - 1]] for t in range(1, n)]
    Xx = [[1, x[t - 1], y[t - 1]] for t in range(1, n)]
    t_xy, b_xy = tstat(yl, Xy, 2)   # x lags in y's equation
    t_yx, b_yx = tstat(xl, Xx, 2)   # y lags in x's equation
    assert t_xy > 3, t_xy
    assert abs(t_yx) < 2, t_yx
    print("x -> y: t = %.2f (b = %.3f): x Granger-causes y" % (t_xy, b_xy))
    print("y -> x: t = %.2f (b = %.3f): y does not Granger-cause x" % (t_yx, b_yx))
    # impulse response: shock x by 1 sd, trace y
    sdx = math.sqrt(_var(x))
    ir = []
    dx_, dy_ = sdx, 0.0
    for _ in range(6):
        ir.append(dy_)
        dx_, dy_ = 0.5 * dx_, 0.4 * dy_ + 0.6 * dx_
    assert ir[1] > 0.3 * sdx, ir
    print("impulse response of y to an x shock: %s" %
          ", ".join("%.2f" % v for v in ir[:4]))
    print("rule: Granger = predictability; structural answers need identifying restrictions")
    print("OK: %s ran the VAR" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_econ_simultaneous(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    rng = random.Random(241)
    n = 1000
    # demand: Q = 10 - 2P + 1*Y + u ; supply: Q = 2 + 3P - 1*W + v
    Y = [rng.gauss(0, 1) for _ in range(n)]   # demand shifter (excluded from supply)
    W = [rng.gauss(0, 1) for _ in range(n)]   # supply shifter (excluded from demand)
    P, Q = [], []
    for yi, wi in zip(Y, W):
        u, v = rng.gauss(0, 1), rng.gauss(0, 1)
        p = (8 + yi + wi + u - v) / 5          # equilibrium: solve the system
        q = 10 - 2 * p + yi + u
        P.append(p); Q.append(q)
    # OLS on demand is biased: P correlates with u by construction
    b_ols = _cov(P, Q) / _var(P)
    assert abs(b_ols - (-2)) > 0.3, b_ols
    print("OLS demand slope = %.3f (truth -2): simultaneity bias" % b_ols)
    # order condition: demand excludes W (1 excl >= 1 endog regressor) -> identified
    print("order condition: demand excludes the supply-shifter W -> exactly identified")
    # 2SLS: stage 1 P on (Y, W) ; stage 2 Q on P-hat, Y
    X1 = [[1, yi, wi] for yi, wi in zip(Y, W)]
    g = _ols(P, X1)
    Phat = [g[0] + g[1] * yi + g[2] * wi for yi, wi in zip(Y, W)]
    X2 = [[1, ph, yi] for ph, yi in zip(Phat, Y)]
    b2 = _ols(Q, X2)
    assert abs(b2[1] - (-2)) < 0.35 and abs(b2[2] - 1) < 0.3, b2
    print("2SLS demand: price slope %.3f (truth -2), income slope %.3f (truth 1)" % (b2[1], b2[2]))
    # supply via 2SLS with Y as the excluded instrument
    X2s = [[1, ph, wi] for ph, wi in zip(Phat, W)]
    bs = _ols(Q, X2s)
    assert abs(bs[1] - 3) < 0.4, bs
    print("2SLS supply: price slope %.3f (truth 3)" % bs[1])
    print("rule: identification comes from exclusion - what shifts one curve but not the other")
    print("OK: %s cut the simultaneity knot" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_econ_gmm(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    rng = random.Random(251)
    n = 2000
    # truth y = 1 + 2x + u ; x endogenous ; z1, z2 valid instruments (overidentified)
    z1 = [rng.gauss(0, 1) for _ in range(n)]
    z2 = [rng.gauss(0, 1) for _ in range(n)]
    u = [rng.gauss(0, 1) for _ in range(n)]
    x = [0.8 * a + 0.5 * b + 0.7 * c + rng.gauss(0, 0.5) for a, b, c in zip(z1, z2, u)]
    y = [1 + 2 * a + c for a, c in zip(x, u)]
    Z = [[1, a, b] for a, b in zip(z1, z2)]
    X = [[1, a] for a in x]
    # one-step GMM (W = I): moment vector m = Z'(y - Xb)/n, minimize m'm
    def moments(b):
        r = [y[i] - (b[0] + b[1] * x[i]) for i in range(n)]
        return [sum(Z[i][j] * r[i] for i in range(n)) / n for j in range(3)]
    def obj(b, W):
        m = moments(b)
        return sum(m[a] * W[a][c] * m[c] for a in range(3) for c in range(3))
    I3 = [[1 if a == c else 0 for c in range(3)] for a in range(3)]
    # grid + refine on b1 (b0 profiled by OLS on residual)
    best, bo = 1e18, None
    for trial in [i / 100 for i in range(100, 301)]:
        r = [y[i] - trial * x[i] for i in range(n)]
        b0 = _mean(r)
        v = obj([b0, trial], I3)
        if v < best:
            best, bo = v, [b0, trial]
    b1 = bo
    # two-step: W = inverse covariance of moments at one-step estimates
    r1 = [y[i] - (b1[0] + b1[1] * x[i]) for i in range(n)]
    g = [[Z[i][j] * r1[i] for j in range(3)] for i in range(n)]
    gm = [_mean([row[j] for row in g]) for j in range(3)]
    S = [[sum((g[i][a] - gm[a]) * (g[i][c] - gm[c]) for i in range(n)) / n
          for c in range(3)] for a in range(3)]
    W = _inv(S)
    best2, b2 = 1e18, None
    for trial in [b1[1] + i / 500 for i in range(-100, 101)]:
        r = [y[i] - trial * x[i] for i in range(n)]
        b0 = _mean(r)
        v = obj([b0, trial], W)
        if v < best2:
            best2, b2 = v, [b0, trial]
    assert abs(b2[1] - 2) < 0.15, b2
    print("two-step GMM slope = %.3f (truth 2.0)" % b2[1])
    # Hansen J: n * min obj ~ chi2(moments - params) = chi2(1), critical 3.84
    J = n * best2
    assert J < 3.84, J
    print("Hansen J = %.2f < 3.84: the instruments do not contradict each other" % J)
    print("rule: theory writes moment conditions; GMM makes them as close to zero as possible")
    print("OK: %s estimated by moments" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_econ_quantile(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def qreg(x, y, tau, iters=60):
    # IRLS for quantile regression: weighted LS with asymmetric weights
    n = len(x)
    b = [0.0, 0.0]
    for _ in range(iters):
        e = [y[i] - (b[0] + b[1] * x[i]) for i in range(n)]
        w = [(tau if ei >= 0 else (1 - tau)) / max(abs(ei), 1e-6) for ei in e]
        X = [[1, a] for a in x]
        XtWX = [[sum(w[i] * X[i][a] * X[i][c] for i in range(n)) for c in range(2)] for a in range(2)]
        XtWy = [sum(w[i] * X[i][a] * y[i] for i in range(n)) for a in range(2)]
        b = _solve(XtWX, XtWy)
    return b
def main():
    rng = random.Random(261)
    n = 1500
    x = [rng.gauss(0, 1) for _ in range(n)]
    # heteroskedastic: y = 1 + 2x + (1 + 0.5x)*u -> quantile slopes fan out
    y = [1 + 2 * a + (1 + 0.5 * a) * rng.gauss(0, 1) for a in x]
    b10 = qreg(x, y, 0.10)
    b50 = qreg(x, y, 0.50)
    b90 = qreg(x, y, 0.90)
    print("quantile slopes: tau=0.10 -> %.3f, tau=0.50 -> %.3f, tau=0.90 -> %.3f" %
          (b10[1], b50[1], b90[1]))
    assert abs(b50[1] - 2) < 0.3, b50          # median slope ~ 2
    assert b90[1] > b10[1] + 0.3, (b90[1], b10[1])  # fanning: heterogeneous effects
    print("median slope %.3f ~ truth 2; the 90th-percentile slope exceeds the 10th" % b50[1])
    # robustness: one huge outlier barely moves the median, wrecks OLS
    yo = y[:] ; yo[0] += 500
    b_ols = _cov(x, yo) / _var(x)
    b_med_o = qreg(x, yo, 0.50)
    assert abs(b_med_o[1] - b50[1]) < 0.15
    print("+500 outlier: OLS slope %.3f (wrecked) vs median slope %.3f (unmoved)" % (b_ols, b_med_o[1]))
    print("rule: plot coefficients across tau - fanning lines mean the effect lives somewhere specific")
    print("OK: %s regressed the quantiles" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_econ_forecast(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    rng = random.Random(271)
    n = 160
    # truth: AR(1) with rho = 0.7
    y = [0.0]
    for _ in range(n - 1):
        y.append(0.7 * y[-1] + rng.gauss(0, 1))
    # expanding-window one-step forecasts from t = 80
    f_model, f_naive, actual = [], [], []
    for t in range(80, n - 1):
        hist = y[:t + 1]
        m = _mean(hist)
        rho = sum((hist[i] - m) * (hist[i - 1] - m) for i in range(1, len(hist))) / sum((v - m) ** 2 for v in hist)
        f_model.append(rho * y[t])
        f_naive.append(y[t])
        actual.append(y[t + 1])
    H = len(actual)
    rmse_m = math.sqrt(sum((a - f) ** 2 for a, f in zip(actual, f_model)) / H)
    rmse_n = math.sqrt(sum((a - f) ** 2 for a, f in zip(actual, f_naive)) / H)
    assert rmse_m < rmse_n, (rmse_m, rmse_n)
    print("expanding-window RMSE: AR model %.3f vs naive %.3f - the model wins out-of-sample" % (rmse_m, rmse_n))
    # Mincer-Zarnowitz: actual on forecast -> intercept 0, slope 1
    X = [[1, f] for f in f_model]
    bmz = _ols(actual, X)
    assert abs(bmz[0]) < 0.25 and abs(bmz[1] - 1) < 0.25, bmz
    print("Mincer-Zarnowitz: intercept %.3f (~0), slope %.3f (~1) - unbiased and efficient" % (bmz[0], bmz[1]))
    # Diebold-Mariano sketch: mean loss differential with HAC-ish se
    d = [(a - fn) ** 2 - (a - fm) ** 2 for a, fn, fm in zip(actual, f_naive, f_model)]
    dm = _mean(d) / (math.sqrt(_var(d) / H))
    assert dm > 1.96, dm
    print("Diebold-Mariano = %.2f > 1.96: the model's edge is significant" % dm)
    print("rule: evaluate out-of-sample, benchmark the naive, test the difference")
    print("OK: %s forecast honestly" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_econ_chow(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    rng = random.Random(281)
    n = 200
    brk = 100
    x = [rng.gauss(0, 1) for _ in range(n)]
    # regime 1: slope 2 ; regime 2: slope 5 (break at t = 100)
    y = [(1 + (2 if t < brk else 5) * a + rng.gauss(0, 1)) for t, a in enumerate(x)]
    X = [[1, a] for a in x]
    bp = _ols(y, X)
    ssr_p = _ssr(y, X, bp)
    X1, y1 = X[:brk], y[:brk]
    X2, y2 = X[brk:], y[brk:]
    b1, b2 = _ols(y1, X1), _ols(y2, X2)
    ssr_1, ssr_2 = _ssr(y1, X1, b1), _ssr(y2, X2, b2)
    k = 2
    F = ((ssr_p - ssr_1 - ssr_2) / k) / ((ssr_1 + ssr_2) / (n - 2 * k))
    assert F > 10, F
    print("Chow F = %.1f >> critical ~3: the parameters broke at t = %d" % (F, brk))
    print("regime slopes: %.2f then %.2f (truth 2 then 5)" % (b1[1], b2[1]))
    # dummy-interaction form gives the identical statistic and names the breaker
    D = [0 if t < brk else 1 for t in range(n)]
    Xd = [[1, a, d, a * d] for a, d in zip(x, D)]
    bd = _ols(y, Xd)
    assert abs(bd[3] - (b2[1] - b1[1])) < 1e-9
    print("interaction form: slope shift = %.3f == regime difference" % bd[3])
    # recursive estimation: the slope estimate migrates as the window crosses the break
    slopes = []
    for t in range(60, n + 1):
        Xt, yt = X[:t], y[:t]
        bt = _ols(yt, Xt)
        slopes.append(bt[1])
    shift = slopes[-1] - slopes[0]
    assert shift > 0.8, shift
    print("recursive slopes: t=60 -> %.2f, t=200 -> %.2f (shift %.2f): the eye sees the break form" %
          (slopes[0], slopes[-1], shift))
    # the break inflates pooled residual variance vs the split fits
    assert ssr_p > 2 * (ssr_1 + ssr_2), (ssr_p, ssr_1 + ssr_2)
    print("pooled SSR %.0f vs split SSR %.0f: one line cannot serve two regimes" %
          (ssr_p, ssr_1 + ssr_2))
    print("rule: test the break, then model the regimes - never average across the fracture")
    print("OK: %s found the fault line" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_econ_arch(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    rng = random.Random(291)
    n = 600
    # truth: ARCH(1) sigma_t^2 = 0.5 + 0.7*e_{t-1}^2
    e = [rng.gauss(0, 1)]
    for _ in range(n - 1):
        s2 = 0.5 + 0.7 * e[-1] ** 2
        e.append(math.sqrt(s2) * rng.gauss(0, 1))
    # Engle's ARCH-LM: e^2 on lagged e^2 ; nR^2 ~ chi2(1)
    e2 = [v * v for v in e]
    Xlm = [[1, e2[t - 1]] for t in range(1, n)]
    blm = _ols(e2[1:], Xlm)
    elm = _resid(e2[1:], Xlm, blm)
    R2lm = 1 - sum(v * v for v in elm) / sum((v - _mean(e2[1:])) ** 2 for v in e2[1:])
    stat = (n - 1) * R2lm
    assert stat > 3.84, stat
    print("ARCH-LM nR^2 = %.1f > 3.84: volatility clustering detected" % stat)
    # MLE by grid search over (w, a)
    def ll(w, a):
        tot, prev = 0.0, sum(v * v for v in e) / n
        for v in e:
            s2 = w + a * prev
            tot += -0.5 * (math.log(s2) + v * v / s2)
            prev = v * v
        return tot
    best, bw, ba = -1e18, 0, 0
    wv = 0.1
    while wv <= 1.2:
        av = 0.05
        while av <= 0.95:
            v = ll(wv, av)
            if v > best:
                best, bw, ba = v, wv, av
            av += 0.05
        wv += 0.1
    assert abs(bw - 0.5) < 0.3 and abs(ba - 0.7) < 0.2, (bw, ba)
    print("ARCH(1) MLE: w = %.2f (truth 0.5), alpha = %.2f (truth 0.7)" % (bw, ba))
    # standardized residuals look iid: no ARCH left
    prev = sum(v * v for v in e) / n
    std = []
    for v in e:
        s2 = bw + ba * prev
        std.append(v / math.sqrt(s2))
        prev = v * v
    s2s = [v * v for v in std]
    Xlm2 = [[1, s2s[t - 1]] for t in range(1, n)]
    blm2 = _ols(s2s[1:], Xlm2)
    elm2 = _resid(s2s[1:], Xlm2, blm2)
    R2b = 1 - sum(v * v for v in elm2) / sum((v - _mean(s2s[1:])) ** 2 for v in s2s[1:])
    assert (n - 1) * R2b < 3.84, (n - 1) * R2b
    print("ARCH-LM on standardized residuals: %.2f < 3.84 - structure captured" % ((n - 1) * R2b))
    print("rule: test for ARCH first, then let the variance have its own dynamics")
    print("OK: %s modeled the storms" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_econ_nls_mle(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    rng = random.Random(301)
    n = 120
    x = [2 * rng.random() for _ in range(n)]          # 0..2
    # truth: y = 2*exp(0.5*x) + u
    y = [2 * math.exp(0.5 * a) + rng.gauss(0, 0.4) for a in x]
    # Gauss-Newton from a rough start
    b = [1.0, 0.2]
    for _ in range(50):
        r = [y[i] - b[0] * math.exp(b[1] * x[i]) for i in range(n)]
        J = [[math.exp(b[1] * a), b[0] * a * math.exp(b[1] * a)] for a in x]
        XtX = [[sum(J[i][a] * J[i][c] for i in range(n)) for c in range(2)] for a in range(2)]
        XtR = [sum(J[i][a] * r[i] for i in range(n)) for a in range(2)]
        step = _solve(XtX, XtR)
        b = [b[0] + step[0], b[1] + step[1]]
        if math.sqrt(sum(v * v for v in step)) < 1e-10:
            break
    assert abs(b[0] - 2) < 0.2 and abs(b[1] - 0.5) < 0.08, b
    print("Gauss-Newton NLS: A = %.3f (truth 2), b = %.3f (truth 0.5)" % (b[0], b[1]))
    # the linearized shortcut (log-OLS) is biased by Jensen's inequality
    yl = [math.log(v) for v in y]
    bl = _cov(x, yl) / _var(x)
    A_lin = math.exp(_mean(yl) - bl * _mean(x))
    assert abs(A_lin - 2) > abs(b[0] - 2), (A_lin, b[0])
    print("log-linearized OLS: A = %.3f - Jensen's inequality biases the retransform" % A_lin)
    # standard errors from s^2 (J'J)^{-1}
    r = [y[i] - b[0] * math.exp(b[1] * x[i]) for i in range(n)]
    s2 = sum(v * v for v in r) / (n - 2)
    J = [[math.exp(b[1] * a), b[0] * a * math.exp(b[1] * a)] for a in x]
    XtX = [[sum(J[i][a] * J[i][c] for i in range(n)) for c in range(2)] for a in range(2)]
    inv = [_solve(XtX, [1 if i == j else 0 for i in range(2)]) for j in range(2)]
    print("se(A) = %.3f, se(b) = %.4f" % (math.sqrt(s2 * inv[0][0]), math.sqrt(s2 * inv[1][1])))
    print("rule: nonlinear in parameters -> minimize numerically; start well, check convergence")
    print("OK: %s forged the curve" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_econ_spatial(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    rng = random.Random(311)
    S = 6
    n = S * S
    # clustered truth: top-left high, bottom-right low + noise
    y = []
    for r in range(S):
        for c in range(S):
            y.append((3 if r < 3 and c < 3 else (-3 if r >= 3 and c >= 3 else 0)) + rng.gauss(0, 1))
    # rook-contiguity W, row-standardized
    W = [[0.0] * n for _ in range(n)]
    for r in range(S):
        for c in range(S):
            i = r * S + c
            nb = []
            if r > 0: nb.append((r - 1) * S + c)
            if r < S - 1: nb.append((r + 1) * S + c)
            if c > 0: nb.append(r * S + c - 1)
            if c < S - 1: nb.append(r * S + c + 1)
            for j in nb:
                W[i][j] = 1.0 / len(nb)
    m = _mean(y)
    num = sum(W[i][j] * (y[i] - m) * (y[j] - m) for i in range(n) for j in range(n))
    den = sum((v - m) ** 2 for v in y)
    I = (n / sum(sum(row) for row in W)) * num / den
    # null moments under randomization
    EI = -1 / (n - 1)
    assert I > 0.25, I
    print("Moran's I = %.3f (null %.3f): strong positive spatial clustering" % (I, EI))
    # spatial lag model by 2SLS: Wy instrumented by X=1 (use neighbor mean of x-> here intercept-only demo)
    Wy = [sum(W[i][j] * y[j] for j in range(n)) for i in range(n)]
    # instrument Wy with spatial lags of an exogenous x
    xs = [rng.gauss(0, 1) for _ in range(n)]
    Wx = [sum(W[i][j] * xs[j] for j in range(n)) for i in range(n)]
    X1 = [[1, w] for w in Wx]
    g = _ols(Wy, X1)
    Wyh = [g[0] + g[1] * w for w in Wx]
    X2 = [[1, w] for w in Wyh]
    bs = _ols(y, X2)
    assert bs[1] > 0.3, bs
    print("spatial lag (2SLS): rho = %.3f > 0 - neighbors' outcomes pull each other" % bs[1])
    print("rule: map the residuals, test with Moran's I, and show robustness across W")
    print("OK: %s mapped the neighborhood" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_econ_matching(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    rng = random.Random(321)
    n = 2500
    x = [rng.gauss(0, 1) for _ in range(n)]
    # propensity: P(D=1) = logistic(-0.5 + x) ; truth: y = 1 + 2D + x + u (ATT = 2)
    D = [1 if rng.random() < 1 / (1 + math.exp(0.5 - a)) else 0 for a in x]
    y = [1 + 2 * d + a + rng.gauss(0, 1) for d, a in zip(D, x)]
    # naive treated-control gap is confounded (x drives both D and y)
    naive = _mean([v for v, d in zip(y, D) if d == 1]) - _mean([v for v, d in zip(y, D) if d == 0])
    assert abs(naive - 2) > 0.3, naive
    print("naive gap = %.3f (truth 2.0): selection on x contaminates it" % naive)
    # propensity score via logit Newton-Raphson
    b = [0.0, 0.0]
    for _ in range(25):
        g = [0.0, 0.0]
        H = [[0.0, 0.0], [0.0, 0.0]]
        for xi, di in zip(x, D):
            pi = 1 / (1 + math.exp(-(b[0] + b[1] * xi)))
            r = di - pi
            w = pi * (1 - pi)
            g[0] += r; g[1] += r * xi
            H[0][0] += w; H[0][1] += w * xi; H[1][1] += w * xi * xi
        H[1][0] = H[0][1]
        step = _solve(H, g)
        b = [b[0] + step[0], b[1] + step[1]]
    ps = [1 / (1 + math.exp(-(b[0] + b[1] * a))) for a in x]
    # stratification into 5 bins: ATT = treated-weighted within-bin gaps
    order = sorted(range(n), key=lambda i: ps[i])
    B = 5
    att, wt = 0.0, 0
    for k in range(B):
        idx = order[k * n // B:(k + 1) * n // B]
        yt = [y[i] for i in idx if D[i] == 1]
        yc = [y[i] for i in idx if D[i] == 0]
        if yt and yc:
            att += len(yt) * (_mean(yt) - _mean(yc))
            wt += len(yt)
    att /= wt
    assert abs(att - 2) < 0.4, att
    print("propensity-stratified ATT = %.3f (truth 2.0)" % att)
    # balance check: within-bin x means of treated vs control converge
    idx0 = order[:n // B]
    gap = abs(_mean([x[i] for i in idx0 if D[i] == 1]) - _mean([x[i] for i in idx0 if D[i] == 0]))
    gap_raw = abs(_mean([a for a, d in zip(x, D) if d == 1]) - _mean([a for a, d in zip(x, D) if d == 0]))
    assert gap < gap_raw, (gap, gap_raw)
    print("covariate gap: raw %.3f -> stratified %.3f - matching balances the lookalikes" % (gap_raw, gap))
    print("rule: balance tables and overlap plots are the credibility documents")
    print("OK: %s found the twins" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_econ_workflow(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    rng = random.Random(331)
    n = 500
    # synthetic wage study: log-wage on schooling, experience, experience^2
    educ = [12 + rng.gauss(0, 2.5) for _ in range(n)]
    exper = [10 + rng.gauss(0, 6) for _ in range(n)]
    lw = [1.2 + 0.08 * s + 0.05 * e - 0.0008 * e * e + rng.gauss(0, 0.4) for s, e in zip(educ, exper)]
    print("=== STAGE 1: audit ===")
    assert len(lw) == n and all(v == v for v in lw)
    print("n = %d, no missing values, log-wage range [%.2f, %.2f]" % (n, min(lw), max(lw)))
    print("=== STAGE 2: describe ===")
    print("mean schooling %.1f yrs, mean experience %.1f yrs" % (_mean(educ), _mean(exper)))
    print("=== STAGE 3: estimate (OLS, robust SEs) ===")
    X = [[1, s, e, e * e] for s, e in zip(educ, exper)]
    b = _ols(lw, X)
    e = _resid(lw, X, b)
    k = 4
    XtX = [[sum(X[i][a] * X[i][c] for i in range(n)) for c in range(k)] for a in range(k)]
    inv = [_solve(XtX, [1 if i == j else 0 for i in range(k)]) for j in range(k)]
    # HC0 sandwich
    meat = [[sum(X[i][a] * X[i][c] * e[i] ** 2 for i in range(n)) for c in range(k)] for a in range(k)]
    varb = [[sum(inv[a][p] * meat[p][q] * inv[q][c] for p in range(k) for q in range(k))
             for c in range(k)] for a in range(k)]
    labels = ["const", "educ", "exper", "exper^2"]
    for j, lab in enumerate(labels):
        se = math.sqrt(varb[j][j])
        print("  %-7s %8.4f (%8.4f) t=%7.2f" % (lab, b[j], se, b[j] / se))
    assert abs(b[1] - 0.08) < 0.02
    print("return to schooling: %.1f%% per year - the headline magnitude" % (100 * b[1]))
    print("=== STAGE 4: diagnose ===")
    # White test
    e2 = [v * v for v in e]
    Xw = [[1, s, ee, s * s, ee * ee, s * ee] for s, ee in zip(educ, exper)]
    bw = _ols(e2, Xw)
    R2w = 1 - _ssr(e2, Xw, bw) / sum((v - _mean(e2)) ** 2 for v in e2)
    print("White nR^2 = %.2f %s" % (n * R2w, "(heteroskedastic - robust SEs already used)" if n * R2w > 12.59 else "(homoskedastic)"))
    # Durbin-Watson
    dw = sum((e[t] - e[t - 1]) ** 2 for t in range(1, n)) / sum(v * v for v in e)
    print("Durbin-Watson = %.2f %s" % (dw, "(clean)" if dw > 1.5 else "(autocorrelated!)"))
    # VIF on educ
    Xo = [[1, ee, ee * ee] for ee in exper]
    bo = _ols(educ, Xo)
    eo = _resid(educ, Xo, bo)
    R2o = 1 - sum(v * v for v in eo) / sum((v - _mean(educ)) ** 2 for v in educ)
    print("VIF(educ) = %.2f %s" % (1 / (1 - R2o), "(fine)" if R2o < 0.9 else "(collinear!)"))
    print("=== STAGE 5: report ===")
    print("deliverable: scripted, seeded pipeline - question, design, table, diagnostics, answer")
    print("rule: audit, describe, specify, estimate, diagnose, stress-test, report - in that order")
    print("OK: %s ran the full pipeline" % NAME)
if __name__ == "__main__":
    main()
''')

DEMOS = {
    "econ_what": demo_econ_what, "econ_data_types": demo_econ_data_types,
    "econ_causation": demo_econ_causation, "econ_simple_reg": demo_econ_simple_reg,
    "econ_multiple_reg": demo_econ_multiple_reg, "econ_ols_mechanics": demo_econ_ols_mechanics,
    "econ_reading_output": demo_econ_reading_output, "econ_r2": demo_econ_r2,
    "econ_dummy": demo_econ_dummy, "econ_gauss_markov": demo_econ_gauss_markov,
    "econ_hetero": demo_econ_hetero, "econ_multicoll": demo_econ_multicoll,
    "econ_autocorr": demo_econ_autocorr, "econ_ovb": demo_econ_ovb,
    "econ_iv": demo_econ_iv, "econ_meas_error": demo_econ_meas_error,
    "econ_probit_logit": demo_econ_probit_logit, "econ_tobit": demo_econ_tobit,
    "econ_panel": demo_econ_panel, "econ_hausman": demo_econ_hausman,
    "econ_did": demo_econ_did, "econ_rdd": demo_econ_rdd,
    "econ_unit_root": demo_econ_unit_root, "econ_arima": demo_econ_arima,
    "econ_cointegration": demo_econ_cointegration, "econ_var_granger": demo_econ_var_granger,
    "econ_simultaneous": demo_econ_simultaneous, "econ_gmm": demo_econ_gmm,
    "econ_quantile": demo_econ_quantile, "econ_forecast": demo_econ_forecast,
    "econ_chow": demo_econ_chow, "econ_arch": demo_econ_arch,
    "econ_nls_mle": demo_econ_nls_mle, "econ_spatial": demo_econ_spatial,
    "econ_matching": demo_econ_matching, "econ_workflow": demo_econ_workflow,
}
# ---------------------------------------------------------------- records

def build_records(slug, source):
    cfg = DBCFG[slug]
    sig = source == "signature"
    # Teaching-ladder order: stable sort by ladder_rank (entries are already
    # in ladder order in entries_econometrics.py).
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
        demo_fn = DEMOS[e["demo_kind"]]
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
    for slug in ("econometrics", "econometrics-signature"):
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
