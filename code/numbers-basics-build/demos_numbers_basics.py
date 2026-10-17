#!/usr/bin/env python3
"""Demo programs for The Numbers Basics Database (fundamentals order #9).

Every demo is real, runnable, stdlib-only Python performing the actual
foundational computation for its record. All are machine-executed by
build.py: each prints its real computed values, asserts tight bounds
(never float exact-equality - integer arithmetic wherever possible),
and ends with the OK marker.
"""

import json as _json

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", _json.dumps(name))


def demo_nb_what_is_number(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the number is what two matched piles share: pair every apple with a stone
    apples = ["apple%d" % i for i in range(10)]
    stones = ["stone%d" % i for i in range(10)]
    pairs = list(zip(apples, stones))
    assert len(pairs) == 10 and len(set(a for a, s in pairs)) == 10
    # count the pile one by one: the last count word is the number
    count = 0
    for a in apples:
        count += 1
    print("pile counted one by one: %d" % count)
    assert count == 10
    # zero is the honest answer for an empty pile
    empty = []
    print("empty pile count: %d" % len(empty))
    assert len(empty) == 0
    print("rule: the number is what matched piles share")
    print("OK: %s named the threeness" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nb_counting_first_skill(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # one-to-one matching: each item gets exactly one count word, in order
    items = ["toy%d" % i for i in range(12)]
    words = ["one","two","three","four","five","six","seven","eight",
             "nine","ten","eleven","twelve"]
    assigned = {}
    for item, word in zip(items, words):
        assigned[item] = word
    assert len(assigned) == 12 and len(set(assigned.values())) == 12
    total = words[len(items) - 1]
    print("twelve items counted, last word said: %s" % total)
    assert total == "twelve"
    # recount from a different starting point: same total (cardinality)
    total2 = len(items)
    print("recount from other end: %d" % total2)
    assert total2 == 12
    print("rule: last word said is the answer")
    print("OK: %s kept the five rules" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nb_number_line(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the line from 0 to 10: address of 7, distance from 3 to 8, hops for 2+3
    line = list(range(0, 11))
    address_of_7 = line.index(7)
    print("address of 7: %d" % address_of_7)
    assert address_of_7 == 7
    distance = abs(line.index(8) - line.index(3))
    print("steps from 3 to 8: %d" % distance)
    assert distance == 5
    # addition as rightward hops: start at 2, hop right 3
    pos = 2
    for _ in range(3):
        pos += 1
    print("2 plus 3 by hopping: %d" % pos)
    assert pos == 5
    print("rule: position is size, right is more")
    print("OK: %s walked the line" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nb_numerals_words(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the three faces: word -> numeral -> word round trips for 0..20
    table = {0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",
             7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve",
             13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",
             17:"seventeen",18:"eighteen",19:"nineteen",20:"twenty"}
    back = {w: n for n, w in table.items()}
    for n in range(0, 21):
        assert back[table[n]] == n, n
    print("round trips 0..20: all 21 pass")
    # the teen exceptions map correctly, no confusion
    for w, n in [("eleven",11),("twelve",12),("thirteen",13),
                 ("fourteen",14),("fifteen",15)]:
        assert back[w] == n
    print("teen words map: eleven->11 ... fifteen->15")
    print("rule: hear it, write it, read it - three faces, one number")
    print("OK: %s knew every face" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nb_more_less_same(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # count two piles, then decide with the three verdict symbols
    pile_a = 9
    pile_b = 7
    print("pile A: %d, pile B: %d" % (pile_a, pile_b))
    assert pile_a > pile_b
    assert pile_b < pile_a
    assert pile_a == 9 and pile_b == 7
    print("9 > 7, 7 < 9: verdicts hold")
    pile_c = 7
    assert pile_b == pile_c
    print("7 = 7: the same")
    # hungry-mouth rule: open side faces the larger count
    assert (9 > 7) and not (7 > 9)
    print("rule: the open mouth faces the bigger pile")
    print("OK: %s judged truly" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nb_ordering_numbers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # repeated-find-smallest on the mixed set
    mixed = [7, 3, 9, 1, 5]
    remaining = list(mixed)
    ordered = []
    while remaining:
        smallest = min(remaining)
        ordered.append(smallest)
        remaining.remove(smallest)
    print("mixed: %s -> ordered: %s" % (mixed, ordered))
    assert ordered == [1, 3, 5, 7, 9]
    # neighbor test: every adjacent pair satisfies <
    for i in range(len(ordered) - 1):
        assert ordered[i] < ordered[i + 1]
    print("neighbor test: 1<3<5<7<9 all true")
    assert list(reversed(ordered)) == [9, 7, 5, 3, 1]
    print("greatest-to-least: [9, 7, 5, 3, 1]")
    print("rule: every number finds its place")
    print("OK: %s mustered the numbers" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nb_before_after_between(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # neighbors by stepping one on the counting line
    before_6 = 6 - 1
    after_6 = 6 + 1
    print("before 6: %d, after 6: %d" % (before_6, after_6))
    assert before_6 == 5 and after_6 == 7
    # decade crossing: before 20 is 19
    assert 20 - 1 == 19
    print("before 20: 19 (decade crossing holds)")
    # between 4 and 6: the n with 4 < n < 6
    between = [n for n in range(0, 11) if 4 < n < 6]
    print("between 4 and 6: %s" % between)
    assert between == [5]
    assert 5 < 6 < 7
    print("neighbor chain 5 < 6 < 7: true")
    print("rule: one less, one more, and the middle")
    print("OK: %s knew the neighbors" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nb_place_value_tens(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # split 47 into tens and ones, then rebuild
    n = 47
    tens = n // 10
    ones = n % 10
    print("47 -> tens: %d, ones: %d" % (tens, ones))
    assert tens == 4 and ones == 7
    rebuilt = tens * 10 + ones * 1
    print("rebuilt: 4 x 10 + 7 x 1 = %d" % rebuilt)
    assert rebuilt == 47
    # the bundling law: ten ones trade for one ten
    loose = 10
    bundles, left = divmod(loose, 10)
    assert bundles == 1 and left == 0
    print("10 loose ones -> 1 ten-bundle, 0 left")
    print("rule: position is worth")
    print("OK: %s bundled truly" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nb_place_value_big(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # decompose 3,528 digit by digit, then rebuild by expanded form
    n = 3528
    digits = []
    temp = n
    for _ in range(4):
        digits.append(temp % 10)
        temp //= 10
    digits.reverse()
    print("3528 -> digits: %s" % digits)
    assert digits == [3, 5, 2, 8]
    rebuilt = digits[0]*1000 + digits[1]*100 + digits[2]*10 + digits[3]*1
    print("expanded: 3x1000 + 5x100 + 2x10 + 8x1 = %d" % rebuilt)
    assert rebuilt == 3528
    # zero the placeholder: 4,062 keeps its hundreds post
    z = [4, 0, 6, 2]
    assert z[1] == 0
    assert z[0]*1000 + z[1]*100 + z[2]*10 + z[3] == 4062
    print("4062: zero holds the hundreds place")
    print("rule: every digit at its post")
    print("OK: %s read the big places" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nb_even_odd(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # pairing test on 0..20: remainder 0 means even
    evens = [n for n in range(0, 21) if n % 2 == 0]
    odds = [n for n in range(0, 21) if n % 2 == 1]
    print("evens 0..20: %s" % evens)
    assert evens == [0,2,4,6,8,10,12,14,16,18,20]
    assert len(odds) == 10 and odds[0] == 1
    # ones-digit shortcut on big numbers
    assert (3528 % 10) in (0,2,4,6,8)
    assert (4061 % 10) in (1,3,5,7,9)
    print("3528 even (ones 8), 4061 odd (ones 1)")
    # parity of sums
    assert (4 + 6) % 2 == 0 and (3 + 5) % 2 == 0 and (4 + 5) % 2 == 1
    print("even+even=even, odd+odd=even, even+odd=odd")
    print("rule: the ones digit tells the pairing")
    print("OK: %s read the banners" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nb_adding_together(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # join the piles and recount
    pile = ["apple%d" % i for i in range(5)] + ["apple%d" % i for i in range(5, 8)]
    total = len(pile)
    print("5 apples + 3 apples = %d apples" % total)
    assert total == 8
    # counting on: hold 5, count 3 more
    n = 5
    for _ in range(3):
        n += 1
    assert n == 8
    print("counting on from 5: %d" % n)
    # commutativity and identity
    assert 3 + 5 == 8 and 5 + 0 == 5
    print("3 + 5 = 8 (order free), 5 + 0 = 5 (zero changes nothing)")
    print("rule: put together, count the whole")
    print("OK: %s gathered truly" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nb_subtracting_away(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # take 4 from 9, count what remains
    pile = list(range(9))
    taken = pile[:4]
    left = pile[4:]
    print("9 take away 4: %d left" % len(left))
    assert len(left) == 5
    # counting back: 9, then 4 steps down
    n = 9
    for _ in range(4):
        n -= 1
    assert n == 5
    print("counting back from 9: %d" % n)
    # the addition check: subtraction undone by addition
    assert 5 + 4 == 9
    print("check: 5 + 4 = 9, so 9 - 4 = 5 is certain")
    print("rule: what is taken is gone; what remains is counted")
    print("OK: %s withdrew honestly" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "what_is_number": demo_nb_what_is_number,
    "counting_first_skill": demo_nb_counting_first_skill,
    "number_line": demo_nb_number_line,
    "numerals_words": demo_nb_numerals_words,
    "more_less_same": demo_nb_more_less_same,
    "ordering_numbers": demo_nb_ordering_numbers,
    "before_after_between": demo_nb_before_after_between,
    "place_value_tens": demo_nb_place_value_tens,
    "place_value_big": demo_nb_place_value_big,
    "even_odd": demo_nb_even_odd,
    "adding_together": demo_nb_adding_together,
    "subtracting_away": demo_nb_subtracting_away,
}

def demo_nb_facts_to_10(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # every addition fact 0..9 x 0..9, verified against arithmetic itself
    facts = {}
    for a in range(0, 10):
        for b in range(0, 10):
            facts[(a, b)] = a + b
    print("addition facts 0..9: %d" % len(facts))
    assert len(facts) == 100
    assert facts[(9, 9)] == 18 and facts[(8, 5)] == 13
    # subtraction facts derived as inverses
    assert facts[(8, 5)] - 8 == 5
    print("anchors: 9+9=18, 8+5=13, 13-8=5")
    # the 3-5-8 family: four facts from three numbers
    a, b, c = 3, 5, 8
    assert a + b == c and b + a == c and c - a == b and c - b == a
    print("family 3-5-8: 3+5=8, 5+3=8, 8-3=5, 8-5=3")
    print("rule: four facts for the price of one")
    print("OK: %s swore the hundred oaths" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nb_add_two_digit(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # column addition on 34 + 28, right to left with the carry
    a, b = 34, 28
    ones_sum = (a % 10) + (b % 10)
    carry, ones_digit = divmod(ones_sum, 10)
    tens_sum = (a // 10) + (b // 10) + carry
    total = tens_sum * 10 + ones_digit
    print("ones: 4 + 8 = %d -> write %d, carry %d" % (ones_sum, ones_digit, carry))
    print("tens: 3 + 2 + %d = %d" % (carry, tens_sum))
    print("34 + 28 = %d" % total)
    assert ones_sum == 12 and carry == 1 and ones_digit == 2
    assert tens_sum == 6 and total == 62
    # expanded-form cross-check
    assert (30 + 4) + (20 + 8) == 62
    print("cross-check (30+4)+(20+8) = 62")
    print("rule: bundle tens as they form, march left")
    print("OK: %s mustered the columns" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nb_subtract_two_digit(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # column subtraction on 52 - 27 with borrowing as un-bundling
    a, b = 52, 27
    a_tens, a_ones = a // 10, a % 10
    b_tens, b_ones = b // 10, b % 10
    if a_ones < b_ones:
        a_tens -= 1
        a_ones += 10
        print("borrow: 5 tens 2 ones -> 4 tens 12 ones")
    assert a_tens == 4 and a_ones == 12
    d_ones = a_ones - b_ones
    d_tens = a_tens - b_tens
    diff = d_tens * 10 + d_ones
    print("ones: 12 - 7 = %d, tens: 4 - 2 = %d" % (d_ones, d_tens))
    print("52 - 27 = %d" % diff)
    assert diff == 25
    # inverse check
    assert 25 + 27 == 52
    print("check: 25 + 27 = 52")
    print("rule: un-bundle first, then pay, then check")
    print("OK: %s paid in full" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nb_multiplication_groups(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # four bags of three, counted as repeated addition
    groups = [[1, 1, 1] for _ in range(4)]
    total = sum(sum(g) for g in groups)
    print("4 groups of 3: %d" % total)
    assert total == 12
    assert 4 * 3 == 12
    # the array rotated: 3 x 4 is the same twelve
    assert 3 * 4 == 12
    print("3 x 4 = 12: the rectangle rotated, same dots")
    # the special cases
    assert 7 * 0 == 0 and 7 * 1 == 7
    print("7 x 0 = 0 (no groups, nothing), 7 x 1 = 7 (one group, unchanged)")
    print("rule: equal groups, counted fast")
    print("OK: %s mustered the formation" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nb_multiplication_facts(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the 0..10 table built by repeated addition
    table = {}
    for a in range(0, 11):
        for b in range(0, 11):
            table[(a, b)] = sum(b for _ in range(a))
    print("times table 0..10: %d facts" % len(table))
    assert len(table) == 121
    assert table[(7, 8)] == 56 and table[(9, 7)] == 63
    print("anchors: 7 x 8 = 56, 9 x 7 = 63")
    # the 5 row ends in 0 or 5
    for b in range(0, 11):
        assert table[(5, b)] % 10 in (0, 5)
    print("5 row: every product ends in 0 or 5")
    # the 9 row: digits sum to 9
    for b in range(1, 11):
        p = table[(9, b)]
        assert p // 10 + p % 10 == 9, (b, p)
    print("9 row: digits of every product sum to 9")
    # symmetry: commutativity across the whole table
    for a in range(0, 11):
        for b in range(0, 11):
            assert table[(a, b)] == table[(b, a)]
    print("symmetric: a x b == b x a everywhere")
    print("rule: patterns plus recall")
    print("OK: %s learned the table" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nb_division_sharing(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # sharing: deal 12 cookies round by round to 3 children
    children = [[], [], []]
    cookies = list(range(12))
    i = 0
    while cookies:
        children[i % 3].append(cookies.pop(0))
        i += 1
    shares = [len(c) for c in children]
    print("12 cookies, 3 children: shares %s" % shares)
    assert shares == [4, 4, 4]
    # grouping: pack 12 cookies 3 to a bag
    bags = 0
    left = 12
    while left >= 3:
        left -= 3
        bags += 1
    print("12 cookies, 3 per bag: %d bags, %d left" % (bags, left))
    assert bags == 4 and left == 0
    assert 4 * 3 == 12
    # the remainder case: 13 cookies
    q, r = divmod(13, 3)
    print("13 / 3: quotient %d remainder %d" % (q, r))
    assert q == 4 and r == 1 and 4 * 3 + 1 == 13
    print("rule: deal fairly, name the leftover")
    print("OK: %s shared fairly" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nb_mult_div_relation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # one array, four facts: the 3-4-12 family
    rows, cols = 3, 4
    dots = rows * cols
    print("3-by-4 array: %d dots" % dots)
    assert dots == 12
    assert 3 * 4 == 12 and 4 * 3 == 12
    assert 12 // 3 == 4 and 12 // 4 == 3
    print("family: 3x4=12, 4x3=12, 12/3=4, 12/4=3")
    # unknown factor solved by division, proved by substitution
    unknown = 12 // 3
    assert 3 * unknown == 12
    print("3 x ? = 12 -> ? = 12 / 3 = %d, check 3 x %d = 12" % (unknown, unknown))
    print("rule: one covenant, read both ways")
    print("OK: %s read backward and forward" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nb_fractions_parts(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # a whole split into 4 equal parts: quarters reassemble to the whole
    from fractions import Fraction
    whole = Fraction(1, 1)
    quarters = [Fraction(1, 4)] * 4
    assert sum(quarters) == whole
    print("1/4 + 1/4 + 1/4 + 1/4 = %s (the whole)" % sum(quarters))
    assert Fraction(1, 2) + Fraction(1, 2) == 1
    print("1/2 + 1/2 = 1")
    # part of a set: 3/4 of 12 marbles
    marbles = 12
    groups = marbles // 4
    share = 3 * groups
    print("3/4 of 12 marbles: %d" % share)
    assert share == 9
    assert Fraction(3, 4) * 12 == 9
    print("rule: equal pieces, honestly counted")
    print("OK: %s cut fairly" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nb_fractions_number_line(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # addresses on the subdivided unit segment, exact rational arithmetic
    from fractions import Fraction
    addr_34 = Fraction(3, 4)
    addr_12 = Fraction(1, 2)
    print("address of 3/4: %s, address of 1/2: %s" % (addr_34, addr_12))
    assert Fraction(1, 2) < addr_34 < Fraction(1, 1)
    # equivalent fractions share one address
    assert Fraction(1, 2) == Fraction(2, 4) == Fraction(3, 6)
    print("1/2 = 2/4 = 3/6: one address, three names")
    # order on the line
    assert Fraction(1, 4) < Fraction(1, 2) < Fraction(3, 4) < Fraction(1, 1)
    print("1/4 < 1/2 < 3/4 < 1: left to right, least to greatest")
    assert Fraction(3, 4) > Fraction(1, 2)
    print("3/4 sits right of 1/2, so 3/4 > 1/2")
    print("rule: every fraction has an address")
    print("OK: %s placed the milestones" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nb_comparing_fractions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # same denominator: compare numerators
    from fractions import Fraction
    assert Fraction(3, 8) < Fraction(5, 8)
    print("3/8 < 5/8: same pieces, fewer pieces loses")
    # same numerator: bigger denominator loses
    assert Fraction(3, 8) < Fraction(3, 4)
    print("3/8 < 3/4: same count, smaller pieces loses")
    # cross-multiplication: 2/3 vs 3/5
    left_cross = 2 * 5
    right_cross = 3 * 3
    print("2/3 vs 3/5: cross products %d vs %d" % (left_cross, right_cross))
    assert left_cross == 10 and right_cross == 9
    assert Fraction(2, 3) > Fraction(3, 5)
    print("10 > 9, so 2/3 > 3/5: the scales agree with the exact value")
    print("rule: weigh piece-count against piece-size")
    print("OK: %s weighed the shares" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nb_mixed_numbers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 7/3 -> mixed by division with remainder
    num, den = 7, 3
    whole, rem = divmod(num, den)
    print("7/3: %d wholes, %d/%d left over" % (whole, rem, den))
    assert whole == 2 and rem == 1
    # back to improper: (whole x den + num) / den
    back_num = whole * den + rem
    print("2 1/3 -> (%d x %d + %d)/%d = %d/%d" % (whole, den, rem, den, back_num, den))
    assert back_num == 7
    from fractions import Fraction
    assert Fraction(7, 3) == whole + Fraction(rem, den)
    print("7/3 = 2 + 1/3: both forms name the same amount")
    # on the line: between 2 and 3
    assert 2 < Fraction(7, 3) < 3
    print("2 1/3 sits between 2 and 3")
    print("rule: wholes separated, leftovers named")
    print("OK: %s took honest inventory" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS.update({
    "facts_to_10": demo_nb_facts_to_10,
    "add_two_digit": demo_nb_add_two_digit,
    "subtract_two_digit": demo_nb_subtract_two_digit,
    "multiplication_groups": demo_nb_multiplication_groups,
    "multiplication_facts": demo_nb_multiplication_facts,
    "division_sharing": demo_nb_division_sharing,
    "mult_div_relation": demo_nb_mult_div_relation,
    "fractions_parts": demo_nb_fractions_parts,
    "fractions_number_line": demo_nb_fractions_number_line,
    "comparing_fractions": demo_nb_comparing_fractions,
    "mixed_numbers": demo_nb_mixed_numbers,
})

def demo_nb_decimals_tenths(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # decimal addition in integer tenths: 0.3 + 0.4 = 0.7
    tenths_sum = 3 + 4
    print("3 tenths + 4 tenths = %d tenths = 0.%d" % (tenths_sum, tenths_sum))
    assert tenths_sum == 7
    # 3/4 as a decimal by division
    val = 3 / 4
    print("3/4 = %.2f" % val)
    assert 0.749 < val < 0.751
    # trailing zeros change nothing: 0.50 and 0.5 share the value
    assert abs(50 / 100 - 5 / 10) < 1e-12
    print("0.50 = 50/100 = 5/10 = 0.5")
    # ordering left to right by place: 0.47 < 0.5 < 0.75
    assert 47 < 50 < 75
    print("47 hundredths < 50 hundredths < 75 hundredths")
    print("rule: tenths with tenths, like places together")
    print("OK: %s kept the fine ledger" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nb_money_decimals(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # count in integer cents: no decimal wobble
    price1 = 235  # $2.35
    price2 = 145  # $1.45
    total = price1 + price2
    print("$2.35 + $1.45 = %d cents = $%d.%02d" % (total, total // 100, total % 100))
    assert total == 380
    # change from $5.00 after a $3.80 purchase
    change = 500 - 380
    print("change from $5.00: %d cents = $%d.%02d" % (change, change // 100, change % 100))
    assert change == 120
    # count-up check: 380 + 20 = 400, 400 + 100 = 500
    assert 380 + 20 + 100 == 500
    print("count-up: 380 + 20 + 100 = 500, change 120")
    print("rule: cents are whole, honest integers")
    print("OK: %s counted the purse truly" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nb_rounding_estimating(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the halfway rule to the nearest ten
    def round_ten(n):
        d = n % 10
        return n - d + (10 if d >= 5 else 0)
    r47 = round_ten(47)
    r43 = round_ten(43)
    print("47 -> %d, 43 -> %d" % (r47, r43))
    assert r47 == 50 and r43 == 40
    # estimate 48 + 31 with compatible numbers
    estimate = round_ten(48) + round_ten(31)
    truth = 48 + 31
    print("estimate 50 + 30 = %d, truth = %d" % (estimate, truth))
    assert estimate == 80 and truth == 79
    assert abs(estimate - truth) <= 5
    print("estimate within 5 of truth: guard passes")
    # the guard catches a planted wrong answer
    wrong = 109
    assert abs(wrong - estimate) > 20
    print("planted wrong answer 109: guard rejects, recompute")
    print("rule: estimate first, compute second, check third")
    print("OK: %s posted the guard" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nb_number_patterns(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # find the step, predict, verify
    seq = [5, 10, 15, 20]
    diffs = [seq[i+1] - seq[i] for i in range(len(seq) - 1)]
    print("sequence %s, steps %s" % (seq, diffs))
    assert diffs == [5, 5, 5]
    nxt = seq[-1] + 5
    print("rule 'add 5', next term: %d" % nxt)
    assert nxt == 25
    extended = seq + [25, 30, 35]
    for i in range(len(seq), len(extended) - 1):
        assert extended[i+1] - extended[i] == 5
    print("extended keeps the step: verified")
    # square numbers: n-squared, with odd-number gaps
    squares = [n * n for n in range(1, 6)]
    print("squares 1..5: %s" % squares)
    assert squares == [1, 4, 9, 16, 25]
    gaps = [squares[i+1] - squares[i] for i in range(4)]
    assert gaps == [3, 5, 7, 9]
    print("gaps %s: the odd numbers, a pattern inside the pattern" % gaps)
    print("rule: list, step, predict, verify")
    print("OK: %s read the footprints" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nb_primes_composites(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the sieve of Eratosthenes to 30
    limit = 30
    alive = [True] * (limit + 1)
    alive[0] = alive[1] = False
    p = 2
    while p * p <= limit:
        if alive[p]:
            for m in range(p * p, limit + 1, p):
                alive[m] = False
        p += 1
    primes = [n for n in range(limit + 1) if alive[n]]
    print("primes to 30: %s" % primes)
    assert primes == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    # 12 = 2 x 2 x 3, the only prime recipe
    factors = []
    n = 12
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    print("12 factors into: %s" % factors)
    assert factors == [2, 2, 3]
    prod = 1
    for f in factors:
        prod *= f
    assert prod == 12
    # 1 is neither
    assert len([d for d in range(1, 2) if 1 % d == 0]) == 1
    print("1 has one divisor: neither prime nor composite")
    print("rule: the sieve separates the unbreakable from the built")
    print("OK: %s ran the muster" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nb_measuring_numbers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # unit rates are exact: convert and convert back
    inches = 3 * 12
    print("3 feet x 12 in/ft = %d inches" % inches)
    assert inches == 36
    assert inches // 12 == 3
    print("36 inches back to feet: %d" % (inches // 12))
    grams = 2 * 1000
    print("2 kg x 1000 g/kg = %d grams" % grams)
    assert grams == 2000
    # between-marks reading: halfway between 7 and 8 cm
    reading_tenths = 75  # 7.5 cm in tenths
    print("halfway between 7 and 8 cm: 7.%d cm" % (reading_tenths % 10))
    assert reading_tenths == 75
    assert 70 < reading_tenths < 80
    print("rule: the unit is part of the answer")
    print("OK: %s numbered the real" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nb_word_problems(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # story 1: 15 apples, eat 6, buy 4
    after_eating = 15 - 6
    final = after_eating + 4
    print("15 - 6 = %d, %d + 4 = %d apples" % (after_eating, after_eating, final))
    assert after_eating == 9 and final == 13
    assert 0 <= final <= 15 + 4
    print("sensibility: 13 between 0 and 19, passes")
    # story 2: 4 bags, 6 marbles each - equal groups multiply
    marbles = 4 * 6
    print("4 bags x 6 marbles = %d marbles" % marbles)
    assert marbles == 24
    assert marbles // 4 == 6
    print("check: 24 / 4 = 6 per bag")
    print("rule: picture, operate, compute, check")
    print("OK: %s answered the dispatch" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nb_negative_numbers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # order left of zero: further left is smaller
    assert -5 < -2
    print("-5 < -2: nearer zero is greater")
    # walk right from -5 by 8 steps
    pos = -5
    for _ in range(8):
        pos += 1
    print("-5 + 8 by stepping: %d" % pos)
    assert pos == 3
    # temperature story
    assert -5 + 8 == 3
    print("-5 degrees, warms 8: 3 degrees")
    # below zero by subtraction
    assert 3 - 5 == -2
    print("3 - 5 = -2: the road runs past zero")
    # opposites cancel
    assert 4 + (-4) == 0
    print("4 + (-4) = 0: the balanced scales")
    print("rule: the line rules never change, only the ground")
    print("OK: %s walked the far side" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nb_properties_operations(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # commutative: order free for + and x
    assert 5 + 3 == 3 + 5 == 8
    assert 4 * 7 == 7 * 4 == 28
    print("5+3=3+5=8, 4x7=7x4=28: order free")
    # associative: grouping free
    assert (8 + 2) + 3 == 8 + (2 + 3) == 13
    print("(8+2)+3 = 8+(2+3) = 13: regroup at will")
    # identity
    assert 7 + 0 == 7 and 7 * 1 == 7
    print("7+0=7, 7x1=7: the quiet partners")
    # distributive: 3 x 14 split apart
    split = 3 * 10 + 3 * 4
    direct = 3 * 14
    print("3 x (10+4) = 30 + 12 = %d, direct 3 x 14 = %d" % (split, direct))
    assert split == 42 and direct == 42
    # the boundary: subtraction does NOT commute
    assert 9 - 4 != 4 - 9
    print("9-4=5 but 4-9=-5: subtraction exempt from the law")
    print("rule: know which operations obey which laws")
    print("OK: %s learned the high laws" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nb_checking_work(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # claim: 47 + 28 = 75; four independent checks
    claim = 47 + 28
    assert claim == 75
    # 1. inverse check
    assert 75 - 28 == 47
    print("inverse: 75 - 28 = 47, passes")
    # 2. estimate check
    assert abs(75 - 80) <= 5
    print("estimate: 75 within 5 of 80, passes")
    # 3. reasonableness: sum exceeds each addend
    assert 75 > 47 and 75 > 28
    print("reasonableness: 75 > 47 and 75 > 28, passes")
    # 4. re-do by expanded form
    assert (40 + 7) + (20 + 8) == 75
    print("re-do: (40+7)+(20+8) = 75, matches")
    # the checks catch a planted wrong answer
    wrong = 65
    assert wrong - 28 != 47
    print("planted 65: inverse check 65-28=37 != 47, caught")
    print("rule: no oath sworn until verified")
    print("OK: %s sealed the work" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nb_numbers_big_picture(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the crown sum: 1 + 2 + ... + 100 by pairing
    pairs = [(i, 101 - i) for i in range(1, 51)]
    print("pairs: %d" % len(pairs))
    assert len(pairs) == 50
    for a, b in pairs:
        assert a + b == 101, (a, b)
    print("first pair 1+100=101, middle 25+76=101, last 50+51=101: all 101")
    total = 50 * 101
    print("50 x 101 = %d" % total)
    assert total == 5050
    # cross-check against the direct sum
    assert sum(range(1, 101)) == 5050
    print("direct sum 1..100 = 5050: the pairing is true")
    print("rule: every rung earned, the view complete")
    print("OK: %s reached the summit" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS.update({
    "decimals_tenths": demo_nb_decimals_tenths,
    "money_decimals": demo_nb_money_decimals,
    "rounding_estimating": demo_nb_rounding_estimating,
    "number_patterns": demo_nb_number_patterns,
    "primes_composites": demo_nb_primes_composites,
    "measuring_numbers": demo_nb_measuring_numbers,
    "word_problems": demo_nb_word_problems,
    "negative_numbers": demo_nb_negative_numbers,
    "properties_operations": demo_nb_properties_operations,
    "checking_work": demo_nb_checking_work,
    "numbers_big_picture": demo_nb_numbers_big_picture,
})

assert set(DEMOS) == {e["key"] for e in __import__("entries_numbers_basics").ENTRIES}, \
    "demo map misses entries"
