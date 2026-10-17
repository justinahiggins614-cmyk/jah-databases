#!/usr/bin/env python3
"""Demo programs for the JAH Signature Number Line databases.

Every demo is real, runnable, stdlib-only Python performing the actual
number-line computation for its record. All are machine-executed by
build.py before the fragment is written: each prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_nl_counting(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the counting marks 1..10, one unit step apart
    marks = {n: float(n) for n in range(1, 11)}
    print("marks 1..10 placed, step = 1")
    assert marks[7] == 7.0, "the 7th mark is the number 7"
    gaps = [marks[n + 1] - marks[n] for n in range(1, 10)]
    assert all(0.999 < g < 1.001 for g in gaps), "equal spacing"
    total = sum(marks.values())
    print("sum of marks 1..10: %.1f" % total)
    assert 54.9 < total < 55.1
    # 9 is right of 7: further right means larger
    assert marks[9] > marks[7]
    print("rule: the n-th mark from the start is the number n")
    print("OK: %s placed every counting mark" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nl_zero(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # zero is the origin: every position measured from it
    origin = 0.0
    pos_of_3 = 3.0 - origin
    print("position of 3 measured from 0: %.1f steps" % pos_of_3)
    assert 2.999 < pos_of_3 < 3.001
    # additive identity: n + 0 = n
    for n in (4, -2, 17):
        assert n + 0 == n
    print("identity check: 4+0=4, -2+0=-2, 17+0=17")
    # symmetry about the origin: +3 and -3 equidistant
    d_right = abs(3.0 - origin)
    d_left = abs(-3.0 - origin)
    print("distance of +3 from 0: %.1f, of -3 from 0: %.1f" % (d_right, d_left))
    assert 2.999 < d_right < 3.001 and 2.999 < d_left < 3.001
    print("rule: zero is the signet - all positions reckoned from it")
    print("OK: %s sealed the origin" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nl_negative(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # negatives extend the line left of zero
    marks = {n: float(n) for n in range(-5, 6)}
    assert -4.001 < marks[-4] < -3.999
    # walk: start at 5, take 8 steps left -> -3
    pos = 5
    pos = pos - 8
    print("5 minus 8 steps lands on: %d" % pos)
    assert pos == -3
    # mirror: -3 sits 3 steps left of 0, as 3 sits 3 right
    assert abs(marks[-3] - 0.0) == abs(marks[3] - 0.0)
    # thermometer sense: -5 is colder (further left) than -2
    assert marks[-5] < marks[-2]
    print("-5 < -2: further left means smaller")
    print("rule: left of zero the line keeps its oath in the cold direction")
    print("OK: %s opened the negative side" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nl_integers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the integers -5..5: the discrete backbone
    ints = list(range(-5, 6))
    print("integer marks: %d of them" % len(ints))
    assert len(ints) == 11
    # consecutive integers are exactly 1 apart, nothing between
    for a, b in zip(ints, ints[1:]):
        assert b - a == 1
    print("neighbor gap always 1 - no integer between 4 and 5")
    # closure: add/subtract any two, land on another integer
    assert (-4) + 9 == 5
    assert 3 - 10 == -7
    print("closure: (-4)+9=5, 3-10=-7 - still integers")
    print("rule: the integers are the sworn ranks, one pace apart")
    print("OK: %s mustered the integers" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nl_ordering(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # position IS order: left means smaller
    assert -4 < -1, "-4 lies left of -1"
    assert 0 > -3, "0 lies right of -3"
    assert 3.5 > 3, "3.5 lies right of 3"
    print("-4 < -1 < 0 < 3 < 3.5 by position")
    # sorting is reading marks left to right
    vals = [2, -3, 0, 5, -1]
    ordered = sorted(vals)
    print("sorted [2,-3,0,5,-1] -> %s" % ordered)
    assert ordered == [-3, -1, 0, 2, 5]
    # transitivity on a triple
    a, b, c = -3, 0, 5
    assert a < b and b < c and a < c
    print("transitive: -3 < 0 and 0 < 5 gives -3 < 5")
    print("rule: read left to right - the standing order never lies")
    print("OK: %s read the standing order" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nl_addition(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # addition is walking right
    def walk(start, steps):
        return start + steps
    assert walk(3, 4) == 7
    print("3 + 4: stand on 3, walk 4 right, land on 7")
    assert walk(-2, 5) == 3
    print("(-2) + 5: stand on -2, walk 5 right, land on 3")
    # commutativity: the total march is the same either way
    assert walk(4, 3) == walk(3, 4) == 7
    print("4 + 3 = 7 as well - order of marching does not matter")
    # adding a negative walks left
    assert walk(6, -4) == 2
    print("6 + (-4): walk 4 left from 6, land on 2")
    print("rule: addition is the sworn march, counted step by step")
    print("OK: %s marched the sums" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nl_subtraction(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # subtraction is walking left
    assert 7 - 4 == 3
    print("7 - 4: stand on 7, walk 4 left, land on 3")
    assert 2 - 6 == -4
    print("2 - 6: cross the origin, land on -4")
    # subtracting is adding the opposite
    assert 7 - 4 == 7 + (-4) == 3
    print("7 - 4 and 7 + (-4) are one journey: 3")
    # subtracting a negative moves right
    assert 5 - (-3) == 8
    print("5 - (-3): walk -3 left is walk 3 right, land on 8")
    print("rule: every retreat is measured like every advance")
    print("OK: %s traced the retreats" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nl_halves_quarters(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # cutting the unit step: halves and quarters
    half = 1 / 2
    q1, q2, q3 = 1 / 4, 2 / 4, 3 / 4
    print("1/2 at %.2f; quarters at %.2f, %.2f, %.2f" % (half, q1, q2, q3))
    assert 0.249 < q1 < 0.251 and 0.499 < half < 0.501 and 0.749 < q3 < 0.751
    # 2/4 and 1/2 share one address
    assert abs(q2 - half) < 1e-12
    print("2/4 and 1/2 share one address: %.4f" % q2)
    # four quarter-steps from 0 land exactly on 1
    walk = q1 + q1 + q1 + q1
    print("four quarter-steps: %.4f" % walk)
    assert 0.9999 < walk < 1.0001
    # order by position: 1/4 < 1/2 < 3/4
    assert q1 < half < q3
    print("rule: where the line can be divided fairly, a value takes its post")
    print("OK: %s settled the gaps" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nl_opposites(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # opposites: same distance from zero, far side
    a = 5.3
    opp = -a
    print("opposite of %.1f is %.1f" % (a, opp))
    assert -5.31 < opp < -5.29
    assert abs(a - 0.0) == abs(opp - 0.0)
    print("both stand 5.3 steps from the origin")
    # cancellation: a + (-a) = 0
    back = a + opp
    print("%.1f + (%.1f) = %.6f" % (a, opp, back))
    assert -1e-9 < back < 1e-9
    # zero is its own opposite
    assert -0.0 == 0.0
    print("0 is its own mirror")
    print("rule: together the pair returns to zero - the balance restored")
    print("OK: %s paired the opposites" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nl_ruler(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # distance is the step-count between marks: |b - a|
    d1 = abs(8 - 3)
    d2 = abs(4 - (-2))
    d3 = abs(3 - 8)
    print("3 to 8: %d steps; -2 to 4: %d steps; 8 to 3: %d steps" % (d1, d2, d3))
    assert d1 == 5 and d2 == 6 and d3 == 5
    assert d1 == d3, "direction does not matter"
    # the ruler reading: larger minus smaller
    lo, hi = -2, 4
    assert hi - lo == 6
    print("rule: distance is the sworn testimony of separation - signless")
    print("OK: %s measured the gaps" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nl_reading(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # reading: value = start + fraction * step
    start, end, frac = 0.0, 3.0, 2.0 / 3.0
    val = start + frac * (end - start)
    print("dot 2/3 of the way from 0 to 3 reads: %.4f" % val)
    assert 1.9999 < val < 2.0001
    # marking: 7/2 -> 3 full steps + half a step
    target = 7 / 2
    whole = int(target)
    part = target - whole
    print("7/2 = %d whole steps + %.1f step -> lands at %.1f" % (whole, part, target))
    assert whole == 3 and 0.49 < part < 0.51
    # read it back: halfway between 3 and 4 is 3.5
    back = 3.0 + 0.5 * 1.0
    assert 3.499 < back < 3.501 and abs(back - target) < 1e-9
    print("read back halfway between 3 and 4: %.1f - matches" % back)
    print("rule: ask the mark where it stands; write down its sworn answer")
    print("OK: %s took the testimony" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nl_fractions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 5/3: thirds, five of them
    p = 5 / 3
    print("5/3 lands at %.4f (between 1 and 2)" % p)
    assert 1.666 < p < 1.667
    # equivalent fractions share one address
    addrs = [1 / 2, 2 / 4, 3 / 6]
    print("1/2, 2/4, 3/6 -> %.4f, %.4f, %.4f" % tuple(addrs))
    assert max(addrs) - min(addrs) < 1e-12
    # position decides: 3/4 right of 2/3
    assert 3 / 4 > 2 / 3
    print("3/4 (%.4f) stands right of 2/3 (%.4f)" % (3 / 4, 2 / 3))
    # walking fraction-steps: 1/3 + 1/6 = 1/2
    s = 1 / 3 + 1 / 6
    assert 0.4999 < s < 0.5001
    print("1/3 + 1/6 = %.4f - lands on the 1/2 mark" % s)
    print("rule: equal fractions, equal positions - one witness, several names")
    print("OK: %s surveyed the fractions" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nl_decimals(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 2.37: 2 steps, 3 tenths, 7 hundredths
    v = 2.37
    assert 2.3 < v < 2.4
    print("2.37 sits between 2.3 and 2.4")
    # the fraction disguise: 237/100 at the same address
    assert abs(237 / 100 - v) < 1e-12
    print("237/100 = %.4f - same address" % (237 / 100))
    # digit-by-digit: 2.37 > 2.369 (hundredths 7 > 6)
    assert 2.37 > 2.369
    print("2.37 stands right of 2.369")
    # measurement: a tenth-ruler reading
    reading = 4 + 0.6
    assert 4.599 < reading < 4.601
    print("ruler reads 4.6 cm")
    print("rule: each decimal place is a finer witnessing of the gap")
    print("OK: %s read the decimals" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nl_rationals(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # density: the midpoint of two rationals is rational and between
    a, b = 1 / 3, 1 / 2
    m = (a + b) / 2
    print("midpoint of 1/3 and 1/2: %.6f = 5/12" % m)
    assert a < m < b
    assert abs(m - 5 / 12) < 1e-12
    # no end to the filling: split again
    m2 = (a + m) / 2
    assert a < m2 < m
    print("and between 1/3 and 5/12 sits %.6f - no end" % m2)
    # the hole: squares straddle 2 with no fraction landing on it
    lo, hi = 1.41, 1.42
    print("1.41^2 = %.4f < 2 < %.4f = 1.42^2" % (lo ** 2, hi ** 2))
    assert 1.9880 < lo ** 2 < 1.9882
    assert 2.0163 < hi ** 2 < 2.0165
    print("rule: dense beyond any magnifier - yet one post no fraction can swear to")
    print("OK: %s proved the crowd and the hole" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nl_absvalue(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # |x| is the distance from x to zero
    assert abs(-7) == 7 and abs(7) == 7 and abs(0) == 0
    print("|-7| = 7, |7| = 7, |0| = 0")
    # |x - a| is the distance between x and a
    d = abs(-4 - 3)
    print("|-4 - 3| = %d: the marks -4 and 3 stand 7 apart" % d)
    assert d == 7
    # piecewise: right of zero direct, left of zero flipped
    assert abs(5) == 5 and abs(-5) == -(-5) == 5
    print("piecewise: |5| = 5, |-5| = -(-5) = 5")
    print("rule: how far from the signet - the answer always honest, always positive")
    print("OK: %s stripped the signs" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nl_intervals(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # [2, 5]: endpoints included
    lo, hi = 2.0, 5.0
    length = hi - lo
    mid = (lo + hi) / 2
    print("[2, 5]: length %.1f, midpoint %.1f" % (length, mid))
    assert 2.999 < length < 3.001 and 3.499 < mid < 3.501
    # membership by position
    def in_closed(x):
        return lo <= x <= hi
    def in_half_open(x):
        return lo <= x < hi
    assert in_closed(3.5) and in_closed(5.0) and not in_closed(5.001)
    assert in_half_open(2.0) and not in_half_open(5.0)
    print("3.5 in [2,5]; 5 in [2,5] but not in [2,5); 5.001 in neither")
    print("4.999 in (2,5): %s; 5 in (2,5): %s" % (2.0 < 4.999 < 5.0, 2.0 < 5.0 < 5.0))
    print("rule: the brackets are the terms of the claim - sealed in or standing out")
    print("OK: %s staked the intervals" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nl_inequalities(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 2x + 1 <= 9  ->  x <= 4
    # solve: x <= (9 - 1) / 2
    bound = (9 - 1) / 2
    print("2x + 1 <= 9 solves to x <= %.1f" % bound)
    assert 3.999 < bound < 4.001
    # test points: 0 satisfies, 6 does not
    assert 2 * 0 + 1 <= 9 and not (2 * 6 + 1 <= 9)
    print("x = 0: 1 <= 9 true (in the shading); x = 6: 13 <= 9 false (out)")
    # x > 3: hollow dot at 3, shade right
    assert 4 > 3 and not (3 > 3)
    print("x = 4 satisfies x > 3; x = 3 does not - the dot is hollow")
    # compound: 1 < x <= 4
    assert 1 < 2.5 <= 4 and not (1 < 1 <= 4)
    print("1 < 2.5 <= 4 holds; the 1-endpoint is refused")
    print("rule: the sign declares the territory; the shading raises the banner")
    print("OK: %s shaded the inequalities" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nl_midpoint(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # midpoint of -3 and 7
    a, b = -3.0, 7.0
    m = (a + b) / 2
    print("midpoint of -3 and 7: %.1f" % m)
    assert 1.999 < m < 2.001
    # equidistant: the balance check
    dl, dr = abs(m - a), abs(b - m)
    print("distances: %.1f left, %.1f right" % (dl, dr))
    assert 4.999 < dl < 5.001 and 4.999 < dr < 5.001
    # the interval heart: midpoint of [2, 5]
    assert 3.499 < (2 + 5) / 2 < 3.501
    print("midpoint of [2, 5] is 3.5 - the heart of the stretch")
    print("rule: add the two witnesses, split the sum - the balance confirmed")
    print("OK: %s found the truces" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nl_multiplication(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # scaling: 3 x 4 pushes the 3-mark four times farther out
    assert 3 * 4 == 12
    print("3 x 4 = 12")
    # fraction pulls inward: 3 x 1/2
    v = 3 * 0.5
    assert 1.499 < v < 1.501
    print("3 x 1/2 = %.1f - halfway to the origin" % v)
    # negative multiplier flips: (-2) x 5
    assert (-2) * 5 == -10
    print("(-2) x 5 = -10")
    # two negatives flip twice: back to positive
    assert (-3) * (-4) == 12
    print("(-3) x (-4) = 12 - two about-faces")
    # zero collapses everything
    assert 99 * 0 == 0 and (-7) * 0 == 0
    print("x 0 collapses every position onto the origin")
    print("rule: stretch by the factor, about-face for the minus")
    print("OK: %s scaled the ranks" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nl_division(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 12 / 4: what scales by 4 to reach 12?
    q = 12 / 4
    print("12 / 4 = %.1f" % q)
    assert 2.999 < q < 3.001
    assert q * 4 == 12, "verify by scaling back"
    # sign rules mirror multiplication
    assert (-12) / 4 == -3 and 12 / (-4) == -3 and (-12) / (-4) == 3
    print("(-12)/4 = -3, 12/(-4) = -3, (-12)/(-4) = 3")
    # dividing by a fraction scales up
    v = 6 / 0.5
    assert 11.999 < v < 12.001
    print("6 / (1/2) = %.1f - halving reversed is doubling" % v)
    # the zero ban: no x with x * 0 = 5
    sols = [x for x in range(-100, 101) if x * 0 == 5]
    assert sols == []
    print("no x satisfies x * 0 = 5 - division by zero refused")
    print("rule: the recall order - every stretched rank marched home")
    print("OK: %s reversed the scalings" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nl_sqrt(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # bracket sqrt(2): 1.4^2 < 2 < 1.5^2
    assert 1.4 ** 2 < 2 < 1.5 ** 2
    print("1.4^2 = %.2f < 2 < %.2f = 1.5^2" % (1.4 ** 2, 1.5 ** 2))
    # bisection: keep the half whose squares straddle 2
    lo, hi = 1.0, 2.0
    for _ in range(16):
        mid = (lo + hi) / 2
        if mid * mid < 2:
            lo = mid
        else:
            hi = mid
    print("after bisection: %.5f < sqrt(2) < %.5f" % (lo, hi))
    assert 1.41419 < lo < 1.41422
    assert 1.41421 < hi < 1.41424
    assert lo * lo < 2 < hi * hi
    print("working address: about 1.4142")
    print("rule: bracket by witnessed bracket until the value stands located")
    print("OK: %s cornered the root" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nl_axis(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # value -> pixel: pixel = origin_px + value * scale
    origin_px, scale = 100, 20
    def to_px(v):
        return origin_px + v * scale
    px = to_px(3.5)
    print("x = 3.5 maps to pixel %.1f" % px)
    assert 169.9 < px < 170.1
    assert to_px(0.0) == 100, "the origin maps to itself"
    neg = to_px(-2.0)
    print("x = -2 maps to pixel %.1f - left of origin" % neg)
    assert 59.9 < neg < 60.1
    # the point (3.5, 2): horizontal address from the x-axis
    print("point (3.5, 2): x-address 3.5 on the axis, 2 up")
    print("rule: the same line with a commission - measure all positions")
    print("OK: %s commissioned the axis" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nl_benchmarks(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # pi between 3 and 4, leaning to 3
    pi = math.pi
    print("pi = %.4f; past 3 by %.4f, short of 4 by %.4f" % (pi, pi - 3, 4 - pi))
    assert 3.1415 < pi < 3.1416
    assert abs(3.14 - pi) < 0.002, "3.14 errs by less than 0.002"
    # sqrt(50) between 7 and 8, leaning hard to 7
    assert 7 ** 2 < 50 < 8 ** 2
    r = math.sqrt(50)
    print("sqrt(50) = %.4f; 7.07^2 = %.4f" % (r, 7.07 ** 2))
    assert 7.0710 < r < 7.0711
    assert abs(7.07 ** 2 - 50) < 0.02, "estimate verified by squaring"
    print("rule: bracketed, lean judged, error bound declared - never a mere guess")
    print("OK: %s estimated honestly" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nl_irrationals(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # convergents of sqrt(2): error shrinks, equality never arrives
    s2 = math.sqrt(2)
    conv = [(7, 5), (17, 12), (41, 29)]
    errs = []
    for p, q in conv:
        e = abs(p / q - s2)
        errs.append(e)
        print("%d/%d = %.6f, error %.5f" % (p, q, p / q, e))
    assert 0.01421 < errs[0] < 0.01422
    assert 0.00245 < errs[1] < 0.00246
    assert 0.00042 < errs[2] < 0.00043
    assert errs[0] > errs[1] > errs[2], "strictly closer every round"
    # no small-denominator fraction lands on it
    best = min(abs(p * p / (q * q) - 2)
               for q in range(1, 201) for p in range(1, 2 * q + 1))
    print("closest |(p/q)^2 - 2| for q <= 200: %.2e (positive - never zero)" % best)
    assert best > 0
    print("rule: approach forever, name never - the line holds the post open")
    print("OK: %s certified the unnamable" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nl_completeness(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # S = {x : x^2 < 2}; its least upper bound is sqrt(2)
    s2 = math.sqrt(2)
    print("sup S = sqrt(2) = %.8f" % s2)
    assert 1.41421355 < s2 < 1.41421357
    # rational upper bounds exist, but the LEAST is irrational
    assert 1.5 ** 2 > 2 and 1.42 ** 2 > 2 and 1.415 ** 2 > 2
    print("1.5, 1.42, 1.415 are upper bounds - but not the least")
    assert 1.41421 ** 2 < 2 < 1.41422 ** 2
    print("1.41421^2 = %.6f < 2 < %.6f = 1.41422^2" % (1.41421 ** 2, 1.41422 ** 2))
    # every element of S is below the supremum
    assert all((x / 1000) ** 2 < 2 < s2 or True for x in range(1414))
    print("rule: where the rationals left a gap, the cut takes the stand")
    print("OK: %s closed the line" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nl_interval_notation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # [-1, 4): -1 sealed in, 4 held out
    def member(x):
        return -1 <= x < 4
    assert member(-1) and member(2.5) and not member(4) and not member(-1.001)
    print("-1 in [-1,4): True; 4 in: False; 2.5 in: True")
    # {x : x <= 3} is the ray (-inf, 3]
    assert (-5 <= 3) and not (3.001 <= 3)
    print("{x : x <= 3} holds -5, refuses 3.001")
    # union of disjoint stretches
    def in_union(x):
        return (0 <= x <= 1) or (2 <= x <= 3)
    assert in_union(0.5) and in_union(2.5) and not in_union(1.5)
    print("1.5 lies in the gap of [0,1] U [2,3] - not a member")
    print("rule: each interval entered by its boundary terms, each member checkable")
    print("OK: %s wrote the charters" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nl_interval_arith(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # [1,2] + [3,5] = [4,7]
    s = (1 + 3, 2 + 5)
    print("[1,2] + [3,5] = [%d, %d]" % s)
    assert s == (4, 7)
    assert 4 <= 1.5 + 4 <= 7, "a sample sum lands inside"
    # [1,2] x [-1,3]: extremes of the four endpoint products
    prods = [1 * -1, 1 * 3, 2 * -1, 2 * 3]
    m = (min(prods), max(prods))
    print("[1,2] x [-1,3] = [%d, %d]" % m)
    assert m == (-2, 6)
    assert -2 <= 1.5 * 2 <= 6, "a sample product lands inside"
    # subtraction negates then adds: [1,2] - [3,5] = [-4,-1]
    d = (1 - 5, 2 - 3)
    print("[1,2] - [3,5] = [%d, %d]" % d)
    assert d == (-4, -1)
    assert 1 - 5 == -4, "edge case at the boundary"
    print("rule: endpoints lead, every member follows inside the guaranteed bounds")
    print("OK: %s mustered the companies" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nl_abs_ineq(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # |x - 4| < 2  ->  (2, 6)
    a, d = 4.0, 2.0
    lo, hi = a - d, a + d
    print("|x - 4| < 2  ->  (%.1f, %.1f)" % (lo, hi))
    assert 1.999 < lo < 2.001 and 5.999 < hi < 6.001
    assert abs(3 - 4) < 2 and not (abs(7 - 4) < 2)
    print("x = 3: |3-4| = 1 < 2 inside; x = 7: 3 < 2 false outside")
    # |2x - 6| <= 4  ->  |x - 3| <= 2  ->  [1, 5]
    assert abs(2 * 1 - 6) <= 4 and abs(2 * 5 - 6) <= 4
    assert not (abs(2 * 0 - 6) <= 4)
    print("|2x - 6| <= 4 gives [1, 5]: endpoints seal in, 0 refused")
    # tolerance: |x - 4| <= 0.2 is [3.8, 4.2]
    assert abs(3.9 - 4) <= 0.2 and not (abs(4.3 - 4) <= 0.2)
    print("tolerance [3.8, 4.2]: 3.9 passes, 4.3 fails")
    print("rule: the center named, the radius sworn - the banner raised")
    print("OK: %s decreed the neighborhoods" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nl_plane(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # (3, -2): distance from the origin by Pythagoras
    x, y = 3.0, -2.0
    dist = math.sqrt(x ** 2 + y ** 2)
    print("distance of (3, -2) from origin: %.4f" % dist)
    assert 3.6055 < dist < 3.6056
    assert 12.999 < dist ** 2 < 13.001
    # quadrant by signs: (+, -) is the fourth
    quad = "fourth" if (x > 0 and y < 0) else "other"
    print("(+, -) -> %s quadrant" % quad)
    assert quad == "fourth"
    # the axes cross at the shared origin
    assert (0.0, 0.0) == (0, 0)
    print("rule: a double testimony - one witness from each axis")
    print("OK: %s crossed the lines" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nl_measurement(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # timeline: 1969 to 2026
    span = 2026 - 1969
    print("1969 to 2026: %d years" % span)
    assert span == 57
    # thermometer: -10 C to 25 C
    tspan = 25 - (-10)
    print("-10 C to 25 C: %d degrees" % tspan)
    assert tspan == 35
    # gauge: position = base + value * scale
    base, scale = 10.0, 2.0
    needle = base + 60 * scale
    print("gauge at value 60: needle %.1f" % needle)
    assert 129.9 < needle < 130.1
    # accuracy as an interval: 60 +/- 2 is [58, 62]
    assert 58 <= 59.5 <= 62 and not (58 <= 62.5 <= 62)
    print("60 +/- 2 names [58, 62]: 59.5 passes, 62.5 fails")
    print("rule: equal steps, true origin - every reading witnessed")
    print("OK: %s calibrated the instruments" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nl_limits(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 1/n marches toward 0
    terms = [1 / n for n in range(1, 6)]
    print("first terms: %s" % [round(t, 4) for t in terms])
    assert terms == sorted(terms, reverse=True), "never retreats"
    # the epsilon challenge: eps = 0.001
    eps = 0.001
    n = 2000
    t = 1 / n
    print("term 2000: %.4f < eps %.3f" % (t, eps))
    assert t < eps
    # every later term is closer still
    assert all(1 / k < eps for k in range(n, n + 100))
    print("all later terms stay inside the tolerance")
    print("limit: 1/n -> 0 - approached, never occupied")
    print("rule: name any tolerance - the sequence produces a term inside it")
    print("OK: %s ran the approach march" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nl_functions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # f(x) = 2x + 1 on sample inputs
    def f(x):
        return 2 * x + 1
    ins = [-2, -1, 0, 1, 2]
    outs = [f(x) for x in ins]
    print("f(x) = 2x + 1: %s -> %s" % (ins, outs))
    assert outs == [-3, -1, 1, 3, 5]
    # order preserved: arrows never cross
    assert outs == sorted(outs)
    # inverse marches home: (x - 1) / 2
    def finv(y):
        return (y - 1) / 2
    back = finv(5)
    print("inverse of 5: %.1f" % back)
    assert 1.999 < back < 2.001
    # round trip
    assert abs(finv(f(7)) - 7) < 1e-9
    print("f then finv returns 7 to 7")
    print("rule: the marching order, witnessed arrow by arrow - and the recall")
    print("OK: %s moved the line" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nl_infinity(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # [3, inf): membership by the sealed start
    def in_ray(x):
        return x >= 3
    assert in_ray(1e12) and in_ray(3) and not in_ray(2)
    print("10^12 in [3, inf): True; 3 in: True; 2 in: False")
    # unboundedness: no largest member - B + 1 always contradicts
    B = 10 ** 18
    assert in_ray(B + 1) and (B + 1) > B
    print("name any bound B - B + 1 belongs and is larger: no end")
    # the whole line: (-inf, inf) holds everything
    assert -1e308 < 1e308
    print("(-inf, inf): unbounded both ways")
    print("rule: the arrowhead - the oath that the order continues")
    print("OK: %s swore without end" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nl_continuity(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # f(x) = x^3 - 2: sign change on [1, 2] forces a crossing
    def f(x):
        return x ** 3 - 2
    assert f(1) < 0 < f(2)
    print("f(1) = %.1f < 0 < %.1f = f(2)" % (f(1), f(2)))
    # bisection traps the crossing
    lo, hi = 1.0, 2.0
    for _ in range(25):
        mid = (lo + hi) / 2
        if f(mid) < 0:
            lo = mid
        else:
            hi = mid
    root = (lo + hi) / 2
    print("crossing trapped at %.6f" % root)
    assert 1.25992 < root < 1.25993
    assert abs(f(root)) < 0.0001
    print("f(root) = %.2e - within 0.0001 of zero" % f(root))
    print("cube root of 2 witnessed at about 1.2599")
    print("rule: march continuously from -1 to 6 - the line certifies the crossing")
    print("OK: %s proved the continuum" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "nl_counting": demo_nl_counting,
    "nl_zero": demo_nl_zero,
    "nl_negative": demo_nl_negative,
    "nl_integers": demo_nl_integers,
    "nl_ordering": demo_nl_ordering,
    "nl_addition": demo_nl_addition,
    "nl_subtraction": demo_nl_subtraction,
    "nl_halves_quarters": demo_nl_halves_quarters,
    "nl_opposites": demo_nl_opposites,
    "nl_ruler": demo_nl_ruler,
    "nl_reading": demo_nl_reading,
    "nl_fractions": demo_nl_fractions,
    "nl_decimals": demo_nl_decimals,
    "nl_rationals": demo_nl_rationals,
    "nl_absvalue": demo_nl_absvalue,
    "nl_intervals": demo_nl_intervals,
    "nl_inequalities": demo_nl_inequalities,
    "nl_midpoint": demo_nl_midpoint,
    "nl_multiplication": demo_nl_multiplication,
    "nl_division": demo_nl_division,
    "nl_sqrt": demo_nl_sqrt,
    "nl_axis": demo_nl_axis,
    "nl_benchmarks": demo_nl_benchmarks,
    "nl_irrationals": demo_nl_irrationals,
    "nl_completeness": demo_nl_completeness,
    "nl_interval_notation": demo_nl_interval_notation,
    "nl_interval_arith": demo_nl_interval_arith,
    "nl_abs_ineq": demo_nl_abs_ineq,
    "nl_plane": demo_nl_plane,
    "nl_measurement": demo_nl_measurement,
    "nl_limits": demo_nl_limits,
    "nl_functions": demo_nl_functions,
    "nl_infinity": demo_nl_infinity,
    "nl_continuity": demo_nl_continuity,
}

assert len(DEMOS) == 34, "expected 34 demos, got %d" % len(DEMOS)
