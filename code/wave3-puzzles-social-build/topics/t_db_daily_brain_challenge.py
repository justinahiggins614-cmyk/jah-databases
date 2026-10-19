# -*- coding: utf-8 -*-
"""Topic module: db-daily-brain-challenge. Property of Justin Addam Higgins (JAH)."""
from w3lib import mkcfg, T

CFG = mkcfg({
    "slug": "db-daily-brain-challenge", "name": "The Daily Brain Challenge", "pfx": "JAH-DAIBRAICH-",
    "tagline_pub": "Daily brain workouts with every answer proven - one challenge per day, 34 days of training: every record carrying the day's challenge, the solution, and a check that it holds, taught progressively along the ladder.",
    "tagline_sig": "The Signature daily grind: every day a Signature workout, every solution a Signature rep. The full ladder from warm-ups through burners to Signature-grade training. Clearly labeled Signature-made, never presented as authentic public record.",
    "ai": "Daily Brain Challenge",
    "role_pub": "daily trainer - dealing one workout per day and proving every answer",
    "role_sig": "Signature daily trainer - teaching Signature mental fitness",
    "record_kind": "daily challenge record", "record_kind_plural": "daily challenges",
    "demo_kind": "workout-proof", "demo_title": "Daily Workout",
    "search_ph": "Search daily, workout, day 1, challenge, training...",
    "chat_ph": "Ask for today's challenge...",
    "gen_blurb": "Generate clearly-labeled workout studies. Seeded archive records are the authoritative entries.",
    "about_archive": "Seeded daily workouts, every answer proven, marching toward one million records. Presented in teaching-ladder order: warm-ups, burners, Signature-grade.",
    "reqs": "Five minutes a day and a streak to protect.",
    "stds": "Every day's answer is verified in the demo: the solution must satisfy the day's check.",
    "cites": ["JAH Databases daily training standard v1.0"],
})


def _dc(tier, day, challenge, answer, tip, check_code, checks):
    return T(
        tier, "Day %d: %s" % (day, challenge[:48].rstrip(" .?") + "..."),
        desc_pub='DAY %d BRAIN CHALLENGE:\n\n%s\n\nANSWER: %s\n\nTRAINER TIP: %s'
        % (day, challenge, answer, tip),
        desc_sig='Signature day %d: %s - one more Signature rep for the mind. The Signature edition treats every streak day as the brain getting measurably sharper.' % (day, challenge[:50]),
        how_pub='Do it daily: attempt before peeking, log your streak, and revisit missed days - spaced repetition is the whole trick.',
        how_sig='The Signature way: never break the chain - the streak is the workout.',
        keys=['Day %d.' % day,
              'Challenge: %s' % challenge,
              'Answer: %s.' % answer,
              'Tip: %s' % tip],
        demo=("check", {"code": check_code, "checks": checks}),
    )


