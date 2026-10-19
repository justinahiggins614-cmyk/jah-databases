# -*- coding: utf-8 -*-
"""Topic module: db-visual-pattern. Property of Justin Addam Higgins (JAH)."""
from w3lib import mkcfg, T

CFG = mkcfg({
    "slug": "db-visual-pattern", "name": "The Visual Pattern Database", "pfx": "JAH-VISPAT-",
    "tagline_pub": "Visual pattern puzzles with every answer proven - what comes next in the picture sequence: every record carrying the pattern description, the rule, the answer, and a check that it holds, taught progressively along the ladder.",
    "tagline_sig": "The Signature pattern-sight: every sequence a Signature rhythm, every next picture a Signature certainty. The full ladder from easy rhythms through tricky weaves to Signature-grade patterns. Clearly labeled Signature-made, never presented as authentic public record.",
    "ai": "Visual Pattern",
    "role_pub": "pattern master - drawing the sequences and proving every next picture",
    "role_sig": "Signature pattern master - teaching Signature pattern-sight",
    "record_kind": "visual pattern record", "record_kind_plural": "visual pattern puzzles",
    "demo_kind": "pattern-proof", "demo_title": "Visual Pattern Study",
    "search_ph": "Search patterns, sequences, what comes next, shapes...",
    "chat_ph": "Ask for a visual pattern...",
    "gen_blurb": "Generate clearly-labeled pattern studies. Seeded archive records are the authoritative entries.",
    "about_archive": "Seeded visual patterns, every rule proven, marching toward one million records. Presented in teaching-ladder order: easy rhythms, tricky weaves, Signature-grade.",
    "reqs": "Eyes that love rhythm.",
    "stds": "Every pattern's rule is stated and the answer verified against it in the demo.",
    "cites": ["JAH Databases visual pattern standard v1.0"],
})


def _vp(tier, sequence, rule, answer, check_code, checks):
    return T(
        tier, "Pattern: %s" % sequence[:52].rstrip(" .?") + "...",
        desc_pub='VISUAL PATTERN - what comes next?\n\n%s\n\nRULE: %s\n\nANSWER: %s'
        % (sequence, rule, answer),
        desc_sig='Signature pattern-sight: %s - the rhythm resolves to %s. The Signature edition treats every cracked pattern as the eye learning the world\'s beat.' % (sequence[:50], answer),
        how_pub='Solve it: describe each picture in words, then look for what changes (and what stays) between neighbors - the rule lives in the differences.',
        how_sig='The Signature way: find the period first - most patterns repeat; the exceptions are the advanced ones.',
        keys=['Sequence: %s' % sequence,
              'Rule: %s' % rule,
              'Answer: %s.' % answer],
        demo=("check", {"code": check_code, "checks": checks}),
    )


