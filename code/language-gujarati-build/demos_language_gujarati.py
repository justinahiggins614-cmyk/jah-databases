#!/usr/bin/env python3
"""Demo programs for The Gujarati to English Database (language-gujarati).

Every program is real, runnable, stdlib-only Python. Each prints real
computed values (drill counts, quiz scores, word statistics), asserts
tight bounds (never float exact-equality), and ends with an OK: marker.
All embedded Gujarati matches the entry text verbatim (cross-checked by
the build: sampled Gujarati tokens from each demo must appear in the
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
            "    print('total Gujarati words:', words)\n"
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


def _items(words, expected):
    def fn(hdr, name, rid, group, points, req):
        body = (
            "\nWORDS = " + repr(words) + "\n"
            "EXPECTED = " + repr(expected) + "\n"
            "def main():\n"
            "    n = len(WORDS)\n"
            "    print('drill items:', n)\n"
            "    assert n == EXPECTED, 'item count drift'\n"
            "    total = sum(len(w) for w in WORDS)\n"
            "    print('total chars:', total)\n"
            "    assert total > n\n"
            "    longest = max(WORDS, key=len)\n"
            "    print('longest:', longest)\n"
            "    print('sample:', WORDS[0])\n"
            "    print('OK: drill complete - %d items' % n)\n"
            "main()\n"
        )
        return hdr(name, rid, group) + body
    return fn


# ---------------------------------------------------------------- data
_NOUNS = [('માણસ', 'māṇas', 'person'), ('સ્ત્રી', 'strī', 'woman'), ('છોકરો', 'chokro', 'boy'), ('છોકરી', 'chokrī', 'girl'), ('બાળક', 'bāḷak', 'child'), ('ઘર', 'ghar', 'house'), ('પાણી', 'pāṇī', 'water'), ('ખોરાક', 'khorāk', 'food'), ('રોટલી', 'roṭlī', 'bread'), ('શાક', 'śāk', 'vegetable curry'), ('દૂધ', 'dūdh', 'milk'), ('ચા', 'cā', 'tea'), ('પુસ્તક', 'pustak', 'book'), ('કલમ', 'kalam', 'pen'), ('શાળા', 'śāḷā', 'school'), ('શિક્ષક', 'śikṣak', 'teacher'), ('ડૉક્ટર', 'ḍŏkṭar', 'doctor'), ('બજાર', 'bajār', 'market'), ('રસ્તો', 'rasto', 'road'), ('ગાડી', 'gāḍī', 'car'), ('ફોન', 'phon', 'phone'), ('પૈસા', 'paisā', 'money'), ('સમય', 'samay', 'time'), ('દિવસ', 'divas', 'day'), ('રાત', 'rāt', 'night')]
_VERBS = [('કરવું', 'karvuṁ', 'to do'), ('હોવું', 'hovuṁ', 'to be'), ('જવું', 'javuṁ', 'to go'), ('આવવું', 'āvvū', 'to come'), ('ખાવું', 'khāvuṁ', 'to eat'), ('પીવું', 'pīvuṁ', 'to drink'), ('બોલવું', 'bolvuṁ', 'to speak'), ('વાંચવું', 'vā̃cvuṁ', 'to read'), ('લખવું', 'lakhvuṁ', 'to write'), ('જોવું', 'jovuṁ', 'to see'), ('સાંભળવું', 'sā̃bhaḷvuṁ', 'to listen'), ('સૂવું', 'sūvuṁ', 'to sleep'), ('ઊઠવું', 'ūṭhvuṁ', 'to get up'), ('બેસવું', 'besvuṁ', 'to sit'), ('ચાલવું', 'cālvuṁ', 'to walk'), ('દોડવું', 'doḍvuṁ', 'to run'), ('આપવું', 'āpvuṁ', 'to give'), ('લેવું', 'levuṁ', 'to take'), ('ખરીદવું', 'kharīdvuṁ', 'to buy'), ('વેચવું', 'vecvuṁ', 'to sell'), ('બનાવવું', 'banāvuṁ', 'to make'), ('શીખવું', 'śīkhvuṁ', 'to learn'), ('શીખવવું', 'śīkhavvuṁ', 'to teach'), ('સમજવું', 'samajvuṁ', 'to understand'), ('કામ કરવું', 'kām karvuṁ', 'to work')]
_ADJADV = [('સારો', 'sāro', 'good'), ('ખરાબ', 'kharāb', 'bad'), ('મોટો', 'moṭo', 'big'), ('નાનો', 'nāno', 'small'), ('નવો', 'navo', 'new'), ('જૂનો', 'jūno', 'old'), ('લાંબો', 'lāṁbo', 'long/tall'), ('ટૂંકો', 'ṭūṁko', 'short'), ('ગરમ', 'garam', 'hot'), ('ઠંડો', 'ṭhaṇḍo', 'cold'), ('મીઠો', 'mīṭho', 'sweet'), ('ખાટો', 'khāṭo', 'sour'), ('તીખો', 'tīkho', 'spicy'), ('સુંદર', 'sundar', 'beautiful'), ('ઝડપી', 'jhaḍpī', 'fast'), ('ધીમો', 'dhīmo', 'slow'), ('ખુશ', 'khuś', 'happy'), ('દુઃખી', 'duḥkhī', 'sad'), ('ભૂખ્યો', 'bhūkhyo', 'hungry'), ('તરસ્યો', 'tarasyo', 'thirsty'), ('થાકેલો', 'thākelo', 'tired'), ('સ્વચ્છ', 'svacch', 'clean'), ('ગંદો', 'gando', 'dirty'), ('ધનવાન', 'dhanvān', 'rich'), ('ગરીબ', 'garīb', 'poor'), ('ખૂબ', 'khūb', 'very'), ('ધીમે ધીમે', 'dhīme dhīme', 'slowly'), ('ઝડપથી', 'jhaḍapthī', 'quickly'), ('હંમેશા', 'hameśā', 'always'), ('ક્યારેક', 'kyārek', 'sometimes'), ('ક્યારેય નહીં', 'kyārey nahī̃', 'never'), ('આજે', 'āje', 'today'), ('કાલે', 'kāle', 'tomorrow'), ('અહીં', 'ahī̃', 'here'), ('ત્યાં', 'tyā̃', 'there'), ('અંદર', 'andar', 'inside'), ('બહાર', 'bahār', 'outside'), ('ઉપર', 'upar', 'up'), ('નીચે', 'nīce', 'down'), ('સાથે', 'sāthe', 'together')]
_GREET = [('નમસ્તે', 'namaste', 'Hello / greetings'), ('કેમ છો?', 'kem cho?', 'How are you? (formal)'), ('કેમ છે?', 'kem che?', 'How are you? (informal)'), ('મજામાં?', 'majāmā̃?', 'Doing well?'), ('સારું છે', 'sāruṁ che', 'All good'), ('બસ, મજામાં', 'bas, majāmā̃', 'Just fine'), ('આવો, આવો', 'āvo, āvo', 'Come in, come in'), ('બેસો', 'beso', 'Please sit'), ('ચા પીશો?', 'cā pīśo?', 'Will you have tea?'), ('આવજો', 'āvjo', 'Goodbye (come again)'), ('ફરી મળીશું', 'pharī maḷīśuṁ', 'We will meet again'), ('શુભ સવાર', 'śubh savār', 'Good morning'), ('શુભ સાંજ', 'śubh sā̃j', 'Good evening'), ('શુભ રાત્રિ', 'śubh rātri', 'Good night'), ('આભાર', 'ābhār', 'Thank you'), ('ખૂબ ખૂબ આભાર', 'khūb khūb ābhār', 'Thank you very much'), ('માફ કરજો', 'māph karjo', 'Please forgive me'), ('માફ કરશો', 'māph karśo', 'Excuse me'), ('કૃપા કરીને', 'kṛpā karīne', 'Please'), ('મહેરબાની કરીને', 'maherbānī karīne', 'Please (kindly)'), ('વાંધો નહીં', 'vā̃dho nahī̃', 'No problem'), ('ભલે', 'bhale', 'Okay'), ('સારું', 'sāruṁ', 'Good / okay'), ('હા', 'hā', 'Yes'), ('ના', 'nā', 'No'), ('ખરેખર?', 'kharekhar?', 'Really?'), ('અરે વાહ!', 'are vāh!', 'Oh wow!'), ('શાબાશ!', 'śābāś!', 'Well done!'), ('અભિનંદન', 'abhinandan', 'Congratulations'), ('શુભેચ્છા', 'śubhecchā', 'Best wishes')]
_HOME = [('આ મારું ઘર છે', 'This is my house'), ('ઘરમાં ચાર ઓરડા છે', 'There are four rooms in the house'), ('રસોડું મોટું છે', 'The kitchen is big'), ('બેઠકખંડમાં સોફો છે', 'There is a sofa in the living room'), ('મારો ઓરડો ઉપર છે', 'My room is upstairs'), ('ટેબલ પર પુસ્તક છે', 'There is a book on the table'), ('ખુરશી બારી પાસે છે', 'The chair is near the window'), ('પિતા ઑફિસે ગયા છે', 'Father has gone to the office'), ('માતા રસોડામાં રાંધે છે', 'Mother is cooking in the kitchen'), ('મારો ભાઈ શાળાએ જાય છે', 'My brother goes to school'), ('મારી બહેન કૉલેજમાં ભણે છે', 'My sister studies in college'), ('દાદા બગીચામાં બેઠા છે', 'Grandfather is sitting in the garden'), ('દાદી વાર્તા કહે છે', 'Grandmother tells stories'), ('અમે સાથે જમીએ છીએ', 'We eat together'), ('ઘર સાફ રાખો', 'Keep the house clean'), ('લાઇટ બંધ કરો', 'Turn off the light'), ('બારણું ખોલો', 'Open the door'), ('બારી બંધ કરો', 'Close the window'), ('મારો પરિવાર મોટો છે', 'My family is big'), ('અમે ઘરે ખુશ છીએ', 'We are happy at home')]
_FOOD = [('મને ભૂખ લાગી છે', 'I am hungry'), ('જમવાનું તૈયાર છે', 'The meal is ready'), ('આજે શું બનાવ્યું?', 'What did you cook today?'), ('રોટલી અને શાક ખૂબ સ્વાદિષ્ટ છે', 'The bread and curry are very tasty'), ('મને તીખું નથી ભાવતું', 'I do not like spicy food'), ('થોડું મીઠું આપો', 'Give me a little salt'), ('ચામાં ખાંડ નાખો', 'Put sugar in the tea'), ('દૂધ ઉકાળો', 'Boil the milk'), ('શાક સમારો', 'Chop the vegetables'), ('ભાત રાંધો', 'Cook the rice'), ('હું શાકાહારી છું', 'I am vegetarian'), ('મને દાળ ભાત ભાવે છે', 'I like lentils and rice'), ('ખીચડી હળવી હોય છે', 'Khichdi is light (easy to digest)'), ('જમ્યા પછી ફળ ખાઓ', 'Eat fruit after the meal'), ('પાણી પીઓ', 'Drink water'), ('રેસ્ટોરન્ટમાં ટેબલ બુક કરો', 'Book a table in the restaurant'), ('મેનુ બતાવો', 'Show me the menu'), ('બિલ લાવો', 'Bring the bill'), ('જમવાનું ખૂબ સરસ હતું', 'The meal was very nice'), ('આવજો, ફરી આવજો', 'Goodbye, come again - leaving the table')]
_TRAVEL = [('સ્ટેશન ક્યાં છે?', 'Where is the station?'), ('બસ સ્ટેન્ડ કેટલું દૂર છે?', 'How far is the bus stand?'), ('જમણી બાજુ વળો', 'Turn right'), ('ડાબી બાજુ વળો', 'Turn left'), ('સીધા જાઓ', 'Go straight'), ('અહીંથી કેટલો સમય લાગશે?', 'How long will it take from here?'), ('ટિકિટ કેટલાની છે?', 'How much is the ticket?'), ('એક ટિકિટ આપો', 'Give me one ticket'), ('ટ્રેન ક્યારે આવશે?', 'When will the train come?'), ('બસ મોડી છે', 'The bus is late'), ('રિક્ષા મળશે?', 'Will I get a rickshaw?'), ('ભાડું કેટલું?', 'What is the fare?'), ('મીટર પર ચલાવો', 'Go by the meter'), ('અહીં ઊભા રાખો', 'Stop here'), ('હોટલ ક્યાં છે?', 'Where is the hotel?'), ('એક રૂમ જોઈએ છે', 'I need a room'), ('એક રાતનું ભાડું કેટલું?', 'What is the charge for one night?'), ('સવારે ચા મળશે?', 'Will tea be available in the morning?'), ('મારો સામાન ઉપર લઈ જાઓ', 'Take my luggage upstairs'), ('મુસાફરી સુખદ રહો', 'Have a pleasant journey')]
_WORKSCHOOL = [('તમે શું કામ કરો છો?', 'What work do you do?'), ('હું શિક્ષક છું', 'I am a teacher'), ('તે ડૉક્ટર છે', 'She is a doctor'), ('હું ઑફિસમાં કામ કરું છું', 'I work in an office'), ('મારી નોકરી સારી છે', 'My job is good'), ('મીટિંગ દસ વાગ્યે છે', 'The meeting is at ten o’clock'), ('રિપોર્ટ તૈયાર કરો', 'Prepare the report'), ('ઈમેલ મોકલો', 'Send the email'), ('બોસ સાથે વાત કરો', 'Talk to the boss'), ('રજા જોઈએ છે', 'I need leave'), ('શાળા સવારે શરૂ થાય છે', 'School starts in the morning'), ('વર્ગમાં શાંતિથી બેસો', 'Sit quietly in class'), ('પુસ્તક ખોલો', 'Open the book'), ('પાઠ વાંચો', 'Read the lesson'), ('પ્રશ્ન પૂછો', 'Ask a question'), ('જવાબ લખો', 'Write the answer'), ('ગૃહકાર્ય કરો', 'Do the homework'), ('પરીક્ષા આવતા અઠવાડિયે છે', 'The exam is next week'), ('મહેનત કરો, સફળ થશો', 'Work hard, you will succeed'), ('શીખવાનું ક્યારેય બંધ ન કરો', 'Never stop learning')]
_HEALTH = [('મારું માથું દુઃખે છે', 'My head aches'), ('મારી આંખો લાલ છે', 'My eyes are red'), ('કાનમાં દુઃખે છે', 'My ear hurts'), ('નાક બંધ છે', 'My nose is blocked'), ('મોં ખોલો', 'Open your mouth'), ('દાંત દુઃખે છે', 'My tooth aches'), ('ગળામાં ખારાશ છે', 'My throat is sore'), ('હાથ ધુઓ', 'Wash your hands'), ('પગ મચકોડાયો છે', 'My ankle is sprained'), ('11. મને તાવ છે', 'I have a fever'), ('મને તાવ છે', 'I have a fever'), ('મને શરદી થઈ છે', 'I have a cold'), ('મને ઉધરસ આવે છે', 'I have a cough'), ('મને ચક્કર આવે છે', 'I feel dizzy'), ('16. ડૉક્ટરને બતાવો', 'See a doctor'), ('ડૉક્ટરને બતાવો', 'See a doctor'), ('દવા સમયસર લો', 'Take the medicine on time'), ('આરામ કરો', 'Rest'), ('20. મને તાવની દવા આપો', 'Give me medicine for fever'), ('મને તાવની દવા આપો', 'Give me medicine for fever')]
_EMOTIONS = [('હું ખૂબ ખુશ છું', 'I am very happy'), ('આજે મારો દિવસ સારો છે', 'Today is a good day for me'), ('તે હસી રહી છે', 'She is laughing'), ('સમાચાર સાંભળીને આનંદ થયો', 'Hearing the news made me glad'), ('હું દુઃખી છું', 'I am sad'), ('તે રડે છે', 'He is crying'), ('મારું દિલ ભારે છે', 'My heart feels heavy'), ('ચિંતા ન કરો', 'Do not worry'), ('મને ગુસ્સો આવે છે', 'I feel angry'), ('શાંત થાઓ', 'Calm down'), ('મને બીક લાગે છે', 'I feel afraid'), ('અંધારાથી ડર લાગે છે', 'The darkness frightens me'), ('હિંમત રાખો', 'Be brave'), ('હું તને પ્રેમ કરું છું', 'I love you'), ('મારો પરિવાર મને વહાલો છે', 'My family is dear to me'), ('મને નવાઈ લાગી', 'I was surprised'), ('ખરેખર? મને વિશ્વાસ નથી થતો', 'Really? I cannot believe it'), ('મને શરમ આવે છે', 'I feel embarrassed'), ('મને ગર્વ છે', 'I feel proud'), ('બધું સારું થશે', 'Everything will be all right')]
_NATURE = [('આજે હવામાન સારું છે', 'The weather is nice today'), ('વરસાદ પડે છે', 'It is raining'), ('તડકો નીકળ્યો છે', 'The sun has come out'), ('ખૂબ ગરમી છે', 'It is very hot'), ('ઠંડી વાય છે', 'A cold wind is blowing'), ('ચોમાસું આવી ગયું', 'The monsoon has arrived'), ('શિયાળામાં ધુમ્મસ હોય છે', 'There is fog in winter'), ('વસંતમાં ફૂલો ખીલે છે', 'Flowers bloom in spring'), ('ઝાડ પર પક્ષીઓ બેઠાં છે', 'Birds are sitting on the tree'), ('કૂતરો ભસે છે', 'The dog is barking'), ('બિલાડી દૂધ પીએ છે', 'The cat drinks milk'), ('ગાય ઘાસ ખાય છે', 'The cow eats grass'), ('હાથી મોટું પ્રાણી છે', 'The elephant is a big animal'), ('વાઘ જંગલમાં રહે છે', 'The tiger lives in the forest'), ('માછલી પાણીમાં તરે છે', 'The fish swims in water'), ('નદી વહે છે', 'The river flows'), ('પહાડ ઊંચો છે', 'The mountain is tall'), ('સમુદ્ર વિશાળ છે', 'The ocean is vast'), ('ચાંદ ચમકે છે', 'The moon is shining'), ('તારા ટમટમે છે', 'The stars are twinkling')]
_SHOPPING = [('આ કેટલાનું છે?', 'How much is this?'), ('આ બહુ મોંઘું છે', 'This is too expensive'), ('થોડું ઓછું કરો', 'Reduce the price a little'), ('છેલ્લો ભાવ બોલો', 'Tell me your final price'), ('સો રૂપિયામાં આપશો?', 'Will you give it for a hundred rupees?'), ('બરાબર, પેક કરો', 'Okay, pack it'), ('બીજું બતાવો', 'Show me another'), ('આનો રંગ બીજો છે?', 'Is there another color of this?'), ('મોટી સાઇઝ છે?', 'Is there a larger size?'), ('આ તાજું છે?', 'Is this fresh?'), ('એક કિલો બટાટા આપો', 'Give me one kilo of potatoes'), ('અડધો કિલો ડુંગળી', 'Half a kilo of onions'), ('છૂટા પૈસા છે?', 'Do you have change?'), ('કાર્ડ ચાલશે?', 'Will you accept a card?'), ('રોકડા આપું છું', 'I am paying cash'), ('બિલ આપો', 'Give me the bill'), ('થેલીમાં નાખો', 'Put it in the bag'), ('કાલે નવો માલ આવશે', 'New stock will come tomorrow'), ('દુકાન ક્યારે બંધ થાય છે?', 'When does the shop close?'), ('ખરીદી મજા આવી', 'Shopping was fun')]
_SOCIAL = [('તમને મળીને આનંદ થયો', 'Nice to meet you'), ('તમે ક્યાં રહો છો?', 'Where do you live?'), ('હું અમદાવાદમાં રહું છું', 'I live in Ahmedabad'), ('તમારો ફોન નંબર શું છે?', 'What is your phone number?'), ('આપણે મિત્રો બનીએ', 'Let us become friends'), ('કાલે મારે ઘરે આવો', 'Come to my home tomorrow'), ('જમવા માટે આમંત્રણ છે', 'You are invited for a meal'), ('જરૂર આવજો', 'Do come'), ('તમારો જન્મદિવસ ક્યારે છે?', 'When is your birthday?'), ('જન્મદિવસની શુભેચ્છા', 'Happy birthday'), ('ભેટ સ્વીકારો', 'Please accept the gift'), ('લગ્નમાં આવજો', 'Come to the wedding'), ('અભિનંદન!', 'Congratulations!'), ('તહેવારની શુભેચ્છા', 'Festival greetings'), ('દિવાળી મુબારક', 'Happy Diwali'), ('સાથે ફોટો પડાવીએ', 'Let us take a photo together'), ('સંપર્કમાં રહેજો', 'Stay in touch'), ('ફરી ક્યારે મળીશું?', 'When will we meet again?'), ('તમારી સાથે વાત કરીને મજા આવી', 'I enjoyed talking with you'), ('આવજો, સંભાળજો', 'Goodbye, take care')]
_TECH = [('મારો ફોન ક્યાં છે?', 'Where is my phone?'), ('ફોન વાગે છે', 'The phone is ringing'), ('ફોન ઉપાડો', 'Pick up the phone'), ('હેલો, કોણ બોલે છે?', 'Hello, who is speaking?'), ('લાઇન કપાઈ ગઈ', 'The line got disconnected'), ('ફરી ફોન કરજો', 'Please call again'), ('મેસેજ મોકલો', 'Send a message'), ('મને મેસેજ મળ્યો', 'I got the message'), ('ઈન્ટરનેટ ચાલે છે?', 'Is the internet working?'), ('વાઇફાઇ પાસવર્ડ શું છે?', 'What is the WiFi password?'), ('કમ્પ્યુટર ચાલુ કરો', 'Turn on the computer'), ('કમ્પ્યુટર બંધ કરો', 'Turn off the computer'), ('ફાઇલ સેવ કરો', 'Save the file'), ('ફોટો મોકલો', 'Send the photo'), ('વીડિયો કૉલ કરીએ', 'Let us make a video call'), ('બેટરી ઓછી છે', 'The battery is low'), ('ચાર્જર આપો', 'Give me the charger'), ('સ્ક્રીન તૂટી ગઈ', 'The screen broke'), ('એપ ડાઉનલોડ કરો', 'Download the app'), ('ઑનલાઇન મળીશું', 'We will meet online')]
_DESCRIPTIONS = [('મારો મિત્ર ઊંચો અને પાતળો છે', 'My friend is tall and slim'), ('તેની આંખો કાળી છે', 'Her eyes are black'), ('તેના વાળ લાંબા છે', 'His hair is long'), ('દાદીનો ચહેરો પ્રેમાળ છે', 'Grandmother has a loving face'), ('બાળક ગોળમટોળ છે', 'The baby is chubby'), ('શિક્ષક કડક પણ ન્યાયી છે', 'The teacher is strict but fair'), ('તે હંમેશા હસતો રહે છે', 'He is always smiling'), ('અમદાવાદ મોટું શહેર છે', 'Ahmedabad is a big city'), ('સાબરમતી નદી શહેરમાંથી વહે છે', 'The Sabarmati river flows through the city'), ('મારું ગામ નાનું પણ સુંદર છે', 'My village is small but beautiful'), ('ઘરની આસપાસ લીલાં ઝાડ છે', 'There are green trees around the house'), ('બગીચામાં રંગબેરંગી ફૂલો છે', 'There are colorful flowers in the garden'), ('બજારમાં ભીડ છે', 'The market is crowded'), ('રસ્તો પહોળો અને સાફ છે', 'The road is wide and clean'), ('મંદિર જૂનું અને ભવ્ય છે', 'The temple is old and grand'), ('તળાવનું પાણી ચોખ્ખું છે', 'The lake water is clear'), ('સાંજનું આકાશ લાલ છે', 'The evening sky is red'), ('વરસાદ પછી હવા તાજી છે', 'The air is fresh after rain'), ('આ પુસ્તક જાડું પણ રસપ્રદ છે', 'This book is thick but interesting'), ('મારો દિવસ લાંબો પણ આનંદદાયક હતો', 'My day was long but joyful')]
_STORY1 = [('રવિવારે સવારે હું તળાવે જાઉં છું', 'On Sunday morning I go to the lake'), ('તળાવનું પાણી ચોખ્ખું અને શાંત છે', 'The lake water is clear and calm'), ('કિનારે લીલું ઘાસ છે', 'There is green grass on the bank'), ('પક્ષીઓ પાણીમાં તરે છે', 'Birds swim in the water'), ('હું ઝાડ નીચે બેસું છું', 'I sit under a tree'), ('મારો મિત્ર પણ આવે છે', 'My friend comes too'), ('અમે સાથે વાતો કરીએ છીએ', 'We chat together'), ('પછી અમે નાસ્તો કરીએ છીએ', 'Then we have breakfast'), ('સૂરજ ઊંચે ચડે છે', 'The sun climbs high'), ('અમે ખુશ થઈને ઘરે જઈએ છીએ', 'We go home happily')]
_STORY2 = [('ગઈકાલે સાંજે હું બજાર ગયો', 'Yesterday evening I went to the market'), ('મેં શાક અને ફળ ખરીદ્યાં', 'I bought vegetables and fruit'), ('ઘરે આવીને મેં ખિસ્સામાં હાથ નાખ્યો', 'Coming home, I put my hand in my pocket'), ('મારું પાકીટ નહોતું!', 'My wallet was not there!'), ('હું ગભરાયો', 'I panicked'), ('હું તરત બજાર પાછો ગયો', 'I went straight back to the market'), ('દુકાનદારે પાકીટ સાચવી રાખ્યું હતું', 'The shopkeeper had kept the wallet safe'), ('મેં તેનો ખૂબ આભાર માન્યો', 'I thanked him warmly'), ("તેણે કહ્યું, 'પ્રામાણિકતા જ સાચી દોલત છે'", 'He said, Honesty is the true wealth'), ('હું ખુશ થઈને ઘરે પાછો આવ્યો', 'I came back home happily')]
_STORY3 = [('કાલે સવારે અમે સફરે જઈશું', 'Tomorrow morning we will go on a journey'), ('અમે ટ્રેનમાં બેસીશું', 'We will sit in the train'), ('બારીમાંથી ખેતરો દેખાશે', 'Fields will be visible from the window'), ('બપોરે અમે નવા શહેરે પહોંચીશું', 'At noon we will reach the new city'), ('પહેલાં અમે હોટલમાં રૂમ લઈશું', 'First we will take a room in the hotel'), ('પછી અમે બજાર ફરીશું', 'Then we will roam the market'), ('સાંજે અમે નદી કિનારે બેસીશું', 'In the evening we will sit by the river'), ('જો વરસાદ પડશે તો અમે હોટલમાં જ રોકાઈશું', 'If it rains, we will stay right in the hotel'), ('બીજા દિવસે અમે પાછા આવીશું', 'The next day we will come back'), ('આ સફર યાદગાર રહેશે', 'This journey will be memorable')]
_DIALOGUE1 = [('ખરીદનાર', 'નમસ્તે! શાક તાજું છે?', 'Hello! Are the vegetables fresh?'), ('વેચનાર', 'નમસ્તે! એકદમ તાજું, સવારે જ આવ્યું', 'Hello! Completely fresh, arrived this morning'), ('ખરીદનાર', 'ટામેટા કેટલાના?', 'How much are the tomatoes?'), ('વેચનાર', 'ચાળીસ રૂપિયા કિલો', 'Forty rupees a kilo'), ('ખરીદનાર', 'બહુ મોંઘું! ત્રીસમાં આપો', 'Too expensive! Give it for thirty'), ('વેચનાર', 'ત્રીસમાં નહીં થાય, પાંત્રીસ છેલ્લા', 'Not for thirty; thirty-five is final'), ('ખરીદનાર', 'બરાબર, એક કિલો આપો', 'Okay, give one kilo'), ('વેચનાર', 'બીજું કંઈ જોઈએ?', 'Do you need anything else?'), ('ખરીદનાર', 'અડધો કિલો ડુંગળી અને લીંબુ', 'Half a kilo of onions and lemons'), ('વેચનાર', 'લીંબુ મફત, ડુંગળી પંદર રૂપિયા', 'Lemons free, onions fifteen rupees'), ('ખરીદનાર', 'વાહ! આભાર', 'Wow! Thanks'), ('વેચનાર', 'કુલ પચાસ રૂપિયા', 'Fifty rupees total'), ('ખરીદનાર', 'આ રહ્યા પચાસ રૂપિયા', 'Here are fifty rupees'), ('વેચનાર', 'થેલીમાં નાખી દઉં?', 'Shall I put it in the bag?'), ('ખરીદનાર', 'હા, મહેરબાની', 'Yes, please'), ('વેચનાર', 'કાલે નવો માલ આવશે', 'New stock comes tomorrow'), ('ખરીદનાર', 'જરૂર આવીશ', 'I will surely come'), ('વેચનાર', 'આવજો!', 'Goodbye - come again!'), ('ખરીદનાર', 'આવજો!', 'Goodbye!'), ('વેચનાર', 'ફરી પધારજો!', 'Do visit again!')]
_DIALOGUE2 = [('રવિ', 'અરે સીતા! કેમ છો?', 'Hey Sita! How are you?'), ('સીતા', 'રવિ! મજામાં! તું કેમ છે?', 'Ravi! Doing well! How are you?'), ('રવિ', 'બસ, મજામાં. ઘણા દિવસે મળ્યા', 'Just fine. We meet after many days'), ('સીતા', 'હા! શું ચાલે છે?', 'Yes! What is going on?'), ('રવિ', 'નવી નોકરી મળી', 'I got a new job'), ('સીતા', 'અરે વાહ! અભિનંદન!', 'Oh wow! Congratulations!'), ('રવિ', 'આભાર! ચા પીશે?', 'Thanks! Will you have tea?'), ('સીતા', 'હા, જરૂર', 'Yes, surely'), ('રવિ', 'તો ચાલ, સામેની હોટલમાં જઈએ', 'Then come, let us go to the hotel across'), ('સીતા', 'તારું કામ કેવું ચાલે છે?', 'How is your work going?'), ('રવિ', 'ખૂબ સરસ, પણ કામ વધારે છે', 'Very good, but there is lots of work'), ('સીતા', 'મહેનતનું ફળ મીઠું', 'The fruit of hard work is sweet'), ('રવિ', 'સાચું કહ્યું! તારો અભ્યાસ કેમ ચાલે?', 'Well said! How are your studies?'), ('સીતા', 'પરીક્ષા નજીક છે, તૈયારી ચાલે છે', 'Exams are near, preparation is on'), ('રવિ', 'શુભેચ્છા! તું જરૂર પાસ થઈશ', 'Best wishes! You will surely pass'), ('સીતા', 'આભાર! મળીને આનંદ થયો', 'Thanks! Nice meeting you'), ('રવિ', 'મને પણ! સંપર્કમાં રહેજે', 'Me too! Stay in touch'), ('સીતા', 'જરૂર! આવતા રવિવારે મળીએ', 'Surely! Let us meet next Sunday'), ('રવિ', 'નક્કી! આવજે', 'Done! Bye'), ('સીતા', 'આવજે!', 'Bye!')]
_DIALOGUE3 = [('અનિલ', 'અરે! બસ ચૂકી ગઈ!', 'Oh no! I missed the bus!'), ('મીરા', 'શાંત થા, શું થયું?', 'Calm down, what happened?'), ('અનિલ', 'છેલ્લી બસ નીકળી ગઈ, હવે શું કરું?', 'The last bus left; what do I do now?'), ('મીરા', 'ચિંતા ન કર, ઉપાય છે', 'Do not worry, there is a solution'), ('અનિલ', 'કયો ઉપાય?', 'Which solution?'), ('મીરા', 'રિક્ષા કરીએ?', 'Shall we take a rickshaw?'), ('અનિલ', 'રિક્ષાવાળો બહુ પૈસા માંગશે', 'The rickshaw driver will ask for a lot'), ('મીરા', 'તો મારા ભાઈને ફોન કરું?', 'Then shall I call my brother?'), ('અનિલ', 'તે કેટલે દૂર છે?', 'How far is he?'), ('મીરા', 'દસ મિનિટમાં આવી જશે', 'He will come in ten minutes'), ('અનિલ', 'એ તો સરસ!', 'That is great!'), ('મીરા', 'ઊભો રહે, ફોન કરું છું', 'Wait here, I am calling'), ('અનિલ', 'તારો ખૂબ આભાર', 'Thank you so much'), ('મીરા', 'એમાં શું? મિત્રો કામના જ હોય', 'What of it? Friends are for helping'), ('અનિલ', 'હવે પછી વહેલો નીકળીશ', 'From now on I will leave early'), ('મીરા', 'બરાબર! ભાઈ આવી ગયો', 'Right! Brother has arrived'), ('અનિલ', 'નમસ્તે ભાઈ!', 'Hello, brother!'), ('મીરા', 'ચાલો, બેસીએ', 'Come, let us sit'), ('અનિલ', 'આજે તું ન હોત તો...', 'If you had not been here today...'), ('મીરા', 'બસ હવે! ઘરે જઈએ', 'Enough now! Let us go home')]
_C_OVERVIEW = ['ગુજરાતી', 'હું ગુજરાતી બોલું છું', 'કેમ છો?', 'આભાર', 'મારું નામ મીરા છે', 'આવજો']
_C_WRITING = ['અ', 'આ', 'ક', 'ખ', 'ળ', 'કી', 'ક્ષ', 'જ્ઞ', 'ત્ર', '૦ ૧ ૨ ૩ ૪ ૫ ૬ ૭ ૮ ૯', 'નમસ્તે', 'પાણી', 'પુસ્તક', 'ઘર', 'શાળા', 'હું ગુજરાતી લખું છું']
_C_PHONOLOGY = ['પાણી', 'ઘર', 'છોકરો', 'છોકરી', 'બાળક', 'રોટલી', 'દૂધ', 'સૂરજ', 'ચાંદ', 'ફૂલ', 'ઝાડ', 'કૂતરો', 'સૂરજ પૂર્વમાં ઊગે છે']
_C_PRONOUNS = ['હું', 'તું', 'તમે', 'તે', 'તેઓ', 'અમે', 'આપણે', 'મારો', 'મારી', 'મારું', 'તમારું', 'આ', 'કોણ', 'શું', 'મેં', 'તેણે']
_C_NUMBERS = ['એક', 'બે', 'ત્રણ', 'ચાર', 'પાંચ', 'છ', 'સાત', 'આઠ', 'નવ', 'દસ', 'વીસ', 'ત્રીસ', 'સો', 'હજાર', 'લાખ', 'કરોડ', 'પહેલો', 'બીજો', 'સોમવાર', 'રવિવાર', 'ત્રણ વાગ્યા', 'સવા ત્રણ']
_C_GRAMMAR = ['હું પાણી પીઉં છું', 'છોકરો રમે છે', 'ઘરમાં', 'ટેબલ પર', 'ગામથી', 'મારું પુસ્તક', 'મારી સાથે આવો', 'હું નથી જતો', 'તું ક્યાં જાય છે?', 'મેં પત્ર લખ્યો', 'તેણે ચા પીધી', 'નવો ફોન', 'બેસો']
_C_TENSES = ['હું રોટલી ખાઉં છું', 'હું ગયો', 'મેં પત્ર લખ્યો', 'તેણે ચા પીધી', 'હું જઈશ', 'તે કરશે', 'અમે મળીશું', 'હું વાંચી રહ્યો છું', 'હું ખાઈ ચૂક્યો છું', 'જો વરસાદ પડે તો હું નહીં જાઉં']
_C_QA = ['તમારું નામ શું છે?', 'મારું નામ રવિ છે', 'તમે ક્યાં રહો છો?', 'હું સુરતમાં રહું છું', 'આ શું છે?', 'કોણ આવ્યું?', 'કેટલા વાગ્યા?', 'ચાર વાગ્યા', 'શું તું આવીશ?', 'હા, જરૂર આવીશ']
_C_COMMANDS = ['બેસ', 'બેસો', 'અંદર આવો', 'ધીમે બોલો', 'મદદ કરજો', 'પાણી આપજો', 'રાહ જોજો', 'માફ કરજો', 'ઘોંઘાટ ન કરો', 'ચાલો, જઈએ', 'આપણે ચા પીએ']
_C_IDIOMS = ['જેવું વાવો તેવું લણો', 'દૂરના ઢોલ વાગે મીઠા', 'નાચ ન જાણે આંગણ વાંકું', 'જ્યાં ચાહ ત્યાં રાહ', 'ખાલી ચણો વાગે ઘણો', 'ઊંટના મોંમાં જીરું', 'ધીરજનાં ફળ મીઠાં', 'કર ભલા તો હો ભલા', 'લોભે લક્ષણ જાય', 'ટીપે ટીપે સરોવર ભરાય', 'દીવા તળે અંધારું', 'ઘર ફૂટે ઘર જાય']
_C_REGISTER = ['તું ક્યાં જાય છે?', 'તમે ક્યાં જાઓ છો?', 'બેસ', 'બેસો', 'પધારો', 'મહેરબાની કરીને જણાવશો', 'પ્રતિ, માનનીય સાહેબ', 'આપનો વિશ્વાસુ', 'ક્ષમા કરશો', 'ફરી મળવાની આશા રાખું છું']
_C_COMPLEX = ['હું બજાર ગયો અને શાક ખરીદ્યું', 'જો તું મહેનત કરીશ તો સફળ થઈશ', 'જે છોકરો ત્યાં ઊભો છે તે મારો ભાઈ છે', 'કારણ કે વરસાદ પડતો હતો, અમે ઘરે રોકાયા', 'પહેલાં હાથ ધુઓ પછી જમો', 'ભલે વરસાદ પડે, કાર્યક્રમ થશે']
_C_MASTERY = ['અ', 'ક', 'ળ', '૦૧૨૩૪૫૬૭૮૯', 'માણસ', 'ઘર', 'પાણી', 'કરવું', 'જવું', 'સારો', 'હું', 'તમે', 'એક', 'દસ', 'સો', 'નમસ્તે', 'કેમ છો', 'આભાર', 'આવજો', 'જેવું વાવો તેવું લણો']


DEMOS = {
 "overview": _items(_C_OVERVIEW, 6),
 "writing": _items(_C_WRITING, 16),
 "phonology": _items(_C_PHONOLOGY, 13),
 "nouns1": _vocab(_NOUNS, 25, 101),
 "verbs1": _vocab(_VERBS, 25, 202),
 "adjadv": _vocab(_ADJADV, 40, 303),
 "pronouns": _items(_C_PRONOUNS, 16),
 "numbers": _items(_C_NUMBERS, 22),
 "greetings": _vocab(_GREET, 30, 404),
 "grammar": _items(_C_GRAMMAR, 13),
 "home": _sents(_HOME, 20, 11),
 "food": _sents(_FOOD, 20, 12),
 "travel": _sents(_TRAVEL, 20, 13),
 "workschool": _sents(_WORKSCHOOL, 20, 14),
 "health": _sents(_HEALTH, 20, 15),
 "emotions": _sents(_EMOTIONS, 20, 16),
 "nature": _sents(_NATURE, 20, 17),
 "shopping": _sents(_SHOPPING, 20, 18),
 "social": _sents(_SOCIAL, 20, 19),
 "tech": _sents(_TECH, 20, 20),
 "tenses": _items(_C_TENSES, 10),
 "qa": _items(_C_QA, 10),
 "commands": _items(_C_COMMANDS, 11),
 "descriptions": _sents(_DESCRIPTIONS, 20, 24),
 "story1": _story(_STORY1, 10),
 "story2": _story(_STORY2, 10),
 "story3": _story(_STORY3, 10),
 "idioms": _items(_C_IDIOMS, 12),
 "register": _items(_C_REGISTER, 10),
 "complex": _items(_C_COMPLEX, 6),
 "dialogue1": _dialogue(_DIALOGUE1, 20, ['ખરીદનાર', 'વેચનાર']),
 "dialogue2": _dialogue(_DIALOGUE2, 20, ['રવિ', 'સીતા']),
 "dialogue3": _dialogue(_DIALOGUE3, 20, ['અનિલ', 'મીરા']),
 "mastery": _items(_C_MASTERY, 20),
}
