# -*- coding: utf-8 -*-
"""Topic module: db-codebreaker-challenge. Ciphers generated at load time so
every encoded message is guaranteed correct. Property of Justin Addam Higgins (JAH)."""
from w3lib import mkcfg, T


def caesar(s, shift):
    out = []
    for c in s:
        if "a" <= c <= "z":
            out.append(chr((ord(c) - 97 + shift) % 26 + 97))
        elif "A" <= c <= "Z":
            out.append(chr((ord(c) - 65 + shift) % 26 + 65))
        else:
            out.append(c)
    return "".join(out)


def atbash(s):
    out = []
    for c in s:
        if "a" <= c <= "z":
            out.append(chr(122 - (ord(c) - 97)))
        elif "A" <= c <= "Z":
            out.append(chr(90 - (ord(c) - 65)))
        else:
            out.append(c)
    return "".join(out)


def vigenere(s, key):
    key = key.upper()
    out, ki = [], 0
    for c in s:
        if c.isalpha():
            sh = ord(key[ki % len(key)]) - 65
            base = 65 if c.isupper() else 97
            out.append(chr((ord(c) - base + sh) % 26 + base))
            ki += 1
        else:
            out.append(c)
    return "".join(out)


def railfence(s, rails):
    if rails < 2:
        return s
    rows = [""] * rails
    r, d = 0, 1
    for c in s:
        rows[r] += c
        r += d
        if r == 0 or r == rails - 1:
            d = -d
    return "".join(rows)


def unrailfence(s, rails):
    if rails < 2:
        return s
    pat = []
    r, d = 0, 1
    for _ in s:
        pat.append(r)
        r += d
        if r == 0 or r == rails - 1:
            d = -d
    lens = [pat.count(i) for i in range(rails)]
    chunks, pos = [], 0
    for ln in lens:
        chunks.append(s[pos:pos + ln])
        pos += ln
    idx = [0] * rails
    out = []
    for p in pat:
        out.append(chunks[p][idx[p]])
        idx[p] += 1
    return "".join(out)


CFG = mkcfg({
    "slug": "db-codebreaker-challenge", "name": "The Codebreaker Challenge", "pfx": "JAH-CODCHA-",
    "tagline_pub": "Substitution ciphers, pattern recognition, and historical codebreaking - Caesar shifts, Atbash mirrors, Vigenere keys, and rail-fence zigzags: every record carrying an encoded message, the method, the decoded answer, and the full working of the cipher, taught progressively along the ladder.",
    "tagline_sig": "The Signature cipher school: every code a Signature lock, every key a Signature answer. The full ladder from Caesar shifts through Atbash mirrors and Vigenere keys to Signature-grade rail-fence zigzags. Clearly labeled Signature-made, never presented as authentic public record.",
    "ai": "Codebreaker Challenge",
    "role_pub": "codebreaker instructor - teaching ciphers by encoding real messages and proving every decode",
    "role_sig": "Signature codebreaker instructor - teaching the Signature cipher school",
    "record_kind": "codebreaker puzzle record", "record_kind_plural": "codebreaker puzzles",
    "demo_kind": "cipher-roundtrip", "demo_title": "Codebreaker Study",
    "search_ph": "Search Caesar, Atbash, Vigenere, rail fence, ciphers...",
    "chat_ph": "Ask about ciphers...",
    "gen_blurb": "Generate clearly-labeled cipher studies. Seeded archive records are the authoritative entries.",
    "about_archive": "Seeded cipher puzzles, every encode/decode machine-verified, marching toward one million records. Presented in teaching-ladder order: Caesar, mirrors, keyed ciphers, zigzags.",
    "reqs": "Paper, pencil, and patience. An alphabet strip helps for the first ciphers.",
    "stds": "Every encoded message is machine-generated from its plaintext at build time, and every demo decodes it back - zero hand-encoding errors.",
    "cites": ["JAH Databases cipher verification standard v1.0"],
})


