#!/usr/bin/env python3
"""Entries for the Malayalam to English databases (Manon's language project, 2026-10-17).

Verified 2026-10-17: RAW SWEEP over the full manifest (2,750 databases) PLUS
every shard index title in jah-databases-data-1: zero 'language-malayalam*'
slugs; ID prefixes JAH-LMAL- (public) and JAH-LMALS- (signature) verified
free in the manifest id_prefix values AND in every shard index (zero zgrep
hits for 'JAH-LMAL' across all index.jsonl.gz files). Pre-authoring
whole-system dedupe-gate check over all 68 planned titles (34 records + 34
Signature Edition titles): zero collisions, zero refusals.

This build creates two NEW databases, 34 ladder-ordered records each:

  language-malayalam              - The Malayalam to English Database
                                (public-harvest: real, fact-checked
                                Malayalam - overview, the Malayalam script,
                                pronunciation, core vocabulary with
                                sentences, grammar essentials, themed
                                sentence sets, verb tenses, questions and
                                answers, commands, descriptions, stories,
                                idioms and proverbs, registers, complex
                                sentences, conversations, mastery
                                reference; standard references Asher &
                                Kumari 1997, Andronov 1996, Mohanan &
                                Mohanan 1984, ISO 639 ml/mal)
  language-malayalam-signature    - The Malayalam to English Signature
                                Database
                                (his original Signature Language Method:
                                every letter a sworn mark, every curve of
                                the script a sealed vow, every sentence a
                                covenant of meaning; src signature, titles
                                suffixed " (Signature Edition)", clearly
                                labeled Signature-made, never presented as
                                authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-34,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

Every record carries Malayalam content with English translation + example
sentences. Sentences are required in EVERY record - no vocabulary-list-only
records.

Practice sentences, dialogues, and stories are constructed by the archive
for teaching and are labeled as such; vocabulary, grammar, proverb glosses,
and language facts follow the cited references. Romanization is the
archive's consistent scholarly-lite scheme (documented in the writing
record): a aa i ii u uu R e ee ai o oo au, k kh g gh ng, ch chh j jh ny,
tT tTh dD dDh nN, t th d dh n, p ph b bh m, y r l v, sh sSh s h, lL zh rR;
the half-u of word-final -u is written u with a breve mark u-with-note.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_language_malayalam.py). Every demo prints its real
computed values, asserts tight bounds (never float exact-equality), and
ends with the OK marker; the build machine-executes all 68 demos before
writing.

Build-time cross-check: every entry declares 'must_contain' strings and the
build asserts each one appears verbatim in the record description, so entry
text and demo outputs can never drift apart.

No website references. Screened per canon.
"""

SIG_TAIL = ("Signature original - his original Signature Language Method: "
            "every letter a sworn mark, every curve of the script a sealed "
            "vow, every sentence a covenant of meaning. Clearly labeled "
            "Signature-made, never presented as authentic public record.")

CIT_ASHER = ("Asher RE, Kumari TC. Malayalam. Descriptive Grammars. "
             "London: Routledge; 1997.")
CIT_ANDRONOV = ("Andronov M. A Grammar of the Malayalam Language in "
                "Historical Treatment. Wiesbaden: Harrassowitz; 1996.")
CIT_MOHANAN = ("Mohanan KP, Mohanan T. Lexical Phonology of the Consonant "
               "System in Malayalam. Linguistic Inquiry. 1984;15(4):575-602.")
CIT_ISO = ("ISO 639: Malayalam is coded ml (ISO 639-1) and mal "
           "(ISO 639-3).")
CIT_CLASSICAL = ("The Government of India declared Malayalam a Classical "
                 "Language in 2013; it is one of the 22 scheduled languages "
                 "of India.")
CIT_CENSUS = ("Census of India 2011: Kerala's literacy rate stands at about "
              "94 percent, among the highest of any Indian state.")

# The Malayalam vowel letters (traditional sixteen), each with the
# archive's romanization.
VOWELS = [
    ("അ", "a", "a as in about"), ("ആ", "aa", "aa as in father"),
    ("ഇ", "i", "i as in pin"), ("ഈ", "ii", "ii as in machine"),
    ("ഉ", "u", "u as in put"), ("ഊ", "uu", "uu as in moon"),
    ("ഋ", "R", "ru as in rural, syllabic r"), ("ൠ", "RR", "long syllabic r"),
    ("ഌ", "lR", "syllabic l, rare"), ("ൡ", "lRR", "long syllabic l, rare"),
    ("എ", "e", "e as in pen"), ("ഏ", "ee", "ay as in pay"),
    ("ഐ", "ai", "ai as in aisle"), ("ഒ", "o", "o as in fork"),
    ("ഓ", "oo", "o as in go"), ("ഔ", "au", "ow as in cow"),
]
# The 36 consonants: 5 vargas of 5 + 4 semivowels + 4 sibilant/h + 3 specials.
CONSONANTS = [
    ("ക", "k"), ("ഖ", "kh"), ("ഗ", "g"), ("ഘ", "gh"), ("ങ", "ng"),
    ("ച", "ch"), ("ഛ", "chh"), ("ജ", "j"), ("ഝ", "jh"), ("ഞ", "ny"),
    ("ട", "tT"), ("ഠ", "tTh"), ("ഡ", "dD"), ("ഢ", "dDh"), ("ണ", "nN"),
    ("ത", "t"), ("ഥ", "th"), ("ദ", "d"), ("ധ", "dh"), ("ന", "n"),
    ("പ", "p"), ("ഫ", "ph"), ("ബ", "b"), ("ഭ", "bh"), ("മ", "m"),
    ("യ", "y"), ("ര", "r"), ("ല", "l"), ("വ", "v"),
    ("ശ", "sh"), ("ഷ", "sSh"), ("സ", "s"), ("ഹ", "h"),
    ("ള", "lL"), ("ഴ", "zh"), ("റ", "rR"),
]
# The five chillu letters - pure consonants with no vowel at all.
CHILLU = [("ൻ", "n"), ("ൺ", "nN"), ("ർ", "r"), ("ൽ", "l"), ("ൾ", "lL")]
# Malayalam digits 0-9.
DIGITS = ["൦", "൧", "൨", "൩", "൪", "൫", "൬", "൭", "൮", "൯"]


def _alpha_lines():
    out = ["Vowels (16):"]
    out += ["  %s  - %s (%s)" % (ch, rom, note) for ch, rom, note in VOWELS]
    out.append("Consonants (36):")
    out += ["  %s  - %s" % (ch, rom) for ch, rom in CONSONANTS]
    out.append("Chillu - vowelless consonants (5):")
    out += ["  %s  - %s (pure consonant, no vowel)" % (ch, rom) for ch, rom in CHILLU]
    out.append("Digits:")
    out.append("  " + " ".join("%s=%d" % (d, i) for i, d in enumerate(DIGITS)))
    return "\n".join(out)


