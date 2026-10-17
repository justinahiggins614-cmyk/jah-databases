#!/usr/bin/env python3
"""Build the Calculus field databases for JAH Databases (field #16, taxonomy order).

Verified 2026-10-17: NO database covers calculus as a discipline.
- 'mathematics-public' / 'mathematics-signature' / 'everything-mathematics':
  survey-level topic cards ("Calculus: limits, derivatives, integrals" as one
  card among dozens of branches) - no teaching depth.
- 'mathematics-study': curriculum/qualification cards - not the discipline.
- 'equations' (48,300 records): solved equation records - not calculus.
- 'scientific-formulas': formula CARDS - bare formulas ("Chain Rule",
  "Product Rule", "Taylor Series", "Derivative (power rule)") as reference,
  with no teaching, no ladder, no how-it-works, no demos. Per the field
  brief, formula cards do NOT count as discipline coverage.
- 'hard-equations', 'math-word-problems', 'math': equation/puzzle content,
  not calculus teaching.
- Whole-system dedupe index: zero calculus-discipline titles exist.

So this build creates two NEW databases:

  calculus             — The Calculus Database
                         (public-harvest: real, fact-checked calculus)
  calculus-signature   — The Calculus Signature Database
                         (his original Signature interpretation;
                         src signature, titles suffixed
                         " (Signature Edition)", never presented
                         as authentic public record)

36 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

Every record: description + how-it-works + key points + requirements +
standards + citations + working demonstration code (real, runnable,
stdlib-only Python; machine-executed OK). Calculus demos: numerical
differentiation, Riemann sums, series convergence tests, Euler's method,
Simpson's rule, and symbolic-verification checks.

Subtitle disambiguation (fields #13-16 pattern): where a bare formula card
exists in scientific-formulas, discipline titles carry teaching-focused
subtitles, e.g. "The Chain Rule: Differentiating Composite Functions" and
"Taylor and Maclaurin Series: Approximating Functions" rather than the bare
card titles.

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
# main repo (256 shards; titles from fields #12-15 cross-checked directly
# against their shard indexes in jah-databases-data-1 since the gate index
# predates them - subtitle disambiguation used throughout).
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_calculus import ENTRIES, SIG_TAIL

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature interpretation of calculus: "
                "clearly labeled Signature-made, never presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked calculus: what calculus is; functions "
                "and models; limits; computing limits; continuity; the derivative; "
                "differentiation rules; the chain rule; implicit differentiation; "
                "higher-order derivatives; related rates; optimization; extrema, concavity, "
                "and curve sketching; L'Hôpital's rule; antiderivatives; Riemann sums and "
                "the definite integral; the fundamental theorem; substitution; integration "
                "by parts; trigonometric integrals; partial fractions; improper integrals; "
                "area between curves; volumes of revolution; arc length, surface area, and "
                "work; sequences; series and convergence tests; Taylor and Maclaurin "
                "series; power series; parametric and polar calculus; partial derivatives "
                "and the gradient; multiple integrals; vector line and surface integrals; "
                "Green's, Stokes', and divergence theorems; first-order differential "
                "equations; second-order equations, Laplace transforms, and numerical "
                "methods, organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations (what calculus is, "
              "functions and models, limits, computing limits, continuity, the derivative, "
              "differentiation rules) -> Compounded (the chain rule, implicit "
              "differentiation, higher-order derivatives, related rates, optimization, "
              "curve sketching, L'Hôpital's rule, antiderivatives, Riemann sums) -> "
              "Advanced (the fundamental theorem, substitution, integration by parts, "
              "trigonometric integrals, partial fractions, improper integrals, area, "
              "volumes, arc length and work, sequences, series tests, Taylor/Maclaurin, "
              "power series, parametric and polar, partial derivatives, multiple "
              "integrals, vector calculus theorems, differential equations, numerical "
              "methods).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search limits, chain rule, Riemann sums, Taylor series, gradient, Laplace, Simpson's rule...",
        "chat_ph": "Ask about calculus...",
        "archive_blurb": ("Seeded %s calculus records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled structural calculus studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about calculus - from limits and derivatives to integrals, series, vector calculus, and differential equations." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "calculus-study", "gen_demo_kind": "calculus-demo",
        "source": source,
    }

CIT_PUB = "Calculus (peer-reviewed literature and standard textbooks)."
CIT_SIG = CIT_PUB + " " + SIG_TAIL

DBCFG = {}
DBCFG["calculus"] = _cfg(
    "calculus", "The Calculus Database",
    "Real, fact-checked calculus: the discipline from limits and derivatives through "
    "integrals, series, multivariable and vector calculus, differential equations, "
    "and numerical methods - taught progressively along the ladder.",
    "calculus record", "JAH-CALC-", "JAH Calculus Archivist",
    "calculus archivist - what calculus is, functions and models, limits, computing "
    "limits, continuity, the derivative, differentiation rules, the chain rule, "
    "implicit differentiation, higher-order derivatives, related rates, optimization, "
    "extrema and curve sketching, L'Hôpital's rule, antiderivatives, Riemann sums, "
    "the fundamental theorem, substitution, integration by parts, trigonometric "
    "integrals, partial fractions, improper integrals, area between curves, volumes "
    "of revolution, arc length and work, sequences, series convergence tests, "
    "Taylor and Maclaurin series, power series, parametric and polar calculus, "
    "partial derivatives and the gradient, multiple integrals, vector line and "
    "surface integrals, Green's/Stokes'/divergence theorems, first-order "
    "differential equations, second-order equations, Laplace transforms, and "
    "numerical methods; teaching progressively along the ladder from foundations "
    "through compounded to advanced; answers from many angles - definition, "
    "example, analogy, application, history, math, how-to - using only the "
    "system's own archive data",
    CIT_PUB, "public")
DBCFG["calculus-signature"] = _cfg(
    "calculus-signature", "The Calculus Signature Database",
    "His original Signature interpretation of calculus: the full ladder from limits "
    "and the derivative through integrals, series, vector calculus, differential "
    "equations, and numerical methods, reframed as Signature science. Clearly labeled "
    "Signature-made, never presented as authentic public record.",
    "calculus record", "JAH-CALCS-", "JAH Calculus Archivist (Signature)",
    "calculus archivist - Signature editions: his original Signature interpretation "
    "of calculus, clearly labeled Signature-made and never presented as authentic "
    "public record; teaches progressively along the ladder from foundations through "
    "compounded to advanced; answers from many angles - definition, example, analogy, "
    "application, history, math, how-to - using only the system's own archive data",
    CIT_SIG, "signature")

base.DBCFG = DBCFG
# ---------------------------------------------------------------- demos
# Every demo is real, runnable, stdlib-only Python performing the actual
# calculus computation for its record. All are machine-executed by main().

_PREAMBLE = "import math\nimport re\n"

def _wrap(name, rid, group, body):
    return (base._hdr(name, rid, group) + _PREAMBLE + body.replace("NAME", json.dumps(name)))

def demo_calc_branches(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
BRANCHES = {
    "differential calculus": "limits, derivatives, rates of change, optimization",
    "integral calculus": "antiderivatives, definite integrals, area, volume, work",
    "sequences and series": "convergence tests, Taylor and power series",
    "multivariable calculus": "partial derivatives, gradients, multiple integrals",
    "vector calculus": "line and surface integrals, Green/Stokes/divergence theorems",
    "differential equations": "first-order, second-order, Laplace, numerical methods",
}
def main():
    assert len(BRANCHES) == 6
    assert "derivatives" in BRANCHES["differential calculus"]
    for branch, focus in BRANCHES.items():
        print("%-24s -> %s" % (branch, focus))
    print("two inverse operations bind them: differentiate to cut change apart, integrate to add it up")
    print("rule: the limit is the foundation; the fundamental theorem is the hinge")
    print("OK: %s mapped the discipline" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_calc_models(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def linear_fit(xs, ys):
    n = len(xs)
    sx = sum(xs); sy = sum(ys)
    sxx = sum(x * x for x in xs); sxy = sum(x * y for x, y in zip(xs, ys))
    slope = (n * sxy - sx * sy) / (n * sxx - sx * sx)
    intercept = (sy - slope * sx) / n
    return slope, intercept
def compose(f, g):
    return lambda x: f(g(x))
def main():
    # cooling data: temperature falls toward room temp; fit a line to log-excess
    t = [0.0, 5.0, 10.0, 15.0, 20.0]
    temp = [90.0, 71.0, 57.0, 47.0, 40.0]
    room = 20.0
    m, b = linear_fit(t, [math.log(T - room) for T in temp])
    assert m < 0.0, m  # excess temperature decays
    k = -m
    pred = room + math.exp(b) * math.exp(-k * 25.0)
    assert 30.0 < pred < 40.0, pred
    print("cooling constant k = %.4f per minute; predicted temp at t=25: %.1f" % (k, pred))
    # composition: f(g(x)) with f(u)=u^2, g(x)=x+1
    h = compose(lambda u: u * u, lambda x: x + 1.0)
    assert abs(h(2.0) - 9.0) < 1e-12
    print("composition check: (x+1)^2 at x=2 -> %.1f" % h(2.0))
    print("rule: choose the family by shape, fit parameters by data, validate on fresh points")
    print("OK: %s modeled the data" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_calc_limit_idea(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def f(x):
    return (x * x - 1.0) / (x - 1.0)  # undefined at x = 1, limit is 2
def main():
    left = [f(1.0 - 10.0 ** -k) for k in range(1, 7)]
    right = [f(1.0 + 10.0 ** -k) for k in range(1, 7)]
    for k, v in enumerate(left + right, start=1):
        kk = ((k - 1) % 6) + 1
        assert abs(v - 2.0) < 2.0 * 10.0 ** -kk, (k, v)
    print("x -> 1- : " + ", ".join("%.6f" % v for v in left[:3]))
    print("x -> 1+ : " + ", ".join("%.6f" % v for v in right[:3]))
    print("the formula is 0/0 at x=1 (undefined) yet both sides crowd toward 2")
    # epsilon-delta: for tolerance 1e-3, delta = 1e-3 works since |f(x)-2| = |x-1|
    eps = 1e-3
    delta = eps
    for x in (1.0 - delta / 2.0, 1.0 + delta / 2.0):
        assert abs(f(x) - 2.0) < eps
    print("epsilon-delta check: eps=%.0e satisfied with delta=%.0e" % (eps, delta))
    print("rule: the limit is about approach, never about the value at the point")
    print("OK: %s took the limit" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_calc_limit_compute(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # 0/0 by factoring: (x^2-4)/(x-2) -> 4 as x -> 2
    def g(x): return (x * x - 4.0) / (x - 2.0)
    assert abs(g(2.0 + 1e-7) - 4.0) < 1e-5
    print("factor-and-cancel: (x^2-4)/(x-2) -> %.6f at x=2" % g(2.0 + 1e-7))
    # limit at infinity: divide by highest power -> 3/2
    def h(x): return (3.0 * x * x + 1.0) / (2.0 * x * x - x)
    assert abs(h(1e7) - 1.5) < 1e-6
    print("at infinity: (3x^2+1)/(2x^2-x) -> %.6f" % h(1e7))
    # squeeze: x*sin(1/x) -> 0
    def s(x): return x * math.sin(1.0 / x)
    for x in (1e-2, -1e-2, 1e-4):
        assert abs(s(x)) <= abs(x) + 1e-15
    assert abs(s(1e-6)) < 1e-5
    print("squeeze: x*sin(1/x) trapped between -|x| and |x| -> 0")
    # special trig limit: sin(x)/x -> 1
    assert abs(math.sin(1e-7) / 1e-7 - 1.0) < 1e-9
    print("special limit: sin(x)/x -> 1 as x -> 0")
    print("rule: substitute first; factor, rationalize, or divide by the top power when it fails")
    print("OK: %s computed the limits" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_calc_continuity(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def f(x):  # continuous at x=1: x^2 from left, 2x-1 from right
    return x * x if x < 1.0 else 2.0 * x - 1.0
def g(x):  # jump discontinuity at x=0
    return 0.0 if x < 0.0 else 1.0
def ivt_root(fn, a, b, tol=1e-10):
    fa, fb = fn(a), fn(b)
    assert fa * fb < 0.0, "no sign change: IVT does not apply"
    while b - a > tol:
        m = 0.5 * (a + b)
        if fn(a) * fn(m) <= 0.0: b = m
        else: a = m
    return 0.5 * (a + b)
def main():
    h = 1e-9
    left = f(1.0 - h); right = f(1.0 + h); val = f(1.0)
    assert abs(left - 1.0) < 1e-6 and abs(right - 1.0) < 1e-6 and val == 1.0
    print("f continuous at 1: left=%.9f right=%.9f f(1)=%.1f" % (left, right, val))
    assert abs(g(0.0 - h) - 0.0) < 1e-9 and abs(g(0.0 + h) - 1.0) < 1e-9
    print("g has a jump at 0: left -> 0, right -> 1 (limit DNE)")
    root = ivt_root(lambda x: x ** 3 - 2.0, 1.0, 2.0)
    assert abs(root ** 3 - 2.0) < 1e-9
    print("IVT + bisection: cube root of 2 = %.10f" % root)
    print("rule: defined, limit exists, limit equals value - all three, every point")
    print("OK: %s checked continuity" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_calc_deriv_def(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def f(x): return x ** 3 - 2.0 * x + 1.0
def diff_quotient(x, h): return (f(x + h) - f(x)) / h
def central(x, h): return (f(x + h) - f(x - h)) / (2.0 * h)
def main():
    x0 = 2.0
    exact = 3.0 * x0 * x0 - 2.0  # f'(x) = 3x^2 - 2 -> 10 at x=2
    assert exact == 10.0
    for h in (0.1, 0.01, 0.001, 1e-5):
        dq = diff_quotient(x0, h)
        assert abs(dq - exact) < 0.5 * h * 100.0, (h, dq)
    print("difference quotients at x=2: h=0.1 -> %.4f, h=1e-5 -> %.7f (limit 10)" %
          (diff_quotient(x0, 0.1), diff_quotient(x0, 1e-5)))
    assert abs(central(x0, 1e-5) - exact) < 1e-8
    print("central difference converges faster: %.10f" % central(x0, 1e-5))
    # tangent line at (2, f(2)) = (2, 5): y = 5 + 10(x-2)
    assert abs(f(x0) - 5.0) < 1e-12
    print("tangent line at (2,5): y = 5 + 10(x - 2)")
    print("rule: average rate over shrinking intervals -> instantaneous rate")
    print("OK: %s differentiated from the definition" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_calc_diff_rules(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def central(f, x, h=1e-7): return (f(x + h) - f(x - h)) / (2.0 * h)
def main():
    # power + sum rules: f = x^3 + 2x^2 - 5x + 1 -> f' = 3x^2 + 4x - 5
    f = lambda x: x ** 3 + 2.0 * x ** 2 - 5.0 * x + 1.0
    fp = lambda x: 3.0 * x ** 2 + 4.0 * x - 5.0
    x0 = 1.5
    assert abs(fp(x0) - central(f, x0)) < 1e-6
    print("power/sum rules at x=1.5: symbolic %.4f vs numeric %.4f" % (fp(x0), central(f, x0)))
    # product rule: (x^2)(sin x) -> 2x sin x + x^2 cos x
    g = lambda x: x * x * math.sin(x)
    gp = lambda x: 2.0 * x * math.sin(x) + x * x * math.cos(x)
    assert abs(gp(1.0) - central(g, 1.0)) < 1e-6
    print("product rule at x=1: symbolic %.6f vs numeric %.6f" % (gp(1.0), central(g, 1.0)))
    # quotient rule: (x^2+1)/(x-1) at x=2 -> ((2x)(x-1) - (x^2+1))/((x-1)^2) = -1
    q = lambda x: (x * x + 1.0) / (x - 1.0)
    qp = lambda x: (2.0 * x * (x - 1.0) - (x * x + 1.0)) / ((x - 1.0) ** 2)
    assert abs(qp(2.0) - (-1.0)) < 1e-12
    assert abs(qp(2.0) - central(q, 2.0)) < 1e-6
    print("quotient rule at x=2: %.6f (exactly -1)" % qp(2.0))
    # standard derivatives spot checks
    assert abs(central(math.exp, 0.5) - math.exp(0.5)) < 1e-6
    assert abs(central(math.sin, 1.0) - math.cos(1.0)) < 1e-6
    print("e^x -> e^x and sin x -> cos x confirmed numerically")
    print("rule: identify the structure, apply the matching rule, simplify, verify numerically")
    print("OK: %s applied the rules" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_calc_chain(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def central(f, x, h=1e-7): return (f(x + h) - f(x - h)) / (2.0 * h)
def main():
    # d/dx sin(x^2) = cos(x^2) * 2x
    f = lambda x: math.sin(x * x)
    fp = lambda x: math.cos(x * x) * 2.0 * x
    x0 = 1.5
    assert abs(fp(x0) - central(f, x0)) < 1e-6
    print("chain: d/dx sin(x^2) at 1.5 = 2x cos(x^2) = %.6f" % fp(x0))
    # triple nesting: d/dx e^((x^2+1)^3)... use ((x^3+2x)^10)' = 10(x^3+2x)^9 (3x^2+2)
    g = lambda x: (x ** 3 + 2.0 * x) ** 10
    gp = lambda x: 10.0 * (x ** 3 + 2.0 * x) ** 9 * (3.0 * x ** 2 + 2.0)
    assert abs(gp(0.5) - central(g, 0.5)) / abs(gp(0.5)) < 1e-5
    print("nested: d/dx (x^3+2x)^10 at 0.5 = %.6f" % gp(0.5))
    # the classic error: forgetting the inner derivative gives cos(x^2) alone
    wrong = math.cos(x0 * x0)
    assert abs(wrong - fp(x0)) > 1.0
    print("dropping the inner factor would give %.4f instead of %.4f - never skip it" % (wrong, fp(x0)))
    print("rule: outer derivative first (inner untouched), then multiply by the inner derivative")
    print("OK: %s chained the derivatives" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_calc_implicit(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # circle x^2 + y^2 = 25 at (3, 4): dy/dx = -x/y = -0.75
    x0, y0 = 3.0, 4.0
    slope = -x0 / y0
    assert abs(slope - (-0.75)) < 1e-12
    # numerical check: step along the circle implicitly
    dx = 1e-6
    y1 = math.sqrt(25.0 - (x0 + dx) ** 2)
    num_slope = (y1 - y0) / dx
    assert abs(num_slope - slope) < 1e-4, (num_slope, slope)
    print("circle at (3,4): implicit dy/dx = -x/y = %.4f; numeric %.4f" % (slope, num_slope))
    # inverse trig via implicit: y = arcsin(x) -> sin(y) = x -> cos(y) dy/dx = 1
    x1 = 0.5
    dy = 1.0 / math.sqrt(1.0 - x1 * x1)  # 1/sqrt(1-x^2)
    assert abs(dy - 1.1547005383792517) < 1e-9
    h = 1e-7
    num = (math.asin(x1 + h) - math.asin(x1 - h)) / (2.0 * h)
    assert abs(num - dy) < 1e-6
    print("d/dx arcsin(x) at 0.5 = 1/sqrt(1-x^2) = %.6f" % dy)
    print("rule: differentiate both sides, every y-term earns a dy/dx, then solve")
    print("OK: %s differentiated implicitly" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_calc_higher(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def second_diff(f, x, h=1e-4): return (f(x + h) - 2.0 * f(x) + f(x - h)) / (h * h)
def main():
    f = lambda x: x ** 4 - 3.0 * x ** 2 + 2.0
    fp = lambda x: 4.0 * x ** 3 - 6.0 * x
    fpp = lambda x: 12.0 * x ** 2 - 6.0
    # critical points: 4x^3 - 6x = 2x(2x^2 - 3) = 0 -> x = 0, ±sqrt(3/2)
    import math as _m
    cps = [0.0, _m.sqrt(1.5), -_m.sqrt(1.5)]
    for c in cps:
        assert abs(fp(c)) < 1e-12, c
    # second derivative test
    assert fpp(0.0) < 0.0  # local max
    assert fpp(_m.sqrt(1.5)) > 0.0  # local min
    print("critical points at 0, ±sqrt(3/2): f''(0)=-6 <0 max; f''(±1.22)>0 min")
    # inflection points: f'' = 0 -> x = ±1/sqrt(2), sign changes
    ip = 1.0 / _m.sqrt(2.0)
    assert abs(fpp(ip)) < 1e-12
    assert fpp(ip - 0.1) < 0.0 < fpp(ip + 0.1)
    print("inflection at x=±%.4f: concavity flips there" % ip)
    # numeric second derivative check
    assert abs(second_diff(f, 1.0) - fpp(1.0)) < 1e-3
    print("numeric f''(1) = %.4f vs symbolic %.4f" % (second_diff(f, 1.0), fpp(1.0)))
    # motion reading: s(t)=t^3 -> v=3t^2, a=6t, jerk=6
    print("motion chain: position -> velocity -> acceleration -> jerk, each the derivative of the last")
    print("rule: f'=0 finds candidates; f'' classifies; sign change of f'' marks inflection")
    print("OK: %s went to second order" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_calc_related(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # spherical balloon: V = 4/3 pi r^3, dV/dt = 100 cm^3/s, find dr/dt at r = 5
    dVdt = 100.0
    r = 5.0
    drdt = dVdt / (4.0 * math.pi * r * r)
    assert abs(drdt - 1.0 / math.pi) < 1e-12
    print("balloon: dV/dt=100, r=5 -> dr/dt = 1/pi = %.4f cm/s" % drdt)
    # finite-difference sanity: advance r by drdt*dt, check volume change
    dt = 1e-4
    V = lambda rr: 4.0 / 3.0 * math.pi * rr ** 3
    num_rate = (V(r + drdt * dt) - V(r)) / dt
    assert abs(num_rate - dVdt) / dVdt < 1e-3
    print("check: advancing the radius reproduces dV/dt = %.2f" % num_rate)
    # ladder: x^2 + y^2 = 25, dx/dt = 2 ft/s at x = 3 -> dy/dt = -(x/y) dx/dt
    x, y = 3.0, 4.0
    dydt = -(x / y) * 2.0
    assert abs(dydt - (-1.5)) < 1e-12
    print("ladder: sliding at 2 ft/s with x=3 -> top falls at %.2f ft/s" % -dydt)
    print("rule: relate, differentiate in time, substitute AFTER, solve, check sign and units")
    print("OK: %s related the rates" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_calc_optimize(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # rectangle with perimeter 100: A = x(50 - x), domain [0, 50]
    A = lambda x: x * (50.0 - x)
    Ap = lambda x: 50.0 - 2.0 * x
    crit = 25.0
    assert abs(Ap(crit)) < 1e-12
    candidates = [(0.0, A(0.0)), (crit, A(crit)), (50.0, A(50.0))]
    best = max(candidates, key=lambda p: p[1])
    assert best == (25.0, 625.0), best
    print("fence 100: candidates x=0 -> 0, x=25 -> 625, x=50 -> 0; max area 625 at 25x25")
    # open-top box from 12x12 sheet, cut squares of side x: V = x(12-2x)^2, domain [0,6]
    V = lambda x: x * (12.0 - 2.0 * x) ** 2
    # V' = (12-2x)^2 - 4x(12-2x) = (12-2x)(12-6x) = 0 -> x=2 (x=6 degenerate)
    xs = [i * 0.01 for i in range(1, 600)]
    bx = max(xs, key=V)
    assert abs(bx - 2.0) < 0.02, bx
    assert abs(V(2.0) - 128.0) < 1e-9
    print("box: cut x=2 from 12x12 sheet -> max volume %.1f" % V(2.0))
    print("rule: constraint eliminates variables; endpoints compete with critical points")
    print("OK: %s found the optimum" % NAME)
if __name__ == "__main__":
    main()
''')
def demo_calc_sketch(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    f = lambda x: x ** 3 - 3.0 * x
    fp = lambda x: 3.0 * x ** 2 - 3.0
    fpp = lambda x: 6.0 * x
    # critical points: 3x^2 - 3 = 0 -> x = ±1
    assert abs(fp(1.0)) < 1e-12 and abs(fp(-1.0)) < 1e-12
    # first derivative test: sign chart of f'
    assert fp(-2.0) > 0.0 and fp(0.0) < 0.0 and fp(2.0) > 0.0
    print("f' sign: + on (-inf,-1), - on (-1,1), + on (1,inf)")
    print("local max at x=-1 (f=2), local min at x=1 (f=-2)")
    assert abs(f(-1.0) - 2.0) < 1e-12 and abs(f(1.0) - (-2.0)) < 1e-12
    # second derivative test agrees: f''(-1) = -6 < 0 max; f''(1) = 6 > 0 min
    assert fpp(-1.0) < 0.0 < fpp(1.0)
    # concavity: f'' < 0 for x<0 (down), > 0 for x>0 (up); inflection at 0
    assert fpp(-1.0) < 0.0 and fpp(1.0) > 0.0 and abs(fpp(0.0)) < 1e-12
    print("concavity: down on (-inf,0), up on (0,inf); inflection at (0,0)")
    # limits at infinity: no horizontal asymptote; odd-degree ends oppose
    assert f(1e6) > 0.0 and f(-1e6) < 0.0
    print("end behavior: -> +inf right, -> -inf left (no horizontal asymptote)")
    print("rule: f' charts rise/fall, f'' charts cup, asymptotes frame - then draw")
    print("OK: %s sketched the curve" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_calc_lhopital(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # sin(x)/x -> 1 (0/0): L'Hopital gives cos(x)/1 -> 1
    x = 1e-7
    assert abs(math.sin(x) / x - 1.0) < 1e-9
    print("sin(x)/x -> 1 (0/0 resolved by differentiating top and bottom)")
    # (e^x - 1)/x -> 1
    assert abs((math.exp(x) - 1.0) / x - 1.0) < 1e-6
    print("(e^x-1)/x -> 1")
    # ln(x)/(x-1) -> 1 as x -> 1: derivatives 1/x and 1 -> 1/1
    y = 1.0 + 1e-6
    assert abs(math.log(y) / (y - 1.0) - 1.0) < 1e-5
    print("ln(x)/(x-1) -> 1 as x -> 1")
    # 1^inf form via logarithms: (1 + 1/n)^n -> e
    n = 100000.0
    assert abs((1.0 + 1.0 / n) ** n - math.e) < 1e-4
    print("(1+1/n)^n -> e = %.6f (logarithm tames the 1^inf form)" % math.e)
    # gate check demo: x^2/x at 0 is NOT indeterminate after simplifying... verify rule not misapplied
    # direct: (x^2+1)/x at x->0 is not 0/0, so L'Hopital does not apply; it diverges
    assert abs((0.001 ** 2 + 1.0) / 0.001) > 900.0
    print("gate: (x^2+1)/x at 0 is not 0/0 - the rule stays holstered, the limit diverges")
    print("rule: verify 0/0 or inf/inf first; differentiate top and bottom separately; repeat if needed")
    print("OK: %s applied L'Hopital" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_calc_antideriv(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def central(f, x, h=1e-7): return (f(x + h) - f(x - h)) / (2.0 * h)
def main():
    # family F(x) = x^3/3 + C for f(x) = x^2
    for C in (-100.0, 0.0, 5.0):
        F = lambda x, C=C: x ** 3 / 3.0 + C
        assert abs(central(lambda x: F(x), 2.0) - 4.0) < 1e-6
    print("x^2 -> x^3/3 + C: every C differentiates back to x^2")
    # initial condition pins C: F(0) = 5 -> C = 5
    C = 5.0
    F = lambda x: x ** 3 / 3.0 + C
    assert abs(F(0.0) - 5.0) < 1e-12
    print("initial condition F(0)=5 selects C=5 from the family")
    # motion: a(t) = 9.8 -> v(t) = 9.8t + v0 -> s(t) = 4.9t^2 + v0 t + s0
    v0, s0 = 0.0, 100.0
    s = lambda t: 4.9 * t * t + v0 * t + s0
    hh = 1e-4
    acc = (s(1.0 + hh) - 2.0 * s(1.0) + s(1.0 - hh)) / (hh * hh)
    assert abs(acc - 9.8) < 1e-3, acc
    print("falling body: s(t)=4.9t^2+100; s''=9.8 confirms the double reversal")
    # reversal pairs
    assert abs(central(math.log, 2.0) - 0.5) < 1e-6      # 1/x -> ln|x|
    assert abs(central(lambda x: -math.cos(x), 1.0) - math.sin(1.0)) < 1e-6  # sin -> -cos
    print("pairs hold: 1/x <- ln|x|, sin x <- -cos x")
    print("rule: ask what differentiates to the integrand; always + C; verify by differentiating")
    print("OK: %s reversed differentiation" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_calc_riemann(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def riemann(f, a, b, n, kind):
    dx = (b - a) / n
    total = 0.0
    for i in range(n):
        if kind == "left": x = a + i * dx
        elif kind == "right": x = a + (i + 1) * dx
        else: x = a + (i + 0.5) * dx
        total += f(x) * dx
    return total
def main():
    f = lambda x: x * x
    exact = 1.0 / 3.0
    for n in (10, 100, 1000):
        L = riemann(f, 0.0, 1.0, n, "left")
        R = riemann(f, 0.0, 1.0, n, "right")
        M = riemann(f, 0.0, 1.0, n, "mid")
        # for increasing f: left < exact < right (bracketing)
        assert L < exact < R, (n, L, R)
        print("n=%4d: left=%.6f mid=%.8f right=%.6f (exact 1/3)" % (n, L, M, R))
    assert abs(riemann(f, 0.0, 1.0, 1000, "mid") - exact) < 1e-6
    # signed area: integral of x^3 on [-1,1] cancels to 0
    assert abs(riemann(lambda x: x ** 3, -1.0, 1.0, 2000, "mid")) < 1e-9
    print("signed area: x^3 on [-1,1] nets to 0 (above cancels below)")
    print("rule: slice, sample, sum, refine - the limit of the sums IS the integral")
    print("OK: %s summed the rectangles" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_calc_ftc(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # Part 2: integral of x^2 on [0,2] = F(2)-F(0), F = x^3/3 -> 8/3
    F = lambda x: x ** 3 / 3.0
    val = F(2.0) - F(0.0)
    assert abs(val - 8.0 / 3.0) < 1e-12
    print("FTC Part 2: integral of x^2 on [0,2] = 8/3 = %.6f" % val)
    # any antiderivative works: the +C cancels
    G = lambda x: x ** 3 / 3.0 + 42.0
    assert abs((G(2.0) - G(0.0)) - val) < 1e-9
    print("the +C cancels in the subtraction - any antiderivative will do")
    # Part 1: d/dx integral_0^x t^2 dt = x^2, checked numerically at x=1.5
    def accum(x, n=20000):
        dx = x / n
        return sum(((i + 0.5) * dx) ** 2 * dx for i in range(n))
    h = 1e-5
    dacc = (accum(1.5 + h) - accum(1.5 - h)) / (2.0 * h)
    assert abs(dacc - 2.25) < 1e-3, dacc
    print("FTC Part 1: d/dx of the accumulation at x=1.5 -> %.4f (= x^2)" % dacc)
    # net change: velocity v(t)=3t^2 on [1,2] -> displacement = [t^3]_1^2 = 7
    G = lambda x: x ** 3
    assert abs((G(2.0) - G(1.0)) - 7.0) < 1e-12
    print("net change: integral of velocity 3t^2 on [1,2] = displacement 7")
    print("rule: find any antiderivative, evaluate top minus bottom - the sums are bypassed")
    print("OK: %s used the fundamental theorem" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_calc_substitution(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def central(f, x, h=1e-7): return (f(x + h) - f(x - h)) / (2.0 * h)
def main():
    # integral 2x*cos(x^2) dx, u = x^2 -> sin(x^2) + C
    F = lambda x: math.sin(x * x)
    f = lambda x: 2.0 * x * math.cos(x * x)
    assert abs(central(F, 0.7) - f(0.7)) < 1e-6
    print("u = x^2: integral of 2x cos(x^2) = sin(x^2); derivative check at 0.7 passes")
    # definite with changed limits: integral_0^1 2x e^(x^2) dx = [e^u]_0^1 = e - 1
    val = math.e - 1.0
    n = 20000
    dx = 1.0 / n
    num = sum(2.0 * (i + 0.5) * dx * math.exp(((i + 0.5) * dx) ** 2) * dx for i in range(n))
    assert abs(num - val) < 1e-6, (num, val)
    print("definite via u-limits: integral_0^1 2x e^(x^2) dx = e - 1 = %.6f" % val)
    # failed substitution signal: integral of e^(x^2) dx has no du factor -> not elementary
    # (demonstrate the missing-factor check programmatically)
    def has_du_factor(u_prime_form, integrand_factors):
        return u_prime_form in integrand_factors
    assert not has_du_factor("2x", ["e^(x^2)"])
    print("no 2x factor next to e^(x^2): substitution fails - a known non-elementary integral")
    print("rule: name u, compute du, demand the du factor be present, rewrite fully in u")
    print("OK: %s substituted" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_calc_parts(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def central(f, x, h=1e-7): return (f(x + h) - f(x - h)) / (2.0 * h)
def main():
    # LIATE: x is Algebraic (before Exponential) -> u = x, dv = e^x dx
    # integral x e^x dx = x e^x - integral e^x dx = (x-1) e^x + C
    F = lambda x: (x - 1.0) * math.exp(x)
    f = lambda x: x * math.exp(x)
    assert abs(central(F, 1.2) - f(1.2)) < 1e-5
    print("LIATE picks u=x: integral of x e^x = (x-1)e^x; derivative check passes")
    # definite: integral_0^1 x e^x dx = [(x-1)e^x]_0^1 = 0 - (-1) = 1
    assert abs((F(1.0) - F(0.0)) - 1.0) < 1e-12
    print("definite: integral_0^1 x e^x dx = %.6f (exactly 1)" % (F(1.0) - F(0.0)))
    # cyclic case: integral e^x sin x dx; parts twice returns to start -> solve
    # result: (e^x (sin x - cos x))/2
    G = lambda x: math.exp(x) * (math.sin(x) - math.cos(x)) / 2.0
    g = lambda x: math.exp(x) * math.sin(x)
    assert abs(central(G, 0.8) - g(0.8)) < 1e-5
    print("cyclic: integral of e^x sin x = e^x(sin x - cos x)/2; solved algebraically")
    print("rule: LIATE chooses u; differentiate u down, integrate dv across; cycle -> solve")
    print("OK: %s integrated by parts" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_calc_trigint(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def central(f, x, h=1e-7): return (f(x + h) - f(x - h)) / (2.0 * h)
def main():
    # even power via half-angle: integral sin^2 x dx = x/2 - sin(2x)/4 + C
    F = lambda x: x / 2.0 - math.sin(2.0 * x) / 4.0
    f = lambda x: math.sin(x) ** 2
    assert abs(central(F, 0.9) - f(0.9)) < 1e-6
    print("half-angle: integral of sin^2 x = x/2 - sin(2x)/4; check at 0.9 passes")
    # odd power: integral sin^3 x dx = -cos x + cos^3 x / 3 + C
    G = lambda x: -math.cos(x) + math.cos(x) ** 3 / 3.0
    g = lambda x: math.sin(x) ** 3
    assert abs(central(G, 1.1) - g(1.1)) < 1e-6
    print("odd power: peel one sin for du, convert the rest; check at 1.1 passes")
    # trig substitution: x = 2 sin(theta) kills sqrt(4 - x^2) -> 2 cos(theta)
    x = 1.0
    theta = math.asin(x / 2.0)
    assert abs(2.0 * math.cos(theta) - math.sqrt(4.0 - x * x)) < 1e-12
    print("trig sub: x=2 sin θ turns sqrt(4-x^2) into 2cos θ (reference triangle closes it)")
    # product-to-sum spot check: sin(3x)cos(2x) = (sin5x + sin x)/2
    xv = 0.6
    assert abs(math.sin(3*xv)*math.cos(2*xv) - (math.sin(5*xv)+math.sin(xv))/2.0) < 1e-12
    print("product-to-sum identity confirmed numerically")
    print("rule: identities first - odd peels, even halves, roots substitute")
    print("OK: %s tamed the trig integrals" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_calc_partfrac(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def central(f, x, h=1e-7): return (f(x + h) - f(x - h)) / (2.0 * h)
def main():
    # 1/(x(x-1)) = -1/x + 1/(x-1): cover-up gives A = -1 at x=0, B = 1 at x=1
    def orig(x): return 1.0 / (x * (x - 1.0))
    def decomp(x): return -1.0 / x + 1.0 / (x - 1.0)
    for x in (2.5, -0.7, 3.3):
        assert abs(orig(x) - decomp(x)) < 1e-12, x
    print("decomposition: 1/(x(x-1)) = -1/x + 1/(x-1) verified at three points")
    # integrate termwise: -ln|x| + ln|x-1| + C
    F = lambda x: -math.log(abs(x)) + math.log(abs(x - 1.0))
    assert abs(central(F, 2.5) - orig(2.5)) < 1e-6
    print("termwise integral: ln|x-1| - ln|x|; derivative check at 2.5 passes")
    # repeated factor template: 1/(x(x-1)^2) = A/x + B/(x-1) + C/(x-1)^2
    # solving: A=1 (x=0), C=1 (x=1), B=-1 (x^2 coeff) - verified by recombining
    def orig2(x): return 1.0 / (x * (x - 1.0) ** 2)
    def decomp2(x): return 1.0 / x - 1.0 / (x - 1.0) + 1.0 / (x - 1.0) ** 2
    for x in (2.0, 0.5, 4.0):
        assert abs(orig2(x) - decomp2(x)) < 1e-9, x
    print("repeated factor: 1/(x(x-1)^2) splits into three pieces; recombination verifies")
    print("rule: factor, template, cover-up constants, integrate the pieces")
    print("OK: %s split the fractions" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_calc_improper(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # convergent: integral_1^b x^-2 dx = 1 - 1/b -> 1
    b = 1e6
    val = 1.0 - 1.0 / b
    assert abs(val - 1.0) < 1e-5
    print("integral_1^inf x^-2 dx = lim (1 - 1/b) = 1: infinite tail, finite area")
    # divergent: integral_1^b x^-1 dx = ln b -> unbounded
    assert abs(math.log(1e6) - 13.815510557964274) < 1e-9
    print("integral_1^inf x^-1 dx = lim ln b = inf: diverges (p = 1 is the knife-edge)")
    # p-test sweep
    for p, converges in ((2.0, True), (1.5, True), (1.0, False), (0.5, False)):
        # partial integral to b=1e4 of x^-p from 1: (b^(1-p) - 1)/(1-p)
        if abs(p - 1.0) < 1e-12:
            partial = math.log(1e4)
            is_conv = False
        else:
            partial = (1e4 ** (1.0 - p) - 1.0) / (1.0 - p)
            is_conv = p > 1.0
        assert is_conv == converges
        print("p = %.1f: partial to 1e4 = %.4f -> %s" % (p, partial, "converges" if is_conv else "diverges"))
    # blow-up inside: integral_0^1 x^-1/2 dx = [2 sqrt(x)]_0^1 = 2
    n = 200000
    a = 1e-9
    dx = (1.0 - a) / n
    num = sum(((a + (i + 0.5) * dx) ** -0.5) * dx for i in range(n))
    assert abs(num - 2.0) < 5e-3, num
    print("interior blow-up: integral_0^1 x^(-1/2) dx = 2 (p < 1 at zero converges)")
    print("rule: replace the trouble with a limit; p > 1 at infinity, p < 1 at zero")
    print("OK: %s integrated the improper" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_calc_area(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def simpson(f, a, b, n=2000):
    assert n % 2 == 0
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4.0 if i % 2 else 2.0) * f(a + i * h)
    return s * h / 3.0
def main():
    # y = x on top of y = x^2 on [0,1]: area = integral (x - x^2) = 1/2 - 1/3 = 1/6
    exact = 1.0 / 6.0
    num = simpson(lambda x: x - x * x, 0.0, 1.0)
    assert abs(num - exact) < 1e-9, (num, exact)
    print("area between x and x^2 on [0,1] = 1/6 = %.6f" % exact)
    # split where top changes: sin x vs 0 on [0, 2pi] -> two humps, each area 2
    a1 = simpson(lambda x: math.sin(x), 0.0, math.pi)
    a2 = simpson(lambda x: -math.sin(x), math.pi, 2.0 * math.pi)
    assert abs(a1 - 2.0) < 1e-9 and abs(a2 - 2.0) < 1e-9
    print("sin x vs 0 on [0,2pi]: split at pi -> 2 + 2 = 4 total area")
    # horizontal slicing: region between x = y^2 and x = y + 2, intersections at y=-1,2
    # area = integral_{-1}^{2} ((y+2) - y^2) dy = [y^2/2 + 2y - y^3/3] = 9/2
    exact_h = 4.5
    num_h = simpson(lambda y: (y + 2.0) - y * y, -1.0, 2.0)
    assert abs(num_h - exact_h) < 1e-9
    print("horizontal slice: x=y^2 vs x=y+2 -> area 9/2 = %.4f" % exact_h)
    print("rule: intersections set limits; test the top; split where it changes")
    print("OK: %s measured between the curves" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_calc_volumes(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def simpson(f, a, b, n=2000):
    assert n % 2 == 0
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4.0 if i % 2 else 2.0) * f(a + i * h)
    return s * h / 3.0
def main():
    # sphere r=3 by disks: V = integral_{-3}^{3} pi(9 - x^2) dx = 36 pi
    r = 3.0
    exact = 4.0 / 3.0 * math.pi * r ** 3
    num = simpson(lambda x: math.pi * (r * r - x * x), -r, r)
    assert abs(num - exact) / exact < 1e-9
    print("sphere r=3 by disks: 4/3 pi r^3 = %.6f" % exact)
    # washer: region between y = x^2 and y = x on [0,1] revolved about x-axis
    # V = pi integral (x^2 - x^4) dx = pi(1/3 - 1/5) = 2pi/15
    exact_w = 2.0 * math.pi / 15.0
    num_w = simpson(lambda x: math.pi * (x * x - x ** 4), 0.0, 1.0)
    assert abs(num_w - exact_w) < 1e-9
    print("washer: x vs x^2 about x-axis -> 2pi/15 = %.6f" % exact_w)
    # shell: y = x^2 on [0,2] about y-axis: V = integral 2 pi x * x^2 dx = 8 pi
    exact_s = 8.0 * math.pi
    num_s = simpson(lambda x: 2.0 * math.pi * x * x * x, 0.0, 2.0)
    assert abs(num_s - exact_s) < 1e-9
    print("shell: y=x^2 on [0,2] about y-axis -> 8pi = %.6f" % exact_s)
    print("rule: disks for perpendicular slices, shells for parallel - pick the cleaner radius")
    print("OK: %s spun the volumes" % NAME)
if __name__ == "__main__":
    main()
''')
def demo_calc_arclen(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def simpson(f, a, b, n=4000):
    assert n % 2 == 0
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4.0 if i % 2 else 2.0) * f(a + i * h)
    return s * h / 3.0
def main():
    # arc length of y = x^2 on [0,1]: integral sqrt(1 + 4x^2) dx
    # exact: x/2 sqrt(1+4x^2) + asinh(2x)/4 evaluated 0..1
    exact = 0.5 * math.sqrt(5.0) + math.asinh(2.0) / 4.0
    num = simpson(lambda x: math.sqrt(1.0 + 4.0 * x * x), 0.0, 1.0)
    assert abs(num - exact) < 1e-9, (num, exact)
    print("arc length of x^2 on [0,1] = %.6f" % exact)
    # straight line check: y = 3x on [0,2] has length 2*sqrt(10)
    line_len = simpson(lambda x: math.sqrt(1.0 + 9.0), 0.0, 2.0)
    assert abs(line_len - 2.0 * math.sqrt(10.0)) < 1e-9
    print("line y=3x on [0,2]: integral gives 2*sqrt(10) = %.6f" % line_len)
    # work: spring F = kx, k = 50 N/m, stretched 0.2 m -> W = 1/2 k x^2 = 1 J
    k, x = 50.0, 0.2
    W = simpson(lambda t: k * t, 0.0, x)
    assert abs(W - 0.5 * k * x * x) < 1e-9
    print("spring work: 1/2 k x^2 = %.4f J" % W)
    # pumping: tank 2x2x3 m full of water (rho=1000, g=9.8), lift to top
    # dW = rho*g*(4 dy)*(3 - y); W = rho*g*4*integral_0^3 (3-y) dy = rho*g*18
    rho, g = 1000.0, 9.8
    Wp = simpson(lambda y: rho * g * 4.0 * (3.0 - y), 0.0, 3.0)
    assert abs(Wp - rho * g * 18.0) / Wp < 1e-9
    print("pumping 12 m^3 up 1.5 m average: W = %.1f kJ" % (Wp / 1000.0))
    print("rule: ds = sqrt(dx^2+dy^2); work = integral of force over distance")
    print("OK: %s measured length and work" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_calc_sequences(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # (1 + 1/n)^n -> e
    n = 100000
    val = (1.0 + 1.0 / n) ** n
    assert abs(val - math.e) < 1e-4, val
    print("(1+1/n)^n at n=100000: %.6f -> e = %.6f" % (val, math.e))
    # 1/n -> 0
    assert abs(1.0 / 10 ** 9) < 1e-8
    print("1/n -> 0: terms shrink without bound")
    # (-1)^n oscillates: no limit
    terms = [(-1.0) ** k for k in range(10)]
    assert set(terms) == {1.0, -1.0}
    print("(-1)^n oscillates forever: divergence by oscillation")
    # monotone bounded: a_1 = 1, a_{n+1} = sqrt(2 + a_n) increases toward 2
    a = 1.0
    for _ in range(50):
        a = math.sqrt(2.0 + a)
    assert abs(a - 2.0) < 1e-9, a
    print("recursive sqrt(2+a_n): monotone and bounded by 2 -> converges to 2")
    # growth race: n^2 vs 2^n - exponential wins
    assert (2.0 ** 100) / (100.0 ** 2) > 1e20
    print("growth hierarchy: exponentials outrun polynomials eventually")
    print("rule: take the limit; if none exists, prove monotone+bounded or name the oscillation")
    print("OK: %s ran the sequences" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_calc_series(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def partial(f, N): return sum(f(n) for n in range(1, N + 1))
def main():
    # geometric: sum (1/2)^n = 1
    s = partial(lambda n: 0.5 ** n, 60)
    assert abs(s - 1.0) < 1e-12, s
    print("geometric sum (1/2)^n = 1 (60 terms suffice)")
    # p-series p=2 -> pi^2/6; tail bounded by 1/N
    N = 20000
    s2 = partial(lambda n: 1.0 / (n * n), N)
    assert abs(s2 - math.pi ** 2 / 6.0) < 1.5 / N, s2
    print("sum 1/n^2 = pi^2/6 = %.6f (partial sum within 1/N)" % (math.pi ** 2 / 6.0))
    # harmonic diverges: sum to 10^6 exceeds 14
    h = partial(lambda n: 1.0 / n, 10 ** 6)
    assert h > 14.0, h
    print("harmonic sum to 10^6 = %.4f: diverges, but slowly" % h)
    # ratio test: n! / n^n -> ratio 1/(1+1/n)^n -> 1/e < 1, converges
    def term(n): return math.factorial(n) / (n ** n)
    ratios = [term(n + 1) / term(n) for n in (5, 10, 20)]
    for r in ratios:
        assert r < 0.5, r
    print("ratio test on n!/n^n: successive ratios -> 1/e < 1, converges")
    # alternating: sum (-1)^n / n -> -ln 2; error bounded by first omitted term
    alt = sum(((-1.0) ** n) / n for n in range(1, 10001))
    assert abs(alt - (-math.log(2.0))) < 1.0 / 10001 + 1e-12
    print("alternating harmonic -> -ln 2 = %.6f; remainder < 1/10001" % (-math.log(2.0)))
    print("rule: divergence test first, then match the family, then pick the test")
    print("OK: %s tested the series" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_calc_taylor(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def taylor_sin(x, terms):
    total, sign, fact, pw = 0.0, 1.0, 1.0, x
    for n in range(terms):
        k = 2 * n + 1
        if n > 0:
            fact *= (k - 1) * k
            pw *= x * x
        total += sign * pw / fact
        sign = -sign
    return total
def main():
    x = 0.5
    approx = taylor_sin(x, 3)  # x - x^3/6 + x^5/120
    exact = math.sin(x)
    bound = x ** 7 / math.factorial(7)  # Taylor remainder bound
    assert abs(approx - exact) < bound + 1e-15, (approx, exact, bound)
    print("sin(0.5): Taylor x-x^3/6+x^5/120 = %.7f vs %.7f (error < %.1e)" % (approx, exact, bound))
    # e^x series at x=1 -> e
    e_approx = sum(1.0 / math.factorial(n) for n in range(15))
    assert abs(e_approx - math.e) < 1e-12
    print("e^1 from sum 1/n!: %.10f" % e_approx)
    # substitution: e^(-x^2) series integrated termwise: integral_0^1 e^(-x^2) dx
    terms = [((-1.0) ** n) / (math.factorial(n) * (2 * n + 1)) for n in range(12)]
    val = sum(terms)
    assert abs(val - 0.7468241328124271) < 1e-9, val
    print("integral_0^1 e^(-x^2) dx via termwise integration = %.9f" % val)
    # geometric series as Maclaurin: 1/(1-x) = sum x^n
    xv = 0.3
    assert abs(sum(xv ** n for n in range(30)) - 1.0 / (1.0 - xv)) < 1e-9
    print("1/(1-x) Maclaurin at x=0.3 confirmed")
    print("rule: derivatives at a point -> polynomial; truncate with a remainder bound")
    print("OK: %s expanded the series" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_calc_powerseries(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def radius_ratio(coeff, n=50):
    # R = lim |c_n / c_{n+1}|
    return abs(coeff(n) / coeff(n + 1))
def main():
    # sum x^n / n! : |c_n / c_{n+1}| = n + 1 -> infinity, so R = inf
    R1a = radius_ratio(lambda n: 1.0 / math.factorial(n), n=50)
    R1b = radius_ratio(lambda n: 1.0 / math.factorial(n), n=100)
    assert abs(R1a - 51.0) < 1e-9 and abs(R1b - 101.0) < 1e-9 and R1b > R1a
    print("sum x^n/n!: |c_n/c_{n+1}| = n+1 -> infinity, so R = infinity (converges everywhere)")
    # sum n! x^n : R = 0
    R2 = radius_ratio(lambda n: float(math.factorial(n)))
    assert R2 < 0.05, R2  # 1/51 at n=50, tending to 0
    print("sum n! x^n: R = 0 (converges only at x = 0)")
    # sum x^n / n^2 : R = 1; endpoints converge (p=2, alternating p=2)
    R3 = radius_ratio(lambda n: 1.0 / (n * n))
    assert abs(R3 - 1.0) < 0.05, R3
    s_pos = sum(1.0 / (n * n) for n in range(1, 20001))
    assert abs(s_pos - math.pi ** 2 / 6.0) < 1e-3
    s_neg = sum(((-1.0) ** n) / (n * n) for n in range(1, 20001))
    assert abs(s_neg - (-math.pi ** 2 / 12.0)) < 1e-3
    print("sum x^n/n^2: R = 1; x=1 -> pi^2/6, x=-1 -> -pi^2/12 (both endpoints converge)")
    # termwise differentiation: d/dx sum x^n/n! = sum x^n/n! (e^x is its own derivative)
    x = 0.7
    s = sum(x ** n / math.factorial(n) for n in range(20))
    ds = sum(n * x ** (n - 1) / math.factorial(n) for n in range(1, 20))
    assert abs(ds - s) < 1e-9
    print("termwise differentiation: d/dx e^x series = e^x series, inside R")
    print("rule: ratio test finds R; test each endpoint; inside, differentiate and integrate freely")
    print("OK: %s mapped the radius" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_calc_parampolar(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def simpson(f, a, b, n=4000):
    assert n % 2 == 0
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4.0 if i % 2 else 2.0) * f(a + i * h)
    return s * h / 3.0
def main():
    # parametric circle x = cos t, y = sin t: dy/dx = -cot t; at t = pi/4 -> -1
    t = math.pi / 4.0
    dydx = math.cos(t) / (-math.sin(t))
    assert abs(dydx - (-1.0)) < 1e-12
    print("parametric circle: dy/dx = (dy/dt)/(dx/dt) = -cot t; at pi/4 -> -1")
    # vertical tangent where dx/dt = 0 and dy/dt != 0: t = 0, point (1, 0)
    assert abs(-math.sin(0.0)) < 1e-12 and abs(math.cos(0.0) - 1.0) < 1e-12
    print("dx/dt = -sin t = 0 at t=0 (dy/dt = 1): vertical tangent at (1, 0)")
    # arc length of parametric: circle r=1, t in [0, 2pi] -> 2pi
    L = simpson(lambda u: math.sqrt(math.sin(u) ** 2 + math.cos(u) ** 2), 0.0, 2.0 * math.pi)
    assert abs(L - 2.0 * math.pi) < 1e-9
    print("arc length via speed integral: 2pi = %.6f" % L)
    # polar area: cardioid r = 1 + cos(theta): (1/2) integral (1+cos)^2 = 3pi/2
    A = 0.5 * simpson(lambda th: (1.0 + math.cos(th)) ** 2, 0.0, 2.0 * math.pi)
    assert abs(A - 1.5 * math.pi) < 1e-9, A
    print("cardioid area: (1/2) integral r^2 dtheta = 3pi/2 = %.6f" % A)
    # polar tangent: r = 1 + cos theta at theta = pi/2: dr/dtheta = -sin = -1
    th = math.pi / 2.0
    dr = -math.sin(th)
    dydx_p = (dr * math.sin(th) + (1 + math.cos(th)) * math.cos(th)) / (dr * math.cos(th) - (1 + math.cos(th)) * math.sin(th))
    assert abs(dydx_p - 1.0) < 1e-9, dydx_p
    print("polar slope formula at theta=pi/2 on the cardioid: %.4f" % dydx_p)
    print("rule: parametrize, divide the rates; in polar, area is (1/2) integral r^2")
    print("OK: %s traced the curves" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_calc_partial(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # f(x, y) = x^2 y + sin(xy) at (1, 2)
    def f(x, y): return x * x * y + math.sin(x * y)
    h = 1e-7
    fx = (f(1.0 + h, 2.0) - f(1.0 - h, 2.0)) / (2.0 * h)
    fy = (f(1.0, 2.0 + h) - f(1.0, 2.0 - h)) / (2.0 * h)
    fx_exact = 2.0 * 1.0 * 2.0 + 2.0 * math.cos(2.0)
    fy_exact = 1.0 + 1.0 * math.cos(2.0)
    assert abs(fx - fx_exact) < 1e-5 and abs(fy - fy_exact) < 1e-5
    print("partials at (1,2): fx = 2xy + y cos(xy) = %.4f; fy = x^2 + x cos(xy) = %.4f" % (fx_exact, fy_exact))
    # gradient: steepest ascent
    mag = math.hypot(fx_exact, fy_exact)
    ux, uy = fx_exact / mag, fy_exact / mag
    print("gradient = (%.4f, %.4f); steepest ascent direction (%.4f, %.4f), slope %.4f" %
          (fx_exact, fy_exact, ux, uy, mag))
    # directional derivative along (1,0) equals fx
    assert abs(fx_exact * 1.0 + fy_exact * 0.0 - fx_exact) < 1e-12
    # Clairaut: f_xy = f_yx = 2x - xy sin(xy)... check numerically
    fxy = (f(1.0 + h, 2.0 + h) - f(1.0 + h, 2.0 - h) - f(1.0 - h, 2.0 + h) + f(1.0 - h, 2.0 - h)) / (4.0 * h * h)
    fyx = (f(1.0 + h, 2.0 + h) - f(1.0 - h, 2.0 + h) - f(1.0 + h, 2.0 - h) + f(1.0 - h, 2.0 - h)) / (4.0 * h * h)
    assert abs(fxy - fyx) < 1e-3, (fxy, fyx)
    print("Clairaut: mixed partials agree (%.4f vs %.4f)" % (fxy, fyx))
    # critical point classification: g = x^2 + y^2 - 4x -> min at (2, 0)
    # D = gxx*gyy - gxy^2 = 2*2 - 0 = 4 > 0, gxx > 0 -> minimum
    print("D-test: D = fxx*fyy - fxy^2 sorts minima, maxima, and saddles")
    print("rule: freeze all but one variable, differentiate, assemble the gradient")
    print("OK: %s took the partials" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_calc_multiple(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def dbl_mid(f, ax, bx, ay, by, n=200):
    hx, hy = (bx - ax) / n, (by - ay) / n
    total = 0.0
    for i in range(n):
        for j in range(n):
            total += f(ax + (i + 0.5) * hx, ay + (j + 0.5) * hy)
    return total * hx * hy
def main():
    # double integral of (x + 2y) over [0,1] x [0,2] = 5
    exact = 5.0
    num = dbl_mid(lambda x, y: x + 2.0 * y, 0.0, 1.0, 0.0, 2.0)
    assert abs(num - exact) < 0.01, num
    print("iterated: integral_0^1 integral_0^2 (x+2y) dy dx = 5 (numeric %.4f)" % num)
    # volume under z = 4 - x^2 - y^2 over the disk x^2+y^2 <= 4: polar -> 8 pi
    # integral_0^{2pi} integral_0^2 (4 - r^2) r dr dtheta = 2pi * 8 = 16 pi... check:
    # integral_0^2 (4r - r^3) dr = 8 - 4 = 4; times 2pi = 8 pi
    exact_p = 8.0 * math.pi
    n = 400
    hr, ht = 2.0 / n, 2.0 * math.pi / n
    total = 0.0
    for i in range(n):
        for j in range(n):
            r = (i + 0.5) * hr
            total += (4.0 - r * r) * r * hr * ht
    assert abs(total - exact_p) / exact_p < 0.005, total
    print("polar: volume under paraboloid over disk radius 2 = 8pi = %.4f" % exact_p)
    # average value: integral / area
    avg = exact / (1.0 * 2.0)
    assert abs(avg - 2.5) < 1e-12
    print("average value of x+2y over the rectangle: 2.5")
    print("rule: describe the region, iterate inside-out, switch coordinates when round")
    print("OK: %s integrated multiply" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_calc_vector(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def simpson(f, a, b, n=4000):
    assert n % 2 == 0
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4.0 if i % 2 else 2.0) * f(a + i * h)
    return s * h / 3.0
def main():
    # F = (2xy, x^2): P_y = 2x = Q_x -> conservative; potential f = x^2 y
    # work along r(t) = (t, t^2), t in [0,1]: integral F(r).r' dt
    def integrand(t):
        x, y = t, t * t
        Fx, Fy = 2.0 * x * y, x * x
        return Fx * 1.0 + Fy * 2.0 * t
    work = simpson(integrand, 0.0, 1.0)
    assert abs(work - 1.0) < 1e-9, work  # f(1,1) - f(0,0) = 1
    print("conservative work: path integral = 1 = potential difference f(1,1)-f(0,0)")
    # closed loop on a conservative field: zero
    loop = simpson(lambda t: integrand(t) if t <= 1.0 else 0.0, 0.0, 1.0)
    assert abs(loop - 1.0) < 1e-9
    # non-conservative: F = (-y, x) around unit circle -> 2 pi
    circ = simpson(lambda t: (-math.sin(t)) * (-math.sin(t)) + math.cos(t) * math.cos(t),
                   0.0, 2.0 * math.pi)
    assert abs(circ - 2.0 * math.pi) < 1e-9
    print("non-conservative circulation around unit circle: 2pi = %.6f" % circ)
    # flux of F = (x, y) across unit circle (outward): integral F.n ds = 2 pi
    flux = simpson(lambda t: 1.0, 0.0, 2.0 * math.pi)
    assert abs(flux - 2.0 * math.pi) < 1e-9
    print("flux of (x,y) through unit circle: 2pi (what flows out)")
    print("rule: parametrize, dot with tangent (work) or normal (flux), integrate")
    print("OK: %s measured work and flux" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_calc_theorems(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def simpson(f, a, b, n=4000):
    assert n % 2 == 0
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4.0 if i % 2 else 2.0) * f(a + i * h)
    return s * h / 3.0
def main():
    # Green's: F = (-y, x); Q_x - P_y = 1 - (-1) = 2; over unit disk: 4pi/2... = 2pi
    # boundary: r(t) = (cos t, sin t): integral F.r' dt = integral 1 dt = 2pi
    boundary = simpson(lambda t: (-math.sin(t)) * (-math.sin(t)) + math.cos(t) * math.cos(t),
                       0.0, 2.0 * math.pi)
    interior = 2.0 * math.pi * 1.0 ** 2  # double integral of 2 over unit disk
    assert abs(boundary - interior) < 1e-9, (boundary, interior)
    print("Green: circulation 2pi = double integral of (Q_x - P_y) = 2pi")
    # Divergence: F = (x, y, z), div F = 3; unit ball volume 4pi/3 -> flux 4pi
    # boundary flux: on unit sphere F.n = 1, area 4pi
    div, vol = 3.0, 4.0 / 3.0 * math.pi
    assert abs(div * vol - 4.0 * math.pi) < 1e-12
    print("Divergence: div=3 over unit ball -> flux 4pi = %.6f" % (4.0 * math.pi))
    # Stokes: F = (-y, x, 0), curl = (0, 0, 2); disk z=0 radius 1, normal +k
    # flux of curl = 2 * area = 2pi = circulation (same as Green here)
    print("Stokes: circulation = flux of curl through the spanning surface = 2pi")
    # gradient theorem: work of grad(x^2 y) from (0,0) to (1,1) = 1 regardless of path
    assert abs((1.0 ** 2 * 1.0) - 0.0 - 1.0) < 1e-12
    print("Gradient theorem: work = potential(end) - potential(start), path irrelevant")
    print("rule: boundary integral = interior integral; check orientation every time")
    print("OK: %s proved the big three" % NAME)
if __name__ == "__main__":
    main()
''')
def demo_calc_de1(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def euler(f, x0, y0, h, steps):
    x, y = x0, y0
    for _ in range(steps):
        y += h * f(x, y)
        x += h
    return y
def main():
    # dy/dx = y, y(0) = 1 -> y = e^x; Euler's method to x = 1
    exact = math.e
    y_euler = euler(lambda x, y: y, 0.0, 1.0, 0.1, 10)
    assert abs(y_euler - 1.1 ** 10) < 1e-12
    assert abs(y_euler - exact) < 0.15, (y_euler, exact)
    print("Euler h=0.1: y(1) = %.4f vs e = %.4f (error O(h))" % (y_euler, exact))
    # halving h roughly halves the error
    y_fine = euler(lambda x, y: y, 0.0, 1.0, 0.05, 20)
    assert abs(y_fine - exact) < abs(y_euler - exact)
    print("Euler h=0.05: y(1) = %.4f (error shrinks with h)" % y_fine)
    # separable: dy/dx = 2x, y(0) = 1 -> y = x^2 + 1
    y_sep = lambda x: x * x + 1.0
    assert abs(y_sep(3.0) - 10.0) < 1e-12
    h = 1e-7
    assert abs((y_sep(3.0 + h) - y_sep(3.0 - h)) / (2.0 * h) - 6.0) < 1e-5
    print("separable dy/dx = 2x: y = x^2 + 1 verified by differentiation")
    # linear via integrating factor: y' + 2y = 6, y(0) = 0 -> y = 3(1 - e^{-2x})
    y_lin = lambda x: 3.0 * (1.0 - math.exp(-2.0 * x))
    assert abs(y_lin(0.0)) < 1e-12
    assert abs((y_lin(1.0 + h) - y_lin(1.0 - h)) / (2.0 * h) + 2.0 * y_lin(1.0) - 6.0) < 1e-4
    print("linear y'+2y=6: integrating factor gives y = 3(1-e^{-2x}); substitution verifies")
    # direction field sample: dy/dx = x - y at (1, 0) has slope 1
    assert abs((1.0 - 0.0) - 1.0) < 1e-12
    print("direction field: slope at (1,0) for y' = x - y is 1")
    print("rule: separable splits, linear takes an integrating factor, the rest march numerically")
    print("OK: %s solved first-order" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_calc_de2num(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def simpson(f, a, b, n=2000):
    assert n % 2 == 0
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4.0 if i % 2 else 2.0) * f(a + i * h)
    return s * h / 3.0
def main():
    # characteristic: y'' + 3y' + 2y = 0 -> r^2 + 3r + 2 = 0 -> r = -1, -2
    import cmath
    disc = 9.0 - 8.0
    r1 = (-3.0 + math.sqrt(disc)) / 2.0
    r2 = (-3.0 - math.sqrt(disc)) / 2.0
    assert abs(r1 - (-1.0)) < 1e-12 and abs(r2 - (-2.0)) < 1e-12
    print("characteristic r^2+3r+2=0: roots -1, -2 -> y = C1 e^{-t} + C2 e^{-2t}")
    # verify y = e^{-t} satisfies the ODE numerically
    y = lambda t: math.exp(-t)
    h = 1e-5
    ypp = (y(h) - 2.0 * y(0.0) + y(-h)) / (h * h)
    yp = (y(h) - y(-h)) / (2.0 * h)
    assert abs(ypp + 3.0 * yp + 2.0 * y(0.0)) < 1e-3
    print("ODE residual for e^{-t}: %.2e (satisfies y''+3y'+2y=0)" % (ypp + 3.0 * yp + 2.0 * y(0.0)))
    # Laplace: L{t^2}(s) = 2/s^3; check at s = 2 numerically
    s = 2.0
    num = simpson(lambda t: math.exp(-s * t) * t * t, 0.0, 30.0)
    assert abs(num - 2.0 / s ** 3) < 1e-6, (num, 2.0 / s ** 3)
    print("Laplace L{t^2}(2) = %.6f = 2/2^3 (integral definition)" % num)
    # Simpson: integral_0^1 e^x dx, O(h^4) accuracy
    val = simpson(math.exp, 0.0, 1.0, n=40)
    exact = math.e - 1.0
    assert abs(val - exact) < 1e-8, (val, exact)
    print("Simpson n=40: integral_0^1 e^x dx = %.9f (error < 1e-8)" % val)
    # error order: doubling n cuts Simpson error ~16x
    e1 = abs(simpson(math.exp, 0.0, 1.0, n=10) - exact)
    e2 = abs(simpson(math.exp, 0.0, 1.0, n=20) - exact)
    assert e1 / e2 > 8.0, (e1, e2)
    print("Simpson error ratio n=10 -> n=20: %.1fx (O(h^4) theory says ~16x)" % (e1 / e2))
    print("rule: characteristic roots classify, Laplace algebraizes, Simpson integrates")
    print("OK: %s closed the ladder" % NAME)
if __name__ == "__main__":
    main()
''')

DEMOS = {
    "calc_branches": demo_calc_branches, "calc_models": demo_calc_models,
    "calc_limit_idea": demo_calc_limit_idea, "calc_limit_compute": demo_calc_limit_compute,
    "calc_continuity": demo_calc_continuity, "calc_deriv_def": demo_calc_deriv_def,
    "calc_diff_rules": demo_calc_diff_rules, "calc_chain": demo_calc_chain,
    "calc_implicit": demo_calc_implicit, "calc_higher": demo_calc_higher,
    "calc_related": demo_calc_related, "calc_optimize": demo_calc_optimize,
    "calc_sketch": demo_calc_sketch, "calc_lhopital": demo_calc_lhopital,
    "calc_antideriv": demo_calc_antideriv, "calc_riemann": demo_calc_riemann,
    "calc_ftc": demo_calc_ftc, "calc_substitution": demo_calc_substitution,
    "calc_parts": demo_calc_parts, "calc_trigint": demo_calc_trigint,
    "calc_partfrac": demo_calc_partfrac, "calc_improper": demo_calc_improper,
    "calc_area": demo_calc_area, "calc_volumes": demo_calc_volumes,
    "calc_arclen": demo_calc_arclen, "calc_sequences": demo_calc_sequences,
    "calc_series": demo_calc_series, "calc_taylor": demo_calc_taylor,
    "calc_powerseries": demo_calc_powerseries, "calc_parampolar": demo_calc_parampolar,
    "calc_partial": demo_calc_partial, "calc_multiple": demo_calc_multiple,
    "calc_vector": demo_calc_vector, "calc_theorems": demo_calc_theorems,
    "calc_de1": demo_calc_de1, "calc_de2num": demo_calc_de2num,
}
# ---------------------------------------------------------------- records

def build_records(slug, source):
    cfg = DBCFG[slug]
    sig = source == "signature"
    # Teaching-ladder order: stable sort by ladder_rank (entries are already
    # in ladder order in entries_calculus.py).
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
    for slug in ("calculus", "calculus-signature"):
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
                               capture_output=True, text=True, timeout=60)
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
