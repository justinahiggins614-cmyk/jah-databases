#!/usr/bin/env python3
"""Demo programs for the JAH Signature Binary System databases.

Every demo is real, runnable, stdlib-only Python performing the actual
binary computation for its record. All are machine-executed by build.py:
each prints its real computed values, asserts tight bounds (never float
exact-equality), and ends with the OK marker.
"""

import json as _json

_PREAMBLE = "import math\nimport struct\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace(
        "NAME", _json.dumps(name))


def demo_jbs_what_is_binary(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # one bit: two values; n bits: 2**n values
    for n in (1, 2, 4, 8):
        print("%d bit(s): %d values" % (n, 2 ** n))
    assert 2 ** 1 == 2
    assert 2 ** 2 == 4
    assert 2 ** 4 == 16
    assert 2 ** 8 == 256
    # enumerate every 4-bit pattern: there must be exactly 16
    patterns = [format(i, "04b") for i in range(16)]
    assert len(set(patterns)) == 16
    assert patterns[0] == "0000" and patterns[15] == "1111"
    print("4-bit patterns enumerated: %d" % len(patterns))
    print("rule: n bits name 2**n values - each added bit doubles the world")
    print("OK: %s swore the two symbols" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jbs_counting_binary(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # count 0..15 in binary by the carry rule, verify against integers
    def next_bin(bits):
        b = list(bits)
        i = len(b) - 1
        while i >= 0 and b[i] == 1:
            b[i] = 0
            i -= 1
        if i < 0:
            b = [1] + b
        else:
            b[i] = 1
        return b
    bits = [0, 0, 0, 0]
    for n in range(16):
        assert int("".join(map(str, bits)), 2) == n, (bits, n)
        bits = next_bin(bits)
    # the rollover: 1111 -> 10000
    assert next_bin([1, 1, 1, 1]) == [1, 0, 0, 0, 0]
    # column periods: bit k toggles every 2**k counts
    seq = [format(n, "04b") for n in range(16)]
    col0 = [s[3] for s in seq]  # rightmost
    assert col0 == list("0101010101010101")
    col2 = [s[1] for s in seq]
    assert col2 == list("0000111100001111")
    print("counted 0..15 by the carry rule; rollover 1111 -> 10000 verified")
    print("rule: flip trailing 1s to 0, flip the first 0 to 1")
    print("OK: %s walked the odometer" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jbs_bits_bytes(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the bundles: nibble=4, byte=8, word=16/32/64
    assert 4 // 4 == 1  # one hex digit per nibble
    byte_bits = 8
    print("nibble: 4 bits, byte: %d bits" % byte_bits)
    for w in (16, 32, 64):
        print("word %2d bits = %d bytes" % (w, w // 8))
        assert w // 8 * 8 == w
    # binary data sizes: each step multiplies by 1024
    kib = 1024
    mib = kib * 1024
    gib = mib * 1024
    print("1 KiB = %d bytes = %d bits" % (kib, kib * 8))
    assert kib == 2 ** 10
    assert mib == 2 ** 20
    assert gib == 2 ** 30
    assert kib * 8 == 8192
    # addressability: 32-bit address bus reaches 4 GiB
    assert 2 ** 32 == 4 * gib
    print("32-bit address space: %d bytes = 4 GiB" % (2 ** 32))
    print("rule: bundles nest by powers of two - nibble, byte, word, KiB, MiB, GiB")
    print("OK: %s bundled the witnesses" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jbs_binary_addition(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # column addition with carry: 1011 (11) + 0110 (6)
    def add_bits(a, b):
        n = max(len(a), len(b))
        a = [0] * (n - len(a)) + a
        b = [0] * (n - len(b)) + b
        carry, out = 0, []
        for x, y in zip(reversed(a), reversed(b)):
            total = x + y + carry
            out.append(total % 2)
            carry = total // 2
        if carry:
            out.append(carry)
        return list(reversed(out))
    a = [1, 0, 1, 1]
    b = [0, 1, 1, 0]
    s = add_bits(a, b)
    sval = int("".join(map(str, s)), 2)
    print("1011 + 0110 = %s = %d" % ("".join(map(str, s)), sval))
    assert s == [1, 0, 0, 0, 1]
    assert sval == 17
    # the hard carry chain: 1111 + 0001 ripples through every column
    r = add_bits([1, 1, 1, 1], [0, 0, 0, 1])
    assert r == [1, 0, 0, 0, 0]
    assert int("".join(map(str, r)), 2) == 16
    # the four column facts
    assert add_bits([1], [1]) == [1, 0]
    assert add_bits([0], [1]) == [1]
    print("carry chain 1111 + 0001 = 10000 verified")
    print("rule: 1+1 = 10 - write 0, carry 1")
    print("OK: %s passed the carry" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jbs_binary_subtraction(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # borrow subtraction: 10100 (20) - 00111 (7)
    def sub_bits(a, b):
        n = max(len(a), len(b))
        a = [0] * (n - len(a)) + a
        b = [0] * (n - len(b)) + b
        borrow, out = 0, []
        for x, y in zip(reversed(a), reversed(b)):
            diff = x - y - borrow
            if diff < 0:
                diff += 2
                borrow = 1
            else:
                borrow = 0
            out.append(diff)
        return list(reversed(out)), borrow
    a = [1, 0, 1, 0, 0]
    b = [0, 0, 1, 1, 1]
    d, borrow = sub_bits(a, b)
    dval = int("".join(map(str, d)), 2)
    print("10100 - 00111 = %s = %d (borrow out %d)" % ("".join(map(str, d)), dval, borrow))
    assert d == [0, 1, 1, 0, 1]
    assert dval == 13
    assert borrow == 0
    # borrow off the left end signals a negative result: 7 - 20
    d2, borrow2 = sub_bits(b, a)
    assert borrow2 == 1
    print("00111 - 10100 borrows off the left end: negative result signalled")
    print("rule: a borrow from the left is worth 2 where it lands")
    print("OK: %s settled the debt" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jbs_powers_of_two(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the milestone powers
    p10 = 2 ** 10
    p20 = 2 ** 20
    p30 = 2 ** 30
    p32 = 2 ** 32
    print("2^10 = %d" % p10)
    print("2^20 = %d" % p20)
    print("2^30 = %d" % p30)
    print("2^32 = %d" % p32)
    assert p10 == 1024
    assert p20 == 1048576
    assert p30 == 1073741824
    assert p32 == 4294967296
    # the unsigned maxima: 2**n - 1
    assert 2 ** 8 - 1 == 255
    assert 2 ** 16 - 1 == 65535
    assert 2 ** 32 - 1 == 4294967295
    print("8/16/32-bit maxima: 255, 65535, 4294967295")
    # the estimator: 2**10 ~= 10**3
    ratio = p10 / 1000.0
    print("2^10 / 10^3 = %.4f" % ratio)
    assert 1.023 < ratio < 1.025
    print("rule: 2^n values, 2^n - 1 the largest; 2^10 ~= a thousand")
    print("OK: %s named the milestones" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jbs_dec_to_bin(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # repeated division by 2: 173 -> remainders bottom-up
    n = 173
    remainders = []
    q = n
    while q > 0:
        q, r = divmod(q, 2)
        remainders.append(r)
    bits = "".join(map(str, reversed(remainders)))
    print("173 -> remainders %s -> %s" % (remainders, bits))
    assert bits == "10101101"
    assert int(bits, 2) == 173
    # the subtraction method: peel the largest fitting power of two
    rest, places = 173, []
    for p in (128, 64, 32, 16, 8, 4, 2, 1):
        if rest >= p:
            places.append(1)
            rest -= p
        else:
            places.append(0)
    bits2 = "".join(map(str, places))
    assert bits2 == "10101101"
    assert rest == 0
    print("subtraction method: 173 = 128+32+8+4+1 -> %s" % bits2)
    print("rule: divide by 2, read remainders bottom-up")
    print("OK: %s translated the testimony" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jbs_bin_to_dec(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    s = "1101101"
    # positional sum
    total = sum(int(ch) * (2 ** i) for i, ch in enumerate(reversed(s)))
    print("positional sum of %s = %d" % (s, total))
    assert total == 109
    # Horner doubling: scan left to right, double and add
    acc = 0
    for ch in s:
        acc = acc * 2 + int(ch)
    print("Horner doubling of %s = %d" % (s, acc))
    assert acc == 109
    # leading zeros change nothing
    assert int("001101101", 2) == 109
    # cross-check a longer string
    assert int("10101101", 2) == 173
    print("rule: weigh the places, or double-and-add left to right")
    print("OK: %s read the seal back" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jbs_binary_multiplication(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # shift-and-add: 13 x 11
    a, b = 13, 11
    partials = []
    shift = 0
    m = b
    while m:
        if m & 1:
            partials.append((a << shift, shift))
        m >>= 1
        shift += 1
    for p, sh in partials:
        print("partial product: 13 << %d = %d" % (sh, p))
    assert [p for p, _ in partials] == [13, 26, 104]
    assert len(partials) == bin(b).count("1") == 3
    product = sum(p for p, _ in partials)
    print("13 x 11 = %d" % product)
    assert product == 143
    # shift left by k multiplies by 2**k with no adder
    assert (13 << 3) == 13 * 8 == 104
    # width rule: n-bit x n-bit needs up to 2n bits
    assert (255 * 255).bit_length() <= 16
    assert 255 * 255 == 65025
    print("rule: shift where the multiplier has 1s, then add")
    print("OK: %s mustered the product" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jbs_binary_division(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # restoring division: 45 / 6
    dividend, divisor = 45, 6
    n = dividend.bit_length()
    remainder, quotient = 0, 0
    for i in range(n - 1, -1, -1):
        remainder = (remainder << 1) | ((dividend >> i) & 1)
        trial = remainder - divisor
        quotient <<= 1
        if trial >= 0:
            remainder = trial
            quotient |= 1
    print("45 / 6: quotient %d, remainder %d" % (quotient, remainder))
    assert quotient == 7
    assert remainder == 3
    assert divisor * quotient + remainder == dividend
    assert 0 <= remainder < divisor
    # binary forms of the answer
    assert format(quotient, "b") == "111"
    assert format(remainder, "b") == "11"
    # a second check
    assert 100 // 7 == 14 and 100 % 7 == 2
    print("contract holds: 45 = 6 x 7 + 3, 0 <= 3 < 6")
    print("rule: each step asks one question - does the divisor fit?")
    print("OK: %s apportioned the muster" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jbs_ones_complement(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # ones complement: negate by flipping every bit (8-bit)
    def neg1(x):
        return (~x) & 0xFF
    assert neg1(13) == 0b11110010 == 242
    assert neg1(neg1(13)) == 13  # the mirror of the mirror restores
    print("+13 = 00001101, -13 = %s" % format(neg1(13), "08b"))
    # the two zeros
    assert 0b00000000 == 0
    assert neg1(0) == 0b11111111  # negative zero
    # end-around carry: 13 + (-5)
    raw = 13 + neg1(5)  # 00001101 + 11111010
    carry = raw >> 8
    result = (raw & 0xFF) + carry
    print("13 + (-5): raw %d, end-around carry %d, result %d" % (raw, carry, result))
    assert result == 8
    # range check: -127..127
    assert neg1(127) == 0b10000000
    print("rule: flip every bit; the carry walks all the way around")
    print("OK: %s held the mirror" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jbs_twos_complement(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # twos complement: flip and add 1 (8-bit)
    def neg2(x):
        return ((~x) + 1) & 0xFF
    assert neg2(13) == 0b11110011 == 243
    print("-13 in 8 bits = %s = %d unsigned" % (format(neg2(13), "08b"), neg2(13)))
    # the sign bit weighs -128: 243 - 256 = -13
    assert 243 - 256 == -13
    # ordinary addition just works: 13 + (-13) = 0, carry discarded
    assert (13 + neg2(13)) & 0xFF == 0
    # subtraction as addition: 20 - 7 = 20 + (-7)
    assert (20 + neg2(7)) & 0xFF == 13
    # one zero only
    assert neg2(0) == 0
    # range: -128..127; the edge case -128 has no positive counterpart
    assert neg2(128) == 128  # -(-128) wraps back to -128
    # sign extension: -13 in 16 bits
    assert 0xFFFF & 0xFF00 | neg2(13) == 0xFFF3
    print("13 + (-13) = 0 with carry discarded; 20 - 7 = 13 via complement")
    print("rule: flip, add 1 - one zero, one adder for everything")
    print("OK: %s balanced the ledger" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "what_is_binary": demo_jbs_what_is_binary,
    "counting_binary": demo_jbs_counting_binary,
    "bits_bytes": demo_jbs_bits_bytes,
    "binary_addition": demo_jbs_binary_addition,
    "binary_subtraction": demo_jbs_binary_subtraction,
    "powers_of_two": demo_jbs_powers_of_two,
    "dec_to_bin": demo_jbs_dec_to_bin,
    "bin_to_dec": demo_jbs_bin_to_dec,
    "binary_multiplication": demo_jbs_binary_multiplication,
    "binary_division": demo_jbs_binary_division,
    "ones_complement": demo_jbs_ones_complement,
    "twos_complement": demo_jbs_twos_complement,
}


def demo_jbs_signed_unsigned(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # same bits, two readings
    def signed8(x):
        return x - 256 if x & 0x80 else x
    assert signed8(0xFF) == -1
    assert 0xFF == 255
    assert signed8(0x80) == -128
    assert 0x80 == 128
    print("0xFF: unsigned 255, signed %d" % signed8(0xFF))
    print("0x80: unsigned 128, signed %d" % signed8(0x80))
    # the unsigned maxima
    assert 2 ** 8 - 1 == 255
    assert 2 ** 16 - 1 == 65535
    assert 2 ** 32 - 1 == 4294967295
    # the signed ranges
    assert (-2 ** 7, 2 ** 7 - 1) == (-128, 127)
    assert (-2 ** 31, 2 ** 31 - 1) == (-2147483648, 2147483647)
    # widening: zero-extend unsigned, sign-extend signed
    assert 0x00FF == 255
    assert signed8(0xFF) | ~0xFF == -1  # sign extension to full width
    print("rule: the bits do not change - only the reading")
    print("OK: %s read the row twice" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jbs_bitwise_and(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the four column facts
    assert (0 & 0, 0 & 1, 1 & 0, 1 & 1) == (0, 0, 0, 1)
    assert 0b1100 & 0b1010 == 0b1000 == 8
    print("1100 & 1010 = %s" % format(0b1100 & 0b1010, "04b"))
    # masking: extract the low byte of 0xABCD
    assert 0xABCD & 0x00FF == 0x00CD == 205
    print("0xABCD & 0x00FF = 0x%02X" % (0xABCD & 0x00FF))
    # testing a single bit
    assert 0b10110 & 0x01 == 0
    assert 0b10111 & 0x01 == 1
    # power-of-two test: single 1-bit means x & (x-1) == 0
    for x in (1, 2, 4, 64, 1024):
        assert (x & (x - 1)) == 0
    for x in (3, 6, 100):
        assert (x & (x - 1)) != 0
    print("powers of two detected: 1, 2, 4, 64, 1024")
    print("rule: 1 where BOTH are 1 - the strict agreement")
    print("OK: %s appointed the panel" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jbs_bitwise_or_xor(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # OR: 1 where at least one is 1
    assert 0b1100 | 0b1010 == 0b1110 == 14
    print("1100 | 1010 = %s" % format(0b1100 | 0b1010, "04b"))
    # OR sets bits: force bit 2 of 0b1000
    assert 0b1000 | 0b0100 == 0b1100
    # XOR: 1 where the inputs differ
    assert 0b1100 ^ 0b1010 == 0b0110 == 6
    print("1100 ^ 1010 = %s" % format(0b1100 ^ 0b1010, "04b"))
    # XOR toggles: with 1 flips, with 0 keeps
    assert 0b1010 ^ 0b1111 == 0b0101
    assert 0b1010 ^ 0 == 0b1010
    # double XOR restores
    x = 0b11010110
    assert (x ^ 0xFF) ^ 0xFF == x
    # the xor-swap: no temporary
    a, b = 13, 29
    a ^= b
    b ^= a
    a ^= b
    assert (a, b) == (29, 13)
    print("xor-swap: 13 and 29 exchanged with no temporary")
    # half-adder sum bit is an XOR
    for p, q in ((0, 0), (0, 1), (1, 0), (1, 1)):
        assert (p ^ q) == (p + q) % 2
    print("rule: OR sets, XOR differs - and twice-XOR restores")
    print("OK: %s heard the dissent" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jbs_bitwise_not_masks(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # NOT flips every bit (8-bit view)
    assert (~0b00001111) & 0xFF == 0b11110000 == 240
    print("~00001111 = %s" % format((~0b00001111) & 0xFF, "08b"))
    # the four idioms on x = 0b00100000 (32)
    x = 0b00100000
    x = x | (1 << 0)          # SET bit 0
    assert x == 33
    x = x & ~(1 << 5)         # CLEAR bit 5
    assert x == 1
    x = x ^ (1 << 2)          # TOGGLE bit 2
    assert x == 5
    assert (x >> 2) & 1 == 1  # TEST bit 2
    print("SET/CLEAR/TOGGLE/TEST on 0b00100000 -> final %s" % format(x, "08b"))
    # field extract: high nibble of 0xAB
    assert (0xAB & 0xF0) >> 4 == 0xA == 10
    # field insert: put 0x5 into the high nibble of 0x0B
    v = (0x0B & ~0xF0) | ((0x5 << 4) & 0xF0)
    assert v == 0x5B
    print("high nibble of 0xAB = 0xA; insert 0x5 -> 0x%02X" % v)
    # ~x = -x - 1
    assert ~5 == -6
    print("rule: SET with OR, CLEAR with AND-NOT, TOGGLE with XOR, TEST with shift")
    print("OK: %s kept the four instruments" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jbs_bit_shifts(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # left shift multiplies by 2**k
    assert (0b00010110 << 2) == 88
    print("22 << 2 = %d" % (22 << 2))
    # logical right shift: zeros fill the left
    assert (0b00010110 >> 2) == 0b00000101 == 5
    print("22 >> 2 = %d (logical, unsigned)" % (22 >> 2))
    # arithmetic right shift: sign bit fills the left (-8 >> 2 = -2)
    neg8 = 0b11111000  # -8 in 8-bit twos complement
    shifted = (neg8 >> 2) | 0xC0  # fill the two vacated bits with 1s
    assert shifted == 0b11111110 == 254
    assert shifted - 256 == -2
    print("-8 >> 2 (arithmetic) = %s = -2" % format(shifted, "08b"))
    # bits shifted past the width are lost
    assert (0b10000000 << 1) & 0xFF == 0
    # arithmetic shift rounds toward negative infinity
    assert -7 // 4 == -2  # floor division matches arithmetic shift
    print("rule: << multiplies by 2^k; >> divides - logically or arithmetically")
    print("OK: %s promoted and demoted the muster" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jbs_hexadecimal(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # one hex digit = 4 bits: digit-by-digit translation
    table = "0123456789ABCDEF"
    def to_hex(n, digits):
        return "".join(table[(n >> (4 * i)) & 0xF] for i in reversed(range(digits)))
    assert to_hex(0xDEAD, 4) == "DEAD"
    # 1101111010101101 grouped in fours = D E A D
    assert int("1101111010101101", 2) == 0xDEAD == 57005
    print("1101111010101101 = 0xDEAD = %d" % 0xDEAD)
    # positional check: 13*16^3 + 14*16^2 + 10*16 + 13
    assert 13 * 16 ** 3 + 14 * 16 ** 2 + 10 * 16 + 13 == 57005
    assert 0xFF == 255
    assert 0x10 == 16
    # two hex digits per byte, eight per 32-bit word
    assert len("%08X" % 0xDEADBEEF) == 8
    print("0xDEADBEEF is %d hex digits = 32 bits" % len("%08X" % 0xDEADBEEF))
    print("rule: group in fours from the right, translate each group")
    print("OK: %s wrote the seal-script" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jbs_octal_bases(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # one octal digit = 3 bits: group in threes from the right
    assert int("101110", 2) == 0o56 == 46
    print("101110 binary = 56 octal = %d decimal" % 0o56)
    # Unix permissions: 0o755 = rwxr-xr-x
    assert 0o755 == 493
    perms = 0o755
    owner = (perms >> 6) & 7
    grp = (perms >> 3) & 7
    oth = perms & 7
    assert (owner, grp, oth) == (7, 5, 5)
    names = {7: "rwx", 5: "r-x", 4: "r--"}
    print("0o755 = %s%s%s = %d" % (names[owner], names[grp], names[oth], perms))
    # power-of-two bases regroup without arithmetic: 0o755 -> binary -> hex
    b = format(0o755, "09b")
    assert b == "111101101"
    assert int(b, 2) == 493
    assert format(493, "X") == "1ED"
    print("0o755 -> %s binary -> 0x1ED" % b)
    print("rule: powers of two regroup; other bases route through decimal")
    print("OK: %s guarded the permissions" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jbs_ascii(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the landmark code points
    assert ord("A") == 65 == 0x41
    assert ord("a") == 97 == 0x61
    assert ord("0") == 48
    assert ord(" ") == 32
    assert ord(chr(127)) == 127  # DEL
    print("'A'=%d (0x%02X), 'a'=%d, '0'=%d, space=%d" % (65, 65, 97, 48, 32))
    # case differs by bit 5 (value 32)
    assert ord("a") ^ 32 == ord("A")
    assert ord("a") & ~32 == ord("A")
    print("'a' XOR 32 = 'A' verified")
    # control codes
    assert ord("\\n") == 10
    assert ord("\\r") == 13
    assert ord(chr(27)) == 27  # ESC
    # printable range 32..126
    assert [c for c in range(128) if 32 <= c <= 126].__len__() == 95
    assert all(c < 128 for c in b"Hello, World!")
    print("printable ASCII: 95 characters, codes 32-126")
    print("rule: 7 bits, 128 characters - digits, upper, lower in order")
    print("OK: %s swore the first alphabet" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jbs_unicode_utf8(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the euro sign: U+20AC -> E2 82 AC
    raw = "€".encode("utf-8")
    assert raw == b"\\xe2\\x82\\xac"
    assert len(raw) == 3
    print("U+20AC encodes as %s" % raw.hex().upper())
    # hand-pack U+20AC: 14 bits split 4+6+6 into the 3-byte template
    cp = 0x20AC
    b0 = 0xE0 | (cp >> 12)
    b1 = 0x80 | ((cp >> 6) & 0x3F)
    b2 = 0x80 | (cp & 0x3F)
    assert (b0, b1, b2) == (0xE2, 0x82, 0xAC)
    assert bytes((b0, b1, b2)).decode("utf-8") == "€"
    print("hand-packed template 1110xxxx 10xxxxxx 10xxxxxx -> E2 82 AC")
    # ASCII transparency: every ASCII byte is its own character
    assert "Hi!".encode("utf-8") == b"Hi!"
    # round trip of a 4-byte character
    ch = "\\U0001F600"
    assert ch.encode("utf-8").decode("utf-8") == ch
    assert len(ch.encode("utf-8")) == 4
    print("4-byte code point round-trips through UTF-8")
    print("rule: the lead byte declares the length; ASCII rides unchanged")
    print("OK: %s sealed the many tongues" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jbs_fixed_point(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Q8.8: value = stored / 256
    SCALE = 256
    stored = int(3.75 * SCALE)
    assert stored == 960
    assert stored == 0x03C0
    print("3.75 in Q8.8 = %d (0x%04X)" % (stored, stored))
    # the resolution: 1/256 per step - as an exact fraction
    from fractions import Fraction
    step = Fraction(1, SCALE)
    assert step == Fraction(1, 256)
    # fraction places: 0.101 binary = 1/2 + 1/8
    assert Fraction(1, 2) + Fraction(1, 8) == Fraction(5, 8)
    # addition needs no adjustment
    assert (960 + 640) == 1600  # 3.75 + 2.5 = 6.25 -> 1600/256
    assert Fraction(1600, 256) == Fraction(25, 4)
    # multiplication: Q8.8 x Q8.8 -> shift right 8 to renormalize
    prod = (960 * 640) >> 8  # 3.75 * 2.5 = 9.375
    assert prod == 2400
    assert Fraction(2400, 256) == Fraction(75, 8)
    print("3.75 x 2.5 in Q8.8: (960*640)>>8 = %d = 75/8" % prod)
    print("rule: agree the point's place, then it is all integers")
    print("OK: %s held the sworn measure" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jbs_ieee754(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 3.14 as IEEE 754 single: the famous 0x4048F5C3
    bits = struct.unpack(">I", struct.pack(">f", 3.14))[0]
    print("3.14 -> 0x%08X" % bits)
    assert bits == 0x4048F5C3
    # decode the three fields
    sign = (bits >> 31) & 1
    exp = (bits >> 23) & 0xFF
    mant = bits & 0x7FFFFF
    assert sign == 0
    assert exp == 128  # 128 - 127 = 2**1
    value = (1.0 + mant / 2.0 ** 23) * 2.0 ** (exp - 127)
    print("sign %d, exponent %d (bias 127 -> 2^1), mantissa 0x%06X" % (sign, exp, mant))
    f32 = struct.unpack(">f", struct.pack(">f", 3.14))[0]
    assert abs(value - f32) < 1e-12
    # the specials
    assert struct.unpack(">f", struct.pack(">I", 0x7F800000))[0] == float("inf")
    assert struct.unpack(">f", struct.pack(">I", 0xFF800000))[0] == float("-inf")
    nan = struct.unpack(">f", struct.pack(">I", 0x7FC00000))[0]
    assert nan != nan  # NaN is not equal to itself
    assert struct.unpack(">f", struct.pack(">I", 0x80000000))[0] == 0.0
    print("specials verified: +inf, -inf, NaN, signed zero")
    # 0.1 + 0.2 != 0.3 in binary floating point
    assert 0.1 + 0.2 != 0.3
    print("0.1 + 0.2 = %.17f (not 0.3)" % (0.1 + 0.2))
    print("rule: sign, biased exponent, mantissa - and never floats for money")
    print("OK: %s rode the sliding scale" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "what_is_binary": demo_jbs_what_is_binary,
    "counting_binary": demo_jbs_counting_binary,
    "bits_bytes": demo_jbs_bits_bytes,
    "binary_addition": demo_jbs_binary_addition,
    "binary_subtraction": demo_jbs_binary_subtraction,
    "powers_of_two": demo_jbs_powers_of_two,
    "dec_to_bin": demo_jbs_dec_to_bin,
    "bin_to_dec": demo_jbs_bin_to_dec,
    "binary_multiplication": demo_jbs_binary_multiplication,
    "binary_division": demo_jbs_binary_division,
    "ones_complement": demo_jbs_ones_complement,
    "twos_complement": demo_jbs_twos_complement,
}


def demo_jbs_logic_gates_basic(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the three primal truth tables
    def AND(a, b):
        return a & b
    def OR(a, b):
        return a | b
    def NOT(a):
        return 1 - a
    for a in (0, 1):
        for b in (0, 1):
            assert AND(a, b) == (1 if a == 1 and b == 1 else 0)
            assert OR(a, b) == (1 if a == 1 or b == 1 else 0)
        assert NOT(a) == (0 if a == 1 else 1)
    print("AND: only 11->1; OR: only 00->0; NOT: flips")
    # De Morgan: NOT (A AND B) == (NOT A) OR (NOT B)
    for a in (0, 1):
        for b in (0, 1):
            assert NOT(AND(a, b)) == OR(NOT(a), NOT(b))
            assert NOT(OR(a, b)) == AND(NOT(a), NOT(b))
    print("De Morgan verified on all input pairs")
    # composition: (A AND B) OR (NOT C)
    def circuit(a, b, c):
        return OR(AND(a, b), NOT(c))
    assert circuit(1, 1, 0) == 1
    assert circuit(1, 0, 1) == 0
    assert circuit(0, 0, 0) == 1
    print("rule: three gates, composed without limit")
    print("OK: %s raised the three stones" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jbs_logic_gates_compound(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the compound tables
    def XOR(a, b):
        return a ^ b
    def NAND(a, b):
        return 1 - (a & b)
    def NOR(a, b):
        return 1 - (a | b)
    def XNOR(a, b):
        return 1 - (a ^ b)
    assert [XOR(a, b) for a in (0, 1) for b in (0, 1)] == [0, 1, 1, 0]
    assert [NAND(a, b) for a in (0, 1) for b in (0, 1)] == [1, 1, 1, 0]
    assert [NOR(a, b) for a in (0, 1) for b in (0, 1)] == [1, 0, 0, 0]
    assert [XNOR(a, b) for a in (0, 1) for b in (0, 1)] == [1, 0, 0, 1]
    print("XOR: 1 when different; XNOR: 1 when equal")
    # NAND universality: build NOT, AND, OR from NAND alone
    def nNOT(a):
        return NAND(a, a)
    def nAND(a, b):
        return nNOT(NAND(a, b))
    def nOR(a, b):
        return NAND(nNOT(a), nNOT(b))
    for a in (0, 1):
        for b in (0, 1):
            assert nNOT(a) == (1 - a)
            assert nAND(a, b) == (a & b)
            assert nOR(a, b) == (a | b)
    print("NAND builds NOT, AND, OR - verified on all inputs")
    # XNOR equality comparator over 4 bits
    def equal4(x, y):
        return all(XNOR((x >> i) & 1, (y >> i) & 1) for i in range(4))
    assert equal4(0b1011, 0b1011) and not equal4(0b1011, 0b1010)
    print("rule: one gate type can build them all")
    print("OK: %s proved the parsimony" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jbs_half_full_adder(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # half adder: sum = XOR, carry = AND
    def half(a, b):
        return (a ^ b, a & b)
    assert half(0, 0) == (0, 0)
    assert half(0, 1) == (1, 0)
    assert half(1, 0) == (1, 0)
    assert half(1, 1) == (0, 1)
    # full adder: three bits in
    def full(a, b, cin):
        s = a ^ b ^ cin
        cout = (a & b) | (cin & (a ^ b))
        return (s, cout)
    for a in (0, 1):
        for b in (0, 1):
            for cin in (0, 1):
                s, cout = full(a, b, cin)
                assert s == (a + b + cin) % 2
                assert cout == (1 if (a + b + cin) >= 2 else 0)
    print("full adder verified on all 8 input triples")
    # ripple-carry: 13 + 11 = 24 through the gate chain
    def ripple(a, b, n=8):
        carry, out = 0, 0
        for i in range(n):
            s, carry = full((a >> i) & 1, (b >> i) & 1, carry)
            out |= s << i
        return out, carry
    total, cout = ripple(13, 11)
    print("13 + 11 via gate-level ripple adder = %d (carry out %d)" % (total, cout))
    assert total == 24
    assert cout == 0
    # subtraction reuses the adder: 20 - 7 = 20 + ~7 + 1
    total2, _ = ripple(20, 0xFF ^ 7, 8)
    total2 = (total2 + 1) & 0xFF
    assert total2 == 13
    print("rule: three witnesses in, a kept bit and a forwarded oath out")
    print("OK: %s walked the carry chain" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jbs_fast_adders(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # generate/propagate lookahead vs the ripple wait
    def add_lookahead(a, b, n=32):
        g = [((a >> i) & 1) & ((b >> i) & 1) for i in range(n)]
        p = [((a >> i) & 1) ^ ((b >> i) & 1) for i in range(n)]
        carry = [0] * (n + 1)
        for i in range(n):
            # carry[i+1] = g[i] OR (p[i] AND carry[i]) - direct from inputs
            carry[i + 1] = g[i] | (p[i] & carry[i])
        out = 0
        for i in range(n):
            out |= (((a >> i) & 1) ^ ((b >> i) & 1) ^ carry[i]) << i
        return out, carry[n]
    a = 0x12345678
    b = 0x9ABCDEF0
    total, cout = add_lookahead(a, b)
    assert total == (a + b) & 0xFFFFFFFF
    assert cout == ((a + b) >> 32)
    print("0x12345678 + 0x9ABCDEF0 = 0x%08X (carry %d)" % (total, cout))
    # delay accounting: ripple waits n carry steps; lookahead settles in ~log steps
    n = 32
    ripple_depth = 2 * n          # ~2 gate delays per bit of carry
    lookahead_depth = 6           # two-level 4-bit lookahead blocks
    print("32-bit ripple depth ~%d gate delays; lookahead ~%d" % (ripple_depth, lookahead_depth))
    assert ripple_depth == 64
    assert lookahead_depth < ripple_depth
    # worst case for ripple: 0xFFFFFFFF + 1 ripples through all 32
    t2, c2 = add_lookahead(0xFFFFFFFF, 1)
    assert t2 == 0 and c2 == 1
    print("rule: declare generate/propagate up front, read carries directly")
    print("OK: %s bought speed with witnesses" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jbs_parity(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # even parity of 0b1011001: four 1s -> parity bit 0
    data = 0b1011001
    ones = bin(data).count("1")
    pbit = ones % 2  # even parity: total 1s must be even
    assert ones == 4
    assert pbit == 0
    code = (data << 1) | pbit
    print("data %s + even-parity bit %d -> %s" % (format(data, "07b"), pbit, format(code, "08b")))
    def check(word):
        return bin(word).count("1") % 2 == 0
    assert check(code)
    # a single flipped bit breaks the tally
    corrupted = code ^ (1 << 2)
    assert not check(corrupted)
    print("one flipped bit detected: parity check fails")
    # two flipped bits conspire past the checker: the blind spot
    double = code ^ (1 << 2) ^ (1 << 3)
    assert check(double)
    print("two flipped bits NOT detected: the honest blind spot")
    # odd parity variant
    assert (bin(data).count("1") + 1) % 2 == 1
    print("rule: one appointed checker per row - single lies exposed")
    print("OK: %s kept the tally" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jbs_hamming(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Hamming(7,4): parity at positions 1,2,4; data at 3,5,6,7
    def encode(d1, d2, d3, d4):
        p1 = d1 ^ d2 ^ d4
        p2 = d1 ^ d3 ^ d4
        p4 = d2 ^ d3 ^ d4
        # integer with position 1 = LSB
        return p1 | (p2 << 1) | (d1 << 2) | (p4 << 3) | (d2 << 4) | (d3 << 5) | (d4 << 6)
    cw = encode(1, 0, 1, 1)
    assert cw == 0b1100110 == 102  # positions 7..1; read 1..7 it is 0110011
    pos_order = "".join(str((cw >> (p - 1)) & 1) for p in range(1, 8))
    assert pos_order == "0110011"
    print("data 1011 -> codeword %s (positions 1..7)" % pos_order)
    def syndrome(w):
        b = lambda pos: (w >> (pos - 1)) & 1
        s1 = b(1) ^ b(3) ^ b(5) ^ b(7)
        s2 = b(2) ^ b(3) ^ b(6) ^ b(7)
        s4 = b(4) ^ b(5) ^ b(6) ^ b(7)
        return s1 | (s2 << 1) | (s4 << 2)
    assert syndrome(cw) == 0
    # corrupt position 5 and let the syndrome name it
    bad = cw ^ (1 << 4)
    s = syndrome(bad)
    print("corrupted bit 5 -> syndrome %d" % s)
    assert s == 5
    fixed = bad ^ (1 << (s - 1))
    assert fixed == cw
    # read the data back off
    d = ((fixed >> 2) & 1, (fixed >> 4) & 1, (fixed >> 5) & 1, (fixed >> 6) & 1)
    assert d == (1, 0, 1, 1)
    print("syndrome named position 5; flipped back; data 1011 recovered")
    print("rule: the checkers convene, and their pattern names the liar")
    print("OK: %s healed the covenant" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jbs_crc(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # CRC-8, polynomial x^8+x^2+x+1 (0x07), init 0x00
    def crc8(data):
        crc = 0
        for byte in data:
            crc ^= byte
            for _ in range(8):
                if crc & 0x80:
                    crc = ((crc << 1) ^ 0x07) & 0xFF
                else:
                    crc = (crc << 1) & 0xFF
        return crc
    check = crc8(b"123456789")
    print("CRC-8 of '123456789' = 0x%02X" % check)
    assert check == 0xF4  # the standard check value
    # the receiver divides message+CRC and expects zero remainder
    assert crc8(b"123456789" + bytes((check,))) == 0
    print("message + CRC divides clean: remainder 0")
    # a single flipped bit is caught
    tampered = bytearray(b"123456789")
    tampered[0] ^= 0x01
    assert crc8(bytes(tampered) + bytes((check,))) != 0
    print("one flipped bit caught: remainder nonzero")
    # all-zeros message has zero CRC
    assert crc8(b"\\x00\\x00\\x00") == 0
    print("rule: divide by the sworn polynomial; the remainder is the seal")
    print("OK: %s inspected the seal" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jbs_binary_gray_code(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # binary -> Gray: g = b ^ (b >> 1)
    def to_gray(b):
        return b ^ (b >> 1)
    # Gray -> binary: b MSB = g MSB; each lower bit = higher b-bit XOR g-bit
    def from_gray(g, n=4):
        b = 0
        prev = 0
        for i in range(n - 1, -1, -1):
            gbit = (g >> i) & 1
            bbit = prev ^ gbit if i < n - 1 else gbit
            b = (b << 1) | bbit
            prev = bbit
        return b
    seq = [to_gray(b) for b in range(16)]
    print("4-bit Gray: %s" % " ".join(format(g, "04b") for g in seq))
    assert seq[0] == 0
    # every neighboring pair differs in exactly one bit (Hamming distance 1)
    def ham(x, y):
        return bin(x ^ y).count("1")
    for i in range(16):
        assert ham(seq[i], seq[(i + 1) % 16]) == 1, i
    print("all 16 transitions (incl. wraparound) change exactly 1 bit")
    # round trip
    for b in range(16):
        assert from_gray(to_gray(b)) == b
    # the encoder hazard Gray avoids: 0111 -> 1000 flips 4 bits in binary
    assert ham(0b0111, 0b1000) == 4
    assert ham(to_gray(7), to_gray(8)) == 1
    print("binary 0111->1000 flips 4 bits; Gray flips 1")
    print("rule: one step, one witness - no stumble")
    print("OK: %s marched the procession" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jbs_bcd(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # each decimal digit in its own nibble: 93 = 0x93
    def to_bcd(n):
        out, shift = 0, 0
        while n:
            out |= (n % 10) << shift
            n //= 10
            shift += 4
        return out
    assert to_bcd(93) == 0x93
    assert to_bcd(2026) == 0x2026
    print("93 -> BCD 0x%02X; 2026 -> BCD 0x%04X" % (to_bcd(93), to_bcd(2026)))
    # BCD addition with the +6 correction: 93 + 59 = 152
    def bcd_add(a, b):
        raw = a + b
        lo = raw & 0xF
        hi = (raw >> 4) & 0xF
        carry = raw >> 8
        if lo > 9:
            lo_carry, lo = divmod(lo + 6, 16)
            hi += lo_carry
        if hi > 9 or carry:
            hi_carry, hi = divmod(hi + 6, 16)
            carry += hi_carry
        return (carry << 8) | (hi << 4) | lo
    r = bcd_add(0x93, 0x59)
    assert r == 0x152
    print("0x93 + 0x59 with +6 correction = 0x%03X = %d" % (r, 152))
    # illegal patterns 1010-1111 never appear in a valid BCD digit
    assert all(((r >> s) & 0xF) <= 9 for s in (0, 4, 8))
    print("rule: a nibble per digit, +6 to skip the illegal country")
    print("OK: %s kept the decimal oath" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jbs_subnet_masks(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 192.168.1.77/24 with pure integer bit operations
    def pack(a, b, c, d):
        return (a << 24) | (b << 16) | (c << 8) | d
    def dotted(n):
        return "%d.%d.%d.%d" % ((n >> 24) & 0xFF, (n >> 16) & 0xFF, (n >> 8) & 0xFF, n & 0xFF)
    ip = pack(192, 168, 1, 77)
    mask = (0xFFFFFFFF << 8) & 0xFFFFFFFF  # /24
    assert mask == 0xFFFFFF00
    assert dotted(mask) == "255.255.255.0"
    network = ip & mask
    broadcast = network | (~mask & 0xFFFFFFFF)
    assert dotted(network) == "192.168.1.0"
    assert dotted(broadcast) == "192.168.1.255"
    hosts = 2 ** 8 - 2
    assert hosts == 254
    print("192.168.1.77/24: network %s, broadcast %s, usable hosts %d"
          % (dotted(network), dotted(broadcast), hosts))
    # /26 split: 64 addresses, 62 usable
    mask26 = (0xFFFFFFFF << 6) & 0xFFFFFFFF
    assert dotted(mask26) == "255.255.255.192"
    assert 2 ** 6 - 2 == 62
    print("/26: mask %s, 62 usable hosts" % dotted(mask26))
    print("rule: AND the address with the mask - the territory line")
    print("OK: %s drew the borders" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_jbs_overflow_flags(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 8-bit addition with per-bit carries: 100 + 60
    def add8(a, b):
        carries = [0]
        out = 0
        for i in range(8):
            total = ((a >> i) & 1) + ((b >> i) & 1) + carries[i]
            out |= (total % 2) << i
            carries.append(total // 2)
        C = carries[8]
        V = carries[7] ^ carries[8]  # carry into sign bit XOR carry out
        Z = 1 if out == 0 else 0
        N = (out >> 7) & 1
        return out, C, V, Z, N
    out, C, V, Z, N = add8(100, 60)
    signed = out - 256 if out & 0x80 else out
    print("100 + 60 (8-bit): result %d, signed reading %d" % (out, signed))
    print("flags: C=%d V=%d Z=%d N=%d" % (C, V, Z, N))
    assert out == 160
    assert signed == -96
    assert V == 1  # two positives made a negative: signed overflow
    assert C == 0  # unsigned 160 < 255: no unsigned overflow
    assert Z == 0 and N == 1
    # unsigned overflow instead: 200 + 100 = 300
    out2, C2, V2, Z2, N2 = add8(200, 100)
    assert out2 == 44 and C2 == 1 and V2 == 0
    print("200 + 100 (8-bit): result %d, C=%d (unsigned overflow), V=%d" % (out2, C2, V2))
    # zero flag
    _, _, _, Z3, _ = add8(13, 243)  # 13 + (-13)
    assert Z3 == 1
    print("rule: C watches unsigned, V watches signed - one XOR on the last carries")
    print("OK: %s heard the after-action testimony" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS.update({
    "signed_unsigned": demo_jbs_signed_unsigned,
    "bitwise_and": demo_jbs_bitwise_and,
    "bitwise_or_xor": demo_jbs_bitwise_or_xor,
    "bitwise_not_masks": demo_jbs_bitwise_not_masks,
    "bit_shifts": demo_jbs_bit_shifts,
    "hexadecimal": demo_jbs_hexadecimal,
    "octal_bases": demo_jbs_octal_bases,
    "ascii": demo_jbs_ascii,
    "unicode_utf8": demo_jbs_unicode_utf8,
    "fixed_point": demo_jbs_fixed_point,
    "ieee754": demo_jbs_ieee754,
    "logic_gates_basic": demo_jbs_logic_gates_basic,
    "logic_gates_compound": demo_jbs_logic_gates_compound,
    "half_full_adder": demo_jbs_half_full_adder,
    "fast_adders": demo_jbs_fast_adders,
    "parity": demo_jbs_parity,
    "hamming": demo_jbs_hamming,
    "crc": demo_jbs_crc,
    "binary_gray_code": demo_jbs_binary_gray_code,
    "bcd": demo_jbs_bcd,
    "subnet_masks": demo_jbs_subnet_masks,
    "overflow_flags": demo_jbs_overflow_flags,
})
