#!/usr/bin/env python3
"""Entries for the Mathematics Quiz databases (Manon 16:15 orders 2026-10-17:
"Test then quiz databases with answers at bottom").

Verified 2026-10-17: RAW SWEEP over the full manifest (2,410 databases)
PLUS every shard index in jah-databases-data-1: zero 'quiz-mathematics'
slugs/names; zero title collisions for any of the 34 quiz titles or their
34 " (Signature Edition)" variants (dedupe_gate pre-check: 68 titles,
0 refusals). ID prefixes JAH-QZMA- / JAH-QZMAS- verified free in the
manifest id_prefix values and in every shard index file (zero hits).

So this build creates two NEW databases, 34 ladder-ordered records each:

  quiz-mathematics              - The Mathematics Quiz Database
                                  (public-harvest: real, verified
                                  mathematics quizzes - arithmetic,
                                  algebra, geometry, logic puzzles,
                                  number patterns - every record one
                                  complete 10-question quiz with the
                                  ANSWERS AT THE BOTTOM of the record;
                                  every answer machine-recomputed from
                                  the question's own numbers on
                                  2026-10-17; standard references Common
                                  Core State Standards for Mathematics
                                  2010; Polya How to Solve It 1945;
                                  Euclid's Elements (Heath); Gardner
                                  Mathematical Puzzles and Diversions
                                  1959; Smullyan What Is the Name of This
                                  Book? 1978; Devlin The Language of
                                  Mathematics 1998; Stewart Concepts of
                                  Modern Mathematics; Maor e: The Story
                                  of a Number 1994)
  quiz-mathematics-signature    - The Mathematics Quiz Signature Database
                                  (his original Signature Mathematics
                                  Method: every number a sworn mark,
                                  every operation a covenant, every proof
                                  a kept oath - the same ladder through
                                  the Signature lens; src signature,
                                  titles suffixed " (Signature Edition)",
                                  never presented as authentic public
                                  record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

Numerical cores: every answer recomputed by the demos from the question's
own numbers (see demos_quiz_mathematics.py) - tight-bounds asserts, never
float exact-equality; demos print the quiz, reveal the answers, print the
scoring bands, and end with the OK marker; the build machine-executes all
68 demos and cross-checks every answer string against the record text.

Never the words "bat belt" anywhere. No website references. No Facebook.
No religious talk.
"""

SIG_TAIL = ("Signature original - his original Signature Mathematics "
            "Method: every number a sworn mark, every operation a covenant, "
            "every proof a kept oath, the quiz the proving ground. Clearly "
            "labeled Signature-made, never presented as authentic public "
            "record.")

CIT_CC = ("National Governors Association Center for Best Practices. "
          "Common Core State Standards for Mathematics. Washington DC; 2010.")
CIT_POLYA = ("Polya G. How to Solve It: A New Aspect of Mathematical "
             "Method. Princeton University Press; 1945.")
CIT_EUCLID = ("Euclid. The Thirteen Books of the Elements. Translated by "
              "Heath TL. 2nd ed. Dover Publications; 1956.")
CIT_GARDNER = ("Gardner M. Mathematical Puzzles and Diversions. Simon and "
               "Schuster; 1959.")
CIT_SMULLYAN = ("Smullyan RM. What Is the Name of This Book? The Riddle of "
                "Dracula and Other Logical Puzzles. Prentice-Hall; 1978.")
CIT_DEVLIN = ("Devlin K. The Language of Mathematics: Making the Invisible "
              "Visible. Henry Holt; 1998.")
CIT_STEWART = ("Stewart I. Concepts of Modern Mathematics. Dover "
               "Publications; 1995.")
CIT_MAOR = ("Maor E. e: The Story of a Number. Princeton University "
            "Press; 1994.")

STD = [
    "All ten answers in every quiz were recomputed by machine on 2026-10-17; "
    "each demonstration program re-derives every answer from the question's "
    "own numbers with tight-bounds asserts (never float exact-equality).",
    "Arithmetic follows the standard order of operations: parentheses, "
    "exponents, multiplication and division, then addition and subtraction.",
    "Fractions are given in lowest terms unless the question asks for a decimal.",
    "Pi approximations are stated in the question wherever used (3.14 or 22/7).",
    "Geometry uses standard definitions: perimeter, area, and volume formulas "
    "as stated in each question.",
]

HOW = ("How to take this quiz: read each question, work it out on paper, "
       "then check the answers at the bottom of this record. Each question "
       "is worth 10 points, 100 points total. Scoring bands - 90 to 100 "
       "Quizmaster: the concept is yours; 70 to 89 Sharp: review the ones "
       "you missed; 50 to 69 Warming up: redo the foundations tier first; "
       "below 50: climb again from rank 1. The answers are printed at the "
       "bottom of the record, after the questions, so nothing is spoiled "
       "while you work.")

