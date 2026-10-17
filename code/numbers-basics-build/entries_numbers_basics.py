#!/usr/bin/env python3
"""Entries for The Numbers Basics Database (fundamentals order #9, 2026-10-17).

First-principles number teaching for a learner who knows nothing: what
numbers are, counting, number sense, the number line, numerals and words,
comparing and ordering, place value, even and odd, addition, subtraction,
multiplication, division, fractions as parts, decimals, money, rounding,
patterns, primes, measuring, word problems, negative numbers, properties
of operations, checking work, and the big picture.

34 records each, teaching-ladder ordered (ladder_rank 1-10, non-decreasing;
foundations -> compounded -> advanced). Public records are real,
fact-checked foundational mathematics (standard references: NCTM
Principles to Actions; Common Core State Standards for Mathematics,
domains K.CC, K.OA, 1.OA, 2.NBT, 3.OA, 3.NF, 4.NBT, 4.NF, 5.NBT; Dehaene
S. The Number Sense. Oxford University Press; 2011; Butterworth B. The
Mathematical Brain. Macmillan; 1999; Van de Walle JA et al. Elementary
and Middle School Mathematics. 10th ed. Pearson; 2019). Signature
editions carry the same ladder through the Signature lens: numbers as
his covenant of counted things, the ladder as the Signature ascent, each
operation an oath kept. src signature, titles suffixed " (Signature
Edition)", clearly labeled Signature-made, never presented as authentic
public record.

ID prefixes: JAH-NUMB- (public) and JAH-NUMBS- (signature), verified free
in the manifest id_prefix values and in every shard index file
(zero hits for JAH-NUMB).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_numbers_basics.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature number method: "
            "numbers as the covenant of counted things, the teaching ladder "
            "as the Signature ascent from knowing nothing to knowing truly, "
            "each operation an oath kept between the learner and the count. "
            "Clearly labeled Signature-made, never presented as authentic "
            "public record.")

CIT_NCTM = ("National Council of Teachers of Mathematics. Principles to "
            "Actions: Ensuring Mathematical Success for All. NCTM; 2014.")
CIT_CCSS = ("National Governors Association Center for Best Practices, "
            "Council of Chief State School Officers. Common Core State "
            "Standards for Mathematics. Domains K.CC Counting and "
            "Cardinality, K.OA Operations and Algebraic Thinking, 1.OA, "
            "2.NBT Number and Operations in Base Ten, 3.OA, 3.NF Number and "
            "Operations - Fractions, 4.NBT, 4.NF, 5.NBT; 2010.")
CIT_DEHAENE = ("Dehaene S. The Number Sense: How the Mind Creates "
               "Mathematics. 2nd ed. Oxford University Press; 2011.")
CIT_BUTTERWORTH = ("Butterworth B. The Mathematical Brain. Macmillan; 1999.")
CIT_VANDEWALLE = ("Van de Walle JA, Karp KS, Bay-Williams JM. Elementary and "
                  "Middle School Mathematics: Teaching Developmentally. "
                  "10th ed. Pearson; 2019.")

ENTRIES = [
    {
        "key": "what_is_number",
        "name": "What a Number Is",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "A number is an idea that answers the question 'how many'. Before "
            "numbers, people could point at a pile of stones and say 'many' "
            "or 'few', but they could not say exactly how many without "
            "counting one by one. A number is what is left when you forget "
            "everything about a pile of things except how many things it "
            "holds: three apples and three stones and three clouds share the "
            "same threeness, and that threeness is the number three. Numbers "
            "do not live in the apples or the stones; they live in the "
            "matching. When every apple can be paired with exactly one "
            "stone and none are left over, the two piles share a number. "
            "Zero is the number for an empty pile, the honest answer to "
            "'how many' when there is nothing there. One is the number for "
            "a single thing. From there the counting numbers go on without "
            "end: two, three, four, and so on, each one meaning one more "
            "than the last. Every later idea in this database - adding, "
            "subtracting, multiplying, dividing, fractions, decimals - is "
            "built on this one foundation: a number is a precise answer to "
            "'how many'."
        ),
        "how_it_works": (
            "A number works by standing for a matched pile. Put ten pebbles "
            "in a row and touch each one exactly once, saying the count "
            "words in order: one, two, three, four, five, six, seven, eight, "
            "nine, ten. The last word you say, ten, is the number of the "
            "pile. Now take the pebbles away and the number ten remains as "
            "a thought you can carry anywhere - you can say 'ten' without "
            "any pebbles present, and anyone who understands numbers knows "
            "exactly what you mean. That is the whole trick: numbers let "
            "people agree about quantities without pointing at the objects. "
            "The demonstration program proves the matching: it builds a "
            "pile of ten pebbles, counts them one by one with no repeats "
            "and no skips, and checks that the count reached equals the "
            "pile size, so the number earned is exactly ten."
        ),
        "key_points": [
            "A number is a precise answer to 'how many' - it is what two piles share when every item in one can be paired with exactly one item in the other.",
            "Numbers are ideas, not objects: the number three lives in the matching of three apples with three stones, not in the apples or the stones.",
            "Zero is the number for an empty pile, the honest answer when there is nothing to count.",
            "The counting numbers go on without end, each one exactly one more than the last - there is no largest number.",
        ],
        "requirements": [
            "A pile of distinct objects to count, with each object touched exactly once.",
            "An ordered sequence of count words (one, two, three, ...) memorized in fixed order.",
            "No skipping and no double-counting - the match must be one-to-one.",
        ],
        "standards": ["CCSS K.CC.1, K.CC.4 - counting and cardinality."],
        "citations": [CIT_CCSS, CIT_DEHAENE, CIT_BUTTERWORTH],
        "sig_lens": (
            "Through the Signature lens, a number is the covenant of counted "
            "things: when he counts a pile, the number he speaks is his oath "
            "that the count is true. Threeness is the Signature bond between "
            "any three things anywhere - the bond does not change when the "
            "things change, and that unchanging bond is what makes numbers "
            "trustworthy. Zero is his honest ledger entry for nothing held."
        ),
    },
    {
        "key": "counting_first_skill",
        "name": "Counting: The First Skill",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Counting is the first skill every number learner must master, "
            "and it has five strict rules. First, the count words must come "
            "in the same order every time: one, two, three, never two, one, "
            "three. Second, each object gets exactly one word - no skipping, "
            "no doubling. Third, the last word said is the answer: if you "
            "finish on 'twelve', there are twelve. Fourth, it does not "
            "matter where you start in the pile or which object you touch "
            "first. Fifth, it does not matter what the objects are - twelve "
            "apples, twelve stones, or twelve mixed toys all count to "
            "twelve. Children who can recite the words but hand out two "
            "words to one toy have not yet learned counting; they have "
            "learned a song. Real counting is the one-to-one match of words "
            "to things, and the last word is the total. When the rules are "
            "kept, counting is proof: nobody can argue with a pile that "
            "was counted one by one."
        ),
        "how_it_works": (
            "Counting works by pairing. Line up twelve pebbles. Point at "
            "one and say 'one'. Move to the next and say 'two'. Keep going "
            "until every pebble has been pointed at once. The word you said "
            "on the last pebble - 'twelve' - is how many pebbles there are. "
            "To check the work, count again starting from a different "
            "pebble, or have someone else count. If every count ends on "
            "'twelve', the answer is certain. The demonstration program "
            "performs a true machine count of twelve items: it assigns each "
            "item exactly one number in order, verifies no item was counted "
            "twice and none was missed, and asserts the final count equals "
            "twelve, then proves recounting from a different starting point "
            "gives the same total."
        ),
        "key_points": [
            "Count words must always come in the same fixed order, and each object gets exactly one word.",
            "The last count word spoken is the total - this is the cardinality rule, the whole point of counting.",
            "Order of touching and the kind of objects do not change the count.",
            "Recounting from a different starting point checks the work and always gives the same total when the rules were kept.",
        ],
        "requirements": [
            "The ordered count-word sequence memorized: one through at least twenty.",
            "One-to-one matching of each word to exactly one object.",
            "Touching or pointing to track which objects are already counted.",
        ],
        "standards": ["CCSS K.CC.1 through K.CC.5 - counting and cardinality."],
        "citations": [CIT_CCSS, CIT_VANDEWALLE, CIT_BUTTERWORTH],
        "sig_lens": (
            "Through the Signature lens, counting is the first oath kept: "
            "one word, one thing, no more, no less. He who keeps the five "
            "rules of counting has made his first true contract with "
            "numbers, and every later operation is just a faster way of "
            "keeping that same contract."
        ),
    },
    {
        "key": "number_line",
        "name": "The Number Line",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The number line is a straight line with numbers placed along "
            "it in order, evenly spaced: zero at one end, then one, two, "
            "three, marching to the right without end. It turns counting "
            "into geography. A number's position on the line shows its "
            "size: numbers to the right are bigger, numbers to the left "
            "are smaller. The distance between two numbers is the number of "
            "steps between them - from three to eight is five steps. Moving "
            "right one step adds one; moving left one step takes one away. "
            "The number line is the first map of all mathematics, and it "
            "never stops being useful: fractions live between the whole "
            "numbers on it, decimals live there too, and negative numbers "
            "extend it left past zero. Learn to see numbers as places on "
            "this line, and comparing, adding, and subtracting become "
            "visible as movement."
        ),
        "how_it_works": (
            "The number line works by giving every number an address. Draw "
            "a line, mark evenly spaced points, and label them 0, 1, 2, 3, "
            "up to 10. The number seven lives at the seventh mark. The "
            "distance between three and eight is found by counting the "
            "steps from one mark to the other: five steps, so the distance "
            "is five. To add two plus three, start at two and hop right "
            "three steps; you land on five. To subtract eight minus three, "
            "start at eight and hop left three steps; you land on five. The "
            "demonstration program builds the line from zero to ten, finds "
            "the address of seven, measures the step distance between three "
            "and eight, and asserts it equals five, then walks two plus "
            "three as hops and verifies the landing point is five."
        ),
        "key_points": [
            "Numbers sit on the line in order with equal spacing; position is size.",
            "Moving right adds, moving left subtracts - addition and subtraction are visible as hops.",
            "The distance between two numbers is the count of steps between their marks.",
            "The line extends left past zero for negatives and holds fractions and decimals between the whole numbers.",
        ],
        "requirements": [
            "Numbers in their fixed counting order to label the marks.",
            "Equal spacing between consecutive marks - a crooked line lies.",
            "A chosen zero point and a direction (rightward is standard).",
        ],
        "standards": ["CCSS K.CC.7, 1.OA, 2.MD.6 - comparing and the number line."],
        "citations": [CIT_CCSS, CIT_DEHAENE, CIT_VANDEWALLE],
        "sig_lens": (
            "Through the Signature lens, the number line is the first road "
            "of the Signature ascent: zero is the trailhead, and every step "
            "right is one more kept promise. Hops are his strides - add by "
            "walking forward, subtract by walking back, and the road never "
            "lies about where you land."
        ),
    },
    {
        "key": "numerals_words",
        "name": "Writing Numerals and Number Words",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Numbers have three faces: the spoken word ('seven'), the "
            "written word ('seven'), and the numeral ('7'). The numeral "
            "system we use has ten digit symbols - 0, 1, 2, 3, 4, 5, 6, 7, "
            "8, 9 - and every larger number is written by combining them. "
            "The spoken and written words are language; the numerals are "
            "mathematics. A learner must be able to move between all three "
            "faces freely: hear 'seven', write 7; see 7, say 'seven'. The "
            "number words from eleven to nineteen are the tricky patch - "
            "'eleven', 'twelve', 'thirteen' through 'nineteen' do not sound "
            "like their tens and ones, so they must be memorized. From "
            "twenty on, the pattern is honest again: twenty-one, "
            "twenty-two, thirty-five. The numerals from 0 to 20 should be "
            "read and written without hesitation before any further ladder "
            "climbing, because every later skill - place value, addition, "
            "subtraction - assumes these faces are recognized instantly."
        ),
        "how_it_works": (
            "The numeral system works by symbol agreement: everyone who "
            "learns it agrees that the curved shape '7' stands for the "
            "quantity seven. Writing a number means choosing the right "
            "symbols; reading a number means turning the symbols back into "
            "the quantity. The translation between words and numerals is "
            "tested both ways: given the word 'fourteen', write 14; given "
            "14, say 'fourteen'. For two-digit numbers the spoken word "
            "carries the structure - 'twenty-one' names the tens word then "
            "the ones word. The demonstration program holds the complete "
            "word-to-numeral table for zero through twenty, translates every "
            "word to its numeral and back, asserts each round trip returns "
            "the original, and verifies that the teen words map to their "
            "correct numerals with no confusion."
        ),
        "key_points": [
            "Every number has three faces - spoken word, written word, numeral - and fluency means moving freely between them.",
            "Ten digit symbols (0-9) combine to write every number in the system.",
            "The teen words (eleven through nineteen) break the pattern and must be memorized as special cases.",
            "Instant recognition of numerals 0 to 20 is the gateway to place value and all arithmetic.",
        ],
        "requirements": [
            "The ten digit symbols memorized by shape and name.",
            "The number words from zero to twenty, including the teen exceptions.",
            "The tens words: twenty, thirty, forty, fifty, sixty, seventy, eighty, ninety.",
        ],
        "standards": ["CCSS K.CC.3 - writing numerals; K.CC.4 - naming quantities."],
        "citations": [CIT_CCSS, CIT_VANDEWALLE],
        "sig_lens": (
            "Through the Signature lens, each numeral is a mark of his "
            "house: ten signs, and with ten signs he can name any quantity "
            "that exists. The words are the voice of the covenant and the "
            "numerals are its seal - a learner who can speak, write, and "
            "seal a number has taken the mark three ways at once."
        ),
    },
    {
        "key": "more_less_same",
        "name": "More, Less, and the Same",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Comparing is deciding which of two piles holds more, which "
            "holds less, and whether they hold the same. The oldest method "
            "is matching: pair each apple with one stone; the pile with "
            "leftovers is more. When both run out together, the piles are "
            "the same. Once numbers are known, comparing becomes faster: "
            "count each pile, then compare the counts. Nine is more than "
            "seven, seven is less than nine, and seven is the same as "
            "seven. Three symbols make the verdict permanent: > means "
            "'is greater than' (9 > 7), < means 'is less than' (7 < 9), and "
            "= means 'is equal to' (7 = 7). The hungry-mouth trick helps "
            "remember which is which: the open mouth of > and < always "
            "faces the bigger number, because it wants to eat the larger "
            "pile. Comparing is the skill behind every later decision: "
            "which price is lower, which team scored more, whether you "
            "have enough."
        ),
        "how_it_works": (
            "Comparing works by count-then-decide. Count pile A: nine "
            "pebbles. Count pile B: seven pebbles. Compare the counts: "
            "nine comes after seven in the counting order, so nine is more "
            "and seven is less - 9 > 7, and the same fact reversed is 7 < "
            "9. For equality, count pile C: seven pebbles. Seven and seven "
            "match exactly, so 7 = 7. On the number line this is geography: "
            "nine sits to the right of seven, so nine is greater. The "
            "demonstration program counts two piles of nine and seven "
            "items, compares the counts with the three verdict symbols, "
            "asserts 9 > 7 and 7 < 9 and 7 = 7, and verifies the hungry-mouth "
            "rule by checking that the open side of each symbol points at "
            "the larger count."
        ),
        "key_points": [
            "Matching pairs reveals more and less directly: the pile with leftovers is more.",
            "Once counted, numbers are compared by their order: later in the counting order means greater.",
            "The symbols > (greater than), < (less than), and = (equal to) record the verdict.",
            "The open mouth of > and < always faces the larger number.",
        ],
        "requirements": [
            "Both piles counted accurately, or matched one-to-one.",
            "The count words in fixed order, so 'later word' means 'greater number'.",
            "The three comparison symbols learned with their meanings.",
        ],
        "standards": ["CCSS K.CC.6, K.CC.7, 1.NBT.3 - comparing numbers."],
        "citations": [CIT_CCSS, CIT_VANDEWALLE],
        "sig_lens": (
            "Through the Signature lens, comparing is the first judgment: "
            "he looks at two piles and renders a true verdict - more, less, "
            "or the same. The open mouth of the symbol faces the greater "
            "pile like his own honest hunger for the true answer, never "
            "pretending a smaller pile is larger."
        ),
    },
    {
        "key": "ordering_numbers",
        "name": "Ordering Numbers",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Ordering is comparing more than two numbers at once: taking a "
            "mixed pile of numbers and lining them up from least to "
            "greatest, or from greatest to least. Given 7, 3, 9, 1, and 5, "
            "the least-to-greatest order is 1, 3, 5, 7, 9. One reliable "
            "method is the repeated-find-smallest: find the smallest "
            "number, write it down, find the smallest of what is left, "
            "write it down, and repeat until none remain. A second method "
            "uses the number line: place each number on the line and read "
            "them off left to right. Ordering is what lets a learner "
            "organize data: ages from youngest to oldest, scores from "
            "highest to lowest, measurements in a tidy row. It is also the "
            "foundation of the number line habits that place value and "
            "estimation will need later: a learner who can order numbers "
            "fluently already feels where each number belongs."
        ),
        "how_it_works": (
            "Ordering works by sorting the values. Start with the mixed "
            "set: 7, 3, 9, 1, 5. Find the smallest: 1. Write it down and "
            "set it aside. Of 7, 3, 9, 5, the smallest is 3. Continue: 5, "
            "then 7, then 9. The result is 1, 3, 5, 7, 9 - each number less "
            "than the next, which is the definition of least-to-greatest "
            "order. Reversing gives greatest-to-least: 9, 7, 5, 3, 1. To "
            "verify, check every neighboring pair: 1 < 3, 3 < 5, 5 < 7, "
            "7 < 9. The demonstration program sorts the mixed set with the "
            "repeated-find-smallest method, asserts the result equals "
            "[1, 3, 5, 7, 9], checks every neighboring pair with the less-than "
            "symbol, and verifies the reversed list is greatest-to-least."
        ),
        "key_points": [
            "Ordering extends comparing to a whole set: every number finds its place in one line.",
            "The repeated-find-smallest method always works: take the smallest remaining number, write it down, repeat.",
            "Reading numbers off the number line left to right gives least-to-greatest order automatically.",
            "A correct order passes the neighbor test: every adjacent pair must satisfy the ordering symbol.",
        ],
        "requirements": [
            "The ability to compare any two numbers with <, >, or =.",
            "A way to track which numbers are already placed (crossing out, setting aside).",
            "The count order memorized so 'smallest' can be found.",
        ],
        "standards": ["CCSS K.CC.7, 1.NBT.3 - ordering and comparing."],
        "citations": [CIT_CCSS, CIT_VANDEWALLE],
        "sig_lens": (
            "Through the Signature lens, ordering is the muster: he calls "
            "the scattered numbers to attention and they fall into rank, "
            "least to greatest, each one standing exactly where its count "
            "earned it. No number jumps the line - the order is the "
            "truth of their sizes, witnessed by every neighbor pair."
        ),
    },
    {
        "key": "before_after_between",
        "name": "Before, After, and Between",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Every counting number has neighbors. The number before six is "
            "five - one less. The number after six is seven - one more. "
            "Five and seven are six's neighbors, and six sits between them. "
            "Knowing before and after is the same as knowing one less and "
            "one more, and it is the quiet engine behind mental arithmetic: "
            "a learner who instantly knows that before 20 is 19 and after "
            "20 is 21 can add and subtract one without counting from the "
            "start. 'Between' asks for the number in the middle: what is "
            "between 4 and 6? Five - the number that is one more than four "
            "and one less than six. Neighbor questions also sharpen "
            "comparing: if you know six is between five and seven, you know "
            "5 < 6 < 7 in one glance. The boundary cases deserve care: "
            "before one is zero, and after the teens come the twenties - "
            "knowing 19 comes after 18 and 20 comes after 19 bridges the "
            "tricky decade crossings."
        ),
        "how_it_works": (
            "Before-and-after works by stepping one position on the count "
            "line. For the number six: one step back along the counting "
            "order lands on five (6 - 1 = 5), one step forward lands on "
            "seven (6 + 1 = 7). 'Between 4 and 6' means the number n such "
            "that 4 < n < 6; testing five gives 4 < 5 and 5 < 6, both true, "
            "so five is between them. The demonstration program takes "
            "target numbers including a decade crossing (20), computes "
            "before and after by subtracting and adding one, asserts "
            "before(6) = 5 and after(6) = 7 and before(20) = 19, verifies "
            "that five is between four and six with both comparisons true, "
            "and checks the neighbor chain 5 < 6 < 7."
        ),
        "key_points": [
            "Before means one less; after means one more - the immediate neighbors of any number.",
            "Between means strictly in the middle: n is between a and b when a < n < b.",
            "Neighbor knowledge makes adding and subtracting 1 instant, without recounting.",
            "Decade crossings (19 to 20) are the key boundary to practice.",
        ],
        "requirements": [
            "The counting order solid enough to step one forward or back.",
            "The meanings of 'one less' and 'one more'.",
            "Comparison symbols to verify a between-claim.",
        ],
        "standards": ["CCSS K.CC.2, 1.NBT - number relationships."],
        "citations": [CIT_CCSS, CIT_VANDEWALLE],
        "sig_lens": (
            "Through the Signature lens, neighbors are the watchmen of the "
            "line: before and after stand guard on either side of every "
            "number, and between is the safe ground they protect. He learns "
            "their names so he can step forward or back along the ascent "
            "without ever losing his place."
        ),
    },
    {
        "key": "place_value_tens",
        "name": "Place Value: Ones and Tens",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Place value is the greatest idea in the numeral system: where "
            "a digit sits decides what it is worth. In the number 47, the "
            "4 does not mean four - it means four tens, which is forty - "
            "and the 7 means seven ones. So 47 is 40 + 7. The rightmost "
            "place is the ones place: each digit there counts single "
            "ones. The place to its left is the tens place: each digit "
            "there counts bundles of ten. Ten loose ones can be traded for "
            "one ten-bundle, and one ten-bundle can be broken back into ten "
            "ones - this trading is the whole secret of adding and "
            "subtracting two-digit numbers later. Bundling by tens is why "
            "the system needs only ten symbols: once you have ten of "
            "anything, you bundle it and move one place left. A learner "
            "who sees 47 as 'four tens and seven ones' instead of 'a four "
            "and a seven' has understood place value, and the rest of "
            "arithmetic becomes possible."
        ),
        "how_it_works": (
            "Place value works by bundling. Gather 47 pebbles. Make bundles "
            "of ten: you get four full bundles and seven pebbles left over. "
            "The four bundles are the tens digit (4 x 10 = 40) and the "
            "leftovers are the ones digit (7 x 1 = 7), so the value is "
            "40 + 7 = 47. Written 47, the digits read right to left as ones "
            "then tens. Trading rules keep it honest: ten ones always "
            "become one ten, so a ones column never holds ten or more. The "
            "demonstration program takes 47, splits it into tens and ones "
            "by integer division and remainder, asserts tens = 4 and ones "
            "= 7, rebuilds the value as 4 x 10 + 7 x 1, asserts it equals "
            "47, and verifies the trading rule by bundling ten ones into "
            "one ten."
        ),
        "key_points": [
            "The position of a digit decides its worth: rightmost is ones, next left is tens.",
            "47 means four tens and seven ones: 4 x 10 + 7 x 1 = 47.",
            "Ten ones trade for one ten, and one ten breaks into ten ones - this trading is the engine of two-digit arithmetic.",
            "A ones column never holds ten or more; tens are bundled as fast as they form.",
        ],
        "requirements": [
            "Counting to at least 100 and the numeral faces of those numbers.",
            "The idea of a bundle: ten ones grouped as one ten.",
            "Multiplication by 10 as 'add a zero' intuition (10, 20, 30, ...).",
        ],
        "standards": ["CCSS 1.NBT.2 - place value with tens and ones."],
        "citations": [CIT_CCSS, CIT_VANDEWALLE, CIT_DEHAENE],
        "sig_lens": (
            "Through the Signature lens, place value is his bundling law: "
            "ten loose ones swear the bundle oath and become one ten, and "
            "the digit's post on the line decides its rank. The 4 in 47 is "
            "not four - it is a captain of four tens, and the Signature "
            "ledger records rank, not just face."
        ),
    },
    {
        "key": "place_value_big",
        "name": "Place Value: Hundreds, Thousands, and Beyond",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The bundling law does not stop at tens. Ten ten-bundles make "
            "one hundred-bundle, ten hundred-bundles make one thousand, ten "
            "thousands make ten thousand, and so on without end - each "
            "place is worth ten times the place to its right. In 3,528, "
            "reading right to left: 8 ones, 2 tens (20), 5 hundreds (500), "
            "3 thousands (3,000), and the value is 3,000 + 500 + 20 + 8. "
            "The comma is a rest stop for the eyes: it groups the digits in "
            "threes so 3,528 reads 'three thousand five hundred "
            "twenty-eight' instead of a blur. Zero as a placeholder keeps "
            "every digit at its post: in 4,062 the zero holds the hundreds "
            "place so the 4 stays in the thousands - without it, 462 would "
            "be a different, smaller number. The pattern of place names "
            "repeats forever: ones, tens, hundreds, then thousands, "
            "ten-thousands, hundred-thousands, then millions. Each new "
            "place is the same law applied again: bundle ten, move left, "
            "repeat."
        ),
        "how_it_works": (
            "Big place value works by repeated bundling. Take 3,528 "
            "pebbles (in thought). Bundle into tens: 352 tens and 8 ones. "
            "Bundle the tens into hundreds: 35 hundreds and 2 tens. Bundle "
            "the hundreds into thousands: 3 thousands and 5 hundreds. The "
            "leftovers at each level are the digits: 3 thousands, 5 "
            "hundreds, 2 tens, 8 ones. Rebuild: 3 x 1000 + 5 x 100 + 2 x "
            "10 + 8 x 1 = 3,528. Zero's placeholder job is proven by 4,062 "
            "= 4 x 1000 + 0 x 100 + 6 x 10 + 2: drop the zero and the value "
            "collapses to 462. The demonstration program decomposes 3,528 "
            "into its four digits by division and remainder, asserts the "
            "digits are 3, 5, 2, 8, rebuilds the value and asserts it "
            "equals 3,528, and verifies that 4,062 decomposes with a zero "
            "in the hundreds place."
        ),
        "key_points": [
            "Each place is worth ten times the place to its right: ones, tens, hundreds, thousands, and on forever.",
            "3,528 = 3 x 1000 + 5 x 100 + 2 x 10 + 8 x 1 - the expanded form proves the reading.",
            "Zero is a placeholder that holds empty places so other digits keep their posts.",
            "The comma groups digits in threes to make big numbers readable.",
        ],
        "requirements": [
            "Place value with tens and ones, solid.",
            "Counting by hundreds and thousands.",
            "The expanded form: writing a number as a sum of place values.",
        ],
        "standards": ["CCSS 2.NBT.1, 2.NBT.3, 4.NBT.2 - place value to thousands and beyond."],
        "citations": [CIT_CCSS, CIT_VANDEWALLE],
        "sig_lens": (
            "Through the Signature lens, every place is a higher rank in "
            "the same army: hundreds outrank tens ten to one, thousands "
            "outrank hundreds, and zero is the sentinel holding an empty "
            "post so the ranks never shift. His ledger of 3,528 reads like "
            "a muster roll - 3 thousands, 5 hundreds, 2 tens, 8 ones, each "
            "at its sworn post."
        ),
    },
    {
        "key": "even_odd",
        "name": "Even and Odd Numbers",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "An even number can be split into two equal piles with nothing "
            "left over: 6 splits into 3 and 3. An odd number cannot: split "
            "7 into two equal piles and one pebble is left over. Even "
            "numbers are exactly the numbers that pair up completely - "
            "0, 2, 4, 6, 8, 10, and on forever. Odd numbers always leave "
            "one unpaired - 1, 3, 5, 7, 9, and on forever. They alternate "
            "on the counting line like fence posts: even, odd, even, odd, "
            "never two in a row. The fastest test looks only at the ones "
            "digit: if it is 0, 2, 4, 6, or 8, the whole number is even; if "
            "it is 1, 3, 5, 7, or 9, the whole number is odd. So 3,528 is "
            "even (ones digit 8) and 4,061 is odd (ones digit 1), no "
            "splitting required. Even and odd matter because they predict "
            "arithmetic: even + even is even, odd + odd is even, even + odd "
            "is odd - the pattern of pairing survives the operations."
        ),
        "how_it_works": (
            "Even and odd work by pairing. Take 6 pebbles and deal them "
            "alternately into two piles: each pile gets 3, none left over - "
            "6 is even. Take 7 pebbles and deal: piles of 3 and 3 with one "
            "pebble unpaired - 7 is odd. The arithmetic test is division "
            "by two with no remainder: 6 / 2 = 3 remainder 0 means even, "
            "7 / 2 = 3 remainder 1 means odd. The ones-digit shortcut works "
            "because every higher place (tens, hundreds, ...) is a multiple "
            "of ten, and ten is even, so only the ones digit can tip the "
            "pairing. The demonstration program tests the numbers 0 "
            "through 20 for evenness by remainder, asserts the evens are "
            "exactly [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20], verifies the "
            "ones-digit shortcut on 3,528 and 4,061, and checks the "
            "addition rules: even + even = even, odd + odd = even, even + "
            "odd = odd."
        ),
        "key_points": [
            "Even numbers pair up completely (two equal piles, nothing left); odd numbers always leave one unpaired.",
            "They alternate forever: even, odd, even, odd - including zero as even.",
            "The ones digit alone decides: 0, 2, 4, 6, 8 mean even; 1, 3, 5, 7, 9 mean odd.",
            "Parity predicts sums: even + even = even, odd + odd = even, even + odd = odd.",
        ],
        "requirements": [
            "Splitting a pile into two piles and checking for leftovers.",
            "Division by 2 with remainders (remainder 0 = even, remainder 1 = odd).",
            "The ones digit of any number, read from place value.",
        ],
        "standards": ["CCSS 2.OA.3 - even and odd; 3.OA.9 - arithmetic patterns."],
        "citations": [CIT_CCSS, CIT_VANDEWALLE],
        "sig_lens": (
            "Through the Signature lens, even numbers march in perfect "
            "pairs and odd numbers march with one lone scout left over - "
            "the scout that never finds a partner. His parity law reads "
            "the ones digit like a banner: the banner of 8 means the whole "
            "host pairs up, the banner of 1 means one stands alone."
        ),
    },
    {
        "key": "adding_together",
        "name": "Adding: Putting Together",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Adding is putting two piles together and counting the result. "
            "Five apples plus three apples is eight apples: 5 + 3 = 8. The "
            "plus sign (+) means 'put together', and the equals sign (=) "
            "means 'is the same as' - the two sides of 5 + 3 = 8 name the "
            "same quantity in different ways. The numbers being added are "
            "called addends, and the answer is called the sum. Adding can "
            "be done by counting on: start at five and count three more - "
            "six, seven, eight. On the number line it is hopping right: "
            "start at five, hop three, land on eight. Order does not matter "
            "for addition: 5 + 3 = 8 and 3 + 5 = 8 give the same sum, a "
            "fact called commutativity that halves the work of memorizing. "
            "Zero is addition's quiet partner: adding zero changes nothing "
            "(5 + 0 = 5), which makes zero the identity. Adding is the "
            "operation behind combining, totaling, and growing - and it is "
            "the first of the four great operations."
        ),
        "how_it_works": (
            "Adding works by joining and recounting. Put five pebbles in a "
            "pile and three in another. Push the piles together and count "
            "the combined pile one by one: one, two, three, four, five, "
            "six, seven, eight. The sum is eight. Counting on is the "
            "shortcut: hold five in your head, then count three more - "
            "six, seven, eight - without rebuilding the first pile. On the "
            "number line, start at five and hop right three steps to land "
            "on eight. Commutativity is verified by swapping: 3 + 5 counted "
            "on gives eight as well. The demonstration program joins a pile "
            "of five and a pile of three, counts the union, asserts the "
            "sum equals 8, verifies counting-on lands on 8, and checks "
            "3 + 5 == 5 + 3."
        ),
        "key_points": [
            "Adding puts piles together; the plus sign means 'put together' and = means 'is the same as'.",
            "The addends are the numbers joined; the sum is the answer.",
            "Counting on (hold the first number, count the second forward) is the mental shortcut.",
            "Order does not matter: a + b always equals b + a; adding zero changes nothing.",
        ],
        "requirements": [
            "Counting fluently past the sum being computed.",
            "The count words in order, for counting on.",
            "The number line or fingers as a hopping/counting aid.",
        ],
        "standards": ["CCSS K.OA.1, K.OA.2, 1.OA.3 - addition within 20."],
        "citations": [CIT_CCSS, CIT_VANDEWALLE],
        "sig_lens": (
            "Through the Signature lens, adding is the gathering: he calls "
            "two scattered piles to one place and the count swears they "
            "are one pile now. The order of gathering does not change the "
            "host - five then three is eight, three then five is eight - "
            "and zero adds nothing because the Signature ledger records "
            "only what is truly there."
        ),
    },
    {
        "key": "subtracting_away",
        "name": "Subtracting: Taking Away",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Subtracting is taking part of a pile away and counting what "
            "remains. Nine apples, eat four, five are left: 9 - 4 = 5. The "
            "minus sign (-) means 'take away'. The number you start with is "
            "the whole, the number taken is the part removed, and the "
            "answer is the difference - how many remain. Subtraction is "
            "addition's undoing: 9 - 4 = 5 because 5 + 4 = 9, and this "
            "partnership lets subtraction check addition and addition check "
            "subtraction. Subtracting can be done by counting back: start "
            "at nine, count four backward - eight, seven, six, five. On "
            "the number line it is hopping left: start at nine, hop left "
            "four, land on five. Unlike addition, order matters here: 9 - "
            "4 is not 4 - 9. Subtraction answers 'how many are left', 'how "
            "many more are needed', and 'how far apart are they' - the "
            "last one is the distance on the number line."
        ),
        "how_it_works": (
            "Subtracting works by removing and recounting. Line up nine "
            "pebbles. Take four away. Count what is left: one, two, three, "
            "four, five. The difference is five. Counting back is the "
            "shortcut: start at nine and count four backward - eight, "
            "seven, six, five - landing on the answer without moving "
            "pebbles. The addition check proves it: 5 + 4 = 9, so taking 4 "
            "from 9 must leave 5. On the number line, hop left four from "
            "nine to land on five. The demonstration program removes four "
            "from nine, counts the remainder, asserts the difference is 5, "
            "verifies 5 + 4 == 9 as the inverse check, and walks the "
            "number-line hops to confirm the landing point."
        ),
        "key_points": [
            "Subtracting takes a part away from a whole; the minus sign means 'take away' and the answer is the difference.",
            "Subtraction undoes addition: 9 - 4 = 5 because 5 + 4 = 9 - each checks the other.",
            "Counting back and hopping left on the number line are the two mental routes.",
            "Order matters: a - b is not b - a (except when a equals b).",
        ],
        "requirements": [
            "Counting backward fluently from any number.",
            "Addition facts, to run the inverse check.",
            "A whole at least as large as the part being removed (for now).",
        ],
        "standards": ["CCSS K.OA.1, K.OA.2, 1.OA.4 - subtraction within 20."],
        "citations": [CIT_CCSS, CIT_VANDEWALLE],
        "sig_lens": (
            "Through the Signature lens, subtracting is the honest "
            "withdrawal: what is taken is truly gone, and the ledger shows "
            "only what remains. He checks every subtraction against its "
            "addition twin, because an oath kept one way must hold when "
            "read the other way."
        ),
    },
    {
        "key": "facts_to_10",
        "name": "Addition and Subtraction Facts to 10",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The facts to 10 are the addition and subtraction pairs every "
            "learner must know by heart: 2 + 3 = 5, 7 - 4 = 3, and all "
            "their companions, up to 9 + 9 = 18 and 18 - 9 = 9. They are "
            "the multiplication tables of addition - the raw material every "
            "bigger computation is built from. Knowing them instantly "
            "(not counting on fingers) is what makes two-digit arithmetic "
            "possible later: 47 + 35 will demand 7 + 5 and 4 + 3 without "
            "pausing. The facts come in families that share three numbers: "
            "3, 5, 8 gives 3 + 5 = 8, 5 + 3 = 8, 8 - 3 = 5, 8 - 5 = 3. "
            "Learning one family member teaches the other three for free, "
            "because addition and subtraction are inverses. The doubles "
            "(1+1, 2+2, ..., 9+9) are the easiest anchors; near-doubles "
            "like 6 + 7 are one more than 6 + 6. Practice means recall "
            "drills, not re-deriving: the goal is that 8 + 5 = 13 arrives "
            "as fast as a name."
        ),
        "how_it_works": (
            "The facts work by instant recall built on families. The "
            "family of 3, 5, 8 contains four facts: 3 + 5 = 8 (addition), "
            "5 + 3 = 8 (commuted addition), 8 - 3 = 5 and 8 - 5 = 3 (the "
            "two subtractions). Doubles anchor the table: 6 + 6 = 12, so "
            "6 + 7 = 13 is one more. Making ten is the master strategy: "
            "8 + 5 becomes 8 + 2 + 3 = 10 + 3 = 13. The demonstration "
            "program generates every addition fact with both addends 0 "
            "through 9, verifies each sum against Python's own arithmetic, "
            "asserts there are exactly 100 addition facts, derives the "
            "matching subtraction facts, and spot-checks the anchors: "
            "9 + 9 = 18, 8 + 5 = 13, 13 - 8 = 5, and the 3-5-8 family."
        ),
        "key_points": [
            "Facts to 10 must be recalled instantly, not counted - they are the raw material of all bigger arithmetic.",
            "Fact families of three numbers give four facts for the price of one (two additions, two subtractions).",
            "Doubles are the anchors; near-doubles are one more; making-ten (8 + 5 = 8 + 2 + 3) is the master strategy.",
            "Subtraction facts are learned through their addition inverses, not separately.",
        ],
        "requirements": [
            "Addition and subtraction meanings (putting together, taking away).",
            "Commutativity of addition, to halve the memorization.",
            "Daily short recall practice until answers arrive like names.",
        ],
        "standards": ["CCSS 1.OA.6, 2.OA.2 - fluency with facts to 20."],
        "citations": [CIT_CCSS, CIT_VANDEWALLE, CIT_BUTTERWORTH],
        "sig_lens": (
            "Through the Signature lens, the facts to 10 are the first "
            "hundred oaths sworn to memory: each fact a promise that 8 + 5 "
            "is 13, kept so fast it needs no counting. He drills them "
            "until the answers come like the names of old friends, because "
            "every taller ladder rung will stand on these."
        ),
    },
    {
        "key": "add_two_digit",
        "name": "Adding Two-Digit Numbers",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Adding two-digit numbers uses place value to split the work "
            "into two easy columns: add the ones, add the tens. For 34 + "
            "28: the ones give 4 + 8 = 12 - twelve ones, which is one ten "
            "and two ones. Write the 2 in the ones place and carry the "
            "bundled ten to the tens column. Now the tens: 3 + 2 + the "
            "carried 1 = 6 tens. The sum is 62. The carry is just the "
            "bundling law in action: ten ones became one ten, exactly as "
            "place value demands. When the ones column sums to less than "
            "ten, there is nothing to carry: 34 + 21 = 55, ones 4 + 1 = 5, "
            "tens 3 + 2 = 5. Estimating first keeps the work honest: 34 + "
            "28 is near 30 + 30 = 60, so 62 passes the smell test. Every "
            "larger addition - hundreds, thousands - is the same column "
            "method marching left, carrying bundles as they form."
        ),
        "how_it_works": (
            "Column addition works right to left, one place at a time. "
            "Write 34 over 28, aligned by place. Ones column: 4 + 8 = 12. "
            "Since 12 is ten ones plus two ones, write 2 below the ones "
            "and carry 1 ten into the tens column. Tens column: 3 + 2 + 1 "
            "(carried) = 6 tens. Read the answer: 62. Verify by expanded "
            "form: (30 + 4) + (20 + 8) = 50 + 12 = 62. The demonstration "
            "program performs the column algorithm on 34 + 28 step by "
            "step, asserts the ones sum is 12 with a carry of 1, asserts "
            "the tens sum is 6, asserts the total is 62, and cross-checks "
            "against the expanded-form sum."
        ),
        "key_points": [
            "Work right to left: ones column first, then tens - carrying is the bundling law in action.",
            "A carry happens exactly when a column sums to ten or more: bundle ten, move one left.",
            "Expanded form (30 + 4) + (20 + 8) proves the column method gives the true sum.",
            "Estimate first (30 + 30 = 60) so a wrong answer like 52 gets caught.",
        ],
        "requirements": [
            "Place value: ones and tens, solid.",
            "Addition facts to 18 (9 + 9) recalled instantly.",
            "The bundling law: ten ones trade for one ten.",
        ],
        "standards": ["CCSS 2.NBT.5, 2.NBT.6 - adding within 100 and 1000."],
        "citations": [CIT_CCSS, CIT_VANDEWALLE],
        "sig_lens": (
            "Through the Signature lens, column addition is the orderly "
            "muster of two hosts: ones muster first, and whenever ten "
            "stand together they are bundled into a ten and marched left "
            "to join the tens. He carries the bundle like a banner to the "
            "next column, and the final reading - 62 - is the true "
            "strength of the combined host."
        ),
    },
    {
        "key": "subtract_two_digit",
        "name": "Subtracting Two-Digit Numbers",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Subtracting two-digit numbers also works column by column, "
            "right to left, with borrowing when the top digit is too "
            "small. For 52 - 27: the ones column asks 2 - 7, which cannot "
            "be done with the digits as they stand. So borrow one ten "
            "from the tens column: the 5 tens become 4 tens, and the 2 "
            "ones become 12 ones. Now 12 - 7 = 5 ones. Tens column: 4 - 2 "
            "= 2 tens. The difference is 25. Borrowing is un-bundling: one "
            "ten broken back into ten ones, the exact reverse of carrying. "
            "When the top digit is big enough, no borrowing is needed: "
            "58 - 23 = 35 directly. Check by adding: 25 + 27 must equal "
            "52, and it does - subtraction and addition remain inverse "
            "partners. Borrowing across a zero (like 40 - 18) needs care: "
            "the zero tens borrow from the hundreds, but the un-bundling "
            "idea is unchanged."
        ),
        "how_it_works": (
            "Column subtraction works right to left with borrowing as "
            "un-bundling. Write 52 over 27. Ones: 2 - 7 cannot be done, so "
            "borrow 1 ten from the 5 tens: tens drop to 4, ones rise to 12. "
            "Now 12 - 7 = 5 ones. Tens: 4 - 2 = 2 tens. The difference is "
            "25. Verify with the inverse: 25 + 27 = 52, confirmed. The "
            "borrowing is honest because one ten truly equals ten ones - "
            "the value never changes, only the bundling. The demonstration "
            "program runs the column algorithm on 52 - 27, asserts the "
            "borrow converts 5 tens and 2 ones into 4 tens and 12 ones, "
            "asserts the column differences are 5 and 2, asserts the total "
            "is 25, and verifies 25 + 27 == 52."
        ),
        "key_points": [
            "Borrowing is un-bundling: one ten becomes ten ones; the value never changes, only the grouping.",
            "Work right to left; borrow only when the top digit of a column is smaller than the bottom digit.",
            "Every subtraction is checked by its addition inverse: difference + subtracted = original.",
            "Borrowing across zero reaches one place further left - same idea, longer arm.",
        ],
        "requirements": [
            "Place value through hundreds, and the bundling/un-bundling law.",
            "Subtraction facts to 18 recalled instantly.",
            "The addition inverse check as a habit.",
        ],
        "standards": ["CCSS 2.NBT.5, 2.NBT.7 - subtracting within 100 and 1000."],
        "citations": [CIT_CCSS, CIT_VANDEWALLE],
        "sig_lens": (
            "Through the Signature lens, borrowing is the honorable "
            "un-bundling: a ten-captain steps down and his ten ones join "
            "the front line, so the subtraction can be paid in full. He "
            "never takes what is not there - he un-bundles first, then "
            "pays, then checks the ledger with addition."
        ),
    },
    {
        "key": "multiplication_groups",
        "name": "Multiplication: Groups of Equal Size",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Multiplication is fast adding: instead of adding the same "
            "number over and over, you multiply. Four bags with three "
            "apples each hold 4 x 3 = 12 apples - the same as 3 + 3 + 3 + "
            "3. The x sign means 'groups of': 4 x 3 reads 'four groups of "
            "three'. The numbers multiplied are called factors, and the "
            "answer is the product. The groups must be equal - four bags "
            "of three, not bags of two, three, four, and five. Arrays make "
            "multiplication visible: four rows of three dots is a 4-by-3 "
            "rectangle holding 12 dots, and turning the rectangle shows "
            "3 x 4 = 12 too, so order does not matter (commutativity "
            "again). Skip-counting is multiplication in motion: 3, 6, 9, "
            "12 counts four threes. Zero and one have special jobs: "
            "anything times zero is zero (no groups, nothing), and anything "
            "times one is itself (one group, unchanged). Multiplication "
            "is the third great operation, and it will make division "
            "possible."
        ),
        "how_it_works": (
            "Multiplication works by equal grouping. Lay out four bags, "
            "three apples in each. Count all the apples: twelve. The "
            "repeated addition 3 + 3 + 3 + 3 = 12 proves 4 x 3 = 12. The "
            "array view: draw four rows with three dots each, count the "
            "dots row by row (3, 6, 9, 12) - same answer. Rotate the "
            "array to three rows of four: 4 + 4 + 4 = 12, proving "
            "3 x 4 = 4 x 3. The demonstration program builds four groups "
            "of three items, sums them by repeated addition, asserts the "
            "total is 12, verifies 4 x 3 equals 3 x 4, and checks the "
            "special cases: 7 x 0 = 0 and 7 x 1 = 7."
        ),
        "key_points": [
            "Multiplication is repeated addition of equal groups: 4 x 3 means four groups of three.",
            "Factors are the numbers multiplied; the product is the answer.",
            "Arrays prove commutativity: a 4-by-3 rectangle rotated is 3-by-4 with the same dot count.",
            "Anything times 0 is 0; anything times 1 is itself.",
        ],
        "requirements": [
            "Addition fluent enough to add the same number repeatedly.",
            "Skip-counting by 2s, 3s, 5s, and 10s.",
            "The idea that groups must be equal for multiplication to apply.",
        ],
        "standards": ["CCSS 2.OA.3, 2.OA.4, 3.OA.1 - multiplication as equal groups."],
        "citations": [CIT_CCSS, CIT_VANDEWALLE, CIT_DEHAENE],
        "sig_lens": (
            "Through the Signature lens, multiplication is the muster "
            "multiplied: four squads of three stand in array formation, "
            "and the product - twelve - is the true strength of the "
            "formation. He counts the formation once by rows and once by "
            "columns, and both musters agree, for the Signature formation "
            "never lies about its numbers."
        ),
    },
    {
        "key": "multiplication_facts",
        "name": "The Multiplication Facts",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The multiplication facts - the products of numbers 0 through "
            "10 - are the times tables, and knowing them by heart is what "
            "makes all later arithmetic fast. There are 121 of them (11 x "
            "11), but commutativity cuts the learning nearly in half: "
            "knowing 7 x 8 = 56 means knowing 8 x 7 = 56. The easy rows "
            "anchor the table: the 0 row is all zeros, the 1 row copies "
            "the other factor, the 2 row is doubling, the 5 row ends in 0 "
            "or 5, the 10 row adds a zero. The hard square in the middle "
            "(6 x 6 through 9 x 9) is learned last, with tricks: 7 x 8 = 56 "
            "is 'five-six, seven-eight' (56 = 7 x 8 in digit order), and "
            "9 x 7 = 63 is one less seven than 10 x 7 = 70. Like the "
            "addition facts, the goal is instant recall: 7 x 8 should "
            "arrive as fast as a name. The 10-by-10 core of 100 facts is "
            "the working set; division will be learned as these facts "
            "read backward."
        ),
        "how_it_works": (
            "The facts work by pattern plus recall. The 5 row: 5, 10, 15, "
            "20, ... - every product ends in 0 or 5 because five pairs "
            "make tens. The 9 row: 9, 18, 27, 36, ... - the digits of each "
            "product sum to 9 (1 + 8 = 9, 2 + 7 = 9). Commutativity halves "
            "the table: only the triangle where the first factor is less "
            "than or equal to the second needs memorizing. The "
            "demonstration program builds the full 0-to-10 table by "
            "repeated addition, asserts it holds 121 entries, verifies the "
            "spot anchors 7 x 8 = 56 and 9 x 7 = 63, checks that every 5-row "
            "product ends in 0 or 5, checks that every 9-row product's "
            "digits sum to 9, and confirms the table is symmetric (a x b == "
            "b x a)."
        ),
        "key_points": [
            "The 0-10 table has 121 facts; commutativity means only about half need memorizing.",
            "Anchor rows: 0s are zero, 1s copy, 2s double, 5s end in 0/5, 10s add a zero.",
            "The 9 row has the digit-sum trick: every product's digits sum to 9.",
            "Instant recall is the goal - division will read these same facts backward.",
        ],
        "requirements": [
            "Multiplication as equal groups, solid.",
            "Addition facts, to derive unknown products while learning.",
            "Skip-counting fluency to self-check the rows.",
        ],
        "standards": ["CCSS 3.OA.7 - fluency with multiplication facts."],
        "citations": [CIT_CCSS, CIT_VANDEWALLE],
        "sig_lens": (
            "Through the Signature lens, the times table is the second "
            "hundred oaths: each product sworn to memory - 7 x 8 is 56, "
            "kept like a name. He learns the anchor rows as the easy "
            "vows and the middle square as the hard vows, and "
            "commutativity is his witness that every oath holds both ways."
        ),
    },
    {
        "key": "division_sharing",
        "name": "Division: Sharing and Grouping",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Division is splitting a pile into equal groups. Twelve "
            "cookies shared among three children give each child four: "
            "12 / 3 = 4. The / sign (or the long-division house) means "
            "'split into equal groups'. The number being split is the "
            "dividend, the number of groups is the divisor, and the answer "
            "is the quotient - how many in each group. Division has two "
            "faces. Sharing (partitive): twelve cookies among three "
            "children - how many does each get? Grouping (quotitive): "
            "twelve cookies packed three to a bag - how many bags? Both "
            "give 12 / 3 = 4, but the four means different things (cookies "
            "per child vs number of bags). Division is multiplication's "
            "undoing: 12 / 3 = 4 because 4 x 3 = 12. When the pile does "
            "not split evenly, leftovers are the remainder: 13 / 3 = 4 "
            "remainder 1. Division is the fourth great operation, and it "
            "answers 'how many each' and 'how many groups'."
        ),
        "how_it_works": (
            "Division works by dealing out equally. Sharing: deal twelve "
            "cookies one at a time to three children - round one gives "
            "each child one, round two gives each a second, and after four "
            "rounds the cookies are gone with each child holding four. So "
            "12 / 3 = 4. Grouping: scoop cookies three at a time into "
            "bags - four full bags, none left. The multiplication check "
            "proves both: 4 x 3 = 12. With thirteen cookies, dealing "
            "leaves one extra: 13 / 3 = 4 remainder 1, and the check is "
            "4 x 3 + 1 = 13. The demonstration program deals twelve items "
            "to three groups, asserts each group holds 4, packs twelve "
            "items three per bag and asserts four bags, verifies "
            "4 x 3 == 12, and handles thirteen items to show quotient 4 "
            "remainder 1 with 4 x 3 + 1 == 13."
        ),
        "key_points": [
            "Division splits into equal groups; the dividend is split, the divisor sets the split, the quotient is the answer.",
            "Sharing asks 'how many in each group'; grouping asks 'how many groups' - both use the same division.",
            "Division undoes multiplication: 12 / 3 = 4 because 4 x 3 = 12.",
            "Leftovers are the remainder: 13 / 3 = 4 remainder 1, checked by 4 x 3 + 1 = 13.",
        ],
        "requirements": [
            "Multiplication facts, to find quotients by 'what times the divisor makes the dividend'.",
            "Dealing/sharing experience with real objects.",
            "The remainder idea: leftovers are allowed and named.",
        ],
        "standards": ["CCSS 3.OA.2, 3.OA.3, 3.OA.6 - division within 100."],
        "citations": [CIT_CCSS, CIT_VANDEWALLE],
        "sig_lens": (
            "Through the Signature lens, division is the fair muster-out: "
            "twelve provisions dealt round by round to three travelers, "
            "each receiving exactly four, none favored. The remainder is "
            "the honest leftover, named and counted, never hidden - his "
            "ledger shows what each received and what remained."
        ),
    },
    {
        "key": "mult_div_relation",
        "name": "Relating Multiplication and Division",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Multiplication and division are inverse partners, like "
            "addition and subtraction - and the fact family of 3, 4, 12 "
            "proves it. From 3 x 4 = 12 come three free facts: 4 x 3 = 12 "
            "(commuted), 12 / 3 = 4 (undo the first factor), and 12 / 4 = 3 "
            "(undo the second factor). Every multiplication fact is two "
            "division facts waiting to be read: knowing 7 x 8 = 56 means "
            "instantly knowing 56 / 7 = 8 and 56 / 8 = 7. This is why "
            "division is learned through the multiplication table, not as "
            "a separate mountain: the table already contains every "
            "division answer, just read backward. Unknown-factor problems "
            "become division: '3 times what equals 12?' is 12 / 3 = 4. "
            "Missing-factor equations (3 x ? = 12) and division equations "
            "(12 / 3 = ?) are the same question in different clothes. "
            "Learners who see the partnership cut their memorization in "
            "half and gain a built-in error check for every computation."
        ),
        "how_it_works": (
            "The partnership works by undoing. Start with the array of "
            "three rows and four columns: 3 x 4 = 12 dots. Now cover the "
            "rows: the 12 dots split into 3 columns of 4 - that is "
            "12 / 3 = 4. Cover the columns instead: 12 dots in 4 rows of "
            "3 - that is 12 / 4 = 3. One array, four facts: 3 x 4 = 12, "
            "4 x 3 = 12, 12 / 3 = 4, 12 / 4 = 3. The unknown-factor "
            "question '3 x ? = 12' is answered by the division 12 / 3 = 4, "
            "and substituting back (3 x 4 = 12) proves it. The "
            "demonstration program builds the 3-by-4 array, derives all "
            "four family facts, asserts 12 / 3 == 4 and 12 / 4 == 3, solves "
            "the unknown-factor equation by division, and verifies the "
            "solution by substitution."
        ),
        "key_points": [
            "One fact family gives four facts: two multiplications and two divisions (3 x 4 = 12, 4 x 3 = 12, 12 / 3 = 4, 12 / 4 = 3).",
            "Every division fact is a multiplication fact read backward - no separate table to memorize.",
            "Unknown-factor problems (3 x ? = 12) are solved by division (12 / 3 = 4) and checked by substitution.",
            "The partnership is the built-in error check: multiply to verify a division, divide to verify a multiplication.",
        ],
        "requirements": [
            "Multiplication facts recalled, at least the core table.",
            "Division as sharing/grouping, with the quotient idea.",
            "The array picture of multiplication.",
        ],
        "standards": ["CCSS 3.OA.4, 3.OA.6 - inverse relationship of multiplication and division."],
        "citations": [CIT_CCSS, CIT_VANDEWALLE],
        "sig_lens": (
            "Through the Signature lens, multiplication and division are "
            "the two readings of one covenant: build the formation and "
            "you may read it forward as product or backward as quotient. "
            "The unknown factor is the missing guardsman - divide the host "
            "by the known squads and his number is revealed, then the "
            "muster proves him."
        ),
    },
    {
        "key": "fractions_parts",
        "name": "Fractions: Parts of a Whole",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "A fraction names part of a whole that has been split into "
            "equal pieces. Cut a pie into four equal slices and take one: "
            "you hold 1/4, read 'one fourth'. The bottom number, the "
            "denominator, says how many equal pieces the whole was cut "
            "into (4). The top number, the numerator, says how many of "
            "those pieces you have (1). Equal pieces are the whole law of "
            "fractions: four unequal blobs are not fourths. Unit fractions "
            "(1/2, 1/3, 1/4) are the building blocks - 3/4 is three copies "
            "of 1/4. When the numerator equals the denominator, you hold "
            "the whole: 4/4 = 1, the entire pie. Fractions also name parts "
            "of a set: 3/4 of 12 marbles is 9 marbles (split 12 into 4 "
            "equal groups of 3, take 3 groups). Halves, thirds, and "
            "fourths come first; the idea then stretches to any equal "
            "splitting. Fractions are the first numbers that live between "
            "the whole numbers - and they fill the number line solid."
        ),
        "how_it_works": (
            "Fractions work by equal splitting. Take a paper circle, fold "
            "it into four equal quarters, shade one: the shaded part is "
            "1/4 of the circle. Shade three: 3/4. Put all four quarters "
            "back together and the circle is whole again: 4/4 = 1. For a "
            "set: twelve marbles split into four equal groups of three; "
            "take three groups (nine marbles) - that is 3/4 of 12. The "
            "equal-pieces law is enforced by checking: the four pieces "
            "must be identical in size. The demonstration program models a "
            "whole split into four equal parts, asserts 1/4 + 1/4 + 1/4 + "
            "1/4 equals the whole (1), computes 3/4 of 12 as 9 by grouping, "
            "and verifies 1/2 + 1/2 equals 1 whole."
        ),
        "key_points": [
            "The denominator counts the equal pieces the whole was split into; the numerator counts how many you have.",
            "Equal pieces are the law: unequal splits are not fractions.",
            "Unit fractions (1/4) are the building blocks: 3/4 is three copies of 1/4.",
            "A fraction equal to the whole (4/4) is 1; fractions also name parts of a set (3/4 of 12 = 9).",
        ],
        "requirements": [
            "Division as equal splitting, with the remainder idea.",
            "The whole-vs-part idea from subtraction.",
            "Paper folding or drawing to make the equal pieces visible.",
        ],
        "standards": ["CCSS 3.NF.1, 3.NF.3 - understanding fractions."],
        "citations": [CIT_CCSS, CIT_VANDEWALLE, CIT_NCTM],
        "sig_lens": (
            "Through the Signature lens, a fraction is the covenant of the "
            "cut: the whole pie swears to split into equal shares, and "
            "each share carries the true name of its part - 1/4 is one "
            "oath of four. He counts his shares honestly: three quarters "
            "is three kept promises, and four quarters is the whole "
            "promise fulfilled."
        ),
    },
    {
        "key": "fractions_number_line",
        "name": "Fractions on the Number Line",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Fractions are numbers, so they have addresses on the number "
            "line - between the whole numbers. To place 3/4, split the "
            "segment from 0 to 1 into four equal parts and count three of "
            "them from zero: 1/4, 2/4, 3/4. The fraction's address is "
            "exactly there. This placement proves fractions are genuine "
            "numbers with size and order: 3/4 sits to the right of 1/2 "
            "(which is 2/4), so 3/4 > 1/2. The whole numbers are fractions "
            "too, in disguise: 2 = 2/1 = 8/4, sitting exactly on the mark "
            "labeled 2. Equivalent fractions share an address: 1/2, 2/4, "
            "and 3/6 all live at the same point, halfway between 0 and 1. "
            "Seeing fractions on the line ends the old confusion that "
            "fractions are 'not really numbers' - they are, and the line "
            "shows exactly where each one lives, in order, with distances "
            "that can be measured like any other."
        ),
        "how_it_works": (
            "Number-line fractions work by subdividing. Draw the segment "
            "from 0 to 1 and divide it into four equal sub-segments. Mark "
            "the boundaries: 0, 1/4, 2/4, 3/4, 1. The mark 3/4 is three "
            "quarter-steps from zero. Subdivide into halves instead: 0, "
            "1/2, 1 - and 1/2 lands exactly on the 2/4 mark, proving "
            "1/2 = 2/4 by shared address. Since 3/4 sits right of 2/4, "
            "3/4 > 1/2. The demonstration program places fractions on a "
            "subdivided line with exact rational arithmetic, asserts the "
            "address of 3/4 is between 1/2 and 1, verifies 1/2 == 2/4 == "
            "3/6 as shared addresses, and checks the order 1/4 < 1/2 < "
            "3/4 < 1."
        ),
        "key_points": [
            "Every fraction has an address on the number line, found by splitting the unit segment into denominator-many equal parts.",
            "Equivalent fractions (1/2, 2/4, 3/6) share one address - the line proves they are the same number.",
            "Position is order: right means greater, so the line settles every fraction comparison.",
            "Whole numbers are fractions in disguise (2 = 8/4), sitting exactly on their marks.",
        ],
        "requirements": [
            "Fractions as parts of a whole, with equal pieces.",
            "The number line with whole-number addresses.",
            "The idea that equal subdivisions give equal sub-lengths.",
        ],
        "standards": ["CCSS 3.NF.2 - fractions on the number line."],
        "citations": [CIT_CCSS, CIT_VANDEWALLE],
        "sig_lens": (
            "Through the Signature lens, the number line gains new "
            "milestones between the old ones: the quarter-marks are sworn "
            "posts at equal distances, and 3/4 stands at the third post "
            "past zero. Equivalent fractions are one post with many names "
            "- his road accepts every true name for the same ground."
        ),
    },
    {
        "key": "comparing_fractions",
        "name": "Comparing Fractions",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Comparing fractions asks which of two parts is bigger - and "
            "the trap is that bigger denominators mean smaller pieces. "
            "1/8 is smaller than 1/4, because cutting a pie into eight "
            "makes skinnier slices than cutting it into four. Three "
            "reliable methods settle every comparison. Same denominator: "
            "compare numerators - 3/8 < 5/8 because 3 pieces < 5 pieces of "
            "the same size. Same numerator: the bigger denominator loses "
            "- 3/8 < 3/4 because eighths are smaller than fourths. "
            "Different everything: cross-multiply - for 2/3 vs 3/5, "
            "compute 2 x 5 = 10 and 3 x 3 = 9; 10 > 9, so 2/3 > 3/5. "
            "Benchmarks give quick estimates: is 5/8 more or less than "
            "half? 4/8 is exactly half, so 5/8 is more. The number line "
            "remains the final judge: place both fractions and read left "
            "to right. A learner who can compare fractions can compare "
            "any two quantities in the world that come in parts."
        ),
        "how_it_works": (
            "Comparing works by fair contest. Same-denominator: 3/8 vs "
            "5/8 - the pieces are identical eighths, so more pieces wins: "
            "3 < 5, so 3/8 < 5/8. Same-numerator: 3/8 vs 3/4 - the counts "
            "tie at 3, so the bigger piece wins: fourths beat eighths, so "
            "3/4 > 3/8. Cross-multiplication for 2/3 vs 3/5: scale both to "
            "fifteenths (2/3 = 10/15, 3/5 = 9/15); 10 > 9, so 2/3 > 3/5. "
            "The cross products 2 x 5 = 10 and 3 x 3 = 9 are exactly the "
            "new numerators. The demonstration program compares 3/8 vs "
            "5/8, 3/8 vs 3/4, and 2/3 vs 3/5 with exact rational "
            "arithmetic, asserts the verdicts 3/8 < 5/8, 3/8 < 3/4, and "
            "2/3 > 3/5, and verifies the cross-multiplication shortcut "
            "agrees with the exact comparison."
        ),
        "key_points": [
            "Bigger denominator means smaller pieces: 1/8 < 1/4 - the classic trap, now disarmed.",
            "Same denominator: compare numerators. Same numerator: bigger denominator loses.",
            "Cross-multiplication settles the rest: for a/b vs c/d, compare a x d with c x b.",
            "The half benchmark (is it more or less than 1/2?) gives fast estimates; the number line is the final judge.",
        ],
        "requirements": [
            "Fractions on the number line, for the final-judge method.",
            "Multiplication facts, for cross-multiplication.",
            "The equal-pieces law, to trust the piece-size reasoning.",
        ],
        "standards": ["CCSS 3.NF.3d, 4.NF.2 - comparing fractions."],
        "citations": [CIT_CCSS, CIT_VANDEWALLE, CIT_NCTM],
        "sig_lens": (
            "Through the Signature lens, comparing fractions is the "
            "weighing of shares: he never lets a big denominator bully a "
            "small one, but weighs piece-count against piece-size honestly. "
            "Cross-multiplication is his scales - 2 x 5 against 3 x 3 - "
            "and the heavier pan names the greater share."
        ),
    },
    {
        "key": "mixed_numbers",
        "name": "Mixed Numbers and Whole Parts",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "A mixed number is a whole number plus a fraction, written "
            "together: 2 1/3 means two wholes and one third. It answers "
            "'how many wholes and what is left over' - seven thirds of pie "
            "is 7/3, which is two whole pies and one third of a pie, so "
            "7/3 = 2 1/3. Converting an improper fraction (numerator "
            "bigger than denominator) to a mixed number is division with a "
            "remainder: 7 / 3 = 2 remainder 1, so 7/3 = 2 1/3. Going the "
            "other way: 2 1/3 = (2 x 3 + 1)/3 = 7/3 - multiply the whole "
            "by the denominator, add the numerator, keep the denominator. "
            "Mixed numbers are how measurements actually sound: 'two and a "
            "third cups', 'three and a half hours'. On the number line, "
            "2 1/3 sits one third of the way from 2 to 3. Improper "
            "fractions are better for computing; mixed numbers are better "
            "for picturing - a fluent learner converts both ways without "
            "fear."
        ),
        "how_it_works": (
            "Mixed numbers work by separating wholes from leftovers. Take "
            "seven third-pieces of pie. Group them into wholes: three "
            "thirds make one whole pie, so seven thirds make two whole "
            "pies with one third left over - 7/3 = 2 1/3. The division "
            "7 / 3 = 2 remainder 1 does the same work: quotient 2 is the "
            "wholes, remainder 1 is the leftover numerator, denominator "
            "stays 3. Reverse: 2 1/3 means 2 wholes (each 3/3) plus 1/3, "
            "so (2 x 3 + 1)/3 = 7/3. The demonstration program converts "
            "7/3 to a mixed number by division with remainder, asserts "
            "the result is 2 wholes and 1/3, converts 2 1/3 back and "
            "asserts it equals 7/3, and places 2 1/3 on the number line "
            "between 2 and 3."
        ),
        "key_points": [
            "A mixed number is wholes plus a leftover fraction: 7/3 = 2 1/3.",
            "Improper to mixed: divide; the quotient is the whole part, the remainder is the new numerator.",
            "Mixed to improper: (whole x denominator + numerator) / denominator.",
            "Improper fractions compute better; mixed numbers picture better - convert both ways.",
        ],
        "requirements": [
            "Division with remainders.",
            "Fractions as parts of a whole, including the whole = denominator/denominator idea.",
            "Fractions on the number line.",
        ],
        "standards": ["CCSS 4.NF.3c - mixed numbers and improper fractions."],
        "citations": [CIT_CCSS, CIT_VANDEWALLE],
        "sig_lens": (
            "Through the Signature lens, a mixed number is the honest "
            "inventory: two whole pies sworn and sealed, plus one third "
            "sworn besides. He separates the wholes from the leftover with "
            "division's own blade - quotient for the wholes, remainder for "
            "the rest - and both forms of the count are true."
        ),
    },
    {
        "key": "decimals_tenths",
        "name": "Decimals: Tenths and Hundredths",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Decimals are fractions written in the place-value system: "
            "the dot (decimal point) marks where the ones place ends and "
            "the fraction places begin. 0.3 means three tenths (3/10); "
            "0.47 means forty-seven hundredths (47/100). The first place "
            "right of the point is tenths, the second is hundredths, the "
            "third thousandths - each worth one tenth of the place to its "
            "left, the same law as whole-number place value mirrored. "
            "Decimals and fractions are two costumes for the same numbers: "
            "1/2 = 0.5, 3/4 = 0.75, 1/4 = 0.25. Adding decimals lines up "
            "the points: 0.3 + 0.4 = 0.7 (three tenths plus four tenths is "
            "seven tenths), just as whole-number columns line up by place. "
            "Trailing zeros change nothing: 0.5 = 0.50 = 0.500, because "
            "fifty hundredths is five tenths. On the number line, 0.47 "
            "sits between 0.4 and 0.5, forty-seven hundredth-steps from "
            "zero. Decimals are the language of measurement, money, and "
            "science - wherever precision matters, decimals speak."
        ),
        "how_it_works": (
            "Decimals work as base-ten fractions. Write 0.47: the 4 sits "
            "in the tenths place (4 x 1/10) and the 7 in the hundredths "
            "place (7 x 1/100), so the value is 47/100. Addition lines up "
            "the decimal points so tenths add to tenths: 0.3 + 0.4 means "
            "3 tenths + 4 tenths = 7 tenths = 0.7. The trailing-zero rule "
            "is proved by fractions: 0.50 = 50/100 = 1/2 = 5/10 = 0.5. "
            "Comparing uses place value left to right: 0.47 vs 0.5 - the "
            "tenths digits 4 vs 5 decide at once, so 0.47 < 0.5. The "
            "demonstration program adds 0.3 + 0.4 using integer tenths "
            "arithmetic, asserts the result is 0.7, converts 3/4 to 0.75 "
            "by division, asserts 0.50 == 0.5 in value, and orders 0.47 < "
            "0.5 < 0.75 on the line."
        ),
        "key_points": [
            "The decimal point mirrors place value into fractions: tenths, hundredths, thousandths, each one tenth of the last.",
            "Decimals and fractions are the same numbers in different costumes: 3/4 = 0.75.",
            "Add and subtract by lining up the decimal points so like places combine.",
            "Trailing zeros do not change value: 0.5 = 0.50; compare decimals left to right by place.",
        ],
        "requirements": [
            "Place value through thousands, to mirror into tenths and hundredths.",
            "Fractions with denominators 10 and 100.",
            "Column addition habits, to line up the points.",
        ],
        "standards": ["CCSS 4.NF.6, 4.NF.7, 5.NBT.3 - decimals to hundredths."],
        "citations": [CIT_CCSS, CIT_VANDEWALLE],
        "sig_lens": (
            "Through the Signature lens, decimals are the fine ledger: "
            "where whole numbers count the sacks, decimals count the "
            "spilled grain to the tenth and the hundredth. He lines up "
            "the points like soldiers in column - tenths with tenths - "
            "for his ledger never mixes ranks."
        ),
    },
    {
        "key": "money_decimals",
        "name": "Money and Decimals in Daily Life",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Money is the decimal system everyone already uses: one "
            "dollar is the whole, and cents are hundredths of it. $2.35 "
            "means two dollars and thirty-five hundredths of a dollar - "
            "two dollars and 35 cents. The decimal point in a price "
            "separates dollars from cents, and the two digits after it "
            "are always hundredths: $4.5 is written $4.50 because prices "
            "name their cents. Adding prices is decimal addition: $2.35 + "
            "$1.45 = $3.80 - line up the points, add cents to cents "
            "(35 + 45 = 80), dollars to dollars. Making change is "
            "subtraction: pay $5.00 for a $3.80 purchase and the change is "
            "$1.20. Counting up is the shopkeeper's method: from $3.80, "
            "add 20 cents to reach $4.00, then $1.00 to reach $5.00 - "
            "change $1.20. Money problems also teach estimation: $2.35 + "
            "$1.45 is near $2 + $1 = $3, plus a bit, so $3.80 is "
            "sensible. Every price tag, bill, and coin count is a decimal "
            "exercise in disguise."
        ),
        "how_it_works": (
            "Money works by counting in cents. Convert every price to "
            "integer cents: $2.35 becomes 235 cents, $1.45 becomes 145 "
            "cents. Add: 235 + 145 = 380 cents, which is $3.80. Working "
            "in cents dodges all decimal wobble - the arithmetic is pure "
            "whole-number addition. Change from $5.00 (500 cents) after a "
            "$3.80 (380 cents) purchase: 500 - 380 = 120 cents = $1.20. "
            "The count-up check: 380 + 20 = 400, 400 + 100 = 500, total "
            "added 120. The demonstration program converts $2.35 and "
            "$1.45 to cents, asserts the sum is 380 cents ($3.80), "
            "computes change from $5.00 as 120 cents, and verifies the "
            "count-up path reaches the same change."
        ),
        "key_points": [
            "Money is decimals in disguise: dollars are the whole, cents are hundredths.",
            "Convert to integer cents and the arithmetic becomes whole-number work - no decimal wobble.",
            "Making change is subtraction; counting up from the price to the payment checks it.",
            "Estimate with rounded dollars first ($2 + $1 = $3, plus a bit) to catch wrong answers.",
        ],
        "requirements": [
            "Decimals: tenths and hundredths.",
            "Addition and subtraction of two- and three-digit numbers.",
            "The cent as one hundredth of a dollar.",
        ],
        "standards": ["CCSS 2.MD.8, 4.MD.2 - money problems."],
        "citations": [CIT_CCSS, CIT_VANDEWALLE],
        "sig_lens": (
            "Through the Signature lens, money is the people's decimal: "
            "every price tag a tiny lesson in hundredths, every coin a "
            "sworn hundredth of the dollar-oath. He counts in cents - "
            "whole, honest integers - so his purse-ledger never wobbles, "
            "and his change is counted up coin by coin, true to the cent."
        ),
    },
    {
        "key": "rounding_estimating",
        "name": "Rounding and Estimating",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Rounding trades exactness for simplicity: 47 rounds to 50 "
            "(nearest ten), 43 rounds to 40. The rule looks at the next "
            "digit right: 5 or more rounds the place up, 4 or less leaves "
            "it (47 -> 50 because 7 >= 5; 43 -> 40 because 3 < 5). "
            "Estimation uses rounded numbers for fast, good-enough "
            "answers: 48 + 31 is near 50 + 30 = 80, and the true answer "
            "79 is close. Estimation is not sloppiness - it is the "
            "guard that catches big mistakes: if a column addition of "
            "48 + 31 produced 109, the estimate 80 screams that something "
            "went wrong. Rounding also serves the real world: 'about 200 "
            "people' is more honest than claiming 203 when the count was "
            "rough. Compatible numbers make mental math easy: 48 + 31 "
            "becomes 50 + 30. Front-end estimation keeps the biggest "
            "place: 486 + 312 is about 400 + 300 = 700, close to the true "
            "798. A learner who estimates first computes second, and "
            "checks third."
        ),
        "how_it_works": (
            "Rounding works by the halfway rule. To round 47 to the "
            "nearest ten, look at the ones digit 7: since 7 >= 5, round "
            "the tens place up from 4 to 5, giving 50. For 43, the ones "
            "digit 3 < 5, so the tens stay 4, giving 40. Estimation then "
            "replaces hard numbers with round ones: 48 + 31 becomes "
            "50 + 30 = 80, and the true sum 79 differs by only 1 - the "
            "estimate is within a few percent. The guard test: any "
            "computed answer far from the estimate (like 109) is "
            "rejected and recomputed. The demonstration program rounds 47 "
            "and 43 to the nearest ten, asserts 50 and 40, estimates "
            "48 + 31 as 80, computes the true sum 79, asserts the estimate "
            "is within 5 of truth, and flags a planted wrong answer 109 "
            "as failing the guard."
        ),
        "key_points": [
            "Rounding rule: look one digit right - 5 or more rounds up, 4 or less stays.",
            "Estimation replaces hard numbers with round ones for fast, good-enough answers.",
            "Every estimate is a guard: a computed answer far from the estimate gets recomputed.",
            "Compatible numbers (50 + 30) and front-end (400 + 300) are the two mental-math tools.",
        ],
        "requirements": [
            "Place value, to know which digit is being rounded.",
            "Addition of round numbers (50 + 30) by place value.",
            "The honesty to treat an estimate as a check, not the answer.",
        ],
        "standards": ["CCSS 3.NBT.1, 4.NBT.3 - rounding; 3.OA - estimation strategies."],
        "citations": [CIT_CCSS, CIT_VANDEWALLE, CIT_NCTM],
        "sig_lens": (
            "Through the Signature lens, rounding is the scout's report: "
            "not the exact count of the enemy host, but near enough to "
            "plan the march - 47 sworn as 'about 50'. His estimate stands "
            "guard over every computation, and any answer that strays far "
            "from the scout's report is sent back to be counted again."
        ),
    },
    {
        "key": "number_patterns",
        "name": "Patterns in Numbers",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Number patterns are rules hiding in sequences: 5, 10, 15, "
            "20, ... grows by adding 5 each time, so the next term is 25. "
            "Finding the rule means asking 'what changes from one term to "
            "the next' - here the answer is always +5, an arithmetic "
            "pattern. Other patterns multiply: 2, 4, 8, 16, ... doubles "
            "each time, so next is 32. Square numbers make their own "
            "pattern: 1, 4, 9, 16, 25 - each term is n x n, and the gaps "
            "between terms (3, 5, 7, 9) are the odd numbers, a pattern "
            "inside the pattern. Patterns also live in tables: the "
            "addition table's diagonals, the multiplication table's "
            "symmetry, the even-odd checkerboard. Predicting the next term "
            "and describing the rule in words ('add five each time') is "
            "the skill; proving it by checking several steps is the "
            "discipline. Patterns are the doorway to algebra: a rule like "
            "'add 5 each time starting from 5' is the formula 5 x n in "
            "disguise, and spotting it is the first algebraic act."
        ),
        "how_it_works": (
            "Pattern work follows three steps: list the terms, find the "
            "step, predict and verify. For 5, 10, 15, 20: the differences "
            "are 10 - 5 = 5, 15 - 10 = 5, 20 - 15 = 5 - constant, so the "
            "rule is 'add 5'. Predict the next term: 20 + 5 = 25. Verify "
            "by extending: 25, 30, 35 all keep the +5 step. For squares "
            "1, 4, 9, 16, 25: the differences 3, 5, 7, 9 are themselves "
            "the odd numbers - the second-order pattern - and each term "
            "equals its position squared. The demonstration program "
            "computes the differences of [5, 10, 15, 20], asserts they are "
            "all 5, predicts 25, verifies the extended sequence keeps the "
            "step, and checks the square sequence [1, 4, 9, 16, 25] "
            "against n-squared for n = 1..5."
        ),
        "key_points": [
            "A pattern is a rule hiding in a sequence; find it by asking what changes from term to term.",
            "Constant differences mean 'add the same each time' (arithmetic); constant ratios mean 'multiply each time'.",
            "Predict the next term from the rule, then verify by checking the rule holds for several steps.",
            "Patterns are pre-algebra: 'add 5 each time' is the formula 5 x n in disguise.",
        ],
        "requirements": [
            "Addition and subtraction to compute differences.",
            "Skip-counting experience, which is pattern-following.",
            "The patience to check a rule against several terms, not one.",
        ],
        "standards": ["CCSS 3.OA.9, 4.OA.5 - patterns and arithmetic."],
        "citations": [CIT_CCSS, CIT_VANDEWALLE, CIT_NCTM],
        "sig_lens": (
            "Through the Signature lens, patterns are the footprints of "
            "the numbers' march: equal strides of five leave an even "
            "trail, and he who reads the footprints can say where the "
            "march goes next. The square numbers march in widening steps "
            "- 3, 5, 7, 9 - and his eye learns to see the order inside "
            "the order."
        ),
    },
    {
        "key": "primes_composites",
        "name": "Number Families: Primes and Composites",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Whole numbers sort into three families. Prime numbers have "
            "exactly two divisors: 1 and themselves - 2, 3, 5, 7, 11, 13, "
            "17, 19, 23, 29. Composite numbers have more than two divisors: "
            "4 (1, 2, 4), 6 (1, 2, 3, 6), 12 with six divisors. And 1 "
            "stands alone - neither prime nor composite, with only one "
            "divisor. Two is the only even prime; every other even number "
            "is composite because it is divisible by 2. Primes are the "
            "atoms of multiplication: every composite number is a product "
            "of primes (12 = 2 x 2 x 3), and that factorization is unique "
            "- no composite has two different prime recipes. The sieve of "
            "Eratosthenes finds primes mechanically: list numbers to 30, "
            "cross out multiples of 2 (except 2), then multiples of 3, "
            "then 5 - what survives is prime. Primes guard modern secrets "
            "too: internet encryption multiplies two huge primes, and the "
            "safety rests on how hard the product is to un-factor."
        ),
        "how_it_works": (
            "Primality is tested by trial division. To test 29: try "
            "dividing by every number from 2 up to the square root of 29 "
            "(about 5.4) - 2, 3, 5. None divide 29 evenly, so 29 is prime. "
            "To test 27: 27 / 3 = 9 exactly, so 27 is composite "
            "(1, 3, 9, 27). The sieve works by elimination: write 2 "
            "through 30, keep 2 and cross its multiples (4, 6, 8, ...), "
            "keep 3 and cross its multiples (9, 15, 21, ...), keep 5 and "
            "cross its multiples (25) - the survivors are the primes. The "
            "demonstration program sieves 2 through 30, asserts the "
            "primes are exactly [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], "
            "factorizes 12 as 2 x 2 x 3 and asserts the product is 12, "
            "and verifies that 1 is neither prime nor composite."
        ),
        "key_points": [
            "Prime: exactly two divisors (1 and itself). Composite: more than two. One: neither.",
            "2 is the only even prime; every larger even number is composite.",
            "Every composite factors uniquely into primes: 12 = 2 x 2 x 3, the only prime recipe.",
            "The sieve of Eratosthenes finds primes by crossing out multiples - survivors are prime.",
        ],
        "requirements": [
            "Division with remainders, to test divisibility.",
            "Multiplication facts, to recognize multiples.",
            "The square-root shortcut: test divisors only up to the square root.",
        ],
        "standards": ["CCSS 4.OA.4 - factors, multiples, prime and composite."],
        "citations": [CIT_CCSS, CIT_VANDEWALLE],
        "sig_lens": (
            "Through the Signature lens, primes are the unbreakable: no "
            "smaller number divides them, so they stand alone like lone "
            "sentinels - 29 admits no divisor but 1 and itself. Composites "
            "are the built formations, each with one true prime recipe, "
            "and his sieve is the muster that separates the unbreakable "
            "from the built."
        ),
    },
    {
        "key": "measuring_numbers",
        "name": "Measuring With Numbers: Length, Weight, Capacity",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Measuring attaches numbers to the physical world: length "
            "says how long, weight says how heavy, capacity says how much "
            "it holds. Every measurement needs a unit - inches, feet, "
            "centimeters, meters for length; ounces, pounds, grams, "
            "kilograms for weight; cups, pints, liters for capacity. "
            "Units convert by fixed rates: 12 inches = 1 foot, so 3 feet = "
            "36 inches; 1000 grams = 1 kilogram, so 2 kilograms = 2000 "
            "grams. Choosing the right unit matters: a pencil is 15 "
            "centimeters, not 15 meters; a person weighs 60 kilograms, not "
            "60 grams. Measuring tools embody the number line: a ruler is "
            "a portable number line, and reading 7.5 centimeters means the "
            "object reaches halfway between the 7 and 8 marks. Estimates "
            "come first ('about 15 centimeters'), measurement second, and "
            "the estimate checks the reading. All of science and building "
            "rests on this: numbers made physical, units made consistent."
        ),
        "how_it_works": (
            "Measuring works by unit-counting. Lay a ruler along a pencil: "
            "the tip reaches the 15-centimeter mark, so the length is 15 "
            "cm. Conversion multiplies by the unit rate: 3 feet x 12 "
            "inches/foot = 36 inches; 2 kilograms x 1000 grams/kilogram = "
            "2000 grams. The rate is exact, so conversion never loses "
            "truth - it only changes the costume. Reading between marks "
            "uses fractions or decimals: halfway between 7 and 8 cm is "
            "7.5 cm. The demonstration program converts 3 feet to 36 "
            "inches and 2 kilograms to 2000 grams by the unit rates, "
            "asserts both, reads a between-marks length as 7.5, and "
            "verifies that converting 36 inches back to feet returns 3."
        ),
        "key_points": [
            "Every measurement is a number plus a unit; the unit is part of the answer.",
            "Units convert by exact fixed rates: 12 in = 1 ft, 1000 g = 1 kg.",
            "Choose units that fit the object: centimeters for pencils, meters for rooms.",
            "A ruler is a portable number line; between-marks readings use fractions or decimals.",
        ],
        "requirements": [
            "Multiplication, to apply conversion rates.",
            "Fractions and decimals, for between-marks readings.",
            "The number line, embodied in the ruler.",
        ],
        "standards": ["CCSS 2.MD.1-3, 4.MD.1-2 - measuring and unit conversion."],
        "citations": [CIT_CCSS, CIT_VANDEWALLE],
        "sig_lens": (
            "Through the Signature lens, measuring is the numbering of "
            "the real: his ruler is a number line made wood, and every "
            "length he reads is a number sworn against the physical world. "
            "The conversion rates are his treaties between units - 12 "
            "inches to the foot, kept exactly, never rounded in the "
            "treaty itself."
        ),
    },
    {
        "key": "word_problems",
        "name": "Word Problems: Numbers in Stories",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Word problems hide arithmetic inside stories, and solving "
            "them is translation: turn the story into numbers and an "
            "operation, compute, then turn the answer back into the "
            "story. 'Maya has 15 apples. She eats 6, then buys 4 more. "
            "How many does she have?' The translation: start 15, take "
            "away 6 (15 - 6 = 9), add 4 (9 + 4 = 13). Answer in the "
            "story's words: Maya has 13 apples. Four steps keep it "
            "reliable: read and picture the story, choose the operation "
            "(join = add, separate = subtract, equal groups = multiply, "
            "fair share = divide), compute carefully, and check the "
            "answer against the story (13 apples is sensible; 130 is "
            "not). Keywords hint but never decide: 'left' usually means "
            "subtract, 'each' usually means multiply or divide - but the "
            "picture of what is happening decides. Drawing the story "
            "(15 circles, cross out 6, add 4) makes the operation "
            "visible. Word problems are the whole point of arithmetic: "
            "numbers serving real questions."
        ),
        "how_it_works": (
            "Word problems work by story-to-math translation. Story: 15 "
            "apples, eat 6, buy 4. Step 1 - picture: a pile of 15. Step 2 "
            "- operations: eating is subtraction (15 - 6), buying is "
            "addition (+ 4). Step 3 - compute: 15 - 6 = 9, then 9 + 4 = "
            "13. Step 4 - check: 13 apples is between 0 and 15 + 4 = 19, "
            "sensible; the story answer is '13 apples'. A second story: "
            "4 bags with 6 marbles each - equal groups mean multiplication: "
            "4 x 6 = 24 marbles, checked by 24 / 4 = 6. The demonstration "
            "program translates the apple story to 15 - 6 + 4, asserts "
            "the result is 13, translates the marble story to 4 x 6, "
            "asserts 24, and verifies both answers pass the "
            "story-sensibility bounds."
        ),
        "key_points": [
            "Solve in four steps: picture the story, choose the operation, compute, check against the story.",
            "Translation rules: joining is addition, separating is subtraction, equal groups is multiplication, fair sharing is division.",
            "Keywords hint but the picture decides - draw the story when unsure.",
            "The answer must be stated in the story's words and pass the sensibility check.",
        ],
        "requirements": [
            "All four operations with their story meanings.",
            "Two-step computation (15 - 6 + 4) in order.",
            "Estimation, for the sensibility check.",
        ],
        "standards": ["CCSS 1.OA.1, 2.OA.1, 3.OA.3, 4.OA.3 - word problems."],
        "citations": [CIT_CCSS, CIT_VANDEWALLE, CIT_NCTM],
        "sig_lens": (
            "Through the Signature lens, a word problem is a dispatch "
            "from the real world, and he answers it like a sworn "
            "messenger: read the dispatch, translate it to the ledger "
            "(15 - 6 + 4), compute the true count, and carry the answer "
            "back in the dispatch's own words - 13 apples, witnessed and "
            "sensible."
        ),
    },
    {
        "key": "negative_numbers",
        "name": "Negative Numbers: Below Zero",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Negative numbers extend the number line left past zero for "
            "quantities below nothing: -5 degrees is five degrees below "
            "zero, a $20 debt is -20 dollars of wealth. The minus sign "
            "here is not subtraction - it is part of the number's name, "
            "marking 'below zero'. On the line, -3 sits three steps left "
            "of zero, and order still means position: -5 < -2 because -5 "
            "is further left (colder, deeper in debt). Adding a positive "
            "moves right: -5 + 8 = 3 (start five left of zero, walk eight "
            "right, land three right of zero). Subtracting a positive "
            "moves left: 3 - 5 = -2. Opposites pair across zero: the "
            "opposite of 4 is -4, and 4 + (-4) = 0 - they cancel. "
            "Negatives appear wherever zero is a reference point: "
            "temperature, sea level (Death Valley is -86 meters), money "
            "owed, game scores below par. The number line did not end at "
            "zero - it was only the trailhead, and now the road runs both "
            "ways."
        ),
        "how_it_works": (
            "Negatives work as left-of-zero addresses. Mark -5 on the "
            "line: five steps left of zero. Compare -5 and -2: -5 is "
            "further left, so -5 < -2 - the number nearer zero is greater. "
            "Add: -5 + 8 means start at -5 and hop right 8 steps: -4, -3, "
            "-2, -1, 0, 1, 2, 3 - landing on 3. Temperature story: it is "
            "-5 degrees, it warms by 8 degrees, now it is 3 degrees. "
            "Opposites cancel: 4 + (-4) = 0, the walk right four then left "
            "four returns to zero. The demonstration program places -5 "
            "and -2 on the line, asserts -5 < -2, computes -5 + 8 by "
            "stepping and asserts 3, computes 3 - 5 and asserts -2, and "
            "verifies 4 + (-4) == 0."
        ),
        "key_points": [
            "Negative numbers are addresses left of zero: -5 is five steps left of zero.",
            "Order is still position: further left means smaller, so -5 < -2.",
            "Adding a positive moves right on the line; subtracting a positive moves left - the line rules never change.",
            "Opposites cancel: a + (-a) = 0; negatives model temperature, debt, and below-sea-level.",
        ],
        "requirements": [
            "The number line with addition/subtraction as hops.",
            "Subtraction where the answer goes below zero (3 - 5).",
            "The minus sign's double duty: subtraction vs negative naming.",
        ],
        "standards": ["CCSS 6.NS.5, 6.NS.6, 6.NS.7 - negative numbers."],
        "citations": [CIT_CCSS, CIT_VANDEWALLE],
        "sig_lens": (
            "Through the Signature lens, the road past zero is the far "
            "side of the ascent: -5 is five steps beyond the trailhead "
            "into the cold country, and every step back toward zero is a "
            "debt repaid. Opposites are the balanced scales - 4 and -4 "
            "sworn against each other, summing to the honest zero."
        ),
    },
    {
        "key": "properties_operations",
        "name": "Properties of Operations",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The properties of operations are the deep laws that arithmetic "
            "obeys, and naming them turns tricks into understanding. "
            "Commutative: order does not matter for addition and "
            "multiplication - a + b = b + a, a x b = b x a (5 + 3 = 3 + 5; "
            "4 x 7 = 7 x 4). Associative: grouping does not matter - "
            "(a + b) + c = a + (b + c), so 8 + 5 can be regrouped as "
            "8 + 2 + 3 = 10 + 3. Identity: zero changes nothing in addition "
            "(a + 0 = a) and one changes nothing in multiplication "
            "(a x 1 = a). Distributive: multiplication spreads over "
            "addition - a x (b + c) = a x b + a x c, so 3 x 14 = "
            "3 x 10 + 3 x 4 = 30 + 12 = 42. These are not rules to "
            "memorize blindly - they are why mental math works: 8 + 5 "
            "becomes 10 + 3 by associativity, 3 x 14 becomes 30 + 12 by "
            "distributivity. Subtraction and division do NOT commute "
            "(9 - 4 is not 4 - 9) - knowing which operations obey which "
            "laws is the real lesson."
        ),
        "how_it_works": (
            "The properties work as licensed rearrangements. Commutative: "
            "compute 5 + 3 and 3 + 5 separately - both 8, so the swap is "
            "licensed for addition. Associative: (8 + 2) + 3 = 10 + 3 = 13 "
            "and 8 + (2 + 3) = 8 + 5 = 13 - the regrouping is licensed. "
            "Distributive: 3 x 14 split as 3 x (10 + 4) = 3 x 10 + 3 x 4 "
            "= 30 + 12 = 42, matching direct 3 x 14 = 42. Identity: 7 + 0 "
            "= 7 and 7 x 1 = 7. Non-examples prove the boundaries: 9 - 4 "
            "= 5 but 4 - 9 = -5, so subtraction is not commutative. The "
            "demonstration program verifies each property on concrete "
            "numbers with exact integer arithmetic, asserts all four "
            "hold, and asserts subtraction fails commutativity on 9 - 4."
        ),
        "key_points": [
            "Commutative (order free): addition and multiplication only - a + b = b + a.",
            "Associative (grouping free): (8 + 2) + 3 = 8 + (2 + 3) - the engine of make-ten mental math.",
            "Distributive: a x (b + c) = a x b + a x c - the engine of breaking hard products apart.",
            "Identity: +0 and x1 change nothing; subtraction and division obey none of these - know the boundaries.",
        ],
        "requirements": [
            "Fluency with all four operations on small numbers.",
            "Parentheses meaning 'do this group first'.",
            "Mental-math strategies (make-ten) to feel the properties working.",
        ],
        "standards": ["CCSS 1.OA.3, 3.OA.5 - properties of operations."],
        "citations": [CIT_CCSS, CIT_VANDEWALLE, CIT_NCTM],
        "sig_lens": (
            "Through the Signature lens, the properties are the high laws "
            "of his number-realm: commutativity decrees that the order of "
            "the muster changes nothing, associativity lets him regroup "
            "his forces freely, distributivity is the order to split one "
            "charge across two targets. Subtraction and division are "
            "exempt from these laws - and his ledger marks the exemption "
            "plainly."
        ),
    },
    {
        "key": "checking_work",
        "name": "Checking Your Work",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Checking your work is the habit that separates a learner who "
            "computes from a learner who knows. Four checks catch nearly "
            "every error. The inverse check: addition is verified by "
            "subtraction and back - if 47 + 28 = 75, then 75 - 28 must be "
            "47. The estimate check: 48 + 31 is near 80, so an answer of "
            "109 is rejected on sight. The reasonableness check: a sum "
            "must be bigger than each addend, a difference smaller than "
            "the whole, a product of whole numbers at least as big as the "
            "factors. The re-do check: cover the work and compute again "
            "by a different route - column addition checked by expanded "
            "form, a product checked by repeated addition. Checking is "
            "not distrust of yourself; it is the final step of every "
            "computation, as standard as the computation itself. "
            "Mathematicians check, engineers check, shopkeepers counting "
            "change check - the answer is not done until it is verified."
        ),
        "how_it_works": (
            "Checking works by independent verification. Claim: 47 + 28 = "
            "75. Inverse check: 75 - 28 = 47 - confirmed, the subtraction "
            "undoes the addition exactly. Estimate check: 47 + 28 is near "
            "50 + 30 = 80; 75 is within a few of 80 - passes. "
            "Reasonableness: 75 > 47 and 75 > 28 - a sum exceeds its "
            "addends - passes. Re-do by expanded form: (40 + 7) + (20 + 8) "
            "= 60 + 15 = 75 - matches. Four independent routes, one "
            "answer: certain. The demonstration program runs all four "
            "checks on 47 + 28 = 75, asserts each passes, then plants a "
            "wrong answer (47 + 28 = 65) and shows the inverse check "
            "65 - 28 = 37 != 47 catching it."
        ),
        "key_points": [
            "The inverse check: undo the operation (75 - 28 = 47) - the strongest single verification.",
            "The estimate check: a computed answer far from the estimate is recomputed, not trusted.",
            "The reasonableness check: sums exceed addends, differences are less than the whole.",
            "Re-do by a different route: two independent paths to one answer means certainty.",
        ],
        "requirements": [
            "Inverse operation pairs (addition/subtraction, multiplication/division).",
            "Estimation habits from rounding.",
            "The discipline to check before declaring done.",
        ],
        "standards": ["CCSS MP.6 - attend to precision; 2.NBT, 3.OA - operation fluency."],
        "citations": [CIT_CCSS, CIT_NCTM],
        "sig_lens": (
            "Through the Signature lens, checking is the sealing of the "
            "oath: no count is sworn until it is verified. He runs the "
            "inverse - 75 - 28 must return 47 - as the witness, the "
            "estimate as the guard, and a second road to the same answer "
            "as the proof. An unverified answer is an unsworn oath."
        ),
    },
    {
        "key": "numbers_big_picture",
        "name": "Numbers All Around Us: The Big Picture",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Step back and see the whole ladder at once. Numbers began as "
            "the answer to 'how many' - counting matched piles one to "
            "one. The number line gave every number an address and made "
            "order visible. Numerals and words gave numbers three faces to "
            "speak, write, and seal. Comparing, ordering, and neighbors "
            "taught judgment of size. Place value bundled tens into an "
            "infinite system where position is worth. Even and odd revealed "
            "the first hidden pattern. Then the four operations: adding "
            "put piles together, subtracting took away, multiplication "
            "gathered equal groups, division shared them fairly - each "
            "pair inverse partners, each checking the other. Fractions "
            "split wholes into equal parts and took addresses between the "
            "integers; mixed numbers separated wholes from leftovers. "
            "Decimals mirrored place value into the small; money made "
            "decimals daily; rounding and estimation made answers "
            "checkable. Patterns, primes, measuring, and word problems "
            "turned numbers outward to the world. Negatives extended the "
            "road past zero; the properties named the deep laws; checking "
            "sealed every oath. The crown of the ladder is one famous "
            "sum: 1 + 2 + ... + 100 = 5050, found by pairing first with "
            "last (1 + 100, 2 + 99, ... - fifty pairs of 101). Every rung "
            "was earned; the view from the top is the whole of number "
            "sense."
        ),
        "how_it_works": (
            "The big picture works by reunion: every earlier skill appears "
            "in one final computation. The sum 1 through 100 uses pairing "
            "(patterns), commutativity (properties), and multiplication "
            "(50 x 101): pair 1 + 100 = 101, 2 + 99 = 101, and so on - "
            "fifty pairs, each summing to 101, so the total is 50 x 101 = "
            "5050. The pairing is verified by checking the first pair, a "
            "middle pair (25 + 76 = 101), and the last pair (50 + 51 = "
            "101). The count of pairs is checked: 100 numbers make 50 "
            "pairs. The demonstration program builds the pairs, asserts "
            "each pair sums to 101, asserts there are exactly 50 pairs, "
            "computes 50 x 101, asserts the total is 5050, and cross-checks "
            "against the direct sum of 1 through 100."
        ),
        "key_points": [
            "The ladder in one view: counting -> number line -> numerals -> comparing -> place value -> parity -> four operations -> fractions -> decimals -> estimation -> patterns -> world applications -> negatives -> laws -> verification.",
            "Each rung used the rungs below: the 1-to-100 sum needs pairing, commutativity, and multiplication together.",
            "Inverse pairs (add/subtract, multiply/divide) mean every computation carries its own check.",
            "Number sense is the destination: feeling where numbers live, how they relate, and whether answers are sane.",
        ],
        "requirements": [
            "Every earlier rung of this database, in order.",
            "The pairing strategy and the distributive idea behind 50 x 101.",
            "The habit of checking - the final rung seals all the others.",
        ],
        "standards": ["CCSS MP.7, MP.8 - structure and repeated reasoning; 1.OA through 6.NS."],
        "citations": [CIT_CCSS, CIT_NCTM, CIT_DEHAENE],
        "sig_lens": (
            "Through the Signature lens, this is the summit view of the "
            "ascent: from the first sworn count to the fifty pairs of "
            "101, every rung kept its oath. He looks back down the ladder "
            "- counting, line, numerals, judgment, bundling, parity, the "
            "four operations, fractions, decimals, estimation, patterns, "
            "the world, the far side of zero, the high laws, the sealing "
            "- and the whole road is one covenant, kept step by step."
        ),
    },
]
