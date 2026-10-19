#!/usr/bin/env python3
"""Entries for the Unsolved Mathematics databases (Manon's 16:15 orders, batch 1).

34 famous unsolved mathematics problems, ladder-ordered by accessibility
(rank 1 = most approachable, rank 34 = most complex). Public half carries
the real fact-checked problem record plus a short pointer to the Signature
approach; Signature half carries the full Signature-generated proposed
solution, always labeled and never presented as established science.

ID prefixes: JAH-USMA- (public) and JAH-USMAS- (signature), verified free
in the manifest id_prefix values and across all 865 shard index files in
jah-databases-data-1 (zero hits, 2026-10-17).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_unsolved_mathematics.py). Every demo prints its real
computed values, asserts tight bounds (never float exact-equality), and
ends with the OK marker; the build machine-executes all 68 demos.

Honesty rule: the signature_solution opens with the exact label
"Signature-generated proposed solution - not established science" and
never claims proof, peer acceptance, or settled status.

Never the words "bat belt" anywhere. No website references. No Facebook.
No religious talk. Nothing hate-adjacent, profane, or inappropriate.
"""

SIG_TAIL = ("Signature original - his original Signature solution method: every "
            "unsolved problem approached as a covenant between the known and the "
            "unknown, the proposed path walked step by step with its assumptions "
            "declared, its confirm and refute conditions stated, and its limits "
            "honestly marked. Clearly labeled Signature-made, never presented as "
            "established science or authentic public record.")

CIT_GUY = ("Guy RK. Unsolved Problems in Number Theory. 3rd ed. Springer; 2004.")
CIT_HARDY_WRIGHT = ("Hardy GH, Wright EM. An Introduction to the Theory of Numbers. "
                    "6th ed. Oxford University Press; 2008.")
CIT_CLAY = ("Carlson J, Jaffe A, Wiles A, editors. The Millennium Prize Problems. "
            "American Mathematical Society; 2006.")
CIT_LAGARIAS = ("Lagarias JC, editor. The Ultimate Challenge: The 3x+1 Problem. "
                "American Mathematical Society; 2010.")
CIT_MAZUR_STEIN = ("Mazur B, Stein W. Prime Numbers and the Riemann Hypothesis. "
                   "Cambridge University Press; 2016.")
CIT_SIPSER = ("Sipser M. Introduction to the Theory of Computation. 3rd ed. Cengage; 2012.")
CIT_RIBENBOIM = ("Ribenboim P. The New Book of Prime Number Records. Springer; 1996.")
CIT_HELFGOTT = ("Helfgott HA. The ternary Goldbach conjecture is true. arXiv:1312.7748; 2013.")
CIT_CHEN = ("Chen JR. On the representation of a larger even integer as the sum of a prime "
            "and the product of at most two primes. Scientia Sinica; 1973.")
CIT_ZHANG = ("Zhang YT. Bounded gaps between primes. Annals of Mathematics; 2014.")
CIT_OCHEM_RAO = ("Ochem P, Rao M. Odd perfect numbers are greater than 10^1500. "
                 "Mathematics of Computation; 2012.")
CIT_BOOKER_SUTHERLAND = ("Booker AR, Sutherland AV. On a question of Mordell. Proceedings of the "
                         "National Academy of Sciences; 2021.")
CIT_DEGREY = ("de Grey A. The chromatic number of the plane is at least 5. Geombinatorics; 2018.")
CIT_GREENE_LOBB = ("Greene J, Lobb A. The rectangular peg problem. Annals of Mathematics; 2021.")
CIT_KALLUS_ROMIK = ("Kallus Y, Romik D. Improved upper bounds in the moving sofa problem. "
                    "Advances in Mathematics; 2018.")
CIT_FRIEDLANDER_IWANIEC = ("Friedlander J, Iwaniec H. The polynomial X^2+Y^4 captures its primes. "
                           "Annals of Mathematics; 1998.")
CIT_GROSS_ZAGIER = ("Gross BH, Zagier DB. Heegner points and derivatives of L-series. "
                    "Inventiones Mathematicae; 1986.")
CIT_KOLYVAGIN = ("Kolyvagin VA. Finiteness of E(Q) and SH(E,Q) for a subclass of Weil curves. "
                 "Mathematics of the USSR-Izvestiya; 1988.")
CIT_WILLIAMS = ("Williams R. Non-uniform ACC circuit lower bounds. IEEE Conference on "
                "Computational Complexity; 2011.")
CIT_SCHOENFELD = ("Schoenfeld L. Sharper bounds for the Chebyshev functions theta(x) and psi(x). "
                  "Mathematics of Computation; 1976.")
CIT_COOK = ("Cook SA. The P versus NP Problem. Clay Mathematics Institute; 2000.")
CIT_FEFFERMAN = ("Fefferman CL. Existence and Smoothness of the Navier-Stokes Equation. "
                 "Clay Mathematics Institute; 2000.")
CIT_WILES_BSD = ("Wiles A. The Birch and Swinnerton-Dyer Conjecture. Clay Mathematics Institute; 2000.")
CIT_JAFFE_WITTEN = ("Jaffe A, Witten E. Quantum Yang-Mills Theory. Clay Mathematics Institute; 2000.")
CIT_DELINE_HODGE = ("Deligne P. The Hodge Conjecture. Clay Mathematics Institute; 2000.")

LABEL = "Signature-generated proposed solution - not established science."