ENTRIES = [
    {
        "key": "overview",
        "name": "Malayalam Language Overview",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Malayalam (മലയാളം, malayaalLam) is the Dravidian language of "
            "Kerala on India's southwest coast. It carries ISO codes ml "
            "(ISO 639-1) and mal (ISO 639-3), belongs to the South Dravidian "
            "branch of the Dravidian family, and is spoken natively by about "
            "38 million people, with total speakers above 45 million when "
            "second-language users are counted. \n\n"
            "Where it is spoken. The heartland is Kerala - "
            "Thiruvananthapuram, Kochi, Kozhikode, Thrissur, Kannur - with "
            "Malayalam also official in Lakshadweep and in the Mahe district "
            "of Puducherry. Large Malayalam-speaking communities live across "
            "the Gulf states, and in Karnataka, Tamil Nadu, and Maharashtra. "
            "Malayalam is the language of Kerala's schools, courts, "
            "newspapers, films, and festivals. \n\n"
            "Official status. Malayalam is the official language of Kerala, "
            "one of the 22 scheduled languages of India, and was declared a "
            "Classical Language of India in 2013. \n\n"
            "Dialects. The standard is based on central Kerala speech. "
            "Northern (Malabar), central, and southern (Travancore) dialects "
            "differ in vocabulary and some sounds - a Kozhikode speaker and "
            "a Thiruvananthapuram speaker understand each other with ease. "
            "Colloquial spoken Malayalam differs markedly from the formal "
            "literary register used in writing. \n\n"
            "History in one breath. Malayalam grew out of the western "
            "coastal dialects of Old Tamil; a distinct literary tradition "
            "emerged by the 9th century CE, and Thunchaththu Ezhuthachan of "
            "the 16th century is honored as the father of the Malayalam "
            "language. Its script evolved from the Grantha script. The word "
            "'Malayalam' itself reads the same forward and backward in "
            "Latin letters - a famous palindrome. \n\n"
            "What makes Malayalam learnable. The script is phonetic, the "
            "word order is a steady subject-object-verb, and verbs mark "
            "tense with a small set of endings: -unnu (present), -i (past), "
            "-um (future). Learn the endings, learn the cases, and the "
            "language opens like a door. \n\n"
            "First sentences in Malayalam:\n"
            "  നമസ്കാരം! - namaskaaram! - Hello!\n"
            "  എന്റെ പേര് മനോൻ. - enTe peeru manoon. - My name is Manon.\n"
            "  ഞാൻ മലയാളം പഠിക്കുന്നു. - njaan malayaalLam patThikkunnu. - "
            "I am learning Malayalam.\n"
            "  ഇന്ന് ഞാൻ മലയാളം പഠിക്കാൻ തുടങ്ങി. - innu njaan malayaalLam "
            "patThikkaan tutangi. - Today I started learning Malayalam."
        ),
        "how_it_works": (
            "This record is the map of the whole database. It fixes the "
            "identity of the language - name (മലയാളം, malayaalLam), codes "
            "(ml / mal), family (Dravidian, South Dravidian), speaker scale "
            "(about 38 million native, above 45 million total), territory "
            "(Kerala, Lakshadweep, Mahe, and the Gulf diaspora), official "
            "standing (Kerala; scheduled language; Classical Language "
            "2013), dialect landscape (Malabar, central, Travancore; "
            "colloquial versus literary registers), and the historical arc "
            "(Old Tamil coastal roots, 9th-century literature, Ezhuthachan "
            "16th century, Grantha-derived script). Every later record "
            "hangs facts on this frame: the writing record spells the "
            "letters, the phonology record sounds them, the vocabulary "
            "records fill the word-hoard, and the grammar records assemble "
            "the engine. Work through the ladder in order and each record "
            "assumes only what earlier records taught."
        ),
        "key_points": [
            "Native name: മലയാളം (malayaalLam); ISO 639-1 ml, ISO 639-3 mal.",
            "Family: Dravidian, South Dravidian branch.",
            "About 38 million native speakers; above 45 million total with second-language users.",
            "Official in Kerala, Lakshadweep, and Mahe; scheduled language of India; Classical Language since 2013.",
            "Dialects: northern (Malabar), central (standard), southern (Travancore); strong colloquial/literary split.",
            "Literary tradition from the 9th century CE; Thunchaththu Ezhuthachan, 16th century, father of the language.",
            "SOV word order; tense carried by verb endings (-unnu present, -i past, -um future).",
        ],
        "requirements": [
            "No prior knowledge of any Indian language is assumed.",
            "Read the writing-system record before the phonology record; read both before the vocabulary records.",
        ],
        "standards": [
            "Speaker figures are rounded public estimates (Census/Ethnologue-style reporting); stated as approximate.",
            "Dialect and history claims follow the standard references: Asher & Kumari 1997, Andronov 1996.",
            "Practice sentences are constructed by the archive for teaching; language facts follow the cited references.",
        ],
        "citations": [CIT_ASHER, CIT_ANDRONOV, CIT_ISO, CIT_CLASSICAL],
        "must_contain": ["malayaalLam", "ml", "mal", "Dravidian", "Kerala", "38 million"],
        "sig_lens": (
            "Through the Signature lens this overview is a census of a "
            "living nation of speakers: every headcount a sworn roll-call, "
            "every dialect a branch of one family tree, every classical "
            "seal a vow that this language will be carried whole into the "
            "archive."
        ),
        "drill": {
            "native_m": 38.0, "total_m": 45.0, "official_regions": 3,
            "iso1": "ml", "iso3": "mal", "scheduled": 22,
            "dialects": ["Malabar", "Central", "Travancore"],
            "regions": ["Kerala", "Lakshadweep", "Mahe", "Gulf states",
                        "Karnataka", "Tamil Nadu", "Maharashtra"],
            "classical_year": 2013,
        },
    },
    {
        "key": "writing",
        "name": "The Malayalam Writing System",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Malayalam is written in the Malayalam script, evolved from the "
            "Grantha script. It runs left-to-right, is fully phonetic (one "
            "letter, one sound), and uses the Malayalam digits ൦-൯ alongside "
            "Arabic numerals, with punctuation borrowed from English. \n\n"
            + _alpha_lines() + "\n\n"
            "How the script works. Every consonant carries an inherent 'a' "
            "vowel: ക is ka, not k. The chandrakkala (്) kills the vowel: "
            "ക് is pure k. Vowel signs reshape the consonant: ക + ി = കി "
            "(ki), ക + ൂ = കൂ (kuu). Consonant clusters stack or fuse: ക്ത "
            "(kta), സ്ത്രീ (strii, woman). The five chillu letters (ൻ ൺ ർ "
            "ൽ ൾ) are pure vowelless consonants - അവൻ (avan, he) ends in "
            "the chillu ൻ. \n\n"
            "The archive romanization used across this database: vowels a "
            "aa i ii u uu R e ee ai o oo au; consonants k kh g gh ng, ch "
            "chh j jh ny, tT tTh dD dDh nN, t th d dh n, p ph b bh m, y r l "
            "v, sh sSh s h, lL zh rR; the word-final half-u is written with "
            "a breve note. \n\n"
            "Read and write these first words:\n"
            "  വീട് - viiTu - house\n"
            "  വെള്ളം - velLlam - water\n"
            "  അമ്മ - amma - mother\n"
            "  പുസ്തകം - pustakam - book\n"
            "  മലയാളം - malayaalLam - Malayalam\n"
            "  നമസ്കാരം - namaskaaram - greeting"
        ),
        "how_it_works": (
            "The script works by syllable blocks: learn the 16 vowels, the "
            "36 consonants, the 5 chillu letters, and the two killer marks "
            "(chandrakkala ് and the vowel signs), and you can read any "
            "Malayalam word aloud. Because the script is phonetic, spelling "
            "drills double as pronunciation drills. The chillu letters are "
            "the signature of written Malayalam: a word ending in ൻ ൺ ർ ൽ "
            "or ൾ ends on a bare consonant with no vowel at all. Conjunct "
            "clusters (kta, strii) are the only hard part - practice them "
            "as fused blocks, not as letter sequences. Arabic numerals "
            "dominate daily life; the Malayalam digits ൦-൯ appear on "
            "calendars, invitations, and formal documents."
        ),
        "key_points": [
            "Malayalam script, evolved from Grantha; written left-to-right, fully phonetic.",
            "16 vowels + 36 consonants + 5 chillu letters = the working alphabet.",
            "Every consonant carries inherent 'a'; chandrakkala (്) kills the vowel.",
            "Chillu letters (ൻ ൺ ർ ൽ ൾ) are pure vowelless consonants.",
            "Conjunct clusters stack or fuse (ക്ത, സ്ത്രീ).",
            "Malayalam digits ൦-൯; Arabic numerals and English punctuation in daily use.",
        ],
        "requirements": [
            "Read the overview record first for the language's identity and codes.",
            "Practice writing the vowel signs on ക before moving to the phonology record.",
        ],
        "standards": [
            "Letter inventory follows the traditional grammar count (16 vowels, 36 consonants, 5 chillu); sources differ on marginal signs.",
            "Romanization is the archive's consistent scheme, defined in this record and used database-wide.",
            "Practice words are standard dictionary forms (Asher & Kumari 1997).",
        ],
        "citations": [CIT_ASHER, CIT_ANDRONOV, CIT_ISO],
        "must_contain": ["Grantha", "chandrakkala", "chillu", "൦", "left-to-right"],
        "sig_lens": (
            "Through the Signature lens each letter is a sworn mark: the "
            "curves of the script are seals pressed into the page, the "
            "chillu a vow cut clean with no vowel to soften it, and every "
            "syllable block a covenant that sound and sign will never part."
        ),
        "drill": {
            "vowels": 16, "consonants": 36, "chillu": 5,
            "letters": [c for c, r, n in VOWELS] + [c for c, r in CONSONANTS],
            "chillu_letters": [c for c, r in CHILLU],
            "digits": DIGITS, "direction": "left-to-right",
            "killer": "്",
            "test_words": ["വീട്", "വെള്ളം", "അമ്മ", "മലയാളം"],
        },
    },
    {
        "key": "phonology",
        "name": "Malayalam Pronunciation and Phonology",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Malayalam has about 16 vowel sounds and over 35 consonant "
            "sounds. Vowel length changes meaning: കല (kala, art) versus "
            "കാല് (kaalu, leg). Stress falls gently on the first syllable; "
            "there are no tones - pitch does not change word meaning as it "
            "does in Hausa or Mandarin. \n\n"
            "The five consonant rows, each in the same five-step pattern "
            "(voiceless, aspirated, voiced, voiced-aspirated, nasal):\n"
            "  ക ഖ ഗ ഘ ങ (k kh g gh ng) - throat\n"
            "  ച ഛ ജ ഝ ഞ (ch chh j jh ny) - palate\n"
            "  ട ഠ ഡ ഢ ണ (tT tTh dD dDh nN) - tongue curled back (retroflex)\n"
            "  ത ഥ ദ ധ ന (t th d dh n) - tongue on teeth (dental)\n"
            "  പ ഫ ബ ഭ മ (p ph b bh m) - lips\n"
            "Dental versus retroflex is the great divide: ത (tongue on "
            "teeth) against ട (tongue curled back) are different sounds and "
            "different letters. These five rows are called vargas. \n\n"
            "Signature sounds. ഴ (zh) is the famous Malayalam-Tamil sound - "
            "a tongue-tip trill found almost nowhere else. റ (rR) is a "
            "strong trill, ര (r) a light tap. ള (lL) is a retroflex l. "
            "The word-final half-u (samvruthokaram) in വീട് is a whisper of "
            "a vowel, not a full 'oo'. \n\n"
            "Ten spoken-example words - say each aloud:\n"
            "  മലയാളം (malayaalLam) - Malayalam\n"
            "  വെള്ളം (velLlam) - water\n"
            "  ചോറ് (chooRu) - cooked rice\n"
            "  പുഴ (puzha) - river\n"
            "  മഴ (mazha) - rain\n"
            "  കടൽ (katal) - sea\n"
            "  സൂര്യൻ (suuryan) - sun\n"
            "  പൂവ് (puuvu) - flower\n"
            "  കണ്ണ് (kanNu) - eye\n"
            "  കാത് (kaatu) - ear"
        ),
        "how_it_works": (
            "The sound system works in rows: master the five vargas (throat, "
            "palate, curled-tongue, teeth, lips), each running voiceless to "
            "nasal in the same five steps, and the consonants organize "
            "themselves. Vowel length is phonemic - hold ആ twice as long as "
            "അ. The signature drills are minimal pairs: തല (tala, head) "
            "versus ടല? No - real pairs: പല (pala, many) with dental-adjacent "
            "sounds against retroflex sets like കട (kata, shop) with its "
            "curled-tongue ട. Stress stays light and early; intonation "
            "rises at the end of questions. The half-u at word ends "
            "(samvruthokaram) is whispered, never a full vowel - saying "
            "viiToo for വീട് marks the beginner instantly."
        ),
        "key_points": [
            "About 16 vowels; vowel length changes meaning (kala art, kaalu leg).",
            "Five vargas of five: throat, palate, retroflex, dental, lips - voiceless to nasal.",
            "Dental (ത) vs retroflex (ട) is the core contrast; tongue placement differs.",
            "Signature sounds: ഴ (zh), റ (rR trill), ള (lL retroflex l).",
            "No tones; stress falls lightly on the first syllable.",
            "Word-final half-u (samvruthokaram) is whispered, not a full vowel.",
        ],
        "requirements": [
            "Read the writing-system record first; the letters carry the sounds.",
            "Say the ten example words aloud before the vocabulary records.",
        ],
        "standards": [
            "Sound inventory follows Asher & Kumari 1997 and Mohanan & Mohanan 1984.",
            "English approximations are guides only; the Malayalam letters are authoritative.",
            "Practice words are standard dictionary forms.",
        ],
        "citations": [CIT_ASHER, CIT_MOHANAN, CIT_ANDRONOV],
        "must_contain": ["varga", "retroflex", "samvruthokaram", "zh", "no tones"],
        "sig_lens": (
            "Through the Signature lens every sound is a sealed vow: the "
            "five vargas are five sworn rows, the retroflex curl a mark of "
            "distinction, and the rare ഴ a covenant-sound found almost "
            "nowhere else on earth."
        ),
        "drill": {
            "vowel_count": 16, "vargas": 5, "steps": 5,
            "signature_sounds": ["ഴ", "റ", "ള"],
            "tones": False,
            "minimal_pairs": [("കല", "kala", "art"), ("കാല്", "kaalu", "leg")],
            "example_words": ["മലയാളം", "വെള്ളം", "ചോറ്", "പുഴ", "മഴ",
                              "കടൽ", "സൂര്യൻ", "പൂവ്", "കണ്ണ്", "കാത്"],
            "stress": "first syllable",
        },
    },
    {
        "key": "nouns",
        "name": "Malayalam Core Nouns I",
        "group": "Core Vocabulary",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "Twenty-five essential nouns - person, place, thing - each with "
            "romanization, English, and one translated example sentence. "
            "Malayalam nouns take case endings directly (no prepositions): "
            "വീട് (house) becomes വീട്ടിൽ (in the house). \n\n"
            "  1. വീട് (viiTu) - house. എന്റെ വീട് വലുതാണ്. (enTe viiTu "
            "valutaanu.) - My house is big.\n"
            "  2. വെള്ളം (velLlam) - water. എനിക്ക് വെള്ളം വേണം. (enikku "
            "velLlam veeNam.) - I want water.\n"
            "  3. ചോറ് (chooRu) - cooked rice. ചോറ് ചൂടാണ്. (chooRu "
            "chuutaanu.) - The rice is hot.\n"
            "  4. അമ്മ (amma) - mother. അമ്മ പാചകം ചെയ്യുന്നു. (amma "
            "paachakam cheyyunnu.) - Mother is cooking.\n"
            "  5. അച്ഛൻ (achchhan) - father. അച്ഛൻ ജോലിക്ക് പോയി. "
            "(achchhan joolikku pooyi.) - Father went to work.\n"
            "  6. സുഹൃത്ത് (suhruttu) - friend. അവൻ എന്റെ സുഹൃത്താണ്. "
            "(avan enTe suhruttaanu.) - He is my friend.\n"
            "  7. പുസ്തകം (pustakam) - book. ഈ പുസ്തകം നല്ലതാണ്. (ii "
            "pustakam nallataanu.) - This book is good.\n"
            "  8. സ്കൂൾ (skuul) - school. കുട്ടികൾ സ്കൂളിൽ പോകുന്നു. "
            "(kuttikal skuulil pookunnu.) - The children go to school.\n"
            "  9. മരം (maram) - tree. മരം ഉയരമുള്ളതാണ്. (maram "
            "uyaramulLattaanu.) - The tree is tall.\n"
            "  10. പൂവ് (puuvu) - flower. പൂവ് മനോഹരമാണ്. (puuvu "
            "manooharamaanu.) - The flower is beautiful.\n"
            "  11. സൂര്യൻ (suuryan) - sun. സൂര്യൻ ഉദിച്ചു. (suuryan "
            "udichchu.) - The sun rose.\n"
            "  12. ചന്ദ്രൻ (chandran) - moon. ചന്ദ്രൻ തിളങ്ങുന്നു. "
            "(chandran tilangunnu.) - The moon is shining.\n"
            "  13. നായ (naaya) - dog. നായ ഓടുന്നു. (naaya ootunnu.) - The "
            "dog is running.\n"
            "  14. പൂച്ച (puuchcha) - cat. പൂച്ച ഉറങ്ങുന്നു. (puuchcha "
            "urangunnu.) - The cat is sleeping.\n"
            "  15. മീൻ (miin) - fish. മീൻ വെള്ളത്തിൽ നീന്തുന്നു. (miin "
            "velLlattil niintunnu.) - The fish swims in the water.\n"
            "  16. പണം (panNam) - money. എന്റെ കൈയിൽ പണമുണ്ട്. (enTe "
            "kaiyil panNamunTu.) - I have money in my hand.\n"
            "  17. കട (kata) - shop. കട അടുത്താണ്. (kata atuttaanu.) - The "
            "shop is near.\n"
            "  18. റോഡ് (rootu) - road. റോഡ് നീളമുള്ളതാണ്. (rootu "
            "niilamulLattaanu.) - The road is long.\n"
            "  19. കാർ (kaar) - car. കാർ വേഗത്തിൽ പോകുന്നു. (kaar "
            "veegattil pookunnu.) - The car goes fast.\n"
            "  20. ഫോൺ (phoonu) - phone. ഫോൺ മേശപ്പുറത്തുണ്ട്. (phoonu "
            "meeshappurattunTu.) - The phone is on the table.\n"
            "  21. ആശുപത്രി (aashupatri) - hospital. ആശുപത്രി ദൂരെയാണ്. "
            "(aashupatri duurayaanu.) - The hospital is far.\n"
            "  22. മഴ (mazha) - rain. മഴ പെയ്യുന്നു. (mazha peyyunnu.) - "
            "It is raining.\n"
            "  23. ഭക്ഷണം (bhakshanam) - food. ഭക്ഷണം രുചികരമാണ്. "
            "(bhakshanam ruchikaramaanu.) - The food is tasty.\n"
            "  24. കുട്ടി (kutti) - child. കുട്ടി കളിക്കുന്നു. (kutti "
            "kalikkunnu.) - The child is playing.\n"
            "  25. ദിവസം (divasam) - day. ഇന്ന് നല്ല ദിവസമാണ്. (innu nalla "
            "divasamaanu.) - Today is a good day. \n\n"
            "Plurals add -കൾ: പുസ്തകം becomes പുസ്തകങ്ങൾ (books)."
        ),
        "how_it_works": (
            "Nouns are the anchors of the SOV sentence: subject first, "
            "object before the verb. Malayalam nouns do not use articles - "
            "പുസ്തകം means 'book' or 'the book' by context. Number is "
            "marked with -കൾ (kal): പുസ്തകങ്ങൾ (books), കുട്ടികൾ "
            "(children). Case endings attach directly to the noun stem, "
            "often with a linking change: വീട് + ഇൽ = വീട്ടിൽ (in the "
            "house). Human nouns distinguish masculine (അച്ഛൻ), feminine "
            "(അമ്മ), and plural (അവർ); non-human nouns take അത്/അവ. Learn "
            "each noun with its sentence and the case endings of the "
            "grammar record will snap on like fittings."
        ),
        "key_points": [
            "25 essential nouns: people, places, things - each with a translated sentence.",
            "No articles: പുസ്തകം is 'book' or 'the book' by context.",
            "Plural with -കൾ: പുസ്തകങ്ങൾ (books), കുട്ടികൾ (children).",
            "Case endings attach to the noun: വീട്ടിൽ (in the house).",
            "Human nouns mark masculine/feminine; non-humans take അത്/അവ.",
        ],
        "requirements": [
            "Read the writing and phonology records first to sound the words.",
            "Say each sentence aloud; the verb endings preview the verb record.",
        ],
        "standards": [
            "Word forms are standard dictionary Malayalam (Asher & Kumari 1997).",
            "Practice sentences are constructed by the archive for teaching.",
            "Romanization follows this database's scheme from the writing record.",
        ],
        "citations": [CIT_ASHER, CIT_ANDRONOV],
        "must_contain": ["viiTu", "suhruttu", "പുസ്തകങ്ങൾ", "-കൾ", "വീട്ടിൽ"],
        "sig_lens": (
            "Through the Signature lens each noun is a sworn name: house, "
            "water, mother, sun - twenty-five marks pressed into the "
            "archive, each carrying its sentence like a seal carries its "
            "wax."
        ),
        "drill": {
            "nouns": ["വീട്", "വെള്ളം", "ചോറ്", "അമ്മ", "അച്ഛൻ",
                      "സുഹൃത്ത്", "പുസ്തകം", "സ്കൂൾ", "മരം", "പൂവ്",
                      "സൂര്യൻ", "ചന്ദ്രൻ", "നായ", "പൂച്ച", "മീൻ",
                      "പണം", "കട", "റോഡ്", "കാർ", "ഫോൺ",
                      "ആശുപത്രി", "മഴ", "ഭക്ഷണം", "കുട്ടി", "ദിവസം"],
            "plural_suffix": "കൾ",
            "locative_example": ("വീട്", "വീട്ടിൽ"),
        },
    },
    {
        "key": "verbs",
        "name": "Malayalam Core Verbs I",
        "group": "Core Vocabulary",
        "ladder_rank": 5,
        "ladder_tier": "foundations",
        "description": (
            "Twenty-five essential verbs - each with romanization, English, "
            "and one translated example sentence. The citation form ends in "
            "-uka: പോകുക (to go). Present tense adds -unnu, past -i, "
            "future -um: ഞാൻ പോകും (I will go). \n\n"
            "  1. പോകുക (pookuka) - to go. ഞാൻ സ്കൂളിൽ പോകുന്നു. (njaan "
            "skuulil pookunnu.) - I go to school.\n"
            "  2. വരിക (varika) - to come. അവൻ വരുന്നു. (avan varunnu.) - "
            "He is coming.\n"
            "  3. കഴിക്കുക (kazhikkuka) - to eat. ഞാൻ ചോറ് കഴിക്കുന്നു. "
            "(njaan chooRu kazhikkunnu.) - I eat rice.\n"
            "  4. കുടിക്കുക (kutikkuka) - to drink. അവൾ വെള്ളം കുടിക്കുന്നു. "
            "(aval velLlam kutikkunnu.) - She drinks water.\n"
            "  5. കാണുക (kaanuka) - to see. ഞാൻ സിനിമ കാണുന്നു. (njaan "
            "sinima kaanunnu.) - I watch a film.\n"
            "  6. ചെയ്യുക (cheyyuka) - to do. ഞാൻ ജോലി ചെയ്യുന്നു. (njaan "
            "jooli cheyyunnu.) - I do work.\n"
            "  7. പറയുക (parayuka) - to say. അവൻ സത്യം പറയുന്നു. (avan "
            "satyam parayunnu.) - He speaks the truth.\n"
            "  8. എഴുതുക (ezhutuka) - to write. ഞാൻ കത്ത് എഴുതുന്നു. "
            "(njaan kattu ezhutunnu.) - I write a letter.\n"
            "  9. വായിക്കുക (vaayikkuka) - to read. അവൾ പുസ്തകം "
            "വായിക്കുന്നു. (aval pustakam vaayikkunnu.) - She reads a book.\n"
            "  10. പഠിക്കുക (patThikkuka) - to learn. ഞാൻ മലയാളം "
            "പഠിക്കുന്നു. (njaan malayaalLam patThikkunnu.) - I learn "
            "Malayalam.\n"
            "  11. പഠിപ്പിക്കുക (patThippikkuka) - to teach. അധ്യാപകൻ "
            "പഠിപ്പിക്കുന്നു. (adhyaapakan patThippikkunnu.) - The teacher "
            "teaches.\n"
            "  12. ഉറങ്ങുക (uranguka) - to sleep. കുട്ടി ഉറങ്ങുന്നു. "
            "(kutti urangunnu.) - The child sleeps.\n"
            "  13. ഉണരുക (unaruka) - to wake up. ഞാൻ നേരത്തെ ഉണരുന്നു. "
            "(njaan neertte unarunnu.) - I wake up early.\n"
            "  14. ഓടുക (ootuka) - to run. നായ വേഗത്തിൽ ഓടുന്നു. (naaya "
            "veegattil ootunnu.) - The dog runs fast.\n"
            "  15. നടക്കുക (natakkuka) - to walk. ഞാൻ പാർക്കിൽ നടക്കുന്നു. "
            "(njaan paarkkil natakkunnu.) - I walk in the park.\n"
            "  16. ഇരിക്കുക (irikkuka) - to sit. അവൻ കസേരയിൽ ഇരിക്കുന്നു. "
            "(avan kaseerayil irikkunnu.) - He sits on the chair.\n"
            "  17. നിൽക്കുക (nilkkuka) - to stand. ഞാൻ വാതിലിനരികിൽ "
            "നിൽക്കുന്നു. (njaan vaatilinarikil nilkkunnu.) - I stand near "
            "the door.\n"
            "  18. കൊടുക്കുക (kotukkuka) - to give. അമ്മ പണം കൊടുക്കുന്നു. "
            "(amma panNam kotukkunnu.) - Mother gives money.\n"
            "  19. എടുക്കുക (etukkuka) - to take. ഞാൻ പുസ്തകം എടുക്കുന്നു. "
            "(njaan pustakam etukkunnu.) - I take the book.\n"
            "  20. വാങ്ങുക (vaanguka) - to buy. ഞാൻ പഴം വാങ്ങുന്നു. (njaan "
            "pazham vaangunnu.) - I buy bananas.\n"
            "  21. വിൽക്കുക (vilkkuka) - to sell. കടക്കാരൻ പച്ചക്കറി "
            "വിൽക്കുന്നു. (katakkaaran pachakkari vilkkunnu.) - The "
            "shopkeeper sells vegetables.\n"
            "  22. സ്നേഹിക്കുക (sneehikkuka) - to love. ഞാൻ എന്റെ അമ്മയെ "
            "സ്നേഹിക്കുന്നു. (njaan enTe ammaye sneehikkunnu.) - I love my "
            "mother.\n"
            "  23. ചിരിക്കുക (chirikkuka) - to laugh. കുട്ടികൾ ചിരിക്കുന്നു. "
            "(kuttikal chirikkunnu.) - The children laugh.\n"
            "  24. കരയുക (karayuka) - to cry. കുഞ്ഞ് കരയുന്നു. (kunyu "
            "karayunnu.) - The baby cries.\n"
            "  25. ജോലി ചെയ്യുക (jooli cheyyuka) - to work. അച്ഛൻ ഓഫീസിൽ "
            "ജോലി ചെയ്യുന്നു. (achchhan oofiisil jooli cheyyunnu.) - Father "
            "works in the office."
        ),
        "how_it_works": (
            "Verbs are the engine at the end of the sentence. Strip -uka "
            "to find the stem (പോക് from പോകുക), then add the tense: "
            "stem + unnu = present (പോകുന്നു, goes), stem + i = past "
            "(പോയി, went), stem + um = future (പോകും, will go). The verb "
            "agrees with the subject's person but Malayalam verbs do not "
            "change for gender - അവൻ പോകുന്നു and അവൾ പോകുന്നു use the "
            "same form. ചെയ്യുക (to do) pairs with nouns to make compound "
            "verbs: ജോലി ചെയ്യുക (to work), പാചകം ചെയ്യുക (to cook). "
            "Causatives grow with -ippikku: പഠിക്കുക (learn) becomes "
            "പഠിപ്പിക്കുക (teach, cause to learn)."
        ),
        "key_points": [
            "25 essential verbs, each with a translated sentence.",
            "Citation form ends in -uka; stem + unnu/i/um = present/past/future.",
            "Verbs do not inflect for gender: അവൻ പോകുന്നു = അവൾ പോകുന്നു.",
            "ചെയ്യുക builds compound verbs: ജോലി ചെയ്യുക, പാചകം ചെയ്യുക.",
            "Causative -ippikku: പഠിക്കുക (learn) -> പഠിപ്പിക്കുക (teach).",
        ],
        "requirements": [
            "Read the noun record first; verbs need subjects and objects.",
            "Conjugate each verb in all three tenses aloud.",
        ],
        "standards": [
            "Verb forms are standard literary Malayalam (Asher & Kumari 1997).",
            "Practice sentences are constructed by the archive for teaching.",
        ],
        "citations": [CIT_ASHER, CIT_ANDRONOV],
        "must_contain": ["പോകുക", "-unnu", "പഠിപ്പിക്കുക", "cheyyuka", "പോകും"],
        "sig_lens": (
            "Through the Signature lens each verb is a sworn action: to go, "
            "to learn, to love - twenty-five vows of doing, each sealed "
            "with its tense-endings like wax on a covenant."
        ),
        "drill": {
            "verbs": ["പോകുക", "വരിക", "കഴിക്കുക", "കുടിക്കുക", "കാണുക",
                      "ചെയ്യുക", "പറയുക", "എഴുതുക", "വായിക്കുക",
                      "പഠിക്കുക", "പഠിപ്പിക്കുക", "ഉറങ്ങുക", "ഉണരുക",
                      "ഓടുക", "നടക്കുക", "ഇരിക്കുക", "നിൽക്കുക",
                      "കൊടുക്കുക", "എടുക്കുക", "വാങ്ങുക", "വിൽക്കുക",
                      "സ്നേഹിക്കുക", "ചിരിക്കുക", "കരയുക", "ജോലി ചെയ്യുക"],
            "present": "unnu", "past": "i", "future": "um",
            "stem_example": ("പോകുക", "പോക്"),
            "conjugated": {"present": "പോകുന്നു", "past": "പോയി", "future": "പോകും"},
        },
    },
    {
        "key": "adjectives",
        "name": "Malayalam Adjectives and Adverbs",
        "group": "Core Vocabulary",
        "ladder_rank": 6,
        "ladder_tier": "foundations",
        "description": (
            "Twenty-five adjectives and fifteen adverbs, each with a "
            "translated sentence. Malayalam adjectives stand before the "
            "noun and do not change for gender or number: നല്ല പുസ്തകം "
            "(good book), നല്ല പുസ്തകങ്ങൾ (good books). \n\n"
            "Adjectives:\n"
            "  നല്ല (nalla) - good. ഇത് നല്ല പുസ്തകമാണ്. - This is a good "
            "book.\n"
            "  ചീത്ത (chiitta) - bad. ചീത്ത ശീലം ഒഴിവാക്കുക. - Avoid bad "
            "habits.\n"
            "  വലിയ (valiya) - big. വലിയ വീട് കാണുക. - See the big house.\n"
            "  ചെറിയ (cherriya) - small. ചെറിയ കുട്ടി കളിക്കുന്നു. - The "
            "small child is playing.\n"
            "  പുതിയ (putiya) - new. എനിക്ക് പുതിയ ഫോണുണ്ട്. - I have a new "
            "phone.\n"
            "  പഴയ (pazhaya) - old. പഴയ കാർ വിൽക്കുന്നു. - (He) sells the "
            "old car.\n"
            "  മനോഹരമായ (manooharamaaya) - beautiful. മനോഹരമായ പൂവ്. - A "
            "beautiful flower.\n"
            "  ഉയർന്ന (uyarnna) - tall/high. ഉയർന്ന മരം. - A tall tree.\n"
            "  കുറിയ (kurriya) - short. കുറിയ മതിൽ. - A short wall.\n"
            "  നീളമുള്ള (niilamulLa) - long. നീളമുള്ള റോഡ്. - A long road.\n"
            "  ചൂടുള്ള (chuutulLa) - hot. ചൂടുള്ള ചായ കുടിക്കുക. - Drink hot "
            "tea.\n"
            "  തണുത്ത (tanutta) - cold. തണുത്ത വെള്ളം. - Cold water.\n"
            "  മധുരമുള്ള (madhuramulLa) - sweet. മധുരമുള്ള മാങ്ങ. - A sweet "
            "mango.\n"
            "  പുളിയുള്ള (puliyulLa) - sour. പുളിയുള്ള നാരങ്ങ. - A sour "
            "lemon.\n"
            "  എരിവുള്ള (erivulLa) - spicy. എരിവുള്ള കറി. - Spicy curry.\n"
            "  സമ്പന്നമായ (sampannamaaya) - rich. സമ്പന്നമായ നാട്. - A rich "
            "country.\n"
            "  ദരിദ്രമായ (daridramaaya) - poor. ദരിദ്രമായ കുടുംബം. - A poor "
            "family.\n"
            "  സന്തോഷമുള്ള (santoshhamulLa) - happy. സന്തോഷമുള്ള കുട്ടി. - A "
            "happy child.\n"
            "  ദുഃഖമുള്ള (dukkhamulLa) - sad. ദുഃഖമുള്ള മുഖം. - A sad face.\n"
            "  ബുദ്ധിമാനായ (buddhimaanaaya) - intelligent. ബുദ്ധിമാനായ "
            "കുട്ടി. - An intelligent child.\n"
            "  ശക്തമായ (shaktamaaya) - strong. ശക്തമായ കാറ്റ്. - Strong "
            "wind.\n"
            "  മൃദുവായ (mruduvaaya) - soft. മൃദുവായ തലയിണ. - A soft pillow.\n"
            "  കഠിനമായ (kathinamaaya) - hard/difficult. കഠിനമായ പരീക്ഷ. - A "
            "difficult exam.\n"
            "  വൃത്തിയുള്ള (vruttiyulLa) - clean. വൃത്തിയുള്ള മുറി. - A "
            "clean room.\n"
            "  വേഗമുള്ള (veegamulLa) - fast. വേഗമുള്ള കാർ. - A fast car.\n\n"
            "Adverbs:\n"
            "  വേഗത്തിൽ (veegattil) - quickly. അവൻ വേഗത്തിൽ ഓടുന്നു. - He "
            "runs quickly.\n"
            "  പതുക്കെ (patukke) - slowly. പതുക്കെ നടക്കുക. - Walk slowly.\n"
            "  നന്നായി (nannaayi) - well. അവൾ നന്നായി പാടുന്നു. - She sings "
            "well.\n"
            "  വളരെ (valare) - very. വളരെ നല്ലത്. - Very good.\n"
            "  ഇന്ന് (innu) - today. ഇന്ന് മഴ പെയ്യുന്നു. - It rains today.\n"
            "  നാളെ (naalLe) - tomorrow. നാളെ വരൂ. - Come tomorrow.\n"
            "  ഇന്നലെ (innale) - yesterday. ഇന്നലെ ഞാൻ പോയി. - I went "
            "yesterday.\n"
            "  എപ്പോഴും (eppoozhum) - always. ഞാൻ എപ്പോഴും സത്യം പറയും. - I "
            "always speak the truth.\n"
            "  ഒരിക്കലും (orikkalum) - never. ഞാൻ ഒരിക്കലും കള്ളം പറയില്ല. - "
            "I never lie.\n"
            "  ഒരുമിച്ച് (orumichchu) - together. നമുക്ക് ഒരുമിച്ച് പോകാം. - "
            "Let's go together.\n"
            "  ശ്രദ്ധയോടെ (shraddhayootte) - carefully. ശ്രദ്ധയോടെ വായിക്കുക. "
            "- Read carefully.\n"
            "  സന്തോഷത്തോടെ (santoshhattootte) - happily. അവർ "
            "സന്തോഷത്തോടെ ചിരിച്ചു. - They laughed happily.\n"
            "  ഉറക്കെ (urakke) - loudly. ഉറക്കെ സംസാരിക്കരുത്. - Don't speak "
            "loudly.\n"
            "  മെല്ലെ (melle) - softly. മെല്ലെ പാടുക. - Sing softly.\n"
            "  പുറത്ത് (purattu) - outside. പുറത്ത് മഴ പെയ്യുന്നു. - It is "
            "raining outside. \n\n"
            "Adjectives build with -ഉള്ള (ചൂടുള്ള, hot) and -മായ "
            "(മനോഹരമായ, beautiful); comparison uses -ഏക്കാൾ: ഇത് "
            "അതിനേക്കാൾ വലുതാണ് (this is bigger than that)."
        ),
        "how_it_works": (
            "Adjectives in Malayalam are beautifully simple: they never "
            "inflect. നല്ല stays നല്ല whether the noun is singular, "
            "plural, masculine, or feminine - നല്ല കുട്ടി, നല്ല കുട്ടികൾ. "
            "Many adjectives are built from nouns with -ഉള്ള (having): "
            "ചൂട് (heat) + ഉള്ള = ചൂടുള്ള (hot, heat-having); സന്തോഷം "
            "(happiness) + ഉള്ള = സന്തോഷമുള്ള (happy). Others use -മായ "
            "(like): മനോഹരം + മായ = മനോഹരമായ. Adverbs of manner often end "
            "in -ആയി (നന്നായി) or -ഓടെ (ശ്രദ്ധയോടെ), and adverbs of time "
            "and place (ഇന്ന്, പുറത്ത്) stand freely in the sentence. "
            "Comparison uses -ഏക്കാൾ: ഇത് അതിനേക്കാൾ വലുതാണ് (this is "
            "bigger than that)."
        ),
        "key_points": [
            "Adjectives never inflect for gender or number: നല്ല കുട്ടി / നല്ല കുട്ടികൾ.",
            "Adjective builders: -ഉള്ള (having) and -മായ (like).",
            "Adverbs of manner: -ആയി (നന്നായി), -ഓടെ (ശ്രദ്ധയോടെ).",
            "Comparison with -ഏക്കാൾ: അതിനേക്കാൾ വലുതാണ് (bigger than that).",
            "25 adjectives + 15 adverbs, each with a translated sentence.",
        ],
        "requirements": [
            "Read the noun and verb records first.",
            "Build five -ഉള്ള adjectives from nouns you know.",
        ],
        "standards": [
            "Forms are standard literary Malayalam (Asher & Kumari 1997).",
            "Practice sentences are constructed by the archive for teaching.",
        ],
        "citations": [CIT_ASHER, CIT_ANDRONOV],
        "must_contain": ["നല്ല", "-ഉള്ള", "-മായ", "വേഗത്തിൽ", "-ഏക്കാൾ"],
        "sig_lens": (
            "Through the Signature lens each describing word is a sworn "
            "color: good, swift, sweet, strong - forty marks that paint "
            "the world, each sealed to its sentence."
        ),
        "drill": {
            "adjective_count": 25, "adverb_count": 15,
            "invariable_example": ("നല്ല", "നല്ല കുട്ടി", "നല്ല കുട്ടികൾ"),
            "builders": ["ഉള്ള", "മായ"],
            "adverb_endings": ["ആയി", "ഓടെ"],
            "comparative": "ഏക്കാൾ",
        },
    },
    {
        "key": "pronouns",
        "name": "Malayalam Pronouns",
        "group": "Core Vocabulary",
        "ladder_rank": 7,
        "ladder_tier": "foundations",
        "description": (
            "The full pronoun paradigms - personal, possessive, "
            "demonstrative, interrogative - each with translated example "
            "sentences. Malayalam marks formality in 'you' and keeps two "
            "words for 'we'. \n\n"
            "Personal pronouns:\n"
            "  ഞാൻ (njaan) - I. ഞാൻ വിദ്യാർത്ഥിയാണ്. - I am a student.\n"
            "  നീ (nii) - you (informal, to friends/children). നീ വരുന്നോ? "
            "- Are you coming?\n"
            "  നിങ്ങൾ (ningalL) - you (formal/plural). നിങ്ങൾ "
            "സുഖമാണോ? - Are you well?\n"
            "  അവൻ (avan) - he. അവൻ എന്റെ സഹോദരനാണ്. - He is my brother.\n"
            "  അവൾ (aval) - she. അവൾ എന്റെ സഹോദരിയാണ്. - She is my "
            "sister.\n"
            "  അത് (atu) - it. അത് പുസ്തകമാണ്. - It is a book.\n"
            "  ഞങ്ങൾ (njangalL) - we (excluding the listener). ഞങ്ങൾ "
            "പോകുന്നു. - We (not you) are going.\n"
            "  നമ്മൾ (nammalL) - we (including the listener). നമ്മൾ "
            "ഒരുമിച്ച് പോകാം. - Let's go together (you and I).\n"
            "  അവർ (avar) - they (people). അവർ വന്നു. - They came.\n"
            "  അവ (ava) - they (things). അവ വലുതാണ്. - They are big.\n\n"
            "Possessives (add -എ/-ഉടെ):\n"
            "  എന്റെ (enTe) - my. എന്റെ പുസ്തകം. - My book.\n"
            "  നിന്റെ (ninTe) - your (informal). നിന്റെ വീട്. - Your house.\n"
            "  നിങ്ങളുടെ (ningalLute) - your (formal). നിങ്ങളുടെ പേര്? - "
            "Your name?\n"
            "  അവന്റെ (avanTe) - his. അവന്റെ കാർ. - His car.\n"
            "  അവളുടെ (avalLute) - her. അവളുടെ ഫോൺ. - Her phone.\n"
            "  നമ്മുടെ (nammute) - our. നമ്മുടെ നാട്. - Our land.\n\n"
            "Demonstratives:\n"
            "  ഇത് (itu) - this. ഇത് എന്താണ്? - What is this?\n"
            "  അത് (atu) - that. അത് ദൂരെയാണ്. - That is far.\n"
            "  ഇവൻ (ivan) - this man. ഇവൻ എന്റെ സുഹൃത്താണ്. - This man is "
            "my friend.\n"
            "  അവൾ (aval) - that woman. അവൾ ഡോക്ടറാണ്. - That woman is a "
            "doctor.\n"
            "  ഇവർ (ivar) - these people. ഇവർ വന്നു. - These people came.\n\n"
            "Interrogatives:\n"
            "  ആര് (aaru) - who. ആര് വന്നു? - Who came?\n"
            "  എന്ത് (entu) - what. എന്ത് വേണം? - What do you want?\n"
            "  ഏത് (eetu) - which. ഏത് പുസ്തകം? - Which book?\n"
            "  എവിടെ (evite) - where. എവിടെ പോകുന്നു? - Where are you "
            "going?\n"
            "  എപ്പോൾ (eppoolL) - when. എപ്പോൾ വരും? - When will (you) "
            "come?\n"
            "  എന്തുകൊണ്ട് (entukonTu) - why. എന്തുകൊണ്ട് കരയുന്നു? - Why "
            "are you crying?\n"
            "  എങ്ങനെ (engane) - how. എങ്ങനെയുണ്ട്? - How are you?\n"
            "  എത്ര (etra) - how much/many. എത്ര രൂപ? - How many rupees?"
        ),
        "how_it_works": (
            "Pronouns decline through the same seven cases as nouns: ഞാൻ "
            "(I) becomes എന്നെ (me, accusative), എനിക്ക് (to me, dative), "
            "എന്റെ (my, genitive). The two 'we' words are the famous "
            "inclusive/exclusive split: നമ്മൾ includes the person you are "
            "talking to (we = you and I), ഞങ്ങൾ excludes them (we = I and "
            "others, not you) - using the wrong one changes the meaning of "
            "an invitation. നീ is intimate (friends, children, juniors); "
            "നിങ്ങൾ is respectful and also the plural. Third-person "
            "pronouns grade by distance and respect: അവൻ/അവൾ (he/she), "
            "with remote forms like അദ്ദേഹം for honored elders. അവർ is "
            "both 'they' (people) and the respectful 'he/she'."
        ),
        "key_points": [
            "Two words for 'we': നമ്മൾ (inclusive) vs ഞങ്ങൾ (exclusive).",
            "നീ informal/intimate; നിങ്ങൾ formal and plural.",
            "Pronouns decline like nouns: ഞാൻ/എന്നെ/എനിക്ക്/എന്റെ.",
            "അവർ = they (people) and respectful he/she.",
            "Interrogatives: ആര് who, എന്ത് what, എവിടെ where, എപ്പോൾ when, എന്തുകൊണ്ട് why, എങ്ങനെ how.",
        ],
        "requirements": [
            "Read the noun record for the case system the pronouns follow.",
            "Practice the inclusive/exclusive 'we' in spoken invitations.",
        ],
        "standards": [
            "Paradigms follow Asher & Kumari 1997.",
            "Practice sentences are constructed by the archive for teaching.",
        ],
        "citations": [CIT_ASHER, CIT_ANDRONOV],
        "must_contain": ["നമ്മൾ", "ഞങ്ങൾ", "നിങ്ങൾ", "എന്റെ", "എവിടെ"],
        "sig_lens": (
            "Through the Signature lens each pronoun is a sworn pointing: "
            "I, you, we-together, we-apart - marks that aim the sentence "
            "at its people, sealed with the inclusive vow."
        ),
        "drill": {
            "personal": ["ഞാൻ", "നീ", "നിങ്ങൾ", "അവൻ", "അവൾ", "അത്",
                         "ഞങ്ങൾ", "നമ്മൾ", "അവർ", "അവ"],
            "possessive": ["എന്റെ", "നിന്റെ", "നിങ്ങളുടെ", "അവന്റെ",
                           "അവളുടെ", "നമ്മുടെ"],
            "demonstrative": ["ഇത്", "അത്", "ഇവൻ", "അവൾ", "ഇവർ"],
            "interrogative": ["ആര്", "എന്ത്", "ഏത്", "എവിടെ", "എപ്പോൾ",
                              "എന്തുകൊണ്ട്", "എങ്ങനെ", "എത്ര"],
            "we_split": ("നമ്മൾ", "ഞങ്ങൾ"),
        },
    },
    {
        "key": "numbers",
        "name": "Malayalam Numbers and Time",
        "group": "Core Vocabulary",
        "ladder_rank": 8,
        "ladder_tier": "foundations",
        "description": (
            "Numbers 1-100, ordinals, days, months, seasons, clock time, and "
            "dates - each with translated example sentences. \n\n"
            "Cardinal numbers 1-10:\n"
            "  1 ഒന്ന് (onnu), 2 രണ്ട് (ranTu), 3 മൂന്ന് (muunnu), 4 നാല് "
            "(naalu), 5 അഞ്ച് (anchu), 6 ആറ് (aaRu), 7 ഏഴ് (eezhu), 8 എട്ട് "
            "(ettu), 9 ഒമ്പത് (ompatu), 10 പത്ത് (pattu)\n"
            "11-20: പതിനൊന്ന് (11), പന്ത്രണ്ട് (12), പതിമൂന്ന് (13), "
            "പതിനാല് (14), പതിനഞ്ച് (15), പതിനാറ് (16), പതിനേഴ് (17), "
            "പതിനെട്ട് (18), പത്തൊമ്പത് (19), ഇരുപത് (20)\n"
            "Tens: 30 മുപ്പത്, 40 നാൽപ്പത്, 50 അമ്പത്, 60 അറുപത്, 70 "
            "എഴുപത്, 80 എൺപത്, 90 തൊണ്ണൂറ്, 100 നൂറ്\n"
            "  എനിക്ക് രണ്ട് പുസ്തകങ്ങളുണ്ട്. - I have two books.\n"
            "  ഇരുപത് രൂപ തരൂ. - Give twenty rupees.\n\n"
            "Ordinals: ഒന്നാം (first), രണ്ടാം (second), മൂന്നാം (third) - "
            "ഒന്നാമത്തെ ദിവസം (the first day). \n\n"
            "Days of the week:\n"
            "  ഞായർ (nyaayar) Sunday, തിങ്കൾ (tingalL) Monday, ചൊവ്വ "
            "(chovva) Tuesday, ബുധൻ (budhan) Wednesday, വ്യാഴം (vyaazham) "
            "Thursday, വെള്ളി (velLli) Friday, ശനി (shani) Saturday\n"
            "  ഇന്ന് തിങ്കളാണ്. - Today is Monday.\n\n"
            "Malayalam months (the Kollam-era calendar): ചിങ്ങം, കന്നി, "
            "തുലാം, വൃശ്ചികം, ധനു, മകരം, കുംഭം, മീനം, മേടം (വിഷു "
            "new year), ഇടവം, മിഥുനം, കർക്കടകം. \n\n"
            "Clock time: മണി (manNi) = o'clock. മൂന്ന് മണി (3 o'clock), "
            "അഞ്ചര (5:30, anchara), ആറേകാൽ (6:15). എത്ര മണിയായി? - What "
            "time is it? \n\n"
            "Dates and seasons: തീയതി (tiiyati, date), മാസം (maasam, "
            "month), വർഷം (varsham, year). Seasons: വേനൽക്കാലം (summer), "
            "മഴക്കാലം (monsoon), ശീതകാലം (winter). ഇന്ന് ഏത് തീയതിയാണ്? - "
            "What is today's date?"
        ),
        "how_it_works": (
            "Numbers build by compounding: പത്ത് (10) + ഒന്ന് (1) fuses "
            "into പതിനൊന്ന് (11); ഇരുപത് (20) + അഞ്ച് (5) gives "
            "ഇരുപത്തഞ്ച് (25). Tens have their own roots (മുപ്പത്, "
            "നാൽപ്പത്) learned as units. Ordinals add -ആം: ഒന്ന് becomes "
            "ഒന്നാം (first). Time is told with മണി: number + മണി, with "
            "അര (half) and കാൽ (quarter) for the fractions - അഞ്ചര is "
            "5:30. The traditional calendar's new year is വിഷു in മേടം "
            "(April). Malayalam digits ൦-൯ from the writing record appear "
            "on calendars and invitations; Arabic numerals rule daily "
            "life."
        ),
        "key_points": [
            "1-10: ഒന്ന് രണ്ട് മൂന്ന് നാല് അഞ്ച് ആറ് ഏഴ് എട്ട് ഒമ്പത് പത്ത്.",
            "11-19 compound with പത്ത്: പതിനൊന്ന്, പന്ത്രണ്ട്...",
            "Tens: മുപ്പത് 30, നാൽപ്പത് 40, അമ്പത് 50, അറുപത് 60, എഴുപത് 70, എൺപത് 80, തൊണ്ണൂറ് 90, നൂറ് 100.",
            "Ordinals add -ആം: ഒന്നാം first, രണ്ടാം second.",
            "Time: number + മണി; അര half, കാൽ quarter (അഞ്ചര = 5:30).",
            "Days ഞായർ-ശനി; 12 Malayalam months; new year വിഷു in മേടം.",
        ],
        "requirements": [
            "Count 1-20 aloud until the compounds feel automatic.",
            "Read the writing record for the Malayalam digits ൦-൯.",
        ],
        "standards": [
            "Number forms follow standard Malayalam (Asher & Kumari 1997).",
            "Practice sentences are constructed by the archive for teaching.",
        ],
        "citations": [CIT_ASHER, CIT_ANDRONOV],
        "must_contain": ["പതിനൊന്ന്", "മുപ്പത്", "മണി", "വിഷു", "തിങ്കൾ"],
        "sig_lens": (
            "Through the Signature lens numbers are sworn counts: one "
            "through a hundred, each a mark in sequence, each hour a vow "
            "struck on the clock of the archive."
        ),
        "drill": {
            "one_to_ten": ["ഒന്ന്", "രണ്ട്", "മൂന്ന്", "നാല്", "അഞ്ച്",
                           "ആറ്", "ഏഴ്", "എട്ട്", "ഒമ്പത്", "പത്ത്"],
            "tens": {"30": "മുപ്പത്", "40": "നാൽപ്പത്", "50": "അമ്പത്",
                     "60": "അറുപത്", "70": "എഴുപത്", "80": "എൺപത്",
                     "90": "തൊണ്ണൂറ്", "100": "നൂറ്"},
            "eleven": "പതിനൊന്ന്",
            "days": ["ഞായർ", "തിങ്കൾ", "ചൊവ്വ", "ബുധൻ", "വ്യാഴം",
                     "വെള്ളി", "ശനി"],
            "months": ["ചിങ്ങം", "കന്നി", "തുലാം", "വൃശ്ചികം", "ധനു",
                       "മകരം", "കുംഭം", "മീനം", "മേടം", "ഇടവം",
                       "മിഥുനം", "കർക്കടകം"],
            "oclock": "മണി", "half": "അര", "quarter": "കാൽ",
        },
    },
    {
        "key": "greetings",
        "name": "Malayalam Greetings and Everyday Phrases",
        "group": "Core Vocabulary",
        "ladder_rank": 9,
        "ladder_tier": "foundations",
        "description": (
            "Thirty greetings, farewells, and politeness phrases - each "
            "with romanization, English, and a usage note. \n\n"
            "  1. നമസ്കാരം (namaskaaram) - Hello (respectful greeting).\n"
            "  2. സുഖമാണോ? (sukhamaan oo?) - Are you well? (standard "
            "how-are-you).\n"
            "  3. എങ്ങനെയുണ്ട്? (enganeyunTu?) - How is it going?\n"
            "  4. സുപ്രഭാതം (suprabhaatam) - Good morning (formal).\n"
            "  5. ശുഭദിനം (shubhadinam) - Good day.\n"
            "  6. ശുഭരാത്രി (shubharaatri) - Good night.\n"
            "  7. നന്ദി (nanni) - Thank you.\n"
            "  8. വളരെ നന്ദി (valare nanni) - Thank you very much.\n"
            "  9. ദയവായി (dayavaayi) - Please (requesting).\n"
            "  10. ക്ഷമിക്കണം (kshamikkanam) - Excuse me / sorry.\n"
            "  11. സാരമില്ല (saaramilla) - It doesn't matter / never mind.\n"
            "  12. കുഴപ്പമില്ല (kuzhappamilla) - No problem.\n"
            "  13. സ്വാഗതം (svaagatam) - Welcome.\n"
            "  14. സന്തോഷം (santoshham) - Glad to meet you (lit. "
            "happiness).\n"
            "  15. കാണാം (kaanaam) - See you.\n"
            "  16. പിന്നെ കാണാം (pinne kaanaam) - See you later.\n"
            "  17. വിട (vita) - Goodbye (farewell).\n"
            "  18. യാത്ര സുഖകരമാകട്ടെ (yaatra sukhakaramaakatte) - Have a "
            "safe journey.\n"
            "  19. അഭിനന്ദനങ്ങൾ (abhinandanangalL) - Congratulations.\n"
            "  20. ആശംസകൾ (aashamsakalL) - Best wishes.\n"
            "  21. ആശംസിക്കുന്നു (aashamsikkunnu) - (I) wish you well.\n"
            "  22. സുഖമായിരിക്കുക (sukhamaayirikku ka) - Stay well (parting "
            "blessing).\n"
            "  23. ദൈവം അനുഗ്രഹിക്കട്ടെ (daivam anugrahikkatte) - God bless "
            "you.\n"
            "  24. എനിക്ക് മനസ്സിലായി (enikku manassilaayi) - I understood.\n"
            "  25. എനിക്ക് മനസ്സിലായില്ല (enikku manassilaayilla) - I "
            "didn't understand.\n"
            "  26. പതുക്കെ പറയൂ (patukke parayuu) - Please speak slowly.\n"
            "  27. വീണ്ടും പറയൂ (viinTum parayuu) - Please say it again.\n"
            "  28. സഹായിക്കാമോ? (sahaayikkaamoo?) - Can you help?\n"
            "  29. അതെ (ate) - Yes. / ഇല്ല (illa) - No.\n"
            "  30. ശരി (shari) - OK / alright."
        ),
        "how_it_works": (
            "Malayalam greetings run on warmth and formality together. "
            "നമസ്കാരം opens any respectful meeting; among friends a "
            "simple സുഖമാണോ does the work. Requests soften with ദയവായി "
            "or the gentle imperative -ൂ (പറയൂ, please say). Apologies "
            "and thanks are short - നന്ദി, ക്ഷമിക്കണം - and never "
            "overlong. The learner's survival kit is phrases 24-27: "
            "മനസ്സിലായില്ല (I didn't understand), പതുക്കെ പറയൂ (speak "
            "slowly), വീണ്ടും പറയൂ (say again) - with these three, any "
            "conversation can be steered. അതെ/ഇല്ല answer everything; "
            "ശരി seals agreement."
        ),
        "key_points": [
            "നമസ്കാരം: the universal respectful greeting.",
            "സുഖമാണോ: the standard how-are-you.",
            "Soft requests: ദയവായി + gentle imperative -ൂ.",
            "Learner survival kit: മനസ്സിലായില്ല, പതുക്കെ പറയൂ, വീണ്ടും പറയൂ.",
            "അതെ yes / ഇല്ല no / ശരി OK.",
        ],
        "requirements": [
            "Greet someone with നമസ്കാരം today.",
            "Memorize the three survival phrases before the conversation records.",
        ],
        "standards": [
            "Phrases are standard Kerala usage (Asher & Kumari 1997).",
            "Usage notes reflect common spoken practice.",
        ],
        "citations": [CIT_ASHER],
        "must_contain": ["നമസ്കാരം", "സുഖമാണോ", "ക്ഷമിക്കണം", "മനസ്സിലായില്ല", "അതെ"],
        "sig_lens": (
            "Through the Signature lens each greeting is a sworn "
            "welcome: thirty vows of courtesy, from the first "
            "നമസ്കാരം to the last ശരി, each sealed with warmth."
        ),
        "drill": {
            "count": 30,
            "hello": "നമസ്കാരം", "how_are_you": "സുഖമാണോ",
            "thanks": "നന്ദി", "please": "ദയവായി", "sorry": "ക്ഷമിക്കണം",
            "yes": "അതെ", "no": "ഇല്ല", "ok": "ശരി",
            "survival": ["എനിക്ക് മനസ്സിലായില്ല", "പതുക്കെ പറയൂ",
                         "വീണ്ടും പറയൂ"],
        },
    },
    {
        "key": "grammar",
        "name": "Malayalam Grammar Essentials",
        "group": "Grammar Essentials",
        "ladder_rank": 10,
        "ladder_tier": "foundations",
        "description": (
            "The ten load-bearing rules of Malayalam - each with "
            "translated example sentences. \n\n"
            "1. Word order is SOV. ഞാൻ (I) ചോറ് (rice) കഴിക്കുന്നു (eat). "
            "- I eat rice.\n"
            "2. No grammatical gender for things. Adjectives never change: "
            "നല്ല പുസ്തകം, നല്ല പുസ്തകങ്ങൾ.\n"
            "3. Seven cases (vibhakti) attach as suffixes: nominative "
            "(unmarked), accusative -എ, dative -ന്/-ക്ക്, sociative -ഓട്, "
            "instrumental -കൊണ്ട്, genitive -ഉടെ, locative -ഇൽ. വീട് -> "
            "വീട്ടിൽ (in the house); അമ്മ -> അമ്മയ്ക്ക് (to mother).\n"
            "4. Postpositions, not prepositions: മേശയുടെ മുകളിൽ (on the "
            "table, lit. table's top-in).\n"
            "5. Three tenses on the verb: present -unnu, past -i, future "
            "-um. പോകുന്നു / പോയി / പോകും.\n"
            "6. The copula ആണ് (aanu) links nouns: അവൻ ഡോക്ടറാണ് (he is "
            "a doctor). Past: ആയിരുന്നു. Future: ആകും.\n"
            "7. Negation: അല്ല (alla) denies identity - അവൻ ഡോക്ടറല്ല "
            "(he is not a doctor); ഇല്ല (illa) denies existence/action - "
            "അവൻ വന്നില്ല (he did not come).\n"
            "8. Questions: add -ഓ to the verb - നീ വരുന്നോ? (are you "
            "coming?); or start with a question word - എവിടെ പോകുന്നു? "
            "(where are you going?)\n"
            "9. Plurals with -കൾ: പുസ്തകങ്ങൾ (books). Pronouns have their "
            "own plurals (ഞാൻ -> ഞങ്ങൾ).\n"
            "10. Honorifics: നിങ്ങൾ for respected 'you'; അവർ for "
            "respected he/she; -തേ honorific verb endings in formal "
            "address."
        ),
        "how_it_works": (
            "The engine works like this: pick the noun, glue the case "
            "suffix to it, place the object before the verb, and close "
            "with the tensed verb. എനിക്ക് (to me, dative of ഞാൻ) വെള്ളം "
            "(water, object) വേണം (is wanted, verb) - 'I want water' "
            "built exactly as Malayalam thinks it. Cases replace "
            "prepositions: -ഇൽ means 'in', -ഓട് means 'with', -കൊണ്ട് "
            "means 'with/by means of'. The verb agrees with the subject "
            "in person, never in gender. Negation splits cleanly: അല്ല "
            "for 'is not', ഇല്ല for 'does not / there is not'. Questions "
            "need no word-order change - just the -ഓ particle or a "
            "question word. With these ten rules every later record's "
            "sentences become transparent."
        ),
        "key_points": [
            "SOV word order; verb always last.",
            "Seven cases as suffixes: -എ -ന്/-ക്ക് -ഓട് -കൊണ്ട് -ഉടെ -ഇൽ.",
            "Postpositions, not prepositions.",
            "Tenses: -unnu present, -i past, -um future; copula ആണ്/ആയിരുന്നു/ആകും.",
            "Negation: അല്ല (is-not) vs ഇല്ല (does-not / there-is-not).",
            "Questions with -ഓ or question words; no word-order change.",
        ],
        "requirements": [
            "Read all vocabulary records first so the examples land.",
            "Parse five sentences into S-O-V before the themed records.",
        ],
        "standards": [
            "Grammar follows Asher & Kumari 1997 and Andronov 1996.",
            "Case labels use the traditional vibhakti names.",
            "Practice sentences are constructed by the archive for teaching.",
        ],
        "citations": [CIT_ASHER, CIT_ANDRONOV],
        "must_contain": ["SOV", "vibhakti", "ആണ്", "അല്ല", "-ഓ", "Postpositions"],
        "sig_lens": (
            "Through the Signature lens these ten rules are the ten "
            "load-bearing vows of the language: every case a sealed joint, "
            "every verb-ending a covenant that the sentence will stand."
        ),
        "drill": {
            "rules": 10, "word_order": "SOV",
            "cases": ["nominative", "accusative", "dative", "sociative",
                      "instrumental", "genitive", "locative"],
            "case_suffixes": ["എ", "ന്", "ക്ക്", "ഓട്", "കൊണ്ട്", "ഉടെ", "ഇൽ"],
            "tenses": {"present": "unnu", "past": "i", "future": "um"},
            "copula": ["ആണ്", "ആയിരുന്നു", "ആകും"],
            "negation": ["അല്ല", "ഇല്ല"],
            "question_particle": "ഓ",
        },
    },
    {
        "key": "home",
        "name": "Malayalam Home and Family Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 11,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences on house, rooms, furniture, and family "
            "members - each in Malayalam with romanization and English. \n\n"
            "  1. ഇത് എന്റെ വീടാണ്. (itu enTe viitaan u.) - This is my "
            "house.\n"
            "  2. വീട്ടിൽ നാല് മുറികളുണ്ട്. (viittil naalu murikalunTu.) - "
            "There are four rooms in the house.\n"
            "  3. അടുക്കളയിൽ അമ്മ പാചകം ചെയ്യുന്നു. (atukkalayil amma "
            "paachakam cheyyunnu.) - Mother is cooking in the kitchen.\n"
            "  4. കിടപ്പുമുറിയിൽ കട്ടിലുണ്ട്. (kitappumuriyil kattilunTu.) "
            "- There is a bed in the bedroom.\n"
            "  5. സ്വീകരണമുറിയിൽ സോഫയുണ്ട്. (sviikaranamuriyil soofayunTu.) "
            "- There is a sofa in the living room.\n"
            "  6. മേശപ്പുറത്ത് പുസ്തകങ്ങളുണ്ട്. (meeshappurattu "
            "pustakangalunTu.) - There are books on the table.\n"
            "  7. കസേരയിൽ ആരിരിക്കുന്നു? (kaseerayil aaririkkunnu?) - Who is "
            "sitting on the chair?\n"
            "  8. ജനലിലൂടെ കാറ്റ് വരുന്നു. (janaliloote kaattu varunnu.) - "
            "Wind comes through the window.\n"
            "  9. വാതിൽ അടയ്ക്കൂ. (vaatil ataykkuu.) - Please close the "
            "door.\n"
            "  10. എന്റെ കുടുംബം വലുതാണ്. (enTe kutumbam valutaanu.) - My "
            "family is big.\n"
            "  11. എനിക്ക് രണ്ട് സഹോദരന്മാരുണ്ട്. (enikku ranTu "
            "sahoodaranmaarunTu.) - I have two brothers.\n"
            "  12. എന്റെ സഹോദരി അധ്യാപികയാണ്. (enTe sahoodari "
            "adhyaapikayaanu.) - My sister is a teacher.\n"
            "  13. അമ്മാവൻ നാട്ടിൽ താമസിക്കുന്നു. (ammaavan naattil "
            "taamasikkunnu.) - Uncle lives in the village.\n"
            "  14. അമ്മായി നല്ലവളാണ്. (ammaayi nallaval aanu.) - Aunt is "
            "kind.\n"
            "  15. മുത്തശ്ശൻ കഥ പറയുന്നു. (muttashshan kata parayunnu.) - "
            "Grandfather tells stories.\n"
            "  16. മുത്തശ്ശി പായസം ഉണ്ടാക്കുന്നു. (muttashshi paayasam "
            "unTaakkunnu.) - Grandmother makes payasam.\n"
            "  17. കുട്ടികൾ മുറ്റത്ത് കളിക്കുന്നു. (kuttikal muttattu "
            "kalikkunnu.) - The children play in the courtyard.\n"
            "  18. ഞങ്ങൾ ഒരുമിച്ച് ഭക്ഷണം കഴിക്കുന്നു. (njangalL orumichchu "
            "bhakshanam kazhikkunnu.) - We eat food together.\n"
            "  19. വീട് വൃത്തിയായി സൂക്ഷിക്കുക. (viitu vruttiyaayi "
            "suukshikkuka.) - Keep the house clean.\n"
            "  20. എന്റെ വീട്ടിലേക്ക് സ്വാഗതം. (enTe viittilekku "
            "svaagatam.) - Welcome to my house. \n\n"
            "The existence verb is ഉണ്ട് (there is): മുറിയിൽ കട്ടിലുണ്ട് "
            "(there is a bed in the room)."
        ),
        "how_it_works": (
            "Home sentences run on the locative -ഇൽ and the existence verb "
            "ഉണ്ട് (there is): room + ഇൽ + thing + ഉണ്ട് builds every "
            "'there is' sentence in the set. Family words pair by gender: "
            "അച്ഛൻ/അമ്മ, സഹോദരൻ/സഹോദരി, മുത്തശ്ശൻ/മുത്തശ്ശി, അമ്മാവൻ/അമ്മായി. "
            "Direction uses -ഇലേക്ക് (toward): വീട്ടിലേക്ക് (to the "
            "house). Commands soften with -ൂ: അടയ്ക്കൂ (please close). "
            "Notice the SOV skeleton holding in every line: subject, "
            "place-phrase, verb last."
        ),
        "key_points": [
            "ഉണ്ട് (there is) + locative -ഇൽ builds 'there is' sentences.",
            "Family pairs: അച്ഛൻ/അമ്മ, സഹോദരൻ/സഹോദരി, മുത്തശ്ശൻ/മുത്തശ്ശി.",
            "Direction -ഇലേക്ക്: വീട്ടിലേക്ക് (to the house).",
            "Soft commands with -ൂ: അടയ്ക്കൂ.",
            "20 sentences: house, rooms, furniture, family.",
        ],
        "requirements": [
            "Read the grammar record for -ഇൽ and ഉണ്ട്.",
            "Describe your own house in five Malayalam sentences.",
        ],
        "standards": [
            "Forms follow standard Malayalam (Asher & Kumari 1997).",
            "Practice sentences are constructed by the archive for teaching.",
        ],
        "citations": [CIT_ASHER],
        "must_contain": ["ഉണ്ട്", "അടുക്കള", "മുത്തശ്ശി", "വീട്ടിലേക്ക്", "സ്വാഗതം"],
        "sig_lens": (
            "Through the Signature lens the home is the first sealed "
            "covenant: every room a vow of shelter, every family name a "
            "mark of belonging."
        ),
        "drill": {
            "sentences": 20, "existence_verb": "ഉണ്ട്",
            "locative": "ഇൽ", "direction": "ഇലേക്ക്",
            "family_pairs": [("അച്ഛൻ", "അമ്മ"), ("സഹോദരൻ", "സഹോദരി"),
                             ("മുത്തശ്ശൻ", "മുത്തശ്ശി"),
                             ("അമ്മാവൻ", "അമ്മായി")],
        },
    },
    {
        "key": "food",
        "name": "Malayalam Food and Cooking Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 12,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences on meals, ingredients, cooking actions, and "
            "the restaurant - each with romanization and English. \n\n"
            "  1. ഞാൻ രാവിലെ ഇഡ്ഡലി കഴിച്ചു. (njaan raavile iddali "
            "kazhichchu.) - I ate idli in the morning.\n"
            "  2. ഉച്ചയ്ക്ക് ചോറും സാമ്പാറും. (uchchaykku choorum "
            "saambaarum.) - Rice and sambar at noon.\n"
            "  3. അമ്മ ദോശ ചുടുന്നു. (amma doosha chutunnu.) - Mother is "
            "making dosa.\n"
            "  4. കറി എരിവുള്ളതാണ്. (kari erivulLataan u.) - The curry is "
            "spicy.\n"
            "  5. മീൻ കറി രുചികരമാണ്. (miin kari ruchikaramaanu.) - Fish "
            "curry is tasty.\n"
            "  6. ചായയിൽ പഞ്ചസാര കുറയ്ക്കൂ. (chaayayil panchasaara "
            "kuraykkuu.) - Reduce the sugar in the tea.\n"
            "  7. കാപ്പി ചൂടോടെ കുടിക്കുക. (kaappi chuutootte kutikkuka.) - "
            "Drink the coffee hot.\n"
            "  8. പച്ചക്കറി അരിയുക. (pachakkari ariyuka.) - Chop the "
            "vegetables.\n"
            "  9. ഉള്ളി വഴറ്റുക. (ullLi vazhattuka.) - Saute the onions.\n"
            "  10. വെള്ളം തിളപ്പിക്കുക. (velLlam tilappikkuka.) - Boil the "
            "water.\n"
            "  11. അരി കഴുകുക. (ari kazhukuka.) - Wash the rice.\n"
            "  12. അടുപ്പ് കത്തിക്കുക. (atuppu kattikkuka.) - Light the "
            "stove.\n"
            "  13. ഉപ്പ് ചേർക്കൂ. (uppu cheerkkuu.) - Add salt.\n"
            "  14. തേങ്ങാ ചിരകുക. (teengaa chirakuka.) - Grate the coconut.\n"
            "  15. പായസം മധുരമുള്ളതാണ്. (paayasam madhuramulLataan u.) - "
            "Payasam is sweet.\n"
            "  16. ഹോട്ടലിൽ മേശ ബുക്ക് ചെയ്യൂ. (hoottalil meesha bukku "
            "cheyyuu.) - Book a table at the hotel.\n"
            "  17. മെനു കാണിക്കൂ. (menu kaanikkuu.) - Please show the menu.\n"
            "  18. ബില്ല് തരൂ. (billu taruu.) - Please give the bill.\n"
            "  19. ഭക്ഷണം വളരെ നന്നായിരുന്നു. (bhakshanam valare "
            "nannaayirunnu.) - The food was very good.\n"
            "  20. വിശന്നിരിക്കുന്നു; ഭക്ഷണം കഴിക്കാം. (vishannirikkunnu; "
            "bhakshanam kazhikkaam.) - (I) am hungry; let's eat."
        ),
        "how_it_works": (
            "Food sentences run on cooking verbs in the imperative -ൂ "
            "(ചേർക്കൂ, അരിയുക -> അരിയൂ) and tasting adjectives with "
            "-ഉള്ള (എരിവുള്ള, മധുരമുള്ള). Meals divide the day: പ്രാതൽ "
            "(breakfast), ഉച്ചഭക്ഷണം (lunch), അത്താഴം (dinner). Restaurant "
            "Malayalam borrows freely - മെനു, ബില്ല്, ബുക്ക് - with "
            "Malayalam grammar wrapped around the loans. The polite request "
            "pattern is noun + തരൂ/കാണിക്കൂ; the kitchen command pattern is "
            "ingredient + verb-ൂ. കഴിക്കാം (let's eat) is the inclusive "
            "suggestion form every host uses."
        ),
        "key_points": [
            "Kitchen imperatives with -ൂ: ചേർക്കൂ, അരിയൂ.",
            "Tasting adjectives: എരിവുള്ള, മധുരമുള്ള, രുചികരം.",
            "Meals: പ്രാതൽ, ഉച്ചഭക്ഷണം, അത്താഴം.",
            "Restaurant loans: മെനു, ബില്ല്, ബുക്ക് with Malayalam grammar.",
            "20 sentences: meals, ingredients, cooking, restaurant.",
        ],
        "requirements": [
            "Read the verb record for imperative forms.",
            "Name five Kerala dishes in Malayalam.",
        ],
        "standards": [
            "Forms follow standard Malayalam (Asher & Kumari 1997).",
            "Practice sentences are constructed by the archive for teaching.",
        ],
        "citations": [CIT_ASHER],
        "must_contain": ["പായസം", "സാമ്പാറും", "ചേർക്കൂ", "ബില്ല്", "കഴിക്കാം"],
        "sig_lens": (
            "Through the Signature lens the kitchen is a covenant of "
            "nourishment: every ingredient a sworn gift, every shared meal "
            "a seal of togetherness."
        ),
        "drill": {
            "sentences": 20,
            "meals": ["പ്രാതൽ", "ഉച്ചഭക്ഷണം", "അത്താഴം"],
            "imperative": "ൂ",
            "dishes": ["ഇഡ്ഡലി", "ദോശ", "സാമ്പാർ", "പായസം", "മീൻ കറി"],
        },
    },
    {
        "key": "travel",
        "name": "Malayalam Travel and Directions Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 13,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences on transport, asking directions, tickets, "
            "and lodging - each with romanization and English. \n\n"
            "  1. റെയിൽവേ സ്റ്റേഷൻ എവിടെയാണ്? (reyilve stteshan "
            "eviteyaanu?) - Where is the railway station?\n"
            "  2. ബസ് സ്റ്റാൻഡ് അടുത്താണോ? (basu sttaantu atuttaanoo?) - Is "
            "the bus stand near?\n"
            "  3. നേരെ പോയി വലത്തോട്ട് തിരിയൂ. (neere pooyi valattoottu "
            "tiriyuu.) - Go straight and turn right.\n"
            "  4. ഇടത്തോട്ടാണ് ക്ഷേത്രം. (itattoottaanu kshetram.) - The "
            "temple is to the left.\n"
            "  5. എത്ര ദൂരമുണ്ട്? (etra duuramunTu?) - How far is it?\n"
            "  6. ഓട്ടോ വിളിക്കൂ. (oottoo vilikkuu.) - Call an auto.\n"
            "  7. ടാക്സി കിട്ടുമോ? (ttaaksi kittumoo?) - Can I get a taxi?\n"
            "  8. കൊച്ചിയിലേക്ക് ഒരു ടിക്കറ്റ്. (kochchiyilekku oru "
            "ttikkattu.) - One ticket to Kochi.\n"
            "  9. ട്രെയിൻ എപ്പോൾ വരും? (ttreyin eppoolL varum?) - When "
            "will the train come?\n"
            "  10. ബസ് എത്ര മണിക്ക് പുറപ്പെടും? (basu etra mannikku "
            "purappetum?) - At what time does the bus leave?\n"
            "  11. ഈ സീറ്റ് ഒഴിവാണോ? (ii siittu ozhivaanoo?) - Is this seat "
            "free?\n"
            "  12. വിമാനത്താവളം ദൂരെയാണ്. (vimaanattaavalam duurayaanu.) - "
            "The airport is far.\n"
            "  13. ഹോട്ടലിൽ മുറി ബുക്ക് ചെയ്തിട്ടുണ്ട്. (hoottalil muri "
            "bukku cheytittunTu.) - A room is booked at the hotel.\n"
            "  14. ഒരു രാത്രിക്ക് എത്ര രൂപ? (oru raattrikku etra ruupa?) - "
            "How much for one night?\n"
            "  15. വെള്ളം കിട്ടുമോ? (velLlam kittumoo?) - Can I get water?\n"
            "  16. മാപ്പ് കാണിക്കൂ. (maappu kaanikkuu.) - Please show the "
            "map.\n"
            "  17. ഞാൻ വഴി തെറ്റി. (njaan vazhi tetti.) - I lost my way.\n"
            "  18. സഹായിക്കാമോ? (sahaayikkaamoo?) - Can you help?\n"
            "  19. യാത്ര സുഖകരമായിരുന്നു. (yaatra sukhakaramaayirunnu.) - "
            "The journey was pleasant.\n"
            "  20. നാളെ തിരിച്ചു പോകും. (naalLe tirichchu pookum.) - "
            "(I) will return tomorrow."
        ),
        "how_it_works": (
            "Direction sentences pivot on -ഇലേക്ക് (toward) and the "
            "left/right pair ഇടത്ത്/വലത്ത്: കൊച്ചിയിലേക്ക് (to Kochi), "
            "വലത്തോട്ട് (to the right). 'Is there / can I get' runs on "
            "ഉണ്ട് and കിട്ടുമോ: ടാക്സി കിട്ടുമോ? (can a taxi be got?). "
            "Ticket and time questions use എത്ര and എപ്പോൾ with the "
            "dative of purpose. The lost-traveler kit is three lines: "
            "ഞാൻ വഴി തെറ്റി (I lost my way), സഹായിക്കാമോ (can you help), "
            "മാപ്പ് കാണിക്കൂ (show the map). Transport loans - ബസ്, "
            "ട്രെയിൻ, ടിക്കറ്റ് - take Malayalam case endings like native "
            "nouns."
        ),
        "key_points": [
            "Directions: -ഇലേക്ക് (toward), ഇടത്ത്/വലത്ത് (left/right).",
            "'Can I get': കിട്ടുമോ with the noun.",
            "Time questions: എപ്പോൾ, എത്ര മണിക്ക്.",
            "Lost-traveler kit: വഴി തെറ്റി, സഹായിക്കാമോ, മാപ്പ് കാണിക്കൂ.",
            "20 sentences: transport, directions, tickets, lodging.",
        ],
        "requirements": [
            "Read the grammar record for -ഇലേക്ക് and the dative.",
            "Ask for directions to three real places in Malayalam.",
        ],
        "standards": [
            "Forms follow standard Malayalam (Asher & Kumari 1997).",
            "Practice sentences are constructed by the archive for teaching.",
        ],
        "citations": [CIT_ASHER],
        "must_contain": ["എവിടെയാണ്", "വലത്തോട്ട്", "കിട്ടുമോ", "ടിക്കറ്റ്", "വഴി തെറ്റി"],
        "sig_lens": (
            "Through the Signature lens every journey is a sworn passage: "
            "each direction a vow of arrival, each ticket a seal on the "
            "road."
        ),
        "drill": {
            "sentences": 20, "left": "ഇടത്ത്", "right": "വലത്ത്",
            "toward": "ഇലേക്ക്", "can_i_get": "കിട്ടുമോ",
            "transport": ["ബസ്", "ട്രെയിൻ", "ടാക്സി", "ഓട്ടോ", "വിമാനം"],
        },
    },
    {
        "key": "work",
        "name": "Malayalam Work and School Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 14,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences on jobs, the office, the classroom, and "
            "learning - each with romanization and English. \n\n"
            "  1. ഞാൻ അധ്യാപകനാണ്. (njaan adhyaapakanan u.) - I am a "
            "teacher.\n"
            "  2. അവൾ ഡോക്ടറാണ്. (aval ttaakttaraan u.) - She is a doctor.\n"
            "  3. അച്ഛൻ എഞ്ചിനീയറാണ്. (achchhan enjiniiyaran u.) - Father "
            "is an engineer.\n"
            "  4. ഞാൻ ഓഫീസിൽ ജോലി ചെയ്യുന്നു. (njaan oofiisil jooli "
            "cheyyunnu.) - I work in an office.\n"
            "  5. യോഗം പത്ത് മണിക്കാണ്. (yoogam pattu mannikkaan u.) - The "
            "meeting is at ten o'clock.\n"
            "  6. റിപ്പോർട്ട് എഴുതി തീർക്കൂ. (rippoor ttu ezhuti "
            "tiirkkuu.) - Finish writing the report.\n"
            "  7. ഇമെയിൽ അയച്ചിട്ടുണ്ടോ? (imeyil ayachchittunToo?) - Have "
            "you sent the email?\n"
            "  8. ശമ്പളം മാസാവസാനം കിട്ടും. (shampalam maasaavasaanam "
            "kittum.) - Salary comes at month's end.\n"
            "  9. അവധി എടുക്കാമോ? (avadh i etukkaamoo?) - May I take leave?\n"
            "  10. സഹപ്രവർത്തകർ സഹായിക്കുന്നു. (sahapravarttakar "
            "sahaayikkunnu.) - Colleagues help.\n"
            "  11. കുട്ടികൾ സ്കൂളിൽ പഠിക്കുന്നു. (kuttikal skuulil "
            "patThikkunnu.) - Children study at school.\n"
            "  12. അധ്യാപകൻ പാഠം വിശദീകരിക്കുന്നു. (adhyaapakan paattham "
            "vishadiikarikkunnu.) - The teacher explains the lesson.\n"
            "  13. പുസ്തകം തുറക്കൂ. (pustakam turakkuu.) - Open the book.\n"
            "  14. ചോദ്യത്തിന് ഉത്തരം പറയൂ. (choodyattinu uttaram parayuu.) "
            "- Answer the question.\n"
            "  15. ഹോംവർക്ക് ചെയ്തോ? (hoomvarkku cheytoo?) - Did you do the "
            "homework?\n"
            "  16. പരീക്ഷ നാളെയാണ്. (pariiksha naalLeyaanu.) - The exam is "
            "tomorrow.\n"
            "  17. നന്നായി പഠിച്ചാൽ ജയിക്കും. (nannaayi patThichchaal "
            "jayikkum.) - If you study well, you will pass.\n"
            "  18. ലൈബ്രറിയിൽ നിശ്ശബ്ദത പാലിക്കുക. (laybrariyil "
            "nishshabdata paalikkuka.) - Keep silence in the library.\n"
            "  19. എന്റെ സ്വപ്നം ഡോക്ടറാകുക എന്നതാണ്. (enTe svapnam "
            "ttaakt taraakuka ennataan u.) - My dream is to become a "
            "doctor.\n"
            "  20. ജോലി കഴിഞ്ഞ് വീട്ടിൽ പോകും. (jooli kazhynyu viittil "
            "pookum.) - After work (I) will go home."
        ),
        "how_it_works": (
            "Work sentences use the profession + ആണ് frame: ഞാൻ "
            "അധ്യാപകനാണ് (I am a teacher) - note the masculine -ൻ on the "
            "profession for a male speaker (അധ്യാപിക for a woman). Office "
            "commands use the -ൂ imperative or the perfective ചെയ്തിട്ടുണ്ട് "
            "(have done). School sentences run on the teacher/student pair "
            "അധ്യാപകൻ/വിദ്യാർത്ഥി and the lesson word പാഠം. Conditionals "
            "with -ആൽ (പഠിച്ചാൽ, if you study) open the 'if' pattern that "
            "the complex-sentences record expands. Time phrases anchor "
            "everything: പത്ത് മണിക്ക്, നാളെ, മാസാവസാനം."
        ),
        "key_points": [
            "Profession + ആണ്: അധ്യാപകനാണ് / അധ്യാപികയാണ്.",
            "Perfective ചെയ്തിട്ടുണ്ട്: അയച്ചിട്ടുണ്ടോ (have you sent?).",
            "Conditional -ആൽ: പഠിച്ചാൽ (if you study).",
            "Work/school vocabulary: യോഗം, ശമ്പളം, പരീക്ഷ, പാഠം.",
            "20 sentences: jobs, office, classroom, learning.",
        ],
        "requirements": [
            "Read the verb record for imperatives and perfectives.",
            "State your own job or dream job in Malayalam.",
        ],
        "standards": [
            "Forms follow standard Malayalam (Asher & Kumari 1997).",
            "Practice sentences are constructed by the archive for teaching.",
        ],
        "citations": [CIT_ASHER],
        "must_contain": ["അധ്യാപകനാണ്", "യോഗം", "പരീക്ഷ", "പഠിച്ചാൽ", "ശമ്പളം"],
        "sig_lens": (
            "Through the Signature lens work is a sworn craft: every "
            "profession a vow of service, every lesson a seal on the "
            "learner's future."
        ),
        "drill": {
            "sentences": 20,
            "professions": ["അധ്യാപകൻ", "ഡോക്ടർ", "എഞ്ചിനീയർ"],
            "conditional": "ആൽ", "perfective": "ഇട്ടുണ്ട്",
            "school_words": ["പാഠം", "പരീക്ഷ", "വിദ്യാർത്ഥി"],
        },
    },
    {
        "key": "health",
        "name": "Malayalam Health and Body Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 15,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences on body parts, symptoms, the doctor visit, "
            "and the pharmacy - each with romanization and English. \n\n"
            "  1. എന്റെ തല വേദനിക്കുന്നു. (enTe tala veedanikkunnu.) - My "
            "head aches.\n"
            "  2. കണ്ണിന് ചൊറിച്ചിൽ ഉണ്ട്. (kanninu chorichchil unTu.) - "
            "The eye itches.\n"
            "  3. പല്ല് വേദനിക്കുന്നു. (pallu veedanikkunnu.) - The tooth "
            "aches.\n"
            "  4. എനിക്ക് പനിയുണ്ട്. (enikku paniyunTu.) - I have a fever.\n"
            "  5. ചുമയും ജലദോഷവുമുണ്ട്. (chumayum jaladoshavumunTu.) - "
            "(I) have cough and cold.\n"
            "  6. വയറ് വേദനിക്കുന്നു. (vayaru veedanikkunnu.) - The stomach "
            "aches.\n"
            "  7. കാലിൽ മുറിവുണ്ട്. (kaalil murivunTu.) - There is a wound "
            "on the leg.\n"
            "  8. തൊണ്ട വേദനിക്കുന്നു. (tonTa veedanikkunnu.) - The throat "
            "hurts.\n"
            "  9. എനിക്ക് തലകറക്കം ഉണ്ട്. (enikku talakarakkam unTu.) - I "
            "feel dizzy.\n"
            "  10. ഡോക്ടറെ കാണണം. (ttaakt tare kaananam.) - (I) must see "
            "the doctor.\n"
            "  11. ആശുപത്രിയിൽ പോകൂ. (aashupatriyil pookuu.) - Go to the "
            "hospital.\n"
            "  12. എവിടെ വേദനിക്കുന്നു? (evite veedanikkunnu?) - Where does "
            "it hurt?\n"
            "  13. എത്ര ദിവസമായി? (etra divasamaayi?) - For how many days?\n"
            "  14. മരുന്ന് കഴിക്കൂ. (marunnu kazhikkuu.) - Take the "
            "medicine.\n"
            "  15. ദിവസം രണ്ട് നേരം. (divasam ranTu neeram.) - Twice a day.\n"
            "  16. ഭക്ഷണത്തിന് ശേഷം. (bhakshanattinu sheesh am.) - After "
            "food.\n"
            "  17. വെള്ളം ധാരാളം കുടിക്കുക. (velLlam dhaaraallam "
            "kutikkuka.) - Drink plenty of water.\n"
            "  18. വിശ്രമം ആവശ്യമാണ്. (vishramam aavashyamaanu.) - Rest is "
            "needed.\n"
            "  19. ഫാർമസിയിൽ നിന്ന് മരുന്ന് വാങ്ങൂ. (faarmasiyil ninnu "
            "marunnu vaanguu.) - Buy medicine from the pharmacy.\n"
            "  20. ഇപ്പോൾ സുഖമുണ്ട്. (ippoolL sukhamunTu.) - (I) feel "
            "better now."
        ),
        "how_it_works": (
            "Symptom sentences use the dative experiencer: എനിക്ക് "
            "പനിയുണ്ട് (to me fever-is) - the sick person is the "
            "recipient, not the subject. Pain verbs attach to the part: "
            "തല വേദനിക്കുന്നു (head pains). Doctor questions are short: "
            "എവിടെ വേദനിക്കുന്നു? എത്ര ദിവസമായി? Prescriptions run on "
            "the imperative -ൂ (കഴിക്കൂ, വാങ്ങൂ) and time phrases "
            "(ദിവസം രണ്ട് നേരം, ഭക്ഷണത്തിന് ശേഷം). Body parts pair "
            "simply: തല head, കണ്ണ് eye, പല്ല് tooth, തൊണ്ട throat, "
            "വയറ് stomach, കാല് leg, കൈ hand, ഹൃദയം heart. The pharmacy "
            "is ഫാർമസി; the prescription is കുറിപ്പടി."
        ),
        "key_points": [
            "Dative experiencer: എനിക്ക് പനിയുണ്ട് (to me there is fever).",
            "Pain pattern: body-part + വേദനിക്കുന്നു.",
            "Doctor questions: എവിടെ വേദനിക്കുന്നു? എത്ര ദിവസമായി?",
            "Dosage phrases: ദിവസം രണ്ട് നേരം; ഭക്ഷണത്തിന് ശേഷം.",
            "20 sentences: body, symptoms, doctor, pharmacy.",
        ],
        "requirements": [
            "Read the grammar record for the dative case.",
            "Learn the eight body parts by pointing and naming.",
        ],
        "standards": [
            "Forms follow standard Malayalam (Asher & Kumari 1997).",
            "Practice sentences are constructed by the archive for teaching; not medical advice.",
        ],
        "citations": [CIT_ASHER],
        "must_contain": ["പനിയുണ്ട്", "വേദനിക്കുന്നു", "ഡോക്ടറെ", "മരുന്ന്", "ഫാർമസി"],
        "sig_lens": (
            "Through the Signature lens the body is a sworn temple: every "
            "part named, every ache spoken plainly, every healing a seal "
            "of care."
        ),
        "drill": {
            "sentences": 20,
            "body_parts": ["തല", "കണ്ണ്", "പല്ല്", "തൊണ്ട", "വയറ്",
                           "കാല്", "കൈ", "ഹൃദയം"],
            "pain_verb": "വേദനിക്കുന്നു",
            "experiencer": "എനിക്ക്",
        },
    },
    {
        "key": "emotions",
        "name": "Malayalam Emotions and Feelings Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 16,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences on happiness, sadness, anger, fear, love, "
            "and surprise - each with romanization and English. \n\n"
            "  1. ഞാൻ വളരെ സന്തോഷവാനാണ്. (njaan valare santoshhavaanaan u.) "
            "- I am very happy.\n"
            "  2. ഇന്ന് എന്റെ മനസ്സ് തെളിഞ്ഞിരിക്കുന്നു. (innu enTe manassu "
            "telinyririkkunnu.) - My mind is clear today.\n"
            "  3. അവൾ ചിരിച്ചുകൊണ്ടിരിക്കുന്നു. (aval chirichchukontirikkunnu.) "
            "- She keeps laughing.\n"
            "  4. വാർത്ത കേട്ട് ഞാൻ സന്തോഷിച്ചു. (vaartta keettu njaan "
            "santoshhichchu.) - I rejoiced hearing the news.\n"
            "  5. അവൻ ദുഃഖിതനാണ്. (avan dukkhitanaan u.) - He is sad.\n"
            "  6. കണ്ണീർ വരുന്നു. (kanniir varunnu.) - Tears are coming.\n"
            "  7. എന്തിനാണ് കരയുന്നത്? (entaanaa karayunnatu?) - Why are "
            "you crying?\n"
            "  8. വിഷമിക്കേണ്ട. (vishamikkeenta.) - Don't worry.\n"
            "  9. അവന് ദേഷ്യം വന്നു. (avanu deshyam vannu.) - He became "
            "angry.\n"
            "  10. ശാന്തമാകൂ. (shaantamaakuu.) - Calm down.\n"
            "  11. ക്ഷമിക്കൂ, ഞാൻ തെറ്റിദ്ധരിച്ചു. (kshamikkuu, njaan "
            "tettiddharichchu.) - Forgive me, I misunderstood.\n"
            "  12. എനിക്ക് പേടിയുണ്ട്. (enikku peetiyunTu.) - I am afraid.\n"
            "  13. ഇരുട്ടിനെ പേടിക്കേണ്ട. (iruttine peetikkeenta.) - Don't "
            "fear the dark.\n"
            "  14. ധൈര്യമായിരിക്കുക. (dhairyamaayirikku ka.) - Be brave.\n"
            "  15. ഞാൻ നിന്നെ സ്നേഹിക്കുന്നു. (njaan ninne sneehikkunnu.) - "
            "I love you.\n"
            "  16. സ്നേഹം ഏറ്റവും വലിയ ശക്തിയാണ്. (sneham eettavum valiya "
            "shaktiyaanu.) - Love is the greatest strength.\n"
            "  17. അവൾ അത്ഭുതപ്പെട്ടു. (aval atbhutappettu.) - She was "
            "surprised.\n"
            "  18. എന്തൊരു അത്ഭുതം! (entoru atbhutam!) - What a surprise!\n"
            "  19. എനിക്ക് അഭിമാനം തോന്നുന്നു. (enikku abhimaanam "
            "toonunnu.) - I feel proud.\n"
            "  20. മനസ്സ് ശാന്തമാക്കുക. (manassu shaantamaakkuka.) - Calm "
            "the mind."
        ),
        "how_it_works": (
            "Emotion sentences use the dative experiencer like health "
            "sentences: എനിക്ക് പേടിയുണ്ട് (to me fear-is), എനിക്ക് "
            "അഭിമാനം തോന്നുന്നു (to me pride feels). Anger 'comes': "
            "ദേഷ്യം വന്നു. Comfort imperatives are gentle: വിഷമിക്കേണ്ട "
            "(don't worry), ശാന്തമാകൂ (calm down). Love uses സ്നേഹം (deep "
            "affection) versus ഇഷ്ടം (liking): ഞാൻ നിന്നെ സ്നേഹിക്കുന്നു "
            "is the full vow. Surprise exclaims with എന്തൊരു: എന്തൊരു "
            "അത്ഭുതം! Gender shows in സന്തോഷവാൻ (happy man) versus "
            "സന്തോഷവതി (happy woman) - one of the few places adjectives "
            "mark gender."
        ),
        "key_points": [
            "Dative experiencer for feelings: എനിക്ക് പേടിയുണ്ട്.",
            "Anger 'comes': ദേഷ്യം വന്നു.",
            "സ്നേഹം (deep love) vs ഇഷ്ടം (liking).",
            "Comfort forms: വിഷമിക്കേണ്ട, ശാന്തമാകൂ.",
            "20 sentences across six emotions.",
        ],
        "requirements": [
            "Read the health record for the dative-experiencer pattern.",
            "Express three feelings about your own day in Malayalam.",
        ],
        "standards": [
            "Forms follow standard Malayalam (Asher & Kumari 1997).",
            "Practice sentences are constructed by the archive for teaching.",
        ],
        "citations": [CIT_ASHER],
        "must_contain": ["സന്തോഷവാനാണ്", "ദേഷ്യം വന്നു", "സ്നേഹിക്കുന്നു", "വിഷമിക്കേണ്ട", "അത്ഭുതം"],
        "sig_lens": (
            "Through the Signature lens feelings are sworn weather of the "
            "heart: joy, grief, anger, fear, love, wonder - each named "
            "plainly, each sealed with honesty."
        ),
        "drill": {
            "sentences": 20,
            "emotions": ["സന്തോഷം", "ദുഃഖം", "ദേഷ്യം", "പേടി",
                         "സ്നേഹം", "അത്ഭുതം"],
            "love_verb": "സ്നേഹിക്കുന്നു",
            "comfort": ["വിഷമിക്കേണ്ട", "ശാന്തമാകൂ"],
        },
    },
    {
        "key": "nature",
        "name": "Malayalam Nature and Weather Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 17,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences on animals, plants, seasons, and weather "
            "talk - each with romanization and English. \n\n"
            "  1. ആന കാട്ടിൽ വസിക്കുന്നു. (aana kaattil vasikkunnu.) - The "
            "elephant lives in the forest.\n"
            "  2. കടുവ ശക്തമായ മൃഗമാണ്. (katuva shaktamaaya mrgamaan u.) - "
            "The tiger is a strong animal.\n"
            "  3. മയിൽ നൃത്തം ചെയ്യുന്നു. (mayil nruttam cheyyunnu.) - The "
            "peacock dances.\n"
            "  4. കിളി പാടുന്നു. (kilLi paatunnu.) - The bird sings.\n"
            "  5. പശു പാൽ തരുന്നു. (pashu paal tarunnu.) - The cow gives "
            "milk.\n"
            "  6. തേങ്ങാ മരത്തിൽ നിന്ന് വീണു. (teengaa marattil ninnu "
            "viinu.) - The coconut fell from the tree.\n"
            "  7. മാവിൽ മാങ്ങയുണ്ട്. (maavil maangayunTu.) - There are "
            "mangoes on the mango tree.\n"
            "  8. വാഴ വേഗത്തിൽ വളരുന്നു. (vaazha veegattil valarunnu.) - "
            "The banana plant grows fast.\n"
            "  9. പൂക്കൾ വിരിഞ്ഞു. (puukkal virinju.) - The flowers "
            "bloomed.\n"
            "  10. പുഴയിൽ വെള്ളമുണ്ട്. (puzhayil velLlamunTu.) - There is "
            "water in the river.\n"
            "  11. കടൽ ആഴമുള്ളതാണ്. (katal aazhamulLataan u.) - The sea is "
            "deep.\n"
            "  12. മലമുകളിൽ മഞ്ഞുണ്ട്. (malamukalil manj unTu.) - There is "
            "mist on the mountain top.\n"
            "  13. ഇന്ന് കാലാവസ്ഥ നല്ലതാണ്. (innu kaalaavasta nallataan u.) "
            "- The weather is good today.\n"
            "  14. മഴ പെയ്യുമെന്ന് തോന്നുന്നു. (mazha peyyumen nu "
            "toonunnu.) - It looks like it will rain.\n"
            "  15. വെയിൽ ശക്തമാണ്. (veyil shaktamaanu.) - The sunshine is "
            "strong.\n"
            "  16. കാറ്റ് വീശുന്നു. (kaattu viishunnu.) - The wind blows.\n"
            "  17. മഴക്കാലത്ത് കുട എടുക്കൂ. (mazhakkaalattu kuta "
            "etukkuu.) - Take an umbrella in the monsoon.\n"
            "  18. വേനൽക്കാലത്ത് ചൂടാണ്. (veenalkaalattu chuutaan u.) - It "
            "is hot in summer.\n"
            "  19. പ്രകൃതിയെ സംരക്ഷിക്കുക. (prakrtiye samrakshikkuka.) - "
            "Protect nature.\n"
            "  20. നാളെ മഴയ്ക്ക് സാധ്യതയുണ്ട്. (naalLe mazhaykku "
            "saadhyatayunTu.) - There is a chance of rain tomorrow."
        ),
        "how_it_works": (
            "Nature sentences name Kerala's living world: ആന (elephant), "
            "കടുവ (tiger), മയിൽ (peacock), തേങ്ങ് (coconut), മാവ് (mango "
            "tree). Weather talk uses the -കാലത്ത് (in the season) frame: "
            "മഴക്കാലത്ത്, വേനൽക്കാലത്ത്. Predictions use -ഉം with "
            "തോന്നുന്നു (it seems): മഴ പെയ്യുമെന്ന് തോന്നുന്നു. The "
            "existence pattern from the home record returns: പുഴയിൽ "
            "വെള്ളമുണ്ട്, മലമുകളിൽ മഞ്ഞുണ്ട്. Animal sounds and motions "
            "take their own verbs: നൃത്തം ചെയ്യുന്നു (dances), പാടുന്നു "
            "(sings), വീശുന്നു (blows, of wind)."
        ),
        "key_points": [
            "Kerala's nature words: ആന, കടുവ, മയിൽ, തേങ്ങ്, മാവ്.",
            "Season frame: -കാലത്ത് (മഴക്കാലത്ത്, വേനൽക്കാലത്ത്).",
            "Weather prediction: -ഉം + തോന്നുന്നു.",
            "Existence pattern: പുഴയിൽ വെള്ളമുണ്ട്.",
            "20 sentences: animals, plants, seasons, weather.",
        ],
        "requirements": [
            "Read the home record for the ഉണ്ട് existence pattern.",
            "Describe today's weather in three Malayalam sentences.",
        ],
        "standards": [
            "Forms follow standard Malayalam (Asher & Kumari 1997).",
            "Practice sentences are constructed by the archive for teaching.",
        ],
        "citations": [CIT_ASHER],
        "must_contain": ["മഴക്കാലത്ത്", "പെയ്യുമെന്ന്", "മയിൽ", "തേങ്ങാ", "പ്രകൃതി"],
        "sig_lens": (
            "Through the Signature lens nature is a sworn garden: every "
            "creature named, every season sealed in its turn, every "
            "raincloud a covenant of return."
        ),
        "drill": {
            "sentences": 20,
            "animals": ["ആന", "കടുവ", "മയിൽ", "കിളി", "പശു"],
            "plants": ["തേങ്ങ്", "മാവ്", "വാഴ"],
            "seasons": ["വേനൽക്കാലം", "മഴക്കാലം", "ശീതകാലം"],
            "prediction": "തോന്നുന്നു",
        },
    },
    {
        "key": "shopping",
        "name": "Malayalam Shopping and Money Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 18,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences on the market, prices, bargaining, and "
            "paying - each with romanization and English. \n\n"
            "  1. കട എപ്പോൾ തുറക്കും? (kata eppoolL turakkum?) - When does "
            "the shop open?\n"
            "  2. ഇതിന്റെ വില എത്ര? (itinTe vila etra?) - How much does "
            "this cost?\n"
            "  3. ഒരു കിലോ അരി തരൂ. (oru kiloo ari taruu.) - Give one kilo "
            "of rice.\n"
            "  4. വില കുറയ്ക്കാമോ? (vila kuraykkaamoo?) - Can you reduce the "
            "price?\n"
            "  5. ഇത് വളരെ കൂടുതലാണ്. (itu valare kuututalaanu.) - This is "
            "too much.\n"
            "  6. കുറച്ച് കുറയ്ക്കൂ. (kurachchu kuraykkuu.) - Reduce it a "
            "little.\n"
            "  7. ശരി, വാങ്ങാം. (shari, vaangaam.) - OK, I'll buy it.\n"
            "  8. പണം കൊടുക്കൂ. (panNam kotukkuu.) - Pay the money.\n"
            "  9. ബാക്കി തരൂ. (baakki taruu.) - Give the change.\n"
            "  10. കാർഡ് എടുക്കുമോ? (kaardu etukkumoo?) - Do you take "
            "card?\n"
            "  11. ക്യാഷ് മാത്രം. (kyaashu maatram.) - Cash only.\n"
            "  12. ബില്ല് തരൂ. (billu taruu.) - Give the bill.\n"
            "  13. ഇത് പുതിയതാണോ? (itu putiyataanoo?) - Is this new?\n"
            "  14. വേറെ നിറമുണ്ടോ? (veere niramunToo?) - Is there another "
            "color?\n"
            "  15. വലിയ സൈസ് ഉണ്ടോ? (valiya sayzu unToo?) - Is there a "
            "large size?\n"
            "  16. ഇത് ധരിച്ചു നോക്കാം. (itu dharichchu nookkaam.) - (I) "
            "can try this on.\n"
            "  17. നന്നായിരിക്കുന്നു; എടുക്കാം. (nannaayirikkunnu; "
            "etukkaam.) - It looks good; I'll take it.\n"
            "  18. പച്ചക്കറി ചന്ത എവിടെ? (pachakkari chanta evite?) - Where "
            "is the vegetable market?\n"
            "  19. പഴങ്ങൾ ഫ്രഷാണോ? (pazhangalL fresh aanoo?) - Are the "
            "fruits fresh?\n"
            "  20. നാളെ വീണ്ടും വരാം. (naalLe viinTum varaam.) - (I) will "
            "come again tomorrow."
        ),
        "how_it_works": (
            "Market Malayalam runs on three questions: എത്ര (how much), "
            "ഉണ്ടോ (is there), കുറയ്ക്കാമോ (can you reduce). Bargaining is "
            "polite and formulaic: വില കുറയ്ക്കാമോ? ... കുറച്ച് കുറയ്ക്കൂ "
            "... ശരി, വാങ്ങാം. Payment closes with പണം കൊടുക്കൂ and "
            "ബാക്കി തരൂ. The -ആം suggestion form (വാങ്ങാം, നോക്കാം, "
            "വരാം) lets the buyer propose without commanding. Loans - "
            "കാർഡ്, ക്യാഷ്, സൈസ് - slot into Malayalam frames with "
            "Malayalam endings. Measures use കിലോ, ലിറ്റർ, മീറ്റർ with "
            "the genitive: ഒരു കിലോ അരി (one kilo of rice)."
        ),
        "key_points": [
            "Market questions: എത്ര, ഉണ്ടോ, കുറയ്ക്കാമോ.",
            "Bargaining formula: ask, counter, ശരി വാങ്ങാം.",
            "Suggestion -ആം: വാങ്ങാം, നോക്കാം, വരാം.",
            "Measures: കിലോ, ലിറ്റർ with genitive (ഒരു കിലോ അരി).",
            "20 sentences: market, prices, bargaining, paying.",
        ],
        "requirements": [
            "Read the numbers record for prices and measures.",
            "Role-play a market bargain in Malayalam.",
        ],
        "standards": [
            "Forms follow standard Malayalam (Asher & Kumari 1997).",
            "Practice sentences are constructed by the archive for teaching.",
        ],
        "citations": [CIT_ASHER],
        "must_contain": ["വില", "കുറയ്ക്കാമോ", "ബാക്കി", "വാങ്ങാം", "ചന്ത"],
        "sig_lens": (
            "Through the Signature lens the market is a sworn exchange: "
            "every price a vow of fairness, every bargain a sealed "
            "agreement, every coin a mark of trust."
        ),
        "drill": {
            "sentences": 20,
            "bargain_steps": ["വില കുറയ്ക്കാമോ?", "കുറച്ച് കുറയ്ക്കൂ.",
                              "ശരി, വാങ്ങാം."],
            "suggestion": "ആം",
            "measures": ["കിലോ", "ലിറ്റർ", "മീറ്റർ"],
        },
    },
    {
        "key": "friendship",
        "name": "Malayalam Friendship and Social Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 19,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences on meeting people, invitations, and "
            "celebrations - each with romanization and English. \n\n"
            "  1. നിങ്ങളെ കണ്ടതിൽ സന്തോഷം. (ningale kantatil santoshham.) - "
            "Glad to meet you.\n"
            "  2. എന്റെ സുഹൃത്തിനെ പരിചയപ്പെടൂ. (enTe suhruttine "
            "parichayappetuu.) - Meet my friend.\n"
            "  3. നിങ്ങളുടെ പേരെന്താണ്? (ningalLute peerenta anu?) - What is "
            "your name?\n"
            "  4. എവിടെയാണ് താമസം? (eviteyaanu taamasam?) - Where do you "
            "live?\n"
            "  5. എന്ത് ജോലിയാണ് ചെയ്യുന്നത്? (entu jooliyaanu "
            "cheyyunnatu?) - What work do you do?\n"
            "  6. നമുക്ക് സുഹൃത്തുക്കളാകാം. (namukku suhruttukkalaakaam.) - "
            "Let's be friends.\n"
            "  7. വീട്ടിലേക്ക് വരൂ. (viittilekku varuu.) - Come home.\n"
            "  8. ചായ കുടിക്കാമോ? (chaaya kutikkaamoo?) - Shall we have "
            "tea?\n"
            "  9. നാളെ കാണാമോ? (naalLe kaanaamoo?) - Shall we meet "
            "tomorrow?\n"
            "  10. പിറന്നാൾ ആശംസകൾ! (pirannaaLL aashamsakalL!) - Happy "
            "birthday!\n"
            "  11. വിവാഹത്തിന് ക്ഷണിക്കുന്നു. (vivaahattinu kshanikkunnu.) - "
            "(I) invite you to the wedding.\n"
            "  12. ഓണം ആശംസകൾ! (oonam aashamsakalL!) - Happy Onam!\n"
            "  13. വിഷു ആശംസകൾ! (vishu aashamsakalL!) - Happy Vishu!\n"
            "  14. സദ്യ കഴിച്ചോ? (sadya kazhichchoo?) - Did you have the "
            "feast?\n"
            "  15. ഒരുമിച്ച് സിനിമ കാണാം. (orumichchu sinima kaanaam.) - "
            "Let's watch a film together.\n"
            "  16. ഫോൺ നമ്പർ തരൂ. (phoonu nampar taruu.) - Give your phone "
            "number.\n"
            "  17. ബന്ധം പുലർത്താം. (bandham pularttaam.) - Let's stay in "
            "touch.\n"
            "  18. സഹായത്തിന് നന്ദി. (sahaayattinu nanni.) - Thanks for the "
            "help.\n"
            "  19. ക്ഷമിക്കണം, വൈകി. (kshamikkanam, vayki.) - Sorry I'm "
            "late.\n"
            "  20. എന്നും സുഹൃത്തുക്കളായിരിക്കും. (ennum "
            "suhruttukkalaayirikkum.) - (We) will always be friends."
        ),
        "how_it_works": (
            "Social Malayalam opens with നിങ്ങളെ കണ്ടതിൽ സന്തോഷം and "
            "builds with the -ആം invitation form: കാണാം, ആകാം, പുലർത്താം "
            "- proposals, never orders. Introductions follow the "
            "name-place-work triple: പേര്, താമസം, ജോലി. Festival "
            "greetings name the feast: ഓണം (the harvest festival), വിഷു "
            "(new year), with സദ്യ the great feast-meal. Thanks and "
            "apology close the circle: സഹായത്തിന് നന്ദി, ക്ഷമിക്കണം വൈകി. "
            "The inclusive നമുക്ക് (for us, including you) makes every "
            "invitation warm: നമുക്ക് സുഹൃത്തുക്കളാകാം."
        ),
        "key_points": [
            "Invitation form -ആം: കാണാം, ആകാം, പുലർത്താം.",
            "Introduction triple: പേര്, താമസം, ജോലി.",
            "Festivals: ഓണം, വിഷു; the feast is സദ്യ.",
            "Inclusive നമുക്ക് warms every invitation.",
            "20 sentences: meeting, invitations, celebrations.",
        ],
        "requirements": [
            "Read the greetings record first.",
            "Introduce yourself fully in Malayalam.",
        ],
        "standards": [
            "Forms follow standard Malayalam (Asher & Kumari 1997).",
            "Practice sentences are constructed by the archive for teaching.",
        ],
        "citations": [CIT_ASHER],
        "must_contain": ["പരിചയപ്പെടൂ", "ഓണം", "വിഷു", "സദ്യ", "നമുക്ക്"],
        "sig_lens": (
            "Through the Signature lens friendship is a sworn bond: every "
            "introduction a vow of welcome, every festival a seal of "
            "shared joy."
        ),
        "drill": {
            "sentences": 20,
            "invitation": "ആം",
            "festivals": ["ഓണം", "വിഷു"],
            "intro_triple": ["പേര്", "താമസം", "ജോലി"],
        },
    },
    {
        "key": "technology",
        "name": "Malayalam Technology and Communication Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 20,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences on the phone, internet, computer, and "
            "messaging - each with romanization and English. \n\n"
            "  1. ഫോൺ എടുക്കൂ. (phoonu etukkuu.) - Answer the phone.\n"
            "  2. ആരാണ് വിളിക്കുന്നത്? (aaraan u vilikkunnatu?) - Who is "
            "calling?\n"
            "  3. ഞാൻ പിന്നെ വിളിക്കാം. (njaan pinne vilikkaam.) - I will "
            "call later.\n"
            "  4. നെറ്റ്‌വർക്ക് ഇല്ല. (netvarkku illa.) - There is no "
            "network.\n"
            "  5. ചാർജ് തീർന്നു. (chaarju tiirnnu.) - The charge ran out.\n"
            "  6. മെസ്സേജ് അയയ്ക്കൂ. (messeeyju ayaykkuu.) - Send a message.\n"
            "  7. വാട്ട്സ്ആപ്പിൽ അയയ്ക്കാം. (vaattsaappil ayaykkaam.) - "
            "(I) will send it on WhatsApp.\n"
            "  8. ഇമെയിൽ വായിച്ചോ? (imeyil vaayichchoo?) - Did you read the "
            "email?\n"
            "  9. ഇന്റർനെറ്റ് വേഗത കുറവാണ്. (intarnettu veegata "
            "kuravaanu.) - The internet speed is low.\n"
            "  10. വൈഫൈ പാസ്‌വേഡ് തരൂ. (vayfay paasveedu taruu.) - Give "
            "the WiFi password.\n"
            "  11. കമ്പ്യൂട്ടർ ഓണാക്കൂ. (kampyuuttar oonaakkuu.) - Turn on "
            "the computer.\n"
            "  12. ഫയൽ സേവ് ചെയ്യൂ. (fayal seevu cheyyuu.) - Save the "
            "file.\n"
            "  13. പ്രിന്റ് എടുക്കൂ. (printu etukkuu.) - Take a printout.\n"
            "  14. സ്ക്രീൻഷോട്ട് എടുത്തോ? (skriinshootu etuttoo?) - Did you "
            "take a screenshot?\n"
            "  15. ആപ്പ് ഡൗൺലോഡ് ചെയ്യൂ. (aappu daunloodu cheyyuu.) - "
            "Download the app.\n"
            "  16. പാസ്‌വേഡ് മറന്നു. (paasveedu marannu.) - (I) forgot the "
            "password.\n"
            "  17. അക്കൗണ്ട് ഉണ്ടാക്കൂ. (akkauntu unTaakkuu.) - Create an "
            "account.\n"
            "  18. വീഡിയോ കോൾ ചെയ്യാം. (viitiyoo koolL cheyyaam.) - Let's "
            "do a video call.\n"
            "  19. ഓൺലൈനിൽ കാണാം. (oonlayinil kaanaam.) - See you online.\n"
            "  20. ഫോൺ നിശ്ശബ്ദമാക്കൂ. (phoonu nishshabdamaakkuu.) - Put "
            "the phone on silent."
        ),
        "how_it_works": (
            "Technology Malayalam is Malayalam grammar wearing English "
            "loans: ഫോൺ, മെസ്സേജ്, ഇമെയിൽ, കമ്പ്യൂട്ടർ, ആപ്പ് take "
            "Malayalam case endings (വാട്ട്സ്ആപ്പിൽ, ഓൺലൈനിൽ) and "
            "Malayalam verbs (അയയ്ക്കൂ, ഡൗൺലോഡ് ചെയ്യൂ). Commands use "
            "-ൂ: എടുക്കൂ, അയയ്ക്കൂ, ഓണാക്കൂ. Problems state with ഇല്ല or "
            "the past: നെറ്റ്‌വർക്ക് ഇല്ല, ചാർജ് തീർന്നു, പാസ്‌വേഡ് "
            "മറന്നു. Plans use -ആം: വിളിക്കാം, അയയ്ക്കാം, ചെയ്യാം. "
            "The pattern is endlessly productive - any new English tech "
            "word drops into a Malayalam frame and works."
        ),
        "key_points": [
            "English loans take Malayalam endings: വാട്ട്സ്ആപ്പിൽ, ഓൺലൈനിൽ.",
            "Tech commands with -ൂ: എടുക്കൂ, അയയ്ക്കൂ.",
            "Problem pattern: noun + ഇല്ല / past verb.",
            "Plan pattern -ആം: വിളിക്കാം, ചെയ്യാം.",
            "20 sentences: phone, internet, computer, messaging.",
        ],
        "requirements": [
            "Read the verb record for -ൂ imperatives.",
            "Send a real message using one of these sentences.",
        ],
        "standards": [
            "Forms follow standard spoken Malayalam usage.",
            "Practice sentences are constructed by the archive for teaching.",
        ],
        "citations": [CIT_ASHER],
        "must_contain": ["വാട്ട്സ്ആപ്പിൽ", "അയയ്ക്കൂ", "നെറ്റ്‌വർക്ക്", "ഡൗൺലോഡ്", "വിളിക്കാം"],
        "sig_lens": (
            "Through the Signature lens technology is a sworn wire: every "
            "message a vow carried, every call a seal across the distance."
        ),
        "drill": {
            "sentences": 20,
            "loans": ["ഫോൺ", "മെസ്സേജ്", "ഇമെയിൽ", "കമ്പ്യൂട്ടർ",
                      "ആപ്പ്"],
            "problem_words": ["ഇല്ല", "തീർന്നു", "മറന്നു"],
        },
    },
    {
        "key": "tenses",
        "name": "Malayalam Verb Tenses in Sentences",
        "group": "Grammar in Action",
        "ladder_rank": 21,
        "ladder_tier": "compounded",
        "description": (
            "Present, past, and future - five or more translated sentences "
            "per tense, plus aspect shades. \n\n"
            "Present (-unnu / -aanu):\n"
            "  ഞാൻ പഠിക്കുന്നു. (njaan patThikkunnu.) - I study.\n"
            "  അവൾ പാടുന്നു. (aval paatunnu.) - She sings.\n"
            "  മഴ പെയ്യുന്നു. (mazha peyyunnu.) - It is raining.\n"
            "  ഞാൻ സന്തോഷവാനാണ്. (njaan santoshhavaanaan u.) - I am happy.\n"
            "  അവർ വരുന്നുണ്ട്. (avar varunnunTu.) - They are coming "
            "(emphatic).\n"
            "  ഞാൻ എഴുതിക്കൊണ്ടിരിക്കുന്നു. (njaan ezhutikkontirikkunnu.) - "
            "I am in the middle of writing.\n\n"
            "Past (-i / -tu / -nju):\n"
            "  ഞാൻ പോയി. (njaan pooyi.) - I went.\n"
            "  അവൻ വന്നു. (avan vannu.) - He came.\n"
            "  ഞാൻ കഴിച്ചു. (njaan kazhichchu.) - I ate.\n"
            "  അവൾ പാടി. (aval paati.) - She sang.\n"
            "  മഴ പെയ്തു. (mazha peytu.) - It rained.\n"
            "  ഞാൻ കണ്ടിട്ടുണ്ട്. (njaan kantittunTu.) - I have seen "
            "(perfect).\n\n"
            "Future (-um):\n"
            "  ഞാൻ പോകും. (njaan pookum.) - I will go.\n"
            "  അവൻ വരും. (avan varum.) - He will come.\n"
            "  നാളെ മഴ പെയ്യും. (naalLe mazha peyyum.) - It will rain "
            "tomorrow.\n"
            "  ഞാൻ പഠിക്കും. (njaan patThikkum.) - I will study.\n"
            "  നമ്മൾ ജയിക്കും. (nammalL jayikkum.) - We will win.\n"
            "  അവൾ പാടുമോ? (aval paatumoo?) - Will she sing?\n\n"
            "Aspect shades: -konTirikkunnu marks ongoing action "
            "(എഴുതിക്കൊണ്ടിരിക്കുന്നു, is writing right now); -ittunTu "
            "marks the perfect (കണ്ടിട്ടുണ്ട്, have seen); -aarunTu marks "
            "habit (പോകാറുണ്ട്, usually goes)."
        ),
        "how_it_works": (
            "The tense machine: strip -uka, add the ending. പോകുക -> "
            "പോക് + unnu/i/um. Past stems reshape - പോക് becomes പോയി, "
            "വരിക becomes വന്നു, കഴിക്കുക becomes കഴിച്ചു - the "
            "irregulars are few and learned as units. Negation rides the "
            "tense: പോകുന്നില്ല (does not go), പോയില്ല (did not go), "
            "പോകില്ല (will not go). The emphatic -unTu (വരുന്നുണ്ട്) "
            "insists the action is really happening. Aspect auxiliaries "
            "stack after the main verb: -konTirikkunnu (ongoing), "
            "-ittunTu (perfect), -aarunTu (habitual). Master the three "
            "endings and the auxiliaries, and time bends to your will."
        ),
        "key_points": [
            "Present -unnu, past -i/-tu, future -um on the verb stem.",
            "Past stems reshape: പോയി, വന്നു, കഴിച്ചു.",
            "Negation: -unnilla, -illa, -illa per tense.",
            "Emphatic -unTu: വരുന്നുണ്ട് (really coming).",
            "Aspects: -konTirikkunnu ongoing, -ittunTu perfect, -aarunTu habitual.",
        ],
        "requirements": [
            "Read the verb record for stems.",
            "Conjugate പോകുക, വരിക, കഴിക്കുക in all tenses and negations.",
        ],
        "standards": [
            "Tense forms follow Asher & Kumari 1997 and Andronov 1996.",
            "Practice sentences are constructed by the archive for teaching.",
        ],
        "citations": [CIT_ASHER, CIT_ANDRONOV],
        "must_contain": ["-unnu", "പോയി", "-um", "കണ്ടിട്ടുണ്ട്", "konTirikkunnu"],
        "sig_lens": (
            "Through the Signature lens tense is a sworn timeline: what "
            "is, what was, what will be - each ending a seal on its "
            "moment."
        ),
        "drill": {
            "present": "unnu", "future": "um",
            "past_forms": {"പോകുക": "പോയി", "വരിക": "വന്നു",
                           "കഴിക്കുക": "കഴിച്ചു", "പാടുക": "പാടി",
                           "പെയ്യുക": "പെയ്തു"},
            "negations": ["പോകുന്നില്ല", "പോയില്ല", "പോകില്ല"],
            "aspects": ["konTirikkunnu", "ittunTu", "aarunTu"],
            "per_tense": 6,
        },
    },
    {
        "key": "qa",
        "name": "Malayalam Questions and Answers",
        "group": "Grammar in Action",
        "ladder_rank": 22,
        "ladder_tier": "compounded",
        "description": (
            "Twenty question-and-answer pairs covering who, what, where, "
            "when, why, and how - each with romanization and English. \n\n"
            "  1. Q: നിന്റെ പേരെന്താണ്? (ninTe peerenta anu?) - What is "
            "your name? A: എന്റെ പേര് രവിയാണ്. - My name is Ravi.\n"
            "  2. Q: നീ എവിടെയാണ് താമസിക്കുന്നത്? - Where do you live? A: "
            "ഞാൻ കൊച്ചിയിൽ താമസിക്കുന്നു. - I live in Kochi.\n"
            "  3. Q: ആര് വന്നു? - Who came? A: എന്റെ സുഹൃത്ത് വന്നു. - My "
            "friend came.\n"
            "  4. Q: എന്ത് വേണം? - What do you want? A: വെള്ളം വേണം. - "
            "(I) want water.\n"
            "  5. Q: എപ്പോൾ പോകും? - When will you go? A: നാളെ രാവിലെ "
            "പോകും. - (I) will go tomorrow morning.\n"
            "  6. Q: എന്തുകൊണ്ട് വൈകി? - Why are you late? A: ബസ് വൈകി. - "
            "The bus was late.\n"
            "  7. Q: എങ്ങനെ പോകും? - How will you go? A: ബസിൽ പോകും. - "
            "(I) will go by bus.\n"
            "  8. Q: ഏത് പുസ്തകമാണ് നല്ലത്? - Which book is good? A: ഈ "
            "പുസ്തകം നല്ലതാണ്. - This book is good.\n"
            "  9. Q: എത്ര രൂപയായി? - How much is it? A: അമ്പത് രൂപ. - "
            "Fifty rupees.\n"
            "  10. Q: നീ വരുന്നോ? - Are you coming? A: അതെ, വരുന്നു. - "
            "Yes, (I) am coming.\n"
            "  11. Q: ഭക്ഷണം കഴിച്ചോ? - Did you eat? A: ഇല്ല, ഇതുവരെ "
            "ഇല്ല. - No, not yet.\n"
            "  12. Q: മലയാളം അറിയാമോ? - Do you know Malayalam? A: കുറച്ച് "
            "അറിയാം. - (I) know a little.\n"
            "  13. Q: ഇത് എന്താണ്? - What is this? A: ഇത് പൂവാണ്. - This "
            "is a flower.\n"
            "  14. Q: അവൻ എവിടെ? - Where is he? A: അവൻ സ്കൂളിലാണ്. - He "
            "is at school.\n"
            "  15. Q: എത്ര മണിയായി? - What time is it? A: മൂന്ന് മണി. - "
            "Three o'clock.\n"
            "  16. Q: നാളെ മഴ പെയ്യുമോ? - Will it rain tomorrow? A: "
            "പെയ്യുമെന്ന് തോന്നുന്നു. - It looks like it will.\n"
            "  17. Q: സഹായിക്കാമോ? - Can you help? A: തീർച്ചയായും. - "
            "Certainly.\n"
            "  18. Q: എത്ര ദൂരമുണ്ട്? - How far is it? A: രണ്ട് "
            "കിലോമീറ്റർ. - Two kilometers.\n"
            "  19. Q: ആരോട് പറയണം? - Whom should I tell? A: അധ്യാപകനോട് "
            "പറയൂ. - Tell the teacher.\n"
            "  20. Q: എന്താണ് പ്രശ്നം? - What is the problem? A: "
            "പ്രശ്നമൊന്നുമില്ല. - No problem at all."
        ),
        "how_it_works": (
            "Questions need no word-order change: take the statement, add "
            "-ഓ to the verb (വരുന്നോ, പെയ്യുമോ), or open with a question "
            "word (ആര്, എന്ത്, എവിടെ, എപ്പോൾ, എന്തുകൊണ്ട്, എങ്ങനെ, ഏത്, "
            "എത്ര). Answers mirror the question's verb: Q എപ്പോൾ പോകും? "
            "A നാളെ പോകും. അതെ/ഇല്ല answer yes-no questions; ഇതുവരെ "
            "ഇല്ല (not yet) softens a no. അറിയാമോ (do you know) takes "
            "the dative knower: എനിക്ക് അറിയാം. The pair pattern is "
            "everything - learn each question with its answer as one "
            "unit."
        ),
        "key_points": [
            "Yes-no questions: verb + -ഓ (വരുന്നോ, പെയ്യുമോ).",
            "Question words: ആര് എന്ത് എവിടെ എപ്പോൾ എന്തുകൊണ്ട് എങ്ങനെ ഏത് എത്ര.",
            "No word-order change for questions.",
            "Answers mirror the question's verb and tense.",
            "20 Q/A pairs across who/what/where/when/why/how.",
        ],
        "requirements": [
            "Read the pronoun record for the interrogatives.",
            "Ask and answer all 20 pairs aloud with a partner.",
        ],
        "standards": [
            "Forms follow standard Malayalam (Asher & Kumari 1997).",
            "Practice pairs are constructed by the archive for teaching.",
        ],
        "citations": [CIT_ASHER],
        "must_contain": ["വരുന്നോ", "എന്തുകൊണ്ട്", "അറിയാമോ", "ഇതുവരെ ഇല്ല", "തീർച്ചയായും"],
        "sig_lens": (
            "Through the Signature lens every question is a sworn "
            "knocking: who, what, where, when, why, how - each answer a "
            "seal of truth given back."
        ),
        "drill": {
            "pairs": 20,
            "question_particle": "ഓ",
            "question_words": ["ആര്", "എന്ത്", "ഏത്", "എവിടെ",
                               "എപ്പോൾ", "എന്തുകൊണ്ട്", "എങ്ങനെ",
                               "എത്ര"],
            "yes": "അതെ", "no": "ഇല്ല",
        },
    },
    {
        "key": "commands",
        "name": "Malayalam Commands and Requests",
        "group": "Grammar in Action",
        "ladder_rank": 23,
        "ladder_tier": "compounded",
        "description": (
            "Twenty imperatives and polite requests - formal versus "
            "informal - each with romanization and English. \n\n"
            "Informal (to friends, children, juniors):\n"
            "  1. വാ. (vaa.) - Come.\n"
            "  2. പോ. (poo.) - Go.\n"
            "  3. ഇരിക്ക്. (irikku.) - Sit.\n"
            "  4. പറ. (para.) - Say (it).\n"
            "  5. നോക്ക്. (nookku.) - Look.\n\n"
            "Polite everyday (-ൂ):\n"
            "  6. വരൂ. (varuu.) - Please come.\n"
            "  7. ഇരിക്കൂ. (irikkuu.) - Please sit.\n"
            "  8. പറയൂ. (parayuu.) - Please say.\n"
            "  9. തരൂ. (taruu.) - Please give.\n"
            "  10. നോക്കൂ. (nookkuu.) - Please look.\n\n"
            "Formal / respectful (-ാലൂ, -ക്കൂ):\n"
            "  11. വരൂ, ഇരിക്കൂ. - Please come, please sit (respectful).\n"
            "  12. ദയവായി സഹായിക്കൂ. (dayavaayi sahaayikkuu.) - Please "
            "help me.\n"
            "  13. ക്ഷമിക്കണം, ഒന്ന് മാറി നിൽക്കൂ. - Excuse me, please "
            "step aside.\n"
            "  14. അകത്തേക്ക് വരൂ. (akattekku varuu.) - Please come in.\n"
            "  15. ഇവിടെ ഒപ്പിടൂ. (ivite oppituu.) - Please sign here.\n\n"
            "Prohibitions and suggestions:\n"
            "  16. പോകരുത്. (pookarutu.) - Don't go.\n"
            "  17. സംസാരിക്കരുത്. (samsaarikkarutu.) - Don't talk.\n"
            "  18. വിഷമിക്കേണ്ട. (vishamikkeenta.) - Don't worry.\n"
            "  19. നമുക്ക് പോകാം. (namukku pookaam.) - Let's go.\n"
            "  20. നമുക്ക് തുടങ്ങാം. (namukku tutangaam.) - Let's begin."
        ),
        "how_it_works": (
            "The command ladder has four rungs: bare stem (വാ, പോ) for "
            "intimates; -ൂ (വരൂ, തരൂ) for polite everyday requests; "
            "ദയവായി + -ൂ for formal deference; -രുത് for prohibition "
            "(പോകരുത്, don't go) and -ഏണ്ട for gentle dissuasion "
            "(വിഷമിക്കേണ്ട, don't worry). The -ആം form (പോകാം, തുടങ്ങാം) "
            "proposes joint action - 'let's' - and belongs with നമുക്ക്. "
            "Negative commands never use ഇല്ല; they use -രുത്. "
            "Choosing the rung is social grammar: -ൂ to a shopkeeper, "
            "ദയവായി to an elder, bare stem only to close friends and "
            "children."
        ),
        "key_points": [
            "Four rungs: bare stem, -ൂ polite, ദയവായി formal, -രുത് prohibition.",
            "Gentle dissuasion: -ഏണ്ട (വിഷമിക്കേണ്ട).",
            "'Let's' with -ആം + നമുക്ക്: പോകാം.",
            "Negative commands use -രുത്, never ഇല്ല.",
            "20 sentences: formal vs informal commands and requests.",
        ],
        "requirements": [
            "Read the verb record for stems.",
            "Give five polite commands to a friend, five formal to an elder.",
        ],
        "standards": [
            "Forms follow standard Malayalam (Asher & Kumari 1997).",
            "Practice sentences are constructed by the archive for teaching.",
        ],
        "citations": [CIT_ASHER],
        "must_contain": ["വരൂ", "പോകരുത്", "വിഷമിക്കേണ്ട", "പോകാം", "ദയവായി"],
        "sig_lens": (
            "Through the Signature lens commands are sworn directions: "
            "each rung of politeness a seal of respect, each prohibition "
            "a vow of protection."
        ),
        "drill": {
            "sentences": 20,
            "rungs": ["bare stem", "ൂ", "ദയവായി + ൂ", "രുത്"],
            "prohibition": "രുത്", "lets": "ആം",
            "informal": ["വാ", "പോ", "ഇരിക്ക്"],
        },
    },
    {
        "key": "descriptions",
        "name": "Malayalam Descriptions of People and Places",
        "group": "Grammar in Action",
        "ladder_rank": 24,
        "ladder_tier": "advanced",
        "description": (
            "Twenty sentences describing people, places, and things in "
            "detail - each with romanization and English. \n\n"
            "  1. എന്റെ അമ്മ ദയയുള്ളവളാണ്. (enTe amma dayayulLavalaanu.) - "
            "My mother is kind.\n"
            "  2. അച്ഛൻ ഉയരമുള്ള, ശാന്തനായ മനുഷ്യനാണ്. (achchhan "
            "uyaramulLa, shaantanaaya manushyanaanu.) - Father is a tall, "
            "calm man.\n"
            "  3. എന്റെ സുഹൃത്ത് ബുദ്ധിമാനും തമാശക്കാരനുമാണ്. (enTe "
            "suhruttu buddhimaanum tamashakkaranumaanu.) - My friend is "
            "intelligent and funny.\n"
            "  4. കുട്ടിയുടെ കണ്ണുകൾ തിളങ്ങുന്നു. (kuttiyute kannukalL "
            "tilangunnu.) - The child's eyes shine.\n"
            "  5. അവളുടെ മുടി നീളമുള്ളതും കറുത്തതുമാണ്. (avalLute muti "
            "niilamulLatum karuttatuma anu.) - Her hair is long and black.\n"
            "  6. അധ്യാപകൻ ക്ഷമയുള്ളവനാണ്. (adhyaapakan kshamayulLavanaanu.) "
            "- The teacher is patient.\n"
            "  7. മുത്തശ്ശിയുടെ കഥകൾ മനോഹരമാണ്. (muttashshiyute katakalL "
            "manooharamaanu.) - Grandmother's stories are beautiful.\n"
            "  8. കേരളം പച്ചപ്പ് നിറഞ്ഞ നാടാണ്. (keerallam pachappu niranja "
            "naataan u.) - Kerala is a land full of greenery.\n"
            "  9. കൊച്ചി തിരക്കേറിയ നഗരമാണ്. (kochchi tirakkerriya "
            "nagaramaanu.) - Kochi is a busy city.\n"
            "  10. കടൽത്തീരം ശാന്തവും മനോഹരവുമാണ്. (katalttiiram "
            "shaantavum manooharavumaanu.) - The beach is calm and "
            "beautiful.\n"
            "  11. മലമുകളിൽ നിന്നുള്ള കാഴ്ച അത്ഭുതകരമാണ്. (malamukalil "
            "ninnulLa kaazhcha atbhutakaramaanu.) - The view from the "
            "mountaintop is wonderful.\n"
            "  12. പുഴയുടെ വെള്ളം തെളിഞ്ഞതാണ്. (puzhayute velLlam "
            "telinjat aanu.) - The river's water is clear.\n"
            "  13. ഈ വീട് പഴയതും വലുതുമാണ്. (ii viitu pazhayatum "
            "valutumaanu.) - This house is old and big.\n"
            "  14. മുറി വൃത്തിയുള്ളതും വെളിച്ചമുള്ളതുമാണ്. (muri "
            "vruttiyulLatum velichchamulLatumaanu.) - The room is clean and "
            "bright.\n"
            "  15. പൂന്തോട്ടത്തിൽ നിറയെ പൂക്കളുണ്ട്. (puuntoottattil niraye "
            "puukkalunTu.) - The garden is full of flowers.\n"
            "  16. ആന വലിയ, ശക്തമായ മൃഗമാണ്. (aana valiya, shaktamaaya "
            "mrgamaanu.) - The elephant is a big, strong animal.\n"
            "  17. മയിൽ അതിമനോഹരമായ പക്ഷിയാണ്. (mayil atimanooharamaaya "
            "pakshiyaanu.) - The peacock is an extremely beautiful bird.\n"
            "  18. ചായ ചൂടുള്ളതും മധുരമുള്ളതുമാണ്. (chaaya chuutulLatum "
            "madhuramulLatumaanu.) - The tea is hot and sweet.\n"
            "  19. ഇന്നത്തെ കാലാവസ്ഥ തെളിഞ്ഞതാണ്. (innatte kaalaavasta "
            "telinjataan u.) - Today's weather is clear.\n"
            "  20. എന്റെ നാട് എനിക്ക് ഏറ്റവും പ്രിയപ്പെട്ടതാണ്. (enTe naatu "
            "enikku eettavum priyappettataan u.) - My homeland is dearest "
            "to me."
        ),
        "how_it_works": (
            "Descriptions stack adjectives before the noun and join pairs "
            "with -ഉം: വലിയ, ശക്തമായ മൃഗം; ശാന്തവും മനോഹരവും. The -ഉള്ള "
            "adjectives (ദയയുള്ള, ക്ഷമയുള്ള) describe character; -മായ "
            "adjectives (മനോഹരമായ, അത്ഭുതകരമായ) describe quality. "
            "Possession frames ownership of features: അവളുടെ മുടി "
            "(her hair), കുട്ടിയുടെ കണ്ണുകൾ (the child's eyes). "
            "Superlatives use ഏറ്റവും: ഏറ്റവും പ്രിയപ്പെട്ടത് (the "
            "dearest). Place descriptions anchor with -ഇൽ phrases: "
            "മലമുകളിൽ നിന്നുള്ള കാഴ്ച (the view from the mountaintop). "
            "Every description is still SOV underneath the decoration."
        ),
        "key_points": [
            "Adjective stacking before the noun; pairs joined with -ഉം.",
            "-ഉള്ള for character, -മായ for quality.",
            "Possession frames features: അവളുടെ മുടി.",
            "Superlative ഏറ്റവും: ഏറ്റവും പ്രിയപ്പെട്ടത്.",
            "20 detailed descriptive sentences.",
        ],
        "requirements": [
            "Read the adjectives record for -ഉള്ള and -മായ.",
            "Describe one person and one place in five sentences each.",
        ],
        "standards": [
            "Forms follow standard Malayalam (Asher & Kumari 1997).",
            "Practice sentences are constructed by the archive for teaching.",
        ],
        "citations": [CIT_ASHER],
        "must_contain": ["ദയയുള്ളവളാണ്", "കടൽത്തീരം", "ഏറ്റവും", "പൂന്തോട്ടത്തിൽ", "ശാന്തവും"],
        "sig_lens": (
            "Through the Signature lens description is sworn portraiture: "
            "every trait a vow of truth, every landscape a seal of "
            "belonging."
        ),
        "drill": {
            "sentences": 20,
            "pair_joiner": "ഉം", "superlative": "ഏറ്റവും",
            "character_adj": "ഉള്ള", "quality_adj": "മായ",
        },
    },
    {
        "key": "story1",
        "name": "Malayalam Short Story I: A Simple Day",
        "group": "Stories and Idioms",
        "ladder_rank": 25,
        "ladder_tier": "advanced",
        "description": (
            "A ten-sentence simple story in Malayalam - present tense, "
            "everyday words - with line-by-line English translation. "
            "(Archive-constructed teaching story.) \n\n"
            "  1. രവി രാവിലെ നേരത്തെ ഉണരുന്നു. (ravi raavile neertte "
            "unarunnu.) - Ravi wakes up early in the morning.\n"
            "  2. അവൻ മുഖം കഴുകി പല്ല് തേക്കുന്നു. (avan mukham kazhuki "
            "pallu teekkunnu.) - He washes his face and brushes his teeth.\n"
            "  3. അമ്മ അടുക്കളയിൽ പ്രാതൽ ഉണ്ടാക്കുന്നു. (amma atukkalayil "
            "praatal unTaakkunnu.) - Mother makes breakfast in the "
            "kitchen.\n"
            "  4. രവി ഇഡ്ഡലിയും ചായയും കഴിക്കുന്നു. (ravi iddaliyum "
            "chaayayum kazhikkunnu.) - Ravi eats idli and tea.\n"
            "  5. അവൻ ബാഗ് എടുത്ത് സ്കൂളിൽ പോകുന്നു. (avan baagu etuttu "
            "skuulil pookunnu.) - He takes his bag and goes to school.\n"
            "  6. സ്കൂളിൽ സുഹൃത്തുക്കൾ കാത്തിരിക്കുന്നു. (skuulil "
            "suhruttukkal kaattirikkunnu.) - Friends wait at the school.\n"
            "  7. അധ്യാപകൻ പുതിയ പാഠം പഠിപ്പിക്കുന്നു. (adhyaapakan putiya "
            "paattham patThippikkunnu.) - The teacher teaches a new lesson.\n"
            "  8. ഉച്ചയ്ക്ക് എല്ലാവരും ഒരുമിച്ച് ഭക്ഷണം കഴിക്കുന്നു. "
            "(uchchaykku ellaavarum orumichchu bhakshanam kazhikkunnu.) - "
            "At noon everyone eats together.\n"
            "  9. വൈകുന്നേരം രവി വീട്ടിൽ തിരിച്ചെത്തുന്നു. (vaykunneeram "
            "ravi viittil tirichchettunnu.) - In the evening Ravi returns "
            "home.\n"
            "  10. രാത്രി അവൻ നന്ദിയോടെ ഉറങ്ങുന്നു. (raatri avan "
            "nanniyootte urangunnu.) - At night he sleeps gratefully."
        ),
        "how_it_works": (
            "The story is a chain of present-tense SOV sentences, each "
            "reusing words from earlier records: ഉണരുന്നു, കഴിക്കുന്നു, "
            "പോകുന്നു, പഠിപ്പിക്കുന്നു. Time words order the chain: "
            "രാവിലെ, ഉച്ചയ്ക്ക്, വൈകുന്നേരം, രാത്രി. Conjoined actions "
            "use -ഉം (ഇഡ്ഡലിയും ചായയും) and serial verbs (എടുത്ത് ... "
            "പോകുന്നു). Read it straight through, then retell it without "
            "looking: the ladder has taught every word in it."
        ),
        "key_points": [
            "10-sentence story in present tense; line-by-line translation.",
            "Time chain: രാവിലെ, ഉച്ചയ്ക്ക്, വൈകുന്നേരം, രാത്രി.",
            "Conjoined nouns with -ഉം; serial verbs with -ത്ത്.",
            "Every word drawn from earlier ladder records.",
        ],
        "requirements": [
            "Read all vocabulary records first.",
            "Retell the story aloud without looking.",
        ],
        "standards": [
            "Story is constructed by the archive for teaching; grammar follows Asher & Kumari 1997.",
        ],
        "citations": [CIT_ASHER],
        "must_contain": ["രവി", "പ്രാതൽ", "വൈകുന്നേരം", "തിരിച്ചെത്തുന്നു", "നന്ദിയോടെ"],
        "sig_lens": (
            "Through the Signature lens this day is a sworn circle: dawn "
            "to night, each hour a vow kept, each meal a seal of the "
            "ordinary made sacred."
        ),
        "drill": {
            "lines": 10,
            "time_words": ["രാവിലെ", "ഉച്ചയ്ക്ക്", "വൈകുന്നേരം", "രാത്രി"],
            "hero": "രവി",
        },
    },
    {
        "key": "story2",
        "name": "Malayalam Short Story II: The Journey",
        "group": "Stories and Idioms",
        "ladder_rank": 26,
        "ladder_tier": "advanced",
        "description": (
            "A ten-sentence story in the past tense - a journey to the "
            "grandmother's village - with line-by-line English "
            "translation. (Archive-constructed teaching story.) \n\n"
            "  1. കഴിഞ്ഞ വർഷം ഞങ്ങൾ നാട്ടിൽ പോയി. (kazhynya varsham "
            "njangalL naattil pooyi.) - Last year we went to the village.\n"
            "  2. രാവിലെ ആറ് മണിക്ക് ബസ് പുറപ്പെട്ടു. (raavile aaru "
            "manikku basu purappettu.) - The bus left at six in the "
            "morning.\n"
            "  3. വഴിയിൽ പുഴയും പാടങ്ങളും കണ്ടു. (vazhiyil puzhayum "
            "paadangalum kantu.) - On the way (we) saw rivers and fields.\n"
            "  4. ഉച്ചയ്ക്ക് ഞങ്ങൾ ചോറും കറിയും കഴിച്ചു. (uchchaykku "
            "njangalL choorum kariyum kazhichchu.) - At noon we ate rice "
            "and curry.\n"
            "  5. മുത്തശ്ശി വാതിലിനരികിൽ കാത്തിരുന്നു. (muttashshi "
            "vaatilinarikil kaattirunnu.) - Grandmother waited near the "
            "door.\n"
            "  6. അവർ ഞങ്ങളെ സ്നേഹത്തോടെ സ്വീകരിച്ചു. (avar njangale "
            "snehattootte sviikarichchu.) - She welcomed us with love.\n"
            "  7. വൈകുന്നേരം ഞങ്ങൾ പുഴയിൽ കുളിച്ചു. (vaykunneeram njangalL "
            "puzhayil kulichchu.) - In the evening we bathed in the river.\n"
            "  8. രാത്രി മുത്തശ്ശി കഥ പറഞ്ഞു. (raatri muttashshi kata "
            "paranju.) - At night grandmother told a story.\n"
            "  9. കഥ കേട്ട് ഞങ്ങൾ ഉറങ്ങി. (kata keettu njangalL urangi.) - "
            "Hearing the story, we slept.\n"
            "  10. ആ യാത്ര ഞങ്ങൾ ഒരിക്കലും മറക്കില്ല. (aa yaatra njangalL "
            "orikkalum marakkilla.) - We will never forget that journey."
        ),
        "how_it_works": (
            "The past tense carries the whole journey: പോയി, പുറപ്പെട്ടു, "
            "കണ്ടു, കഴിച്ചു, കാത്തിരുന്നു, സ്വീകരിച്ചു, കുളിച്ചു, പറഞ്ഞു, "
            "ഉറങ്ങി - nine past verbs, each reshaped from its stem. "
            "കഴിഞ്ഞ വർഷം (last year) sets the frame; the day-chain "
            "orders it. കേട്ട് (having heard) shows the conjunctive "
            "participle chaining actions: കഥ കേട്ട് ഉറങ്ങി. The closing "
            "line pivots to the future negative മറക്കില്ല (will not "
            "forget) - the journey sealed in memory. Past-tense travel "
            "is the most useful narrative skill; master these verbs and "
            "any trip can be retold."
        ),
        "key_points": [
            "10-sentence past-tense story; line-by-line translation.",
            "Nine reshaped past verbs: പോയി, വന്നു-class forms.",
            "Conjunctive participle: കഥ കേട്ട് ഉറങ്ങി.",
            "Closing pivot: future negative മറക്കില്ല.",
        ],
        "requirements": [
            "Read the tenses record for past forms.",
            "Retell a real trip of yours in past-tense Malayalam.",
        ],
        "standards": [
            "Story is constructed by the archive for teaching; grammar follows Asher & Kumari 1997.",
        ],
        "citations": [CIT_ASHER],
        "must_contain": ["കഴിഞ്ഞ വർഷം", "പുറപ്പെട്ടു", "സ്വീകരിച്ചു", "കേട്ട്", "മറക്കില്ല"],
        "sig_lens": (
            "Through the Signature lens this journey is a sworn return: "
            "every mile a vow of remembrance, every grandmother's welcome "
            "a seal on belonging."
        ),
        "drill": {
            "lines": 10,
            "past_verbs": ["പോയി", "പുറപ്പെട്ടു", "കണ്ടു", "കഴിച്ചു",
                           "കാത്തിരുന്നു", "സ്വീകരിച്ചു", "കുളിച്ചു",
                           "പറഞ്ഞു", "ഉറങ്ങി"],
            "frame": "കഴിഞ്ഞ വർഷം",
            "closing": "മറക്കില്ല",
        },
    },
    {
        "key": "story3",
        "name": "Malayalam Short Story III: Plans for Tomorrow",
        "group": "Stories and Idioms",
        "ladder_rank": 27,
        "ladder_tier": "advanced",
        "description": (
            "A ten-sentence story in the future tense with conditionals - "
            "plans for tomorrow - with line-by-line English translation. "
            "(Archive-constructed teaching story.) \n\n"
            "  1. നാളെ ഞാൻ നേരത്തെ ഉണരും. (naalLe njaan neertte unarum.) - "
            "Tomorrow I will wake up early.\n"
            "  2. മഴ പെയ്താൽ ഞാൻ കുട എടുക്കും. (mazha peytaal njaan kuta "
            "etukkum.) - If it rains, I will take an umbrella.\n"
            "  3. ഞങ്ങൾ ഒരുമിച്ച് മാർക്കറ്റിൽ പോകും. (njangalL orumichchu "
            "maarkkattil pookum.) - We will go to the market together.\n"
            "  4. അമ്മ പച്ചക്കറി വാങ്ങും. (amma pachakkari vaangum.) - "
            "Mother will buy vegetables.\n"
            "  5. ഞാൻ പഴങ്ങൾ തിരഞ്ഞെടുക്കും. (njaan pazhangalL "
            "tiranjyetukkum.) - I will choose the fruits.\n"
            "  6. വീട്ടിൽ തിരിച്ചെത്തിയാൽ അമ്മ പാചകം ചെയ്യും. (viittil "
            "tirichchettiyaal amma paachakam cheyyum.) - When we return "
            "home, mother will cook.\n"
            "  7. വൈകുന്നേരം സുഹൃത്തുക്കൾ വരും. (vaykunneeram "
            "suhruttukkal varum.) - In the evening friends will come.\n"
            "  8. ഞങ്ങൾ ഒരുമിച്ച് ചായ കുടിക്കും. (njangalL orumichchu "
            "chaaya kutikkum.) - We will drink tea together.\n"
            "  9. രാത്രി ഞാൻ പാഠങ്ങൾ പഠിക്കും. (raatri njaan paatthangalL "
            "patThikkum.) - At night I will study the lessons.\n"
            "  10. നാളെ നല്ല ദിവസമായിരിക്കും. (naalLe nalla "
            "divasamaayirikkum.) - Tomorrow will be a good day."
        ),
        "how_it_works": (
            "The future tense -ഉം drives every line: ഉണരും, എടുക്കും, "
            "പോകും, വാങ്ങും, ചെയ്യും, വരും, കുടിക്കും, പഠിക്കും, "
            "ആയിരിക്കും. Conditionals with -ആൽ branch the plan: മഴ "
            "പെയ്താൽ (if it rains), തിരിച്ചെത്തിയാൽ (when we return). "
            "The copula's future ആയിരിക്കും closes with a blessing on "
            "the day. Future plans are the friendliest conversation "
            "topic - master -ഉം and -ആൽ and every tomorrow opens."
        ),
        "key_points": [
            "10-sentence future-tense story; line-by-line translation.",
            "Future -ഉം on every verb.",
            "Conditionals -ആൽ: പെയ്താൽ, തിരിച്ചെത്തിയാൽ.",
            "Copula future: ആയിരിക്കും.",
        ],
        "requirements": [
            "Read the tenses record for -ഉം and -ആൽ.",
            "Write your own ten-line plan for tomorrow.",
        ],
        "standards": [
            "Story is constructed by the archive for teaching; grammar follows Asher & Kumari 1997.",
        ],
        "citations": [CIT_ASHER],
        "must_contain": ["ഉണരും", "പെയ്താൽ", "തിരിച്ചെത്തിയാൽ", "മായിരിക്കും", "നാളെ"],
        "sig_lens": (
            "Through the Signature lens tomorrow is a sworn promise: "
            "every plan a vow of intention, every conditional a seal on "
            "readiness."
        ),
        "drill": {
            "lines": 10,
            "future_verbs": ["ഉണരും", "എടുക്കും", "പോകും", "വാങ്ങും",
                             "ചെയ്യും", "വരും", "കുടിക്കും", "പഠിക്കും"],
            "conditionals": ["പെയ്താൽ", "തിരിച്ചെത്തിയാൽ"],
            "copula_future": "ആയിരിക്കും",
        },
    },
    {
        "key": "idioms",
        "name": "Malayalam Idioms and Proverbs",
        "group": "Stories and Idioms",
        "ladder_rank": 28,
        "ladder_tier": "advanced",
        "description": (
            "Twenty idioms and proverbs - Malayalam, literal translation, "
            "real meaning, and an example sentence each. \n\n"
            "  1. അതിഥി ദേവോ ഭവ. - Lit: the guest is god. Meaning: treat "
            "guests with reverence. വിരുന്നുകാരെ സ്നേഹത്തോടെ സ്വീകരിക്കൂ; "
            "അതിഥി ദേവോ ഭവ.\n"
            "  2. പഴഞ്ചൊല്ലിൽ പതിരില്ല. - Lit: there is no chaff in an old "
            "saying. Meaning: proverbs hold truth. മുത്തശ്ശി പറഞ്ഞത് "
            "ശരിയാണ്; പഴഞ്ചൊല്ലിൽ പതിരില്ല.\n"
            "  3. കാക്കയ്ക്ക് തൻകുഞ്ഞ് പൊൻകുഞ്ഞ്. - Lit: to the crow its "
            "chick is a golden chick. Meaning: every parent finds their "
            "own child precious. അവൾ കുട്ടിയെ പുകഴ്ത്തുന്നു; കാക്കയ്ക്ക് "
            "തൻകുഞ്ഞ് പൊൻകുഞ്ഞ്.\n"
            "  4. ആനവായിൽ അമ്പഴങ്ങ. - Lit: a hog-plum in an elephant's "
            "mouth. Meaning: far too little for the need. ഈ സഹായം "
            "ആനവായിൽ അമ്പഴങ്ങ പോലെയാണ്.\n"
            "  5. വിദ്യാധനം സർവധനാൽ പ്രധാനം. - Lit: the wealth of learning "
            "is the highest of all wealth. Meaning: knowledge outlasts "
            "riches. പഠിക്കൂ; വിദ്യാധനം സർവധനാൽ പ്രധാനം.\n"
            "  6. കാറ്റുള്ളപ്പോൾ തൂറ്റുക. - Lit: winnow while the wind "
            "blows. Meaning: act while conditions favor. അവസരം വന്നപ്പോൾ "
            "പ്രവർത്തിക്കൂ; കാറ്റുള്ളപ്പോൾ തൂറ്റുക.\n"
            "  7. അടി തെറ്റിയാൽ ആനയും വീഴും. - Lit: if the footing slips, "
            "even the elephant falls. Meaning: anyone can fail from a "
            "small mistake. ശ്രദ്ധിക്കൂ; അടി തെറ്റിയാൽ ആനയും വീഴും.\n"
            "  8. വിനാശകാലേ വിപരീതബുദ്ധി. - Lit: when ruin nears, judgment "
            "turns perverse. Meaning: bad decisions precede downfall. "
            "അവൻ തെറ്റായ വഴി തിരഞ്ഞെടുത്തു; വിനാശകാലേ വിപരീതബുദ്ധി.\n"
            "  9. ഉപ്പ് തിന്നവൻ വെള്ളം കുടിക്കും. - Lit: who eats salt will "
            "drink water. Meaning: actions have consequences. ചെയ്തതിന്റെ "
            "ഫലം അനുഭവിക്കണം; ഉപ്പ് തിന്നവൻ വെള്ളം കുടിക്കും.\n"
            "  10. ആരോഗ്യമാണ് മഹാഭാഗ്യം. - Lit: health is the greatest "
            "fortune. Meaning: health outweighs wealth. പണം പോയാലും "
            "ആരോഗ്യം വേണം; ആരോഗ്യമാണ് മഹാഭാഗ്യം.\n"
            "  11. ഒരുമയാണ് ബലം. - Lit: unity is strength. Meaning: "
            "together we are strong. എല്ലാവരും ഒരുമിച്ച് നിന്നു; ഒരുമയാണ് "
            "ബലം.\n"
            "  12. സമയം പൊൻവിലയുള്ളത്. - Lit: time is worth gold. "
            "Meaning: do not waste time. വൈകരുത്; സമയം പൊൻവിലയുള്ളത്.\n"
            "  13. പറയാൻ എളുപ്പം, ചെയ്യാൻ പ്രയാസം. - Lit: easy to say, "
            "hard to do. Meaning: doing exceeds talking. അവൻ പറഞ്ഞു, "
            "പക്ഷേ ചെയ്തില്ല; പറയാൻ എളുപ്പം, ചെയ്യാൻ പ്രയാസം.\n"
            "  14. കണ്ടതെല്ലാം വിശ്വസിക്കരുത്. - Lit: don't believe "
            "everything seen. Meaning: verify before trusting. വാർത്ത "
            "പരിശോധിക്കൂ; കണ്ടതെല്ലാം വിശ്വസിക്കരുത്.\n"
            "  15. അധ്വാനം ഫലം തരും. - Lit: labor gives fruit. Meaning: "
            "hard work pays. ദിവസവും പഠിക്കൂ; അധ്വാനം ഫലം തരും.\n"
            "  16. അറിവാണ് ശക്തി. - Lit: knowledge is power. Meaning: "
            "learning empowers. പുസ്തകങ്ങൾ വായിക്കൂ; അറിവാണ് ശക്തി.\n"
            "  17. തന്നെത്താൻ സഹായിക്കുന്നവനെ ദൈവം സഹായിക്കും. - Lit: god "
            "helps who helps himself. Meaning: self-effort comes first. "
            "പരിശ്രമിക്കൂ; തന്നെത്താൻ സഹായിക്കുന്നവനെ ദൈവം സഹായിക്കും.\n"
            "  18. ക്ഷമയ്ക്ക് ഫലമുണ്ട്. - Lit: patience has fruit. Meaning: "
            "patience is rewarded. കാത്തിരിക്കൂ; ക്ഷമയ്ക്ക് ഫലമുണ്ട്.\n"
            "  19. ഇന്ന് ചെയ്യേണ്ടത് നാളേക്ക് മാറ്റരുത്. - Lit: don't put "
            "off today's work to tomorrow. Meaning: act now. ഇപ്പോൾ "
            "തുടങ്ങൂ; ഇന്ന് ചെയ്യേണ്ടത് നാളേക്ക് മാറ്റരുത്.\n"
            "  20. സത്യത്തിന് ജയം. - Lit: truth has victory. Meaning: "
            "truth triumphs in the end. സത്യം പറയൂ; സത്യത്തിന് ജയം."
        ),
        "how_it_works": (
            "Proverbs compress whole philosophies into one line: the "
            "literal image (elephant, crow, salt, wind) carries the "
            "meaning, and speakers deploy the proverb as the punchline of "
            "advice. പഴഞ്ചൊല്ല് (old saying) is the native word for "
            "proverb. Many Malayalam proverbs are shared Sanskrit "
            "maxims (അതിഥി ദേവോ ഭവ, വിദ്യാധനം); others are pure Kerala "
            "soil (ആനവായിൽ അമ്പഴങ്ങ, കാക്കയ്ക്ക് തൻകുഞ്ഞ് പൊൻകുഞ്ഞ്). Use "
            "one proverb per conversation - more is showing off. Each "
            "entry's example sentence shows the natural slot where the "
            "proverb lands."
        ),
        "key_points": [
            "20 proverbs: Malayalam + literal + meaning + example.",
            "പഴഞ്ചൊല്ല്: the native word for proverb.",
            "Two streams: Sanskrit maxims and Kerala-soil sayings.",
            "One proverb per conversation is the custom.",
        ],
        "requirements": [
            "Use three proverbs in real conversation this week.",
            "Learn the literal images; they are the memory hooks.",
        ],
        "standards": [
            "Proverb glosses follow documented Kerala usage; example sentences are constructed by the archive.",
        ],
        "citations": [CIT_ASHER, CIT_ANDRONOV],
        "must_contain": ["പഴഞ്ചൊല്ലിൽ പതിരില്ല", "ആനവായിൽ അമ്പഴങ്ങ", "പഴഞ്ചൊല്ലിൽ", "സത്യത്തിന് ജയം", "ക്ഷമയ്ക്ക്"],
        "sig_lens": (
            "Through the Signature lens proverbs are sworn wisdom: "
            "twenty seals of the ancestors, each a vow that truth, "
            "once spoken well, never dies."
        ),
        "drill": {
            "proverbs": 20,
            "streams": ["Sanskrit maxims", "Kerala-soil sayings"],
            "native_word": "പഴഞ്ചൊല്ല്",
        },
    },
    {
        "key": "registers",
        "name": "Malayalam Formal and Polite Registers",
        "group": "Conversation and Registers",
        "ladder_rank": 29,
        "ladder_tier": "advanced",
        "description": (
            "Fifteen formal-versus-informal pairs - letters, business, "
            "and elders - each with translation. \n\n"
            "  1. Informal: നീ വരുന്നോ? - Are you coming? Formal: "
            "താങ്കൾ വരുന്നുണ്ടോ? - Are you coming? (respectful)\n"
            "  2. Informal: ഇത് തരൂ. - Give this. Formal: ദയവായി ഇത് "
            "തരൂ. - Please give this.\n"
            "  3. Informal: പോയി വാ. - Go and come. Formal: പോയി "
            "വരൂ. - Please go and come back.\n"
            "  4. Informal: എന്താ? - What? Formal: എന്താണ്? - What is it?\n"
            "  5. Informal: ശരി, പോട്ടെ. - OK, bye. Formal: ശരി, പിന്നെ "
            "കാണാം. - Very well, see you later.\n"
            "  6. Letter opening informal: പ്രിയ സുഹൃത്തേ, - Dear friend, "
            "Letter opening formal: ബഹുമാനപ്പെട്ട സാർ, - Respected Sir,\n"
            "  7. Letter close informal: സ്നേഹത്തോടെ, - With love, Letter "
            "close formal: വിശ്വസ്തതയോടെ, - Faithfully,\n"
            "  8. Business informal: വില കുറയ്ക്കൂ. - Reduce the price. "
            "Business formal: വിലയിൽ ഇളവ് തരുമോ? - Would you give a "
            "discount?\n"
            "  9. To an elder informal: (never used) - To an elder formal: "
            "അമ്മേ, സുഖമാണോ? - Mother, are you well?\n"
            "  10. Request informal: സഹായിക്ക്. - Help. Request formal: "
            "സഹായിക്കാമോ? - Could you help?\n"
            "  11. Phone informal: ആരാ? - Who is it? Phone formal: ആരാണ് "
            "സംസാരിക്കുന്നത്? - Who is speaking?\n"
            "  12. Apology informal: സോറി. - Sorry. Apology formal: "
            "ക്ഷമിക്കണം. - Forgive me.\n"
            "  13. Thanks informal: നന്ദി. - Thanks. Thanks formal: വളരെ "
            "നന്ദിയുണ്ട്. - (I) am very grateful.\n"
            "  14. Invitation informal: വീട്ടിൽ വാ. - Come home. Invitation "
            "formal: വീട്ടിലേക്ക് ക്ഷണിക്കുന്നു. - (I) invite you home.\n"
            "  15. Farewell informal: പോട്ടെ. - Bye. Farewell formal: "
            "യാത്ര സുഖകരമാകട്ടെ. - Have a pleasant journey."
        ),
        "how_it_works": (
            "Register shifts on three levers: pronoun (നീ -> താങ്കൾ/നിങ്ങൾ), "
            "verb ending (bare stem -> -ൂ -> ദയവായി + -ൂ), and full forms "
            "versus contractions (എന്താണ് versus എന്താ). Elders, teachers, "
            "officials, and strangers get the formal set; friends, "
            "children, and juniors get the informal. Letters open "
            "ബഹുമാനപ്പെട്ട (respected) and close വിശ്വസ്തതയോടെ "
            "(faithfully) in formal style. Business Malayalam softens "
            "commands into questions: വിലയിൽ ഇളവ് തരുമോ? Using നീ to an "
            "elder is the classic learner's blunder - നിങ്ങൾ is always "
            "safe."
        ),
        "key_points": [
            "Three levers: pronoun, verb ending, full vs contracted forms.",
            "നീ intimate only; നിങ്ങൾ always safe.",
            "Formal letters: ബഹുമാനപ്പെട്ട ... വിശ്വസ്തതയോടെ.",
            "Business softens commands into questions.",
            "15 formal/informal pairs with translations.",
        ],
        "requirements": [
            "Read the commands record for the -ൂ forms.",
            "Write one formal letter opening and closing.",
        ],
        "standards": [
            "Register guidance follows standard Kerala usage (Asher & Kumari 1997).",
        ],
        "citations": [CIT_ASHER],
        "must_contain": ["താങ്കൾ", "ബഹുമാനപ്പെട്ട", "വിശ്വസ്തതയോടെ", "ദയവായി", "എന്താണ്"],
        "sig_lens": (
            "Through the Signature lens register is sworn courtesy: every "
            "level of speech a vow of respect, fitted to its person like "
            "a seal to its letter."
        ),
        "drill": {
            "pairs": 15,
            "levers": ["pronoun", "verb ending", "full vs contracted"],
            "safe_you": "നിങ്ങൾ",
            "formal_open": "ബഹുമാനപ്പെട്ട",
            "formal_close": "വിശ്വസ്തതയോടെ",
        },
    },
    {
        "key": "complex",
        "name": "Malayalam Compound and Complex Sentences",
        "group": "Conversation and Registers",
        "ladder_rank": 30,
        "ladder_tier": "advanced",
        "description": (
            "Fifteen long sentences with clauses, connectors, and relative "
            "clauses - parsed and translated. \n\n"
            "  1. ഞാൻ സ്കൂളിൽ പോയി, പാഠം പഠിച്ച്, വീട്ടിൽ വന്നു. - I went "
            "to school, studied the lesson, and came home. [serial verbs "
            "with -ഇ/-ച്ച്]\n"
            "  2. മഴ പെയ്തതുകൊണ്ട് ഞങ്ങൾ വീട്ടിൽ നിന്നു. - Because it "
            "rained, we stayed home. [-തുകൊണ്ട്: because]\n"
            "  3. അവൻ വന്നപ്പോൾ ഞാൻ പഠിച്ചുകൊണ്ടിരുന്നു. - When he came, "
            "I was studying. [-പ്പോൾ: when]\n"
            "  4. നന്നായി പഠിച്ചാൽ നീ ജയിക്കും. - If you study well, you "
            "will pass. [-ആൽ: if]\n"
            "  5. പുസ്തകം വായിക്കുന്ന കുട്ടി ബുദ്ധിമാനാണ്. - The child "
            "who reads books is intelligent. [relative participle "
            "-ഉന്ന]\n"
            "  6. ഞാൻ കണ്ട സിനിമ നല്ലതായിരുന്നു. - The film that I saw was "
            "good. [relative participle -അ]\n"
            "  7. അമ്മ ഉണ്ടാക്കിയ പായസം മധുരമുള്ളതാണ്. - The payasam that "
            "mother made is sweet. [-ഇയ participle]\n"
            "  8. വേഗത്തിൽ ഓടിയിട്ടും ബസ് കിട്ടിയില്ല. - Although (he) ran "
            "fast, (he) didn't get the bus. [-ഇട്ടും: although]\n"
            "  9. ചായ കുടിച്ചുകൊണ്ട് പത്രം വായിച്ചു. - (He) read the paper "
            "while drinking tea. [-കൊണ്ട്: while]\n"
            "  10. എനിക്ക് വേണ്ടത് സമാധാനമാണ്. - What I need is peace. "
            "[-അത് nominalizer]\n"
            "  11. അവൻ പറഞ്ഞത് സത്യമാണെന്ന് ഞാൻ വിശ്വസിക്കുന്നു. - I "
            "believe that what he said is true. [-എന്ന്: that]\n"
            "  12. പോകണോ വേണ്ടയോ എന്ന് തീരുമാനിക്കൂ. - Decide whether to "
            "go or not. [-ഓ ... എന്ന്: whether]\n"
            "  13. കുട്ടികൾ കളിക്കുന്നത് കണ്ട് അമ്മ ചിരിച്ചു. - Seeing the "
            "children play, mother laughed. [causal participle]\n"
            "  14. പണം ഉണ്ടെങ്കിൽ എല്ലാം നടക്കും. - If there is money, "
            "everything works. [-എങ്കിൽ: if (existential)]\n"
            "  15. പഠിക്കുന്നതും ജോലി ചെയ്യുന്നതും ഒരുമിച്ച് "
            "കൊണ്ടുപോകാം. - Studying and working can be carried on "
            "together. [nominalized verbs as subjects]"
        ),
        "how_it_works": (
            "Complex sentences are built with participles, not conjunctions "
            "like English 'that/which'. The relative participle turns a "
            "whole clause into an adjective: വായിക്കുന്ന കുട്ടി (the "
            "reading child = the child who reads). The -എന്ന് clause "
            "reports speech and thought: ...എന്ന് വിശ്വസിക്കുന്നു (believe "
            "that...). Reason, time, condition, and concession each have "
            "their suffix: -തുകൊണ്ട് (because), -പ്പോൾ (when), -ആൽ "
            "(if), -ഇട്ടും (although). Serial actions chain with the "
            "conjunctive participle: പോയി, പഠിച്ച്, വന്നു. The verb still "
            "comes last - the whole branching tree hangs before the final "
            "verb."
        ),
        "key_points": [
            "Relative participles replace 'who/which': വായിക്കുന്ന കുട്ടി.",
            "-എന്ന് for reported speech/thought.",
            "Clause suffixes: -തുകൊണ്ട് because, -പ്പോൾ when, -ആൽ if, -ഇട്ടും although.",
            "Serial verbs chain with conjunctive participles.",
            "15 parsed complex sentences.",
        ],
        "requirements": [
            "Read the tenses record for participles.",
            "Combine three simple sentences into one complex sentence.",
        ],
        "standards": [
            "Clause analysis follows Asher & Kumari 1997 and Andronov 1996.",
            "Practice sentences are constructed by the archive for teaching.",
        ],
        "citations": [CIT_ASHER, CIT_ANDRONOV],
        "must_contain": ["വായിക്കുന്ന", "-എന്ന്", "-തുകൊണ്ട്", "-ആൽ", "-ഇട്ടും"],
        "sig_lens": (
            "Through the Signature lens complex sentences are sworn "
            "architecture: every clause a sealed chamber, every "
            "participle a joint, the final verb the keystone."
        ),
        "drill": {
            "sentences": 15,
            "relative": "വായിക്കുന്ന",
            "reported": "എന്ന്",
            "suffixes": ["തുകൊണ്ട്", "പ്പോൾ", "ആൽ", "ഇട്ടും"],
        },
    },
    {
        "key": "conv_market",
        "name": "Malayalam Conversation: At the Market",
        "group": "Conversation and Registers",
        "ladder_rank": 31,
        "ladder_tier": "advanced",
        "description": (
            "A twenty-line bilingual dialogue at the vegetable market - "
            "Malayalam with romanization and English, annotated. "
            "(Archive-constructed teaching dialogue.) \n\n"
            "  1. A: നമസ്കാരം! (namaskaaram!) - Hello!\n"
            "  2. B: നമസ്കാരം, വരൂ. (namaskaaram, varuu.) - Hello, come in.\n"
            "  3. A: തക്കാളി എത്ര? (takkaalLi etra?) - How much are the "
            "tomatoes?\n"
            "  4. B: കിലോയ്ക്ക് നാൽപ്പത് രൂപ. (kiloykku naalppatu ruupa.) - "
            "Forty rupees a kilo.\n"
            "  5. A: വില കൂടുതലാണ്; കുറയ്ക്കാമോ? (vila kuututalaanu; "
            "kuraykkaamoo?) - The price is high; can you reduce it?\n"
            "  6. B: ശരി, മുപ്പത്തഞ്ച് തരാം. (shari, muppat tanchu taraam.) "
            "- OK, I'll give it for thirty-five.\n"
            "  7. A: രണ്ട് കിലോ തരൂ. (ranTu kiloo taruu.) - Give two kilos.\n"
            "  8. B: വേറെ എന്ത് വേണം? (veere entu veenam?) - What else do "
            "you need?\n"
            "  9. A: ഒരു കിലോ ഉള്ളിയും. (oru kiloo ullLiyum.) - One kilo of "
            "onions too.\n"
            "  10. B: ഉള്ളി ഫ്രഷാണ്. (ullLi fresh aanu.) - The onions are "
            "fresh.\n"
            "  11. A: പച്ചമുളക് ഉണ്ടോ? (pachchamulaku unToo?) - Do you have "
            "green chilies?\n"
            "  12. B: ഉണ്ട്, എത്ര വേണം? (unTu, etra veenam?) - Yes, how "
            "much do you need?\n"
            "  13. A: കാൽ കിലോ മതി. (kaal kiloo mati.) - A quarter kilo is "
            "enough.\n"
            "  14. B: ശരി, എല്ലാം കൂടി എഴുപത് രൂപ. (shari, ellaam kuuti "
            "ezhupatu ruupa.) - OK, seventy rupees altogether.\n"
            "  15. A: കാർഡ് എടുക്കുമോ? (kaardu etukkumoo?) - Do you take "
            "card?\n"
            "  16. B: ക്യാഷ് മാത്രം. (kyaashu maatram.) - Cash only.\n"
            "  17. A: ശരി, നൂറ് രൂപ തരാം. (shari, nuuru ruupa taraam.) - "
            "OK, I'll give a hundred rupees.\n"
            "  18. B: ബാക്കി മുപ്പത് രൂപ. (baakki muppatu ruupa.) - Thirty "
            "rupees change.\n"
            "  19. A: നന്ദി! (nanni!) - Thanks!\n"
            "  20. B: വീണ്ടും വരൂ! (viinTum varuu!) - Come again!"
        ),
        "how_it_works": (
            "The market dialogue runs the full bargaining arc from the "
            "shopping record: greeting, price-ask (എത്ര?), counter "
            "(കുറയ്ക്കാമോ?), agreement (തരാം), quantities (രണ്ട് കിലോ, "
            "കാൽ കിലോ), payment (കാർഡ് എടുക്കുമോ? ക്യാഷ് മാത്രം), "
            "change (ബാക്കി), farewell (വീണ്ടും വരൂ!). തരാം (I will "
            "give) is the seller's promise-form. Note കിലോയ്ക്ക് (per "
            "kilo, dative) and കൂടി (altogether). Every line reuses "
            "ladder vocabulary - nothing here is new, which is the "
            "point: fluency is recombination."
        ),
        "key_points": [
            "Full bargaining arc in 20 lines.",
            "Seller's promise-form: തരാം.",
            "Per-unit price: കിലോയ്ക്ക് (dative).",
            "Quantities: കിലോ, കാൽ കിലോ.",
            "Fluency is recombination of ladder words.",
        ],
        "requirements": [
            "Read the shopping record first.",
            "Act out the dialogue with a partner, swapping roles.",
        ],
        "standards": [
            "Dialogue is constructed by the archive for teaching; usage follows standard Kerala market practice.",
        ],
        "citations": [CIT_ASHER],
        "must_contain": ["തക്കാളി", "കുറയ്ക്കാമോ", "തരാം", "ബാക്കി", "വീണ്ടും വരൂ"],
        "sig_lens": (
            "Through the Signature lens this market is a sworn fair: "
            "every price haggled honestly, every change counted true, "
            "every parting a vow to return."
        ),
        "drill": {
            "lines": 20, "speakers": ["A", "B"],
            "arc": ["greeting", "price-ask", "bargain", "quantities",
                    "payment", "farewell"],
            "promise_form": "തരാം",
        },
    },
    {
        "key": "conv_friend",
        "name": "Malayalam Conversation: Meeting a Friend",
        "group": "Conversation and Registers",
        "ladder_rank": 32,
        "ladder_tier": "advanced",
        "description": (
            "A twenty-line bilingual dialogue between old friends meeting "
            "after years - Malayalam with romanization and English, "
            "annotated. (Archive-constructed teaching dialogue.) \n\n"
            "  1. A: അയ്യോ, രവിയല്ലേ! (ayyoo, raviyallee!) - Oh, it's "
            "Ravi!\n"
            "  2. B: അനൂപ്! എത്ര നാളായി! (anuup! etra naalaayi!) - Anoop! "
            "It's been so long!\n"
            "  3. A: സുഖമാണോ? (sukhamaan oo?) - Are you well?\n"
            "  4. B: സുഖം, നീ? (sukham, nii?) - Well, and you?\n"
            "  5. A: ഞാനും സുഖം. എവിടെയാണ് ജോലി? (njaanum sukham. eviteyaanu "
            "jooli?) - I'm well too. Where do you work?\n"
            "  6. B: കൊച്ചിയിൽ, ഒരു കമ്പനിയിൽ. (kochchiyil, oru "
            "kampaniyil.) - In Kochi, at a company.\n"
            "  7. A: കുടുംബം സുഖമാണോ? (kutumbam sukhamaan oo?) - Is the "
            "family well?\n"
            "  8. B: എല്ലാവരും സുഖം. അച്ഛനമ്മമാർ വീട്ടിലുണ്ട്. (ellaavarum "
            "sukham. achchhanammamaar viittilunTu.) - Everyone's well. "
            "Parents are home.\n"
            "  9. A: കുട്ടികൾ എത്ര പേർ? (kuttikal etra peer?) - How many "
            "children?\n"
            "  10. B: രണ്ട് പേർ - ഒരു മകനും ഒരു മകളും. (ranTu peer - oru "
            "makanum oru makalum.) - Two - a son and a daughter.\n"
            "  11. A: നമുക്ക് ചായ കുടിക്കാം. (namukku chaaya kutikkaam.) - "
            "Let's have tea.\n"
            "  12. B: തീർച്ചയായും! (tiirchchayaayum!) - Certainly!\n"
            "  13. A: പഴയ കാലം ഓർമ്മയുണ്ടോ? (pazhaya kaalam ormmayunToo?) "
            "- Do you remember the old days?\n"
            "  14. B: എങ്ങനെ മറക്കും! (engane marakkum!) - How could I "
            "forget!\n"
            "  15. A: സ്കൂൾ കാലത്തെ കളികൾ! (skuul kaalatte kalikalL!) - "
            "The school-day games!\n"
            "  16. B: നമ്മൾ എത്ര കളിച്ചിരുന്നു! (nammalL etra "
            "kalichchirunnu!) - How we used to play!\n"
            "  17. A: നാളെ വീട്ടിൽ വരൂ. (naalLe viittil varuu.) - Come "
            "home tomorrow.\n"
            "  18. B: തീർച്ചയായും വരാം. (tiirchchayaayum varaam.) - "
            "I'll certainly come.\n"
            "  19. A: കാണാം! (kaanaam!) - See you!\n"
            "  20. B: പിന്നെ കാണാം! (pinne kaanaam!) - See you later!"
        ),
        "how_it_works": (
            "Friends use നീ and the intimate register from the commands "
            "record - the dialogue would sound stiff with നിങ്ങൾ. The "
            "reunion arc: exclamation (അയ്യോ!), health-check (സുഖമാണോ?), "
            "catch-up triple (ജോലി, കുടുംബം, കുട്ടികൾ), invitation "
            "(ചായ കുടിക്കാം), nostalgia (പഴയ കാലം), re-invitation "
            "(വീട്ടിൽ വരൂ), farewell. എത്ര നാളായി! and എങ്ങനെ മറക്കും! "
            "are the emotional peaks - exclamation carries the feeling. "
            "കളിച്ചിരുന്നു shows the habitual past (-ഇരുന്നു): 'used to "
            "play'."
        ),
        "key_points": [
            "Intimate register: നീ between friends.",
            "Reunion arc: exclaim, health-check, catch-up, invite, remember, farewell.",
            "Emotional peaks ride exclamation.",
            "Habitual past -ഇരുന്നു: കളിച്ചിരുന്നു (used to play).",
            "20-line annotated bilingual dialogue.",
        ],
        "requirements": [
            "Read the friendship and greetings records first.",
            "Perform the dialogue, then improvise your own reunion.",
        ],
        "standards": [
            "Dialogue is constructed by the archive for teaching; usage follows standard Kerala speech.",
        ],
        "citations": [CIT_ASHER],
        "must_contain": ["എത്ര നാളായി", "കളിച്ചിരുന്നു", "പഴയ കാലം", "ചായ കുടിക്കാം", "പിന്നെ കാണാം"],
        "sig_lens": (
            "Through the Signature lens reunion is a sworn renewal: every "
            "remembered game a vow kept across the years, every "
            "invitation a seal on friendship."
        ),
        "drill": {
            "lines": 20, "speakers": ["A", "B"],
            "register": "intimate",
            "arc": ["exclaim", "health-check", "catch-up", "invite",
                    "nostalgia", "farewell"],
            "habitual_past": "കളിച്ചിരുന്നു",
        },
    },
    {
        "key": "conv_problem",
        "name": "Malayalam Conversation: Solving a Problem",
        "group": "Conversation and Registers",
        "ladder_rank": 33,
        "ladder_tier": "advanced",
        "description": (
            "A twenty-line bilingual dialogue solving a problem - a "
            "traveler whose bus broke down - Malayalam with romanization "
            "and English, annotated. (Archive-constructed teaching "
            "dialogue.) \n\n"
            "  1. A: സഹായിക്കാമോ? ബസ് കേടായി. (sahaayikkaamoo? basu "
            "ketaayi.) - Can you help? The bus broke down.\n"
            "  2. B: എവിടെ വച്ച്? (evite vachu?) - Where did it happen?\n"
            "  3. A: അടുത്ത ജംഗ്ഷനിൽ. (atutta jangshanil.) - At the next "
            "junction.\n"
            "  4. B: വിഷമിക്കേണ്ട, ഞാൻ വരാം. (vishamikkeenta, njaan "
            "varaam.) - Don't worry, I'll come.\n"
            "  5. A: വളരെ നന്ദി! (valare nanni!) - Thank you so much!\n"
            "  6. B: എത്ര പേരുണ്ട്? (etra peerunTu?) - How many people are "
            "there?\n"
            "  7. A: ഇരുപത് പേർ. (irupatu peer.) - Twenty people.\n"
            "  8. B: മെക്കാനിക്കിനെ വിളിക്കാം. (mekkaanikkine vilikkaam.) - "
            "Let's call a mechanic.\n"
            "  9. A: എത്ര സമയമെടുക്കും? (etra samayametukkum?) - How long "
            "will it take?\n"
            "  10. B: ഒരു മണിക്കൂർ. (oru mannikkuur.) - One hour.\n"
            "  11. A: കുട്ടികൾക്ക് വെള്ളം വേണം. (kuttikalkku velLlam "
            "veenam.) - The children need water.\n"
            "  12. B: കട അടുത്താണ്; വാങ്ങിത്തരാം. (kata atuttaanu; "
            "vaangittaraam.) - The shop is near; I'll buy and give.\n"
            "  13. A: പണം ഞാൻ തരാം. (panNam njaan taraam.) - I'll pay.\n"
            "  14. B: സാരമില്ല, ഞാൻ എടുക്കാം. (saaramilla, njaan "
            "etukkaam.) - Never mind, I'll get it.\n"
            "  15. A: മെക്കാനിക് വന്നോ? (mekkaanik vannoo?) - Has the "
            "mechanic come?\n"
            "  16. B: വന്നു, നോക്കുന്നുണ്ട്. (vannu, nookkunnunTu.) - "
            "He's come; he's looking at it.\n"
            "  17. A: ശരിയാകുമോ? (shariyaakumoo?) - Will it be fixed?\n"
            "  18. B: ശരിയാകും, വിഷമിക്കേണ്ട. (shariyaakum, "
            "vishamikkeenta.) - It'll be fixed, don't worry.\n"
            "  19. A: നിങ്ങളുടെ സഹായം വലുതാണ്. (ningalLute sahaayam "
            "valutaanu.) - Your help means a lot.\n"
            "  20. B: സന്തോഷം! യാത്ര സുഖകരമാകട്ടെ! (santoshham! yaatra "
            "sukhakaramaakatte!) - My pleasure! Have a safe journey!"
        ),
        "how_it_works": (
            "Problem-solving runs on the comfort-action loop: "
            "വിഷമിക്കേണ്ട (don't worry) + -ആം proposals (വിളിക്കാം, "
            "വാങ്ങിത്തരാം, എടുക്കാം). The problem states in the past "
            "(കേടായി), needs in the present (വേണം), solutions in the "
            "future (വരാം, ശരിയാകും). Questions diagnose: എവിടെ വച്ച്? "
            "എത്ര പേർ? എത്ര സമയം? The helper's തരാം/തരാം-forms promise "
            "action; the traveler's തരാം promises payment. Closing "
            "gratitude (സഹായം വലുതാണ്) and blessing (യാത്ര "
            "സുഖകരമാകട്ടെ) seal the exchange. This is the most useful "
            "dialogue in the database - real trouble, real Malayalam."
        ),
        "key_points": [
            "Comfort-action loop: വിഷമിക്കേണ്ട + -ആം proposals.",
            "Problem past, need present, solution future.",
            "Diagnostic questions: എവിടെ, എത്ര, എത്ര സമയം.",
            "Promise-forms: തരാം, വരാം, ശരിയാകും.",
            "20-line annotated bilingual dialogue.",
        ],
        "requirements": [
            "Read the travel and health records for problem vocabulary.",
            "Rehearse the comfort-action loop until automatic.",
        ],
        "standards": [
            "Dialogue is constructed by the archive for teaching; usage follows standard Kerala speech.",
        ],
        "citations": [CIT_ASHER],
        "must_contain": ["കേടായി", "വിഷമിക്കേണ്ട", "വാങ്ങിത്തരാം", "ശരിയാകും", "സുഖകരമാകട്ടെ"],
        "sig_lens": (
            "Through the Signature lens help is a sworn rescue: every "
            "problem spoken plainly, every solution a vow kept, every "
            "safe journey a seal of care."
        ),
        "drill": {
            "lines": 20, "speakers": ["A", "B"],
            "loop": ["comfort", "diagnose", "propose", "promise",
                     "gratitude"],
            "problem_past": "കേടായി", "solution_future": "ശരിയാകും",
        },
    },
    {
        "key": "mastery",
        "name": "Malayalam Mastery Review and Full Reference",
        "group": "Mastery Reference",
        "ladder_rank": 34,
        "ladder_tier": "advanced",
        "description": (
            "The whole database in one teaching summary - alphabet, 200 "
            "core words, key grammar, and all phrase tables. \n\n"
            "ALPHABET: 16 vowels (അ ആ ഇ ഈ ഉ ഊ ഋ ൠ ഌ ൡ എ ഏ ഐ ഒ ഓ ഔ), 36 "
            "consonants in five vargas (ക ഖ ഗ ഘ ങ | ച ഛ ജ ഝ ഞ | ട ഠ ഡ ഢ "
            "ണ | ത ഥ ദ ധ ന | പ ഫ ബ ഭ മ | യ ര ല വ | ശ ഷ സ ഹ | ള ഴ റ), 5 "
            "chillu (ൻ ൺ ർ ൽ ൾ), digits ൦-൯. Inherent 'a'; chandrakkala "
            "് kills it. \n\n"
            "200 CORE WORDS (Malayalam - English): വീട് house, വെള്ളം "
            "water, ചോറ് rice, അമ്മ mother, അച്ഛൻ father, സുഹൃത്ത് friend, "
            "പുസ്തകം book, സ്കൂൾ school, മരം tree, പൂവ് flower, സൂര്യൻ "
            "sun, ചന്ദ്രൻ moon, നായ dog, പൂച്ച cat, മീൻ fish, പണം money, "
            "കട shop, റോഡ് road, കാർ car, ഫോൺ phone, ആശുപത്രി hospital, "
            "മഴ rain, ഭക്ഷണം food, കുട്ടി child, ദിവസം day, പോകുക go, "
            "വരിക come, കഴിക്കുക eat, കുടിക്കുക drink, കാണുക see, ചെയ്യുക "
            "do, പറയുക say, എഴുതുക write, വായിക്കുക read, പഠിക്കുക learn, "
            "പഠിപ്പിക്കുക teach, ഉറങ്ങുക sleep, ഉണരുക wake, ഓടുക run, "
            "നടക്കുക walk, ഇരിക്കുക sit, നിൽക്കുക stand, കൊടുക്കുക give, "
            "എടുക്കുക take, വാങ്ങുക buy, വിൽക്കുക sell, സ്നേഹിക്കുക love, "
            "ചിരിക്കുക laugh, കരയുക cry, നല്ല good, ചീത്ത bad, വലിയ big, "
            "ചെറിയ small, പുതിയ new, പഴയ old, മനോഹരം beautiful, ഉയർന്ന "
            "tall, കുറിയ short, നീളമുള്ള long, ചൂടുള്ള hot, തണുത്ത cold, "
            "മധുരമുള്ള sweet, പുളിയുള്ള sour, എരിവുള്ള spicy, ദൂരെ far, "
            "അടുത്ത് near, ഞാൻ I, നീ you(inf), നിങ്ങൾ you(form), അവൻ he, "
            "അവൾ she, അത് it, ഞങ്ങൾ we(excl), നമ്മൾ we(incl), അവർ they, "
            "എന്റെ my, നിന്റെ your, അവന്റെ his, അവളുടെ her, ഇത് this, അത് "
            "that, ആര് who, എന്ത് what, ഏത് which, എവിടെ where, എപ്പോൾ "
            "when, എന്തുകൊണ്ട് why, എങ്ങനെ how, എത്ര how many, ഒന്ന് 1, "
            "രണ്ട് 2, മൂന്ന് 3, നാല് 4, അഞ്ച് 5, ആറ് 6, ഏഴ് 7, എട്ട് 8, "
            "ഒമ്പത് 9, പത്ത് 10, ഇരുപത് 20, മുപ്പത് 30, നൂറ് 100, തിങ്കൾ "
            "Monday, വെള്ളി Friday, ഞായർ Sunday, മണി o'clock, ഇന്ന് "
            "today, നാളെ tomorrow, ഇന്നലെ yesterday, നമസ്കാരം hello, നന്ദി "
            "thanks, ദയവായി please, ക്ഷമിക്കണം sorry, അതെ yes, ഇല്ല no, "
            "ശരി OK, സുഖമാണോ how are you, കാണാം see you, അടുക്കള kitchen, "
            "മുറി room, മേശ table, കസേര chair, വാതിൽ door, ജനൽ window, "
            "കുടുംബം family, സഹോദരൻ brother, സഹോദരി sister, മുത്തശ്ശൻ "
            "grandfather, മുത്തശ്ശി grandmother, ചായ tea, കാപ്പി coffee, "
            "പാൽ milk, പഞ്ചസാര sugar, ഉപ്പ് salt, തേങ്ങ coconut, മാങ്ങ "
            "mango, പഴം banana, പച്ചക്കറി vegetables, കറി curry, പായസം "
            "payasam, ബസ് bus, ട്രെയിൻ train, ടിക്കറ്റ് ticket, "
            "വിമാനത്താവളം airport, ഹോട്ടൽ hotel, യാത്ര journey, "
            "ആശുപത്രി hospital, ഡോക്ടർ doctor, മരുന്ന് medicine, തല head, "
            "കണ്ണ് eye, കൈ hand, കാല് leg, ഹൃദയം heart, പനി fever, "
            "വേദന pain, സന്തോഷം happiness, ദുഃഖം sadness, ദേഷ്യം anger, "
            "പേടി fear, സ്നേഹം love, അത്ഭുതം surprise, ആന elephant, കടുവ "
            "tiger, മയിൽ peacock, കിളി bird, പുഴ river, കടൽ sea, മല "
            "mountain, കാലാവസ്ഥ weather, പ്രകൃതി nature, വില price, "
            "ചന്ത market, ബില്ല് bill, ഓണം Onam, വിഷു Vishu, സദ്യ feast, "
            "ജോലി work, ഓഫീസ് office, യോഗം meeting, ശമ്പളം salary, "
            "പരീക്ഷ exam, പാഠം lesson, വിദ്യാർത്ഥി student, അധ്യാപകൻ "
            "teacher, മെസ്സേജ് message, ഇമെയിൽ email, കമ്പ്യൂട്ടർ "
            "computer, ആപ്പ് app, ഇന്റർനെറ്റ് internet. \n\n"
            "KEY GRAMMAR: SOV order. Seven cases: -എ -ന്/-ക്ക് -ഓട് "
            "-കൊണ്ട് -ഉടെ -ഇൽ. Postpositions. Tenses: -unnu / -i / -um. "
            "Copula ആണ്/ആയിരുന്നു/ആകും. Negation അല്ല/ഇല്ല. Questions "
            "-ഓ. Plurals -കൾ. Pronouns: നമ്മൾ/ഞങ്ങൾ, നീ/നിങ്ങൾ. "
            "Imperatives: stem / -ൂ / ദയവായി / -രുത്. Conditionals -ആൽ. "
            "Relatives: -ഉന്ന/-അ participles. Reported: -എന്ന്. \n\n"
            "PHRASE TABLES: Greetings - നമസ്കാരം, സുഖമാണോ, നന്ദി, "
            "ദയവായി, ക്ഷമിക്കണം, കാണാം. Survival - മനസ്സിലായില്ല, "
            "പതുക്കെ പറയൂ, വീണ്ടും പറയൂ. Market - എത്ര, കുറയ്ക്കാമോ, "
            "ബാക്കി. Travel - എവിടെയാണ്, കിട്ടുമോ, വഴി തെറ്റി. Health - "
            "പനിയുണ്ട്, വേദനിക്കുന്നു, ഡോക്ടറെ. Feelings - സന്തോഷം, "
            "ദുഃഖം, സ്നേഹിക്കുന്നു. Time - മൂന്ന് മണി, അഞ്ചര, നാളെ. "
            "Proverbs - പഴഞ്ചൊല്ലിൽ പതിരില്ല, ആനവായിൽ അമ്പഴങ്ങ, "
            "സത്യത്തിന് ജയം. \n\n"
            "You climbed the ladder: overview, script, sounds, words, "
            "grammar, themes, tenses, stories, idioms, registers, "
            "complex sentences, conversations - and now the whole "
            "language fits on one page. Keep speaking; the ladder never "
            "ends."
        ),
        "how_it_works": (
            "This record compresses the other thirty-three into a single "
            "reference page: the alphabet table, the 200-word core (every "
            "noun, verb, adjective, pronoun, and number from the ladder), "
            "the grammar rules in telegraph form, and the phrase tables "
            "for greetings, survival, market, travel, health, feelings, "
            "time, and proverbs. Use it as the daily drill sheet: cover "
            "the English column and produce the Malayalam, then reverse. "
            "Anything fuzzy sends you back up the ladder to the full "
            "record - the mastery page is the index, the records are the "
            "library."
        ),
        "key_points": [
            "Alphabet table: 16 vowels, 36 consonants, 5 chillu, digits.",
            "200 core words with English glosses.",
            "Grammar in telegraph form: cases, tenses, negation, questions.",
            "Phrase tables: greetings, survival, market, travel, health, feelings, time, proverbs.",
            "The index to the whole ladder.",
        ],
        "requirements": [
            "Read every record before drilling this page.",
            "Drill Malayalam-to-English and English-to-Malayalam daily.",
        ],
        "standards": [
            "Summary is derived from the ladder records; forms follow Asher & Kumari 1997.",
        ],
        "citations": [CIT_ASHER, CIT_ANDRONOV, CIT_ISO, CIT_CLASSICAL, CIT_CENSUS],
        "must_contain": ["200", "chillu", "SOV", "-ആൽ", "പഴഞ്ചൊല്ലിൽ പതിരില്ല"],
        "sig_lens": (
            "Through the Signature lens this page is the sworn seal of "
            "the whole archive: thirty-four vows compressed into one "
            "covenant, the language entire, carried whole."
        ),
        "drill": {
            "core_words": 200,
            "vowels": 16, "consonants": 36, "chillu": 5,
            "cases": 7, "tenses": 3,
        },
    },
]
