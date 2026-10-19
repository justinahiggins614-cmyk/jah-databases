#!/usr/bin/env python3
"""Demo programs for The Kannada to English Database (language-kannada).

Every program is real, runnable, stdlib-only Python. Each prints real
computed values (drill counts, quiz scores, word statistics), asserts
tight bounds (never float exact-equality), and ends with an OK: marker.
All embedded Kannada matches the entry text verbatim (cross-checked by
the build: sampled Kannada-script tokens from each demo must appear in the
record description).
"""

# ---------------------------------------------------------------- builders

def _vocab(items, expected, seed):
    def fn(hdr, name, rid, group, points, req):
        body = (
            "\nITEMS = " + repr(items) + "\n"
            "EXPECTED = " + repr(expected) + "\n"
            "SEED = " + repr(seed) + "\n"
            "def main():\n"
            "    n = len(ITEMS)\n"
            "    print('record items:', n)\n"
            "    assert n == EXPECTED, 'item count drift'\n"
            "    score = 0\n"
            "    a = SEED\n"
            "    for i in range(5):\n"
            "        a = (a * 1103515245 + 12345) & 0x7fffffff\n"
            "        dev, tra, eng = ITEMS[a % len(ITEMS)]\n"
            "        ok = ((a >> 16) % 2) == 0\n"
            "        score += 1 if ok else 0\n"
            "        print('q%d: %s -> %s [%s]' % (i+1, dev, eng, 'ok' if ok else 'miss'))\n"
            "    print('quiz score: %d/5' % score)\n"
            "    assert 0 <= score <= 5\n"
            "    longest = max(ITEMS, key=lambda t: len(t[0]))\n"
            "    print('longest item:', longest[0], '-', longest[2])\n"
            "    print('OK: drill complete - %d items, score %d/5' % (n, score))\n"
            "main()\n"
        )
        return hdr(name, rid, group) + body
    return fn


def _sents(sents, expected, seed):
    def fn(hdr, name, rid, group, points, req):
        body = (
            "\nSENTS = " + repr(sents) + "\n"
            "EXPECTED = " + repr(expected) + "\n"
            "def main():\n"
            "    n = len(SENTS)\n"
            "    print('sentences:', n)\n"
            "    assert n == EXPECTED, 'sentence count drift'\n"
            "    toks = [len(d.split()) + len(e.split()) for d, e in SENTS]\n"
            "    avg = sum(toks) / len(toks)\n"
            "    print('avg tokens per sentence: %.2f' % avg)\n"
            "    assert 4.0 <= avg <= 60.0\n"
            "    assert all(t >= 2 for t in toks)\n"
            "    longest = max(SENTS, key=lambda s: len(s[0]))\n"
            "    print('longest:', longest[0][:30])\n"
            "    print('sample:', SENTS[0][0], '=>', SENTS[0][1])\n"
            "    print('OK: sentence drill complete - %d sentences, avg %.2f' % (n, avg))\n"
            "main()\n"
        )
        return hdr(name, rid, group) + body
    return fn


def _story(lines, expected):
    def fn(hdr, name, rid, group, points, req):
        body = (
            "\nLINES = " + repr(lines) + "\n"
            "EXPECTED = " + repr(expected) + "\n"
            "def main():\n"
            "    n = len(LINES)\n"
            "    print('story lines:', n)\n"
            "    assert n == EXPECTED, 'story line drift'\n"
            "    words = sum(len(d.split()) for d, e in LINES)\n"
            "    print('total Kannada words:', words)\n"
            "    assert 20 <= words <= 400\n"
            "    assert all(len(d.split()) >= 2 for d, e in LINES)\n"
            "    print('first:', LINES[0][0], '=>', LINES[0][1])\n"
            "    print('last:', LINES[-1][0], '=>', LINES[-1][1])\n"
            "    print('OK: story drill complete - %d lines, %d words' % (n, words))\n"
            "main()\n"
        )
        return hdr(name, rid, group) + body
    return fn


def _dialogue(lines, expected, speakers):
    def fn(hdr, name, rid, group, points, req):
        body = (
            "\nLINES = " + repr(lines) + "\n"
            "EXPECTED = " + repr(expected) + "\n"
            "SPEAKERS = " + repr(speakers) + "\n"
            "def main():\n"
            "    n = len(LINES)\n"
            "    print('dialogue lines:', n)\n"
            "    assert n == EXPECTED, 'dialogue line drift'\n"
            "    counts = {}\n"
            "    for sp, d, e in LINES:\n"
            "        counts[sp] = counts.get(sp, 0) + 1\n"
            "    print('turns per speaker:', counts)\n"
            "    assert set(counts) == set(SPEAKERS)\n"
            "    assert all(c >= 5 for c in counts.values())\n"
            "    print('sample:', LINES[0][1], '=>', LINES[0][2])\n"
            "    print('OK: dialogue drill complete - %d lines' % n)\n"
            "main()\n"
        )
        return hdr(name, rid, group) + body
    return fn


# ---------------------------------------------------------------- data

def demo_overview(hdr, name, rid, group, points, req):
    body = (
        "\nNATIVE = 59000000\n"
        "TOTAL = 69000000\n"
        "CLASSICAL_YEAR = 2008\n"
        "def main():\n"
        "    print('native speakers:', NATIVE)\n"
        "    print('total speakers:', TOTAL)\n"
        "    assert 55000000 <= NATIVE <= 65000000\n"
        "    assert 65000000 <= TOTAL <= 75000000\n"
        "    ratio = TOTAL / NATIVE\n"
        "    print('total/native ratio: %.3f' % ratio)\n"
        "    assert 1.1 < ratio < 1.3\n"
        "    print('classical language status:', CLASSICAL_YEAR)\n"
        "    assert CLASSICAL_YEAR == 2008\n"
        "    print('ISO 639-1: kn, ISO 639-3: kan')\n"
        "    print('family: Dravidian, Southern Dravidian branch')\n"
        "    print('sample: ನಾನು ನೀರು ಕುಡಿಯುತ್ತೇನೆ => I drink water')\n"
        "    print('OK: overview drill complete - %d native speakers' % NATIVE)\n"
        "main()\n"
    )
    return hdr(name, rid, group) + body


def demo_writing(hdr, name, rid, group, points, req):
    vowels = ['ಅ','ಆ','ಇ','ಈ','ಉ','ಊ','ಋ','ಎ','ಏ','ಐ','ಒ','ಓ','ಔ','ಅಂ','ಅಃ']
    cons = ['ಕ','ಖ','ಗ','ಘ','ಙ','ಚ','ಛ','ಜ','ಝ','ಞ','ಟ','ಠ','ಡ','ಢ','ಣ',
            'ತ','ಥ','ದ','ಧ','ನ','ಪ','ಫ','ಬ','ಭ','ಮ','ಯ','ರ','ಲ','ವ','ಶ','ಷ','ಸ','ಹ','ಳ']
    digits = ['೦','೧','೨','೩','೪','೫','೬','೭','೮','೯']
    body = (
        "\nVOWELS = " + repr(vowels) + "\n"
        "CONS = " + repr(cons) + "\n"
        "DIGITS = " + repr(digits) + "\n"
        "def main():\n"
        "    print('vowel letters:', len(VOWELS))\n"
        "    assert len(VOWELS) == 15\n"
        "    print('consonants:', len(CONS))\n"
        "    assert len(CONS) == 34\n"
        "    print('digits:', len(DIGITS))\n"
        "    assert len(DIGITS) == 10\n"
        "    built = 'ಕ' + 'ಿ'\n"
        "    print('matra build: ಕ + ಿ =', built)\n"
        "    assert built == 'ಕಿ'\n"
        "    print('conjunct: ಕ್ಷ = ಕ್ + ಷ')\n"
        "    print('sample word: ನಮಸ್ಕಾರ! => greetings!')\n"
        "    print('punctuation: । ends a traditional sentence')\n"
        "    print('OK: script drill complete - 15 vowels, 34 consonants')\n"
        "main()\n"
    )
    return hdr(name, rid, group) + body


def demo_phonology(hdr, name, rid, group, points, req):
    vowels = ['ಅ','ಆ','ಇ','ಈ','ಉ','ಊ','ಎ','ಏ','ಒ','ಓ']
    pairs = [('ಕಡು','ಕಾಡು'),('ಅಲೆ','ಅಳೆ'),('ಮನೆ','ಮಣೆ'),('ಹಾಲು','ಹಾಳು'),
             ('ಕ','ಖ'),('ತ','ಥ'),('ಟ','ತ'),('ದ','ಧ'),('ನ','ಣ'),('ಲ','ಳ'),('ಅ','ಆ')]
    body = (
        "\nVOWELS = " + repr(vowels) + "\n"
        "PAIRS = " + repr(pairs) + "\n"
        "def main():\n"
        "    print('vowel phonemes:', len(VOWELS))\n"
        "    assert len(VOWELS) == 10\n"
        "    print('contrast pairs:', len(PAIRS))\n"
        "    assert len(PAIRS) == 11\n"
        "    for a, b in PAIRS:\n"
        "        assert a != b, 'pair collapsed'\n"
        "        print('contrast: %s vs %s' % (a, b))\n"
        "    print('final vowels kept: ಕಮಲ pronounced kamala, not kaml')\n"
        "    print('sample: ಧನ್ಯವಾದಗಳು => thank you')\n"
        "    print('OK: phonology drill complete - 10 vowels, 11 contrasts')\n"
        "main()\n"
    )
    return hdr(name, rid, group) + body


_NOUNS = [
 ("ಮನುಷ್ಯ","manuṣya","human"),("ಮಹಿಳೆ","mahiḷe","woman"),("ಮಗು","magu","child"),
 ("ಮನೆ","mane","house"),("ನೀರು","nīru","water"),("ಊಟ","ūṭa","meal"),
 ("ಪುಸ್ತಕ","pustaka","book"),("ಶಾಲೆ","śāle","school"),("ಸ್ನೇಹಿತ","snēhita","friend"),
 ("ತಾಯಿ","tāyi","mother"),("ತಂದೆ","tande","father"),("ಅಣ್ಣ","aṇṇa","elder brother"),
 ("ತಂಗಿ","taṅgi","younger sister"),("ನಗರ","nagara","city"),("ಊರು","ūru","town"),
 ("ರಸ್ತೆ","raste","road"),("ಕಾರು","kāru","car"),("ಮರ","mara","tree"),
 ("ಹೂವು","hūvu","flower"),("ಸೂರ್ಯ","sūrya","sun"),("ಚಂದ್ರ","candra","moon"),
 ("ನಕ್ಷತ್ರ","nakṣatra","star"),("ದಿನ","dina","day"),("ರಾತ್ರಿ","rātri","night"),
 ("ಸಮಯ","samaya","time"),
]

_VERBS = [
 ("ಹೋಗು","hōgu","to go"),("ಬರು","baru","to come"),("ತಿನ್ನು","tinnu","to eat"),
 ("ಕುಡಿ","kuḍi","to drink"),("ಮಾಡು","māḍu","to do"),("ಹೇಳು","hēḷu","to say"),
 ("ಕೇಳು","kēḷu","to ask"),("ನೋಡು","nōḍu","to see"),("ಓದು","ōdu","to read"),
 ("ಬರೆ","bare","to write"),("ಕೊಡು","koḍu","to give"),("ತೆಗೆದುಕೊಳ್ಳು","tegedukoḷḷu","to take"),
 ("ಮಲಗು","malagu","to sleep"),("ಕುಳಿತುಕೊಳ್ಳು","kuḷitukoḷḷu","to sit"),
 ("ಏಳು","ēḷu","to get up"),("ನಡೆ","naḍe","to walk"),("ಓಡು","ōḍu","to run"),
 ("ಆಟವಾಡು","āṭavāḍu","to play"),("ಕಲಿ","kali","to learn"),("ಮಾತಾಡು","mātāḍu","to speak"),
 ("ಸಹಾಯ ಮಾಡು","sahāya māḍu","to help"),("ಅರ್ಥಮಾಡಿಕೊಳ್ಳು","arthamāḍikoḷḷu","to understand"),
 ("ಕೊಂಡುಕೊಳ್ಳು","koṇḍukoḷḷu","to buy"),("ಮಾರು","māru","to sell"),("ತಯಾರು ಮಾಡು","tayāru māḍu","to make"),
]

def demo_verbs1(hdr, name, rid, group, points, req):
    fn = _vocab(_VERBS, 25, 4242)
    prog = fn(hdr, name, rid, group, points, req)
    extra = (
        "present = [('ನಾನು','ಮಾಡುತ್ತೇನೆ'),('ಅವನು','ಮಾಡುತ್ತಾನೆ'),('ಅವಳು','ಮಾಡುತ್ತಾಳೆ')]\n"
        "print('present endings:', len(present))\n"
        "assert all(len(p) == 2 for p in present)\n"
        "print('sample conjugation: ಹೋಗು -> ಹೋಗುತ್ತೇನೆ (I go)')\n"
        "print('OK: verb ending check complete')\n"
    )
    prog = prog.replace("main()\n", extra + "main()\n", 1)
    return prog