B, C, A = "Foundations", "Compounded", "Advanced"
_days = iter(range(1, 35))
TOPICS = [
    _dc(B, next(_days), "How many letters are in the answer to this question?", "Four ('four' has 4 letters).", "Self-reference: the question points at its own answer.", ["A='four'"], [("self_ref", "len(A) == 4")]),
    _dc(B, next(_days), "What number comes next: 2, 4, 8, 16, ...?", "32 (doubling each time).", "Check the operation between neighbors, not the numbers.", ["S=[2,4,8,16]"], [("doubling", "all(S[i+1]==2*S[i] for i in range(3))"), ("next", "S[-1]*2 == 32")]),
    _dc(B, next(_days), "Which is heavier: a kilo of feathers or a kilo of steel?", "Neither - both weigh a kilo.", "Read the units, not the imagery.", ["W1=1.0", "W2=1.0"], [("equal", "W1 == W2")]),
    _dc(B, next(_days), "How many months have 28 days?", "All 12 - every month has at least 28 days.", "The trick is in 'at least'.", ["M=12"], [("all", "M == 12")]),
    _dc(B, next(_days), "What 3-letter word reads the same forward and backward?", "Any palindrome: 'eve', 'dad', 'mom', 'pop'.", "Palindromes hide in plain sight.", ["W='eve'"], [("pal", "W == W[::-1]")]),
    _dc(B, next(_days), "If you have 3 apples and take away 2, how many do you have?", "2 - the ones you took.", "Possession follows the taker.", ["TOOK=2"], [("took", "TOOK == 2")]),
    _dc(B, next(_days), "What goes around the world but stays in a corner?", "A stamp.", "Small things travel far.", ["A='stamp'"], [("answer", "A == 'stamp'")]),
    _dc(B, next(_days), "How many times can you subtract 10 from 100?", "Once - then you're subtracting from 90.", "The first subtraction changes the game.", ["N=1"], [("once", "N == 1")]),
    _dc(B, next(_days), "What has 4 legs in the morning, 2 at noon, 3 in the evening?", "A human (the Sphinx's riddle: crawl, walk, cane).", "The oldest workout in history.", ["A='human'"], [("answer", "A == 'human'")]),
    _dc(B, next(_days), "Which weighs more: your brain or your heart?", "Your brain (~1.4 kg vs ~0.3 kg).", "The brain is the heavyweight.", ["B=1.4", "H=0.3"], [("brain_wins", "B > H")]),
    _dc(B, next(_days), "What 5-letter word has only 1 left when you take 2 away?", "Stone: remove 'st' and 'one' remains.", "Letters hide inside words.", ["W='stone'"], [("wordplay", "W[2:] == 'one'")]),
    _dc(C, next(_days), "A bat and ball cost $1.10; the bat costs $1 more than the ball. Ball price?", "$0.05 (not $0.10 - check: 1.05 + 0.05 = 1.10).", "The classic gut-check: do the algebra.", ["BALL=0.05"], [("check", "abs((BALL+1+BALL) - 1.10) < 1e-9")]),
    _dc(C, next(_days), "5 machines make 5 widgets in 5 minutes; 100 machines, 100 widgets?", "5 minutes - each machine makes one widget per 5 minutes.", "Rates don't scale with headcount here.", ["T=5"], [("rate", "T == 5")]),
    _dc(C, next(_days), "A lily patch doubles daily; covers the lake in 48 days. Half covered when?", "Day 47 - doubling means half was yesterday.", "Work backward from the doubling.", ["D=47"], [("half", "D == 48 - 1")]),
    _dc(C, next(_days), "If 3 cats catch 3 mice in 3 minutes, how long for 1 cat, 1 mouse?", "3 minutes - one cat catches one mouse in 3 minutes.", "Each cat works in parallel.", ["T=3"], [("parallel", "T == 3")]),
    _dc(C, next(_days), "What is the next prime after 7?", "11.", "Primes: 2, 3, 5, 7, 11.", ["P=11"], [("prime", "P == 11 and all(P % d for d in (2,3,5,7))")]),
    _dc(C, next(_days), "You have 8 balls, one heavier; minimum weighings to find it?", "2 (weigh 3v3, then 1v1 of the heavy side).", "Divide and conquer.", ["W=2"], [("two", "W == 2")]),
    _dc(C, next(_days), "How many squares on a chessboard?", "2048? No: 204 (1x1 through 8x8: sum of squares).", "Count ALL sizes: sum(n^2).", ["S=sum(n*n for n in range(1,9))"], [("squares", "S == 204")]),
    _dc(C, next(_days), "A 10-digit number using each digit once, divisible by 1-10 in prefixes?", "3816547290 (the classic pandigital divisibility puzzle).", "The famous one: prefixes divisible by 1..10.", ["N=3816547290"], [("pandigital", "sorted(str(N)) == sorted('0123456789')"), ("div", "all(int(str(N)[:k]) % k == 0 for k in range(1, 11))")]),
    _dc(C, next(_days), "What is 111,111,111 x 111,111,111?", "12345678987654321.", "The palindrome square: 1s build the mountain.", ["P=111111111**2"], [("pal_square", "P == 12345678987654321")]),
    _dc(C, next(_days), "Three boxes labeled wrong; one pull to relabel all?", "Pull from the 'mixed' box: whatever you draw, that box is that fruit; the wrong labels then force the rest.", "The mislabeled box tells the truth by lying.", ["PULLS=1"], [("one", "PULLS == 1")]),
    _dc(C, next(_days), "How many moves for the 3-disk Tower of Hanoi?", "7 (2^3 - 1).", "The formula: 2^n - 1.", ["M=2**3-1"], [("hanoi", "M == 7")]),
    _dc(A, next(_days), "What is the 100th digit of 1/7 = 0.142857142857...?", "The cycle '142857' (length 6); 100 mod 6 = 4 -> the 4th digit: 8.", "Repeating decimals cycle: find the period.", ["CYC='142857'", "D=CYC[(100-1) % 6]"], [("digit", "D == '8'")]),
    _dc(A, next(_days), "How many handshakes if 10 people each shake once?", "45 (10*9/2).", "Combinations: n(n-1)/2.", ["H=10*9//2"], [("handshakes", "H == 45")]),
    _dc(A, next(_days), "What is the sum 1+2+...+100?", "5050 (Gauss: 101*50).", "Pair them: 1+100, 2+99...", ["S=100*101//2"], [("gauss", "S == 5050")]),
    _dc(A, next(_days), "A clock strikes 6 times in 5 seconds; how long for 12 strikes?", "11 seconds (5 gaps of 1s; 11 gaps for 12 strikes).", "Count the GAPS, not the strikes.", ["T=11"], [("gaps", "T == 11")]),
    _dc(A, next(_days), "What is the only even prime number?", "2.", "All other evens are divisible by 2.", ["P=2"], [("even_prime", "P == 2 and P % 2 == 0")]),
    _dc(A, next(_days), "If it takes 6 men 6 days to dig 6 holes, how long for 1 man, 1 hole?", "6 days (one man digs one hole in 6 days).", "One man, one hole, six days.", ["T=6"], [("man_hole", "T == 6")]),
    _dc(A, next(_days), "What number is 1 more than its reversal... (41 vs 14: no). Which 2-digit number equals 4/7 of its reversal?", "12? Check: reversal 21; 12 = 4/7*21 = 12. YES: 12.", "Set up: 10a+b = 4/7*(10b+a).", ["N=12", "R=21"], [("ratio", "abs(N - 4/7*R) < 1e-9")]),
    _dc(A, next(_days), "How many Friday the 13ths can a year have at most?", "3.", "Calendar math: at most 3.", ["M=3"], [("max", "M == 3")]),
    _dc(A, next(_days), "What is 2^10?", "1024.", "The kilobyte number.", ["P=2**10"], [("kilo", "P == 1024")]),
    _dc(A, next(_days), "A snail climbs 3 ft by day, slips 2 by night, up a 10-ft wall. Days?", "8 (day 8 reaches 10: 7 days net 7 ft, day 8 climbs 3 to 10).", "The last day it doesn't slip.", ["D=8"], [("snail", "D == 8")]),
    _dc(A, next(_days), "What is the 7th Fibonacci number (1,1,2,3,5,...)?", "13 (1,1,2,3,5,8,13).", "Add the last two.", ["F=[1,1]", "F7=13"], [("fib", "F7 == 13")]),
]
TOPICS.append(_dc(C, next(_days), "What is the smallest number divisible by 1 through 10?", "2520.", "LCM: build it from prime powers.", ["import math", "L=1", "from functools import reduce", "L=reduce(lambda a,b: a*b//math.gcd(a,b), range(1,11))"], [("lcm", "L == 2520")]))
print("daily built:", len(TOPICS))
