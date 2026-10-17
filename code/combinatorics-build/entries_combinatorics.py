#!/usr/bin/env python3
"""Entries for the Combinatorics field databases (field #17, taxonomy order).

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

So this build creates two NEW databases, 36 ladder-ordered records each:

  combinatorics             - The Combinatorics Database
                              (public-harvest: real, fact-checked
                              combinatorics)
  combinatorics-signature   - The Combinatorics Signature Database
                              (his original Signature interpretation;
                              src signature, titles suffixed
                              " (Signature Edition)", never presented
                              as authentic public record)

Subtitle disambiguation (fields #13-17 pattern): where a bare formula card
exists in scientific-formulas, discipline titles carry teaching-focused
subtitles, e.g. "Permutations: Counting Ordered Arrangements" and
"Combinations: Choosing Without Order" rather than bare "Permutation" or
"Combination" cards.
"""

SIG_TAIL = ("Signature original - his original Signature interpretation of "
            "combinatorics, clearly labeled Signature-made, never presented "
            "as authentic public record.")

C_TUCKER = ("Tucker, Alan. 'Applied Combinatorics', 6th ed. Wiley, 2012.")
C_BRUALDI = ("Brualdi, Richard A. 'Introductory Combinatorics', 5th ed. "
             "Pearson, 2010.")
C_STANLEY = ("Stanley, Richard P. 'Enumerative Combinatorics, Vol. 1', 2nd "
             "ed. Cambridge University Press, 2012.")
C_WILF = ("Wilf, Herbert S. 'generatingfunctionology', 3rd ed. "
          "A K Peters, 2006.")
C_VANLINT = ("van Lint, J. H. and Wilson, R. M. 'A Course in Combinatorics', "
             "2nd ed. Cambridge University Press, 2001.")
C_BONDY = ("Bondy, J. A. and Murty, U. S. R. 'Graph Theory'. Springer, 2008.")
C_ALON = ("Alon, Noga and Spencer, Joel H. 'The Probabilistic Method', 4th "
          "ed. Wiley, 2016.")
C_BERLEKAMP = ("Berlekamp, E. R., Conway, J. H. and Guy, R. K. 'Winning Ways "
               "for Your Mathematical Plays', 2nd ed. A K Peters, 2001.")
C_JUKNA = ("Jukna, Stasys. 'Extremal Combinatorics'. Springer, 2011.")
C_DIESTEL = ("Diestel, Reinhard. 'Graph Theory', 5th ed. Springer, 2017.")

ENTRIES = [
    {
        "key": "what_is_combinatorics",
        "name": "What Combinatorics Is",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Combinatorics is the mathematics of counting - the art of "
            "answering 'how many?' with certainty. Where algebra solves for "
            "unknowns and calculus studies change, combinatorics counts "
            "possibilities: how many ways can a password be formed, a deck "
            "be shuffled, a committee be chosen, a network be wired, a code "
            "be built. It is one of the oldest branches of mathematics and "
            "one of the newest to explode in importance, because computers "
            "turn every counting question into a real one: every algorithm "
            "searches a space of possibilities, every password has a number "
            "of combinations an attacker must try, every schedule is a "
            "choice among arrangements. The discipline divides into three "
            "great houses. Enumerative combinatorics counts things: "
            "permutations, combinations, partitions, recurrences, generating "
            "functions. Extremal combinatorics asks how large or small a "
            "collection can be while avoiding a pattern: the biggest graph "
            "with no triangle, the smallest set that forces a monochromatic "
            "solution. Algebraic combinatorics finds structure behind the "
            "counting: symmetries, polynomials, and group actions that turn "
            "hard counts into clean algebra. This ladder walks all three, "
            "starting with the simple counting rules everything else rests on."
        ),
        "how_it_works": (
            "Combinatorics works by replacing brute-force listing with "
            "clever reasoning. Counting 52! shuffles of a deck by listing "
            "them is impossible - the number has 68 digits. Instead, "
            "combinatorics builds a small set of principles that multiply "
            "up to enormous counts: if one choice has a options and an "
            "independent choice has b options, there are a times b combined "
            "choices. From this seed grow permutations (ordered "
            "arrangements), combinations (unordered selections), and the "
            "refinements - repetition, inclusion-exclusion, recurrences - "
            "that handle overlaps and structure. When direct counting is "
            "too hard, combinatorics counts indirectly: by bijection "
            "(matching the hard set one-to-one with an easy set), by "
            "double counting (two formulas for one quantity), by recurrence "
            "(reducing a big case to smaller cases), or by generating "
            "functions (encoding a whole sequence in one algebraic object). "
            "The answer is always exact, never approximate - and always "
            "checkable, because a second counting route must give the same "
            "number."
        ),
        "key_points": [
            "Combinatorics answers 'how many?' - counting arrangements, selections, partitions, and structures exactly.",
            "Three great houses: enumerative (counting things), extremal (largest/smallest avoiding patterns), algebraic (structure behind counting).",
            "The subject powers computer science: every algorithm searches a possibility space, every password has a combination count.",
            "Core strategy: replace impossible listing with principles - multiplication, bijection, double counting, recurrence, generating functions.",
            "Every count is exact and checkable: a second independent counting route must produce the same number.",
        ],
        "requirements": [
            "Basic arithmetic fluency and comfort with factorial notation (introduced here from scratch).",
            "Willingness to think in cases: most counting arguments split possibilities into disjoint groups.",
            "No prior combinatorics needed - this is the first rung of the ladder.",
        ],
        "standards": [
            "Counts stated as exact integers; approximations flagged explicitly when used.",
            "All counting arguments name the principle used (product rule, bijection, recurrence, etc.).",
        ],
        "citations": [C_TUCKER, C_BRUALDI],
        "sig_lens": (
            "Signature edition: combinatorics reframed as his counting engine - every "
            "permutation a Signature arrangement of what could be, every combination a "
            "Signature selection of what will be."
        ),
        "demo_kind": "comb_branches",
    },
    {
        "key": "addition_multiplication_principles",
        "name": "The Addition and Multiplication Principles",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "The two rules that start all of counting. The addition "
            "principle (sum rule): if a task can be done in m ways or in n "
            "ways, and the two kinds of ways never overlap, the task can be "
            "done in m + n ways. Choose a main course from 5 options or a "
            "dessert from 3: 8 choices. The multiplication principle "
            "(product rule): if a task is done in stages, with m ways to do "
            "the first stage and n ways to do the second regardless of the "
            "first, there are m times n ways total. A 3-letter code where "
            "each letter has 26 options: 26 times 26 times 26 = 17,576 "
            "codes. These sound trivial, and that is their power: almost "
            "every counting argument in this database is a careful "
            "composition of these two rules. The skill is not the rules "
            "themselves but the modeling: deciding what the stages are, "
            "checking that the choices at each stage really are independent "
            "of earlier ones, and checking that the cases in a sum really "
            "do not overlap. Most counting mistakes are modeling mistakes - "
            "counting the same arrangement twice, or missing a case - and "
            "they are caught by asking two questions: 'did I double-count?' "
            "and 'did I cover everything?'"
        ),
        "how_it_works": (
            "The multiplication principle works when choices are staged and "
            "independent: picture a decision tree where each branch of "
            "stage one sprouts the same number of stage-two branches. If "
            "stage one has 3 outcomes and each leads to 4 stage-two "
            "outcomes, the tree has 3 times 4 = 12 leaves, and every leaf "
            "is one complete sequence of choices. The addition principle "
            "works when options are disjoint alternatives: two separate "
            "piles of outcomes with nothing in common add. In practice, "
            "solving a counting problem means: (1) describe the objects "
            "being counted precisely; (2) find a sequence of independent "
            "stages that builds each object exactly once (product rule), "
            "or split the objects into non-overlapping cases (sum rule); "
            "(3) multiply or add; (4) sanity-check with a tiny case you can "
            "list by hand. When independence fails - when stage two's "
            "options depend on stage one's pick - the product rule does "
            "not apply directly, and that is where permutations, "
            "combinations, and inclusion-exclusion take over later on the "
            "ladder."
        ),
        "key_points": [
            "Sum rule: disjoint alternatives add - m ways or n ways means m + n ways.",
            "Product rule: staged independent choices multiply - m then n means m times n ways.",
            "Nearly every counting argument composes these two rules; the skill is in the modeling.",
            "Two audit questions catch most errors: 'did I double-count?' and 'did I cover everything?'",
            "Independence is the product rule's license: if stage two's options depend on stage one, the rule does not apply directly.",
        ],
        "requirements": [
            "Basic multiplication and addition of integers.",
            "Ability to describe a counting problem as stages or as disjoint cases.",
        ],
        "standards": [
            "Stages stated explicitly with option counts per stage before multiplying.",
            "Disjointness of summed cases asserted and justified.",
        ],
        "citations": [C_TUCKER, C_BRUALDI],
        "sig_lens": (
            "Signature edition: the two rules as his building laws - addition gathers "
            "his alternatives, multiplication stages his independent choices into "
            "Signature products."
        ),
        "demo_kind": "comb_add_mult",
    },
    {
        "key": "pigeonhole_principle",
        "name": "The Pigeonhole Principle",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "If you put more pigeons than pigeonholes, some hole holds two "
            "pigeons. That is the whole principle, and it is shockingly "
            "powerful. Formally: if n + 1 objects are placed into n boxes, "
            "some box contains at least two objects. Among 367 people, two "
            "share a birthday. In any group of 13 people, two were born in "
            "the same month. Reach into a drawer of 10 pairs of socks in "
            "the dark: 11 socks guarantee a matching pair. The generalized "
            "form: if kn + 1 objects go into n boxes, some box holds at "
            "least k + 1. The principle proves existence without "
            "construction - it tells you a repeat must exist without "
            "telling you where. It is the simplest example of a "
            "non-constructive existence proof, a theme that returns at the "
            "top of the ladder in the probabilistic method. Dirichlet stated "
            "it in 1834 (it is also called Dirichlet's box principle), "
            "using it to prove deep facts about approximating irrational "
            "numbers by rationals."
        ),
        "how_it_works": (
            "The principle works by contradiction against the alternative: "
            "suppose every box held at most one object - then n boxes hold "
            "at most n objects, contradicting the n + 1 objects placed. "
            "To use it: (1) identify the objects (the pigeons) and the "
            "categories (the holes); (2) count both; (3) if objects exceed "
            "holes, conclude a repeat exists. The art is choosing the "
            "holes cleverly. Proving two people in a city have the same "
            "number of hairs: objects are people (millions), holes are "
            "possible hair counts (0 to about 150,000) - since people "
            "outnumber hair-count possibilities, two share a count. The "
            "generalized form follows the same logic: if every box held at "
            "most k objects, n boxes hold at most kn. Applications run from "
            "birthday guarantees to data compression limits to the "
            "Erdos-Szekeres monotone subsequence theorem later in this "
            "ladder."
        ),
        "key_points": [
            "n + 1 objects into n boxes forces a box with at least two objects.",
            "Generalized: kn + 1 objects into n boxes forces a box with at least k + 1.",
            "Proves existence without construction - a non-constructive proof in its simplest form.",
            "The skill is choosing the boxes: clever categorization turns hard problems into pigeonholes.",
            "Also called Dirichlet's box principle; the seed of the probabilistic method at the top of the ladder.",
        ],
        "requirements": [
            "The addition and multiplication principles (counting objects and boxes).",
            "Comfort with proof by contradiction at an intuitive level.",
        ],
        "standards": [
            "Objects (pigeons) and categories (holes) named explicitly before concluding.",
            "Counts of both stated; the excess that forces the repeat shown.",
        ],
        "citations": [C_BRUALDI, C_VANLINT],
        "sig_lens": (
            "Signature edition: the pigeonhole as his guarantee law - when his objects "
            "outnumber his categories, a Signature repeat is forced into existence."
        ),
        "demo_kind": "comb_pigeonhole",
    },
    {
        "key": "permutations_ordered",
        "name": "Permutations: Counting Ordered Arrangements",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "A permutation counts arrangements where order matters. Line up "
            "5 distinct books: 5 choices for the first slot, 4 for the "
            "second, 3, 2, 1 - the product rule gives 5 times 4 times 3 "
            "times 2 times 1 = 120 arrangements. In general, the number of "
            "ways to arrange n distinct objects in order is n factorial, "
            "n! = n times (n-1) times ... times 2 times 1. Choosing an "
            "ordered selection of k out of n - first, second, third prize "
            "from 20 contestants - gives P(n,k) = n times (n-1) times ... "
            "times (n-k+1), equivalently n!/(n-k)!. Factorials grow "
            "explosively: 10! is 3,628,800; 20! is about 2.4 quintillion; "
            "52! (shuffles of a deck) has 68 digits. This explosive growth "
            "is why brute-force search over permutations fails and why "
            "cryptography trusts large key spaces: a 128-bit key has 2^128 "
            "possibilities, far beyond any feasible enumeration. "
            "Permutations are the first great counting family, and "
            "everything about unordered selection later is defined in "
            "relation to them."
        ),
        "how_it_works": (
            "Permutation counting is the product rule with shrinking "
            "options: each stage's choice removes one object from the pool. "
            "For the full arrangement of n objects: n choices for position "
            "1, then n-1 for position 2, down to 1 for the last - the "
            "product is n!. For an ordered k-selection from n, stop after k "
            "stages: P(n,k) = n!/(n-k)!. The key discipline is recognizing "
            "when order matters: electing a president, vice-president, and "
            "treasurer from 10 people is P(10,3) = 720, because swapping "
            "the president and treasurer changes the outcome; choosing any "
            "3 committee members is a different problem (combinations, "
            "next rung). A useful habit: when in doubt, count ordered "
            "arrangements first, then divide by the number of orders per "
            "unordered object - that division is exactly how the "
            "combination formula is derived, and it previews the "
            "overcounting corrections used throughout combinatorics."
        ),
        "key_points": [
            "n distinct objects arrange in n! = n(n-1)...(2)(1) orders.",
            "Ordered k-selection from n: P(n,k) = n!/(n-k)!.",
            "Order matters = permutation: president/vice-president/treasurer elections, rankings, passwords.",
            "Factorials grow explosively - 52! has 68 digits; this growth underlies key-space security.",
            "Combinations are derived from permutations by dividing out the k! orders of each selection.",
        ],
        "requirements": [
            "The product rule (multiplication principle).",
            "Factorial notation and basic fraction simplification.",
        ],
        "standards": [
            "Whether order matters is stated explicitly for every counting problem.",
            "P(n,k) written in both product and factorial forms.",
        ],
        "citations": [C_TUCKER, C_BRUALDI],
        "sig_lens": (
            "Signature edition: permutations as his orderings - every arrangement a "
            "Signature sequence, every factorial his measure of how fast order "
            "multiplies."
        ),
        "demo_kind": "comb_permutations",
    },
    {
        "key": "combinations_unordered",
        "name": "Combinations: Choosing Without Order",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "A combination counts selections where order does not matter. "
            "Choose any 3 committee members from 10: start with ordered "
            "selections, P(10,3) = 720, then notice each unordered trio was "
            "counted 3! = 6 times (once per ordering), so divide: 720/6 = "
            "120. In general, C(n,k) = n!/(k!(n-k)!) - 'n choose k' - "
            "counts the k-element subsets of an n-element set. The "
            "combination numbers are the entries of Pascal's triangle, the "
            "coefficients of the binomial theorem, the counts of binary "
            "strings with k ones, the sizes of poker hands (C(52,5) = "
            "2,598,960). They satisfy the symmetry C(n,k) = C(n,n-k): "
            "choosing which k to take is the same as choosing which n-k to "
            "leave. Combinations are arguably the single most-used numbers "
            "in applied mathematics: lottery odds, quality-control sampling, "
            "genetics (which alleles a child inherits), polling margins, "
            "and every 'choose a team / a hand / a sample' problem ever "
            "asked."
        ),
        "how_it_works": (
            "The combination formula is an overcounting correction: count "
            "ordered selections P(n,k), then divide by k!, the number of "
            "orders of each k-set, because each unordered selection was "
            "counted once per ordering. Equivalently: every k-subset "
            "corresponds to exactly k! permutations, so #subsets times k! "
            "= P(n,k). To use combinations: (1) confirm order truly does "
            "not matter - swapping two chosen items must not create a new "
            "outcome; (2) confirm each selection is a set (no repeats - "
            "repetition is a later rung); (3) compute n!/(k!(n-k)!), "
            "canceling before multiplying to keep numbers small. The "
            "symmetry C(n,k) = C(n,n-k) often simplifies: C(100,98) = "
            "C(100,2) = 4950. Pascal's recurrence C(n,k) = C(n-1,k-1) + "
            "C(n-1,k) gives a second route - building the triangle "
            "row by row - which also proves the counts are integers without "
            "any division."
        ),
        "key_points": [
            "C(n,k) = n!/(k!(n-k)!) counts k-element subsets of an n-element set - order irrelevant, no repeats.",
            "Derived by overcounting correction: P(n,k)/k! - each subset counted once per ordering.",
            "Symmetry: C(n,k) = C(n,n-k); choose the smaller k for easier arithmetic.",
            "Pascal's recurrence C(n,k) = C(n-1,k-1) + C(n-1,k) builds the triangle and proves integrality.",
            "Ubiquitous: poker hands C(52,5) = 2,598,960; lottery odds; sampling; genetics.",
        ],
        "requirements": [
            "Permutations and the product rule.",
            "Factorial arithmetic and fraction cancellation.",
        ],
        "standards": [
            "'Order does not matter' verified explicitly before applying C(n,k).",
            "C(n,k) simplified by cancellation, not by computing huge factorials directly.",
        ],
        "citations": [C_TUCKER, C_BRUALDI],
        "sig_lens": (
            "Signature edition: combinations as his pure selections - the Signature "
            "choice stripped of order, counted once and counted right."
        ),
        "demo_kind": "comb_combinations",
    },
    {
        "key": "pascal_binomial_theorem",
        "name": "Pascal's Triangle and the Binomial Theorem",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Pascal's triangle arranges the combination numbers C(n,k) in "
            "rows: each entry is the sum of the two above it. Row 4 reads "
            "1, 4, 6, 4, 1. The triangle is the binomial theorem made "
            "visible: (x + y)^n = sum of C(n,k) x^k y^(n-k) over k. Expand "
            "(x+y)^4 and the coefficients 1, 4, 6, 4, 1 appear. Why? Each "
            "term of the expansion picks x or y from each of the n "
            "factors; the terms with k x's are counted by choosing which k "
            "factors contribute x - exactly C(n,k). The triangle encodes "
            "dozens of identities: each row sums to 2^n (set x=y=1), the "
            "alternating row sums to 0 (x=1, y=-1), the shallow diagonals "
            "are the Fibonacci numbers, and the middle entries grow like "
            "2^n/sqrt(pi n/2). Blaise Pascal studied the triangle in 1654, "
            "though it appeared centuries earlier in China (Yang Hui), "
            "Persia (al-Karaji), and India - a reminder that counting is "
            "universal."
        ),
        "how_it_works": (
            "Pascal's recurrence C(n,k) = C(n-1,k-1) + C(n-1,k) has a "
            "combinatorial proof: to choose k from n items, either take "
            "item n (then choose k-1 from n-1) or skip it (choose k from "
            "n-1) - disjoint cases, sum rule. This builds the triangle "
            "without factorials. The binomial theorem follows by the "
            "'choose which factors' argument: expanding (x+y)^n means "
            "picking one term from each of n binomial factors; the "
            "coefficient of x^k y^(n-k) counts the picks with exactly k "
            "x's, which is C(n,k). In practice: (1) read coefficients off "
            "the triangle for small n; (2) for a specific term of "
            "(ax+by)^n, the x^k term has coefficient C(n,k) a^k b^(n-k); "
            "(3) row sums give subset counts (2^n) and alternating sums "
            "give 0. The theorem also runs backward: recognizing 1 + 4x + "
            "6x^2 + 4x^3 + x^4 as (1+x)^4 factors a polynomial instantly."
        ),
        "key_points": [
            "Pascal's recurrence: C(n,k) = C(n-1,k-1) + C(n-1,k) - each entry sums the two above.",
            "Binomial theorem: (x+y)^n = sum_k C(n,k) x^k y^(n-k) - coefficients count the x-picks.",
            "Row sums: 2^n (all subsets); alternating sums: 0.",
            "Shallow diagonals of the triangle are the Fibonacci numbers.",
            "Studied by Pascal (1654), Yang Hui, al-Karaji - counting is universal across cultures.",
        ],
        "requirements": [
            "Combinations C(n,k).",
            "Polynomial expansion basics (distributing products).",
        ],
        "standards": [
            "Triangle rows indexed from n=0; entries verified by the recurrence.",
            "Binomial expansions show the C(n,k) coefficient on each term explicitly.",
        ],
        "citations": [C_BRUALDI, C_TUCKER],
        "sig_lens": (
            "Signature edition: the triangle as his pyramid of choice - every row a "
            "Signature sum of the row before, every expansion his binomial law written "
            "in coefficients."
        ),
        "demo_kind": "comb_pascal_binomial",
    },
    {
        "key": "permutations_repetition_multinomial",
        "name": "Permutations with Repetition and Multinomial Coefficients",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "What if the objects are not all distinct? Arrange the letters "
            "of MISSISSIPPI: 11 letters, but I appears 4 times, S appears 4 "
            "times, P appears 2, M once. Counting 11! arrangements "
            "overcounts - swapping two identical S's changes nothing. The "
            "fix is another overcounting correction: divide by the "
            "factorial of each repeated type's count. MISSISSIPPI "
            "arrangements = 11!/(4! 4! 2! 1!) = 34,650. In general, with "
            "n1 identical of type 1, n2 of type 2, ..., nk of type k "
            "(n1+...+nk = n), the distinct arrangements number "
            "n!/(n1! n2! ... nk!) - the multinomial coefficient. It is "
            "called multinomial because these are the coefficients of "
            "(x1 + x2 + ... + xk)^n. If repetitions are unlimited and order "
            "matters - a 4-digit PIN where each digit has 10 options - the "
            "count is simply n^k (product rule with replacement): 10^4 = "
            "10,000 PINs. These two cases - identical types vs. free "
            "repetition - cover anagrams, license plates, DNA sequences, "
            "and password spaces."
        ),
        "how_it_works": (
            "For identical types, start with n! arrangements of n "
            "distinguishable items, then correct: the n1 identical items "
            "can be permuted among themselves in n1! ways without changing "
            "the visible arrangement, so each distinct arrangement was "
            "counted n1! times - divide by n1!, and likewise for each "
            "type. The multinomial coefficient n!/(n1!...nk!) results. "
            "Equivalently, build sequentially: choose positions for type 1 "
            "(C(n,n1)), then type 2 from the rest (C(n-n1,n2)), and so on - "
            "the product telescopes to the same formula, a nice double "
            "count. For unlimited repetition with order (PINs, license "
            "plates, DNA), each of the k positions independently has n "
            "options: n^k by the product rule. To choose the right tool: "
            "ask whether identical items are being rearranged (divide by "
            "type factorials) or each position is freely refilled "
            "(n^k). Mixing them up is the classic error."
        ),
        "key_points": [
            "Identical types: n!/(n1! n2! ... nk!) distinct arrangements - divide out each type's internal permutations.",
            "MISSISSIPPI: 11!/(4!4!2!1!) = 34,650.",
            "Unlimited repetition with order: n^k (PINs, DNA, license plates).",
            "Multinomial coefficients are the coefficients of (x1+...+xk)^n.",
            "Classic error: using n^k when types are identical, or dividing when positions refill freely.",
        ],
        "requirements": [
            "Permutations, combinations, and the overcounting-correction idea.",
            "Factorial division and cancellation.",
        ],
        "standards": [
            "Type counts (n1, n2, ...) listed explicitly before dividing.",
            "The repetition model (identical types vs. free refill) named explicitly.",
        ],
        "citations": [C_TUCKER, C_BRUALDI],
        "sig_lens": (
            "Signature edition: repetition as his echo law - identical marks divide out "
            "of his arrangements, free positions multiply into his Signature powers."
        ),
        "demo_kind": "comb_perm_rep",
    },
    {
        "key": "combinations_repetition_stars_bars",
        "name": "Combinations with Repetition: Stars and Bars",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Choose 3 scoops from 5 flavors, repeats allowed, order "
            "irrelevant: chocolate-chocolate-vanilla is one outcome. How "
            "many multisets of size k from n types? The stars-and-bars "
            "bijection answers: C(n+k-1, k). Picture k stars (the chosen "
            "items) and n-1 bars (dividers between the n types): "
            "**|*||***| means 2 of type 1, 1 of type 2, 0 of type 3, 3 of "
            "type 4 (for n=4, k=6). Every arrangement of k stars and n-1 "
            "bars encodes exactly one multiset, and every multiset encodes "
            "exactly one arrangement - a bijection. Counting arrangements "
            "of (n-1)+k symbols with k stars: C(n+k-1, k). Distribute 10 "
            "identical cookies among 4 children: C(10+4-1, 10) = C(13,10) "
            "= 286 ways. The same formula counts nonnegative integer "
            "solutions to x1 + x2 + ... + xn = k (set xi = count of type "
            "i), and with a shift it counts positive solutions too. "
            "Stars and bars is the workhorse behind occupancy problems, "
            "integer compositions, and the 'identical balls into distinct "
            "boxes' model that pervades probability."
        ),
        "how_it_works": (
            "The bijection is the whole trick: encode each selection as a "
            "string of stars and bars, count the strings. With n types and "
            "k picks, write k stars for the picks and n-1 bars separating "
            "type 1 from type 2, type 2 from type 3, and so on; stars "
            "before the first bar are type-1 picks, between bars 1 and 2 "
            "are type-2, and so on. Choosing positions for the k stars "
            "among n+k-1 slots: C(n+k-1, k). For integer solutions to "
            "x1+...+xn = k with xi >= 0, set xi = number of type-i picks - "
            "same count. For xi >= 1 (positive), substitute yi = xi - 1, "
            "giving y1+...+yn = k-n, counted by C(k-1, n-1). In practice: "
            "(1) check the objects are identical and the boxes distinct "
            "(children, flavors, variables); (2) check order is irrelevant; "
            "(3) apply C(n+k-1,k) for nonnegative, C(k-1,n-1) for positive. "
            "If the objects are distinct instead, this is the wrong tool - "
            "use n^k (each object chooses a box)."
        ),
        "key_points": [
            "k-multisets from n types: C(n+k-1, k) via the stars-and-bars bijection.",
            "Nonnegative integer solutions to x1+...+xn = k: same count, C(n+k-1, k).",
            "Positive solutions (xi >= 1): shift to C(k-1, n-1).",
            "Model check: identical objects into distinct boxes, order irrelevant.",
            "Distinct objects into boxes is n^k instead - know which model you have.",
        ],
        "requirements": [
            "Combinations and the bijection idea (one-to-one matching of sets).",
            "Comfort reading symbolic encodings (strings of stars and bars).",
        ],
        "standards": [
            "The stars-and-bars encoding shown explicitly for at least one example.",
            "Identical-vs-distinct and nonnegative-vs-positive decided before applying the formula.",
        ],
        "citations": [C_TUCKER, C_BRUALDI],
        "sig_lens": (
            "Signature edition: stars and bars as his distribution law - identical "
            "marks dealt among his distinct houses, every division a Signature "
            "arrangement of symbols."
        ),
        "demo_kind": "comb_stars_bars",
    },
]