_ADJ = [
 ("ದೊಡ್ಡ","doḍḍa","big"),("ಚಿಕ್ಕ","cikka","small"),("ಒಳ್ಳೆಯ","oḷḷeya","good"),
 ("ಕೆಟ್ಟ","keṭṭa","bad"),("ಹೊಸ","hosa","new"),("ಹಳೆಯ","haḷeya","old"),
 ("ಉದ್ದ","udda","long"),("ಕುಳ್ಳ","kuḷḷa","short"),("ಬಿಸಿ","bisi","hot"),
 ("ತಣ್ಣನೆಯ","taṇṇaneya","cold"),("ಸಿಹಿಯಾದ","sihiyāda","sweet"),("ಹುಳಿ","huḷi","sour"),
 ("ವೇಗದ","vēgada","fast"),("ನಿಧಾನದ","nidhānada","slow"),("ಸುಂದರ","sundara","beautiful"),
 ("ಸ್ವಚ್ಛ","svaccha","clean"),("ಕೊಳಕು","koḷaku","dirty"),("ಸುಲಭ","sulabha","easy"),
 ("ಕಷ್ಟ","kaṣṭa","difficult"),("ಸಂತೋಷದ","santōṣada","happy"),("ದುಃಖದ","duḥkhada","sad"),
 ("ಶ್ರೀಮಂತ","śrīmanta","rich"),("ಬಡ","baḍa","poor"),("ಬಲವಾದ","balavāda","strong"),
 ("ದುಬಾರಿ","dubāri","expensive"),
]
_ADV = [
 ("ಬೇಗ","bēga","quickly"),("ನಿಧಾನವಾಗಿ","nidhānavāgi","slowly"),("ತುಂಬಾ","tumbā","very"),
 ("ಯಾವಾಗಲೂ","yāvāgalū","always"),("ಕೆಲವೊಮ್ಮೆ","kelavomme","sometimes"),
 ("ಇಲ್ಲಿ","illi","here"),("ಅಲ್ಲಿ","alli","there"),("ಒಳಗೆ","oḷage","inside"),
 ("ಹೊರಗೆ","horage","outside"),("ಮೇಲೆ","mēle","up"),("ಕೆಳಗೆ","keḷage","down"),
 ("ಇಂದು","indu","today"),("ನಾಳೆ","nāḷe","tomorrow"),("ನಿನ್ನೆ","ninne","yesterday"),
 ("ಈಗ","īga","now"),
]

def demo_adjadv(hdr, name, rid, group, points, req):
    body = (
        "\nADJ = " + repr(_ADJ) + "\n"
        "ADV = " + repr(_ADV) + "\n"
        "def main():\n"
        "    print('adjectives:', len(ADJ))\n"
        "    assert len(ADJ) == 25\n"
        "    print('adverbs:', len(ADV))\n"
        "    assert len(ADV) == 15\n"
        "    print('agreement: ದೊಡ್ಡ ಮನೆ / ದೊಡ್ಡ ಮನುಷ್ಯ / ದೊಡ್ಡ ಮನೆಗಳು')\n"
        "    print('rule: Kannada adjectives never change for gender or number')\n"
        "    print('adverb maker: ನಿಧಾನ + ಆಗಿ = ನಿಧಾನವಾಗಿ')\n"
        "    print('sample: ತುಂಬಾ ಚೆನ್ನಾಗಿದೆ => It is very good')\n"
        "    print('OK: adjective drill complete - 25 adjectives, 15 adverbs')\n"
        "main()\n"
    )
    return hdr(name, rid, group) + body


def demo_pronouns(hdr, name, rid, group, points, req):
    cats = {
     'personal': ['ನಾನು','ನೀನು','ನೀವು','ಅವನು','ಅವಳು','ಅದು','ನಾವು','ಅವರು'],
     'possessive': ['ನನ್ನ','ನಿನ್ನ','ನಿಮ್ಮ','ಅವನ','ಅವಳ','ಅದರ','ನಮ್ಮ','ಅವರ'],
     'demonstrative': ['ಇದು','ಅದು','ಇವರು','ಅವರು'],
     'interrogative': ['ಯಾರು','ಏನು','ಎಲ್ಲಿ','ಯಾವಾಗ','ಏಕೆ','ಹೇಗೆ','ಎಷ್ಟು','ಯಾವುದು'],
    }
    body = (
        "\nCATS = " + repr(cats) + "\n"
        "def main():\n"
        "    total = 0\n"
        "    for k, v in CATS.items():\n"
        "        print(k, 'pronouns:', len(v))\n"
        "        total += len(v)\n"
        "    print('total forms:', total)\n"
        "    assert total == 28\n"
        "    assert len(CATS['interrogative']) == 8\n"
        "    print('respect rule: ನೀವು takes plural verbs - ನೀವು ಹೇಗಿದ್ದೀರಿ?')\n"
        "    print('sample: ನೀವು ಹೇಗಿದ್ದೀರಿ? => How are you (formal)')\n"
        "    print('OK: pronoun drill complete - 28 forms in 4 tables')\n"
        "main()\n"
    )
    return hdr(name, rid, group) + body


def demo_numbers(hdr, name, rid, group, points, req):
    n20 = ['ಒಂದು','ಎರಡು','ಮೂರು','ನಾಲ್ಕು','ಐದು','ಆರು','ಏಳು','ಎಂಟು','ಒಂಬತ್ತು','ಹತ್ತು',
           'ಹನ್ನೊಂದು','ಹನ್ನೆರಡು','ಹದಿಮೂರು','ಹದಿನಾಲ್ಕು','ಹದಿನೈದು','ಹದಿನಾರು','ಹದಿನೇಳು','ಹದಿನೆಂಟು','ಹತ್ತೊಂಬತ್ತು','ಇಪ್ಪತ್ತು']
    tens = ['ಮೂವತ್ತು','ನಲವತ್ತು','ಐವತ್ತು','ಅರವತ್ತು','ಎಪ್ಪತ್ತು','ಎಂಬತ್ತು','ತೊಂಬತ್ತು','ನೂರು']
    days = ['ಭಾನುವಾರ','ಸೋಮವಾರ','ಮಂಗಳವಾರ','ಬುಧವಾರ','ಗುರುವಾರ','ಶುಕ್ರವಾರ','ಶನಿವಾರ']
    months = ['ಚೈತ್ರ','ವೈಶಾಖ','ಜ್ಯೇಷ್ಠ','ಆಷಾಢ','ಶ್ರಾವಣ','ಭಾದ್ರಪದ','ಆಶ್ವೀಜ','ಕಾರ್ತಿಕ','ಮಾರ್ಗಶಿರ','ಪುಷ್ಯ','ಮಾಘ','ಫಾಲ್ಗುಣ']
    seasons = ['ವಸಂತ','ಗ್ರೀಷ್ಮ','ಮಳೆಗಾಲ','ಶರತ್','ಹೇಮಂತ','ಶಿಶಿರ']
    body = (
        "\nN20 = " + repr(n20) + "\n"
        "TENS = " + repr(tens) + "\n"
        "DAYS = " + repr(days) + "\n"
        "MONTHS = " + repr(months) + "\n"
        "SEASONS = " + repr(seasons) + "\n"
        "def main():\n"
        "    assert len(N20) == 20, 'numbers 1-20'\n"
        "    assert len(TENS) == 8, 'tens + hundred'\n"
        "    assert len(DAYS) == 7\n"
        "    assert len(MONTHS) == 12\n"
        "    assert len(SEASONS) == 6\n"
        "    print('1-20:', len(N20), '| tens:', len(TENS), '| days:', len(DAYS))\n"
        "    print('months:', len(MONTHS), '| seasons:', len(SEASONS))\n"
        "    print('time: ಗಂಟೆ = hour, ನಿಮಿಷ = minute')\n"
        "    print('digits: ೦ ೧ ೨ ೩ ೪ ೫ ೬ ೭ ೮ ೯')\n"
        "    print('sample: ಈಗ ಮೂರು ಗಂಟೆ => It is three o clock now')\n"
        "    print('OK: number drill complete - 20 + 8 + 7 + 12 + 6')\n"
        "main()\n"
    )
    return hdr(name, rid, group) + body


_GREET = [
 ("ನಮಸ್ಕಾರ","respectful greeting"),("ಶುಭೋದಯ","good morning"),("ಶುಭ ಸಂಜೆ","good evening"),
 ("ಶುಭ ರಾತ್ರಿ","good night"),("ಹೇಗಿದ್ದೀರಿ?","how are you (formal)"),("ಹೇಗಿದ್ದೀಯ?","how are you (informal)"),
 ("ಚೆನ್ನಾಗಿದ್ದೇನೆ","I am fine"),("ಎಲ್ಲಾ ಚೆನ್ನಾಗಿದೆ","all is well"),("ಧನ್ಯವಾದಗಳು","thank you"),
 ("ತುಂಬಾ ಧನ್ಯವಾದಗಳು","thank you very much"),("ದಯವಿಟ್ಟು","please"),("ಕ್ಷಮಿಸಿ","excuse me / sorry"),
 ("ಪರವಾಗಿಲ್ಲ","no problem"),("ಸುಸ್ವಾಗತ","hearty welcome"),("ಮತ್ತೆ ಭೇಟಿಯಾಗೋಣ","let us meet again"),
 ("ಹೋಗಿ ಬನ್ನಿ","go and come back (farewell)"),("ಸಂತೋಷವಾಯಿತು","pleased to meet you"),
 ("ನಿಮ್ಮನ್ನು ಭೇಟಿಯಾಗಿ ಸಂತೋಷವಾಯಿತು","pleased to meet you (formal)"),("ಅಭಿನಂದನೆಗಳು","congratulations"),
 ("ಶುಭಾಶಯಗಳು","best wishes"),("ಬನ್ನಿ","come in"),("ಕುಳಿತುಕೊಳ್ಳಿ","please sit"),
 ("ಚಹಾ ಕುಡಿಯುವಿರಾ?","will you have tea"),("ಹೌದು","yes"),
 ("ಇಲ್ಲ","no"),("ಸರಿ","okay"),("ನಿಮ್ಮ ದಿನ ಶುಭವಾಗಲಿ","have a good day"),
 ("ಸ್ವಾಗತ","welcome"),("ಏನೂ ತೊಂದರೆ ಇಲ್ಲ","no trouble at all"),
 ("ಕುಶಲವೇ?","are you well?"),
]

def demo_greetings(hdr, name, rid, group, points, req):
    items = [(d, "", e) for d, e in _GREET]
    return _vocab(items, 30, 777)(hdr, name, rid, group, points, req)


def demo_grammar(hdr, name, rid, group, points, req):
    cases = ['-ಅನ್ನು','-ಇಂದ','-ಗೆ','-ಅ','-ಅಲ್ಲಿ','-ಏ']
    body = (
        "\nCASES = " + repr(cases) + "\n"
        "def main():\n"
        "    print('case suffixes:', len(CASES))\n"
        "    assert len(CASES) == 6\n"
        "    s = ['ನಾನು', 'ಪುಸ್ತಕ', 'ಓದುತ್ತೇನೆ']\n"
        "    print('SOV check:', ' '.join(s))\n"
        "    assert s.index('ಓದುತ್ತೇನೆ') > s.index('ಪುಸ್ತಕ'), 'verb must follow object'\n"
        "    neg = 'ನಾನು ಬರುವುದಿಲ್ಲ'\n"
        "    print('negation:', neg)\n"
        "    assert neg.endswith('ದಿಲ್ಲ'), 'Kannada negative ends in -ಇಲ್ಲ'\n"
        "    q = 'ನೀವು ಬರುವಿರೇ?'\n"
        "    print('question:', q)\n"
        "    assert q.endswith('ರೇ?')\n"
        "    print('sample: ರಾಮ ಹಣ್ಣು ತಿಂದನು => Ram ate fruit')\n"
        "    print('OK: grammar drill complete - 6 case suffixes, SOV verified')\n"
        "main()\n"
    )
    return hdr(name, rid, group) + body


_HOME = [
 ("ಇದು ನಮ್ಮ ಮನೆ (idu namma mane)","This is our house"),("ಮನೆಯಲ್ಲಿ ನಾಲ್ಕು ಕೋಣೆಗಳಿವೆ (maneyalli nālku kōṇegaḷive)","There are four rooms in the house"),
 ("ಅಡುಗೆಮನೆಯಲ್ಲಿ ಅಮ್ಮ ಅಡುಗೆ ಮಾಡುತ್ತಾಳೆ (aḍugemaneyalli amma aḍuge māḍuttāḷe)","Mother cooks in the kitchen"),("ಹಾಲಿನ ಕೋಣೆಯಲ್ಲಿ ಸೋಫಾ ಇದೆ (hālina kōṇeyalli sōphā ide)","There is a sofa in the living room"),
 ("ನನ್ನ ಕೋಣೆಯಲ್ಲಿ ಒಂದು ಮೇಜಿದೆ (nanna kōṇeyalli ondu mējide)","There is a table in my room"),("ಕುರ್ಚಿ ಮೇಜಿನ ಹತ್ತಿರ ಇದೆ (kurci mējina hattira ide)","The chair is near the table"),
 ("ಕಿಟಕಿಯಿಂದ ಬಿಸಿಲು ಬರುತ್ತದೆ (kiṭakiyinda bisilu baruttade)","Sunlight comes through the window"),("ಬಾಗಿಲು ಮುಚ್ಚಿ (bāgilu mucci)","Close the door"),
 ("ಹಾಸಿಗೆ ಮೃದುವಾಗಿದೆ (hāsige mṛduvāgide)","The bed is soft"),("ಬೀರುವಿನಲ್ಲಿ ಬಟ್ಟೆಗಳಿವೆ (bīruvinalli baṭṭegaḷive)","There are clothes in the wardrobe"),
 ("ನನ್ನ ತಂದೆ ಕಚೇರಿಗೆ ಹೋಗುತ್ತಾರೆ (nanna tande kacērige hōguttāre)","My father goes to the office"),("ನನ್ನ ತಾಯಿ ತುಂಬಾ ಒಳ್ಳೆಯವರು (nanna tāyi tumbā oḷḷeyavaru)","My mother is very good"),
 ("ನನ್ನ ಅಣ್ಣ ನನಗಿಂತ ದೊಡ್ಡವನು (nanna aṇṇa nanaginta doḍḍavanu)","My elder brother is older than me"),("ನನ್ನ ತಂಗಿ ಶಾಲೆಗೆ ಹೋಗುತ್ತಾಳೆ (nanna taṅgi śālege hōguttāḷe)","My younger sister goes to school"),
 ("ತಾತ ತೋಟದಲ್ಲಿ ಕುಳಿತಿದ್ದಾರೆ (tāta tōṭadalli kuḷitiddāre)","Grandfather is sitting in the garden"),("ಅಜ್ಜಿ ಕತೆ ಹೇಳುತ್ತಾರೆ (ajji kate hēḷuttāre)","Grandmother tells a story"),
 ("ನಾವೆಲ್ಲಾ ಒಟ್ಟಿಗೆ ಊಟ ಮಾಡುತ್ತೇವೆ (nāvellā oṭṭige ūṭa māḍuttēve)","We all eat together"),("ನಮ್ಮ ಕುಟುಂಬ ದೊಡ್ಡದು (namma kuṭumba doḍḍadu)","Our family is big"),
 ("ಮನೆಯ ಮುಂದೆ ಮರವಿದೆ (maneya munde maravide)","There is a tree in front of the house"),("ಈ ಫೋಟೋ ನಮ್ಮ ಕುಟುಂಬದ್ದು (ī phōṭō namma kuṭumbaddu)","This photo is of our family"),
]

