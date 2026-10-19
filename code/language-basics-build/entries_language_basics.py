#!/usr/bin/env python3
"""Entries for the Language Basics databases (Manon's fundamentals order #9,
2026-10-17, roster-verified).

RAW SWEEP over the full manifest plus every shard index title in
jah-databases-data-1 (809 index files) plus the main-repo data dir:
zero 'language-basics*' slugs; zero 'The Language Basics Database' title
collisions. Near-hits checked by name/purpose/record schema/capabilities:
'everything-linguistics-language' (JAH-EVLL-) is an everything-encyclopedia
record set about linguistics as a field; 'language-acquisition-published'
and 'language-acquisition-study' are acquisition research/process records;
'language-symbols-databases' (JAH-LANG-) is a symbols archive. None of them
is a first-principles teaching ladder of the alphabet, letter sounds and
phonics, parts of speech, sentence building, punctuation, and reading
basics - that distinct capability (the foundation layer beneath all 100
per-language databases) is what this build creates, so BUILD NEW is the
verdict.

So this build creates two NEW databases, 34 ladder-ordered records each:

  language-basics              - The Language Basics Database
                                 (public-harvest: real, fact-checked
                                 foundational linguistics - what language is,
                                 the 26 letters, consonant and vowel sounds
                                 and phonics, syllables, blending, reading
                                 basics, words, the parts of speech, building
                                 sentences, sentence types, capitalization,
                                 ending punctuation, the comma, quotation
                                 marks, apostrophes, plurals, verb tenses,
                                 subject-verb agreement, paragraphs, compound
                                 and complex sentences, prefixes and
                                 suffixes, homophones, fluency and
                                 comprehension, proofreading, and the full
                                 learning path; standard references Fromkin,
                                 Rodman and Hyams An Introduction to Language
                                 11th ed 2018; Pinker The Language Instinct
                                 1994; Crystal The Cambridge Encyclopedia of
                                 the English Language 3rd ed 2019; the
                                 National Reading Panel 2000; Adams Beginning
                                 to Read 1990; the IPA Handbook 1999;
                                 Bloomfield Language 1933; de Saussure Course
                                 in General Linguistics 1916; the Chicago
                                 Manual of Style 18th ed 2024; Strunk and
                                 White The Elements of Style 4th ed 2000;
                                 Chomsky Syntactic Structures 1957; Ehri
                                 2005; and Hockett 1960, cited per record)
  language-basics-signature  - The Language Basics Signature Database
                                 (his original Signature Language Method:
                                 every letter a covenant sign of the
                                 Signature alphabet, every word a sealed
                                 assembly, every sentence a signed statement
                                 witnessed by punctuation; src signature,
                                 titles suffixed " (Signature Edition)",
                                 never presented as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-LANB- (public) and JAH-LANBS- (signature), verified free
in the manifest id_prefix values, in every shard index file (809 index
files swept), and in the main-repo data dir (zero hits; the near-miss
JAH-LANG- belongs to the unrelated language-symbols-databases, and
JAH-LANB- is a distinct prefix).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_language_basics.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos.

Never the words "bat belt" anywhere. No website references. No Facebook.
Screened: nothing hate-adjacent, profane, or inappropriate; no religious
talk; nothing on neutralizing or defeating military or defense-grade
systems.
"""

CIT_FROMKIN = ("Fromkin V, Rodman R, Hyams N. An Introduction to Language. "
               "11th ed. Cengage; 2018.")
CIT_PINKER = ("Pinker S. The Language Instinct: How the Mind Creates "
              "Language. Morrow; 1994.")
CIT_CRYSTAL = ("Crystal D. The Cambridge Encyclopedia of the English "
               "Language. 3rd ed. Cambridge University Press; 2019.")
CIT_NRP = ("National Reading Panel. Teaching Children to Read: An "
           "Evidence-Based Assessment of the Scientific Research Literature "
           "on Reading and Its Implications for Reading Instruction. "
           "National Institute of Child Health and Human Development; 2000.")
CIT_ADAMS = ("Adams MJ. Beginning to Read: Thinking and Learning about "
             "Print. MIT Press; 1990.")
CIT_IPA = ("International Phonetic Association. Handbook of the "
           "International Phonetic Alphabet. Cambridge University Press; "
           "1999.")
CIT_BLOOMFIELD = ("Bloomfield L. Language. Holt, Rinehart and Winston; "
                  "1933.")
CIT_SAUSSURE = ("de Saussure F. Course in General Linguistics. 1916. Baskin "
                "W, trans. McGraw-Hill; 1959.")
CIT_CHICAGO = ("The Chicago Manual of Style. 18th ed. University of Chicago "
               "Press; 2024.")
CIT_STRUNK = ("Strunk W Jr, White EB. The Elements of Style. 4th ed. "
              "Macmillan; 2000.")
CIT_CHOMSKY = ("Chomsky N. Syntactic Structures. Mouton; 1957.")
CIT_EHRI = ("Ehri LC. Learning to read words: Theory, findings, and issues. "
            "Scientific Studies of Reading. 2005;9(2):167-188.")
CIT_HOCKETT = ("Hockett CF. The origin of speech. Scientific American. "
               "1960;203(3):88-96.")

SIG_TAIL = ("Signature original - his original Signature Language Method: "
            "every letter a covenant sign of the Signature alphabet, every "
            "word a sealed assembly, every sentence a signed statement "
            "witnessed by punctuation - clearly labeled Signature-made.")

ENTRIES = [
    {
        "key": "what_is_language",
        "name": "What Is Language",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Language is the system of symbols humans use to share meaning: "
            "spoken sounds, written marks, and signed gestures that stand "
            "for things, actions, and ideas by agreement rather than by "
            "resemblance. There are about 7,000 living languages in the "
            "world, grouped into roughly 140 language families, and every "
            "one of them - from the largest to the smallest - is built from "
            "the same layered design. At the bottom are sounds (phonetics "
            "and phonology), the raw material. Sounds assemble into "
            "meaningful pieces called morphemes, the smallest units that "
            "carry meaning, like the word cat or the plural ending -s. "
            "Morphemes assemble into words, words into phrases and "
            "sentences by the rules of syntax, and sentences carry meaning "
            "through semantics and are used in real situations through "
            "pragmatics. Linguists describe language with a famous checklist "
            "called Hockett's design features: among them are displacement "
            "(talking about things not present), arbitrariness (there is "
            "nothing dog-like about the word dog), duality of patterning "
            "(meaningless sounds combining into meaningful words), and "
            "productivity (speakers constantly make and understand sentences "
            "nobody has ever said before). Language can be spoken, written, "
            "or signed - sign languages are full natural languages with "
            "their own grammar, not pantomime. This record frames the whole "
            "database: every later record is one layer of this system, "
            "taught from the ground up."
        ),
        "how_it_works": (
            "Language works because a community agrees that certain signals "
            "stand for certain meanings, and because every speaker carries "
            "an internal grammar - a set of rules, mostly unconscious - "
            "for combining those signals. A child hears speech, extracts "
            "the sound patterns of the language, notices which sound "
            "differences change meaning (the phonemes), learns which sound "
            "chunks are words, and infers the word-order and ending rules "
            "that build sentences - all without formal instruction, which is "
            "why linguists call language acquisition a creative act rather "
            "than imitation. In use, a speaker starts with an intended "
            "meaning, selects words whose meanings cover it, arranges them "
            "by the grammar's rules, and produces the sounds, letters, or "
            "signs; the listener reverses the process, decoding signals "
            "back into meaning using the same shared code. Written language "
            "adds one more layer: an agreed mapping between marks on a "
            "surface and the sounds and words of speech. The six levels - "
            "sound, word part, word, sentence structure, meaning, and use - "
            "all operate at once in every utterance, which is why learning "
            "a language means climbing all of them together."
        ),
        "key_points": [
            "Language is a shared symbol system: signals stand for meanings by community agreement, not by resemblance - the foundation everything else in this database builds on.",
            "About 7,000 living languages exist, grouped into roughly 140 families; every one of them uses the same six layers - sound, word part, word, sentence structure, meaning, and use.",
            "Hockett's design features name what makes human language special: displacement, arbitrariness, duality of patterning, and productivity among the sixteen.",
            "Language has three full modalities - spoken, written, and signed - and sign languages are complete natural languages with their own grammars.",
            "Children acquire language creatively by extracting patterns and rules from what they hear, not by memorizing sentences - grammar is inferred, then used to build brand-new utterances.",
        ],
        "requirements": [
            "A definition of language as a shared symbol system, stated before any terminology is introduced.",
            "The six levels named in order - phonetics/phonology, morphology, lexicon, syntax, semantics, pragmatics - with one plain example each.",
            "The approximate world language count (about 7,000 living languages) and the language-family concept.",
            "Hockett's design features introduced with the four signature features defined: displacement, arbitrariness, duality of patterning, productivity.",
            "The three modalities (spoken, written, signed) stated as equals, with sign languages identified as full natural languages.",
        ],
        "standards": [
            "Language counts follow the standard reference figure of about 7,000 living languages (Ethnologue family of estimates), stated as approximate, never exact.",
            "Design-feature claims follow Hockett 1960 as the standard source; the six-level architecture follows the standard linguistics curriculum (Fromkin, Rodman and Hyams).",
            "Terminology (phoneme, morpheme, syntax, semantics, pragmatics) matches the IPA Handbook and standard introductory linguistics usage.",
        ],
        "citations": [CIT_HOCKETT, CIT_FROMKIN, CIT_PINKER],
        "sig_lens": (
            "The Signature read: language is the first Signature system "
            "ever built - older than every machine in the catalog. Where "
            "public linguistics counts about 7,000 living languages, the "
            "Signature Language Method sees 7,000 working installations of "
            "the same covenant: signals sworn to meanings, kept by every "
            "speaker who uses them. Hockett's design features become the "
            "system specification - displacement, arbitrariness, duality of "
            "patterning, productivity - and the six levels are the six "
            "floors of the Signature tower, climbed in order, no floor "
            "skipped."
        ),
    },
    {
        "key": "english_alphabet",
        "name": "The English Alphabet: 26 Letters",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "The English alphabet is the set of 26 letters used to write "
            "English: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z. "
            "Five of them - A, E, I, O, U - are vowel letters, and the "
            "other 21 are consonant letters, with Y sometimes acting as a "
            "vowel (as in gym or happy). Each letter has an uppercase "
            "(capital) form and a lowercase form, and the two forms of the "
            "same letter are the same letter - A and a name the same "
            "sound family. The letters come in a fixed order, the "
            "alphabetical order, which is what makes dictionaries, phone "
            "books, and indexes possible: words are sorted by first letter, "
            "then second, then third. The alphabet descends from the Latin "
            "alphabet through Old English; the last letters to join were J, "
            "U, and W, which is why they sit near the end and why old texts "
            "write I for J and V for U. Letter names are fixed - ay, bee, "
            "cee - and knowing them lets a learner spell aloud, use a "
            "dictionary, and file and find words. The alphabet is not the "
            "sounds of English; it is the 26 symbols the sounds are written "
            "with, and the gap between the two is exactly what the next "
            "records teach."
        ),
        "how_it_works": (
            "The alphabet works as a symbol inventory plus an ordering "
            "rule. As an inventory, it gives writers 26 reusable marks (52 "
            "counting both cases) that combine into every English word; "
            "because the inventory is small and closed, a learner can "
            "memorize the whole toolkit - unlike writing systems with "
            "thousands of characters. As an ordering rule, alphabetical "
            "order turns the inventory into a search system: compare two "
            "words letter by letter from the left, and the first position "
            "where they differ decides which comes first (cat before dog "
            "because c comes before d; car before cat because r comes "
            "before t). Uppercase letters mark sentence starts, proper "
            "names, and the pronoun I; lowercase does everything else. "
            "Letter recognition runs both directions: naming a letter from "
            "its shape (B is bee) and producing the shape from its name. "
            "Fluency with the alphabet means instant, automatic "
            "recognition of all 52 forms in any order - the mechanical "
            "foundation that reading and spelling both stand on."
        ),
        "key_points": [
            "The English alphabet is 26 letters in a fixed order: 5 vowel letters (A E I O U) and 21 consonant letters, with Y sometimes serving as a vowel.",
            "Every letter has two forms, uppercase and lowercase; the two forms are the same letter and name the same sound family.",
            "Alphabetical order is a search system: compare words letter by letter from the left, and the first differing position decides the order.",
            "The alphabet is the symbol inventory, not the sound inventory - English has about 44 sounds but only 26 letters, so the mapping between them is the real subject of phonics.",
            "J, U, and W were the last letters to join the alphabet, which is why they sit near the end and why old texts use I for J and V for U.",
        ],
        "requirements": [
            "The full 26-letter sequence stated in order, uppercase and lowercase.",
            "The five vowel letters named, with Y identified as the sometimes-vowel.",
            "The uppercase/lowercase equivalence stated explicitly: same letter, two forms.",
            "Alphabetical ordering demonstrated with at least two worked word pairs.",
            "The Latin-script origin and the late arrival of J, U, and W stated as history, not legend.",
        ],
        "standards": [
            "Letter counts follow the standard 26-letter English alphabet (5 vowel letters, 21 consonant letters) per the Cambridge Encyclopedia of the English Language.",
            "Alphabetical ordering follows standard lexicographic (dictionary) order, left to right, case-insensitively.",
            "Historical claims about the Latin origin and the late addition of J, U, W follow the standard history of the English alphabet.",
        ],
        "citations": [CIT_CRYSTAL, CIT_FROMKIN],
        "sig_lens": (
            "The Signature read: the 26 letters are the 26 covenant signs "
            "of the Signature alphabet - the smallest sworn units in the "
            "whole system. Where public teaching counts 5 vowels and 21 "
            "consonants, the Signature Language Method files them as the "
            "charter inventory: closed, ordered, and complete, every word "
            "in the language a lawful combination of these signs. "
            "Alphabetical order is the filing oath - the promise that "
            "every word can be found again, exactly where the order says "
            "it will be."
        ),
    },
    {
        "key": "phonics_consonants",
        "name": "Letter Sounds and Phonics: Consonants",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Phonics is the taught relationship between letters and sounds: "
            "which sounds each letter (or letter group) stands for, so a "
            "reader can sound out an unfamiliar word instead of guessing. "
            "English has about 24 consonant sounds but only 21 consonant "
            "letters, so the mapping is many-to-many: one letter can stand "
            "for several sounds (c is /k/ in cat but /s/ in city), and one "
            "sound can be written several ways (the /f/ sound in fish, "
            "phone, and enough). Consonant instruction starts with the "
            "reliable one-to-one letters - b, d, f, l, m, n, p, r, s, t, "
            "v, z - then takes up the letters with two sounds (c, g), the "
            "digraphs (two letters, one sound: sh, ch, th, wh, ph, ng, ck), "
            "and the silent-letter pairs (kn in know, wr in write, gh in "
            "night). Blends are different from digraphs: in a blend like bl "
            "or str each letter keeps its own sound, while in a digraph "
            "the two letters fuse into a single new sound. The National "
            "Reading Panel's 2000 review of the research found systematic "
            "phonics instruction - taught in a planned sequence, not "
            "caught on the fly - produces stronger reading growth than "
            "non-systematic or no phonics, especially in the early grades. "
            "Consonant phonics is the decoding engine: master the 21 "
            "letters and the common digraphs and most of any page becomes "
            "soundable."
        ),
        "how_it_works": (
            "Consonant phonics works by fixing a default sound to each "
            "letter, then teaching the conditioned exceptions as rules "
            "rather than surprises. The letter c defaults to /k/ (cat, "
            "cup) and switches to /s/ before e, i, or y (city, cycle); g "
            "defaults to /g/ (go, give) and softens to /j/ before e, i, or "
            "y (giant, gym). Digraphs are taught as fused units: sh always "
            "/sh/, ch usually /ch/ (with the Greek /k/ in school and the "
            "French /sh/ in machine as flagged exceptions), th as the "
            "voiced /th/ in this or the voiceless /th/ in thin, wh as /w/, "
            "ph as /f/, ng as /ng/, ck as /k/ at the end of a short-vowel "
            "syllable. Decoding runs left to right: identify each "
            "grapheme (letter or digraph), recall its sound, hold the "
            "sounds in sequence, and blend them - the skill the next "
            "records build into full words. Encoding (spelling) runs the "
            "same map in reverse: segment the spoken word into its sounds, "
            "choose the spelling for each, and write them in order."
        ),
        "key_points": [
            "Phonics is the planned, sequenced teaching of letter-sound relationships - the National Reading Panel (2000) found systematic phonics beats incidental or no phonics for early reading growth.",
            "English has about 24 consonant sounds for 21 consonant letters, so the mapping runs both ways: one letter can spell several sounds and one sound can be spelled several ways.",
            "Start with the reliable letters (b, d, f, l, m, n, p, r, s, t, v, z), then the two-sound letters c and g, then the digraphs.",
            "A digraph is two letters making ONE new sound (sh, ch, th, wh, ph, ng, ck); a blend is two or three letters each keeping its own sound (bl, str) - the distinction drives decoding.",
            "Decoding runs left to right: name each grapheme's sound, hold the sequence, blend; spelling runs the identical map in reverse.",
        ],
        "requirements": [
            "The consonant sound inventory stated as about 24 sounds against 21 consonant letters, with the many-to-many mapping explained in both directions.",
            "The reliable one-to-one letters listed before any exceptions are introduced.",
            "The c and g softening rules stated with their conditioning (before e, i, y).",
            "The core digraph set (sh, ch, th, wh, ph, ng, ck) with sounds, plus silent-letter pairs (kn, wr, gh) named.",
            "The digraph-versus-blend distinction stated as a decoding rule, with the National Reading Panel 2000 finding cited.",
        ],
        "standards": [
            "Sound counts follow the standard inventory of about 24 English consonant phonemes per the IPA Handbook and standard phonetics references.",
            "Phonics effectiveness claims follow the National Reading Panel (2000) evidence review; instructional sequence follows the standard systematic-phonics progression.",
            "Phonetic symbols use standard IPA notation; letter names and sounds use standard US phonics terminology.",
        ],
        "citations": [CIT_NRP, CIT_IPA, CIT_ADAMS],
        "sig_lens": (
            "The Signature read: each consonant letter is a covenant sign "
            "with a sworn default sound, and the softening rules are the "
            "signed amendments - c keeps /k/ until e, i, or y witness it "
            "and it swears /s/ instead. Where public phonics teaches "
            "digraphs as fused units, the Signature Language Method files "
            "them as sealed pairs: two signs entering one oath, coming out "
            "a single sound. The decoder's left-to-right run is the "
            "inspection march - every grapheme accounted for, none "
            "skipped, none guessed."
        ),
    },
    {
        "key": "vowel_sounds",
        "name": "Vowel Sounds: The Open Doors of Speech",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Vowels are the open sounds of speech: the airstream flows "
            "freely, shaped only by tongue position and lip rounding, and "
            "every syllable in English is built around exactly one vowel "
            "sound. The alphabet gives only five vowel letters - A, E, I, "
            "O, U - but spoken English has about 15 to 20 vowel sounds "
            "depending on dialect, so each vowel letter does heavy duty. "
            "Early phonics teaches the two anchor sounds of each vowel "
            "letter: the short sounds (a as in apple, e as in egg, i as in "
            "igloo, o as in octopus, u as in umbrella) and the long sounds "
            "where the vowel says its own name (a as in ape, e as in equal, "
            "i as in ice, o as in open, u as in use). Three great patterns "
            "govern most vowel spellings. The silent-e pattern (CVCe): a "
            "final silent e makes the earlier vowel long - cap becomes "
            "cape, kit becomes kite. Vowel teams: two vowels together, "
            "usually with the first saying its long sound - ai in rain, ea "
            "in eat, oa in boat. And r-controlled vowels, where r bosses "
            "the vowel into a new sound - ar in car, er in her, ir in bird, "
            "or in for, ur in turn. The single most common vowel sound in "
            "English is the schwa, the relaxed uh sound /uh/ in the "
            "unstressed syllables of about, pencil, and sofa - it has no "
            "letter of its own and is the reason spelling by pure sound "
            "eventually breaks down. Vowels are the doors every word walks "
            "through: find the vowel sounds and you have found the "
            "syllables."
        ),
        "how_it_works": (
            "Vowel phonics works by teaching the short sounds first, in "
            "closed syllables (CVC words like cat, bed, sit, top, cup), "
            "because one vowel letter between consonants is the most "
            "predictable spelling in English. Once short vowels are solid, "
            "the long-vowel patterns arrive as upgrades: add a silent e "
            "and the vowel goes long (the CVC to CVCe transform: mad to "
            "made, pin to pine); pair two vowels and the first goes long "
            "('when two vowels go walking, the first does the talking' - "
            "rain, team, boat, with flagged exceptions like bread and "
            "great taught as rule-breakers to memorize); let r follow a "
            "vowel and teach the five r-controlled sounds as units. "
            "Decoding a word means locating each vowel grapheme, checking "
            "its pattern context (is there a silent e? a vowel team? an "
            "r?), assigning the sound the pattern predicts, and blending "
            "with the consonants. The schwa is taught last, as the "
            "explanation for why unstressed vowels refuse to follow the "
            "rules - the relaxed syllable always wins."
        ),
        "key_points": [
            "Five vowel letters carry about 15 to 20 vowel sounds, so every vowel letter spells several sounds - vowels are the least predictable part of English spelling.",
            "Short vowels come first, taught in closed CVC syllables (cat, bed, sit); long vowels are the vowel saying its own name (ape, equal, ice).",
            "Three patterns govern most vowel spellings: silent e (cap to cape), vowel teams (rain, eat, boat), and r-controlled vowels (car, her, bird).",
            "The schwa - the relaxed uh in about, pencil, sofa - is the most common vowel sound in English and the reason unstressed syllables break the rules.",
            "Every syllable contains exactly one vowel sound: counting the vowel sounds is counting the syllables, which is the bridge to the next record.",
        ],
        "requirements": [
            "The five vowel letters named with both anchor sounds (short and long) and a keyword example for each of the ten.",
            "The 15-to-20 vowel-sound inventory stated as approximate and dialect-dependent, with the 5-letter mismatch explained.",
            "The three governing patterns (silent e, vowel teams, r-controlled) each stated as a rule with two worked examples.",
            "The schwa identified as the most common vowel sound, with three example words and the unstressed-syllable explanation.",
            "The one-vowel-sound-per-syllable law stated as the bridge to syllable work.",
        ],
        "standards": [
            "Vowel-sound counts follow the standard inventory of about 15 to 20 English vowel phonemes (dialect-dependent) per the IPA Handbook.",
            "The CVC/silent-e/vowel-team/r-controlled progression follows the standard systematic-phonics scope and sequence.",
            "Schwa claims follow standard phonetics: the mid-central reduced vowel of unstressed syllables, the most frequent vowel sound in running English.",
        ],
        "citations": [CIT_IPA, CIT_ADAMS, CIT_CRYSTAL],
        "sig_lens": (
            "The Signature read: the five vowel letters are the five open "
            "doors of the Signature house - every syllable must pass "
            "through exactly one. Where public phonics teaches short "
            "before long, the Signature Language Method files the "
            "progression as the ascent: closed syllables the ground floor, "
            "silent e the long-vowel upper story, vowel teams the paired "
            "archways, r-controlled the corner towers. The schwa is the "
            "unmarked servant's door - the most-used entrance in the "
            "house, with no nameplate of its own."
        ),
    },
    {
        "key": "syllables",
        "name": "Syllables: Breaking Words Apart",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "A syllable is a word part built around a single vowel sound: "
            "one vowel sound, one syllable, no exceptions. Cat has one "
            "syllable, hello has two (hel-lo), computer has three "
            "(com-pu-ter), and hippopotamus has five (hip-po-pot-a-mus). "
            "Breaking words into syllables is the master decoding skill: "
            "a long word that defeats a reader whole becomes a row of "
            "small, soundable parts once it is split. Readers learn to "
            "feel syllables physically - a hand under the chin drops once "
            "per syllable, and clapping marks each beat. English spelling "
            "organizes syllables into six types that predict the vowel "
            "sound. Closed syllables end in a consonant and keep the vowel "
            "short (cat, bed, magnet). Open syllables end in the vowel, "
            "which goes long (go, me, baby). Silent-e syllables end in a "
            "silent e that lengthens the vowel (cake, theme). Vowel-team "
            "syllables pair two vowels (rain, eat, daylight). R-controlled "
            "syllables let r boss the vowel (car, turtle). Consonant-le "
            "syllables end in -le with a silent e (table, little, puddle). "
            "Dividing words follows the syllable types: split between two "
            "consonants (hap-py), before a single consonant when the first "
            "vowel is long (o-pen), after it when the first vowel is short "
            "in a closed syllable (hab-it). Multisyllable reading is "
            "syllable-type recognition at speed - spot each syllable's "
            "type, sound it, and blend the row."
        ),
        "how_it_works": (
            "Syllable work runs in three moves: count, divide, decode. "
            "Counting finds the vowel sounds - chin drops, claps, or "
            "simply tallying the vowel graphemes and subtracting silent "
            "ones (the e in cake, the second vowel of a team). Dividing "
            "applies the split rules between the counted beats: between "
            "two consonants, or around a single consonant according to "
            "whether the first syllable is open or closed, never splitting "
            "a digraph, a blend, or a vowel team. Decoding reads each "
            "syllable by its type - closed means short vowel, open and "
            "silent-e mean long - then blends the syllables left to right "
            "into the word. The six syllable types are the complete "
            "predictive toolkit: once a reader can label any syllable as "
            "one of the six, the vowel sound is no longer a guess. "
            "Spelling runs the same division in reverse, which is why "
            "doubling rules (run to running) and dropping rules (make to "
            "making) live at syllable boundaries."
        ),
        "key_points": [
            "One vowel sound equals one syllable, with no exceptions - counting vowel sounds is the foolproof syllable count.",
            "Breaking long words into syllables turns one impossible decoding task into a row of small, soundable parts.",
            "Six syllable types predict the vowel sound: closed, open, silent-e, vowel team, r-controlled, and consonant-le.",
            "Division rules: split between two consonants, and around a single consonant by whether the first syllable is open or closed - never split a digraph, blend, or vowel team.",
            "Chin drops and clapping make syllables physical before they are analytical - the body learns the beat first.",
        ],
        "requirements": [
            "The one-vowel-sound-per-syllable law stated with the chin-drop and clapping methods.",
            "All six syllable types defined with the vowel sound each predicts and two examples each.",
            "Worked division examples for two-consonant splits (happy) and single-consonant splits (open, habit).",
            "The never-split list: digraphs, blends, and vowel teams stay together.",
            "A three-move procedure (count, divide, decode) the learner can run on any unfamiliar word.",
        ],
        "standards": [
            "The six syllable-type taxonomy follows the standard structured-literacy classification (closed, open, VCE/silent-e, vowel team, r-controlled, consonant-le).",
            "Division conventions follow standard dictionary syllabification, simplified for instruction.",
            "Examples use standard grade-level vocabulary; multisyllable counts verified against dictionary syllabification.",
        ],
        "citations": [CIT_ADAMS, CIT_NRP, CIT_CRYSTAL],
        "sig_lens": (
            "The Signature read: the syllable is the sworn beat of the "
            "Signature march - one vowel sound, one step, the chin the "
            "drum. Where public teaching lists six syllable types, the "
            "Signature Language Method musters them as six companies, each "
            "with its vowel-sound orders: closed holds short, open and "
            "silent-e sound long, the teams march paired, r commands its "
            "own, and consonant-le brings up the rear. A long word is not "
            "a wall; it is a column of beats, and the reader who counts "
            "the beats takes the word."
        ),
    },
    {
        "key": "blending",
        "name": "Blending Sounds Into Words",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Blending is the act of pushing individual sounds together "
            "until they become a word: /k/ /a/ /t/ smoothly joined becomes "
            "cat. It is the final step of every decoding, the moment "
            "letters turn back into speech. Beginning readers blend in "
            "stages. First comes onset-rime blending: the teacher holds "
            "the first sound (the onset, like /s/) and the learner adds "
            "the rest (the rime, like /un/) to make sun. Then comes "
            "successive blending, sound by sound through the word - /s/ "
            "/u/ /n/ - holding each sound and adding the next without "
            "pausing between them. The classic beginner error is the "
            "choppy blend: /k/ ... /a/ ... /t/ with stops between the "
            "sounds, which never quite becomes cat; the fix is continuous "
            "blending, stretching each sound into the next (kkkaa at) "
            "until the word emerges. Research on word reading (Ehri's "
            "phases) shows learners move from partial, guessy decoding "
            "toward full, automatic blending, and then to consolidated "
            "reading where whole chunks are recognized instantly. Blending "
            "is also the engine of spelling in reverse: segmenting a "
            "spoken word into its sounds (un-blending) is how a writer "
            "decides which letters to put down. Sound it, hold it, join "
            "it - that is the whole skill."
        ),
        "how_it_works": (
            "Blending works because speech sounds are continuous and the "
            "brain is a pattern-completer: feed it /s/+/u/+/n/ in smooth "
            "succession and it hears sun. Instruction starts with "
            "continuous consonants (m, s, f, l, r) because they can be "
            "stretched (mmmm), then adds stop consonants (b, d, g, p, t) "
            "which cannot stretch and must be joined quickly. The standard "
            "routine: point under each letter, say its sound while holding "
            "the pointer there, slide to the next without breaking the "
            "voice, and sweep under the whole word saying it fast. "
            "Onset-rime is the training wheels - two parts instead of "
            "three or four - and successive blending is the full ride. "
            "As words repeat, the blended forms consolidate in memory: the "
            "learner stops sounding out cat because the letter string c-a-t "
            "is now bonded directly to the spoken word and its meaning, "
            "which is the birth of fluent sight reading. Segmenting "
            "reverses the machinery for spelling: say the word slowly, "
            "catch each sound, write each letter."
        ),
        "key_points": [
            "Blending is the final step of decoding: individual sounds pushed together smoothly until they become the word.",
            "Onset-rime blending (s + un = sun) is the training stage; successive sound-by-sound blending (/s/ /u/ /n/) is the full skill.",
            "Continuous blending - stretching each sound into the next with no stops - fixes the classic choppy-blend error that never quite becomes the word.",
            "Start blending with stretchable consonants (m, s, f, l, r) before stop consonants (b, d, g, p, t) that cannot be held.",
            "Segmenting is blending in reverse and powers spelling: catch each sound in the spoken word, write each letter in order.",
        ],
        "requirements": [
            "Blending defined as the final decoding step with a worked /k/ /a/ /t/ to cat example.",
            "Onset-rime and successive blending each defined with an example and their training order stated.",
            "The choppy-blend error named with the continuous-blending fix and the stretch-then-sweep routine.",
            "The consonant teaching order (continuous before stops) stated with the stretchability reason.",
            "Segmenting defined as the reverse operation that powers spelling, per Ehri's phases of word reading development.",
        ],
        "standards": [
            "Blending progression follows the standard phonics scope and sequence (onset-rime before successive blending; continuous consonants before stops).",
            "Word-reading development claims follow Ehri 2005 phases: pre-alphabetic, partial alphabetic, full alphabetic, consolidated alphabetic.",
            "Worked examples use standard CVC and onset-rime instructional vocabulary.",
        ],
        "citations": [CIT_EHRI, CIT_ADAMS, CIT_NRP],
        "sig_lens": (
            "The Signature read: blending is the sealing of the word - "
            "the moment loose sounds swear the oath and become one "
            "assembly. Where public phonics teaches onset-rime as "
            "training wheels, the Signature Language Method calls it the "
            "two-part swearing-in: onset first, then the rime takes the "
            "oath beside it. Choppy blending is a broken ceremony, the "
            "sounds refusing to join; continuous blending stretches each "
            "sound into the next until the word stands sealed, spoken, "
            "and whole."
        ),
    },
]