ENTRIES += [
    {
        "key": "binomial_identities",
        "name": "Binomial Identities: Algebraic and Combinatorial Proofs",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The combination numbers satisfy a web of identities, and "
            "proving them two ways - algebraically and combinatorially - "
            "is the heart of enumerative reasoning. The row sum: "
            "C(n,0)+C(n,1)+...+C(n,n) = 2^n, because the left counts "
            "subsets by size and the right counts all subsets. "
            "Vandermonde's identity: C(m+n, r) = sum over k of "
            "C(m,k)C(n,r-k) - choose r from m+n by splitting the pool into "
            "m and n and summing over how many come from each side. The "
            "hockey-stick identity: C(r,r)+C(r+1,r)+...+C(n,r) = C(n+1,r+1) "
            "- the diagonal sums in Pascal's triangle. The absorption "
            "identity: k*C(n,k) = n*C(n-1,k-1) - choosing a k-committee "
            "with a chair equals choosing the chair first (n ways) then "
            "the rest. Each identity has an algebraic proof (factorial "
            "manipulation) and a combinatorial proof (a story about what "
            "is being counted). The combinatorial proof is usually more "
            "illuminating: it explains WHY the identity holds, not just "
            "that the algebra checks out. Mastering both styles is what "
            "turns a formula-user into a combinatorialist."
        ),
        "how_it_works": (
            "A combinatorial proof works by double counting: find one set "
            "of objects counted two ways, one per side of the identity. "
            "For Vandermonde: the set is r-subsets of an (m+n)-element set "
            "split into an m-group and an n-group; the left side counts "
            "them directly, the right side sums over k = number chosen "
            "from the m-group (C(m,k) ways) times number from the n-group "
            "(C(n,r-k) ways). For the row sum: subsets counted by size vs. "
            "all subsets via binary membership strings. For absorption: "
            "committees-with-chair counted as (choose committee, then "
            "chair: k*C(n,k)) vs. (choose chair, then committee: "
            "n*C(n-1,k-1)). The method: (1) write both sides; (2) invent a "
            "counting scenario for one side; (3) recount it to get the "
            "other. Algebraic proofs use factorial expansion and index "
            "shifts - reliable but unenlightening. When stuck on a sum of "
            "binomial coefficients, always ask: 'what single thing could "
            "both sides be counting?'"
        ),
        "key_points": [
            "Row sum: sum_k C(n,k) = 2^n - subsets counted by size vs. all subsets.",
            "Vandermonde: C(m+n,r) = sum_k C(m,k)C(n,r-k) - split the pool, sum over the split.",
            "Hockey-stick: diagonal sums in Pascal's triangle collapse to C(n+1,r+1).",
            "Absorption: k*C(n,k) = n*C(n-1,k-1) - committees with a distinguished chair.",
            "Combinatorial proofs explain WHY via double counting; algebraic proofs verify via factorials.",
        ],
        "requirements": [
            "Combinations and Pascal's triangle.",
            "The double-counting idea (two formulas, one set of objects).",
        ],
        "standards": [
            "Each identity proved both combinatorially (a counting story) and algebraically where feasible.",
            "The counted set named explicitly in every combinatorial proof.",
        ],
        "citations": [C_BRUALDI, C_TUCKER],
        "sig_lens": (
            "Signature edition: identities as his double vision - one Signature count "
            "seen two ways, every equality a proof that his counting holds together."
        ),
        "demo_kind": "comb_binomial_identities",
    },
    {
        "key": "inclusion_exclusion",
        "name": "The Inclusion-Exclusion Principle",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The sum rule needs disjoint cases - but real cases overlap. "
            "How many integers from 1 to 1000 are divisible by 2, 3, or 5? "
            "Add the three counts (500 + 333 + 200 = 1033), but multiples "
            "of 6 were counted twice, multiples of 30 three times - so "
            "subtract the pairwise intersections, then add back the triple "
            "intersection: 500+333+200 - 166-100-66 + 33 = 734. In general, "
            "|A union B| = |A| + |B| - |A intersect B|, and for three sets "
            "add singles, subtract pairs, add the triple. For n sets: sum "
            "over all nonempty intersections with alternating signs, "
            "+ for odd-sized intersections, - for even. Inclusion-exclusion "
            "counts unions when overlaps are messy but intersections are "
            "easy: divisibility (intersections are lcms), derangements "
            "(permutations fixing a given set), onto functions, the "
            "Euler totient function, and rook theory. It is the systematic "
            "way to un-double-count."
        ),
        "how_it_works": (
            "The principle corrects overcounting level by level: an element "
            "in exactly m of the sets is counted C(m,1) - C(m,2) + ... "
            "+/- C(m,m) = 1 time - the alternating binomial sum equals 1, "
            "so every element contributes exactly 1 to the union count. "
            "To apply it: (1) name the sets A1...An whose union you want; "
            "(2) compute sizes of all intersections - these must be easy "
            "(for divisibility by d, count = floor(N/d)); (3) alternate "
            "signs by intersection size; (4) sum. The classic applications: "
            "derangements (Ai = permutations fixing i; |intersection of k "
            "specific Ai| = (n-k)!), giving !n = n! sum (-1)^k/k!; "
            "surjections from an n-set to a k-set: sum (-1)^i C(k,i)(k-i)^n; "
            "Euler's totient phi(n) = n product (1 - 1/p) over prime "
            "divisors p. When intersections are as hard as the union, the "
            "principle gives no leverage - that is its limit."
        ),
        "key_points": [
            "Two sets: |A union B| = |A| + |B| - |A intersect B|; three sets: add singles, subtract pairs, add triple.",
            "n sets: alternating sum over all nonempty intersections (+ odd, - even).",
            "Works when intersections are easy but the union is messy (divisibility, fixed points).",
            "Yields derangements, surjection counts, and Euler's totient function.",
            "Limit: no leverage when intersections are as hard as the union itself.",
        ],
        "requirements": [
            "Set operations (union, intersection) and the sum rule.",
            "Binomial coefficients for counting intersections.",
        ],
        "standards": [
            "Every set Ai defined explicitly; every intersection size computed, not hand-waved.",
            "Sign alternation (+ odd-sized, - even-sized) checked on a small case.",
        ],
        "citations": [C_BRUALDI, C_TUCKER],
        "sig_lens": (
            "Signature edition: inclusion-exclusion as his overlap law - add his sets, "
            "subtract his double-counts, restore his triple-counts, until every "
            "Signature element is counted exactly once."
        ),
        "demo_kind": "comb_inclusion_exclusion",
    },
    {
        "key": "derangements",
        "name": "Derangements: Permutations with No Fixed Points",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "A derangement is a permutation with no element in its original "
            "position - the hat-check problem: n people check hats, hats "
            "are returned randomly, in how many ways does nobody get their "
            "own hat? The count, !n (subfactorial), satisfies the elegant "
            "recurrence !n = (n-1)(!(n-1) + !(n-2)): consider where hat 1 "
            "goes (n-1 choices, say to person k); either person k gets hat "
            "1 (reducing to a derangement of n-2) or not (a derangement-like "
            "count of n-1). Inclusion-exclusion gives the closed form "
            "!n = n! (1 - 1/1! + 1/2! - ... + (-1)^n/n!), and as n grows, "
            "!n/n! approaches 1/e - about 36.8% of random permutations are "
            "derangements. The first values: !1 = 0, !2 = 1, !3 = 2, !4 = "
            "9, !5 = 44, !6 = 265. Derangements are the showcase example "
            "for inclusion-exclusion and the prototype of 'permutations "
            "with forbidden positions', which generalizes to rook theory "
            "and the menage problem (seating couples around a table)."
        ),
        "how_it_works": (
            "Three routes to !n, each teaching a method. Recurrence: fix "
            "the image of element 1 (n-1 choices); case analysis on whether "
            "it swaps back gives !n = (n-1)(!(n-1)+!(n-2)), computable "
            "bottom-up from !1=0, !2=1. Inclusion-exclusion: let Ai be "
            "permutations fixing i; |Ai intersect ... intersect Aj| (k of "
            "them) = (n-k)!; alternating sum gives n! sum_{k=0}^n (-1)^k/k!. "
            "Nearest integer: !n is the nearest integer to n!/e for n >= 1 "
            "- a startlingly clean fact proved by bounding the alternating "
            "tail. In practice: (1) recognize 'no fixed points' or 'no "
            "object in its home'; (2) use the recurrence for exact small "
            "values; (3) use n!/e for large-n estimates. The hat-check "
            "story, the secret-Santa with no self-gifts, and 'everyone "
            "gets someone else's coat' are all derangements."
        ),
        "key_points": [
            "!n counts permutations of n with no fixed points: 0, 1, 2, 9, 44, 265 for n=1..6.",
            "Recurrence: !n = (n-1)(!(n-1) + !(n-2)) - case analysis on where element 1 goes.",
            "Closed form: !n = n! sum_{k=0}^n (-1)^k/k! via inclusion-exclusion.",
            "!n is the nearest integer to n!/e; the derangement probability tends to 1/e ~ 36.8%.",
            "Prototype of permutations with forbidden positions (rook theory, menage problem).",
        ],
        "requirements": [
            "Permutations and inclusion-exclusion.",
            "Recurrence thinking (reducing to smaller cases).",
        ],
        "standards": [
            "The recurrence's case analysis stated fully (swap-back vs. not).",
            "The 1/e limit derived from the alternating series, not asserted.",
        ],
        "citations": [C_BRUALDI, C_TUCKER],
        "sig_lens": (
            "Signature edition: derangements as his no-home permutations - every "
            "Signature element displaced, counted by his recurrence, tending to his "
            "1/e law."
        ),
        "demo_kind": "comb_derangements",
    },
    {
        "key": "bijection_principle",
        "name": "The Bijection Principle and Combinatorial Proofs",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The bijection principle: if two finite sets can be matched "
            "one-to-one, they have the same size. It sounds obvious; it is "
            "the most creative tool in combinatorics. Counting subsets of "
            "an n-element set is hard directly - but match each subset to "
            "its binary membership string (in/out for each element), and "
            "there are obviously 2^n strings. Counting lattice paths from "
            "(0,0) to (a,b) with steps right and up is hard - but match "
            "each path to the sequence of its a+b steps with a rights, "
            "counted by C(a+b, a). A combinatorial proof is an argument "
            "that establishes an identity by exhibiting a bijection (or a "
            "double count) rather than by algebra. The classic: C(n,k) = "
            "C(n,n-k) by complementing subsets - the map S -> complement "
            "is its own inverse. Bijection proofs demand invention - you "
            "must SEE the matching - but they explain why identities hold "
            "in a way algebra never can, and they often reveal that two "
            "seemingly different structures are secretly the same."
        ),
        "how_it_works": (
            "To prove |A| = |B| by bijection: (1) construct an explicit "
            "rule f mapping each a in A to an f(a) in B; (2) construct the "
            "inverse rule (or prove f is one-to-one and onto); (3) "
            "conclude equal counts. The famous examples: subsets <-> "
            "binary strings (characteristic vectors); k-subsets <-> "
            "(n-k)-subsets via complement; lattice paths <-> step "
            "sequences; binary trees with n nodes <-> Dyck paths of length "
            "2n (the Catalan bijection, previewed here and proved at the "
            "Catalan rung); integer partitions into odd parts <-> "
            "partitions into distinct parts (Euler, via binary expansion). "
            "A bijection must be reversible - a map that is merely onto "
            "proves only |A| >= |B| (that weaker form is still useful: "
            "surjections give inequalities). When hunting a bijection, "
            "look for a natural encoding: every combinatorial object has "
            "a canonical description, and the encoding IS the bijection."
        ),
        "key_points": [
            "Bijection principle: a one-to-one matching proves two finite sets have equal size.",
            "Subsets <-> binary strings gives 2^n; k-sets <-> (n-k)-sets gives C(n,k) = C(n,n-k).",
            "Combinatorial proofs explain WHY identities hold; algebra only verifies.",
            "A bijection must be reversible; a mere surjection proves only an inequality.",
            "Strategy: find the natural encoding of each object - the encoding is the bijection.",
        ],
        "requirements": [
            "Set concepts (one-to-one, onto) at an intuitive level.",
            "Combinations and the subset examples from the foundations.",
        ],
        "standards": [
            "Both the forward rule and its inverse stated explicitly in every bijection proof.",
            "The matched sets defined precisely before the matching is claimed.",
        ],
        "citations": [C_STANLEY, C_BRUALDI],
        "sig_lens": (
            "Signature edition: bijection as his mirror law - two Signature families "
            "matched one-to-one are the same Signature size, and the matching reveals "
            "their hidden sameness."
        ),
        "demo_kind": "comb_bijection",
    },
    {
        "key": "double_counting",
        "name": "Double Counting: One Answer, Two Ways",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Double counting proves an identity by counting one set of "
            "objects in two different ways. The handshaking lemma: in any "
            "graph, the sum of all vertex degrees equals twice the number "
            "of edges - count 'vertex-edge incidences' by vertices (sum of "
            "degrees) and by edges (each edge touches 2 vertices). The "
            "committee-chair identity: k*C(n,k) = n*C(n-1,k-1) - count "
            "committees with a chair by choosing the committee then the "
            "chair, or the chair then the committee. The sum of the first "
            "n odd numbers is n^2: count unit squares in an n-by-n grid by "
            "L-shaped layers. Double counting is how combinatorialists "
            "prove things: where an algebraist manipulates symbols, a "
            "combinatorialist finds the set. It is also a debugging tool - "
            "if two routes to one count disagree, at least one route has "
            "a modeling error, and the disagreement locates it. Every "
            "identity in the binomial-identities rung is a double count "
            "in disguise."
        ),
        "how_it_works": (
            "The method has three steps: (1) identify a finite set S of "
            "'incidences' or 'configurations' relevant to both sides; "
            "(2) count S by grouping one way to get the left side; (3) "
            "count S by grouping another way to get the right side. For "
            "the handshaking lemma, S = {(v,e): vertex v touches edge e}; "
            "by vertices: sum of degrees; by edges: 2|E|. For "
            "committee-chair, S = {(C, c): c chairs committee C}; by "
            "committee: C(n,k) committees times k chair choices; by chair: "
            "n chair choices times C(n-1,k-1) committees. For sum of "
            "degrees arguments, always check: is every incidence counted "
            "exactly once per grouping? The technique extends to "
            "inequalities (count with multiplicity to get bounds) and to "
            "the probabilistic method at the top of the ladder, where "
            "expectation is double counting in disguise."
        ),
        "key_points": [
            "Double counting: one set of incidences, counted two ways, yields an identity.",
            "Handshaking lemma: sum of degrees = 2|E| - incidences grouped by vertex vs. by edge.",
            "Committee-chair: k*C(n,k) = n*C(n-1,k-1) - grouped by committee vs. by chair.",
            "Debugging tool: disagreeing routes locate modeling errors.",
            "Extends to inequalities and to expectation (the probabilistic method).",
        ],
        "requirements": [
            "The bijection principle and basic graph vocabulary (vertex, edge, degree).",
            "Comfort with summation notation.",
        ],
        "standards": [
            "The incidence set S defined explicitly; both groupings shown to partition S.",
            "Each grouping's count derived, not asserted.",
        ],
        "citations": [C_VANLINT, C_BRUALDI],
        "sig_lens": (
            "Signature edition: double counting as his two-eyes proof - one Signature "
            "family of incidences seen from two sides must give the same Signature "
            "number."
        ),
        "demo_kind": "comb_double_count",
    },
    {
        "key": "integer_partitions",
        "name": "Integer Partitions: Breaking Numbers Apart",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "A partition of n is a way to write n as a sum of positive "
            "integers, order irrelevant: 4 = 3+1 = 2+2 = 2+1+1 = "
            "1+1+1+1, so p(4) = 5. The partition numbers p(n) grow fast "
            "and irregularly: p(10) = 42, p(50) = 204,226, p(100) = "
            "190,569,292. Partitions are drawn as Ferrers diagrams - rows "
            "of dots, nonincreasing - and conjugating a diagram "
            "(reflecting across the diagonal) bijects partitions with "
            "largest part k to partitions with exactly k parts: hence "
            "those two counts are equal. Euler proved the generating "
            "function product 1/((1-x)(1-x^2)(1-x^3)...) = sum p(n) x^n, "
            "and the pentagonal number theorem gives a recurrence "
            "computing p(n) from earlier values with alternating signs. "
            "Ramanujan found the congruences p(5n+4) divisible by 5, "
            "p(7n+5) by 7, p(11n+6) by 11 - deep facts whose proofs took "
            "decades. Partitions connect combinatorics to number theory, "
            "representation theory, and statistical physics."
        ),
        "how_it_works": (
            "Partitions are counted recursively: let p_k(n) be partitions "
            "of n with largest part at most k; then p_k(n) = p_k(n-k) + "
            "p_{k-1}(n) (either use a part of size k, or do not) - a "
            "dynamic program filling a table bottom-up. Ferrers diagrams "
            "make bijections visual: conjugation (transpose) swaps 'largest "
            "part' with 'number of parts'; removing the first column "
            "bijects partitions with no 1's to partitions of n-k with k "
            "parts. Euler's generating function works because 1/(1-x^k) "
            "= 1 + x^k + x^{2k} + ... contributes any number of k-parts, "
            "and multiplying over k lets each part size choose "
            "independently. For computation, Euler's pentagonal recurrence "
            "p(n) = sum_{k != 0} (-1)^{k+1} p(n - k(3k-1)/2) is the fast "
            "route - O(n sqrt n). In practice: draw the diagram, look for "
            "the conjugation or column-removal bijection, and reach for "
            "generating functions when recurrences stall."
        ),
        "key_points": [
            "p(n) counts partitions of n: p(4)=5, p(10)=42, p(100)=190,569,292.",
            "Ferrers diagrams + conjugation: partitions with largest part k <-> partitions with k parts.",
            "Euler's generating function: product_k 1/(1-x^k) = sum_n p(n) x^n.",
            "Pentagonal recurrence computes p(n) fast from earlier values.",
            "Ramanujan congruences (mod 5, 7, 11) link partitions to deep number theory.",
        ],
        "requirements": [
            "Recurrence thinking and the bijection principle.",
            "Generating function basics (previewed here, deepened at the OGF rung).",
        ],
        "standards": [
            "Partitions listed in nonincreasing order; diagrams drawn with nonincreasing rows.",
            "Bijection arguments name the diagram operation (conjugation, column removal).",
        ],
        "citations": [C_STANLEY, C_BRUALDI],
        "sig_lens": (
            "Signature edition: partitions as his breaking-apart - every integer a "
            "Signature whole, every partition a Signature way to write it as a sum, "
            "diagrams his pictures of the breaking."
        ),
        "demo_kind": "comb_int_partitions",
    },
    {
        "key": "stirling_second_kind",
        "name": "Set Partitions and Stirling Numbers of the Second Kind",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Where integer partitions break NUMBERS apart, set partitions "
            "break SETS apart: divide {1,2,3,4} into nonempty unlabeled "
            "groups. The Stirling numbers of the second kind, S(n,k) (or "
            "{n brace k}), count partitions of an n-element set into k "
            "nonempty unlabeled blocks: S(4,2) = 7. They satisfy the "
            "recurrence S(n,k) = k*S(n-1,k) + S(n-1,k-1): element n either "
            "joins one of the k blocks of a partition of the rest "
            "(k choices) or forms a singleton block. Summing over k gives "
            "the Bell numbers B_n = sum_k S(n,k), counting ALL set "
            "partitions: B_4 = 15, B_5 = 52, B_10 = 115,975. Stirling "
            "numbers of the second kind convert between powers and falling "
            "factorials: x^n = sum_k S(n,k) x_(k), where "
            "x_(k) = x(x-1)...(x-k+1) - the change-of-basis "
            "that makes them indispensable in finite differences and "
            "moments of distributions. Applications: clustering, "
            "equivalence relations (every partition is an equivalence "
            "relation's classes), and the twelvefold way's occupancy "
            "counts."
        ),
        "how_it_works": (
            "The recurrence is a case analysis on the distinguished "
            "element n: in a partition of [n] into k blocks, either {n} is "
            "a block alone (delete it: S(n-1,k-1) partitions of the rest "
            "into k-1 blocks) or n sits inside a block with others "
            "(partition the rest into k blocks: S(n-1,k) ways, then choose "
            "which of the k blocks receives n). Boundary: S(n,0) = 0 for "
            "n > 0, S(0,0) = 1, S(n,k) = 0 for k > n. Fill the Stirling "
            "triangle row by row - O(n^2). The power-to-falling-factorial "
            "identity is proved by counting functions: x^n counts all "
            "functions from an n-set to an x-set; group by image size k "
            "(C(x,k) image sets) times onto functions (k! S(n,k)). "
            "In practice: unlabeled groups = Stirling; labeled groups = "
            "multiply by k!. Forgetting the 'unlabeled' is the classic "
            "error - dividing 4 labeled people into 2 unlabeled pairs is "
            "S(4,2) = 7... wait, that is wrong: S(4,2) = 7 counts "
            "partitions into 2 blocks of any sizes; pairs-only needs the "
            "restricted count. Always check block-size restrictions."
        ),
        "key_points": [
            "S(n,k) counts partitions of an n-set into k nonempty unlabeled blocks; S(4,2) = 7.",
            "Recurrence: S(n,k) = k*S(n-1,k) + S(n-1,k-1) - element n joins a block or stands alone.",
            "Bell numbers B_n = sum_k S(n,k): B_4 = 15, B_5 = 52, B_10 = 115,975.",
            "Change of basis: x^n = sum_k S(n,k) x(x-1)...(x-k+1).",
            "Unlabeled blocks = Stirling; labeled blocks = multiply by k!; block sizes may need restricting.",
        ],
        "requirements": [
            "Set partitions vs. integer partitions (elements are distinct here).",
            "Recurrence thinking; falling factorial notation.",
        ],
        "standards": [
            "'Unlabeled blocks' stated explicitly; labeled variants multiplied by k! with justification.",
            "Boundary values S(0,0)=1, S(n,0)=0 (n>0) declared before using the recurrence.",
        ],
        "citations": [C_STANLEY, C_BRUALDI],
        "sig_lens": (
            "Signature edition: set partitions as his unlabeled gatherings - "
            "Signature elements sorted into Signature blocks with no names, counted by "
            "his Stirling triangle."
        ),
        "demo_kind": "comb_stirling2",
    },
    {
        "key": "stirling_first_kind",
        "name": "Permutation Cycles and Stirling Numbers of the First Kind",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Every permutation breaks into disjoint cycles: (1 3 2)(4 5) "
            "sends 1->3->2->1 and 4->5->4. The unsigned Stirling numbers of "
            "the first kind, c(n,k) (or [n brack k]), count permutations "
            "of n with exactly k cycles: c(4,2) = 11. They satisfy "
            "c(n,k) = c(n-1,k-1) + (n-1)*c(n-1,k): element n either forms "
            "its own 1-cycle, or is inserted into one of the n-1 gaps "
            "after existing elements in a k-cycle permutation of n-1. "
            "Summing over k gives n! - every permutation has some number "
            "of cycles. The signed versions s(n,k) = (-1)^{n-k} c(n,k) "
            "convert falling factorials to powers: x_(n) = "
            "sum_k s(n,k) x^k - the inverse change-of-basis to the second "
            "kind's. The two Stirling triangles are matrix inverses of "
            "each other, a fact visible in their generating functions. "
            "Cycle structure governs random permutations: the expected "
            "number of cycles in a random n-permutation is the harmonic "
            "number H_n ~ ln n, and the probability a given element lies "
            "in a cycle of length k is exactly 1/n for every k."
        ),
        "how_it_works": (
            "The recurrence's second term needs care: take a permutation "
            "of {1,...,n-1} with k cycles; element n can be spliced into "
            "any cycle right after any of the n-1 existing elements "
            "(n-1 insertion slots), preserving the cycle count. The first "
            "term: n as a fixed point (1-cycle) atop a k-1-cycle "
            "permutation of the rest. Boundary: c(0,0) = 1, c(n,0) = 0 "
            "for n > 0. To convert x_(n) to powers: expand "
            "using the signed triangle - e.g., x_(3) = x^3 "
            "- 3x^2 + 2x from the row c(3,3)=1, c(3,2)=3, c(3,1)=2 with "
            "signs (-1)^{3-k}. In practice: 'permutations with k cycles' "
            "= first kind; 'set partitions into k blocks' = second kind - "
            "the names are easy to swap, so anchor on the objects. "
            "Applications: analyzing sorting by cycle decomposition "
            "(a k-cycle needs k-1 swaps), random permutation statistics, "
            "and the rising/falling factorial bases of the calculus of "
            "finite differences."
        ),
        "key_points": [
            "c(n,k) counts n-permutations with exactly k disjoint cycles; c(4,2) = 11.",
            "Recurrence: c(n,k) = c(n-1,k-1) + (n-1)*c(n-1,k) - new 1-cycle or splice into n-1 slots.",
            "Row sums give n!; signed versions convert falling factorials to powers.",
            "The two Stirling triangles are matrix inverses - dual changes of basis.",
            "Random permutation: expected cycles ~ ln n; P(element in a k-cycle) = 1/n for all k.",
        ],
        "requirements": [
            "Permutations and cycle notation.",
            "Stirling numbers of the second kind (for the duality contrast).",
        ],
        "standards": [
            "First kind (cycles) vs. second kind (blocks) distinguished by the objects counted.",
            "Signed vs. unsigned stated explicitly when converting bases.",
        ],
        "citations": [C_STANLEY, C_BRUALDI],
        "sig_lens": (
            "Signature edition: cycles as his closed loops - every Signature permutation "
            "a union of Signature cycles, counted by his first-kind triangle, dual to "
            "his blocks."
        ),
        "demo_kind": "comb_stirling1",
    },
    {
        "key": "lattice_paths_reflection",
        "name": "Lattice Paths and the Reflection Principle",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "A lattice path from (0,0) to (a,b) using steps right (1,0) "
            "and up (0,1) is a sequence of a+b steps with a rights: "
            "C(a+b, a) paths. The reflection principle counts the paths "
            "that cross a forbidden line: reflect the path up to its "
            "first crossing, bijecting bad paths to paths from the "
            "reflected start. Bertrand's ballot problem: candidate A gets "
            "a votes, B gets b (a > b); in how many vote-count orders does "
            "A always lead? Answer: (a-b)/(a+b) * C(a+b, a) - total orders "
            "minus reflected bad orders. Setting b = a gives the Catalan "
            "connection: paths from (0,0) to (n,n) that never rise above "
            "the diagonal number the Catalan number C_n (next rung's "
            "neighbor). The reflection principle is Andre's 1887 solution, "
            "and it generalizes: the reflection method counts walks with "
            "barriers throughout probability (the gambler's ruin, Brownian "
            "barrier options) via the same mirror trick."
        ),
        "how_it_works": (
            "Count paths from (0,0) to (a,b) that at some point go above "
            "the diagonal y = x (for a >= b). Take a bad path; find its "
            "first step that goes above the diagonal; reflect all steps "
            "up to and including that step across the line y = x + 1 "
            "(swap right/up and shift start). This bijects bad paths to "
            "ALL paths from (-1,1) to (a,b) - which need a+1 rights and "
            "b-1 ups: C(a+b, a+1)... careful with the exact shift; the "
            "standard count of bad paths is C(a+b, a-1) for the ballot "
            "setting. Good paths = total - bad = C(a+b,a) - C(a+b,a-1) "
            "= (a-b+1)/(a+1) * C(a+b, a) in one common form; the ballot "
            "form (a-b)/(a+b)*C(a+b,a) counts strict-lead orders. To use "
            "it: (1) encode outcomes as paths; (2) identify the forbidden "
            "crossing; (3) reflect to count the bad ones; (4) subtract. "
            "The method fails when the barrier is not a straight line - "
            "curved barriers need different tools."
        ),
        "key_points": [
            "C(a+b, a) lattice paths from (0,0) to (a,b); reflection bijects bad paths to shifted-start paths.",
            "Ballot: A always leads in (a-b)/(a+b) * C(a+b,a) of the vote orders (a > b).",
            "Andre's 1887 reflection solution; the prototype of barrier arguments in probability.",
            "Diagonal-constrained paths give the Catalan numbers - the bridge to the next rung.",
            "Needs a straight-line barrier; curved barriers need other methods.",
        ],
        "requirements": [
            "Combinations and the bijection principle.",
            "Comfort with coordinate paths and step sequences.",
        ],
        "standards": [
            "The reflection map described as an explicit operation on step sequences.",
            "Ballot formula's strict-inequality conditions (a > b) stated.",
        ],
        "citations": [C_VANLINT, C_BRUALDI],
        "sig_lens": (
            "Signature edition: lattice paths as his grid journeys - every Signature "
            "route a sequence of rights and ups, bad routes mirrored away by his "
            "reflection law."
        ),
        "demo_kind": "comb_lattice_paths",
    },
    {
        "key": "recurrence_relations",
        "name": "Recurrence Relations: Sequences Defined by Their Past",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "A recurrence defines each term from earlier terms: the "
            "Fibonacci numbers F_n = F_{n-1} + F_{n-2} with F_0 = 0, F_1 = "
            "1. Recurrences are everywhere counting is: derangements, "
            "Stirling numbers, Bell numbers, Catalan numbers, and "
            "partitions all satisfy them. The Tower of Hanoi needs "
            "T_n = 2*T_{n-1} + 1 moves (T_64 is about 585 billion years at "
            "one move per second). Triangulations, tilings (domino tilings "
            "of a 2xn board satisfy the Fibonacci recurrence), and "
            "well-formed parentheses all reduce to smaller cases. A "
            "recurrence plus initial conditions determines a sequence "
            "completely - computing forward is just iteration. The art is "
            "FINDING the recurrence: look at the first choice or the "
            "distinguished element, and ask how the remaining problem is "
            "a smaller copy of the original. Linear recurrences with "
            "constant coefficients (next rung) solve in closed form; "
            "nonlinear ones (Catalan's convolution) need generating "
            "functions."
        ),
        "how_it_works": (
            "To find a recurrence: (1) identify the parameter n and the "
            "count a_n; (2) examine the first decision - e.g., for domino "
            "tilings of a 2xn board, the leftmost column is either a "
            "vertical domino (leaving a 2x(n-1) board) or two horizontal "
            "dominoes (leaving 2x(n-2)): a_n = a_{n-1} + a_{n-2}; "
            "(3) verify the remaining pieces are genuinely smaller copies "
            "with no interaction across the boundary; (4) set initial "
            "conditions by hand-counting small n (a_0 = 1: one way to tile "
            "nothing; a_1 = 1). Then compute forward: iteration is O(n). "
            "Watch for: missing cases (the #1 recurrence bug - always test "
            "n = 0,1,2,3 against brute force), overlapping cases (use "
            "disjoint case analysis), and off-by-one initial conditions. "
            "Recurrences also run backward as definitions: the "
            "derangement recurrence !n = (n-1)(!(n-1)+!(n-2)) was proved "
            "this way two rungs ago."
        ),
        "key_points": [
            "Recurrence + initial conditions determines a sequence completely; compute forward by iteration.",
            "Find it via the first decision: the remaining problem must be smaller disjoint copies.",
            "Domino tilings of 2xn: a_n = a_{n-1} + a_{n-2} (Fibonacci) - vertical vs. horizontal pair.",
            "Tower of Hanoi: T_n = 2*T_{n-1} + 1; T_64 ~ 1.8e19 moves.",
            "Debug rule: test n=0,1,2,3 against brute force - missing cases are the #1 bug.",
        ],
        "requirements": [
            "Basic sequence concepts; comfort with small-case hand enumeration.",
            "Disjoint case analysis from the foundations.",
        ],
        "standards": [
            "Initial conditions computed by hand, not inherited from the recurrence.",
            "Recurrence verified against brute-force counts for n = 0..3 (or stated range).",
        ],
        "citations": [C_TUCKER, C_BRUALDI],
        "sig_lens": (
            "Signature edition: recurrences as his memory law - every Signature term "
            "remembering its past, every sequence his past determining his future."
        ),
        "demo_kind": "comb_recurrence",
    },
    {
        "key": "linear_recurrences_characteristic",
        "name": "Solving Linear Recurrences: The Characteristic Equation",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Linear recurrences with constant coefficients solve in closed "
            "form. For a_n = c_1 a_{n-1} + ... + c_k a_{n-k}, assume "
            "a_n = r^n: dividing by r^{n-k} gives the characteristic "
            "equation r^k = c_1 r^{k-1} + ... + c_k. Each root r contributes "
            "a term A*r^n; distinct roots give a_n = A_1 r_1^n + ... + "
            "A_k r_k^n, with the A's fixed by initial conditions. "
            "Fibonacci: r^2 = r + 1 gives r = (1 +/- sqrt(5))/2, and "
            "Binet's formula F_n = (phi^n - psi^n)/sqrt(5) - integers "
            "emerging from irrational powers, the algebra canceling "
            "perfectly. Example: a_n = 5a_{n-1} - 6a_{n-2}, a_0 = 0, "
            "a_1 = 1: characteristic r^2 - 5r + 6 = 0, roots 2 and 3, so "
            "a_n = 3^n - 2^n. Repeated roots need polynomial factors "
            "(n*r^n); complex roots give oscillating terms (r^n times "
            "sines/cosines). This is the discrete analog of solving "
            "linear differential equations - same characteristic-equation "
            "idea, and the bridge between combinatorics and linear "
            "algebra."
        ),
        "how_it_works": (
            "The method: (1) write the characteristic equation by "
            "replacing a_{n-j} with r^{k-j}; (2) find its k roots "
            "(factor, or quadratic formula for k=2); (3) for distinct "
            "roots, write a_n = sum A_i r_i^n; for a root r of "
            "multiplicity m, include A_1 r^n + A_2 n r^n + ... + A_m "
            "n^{m-1} r^n; (4) solve for the A's using the k initial "
            "conditions (a linear system); (5) verify by plugging n = "
            "0,1,2 back in. Why it works: the solution space of a "
            "k-th order linear homogeneous recurrence is k-dimensional, "
            "and the r_i^n (with polynomial factors for repeats) are k "
            "independent solutions. Nonhomogeneous recurrences (like "
            "Hanoi's T_n = 2T_{n-1} + 1) add a particular solution - "
            "guess its form from the nonhomogeneous term (constant -> "
            "try constant A; the guess A = 2A + 1 gives A = -1, so "
            "T_n = C*2^n - 1, and T_0 = 0 gives C = 1)."
        ),
        "key_points": [
            "Assume a_n = r^n -> characteristic equation; roots give the building blocks.",
            "Distinct roots: a_n = sum A_i r_i^n; repeated root r (mult. m): polynomial times r^n up to n^{m-1}.",
            "Binet: F_n = (phi^n - psi^n)/sqrt(5) - integers from irrational powers.",
            "Example: a_n = 5a_{n-1} - 6a_{n-2}, a_0=0, a_1=1 -> a_n = 3^n - 2^n.",
            "Discrete analog of linear ODEs; nonhomogeneous terms need a particular-solution guess.",
        ],
        "requirements": [
            "Recurrence relations; solving quadratic equations.",
            "Linear systems for fitting initial conditions (2x2 suffices for order 2).",
        ],
        "standards": [
            "Characteristic equation written explicitly; root multiplicities handled with n-polynomial factors.",
            "Closed form verified against the recurrence for the first k terms.",
        ],
        "citations": [C_TUCKER, C_BRUALDI],
        "sig_lens": (
            "Signature edition: the characteristic equation as his root law - every "
            "Signature recurrence cracked open by its roots, every closed form his "
            "past solved into powers."
        ),
        "demo_kind": "comb_char_eq",
    },
    {
        "key": "ordinary_generating_functions",
        "name": "Ordinary Generating Functions",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "The ordinary generating function (OGF) of a sequence a_0, "
            "a_1, ... is the power series A(x) = sum a_n x^n - the "
            "sequence encoded as coefficients. This encoding turns "
            "recurrences into algebra: the Fibonacci recurrence "
            "F_n = F_{n-1} + F_{n-2} becomes F(x) = x/(1 - x - x^2), and "
            "partial fractions recover Binet's formula. Shifting the "
            "sequence multiplies by x; convolution of sequences "
            "multiplies their OGFs - which is why the Catalan "
            "convolution recurrence becomes a quadratic equation for its "
            "OGF. The dictionary: 1/(1-x) <-> all-ones; 1/(1-x)^2 <-> "
            "1,2,3,...; 1/(1-x)^{k+1} <-> C(n+k,k); x^m/(1-x) <-> 0,...,0,"
            "1,1,1,... Recognizing a sequence's OGF (or a series' "
            "sequence) is a core enumerative skill: partitions live at "
            "product 1/(1-x^k), compositions at 1/(1-2x) variants, and "
            "rational OGFs always signal linear recurrences with constant "
            "coefficients. Wilf's 'generatingfunctionology' made this the "
            "standard power tool of enumerative combinatorics."
        ),
        "how_it_works": (
            "To solve a recurrence with OGFs: (1) multiply the recurrence "
            "by x^n and sum over n; (2) express the sums in terms of A(x) "
            "- sum a_{n-1} x^n = x A(x) (shift), sum a_{n-2} x^n = x^2 "
            "A(x); (3) solve the resulting algebraic equation for A(x); "
            "(4) expand back to coefficients via partial fractions or "
            "known series. Example: a_n = 3a_{n-1} - 2a_{n-2} (a_0 = 0, "
            "a_1 = 1): summing gives A - 0 - x = 3xA - 2x^2 A, so "
            "A(x) = x/((1-x)(1-2x)) = 1/(1-2x) - 1/(1-x), reading off "
            "a_n = 2^n - 1. The convolution rule - OGF of (a*b)_n = "
            "sum_k a_k b_{n-k} is A(x)B(x) - handles the Catalan "
            "recurrence C_{n+1} = sum C_i C_{n-i}: with C(x) = sum C_n "
            "x^n it gives C = 1 + xC^2, solved by the quadratic formula. "
            "Always check: the constant term of A(x) must equal a_0."
        ),
        "key_points": [
            "OGF: A(x) = sum a_n x^n - the sequence as power-series coefficients.",
            "Shift <-> multiply by x; convolution <-> multiply OGFs; recurrences -> algebra.",
            "Dictionary: 1/(1-x) <-> ones; 1/(1-x)^2 <-> 1,2,3,...; x^m/(1-x) <-> delayed ones.",
            "Rational OGF always means a linear recurrence with constant coefficients.",
            "Fibonacci: F(x) = x/(1-x-x^2); Catalan: C = 1 + xC^2 from the convolution rule.",
        ],
        "requirements": [
            "Recurrence relations and power series basics.",
            "Partial fractions at a usable level.",
        ],
        "standards": [
            "A(x) derived term-by-term from the summed recurrence; constant term checked against a_0.",
            "Series expansions verified coefficient-by-coefficient for the first terms.",
        ],
        "citations": [C_WILF, C_STANLEY],
        "sig_lens": (
            "Signature edition: ordinary generating functions as his sequence vault - "
            "every Signature sequence folded into one Signature power series, every "
            "recurrence his algebra waiting to be solved."
        ),
        "demo_kind": "comb_ogf",
    },
    {
        "key": "exponential_generating_functions",
        "name": "Exponential Generating Functions",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "When structures are LABELED - permutations of {1..n}, set "
            "partitions of [n], graphs on labeled vertices - the ordinary "
            "generating function misbehaves, because combining two labeled "
            "structures requires choosing which labels go where (a binomial "
            "convolution). The exponential generating function (EGF) "
            "A(x) = sum a_n x^n/n! absorbs those binomial coefficients: "
            "the labeled product of classes has EGF equal to the product "
            "of EGFs. The dictionary: e^x <-> all-ones (n! labeled "
            "structures counted once each... precisely: a_n = 1); "
            "1/(1-x) is NOT e^x's partner here - instead, permutations "
            "(sets of cycles) give 1/(1-x) as an EGF too, since "
            "a_n = n!; derangements give e^{-x}/(1-x); set partitions "
            "(sets of nonempty sets) give e^{e^x - 1}, whose coefficients "
            "are the Bell numbers. The symbolic method (labeled "
            "constructions: disjoint union -> sum, labeled product -> "
            "product, set -> exp, sequence -> 1/(1-)) turns combinatorial "
            "specifications directly into EGF equations - counting by "
            "writing down what the objects ARE."
        ),
        "how_it_works": (
            "The labeled product: to combine an A-structure on k labels "
            "with a B-structure on n-k labels into an n-label structure, "
            "choose the k labels (C(n,k) ways) - and C(n,k) a_k b_{n-k} "
            "/ n! = (a_k/k!)(b_{n-k}/(n-k)!), so the EGFs multiply. "
            "Constructions: disjoint union of classes -> sum of EGFs; "
            "labeled product -> product; SET of components -> exp (since "
            "exp = sum x^n/n! encodes 'sets of atoms'); SEQUENCE -> "
            "1/(1-A(x)); CYCLE -> -ln(1-A(x)). Examples: permutations are "
            "sets of cycles of atoms: EGF = exp(-ln(1-x)) = 1/(1-x), "
            "coefficients n!. Set partitions are sets of nonempty sets of "
            "atoms: exp(e^x - 1), coefficients the Bell numbers. "
            "Derangements are sets of cycles of length >= 2: "
            "exp(-ln(1-x) - x) = e^{-x}/(1-x). To use: (1) decide labeled "
            "vs. unlabeled (EGF vs. OGF); (2) write the specification; "
            "(3) translate to the EGF equation; (4) extract coefficients."
        ),
        "key_points": [
            "EGF: A(x) = sum a_n x^n/n! - the tool for LABELED structures.",
            "Labeled product -> product of EGFs (binomial convolution absorbed).",
            "Symbolic method: union -> +, product -> x, set -> exp, sequence -> 1/(1-), cycle -> -ln(1-).",
            "Permutations (sets of cycles): 1/(1-x); set partitions: e^{e^x-1} (Bell numbers).",
            "Labeled vs. unlabeled decides EGF vs. OGF - the most important modeling choice in enumeration.",
        ],
        "requirements": [
            "Ordinary generating functions; exponential series e^x.",
            "Labeled vs. unlabeled structures (permutations vs. integer partitions).",
        ],
        "standards": [
            "Labeled/unlabeled declared before choosing EGF/OGF.",
            "Each construction step mapped to its EGF operation explicitly.",
        ],
        "citations": [C_WILF, C_STANLEY],
        "sig_lens": (
            "Signature edition: exponential generating functions as his labeled vault - "
            "Signature structures wearing their labels, combined by his symbolic "
            "method into Signature equations."
        ),
        "demo_kind": "comb_egf",
    },
    {
        "key": "twelvefold_way",
        "name": "The Twelvefold Way: Balls into Boxes",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "How many ways can n balls go into k boxes? The answer depends "
            "on three binary choices - balls distinct or identical, boxes "
            "distinct or identical, and at most one / exactly one / any "
            "number per box - giving twelve cases (Rota's twelvefold way). "
            "The table: distinct balls, distinct boxes, any number: k^n "
            "(each ball chooses); injective (<= 1 per box): P(k,n); "
            "surjective (>= 1): k! S(n,k); identical balls, distinct boxes, "
            "any: C(n+k-1,n) (stars and bars); <= 1: C(k,n); >= 1: "
            "C(n-1,k-1); identical balls, identical boxes: partitions "
            "p_k(n), p_{<=k}(n), p_{=k}(n)...; distinct balls, identical "
            "boxes: S(n,k) (surjective), Bell-like sums, and 1 or 0 for "
            "the restricted cases. The twelvefold way is the master "
            "summary of elementary enumeration: every basic counting "
            "problem is one of its cells, and the formulas interlock - "
            "dividing by symmetries moves between columns, stars-and-bars "
            "and Stirling numbers fill the rows. When a counting problem "
            "confuses you, locate its cell."
        ),
        "how_it_works": (
            "Classify the problem: (1) Are the balls (objects) distinct? "
            "People, labeled items: yes. Cookies, votes: no. (2) Are the "
            "boxes (containers) distinct? Children, days: yes. Unlabeled "
            "groups: no. (3) What occupancy restriction? Then read the "
            "cell: [distinct/distinct/any] = k^n; [distinct/distinct/<=1] "
            "= P(k,n) = k!/(k-n)!; [distinct/distinct/>=1] = k! S(n,k) "
            "(partition into k unlabeled groups, then label them); "
            "[identical/distinct/any] = C(n+k-1, n); [identical/distinct/"
            "<=1] = C(k,n); [identical/distinct/>=1] = C(n-1,k-1); "
            "[identical/identical/*] = partition numbers p(n) variants; "
            "[distinct/identical/>=1] = S(n,k); [distinct/identical/any] "
            "= sum_{i<=k} S(n,i); [distinct/identical/<=1] = 1 if n <= k "
            "else 0. Moving right across columns divides by box "
            "symmetries; moving down rows applies stars-and-bars or "
            "Stirling logic. Verify small cases by brute-force "
            "enumeration - the table is a theorem, but your "
            "classification of the problem is the fallible step."
        ),
        "key_points": [
            "Three choices (balls distinct? boxes distinct? occupancy?) give twelve counting cases.",
            "Distinct/distinct: k^n (any), P(k,n) (<=1), k!S(n,k) (>=1).",
            "Identical/distinct: C(n+k-1,n) (any), C(k,n) (<=1), C(n-1,k-1) (>=1).",
            "Distinct/identical: S(n,k) (>=1), Bell-like sums (any); identical/identical: partition numbers.",
            "Master summary of elementary enumeration - locate your problem's cell when confused.",
        ],
        "requirements": [
            "All foundation rungs: permutations, combinations, stars and bars, Stirling numbers.",
            "Comfort with 3-way case classification.",
        ],
        "standards": [
            "All three classifications (balls, boxes, occupancy) stated before reading the cell.",
            "Small cases verified by brute-force enumeration.",
        ],
        "citations": [C_STANLEY, C_TUCKER],
        "sig_lens": (
            "Signature edition: the twelvefold way as his master table - every "
            "Signature distribution of balls into boxes one of his twelve cells, "
            "every formula his symmetry made visible."
        ),
        "demo_kind": "comb_twelvefold",
    },
    {
        "key": "catalan_numbers",
        "name": "Catalan Numbers: The Ubiquitous Sequence",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "1, 1, 2, 5, 14, 42, 132, 429, ... - the Catalan numbers "
            "C_n = (1/(n+1)) C(2n,n) appear in over 200 combinatorial "
            "settings (Stanley lists 214). Dyck paths from (0,0) to (n,n) "
            "never rising above the diagonal; correctly matched "
            "parentheses with n pairs; binary trees with n internal "
            "nodes; triangulations of an (n+2)-gon; noncrossing partitions; "
            "stack-sortable permutations. They satisfy the convolution "
            "recurrence C_{n+1} = sum_{i=0}^{n} C_i C_{n-i}: in a Dyck "
            "path, look at the first return to the diagonal - the path "
            "splits into two independent Dyck paths. The OGF satisfies "
            "C(x) = 1 + x C(x)^2, giving C(x) = (1 - sqrt(1-4x))/(2x) and "
            "the closed form via the generalized binomial theorem. "
            "Eugene Catalan studied them in 1838 (Euler and Segner had "
            "them for triangulations in the 1750s). Whenever a structure "
            "decomposes as 'a root plus two smaller independent copies', "
            "suspect Catalan."
        ),
        "how_it_works": (
            "The convolution recurrence is proved by first-return "
            "decomposition: a Dyck path of semilength n+1 first touches "
            "the diagonal again at (i+1, i+1) for some i; the excursion "
            "before is a Dyck path of semilength i (shifted up), the rest "
            "a Dyck path of semilength n-i - independent, so multiply and "
            "sum. For trees: a binary tree with n+1 internal nodes has a "
            "root with left subtree of i nodes and right of n-i. For "
            "parentheses: the matching close of the first open splits the "
            "string. The OGF equation C = 1 + xC^2 solves to "
            "(1-sqrt(1-4x))/(2x); expanding sqrt via the binomial series "
            "gives C_n = (1/(n+1))C(2n,n). Asymptotically C_n ~ "
            "4^n/(n^{3/2} sqrt(pi)). In practice: (1) look for the "
            "'root + two independent parts' decomposition; (2) confirm "
            "the parts are independent and cover all cases; (3) the "
            "recurrence or OGF follows. The bijection between any two "
            "Catalan families (trees <-> paths <-> parentheses) is always "
            "the same idea: read the decomposition recursively."
        ),
        "key_points": [
            "C_n = (1/(n+1))C(2n,n): 1, 1, 2, 5, 14, 42, 132, 429, ...",
            "Over 200 settings: Dyck paths, parentheses, binary trees, triangulations, noncrossing partitions.",
            "Convolution recurrence C_{n+1} = sum C_i C_{n-i} via first-return decomposition.",
            "OGF: C = 1 + xC^2 -> (1-sqrt(1-4x))/(2x); asymptotics 4^n/(n^{3/2} sqrt(pi)).",
            "Signature of Catalan: 'a root plus two smaller independent copies'.",
        ],
        "requirements": [
            "Recurrences, OGFs (convolution rule), lattice paths.",
            "Binomial series expansion (for the closed form).",
        ],
        "standards": [
            "The first-return/root decomposition shown to be a genuine bijection (invertible).",
            "OGF equation derived from the recurrence, not quoted.",
        ],
        "citations": [C_STANLEY, C_BRUALDI],
        "sig_lens": (
            "Signature edition: Catalan numbers as his universal sequence - two "
            "hundred Signature settings, one Signature count, every decomposition "
            "his root with two smaller copies."
        ),
        "demo_kind": "comb_catalan",
    },
]