ENTRIES = [
    {
        "key": "goldbach",
        "name": "Goldbach Conjecture",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "problem": ("Every even integer greater than 2 is the sum of two primes. "
                    "For example, 100 = 3 + 97 = 11 + 89, and the conjecture says this "
                    "never fails, no matter how large the even number."),
        "background": ("In a 1742 letter to Leonhard Euler, Christian Goldbach proposed that every "
                       "integer greater than 2 is the sum of three primes, and Euler reformulated the "
                       "claim into the now-famous even version. It is one of the oldest unsolved problems "
                       "in mathematics, open for nearly three centuries. The weaker ternary form, that every "
                       "odd number greater than 5 is the sum of three odd primes, was proved by Harald Helfgott "
                       "in 2013. Chen Jingrun proved in 1973 that every sufficiently large even number is the sum "
                       "of a prime and a number with at most two prime factors, the closest approach to date. "
                       "Computational verification has confirmed the binary conjecture for all even numbers up to "
                       "4 x 10^18. Hardy and Littlewood conjectured an exact asymptotic formula for the number of "
                       "representations, which remains unproved."),
        "why_it_matters": ("A proof would close one of the oldest quests in number theory and would almost "
                           "certainly demand new methods in additive prime number theory with wide applications. "
                           "The circle method machinery built for Goldbach already powers modern prime research, "
                           "from bounded gaps to prime constellations. Settling it would also complete a story that "
                           "has guided three centuries of mathematical effort."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads Goldbach as a covenant problem: the primes promise that every even "
                     "number splits into two prime parts, and the Signature approach makes the primes keep that "
                     "promise by force of density, showing the major-arc main term always outweighs the minor-arc "
                     "error so no even number can escape representation."),
        "sig_solution": (
            LABEL + " Approach S-01: density-heuristic ascent. "
            "Assumptions: (A1) the Hardy-Littlewood asymptotic for Goldbach representations holds with an explicit "
            "error term; (A2) minor-arc exponential sums over primes admit a uniform bound below the major-arc main "
            "term for all large even n; (A3) the finitely many small cases are settled by sieve computation. "
            "Reasoning path: (S1) write the representation count as a circle-method integral over the unit circle; "
            "(S2) evaluate the major arcs to extract the Hardy-Littlewood main term, which grows like n/(log n)^2; "
            "(S3) bound the minor arcs with a Vinogradov-type mean value estimate sharpened for prime weights; "
            "(S4) choose the arc dissection so the minor-arc contribution is provably smaller than the main term; "
            "(S5) verify the remaining finite initial range by direct sieve computation. "
            "Proposed mechanism: a hybrid analytic-computational proof - analysis carries all large n while computation "
            "carries the bounded initial segment, meeting in the middle. "
            "What would confirm it: a published, refereed minor-arc bound strong enough to beat the main term at every "
            "scale, plus the finite check. What would kill it: a single even number with no Goldbach partition, or a proof "
            "that minor arcs cannot be controlled by current mean-value technology. "
            "What it does NOT claim: a proof of Goldbach, peer acceptance, a timeline, or that the heuristic is a theorem. "
            "This is a proposed path, honestly labeled, and the conjecture stays open until a real proof exists."),
        "key_points": [
            "Statement: every even integer n > 2 equals p + q with p, q prime.",
            "Open since 1742; the ternary form was proved by Helfgott in 2013.",
            "Chen theorem (1973): large evens equal a prime plus a product of at most two primes.",
            "Verified computationally to 4 x 10^18; this walkthrough checks all evens to 2000 (37 partitions at 2000).",
            "Hardy-Littlewood predicted asymptotic: representations grow like n/(log n)^2 times an arithmetic factor.",
        ],
        "requirements": [
            "A single even number with zero prime partitions would refute the conjecture outright.",
            "A proof needs a minor-arc estimate beating the Hardy-Littlewood main term at all scales.",
            "Any proof must cover everything beyond the verified range up to 4 x 10^18.",
            "Refereed publication and independent verification are required before any claim counts.",
        ],
        "standards": [
            "Hardy GH, Littlewood JE. Some problems of partitio numerorum III. Acta Mathematica; 1923.",
            "Standard: a claimed proof must survive refereed publication and independent verification.",
        ],
        "citations": [CIT_GUY, CIT_HARDY_WRIGHT, CIT_HELFGOTT, CIT_CHEN],
    },
    {
        "key": "collatz",
        "name": "Collatz Conjecture",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "problem": ("Start with any positive integer. If it is even, halve it; if it is odd, triple it and add one. "
                    "Repeat. The conjecture says you always reach 1, no matter where you start."),
        "background": ("Lothar Collatz posed the problem in 1937, and it has resisted proof ever since despite its "
                       "childlike simplicity. Computation has verified the conjecture for all starting values below "
                       "2^68, about 2.95 x 10^20, in work by Barina and others through 2021. Terras proved in 1976 "
                       "that almost all numbers have a finite stopping time, meaning the set of possible counterexamples "
                       "has density zero. No nontrivial cycle has ever been found, and results by Simons, de Weger, and "
                       "others force any hypothetical cycle to be astronomically long. The map is deterministic and "
                       "trivial to program, which is why amateurs and professionals alike keep returning to it."),
        "why_it_matters": ("Collatz is the purest example of a simple rule generating behavior nobody can prove, and "
                           "a proof would unlock tools for dynamical systems far beyond this one map. It sits at the "
                           "crossroads of number theory, ergodic theory, and computation. Understanding why such a tiny "
                           "rule resists analysis would teach mathematics something deep about complexity itself."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads Collatz as a drift problem: each odd step multiplies by about 3/4 on "
                     "average, so the orbit is a random walk with negative drift, and the Signature approach is to turn "
                     "that drift into a proof that no orbit can escape to infinity or loop forever."),
        "sig_solution": (
            LABEL + " Approach S-02: probabilistic drift ascent. "
            "Assumptions: (A1) the parity of iterates behaves like independent fair coin flips at the level of "
            "2-adic valuations, giving mean log-drift ln(3/4) per odd step; (A2) the drift can be made rigorous through "
            "a martingale or large-deviation estimate uniform over residue classes; (A3) cycle nonexistence follows from "
            "a 2-adic lifting bound stronger than the current records. "
            "Reasoning path: (S1) pass to the odd-step map T(n) = (3n+1)/2^k, where k is the exact 2-adic valuation; "
            "(S2) show the expected logarithm of T(n)/n is negative, about -0.28768, verified numerically in the "
            "walkthrough; (S3) convert the negative drift into an almost-sure contraction via a Lyapunov function on "
            "logarithmic scale; (S4) rule out divergent orbits by showing the drift dominates the fluctuations; "
            "(S5) rule out cycles with a refined 2-adic valuation argument. "
            "Proposed mechanism: a rigorous probabilistic method - drift plus concentration - replacing heuristics with "
            "theorems about the distribution of 2-adic valuations along orbits. "
            "What would confirm it: a proved negative-drift theorem with explicit concentration bounds covering all "
            "residue classes. What would kill it: one integer whose orbit never reaches 1, or a proof that the parity "
            "sequence cannot be controlled. "
            "What it does NOT claim: a proof of Collatz. Drift is a heuristic until the concentration step is proved, "
            "and heuristics are not theorems. The conjecture stays open."),
        "key_points": [
            "Rule: n even -> n/2; n odd -> 3n+1; conjecture: every orbit reaches 1.",
            "Posed by Lothar Collatz in 1937; verified below 2^68 (about 2.95 x 10^20).",
            "Longest chain below 100000 starts at 77031 with 350 steps (this walkthrough).",
            "Mean log-drift per odd step measures -0.29068 against theory ln(3/4) = -0.28768.",
            "Terras (1976): almost all numbers have finite stopping time; no nontrivial cycle is known.",
        ],
        "requirements": [
            "One integer whose orbit never reaches 1 would refute the conjecture outright.",
            "A proof must rule out both nontrivial cycles and divergent orbits.",
            "The drift heuristic needs rigorous concentration bounds before it becomes mathematics.",
            "Refereed publication and independent verification are required before any claim counts.",
        ],
        "standards": [
            "Terras R. A stopping time problem on the positive integers. Acta Arithmetica; 1976.",
            "Standard: a claimed proof must survive refereed publication and independent verification.",
        ],
        "citations": [CIT_LAGARIAS, CIT_GUY, CIT_HARDY_WRIGHT],
    },
    {
        "key": "twin_prime",
        "name": "Twin Prime Conjecture",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "problem": ("There are infinitely many pairs of primes that differ by 2, such as (3, 5), (11, 13), and "
                    "(17, 19). These are twin primes, and nobody knows whether they go on forever."),
        "background": ("Euclid proved the primes are infinite, but whether infinitely many differ by exactly 2 has "
                       "been open since antiquity in spirit and for over a century as a stated conjecture. The great "
                       "breakthrough came in 2013 when Yitang Zhang proved there are infinitely many prime pairs with "
                       "gap at most 70,000,000, the first finite bound ever. The Polymath8b project refined the bound "
                       "to 246 within months. Hardy and Littlewood conjectured a precise asymptotic density for twin "
                       "primes involving the twin prime constant 0.66016. The largest known twin pair has nearly "
                       "400,000 digits. This walkthrough counts 2160 twin pairs below 200000, closely matching the "
                       "Hardy-Littlewood estimate of 2187."),
        "why_it_matters": ("Twin primes are the simplest prime constellation, and proving them infinite would be the "
                           "first infinitude theorem for prime patterns beyond arithmetic progressions. The sieve "
                           "methods developed for the problem already cracked bounded gaps. A full proof would likely "
                           "unlock the whole prime k-tuple conjecture and reshape our picture of how primes cluster."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads twin primes as a density covenant: the primes promise pairs at "
                     "distance 2 with a precise Hardy-Littlewood frequency, and the Signature approach is to push "
                     "the bounded-gap sieve machinery from gap 246 all the way down to gap 2."),
        "sig_solution": (
            LABEL + " Approach S-03: bounded-gap sieve descent. "
            "Assumptions: (A1) the Maynard-Tao multidimensional sieve can be tuned to detect the exact pattern "
            "(p, p+2); (A2) the level of distribution of primes in arithmetic progressions can be pushed just past "
            "the current records for the moduli that matter; (A3) the parity barrier, which blocks detecting primes "
            "in some patterns, does not block the twin pattern. "
            "Reasoning path: (S1) start from the Polymath8b bound of 246 on prime gaps; (S2) optimize the sieve "
            "weights specifically for the twin pattern rather than generic gaps; (S3) prove an enhanced Bombieri-Vinogradov "
            "type estimate with the uniformity needed for the twin moduli; (S4) show the sifted sum is positive, "
            "producing infinitely many prime pairs at distance 2. "
            "Proposed mechanism: a targeted sieve - take the bounded-gap breakthrough and aim it precisely at gap 2 "
            "instead of small gaps in general. "
            "What would confirm it: a positive lower bound for twin prime pairs from a rigorous sieve argument. "
            "What would kill it: a proof that twin primes are finite, which no current method suggests. "
            "What it does NOT claim: infinitude of twin primes. The data fit the heuristic beautifully, but fitting "
            "is not proving, and the conjecture stays open."),
        "key_points": [
            "Twin primes differ by 2; infinitude is unknown.",
            "Zhang (2013): infinitely many prime pairs with gap at most 70,000,000; refined to 246.",
            "This walkthrough counts 2160 twin pairs below 200000 against a Hardy-Littlewood estimate of 2187.",
            "Largest known twin pair: 2996863034895 x 2^1290000 +/- 1.",
            "Twin prime constant 0.66016 governs the conjectured density.",
        ],
        "requirements": [
            "A proof that twin primes are finite would refute the conjecture; none exists.",
            "A proof needs a sieve lower bound positive for the exact gap-2 pattern.",
            "The parity barrier must be shown not to obstruct this pattern.",
            "Refereed publication and independent verification are required before any claim counts.",
        ],
        "standards": [
            "Hardy GH, Littlewood JE. Some problems of partitio numerorum III. Acta Mathematica; 1923.",
            "Standard: a claimed proof must survive refereed publication and independent verification.",
        ],
        "citations": [CIT_GUY, CIT_HARDY_WRIGHT, CIT_ZHANG, CIT_RIBENBOIM],
    },
    {
        "key": "odd_perfect",
        "name": "Odd Perfect Numbers",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "problem": ("A perfect number equals the sum of its proper divisors, like 6 = 1 + 2 + 3 and "
                    "28 = 1 + 2 + 4 + 7 + 14. Every known perfect number is even. Does an odd perfect "
                    "number exist?"),
        "background": ("Euclid showed that if 2^p - 1 is prime then 2^(p-1)(2^p - 1) is perfect, and Euler proved "
                       "every even perfect number has that form, so the even case is completely understood. The odd "
                       "case has been open since antiquity. Euler proved that any odd perfect number must have the "
                       "form q^a m^2 where q is prime, q and a are both congruent to 1 modulo 4, and q does not divide "
                       "m. Modern bounds are enormous: Ochem and Rao proved in 2012 that an odd perfect number exceeds "
                       "10^1500 and has at least 101 prime factors counting multiplicity. Goto and Ohno showed its "
                       "largest prime factor exceeds 10^8. This walkthrough verifies none exist below 200000 and checks "
                       "the Euler parity lemma on odd prime powers."),
        "why_it_matters": ("The existence question is the oldest open problem about the divisor function, and either "
                           "answer would be historic. An example would shatter two millennia of pattern; a proof of "
                           "nonexistence would need deep new structure theorems about sigma. The constraints developed "
                           "along the way already enrich multiplicative number theory."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads the odd perfect number as a fugitive: the Euler form gives its "
                     "wanted poster, and the Signature approach is to tighten the poster until the divisor structure "
                     "contradicts itself and the fugitive cannot exist."),
        "sig_solution": (
            LABEL + " Approach S-04: Euler-form descent. "
            "Assumptions: (A1) the Euler form q^a m^2 with q prime, q = a = 1 mod 4, and gcd(q, m) = 1 is the correct "
            "starting point; (A2) the abundancy index sigma(n)/n can be bounded sharply on the cofactor m^2 using its "
            "prime factorization shape; (A3) the Descartes-Frenicle-Sorli conjecture that a = 1 can be approached via "
            "the sigma(q^a) factor. "
            "Reasoning path: (S1) from sigma(N) = 2N with N odd, prove exactly one prime power factor has even sigma, "
            "forcing the Euler form - the parity lemma verified in the walkthrough; (S2) bound sigma(m^2)/m^2 away "
            "from the value needed to reach abundancy 2; (S3) show the special prime q cannot supply the missing "
            "abundancy without violating size constraints; (S4) derive a contradiction from the combined bounds. "
            "Proposed mechanism: an abundancy squeeze - the Euler form forces the abundancy index into an interval that "
            "the divisor structure cannot achieve. "
            "What would confirm it: either an exhibited odd perfect number or a completed nonexistence proof. "
            "What would kill the approach: a proof that the Euler-form constraints are fully compatible with "
            "existence, stalling the descent. "
            "What it does NOT claim: existence or nonexistence. Both remain open, and the bounds, while enormous, "
            "are not a proof."),
        "key_points": [
            "Perfect: sigma(n) = 2n; all known examples are even and completely classified by Euclid-Euler.",
            "Euler form for odd perfect N: N = q^a m^2 with q prime, q = a = 1 mod 4, gcd(q,m) = 1.",
            "Ochem-Rao (2012): any odd perfect exceeds 10^1500 with at least 101 prime factors.",
            "This walkthrough finds none below 200000 and verifies the Euler parity lemma.",
            "The Descartes-Frenicle-Sorli conjecture predicts a = 1 for the special prime exponent.",
        ],
        "requirements": [
            "One exhibited odd perfect number would settle existence affirmatively.",
            "A nonexistence proof must contradict the Euler form, not merely extend bounds.",
            "Any proof must handle the abundancy index constraints on both factors.",
            "Refereed publication and independent verification are required before any claim counts.",
        ],
        "standards": [
            "Euler L. De numeris amicabilibus. Opera Omnia; 1747 (Euler form).",
            "Standard: a claimed proof must survive refereed publication and independent verification.",
        ],
        "citations": [CIT_GUY, CIT_HARDY_WRIGHT, CIT_OCHEM_RAO],
    },
    {
        "key": "mersenne",
        "name": "Infinitely Many Mersenne Primes",
        "group": "Foundations",
        "ladder_rank": 5,
        "ladder_tier": "foundations",
        "problem": ("A Mersenne prime is a prime of the form 2^p - 1 with p prime, like 3, 7, 31, and 127. "
                    "Fifty-two are known. Are there infinitely many, or does the list eventually stop?"),
        "background": ("Marin Mersenne discussed these numbers in 1644, and Euclid had already linked them to even "
                       "perfect numbers: 2^(p-1)(2^p - 1) is perfect exactly when 2^p - 1 is prime. The search is now "
                       "carried out by the Great Internet Mersenne Prime Search, a distributed computing project. The "
                       "largest known prime of any kind is the Mersenne prime 2^136279841 - 1, found in October 2024 "
                       "by Luke Durant. The Lenstra-Pomerance-Wagstaff heuristic predicts about (e^gamma/ln 2) ln ln x "
                       "Mersenne primes below x, which suggests infinitude, but it is only a heuristic. This walkthrough "
                       "verifies the nine Mersenne exponents up to 61 and checks the heuristic prediction of 9.62 "
                       "against the actual count of 9."),
        "why_it_matters": ("Mersenne primes are the source of the largest known primes and of all even perfect numbers, "
                           "so their infinitude is tied to the infinitude of perfect numbers. A proof would be the first "
                           "infinitude result for an exponential prime sequence. The search itself drives distributed "
                           "computing and primality testing forward."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads Mersenne primes as the primes hiding in the doubling sequence: each "
                     "one is a place where 2^p - 1 lands exactly on a prime, and the Signature approach is to prove "
                     "the Lenstra-Pomerance-Wagstaff density by treating Mersenne numbers as prime constellations in "
                     "Lucas sequences."),
        "sig_solution": (
            LABEL + " Approach S-05: Lenstra-Pomerance-Wagstaff heuristic ascent. "
            "Assumptions: (A1) the residues of 2^p - 1 modulo small primes behave randomly enough for a sieve heuristic; "
            "(A2) the Wagstaff adjustment for the algebraic factorization structure is essentially correct; "
            "(A3) a weak form of the heuristic, infinitude rather than the exact count, is provable with current "
            "technology plus one new idea about prime divisors of Lucas sequences. "
            "Reasoning path: (S1) study the set of prime divisors of values of the Lucas sequence U_n = 2^n - 1; "
            "(S2) prove the primes dividing some Mersenne number are equidistributed enough for a lower-bound sieve; "
            "(S3) show the sifted count of prime values is positive infinitely often, giving infinitely many Mersenne "
            "primes; (S4) calibrate against the observed data, where the heuristic predicts 9.62 near 2^61 against 9 "
            "actual. "
            "Proposed mechanism: a constellation sieve on Lucas sequences - treat Mersenne primality as a prime pattern "
            "problem and import the bounded-gap sieve philosophy. "
            "What would confirm it: a proof that infinitely many Mersenne primes exist. "
            "What would kill it: a proof of finiteness, which no heuristic or computation suggests. "
            "What it does NOT claim: infinitude. The heuristic fits the data beautifully, but fitting is not proving, "
            "and the question stays open."),
        "key_points": [
            "Mersenne prime: prime of the form 2^p - 1; 52 known.",
            "Largest known: 2^136279841 - 1, found October 2024.",
            "Mersenne exponents up to 61 are exactly 2, 3, 5, 7, 13, 17, 19, 31, 61 (this walkthrough).",
            "LPW heuristic predicts 9.62 near 2^61; actual count is 9.",
            "Each Mersenne prime yields an even perfect number via the Euclid-Euler theorem.",
        ],
        "requirements": [
            "Infinitude needs a lower-bound sieve result for prime values of 2^p - 1.",
            "A finiteness proof would refute the conjecture; none exists.",
            "Any proof must handle the algebraic structure of Lucas sequences.",
            "Refereed publication and independent verification are required before any claim counts.",
        ],
        "standards": [
            "Standard: a claimed proof must survive refereed publication and independent verification.",
            "Computational records are maintained by the distributed search community and cross-checked.",
        ],
        "citations": [CIT_RIBENBOIM, CIT_GUY, CIT_HARDY_WRIGHT],
    },
    {
        "key": "sophie_germain",
        "name": "Sophie Germain Primes",
        "group": "Foundations",
        "ladder_rank": 6,
        "ladder_tier": "foundations",
        "problem": ("A Sophie Germain prime is a prime p for which 2p + 1 is also prime, like 11 (since 23 is prime) "
                    "or 83 (since 167 is prime). Are there infinitely many such primes?"),
        "background": ("Sophie Germain used these primes in her pioneering work on Fermat's Last Theorem, proving the "
                       "first case of the theorem for exponents p where 2p + 1 is also prime. That alone makes them "
                       "historically important. The infinitude question has been open since her time. Heuristics predict "
                       "about 2*C2*N/(ln N)^2 such primes below N, where C2 is the twin prime constant, and the data "
                       "fit well: this walkthrough counts 2058 Sophie Germain primes below 200000 against a heuristic "
                       "estimate of 1772. The largest known examples have hundreds of thousands of digits. Like twin "
                       "primes, they are a prime constellation problem, and no general method proves infinitude for any "
                       "nontrivial constellation."),
        "why_it_matters": ("These primes are the workhorses of cryptography-adjacent prime generation and of safe-prime "
                           "constructions, so their distribution matters practically. Theoretically, infinitude would be "
                           "the first constellation infinitude beyond arithmetic progressions. Germain herself would "
                           "surely want to know whether her primes go on forever."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads Sophie Germain primes as chained promises: p prime promises 2p + 1 "
                     "prime, and the Signature approach is to adapt the bounded-gap sieve machinery to catch this "
                     "two-term pattern infinitely often."),
        "sig_solution": (
            LABEL + " Approach S-06: prime-constellation density ascent. "
            "Assumptions: (A1) the pair (p, 2p+1) behaves like a prime k-tuple with the Hardy-Littlewood density "
            "2*C2/(ln x)^2; (A2) the Maynard-Tao sieve can be specialized to linear forms with a doubling relation; "
            "(A3) the parity barrier does not obstruct this specific constellation. "
            "Reasoning path: (S1) formulate Sophie Germain infinitude as a prime k-tuple problem for the forms "
            "(n, 2n+1); (S2) build sieve weights detecting both linear forms simultaneously; (S3) prove the required "
            "level of distribution for the moduli involved; (S4) extract a positive lower bound for the count, giving "
            "infinitude. "
            "Proposed mechanism: a targeted constellation sieve - the same philosophy that gave bounded prime gaps, "
            "aimed at the doubling pattern. "
            "What would confirm it: infinitely many Sophie Germain primes proved to exist. "
            "What would kill it: a finiteness proof, which nothing suggests. "
            "What it does NOT claim: infinitude. Germain used these primes to attack Fermat; two centuries later "
            "their infinitude is still open, and heuristics are not proofs."),
        "key_points": [
            "Sophie Germain prime p: both p and 2p + 1 are prime.",
            "This walkthrough counts 2058 below 200000; heuristic estimate 1772.",
            "Germain proved the first case of Fermat's Last Theorem for such exponents.",
            "Largest known examples have hundreds of thousands of digits.",
            "No nontrivial prime constellation is known to be infinite.",
        ],
        "requirements": [
            "Infinitude needs a sieve lower bound for the pattern (p, 2p+1).",
            "A finiteness proof would refute the conjecture; none exists.",
            "The parity barrier must be shown not to block this constellation.",
            "Refereed publication and independent verification are required before any claim counts.",
        ],
        "standards": [
            "Standard: a claimed proof must survive refereed publication and independent verification.",
            "Heuristic density: 2*C2*N/(ln N)^2 with C2 the twin prime constant.",
        ],
        "citations": [CIT_GUY, CIT_RIBENBOIM, CIT_HARDY_WRIGHT],
    },
    {
        "key": "beal",
        "name": "Beal Conjecture",
        "group": "Foundations",
        "ladder_rank": 7,
        "ladder_tier": "foundations",
        "problem": ("If x^p + y^q = z^r with x, y, z positive integers and p, q, r all greater than 2, then x, y, "
                    "and z must share a common prime factor. No counterexample with coprime bases has ever been found."),
        "background": ("Texas banker Andrew Beal proposed the conjecture in 1993 and put up a prize, now one million "
                       "US dollars administered through the American Mathematical Society, for a proof or a "
                       "counterexample. It generalizes Fermat's Last Theorem, which is the special case where the "
                       "exponents are equal and the bases are coprime. Solutions with a common factor are easy to find, "
                       "for example 2^5 + 2^5 = 2^6, so the conjecture is precisely about the coprime case. Extensive "
                       "computer searches have found no counterexample. This walkthrough searches x, y, z up to 40 with "
                       "exponents 3 through 6, finding 18 solutions, every one with a common prime factor and none "
                       "coprime."),
        "why_it_matters": ("Beal is the natural common generalization of Fermat's Last Theorem, and a proof would "
                           "complete the story Wiles began. The million-dollar prize makes it the most valuable open "
                           "problem an amateur can understand in one sentence. Either a proof or a counterexample would "
                           "be a landmark in Diophantine equations."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads Beal as a forbidden equation: coprime bases are not allowed to satisfy "
                     "x^p + y^q = z^r, and the Signature approach is to attach a Frey-type elliptic curve to any "
                     "hypothetical counterexample and derive a contradiction from modularity, the way Wiles did for "
                     "Fermat."),
        "sig_solution": (
            LABEL + " Approach S-07: Frey-curve descent. "
            "Assumptions: (A1) a coprime Beal solution yields a Frey-Hellegouarch elliptic curve with tightly "
            "constrained ramification; (A2) the mod-p Galois representation of that curve is modular of a small level, "
            "as in the proof of Fermat's Last Theorem; (A3) the level-lowering argument eliminates all possibilities "
            "for the exponent patterns. "
            "Reasoning path: (S1) assume a coprime solution to x^p + y^q = z^r with p, q, r > 2; (S2) construct the "
            "associated Frey curve, whose discriminant encodes the solution; (S3) apply modularity and level lowering "
            "to force the representation to come from a newform of small level; (S4) show no such newform exists for "
            "any exponent pattern, a contradiction. "
            "Proposed mechanism: the Wiles program, generalized - turn the Diophantine equation into a statement about "
            "Galois representations and let modularity do the killing. "
            "What would confirm it: a completed Frey-curve contradiction for all exponent patterns, winning the prize. "
            "What would kill it: one coprime solution with all exponents greater than 2, which would also win the prize. "
            "What it does NOT claim: a proof. The million-dollar prize is still unclaimed, and this is a proposed "
            "strategy, not a completed argument."),
        "key_points": [
            "Beal: x^p + y^q = z^r with p,q,r > 2 forces a common prime factor of x, y, z.",
            "Proposed 1993 by Andrew Beal; prize now US$1,000,000 via the American Mathematical Society.",
            "Generalizes Fermat's Last Theorem, proved by Wiles in 1995.",
            "This walkthrough: 18 solutions with a common factor, 0 coprime, in bounds x,y,z <= 40.",
            "Example allowed solution: 2^5 + 2^5 = 2^6 (common factor 2).",
        ],
        "requirements": [
            "One coprime solution with exponents above 2 would refute the conjecture and win the prize.",
            "A proof must handle all exponent patterns, not just equal exponents.",
            "The Frey-curve strategy needs modularity for the relevant Galois representations.",
            "The prize rules require publication in a refereed journal and a two-year waiting period.",
        ],
        "standards": [
            "American Mathematical Society. Beal Prize rules (US$1,000,000).",
            "Standard: a claimed proof must survive refereed publication and independent verification.",
        ],
        "citations": [CIT_GUY, CIT_CLAY, CIT_HARDY_WRIGHT],
    },
    {
        "key": "legendre",
        "name": "Legendre Conjecture",
        "group": "Foundations",
        "ladder_rank": 8,
        "ladder_tier": "foundations",
        "problem": ("Between every pair of consecutive perfect squares there is at least one prime. That is, for "
                    "every positive integer n, the interval from n^2 to (n+1)^2 always contains a prime."),
        "background": ("Adrien-Marie Legendre stated the conjecture centuries ago, and it remains one of the "
                       "simplest unsolved claims about prime gaps. The interval (n^2, (n+1)^2) has length 2n + 1, so "
                       "the conjecture says prime gaps near x are always shorter than about 2*sqrt(x). It would follow "
                       "immediately from the Riemann Hypothesis, which gives much stronger gap bounds, but it is open "
                       "unconditionally. Computational checks confirm it far beyond any range checkable by hand; this "
                       "walkthrough verifies every n up to 3000, finding as few as 2 primes in the sparsest interval. "
                       "Stronger conjectures like Oppermann and Andrica each imply Legendre."),
        "why_it_matters": ("Legendre is the cleanest test of our understanding of prime gaps: squares are the most "
                           "natural landmarks, and primes refusing to skip over any square interval would show the "
                           "primes are remarkably regular. A proof would give the first unconditional prime-gap bound "
                           "of the form O(sqrt(x)) and would be a major event in analytic number theory."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads Legendre as a no-skipping rule: the primes are not allowed to jump "
                     "clean over any square interval, and the Signature approach is to prove a prime-gap ceiling of "
                     "2*sqrt(p) + 1 from explicit zero-free regions for the zeta function."),
        "sig_solution": (
            LABEL + " Approach S-08: prime-gap ceiling descent. "
            "Assumptions: (A1) an explicit zero-free region for the Riemann zeta function yields a prime-gap bound "
            "below 2*sqrt(x) + 1 for all x; (A2) the finitely many small cases are checked by computation; "
            "(A3) the error terms in the explicit formula can be made fully explicit with manageable constants. "
            "Reasoning path: (S1) convert a zero-free region into a bound on psi(x + h) - psi(x); (S2) choose h = "
            "2*sqrt(x) + 1 and show the interval always contains prime weight; (S3) make every constant explicit so "
            "the argument covers all x, not just large x; (S4) verify the remaining small range directly. "
            "Proposed mechanism: an explicit-formula assault - turn zero-free regions into gap bounds with every "
            "constant nailed down. "
            "What would confirm it: a proved prime-gap bound below the interval length for all x. "
            "What would kill it: one n with no prime between n^2 and (n+1)^2. "
            "What it does NOT claim: a proof. Legendre would follow from the Riemann Hypothesis, but unconditionally "
            "it is open, and this is a proposed path, not a theorem."),
        "key_points": [
            "Legendre: a prime always lies strictly between n^2 and (n+1)^2.",
            "Equivalent to prime gaps near x staying below about 2*sqrt(x).",
            "Follows from the Riemann Hypothesis; open unconditionally.",
            "This walkthrough verifies n up to 3000; sparsest interval holds 2 primes.",
            "Implied by the stronger Andrica and Oppermann conjectures.",
        ],
        "requirements": [
            "One n with no prime in (n^2, (n+1)^2) would refute the conjecture.",
            "A proof needs an unconditional prime-gap bound below 2*sqrt(x) + 1.",
            "All constants must be explicit to cover small x as well as large.",
            "Refereed publication and independent verification are required before any claim counts.",
        ],
        "standards": [
            "Standard: a claimed proof must survive refereed publication and independent verification.",
            "Prime-gap bounds are measured against the Riemann Hypothesis prediction.",
        ],
        "citations": [CIT_GUY, CIT_HARDY_WRIGHT, CIT_MAZUR_STEIN],
    },
    {
        "key": "brocard_ramanujan",
        "name": "Brocard-Ramanujan Problem",
        "group": "Foundations",
        "ladder_rank": 9,
        "ladder_tier": "foundations",
        "problem": ("Find all integers n such that n! + 1 is a perfect square. The known solutions are n = 4 "
                    "(25 = 5^2), n = 5 (121 = 11^2), and n = 7 (5041 = 71^2). Are there any more?"),
        "background": ("Henri Brocard asked the question in 1876 and again in 1885, and Srinivasa Ramanujan asked it "
                       "independently in 1913, so it carries both names. Only the three solutions 4, 5, and 7 are "
                       "known. Berndt and Galway searched up to n = 10^9 in 2000 and found nothing new. The abc "
                       "conjecture would imply there are only finitely many solutions, but even finiteness is open "
                       "without it. This walkthrough checks n up to 22 and confirms exactly the three known solutions. "
                       "The problem is a Diophantine equation of exponential type, which is why it resists elementary "
                       "methods."),
        "why_it_matters": ("The problem is a perfect ambassador for exponential Diophantine equations: easy to state, "
                           "connected to deep conjectures like abc, and completely open. Settling it would either "
                           "exhibit a new solution or develop the methods to rule them out. It also serves as a "
                           "concrete test case for the power of the abc conjecture."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads n! + 1 = m^2 as a growth race: the factorial explodes while squares "
                     "stay rigid, and the Signature approach is to let the abc conjecture referee the race, bounding "
                     "n and reducing the infinite search to a finite check."),
        "sig_solution": (
            LABEL + " Approach S-09: abc-powered finiteness ascent. "
            "Assumptions: (A1) the abc conjecture holds with an explicit constant; (A2) the equation n! + 1 = m^2 "
            "can be rewritten in abc form with controlled radical; (A3) the resulting bound on n is small enough for "
            "a finite computational check. "
            "Reasoning path: (S1) write n! + 1 = m^2 as m^2 - n! = 1, an abc-type relation; (S2) apply the abc "
            "conjecture to bound the radical of the triple, forcing n below an explicit bound; (S3) check all n below "
            "the bound by direct computation, extending the Berndt-Galway search; (S4) conclude the solution list is "
            "complete. "
            "Proposed mechanism: a conditional finiteness proof - assume abc, derive an explicit bound, finish by "
            "computation. "
            "What would confirm it: a proof of abc plus the finite check, or a direct unconditional finiteness proof. "
            "What would kill it: a fourth solution, which computation has not found up to 10^9. "
            "What it does NOT claim: finiteness, let alone the full solution list. Without abc even finiteness is "
            "open, and this is a proposed conditional path, honestly labeled."),
        "key_points": [
            "Brocard-Ramanujan: n! + 1 = m^2; known solutions n = 4, 5, 7.",
            "Asked by Brocard (1876, 1885) and independently by Ramanujan (1913).",
            "Searched to n = 10^9 by Berndt and Galway (2000) with no new solutions.",
            "The abc conjecture implies only finitely many solutions.",
            "This walkthrough confirms exactly 4, 5, 7 below 23.",
        ],
        "requirements": [
            "A fourth solution would extend the list; none is known.",
            "Finiteness is open unconditionally; abc would imply it.",
            "Any proof must handle the exponential growth of the factorial.",
            "Refereed publication and independent verification are required before any claim counts.",
        ],
        "standards": [
            "Standard: a claimed proof must survive refereed publication and independent verification.",
            "The abc conjecture is the benchmark conditional hypothesis for this problem.",
        ],
        "citations": [CIT_GUY, CIT_HARDY_WRIGHT],
    },
    {
        "key": "three_cubes",
        "name": "Sums of Three Cubes",
        "group": "Foundations",
        "ladder_rank": 10,
        "ladder_tier": "foundations",
        "problem": ("Which integers k can be written as x^3 + y^3 + z^3 with x, y, z integers? Cubes modulo 9 are "
                    "only 0, 1, and 8, so k congruent to 4 or 5 modulo 9 is impossible. Does every other k work?"),
        "background": ("The mod-9 obstruction is elementary: since every cube is 0, 1, or 8 mod 9, sums of three "
                       "cubes avoid residues 4 and 5. For decades the question was whether the obstruction is the "
                       "only one. The last two numbers below 100, namely 33 and 42, were cracked in 2019: Booker found "
                       "33, and Booker and Sutherland found 42 using a massive distributed search. Solutions can be "
                       "enormous; the representation of 42 uses 19-digit numbers. This walkthrough searches with "
                       "|x|,|y|,|z| up to 200 and represents 34 of the 38 eligible k up to 50, missing only 30, 33, 39, "
                       "and 42 within those bounds, and it verifies the mod-9 obstruction is genuine."),
        "why_it_matters": ("The problem is the flagship of computational number theory: it shows how clever "
                           "parametrizations plus massive search can crack cases one at a time. Each solved k, like "
                           "42, becomes a cultural event. A general theorem would need to explain why the mod-9 "
                           "obstruction is the only one, which would be a deep statement about cubic forms."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads x^3 + y^3 + z^3 = k as a ladder of elliptic curves: fix z and the "
                     "equation becomes a curve in x and y, and the Signature approach is to climb curves of "
                     "increasing rank until a rational point appears for every eligible k."),
        "sig_solution": (
            LABEL + " Approach S-10: elliptic-curve ladder ascent. "
            "Assumptions: (A1) for each eligible k, some elliptic curve in the natural family has positive rank; "
            "(A2) rational points on these curves can be found by a bounded descent search; (A3) the mod-9 obstruction "
            "is the only local obstruction, so the Hasse principle nearly holds. "
            "Reasoning path: (S1) rewrite x^3 + y^3 + z^3 = k as an elliptic curve over Q(z) or via standard "
            "parametrizations; (S2) compute the rank and generators for the curve attached to each k; (S3) search for "
            "rational points up to a height bound derived from the regulator; (S4) lift each point to an integer "
            "triple. "
            "Proposed mechanism: a curve-by-curve constructive proof - one elliptic curve per k, each yielding its "
            "triple. "
            "What would confirm it: an explicit triple for every eligible k, or a theorem producing one. "
            "What would kill it: one eligible k proved to have no integer representation. "
            "What it does NOT claim: that every eligible k works. That is exactly what is open; the 2019 solutions "
            "of 33 and 42 show how hard individual cases are, and this is a proposed systematic path, not a theorem."),
        "key_points": [
            "Sums of three cubes: k = x^3 + y^3 + z^3; residues 4 and 5 mod 9 are impossible.",
            "33 solved by Booker (2019); 42 by Booker and Sutherland (2019) with 19-digit numbers.",
            "This walkthrough represents 34 of 38 eligible k up to 50 within |vars| <= 200.",
            "The mod-9 obstruction is proved; whether it is the only one is open.",
            "Solutions can be astronomically large even for small k.",
        ],
        "requirements": [
            "One eligible k with no representation would refute the hope; none is known.",
            "A general proof must produce triples for all eligible k, not just small ones.",
            "Any proof must explain why mod 9 is the only obstruction.",
            "Refereed publication and independent verification are required before any claim counts.",
        ],
        "standards": [
            "Standard: a claimed proof must survive refereed publication and independent verification.",
            "Computational solutions must be independently checkable by direct substitution.",
        ],
        "citations": [CIT_GUY, CIT_BOOKER_SUTHERLAND, CIT_HARDY_WRIGHT],
    },
    {
        "key": "gilbreath",
        "name": "Gilbreath Conjecture",
        "group": "Foundations",
        "ladder_rank": 11,
        "ladder_tier": "foundations",
        "problem": ("Write down the primes, then repeatedly replace the list by the absolute differences of "
                    "consecutive terms. The conjecture says the first term of every row is always 1."),
        "background": ("Norman Gilbreath observed the pattern in 1958: starting from 2, 3, 5, 7, 11, 13, the first "
                       "differences are 1, 2, 2, 4, 2, and iterating keeps producing a leading 1 in every row. It has "
                       "been verified for initial primes into the trillions, yet no proof exists. The conjecture is "
                       "about the fine structure of prime gaps: the iterated differences staying small at the front "
                       "means the gaps cannot conspire badly. This walkthrough runs the full difference table for the "
                       "primes below 20000, all 2261 rounds, and the leading term is 1 every single time. It is a rare "
                       "conjecture that anyone can test on a napkin for small cases."),
        "why_it_matters": ("Gilbreath is the most accessible unsolved problem about prime gaps: no analysis background "
                           "is needed to understand it, yet it encodes deep facts about how primes are spaced. A proof "
                           "would give a new structural theorem about prime gaps. It is also a wonderful advertisement "
                           "for experimental mathematics."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads Gilbreath as a collapse process: iterated differencing squeezes the "
                     "prime gaps, and the Signature approach is to prove the gaps are too well-behaved for the "
                     "leading term ever to escape 1."),
        "sig_solution": (
            LABEL + " Approach S-11: prime-gap control ascent. "
            "Assumptions: (A1) maximal prime gaps grow slowly enough that iterated absolute differences contract; "
            "(A2) the difference table can be modeled by a linear cellular process whose leading edge is stable; "
            "(A3) a sufficiently strong explicit prime-gap bound implies the leading-1 property at every depth. "
            "Reasoning path: (S1) express the k-th row entries as alternating binomial sums of the primes; "
            "(S2) bound these sums using maximal prime-gap estimates; (S3) show by induction on the rows that the "
            "first entry must be 1, using the fact that all entries stay small; (S4) verify the base rows by "
            "computation. "
            "Proposed mechanism: a gap-driven induction - control the prime gaps, and the difference table has no "
            "choice but to keep its leading 1. "
            "What would confirm it: a prime-gap theorem strong enough to force the leading 1 at every iteration depth. "
            "What would kill it: one starting row of primes whose difference table shows a leading term other than 1. "
            "What it does NOT claim: a proof. Verified here to 20000 and far beyond in the literature, conjectured "
            "for all primes, but still open, and this is a proposed path, honestly labeled."),
        "key_points": [
            "Gilbreath: iterated absolute differences of the primes always lead with 1.",
            "Observed by Norman Gilbreath in 1958; verified into the trillions.",
            "This walkthrough runs all 2261 rounds for primes below 20000 with leading 1 throughout.",
            "The first row is the prime gaps; deeper rows mix them binomially.",
            "Equivalent to a strong regularity statement about prime gaps.",
        ],
        "requirements": [
            "One row with a leading term other than 1 would refute the conjecture.",
            "A proof needs prime-gap bounds that control the whole difference table.",
            "The binomial-sum representation must be bounded at every depth.",
            "Refereed publication and independent verification are required before any claim counts.",
        ],
        "standards": [
            "Standard: a claimed proof must survive refereed publication and independent verification.",
            "Computational verifications must cover initial segments far beyond hand-checkable range.",
        ],
        "citations": [CIT_GUY, CIT_HARDY_WRIGHT],
    },
    {
        "key": "moving_sofa",
        "name": "Moving Sofa Problem",
        "group": "Foundations",
        "ladder_rank": 12,
        "ladder_tier": "foundations",
        "problem": ("What is the largest area of a shape that can be moved around a right-angled hallway of width 1? "
                    "The shape can be any connected rigid region; the hallway is an L-shape with unit-width arms."),
        "background": ("Leo Moser posed the problem informally in 1966, and it became famous through Martin Gardner. "
                       "Hammersley found a sofa with area pi/2 + 2/pi, about 2.2074, and proved no sofa exceeds "
                       "2*sqrt(2), about 2.8284. Gerver constructed an 18-piece sofa in 1992 with area about 2.2195, "
                       "the largest known, and described 18 curve segments forming its boundary. Kallus and Romik "
                       "proved in 2018 that no sofa exceeds 2.37, narrowing the gap. Romik later gave a proof of "
                       "optimality under an injectivity assumption, but the full problem remains open. This walkthrough "
                       "verifies the numerical chain 2.2074 < 2.2195 < 2.37 < 2.8284."),
        "why_it_matters": ("The moving sofa is the most famous unsolved problem in geometry that anyone can picture: "
                           "everyone has wrestled furniture around a corner. A solution would complete a beautiful "
                           "chapter in the calculus of variations and shape optimization. The techniques would apply "
                           "to motion planning, robotics, and packing problems."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads the moving sofa as a shape trying to be as large as possible while "
                     "slipping around the corner: the hallway walls carve the boundary arcs, and the Signature "
                     "approach is to parametrize every candidate, derive the optimality conditions on each arc, and "
                     "prove no asymmetric shape beats the symmetric Gerver form."),
        "sig_solution": (
            LABEL + " Approach S-12: parametric shape optimization. "
            "Assumptions: (A1) the optimal sofa is a balanced symmetric shape whose boundary arcs are determined by "
            "contact with the hallway walls, as in Gerver's 18-curve construction; (A2) the Euler-Lagrange conditions "
            "for the area functional under the movement constraints have a unique symmetric solution; (A3) asymmetric "
            "perturbations can be shown to decrease area via a second-variation argument. "
            "Reasoning path: (S1) parametrize candidate sofas by their rotation-angle envelope; (S2) write the area as "
            "a functional of the boundary arcs; (S3) derive first-order optimality conditions on each arc; (S4) show "
            "Gerver's shape is the unique critical point and that the second variation is negative definite. "
            "Proposed mechanism: a calculus-of-variations proof - turn the moving problem into an optimization problem "
            "and solve it. "
            "What would confirm it: a proof that Gerver's constant 2.2195 is optimal among all movable shapes. "
            "What would kill it: a sofa with area above 2.37, or any shape beating Gerver. "
            "What it does NOT claim: optimality. The gap between 2.2195 and 2.37 is still open, and this is a proposed "
            "path, honestly labeled."),
        "key_points": [
            "Moving sofa: largest area movable around a unit-width right-angle hallway.",
            "Hammersley sofa: about 2.2074; Gerver sofa: about 2.2195 (largest known).",
            "Upper bounds: 2.37 (Kallus-Romik 2018); trivial 2*sqrt(2) about 2.8284.",
            "Posed by Moser (1966); Gerver construction has 18 boundary arcs (1992).",
            "This walkthrough verifies the numerical chain of bounds.",
        ],
        "requirements": [
            "A sofa with area above 2.37 would break the best upper bound.",
            "Optimality needs the full calculus of variations, not just symmetric candidates.",
            "Any proof must handle arbitrary connected shapes, not only nice ones.",
            "Refereed publication and independent verification are required before any claim counts.",
        ],
        "standards": [
            "Standard: a claimed proof must survive refereed publication and independent verification.",
            "Area computations must be rigorous, not merely numerical.",
        ],
        "citations": [CIT_GUY, CIT_KALLUS_ROMIK],
    },
]