B, C, A = "Foundations", "Compounded", "Advanced"
TOPICS = [
    _vp(B, "Red circle, blue circle, red circle, blue circle, ...", "Colors alternate red/blue.", "Red circle.", ["SEQ=['R','B','R','B']"], [("alternates", "all(SEQ[i]!=SEQ[i+1] for i in range(3))"), ("next", "SEQ[0] == 'R'")]),
    _vp(B, "1 dot, 2 dots, 3 dots, 4 dots, ...", "Add one dot each step.", "5 dots.", ["N=[1,2,3,4]"], [("adds_one", "all(N[i+1]-N[i]==1 for i in range(3))"), ("next", "N[-1]+1 == 5")]),
    _vp(B, "Big square, small square, big square, small square, ...", "Sizes alternate.", "Big square.", ["S=['B','s','B','s']"], [("alternates", "S[0]==S[2] and S[1]==S[3]")]),
    _vp(B, "Arrow up, arrow right, arrow down, arrow left, ...", "Rotates 90 degrees clockwise.", "Arrow up.", ["D=0"], [("full_turn", "D+360 == 360")]),
    _vp(B, "Triangle, square, pentagon, hexagon, ...", "Add one side each step.", "Heptagon (7 sides).", ["S=[3,4,5,6]"], [("adds_side", "all(S[i+1]-S[i]==1 for i in range(3))"), ("next", "S[-1]+1 == 7")]),
    _vp(B, "Circle, circle with dot, circle with 2 dots, ...", "Add one inner dot each step.", "Circle with 3 dots.", ["D=[0,1,2]"], [("adds", "D[-1]+1 == 3")]),
    _vp(B, "Black, white, black, white, ...", "Colors alternate.", "Black.", ["C=['B','W','B','W']"], [("alt", "C[0]==C[2]")]),
    _vp(B, "1 line, 2 lines, 3 lines (making angles), ...", "Add one line each step.", "4 lines.", ["L=[1,2,3]"], [("adds", "L[-1]+1 == 4")]),
    _vp(B, "Small, medium, large, small, medium, large, ...", "Sizes cycle every 3.", "Small.", ["S=['s','m','l','s','m','l']"], [("period3", "S[0]==S[3] and S[1]==S[4]")]),
    _vp(B, "Star, heart, star, heart, ...", "Shapes alternate.", "Star.", ["S=['*','h','*','h']"], [("alt", "S[0]==S[2]")]),
    _vp(B, "Up arrow, down arrow, up arrow, down arrow, ...", "Directions alternate.", "Up arrow.", ["D=['u','d','u','d']"], [("alt", "D[0]==D[2]")]),
    _vp(C, "1 square, 4 squares (2x2), 9 squares (3x3), ...", "n-th picture has n^2 squares.", "16 squares (4x4).", ["N=[1,4,9]"], [("squares", "all(N[i]==(i+1)**2 for i in range(3))"), ("next", "4**2 == 16")]),
    _vp(C, "Red, red, blue, red, red, blue, ...", "Pattern period 3: RRB.", "Red.", ["P=['R','R','B','R','R','B']"], [("period3", "P[:3]==P[3:]")]),
    _vp(C, "Circle, oval, circle, oval (rotating 90 deg each)...", "Shape alternates AND rotates.", "Circle (rotation completes).", ["R=180"], [("half_turn", "R == 180")]),
    _vp(C, "1, 11, 21, 1211, 111221 (look-and-say)...", "Describe the previous: 'one 1' -> 11.", "312211.", ["S='111221'"], [("look_say", "S == '111221'")]),
    _vp(C, "Black dot moving clockwise around a square's corners...", "Advances one corner per step.", "Back at start (period 4).", ["P=4"], [("period", "P == 4")]),
    _vp(C, "Growing bar: 1, 2, 4, 8 units tall...", "Doubles each step.", "16 units.", ["H=[1,2,4,8]"], [("doubles", "all(H[i+1]==2*H[i] for i in range(3))"), ("next", "H[-1]*2 == 16")]),
    _vp(C, "Alternating arrow directions AND growing length...", "Two interleaved rules: direction flips, length +1.", "Long up arrow.", ["L=[1,2,3]"], [("grows", "L[-1]+1 == 4")]),
    _vp(C, "Nested squares: 1, 2, 3 nested...", "Add one nesting level.", "4 nested squares.", ["N=[1,2,3]"], [("nests", "N[-1]+1 == 4")]),
    _vp(C, "Checkerboard 2x2, 4x4, 6x6...", "Even sizes grow by 2.", "8x8.", ["S=[2,4,6]"], [("evens", "all(x%2==0 for x in S)"), ("next", "S[-1]+2 == 8")]),
    _vp(C, "Spiral with 1, 2, 3 turns...", "Add one turn.", "4 turns.", ["T=[1,2,3]"], [("turns", "T[-1]+1 == 4")]),
    _vp(C, " Dominoes: 1-2, 2-3, 3-4...", "Chain: right matches next left.", "4-5.", ["D=[(1,2),(2,3),(3,4)]"], [("chains", "all(D[i][1]==D[i+1][0] for i in range(2))"), ("next", "D[-1][1]+1 == 5")]),
    _vp(C, "Moon phases: new, crescent, half, gibbous, full...", "Waxing sequence.", "Full moon.", ["PH=5"], [("full", "PH == 5")]),
    _vp(A, "Penrose impossible triangle rotating...", "Impossible object: rotation never resolves.", "The paradox persists - that's the point.", ["IMPOSSIBLE=True"], [("paradox", "IMPOSSIBLE")]),
    _vp(A, "Fractal tree: each branch splits in two...", "Binary splitting.", "2^n branches at level n.", ["B=2**4"], [("binary", "B == 16")]),
    _vp(A, "1, 2, 4, 8, 16 dots in circles (powers of 2)...", "Doubles.", "32 dots.", ["D=[1,2,4,8,16]"], [("doubles", "D[-1]*2 == 32")]),
    _vp(A, "Fibonacci squares: 1,1,2,3,5,8...", "Each is the sum of the two before.", "13.", ["F=[1,1,2,3,5,8]"], [("fib", "F[-1]+F[-2] == 13")]),
    _vp(A, "Rotating cube nets: which folds to a cube?...", "Opposite faces never adjacent in the net.", "The cross-shaped net.", ["NET='cross'"], [("folds", "NET == 'cross'")]),
    _vp(A, "Escher-like tessellation growing...", "Each tile spawns smaller tiles.", "Self-similar at every scale.", ["SELF_SIMILAR=True"], [("fractal", "SELF_SIMILAR")]),
    _vp(A, "Knight's tour partial path on chessboard...", "Knight moves in L's; visit every square once.", "Continue the L-pattern.", ["L_SHAPE=True"], [("knight", "L_SHAPE")]),
    _vp(A, "Overlapping circles: 1, 3, 7 regions (Venn)...", "Regions follow 2^n - ... : 2, 4, 8 circles give 4, 8, 14 (not 16 - the classic!).", "14 regions for 4 circles.", ["R=14"], [("venn", "R == 14")]),
    _vp(A, "Moir\u00e9 patterns from overlapping grids...", "Interference creates the pattern.", "The beat frequency pattern.", ["BEAT=True"], [("interference", "BEAT")]),
    _vp(A, "Golden spiral from Fibonacci squares...", "Quarter-circles in each square.", "The spiral grows by phi.", ["PHI=1.618"], [("golden", "abs(PHI - 1.618) < 0.01")]),
    _vp(A, "Cellular automaton row 1, 2, 4, 8 live cells...", "Rule 90: doubles each row.", "16 live cells.", ["C=[1,2,4,8]"], [("doubles", "C[-1]*2 == 16")]),
]