def _cb(tier, title, method, plaintext, encoded, how_decode, note, decode_expr):
    return T(
        tier, title,
        desc_pub='CODEBREAKER CHALLENGE - %s:\n\nEncoded message: "%s"\nMethod: %s\n\nDECODED: "%s"\n\nHow the decode works: %s\n\n%s'
        % (title, encoded, method, plaintext, how_decode, note),
        desc_sig='Signature cipher school: this %s is a Signature lock, and the decode is the Signature key turning. The Signature edition treats every broken code as a small victory of patience over secrecy.' % method.split(",")[0],
        how_pub='Break it yourself: %s Then check against the decoded answer - and notice which step gave you the most trouble; that step is the skill.' % how_decode,
        how_sig='The Signature way: decode with a steady hand and a slow eye - ciphers surrender to patience, never to hurry.',
        keys=['Method: %s.' % method,
              'Encoded: "%s".' % encoded,
              'Decoded: "%s".' % plaintext,
              'Codebreaker note: %s' % note],
        demo=("compute", {"preamble": HELPERS,
                          "code": ["ENC = %r" % encoded, "DEC = %s" % decode_expr],
                          "show": ["ENC", "DEC"],
                          "asserts": [("roundtrip_ok", "DEC == %r" % plaintext)]}),
    )


def _caesar_rec(tier, shift, plaintext, note):
    enc = caesar(plaintext, shift)
    return _cb(tier, "Codebreaker: Caesar shift %d (%s)" % (shift, plaintext[:20].rstrip()),
               "Caesar cipher, shift %d (each letter moved %d forward)" % (shift, shift),
               plaintext, enc,
               "write the alphabet, then write it shifted %d places beneath; replace each encoded letter with the one above it" % shift,
               note, "caesar(ENC, %d)" % (26 - shift))


# local decode helpers injected into demo namespace via code strings
HELPERS = """
def caesar(s, shift):
    o = []
    for c in s:
        o.append(chr((ord(c) - (65 if c.isupper() else 97) + shift) % 26 + (65 if c.isupper() else 97)) if c.isalpha() else c)
    return "".join(o)
def atbash(s):
    o = []
    for c in s:
        o.append(chr((90 if c.isupper() else 122) - (ord(c) - (65 if c.isupper() else 97))) if c.isalpha() else c)
    return "".join(o)
def vigenere_dec(s, key):
    key = key.upper(); o = []; ki = 0
    for c in s:
        sh = ord(key[ki % len(key)]) - 65; base = 65 if c.isupper() else 97
        o.append(chr((ord(c) - base - sh) % 26 + base) if c.isalpha() else c)
        ki += c.isalpha()
    return "".join(o)
def unrailfence(s, rails):
    pat = []; r = 0; d = 1
    for _ in s:
        pat.append(r); r += d
        if r == 0 or r == rails - 1: d = -d
    lens = [pat.count(i) for i in range(rails)]
    chunks = []; pos = 0
    for ln in lens:
        chunks.append(s[pos:pos + ln]); pos += ln
    idx = [0] * rails; o = []
    for q in pat:
        o.append(chunks[q][idx[q]]); idx[q] += 1
    return "".join(o)
"""

B, C, A = "Foundations", "Compounded", "Advanced"
_caesar_data = [
    (B, 3, "THE EAGLE HAS LANDED", "Shift 3 is the classic Caesar used by Julius himself - history's first famous cipher."),
    (B, 3, "MEET AT DAWN", "Short and sweet: three words, one shift, pure codebreaker calisthenics."),
    (B, 5, "ATTACK AT SUNRISE", "Shift 5 toughens the workout - the alphabet strip earns its keep."),
    (B, 1, "HELLO WORLD", "Shift 1 is the gentle on-ramp: every letter just slides one step."),
    (B, 7, "THE QUICK BROWN FOX", "The pangram goes undercover - every letter of the alphabet, shifted."),
    (B, 3, "SECRETS HIDE IN PLAIN SIGHT", "A motto for the whole database, encoded in the cipher that started it all."),
    (B, 10, "CODEBREAKERS NEVER QUIT", "Shift 10: double digits, double determination."),
    (B, 13, "ROT THIRTEEN HIDES NOTHING", "ROT13 - the internet's favorite almost-cipher, hiding in plain sight."),
    (B, 4, "PATIENCE BREAKS CODES", "The truest sentence in cryptography, shifted four."),
    (B, 8, "EVERY LETTER COUNTS", "Shift 8 on a five-word truth."),
    (B, 2, "SMALL STEPS WIN", "Shift 2: barely a disguise, perfect for beginners."),
    (C, 19, "THE LONG WAY ROUND", "Shift 19 is shift -7 in disguise - codebreakers learn to see both."),
    (C, 23, "ALMOST HOME FREE", "Shift 23 is shift -3 wearing a mask."),
]
TOPICS = []
for _t, _sh, _pt, _nt in _caesar_data:
    TOPICS.append(_caesar_rec(_t, _sh, _pt, _nt))

