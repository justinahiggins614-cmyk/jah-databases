#!/usr/bin/env python3
"""Build the Combinatorics field databases for JAH Databases (field #17, taxonomy order).

Verified 2026-10-17: NO database covers combinatorics as a discipline.
- 'mathematics-public' / 'mathematics-signature' / 'everything-mathematics':
  survey-level topic cards (combinatorics as one card among dozens of
  branches) - no teaching depth.
- 'mathematics-study' / 'mathematics-study-published': curriculum /
  qualification / assessment cards ABOUT combinatorics pedagogy
  ("Methods - Combinatorics (case analysis)") - not the discipline.
- 'scientific-formulas': formula CARDS (bare binomial / permutation /
  combination formulas) as reference, with no teaching, no ladder, no
  how-it-works, no demos. Reference cards are not discipline coverage
  (task instruction: formula cards do NOT count).
- 'graph-databases' / 'graph-databases-signature': graph DATABASES
  (storage/query technology) - not graph theory as counting.
- 'cryptography', 'math', 'math-word-problems', 'hard-equations',
  'equations': puzzles/equation records - not combinatorics teaching.
- Whole-system dedupe index (256 shards): zero combinatorics-discipline
  titles exist. Fields #12-16 shard indexes (climatology,
  atmospheric-science, hydrology, meteorology, calculus - the gate index
  predates them) checked directly: zero combinatorics-relevant titles.

So this build creates two NEW databases:

  combinatorics             - The Combinatorics Database
                              (public-harvest: real, fact-checked
                              combinatorics)
  combinatorics-signature   - The Combinatorics Signature Database
                              (his original Signature interpretation;
                              src signature, titles suffixed
                              " (Signature Edition)", never presented
                              as authentic public record)

36 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

Every record: description + how-it-works + key points + requirements +
standards + citations + working demonstration code (real, runnable,
stdlib-only Python; machine-executed OK). Combinatorics demos: counting
functions, Pascal's triangle, stars-and-bars enumeration, inclusion-
exclusion, derangements, Stirling numbers, recurrence solvers, generating
function series checks, Catalan structures, Prufer codes, Ramsey brute
force, Fano plane verification, Burnside's lemma, Nim strategy.

Subtitle disambiguation (fields #13-17 pattern): where a bare formula card
exists in scientific-formulas, discipline titles carry teaching-focused
subtitles, e.g. "Permutations: Counting Ordered Arrangements" and
"Combinations: Choosing Without Order" rather than bare "Permutation" or
"Combination" cards.

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
# main repo (256 shards; titles from fields #12-16 cross-checked directly
# against their shard indexes in jah-databases-data-1 since the gate index
# predates them - subtitle disambiguation used throughout).
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_combinatorics import ENTRIES, SIG_TAIL

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature interpretation of combinatorics: "
                "clearly labeled Signature-made, never presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked combinatorics: what combinatorics is; "
                "the addition and multiplication principles; the pigeonhole principle; "
                "permutations; combinations; Pascal's triangle and the binomial theorem; "
                "permutations with repetition and multinomial coefficients; combinations "
                "with repetition (stars and bars); binomial identities; inclusion-exclusion; "
                "derangements; the bijection principle; double counting; integer partitions; "
                "Stirling numbers of the second and first kinds; lattice paths and the "
                "reflection principle; recurrence relations; linear recurrences and the "
                "characteristic equation; ordinary and exponential generating functions; "
                "the twelvefold way; Catalan numbers; Bell numbers; Euler's partition "
                "theorems; graph counting and the handshaking lemma; trees and Cayley's "
                "formula; Eulerian trails and Hamiltonian cycles; Ramsey theory; block "
                "designs and the Fano plane; Latin squares; combinatorial games; extremal "
                "combinatorics and Turan's theorem; the probabilistic method; Polya "
                "enumeration; algebraic combinatorics and symmetric functions, organized "
                "in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations (what combinatorics "
              "is, addition/multiplication principles, pigeonhole principle, permutations, "
              "combinations, Pascal's triangle and the binomial theorem, permutations with "
              "repetition, stars and bars) -> Compounded (binomial identities, "
              "inclusion-exclusion, derangements, bijection principle, double counting, "
              "integer partitions, Stirling numbers of both kinds, lattice paths, "
              "recurrences, characteristic equations, ordinary and exponential generating "
              "functions, the twelvefold way, Catalan numbers) -> Advanced (Bell numbers, "
              "Euler's partition theorems, graph counting, trees and Cayley, Eulerian "
              "and Hamiltonian routes, Ramsey theory, block designs, Latin squares, "
              "combinatorial games, extremal combinatorics, the probabilistic method, "
              "Polya enumeration, symmetric functions).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search permutations, combinations, pigeonhole, inclusion-exclusion, Stirling, Catalan, Ramsey, generating functions...",
        "chat_ph": "Ask about combinatorics...",
        "archive_blurb": ("Seeded %s combinatorics records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled structural combinatorics studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about combinatorics - from permutations and combinations to generating functions, Ramsey theory, and Polya enumeration." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "combinatorics-study", "gen_demo_kind": "combinatorics-demo",
        "source": source,
    }

CIT_PUB = "Combinatorics (peer-reviewed literature and standard textbooks)."
CIT_SIG = CIT_PUB + " " + SIG_TAIL

DBCFG = {}
DBCFG["combinatorics"] = _cfg(
    "combinatorics", "The Combinatorics Database",
    "Real, fact-checked combinatorics: the discipline from counting principles, "
    "permutations and combinations through partitions, recurrences, generating "
    "functions, graph counting, Ramsey theory, designs, and symmetric functions "
    "- taught progressively along the ladder.",
    "combinatorics record", "JAH-COMB-", "JAH Combinatorics Archivist",
    "combinatorics archivist - what combinatorics is, counting principles, "
    "pigeonhole, permutations, combinations, binomial theorem, repetition, "
    "stars and bars, binomial identities, inclusion-exclusion, derangements, "
    "bijections, double counting, partitions, Stirling numbers, lattice paths, "
    "recurrences, generating functions, twelvefold way, Catalan and Bell "
    "numbers, graph counting, trees, Eulerian/Hamiltonian routes, Ramsey "
    "theory, designs, Latin squares, games, extremal combinatorics, "
    "probabilistic method, Polya enumeration, symmetric functions; teaching "
    "progressively along the ladder from foundations through compounded to "
    "advanced; answers from many angles - definition, example, analogy, "
    "application, history, math, how-to - using only the system's own "
    "archive data",
    CIT_PUB, "public")
DBCFG["combinatorics-signature"] = _cfg(
    "combinatorics-signature", "The Combinatorics Signature Database",
    "His original Signature interpretation of combinatorics: the full ladder from "
    "counting principles and permutations through partitions, generating functions, "
    "Ramsey theory, and symmetric functions, reframed as Signature science. Clearly "
    "labeled Signature-made, never presented as authentic public record.",
    "combinatorics record", "JAH-COMBS-", "JAH Combinatorics Archivist (Signature)",
    "combinatorics archivist - Signature editions: his original Signature interpretation "
    "of combinatorics, clearly labeled Signature-made and never presented as authentic "
    "public record; teaches progressively along the ladder from foundations through "
    "compounded to advanced; answers from many angles - definition, example, analogy, "
    "application, history, math, how-to - using only the system's own archive data",
    CIT_SIG, "signature")

base.DBCFG = DBCFG
# ---------------------------------------------------------------- demos
# Every demo is real, runnable, stdlib-only Python performing the actual
# combinatorics computation for its record. All are machine-executed by main().

_PREAMBLE = "import math\nimport itertools\n"

def _wrap(name, rid, group, body):
    return (base._hdr(name, rid, group) + _PREAMBLE + body.replace("NAME", json.dumps(name)))

def demo_comb_branches(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
HOUSES = {
    "enumerative combinatorics": "counting things: permutations, combinations, partitions, recurrences, generating functions",
    "extremal combinatorics": "largest/smallest structures avoiding a pattern: Turan, Ramsey, Erdos-Ko-Rado",
    "algebraic combinatorics": "structure behind counting: symmetries, Polya, symmetric functions, representation theory",
}
def main():
    assert len(HOUSES) == 3
    assert "permutations" in HOUSES["enumerative combinatorics"]
    for house, focus in HOUSES.items():
        print("%-26s -> %s" % (house, focus))
    print("one question binds them: how many - answered exactly, never approximately")
    print("rule: model the objects, pick the principle, verify by a second count")
    print("OK: %s mapped the discipline" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_comb_add_mult(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # product rule: 4-digit PIN, 10 options per digit, independent stages
    pins = 10 ** 4
    assert pins == 10000
    print("product rule: 4-digit PINs = 10^4 = %d" % pins)
    # sum rule: 5 mains or 3 desserts, disjoint alternatives
    meals = 5 + 3
    assert meals == 8
    print("sum rule: 5 mains or 3 desserts = %d choices" % meals)
    # staged product: license plate, 3 letters then 3 digits
    plates = 26 ** 3 * 10 ** 3
    assert plates == 17576000
    print("staged product: 3 letters + 3 digits = 26^3 * 10^3 = %d plates" % plates)
    # audit: brute-force check on a tiny staged count
    tiny = [(a, b) for a in range(3) for b in range(4)]
    assert len(tiny) == 3 * 4
    print("audit: 3 x 4 staged choices enumerated = %d, matches the product" % len(tiny))
    print("rule: independent stages multiply, disjoint alternatives add - then audit by enumeration")
    print("OK: %s applied the two rules" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_comb_pigeonhole(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # 367 people, 366 possible birthdays -> some birthday repeats
    birthdays = [i % 366 for i in range(367)]
    assert len(set(birthdays)) < len(birthdays)
    print("367 people, 366 birthdays: a repeat is forced (found duplicate day %d)" %
          next(d for d in birthdays if birthdays.count(d) > 1))
    # sock drawer: 10 pairs (types 0-9), draw 11 -> a matching pair
    drawer = list(range(10)) * 2
    drawn = drawer[:11]  # worst case: one of each type, then the 11th matches
    assert len(set(drawn)) < len(drawn)
    print("10 pairs, 11 socks drawn: a matching pair is forced")
    # generalized: k*n + 1 objects into n boxes -> some box holds k + 1
    n, k = 5, 3
    objects = k * n + 1  # 16
    # most even distribution: four boxes get 3, one gets 4 = k+1
    dist = [objects // n + (1 if i < objects % n else 0) for i in range(n)]
    assert sum(dist) == objects and max(dist) == k + 1
    print("generalized: %d objects into %d boxes -> fullest box holds %d = k+1" % (objects, n, max(dist)))
    print("rule: name the pigeons, name the holes, count both - the excess forces the repeat")
    print("OK: %s forced the repeat" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_comb_permutations(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def P(n, k):
    return math.factorial(n) // math.factorial(n - k)
def main():
    assert P(5, 5) == 120
    print("5 distinct books in a row: 5! = 120")
    assert P(10, 3) == 720
    print("president/VP/treasurer from 10: P(10,3) = 720")
    # brute-force audit: ordered 3-selections from {1,2,3,4}
    audit = list(itertools.permutations([1, 2, 3, 4], 3))
    assert len(audit) == P(4, 3) == 24
    print("audit: permutations of 4 choose 3 enumerated = 24 = P(4,3)")
    # growth: 52! has 68 digits
    assert len(str(math.factorial(52))) == 68
    print("52! has %d digits - brute force over shuffles is hopeless" % len(str(math.factorial(52))))
    print("rule: order matters -> product of shrinking options; audit small cases by listing")
    print("OK: %s arranged in order" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_comb_combinations(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    assert math.comb(10, 3) == 120
    print("committee of 3 from 10: C(10,3) = 120")
    # symmetry: choosing k to take = choosing n-k to leave
    assert math.comb(10, 3) == math.comb(10, 7)
    assert math.comb(100, 98) == math.comb(100, 2) == 4950
    print("symmetry: C(10,3) = C(10,7); C(100,98) = C(100,2) = 4950")
    assert math.comb(52, 5) == 2598960
    print("poker hands: C(52,5) = 2,598,960")
    # overcounting-correction audit: ordered selections / orders per set
    ordered = list(itertools.permutations([1, 2, 3, 4, 5], 3))
    assert len(ordered) // math.factorial(3) == math.comb(5, 3) == 10
    print("audit: P(5,3)/3! = 720/6 = 10 = C(5,3)")
    # brute-force subset count
    subs = list(itertools.combinations([1, 2, 3, 4, 5], 2))
    assert len(subs) == math.comb(5, 2) == 10
    print("audit: 2-subsets of a 5-set enumerated = 10")
    print("rule: order irrelevant -> divide ordered counts by k!; symmetry picks the easier k")
    print("OK: %s chose without order" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_comb_pascal_binomial(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def pascal_row(n):
    row = [1]
    for k in range(1, n + 1):
        row.append(row[-1] * (n - k + 1) // k)
    return row
def main():
    # Pascal's recurrence builds rows without factorials
    tri = [[1]]
    for n in range(1, 7):
        prev = tri[-1]
        tri.append([1] + [prev[k - 1] + prev[k] for k in range(1, n)] + [1])
    assert tri[4] == [1, 4, 6, 4, 1]
    print("Pascal row 4: %s" % tri[4])
    for n, row in enumerate(tri):
        assert row == pascal_row(n)
        assert sum(row) == 2 ** n  # row sums: subsets counted by size
    print("row sums: 1, 2, 4, ... row n sums to 2^n (verified to row 6)")
    # binomial theorem: (x+y)^4 expanded two ways
    x, y, n = 2, 3, 4
    lhs = (x + y) ** n
    rhs = sum(math.comb(n, k) * x ** k * y ** (n - k) for k in range(n + 1))
    assert lhs == rhs == 625
    print("binomial theorem: (2+3)^4 = %d = sum C(4,k) 2^k 3^(4-k)" % lhs)
    # single term: coefficient of x^2 in (3x+1)^5
    assert math.comb(5, 2) * 3 ** 2 == 90
    print("term pick: [x^2](3x+1)^5 = C(5,2)*3^2 = 90")
    print("rule: recurrence builds the triangle; 'choose which factors give x' proves the theorem")
    print("OK: %s expanded the binomial" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_comb_perm_rep(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # MISSISSIPPI: 11 letters, I x4, S x4, P x2, M x1
    val = math.factorial(11) // (math.factorial(4) * math.factorial(4) * math.factorial(2))
    assert val == 34650
    print("MISSISSIPPI arrangements: 11!/(4!4!2!) = %d" % val)
    # sequential-choice audit: place the I's, then S's, then P's, then M
    seq = math.comb(11, 4) * math.comb(7, 4) * math.comb(3, 2) * math.comb(1, 1)
    assert seq == 34650
    print("audit: C(11,4)*C(7,4)*C(3,2)*C(1,1) = %d - same count, second route" % seq)
    # unlimited repetition with order: 4-digit PINs
    assert 10 ** 4 == 10000
    print("free refill: 4-digit PINs = 10^4 = 10000")
    # DNA: 8-base sequences over 4 letters
    assert 4 ** 8 == 65536
    print("DNA 8-mers: 4^8 = 65536")
    # tiny brute-force audit: arrangements of AAB
    words = set(itertools.permutations("AAB"))
    assert len(words) == 3  # AAB, ABA, BAA
    assert len(words) == math.factorial(3) // math.factorial(2)
    print("audit: distinct arrangements of AAB = 3 = 3!/2!")
    print("rule: identical types -> divide by type factorials; free refill -> n^k")
    print("OK: %s handled repetition" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_comb_stars_bars(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # 10 identical cookies among 4 children: C(10+4-1, 10)
    assert math.comb(13, 10) == 286
    print("10 identical cookies, 4 children: C(13,10) = 286")
    # stars-and-bars encoding audit: 3 picks from 2 types
    # strings of 3 stars + 1 bar, choose star positions
    encodings = list(itertools.combinations(range(4), 3))
    assert len(encodings) == math.comb(2 + 3 - 1, 3) == 4
    print("audit: 3 stars + 1 bar, star positions C(4,3) = 4 -> multisets {333},{332},{322},{222}")
    # integer solutions: x1+x2+x3 = 5, xi >= 0 -> C(7,2) = 21
    sols = [(a, b, c) for a in range(6) for b in range(6 - a) for c in [5 - a - b]]
    assert len(sols) == math.comb(5 + 3 - 1, 5) == 21
    print("audit: nonnegative solutions to x1+x2+x3=5 enumerated = 21 = C(7,2)")
    # positive solutions: xi >= 1 -> C(5-1, 3-1) = 6
    poss = [(a, b, c) for a in range(1, 6) for b in range(1, 6 - a)
            for c in [5 - a - b] if c >= 1]
    assert len(poss) == math.comb(4, 2) == 6
    print("positive solutions to x1+x2+x3=5: %d = C(4,2)" % len(poss))
    print("rule: identical objects, distinct boxes, order irrelevant -> C(n+k-1,k); shift for positive")
    print("OK: %s placed stars and bars" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_comb_binomial_identities(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # row sum: subsets by size vs. all subsets
    n = 8
    assert sum(math.comb(n, k) for k in range(n + 1)) == 2 ** n == 256
    print("row sum: sum C(8,k) = 256 = 2^8")
    # Vandermonde: split a 12-pool into 5 + 7
    m, nn, r = 5, 7, 4
    lhs = math.comb(m + nn, r)
    rhs = sum(math.comb(m, k) * math.comb(nn, r - k) for k in range(r + 1))
    assert lhs == rhs == 495
    print("Vandermonde: C(12,4) = %d = sum_k C(5,k)C(7,4-k)" % lhs)
    # hockey-stick: diagonal C(2,2)+...+C(6,2) = C(7,3)
    assert sum(math.comb(i, 2) for i in range(2, 7)) == math.comb(7, 3) == 35
    print("hockey-stick: 1+3+6+10+15 = 35 = C(7,3)")
    # absorption / committee-chair: k*C(n,k) = n*C(n-1,k-1)
    nn2, k2 = 10, 3
    assert k2 * math.comb(nn2, k2) == nn2 * math.comb(nn2 - 1, k2 - 1) == 360
    print("committee-chair: 3*C(10,3) = 10*C(9,2) = 360")
    # alternating row sum = 0
    assert sum(((-1) ** k) * math.comb(6, k) for k in range(7)) == 0
    print("alternating sum: sum (-1)^k C(6,k) = 0")
    print("rule: both sides count one set - find it, count it twice")
    print("OK: %s proved the identities" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_comb_inclusion_exclusion(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    N = 1000
    # divisible by 2, 3, or 5: add singles, subtract pairs, add triple
    singles = N // 2 + N // 3 + N // 5
    pairs = N // 6 + N // 10 + N // 15
    triple = N // 30
    val = singles - pairs + triple
    assert val == 734, val
    brute = sum(1 for i in range(1, N + 1) if i % 2 == 0 or i % 3 == 0 or i % 5 == 0)
    assert brute == val
    print("<= 1000 divisible by 2/3/5: %d (brute force agrees)" % val)
    # Euler totient via inclusion-exclusion on prime divisors of 30 (exact integer steps)
    n = 30
    phi = n
    for p in (2, 3, 5):
        phi = phi // p * (p - 1)
    assert phi == 8
    brute_phi = sum(1 for i in range(1, n + 1) if math.gcd(i, n) == 1)
    assert brute_phi == 8
    print("phi(30) = 30*(1/2)*(2/3)*(4/5) = 8 (brute force agrees)")
    # onto functions: 3-set -> 2-set = 2^3 - 2 = 6
    onto = sum(((-1) ** i) * math.comb(2, i) * (2 - i) ** 3 for i in range(3))
    assert onto == 6
    brute_onto = sum(1 for f in itertools.product([0, 1], repeat=3) if set(f) == {0, 1})
    assert brute_onto == onto
    print("onto functions {1,2,3} -> {a,b}: %d (inclusion-exclusion = brute force)" % onto)
    print("rule: add singles, subtract pairs, add triples - every element counted exactly once")
    print("OK: %s un-overlapped the union" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_comb_derangements(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def derangements_upto(n):
    d = [0] * (n + 1)
    if n >= 1: d[1] = 0
    if n >= 2: d[2] = 1
    for i in range(3, n + 1):
        d[i] = (i - 1) * (d[i - 1] + d[i - 2])
    return d
def main():
    d = derangements_upto(10)
    assert d[1:7] == [0, 1, 2, 9, 44, 265]
    print("derangements: !1..!6 = %s" % d[1:7])
    # brute-force audit: permutations of 4 with no fixed points
    brute = [p for p in itertools.permutations([1, 2, 3, 4])
             if all(p[i] != i + 1 for i in range(4))]
    assert len(brute) == d[4] == 9
    print("audit: derangements of 4 enumerated = 9")
    # closed form: !n = n! * sum (-1)^k / k!
    n = 6
    closed = round(math.factorial(n) * sum(((-1) ** k) / math.factorial(k) for k in range(n + 1)))
    assert closed == d[n]
    print("closed form: 6! * sum (-1)^k/k! rounds to %d" % closed)
    # limit: !n / n! -> 1/e
    ratio = d[10] / math.factorial(10)
    assert abs(ratio - 1 / math.e) < 1e-6
    print("!10/10! = %.6f -> 1/e = %.6f" % (ratio, 1 / math.e))
    print("rule: recurrence for exact values, inclusion-exclusion for the form, 1/e for large n")
    print("OK: %s deranged completely" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_comb_bijection(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # subsets of {1,2,3,4} <-> binary strings: characteristic vectors
    universe = [1, 2, 3, 4]
    pairs = []
    for mask in range(16):
        subset = tuple(u for i, u in enumerate(universe) if mask & (1 << i))
        pairs.append((subset, mask))
    masks = [m for _, m in pairs]
    assert len(set(masks)) == 16 and set(masks) == set(range(16))
    print("bijection: 16 subsets <-> 16 binary strings, one-to-one both ways")
    # complement bijection: 2-subsets <-> 4-subsets of a 6-set
    six = set(range(6))
    subs2 = list(itertools.combinations(range(6), 2))
    images = [tuple(sorted(six - set(s))) for s in subs2]
    assert len(subs2) == math.comb(6, 2) == 15
    assert len(set(images)) == 15  # injective
    assert all(len(im) == 4 for im in images)  # lands in 4-subsets
    assert len(set(images)) == math.comb(6, 4)  # onto: all 4-subsets hit
    print("complement bijection: C(6,2) = C(6,4) = 15, reversible S -> complement")
    # lattice paths <-> step sequences: paths (0,0)->(2,1) <-> sequences with 2 R's
    seqs = [s for s in itertools.product("RU", repeat=3) if s.count("R") == 2]
    assert len(seqs) == math.comb(3, 2) == 3
    print("path encoding: %d step sequences = C(3,2) lattice paths" % len(seqs))
    print("rule: find the natural encoding - the encoding IS the bijection; exhibit the inverse")
    print("OK: %s matched one-to-one" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_comb_double_count(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # handshaking lemma: sum of degrees = 2|E|
    edges = [(0, 1), (0, 2), (1, 2), (2, 3), (3, 4)]
    deg = {}
    for u, v in edges:
        deg[u] = deg.get(u, 0) + 1
        deg[v] = deg.get(v, 0) + 1
    assert sum(deg.values()) == 2 * len(edges) == 10
    print("handshaking: degrees %s sum to %d = 2*%d edges" %
          (sorted(deg.values()), sum(deg.values()), len(edges)))
    # corollary: even number of odd-degree vertices
    odds = sum(1 for d in deg.values() if d % 2 == 1)
    assert odds % 2 == 0
    print("corollary: %d odd-degree vertices (even, as forced)" % odds)
    # committee-chair by double counting incidences (committee, chair)
    n, k = 10, 3
    by_committee = math.comb(n, k) * k
    by_chair = n * math.comb(n - 1, k - 1)
    assert by_committee == by_chair == 360
    print("committee-chair: by committee %d = by chair %d" % (by_committee, by_chair))
    # sum of first n odds = n^2 via L-shaped layers of a grid
    n2 = 7
    assert sum(2 * i - 1 for i in range(1, n2 + 1)) == n2 * n2 == 49
    print("odd sum: 1+3+...+13 = 49 = 7^2 (L-layers of the grid)")
    print("rule: name the incidence set, count it two ways, equate")
    print("OK: %s counted twice" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_comb_int_partitions(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def partitions_upto(N):
    # p_le[k][n]: partitions of n with largest part <= k
    p = [[0] * (N + 1) for _ in range(N + 1)]
    for k in range(N + 1):
        p[k][0] = 1
    for k in range(1, N + 1):
        for n in range(1, N + 1):
            p[k][n] = p[k - 1][n] + (p[k][n - k] if n >= k else 0)
    return [p[N][n] for n in range(N + 1)]
def conjugate(part):
    # Ferrers transpose: conjugate[i] = #{parts >= i+1}
    if not part:
        return []
    return [sum(1 for x in part if x > i) for i in range(part[0])]
def main():
    p = partitions_upto(12)
    assert p[4] == 5 and p[10] == 42
    print("partition numbers: p(4) = 5, p(10) = 42")
    # conjugation is an involution
    part = [4, 1, 1]
    conj = conjugate(part)
    assert conj == [3, 1, 1, 1], conj
    assert conjugate(conj) == part
    print("conjugation: [4,1,1] <-> [3,1,1,1], involution verified")
    # largest part k <-> exactly k parts: partitions of 8, largest part 3
    def partitions_of(n, max_part=None):
        if n == 0:
            yield []
            return
        for first in range(min(n, max_part or n), 0, -1):
            for rest in partitions_of(n - first, first):
                yield [first] + rest
    by_largest3 = [q for q in partitions_of(8) if q[0] == 3]
    by_exactly3 = [q for q in partitions_of(8) if len(q) == 3]
    assert len(by_largest3) == len(by_exactly3) == 5
    print("audit: partitions of 8 with largest part 3: %d = with exactly 3 parts: %d" %
          (len(by_largest3), len(by_exactly3)))
    print("rule: draw the diagram; conjugation and column-removal are the bijections")
    print("OK: %s broke numbers apart" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_comb_stirling2(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def stirling2_table(n):
    S = [[0] * (n + 1) for _ in range(n + 1)]
    S[0][0] = 1
    for i in range(1, n + 1):
        for k in range(1, i + 1):
            S[i][k] = k * S[i - 1][k] + S[i - 1][k - 1]
    return S
def main():
    S = stirling2_table(8)
    assert S[4][2] == 7
    print("S(4,2) = 7: partitions of {1,2,3,4} into 2 unlabeled blocks")
    # Bell numbers: row sums
    B = [sum(S[n]) for n in range(7)]
    assert B[1:6] == [1, 2, 5, 15, 52]
    print("Bell numbers B_1..B_5 = %s" % B[1:6])
    # brute-force audit: set partitions of {1,2,3} into 2 blocks = 3
    # canonical labelings: element 0 -> block 0, both block labels used
    count = 0
    for labels in itertools.product(range(2), repeat=3):
        if labels[0] != 0 or set(labels) != {0, 1}:
            continue
        count += 1
    assert count == S[3][2] == 3
    print("audit: partitions of {1,2,3} into 2 blocks enumerated = 3")
    # change of basis: x^3 = S(3,1)x + S(3,2)x(x-1) + S(3,3)x(x-1)(x-2)
    x = 5
    assert x ** 3 == S[3][1] * x + S[3][2] * x * (x - 1) + S[3][3] * x * (x - 1) * (x - 2)
    print("basis change: 5^3 = %d via Stirling second-kind expansion" % x ** 3)
    print("rule: unlabeled blocks = Stirling; element n joins a block or stands alone")
    print("OK: %s partitioned sets" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_comb_stirling1(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def stirling1_table(n):
    c = [[0] * (n + 1) for _ in range(n + 1)]
    c[0][0] = 1
    for i in range(1, n + 1):
        for k in range(1, i + 1):
            c[i][k] = c[i - 1][k - 1] + (i - 1) * c[i - 1][k]
    return c
def cycle_count(p):
    n = len(p)
    seen = [False] * n
    cycles = 0
    for i in range(n):
        if not seen[i]:
            cycles += 1
            j = i
            while not seen[j]:
                seen[j] = True
                j = p[j]
    return cycles
def main():
    c = stirling1_table(6)
    assert c[4][2] == 11
    print("c(4,2) = 11: permutations of 4 with exactly 2 cycles")
    assert sum(c[4]) == math.factorial(4) == 24
    print("row sum: c(4,1)+c(4,2)+c(4,3)+c(4,4) = 6+11+6+1 = 24 = 4!")
    # brute-force audit: cycle counts over all 24 permutations of 4
    tally = {}
    for p in itertools.permutations(range(4)):
        k = cycle_count(p)
        tally[k] = tally.get(k, 0) + 1
    assert tally[2] == 11 and sum(tally.values()) == 24
    print("audit: cycle-count tally over S_4 = %s" % sorted(tally.items()))
    # signed: x_(3) = x^3 - 3x^2 + 2x
    x = 5
    assert x * (x - 1) * (x - 2) == x ** 3 - 3 * x ** 2 + 2 * x == 60
    print("falling factorial: x_(3) at x=5: 60 = 125 - 75 + 10")
    print("rule: first kind = cycles; new element forms a 1-cycle or splices into n-1 slots")
    print("OK: %s decomposed into cycles" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_comb_lattice_paths(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def paths(a, b):
    # step sequences with a rights and b ups
    return [s for s in itertools.product("RU", repeat=a + b) if s.count("R") == a]
def main():
    assert len(paths(3, 2)) == math.comb(5, 3) == 10
    print("lattice paths (0,0)->(3,2): %d = C(5,3)" % len(paths(3, 2)))
    # ballot: A gets 3, B gets 2; orders where A always strictly leads
    a, b = 3, 2
    good = 0
    for s in itertools.product("AB", repeat=a + b):
        if s.count("A") != a:
            continue
        lead, ok = 0, True
        for ch in s:
            lead += 1 if ch == "A" else -1
            if lead <= 0:
                ok = False
                break
        good += ok
    formula = (a - b) * math.comb(a + b, a) // (a + b)
    assert good == formula == 2
    print("ballot: A=3,B=2, A always leads in %d orders = (3-2)/5*C(5,3)" % good)
    # Catalan preview: (0,0)->(2,2) never above diagonal
    dyck = [s for s in paths(2, 2)
            if all(s[:i + 1].count("U") <= s[:i + 1].count("R") for i in range(4))]
    assert len(dyck) == 2  # C_2
    print("diagonal-constrained paths to (2,2): %d = Catalan C_2" % len(dyck))
    print("rule: encode as step sequences; reflect bad paths across the barrier")
    print("OK: %s walked the lattice" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_comb_recurrence(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
def tilings(n):
    # brute-force domino tilings of a 2xn board via backtracking
    board = [[False] * n for _ in range(2)]
    count = [0]
    def rec():
        for r in range(2):
            for c_ in range(n):
                if not board[r][c_]:
                    # vertical domino
                    if r == 0 and not board[1][c_]:
                        board[0][c_] = board[1][c_] = True
                        rec()
                        board[0][c_] = board[1][c_] = False
                    # horizontal domino
                    if c_ + 1 < n and not board[r][c_ + 1]:
                        board[r][c_] = board[r][c_ + 1] = True
                        rec()
                        board[r][c_] = board[r][c_ + 1] = False
                    return
        count[0] += 1
    rec()
    return count[0]
def main():
    assert fib(10) == 55
    print("Fibonacci: F_10 = 55 by iteration")
    # domino tilings of 2xn satisfy the Fibonacci recurrence
    a = {0: 1, 1: 1}
    for n in range(2, 7):
        a[n] = a[n - 1] + a[n - 2]
    assert tilings(3) == a[3] == 3
    assert tilings(4) == a[4] == 5
    print("domino tilings: 2x3 -> %d, 2x4 -> %d (brute force = Fibonacci recurrence)" %
          (tilings(3), tilings(4)))
    # Tower of Hanoi: T_n = 2*T_{n-1} + 1
    T = 0
    for _ in range(4):
        T = 2 * T + 1
    assert T == 15
    print("Hanoi: 4 disks need %d moves" % T)
    print("rule: first decision splits the problem; test n=0..3 against brute force")
    print("OK: %s recurred" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_comb_char_eq(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # a_n = 5a_{n-1} - 6a_{n-2}, a_0 = 0, a_1 = 1
    # characteristic r^2 - 5r + 6 = 0 -> roots 2, 3 -> a_n = 3^n - 2^n
    disc = 25 - 24
    r1 = (5 + math.sqrt(disc)) / 2
    r2 = (5 - math.sqrt(disc)) / 2
    assert abs(r1 - 3.0) < 1e-12 and abs(r2 - 2.0) < 1e-12
    seq = [0, 1]
    for n in range(2, 8):
        seq.append(5 * seq[-1] - 6 * seq[-2])
    closed = [3 ** n - 2 ** n for n in range(8)]
    assert seq == closed
    print("a_n = 5a_{n-1} - 6a_{n-2}: roots 2,3 -> a_n = 3^n - 2^n; first terms %s" % seq[:6])
    # Binet: F_10 from (phi^10 - psi^10)/sqrt(5)
    phi = (1 + math.sqrt(5)) / 2
    psi = (1 - math.sqrt(5)) / 2
    assert round((phi ** 10 - psi ** 10) / math.sqrt(5)) == 55
    print("Binet: F_10 = 55 from irrational powers")
    # repeated root: a_n = 4a_{n-1} - 4a_{n-2}, a_0 = 1, a_1 = 4 -> (1+n)2^n
    seq2 = [1, 4]
    for n in range(2, 7):
        seq2.append(4 * seq2[-1] - 4 * seq2[-2])
    assert seq2 == [(1 + n) * 2 ** n for n in range(7)]
    print("repeated root 2: a_n = (1+n)2^n verified to n=6")
    print("rule: roots give building blocks; fit constants to initial conditions; verify")
    print("OK: %s solved the recurrence" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_comb_ogf(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def series_mul(A, B, n):
    return [sum(A[k] * B[j - k] for k in range(j + 1)) for j in range(n)]
def main():
    N = 8
    # 1/(1-x)^2 <-> 1, 2, 3, ... : verify (1-x)^2 * S = 1
    S = list(range(1, N + 1))
    one_minus_x_sq = [1, -2, 1] + [0] * (N - 3)
    prod = series_mul(one_minus_x_sq, S, N)
    assert prod[0] == 1 and all(p == 0 for p in prod[1:])
    print("OGF check: (1-x)^2 * [1,2,3,...] = 1 (series identity to x^%d)" % (N - 1))
    # Fibonacci OGF: x/(1-x-x^2); verify (1-x-x^2)*F(x) = x
    F = [0, 1, 1, 2, 3, 5, 8, 13]
    denom = [1, -1, -1] + [0] * (N - 3)
    prod2 = series_mul(denom, F, N)
    assert prod2[0] == 0 and prod2[1] == 1 and all(p == 0 for p in prod2[2:])
    print("Fibonacci OGF: (1-x-x^2)*F(x) = x verified to x^7")
    # Catalan OGF: C = 1 + x*C^2; verify with C = 1,1,2,5,14
    C = [1, 1, 2, 5, 14]
    C2 = series_mul(C, C, 5)
    rhs = [1] + C2[:4]  # 1 + x*C^2
    assert rhs == C
    print("Catalan OGF: 1 + x*C(x)^2 = C(x) verified on 1,1,2,5,14")
    print("rule: sum the recurrence against x^n; shift = multiply by x; convolution = multiply series")
    print("OK: %s encoded the sequences" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_comb_egf(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
from fractions import Fraction
def series_mul(A, B, n):
    return [sum(A[k] * B[j - k] for k in range(j + 1)) for j in range(n)]
def series_exp(A, n):
    # exp of series with A[0] = 0, exact Fractions
    E = [Fraction(0)] * n
    E[0] = Fraction(1)
    for j in range(1, n):
        E[j] = sum(Fraction(k, j) * A[k] * E[j - k] for k in range(1, j + 1))
    return E
def main():
    N = 6
    # derangements EGF: e^{-x}/(1-x); coefficients !n/n!
    neg = [Fraction((-1) ** k, math.factorial(k)) for k in range(N)]
    ones = [Fraction(1)] * N
    D = series_mul(neg, ones, N)
    der = [1, 0, 1, 2, 9, 44]  # !0=1, !1=0, !2=1, !3=2, !4=9, !5=44
    assert [int(D[n] * math.factorial(n)) for n in range(N)] == der
    print("derangement EGF: e^{-x}/(1-x) coefficients x !n/n! -> !0..!5 = %s" % der)
    # Bell EGF: e^{e^x - 1}; e^x - 1 has zero constant term
    em1 = [Fraction(0)] + [Fraction(1, math.factorial(k)) for k in range(1, N)]
    Bser = series_exp(em1, N)
    bells = [1, 1, 2, 5, 15, 52]
    assert [int(Bser[n] * math.factorial(n)) for n in range(N)] == bells
    print("Bell EGF: e^{e^x-1} coefficients x B_n/n! -> B_0..B_5 = %s" % bells)
    # labeled product: permutations = sets of cycles -> 1/(1-x) as EGF gives n!
    print("sets of cycles: EGF 1/(1-x) -> coefficients n!/n! = 1 x n! permutations")
    print("rule: labeled structures -> EGF; union -> +, product -> x, set -> exp")
    print("OK: %s exponentiated the labels" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_comb_twelvefold(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # distinct balls, distinct boxes
    n, k = 3, 2
    any_assign = list(itertools.product(range(k), repeat=n))
    assert len(any_assign) == k ** n == 8
    onto = [a for a in any_assign if set(a) == {0, 1}]
    assert len(onto) == 6 == math.factorial(k) * 3  # k! S(3,2) = 2*3
    print("distinct/distinct: any = 2^3 = 8; onto = 6 = 2!*S(3,2)")
    n2, k2 = 2, 3
    inj = [a for a in itertools.product(range(k2), repeat=n2) if len(set(a)) == n2]
    assert len(inj) == 3 * 2 == 6  # P(3,2)
    print("distinct/distinct injective (2 balls, 3 boxes): P(3,2) = 6")
    # identical balls, distinct boxes: compositions of 3 into 2 parts
    comps = [(i, 3 - i) for i in range(4)]
    assert len(comps) == math.comb(3 + 2 - 1, 3) == 4
    print("identical/distinct: compositions of 3 into 2 parts = 4 = C(4,3)")
    # identical/distinct, >= 1 per box: C(n-1, k-1)
    comps_pos = [(i, 3 - i) for i in range(1, 3)]
    assert len(comps_pos) == math.comb(2, 1) == 2
    print("identical/distinct >=1: 2 = C(2,1)")
    # distinct balls, identical boxes, >= 1: S(3,2) = 3 (unlabeled pairs)
    parts = set()
    for a in onto:
        boxes = {}
        for ball, box in enumerate(a):
            boxes.setdefault(box, []).append(ball)
        parts.add(frozenset(frozenset(b) for b in boxes.values()))
    assert len(parts) == 3
    print("distinct/identical >=1: S(3,2) = 3 unlabeled onto groupings")
    # identical/identical: integer partitions p(3) = 3
    assert len([[3], [2, 1], [1, 1, 1]]) == 3
    print("identical/identical: p(3) = 3 partitions")
    print("rule: classify balls, boxes, occupancy - then read the cell")
    print("OK: %s filled the twelve cells" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_comb_catalan(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def catalan_closed(n):
    return math.comb(2 * n, n) // (n + 1)
def catalan_rec(n):
    C = [1]
    for m in range(n):
        C.append(sum(C[i] * C[m - i] for i in range(m + 1)))
    return C
def dyck_paths(n):
    # paths with n R and n U steps, never more U than R in any prefix
    res = []
    def rec(seq, r, u):
        if r == 0 and u == 0:
            res.append(seq)
            return
        if r > 0:
            rec(seq + "R", r - 1, u)
        if u > r:
            rec(seq + "U", r, u - 1)
    rec("", n, n)
    return res
def main():
    C = catalan_rec(12)
    assert C[:6] == [1, 1, 2, 5, 14, 42]
    assert all(catalan_closed(n) == C[n] for n in range(12))
    print("Catalan: closed form (1/(n+1))C(2n,n) = recurrence; C_5 = 42")
    assert len(dyck_paths(3)) == 5
    print("Dyck paths of semilength 3: %d enumerated" % len(dyck_paths(3)))
    # well-formed parentheses with 3 pairs
    parens = []
    def rec(s, o, c):
        if o == 0 and c == 0:
            parens.append(s)
            return
        if o > 0:
            rec(s + "(", o - 1, c)
        if c > o:
            rec(s + ")", o, c - 1)
    rec("", 3, 3)
    assert len(parens) == 5
    print("parenthesizations of 3 pairs: %d" % len(parens))
    # asymptotics: C_n ~ 4^n / (n^{3/2} sqrt(pi)) (slow convergence: use n=12)
    approx = 4 ** 12 / (12 ** 1.5 * math.sqrt(math.pi))
    assert abs(C[12] / approx - 1) < 0.1
    print("asymptotics: C_12 = %d ~ 4^12/(12^1.5 sqrt(pi)) = %.0f" % (C[12], approx))
    print("rule: find the 'root + two independent parts' decomposition")
    print("OK: %s counted the ubiquitous" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_comb_bell(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def bell_upto(n):
    B = [1]  # B_0
    for m in range(n):
        B.append(sum(math.comb(m, k) * B[k] for k in range(m + 1)))
    return B
def aitken(n):
    # Aitken's Bell triangle; row n starts with last entry of previous row
    tri = [[1]]
    for _ in range(n):
        prev = tri[-1]
        row = [prev[-1]]
        for x in prev:
            row.append(row[-1] + x)
        tri.append(row)
    return tri
def main():
    B = bell_upto(6)
    assert B[1:6] == [1, 2, 5, 15, 52]
    print("Bell recurrence B_{n+1} = sum C(n,k)B_k: B_1..B_5 = %s" % B[1:6])
    tri = aitken(5)
    assert tri[5][0] == 52
    print("Aitken triangle row 5 starts with %d = B_5" % tri[5][0])
    # Dobinski: B_5 = (1/e) sum k^5/k!
    dob = sum(k ** 5 / math.factorial(k) for k in range(25)) / math.e
    assert abs(dob - 52) < 0.01
    print("Dobinski: (1/e) sum k^5/k! = %.4f ~ 52" % dob)
    # rhyme schemes: partitions of 4 line-positions = B_4 = 15
    assert B[4] == 15
    print("rhyme schemes for 4 lines: %d = B_4" % B[4])
    print("rule: condition on the distinguished element's block; unlabeled blocks throughout")
    print("OK: %s gathered everything" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_comb_partition_gf(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
from functools import lru_cache
@lru_cache(maxsize=None)
def p_euler(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    total, k, sign = 0, 1, 1
    while True:
        for kk in (k, -k):
            g = kk * (3 * kk - 1) // 2
            if g > n:
                if kk < 0:
                    return total
                break
            total += sign * p_euler(n - g)
        else:
            k += 1
            sign = -sign
            continue
        break
    return total
def partitions_of(n, max_part=None):
    if n == 0:
        yield []
        return
    for first in range(min(n, max_part or n), 0, -1):
        for rest in partitions_of(n - first, first):
            yield [first] + rest
def main():
    assert p_euler(10) == 42
    assert p_euler(50) == 204226
    print("pentagonal recurrence: p(10) = 42, p(50) = 204226")
    # odd parts <-> distinct parts for n = 6
    odd = [q for q in partitions_of(6) if all(x % 2 == 1 for x in q)]
    dist = [q for q in partitions_of(6) if len(set(q)) == len(q)]
    assert len(odd) == len(dist) == 4
    print("Euler odd=distinct: partitions of 6 into odd parts: %d; into distinct: %d" %
          (len(odd), len(dist)))
    # merge/split bijection on one example: 3+3+1+1 -> merge pairs -> 6+2
    def merge_pairs(q):
        from collections import Counter
        c = Counter(q)
        out = []
        for part, mult in sorted(c.items()):
            while mult >= 2:
                out.append(2 * part)
                mult -= 2
            if mult:
                out.append(part)
        # repeat until all distinct
        res = sorted(out, reverse=True)
        while len(set(res)) != len(res):
            res = merge_pairs(res)
        return res
    assert merge_pairs([3, 3, 1, 1]) == [6, 2]
    print("merge bijection: [3,3,1,1] -> [6,2] (odd parts merged to distinct)")
    # generating-function identity: prod 1/(1-x^{odd}) = prod (1+x^k), check to x^8
    N = 9
    A = [1] + [0] * (N - 1)
    for k in range(1, N, 2):
        B = [0] * N
        for j in range(N):
            if A[j]:
                m = j
                while m < N:
                    B[m] += A[j]
                    m += k
        A = B
    C = [1] + [0] * (N - 1)
    for k in range(1, N):
        D = [0] * N
        for j in range(N):
            if C[j]:
                D[j] += C[j]
                if j + k < N:
                    D[j + k] += C[j]
        C = D
    assert A == C
    print("generating functions agree to x^8: odd-parts product = distinct-parts product")
    print("rule: pentagonal recurrence for values, bijections for identities, series for proofs")
    print("OK: %s proved Euler's theorems" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_comb_graph_counting(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def mat_mul(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
def main():
    # graph: 0-1, 0-2, 1-2 (triangle), 2-3
    n = 4
    edges = [(0, 1), (0, 2), (1, 2), (2, 3)]
    A = [[0] * n for _ in range(n)]
    for u, v in edges:
        A[u][v] = A[v][u] = 1
    deg = [sum(row) for row in A]
    assert deg == [2, 2, 3, 1] and sum(deg) == 2 * len(edges)
    print("handshaking: degrees %s sum to %d = 2*%d" % (deg, sum(deg), len(edges)))
    A2 = mat_mul(A, A)
    # walks of length 2 from 0 to 3: only 0->2->3
    assert A2[0][3] == 1
    # closed 2-walks at 0 = degree of 0
    assert A2[0][0] == deg[0] == 2
    print("walk counting: (A^2)[0][3] = %d walk 0->2->3; (A^2)[0][0] = deg(0)" % A2[0][3])
    A3 = mat_mul(A2, A)
    assert sum(A3[i][i] for i in range(n)) // 6 == 1  # one triangle
    print("triangles: trace(A^3)/6 = %d" % (sum(A3[i][i] for i in range(n)) // 6))
    # Havel-Hakimi: (2,2,2,2) graphic (C4); (3,3,3,1) not graphic
    def havel_hakimi(ds):
        ds = sorted([d for d in ds if d > 0], reverse=True)
        while ds:
            d = ds.pop(0)
            if d > len(ds):
                return False
            ds = sorted([x - 1 for x in ds[:d]] + ds[d:], reverse=True)
            ds = [x for x in ds if x > 0]
        return True
    assert havel_hakimi([2, 2, 2, 2]) is True
    assert havel_hakimi([3, 3, 3, 1]) is False
    print("Havel-Hakimi: (2,2,2,2) graphic, (3,3,3,1) not graphic")
    print("rule: model as vertices+edges; matrix powers count walks; HH tests sequences")
    print("OK: %s counted on graphs" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_comb_cayley(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def prufer_encode(edges, n):
    adj = {i: set() for i in range(1, n + 1)}
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    seq = []
    alive = set(range(1, n + 1))
    for _ in range(n - 2):
        leaf = min(v for v in alive if len(adj[v] & alive) == 1)
        (nbr,) = adj[leaf] & alive
        seq.append(nbr)
        alive.discard(leaf)
    return seq
def prufer_decode(seq, n):
    from collections import Counter
    cnt = Counter(seq)
    import heapq
    leaves = [v for v in range(1, n + 1) if cnt.get(v, 0) == 0]
    heapq.heapify(leaves)
    edges = []
    for s in seq:
        leaf = heapq.heappop(leaves)
        edges.append((leaf, s))
        cnt[s] -= 1
        if cnt[s] == 0:
            heapq.heappush(leaves, s)
    a = heapq.heappop(leaves)
    b = heapq.heappop(leaves)
    edges.append((a, b))
    return edges
def is_tree(edges, n):
    if len(edges) != n - 1:
        return False
    adj = {i: set() for i in range(1, n + 1)}
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    seen, stack = set(), [1]
    while stack:
        v = stack.pop()
        if v in seen:
            continue
        seen.add(v)
        stack.extend(adj[v] - seen)
    return len(seen) == n
def main():
    n = 4
    # all Prufer sequences decode to distinct trees: n^{n-2}
    trees = set()
    for seq in itertools.product(range(1, n + 1), repeat=n - 2):
        e = prufer_decode(list(seq), n)
        assert is_tree(e, n)
        trees.add(frozenset(frozenset(x) for x in e))
    assert len(trees) == n ** (n - 2) == 16
    print("Cayley: %d labeled trees on 4 vertices = 4^2 (all Prufer decodes valid+distinct)" % len(trees))
    # round trip on an example
    edges = [(1, 2), (2, 3), (2, 4)]
    seq = prufer_encode(edges, 4)
    assert seq == [2, 2], seq
    back = prufer_decode(seq, 4)
    assert set(map(frozenset, back)) == set(map(frozenset, edges))
    print("Prufer round trip: tree -> [2,2] -> tree")
    print("rule: labeled trees <-> length-(n-2) strings; count the strings")
    print("OK: %s encoded the trees" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_comb_euler_ham(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def hierholzer(n, edges):
    from collections import defaultdict
    adj = defaultdict(list)
    for i, (u, v) in enumerate(edges):
        adj[u].append([v, i])
        adj[v].append([u, i])
    used = [False] * len(edges)
    start = edges[0][0]
    # start at an odd vertex if there is one (Eulerian trail)
    deg = defaultdict(int)
    for u, v in edges:
        deg[u] += 1
        deg[v] += 1
    for v, d in deg.items():
        if d % 2 == 1:
            start = v
            break
    circuit, stack = [], [start]
    while stack:
        v = stack[-1]
        while adj[v] and used[adj[v][-1][1]]:
            adj[v].pop()
        if adj[v]:
            w, i = adj[v].pop()
            used[i] = True
            stack.append(w)
        else:
            circuit.append(stack.pop())
    return circuit
def hamiltonian(n, edges):
    adj = {i: set() for i in range(n)}
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    def rec(path, seen):
        if len(path) == n:
            return path[0] in adj[path[-1]]
        for w in adj[path[-1]]:
            if w not in seen:
                seen.add(w)
                if rec(path + [w], seen):
                    return True
                seen.discard(w)
        return False
    return rec([0], {0})
def main():
    # Eulerian circuit: square 0-1-2-3-0, all degrees even
    sq = [(0, 1), (1, 2), (2, 3), (3, 0)]
    circ = hierholzer(4, sq)
    assert len(circ) == len(sq) + 1 and circ[0] == circ[-1]
    used_edges = set()
    for a, b in zip(circ, circ[1:]):
        e = frozenset((a, b))
        assert e not in used_edges
        used_edges.add(e)
    assert len(used_edges) == 4
    print("Eulerian circuit on square: %s (every edge once)" % circ)
    # trail with 2 odd vertices: path 0-1-2-3
    path_edges = [(0, 1), (1, 2), (2, 3)]
    trail = hierholzer(4, path_edges)
    assert len(trail) == 4 and {trail[0], trail[-1]} == {0, 3}
    print("Eulerian trail on path: %s (odd endpoints 0 and 3)" % trail)
    # Konigsberg: degrees 3,3,3,5 -> 4 odds -> impossible
    kb = [(0, 1), (0, 1), (0, 2), (0, 3), (0, 3), (1, 2), (2, 3)]
    from collections import Counter
    degs = Counter()
    for u, v in kb:
        degs[u] += 1
        degs[v] += 1
    odds = sum(1 for d in degs.values() if d % 2)
    assert odds == 4
    print("Konigsberg: %d odd-degree vertices -> no Eulerian trail (Euler 1736)" % odds)
    # Hamiltonian: square has one; Dirac satisfied (min degree 2 >= 4/2)
    assert hamiltonian(4, sq) is True
    print("Hamiltonian cycle on square: exists (Dirac: min degree 2 >= n/2)")
    print("rule: edges-once = check degrees (easy); vertices-once = search (hard)")
    print("OK: %s toured the graphs" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_comb_ramsey(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def has_mono_triangle(n, edges, coloring):
    red = set(i for i, c in enumerate(coloring) if c == 0)
    for a, b, c_ in itertools.combinations(range(n), 3):
        eab = edges.index((a, b))
        eac = edges.index((a, c_))
        ebc = edges.index((b, c_))
        cols = {eab in red, eac in red, ebc in red}
        if len(cols) == 1:
            return True
    return False
def main():
    n = 6
    edges = [(a, b) for a in range(n) for b in range(a + 1, n)]
    assert len(edges) == 15
    # every 2-coloring of K6 has a monochromatic triangle: 2^15 colorings
    bad = 0
    for mask in range(2 ** 15):
        coloring = [(mask >> i) & 1 for i in range(15)]
        if not has_mono_triangle(n, edges, coloring):
            bad += 1
    assert bad == 0
    print("R(3,3) <= 6: all %d red-blue colorings of K6 contain a monochromatic triangle" % 2 ** 15)
    # lower bound: 5-cycle red, chords blue -> no monochromatic triangle on K5
    n5 = 5
    e5 = [(a, b) for a in range(n5) for b in range(a + 1, n5)]
    cyc = {(0, 1), (1, 2), (2, 3), (3, 4), (0, 4)}
    coloring5 = [0 if e in cyc else 1 for e in e5]
    assert not has_mono_triangle(n5, e5, coloring5)
    print("R(3,3) > 5: 5-cycle red + chords blue has no monochromatic triangle")
    print("R(3,3) = 6 exactly")
    # recurrence bound: R(3,4) <= R(2,4) + R(3,3) = 4 + 6 = 10 (true value 9)
    assert 4 + 6 == 10
    print("recurrence: R(3,4) <= R(2,4)+R(3,3) = 4+6 = 10 (actual 9)")
    print("rule: pigeonhole a vertex's red/blue neighborhoods, recurse; exhibit colorings for lower bounds")
    print("OK: %s forced the order" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_comb_designs(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # Fano plane: lines {i, i+1, i+3} mod 7
    blocks = [frozenset([(i) % 7, (i + 1) % 7, (i + 3) % 7]) for i in range(7)]
    assert len(set(blocks)) == 7
    # every pair in exactly one block
    pair_count = {}
    for b in blocks:
        for a, c_ in itertools.combinations(sorted(b), 2):
            pair_count[(a, c_)] = pair_count.get((a, c_), 0) + 1
    assert len(pair_count) == math.comb(7, 2) == 21
    assert set(pair_count.values()) == {1}
    print("Fano plane: 7 blocks, all 21 pairs in exactly one block (lambda=1)")
    # parameters: bk = vr, r(k-1) = lambda(v-1), Fisher b >= v
    v, b, r, k, lam = 7, 7, 3, 3, 1
    assert b * k == v * r == 21
    assert r * (k - 1) == lam * (v - 1) == 6
    assert b >= v
    print("parameters (7,7,3,3,1): bk=vr=21, r(k-1)=lambda(v-1)=6, Fisher holds")
    # difference set {0,1,3}: all nonzero differences mod 7 appear exactly once
    D = {0, 1, 3}
    diffs = sorted((a - c_) % 7 for a in D for c_ in D if a != c_)
    assert diffs == [1, 2, 3, 4, 5, 6]
    print("difference set {0,1,3}: differences cover 1..6 exactly once")
    # each point in exactly r = 3 blocks
    for pt in range(7):
        assert sum(1 for bl in blocks if pt in bl) == 3
    print("each point lies on exactly 3 blocks")
    print("rule: verify bk=vr and r(k-1)=lambda(v-1); build symmetric designs from difference sets")
    print("OK: %s balanced the blocks" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_comb_latin(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def is_latin(sq):
    n = len(sq)
    syms = set(range(n))
    return all(set(row) == syms for row in sq) and all(
        set(sq[r][c] for r in range(n)) == syms for c in range(n))
def main():
    A = [[0, 1, 2], [1, 2, 0], [2, 0, 1]]
    B = [[0, 1, 2], [2, 0, 1], [1, 2, 0]]
    assert is_latin(A) and is_latin(B)
    # orthogonality: all 9 overlay pairs distinct
    pairs = [(A[r][c], B[r][c]) for r in range(3) for c in range(3)]
    assert len(set(pairs)) == 9
    print("orthogonal pair of order 3: overlay shows all 9 pairs")
    # count: reduced (first row/col fixed) order-3 squares
    count = 0
    cells = [(1, 1), (1, 2), (2, 1), (2, 2)]
    for vals in itertools.product(range(3), repeat=4):
        sq = [[0, 1, 2], [1, 0, 0], [2, 0, 0]]
        for (r, c), v in zip(cells, vals):
            sq[r][c] = v
        if is_latin(sq):
            count += 1
    assert count == 1
    total = math.factorial(3) * math.factorial(2) * count
    assert total == 12
    print("Latin squares of order 3: 12 = 3! * 2! * 1 reduced")
    # Euler 36 officers: no orthogonal pair of order 6 (Tarry 1900) - note the bound
    print("Euler's 36 officers: no Graeco-Latin square of order 6 (Tarry, 1900)")
    print("rule: rows+columns are permutations; orthogonality = all n^2 pairs on overlay")
    print("OK: %s squared the grid" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_comb_turan(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def max_triangle_free(n):
    edges = [(a, b) for a in range(n) for b in range(a + 1, n)]
    m = len(edges)
    best = 0
    for mask in range(2 ** m):
        chosen = [edges[i] for i in range(m) if mask & (1 << i)]
        if len(chosen) <= best:
            continue
        adj = {i: set() for i in range(n)}
        for u, v in chosen:
            adj[u].add(v)
            adj[v].add(u)
        tri = any(w in adj[u] and w in adj[v]
                  for u in range(n) for v in adj[u] for w in adj[v] if w != u)
        if not tri:
            best = len(chosen)
    return best
def main():
    # brute force: max edges triangle-free on 5 vertices
    best5 = max_triangle_free(5)
    assert best5 == 6
    print("brute force: max triangle-free edges on 5 vertices = %d" % best5)
    # Mantel bound floor(n^2/4)
    assert best5 == 25 // 4
    print("Mantel: floor(25/4) = 6, attained by K_{2,3}")
    # K_{2,3} has 2*3 = 6 edges, triangle-free (bipartite)
    assert 2 * 3 == 6
    # Turan graph T(6,2) = K_{3,3}: 9 edges = (1-1/2)*36/2
    assert 3 * 3 == 9 == (1 - 1 / 2) * 36 / 2
    print("Turan T(6,2) = K_{3,3}: 9 edges = (1-1/2)*6^2/2")
    # T(7,3): parts 3,2,2 -> edges = total - sum C(part,2)
    parts = [3, 2, 2]
    e = math.comb(7, 2) - sum(math.comb(p, 2) for p in parts)
    assert e == 16
    print("Turan T(7,3): parts 3,2,2 -> %d edges, no K_4" % e)
    print("rule: guess the balanced complete multipartite graph, prove nothing beats it")
    print("OK: %s maximized without triangles" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_comb_prob_method(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def has_mono_k(n, edges, coloring, k):
    red = set(i for i, c in enumerate(coloring) if c == 0)
    for S in itertools.combinations(range(n), k):
        idx = [edges.index((a, b)) for a, b in itertools.combinations(S, 2)]
        cols = {i in red for i in idx}
        if len(cols) == 1:
            return True
    return False
def main():
    # Erdos 1947: R(4,4) > 6 via the union bound
    n, s = 6, 4
    bound = math.comb(n, s) * 2 ** (1 - math.comb(s, 2))
    assert bound == 15 / 32 < 1
    print("union bound: C(6,4)*2^{1-6} = 15/32 < 1 -> R(4,4) > 6")
    # the method promises existence; exhibit one by search (non-constructive proof made concrete)
    edges = [(a, b) for a in range(n) for b in range(a + 1, n)]
    found = None
    for mask in range(2 ** len(edges)):
        coloring = [(mask >> i) & 1 for i in range(len(edges))]
        if not has_mono_k(n, edges, coloring, 4):
            found = coloring
            break
    assert found is not None
    print("a 2-coloring of K6 with no monochromatic K4 exists (search found one)")
    # general lower bound R(s,s) > 2^{s/2}: check s=5, n=11
    s2, n2 = 5, 11
    b2 = math.comb(n2, s2) * 2 ** (1 - math.comb(s2, 2))
    assert b2 < 1, b2
    print("R(5,5) > 11: C(11,5)*2^{-9} = %.3f < 1" % b2)
    # alteration: independent set in C5, bound alpha >= n^2/4m = 25/20
    import random
    rng = random.Random(42)
    c5 = [(i, (i + 1) % 5) for i in range(5)]
    n3, m3 = 5, 5
    best = 0
    for _ in range(2000):
        keep = [i for i in range(n3) if rng.random() < n3 / (2 * m3)]
        S = set(keep)
        for u, v in c5:
            if u in S and v in S:
                S.discard(v)  # alteration: fix each surviving edge
        best = max(best, len(S))
    assert best >= 2  # true alpha(C5) = 2
    print("alteration: random+fix finds independent set of size %d in C5 (bound n^2/4m = 1.25)" % best)
    print("rule: random object + P(good) > 0 => good object exists; alteration fixes defects")
    print("OK: %s proved by randomness" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_comb_polya(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    n, k = 4, 2
    # Burnside: rotations of 4 beads; rotation by j has gcd(4,j) cycles
    total = sum(k ** math.gcd(n, j) for j in range(n))
    assert total == 16 + 2 + 4 + 2 == 24
    necklaces = total // n
    assert necklaces == 6
    print("Burnside: (2^4 + 2^1 + 2^2 + 2^1)/4 = %d necklaces (4 beads, 2 colors)" % necklaces)
    # cycle-index form: (1/4)(phi(1)2^4 + phi(2)2^2 + phi(4)2^1)
    phi = lambda m: sum(1 for i in range(1, m + 1) if math.gcd(i, m) == 1)
    ci = sum(phi(d) * k ** (n // d) for d in (1, 2, 4) if n % d == 0) // n
    assert ci == 6
    print("cycle index: (phi(1)2^4 + phi(2)2^2 + phi(4)2^1)/4 = %d" % ci)
    # brute-force audit: orbits of 16 colorings under rotation
    def rotate(c):
        return c[1:] + c[:1]
    seen, orbits = set(), 0
    for mask in range(16):
        c = tuple((mask >> i) & 1 for i in range(n))
        if c in seen:
            continue
        orbits += 1
        r = c
        for _ in range(n):
            seen.add(r)
            r = rotate(r)
    assert orbits == 6
    print("audit: 16 colorings fall into %d rotation orbits" % orbits)
    # pattern inventory: count by number of black beads via cycle index substitution
    # Z = (z1^4 + z2^2 + 2*z1^2*z2 ... )/4; coefficient check: 2 necklaces with exactly 2 black
    two_black = [mask for mask in range(16) if bin(mask).count("1") == 2]
    orb2, seen2 = 0, set()
    for mask in two_black:
        c = tuple((mask >> i) & 1 for i in range(n))
        if c in seen2:
            continue
        orb2 += 1
        r = c
        for _ in range(n):
            seen2.add(r)
            r = rotate(r)
    assert orb2 == 2  # {0011-type} and {0101-type}
    print("inventory: %d necklaces with exactly 2 black beads" % orb2)
    print("rule: average fixed colorings over the group; verify small cases by orbit enumeration")
    print("OK: %s counted up to symmetry" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_comb_games(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def grundy_subtract(n, moves):
    g = [0] * (n + 1)
    for i in range(1, n + 1):
        reachable = {g[i - m] for m in moves if m <= i}
        mex = 0
        while mex in reachable:
            mex += 1
        g[i] = mex
    return g
def main():
    # Nim: heaps (3, 5, 7)
    heaps = (3, 5, 7)
    x = heaps[0] ^ heaps[1] ^ heaps[2]
    assert x == 1  # nonzero -> N-position, winning move exists
    print("Nim (3,5,7): xor = %d (nonzero -> next player wins)" % x)
    # winning move: make the xor zero; reduce heap 7 -> 6
    assert 3 ^ 5 ^ 6 == 0
    print("winning move: 7 -> 6, since 3 xor 5 xor 6 = 0")
    # verify: from xor 0 (P-position), every move makes it nonzero
    ppos = (3, 5, 6)
    assert ppos[0] ^ ppos[1] ^ ppos[2] == 0
    nmoves = 0
    for h in range(3):
        for new in range(ppos[h]):
            nh = list(ppos)
            nh[h] = new
            assert nh[0] ^ nh[1] ^ nh[2] != 0
            nmoves += 1
    assert nmoves == 14
    print("audit: from P-position (3,5,6), all %d moves go to nonzero xor" % nmoves)
    # Sprague-Grundy: subtraction game {1,2,3}
    g = grundy_subtract(12, (1, 2, 3))
    assert g[:9] == [0, 1, 2, 3, 0, 1, 2, 3, 0]
    print("subtraction {1,2,3}: Grundy numbers periodic 0,1,2,3,...")
    # heap of 4 is a P-position
    assert g[4] == 0
    print("heap of 4: Grundy 0 = P-position (losing for player to move)")
    print("rule: xor the heaps (Nim); mex the options (Grundy); zero means losing")
    print("OK: %s played perfectly" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_comb_symmetric(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def elem_sym(vals, k):
    return sum(math.prod(c) for c in itertools.combinations(vals, k))
def power_sum(vals, k):
    return sum(v ** k for v in vals)
def main():
    vals = (1, 2, 3)
    e1, e2, e3 = (elem_sym(vals, k) for k in (1, 2, 3))
    assert (e1, e2, e3) == (6, 11, 6)
    print("elementary symmetric of (1,2,3): e1=%d, e2=%d, e3=%d" % (e1, e2, e3))
    # Newton: p_2 = e_1 p_1 - 2 e_2
    p1, p2 = power_sum(vals, 1), power_sum(vals, 2)
    assert p2 == e1 * p1 - 2 * e2 == 14
    print("Newton: p_2 = e_1*p_1 - 2*e_2 = %d = 1+4+9" % p2)
    # Vieta: (x-1)(x-2)(x-3) = x^3 - e_1 x^2 + e_2 x - e_3
    coeffs = [1, -e1, e2, -e3]
    assert coeffs == [1, -6, 11, -6]
    for x in (0, 1, 2, 3, 5):
        lhs = (x - 1) * (x - 2) * (x - 3)
        rhs = x ** 3 - 6 * x ** 2 + 11 * x - 6
        assert lhs == rhs
    print("Vieta: (x-1)(x-2)(x-3) = x^3 - 6x^2 + 11x - 6 (verified at 5 points)")
    # random numerical audit of Newton p_3 = e_1 p_2 - e_2 p_1 + 3 e_3
    p3 = power_sum(vals, 3)
    assert p3 == e1 * p2 - e2 * p1 + 3 * e3 == 36
    print("Newton p_3: %d = 1+8+27" % p3)
    print("rule: symmetry -> e/h/p basis; Newton converts; Vieta reads roots")
    print("OK: %s symmetrized the algebra" % NAME)
if __name__ == "__main__":
    main()
''')

DEMOS = {
    "comb_branches": demo_comb_branches, "comb_add_mult": demo_comb_add_mult,
    "comb_pigeonhole": demo_comb_pigeonhole, "comb_permutations": demo_comb_permutations,
    "comb_combinations": demo_comb_combinations, "comb_pascal_binomial": demo_comb_pascal_binomial,
    "comb_perm_rep": demo_comb_perm_rep, "comb_stars_bars": demo_comb_stars_bars,
    "comb_binomial_identities": demo_comb_binomial_identities,
    "comb_inclusion_exclusion": demo_comb_inclusion_exclusion,
    "comb_derangements": demo_comb_derangements, "comb_bijection": demo_comb_bijection,
    "comb_double_count": demo_comb_double_count, "comb_int_partitions": demo_comb_int_partitions,
    "comb_stirling2": demo_comb_stirling2, "comb_stirling1": demo_comb_stirling1,
    "comb_lattice_paths": demo_comb_lattice_paths, "comb_recurrence": demo_comb_recurrence,
    "comb_char_eq": demo_comb_char_eq, "comb_ogf": demo_comb_ogf,
    "comb_egf": demo_comb_egf, "comb_twelvefold": demo_comb_twelvefold,
    "comb_catalan": demo_comb_catalan, "comb_bell": demo_comb_bell,
    "comb_partition_gf": demo_comb_partition_gf, "comb_graph_counting": demo_comb_graph_counting,
    "comb_cayley": demo_comb_cayley, "comb_euler_ham": demo_comb_euler_ham,
    "comb_ramsey": demo_comb_ramsey, "comb_designs": demo_comb_designs,
    "comb_latin": demo_comb_latin, "comb_turan": demo_comb_turan,
    "comb_prob_method": demo_comb_prob_method, "comb_polya": demo_comb_polya,
    "comb_games": demo_comb_games, "comb_symmetric": demo_comb_symmetric,
}
# ---------------------------------------------------------------- records

def build_records(slug, source):
    cfg = DBCFG[slug]
    sig = source == "signature"
    # Teaching-ladder order: stable sort by ladder_rank (entries are already
    # in ladder order in entries_combinatorics.py).
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
    for slug in ("combinatorics", "combinatorics-signature"):
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