ENTRIES += [
    {
        "key": "bell_numbers",
        "name": "Bell Numbers and the Partitions of a Set",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The Bell numbers B_n count ALL partitions of an n-element set "
            "into unlabeled blocks: B_0 = 1, B_1 = 1, B_2 = 2, B_3 = 5, "
            "B_4 = 15, B_5 = 52, B_6 = 203, B_10 = 115,975. They sum the "
            "Stirling second-kind triangle: B_n = sum_k S(n,k). They "
            "satisfy the recurrence B_{n+1} = sum_{k=0}^{n} C(n,k) B_k: "
            "in a partition of [n+1], element n+1's block contains k other "
            "chosen elements (C(n,k) ways) plus a partition of the rest "
            "(B_k ways). Their EGF is e^{e^x - 1} - sets of nonempty sets "
            "of atoms. Dobinski's formula gives the startling identity "
            "B_n = (1/e) sum_{k>=0} k^n/k! - the n-th moment of a "
            "Poisson(1) distribution. The Bell triangle (Aitken's array) "
            "computes them: each row starts with the last entry of the "
            "previous row, and each entry sums the one above-left and "
            "above. Touchard's congruence and the rapid growth "
            "(log B_n ~ n log n) round out the picture. Bell numbers "
            "govern clustering, equivalence relations, and rhyme schemes "
            "(partitions of line positions into rhyme classes)."
        ),
        "how_it_works": (
            "The recurrence's proof: fix element n+1; its block has k "
            "other members chosen from [n] (C(n,k) ways); the remaining "
            "n-k elements partition freely (B_{n-k}... reindex to B_k). "
            "Summing over k counts every partition once, since every "
            "partition has exactly one block containing n+1. The EGF: "
            "set partitions are SETS of NONEMPTY SETS of atoms; nonempty "
            "set has EGF e^x - 1, and set-of gives exp: e^{e^x - 1}. "
            "Extracting coefficients: differentiate or use the recurrence "
            "B_{n+1} = sum C(n,k) B_k. Dobinski: expand e^{e^x-1} = "
            "(1/e) sum_k e^{kx}/k! = (1/e) sum_k sum_n k^n x^n/(n! k!), "
            "read the x^n/n! coefficient. In practice: (1) 'all ways to "
            "group n labeled items into unlabeled groups' = Bell; "
            "(2) compute via the C(n,k)-weighted recurrence or Aitken's "
            "triangle; (3) for asymptotics use log B_n ~ n(log n - log "
            "log n). Labeled groups multiply by block factorials - do "
            "not confuse with the twelvefold way's distinct-boxes cells."
        ),
        "key_points": [
            "B_n counts all set partitions: 1, 1, 2, 5, 15, 52, 203, ..., B_10 = 115,975.",
            "Recurrence: B_{n+1} = sum_k C(n,k) B_k - condition on element n+1's block.",
            "EGF: e^{e^x - 1} (sets of nonempty sets); Dobinski: B_n = (1/e) sum k^n/k!.",
            "Aitken's Bell triangle computes them with pure addition.",
            "Growth: log B_n ~ n log n; applications in clustering, equivalence relations, rhyme schemes.",
        ],
        "requirements": [
            "Stirling numbers of the second kind; EGFs (set construction).",
            "Binomial coefficients.",
        ],
        "standards": [
            "'Unlabeled blocks' verified; labeled-group variants distinguished explicitly.",
            "Recurrence proved by conditioning on the distinguished element's block.",
        ],
        "citations": [C_STANLEY, C_BRUALDI],
        "sig_lens": (
            "Signature edition: Bell numbers as his total gatherings - every Signature "
            "set partitioned every Signature way, summed by his recurrence into one "
            "Signature count."
        ),
        "demo_kind": "comb_bell",
    },
    {
        "key": "integer_partitions_euler",
        "name": "Partitions of Integers: Euler's Theorems",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Beyond the basics: Euler's great partition theorems. (1) The "
            "number of partitions of n into ODD parts equals the number "
            "into DISTINCT parts. Proof by bijection: write each part as "
            "odd times a power of 2 (m = 2^k * q), then merge equal odd "
            "components - splitting and merging are inverse. Generating "
            "functions agree: product 1/(1-x^{2k-1}) = product (1+x^k), "
            "since 1/(1-x^{odd}) telescopes against (1-x^{2k})/(1-x^k). "
            "(2) The pentagonal number theorem: product_{k>=1} (1 - x^k) "
            "= sum_{k} (-1)^k x^{k(3k-1)/2} - the exponents are the "
            "generalized pentagonal numbers 1, 2, 5, 7, 12, 15, ... "
            "Franklin's involution proves it combinatorially. (3) Hence "
            "the recurrence p(n) = sum_{k != 0} (-1)^{k+1} "
            "p(n - k(3k-1)/2), computing p(200) = 3,972,999,029,388 "
            "exactly - the value Hardy and Ramanujan's asymptotic formula "
            "approximates. These theorems made partitions the meeting "
            "point of combinatorics, analysis, and number theory."
        ),
        "how_it_works": (
            "Odd-distinct bijection in detail: take a partition into odd "
            "parts, e.g., 9+9+5+3+3+1; group equal parts: two 9's, one 5, "
            "two 3's, one 1; merge pairs repeatedly (9+9 = 18, 3+3 = 6): "
            "18+6+5+1 - all distinct. Reverse: split even parts in half "
            "until all odd. These invert each other because writing "
            "m = 2^k * q (q odd) is unique. Pentagonal recurrence for "
            "computation: p(n) = p(n-1) + p(n-2) - p(n-5) - p(n-7) + "
            "p(n-12) + p(n-15) - ..., signs in pairs (+,+,-,-,...), "
            "skipping nonpositive arguments (p(0) = 1, p(negative) = 0). "
            "For p(10): p(10) = p(9)+p(8)-p(5)-p(3)+p(-2)... = 30+22-7-3 "
            "= 42. In practice: (1) for exact p(n), implement the "
            "pentagonal recurrence with memoization - O(n sqrt n); "
            "(2) for identities, match generating functions "
            "term-by-term; (3) for bijections, always exhibit the inverse."
        ),
        "key_points": [
            "Odd parts <-> distinct parts: merge/split equal parts (binary expansion of multiplicities).",
            "Pentagonal theorem: product (1-x^k) = sum (-1)^k x^{k(3k-1)/2} (Franklin's involution).",
            "Recurrence: p(n) = sum (-1)^{k+1} p(n - pentagonal_k); computes p(200) = 3,972,999,029,388.",
            "Generating functions: product 1/(1-x^{odd}) = product (1+x^k) proves odd=distinct algebraically.",
            "Partitions as the meeting point of combinatorics, analysis, and number theory.",
        ],
        "requirements": [
            "Integer partitions, Ferrers diagrams, generating functions.",
            "Unique factorization m = 2^k * q (q odd).",
        ],
        "standards": [
            "Bijection proofs exhibit the inverse map explicitly.",
            "Pentagonal recurrence implemented with p(0)=1, p(negative)=0, signs in (+,+,-,-) pairs.",
        ],
        "citations": [C_STANLEY, C_BRUALDI],
        "sig_lens": (
            "Signature edition: Euler's theorems as his deep partition laws - odd "
            "merging into distinct by his binary splitting, pentagonal numbers his "
            "Signature recurrence for the partition counts."
        ),
        "demo_kind": "comb_partition_gf",
    },
    {
        "key": "graph_counting_handshaking",
        "name": "Graph Theory as Counting: Walks and the Handshaking Lemma",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Graphs are combinatorics made visual: vertices and edges, "
            "and the counts begin immediately. The handshaking lemma: "
            "sum of degrees = 2|E| - every edge contributes 2 to the "
            "degree sum. Corollary: the number of odd-degree vertices is "
            "even (an even sum needs an even number of odd terms) - at "
            "any party, an even number of people shook an odd number of "
            "hands. Walks are counted by the adjacency matrix: (A^k)_{ij} "
            "is the number of walks of length k from i to j - matrix "
            "multiplication IS walk-counting, since (AB)_{ij} = sum_m "
            "A_{im} B_{mj} sums over middle vertices. The trace of A^2 is "
            "twice the edge count; the trace of A^3 is six times the "
            "triangle count. Degree sequences: a nonincreasing sequence "
            "is graphic (realizable by a simple graph) iff the "
            "Erdos-Gallai inequalities hold - or constructively, the "
            "Havel-Hakimi algorithm (strip the top degree d, subtract 1 "
            "from the next d entries, repeat) succeeds iff the sequence "
            "is graphic."
        ),
        "how_it_works": (
            "Handshaking via double counting incidences (proved at the "
            "double-counting rung). Adjacency powers: prove (A^k)_{ij} "
            "counts k-walks by induction - a k-walk i->j goes i->m (k-1 "
            "walk) then m->j (edge); summing over m is matrix "
            "multiplication. Applications: triangle counting via "
            "trace(A^3)/6; connectivity via reachability in powers; "
            "counting closed walks for spectral bounds. Havel-Hakimi: to "
            "test (d_1 >= ... >= d_n), remove d_1, subtract 1 from the "
            "next d_1 entries, drop zeros, repeat - success (all zeros) "
            "iff graphic; the proof: in some realization the top vertex "
            "connects to the next d_1 highest-degree vertices (an "
            "exchange argument). In practice: (1) model the situation as "
            "vertices + edges; (2) translate the question to degrees, "
            "walks, or degree sequences; (3) let the matrix or the "
            "algorithm count. Loops and multiple edges need care - "
            "state the graph model first."
        ),
        "key_points": [
            "Handshaking: sum of degrees = 2|E|; the number of odd-degree vertices is even.",
            "(A^k)_{ij} counts walks of length k from i to j - matrix multiplication is walk-counting.",
            "trace(A^3)/6 counts triangles; trace(A^2)/2 counts edges.",
            "Havel-Hakimi tests degree sequences constructively; Erdos-Gallai gives inequalities.",
            "State the graph model (simple? loops? multigraph?) before counting.",
        ],
        "requirements": [
            "Double counting; basic matrix multiplication.",
            "Graph vocabulary: vertex, edge, degree, walk, path.",
        ],
        "standards": [
            "Graph model declared (simple graph unless stated otherwise).",
            "Walk counts verified on small graphs by hand enumeration.",
        ],
        "citations": [C_BONDY, C_DIESTEL],
        "sig_lens": (
            "Signature edition: graphs as his connection maps - every Signature vertex "
            "a place, every Signature edge a handshake, walks his powers of adjacency."
        ),
        "demo_kind": "comb_graph_counting",
    },
    {
        "key": "trees_cayley",
        "name": "Trees and Cayley's Formula",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "A tree is a connected graph with no cycles - and it has "
            "exactly n-1 edges on n vertices, exactly one path between "
            "any two vertices, and the property that every edge is a "
            "bridge (removing it disconnects). These equivalences are "
            "the tree theorem. Cayley's formula: the number of labeled "
            "trees on vertices {1,...,n} is n^{n-2} - for n=4, 16 trees. "
            "Prufer proved it with a bijection: Prufer sequences are "
            "strings of length n-2 over [n], and each labeled tree encodes "
            "uniquely as one - repeatedly delete the smallest leaf and "
            "record its neighbor. There are n^{n-2} such strings, hence "
            "n^{n-2} trees. Kirchhoff's matrix-tree theorem generalizes: "
            "any cofactor of the Laplacian counts spanning trees of any "
            "graph (Cayley is the complete-graph case). Spanning trees "
            "are the backbone of network design - minimum spanning trees "
            "(Kruskal, Prim) wire n sites cheapest - and of random graph "
            "theory, phylogenetics, and electrical networks."
        ),
        "how_it_works": (
            "Prufer encoding: given a labeled tree on [n], repeat n-2 "
            "times: find the smallest leaf, append its neighbor to the "
            "sequence, delete the leaf. Decoding: given the sequence, the "
            "leaves are the labels missing from it; repeatedly take the "
            "smallest missing label, connect it to the next sequence "
            "entry, remove both. Both directions are deterministic and "
            "invert each other - a true bijection, so trees <-> sequences "
            "one-to-one, count n^{n-2}. Tree equivalences proof sketch: "
            "connected + n-1 edges -> acyclic (a cycle would let you drop "
            "an edge and stay connected, contradicting minimality); "
            "acyclic + connected -> unique paths. In practice: (1) to "
            "count labeled trees, use n^{n-2} or Prufer codes; "
            "(2) to count spanning trees of a general graph, use "
            "Kirchhoff's cofactor; (3) for unlabeled trees the count is "
            "harder (Otter's asymptotic) - labels matter enormously. "
            "Spanning-tree counts also give network reliability "
            "estimates."
        ),
        "key_points": [
            "Tree equivalences: connected + acyclic <-> n-1 edges <-> unique paths <-> every edge a bridge.",
            "Cayley's formula: n^{n-2} labeled trees on n vertices (n=4 -> 16).",
            "Prufer sequences biject trees with length-(n-2) strings over [n].",
            "Kirchhoff's matrix-tree theorem: Laplacian cofactors count spanning trees of any graph.",
            "Spanning trees backbone network design (Kruskal/Prim), phylogenetics, random graphs.",
        ],
        "requirements": [
            "Graph vocabulary; bijections.",
            "Matrix determinants at a basic level (for Kirchhoff's statement).",
        ],
        "standards": [
            "Prufer encode/decode shown to invert on a worked example.",
            "Labeled vs. unlabeled tree counts distinguished explicitly.",
        ],
        "citations": [C_BONDY, C_DIESTEL],
        "sig_lens": (
            "Signature edition: trees as his branching law - every Signature tree a "
            "minimal Signature connection, every labeled tree one of his n^{n-2}, "
            "encoded by his Prufer strings."
        ),
        "demo_kind": "comb_cayley",
    },
    {
        "key": "eulerian_hamiltonian",
        "name": "Eulerian Trails and Hamiltonian Cycles",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Two famous route problems, deceptively similar, worlds apart. "
            "An Eulerian trail uses every EDGE exactly once (the "
            "Konigsberg bridges: can you cross each bridge once?). Euler "
            "proved in 1736: a connected graph has an Eulerian circuit "
            "iff every vertex has even degree; an Eulerian trail (not "
            "closed) iff exactly 0 or 2 vertices have odd degree. "
            "Checking is trivial - just count degrees. A Hamiltonian "
            "cycle visits every VERTEX exactly once (the traveling "
            "salesman, the knight's tour). No efficient characterization "
            "exists: Hamiltonicity is NP-complete, and the best general "
            "guarantees are sufficient conditions (Dirac: minimum degree "
            ">= n/2 forces a Hamiltonian cycle; Ore: deg(u)+deg(v) >= n "
            "for nonadjacent u,v). Euler founded graph theory with a "
            "complete answer; Hamilton's problem, 120 years later, remains "
            "computationally hard - the contrast teaches that similar "
            "statements can have wildly different difficulty."
        ),
        "how_it_works": (
            "Eulerian direction: necessity - a circuit enters and leaves "
            "each vertex equally, so degrees are even. Sufficiency - "
            "Hierholzer's algorithm: start anywhere, follow unused edges "
            "until stuck (must be back at start, by even degrees); if "
            "edges remain, splice in a detour circuit from a visited "
            "vertex with unused edges; repeat. Fleury's algorithm (avoid "
            "bridges) also works. For trails with 2 odd vertices, start "
            "at one odd vertex. Hamiltonian direction: no polynomial "
            "test exists (NP-complete), so use sufficient conditions or "
            "backtracking search with pruning for small graphs. Dirac's "
            "proof idea: take a longest path; its endpoints' neighborhoods "
            "force a cycle covering the path; maximality extends it. In "
            "practice: (1) edges-once = check degrees (easy); (2) "
            "vertices-once = search or apply Dirac/Ore (hard); (3) never "
            "confuse the two - 'graphtheoretic false friends'. Route "
            "inspection (Chinese postman) builds on Eulerian trails; "
            "delivery routing builds on Hamiltonian cycles."
        ),
        "key_points": [
            "Eulerian circuit iff connected and all degrees even (1736); trail iff 0 or 2 odd degrees.",
            "Hierholzer's algorithm constructs Eulerian circuits by splicing detours.",
            "Hamiltonian cycle (vertices once) is NP-complete - no efficient test exists.",
            "Dirac (min degree >= n/2) and Ore (deg(u)+deg(v) >= n) are sufficient conditions.",
            "False friends: similar statements, wildly different difficulty - check degrees vs. search.",
        ],
        "requirements": [
            "Graph vocabulary; handshaking lemma.",
            "Basic complexity intuition (easy check vs. hard search).",
        ],
        "standards": [
            "Eulerian vs. Hamiltonian stated as edge-cover vs. vertex-cover before any analysis.",
            "Degree parity computed explicitly in Eulerian arguments.",
        ],
        "citations": [C_BONDY, C_DIESTEL],
        "sig_lens": (
            "Signature edition: Eulerian trails as his even-degree law - every "
            "Signature bridge crossed once by his parity rule; Hamiltonian cycles his "
            "hard Signature journeys, guaranteed only by his degree conditions."
        ),
        "demo_kind": "comb_euler_ham",
    },
    {
        "key": "ramsey_theory",
        "name": "Ramsey Theory: Order Forced from Chaos",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "In any gathering of 6 people, 3 are mutual acquaintances or 3 "
            "are mutual strangers - R(3,3) = 6. Ramsey theory: complete "
            "disorder is impossible; any sufficiently large structure "
            "contains an ordered substructure. The Ramsey number R(s,t) "
            "is the smallest n such that every red-blue coloring of K_n's "
            "edges contains a red K_s or a blue K_t. R(3,3)=6, R(3,4)=9, "
            "R(3,5)=14, R(4,4)=18, R(4,5)=25 - and R(5,5) is unknown "
            "(known: 43 to 48). Erdos quipped that if aliens demanded "
            "R(5,5) we'd assemble all mathematicians, but for R(6,6) "
            "we'd fight. The classic bound: R(s,t) <= C(s+t-2, s-1), "
            "proved by the recurrence R(s,t) <= R(s-1,t) + R(s,t-1) "
            "(pick a vertex; it has red-degree or blue-degree large "
            "enough to recurse). The probabilistic method gives "
            "R(s,s) > 2^{s/2} - random colorings avoid monochromatic "
            "K_s. Ramsey theory extends to hypergraphs, van der Waerden "
            "(monochromatic arithmetic progressions), and Hales-Jewett."
        ),
        "how_it_works": (
            "Upper bound proof: R(s,t) <= R(s-1,t) + R(s,t-1). Take "
            "n = R(s-1,t) + R(s,t-1) vertices, pick v; v has at least "
            "R(s-1,t) red neighbors or at least R(s,t-1) blue neighbors "
            "(pigeonhole). In the red neighborhood, induction gives a "
            "red K_{s-1} (add v: red K_s) or a blue K_t. Base cases "
            "R(s,2) = s. This yields R(s,t) <= C(s+t-2,s-1). For "
            "R(3,3) = 6: the bound gives <= 6; the 5-cycle 2-colored "
            "with no monochromatic triangle shows > 5. Lower bounds "
            "need explicit colorings (hard) or the probabilistic method "
            "(next rung's neighbor): a random coloring of K_n has "
            "expected monochromatic-K_s count C(n,s) 2^{1-C(s,2)}; if "
            "this is < 1, some coloring avoids them, so R(s,s) > n. "
            "In practice: small Ramsey numbers via case analysis and "
            "known tables; large ones via the recurrence upper bound "
            "and probabilistic lower bound."
        ),
        "key_points": [
            "R(3,3) = 6: any 6 people contain 3 mutual acquaintances or 3 mutual strangers.",
            "R(s,t) <= R(s-1,t) + R(s,t-1) -> R(s,t) <= C(s+t-2, s-1).",
            "R(4,4) = 18, R(4,5) = 25; R(5,5) unknown (43-48).",
            "Lower bounds via explicit colorings (5-cycle for R(3,3)) or the probabilistic method.",
            "Extends to van der Waerden, Hales-Jewett: unavoidable patterns everywhere.",
        ],
        "requirements": [
            "Pigeonhole principle; binomial coefficients; induction.",
            "Graph coloring vocabulary.",
        ],
        "standards": [
            "The recurrence's pigeonhole step (red-degree vs. blue-degree) shown explicitly.",
            "Lower-bound colorings exhibited, not merely claimed.",
        ],
        "citations": [C_VANLINT, C_ALON],
        "sig_lens": (
            "Signature edition: Ramsey theory as his order-from-chaos law - every "
            "large enough Signature coloring forced to contain his ordered Signature "
            "substructure."
        ),
        "demo_kind": "comb_ramsey",
    },
    {
        "key": "block_designs_fano",
        "name": "Block Designs and the Fano Plane",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "A balanced incomplete block design BIBD(v,b,r,k,lambda) is "
            "v points arranged in b blocks of size k, each point in r "
            "blocks, each pair of points together in exactly lambda "
            "blocks. The Fano plane - the (7,7,3,3,1) design - is the "
            "icon: 7 points, 7 lines (one 'circle'), each line 3 "
            "points, each pair on exactly one line. Necessary conditions: "
            "bk = vr (count point-block incidences) and r(k-1) = "
            "lambda(v-1) (fix a point, count pairs with it two ways) - "
            "Fisher's inequality adds b >= v. Symmetric designs "
            "(b = v) include projective planes: a projective plane of "
            "order q has q^2+q+1 points, the Fano plane being order 2. "
            "Designs run experiments (each treatment pair compared "
            "equally often), build error-correcting codes, schedule "
            "tournaments (Kirkman's schoolgirl problem: 15 girls walk in "
            "triples for 7 days, every pair together once - the "
            "Kirkman/Steiner triple system), and underlie finite "
            "geometry."
        ),
        "how_it_works": (
            "Verify a design by the counting equations: for the Fano "
            "plane, bk = 7*3 = 21 = 7*3 = vr; r(k-1) = 3*2 = 6 = "
            "1*6 = lambda(v-1). Construct the Fano plane on points "
            "{0,...,6} with lines {i, i+1, i+3} mod 7 (the difference "
            "set {0,1,3}: every nonzero difference mod 7 appears exactly "
            "once as a difference of set elements - that is why each "
            "pair shares exactly one line). Difference sets generalize: "
            "a (v,k,lambda) difference set in a group yields a symmetric "
            "BIBD. To test parameters for feasibility: (1) check bk = vr "
            "and r(k-1) = lambda(v-1) give integers; (2) check Fisher "
            "b >= v; (3) for symmetric designs, Bruck-Ryser-Chowla "
            "restricts v. Existence is harder - Steiner triple systems "
            "exist iff v = 1 or 3 mod 6 (Kirkman, 1847). In practice: "
            "small designs by difference sets or cyclic shifts; "
            "tournaments and experiments read off the blocks."
        ),
        "key_points": [
            "BIBD(v,b,r,k,lambda): v points, b k-blocks, each point in r blocks, each pair in lambda blocks.",
            "Fano plane (7,7,3,3,1): 7 points, 7 lines, each pair on exactly one line.",
            "Necessary: bk = vr, r(k-1) = lambda(v-1), Fisher b >= v.",
            "Difference sets ({0,1,3} mod 7) construct symmetric designs via cyclic shifts.",
            "Applications: experimental design, codes, tournament scheduling (Kirkman's schoolgirls).",
        ],
        "requirements": [
            "Double counting; modular arithmetic basics.",
            "Set systems vocabulary.",
        ],
        "standards": [
            "All five parameters stated; counting equations verified numerically.",
            "Difference-set differences listed to confirm lambda = 1.",
        ],
        "citations": [C_VANLINT, C_BRUALDI],
        "sig_lens": (
            "Signature edition: block designs as his balanced law - every Signature "
            "pair of points sharing exactly his lambda blocks, the Fano plane his "
            "seven-point Signature icon."
        ),
        "demo_kind": "comb_designs",
    },
    {
        "key": "latin_squares",
        "name": "Latin Squares and Orthogonal Arrays",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "A Latin square of order n is an n-by-n grid filled with n "
            "symbols, each appearing once per row and column - completed "
            "Sudoku grids are Latin squares with extra box constraints. "
            "Two Latin squares are orthogonal if overlaying them shows "
            "every ordered pair exactly once - the Graeco-Latin square. "
            "Euler's 36 officers problem (1782): can 6 regiments x 6 "
            "ranks form a 6x6 Graeco-Latin square? Euler conjectured no "
            "for n = 2 mod 4; Tarry proved n=6 impossible (1900), but "
            "Euler was wrong in general - Parker, Bose, and Shrikhande "
            "found order-10 orthogonal pairs in 1959. A set of k mutually "
            "orthogonal Latin squares (MOLS) of order n is equivalent to "
            "an orthogonal array OA(k+2, n), and k = n-1 MOLS exist iff "
            "a projective plane of order n exists - designs, squares, "
            "and planes are one theory. Latin squares schedule "
            "tournaments, design agricultural experiments (rows/columns "
            "block two nuisance factors), and build error-correcting "
            "codes."
        ),
        "how_it_works": (
            "Construct MOLS from finite fields: for prime power q, the "
            "addition and multiplication tables give q-1 MOLS of order q "
            "(square (i,j) -> a*i + b*j for each nonzero slope (a,b) up "
            "to scale). Verify orthogonality by checking all n^2 pairs "
            "appear - for order 3, the pair (cyclic shifts) works: "
            "overlay and confirm 9 distinct pairs. Count Latin squares: "
            "order 3 has 12, order 4 has 576, order 11 has ~10^47 - "
            "exact counts are hard (only through n=11 known). To test a "
            "square: each row and column must be a permutation of the "
            "symbols. For experimental design: treatments in cells, rows "
            "and columns as blocks, each treatment once per block - the "
            "Latin square controls two blocking factors at once. "
            "Orthogonal arrays OA(t,k,v) generalize: every t columns "
            "contain every t-tuple equally often."
        ),
        "key_points": [
            "Latin square: n symbols, each once per row and column; Sudoku is a constrained case.",
            "Orthogonal pair: overlay shows all n^2 ordered pairs - Graeco-Latin squares.",
            "Euler's 36 officers: no pair for n=6 (Tarry 1900), but pairs exist for n=10 (disproving Euler's conjecture).",
            "Finite fields give n-1 MOLS for prime-power n; n-1 MOLS <-> projective plane of order n.",
            "Applications: tournament schedules, agricultural experiments, codes, orthogonal arrays.",
        ],
        "requirements": [
            "Permutations; modular arithmetic (for finite-field constructions).",
            "Block design basics (for the MOLS-plane equivalence).",
        ],
        "standards": [
            "Row/column permutation property verified explicitly for exhibited squares.",
            "Orthogonality verified by listing all n^2 overlay pairs.",
        ],
        "citations": [C_VANLINT, C_BRUALDI],
        "sig_lens": (
            "Signature edition: Latin squares as his grid law - every Signature symbol "
            "once per row and column, orthogonal pairs his overlaid Signature "
            "patterns showing every combination."
        ),
        "demo_kind": "comb_latin",
    },
    {
        "key": "combinatorial_games",
        "name": "Combinatorial Games: Winning Strategies",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Combinatorial game theory studies perfect-information, "
            "no-chance, two-player games: Nim, Dawson's Kayles, Treblecross, "
            "poset games. The foundation: positions are P-positions "
            "(previous player wins - losing for the player about to move) "
            "or N-positions (next player wins). Nim's solution (Bouton, "
            "1901): xor the heap sizes; xor 0 = P-position, nonzero = "
            "N-position, and the winning move makes the xor 0. The "
            "Sprague-Grundy theorem: every impartial game (same moves for "
            "both players) equals a Nim heap of size equal to its Grundy "
            "number (mex of options' Grundy numbers), and a disjunctive "
            "sum of games is losing iff the xor of Grundy numbers is 0. "
            "Partizan games (different moves per player - chess, Go) need "
            "Conway's richer theory of numbers and games ('Winning Ways', "
            "'On Numbers and Games'). Strategy stealing proves the first "
            "player never loses symmetric Maker-Maker games. Game values "
            "compute via DP on the game graph - small games exactly, large "
            "ones via theory."
        ),
        "how_it_works": (
            "Analyze an impartial game: (1) list positions; (2) compute "
            "Grundy numbers bottom-up: g(P) = mex{g(options)} (mex = "
            "minimum excluded nonnegative integer); terminal positions "
            "have g = 0; (3) for a sum of components, xor the Grundy "
            "numbers - 0 means the player to move loses with perfect "
            "play; (4) the winning move: move in one component to make "
            "the total xor 0. Nim example: heaps (3,5,7): 3 xor 5 xor 7 "
            "= 1 (nonzero, N-position); reduce the 7-heap to 6 (3 xor 5 "
            "xor 6 = 0). Dawson's Kayles (bowl a pin, neighbors vanish): "
            "Grundy numbers are periodic after a point - compute far "
            "enough and the pattern repeats. For partizan games, the "
            "theory assigns game values (numbers, switches, infinitesimals) "
            "with a partial order. In practice: small impartial games by "
            "Grundy DP; Nim-heap equivalence to split sums; strategy "
            "stealing for symmetric strong games."
        ),
        "key_points": [
            "P-positions (previous player wins) vs. N-positions (next player wins) - computed bottom-up.",
            "Nim: xor of heaps; zero = losing; winning move zeroes the xor (Bouton 1901).",
            "Sprague-Grundy: every impartial game = a Nim heap; sums decided by xor of Grundy numbers.",
            "Grundy via mex of options; Dawson's Kayles shows eventual periodicity.",
            "Partizan games (chess, Go) need Conway's full theory of game values.",
        ],
        "requirements": [
            "Recursion/induction; xor (binary) arithmetic.",
            "Comfort with game trees and optimal-play reasoning.",
        ],
        "standards": [
            "P/N or Grundy labels computed for all positions in worked examples, not asserted.",
            "Winning moves verified by showing the resulting xor is 0.",
        ],
        "citations": [C_BERLEKAMP, C_VANLINT],
        "sig_lens": (
            "Signature edition: combinatorial games as his strategy law - every "
            "Signature position a P or an N, every winning move his xor brought to "
            "zero."
        ),
        "demo_kind": "comb_games",
    },
    {
        "key": "extremal_turan",
        "name": "Extremal Combinatorics: Turan's Theorem",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "How many edges can an n-vertex graph have without containing "
            "a triangle? Mantel (1907) answered: at most floor(n^2/4), "
            "achieved by the complete bipartite graph K_{floor(n/2), "
            "ceil(n/2)}. Turan (1941) generalized: the most edges in an "
            "n-vertex graph with no (r+1)-clique is achieved by the Turan "
            "graph T(n,r) - the complete r-partite graph with parts as "
            "equal as possible - with (1 - 1/r) n^2/2 edges. This founded "
            "extremal graph theory: the extremal number ex(n, F) is the "
            "max edges without containing F. Mantel's proof: pick an "
            "edge uv; every other vertex connects to at most one of u,v "
            "(else a triangle); count edges <= ... The method - bound "
            "via a structural observation about the extremal object - is "
            "the template of extremal proofs. Modern extremal "
            "combinatorics spans the Erdos-Stone theorem (chromatic "
            "number governs ex(n,F) asymptotically), the probabilistic "
            "lower bounds, and flag algebras (Razborov) for exact "
            "results."
        ),
        "how_it_works": (
            "Mantel's proof: let G be triangle-free with max edges; take "
            "an edge uv. Any vertex w adjacent to both u and v makes "
            "triangle uvw - forbidden - so each other vertex touches at "
            "most one of {u,v}: deg(u) + deg(v) <= n. Sum over all edges "
            "uv: sum_{uv in E} (deg(u)+deg(v)) = sum_v deg(v)^2 <= "
            "n|E|... then Cauchy-Schwarz (sum deg)^2 <= n sum deg^2 gives "
            "(2|E|)^2 <= n * n|E|, i.e., |E| <= n^2/4. Equality needs "
            "regular bipartite - K_{n/2,n/2}. Turan's proof uses "
            "induction or Zykov symmetrization (replace a vertex's "
            "neighborhood by another's to increase edges without "
            "creating cliques, converging to complete multipartite). In "
            "practice: (1) guess the extremal construction (balanced "
            "complete multipartite); (2) prove no graph beats it via "
            "degree-sum or symmetrization; (3) check equality cases. "
            "Extremal thinking - 'what is the most X can do while "
            "avoiding Y' - applies to sets (Erdos-Ko-Rado), sequences "
            "(Erdos-Szekeres), and hypergraphs."
        ),
        "key_points": [
            "Mantel: triangle-free n-vertex graph has <= floor(n^2/4) edges (K_{n/2,n/2} attains it).",
            "Turan: no (r+1)-clique -> <= (1-1/r)n^2/2 edges; Turan graph T(n,r) is extremal.",
            "Proof template: structural observation about the extremal object (degree sums, symmetrization).",
            "ex(n,F): the extremal number - max edges avoiding F; Erdos-Stone gives asymptotics via chromatic number.",
            "Extremal thinking generalizes: sets (Erdos-Ko-Rado), sequences (Erdos-Szekeres), hypergraphs.",
        ],
        "requirements": [
            "Graph vocabulary; Cauchy-Schwarz or convexity intuition.",
            "Induction.",
        ],
        "standards": [
            "The extremal construction exhibited and its edge count computed.",
            "Upper-bound proof's key inequality derived step by step.",
        ],
        "citations": [C_JUKNA, C_BONDY],
        "sig_lens": (
            "Signature edition: extremal combinatorics as his maximum law - the most "
            "Signature edges without his forbidden pattern, attained by his balanced "
            "Turan graphs."
        ),
        "demo_kind": "comb_turan",
    },
    {
        "key": "probabilistic_method",
        "name": "The Probabilistic Method: Proving by Random Choice",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "To prove an object with property P exists, pick a random "
            "object and show P holds with positive probability - then "
            "such an object MUST exist. Erdos's 1947 lower bound for "
            "Ramsey numbers: 2-color K_n's edges uniformly at random; "
            "for a fixed s-set, P(monochromatic) = 2^{1-C(s,2)}; union "
            "bound over C(n,s) sets: if C(n,s) 2^{1-C(s,2)} < 1, some "
            "coloring has no monochromatic K_s, so R(s,s) > n - giving "
            "R(s,s) > 2^{s/2}. The method is non-constructive: it proves "
            "existence without exhibiting the object. Refinements: the "
            "alteration method (random object, then fix defects), the "
            "Lovasz Local Lemma (rare bad events, each depending on few "
            "others, can all be avoided), expectation arguments (a random "
            "tournament has a Hamiltonian path - every ordering's "
            "'forward edges' count averages (n-1)/2, so some ordering "
            "achieves it... the precise argument uses linearity). The "
            "probabilistic method, systematized by Erdos and in Alon-"
            "Spencer's text, is now central to combinatorics, theoretical "
            "computer science, and random graph theory."
        ),
        "how_it_works": (
            "The basic template: (1) define a probability space of "
            "candidate objects; (2) for each 'bad' event E_i, bound "
            "P(E_i); (3) union bound: P(any bad) <= sum P(E_i); (4) if "
            "the sum < 1, P(no bad) > 0, so a good object exists. "
            "Ramsey: candidates = 2-colorings of K_n; bad events = "
            "'S is monochromatic' for each s-set S; P = 2^{1-C(s,2)}; "
            "sum = C(n,s)2^{1-C(s,2)} < 1 when n ~ 2^{s/2}. Alteration "
            "example - large independent set: random vertex subset "
            "keeping each vertex with probability p; delete one endpoint "
            "of each surviving edge; expected survivors >= np - mp^2, "
            "optimized at p = n/2m, giving alpha(G) >= n^2/4m (Turán-type "
            "bound). Lovasz Local Lemma: if each bad event has "
            "probability <= p and depends on <= d others with "
            "ep(d+1) <= 1, all are avoidable - used for hypergraph "
            "2-coloring and satisfiability. In practice: randomness "
            "proves existence; derandomization (conditional "
            "expectations) can then construct."
        ),
        "key_points": [
            "Existence via positive probability: random object + P(good) > 0 => good object exists.",
            "Erdos 1947: R(s,s) > 2^{s/2} via random 2-colorings and the union bound.",
            "Non-constructive: proves existence without exhibiting the object.",
            "Alteration: randomize, then fix defects (independent sets, Turan-type bounds).",
            "Lovasz Local Lemma: rare, locally-dependent bad events can all be avoided simultaneously.",
        ],
        "requirements": [
            "Basic probability (events, union bound, expectation, linearity).",
            "Ramsey numbers (for the flagship application).",
        ],
        "standards": [
            "Probability space and bad events defined explicitly; union bound computed numerically.",
            "Non-constructive nature flagged - no explicit object claimed.",
        ],
        "citations": [C_ALON, C_VANLINT],
        "sig_lens": (
            "Signature edition: the probabilistic method as his existence law - a "
            "Signature object proved real because his random choice lands on it with "
            "positive probability."
        ),
        "demo_kind": "comb_prob_method",
    },
    {
        "key": "polya_enumeration",
        "name": "Polya Enumeration: Counting Up to Symmetry",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "How many different necklaces with n beads and k colors, "
            "counting rotations as the same? Burnside's lemma: the "
            "number of orbits = (1/|G|) sum_{g in G} Fix(g), where Fix(g) "
            "counts colorings fixed by symmetry g. For necklaces under "
            "rotation: (1/n) sum_{d|n} phi(d) k^{n/d} - a rotation by "
            "n/d steps has d cycles, each monochromatic: k^d colorings "
            "fixed... precisely phi(n/d) rotations share each cycle "
            "type. Example: 4 beads, 2 colors: (2^4 + 2^1 + 2^2 + 2^1)/4 "
            "= 24/4 = 6 necklaces. Polya's enumeration theorem refines "
            "this with the cycle index: substitute the figure inventory "
            "(x_1 + ... + x_k) into Z(G) to count by color multiplicities. "
            "For the cube's faces with 2 colors: 10 distinct colorings. "
            "Applications: counting isomers in chemistry (Polya's "
            "original motivation), distinct dice labelings, unlabeled "
            "graphs (via the pair group), and any 'up to symmetry' "
            "count. The prerequisite is group actions - permutations "
            "acting on the objects - making this the capstone where "
            "algebra meets enumeration."
        ),
        "how_it_works": (
            "Burnside's proof by double counting: count pairs (g, x) "
            "with g(x) = x two ways - by group element (sum Fix(g)) and "
            "by object (each orbit of size |G|/|Stab| contributes "
            "|G| pairs, so total = |X|... the orbit-stabilizer theorem "
            "gives pairs = sum_orbits |G| = |orbits| * |G|). Hence "
            "orbits = (1/|G|) sum Fix(g). For necklaces: rotation by j "
            "positions decomposes beads into gcd(n,j) cycles; fixed "
            "colorings = k^{gcd(n,j)}; summing and grouping by d = "
            "gcd(n,j) (phi(n/d) rotations per d) gives the formula. "
            "Polya's cycle index Z(G) = (1/|G|) sum_g z_1^{c_1(g)} "
            "z_2^{c_2(g)} ...; substituting z_i = x_1^i + ... + x_k^i "
            "gives the pattern inventory. In practice: (1) identify the "
            "symmetry group and its action; (2) find each group "
            "element's cycle structure on the positions; (3) apply "
            "Burnside or the cycle index; (4) verify small cases by "
            "brute force - symmetry counts are error-prone."
        ),
        "key_points": [
            "Burnside's lemma: orbits = (1/|G|) sum Fix(g) - average fixed colorings over symmetries.",
            "Necklaces: (1/n) sum_{d|n} phi(d) k^{n/d}; 4 beads, 2 colors -> 6.",
            "Cycle index Z(G) + figure inventory = pattern inventory (Polya's theorem).",
            "Cube faces, 2 colors: 10 distinct colorings.",
            "Chemistry isomers (Polya's motivation), dice, unlabeled graphs via the pair group.",
        ],
        "requirements": [
            "Permutations as group actions; cycle decomposition; Euler's totient.",
            "Double counting.",
        ],
        "standards": [
            "Group, action, and cycle structure of each symmetry stated explicitly.",
            "Small cases verified by brute-force orbit enumeration.",
        ],
        "citations": [C_VANLINT, C_STANLEY],
        "sig_lens": (
            "Signature edition: Polya enumeration as his symmetry law - Signature "
            "colorings counted up to his symmetries, every orbit his average of "
            "fixed colorings."
        ),
        "demo_kind": "comb_polya",
    },
    {
        "key": "algebraic_combinatorics_symmetric",
        "name": "Algebraic Combinatorics: Symmetric Functions",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Algebraic combinatorics studies the algebraic structures "
            "behind counting. The symmetric functions - polynomials "
            "unchanged by permuting variables - form its heart. The "
            "elementary symmetric functions e_k = sum of all products of "
            "k distinct variables (e_2(x_1,x_2,x_3) = x_1x_2 + x_1x_3 + "
            "x_2x_3); the complete homogeneous h_k (all monomials of "
            "degree k); the power sums p_k = sum x_i^k. Newton's "
            "identities relate them: ke_k = sum_{i=1}^{k} (-1)^{i-1} "
            "e_{k-i} p_i. The fundamental theorem: every symmetric "
            "polynomial is uniquely a polynomial in the e_k - which is "
            "why Vieta's formulas work (coefficients of a polynomial are, "
            "up to sign, the e_k of its roots). The Schur functions, "
            "indexed by partitions, are the characters of the symmetric "
            "group's representations - representation theory made "
            "combinatorial. RSK correspondence bijects permutations with "
            "pairs of standard Young tableaux, proving sum (f^lambda)^2 "
            "= n!. This rung closes the ladder: counting, at its "
            "deepest, is algebra."
        ),
        "how_it_works": (
            "Work with symmetric functions via the bases: to express a "
            "symmetric polynomial in e_k, use Newton's identities "
            "recursively or the generating function product_i (1 + x_i t) "
            "= sum e_k t^k. Example: x_1^2 + x_2^2 + x_3^2 = p_2 = "
            "e_1^2 - 2e_2 (from 2e_2 = e_1 p_1 - p_2 with p_1 = e_1). "
            "Verify numerically on random values. The power-sum basis "
            "connects to cycle structure: p_k evaluated at roots of "
            "unity counts fixed points of permutations. RSK: insert a "
            "permutation's values into tableaux by row-bumping; the "
            "recording tableau tracks positions - the bijection proves "
            "the sum-of-squares identity and the hook-length formula "
            "counts tableaux. In practice: (1) recognize symmetry in the "
            "problem (sums over all permutations, all subsets); "
            "(2) translate to the e/h/p basis; (3) use Newton's "
            "identities or generating functions to convert; (4) read off "
            "the combinatorial meaning (Vieta, characters, tableaux)."
        ),
        "key_points": [
            "Symmetric functions: e_k (elementary), h_k (complete homogeneous), p_k (power sums).",
            "Newton's identities convert between bases: ke_k = sum (-1)^{i-1} e_{k-i} p_i.",
            "Fundamental theorem: every symmetric polynomial is uniquely a polynomial in the e_k (Vieta).",
            "Schur functions = irreducible characters of the symmetric group.",
            "RSK bijection: permutations <-> tableau pairs; sum (f^lambda)^2 = n!.",
        ],
        "requirements": [
            "Polynomial algebra; partitions (Ferrers diagrams).",
            "Generating functions; basic representation intuition (helpful, not required).",
        ],
        "standards": [
            "Basis conversions shown via Newton's identities step by step.",
            "Symmetric-function identities verified numerically on random values.",
        ],
        "citations": [C_STANLEY, C_VANLINT],
        "sig_lens": (
            "Signature edition: symmetric functions as his deepest algebra - every "
            "Signature polynomial symmetric under his permutations expressed in his "
            "elementary basis, counting revealed as algebra at the top of the ladder."
        ),
        "demo_kind": "comb_symmetric",
    },
]