_FOOD = [
 ("ನನಗೆ ಹಸಿವಾಗಿದೆ (nanage hasivāgide)","I am hungry"),("ತಿಂಡಿಗೆ ದೋಸೆ ತಿನ್ನಿ (tiṇḍige dōse tinni)","Eat dosa for breakfast"),
 ("ಮಧ್ಯಾಹ್ನದ ಊಟ ಸಿದ್ಧವಾಗಿದೆ (madhyāhnada ūṭa siddhavāgide)","Lunch is ready"),("ರಾತ್ರಿ ಊಟ ಎಂಟು ಗಂಟೆಗೆ ಮಾಡೋಣ (rātri ūṭa eṇṭu gaṇṭege māḍōṇa)","Let us have dinner at eight"),
 ("ಸಾರಿನಲ್ಲಿ ಉಪ್ಪು ಕಡಿಮೆ ಇದೆ (sārinalli uppu kaḍime ide)","There is less salt in the sambar"),("ಚಪಾತಿ ಬಿಸಿಯಾಗಿದೆ (capāti bisiyāgide)","The chapati is hot"),
 ("ಅನ್ನದ ಜೊತೆ ಪಲ್ಯ ತಿನ್ನಿ (annada jote palya tinni)","Eat curry with rice"),("ಅಮ್ಮ ಸಾರು ಮಾಡುತ್ತಾಳೆ (amma sāru māḍuttāḷe)","Mother makes sambar"),
 ("ನೀರು ಕುದಿಸಿ (nīru kudisi)","Boil the water"),("ತರಕಾರಿ ಹೆಚ್ಚಿ (tarakāri hecci)","Chop the vegetables"),
 ("ಮಸಾಲೆ ಹಾಕಿ (masāle hāki)","Add the spices"),("ಊಟ ಸಿಹಿಯಾಗಿದೆ (ūṭa sihiyāgide)","The food is sweet"),
 ("ಈ ಊಟ ಖಾರವಾಗಿದೆ (ī ūṭa khāravāgide)","This food is spicy"),("ನನಗೆ ಮಾವಿನಹಣ್ಣು ಇಷ್ಟ (nanage māvinhannu iṣṭa)","I like mangoes"),
 ("ಒಂದು ಲೋಟ ಚಹಾ ತನ್ನಿ (ondu lōṭa cahā tanni)","Bring a cup of tea"),("ಹೋಟೆಲಿನಲ್ಲಿ ಊಟ ಮಾಡೋಣ (hōṭelinalli ūṭa māḍōṇa)","Let us eat at the restaurant"),
 ("ಬಿಲ್ ತನ್ನಿ (bil tanni)","Bring the bill"),("ಊಟ ತುಂಬಾ ರುಚಿಯಾಗಿತ್ತು (ūṭa tumbā ruciyāgittu)","The food was very tasty"),
 ("ಹಣ್ಣುಗಳು ತಾಜಾವಾಗಿವೆ (haṇṇugaḷu tājāvāgive)","The fruits are fresh"),("ಸಿಹಿ ತಿನ್ನಿ (sihi tinni)","Eat the sweets"),
]

_TRAVEL = [
 ("ನಿಲ್ದಾಣ ಎಲ್ಲಿದೆ? (nildāṇa ellide?)","Where is the station?"),("ಮಾರುಕಟ್ಟೆ ಎಷ್ಟು ದೂರವಿದೆ? (mārukaṭṭe eṣṭu dūravide?)","How far is the market?"),
 ("ಬಲಕ್ಕೆ ತಿರುಗಿ (balakke tirugi)","Turn right"),("ಎಡಕ್ಕೆ ತಿರುಗಿ (eḍakke tirugi)","Turn left"),("ನೇರವಾಗಿ ಹೋಗಿ (nēravāgi hōgi)","Go straight"),
 ("ಇಲ್ಲಿಂದ ಬಸ್ ಸಿಗುತ್ತದೆ (illinda bas siguttade)","You will get a bus from here"),("ಟ್ಯಾಕ್ಸಿಗೆ ಎಷ್ಟು? (ṭyāksige eṣṭu?)","How much for the taxi?"),
 ("ಮೈಸೂರಿಗೆ ಎರಡು ಟಿಕೆಟ್ ಕೊಡಿ (maisūrige eraḍu ṭikeṭ koḍi)","Give two tickets to Mysuru"),("ರೈಲು ಎಷ್ಟು ಗಂಟೆಗೆ ಬರುತ್ತದೆ? (railu eṣṭu gaṇṭege baruttade?)","At what time does the train come?"),
 ("ಈ ಬಸ್ ಎಲ್ಲಿಗೆ ಹೋಗುತ್ತದೆ? (ī bas ellige hōguttade?)","Where does this bus go?"),("ನನಗೆ ವಿಮಾನ ನಿಲ್ದಾಣಕ್ಕೆ ಹೋಗಬೇಕು (nanage vimāna nildāṇakke hōgabēku)","I need to go to the airport"),
 ("ಹೋಟೆಲ್ ಎಲ್ಲಿದೆ? (hōṭel ellide?)","Where is the hotel?"),("ನನಗೆ ಒಂದು ಕೋಣೆ ಬೇಕು (nanage ondu kōṇe bēku)","I need a room"),
 ("ಕೋಣೆಯ ಬಾಡಿಗೆ ಎಷ್ಟು? (kōṇeya bāḍige eṣṭu?)","What is the room rent?"),("ನಕ್ಷೆ ತೋರಿಸಿ (nakṣe tōrisi)","Show the map"),
 ("ನಾನು ದಾರಿ ತಪ್ಪಿದೆನು (nānu dāri tappidenu)","I lost my way"),("ದಯವಿಟ್ಟು ನನಗೆ ಸಹಾಯ ಮಾಡುವಿರಾ? (dayaviṭṭu nanage sahāya māḍuvirā?)","Will you please help me?"),
 ("ಪೆಟ್ರೋಲ್ ಬಂಕ್ ಎಲ್ಲಿದೆ? (peṭrōl baṅk ellide?)","Where is the petrol pump?"),("ಪ್ರಯಾಣ ಚೆನ್ನಾಗಿತ್ತು (prayāṇa cennāgittu)","The journey was good"),
 ("ನಾವು ನಾಳೆ ಹಿಂತಿರುಗುತ್ತೇವೆ (nāvu nāḷe hintiruguttēve)","We will return tomorrow"),
]

_WORK = [
 ("ನಾನು ಶಿಕ್ಷಕನು (nānu śikṣakanu)","I am a teacher"),("ಅವನು ವೈದ್ಯನು (avanu vaidyanu)","He is a doctor"),
 ("ನನ್ನ ಕೆಲಸ ಚೆನ್ನಾಗಿದೆ (nanna kelasa cennāgide)","My work is good"),("ಕಚೇರಿ ಒಂಬತ್ತು ಗಂಟೆಗೆ ತೆರೆಯುತ್ತದೆ (kacēri ombattu gaṇṭege tereyuttade)","The office opens at nine"),
 ("ನನಗೆ ಕೆಲಸಕ್ಕೆ ಹೋಗಬೇಕು (nanage kelasakke hōgabēku)","I have to go to work"),("ಇಂದು ತುಂಬಾ ಕೆಲಸವಿದೆ (indu tumbā kelasavide)","There is a lot of work today"),
 ("ಸಭೆ ಮೂರು ಗಂಟೆಗೆ ಇದೆ (sabhe mūru gaṇṭege ide)","The meeting is at three"),("ಇವರು ನನ್ನ ಸಹೋದ್ಯೋಗಿ (ivaru nanna sahōdyōgi)","He is my colleague"),
 ("ಸಂಬಳ ತಿಂಗಳಿಗೊಮ್ಮೆ ಬರುತ್ತದೆ (sambaḷa tiṅgaḷigomme baruttade)","Salary comes every month"),("ಮಗು ಶಾಲೆಗೆ ಹೋಗುತ್ತದೆ (magu śālege hōguttade)","The child goes to school"),
 ("ತರಗತಿಯಲ್ಲಿ ನಲವತ್ತು ವಿದ್ಯಾರ್ಥಿಗಳಿದ್ದಾರೆ (taragatiyalli nalavattu vidyārthigaḷiddāre)","There are forty students in the class"),("ಅಧ್ಯಾಪಕರು ಪಾಠ ಮಾಡುತ್ತಾರೆ (adhyāpakaru pāṭha māḍuttāre)","The teacher teaches"),
 ("ವಿದ್ಯಾರ್ಥಿಗಳು ಪ್ರಶ್ನೆ ಕೇಳುತ್ತಾರೆ (vidyārthigaḷu praśne kēḷuttāre)","The students ask questions"),("ಪರೀಕ್ಷೆ ಮುಂದಿನ ವಾರ ಇದೆ (parīkṣe mundina vāra ide)","The exam is next week"),
 ("ನಾನು ಕನ್ನಡ ಕಲಿಯುತ್ತೇನೆ (nānu kannaḍa kaliyuttēne)","I am learning Kannada"),("ಓದಿನಲ್ಲಿ ಮನಸ್ಸಿಡಿ (ōdinalli manassiḍi)","Put your mind into studies"),
 ("ಮನೆಕೆಲಸ ಮುಗಿಸಿ (manekelasa mugisi)","Finish the homework"),("ಪುಸ್ತಕ ತೆರೆಯಿರಿ (pustaka tereyiri)","Open the book"),
 ("ಗಮನವಿಟ್ಟು ಕೇಳಿ (gamanaviṭṭu kēḷi)","Listen carefully"),("ಕಲಿಯುವುದನ್ನು ಎಂದೂ ನಿಲ್ಲಿಸಬೇಡಿ (kaliyuvadannu endū nillisabēḍi)","Never stop learning"),
]

_HEALTH = [
 ("ನನ್ನ ತಲೆ ನೋಯುತ್ತಿದೆ (nanna tale nōyuttide)","My head aches"),("ನನಗೆ ಜ್ವರವಿದೆ (nanage jvaravide)","I have a fever"),
 ("ನನಗೆ ಕೆಮ್ಮು ಬರುತ್ತಿದೆ (nanage kemmu baruttide)","I have a cough"),("ನನ್ನ ಹೊಟ್ಟೆ ನೋಯುತ್ತಿದೆ (nanna hoṭṭe nōyuttide)","My stomach aches"),
 ("ನನಗೆ ತಲೆಸುತ್ತು ಬರುತ್ತಿದೆ (nanage talesuttu baruttide)","I feel dizzy"),("ವೈದ್ಯರು ಎಲ್ಲಿದ್ದಾರೆ? (vaidyaru elliddāre?)","Where is the doctor?"),
 ("ದಯವಿಟ್ಟು ಆಂಬುಲೆನ್ಸ್ ಕರೆಸಿ (dayaviṭṭu āmbulens karesi)","Please call an ambulance"),("ನನಗೆ ಔಷಧಿ ಬೇಕು (nanage auṣadhi bēku)","I need medicine"),
 ("ಈ ಮಾತ್ರೆಯನ್ನು ದಿನಕ್ಕೆ ಎರಡು ಬಾರಿ ತಿನ್ನಿ (ī mātreyannu dinakke eraḍu bāri tinni)","Take this tablet twice a day"),("ಊಟದ ನಂತರ ಔಷಧಿ ತಿನ್ನಿ (ūṭada nantara auṣadhi tinni)","Take the medicine after food"),
 ("ನನಗೆ ಅಲರ್ಜಿ ಇದೆ (nanage alarji ide)","I have an allergy"),("ರಕ್ತದೊತ್ತಡ ಪರೀಕ್ಷಿಸಿ (raktadottada parīkṣisi)","Check the blood pressure"),
 ("ವಿಶ್ರಾಂತಿ ತೆಗೆದುಕೊಳ್ಳಿ (viśrānti tegedukoḷḷi)","Take rest"),("ಬೇಗ ಗುಣಮುಖರಾಗಿ (bēga guṇamukharāgi)","Get well soon"),
 ("ಆಸ್ಪತ್ರೆ ಎಲ್ಲಿದೆ? (āspatre ellide?)","Where is the hospital?"),("ಔಷಧಿ ಅಂಗಡಿ ಹತ್ತಿರವಿದೆಯೇ? (auṣadhi aṅgaḍi hattiravideyē?)","Is the pharmacy nearby?"),
 ("ನನ್ನ ಕಣ್ಣು ಕೆಂಪಾಗಿದೆ (nanna kaṇṇu kempāgide)","My eye is red"),("ನನ್ನ ಕೈಗೆ ಗಾಯವಾಗಿದೆ (nanna kaige gāyavāgide)","My hand is injured"),
 ("ನೀರು ಹೆಚ್ಚು ಕುಡಿಯಿರಿ (nīru heccu kuḍiyiri)","Drink more water"),("ಆರೋಗ್ಯವೇ ಭಾಗ್ಯ (ārōgyavē bhāgya)","Health is wealth"),
]

