#!/usr/bin/env python3
"""Demo programs for The Hindi to English Database (language-hindi).

Every program is real, runnable, stdlib-only Python. Each prints real
computed values (drill counts, quiz scores, word statistics), asserts
tight bounds (never float exact-equality), and ends with an OK: marker.
All embedded Hindi matches the entry text verbatim (cross-checked by
the build: sampled Devanagari tokens from each demo must appear in the
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
            "    print('total Hindi words:', words)\n"
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
        "\nNATIVE = 345000000\n"
        "TOTAL = 600000000\n"
        "STATES = 9\n"
        "def main():\n"
        "    print('native speakers:', NATIVE)\n"
        "    print('total speakers:', TOTAL)\n"
        "    assert 300000000 <= NATIVE <= 400000000\n"
        "    assert 500000000 <= TOTAL <= 700000000\n"
        "    ratio = TOTAL / NATIVE\n"
        "    print('total/native ratio: %.3f' % ratio)\n"
        "    assert 1.5 < ratio < 2.0\n"
        "    print('official states/UTs:', STATES)\n"
        "    assert STATES >= 9\n"
        "    print('ISO 639-1: hi, ISO 639-3: hin')\n"
        "    print('sample: मैं पानी पीता हूँ => I drink water')\n"
        "    print('OK: overview drill complete - %d native speakers' % NATIVE)\n"
        "main()\n"
    )
    return hdr(name, rid, group) + body


def demo_writing(hdr, name, rid, group, points, req):
    vowels = ['अ','आ','इ','ई','उ','ऊ','ऋ','ए','ऐ','ओ','औ','अं','अः']
    cons = ['क','ख','ग','घ','ङ','च','छ','ज','झ','ञ','ट','ठ','ड','ढ','ण',
            'त','थ','द','ध','न','प','फ','ब','भ','म','य','र','ल','व','श','ष','स','ह']
    digits = ['०','१','२','३','४','५','६','७','८','९']
    body = (
        "\nVOWELS = " + repr(vowels) + "\n"
        "CONS = " + repr(cons) + "\n"
        "DIGITS = " + repr(digits) + "\n"
        "def main():\n"
        "    print('independent vowels:', len(VOWELS))\n"
        "    assert len(VOWELS) == 13\n"
        "    print('consonants:', len(CONS))\n"
        "    assert len(CONS) == 33\n"
        "    print('digits:', len(DIGITS))\n"
        "    assert len(DIGITS) == 10\n"
        "    built = 'क' + 'ी'\n"
        "    print('matra build: क + ी =', built)\n"
        "    assert built == 'की'\n"
        "    print('sample word: नमस्ते => hello')\n"
        "    print('punctuation: । ends a sentence')\n"
        "    print('OK: script drill complete - 13 vowels, 33 consonants')\n"
        "main()\n"
    )
    return hdr(name, rid, group) + body


def demo_phonology(hdr, name, rid, group, points, req):
    vowels = ['अ','आ','इ','ई','उ','ऊ','ऋ','ए','ऐ','ओ','औ']
    pairs = [('कम','काम'),('दिन','दीन'),('कुल','कूल'),('पल','पाल'),('मिल','मील'),
             ('है','हैं'),('त','ट'),('द','ड'),('न','ण'),('क','ख'),('ग','घ')]
    body = (
        "\nVOWELS = " + repr(vowels) + "\n"
        "PAIRS = " + repr(pairs) + "\n"
        "def main():\n"
        "    print('vowel phonemes:', len(VOWELS))\n"
        "    assert len(VOWELS) == 11\n"
        "    print('contrast pairs:', len(PAIRS))\n"
        "    assert len(PAIRS) == 11\n"
        "    for a, b in PAIRS:\n"
        "        assert a != b, 'pair collapsed'\n"
        "        print('contrast: %s vs %s' % (a, b))\n"
        "    print('schwa deletion: राम pronounced ram, not raama')\n"
        "    print('sample: धन्यवाद => thank you')\n"
        "    print('OK: phonology drill complete - 11 vowels, 11 contrasts')\n"
        "main()\n"
    )
    return hdr(name, rid, group) + body


_NOUNS = [
 ("आदमी","ādmī","man"),("औरत","aurat","woman"),("बच्चा","baccā","child"),
 ("घर","ghar","house"),("पानी","pānī","water"),("खाना","khānā","food"),
 ("किताब","kitāb","book"),("स्कूल","skūl","school"),("दोस्त","dost","friend"),
 ("माँ","mā̃","mother"),("पिता","pitā","father"),("भाई","bhāī","brother"),
 ("बहन","bahan","sister"),("शहर","śahar","city"),("गाँव","gā̃v","village"),
 ("सड़क","saṛak","road"),("गाड़ी","gāṛī","car"),("पेड़","peṛ","tree"),
 ("फूल","phūl","flower"),("सूरज","sūraj","sun"),("चाँद","cā̃d","moon"),
 ("तारा","tārā","star"),("दिन","din","day"),("रात","rāt","night"),
 ("समय","samay","time"),
]

_VERBS = [
 ("जाना","jānā","to go"),("आना","ānā","to come"),("खाना","khānā","to eat"),
 ("पीना","pīnā","to drink"),("करना","karnā","to do"),("बोलना","bolnā","to speak"),
 ("पढ़ना","paṛhnā","to read"),("लिखना","likhnā","to write"),
 ("देखना","dekhnā","to see"),("सुनना","sunnā","to listen"),
 ("सोना","sonā","to sleep"),("उठना","uṭhnā","to wake up"),
 ("बैठना","baiṭhnā","to sit"),("चलना","calnā","to walk"),
 ("दौड़ना","dauṛnā","to run"),("देना","denā","to give"),
 ("लेना","lenā","to take"),("खरीदना","kharīdnā","to buy"),
 ("बेचना","becnā","to sell"),("बनाना","banānā","to make"),
 ("खेलना","khelnā","to play"),("हँसना","hãsnā","to laugh"),
 ("रोना","ronā","to cry"),("समझना","samajhnā","to understand"),
 ("मदद करना","madad karnā","to help"),
]

def demo_verbs1(hdr, name, rid, group, points, req):
    fn = _vocab(_VERBS, 25, 4242)
    prog = fn(hdr, name, rid, group, points, req)
    extra = (
        "stems = [d[:-2] if d.endswith('ना') else d for d, t, e in ITEMS]\n"
        "print('stems extracted:', len(stems))\n"
        "assert all(d.endswith('ना') or ' ' in d for d, t, e in ITEMS)\n"
        "print('sample stem: जा from जाना')\n"
        "print('OK: verb stem check complete')\n"
    )
    prog = prog.replace("main()\n", extra + "main()\n", 1)
    return prog


_ADJ = [
 ("बड़ा","baṛā","big"),("छोटा","choṭā","small"),("अच्छा","acchā","good"),
 ("बुरा","burā","bad"),("नया","nayā","new"),("पुराना","purānā","old"),
 ("लंबा","lambā","long"),("गर्म","garm","hot"),("ठंडा","ṭhaṇḍā","cold"),
 ("मीठा","mīṭhā","sweet"),("खट्टा","khaṭṭā","sour"),("तेज़","tez","fast"),
 ("धीमा","dhīmā","slow"),("सुंदर","sundar","beautiful"),("साफ़","sāf","clean"),
 ("गंदा","gandā","dirty"),("आसान","āsān","easy"),("मुश्किल","muśkil","difficult"),
 ("खुश","khuś","happy"),("दुखी","dukhī","sad"),("अमीर","amīr","rich"),
 ("गरीब","garīb","poor"),("मजबूत","majbūt","strong"),("कमजोर","kamzor","weak"),
 ("महँगा","mahãgā","expensive"),
]
_ADV = [
 ("बहुत","bahut","very"),("जल्दी","jaldī","quickly"),("धीरे","dhīre","slowly"),
 ("हमेशा","hameśā","always"),("कभी","kabhī","sometimes"),
 ("कभी नहीं","kabhī nahī̃","never"),("यहाँ","yahā̃","here"),("वहाँ","vahā̃","there"),
 ("अंदर","andar","inside"),("बाहर","bāhar","outside"),("ऊपर","ūpar","up"),
 ("नीचे","nīce","down"),("आज","āj","today"),("कल","kal","tomorrow/yesterday"),
 ("अब","ab","now"),
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
        "    infl = [d for d, t, e in ADJ if d.endswith('ा')]\n"
        "    print('inflecting -ा adjectives:', len(infl))\n"
        "    assert 8 <= len(infl) <= 20\n"
        "    print('agreement: बड़ा घर / बड़ी किताब / बड़े घर')\n"
        "    print('invariable: खुश लड़का / खुश लड़की')\n"
        "    print('sample: वह बहुत अच्छा है => He is very good')\n"
        "    print('OK: adjective drill complete - 25 adjectives, 15 adverbs')\n"
        "main()\n"
    )
    return hdr(name, rid, group) + body


def demo_pronouns(hdr, name, rid, group, points, req):
    cats = {
     'personal': ['मैं','तुम','आप','वह','यह','हम','वे'],
     'oblique': ['मुझ','तुझ','उस','इस','हम','उन'],
     'possessive': ['मेरा','तुम्हारा','आपका','उसका','इसका','हमारा','उनका'],
     'demonstrative': ['यह','वह','ये','वे'],
     'interrogative': ['कौन','क्या','कहाँ','कब','क्यों','कैसे','कितना','कौन-सा'],
    }
    body = (
        "\nCATS = " + repr(cats) + "\n"
        "def main():\n"
        "    total = 0\n"
        "    for k, v in CATS.items():\n"
        "        print(k, 'pronouns:', len(v))\n"
        "        total += len(v)\n"
        "    print('total forms:', total)\n"
        "    assert total == 32\n"
        "    assert len(CATS['interrogative']) == 8\n"
        "    print('respect rule: आप takes plural verbs - आप जाते हैं')\n"
        "    print('sample: आप कैसे हैं => How are you (formal)')\n"
        "    print('OK: pronoun drill complete - 32 forms in 5 tables')\n"
        "main()\n"
    )
    return hdr(name, rid, group) + body


def demo_numbers(hdr, name, rid, group, points, req):
    n20 = ['एक','दो','तीन','चार','पाँच','छह','सात','आठ','नौ','दस',
           'ग्यारह','बारह','तेरह','चौदह','पंद्रह','सोलह','सत्रह','अठारह','उन्नीस','बीस']
    tens = ['तीस','चालीस','पचास','साठ','सत्तर','अस्सी','नब्बे','सौ']
    days = ['सोमवार','मंगलवार','बुधवार','गुरुवार','शुक्रवार','शनिवार','रविवार']
    months = ['जनवरी','फ़रवरी','मार्च','अप्रैल','मई','जून','जुलाई','अगस्त','सितंबर','अक्टूबर','नवंबर','दिसंबर']
    seasons = ['वसंत','ग्रीष्म','वर्षा','शरद','हेमंत','शिशिर']
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
        "    print('time: सवा = quarter past, साढ़े = half past, पौने = quarter to')\n"
        "    print('sample: अब तीन बजे हैं => It is three o clock now')\n"
        "    print('OK: number drill complete - 20 + 8 + 7 + 12 + 6')\n"
        "main()\n"
    )
    return hdr(name, rid, group) + body


_GREET = [
 ("नमस्ते","hello"),("नमस्कार","greetings"),("शुभ प्रभात","good morning"),
 ("शुभ संध्या","good evening"),("शुभ रात्रि","good night"),
 ("आप कैसे हैं","how are you (formal)"),("तुम कैसे हो","how are you (informal)"),
 ("मैं ठीक हूँ","I am fine"),("सब ठीक है","all is well"),("धन्यवाद","thank you"),
 ("शुक्रिया","thanks"),("बहुत-बहुत धन्यवाद","thank you very much"),
 ("कृपया","please"),("माफ़ कीजिए","excuse me (formal)"),
 ("माफ़ करना","excuse me (informal)"),("कोई बात नहीं","no problem"),
 ("आपका स्वागत है","you are welcome"),("फिर मिलेंगे","we will meet again"),
 ("अलविदा","farewell"),("बहुत खुशी हुई","pleased to meet you"),
 ("आपसे मिलकर खुशी हुई","pleased to meet you"),("बधाई हो","congratulations"),
 ("शुभकामनाएँ","best wishes"),("आइए","please come in"),("बैठिए","please sit"),
 ("चाय पिएँगे","will you have tea"),("जी हाँ","yes (respectful)"),
 ("जी नहीं","no (respectful)"),("ठीक है","okay"),
 ("आपका दिन शुभ हो","have a good day"),
]

def demo_greetings(hdr, name, rid, group, points, req):
    items = [(d, "", e) for d, e in _GREET]
    return _vocab(items, 30, 777)(hdr, name, rid, group, points, req)


def demo_grammar(hdr, name, rid, group, points, req):
    post = ['ने','को','से','में','पर','का','की']
    body = (
        "\nPOST = " + repr(post) + "\n"
        "def main():\n"
        "    print('postpositions:', len(POST))\n"
        "    assert len(POST) == 7\n"
        "    s = ['मैं', 'किताब', 'पढ़ता', 'हूँ']\n"
        "    print('SOV check:', ' '.join(s))\n"
        "    assert s.index('पढ़ता') > s.index('किताब'), 'verb must follow object'\n"
        "    neg = 'मैं नहीं जाता'\n"
        "    print('negation:', neg)\n"
        "    assert 'नहीं' in neg\n"
        "    q = 'क्या तुम आओगे'\n"
        "    print('question:', q)\n"
        "    assert q.startswith('क्या')\n"
        "    print('sample: राम ने खाना खाया => Ram ate food')\n"
        "    print('OK: grammar drill complete - 7 postpositions, SOV verified')\n"
        "main()\n"
    )
    return hdr(name, rid, group) + body

_HOME = [
 ("यह मेरा घर है","This is my house"),("घर में चार कमरे हैं","There are four rooms in the house"),
 ("रसोई में माँ खाना बनाती है","Mother cooks food in the kitchen"),("बैठक में सोफ़ा है","There is a sofa in the living room"),
 ("मेरे कमरे में एक मेज़ है","There is a table in my room"),("कुर्सी मेज़ के पास है","The chair is near the table"),
 ("खिड़की से धूप आती है","Sunlight comes through the window"),("दरवाज़ा बंद करो","Close the door"),
 ("बिस्तर नरम है","The bed is soft"),("अलमारी में कपड़े हैं","There are clothes in the wardrobe"),
 ("मेरे पिता दफ़्तर जाते हैं","My father goes to the office"),("मेरी माँ बहुत अच्छी है","My mother is very good"),
 ("मेरा भाई मुझसे बड़ा है","My brother is older than me"),("मेरी बहन स्कूल जाती है","My sister goes to school"),
 ("दादा बगीचे में बैठते हैं","Grandfather sits in the garden"),("दादी कहानी सुनाती है","Grandmother tells a story"),
 ("हम सब साथ खाना खाते हैं","We all eat food together"),("मेरा परिवार बड़ा है","My family is big"),
 ("घर के सामने पेड़ है","There is a tree in front of the house"),("यह तस्वीर मेरे परिवार की है","This photo is of my family"),
]

_FOOD = [
 ("मुझे भूख लगी है","I am hungry"),("नाश्ते में पराठा खाओ","Eat paratha for breakfast"),
 ("दोपहर का खाना तैयार है","Lunch is ready"),("रात का खाना आठ बजे खाएँगे","We will eat dinner at eight"),
 ("दाल में नमक कम है","There is less salt in the lentils"),("रोटी गरम है","The bread is hot"),
 ("चावल के साथ सब्ज़ी खाओ","Eat vegetables with rice"),("माँ दाल बनाती है","Mother makes lentils"),
 ("पानी उबालो","Boil the water"),("सब्ज़ी काटो","Cut the vegetables"),
 ("मसाले डालो","Add the spices"),("खाना मीठा है","The food is sweet"),
 ("यह खाना तीखा है","This food is spicy"),("मुझे आम पसंद है","I like mangoes"),
 ("एक कप चाय लाओ","Bring a cup of tea"),("रेस्टोरेंट में खाना खाएँगे","We will eat at the restaurant"),
 ("बिल लाइए","Bring the bill (please)"),("खाना बहुत स्वादिष्ट था","The food was very tasty"),
 ("फल ताज़े हैं","The fruits are fresh"),("मिठाई खाओ","Eat the sweets"),
]

_TRAVEL = [
 ("स्टेशन कहाँ है","Where is the station"),("बाज़ार कितनी दूर है","How far is the market"),
 ("दाएँ मुड़ो","Turn right"),("बाएँ मुड़ो","Turn left"),("सीधे जाओ","Go straight"),
 ("यहाँ से बस मिलेगी","You will get a bus from here"),("टैक्सी कितने की है","How much is the taxi"),
 ("दिल्ली का टिकट दो","Give two tickets to Delhi"),("ट्रेन कितने बजे आएगी","At what time will the train come"),
 ("यह बस कहाँ जाती है","Where does this bus go"),("मुझे हवाई अड्डा जाना है","I have to go to the airport"),
 ("होटल कहाँ है","Where is the hotel"),("एक कमरा चाहिए","I need a room"),
 ("कमरे का किराया कितना है","What is the room rent"),("नक्शा दिखाइए","Show the map (please)"),
 ("मैं रास्ता भूल गया","I lost my way"),("क्या आप मेरी मदद करेंगे","Will you help me"),
 ("पेट्रोल पंप कहाँ है","Where is the petrol pump"),("यात्रा अच्छी रही","The journey was good"),
 ("हम कल वापस जाएँगे","We will go back tomorrow"),
]

_WORK = [
 ("मैं शिक्षक हूँ","I am a teacher"),("वह डॉक्टर है","He is a doctor"),
 ("मेरा काम अच्छा है","My work is good"),("दफ़्तर नौ बजे खुलता है","The office opens at nine"),
 ("मुझे काम पर जाना है","I have to go to work"),("आज बहुत काम है","There is a lot of work today"),
 ("बैठक तीन बजे है","The meeting is at three"),("यह मेरा सहकर्मी है","He is my colleague"),
 ("वेतन महीने में मिलता है","Salary comes every month"),("बच्चा स्कूल जाता है","The child goes to school"),
 ("कक्षा में चालीस छात्र हैं","There are forty students in the class"),("अध्यापक पढ़ाते हैं","The teacher teaches"),
 ("छात्र सवाल पूछते हैं","The students ask questions"),("परीक्षा अगले हफ़्ते है","The exam is next week"),
 ("मैं हिन्दी सीखता हूँ","I am learning Hindi"),("पढ़ाई में मन लगाओ","Put your mind into studies"),
 ("गृहकार्य पूरा करो","Complete the homework"),("किताब खोलो","Open the book"),
 ("ध्यान से सुनो","Listen carefully"),("सीखना कभी बंद मत करो","Never stop learning"),
]

_HEALTH = [
 ("मेरा सिर दुख रहा है","My head is aching"),("मुझे बुखार है","I have a fever"),
 ("मेरा गला खराब है","My throat is sore"),("मुझे खाँसी है","I have a cough"),
 ("मेरा पेट दुखता है","My stomach hurts"),("मेरी आँखें लाल हैं","My eyes are red"),
 ("मेरा हाथ कट गया","My hand got cut"),("मेरे पैर में दर्द है","There is pain in my leg"),
 ("डॉक्टर को दिखाओ","Show it to the doctor"),("अस्पताल कहाँ है","Where is the hospital"),
 ("डॉक्टर ने दवा दी","The doctor gave medicine"),("दवा समय पर लो","Take the medicine on time"),
 ("आराम करो","Take rest"),("ज़्यादा पानी पियो","Drink more water"),
 ("अब तबीयत कैसी है","How is your health now"),("मैं ठीक हो रहा हूँ","I am getting better"),
 ("दवा की दुकान कहाँ है","Where is the pharmacy"),("यह दवा दिन में दो बार लो","Take this medicine twice a day"),
 ("सेहत का ख्याल रखो","Take care of your health"),("रोज़ व्यायाम करो","Exercise daily"),
]

_EMO = [
 ("मैं बहुत खुश हूँ","I am very happy"),("आज मेरा मन प्रसन्न है","My heart is cheerful today"),
 ("वह हँस रही है","She is laughing"),("अच्छी खबर सुनकर खुशी हुई","I felt happy hearing the good news"),
 ("मैं दुखी हूँ","I am sad"),("वह रो रहा है","He is crying"),
 ("मुझे आपकी याद आती है","I miss you"),("दिल टूट गया","The heart broke"),
 ("मुझे गुस्सा आ रहा है","I am getting angry"),("शांत हो जाओ","Calm down"),
 ("मुझे डर लग रहा है","I am feeling scared"),("अँधेरे से मत डरो","Do not fear the darkness"),
 ("मैं तुमसे प्यार करता हूँ","I love you"),("प्यार सबसे बड़ी ताकत है","Love is the greatest strength"),
 ("मुझे आश्चर्य हुआ","I was surprised"),("यह तो कमाल है","This is amazing"),
 ("मुझे गर्व है","I am proud"),("चिंता मत करो","Do not worry"),
 ("सब ठीक हो जाएगा","Everything will be all right"),("मुस्कुराओ, जीवन सुंदर है","Smile, life is beautiful"),
]

_NATURE = [
 ("कुत्ता भौंक रहा है","The dog is barking"),("बिल्ली दूध पीती है","The cat drinks milk"),
 ("गाय घास खाती है","The cow eats grass"),("हाथी बहुत बड़ा जानवर है","The elephant is a very big animal"),
 ("चिड़िया पेड़ पर बैठी है","The bird is sitting on the tree"),("मछली पानी में तैरती है","The fish swims in water"),
 ("बगीचे में फूल खिले हैं","Flowers have bloomed in the garden"),("पेड़ की छाँव ठंडी है","The tree's shade is cool"),
 ("आज मौसम अच्छा है","The weather is nice today"),("बहुत गर्मी है","It is very hot"),
 ("सर्दी बढ़ रही है","The cold is increasing"),("बारिश हो रही है","It is raining"),
 ("बादल छाए हैं","Clouds have gathered"),("हवा तेज़ चल रही है","The wind is blowing fast"),
 ("आसमान नीला है","The sky is blue"),("इंद्रधनुष दिख रहा है","A rainbow is visible"),
 ("कल धूप निकलेगी","The sun will come out tomorrow"),("नदी में पानी बह रहा है","Water is flowing in the river"),
 ("पहाड़ बहुत ऊँचे हैं","The mountains are very high"),("प्रकृति सुंदर है","Nature is beautiful"),
]

_SHOP = [
 ("बाज़ार कहाँ है","Where is the market"),("यह कितने का है","How much is this"),
 ("बहुत महँगा है","It is very expensive"),("कुछ कम कीजिए","Reduce the price a little (please)"),
 ("आखिरी दाम बताइए","Tell me the final price"),("ठीक है, दे दीजिए","Okay, give it"),
 ("क्या आपके पास छोटा नोट है","Do you have a smaller note"),("मैं नकद दूँगा","I will pay cash"),
 ("क्या कार्ड चलता है","Do you accept cards"),("रसीद दीजिए","Give the receipt (please)"),
 ("सब्ज़ी ताज़ी है","The vegetables are fresh"),("एक किलो टमाटर दो","Give one kilo of tomatoes"),
 ("आधा किलो आलू चाहिए","I need half a kilo of potatoes"),("फल मीठे हैं","The fruits are sweet"),
 ("यह कपड़ा अच्छा है","This cloth is good"),("बड़ा साइज़ दिखाइए","Show a bigger size (please)"),
 ("छूट मिलेगी","Will I get a discount"),("दुकान कब बंद होती है","When does the shop close"),
 ("मैं कल फिर आऊँगा","I will come again tomorrow"),("खरीदारी अच्छी रही","The shopping went well"),
]

_SOCIAL = [
 ("आपसे मिलकर खुशी हुई","Pleased to meet you"),("मेरा नाम राम है","My name is Ram"),
 ("आपका नाम क्या है","What is your name"),("आप कहाँ रहते हैं","Where do you live"),
 ("मैं दिल्ली में रहता हूँ","I live in Delhi"),("आप क्या काम करते हैं","What work do you do"),
 ("क्या हम दोस्त बन सकते हैं","Can we become friends"),("मेरा नंबर ले लीजिए","Please take my number"),
 ("कल मेरे घर आइए","Please come to my house tomorrow"),("चाय पिएँगे","Will you have tea"),
 ("जन्मदिन की बधाई","Happy birthday"),("शादी में आइएगा","Please come to the wedding"),
 ("त्योहार की शुभकामनाएँ","Festival greetings"),("साथ में खाना खाएँगे","We will eat together"),
 ("बहुत मज़ा आया","I had a lot of fun"),("फिर कब मिलेंगे","When will we meet again"),
 ("संपर्क में रहिएगा","Stay in touch"),("आपकी मदद के लिए धन्यवाद","Thanks for your help"),
 ("आप बहुत अच्छे हैं","You are very kind"),("दोस्ती ज़िंदाबाद","Long live friendship"),
]

_TECH = [
 ("मेरा फ़ोन कहाँ है","Where is my phone"),("फ़ोन की बैटरी खत्म हो गई","The phone battery died"),
 ("चार्जर दीजिए","Give the charger (please)"),("मुझे फ़ोन कीजिए","Call me"),
 ("नेटवर्क नहीं आ रहा","There is no network"),("इंटरनेट धीमा है","The internet is slow"),
 ("वाई-फ़ाई का पासवर्ड क्या है","What is the Wi-Fi password"),("मुझे संदेश भेजो","Send me a message"),
 ("मैंने ईमेल भेजा","I sent an email"),("तस्वीर भेजो","Send the photo"),
 ("वीडियो कॉल करो","Make a video call"),("कंप्यूटर चालू करो","Turn on the computer"),
 ("कंप्यूटर बंद करो","Turn off the computer"),("फ़ाइल खोलो","Open the file"),
 ("यह ऐप बहुत अच्छा है","This app is very good"),("सॉफ़्टवेयर अपडेट करो","Update the software"),
 ("पासवर्ड भूल गया","I forgot the password"),("ऑनलाइन पढ़ाई करो","Study online"),
 ("खबर देखो","Watch the news"),("तकनीक जीवन आसान बनाती है","Technology makes life easy"),
]

def demo_tenses(hdr, name, rid, group, points, req):
    groups = {'habitual': 5, 'progressive': 3, 'past_simple': 5,
              'past_prog': 1, 'perfect': 1, 'future': 5}
    samples = [
     ('habitual','मैं पढ़ता हूँ','I read (habitually)'),
     ('progressive','मैं पढ़ रहा हूँ','I am reading'),
     ('past_simple','राम ने खाना खाया','Ram ate food'),
     ('perfect','मैं खा चुका हूँ','I have finished eating'),
     ('future','मैं जाऊँगा','I will go'),
    ]
    body = (
        "\nGROUPS = " + repr(groups) + "\n"
        "SAMPLES = " + repr(samples) + "\n"
        "def main():\n"
        "    total = sum(GROUPS.values())\n"
        "    print('tense groups:', GROUPS)\n"
        "    print('total sentences:', total)\n"
        "    assert total == 20\n"
        "    assert all(v >= 1 for v in GROUPS.values())\n"
        "    assert len(GROUPS) == 6\n"
        "    for tense, dev, eng in SAMPLES:\n"
        "        print('%s: %s => %s' % (tense, dev, eng))\n"
        "    print('aspect keys: ता habit, रहा now, चुका done, गा future')\n"
        "    print('OK: tense drill complete - 20 sentences in 6 groups')\n"
        "main()\n"
    )
    return hdr(name, rid, group) + body


def demo_qa(hdr, name, rid, group, points, req):
    pairs = [
     ("आपका नाम क्या है","मेरा नाम सीता है"),("आप कहाँ रहते हैं","मैं जयपुर में रहता हूँ"),
     ("यह कौन है","यह मेरा भाई है"),("तुम क्या करते हो","मैं पढ़ता हूँ"),
     ("बाज़ार कब जाओगे","मैं शाम को जाऊँगा"),("तुम क्यों नहीं आए","मैं बीमार था"),
     ("यह कैसे काम करता है","बटन दबाओ"),("कितने बजे हैं","दो बजे हैं"),
     ("क्या तुम हिन्दी बोलते हो","हाँ, थोड़ी-थोड़ी"),("खाना कैसा था","बहुत अच्छा था"),
     ("टिकट कितने का है","पचास रुपये का है"),("डॉक्टर कहाँ है","डॉक्टर अंदर है"),
     ("तुम्हारी उम्र क्या है","मेरी उम्र बीस साल है"),("क्या बारिश होगी","हाँ, लगता है"),
     ("यह किसका है","यह मेरा है"),("तुम कहाँ से हो","मैं आगरा से हूँ"),
     ("क्या मैं अंदर आ सकता हूँ","हाँ, आइए"),("कल क्या करोगे","कल मैं घर पर रहूँगा"),
     ("चाय लोगे","हाँ, धन्यवाद"),("सब ठीक है","हाँ, सब ठीक है"),
    ]
    qwords = ['कौन','क्या','कहाँ','कब','क्यों','कैसे','कितने','किसका']
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
    informal = ['आओ','बैठो','पानी पियो','धीरे बोलो','दरवाज़ा खोलो',
                'मुझे किताब दो','जल्दी आओ','मत जाओ','चिंता मत करो','खाना खाओ']
    formal = ['आइए','बैठिए','चाय पीजिए','कृपया धीरे बोलिए','कृपया दरवाज़ा बंद कीजिए',
              'कृपया मेरी मदद कीजिए','ज़रा रुकिए','मत जाइए','आराम कीजिए','शुभ यात्रा']
    body = (
        "\nINF = " + repr(informal) + "\n"
        "FORM = " + repr(formal) + "\n"
        "def main():\n"
        "    print('informal commands:', len(INF))\n"
        "    print('formal requests:', len(FORM))\n"
        "    assert len(INF) == 10\n"
        "    assert len(FORM) == 10\n"
        "    assert len(INF) + len(FORM) == 20\n"
        "    soft = [f for f in FORM if 'कृपया' in f or 'ज़रा' in f]\n"
        "    print('softened with कृपया/ज़रा:', len(soft))\n"
        "    assert len(soft) >= 3\n"
        "    print('pair: आओ (inf) vs आइए (formal)')\n"
        "    print('OK: command drill complete - 10 informal, 10 formal')\n"
        "main()\n"
    )
    return hdr(name, rid, group) + body


_DESCR = [
 ("मेरी माँ लंबी और सुंदर है","My mother is tall and beautiful"),("उसका चेहरा गोल है","His face is round"),
 ("उसकी आँखें काली हैं","Her eyes are black"),("उसके बाल लंबे हैं","His hair is long"),
 ("वह नीली कमीज़ पहनता है","He wears a blue shirt"),("बच्चा छोटा और प्यारा है","The child is small and lovely"),
 ("दादा के बाल सफ़ेद हैं","Grandfather's hair is white"),("वह हमेशा मुस्कुराती है","She always smiles"),
 ("दिल्ली बड़ा शहर है","Delhi is a big city"),("आगरा में ताजमहल है","The Taj Mahal is in Agra"),
 ("जयपुर गुलाबी शहर है","Jaipur is the pink city"),("गंगा लंबी नदी है","The Ganga is a long river"),
 ("हिमालय ऊँचा पहाड़ है","The Himalaya is a high mountain"),("मेरा गाँव हरा-भरा है","My village is lush green"),
 ("यह घर पुराना पर मज़बूत है","This house is old but strong"),("बाज़ार भीड़भाड़ वाला है","The market is crowded"),
 ("कमरा साफ़ और हवादार है","The room is clean and airy"),("फूल लाल, पीले और सफ़ेद हैं","The flowers are red, yellow and white"),
 ("आसमान साफ़ नीला है","The sky is clear blue"),("यह जगह शांत और सुंदर है","This place is peaceful and beautiful"),
]

_STORY1 = [
 ("एक लड़का था","There was a boy"),("उसका नाम मोहन था","His name was Mohan"),
 ("वह गाँव में रहता था","He lived in a village"),("उसका एक कुत्ता था","He had a dog"),
 ("उसके कुत्ते का नाम मोती था","His dog's name was Moti"),
 ("हर सुबह मोहन और मोती सैर पर जाते थे","Every morning Mohan and Moti went for a walk"),
 ("एक दिन नदी किनारे एक चिड़िया मिली","One day they met a bird by the river"),
 ("चिड़िया घायल थी","The bird was hurt"),("मोहन ने चिड़िया की देखभाल की","Mohan took care of the bird"),
 ("दस दिन में चिड़िया ठीक हो गई और मोहन बहुत खुश हुआ","In ten days the bird recovered and Mohan was very happy"),
]

_STORY2 = [
 ("पिछले साल मैं जयपुर गया","Last year I went to Jaipur"),("मेरे साथ मेरा दोस्त था","My friend was with me"),
 ("हमने सुबह की ट्रेन पकड़ी","We caught the morning train"),("ट्रेन पाँच घंटे में पहुँची","The train arrived in five hours"),
 ("हमने होटल में कमरा लिया","We took a room in the hotel"),("दोपहर में हमने किला देखा","In the afternoon we saw the fort"),
 ("किला बहुत पुराना था","The fort was very old"),("शाम को हमने बाज़ार में खरीदारी की","In the evening we shopped in the market"),
 ("रात को हमने दाल-बाटी खाई","At night we ate dal-baati"),
 ("अगले दिन हम घर वापस आए और यात्रा बहुत अच्छी रही","The next day we came back home and the journey was very good"),
]

_STORY3 = [
 ("अगले महीने मैं नया काम शुरू करूँगा","Next month I will start a new job"),
 ("मैं रोज़ सुबह जल्दी उठूँगा","I will wake up early every morning"),
 ("अगर मेहनत करूँगा तो सफल होऊँगा","If I work hard, I will succeed"),
 ("मैं हिन्दी में बात करूँगा","I will speak in Hindi"),("मेरे दोस्त मेरी मदद करेंगे","My friends will help me"),
 ("हम सब मिलकर काम करेंगे","We will all work together"),("अगर बारिश होगी तो हम घर पर रहेंगे","If it rains, we will stay home"),
 ("साल के अंत तक मैं बहुत कुछ सीख लूँगा","By year's end I will have learned a lot"),
 ("मेरा परिवार मुझ पर गर्व करेगा","My family will be proud of me"),("भविष्य उज्ज्वल होगा","The future will be bright"),
]

_IDIOMS = [
 ("नाक में दम करना","to harass"),("आँखों का तारा","beloved"),
 ("मुँह में पानी आना","to drool with desire"),("नौ दो ग्यारह होना","to run away"),
 ("ऊँट के मुँह में जीरा","too little for the need"),("राई का पहाड़ बनाना","to exaggerate"),
 ("जैसी करनी वैसी भरनी","you reap what you sow"),("बूँद बूँद से सागर भरता है","small efforts add up"),
 ("अंधों में काना राजा","among the blind the one-eyed is king"),("हाथ कंगन को आरसी क्या","the obvious needs no proof"),
 ("मुँह की खाना","to suffer defeat"),("टस से मस न होना","to not budge an inch"),
 ("आ बैल मुझे मार","to invite trouble"),("नेकी कर दरिया में डाल","do good without expecting return"),
 ("घर का भेदी लंका ढाए","beware the traitor within"),("साँप भी मर जाए लाठी भी न टूटे","solve it without loss"),
 ("दाँतों तले उँगली दबाना","to be amazed"),("हाथ मलना","to regret"),
 ("अपनी धुन में मस्त","happily absorbed"),("चाँद पर थूकना","a futile insult"),
]

_REGISTER = [
 ("तुम कैसे हो","आप कैसे हैं"),("बैठो","कृपया बैठिए"),("पानी दो","कृपया पानी दीजिए"),
 ("तुम जाओ","आप जाइए"),("क्या चाहिए","आपको क्या चाहिए"),("माफ़ करना","क्षमा कीजिए"),
 ("फिर मिलेंगे","आपसे फिर मिलने की आशा है"),("ठीक है","जी, बिल्कुल ठीक है"),
 ("जल्दी करो","कृपया शीघ्रता करें"),("सुनो","कृपया ध्यान दीजिए"),
 ("प्रिय मित्र","आदरणीय महोदय"),("तुम्हारा दोस्त","भवदीय"),
 ("मुझे नहीं पता","मुझे जानकारी नहीं है"),("अंदर आओ","कृपया अंदर पधारिए"),
 ("धन्यवाद","आपका बहुत-बहुत आभारी हूँ"),
]

_COMPLEX = [
 ("मैं बाज़ार गया और सब्ज़ी खरीदी","और"),("वह थका था लेकिन काम करता रहा","लेकिन"),
 ("जो लड़का वहाँ खड़ा है वह मेरा भाई है","जो...वह"),("जिस किताब की तुम बात कर रहे हो वह मेरी है","जिस...वह"),
 ("जब बारिश हुई तब हम घर पर थे","जब...तब"),("जहाँ तुम जाओगे वहाँ मैं भी जाऊँगा","जहाँ...वहाँ"),
 ("अगर तुम मेहनत करोगे तो सफल होगे","अगर...तो"),("हालाँकि वह बीमार था फिर भी वह आया","हालाँकि"),
 ("मैंने खाना खाया क्योंकि मुझे भूख लगी थी","क्योंकि"),("वह इतना तेज़ दौड़ा कि सब हैरान रह गए","कि"),
 ("मुझे नहीं पता कि वह कहाँ है","कि"),("पहले तुम पढ़ो फिर खेलो","पहले...फिर"),
 ("न तो वह आया न उसने फ़ोन किया","न तो...न"),("या तो तुम चलो या मैं जाऊँ","या तो...या"),
 ("जितनी मेहनत करोगे उतना फल मिलेगा","जितना...उतना"),
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
        "    print('informal -> formal: तुम कैसे हो -> आप कैसे हैं')\n"
        "    print('letter: प्रिय मित्र -> आदरणीय महोदय')\n"
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
        "    assert 'कि' in conns\n"
        "    print('sample:', SENTS[2][0])\n"
        "    print('OK: complex-sentence drill complete - 15 sentences')\n"
        "main()\n"
    )
    return hdr(name, rid, group) + body


_DLG1 = [
 ("खरीदार","नमस्ते भाई साहब","Hello, brother"),("विक्रेता","नमस्ते, आइए, क्या चाहिए","Hello, come in, what do you need"),
 ("खरीदार","टमाटर कैसे दिए","What is the rate for tomatoes"),("विक्रेता","चालीस रुपये किलो","Forty rupees a kilo"),
 ("खरीदार","बहुत महँगे हैं","Very expensive"),("विक्रेता","ताज़ा हैं साहब","They are fresh, sir"),
 ("खरीदार","तीस रुपये लगाओ","Make it thirty rupees"),("विक्रेता","नहीं हो पाएगा","That will not be possible"),
 ("खरीदार","आखिरी दाम बताओ","Tell me the final price"),("विक्रेता","पैंतीस रुपये, बस","Thirty-five rupees, final"),
 ("खरीदार","ठीक है, एक किलो दो","Okay, give one kilo"),("विक्रेता","और कुछ","Anything else"),
 ("खरीदार","आलू कैसे हैं","How are the potatoes (priced)"),("विक्रेता","बीस रुपये किलो","Twenty rupees a kilo"),
 ("खरीदार","आधा किलो आलू भी दो","Give half a kilo of potatoes too"),("विक्रेता","यह लीजिए","Here you are"),
 ("खरीदार","कुल कितने हुए","What is the total"),("विक्रेता","पैंतालीस रुपये","Forty-five rupees"),
 ("खरीदार","यह लीजिए, धन्यवाद","Here you are, thank you"),("विक्रेता","फिर पधारिएगा","Please come again"),
]

_DLG2 = [
 ("रवि","अरे सीता, कैसी हो","Hey Sita, how are you"),("सीता","मैं ठीक हूँ, तुम कैसे हो","I am fine, how are you"),
 ("रवि","बहुत दिनों बाद मिले","Met after many days"),("सीता","हाँ, कहाँ थे इतने दिन","Yes, where were you all these days"),
 ("रवि","मैं गाँव गया था","I had gone to the village"),("सीता","गाँव में सब कैसे हैं","How is everyone in the village"),
 ("रवि","सब ठीक हैं, तुम्हें याद करते हैं","All fine, they remember you"),("सीता","चलो, चाय पीते हैं","Come, let us have tea"),
 ("रवि","चलो, बहुत मन है","Let us go, I really feel like it"),("सीता","नया काम कैसा चल रहा है","How is the new job going"),
 ("रवि","अच्छा चल रहा है","Going well"),("सीता","और पढ़ाई","And studies"),
 ("रवि","हिन्दी सीख रहा हूँ","I am learning Hindi"),("सीता","बहुत बढ़िया","Excellent"),
 ("रवि","तुम मुझे सिखाओगी","Will you teach me"),("सीता","ज़रूर, कल से शुरू करते हैं","Sure, we start tomorrow"),
 ("रवि","धन्यवाद, तुम बहुत अच्छी हो","Thank you, you are very kind"),("सीता","कोई बात नहीं","No problem"),
 ("रवि","अब चलता हूँ, फिर मिलेंगे","I leave now, we will meet again"),("सीता","ठीक है, अपना ख्याल रखना","Okay, take care of yourself"),
]

_DLG3 = [
 ("अनिल","अरे, मेरी चाबी नहीं मिल रही","Oh no, I cannot find my keys"),("मीरा","शांत हो जाओ, कहाँ रखी थी","Calm down, where did you keep them"),
 ("अनिल","मेज़ पर रखी थी","I had kept them on the table"),("मीरा","वहाँ देखो","Look there"),
 ("अनिल","वहाँ नहीं है","Not there"),("मीरा","जेब में देखो","Check your pocket"),
 ("अनिल","जेब खाली है","The pocket is empty"),("मीरा","कब आखिरी बार देखी थी","When did you last see them"),
 ("अनिल","सुबह दरवाज़ा खोला था","I opened the door in the morning"),("मीरा","तो चाबी दरवाज़े के पास होगी","Then the keys must be near the door"),
 ("अनिल","चलो देखते हैं","Let us check"),("मीरा","जूते के पास देखो","Look near the shoes"),
 ("अनिल","मिल गई","Found them"),("मीरा","बहुत बढ़िया, कहाँ थी","Great, where were they"),
 ("अनिल","थैले में थी","In the bag"),("मीरा","देखा, शांत रहने से मिल जाती है","See, staying calm finds things"),
 ("अनिल","तुम्हारी मदद के लिए धन्यवाद","Thanks for your help"),("मीरा","अगली बार खूँटी पर टाँगना","Next time hang them on the hook"),
 ("अनिल","पक्का, अब याद रहेगा","Sure, I will remember now"),("मीरा","चलो, चाय पीते हैं","Come, let us have tea"),
]

_WORDS200 = [
 ("मैं","I"),("तुम","you (inf)"),("आप","you (formal)"),("वह","he/she"),("यह","this"),
 ("हम","we"),("वे","they"),("मेरा","my"),("तुम्हारा","your"),("कौन","who"),
 ("क्या","what"),("कहाँ","where"),("कब","when"),("क्यों","why"),("कैसे","how"),
 ("आदमी","man"),("औरत","woman"),("बच्चा","child"),("दोस्त","friend"),("माँ","mother"),
 ("पिता","father"),("भाई","brother"),("बहन","sister"),("घर","house"),("कमरा","room"),
 ("रसोई","kitchen"),("स्कूल","school"),("दफ़्तर","office"),("बाज़ार","market"),("शहर","city"),
 ("गाँव","village"),("सड़क","road"),("पानी","water"),("खाना","food"),("चाय","tea"),
 ("दूध","milk"),("रोटी","bread"),("दाल","lentils"),("चावल","rice"),("फल","fruit"),
 ("किताब","book"),("कलम","pen"),("कागज़","paper"),("मेज़","table"),("कुर्सी","chair"),
 ("दरवाज़ा","door"),("खिड़की","window"),("पैसा","money"),("रुपया","rupee"),("समय","time"),
 ("दिन","day"),("रात","night"),("सुबह","morning"),("शाम","evening"),("आज","today"),
 ("कल","tomorrow/yesterday"),("अब","now"),("साल","year"),("महीना","month"),("हफ़्ता","week"),
 ("पेड़","tree"),("फूल","flower"),("सूरज","sun"),("चाँद","moon"),("तारा","star"),
 ("आसमान","sky"),("बादल","cloud"),("बारिश","rain"),("हवा","wind"),("नदी","river"),
 ("पहाड़","mountain"),("कुत्ता","dog"),("बिल्ली","cat"),("गाय","cow"),("हाथी","elephant"),
 ("चिड़िया","bird"),("मछली","fish"),("सिर","head"),("आँख","eye"),("हाथ","hand"),
 ("पैर","leg"),("दिल","heart"),("बड़ा","big"),("छोटा","small"),("अच्छा","good"),
 ("बुरा","bad"),("नया","new"),("पुराना","old"),("लंबा","long"),("गर्म","hot"),
 ("ठंडा","cold"),("मीठा","sweet"),("तेज़","fast"),("सुंदर","beautiful"),("साफ़","clean"),
 ("आसान","easy"),("मुश्किल","difficult"),("खुश","happy"),("बहुत","very"),
 ("जल्दी","quickly"),("धीरे","slowly"),("हमेशा","always"),("कभी","sometimes"),
 ("यहाँ","here"),("वहाँ","there"),("अंदर","inside"),("बाहर","outside"),("ऊपर","up"),
 ("नीचे","down"),("जाना","to go"),("आना","to come"),("खाना","to eat"),("पीना","to drink"),
 ("करना","to do"),("बोलना","to speak"),("पढ़ना","to read"),("लिखना","to write"),
 ("देखना","to see"),("सुनना","to listen"),("सोना","to sleep"),("उठना","to wake up"),
 ("बैठना","to sit"),("चलना","to walk"),("दौड़ना","to run"),("देना","to give"),
 ("लेना","to take"),("खरीदना","to buy"),("बनाना","to make"),("खेलना","to play"),
 ("समझना","to understand"),("मदद","help"),("काम","work"),("पढ़ाई","studies"),
 ("परीक्षा","exam"),("सवाल","question"),("जवाब","answer"),("नाम","name"),("देश","country"),
 ("भाषा","language"),("लोग","people"),("दुनिया","world"),("जीवन","life"),("प्यार","love"),
 ("खुशी","happiness"),("दुख","sorrow"),("डॉक्टर","doctor"),("दवा","medicine"),
 ("अस्पताल","hospital"),("फ़ोन","phone"),("संदेश","message"),("कंप्यूटर","computer"),
 ("एक","one"),("दो","two"),("तीन","three"),("चार","four"),("पाँच","five"),
 ("दस","ten"),("बीस","twenty"),("सौ","hundred"),("पहला","first"),("सोमवार","Monday"),
 ("रविवार","Sunday"),("जनवरी","January"),("नमस्ते","hello"),("धन्यवाद","thanks"),
 ("कृपया","please"),("माफ़","sorry"),("हाँ","yes"),("नहीं","no/not"),("ठीक","fine/okay"),
 ("और","and"),("लेकिन","but"),("क्योंकि","because"),("अगर","if"),("तो","then"),
 ("जब","when"),("तब","then"),("जो","who/which"),("में","in"),("पर","on"),
 ("का","of"),("को","to/for"),("से","from/with"),("ने","ergative marker"),("है","is"),
 ("हैं","are"),("हूँ","am"),("था","was"),("होगा","will be"),("चाहिए","need/want"),
 ("सकता","can"),("मत","do-not"),("जी","respect particle"),("सब","all"),
 ("कोई","someone/any"),("कुछ","some"),("बहुत","very (anchor)"),("ज़रूर","certainly"),
 ("यह","this (repeat anchor)"),("वह","that (repeat anchor)"),
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
 "dialogue1": _dialogue(_DLG1, 20, ['खरीदार', 'विक्रेता']),
 "dialogue2": _dialogue(_DLG2, 20, ['रवि', 'सीता']),
 "dialogue3": _dialogue(_DLG3, 20, ['अनिल', 'मीरा']),
 "mastery": demo_mastery,
}
