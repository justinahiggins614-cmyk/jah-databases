#!/usr/bin/env python3
"""Entries for the Arabic to English databases (Manon's language orders #10-11,
2026-10-17, roster rank 5).

Verified 2026-10-17: RAW SWEEP over the full manifest (2,410 databases) PLUS
every shard index title in jah-databases-data-1 (814 index files) — zero
'language-arabic*' slugs; ID prefixes JAH-LARA- (public) and JAH-LARAS-
(signature) verified free in the manifest id_prefix values AND in every
shard index (zero zgrep hits for 'JAH-LARA' across 814 index.jsonl.gz
files). Pre-authoring whole-system dedupe-gate check over all 68 planned
titles (34 records + 34 Signature Edition titles): zero collisions, zero
refusals.

This build creates two NEW databases, 34 ladder-ordered records each:

  language-arabic              - The Arabic to English Database
                                 (public-harvest: real, fact-checked Modern
                                 Standard Arabic - overview, writing system,
                                 phonology, core vocabulary with sentences,
                                 grammar essentials, themed sentence sets,
                                 verb tenses, questions and answers,
                                 commands, descriptions, stories, idioms,
                                 registers, complex sentences, conversations,
                                 mastery reference; every line in Arabic
                                 script with transliteration and English
                                 translation; standard references Wright
                                 1896, Ryding 2005, Badawi-Carter-Gully 2004,
                                 Holes 2004, Hans Wehr 1979, ISO 233:1984)
  language-arabic-signature    - The Arabic to English Signature Database
                                 (his original Signature Language Method:
                                 every letter a sworn mark, every root a
                                 family, grammar the covenant of meaning;
                                 src signature, titles suffixed " (Signature
                                 Edition)", clearly labeled Signature-made,
                                 never presented as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

Every record carries Arabic content (Arabic script + transliteration) +
English translation + example sentences. Sentences are required in EVERY
record - no vocabulary-list-only records.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_language_arabic.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos before writing.

Build-time cross-check: every entry declares 'must_contain' strings and the
build asserts each one appears verbatim in the record description, so entry
text and demo outputs can never drift apart.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature Language Method: "
            "every letter a sworn mark, every root a family, every sentence "
            "a covenant of meaning. Clearly labeled Signature-made, never "
            "presented as authentic public record.")

CIT_WRIGHT = ("Wright W. A Grammar of the Arabic Language. 3rd ed. "
              "Cambridge University Press; 1896 (revised 1967).")
CIT_RYDING = ("Ryding KC. A Reference Grammar of Modern Standard Arabic. "
              "Cambridge University Press; 2005.")
CIT_BADAWI = ("Badawi E, Carter MG, Gully A. Reference Grammar of Literary "
              "Arabic. Routledge; 2004.")
CIT_HOLES = ("Holes C. Modern Arabic: Structures, Functions, and Varieties. "
             "Georgetown University Press; 2004.")
CIT_WEHR = ("Wehr H. A Dictionary of Modern Written Arabic. 4th ed. "
            "Harrassowitz; 1979.")
CIT_ISO233 = ("ISO 233:1984. Documentation - Transliteration of Arabic "
              "characters into Latin characters.")
CIT_UN = ("United Nations: Arabic is one of the six official languages of "
          "the United Nations (General Assembly resolution 3190 (XXVIII), "
          "1973).")

# The 28 letters: (isolated form, name, transliteration). Order is the
# standard abjadi-derived teaching order used across Arabic curricula.
LETTERS28 = [
    ("ا", "alif", "a"), ("ب", "ba", "b"), ("ت", "ta", "t"),
    ("ث", "tha", "th"), ("ج", "jim", "j"), ("ح", "ha", "h"),
    ("خ", "kha", "kh"), ("د", "dal", "d"), ("ذ", "dhal", "dh"),
    ("ر", "ra", "r"), ("ز", "zay", "z"), ("س", "sin", "s"),
    ("ش", "shin", "sh"), ("ص", "sad", "s"), ("ض", "dad", "d"),
    ("ط", "ta2", "t"), ("ظ", "za", "z"), ("ع", "ayn", "3"),
    ("غ", "ghayn", "gh"), ("ف", "fa", "f"), ("ق", "qaf", "q"),
    ("ك", "kaf", "k"), ("ل", "lam", "l"), ("م", "mim", "m"),
    ("ن", "nun", "n"), ("ه", "ha2", "h"), ("و", "waw", "w"),
    ("ي", "ya", "y"),
]
# 28 plain transliterations (emphatics distinguished in the record text with
# dot-below marks: ṣ ḍ ṭ ẓ, plus ḥ ʿ ʾ).
LETTER_TLIN = {
    "ا": "ā", "ب": "b", "ت": "t", "ث": "th", "ج": "j", "ح": "ḥ",
    "خ": "kh", "د": "d", "ذ": "dh", "ر": "r", "ز": "z", "س": "s",
    "ش": "sh", "ص": "ṣ", "ض": "ḍ", "ط": "ṭ", "ظ": "ẓ", "ع": "ʿ",
    "غ": "gh", "ف": "f", "ق": "q", "ك": "k", "ل": "l", "م": "m",
    "ن": "n", "ه": "h", "و": "w", "ي": "y",
}
ARABIC_INDIC = ["٠", "١", "٢", "٣", "٤", "٥", "٦", "٧", "٨", "٩"]


def _alpha_lines():
    return "\n".join(
        "  %s  %s (%s)" % (ch, name, LETTER_TLIN[ch]) for ch, name, _ in LETTERS28)


ENTRIES = [
    {
        "key": "overview",
        "name": "Arabic Language Overview",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Arabic (العربية, al-ʿarabiyyah) is the Semitic language of the "
            "Afro-Asiatic family spoken as a mother tongue by about 315 "
            "million people, with total speakers above 400 million when "
            "second-language users are counted. It is the official language "
            "of more than 25 countries across the Middle East and North "
            "Africa, from Morocco and Algeria in the west to Iraq and the "
            "Gulf states in the east, and one of the six official languages "
            "of the United Nations.\n"
            "Arabic is written in the Arabic script, read right to left, "
            "with 28 letters. Modern Standard Arabic (MSA, الفصحى "
            "al-fuṣḥā) is the shared written and formal spoken standard "
            "used in news, education, books, and official speech across the "
            "whole Arab world. Everyday conversation runs in regional "
            "dialects - Egyptian, Levantine, Gulf, Iraqi, and Maghrebi "
            "among the largest - which differ in pronunciation and "
            "vocabulary but share the MSA core taught in this database.\n"
            "Key facts a learner should hold from day one: (1) Arabic "
            "builds words from three-letter roots fitted into patterns, so "
            "learning one root unlocks a whole family of words; (2) short "
            "vowels are usually unwritten, so reading means recognizing "
            "word shapes; (3) the grammar marks gender on nearly everything "
            "and number in three values - singular, dual, and plural; (4) "
            "the basic sentence order is verb first, then subject, then "
            "object."
        ),
        "how_it_works": (
            "Arabic works as a root-and-pattern system. Most words grow "
            "from a root of (usually) three consonants - for example "
            "k-t-b (ك-ت-ب), the root of writing. Slot the root into the "
            "pattern faʿala and you get kataba (كتب, he wrote); into "
            "mafʿal and you get maktab (مكتب, office, the place of "
            "writing); into kitāb and you get kitāb (كتاب, book, the thing "
            "written). The consonants carry the core idea, the vowel "
            "pattern carries the grammatical job. Once you see the system, "
            "vocabulary stops being a pile of separate words and becomes "
            "families you can predict."
        ),
        "key_points": [
            "Arabic (العربية al-ʿarabiyyah): Afro-Asiatic family, Semitic branch.",
            "About 315 million native speakers; over 400 million total speakers.",
            "Official in 25+ countries across the Middle East and North Africa.",
            "One of the six official languages of the United Nations.",
            "Modern Standard Arabic (MSA) is the shared formal standard; dialects rule daily speech.",
            "28-letter script, written right to left; short vowels usually unwritten.",
            "Root-and-pattern morphology: three-letter roots + vowel patterns = word families.",
            "Grammar marks gender (masculine/feminine) and three numbers (singular/dual/plural).",
        ],
        "requirements": [
            "No prior knowledge of Arabic is assumed; the writing system record comes next.",
            "A willingness to read right to left - the single biggest first-week adjustment.",
            "Learning roots, not just words: every new word should be filed under its root.",
        ],
        "standards": [
            "ISO 639-1 code ar; ISO 639-3 code ara.",
            "Transliteration in this database follows ISO 233:1984 conventions.",
            "Speaker figures are best-available estimates, rounded, per the roster note.",
        ],
        "citations": [CIT_HOLES, CIT_UN, CIT_ISO233],
        "sig_lens": (
            "The Signature read: Arabic is the Language of the Covenant - "
            "a system where nothing stands alone. Every word swears its "
            "allegiance to a root, every root raises a family, every "
            "sentence is built like a sworn formation. The Signature "
            "Language Method learns Arabic the way Arabic is actually "
            "built: root first, pattern second, sentence last - so the "
            "learner commands families of words, not lists."
        ),
        "drill": {
            "native_m": 315, "total_m": 400, "official_countries": 26,
            "un_langs": 6, "letters": 28,
        },
        "must_contain": ["315", "Afro-Asiatic", "Semitic", "العربية"],
    },
    {
        "key": "writing",
        "name": "The Arabic Writing System",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Arabic is written right to left in the Arabic script, a "
            "cursive alphabet of 28 letters. Most letters join to their "
            "neighbors, so each letter has up to four shapes - isolated, "
            "initial, medial, final - though the letter is always the same "
            "letter. Six letters (ا د ذ ر ز و) join only to the right and "
            "never to the left, which is why words break visually after "
            "them.\n"
            "The 28 letters, in teaching order, with English "
            "transliteration:\n" + _alpha_lines() + "\n"
            "Short vowels are marks, not letters: فتحة (fatḥa, a), ضمة "
            "(ḍamma, u), كسرة (kasra, i). A small circle ْ (sukūn) marks "
            "no vowel; a small w-like mark ّ (shadda) doubles a consonant; "
            "doubled vowel marks (ً ٌ ٍ, tanwīn) add an -n sound. In "
            "ordinary books, newspapers, and screens these marks are "
            "omitted - you read كتب as kataba (he wrote), kutiba (it was "
            "written), or kutub (books) from context.\n"
            "Arabic numerals in daily use are the Arabic-Indic digits: "
            "٠ ١ ٢ ٣ ٤ ٥ ٦ ٧ ٨ ٩ (0-9). Punctuation mirrors English with "
            "two flipped marks: ؟ for the question mark and ، for the "
            "comma. Example sentence: الكتابُ على المكتبِ (al-kitābu ʿalā "
            "l-maktabi) - the book is on the desk."
        ),
        "how_it_works": (
            "Reading Arabic means recognizing connected shapes, not "
            "spelling letter by letter. Train your eye on the four facts "
            "that matter: (1) direction is right to left, always; (2) "
            "letters join except the six right-joiners ا د ذ ر ز و; (3) "
            "dots distinguish look-alikes - ب ت ث differ only in dots, "
            "as do ج ح خ and س ش and ص ض and ط ظ and ع غ and ف ق; (4) "
            "short vowels are invisible in real text, so you read by word "
            "shape plus context. Copy each letter in all its joined forms "
            "by hand until the shapes are automatic."
        ),
        "key_points": [
            "Right-to-left cursive script; 28 letters, most joining both sides.",
            "Six right-joining-only letters: ا د ذ ر ز و.",
            "Dots separate look-alike letters (ب ت ث / ج ح خ / س ش / ص ض / ط ظ / ع غ / ف ق).",
            "Short vowels (fatḥa, ḍamma, kasra) are marks, usually omitted in print.",
            "Shadda doubles a consonant; tanwīn adds an -n ending.",
            "Arabic-Indic digits ٠١٢٣٤٥٦٧٨٩ are standard in most Arab countries.",
            "Flipped punctuation: ؟ (question mark), ، (comma).",
            "Example: الكتابُ على المكتبِ (al-kitābu ʿalā l-maktabi) - the book is on the desk.",
        ],
        "requirements": [
            "Practice writing each letter in isolated, initial, medial, and final form.",
            "Memorize the six right-joiners first - they explain most word breaks.",
            "Learn the dotted pairs as pairs, not as separate letters.",
        ],
        "standards": [
            "Letter order and names follow the standard Arabic abjadi-derived teaching order.",
            "Transliteration follows ISO 233:1984 (ḥ ṣ ḍ ṭ ẓ ʿ ʾ).",
        ],
        "citations": [CIT_ISO233, CIT_RYDING],
        "sig_lens": (
            "The Signature read: the script is the sworn alphabet - 28 "
            "marks, each a sworn soldier that joins the line or stands "
            "apart by law (the six right-joiners). The Signature Language "
            "Method drills the joiners and the dotted pairs first, because "
            "the whole script surrenders once you can tell ب from ت from ث "
            "at speed."
        ),
        "drill": {
            "letters": [(ch, name) for ch, name, _ in LETTERS28],
            "tlin": LETTER_TLIN,
            "numerals": ARABIC_INDIC,
            "right_joiners": ["ا", "د", "ذ", "ر", "ز", "و"],
            "map_tests": [("باب", "bāb"), ("نار", "nār"), ("دار", "dār")],
        },
        "must_contain": ["؟", "،", "الكتابُ على المكتبِ", "ا د ذ ر ز و"],
    },
]


# ---------------------------------------------------------------- helpers

def _sent_lines(sents):
    """(arabic, translit, english) -> display lines."""
    return "\n".join("  %s (%s) — %s." % (a, t, e) for a, t, e in sents)


def _word_lines(words):
    """(arabic, translit, english) -> display lines."""
    return "\n".join("  %s (%s) — %s." % (a, t, e) for a, t, e in words)


# ---------------------------------------------------------------- record 3: phonology

PHONO_EXAMPLES = [
    ("كتاب", "kitāb", "book"), ("قلم", "qalam", "pen"),
    ("شمس", "shams", "sun"), ("قمر", "qamar", "moon"),
    ("ماء", "māʾ", "water"), ("نار", "nār", "fire"),
    ("باب", "bāb", "door"), ("نافذة", "nāfidha", "window"),
    ("مدرسة", "madrasa", "school"), ("معلم", "muʿallim", "teacher"),
    ("صديق", "ṣadīq", "friend"), ("عين", "ʿayn", "eye"),
    ("قلب", "qalb", "heart"), ("ليل", "layl", "night"),
    ("نهار", "nahār", "daytime"), ("خبز", "khubz", "bread"),
]
PHONO_EMPH = [("ص", "ṣ"), ("ض", "ḍ"), ("ط", "ṭ"), ("ظ", "ẓ")]

ENTRIES.append({
    "key": "phonology",
    "name": "Arabic Pronunciation and Phonology",
    "group": "Foundations",
    "ladder_rank": 2,
    "ladder_tier": "foundations",
    "description": (
        "Arabic has 28 consonants, three short vowels (a, i, u), and three "
        "long vowels (ā, ī, ū). The sounds English speakers must learn "
        "new are: the emphatic consonants ص ض ط ظ (ṣ ḍ ṭ ẓ), pronounced "
        "with the back of the tongue raised so neighboring vowels sound "
        "darker - compare سين (sīn, the letter s) with صاد (ṣād, the "
        "emphatic s); the voiced pharyngeal ع (ʿayn), a constriction deep "
        "in the throat with no English equivalent; the glottal stop ء "
        "(hamza, ʾ), the catch in the throat in uh-oh; ح (ḥāʾ), a "
        "breathy h from deep in the throat; خ (khāʾ), like clearing the "
        "throat; and ق (qāf), a k made far back at the uvula.\n"
        "Stress in Modern Standard Arabic falls on a long syllable if one "
        "is near the end of the word, otherwise on the third-to-last "
        "syllable: مَدْرَسة (mádrasa, school), مُعَلِّم (muʿállim, "
        "teacher), كِتاب (kitā́b, book). Intonation rises on yes-no "
        "questions and falls on statements, as in English.\n"
        "Sixteen spoken examples to train the ear (word, pronunciation, "
        "meaning):\n" + _word_lines(PHONO_EXAMPLES) + "\n"
        "Practice tip: learn ع and the emphatics by exaggerating first - "
        "whisper عين (ʿayn) until you feel the throat constrict, and say "
        "صاد (ṣād) with rounded dark lips before relaxing into normal "
        "speech."
    ),
    "how_it_works": (
        "Arabic syllables are built from consonant-vowel units, and every "
        "syllable starts with a consonant - a word never starts with a "
        "bare vowel sound (alif carries a glottal stop or a long vowel "
        "instead). Short vowels a/i/u stretch into long ā/ī/ū, and the "
        "length changes meaning: kataba (he wrote) vs kātaba (he "
        "corresponded). Emphatic consonants spread their darkness to "
        "adjacent vowels, which is why صلاة (ṣalāh, prayer) sounds "
        "completely different from سلام (salām, peace). Master the "
        "throat: ʿayn, ḥāʾ, hamza, and the uvular qāf and ghayn are the "
        "muscles English never trains."
    ),
    "key_points": [
        "28 consonants + 3 short vowels (a, i, u) + 3 long vowels (ā, ī, ū).",
        "Emphatics ص ض ط ظ (ṣ ḍ ṭ ẓ) darken neighboring vowels.",
        "ع (ʿayn) is a voiced pharyngeal constriction; ء (hamza) is a glottal stop.",
        "ح (ḥāʾ) is a deep breathy h; خ (khāʾ) is a throat-clearing fricative; ق (qāf) is uvular.",
        "Vowel length changes meaning: kataba vs kātaba.",
        "Stress: long syllable near the end wins, else third-to-last syllable.",
        "Every syllable begins with a consonant - no bare initial vowels.",
        "16 spoken example words with pronunciation and meaning above.",
    ],
    "requirements": [
        "Train ع, ح, ء, ق, خ aloud daily - throat sounds need muscle memory.",
        "Drill the emphatic/plain pairs (س/ص, ت/ط, د/ض, ذ/ظ) as minimal pairs.",
        "Shadow the 16 example words until the long vowels hold their full length.",
    ],
    "standards": [
        "Phoneme inventory per standard MSA descriptions (Ryding 2005).",
        "Transliteration follows ISO 233:1984 (ḥ ṣ ḍ ṭ ẓ ʿ ʾ).",
    ],
    "citations": [CIT_RYDING, CIT_ISO233],
    "sig_lens": (
        "The Signature read: sound is the oath spoken aloud. The "
        "Signature Language Method treats the throat letters as the "
        "proving ground - ʿayn, ḥāʾ, hamza, qāf - because a learner who "
        "commands the hard sounds commands the ear of every native "
        "speaker. Emphatics are the dark vow: ص ض ط ظ spoken with the "
        "whole mouth, not just the tongue."
    ),
    "drill": {
        "consonants": 28, "short_vowels": 3, "long_vowels": 3,
        "emphatics": [c for c, _ in PHONO_EMPH],
        "examples": PHONO_EXAMPLES,
    },
    "must_contain": ["28", "ṣ ḍ ṭ ẓ", "ʿayn", "مدرسة", "خبز"],
})

# ---------------------------------------------------------------- record 4: core nouns I

NOUNS = [
    ("رجل", "rajul", "man", "الرجلُ في البيتِ", "ar-rajulu fī l-bayti", "The man is in the house"),
    ("امرأة", "imraʾa", "woman", "المرأةُ تقرأُ الكتابَ", "al-marʾatu taqraʾu l-kitāba", "The woman reads the book"),
    ("طفل", "ṭifl", "child", "الطفلُ يلعبُ في الحديقةِ", "aṭ-ṭiflu yalʿabu fī l-ḥadīqati", "The child plays in the garden"),
    ("صديق", "ṣadīq", "friend", "صديقي من مصرَ", "ṣadīqī min miṣra", "My friend is from Egypt"),
    ("معلم", "muʿallim", "teacher", "المعلمُ يشرحُ الدرسَ", "al-muʿallimu yashraḥu d-darsa", "The teacher explains the lesson"),
    ("طبيب", "ṭabīb", "doctor", "الطبيبُ في المستشفى", "aṭ-ṭabību fī l-mustashfā", "The doctor is in the hospital"),
    ("مهندس", "muhandis", "engineer", "المهندسُ يبني الجسرَ", "al-muhandisu yabnī l-jisra", "The engineer builds the bridge"),
    ("طالب", "ṭālib", "student", "الطالبُ يدرسُ العربيةَ", "aṭ-ṭālibu yadrusu l-ʿarabiyyata", "The student studies Arabic"),
    ("عامل", "ʿāmil", "worker", "العاملُ يعملُ بجدٍّ", "al-ʿāmilu yaʿmalu bijiddin", "The worker works hard"),
    ("جار", "jār", "neighbor", "جاري رجلٌ طيبٌ", "jārī rajulun ṭayyibun", "My neighbor is a kind man"),
    ("بيت", "bayt", "house", "البيتُ كبيرٌ", "al-baytu kabīrun", "The house is big"),
    ("مدرسة", "madrasa", "school", "المدرسةُ قريبةٌ من البيتِ", "al-madrasatu qarībatun mina l-bayti", "The school is near the house"),
    ("مسجد", "masjid", "mosque", "المسجدُ في وسطِ المدينةِ", "al-masjidu fī wasaṭi l-madīnati", "The mosque is in the city center"),
    ("سوق", "sūq", "market", "السوقُ مزدحمٌ اليومَ", "as-sūqu muzdaḥimun al-yawma", "The market is crowded today"),
    ("مستشفى", "mustashfā", "hospital", "المستشفى بعيدٌ عن هنا", "al-mustashfā baʿīdun ʿan hunā", "The hospital is far from here"),
    ("مدينة", "madīna", "city", "المدينةُ جميلةٌ", "al-madīnatu jamīlatun", "The city is beautiful"),
    ("قرية", "qarya", "village", "القريةُ صغيرةٌ وهادئةٌ", "al-qaryatu ṣaghīratun wa hādiʾatun", "The village is small and quiet"),
    ("حديقة", "ḥadīqa", "garden", "الحديقةُ مليئةٌ بالزهورِ", "al-ḥadīqatu malīʾatun biz-zuhūri", "The garden is full of flowers"),
    ("شارع", "shāriʿ", "street", "الشارعُ واسعٌ ونظيفٌ", "ash-shāriʿu wāsiʿun wa naẓīfun", "The street is wide and clean"),
    ("مكتب", "maktab", "office", "مكتبي في الطابقِ الثاني", "maktabī fī ṭ-ṭābiqi th-thānī", "My office is on the second floor"),
    ("كتاب", "kitāb", "book", "هذا الكتابُ مفيدٌ", "hādhā l-kitābu mufīdun", "This book is useful"),
    ("قلم", "qalam", "pen", "القلمُ على الطاولةِ", "al-qalamu ʿalā ṭ-ṭāwilati", "The pen is on the table"),
    ("سيارة", "sayyāra", "car", "السيارةُ جديدةٌ", "as-sayyāratu jadīdatun", "The car is new"),
    ("هاتف", "hātif", "phone", "هاتفي في جيبي", "hātifī fī jaybī", "My phone is in my pocket"),
    ("ماء", "māʾ", "water", "الماءُ باردٌ", "al-māʾu bāridun", "The water is cold"),
]

ENTRIES.append({
    "key": "nouns1",
    "name": "Core Arabic Nouns I",
    "group": "Core Vocabulary",
    "ladder_rank": 2,
    "ladder_tier": "foundations",
    "description": (
        "Twenty-five essential nouns - people, places, and things - each "
        "with its transliteration, English meaning, and one full example "
        "sentence in Arabic with transliteration and translation. Learn "
        "each noun with its gender, because adjectives, verbs, and "
        "pronouns will all agree with it later. Feminine nouns usually "
        "end in ة (tāʾ marbūṭa): امرأة، مدرسة، مدينة، سيارة.\n" +
        "\n".join("  %s (%s) — %s. مثال: %s (%s) — %s." % (a, t, e, xa, xt, xe)
                  for a, t, e, xa, xt, xe in NOUNS)
    ),
    "how_it_works": (
        "Arabic nouns carry gender (masculine or feminine) and number "
        "(singular, dual, plural) as part of their identity. The "
        "definite article ال (al-) makes a noun specific: كتاب (a book) "
        "vs الكتاب (the book). Before sun letters (ت ث د ذ ر ز س ش ص ض "
        "ط ظ ل ن) the l of ال assimilates: الشمس is pronounced ash-shams, "
        "not al-shams. Plurals come in two kinds: sound plurals add a "
        "suffix (معلم → معلمون), broken plurals reshape the word (كتاب "
        "→ كتب). Learn the plural with the singular from day one."
    ),
    "key_points": [
        "25 essential nouns: 10 people, 9 places, 6 things.",
        "Every noun has grammatical gender - memorize it with the word.",
        "Feminine marker ة (tāʾ marbūṭa) on most feminine nouns.",
        "ال (al-) = the; sun letters assimilate its l (ash-shams).",
        "Three numbers: singular, dual (-ān), plural (sound or broken).",
        "Broken plurals (كتاب → كتب) must be memorized per word.",
        "Each noun above carries one full translated example sentence.",
    ],
    "requirements": [
        "Say each noun aloud with its example sentence, not alone.",
        "Mark the gender of every new noun in your notes (m/f).",
        "Learn one plural form for each noun as you meet it.",
    ],
    "standards": [
        "Vocabulary is core MSA per Hans Wehr, A Dictionary of Modern Written Arabic (1979).",
        "Transliteration follows ISO 233:1984.",
    ],
    "citations": [CIT_WEHR, CIT_RYDING],
    "sig_lens": (
        "The Signature read: nouns are the named things of the world, "
        "and naming is the first covenant. The Signature Language Method "
        "files every noun under gender and plural the way the armory "
        "files every part under its ratings - no noun enters the "
        "vocabulary without its papers: its gender, its plural, its "
        "sentence."
    ),
    "drill": {"items": NOUNS, "count": 25},
    "must_contain": [w[0] for w in NOUNS],
})

# ---------------------------------------------------------------- record 5: core verbs I

VERBS = [
    ("كتب", "kataba", "to write", "كتبَ الطالبُ الدرسَ", "kataba ṭ-ṭālibu d-darsa", "The student wrote the lesson"),
    ("قرأ", "qaraʾa", "to read", "قرأتُ الكتابَ أمسِ", "qaraʾtu l-kitāba amsi", "I read the book yesterday"),
    ("ذهب", "dhahaba", "to go", "ذهبَ إلى المدرسةِ صباحاً", "dhahaba ilā l-madrasati ṣabāḥan", "He went to school in the morning"),
    ("جاء", "jāʾa", "to come", "جاءَ صديقي لزيارتي", "jāʾa ṣadīqī liziyāratī", "My friend came to visit me"),
    ("أكل", "akala", "to eat", "أكلنا العشاءَ معاً", "akalnā l-ʿashāʾa maʿan", "We ate dinner together"),
    ("شرب", "shariba", "to drink", "شربتُ كوباً من الشايِ", "sharibtu kūban mina sh-shāyi", "I drank a cup of tea"),
    ("نام", "nāma", "to sleep", "نامَ الطفلُ مبكراً", "nāma ṭ-ṭiflu mubakkiran", "The child slept early"),
    ("استيقظ", "istayqaẓa", "to wake up", "استيقظتُ في السادسةِ صباحاً", "istayqaẓtu fī s-sādisati ṣabāḥan", "I woke up at six in the morning"),
    ("عمل", "ʿamila", "to work", "يعملُ أبي في شركةٍ كبيرةٍ", "yaʿmalu abī fī sharīkatin kabīratin", "My father works in a big company"),
    ("درس", "darasa", "to study", "تدرسُ أختي الطبَّ", "tadrusu ukhtī ṭ-ṭibba", "My sister studies medicine"),
    ("علّم", "ʿallama", "to teach", "يعلّمُ المعلمُ الأطفالَ القراءةَ", "yuʿallimu l-muʿallimu l-aṭfāla l-qirāʾata", "The teacher teaches the children reading"),
    ("تكلّم", "takallama", "to speak", "تكلّمَ معي بالعربيةِ", "takallama maʿī bil-ʿarabiyyati", "He spoke with me in Arabic"),
    ("سمع", "samiʿa", "to hear", "سمعتُ صوتاً غريباً", "samiʿtu ṣawtan gharīban", "I heard a strange sound"),
    ("رأى", "raʾā", "to see", "رأيتُ فيلماً جميلاً", "raʾaytu filman jamīlan", "I saw a beautiful film"),
    ("أحبّ", "aḥabba", "to love", "أحبُّ القراءةَ كثيراً", "uḥibbu l-qirāʾata kathīran", "I love reading a lot"),
    ("لعب", "laʿiba", "to play", "يلعبُ الأولادُ كرةَ القدمِ", "yalʿabu l-awlādu kurata l-qadami", "The boys play football"),
    ("مشى", "mashā", "to walk", "مشيتُ إلى السوقِ", "mashaytu ilā s-sūqi", "I walked to the market"),
    ("ركض", "rakaḍa", "to run", "ركضَ اللاعبُ بسرعةٍ", "rakaḍa l-lāʿibu bisurʿatin", "The player ran quickly"),
    ("جلس", "jalasa", "to sit", "جلسنا تحتَ الشجرةِ", "jalasnā taḥta sh-shajarati", "We sat under the tree"),
    ("وقف", "waqafa", "to stand", "وقفَ الرجلُ أمامَ البابِ", "waqafa r-rajulu amāma l-bābi", "The man stood in front of the door"),
    ("فتح", "fataḥa", "to open", "فتحتُ النافذةَ", "fataḥtu n-nāfidhata", "I opened the window"),
    ("أغلق", "aghlaqa", "to close", "أغلقَ المحلُّ أبوابَهُ", "aghlaqa l-maḥallu abwābahu", "The shop closed its doors"),
    ("اشترى", "ishtarā", "to buy", "اشتريتُ قميصاً جديداً", "ishtaraytu qamīṣan jadīdan", "I bought a new shirt"),
    ("باع", "bāʿa", "to sell", "باعَ التاجرُ بضاعتَهُ", "bāʿa t-tājiru biḍāʿatahu", "The merchant sold his goods"),
    ("ساعد", "sāʿada", "to help", "ساعدتُ أمي في المطبخِ", "sāʿadtu ummī fī l-maṭbakhi", "I helped my mother in the kitchen"),
]

ENTRIES.append({
    "key": "verbs1",
    "name": "Core Arabic Verbs I",
    "group": "Core Vocabulary",
    "ladder_rank": 2,
    "ladder_tier": "foundations",
    "description": (
        "Twenty-five essential verbs, each shown in its dictionary form "
        "(third-person masculine singular past, e.g. كتبَ kataba, he "
        "wrote), with transliteration, English meaning, and one full "
        "example sentence in Arabic with transliteration and translation. "
        "Arabic verbs conjugate for person, gender, and number - one verb "
        "form already says who did it, so pronouns are often dropped.\n" +
        "\n".join("  %s (%s) — %s. مثال: %s (%s) — %s." % (a, t, e, xa, xt, xe)
                  for a, t, e, xa, xt, xe in VERBS)
    ),
    "how_it_works": (
        "The dictionary form of an Arabic verb is the past tense "
        "he-form: kataba (he wrote). To say I wrote, change the ending: "
        "katabtu (كتبتُ). The past tense is built with suffixes on the "
        "stem: -tu (I), -ta (you m), -ti (you f), -a (he), -at (she), -nā "
        "(we), -tum (you pl), -ū (they m), -na (they f). The present "
        "tense instead uses prefixes: ya-ktub-u (he writes), ta-ktub-u "
        "(she writes / you m write), a-ktub-u (I write), na-ktub-u (we "
        "write). Learn the two stems - past stem and present stem - and "
        "the whole conjugation table follows."
    ),
    "key_points": [
        "25 essential verbs with one full translated example sentence each.",
        "Dictionary form = he-past (kataba = he wrote).",
        "Past tense: suffixes on the stem (-tu, -ta, -ti, -a, -at, -nā, -tum, -ū, -na).",
        "Present tense: prefixes (ya-, ta-, a-, na-) + suffixes.",
        "Verb forms encode person/gender/number - pronouns often dropped.",
        "Two stems per verb (past, present) unlock the full table.",
        "Example: كتبَ الطالبُ الدرسَ (kataba ṭ-ṭālibu d-darsa) - the student wrote the lesson.",
    ],
    "requirements": [
        "Recite each verb in he-past, I-past, and he-present forms aloud.",
        "Write the example sentences by hand to train verb-subject order.",
        "Group verbs by their present-tense vowel (yaktub-u vs yafʿal-u patterns).",
    ],
    "standards": [
        "Conjugation tables per Wright 1896 and Ryding 2005.",
        "Vocabulary is core MSA per Hans Wehr (1979).",
    ],
    "citations": [CIT_WRIGHT, CIT_WEHR],
    "sig_lens": (
        "The Signature read: verbs are the actions of the covenant - "
        "every verb a sworn deed with its doer sealed into the ending. "
        "The Signature Language Method drills the two stems of each verb "
        "like the two edges of a blade: past stem, present stem. Hold "
        "both and the whole conjugation table is yours."
    ),
    "drill": {
        "items": VERBS, "count": 25,
        "root": ("ك", "ت", "ب"),
        "past_suffixes": ["تُ", "تَ", "تِ", "", "تْ", "نَا", "تُم", "وا", "نَ"],
        "past_persons": ["I", "you-m", "you-f", "he", "she", "we", "you-pl", "they-m", "they-f"],
        "past_spot": {"I": "كتبتُ", "he": "كتب", "she": "كتبت", "we": "كتبنا", "they-m": "كتبوا"},
    },
    "must_contain": [w[0] for w in VERBS],
})

# ---------------------------------------------------------------- record 6: adjectives & adverbs

ADJECTIVES = [
    ("كبير", "kabīr", "big", "كبيرة", "بيتٌ كبيرٌ", "baytun kabīrun", "a big house"),
    ("صغير", "ṣaghīr", "small", "صغيرة", "قطةٌ صغيرةٌ", "qiṭṭatun ṣaghīratun", "a small cat"),
    ("طويل", "ṭawīl", "tall", "طويلة", "رجلٌ طويلٌ", "rajulun ṭawīlun", "a tall man"),
    ("قصير", "qaṣīr", "short", "قصيرة", "قصةٌ قصيرةٌ", "qiṣṣatun qaṣīratun", "a short story"),
    ("جديد", "jadīd", "new", "جديدة", "سيارةٌ جديدةٌ", "sayyāratun jadīdatun", "a new car"),
    ("قديم", "qadīm", "old", "قديمة", "مدينةٌ قديمةٌ", "madīnatun qadīmatun", "an old city"),
    ("جميل", "jamīl", "beautiful", "جميلة", "زهرةٌ جميلةٌ", "zahratun jamīlatun", "a beautiful flower"),
    ("قبيح", "qabīḥ", "ugly", "قبيحة", "منظرٌ قبيحٌ", "manẓarun qabīḥun", "an ugly sight"),
    ("سعيد", "saʿīd", "happy", "سعيدة", "طفلٌ سعيدٌ", "ṭiflun saʿīdun", "a happy child"),
    ("حزين", "ḥazīn", "sad", "حزينة", "خبرٌ حزينٌ", "khabarun ḥazīnun", "sad news"),
    ("سريع", "sarīʿ", "fast", "سريعة", "قطارٌ سريعٌ", "qiṭārun sarīʿun", "a fast train"),
    ("بطيء", "baṭīʾ", "slow", "بطيئة", "سلحفاةٌ بطيئةٌ", "sulḥafātun baṭīʾatun", "a slow turtle"),
    ("قوي", "qawiyy", "strong", "قوية", "رجلٌ قويٌّ", "rajulun qawiyyun", "a strong man"),
    ("ضعيف", "ḍaʿīf", "weak", "ضعيفة", "حجةٌ ضعيفةٌ", "ḥujjatun ḍaʿīfatun", "a weak argument"),
    ("غني", "ghaniyy", "rich", "غنية", "تاجرٌ غنيٌّ", "tājirun ghaniyyun", "a rich merchant"),
    ("فقير", "faqīr", "poor", "فقيرة", "أسرةٌ فقيرةٌ", "usratun faqīratun", "a poor family"),
    ("حارّ", "ḥārr", "hot", "حارّة", "شايٌ حارٌّ", "shāyun ḥārrun", "hot tea"),
    ("بارد", "bārid", "cold", "باردة", "ماءٌ باردٌ", "māʾun bāridun", "cold water"),
    ("سهل", "sahl", "easy", "سهلة", "درسٌ سهلٌ", "darsun sahlun", "an easy lesson"),
    ("صعب", "ṣaʿb", "difficult", "صعبة", "مسألةٌ صعبةٌ", "masʾalatun ṣaʿbatun", "a difficult problem"),
    ("قريب", "qarīb", "near", "قريبة", "المدرسةُ قريبةٌ", "al-madrasatu qarībatun", "The school is near"),
    ("بعيد", "baʿīd", "far", "بعيدة", "القريةُ بعيدةٌ", "al-qaryatu baʿīdatun", "The village is far"),
    ("نظيف", "naẓīf", "clean", "نظيفة", "غرفةٌ نظيفةٌ", "ghurfatun naẓīfatun", "a clean room"),
    ("وسخ", "wasikh", "dirty", "وسخة", "ثوبٌ وسخٌ", "thawbun wasikhun", "a dirty garment"),
    ("ذكي", "dhakiyy", "smart", "ذكية", "تلميذٌ ذكيٌّ", "tilmīdhun dhakiyyun", "a smart pupil"),
]
ADVERBS = [
    ("بسرعة", "bisurʿa", "quickly", "يجري بسرعةٍ", "yajrī bisurʿatin", "He runs quickly"),
    ("ببطء", "bibuṭʾ", "slowly", "يمشي ببطءٍ", "yamshī bibuṭʾin", "He walks slowly"),
    ("جيداً", "jayyidan", "well", "يتكلمُ العربيةَ جيداً", "yatakallamu l-ʿarabiyyata jayyidan", "He speaks Arabic well"),
    ("دائماً", "dāʾiman", "always", "هو دائماً سعيدٌ", "huwa dāʾiman saʿīdun", "He is always happy"),
    ("أبداً", "abadan", "never", "لا أكذبُ أبداً", "lā akdhibu abadan", "I never lie"),
    ("أحياناً", "aḥyānan", "sometimes", "أحياناً أزورُ جدتي", "aḥyānan azūru jaddatī", "Sometimes I visit my grandmother"),
    ("اليوم", "al-yawm", "today", "اليومَ الجوُّ جميلٌ", "al-yawma l-jawwu jamīlun", "Today the weather is beautiful"),
    ("غداً", "ghadan", "tomorrow", "سأسافرُ غداً", "saʾusāfiru ghadan", "I will travel tomorrow"),
    ("أمسِ", "amsi", "yesterday", "وصلَ أمسِ", "waṣala amsi", "He arrived yesterday"),
    ("هنا", "hunā", "here", "اجلسْ هنا", "ijlis hunā", "Sit here"),
    ("هناك", "hunāka", "there", "الكتابُ هناك", "al-kitābu hunāka", "The book is there"),
    ("كثيراً", "kathīran", "a lot", "أحبُّها كثيراً", "uḥibbuhā kathīran", "I love it a lot"),
    ("قليلاً", "qalīlan", "a little", "انتظرْ قليلاً", "intaẓir qalīlan", "Wait a little"),
    ("معاً", "maʿan", "together", "نعملُ معاً", "naʿmalu maʿan", "We work together"),
    ("وحده", "waḥdahu", "alone", "يعيشُ وحده", "yaʿīshu waḥdahu", "He lives alone"),
]

ENTRIES.append({
    "key": "adjadv",
    "name": "Arabic Adjectives and Adverbs",
    "group": "Core Vocabulary",
    "ladder_rank": 3,
    "ladder_tier": "foundations",
    "description": (
        "Twenty-five adjectives and fifteen adverbs with example "
        "sentences. The golden rule: the adjective follows the noun and "
        "agrees with it in gender, number, and definiteness. Masculine "
        "كبير becomes feminine كبيرة by adding ة; a definite noun takes "
        "a definite adjective: بيتٌ كبيرٌ (a big house) vs البيتُ الكبيرُ "
        "(the big house). Adverbs of manner often use the accusative "
        "ending: سريع (fast) → بسرعةٍ (quickly) or سريعاً.\n"
        "Adjectives (masculine — feminine):\n" +
        "\n".join("  %s (%s) — %s — %s. مثال: %s (%s) — %s." % (a, t, e, f, xa, xt, xe)
                  for a, t, e, f, xa, xt, xe in ADJECTIVES) +
        "\nAdverbs:\n" +
        "\n".join("  %s (%s) — %s. مثال: %s (%s) — %s." % (a, t, e, xa, xt, xe)
                  for a, t, e, xa, xt, xe in ADVERBS)
    ),
    "how_it_works": (
        "Agreement is the engine of Arabic description. Take the noun "
        "بيت (house, masculine): indefinite big house is بيتٌ كبيرٌ, "
        "definite the big house is البيتُ الكبيرُ - the adjective copies "
        "the noun's definiteness. Feminine nouns take the ة form: سيارةٌ "
        "جديدةٌ (a new car). Plural nouns take plural adjectives, except "
        "non-human plurals, which take the feminine singular: كتبٌ جديدةٌ "
        "(new books) - literally new (feminine singular) books. This "
        "last rule surprises every learner once and then becomes "
        "automatic."
    ),
    "key_points": [
        "25 adjectives + 15 adverbs, each with a translated example sentence.",
        "Adjective follows the noun and agrees in gender, number, definiteness.",
        "Feminine = masculine + ة (kabīr → kabīra).",
        "Definite noun → definite adjective: البيتُ الكبيرُ (the big house).",
        "Non-human plurals take feminine-singular adjectives: كتبٌ جديدةٌ.",
        "Manner adverbs: بِ + noun (بسرعةٍ) or accusative -اً (سريعاً).",
        "Time/place adverbs (اليوم، هنا) are fixed words - just memorize them.",
    ],
    "requirements": [
        "For each adjective, write it with a masculine noun, a feminine noun, and definite.",
        "Drill the non-human plural rule with 10 plural nouns.",
        "Use five adverbs in your own sentences about your day.",
    ],
    "standards": [
        "Agreement rules per Wright 1896; Ryding 2005.",
        "Vocabulary is core MSA per Hans Wehr (1979).",
    ],
    "citations": [CIT_WRIGHT, CIT_RYDING, CIT_WEHR],
    "sig_lens": (
        "The Signature read: the adjective is the sworn witness - it "
        "stands behind the noun and testifies in the same uniform: same "
        "gender, same number, same definiteness. The Signature Language "
        "Method never lets an adjective march out of step. Non-human "
        "plurals bowing to the feminine singular is the covenant's "
        "oldest courtesy - learn it as law, not exception."
    ),
    "drill": {"adjectives": ADJECTIVES, "adverbs": ADVERBS,
              "adj_count": 25, "adv_count": 15},
    "must_contain": [w[0] for w in ADJECTIVES] + [w[0] for w in ADVERBS],
})

# ---------------------------------------------------------------- record 7: pronouns

PRON_PERSONAL = [
    ("أنا", "anā", "I"), ("نحن", "naḥnu", "we"),
    ("أنتَ", "anta", "you (m)"), ("أنتِ", "anti", "you (f)"),
    ("أنتما", "antumā", "you (dual)"), ("أنتم", "antum", "you (m pl)"),
    ("أنتنَّ", "antunna", "you (f pl)"), ("هو", "huwa", "he"),
    ("هي", "hiya", "she"), ("هما", "humā", "they (dual)"),
    ("هم", "hum", "they (m)"), ("هنَّ", "hunna", "they (f)"),
]
PRON_POSSESSIVE = [
    ("كتابي", "kitābī", "my book"), ("كتابُكَ", "kitābuka", "your (m) book"),
    ("كتابُكِ", "kitābuki", "your (f) book"), ("كتابُهُ", "kitābuhu", "his book"),
    ("كتابُها", "kitābuhā", "her book"), ("كتابُنا", "kitābunā", "our book"),
    ("كتابُكم", "kitābukum", "your (pl) book"), ("كتابُهم", "kitābuhum", "their book"),
]
PRON_DEMONST = [
    ("هذا", "hādhā", "this (m)", "هذا كتابٌ", "hādhā kitābun", "This is a book"),
    ("هذه", "hādhihi", "this (f)", "هذه سيارةٌ", "hādhihi sayyāratun", "This is a car"),
    ("هؤلاء", "hāʾulāʾi", "these", "هؤلاء أصدقائي", "hāʾulāʾi aṣdiqāʾī", "These are my friends"),
    ("ذلك", "dhālika", "that (m)", "ذلك بيتُنا", "dhālika baytunā", "That is our house"),
    ("تلك", "tilka", "that (f)", "تلك مدرستي", "tilka madrasatī", "That is my school"),
    ("أولئك", "ulāʾika", "those", "أولئك الطلابُ مجتهدون", "ulāʾika ṭ-ṭullābu mujtahidūn", "Those students are hardworking"),
]
PRON_INTERROG = [
    ("من", "man", "who", "من هذا؟", "man hādhā؟", "Who is this"),
    ("ما", "mā", "what", "ما هذا؟", "mā hādhā؟", "What is this"),
    ("ماذا", "mādhā", "what", "ماذا تريد؟", "mādhā turīd؟", "What do you want"),
    ("أين", "ayna", "where", "أين المدرسة؟", "ayna l-madrasa؟", "Where is the school"),
    ("متى", "matā", "when", "متى تسافر؟", "matā tusāfir؟", "When do you travel"),
    ("لماذا", "limādhā", "why", "لماذا تبكي؟", "limādhā tabkī؟", "Why are you crying"),
    ("كيف", "kayfa", "how", "كيف حالك؟", "kayfa ḥāluk؟", "How are you"),
    ("كم", "kam", "how many", "كم عمرك؟", "kam ʿumruk؟", "How old are you"),
]

ENTRIES.append({
    "key": "pronouns",
    "name": "Arabic Pronouns",
    "group": "Core Vocabulary",
    "ladder_rank": 3,
    "ladder_tier": "foundations",
    "description": (
        "The full pronoun system: 12 personal pronouns, 8 possessive "
        "suffixes, 6 demonstratives, and 8 interrogatives - each with "
        "transliteration, English, and example sentences where they carry "
        "meaning.\n"
        "Personal pronouns (used for emphasis or clarity; verbs already "
        "mark the person):\n" + _word_lines(PRON_PERSONAL) + "\n"
        "Possessive suffixes attach to nouns - here on كتاب (book):\n" +
        _word_lines(PRON_POSSESSIVE) + "\n"
        "Demonstratives (this/that/these/those):\n" +
        "\n".join("  %s (%s) — %s. مثال: %s (%s) — %s." % (a, t, e, xa, xt, xe)
                  for a, t, e, xa, xt, xe in PRON_DEMONST) + "\n"
        "Interrogatives (question words):\n" +
        "\n".join("  %s (%s) — %s. مثال: %s (%s) — %s." % (a, t, e, xa, xt, xe)
                  for a, t, e, xa, xt, xe in PRON_INTERROG) + "\n"
        "Note the dual forms (أنتما، هما): Arabic has a dedicated number "
        "for exactly two of anything - one of its most distinctive "
        "features."
    ),
    "how_it_works": (
        "Pronouns in Arabic are often suffixes, not separate words. "
        "Possession glues onto the noun: kitāb + ī = kitābī (my book). "
        "Object pronouns glue onto verbs: raʾaytu + hu = raʾaytuhu (I "
        "saw him). Prepositions take them too: maʿa + ka = maʿaka (with "
        "you). The standalone personal pronouns (anā, anta, huwa...) "
        "appear for emphasis or when no verb carries the person - أنا "
        "طالب (I am a student) needs أنا because there is no verb at "
        "all. Demonstratives agree in gender with the noun they point "
        "at: هذا كتاب (this [m] book) vs هذه سيارة (this [f] car)."
    ),
    "key_points": [
        "12 personal pronouns across person, gender, and number (incl. dual).",
        "Possessive/object suffixes attach to nouns, verbs, and prepositions.",
        "Demonstratives: هذا/هذه (this), هؤلاء (these), ذلك/تلك (that), أولئك (those).",
        "8 interrogatives: من ما ماذا أين متى لماذا كيف كم.",
        "Standalone pronouns appear for emphasis or with no verb (أنا طالب).",
        "The dual (two of something) has its own pronoun forms.",
        "Suffix pronouns: -ī my, -ka your (m), -ki your (f), -hu his, -hā her, -nā our.",
    ],
    "requirements": [
        "Recite the 12 personal pronouns in order until automatic.",
        "Attach possessive suffixes to بيت، سيارة، صديق from memory.",
        "Ask and answer 10 questions using each interrogative once.",
    ],
    "standards": [
        "Paradigms per Wright 1896; Ryding 2005.",
        "Dual and pronoun forms are standard MSA.",
    ],
    "citations": [CIT_WRIGHT, CIT_RYDING],
    "sig_lens": (
        "The Signature read: pronouns are the sworn stand-ins - small "
        "words that carry the weight of the person. The Signature "
        "Language Method drills the suffixes as bindings: -ī binds to "
        "me, -ka binds to you, -hu binds to him. Nothing dangles; every "
        "person is attached. The dual is honored, never skipped: two is "
        "its own number in the covenant."
    ),
    "drill": {
        "personal": PRON_PERSONAL, "possessive": PRON_POSSESSIVE,
        "demonstrative": PRON_DEMONST, "interrogative": PRON_INTERROG,
        "counts": (12, 8, 6, 8),
    },
    "must_contain": ["أنتما", "هما", "كتابُكم", "أولئك", "لماذا"],
})

# ---------------------------------------------------------------- record 8: numbers & time

NUM_1_10 = [
    ("واحد", "wāḥid", "1"), ("اثنان", "ithnān", "2"), ("ثلاثة", "thalātha", "3"),
    ("أربعة", "arbaʿa", "4"), ("خمسة", "khamsa", "5"), ("ستة", "sitta", "6"),
    ("سبعة", "sabʿa", "7"), ("ثمانية", "thamāniya", "8"), ("تسعة", "tisʿa", "9"),
    ("عشرة", "ʿashara", "10"),
]
NUM_11_19 = [
    ("أحد عشر", "aḥada ʿashar", "11"), ("اثنا عشر", "ithnā ʿashar", "12"),
    ("ثلاثة عشر", "thalāthata ʿashar", "13"), ("أربعة عشر", "arbaʿata ʿashar", "14"),
    ("خمسة عشر", "khamsata ʿashar", "15"), ("ستة عشر", "sittata ʿashar", "16"),
    ("سبعة عشر", "sabʿata ʿashar", "17"), ("ثمانية عشر", "thamāniyata ʿashar", "18"),
    ("تسعة عشر", "tisʿata ʿashar", "19"),
]
NUM_TENS = [
    ("عشرون", "ʿishrūn", "20"), ("ثلاثون", "thalāthūn", "30"),
    ("أربعون", "arbaʿūn", "40"), ("خمسون", "khamsūn", "50"),
    ("ستون", "sittūn", "60"), ("سبعون", "sabʿūn", "70"),
    ("ثمانون", "thamānūn", "80"), ("تسعون", "tisʿūn", "90"),
    ("مائة", "miʾa", "100"), ("ألف", "alf", "1000"),
]
NUM_ORDINAL = [
    ("الأول", "al-awwal", "1st"), ("الثاني", "ath-thānī", "2nd"),
    ("الثالث", "ath-thālith", "3rd"), ("الرابع", "ar-rābiʿ", "4th"),
    ("الخامس", "al-khāmis", "5th"), ("السادس", "as-sādis", "6th"),
    ("السابع", "as-sābiʿ", "7th"), ("الثامن", "ath-thāmin", "8th"),
    ("التاسع", "at-tāsiʿ", "9th"), ("العاشر", "al-ʿāshir", "10th"),
]
NUM_DAYS = [
    ("الأحد", "al-aḥad", "Sunday"), ("الاثنين", "al-ithnayn", "Monday"),
    ("الثلاثاء", "ath-thulāthāʾ", "Tuesday"), ("الأربعاء", "al-arbiʿāʾ", "Wednesday"),
    ("الخميس", "al-khamīs", "Thursday"), ("الجمعة", "al-jumuʿa", "Friday"),
    ("السبت", "as-sabt", "Saturday"),
]
NUM_MONTHS = [
    ("يناير", "yanāyir", "January"), ("فبراير", "fibrāyir", "February"),
    ("مارس", "māris", "March"), ("أبريل", "ibrīl", "April"),
    ("مايو", "māyū", "May"), ("يونيو", "yūnyū", "June"),
    ("يوليو", "yūlyū", "July"), ("أغسطس", "aghusṭus", "August"),
    ("سبتمبر", "sibtambar", "September"), ("أكتوبر", "uktūbar", "October"),
    ("نوفمبر", "nūfambar", "November"), ("ديسمبر", "dīsambar", "December"),
]
NUM_SEASONS = [
    ("الربيع", "ar-rabīʿ", "spring"), ("الصيف", "aṣ-ṣayf", "summer"),
    ("الخريف", "al-kharīf", "autumn"), ("الشتاء", "ash-shitāʾ", "winter"),
]
NUM_SENTENCES = [
    ("عندي ثلاثةُ كتبٍ", "ʿindī thalāthatu kutubin", "I have three books"),
    ("اليومُ الاثنين", "al-yawmu l-ithnayn", "Today is Monday"),
    ("عيدُ ميلادي في مارس", "ʿīdu mīlādī fī māris", "My birthday is in March"),
    ("الساعةُ الخامسةُ مساءً", "as-sāʿatu l-khāmisatu masāʾan", "It is five in the evening"),
    ("الصفُّ الأولُ كبيرٌ", "aṣ-ṣaffu l-awwalu kabīrun", "The first class is big"),
    ("في الصيفِ الجوُّ حارٌّ", "fī ṣ-ṣayfi l-jawwu ḥārrun", "In summer the weather is hot"),
]

ENTRIES.append({
    "key": "numbers",
    "name": "Arabic Numbers and Time",
    "group": "Core Vocabulary",
    "ladder_rank": 3,
    "ladder_tier": "foundations",
    "description": (
        "Numbers 1-100, ordinals, days, months, seasons, clock time, and "
        "dates - each with transliteration and example sentences. "
        "Cardinals 1-10:\n" + _word_lines(NUM_1_10) + "\n"
        "Eleven to nineteen:\n" + _word_lines(NUM_11_19) + "\n"
        "Tens, hundred, thousand:\n" + _word_lines(NUM_TENS) + "\n"
        "Ordinals 1st-10th:\n" + _word_lines(NUM_ORDINAL) + "\n"
        "Days of the week (the week starts Sunday in most Arab "
        "countries):\n" + _word_lines(NUM_DAYS) + "\n"
        "Months (Gregorian names used in Egypt, the Levant, and Iraq; "
        "the Gulf often uses كانون الثاني/شباط-style names):\n" +
        _word_lines(NUM_MONTHS) + "\n"
        "Seasons:\n" + _word_lines(NUM_SEASONS) + "\n"
        "Clock time uses الساعة (hour) + ordinal: الساعةُ الواحدةُ "
        "(one o'clock), الساعةُ الثالثةُ والنصفُ (half past three). "
        "Example sentences:\n" + _sent_lines(NUM_SENTENCES) + "\n"
        "Note the famous gender polarity of 3-10: masculine nouns take "
        "the feminine-looking number (ثلاثةُ كتبٍ, three books) and "
        "feminine nouns take the plain form (ثلاثُ سياراتٍ, three cars)."
    ),
    "how_it_works": (
        "Arabic numbers are a small machine with three gears. Gear one: "
        "1 and 2 agree with the noun like adjectives (كتابٌ واحدٌ, one "
        "book). Gear two: 3-10 show gender polarity - the number takes "
        "the opposite gender of the noun, and the noun goes plural "
        "(ثلاثةُ كتبٍ). Gear three: 11-99 put the noun in singular "
        "(عشرون كتاباً, twenty books - book stays singular). Ordinals "
        "behave like normal adjectives: الصفُّ الأولُ (the first class). "
        "Days are mostly numbered (الأحد = the first, الاثنين = the "
        "second) except Friday (الجمعة, gathering) and Saturday "
        "(السبت, sabbath)."
    ),
    "key_points": [
        "Cardinals 1-100 above, each with transliteration.",
        "Gender polarity 3-10: number takes the opposite gender of the noun.",
        "1-2 agree like adjectives; 11-99 take a singular noun.",
        "Ordinals 1st-10th behave as adjectives (الأول، الثاني...).",
        "7 days, 12 months, 4 seasons - listed with transliteration.",
        "Clock: الساعة + ordinal (الساعةُ الخامسةُ = five o'clock).",
        "Arabic-Indic digits ٠١٢٣٤٥٦٧٨٩ in daily writing.",
        "6 example sentences covering numbers, days, months, and clock time.",
    ],
    "requirements": [
        "Count aloud 1-20 forward and backward daily for a week.",
        "Write the date in Arabic every day (day, date, month).",
        "Tell the time in Arabic whenever you check a clock.",
    ],
    "standards": [
        "Number grammar per Wright 1896; Ryding 2005.",
        "Month names are the standard Gregorian forms used in Egypt/Levant/Iraq.",
    ],
    "citations": [CIT_WRIGHT, CIT_RYDING],
    "sig_lens": (
        "The Signature read: numbers are the sworn counters - exact, "
        "unyielding, and honest. The Signature Language Method drills "
        "the polarity rule as a law of opposites: three through ten "
        "always face the other way. A learner who can count to one "
        "hundred, name the seven days, and tell the hour holds the keys "
        "to every market, station, and appointment in the Arab world."
    ),
    "drill": {
        "n1_10": NUM_1_10, "n11_19": NUM_11_19, "tens": NUM_TENS,
        "ordinals": NUM_ORDINAL, "days": NUM_DAYS, "months": NUM_MONTHS,
        "seasons": NUM_SEASONS, "sentences": NUM_SENTENCES,
        "indic": ARABIC_INDIC,
    },
    "must_contain": ["اثنا عشر", "تسعون", "العاشر", "الجمعة", "ديسمبر", "الشتاء", "الساعةُ الخامسةُ مساءً"],
})

# ---------------------------------------------------------------- record 9: greetings

GREETINGS = [
    ("السلام عليكم", "as-salāmu ʿalaykum", "Peace be upon you", "greeting", "The universal Muslim-world greeting; used by all Arabic speakers"),
    ("وعليكم السلام", "wa ʿalaykumu s-salām", "And peace be upon you", "greeting", "The required reply to السلام عليكم"),
    ("صباح الخير", "ṣabāḥ al-khayr", "Good morning", "greeting", "Used until around noon"),
    ("صباح النور", "ṣabāḥ an-nūr", "Morning of light", "greeting", "The classic reply to صباح الخير"),
    ("مساء الخير", "masāʾ al-khayr", "Good evening", "greeting", "Used from late afternoon on"),
    ("مساء النور", "masāʾ an-nūr", "Evening of light", "greeting", "The classic reply to مساء الخير"),
    ("أهلاً وسهلاً", "ahlan wa sahlan", "Welcome", "greeting", "Warm welcome to a guest; literally be at ease"),
    ("مرحباً", "marḥaban", "Hello", "greeting", "Neutral hello, any time of day"),
    ("كيف حالك؟", "kayfa ḥāluk/a؟", "How are you", "greeting", "Use حالكَ to a man, حالكِ to a woman"),
    ("بخير، الحمد لله", "bikhayr, al-ḥamdu lillāh", "Fine, praise God", "greeting", "The standard well-mannered answer"),
    ("كيف الحال؟", "kayfa l-ḥāl؟", "How is it going", "greeting", "Casual check-in between friends"),
    ("أهلاً بك", "ahlan bik/a", "Welcome to you", "greeting", "Personal welcome; بكَ to a man, بكِ to a woman"),
    ("تشرفت بمعرفتك", "tasharraftu bimaʿrifatik", "Pleased to meet you", "greeting", "Said when introduced to someone"),
    ("الحمد لله على السلامة", "al-ḥamdu lillāh ʿalā s-salāma", "Praise God for your safe arrival", "greeting", "Said to a traveler who just arrived"),
    ("مع السلامة", "maʿa s-salāma", "Goodbye (go with safety)", "farewell", "Said to someone who is leaving"),
    ("في أمان الله", "fī amān Allāh", "In Gods safekeeping", "farewell", "Warm farewell, literally in the safety of God"),
    ("إلى اللقاء", "ilā l-liqāʾ", "See you later", "farewell", "Neutral see-you-later"),
    ("تصبح على خير", "tuṣbiḥ ʿalā khayr", "Good night", "farewell", "Said in the evening; reply وأنت من أهله"),
    ("شكراً", "shukran", "Thank you", "politeness", "The everyday thanks"),
    ("شكراً جزيلاً", "shukran jazīlan", "Thank you very much", "politeness", "Stronger thanks"),
    ("عفواً", "ʿafwan", "You are welcome / excuse me", "politeness", "Reply to thanks; also excuse me when passing"),
    ("من فضلك", "min faḍlik/a", "Please", "politeness", "Softens any request"),
    ("لو سمحت", "law samaḥt", "Excuse me / please", "politeness", "Getting attention politely; if you permit"),
    ("آسف", "āsif", "Sorry", "politeness", "Apology; آسفة (āsifa) for a female speaker"),
    ("لا بأس", "lā baʾs", "No problem", "politeness", "Dismissing an apology or a worry"),
    ("تفضل", "tafaḍḍal", "Please come in / here you are", "politeness", "Inviting someone in or offering something"),
    ("بارك الله فيك", "bāraka llāhu fīk", "God bless you", "politeness", "Thanks with warmth; said for a favor"),
    ("جزاك الله خيراً", "jazāka llāhu khayran", "May God reward you with good", "politeness", "Deep thanks for real help"),
    ("إن شاء الله", "in shāʾa llāh", "God willing", "politeness", "Said for any future plan - obligatory politeness"),
    ("ما شاء الله", "mā shāʾa llāh", "As God willed", "politeness", "Said in admiration; wards off the evil eye"),
]

ENTRIES.append({
    "key": "greetings",
    "name": "Arabic Greetings and Everyday Phrases",
    "group": "Core Vocabulary",
    "ladder_rank": 4,
    "ladder_tier": "foundations",
    "description": (
        "Thirty greetings, farewells, and politeness phrases - the "
        "social survival kit. Each carries transliteration, English, "
        "category, and a usage note, because in Arabic the wrong "
        "greeting at the wrong time is a real social error.\n" +
        "\n".join("  %s (%s) — %s [%s]. %s." % (a, t, e, c, n)
                  for a, t, e, c, n in GREETINGS) + "\n"
        "Master the pairs: greeting and reply belong together - صباح "
        "الخير demands صباح النور, السلام عليكم demands وعليكم السلام. "
        "Politeness phrases (من فضلك، لو سمحت، شكراً، عفواً) oil every "
        "transaction; religiously-flavored phrases (إن شاء الله، ما شاء "
        "الله، الحمد لله) are everyday speech for all Arabic speakers, "
        "used constantly in secular contexts too."
    ),
    "how_it_works": (
        "Arabic greetings run on reciprocity. Nearly every greeting has "
        "a fixed reply, and returning it is socially mandatory - "
        "silence reads as rudeness. Time-of-day greetings split the day: "
        "صباح الخير until midday, مساء الخير after. Gender reaches into "
        "greetings too: كيف حالكَ (to a man) vs كيف حالكِ (to a woman). "
        "Farewells bless the traveler's safety (مع السلامة، في أمان "
        "الله) because travel was once dangerous and the language "
        "remembers. Learn greetings as call-and-response pairs, never "
        "alone."
    ),
    "key_points": [
        "30 phrases: 14 greetings, 4 farewells, 12 politeness phrases.",
        "Every greeting has a fixed reply - reciprocity is mandatory.",
        "صباح الخير/صباح النور (morning pair), مساء الخير/مساء النور (evening pair).",
        "السلام عليكم/وعليكم السلام is the universal greeting pair.",
        "Gendered forms: حالكَ (m) vs حالكِ (f).",
        "من فضلك، لو سمحت، شكراً، عفواً، تفضل - the politeness core.",
        "إن شاء الله for future plans is obligatory politeness, not optional.",
        "Usage notes on each phrase above tell you exactly when to use it.",
    ],
    "requirements": [
        "Memorize the four call-and-response pairs first.",
        "Practice gendered forms aloud (كَ vs كِ endings).",
        "Use three politeness phrases in role-play before real use.",
    ],
    "standards": [
        "Phrases are standard pan-Arab MSA usage.",
        "Usage notes reflect standard Arab social norms.",
    ],
    "citations": [CIT_HOLES, CIT_BADAWI],
    "sig_lens": (
        "The Signature read: greetings are the sworn handshake of the "
        "language - peace offered, peace returned, never left hanging. "
        "The Signature Language Method drills them as pairs because a "
        "greeting without its reply is a broken covenant. Master the "
        "four pairs and the politeness core, and every door in the Arab "
        "world opens."
    ),
    "drill": {"items": GREETINGS, "count": 30,
              "cats": {"greeting": 14, "farewell": 4, "politeness": 12}},
    "must_contain": ["وعليكم السلام", "صباح النور", "إلى اللقاء", "تفضل", "ما شاء الله"],
})

# ---------------------------------------------------------------- record 10: grammar essentials

GRAMMAR_RULES = [
    ("Word order", "Default is verb-subject-object: كتبَ الطالبُ الدرسَ (kataba ṭ-ṭālibu d-darsa) - the student wrote the lesson. Subject-first (الطالبُ كتبَ الدرسَ) adds emphasis to the subject."),
    ("Gender", "Every noun is masculine or feminine. Feminine is usually marked with ة: معلم (male teacher) / معلمة (female teacher). Verbs and adjectives agree: هي تكتبُ (she writes) vs هو يكتبُ (he writes)."),
    ("Number", "Three numbers: singular, dual (-انِ: كتابانِ, two books), plural. Sound plurals add ون/ين (m) or ات (f): معلمون، سيارات. Broken plurals reshape the word: كتاب → كتب."),
    ("Definite article", "ال (al-) = the. Before sun letters (ت ث د ذ ر ز س ش ص ض ط ظ ل ن) the l assimilates: الشمس (ash-shams). ال also marks generic concepts: الحبُّ (love)."),
    ("Cases", "In formal MSA, nouns show case: nominative ـُ (الطالبُ), accusative ـَ (رأيتُ الطالبَ), genitive ـِ (مع الطالبِ). Spoken dialects drop them; MSA keeps them in formal speech."),
    ("Negation", "لا + present: لا أعرفُ (I do not know). لم + jussive = past: لم أذهبْ (I did not go). لن + subjunctive = future: لن أنسى (I will not forget). ما negates past in some styles: ما فعلتُ."),
    ("Questions", "هل turns a statement into a yes-no question: هل تتكلمُ العربيةَ؟ (Do you speak Arabic?). Or front an interrogative: أين، متى، كيف، لماذا، كم، من، ما."),
    ("Idafa (construct)", "Two nouns, first indefinite, second definite: كتابُ الطالبِ (the students book) - literally book the-student. Chains stack: بابُ بيتِ الجارِ (the neighbors house door)."),
    ("Adjective agreement", "The adjective follows the noun and copies gender, number, and definiteness: البيتُ الكبيرُ (the big house); سيارةٌ جديدةٌ (a new car). Non-human plurals take feminine singular: كتبٌ جديدةٌ."),
    ("Verb agreement", "The verb agrees with its subject in person, gender, number: أنا أكتبُ (I write)، هي تكتبُ (she writes)، هم يكتبونَ (they m write). In VSO order with a plural subject, the verb stays singular: كتبَ الطلابُ (the students wrote)."),
]

ENTRIES.append({
    "key": "grammar",
    "name": "Arabic Grammar Essentials",
    "group": "Grammar Essentials",
    "ladder_rank": 4,
    "ladder_tier": "foundations",
    "description": (
        "The ten load-bearing rules of Arabic grammar, each with "
        "translated example sentences. These ten rules generate the "
        "great majority of correct everyday sentences.\n" +
        "\n".join("  %d. %s: %s" % (i + 1, r, x) for i, (r, x) in enumerate(GRAMMAR_RULES)) + "\n"
        "Read the rules in order: word order tells you where things "
        "go, gender and number tell you how words change shape, the "
        "article and cases tell you how nouns mark their role, negation "
        "and questions tell you how sentences change mood, and idafa, "
        "adjective agreement, and verb agreement tell you how words "
        "bind to each other."
    ),
    "how_it_works": (
        "Arabic grammar is agreement all the way down. The verb agrees "
        "with the subject, the adjective agrees with the noun, the "
        "pronoun agrees with its antecedent - every word checks its "
        "neighbors and matches gender and number. The one famous "
        "exception proves the rule: in verb-first order with a plural "
        "subject, the verb stays singular (كتبَ الطلابُ), as if the "
        "verb greets the subject before counting it. Cases (-u/-a/-i) "
        "are the formal dress of nouns; negation particles are chosen "
        "by tense (لا present, لم past, لن future); questions are built "
        "by fronting هل or a question word. Ten rules, and the sentence "
        "engine runs."
    ),
    "key_points": [
        "Default word order VSO; SVO adds emphasis.",
        "Gender (m/f) and number (singular/dual/plural) on nouns, verbs, adjectives.",
        "ال = the; sun letters assimilate its l.",
        "Cases -u/-a/-i in formal MSA; dropped in dialects.",
        "Negation by tense: لا (present), لم (past), لن (future).",
        "هل for yes-no questions; interrogatives fronted otherwise.",
        "Idafa: possessed + possessor, first noun indefinite.",
        "Adjectives follow and agree; verbs agree with subjects.",
        "VSO + plural subject → verb stays singular (كتبَ الطلابُ).",
        "Non-human plurals take feminine-singular agreement.",
    ],
    "requirements": [
        "Write 5 sentences in VSO and convert them to SVO.",
        "Conjugate one verb fully (past + present) as the agreement drill.",
        "Build 10 idafa phrases from your noun vocabulary.",
    ],
    "standards": [
        "Rules per Wright 1896; Ryding 2005; Badawi-Carter-Gully 2004.",
    ],
    "citations": [CIT_WRIGHT, CIT_RYDING, CIT_BADAWI],
    "sig_lens": (
        "The Signature read: grammar is the covenant of the sentence - "
        "ten articles, each binding. Word order, gender, number, case, "
        "negation, question, idafa, agreement: every word signs, every "
        "neighbor witnesses. The Signature Language Method teaches the "
        "ten as law tablets, drilled in order, because a sentence built "
        "on all ten never falls."
    ),
    "drill": {"rules": GRAMMAR_RULES, "count": 10,
              "vso": "كتبَ الطالبُ الدرسَ",
              "neg": ["لا", "لم", "لن"],
              "cases": ["ُ", "َ", "ِ"]},
    "must_contain": ["كتبَ الطلابُ", "لم أذهبْ", "لن أنسى", "كتابُ الطالبِ", "هل تتكلمُ العربيةَ؟"],
})


def _theme_entry(key, name, rank, tier, group, intro, sentences, keywords,
                 how, points, sig):
    return {
        "key": key, "name": name, "group": group,
        "ladder_rank": rank, "ladder_tier": tier,
        "description": intro + "\n" + _sent_lines(sentences),
        "how_it_works": how,
        "key_points": points,
        "requirements": [
            "Read all 20 sentences aloud twice - once slowly, once at speed.",
            "Cover the English column and translate from the Arabic alone.",
            "Write 5 of your own sentences reusing the theme vocabulary.",
        ],
        "standards": [
            "Sentences are standard MSA; vocabulary per Hans Wehr (1979).",
            "Transliteration follows ISO 233:1984.",
        ],
        "citations": [CIT_WEHR, CIT_RYDING],
        "sig_lens": sig,
        "drill": {"sentences": sentences, "count": 20, "keywords": keywords},
        "must_contain": [s[0] for s in sentences],
    }


S_HOME = [
    ("بيتُنا واسعٌ ومريحٌ", "baytunā wāsiʿun wa murīḥun", "Our house is spacious and comfortable"),
    ("غرفةُ المعيشةِ في الطابقِ الأرضي", "ghurfatu l-maʿīshati fī ṭ-ṭābiqi l-arḍī", "The living room is on the ground floor"),
    ("المطبخُ بجانبِ غرفةِ الطعامِ", "al-maṭbakhu bijānibi ghurfati ṭ-ṭaʿāmi", "The kitchen is next to the dining room"),
    ("أبي يجلسُ في الشرفةِ كلَّ مساءٍ", "abī yajlisu fī sh-shurfati kulla masāʾin", "My father sits on the balcony every evening"),
    ("أمي تطبخُ طعاماً لذيذاً", "ummī taṭbukhu ṭaʿāman ladhīdhan", "My mother cooks delicious food"),
    ("أخي الأكبرُ يعملُ مهندساً", "akhī l-akbaru yaʿmalu muhandisan", "My older brother works as an engineer"),
    ("أختي الصغرى تدرسُ في الجامعةِ", "ukhtī ṣ-ṣughrā tadrusu fī l-jāmiʿati", "My younger sister studies at the university"),
    ("جدّي يحكي لنا قصصاً قديمةً", "jaddī yaḥkī lanā qiṣaṣan qadīmatan", "My grandfather tells us old stories"),
    ("جدّتي تصنعُ أطيبَ الحلوياتِ", "jaddatī taṣnaʿu aṭyaba l-ḥalawiyyāti", "My grandmother makes the tastiest sweets"),
    ("عمي يسكنُ في المدينةِ المجاورةِ", "ʿammī yaskunu fī l-madīnati l-mujāwirati", "My uncle lives in the neighboring city"),
    ("خالتي تزورُنا كلَّ أسبوعٍ", "khālatī tazūrunā kulla usbūʿin", "My aunt visits us every week"),
    ("ابنُ عمي صديقي المفضلُ", "ibnu ʿammī ṣadīqī l-mufaḍḍalu", "My cousin is my favorite friend"),
    ("نظّفتُ غرفتي صباحَ اليومِ", "naẓẓaftu ghurfatī ṣabāḥa l-yawmi", "I cleaned my room this morning"),
    ("الستائرُ الجديدةُ جميلةٌ", "as-satāʾiru l-jadīdatu jamīlatun", "The new curtains are beautiful"),
    ("اشترينا أريكةً جديدةً للصالونِ", "ishtaraynā arīkatan jadīdatan liṣ-ṣālūni", "We bought a new sofa for the living room"),
    ("المصباحُ في غرفتي لا يعملُ", "al-miṣbāḥu fī ghurfatī lā yaʿmalu", "The lamp in my room does not work"),
    ("نتناولُ العشاءَ معاً كلَّ ليلةٍ", "natanāwalu l-ʿashāʾa maʿan kulla laylatin", "We have dinner together every night"),
    ("بيتُ جدّي في القريةِ كبيرٌ", "baytu jaddī fī l-qaryati kabīrun", "My grandfathers house in the village is big"),
    ("أحبُّ الجلوسَ مع عائلتي", "uḥibbu l-julūsa maʿa ʿāʾilatī", "I love sitting with my family"),
    ("العائلةُ أهمُّ شيءٍ في الحياةِ", "al-ʿāʾilatu ahammu shayʾin fī l-ḥayāti", "Family is the most important thing in life"),
]

S_FOOD = [
    ("أفطرُ في السابعةِ صباحاً", "ufṭiru fī s-sābiʿati ṣabāḥan", "I have breakfast at seven in the morning"),
    ("الخبزُ الطازجُ لذيذٌ", "al-khubzu ṭ-ṭāzaju ladhīdhun", "Fresh bread is delicious"),
    ("أشربُ القهوةَ العربيةَ كلَّ صباحٍ", "ashrabu l-qahwata l-ʿarabiyyata kulla ṣabāḥin", "I drink Arabic coffee every morning"),
    ("الغداءُ جاهزٌ على الطاولةِ", "al-ghadāʾu jāhizun ʿalā ṭ-ṭāwilati", "Lunch is ready on the table"),
    ("أمي تطبخُ الكبسةَ يومَ الجمعةِ", "ummī taṭbukhu l-kabsata yawma l-jumuʿati", "My mother cooks kabsa on Fridays"),
    ("أحبُّ الفواكهَ الطازجةَ", "uḥibbu l-fawākiha ṭ-ṭāzajata", "I love fresh fruit"),
    ("الخضارُ مفيدةٌ للصحةِ", "al-khuḍāru mufīdatun liṣ-ṣiḥḥati", "Vegetables are good for health"),
    ("اشتريتُ كيلوَ لحمٍ من الجزارِ", "ishtaraytu kīlū laḥmin mina l-jazzāri", "I bought a kilo of meat from the butcher"),
    ("السمكُ المشويُّ صحيٌّ ولذيذٌ", "as-samaku l-mashwiyyu ṣiḥḥiyyun wa ladhīdhun", "Grilled fish is healthy and delicious"),
    ("أضفْ قليلاً من الملحِ", "aḍif qalīlan mina l-milḥi", "Add a little salt"),
    ("الشايُ بالنعناعِ مشروبي المفضلُ", "ash-shāyu bin-naʿnāʿi mashrūbī l-mufaḍḍalu", "Mint tea is my favorite drink"),
    ("الحلوياتُ الشرقيةُ مشهورةٌ", "al-ḥalawiyyātu sh-sharqiyyatu mashhūratun", "Eastern sweets are famous"),
    ("نتناولُ العشاءَ في مطعمٍ جديدٍ", "natanāwalu l-ʿashāʾa fī maṭʿamin jadīdin", "We are having dinner at a new restaurant"),
    ("الفاتورةُ، لو سمحتَ", "al-fātūratu, law samaḥta", "The bill, please"),
    ("الأكلُ هنا رخيصٌ ولذيذٌ", "al-aklu hunā rakhīṣun wa ladhīdhun", "The food here is cheap and delicious"),
    ("هل الطعامُ حارٌّ؟", "hal aṭ-ṭaʿāmu ḥārrun؟", "Is the food spicy"),
    ("أنا نباتيٌّ، لا آكلُ اللحمَ", "anā nabātiyyun, lā ākulu l-laḥma", "I am vegetarian, I do not eat meat"),
    ("قطّعْ البصلَ قطعاً صغيرةً", "qaṭṭiʿi l-baṣala qiṭaʿan ṣaghīratan", "Cut the onion into small pieces"),
    ("اتركْ الطعامَ على النارِ عشرين دقيقةً", "utruk aṭ-ṭaʿāma ʿalā n-nāri ʿishrīna daqīqatan", "Leave the food on the fire for twenty minutes"),
    ("بالهناءِ والشفاءِ", "bil-hanāʾi wash-shifāʾi", "Enjoy your meal (bon appétit)"),
]

S_TRAVEL = [
    ("أين محطةُ القطارِ؟", "ayna maḥaṭṭatu l-qiṭāri؟", "Where is the train station"),
    ("كم ثمنُ التذكرةِ إلى القاهرةِ؟", "kam thamanu t-tadhkarati ilā l-qāhirati؟", "How much is the ticket to Cairo"),
    ("الطائرةُ تغادرُ في العاشرةِ صباحاً", "aṭ-ṭāʾiratu tughādiru fī l-ʿāshirati ṣabāḥan", "The plane departs at ten in the morning"),
    ("أريدُ حجزَ غرفةٍ مفردةٍ", "urīdu ḥajza ghurfatin mufradatin", "I want to book a single room"),
    ("الفندقُ قريبٌ من المطارِ", "al-funduqu qarībun mina l-maṭāri", "The hotel is near the airport"),
    ("خذْ سيارةَ أجرةٍ إلى وسطِ المدينةِ", "khudh sayyārata ujratin ilā wasaṭi l-madīnati", "Take a taxi to downtown"),
    ("كم تستغرقُ الرحلةُ؟", "kam tastaghriqu r-riḥlatu؟", "How long does the trip take"),
    ("الرحلةُ تستغرقُ ثلاثَ ساعاتٍ", "ar-riḥlatu tastaghriqu thalātha sāʿātin", "The trip takes three hours"),
    ("أضعتُ جوازَ سفري", "aḍaʿtu jawāza safarī", "I lost my passport"),
    ("أين أقربُ صرّافٍ آليٍّ؟", "ayna aqrabu ṣarrāfin āliyyin؟", "Where is the nearest ATM"),
    ("هل يوجدُ حافلةٌ إلى الشاطئِ؟", "hal yūjadu ḥāfilatun ilā sh-shāṭiʾi؟", "Is there a bus to the beach"),
    ("امشِ مستقيماً ثم انعطفْ يميناً", "imshi mustaqīman thumma nʿaṭif yamīnan", "Go straight then turn right"),
    ("المتحفُ على بعدِ عشرِ دقائقَ سيراً", "al-matḥafu ʿalā buʿdi ʿashri daqāʾiqa sayran", "The museum is ten minutes away on foot"),
    ("أريدُ خريطةً للمدينةِ", "urīdu kharīṭatan lil-madīnati", "I want a map of the city"),
    ("هل تتكلمُ الإنجليزيةَ؟", "hal tatakallamu l-ingilīziyyata؟", "Do you speak English"),
    ("أنا سائحٌ، هذه أولُ زيارةٍ لي", "anā sāʾiḥun, hādhihi awwalu ziyāratin lī", "I am a tourist, this is my first visit"),
    ("الجوازُ والتذكرةُ، من فضلكَ", "al-jawāzu wat-tadhkaratu, min faḍlika", "Passport and ticket, please"),
    ("رحلةً سعيدةً", "riḥlatan saʿīdatan", "Have a happy trip"),
    ("وصلْنا إلى الفندقِ مساءً", "waṣalnā ilā l-funduqi masāʾan", "We arrived at the hotel in the evening"),
    ("السفرُ يوسّعُ المداركَ", "as-safaru yuwassiʿu l-madārika", "Travel broadens the mind"),
]

S_WORK = [
    ("أعملُ مدرّساً في مدرسةٍ ثانويةٍ", "aʿmalu mudarrisan fī madrasatin thānawiyyatin", "I work as a teacher in a secondary school"),
    ("يبدأُ الدوامُ في الثامنةِ صباحاً", "yabdaʾu d-dawāmu fī th-thāminati ṣabāḥan", "Work starts at eight in the morning"),
    ("عندي اجتماعٌ مهمٌّ اليومَ", "ʿindī ijtimāʿun muhimmun al-yawma", "I have an important meeting today"),
    ("المكتبُ في الطابقِ العاشرِ", "al-maktabu fī ṭ-ṭābiqi l-ʿāshiri", "The office is on the tenth floor"),
    ("زميلي في العملِ لطيفٌ جداً", "zamīlī fī l-ʿamali laṭīfun jiddan", "My work colleague is very nice"),
    ("أرسلتُ التقريرَ بالبريدِ الإلكتروني", "arsaltu t-taqrīra bil-barīdi l-iliktrūnī", "I sent the report by email"),
    ("المديرُ طلبَ مني إنهاءَ المشروعِ", "al-mudīru ṭalaba minnī inhāʾa l-mashrūʿi", "The manager asked me to finish the project"),
    ("أدرسُ الهندسةَ في الجامعةِ", "adrusu l-handasata fī l-jāmiʿati", "I study engineering at the university"),
    ("الامتحانُ الأسبوعَ القادمَ", "al-imtiḥānu l-usbūʿa l-qādima", "The exam is next week"),
    ("المعلمةُ شرحتْ الدرسَ بوضوحٍ", "al-muʿallimatu sharaḥat d-darsa biwuḍūḥin", "The teacher explained the lesson clearly"),
    ("كتبتُ واجبي المدرسيَّ أمسِ", "katabtu wājibī l-madrasīya amsi", "I wrote my homework yesterday"),
    ("الطلابُ يستمعونَ بانتباهٍ", "aṭ-ṭullābu yastamiʿūna bi-intibāhin", "The students listen attentively"),
    ("المكتبةُ مليئةٌ بالكتبِ المفيدةِ", "al-maktabatu malīʾatun bil-kutubi l-mufīdati", "The library is full of useful books"),
    ("تخرّجتُ من الجامعةِ العامَ الماضي", "takharrajtu mina l-jāmiʿati l-ʿāma l-māḍī", "I graduated from university last year"),
    ("أبحثُ عن وظيفةٍ جديدةٍ", "abḥathu ʿan waẓīfatin jadīdatin", "I am looking for a new job"),
    ("الراتبُ يُدفعُ في نهايةِ الشهرِ", "ar-rātibu yudfaʿu fī nihāyati sh-shahri", "The salary is paid at the end of the month"),
    ("أخذتُ إجازةً لمدةِ أسبوعٍ", "akhadhtu ijāzatan limuddati usbūʿin", "I took a week of vacation"),
    ("العملُ الجماعيُّ يحققُ النجاحَ", "al-ʿamalu l-jamāʿiyyu yuḥaqqiqu n-najāḥa", "Teamwork achieves success"),
    ("العلمُ نورٌ يضيءُ الطريقَ", "al-ʿilmu nūrun yuḍīʾu ṭ-ṭarīqa", "Knowledge is a light that illuminates the path"),
    ("من جدَّ وجدَ", "man jadda wajada", "Whoever strives, finds (proverb)"),
]

S_HEALTH = [
    ("أشعرُ بألمٍ في رأسي", "ashʿuru bi-alamin fī raʾsī", "I feel pain in my head"),
    ("عندي حمّى منذُ أمسِ", "ʿindī ḥummā mundhu amsi", "I have had a fever since yesterday"),
    ("أحتاجُ إلى رؤيةِ الطبيبِ", "aḥtāju ilā ruʾyati ṭ-ṭabībi", "I need to see the doctor"),
    ("أين أقربُ مستشفى؟", "ayna aqrabu mustashfā؟", "Where is the nearest hospital"),
    ("الصيدليةُ تفتحُ حتى منتصفِ الليلِ", "aṣ-ṣaydaliyyatu taftaḥu ḥattā muntaṣafi l-layli", "The pharmacy is open until midnight"),
    ("خذْ هذا الدواءَ مرتينِ يومياً", "khudh hādhā d-dawāʾa marratayni yawmiyyan", "Take this medicine twice a day"),
    ("اشربْ كثيراً من الماءِ", "ishrab kathīran mina l-māʾi", "Drink plenty of water"),
    ("يجبُ أن ترتاحَ في الفراشِ", "yajibu an tartāḥa fī l-firāshi", "You must rest in bed"),
    ("عيني تؤلمني", "ʿaynī tuʾlimunī", "My eye hurts"),
    ("أسناني سليمةٌ", "asnānī salīmatun", "My teeth are healthy"),
    ("قلبي يدقُّ بسرعةٍ", "qalbī yaduqqu bisurʿatin", "My heart beats fast"),
    ("أعاني من حساسيةِ الربيعِ", "uʿānī min ḥassāsiyyati r-rabīʿi", "I suffer from spring allergies"),
    ("الرياضةُ مفيدةٌ للجسمِ", "ar-riyāḍatu mufīdatun lil-jismi", "Exercise is good for the body"),
    ("امشِ ثلاثين دقيقةً كلَّ يومٍ", "imshi thalāthīna daqīqatan kulla yawmin", "Walk thirty minutes every day"),
    ("النومُ المبكرُ صحيٌّ", "an-nawmu l-mubakkiru ṣiḥḥiyyun", "Early sleep is healthy"),
    ("تجنّبْ الأكلَ السريعَ", "tajannab al-akla s-sarīʿa", "Avoid fast food"),
    ("الخضارُ والفواكهُ تقوّي المناعةَ", "al-khuḍāru wal-fawākihu tuqawwī l-manāʿata", "Vegetables and fruit strengthen immunity"),
    ("ضغطُ دمي مرتفعٌ", "ḍaghṭu damī murtafiʿun", "My blood pressure is high"),
    ("سآخذُ موعداً مع طبيبِ الأسنانِ", "saʾākhudhu mawʿidan maʿa ṭabībi l-asnāni", "I will make an appointment with the dentist"),
    ("العقلُ السليمُ في الجسمِ السليمِ", "al-ʿaqlu s-salīmu fī l-jismi s-salīmi", "A healthy mind in a healthy body"),
]

S_EMOTIONS = [
    ("أنا سعيدٌ جداً اليومَ", "anā saʿīdun jiddan al-yawma", "I am very happy today"),
    ("الخبرُ السارُّ أسعدَني", "al-khabaru s-sārru asʿadanī", "The good news made me happy"),
    ("أشعرُ بالحزنِ الشديدِ", "ashʿuru bil-ḥuzni sh-shadīdi", "I feel deep sadness"),
    ("بكتْ من شدةِ الفرحِ", "bakat min shiddati l-faraḥi", "She cried from overwhelming joy"),
    ("أنا غاضبٌ من هذا التصرفِ", "anā ghāḍibun min hādhā t-taṣarrufi", "I am angry about this behavior"),
    ("اهدأْ، لا داعيَ للغضبِ", "ihdaʾ, lā dāʿiya lil-ghaḍabi", "Calm down, there is no need for anger"),
    ("أخافُ من الظلامِ", "akhāfu mina ẓ-ẓalāmi", "I am afraid of the dark"),
    ("لا تخفْ، أنا معكَ", "lā takhaf, anā maʿaka", "Do not be afraid, I am with you"),
    ("أحبُّ عائلتي كثيراً", "uḥibbu ʿāʾilatī kathīran", "I love my family a lot"),
    ("الحبُّ أجملُ شعورٍ", "al-ḥubbu ajmalu shuʿūrin", "Love is the most beautiful feeling"),
    ("فاجأَني صديقي بهديةٍ", "fājaʾanī ṣadīqī bihadiyyatin", "My friend surprised me with a gift"),
    ("كانتْ مفاجأةً سارةً", "kānat mufājaʾatan sārratan", "It was a pleasant surprise"),
    ("أشعرُ بالقلقِ على الامتحانِ", "ashʿuru bil-qalaqi ʿalā l-imtiḥāni", "I feel anxious about the exam"),
    ("اطمئنَّ، كلُّ شيءٍ سيكونُ بخيرٍ", "iṭmaʾinna, kullu shayʾin sayakūnu bikhayrin", "Rest assured, everything will be fine"),
    ("أنا فخورٌ بنجاحِكَ", "anā fakhūrun binajāḥika", "I am proud of your success"),
    ("شعرتُ بالخجلِ من خطئي", "shaʿartu bil-khajali min khaṭaʾī", "I felt ashamed of my mistake"),
    ("الغيرةُ شعورٌ طبيعيٌّ", "al-ghīratu shuʿūrun ṭabīʿiyyun", "Jealousy is a natural feeling"),
    ("أنا ممتنٌّ لمساعدتِكَ", "anā mumatinnun limusāʿadatika", "I am grateful for your help"),
    ("الأملُ لا يموتُ أبداً", "al-amalu lā yamūtu abadan", "Hope never dies"),
    ("الصبرُ مفتاحُ الفرجِ", "aṣ-ṣabru miftāḥu l-faraji", "Patience is the key to relief"),
]

S_NATURE = [
    ("الشمسُ تشرقُ من الشرقِ", "ash-shamsu tushriqu mina sh-sharqi", "The sun rises in the east"),
    ("القمرُ مكتملٌ الليلةَ", "al-qamaru mukhtamilun al-laylata", "The moon is full tonight"),
    ("النجومُ تلمعُ في السماءِ", "an-nujūmu talmaʿu fī s-samāʾi", "The stars shine in the sky"),
    ("الجوُّ جميلٌ اليومَ", "al-jawwu jamīlun al-yawma", "The weather is beautiful today"),
    ("تمطرُ بغزارةٍ منذُ الصباحِ", "tumṭiru bighazāratin mundhu ṣ-ṣabāḥi", "It has been raining heavily since morning"),
    ("الثلجُ يغطي الجبالَ", "ath-thalju yughaṭṭī l-jibāla", "Snow covers the mountains"),
    ("الرياحُ قويةٌ الليلةَ", "ar-riyāḥu qawiyyatun al-laylata", "The wind is strong tonight"),
    ("الربيعُ أجملُ الفصولِ", "ar-rabīʿu ajmalu l-fuṣūli", "Spring is the most beautiful season"),
    ("الزهورُ تتفتحُ في الحديقةِ", "az-zuhūru tatafattaḥu fī l-ḥadīqati", "The flowers bloom in the garden"),
    ("الشجرةُ الكبيرةُ تعطي ظلاًّ", "ash-shajaratu l-kabīratu tuʿṭī ẓillan", "The big tree gives shade"),
    ("العصفورُ يغرّدُ على الغصنِ", "al-ʿuṣfūru yugharridu ʿalā l-ghuṣni", "The bird sings on the branch"),
    ("القطةُ تنامُ تحتَ الشجرةِ", "al-qiṭṭatu tanāmu taḥta sh-shajarati", "The cat sleeps under the tree"),
    ("الكلبُ يحرسُ البيتَ", "al-kalbu yaḥrusu l-bayta", "The dog guards the house"),
    ("الحصانُ يجري في الحقلِ", "al-ḥiṣānu yajrī fī l-ḥaqli", "The horse runs in the field"),
    ("الجملُ سفينةُ الصحراءِ", "al-jamalu safīnatu ṣ-ṣaḥrāʾi", "The camel is the ship of the desert"),
    ("البحرُ هادئٌ هذا المساءَ", "al-baḥru hādiʾun hādhā l-masāʾa", "The sea is calm this evening"),
    ("النهرُ يجري نحوَ البحرِ", "an-nahru yajrī naḥwa l-baḥri", "The river flows toward the sea"),
    ("الصحراءُ واسعةٌ وجميلةٌ", "aṣ-ṣaḥrāʾu wāsiʿatun wa jamīlatun", "The desert is vast and beautiful"),
    ("الغابةُ مليئةٌ بالأشجارِ", "al-ghābatu malīʾatun bil-ashjāri", "The forest is full of trees"),
    ("حافظْ على البيئةِ نظيفةً", "ḥāfiẓ ʿalā l-bīʾati naẓīfatan", "Keep the environment clean"),
]

S_SHOPPING = [
    ("كم سعرُ هذا القميصِ؟", "kam siʿru hādhā l-qamīṣi؟", "How much is this shirt"),
    ("السعرُ مائةُ ريالٍ", "as-siʿru miʾatu riyālin", "The price is one hundred riyals"),
    ("هل يوجدُ خصمٌ؟", "hal yūjadu khaṣmun؟", "Is there a discount"),
    ("هذا غالٍ جداً", "hādhā ghālin jiddan", "This is very expensive"),
    ("أريدُ مقاساً أكبرَ", "urīdu maqāsan akbara", "I want a bigger size"),
    ("هل يمكنُ أن أجرّبَهُ؟", "hal yumkinu an ujarribahu؟", "Can I try it on"),
    ("غرفةُ القياسِ هناك", "ghurfatu l-qiyāsi hunāka", "The fitting room is over there"),
    ("آخذُهُ، لفَّهُ من فضلكَ", "ākhuḏuhu, liffahu min faḍlika", "I will take it, wrap it please"),
    ("أدفعُ نقداً أم بالبطاقةِ؟", "adfaʿu naqdan am bil-biṭāqati؟", "Do I pay cash or by card"),
    ("هل تقبلونَ البطاقاتِ؟", "hal taqbalūna l-biṭāqāti؟", "Do you accept cards"),
    ("أريدُ إرجاعَ هذا", "urīdu irjāʿa hādhā", "I want to return this"),
    ("أين قسمُ الأحذيةِ؟", "ayna qismu l-aḥdhiyati؟", "Where is the shoe section"),
    ("السوقُ الشعبيُّ أرخصُ", "as-sūqu sh-shaʿbiyyu arkhaṣu", "The popular market is cheaper"),
    ("المساومةُ جزءٌ من التسوقِ", "al-musāwamatu juzʾun mina t-tasawwuqi", "Bargaining is part of shopping"),
    ("أعطني سعرَكَ الأخيرَ", "aʿṭinī siʿraka l-akhīra", "Give me your final price"),
    ("اتفقْنا، صفقةٌ رابحةٌ", "ittafaqnā, ṣafqatun rābiḥatun", "Deal, a winning bargain"),
    ("أحتاجُ قائمةَ المشترياتِ", "aḥtāju qāʾimata l-mushtarayāti", "I need the shopping list"),
    ("اشتريتُ خضاراً وفواكهَ", "ishtaraytu khuḍāran wa fawākiha", "I bought vegetables and fruit"),
    ("المحلُّ يفتحُ في التاسعةِ", "al-maḥallu yaftaḥu fī t-tāsiʿati", "The shop opens at nine"),
    ("التسوقُ الذكيُّ يوفّرُ المالَ", "at-tasawwuqu dh-dhakiyyu yuwaffiru l-māla", "Smart shopping saves money"),
]

S_SOCIAL = [
    ("تشرّفتُ بمعرفتِكَ", "tasharraftu bimaʿrifatika", "Pleased to meet you"),
    ("من أين أنتَ؟", "min ayna anta؟", "Where are you from"),
    ("أنا من الرياضِ", "anā mina r-riyāḍi", "I am from Riyadh"),
    ("كم عمرُكَ؟", "kam ʿumruka؟", "How old are you"),
    ("عمري ثلاثون سنةً", "ʿumrī thalāthūna sanatan", "I am thirty years old"),
    ("هل أنتَ متزوجٌ؟", "hal anta mutazawwijun؟", "Are you married"),
    ("عندي ثلاثةُ أطفالٍ", "ʿindī thalāthatu aṭfālin", "I have three children"),
    ("أدعوكَ إلى حفلِ عيدِ ميلادي", "adʿūka ilā ḥafli ʿīdi mīlādī", "I invite you to my birthday party"),
    ("متى الحفلُ؟", "matā l-ḥaflu؟", "When is the party"),
    ("الحفلُ يومَ السبتِ القادمِ", "al-ḥaflu yawma s-sabti l-qādimi", "The party is next Saturday"),
    ("مباركٌ الزواجُ", "mubārakun az-zawāju", "Congratulations on the marriage"),
    ("مباركٌ النجاحُ", "mubārakun an-najāḥu", "Congratulations on the success"),
    ("أهلاً وسهلاً بكم في بيتِنا", "ahlan wa sahlan bikum fī baytinā", "Welcome to our home"),
    ("تفضّلْ بالدخولِ", "tafaḍḍal bid-dukhūli", "Please come in"),
    ("اشربْ الشايَ معنا", "ishrab ash-shāya maʿanā", "Have tea with us"),
    ("صديقي منذُ الطفولةِ", "ṣadīqī mundhu ṭ-ṭufūlati", "My friend since childhood"),
    ("نخرجُ معاً كلَّ نهايةِ أسبوعٍ", "nakhruju maʿan kulla nihāyati usbūʿin", "We go out together every weekend"),
    ("الصداقةُ كنزٌ ثمينٌ", "aṣ-ṣadāqatu kanzun thamīnun", "Friendship is a precious treasure"),
    ("سأفتقدُكَ كثيراً", "saʾaftaqiduka kathīran", "I will miss you a lot"),
    ("نبقى على تواصلٍ", "nabqā ʿalā tawāṣulin", "We will stay in touch"),
]

S_TECH = [
    ("هاتفي الجديدُ سريعٌ", "hātifī l-jadīdu sarīʿun", "My new phone is fast"),
    ("اشحنْ هاتفَكَ قبلَ الخروجِ", "ishḥan hātifaka qabla l-khurūji", "Charge your phone before going out"),
    ("ما كلمةُ سرِّ الواي فاي؟", "mā kalimatu sirri l-wāy fāy؟", "What is the Wi-Fi password"),
    ("الإنترنتُ بطيءٌ اليومَ", "al-intirnitu baṭīʾun al-yawma", "The internet is slow today"),
    ("أرسلتُ لكَ رسالةً نصيةً", "arsaltu laka risālatan naṣṣiyyatan", "I sent you a text message"),
    ("اتصلْ بي عندما تصلُ", "ittaṣil bī ʿindamā taṣilu", "Call me when you arrive"),
    ("حمّلتُ تطبيقاً جديداً", "ḥammaltu taṭbīqan jadīdan", "I downloaded a new app"),
    ("حدّثْ نظامَ التشغيلِ", "ḥaddith niẓāma t-tashghīli", "Update the operating system"),
    ("احفظْ ملفاتِكَ في مكانٍ آمنٍ", "iḥfaẓ mallafātika fī makānin āminin", "Save your files in a safe place"),
    ("الحاسوبُ لا يعملُ", "al-ḥāsūbu lā yaʿmalu", "The computer does not work"),
    ("أعدْ تشغيلَ الجهازِ", "aʿid tashghīla l-jihāzi", "Restart the device"),
    ("الشاشةُ مكسورةٌ", "ash-shāshatu maksūratun", "The screen is broken"),
    ("أبحثُ في الإنترنتِ عن معلومةٍ", "abḥathu fī l-intirniti ʿan maʿlūmatin", "I am searching the internet for information"),
    ("البريدُ الإلكتروني وصلَ", "al-barīdu l-iliktrūnī waṣala", "The email arrived"),
    ("شاركتُ الصورةَ مع أصدقائي", "shāraktu ṣ-ṣūrata maʿa aṣdiqāʾī", "I shared the photo with my friends"),
    ("تابعْني على حسابي", "tābiʿnī ʿalā ḥisābī", "Follow me on my account"),
    ("الذكاءُ الاصطناعيُّ يتطورُ بسرعةٍ", "adh-dhakāʾu l-iṣṭināʿiyyu yataṭawwaru bisurʿatin", "Artificial intelligence evolves quickly"),
    ("احذرْ من الرسائلِ الاحتياليةِ", "iḥdhar mina r-rasāʾili l-iḥtiyāliyyati", "Beware of scam messages"),
    ("التكنولوجيا تسهِّلُ حياتَنا", "at-tiknūlūjyā tusahhilu ḥayātanā", "Technology makes our life easier"),
    ("أغلقْ هاتفَكَ أثناءَ القيادةِ", "aghliq hātifaka athnāʾa l-qiyādati", "Turn off your phone while driving"),
]

ENTRIES.append(_theme_entry(
    "home", "Arabic Home and Family Sentences", 4, "compounded", "Everyday Themes",
    "Twenty sentences about the house, rooms, furniture, and family members. "
    "Family vocabulary is central in Arab culture - learn the kinship terms "
    "(أب، أم، أخ، أخت، جدّ، جدّة، عمّ، خالة) as carefully as the furniture words.",
    S_HOME, ["بيت", "عائلة", "أب", "أم", "غرفة"],
    "House sentences teach possession (بيتُنا, our house) and location "
    "(في، بجانب، تحت). Family sentences teach kinship terms and the "
    "idafa of relationship (ابنُ عمي, my cousin - literally son of my "
    "uncle). Notice how possession suffixes (-ī my, -nā our) do the work "
    "English does with separate words.",
    [
        "20 sentences: house, rooms, furniture, family members.",
        "Kinship terms: أب أم أخ أخت جدّ جدّة عمّ خالة ابن عمّ.",
        "Possession suffixes in action: بيتُنا (our house)، غرفتي (my room).",
        "Location prepositions: في (in)، بجانب (next to)، تحت (under).",
        "Every sentence carries Arabic script, transliteration, and English.",
    ],
    "The Signature read: the home is the first kingdom - every room a "
    "province, every family member a sworn ally. The Signature Language "
    "Method builds the house of vocabulary room by room, and the family "
    "is learned as a formation: father, mother, brother, sister, "
    "grandfather, grandmother, each with their station and their name.",
))
ENTRIES.append(_theme_entry(
    "food", "Arabic Food and Cooking Sentences", 5, "compounded", "Everyday Themes",
    "Twenty sentences about meals, ingredients, cooking actions, and the "
    "restaurant. Food is hospitality in Arab culture - بالهناء والشفاء "
    "(enjoy your meal) is said with real warmth.",
    S_FOOD, ["طعام", "مطعم", "طبخ", "خبز", "شاي"],
    "Food sentences teach the verbs of the kitchen (طبخ، أضاف، قطّع) "
    "and restaurant survival (الفاتورة، لو سمحتَ). Cooking instructions "
    "use the imperative (أضفْ، قطّعْ، اتركْ) - the command form you "
    "will meet again in record 23. Quantities teach numbers in action: "
    "كيلو لحمٍ، عشرين دقيقةً.",
    [
        "20 sentences: meals, ingredients, cooking, restaurant.",
        "Kitchen verbs: طبخ (cook)، أضاف (add)، قطّع (cut).",
        "Imperatives previewed: أضفْ، قطّعْ، اتركْ.",
        "Restaurant survival: الفاتورة، لو سمحتَ، هل يوجد خصم.",
        "Hospitality core: بالهناء والشفاء (enjoy your meal).",
    ],
    "The Signature read: the kitchen is the laboratory of the home - "
    "fire, measure, and patience. The Signature Language Method learns "
    "food as fuel and fellowship: the verbs that feed, the phrases "
    "that honor the guest, the numbers that measure. بالهناء والشفاء "
    "is not a phrase; it is a blessing served warm.",
))
ENTRIES.append(_theme_entry(
    "travel", "Arabic Travel and Directions Sentences", 5, "compounded", "Everyday Themes",
    "Twenty sentences about transport, asking directions, tickets, and "
    "lodging. The traveler's survival kit - every sentence is one you "
    "will actually say.",
    S_TRAVEL, ["سفر", "فندق", "تذكرة", "مطار", "طريق"],
    "Travel sentences teach question patterns (أين، كم) under pressure "
    "and direction imperatives (امشِ، انعطفْ). Transport nouns (قطار، "
    "طائرة، حافلة، سيارة أجرة) combine with time expressions: تغادر في "
    "العاشرةِ. Emergency phrases (أضعتُ جوازَ سفري) are short on "
    "purpose - stress demands short sentences.",
    [
        "20 sentences: transport, directions, tickets, lodging.",
        "Survival questions: أين (where)، كم (how much/how long).",
        "Direction imperatives: امشِ (go)، انعطفْ (turn).",
        "Transport + time: تغادر في العاشرةِ (departs at ten).",
        "Emergency core: أضعتُ جوازَ سفري (I lost my passport).",
    ],
    "The Signature read: the road is the test of the language - no "
    "dictionary in a moving taxi. The Signature Language Method arms "
    "the traveler with twenty sworn sentences: where, how much, how "
    "long, and the emergency line. Travel sentences are short because "
    "the road does not wait.",
))
ENTRIES.append(_theme_entry(
    "work", "Arabic Work and School Sentences", 5, "compounded", "Everyday Themes",
    "Twenty sentences about jobs, the office, the classroom, and "
    "learning. Work and study share the vocabulary of effort - من جدَّ "
    "وجدَ (whoever strives, finds).",
    S_WORK, ["عمل", "مدرسة", "جامعة", "امتحان", "وظيفة"],
    "Work sentences teach professional nouns (اجتماع، تقرير، مدير، "
    "راتب) and the verbs of office life (أرسلَ، طلبَ، بدأَ). School "
    "sentences teach the learning verbs (درسَ، شرحَ، كتبَ، تخرّجَ) and "
    "time markers of academic life (الامتحانُ الأسبوعَ القادمَ). The "
    "proverb من جدَّ وجدَ closes the set - effort as a worldview.",
    [
        "20 sentences: jobs, office, classroom, learning.",
        "Office core: اجتماع، تقرير، مدير، راتب، إجازة.",
        "School core: درس، امتحان، واجب، مكتبة، تخرّج.",
        "Professional verbs: أرسلَ، طلبَ، بدأَ، حقّقَ.",
        "Wisdom close: من جدَّ وجدَ (whoever strives, finds).",
    ],
    "The Signature read: work is the sworn craft and school its "
    "apprenticeship. The Signature Language Method treats the office "
    "and the classroom as one field of effort - the verbs of sending "
    "and finishing beside the verbs of studying and graduating. من "
    "جدَّ وجدَ is the law written over the door.",
))
ENTRIES.append(_theme_entry(
    "health", "Arabic Health and Body Sentences", 6, "compounded", "Everyday Themes",
    "Twenty sentences about body parts, symptoms, the doctor visit, and "
    "the pharmacy. Health phrases must be exact - ambiguity here costs "
    "more than anywhere.",
    S_HEALTH, ["طبيب", "مستشفى", "دواء", "ألم", "صحة"],
    "Health sentences teach body nouns (رأس، عين، سنّ، قلب، دم) and "
    "the symptom pattern أشعرُ بـ (I feel) + noun. Doctor-visit "
    "sentences use need-language (أحتاجُ إلى، يجبُ أن) and the "
    "pharmacy teaches dosage imperatives (خذْ... مرتينِ يومياً). "
    "Prevention closes the set: رياضة، نوم مبكر، خضار.",
    [
        "20 sentences: body parts, symptoms, doctor, pharmacy.",
        "Body core: رأس، عين، أسنان، قلب، دم، ضغط.",
        "Symptom pattern: أشعرُ بألمٍ في (I feel pain in).",
        "Need-language: أحتاجُ إلى، يجبُ أن.",
        "Dosage imperative: خذْ هذا الدواءَ مرتينِ يومياً.",
    ],
    "The Signature read: the body is the first instrument - every "
    "part named, every pain reported exactly. The Signature Language "
    "Method drills health speech as precision speech: the symptom "
    "named, the need stated, the dosage followed. العقل السليم في "
    "الجسم السليم is the maintenance oath.",
))
ENTRIES.append(_theme_entry(
    "emotions", "Arabic Emotions and Feelings Sentences", 6, "compounded", "Everyday Themes",
    "Twenty sentences about happiness, sadness, anger, fear, love, and "
    "surprise. Emotions are where a language shows its heart - Arabic "
    "names feelings with a poet's precision.",
    S_EMOTIONS, ["سعيد", "سعد", "حزن", "غضب", "خاف", "خف", "حب", "فرح", "قلق", "فاجأ"],
    "Emotion sentences teach the feeling adjectives (سعيد، حزين، "
    "غاضب، فخور، ممتنّ) and the verbs of feeling (شعرَ، أحبَّ، خافَ). "
    "Comfort phrases (اهدأْ، لا تخفْ، اطمئنَّ) are imperatives of care "
    "- grammar serving kindness. The set closes on hope and patience: "
    "الأملُ لا يموتُ، الصبرُ مفتاحُ الفرجِ.",
    [
        "20 sentences: happy, sad, angry, afraid, love, surprise.",
        "Feeling adjectives: سعيد، حزين، غاضب، فخور، ممتنّ.",
        "Feeling verbs: شعرَ، أحبَّ، خافَ، فاجأَ.",
        "Comfort imperatives: اهدأْ، لا تخفْ، اطمئنَّ.",
        "Wisdom close: الأملُ لا يموتُ؛ الصبرُ مفتاحُ الفرجِ.",
    ],
    "The Signature read: feelings are the weather of the soul, and "
    "Arabic gives every weather a name. The Signature Language Method "
    "learns the bright and the dark alike - joy named, grief named, "
    "anger calmed by grammar itself. To comfort in another language "
    "(لا تخفْ، أنا معكَ) is the highest use of speech.",
))
ENTRIES.append(_theme_entry(
    "nature", "Arabic Nature and Weather Sentences", 6, "compounded", "Everyday Themes",
    "Twenty sentences about animals, plants, seasons, and weather talk. "
    "Weather is the universal small talk - الجوُّ جميلٌ اليومَ opens a "
    "thousand conversations.",
    S_NATURE, ["شمس", "قمر", "مطر", "شجرة", "بحر"],
    "Nature sentences teach the sky vocabulary (شمس، قمر، نجوم، سماء) "
    "and weather verbs (تمطرُ، تشرقُ، يغطي). Animal sentences (عصفور، "
    "قطة، كلب، حصان، جمل) carry the famous metaphors: الجملُ سفينةُ "
    "الصحراءِ. The set closes on stewardship: حافظْ على البيئةِ "
    "نظيفةً.",
    [
        "20 sentences: animals, plants, seasons, weather.",
        "Sky core: شمس، قمر، نجوم، سماء.",
        "Weather verbs: تمطرُ، تشرقُ، تلمعُ، يغطي.",
        "Animal metaphors: الجملُ سفينةُ الصحراءِ.",
        "Stewardship close: حافظْ على البيئةِ نظيفةً.",
    ],
    "The Signature read: nature is the first textbook - sun, moon, "
    "and rain taught humans before any school. The Signature Language "
    "Method learns the sky first, then the weather that falls from "
    "it, then the creatures that live under it. The camel as ship of "
    "the desert is not decoration; it is how a desert people think.",
))
ENTRIES.append(_theme_entry(
    "shopping", "Arabic Shopping and Money Sentences", 7, "compounded", "Everyday Themes",
    "Twenty sentences about the market, prices, bargaining, and paying. "
    "The souk is a language school where every lesson has a price tag - "
    "المساومةُ جزءٌ من التسوقِ (bargaining is part of shopping).",
    S_SHOPPING, ["سعر", "سوق", "مال", "خصم", "بطاقة"],
    "Shopping sentences teach the price question (كم سعرُ...؟) and the "
    "bargaining dance: هذا غالٍ جداً → أعطني سعرَكَ الأخيرَ → اتفقْنا. "
    "Payment vocabulary (نقداً، بطاقة، فاتورة) and return language "
    "(أريدُ إرجاعَ هذا) complete the transaction. Numbers do heavy "
    "lifting here - مائةُ ريالٍ in living use.",
    [
        "20 sentences: market, prices, bargaining, paying.",
        "Price core: كم سعرُ...؟، السعرُ، خصمٌ، غالٍ، رخيصٌ.",
        "Bargaining arc: غالٍ جداً → سعرَكَ الأخيرَ → اتفقْنا.",
        "Payment: نقداً (cash)، بطاقة (card)، فاتورة (bill).",
        "Market wisdom: المساومةُ جزءٌ من التسوقِ.",
    ],
    "The Signature read: the market is the arena where language "
    "becomes leverage. The Signature Language Method teaches the "
    "souk as a negotiation drill: ask the price, wince, counter, "
    "close. Every price is a sentence, every bargain a dialogue won. "
    "اتفقْنا is the handshake that ends the bout.",
))
ENTRIES.append(_theme_entry(
    "social", "Arabic Friendship and Social Life Sentences", 7, "compounded", "Everyday Themes",
    "Twenty sentences about meeting people, invitations, and "
    "celebrations. Arab social life runs on hospitality - تفضّلْ "
    "بالدخولِ (please come in) is never just words.",
    S_SOCIAL, ["صديق", "حفل", "زواج", "دعوة", "مبارك"],
    "Social sentences teach introductions (تشرّفتُ بمعرفتِكَ، من أين "
    "أنتَ؟) and the personal questions that follow (كم عمرُكَ؟، هل "
    "أنتَ متزوجٌ؟). Invitations (أدعوكَ إلى...) and congratulations "
    "(مباركٌ...) are fixed social formulas - learn them whole. "
    "Hospitality imperatives (تفضّلْ، اشربْ) turn grammar into "
    "generosity.",
    [
        "20 sentences: meeting people, invitations, celebrations.",
        "Introduction core: تشرّفتُ بمعرفتِكَ، من أين أنتَ؟",
        "Invitation formula: أدعوكَ إلى حفلِ...",
        "Congratulations: مباركٌ الزواجُ / مباركٌ النجاحُ.",
        "Hospitality imperatives: تفضّلْ، اشربْ.",
    ],
    "The Signature read: friendship is the sworn alliance of "
    "peacetime. The Signature Language Method learns the social "
    "formulas as ceremonies: the introduction, the invitation, the "
    "congratulation, the farewell that promises return (نبقى على "
    "تواصلٍ). الصداقةُ كنزٌ ثمينٌ - and the language is how the "
    "treasure is kept.",
))
ENTRIES.append(_theme_entry(
    "tech", "Arabic Technology and Communication Sentences", 7, "compounded", "Everyday Themes",
    "Twenty sentences about the phone, internet, computer, and "
    "messaging. Modern life in Modern Standard Arabic - the language "
    "absorbs technology with borrowed words (واي فاي، إنترنت، تطبيق) "
    "and native verbs (حمّلَ، حدّثَ، شاركَ).",
    S_TECH, ["هاتف", "إنترنت", "حاسوب", "رسالة", "تطبيق"],
    "Tech sentences mix loanwords (واي فاي، إنترنت، تطبيق) with native "
    "grammar - the nouns are foreign, the verbs are Arabic: حمّلتُ "
    "تطبيقاً، حدّثْ نظامَ التشغيلِ. Troubleshooting teaches the "
    "fix-it imperative chain: أعدْ تشغيلَ الجهازِ. Safety closes the "
    "set: احذرْ من الرسائلِ الاحتياليةِ.",
    [
        "20 sentences: phone, internet, computer, messaging.",
        "Loanwords + Arabic verbs: حمّلَ تطبيقاً، حدّثَ النظامَ.",
        "Troubleshooting imperatives: أعدْ تشغيلَ الجهازِ.",
        "Communication core: رسالة، اتصلْ، شاركَ، تابعْ.",
        "Safety close: احذرْ من الرسائلِ الاحتياليةِ.",
    ],
    "The Signature read: the machine is the newest member of the "
    "household, and Arabic adopts it without surrendering - foreign "
    "nouns, native verbs. The Signature Language Method treats tech "
    "speech as command speech: charge, update, restart, save. The "
    "phone obeys Arabic grammar now; that is the real download.",
))


# ---------------------------------------------------------------- record 21: verb tenses

TENSE_PAST = [
    ("كتبتُ رسالةً إلى صديقي", "katabtu risālatan ilā ṣadīqī", "I wrote a letter to my friend"),
    ("قرأَ الطلابُ الدرسَ أمسِ", "qaraʾa ṭ-ṭullābu d-darsa amsi", "The students read the lesson yesterday"),
    ("ذهبْنا إلى السوقِ صباحاً", "dhahabnā ilā s-sūqi ṣabāḥan", "We went to the market in the morning"),
    ("شربتْ أمي الشايَ", "sharibat ummī sh-shāya", "My mother drank the tea"),
    ("نامَ الأطفالُ مبكراً", "nāma l-aṭfālu mubakkiran", "The children slept early"),
    ("فتحَ المحلُّ أبوابَهُ", "fataḥa l-maḥallu abwābahu", "The shop opened its doors"),
]
TENSE_PRESENT = [
    ("أكتبُ واجبي الآنَ", "aktubu wājibī l-āna", "I am writing my homework now"),
    ("يقرأُ أخي كتاباً ممتعاً", "yaqraʾu akhī kitāban mumtiʿan", "My brother is reading an enjoyable book"),
    ("تذهبُ إلى العملِ بالحافلةِ", "tadhhabu ilā l-ʿamali bil-ḥāfilati", "She goes to work by bus"),
    ("نشربُ القهوةَ كلَّ صباحٍ", "nashrabu l-qahwata kulla ṣabāḥin", "We drink coffee every morning"),
    ("يلعبونَ كرةَ القدمِ مساءً", "yalʿabūna kurata l-qadami masāʾan", "They play football in the evening"),
    ("تدرسينَ بجدٍّ يا ابنتي", "tadrusīna bijiddin yā bnatī", "You study hard, my daughter"),
]
TENSE_FUTURE = [
    ("سأكتبُ لكَ غداً", "saʾaktubu laka ghadan", "I will write to you tomorrow"),
    ("سوف نسافرُ في الصيفِ", "sawfa nusāfiru fī ṣ-ṣayfi", "We will travel in the summer"),
    ("سيقرأُ التقريرَ الليلةَ", "saqraʾu t-taqrīra l-laylata", "He will read the report tonight"),
    ("ستنجحُ بإذنِ اللهِ", "satanjaḥu biʾidhni llāhi", "You will succeed, God willing"),
    ("سأتصلُ بكَ عندما أصلُ", "saʾattaṣilu bika ʿindamā aṣilu", "I will call you when I arrive"),
    ("لن أنسى هذا اليومَ أبداً", "lan ansā hādhā l-yawma abadan", "I will never forget this day"),
]
# present-tense conjugation of kataba (stem -ktub-): 13 persons
TENSE_PRESENT_TABLE = [
    ("أنا", "aktubu", "أكتبُ"), ("نحن", "naktubu", "نكتبُ"),
    ("أنتَ", "taktubu", "تكتبُ"), ("أنتِ", "taktubīna", "تكتبينَ"),
    ("أنتما", "taktubāni", "تكتبانِ"), ("أنتم", "taktubūna", "تكتبونَ"),
    ("أنتنَّ", "taktubna", "تكتبنَ"), ("هو", "yaktubu", "يكتبُ"),
    ("هي", "taktubu", "تكتبُ"), ("هما", "yaktubāni", "يكتبانِ"),
    ("هما-2", "taktubāni", "تكتبانِ"), ("هم", "yaktubūna", "يكتبونَ"),
    ("هنَّ", "yaktubna", "يكتبنَ"),
]

ENTRIES.append({
    "key": "tenses",
    "name": "Arabic Verb Tenses in Sentences",
    "group": "Grammar in Action",
    "ladder_rank": 8,
    "ladder_tier": "compounded",
    "description": (
        "The three tenses of Arabic - past (الماضي), present (المضارع), "
        "future (سـ/سوف + present) - with six translated sentences each, "
        "built on the verbs you already know.\n"
        "Past (completed action; suffixes on the stem):\n" +
        _sent_lines(TENSE_PAST) + "\n"
        "Present (happening now or habitually; prefixes + suffixes):\n" +
        _sent_lines(TENSE_PRESENT) + "\n"
        "Future (سـ or سوف before the present; لن + subjunctive for "
        "negative future):\n" + _sent_lines(TENSE_FUTURE) + "\n"
        "Full present-tense table of كتبَ (to write) - 13 persons:\n" +
        "\n".join("  %s: %s (%s)" % (p, a, t) for p, t, a in TENSE_PRESENT_TABLE) + "\n"
        "Rule of thumb: past tells what finished, present tells what is "
        "or always happens, سـ/سوف points forward, and لن أنسى-style "
        "negation is the strongest promise in the language. Negation "
        "picks its particle by tense: لم أكتبْ (I did not write)، لن "
        "أكتبَ (I will not write)، لا أكتبُ (I do not write)."
    ),
    "how_it_works": (
        "Arabic has two stems and builds time around them. The past "
        "stem + suffixes = completed: katab-tu (I wrote). The present "
        "stem + prefixes (+ endings) = ongoing or habitual: a-ktub-u (I "
        "write / am writing). Future is just the present with a "
        "forward-marker: sa-ktub-u or sawfa aktubu (I will write). "
        "Negation chooses by tense: lam + jussive erases the past (lam "
        "aktub = I did not write), lan + subjunctive bars the future "
        "(lan aktuba = I will not write), lā + present denies the "
        "habit (lā aktubu = I do not write). Master the 13-person "
        "table for one verb and every verb follows."
    ),
    "key_points": [
        "Past = stem + suffixes (katabtu = I wrote); 6 sentences above.",
        "Present = prefixes + stem + endings (aktubu = I write); 6 sentences above.",
        "Future = سـ or سوف + present (سأكتبُ = I will write); 6 sentences above.",
        "Negative past: لم + jussive (لم أكتبْ). Negative future: لن + subjunctive (لن أكتبَ).",
        "13-person present table of كتبَ given in full above.",
        "Present covers both I write and I am writing - context decides.",
        "Imperative preview: the command grows from the present stem (اكتبْ).",
    ],
    "requirements": [
        "Conjugate كتبَ in past and present for all 13 persons from memory.",
        "Convert each past sentence above into present and future.",
        "Write 3 negations per tense using لم، لن، لا correctly.",
    ],
    "standards": [
        "Tense system per Wright 1896; Ryding 2005.",
    ],
    "citations": [CIT_WRIGHT, CIT_RYDING],
    "sig_lens": (
        "The Signature read: time is the third dimension of the verb - "
        "past sealed, present marching, future sworn. The Signature "
        "Language Method drills the 13-person table as a formation "
        "review: every person present, every ending in place. سـ is the "
        "banner raised before the march; لن is the oath that bars "
        "retreat."
    ),
    "drill": {
        "past": TENSE_PAST, "present": TENSE_PRESENT, "future": TENSE_FUTURE,
        "table": TENSE_PRESENT_TABLE, "persons": 13,
    },
    "must_contain": ["سأكتبُ لكَ غداً", "لم أكتبْ", "تكتبونَ", "الماضي", "المضارع"],
})

# ---------------------------------------------------------------- record 22: questions & answers

QA_PAIRS = [
    ("من أنتَ؟", "man anta؟", "Who are you", "أنا طالبٌ من اليمنِ", "anā ṭālibun mina l-yamani", "I am a student from Yemen"),
    ("ما اسمُكَ؟", "mā smuka؟", "What is your name", "اسمي خالدٌ", "ismī khālidun", "My name is Khalid"),
    ("ماذا تعملُ؟", "mādhā taʿmalu؟", "What do you do", "أعملُ مهندساً", "aʿmalu muhandisan", "I work as an engineer"),
    ("أين تسكنُ؟", "ayna taskunu؟", "Where do you live", "أسكنُ في دبي", "askunu fī dubayy", "I live in Dubai"),
    ("متى وصلتَ؟", "matā waṣalta؟", "When did you arrive", "وصلتُ أمسِ مساءً", "waṣaltu amsi masāʾan", "I arrived yesterday evening"),
    ("لماذا تأخرتَ؟", "limādhā taʾakhkharta؟", "Why were you late", "تأخرتُ بسببِ الزحامِ", "taʾakhkhartu bisababi z-ziḥāmi", "I was late because of traffic"),
    ("كيف حالُ عائلتِكَ؟", "kayfa ḥālu ʿāʾilatika؟", "How is your family", "عائلتي بخيرٍ، الحمدُ للهِ", "ʿāʾilatī bikhayrin, al-ḥamdu lillāhi", "My family is fine, praise God"),
    ("كم الساعةُ الآنَ؟", "kam as-sāʿatu l-āna؟", "What time is it now", "الساعةُ الثالثةُ", "as-sāʿatu th-thālithatu", "It is three oclock"),
    ("هل تتكلمُ العربيةَ؟", "hal tatakallamu l-ʿarabiyyata؟", "Do you speak Arabic", "نعم، أتكلمُ العربيةَ قليلاً", "naʿam, atakallamu l-ʿarabiyyata qalīlan", "Yes, I speak a little Arabic"),
    ("هل تحبُّ القهوةَ؟", "hal tuḥibbu l-qahwata؟", "Do you like coffee", "نعم، أحبُّها كثيراً", "naʿam, uḥibbuhā kathīran", "Yes, I like it a lot"),
    ("أيُّ كتابٍ تقرأُ؟", "ayyu kitābin taqraʾu؟", "Which book are you reading", "أقرأُ روايةً تاريخيةً", "aqraʾu riwāyatan tārīkhiyyatan", "I am reading a historical novel"),
    ("بكم اشتريتَ السيارةَ؟", "bikam ishtarayta s-sayyārata؟", "For how much did you buy the car", "اشتريتُها بعشرين ألفاً", "ishtaraytuhā biʿishrīna alfan", "I bought it for twenty thousand"),
    ("من أين اشتريتَ هذا؟", "min ayna ishtarayta hādhā؟", "Where did you buy this from", "اشتريتُهُ من السوقِ القديمِ", "ishtaraytuhu mina s-sūqi l-qadīmi", "I bought it from the old market"),
    ("ماذا تريدُ أن تأكلَ؟", "mādhā turīdu an taʾkula؟", "What do you want to eat", "أريدُ مشوياتٍ مشكّلةً", "urīdu mashwiyyātin mushakkalatan", "I want mixed grills"),
    ("أين تعلّمتَ العربيةَ؟", "ayna taʿallamta l-ʿarabiyyata؟", "Where did you learn Arabic", "تعلّمتُها في معهدِ اللغاتِ", "taʿallamtuhā fī maʿhadi l-lughāti", "I learned it at the language institute"),
    ("هل زرتَ مصرَ من قبلُ؟", "hal zurta miṣra min qablu؟", "Have you visited Egypt before", "لا، لم أزرْها بعدُ", "lā, lam azurhā baʿdu", "No, I have not visited it yet"),
    ("ما رأيُكَ في الطعامِ؟", "mā raʾyuka fī ṭ-ṭaʿāmi؟", "What do you think of the food", "الطعامُ لذيذٌ جداً", "aṭ-ṭaʿāmu ladhīdhun jiddan", "The food is very delicious"),
    ("كيف أصلُ إلى المطارِ؟", "kayfa aṣilu ilā l-maṭāri؟", "How do I get to the airport", "خذْ سيارةَ أجرةٍ من أمامِ الفندقِ", "khudh sayyārata ujratin min amāmi l-funduqi", "Take a taxi from in front of the hotel"),
    ("متى يفتحُ المتحفُ؟", "matā yaftaḥu l-matḥafu؟", "When does the museum open", "يفتحُ في التاسعةِ صباحاً", "yaftaḥu fī t-tāsiʿati ṣabāḥan", "It opens at nine in the morning"),
    ("هل يمكنُكَ مساعدتي؟", "hal yumkinuka musāʿadatī؟", "Can you help me", "بكلِّ سرورٍ، تفضّلْ", "bikulli surūrin, tafaḍḍal", "Gladly, please go ahead"),
]

ENTRIES.append({
    "key": "qa",
    "name": "Arabic Questions and Answers",
    "group": "Grammar in Action",
    "ladder_rank": 8,
    "ladder_tier": "compounded",
    "description": (
        "Twenty question-and-answer pairs covering who, what, where, "
        "when, why, and how. Each pair shows the full question and a "
        "natural full-sentence answer - because answering in fragments "
        "is the habit this record breaks.\n" +
        "\n".join("  س: %s (%s) — %s؟\n  ج: %s (%s) — %s." % (q, qt, qe, a, at, ae)
                  for q, qt, qe, a, at, ae in QA_PAIRS)
    ),
    "how_it_works": (
        "Questions are built two ways. Yes-no questions front هل "
        "(hal): هل تتكلمُ العربيةَ؟ Information questions front the "
        "question word: من (who)، ما/ماذا (what)، أين (where)، متى "
        "(when)، لماذا (why)، كيف (how)، كم (how many)، أيّ (which). "
        "Answers mirror the question's verb and tense: سؤال بالماضي "
        "يُجاب بالماضي (a past question gets a past answer). Notice لم "
        "أزرْها in the Egypt answer - negative past with لم + jussive, "
        "the verb losing its vowel, exactly as record 10 taught."
    ),
    "key_points": [
        "20 Q/A pairs: who/what/where/when/why/how/which/how much.",
        "هل = yes-no question marker; question words front information questions.",
        "Answers mirror the questions verb and tense.",
        "نعم/لا open yes-no answers; لم + jussive for negative past.",
        "Question words: من ما ماذا أين متى لماذا كيف كم أيّ.",
        "Full-sentence answers - never fragments.",
    ],
    "requirements": [
        "Ask a partner all 20 questions; answer each in a full sentence.",
        "Write 5 new pairs of your own about your life.",
        "Convert 5 هل questions into question-word questions.",
    ],
    "standards": [
        "Question formation per Wright 1896; Ryding 2005.",
    ],
    "citations": [CIT_WRIGHT, CIT_RYDING],
    "sig_lens": (
        "The Signature read: the question is the scout sent ahead - "
        "small, fast, and it must return with the answer. The Signature "
        "Language Method pairs every question with its sworn reply, "
        "because a question asked and unanswered is a mission failed. "
        "Twenty scouts, twenty reports, no one left behind."
    ),
    "drill": {"pairs": QA_PAIRS, "count": 20,
              "qwords": ["من", "ما", "ماذا", "أين", "متى", "لماذا", "كيف", "كم", "أي", "هل", "بكم"]},
    "must_contain": ["س: من أنتَ؟", "ج: اسمي خالدٌ", "بكم اشتريتَ السيارةَ؟", "هل يمكنُكَ مساعدتي؟"],
})

# ---------------------------------------------------------------- record 23: commands & requests

COMMANDS = [
    ("اجلسْ هنا من فضلكَ", "ijlis hunā min faḍlika", "Sit here please", False, "polite request, softened with من فضلكَ"),
    ("افتحْ البابَ", "iftaḥ al-bāba", "Open the door", False, "direct command to one person"),
    ("اكتبْ واجبَكَ الآنَ", "uktub wājibaka l-āna", "Write your homework now", False, "parent to child, direct"),
    ("اشربْ الشايَ", "ishrab ash-shāya", "Drink the tea", False, "hospitality imperative"),
    ("تفضّلوا بالدخولِ", "tafaḍḍalū bid-dukhūli", "Please come in (plural/formal)", True, "plural form = formal respect"),
    ("هل يمكنُكَ أن تساعدَني؟", "hal yumkinuka an tusāʿidanī؟", "Could you help me", True, "formal request with هل يمكنُكَ"),
    ("لو سمحتَ، أين الحمّامُ؟", "law samaḥta, ayna l-ḥammāmu؟", "Excuse me, where is the bathroom", True, "لو سمحتَ softens any request"),
    ("أغلقْ النافذةَ", "aghliq an-nāfidhata", "Close the window", False, "direct command"),
    ("انتظرْ قليلاً", "intaẓir qalīlan", "Wait a little", False, "direct command"),
    ("تعالَ إلى هنا", "taʿāla ilā hunā", "Come here", False, "direct command"),
    ("اذهبْ إلى السوقِ", "idhhab ilā s-sūqi", "Go to the market", False, "direct command"),
    ("كُلْ طعامَكَ", "kul ṭaʿāmaka", "Eat your food", False, "direct command"),
    ("اشربْ دواءَكَ", "ishrab dawāʾaka", "Take your medicine", False, "direct command"),
    ("ناموا مبكراً يا أولادُ", "nāmū mubakkiran yā awlādu", "Sleep early, children", False, "plural command to children"),
    ("احترمْ والديكَ", "iḥtarim wālidayka", "Respect your parents", True, "moral imperative, formal weight"),
    ("من فضلِكَ، تحدّثْ ببطءٍ", "min faḍlika, taḥaddath bibuṭʾin", "Please speak slowly", True, "request to a stranger, formal"),
    ("أعطني الفاتورةَ لو سمحتَ", "aʿṭinī l-fātūrata law samaḥta", "Give me the bill please", True, "service request, polite"),
    ("لا تتأخرْ عن الموعدِ", "lā tataʾakhkhar ʿani l-mawʿidi", "Do not be late for the appointment", True, "negative command with لا"),
    ("ساعدْ أخاكَ في دروسِهِ", "sāʿid akhāka fī durūsihi", "Help your brother with his lessons", False, "family imperative"),
    ("حافظْ على نظافةِ مدينتِكَ", "ḥāfiẓ ʿalā naẓāfati madīnatika", "Keep your city clean", True, "civic imperative, formal address"),
]

ENTRIES.append({
    "key": "commands",
    "name": "Arabic Commands and Requests",
    "group": "Grammar in Action",
    "ladder_rank": 8,
    "ladder_tier": "compounded",
    "description": (
        "Twenty imperatives and polite requests, each marked formal or "
        "informal with a usage note. Arabic commands are direct by "
        "default - politeness is added with من فضلكَ، لو سمحتَ, or the "
        "plural/formal address.\n" +
        "\n".join("  %s (%s) — %s. [%s] %s." % (a, t, e, "formal" if f else "informal", n)
                  for a, t, e, f, n in COMMANDS) + "\n"
        "Formal markers to memorize: the plural address (تفضّلوا), هل "
        "يمكنُكَ...؟ (could you...?), لو سمحتَ (if you permit), من "
        "فضلِكَ (please). Negative commands use لا + present: لا "
        "تتأخرْ (do not be late)."
    ),
    "how_it_works": (
        "The imperative grows from the present stem: yaktub-u → uktub "
        "(write!). Its shape depends on the addressee: masculine "
        "singular (اكتبْ), feminine singular (اكتبي), plural (اكتبوا). "
        "Formality in Arabic is not a separate verb form - it is built "
        "with softeners (من فضلكَ، لو سمحتَ), question-form requests "
        "(هل يمكنُكَ), or plural address to one respected person "
        "(تفضّلوا). The negative imperative is لا + jussive: لا تفعلْ "
        "(do not do). Commands to children and friends stay bare and "
        "direct; commands to strangers wear their manners."
    ),
    "key_points": [
        "20 imperatives/requests: 8 formal, 12 informal - each labeled.",
        "Imperative forms: اكتبْ (m)، اكتبي (f)، اكتبوا (pl).",
        "Politeness via softeners: من فضلكَ، لو سمحتَ.",
        "Formal requests: هل يمكنُكَ أن...؟ / plural address.",
        "Negative command: لا + jussive (لا تتأخرْ).",
        "Hospitality imperatives (اشربْ، تفضّلْ) are warmth, not orders.",
    ],
    "requirements": [
        "Conjugate the imperative of فتحَ، ذهبَ، جلسَ for m/f/pl.",
        "Turn 5 informal commands above into formal requests.",
        "Role-play: give 10 commands, refuse 5 politely with لا + reason.",
    ],
    "standards": [
        "Imperative morphology per Wright 1896; Ryding 2005.",
    ],
    "citations": [CIT_WRIGHT, CIT_RYDING],
    "sig_lens": (
        "The Signature read: the command is the order given - short, "
        "clear, and obeyed. But the Signature Language Method teaches "
        "the two uniforms of command: the bare order for the trusted "
        "(اجلسْ) and the honored request for the stranger (هل يمكنُكَ). "
        "A commander who cannot ask politely cannot command at all."
    ),
    "drill": {"items": COMMANDS, "count": 20,
              "formal": 8, "informal": 12},
    "must_contain": ["تفضّلوا بالدخولِ", "لا تتأخرْ عن الموعدِ", "اكتبْ واجبَكَ الآنَ", "هل يمكنُكَ أن تساعدَني؟"],
})

# ---------------------------------------------------------------- record 24: descriptions

DESCRIPTIONS = [
    ("أخي طويلٌ ونحيفٌ، عيناه خضراوان", "akhī ṭawīlun wa naḥīfun, ʿaynāhu khaḍrāwān", "My brother is tall and thin, his eyes are green"),
    ("أمي امرأةٌ حنونةٌ، وجهُها مشرقٌ دائماً", "ummī mraʾatun ḥanūnatun, wajhuhā mushriqun dāʾiman", "My mother is a kind woman, her face always bright"),
    ("صديقي خالدٌ ذكيٌّ ومرحٌ", "ṣadīqī khālidun dhakiyyun wa mariḥun", "My friend Khalid is smart and cheerful"),
    ("المعلمةُ الجديدةُ صارمةٌ لكن عادلةٌ", "al-muʿallimatu l-jadīdatu ṣārimatun lākin ʿādilatun", "The new teacher is strict but fair"),
    ("الطفلُ الصغيرُ يضحكُ بصوتٍ عالٍ", "aṭ-ṭiflu ṣ-ṣaghīru yaḍḥaku biṣawtin ʿālin", "The little child laughs loudly"),
    ("الرجلُ العجوزُ حكيمٌ ومحترمٌ", "ar-rajulu l-ʿajūzu ḥakīmun wa muḥtaramun", "The old man is wise and respected"),
    ("الفتاةُ ترتدي فستاناً أحمرَ جميلاً", "al-fatātu tartadī fustānan aḥmara jamīlan", "The girl wears a beautiful red dress"),
    ("اللاعبُ سريعٌ وقويٌّ", "al-lāʿibu sarīʿun wa qawiyyun", "The player is fast and strong"),
    ("بيتُنا القديمُ مليءٌ بالذكرياتِ", "baytunā l-qadīmu malīʾun bidh-dhikrayāti", "Our old house is full of memories"),
    ("المدينةُ القديمةُ ساحرةٌ بأزقتِها الضيقةِ", "al-madīnatu l-qadīmatu sāḥiratun biʾaziqqatihā ḍ-ḍayyiqati", "The old city is charming with its narrow alleys"),
    ("الحديقةُ العامةُ واسعةٌ وخضراءُ", "al-ḥadīqatu l-ʿāmmatu wāsiʿatun wa khaḍrāʾu", "The public garden is spacious and green"),
    ("المسجدُ الكبيرُ تحفةٌ معماريةٌ", "al-masjidu l-kabīru tuḥfatun miʿmāriyyatun", "The grand mosque is an architectural masterpiece"),
    ("السوقُ القديمُ مزدحمٌ وملوّنٌ", "as-sūqu l-qadīmu muzdaḥimun wa mulawwanun", "The old market is crowded and colorful"),
    ("الجامعةُ حديثةٌ ومجهّزةٌ بأفضلِ المختبراتِ", "al-jāmiʿatu ḥadīthatun wa mujahhazatun biʾafḍali l-mukhtabarāti", "The university is modern, equipped with the best labs"),
    ("الشاطئُ نظيفٌ والمياهُ صافيةٌ", "ash-shāṭiʾu naẓīfun wal-miyāhu ṣāfiyatun", "The beach is clean and the water is clear"),
    ("الجبلُ الشاهقُ يغطيهِ الثلجُ", "al-jabalu sh-shāhiqu yughaṭṭīhi th-thalju", "The towering mountain is covered with snow"),
    ("القريةُ هادئةٌ وهواؤُها نقيٌّ", "al-qaryatu hādiʾatun wa hawāʾuhā naqiyyun", "The village is quiet and its air is pure"),
    ("المطعمُ الجديدُ أنيقٌ وأسعارُهُ معقولةٌ", "al-maṭʿamu l-jadīdu anīqun wa asʿāruhu maʿqūlatun", "The new restaurant is elegant and its prices are reasonable"),
    ("الكتابُ ممتعٌ وأسلوبُهُ سهلٌ", "al-kitābu mumtiʿun wa uslūbuhu sahlun", "The book is enjoyable and its style is easy"),
    ("الليلُ هادئٌ والنجومُ ساطعةٌ", "al-laylu hādiʾun wan-nujūmu sāṭiʿatun", "The night is quiet and the stars are bright"),
]

ENTRIES.append({
    "key": "descriptions",
    "name": "Arabic Descriptions of People and Places",
    "group": "Grammar in Action",
    "ladder_rank": 9,
    "ladder_tier": "compounded",
    "description": (
        "Twenty sentences describing people, places, and things in "
        "detail - the adjective-agreement workout. Every sentence "
        "stacks two or three descriptive phrases, forcing gender, "
        "number, and definiteness to agree across the whole line.\n" +
        _sent_lines(DESCRIPTIONS) + "\n"
        "Watch the agreement chains: المعلمةُ الجديدةُ صارمةٌ (feminine "
        "throughout)، السوقُ القديمُ مزدحمٌ (masculine throughout). "
        "Possession adds a second agreement center: وجهُها مشرقٌ "
        "(her face [m] is bright [m]) inside a sentence about أمي "
        "(feminine)."
    ),
    "how_it_works": (
        "Description in Arabic is agreement under load. Each adjective "
        "must match its noun in gender, number, and definiteness, and "
        "a sentence with two nouns runs two agreement chains at once. "
        "The descriptive sentence has two molds: the equational (X is "
        "Y: أخي طويلٌ) with no verb, and the verbal (X does Y-ly: "
        "يضحكُ بصوتٍ عالٍ). Colors and physical traits use the special "
        "afʿal pattern: أحمر، أخضر، أزرق (m) → حمراء، خضراء، زرقاء "
        "(f). Stack the patterns and the picture appears."
    ),
    "key_points": [
        "20 detailed descriptive sentences, each with 2-3 agreeing phrases.",
        "Agreement chains run the full sentence: gender, number, definiteness.",
        "Equational mold (أخي طويلٌ) and verbal mold (يضحكُ بصوتٍ عالٍ).",
        "Color pattern afʿal: أحمر/حمراء، أخضر/خضراء.",
        "Possession creates second agreement centers (وجهُها مشرقٌ).",
        "لكن (but) pivots description: صارمةٌ لكن عادلةٌ.",
    ],
    "requirements": [
        "Describe 3 people and 3 places you know, 3 sentences each.",
        "Underline every agreement chain in the 20 sentences.",
        "Convert 5 equational sentences to verbal ones.",
    ],
    "standards": [
        "Agreement rules per Wright 1896; Ryding 2005.",
    ],
    "citations": [CIT_WRIGHT, CIT_RYDING],
    "sig_lens": (
        "The Signature read: description is the portrait painted in "
        "sworn colors - every adjective standing inspection beside its "
        "noun. The Signature Language Method paints with agreement: no "
        "color out of uniform, no trait unattached. Twenty portraits, "
        "each witnessed twice - by grammar and by meaning."
    ),
    "drill": {"items": DESCRIPTIONS, "count": 20},
    "must_contain": ["خضراوان", "بأزقتِها الضيقةِ", "النجومُ ساطعةٌ"],
})


# ---------------------------------------------------------------- records 25-27: stories

STORY1 = [
    ("في صباحِ يومٍ مشمسٍ، استيقظَ أحمدُ مبكراً", "fī ṣabāḥi yawmin mushmisin, istayqaẓa aḥmadu mubakkiran", "On a sunny morning, Ahmed woke up early"),
    ("غسلَ وجهَهُ وتناولَ فطوراً خفيفاً", "ghasala wajhahu wa tanāwala fuṭūran khafīfan", "He washed his face and had a light breakfast"),
    ("خرجَ إلى الحديقةِ وسقى الأزهارَ", "kharaja ilā l-ḥadīqati wa saqā l-azhāra", "He went out to the garden and watered the flowers"),
    ("ثم جلسَ تحتَ الشجرةِ يقرأُ كتابَهُ المفضلَ", "thumma jalasa taḥta sh-shajarati yaqraʾu kitābahu l-mufaḍḍala", "Then he sat under the tree reading his favorite book"),
    ("عندَ الظهرِ، جاءَ صديقُهُ خالدٌ لزيارتِهِ", "ʿinda ẓ-ẓuhri, jāʾa ṣadīquhu khālidun liziyāratihi", "At noon, his friend Khalid came to visit him"),
    ("تناولا الغداءَ معاً وتحدثا عن المدرسةِ", "tanāwalā l-ghadāʾa maʿan wa taḥaddathā ʿani l-madrasati", "They had lunch together and talked about school"),
    ("بعدَ الغداءِ، لعبا كرةَ القدمِ في الحديقةِ", "baʿda l-ghadāʾi, laʿibā kurata l-qadami fī l-ḥadīqati", "After lunch, they played football in the garden"),
    ("في المساءِ، عادَ أحمدُ إلى البيتِ سعيداً", "fī l-masāʾi, ʿāda aḥmadu ilā l-bayti saʿīdan", "In the evening, Ahmed returned home happy"),
    ("تناولَ العشاءَ مع عائلتِهِ وحكى لهم عن يومِهِ", "tanāwala l-ʿashāʾa maʿa ʿāʾilatihi wa ḥakā lahum ʿan yawmihi", "He had dinner with his family and told them about his day"),
    ("نامَ مبكراً وهو يحلمُ بيومٍ أجملَ", "nāma mubakkiran wa huwa yaḥlumu biyawmin ajmala", "He slept early, dreaming of an even more beautiful day"),
]
STORY2 = [
    ("في الصيفِ الماضي، سافرَ أحمدُ مع عائلتِهِ إلى الإسكندريةِ", "fī ṣ-ṣayfi l-māḍī, sāfara aḥmadu maʿa ʿāʾilatihi ilā l-iskandariyyati", "Last summer, Ahmed traveled with his family to Alexandria"),
    ("ركبوا القطارَ في الصباحِ الباكرِ", "rakibū l-qiṭāra fī ṣ-ṣabāḥi l-bākiri", "They boarded the train in the early morning"),
    ("وصلوا إلى الفندقِ عندَ الظهرِ", "waṣalū ilā l-funduqi ʿinda ẓ-ẓuhri", "They arrived at the hotel at noon"),
    ("بعدَ الراحةِ، ذهبوا إلى شاطئِ البحرِ", "baʿda r-rāḥati, dhahabū ilā shāṭiʾi l-baḥri", "After resting, they went to the seashore"),
    ("سبحَ أحمدُ في المياهِ الصافيةِ", "sabaḥa aḥmadu fī l-miyāhi ṣ-ṣāfiyati", "Ahmed swam in the clear water"),
    ("بنى مع أختِهِ قلعةً من الرمالِ", "banā maʿa ukhtihi qalʿatan mina r-rimāli", "He built a sandcastle with his sister"),
    ("في المساءِ، تناولوا السمكَ المشويَّ في مطعمٍ على الشاطئِ", "fī l-masāʾi, tanāwalū s-samaka l-mashwiyya fī maṭʿamin ʿalā sh-shāṭiʾi", "In the evening, they ate grilled fish at a beach restaurant"),
    ("اشتروا هدايا تذكاريةً من السوقِ القديمِ", "ishtaraw hadāyā tidhkāriyyatan mina s-sūqi l-qadīmi", "They bought souvenirs from the old market"),
    ("في اليومِ الأخيرِ، ودّعوا البحرَ بحزنٍ", "fī l-yawmi l-akhīri, waddaʿū l-baḥra biḥuznin", "On the last day, they bid the sea farewell with sadness"),
    ("عادوا إلى البيتِ بذكرياتٍ جميلةٍ لا تُنسى", "ʿādū ilā l-bayti bidhikrayātin jamīlatin lā tunsā", "They returned home with beautiful unforgettable memories"),
]
STORY3 = [
    ("غداً سأستيقظُ مبكراً لأن عندي امتحاناً مهماً", "ghadan saʾastayqiẓu mubakkiran liʾanna ʿindī mtiḥānan muhimman", "Tomorrow I will wake up early because I have an important exam"),
    ("سأراجعُ دروسي في المساءِ ثم سأنامُ مبكراً", "saʾurājiʿu durūsī fī l-masāʾi thumma saʾanāmu mubakkiran", "I will review my lessons in the evening, then I will sleep early"),
    ("إذا نجحتُ في الامتحانِ، سأحتفلُ مع أصدقائي", "idhā najaḥtu fī l-imtiḥāni, saʾaḥtafilu maʿa aṣdiqāʾī", "If I pass the exam, I will celebrate with my friends"),
    ("سندرسُ معاً في المكتبةِ كلَّ يومٍ", "sanadrusu maʿan fī l-maktabati kulla yawmin", "We will study together in the library every day"),
    ("سوف يساعدُني معلمي في المواضيعِ الصعبةِ", "sawfa yusāʿidunī muʿallimī fī l-mawāḍīʿi ṣ-ṣaʿbati", "My teacher will help me with the difficult topics"),
    ("بعدَ الامتحاناتِ، سنسافرُ إلى الجبلِ", "baʿda l-imtiḥānāti, sanusāfiru ilā l-jabali", "After the exams, we will travel to the mountains"),
    ("سنقيمُ في بيتٍ ريفيٍّ صغيرٍ", "sanuqīmu fī baytin rīfiyyin ṣaghīrin", "We will stay in a small countryside house"),
    ("سأتعلمُ السباحةَ في البحيرةِ", "saʾataʿallamu s-sibāḥata fī l-buḥayrati", "I will learn swimming in the lake"),
    ("لو كانَ عندي وقتٌ أكثرُ، لسافرتُ حولَ العالمِ", "law kāna ʿindī waqtun aktharu, lasāfartu ḥawla l-ʿālami", "If I had more time, I would travel around the world"),
    ("المستقبلُ مشرقٌ لمن يعملُ بجدٍّ", "al-mustaqbalu mushriqun liman yaʿmalu bijiddin", "The future is bright for whoever works hard"),
]


def _story_entry(key, name, intro, sentences, how, points, sig):
    return {
        "key": key, "name": name, "group": "Stories and Idioms",
        "ladder_rank": 9, "ladder_tier": "advanced",
        "description": intro + "\n" +
            "\n".join("  %d. %s (%s) — %s." % (i + 1, a, t, e)
                      for i, (a, t, e) in enumerate(sentences)),
        "how_it_works": how,
        "key_points": points,
        "requirements": [
            "Read the story aloud, then retell it from memory in Arabic.",
            "Translate each line back to Arabic from the English alone.",
            "Write your own 10-sentence story copying the sentence molds.",
        ],
        "standards": [
            "Story language is standard MSA narrative style.",
            "Transliteration follows ISO 233:1984.",
        ],
        "citations": [CIT_BADAWI, CIT_RYDING],
        "sig_lens": sig,
        "drill": {"sentences": sentences, "count": 10},
        "must_contain": [s[0] for s in sentences],
    }


ENTRIES.append(_story_entry(
    "story1", "Arabic Short Story I: A Simple Day",
    "A ten-sentence simple story in Arabic with line-by-line English "
    "translation. Present and past mix naturally, as in real narration - "
    "follow how the verbs carry the day forward.",
    STORY1,
    "Narration in Arabic chains events with wa (and) and thumma "
    "(then): istayqaẓa... wa tanāwala... thumma jalasa. The dual "
    "appears naturally (tanāwalā, they-two had lunch) because the "
    "story has two boys. Time markers (عندَ الظهرِ، في المساءِ) anchor "
    "each scene. Read for the chain-words first; the story skeleton "
    "is always wa-thumma-baʿda.",
    [
        "10-sentence story with line-by-line English translation.",
        "Chain-words carry narration: wa (and)، ثم (then)، بعدَ (after).",
        "Dual verbs in the wild: تناولا (they-two had lunch).",
        "Time anchors per scene: عندَ الظهرِ، في المساءِ.",
        "Simple past narration - the storytelling tense.",
    ],
    "The Signature read: the simple day is the first campaign - dawn "
    "to dusk, each hour sworn and kept. The Signature Language Method "
    "reads stories as marches: wake, wash, eat, read, play, return. "
    "Ten sentences, ten stations, the day conquered in order.",
))
ENTRIES.append(_story_entry(
    "story2", "Arabic Short Story II: A Journey in the Past",
    "A ten-sentence story in the past tense with line-by-line English "
    "translation - a family trip to Alexandria. Notice how the past "
    "tense (سافرَ، ركبوا، وصلوا) makes the whole journey feel complete "
    "and remembered.",
    STORY2,
    "Past-tense narration uses the suffix engine at full power: "
    "sāfara (he traveled)، rakibū (they boarded)، ishtaraw (they "
    "bought). Plural verbs agree with plural subjects in SVO order "
    "(ركبوا القطارَ) but stay singular after the verb in VSO (ذهبَ "
    "الطلابُ style). The story closes with a timeless passive: ذكرياتٌ "
    "لا تُنسى (memories not forgotten) - the passive voice sealing "
    "the memory.",
    [
        "10-sentence past-tense story, line-by-line translation.",
        "Past suffixes in action: سافرَ، ركبوا، اشتروا، عادوا.",
        "Travel vocabulary in narrative: قطار، فندق، شاطئ، سوق.",
        "Passive close: ذكرياتٌ لا تُنسى (unforgettable memories).",
        "Emotion in past tense: ودّعوا البحرَ بحزنٍ.",
    ],
    "The Signature read: the past journey is the campaign remembered "
    "- every verb a sealed record of ground taken. The Signature "
    "Language Method marches the past tense across real terrain: "
    "train, hotel, sea, market. What is done is sworn: سافرَ، سبحَ، "
    "عادوا - and the memories do not forget.",
))
ENTRIES.append(_story_entry(
    "story3", "Arabic Short Story III: Plans for Tomorrow",
    "A ten-sentence story using future and conditional forms with "
    "line-by-line English translation. سـ/سوف point forward; إذا and "
    "لو open the two doors of condition - the possible and the "
    "wishful.",
    STORY3,
    "Future narration: sa- prefix (سأستيقظُ) and sawfa (سوف يساعدُني) "
    "are interchangeable in meaning, سـ tighter, سوف weightier. "
    "Conditionals split: idhā + past = real possibility (إذا نجحتُ، "
    "سأحتفلُ - if I pass, I will celebrate); law + past = wishful "
    "unreal (لو كانَ عندي وقتٌ، لسافرتُ - if I had time, I would "
    "travel). The story ends on the proverb of effort: المستقبلُ "
    "مشرقٌ لمن يعملُ بجدٍّ.",
    [
        "10-sentence future/conditional story, line-by-line translation.",
        "سـ vs سوف: same future, different weight.",
        "إذا + past = real condition; لو + past = wishful condition.",
        "Future plans vocabulary: امتحان، سأسافرُ، سأتعلمُ.",
        "Wisdom close: المستقبلُ مشرقٌ لمن يعملُ بجدٍّ.",
    ],
    "The Signature read: the future is the campaign planned - every "
    "سـ a banner raised, every سوف a vow spoken aloud. إذا is the "
    "scout reporting possible ground; لو is the dream of ground "
    "uncharted. The Signature Language Method plans in Arabic the "
    "way generals plan: what will be, what would be, and the work "
    "that makes it so.",
))

# ---------------------------------------------------------------- record 28: idioms & proverbs

IDIOMS = [
    ("الصبرُ مفتاحُ الفرجِ", "aṣ-ṣabru miftāḥu l-faraji", "Patience is the key to relief", "Patience solves problems", "اصبرْ، فالصبرُ مفتاحُ الفرجِ", "Be patient, for patience is the key to relief"),
    ("من جدَّ وجدَ", "man jadda wajada", "Whoever strives, finds", "Hard work pays off", "من جدَّ وجدَ، فاجتهدْ في دراستِكَ", "Whoever strives finds, so work hard in your studies"),
    ("الوقتُ كالسيفِ", "al-waqtu kas-sayfi", "Time is like a sword", "Use time well or it cuts you (wasted time harms)", "الوقتُ كالسيفِ إن لم تقطعْهُ قطعَكَ", "Time is like a sword: if you do not cut with it, it cuts you"),
    ("العلمُ نورٌ", "al-ʿilmu nūrun", "Knowledge is light", "Knowledge illuminates life", "العلمُ نورٌ يضيءُ طريقَ المستقبلِ", "Knowledge is a light illuminating the path of the future"),
    ("الصديقُ وقتَ الضيقِ", "aṣ-ṣadīqu waqta ḍ-ḍīqi", "A friend in time of hardship", "True friends appear in hard times", "الصديقُ وقتَ الضيقِ، فساعدْهُ كما ساعدَكَ", "A friend in hardship - help him as he helped you"),
    ("الجارُ قبلَ الدارِ", "al-jāru qabla d-dāri", "The neighbor before the house", "Choose the neighborhood before the house", "اسألْ عن الجيرانِ، فالجارُ قبلَ الدارِ", "Ask about the neighbors, for the neighbor comes before the house"),
    ("يدٌ واحدةٌ لا تصفّقُ", "yadun wāḥidatun lā tuṣaffiqu", "One hand does not clap", "Cooperation is necessary", "يدٌ واحدةٌ لا تصفّقُ، فلنتعاونْ معاً", "One hand does not clap, so let us cooperate together"),
    ("خيرُ الكلامِ ما قلَّ ودلَّ", "khayru l-kalāmi mā qalla wa dalla", "The best speech is brief and meaningful", "Brevity with meaning is best", "تكلّمْ باختصارٍ، فخيرُ الكلامِ ما قلَّ ودلَّ", "Speak briefly, for the best speech is brief and meaningful"),
    ("لا تؤجّلْ عملَ اليومِ إلى الغدِ", "lā tuʾajjil ʿamala l-yawmi ilā l-ghadi", "Do not postpone todays work to tomorrow", "Do not procrastinate", "ابدأْ واجبَكَ الآنَ ولا تؤجّلْ عملَ اليومِ إلى الغدِ", "Start your homework now and do not postpone todays work to tomorrow"),
    ("الطيورُ على أشكالِها تقعُ", "aṭ-ṭuyūru ʿalā ashkālihā taqaʿu", "Birds land with their own kind", "People befriend those like them", "اخترْ أصدقاءَكَ بعنايةٍ، فالطيورُ على أشكالِها تقعُ", "Choose your friends carefully, for birds land with their own kind"),
    ("القناعةُ كنزٌ لا يفنى", "al-qanāʿatu kanzun lā yafnā", "Contentment is an unfailing treasure", "Be content with what you have", "القناعةُ كنزٌ لا يفنى، فاشكرْ ما عندَكَ", "Contentment is an unfailing treasure, so be thankful for what you have"),
    ("قطرةً قطرةً تمتلئُ الجرّةُ", "qaṭratan qaṭratan tamtaliʾu l-jarratu", "Drop by drop the jar fills", "Small efforts accumulate", "واظبْ على الدراسةِ، فقطرةً قطرةً تمتلئُ الجرّةُ", "Keep studying, for drop by drop the jar fills"),
    ("إنَّ مع العسرِ يسراً", "inna maʿa l-ʿusri yusran", "With hardship comes ease", "Hard times pass (Quranic phrasing, everyday use)", "لا تيأسْ، فإنَّ مع العسرِ يسراً", "Do not despair, for with hardship comes ease"),
    ("خيرُ جليسٍ في الزمانِ كتابُ", "khayru jalīsin fī z-zamāni kitābun", "The best companion in life is a book", "Reading is the best company", "اقرأْ كلَّ يومٍ، فخيرُ جليسٍ في الزمانِ كتابُ", "Read every day, for the best companion in life is a book"),
    ("رُبَّ ضارّةٍ نافعةٌ", "rubba ḍārratin nāfiʿatun", "Many a harm brings benefit", "Bad events can have good outcomes", "رُبَّ ضارّةٍ نافعةٌ، فلا تحزنْ", "Many a harm brings benefit, so do not grieve"),
    ("من حفرَ حفرةً لأخيهِ وقعَ فيها", "man ḥafara ḥufratan liʾakhīhi waqaʿa fīhā", "Whoever digs a pit for his brother falls into it", "Scheming backfires", "لا تكِدْ لأحدٍ، فمن حفرَ حفرةً لأخيهِ وقعَ فيها", "Do not scheme against anyone, for whoever digs a pit for his brother falls into it"),
    ("البابُ الذي يأتيكَ منهُ الريحُ سُدَّهُ واسترحْ", "al-bābu lladhī yaʾtīka minhu r-rīḥu suddahu wastariḥ", "Shut the door the wind comes from and rest", "Avoid sources of trouble", "ابتعدْ عن المشاكلِ، فالبابُ الذي يأتيكَ منهُ الريحُ سُدَّهُ واسترحْ", "Stay away from trouble - shut the door the wind comes from and rest"),
    ("الكتابُ يُقرأُ من عنوانِهِ", "al-kitābu yuqraʾu min ʿunwānihi", "The book is read from its title", "First impressions reveal much", "الكتابُ يُقرأُ من عنوانِهِ، فأحسنْ مظهرَكَ", "The book is read from its title, so mind your appearance"),
    ("العقلُ السليمُ في الجسمِ السليمِ", "al-ʿaqlu s-salīmu fī l-jismi s-salīmi", "A healthy mind in a healthy body", "Physical health supports mental health", "مارسِ الرياضةَ، فالعقلُ السليمُ في الجسمِ السليمِ", "Exercise, for a healthy mind is in a healthy body"),
    ("على قدِّ لحافِكَ مُدَّ رجليكَ", "ʿalā qaddi liḥāfika mudda rijlayka", "Stretch your legs to your blanket", "Live within your means", "لا تُسرفْ في الإنفاقِ، فعلى قدِّ لحافِكَ مُدَّ رجليكَ", "Do not overspend - stretch your legs only to your blanket"),
]

ENTRIES.append({
    "key": "idioms",
    "name": "Arabic Idioms and Proverbs",
    "group": "Stories and Idioms",
    "ladder_rank": 9,
    "ladder_tier": "advanced",
    "description": (
        "Twenty idioms and proverbs - literal translation, real meaning, "
        "and an example sentence each. Proverbs are the compressed "
        "wisdom of the language; Arabs quote them constantly, and "
        "dropping the right one at the right moment marks you as "
        "fluent in culture, not just grammar.\n" +
        "\n".join("  %s (%s)\n    حرفياً: %s.\n    المعنى: %s.\n    مثال: %s — %s."
                  % (a, t, lit, mean, xa, xe)
                  for a, t, lit, mean, xa, xe in IDIOMS)
    ),
    "how_it_works": (
        "Proverbs work by metaphor transfer: the image (sword, jar, "
        "birds, blanket) carries the lesson. Most Arabic proverbs are "
        "balanced pairs - condition and consequence in one breath: من "
        "جدَّ وجدَ (whoever strives, finds). Many use the imperative of "
        "wisdom: لا تؤجّلْ (do not postpone)، اصبرْ (be patient). Learn "
        "each proverb as a complete performance piece: the Arabic "
        "first, then the image, then the moment to use it."
    ),
    "key_points": [
        "20 idioms/proverbs: literal meaning + real meaning + example sentence.",
        "Proverb structure: balanced condition-consequence pairs.",
        "Wisdom imperatives: لا تؤجّلْ، اصبرْ، واظبْ.",
        "Metaphor images: sword (time)، jar (effort)، birds (friendship)، blanket (means).",
        "Cultural fluency: quoting proverbs marks deep competence.",
        "Use them sparingly - one per conversation is plenty.",
    ],
    "requirements": [
        "Memorize 10 proverbs with their images and moments.",
        "Use 3 proverbs in real or role-played conversation this week.",
        "Explain each proverbs image to someone else in Arabic.",
    ],
    "standards": [
        "Proverbs are standard pan-Arab usage.",
    ],
    "citations": [CIT_HOLES, CIT_BADAWI],
    "sig_lens": (
        "The Signature read: proverbs are the sworn wisdom - the "
        "elders speaking through your mouth. The Signature Language "
        "Method treats each proverb as a medal: earned by understanding "
        "the image, worn by using it once at exactly the right moment. "
        "Twenty medals; wear them one at a time."
    ),
    "drill": {"items": IDIOMS, "count": 20},
    "must_contain": ["الوقتُ كالسيفِ", "قطرةً قطرةً تمتلئُ الجرّةُ", "على قدِّ لحافِكَ مُدَّ رجليكَ", "حرفياً"],
})

# ---------------------------------------------------------------- record 29: formal & polite registers

REGISTERS = [
    ("أودُّ أن أستفسرَ عن موعدِ المقابلةِ", "I would like to inquire about the interview appointment", "أبغى أعرفْ متى المقابلةْ", "I wanna know when the interview is"),
    ("هل يمكنُكَ التفضّلُ بمساعدتي؟", "Could you kindly help me", "ممكن تساعدْني؟", "Can you help me"),
    ("أرجو قبولَ خالصِ اعتذاري", "I beg you to accept my sincere apology", "آسفْ واللهْ", "Sorry, I swear"),
    ("يسرُّني أن أدعوَكَ إلى الحفلِ", "I am pleased to invite you to the ceremony", "تعالَ الحفلةْ", "Come to the party"),
    ("نرجو من حضرتِكَ التكرّمَ بالحضورِ", "We request your honored self to grace us with attendance", "تشرّفْنا بحضورَكْ", "Honor us with your presence"),
    ("أشكرُكَ جزيلَ الشكرِ على جهودِكَ", "I thank you profusely for your efforts", "شكراً كثيرْ على تعبَكْ", "Thanks a lot for your effort"),
    ("برجاءِ إرسالِ التقريرِ في أقربِ وقتٍ", "Please send the report at the earliest", "ابعتْ التقريرْ بسرعةْ", "Send the report quickly"),
    ("أطيبُ التحياتِ وأصدقُ الأمنياتِ", "Kindest regards and sincerest wishes", "مع السلامةْ", "Bye"),
    ("سأكونُ ممتنّاً لو تفضّلتَ بالردِّ", "I would be grateful if you would reply", "ردْ عليّ لو سمحتْ", "Reply to me please"),
    ("يُرجى الالتزامُ بالمواعيدِ المحددةِ", "Kindly adhere to the scheduled times", "التزمْ بالمواعيدْ", "Stick to the schedule"),
    ("حضرتُكَ ضيفٌ عزيزٌ علينا", "Your honored self is a dear guest to us", "إنتَ ضيفْ عزيزْ", "You are a dear guest"),
    ("تشرّفْنا بلقائِكَ", "We were honored to meet you", "انبسطْنا بشوفتَكْ", "We were happy to see you"),
    ("لا مانعَ لديَّ إطلاقاً", "I have no objection whatsoever", "ما عندي مانعْ", "I do not mind"),
    ("بكلِّ سرورٍ وامتنانٍ", "With all pleasure and gratitude", "على عيني وراسي", "With pleasure (on my eye and head)"),
    ("دمتَ في رعايةِ اللهِ وحفظِهِ", "Remain in Gods care and protection", "اللهْ يحفظَكْ", "God protect you"),
]

ENTRIES.append({
    "key": "registers",
    "name": "Arabic Formal and Polite Registers",
    "group": "Conversation and Registers",
    "ladder_rank": 10,
    "ladder_tier": "advanced",
    "description": (
        "Fifteen formal-vs-informal pairs for letters, business, and "
        "elders - each with English translation. Formal MSA (الفصحى) "
        "elevates with full case endings, حضرتُكَ (your honored self), "
        "and verbs like أودُّ، أرجو، يُرجى. Informal speech shortens "
        "everything and drops the endings.\n" +
        "\n".join("  رسمي: %s — %s.\n  عامي: %s — %s." % (f, fe, i, ie)
                  for f, fe, i, ie in REGISTERS) + "\n"
        "Rule: write formal, speak warm. Letters, applications, and "
        "addresses to elders use the رسمي column; friends and family "
        "get the عامي column. Mixing them - formal words to a close "
        "friend - sounds stiff; informal words to a minister sounds "
        "rude."
    ),
    "how_it_works": (
        "Register is grammar wearing a suit. Formal MSA restores the "
        "case endings speech drops (-un, -an, -in), chooses weighty "
        "verbs (أودُّ، أرجو، يُرجى، نرجو), and addresses the person as "
        "حضرتُكَ (your honored self) instead of أنتَ. Informal speech "
        "clips endings, shortens verbs (أبغى، ابعتْ), and warms with "
        "dialect flavor. The pairs above are the same message in two "
        "uniforms - learn to change uniform without changing meaning."
    ),
    "key_points": [
        "15 formal/informal pairs with English translations.",
        "Formal markers: case endings، حضرتُكَ، أودُّ/أرجو/يُرجى.",
        "Informal markers: clipped endings, short verbs, dialect warmth.",
        "رسمي for letters, business, elders; عامي for friends, family.",
        "Wrong register = social error, not grammar error.",
        "Master both columns for the same message.",
    ],
    "requirements": [
        "Write a formal request letter using 5 رسمي phrases.",
        "Convert it to an informal message to a friend.",
        "Address an elder role-play partner with حضرتُكَ throughout.",
    ],
    "standards": [
        "Formal forms are standard written MSA; informal forms are pan-Arab colloquial.",
    ],
    "citations": [CIT_HOLES, CIT_RYDING],
    "sig_lens": (
        "The Signature read: register is the uniform of speech - parade "
        "dress for the letter, field dress for the friend. The "
        "Signature Language Method drills the change of uniform until "
        "it is instant: same message, two bearings. A speaker who "
        "commands both registers commands every room."
    ),
    "drill": {"pairs": REGISTERS, "count": 15},
    "must_contain": ["حضرتُكَ ضيفٌ عزيزٌ علينا", "على عيني وراسي", "رسمي:", "عامي:"],
})

# ---------------------------------------------------------------- record 30: complex sentences

COMPLEX = [
    ("ذهبتُ إلى السوقِ لأنني أحتاجُ إلى خضارٍ طازجةٍ", "dhahabtu ilā s-sūqi liʾannanī aḥtāju ilā khuḍārin ṭāzajatin", "I went to the market because I need fresh vegetables", "لأنَّ (because)"),
    ("بينما كنتُ أقرأُ، اتصلَ بي صديقي", "baynamā kuntu aqraʾu, ittaṣala bī ṣadīqī", "While I was reading, my friend called me", "بينما (while)"),
    ("الكتابُ الذي اشتريتُهُ ممتعٌ جداً", "al-kitābu lladhī shtaraytuhu mumtiʿun jiddan", "The book that I bought is very enjoyable", "الذي (who/which m)"),
    ("المدينةُ التي وُلدتُ فيها جميلةٌ", "al-madīnatu llatī wulidtu fīhā jamīlatun", "The city in which I was born is beautiful", "التي (who/which f)"),
    ("عندما تصلُ، اتصلْ بي", "ʿindamā taṣilu, ittaṣil bī", "When you arrive, call me", "عندما (when)"),
    ("سأنتظرُكَ حتى تعودَ", "saʾantaẓiruka ḥattā taʿūda", "I will wait for you until you return", "حتى (until)"),
    ("رغمَ أنَّ الجوَّ كانَ حاراًّ، خرجْنا للنزهةِ", "raghma anna l-jawwa kāna ḥārran, kharajnā lin-nuzhati", "Although the weather was hot, we went out for a picnic", "رغم أنَّ (although)"),
    ("ادرسْ بجدٍّ لكي تنجحَ", "udrus bijiddin likay tanjaḥa", "Study hard so that you succeed", "لكي (so that)"),
    ("قبلَ أن تسافرَ، تأكّدْ من جوازِكَ", "qabla an tusāfira, taʾakkad min jawāzika", "Before you travel, check your passport", "قبل أن (before)"),
    ("بعدَ أن انتهى الاجتماعُ، عدتُ إلى مكتبي", "baʿda an intahā l-ijtimāʿu, ʿudtu ilā maktabī", "After the meeting ended, I returned to my office", "بعد أن (after)"),
    ("إذا درستَ بجدٍّ، ستنجحُ بتفوقٍ", "idhā darasta bijiddin, satanjaḥu bitafawwuqin", "If you study hard, you will succeed with excellence", "إذا (if)"),
    ("هو ذكيٌّ لكنَّهُ كسولٌ", "huwa dhakiyyun lākinnahu kasūlun", "He is smart but he is lazy", "لكنَّ (but)"),
    ("أحبُّ الشايَ والقهوةَ معاً", "uḥibbu sh-shāya wal-qahwata maʿan", "I love tea and coffee together", "وَ (and)"),
    ("المكانُ حيثُ التقينا أولَ مرةٍ", "al-makānu ḥaythu ltaqaynā awwala marratin", "The place where we first met", "حيثُ (where)"),
    ("كلما قرأتَ أكثرَ، تعلمتَ أكثرَ", "kullamā qaraʾta akthara, taʿallamta akthara", "The more you read, the more you learn", "كلما (the more... the more)"),
]

ENTRIES.append({
    "key": "complex",
    "name": "Arabic Compound and Complex Sentences",
    "group": "Conversation and Registers",
    "ladder_rank": 10,
    "ladder_tier": "advanced",
    "description": (
        "Fifteen long sentences with clauses, connectors, and relative "
        "clauses - each parsed with its connector named and translated.\n" +
        "\n".join("  %s (%s) — %s.\n    الرابط: %s." % (a, t, e, c)
                  for a, t, e, c in COMPLEX) + "\n"
        "The connector toolkit: وَ (and)، لكنَّ (but)، لأنَّ (because)، "
        "عندما (when)، بينما (while)، الذي/التي (who/which)، إذا (if)، "
        "حتى (until)، لكي (so that)، قبل أن (before)، بعد أن (after)، "
        "رغم أنَّ (although)، حيثُ (where)، كلما (the more)."
    ),
    "how_it_works": (
        "Complex sentences join two thoughts with a connector word that "
        "names the relationship: cause (لأنَّ)، time (عندما، بينما، قبل "
        "أن، بعد أن، حتى)، contrast (لكنَّ، رغم أنَّ)، purpose (لكي)، "
        "condition (إذا)، place (حيثُ). Relative clauses use الذي "
        "(masculine) / التي (feminine) / الذين (plural): الكتابُ الذي "
        "اشتريتُهُ - the book which I bought it (Arabic keeps the "
        "resumptive pronoun ـهُ where English drops it). أنَّ "
        "introduces noun clauses: رغمَ أنَّ الجوَّ كانَ حاراًّ. One "
        "connector per join, and the long sentence holds."
    ),
    "key_points": [
        "15 complex sentences, each parsed with its connector named.",
        "Connector toolkit: 14 connectors above with translations.",
        "Relative pronouns: الذي/التي/الذين + resumptive pronoun.",
        "أنَّ introduces noun clauses (رغمَ أنَّ...).",
        "Time connectors: عندما، بينما، قبل أن، بعد أن، حتى.",
        "Purpose and condition: لكي، إذا، كلما.",
    ],
    "requirements": [
        "Join 10 pairs of simple sentences with a fitting connector.",
        "Write 5 relative-clause sentences about people you know.",
        "Parse each of the 15 sentences: main clause + subordinate + connector.",
    ],
    "standards": [
        "Clause structure per Badawi-Carter-Gully 2004; Ryding 2005.",
    ],
    "citations": [CIT_BADAWI, CIT_RYDING],
    "sig_lens": (
        "The Signature read: the complex sentence is the allied "
        "formation - two thoughts marching under one banner, bound by "
        "the connector-oath. لأنَّ swears cause, لكنَّ swears contrast, "
        "الذي binds the description to its noun. The Signature Language "
        "Method never lets a clause desert: every subordinate has its "
        "commander, every join its named bond."
    ),
    "drill": {"items": COMPLEX, "count": 15},
    "must_contain": ["الذي اشتريتُهُ", "رغمَ أنَّ الجوَّ كانَ حاراًّ", "كلما قرأتَ أكثرَ", "الرابط:"],
})


# ---------------------------------------------------------------- records 31-33: conversations

DIALOG_MARKET = [
    ("البائع", "أهلاً وسهلاً! تفضّلْ، ماذا تريدُ؟", "ahlan wa sahlan! tafaḍḍal, mādhā turīd؟", "Welcome! Please, what do you want", "Opening: the universal welcome + تفضّلْ"),
    ("المشتري", "أريدُ كيلوَ تفاحٍ، لو سمحتَ", "urīdu kīlū tuffāḥin, law samaḥta", "I want a kilo of apples, please", "Request softened with لو سمحتَ"),
    ("البائع", "التفاحُ طازجٌ اليومَ، بعشرةِ ريالاتٍ للكيلو", "at-tuffāḥu ṭāzajun al-yawma, biʿasharati riyālātin lil-kīlū", "The apples are fresh today, ten riyals per kilo", "Quality claim + price"),
    ("المشتري", "غالٍ جداً! أعطني سعرَكَ الأخيرَ", "ghālin jiddan! aʿṭinī siʿraka l-akhīra", "Too expensive! Give me your final price", "Bargaining opens"),
    ("البائع", "لخاطرِكَ، ثمانيةُ ريالاتٍ", "likhāṭirika, thamāniyatu riyālātin", "For your sake, eight riyals", "لخاطرِكَ = for your sake (flattery discount)"),
    ("المشتري", "اتفقْنا. وأريدُ أيضاً نصفَ كيلو عنبٍ", "ittafaqnā. wa urīdu ayḍan niṣfa kīlū ʿinabin", "Deal. I also want half a kilo of grapes", "اتفقْنا seals the bargain"),
    ("البائع", "العنبُ حلوٌ كالعسلِ، تذوّقْ", "al-ʿinabu ḥulwun kal-ʿasali, tadhawwaq", "The grapes are sweet as honey, taste", "Free sample = salesmanship"),
    ("المشتري", "ممم، لذيذٌ فعلاً. كم سعرُ العنبِ؟", "mm, ladhīdhun fiʿlan. kam siʿru l-ʿinabi؟", "Mmm, truly delicious. How much are the grapes", "Taste approved, price asked"),
    ("البائع", "اثنا عشرَ ريالاً للكيلو", "ithnā ʿashara riyālan lil-kīlū", "Twelve riyals per kilo", "Firm price after the taste"),
    ("المشتري", "أعطني نصفَ كيلو فقط", "aʿṭinī niṣfa kīlū faqaṭ", "Give me just half a kilo", "فقط limits the quantity"),
    ("البائع", "حاضر! شيءٌ آخرُ؟", "ḥāḍir! shayʾun ākharu؟", "Right away! Anything else", "Upsell attempt"),
    ("المشتري", "نعم، كيلوَ طماطمَ للسلطةِ", "naʿam, kīlū ṭamāṭima liṣ-ṣalaṭati", "Yes, a kilo of tomatoes for the salad", "Purpose stated: للسلطةِ"),
    ("البائع", "الطماطمُ بخمسةِ ريالاتٍ", "aṭ-ṭamāṭimu bikhamsati riyālātin", "Tomatoes are five riyals", "Quick price"),
    ("المشتري", "المجموعُ كم؟", "al-majmūʿu kam؟", "What is the total", "المجموعُ = the total"),
    ("البائع", "ثمانيةٌ وستةٌ وخمسةٌ، تسعةَ عشرَ ريالاً", "thamāniyatun wa sittatun wa khamsatun, tisʿata ʿashara riyālan", "Eight and six and five: nineteen riyals", "Mental arithmetic aloud"),
    ("المشتري", "تفضّلْ، عشرونَ ريالاً", "tafaḍḍal, ʿishrūna riyālan", "Here you are, twenty riyals", "تفضّلْ = here you are"),
    ("البائع", "والباقي ريالٌ واحدٌ. شكراً لكَ!", "wal-bāqī riyālun wāḥidun. shukran laka!", "And one riyal change. Thank you!", "الباقي = the change"),
    ("المشتري", "عفواً. الفواكهُ طازجةٌ عندَكَ", "ʿafwan. al-fawākihu ṭāzajatun ʿindaka", "You are welcome. Your fruit is fresh", "Compliment = loyalty"),
    ("البائع", "أهلاً بكَ دائماً! مع السلامةِ", "ahlan bika dāʾiman! maʿa s-salāmati", "Always welcome! Goodbye", "Return invitation"),
    ("المشتري", "مع السلامةِ، إلى اللقاءِ", "maʿa s-salāmati, ilā l-liqāʾi", "Goodbye, see you later", "Farewell pair"),
]
DIALOG_FRIEND = [
    ("سامي", "ليلى! ما هذه الصدفةُ السعيدةُ؟", "laylā! mā hādhihi ṣ-ṣudfatu s-saʿīdatu؟", "Layla! What a happy coincidence!", "Exclamation of surprise"),
    ("ليلى", "سامي! لم أرَكَ منذُ زمنٍ! كيف حالُكَ؟", "sāmī! lam araka mundhu zamanin! kayfa ḥāluka؟", "Sami! I have not seen you for ages! How are you?", "لم أرَكَ = I have not seen you"),
    ("سامي", "بخيرٍ، الحمدُ للهِ. وأنتِ؟", "bikhayrin, al-ḥamdu lillāhi. wa anti؟", "Fine, praise God. And you?", "Standard well-mannered reply"),
    ("ليلى", "بخيرٍ. ماذا تفعلُ هذه الأيامَ؟", "bikhayrin. mādhā tafʿalu hādhihi l-ayyāma؟", "Fine. What are you doing these days?", "Catching up"),
    ("سامي", "أعملُ مهندساً وأدرسُ الماجستيرَ مساءً", "aʿmalu muhandisan wa adrusu l-mājistīra masāʾan", "I work as an engineer and study for my masters in the evening", "Two verbs, one life"),
    ("ليلى", "ما شاءَ اللهُ! وأنا تخرّجتُ وأعملُ طبيبةً الآنَ", "mā shāʾa llāhu! wa anā takharrajtu wa aʿmalu ṭabībatan al-āna", "Wonderful! I graduated and now work as a doctor", "ما شاءَ اللهُ = admiration"),
    ("سامي", "مباركٌ! أين تعملينَ؟", "mubārakun! ayna taʿmalīna؟", "Congratulations! Where do you work?", "مباركٌ = congratulations"),
    ("ليلى", "في المستشفى المركزيِّ. العملُ متعبٌ لكن ممتعٌ", "fī l-mustashfā l-markaziyyi. al-ʿamalu mutʿibun lākin mumtiʿun", "At the central hospital. The work is tiring but enjoyable", "لكن pivots the description"),
    ("سامي", "هل تذكرينَ أيامَ الجامعةِ؟", "hal tadhkurīna ayyāma l-jāmiʿati؟", "Do you remember the university days?", "هل opens the memory"),
    ("ليلى", "بالطبعِ! أجملُ أيامِ حياتي", "biṭ-ṭabʿi! ajmalu ayyāmi ḥayātī", "Of course! The most beautiful days of my life", "Superlative of nostalgia"),
    ("سامي", "ما رأيُكِ أن نشربَ القهوةَ معاً؟", "mā raʾyuki an nashraba l-qahwata maʿan؟", "How about we have coffee together?", "ما رأيُكِ = what do you think"),
    ("ليلى", "فكرةٌ رائعةٌ! المقهى القريبُ هادئٌ", "fikratun rāʾiʿatun! al-maqhā l-qarību hādiʾun", "A great idea! The nearby café is quiet", "Agreement + suggestion"),
    ("سامي", "أخبريني عن عائلتِكِ", "akhbirīnī ʿan ʿāʾilatiki", "Tell me about your family", "Imperative of interest"),
    ("ليلى", "والدي تقاعدَ، وأمي بخيرٍ، وأخي تزوّجَ السنةَ الماضيةَ", "wālidī taqāʿada, wa ummī bikhayrin, wa akhī tazawwaja s-sanata l-māḍiyata", "My father retired, my mother is fine, and my brother married last year", "Three family news in one breath"),
    ("سامي", "باركَ اللهُ لهُ! وعائلتي بخيرٍ أيضاً", "bāraka llāhu lahu! wa ʿāʾilatī bikhayrin ayḍan", "God bless him! My family is fine too", "Blessing + reciprocation"),
    ("ليلى", "يجبُ أن نلتقيَ أكثرَ", "yajibu an naltaqiya akthara", "We must meet more often", "يجبُ أن = must"),
    ("سامي", "اتفقْنا. ما رقمُ هاتفِكِ الجديدُ؟", "ittafaqnā. mā raqmu hātifiki l-jadīdu؟", "Agreed. What is your new phone number?", "اتفقْنا = agreed"),
    ("ليلى", "سأرسلُهُ لكَ في رسالةٍ", "saʾursiluhu laka fī risālatin", "I will send it to you in a message", "Future promise"),
    ("سامي", "ممتازٌ. سعدتُ جداً برؤيتِكِ", "mumtāzun. saʿidtu jiddan biruʾyatiki", "Excellent. I was very happy to see you", "Warm close"),
    ("ليلى", "وأنا أيضاً. إلى اللقاءِ قريباً!", "wa anā ayḍan. ilā l-liqāʾi qarīban!", "Me too. See you soon!", "إلى اللقاءِ قريباً = see you soon"),
]
DIALOG_PROBLEM = [
    ("المدير", "تفضّلْ بالجلوسِ. نحتاجُ أن نتحدثَ عن المشروعِ", "tafaḍḍal bil-julūsi. naḥtāju an nataḥaddatha ʿani l-mashrūʿi", "Please sit down. We need to talk about the project", "Formal opening, problem framed"),
    ("الموظف", "نعم يا سيدي. أعرفُ أن التسليمَ تأخّرَ", "naʿam yā sayyidī. aʿrifu anna t-taslīma taʾakhkhara", "Yes sir. I know the delivery is delayed", "Honest acknowledgment"),
    ("المدير", "ما سببُ التأخيرِ؟", "mā sababu t-taʾkhīri؟", "What is the cause of the delay?", "Direct ما question"),
    ("الموظف", "واجهْنا مشكلةً تقنيةً في النظامِ الجديدِ", "wājahnā mushkilatan tiqniyyatan fī n-niẓāmi l-jadīdi", "We faced a technical problem in the new system", "Problem named precisely"),
    ("المدير", "لماذا لم تُبلغْني مبكراً؟", "limādhā lam tublighnī mubakkiran؟", "Why did you not inform me earlier?", "لماذا + negative past"),
    ("الموظف", "حاولْنا حلَّها بأنفسِنا أولاً، لكنها أكبرُ منا", "ḥāwalnā ḥallahā biʾanfusinā awwalan, lākinnahā akbaru minnā", "We tried to solve it ourselves first, but it is bigger than us", "لكنَّ pivots to honesty"),
    ("المدير", "حسناً. ما الحلُّ المقترحُ؟", "ḥasanan. mā l-ḥallu l-muqtaraḥu؟", "Well. What is the proposed solution?", "حسناً moves past blame"),
    ("الموظف", "نحتاجُ إلى خبيرٍ خارجيٍّ لمدةِ أسبوعٍ", "naḥtāju ilā khabīrin khārijiyyin limuddati usbūʿin", "We need an external expert for a week", "Solution proposed"),
    ("المدير", "كم سيكلّفُ ذلكَ؟", "kam sayukallifu dhālika؟", "How much will that cost?", "Cost question"),
    ("الموظف", "حوالي خمسةِ آلافِ ريالٍ", "ḥawālā khamsati ālāfi riyālin", "About five thousand riyals", "حوالي = about"),
    ("المدير", "هذا مبلغٌ كبيرٌ. هل يوجدُ حلٌّ أرخصُ؟", "hādhā mablaghun kabīrun. hal yūjadu ḥallun arkhaṣu؟", "That is a large amount. Is there a cheaper solution?", "Pushback with هل"),
    ("الموظف", "يمكنُ أن نستعيرَ خبيراً من فرعِ جدةَ", "yumkinu an nastaʿīra khabīran min farʿi juddata", "We can borrow an expert from the Jeddah branch", "Cheaper alternative"),
    ("المدير", "فكرةٌ جيدةٌ. كم سيستغرقُ؟", "fikratun jayyidatun. kam sayastaghriqu؟", "A good idea. How long will it take?", "Approval + time check"),
    ("الموظف", "ثلاثةُ أيامٍ على الأكثرِ", "thalāthatu ayyāmin ʿalā l-akthari", "Three days at most", "على الأكثرِ = at most"),
    ("المدير", "اتفقْنا. اتصلْ بهم اليومَ", "ittafaqnā. ittaṣil bihim al-yawma", "Agreed. Call them today", "Decision + action"),
    ("الموظف", "حاضرٌ يا سيدي. سأرسلُ لكَ تقريراً يومياً", "ḥāḍirun yā sayyidī. saʾursilu laka taqrīran yawmiyyan", "At once, sir. I will send you a daily report", "حاضرٌ = at once (respect)"),
    ("المدير", "ممتازٌ. وأريدُ خطةً واضحةً غداً صباحاً", "mumtāzun. wa urīdu khiṭṭatan wāḍiḥatan ghadan ṣabāḥan", "Excellent. And I want a clear plan tomorrow morning", "Follow-up demand"),
    ("الموظف", "ستكونُ جاهزةً إن شاءَ اللهُ", "satakūnu jāhizatan in shāʾa llāhu", "It will be ready, God willing", "إن شاءَ اللهُ = commitment softener"),
    ("المدير", "أثقُ بكَ. لا تترددْ في طلبِ المساعدةِ", "athiqu bika. lā tataraddad fī ṭalabi l-musāʿadati", "I trust you. Do not hesitate to ask for help", "Trust + open door"),
    ("الموظف", "شكراً لثقتِكَ يا سيدي. مع السلامةِ", "shukran lithiqatika yā sayyidī. maʿa s-salāmati", "Thank you for your trust, sir. Goodbye", "Grateful close"),
]


def _dialog_entry(key, name, intro, lines, how, points, sig):
    return {
        "key": key, "name": name, "group": "Conversation and Registers",
        "ladder_rank": 10, "ladder_tier": "advanced",
        "description": intro + "\n" +
            "\n".join("  %s: %s (%s) — %s. [%s]" % (sp, a, t, e, n)
                      for sp, a, t, e, n in lines),
        "how_it_works": how,
        "key_points": points,
        "requirements": [
            "Act out the dialogue with a partner, swapping roles.",
            "Cover one column and reconstruct it from the other two.",
            "Write a 10-line continuation of the conversation.",
        ],
        "standards": [
            "Dialogue language is natural standard MSA with polite forms.",
        ],
        "citations": [CIT_HOLES, CIT_BADAWI],
        "sig_lens": sig,
        "drill": {"lines": lines, "count": 20},
        "must_contain": [l[1] for l in lines],
    }


ENTRIES.append(_dialog_entry(
    "market", "Arabic Conversation: At the Market",
    "A 20-line bilingual market dialogue (Arabic + transliteration + "
    "English), annotated line by line. The souk negotiation in full: "
    "greeting, request, price, bargain, taste, total, change, farewell.",
    DIALOG_MARKET,
    "The market dialogue runs the full transaction arc: welcome "
    "(أهلاً وسهلاً) → request (أريدُ... لو سمحتَ) → price (بعشرةِ "
    "ريالاتٍ) → objection (غالٍ جداً!) → counter (لخاطرِكَ...) → deal "
    "(اتفقْنا) → extras (شيءٌ آخرُ؟) → total (المجموعُ كم؟) → payment "
    "(تفضّلْ) → change (والباقي) → farewell (مع السلامةِ). Each line "
    "is annotated with the move it makes - learn the moves, not just "
    "the words.",
    [
        "20-line bilingual dialogue, annotated per line.",
        "Full transaction arc: welcome → bargain → pay → farewell.",
        "Bargaining moves: غالٍ جداً، لخاطرِكَ، اتفقْنا.",
        "Numbers in action: prices, totals, change.",
        "Politeness under pressure: لو سمحتَ throughout.",
    ],
    "The Signature read: the market dialogue is the negotiation "
    "drill - twenty moves, no wasted words. The Signature Language "
    "Method spars in the souk: ask, object, counter, close. The "
    "bargain sealed with اتفقْنا is a treaty signed; the change "
    "counted aloud is honor kept.",
))
ENTRIES.append(_dialog_entry(
    "friend", "Arabic Conversation: Meeting a Friend",
    "A 20-line bilingual dialogue between Sami and Layla, annotated. "
    "The reunion arc: surprise, catching up, news exchanged, coffee "
    "proposed, family updates, and the promise to meet again.",
    DIALOG_FRIEND,
    "Reunion dialogues run on reciprocity: surprise (ما هذه الصدفةُ!) "
    "→ health check (كيف حالُكَ؟) → life update (ماذا تفعلُ؟) → "
    "admiration (ما شاءَ اللهُ، مباركٌ) → shared memory (هل تذكرينَ؟) "
    "→ invitation (ما رأيُكِ أن...؟) → family news → future promise "
    "(يجبُ أن نلتقيَ أكثرَ). Gendered address runs throughout: "
    "حالُكَ/حالُكِ، تذكرينَ - the dialogue is a gender-agreement "
    "workout disguised as friendship.",
    [
        "20-line bilingual dialogue, annotated per line.",
        "Reunion arc: surprise → updates → invitation → promise.",
        "Admiration formulas: ما شاءَ اللهُ، مباركٌ.",
        "Gendered address throughout (كَ/كِ، تذكرينَ).",
        "Invitation mold: ما رأيُكِ أن نشربَ القهوةَ؟",
    ],
    "The Signature read: the reunion is the alliance renewed - two "
    "old comrades reporting from their separate campaigns. The "
    "Signature Language Method treats friendship dialogue as the "
    "debrief: news exchanged, honors given (مباركٌ), the next meeting "
    "sworn (يجبُ أن نلتقيَ أكثرَ). No ally left uncontacted.",
))
ENTRIES.append(_dialog_entry(
    "problem", "Arabic Conversation: Solving a Problem",
    "A 20-line bilingual dialogue between a manager and an employee, "
    "annotated. The problem-solving arc: problem named, cause probed, "
    "blame set aside, solutions proposed, costs weighed, decision "
    "made, follow-up sworn.",
    DIALOG_PROBLEM,
    "Workplace problem-solving follows a strict arc: frame (نحتاجُ أن "
    "نتحدثَ) → acknowledge (أعرفُ أن...) → probe (ما سببُ؟، لماذا؟) → "
    "propose (نحتاجُ إلى...) → cost (كم سيكلّفُ؟) → cheaper alternative "
    "→ decide (اتفقْنا) → assign (اتصلْ بهم اليومَ) → follow up (تقريراً "
    "يومياً) → trust (أثقُ بكَ). Formal address (يا سيدي، حضرتُكَ-style "
    "respect) holds throughout - problems are solved up the chain, "
    "never around it.",
    [
        "20-line bilingual dialogue, annotated per line.",
        "Problem-solving arc: frame → probe → propose → decide → follow up.",
        "Cost negotiation: كم سيكلّفُ؟ → cheaper alternative.",
        "Formal workplace address: يا سيدي throughout.",
        "Trust close: أثقُ بكَ - the problem solved as alliance.",
    ],
    "The Signature read: the problem meeting is the war council - "
    "the fault named without flinching, the blame set aside, the "
    "solutions weighed like supplies. The Signature Language Method "
    "runs the council in order: probe, propose, price, decide, "
    "follow up. أثقُ بكَ is the commander entrusting the mission; "
    "the daily report is the oath of accountability.",
))

# ---------------------------------------------------------------- record 34: mastery review

WORDS200 = (
    [(a, t, e) for a, t, e, _, _, _ in NOUNS] +
    [(a, t, e) for a, t, e, _, _, _ in VERBS] +
    [(a, t, e, ) for a, t, e, _, _, _, _ in ADJECTIVES] +
    [(a, t, e) for a, t, e, _, _, _ in ADVERBS] +
    [(a, t, e) for a, t, e in PRON_PERSONAL] +
    [(a, t, e) for a, t, e in PRON_POSSESSIVE] +
    [(a, t, e) for a, t, e, _, _, _ in PRON_DEMONST] +
    [(a, t, e) for a, t, e, _, _, _ in PRON_INTERROG] +
    [(a, t, e) for a, t, e in NUM_1_10] +
    [(a, t, e) for a, t, e in NUM_DAYS] +
    [(a, t, e) for a, t, e in NUM_MONTHS] +
    [(a, t, e) for a, t, e in NUM_SEASONS] +
    [("أحمر", "aḥmar", "red"), ("أخضر", "akhḍar", "green"),
     ("أزرق", "azraq", "blue"), ("أصفر", "aṣfar", "yellow"),
     ("أسود", "aswad", "black"), ("أبيض", "abyaḍ", "white"),
     ("بني", "bunnī", "brown"), ("رمادي", "ramādī", "gray")] +
    [("أب", "ab", "father"), ("أم", "umm", "mother"),
     ("أخ", "akh", "brother"), ("أخت", "ukht", "sister"),
     ("ابن", "ibn", "son"), ("ابنة", "ibna", "daughter"),
     ("زوج", "zawj", "husband"), ("زوجة", "zawja", "wife")] +
    [("رأس", "raʾs", "head"), ("عين", "ʿayn", "eye"),
     ("أذن", "udhUn".replace("U", "u"), "ear"), ("أنف", "anf", "nose"),
     ("فم", "fam", "mouth"), ("يد", "yad", "hand"),
     ("رجل", "rijl", "leg"), ("قلب", "qalb", "heart"),
     ("شعر", "shaʿr", "hair"), ("سن", "sinn", "tooth")] +
    [("أرز", "urz", "rice"), ("دجاج", "dajāj", "chicken"),
     ("سمك", "samak", "fish"), ("بيض", "bayḍ", "eggs"),
     ("حليب", "ḥalīb", "milk"), ("جبن", "jubn", "cheese"),
     ("عسل", "ʿasal", "honey"), ("تمر", "tamr", "dates"),
     ("زيت", "zayt", "oil"), ("سكر", "sukkar", "sugar")] +
    [("نعم", "naʿam", "yes"), ("لا", "lā", "no"),
     ("شكراً", "shukran", "thanks"), ("من فضلك", "min faḍlika", "please"),
     ("عفواً", "ʿafwan", "excuse me"), ("آسف", "āsif", "sorry"),
     ("مرحباً", "marḥaban", "hello")]
)
assert len(WORDS200) == 200, "WORDS200 must be 200, got %d" % len(WORDS200)

MASTERY_GRAMMAR = [
    "Word order: VSO default (كتبَ الطالبُ الدرسَ); SVO for emphasis.",
    "Gender: masculine/feminine; ة marks most feminines; everything agrees.",
    "Number: singular, dual (-انِ), plural (sound ون/ين/ات or broken).",
    "ال = the; sun letters assimilate (الشمس = ash-shams).",
    "Cases in formal MSA: -ُ nominative, -َ accusative, -ِ genitive.",
    "Negation by tense: لا (present)، لم (past)، لن (future).",
    "Questions: هل (yes-no) or fronted interrogative (من ما أين متى لماذا كيف كم).",
    "Idafa: possessed + possessor (كتابُ الطالبِ = the students book).",
    "Adjectives follow and agree; non-human plurals take feminine singular.",
    "Past = suffixes (كتبتُ); present = prefixes (أكتبُ); future = سـ/سوف + present.",
]

ENTRIES.append({
    "key": "mastery",
    "name": "Arabic Mastery Review and Full Reference",
    "group": "Mastery Reference",
    "ladder_rank": 10,
    "ladder_tier": "advanced",
    "description": (
        "The whole database in one teaching summary: the alphabet, 200 "
        "core words, the ten grammar rules, and the essential phrase "
        "tables. Print this record and the database travels with you.\n"
        "Alphabet (28 letters):\n" + _alpha_lines() + "\n"
        "200 core words (Arabic — transliteration — English):\n" +
        "\n".join("  %d. %s (%s) — %s." % (i + 1, a, t, e)
                  for i, (a, t, e) in enumerate(WORDS200)) + "\n"
        "Ten grammar rules:\n" +
        "\n".join("  %d. %s" % (i + 1, r) for i, r in enumerate(MASTERY_GRAMMAR)) + "\n"
        "Core phrase tables: greetings (السلام عليكم/وعليكم السلام، صباح "
        "الخير/صباح النور، مساء الخير/مساء النور، مع السلامة، إلى "
        "اللقاء)؛ politeness (شكراً/عفواً، من فضلك، لو سمحت، تفضّل)؛ "
        "survival (أين...؟، كم...؟، هل تتكلمُ الإنجليزيةَ؟، أريدُ...، "
        "الفاتورةُ لو سمحتَ)؛ time (اليوم، غداً، أمسِ، صباحاً، مساءً)."
    ),
    "how_it_works": (
        "Mastery is the ladder folded into one page. Work it in loops: "
        "loop one, read the alphabet aloud and write each letter from "
        "memory; loop two, cover the English of the 200 words and "
        "produce the Arabic; loop three, recite the ten grammar rules "
        "and give one example each from the earlier records; loop four, "
        "run the phrase tables as call-and-response. When a loop is "
        "clean three days running, the database is yours."
    ),
    "key_points": [
        "Full alphabet table: 28 letters with transliteration.",
        "200 core words numbered, each with transliteration and English.",
        "Ten grammar rules in compressed reference form.",
        "Four phrase tables: greetings, politeness, survival, time.",
        "Four-loop study method: alphabet → words → rules → phrases.",
        "This record plus records 1-33 = the complete ladder.",
    ],
    "requirements": [
        "Score 100% on the 200-word drill three days running.",
        "Recite the 10 rules with one example each from memory.",
        "Hold a 5-minute conversation using only this records material.",
    ],
    "standards": [
        "Reference compiled from records 1-33 of this database.",
        "Transliteration follows ISO 233:1984.",
    ],
    "citations": [CIT_WRIGHT, CIT_RYDING, CIT_WEHR, CIT_ISO233],
    "sig_lens": (
        "The Signature read: the mastery review is the final muster - "
        "every letter, every word, every rule standing in formation for "
        "inspection. The Signature Language Method musters in four "
        "loops, and no soldier is dismissed until clean three days "
        "running. 28 letters, 200 words, 10 rules, 4 tables: the whole "
        "covenant on one page, ready to march."
    ),
    "drill": {"words200": WORDS200, "count": 200,
              "alphabet": 28, "grammar_rules": MASTERY_GRAMMAR},
    "must_contain": ["200 core words", "Ten grammar rules", "Core phrase tables", "أربعون"] if False else ["200 core words", "Ten grammar rules", "Core phrase tables", "رمادي", "الفاتورةُ لو سمحتَ"],
})