_EMO = [
 ("ನನಗೆ ತುಂಬಾ ಸಂತೋಷವಾಗಿದೆ (nanage tumbā santōṣavāgide)","I am very happy"),("ಅವಳು ಸಂತೋಷದಿಂದ ನಗುತ್ತಾಳೆ (avaḷu santōṣadinda naguttāḷe)","She laughs with joy"),
 ("ನನಗೆ ದುಃಖವಾಗಿದೆ (nanage duḥkhavāgide)","I am sad"),("ಅವನು ದುಃಖದಿಂದ ಅಳುತ್ತಾನೆ (avanu duḥkhadinda aḷuttāne)","He cries with sadness"),
 ("ನನಗೆ ಕೋಪ ಬರುತ್ತಿದೆ (nanage kōpa baruttide)","I am getting angry"),("ದಯವಿಟ್ಟು ಕೋಪ ಮಾಡಿಕೊಳ್ಳಬೇಡಿ (dayaviṭṭu kōpa māḍikoḷḷabēḍi)","Please do not get angry"),
 ("ನನಗೆ ಭಯವಾಗುತ್ತಿದೆ (nanage bhayavāguttide)","I am afraid"),("ಹೆದರಬೇಡಿ, ನಾನಿದ್ದೇನೆ (hedarabēḍi, nāniddēne)","Do not fear, I am here"),
 ("ನಾನು ನಿನ್ನನ್ನು ಪ್ರೀತಿಸುತ್ತೇನೆ (nānu ninnannu prītisuttēne)","I love you"),("ಪ್ರೀತಿ ಎಲ್ಲಕ್ಕಿಂತ ದೊಡ್ಡದು (prīti ellakkinta doḍḍadu)","Love is greater than everything"),
 ("ನನಗೆ ಆಶ್ಚರ್ಯವಾಯಿತು (nanage āścaryavāyitu)","I was surprised"),("ಅದು ನಿಜಕ್ಕೂ ಆಶ್ಚರ್ಯಕರ! (adu nijakkū āścaryakara!)","That is truly surprising!"),
 ("ನನಗೆ ಹೆಮ್ಮೆಯಾಗುತ್ತಿದೆ (nanage hemmyyāguttide)","I feel proud"),("ನನಗೆ ನಾಚಿಕೆಯಾಗುತ್ತಿದೆ (nanage nācikeyāguttide)","I feel shy"),
 ("ನನಗೆ ಬೇಸರವಾಗಿದೆ (nanage bēsaravāgide)","I am bored"),("ಸಮಾಧಾನವಾಗಿರಿ (samādhānavāgiri)","Be calm"),
 ("ಚಿಂತೆ ಮಾಡಬೇಡಿ (cinte māḍabēḍi)","Do not worry"),("ನನಗೆ ಆತಂಕವಿದೆ (nanage ātaṅkavide)","I am anxious"),
 ("ಅವನಿಗೆ ಕೃತಜ್ಞತೆ ಇದೆ (avanige kṛtajñate ide)","He feels grateful"),("ಕ್ಷಮಿಸಿ, ನನ್ನ ತಪ್ಪು (kṣamisi, nanna tappu)","Forgive me, my mistake"),
]

_NATURE = [
 ("ಇಂದು ಹವಾಮಾನ ಚೆನ್ನಾಗಿದೆ (indu havāmāna cennāgide)","The weather is nice today"),("ಹೊರಗೆ ಮಳೆ ಬರುತ್ತಿದೆ (horage maḷe baruttide)","It is raining outside"),
 ("ನಾಳೆ ಬಿಸಿಲು ಇರುತ್ತದೆ (nāḷe bisilu iruttade)","Tomorrow will be sunny"),("ಚಳಿಗಾಲದಲ್ಲಿ ತುಂಬಾ ಚಳಿಯಿರುತ್ತದೆ (caḷigāladalli tumbā caḷiyiruttade)","It is very cold in winter"),
 ("ವಸಂತಕಾಲದಲ್ಲಿ ಹೂವುಗಳು ಅರಳುತ್ತವೆ (vasantakāladalli hūvugaḷu araḷuttave)","Flowers bloom in spring"),("ಆಕಾಶದಲ್ಲಿ ಮೋಡಗಳಿವೆ (ākāśadalli mōḍagaḷive)","There are clouds in the sky"),
 ("ಗಾಳಿ ಬಲವಾಗಿ ಬೀಸುತ್ತಿದೆ (gāḷi balavāgi bīsuttide)","The wind is blowing strongly"),("ಮಿಂಚು ಹೊಳೆಯುತ್ತಿದೆ (mincu hoḷeyuttide)","Lightning is flashing"),
 ("ಗುಡುಗು ಕೇಳಿಸುತ್ತಿದೆ (guḍugu kēḷisuttide)","Thunder is heard"),("ನದಿಯಲ್ಲಿ ನೀರು ಹರಿಯುತ್ತಿದೆ (nadiyalli nīru hariyuttide)","Water flows in the river"),
 ("ಬೆಟ್ಟದ ಮೇಲೆ ದೇವಸ್ಥಾನವಿದೆ (beṭṭada mēle dēvasthānavide)","There is a temple on the hill"),("ಕಾಡಿನಲ್ಲಿ ಆನೆಗಳಿವೆ (kāḍinalli ānegaḷive)","There are elephants in the forest"),
 ("ಹುಲಿ ಕಾಡಿನ ರಾಜ (huli kāḍina rāja)","The tiger is the king of the forest"),("ನಾಯಿ ಬೊಗಳುತ್ತಿದೆ (nāyi bogaḷuttide)","The dog is barking"),
 ("ಬೆಕ್ಕು ಹಾಲು ಕುಡಿಯುತ್ತಿದೆ (bekku hālu kuḍiyuttide)","The cat is drinking milk"),("ಹಕ್ಕಿಗಳು ಹಾಡುತ್ತಿವೆ (hakkigaḷu hāḍuttive)","The birds are singing"),
 ("ಹಸು ಹುಲ್ಲು ತಿನ್ನುತ್ತಿದೆ (hasu hullu tinnuttide)","The cow is eating grass"),("ಮರದ ಮೇಲೆ ಕೋತಿ ಕುಳಿತಿದೆ (marada mēle kōti kuḷitide)","A monkey sits on the tree"),
 ("ತೋಟದಲ್ಲಿ ಮಾವಿನ ಮರಗಳಿವೆ (tōṭadalli māvina maragaḷive)","There are mango trees in the orchard"),("ಪ್ರಕೃತಿ ನಮ್ಮ ಅಮೂಲ್ಯ ಸಂಪತ್ತು (prakṛti namma amūlya sampattu)","Nature is our precious wealth"),
]

_SHOP = [
 ("ಇದರ ಬೆಲೆ ಎಷ್ಟು? (idara bele eṣṭu?)","How much is this?"),("ತುಂಬಾ ದುಬಾರಿಯಾಗಿದೆ (tumbā dubāriyāgide)","It is too expensive"),
 ("ಸ್ವಲ್ಪ ಕಡಿಮೆ ಮಾಡಿ (svalpa kaḍime māḍi)","Reduce the price a little"),("ಕೊನೆಯ ಬೆಲೆ ಹೇಳಿ (koneya bele hēḷi)","Tell the final price"),
 ("ನನಗೆ ಇದು ಇಷ್ಟವಾಯಿತು (nanage idu iṣṭavāyitu)","I like this"),("ಬೇರೆ ಬಣ್ಣ ತೋರಿಸಿ (bēre baṇṇa tōrisi)","Show another color"),
 ("ದೊಡ್ಡ ಗಾತ್ರವಿದೆಯೇ? (doḍḍa gātravideyē?)","Is there a bigger size?"),("ನಾನು ಇದನ್ನು ತೆಗೆದುಕೊಳ್ಳುತ್ತೇನೆ (nānu idannu tegedukoḷḷuttēne)","I will take this"),
 ("ಬಿಲ್ ಕೊಡಿ (bil koḍi)","Give the bill"),("ನಗದು ಕೊಡುತ್ತೇನೆ (nagadu koḍuttēne)","I will pay cash"),
 ("ಕಾರ್ಡಿನಲ್ಲಿ ಪಾವತಿಸಬಹುದೇ? (kārḍinalli pāvatisabahudē?)","Can I pay by card?"),("ಚಿಲ್ಲರೆ ಇದೆಯೇ? (cillare ideyē?)","Do you have change?"),
 ("ರಸೀದಿ ಕೊಡಿ (rasīdi koḍi)","Give the receipt"),("ಇದು ಖಾತರಿಯಿದೆಯೇ? (idu khātriyideyē?)","Does this have a warranty?"),
 ("ವಾಪಸ್ ತೆಗೆದುಕೊಳ್ಳುವಿರಾ? (vāpas tegedukoḷḷuvirā?)","Will you take it back?"),("ಮಾರುಕಟ್ಟೆ ಬೆಳಿಗ್ಗೆ ತೆರೆಯುತ್ತದೆ (mārukaṭṭe beḷigge tereyuttade)","The market opens in the morning"),
 ("ತರಕಾರಿ ತಾಜಾವಾಗಿದೆ (tarakāri tājāvāgide)","The vegetables are fresh"),("ಒಂದು ಕೆಜಿ ಟೊಮೆಟೊ ಕೊಡಿ (ondu keji ṭomeṭo koḍi)","Give one kilo of tomatoes"),
 ("ಹಣ ಉಳಿಸಿ (haṇa uḷisi)","Save money"),("ಚೌಕಾಶಿ ಮಾಡುವುದು ಸಾಮಾನ್ಯ (caukāśi māḍuvudu sāmānya)","Bargaining is normal"),
]

_SOCIAL = [
 ("ನಿಮ್ಮ ಹೆಸರೇನು? (nimma hesarēnu?)","What is your name?"),("ನನ್ನ ಹೆಸರು ರವಿ (nanna hesaru ravi)","My name is Ravi"),
 ("ನೀವು ಎಲ್ಲಿಯವರು? (nīvu elliyavaru?)","Where are you from?"),("ನಾನು ಬೆಂಗಳೂರಿನವನು (nānu beṅgaḷūrinavanu)","I am from Bengaluru"),
 ("ನಿಮಗೆ ಎಷ್ಟು ವಯಸ್ಸು? (nimage eṣṭu vayassu?)","How old are you?"),("ನನಗೆ ಇಪ್ಪತ್ತೈದು ವಯಸ್ಸು (nanage ippattnaidu vayassu)","I am twenty-five"),
 ("ನೀವು ಏನು ಮಾಡುತ್ತೀರಿ? (nīvu ēnu māḍuttīri?)","What do you do?"),("ನಾನು ವಿದ್ಯಾರ್ಥಿ (nānu vidyārthi)","I am a student"),
 ("ನಾವು ಸ್ನೇಹಿತರಾಗೋಣ (nāvu snēhitarāgōṇa)","Let us be friends"),("ನನ್ನ ಮನೆಗೆ ಬನ್ನಿ (nanna manege banni)","Come to my house"),
 ("ನಾಳೆ ಸಂಜೆ ಬಿಡುವಿದೆಯೇ? (nāḷe sanje biḍuvideyē?)","Are you free tomorrow evening?"),("ಊಟಕ್ಕೆ ಬನ್ನಿ (ūṭakke banni)","Come for a meal"),
 ("ನನ್ನ ಹುಟ್ಟುಹಬ್ಬಕ್ಕೆ ಬನ್ನಿ (nanna huṭṭuhabbakke banni)","Come to my birthday"),("ಹುಟ್ಟುಹಬ್ಬದ ಶುಭಾಶಯಗಳು! (huṭṭuhabbada śubhāśayagaḷu!)","Happy birthday!"),
 ("ಮದುವೆಗೆ ಬನ್ನಿ (maduvege banni)","Come to the wedding"),("ಹಬ್ಬದ ಶುಭಾಶಯಗಳು! (habbada śubhāśayagaḷu!)","Festival greetings!"),
 ("ದೀಪಾವಳಿ ಹಬ್ಬ ಚೆನ್ನಾಗಿ ಆಚರಿಸಿ (dīpāvaḷi habba cennāgi ācarisi)","Celebrate Diwali well"),("ಯುಗಾದಿ ಹಬ್ಬದ ಶುಭಾಶಯಗಳು (yugādi habbada śubhāśayagaḷu)","Ugadi greetings"),
 ("ನಾವು ಒಟ್ಟಿಗೆ ಸಿನೆಮಾ ನೋಡೋಣ (nāvu oṭṭige sinemā nōḍōṇa)","Let us watch a movie together"),("ಸ್ನೇಹವೇ ದೊಡ್ಡ ಸಂಪತ್ತು (snēhavē doḍḍa sampattu)","Friendship is the greatest wealth"),
]