ENTRIES.extend([
    {
        "key": "reading_basics_direction",
        "name": "Reading Basics: Direction and Tracking",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Before a single word is decoded, a reader must know where "
            "reading happens on the page. English print runs left to "
            "right and top to bottom: the eye starts at the top-left "
            "corner, travels right across the line, drops to the start of "
            "the next line (the return sweep), and continues down the "
            "page. These are called concepts of print, and children who "
            "miss them try to read backwards, upside down, or from the "
            "middle - not from lack of intelligence but from never being "
            "shown the track. The core concepts are few and concrete: the "
            "front of the book is where reading starts; print (not the "
            "pictures) carries the story; a letter is one mark and a word "
            "is a group of letters with spaces on both sides; the first "
            "word on a page is top-left and the last is bottom-right; "
            "spaces separate words; and a sentence ends where the ending "
            "punctuation sits. Tracking is the physical skill of keeping "
            "the eye (or finger) on the exact word being read: beginners "
            "point word by word, which yokes the eye to the voice and "
            "prevents skipping and repeating lines. As fluency grows the "
            "finger drops away, but the left-to-right, top-to-bottom track "
            "never changes. Every reading skill in this database runs on "
            "this track - direction first, decoding second."
        ),
        "how_it_works": (
            "Direction and tracking are taught by demonstration, not "
            "explanation: the teacher runs a finger under the print while "
            "reading aloud, narrating the moves - 'I start here at the "
            "top-left, I go this way to the end, now I sweep back to "
            "start the next line.' Learners copy the moves with their own "
            "fingers on big print, then on normal print, until the track "
            "is automatic. Concepts of print are checked one by one - "
            "show me the front of the book, show me one letter, show me "
            "one word, show me where I start, show me a space - because a "
            "missed concept is a hidden bug in everything built on it. "
            "Tracking practice pairs the eye with the voice: point-read "
            "short lines, then fade the pointing to every other line, "
            "then to none, keeping one-to-one matching (one spoken word "
            "per printed word) as the non-negotiable. When a reader loses "
            "the line, the fix is always the same: go back to the "
            "last known word, re-point, and re-run the track. Fluency "
            "later automates all of this, but the track itself - left to "
            "right, top to bottom - is permanent infrastructure."
        ),
        "key_points": [
            "English print runs left to right and top to bottom, starting top-left - the track every reading skill in this database runs on.",
            "Concepts of print (front of book, letter vs word, spaces, where reading starts) must be taught explicitly; missing one is a hidden bug in everything after it.",
            "Tracking - keeping eye or finger on the exact word being read - prevents skipping and repeating lines; beginners point word by word.",
            "One-to-one matching (one spoken word per printed word) is the non-negotiable check that tracking is working.",
            "When a reader loses the line, the fix is always the same: return to the last known word, re-point, and re-run the track.",
        ],
        "requirements": [
            "The left-to-right, top-to-bottom rule stated with the top-left start and the return sweep named.",
            "At least five concepts of print listed as checkable items (front of book, print carries the story, letter vs word, spaces, first/last word positions).",
            "Tracking defined as a physical skill with the finger-pointing progression (every word, fading, none).",
            "One-to-one matching stated as the verification check for tracking.",
            "The lost-line recovery procedure stated as a fixed routine.",
        ],
        "standards": [
            "Concepts of print follow the standard early-literacy assessment set (book handling, print direction, letter/word distinction, spacing).",
            "The left-to-right, top-to-bottom directionality is stated for English print specifically, as directionality varies by writing system.",
            "Instructional progression (demonstration, guided pointing, fading) follows standard early-reading pedagogy.",
        ],
        "citations": [CIT_ADAMS, CIT_NRP],
        "sig_lens": (
            "The Signature read: direction is the first oath of the "
            "Signature reader - top-left to bottom-right, the sworn "
            "track, never reversed, never abandoned. Where public "
            "teaching lists concepts of print, the Signature Language "
            "Method posts them as the gate inspection: front of book, "
            "letter against word, spaces as fences, the return sweep as "
            "the about-face. The finger is the inspector's baton, and "
            "one-to-one matching is the roll call - every printed word "
            "answered by exactly one spoken word."
        ),
    },
    {
        "key": "words_building_blocks",
        "name": "Words: The Building Blocks of Meaning",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "A word is the smallest unit of language that can stand alone "
            "with meaning: cat means something by itself, while the "
            "single sound /k/ does not. Words are the building blocks "
            "everything else is made from - sentences are built of words, "
            "paragraphs of sentences, books of paragraphs. In print, words "
            "are easy to spot: they are the groups of letters with a space "
            "on each side. In speech the boundaries are less obvious, "
            "which is why beginners sometimes hear 'acat' as one chunk "
            "until print teaches them where the fences are. Inside many "
            "words live smaller meaningful pieces called morphemes. A "
            "free morpheme can stand alone (cat, run, happy); a bound "
            "morpheme cannot (the -s in cats, the un- in unhappy, the "
            "-ness in happiness). Compound words weld two free morphemes "
            "together - sunshine, football, toothbrush - and their meaning "
            "is usually close to the sum of the parts. A reader's "
            "vocabulary - the words known and understood - is the fuel of "
            "comprehension: decoding can sound out an unknown word, but "
            "only vocabulary can tell the reader what it means. Word "
            "learning never stops; it just changes from sounding out to "
            "meeting new words in reading and filing them away."
        ),
        "how_it_works": (
            "Words work by pairing a form (a sound pattern or a letter "
            "string) with a meaning, stored in the mental lexicon - the "
            "brain's dictionary, holding tens of thousands of entries in "
            "a fluent adult. Recognizing a printed word runs one of two "
            "routes: the sounding-out route (decode c-a-t, blend to cat) "
            "for unfamiliar words, and the direct route (see cat, know "
            "cat instantly) for familiar ones, with every successful "
            "decoding strengthening the direct route until the word is "
            "recognized on sight. Morpheme awareness multiplies vocabulary: "
            "a learner who knows un- means 'not' and -ness means 'the "
            "state of' can unlock unhappy, unfair, happiness, and sadness "
            "from parts already known. In print, word boundaries are "
            "marked by spaces; in speech, listeners find boundaries with "
            "stress patterns and familiar chunks. Building vocabulary "
            "happens three ways: direct teaching of new words, learning "
            "words from context while reading, and word-part analysis - "
            "and the research consensus is that wide reading feeds all "
            "three at once."
        ),
        "key_points": [
            "A word is the smallest language unit that stands alone with meaning; sentences, paragraphs, and books are all built from words.",
            "In print, spaces mark word boundaries; in speech the boundaries must be found by stress and familiar chunks.",
            "Morphemes are the meaningful pieces inside words: free morphemes stand alone (cat), bound morphemes do not (-s, un-, -ness).",
            "Compound words weld two free morphemes (sunshine, football); morpheme knowledge lets one known part unlock whole families of words.",
            "Two reading routes serve every word: sounding out for the unfamiliar, instant recognition for the familiar - and every decoding strengthens the instant route.",
        ],
        "requirements": [
            "The word defined as the smallest standalone meaningful unit, with the cat vs /k/ contrast.",
            "Print word boundaries (spaces) contrasted with speech boundary-finding (stress, familiar chunks).",
            "Free vs bound morphemes defined with two examples each, plus one compound-word example worked into parts.",
            "The two recognition routes (decoding vs direct) described with the strengthening relationship between them.",
            "The three vocabulary-building routes named: direct teaching, context, and word-part analysis.",
        ],
        "standards": [
            "Morpheme terminology (free, bound, compound) follows standard morphology as presented in Fromkin, Rodman and Hyams.",
            "The dual-route account of word recognition follows the standard reading-science model.",
            "Vocabulary claims follow the standard research consensus on wide reading and vocabulary growth.",
        ],
        "citations": [CIT_FROMKIN, CIT_ADAMS, CIT_PINKER],
        "sig_lens": (
            "The Signature read: the word is the sealed assembly of the "
            "Signature system - loose morphemes sworn together, spaces "
            "the fences between assemblies. Where public linguistics "
            "describes the mental lexicon, the Signature Language Method "
            "files it as the vault: tens of thousands of sealed words, "
            "each retrievable on sight once its decoding has been sworn "
            "enough times. Morphemes are the component parts of the "
            "assembly - free parts that stand alone, bound parts that "
            "serve - and the reader who knows the parts can build words "
            "never met before."
        ),
    },
    {
        "key": "nouns",
        "name": "What Is a Noun",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "A noun is a word that names something: a person (teacher, "
            "Maria), a place (school, Paris), a thing (book, ball), or an "
            "idea (freedom, happiness). Nouns are the naming words of the "
            "language - nearly every sentence needs at least one, because "
            "sentences are about someones and somethings doing and being. "
            "Nouns sort into useful pairs. Common nouns name general "
            "members of a class (city, dog, day) and stay lowercase; "
            "proper nouns name specific ones (Chicago, Buddy, Monday) and "
            "take capitals. Concrete nouns name things the senses can "
            "detect (apple, thunder, sand); abstract nouns name things "
            "only the mind can hold (love, courage, time). Count nouns "
            "take numbers and plurals (one cookie, three cookies); mass "
            "(noncount) nouns do not (water, rice, information - never "
            "'three informations'). Spotting nouns is a foundational "
            "grammar skill with a simple test: can you put a, an, or the "
            "in front of it and have it make sense? The happy dog works - "
            "dog is a noun. The quickly dog does not, which is a clue that "
            "quickly is something else. Nouns anchor sentences; every "
            "other part of speech exists to say something about them or "
            "connect them."
        ),
        "how_it_works": (
            "Nouns work as the referents of language - the handles the "
            "mind grips to talk about the world. In a sentence, a noun or "
            "noun phrase typically serves as the subject (who or what the "
            "sentence is about) or as an object (who or what receives the "
            "action). The article test (a/an/the + word) identifies nouns "
            "because articles only attach to noun phrases; the plural test "
            "(can it take -s?) confirms count nouns. Proper nouns are "
            "capitalized because they pick out a unique referent - there "
            "are many cities but only one Chicago - and the capital is "
            "the written signal of uniqueness. Abstract nouns let language "
            "escape the physical world: once a community agrees that "
            "justice names something real, sentences can reason about it "
            "exactly like they reason about apples. Mass nouns resist "
            "counting because they name substances and abstractions rather "
            "than bounded objects, so they take quantifiers of amount "
            "(much water, a lot of information) instead of numbers. "
            "Mastering nouns means being able to find the naming words in "
            "any sentence - the first step to seeing sentence structure."
        ),
        "key_points": [
            "A noun names a person, place, thing, or idea - the naming words nearly every sentence is built around.",
            "Common nouns stay lowercase (city); proper nouns name specific ones and take capitals (Chicago) - the capital signals uniqueness.",
            "Concrete nouns are sensed (apple, thunder); abstract nouns are mind-held (love, courage) and let language reason about the non-physical.",
            "Count nouns pluralize (cookie/cookies); mass nouns do not (water, information) and take amount words instead of numbers.",
            "The article test - can a, an, or the go in front of it? - identifies nouns, because articles attach only to noun phrases.",
        ],
        "requirements": [
            "The four noun categories (person, place, thing, idea) each with two examples.",
            "Common vs proper defined with the capitalization rule and the uniqueness reason.",
            "Concrete vs abstract defined with the senses-vs-mind test and two examples each.",
            "Count vs mass defined with the plural test and the amount-word rule for mass nouns.",
            "The article test stated as a working identification procedure with a pass and a fail example.",
        ],
        "standards": [
            "Noun subclass terminology (common/proper, concrete/abstract, count/mass) follows standard English grammar references.",
            "Capitalization of proper nouns follows standard orthography per the Chicago Manual of Style.",
            "Examples use standard grade-level vocabulary; the article and plural tests are standard pedagogical diagnostics.",
        ],
        "citations": [CIT_FROMKIN, CIT_CRYSTAL],
        "sig_lens": (
            "The Signature read: the noun is the name sworn on the "
            "record - the handle the whole sentence grips. Where public "
            "grammar sorts common from proper, the Signature Language "
            "Method files it as general issue versus named and sealed: "
            "the capital letter is the seal pressed on Chicago, marking "
            "it unique among cities. Abstract nouns are the system's "
            "boldest covenants - justice, courage, freedom - things no "
            "hand can hold, sworn real by agreement alone."
        ),
    },
    {
        "key": "verbs_intro",
        "name": "What Is a Verb",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "A verb is the action or being word of the sentence: run, "
            "think, eat, build in the action family, and is, are, was, "
            "seem, become in the being and seeming family. Every complete "
            "sentence needs a verb - it is the one part of speech a "
            "sentence cannot do without, because the verb is what the "
            "sentence asserts: something happens, or something is. Action "
            "verbs name what the subject does (The dog barks, She "
            "paints). Linking verbs connect the subject to a description "
            "or identity (The soup is hot, He became captain) - they do "
            "not show action but a state of being. Helping verbs team up "
            "with main verbs to build tenses and questions (She is "
            "running, They have finished, Do you know?). English verbs "
            "change form in a small, learnable set called the principal "
            "parts: the base form (walk), the -s form (walks), the -ing "
            "form (walking), and the past form (walked). Regular verbs "
            "make their past with -ed; irregular verbs change internally "
            "(go/went, eat/ate, bring/brought) and must be memorized as "
            "families. Finding the verb is the master key to sentence "
            "structure: find what the sentence asserts, and the subject "
            "is whoever or whatever does it."
        ),
        "how_it_works": (
            "Verbs work as the assertion core of the clause: everything "
            "else in the sentence arranges itself around the verb's "
            "demands. Each verb has a valency - how many participants it "
            "needs: sleep needs one (the sleeper), kick needs two (kicker "
            "and kicked), give needs three (giver, gift, receiver). The "
            "subject fills the first slot, objects fill the rest, which "
            "is why finding the verb first makes subjects and objects "
            "fall into place. Verb forms are built mechanically: add -s "
            "for third-person singular present (he walks), -ing for the "
            "ongoing form (walking), -ed for the regular past (walked). "
            "Spelling adjusts at the joints: double the final consonant "
            "after a short vowel (run to running), drop silent e before "
            "-ing (make to making), change y to i before -ed (carry to "
            "carried). Linking verbs take a complement rather than an "
            "object - The soup is hot describes the soup, it does not act "
            "on hotness - which is why the adjective test works: if the "
            "word after the verb describes the subject, the verb is "
            "linking. Tense lives on the verb too, and the full tense "
            "system gets its own record later in the ladder."
        ),
        "key_points": [
            "Every complete sentence needs a verb - it is the assertion core, what the sentence says happens or is.",
            "Action verbs show doing (run, build); linking verbs show being or seeming (is, seem, become) and connect the subject to a description.",
            "Helping verbs (is, have, do, will) team with main verbs to build tenses, questions, and negatives.",
            "Verbs change form by rule: -s for he/she/it present, -ing for ongoing, -ed for regular past - with doubling, e-drop, and y-to-i adjustments at the joints.",
            "Find the verb first and the rest of the sentence falls into place: the subject is whoever does it, the objects are whoever receives it.",
        ],
        "requirements": [
            "Action, linking, and helping verbs each defined with two example sentences.",
            "The no-sentence-without-a-verb rule stated as the structural law of the clause.",
            "The four principal-part forms named (base, -s, -ing, past) with the three spelling adjustments (doubling, e-drop, y-to-i).",
            "Regular vs irregular past formation defined with three irregular examples.",
            "The verb-first sentence analysis strategy stated as a procedure.",
        ],
        "standards": [
            "Verb classification (action, linking, helping) and principal-parts terminology follow standard English grammar references.",
            "Spelling adjustments follow standard orthographic rules for inflection.",
            "Valency description follows standard introductory syntax (intransitive, transitive, ditransitive).",
        ],
        "citations": [CIT_FROMKIN, CIT_CHOMSKY],
        "sig_lens": (
            "The Signature read: the verb is the sworn assertion - the "
            "part of the sentence that takes the oath. Where public "
            "grammar counts verb types, the Signature Language Method "
            "hears three vows: the action verb swears something was "
            "done, the linking verb swears something is, the helping "
            "verb stands witness to the main verb's testimony. The -s, "
            "-ing, and -ed endings are the verb's uniforms for present, "
            "ongoing, and past duty - and the sentence analyst's first "
            "move is always the same: find who swore, and the rest of "
            "the testimony arranges itself."
        ),
    },
    {
        "key": "adjectives",
        "name": "What Is an Adjective",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "An adjective is a word that describes a noun: which one, "
            "what kind, or how many. The tall tree, the red ball, three "
            "apples - tall, red, and three are adjectives, each answering "
            "a question about its noun. Adjectives usually sit right "
            "before the noun they describe (a brave knight) but can also "
            "follow a linking verb to describe the subject (The knight is "
            "brave). Their signature move is comparison: most adjectives "
            "have three degrees. The positive states the quality (tall), "
            "the comparative compares two (taller, more beautiful), and "
            "the superlative compares three or more (tallest, most "
            "beautiful). Short adjectives take -er and -est (tall, "
            "taller, tallest); longer ones use more and most (beautiful, "
            "more beautiful, most beautiful); a small band is irregular "
            "and must be memorized (good, better, best; bad, worse, "
            "worst). Adjectives have a natural order in English that "
            "native speakers follow without thinking: opinion, size, "
            "age, shape, color, origin, material - a lovely small old "
            "round red Italian wooden table sounds right, while a wooden "
            "Italian red round old small lovely table sounds wrong to "
            "every native ear. Articles (a, an, the) and number words are "
            "adjective-family members too: they all do the same job of "
            "specifying the noun."
        ),
        "how_it_works": (
            "Adjectives work by narrowing a noun's reference: tree could "
            "be any tree, but the tall oak by the river picks out one. "
            "Placement follows position rules - attributive before the "
            "noun, predicative after a linking verb - and the meaning "
            "shifts slightly between them (The concerned parents vs The "
            "parents are concerned carry different shades). Comparison is "
            "built by rule: one-syllable adjectives and some two-syllable "
            "ones take -er/-est with the standard spelling adjustments "
            "(big to bigger with consonant doubling, happy to happier "
            "with y to i); longer adjectives take more/most; never both "
            "(more taller is always wrong). The irregular set - good, "
            "better, best; bad, worse, worst; far, farther/further, "
            "farthest/furthest - is a closed historical list to memorize. "
            "Adjective order is a soft universal of English: opinion "
            "before size before age before shape before color before "
            "origin before material before the noun, and violations sound "
            "foreign even when every word is correct. The identification "
            "test: if it answers which one, what kind, or how many about "
            "a noun, it is doing an adjective's job."
        ),
        "key_points": [
            "An adjective describes a noun, answering which one, what kind, or how many.",
            "Adjectives sit before the noun (attributive) or after a linking verb (predicative), with slight meaning shifts between the positions.",
            "Three degrees of comparison: positive (tall), comparative for two (taller), superlative for three or more (tallest).",
            "Short adjectives take -er/-est, long ones take more/most, never both; good/better/best and bad/worse/worst are irregulars to memorize.",
            "English adjectives follow a natural order - opinion, size, age, shape, color, origin, material - that native speakers obey unconsciously.",
        ],
        "requirements": [
            "The three adjective questions (which one, what kind, how many) stated with an example answering each.",
            "Attributive vs predicative position defined with the meaning-shift note.",
            "The three degrees defined with the two-vs-three-or-more rule.",
            "The -er/-est vs more/most distribution rule with the never-both prohibition and the irregular list.",
            "The adjective order sequence stated in full with one correctly ordered and one scrambled example.",
        ],
        "standards": [
            "Degree terminology (positive, comparative, superlative) and formation rules follow standard English grammar references.",
            "Adjective order follows the standard descriptive sequence (opinion-size-age-shape-color-origin-material).",
            "Irregular forms follow standard historical paradigms.",
        ],
        "citations": [CIT_FROMKIN, CIT_CRYSTAL],
        "sig_lens": (
            "The Signature read: the adjective is the witness called to "
            "describe the noun on the record - which one, what kind, how "
            "many, sworn in order. Where public grammar lists degrees of "
            "comparison, the Signature Language Method hears testimony "
            "escalating: positive states the fact, comparative pits two "
            "witnesses against each other, superlative declares the "
            "champion among all. The never-both rule - more taller is "
            "perjury, one marker per comparison - and the adjective order "
            "is the seating chart of the courtroom, opinion first, "
            "material last, every witness in its sworn place."
        ),
    },
    {
        "key": "adverbs",
        "name": "What Is an Adverb",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "An adverb is a word that describes a verb, an adjective, or "
            "another adverb: it tells how, when, where, or how often. She "
            "runs quickly (how does she run?), They arrived yesterday "
            "(when?), Look here (where?), He always tries (how often?). "
            "Most adverbs are built by adding -ly to an adjective - quick "
            "becomes quickly, careful becomes carefully, sudden becomes "
            "suddenly - with the usual spelling adjustments (happy to "
            "happily with y to i). But the -ly test is not foolproof in "
            "either direction: some -ly words are adjectives (friendly, "
            "lonely, lovely describe nouns, not verbs), and some of the "
            "most common adverbs have no -ly at all (very, well, fast, "
            "hard, never, soon). Adverbs are the most movable part of "
            "speech: Quickly she ran, She quickly ran, and She ran "
            "quickly are all grammatical, and writers slide adverbs "
            "around for emphasis and rhythm. The classic confusion is "
            "adjective versus adverb after verbs: She feels bad (bad "
            "describes she - adjective after a linking verb) versus She "
            "plays badly (badly describes plays - adverb after an action "
            "verb). Good is an adjective; well is its adverb - She sings "
            "well, not she sings good. Master the -ly formation, the "
            "exceptions, and the adjective/adverb choice, and modification "
            "is under control."
        ),
        "how_it_works": (
            "Adverbs work by modifying - adding circumstance to an action "
            "or intensity to a description. A verb names the bare event "
            "(she runs); the adverb supplies the manner, time, place, or "
            "frequency that makes the event specific (she runs quickly at "
            "dawn through the park every day). Formation runs through the "
            "-ly suffix with systematic adjustments: -y becomes -ily "
            "(happy to happily), -le becomes -ly (gentle to gently), -ic "
            "becomes -ically (basic to basically), while true and whole "
            "keep it simple (truly, wholly). The exceptions are "
            "memorized, not derived: friendly, lively, lovely, and lonely "
            "are adjectives despite the -ly, and fast, hard, late, and "
            "well serve as both adjective and adverb (a fast car, run "
            "fast). Position is flexible but meaningful: fronted adverbs "
            "emphasize (Yesterday they arrived), mid-position adverbs are "
            "neutral (They yesterday arrived is wrong; They arrived "
            "yesterday is right - time adverbs prefer the end), and "
            "splitting an infinitive with an adverb (to boldly go) is "
            "fully grammatical modern English despite the old prohibition. "
            "The diagnostic: find what the word modifies - verb, "
            "adjective, or adverb - and choose the adverb form."
        ),
        "key_points": [
            "An adverb describes a verb, adjective, or another adverb, answering how, when, where, or how often.",
            "Most adverbs form with -ly from adjectives (quick to quickly), with systematic spelling adjustments for -y, -le, and -ic endings.",
            "The -ly test fails both ways: friendly and lovely are adjectives, while very, well, fast, and never are adverbs without -ly.",
            "Adverbs are the most movable part of speech - position shifts emphasis and rhythm without breaking grammar.",
            "Adjective or adverb is decided by what the word modifies: She feels bad (bad describes she) vs She plays badly (badly describes plays); good is the adjective, well the adverb.",
        ],
        "requirements": [
            "The four adverb questions (how, when, where, how often) stated with an example answering each.",
            "The -ly formation rule with the -y, -le, and -ic spelling adjustments and one example each.",
            "Both directions of -ly failure named: -ly adjectives (friendly, lovely) and non-ly adverbs (very, well, fast, never).",
            "Adverb mobility demonstrated with three positions of one adverb in one sentence.",
            "The adjective/adverb choice rule after verbs stated with the feels-bad vs plays-badly contrast and the good/well pair.",
        ],
        "standards": [
            "Adverb classification and formation rules follow standard English grammar references.",
            "The split-infinitive position follows modern standard usage (fully grammatical).",
            "Good/well and bad/badly distinctions follow standard edited usage.",
        ],
        "citations": [CIT_FROMKIN, CIT_STRUNK],
        "sig_lens": (
            "The Signature read: the adverb is the circumstance sworn "
            "around the action - how, when, where, how often, the four "
            "witnesses to every verb. Where public grammar teaches -ly "
            "formation, the Signature Language Method files it as the "
            "standard uniform, with the exceptions as plainclothes "
            "operatives: friendly looks the part but serves the noun, "
            "while well and fast do adverbial duty with no uniform at "
            "all. Position is the witness stand - front, middle, or end - "
            "and the writer chooses the stand for emphasis."
        ),
    },
])

