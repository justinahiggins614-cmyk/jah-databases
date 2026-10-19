#!/usr/bin/env python3
"""Demo programs for the Unsolved Mathematics databases (Manon's 16:15 orders, batch 1).

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

_PREAMBLE = "import math\n\ndef _sieve(n):\n    bs = bytearray(b'\\x01') * (n + 1)\n    bs[0:2] = b'\\x00\\x00'\n    for i in range(2, int(math.isqrt(n)) + 1):\n        if bs[i]:\n            bs[i*i:n+1:i] = b'\\x00' * ((n - i*i)//i + 1)\n    return [i for i in range(2, n + 1) if bs[i]]\n\ndef _is_prime(n):\n    if n < 2:\n        return False\n    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):\n        if n % p == 0:\n            return n == p\n    d = n - 1\n    r = 0\n    while d % 2 == 0:\n        d //= 2\n        r += 1\n    for a in (2, 3, 5, 7, 11, 13):\n        if a % n == 0:\n            continue\n        x = pow(a, d, n)\n        if x in (1, n - 1):\n            continue\n        for _ in range(r - 1):\n            x = (x * x) % n\n            if x == n - 1:\n                break\n        else:\n            return False\n    return True\n\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_usma_goldbach(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    primes = _sieve(200000)
    is_p = bytearray(b'\\x00') * 200001
    for p in primes:
        is_p[p] = 1
    def partitions(n):
        c = 0
        for p in primes:
            if p > n // 2:
                break
            if is_p[n - p]:
                c += 1
        return c
    worst = None
    for n in range(4, 2001, 2):
        c = partitions(n)
        if worst is None or c < worst[1]:
            worst = (n, c)
    print("evens checked: 4..2000, every one partitioned")
    print("fewest Goldbach partitions: %d at n=%d" % (worst[1], worst[0]))
    for n in (100, 1000, 2000):
        print("partitions(%d) = %d" % (n, partitions(n)))
    assert worst[1] >= 1, "an even with zero partitions would kill the conjecture"
    # Signature approach S-01: density-heuristic ascent (circle method).
    # Adjustable assumption A1: minor arcs stay below the Hardy-Littlewood main term.
    hl = 2000 / (2.0 * (math.log(1000.0) ** 2))
    print("Hardy-Littlewood order estimate at n=2000: %.1f partitions" % hl)
    print("approach: prove the asymptotic with an explicit minor-arc bound")
    print("CONFIRM IF: the minor-arc contribution is proved smaller than the major-arc main term for all large even n")
    print("REFUTE IF: one even n > 2 with zero prime partitions is exhibited")
    print("does NOT claim: a proof, peer acceptance, or a timeline")
    print("OK: %s explored partitions to 2000" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usma_collatz(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    import random
    def stopping(n):
        c = 0
        while n != 1:
            n = n // 2 if n % 2 == 0 else 3 * n + 1
            c += 1
        return c
    worst = (0, 0)
    for n in range(1, 100000):
        t = stopping(n)
        if t > worst[1]:
            worst = (n, t)
    print("integers 1..99999: all reached 1")
    print("longest chain: n=%d steps=%d" % worst)
    assert worst[1] >= 300
    # Signature approach S-02: probabilistic drift on the odd-step map.
    # Adjustable assumption A2: odd steps shrink by factor ~3/4 on average.
    random.seed(7)
    s = 0.0
    M = 50000
    for _ in range(M):
        n = random.randrange(1, 10 ** 12, 2)
        t = 3 * n + 1
        k = (t & -t).bit_length() - 1
        s += math.log(t) - math.log(n) - k * math.log(2)
    mean = s / M
    print("mean log drift per odd step: %.5f (theory ln(3/4) = -0.28768)" % mean)
    assert -0.32 < mean < -0.25
    print("approach: turn the negative drift into a proof that no divergent orbit exists")
    print("CONFIRM IF: a proof rules out both nontrivial cycles and divergent orbits")
    print("REFUTE IF: one integer whose orbit never reaches 1 is exhibited")
    print("does NOT claim: a proof - drift is heuristic, and heuristics are not theorems")
    print("OK: %s reached 1 for all n < 100000" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usma_twin_prime(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    N = 200000
    primes = _sieve(N)
    s = set(primes)
    twins = [p for p in primes if p + 2 in s]
    print("twin prime pairs below %d: %d" % (N, len(twins)))
    print("largest pair below %d: (%d, %d)" % (N, twins[-1], twins[-1] + 2))
    assert len(twins) > 1000
    # Signature approach S-03: twin-prime constant density ascent.
    # Adjustable assumption A3: pairs follow the Hardy-Littlewood density 2*C2/(ln x)^2.
    C2 = 0.6601618158468696
    M = 20000
    a, b = 2.0, float(N)
    h = (b - a) / M
    tot = 0.0
    for i in range(M + 1):
        x = a + i * h
        w = 1.0 if i == 0 or i == M else (4.0 if i % 2 == 1 else 2.0)
        tot += w / (math.log(x) ** 2)
    est = 2 * C2 * tot * h / 3.0
    print("Hardy-Littlewood estimate: %.0f pairs" % est)
    assert 0.85 * est < len(twins) < 1.15 * est
    print("approach: extend bounded-gap sieve methods toward gap 2")
    print("CONFIRM IF: a sieve argument pushes the bounded gap from 246 down to 2")
    print("REFUTE IF: twin primes are proved finite (no such proof exists)")
    print("does NOT claim: infinitude - the data fit the heuristic; the heuristic is not a proof")
    print("OK: %s counted twin pairs to 200000" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usma_odd_perfect(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    N = 200000
    sig = [0] * (N + 1)
    for i in range(1, N + 1):
        for j in range(i, N + 1, i):
            sig[j] += i
    found = [n for n in range(3, N + 1, 2) if sig[n] == 2 * n]
    print("odd perfect numbers below %d: %s" % (N, found))
    assert found == []
    # Signature approach S-04: Euler-form descent.
    # Key lemma (Euler): sigma(q^a) for odd prime q is even iff a is odd.
    def sigma_pp(q, a):
        return sum(q ** k for k in range(a + 1))
    for q in (3, 5, 7, 11, 13):
        for a in range(1, 7):
            assert (sigma_pp(q, a) % 2 == 0) == (a % 2 == 1)
    print("Euler parity lemma verified on odd prime powers")
    print("approach: from sigma(N) = 2N with N odd, force the Euler form q^a m^2,")
    print("  then derive a contradiction from the divisor structure of m")
    print("CONFIRM IF: an odd perfect number is exhibited, or nonexistence is proved")
    print("REFUTE IF: the Euler-form constraints are shown compatible with existence")
    print("does NOT claim: existence or nonexistence - both remain open")
    print("OK: %s searched odds below 200000" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usma_mersenne(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    exps = _sieve(61)
    found = [p for p in exps if _is_prime((1 << p) - 1)]
    print("Mersenne prime exponents <= 61: %s" % found)
    assert found == [2, 3, 5, 7, 13, 17, 19, 31, 61]
    # Signature approach S-05: Lenstra-Pomerance-Wagstaff heuristic ascent.
    # Adjustable assumption A5: Mersenne primes follow the LPW density.
    pred = (math.exp(0.5772156649) / math.log(2)) * math.log(61 * math.log(2))
    print("LPW predicted count near 2^61: %.2f; actual: %d" % (pred, len(found)))
    assert abs(pred - len(found)) < 1.5
    print("approach: prove a weak form of the LPW heuristic via prime constellations in Lucas sequences")
    print("CONFIRM IF: infinitely many Mersenne primes are proved to exist")
    print("REFUTE IF: Mersenne primes are proved finite (no such proof exists)")
    print("does NOT claim: infinitude - the heuristic fits; fitting is not proving")
    print("OK: %s verified Mersenne exponents to 61" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usma_sophie_germain(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    N = 200000
    primes = _sieve(2 * N + 1)
    s = set(primes)
    sg = [p for p in primes if p <= N and 2 * p + 1 in s]
    print("Sophie Germain primes below %d: %d" % (N, len(sg)))
    print("largest below %d: %d (2p+1 = %d)" % (N, sg[-1], 2 * sg[-1] + 1))
    assert len(sg) > 500
    # Signature approach S-06: prime-constellation density ascent.
    # Adjustable assumption A6: SG primes follow 2*C2*N/(ln N)^2.
    C2 = 0.6601618158468696
    est = 2 * C2 * N / (math.log(N) ** 2)
    print("constellation estimate: %.0f" % est)
    assert 0.7 * est < len(sg) < 1.3 * est
    print("approach: adapt the bounded-gap sieve machinery to the pair (p, 2p+1)")
    print("CONFIRM IF: infinitely many Sophie Germain primes are proved to exist")
    print("REFUTE IF: they are proved finite (no such proof exists)")
    print("does NOT claim: infinitude - Germain used them for Fermat; their infinitude is still open")
    print("OK: %s counted Sophie Germain primes to 200000" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usma_beal(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    import math as _m
    LIM = 40
    powers = {}
    for x in range(2, LIM + 1):
        for p in range(3, 7):
            powers.setdefault(x ** p, (x, p))
    S = set(powers)
    vals = sorted(S)
    sols, coprime = [], []
    for z in range(2, LIM + 1):
        for r in range(3, 7):
            t = z ** r
            if t > 2 * LIM ** 6:
                break
            for v in vals:
                if v >= t:
                    break
                w = t - v
                if w in S:
                    x, p = powers[v]
                    y, q = powers[w]
                    if _m.gcd(_m.gcd(x, y), z) == 1:
                        coprime.append((x, p, y, q, z, r))
                    else:
                        sols.append((x, p, y, q, z, r))
    print("solutions x^p + y^q = z^r with a common prime factor: %d" % len(sols))
    print("solutions with coprime bases: %d" % len(coprime))
    assert len(sols) >= 3
    assert coprime == [], "a coprime solution would refute Beal outright"
    # Signature approach S-07: Frey-curve descent.
    # Adjustable assumption A7: a coprime Beal solution yields a Frey-type elliptic curve
    #   whose mod-p Galois representation is too constrained to exist (as in Wiles).
    print("approach: attach a Frey curve to a hypothetical coprime solution and derive a contradiction via modularity")
    print("CONFIRM IF: the Frey-curve contradiction is completed for all exponent patterns")
    print("REFUTE IF: one coprime solution with p,q,r > 2 is exhibited")
    print("does NOT claim: a proof - the million-dollar prize is still unclaimed")
    print("OK: %s searched x,y,z <= 40, exponents 3..6" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usma_legendre(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    LIM = 3000
    primes = _sieve((LIM + 1) * (LIM + 1))
    idx = 0
    worst = None
    for n in range(1, LIM + 1):
        lo, hi = n * n, (n + 1) * (n + 1)
        while primes[idx] <= lo:
            idx += 1
        assert primes[idx] < hi, "Legendre fails at n=%d" % n
        cnt = 0
        j = idx
        while j < len(primes) and primes[j] < hi:
            cnt += 1
            j += 1
        if worst is None or cnt < worst[1]:
            worst = (n, cnt)
    print("n checked: 1..%d - every interval (n^2, (n+1)^2) holds a prime" % LIM)
    print("fewest primes in any interval: %d at n=%d" % (worst[1], worst[0]))
    assert worst[1] >= 1
    # Signature approach S-08: prime-gap ceiling descent.
    # Adjustable assumption A8: maximal prime gaps below x stay under 2*sqrt(x) + 1.
    print("approach: prove p_{n+1} - p_n < 2*sqrt(p_n) + 1 via explicit zero-free regions")
    print("CONFIRM IF: an explicit prime-gap bound below the interval length is proved for all x")
    print("REFUTE IF: one n with no prime between n^2 and (n+1)^2 is found")
    print("does NOT claim: a proof - it would follow from RH but is open unconditionally")
    print("OK: %s verified Legendre intervals to n=3000" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usma_brocard_ramanujan(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    sols = []
    for n in range(2, 23):
        f = math.factorial(n) + 1
        r = math.isqrt(f)
        if r * r == f:
            sols.append((n, r))
    print("n <= 22 with n! + 1 a perfect square: %s" % sols)
    assert [n for n, _ in sols] == [4, 5, 7]
    # Signature approach S-09: abc-powered finiteness ascent.
    # Adjustable assumption A9: the abc conjecture holds, forcing n! + 1 = m^2 to have finitely many solutions.
    print("approach: assume abc; then n! + 1 = m^2 forces n bounded, and a finite check closes the list")
    print("CONFIRM IF: abc is proved and the resulting finite bound is checked")
    print("REFUTE IF: a fourth solution (n beyond 7) is found")
    print("does NOT claim: finiteness - without abc even finiteness is open")
    print("OK: %s confirmed only n = 4, 5, 7 below 23" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usma_three_cubes(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    B = 200
    c3 = [i ** 3 for i in range(-B, B + 1)]
    S = set(c3)
    done, missing = [], []
    for k in range(1, 51):
        if k % 9 in (4, 5):
            continue
        ok = False
        for x3 in c3:
            if ok:
                break
            for y3 in c3:
                if k - x3 - y3 in S:
                    ok = True
                    break
        (done if ok else missing).append(k)
    print("eligible k <= 50 represented with |x|,|y|,|z| <= %d: %d of %d" % (B, len(done), len(done) + len(missing)))
    print("not found within bounds: %s" % missing)
    # the proven obstruction: cubes mod 9 are only 0, 1, 8
    residues = {(a + b + c) % 9 for a in (0, 1, 8) for b in (0, 1, 8) for c in (0, 1, 8)}
    assert 4 not in residues and 5 not in residues
    assert len(done) >= 30
    # Signature approach S-10: descent via the elliptic-curve ladder.
    # Adjustable assumption A10: for each eligible k, the curve x^3 + y^3 = k - z^3
    #   carries a rational point reachable by a bounded search.
    print("approach: parametrize x^3 + y^3 + z^3 = k via elliptic curves of increasing rank")
    print("CONFIRM IF: every eligible k is exhibited with an explicit triple")
    print("REFUTE IF: one eligible k is proved to have no integer representation")
    print("does NOT claim: that every eligible k works - that is exactly what is open")
    print("OK: %s represented sums of three cubes" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usma_gilbreath(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    primes = _sieve(20000)
    a = primes[:]
    rounds = 0
    while len(a) > 1:
        a = [abs(a[i + 1] - a[i]) for i in range(len(a) - 1)]
        assert a[0] == 1, "Gilbreath fails at round %d" % rounds
        rounds += 1
    print("primes below 20000: %d; difference rounds: %d" % (len(primes), rounds))
    print("first term of every row: 1")
    # Signature approach S-11: prime-gap control ascent.
    # Adjustable assumption A11: prime gaps grow slowly enough that the iterated
    #   differences keep collapsing to a leading 1.
    print("approach: bound the iterated absolute differences via maximal prime gaps")
    print("CONFIRM IF: a prime-gap theorem forces the leading 1 at every iteration depth")
    print("REFUTE IF: one starting row of primes yields a leading term other than 1")
    print("does NOT claim: a proof - verified to 20000 here, conjectured for all primes")
    print("OK: %s ran Gilbreath differences to completion" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usma_moving_sofa(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    hammersley = math.pi / 2 + 2 / math.pi
    gerver = 2.219531668871
    kallus_romik = 2.37
    trivial = 2 * math.sqrt(2)
    print("Hammersley sofa area (lower bound): %.6f" % hammersley)
    print("Gerver sofa area (best known):       %.6f" % gerver)
    print("Kallus-Romik upper bound:            %.6f" % kallus_romik)
    print("trivial upper bound 2*sqrt(2):      %.6f" % trivial)
    assert 2.2074 < hammersley < 2.2075
    assert hammersley < gerver < kallus_romik < trivial
    # Signature approach S-12: parametric shape optimization.
    # Adjustable assumption A12: the optimum is a balanced lambda-shape whose
    #   boundary arcs are fixed by the hallway walls (Gerver's 18-curve form).
    print("approach: parametrize candidate sofas, derive Euler-Lagrange conditions on the arcs,")
    print("  and prove no asymmetric perturbation beats the symmetric Gerver form")
    print("CONFIRM IF: Gerver's constant is proved optimal among all movable shapes")
    print("REFUTE IF: a sofa with area above 2.37 is exhibited")
    print("does NOT claim: optimality - the gap between 2.2195 and 2.37 is still open")
    print("OK: %s bounded the moving sofa" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usma_near_square(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    N = 100000
    hits = [n for n in range(2, N + 1, 2) if _is_prime(n * n + 1)]
    print("even n <= %d with n^2+1 prime: %d" % (N, len(hits)))
    print("largest: n=%d -> %d" % (hits[-1], hits[-1] ** 2 + 1))
    assert len(hits) > 50
    # Signature approach S-13: polynomial-value sieve ascent.
    # Adjustable assumption A13: n^2+1 follows the Hardy-Littlewood density C*N/ln(N^2).
    C = 1.37281346
    est = C * N / math.log(N * N)
    print("heuristic estimate: %.0f" % est)
    assert 0.5 * est < len(hits) < 2.0 * est
    print("approach: extend the Friedlander-Iwaniec sieve for x^2 + y^4 toward y = 1")
    print("CONFIRM IF: infinitely many primes of the form n^2+1 are proved to exist")
    print("REFUTE IF: n^2+1 is proved to take prime values only finitely often")
    print("does NOT claim: infinitude - Landau listed it in 1912 and it is still open")
    print("OK: %s counted near-square primes to 100000" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usma_andrica(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    primes = _sieve(2000000)
    mx = 0.0
    at = (0, 0)
    for a, b in zip(primes, primes[1:]):
        d = math.sqrt(b) - math.sqrt(a)
        if d > mx:
            mx, at = d, (a, b)
    print("primes checked: %d" % len(primes))
    print("max sqrt-gap: %.6f at (%d, %d)" % (mx, at[0], at[1]))
    assert mx < 1.0
    assert mx < 0.8
    # Signature approach S-14: square-root gap descent.
    # Adjustable assumption A14: prime gaps satisfy p_{n+1} - p_n < 2*sqrt(p_n) + 1 for all n.
    print("approach: prove the gap bound 2*sqrt(p)+1 via explicit zero-free regions for zeta")
    print("CONFIRM IF: the gap bound is proved for all primes")
    print("REFUTE IF: one prime pair violates sqrt(p_{n+1}) - sqrt(p_n) < 1")
    print("does NOT claim: a proof - Andrica implies Legendre, and both are open")
    print("OK: %s measured prime sqrt-gaps to 2000000" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usma_oppermann(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    LIM = 3000
    primes = _sieve(LIM * (LIM + 1))
    idx = 0
    for n in range(2, LIM + 1):
        lo1, mid, hi1 = n * (n - 1), n * n, n * (n + 1)
        while primes[idx] <= lo1:
            idx += 1
        assert primes[idx] < mid, "Oppermann lower fails at n=%d" % n
        j = idx
        while primes[j] < mid:
            j += 1
        assert primes[j] < hi1, "Oppermann upper fails at n=%d" % n
    print("n checked: 2..%d - primes found in both (n(n-1), n^2) and (n^2, n(n+1))" % LIM)
    # Signature approach S-15: half-interval prime descent.
    # Adjustable assumption A15: prime gaps below x^2 stay under x for all large x.
    print("approach: sharpen explicit prime-gap bounds to beat intervals of length ~n")
    print("CONFIRM IF: a prime-gap bound below n is proved near n^2 for all n")
    print("REFUTE IF: one n lacks a prime in either half-interval")
    print("does NOT claim: a proof - stronger than Legendre, equally open")
    print("OK: %s verified Oppermann intervals to n=3000" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usma_cramer(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    primes = _sieve(2000000)
    max_gap, max_merit, at = 0, 0.0, (0, 0)
    for a, b in zip(primes, primes[1:]):
        g = b - a
        if g > max_gap:
            max_gap = g
        if a < 1000:
            continue
        m = g / (math.log(a) ** 2)
        if m > max_merit:
            max_merit, at = m, (a, b)
    print("primes checked: %d" % len(primes))
    print("max gap: %d; max merit gap/(ln p)^2 for p >= 1000: %.4f at (%d, %d)" % (max_gap, max_merit, at[0], at[1]))
    assert max_merit < 1.2
    # Signature approach S-16: random-model gap ascent.
    # Adjustable assumption A16: prime gaps behave like the Cramer random model, max ~ (ln p)^2.
    print("approach: make the Cramer model rigorous via a sieve with random-like error terms")
    print("CONFIRM IF: lim sup of gap/(ln p)^2 is proved to equal 1")
    print("REFUTE IF: gaps exceeding (ln p)^2 by an unbounded factor are found")
    print("does NOT claim: the constant 1 - the model predicts it; proof is far away")
    print("OK: %s measured prime gaps to 2000000" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usma_lehmer(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    from array import array
    N = 3000000
    phi = array('I', range(N + 1))
    for i in range(2, N + 1):
        if phi[i] == i:
            for j in range(i, N + 1, i):
                phi[j] -= phi[j] // i
    bad = [n for n in range(4, N + 1) if phi[n] != n - 1 and (n - 1) % phi[n] == 0]
    print("composite n <= %d with phi(n) dividing n-1: %s" % (N, bad))
    assert bad == []
    # Signature approach S-17: Korselt-type descent.
    # Adjustable assumption A17: any Lehmer composite is odd, squarefree, with many prime factors.
    print("approach: push the known factor-count lower bounds until the product exceeds any bound")
    print("CONFIRM IF: a composite with phi(n) | (n-1) is exhibited, or impossibility is proved")
    print("REFUTE IF: the factor-count bounds stall below a contradiction")
    print("does NOT claim: either outcome - Lehmer asked in 1932 and both are open")
    print("OK: %s searched composites to 3000000" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usma_odd_weird(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    N = 30000
    spf = list(range(N + 1))
    for i in range(2, int(math.isqrt(N)) + 1):
        if spf[i] == i:
            for j in range(i * i, N + 1, i):
                if spf[j] == j:
                    spf[j] = i
    def sigma(n):
        s = 1
        while n > 1:
            p = spf[n]
            pw = 1
            while n % p == 0:
                n //= p
                pw *= p
            s *= (pw * p - 1) // (p - 1)
        return s
    def proper_divisors(n):
        fac = []
        m = n
        while m > 1:
            p = spf[m]
            e = 0
            while m % p == 0:
                m //= p
                e += 1
            fac.append((p, e))
        divs = [1]
        for p, e in fac:
            cur = []
            pw = 1
            for _ in range(e):
                pw *= p
                for d in divs:
                    cur.append(d * pw)
            divs += cur
        divs.remove(n)
        return divs
    weird = []
    abundant = 0
    for n in range(3, N + 1, 2):
        sn = sigma(n)
        if sn > 2 * n:
            abundant += 1
            target = sn - 2 * n
            bits = 1
            for d in proper_divisors(n):
                bits |= bits << d
                if (bits >> target) & 1:
                    break
            if not ((bits >> target) & 1):
                weird.append(n)
    print("odd abundant numbers below %d: %d" % (N, abundant))
    print("odd weird numbers found: %s" % weird)
    assert weird == []
    # Signature approach S-18: abundancy-index ascent.
    # Adjustable assumption A18: odd weird numbers, if any, have abundancy index
    #   sigma(n)/n in a narrow window that a refined search can rule out progressively.
    print("approach: bound the abundancy index of odd weird candidates and extend the search window")
    print("CONFIRM IF: an odd weird number is exhibited")
    print("REFUTE IF: odd weird numbers are proved impossible")
    print("does NOT claim: either - none are known, and none are ruled out")
    print("OK: %s tested odd abundants below 30000" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usma_aliquot(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    import random
    random.seed(99)
    def pollard_rho(n):
        if n % 2 == 0:
            return 2
        if n % 3 == 0:
            return 3
        while True:
            c = random.randrange(1, n)
            x = random.randrange(2, n)
            y = x
            d = 1
            while d == 1:
                x = (x * x + c) % n
                y = (y * y + c) % n
                y = (y * y + c) % n
                d = math.gcd(abs(x - y), n)
            if d != n:
                return d
    def factorize(n, out):
        if n == 1:
            return
        if _is_prime(n):
            out.append(n)
            return
        d = pollard_rho(n)
        factorize(d, out)
        factorize(n // d, out)
    def sigma(n):
        fac = []
        factorize(n, fac)
        s = 1
        for p in set(fac):
            e = fac.count(p)
            s *= (p ** (e + 1) - 1) // (p - 1)
        return s
    CAP, VLIM = 3000, 10 ** 18
    status = {}
    trails = {}
    def classify(n):
        seen = {}
        seq = []
        cur = n
        while True:
            if cur in status:
                st = status[cur]
                break
            if cur in seen:
                st = "cycle"
                break
            if cur <= 1:
                st = "terminates"
                break
            if len(seq) > CAP or cur > VLIM:
                st = "open-at-cap"
                break
            seen[cur] = len(seq)
            seq.append(cur)
            cur = sigma(cur) - cur
        if st in ("terminates", "cycle"):
            for v in seq:
                status[v] = st
        else:
            trails[n] = seq
        return st
    results = [(n, classify(n)) for n in range(2, 1001)]
    n_term = sum(1 for _, st in results if st == "terminates")
    n_cyc = sum(1 for _, st in results if st == "cycle")
    open_ids = [n for n, st in results if st == "open-at-cap"]
    # merge open starts into families by shared sequence values
    parent = {n: n for n in open_ids}
    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a
    val_owner = {}
    for n in open_ids:
        for v in trails[n]:
            if v in val_owner:
                a, b = find(n), find(val_owner[v])
                if a != b:
                    parent[a] = b
            else:
                val_owner[v] = n
    families = {}
    for n in open_ids:
        families.setdefault(find(n), []).append(n)
    print("starting values 2..1000: terminates=%d cycles=%d open-at-cap=%d" % (n_term, n_cyc, len(open_ids)))
    print("open-at-cap families (%d):" % len(families))
    for rep, members in sorted(families.items()):
        print("  family of %d: %s" % (rep, members))
    for f in (276, 552, 564, 660, 966):
        assert f in open_ids, "famous open case %d should be open at cap" % f
    assert len(families) <= 8, "open starts should merge into few families"
    # Signature approach S-19: driver-action ascent.
    # Adjustable assumption A19: aliquot sequences are driven by small prime factors;
    #   controlling the driver structure bounds the growth.
    print("approach: classify sequences by their driver (the persistent small-factor pattern)")
    print("  and prove every driver class either terminates or cycles")
    print("CONFIRM IF: every aliquot sequence is proved to terminate or cycle")
    print("REFUTE IF: one sequence is proved to diverge to infinity")
    print("does NOT claim: termination - 276 alone keeps the question open")
    print("OK: %s classified aliquot sequences below 1000" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usma_perfect_cuboid(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    LIM = 300
    sq = set(i * i for i in range(1, 3 * LIM + 1))
    pairs = []
    for a in range(1, LIM + 1):
        for b in range(a + 1, LIM + 1):
            if a * a + b * b in sq:
                pairs.append((a, b, math.isqrt(a * a + b * b)))
    print("Pythagorean pairs with legs <= %d: %d" % (LIM, len(pairs)))
    found = []
    for a, b, d in pairs:
        for c in range(1, LIM + 1):
            if a * a + c * c in sq and b * b + c * c in sq and d * d + c * c in sq:
                found.append((a, b, c))
    print("perfect cuboids with edges <= %d: %s" % (LIM, found))
    assert found == []
    # Signature approach S-20: elliptic-surface descent.
    # Adjustable assumption A20: a perfect cuboid yields a rational point on a K3 surface
    #   whose rational points can be enumerated by descent.
    print("approach: parametrize Euler bricks, lift to the perfect-cuboid surface, and run a Mordell-Weil sieve")
    print("CONFIRM IF: a perfect cuboid is exhibited, or the surface is proved to have no eligible rational point")
    print("REFUTE IF: the sieve stalls with unresolved residue classes")
    print("does NOT claim: existence or nonexistence - both are open")
    print("OK: %s searched cuboids to edge 300" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usma_magic_square(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    SQS = [i * i for i in range(1, 21)]
    rowset = {}
    for a in SQS:
        for b in SQS:
            for c in SQS:
                rowset.setdefault(a + b + c, set()).add((a, b, c))
    full = []
    for S, rset in rowset.items():
        rows = list(rset)
        for r1 in rows:
            for r2 in rows:
                r3 = (S - r1[0] - r2[0], S - r1[1] - r2[1], S - r1[2] - r2[2])
                if r3 in rset and r1[0] + r2[1] + r3[2] == S and r1[2] + r2[1] + r3[0] == S:
                    full.append((r1, r2, r3))
    def entries(q):
        return [q[0][0], q[0][1], q[0][2], q[1][0], q[1][1], q[1][2], q[2][0], q[2][1], q[2][2]]
    repeated = [q for q in full if len(set(entries(q))) > 1]
    distinct = [q for q in full if len(set(entries(q))) == 9]
    print("magic-sum values examined: %d" % len(rowset))
    print("full 3x3 squares of squares <= 400: %d (%d with repeats, %d with 9 distinct entries)" % (len(full), len(repeated), len(distinct)))
    assert distinct == [], "no 3x3 magic square of 9 distinct squares <= 400"
    # Signature approach S-21: near-miss refinement.
    # Adjustable assumption A21: the Parker near-miss (rows/cols/one diagonal 3051,
    #   other diagonal 4107) sits in a parametrized family whose defect can be driven to zero.
    print("approach: parametrize 3x3 semi-magic squares of squares and minimize the diagonal defect")
    print("CONFIRM IF: a true 3x3 magic square of squares is exhibited, or impossibility is proved")
    print("REFUTE IF: the defect is proved bounded away from zero")
    print("does NOT claim: existence - the Parker square shows how close failure can look")
    print("OK: %s searched magic squares of squares to 400" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usma_singmaster(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    from collections import Counter
    R = 500
    cnt = Counter()
    row = [1]
    for _ in range(R + 1):
        cnt.update(row)
        row = [1] + [row[i] + row[i + 1] for i in range(len(row) - 1)] + [1]
    best = max((c, v) for v, c in cnt.items() if v != 1)
    print("Pascal rows examined: 0..%d" % R)
    print("highest multiplicity (excluding 1): %d for value %d" % best)
    assert best[0] <= 8
    # Signature approach S-22: Diophantine finiteness ascent.
    # Adjustable assumption A22: C(n,k) = C(m,j) with distinct pairs forces a
    #   Catalan-type exponential Diophantine equation with finitely many solutions per value.
    print("approach: show each multiplicity equation reduces to a finite exponential Diophantine problem")
    print("CONFIRM IF: multiplicities are proved uniformly bounded")
    print("REFUTE IF: values of unbounded multiplicity are exhibited")
    print("does NOT claim: boundedness - 3003 appears 8 times and the ceiling is unknown")
    print("OK: %s measured binomial multiplicities to row 500" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usma_hadamard(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    def sylvester(k):
        H = [[1]]
        for _ in range(k):
            n = len(H)
            top = [r + r for r in H]
            bot = [r + [-x for x in r] for r in H]
            H = top + bot
        return H
    for k in range(0, 6):
        n = 2 ** k
        H = sylvester(k)
        ok = True
        for i in range(n):
            Hi = H[i]
            for j in range(n):
                s = 0
                Hj = H[j]
                for t in range(n):
                    s += Hi[t] * Hj[t]
                if s != (n if i == j else 0):
                    ok = False
        print("order %d: Sylvester Hadamard matrix %s" % (n, "verified (H H^T = nI)" if ok else "FAILED"))
        assert ok
    # Signature approach S-23: Williamson-type construction ascent.
    # Adjustable assumption A23: every multiple of 4 admits a Williamson or cocyclic construction.
    print("approach: extend cocyclic and Williamson constructions to cover the open orders (668 is smallest)")
    print("CONFIRM IF: a Hadamard matrix is exhibited for every order divisible by 4")
    print("REFUTE IF: one multiple of 4 is proved to admit no Hadamard matrix")
    print("does NOT claim: the conjecture - order 668 alone is still open")
    print("OK: %s verified Sylvester Hadamard matrices to order 32" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usma_lonely_runner(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    def dist(x):
        return abs(x - round(x))
    G = 40000
    for speeds in ([1, 2], [1, 2, 3], [1, 2, 3, 4]):
        n = len(speeds)
        best = 0.0
        for g in range(G):
            t = g / G
            m = min(dist(t * v) for v in speeds)
            if m > best:
                best = m
        target = 1.0 / (n + 1)
        print("runners=%d speeds=%s: best loneliness %.5f (need >= %.5f)" % (n + 1, speeds, best, target))
        assert best >= target - 1.0 / G - 1e-9
    # Signature approach S-24: view-obstruction ascent.
    # Adjustable assumption A24: the lonely time can be found in a structured
    #   set of rationals with small denominators.
    print("approach: reduce to a covering problem on the torus and apply the Beck-Spencer method")
    print("CONFIRM IF: every set of n+1 speeds admits a lonely time")
    print("REFUTE IF: one speed set is proved to admit no lonely time")
    print("does NOT claim: the conjecture - verified here for small fields, open in general")
    print("OK: %s found lonely times by grid search" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usma_inscribed_square(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    def check_square(verts, curve):
        for x, y in verts:
            assert abs(curve(x, y) - 1.0) < 1e-9, "vertex off the curve"
        def d(p, q):
            return math.hypot(p[0] - q[0], p[1] - q[1])
        s0 = d(verts[0], verts[1])
        for k in range(1, 4):
            assert abs(d(verts[k], verts[(k + 1) % 4]) - s0) < 1e-9, "not equilateral"
        assert abs(d(verts[0], verts[2]) - d(verts[1], verts[3])) < 1e-9, "diagonals differ"
        assert abs(d(verts[0], verts[2]) - s0 * math.sqrt(2)) < 1e-9, "not a square"
        return s0
    # unit circle: rotation invariance gives inscribed squares at every angle
    for deg in (0, 15, 30, 45, 60, 75):
        th = math.radians(deg)
        verts = [(math.cos(th + k * math.pi / 2), math.sin(th + k * math.pi / 2)) for k in range(4)]
        check_square(verts, lambda x, y: x * x + y * y)
    print("unit circle: inscribed squares verified at 6 rotations")
    # ellipse x^2/4 + y^2 = 1: the 45-degree centered square works
    a, b = 2.0, 1.0
    th = math.pi / 4
    r = 1.0 / math.sqrt((math.cos(th) / a) ** 2 + (math.sin(th) / b) ** 2)
    verts = [(r * math.cos(th + k * math.pi / 2), r * math.sin(th + k * math.pi / 2)) for k in range(4)]
    s0 = check_square(verts, lambda x, y: (x / a) ** 2 + (y / b) ** 2)
    print("ellipse a=2 b=1: 45-degree inscribed square verified, side=%.6f" % s0)
    # Signature approach S-25: topological degree ascent.
    # Adjustable assumption A25: the square-inscribing map on curve quadruples has
    #   nonzero degree for every Jordan curve, forcing a zero.
    print("approach: define a test map on inscribed quadrilaterals; prove its degree is nonzero")
    print("CONFIRM IF: every Jordan curve is proved to inscribe a square")
    print("REFUTE IF: one Jordan curve is proved to inscribe no square")
    print("does NOT claim: the full conjecture - smooth curves are settled, rough ones are not")
    print("OK: %s inscribed squares in an ellipse" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usma_chromatic_plane(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    edges = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3),
             (0, 4), (0, 5), (4, 5), (4, 6), (5, 6),
             (3, 6)]
    n = 7
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    coloring = [0] * n
    found = []
    def bt(v):
        if found:
            return
        if v == n:
            found.append(tuple(coloring))
            return
        for c in range(3):
            if all(coloring[u] != c for u in adj[v] if u < v):
                coloring[v] = c
                bt(v + 1)
    bt(0)
    print("Moser spindle: 7 vertices, %d edges" % len(edges))
    print("3-colorings: %d" % len(found))
    assert found == []
    four = [0, 1, 2, 0, 1, 2, 3]
    for u, v in edges:
        assert four[u] != four[v]
    print("4-coloring exhibited: %s" % four)
    # Signature approach S-26: unit-distance graph ascent.
    # Adjustable assumption A26: the de Grey 5-chromatic construction extends by
    #   spindle-chaining to force 6, then 7.
    print("approach: chain Moser spindles into larger unit-distance graphs of higher chromatic number")
    print("CONFIRM IF: the chromatic number of the plane is pinned to exactly 5, 6, or 7 by construction")
    print("REFUTE IF: a unit-distance graph needing 8 colors is exhibited (would break the hexagon tiling bound)")
    print("does NOT claim: the exact number - it is 5, 6, or 7, and nobody knows which")
    print("OK: %s proved the Moser spindle needs 4 colors" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usma_pi_normal(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    from decimal import Decimal, getcontext
    getcontext().prec = 1250
    D = Decimal
    C = D(640320)
    s = D(0)
    for k in range(95):
        num = D(math.factorial(6 * k)) * D(13591409 + 545140134 * k)
        den = D(math.factorial(3 * k)) * D(math.factorial(k) ** 3) * (D(640320) ** (3 * k))
        term = num / den
        s += -term if k % 2 else term
    pi = D(1) / (D(12) * s / (C * C.sqrt()))
    txt = format(pi, 'f')
    intpart, _, frac = txt.partition('.')
    assert intpart == '3' and frac[:10] == '1415926535'
    digits = [int(ch) for ch in frac[:1000]]
    counts = [0] * 10
    for d in digits:
        counts[d] += 1
    chi2 = sum((c - 100.0) ** 2 / 100.0 for c in counts)
    print("first 1000 decimal digits of pi: digit counts %s" % counts)
    print("chi-square vs uniform (9 df): %.2f" % chi2)
    assert chi2 < 30.0
    # Signature approach S-27: finite-state normality ascent.
    # Adjustable assumption A27: the BBP digit-extraction formula exposes enough
    #   pseudorandom structure to force equidistribution.
    print("approach: prove the BBP series for pi behaves like a normal number generator")
    print("CONFIRM IF: pi is proved normal in some base")
    print("REFUTE IF: some digit is proved to occur with the wrong frequency")
    print("does NOT claim: normality - a thousand digits passing chi-square proves nothing")
    print("OK: %s tested pi digits for uniformity" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usma_abc(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    from array import array
    N = 1500
    spf = array('I', range(N + 1))
    for i in range(2, int(math.isqrt(N)) + 1):
        if spf[i] == i:
            for j in range(i * i, N + 1, i):
                if spf[j] == j:
                    spf[j] = i
    def rad(n):
        r = 1
        while n > 1:
            p = spf[n]
            r *= p
            while n % p == 0:
                n //= p
        return r
    R = [0] * (N + 1)
    for i in range(1, N + 1):
        R[i] = rad(i)
    best = (0.0, None)
    over14 = 0
    for a in range(1, N):
        ra = R[a]
        for b in range(a + 1, N - a):
            if math.gcd(a, b) != 1:
                continue
            c = a + b
            q = math.log(c) / math.log(ra * R[b] * R[c])
            if q > 1.4:
                over14 += 1
            if q > best[0]:
                best = (q, (a, b, c))
    print("abc triples c <= %d: max quality %.4f at %s" % (N, best[0], best[1]))
    print("triples with quality > 1.4: %d" % over14)
    assert over14 >= 1
    assert best[0] < 1.63, "quality record is 1.6299; nothing here may exceed it"
    # Signature approach S-28: Szpiro-discriminant ascent.
    # Adjustable assumption A28: the abc inequality follows from a discriminant
    #   bound on the associated Frey-Hellegouarch elliptic curve.
    print("approach: translate abc into Szpiro's conjecture on elliptic discriminants and prove it there")
    print("CONFIRM IF: a refereed proof of abc (or Szpiro) is accepted")
    print("REFUTE IF: triples of arbitrarily high quality are exhibited")
    print("does NOT claim: a proof - the claimed IUTT proof is not accepted; abc stays open")
    print("OK: %s searched abc triples to c=1500" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usma_riemann(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    N = 1000000
    primes = _sieve(N)
    is_p = bytearray(b'\\x00') * (N + 1)
    for p in primes:
        is_p[p] = 1
    pic = [0] * (N + 1)
    c = 0
    for i in range(N + 1):
        c += is_p[i]
        pic[i] = c
    def _simpson(a, b, M):
        h = (b - a) / M
        tot = 0.0
        for i in range(M + 1):
            t = a + i * h
            w = 1.0 if i == 0 or i == M else (4.0 if i % 2 == 1 else 2.0)
            tot += w / math.log(t)
        return tot * h / 3.0
    def li(x):
        # split the integral: the integrand moves fast near 2, slowly later
        return 1.0451637801174929 + _simpson(2.0, 20.0, 3600) + _simpson(20.0, float(x), 200000)
    worst = 0.0
    for x in (2657, 10000, 100000, 1000000):
        diff = abs(pic[x] - li(x))
        bound = math.sqrt(x) * math.log(x) / (8 * math.pi)
        r = diff / bound
        print("x=%d pi=%d li=%.1f |diff|=%.1f Schoenfeld-bound=%.1f ratio=%.3f" % (x, pic[x], li(x), diff, bound, r))
        assert diff < bound, "Schoenfeld corollary check failed at x=%d" % x
        worst = max(worst, r)
    print("max |pi - li| / bound: %.3f" % worst)
    # Signature approach S-29: zero-free region ascent.
    # Adjustable assumption A29: an explicit zero-free region plus Turing's method
    #   can be pushed to cover all heights.
    print("approach: extend the verified zero-free region and the Turing zero-count until no room for off-line zeros remains")
    print("CONFIRM IF: every nontrivial zero is proved to lie on the critical line")
    print("REFUTE IF: one zero with real part != 1/2 is exhibited")
    print("does NOT claim: RH - checking a corollary is not proving the hypothesis")
    print("OK: %s checked the Schoenfeld bound to 10^6" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usma_p_vs_np(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    import random
    random.seed(12345)
    def rand_cnf(n, m, k):
        clauses = []
        for _ in range(m):
            cl = set()
            while len(cl) < k:
                cl.add((random.randrange(n), random.randrange(2)))
            clauses.append(list(cl))
        return clauses
    def brute_ops(n, clauses):
        # bitmask clauses: satisfied iff (mask & pos) or (~mask & neg)
        full = (1 << n) - 1
        packed = []
        for cl in clauses:
            pos = neg = 0
            for v, b in cl:
                if b:
                    pos |= 1 << v
                else:
                    neg |= 1 << v
            packed.append((pos, neg))
        ops = 0
        sat = False
        for mask in range(1 << n):
            ok = True
            nmask = (~mask) & full
            for pos, neg in packed:
                ops += 1
                if not ((mask & pos) or (nmask & neg)):
                    ok = False
                    break
            if ok:
                sat = True
                break
        return sat, ops
    counts = []
    for n in (10, 12, 14, 16):
        clauses = rand_cnf(n, int(4.3 * n), 3)
        sat, ops = brute_ops(n, clauses)
        counts.append(ops)
        print("3-SAT n=%d: %s, clause evaluations=%d" % (n, "SAT" if sat else "UNSAT", ops))
    assert counts[3] > 10 * counts[0], "expected exponential signature in brute force"
    # 2-SAT is polynomial: implication graph + Kosaraju SCC
    def two_sat(n, clauses):
        N2 = 2 * n
        g = [[] for _ in range(N2)]
        gr = [[] for _ in range(N2)]
        for (v1, b1), (v2, b2) in clauses:
            a, b = 2 * v1 + (0 if b1 else 1), 2 * v2 + (0 if b2 else 1)
            for x, y in ((a ^ 1, b), (b ^ 1, a)):
                g[x].append(y)
                gr[y].append(x)
        seen = [False] * N2
        order = []
        for s in range(N2):
            if seen[s]:
                continue
            stack = [(s, 0)]
            while stack:
                v, i = stack[-1]
                seen[v] = True
                nxt = None
                for j in range(i, len(g[v])):
                    w = g[v][j]
                    if not seen[w]:
                        nxt = (w, j)
                        break
                if nxt is None:
                    order.append(v)
                    stack.pop()
                else:
                    stack[-1] = (v, nxt[1] + 1)
                    stack.append((nxt[0], 0))
        comp = [-1] * N2
        label = 0
        for v in reversed(order):
            if comp[v] != -1:
                continue
            stack = [v]
            comp[v] = label
            while stack:
                u = stack.pop()
                for w in gr[u]:
                    if comp[w] == -1:
                        comp[w] = label
                        stack.append(w)
            label += 1
        asg = []
        for v in range(n):
            if comp[2 * v] == comp[2 * v + 1]:
                return None
            asg.append(comp[2 * v] > comp[2 * v + 1])
        return asg
    agree = 0
    for trial in range(10):
        n = 12
        clauses = rand_cnf(n, 30, 2)
        sat_b, _ = brute_ops(n, clauses)
        asg = two_sat(n, clauses)
        assert (asg is not None) == sat_b, "2-SAT solver disagrees with brute force"
        if asg is not None:
            for cl in clauses:
                assert any(asg[v] == bool(b) for v, b in cl)
        agree += 1
    print("2-SAT solver agreed with brute force on %d instances; assignments verified" % agree)
    # Signature approach S-30: circuit lower-bound ascent.
    # Adjustable assumption A30: SAT needs superpolynomial circuits; prove it by
    #   extending Williams-style non-uniform lower bounds.
    print("approach: prove superpolynomial circuit lower bounds for an NP-complete problem")
    print("CONFIRM IF: P != NP is proved, or P = NP is proved by exhibiting a polynomial algorithm")
    print("REFUTE IF: the relativization and natural-proofs barriers are shown insurmountable this way")
    print("does NOT claim: a resolution - this is the deepest open problem in computer science")
    print("OK: %s measured SAT scaling and verified a 2-SAT solver" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usma_navier_stokes(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    N = 256
    nu = 0.05
    dx = 2 * math.pi / N
    dt = 0.0005
    steps = 1200
    u = [math.sin(i * dx) + 0.4 * math.sin(2 * i * dx + 1.0) for i in range(N)]
    def energy(v):
        return sum(x * x for x in v) * dx
    E0 = energy(u)
    max_slope = 0.0
    for _ in range(steps):
        un = [0.0] * N
        for i in range(N):
            im = (i - 1) % N
            ip = (i + 1) % N
            ux = (u[ip] - u[im]) / (2 * dx)
            uxx = (u[ip] - 2 * u[i] + u[im]) / (dx * dx)
            un[i] = u[i] + dt * (-u[i] * ux + nu * uxx)
        u = un
        for i in range(N):
            s = abs((u[(i + 1) % N] - u[(i - 1) % N]) / (2 * dx))
            if s > max_slope:
                max_slope = s
    E1 = energy(u)
    print("1D viscous Burgers: E(0)=%.4f E(T)=%.4f max|u_x|=%.3f" % (E0, E1, max_slope))
    assert E1 < E0, "viscosity must dissipate energy"
    assert max_slope < 5.0, "solution stayed smooth in this run"
    # Signature approach S-31: critical-norm control ascent.
    # Adjustable assumption A31: a scale-critical quantity stays bounded along
    #   every finite-energy 3D flow, ruling out blowup.
    print("approach: find a monotone critical quantity for 3D Navier-Stokes that forbids finite-time blowup")
    print("CONFIRM IF: global smooth solutions are proved for all smooth finite-energy data (or a blowup is exhibited)")
    print("REFUTE IF: the critical quantity is shown to admit concentration")
    print("does NOT claim: 3D regularity - the 1D model is smooth; 3D is the open problem")
    print("OK: %s simulated viscous Burgers with energy decay" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usma_bsd(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    PLIM = 2000
    primes = _sieve(PLIM)
    def legendre(a, p):
        a %= p
        if a == 0:
            return 0
        return 1 if pow(a, (p - 1) // 2, p) == 1 else -1
    def ap_list(A, B):
        ap = {}
        disc_bad = set()
        for p in primes:
            s = 0
            for x in range(p):
                s += legendre(x * x * x + A * x + B, p)
            ap[p] = -s
            if (4 * A * A * A + 27 * B * B) % p == 0:
                disc_bad.add(p)
        return ap, disc_bad
    def l_partial(A, B, N):
        ap, bad = ap_list(A, B)
        apk = {}
        for p in primes:
            if p > N:
                break
            pw = [1, ap[p]]
            pp = p
            while pp <= N // p:
                pp *= p
                if p in bad:
                    pw.append(pw[-1] * ap[p])
                else:
                    pw.append(ap[p] * pw[-1] - p * pw[-2])
            apk[p] = pw
        an = [0] * (N + 1)
        an[1] = 1
        for p in primes:
            if p > N:
                break
            pw = apk[p]
            new = [0] * (N + 1)
            for n in range(1, N + 1):
                if an[n] == 0:
                    continue
                m, k = n, 0
                while m <= N and k < len(pw):
                    new[m] += an[n] * pw[k]
                    if m > N // p:
                        break
                    m *= p
                    k += 1
            an = new
        return sum(an[n] / n for n in range(1, N + 1))
    s0 = l_partial(-1, 0, 1500)
    s1 = l_partial(0, -2, 1500)
    print("partial L(E0,1), E0: y^2 = x^3 - x (rank 0): %.4f" % s0)
    print("partial L(E1,1), E1: y^2 = x^3 - 2 (rank 1): %.4f" % s1)
    assert s0 > 0.3, "nonvanishing partial sum, consistent with rank 0"
    assert abs(s1) < 0.25, "near-vanishing partial sum, consistent with rank 1"
    # Signature approach S-32: Heegner-point descent ascent.
    # Adjustable assumption A32: the Gross-Zagier / Kolyvagin machinery extends
    #   from analytic rank <= 1 to all ranks.
    print("approach: extend Heegner-point Euler systems to prove rank = analytic order of vanishing in general")
    print("CONFIRM IF: rank E(Q) is proved to equal ord_{s=1} L(E,s) for every elliptic curve")
    print("REFUTE IF: one curve is found with rank != analytic order of vanishing")
    print("does NOT claim: BSD - partial sums suggest; only proof decides")
    print("OK: %s compared L-values with ranks" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usma_hodge(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # f = y^3 + x^2 y + x^3, g = y^2 + x y + x^2 ; resultant in y via Sylvester + Bareiss
    def sylvester_det(t):
        f = [t ** 3, t ** 2, 0, 1]
        g = [t ** 2, t, 1]
        M = [[0] * 5 for _ in range(5)]
        for i in range(2):
            for j in range(4):
                M[i][i + j] = f[j]
        for i in range(3):
            for j in range(3):
                M[2 + i][i + j] = g[j]
        n = 5
        A = [row[:] for row in M]
        prev = 1
        for k in range(n - 1):
            if A[k][k] == 0:
                piv_r = None
                for r in range(k + 1, n):
                    if A[r][k] != 0:
                        piv_r = r
                        break
                if piv_r is None:
                    return 0
                A[k], A[piv_r] = A[piv_r], A[k]
            piv = A[k][k]
            for i in range(k + 1, n):
                for j in range(k + 1, n):
                    A[i][j] = (A[i][j] * piv - A[i][k] * A[k][j]) // prev
            prev = piv
        return A[n - 1][n - 1]
    vals = [sylvester_det(t) for t in range(8)]
    print("Res_y(f,g) at x=0..7: %s" % vals)
    d = vals[:]
    deg = 0
    while any(v != 0 for v in d):
        d = [d[i + 1] - d[i] for i in range(len(d) - 1)]
        deg += 1
    print("degree of resultant: %d (Bezout predicts 3*2 = 6)" % (deg - 1))
    assert deg - 1 == 6
    # Signature approach S-33: standard-conjectures descent.
    # Adjustable assumption A33: the Hodge conjecture follows from the standard
    #   conjectures on algebraic cycles, attacked one codimension at a time.
    print("approach: prove the standard conjectures, which imply Hodge; start with divisors (known) and climb")
    print("CONFIRM IF: every rational Hodge class is proved algebraic")
    print("REFUTE IF: one rational Hodge class is proved non-algebraic")
    print("does NOT claim: Hodge - Bezout counts intersections; the conjecture is the leap beyond")
    print("OK: %s verified Bezout via the resultant" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usma_yang_mills(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    import random
    random.seed(20261017)
    def qmul(a, b):
        w1, x1, y1, z1 = a
        w2, x2, y2, z2 = b
        return (w1*w2 - x1*x2 - y1*y2 - z1*z2,
                w1*x2 + x1*w2 + y1*z2 - z1*y2,
                w1*y2 - x1*z2 + y1*w2 + z1*x2,
                w1*z2 + x1*y2 - y1*x2 + z1*w2)
    def qconj(a):
        w, x, y, z = a
        return (w, -x, -y, -z)
    def qrand():
        v = [random.gauss(0, 1) for _ in range(4)]
        nrm = math.sqrt(sum(c * c for c in v))
        return tuple(c / nrm for c in v)
    def wloop(us):
        u1, u2, u3, u4 = us
        w = qmul(qmul(qmul(u1, u2), u3), u4)
        return w[0]
    us = [qrand() for _ in range(4)]
    w0 = wloop(us)
    gs = [qrand() for _ in range(4)]
    us2 = [qmul(qmul(gs[0], us[0]), qconj(gs[1])),
           qmul(qmul(gs[1], us[1]), qconj(gs[2])),
           qmul(qmul(gs[2], us[2]), qconj(gs[3])),
           qmul(qmul(gs[3], us[3]), qconj(gs[0]))]
    w1 = wloop(us2)
    print("Wilson loop before gauge transform: %.12f" % w0)
    print("Wilson loop after  gauge transform: %.12f" % w1)
    assert abs(w0 - w1) < 1e-9, "gauge invariance is the prerequisite of any mass-gap proof"
    S_rand = 1 - w0
    print("plaquette action, random config: %.4f; trivial config: 0.0000" % S_rand)
    assert S_rand > 0.01
    # Signature approach S-34: constructive mass-gap ascent.
    # Adjustable assumption A34: the lattice Yang-Mills measure has a positive
    #   spectral gap uniformly in the lattice spacing, surviving the continuum limit.
    print("approach: construct the continuum quantum Yang-Mills theory and prove its Hamiltonian has a gap above the vacuum")
    print("CONFIRM IF: a quantum Yang-Mills theory is constructed with a proved mass gap Delta > 0")
    print("REFUTE IF: the gap is proved to close (against all physical expectation)")
    print("does NOT claim: the Clay prize - gauge invariance checks out; the gap is the open mountain")
    print("OK: %s verified SU(2) gauge invariance" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "goldbach": demo_usma_goldbach,
    "collatz": demo_usma_collatz,
    "twin_prime": demo_usma_twin_prime,
    "odd_perfect": demo_usma_odd_perfect,
    "mersenne": demo_usma_mersenne,
    "sophie_germain": demo_usma_sophie_germain,
    "beal": demo_usma_beal,
    "legendre": demo_usma_legendre,
    "brocard_ramanujan": demo_usma_brocard_ramanujan,
    "three_cubes": demo_usma_three_cubes,
    "gilbreath": demo_usma_gilbreath,
    "moving_sofa": demo_usma_moving_sofa,
    "near_square": demo_usma_near_square,
    "andrica": demo_usma_andrica,
    "oppermann": demo_usma_oppermann,
    "cramer": demo_usma_cramer,
    "lehmer": demo_usma_lehmer,
    "odd_weird": demo_usma_odd_weird,
    "aliquot": demo_usma_aliquot,
    "perfect_cuboid": demo_usma_perfect_cuboid,
    "magic_square": demo_usma_magic_square,
    "singmaster": demo_usma_singmaster,
    "hadamard": demo_usma_hadamard,
    "lonely_runner": demo_usma_lonely_runner,
    "inscribed_square": demo_usma_inscribed_square,
    "chromatic_plane": demo_usma_chromatic_plane,
    "pi_normal": demo_usma_pi_normal,
    "abc": demo_usma_abc,
    "riemann": demo_usma_riemann,
    "p_vs_np": demo_usma_p_vs_np,
    "navier_stokes": demo_usma_navier_stokes,
    "bsd": demo_usma_bsd,
    "hodge": demo_usma_hodge,
    "yang_mills": demo_usma_yang_mills,
}
