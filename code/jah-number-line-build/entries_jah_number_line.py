#!/usr/bin/env python3
"""Entries for the JAH Signature Number Line databases (Manon order #13,
2026-10-17 15:32 EDT).

RAW SWEEP over the full manifest (2,390 databases): zero 'jah-number-line*'
slugs/names; zero 'number line' / 'numberline' hits in any name, slug, or
tagline. The one keyword near-hit, the Natural Language Processing pair
(natural-language-public-ai / natural-language-signature-ai, JAH-NLP-PUB /
JAH-NLP-SIG), is about language AI, not the mathematical number line - it
has no number-line records, no intervals, no coordinate mapping. The
paste's rule was applied by name/purpose/record schema/capabilities: a
ladder-ordered archive of number-line records - integers, rationals, reals,
intervals, inequalities, absolute value, coordinate mapping - is a distinct
capability - BUILD NEW is the verdict.

So this build creates two NEW databases, 34 ladder-ordered records each:

  jah-number-line               - The JAH Signature Number Line Database
                                  (public-harvest: real, fact-checked
                                  mathematics of the number line - counting
                                  numbers, zero, negatives, integers,
                                  ordering, addition and subtraction as
                                  steps, fractions, decimals, rational
                                  numbers, absolute value, intervals,
                                  inequalities, midpoints, multiplication
                                  and division as scaling, square roots, the
                                  coordinate axis, estimation, irrational
                                  numbers, the completeness of the reals,
                                  interval arithmetic, the Cartesian plane,
                                  measurement, limits, functions, infinite
                                  intervals, continuity; standard references
                                  Euclid Elements Book VII; Dedekind
                                  Stetigkeit und irrationale Zahlen 1872;
                                  CCSS number-line standards; NCTM
                                  Principles to Actions 2014; ISO 80000-2;
                                  Rudin Principles of Mathematical Analysis;
                                  Apostol Calculus; Stewart Calculus; Devlin
                                  The Language of Mathematics)
  jah-number-line-signature     - The JAH Signature Number Line Signature
                                  Database
                                  (his original Signature Number Line
                                  Method: the line as a sworn order of
                                  values - every position a value sealed at
                                  its post, zero the signet of the origin,
                                  order the covenant of less and greater,
                                  the arrow the oath that the order
                                  continues; src signature, titles suffixed
                                  " (Signature Edition)", never presented
                                  as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-NLN- (public) and JAH-NLNS- (signature), verified free in
the manifest id_prefix values and in every shard index file (zero hits;
JAH-NLP-PUB / JAH-NLP-SIG belong to the unrelated Natural Language
Processing databases, so the NLN form was chosen to avoid even substring
ambiguity).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_jah_number_line.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos before the fragment
is written.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature Number Line "
            "Method: the line as a sworn order of values, every position a "
            "value sealed at its post, zero the signet of the origin, order "
            "the covenant of less and greater, the arrow the oath that the "
            "order continues. Clearly labeled Signature-made, never "
            "presented as authentic public record.")

CIT_EUCLID = ("Euclid. Elements. Book VII (arithmetic of numbers); c. 300 "
              "BCE.")
CIT_DEDEKIND = ("Dedekind R. Stetigkeit und irrationale Zahlen (Continuity "
                "and Irrational Numbers); 1872.")
CIT_CCSS = ("Common Core State Standards for Mathematics. National "
            "Governors Association; 2010.")
CIT_NCTM = ("National Council of Teachers of Mathematics. Principles to "
            "Actions: Ensuring Mathematical Success for All; 2014.")
CIT_ISO80000 = ("ISO 80000-2:2019. Quantities and units - Part 2: "
                "Mathematical signs and symbols to be used in the natural "
                "sciences and technology.")
CIT_RUDIN = ("Rudin W. Principles of Mathematical Analysis. 3rd ed. "
             "McGraw-Hill; 1976.")
CIT_APOSTOL = ("Apostol TM. Calculus, Vol. 1: One-Variable Calculus. 2nd "
               "ed. Wiley; 1967.")
CIT_STEWART = ("Stewart J. Calculus. 8th ed. Cengage; 2016.")
CIT_DEVLIN = ("Devlin K. The Language of Mathematics: Making the Invisible "
              "Visible. Free Press; 2000.")

ENTRIES = [
    # ------------------------------------------------------- FOUNDATIONS
    {
        "key": "nl_counting",
        "name": "The Counting Numbers on the Line",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": ("The number line begins with counting: 1, 2, 3, 4, "
                        "and onward, each number sealed at its own mark, "
                        "evenly spaced like fence posts. Take a straight "
                        "line, choose a starting mark, and lay off equal "
                        "steps to the right - the first mark is 1, the next "
                        "is 2, and every further step adds one more. This "
                        "picture turns counting into geometry: bigger "
                        "numbers sit farther to the right, and the gap "
                        "between any two neighbors is always exactly one. "
                        "Euclid treated numbers in his Elements as built "
                        "from the unit by repetition, and the counting line "
                        "is that idea made visible - every natural number "
                        "gets one and only one address on the line. Once "
                        "the marks are laid, the line can answer questions "
                        "by itself: which of 7 and 9 is larger, how far "
                        "apart are 4 and 6, what comes right after 12. This "
                        "record is the first rung of the ladder: the line "
                        "as a map of counting."),
        "how_it_works": ("Draw a horizontal line and pick a point for the "
                         "start. Choose a step length - any fixed length - "
                         "and mark off equal steps to the right, labeling "
                         "them 1, 2, 3, 4, and so on. The number attached "
                         "to a mark counts how many steps it stands from "
                         "the start, so the n-th mark is the number n. "
                         "Equal steps mean equal differences: moving from "
                         "mark 5 to mark 8 always crosses 3 steps, whatever "
                         "the step length, because 8 - 5 = 3. A longer "
                         "count just extends the line further right; the "
                         "pattern never changes."),
        "key_points": [
            "Counting numbers 1, 2, 3, ... are laid as equally spaced marks to the right.",
            "The n-th mark from the start is the number n.",
            "Equal spacing means the gap between neighbors is always 1.",
            "Rightward position encodes size: further right means larger.",
            "Every counting number has exactly one address on the line.",
        ],
        "requirements": [
            "A straight edge for drawing the line.",
            "A fixed step length for even spacing.",
            "Labels 1, 2, 3, ... placed under their marks.",
        ],
        "standards": [
            "CCSS.MATH.CONTENT.K.CC.A.1 - count to 100 by ones.",
            "NCTM Principles to Actions - number and operations foundations.",
            "ISO 80000-2:2019 - symbols for the set of natural numbers.",
        ],
        "citations": [CIT_EUCLID, CIT_CCSS, CIT_NCTM],
        "sig_lens": ("His Signature reading: counting is the first swearing "
                     "of the line - each mark a value taking its sworn "
                     "post, one step apart, in unbreakable order. The "
                     "counting line is the Signature roll call: 1 answers, "
                     "then 2, then 3, each standing exactly where it "
                     "belongs, none ahead of its turn."),
    },
    {
        "key": "nl_zero",
        "name": "Zero and the Origin",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": ("Zero is the anchor of the number line: the origin, "
                        "the mark from which every position is measured. "
                        "Place 0 one step to the left of 1 and the whole "
                        "line gains a reference point - 3 is three steps to "
                        "the right of 0, and every distance is counted from "
                        "this seal. Zero is not nothing here; it is the "
                        "fixed witness that gives every other number its "
                        "address. On a thermometer, 0 degrees splits the "
                        "scale; on a ruler laid from its end, 0 is where "
                        "measuring begins. Mathematically, 0 is the "
                        "additive identity: adding 0 changes nothing "
                        "(n + 0 = n), and it is the balance point of the "
                        "line - the place where rightward counting starts "
                        "and, as later records show, leftward counting "
                        "continues. Every coordinate system in mathematics "
                        "borrows this idea: one chosen point, called the "
                        "origin, from which all positions are reckoned."),
        "how_it_works": ("Mark a point and label it 0 - this is the "
                         "origin. Lay the counting marks 1, 2, 3, ... one "
                         "step each to the right of it. Now any mark's "
                         "number equals its step-count from 0, and the "
                         "distance between any two marks equals the "
                         "difference of their numbers. Check the identity "
                         "property: start at 4, add 0 steps, and you stand "
                         "at 4 - zero steps move nothing. On a vertical "
                         "line the same origin works, with counting running "
                         "upward instead of rightward."),
        "key_points": [
            "Zero is the origin: the reference mark all positions are measured from.",
            "0 is the additive identity: n + 0 = n for every n.",
            "The number on a mark equals its step-count from 0.",
            "Distance between two marks equals the difference of their numbers.",
            "The origin idea extends to every coordinate system.",
        ],
        "requirements": [
            "A clearly marked 0 point before the counting marks begin.",
            "Equal step spacing carried through the origin.",
        ],
        "standards": [
            "CCSS.MATH.CONTENT.K.CC.A.2 - count forward from a given number.",
            "ISO 80000-2:2019 - symbol 0 and the additive identity.",
        ],
        "citations": [CIT_EUCLID, CIT_CCSS, CIT_ISO80000],
        "sig_lens": ("His Signature reading: zero is the signet of the "
                     "line - the seal pressed at the center from which "
                     "every position is witnessed and measured. In the "
                     "Signature method nothing floats unanchored: 0 is the "
                     "fixed witness, and every number takes its stand by "
                     "counted steps from the seal."),
    },
    {
        "key": "nl_negative",
        "name": "Negative Numbers and Direction",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": ("The line does not stop at zero - it continues to "
                        "the left with the negative numbers: -1, -2, -3, "
                        "and onward. If rightward steps mean more, then "
                        "leftward steps mean less than nothing: a "
                        "temperature of -5 degrees is 5 degrees below "
                        "zero, and a bank balance of -20 dollars is a debt "
                        "of 20 dollars. Each negative number is the mirror "
                        "of a counting number across the origin: -3 sits "
                        "three steps left of 0, exactly as far as 3 sits "
                        "to the right. The minus sign is a direction flag, "
                        "not a subtraction command - it points left. With "
                        "negatives aboard, the line becomes a two-way "
                        "street: motion rightward increases value, motion "
                        "leftward decreases it, and any quantity with an "
                        "opposite - heat and cold, credit and debt, up and "
                        "down - can be placed on the line."),
        "how_it_works": ("From the origin, lay off the same equal steps to "
                         "the left, labeling them -1, -2, -3, and so on. "
                         "The number -n sits n steps left of 0, mirroring "
                         "the counting number n. Walk the line to add and "
                         "subtract: starting at 5 and taking 8 steps left "
                         "lands on -3, which is exactly what 5 - 8 means. "
                         "Check direction sense with a thermometer: -5 is "
                         "colder than -2 because it lies further left, "
                         "further from zero in the cold direction."),
        "key_points": [
            "Negative numbers extend the line left of zero: -1, -2, -3, ...",
            "-n sits n steps left of 0, mirroring n to the right.",
            "The minus sign marks direction (left), not an operation.",
            "Rightward motion increases value; leftward motion decreases it.",
            "Opposite quantities (hot/cold, credit/debt) map onto the two directions.",
        ],
        "requirements": [
            "The origin marked so left and right directions are unambiguous.",
            "Real examples: thermometer, elevation, debt.",
        ],
        "standards": [
            "CCSS.MATH.CONTENT.6.NS.C.5 - positive and negative numbers in real contexts.",
            "CCSS.MATH.CONTENT.6.NS.C.6a - opposites on the number line.",
        ],
        "citations": [CIT_CCSS, CIT_NCTM, CIT_APOSTOL],
        "sig_lens": ("His Signature reading: the negative side is the "
                     "line keeping its oath in both directions - what the "
                     "right hand builds, the left hand mirrors. Every "
                     "value has its sworn opposite across the signet of "
                     "zero, standing guard at equal distance on the far "
                     "side."),
    },
    {
        "key": "nl_integers",
        "name": "The Integers on the Line",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": ("Put the counting numbers, zero, and the negatives "
                        "together and you have the integers: ..., -3, -2, "
                        "-1, 0, 1, 2, 3, ... - the whole-number citizens of "
                        "the line, spaced one step apart forever in both "
                        "directions. The integers are the first complete "
                        "number system on the line: add or subtract any two "
                        "integers and the answer is another integer, a "
                        "property mathematicians call closure. Between any "
                        "two consecutive integers there is no other "
                        "integer - 4 and 5 are neighbors with nobody "
                        "between - which makes the integers a ladder of "
                        "separate rungs rather than a continuous rail. This "
                        "record names the full integer line: the discrete "
                        "backbone on which fractions, decimals, and "
                        "everything later will be hung."),
        "how_it_works": ("Extend the marked line in both directions: "
                         "negatives to the left, zero at the origin, "
                         "counting numbers to the right, every mark one "
                         "step from its neighbors. Test closure: pick any "
                         "two integer marks, add or subtract, and land on "
                         "another integer mark - for example (-4) + 9 = 5. "
                         "Test discreteness: try to find an integer strictly "
                         "between 6 and 7 and find none - consecutive "
                         "integers are always exactly 1 apart with nothing "
                         "between."),
        "key_points": [
            "The integers are ..., -3, -2, -1, 0, 1, 2, 3, ... - whole numbers both directions.",
            "Integers are closed under addition and subtraction.",
            "Consecutive integers are 1 apart with no integer between them.",
            "The integers form the discrete backbone of the number line.",
        ],
        "requirements": [
            "Both directions of the line drawn past zero.",
            "Neighbor pairs checked for the one-step gap.",
        ],
        "standards": [
            "CCSS.MATH.CONTENT.6.NS.C.6 - rational numbers as points on the number line.",
            "ISO 80000-2:2019 - symbol Z for the set of integers.",
        ],
        "citations": [CIT_EUCLID, CIT_CCSS, CIT_ISO80000],
        "sig_lens": ("His Signature reading: the integers are the sworn "
                     "ranks of the line - every whole value standing at "
                     "its post, one pace apart, in both directions without "
                     "end. In the Signature method this is the first full "
                     "muster: the complete roll of whole numbers, each "
                     "witnessed, none missing, none doubled."),
    },
    {
        "key": "nl_ordering",
        "name": "Ordering Numbers: Less Than and Greater Than",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": ("Position on the line IS order: a number is smaller "
                        "exactly when it sits to the left, larger exactly "
                        "when it sits to the right. So -4 < -1 because -4 "
                        "lies left of -1, and 0 > -3 because 0 lies right of "
                        "-3. This one rule replaces memorizing sign tricks: "
                        "to compare two numbers, find their marks and read "
                        "left-to-right. The order is total - for any two "
                        "different numbers, one is always left of the "
                        "other - and transitive: if a sits left of b and b "
                        "sits left of c, then a sits left of c. That "
                        "transitivity is what lets the line sort whole "
                        "lists of numbers into a single correct sequence, "
                        "the way a ruler sorts lengths. Every inequality "
                        "in later mathematics is decided by this left-right "
                        "reading."),
        "how_it_works": ("Place both numbers as marks on the line and read "
                         "left to right: the leftmost mark is the smaller "
                         "number. Compare -4 and -1 by marking both - the "
                         "mark for -4 lies further left, so -4 < -1. "
                         "Compare 3.5 and 3 by marking both - 3.5 sits "
                         "right of 3, so 3.5 > 3. Sort a list like 2, -3, "
                         "0, 5, -1 by placing all five marks and reading "
                         "them left to right: -3, -1, 0, 2, 5. Verify "
                         "transitivity on any triple: if the leftmost is "
                         "smallest against the middle and the middle "
                         "against the rightmost, it is smallest against "
                         "the rightmost too."),
        "key_points": [
            "Left means smaller, right means larger - position is order.",
            "-4 < -1 because -4 lies left of -1.",
            "Order is total: any two different numbers compare.",
            "Order is transitive: a < b and b < c implies a < c.",
            "Sorting numbers is reading their marks left to right.",
        ],
        "requirements": [
            "Both compared numbers marked on the same line.",
            "A consistent left-to-right reading direction.",
        ],
        "standards": [
            "CCSS.MATH.CONTENT.6.NS.C.7a - interpret statements of inequality as statements about relative position.",
            "ISO 80000-2:2019 - symbols <, >, and the ordering relation.",
        ],
        "citations": [CIT_CCSS, CIT_ISO80000, CIT_APOSTOL],
        "sig_lens": ("His Signature reading: order is the covenant of the "
                     "line itself - every value sworn to its place, none "
                     "permitted to stand out of rank. Less-than and "
                     "greater-than are not opinions about numbers; they "
                     "are the witnessed standing order, readable by any "
                     "eye that walks the line left to right."),
    },
    {
        "key": "nl_addition",
        "name": "Addition as Steps to the Right",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": ("Addition on the number line is walking: start at "
                        "the first number and take steps to the right for "
                        "the second. To compute 3 + 4, stand on 3 and walk "
                        "4 steps right - you land on 7, so 3 + 4 = 7. "
                        "Adding a negative means walking left instead: "
                        "(-2) + 5 starts at -2 and walks 5 right, landing "
                        "on 3. This motion picture explains the rules that "
                        "textbooks state: adding positives moves right "
                        "(values grow), adding negatives moves left "
                        "(values shrink), and order does not matter - 4 "
                        "steps then 3 steps lands where 3 steps then 4 "
                        "steps lands (commutativity), because the total "
                        "march is 7 steps either way. The number line "
                        "turns addition from a memorized fact into a "
                        "journey you can watch."),
        "how_it_works": ("Stand a marker on the first addend. Face right "
                         "for a positive second addend (or left for a "
                         "negative one) and walk that many unit steps. "
                         "Read the landing mark - that is the sum. Work "
                         "3 + 4: stand on 3, walk 4 right, land on 7. "
                         "Work (-2) + 5: stand on -2, walk 5 right, land "
                         "on 3. Verify commutativity: 4 + 3 walks 4 then 3 "
                         "right for 7 total steps - the same landing as "
                         "3 + 4."),
        "key_points": [
            "Addition is walking: start at the first number, step right for a positive addend.",
            "Adding a negative means stepping left instead.",
            "3 + 4 = 7: stand on 3, walk 4 right, land on 7.",
            "Commutativity: the total march is the same in either order.",
            "Every addition is a visible journey on the line.",
        ],
        "requirements": [
            "A marked integer line with the origin visible.",
            "A movable marker for the walker.",
        ],
        "standards": [
            "CCSS.MATH.CONTENT.7.NS.A.1b - interpret sums of rational numbers on a number line.",
            "NCTM Principles to Actions - models for operations.",
        ],
        "citations": [CIT_CCSS, CIT_NCTM, CIT_APOSTOL],
        "sig_lens": ("His Signature reading: addition is the sworn march - "
                     "each addend a company of steps, the sum the ground "
                     "they take together. In the Signature method the "
                     "walker never guesses the landing: the steps are "
                     "counted, the direction is faced, and the line "
                     "witnesses every pace of the advance."),
    },
    {
        "key": "nl_subtraction",
        "name": "Subtraction as Steps to the Left",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": ("Subtraction is the reverse march: start at the "
                        "first number and walk left for the amount "
                        "subtracted. To compute 7 - 4, stand on 7 and walk "
                        "4 steps left - you land on 3, so 7 - 4 = 3. When "
                        "the march crosses zero it keeps going: 2 - 6 "
                        "starts at 2, walks 6 left, and lands on -4. This "
                        "picture reveals subtraction as adding the "
                        "opposite: 7 - 4 is the same journey as 7 + (-4), "
                        "because walking 4 left equals walking -4 right. "
                        "It also explains why subtracting a negative "
                        "moves right: 5 - (-3) means walk -3 left, which "
                        "is the same as walking 3 right, landing on 8. "
                        "The line leaves no mystery in the sign rules - "
                        "every subtraction is a walk you can trace."),
        "how_it_works": ("Stand a marker on the starting number. Walk left "
                         "as many steps as the number being subtracted and "
                         "read the landing mark. Work 7 - 4: stand on 7, "
                         "walk 4 left, land on 3. Work 2 - 6: stand on 2, "
                         "walk 6 left across the origin, land on -4. Show "
                         "the opposite rule: 7 + (-4) walks 4 left from 7 "
                         "as well, landing on the same 3 - so subtracting "
                         "4 and adding -4 are one journey. Show 5 - (-3): "
                         "walking -3 left is walking 3 right, landing on "
                         "8."),
        "key_points": [
            "Subtraction is walking left from the starting number.",
            "7 - 4 = 3: stand on 7, walk 4 left, land on 3.",
            "a - b equals a + (-b): walking b left is walking -b right.",
            "Subtracting a negative moves right: 5 - (-3) = 8.",
            "Crossing zero is ordinary: the march continues onto the negative side.",
        ],
        "requirements": [
            "A marked line extending into the negatives.",
            "The walker marker from the addition record.",
        ],
        "standards": [
            "CCSS.MATH.CONTENT.7.NS.A.1c - subtraction as adding the additive inverse.",
            "NCTM Principles to Actions - models for operations.",
        ],
        "citations": [CIT_CCSS, CIT_NCTM, CIT_APOSTOL],
        "sig_lens": ("His Signature reading: subtraction is the sworn "
                     "retreat - the line honors the march backward exactly "
                     "as it honored the advance. In the Signature method "
                     "every retreat is measured: the walker counts its "
                     "steps left, crosses the signet of zero without fear, "
                     "and the landing is witnessed like any other."),
    },
    {
        "key": "nl_halves_quarters",
        "name": "Between the Integers: Halves and Quarters",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": ("The integer marks are not the whole story - "
                        "between 0 and 1 live the fractions. Cut one unit "
                        "step into two equal halves and the cut falls at "
                        "1/2; cut it into four equal quarters and the cuts "
                        "fall at 1/4, 2/4, and 3/4. These are genuine "
                        "addresses on the line: 1/2 sits exactly halfway "
                        "between 0 and 1, and 3/4 sits three quarters of "
                        "the way. Reading order still works - 1/4 < 1/2 < "
                        "3/4 because the marks run left to right - and the "
                        "old rules hold: 1/4 + 1/4 + 1/4 + 1/4 walks four "
                        "quarter-steps from 0 and lands exactly on 1. This "
                        "record opens the line between the rungs: the "
                        "integers were a ladder of separate posts, but "
                        "fractions begin filling the gaps, and later "
                        "records will fill them completely."),
        "how_it_works": ("Take the unit step from 0 to 1 and divide it into "
                         "equal parts - fold or measure halves, then "
                         "quarters. Label the cut marks 1/2, then 1/4, "
                         "2/4, 3/4. Verify position by walking: four "
                         "quarter-steps from 0 reach 1, and two "
                         "quarter-steps reach the 1/2 mark - so 2/4 and "
                         "1/2 share one address. Compare by position: the "
                         "1/4 mark lies left of the 1/2 mark, confirming "
                         "1/4 < 1/2 without any memorized rule."),
        "key_points": [
            "Splitting a unit step into equal parts creates fraction addresses.",
            "1/2 is the halfway cut; 1/4, 2/4, 3/4 are the quarter cuts.",
            "2/4 and 1/2 share one address: equal fractions, equal positions.",
            "Left-to-right order still decides which fraction is larger.",
            "Four quarter-steps from 0 land exactly on 1.",
        ],
        "requirements": [
            "One unit step that can be divided evenly (folding works).",
            "Labels for the new cut marks.",
        ],
        "standards": [
            "CCSS.MATH.CONTENT.3.NF.A.2 - fractions as numbers on the number line.",
            "NCTM Principles to Actions - partitioning models.",
        ],
        "citations": [CIT_CCSS, CIT_NCTM, CIT_EUCLID],
        "sig_lens": ("His Signature reading: the halves and quarters are "
                     "the first settlers between the sworn posts - new "
                     "addresses raised in the gaps, each measured and "
                     "witnessed like the integers before them. In the "
                     "Signature method no gap stays empty forever: where "
                     "the line can be divided fairly, a value takes its "
                     "post."),
    },
    {
        "key": "nl_opposites",
        "name": "Opposites and Symmetry About Zero",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": ("Every number has an opposite: the number the same "
                        "distance from zero on the far side. The opposite "
                        "of 5 is -5, the opposite of -3.2 is 3.2, and the "
                        "opposite of 0 is 0 itself. Opposites are mirror "
                        "images across the origin - fold the line at 0 and "
                        "each pair of opposites lands on each other. Their "
                        "defining property is cancellation: a number plus "
                        "its opposite is always zero (5 + (-5) = 0), which "
                        "is why opposites undo each other in equations. "
                        "Symmetry about zero also governs distance: a and "
                        "-a are always equally far from the origin, so the "
                        "line is perfectly balanced at 0. This balance is "
                        "the geometric form of the additive inverse, one "
                        "of the deepest ideas in arithmetic."),
        "how_it_works": ("Pick a number and measure its distance from 0; "
                         "mark the point the same distance on the other "
                         "side - that is the opposite. Check with 5.3: the "
                         "opposite is -5.3, and folding the line at 0 "
                         "brings the two marks together. Verify "
                         "cancellation: 5.3 + (-5.3) walks 5.3 right then "
                         "5.3 left, returning to 0. Verify the zero case: "
                         "0 is its own opposite, the only number equal to "
                         "its mirror."),
        "key_points": [
            "The opposite of a is the point the same distance from 0 on the other side, written -a.",
            "a + (-a) = 0 always: opposites cancel.",
            "0 is its own opposite.",
            "Folding the line at 0 maps every number onto its opposite.",
            "Opposites are the geometric form of the additive inverse.",
        ],
        "requirements": [
            "A marked line with a visible origin for folding.",
            "A measured distance to mirror across zero.",
        ],
        "standards": [
            "CCSS.MATH.CONTENT.6.NS.C.6a - opposites as points symmetric about zero.",
            "ISO 80000-2:2019 - the unary minus and additive inverse.",
        ],
        "citations": [CIT_CCSS, CIT_ISO80000, CIT_APOSTOL],
        "sig_lens": ("His Signature reading: opposites are the sworn pairs "
                     "of the line - two values standing sentinel at equal "
                     "distance on either side of the signet, each the "
                     "mirror-guard of the other. In the Signature method "
                     "their oath is cancellation: together they return to "
                     "zero, the balance restored, the line at peace."),
    },
    {
        "key": "nl_ruler",
        "name": "The Ruler: Measuring Distance on the Line",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": ("A ruler is a number line you can hold: the "
                        "distance between any two numbers is the count of "
                        "unit steps between their marks. From 3 to 8 is 5 "
                        "steps, from -2 to 4 is 6 steps, and the rule is "
                        "always the same - distance equals the larger "
                        "minus the smaller, or in symbols, |b - a|. "
                        "Distance never cares about direction: the gap "
                        "from 8 to 3 is the same 5 steps as from 3 to 8, "
                        "which is why the absolute value appears - it "
                        "strips the sign and keeps the size. This is the "
                        "line doing its oldest job, the one rulers, tape "
                        "measures, and odometers do: turning the space "
                        "between two positions into a single honest "
                        "number. Every later idea of length, from the "
                        "midpoint to the Cartesian distance formula, "
                        "grows from this step-count."),
        "how_it_works": ("Mark the two numbers and count the unit steps "
                         "between their marks. From 3 to 8: count 4, 5, 6, "
                         "7, 8 - five steps. Compute it directly: 8 - 3 = "
                         "5. Cross zero the same way: from -2 to 4 the "
                         "marks span 4 - (-2) = 6 steps. Check direction "
                         "independence: from 8 down to 3 is still 5 steps, "
                         "so distance is |8 - 3| = |3 - 8| = 5 either way."),
        "key_points": [
            "Distance between a and b is the step-count between their marks.",
            "Distance = larger minus smaller = |b - a|.",
            "From -2 to 4 is 6 steps: 4 - (-2) = 6.",
            "Direction does not matter: |8 - 3| = |3 - 8| = 5.",
            "The ruler is a hand-held number line.",
        ],
        "requirements": [
            "A marked line or physical ruler with unit marks.",
            "Two numbers whose gap is to be measured.",
        ],
        "standards": [
            "CCSS.MATH.CONTENT.2.MD.A.1 - measure length with standard units.",
            "ISO 80000-2:2019 - absolute value notation |x|.",
        ],
        "citations": [CIT_CCSS, CIT_ISO80000, CIT_STEWART],
        "sig_lens": ("His Signature reading: the ruler is the line bearing "
                     "witness to the gap between two sworn positions - no "
                     "favor, no direction, only the honest count of steps. "
                     "In the Signature method distance is the sworn "
                     "testimony of separation: measured, signless, and "
                     "the same whichever way you walk it."),
    },
    {
        "key": "nl_reading",
        "name": "Reading and Marking Points on the Line",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": ("Fluency with the number line means two skills: "
                        "reading a marked point to name its number, and "
                        "marking a point for a given number. To read, find "
                        "the nearest labeled marks and measure the "
                        "fraction of the step: a dot two-thirds of the way "
                        "from 0 to 3 names the number 2, because 0 + (2/3) "
                        "x 3 = 2. To mark, work the rule backward: for "
                        "7/2, walk 3 full steps and one half-step more, "
                        "landing halfway between 3 and 4. Estimation "
                        "rides on the same skill - a dot just past the "
                        "midpoint between 10 and 20 reads about 11 or 12, "
                        "and checking means measuring. These two moves, "
                        "read and mark, are the hands of every later "
                        "record: graphing an inequality is marking a "
                        "region, reading a scale is reading a point, and "
                        "plotting data is marking many points at speed."),
        "how_it_works": ("To read a point: note the labeled marks on either "
                         "side, estimate what fraction of the step the dot "
                         "has crossed, and compute start + fraction x "
                         "step. A dot 2/3 of the way from 0 to 3 reads "
                         "0 + (2/3) x 3 = 2. To mark a number: walk its "
                         "whole part in unit steps, then its fractional "
                         "part of one more step - 7/2 = 3.5 lands halfway "
                         "between 3 and 4. Verify by reading back: the "
                         "marked 7/2 point, read as halfway between 3 and "
                         "4, returns 3.5."),
        "key_points": [
            "Reading: value = start + fraction of step x step size.",
            "Marking: walk the whole part, then the fractional part of a step.",
            "A dot 2/3 of the way from 0 to 3 reads as 2.",
            "7/2 marks halfway between 3 and 4.",
            "Read and mark are the hands of graphing, scales, and plotting.",
        ],
        "requirements": [
            "A line with labeled marks and at least one unlabeled dot.",
            "Fraction estimation of partial steps.",
        ],
        "standards": [
            "CCSS.MATH.CONTENT.3.NF.A.2b - mark fractions on the number line.",
            "NCTM Principles to Actions - representation fluency.",
        ],
        "citations": [CIT_CCSS, CIT_NCTM, CIT_DEVLIN],
        "sig_lens": ("His Signature reading: to read a point is to take "
                     "its testimony - to ask the mark where it stands and "
                     "write down its sworn answer. In the Signature method "
                     "every reading is an act of witness: find the "
                     "neighboring posts, measure the partial step, and "
                     "record the value exactly as the line declares it."),
    },
    # ------------------------------------------------------- COMPOUNDED
    {
        "key": "nl_fractions",
        "name": "Fractions on the Line",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": ("Every fraction a/b names an address: divide each "
                        "unit step into b equal parts and walk a of them "
                        "from 0. So 5/3 means thirds, five of them - one "
                        "full step and two thirds more, landing between 1 "
                        "and 2 at about 1.667. Equivalent fractions share "
                        "one address: 1/2, 2/4, and 3/6 all mark the same "
                        "halfway point, because different divisions can "
                        "cut the same place. Comparing fractions becomes "
                        "comparing positions: 3/4 lies right of 2/3 "
                        "(0.75 > 0.667), so 3/4 is larger - no common "
                        "denominator tricks required, though the tricks "
                        "agree. Adding fractions is walking "
                        "fraction-steps: 1/3 + 1/6 walks a third-step then "
                        "a sixth-step, landing on 1/2. The fractions, "
                        "positive, negative, and zero together, are the "
                        "rational numbers - the first dense filling of "
                        "the line."),
        "how_it_works": ("To place a/b: split every unit step into b equal "
                         "sub-steps and count a sub-steps from 0, walking "
                         "left for negative fractions. Place 5/3: thirds, "
                         "five of them - past 1 to the two-thirds mark, "
                         "about 1.667. Check equivalence: mark 1/2, 2/4, "
                         "and 3/6 - all three cuts coincide at the halfway "
                         "point, proving equal value by shared address. "
                         "Compare 3/4 and 2/3 by position: the 3/4 mark "
                         "stands right of the 2/3 mark, so 3/4 > 2/3."),
        "key_points": [
            "a/b means: split each unit into b parts, walk a of them from 0.",
            "5/3 lands between 1 and 2, at about 1.667.",
            "Equivalent fractions share one address: 1/2 = 2/4 = 3/6.",
            "Position decides comparisons: right means larger.",
            "Fractions with zero and negatives are the rational numbers.",
        ],
        "requirements": [
            "Unit steps divisible into equal sub-steps.",
            "The equivalence check: different divisions, same cut.",
        ],
        "standards": [
            "CCSS.MATH.CONTENT.3.NF.A.2 - fractions as numbers on the number line.",
            "CCSS.MATH.CONTENT.4.NF.A.1 - equivalent fractions.",
            "ISO 80000-2:2019 - symbol Q for the rationals.",
        ],
        "citations": [CIT_CCSS, CIT_EUCLID, CIT_ISO80000],
        "sig_lens": ("His Signature reading: fractions are the fine "
                     "surveying of the line - the unit post divided by "
                     "sworn measure, each sub-step witnessed before a "
                     "value takes its stand there. In the Signature "
                     "method equivalent fractions are one witness under "
                     "several names: 1/2, 2/4, 3/6 all testify to the "
                     "same halfway post."),
    },
    {
        "key": "nl_decimals",
        "name": "Decimals on the Line",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": ("Decimals are fractions written in base ten, and "
                        "on the line they mean tenths, hundredths, "
                        "thousandths of a step. Split each unit into ten "
                        "equal tenths: 2.37 sits at the 3rd tenth past 2 "
                        "plus 7 hundredths more - between 2.3 and 2.4, "
                        "closer to 2.4. Every terminating decimal is a "
                        "fraction in disguise (2.37 = 237/100), and every "
                        "such fraction has a decimal address, so decimals "
                        "and fractions mark the same points. The decimal "
                        "system shines at ordering: compare digit by "
                        "digit from the left - 2.37 > 2.369 because at "
                        "the hundredths place 7 beats 6. Measurement "
                        "lives in decimals: rulers marked in tenths and "
                        "millimeters are decimal number lines, and reading "
                        "one is the reading skill from the foundations "
                        "with finer marks."),
        "how_it_works": ("Divide each unit step into 10 tenths and each "
                         "tenth into 10 hundredths. To place 2.37: walk 2 "
                         "full steps, then 3 tenths, then 7 hundredths - "
                         "landing between the 2.3 and 2.4 marks. Verify "
                         "the fraction disguise: 237/100 places by the "
                         "fraction rule at exactly the same cut. Compare "
                         "2.37 and 2.369 digit by digit: tenths tie at 3, "
                         "hundredths decide 7 > 6, so 2.37 > 2.369 - and "
                         "the 2.37 mark indeed stands right of the 2.369 "
                         "mark."),
        "key_points": [
            "Decimals are base-ten fractions: tenths, hundredths, thousandths of a step.",
            "2.37 sits between 2.3 and 2.4, at 237/100.",
            "Every terminating decimal equals a fraction at the same address.",
            "Digit-by-digit comparison from the left matches left-to-right position.",
            "Rulers and gauges are physical decimal number lines.",
        ],
        "requirements": [
            "Unit steps divided into tenths, then hundredths.",
            "The digit-by-digit comparison habit.",
        ],
        "standards": [
            "CCSS.MATH.CONTENT.4.NF.C.6 - decimal notation for fractions with denominator 10 or 100.",
            "CCSS.MATH.CONTENT.5.NBT.A.3b - compare decimals by place value.",
        ],
        "citations": [CIT_CCSS, CIT_NCTM, CIT_DEVLIN],
        "sig_lens": ("His Signature reading: decimals are the line "
                     "surveyed by tens - each place a finer witnessing of "
                     "the gap, tenths then hundredths then thousandths, "
                     "the testimony growing sharper with every digit. In "
                     "the Signature method a decimal is a value "
                     "introducing itself place by place, and the line "
                     "records each digit as it is sworn."),
    },
    {
        "key": "nl_rationals",
        "name": "Rational Numbers: Dense but Not Complete",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": ("The rational numbers - all fractions p/q - crowd "
                        "the line so tightly that between any two of them "
                        "sits another: the midpoint (a+b)/2 of two "
                        "rationals is rational and strictly between them. "
                        "Between 1/3 and 1/2 lies 5/12; between 1/3 and "
                        "5/12 lies another; there is no end to the "
                        "filling. Mathematicians call this density, and "
                        "it means no rational has a rational neighbor - "
                        "the rungs of the integer ladder have dissolved "
                        "into a crowd. Yet the crowd has holes: this "
                        "record proves by position that no fraction lands "
                        "exactly on the square root of 2 (about 1.4142), "
                        "though rationals approach it as closely as you "
                        "like. Dense but not complete - the rationals "
                        "fill the line beyond any magnifier yet still "
                        "miss points, which is why mathematics needed the "
                        "real numbers of the advanced tier."),
        "how_it_works": ("Prove density: take any two rationals a < b; "
                         "their midpoint m = (a+b)/2 is rational (sums and "
                         "halves of fractions stay fractional) and "
                         "a < m < b, so a third rational always fits "
                         "between. Work it: between 1/3 and 1/2 the "
                         "midpoint is 5/12, and 1/3 < 5/12 < 1/2 "
                         "checks out. Show the hole: square the "
                         "candidates near 1.4142 - (1.41)^2 = 1.9881 and "
                         "(1.42)^2 = 2.0164, so the true square root of 2 "
                         "lies strictly between two rationals whose "
                         "squares straddle 2, with no fraction squaring "
                         "to exactly 2."),
        "key_points": [
            "Rationals are dense: between any two sits another, via the midpoint.",
            "Between 1/3 and 1/2 lies the rational 5/12.",
            "No rational has a rational neighbor.",
            "Dense is not complete: no fraction equals the square root of 2 exactly.",
            "Rationals approach sqrt(2) arbitrarily closely but never land on it.",
        ],
        "requirements": [
            "The midpoint formula for rationals.",
            "Squaring to test candidates near sqrt(2).",
        ],
        "standards": [
            "CCSS.MATH.CONTENT.8.NS.A.1 - rational vs irrational numbers.",
            "NCTM Principles to Actions - density of the rationals.",
        ],
        "citations": [CIT_CCSS, CIT_NCTM, CIT_RUDIN],
        "sig_lens": ("His Signature reading: the rationals are the great "
                     "crowd of the line - value upon value, no two "
                     "neighbors, the filling without end. But in the "
                     "Signature method even a crowd can miss a post: the "
                     "line keeps one address, the square root of 2, that "
                     "no fraction can swear to - and the line is honest "
                     "about the gap."),
    },
    {
        "key": "nl_absvalue",
        "name": "Absolute Value as Distance from Zero",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": ("The absolute value |x| is the distance from x to "
                        "zero - the step-count from the mark to the "
                        "origin, direction stripped away. So |-7| = 7 and "
                        "|7| = 7: both marks stand 7 steps from 0. More "
                        "generally, |x - a| is the distance between x and "
                        "a, which makes absolute value the line's "
                        "distance language: |-4 - 3| = |-7| = 7 says the "
                        "marks -4 and 3 stand 7 steps apart. The piecewise "
                        "rule falls out of the picture - |x| = x when x "
                        "sits right of zero (no stripping needed) and "
                        "|x| = -x when x sits left (the minus flips it "
                        "positive). Absolute value turns up wherever size "
                        "matters and sign does not: errors, tolerances, "
                        "deviations, and every distance on the line."),
        "how_it_works": ("To find |x|: locate x and count steps to 0. For "
                         "-7, count 7 steps to the origin - so |-7| = 7. "
                         "For distances between points, subtract then "
                         "strip: |-4 - 3| = |-7| = 7, verified by counting "
                         "the steps from -4 to 3. Check the piecewise "
                         "rule: |5| = 5 directly (right of zero), while "
                         "|-5| = -(-5) = 5 (the flip makes it positive). "
                         "Confirm |0| = 0 - the origin is zero steps from "
                         "itself."),
        "key_points": [
            "|x| is the distance from x to 0: |-7| = 7, |7| = 7.",
            "|x - a| is the distance between x and a.",
            "|-4 - 3| = 7: the marks -4 and 3 are 7 steps apart.",
            "Piecewise: |x| = x for x >= 0, |x| = -x for x < 0.",
            "Absolute value keeps size and discards sign.",
        ],
        "requirements": [
            "The origin as the measuring base.",
            "The distance-as-subtraction rule from the ruler record.",
        ],
        "standards": [
            "CCSS.MATH.CONTENT.6.NS.C.7c - absolute value as distance from zero.",
            "ISO 80000-2:2019 - absolute value notation |x|.",
        ],
        "citations": [CIT_CCSS, CIT_ISO80000, CIT_APOSTOL],
        "sig_lens": ("His Signature reading: absolute value is the line "
                     "testifying to distance alone - the sign set aside, "
                     "the separation sworn in plain steps. In the "
                     "Signature method |x| asks one question of a value: "
                     "how far do you stand from the signet of zero - and "
                     "the answer is always honest, always positive."),
    },
    {
        "key": "nl_intervals",
        "name": "Intervals: Segments of the Number Line",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": ("An interval is a continuous stretch of the line "
                        "named by its endpoints: [2, 5] is every number "
                        "from 2 to 5, endpoints included. The bracket "
                        "shapes are the whole grammar - square brackets "
                        "[ ] include the endpoint (closed), round "
                        "parentheses ( ) exclude it (open): (2, 5) holds "
                        "everything strictly between but not 2 or 5 "
                        "themselves, while [2, 5) includes 2 but stops "
                        "short of 5. Every interval has a length "
                        "(right endpoint minus left: 5 - 2 = 3) and a "
                        "midpoint ((2+5)/2 = 3.5), the center of the "
                        "stretch. Membership is a position test: 4.999 "
                        "belongs to (2, 5) but 5 does not; -1 belongs to "
                        "neither. Intervals are how mathematics names "
                        "ranges - tolerances, domains, solution sets - "
                        "and the next records build inequalities and "
                        "arithmetic on them."),
        "how_it_works": ("Write the interval with its endpoints and "
                         "brackets, then shade the stretch between them on "
                         "the line - solid dots on included endpoints, "
                         "hollow dots on excluded ones. For [2, 5]: shade "
                         "2 through 5 with solid dots at both ends; "
                         "length = 5 - 2 = 3, midpoint = 3.5. Test "
                         "membership by position: 3.5 lies inside the "
                         "shading (member), 5 sits on a solid dot (member "
                         "of [2,5] but not of [2,5)), and 5.001 lies "
                         "outside (not a member)."),
        "key_points": [
            "[2, 5] is all numbers from 2 to 5, endpoints included.",
            "[ ] includes the endpoint; ( ) excludes it.",
            "Length = right endpoint minus left: 5 - 2 = 3.",
            "Midpoint = (left + right)/2: 3.5 for [2, 5].",
            "Membership is a position test against the shaded stretch.",
        ],
        "requirements": [
            "Endpoint marks with solid/hollow dots for inclusion.",
            "Shading of the included stretch.",
        ],
        "standards": [
            "CCSS.MATH.CONTENT.HSN-CN - interval and set language in high school number.",
            "ISO 80000-2:2019 - interval notation [a, b], (a, b).",
        ],
        "citations": [CIT_CCSS, CIT_ISO80000, CIT_STEWART],
        "sig_lens": ("His Signature reading: an interval is a sworn "
                     "territory of the line - two boundary posts and every "
                     "value between them claimed in one name. In the "
                     "Signature method the brackets are the terms of the "
                     "claim: the square bracket seals the endpoint inside, "
                     "the round parenthesis leaves it standing outside, "
                     "and the line witnesses the boundary exactly as "
                     "written."),
    },
    {
        "key": "nl_inequalities",
        "name": "Graphing Inequalities on the Line",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": ("An inequality like x > 3 is not one address but a "
                        "whole region: every number right of 3. Graphing "
                        "it means shading that ray - a hollow dot at 3 "
                        "(3 itself is not included) and shading to the "
                        "right without end. The direction of the sign "
                        "points the shading: > and >= shade right "
                        "(greater), < and <= shade left (smaller), and "
                        "the bar under the sign (>=, <=) fills the "
                        "endpoint dot. Solving goes the same way: 2x + 1 "
                        "<= 9 simplifies to x <= 4, and the graph is a "
                        "solid dot at 4 with shading left. Test points "
                        "verify the work - x = 0 satisfies x > -2 (shade "
                        "the side containing 0), x = -5 does not. "
                        "Compound inequalities chain regions: 1 < x <= 4 "
                        "shades the stretch between, hollow at 1, solid "
                        "at 4. Every inequality is a question the line "
                        "answers with shading."),
        "how_it_works": ("Solve the inequality for x alone, keeping the "
                         "sign direction - flip it only when multiplying "
                         "or dividing by a negative. For 2x + 1 <= 9: "
                         "subtract 1 (2x <= 8), divide by 2 (x <= 4). "
                         "Mark 4 with a solid dot (<= includes it) and "
                         "shade left. Verify with test points: x = 0 "
                         "gives 1 <= 9, true, and 0 lies in the shading; "
                         "x = 6 gives 13 <= 9, false, and 6 lies outside. "
                         "For x > 3: hollow dot at 3, shade right; x = 4 "
                         "tests true, x = 3 tests false."),
        "key_points": [
            "x > 3 graphs as a hollow dot at 3 with shading right.",
            "> and >= shade right; < and <= shade left.",
            "The bar (>/=, </=) fills the endpoint dot: included.",
            "2x + 1 <= 9 solves to x <= 4: solid dot at 4, shade left.",
            "Test points verify: one inside the shading, one outside.",
        ],
        "requirements": [
            "Solved form with x alone on one side.",
            "Hollow/solid endpoint dots and directional shading.",
        ],
        "standards": [
            "CCSS.MATH.CONTENT.6.EE.B.8 - write and graph inequalities.",
            "CCSS.MATH.CONTENT.HSA-REI.B.3 - solve linear inequalities.",
        ],
        "citations": [CIT_CCSS, CIT_STEWART, CIT_APOSTOL],
        "sig_lens": ("His Signature reading: an inequality is a decree "
                     "over the line - the sign declares which territory "
                     "belongs to x, and the shading raises the banner "
                     "over every claimed value. In the Signature method "
                     "the endpoint dot is the seal of the decree: hollow "
                     "where the boundary itself is refused, solid where "
                     "it is sworn in."),
    },
    {
        "key": "nl_midpoint",
        "name": "The Midpoint of Two Numbers",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": ("The midpoint of a and b is the point exactly "
                        "halfway between them: m = (a + b)/2. Between -3 "
                        "and 7 the midpoint is (−3 + 7)/2 = 2 - check: 2 "
                        "stands 5 steps from -3 and 5 steps from 7, "
                        "perfectly centered. The formula is an average: "
                        "add the two positions and split the sum, which "
                        "is why the midpoint of two rationals is rational "
                        "and why it powered the density proof two records "
                        "ago. Midpoints bisect intervals, center ranges, "
                        "and locate medians: the midpoint of [2, 5] is "
                        "3.5, the heart of the stretch. In higher "
                        "dimensions the same idea averages each "
                        "coordinate, but on the line it is one honest "
                        "average - the balance point of two marks."),
        "how_it_works": ("Add the two endpoint numbers and divide by 2. "
                         "For -3 and 7: (−3 + 7)/2 = 4/2 = 2. Verify "
                         "centering: |2 − (−3)| = 5 and |7 − 2| = 5 - "
                         "equal distances, so 2 is exactly midway. Use "
                         "it on an interval: the midpoint of [2, 5] is "
                         "(2 + 5)/2 = 3.5, the center of the shaded "
                         "stretch. Check the average sense: the midpoint "
                         "is the number m with a + b = 2m, so the pair "
                         "balances at m like a seesaw."),
        "key_points": [
            "Midpoint m = (a + b)/2: the point halfway between a and b.",
            "Midpoint of -3 and 7 is 2, five steps from each.",
            "Equal distances verify centering: |m - a| = |b - m|.",
            "The midpoint of rationals is rational (density engine).",
            "The midpoint of [2, 5] is 3.5, the heart of the interval.",
        ],
        "requirements": [
            "Two endpoint numbers on the line.",
            "The average: sum, then halve.",
        ],
        "standards": [
            "CCSS.MATH.CONTENT.6.NS.C.6c - find and position rational numbers; midpoint reasoning.",
            "NCTM Principles to Actions - averaging as centering.",
        ],
        "citations": [CIT_CCSS, CIT_NCTM, CIT_APOSTOL],
        "sig_lens": ("His Signature reading: the midpoint is the sworn "
                     "truce between two positions - the single post "
                     "exactly equidistant, where neither endpoint can "
                     "claim advantage. In the Signature method the "
                     "midpoint is found by honest averaging: add the two "
                     "witnesses, split the sum, and the line confirms "
                     "the balance with equal steps on either side."),
    },
    {
        "key": "nl_multiplication",
        "name": "Multiplication as Scaling on the Line",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": ("Multiplication stretches or flips the line: 3 x 4 "
                        "means take the position 3 and scale it by 4, "
                        "landing on 12 - the mark 3 is pushed four times "
                        "farther from the origin. Scaling by a number "
                        "greater than 1 pushes outward; scaling by a "
                        "fraction pulls inward (3 x 1/2 = 1.5, halfway "
                        "to the origin). A negative multiplier adds a "
                        "mirror-flip across zero: (−2) x 5 lands on −10, "
                        "the 2-mark stretched fivefold then reflected to "
                        "the far side. Two negatives flip twice and land "
                        "back on the positive side: (−3) x (−4) = 12. "
                        "This picture explains the sign rules without "
                        "memorization - the sign of the product is the "
                        "parity of the flips - and shows why multiplying "
                        "by 0 collapses everything onto the origin."),
        "how_it_works": ("To compute a x b: start at a, scale its distance "
                         "from 0 by |b|, then flip across the origin if b "
                         "is negative. Work 3 x 4: the 3-mark sits 3 from "
                         "0; scale by 4 to distance 12, no flip - land on "
                         "12. Work (−2) x 5: distance 2 scales to 10, then "
                         "the positive 5 means no flip... careful: the "
                         "multiplier is +5 and the base is −2, so the "
                         "product keeps the base's side: −10. Work "
                         "(−3) x (−4): base −3 at distance 3, scale to 12, "
                         "negative multiplier flips across 0 - land on "
                         "+12."),
        "key_points": [
            "a x b scales the distance of a from 0 by |b|.",
            "A negative multiplier reflects the result across zero.",
            "3 x 4 = 12: the 3-mark pushed four times farther out.",
            "(−3) x (−4) = 12: two flips return to the positive side.",
            "Multiplying by 0 collapses every position onto the origin.",
        ],
        "requirements": [
            "The origin as the center of scaling.",
            "The flip rule for negative multipliers.",
        ],
        "standards": [
            "CCSS.MATH.CONTENT.7.NS.A.2 - multiplication of rational numbers and sign rules.",
            "NCTM Principles to Actions - scaling models.",
        ],
        "citations": [CIT_CCSS, CIT_NCTM, CIT_APOSTOL],
        "sig_lens": ("His Signature reading: multiplication is the line "
                     "under orders to stretch - every sworn position "
                     "marched outward by the scale factor, the ranks "
                     "holding their order. In the Signature method a "
                     "negative scale is a double command, stretch and "
                     "about-face across the signet, and two negatives "
                     "about-face twice and stand tall on the positive "
                     "side again."),
    },
    {
        "key": "nl_division",
        "name": "Division as Reverse Scaling",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": ("Division undoes scaling: 12 / 4 asks what "
                        "position, scaled by 4, lands on 12 - the answer "
                        "is 3, the mark that stretches to 12. Equivalently "
                        "it shrinks: divide by 4 and every distance from "
                        "the origin quarters, so the 12-mark slides home "
                        "to 3. The sign rules mirror multiplication - "
                        "(−12)/4 = −3, 12/(−4) = −3, (−12)/(−4) = 3 - "
                        "because division is multiplication by the "
                        "reciprocal (12/4 = 12 x 1/4). The line shows why "
                        "division by zero is forbidden: no scaling of "
                        "any position by 0 can reach a nonzero target, "
                        "and 0/0 could be anything - the reverse march "
                        "has no destination, so mathematics refuses the "
                        "order. Division by a fraction scales up: 6 / "
                        "(1/2) = 12, because halving reversed is "
                        "doubling."),
        "how_it_works": ("To compute a / b: find the position that scales "
                         "by b to reach a, or shrink a's distance from 0 "
                         "by the factor b. Work 12/4: what scales by 4 to "
                         "12? 3 - verify 3 x 4 = 12. Work (−12)/4: shrink "
                         "12 to 3, keep the negative side - land on −3. "
                         "Show the reciprocal form: 6 / (1/2) = 6 x 2 = "
                         "12, since dividing by a half undoes halving. "
                         "Demonstrate the zero ban: try to solve x x 0 = "
                         "5 - every x gives 0, never 5, so 5/0 has no "
                         "answer on the line."),
        "key_points": [
            "a / b is the position that scales by b to reach a.",
            "12 / 4 = 3, verified by 3 x 4 = 12.",
            "Sign rules mirror multiplication: (−12)/(−4) = 3.",
            "Dividing by a fraction scales up: 6 / (1/2) = 12.",
            "Division by zero has no destination: forbidden.",
        ],
        "requirements": [
            "The scaling picture from the multiplication record.",
            "The reciprocal: dividing by b is multiplying by 1/b.",
        ],
        "standards": [
            "CCSS.MATH.CONTENT.7.NS.A.2b - division of rational numbers.",
            "CCSS.MATH.CONTENT.7.NS.A.3 - the division-by-zero context.",
        ],
        "citations": [CIT_CCSS, CIT_APOSTOL, CIT_RUDIN],
        "sig_lens": ("His Signature reading: division is the recall order "
                     "- the stretched ranks marched home by the same "
                     "factor that sent them out, each position returning "
                     "to its true post. In the Signature method the line "
                     "refuses one order only: divide by zero, the command "
                     "with no destination, and the refusal is itself "
                     "witnessed - no march, no landing, no lie."),
    },
    {
        "key": "nl_sqrt",
        "name": "Square Roots on the Line",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": ("The square root of 2 is the number whose square "
                        "is 2 - and it lives on the line at about 1.4142, "
                        "between 1 and 2. Find it by bracketing: 1.4^2 = "
                        "1.96 (too small, mark left of target), 1.5^2 = "
                        "2.25 (too big, mark right), so the root lies "
                        "between 1.4 and 1.5. Narrow the bracket - 1.41^2 "
                        "= 1.9881, 1.42^2 = 2.0164 - and the address "
                        "sharpens to about 1.4142. This bisection is the "
                        "line doing analysis: every bracket is an "
                        "interval, and the true value is the one point "
                        "all the brackets share. The surprise, proved in "
                        "the rationals record, is that no fraction ever "
                        "lands exactly on this point - the square root "
                        "of 2 is the line's first proven irrational "
                        "resident, the hole the rationals could not "
                        "fill."),
        "how_it_works": ("Bracket the root: find integers with squares "
                         "straddling 2 - 1^2 = 1 < 2 < 4 = 2^2, so the "
                         "root lies in (1, 2). Bisect: test 1.5, square "
                         "it (2.25 > 2), keep the left half (1, 1.5). "
                         "Repeat: 1.4^2 = 1.96 < 2 keeps (1.4, 1.5); "
                         "1.41^2 = 1.9881 < 2 and 1.42^2 = 2.0164 > 2 "
                         "give (1.41, 1.42). Two more rounds pin "
                         "1.41421 < sqrt(2) < 1.41422 - mark the "
                         "midpoint 1.4142 as the working address."),
        "key_points": [
            "sqrt(2) is the number whose square is 2, at about 1.4142.",
            "Bracketing: 1.4^2 = 1.96 < 2 < 2.25 = 1.5^2.",
            "Bisection narrows the interval to 1.41421 < sqrt(2) < 1.41422.",
            "Every bracket is an interval; the root is their shared point.",
            "No fraction squares to exactly 2: sqrt(2) is irrational.",
        ],
        "requirements": [
            "Squaring to test each bracket endpoint.",
            "The bisection habit: halve the interval, keep the straddling half.",
        ],
        "standards": [
            "CCSS.MATH.CONTENT.8.NS.A.2 - rational approximations of irrational numbers.",
            "NCTM Principles to Actions - approximation and proof.",
        ],
        "citations": [CIT_CCSS, CIT_EUCLID, CIT_RUDIN],
        "sig_lens": ("His Signature reading: the square root of 2 is the "
                     "address the fractions could never swear to, yet the "
                     "line holds the post open - and bisection is the "
                     "Signature way of closing in, bracket by witnessed "
                     "bracket, until the unsealable value stands located "
                     "to four honest digits. In the Signature method even "
                     "the unreachable gets a located post."),
    },
    {
        "key": "nl_axis",
        "name": "The Line as a Coordinate Axis",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": ("Turn the number line on its side in your mind and "
                        "it becomes the x-axis: the horizontal ruler of "
                        "the coordinate plane, with 0 at the center, "
                        "positives running right, negatives running left. "
                        "Every point of the plane is located by its "
                        "x-address on this axis (plus its y-address on "
                        "the vertical one): the point (3.5, 2) stands "
                        "above the 3.5 mark of the x-axis. Mapping values "
                        "to pixels uses the same idea: screen_x = "
                        "origin_px + value x scale, so with origin at "
                        "pixel 100 and scale 20 px per unit, the value "
                        "3.5 draws at pixel 170. This is the number line "
                        "graduating from a math object to a measuring "
                        "instrument - the axis under every graph, every "
                        "chart, every map scale. Functions will soon be "
                        "drawn as curves above this axis, but the axis "
                        "itself never changes: it is the line, doing "
                        "duty as a coordinate."),
        "how_it_works": ("Lay the number line horizontally and call it the "
                         "x-axis. Locate (3.5, 2): find 3.5 on the axis, "
                         "rise 2 units - the axis gives the horizontal "
                         "address. Convert a value to a screen position: "
                         "pixel = origin_px + value x scale. With origin "
                         "at pixel 100 and 20 px per unit, x = 3.5 maps "
                         "to 100 + 3.5 x 20 = 170. Verify the origin "
                         "maps to itself: 100 + 0 x 20 = 100. Check a "
                         "negative: x = −2 maps to 100 − 40 = 60, left "
                         "of the origin as it should be."),
        "key_points": [
            "The x-axis is the number line in coordinate duty.",
            "Point (3.5, 2) is addressed horizontally by 3.5 on the axis.",
            "Value-to-pixel: pixel = origin_px + value x scale.",
            "3.5 maps to pixel 170 with origin 100 and scale 20.",
            "Every graph, chart, and map scale rests on this axis.",
        ],
        "requirements": [
            "The number line drawn horizontally as the x-axis.",
            "An origin pixel and a pixels-per-unit scale.",
        ],
        "standards": [
            "CCSS.MATH.CONTENT.6.NS.C.6b - the coordinate plane and quadrants.",
            "CCSS.MATH.CONTENT.5.G.A.1 - coordinate systems.",
        ],
        "citations": [CIT_CCSS, CIT_DEVLIN, CIT_STEWART],
        "sig_lens": ("His Signature reading: the axis is the line taking "
                     "up its post as surveyor - no longer just numbering "
                     "itself, but giving every point of the plane its "
                     "sworn horizontal address. In the Signature method "
                     "the x-axis is the same line with a commission: "
                     "measure all positions, witness all addresses, and "
                     "report each value exactly where it stands."),
    },
    {
        "key": "nl_benchmarks",
        "name": "Benchmarks: Estimating Positions on the Line",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": ("Estimation on the line means trapping a number "
                        "between known benchmarks and judging which it "
                        "leans toward. Pi (about 3.1416) sits between 3 "
                        "and 4, closer to 3 - the estimate 3.14 errs by "
                        "less than 0.002. The square root of 50 sits "
                        "between 7 and 8, because 7^2 = 49 and 8^2 = 64; "
                        "it leans hard toward 7 (50 is only 1 past 49), "
                        "and indeed sqrt(50) is about 7.071. Benchmarks "
                        "are the friendly landmarks - integers, halves, "
                        "familiar constants - and the method is always "
                        "the same: bracket with benchmarks, compare "
                        "distances, state the error bound. This skill is "
                        "the working engineer's number line: before "
                        "computing exactly, know roughly where the answer "
                        "must land, and let the line catch any nonsense "
                        "a calculation produces."),
        "how_it_works": ("Pick benchmarks bracketing the target: for pi, "
                         "3 and 4. Judge the lean: 3.1416 is 0.1416 past "
                         "3 and 0.8584 short of 4 - closer to 3. State "
                         "the estimate with its error bound: 3.14 is "
                         "within 0.002 of pi. For sqrt(50): bracket with "
                         "7^2 = 49 and 8^2 = 64 - 50 is 1/15 of the way "
                         "from 49 to 64, so estimate just above 7: about "
                         "7.07, and indeed sqrt(50) = 7.0711. Verify by "
                         "squaring the estimate: 7.07^2 = 49.9849, within "
                         "0.02 of 50."),
        "key_points": [
            "Estimation traps a number between known benchmarks.",
            "Pi is about 3.14: between 3 and 4, leaning to 3.",
            "sqrt(50) is about 7.07: between 7 and 8, leaning hard to 7.",
            "Always state the error bound with the estimate.",
            "Squaring the estimate verifies the bracket.",
        ],
        "requirements": [
            "Friendly benchmarks: integers, halves, known constants.",
            "The bracket-compare-bound routine.",
        ],
        "standards": [
            "CCSS.MATH.CONTENT.8.NS.A.2 - estimate irrational numbers by bracketing.",
            "NCTM Principles to Actions - estimation and number sense.",
        ],
        "citations": [CIT_CCSS, CIT_NCTM, CIT_DEVLIN],
        "sig_lens": ("His Signature reading: benchmarks are the trusted "
                     "elders of the line - the well-known posts between "
                     "which a stranger's position can be sworn "
                     "approximately. In the Signature method an estimate "
                     "is an honest preliminary testimony: bracketed, "
                     "lean judged, error bound declared - never a guess "
                     "pretending to be a measurement."),
    },
    # --------------------------------------------------------- ADVANCED
    {
        "key": "nl_irrationals",
        "name": "The Irrational Numbers on the Line",
        "group": "Advanced",
        "ladder_rank": 7,
        "ladder_tier": "advanced",
        "description": ("Irrational numbers are the points no fraction "
                        "can name: their decimal expansions run forever "
                        "without repeating. The square root of 2 "
                        "(1.41421356...), pi (3.14159265...), and e "
                        "(2.71828182...) are the famous residents - each "
                        "provably not equal to any p/q. Their convergents "
                        "show the chase: 7/5 = 1.4, 17/12 = 1.4167, "
                        "41/29 = 1.41379, each a better rational "
                        "approximation of sqrt(2), the error shrinking "
                        "every round, yet equality never arrives. The "
                        "classic proof is by contradiction: if sqrt(2) = "
                        "p/q in lowest terms, then p^2 = 2q^2 forces p "
                        "even, then q even - contradicting lowest terms. "
                        "So the point exists on the line (bisection finds "
                        "it) but no fraction names it. The irrationals "
                        "are the majority of the line's points - the "
                        "rationals, though dense, are outnumbered beyond "
                        "all measure."),
        "how_it_works": ("List the convergents of sqrt(2) and watch the "
                         "error shrink: 7/5 = 1.4 (error 0.0142), 17/12 "
                         "= 1.41667 (error 0.00245), 41/29 = 1.413793 "
                         "(error 0.00042) - each strictly closer, none "
                         "exact. Verify no small-denominator fraction "
                         "hits it: for denominators 1 through 200, the "
                         "closest |p^2/q^2 − 2| stays positive - near "
                         "zero but never zero. Sketch the contradiction "
                         "proof: assume sqrt(2) = p/q reduced; then p^2 "
                         "= 2q^2, so p is even, p = 2k, then 2k^2 = q^2, "
                         "so q is even - but a reduced fraction cannot "
                         "have both even. Therefore no such fraction "
                         "exists."),
        "key_points": [
            "Irrationals are points no fraction names; decimals run forever without repeating.",
            "sqrt(2), pi, and e are proven irrational residents of the line.",
            "Convergents 7/5, 17/12, 41/29 approach sqrt(2) with shrinking error, never equality.",
            "Contradiction proof: sqrt(2) = p/q in lowest terms forces both p and q even.",
            "The irrationals vastly outnumber the rationals.",
        ],
        "requirements": [
            "The density record: rationals approach but the point is extra.",
            "The even/odd contradiction argument.",
        ],
        "standards": [
            "CCSS.MATH.CONTENT.8.NS.A.1 - irrational numbers and decimal expansions.",
            "NCTM Principles to Actions - proof in the number system.",
        ],
        "citations": [CIT_CCSS, CIT_EUCLID, CIT_RUDIN],
        "sig_lens": ("His Signature reading: the irrationals are the "
                     "unnamable posts of the line - positions the "
                     "fraction-roll can approach forever yet never swear "
                     "to by name. In the Signature method this is no "
                     "failure of the line but its depth: bisection "
                     "locates them, proof certifies them, and the line "
                     "holds their posts open with full honors, named or "
                     "not."),
    },
    {
        "key": "nl_completeness",
        "name": "The Real Number Line: Completeness",
        "group": "Advanced",
        "ladder_rank": 7,
        "ladder_tier": "advanced",
        "description": ("Add the irrationals to the rationals and the "
                        "line is complete: every point is a real number, "
                        "and every real number is a point. Completeness "
                        "has a precise meaning - every nonempty set of "
                        "reals with an upper bound has a least upper "
                        "bound (a supremum). Take S = {x : x^2 < 2}: "
                        "every element is below 1.5, and the least such "
                        "ceiling is sqrt(2) itself, about 1.41421356 - "
                        "a number the rationals alone could not supply "
                        "as the ceiling. Dedekind built the reals in 1872 "
                        "by cutting the rationals at every such gap: "
                        "each cut IS a real number, and the cuts fill "
                        "every hole. The payoff is enormous - calculus "
                        "rests on completeness: limits, continuity, and "
                        "the intermediate value theorem all need a line "
                        "with no missing points. The real line is the "
                        "finished instrument."),
        "how_it_works": ("Form S = {rational x : x^2 < 2} and find its "
                         "least upper bound. Upper bounds include 1.5, "
                         "1.42, 1.415; the least is the limit of the "
                         "bisection brackets, sqrt(2) = 1.41421356... - "
                         "verify: 1.41421^2 = 1.999989 < 2 and 1.41422^2 "
                         "= 2.000018 > 2, so the supremum lies between, "
                         "at the irrational point. Note the rationals "
                         "alone fail: S has rational upper bounds but no "
                         "rational least upper bound - the ceiling itself "
                         "is the missing point. This is Dedekind's cut: "
                         "the set of rationals below the gap defines the "
                         "real that fills it."),
        "key_points": [
            "The reals = rationals + irrationals: every point named, no holes.",
            "Completeness: every bounded-above nonempty set has a least upper bound.",
            "S = {x : x^2 < 2} has supremum sqrt(2), an irrational ceiling.",
            "The rationals alone have no least upper bound for S.",
            "Dedekind (1872): each cut in the rationals is a real number.",
        ],
        "requirements": [
            "The irrational record: the missing points identified.",
            "The supremum idea: least of the upper bounds.",
        ],
        "standards": [
            "CCSS.MATH.CONTENT.HSN-RN - the real number system and completeness.",
            "NCTM Principles to Actions - the completed number line.",
        ],
        "citations": [CIT_DEDEKIND, CIT_RUDIN, CIT_CCSS],
        "sig_lens": ("His Signature reading: completeness is the line "
                     "fully mustered - every gap filled, every post "
                     "occupied, no address left unsworn. In the "
                     "Signature method Dedekind's cut is the final "
                     "witnessing: where the rationals left a gap, the "
                     "cut itself takes the stand, and the line declares "
                     "the roll complete - the finished instrument, ready "
                     "for calculus."),
    },
    {
        "key": "nl_interval_notation",
        "name": "Interval Notation and Set Notation",
        "group": "Advanced",
        "ladder_rank": 7,
        "ladder_tier": "advanced",
        "description": ("Interval notation is the compact script for "
                        "stretches of the line: [−1, 4) names every x "
                        "with −1 ≤ x < 4, the square bracket sealing −1 "
                        "in, the parenthesis holding 4 out. Set-builder "
                        "notation says the same thing in words of logic: "
                        "{x : −1 ≤ x < 4}, read 'the set of x such that "
                        "x is at least −1 and below 4'. The two scripts "
                        "translate both ways - [2, 5] is {x : 2 ≤ x ≤ 5}, "
                        "(−∞, 3] is {x : x ≤ 3} - and fluency means "
                        "reading either at sight. Membership tests are "
                        "mechanical: −1 belongs to [−1, 4) (sealed in), "
                        "4 does not (held out), 0 does (between). Unions "
                        "join stretches: [0, 1] ∪ [2, 3] is two separate "
                        "shaded pieces named as one set. This notation "
                        "is the working language of domains, ranges, and "
                        "solution sets across all of analysis."),
        "how_it_works": ("Translate [−1, 4) to set-builder: {x : −1 ≤ x "
                         "< 4} - the bracket becomes ≤, the parenthesis "
                         "becomes <. Test membership mechanically: −1 "
                         "satisfies −1 ≤ −1 (member), 4 fails 4 < 4 (not "
                         "a member), 2.5 satisfies both (member). "
                         "Translate back: {x : x ≤ 3} becomes (−∞, 3] - "
                         "the ray with a sealed endpoint. Form a union: "
                         "[0, 1] ∪ [2, 3] shades two disjoint stretches, "
                         "and 1.5, lying in the gap, belongs to neither "
                         "piece and hence not to the union."),
        "key_points": [
            "[−1, 4) = {x : −1 ≤ x < 4}: bracket seals in, parenthesis holds out.",
            "Set-builder reads 'the set of x such that ...'.",
            "Membership is mechanical: test the endpoint inequalities.",
            "{x : x ≤ 3} is the ray (−∞, 3].",
            "Unions join stretches: [0, 1] ∪ [2, 3] is two shaded pieces.",
        ],
        "requirements": [
            "The interval record: brackets and endpoints.",
            "The inequality symbols ≤ and <.",
        ],
        "standards": [
            "CCSS.MATH.CONTENT.HSA-CED - set and interval language for solution sets.",
            "ISO 80000-2:2019 - set-builder and interval notation.",
        ],
        "citations": [CIT_CCSS, CIT_ISO80000, CIT_RUDIN],
        "sig_lens": ("His Signature reading: notation is the muster-roll "
                     "script of the line - each interval entered by its "
                     "boundary terms, each member checkable against the "
                     "written oath. In the Signature method [−1, 4) is a "
                     "charter: −1 sworn in by the square bracket, 4 "
                     "dismissed by the round, and every value between "
                     "claimed in the set's name."),
    },
    {
        "key": "nl_interval_arith",
        "name": "Interval Arithmetic",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": ("Intervals can be added, subtracted, multiplied, "
                        "and divided as whole objects: [1, 2] + [3, 5] = "
                        "[4, 7], because the smallest possible sum is "
                        "1 + 3 and the largest is 2 + 5. Multiplication "
                        "takes the extremes of the four endpoint "
                        "products: [1, 2] × [−1, 3] = [−2, 6], since the "
                        "products 1×(−1), 1×3, 2×(−1), 2×3 range from "
                        "−2 to 6. This is honest arithmetic with "
                        "uncertainty: if a measurement lies somewhere in "
                        "[1, 2] and another in [3, 5], their sum lies "
                        "somewhere in [4, 7] - guaranteed, no statistics "
                        "needed. Engineers use it for tolerance "
                        "analysis (worst-case stacks), computers use it "
                        "for rigorous error bounds, and the line "
                        "pictures it perfectly: operate on the "
                        "endpoints, shade the result. Subtraction is "
                        "adding the negated interval; division by an "
                        "interval containing zero is forbidden, the old "
                        "ban in a new uniform."),
        "how_it_works": ("Add intervals endpoint-wise: [a, b] + [c, d] = "
                         "[a+c, b+d]. Work [1, 2] + [3, 5] = [4, 7] - "
                         "verify: 1.5 + 4 = 5.5 lands inside, and no sum "
                         "escapes the bounds. Multiply by endpoint "
                         "extremes: [1, 2] × [−1, 3] - the four products "
                         "are −1, 3, −2, 6, so the result is [−2, 6]; "
                         "verify 1.5 × 2 = 3 lands inside. Subtract by "
                         "negation: [1, 2] − [3, 5] = [1, 2] + [−5, −3] "
                         "= [−4, −1] - verify 1 − 5 = −4 at the edge. "
                         "Note the zero ban: [1, 2]/[−1, 1] is refused, "
                         "since the divisor interval straddles 0."),
        "key_points": [
            "[a, b] + [c, d] = [a+c, b+d]: [1, 2] + [3, 5] = [4, 7].",
            "Multiplication takes min/max of the four endpoint products: [1, 2] × [−1, 3] = [−2, 6].",
            "Interval arithmetic is guaranteed arithmetic with uncertainty.",
            "Subtraction negates then adds: [1, 2] − [3, 5] = [−4, −1].",
            "Division by an interval containing zero is forbidden.",
        ],
        "requirements": [
            "Interval endpoints and the inclusion property.",
            "The four-products rule for multiplication.",
        ],
        "standards": [
            "IEEE 1788-2015 - interval arithmetic standard.",
            "NCTM Principles to Actions - operating on ranges.",
        ],
        "citations": [CIT_CCSS, CIT_NCTM, CIT_RUDIN],
        "sig_lens": ("His Signature reading: interval arithmetic is the "
                     "line mustering whole companies at once - not one "
                     "value marching but the entire stretch, endpoints "
                     "leading, every member following inside the "
                     "guaranteed bounds. In the Signature method this "
                     "is the honest way to compute with uncertainty: "
                     "the result-interval swears that the true answer "
                     "stands somewhere within its posts."),
    },
    {
        "key": "nl_abs_ineq",
        "name": "Absolute Value Inequalities as Intervals",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": ("|x − 4| < 2 says 'the distance from x to 4 is "
                        "less than 2' - and the line shows the answer "
                        "at once: every point within 2 steps of 4, the "
                        "open interval (2, 6). The translation rule is "
                        "mechanical: |x − a| < d becomes the interval "
                        "(a−d, a+d); |x − a| ≤ d becomes [a−d, a+d]; "
                        "with > the answer is two rays, (−∞, a−d) ∪ "
                        "(a+d, ∞). Solve |2x − 6| ≤ 4 by isolating the "
                        "bars: |x − 3| ≤ 2, so x ∈ [1, 5] - verify: x = "
                        "1 gives |2−6| = 4 ≤ 4, true; x = 0 gives 6 ≤ 4, "
                        "false. This is the language of tolerances: 'the "
                        "part must measure 4 cm within 2 mm' is "
                        "|x − 4| ≤ 0.2, the interval [3.8, 4.2]. "
                        "Absolute value turns distance conditions into "
                        "shading, and shading into intervals."),
        "how_it_works": ("Read |x − a| < d as 'within d of a' and mark "
                         "the interval (a−d, a+d). For |x − 4| < 2: "
                         "center 4, radius 2 - the open interval (2, 6). "
                         "Test: x = 3 gives |3−4| = 1 < 2 (inside, "
                         "member); x = 7 gives 3 < 2 false (outside). "
                         "Solve |2x − 6| ≤ 4: divide inside to |x − 3| "
                         "≤ 2, giving [1, 5]. Verify endpoints: x = 1 "
                         "gives |2−6| = 4 ≤ 4 (sealed in by ≤); x = 5 "
                         "gives |10−6| = 4 ≤ 4 (also in)."),
        "key_points": [
            "|x − 4| < 2 means 'within 2 of 4': the interval (2, 6).",
            "|x − a| < d translates to (a−d, a+d).",
            "|2x − 6| ≤ 4 solves to x ∈ [1, 5].",
            "With > the solution is two rays: (−∞, a−d) ∪ (a+d, ∞).",
            "Tolerances are absolute-value inequalities: |x − 4| ≤ 0.2 is [3.8, 4.2].",
        ],
        "requirements": [
            "Absolute value as distance from the earlier record.",
            "Isolating the bars before translating.",
        ],
        "standards": [
            "CCSS.MATH.CONTENT.HSA-REI - solving absolute value inequalities.",
            "ISO 80000-2:2019 - absolute value and interval notation.",
        ],
        "citations": [CIT_CCSS, CIT_ISO80000, CIT_STEWART],
        "sig_lens": ("His Signature reading: an absolute-value "
                     "inequality is a decree of neighborhood - the "
                     "center named, the radius sworn, every value "
                     "within the sworn distance claimed. In the "
                     "Signature method |x − 4| < 2 raises the interval "
                     "(2, 6) like a banner around the post at 4, and "
                     "the line witnesses each member's distance "
                     "personally."),
    },
    {
        "key": "nl_plane",
        "name": "The Number Line in the Cartesian Plane",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": ("Cross two number lines at their origins - one "
                        "horizontal (the x-axis), one vertical (the "
                        "y-axis) - and every point of the plane gets an "
                        "address (x, y). The point (3, −2) stands above "
                        "the 3-mark of the x-axis and below the −2-mark "
                        "of the y-axis, in the fourth quadrant. Distance "
                        "from the origin follows the line's own ruler "
                        "twice: the legs 3 and 2 form a right triangle, "
                        "so the distance is √(3² + 2²) = √13 ≈ 3.6055 - "
                        "the Pythagorean theorem built from two "
                        "one-dimensional measurements. The axes divide "
                        "the plane into four quadrants, named by the "
                        "signs (+,+), (−,+), (−,−), (+,−). Every graph "
                        "ever drawn - every function curve, every data "
                        "plot, every map - is ink on this crossed pair "
                        "of number lines. The line did not end at one "
                        "dimension; it multiplied."),
        "how_it_works": ("Draw the x-axis horizontal and the y-axis "
                         "vertical, crossing at the shared origin. Plot "
                         "(3, −2): walk 3 right on the x-axis, then 2 "
                         "down parallel to the y-axis, and mark the "
                         "point. Compute its distance from the origin: "
                         "the horizontal leg is 3 steps, the vertical "
                         "leg is 2 steps, so by Pythagoras the distance "
                         "is √(9 + 4) = √13 ≈ 3.6055 - verify 3.6055² = "
                         "12.9996, within 0.001 of 13. Name the "
                         "quadrant: x positive, y negative - the fourth "
                         "quadrant."),
        "key_points": [
            "Two crossed number lines make the Cartesian plane; (x, y) is the address.",
            "(3, −2) is 3 right on the x-axis, 2 down on the y-axis.",
            "Distance from origin: √(x² + y²) = √13 ≈ 3.6055.",
            "Signs name the quadrant: (+,−) is the fourth.",
            "Every graph is ink on crossed number lines.",
        ],
        "requirements": [
            "Both axes with a shared, labeled origin.",
            "The Pythagorean theorem for the distance.",
        ],
        "standards": [
            "CCSS.MATH.CONTENT.6.NS.C.6b - the coordinate plane.",
            "CCSS.MATH.CONTENT.8.G.B.8 - distance between two points.",
        ],
        "citations": [CIT_CCSS, CIT_APOSTOL, CIT_STEWART],
        "sig_lens": ("His Signature reading: the plane is two sworn "
                     "lines crossing at the signet - the x-line keeping "
                     "its horizontal oath, the y-line its vertical, "
                     "their crossing witnessed as the origin of "
                     "origins. In the Signature method every plane "
                     "point carries a double testimony, one from each "
                     "axis, and the distance √(x² + y²) is the two "
                     "witnesses agreeing on a single separation."),
    },
    {
        "key": "nl_measurement",
        "name": "Number Lines in Measurement: Timelines, Scales, and Gauges",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": ("The number line left mathematics long ago and "
                        "went to work: a timeline is a number line whose "
                        "marks are years - 1969 to 2026 spans 57 years, "
                        "read straight off the axis. A thermometer is a "
                        "vertical number line in degrees: from −10°C to "
                        "25°C is a 35-degree span. A speedometer, a fuel "
                        "gauge, a pressure dial - each is a bent or "
                        "circular number line, mapping a quantity to a "
                        "needle position by the same value-to-position "
                        "rule as the coordinate axis. Reading any of "
                        "them is the foundations skill - find the "
                        "neighboring marks, judge the fraction - and "
                        "their errors are interval thinking: a gauge "
                        "reading 60 with ±2 accuracy names the interval "
                        "[58, 62]. Whenever a quantity varies along one "
                        "dimension - time, temperature, pressure, speed "
                        "- the number line is the instrument beneath "
                        "the instrument."),
        "how_it_works": ("Read a timeline as a number line in years: "
                         "place 1969 and 2026 as marks and count the "
                         "span - 2026 − 1969 = 57 years. Read a "
                         "thermometer as a vertical line: the span from "
                         "−10°C to 25°C is 25 − (−10) = 35 degrees. "
                         "Calibrate a gauge by the axis rule: position = "
                         "base + value × scale, exactly the pixel "
                         "mapping from the coordinate record. Express "
                         "accuracy as an interval: a ±2 reading at 60 "
                         "names [58, 62], and any true value inside "
                         "passes, any outside fails."),
        "key_points": [
            "A timeline is a number line in years: 1969 to 2026 spans 57 years.",
            "A thermometer is a vertical number line: −10°C to 25°C spans 35 degrees.",
            "Gauges map quantity to needle by position = base + value × scale.",
            "Reading any scale is the read-a-point skill with finer marks.",
            "Accuracy ±2 at 60 names the interval [58, 62].",
        ],
        "requirements": [
            "The axis mapping: value to position by base + value × scale.",
            "Real instruments: timeline, thermometer, gauge.",
        ],
        "standards": [
            "CCSS.MATH.CONTENT.2.MD - measurement and data with scales.",
            "NCTM Principles to Actions - measurement as number-line application.",
        ],
        "citations": [CIT_CCSS, CIT_NCTM, CIT_DEVLIN],
        "sig_lens": ("His Signature reading: every gauge and timeline "
                     "is the line in working uniform - the same sworn "
                     "order of positions, now measuring years, degrees, "
                     "and pressure for the world. In the Signature "
                     "method the instrument is honest exactly when its "
                     "marks keep the line's oath: equal steps, true "
                     "origin, and every reading witnessed against its "
                     "neighbors."),
    },
    {
        "key": "nl_limits",
        "name": "Limits: Approaching a Point on the Line",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": ("A limit is a destination approached but not "
                        "always reached: the sequence 1, 1/2, 1/3, 1/4, "
                        "... marches leftward toward 0, each term closer "
                        "than the last, without ever landing on it. The "
                        "precise claim: for any tiny tolerance ε, some "
                        "term - and every term after - lies within ε of "
                        "0. Take ε = 0.001: the 2000th term is 0.0005, "
                        "inside the tolerance, and all later terms are "
                        "closer still. On the line this is visible as "
                        "marks piling up against a barrier point, the "
                        "gaps shrinking past every magnifier. Limits are "
                        "the doorway to calculus: the derivative is a "
                        "limit of slopes, the integral a limit of sums, "
                        "and both are statements about points on the "
                        "line being approached arbitrarily closely. "
                        "Zeno's old paradoxes dissolve here - infinite "
                        "steps can approach a finite post."),
        "how_it_works": ("List the sequence 1/n on the line: marks at 1, "
                         "0.5, 0.333, 0.25, ... crowding toward 0 from "
                         "the right. Test the ε-challenge with ε = "
                         "0.001: solve 1/n < 0.001 to get n > 1000, so "
                         "the 2000th term 0.0005 is inside - and every "
                         "later term is smaller, hence closer. Verify "
                         "monotonic approach: each term 1/(n+1) < 1/n, "
                         "so the marks never retreat. State the limit: "
                         "lim(n→∞) 1/n = 0 - the barrier point the marks "
                         "approach but never occupy."),
        "key_points": [
            "1, 1/2, 1/3, ... approaches 0 without ever reaching it.",
            "ε = 0.001 is beaten by the 2000th term (0.0005) and all after.",
            "The marks pile against the barrier point, gaps shrinking past every magnifier.",
            "Limits are the doorway to derivatives and integrals.",
            "Infinite steps can approach a finite post.",
        ],
        "requirements": [
            "The sequence terms marked in order on the line.",
            "The ε-challenge: name a tolerance, find the term that beats it.",
        ],
        "standards": [
            "CCSS.MATH.CONTENT.HSF-IF - sequences and the limit idea in functions.",
            "NCTM Principles to Actions - limits as the calculus foundation.",
        ],
        "citations": [CIT_NCTM, CIT_APOSTOL, CIT_RUDIN],
        "sig_lens": ("His Signature reading: a limit is the long "
                     "approach march - term after term advancing on a "
                     "post it never occupies, each step sworn closer "
                     "than the last. In the Signature method the "
                     "ε-challenge is the line's honor test: name any "
                     "tolerance, however small, and the sequence "
                     "produces a term inside it, with every follower "
                     "closer still - witnessed, not merely claimed."),
    },
    {
        "key": "nl_functions",
        "name": "Functions as Mappings Along the Line",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": ("A function is a rule that moves every point of "
                        "the line to a new address: f(x) = 2x + 1 sends "
                        "−2 to −3, −1 to −1, 0 to 1, 1 to 3, 2 to 5 - "
                        "each input marched to its output by doubling "
                        "and adding one. Draw the inputs on one line and "
                        "the outputs on a second, and the function is "
                        "the bundle of arrows between them; draw it on "
                        "the plane and it becomes the familiar graph. "
                        "The domain is where the arrows start "
                        "(here, all reals), the range where they land "
                        "(all reals again, since 2x + 1 hits every "
                        "value). Composition chains the marches: apply "
                        "g then f and the line carries points through "
                        "both moves in order. Inverses march backward: "
                        "f⁻¹ undoes 2x + 1 via (x − 1)/2, returning 5 to "
                        "2. Functions are the line in motion - the "
                        "study of how positions transform."),
        "how_it_works": ("Apply f(x) = 2x + 1 to sample inputs and mark "
                         "each output: f(−2) = −3, f(−1) = −1, f(0) = 1, "
                         "f(1) = 3, f(2) = 5 - verify each by arithmetic. "
                         "Draw the mapping: two parallel lines, arrows "
                         "from each input mark to its output mark - the "
                         "arrows never cross for this function, showing "
                         "order preserved. Find the range: solve y = 2x "
                         "+ 1 for x = (y − 1)/2 - every y has a source, "
                         "so the range is all reals. Undo it: apply "
                         "(x − 1)/2 to 5 and recover 2, the inverse "
                         "marching the point home."),
        "key_points": [
            "f(x) = 2x + 1 maps −2→−3, −1→−1, 0→1, 1→3, 2→5.",
            "A function is arrows from an input line to an output line.",
            "Domain: where arrows start; range: where they land.",
            "Composition chains mappings; inverses march backward.",
            "The inverse of 2x + 1 is (x − 1)/2: 5 returns to 2.",
        ],
        "requirements": [
            "Input and output lines (or the plane) for the arrows.",
            "Sample inputs evaluated by the rule.",
        ],
        "standards": [
            "CCSS.MATH.CONTENT.HSF-IF.A.1 - function as a mapping between sets.",
            "CCSS.MATH.CONTENT.8.F.A.1 - functions as rules assigning outputs.",
        ],
        "citations": [CIT_CCSS, CIT_APOSTOL, CIT_STEWART],
        "sig_lens": ("His Signature reading: a function is a marching "
                     "order issued to the whole line - every post "
                     "abandoned and reoccupied at its assigned new "
                     "address, none left behind, none doubled up. In "
                     "the Signature method the arrows are the orders "
                     "themselves, witnessed from input line to output "
                     "line, and the inverse is the recall: every point "
                     "marched home to the post it started from."),
    },
    {
        "key": "nl_infinity",
        "name": "Infinite Intervals and the Idea of Infinity",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": ("Some stretches of the line never end: [3, ∞) "
                        "is every number from 3 onward, forever - a ray "
                        "with a sealed start and no finish. The ∞ symbol "
                        "is not a number but a direction-word: 'and so "
                        "on without bound'. The ray always has room: "
                        "name any M, however huge, and M + 1 also "
                        "belongs - 10¹² is in [3, ∞), and so is 10¹² + "
                        "1. That unboundedness is provable on the line: "
                        "no finite endpoint can contain the ray, because "
                        "adding 1 steps past any candidate bound. The "
                        "whole line itself is (−∞, ∞), unbounded both "
                        "ways. Infinity also names sizes of sets - the "
                        "integers and the rationals are both infinite, "
                        "yet the reals are a strictly larger infinity - "
                        "but on the line, infinity first of all means "
                        "the arrow: the sworn oath, from the very first "
                        "record, that the order continues."),
        "how_it_works": ("Shade the ray [3, ∞): solid dot at 3, shading "
                         "right with an arrowhead for 'without end'. "
                         "Test membership: 10¹² ≥ 3, so it belongs; 2 "
                         "< 3, so it does not. Prove unboundedness: "
                         "suppose B were the largest member - then B + 1 "
                         "is larger and still ≥ 3, contradiction, so no "
                         "largest member exists. Name the whole line "
                         "(−∞, ∞): shade everything, arrowheads both "
                         "ways. Distinguish the symbol from a number: "
                         "∞ + 1 is meaningless as arithmetic - ∞ marks "
                         "direction, not an address."),
        "key_points": [
            "[3, ∞) is every number from 3 onward, without end.",
            "∞ is a direction-word ('without bound'), not a number.",
            "Any bound fails: if B were largest, B + 1 contradicts it.",
            "The whole line is (−∞, ∞), unbounded both ways.",
            "∞ + 1 is meaningless: infinity is not an address.",
        ],
        "requirements": [
            "The ray shaded with its arrowhead.",
            "The B + 1 contradiction for unboundedness.",
        ],
        "standards": [
            "CCSS.MATH.CONTENT.HSN-RN - extended real line and infinity notation.",
            "ISO 80000-2:2019 - the infinity symbol ∞.",
        ],
        "citations": [CIT_CCSS, CIT_ISO80000, CIT_RUDIN],
        "sig_lens": ("His Signature reading: the infinite ray is the "
                     "line's oldest oath made visible - the arrowhead "
                     "drawn in the very first record, swearing the "
                     "order continues past every bound. In the "
                     "Signature method no finite challenger can close "
                     "the ray: name your largest, and the line answers "
                     "with one more - witnessed, unstoppable, without "
                     "end."),
    },
    {
        "key": "nl_continuity",
        "name": "The Number Line as a Model of Continuity",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": ("The finished line - complete, ordered, dense - "
                        "is mathematics' model of the continuum: "
                        "unbroken, with no gaps and no jumps. Its "
                        "crowning property is the intermediate value "
                        "theorem: a continuous march from one value to "
                        "another passes through every value between. "
                        "Watch it work: f(x) = x³ − 2 runs from f(1) = "
                        "−1 to f(2) = 6, so somewhere between 1 and 2 "
                        "it must cross 0 - and bisection finds the "
                        "crossing at about 1.2599, the cube root of 2 "
                        "(1.2599³ ≈ 1.99996). That crossing is "
                        "guaranteed by the line having no holes: on the "
                        "rationals alone the march could leap the gap, "
                        "but the complete line cannot. Continuity is "
                        "why calculus trusts the line - derivatives and "
                        "integrals are limits taken along an unbroken "
                        "rail. Thirty-four records up the ladder, the "
                        "line that began as counting marks is revealed "
                        "as the continuum: the single instrument on "
                        "which number, order, distance, and change all "
                        "play."),
        "how_it_works": ("Verify the sign change: f(1) = 1 − 2 = −1 "
                         "(below zero), f(2) = 8 − 2 = 6 (above zero) - "
                         "a continuous function must cross between. "
                         "Bisect for the crossing: f(1.5) = 3.375 − 2 = "
                         "1.375 > 0, keep (1, 1.5); f(1.25) = 1.953 − 2 "
                         "= −0.047 < 0, keep (1.25, 1.5); continue to "
                         "1.25992, where f is within 0.0001 of zero. State "
                         "the theorem: because "
                         "the line has no gaps, the crossing point is "
                         "a genuine address - the cube root of 2, "
                         "witnessed at about 1.2599."),
        "key_points": [
            "The complete line is the model of the continuum: no gaps, no jumps.",
            "Intermediate value theorem: a continuous march hits every value between.",
            "f(x) = x³ − 2 goes from −1 to 6, so it crosses 0 between 1 and 2.",
            "Bisection locates the crossing at about 1.2599 (cube root of 2).",
            "On the rationals alone the march could leap the gap; completeness forbids it.",
        ],
        "requirements": [
            "A continuous function with a sign change on an interval.",
            "Bisection to trap the crossing point.",
        ],
        "standards": [
            "CCSS.MATH.CONTENT.HSF-IF - continuity and the intermediate value idea.",
            "NCTM Principles to Actions - the continuum as calculus foundation.",
        ],
        "citations": [CIT_DEDEKIND, CIT_RUDIN, CIT_APOSTOL],
        "sig_lens": ("His Signature reading: continuity is the line's "
                     "final oath kept - the unbroken rail from the "
                     "counting marks of the first record to the "
                     "continuum of the last, sworn complete at every "
                     "rung. In the Signature method the intermediate "
                     "value theorem is the muster of the whole ladder: "
                     "every record's witnessing gathered into one "
                     "guarantee - march continuously from −1 to 6 and "
                     "the line itself certifies the crossing."),
    },
]

assert len(ENTRIES) == 34, "expected 34 entries, got %d" % len(ENTRIES)
ranks = [e["ladder_rank"] for e in ENTRIES]
assert ranks == sorted(ranks), "entries not in ladder order"
tiers = [e["ladder_tier"] for e in ENTRIES]
assert tiers == sorted(tiers, key=("foundations", "compounded", "advanced").index), "tier order broken"
assert all(1 <= r <= 10 for r in ranks), "rank out of range"