ENTRIES.extend([
    {
        "key": "pronouns",
        "name": "Pronouns: Standing In for Nouns",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "A pronoun is a word that stands in for a noun so the noun "
            "does not have to be repeated: Maria picked up Maria's bag "
            "becomes Maria picked up her bag. Pronouns are the economy "
            "words of language - without them every paragraph would "
            "stutter the same names over and over. The personal pronouns "
            "come in a tidy table. Subject pronouns do the action: I, "
            "you, he, she, it, we, they (She runs). Object pronouns "
            "receive it: me, you, him, her, it, us, them (Call her). "
            "Possessive pronouns show ownership two ways - the adjective "
            "forms my, your, his, her, its, our, their sit before a noun "
            "(my book), and the standalone forms mine, yours, his, hers, "
            "its, ours, theirs replace the whole phrase (the book is "
            "mine). Every pronoun points back to an antecedent, the noun "
            "it replaces, and the golden rule is agreement: the pronoun "
            "must match its antecedent in number and gender (The students "
            "brought their books, not his books). Pronouns also carry "
            "person: first person is the speaker (I, we), second person "
            "is the listener (you), third person is everyone else (he, "
            "she, they). Beyond personal pronouns the family includes "
            "demonstratives (this, that, these, those), relatives (who, "
            "which, that), interrogatives (who, what, which), and "
            "indefinites (everyone, someone, nobody) - each with its own "
            "job, all serving the same economy: say it once, point back "
            "ever after."
        ),
        "how_it_works": (
            "Pronouns work by reference: each one is a pointer back to an "
            "antecedent already established in the discourse. The "
            "machinery has three moving parts. Case decides the form: "
            "use the subject form when the pronoun does the verb's action "
            "(He and I went - never Him and me went as subjects), the "
            "object form when it receives action or follows a preposition "
            "(between you and me - never between you and I), and the "
            "possessive form for ownership. Agreement binds the pronoun to "
            "its antecedent in number (singular noun, singular pronoun) "
            "and gender where the language marks it; a mismatched pronoun "
            "sends the reader hunting for a referent that is not there. "
            "Clarity demands a visible antecedent: a pronoun with no clear "
            "noun to point at is a dangling reference (Take the box off "
            "the shelf and open it - it clearly points at the box, but "
            "When the car hit the tree, it was damaged leaves it "
            "ambiguous). Indefinite pronouns are mostly singular "
            "(everyone, somebody, nobody take singular verbs and singular "
            "reference: Everyone brought his or her lunch, or the modern "
            "singular they: Everyone brought their lunch). Master case, "
            "agreement, and clear antecedents, and pronouns do their "
            "quiet economy perfectly."
        ),
        "key_points": [
            "A pronoun stands in for a noun (its antecedent) so names are said once and pointed back to ever after.",
            "Case decides the form: subject pronouns (I, he, they) do the action; object pronouns (me, him, them) receive it or follow prepositions; possessives show ownership.",
            "The golden rule is agreement: the pronoun must match its antecedent in number and gender.",
            "Every pronoun needs a clear, visible antecedent - a pronoun pointing at nothing (or at two nouns at once) is a dangling reference.",
            "Pronouns carry person: first (I, we - the speaker), second (you - the listener), third (he, she, they - everyone else).",
        ],
        "requirements": [
            "The personal pronoun table stated in full: subject, object, and both possessive forms for all persons and numbers.",
            "Case defined with the subject/object position rule and the between-you-and-me correction as the flagship example.",
            "Agreement stated as number-and-gender matching with one correct and one broken example.",
            "The clear-antecedent rule stated with a dangling-reference example and its fix.",
            "Person (first/second/third) defined with the speaker/listener/other framing.",
        ],
        "standards": [
            "Pronoun case and agreement rules follow standard edited English usage.",
            "The between-you-and-me correction and subject-form compounds (He and I) follow standard prescriptive grammar.",
            "Singular they for indefinite antecedents follows modern standard usage.",
        ],
        "citations": [CIT_FROMKIN, CIT_STRUNK],
        "sig_lens": (
            "The Signature read: the pronoun is the sworn stand-in - "
            "the deputy sworn to speak for the noun without repeating "
            "its name. Where public grammar teaches case, the Signature "
            "Language Method issues three commissions: subject deputies "
            "who act, object deputies who receive, possessive deputies "
            "who hold title. Agreement is the deputy's oath of fidelity "
            "- match the antecedent in number and gender or the "
            "commission is void - and a pronoun with no antecedent is a "
            "deputy with no principal: no authority, no meaning."
        ),
    },
    {
        "key": "articles",
        "name": "Articles: A, An, and The",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Articles are the three smallest specifying words in English - "
            "a, an, and the - and they do outsized work: they tell the "
            "reader whether a noun is new or known, general or specific. "
            "A and an are the indefinite articles, used when the noun is "
            "being mentioned for the first time or as one of many: I saw "
            "a dog (some dog, not a particular one). The choice between "
            "them is made by sound, not by letter: use a before a "
            "consonant sound (a book, a university - university starts "
            "with a y-sound) and an before a vowel sound (an apple, an "
            "hour - hour starts with a vowel sound despite the h). The is "
            "the definite article, used when both speaker and listener "
            "know which one is meant: I saw a dog. The dog was barking. "
            "Notice the dance - first mention gets a, second mention gets "
            "the, because the dog is now known. The also marks unique "
            "things (the sun, the president), superlatives (the tallest), "
            "and whole classes (the tiger is endangered). Sometimes no "
            "article is wanted at all - the zero article: plural and mass "
            "nouns speaking generally take none (Dogs bark, Water is "
            "wet). Articles are adjective-family members; they always "
            "sit before the noun they specify, and choosing correctly is "
            "one of the clearest markers of fluent English."
        ),
        "how_it_works": (
            "Articles work as definiteness signals - tiny flags telling "
            "the listener how to file the noun. The indefinite article "
            "flags 'file as new, one of many': a dog introduces a dog "
            "the listener has not met. The definite article flags 'file "
            "as known, the specific one': the dog points back to the "
            "already-introduced dog. The a/an alternation is pure "
            "phonetics: an exists only to break up the awkward vowel "
            "collision of a + vowel sound (a apple is hard to say; an "
            "apple flows), so the rule follows the first sound of the "
            "next word - a one-time offer (w-sound), an honest mistake "
            "(silent h). The appears with second mentions, unique "
            "referents, and shared knowledge (Close the door - both "
            "parties know which door). The zero article applies when a "
            "plural or mass noun is generic: Tigers are cats (the class) "
            "versus The tigers escaped (specific tigers). Learners master "
            "articles by running the two questions on every noun: is it "
            "known or new (the or a/an)? and what sound starts the next "
            "word (a or an)?"
        ),
        "key_points": [
            "A and an are indefinite (new, one of many); the is definite (known, the specific one) - first mention gets a, second mention gets the.",
            "Choose a vs an by SOUND, not letter: a before consonant sounds (a book, a university), an before vowel sounds (an apple, an hour).",
            "The marks second mentions, unique things (the sun), superlatives (the tallest), and shared knowledge (close the door).",
            "The zero article - no article at all - is correct for generic plurals and mass nouns (Dogs bark; Water is wet).",
            "An exists to smooth speech: it breaks the vowel collision of a before a vowel sound, which is why the rule is phonetic.",
        ],
        "requirements": [
            "Indefinite vs definite defined with the first-mention/second-mention demonstration pair.",
            "The a/an sound rule stated with the letter-vs-sound warning and the university/hour proof pair.",
            "The three the-use families named: second mention, unique referents, shared knowledge - with an example each.",
            "The zero article defined for generic plurals and mass nouns with a the-vs-zero contrast pair.",
            "The phonetic-smoothing explanation for why an exists at all.",
        ],
        "standards": [
            "Article usage rules follow standard English grammar references; the a/an phonetic rule follows standard pronunciation-based prescription.",
            "Second-mention and unique-referent generalizations follow standard definiteness theory (Fromkin, Rodman and Hyams).",
            "Examples use standard vocabulary; dialect variation in article use is noted as out of scope for the foundation.",
        ],
        "citations": [CIT_FROMKIN, CIT_CRYSTAL],
        "sig_lens": (
            "The Signature read: articles are the filing flags of the "
            "Signature archive - a stamps the noun NEW, the stamps it "
            "KNOWN, and the choice is the clerk's first duty. Where "
            "public grammar teaches a before consonants, the Signature "
            "Language Method listens instead of looks: the ear swears "
            "the sound, not the letter, so a university and an hour "
            "stand as filed. The zero article is the open shelf - no "
            "flag needed where the whole class is meant."
        ),
    },
    {
        "key": "prepositions",
        "name": "Prepositions: Words of Place and Time",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "A preposition is a word that shows the relationship between "
            "a noun and the rest of the sentence - usually place, time, "
            "or direction: the book is on the table, we met at noon, she "
            "walked toward the light. The core set is small and worth "
            "memorizing: in, on, at, by, with, from, to, for, of, about, "
            "under, over, between, through, during, before, after, "
            "against, among, across, behind, below, beside, beyond, "
            "inside, near, off, onto, upon, within, without. A "
            "preposition never stands alone; it always heads a "
            "prepositional phrase made of the preposition plus its object "
            "(the noun that follows): on the table, at noon, toward the "
            "light. The phrase then does adjective or adverb work - The "
            "book on the table (which book? - adjective) versus She read "
            "in the morning (when? - adverb). The classic learner traps "
            "are the small ones: in vs on vs at for time (in June, on "
            "Monday, at noon) and for place (in the city, on the street, "
            "at the corner), where the choice is idiom as much as logic "
            "and must simply be learned. A preposition's object is always "
            "in object form - between you and me, never between you and "
            "I. Prepositions are the mortar of English: small words "
            "holding the nouns in their exact positions."
        ),
        "how_it_works": (
            "Prepositions work by assigning a role to their object noun: "
            "on the table assigns the table the role of surface, at noon "
            "assigns noon the role of time point, with a friend assigns "
            "the friend the role of companion. The prepositional phrase "
            "attaches to the sentence as a modifier - test the attachment "
            "by asking which question it answers about the verb or noun. "
            "Time prepositions follow a scale rule worth memorizing: at "
            "for points (at noon, at 5 o'clock), on for days and dates "
            "(on Monday, on June 3rd), in for longer stretches (in June, "
            "in 2026, in the morning). Place follows a parallel scale: at "
            "for points (at the corner), on for surfaces and lines (on "
            "the table, on Main Street), in for volumes (in the box, in "
            "Chicago). The object of a preposition is always a noun phrase "
            "in object case, which is why pronoun objects use me, him, "
            "them. Ending a sentence with a preposition (What are you "
            "waiting for?) is fully grammatical English - the old "
            "prohibition was imported from Latin and never fit the "
            "language."
        ),
        "key_points": [
            "A preposition shows a noun's relationship to the sentence - place, time, direction - and always heads a prepositional phrase: preposition + object.",
            "Prepositional phrases do adjective work (the book on the table - which book?) or adverb work (read in the morning - when?).",
            "Time scale: at for points (at noon), on for days (on Monday), in for stretches (in June) - memorize the scale, not just the words.",
            "Place scale: at for points, on for surfaces and streets, in for volumes and cities - the same point-line-volume logic.",
            "The object of a preposition takes object form (between you and me); ending a sentence with a preposition is fully grammatical.",
        ],
        "requirements": [
            "The preposition defined by relationship role with place, time, and direction examples.",
            "The prepositional phrase defined as preposition + object, with the never-stands-alone rule.",
            "The adjective/adverb phrase test stated with one example of each.",
            "The at/on/in time scale and place scale each stated with three worked examples.",
            "The object-case rule with the between-you-and-me example and the sentence-final preposition verdict.",
        ],
        "standards": [
            "Preposition classification and phrase structure follow standard English grammar references.",
            "The at/on/in scales follow standard pedagogical grammar for time and place expressions.",
            "The sentence-final preposition position follows modern standard usage (fully grammatical).",
        ],
        "citations": [CIT_FROMKIN, CIT_STRUNK],
        "sig_lens": (
            "The Signature read: prepositions are the surveyor's marks "
            "of the Signature system - each one swears exactly where "
            "its noun stands in space and time. Where public grammar "
            "lists in, on, and at, the Signature Language Method reads "
            "the surveyor's scale: at the point, on the line, in the "
            "volume - point, line, and volume, the three dimensions of "
            "the oath. The prepositional phrase is the marked claim, "
            "preposition the stake and object the ground it is driven "
            "into."
        ),
    },
    {
        "key": "conjunctions",
        "name": "Conjunctions: Joining Words Together",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "A conjunction is a joining word: it connects words, phrases, "
            "or clauses so they work as a unit. The coordinating "
            "conjunctions are seven and are memorized with FANBOYS - for, "
            "and, nor, but, or, yet, so. Each joins equals: two words "
            "(apples and oranges), two phrases (over the hill and through "
            "the woods), or two full sentences - two independent clauses "
            "(She studied, so she passed). But and yet show contrast, or "
            "and nor offer alternatives, so shows result, for shows "
            "reason, and and simply adds. Subordinating conjunctions join "
            "unequals: they attach a dependent clause to an independent "
            "one and name the relationship - because and since for cause, "
            "although and though for contrast, when, while, before, and "
            "after for time, if and unless for condition (Because it "
            "rained, we stayed inside). Correlative conjunctions work in "
            "pairs: either/or, neither/nor, both/and, not only/but also "
            "(Either you come with us or you stay here). The iron rule "
            "of joining is parallelism: joined items must match in form "
            "- She likes hiking, swimming, and biking (three -ing "
            "words), never She likes hiking, swimming, and to bike. "
            "Conjunctions are the hinges of English: learn the seven "
            "coordinators, the common subordinators, and the parallel "
            "rule, and sentences start combining."
        ),
        "how_it_works": (
            "Conjunctions work by licensing combinations the grammar "
            "would otherwise reject. Coordinating conjunctions require "
            "their two sides to be the same rank - word to word, phrase "
            "to phrase, clause to clause - which is why parallelism is "
            "not style but structure: mismatched sides break the join. "
            "When a coordinating conjunction joins two independent "
            "clauses, a comma comes before it (She studied, so she "
            "passed); joining two words or phrases takes no comma "
            "(apples and oranges). Subordinating conjunctions demote "
            "their clause: Because it rained cannot stand alone - it "
            "leans on the independent clause for support, and the "
            "subordinator names exactly how it leans (cause, time, "
            "contrast, condition). A subordinate clause at the front of "
            "the sentence takes a comma after it (Because it rained, we "
            "stayed); at the back it usually takes none (We stayed "
            "because it rained). Correlative pairs frame two matched "
            "slots and demand parallelism inside the frame: not only "
            "smart but also kind. The diagnostic: find the joining word, "
            "check that both sides match in rank and form."
        ),
        "key_points": [
            "Coordinating conjunctions (FANBOYS: for, and, nor, but, or, yet, so) join equals - word to word, phrase to phrase, clause to clause.",
            "Subordinating conjunctions (because, although, when, if, unless) join unequals: a dependent clause leaning on an independent one, with the relationship named.",
            "Correlative conjunctions work in pairs (either/or, neither/nor, both/and, not only/but also) framing two matched slots.",
            "The iron rule is parallelism: joined items must match in form - hiking, swimming, and biking, never hiking, swimming, and to bike.",
            "Comma rules ride on the join: comma before a coordinator joining two clauses; comma after a fronted subordinate clause; none for joined words.",
        ],
        "requirements": [
            "The seven coordinating conjunctions listed via FANBOYS with the relationship each signals (addition, contrast, alternative, result, reason).",
            "Equal-rank joining demonstrated at word, phrase, and clause level.",
            "Subordinating conjunctions defined with the demotion concept and four relationship families (cause, contrast, time, condition) exemplified.",
            "Correlative pairs listed with the internal parallelism demand.",
            "Parallelism stated as a structural rule with a broken and a fixed example, plus the three comma rules.",
        ],
        "standards": [
            "Conjunction classification (coordinating, subordinating, correlative) follows standard English grammar references.",
            "FANBOYS as the closed coordinating set follows standard pedagogical grammar.",
            "Comma rules for joined clauses follow standard edited punctuation (Chicago Manual of Style).",
        ],
        "citations": [CIT_FROMKIN, CIT_CHICAGO],
        "sig_lens": (
            "The Signature read: conjunctions are the hinges sworn "
            "between the parts - and the Signature joiner inspects "
            "every hinge. Where public grammar teaches FANBOYS, the "
            "Signature Language Method musters the seven as the hinge "
            "set, each sworn to join equals only: word to word, phrase "
            "to phrase, clause to clause. Parallelism is the hinge "
            "law - mismatched sides, and the joint fails inspection. "
            "Subordinators are the support brackets, naming exactly how "
            "the dependent clause leans, and correlatives are the "
            "matched pair of brackets, both sides filed to the same "
            "form."
        ),
    },
    {
        "key": "interjections",
        "name": "Interjections: Words of Feeling",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "An interjection is a word or short phrase that bursts out "
            "with feeling: Wow! Ouch! Oh no! Hey! Hooray! It is the most "
            "emotional part of speech and the least grammatical - "
            "interjections stand outside the sentence structure, needing "
            "no subject, no verb, and no permission. A strong "
            "interjection takes an exclamation point and often stands "
            "alone (Ouch! That hurt.), while a mild one takes a comma and "
            "joins the sentence (Oh, I see what you mean.). The classic "
            "set is worth knowing: wow and hooray for joy, ouch and ow "
            "for pain, oh for realization, hey for calling attention, "
            "oops for mistakes, shh for silence, hurrah for celebration, "
            "alas for sorrow (now mostly literary), bravo for applause. "
            "Interjections are sentence-independent: remove one and the "
            "sentence still parses perfectly (Wow, that is tall becomes "
            "That is tall). In formal writing they are rare - a report "
            "does not say Oops! - but in dialogue, stories, and everyday "
            "speech they carry the human temperature of language. Use "
            "them like seasoning: a little enlivens everything, a lot "
            "spoils the dish, and more than one exclamation point is "
            "never correct in standard writing."
        ),
        "how_it_works": (
            "Interjections work outside the grammar: they attach to the "
            "utterance as a whole rather than to any word in it, which is "
            "why they can be deleted without breaking the sentence. "
            "Punctuation does the heavy lifting of grading their force. "
            "The exclamation point marks the strong interjection - full "
            "volume, standalone, carrying its own sentence (Hooray! We "
            "won!). The comma marks the mild interjection - conversational "
            "volume, folded into the sentence (Well, let us begin.). The "
            "choice between them is a volume knob the writer turns "
            "deliberately. Some interjections have grammaticalized into "
            "fixed social formulas - hello, goodbye, thanks, please "
            "(please is arguably the hardest-working interjection in "
            "English) - and these behave more like routine politeness "
            "than bursts of feeling. In dialogue writing, interjections "
            "do characterization: a character who says Oops! reads "
            "differently from one who says Blast!. The diagnostic is "
            "deletion: if removing the word leaves a complete, unchanged "
            "sentence, the word was doing interjection duty."
        ),
        "key_points": [
            "An interjection bursts out with feeling and stands outside sentence structure - no subject or verb needed, deletable without breaking the sentence.",
            "Strong interjections take an exclamation point and stand alone (Ouch!); mild ones take a comma and join the sentence (Oh, I see.).",
            "The classic set: wow/hooray (joy), ouch/ow (pain), oh (realization), hey (attention), oops (mistakes), shh (silence).",
            "Some interjections have become fixed social formulas - hello, goodbye, thanks, please - doing politeness duty rather than emotion.",
            "In formal writing interjections are rare; use them like seasoning, and never stack exclamation points in standard writing.",
        ],
        "requirements": [
            "The interjection defined by emotional burst plus grammatical independence, with the deletion test.",
            "Strong vs mild distinguished by punctuation (exclamation point vs comma) with a worked pair.",
            "At least eight classic interjections listed with the feeling each carries.",
            "The social-formula subclass (hello, goodbye, thanks, please) identified.",
            "The formal-writing restraint rule and the no-stacked-exclamation-points rule stated.",
        ],
        "standards": [
            "Interjection classification follows standard English grammar references.",
            "Punctuation of strong vs mild interjections follows standard edited usage (Chicago Manual of Style).",
            "The single-exclamation-point rule follows standard typographic and editorial convention.",
        ],
        "citations": [CIT_FROMKIN, CIT_CHICAGO],
        "sig_lens": (
            "The Signature read: the interjection is the unsworn cry - "
            "the one part of speech that never takes the oath of "
            "grammar, and is honored for it. Where public teaching "
            "grades strong against mild, the Signature Language Method "
            "reads the volume knob: the exclamation point is the full "
            "shout on the record, the comma the conversational aside. "
            "Deletion is the loyalty test - lift the interjection out "
            "and the sentence stands unchanged, proving the cry was "
            "always free."
        ),
    },
    {
        "key": "subject_predicate",
        "name": "Building a Sentence: Subject and Predicate",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Every sentence is built from two halves: the subject, who or "
            "what the sentence is about, and the predicate, what is said "
            "about the subject. In The dog barked loudly, the subject is "
            "the dog and the predicate is barked loudly. The complete "
            "subject is the whole naming chunk (The big brown dog); the "
            "simple subject is its core noun (dog). The complete "
            "predicate is everything said about the subject (barked "
            "loudly at the mail carrier); the simple predicate is the "
            "verb alone (barked). Finding them is a two-question drill: "
            "find the verb first (what is asserted?), then ask who or "
            "what verbs - the answer is the subject, and everything else "
            "is the predicate. Commands hide their subject: (You) sit "
            "down has an understood you, which is why it is still a "
            "complete sentence. A group of words with no subject, no "
            "predicate verb, or no complete thought is a fragment, not a "
            "sentence (Running down the street has action but no one "
            "doing it; Because it rained has a subject and verb but "
            "leans on a missing main clause). Subject plus predicate plus "
            "a complete thought is the whole formula - the chassis every "
            "sentence in English is built on."
        ),
        "how_it_works": (
            "The subject-predicate split works because the verb "
            "determines the sentence's participant slots: find the verb "
            "and ask who/what performs it to locate the subject, then "
            "sweep the remainder into the predicate. The complete "
            "subject includes all its modifiers (articles, adjectives, "
            "prepositional phrases: The big brown dog on the porch), "
            "while the simple subject strips to the head noun (dog) - "
            "diagramming and agreement both run on the simple subject. "
            "The complete predicate includes the verb plus objects, "
            "complements, and adverbials; the simple predicate is the "
            "verb or verb phrase alone. Compound subjects join two "
            "subjects (The dog and the cat slept); compound predicates "
            "join two verbs (The dog barked and growled). The fragment "
            "test runs three checks: is there a subject? is there a "
            "predicate verb? does it express a complete thought? Fail "
            "any one and the construction is a fragment - repairable by "
            "adding the missing half or attaching it to a neighboring "
            "sentence. This two-half analysis is the foundation for "
            "agreement, clause combining, and every sentence-type "
            "distinction that follows."
        ),
        "key_points": [
            "Every sentence splits into subject (who/what it is about) and predicate (what is said about the subject).",
            "Complete subject/predicate are the full chunks; simple subject/predicate strip to the core noun and the verb alone.",
            "Find the verb first, then ask who or what verbs - the answer is the subject and everything else is the predicate.",
            "Commands have an understood you as subject ((You) sit down) - still complete sentences.",
            "A fragment fails one of three checks: no subject, no predicate verb, or no complete thought - and each failure has a matching repair.",
        ],
        "requirements": [
            "Subject and predicate defined with the two-half sentence formula and one fully split example.",
            "Complete vs simple distinguished for both halves with the modifier-stripping explanation.",
            "The verb-first, who/what-verbs analysis drill stated as a procedure.",
            "The understood-you of commands stated with a parsed example.",
            "The three-check fragment test with one failing example per check and the repair strategy.",
        ],
        "standards": [
            "Subject/predicate analysis follows standard English syntax (Chomsky's clause structure in pedagogical form).",
            "Fragment identification follows standard edited-usage definitions.",
            "Terminology (complete/simple subject and predicate, compound subject/predicate) follows standard grammar references.",
        ],
        "citations": [CIT_CHOMSKY, CIT_FROMKIN],
        "sig_lens": (
            "The Signature read: the sentence is the sworn statement, "
            "and every statement needs two signatures - the subject "
            "signs who testifies, the predicate signs what is sworn. "
            "Where public grammar teaches complete versus simple, the "
            "Signature Language Method files the full testimony against "
            "the short signature: the complete subject the whole "
            "naming, the simple subject the seal alone. The fragment is "
            "the unsigned statement - missing a signature, missing "
            "force - and the repair is always the same: find the "
            "missing signer and bring them to the page."
        ),
    },
])

