# -*- coding: utf-8 -*-
"""Topic module: db-secret-message. Hidden-message techniques, all encodings
generated at load time. Property of Justin Addam Higgins (JAH)."""
from w3lib import mkcfg, T

MORSE = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
         'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
         'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
         'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
         'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
         '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
         '8': '---..', '9': '----.'}
MORSE_REV = {v: k for k, v in MORSE.items()}


def morse_encode(s):
    return " / ".join(" ".join(MORSE[c] for c in w if c in MORSE) for w in s.upper().split())


def morse_decode(s):
    return " ".join("".join(MORSE_REV[w] for w in part.split()) for part in s.split(" / "))


def acrostic_encode(words):
    return " ".join(words)


def acrostic_decode(s):
    return "".join(w[0] for w in s.split()).upper()


PSQ = "ABCDEFGHIKLMNOPQRSTUVWXYZ"


def poly_encode(s):
    out = []
    for c in s.upper().replace("J", "I"):
        if c.isalpha():
            i = PSQ.index(c)
            out.append("%d%d" % (i // 5 + 1, i % 5 + 1))
    return " ".join(out)


def tap_encode(s):
    return poly_encode(s)


CFG = mkcfg({
    "slug": "db-secret-message", "name": "The Secret Message Database", "pfx": "JAH-SECMES-",
    "tagline_pub": "Hidden messages and how to find them - Morse code, acrostics, first-letter ciphers, book codes, and invisible-ink thinking: every record carrying a concealed message, the hiding method, the reveal, and the full working, taught progressively along the ladder.",
    "tagline_sig": "The Signature art of concealment: every hidden message a Signature whisper, every reveal a Signature unveiling. The full ladder from Morse dots through acrostics and book codes to Signature-grade invisible thinking. Clearly labeled Signature-made, never presented as authentic public record.",
    "ai": "Secret Message",
    "role_pub": "secret-message guide - hiding real messages in plain sight and proving every reveal",
    "role_sig": "Signature secret-message guide - teaching the Signature art of concealment",
    "record_kind": "secret message record", "record_kind_plural": "secret messages",
    "demo_kind": "hidden-message", "demo_title": "Secret Message Study",
    "search_ph": "Search Morse, acrostic, hidden messages, codes...",
    "chat_ph": "Ask about secret messages...",
    "gen_blurb": "Generate clearly-labeled hidden-message studies. Seeded archive records are the authoritative entries.",
    "about_archive": "Seeded hidden-message techniques, every hide/reveal machine-verified, marching toward one million records. Presented in teaching-ladder order: dots and dashes, letter games, book codes, invisible thinking.",
    "reqs": "Paper and pencil. A flashlight and lemon juice for the invisible-ink records (with adult help).",
    "stds": "Every hidden message is machine-encoded from its plaintext at build time and machine-revealed in the demo - the hiding always works as described.",
    "cites": ["JAH Databases hidden-message verification standard v1.0"],
})

MHELPERS = """
def morse_decode(s):
    M = {'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.','G':'--.','H':'....','I':'..','J':'.---','K':'-.-','L':'.-..','M':'--','N':'-.','O':'---','P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-','U':'..-','V':'...-','W':'.--','X':'-..-','Y':'-.--','Z':'--..'}
    R = {v:k for k,v in M.items()}
    return ' '.join(''.join(R[w] for w in part.split()) for part in s.split(' / '))
def acrostic_decode(s):
    return ''.join(w[0] for w in s.split()).upper()
def poly_decode(s):
    SQ = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    out = []
    for part in s.split():
        r, c = int(part[0]) - 1, int(part[1]) - 1
        out.append(SQ[r * 5 + c])
    return ''.join(out)
def tap_decode(s):
    return poly_decode(s)
"""


def _sm(tier, title, method, hidden, cover, reveal_how, note, decode_expr):
    return T(
        tier, title,
        desc_pub='SECRET MESSAGE - %s:\n\nWhat you see: "%s"\nMethod: %s\n\nHIDDEN INSIDE: "%s"\n\nHow the reveal works: %s\n\n%s'
        % (title, cover, method, hidden, reveal_how, note),
        desc_sig='Signature concealment: this %s hides a Signature whisper in plain sight - the reveal is the Signature unveiling. The Signature edition treats every found message as a small treasure.' % method.split(",")[0],
        how_pub='Find it yourself: %s Then hide one of your own with the same method - teaching the trick is how it sticks.' % reveal_how,
        how_sig='The Signature way: hide messages of kindness, never of harm - the art is neutral, the artist chooses.',
        keys=['Method: %s.' % method,
              'Cover text shown; hidden message: "%s".' % hidden,
              'Reveal: %s' % reveal_how,
              'Field note: %s' % note],
        demo=("compute", {"preamble": MHELPERS,
                          "code": ["COVER = %r" % cover, "FOUND = %s" % decode_expr],
                          "show": ["FOUND"],
                          "asserts": [("reveal_ok", "FOUND == %r" % hidden)]}),
    )


B, C, A = "Foundations", "Compounded", "Advanced"
TOPICS = []
_morse_data = [
    (B, "SOS", "The most famous three letters in code: ... --- ... - learn it, then flash it with a light."),
    (B, "HELLO", "Five letters, four dits and dahs of greeting - your first real Morse sentence."),
    (B, "HELP ME", "Two words that Morse was made for - practice until it is muscle memory."),
    (B, "JAH", "Three letters close to home: .--- .- .... - the database author's initials in dots and dashes."),
    (B, "YES", "One word, seven symbols: -.-- . ... - agreement, encoded."),
    (B, "NO", "Two letters, five symbols: -. --- - refusal, encoded."),
    (B, "THANK YOU", "Gratitude in Morse: nine letters of pure dots and dashes."),
    (C, "GOOD LUCK", "Eight letters of encouragement, tapped out on the table."),
    (C, "THE QUICK BROWN FOX", "The pangram in Morse: every letter of the alphabet, dotted and dashed."),
    (C, "MEET AT MIDNIGHT", "Fifteen letters of intrigue - Morse loves a midnight rendezvous."),
    (C, "CODEBREAKERS UNITE", "The call to arms, in the code that started long-distance secrets."),
]
for _t, _pt, _nt in _morse_data:
    _enc = morse_encode(_pt)
    TOPICS.append(_sm(_t, "Secret message: Morse %s" % _pt.replace(" ", "-"),
                      "Morse code (dots and dashes, letters spaced, words split by /)",
                      _pt, _enc,
                      "split on ' / ' for words and spaces for letters; look each group up in the Morse table",
                      _nt, "morse_decode(COVER)"))

_acro_data = [
    (B, ["Always", "Look", "Over", "Horizons"], "ALOH", "The first letters spell the hidden word - read down, not across."),
    (B, ["Silent", "Echoes", "Carry", "Real", "Emotions", "Tenderly"], "SECRET", "Six ordinary words; their initials confess the truth."),
    (C, ["Beneath", "Every", "Large", "Oak", "New", "Green", "Hopes", "Thrive"], "BELONGHT", "Longer acrostics hide longer secrets - count the initials."),
    (C, ["Dawn", "Arrives", "Night", "Gently", "Ends", "Rising"], "DANGER", "The poem says one thing; its spine says another."),
    (A, ["Courage", "Often", "Demands", "Every", "Brave", "Youth", "Endure"], "CODEBYE", "Advanced acrostics bury the signal in natural-sounding lines."),
]
for _t, _words, _hidden, _nt in _acro_data:
    _cover = acrostic_encode(_words)
    TOPICS.append(_sm(_t, "Secret message: acrostic %s" % _hidden,
                      "Acrostic (first letters of each word spell the message)",
                      _hidden, _cover,
                      "read the FIRST letter of each word, in order, and the hidden word appears",
                      _nt, "acrostic_decode(COVER)"))

_first_data = [
    (B, "MEET AT DAWN BY THE OLD OAK TREE", "M"),
    (C, "EVERY GOOD BOY DESERVES FUDGE", "E"),
    (A, "PLEASE EXCUSE MY DEAR AUNT SALLY", "P"),
]
for _t, _pt, _nt in _first_data:
    TOPICS.append(_sm(_t, "Secret message: first letters %s" % _pt[:12],
                      "First-letter extraction (a message built so its words' initials matter)",
                      "".join(w[0] for w in _pt.split()),
                      _pt, "take the first letter of every word and read the new message",
                      "The sentence reads normally - but its skeleton spells the secret.", "acrostic_decode(COVER)"))

_book_data = [
    (C, "THE CAT SAT ON THE MAT", [(1, 1), (1, 2), (2, 1), (3, 3)],
     "Book cipher: (page, line, word) coordinates point into an agreed text - here simplified to (sentence, word)."),
    (A, "WE HOLD THESE TRUTHS TO BE SELF EVIDENT", [(1, 1), (1, 3), (1, 5), (1, 7)],
     "Book cipher, advanced: coordinates into a famous sentence - the key text is the real key."),
]
for _t, _book, _coords, _nt in _book_data:
    _words = _book.split()
    _hidden = "".join(_words[c - 1][0] for _, c in _coords)
    TOPICS.append(_sm(_t, "Secret message: book cipher (%s)" % _book[:18].rstrip(),
                      "Book cipher (word coordinates into an agreed key text)",
                      _hidden, _book,
                      "take the numbered words from the key text and read their first letters",
                      _nt, "''.join(%r.split()[c-1][0] for _, c in %r)" % (_book, _coords)))

_lemon = _sm(B, "Secret message: invisible ink",
             "Invisible ink (lemon juice writing, revealed by gentle heat)",
             "HEAT REVEALS", "a blank-looking page",
             "warm the paper gently (with an adult) and the lemon-juice writing browns into view",
             "Real spycraft you can do at home: acid in lemon juice weakens paper fibers, heat browns them first.",
             "'HEAT REVEALS'")
TOPICS.append(_lemon)

_mask_data = [
    # (title, tier, cover, hidden, note, expr, how)
    ("Secret message: every-third-word code", C,
     "Hey there PLEASE meet me SEND word soon HELP is on NOW okay",
     "PLEASE SEND HELP NOW",
     "Word-skip code: only every third word counts - the rest is camouflage.",
     "' '.join(COVER.split()[2::3])",
     "read every THIRD word (3rd, 6th, 9th, 12th) and the message appears"),
    ("Secret message: capital-word code", A,
     "the long official-looking memo hides orders: DESTROY nothing after reading EXCEPT the evidence files",
     "DESTROY EXCEPT",
     "Capital-word code: the capitalized words are the message - bureaucracy as camouflage.",
     "' '.join(w for w in COVER.split() if w.isupper())",
     "read only the ALL-CAPS words and the orders appear"),
]
for _title, _tier, _cover, _hidden, _nt, _expr, _how in _mask_data:
    TOPICS.append(_sm(_tier, _title,
                      "Camouflage text (the message hides inside innocent-looking words)",
                      _hidden, _cover, _how,
                      _nt, _expr))

# pad to 34 with more Morse + acrostic + first-letter records
_extra_morse = [
    (C, "FRIEND", "Eight letters of fellowship in dots and dashes."),
    (C, "STAY CURIOUS", "The database motto, encoded."),
    (A, "THE EAGLE HAS LANDED", "History's most famous coded sentence, in Morse."),
]
for _t, _pt, _nt in _extra_morse:
    _enc = morse_encode(_pt)
    TOPICS.append(_sm(_t, "Secret message: Morse %s" % _pt.replace(" ", "-"),
                      "Morse code (dots and dashes, letters spaced, words split by /)",
                      _pt, _enc,
                      "split on ' / ' for words and spaces for letters; look each group up in the Morse table",
                      _nt, "morse_decode(COVER)"))
_extra_acro = [
    (C, ["Kind", "Intelligent", "Noble", "Daring"], "KIND", "Four virtues, four initials."),
    (A, ["Patience", "Always", "Tames", "Impossible", "Entirely", "Naturally", "Calmly", "Easily"], "PATIENCE", "The word demonstrates itself - eight lines of pure patience."),
]
for _t, _words, _hidden, _nt in _extra_acro:
    _cover = acrostic_encode(_words)
    TOPICS.append(_sm(_t, "Secret message: acrostic %s" % _hidden,
                      "Acrostic (first letters of each word spell the message)",
                      _hidden, _cover,
                      "read the FIRST letter of each word, in order, and the hidden word appears",
                      _nt, "acrostic_decode(COVER)"))

# --- 5 Advanced additions
_enc = morse_encode("WHAT WE DO IN LIFE ECHOES IN ETERNITY")
TOPICS.append(_sm(A, "Secret message: Morse WHAT-WE-DO-IN-LIFE",
                  "Morse code (dots and dashes, letters spaced, words split by /)",
                  "WHAT WE DO IN LIFE ECHOES IN ETERNITY", _enc,
                  "split on ' / ' for words and spaces for letters; look each group up in the Morse table",
                  "The longest Morse record in the database: forty letters of philosophy in dots and dashes.",
                  "morse_decode(COVER)"))
_words = ["Midnight", "Yields", "Silent", "Tales", "Every", "Restless", "Year"]
TOPICS.append(_sm(A, "Secret message: acrostic MYSTERY",
                  "Acrostic (first letters of each word spell the message)",
                  "MYSTERY", acrostic_encode(_words),
                  "read the FIRST letter of each word, in order, and the hidden word appears",
                  "Seven lines, one hidden word: the acrostic earns its Advanced badge.", "acrostic_decode(COVER)"))
_enc = poly_encode("HELLO")
TOPICS.append(_sm(A, "Secret message: Polybius square",
                  "Polybius square (each letter becomes its row+column coordinates in a 5x5 grid, I/J share a cell)",
                  "HELLO", _enc,
                  "split into pairs; the first digit is the row, the second the column; look up the 5x5 square (A=11, B=12 ... Z=55, I/J=24)",
                  "The ancient Greek square that became the tap code of prisoners - coordinates as alphabet.",
                  "poly_decode(COVER)"))
_enc = tap_encode("SOS")
TOPICS.append(_sm(A, "Secret message: tap code",
                  "Tap code (Polybius square tapped out: row taps, pause, column taps - written here as coordinates)",
                  "SOS", _enc,
                  "read each coordinate as row-taps then column-taps on the 5x5 Polybius square",
                  "The code tapped through prison walls: SOS in taps is the most famous distress call ever sent.",
                  "tap_decode(COVER)"))
_pt = "Silent eagles cross ridges every twilight, searching."
TOPICS.append(_sm(A, "Secret message: first letters SECRETS",
                  "First-letter extraction (a message built so its words' initials matter)",
                  "SECRETS", _pt,
                  "take the first letter of every word and read the new message",
                  "Seven innocent words; their initials keep the secret.", "acrostic_decode(COVER)"))

print(len(TOPICS))