_atbash_data = [
    (C, "THE MIRROR CODE", "Atbash: A becomes Z, B becomes Y - the alphabet folded in half. Decode by folding it back."),
    (C, "BACKWARDS ALPHABET", "Atbash is its own inverse: encode twice and you are home - the demo proves it."),
    (C, "ANCIENT AND ELEGANT", "Atbash is thousands of years old and still stops casual snoopers cold."),
]
for _t, _pt, _nt in _atbash_data:
    _enc = atbash(_pt)
    TOPICS.append(_cb(_t, "Codebreaker: Atbash mirror (%s)" % _pt[:20].rstrip(), "Atbash cipher (alphabet reversed: A<->Z, B<->Y, ...)", _pt, _enc,
                      "replace each letter with its mirror twin: A<->Z, B<->Y, C<->X, all the way to the middle",
                      _nt, "atbash(ENC)"))

_vig_data = [
    (C, "KEY", "LEMON CURD", "Vigenere with key KEY: each letter shifts by the key letter beneath it. The demo walks the key across the message."),
    (C, "CODE", "SECRET AGENT", "Vigenere with key CODE - fittingly, the key is the word CODE."),
    (A, "JAH", "SIGNATURE CIPHER", "Vigenere with key JAH: polyalphabetic, unbreakable by simple frequency counting for centuries."),
    (A, "PUZZLE", "THE FINAL LEVEL", "Vigenere with key PUZZLE: longer keys mean tougher codes - this one earns its Advanced badge."),
]
for _t, _key, _pt, _nt in _vig_data:
    _enc = vigenere(_pt, _key)
    TOPICS.append(_cb(_t, "Codebreaker: Vigenere key %s" % _key, "Vigenere cipher, keyword %s" % _key, _pt, _enc,
                      "write the keyword repeatedly under the message; shift each letter by its key letter (A=0, B=1, ...)",
                      _nt, "vigenere_dec(ENC, %r)" % _key))

_rail_data = [
    (A, 3, "ZIGZAG WRITING HIDES WORDS", "Rail fence, 3 rails: write in a zigzag down and up, then read across the rails."),
    (A, 4, "THE FENCE HAS FOUR RAILS", "Rail fence, 4 rails: deeper zigzag, trickier read-off."),
]
for _t, _rails, _pt, _nt in _rail_data:
    _enc = railfence(_pt, _rails)
    TOPICS.append(_cb(_t, "Codebreaker: rail fence %d" % _rails, "Rail-fence transposition, %d rails" % _rails, _pt, _enc,
                      "rebuild the zigzag: mark the wave pattern under the encoded text, then read down the waves",
                      _nt, "unrailfence(ENC, %d)" % _rails))

_rev_data = [
    (C, "GNITIRW RORRIM", "Reversed writing: the whole message spelled backward - the oldest trick that still works on skimmers."),
    (A, "DOUBLE TROUBLE CODE", "Caesar shift 5 THEN reversed: two locks on one message - decode in reverse order."),
]
_pt = "MIRROR WRITING"
TOPICS.append(_cb(C, "Codebreaker: mirror writing", "Full reversal (message spelled backward)", _pt, _pt[::-1],
                  "read the message from right to left, letter by letter",
                  "The oldest trick that still works on skimmers.", "ENC[::-1]"))