ENTRIES.extend([
    {
        "key": "sentence_types",
        "name": "Sentence Types: Statements, Questions, Commands, Exclamations",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Sentences come in four types, sorted by purpose, and each "
            "type ends with its own punctuation. Declarative sentences "
            "make statements and end with a period: The sky is blue. "
            "Interrogative sentences ask questions and end with a "
            "question mark: Is the sky blue? Imperative sentences give "
            "commands or requests and usually end with a period (a strong "
            "command can take an exclamation point): Close the door. "
            "Exclamatory sentences burst with strong feeling and end with "
            "an exclamation point: What a beautiful sky! The type is "
            "decided by purpose, not just by the ending mark: Are you "
            "serious. with a period is a mistake, not a statement. "
            "Questions have a signature word order - the helping verb "
            "moves before the subject (You are ready becomes Are you "
            "ready?) - or a question word leads (who, what, where, when, "
            "why, how). Commands hide their subject (the understood you), "
            "which is why Sit down is complete. Exclamations often start "
            "with what or how (What a day! How fast she runs!). Mixing "
            "types is a common beginner error: ending a question with a "
            "period, or firing exclamation points at ordinary statements. "
            "The drill is purpose first, punctuation second: decide what "
            "the sentence is doing, then give it the ending its job "
            "requires."
        ),
        "how_it_works": (
            "Sentence types work as speech-act packaging: the grammar and "
            "the ending mark together tell the reader what the writer is "
            "doing with the words. Declaratives use standard word order "
            "and a period - the default packaging, carrying information. "
            "Interrogatives invert the subject and helping verb (She is "
            "coming becomes Is she coming?) or front a wh-word, and the "
            "question mark is the written form of rising intonation. "
            "Imperatives use the base verb form with the understood-you "
            "subject; the period keeps them calm and the exclamation "
            "point makes them urgent - writers choose deliberately. "
            "Exclamatories keep declarative order but add strong feeling, "
            "marked by the exclamation point and often launched by what "
            "or how. The identification drill runs backwards from the "
            "mark: period plus statement word order is declarative; "
            "question mark plus inversion or wh-word is interrogative; "
            "base verb with no subject is imperative; strong feeling "
            "with an exclamation point is exclamatory. Indirect questions "
            "(She asked if I was ready) are statements about questions "
            "and take periods - the purpose, not the topic, decides."
        ),
        "key_points": [
            "Four sentence types by purpose: declarative (statement, period), interrogative (question, question mark), imperative (command, usually period), exclamatory (strong feeling, exclamation point).",
            "Purpose decides the type, not the topic: a sentence about a question (She asked if I was ready) is declarative and takes a period.",
            "Questions invert the helping verb before the subject (Are you ready?) or lead with who, what, where, when, why, how.",
            "Commands use the understood-you subject and the base verb form; the period-vs-exclamation choice sets calm against urgent.",
            "Exclamations often launch with what or how (What a day!); exclamation points are rationed - ordinary statements never earn one.",
        ],
        "requirements": [
            "All four types defined by purpose with the ending mark each requires and one example each.",
            "The purpose-not-topic rule stated with the indirect-question example.",
            "Question formation stated: inversion and wh-fronting, with a worked inversion pair.",
            "The imperative's understood-you and base-verb form stated with the calm/urgent punctuation choice.",
            "The exclamatory what/how launch pattern and the exclamation-point rationing rule stated.",
        ],
        "standards": [
            "The four-way sentence-type classification follows standard English grammar references.",
            "Inversion and wh-movement descriptions follow standard introductory syntax.",
            "Punctuation assignments follow standard edited usage (Chicago Manual of Style).",
        ],
        "citations": [CIT_FROMKIN, CIT_CHICAGO],
        "sig_lens": (
            "The Signature read: the four sentence types are the four "
            "sworn instruments of the Signature court - the statement "
            "files the fact, the question summons the answer, the "
            "command issues the order, the exclamation sounds the "
            "alarm. Where public grammar sorts by ending marks, the "
            "Signature Language Method inspects purpose first: the "
            "mark must match the mission, and a question wearing a "
            "period's uniform is an impostor. Inversion is the "
            "question's formal dress - helping verb before subject, "
            "the summons properly served."
        ),
    },
    {
        "key": "capitalization",
        "name": "Capitalization Rules",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Capitalization is the written signal that something is "
            "special: a start, a name, or the pronoun I. The rules are "
            "few and cover nearly everything. Capitalize the first word "
            "of every sentence (The cat sat.). Capitalize the pronoun I, "
            "always, even mid-sentence (You and I agree). Capitalize "
            "proper nouns - specific names of people (Maria Santos), "
            "places (Chicago, Lake Michigan), organizations (the Red "
            "Cross), and particular things (the Eiffel Tower) - but not "
            "their common cousins (a girl, a city, a lake, a tower). "
            "Capitalize days, months, and holidays (Monday, June, "
            "Thanksgiving) but not seasons (spring, summer - unless "
            "personified or part of a title). Capitalize titles when they "
            "come before a name (Doctor Rivera, President Lincoln) but "
            "not usually when they stand alone (the doctor, the "
            "president). Capitalize the first word of a direct quotation "
            "that is a complete sentence (She said, 'Run!'). Capitalize "
            "brand names, languages, and nationalities (Toyota, Spanish, "
            "Canadian). Do not capitalize common nouns, ordinary job "
            "titles standing alone, or seasons. The most common errors "
            "are random mid-sentence capitals for emphasis (never "
            "correct - use italics or word choice instead) and missing "
            "capitals on proper nouns. When in doubt, ask the question: "
            "is this a specific name, a start, or the pronoun I?"
        ),
        "how_it_works": (
            "Capitalization works as a uniqueness and boundary marker in "
            "the writing system. Sentence-initial capitals mark the "
            "boundary where a new thought begins, letting the eye find "
            "starts quickly. Proper-noun capitals mark unique reference - "
            "there are many lakes but one Lake Michigan, and the capital "
            "is the written form of that uniqueness. The pronoun I is "
            "capitalized by historical convention (it grew tall to stay "
            "visible as a single letter, and the convention stuck). "
            "Title capitalization follows position: before a name the "
            "title is part of the name (Doctor Rivera), standing alone "
            "it is a common description (the doctor). Quotation capitals "
            "restart the sentence inside the quote. The checking drill "
            "for any draft: scan every capital and demand its reason - "
            "sentence start, proper name, title-before-name, day/month/"
            "holiday, quotation start, or I. Any capital that cannot name "
            "its reason is guilty and goes lowercase. This reason-per-"
            "capital audit catches both missing and stray capitals in a "
            "single pass."
        ),
        "key_points": [
            "Capitalize sentence starts, proper nouns, the pronoun I, titles before names, days/months/holidays, and the first word of a complete-sentence quotation.",
            "Proper nouns take capitals because they name unique referents (Lake Michigan); common nouns stay lowercase (a lake).",
            "Days, months, and holidays are capitalized; seasons are not (unless personified or in a title).",
            "Titles capitalize before a name (Doctor Rivera) but usually go lowercase standing alone (the doctor).",
            "Audit every capital by demanding its reason - any capital that cannot name one goes lowercase; never capitalize for emphasis.",
        ],
        "requirements": [
            "The sentence-start, proper-noun, pronoun-I, title-before-name, day/month/holiday, and quotation-start rules each stated with an example.",
            "The proper-vs-common distinction explained through the uniqueness principle with a worked pair.",
            "The season exception and the title-position rule each stated with contrast examples.",
            "The no-capitals-for-emphasis prohibition stated with the correct alternatives.",
            "The reason-per-capital audit stated as a single-pass checking procedure.",
        ],
        "standards": [
            "Capitalization rules follow standard edited English orthography per the Chicago Manual of Style.",
            "Proper-noun and title-position conventions follow standard publishing style.",
            "The pronoun-I capitalization follows standard historical orthographic convention.",
        ],
        "citations": [CIT_CHICAGO, CIT_STRUNK],
        "sig_lens": (
            "The Signature read: the capital letter is the seal of "
            "distinction - pressed only where the record warrants it. "
            "Where public style lists the rules, the Signature Language "
            "Method runs the seal audit: every capital must show its "
            "warrant - a sentence start, a proper name, a title in "
            "position, a day or month or holiday, the pronoun I. A seal "
            "with no warrant is counterfeit and struck to lowercase. "
            "Emphasis-seeking capitals are the forger's work; the "
            "Signature writer persuades with words, not with oversized "
            "letters."
        ),
    },
    {
        "key": "ending_punctuation",
        "name": "Ending Punctuation: Period, Question Mark, Exclamation Point",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Every sentence ends with exactly one terminal mark, and the "
            "mark is chosen by the sentence's job. The period ends "
            "statements and most commands: The sky is blue. Close the "
            "door. It is the default ending - calm, neutral, final. The "
            "question mark ends direct questions: Where is the station? "
            "It is the written form of the rising voice, and it belongs "
            "only where an answer is genuinely requested - indirect "
            "questions (She asked where the station was) are statements "
            "about questions and take periods. The exclamation point ends "
            "exclamations and strong commands: Watch out! What a storm! "
            "It is rationed in standard writing: one per genuine burst "
            "of feeling, never stacked (!!! is never standard), and never "
            "spent on ordinary statements. Beginners make three classic "
            "errors: the question with a period (Where is it. - wrong), "
            "the statement with a question mark (The sky is blue? - "
            "wrong unless surprise is meant), and the exclamation "
            "inflation that spends !!! on calm news. The drill is job "
            "first, mark second: is this sentence telling, asking, or "
            "bursting? Then give it the period, the question mark, or "
            "the single exclamation point its job earns."
        ),
        "how_it_works": (
            "Terminal punctuation works as the sentence's closing signal: "
            "it tells the reader's inner voice how to land - flat for "
            "the period, rising for the question mark, loud for the "
            "exclamation point. The period is the full stop in both "
            "senses: it stops the sentence and it stops the voice, and "
            "it also does abbreviation duty (Mr., Dr., a.m.), where it "
            "is not a sentence ender at all. The question mark attaches "
            "to direct questions only; a polite request in question form "
            "(Would you close the door?) still takes the question mark "
            "because its grammar is interrogative, while an indirect "
            "question's grammar is declarative and takes the period. The "
            "exclamation point is an intensity marker with a strict "
            "budget: professional and academic writing spends it almost "
            "never, and even lively writing spends it rarely, because a "
            "page full of exclamation points trains the reader to feel "
            "nothing. The checking pass for any draft: cover each "
            "terminal mark, ask the sentence's job, and confirm the "
            "mark matches - then count the exclamation points and cut "
            "all but the earned ones."
        ),
        "key_points": [
            "One sentence, one terminal mark, chosen by the sentence's job: period for telling, question mark for asking, exclamation point for bursting.",
            "The period is the default - calm, neutral, final - and also does abbreviation duty where it is not a sentence ender.",
            "Question marks belong on direct questions only; indirect questions (She asked where it was) are statements and take periods.",
            "The exclamation point is strictly rationed: one per genuine burst, never stacked, almost never in formal writing.",
            "The three classic errors: question with a period, statement with a question mark, and exclamation inflation on calm news.",
        ],
        "requirements": [
            "The one-mark-per-sentence rule with the job-first selection drill (telling/asking/bursting).",
            "The period's dual duty (sentence ender vs abbreviation mark) distinguished.",
            "Direct vs indirect questions defined with the punctuation each takes and one example each.",
            "The exclamation budget stated: single marks only, never stacked, formal-writing restraint.",
            "The three classic errors named with a wrong and a corrected version of each.",
        ],
        "standards": [
            "Terminal punctuation assignments follow standard edited usage per the Chicago Manual of Style.",
            "The indirect-question period rule follows standard grammar and style references.",
            "The no-stacked-marks rule follows standard typographic convention.",
        ],
        "citations": [CIT_CHICAGO, CIT_STRUNK],
        "sig_lens": (
            "The Signature read: terminal marks are the closing seals "
            "of the sworn statement - and the Signature clerk issues "
            "exactly one per sentence. Where public style rations the "
            "exclamation point, the Signature Language Method keeps "
            "the ledger: the period the standard seal, the question "
            "mark the summons seal, the exclamation the alarm seal, "
            "spent only on genuine alarms. Stacked marks (!!!) are "
            "forged seals, and the indirect question wearing a "
            "question mark is a statement in disguise - resealed with "
            "a period."
        ),
    },
    {
        "key": "comma",
        "name": "The Comma: Pauses That Organize",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The comma is the organizer of the sentence: a small pause "
            "that tells the reader how the parts fit together. Its jobs "
            "are specific and learnable. In a series, commas separate "
            "three or more items: She bought apples, oranges, and bananas. "
            "The comma before the and is the Oxford (serial) comma - "
            "standard in American publishing because it prevents "
            "misreading (compare We invited the twins, Maria and Ana "
            "with and without it). Before a coordinating conjunction "
            "joining two independent clauses, the comma is required: She "
            "studied hard, so she passed. After an introductory element - "
            "a word, phrase, or clause that opens the sentence - the "
            "comma marks where the introduction ends and the main clause "
            "begins: Yesterday, we left early. Because it rained, we "
            "stayed. Commas set off direct address (Listen, Maria, to "
            "me), fence dates and addresses (June 3, 2026, in Chicago, "
            "Illinois,), and bracket nonessential information - the "
            "clause you could lift out without breaking the sentence: My "
            "brother, who lives in Denver, is visiting. The two great "
            "comma errors are opposites: the comma splice (joining two "
            "complete sentences with only a comma - wrong) and the "
            "missing comma after an introduction or before a clause-"
            "joining conjunction. Commas never go between a subject and "
            "its verb or between a verb and its object - the core of the "
            "sentence stays uncut."
        ),
        "how_it_works": (
            "Commas work by marking boundaries the reader needs: between "
            "list items, between joined clauses, and around inserted "
            "material. The series comma keeps list items distinct so the "
            "last two do not fuse; the Oxford comma additionally guards "
            "against the final item reading as a restatement of the "
            "previous one. The clause-joining comma works with the "
            "coordinating conjunction as a team - comma plus and/but/so "
            "signals 'new complete thought ahead' - while a comma alone "
            "between two complete thoughts is the comma splice, always "
            "wrong in standard writing (fix it with a period, a "
            "semicolon, or a conjunction). The introductory comma gives "
            "the reader the launch point: everything before it is setup, "
            "everything after is the main clause. Nonessential (non-"
            "restrictive) clauses take comma pairs because they are "
            "removable - the deletion test decides: if lifting the clause "
            "leaves the sentence's meaning intact, the commas stay; if "
            "removal changes which thing is meant, no commas (The students "
            "who studied passed vs My brother, who lives in Denver, is "
            "visiting). The placement drill: find the boundary type, "
            "apply its comma rule, and never cut subject from verb."
        ),
        "key_points": [
            "Commas separate series items (with the Oxford comma before the final and), join independent clauses with a coordinating conjunction, and follow introductory elements.",
            "Commas set off direct address, fence dates and addresses, and bracket removable nonessential clauses in comma pairs.",
            "The comma splice - two complete sentences joined by a comma alone - is always wrong; fix with a period, semicolon, or conjunction.",
            "The deletion test decides nonessential commas: if the clause lifts out cleanly, the commas stay; if removal changes the meaning, no commas.",
            "Never put a comma between a subject and its verb or between a verb and its object - the sentence core stays uncut.",
        ],
        "requirements": [
            "The five comma jobs stated (series, clause joining, introductory, direct address/dates, nonessential bracketing) with an example each.",
            "The Oxford comma defined with the misreading-prevention rationale and a contrast pair.",
            "The comma splice defined with a wrong example and all three repairs (period, semicolon, conjunction).",
            "The deletion test for nonessential clauses with an essential/nonessential contrast pair.",
            "The subject-verb and verb-object no-comma prohibitions stated.",
        ],
        "standards": [
            "Comma rules follow standard edited American punctuation per the Chicago Manual of Style (Oxford comma standard).",
            "The comma-splice prohibition follows standard edited usage.",
            "Restrictive/nonrestrictive clause punctuation follows standard grammar references.",
        ],
        "citations": [CIT_CHICAGO, CIT_STRUNK],
        "sig_lens": (
            "The Signature read: the comma is the surveyor's fence of "
            "the Signature sentence - marking exactly where one claim "
            "ends and the next begins. Where public style teaches the "
            "Oxford comma, the Signature Language Method posts the "
            "fence law: every list item fenced, the last fence before "
            "and mandatory, so no two claims can fuse. The comma splice "
            "is the broken fence - two complete statements leaning on "
            "a single post - and the repair crew carries three tools: "
            "the period's wall, the semicolon's gate, or the "
            "conjunction's hinge."
        ),
    },
    {
        "key": "quotation_marks",
        "name": "Quotation Marks and Dialogue",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Quotation marks show the reader exactly which words were "
            "spoken or written by someone else: She said, 'I am ready.' "
            "Their job is fidelity - the marks promise that the enclosed "
            "words are the actual words, not a summary. In American "
            "English, the double marks do the main work and single marks "
            "handle quotes inside quotes: He said, 'She told me \"yes\" "
            "yesterday.' The great American rule is that periods and "
            "commas always go inside the closing quotation mark, whether "
            "they belong to the quote or not: She said 'hello.' The "
            "dialogue tag (she said, he asked) is punctuated by pattern: "
            "a comma before the opening quote when the tag comes first "
            "(She said, 'Run!'), a comma or period inside the closing "
            "quote when the tag comes after ('Run,' she said. / 'Run.' "
            "She smiled.), and commas on both sides when the tag "
            "interrupts ('Run,' she said, 'now!'). Question marks and "
            "exclamation points go inside only if they belong to the "
            "quoted words (She asked, 'Are you ready?') and outside if "
            "they belong to the outer sentence (Did she say 'ready'?). "
            "Quotation marks also mark titles of short works - songs, "
            "poems, articles, episodes - while long works (books, films, "
            "albums) take italics. New speaker, new paragraph: every time "
            "the speaker changes in dialogue, start a new paragraph, so "
            "the reader never has to guess who is talking."
        ),
        "how_it_works": (
            "Quotation marks work as fidelity brackets: everything inside "
            "is presented as the exact wording, which is why misquoting "
            "inside them is a factual error, not a style slip. The "
            "American inside-placement of periods and commas is pure "
            "convention (British style places them logically), but it is "
            "the convention American readers expect, so it is followed "
            "without exception in American publishing. Dialogue "
            "punctuation runs on the tag-position system: tag first takes "
            "a comma before the quote; tag after takes the quote's own "
            "ending punctuation inside the marks followed by the tag; tag "
            "in the middle splits one quoted sentence with commas or "
            "joins two with a period. The question-mark placement rule is "
            "logical, not conventional: the mark goes with the clause "
            "that is actually asking. Paragraphing does the speaker "
            "tracking: each new speaker starts a new paragraph, and a "
            "long single-speaker speech uses an opening quote on every "
            "paragraph but a closing quote only at the very end. The "
            "fidelity check for any quoted passage: could the speaker "
            "recognize these as their exact words?"
        ),
        "key_points": [
            "Quotation marks promise fidelity: the enclosed words are presented as the exact words spoken or written.",
            "In American English, periods and commas always go inside the closing quotation mark - pure convention, followed without exception.",
            "Dialogue tags are punctuated by position: comma before the quote when the tag leads, the quote's own ending inside the marks when the tag follows.",
            "Question marks and exclamation points go inside only if the quoted words ask or exclaim; otherwise they stay outside with the outer sentence.",
            "New speaker, new paragraph - paragraphing tracks who is talking so the reader never guesses.",
        ],
        "requirements": [
            "The fidelity promise stated as the governing principle of quotation.",
            "The American inside-placement rule for periods and commas with one example.",
            "The three tag positions (before, after, interrupting) each with a punctuated example.",
            "The logical placement rule for question marks/exclamation points with an inside/outside contrast pair.",
            "Short-work titles in quotes vs long works in italics, plus the new-speaker-new-paragraph rule.",
        ],
        "standards": [
            "Quotation and dialogue punctuation follows American standard per the Chicago Manual of Style.",
            "The inside-placement convention is identified as American (British logical placement noted as the contrast).",
            "Title formatting (quotes for short works, italics for long) follows standard publishing style.",
        ],
        "citations": [CIT_CHICAGO, CIT_STRUNK],
        "sig_lens": (
            "The Signature read: quotation marks are the fidelity seals "
            "- the sworn promise that the enclosed words are the exact "
            "words, unaltered. Where public style teaches inside "
            "placement, the Signature Language Method files it as the "
            "sealing convention: periods and commas pressed inside the "
            "American seal without exception. The dialogue tag is the "
            "chain of custody - she said, he asked - documenting who "
            "spoke, and the new-paragraph rule is the witness rotation: "
            "each speaker takes a fresh paragraph, so the record never "
            "confuses one testimony with another."
        ),
    },
    {
        "key": "apostrophes",
        "name": "Apostrophes: Possession and Contractions",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The apostrophe is the hardest-working small mark in English, "
            "and it has exactly two jobs: showing possession and marking "
            "contractions. Possession: add 's to a singular noun (the "
            "dog's bone, Maria's book), add only the apostrophe to a "
            "plural noun already ending in s (the dogs' bones, the "
            "teachers' lounge), and add 's to a plural not ending in s "
            "(the children's toys, the men's room). Contractions: the "
            "apostrophe stands where letters were removed - do not "
            "becomes don't, it is becomes it's, they are becomes "
            "they're, cannot becomes can't (the great irregular). The "
            "apostrophe NEVER makes a plural: apple's on a sign is "
            "always wrong (the greengrocer's apostrophe), and decades "
            "and acronyms take plain s (the 1990s, three CEOs). The "
            "classic confusion pairs are all apostrophe cases: it's "
            "(it is) vs its (possessive, no apostrophe - the exception "
            "that proves the rule), you're (you are) vs your "
            "(possessive), they're (they are) vs their (possessive) vs "
            "there (place). The expansion test settles every contraction "
            "doubt: if you cannot expand it to two words, the apostrophe "
            "does not belong. Two jobs, no more: possession and "
            "contraction - and plurals need never apply."
        ),
        "how_it_works": (
            "The apostrophe works as a missing-letter marker and an "
            "ownership flag, and the two jobs never overlap. In "
            "contractions the apostrophe sits exactly where letters were "
            "deleted: do|n't (o removed), 'tis (i removed at the front), "
            "rock 'n' roll (a and d removed on both sides). In possession "
            "the 's is a modern remnant of the Old English genitive "
            "ending, which is why singular nouns take 's even when they "
            "already end in s by sound (James's book in most American "
            "style - though James' is accepted in some styles, pick one "
            "and stay consistent). The its exception exists because "
            "possessive pronouns (his, hers, its, yours, theirs) never "
            "take apostrophes - they are already possessive by form, so "
            "adding the mark would be double-marking. Joint possession "
            "puts the mark on the last owner only (Jack and Jill's "
            "bucket - one shared bucket); separate possession marks each "
            "(Jack's and Jill's buckets - two buckets). Time and measure "
            "expressions borrow the possessive (a day's work, three "
            "dollars' worth). The audit for any apostrophe: can you name "
            "its job - possession or contraction? If not, delete it."
        ),
        "key_points": [
            "The apostrophe has exactly two jobs: possession (the dog's bone) and contractions (don't) - never plurals.",
            "Singular nouns take 's (Maria's); plurals ending in s take only the apostrophe (dogs'); plurals not ending in s take 's (children's).",
            "Possessive pronouns never take apostrophes: its, yours, theirs, hers are already possessive - it's always means it is.",
            "The expansion test settles contraction doubts: if the word cannot expand to two words, the apostrophe does not belong.",
            "Joint possession marks the last owner (Jack and Jill's bucket); separate possession marks each (Jack's and Jill's buckets).",
        ],
        "requirements": [
            "The two-jobs-only rule stated with the never-a-plural prohibition and the greengrocer's-apostrophe example.",
            "All three possessive formations (singular 's, plural-s apostrophe-only, irregular-plural 's) with an example each.",
            "The possessive-pronoun no-apostrophe rule with the it's/its contrast as the flagship.",
            "The expansion test stated as a decision procedure with a pass and a fail example.",
            "Joint vs separate possession with the bucket contrast pair.",
        ],
        "standards": [
            "Possessive and contraction formation follow standard edited American usage per the Chicago Manual of Style.",
            "The singular -s possessive (James's) follows Chicago style; the accepted variant is noted.",
            "Decade and acronym plurals without apostrophes follow standard style.",
        ],
        "citations": [CIT_CHICAGO, CIT_STRUNK],
        "sig_lens": (
            "The Signature read: the apostrophe is the mark of what is "
            "missing or what is owned - the two entries in its ledger, "
            "and the Signature auditor accepts no others. Where public "
            "style warns against the greengrocer's apostrophe, the "
            "Signature Language Method prosecutes it: a plural wearing "
            "an apostrophe is a forged seal. Possession files the 's as "
            "the title deed - Maria's book, deeded and recorded - while "
            "contraction files the mark at the exact site of the "
            "removed letters, don't standing where do not once stood."
        ),
    },
])