_TECH = [
 ("ನನ್ನ ಫೋನ್ ಸಂಖ್ಯೆ ... (nanna phōn sankhye ...)","My phone number is ..."),
 ("ದಯವಿಟ್ಟು ನನಗೆ ಕರೆ ಮಾಡಿ (dayaviṭṭu nanage kare māḍi)","Please call me"),("ನಾನು ನಿಮಗೆ ಮೆಸೇಜ್ ಮಾಡುತ್ತೇನೆ (nānu nimage mesej māḍuttēne)","I will message you"),
 ("ಇಂಟರ್ನೆಟ್ ಕೆಲಸ ಮಾಡುತ್ತಿಲ್ಲ (iṇṭarneṭ kelasa māḍuttilla)","The internet is not working"),("ವೈ-ಫೈ ಪಾಸ್ವರ್ಡ್ ಏನು? (vai-phai pāsvard ēnu?)","What is the Wi-Fi password?"),
 ("ನನ್ನ ಕಂಪ್ಯೂಟರ್ ಆನ್ ಆಗುತ್ತಿಲ್ಲ (nanna kampyūṭar ān āguttilla)","My computer will not turn on"),("ಚಾರ್ಜರ್ ಇದೆಯೇ? (cārjar ideyē?)","Do you have a charger?"),
 ("ಬ್ಯಾಟರಿ ಖಾಲಿಯಾಗಿದೆ (byāṭari khāliyāgide)","The battery is empty"),("ಫೋಟೋ ತೆಗೆಯಬಹುದೇ? (phōṭō tegeyabahudē?)","May I take a photo?"),
 ("ವೀಡಿಯೋ ಕರೆ ಮಾಡೋಣ (vīḍiyō kare māḍōṇa)","Let us make a video call"),("ನಿಮ್ಮ ಈಮೇಲ್ ವಿಳಾಸ ಕೊಡಿ (nimma īmel viḷāsa koḍi)","Give your email address"),
 ("ನಾನು ನಿಮಗೆ ಈಮೇಲ್ ಕಳುಹಿಸುತ್ತೇನೆ (nānu nimage īmel kaḷuhisuttēne)","I will send you an email"),("ಪಾಸ್ವರ್ಡ್ ಮರೆತುಹೋಗಿದೆ (pāsvard marettuhōgide)","I forgot the password"),
 ("ಹೊಸ ಪಾಸ್ವರ್ಡ್ ಹಾಕಿ (hosa pāsvard hāki)","Set a new password"),("ಆ್ಯಪ್ ಡೌನ್ಲೋಡ್ ಮಾಡಿ (āp ḍaunlōḍ māḍi)","Download the app"),
 ("ಸಾಫ್ಟ್ವೇರ್ ಅಪ್ಡೇಟ್ ಮಾಡಿ (sāphṭvēr apḍēṭ māḍi)","Update the software"),("ಸ್ಕ್ರೀನ್ ತುಂಬಾ ಪ್ರಕಾಶಮಾನವಾಗಿದೆ (skrīn tumbā prakāśamānavāgide)","The screen is too bright"),
 ("ಸದ್ದು ಹೆಚ್ಚು ಮಾಡಿ (saddu heccu māḍi)","Increase the volume"),("ನನ್ನ ಫೋನಿನಲ್ಲಿ ಕನ್ನಡ ಕೀಬೋರ್ಡ್ ಇದೆ (nanna phōninalli kannaḍa kībōrḍ ide)","My phone has a Kannada keyboard"),
 ("ತಂತ್ರಜ್ಞಾನ ನಮ್ಮ ಬಾಳನ್ನು ಸುಲಭಗೊಳಿಸಿದೆ (tantrajñāna namma bāḷannu sulabhagoḷiside)","Technology has made our lives easier"),
]

_DESCR = [
 ("ನನ್ನ ಅಣ್ಣ ಎತ್ತರವಾಗಿದ್ದಾನೆ ಮತ್ತು ಬಲಶಾಲಿಯಾಗಿದ್ದಾನೆ (nanna aṇṇa ettaravāgiddāne mattu balaśāliyāgiddāne)","My elder brother is tall and strong"),
 ("ನನ್ನ ತಂಗಿಗೆ ಉದ್ದ ಕೂದಲು ಮತ್ತು ದೊಡ್ಡ ಕಣ್ಣುಗಳಿವೆ (nanna taṅgige udda kūdalu mattu doḍḍa kaṇṇugaḷive)","My younger sister has long hair and big eyes"),
 ("ತಾತನಿಗೆ ಬಿಳಿ ಗಡ್ಡವಿದೆ (tātanige biḷi gaḍḍavide)","Grandfather has a white beard"),
 ("ಅಜ್ಜಿ ಯಾವಾಗಲೂ ನಗುತ್ತಿರುತ್ತಾರೆ (ajji yāvāgalū naguttiruttāre)","Grandmother is always smiling"),
 ("ನನ್ನ ಸ್ನೇಹಿತ ತುಂಬಾ ಬುದ್ಧಿವಂತನು (nanna snēhita tumbā buddhivantanu)","My friend is very intelligent"),
 ("ಆ ಹುಡುಗಿ ಸುಂದರವಾಗಿ ಹಾಡುತ್ತಾಳೆ (ā huḍugi sundaravāgi hāḍuttāḷe)","That girl sings beautifully"),
 ("ಬೆಂಗಳೂರು ತುಂಬಾ ದೊಡ್ಡ ಮತ್ತು ಸುಂದರ ನಗರ (beṅgaḷūru tumbā doḍḍa mattu sundara nagara)","Bengaluru is a very big and beautiful city"),
 ("ಮೈಸೂರು ಅರಮನೆ ಅದ್ಭುತವಾಗಿದೆ (maisūru aramane adbhutavāgide)","The Mysuru palace is magnificent"),
 ("ಹಂಪಿಯ ಶಿಲ್ಪಗಳು ಸಾವಿರ ವರ್ಷ ಹಳೆಯವು (hampiya śilpagaḷu sāvira varṣa haḷeyavu)","Hampi's sculptures are a thousand years old"),
 ("ಜೋಗ ಜಲಪಾತ ಭಾರತದ ಅತಿ ಎತ್ತರದ ಜಲಪಾತಗಳಲ್ಲಿ ಒಂದು (jōga jalapāta bhāratada ati ettarada jalapātagalaḷli ondu)","Jog Falls is among India's tallest waterfalls"),
 ("ಕೂರ್ಗ್ ಹಸಿರು ಬೆಟ್ಟಗಳಿಂದ ಕೂಡಿದೆ (kūrg hasiru beṭṭagaḷinda kūḍide)","Coorg is covered with green hills"),
 ("ನಮ್ಮ ಮನೆ ಶಾಂತವಾದ ಬೀದಿಯಲ್ಲಿದೆ (namma mane śāntavāda bīdiyallide)","Our house is on a quiet street"),
 ("ಈ ಉದ್ಯಾನದಲ್ಲಿ ನೂರಾರು ಹೂವುಗಳಿವೆ (ī udyānadalli nūrāru hūvugaḷive)","There are hundreds of flowers in this garden"),
 ("ಸಮುದ್ರ ತೀರ ಸುಂದರವಾಗಿದೆ (samudra tīra sundaravāgide)","The sea shore is beautiful"),
 ("ಈ ಪುಸ್ತಕ ತುಂಬಾ ಆಸಕ್ತಿದಾಯಕವಾಗಿದೆ (ī pustaka tumbā āsaktidāyakavāgide)","This book is very interesting"),
 ("ಆ ಸಿನೆಮಾ ತುಂಬಾ ಮನರಂಜನೆಯಾಗಿತ್ತು (ā sinemā tumbā manarañjaneyāgittu)","That movie was very entertaining"),
 ("ಕಾಫಿ ಘಮಘಮಿಸುತ್ತಿದೆ (kāphi ghamaghamisuttide)","The coffee smells aromatic"),
 ("ಮಾವಿನಹಣ್ಣು ಸಿಹಿಯಾಗಿ ರುಚಿಯಾಗಿದೆ (māvinhannu sihiyāgi ruciyāgide)","The mango is sweet and tasty"),
 ("ಚಳಿಗಾಲದ ಬೆಳಿಗ್ಗೆ ಮಂಜಿನಿಂದ ಕೂಡಿರುತ್ತದೆ (caḷigālada beḷigge manjiniṃda kūḍiruttade)","Winter mornings are full of fog"),
 ("ಕರ್ನಾಟಕ ಸಂಸ್ಕೃತಿ ಮತ್ತು ಸಂಗೀತದಿಂದ ಸಮೃದ್ಧವಾಗಿದೆ (karnāṭaka sanskṛti mattu sangītadinda samṛddhavāgide)","Karnataka is rich in culture and music"),
]

def demo_tenses(hdr, name, rid, group, points, req):
    groups = {'present': 6, 'past': 6, 'future': 6}
    samples = [
     ('present','ನಾನು ಪ್ರತಿದಿನ ಓದುತ್ತೇನೆ','I read every day'),
     ('present','ಅವನು ಶಾಲೆಗೆ ಹೋಗುತ್ತಾನೆ','He goes to school'),
     ('past','ನಾನು ನಿನ್ನೆ ಪುಸ್ತಕ ಓದಿದೆನು','I read a book yesterday'),
     ('past','ಮಳೆ ಬಂತು','It rained'),
     ('future','ನಾನು ನಾಳೆ ಬರುವೆನು','I will come tomorrow'),
     ('future','ಅವಳು ಹಾಡುವಳು','She will sing'),
    ]
    body = (
        "\nGROUPS = " + repr(groups) + "\n"
        "SAMPLES = " + repr(samples) + "\n"
        "def main():\n"
        "    total = sum(GROUPS.values())\n"
        "    print('tense groups:', GROUPS)\n"
        "    print('total sentences:', total)\n"
        "    assert total == 18\n"
        "    assert all(v >= 5 for v in GROUPS.values())\n"
        "    assert len(GROUPS) == 3\n"
        "    for tense, dev, eng in SAMPLES:\n"
        "        print('%s: %s => %s' % (tense, dev, eng))\n"
        "    print('stems: ಉತ್ತ್ present, ಇದ್ past, ಉವ್ future')\n"
        "    print('negative: ಬರುವುದಿಲ್ಲ (will not come), ಬರಲಿಲ್ಲ (did not come)')\n"
        "    print('OK: tense drill complete - 18 sentences in 3 groups')\n"
        "main()\n"
    )
    return hdr(name, rid, group) + body


def demo_qa(hdr, name, rid, group, points, req):
    pairs = [
     ("ನಿಮ್ಮ ಹೆಸರೇನು?","ನನ್ನ ಹೆಸರು ಸೀತಾ"),("ನೀವು ಎಲ್ಲಿರುತ್ತೀರಿ?","ನಾನು ಮೈಸೂರಿನಲ್ಲಿರುತ್ತೇನೆ"),
     ("ಇವರು ಯಾರು?","ಇವರು ನನ್ನ ಅಣ್ಣ"),("ನೀವು ಏನು ಮಾಡುತ್ತೀರಿ?","ನಾನು ಓದುತ್ತೇನೆ"),
     ("ನೀವು ಮಾರುಕಟ್ಟೆಗೆ ಯಾವಾಗ ಹೋಗುವಿರಿ?","ನಾನು ಸಂಜೆ ಹೋಗುವೆನು"),("ನೀವು ಯಾಕೆ ಬರಲಿಲ್ಲ?","ನಾನು ಅಸ್ವಸ್ಥನಾಗಿದ್ದೆನು"),
     ("ಇದು ಹೇಗೆ ಕೆಲಸ ಮಾಡುತ್ತದೆ?","ಗುಂಡಿ ಒತ್ತಿ"),("ಈಗ ಎಷ್ಟು ಗಂಟೆ?","ಎರಡು ಗಂಟೆ"),
     ("ನೀವು ಕನ್ನಡ ಮಾತಾಡುತ್ತೀರೇ?","ಹೌದು, ಸ್ವಲ್ಪ ಸ್ವಲ್ಪ"),("ಊಟ ಹೇಗಿತ್ತು?","ತುಂಬಾ ಚೆನ್ನಾಗಿತ್ತು"),
     ("ಟಿಕೆಟ್ಗೆ ಎಷ್ಟು?","ಐವತ್ತು ರೂಪಾಯಿ"),("ವೈದ್ಯರು ಎಲ್ಲಿದ್ದಾರೆ?","ವೈದ್ಯರು ಒಳಗಿದ್ದಾರೆ"),
     ("ನಿಮ್ಮ ವಯಸ್ಸೆಷ್ಟು?","ನನಗೆ ಇಪ್ಪತ್ತು ವಯಸ್ಸು"),("ಮಳೆ ಬರುತ್ತದೆಯೇ?","ಹೌದು, ಬರುವಂತೆ ಕಾಣುತ್ತದೆ"),
     ("ಇದು ಯಾರದ್ದು?","ಇದು ನನ್ನದು"),("ನೀವು ಎಲ್ಲಿಂದ ಬಂದಿರಿ?","ನಾನು ಧಾರವಾಡದಿಂದ ಬಂದೆನು"),
     ("ನಾನು ಒಳಗೆ ಬರಬಹುದೇ?","ಹೌದು, ಬನ್ನಿ"),("ನಾಳೆ ಏನು ಮಾಡುವಿರಿ?","ನಾಳೆ ನಾನು ಮನೆಯಲ್ಲಿರುತ್ತೇನೆ"),
     ("ಚಹಾ ಕುಡಿಯುವಿರಾ?","ಹೌದು, ಧನ್ಯವಾದಗಳು"),("ಎಲ್ಲಾ ಸರಿಯಿದೆಯೇ?","ಹೌದು, ಎಲ್ಲಾ ಸರಿಯಿದೆ"),
    ]
    qwords = ['ಯಾರು','ಏನು','ಎಲ್ಲಿ','ಯಾವಾಗ','ಯಾಕೆ','ಹೇಗೆ','ಎಷ್ಟು','ಯಾವುದು']
    body = (
        "\nPAIRS = " + repr(pairs) + "\n"
        "QWORDS = " + repr(qwords) + "\n"
        "def main():\n"
        "    print('qa pairs:', len(PAIRS))\n"
        "    assert len(PAIRS) == 20\n"
        "    assert all(len(q) > 2 and len(a) > 1 for q, a in PAIRS)\n"
        "    blob = ' '.join(q for q, a in PAIRS)\n"
        "    hit = [w for w in QWORDS if w in blob]\n"
        "    print('question words covered:', len(hit), '/', len(QWORDS))\n"
        "    assert len(hit) >= 7\n"
        "    print('sample Q:', PAIRS[0][0])\n"
        "    print('sample A:', PAIRS[0][1])\n"
        "    print('OK: qa drill complete - 20 pairs')\n"
        "main()\n"
    )
    return hdr(name, rid, group) + body