ENTRIES += [
    {
        "key": "near_square",
        "name": "Near-Square Primes",
        "group": "Compounded",
        "ladder_rank": 13,
        "ladder_tier": "compounded",
        "problem": ("Are there infinitely many primes of the form n^2 + 1, such as 2, 5, 17, 37, and 101? This is "
                    "the fourth of Landau's four famous problems from 1912."),
        "background": ("Edmund Landau listed four problems at the 1912 International Congress of Mathematicians that "
                       "he called unattackable: Goldbach, twin primes, Legendre, and infinitely many primes of the form "
                       "n^2 + 1. More than a century later, all four remain open. The n^2 + 1 problem asks for primes in "
                       "the values of the simplest nonlinear polynomial. The closest triumph is Friedlander and Iwaniec, "
                       "who proved in 1998 that x^2 + y^4 takes infinitely many prime values, a thin polynomial sequence "
                       "but not quite n^2 + 1. The Bunyakovsky conjecture would imply infinitude for n^2 + 1 and far "
                       "more. This walkthrough counts 6655 even n up to 100000 with n^2 + 1 prime, against a heuristic "
                       "estimate of 5962."),
        "why_it_matters": ("Polynomial prime values are the meeting point of algebra and analysis, and n^2 + 1 is the "
                           "simplest case where we are completely stuck. A proof would open the door to primes in "
                           "polynomial sequences generally. It would also finally retire one of Landau's four, a "
                           "century-old challenge."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads n^2 + 1 as the thinnest polynomial trail where primes might hide: the "
                     "values grow quadratically while primes thin out logarithmically, and the Signature approach is "
                     "to extend the Friedlander-Iwaniec sieve from x^2 + y^4 down to y = 1."),
        "sig_solution": (
            LABEL + " Approach S-13: polynomial-value sieve ascent. "
            "Assumptions: (A1) the Friedlander-Iwaniec bilinear sieve method can be pushed to handle the single-variable "
            "polynomial n^2 + 1; (A2) the level of distribution for the congruence n^2 = -1 mod p is sufficient for a "
            "lower-bound sieve; (A3) the parity barrier can be sidestepped for this specific thin sequence. "
            "Reasoning path: (S1) study primes dividing values of n^2 + 1, which are 2 and primes congruent to 1 mod 4; "
            "(S2) adapt the asymptotic sieve to the sequence a_n = n^2 + 1 with its restricted prime divisors; "
            "(S3) prove a positive lower bound for the prime values, giving infinitude; (S4) match the observed density "
            "against the Hardy-Littlewood constant 1.3728. "
            "Proposed mechanism: a thin-sequence sieve - take the x^2 + y^4 breakthrough and squeeze out the extra "
            "variable. "
            "What would confirm it: infinitely many primes of the form n^2 + 1 proved to exist. "
            "What would kill it: a proof that n^2 + 1 is prime only finitely often, which nothing suggests. "
            "What it does NOT claim: infinitude. Landau listed it in 1912, Friedlander-Iwaniec got close in 1998, and "
            "it is still open; this is a proposed path, honestly labeled."),
        "key_points": [
            "Near-square primes: primes of the form n^2 + 1; infinitude unknown.",
            "Landau's fourth problem, posed at the 1912 ICM; all four Landau problems remain open.",
            "Friedlander-Iwaniec (1998): infinitely many primes of the form x^2 + y^4.",
            "This walkthrough: 6655 hits below 100000 against heuristic estimate 5962.",
            "Bunyakovsky conjecture would imply infinitude and much more.",
        ],
        "requirements": [
            "Infinitude needs a lower-bound sieve for the thin sequence n^2 + 1.",
            "A finiteness proof would refute the conjecture; none exists.",
            "The parity barrier is the central technical obstacle.",
            "Refereed publication and independent verification are required before any claim counts.",
        ],
        "standards": [
            "Standard: a claimed proof must survive refereed publication and independent verification.",
            "Heuristic density uses the Hardy-Littlewood constant 1.3728 for n^2 + 1.",
        ],
        "citations": [CIT_GUY, CIT_HARDY_WRIGHT, CIT_FRIEDLANDER_IWANIEC],
    },
    {
        "key": "andrica",
        "name": "Andrica Conjecture",
        "group": "Compounded",
        "ladder_rank": 14,
        "ladder_tier": "compounded",
        "problem": ("For consecutive primes p_n and p_{n+1}, the difference of their square roots is always less "
                    "than 1. That is, sqrt(p_{n+1}) - sqrt(p_n) < 1 for every n."),
        "background": ("Dorin Andrica stated the conjecture in 1986, building on earlier observations about prime "
                       "gaps. It is a clean, sharp claim: prime gaps can never reach 2*sqrt(p) + 1. It implies "
                       "Legendre's conjecture, since a prime gap below 2*sqrt(p) + 1 guarantees a prime between n^2 "
                       "and (n+1)^2. Every computed prime gap table confirms it with enormous margin; this walkthrough "
                       "checks all primes below 2000000 and finds the largest sqrt-gap is only 0.670873, at the pair "
                       "(7, 11). The conjecture would follow from the Riemann Hypothesis, but unconditionally it is "
                       "open. It is one of the sharpest known unproved prime-gap statements."),
        "why_it_matters": ("Andrica is the strongest simple prime-gap conjecture, and proving it would give the "
                           "first clean unconditional gap bound of the form O(sqrt(p)). It sits exactly at the "
                           "boundary of what current methods can almost reach. A proof would likely imply Legendre "
                           "and sharpen our whole picture of prime distribution."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads Andrica as a speed limit on prime gaps: no gap may stretch to "
                     "2*sqrt(p) + 1, and the Signature approach is to derive that speed limit from explicit zero-free "
                     "regions for the zeta function."),
        "sig_solution": (
            LABEL + " Approach S-14: square-root gap descent. "
            "Assumptions: (A1) an explicit zero-free region for zeta yields prime gaps below 2*sqrt(p) + 1 for all p; "
            "(A2) the constants in the explicit formula can be made small enough to cover the whole range; "
            "(A3) the small primes are checked directly, as in the walkthrough. "
            "Reasoning path: (S1) note sqrt(p_{n+1}) - sqrt(p_n) < 1 is equivalent to the gap bound p_{n+1} - p_n < "
            "2*sqrt(p_n) + 1; (S2) convert a zero-free region into an explicit bound on prime gaps via the explicit "
            "formula; (S3) optimize the constants until the bound beats 2*sqrt(p) + 1 everywhere; (S4) check the "
            "remaining small range by computation. "
            "Proposed mechanism: an explicit-formula gap theorem - turn zero-free regions into the sharp Andrica "
            "bound. "
            "What would confirm it: a proved prime-gap bound of 2*sqrt(p) + 1 for all primes. "
            "What would kill it: one prime pair violating the sqrt-gap inequality. "
            "What it does NOT claim: a proof. Andrica implies Legendre and both are open; the largest observed "
            "sqrt-gap is 0.670873, far below 1, but data are not proof, and this is a proposed path, honestly labeled."),
        "key_points": [
            "Andrica: sqrt(p_{n+1}) - sqrt(p_n) < 1 for all consecutive primes.",
            "Equivalent to prime gaps below 2*sqrt(p) + 1; implies Legendre's conjecture.",
            "This walkthrough: max sqrt-gap 0.670873 at (7, 11) for primes below 2000000.",
            "Follows from the Riemann Hypothesis; open unconditionally.",
            "Stated by Dorin Andrica in 1986.",
        ],
        "requirements": [
            "One violating prime pair would refute the conjecture.",
            "A proof needs an unconditional gap bound of 2*sqrt(p) + 1.",
            "Constants must be explicit to cover all primes, small and large.",
            "Refereed publication and independent verification are required before any claim counts.",
        ],
        "standards": [
            "Standard: a claimed proof must survive refereed publication and independent verification.",
            "Prime-gap bounds are measured against the Riemann Hypothesis prediction.",
        ],
        "citations": [CIT_GUY, CIT_HARDY_WRIGHT, CIT_MAZUR_STEIN],
    },
    {
        "key": "oppermann",
        "name": "Oppermann Conjecture",
        "group": "Compounded",
        "ladder_rank": 15,
        "ladder_tier": "compounded",
        "problem": ("For every n greater than 1, there is a prime between n(n-1) and n^2, and also a prime between "
                    "n^2 and n(n+1). The squares are bracketed by primes on both sides."),
        "background": ("Ludvig Oppermann stated the conjecture in 1882 in an unpublished lecture, and it has been "
                       "open ever since. It is strictly stronger than Legendre's conjecture, because each half-interval "
                       "has length n, half the length of Legendre's interval. It is also stronger than the claim that "
                       "prime gaps below x^2 stay under x. Computational verification reaches far; this walkthrough "
                       "checks every n up to 3000 and finds primes in both half-intervals throughout. Like Legendre, "
                       "it would follow from the Riemann Hypothesis. It is a natural sharpening that shows how much "
                       "room the data suggest beyond what anyone can prove."),
        "why_it_matters": ("Oppermann measures exactly how much stronger than Legendre the truth might be: the data "
                           "suggest primes near squares twice as often as Legendre requires. Proving it would give "
                           "prime-gap bounds below n near n^2, a genuine advance. It is the right intermediate target "
                           "between Legendre and the full Riemann Hypothesis predictions."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads Oppermann as Legendre with the interval cut in half: primes must "
                     "appear twice as often near squares, and the Signature approach is to sharpen explicit prime-gap "
                     "bounds until they beat intervals of length n."),
        "sig_solution": (
            LABEL + " Approach S-15: half-interval prime descent. "
            "Assumptions: (A1) prime gaps near x^2 stay below x for all large x, provable from an explicit zero-free "
            "region; (A2) the constants can be made to work for every n, not just asymptotically; (A3) small n are "
            "checked computationally. "
            "Reasoning path: (S1) reduce Oppermann to the gap bound p_{n+1} - p_n < n near n^2; (S2) derive this bound "
            "from the explicit formula with a strong zero-free region; (S3) optimize constants to cover the whole "
            "range; (S4) verify small n directly. "
            "Proposed mechanism: a sharpened explicit-formula argument - push the gap technology from 2n down to n. "
            "What would confirm it: a proved prime-gap bound below n near n^2 for all n. "
            "What would kill it: one n lacking a prime in either half-interval. "
            "What it does NOT claim: a proof. Stronger than Legendre and equally open; this is a proposed path, "
            "honestly labeled."),
        "key_points": [
            "Oppermann: primes in both (n(n-1), n^2) and (n^2, n(n+1)) for every n > 1.",
            "Strictly stronger than Legendre; intervals are half as long.",
            "Stated by Ludvig Oppermann in 1882; open ever since.",
            "This walkthrough verifies n up to 3000 in both half-intervals.",
            "Follows from the Riemann Hypothesis; open unconditionally.",
        ],
        "requirements": [
            "One n missing a prime in either half-interval would refute the conjecture.",
            "A proof needs prime gaps below n near n^2, unconditionally.",
            "Constants must be explicit across the whole range.",
            "Refereed publication and independent verification are required before any claim counts.",
        ],
        "standards": [
            "Standard: a claimed proof must survive refereed publication and independent verification.",
            "Prime-gap bounds are measured against the Riemann Hypothesis prediction.",
        ],
        "citations": [CIT_GUY, CIT_HARDY_WRIGHT, CIT_MAZUR_STEIN],
    },
    {
        "key": "cramer",
        "name": "Cramer Conjecture",
        "group": "Compounded",
        "ladder_rank": 16,
        "ladder_tier": "compounded",
        "problem": ("Prime gaps are never much larger than (log p)^2. Precisely, the ratio of the gap after p to "
                    "(log p)^2 should tend to 1 at its largest, so gaps of order (log p)^2 are the biggest possible."),
        "background": ("Harald Cramer proposed the conjecture in 1936 based on a probabilistic model of the primes, "
                       "treating each integer n as prime with probability 1/log n independently. The model predicts "
                       "maximal gaps around (log p)^2, and the data agree beautifully: this walkthrough measures the "
                       "maximal merit, gap divided by (log p)^2, as 0.6813 at the prime pair (370261, 370373) for "
                       "primes below 2000000. The largest known merit values approach 1 from below but have never "
                       "reached it. Granville has argued the constant might be larger than 1, so even the refined "
                       "statement is debated. The conjecture is far beyond current proof technology."),
        "why_it_matters": ("Cramer is the flagship prediction of the probabilistic view of primes, and it quantifies "
                           "exactly how irregular the primes can be. A proof would validate the random model at its "
                           "most extreme. The debate over the constant shows how even heuristics need constant "
                           "testing against data."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads Cramer as the primes obeying a random speed limit: gaps may reach "
                     "(log p)^2 but never essentially exceed it, and the Signature approach is to make the random "
                     "model rigorous through sieve methods with random-like error terms."),
        "sig_solution": (
            LABEL + " Approach S-16: random-model gap ascent. "
            "Assumptions: (A1) the primes behave like Cramer's random model at the level of maximal gaps; "
            "(A2) a sieve with well-controlled error terms can certify gaps up to (1 + epsilon)(log p)^2; "
            "(A3) the Granville correction, if real, can be incorporated without breaking the upper bound. "
            "Reasoning path: (S1) model prime gaps via the Cramer random model to predict the (log p)^2 scale; "
            "(S2) develop a sieve upper bound for prime gaps with the random-model main term; (S3) show the error "
            "terms are smaller than the main term, giving gaps O((log p)^2); (S4) refine toward the constant 1. "
            "Proposed mechanism: a rigorous random model - turn the probabilistic heuristic into a sieve theorem. "
            "What would confirm it: a proved upper bound of (1 + o(1))(log p)^2 on prime gaps. "
            "What would kill it: gaps exceeding (log p)^2 by an unbounded factor, which the data do not show. "
            "What it does NOT claim: the constant 1. The model predicts it, Granville questions it, and proof is far "
            "away; this is a proposed path, honestly labeled."),
        "key_points": [
            "Cramer: maximal prime gaps are O((log p)^2), with lim sup of gap/(log p)^2 equal to 1.",
            "Proposed by Harald Cramer in 1936 from a probabilistic model of the primes.",
            "This walkthrough: max merit 0.6813 at (370261, 370373) for primes below 2000000.",
            "Granville has suggested the true constant may exceed 1.",
            "Far beyond current proof technology.",
        ],
        "requirements": [
            "Gaps exceeding (log p)^2 by an unbounded factor would refute the conjecture.",
            "A proof needs a sieve upper bound matching the random-model prediction.",
            "The constant question (1 versus larger) must be resolved by the proof.",
            "Refereed publication and independent verification are required before any claim counts.",
        ],
        "standards": [
            "Standard: a claimed proof must survive refereed publication and independent verification.",
            "Merit gap/(log p)^2 is the standard measure of large prime gaps.",
        ],
        "citations": [CIT_GUY, CIT_HARDY_WRIGHT, CIT_MAZUR_STEIN],
    },
    {
        "key": "lehmer",
        "name": "Lehmer Totient Problem",
        "group": "Compounded",
        "ladder_rank": 17,
        "ladder_tier": "compounded",
        "problem": ("Is there a composite number n such that phi(n) divides n - 1? Here phi is Euler's totient "
                    "function, counting numbers below n that are coprime to n. For prime n, phi(n) = n - 1 always "
                    "divides n - 1, so the question is whether any composite number shares this property."),
        "background": ("D. H. Lehmer asked the question in 1932. No such composite number is known, and this "
                       "walkthrough searches all composites up to 3000000 and finds none. Any example would have to "
                       "be enormous: results by Hagis and others show it must be odd, squarefree, and have many "
                       "distinct prime factors, with lower bounds reaching far beyond computational range. Carmichael "
                       "numbers satisfy a related but different condition, so they are not examples. The problem is a "
                       "clean test of our understanding of the totient function, and it has resisted all attacks for "
                       "over ninety years."),
        "why_it_matters": ("The totient function is central to cryptography, especially RSA, so understanding its "
                           "values matters practically. A Lehmer composite would be a strange new kind of number with "
                           "potential cryptographic interest. A proof of nonexistence would be a deep structural "
                           "theorem about phi."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads Lehmer as a divisibility trap: phi(n) dividing n - 1 forces n into "
                     "an ever-tighter corner of factor-count and size constraints, and the Signature approach is to "
                     "push those constraints until no corner remains."),
        "sig_solution": (
            LABEL + " Approach S-17: Korselt-type descent. "
            "Assumptions: (A1) any Lehmer composite is odd, squarefree, and has at least k distinct prime factors, "
            "with k improvable by current methods; (A2) the product of the first k primes grows fast enough to force "
            "a contradiction with the divisibility condition; (A3) the prime-factor lower bounds can be raised "
            "systematically. "
            "Reasoning path: (S1) from phi(n) | (n - 1) with n composite, prove n is odd and squarefree; "
            "(S2) show n must have many distinct prime factors, improving the Hagis-type bounds; "
            "(S3) combine the factor-count bound with size estimates to get a contradiction; "
            "(S4) alternatively, construct an example if the bounds permit one. "
            "Proposed mechanism: a constraint squeeze - raise the lower bounds on factor count and size until they "
            "contradict the divisibility. "
            "What would confirm it: an exhibited Lehmer composite, or a completed impossibility proof. "
            "What would kill the approach: the factor-count bounds stalling below a contradiction. "
            "What it does NOT claim: either outcome. Lehmer asked in 1932, no example is known, none is ruled out, "
            "and this is a proposed path, honestly labeled."),
        "key_points": [
            "Lehmer: does composite n exist with phi(n) dividing n - 1?",
            "Asked by D. H. Lehmer in 1932; no example known.",
            "This walkthrough searches composites to 3000000 and finds none.",
            "Any example must be odd, squarefree, with many distinct prime factors.",
            "Carmichael numbers satisfy a different condition and are not examples.",
        ],
        "requirements": [
            "One exhibited composite with phi(n) | (n-1) would settle existence.",
            "A nonexistence proof must contradict the factor-count constraints.",
            "Bounds must be raised systematically, not just computationally.",
            "Refereed publication and independent verification are required before any claim counts.",
        ],
        "standards": [
            "Standard: a claimed proof must survive refereed publication and independent verification.",
            "Factor-count lower bounds are the benchmark progress measure.",
        ],
        "citations": [CIT_GUY, CIT_HARDY_WRIGHT],
    },
    {
        "key": "odd_weird",
        "name": "Odd Weird Numbers",
        "group": "Compounded",
        "ladder_rank": 18,
        "ladder_tier": "compounded",
        "problem": ("A weird number is abundant but not semiperfect: the sum of its divisors exceeds twice the "
                    "number, yet no subset of its proper divisors sums to the number itself. The smallest is 70. "
                    "Every known weird number is even. Does an odd weird number exist?"),
        "background": ("Weird numbers were defined in the 1970s, and 70 is the smallest: its proper divisors sum to "
                       "74, exceeding 70, but no subset sums to exactly 70. All known weird numbers are even, and "
                       "none odd is known. Exhaustive searches have ruled out odd weird numbers below 10^21. The "
                       "abundancy condition sigma(n) > 2n is easy to satisfy for odd n, but the semiperfect condition, "
                       "that some subset of divisors sums to n, seems to always hold for the odd abundant numbers "
                       "found so far. This walkthrough tests every odd abundant number below 30000 with an exact "
                       "subset-sum check and finds zero weird numbers. The question connects divisor sums, subset sums, "
                       "and the structure of odd abundant numbers."),
        "why_it_matters": ("Odd weird numbers would reveal a surprising asymmetry between even and odd divisor "
                           "structures. Their existence or nonexistence is a clean problem in additive number theory "
                           "with connections to the subset-sum problem. Either answer would sharpen our understanding "
                           "of how divisors combine."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads odd weird numbers as missing persons: even weird numbers exist, so "
                     "odd ones should too unless some structural law forbids them, and the Signature approach is to "
                     "narrow the abundancy-index window where they could hide until it closes or one walks out."),
        "sig_solution": (
            LABEL + " Approach S-18: abundancy-index ascent. "
            "Assumptions: (A1) any odd weird number has abundancy index sigma(n)/n in a narrow computable window; "
            "(A2) the subset-sum obstruction can be characterized via the divisor structure; (A3) extending the search "
            "window systematically will either find one or prove the window empty. "
            "Reasoning path: (S1) bound the abundancy index of odd weird candidates using divisor-count arguments; "
            "(S2) for each candidate shape, run the subset-sum test to check semiperfectness; (S3) extend the search "
            "to larger bounds with smarter pruning; (S4) either exhibit an example or prove the constraints are "
            "incompatible. "
            "Proposed mechanism: a window search - confine where odd weird numbers can live, then search or rule out. "
            "What would confirm it: an exhibited odd weird number. "
            "What would kill it: a proof that odd abundant numbers are always semiperfect. "
            "What it does NOT claim: either outcome. None are known below 10^21, none are ruled out above it, and "
            "this is a proposed path, honestly labeled."),
        "key_points": [
            "Weird: abundant but not semiperfect; smallest is 70 (even).",
            "No odd weird number is known; none exist below 10^21.",
            "This walkthrough subset-sum tests every odd abundant below 30000: zero weird.",
            "Abundant means sigma(n) > 2n; semiperfect means some divisors sum to n.",
            "The question links divisor sums with the subset-sum problem.",
        ],
        "requirements": [
            "One exhibited odd weird number would settle existence.",
            "A nonexistence proof must show odd abundant implies semiperfect.",
            "Search bounds must be extended systematically with exact subset-sum checks.",
            "Refereed publication and independent verification are required before any claim counts.",
        ],
        "standards": [
            "Standard: a claimed proof must survive refereed publication and independent verification.",
            "Search bounds are the benchmark progress measure.",
        ],
        "citations": [CIT_GUY, CIT_HARDY_WRIGHT],
    },
    {
        "key": "aliquot",
        "name": "Aliquot Sequence Termination",
        "group": "Compounded",
        "ladder_rank": 19,
        "ladder_tier": "compounded",
        "problem": ("The aliquot sequence of n replaces each term by the sum of its proper divisors, s(n) = "
                    "sigma(n) - n. Does every such sequence eventually reach 1, a perfect number, or an amicable "
                    "cycle? Or do some sequences grow forever?"),
        "background": ("Catalan conjectured in 1888 that all aliquot sequences terminate, and Dickson extended the "
                       "question to allow cycles. Perfect numbers are fixed points and amicable pairs are 2-cycles, so "
                       "termination includes those outcomes. The famous test case is 276: its sequence runs for "
                       "thousands of terms without terminating, and it remains open. Below 1000, the sequences "
                       "starting at 276, 552, 564, 660, and 966 are the celebrated open cases. This walkthrough "
                       "classifies every starting value below 1000: 961 terminate, 22 reach cycles, and 16 remain "
                       "open at the computation cap, merging into just 7 distinct families. The study of drivers, "
                       "persistent small-factor patterns guiding the sequences, is the modern approach."),
        "why_it_matters": ("Aliquot sequences are the oldest dynamical system in number theory, and the termination "
                           "question asks whether divisor sums always settle down. A proof would tame a chaotic-looking "
                           "process; a divergent sequence would be a shocking discovery. The driver theory developed "
                           "for the problem already illuminates how divisor sums evolve."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads aliquot sequences as rivers guided by drivers: small prime factors "
                     "steer the flow, and the Signature approach is to classify every driver and prove each one "
                     "either dams the river into a cycle or lets it drain to 1."),
        "sig_solution": (
            LABEL + " Approach S-19: driver-action ascent. "
            "Assumptions: (A1) every aliquot sequence is eventually guided by a driver, a persistent pattern of small "
            "prime factors; (A2) the set of possible drivers can be completely classified; (A3) each driver class can "
            "be shown to terminate or cycle via a monotonic quantity. "
            "Reasoning path: (S1) formalize the driver concept: the gcd structure that persists along the sequence; "
            "(S2) enumerate all possible drivers and their transitions; (S3) for each driver, find a Lyapunov-like "
            "quantity that forces termination or cycling; (S4) handle the merger phenomenon, where sequences join, as "
            "in the walkthrough's 7 families. "
            "Proposed mechanism: a driver classification proof - tame every possible steering pattern. "
            "What would confirm it: a proof that every aliquot sequence terminates or cycles. "
            "What would kill it: one sequence proved to diverge to infinity. "
            "What it does NOT claim: termination. The sequence starting at 276 alone keeps the question open after "
            "more than a century, and this is a proposed path, honestly labeled."),
        "key_points": [
            "Aliquot sequence: iterate s(n) = sigma(n) - n; question: does it always settle?",
            "Catalan (1888) conjectured termination; Dickson allowed cycles.",
            "Famous open case: 276, whose sequence runs thousands of terms.",
            "This walkthrough: below 1000, 961 terminate, 22 cycle, 16 open at cap in 7 families.",
            "Perfect numbers are fixed points; amicable pairs are 2-cycles.",
        ],
        "requirements": [
            "One sequence proved divergent would refute the termination hope.",
            "A proof must classify all drivers and their long-term behavior.",
            "The merger of sequences into families must be handled, not just single sequences.",
            "Refereed publication and independent verification are required before any claim counts.",
        ],
        "standards": [
            "Standard: a claimed proof must survive refereed publication and independent verification.",
            "Driver theory is the benchmark framework for the problem.",
        ],
        "citations": [CIT_GUY, CIT_HARDY_WRIGHT],
    },
    {
        "key": "perfect_cuboid",
        "name": "Perfect Cuboid",
        "group": "Compounded",
        "ladder_rank": 20,
        "ladder_tier": "compounded",
        "problem": ("Does there exist a rectangular box with integer edges, integer face diagonals, and an integer "
                    "space diagonal? Such a box is called a perfect cuboid, and none has ever been found."),
        "background": ("Euler found integer boxes with integer face diagonals, called Euler bricks; the smallest is "
                       "44 by 117 by 240. But in every known Euler brick the space diagonal is irrational, and no box "
                       "with all seven lengths integral is known. The problem is ancient in spirit: it asks for a "
                       "three-dimensional Pythagorean theorem with all quantities integral. Exhaustive searches with "
                       "edges into the billions have found nothing. Parametrizations of Euler bricks are known, but "
                       "the extra space-diagonal condition resists them all. This walkthrough searches all boxes with "
                       "edges up to 300 via Pythagorean pairs and finds zero perfect cuboids."),
        "why_it_matters": ("The perfect cuboid is the most famous unsolved Diophantine problem in three dimensions, "
                           "and it connects Pythagorean triples, elliptic curves, and K3 surfaces. An example would be "
                           "a computational triumph; a nonexistence proof would need deep arithmetic geometry. Either "
                           "way, the problem sits at a rich crossroads."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads the perfect cuboid as the missing seventh length: Euler bricks give "
                     "six integral lengths and the space diagonal refuses to cooperate, and the Signature approach is "
                     "to lift the problem to a K3 surface and run a Mordell-Weil sieve on its rational points."),
        "sig_solution": (
            LABEL + " Approach S-20: elliptic-surface descent. "
            "Assumptions: (A1) the perfect cuboid conditions define a K3 surface whose rational points parametrize "
            "candidates; (A2) the Mordell-Weil group of the relevant elliptic fibration can be computed; "
            "(A3) a sieve over the rational points can rule out the integral-diagonals condition. "
            "Reasoning path: (S1) parametrize Euler bricks and impose the space-diagonal integrality; (S2) translate "
            "to a question about rational points on a specific K3 surface; (S3) compute the Mordell-Weil group and "
            "run a descent sieve; (S4) either find a point giving a perfect cuboid or prove none exists. "
            "Proposed mechanism: an arithmetic-geometry sieve - turn the box into a surface and let descent decide. "
            "What would confirm it: an exhibited perfect cuboid, or a proof that none exists. "
            "What would kill the approach: the sieve stalling with unresolved residue classes. "
            "What it does NOT claim: existence or nonexistence. Both are open, searches to the billions found "
            "nothing, and this is a proposed path, honestly labeled."),
        "key_points": [
            "Perfect cuboid: integer edges, integer face diagonals, integer space diagonal; none known.",
            "Euler bricks have integer face diagonals but irrational space diagonal; smallest is 44, 117, 240.",
            "Searched with edges into the billions; nothing found.",
            "This walkthrough checks all boxes with edges up to 300: zero perfect cuboids.",
            "The conditions define a K3 surface, linking the problem to arithmetic geometry.",
        ],
        "requirements": [
            "One exhibited perfect cuboid would settle existence.",
            "A nonexistence proof must handle the K3 surface, not just extend searches.",
            "Parametrizations of Euler bricks are known; the space diagonal is the hard condition.",
            "Refereed publication and independent verification are required before any claim counts.",
        ],
        "standards": [
            "Standard: a claimed proof must survive refereed publication and independent verification.",
            "Any claimed example must have all seven lengths verified integral.",
        ],
        "citations": [CIT_GUY, CIT_HARDY_WRIGHT],
    },
    {
        "key": "magic_square",
        "name": "Magic Square of Squares",
        "group": "Compounded",
        "ladder_rank": 21,
        "ladder_tier": "compounded",
        "problem": ("Is there a 3x3 magic square whose nine entries are distinct perfect squares? Rows, columns, and "
                    "both diagonals must all sum to the same magic constant."),
        "background": ("The problem is famous partly because of the Parker square: in 2016 Matt Parker constructed a "
                       "3x3 square of squares on a Numberphile video in which the rows, columns, and one diagonal sum "
                       "to 3051, but the other diagonal sums to 4107, and some entries repeat. It became an internet "
                       "meme and a mascot for noble failure. It has been proved that a magic square of distinct squares "
                       "would need enormous entries, far beyond computational search. Whether one exists at all, or "
                       "whether it is impossible, remains open. This walkthrough exhaustively searches all 3x3 squares "
                       "with entries up to 400: it finds 32 fully magic ones, all with repeated entries, and zero "
                       "with 9 distinct entries."),
        "why_it_matters": ("The problem is the most charming unsolved problem in recreational mathematics, and the "
                           "Parker square made it famous worldwide. A construction would be a delight; an impossibility "
                           "proof would need serious number theory about quadratic forms. It shows how a puzzle can "
                           "encode deep mathematics."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads the magic square of squares as a near-miss begging to be fixed: the "
                     "Parker square gets everything right except one diagonal, and the Signature approach is to "
                     "parametrize the semi-magic family and drive the diagonal defect to zero."),
        "sig_solution": (
            LABEL + " Approach S-21: near-miss refinement. "
            "Assumptions: (A1) the Parker near-miss sits in a parametrized family of 3x3 semi-magic squares of "
            "squares; (A2) the diagonal defect is a rational function on the parameter space that can be minimized; "
            "(A3) either the defect reaches zero at some rational point or it is bounded away from zero, proving "
            "impossibility. "
            "Reasoning path: (S1) parametrize 3x3 squares of squares with rows, columns, and one diagonal magic; "
            "(S2) express the remaining diagonal defect as a function of the parameters; (S3) search the parameter "
            "space for a zero of the defect, or prove a positive lower bound; (S4) lift a zero to a true magic "
            "square of squares. "
            "Proposed mechanism: a defect-minimization proof - turn the near-miss into a variable and optimize it. "
            "What would confirm it: an exhibited 3x3 magic square of distinct squares, or a proof of impossibility. "
            "What would kill the approach: the defect proved bounded away from zero without yielding impossibility. "
            "What it does NOT claim: existence. The Parker square shows how close failure can look, with rows, "
            "columns, and one diagonal at 3051 and the other diagonal at 4107, and this is a proposed path, honestly "
            "labeled."),
        "key_points": [
            "Magic square of squares: 3x3, all entries perfect squares, all lines summing equally.",
            "The Parker square (2016): rows, columns, one diagonal sum to 3051; other diagonal 4107; entries repeat.",
            "Proved: a distinct-entry example would need enormous entries.",
            "This walkthrough: 32 fully magic squares with entries up to 400, all with repeats; 0 with 9 distinct.",
            "Existence and impossibility are both open.",
        ],
        "requirements": [
            "One exhibited example with distinct square entries would settle existence.",
            "An impossibility proof must use the theory of quadratic forms.",
            "The Parker near-miss must be understood as a boundary case, not a solution.",
            "Refereed publication and independent verification are required before any claim counts.",
        ],
        "standards": [
            "Standard: a claimed proof must survive refereed publication and independent verification.",
            "A claimed example must have all eight lines verified equal.",
        ],
        "citations": [CIT_GUY],
    },
    {
        "key": "singmaster",
        "name": "Singmaster Conjecture",
        "group": "Compounded",
        "ladder_rank": 22,
        "ladder_tier": "compounded",
        "problem": ("In Pascal's triangle, most numbers appear a few times. The number 1 appears infinitely often. "
                    "Does any other number appear infinitely often, or is there a universal bound on how many times "
                    "a number greater than 1 can appear?"),
        "background": ("David Singmaster conjectured in 1971 that the multiplicity of any integer greater than 1 in "
                       "Pascal's triangle is bounded, possibly by a small constant like 8 or 12. The champion is "
                       "3003, which appears 8 times: as C(3003,1), C(3003,3002), C(78,2), C(78,76), C(15,5), C(15,10), "
                       "C(14,6), and C(14,8). Abbott, Erdos, and Hanson proved the multiplicity is O(log n), which "
                       "grows without bound but very slowly, so boundedness remains open. This walkthrough examines "
                       "rows 0 through 500 and finds the highest multiplicity, excluding 1, is 6, attained at 3003. "
                       "The conjecture connects binomial coefficients with exponential Diophantine equations."),
        "why_it_matters": ("Singmaster asks whether Pascal's triangle can repeat a value arbitrarily often, a basic "
                           "question about the most famous array in mathematics. A proof would show binomial "
                           "coefficients are more rigid than they look. The exponential Diophantine methods needed "
                           "would have wide applications."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads Singmaster as a rigidity claim: binomial coefficients refuse to repeat "
                     "too often, and the Signature approach is to show each multiplicity equation is a finite "
                     "exponential Diophantine problem, so no value can recur without bound."),
        "sig_solution": (
            LABEL + " Approach S-22: Diophantine finiteness ascent. "
            "Assumptions: (A1) each equation C(n,k) = C(m,j) with distinct pairs reduces to a Catalan-type exponential "
            "Diophantine equation; (A2) these equations have finitely many solutions per value, uniformly bounded; "
            "(A3) the known O(log n) bound can be sharpened to O(1) via linear forms in logarithms. "
            "Reasoning path: (S1) fix a value v and consider all representations v = C(n,k); (S2) show distinct "
            "representations force exponential Diophantine relations between the parameters; (S3) apply Baker's theory "
            "of linear forms in logarithms to bound the number of representations; (S4) make the bound uniform in v. "
            "Proposed mechanism: a Diophantine rigidity proof - turn repetitions into exponential equations and bound "
            "them. "
            "What would confirm it: a proved uniform bound on multiplicities. "
            "What would kill it: values of unbounded multiplicity exhibited. "
            "What it does NOT claim: boundedness. The value 3003 appears 8 times and the ceiling is unknown; the "
            "O(log n) bound grows, however slowly, and this is a proposed path, honestly labeled."),
        "key_points": [
            "Singmaster: multiplicities of integers > 1 in Pascal's triangle are bounded.",
            "Conjectured by David Singmaster in 1971.",
            "Champion: 3003 appears 8 times.",
            "Abbott-Erdos-Hanson: multiplicity is O(log n).",
            "This walkthrough: highest multiplicity below row 500, excluding 1, is 6 at 3003.",
        ],
        "requirements": [
            "Values of unbounded multiplicity would refute the conjecture.",
            "A proof must improve O(log n) to O(1) uniformly.",
            "Linear forms in logarithms are the expected tool.",
            "Refereed publication and independent verification are required before any claim counts.",
        ],
        "standards": [
            "Standard: a claimed proof must survive refereed publication and independent verification.",
            "Multiplicity counts must exclude the trivial infinite multiplicity of 1.",
        ],
        "citations": [CIT_GUY, CIT_HARDY_WRIGHT],
    },
    {
        "key": "hadamard",
        "name": "Hadamard Matrix Conjecture",
        "group": "Compounded",
        "ladder_rank": 23,
        "ladder_tier": "compounded",
        "problem": ("A Hadamard matrix is a square matrix with entries +1 and -1 whose rows are mutually orthogonal. "
                    "They can only exist in orders 1, 2, or multiples of 4. Does one exist for every multiple of 4?"),
        "background": ("Jacques Hadamard studied these matrices in 1893 in connection with maximal determinants. The "
                       "necessary condition on the order is elementary, but sufficiency is open: the smallest unknown "
                       "order is 668. Constructions exist for many infinite families: Sylvester's doubling "
                       "construction gives orders that are powers of 2, Paley's construction gives orders q + 1 for "
                       "prime powers q congruent to 3 mod 4, and Williamson's method covers many more. This "
                       "walkthrough builds Sylvester Hadamard matrices of orders 1 through 32 and verifies "
                       "H H^T = nI exactly. Hadamard matrices are used in error-correcting codes, signal processing, "
                       "and experimental design, so the conjecture matters beyond pure mathematics."),
        "why_it_matters": ("Hadamard matrices are fundamental objects in combinatorics with real applications in codes "
                           "and signal processing. The conjecture is the simplest unsolved existence problem for "
                           "orthogonal designs. A general construction would complete a century-old classification; a "
                           "counterexample would reveal a hidden obstruction."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads Hadamard matrices as orthogonality made concrete: rows of signs at "
                     "right angles to each other, and the Signature approach is to extend the Williamson and cocyclic "
                     "constructions until every multiple of 4 is covered."),
        "sig_solution": (
            LABEL + " Approach S-23: Williamson-type construction ascent. "
            "Assumptions: (A1) every multiple of 4 admits either a Williamson quadruple or a cocyclic construction; "
            "(A2) the known constructions can be combined via product theorems to cover the remaining orders; "
            "(A3) the smallest open order, 668, yields to an explicit computer-aided construction. "
            "Reasoning path: (S1) extend the cocyclic Hadamard framework to new group orders; (S2) prove product "
            "theorems that multiply covered orders; (S3) construct the missing small orders like 668 explicitly; "
            "(S4) combine to cover all multiples of 4. "
            "Proposed mechanism: a constructive covering proof - build the matrices, don't just prove they exist. "
            "What would confirm it: a Hadamard matrix exhibited for every order divisible by 4. "
            "What would kill it: one multiple of 4 proved to admit no Hadamard matrix. "
            "What it does NOT claim: the conjecture. Order 668 alone is still open, and this is a proposed path, "
            "honestly labeled."),
        "key_points": [
            "Hadamard matrix: +-1 entries, orthogonal rows; orders restricted to 1, 2, multiples of 4.",
            "Conjecture: every multiple of 4 occurs; smallest open order is 668.",
            "Sylvester construction gives powers of 2; Paley gives q + 1 for prime powers.",
            "This walkthrough verifies Sylvester matrices to order 32 exactly.",
            "Applications: error-correcting codes, signal processing, experimental design.",
        ],
        "requirements": [
            "One multiple of 4 with no Hadamard matrix would refute the conjecture.",
            "A proof needs constructions covering all multiples of 4, including 668.",
            "Product theorems must combine the infinite families correctly.",
            "Refereed publication and independent verification are required before any claim counts.",
        ],
        "standards": [
            "Standard: a claimed proof must survive refereed publication and independent verification.",
            "Orthogonality H H^T = nI must be verified exactly, not numerically.",
        ],
        "citations": [CIT_GUY],
    },
    {
        "key": "lonely_runner",
        "name": "Lonely Runner Conjecture",
        "group": "Compounded",
        "ladder_rank": 24,
        "ladder_tier": "compounded",
        "problem": ("Runners with distinct speeds run laps on a circular track of length 1. A runner is lonely at a "
                    "moment when every other runner is at distance at least 1/(n+1) away. The conjecture says every "
                    "runner gets lonely at some time, for any number of runners and any distinct speeds."),
        "background": ("Jorg Wills posed the problem in 1967, and it has been open ever since. It is equivalent to a "
                       "view-obstruction problem: rays from the origin in the positive orthant are blocked by a grid "
                       "of cubes. The conjecture is proved for up to 7 runners, but the general case resists. It "
                       "connects to Diophantine approximation, the geometry of numbers, and graph coloring through "
                       "distance graphs. This walkthrough uses grid search to find lonely times for 3, 4, and 5 "
                       "runners with speeds 1 through n, achieving loneliness 0.33332, 0.25000, and 0.20000 against "
                       "targets 1/3, 1/4, and 1/5. The problem is famous for being easy to state and hard to prove."),
        "why_it_matters": ("The lonely runner connects dynamics, number theory, and combinatorics in one picture, so "
                           "a proof would unify tools from all three. The view-obstruction equivalence shows it is "
                           "really about how space can be blocked. It is also a wonderful example of a problem where "
                           "small cases are easy and the general case is hard."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads the lonely runner as a covering problem on the torus: time is a "
                     "circle, loneliness is a region, and the Signature approach is to show the lonely regions for "
                     "all runners always cover the circle."),
        "sig_solution": (
            LABEL + " Approach S-24: view-obstruction ascent. "
            "Assumptions: (A1) the lonely runner conjecture is equivalent to the view-obstruction problem for the "
            "corresponding dimension; (A2) the Beck-Spencer probabilistic method can be sharpened to give the exact "
            "1/(n+1) constant; (A3) the extremal speed sets can be classified and checked. "
            "Reasoning path: (S1) translate loneliness into a covering statement on the n-dimensional torus; "
            "(S2) apply the probabilistic method to show the lonely set is nonempty; (S3) sharpen the constant to "
            "1/(n+1) via the geometry of numbers; (S4) verify the extremal configurations. "
            "Proposed mechanism: a covering proof - show the lonely times cover the whole time circle. "
            "What would confirm it: every set of n+1 speeds proved to admit a lonely time. "
            "What would kill it: one speed set proved to admit no lonely time. "
            "What it does NOT claim: the conjecture. Verified here for small fields and proved up to 7 runners, but "
            "open in general, and this is a proposed path, honestly labeled."),
        "key_points": [
            "Lonely runner: n+1 runners with distinct speeds; each is lonely (1/(n+1) away from all others) sometime.",
            "Posed by Jorg Wills in 1967; proved for up to 7 runners.",
            "Equivalent to a view-obstruction problem in geometry.",
            "This walkthrough finds lonely times for 3, 4, 5 runners by grid search.",
            "Connects dynamics, Diophantine approximation, and graph coloring.",
        ],
        "requirements": [
            "One speed set with no lonely time would refute the conjecture.",
            "A proof must work for all n and all distinct speed sets.",
            "The constant 1/(n+1) must be shown sharp and attainable.",
            "Refereed publication and independent verification are required before any claim counts.",
        ],
        "standards": [
            "Standard: a claimed proof must survive refereed publication and independent verification.",
            "Loneliness must be measured as distance on the circular track, not the line.",
        ],
        "citations": [CIT_GUY],
    },
    {
        "key": "inscribed_square",
        "name": "Inscribed Square Problem",
        "group": "Compounded",
        "ladder_rank": 25,
        "ladder_tier": "compounded",
        "problem": ("Every simple closed curve in the plane, a Jordan curve, should contain four points that form the "
                    "vertices of a square. This is the Toeplitz square peg problem, open since 1911."),
        "background": ("Otto Toeplitz asked in 1911 whether every Jordan curve inscribes a square. The answer is yes "
                       "for smooth curves: Greene and Lobb proved in 2021 that every smooth Jordan curve inscribes a "
                       "square, using symplectic geometry. Stromquist proved it in 1989 for locally monotone curves. "
                       "But for arbitrary continuous Jordan curves, which can be fractal and wild, the problem is "
                       "still open. The related rectangle peg problem asks about rectangles of every aspect ratio. "
                       "This walkthrough verifies inscribed squares on the unit circle at six rotations and on the "
                       "ellipse with axes 2 and 1 at 45 degrees. The gap between smooth and merely continuous is where "
                       "the problem lives."),
        "why_it_matters": ("The square peg problem is the most famous unsolved problem about plane curves, and it "
                           "tests the boundary between smooth and wild geometry. The Greene-Lobb proof brought "
                           "symplectic topology into a century-old problem, showing how new fields can crack old "
                           "nuts. Closing the continuous case would complete the story."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads the inscribed square as a forced pattern: four points of the curve "
                     "must lock into a square, and the Signature approach is to define a test map on inscribed "
                     "quadrilaterals and prove its topological degree is nonzero, forcing a square-shaped zero."),
        "sig_solution": (
            LABEL + " Approach S-25: topological degree ascent. "
            "Assumptions: (A1) the space of inscribed quadrilaterals in a Jordan curve carries a natural test map "
            "measuring squareness; (A2) the degree of this map is nonzero for every Jordan curve, including wild "
            "ones; (A3) a limiting argument extends the smooth case to the continuous case. "
            "Reasoning path: (S1) parametrize quadruples of points on the curve in cyclic order; (S2) define the test "
            "map whose zeros are exactly the inscribed squares; (S3) compute the degree on a model curve and show it "
            "is invariant under the deformations; (S4) conclude a zero exists for every Jordan curve. "
            "Proposed mechanism: a degree-theoretic existence proof - topology forces the square. "
            "What would confirm it: every Jordan curve proved to inscribe a square. "
            "What would kill it: one Jordan curve proved to inscribe no square. "
            "What it does NOT claim: the full conjecture. Smooth curves are settled by Greene and Lobb, rough curves "
            "are not, and this is a proposed path, honestly labeled."),
        "key_points": [
            "Inscribed square: every Jordan curve contains four points forming a square.",
            "Asked by Toeplitz in 1911; open for arbitrary continuous curves.",
            "Greene-Lobb (2021): proved for smooth Jordan curves via symplectic geometry.",
            "Stromquist (1989): proved for locally monotone curves.",
            "This walkthrough verifies inscribed squares on a circle and an ellipse.",
        ],
        "requirements": [
            "One Jordan curve with no inscribed square would refute the conjecture.",
            "A proof must handle wild continuous curves, not just smooth ones.",
            "The degree argument must be invariant under all deformations.",
            "Refereed publication and independent verification are required before any claim counts.",
        ],
        "standards": [
            "Standard: a claimed proof must survive refereed publication and independent verification.",
            "The curve must be a genuine Jordan curve: simple and closed.",
        ],
        "citations": [CIT_GUY, CIT_GREENE_LOBB],
    },
    {
        "key": "chromatic_plane",
        "name": "Chromatic Number of the Plane",
        "group": "Compounded",
        "ladder_rank": 26,
        "ladder_tier": "compounded",
        "problem": ("How many colors are needed to color the plane so that no two points at distance exactly 1 share "
                    "a color? The answer is known to be 5, 6, or 7, and nobody knows which."),
        "background": ("Hadwiger and Nelson posed the problem in the 1950s. The Moser spindle, a 7-vertex unit-distance "
                       "graph, showed at least 4 colors are needed, and a hexagonal tiling shows 7 always suffice. For "
                       "decades the answer sat between 4 and 7. Then in 2018 Aubrey de Grey constructed a 1581-vertex "
                       "unit-distance graph needing 5 colors, moving the lower bound up. So the chromatic number of "
                       "the plane is 5, 6, or 7. This walkthrough builds the Moser spindle, proves by exhaustive search "
                       "that it has no 3-coloring, and exhibits a 4-coloring. Closing the remaining gap is one of the "
                       "most attractive open problems in combinatorics."),
        "why_it_matters": ("The problem asks a question a child can understand whose answer defeats modern "
                           "combinatorics, and it connects graph theory with the geometry of the plane. De Grey's "
                           "breakthrough showed computers can move such problems. Pinning the number to exactly 5, 6, "
                           "or 7 would be a famous result."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads the chromatic number as a forcing game: unit-distance graphs force "
                     "more colors, tilings cap them, and the Signature approach is to chain Moser spindles into ever "
                     "larger graphs until the exact number is squeezed from both sides."),
        "sig_solution": (
            LABEL + " Approach S-26: unit-distance graph ascent. "
            "Assumptions: (A1) the de Grey 5-chromatic construction extends by spindle-chaining to force 6 colors; "
            "(A2) a refined tiling or algebraic argument caps the number at 6, or a construction reaches 7; "
            "(A3) computer search can be guided to the extremal graphs. "
            "Reasoning path: (S1) systematize the Moser spindle chaining that raised the bound from 4 to 5; "
            "(S2) search for 6-chromatic unit-distance graphs with guided computation; (S3) improve the upper bound "
            "with better tilings or new coloring arguments; (S4) close the gap to a single number. "
            "Proposed mechanism: a squeezing proof - push the lower bound up and the upper bound down until they meet. "
            "What would confirm it: the chromatic number pinned to exactly 5, 6, or 7 by construction and proof. "
            "What would kill the approach: the gap resisting both better graphs and better tilings indefinitely. "
            "What it does NOT claim: the exact number. It is 5, 6, or 7, nobody knows which, and this is a proposed "
            "path, honestly labeled."),
        "key_points": [
            "Chromatic number of the plane: colors needed so distance-1 points differ; answer in {5, 6, 7}.",
            "Moser spindle proves 4 are needed; hexagonal tiling proves 7 suffice.",
            "De Grey (2018): 1581-vertex graph needs 5 colors.",
            "This walkthrough: Moser spindle has no 3-coloring; 4-coloring exhibited.",
            "Posed by Hadwiger and Nelson in the 1950s.",
        ],
        "requirements": [
            "A unit-distance graph needing 8 colors would break the hexagon tiling bound; none exists.",
            "Pinning the number needs both better graphs and better tilings.",
            "Computer constructions must be independently verifiable.",
            "Refereed publication and independent verification are required before any claim counts.",
        ],
        "standards": [
            "Standard: a claimed proof must survive refereed publication and independent verification.",
            "Unit-distance graphs must have all edges exactly length 1.",
        ],
        "citations": [CIT_GUY, CIT_DEGREY],
    },
    {
        "key": "pi_normal",
        "name": "Normality of Pi",
        "group": "Compounded",
        "ladder_rank": 27,
        "ladder_tier": "compounded",
        "problem": ("Is pi a normal number? That is, in its decimal expansion, does every finite block of digits "
                    "appear with the expected frequency, so each digit appears one tenth of the time?"),
        "background": ("Emile Borel defined normal numbers in 1909 and proved almost all numbers are normal, yet not "
                       "a single naturally occurring constant, including pi, e, or sqrt(2), has been proved normal in "
                       "any base. Trillions of digits of pi have been computed, and statistically they look perfectly "
                       "uniform: this walkthrough computes 1200 digits via the Chudnovsky formula and finds the first "
                       "1000 digits pass a chi-square uniformity test with value 4.74. The Bailey-Borwein-Plouffe "
                       "formula can extract individual hexadecimal digits of pi without computing the earlier ones, but "
                       "even that has not led to a normality proof. It is a humbling gap between computation and proof."),
        "why_it_matters": ("Normality is the precise form of the belief that pi's digits are random, and proving it "
                           "for even one natural constant would be a historic breakthrough in Diophantine "
                           "approximation. The techniques would apply to e, sqrt(2), and zeta values. It would turn "
                           "a statistical observation into a theorem."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads pi's digits as a pseudorandom stream begging for a generator: the BBP "
                     "formula extracts digits like a machine, and the Signature approach is to prove that machine "
                     "behaves like a normal number generator."),
        "sig_solution": (
            LABEL + " Approach S-27: finite-state normality ascent. "
            "Assumptions: (A1) the BBP digit-extraction formula for pi exposes enough pseudorandom structure; "
            "(A2) the relevant exponential sums exhibit cancellation, giving equidistribution; (A3) the argument "
            "extends from hexadecimal to decimal digits. "
            "Reasoning path: (S1) write the BBP formula as a digit-generating dynamical process; (S2) prove the "
            "process is ergodic with respect to the uniform measure via exponential-sum bounds; (S3) deduce that "
            "every block appears with the right frequency; (S4) transfer from base 16 to base 10. "
            "Proposed mechanism: a dynamical proof - show pi's digit machine is provably equidistributed. "
            "What would confirm it: pi proved normal in some base. "
            "What would kill it: some digit proved to occur with the wrong frequency, which the data contradict. "
            "What it does NOT claim: normality. A thousand digits passing chi-square proves nothing about infinity, "
            "and this is a proposed path, honestly labeled."),
        "key_points": [
            "Normal number: every digit block appears with its expected frequency.",
            "Borel (1909): almost all numbers are normal; none natural is proved normal.",
            "Trillions of pi digits computed; all statistical tests pass.",
            "This walkthrough: first 1000 digits pass chi-square with value 4.74.",
            "BBP formula extracts hex digits of pi without earlier ones.",
        ],
        "requirements": [
            "A digit proved to have wrong frequency would refute normality; data show uniformity.",
            "A proof must handle infinitely many digits, not just computed ones.",
            "Exponential-sum cancellation is the expected technical core.",
            "Refereed publication and independent verification are required before any claim counts.",
        ],
        "standards": [
            "Standard: a claimed proof must survive refereed publication and independent verification.",
            "Normality must be proved in a specified base; base 10 is the classic question.",
        ],
        "citations": [CIT_GUY, CIT_HARDY_WRIGHT],
    },
]