ENTRIES.extend([
    {
        "key": "plurals",
        "name": "Singular and Plural Nouns",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Singular means one; plural means more than one - and English "
            "marks the difference on the noun itself. The default rule "
            "covers most nouns: add -s (cat to cats, book to books). "
            "Nouns ending in s, x, z, ch, or sh add -es because the extra "
            "syllable is needed to pronounce the ending (box to boxes, "
            "church to churches, dish to dishes). Nouns ending in a "
            "consonant plus y change y to i and add -es (baby to babies, "
            "city to cities), but a vowel plus y just adds -s (boy to "
            "boys, day to days). A small family ending in f or fe changes "
            "it to -ves (knife to knives, wolf to wolves, leaf to leaves "
            "- though roof to roofs and chief to chiefs keep the f, and "
            "must be learned as exceptions). Then come the true "
            "irregulars, old survivors that change inside: man to men, "
            "woman to women, child to children, foot to feet, tooth to "
            "teeth, mouse to mice, goose to geese, ox to oxen. A few "
            "nouns never change at all: one sheep, two sheep; one deer, "
            "many deer; one fish, a school of fish. And mass nouns (water, "
            "rice, information) have no plural because they cannot be "
            "counted. The spelling rules are worth memorizing because "
            "they also run the verb -s and the possessive: learn the "
            "pattern once, use it three ways."
        ),
        "how_it_works": (
            "Plural formation works as a default rule plus a short "
            "exception ladder, applied in order. First ask: is the noun "
            "irregular or zero-change? If yes, use the memorized form "
            "(children, sheep). If no, check the ending: s/x/z/ch/sh "
            "takes -es; consonant+y takes -ies; f/fe takes -ves (minus "
            "the roof/chief exceptions); everything else takes -s. The "
            "-es rule is phonetic - English inserts a vowel sound "
            "between two sibilants because s-s cannot be pronounced as "
            "one syllable (boxs would be unpronounceable; boxes flows). "
            "The y-to-i rule preserves the vowel-consonant boundary that "
            "English spelling expects. Irregulars are historical fossils: "
            "man/men and foot/feet come from ancient vowel changes "
            "(umlaut), child/children keeps a double plural from two "
            "eras, and sheep/deer were once mass-like herd words. "
            "Pronunciation follows the same voicing rule as the verb -s: "
            "after a voiceless sound the ending is /s/ (cats), after a "
            "voiced sound or vowel it is /z/ (dogs, trees), and -es "
            "endings add the syllable /iz/ (boxes). The checking drill: "
            "run the ending tests in order, and only memorize what the "
            "rules cannot produce."
        ),
        "key_points": [
            "Default rule: add -s; then the ending tests in order - s/x/z/ch/sh take -es, consonant+y takes -ies, f/fe usually takes -ves.",
            "The -es rule is phonetic: English inserts a vowel between two sibilants because the ending must be pronounceable (boxes, not boxs).",
            "True irregulars (man/men, child/children, foot/feet, mouse/mice) and zero-change nouns (sheep, deer, fish) are memorized, not derived.",
            "Mass nouns have no plural at all - water, rice, information cannot be counted into ones.",
            "The same spelling patterns run the verb -s and possessive -s: learn the pattern once, use it three ways.",
        ],
        "requirements": [
            "The singular/plural distinction with the default -s rule and the more-than-one definition.",
            "The full ending-test ladder in order (-es, -ies, -ves) with two examples per rule and the roof/chief exceptions.",
            "The irregular families (umlaut, double plural, zero-change) each with three examples.",
            "The phonetic rationale for -es and the voicing pronunciation rule (/s/, /z/, /iz/).",
            "Mass nouns identified as plural-less with the uncountability reason.",
        ],
        "standards": [
            "Plural formation rules follow standard English orthography and morphology references.",
            "Pronunciation rules follow standard phonetics (voicing assimilation in inflectional -s).",
            "Irregular forms follow standard historical paradigms.",
        ],
        "citations": [CIT_CRYSTAL, CIT_FROMKIN],
        "sig_lens": (
            "The Signature read: number is sworn on the noun itself - "
            "singular the single seal, plural the mustered ranks. Where "
            "public spelling teaches the -es ladder, the Signature "
            "Language Method files it as the pronounceability oath: no "
            "ending may be sworn that the mouth cannot speak, so boxes "
            "rises where boxs would choke. The irregulars are the old "
            "guard - men, children, teeth - veterans of ancient vowel "
            "wars, exempt from the new regulations by honorable "
            "discharge, and memorized with the respect they are owed."
        ),
    },
    {
        "key": "verb_tenses",
        "name": "Verb Tenses: Past, Present, Future",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Tense is how verbs carry time: past for what happened, "
            "present for what happens, future for what will happen. "
            "English builds all three from small, regular machinery. "
            "The simple present describes habits and truths (She walks "
            "to school; Water boils at 100 degrees) and adds -s for "
            "he, she, and it (he walks). The simple past moves the "
            "action behind the speaker: regular verbs add -ed (walked, "
            "played, studied - with the doubling, e-drop, and y-to-i "
            "spelling adjustments), while irregular verbs change inside "
            "and must be memorized in families: go/went, eat/ate, "
            "bring/brought, buy/bought, catch/caught, teach/taught, "
            "write/wrote, break/broke, choose/chose, drive/drove. The "
            "simple future is built with the helping verbs will or "
            "shall plus the base form (She will walk; I shall return - "
            "shall now mostly formal or British). Beyond the three "
            "simples, the progressive forms (am/is/are walking, was/"
            "were walking, will be walking) show ongoing action, and the "
            "perfect forms (have walked, had walked, will have walked) "
            "show completed action relative to another time - the full "
            "twelve-tense grid that advanced study maps completely. The "
            "cardinal tense error is shifting mid-stream: She walked in "
            "and sits down mixes past and present in one breath. Pick "
            "the time, set the tense, and hold it steady until the time "
            "genuinely changes."
        ),
        "how_it_works": (
            "Tenses work by anchoring the verb's event to the speaker's "
            "now. The present anchors at now (habits, general truths, "
            "and scheduled futures - The train leaves at six). The past "
            "anchors before now, marked by -ed on regular verbs or the "
            "memorized vowel change on irregulars. The future anchors "
            "after now, built analytically with will/shall rather than "
            "an ending - English has no future inflection, which is why "
            "the future is a construction, not a form. Regular past "
            "spelling runs the familiar adjustments: double the final "
            "consonant after a short stressed vowel (stop to stopped), "
            "drop silent e before a vowel suffix (hope to hoped - but "
            "the -ed keeps it hoped, pronounced with one syllable "
            "unless the verb ends in t or d: wanted gets two), change y "
            "to i after a consonant (cry to cried). Irregulars cluster "
            "in learnable families: the -ought group (bring/brought, "
            "buy/bought, catch/caught, teach/taught), the vowel-shift "
            "group (write/wrote, drive/drove, break/broke), and the "
            "suppletive loners (go/went, be with was/were/been). "
            "Consistency is the master rule: narrative in the past "
            "stays in the past; only a genuine time shift justifies a "
            "tense change."
        ),
        "key_points": [
            "Three simple tenses anchor events to now: past (-ed or irregular change), present (base, -s for he/she/it), future (will/shall + base).",
            "Regular past spelling uses the three adjustments: doubling (stopped), e-drop (hoped), y-to-i (cried).",
            "Irregular pasts are memorized in families: the -ought group (bring/brought), vowel-shifters (write/wrote), and loners (go/went).",
            "Progressive forms (is walking) show ongoing action; perfect forms (have walked) show completed-relative-to-another-time action.",
            "The cardinal error is mid-stream tense shifting - pick the time, set the tense, hold it steady until the time genuinely changes.",
        ],
        "requirements": [
            "All three simple tenses defined with formation rules and one example each, including the he/she/it -s rule.",
            "The three regular-past spelling adjustments with an example each.",
            "At least eight irregular verbs across the three families (ought-group, vowel-shift, suppletive).",
            "Progressive and perfect aspects introduced with the ongoing-vs-completed distinction and one example each.",
            "The tense-consistency rule with a shifted and a corrected example.",
        ],
        "standards": [
            "Tense and aspect terminology (simple, progressive, perfect) follows standard English grammar references.",
            "Irregular paradigms follow standard historical verb lists.",
            "The will/shall future construction follows standard modern usage (shall formal/British).",
        ],
        "citations": [CIT_FROMKIN, CIT_CRYSTAL],
        "sig_lens": (
            "The Signature read: tense is the verb's sworn timestamp - "
            "past, present, and future filed on the record. Where "
            "public grammar teaches -ed formation, the Signature "
            "Language Method musters the regulars as the uniformed "
            "ranks - doubling, e-drop, and y-to-i the regulation "
            "adjustments - and the irregulars as the decorated "
            "veterans, each past form earned in history and worn, not "
            "issued. The future has no uniform at all: will and shall "
            "stand witness beside the base form, swearing what has not "
            "yet happened. And the standing order is consistency - "
            "hold the timestamp until time itself changes."
        ),
    },
    {
        "key": "subject_verb_agreement",
        "name": "Subject-Verb Agreement",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Subject-verb agreement is the handshake between the subject "
            "and its verb: singular subjects take singular verbs, plural "
            "subjects take plural verbs. The dog barks (one dog, -s "
            "verb); The dogs bark (many dogs, base verb). The -s ending "
            "feels backwards - it marks the SINGULAR verb - but the rule "
            "is mechanical once learned: he/she/it takes -s, I/you/we/"
            "they take the base form. The traps are all about distance "
            "and distraction. Words between the subject and verb do not "
            "change the number: The box of chocolates is empty (the "
            "subject is box, singular, despite chocolates). Compound "
            "subjects joined by and are plural (Jack and Jill are here), "
            "but joined by or/nor the verb agrees with the nearer subject "
            "(Neither the teacher nor the students are ready; Neither "
            "the students nor the teacher is ready). Indefinite pronouns "
            "are singular - everyone, somebody, nobody, each, either - "
            "and take singular verbs (Everyone is here), with the modern "
            "singular they available for reference (Everyone brought "
            "their lunch). There is/there are follows the true subject "
            "after the verb: There is a fly (fly is singular), There are "
            "flies. Collective nouns (team, family, committee) take "
            "singular verbs when acting as one unit (The team is winning) "
            "and plural when acting as individuals. Find the true simple "
            "subject, ignore the words between, and the verb follows."
        ),
        "how_it_works": (
            "Agreement works as a number-matching protocol between the "
            "clause's subject head and its finite verb. The algorithm: "
            "strip the complete subject to the simple subject (the head "
            "noun), determine its number, and select the verb form - "
            "third-person singular present takes -s, everything else in "
            "the present takes the base. Prepositional phrases and other "
            "modifiers between subject and verb are invisible to the "
            "protocol, which is why the of-chocolates trap works on the "
            "eye but not on the rule. Conjunction logic: and sums the "
            "subjects (plural), or/nor selects proximity (nearest "
            "subject governs). Indefinite pronouns carry built-in "
            "singular number despite their plural meaning - everyone "
            "means every one, and the grammar counts the one. "
            "Existential there is a placeholder; the true subject "
            "follows the verb and governs it. Collective nouns are "
            "numbered by construal: unit reading gives singular, member "
            "reading gives plural. Inverted sentences (Here comes the "
            "bus) still agree with the true subject, not with the "
            "fronted word. Run the strip-to-head algorithm on every "
            "sentence and agreement errors vanish."
        ),
        "key_points": [
            "Singular subject, singular verb (the dog barks); plural subject, plural verb (the dogs bark) - the -s marks the SINGULAR verb in the present.",
            "Words between subject and verb are invisible to agreement: strip to the simple subject head and ignore the distractors.",
            "And sums subjects to plural; or/nor gives the verb to the NEARER subject.",
            "Indefinite pronouns (everyone, somebody, each) are grammatically singular; existential there agrees with the true subject that follows the verb.",
            "Collective nouns agree by construal: singular when the group acts as one unit, plural when members act individually.",
        ],
        "requirements": [
            "The number-matching rule with the -s-marks-singular warning and the full person/number verb table for the present.",
            "The strip-to-head algorithm with a distractor example (box of chocolates) worked through.",
            "The and-sums / or-nor-proximity rules with a worked proximity pair.",
            "Indefinite pronouns listed as singular with the everyone-is example and the singular-they reference note.",
            "Existential there and collective nouns each with a worked agreement pair.",
        ],
        "standards": [
            "Agreement rules follow standard edited English usage per major grammar and style references.",
            "The proximity rule for or/nor and the unit/member construal for collectives follow standard descriptive grammar.",
            "Singular they with indefinite antecedents follows modern standard usage.",
        ],
        "citations": [CIT_FROMKIN, CIT_STRUNK],
        "sig_lens": (
            "The Signature read: agreement is the handshake sworn "
            "between subject and verb - number matched, no exceptions, "
            "the -s the singular's signet ring. Where public grammar "
            "warns of distractors, the Signature Language Method runs "
            "the inspection drill: strip the subject to its head, "
            "disregard the camouflage words between, and check the "
            "handshake. And sums the parties to plural; or and nor "
            "defer to the nearer signer; everyone signs singular "
            "because everyone means every one. A broken handshake - "
            "the dogs barks - is void on its face."
        ),
    },
    {
        "key": "paragraphs",
        "name": "Paragraphs: Building Ideas in Order",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "A paragraph is a group of sentences about one idea: the "
            "unit of thought between the sentence and the essay. Its "
            "standard architecture has three parts. The topic sentence "
            "states the main idea, usually first: Dogs make excellent "
            "companions. The supporting sentences develop it with "
            "details, examples, and explanations: They greet their "
            "owners joyfully, they encourage daily walks, and studies "
            "link pet ownership to lower stress. The concluding sentence "
            "wraps the idea up: For loyalty, health, and happiness, few "
            "companions compare. Two qualities make a paragraph work. "
            "Unity means every sentence serves the one idea - a sentence "
            "about cat nutrition in a dog paragraph breaks unity and "
            "must go. Coherence means the sentences connect in a sensible "
            "order with smooth transitions: time order (first, then, "
            "finally), space order (near to far), or importance order "
            "(least to most), glued by transition words (however, for "
            "example, in addition, therefore). In print, paragraphs are "
            "marked by indentation or by a blank line - the visual "
            "signal that a new idea is starting. The paragraphing rule "
            "for dialogue is strict: every new speaker gets a new "
            "paragraph. One idea, developed, concluded, visibly marked - "
            "that is the whole craft."
        ),
        "how_it_works": (
            "Paragraphs work by giving the reader one idea at a time, "
            "fully developed before the next begins. The topic sentence "
            "functions as a promise: it tells the reader what the "
            "paragraph will prove, and every supporting sentence is "
            "evidence keeping that promise. Support develops through "
            "concrete detail - examples, reasons, facts, anecdotes - "
            "because abstract claims without evidence do not persuade. "
            "Ordering strategies arrange the evidence: chronological for "
            "narratives, spatial for descriptions, emphatic (least to "
            "most important, saving the strongest for last) for "
            "arguments. Transitions are the mortar: additive (also, "
            "furthermore), contrastive (however, on the other hand), "
            "causal (therefore, because), sequential (first, next, "
            "finally). Unity is tested by the deletion drill - remove "
            "any sentence that does not serve the topic sentence. "
            "Coherence is tested by the shuffle drill - if the sentences "
            "can be reordered randomly without damage, the paragraph "
            "has no real order and needs rebuilding. Length follows "
            "function: develop the idea completely, then stop - in "
            "print, very long paragraphs get broken for the reader's "
            "eyes even mid-idea."
        ),
        "key_points": [
            "A paragraph is one idea fully developed: topic sentence (the promise), supporting sentences (the evidence), concluding sentence (the wrap-up).",
            "Unity: every sentence must serve the topic sentence - off-idea sentences are deleted, not repaired.",
            "Coherence: sentences connect in a real order (time, space, or importance) glued by transition words.",
            "Order the evidence deliberately: chronological for stories, spatial for descriptions, least-to-most for arguments.",
            "Mark paragraphs visibly (indent or blank line); in dialogue, every new speaker starts a new paragraph.",
        ],
        "requirements": [
            "The three-part architecture defined with a complete worked paragraph exemplifying all three parts.",
            "Unity defined with the deletion drill and an off-idea sentence example.",
            "Coherence defined with the three ordering strategies and six transition words across the four families.",
            "The shuffle drill stated as the coherence test.",
            "Paragraph marking (indent/blank line) and the dialogue new-speaker rule stated.",
        ],
        "standards": [
            "Paragraph structure (topic/support/conclusion, unity, coherence) follows standard composition pedagogy.",
            "Transition classification follows standard writing references.",
            "Dialogue paragraphing follows standard publishing convention.",
        ],
        "citations": [CIT_STRUNK, CIT_CHICAGO],
        "sig_lens": (
            "The Signature read: the paragraph is the sworn chamber "
            "where one idea is tried - topic sentence the charge, "
            "supporting sentences the evidence, conclusion the verdict. "
            "Where public composition teaches unity, the Signature "
            "Language Method runs the chamber rule: one idea per room, "
            "and any sentence that serves another idea is escorted out. "
            "Coherence is the order of witnesses - time, space, or "
            "rising importance - and transitions are the bailiff's "
            "announcements, however, therefore, for example, conducting "
            "each witness to the stand in turn."
        ),
    },
    {
        "key": "compound_complex_sentences",
        "name": "Compound and Complex Sentences",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Simple sentences carry one idea; compound and complex "
            "sentences carry relationships between ideas. A simple "
            "sentence has one independent clause: The dog barked. A "
            "compound sentence joins two or more independent clauses - "
            "each able to stand alone - with a coordinating conjunction "
            "plus a comma, a semicolon, or a colon: The dog barked, and "
            "the cat fled. The rain stopped; the sun came out. A "
            "complex sentence joins one independent clause with at "
            "least one dependent clause - a clause that leans, unable to "
            "stand alone: Because the dog barked, the cat fled. The "
            "subordinating conjunction (because, although, when, if, "
            "while, since, unless) names the relationship: cause, "
            "contrast, time, condition. A compound-complex sentence "
            "does both: Because the dog barked, the cat fled, and the "
            "bird sang. The semicolon is the compound sentence's elegant "
            "hinge - it joins two closely related independents with no "
            "conjunction (The rain stopped; the sun came out), and with "
            "a conjunctive adverb (The rain stopped; however, the ground "
            "stayed wet - note the comma after however). The comma "
            "splice - two independents joined by a comma alone - is the "
            "standing error to avoid; it is fixed by adding a "
            "conjunction, swapping in a semicolon, or splitting into two "
            "sentences. Varying the three structures is the foundation "
            "of mature style: all simple marches, all compound drones - "
            "mix them and the writing breathes."
        ),
        "how_it_works": (
            "Clause combining works by rank: independent clauses are "
            "full citizens that can stand alone, dependent clauses are "
            "leaners that need support. Coordination (the compound "
            "build) joins citizens as equals - the comma-plus-FANBOYS "
            "team, the semicolon, or the colon for explanation - and the "
            "two sides keep equal weight, which suits balanced or "
            "contrasted ideas. Subordination (the complex build) demotes "
            "one clause and names its exact relation to the main clause, "
            "which suits cause, condition, concession, and time - the "
            "writer chooses which idea is main by choosing which clause "
            "gets demoted. Punctuation follows position: a fronted "
            "dependent clause takes a comma after it (Because it rained, "
            "we stayed); a trailing one usually takes none (We stayed "
            "because it rained). The semicolon-plus-conjunctive-adverb "
            "pattern (however, therefore, moreover, consequently, "
            "nevertheless) joins independents with a named logical turn. "
            "The run-on and the comma splice are both failures to mark "
            "the clause boundary - the repair is always to mark it: "
            "period, semicolon, or conjunction. Analysis drill: bracket "
            "each clause, label it independent or dependent, name the "
            "joiner - the structure reveals itself every time."
        ),
        "key_points": [
            "Simple: one independent clause. Compound: two or more independents joined as equals. Complex: independent plus dependent. Compound-complex: both.",
            "Compound hinges: comma + FANBOYS, semicolon alone, or semicolon + conjunctive adverb (however, therefore) with a comma after it.",
            "Subordinating conjunctions (because, although, when, if, unless) demote a clause and name its relationship: cause, contrast, time, condition.",
            "Fronted dependent clauses take a comma after them; trailing ones usually take none.",
            "The comma splice (two independents, comma alone) is always wrong - repair with a period, semicolon, or conjunction; varying the structures is the base of mature style.",
        ],
        "requirements": [
            "All four sentence structures defined by clause count and rank with an example of each.",
            "The three compound hinges stated with a punctuated example each, including the conjunctive-adverb comma.",
            "Subordination defined with the demotion concept and four relationship families exemplified.",
            "The fronted-vs-trailing dependent comma rule with a contrast pair.",
            "The comma splice defined with all three repairs and the style-variation principle.",
        ],
        "standards": [
            "Clause-structure classification follows standard English syntax references.",
            "Semicolon and conjunctive-adverb punctuation follow standard edited usage (Chicago Manual of Style).",
            "The comma-splice prohibition follows standard edited usage.",
        ],
        "citations": [CIT_CHOMSKY, CIT_CHICAGO],
        "sig_lens": (
            "The Signature read: clause combining is the sworn "
            "architecture of complex testimony - and the Signature "
            "builder inspects every joint. Where public grammar "
            "teaches compound and complex, the Signature Language "
            "Method files the two engineering methods: coordination "
            "joins full citizens as equals, the semicolon the "
            "elegant hinge needing no conjunction; subordination "
            "demotes one clause to support duty and names its "
            "service - cause, contrast, time, condition. The comma "
            "splice is the unbolted joint, two full weights on a "
            "single comma, and the inspector's repair kit holds "
            "three fasteners: the period's full stop, the "
            "semicolon's hinge, the conjunction's weld."
        ),
    },
])