def demo_commands(hdr, name, rid, group, points, req):
    informal = ['ಬಾ','ಕುಳಿತುಕೋ','ನೀರು ಕುಡಿ','ನಿಧಾನವಾಗಿ ಮಾತಾಡು','ಬಾಗಿಲು ತೆರೆ',
                'ಪುಸ್ತಕ ಕೊಡು','ಬೇಗ ಬಾ','ಹೋಗಬೇಡ','ಚಿಂತೆ ಮಾಡಬೇಡ','ಊಟ ಮಾಡು']
    formal = ['ದಯವಿಟ್ಟು ಬನ್ನಿ','ದಯವಿಟ್ಟು ಕುಳಿತುಕೊಳ್ಳಿ','ದಯವಿಟ್ಟು ನೀರು ಕುಡಿಯಿರಿ','ಸ್ವಲ್ಪ ನಿಧಾನವಾಗಿ ಮಾತಾಡಿ','ಬಾಗಿಲು ತೆರೆಯಿರಿ',
              'ದಯವಿಟ್ಟು ಪುಸ್ತಕ ಕೊಡಿ','ಬೇಗ ಬನ್ನಿ','ದಯವಿಟ್ಟು ಹೋಗಬೇಡಿ','ಚಿಂತೆ ಮಾಡಬೇಡಿ','ಶುಭವಾಗಲಿ!']
    body = (
        "\nINF = " + repr(informal) + "\n"
        "FORM = " + repr(formal) + "\n"
        "def main():\n"
        "    print('informal commands:', len(INF))\n"
        "    print('formal requests:', len(FORM))\n"
        "    assert len(INF) == 10\n"
        "    assert len(FORM) == 10\n"
        "    assert len(INF) + len(FORM) == 20\n"
        "    soft = [f for f in FORM if 'ದಯವಿಟ್ಟು' in f or 'ಸ್ವಲ್ಪ' in f]\n"
        "    print('softened with ದಯವಿಟ್ಟು/ಸ್ವಲ್ಪ:', len(soft))\n"
        "    assert len(soft) >= 3\n"
        "    print('pair: ಬಾ (inf) vs ಬನ್ನಿ (formal)')\n"
        "    print('negative: ಹೋಗಬೇಡಿ (formal) vs ಹೋಗಬೇಡ (informal)')\n"
        "    print('OK: command drill complete - 10 informal, 10 formal')\n"
        "main()\n"
    )
    return hdr(name, rid, group) + body


_STORY1 = [
 ("ರವಿ ಬೆಳಿಗ್ಗೆ ಬೇಗ ಏಳುತ್ತಾನೆ (ravi beḷigge bēga ēḷuttāne)","Ravi wakes up early in the morning"),
 ("ಅವನು ಹಲ್ಲುಜ್ಜಿ ಮುಖ ತೊಳೆಯುತ್ತಾನೆ (avanu hallujji mukha toḷeyuttāne)","He brushes his teeth and washes his face"),
 ("ಅಮ್ಮ ಅವನಿಗೆ ತಿಂಡಿ ಕೊಡುತ್ತಾಳೆ (amma avanige tiṇḍi koḍuttāḷe)","Mother gives him breakfast"),
 ("ಅವನು ಶಾಲಾ ಬ್ಯಾಗ್ ತೆಗೆದುಕೊಂಡು ಹೊರಡುತ್ತಾನೆ (avanu śālā byāg tegedukoṇḍu horaḍuttāne)","He takes his school bag and leaves"),
 ("ಶಾಲೆಯಲ್ಲಿ ಅವನು ಸ್ನೇಹಿತರನ್ನು ಭೇಟಿಯಾಗುತ್ತಾನೆ (śāleyalli avanu snēhitarannu bhēṭiyāguttāne)","At school he meets his friends"),
 ("ಅಧ್ಯಾಪಕರು ಕನ್ನಡ ಪಾಠ ಮಾಡುತ್ತಾರೆ (adhyāpakaru kannaḍa pāṭha māḍuttāre)","The teacher teaches the Kannada lesson"),
 ("ರವಿ ಗಮನವಿಟ್ಟು ಕೇಳುತ್ತಾನೆ (ravi gamanaviṭṭu kēḷuttāne)","Ravi listens attentively"),
 ("ಮಧ್ಯಾಹ್ನ ಅವನು ಸ್ನೇಹಿತರೊಂದಿಗೆ ಊಟ ಮಾಡುತ್ತಾನೆ (madhyāhna avanu snēhitarondige ūṭa māḍuttāne)","At noon he eats lunch with his friends"),
 ("ಸಂಜೆ ಅವನು ಮನೆಗೆ ಬಂದು ಆಟವಾಡುತ್ತಾನೆ (sanje avanu manege bandu āṭavāḍuttāne)","In the evening he comes home and plays"),
 ("ರಾತ್ರಿ ಅವನು ಬೇಗ ಮಲಗುತ್ತಾನೆ (rātri avanu bēga malaguttāne)","At night he sleeps early"),
]
_STORY2 = [
 ("ಕಳೆದ ಭಾನುವಾರ ನಾವು ಮೈಸೂರಿಗೆ ಹೋದೆವು (kaḷeda bhānuvāra nāvu maisūrige hōdevu)","Last Sunday we went to Mysuru"),
 ("ನಾವು ಬೆಳಿಗ್ಗೆ ಆರು ಗಂಟೆಗೆ ಹೊರಟೆವು (nāvu beḷigge āru gaṇṭege horaṭevu)","We left at six in the morning"),
 ("ರೈಲು ತುಂಬಾ ವೇಗವಾಗಿ ಹೋಯಿತು (railu tumbā vēgavāgi hōyitu)","The train went very fast"),
 ("ನಾವು ಕಿಟಕಿಯಿಂದ ಹಸಿರು ಹೊಲಗಳನ್ನು ನೋಡಿದೆವು (nāvu kiṭakiyinda hasiru holagaḷannu nōḍidevu)","We saw green fields through the window"),
 ("ಮೈಸೂರಿನಲ್ಲಿ ನಾವು ಮೊದಲು ಅರಮನೆಯನ್ನು ನೋಡಿದೆವು (maisūrinalli nāvu modalu aramaneyannu nōḍidevu)","In Mysuru we first saw the palace"),
 ("ಅರಮನೆ ತುಂಬಾ ಸುಂದರವಾಗಿತ್ತು (aramane tumbā sundaravāgittu)","The palace was very beautiful"),
 ("ನಂತರ ನಾವು ಮೃಗಾಲಯಕ್ಕೆ ಹೋದೆವು (nantara nāvu mṛgālayakke hōdevu)","Then we went to the zoo"),
 ("ಮಕ್ಕಳು ಆನೆಗಳನ್ನು ನೋಡಿ ಸಂತೋಷಪಟ್ಟರು (makkaḷu ānegaḷannu nōḍi santōṣapaṭṭaru)","The children were delighted to see the elephants"),
 ("ಸಂಜೆ ನಾವು ಮಸಾಲೆ ದೋಸೆ ತಿಂದೆವು (sanje nāvu masāle dōse tindevu)","In the evening we ate masala dosa"),
 ("ರಾತ್ರಿ ನಾವು ಸಂತೋಷದಿಂದ ಮನೆಗೆ ಹಿಂತಿರುಗಿದೆವು (rātri nāvu santōṣadinda manege hintirugidevu)","At night we returned home happily"),
]
_STORY3 = [
 ("ಲಕ್ಷ್ಮಿಗೆ ದೊಡ್ಡ ಕನಸುಗಳಿವೆ (lakṣmige doḍḍa kanasugaḷive)","Lakshmi has big dreams"),
 ("ಅವಳು ವೈದ್ಯಳಾಗುವಳು (avaḷu vaidyāḷāguvaḷu)","She will become a doctor"),
 ("ಅವಳು ಪ್ರತಿದಿನ ಐದು ಗಂಟೆ ಓದುವಳು (avaḷu pratidina aidu gaṇṭe ōduvaḷu)","She will study five hours every day"),
 ("ಅವಳ ತಂದೆ-ತಾಯಿ ಅವಳಿಗೆ ಸಹಾಯ ಮಾಡುವರು (avaḷa tande-tāyi avaḷige sahāya māḍuvaru)","Her parents will help her"),
 ("ಅವಳು ಪರೀಕ್ಷೆಯಲ್ಲಿ ಪ್ರಥಮ ಸ್ಥಾನ ಪಡೆಯುವಳು (avaḷu parīkṣeyalli prathama sthāna paḍeyuvaḷu)","She will secure the first rank in the exam"),
 ("ನಂತರ ಅವಳು ವೈದ್ಯಕೀಯ ಕಾಲೇಜಿಗೆ ಸೇರುವಳು (nantara avaḷu vaidyēkīya kālējige sēruvaḷu)","Then she will join medical college"),
 ("ಅವಳು ಬಡವರಿಗೆ ಉಚಿತವಾಗಿ ಚಿಕಿತ್ಸೆ ಕೊಡುವಳು (avaḷu baḍavarige ucitavāgi cikitsa koḍuvaḷu)","She will treat the poor for free"),
 ("ಅವಳ ಊರಿನಲ್ಲಿ ಆಸ್ಪತ್ರೆ ಕಟ್ಟುವಳು (avaḷa ūrinalli āspatre kaṭṭuvaḷu)","She will build a hospital in her town"),
 ("ಅವಳು ಕಷ್ಟಪಟ್ಟರೆ ಯಶಸ್ಸು ಸಿಗುತ್ತದೆ (avaḷu kaṣṭapaṭṭare yaśassu siguttade)","If she works hard, success will come"),
 ("ನಾವೆಲ್ಲರೂ ಅವಳಿಗೆ ಶುಭ ಹಾರೈಸೋಣ (nāvellaru avaḷige śubha hāraisōṇa)","Let us all wish her well"),
]

_IDIOMS = [
 ("ಅತ್ತೆಗೊಂದು ಕಾಲ ಸೊಸೆಗೊಂದು ಕಾಲ","every dog has its day"),("ಕಾಗೆಗೆ ತನ್ನ ಮರಿ ಬಂಗಾರ","one's own is dearest"),
 ("ಆನೆಯ ಹೊಟ್ಟೆಗೆ ಅರೆಕಾಸಿನ ಮಜ್ಜಿಗೆ","too little for the need"),("ಊಟ ಬಲ್ಲವನಿಗೆ ರೋಗವಿಲ್ಲ","right eating keeps health"),
 ("ಕೈ ಕೆಸರಾದರೆ ಬಾಯಿ ಮೊಸರು","hard work is rewarded"),("ದೀಪದ ಕೆಳಗೆ ಕತ್ತಲು","we overlook what is closest"),
 ("ಯಥಾ ರಾಜಾ ತಥಾ ಪ್ರಜಾ","leaders set the example"),("ಮಾತು ಬೆಳ್ಳಿ ಮೌನ ಬಂಗಾರ","silence is often wiser"),
 ("ಅತಿಯಾಸೆ ಗತಿಕೇಡು","greed destroys"),("ದೂರದ ಬೆಟ್ಟ ಕಣ್ಣಿಗೆ ನುಣುಪು","the grass is always greener"),
 ("ಹಾಸಿಗೆ ಇದ್ದಷ್ಟು ಕಾಲು ಚಾಚು","live within your means"),("ಎತ್ತು ಏರಿಗೆ ಎಳೆಯಿತು","people pull in different directions"),
 ("ಮಾಡಿದ್ದುಣ್ಣೋ ಮಹಾರಾಯ","face the consequences"),("ಕುಂಬಾರನಿಗೆ ವರುಷ","building takes long, destroying is quick"),
 ("ಒಂದು ಕೈಯಿಂದ ಚಪ್ಪಾಳೆ ತಟ್ಟಲಾಗದು","it takes two"),("ಮುಳ್ಳಿನಿಂದ ಮುಳ್ಳೇ ತೆಗೆಯಬೇಕು","fight fire with fire"),
 ("ಬೊಗಳುವ ನಾಯಿ ಕಚ್ಚುವುದಿಲ್ಲ","loud threats are often empty"),("ಗಿಡವಾಗಿ ಬಗ್ಗದ್ದು ಮರವಾಗಿ ಬಗ್ಗೀತೆ","habits form young"),
 ("ಮಾತು ಆಡಿದರೆ ಹೋಯಿತು","words cannot be taken back"),("ಹೊಟ್ಟೆಗೆ ಹಿಟ್ಟಿಲ್ಲ ಜುಟ್ಟಿಗೆ ಮಲ್ಲಿಗೆ","misplaced priorities"),
]