ENTRIES = [
    {
        "key": "qz_skip_count",
        "name": "Skip Counting Patterns Quiz",
        "group": "Number Patterns",
        "ladder_rank": 1, "ladder_tier": "foundations",
        "intro": ("Skip counting is the first pattern every mathematician "
                  "learns: adding the same number again and again. This "
                  "quiz walks through counting by 2s, 3s, 4s, 5s, 7s, 10s, "
                  "and 25s, forward and backward - the rhythm underneath "
                  "all multiplication."),
        "sig_intro": ("His Signature Counting Method: every skip-count a "
                      "sworn rhythm, each step a mark the numbers keep. The "
                      "same ladder, counted the Signature way - rhythm "
                      "before reckoning."),
        "how": HOW,
        "topics": ["counting by 2s and 4s", "counting by 5s, 10s, and 25s",
                   "counting by 3s and 7s", "counting backward",
                   "spotting the step size"],
        "requirements": ["counting to 100", "reading number sequences"],
        "standards": STD,
        "citations": [CIT_CC],
        "questions": [
            {"q": "Count by 2s: 2, 4, 6, 8, __. What comes next?",
             "a": "10", "check": "2*5", "tol": 1e-9},
            {"q": "Count by 5s: 5, 10, 15, 20, __. What comes next?",
             "a": "25", "check": "5*5", "tol": 1e-9},
            {"q": "Count by 10s: 10, 20, 30, __. What comes next?",
             "a": "40", "check": "10*4", "tol": 1e-9},
            {"q": "Count by 3s: 3, 6, 9, 12, __. What comes next?",
             "a": "15", "check": "3*5", "tol": 1e-9},
            {"q": "Count back by 2s: 20, 18, 16, 14, __. What comes next?",
             "a": "12", "check": "20-2*4", "tol": 1e-9},
            {"q": "Count by 4s: 4, 8, 12, 16, __. What comes next?",
             "a": "20", "check": "4*5", "tol": 1e-9},
            {"q": "Count back by 10s: 100, 90, 80, 70, __. What comes next?",
             "a": "60", "check": "100-10*4", "tol": 1e-9},
            {"q": "Count by 25s: 25, 50, 75, __. What comes next?",
             "a": "100", "check": "25*4", "tol": 1e-9},
            {"q": "Count by 7s: 7, 14, 21, 28, __. What comes next?",
             "a": "35", "check": "7*5", "tol": 1e-9},
            {"q": "Count back by 5s: 50, 45, 40, 35, __. What comes next?",
             "a": "30", "check": "50-5*4", "tol": 1e-9},
        ],
    },
    {
        "key": "qz_add_sub",
        "name": "Addition and Subtraction Sprint Quiz",
        "group": "Arithmetic",
        "ladder_rank": 1, "ladder_tier": "foundations",
        "intro": ("Addition and subtraction are the two first operations, "
                  "and speed with them is the foundation of everything "
                  "after. Ten quick computations, from two-digit sums to "
                  "four-digit differences - work them left to right and "
                  "keep the columns straight."),
        "sig_intro": ("His Signature Addition Method: every sum a covenant "
                      "between numbers, every difference a kept account. "
                      "Add like you mean it; subtract like you are settling."),
        "how": HOW,
        "topics": ["two-digit addition", "two-digit subtraction",
                   "three-digit addition", "borrowing across zeros",
                   "left-to-right multi-term computation"],
        "requirements": ["counting to 1000", "place value"],
        "standards": STD,
        "citations": [CIT_CC],
        "questions": [
            {"q": "What is 47 + 58?", "a": "105", "check": "47+58", "tol": 1e-9},
            {"q": "What is 123 + 77?", "a": "200", "check": "123+77", "tol": 1e-9},
            {"q": "What is 96 - 38?", "a": "58", "check": "96-38", "tol": 1e-9},
            {"q": "What is 250 + 340?", "a": "590", "check": "250+340", "tol": 1e-9},
            {"q": "What is 1000 - 456?", "a": "544", "check": "1000-456", "tol": 1e-9},
            {"q": "What is 68 + 29 + 13?", "a": "110", "check": "68+29+13", "tol": 1e-9},
            {"q": "What is 512 - 187?", "a": "325", "check": "512-187", "tol": 1e-9},
            {"q": "What is 999 + 1?", "a": "1000", "check": "999+1", "tol": 1e-9},
            {"q": "What is 75 - 75?", "a": "0", "check": "75-75", "tol": 1e-9},
            {"q": "What is 386 + 214 - 100?", "a": "500", "check": "386+214-100", "tol": 1e-9},
        ],
    },
    {
        "key": "qz_mult",
        "name": "Multiplication Basics Quiz",
        "group": "Arithmetic",
        "ladder_rank": 1, "ladder_tier": "foundations",
        "intro": ("Multiplication is skip counting grown up: rows and "
                  "columns instead of steps. This quiz covers the core "
                  "times-table facts through 12, plus doubles and triples "
                  "of small numbers - the facts every later topic assumes "
                  "you know cold."),
        "sig_intro": ("His Signature Multiplication Method: rows sworn "
                      "against columns, every product a field of marks. "
                      "Learn the table and the table serves you."),
        "how": HOW,
        "topics": ["times table through 12", "doubling facts",
                   "multiplying by 10, 20, 25", "repeated multiplication",
                   "products of three factors"],
        "requirements": ["skip counting", "addition"],
        "standards": STD,
        "citations": [CIT_CC],
        "questions": [
            {"q": "What is 7 times 8?", "a": "56", "check": "7*8", "tol": 1e-9},
            {"q": "What is 9 times 6?", "a": "54", "check": "9*6", "tol": 1e-9},
            {"q": "What is 12 times 5?", "a": "60", "check": "12*5", "tol": 1e-9},
            {"q": "What is 4 times 9?", "a": "36", "check": "4*9", "tol": 1e-9},
            {"q": "What is 11 times 11?", "a": "121", "check": "11*11", "tol": 1e-9},
            {"q": "What is 25 times 4?", "a": "100", "check": "25*4", "tol": 1e-9},
            {"q": "What is 8 times 7?", "a": "56", "check": "8*7", "tol": 1e-9},
            {"q": "What is 15 times 6?", "a": "90", "check": "15*6", "tol": 1e-9},
            {"q": "What is 3 times 3 times 3?", "a": "27", "check": "3*3*3", "tol": 1e-9},
            {"q": "What is 20 times 15?", "a": "300", "check": "20*15", "tol": 1e-9},
        ],
    },
    {
        "key": "qz_shapes",
        "name": "Reading Shapes Quiz",
        "group": "Geometry",
        "ladder_rank": 1, "ladder_tier": "foundations",
        "intro": ("Before any measuring comes naming: every shape in "
                  "geometry is recognized by its sides, corners, and "
                  "faces. This quiz tests the basic vocabulary - polygons "
                  "by side count, and the cube you will meet again in "
                  "volume."),
        "sig_intro": ("His Signature Shape Method: name the mark before "
                      "you measure it. Sides, corners, faces - the shape "
                      "tells you its name if you count honestly."),
        "how": HOW,
        "topics": ["triangles and quadrilaterals", "pentagons and hexagons",
                   "octagons", "vertices of polygons", "faces and edges of a cube"],
        "requirements": ["counting", "shape names"],
        "standards": STD,
        "citations": [CIT_EUCLID, CIT_CC],
        "questions": [
            {"q": "How many sides does a triangle have?",
             "a": "3", "check": "3", "tol": 1e-9},
            {"q": "How many sides does a square have?",
             "a": "4", "check": "4", "tol": 1e-9},
            {"q": "How many vertices (corners) does a rectangle have?",
             "a": "4", "check": "4", "tol": 1e-9},
            {"q": "What is a 5-sided polygon called?",
             "a": "pentagon", "check": "'pentagon'", "tol": 1e-9},
            {"q": "How many sides does a hexagon have?",
             "a": "6", "check": "6", "tol": 1e-9},
            {"q": "A circle has how many straight sides?",
             "a": "0", "check": "0", "tol": 1e-9},
            {"q": "How many faces does a cube have?",
             "a": "6", "check": "6", "tol": 1e-9},
            {"q": "What is a 3-sided polygon called?",
             "a": "triangle", "check": "'triangle'", "tol": 1e-9},
            {"q": "How many edges does a cube have?",
             "a": "12", "check": "12", "tol": 1e-9},
            {"q": "What is an 8-sided polygon called?",
             "a": "octagon", "check": "'octagon'", "tol": 1e-9},
        ],
    },
    {
        "key": "qz_div_rem",
        "name": "Division and Remainders Quiz",
        "group": "Arithmetic",
        "ladder_rank": 2, "ladder_tier": "foundations",
        "intro": ("Division asks how many full groups fit, and the "
                  "remainder tells what is left over - the question behind "
                  "every fair share. This quiz mixes clean divisions with "
                  "ones that leave a remainder; report remainders exactly "
                  "as asked."),
        "sig_intro": ("His Signature Division Method: count the full "
                      "groups, then honor the leftover. The remainder is "
                      "not a failure - it is the honest rest."),
        "how": HOW,
        "topics": ["division facts", "division by single digits",
                   "quotient and remainder form", "dividing by 10",
                   "checking division by multiplying back"],
        "requirements": ["multiplication facts", "subtraction"],
        "standards": STD,
        "citations": [CIT_CC],
        "questions": [
            {"q": "What is 48 divided by 6?", "a": "8", "check": "48/6", "tol": 1e-9},
            {"q": "What is 100 divided by 4?", "a": "25", "check": "100/4", "tol": 1e-9},
            {"q": "Divide 37 by 5. Give the quotient and remainder, like '7 remainder 2'.",
             "a": "7 remainder 2", "check": "'%d remainder %d' % (37//5, 37%5)", "tol": 1e-9},
            {"q": "What is 81 divided by 9?", "a": "9", "check": "81/9", "tol": 1e-9},
            {"q": "Divide 55 by 7. Give the quotient and remainder, like '7 remainder 6'.",
             "a": "7 remainder 6", "check": "'%d remainder %d' % (55//7, 55%7)", "tol": 1e-9},
            {"q": "What is 144 divided by 12?", "a": "12", "check": "144/12", "tol": 1e-9},
            {"q": "What is 1000 divided by 8?", "a": "125", "check": "1000/8", "tol": 1e-9},
            {"q": "Divide 23 by 4. Give the quotient and remainder, like '5 remainder 3'.",
             "a": "5 remainder 3", "check": "'%d remainder %d' % (23//4, 23%4)", "tol": 1e-9},
            {"q": "What is 96 divided by 8?", "a": "12", "check": "96/8", "tol": 1e-9},
            {"q": "What is 250 divided by 10?", "a": "25", "check": "250/10", "tol": 1e-9},
        ],
    },
    {
        "key": "qz_order_ops",
        "name": "Order of Operations Starter Quiz",
        "group": "Arithmetic",
        "ladder_rank": 2, "ladder_tier": "foundations",
        "intro": ("Parentheses first, then exponents, then multiplication "
                  "and division, then addition and subtraction - the one "
                  "agreement that keeps arithmetic honest. These ten "
                  "expressions reward whoever respects the order and "
                  "punish whoever just reads left to right."),
        "sig_intro": ("His Signature Order Method: parentheses speak "
                      "first, exponents second, and the rest wait their "
                      "turn. Order is the oath arithmetic swears to itself."),
        "how": HOW,
        "topics": ["parentheses first", "multiplication before addition",
                   "exponents in expressions", "left-to-right for same-level ops",
                   "nested operations"],
        "requirements": ["addition and subtraction", "multiplication", "exponents"],
        "standards": STD,
        "citations": [CIT_CC],
        "questions": [
            {"q": "What is 3 + 4 x 2? (Use the order of operations.)",
             "a": "11", "check": "3+4*2", "tol": 1e-9},
            {"q": "What is (3 + 4) x 2?", "a": "14", "check": "(3+4)*2", "tol": 1e-9},
            {"q": "What is 20 - 6 / 2?", "a": "17", "check": "20-6/2", "tol": 1e-9},
            {"q": "What is 2 x 3 + 4 x 5?", "a": "26", "check": "2*3+4*5", "tol": 1e-9},
            {"q": "What is 100 - (20 + 30)?", "a": "50", "check": "100-(20+30)", "tol": 1e-9},
            {"q": "What is 5 squared + 3 x 4?", "a": "37", "check": "5**2+3*4", "tol": 1e-9},
            {"q": "What is 48 / 6 + 2 x 3?", "a": "14", "check": "48/6+2*3", "tol": 1e-9},
            {"q": "What is (10 - 4) squared?", "a": "36", "check": "(10-4)**2", "tol": 1e-9},
            {"q": "What is 7 + 7 x 7 - 7?", "a": "49", "check": "7+7*7-7", "tol": 1e-9},
            {"q": "What is 2 cubed x 5 - 10?", "a": "30", "check": "2**3*5-10", "tol": 1e-9},
        ],
    },
    {
        "key": "qz_frac_line",
        "name": "Fractions on the Number Line Quiz",
        "group": "Arithmetic",
        "ladder_rank": 2, "ladder_tier": "foundations",
        "intro": ("Fractions are numbers too - they live between the "
                  "whole numbers on the number line. This quiz compares "
                  "fractions, adds and subtracts ones that share a "
                  "denominator, and spots equivalent fractions. Give "
                  "fraction answers in lowest terms."),
        "sig_intro": ("His Signature Fraction Method: every part sworn "
                      "against the whole. Between the integers the "
                      "fractions keep their own honest order."),
        "how": HOW,
        "topics": ["comparing unit fractions", "adding like fractions",
                   "subtracting like fractions", "equivalent fractions",
                   "fractions on the number line"],
        "requirements": ["division basics", "multiplication facts"],
        "standards": STD,
        "citations": [CIT_CC],
        "questions": [
            {"q": "Which is larger: 1/2 or 1/3?",
             "a": "1/2", "check": "('1/2' if 1/2>1/3 else '1/3')", "tol": 1e-9},
            {"q": "What is 1/4 + 1/4? Give the answer in lowest terms.",
             "a": "1/2", "check": "Fraction(1,4)+Fraction(1,4)", "tol": 1e-9},
            {"q": "What is 3/4 - 1/4? Give the answer in lowest terms.",
             "a": "1/2", "check": "Fraction(3,4)-Fraction(1,4)", "tol": 1e-9},
            {"q": "Which is smaller: 2/5 or 3/7?",
             "a": "2/5", "check": "('2/5' if 2/5<3/7 else '3/7')", "tol": 1e-9},
            {"q": "What is 1/2 + 1/4? Give the answer in lowest terms.",
             "a": "3/4", "check": "Fraction(1,2)+Fraction(1,4)", "tol": 1e-9},
            {"q": "What is 5/6 - 1/3? Give the answer in lowest terms.",
             "a": "1/2", "check": "Fraction(5,6)-Fraction(1,3)", "tol": 1e-9},
            {"q": "Is 2/3 greater than 3/5? Answer yes or no.",
             "a": "yes", "check": "('yes' if 2/3>3/5 else 'no')", "tol": 1e-9},
            {"q": "What is 1/3 + 1/6? Give the answer in lowest terms.",
             "a": "1/2", "check": "Fraction(1,3)+Fraction(1,6)", "tol": 1e-9},
            {"q": "Which of these equals 1/2: 2/4, 2/3, or 3/5?",
             "a": "2/4", "check": "('2/4' if Fraction(2,4)==Fraction(1,2) else 'none')", "tol": 1e-9},
            {"q": "What is 7/8 - 3/8? Give the answer in lowest terms.",
             "a": "1/2", "check": "Fraction(7,8)-Fraction(3,8)", "tol": 1e-9},
        ],
    },
    {
        "key": "qz_logic_easy",
        "name": "Easy Logic Riddles Quiz",
        "group": "Logic Puzzles",
        "ladder_rank": 2, "ladder_tier": "foundations",
        "intro": ("Logic begins with reading carefully: most riddles are "
                  "solved by noticing what the words actually say. These "
                  "ten classics each hide one trick - find the trick and "
                  "the answer is simple."),
        "sig_intro": ("His Signature Riddle Method: read the words as "
                      "sworn, not as assumed. The trick is never in the "
                      "numbers - it is in what you brought to them."),
        "how": HOW,
        "topics": ["reading exactly what is asked", "wordplay riddles",
                   "trick questions", "counting what is there",
                   "checking assumptions"],
        "requirements": ["reading comprehension", "basic arithmetic"],
        "standards": STD,
        "citations": [CIT_GARDNER],
        "questions": [
            {"q": "I am an odd number. Take away one letter and I become even. What number am I? (Spell it out.)",
             "a": "seven", "check": "'seven'", "tol": 1e-9},
            {"q": "What has keys but opens no locks?",
             "a": "piano", "check": "'piano'", "tol": 1e-9},
            {"q": "You have 3 apples and you take away 2. How many apples do YOU have now?",
             "a": "2", "check": "2", "tol": 1e-9},
            {"q": "A rooster lays an egg exactly on the peak of a roof. Which way does the egg roll?",
             "a": "It does not roll; roosters do not lay eggs",
             "check": "'It does not roll; roosters do not lay eggs'", "tol": 1e-9},
            {"q": "How many months have 28 days?",
             "a": "12", "check": "12", "tol": 1e-9},
            {"q": "What comes once in a minute, twice in a moment, but never in a thousand years?",
             "a": "the letter m", "check": "'the letter m'", "tol": 1e-9},
            {"q": "The more of me you take, the more you leave behind. What am I?",
             "a": "footsteps", "check": "'footsteps'", "tol": 1e-9},
            {"q": "What do you get when you multiply together all the digits 1 through 9 and 0?",
             "a": "0", "check": "1*2*3*4*5*6*7*8*9*0", "tol": 1e-9},
            {"q": "A doctor gives you 3 pills and tells you to take one every half hour, starting now. How long until the pills are gone?",
             "a": "1 hour", "check": "'%g hour' % ((3-1)*0.5)", "tol": 1e-9},
            {"q": "What is always in front of you but can never be seen?",
             "a": "the future", "check": "'the future'", "tol": 1e-9},
        ],
    },
    {
        "key": "qz_perimeter",
        "name": "Perimeter of Rectangles and Squares Quiz",
        "group": "Geometry",
        "ladder_rank": 2, "ladder_tier": "foundations",
        "intro": ("Perimeter is the distance around a shape - the length "
                  "of the fence, the frame, the border. For rectangles "
                  "and squares it is just adding the sides, with a "
                  "shortcut for each. Give lengths in the same units as "
                  "the question."),
        "sig_intro": ("His Signature Perimeter Method: walk the border "
                      "and count every step. The fence keeps its oath "
                      "only if you measure all four sides."),
        "how": HOW,
        "topics": ["perimeter of a square", "perimeter of a rectangle",
                   "finding a missing side from the perimeter",
                   "perimeter word problems", "decimal side lengths"],
        "requirements": ["addition", "multiplication", "reading shapes"],
        "standards": STD,
        "citations": [CIT_EUCLID, CIT_CC],
        "questions": [
            {"q": "A square has side 9 cm. What is its perimeter in cm?",
             "a": "36", "check": "4*9", "tol": 1e-9},
            {"q": "A rectangle is 12 cm long and 7 cm wide. What is its perimeter in cm?",
             "a": "38", "check": "2*(12+7)", "tol": 1e-9},
            {"q": "A square has perimeter 40 m. How long is each side in m?",
             "a": "10", "check": "40/4", "tol": 1e-9},
            {"q": "A rectangle is 15 m long and 9 m wide. What is its perimeter in m?",
             "a": "48", "check": "2*(15+9)", "tol": 1e-9},
            {"q": "A square has side 25 cm. What is its perimeter in cm?",
             "a": "100", "check": "4*25", "tol": 1e-9},
            {"q": "A rectangle has perimeter 60 cm and length 20 cm. What is its width in cm?",
             "a": "10", "check": "60/2-20", "tol": 1e-9},
            {"q": "A square has side 13 in. What is its perimeter in inches?",
             "a": "52", "check": "4*13", "tol": 1e-9},
            {"q": "A rectangle is 18 ft long and 6 ft wide. What is its perimeter in ft?",
             "a": "48", "check": "2*(18+6)", "tol": 1e-9},
            {"q": "A square has side 1.5 m. What is its perimeter in m?",
             "a": "6", "check": "4*1.5", "tol": 1e-9},
            {"q": "A rectangular garden is 30 m by 12 m. How many meters of fencing go all the way around it?",
             "a": "84", "check": "2*(30+12)", "tol": 1e-9},
        ],
    },
]
ENTRIES += [
    {
        "key": "qz_variable",
        "name": "What Is a Variable Quiz",
        "group": "Algebra",
        "ladder_rank": 2, "ladder_tier": "foundations",
        "intro": ("A variable is a letter that stands for a number you "
                  "do not know yet - a box with a name on it. This quiz "
                  "introduces the vocabulary of algebra (variable, "
                  "coefficient, constant term) and the skill of plugging "
                  "a number in and computing."),
        "sig_intro": ("His Signature Variable Method: the letter is a "
                      "sworn placeholder, holding a number's place until "
                      "the number arrives. Name the box, then fill it."),
        "how": HOW,
        "topics": ["what a variable is", "coefficients",
                   "constant terms", "substituting values",
                   "evaluating expressions"],
        "requirements": ["order of operations", "exponents"],
        "standards": STD,
        "citations": [CIT_CC, CIT_DEVLIN],
        "questions": [
            {"q": "In the expression 3x + 5, what is the variable?",
             "a": "x", "check": "'x'", "tol": 1e-9},
            {"q": "If x = 4, what is x + 7?",
             "a": "11", "check": "4+7", "tol": 1e-9},
            {"q": "If y = 10, what is 2y?",
             "a": "20", "check": "2*10", "tol": 1e-9},
            {"q": "If a = 3, what is a squared?",
             "a": "9", "check": "3**2", "tol": 1e-9},
            {"q": "If n = 5, what is 3n - 2?",
             "a": "13", "check": "3*5-2", "tol": 1e-9},
            {"q": "In the expression 7b - 2, what is the coefficient of b?",
             "a": "7", "check": "7", "tol": 1e-9},
            {"q": "If x = 2, what is x cubed + 1?",
             "a": "9", "check": "2**3+1", "tol": 1e-9},
            {"q": "If m = 6, what is m/2 + 5?",
             "a": "8", "check": "6/2+5", "tol": 1e-9},
            {"q": "In the expression 4x + 9, what is the constant term?",
             "a": "9", "check": "9", "tol": 1e-9},
            {"q": "If z = 12, what is z - 5 + 3?",
             "a": "10", "check": "12-5+3", "tol": 1e-9},
        ],
    },
    {
        "key": "qz_one_step",
        "name": "Solving One-Step Equations Quiz",
        "group": "Algebra",
        "ladder_rank": 3, "ladder_tier": "foundations",
        "intro": ("Solving an equation means undoing one operation to "
                  "free the variable - the gentlest algebra there is. "
                  "Addition undoes subtraction, multiplication undoes "
                  "division. Do the opposite operation to both sides and "
                  "the answer stands alone."),
        "sig_intro": ("His Signature Equation Method: whatever was done "
                      "to the unknown, undo it with honor. One operation, "
                      "one undoing, the variable stands free."),
        "how": HOW,
        "topics": ["undoing addition", "undoing subtraction",
                   "undoing multiplication", "undoing division",
                   "equations with the variable on the right"],
        "requirements": ["what a variable is", "inverse operations"],
        "standards": STD,
        "citations": [CIT_CC, CIT_DEVLIN],
        "questions": [
            {"q": "Solve: x + 9 = 21. What is x?",
             "a": "12", "check": "21-9", "tol": 1e-9},
            {"q": "Solve: x - 7 = 15. What is x?",
             "a": "22", "check": "15+7", "tol": 1e-9},
            {"q": "Solve: 4x = 36. What is x?",
             "a": "9", "check": "36/4", "tol": 1e-9},
            {"q": "Solve: x/5 = 8. What is x?",
             "a": "40", "check": "5*8", "tol": 1e-9},
            {"q": "Solve: x + 13 = 30. What is x?",
             "a": "17", "check": "30-13", "tol": 1e-9},
            {"q": "Solve: 7x = 84. What is x?",
             "a": "12", "check": "84/7", "tol": 1e-9},
            {"q": "Solve: x - 19 = 6. What is x?",
             "a": "25", "check": "6+19", "tol": 1e-9},
            {"q": "Solve: x/4 = 11. What is x?",
             "a": "44", "check": "4*11", "tol": 1e-9},
            {"q": "Solve: 9 + x = 52. What is x?",
             "a": "43", "check": "52-9", "tol": 1e-9},
            {"q": "Solve: 5x = 125. What is x?",
             "a": "25", "check": "125/5", "tol": 1e-9},
        ],
    },
    {
        "key": "qz_dec_frac",
        "name": "Decimals and Fractions Quiz",
        "group": "Arithmetic",
        "ladder_rank": 3, "ladder_tier": "foundations",
        "intro": ("Decimals and fractions are two costumes for the same "
                  "numbers: 1/2 and 0.5 are the same citizen. This quiz "
                  "converts between the two forms and computes with "
                  "decimals. Give fraction answers in lowest terms."),
        "sig_intro": ("His Signature Conversion Method: the fraction and "
                      "the decimal are one mark in two clothes. Change the "
                      "clothes, keep the value sworn."),
        "how": HOW,
        "topics": ["decimals to fractions", "fractions to decimals",
                   "adding decimals", "multiplying decimals",
                   "dividing decimals"],
        "requirements": ["fractions on the number line", "division"],
        "standards": STD,
        "citations": [CIT_CC],
        "questions": [
            {"q": "Write 0.5 as a fraction in lowest terms.",
             "a": "1/2", "check": "Fraction(1,2)", "tol": 1e-9},
            {"q": "Write 3/4 as a decimal.",
             "a": "0.75", "check": "3/4", "tol": 1e-9},
            {"q": "What is 0.25 + 0.75?",
             "a": "1", "check": "0.25+0.75", "tol": 1e-9},
            {"q": "Write 1/5 as a decimal.",
             "a": "0.2", "check": "1/5", "tol": 1e-9},
            {"q": "Write 0.6 as a fraction in lowest terms.",
             "a": "3/5", "check": "Fraction(3,5)", "tol": 1e-9},
            {"q": "What is 2.5 x 4?",
             "a": "10", "check": "2.5*4", "tol": 1e-9},
            {"q": "What is 7/10 + 2/10? Give the answer in lowest terms.",
             "a": "9/10", "check": "Fraction(7,10)+Fraction(2,10)", "tol": 1e-9},
            {"q": "Write 0.125 as a fraction in lowest terms.",
             "a": "1/8", "check": "Fraction(1,8)", "tol": 1e-9},
            {"q": "What is 3.6 / 3?",
             "a": "1.2", "check": "3.6/3", "tol": 1e-9},
            {"q": "Write 9/20 as a decimal.",
             "a": "0.45", "check": "9/20", "tol": 1e-9},
        ],
    },
    {
        "key": "qz_area",
        "name": "Area of Rectangles and Triangles Quiz",
        "group": "Geometry",
        "ladder_rank": 3, "ladder_tier": "foundations",
        "intro": ("Area is how much surface a shape covers - the paint, "
                  "the carpet, the field. Rectangles multiply length by "
                  "width; triangles take half of that. Give areas in "
                  "square units matching the question."),
        "sig_intro": ("His Signature Area Method: the rectangle is the "
                      "whole field, the triangle its sworn half. Measure "
                      "the ground before you claim it."),
        "how": HOW,
        "topics": ["area of a rectangle", "area of a square",
                   "area of a triangle", "finding a missing side from area",
                   "decimal side lengths"],
        "requirements": ["multiplication", "division", "perimeter"],
        "standards": STD,
        "citations": [CIT_EUCLID, CIT_CC],
        "questions": [
            {"q": "A rectangle is 9 cm long and 6 cm wide. What is its area in square cm?",
             "a": "54", "check": "9*6", "tol": 1e-9},
            {"q": "A triangle has base 10 cm and height 8 cm. What is its area in square cm?",
             "a": "40", "check": "10*8/2", "tol": 1e-9},
            {"q": "A square has side 11 m. What is its area in square m?",
             "a": "121", "check": "11**2", "tol": 1e-9},
            {"q": "A rectangle is 15 m long and 4 m wide. What is its area in square m?",
             "a": "60", "check": "15*4", "tol": 1e-9},
            {"q": "A triangle has base 12 in and height 5 in. What is its area in square inches?",
             "a": "30", "check": "12*5/2", "tol": 1e-9},
            {"q": "A square has area 81 square cm. How long is each side in cm?",
             "a": "9", "check": "math.sqrt(81)", "tol": 1e-9},
            {"q": "A rectangle has area 96 square m and length 12 m. What is its width in m?",
             "a": "8", "check": "96/12", "tol": 1e-9},
            {"q": "A triangle has base 7 cm and height 9 cm. What is its area in square cm?",
             "a": "31.5", "check": "7*9/2", "tol": 1e-9},
            {"q": "A rectangle is 2.5 m long and 4 m wide. What is its area in square m?",
             "a": "10", "check": "2.5*4", "tol": 1e-9},
            {"q": "A triangle has base 14 ft and height 6 ft. What is its area in square ft?",
             "a": "42", "check": "14*6/2", "tol": 1e-9},
        ],
    },
    {
        "key": "qz_even_prime",
        "name": "Even, Odd, and Prime Spotting Quiz",
        "group": "Number Patterns",
        "ladder_rank": 3, "ladder_tier": "foundations",
        "intro": ("Numbers have personalities: even or odd, prime or "
                  "composite. A prime has exactly two divisors - 1 and "
                  "itself - and spotting them is the doorway to all of "
                  "number theory. Answer yes/no questions with exactly "
                  "'yes' or 'no'."),
        "sig_intro": ("His Signature Number Method: every integer declares "
                      "itself - even or odd, prime or built. The primes "
                      "are the sworn atoms; learn to spot them."),
        "how": HOW,
        "topics": ["even vs odd", "what makes a number prime",
                   "the number 1 is special", "the number 2 is special",
                   "testing small primes for divisibility"],
        "requirements": ["division", "multiplication facts"],
        "standards": STD,
        "citations": [CIT_EUCLID, CIT_CC],
        "questions": [
            {"q": "Is 47 prime? Answer yes or no.",
             "a": "yes", "check": "('yes' if all(47%p for p in range(2,7)) else 'no')", "tol": 1e-9},
            {"q": "Is 91 prime? Answer yes or no.",
             "a": "no", "check": "('yes' if all(91%p for p in range(2,10)) else 'no')", "tol": 1e-9},
            {"q": "Is 28 even or odd? Answer even or odd.",
             "a": "even", "check": "('even' if 28%2==0 else 'odd')", "tol": 1e-9},
            {"q": "Is 2 prime? Answer yes or no.",
             "a": "yes", "check": "('yes' if all(2%p for p in range(2,2)) else 'no')", "tol": 1e-9},
            {"q": "Is 1 prime? Answer yes or no.",
             "a": "no", "check": "'no'", "tol": 1e-9},
            {"q": "Is 100 even or odd? Answer even or odd.",
             "a": "even", "check": "('even' if 100%2==0 else 'odd')", "tol": 1e-9},
            {"q": "Is 57 prime? Answer yes or no.",
             "a": "no", "check": "('yes' if all(57%p for p in range(2,8)) else 'no')", "tol": 1e-9},
            {"q": "What is the smallest prime number?",
             "a": "2", "check": "2", "tol": 1e-9},
            {"q": "Is 49 prime? Answer yes or no.",
             "a": "no", "check": "('yes' if all(49%p for p in range(2,8)) else 'no')", "tol": 1e-9},
            {"q": "Is 2 the only even prime number? Answer yes or no.",
             "a": "yes", "check": "'yes'", "tol": 1e-9},
        ],
    },
    {
        "key": "qz_word_problems",
        "name": "Multi-Step Word Problems Quiz",
        "group": "Arithmetic",
        "ladder_rank": 4, "ladder_tier": "compounded",
        "intro": ("Word problems are arithmetic wearing a disguise: the "
                  "work is translating the story into numbers, then "
                  "computing in the right order. Each of these ten takes "
                  "two or three steps - write down each step before "
                  "moving on."),
        "sig_intro": ("His Signature Story Method: strip the story to "
                      "its sworn numbers, then compute step by step. The "
                      "tale is the wrapping; the arithmetic is the gift."),
        "how": HOW,
        "topics": ["translating stories to arithmetic", "two-step problems",
                   "money word problems", "rate and distance stories",
                   "checking answers against the story"],
        "requirements": ["addition and subtraction", "multiplication", "division"],
        "standards": STD,
        "citations": [CIT_POLYA, CIT_CC],
        "questions": [
            {"q": "A bakery sells 24 loaves in the morning and 35 in the afternoon. Each loaf costs $2. What is the total revenue in dollars?",
             "a": "118", "check": "(24+35)*2", "tol": 1e-9},
            {"q": "A school bus holds 48 students. Five buses are full and one bus has 17 students. How many students is that in all?",
             "a": "257", "check": "5*48+17", "tol": 1e-9},
            {"q": "Maya has $120. She buys 3 books at $18 each and a pen for $7. How many dollars does she have left?",
             "a": "59", "check": "120-3*18-7", "tol": 1e-9},
            {"q": "A factory makes 150 parts per hour. How many parts does it make in an 8-hour shift?",
             "a": "1200", "check": "150*8", "tol": 1e-9},
            {"q": "Tom ran 5 km on Monday, 7 km on Wednesday, and 12 km on Saturday. How many km did he run in all?",
             "a": "24", "check": "5+7+12", "tol": 1e-9},
            {"q": "A pizza has 8 slices. Three pizzas are ordered and 5 slices are eaten. How many slices are left?",
             "a": "19", "check": "3*8-5", "tol": 1e-9},
            {"q": "A train travels 60 km/h for 3 hours, then 80 km/h for 2 hours. What is the total distance in km?",
             "a": "340", "check": "60*3+80*2", "tol": 1e-9},
            {"q": "There are 120 cookies, packed 12 to a box. How many boxes is that?",
             "a": "10", "check": "120/12", "tol": 1e-9},
            {"q": "Sara saves $15 per week for 9 weeks, then spends $64. How many dollars does she have left?",
             "a": "71", "check": "15*9-64", "tol": 1e-9},
            {"q": "A water tank holds 500 liters. 180 liters are used, then 95 liters are added. How many liters are in the tank now?",
             "a": "415", "check": "500-180+95", "tol": 1e-9},
        ],
    },
    {
        "key": "qz_integers",
        "name": "Integer Operations Quiz",
        "group": "Arithmetic",
        "ladder_rank": 4, "ladder_tier": "compounded",
        "intro": ("Negative numbers measure what is missing or owed - "
                  "debts, depths, cold. The rules are small and strict: "
                  "adding a negative goes down, subtracting a negative "
                  "goes up, and two negatives multiplied make a positive. "
                  "Ten computations below zero and above."),
        "sig_intro": ("His Signature Integer Method: below zero the "
                      "numbers still keep their oath. Debt and depth obey "
                      "the same sworn rules as wealth and height."),
        "how": HOW,
        "topics": ["adding negatives", "subtracting negatives",
                   "multiplying signed numbers", "dividing signed numbers",
                   "absolute value"],
        "requirements": ["addition and subtraction", "multiplication", "division"],
        "standards": STD,
        "citations": [CIT_CC],
        "questions": [
            {"q": "What is -7 + 12?", "a": "5", "check": "-7+12", "tol": 1e-9},
            {"q": "What is 8 - 15?", "a": "-7", "check": "8-15", "tol": 1e-9},
            {"q": "What is -4 times 6?", "a": "-24", "check": "-4*6", "tol": 1e-9},
            {"q": "What is -36 divided by 9?", "a": "-4", "check": "-36/9", "tol": 1e-9},
            {"q": "What is -5 - 9?", "a": "-14", "check": "-5-9", "tol": 1e-9},
            {"q": "What is (-3) times (-7)?", "a": "21", "check": "(-3)*(-7)", "tol": 1e-9},
            {"q": "What is 20 + (-33)?", "a": "-13", "check": "20+(-33)", "tol": 1e-9},
            {"q": "What is -100 divided by -4?", "a": "25", "check": "-100/-4", "tol": 1e-9},
            {"q": "What is the opposite of 2 cubed?", "a": "-8", "check": "-(2**3)", "tol": 1e-9},
            {"q": "What is the absolute value of -15 plus the absolute value of -4?",
             "a": "19", "check": "abs(-15)+abs(-4)", "tol": 1e-9},
        ],
    },
    {
        "key": "qz_two_step",
        "name": "Two-Step Equations Quiz",
        "group": "Algebra",
        "ladder_rank": 4, "ladder_tier": "compounded",
        "intro": ("Two-step equations need two undoings: first free the "
                  "term with the variable, then free the variable "
                  "itself. Undo addition or subtraction first, then undo "
                  "multiplication or division - the reverse of the order "
                  "of operations."),
        "sig_intro": ("His Signature Two-Step Method: two locks, two "
                      "keys, in the sworn order. Free the term, then free "
                      "the letter - never the reverse."),
        "how": HOW,
        "topics": ["undoing in reverse order", "equations with division",
                   "equations with parentheses", "zero as a solution",
                   "checking by substitution"],
        "requirements": ["one-step equations", "order of operations"],
        "standards": STD,
        "citations": [CIT_CC, CIT_DEVLIN],
        "questions": [
            {"q": "Solve: 2x + 5 = 17. What is x?",
             "a": "6", "check": "(17-5)/2", "tol": 1e-9},
            {"q": "Solve: 3x - 8 = 19. What is x?",
             "a": "9", "check": "(19+8)/3", "tol": 1e-9},
            {"q": "Solve: x/4 + 3 = 10. What is x?",
             "a": "28", "check": "(10-3)*4", "tol": 1e-9},
            {"q": "Solve: 5x + 2 = 42. What is x?",
             "a": "8", "check": "(42-2)/5", "tol": 1e-9},
            {"q": "Solve: 7x - 11 = 24. What is x?",
             "a": "5", "check": "(24+11)/7", "tol": 1e-9},
            {"q": "Solve: x/3 - 4 = 6. What is x?",
             "a": "30", "check": "(6+4)*3", "tol": 1e-9},
            {"q": "Solve: 4x + 9 = 9. What is x?",
             "a": "0", "check": "(9-9)/4", "tol": 1e-9},
            {"q": "Solve: 6x - 5 = 37. What is x?",
             "a": "7", "check": "(37+5)/6", "tol": 1e-9},
            {"q": "Solve: 2(x + 3) = 20. What is x?",
             "a": "7", "check": "20/2-3", "tol": 1e-9},
            {"q": "Solve: x/2 + 9 = 21. What is x?",
             "a": "24", "check": "(21-9)*2", "tol": 1e-9},
        ],
    },
    {
        "key": "qz_angles",
        "name": "Angles and Triangles Quiz",
        "group": "Geometry",
        "ladder_rank": 4, "ladder_tier": "compounded",
        "intro": ("Angles are measured in degrees, and triangles always "
                  "carry exactly 180 of them - the most useful fact in "
                  "all of geometry. This quiz names the angle types and "
                  "finds missing angles two ways: in triangles and in "
                  "straight lines."),
        "sig_intro": ("His Signature Angle Method: 180 degrees sworn to "
                      "every triangle, 360 to every circle. Count the "
                      "turn and the shape confesses."),
        "how": HOW,
        "topics": ["right, acute, and obtuse angles", "degrees in a triangle",
                   "degrees in a straight angle", "equilateral triangles",
                   "complementary angles"],
        "requirements": ["reading shapes", "addition and subtraction"],
        "standards": STD,
        "citations": [CIT_EUCLID, CIT_CC],
        "questions": [
            {"q": "A right angle measures how many degrees?",
             "a": "90", "check": "90", "tol": 1e-9},
            {"q": "A triangle has angles of 60 degrees and 70 degrees. How many degrees is the third angle?",
             "a": "50", "check": "180-60-70", "tol": 1e-9},
            {"q": "A straight angle measures how many degrees?",
             "a": "180", "check": "180", "tol": 1e-9},
            {"q": "An acute angle measures less than how many degrees?",
             "a": "90", "check": "90", "tol": 1e-9},
            {"q": "A triangle has angles 90, 45, and 45 degrees. What kind of triangle is it by its angles? Answer with two words, like 'right triangle'.",
             "a": "right triangle", "check": "'right triangle'", "tol": 1e-9},
            {"q": "Each angle of an equilateral triangle measures how many degrees?",
             "a": "60", "check": "180/3", "tol": 1e-9},
            {"q": "Two angles add to 90 degrees. One is 35 degrees. How many degrees is the other?",
             "a": "55", "check": "90-35", "tol": 1e-9},
            {"q": "How many degrees are in a full circle?",
             "a": "360", "check": "360", "tol": 1e-9},
            {"q": "A triangle has angles 50, 60, and 70 degrees. Is it acute, right, or obtuse?",
             "a": "acute", "check": "'acute'", "tol": 1e-9},
            {"q": "An obtuse angle measures more than 90 degrees and less than how many degrees?",
             "a": "180", "check": "180", "tol": 1e-9},
        ],
    },
]
ENTRIES += [
    {
        "key": "qz_fibonacci",
        "name": "The Fibonacci Trail Quiz",
        "group": "Number Patterns",
        "ladder_rank": 4, "ladder_tier": "compounded",
        "intro": ("The Fibonacci sequence starts 1, 1 - and every number "
                  "after is the sum of the two before it. It appears in "
                  "pinecones, shells, and sunflowers, but here it is pure "
                  "pattern: add the last two to find the next."),
        "sig_intro": ("His Signature Fibonacci Method: each mark sworn "
                      "from the two before it, the trail building itself. "
                      "Add backward to step forward."),
        "how": HOW,
        "topics": ["the Fibonacci rule", "extending the sequence",
                   "spotting Fibonacci numbers", "consecutive-term differences",
                   "the first ten terms"],
        "requirements": ["addition", "skip counting patterns"],
        "standards": STD,
        "citations": [CIT_CC, CIT_STEWART],
        "questions": [
            {"q": "The Fibonacci sequence starts 1, 1, 2, 3, 5, 8. What is the next number?",
             "a": "13", "check": "8+5", "tol": 1e-9},
            {"q": "In the Fibonacci sequence, 13, 21, 34 comes next as what?",
             "a": "55", "check": "34+21", "tol": 1e-9},
            {"q": "What are the first two Fibonacci numbers? Answer like '1 and 1'.",
             "a": "1 and 1", "check": "'1 and 1'", "tol": 1e-9},
            {"q": "The sequence 2, 3, 5, 8, 13 continues with what number?",
             "a": "21", "check": "13+8", "tol": 1e-9},
            {"q": "Each Fibonacci number is the sum of the previous how many numbers? Answer with a word.",
             "a": "two", "check": "'two'", "tol": 1e-9},
            {"q": "The Fibonacci numbers 55, 89 continue with what number?",
             "a": "144", "check": "89+55", "tol": 1e-9},
            {"q": "The sequence 5, 8, 13, 21, 34, 55, 89 continues with what number?",
             "a": "144", "check": "89+55", "tol": 1e-9},
            {"q": "Starting 1, 1, what is the 10th Fibonacci number? (The sequence: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...)",
             "a": "55", "check": "[1,1,2,3,5,8,13,21,34,55][9]", "tol": 1e-9},
            {"q": "Is 21 a Fibonacci number? Answer yes or no.",
             "a": "yes", "check": "('yes' if 21 in [1,1,2,3,5,8,13,21,34,55,89] else 'no')", "tol": 1e-9},
            {"q": "What is 144 - 89? (The difference of consecutive Fibonacci numbers is the earlier one.)",
             "a": "55", "check": "144-89", "tol": 1e-9},
        ],
    },
    {
        "key": "qz_percent",
        "name": "Percent Puzzles Quiz",
        "group": "Arithmetic",
        "ladder_rank": 5, "ladder_tier": "compounded",
        "intro": ("Percent means 'out of a hundred' - the language of "
                  "sales, taxes, tips, and test scores. The two moves "
                  "are: percent of a number (multiply by the decimal), "
                  "and what percent one number is of another (divide and "
                  "multiply by 100)."),
        "sig_intro": ("His Signature Percent Method: every hundred sworn "
                      "whole, every part its honest share. Out of a "
                      "hundred, nothing hides."),
        "how": HOW,
        "topics": ["percent of a number", "sale prices and discounts",
                   "what percent is this of that", "percents over 100",
                   "percent in test scores"],
        "requirements": ["multiplication", "decimals and fractions", "division"],
        "standards": STD,
        "citations": [CIT_CC],
        "questions": [
            {"q": "What is 25% of 80?", "a": "20", "check": "0.25*80", "tol": 1e-9},
            {"q": "What is 10% of 250?", "a": "25", "check": "0.10*250", "tol": 1e-9},
            {"q": "What is 50% of 96?", "a": "48", "check": "0.5*96", "tol": 1e-9},
            {"q": "A $40 shirt is 20% off. What is the sale price in dollars?",
             "a": "32", "check": "40*0.8", "tol": 1e-9},
            {"q": "What is 75% of 120?", "a": "90", "check": "0.75*120", "tol": 1e-9},
            {"q": "15 is what percent of 60? Answer with just the number.",
             "a": "25", "check": "15/60*100", "tol": 1e-9},
            {"q": "What is 5% of 300?", "a": "15", "check": "0.05*300", "tol": 1e-9},
            {"q": "A test has 40 questions and you answer 90% correctly. How many is that?",
             "a": "36", "check": "0.9*40", "tol": 1e-9},
            {"q": "What is 120% of 50?", "a": "60", "check": "1.2*50", "tol": 1e-9},
            {"q": "A price of $80 is increased by 25%. What is the new price in dollars?",
             "a": "100", "check": "80*1.25", "tol": 1e-9},
        ],
    },
    {
        "key": "qz_plotting",
        "name": "Plotting Points and Lines Quiz",
        "group": "Algebra",
        "ladder_rank": 5, "ladder_tier": "compounded",
        "intro": ("The coordinate plane gives every point an address: x "
                  "first (across), y second (up). Lines are described by "
                  "slope (steepness) and y-intercept (where they cross "
                  "the vertical axis). This quiz reads addresses and "
                  "describes lines."),
        "sig_intro": ("His Signature Coordinate Method: every point an "
                      "address sworn on two axes, every line a covenant "
                      "of steepness and crossing. Across, then up - the "
                      "oath of the ordered pair."),
        "how": HOW,
        "topics": ["reading coordinates", "quadrants",
                   "slope from two points", "y-intercept",
                   "slope-intercept form"],
        "requirements": ["what a variable is", "division", "integers"],
        "standards": STD,
        "citations": [CIT_CC, CIT_DEVLIN],
        "questions": [
            {"q": "For the point (3, 5), what is the x-coordinate?",
             "a": "3", "check": "3", "tol": 1e-9},
            {"q": "For the point (3, 5), what is the y-coordinate?",
             "a": "5", "check": "5", "tol": 1e-9},
            {"q": "Which quadrant is the point (4, 7) in? Answer like 'first quadrant'.",
             "a": "first quadrant", "check": "'first quadrant'", "tol": 1e-9},
            {"q": "Which quadrant is the point (-3, 5) in? Answer like 'second quadrant'.",
             "a": "second quadrant", "check": "'second quadrant'", "tol": 1e-9},
            {"q": "What is the slope of the line through (0, 0) and (4, 8)?",
             "a": "2", "check": "8/4", "tol": 1e-9},
            {"q": "What is the y-intercept of the line y = 3x + 2?",
             "a": "2", "check": "2", "tol": 1e-9},
            {"q": "What is the slope of the line y = -5x + 11?",
             "a": "-5", "check": "-5", "tol": 1e-9},
            {"q": "Which quadrant is the point (-2, -6) in? Answer like 'third quadrant'.",
             "a": "third quadrant", "check": "'third quadrant'", "tol": 1e-9},
            {"q": "On the line y = 2x + 1, if x = 4, what is y?",
             "a": "9", "check": "2*4+1", "tol": 1e-9},
            {"q": "The origin is the point with what coordinates? Answer like '(0, 0)'.",
             "a": "(0, 0)", "check": "'(0, 0)'", "tol": 1e-9},
        ],
    },
    {
        "key": "qz_circles",
        "name": "Circles: Radius, Diameter, and Circumference Quiz",
        "group": "Geometry",
        "ladder_rank": 5, "ladder_tier": "compounded",
        "intro": ("Every circle is ruled by pi: the diameter is twice "
                  "the radius, the circumference is pi times the "
                  "diameter, and the area is pi times radius squared. "
                  "Use the pi approximation the question gives (3.14 or "
                  "22/7)."),
        "sig_intro": ("His Signature Circle Method: one center, one "
                      "sworn distance, and pi keeping the round honest. "
                      "The radius is the oath; the circle keeps it."),
        "how": HOW,
        "topics": ["radius and diameter", "circumference formula",
                   "area of a circle", "using 3.14", "using 22/7"],
        "requirements": ["multiplication", "decimals", "exponents"],
        "standards": STD,
        "citations": [CIT_EUCLID, CIT_CC],
        "questions": [
            {"q": "A circle has radius 7 cm. What is its diameter in cm?",
             "a": "14", "check": "2*7", "tol": 1e-9},
            {"q": "A circle has diameter 20 m. What is its radius in m?",
             "a": "10", "check": "20/2", "tol": 1e-9},
            {"q": "A circle has radius 10 cm. Using pi = 3.14, what is its circumference in cm?",
             "a": "62.8", "check": "2*3.14*10", "tol": 1e-6},
            {"q": "A circle has radius 5 cm. Using pi = 3.14, what is its area in square cm?",
             "a": "78.5", "check": "3.14*5**2", "tol": 1e-6},
            {"q": "A circle has diameter 14 cm. Using pi = 22/7, what is its circumference in cm?",
             "a": "44", "check": "22/7*14", "tol": 1e-6},
            {"q": "A circle has radius 7 cm. Using pi = 22/7, what is its area in square cm?",
             "a": "154", "check": "22/7*7**2", "tol": 1e-6},
            {"q": "If a circle's radius doubles, its circumference is multiplied by what number?",
             "a": "2", "check": "2", "tol": 1e-9},
            {"q": "The diameter of a circle is how many times its radius?",
             "a": "2", "check": "2", "tol": 1e-9},
            {"q": "A circle's circumference is about how many times its diameter? Answer with a decimal.",
             "a": "3.14", "check": "round(math.pi, 2)", "tol": 1e-9},
            {"q": "A circle has radius 3 m (so diameter 6 m). Using pi = 3.14, what is its circumference in m?",
             "a": "18.84", "check": "3.14*6", "tol": 1e-6},
        ],
    },
    {
        "key": "qz_powers",
        "name": "Powers and Exponents Quiz",
        "group": "Number Patterns",
        "ladder_rank": 5, "ladder_tier": "compounded",
        "intro": ("Exponents are multiplication on fast-forward: 2 to "
                  "the 5th means five 2s multiplied. The laws are few - "
                  "same base means add the exponents when multiplying - "
                  "and anything to the zero power is 1."),
        "sig_intro": ("His Signature Power Method: the base sworn, the "
                      "exponent counting the multiplications. Stack the "
                      "2s and watch the number keep its oath."),
        "how": HOW,
        "topics": ["evaluating powers", "powers of 10",
                   "multiplying powers of the same base", "zero exponent",
                   "powers of powers"],
        "requirements": ["multiplication", "order of operations"],
        "standards": STD,
        "citations": [CIT_CC, CIT_STEWART],
        "questions": [
            {"q": "What is 2 to the 5th power?", "a": "32", "check": "2**5", "tol": 1e-9},
            {"q": "What is 3 to the 4th power?", "a": "81", "check": "3**4", "tol": 1e-9},
            {"q": "What is 10 cubed?", "a": "1000", "check": "10**3", "tol": 1e-9},
            {"q": "5 squared times 5 cubed equals 5 raised to what power? Answer with just the exponent.",
             "a": "5", "check": "2+3", "tol": 1e-9},
            {"q": "What is 7 to the power 0?", "a": "1", "check": "7**0", "tol": 1e-9},
            {"q": "What is 4 cubed?", "a": "64", "check": "4**3", "tol": 1e-9},
            {"q": "What is 2 to the 10th power?", "a": "1024", "check": "2**10", "tol": 1e-9},
            {"q": "What is 9 squared minus 8 squared?", "a": "17", "check": "9**2-8**2", "tol": 1e-9},
            {"q": "What is (2 cubed) squared?", "a": "64", "check": "(2**3)**2", "tol": 1e-9},
            {"q": "What is 1 to the 100th power?", "a": "1", "check": "1**100", "tol": 1e-9},
        ],
    },
    {
        "key": "qz_truth",
        "name": "Truth-Teller Puzzles Quiz",
        "group": "Logic Puzzles",
        "ladder_rank": 5, "ladder_tier": "compounded",
        "intro": ("On the island of knights and knaves, knights always "
                  "tell the truth and knaves always lie. Every puzzle "
                  "below is solved by asking: what if the speaker is a "
                  "knight? What if a knave? Exactly one of those "
                  "assumptions survives."),
        "sig_intro": ("His Signature Truth Method: the knight swears "
                      "true, the knave swears false, and the statement "
                      "itself keeps the ledger. Assume, test, and let "
                      "the contradiction confess."),
        "how": HOW,
        "topics": ["knights always tell truth", "knaves always lie",
                   "proof by cases", "self-referential statements",
                   "impossible statements"],
        "requirements": ["easy logic riddles", "careful reading"],
        "standards": STD,
        "citations": [CIT_SMULLYAN, CIT_GARDNER],
        "solver": "truth",
        "questions": [
            {"q": "A says: 'B and I are both knaves.' B says nothing. What is A? Answer knight or knave.",
             "a": "knave", "check": "'knave'", "tol": 1e-9},
            {"q": "A says: 'B is a knave.' B says: 'A and I are opposite types.' What is A? Answer knight or knave.",
             "a": "knave", "check": "'knave'", "tol": 1e-9},
            {"q": "A says: 'I am a knave.' What can you conclude? Answer with one word: impossible.",
             "a": "impossible", "check": "'impossible'", "tol": 1e-9},
            {"q": "A says: 'All three of us are knaves.' (A, B, C are present.) What is A? Answer knight or knave.",
             "a": "knave", "check": "'knave'", "tol": 1e-9},
            {"q": "A says: 'At least one of us is a knave.' (Just A and B.) What are A and B? Answer like 'A is a knight and B is a knave'.",
             "a": "A is a knight and B is a knave", "check": "'A is a knight and B is a knave'", "tol": 1e-9},
            {"q": "B says: 'A is a knight.' A says nothing. Is it possible that B is a knave? Answer yes or no.",
             "a": "yes", "check": "'yes'", "tol": 1e-9},
            {"q": "A says: 'If I am a knight, then B is a knave.' What is B? Answer knight or knave.",
             "a": "knave", "check": "'knave'", "tol": 1e-9},
            {"q": "A says: 'Exactly one of us is a knight.' B says: 'A is lying.' (Just A and B.) What is B? Answer knight or knave.",
             "a": "knave", "check": "'knave'", "tol": 1e-9},
            {"q": "A says: 'B is a knave.' B says: 'C is a knave.' C says: 'A and B are knaves.' How many knights are there among the three? Answer with a digit.",
             "a": "1", "check": "1", "tol": 1e-9},
            {"q": "A knight and a knave guard two doors; one door leads to safety. What single question, asked of either guard, guarantees you find the safe door? Answer: ask what the other guard would say is the safe door, then choose the other door.",
             "a": "ask what the other guard would say is the safe door, then choose the other door",
             "check": "'ask what the other guard would say is the safe door, then choose the other door'", "tol": 1e-9},
        ],
    },
    {
        "key": "qz_volume",
        "name": "Volume of Boxes and Cylinders Quiz",
        "group": "Geometry",
        "ladder_rank": 6, "ladder_tier": "compounded",
        "intro": ("Volume is how much a solid holds - the water in the "
                  "tank, the air in the box. Boxes multiply length by "
                  "width by height; cylinders multiply pi by radius "
                  "squared by height. Give volumes in cubic units."),
        "sig_intro": ("His Signature Volume Method: the box swears by "
                      "three measures, the cylinder by the round one. "
                      "Fill the solid on paper before you fill it in "
                      "the world."),
        "how": HOW,
        "topics": ["volume of a rectangular box", "volume of a cube",
                   "volume of a cylinder", "cubic units and liters",
                   "finding a missing edge from volume"],
        "requirements": ["area of rectangles", "exponents", "decimals"],
        "standards": STD,
        "citations": [CIT_EUCLID, CIT_CC],
        "questions": [
            {"q": "A box is 5 cm long, 4 cm wide, and 3 cm tall. What is its volume in cubic cm?",
             "a": "60", "check": "5*4*3", "tol": 1e-9},
            {"q": "A cube has side 6 m. What is its volume in cubic m?",
             "a": "216", "check": "6**3", "tol": 1e-9},
            {"q": "A box is 10 in long, 8 in wide, and 2 in tall. What is its volume in cubic inches?",
             "a": "160", "check": "10*8*2", "tol": 1e-9},
            {"q": "A cylinder has radius 3 cm and height 10 cm. Using pi = 3.14, what is its volume in cubic cm?",
             "a": "282.6", "check": "3.14*3**2*10", "tol": 1e-6},
            {"q": "A cube has volume 125 cubic cm. How long is each side in cm?",
             "a": "5", "check": "round(125**(1/3))", "tol": 1e-9},
            {"q": "A box is 12 ft long, 5 ft wide, and 4 ft tall. What is its volume in cubic ft?",
             "a": "240", "check": "12*5*4", "tol": 1e-9},
            {"q": "A cylinder has radius 7 cm and height 6 cm. Using pi = 22/7, what is its volume in cubic cm?",
             "a": "924", "check": "22/7*7**2*6", "tol": 1e-6},
            {"q": "A box is 20 cm by 10 cm by 5 cm. Since 1000 cubic cm = 1 liter, how many liters does it hold?",
             "a": "1", "check": "20*10*5/1000", "tol": 1e-9},
            {"q": "A cube has side 10 cm. Since 1000 cubic cm = 1 liter, how many liters does it hold?",
             "a": "1", "check": "10**3/1000", "tol": 1e-9},
            {"q": "A cylinder has diameter 10 cm (so radius 5 cm) and height 12 cm. Using pi = 3.14, what is its volume in cubic cm?",
             "a": "942", "check": "3.14*5**2*12", "tol": 1e-6},
        ],
    },
    {
        "key": "qz_river",
        "name": "Classic River-Crossing Logic Quiz",
        "group": "Logic Puzzles",
        "ladder_rank": 6, "ladder_tier": "compounded",
        "intro": ("River-crossing puzzles are logic with a boat: the "
                  "wolf cannot be left with the goat, the goat cannot be "
                  "left with the cabbage, and the boat holds only the "
                  "farmer plus one. Every question below is about the "
                  "one safe order - think it through trip by trip."),
        "sig_intro": ("His Signature Crossing Method: the boat keeps its "
                      "oath - one passenger besides the rower - and the "
                      "banks keep theirs. Trip by trip, the safe order "
                      "confesses itself."),
        "how": HOW,
        "topics": ["the wolf-goat-cabbage setup", "why the goat goes first",
                   "the minimum-crossing solution", "the bridge-and-torch puzzle",
                   "missionaries and cannibals"],
        "requirements": ["easy logic riddles", "planning ahead"],
        "standards": STD,
        "citations": [CIT_GARDNER, CIT_POLYA],
        "questions": [
            {"q": "A farmer must cross a river with a wolf, a goat, and a cabbage. The boat holds the farmer plus one item. The wolf cannot be left alone with the goat, and the goat cannot be left alone with the cabbage. Which crosses first?",
             "a": "the goat", "check": "'the goat'", "tol": 1e-9},
            {"q": "In the wolf-goat-cabbage puzzle, what is the minimum number of one-way river crossings needed to get everything across?",
             "a": "7", "check": "7", "tol": 1e-9},
            {"q": "Why must the goat cross first in the wolf-goat-cabbage puzzle? Answer in one sentence.",
             "a": "because the wolf would eat the goat and the goat would eat the cabbage",
             "check": "'because the wolf would eat the goat and the goat would eat the cabbage'", "tol": 1e-9},
            {"q": "Bridge and torch: four people take 1, 2, 7, and 10 minutes to cross; the torch must be carried and at most two cross at once. What is the minimum total time in minutes?",
             "a": "17", "check": "17", "tol": 1e-9},
            {"q": "In the bridge-and-torch puzzle above, which two cross first in the optimal solution? Answer like 'the 1-minute and 2-minute people'.",
             "a": "the 1-minute and 2-minute people", "check": "'the 1-minute and 2-minute people'", "tol": 1e-9},
            {"q": "In the missionaries-and-cannibals puzzle (cannibals must never outnumber missionaries on either bank), what is the smallest boat capacity, besides the rower, that makes it solvable? Answer with a digit.",
             "a": "2", "check": "2", "tol": 1e-9},
            {"q": "In the wolf-goat-cabbage puzzle, how many items besides the farmer can the boat carry? Answer with a digit.",
             "a": "1", "check": "1", "tol": 1e-9},
            {"q": "If the boat could hold the farmer plus two items, what is the minimum number of one-way crossings for the wolf-goat-cabbage puzzle?",
             "a": "3", "check": "3", "tol": 1e-9},
            {"q": "In the wolf-goat-cabbage puzzle, which pairs must never be left alone together on either bank? Answer in one sentence.",
             "a": "the wolf and the goat must never be left together, and the goat and the cabbage must never be left together",
             "check": "'the wolf and the goat must never be left together, and the goat and the cabbage must never be left together'", "tol": 1e-9},
            {"q": "The farmer takes the goat across, returns alone, and takes the cabbage across. What must he do next? Answer in one sentence.",
             "a": "he must take the goat back to the first bank",
             "check": "'he must take the goat back to the first bank'", "tol": 1e-9},
        ],
    },
]
ENTRIES += [
    {
        "key": "qz_systems",
        "name": "Systems of Two Equations Quiz",
        "group": "Algebra",
        "ladder_rank": 8, "ladder_tier": "advanced",
        "intro": ("Two equations, two unknowns: the system is solved "
                  "where both statements are true at once. Add or "
                  "subtract the equations to eliminate one variable, "
                  "solve for the other, then substitute back. Each "
                  "question below is one half of a solved system."),
        "sig_intro": ("His Signature System Method: two oaths, one "
                      "meeting point. Eliminate the extra, solve what "
                      "remains, and let the pair confess together."),
        "how": HOW,
        "topics": ["elimination", "substitution",
                   "solving for x", "solving for y",
                   "checking the ordered pair"],
        "requirements": ["two-step equations", "integers"],
        "standards": STD,
        "citations": [CIT_CC, CIT_DEVLIN],
        "questions": [
            {"q": "Solve the system: x + y = 10 and x - y = 4. What is x?",
             "a": "7", "check": "(10+4)/2", "tol": 1e-9},
            {"q": "For the same system (x + y = 10, x - y = 4), what is y?",
             "a": "3", "check": "(10-4)/2", "tol": 1e-9},
            {"q": "Solve the system: 2x + y = 14 and x + y = 9. What is x?",
             "a": "5", "check": "14-9", "tol": 1e-9},
            {"q": "For the same system (2x + y = 14, x + y = 9), what is y?",
             "a": "4", "check": "9-5", "tol": 1e-9},
            {"q": "Solve the system: 3x + 2y = 22 and x + y = 8. What is x?",
             "a": "6", "check": "22-2*8", "tol": 1e-9},
            {"q": "For the same system (3x + 2y = 22, x + y = 8), what is y?",
             "a": "2", "check": "8-6", "tol": 1e-9},
            {"q": "Solve the system: x + 2y = 15 and 3x - 2y = 5. What is x?",
             "a": "5", "check": "(15+5)/4", "tol": 1e-9},
            {"q": "For the same system (x + 2y = 15, 3x - 2y = 5), what is y?",
             "a": "5", "check": "(15-5)/2", "tol": 1e-9},
            {"q": "Solve the system: 5x - y = 18 and x + y = 12. What is x?",
             "a": "5", "check": "(18+12)/6", "tol": 1e-9},
            {"q": "For the same system (5x - y = 18, x + y = 12), what is y?",
             "a": "7", "check": "12-5", "tol": 1e-9},
        ],
    },
    {
        "key": "qz_modular",
        "name": "Modular Arithmetic Clocks Quiz",
        "group": "Arithmetic",
        "ladder_rank": 8, "ladder_tier": "advanced",
        "intro": ("Modular arithmetic is clock arithmetic: after 12 "
                  "comes 1 again, after Sunday comes Monday again. 'A "
                  "mod n' is the remainder when A is divided by n - and "
                  "remainders run the calendar, the schedule, and the "
                  "secret code."),
        "sig_intro": ("His Signature Clock Method: the numbers wrap and "
                      "begin again, and the remainder keeps the true "
                      "time. Around the dial, the oath renews."),
        "how": HOW,
        "topics": ["remainders as mod", "clock hours",
                   "days of the week", "powers mod n",
                   "sums mod n"],
        "requirements": ["division and remainders", "exponents"],
        "standards": STD,
        "citations": [CIT_CC, CIT_STEWART],
        "questions": [
            {"q": "What is 17 mod 5?",
             "a": "2", "check": "17%5", "tol": 1e-9},
            {"q": "What is 100 mod 7?",
             "a": "2", "check": "100%7", "tol": 1e-9},
            {"q": "It is 9 o'clock. What time is it 5 hours later on a 12-hour clock? Answer with just the hour number.",
             "a": "2", "check": "(9+5)%12", "tol": 1e-9},
            {"q": "What is 3 to the 4th power, mod 5?",
             "a": "1", "check": "3**4%5", "tol": 1e-9},
            {"q": "Day 0 is Monday. Counting 0=Monday, 1=Tuesday, and so on, what day of the week is day 10?",
             "a": "Thursday", "check": "['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'][10%7]", "tol": 1e-9},
            {"q": "What is 2 to the 10th power, mod 3?",
             "a": "1", "check": "2**10%3", "tol": 1e-9},
            {"q": "It is 11 o'clock. What time was it 4 hours ago on a 12-hour clock? Answer with just the hour number.",
             "a": "7", "check": "(11-4)%12", "tol": 1e-9},
            {"q": "What is 25 mod 6?",
             "a": "1", "check": "25%6", "tol": 1e-9},
            {"q": "Day 0 is Sunday. What day of the week is day 100?",
             "a": "Tuesday", "check": "['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'][100%7]", "tol": 1e-9},
            {"q": "What is (14 + 23) mod 9?",
             "a": "1", "check": "(14+23)%9", "tol": 1e-9},
        ],
    },
    {
        "key": "qz_pythagoras",
        "name": "Pythagorean Theorem in Action Quiz",
        "group": "Geometry",
        "ladder_rank": 8, "ladder_tier": "advanced",
        "intro": ("In a right triangle, the square on the hypotenuse "
                  "equals the sum of the squares on the two legs: "
                  "a squared + b squared = c squared. Find the missing "
                  "side - hypotenuse from two legs, or a leg from the "
                  "hypotenuse and the other leg."),
        "sig_intro": ("His Signature Right-Triangle Method: the legs "
                      "swear their squares, and the hypotenuse keeps the "
                      "sum. Square, add, root - the ancient oath holds."),
        "how": HOW,
        "topics": ["finding the hypotenuse", "finding a missing leg",
                   "Pythagorean triples", "ladders and walls",
                   "diagonals of rectangles"],
        "requirements": ["exponents", "square roots", "angles and triangles"],
        "standards": STD,
        "citations": [CIT_EUCLID, CIT_CC],
        "questions": [
            {"q": "A right triangle has legs 3 and 4. What is the hypotenuse?",
             "a": "5", "check": "math.sqrt(3**2+4**2)", "tol": 1e-9},
            {"q": "A right triangle has legs 6 and 8. What is the hypotenuse?",
             "a": "10", "check": "math.sqrt(6**2+8**2)", "tol": 1e-9},
            {"q": "A right triangle has hypotenuse 13 and one leg 5. What is the other leg?",
             "a": "12", "check": "math.sqrt(13**2-5**2)", "tol": 1e-9},
            {"q": "A right triangle has legs 5 and 12. What is the hypotenuse?",
             "a": "13", "check": "math.sqrt(5**2+12**2)", "tol": 1e-9},
            {"q": "A right triangle has hypotenuse 25 and one leg 7. What is the other leg?",
             "a": "24", "check": "math.sqrt(25**2-7**2)", "tol": 1e-9},
            {"q": "A right triangle has legs 9 and 12. What is the hypotenuse?",
             "a": "15", "check": "math.sqrt(9**2+12**2)", "tol": 1e-9},
            {"q": "A 10-ft ladder leans against a wall with its base 6 ft from the wall. How high up the wall does it reach, in ft?",
             "a": "8", "check": "math.sqrt(10**2-6**2)", "tol": 1e-9},
            {"q": "A right triangle has legs 8 and 15. What is the hypotenuse?",
             "a": "17", "check": "math.sqrt(8**2+15**2)", "tol": 1e-9},
            {"q": "A right triangle has hypotenuse 20 and one leg 12. What is the other leg?",
             "a": "16", "check": "math.sqrt(20**2-12**2)", "tol": 1e-9},
            {"q": "What is the diagonal of a 9 by 12 rectangle?",
             "a": "15", "check": "math.sqrt(9**2+12**2)", "tol": 1e-9},
        ],
    },
    {
        "key": "qz_quadratic",
        "name": "Quadratic Roots by Factoring Quiz",
        "group": "Algebra",
        "ladder_rank": 9, "ladder_tier": "advanced",
        "intro": ("A quadratic equation asks where a parabola crosses "
                  "zero. When the quadratic factors into two brackets, "
                  "each bracket gives a root: the x-values that make "
                  "each bracket zero. Find both roots of each equation "
                  "below; give them like '2 and 3'."),
        "sig_intro": ("His Signature Quadratic Method: the parabola "
                      "swears two crossings, and the factors name them. "
                      "Split the middle, pair the terms, read the roots."),
        "how": HOW,
        "topics": ["factoring quadratics", "zero-product property",
                   "roots from factors", "double roots",
                   "quadratics with a leading coefficient"],
        "requirements": ["two-step equations", "multiplication", "integers"],
        "standards": STD,
        "citations": [CIT_CC, CIT_DEVLIN],
        "questions": [
            {"q": "Solve x^2 - 5x + 6 = 0. Give both roots like '2 and 3'.",
             "a": "2 and 3", "check": "'%g and %g' % tuple(sorted(qroots(1,-5,6)))", "tol": 1e-9},
            {"q": "Solve x^2 - 7x + 12 = 0. Give both roots like '3 and 4'.",
             "a": "3 and 4", "check": "'%g and %g' % tuple(sorted(qroots(1,-7,12)))", "tol": 1e-9},
            {"q": "Solve x^2 - 9x + 20 = 0. Give both roots.",
             "a": "4 and 5", "check": "'%g and %g' % tuple(sorted(qroots(1,-9,20)))", "tol": 1e-9},
            {"q": "Solve x^2 + 5x + 6 = 0. Give both roots like '-3 and -2'.",
             "a": "-3 and -2", "check": "'%g and %g' % tuple(sorted(qroots(1,5,6)))", "tol": 1e-9},
            {"q": "Solve x^2 - 4x - 12 = 0. Give both roots.",
             "a": "-2 and 6", "check": "'%g and %g' % tuple(sorted(qroots(1,-4,-12)))", "tol": 1e-9},
            {"q": "Solve x^2 - 1 = 0. Give both roots.",
             "a": "-1 and 1", "check": "'%g and %g' % tuple(sorted(qroots(1,0,-1)))", "tol": 1e-9},
            {"q": "Solve x^2 - 10x + 25 = 0. This one has a double root; answer like '5 (double root)'.",
             "a": "5 (double root)", "check": "'%g (double root)' % qroots(1,-10,25)[0]", "tol": 1e-9},
            {"q": "Solve x^2 + 7x + 12 = 0. Give both roots.",
             "a": "-4 and -3", "check": "'%g and %g' % tuple(sorted(qroots(1,7,12)))", "tol": 1e-9},
            {"q": "Solve x^2 - 11x + 30 = 0. Give both roots.",
             "a": "5 and 6", "check": "'%g and %g' % tuple(sorted(qroots(1,-11,30)))", "tol": 1e-9},
            {"q": "Solve 2x^2 - 8x + 6 = 0. Give both roots.",
             "a": "1 and 3", "check": "'%g and %g' % tuple(sorted(qroots(2,-8,6)))", "tol": 1e-9},
        ],
    },
    {
        "key": "qz_sequences",
        "name": "Sequences and Series Sums Quiz",
        "group": "Number Patterns",
        "ladder_rank": 9, "ladder_tier": "advanced",
        "intro": ("A sequence lists numbers in order; a series adds "
                  "them up. Gauss summed 1 to 100 as a schoolboy by "
                  "pairing: n(n+1)/2. These ten ask for next terms and "
                  "for sums - spot the rule first, then compute."),
        "sig_intro": ("His Signature Series Method: pair the first with "
                      "the last and let Gauss keep the ledger. The rule "
                      "confesses; the sum follows."),
        "how": HOW,
        "topics": ["triangular numbers", "summing 1 to n",
                   "sums of evens and odds", "geometric sequences",
                   "factorial sequences"],
        "requirements": ["powers and exponents", "Fibonacci trail", "multiplication"],
        "standards": STD,
        "citations": [CIT_CC, CIT_STEWART],
        "questions": [
            {"q": "What is 1 + 2 + 3 + ... + 10?",
             "a": "55", "check": "10*11//2", "tol": 1e-9},
            {"q": "What is 1 + 2 + 3 + ... + 100?",
             "a": "5050", "check": "100*101//2", "tol": 1e-9},
            {"q": "What comes next: 2, 6, 12, 20, 30, __? (The differences grow by 2 each time.)",
             "a": "42", "check": "30+12", "tol": 1e-9},
            {"q": "What is the sum of the first 10 odd numbers (1 + 3 + 5 + ... + 19)?",
             "a": "100", "check": "10**2", "tol": 1e-9},
            {"q": "What comes next: 1, 4, 9, 16, 25, __?",
             "a": "36", "check": "6**2", "tol": 1e-9},
            {"q": "What is 2 + 4 + 6 + ... + 20?",
             "a": "110", "check": "2*55", "tol": 1e-9},
            {"q": "What comes next: 3, 9, 27, 81, __?",
             "a": "243", "check": "81*3", "tol": 1e-9},
            {"q": "What is 1 + 2 + 4 + 8 + 16?",
             "a": "31", "check": "2**5-1", "tol": 1e-9},
            {"q": "What comes next: 1, 1, 2, 6, 24, __? (Each term multiplies by the next counting number.)",
             "a": "120", "check": "24*5", "tol": 1e-9},
            {"q": "What is 5 + 10 + 15 + ... + 50?",
             "a": "275", "check": "5*55", "tol": 1e-9},
        ],
    },
    {
        "key": "qz_growth",
        "name": "Compound Growth and Interest Quiz",
        "group": "Arithmetic",
        "ladder_rank": 9, "ladder_tier": "advanced",
        "intro": ("Simple interest pays on the original amount; compound "
                  "interest pays on the growing total - interest on "
                  "interest. The same mathematics doubles populations "
                  "and bacteria. Money answers are in dollars."),
        "sig_intro": ("His Signature Growth Method: the total swears "
                      "interest on itself, and the oath compounds. What "
                      "grows upon its growth keeps the covenant doubled."),
        "how": HOW,
        "topics": ["simple interest", "compound interest",
                   "doubling and tripling", "the rule of 72",
                   "growth as repeated multiplication"],
        "requirements": ["percent puzzles", "powers and exponents", "decimals"],
        "standards": STD,
        "citations": [CIT_MAOR, CIT_CC],
        "questions": [
            {"q": "$1000 earns 5% simple interest for 1 year. What is the interest in dollars?",
             "a": "50", "check": "1000*0.05", "tol": 1e-9},
            {"q": "$1000 at 5% simple interest for 1 year grows to what total in dollars?",
             "a": "1050", "check": "1000*1.05", "tol": 1e-9},
            {"q": "$2000 at 10% compounded annually for 2 years grows to what total in dollars?",
             "a": "2420", "check": "2000*1.1**2", "tol": 1e-9},
            {"q": "A population of 500 doubles every year. What is it after 3 years?",
             "a": "4000", "check": "500*2**3", "tol": 1e-9},
            {"q": "$100 at 100% annual interest, compounded yearly, for 3 years grows to what total in dollars?",
             "a": "800", "check": "100*2**3", "tol": 1e-9},
            {"q": "100 bacteria triple every hour. How many are there after 2 hours?",
             "a": "900", "check": "100*3**2", "tol": 1e-9},
            {"q": "$5000 at 4% simple interest for 3 years earns what interest in dollars?",
             "a": "600", "check": "5000*0.04*3", "tol": 1e-9},
            {"q": "A $200 investment grows 10% per year, compounded, for 2 years. What is the gain in dollars?",
             "a": "42", "check": "200*1.1**2-200", "tol": 1e-9},
            {"q": "Money that doubles in about 10 years earns about what annual percent? (Use the rule of 72.) Answer like 'about 7.2 percent'.",
             "a": "about 7.2 percent", "check": "'about %g percent' % (72/10)", "tol": 1e-9},
            {"q": "$1500 at 6% compounded annually for 2 years grows to what total in dollars?",
             "a": "1685.4", "check": "1500*1.06**2", "tol": 1e-9},
        ],
    },
    {
        "key": "qz_grid",
        "name": "The Logic Grid Challenge Quiz",
        "group": "Logic Puzzles",
        "ladder_rank": 9, "ladder_tier": "advanced",
        "intro": ("Three houses in a row, three owners, three colors, "
                  "three pets - and five clues. The grid is solved by "
                  "elimination: write what each clue forces, cross out "
                  "what it forbids, and the one surviving arrangement is "
                  "the answer. Clues: 1. Amy lives in house 1. 2. The red "
                  "house is house 2. 3. Brad keeps dogs. 4. The green "
                  "house keeps birds. 5. Cara lives in the blue house."),
        "sig_intro": ("His Signature Grid Method: five clues sworn, one "
                      "arrangement surviving. Cross out the impossible "
                      "until only the true house stands."),
        "how": HOW,
        "topics": ["logic grids", "elimination",
                   "combining clues", "unique solutions",
                   "checking consistency"],
        "requirements": ["truth-teller puzzles", "planning ahead"],
        "standards": STD,
        "citations": [CIT_SMULLYAN, CIT_GARDNER],
        "solver": "grid",
        "questions": [
            {"q": "In the three-house puzzle described above, who lives in house 1?",
             "a": "Amy", "check": "'Amy'", "tol": 1e-9},
            {"q": "In the same puzzle, what color is house 2?",
             "a": "red", "check": "'red'", "tol": 1e-9},
            {"q": "In the same puzzle, who keeps dogs?",
             "a": "Brad", "check": "'Brad'", "tol": 1e-9},
            {"q": "In the same puzzle, what pet lives in the green house?",
             "a": "birds", "check": "'birds'", "tol": 1e-9},
            {"q": "In the same puzzle, who lives in the blue house?",
             "a": "Cara", "check": "'Cara'", "tol": 1e-9},
            {"q": "In the same puzzle, what color is Amy's house?",
             "a": "green", "check": "'green'", "tol": 1e-9},
            {"q": "In the same puzzle, who keeps cats?",
             "a": "Cara", "check": "'Cara'", "tol": 1e-9},
            {"q": "In the same puzzle, what color is Brad's house?",
             "a": "red", "check": "'red'", "tol": 1e-9},
            {"q": "In the same puzzle, which house keeps birds? Answer like 'house 1'.",
             "a": "house 1", "check": "'house 1'", "tol": 1e-9},
            {"q": "In the same puzzle, who lives in house 3?",
             "a": "Cara", "check": "'Cara'", "tol": 1e-9},
        ],
    },
    {
        "key": "qz_proof",
        "name": "Proof Puzzles: Convince Yourself Quiz",
        "group": "Logic Puzzles",
        "ladder_rank": 10, "ladder_tier": "advanced",
        "intro": ("A proof is an argument that leaves no escape: direct "
                  "proofs build forward, counterexamples knock claims "
                  "down, and Euclid's ancient argument shows there is no "
                  "largest prime. These ten are the first steps of "
                  "proving - each with one exact answer."),
        "sig_intro": ("His Signature Proof Method: no claim without a "
                      "kept oath behind it. Build forward, or knock down "
                      "with one counterexample - either way, leave no "
                      "escape."),
        "how": HOW,
        "topics": ["direct proof", "counterexamples",
                   "Euclid's infinite primes", "even and odd proofs",
                   "proof by contradiction"],
        "requirements": ["even, odd, and prime spotting", "truth-teller puzzles"],
        "standards": STD,
        "citations": [CIT_EUCLID, CIT_POLYA],
        "questions": [
            {"q": "Two even numbers can be written 2m and 2n. Their sum is 2(m+n), which is even because it has a factor of what? Answer with a digit.",
             "a": "2", "check": "2", "tol": 1e-9},
            {"q": "To prove 6 is composite, write 6 as 2 times what? Answer with a digit.",
             "a": "3", "check": "6//2", "tol": 1e-9},
            {"q": "The sum of the first n odd numbers is n squared. What is 1 + 3 + 5 + 7?",
             "a": "16", "check": "1+3+5+7", "tol": 1e-9},
            {"q": "If a number is divisible by 6, it is divisible by both 2 and 3. Is 42 divisible by 6? Answer yes or no.",
             "a": "yes", "check": "('yes' if 42%6==0 else 'no')", "tol": 1e-9},
            {"q": "Euclid's proof: if the primes were only 2, 3, 5, 7, then 2x3x5x7+1 would be a new prime. What is 2x3x5x7+1?",
             "a": "211", "check": "2*3*5*7+1", "tol": 1e-9},
            {"q": "211 leaves remainder 1 when divided by 2, 3, 5, 7, 11, and 13, so 211 is prime. True or false?",
             "a": "true", "check": "('true' if all(211%p for p in [2,3,5,7,11,13]) else 'false')", "tol": 1e-9},
            {"q": "The product of two odd numbers is odd. What is 9 times 15?",
             "a": "135", "check": "9*15", "tol": 1e-9},
            {"q": "A direct proof that the sum of two rationals is rational: 1/2 + 1/3 = (1x3+1x2)/(2x3). Give the single fraction in lowest terms.",
             "a": "5/6", "check": "Fraction(1,2)+Fraction(1,3)", "tol": 1e-9},
            {"q": "One counterexample disproves 'all prime numbers are odd'. What is the counterexample?",
             "a": "2", "check": "2", "tol": 1e-9},
            {"q": "To prove 'if n squared is even then n is even', use the contrapositive: if n is odd then n squared is what? Answer odd or even.",
             "a": "odd", "check": "'odd'", "tol": 1e-9},
        ],
    },
]