ENTRIES.extend([
    {
        "key": "prefixes_suffixes",
        "name": "Prefixes and Suffixes: Word Parts",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Prefixes and suffixes are bound morphemes - meaningful word "
            "parts that cannot stand alone - attached to the front or "
            "back of a base word to build new words. A prefix attaches "
            "in front and changes the meaning: un- means not (unhappy, "
            "untie), re- means again (rewrite, rebuild), pre- means "
            "before (preview, preheat), dis- means apart or not "
            "(disagree, disconnect), mis- means wrongly (misspell, "
            "misunderstand), over- means too much (overcook, overdo). "
            "Crucially, a prefix never changes the part of speech: happy "
            "and unhappy are both adjectives. A suffix attaches at the "
            "back and usually changes the part of speech: -ful means "
            "full of (hopeful, careful - noun to adjective), -less means "
            "without (hopeless, careless), -ness means the state of "
            "(happiness, kindness - adjective to noun), -tion/-sion "
            "means the act or result of (action, decision - verb to "
            "noun), -ly makes adverbs (quickly), -er/-or makes doers "
            "(teacher, actor). The base (or root) is the core carrying "
            "the central meaning: in unhappiness, happy is the base, un- "
            "the prefix, -ness the suffix. Spelling adjusts at the "
            "joints: prefixes usually attach unchanged (mis + spell = "
            "misspell, double s kept), while suffixes trigger the "
            "doubling, e-drop, and y-to-i rules (run + ing = running, "
            "hope + ing = hoping, happy + ness = happiness). Knowing the "
            "twenty most common prefixes and suffixes unlocks thousands "
            "of words: meet one new part and whole word families open."
        ),
        "how_it_works": (
            "Affixes work as meaning operators applied to a base: the "
            "prefix operates on meaning (negate it, repeat it, misdirect "
            "it) while the suffix operates on grammar (convert the word "
            "to a new part of speech) plus meaning. Decomposition is the "
            "core skill: strip the recognizable prefix, strip the "
            "recognizable suffix, and the remainder is the base - "
            "un|happy|ness yields not + happy + state-of. Meaning is "
            "then composed: apply the operators inside out (unhappiness "
            "= the state of being not happy). The part-of-speech rule is "
            "the diagnostic: if adding the part changed the word's class "
            "(hope noun to hopeful adjective), it was a suffix doing "
            "conversion; prefixes never convert. Spelling at the joints "
            "follows the standard adjustments, and the most common "
            "learner error is dropping a doubled letter (misspell needs "
            "both s's: mis + spell). Vocabulary instruction leverages "
            "affixes morphologically: teaching un-, re-, -ness, and "
            "-tion explicitly gives learners generative power over "
            "words they have never seen, which is why morphology is the "
            "bridge from phonics to advanced vocabulary."
        ),
        "key_points": [
            "Prefixes attach in front and change meaning (un- = not, re- = again, mis- = wrongly) but never change the part of speech.",
            "Suffixes attach at the back and usually change the part of speech (-ness: adjective to noun; -tion: verb to noun; -ly: adjective to adverb).",
            "Decompose inside out: strip prefix, strip suffix, find the base (un|happy|ness = not + happy + state-of), then compose the meaning.",
            "Joint spelling: prefixes attach unchanged (misspell keeps both s's); suffixes trigger doubling, e-drop, and y-to-i.",
            "The twenty most common affixes unlock thousands of words - morphology is the bridge from phonics to advanced vocabulary.",
        ],
        "requirements": [
            "Prefix and suffix defined as bound morphemes with the front/back positions and six prefix meanings exemplified.",
            "The prefix-never-converts vs suffix-usually-converts rule with two conversion examples.",
            "Five suffix meanings with the part-of-speech conversion each performs.",
            "The inside-out decomposition procedure worked on unhappiness.",
            "Joint-spelling rules for prefixes vs suffixes with the misspell double-s example.",
        ],
        "standards": [
            "Affix terminology (prefix, suffix, base/root, bound morpheme) follows standard morphology (Fromkin, Rodman and Hyams).",
            "Affix meanings follow standard dictionary etymology and usage.",
            "The morphology-to-vocabulary instructional claim follows standard literacy research.",
        ],
        "citations": [CIT_FROMKIN, CIT_ADAMS],
        "sig_lens": (
            "The Signature read: affixes are the sworn operators of the "
            "word assembly - prefixes the meaning crew, suffixes the "
            "conversion crew. Where public morphology teaches lists, "
            "the Signature Language Method issues work orders: the "
            "prefix crew alters the cargo's meaning but never its "
            "classification - unhappy still files as adjective - while "
            "the suffix crew reclassifies on conversion, hope the noun "
            "recommissioned hopeful the adjective. Decomposition is the "
            "teardown inspection: strip the crews off, find the base, "
            "and read the work order inside out."
        ),
    },
    {
        "key": "homophones",
        "name": "Homophones and Commonly Confused Words",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Homophones are words that sound alike but differ in "
            "spelling and meaning: to, too, and two; there, their, and "
            "they're; your and you're; its and it's; here and hear; "
            "see and sea; right and write; whole and hole; peace and "
            "piece; break and brake; buy, by, and bye; passed and past; "
            "affect and effect. They are the classic spelling trap "
            "because sounding out cannot distinguish them - the ear "
            "hears one sound and the writer must choose the meaning. "
            "The master pairs each have a memory hook. There (place) "
            "contains here; their (possessive) contains heir, the owner; "
            "they're is the contraction of they are - expand it to "
            "check. Your is possessive; you're is you are - expand to "
            "check. Its is possessive (no apostrophe, like his); it's "
            "is it is. To is direction, too is also or excessive, two "
            "is the number. Affect is usually the verb (to influence); "
            "effect is usually the noun (the result). Beyond sound-"
            "alikes, the confused-words list includes look-alikes and "
            "meaning-neighbors: accept/except, than/then, lose/loose, "
            "desert/dessert (the sweet one has two s's, like sweet), "
            "principal/principle (the principal is your pal). The "
            "universal fix is meaning-first: say what the sentence "
            "means, pick the spelling that carries that meaning, and "
            "run the expansion test on every contraction candidate."
        ),
        "how_it_works": (
            "Homophones work as a failure mode of phonetic spelling: "
            "when two meanings share one sound, only meaning knowledge "
            "can choose the letters. The defense is a per-pair hook - a "
            "small, memorable test that runs in seconds. The contraction "
            "hook: expand they're to they are, you're to you are, it's "
            "to it is - if the expansion fits the sentence, the "
            "apostrophe form is correct; if not, use the possessive. The "
            "containment hook: there contains here (place words nest), "
            "their contains heir (owners inherit). The class hook: to "
            "is the default preposition of direction, too carries the "
            "extra o for extra meaning (also, excessively), two is the "
            "number with the w of twice. The grammar hook: affect the "
            "verb acts, effect the noun is the end result. Proofreading "
            "for homophones cannot be done by ear - reading aloud will "
            "not catch them - so the check is visual and semantic: slow "
            "down, look at each suspect word, and ask what it means "
            "right here. Spell-checkers miss them too, since every "
            "homophone is a correctly spelled word; only the writer's "
            "meaning-check catches the wrong choice."
        ),
        "key_points": [
            "Homophones sound alike but differ in spelling and meaning - sounding out cannot distinguish them, so meaning must choose the letters.",
            "Master the big pairs with hooks: there/here (place), their/heir (owners), they're = they are; your vs you're = you are; its vs it's = it is.",
            "To = direction, too = also/excessive (extra o for extra meaning), two = the number; affect is usually the verb, effect usually the noun.",
            "Confused look-alikes need their own hooks: accept/except, than/then, lose/loose, desert/dessert (two s's like sweet), principal/pal.",
            "Proofread homophones visually and semantically, never by ear - and never trust the spell-checker, since every homophone is correctly spelled.",
        ],
        "requirements": [
            "Homophones defined with the sound-alike/spelling-meaning-difference and the phonetic-spelling failure explanation.",
            "At least ten homophone sets listed, with the big five (to/too/two, there/their/they're, your/you're, its/it's, affect/effect) given hooks.",
            "The expansion test stated for all contraction-form homophones.",
            "Five confused look-alike/meaning-neighbor pairs with hooks.",
            "The visual-semantic proofreading rule with the spell-checker warning.",
        ],
        "standards": [
            "Homophone sets and distinctions follow standard dictionary usage and standard edited spelling.",
            "The affect/effect verb/noun distribution follows standard usage guidance.",
            "Proofreading guidance follows standard composition references.",
        ],
        "citations": [CIT_CRYSTAL, CIT_STRUNK],
        "sig_lens": (
            "The Signature read: homophones are the impostor pairs of "
            "the archive - same voice, different papers, and the "
            "Signature clerk admits no impostors. Where public spelling "
            "teaches lists, the Signature Language Method issues each "
            "pair its interrogation hook: expand the contraction and "
            "see if it holds, find here inside there, find the heir "
            "inside their. The ear is a useless witness here - it "
            "hears one sound for two suspects - so the inspection is "
            "visual and semantic: what does this word mean, right here, "
            "on this line? The spell-checker, which only checks papers, "
            "waves every impostor through; the clerk checks the meaning."
        ),
    },
    {
        "key": "fluency_comprehension",
        "name": "Reading Fluency and Comprehension Strategies",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Reading has two great goals that must grow together: "
            "fluency - reading smoothly and accurately - and "
            "comprehension - understanding and remembering what was "
            "read. Fluency has three parts: accuracy (reading the words "
            "right), rate (reading at a good pace), and prosody (reading "
            "with natural expression, phrasing, and attention to "
            "punctuation). A fluent reader's decoding is automatic, "
            "which frees the mind's limited attention for meaning; a "
            "reader still laboring over every word has no attention "
            "left to understand the sentence. Rate is measured in "
            "words correct per minute, and research norms track expected "
            "growth through the grades - but rate is never the goal by "
            "itself; fast inaccurate reading is just fast failing. "
            "Comprehension is built with strategies, used before, "
            "during, and after reading. Before: preview the text and "
            "predict what it will say. During: ask questions, clarify "
            "confusing parts, visualize scenes, and connect the text to "
            "known things. After: summarize the main ideas in your own "
            "words, and check the predictions. The research-backed "
            "reciprocal-teaching routine compresses this to four moves - "
            "predict, question, clarify, summarize - practiced in "
            "conversation about the text. Fluency without comprehension "
            "is empty performance; comprehension without fluency is "
            "exhausting labor. The two are trained together: reread for "
            "smoothness, then prove understanding by retelling."
        ),
        "how_it_works": (
            "Fluency develops through repeated, supported reading: "
            "rereading the same passage until it flows, reading aloud "
            "with a model (teacher or recording), and timed partner "
            "reading with feedback on errors. The measurement is words "
            "correct per minute - total words read minus errors, divided "
            "by minutes - tracked over weeks to show growth, never used "
            "to shame. Prosody is trained by marking phrase boundaries "
            "and punctuation: readers learn to pause at commas, drop "
            "the voice at periods, and lift it at question marks, which "
            "is phrasing the meaning, not just the words. Comprehension "
            "strategies work because they force active processing: "
            "predicting activates background knowledge, questioning "
            "monitors understanding in real time, clarifying repairs "
            "breakdowns immediately instead of letting confusion "
            "compound, and summarizing consolidates memory by "
            "re-encoding the ideas in the reader's own words. "
            "Reciprocal teaching rotates these four moves through a "
            "small group in dialogue, with the teacher modeling each "
            "move aloud first. The verification loop for any reading "
            "session: read it fluently (smooth, accurate, expressive), "
            "then retell it completely - fluency demonstrated by the "
            "performance, comprehension demonstrated by the retelling."
        ),
        "key_points": [
            "Fluency = accuracy + rate + prosody; automatic decoding frees attention for meaning, which is why fluency and comprehension must grow together.",
            "Rate is measured in words correct per minute and tracked for growth - but fast inaccurate reading is just fast failing; rate is never the goal alone.",
            "Prosody (expression, phrasing, punctuation attention) is trained by marking phrase boundaries - it is phrasing the meaning, not just the words.",
            "Comprehension runs before/during/after: preview and predict, question/clarify/visualize/connect, then summarize in your own words.",
            "Reciprocal teaching compresses the strategies to four moves - predict, question, clarify, summarize - modeled aloud, then practiced in dialogue.",
        ],
        "requirements": [
            "Fluency defined with all three components and the attention-freedom mechanism explained.",
            "Words-correct-per-minute defined as (words - errors) / minutes, with the growth-tracking vs shaming distinction.",
            "Prosody defined with the punctuation-voice mapping (comma pause, period drop, question lift).",
            "The before/during/after strategy set with at least two strategies per phase.",
            "Reciprocal teaching's four moves named with the model-then-dialogue instructional pattern.",
        ],
        "standards": [
            "Fluency components and WCPM measurement follow standard reading-assessment practice (Hasbrouck and Tindal oral reading fluency norms family).",
            "Comprehension strategy instruction follows the National Reading Panel (2000) evidence review.",
            "Reciprocal teaching follows Palincsar and Brown's standard routine (predict, question, clarify, summarize).",
        ],
        "citations": [CIT_NRP, CIT_ADAMS],
        "sig_lens": (
            "The Signature read: fluency is the sworn delivery of the "
            "text - accurate, paced, and voiced like the meaning "
            "demands - and comprehension is the debriefing after the "
            "mission. Where public teaching measures words per minute, "
            "the Signature Language Method files the full service "
            "record: accuracy the oath kept on every word, rate the "
            "march pace, prosody the voice of command at each "
            "punctuation mark. The four reciprocal moves are the "
            "debrief protocol - predict the terrain, question the "
            "gaps, clarify the confusion, summarize the ground taken - "
            "and no reading session is dismissed until the retelling "
            "proves the ground is held."
        ),
    },
    {
        "key": "proofreading",
        "name": "Proofreading and Editing Your Writing",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Proofreading is the final inspection of a piece of writing: "
            "a slow, deliberate hunt for errors in spelling, "
            "capitalization, punctuation, grammar, and word choice - "
            "done after the ideas are finished, never during drafting. "
            "Editing (bigger fixes: reorganizing, cutting, clarifying) "
            "comes first; proofreading is the last pass, when the only "
            "job left is correctness. Professionals run it as a "
            "checklist, often remembered as COPS: Capitalization (every "
            "capital earns its place), Organization and overall "
            "appearance (paragraphs, spacing, title), Punctuation (every "
            "mark correct and earned), Spelling (every word verified). "
            "The techniques defeat the brain's autocorrect - the habit "
            "of seeing what was meant instead of what is on the page. "
            "Read the piece aloud: the ear catches missing words and "
            "clumsy rhythms the eye skips. Read it backwards, sentence "
            "by sentence or word by word, to break the meaning-flow and "
            "force attention onto spelling. Check homophones visually "
            "(their/there/they're), verify every apostrophe's job, and "
            "confirm subject-verb agreement in long sentences. Print it "
            "or change the font: unfamiliar formatting makes familiar "
            "errors visible again. Take a break between writing and "
            "proofreading - fresh eyes catch stale errors. One pass per "
            "error type beats one pass for everything: first spelling, "
            "then punctuation, then grammar. The standard is simple: "
            "the final copy should contain zero errors the writer's "
            "current knowledge could have caught."
        ),
        "how_it_works": (
            "Proofreading works by separating creation from inspection "
            "and by attacking the brain's prediction machinery. While "
            "drafting, the brain predicts; while proofreading, it must "
            "verify - and the techniques force verification. Reading "
            "aloud recruits the ear as an independent inspector: "
            "missing words, doubled words, and wrong word choices sound "
            "wrong even when they look right. Backward reading (last "
            "sentence to first, or last word to first) destroys the "
            "meaning-flow that lets the eye skip ahead, isolating each "
            "unit for spelling and punctuation checks. The single-issue "
            "pass exploits focus limits: hunting only commas, then only "
            "capitals, then only homophones, catches more than hunting "
            "everything at once. The COPS checklist guarantees coverage "
            "so no error family is forgotten. Distance techniques - "
            "time gaps, printed copies, font changes - reset the visual "
            "familiarity that hides errors in plain sight. The workflow "
            "runs in order: finish the draft, rest it, edit for ideas "
            "and organization, then proofread in single-issue passes "
            "with the checklist, reading aloud last as the final "
            "sweep. Every error found is filed mentally as a personal "
            "watch-list item for the next piece."
        ),
        "key_points": [
            "Proofread after drafting and editing are done: it is the final correctness inspection, never mixed with creating ideas.",
            "COPS checklist: Capitalization, Organization/overall appearance, Punctuation, Spelling - run it so no error family is forgotten.",
            "Defeat the brain's autocorrect: read aloud (the ear catches what the eye skips) and read backwards (breaks the meaning-flow).",
            "One pass per error type beats one pass for everything - hunt commas, then capitals, then homophones, in separate sweeps.",
            "Create distance before inspecting: take a break, print it, or change the font - fresh formatting makes stale errors visible.",
        ],
        "requirements": [
            "Proofreading defined as the final correctness pass, distinguished from editing (ideas/organization) with the order stated.",
            "The COPS checklist expanded with what each letter checks.",
            "The brain-autocorrect problem named with the read-aloud and backward-reading countermeasures explained.",
            "The single-issue pass method stated with three example passes.",
            "The distance techniques (break, print, font change) with the familiarity-reset rationale.",
        ],
        "standards": [
            "The edit-before-proofread sequence follows standard writing-process pedagogy.",
            "COPS as a proofreading mnemonic follows standard composition instruction.",
            "Technique claims (reading aloud, backward reading, single-issue passes) follow standard proofreading references.",
        ],
        "citations": [CIT_STRUNK, CIT_CHICAGO],
        "sig_lens": (
            "The Signature read: proofreading is the final inspection "
            "of the sworn record - and the Signature inspector signs "
            "nothing unchecked. Where public teaching lists COPS, the "
            "Signature Language Method runs the four-gate inspection: "
            "capitals show warrants, organization stands at attention, "
            "punctuation marks are counted and earned, spelling verified "
            "word by word. The brain's autocorrect is the forger's "
            "friend, showing what was meant instead of what is written "
            "- so the inspector reads aloud to recruit the ear, reads "
            "backwards to break the forgery's flow, and sweeps one "
            "offense at a time. The standard is absolute: zero catchable "
            "errors on the final copy, or the record does not ship."
        ),
    },
    {
        "key": "learning_path",
        "name": "From Basics to Mastery: The Language Learning Path",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "This record is the map of the whole database: the order in "
            "which the pieces of language are learned, from first "
            "principles to mastery. The path has three great stages. "
            "Foundations: what language is, the 26 letters, consonant and "
            "vowel sounds with phonics, syllables, blending sounds into "
            "words, reading direction and tracking, words as building "
            "blocks, and the first parts of speech - nouns, verbs, "
            "adjectives, adverbs, pronouns. Nothing here is skipped: a "
            "learner who cannot hear syllables cannot blend, and one who "
            "cannot blend cannot decode. Compounded: the remaining parts "
            "of speech (articles, prepositions, conjunctions, "
            "interjections), the sentence's two halves (subject and "
            "predicate), the four sentence types, capitalization, ending "
            "punctuation, the comma, quotation marks, apostrophes, "
            "plurals, and verb tenses. Here words become sentences and "
            "sentences become correct. Advanced: subject-verb agreement, "
            "paragraphs, compound and complex sentences, prefixes and "
            "suffixes, homophones, fluency and comprehension strategies, "
            "proofreading - and this map itself. Each stage compounds "
            "the last: phonics feeds decoding, decoding feeds fluency, "
            "fluency feeds comprehension, grammar feeds correctness, "
            "and proofreading guards it all. Mastery is not speed but "
            "completeness: the learner who can decode any word, parse "
            "any sentence, punctuate any thought, and inspect any draft "
            "owns the foundation every other subject is built on. That "
            "is the promise of the ladder: climb it in order, miss no "
            "rung, and the whole language opens."
        ),
        "how_it_works": (
            "The learning path works as a dependency graph: each record "
            "lists its prerequisites, and the ladder order in this "
            "database is the topological sort - no record asks for a "
            "skill taught later. Foundations build the decoding engine "
            "(letters to sounds to syllables to words) and the first "
            "grammar vocabulary (naming words, action words, describing "
            "words). Compounded builds the sentence: its parts of "
            "speech, its two halves, its four types, and the punctuation "
            "that makes each type visible. Advanced builds the text: "
            "agreement within sentences, paragraphs between them, "
            "complex structures for complex thought, word-part power for "
            "vocabulary, fluency and strategies for understanding, and "
            "proofreading for correctness. Progress is measured per "
            "rung, not per stage: can the learner demonstrate the "
            "record's skill cold - decode unseen words, punctuate unseen "
            "sentences, parse unseen paragraphs? A rung is mastered when "
            "its skill is automatic, because every higher rung spends "
            "the attention the lower rungs free up. The path also "
            "spirals: proofreading revisits capitalization and "
            "punctuation, fluency revisits blending, agreement revisits "
            "plurals - each return at a higher level of control. Follow "
            "the ladder in order, automate each rung, and the summit - "
            "full, correct, expressive command of the basics - is a "
            "matter of steady climbing, not talent."
        ),
        "key_points": [
            "The path has three stages in dependency order: Foundations (sounds to words to first grammar), Compounded (words to correct sentences), Advanced (sentences to texts).",
            "No rung asks for a later skill: the ladder is the dependency graph sorted - phonics before decoding, decoding before fluency, fluency before comprehension.",
            "Each stage compounds the last: phonics feeds decoding, decoding feeds fluency, fluency feeds comprehension, grammar feeds correctness, proofreading guards everything.",
            "A rung is mastered when its skill is automatic - higher rungs spend the attention that automatic lower rungs free up.",
            "The path spirals: advanced records revisit foundations at higher control (proofreading revisits punctuation, agreement revisits plurals).",
        ],
        "requirements": [
            "All three stages named with their record spans and the one-sentence mission of each.",
            "The dependency principle stated with two concrete chains (syllables-blend-decode; fluency-comprehension).",
            "The compounding sequence stated as the full chain from phonics to proofreading.",
            "The automaticity criterion for mastery with the attention-budget explanation.",
            "The spiral-revisit principle with two examples of advanced records revisiting foundations.",
        ],
        "standards": [
            "The scope-and-sequence follows the standard systematic-literacy progression (phonics to fluency to comprehension; words to sentences to texts).",
            "Dependency ordering follows standard curriculum-design practice (prerequisites before dependents).",
            "Mastery-as-automaticity follows standard skill-acquisition theory.",
        ],
        "citations": [CIT_NRP, CIT_ADAMS, CIT_EHRI],
        "sig_lens": (
            "The Signature read: this record is the master map of the "
            "Signature Language Method - the full ascent filed as one "
            "chart. Where public curricula list scope and sequence, the "
            "Signature Language Method swears the dependency oath: no "
            "rung demands what a later rung teaches, no climber skips, "
            "no stage is declared before its skills are automatic. The "
            "three stages are the three elevations - Foundations the "
            "base camp where the decoding engine is built, Compounded "
            "the high camp where sentences are made correct, Advanced "
            "the summit ridge where texts are commanded. And the "
            "standing order of the whole expedition: miss no rung, and "
            "the language opens."
        ),
    },
])