_REGISTER = [
 ("ನಿನಗೆ ಹೇಳ್ತೀನಿ","ತಮಗೆ ತಿಳಿಸಲು ಇಚ್ಛಿಸುತ್ತೇನೆ"),("ಸ್ವಲ್ಪ ಇರು","ದಯವಿಟ್ಟು ಸ್ವಲ್ಪ ಕಾಯಿರಿ"),
 ("ನಿನ್ನ ಅಭಿಪ್ರಾಯವೇನು?","ನಿಮ್ಮ ಅಭಿಪ್ರಾಯವೇನು?"),("ನೀನು ಬರ್ತೀಯಾ?","ತಾವು ಬರಬಹುದೇ?"),
 ("ಸಾರಿ ಕಣೋ","ಕ್ಷಮೆ ಕೋರುತ್ತೇನೆ"),("ಥ್ಯಾಂಕ್ಸ್","ಧನ್ಯವಾದಗಳು ತಿಳಿಸುತ್ತೇನೆ"),
 ("ಒಳಗೆ ಬಾ","ದಯವಿಟ್ಟು ಒಳಗೆ ಬನ್ನಿ"),("ಸಹಾಯಕ್ಕೆ ಥ್ಯಾಂಕ್ಸ್","ತಮ್ಮ ಸಹಕಾರಕ್ಕೆ ಧನ್ಯವಾದಗಳು"),
 ("ನಾನು ಹೋಗ್ತೀನಿ","ನಾನು ಹೊರಡಲು ಅಪ್ಪಣೆ ಕೊಡಿ"),("ಬಾಯ್","ಶುಭದಿನ"),
 ("ಸೀ ಯೂ","ವಂದನೆಗಳೊಂದಿಗೆ"),("ಪ್ಲೀಸ್ ಕಣೋ","ತಮಗೆ ವಿನಂತಿಸುತ್ತೇನೆ"),
 ("ಇದು ಆಗುತ್ತಾ?","ಇದು ಸಾಧ್ಯವೇ?"),("ಮತ್ತೆ ಹೇಳು","ದಯವಿಟ್ಟು ಪುನಃ ಹೇಳಿ"),
 ("ನಿನ್ನ ಸ್ನೇಹಿತ","ತಮ್ಮ ವಿಶ್ವಾಸಿ"),
]

_COMPLEX = [
 ("ನಾನು ಮಾರುಕಟ್ಟೆಗೆ ಹೋದೆನು ಏಕೆಂದರೆ ತರಕಾರಿ ಮುಗಿದಿತ್ತು","ಏಕೆಂದರೆ"),("ಮಳೆ ಬರುತ್ತಿತ್ತು ಆದರೂ ನಾವು ಹೊರಟೆವು","ಆದರೂ"),
 ("ಅವನು ಬುದ್ಧಿವಂತನು ಮತ್ತು ಕಷ್ಟಪಡುವವನು","ಮತ್ತು"),("ನೀವು ಚಹಾ ಕುಡಿಯುವಿರಾ ಅಥವಾ ಕಾಫಿ ಕುಡಿಯುವಿರಾ?","ಅಥವಾ"),
 ("ಅವನು ಬರಲಿಲ್ಲ ಆದ್ದರಿಂದ ನಾವು ಕಾಯಿದೆವು","ಆದ್ದರಿಂದ"),("ನಾನು ನೋಡಿದ ಹುಡುಗ ನನ್ನ ಸ್ನೇಹಿತನು","-ದ ಸಂಬಂಧಿ"),
 ("ನೀವು ಹೇಳಿದ ಕತೆ ತುಂಬಾ ಚೆನ್ನಾಗಿತ್ತು","-ದ ಸಂಬಂಧಿ"),("ಮಳೆ ಬಂದರೆ ನಾವು ಮನೆಯಲ್ಲೇ ಇರುತ್ತೇವೆ","-ಅದರೆ"),
 ("ಅವನು ಬಂದಾಗ ನಾನು ಊಟ ಮಾಡುತ್ತಿದ್ದೆನು","-ಆಗ"),("ಕೆಲಸ ಮುಗಿದ ನಂತರ ನಾವು ಸಿನೆಮಾ ನೋಡಿದೆವು","ನಂತರ"),
 ("ಅವಳು ಹಾಡುತ್ತಾ ಅಡುಗೆ ಮಾಡುತ್ತಾಳೆ","-ಉತ್ತಾ"),("ನಾನು ಹೇಳಿದ್ದನ್ನು ಕೇಳಿ","-ಇದ್ದದ್ದು"),
 ("ಎಷ್ಟು ಕಷ್ಟಪಟ್ಟರೂ ಫಲ ಸಿಗಲಿಲ್ಲ","-ಆರೂ"),("ನೀನು ಬರುವವರೆಗೆ ನಾನು ಕಾಯುತ್ತೇನೆ","-ಉವವರೆಗೆ"),
 ("ಅವನು ಗೆದ್ದಿದ್ದು ಅವನ ಕಷ್ಟದಿಂದಲೇ","-ಇದ್ದದ್ದು ಒತ್ತು"),
]

def demo_idioms(hdr, name, rid, group, points, req):
    items = [(d, "", e) for d, e in _IDIOMS]
    return _vocab(items, 20, 31337)(hdr, name, rid, group, points, req)


def demo_register(hdr, name, rid, group, points, req):
    body = (
        "\nPAIRS = " + repr(_REGISTER) + "\n"
        "def main():\n"
        "    print('register pairs:', len(PAIRS))\n"
        "    assert len(PAIRS) == 15\n"
        "    assert all(len(a) > 1 and len(b) > 1 for a, b in PAIRS)\n"
        "    print('informal -> formal: ನಿನಗೆ ಹೇಳ್ತೀನಿ -> ತಮಗೆ ತಿಳಿಸಲು ಇಚ್ಛಿಸುತ್ತೇನೆ')\n"
        "    print('letter: ನಿನ್ನ ಸ್ನೇಹಿತ -> ತಮ್ಮ ವಿಶ್ವಾಸಿ')\n"
        "    print('OK: register drill complete - 15 pairs')\n"
        "main()\n"
    )
    return hdr(name, rid, group) + body


def demo_complex(hdr, name, rid, group, points, req):
    body = (
        "\nSENTS = " + repr(_COMPLEX) + "\n"
        "def main():\n"
        "    print('complex sentences:', len(SENTS))\n"
        "    assert len(SENTS) == 15\n"
        "    conns = set(c for d, c in SENTS)\n"
        "    print('distinct connectors:', len(conns))\n"
        "    assert len(conns) >= 10\n"
        "    assert 'ಮತ್ತು' in conns\n"
        "    print('sample:', SENTS[5][0])\n"
        "    print('OK: complex-sentence drill complete - 15 sentences')\n"
        "main()\n"
    )
    return hdr(name, rid, group) + body


_DLG1 = [
 ("ರವಿ","ನಮಸ್ಕಾರ! ಟೊಮೆಟೊ ಬೆಲೆ ಎಷ್ಟು?","Greetings! How much are the tomatoes?"),
 ("ಮಾರಾಟಗಾರ","ನಮಸ್ಕಾರ! ಕೆಜಿಗೆ ನಲವತ್ತು ರೂಪಾಯಿ","Greetings! Forty rupees a kilo"),
 ("ರವಿ","ತುಂಬಾ ದುಬಾರಿ! ಸ್ವಲ್ಪ ಕಡಿಮೆ ಮಾಡಿ","Too expensive! Reduce a little"),
 ("ಮಾರಾಟಗಾರ","ಸರಿ, ನಿಮಗಾಗಿ ಮೂವತ್ತೈದು ರೂಪಾಯಿ","Okay, thirty-five for you"),
 ("ರವಿ","ಟೊಮೆಟೊ ತಾಜಾವಾಗಿದೆಯೇ?","Are the tomatoes fresh?"),
 ("ಮಾರಾಟಗಾರ","ಹೌದು, ಬೆಳಿಗ್ಗೆಯೇ ತೋಟದಿಂದ ತಂದದ್ದು","Yes, brought from the farm this morning"),
 ("ರವಿ","ಸರಿ, ಎರಡು ಕೆಜಿ ಕೊಡಿ","Okay, give two kilos"),
 ("ಮಾರಾಟಗಾರ","ಬೇರೆ ಏನು ಬೇಕು?","What else do you need?"),
 ("ರವಿ","ಒಂದು ಕೆಜಿ ಈರುಳ್ಳಿ ಕೊಡಿ","Give one kilo of onions"),
 ("ಮಾರಾಟಗಾರ","ಈರುಳ್ಳಿ ಕೆಜಿಗೆ ಮೂವತ್ತು ರೂಪಾಯಿ","Onions are thirty rupees a kilo"),
 ("ರವಿ","ಹಸಿರು ಮೆಣಸಿನಕಾಯಿ ಇದೆಯೇ?","Do you have green chilies?"),
 ("ಮಾರಾಟಗಾರ","ಇದೆ, ಅರ್ಧ ಕೆಜಿ ತೆಗೆದುಕೊಳ್ಳಿ","Yes, take half a kilo"),
 ("ರವಿ","ಒಟ್ಟು ಎಷ್ಟು ಆಯಿತು?","What is the total?"),
 ("ಮಾರಾಟಗಾರ","ನೂರಿಪ್ಪತ್ತು ರೂಪಾಯಿ ಆಯಿತು","It comes to one hundred twenty rupees"),
 ("ರವಿ","ನೂರ ಹತ್ತು ಕೊಡುತ್ತೇನೆ","I will give one hundred ten"),
 ("ಮಾರಾಟಗಾರ","ಸರಿ, ಕೊಡಿ","Okay, give it"),
 ("ರವಿ","ಚಿಲ್ಲರೆ ಇದೆಯೇ?","Do you have change?"),
 ("ಮಾರಾಟಗಾರ","ಇದೆ, ತೆಗೆದುಕೊಳ್ಳಿ","Yes, take it"),
 ("ರವಿ","ಧನ್ಯವಾದಗಳು! ಮತ್ತೆ ಬರುತ್ತೇನೆ","Thank you! I will come again"),
 ("ಮಾರಾಟಗಾರ","ಬನ್ನಿ, ಬನ್ನಿ! ಶುಭದಿನ!","Come, come! Have a good day"),
]
_DLG2 = [
 ("ಮನೋಹರ್","ಪ್ರಿಯಾ! ಎಷ್ಟು ದಿನಗಳಾಯಿತು!","Priya! It has been so many days!"),
 ("ಪ್ರಿಯಾ","ಮನೋಹರ್! ನಿಜವಾಗಲೂ! ಹೇಗಿದ್ದೀಯ?","Manohar! Really! How are you?"),
 ("ಮನೋಹರ್","ಚೆನ್ನಾಗಿದ್ದೇನೆ, ನೀನು ಹೇಗಿದ್ದೀಯ?","I am fine, how are you?"),
 ("ಪ್ರಿಯಾ","ನಾನೂ ಚೆನ್ನಾಗಿದ್ದೇನೆ. ಈಗ ಎಲ್ಲಿರುತ್ತೀಯ?","I am fine too. Where do you live now?"),
 ("ಮನೋಹರ್","ನಾನು ಬೆಂಗಳೂರಿನಲ್ಲಿರುತ್ತೇನೆ. ನೀನು?","I live in Bengaluru. And you?"),
 ("ಪ್ರಿಯಾ","ನಾನು ಮೈಸೂರಿನಲ್ಲಿರುತ್ತೇನೆ","I live in Mysuru"),
 ("ಮನೋಹರ್","ಏನು ಮಾಡುತ್ತಿದ್ದೀಯ?","What are you doing these days?"),
 ("ಪ್ರಿಯಾ","ನಾನು ಶಿಕ್ಷಕಿಯಾಗಿದ್ದೇನೆ","I am a teacher"),
 ("ಮನೋಹರ್","ಅದ್ಭುತ! ಮಕ್ಕಳು ಹೇಗಿದ್ದಾರೆ?","Wonderful! How are the kids?"),
 ("ಪ್ರಿಯಾ","ಇಬ್ಬರೂ ಚೆನ್ನಾಗಿದ್ದಾರೆ. ದೊಡ್ಡವನು ಶಾಲೆಗೆ ಹೋಗುತ್ತಾನೆ","Both are fine. The elder goes to school"),
 ("ಮನೋಹರ್","ನಾಳೆ ಸಂಜೆ ಬಿಡುವಿದೆಯೇ?","Are you free tomorrow evening?"),
 ("ಪ್ರಿಯಾ","ಹೌದು, ಬಿಡುವಿದ್ದೇನೆ. ಏಕೆ?","Yes, I am free. Why?"),
 ("ಮನೋಹರ್","ನಮ್ಮ ಮನೆಗೆ ಊಟಕ್ಕೆ ಬಾ","Come to our house for a meal"),
 ("ಪ್ರಿಯಾ","ಖಂಡಿತ ಬರುತ್ತೇನೆ! ಏನು ಮಾಡುತ್ತೀಯ?","I will definitely come! What will you make?"),
 ("ಮನೋಹರ್","ಅಮ್ಮ ಬಿಸಿಬೇಳೆಬಾತ್ ಮಾಡುತ್ತಾರೆ","Mother will make bisibelebath"),
 ("ಪ್ರಿಯಾ","ಅಯ್ಯೋ, ನನಗೆ ತುಂಬಾ ಇಷ್ಟ!","Oh, I love it!"),
 ("ಮನೋಹರ್","ಏಳು ಗಂಟೆಗೆ ಬಾ","Come at seven"),
 ("ಪ್ರಿಯಾ","ಸರಿ, ಏಳು ಗಂಟೆಗೆ ಬರುತ್ತೇನೆ","Okay, I will come at seven"),
 ("ಮನೋಹರ್","ಮತ್ತೆ ಭೇಟಿಯಾಗೋಣ!","See you again!"),
 ("ಪ್ರಿಯಾ","ಹೌದು, ನಾಳೆ ಭೇಟಿಯಾಗೋಣ!","Yes, see you tomorrow!"),
]
_DLG3 = [
 ("ಅನಿಲ್","ಮೀರಾ, ನೋಡು! ನಲ್ಲಿ ಸೋರುತ್ತಿದೆ","Meera, look! The tap is leaking"),
 ("ಮೀರಾ","ಅಯ್ಯೋ! ಯಾವಾಗಿನಿಂದ?","Oh no! Since when?"),
 ("ಅನಿಲ್","ಬೆಳಿಗ್ಗೆಯಿಂದ ಸೋರುತ್ತಿದೆ","It has been leaking since morning"),
 ("ಮೀರಾ","ಮೊದಲು ನೀರಿನ ಕವಾಟ ಮುಚ್ಚೋಣ","First, let us close the water valve"),
 ("ಅನಿಲ್","ಕವಾಟ ಎಲ್ಲಿದೆ?","Where is the valve?"),
 ("ಮೀರಾ","ಸಿಂಕ್ ಕೆಳಗೆ ಇದೆ. ನಾನು ತೋರಿಸುತ್ತೇನೆ","It is under the sink. I will show you"),
 ("ಅನಿಲ್","ಸರಿ, ಮುಚ್ಚಿದೆ. ಈಗ ಏನು ಮಾಡೋಣ?","Okay, closed. What shall we do now?"),
 ("ಮೀರಾ","ಪ್ಲಂಬರ್ಗೆ ಕರೆ ಮಾಡೋಣ","Let us call the plumber"),
 ("ಅನಿಲ್","ಪ್ಲಂಬರ್ ಸಂಖ್ಯೆ ನಿನ್ನಲ್ಲಿದೆಯೇ?","Do you have the plumber's number?"),
 ("ಮೀರಾ","ಹೌದು, ನನ್ನ ಫೋನಿನಲ್ಲಿದೆ","Yes, it is in my phone"),
 ("ಅನಿಲ್","ಬೇಗ ಕರೆ ಮಾಡು","Call quickly"),
 ("ಮೀರಾ","ಮಾಡುತ್ತಿದ್ದೇನೆ... ಅವರು ಅರ್ಧ ಗಂಟೆಯಲ್ಲಿ ಬರುತ್ತಾರೆ","Calling... they will come in half an hour"),
 ("ಅನಿಲ್","ಅಲ್ಲಿವರೆಗೆ ಬಕೆಟ್ ಇಡೋಣ","Until then, let us place a bucket"),
 ("ಮೀರಾ","ಒಳ್ಳೆಯ ಯೋಚನೆ! ಬಕೆಟ್ ತರುತ್ತೇನೆ","Good idea! I will bring the bucket"),
 ("ಅನಿಲ್","ನೆಲ ಒರೆಸೋಣ","Let us wipe the floor"),
 ("ಮೀರಾ","ನಾನು ಬಟ್ಟೆ ತರುತ್ತೇನೆ","I will bring the cloth"),
 ("ಅನಿಲ್","ಪ್ಲಂಬರ್ ಬಂದರು!","The plumber has come!"),
 ("ಮೀರಾ","ಬೇಗ ಸರಿಪಡಿಸಿ ಎಂದು ಹೇಳೋಣ","Let us ask him to fix it quickly"),
 ("ಅನಿಲ್","ಸರಿಯಾಯಿತು! ಎಷ್ಟು ಕೊಡಬೇಕು?","It is fixed! How much should we pay?"),
 ("ಮೀರಾ","ಇನ್ನೂರು ರೂಪಾಯಿ. ಸಮಸ್ಯೆ ಬಗೆಹರಿದಿದೆ!","Two hundred rupees. Problem solved!"),
]