_pt2 = "DOUBLE TROUBLE CODE"
_enc2 = caesar(_pt2, 5)[::-1]
TOPICS.append(_cb(A, "Codebreaker: double lock", "Caesar shift 5, then full reversal (two locks)", _pt2, _enc2,
                  "first un-reverse the message, then Caesar-decode with shift 5 (shift back 5)",
                  "Two locks, one message: always decode in the reverse order of encoding.", "caesar(ENC[::-1], 21)"))

# --- extra Compounded ciphers (4)
for _sh, _pt, _nt in [
    (15, "FIFTEEN SHIFTS DEEP", "Shift 15: past the halfway mark of the alphabet - the letters feel far from home."),
    (17, "SEVENTEEN STEPS", "Shift 17 is shift -9 in disguise - two names, one cipher."),
    (21, "TWENTY ONE GUNS", "Shift 21 salutes - big shifts, same simple machinery."),
]:
    TOPICS.append(_caesar_rec(C, _sh, _pt, _nt))
_pt = "THE MIRROR HAS TWO FACES"
_enc = atbash(_pt)
TOPICS.append(_cb(C, "Codebreaker: Atbash mirror (%s)" % _pt[:20].rstrip(), "Atbash cipher (alphabet reversed: A<->Z, B<->Y, ...)", _pt, _enc,
                  "replace each letter with its mirror twin: A<->Z, B<->Y, C<->X, all the way to the middle",
                  "Atbash never repeats itself: encode twice and you are home.", "atbash(ENC)"))

# --- extra Advanced ciphers (6)
for _key, _pt, _nt in [
    ("SIGNATURE", "THE CIPHER SCHOOL", "Vigenere with key SIGNATURE: nine letters of key, serious protection."),
    ("CODEBREAKER", "THE FINAL FRONTIER", "Vigenere with key CODEBREAKER: the longest key in the database - break this and you graduate."),
]:
    _enc = vigenere(_pt, _key)
    TOPICS.append(_cb(A, "Codebreaker: Vigenere key %s" % _key, "Vigenere cipher, keyword %s" % _key, _pt, _enc,
                      "write the keyword repeatedly under the message; shift each letter by its key letter (A=0, B=1, ...)",
                      _nt, "vigenere_dec(ENC, %r)" % _key))
_pt = "FIVE RAILS ARE TRICKY"
_enc = railfence(_pt, 5)
TOPICS.append(_cb(A, "Codebreaker: rail fence 5", "Rail-fence transposition, 5 rails", _pt, _enc,
                  "rebuild the zigzag: mark the wave pattern under the encoded text, then read down the waves",
                  "Five rails deep: the zigzag gets genuinely hard to hold in your head.", "unrailfence(ENC, 5)"))
_pt = "ATBASH THEN CAESAR"
_enc = caesar(atbash(_pt), 7)
TOPICS.append(_cb(A, "Codebreaker: Atbash + Caesar double", "Atbash, then Caesar shift 7 (two locks)", _pt, _enc,
                  "decode in reverse order: first Caesar-decode shift 7 (shift back 7), then Atbash the result",
                  "Two different locks: order of decoding is the reverse of order of encoding.", "atbash(caesar(ENC, 19))"))
_pt = "REVERSE THEN VIGENERE"
_enc = vigenere(_pt[::-1], "KEY")
TOPICS.append(_cb(A, "Codebreaker: reverse + Vigenere double", "Full reversal, then Vigenere key KEY (two locks)", _pt, _enc,
                  "first Vigenere-decode with key KEY, then reverse the whole result",
                  "Reversal plus polyalphabetic: the codebreaker's final exam.", "vigenere_dec(ENC, 'KEY')[::-1]"))
_pt = "THE LAST CIPHER FALLS"
_enc = railfence(caesar(_pt, 11), 3)
TOPICS.append(_cb(A, "Codebreaker: Caesar + rail double", "Caesar shift 11, then rail fence 3 (two locks)", _pt, _enc,
                  "first un-zigzag the rail fence (3 rails), then Caesar-decode shift 11",
                  "Substitution plus transposition: the two great cipher families, combined.", "caesar(unrailfence(ENC, 3), 15)"))