ENTRIES += [
    {
        "key": "abc",
        "name": "abc Conjecture",
        "group": "Advanced",
        "ladder_rank": 28,
        "ladder_tier": "advanced",
        "problem": ("For coprime positive integers with a + b = c, the size of c is controlled by the radical, the "
                    "product of the distinct prime factors of a*b*c. The conjecture says that for any epsilon > 0, "
                    "only finitely many triples have c larger than radical(a*b*c)^(1 + epsilon)."),
        "background": ("Masser and Oesterle proposed the conjecture in 1985, and it has become the central conjecture "
                       "of Diophantine geometry. It implies Fermat's Last Theorem, the Mordell conjecture, and "
                       "finiteness results for many exponential Diophantine equations. The quality of a triple, "
                       "log(c)/log(radical(abc)), measures how extreme it is; the record is held by Reyssat's triple "
                       "2 + 3^10 * 109 = 23^5 with quality about 1.6299. This walkthrough searches all triples with "
                       "c up to 1500 and finds maximal quality 1.4266 at (3, 125, 128), well below the record. In "
                       "2012 Shinichi Mochizuki claimed a proof via inter-universal Teichmuller theory; Scholze and "
                       "Stix identified a gap in 2018, and the mathematical community does not accept the proof. The "
                       "conjecture remains open."),
        "why_it_matters": ("The abc conjecture is the master key of Diophantine equations: dozens of hard problems "
                           "would fall as corollaries. A proof would be the deepest result in number theory of the "
                           "century. The controversy around the claimed proof also makes it a case study in how "
                           "mathematics verifies itself."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads abc as the ultimate size control: the radical of a sum cannot be too "
                     "small compared to the sum, and the Signature approach is to translate the conjecture into "
                     "Szpiro's conjecture about elliptic discriminants and prove it there."),
        "sig_solution": (
            LABEL + " Approach S-28: Szpiro-discriminant ascent. "
            "Assumptions: (A1) the abc conjecture is equivalent to Szpiro's conjecture relating the discriminant and "
            "conductor of elliptic curves; (A2) the Frey-Hellegouarch curve attached to an abc triple has its "
            "discriminant controlled by the radical; (A3) a height bound on the relevant moduli space yields the "
            "conjecture. "
            "Reasoning path: (S1) attach to a + b = c the Frey curve y^2 = x(x - a)(x + b); (S2) compute its minimal "
            "discriminant and conductor in terms of the radical; (S3) prove Szpiro's inequality discriminant <= "
            "conductor^(6 + epsilon); (S4) translate back to the abc inequality. "
            "Proposed mechanism: a moduli-space proof - turn abc into a statement about families of elliptic curves. "
            "What would confirm it: a refereed, accepted proof of abc or equivalently of Szpiro. "
            "What would kill it: triples of arbitrarily high quality exhibited, which the data do not show. "
            "What it does NOT claim: a proof. The claimed IUTT proof is not accepted by the community, the record "
            "quality stands at 1.6299, and this is a proposed path, honestly labeled."),
        "key_points": [
            "abc: c < radical(abc)^(1+epsilon) for all but finitely many coprime triples a + b = c.",
            "Proposed by Masser and Oesterle in 1985; implies Fermat's Last Theorem and the Mordell conjecture.",
            "Record quality 1.6299 (Reyssat triple); this walkthrough finds max 1.4266 below c = 1500.",
            "Mochizuki claimed a proof (2012); Scholze-Stix found a gap (2018); not accepted.",
            "Equivalent to Szpiro's conjecture on elliptic curve discriminants.",
        ],
        "requirements": [
            "Triples of arbitrarily high quality would refute the conjecture; none are known.",
            "A proof must be refereed and accepted; the IUTT claim does not meet this bar.",
            "Any proof must handle all epsilon > 0 simultaneously.",
            "An accepted proof would also settle Szpiro's conjecture.",
        ],
        "standards": [
            "Standard: a claimed proof must survive refereed publication and community acceptance.",
            "Quality log(c)/log(radical(abc)) is the standard measure of extreme triples.",
        ],
        "citations": [CIT_GUY, CIT_CLAY, CIT_MAZUR_STEIN],
    },
    {
        "key": "riemann",
        "name": "Riemann Hypothesis",
        "group": "Advanced",
        "ladder_rank": 29,
        "ladder_tier": "advanced",
        "problem": ("All nontrivial zeros of the Riemann zeta function have real part exactly 1/2. The zeta function "
                    "encodes the primes, so this is really a statement about the ultimate regularity of the primes."),
        "background": ("Bernhard Riemann stated the hypothesis in 1859 in his paper on the number of primes less than "
                       "a given magnitude. It is the most famous unsolved problem in mathematics and the first of the "
                       "Clay Millennium Prize Problems, worth one million dollars. The first 10^13 zeros have been "
                       "verified on the critical line, and Platt and Trudgian verified zeros up to height 3 x 10^12 in "
                       "2021. Schoenfeld proved in 1976 that the hypothesis implies the sharp bound "
                       "|pi(x) - li(x)| < sqrt(x) ln x / (8 pi) for x >= 2657. This walkthrough checks that corollary "
                       "at 2657, 10000, 100000, and 1000000, with ratios 0.965, 0.468, 0.261, and 0.236 against the "
                       "bound. Hundreds of theorems begin with the words assume the Riemann Hypothesis."),
        "why_it_matters": ("The Riemann Hypothesis is the keystone of prime number theory: it would give the best "
                           "possible error term in the prime number theorem and settle countless conditional results. "
                           "It connects analysis, number theory, and even quantum physics through random matrix "
                           "theory. Its proof would be the mathematical event of the century."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads the Riemann Hypothesis as the primes keeping perfect time: the zeros "
                     "line up on the critical line like a metronome, and the Signature approach is to extend the "
                     "verified zero-free region and the Turing zero count until no room remains for an off-line zero."),
        "sig_solution": (
            LABEL + " Approach S-29: zero-free region ascent. "
            "Assumptions: (A1) explicit zero-free regions for zeta can be widened systematically; (A2) Turing's method "
            "for counting zeros can be made to cover all heights with rigorous error bounds; (A3) the De Bruijn-Newman "
            "constant framework can be pushed to its limit. "
            "Reasoning path: (S1) verify computationally that all zeros up to some height T lie on the critical line; "
            "(S2) prove a zero-free region that, combined with the verification, leaves no gap for off-line zeros "
            "below T; (S3) raise T and widen the region iteratively; (S4) close the argument with a theoretical bound "
            "that needs no finite check. "
            "Proposed mechanism: a squeezing proof - computation from below, theory from above, meeting at the truth. "
            "What would confirm it: every nontrivial zero proved to lie on the critical line. "
            "What would kill it: one zero with real part different from 1/2, which would also disprove hundreds of "
            "conditional theorems. "
            "What it does NOT claim: the Riemann Hypothesis. Checking a corollary, as this walkthrough does with the "
            "Schoenfeld bound, is not proving the hypothesis, and this is a proposed path, honestly labeled."),
        "key_points": [
            "Riemann Hypothesis: all nontrivial zeta zeros have real part 1/2.",
            "Stated by Riemann in 1859; Clay Millennium Prize, US$1,000,000.",
            "First 10^13 zeros verified on the critical line; verified to height 3 x 10^12 (2021).",
            "Schoenfeld corollary: |pi(x) - li(x)| < sqrt(x) ln x/(8 pi); this walkthrough checks it to 10^6.",
            "Hundreds of theorems are conditional on the hypothesis.",
        ],
        "requirements": [
            "One off-line zero would refute the hypothesis and topple conditional theorems.",
            "A proof must handle all zeros at all heights, not just verified ranges.",
            "The De Bruijn-Newman constant approach needs to reach its limit.",
            "The Clay prize requires publication and a two-year waiting period.",
        ],
        "standards": [
            "Clay Mathematics Institute. Riemann Hypothesis official problem statement.",
            "Schoenfeld L. Sharper bounds for the Chebyshev functions. Mathematics of Computation; 1976.",
        ],
        "citations": [CIT_CLAY, CIT_MAZUR_STEIN, CIT_SCHOENFELD, CIT_HARDY_WRIGHT],
    },
    {
        "key": "p_vs_np",
        "name": "P versus NP",
        "group": "Advanced",
        "ladder_rank": 30,
        "ladder_tier": "advanced",
        "problem": ("If a problem's solution can be checked quickly, can the solution itself always be found quickly? "
                    "P is the class of problems solvable in polynomial time; NP is the class whose solutions are "
                    "verifiable in polynomial time. Is P equal to NP?"),
        "background": ("Stephen Cook formulated the problem in 1971 in his paper on the complexity of theorem-proving "
                       "procedures, and Leonid Levin independently developed the theory. It is the deepest open "
                       "problem in computer science and a Clay Millennium Prize Problem worth one million dollars. "
                       "Thousands of practical problems, from scheduling to protein folding, are NP-complete, meaning "
                       "a polynomial algorithm for one would give it for all. The nearest major lower bound is "
                       "Williams 2011, showing NEXP is not contained in P/poly, still far from separating P and NP. "
                       "Barriers called relativization, natural proofs, and algebrization explain why standard methods "
                       "fail. This walkthrough measures brute-force SAT scaling, with clause evaluations growing from "
                       "673 at n=10 to 63166 at n=16, the exponential signature, and verifies a polynomial 2-SAT "
                       "solver against brute force."),
        "why_it_matters": ("P versus NP asks whether finding is fundamentally harder than checking, which is really a "
                           "question about the nature of creativity and computation. A proof either way would reshape "
                           "computer science: P = NP would revolutionize optimization and break current cryptography, "
                           "while P != NP would confirm the hardness the digital world relies on."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads P versus NP as the question of whether search can be tamed: "
                     "NP-complete problems resist every clever algorithm, and the Signature approach is to prove that "
                     "resistance is a theorem by establishing superpolynomial circuit lower bounds."),
        "sig_solution": (
            LABEL + " Approach S-30: circuit lower-bound ascent. "
            "Assumptions: (A1) SAT requires superpolynomial-size circuits, the standard formalization of P != NP; "
            "(A2) the Williams program of non-uniform lower bounds can be extended past the known barriers; "
            "(A3) a non-naturalizing, non-relativizing argument exists that sidesteps the three great barriers. "
            "Reasoning path: (S1) formalize the goal as a superpolynomial circuit lower bound for an NP-complete "
            "problem; (S2) extend Williams-style lower bounds to stronger circuit classes; (S3) find an argument that "
            "evades relativization, natural proofs, and algebrization simultaneously; (S4) conclude P != NP. "
            "Proposed mechanism: a barrier-breaking lower bound - prove circuits cannot keep up with search. "
            "What would confirm it: a proof that P != NP, or a polynomial algorithm for an NP-complete problem "
            "proving P = NP. "
            "What would kill the approach: the barriers proved insurmountable for circuit methods, forcing a totally "
            "new idea. "
            "What it does NOT claim: a resolution. This is the deepest open problem in computer science, the "
            "walkthrough only measures the exponential signature of brute force, and this is a proposed path, "
            "honestly labeled."),
        "key_points": [
            "P versus NP: can every efficiently checkable problem be efficiently solved?",
            "Formulated by Cook (1971); Clay Millennium Prize, US$1,000,000.",
            "Thousands of NP-complete problems in scheduling, biology, and optimization.",
            "Williams (2011): NEXP not in P/poly, the nearest major lower bound.",
            "Barriers: relativization, natural proofs, algebrization.",
        ],
        "requirements": [
            "A polynomial algorithm for any NP-complete problem would prove P = NP.",
            "A superpolynomial lower bound for NP would prove P != NP.",
            "Any proof must evade the three known barriers.",
            "The Clay prize requires publication and a two-year waiting period.",
        ],
        "standards": [
            "Cook SA. The P versus NP Problem. Clay Mathematics Institute; 2000.",
            "Sipser M. Introduction to the Theory of Computation. 3rd ed. Cengage; 2012.",
        ],
        "citations": [CIT_CLAY, CIT_COOK, CIT_SIPSER, CIT_WILLIAMS],
    },
    {
        "key": "navier_stokes",
        "name": "Navier-Stokes Existence and Smoothness",
        "group": "Advanced",
        "ladder_rank": 31,
        "ladder_tier": "advanced",
        "problem": ("For the three-dimensional incompressible Navier-Stokes equations, do smooth, finite-energy "
                    "solutions exist for all time from any smooth initial data, or can they develop singularities "
                    "in finite time?"),
        "background": ("The Navier-Stokes equations describe fluid flow and are central to physics and engineering, "
                       "from weather prediction to aircraft design. In two dimensions, global smooth solutions are "
                       "known to exist. In three dimensions, Leray proved weak solutions exist globally, but whether "
                       "they stay smooth is open. Charles Fefferman wrote the official Clay Millennium formulation in "
                       "2000, offering one million dollars for either a proof of global regularity or a counterexample "
                       "with finite-time blowup. Partial regularity theory, by Caffarelli, Kohn, and Nirenberg, shows "
                       "singularities, if they exist, are rare. This walkthrough simulates the one-dimensional viscous "
                       "Burgers model, where energy decays from 3.6442 to 3.3383 and the solution stays smooth, "
                       "illustrating what is known in 1D and what is open in 3D."),
        "why_it_matters": ("Fluids are everywhere, and the equations that describe them are not known to be well "
                           "behaved: a blowup would mean the model itself breaks down. A proof of regularity would "
                           "validate a century of fluid mechanics; a blowup example would reveal new physics. Either "
                           "answer is a landmark for partial differential equations."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads Navier-Stokes as energy trying to concentrate: viscosity spreads it "
                     "out, nonlinearity piles it up, and the Signature approach is to find a scale-critical quantity "
                     "that can never blow up, ruling out singularities forever."),
        "sig_solution": (
            LABEL + " Approach S-31: critical-norm control ascent. "
            "Assumptions: (A1) a scale-critical quantity, such as a critical Besov norm, stays bounded along every "
            "finite-energy flow; (A2) the known partial regularity theory can be bootstrapped from smallness of this "
            "quantity; (A3) the nonlinearity cannot concentrate energy faster than viscosity dissipates it. "
            "Reasoning path: (S1) identify a critical norm that is invariant under the natural scaling; "
            "(S2) prove an epsilon-regularity criterion: small critical norm implies smoothness; "
            "(S3) show the critical norm cannot blow up in finite time using energy methods; "
            "(S4) conclude global smoothness, or find the blowup mechanism if the norm can concentrate. "
            "Proposed mechanism: a critical-quantity proof - find the monotone guardian that forbids singularities. "
            "What would confirm it: global smooth solutions proved for all smooth finite-energy data, or an exhibited "
            "finite-time blowup. "
            "What would kill the approach: the critical quantity shown to admit concentration, forcing a new idea. "
            "What it does NOT claim: 3D regularity. The 1D Burgers model in the walkthrough is smooth and dissipative, "
            "but 3D is the open problem, and this is a proposed path, honestly labeled."),
        "key_points": [
            "Navier-Stokes: global smooth 3D solutions from smooth data, or finite-time blowup?",
            "Clay Millennium Prize, US$1,000,000; official formulation by Fefferman (2000).",
            "2D: global regularity known; 3D: only weak solutions (Leray) and partial regularity (CKN).",
            "This walkthrough: 1D viscous Burgers has energy decay 3.6442 to 3.3383 and stays smooth.",
            "Blowup versus regularity are both still possible.",
        ],
        "requirements": [
            "An exhibited smooth-data blowup would settle the problem negatively.",
            "A regularity proof must control all possible singularity formation.",
            "The critical scaling of the equations must be respected by any proof.",
            "The Clay prize requires publication and a two-year waiting period.",
        ],
        "standards": [
            "Fefferman CL. Existence and Smoothness of the Navier-Stokes Equation. Clay Mathematics Institute; 2000.",
            "Standard: solutions must be smooth and finite-energy for all time.",
        ],
        "citations": [CIT_CLAY, CIT_FEFFERMAN],
    },
    {
        "key": "bsd",
        "name": "Birch and Swinnerton-Dyer Conjecture",
        "group": "Advanced",
        "ladder_rank": 32,
        "ladder_tier": "advanced",
        "problem": ("For an elliptic curve over the rational numbers, the rank of its group of rational points "
                    "equals the order of vanishing of its L-function at s = 1. Arithmetic and analysis agree "
                    "exactly."),
        "background": ("Bryan Birch and Peter Swinnerton-Dyer formulated the conjecture in the 1960s after machine "
                       "computations suggested the link between point counts and L-values. It is a Clay Millennium "
                       "Prize Problem worth one million dollars. Gross and Zagier proved in 1986 that if the L-function "
                       "vanishes to first order then the rank is at least 1, and Kolyvagin proved in 1988-1990 that "
                       "analytic rank 0 or 1 implies the algebraic rank matches, so the conjecture is known when the "
                       "analytic rank is at most 1. Higher ranks remain open. This walkthrough computes partial sums "
                       "of L(E,1) for y^2 = x^3 - x (rank 0), getting 0.7302, nonvanishing as expected, and for "
                       "y^2 = x^3 - 2 (rank 1), getting -0.0360, near-vanishing as expected."),
        "why_it_matters": ("BSD is the deepest open problem about rational solutions to equations, connecting the "
                           "discrete world of rational points with the continuous world of L-functions. It would "
                           "complete the theory of elliptic curves over Q. The Euler-system methods developed for it "
                           "already power much of modern number theory."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads BSD as a promise between two worlds: the rank counts rational points "
                     "while the L-function counts points modulo primes, and the Signature approach is to extend the "
                     "Heegner-point Euler systems from analytic rank 1 to all ranks."),
        "sig_solution": (
            LABEL + " Approach S-32: Heegner-point descent ascent. "
            "Assumptions: (A1) the Gross-Zagier formula and Kolyvagin's Euler system can be generalized beyond "
            "analytic rank 1; (A2) higher-rank Euler systems exist and control the Selmer group; (A3) the Tate-Shafarevich "
            "group is finite, so the Selmer bound gives the rank. "
            "Reasoning path: (S1) start from the known rank 0 and 1 cases via Kolyvagin; (S2) construct Euler systems "
            "for higher analytic rank using Heegner points on Shimura curves; (S3) bound the Selmer group by the "
            "analytic order of vanishing; (S4) deduce rank equals analytic order for every curve. "
            "Proposed mechanism: an Euler-system proof - let special points control the arithmetic. "
            "What would confirm it: rank E(Q) proved equal to the order of vanishing of L(E,s) at s=1 for every "
            "elliptic curve. "
            "What would kill it: one curve with rank different from its analytic order of vanishing. "
            "What it does NOT claim: BSD. Partial sums suggesting the pattern, as in the walkthrough, are "
            "exploration, not proof; only proof decides, and this is a proposed path, honestly labeled."),
        "key_points": [
            "BSD: rank of E(Q) equals the order of vanishing of L(E,s) at s = 1.",
            "Conjectured by Birch and Swinnerton-Dyer in the 1960s; Clay Millennium Prize, US$1,000,000.",
            "Known for analytic rank 0 and 1 (Gross-Zagier, Kolyvagin).",
            "This walkthrough: partial L(E,1) = 0.7302 for the rank-0 curve, -0.0360 for the rank-1 curve.",
            "The full conjecture includes a refined formula with regulators and Tate-Shafarevich groups.",
        ],
        "requirements": [
            "One curve with rank different from analytic vanishing order would refute the conjecture.",
            "A proof must handle all analytic ranks, not just 0 and 1.",
            "Finiteness of the Tate-Shafarevich group is needed for the rank equality.",
            "The Clay prize requires publication and a two-year waiting period.",
        ],
        "standards": [
            "Wiles A. The Birch and Swinnerton-Dyer Conjecture. Clay Mathematics Institute; 2000.",
            "Standard: the rank formula must hold for every elliptic curve over Q.",
        ],
        "citations": [CIT_CLAY, CIT_WILES_BSD, CIT_GROSS_ZAGIER, CIT_KOLYVAGIN],
    },
    {
        "key": "hodge",
        "name": "Hodge Conjecture",
        "group": "Advanced",
        "ladder_rank": 33,
        "ladder_tier": "advanced",
        "problem": ("On a complex projective manifold, every rational cohomology class of type (p,p), a Hodge class, "
                    "is a rational linear combination of classes of algebraic cycles. Topology and algebraic geometry "
                    "agree."),
        "background": ("W. V. D. Hodge stated the conjecture at the 1950 International Congress of Mathematicians. It "
                       "is a Clay Millennium Prize Problem worth one million dollars. It is known for divisors, the "
                       "case p = 1, by the Lefschetz (1,1) theorem of 1924, but already for p = 2 it is wide open in "
                       "general. Counterexamples exist for the integral version, but the rational version stands. The "
                       "conjecture would follow from the standard conjectures on algebraic cycles. This walkthrough "
                       "verifies a concrete case of Bezout's theorem, the intersection side of the story: for the "
                       "curves y^3 + x^2 y + x^3 = 0 and y^2 + xy + x^2 = 0, the resultant has degree exactly 6 = "
                       "3 x 2, counting the intersections."),
        "why_it_matters": ("Hodge is the central conjecture about the topology of algebraic varieties, bridging the "
                           "continuous and the algebraic. A proof would unify large parts of geometry; a "
                           "counterexample would reveal that topology sees more than algebra. Either way it is a "
                           "watershed for algebraic geometry."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads Hodge as the claim that topology cannot see beyond algebra: every "
                     "rational Hodge class is built from algebraic cycles, and the Signature approach is to prove the "
                     "standard conjectures on algebraic cycles, which imply Hodge, climbing one codimension at a time "
                     "from the known divisor case."),
        "sig_solution": (
            LABEL + " Approach S-33: standard-conjectures descent. "
            "Assumptions: (A1) Grothendieck's standard conjectures on algebraic cycles hold; (A2) they imply the Hodge "
            "conjecture by the standard formalism; (A3) the conjectures can be attacked one codimension at a time, "
            "starting from the known Lefschetz (1,1) case. "
            "Reasoning path: (S1) prove the Lefschetz standard conjecture relating numerical and homological "
            "equivalence; (S2) prove the Hodge standard conjecture on positivity of the intersection pairing; "
            "(S3) deduce that every rational Hodge class is algebraic via the standard yoga; (S4) verify the "
            "mechanism on concrete varieties like the ones in the walkthrough. "
            "Proposed mechanism: a conjectures-imply-conjecture proof - climb the standard conjectures to reach "
            "Hodge. "
            "What would confirm it: every rational Hodge class proved algebraic. "
            "What would kill it: one rational Hodge class proved non-algebraic. "
            "What it does NOT claim: Hodge. Bezout counting intersections, as the walkthrough verifies with the "
            "resultant of degree 6, is the algebraic side working correctly; the conjecture is the leap beyond, and "
            "this is a proposed path, honestly labeled."),
        "key_points": [
            "Hodge: every rational Hodge class is a rational combination of algebraic cycle classes.",
            "Stated by Hodge in 1950; Clay Millennium Prize, US$1,000,000.",
            "Known for divisors (Lefschetz (1,1) theorem, 1924); open in general.",
            "Would follow from Grothendieck's standard conjectures.",
            "This walkthrough verifies Bezout: resultant degree 6 = 3 x 2 for two curves.",
        ],
        "requirements": [
            "One rational Hodge class proved non-algebraic would refute the conjecture.",
            "A proof must handle all codimensions, not just divisors.",
            "The integral version is false; the rational version is the open one.",
            "The Clay prize requires publication and a two-year waiting period.",
        ],
        "standards": [
            "Deligne P. The Hodge Conjecture. Clay Mathematics Institute; 2000.",
            "Standard: the statement concerns rational Hodge classes on complex projective manifolds.",
        ],
        "citations": [CIT_CLAY, CIT_DELINE_HODGE],
    },
    {
        "key": "yang_mills",
        "name": "Yang-Mills Mass Gap",
        "group": "Advanced",
        "ladder_rank": 34,
        "ladder_tier": "advanced",
        "problem": ("Construct a quantum Yang-Mills theory on four-dimensional spacetime, for any compact simple gauge "
                    "group, and prove it has a mass gap: the lightest particle has strictly positive mass."),
        "background": ("Yang-Mills theory, introduced by Chen-Ning Yang and Robert Mills in 1954, is the foundation "
                       "of the Standard Model of particle physics: it describes the strong and weak forces. Physicists "
                       "are confident the quantum theory exists and has a mass gap, which is why the strong force is "
                       "short-ranged and why glueballs should exist. But no mathematically rigorous construction of "
                       "the four-dimensional quantum theory exists, let alone a proof of the gap. Jaffe and Witten "
                       "wrote the official Clay Millennium formulation in 2000, with a one-million-dollar prize. "
                       "Lattice gauge theory gives strong numerical evidence for the gap. This walkthrough verifies "
                       "SU(2) gauge invariance of the Wilson loop numerically, the symmetry prerequisite of any "
                       "mass-gap proof, with agreement to 12 decimal places."),
        "why_it_matters": ("The mass gap would put the Standard Model on rigorous mathematical footing and explain "
                           "why the strong force is confined. It is the deepest open problem in mathematical physics, "
                           "requiring new ideas in constructive quantum field theory. A solution would unite geometry, "
                           "analysis, and physics."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the companion "
                    "Signature Edition record for the full step-by-step walkthrough. The problem itself remains "
                    "open in established science; no proof is claimed."),
        "sig_lens": ("The Signature lens reads the mass gap as the vacuum refusing to be approached: the lightest "
                     "excitation stays a positive distance above nothing, and the Signature approach is to construct "
                     "the continuum theory as a limit of lattice theories whose spectral gaps survive the limit."),
        "sig_solution": (
            LABEL + " Approach S-34: constructive mass-gap ascent. "
            "Assumptions: (A1) lattice Yang-Mills theory has a positive spectral gap uniformly in the lattice "
            "spacing; (A2) the continuum limit exists via constructive renormalization group methods; (A3) the gap "
            "survives the limit, giving a massive quantum theory. "
            "Reasoning path: (S1) define SU(N) lattice gauge theory with the Wilson action; (S2) prove a uniform "
            "positive lower bound on the spectral gap using cluster expansions at strong coupling continued to weak "
            "coupling; (S3) construct the continuum limit satisfying the Wightman or Osterwalder-Schrader axioms; "
            "(S4) show the limiting Hamiltonian has spectrum bounded away from zero above the vacuum. "
            "Proposed mechanism: a constructive field-theory proof - build the theory and read off the gap. "
            "What would confirm it: a quantum Yang-Mills theory constructed with a proved mass gap Delta > 0. "
            "What would kill it: the gap proved to close, against all physical expectation and lattice evidence. "
            "What it does NOT claim: the Clay prize. Gauge invariance checks out, as the walkthrough verifies, but "
            "the gap is the open mountain, and this is a proposed path, honestly labeled."),
        "key_points": [
            "Yang-Mills mass gap: construct 4D quantum Yang-Mills and prove Delta > 0.",
            "Yang-Mills theory (1954) underlies the Standard Model strong and weak forces.",
            "Clay Millennium Prize, US$1,000,000; formulation by Jaffe and Witten (2000).",
            "Lattice gauge theory gives numerical evidence for the gap.",
            "This walkthrough verifies SU(2) Wilson-loop gauge invariance to 12 decimals.",
        ],
        "requirements": [
            "A construction with no gap would contradict physical expectation but settle the problem negatively.",
            "The theory must satisfy the Wightman or Osterwalder-Schrader axioms.",
            "The gap must be uniform and survive the continuum limit.",
            "The Clay prize requires publication and a two-year waiting period.",
        ],
        "standards": [
            "Jaffe A, Witten E. Quantum Yang-Mills Theory. Clay Mathematics Institute; 2000.",
            "Standard: existence of the quantum theory plus a proved positive mass gap.",
        ],
        "citations": [CIT_CLAY, CIT_JAFFE_WITTEN],
    },
]