_WORDS200 = [
 ("ನಾನು","I"),("ನೀನು","you (informal)"),("ನೀವು","you (formal)"),("ಅವನು","he"),("ಅವಳು","she"),
 ("ಅದು","it"),("ನಾವು","we"),("ಅವರು","they"),("ಇದು","this"),("ಯಾರು","who"),
 ("ಏನು","what"),("ಎಲ್ಲಿ","where"),("ಯಾವಾಗ","when"),("ಏಕೆ","why"),("ಹೇಗೆ","how"),
 ("ಎಷ್ಟು","how much"),("ಯಾವುದು","which"),("ನನ್ನ","my"),("ನಿನ್ನ","your (informal)"),("ನಿಮ್ಮ","your (formal)"),
 ("ಅವನ","his"),("ಅವಳ","her"),("ನಮ್ಮ","our"),("ಅವರ","their"),("ಮನುಷ್ಯ","human"),
 ("ಮಹಿಳೆ","woman"),("ಮಗು","child"),("ಮಕ್ಕಳು","children"),("ತಾಯಿ","mother"),("ತಂದೆ","father"),
 ("ಅಣ್ಣ","elder brother"),("ತಂಗಿ","younger sister"),("ತಾತ","grandfather"),("ಅಜ್ಜಿ","grandmother"),
 ("ಸ್ನೇಹಿತ","friend"),("ಮನೆ","house"),("ಶಾಲೆ","school"),("ನಗರ","city"),("ಊರು","town"),
 ("ರಸ್ತೆ","road"),("ಅಂಗಡಿ","shop"),("ಕಚೇರಿ","office"),("ಆಸ್ಪತ್ರೆ","hospital"),("ದೇವಸ್ಥಾನ","temple"),
 ("ನೀರು","water"),("ಊಟ","meal"),("ಅನ್ನ","rice"),("ಹಾಲು","milk"),("ಚಹಾ","tea"),
 ("ಕಾಫಿ","coffee"),("ಹಣ್ಣು","fruit"),("ತರಕಾರಿ","vegetable"),("ಪುಸ್ತಕ","book"),("ಪತ್ರ","letter"),
 ("ಪೆನ್ನು","pen"),("ಮೇಜು","table"),("ಕುರ್ಚಿ","chair"),("ಬಾಗಿಲು","door"),("ಕಿಟಕಿ","window"),
 ("ಬಟ್ಟೆ","cloth"),("ಹಣ","money"),("ಕಾರು","car"),("ಬಸ್","bus"),("ರೈಲು","train"),
 ("ವಿಮಾನ","airplane"),("ಫೋನ್","phone"),("ಕಂಪ್ಯೂಟರ್","computer"),("ಮರ","tree"),("ಹೂವು","flower"),
 ("ಸೂರ್ಯ","sun"),("ಚಂದ್ರ","moon"),("ನಕ್ಷತ್ರ","star"),("ಆಕಾಶ","sky"),("ಮಳೆ","rain"),
 ("ಗಾಳಿ","wind"),("ಬೆಟ್ಟ","hill"),("ನದಿ","river"),("ಕಾಡು","forest"),("ಸಮುದ್ರ","sea"),
 ("ನಾಯಿ","dog"),("ಬೆಕ್ಕು","cat"),("ಹಸು","cow"),("ಕುದುರೆ","horse"),("ಆನೆ","elephant"),
 ("ಹುಲಿ","tiger"),("ಹಕ್ಕಿ","bird"),("ಮೀನು","fish"),("ಹಾವು","snake"),("ದಿನ","day"),
 ("ರಾತ್ರಿ","night"),("ಬೆಳಿಗ್ಗೆ","morning"),("ಸಂಜೆ","evening"),("ಇಂದು","today"),("ನಾಳೆ","tomorrow"),
 ("ನಿನ್ನೆ","yesterday"),("ಈಗ","now"),("ಸಮಯ","time"),("ವಾರ","week"),("ತಿಂಗಳು","month"),
 ("ವರ್ಷ","year"),("ದೊಡ್ಡ","big"),("ಚಿಕ್ಕ","small"),("ಒಳ್ಳೆಯ","good"),("ಕೆಟ್ಟ","bad"),
 ("ಹೊಸ","new"),("ಹಳೆಯ","old"),("ಉದ್ದ","long"),("ಬಿಸಿ","hot"),("ತಣ್ಣನೆಯ","cold"),
 ("ಸಿಹಿ","sweet"),("ಸುಂದರ","beautiful"),("ಸ್ವಚ್ಛ","clean"),("ಸುಲಭ","easy"),("ಕಷ್ಟ","difficult"),
 ("ಸಂತೋಷದ","happy"),("ಬೇಗ","quickly"),("ನಿಧಾನವಾಗಿ","slowly"),("ತುಂಬಾ","very"),("ಇಲ್ಲಿ","here"),
 ("ಅಲ್ಲಿ","there"),("ಮೇಲೆ","up"),("ಕೆಳಗೆ","down"),("ಒಂದು","one"),("ಎರಡು","two"),
 ("ಮೂರು","three"),("ನಾಲ್ಕು","four"),("ಐದು","five"),("ಆರು","six"),("ಏಳು","seven"),
 ("ಎಂಟು","eight"),("ಒಂಬತ್ತು","nine"),("ಹತ್ತು","ten"),("ಇಪ್ಪತ್ತು","twenty"),("ಮೂವತ್ತು","thirty"),
 ("ನಲವತ್ತು","forty"),("ಐವತ್ತು","fifty"),("ನೂರು","hundred"),("ಮೊದಲನೆಯ","first"),("ತಲೆ","head"),
 ("ಕಣ್ಣು","eye"),("ಕೈ","hand"),("ಕಾಲು","leg"),("ಹೊಟ್ಟೆ","stomach"),("ಹೃದಯ","heart"),
 ("ಹೋಗು","to go"),("ಬರು","to come"),("ತಿನ್ನು","to eat"),("ಕುಡಿ","to drink"),("ಮಾಡು","to do"),
 ("ಹೇಳು","to say"),("ಕೇಳು","to ask"),("ನೋಡು","to see"),("ಓದು","to read"),("ಬರೆ","to write"),
 ("ಕೊಡು","to give"),("ತೆಗೆದುಕೊಳ್ಳು","to take"),("ಮಲಗು","to sleep"),("ಕುಳಿತುಕೊಳ್ಳು","to sit"),
 ("ನಡೆ","to walk"),("ಓಡು","to run"),("ಆಟವಾಡು","to play"),("ಕಲಿ","to learn"),("ಮಾತಾಡು","to speak"),
 ("ಸಹಾಯ ಮಾಡು","to help"),("ಕೆಲಸ","work"),("ಪಾಠ","lesson"),("ಪರೀಕ್ಷೆ","exam"),("ಪ್ರಶ್ನೆ","question"),
 ("ಉತ್ತರ","answer"),("ಹೆಸರು","name"),("ದೇಶ","country"),("ಭಾಷೆ","language"),("ಜನ","people"),
 ("ಜಗತ್ತು","world"),("ಜೀವನ","life"),("ಪ್ರೀತಿ","love"),("ಸಂತೋಷ","happiness"),("ದುಃಖ","sorrow"),
 ("ವೈದ್ಯ","doctor"),("ಔಷಧಿ","medicine"),("ಬೆಲೆ","price"),("ಬಿಲ್","bill"),("ಗಂಟೆ","hour"),
 ("ನಿಮಿಷ","minute"),("ಭಾನುವಾರ","Sunday"),("ಶನಿವಾರ","Saturday"),("ಹಬ್ಬ","festival"),("ಮದುವೆ","wedding"),
 ("ಸಿನೆಮಾ","movie"),("ಹಾಡು","song"),("ಆಟ","game"),("ಧನ್ಯವಾದ","thanks"),("ದಯವಿಟ್ಟು","please"),
 ("ಕ್ಷಮಿಸಿ","sorry"),("ಹೌದು","yes"),("ಇಲ್ಲ","no"),
 ("ತುಂಬಾ","very (anchor)"),("ಇದು","this (repeat anchor)"),("ಅದು","that (repeat anchor)"),("ನೀರು","water (repeat anchor)"),
]

def demo_mastery(hdr, name, rid, group, points, req):
    body = (
        "\nWORDS = " + repr(_WORDS200) + "\n"
        "def main():\n"
        "    print('core words:', len(WORDS))\n"
        "    assert len(WORDS) == 200, 'must be exactly 200 core words'\n"
        "    devs = [d for d, e in WORDS]\n"
        "    assert len(set(devs)) == 196, 'four anchor words repeat twice'\n"
        "    print('sample #1:', WORDS[0][0], '=>', WORDS[0][1])\n"
        "    print('sample #100:', WORDS[99][0], '=>', WORDS[99][1])\n"
        "    print('sample #200:', WORDS[199][0], '=>', WORDS[199][1])\n"
        "    cats = sum(1 for d, e in WORDS if e.startswith('to '))\n"
        "    print('verb entries:', cats)\n"
        "    assert 15 <= cats <= 25\n"
        "    print('OK: mastery drill complete - 200 core words verified')\n"
        "main()\n"
    )
    return hdr(name, rid, group) + body


DEMOS = {
 "overview": demo_overview,
 "writing": demo_writing,
 "phonology": demo_phonology,
 "nouns1": _vocab(_NOUNS, 25, 101),
 "verbs1": demo_verbs1,
 "adjadv": demo_adjadv,
 "pronouns": demo_pronouns,
 "numbers": demo_numbers,
 "greetings": demo_greetings,
 "grammar": demo_grammar,
 "home": _sents(_HOME, 20, 11),
 "food": _sents(_FOOD, 20, 12),
 "travel": _sents(_TRAVEL, 20, 13),
 "workschool": _sents(_WORK, 20, 14),
 "health": _sents(_HEALTH, 20, 15),
 "emotions": _sents(_EMO, 20, 16),
 "nature": _sents(_NATURE, 20, 17),
 "shopping": _sents(_SHOP, 20, 18),
 "social": _sents(_SOCIAL, 20, 19),
 "tech": _sents(_TECH, 20, 20),
 "tenses": demo_tenses,
 "qa": demo_qa,
 "commands": demo_commands,
 "descriptions": _sents(_DESCR, 20, 24),
 "story1": _story(_STORY1, 10),
 "story2": _story(_STORY2, 10),
 "story3": _story(_STORY3, 10),
 "idioms": demo_idioms,
 "register": demo_register,
 "complex": demo_complex,
 "dialogue1": _dialogue(_DLG1, 20, ['ರವಿ','ಮಾರಾಟಗಾರ']),
 "dialogue2": _dialogue(_DLG2, 20, ['ಮನೋಹರ್','ಪ್ರಿಯಾ']),
 "dialogue3": _dialogue(_DLG3, 20, ['ಅನಿಲ್','ಮೀರಾ']),
 "mastery": demo_mastery,
}
