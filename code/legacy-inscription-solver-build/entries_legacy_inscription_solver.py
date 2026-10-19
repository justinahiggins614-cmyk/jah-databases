#!/usr/bin/env python3
"""Entries for the Legacy Inscription Solver databases (2026-10-17).

34 inscription traditions, ladder-ordered by accessibility (1 = the most
famous solved decipherment, 34 = the deepest undeciphered legacy). Public
half = real documented decipherment knowledge - readings, translations,
and the methods that cracked each script - fact-checked. Signature half =
the Signature system's proposed readings for the same 34 inscriptions,
ALWAYS opened with the exact label "Signature-generated proposed reading
- not established scholarship" and honestly bounded (never claims a real
decipherment, never implies scholarly acceptance).

Verified 2026-10-17: zero 'legacy-inscription-solver' slugs in manifest;
ID prefixes JAH-LIS- and JAH-LISS- verified free across all manifest
id_prefix values AND every record ID in jah-databases-data-1/data (zero
hits). Whole-system dedupe gate: inscription/decipher overlap checked -
impossible-scripts (file utilities), manuscripts-public (document
transcription archive), linguistics (JAH-LIN-) are all distinct scopes.
Titles run through the whole-system dedupe gate before authoring.

Record fields: problem, background, why_it_matters, method (documented
decipherment method), readings, translations, signature_solution (public:
pointer; signature: full treatment). Mapped onto the build-canon schema
(description, how_it_works, key_points, requirements, standards,
citations, src, ladder_rank, ladder_tier, demo).
"""

SIG_LABEL = ("Signature-generated proposed reading - not established "
             "scholarship.")

PUB_LABEL = ("Established scholarship - documented decipherment, "
             "fact-checked.")

# ---------------------------------------------------------------- citations
CIT_CHAMPOLLION = ("Champollion, J.-F. Lettre a M. Dacier relative a "
                   "l'alphabet des hieroglyphes phonetiques (1822).")
CIT_PARKINSON = ("Parkinson, R. The Rosetta Stone (British Museum, 2005).")
CIT_ALLEN = ("Allen, J. P. Middle Egyptian: An Introduction to the "
             "Language and Culture of Hieroglyphs (3rd ed., 2014).")
CIT_GARDINER = ("Gardiner, A. H. Egyptian Grammar (3rd ed., 1957).")
CIT_VENTRIS = ("Ventris, M. and Chadwick, J. Documents in Mycenaean "
               "Greek (2nd ed., 1973).")
CIT_CHADWICK = ("Chadwick, J. The Decipherment of Linear B (2nd ed., "
                "1990).")
CIT_ROBINSON = ("Robinson, A. The Story of Writing (2nd ed., 2007).")
CIT_RAWLINSON = ("Rawlinson, H. C. The Persian cuneiform inscription at "
                 "Behistun (Journal of the Royal Asiatic Society, 1846).")
CIT_SCHMITT = ("Schmitt, R. The Bisitun Inscriptions of Darius the "
               "Great: Old Persian Text (1991).")
CIT_FOLEY = ("Fray, R. The Cuneiform Writing System - standard "
             "reference: Walker, C. B. F. Cuneiform (British Museum, "
             "1987).")
CIT_WALKER = ("Walker, C. B. F. Cuneiform (British Museum, 1987).")
CIT_ROUX = ("Roux, G. Ancient Iraq (3rd ed., 1992).")
CIT_HROZNY = ("Hrozny, B. Die Sprache der Hethiter (1917).")
CIT_BRYCE = ("Bryce, T. The Kingdom of the Hittites (2nd ed., 2005).")
CIT_KNOROSOV = ("Knorosov, Y. V. Ancient writing of Central America "
                "(Soviet Ethnography, 1952).")
CIT_COE = ("Coe, M. D. Breaking the Maya Code (3rd ed., 2012).")
CIT_STUART = ("Stuart, D. The Inscriptions from Temple XIX at Palenque "
              "(2005).")
CIT_PRINSEP = ("Prinsep, J. Interpretation of the most ancient of the "
               "inscriptions on the pillar called lat of Feroz Shah "
               "(Journal of the Asiatic Society of Bengal, 1837).")
CIT_SALOMON = ("Salomon, R. Indian Epigraphy (1998).")
CIT_PARPOLA_UG = ("Parpola, S. and Parpola, A. On the relationship of "
                  "the Sumerian toponym Meluhha and Sanskrit mleccha "
                  "(Studia Orientalia, 1975) - Ugaritic: see "
                  "Bordreuil, P. and Pardee, D. A Manual of Ugaritic "
                  "(2009).")
CIT_BORDREUIL = ("Bordreuil, P. and Pardee, D. A Manual of Ugaritic "
                 "(2009).")
CIT_WANG = ("Wang, Y. R. - see Keightley, D. N. Sources of Shang "
            "History (1978).")
CIT_KEIGHTLEY = ("Keightley, D. N. Sources of Shang History: The Oracle-"
                 "Bone Inscriptions of Bronze Age China (1978).")
CIT_HAWKINS = ("Hawkins, J. D. Corpus of Hieroglyphic Luwian "
               "Inscriptions (2000).")
CIT_MELCHERT = ("Melchert, H. C. (ed.) The Luwians (2003).")
CIT_BONFANTE = ("Bonfante, G. and Bonfante, L. The Etruscan Language: "
                "An Introduction (2nd ed., 2002).")
CIT_RIX = ("Rix, H. Etruskische Texte (1991).")
CIT_GRIFFITH = ("Griffith, F. Ll. The Meroitic Inscriptions "
                "(Archaeological Survey of Egypt, 1911).")
CIT_RILLY = ("Rilly, C. La langue du royaume de Meroe (2007).")
CIT_ADIEGO = ("Adiego, I.-J. The Carian Language (2007).")
CIT_RAY = ("Ray, J. D. An outline of the Carian script (Kadmos, 1982).")
CIT_GOMEZMORENO = ("Gomez-Moreno, M. Sobre los iberos y su lengua "
                  "(Homenaje a Menendez Pidal, 1925).")
CIT_UNTERMANN = ("Untermann, J. Monumenta Linguarum Hispanicarum "
                 "(1975-1997).")
CIT_DESSET = ("Desset, F. et al. The decipherment of Linear Elamite "
              "writing (Zeitschrift fur Assyriologie, 2022).")
CIT_JUSTESON = ("Justeson, J. S. and Kaufman, T. A decipherment of "
                "Epi-Olmec hieroglyphic writing (Science, 1993).")
CIT_URCID = ("Urcid, J. Zapotec Hieroglyphic Writing (2001).")
CIT_KARA = ("Kara, G. Books of the Khitan small script (1987) - see "
            "Aisin-Gioro Ulhicun, Studies of the Khitan language and "
            "scripts (2009).")
CIT_NIE = ("Nie, H. - standard reference: Grinstead, E. Analysis of "
           "the Tangut Script (1972).")
CIT_GRINSTEAD = ("Grinstead, E. Analysis of the Tangut Script (1972).")
CIT_GORILA = ("Godart, L. and Olivier, J.-P. Recueil des inscriptions "
              "en Lineaire A (1976-1985).")
CIT_SCHOEP = ("Schoep, I. The Administration of Neopalatial Crete "
              "(2002).")
CIT_PARPOLA_INDUS = ("Parpola, A. Deciphering the Indus Script (1994).")
CIT_FARMER = ("Farmer, S., Sproat, R. and Witzel, M. The collapse of "
              "the Indus-script thesis (Electronic Journal of Vedic "
              "Studies, 2004).")
CIT_OLIVIER = ("Olivier, J.-P. Les ecritures cretoises - see Yule, P. "
               "Early Cretan Seals (1980).")
CIT_DAHL = ("Dahl, J. L. The Proto-Elamite writing system - see "
              "Dahl (ed.), Proto-Elamite Tablets (Cuneiform Digital "
              "Library, 2005).")
CIT_BARTEL = ("Barthel, T. Grundlagen zur Entzifferung der "
              "Osterinselschrift (1958).")
CIT_POZD = ("Pozdniakov, K. Les bases de l'ecriture de l'ile de "
            "Paques (Journal de la Societe des Oceanistes, 1996).")
CIT_Evans = ("Evans, A. Scripta Minoa I (1909).")
CIT_GODART_PH = ("Godart, L. The Phaistos Disc: The Enigma of an Aegean "
                 "Script (1995).")
CIT_DUNAND = ("Dunand, M. Byblia Grammata (1945).")
CIT_MASSON = ("Masson, E. Cyprominoica (1971).")
CIT_DALES = ("Dales, G. - Voynich: see D'Imperio, M. E. The Voynich "
             "Manuscript: An Elegant Enigma (1978).")
CIT_DIMPERIO = ("D'Imperio, M. E. The Voynich Manuscript: An Elegant "
                "Enigma (1978).")
CIT_VAV = ("Vavrou\u0161ek, P. - Rohonc: see N\u00e9meth, G. A "
           "Rohonci-k\u00f3dex (1990s cataloguing reports).")
CIT_NEMETH = ("Nemeth, G. Cataloguing reports on the Rohonc Codex "
              "(Hungarian Academy of Sciences, 1990s).")
CIT_WINN = ("Winn, S. M. M. Pre-Writing in Southeastern Europe: The "
            "Sign System of the Vinca Culture (1981).")
CIT_RODRIGUEZ = ("Rodriguez Martinez, C. et al. Oldest writing in the "
                 "New World (Science, 2006).")
CIT_GROTEFEND = ("Grotefend, G. F. Praevia de cuneatis quas vocant "
                 "inscriptionibus Persepolitanis legendis et explicandis "
                 "relatio (1802).")

SIG_TAIL = ("Signature completion note: this entry is a Signature-"
            "generated proposed reading - not established scholarship. "
            "It is filed as a Signature original interpretation of a "
            "legacy inscription; it claims no real decipherment and no "
            "scholarly acceptance.")

ENTRIES = [
    # ------------------------------------------------------------ FOUNDATIONS
    {
        "key": "rosetta-stone",
        "name": "The Rosetta Stone",
        "group": "Deciphered Scripts",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "script": "Egyptian hieroglyphic / Demotic / Ancient Greek",
        "status": "deciphered",
        "problem": ("Three scripts carry the same decree on one stone, but "
                    "for fourteen centuries no living person could read the "
                    "top two. The problem was to prove that the hieroglyphic "
                    "and Demotic texts say the same thing as the Greek - and "
                    "then to turn that proof into a working reading system "
                    "for all of ancient Egyptian writing."),
        "background": (
            "The stone was found in 1799 near Rashid (Rosetta) by troops of "
            "the French expedition to Egypt, and passed to the British under "
            "the Treaty of Alexandria in 1801. It carries a priestly decree "
            "of 196 BCE honoring Ptolemy V, written in three scripts: "
            "hieroglyphic for the gods, Demotic for daily administration, "
            "and Ancient Greek for the rulers. Thomas Young showed that the "
            "oval cartouches enclose royal names and that Demotic signs "
            "derive from hieroglyphs. Jean-Francois Champollion, building on "
            "Young and on the Philae obelisk bilingual, announced in his "
            "1822 Lettre a M. Dacier that hieroglyphs are partly phonetic. "
            "His reading of the cartouches of Ptolemy and Cleopatra proved "
            "that signs stand for sounds, unlocking the whole script. The "
            "stone now stands in the British Museum as the most famous "
            "decipherment key in history."),
        "why_it_matters": ("The Rosetta Stone is the template for every "
                           "decipherment since: a parallel text in a known "
                           "language anchors the unknown script. Its story "
                           "teaches the core solving move - find the proper "
                           "names first, because names travel across "
                           "languages almost unchanged."),
        "method": ("First, align the three texts and locate the cartouches, "
                   "the oval rings that mark royal names. Second, match the "
                   "Greek names Ptolemy and Cleopatra against the cartouche "
                   "sign sequences, assigning each sign a sound value from "
                   "the shared letters. Third, test those sound values on "
                   "other cartouches and on the Demotic middle text, where "
                   "Young had already mapped sign correspondences. Fourth, "
                   "extend the phonetic values into running text, checking "
                   "that grammar and sense emerge. Fifth, confirm against "
                   "independent bilinguals such as the Philae obelisk."),
        "readings": [
            "Cartouche reading: the oval rings enclose the royal names Ptolemaios and Kleopatra.",
            "Phonetic principle: hieroglyphic signs can stand for consonantal sounds, not only ideas.",
            "Demotic correspondence: the middle script is a cursive form of the same Egyptian language.",
        ],
        "translations": [
            "Decree opening: a decree of the priests assembled in synod at Memphis for King Ptolemy V.",
            "Closing formula: the decree shall be inscribed on stelae of hard stone in sacred, native, and Greek characters.",
        ],
        "sig_pointer": ("The Signature edition walks the Rosetta solving "
                        "path as a labeled Signature exercise: it re-derives "
                        "the cartouche alignment step by step, states its "
                        "assumptions openly, and never claims to improve on "
                        "Champollion - it is a proposed-reading workout on "
                        "solved material, clearly labeled throughout."),
        "assumptions": [
            "A1: The three texts are the same decree (documented on the stone itself).",
            "A2: Cartouches enclose royal names (Young's documented observation).",
            "A3: The Greek names Ptolemaios and Kleopatra correspond to two cartouches (bilingual anchor).",
            "A4: Shared letters between the two names pin shared sign values (documented method).",
        ],
        "steps": [
            "Isolate every cartouche in the hieroglyphic register and count their signs.",
            "Match the longer cartouche to Ptolemaios using the Greek text position.",
            "Match the shorter cartouche to Kleopatra from the Philae obelisk pairing.",
            "Assign sound values from letters shared between the two names.",
            "Test the values on a third cartouche and keep only values that repeat cleanly.",
            "Read the values back into the decree and verify that titles and grammar make sense.",
        ],
        "confirm": [
            "The same sign values recur in cartouches of other Ptolemaic rulers on temple walls across Egypt.",
            "Demotic sign sequences mapped by Young line up with the hieroglyphic values sign by sign.",
            "Later temple inscriptions read with these values yield coherent ritual and administrative sense.",
        ],
        "refute": [
            "If the cartouches did not contain royal names, the entire alignment chain would collapse at step one.",
            "If shared letters produced contradictory sign values, the phonetic hypothesis would fail immediately.",
            "If the values read nonsense on independent temple texts, the system would be a local accident only.",
        ],
        "not_claims": [
            "It does not claim Champollion's work was guesswork - it was proof.",
            "It does not claim the Signature re-derivation adds new readings.",
            "It does not claim hieroglyphs are purely alphabetic - most signs are not.",
        ],
        "citations": [CIT_PARKINSON, CIT_CHAMPOLLION, CIT_ROBINSON],
        "demo_sample": "PTOLEMAIOS-CARTOUCHE-PTOLEMAIOS-DECREE-PTOLEMAIOS",
        "demo_anchor": "PTOLEMAIOS",
    },
    {
        "key": "egyptian-hieroglyphs",
        "name": "Egyptian Hieroglyphs",
        "group": "Deciphered Scripts",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "script": "Egyptian hieroglyphic",
        "status": "deciphered",
        "problem": ("Seven hundred picture-signs that can be read as words, "
                    "as sounds, or as silent classifiers - sometimes all "
                    "three in one line. The problem was to learn the "
                    "operating system of the script: which signs speak, "
                    "which signs mean, and which signs silently tell you "
                    "what kind of word you just read."),
        "background": (
            "Egyptian hieroglyphs were used for nearly 3,500 years, from "
            "around 3200 BCE to the fourth century CE. The script mixes "
            "logograms (a sign standing for a whole word), phonograms "
            "(signs standing for one, two, or three consonants), and "
            "determinatives (silent signs that classify the word, such as "
            "a seated man for male names). Gardiner's sign list catalogs "
            "the classic repertoire in families from A (man) to Z (strokes "
            "and figures). Egyptian writing records consonants only, so "
            "vowels must be supplied by the reader's knowledge of the "
            "language. Signs can face left or right, and are read toward "
            "the direction the figures face. After Champollion's 1822 "
            "breakthrough, a century of dictionary work turned the script "
            "into a fully readable scholarly language."),
        "why_it_matters": ("Hieroglyphs are the proof that a mixed "
                           "word-and-sound system can be cracked by the "
                           "cartouche method, and they remain the training "
                           "ground for every epigrapher: learn the sign "
                           "functions here and you can attack any logo-"
                           "syllabic script on Earth."),
        "method": ("First, memorize Gardiner's sign families so any sign "
                   "can be looked up by shape. Second, separate phonograms "
                   "from determinatives by testing whether a sign's value "
                   "changes the spoken word. Third, use uniliteral signs "
                   "as an alphabet scaffold and biliterals and triliterals "
                   "as shorthand confirmed by phonetic complements. Fourth, "
                   "read determinatives as classifiers that disambiguate "
                   "homophones. Fifth, check every reading against Coptic, "
                   "the descendant language that preserves the vowels "
                   "hieroglyphs omit."),
        "readings": [
            "Uniliteral owl (G17) reads 'm'; water ripple (N35) reads 'n'.",
            "The ankh sign is both the word for 'life' and the triliteral consonant cluster.",
            "Determinatives are silent: the seated-man sign classifies but is not pronounced.",
        ],
        "translations": [
            "Pyramid Texts opening: words spoken by the king ascending to the sky.",
            "Book of the Dead spell 125: the negative confession before the tribunal of Osiris.",
        ],
        "sig_pointer": ("The Signature edition treats the hieroglyphic "
                        "system as a labeled solving exercise: it re-derives "
                        "sign-function classification on documented signs, "
                        "states assumptions openly, and claims no new "
                        "readings - a proposed-reading workout on solved "
                        "material only."),
        "assumptions": [
            "A1: Gardiner's sign list values are the documented standard (published reference).",
            "A2: Determinatives are silent classifiers (documented grammar).",
            "A3: Coptic preserves vowels lost in hieroglyphic spelling (documented linguistics).",
            "A4: Signs face the start of the line (documented reading convention).",
        ],
        "steps": [
            "Catalog each sign in the sample line by Gardiner family.",
            "Mark candidate phonograms by checking for phonetic complements.",
            "Mark silent determinatives by testing whether removing them changes pronunciation.",
            "Assemble the consonantal skeleton from uniliteral, biliteral, and triliteral values.",
            "Supply vowels from Coptic cognates and check the word against the dictionary.",
            "Verify the full line yields grammatical Egyptian with the determinatives classifying correctly.",
        ],
        "confirm": [
            "Dictionary checks confirm the assembled words exist with the expected meanings in Middle Egyptian.",
            "Coptic cognates supply vowels that fit the consonantal skeletons without forcing.",
            "Parallel texts in hieratic and Demotic give the same readings through independent sign forms.",
        ],
        "refute": [
            "If Coptic cognates systematically contradicted the readings, the vowel supply would be exposed as invention.",
            "If determinatives turned out to be pronounced, whole lines of grammar would have to be re-parsed.",
            "If Gardiner values failed on newly found temple texts, the standard list would need revision.",
        ],
        "not_claims": [
            "It does not claim every rare sign is fully understood - some remain uncertain.",
            "It does not claim the re-derivation improves on a century of dictionary work.",
            "It does not claim hieroglyphs record vowels - they do not.",
        ],
        "citations": [CIT_GARDINER, CIT_ALLEN, CIT_ROBINSON],
        "demo_sample": "N5-D36-N35-R4-Q3-D21-D36-N5-R4",
        "demo_anchor": "D36",
    },
    {
        "key": "demotic-script",
        "name": "The Demotic Script",
        "group": "Deciphered Scripts",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "script": "Egyptian Demotic",
        "status": "deciphered",
        "problem": ("The middle text of the Rosetta Stone is a flowing "
                    "cursive that looks nothing like hieroglyphs, yet it "
                    "writes the same language. The problem was to prove the "
                    "cursive signs are the same signs in rapid handwriting - "
                    "and to build a reading system for the everyday "
                    "documents of late Egypt."),
        "background": (
            "Demotic developed from hieratic around 650 BCE and became the "
            "everyday administrative and literary script of Egypt through "
            "the Ptolemaic and Roman periods. Its signs are highly "
            "ligatured cursive forms in which individual hieroglyphs are "
            "barely recognizable. Thomas Young was the first to map Demotic "
            "signs to their hieroglyphic parents, working sign by sign "
            "through the Rosetta middle text. Heinrich Brugsch later built "
            "the first Demotic grammar and dictionary in the 1850s and "
            "1860s. Demotic documents include contracts, tax receipts, "
            "marriage settlements, and literary tales, giving a ground-"
            "level view of Egyptian life. The script fell out of use in "
            "the fifth century CE as Greek and then Coptic took over."),
        "why_it_matters": ("Demotic proves that the same language can hide "
                           "behind a completely different-looking script, "
                           "and its decipherment taught scholars to trace "
                           "cursive forms back to their monumental parents - "
                           "a move reused for hieratic, Meroitic cursive, "
                           "and palm-leaf scripts."),
        "method": ("First, take the Rosetta Greek text as the sense anchor "
                   "for each Demotic line. Second, isolate repeated sign "
                   "groups and match them to known hieroglyphic words such "
                   "as the royal names. Third, trace each cursive Demotic "
                   "sign back to its hieroglyphic parent through "
                   "intermediate hieratic forms. Fourth, build a sign list "
                   "with the derivation drawn for every entry, so each "
                   "value is checkable. Fifth, test the list on dated "
                   "legal papyri where the sense is constrained by "
                   "formulaic contracts."),
        "readings": [
            "Demotic royal-name groups match the hieroglyphic cartouches sign for sign.",
            "Ligatured verb forms resolve into hieratic ancestors once the pen strokes are traced.",
            "Dated contracts read with the sign list give consistent dates, names, and sums.",
        ],
        "translations": [
            "Marriage settlement formula: the standard silver and grain clauses of Ptolemaic contracts.",
            "Tax receipt ostraca: regnal-year dates with amounts paid in kind.",
        ],
        "sig_pointer": ("The Signature edition re-derives the cursive-to-"
                        "monumental tracing as a labeled exercise, stating "
                        "assumptions openly and claiming no new readings - "
                        "a proposed-reading workout on solved material."),
        "assumptions": [
            "A1: The Rosetta Demotic text matches the Greek decree (documented trilingual).",
            "A2: Demotic signs derive from hieroglyphs via hieratic (documented paleography).",
            "A3: Royal-name groups are the fixed anchor points (documented method).",
            "A4: Formulaic contracts constrain the sense of test documents (documented genre).",
        ],
        "steps": [
            "Align each Demotic line with its Greek decree section.",
            "Isolate the repeated groups that match the cartouche names.",
            "Trace each Demotic sign to its hieroglyphic parent via hieratic intermediates.",
            "Record every derivation in a checkable sign list.",
            "Read a dated contract with the list and verify names, dates, and sums cohere.",
            "Cross-check the reading against a second contract of the same formula.",
        ],
        "confirm": [
            "Hundreds of dated contracts read with the sign list give internally consistent dates and amounts.",
            "Literary papyri read with the same values yield coherent continuous narrative.",
            "Bilingual Greek-Demotic mummy labels confirm personal names in both scripts.",
        ],
        "refute": [
            "If contract dates came out scrambled, the sign values would be exposed as wrong.",
            "If the cursive derivations skipped hieratic intermediates, the parentage would be unproven.",
            "If literary texts read as gibberish, the list would only cover formulaic documents.",
        ],
        "not_claims": [
            "It does not claim every Demotic ligature is securely read - some remain debated.",
            "It does not claim the re-derivation adds to Brugsch's grammar.",
            "It does not claim Demotic is a different language - it is Egyptian in cursive dress.",
        ],
        "citations": [CIT_PARKINSON, CIT_ROBINSON, CIT_ALLEN],
        "demo_sample": "DEMOTIC-PAPYRUS-DEMOTIC-DECREE-SCRIBE-DEMOTIC",
        "demo_anchor": "DEMOTIC",
    },
    {
        "key": "linear-b",
        "name": "Linear B",
        "group": "Deciphered Scripts",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "script": "Linear B syllabary",
        "status": "deciphered",
        "problem": ("Clay tablets from Bronze Age palaces, written in a "
                    "syllabary of 87 signs that no one could read. The "
                    "problem was to crack a syllabic script with no "
                    "bilingual, no known language, and no vowels written - "
                    "using only the internal patterns of the tablets "
                    "themselves."),
        "background": (
            "Linear B tablets were found at Knossos by Arthur Evans and at "
            "Pylos by Carl Blegen, recording the palace economies of "
            "Mycenaean Greece around 1400 to 1200 BCE. Alice Kober laid the "
            "groundwork by proving the script is inflected - word endings "
            "change in patterns that mark an inflected language - and by "
            "building grids of signs that share consonants or vowels. "
            "Architect Michael Ventris took up Kober's grids and, in 1952, "
            "tested the hypothesis that the language was Greek. Place names "
            "on Cretan tablets matched known Cretan towns, and the "
            "inflections fell into Greek patterns. Working with linguist "
            "John Chadwick, Ventris published the decipherment that year. "
            "The tablets turned out to be palace inventories: tripods, "
            "chariots, grain, livestock, and personnel lists."),
        "why_it_matters": ("Linear B is the only great decipherment done "
                           "with no bilingual at all - pure internal "
                           "analysis. It proved that inflection patterns "
                           "and place names can substitute for a Rosetta "
                           "Stone, and it pushed written Greek back seven "
                           "centuries."),
        "method": ("First, build Kober's grids: sort signs by shared "
                   "consonant and vowel behavior from word-ending patterns. "
                   "Second, identify place names by matching sign sequences "
                   "to known Cretan towns on tablets from Knossos. Third, "
                   "test the Greek hypothesis by reading the inflections "
                   "as Greek case endings. Fourth, check vocabulary against "
                   "known Greek roots, such as ti-ri-po-de for tripod. "
                   "Fifth, verify that whole tablets read as coherent "
                   "palace inventories with sensible quantities."),
        "readings": [
            "ti-ri-po-de reads as Greek tripodes, tripods - the vocabulary anchor.",
            "Place-name sequences match Cretan towns, fixing a dozen sign values at once.",
            "Inflection triplets follow Greek case patterns, confirming the language.",
        ],
        "translations": [
            "Pylos Ta 641: inventory of tripods with condition notes, some marked as burnt or missing legs.",
            "Personnel lists: workgroups of women and children with grain ration quantities.",
        ],
        "sig_pointer": ("The Signature edition re-derives the grid method "
                        "as a labeled exercise on solved material: it "
                        "rebuilds the inflection reasoning step by step, "
                        "states assumptions openly, and claims no new "
                        "readings of the tablets."),
        "assumptions": [
            "A1: Word-ending changes mark inflection (Kober's documented proof).",
            "A2: Knossos tablets mention Cretan place names (documented geography).",
            "A3: The underlying language may be Greek (Ventris's tested hypothesis).",
            "A4: Ideograms beside the text label the commodity (documented tablet layout).",
        ],
        "steps": [
            "Grid the signs by shared consonant and vowel behavior from endings.",
            "Isolate place-name candidates on Knossos tablets and match to Cretan towns.",
            "Assign syllable values from the town-name matches.",
            "Read the inflections as Greek case endings and test for fit.",
            "Check vocabulary hits such as ti-ri-po-de against Greek roots.",
            "Read full tablets as inventories and verify quantities make sense.",
        ],
        "confirm": [
            "New tablets found after 1952, including at Thebes, read cleanly with the same sign values.",
            "The vocabulary keeps matching Greek roots across hundreds of tablets without forcing.",
            "Ideogram-plus-text pairs consistently agree: the tripod sign sits beside ti-ri-po-de entries.",
        ],
        "refute": [
            "If the language were not Greek, the inflection patterns would have collapsed on contact with Greek endings.",
            "If place names were misidentified, the sign values would fail on tablets from other palaces.",
            "If ideograms contradicted the text, the readings would be exposed as coincidence.",
        ],
        "not_claims": [
            "It does not claim Ventris worked alone - Kober's grids were the foundation.",
            "It does not claim every tablet is fully understood - some remain fragmentary.",
            "It does not claim the re-derivation changes any accepted reading.",
        ],
        "citations": [CIT_VENTRIS, CIT_CHADWICK, CIT_ROBINSON],
        "demo_sample": "ti-ri-po-de-ko-wo-a2-qe-ti-ja-ro",
        "demo_anchor": "ti-ri-po-de",
    },
    {
        "key": "behistun-inscription",
        "name": "The Behistun Inscription",
        "group": "Deciphered Scripts",
        "ladder_rank": 5,
        "ladder_tier": "foundations",
        "script": "Old Persian / Elamite / Babylonian cuneiform",
        "status": "deciphered",
        "problem": ("A royal proclamation carved 100 meters up a cliff face "
                    "in three cuneiform languages, in a script no European "
                    "had ever read. The problem was to copy it at all - "
                    "then to turn the trilingual text into the key that "
                    "unlocked all of Mesopotamian writing."),
        "background": (
            "Darius I had his autobiography carved around 520 BCE on the "
            "Behistun cliff in western Iran, in Old Persian, Elamite, and "
            "Babylonian versions. Henry Rawlinson, a British officer, "
            "climbed the cliff in 1835 and over several seasons copied the "
            "Old Persian text at great personal risk. The inscription "
            "opens with a genealogy of kings, giving repeated royal names "
            "and titles. Rawlinson used the names to assign sound values, "
            "much as Champollion had used cartouches. His 1846 paper "
            "presented the Old Persian alphabet and a translation. Once "
            "Old Persian was readable, scholars worked through the Elamite "
            "and Babylonian versions, and from Babylonian into the whole "
            "Akkadian cuneiform world. The cliff text remains the founding "
            "document of Assyriology."),
        "why_it_matters": ("Behistun is the Rosetta Stone of cuneiform: the "
                           "trilingual that made Mesopotamia readable. It "
                           "teaches the royal-genealogy attack - repeated "
                           "king lists are nature's bilinguals - and it "
                           "reminds solvers that sometimes the hardest part "
                           "is copying the text."),
        "method": ("First, copy the inscription accurately, sign by sign, "
                   "from the cliff face. Second, isolate the repeated royal "
                   "names and titles in the genealogy opening. Third, match "
                   "the names to kings known from Greek historians, "
                   "assigning sound values to the simple Old Persian "
                   "signs. Fourth, extend the values through the whole Old "
                   "Persian text and translate it fully. Fifth, use the "
                   "Old Persian sense as the anchor to attack the Elamite "
                   "and Babylonian versions line by line."),
        "readings": [
            "The opening genealogy yields the names Darius, Hystaspes, and Arsames in sequence.",
            "Old Persian sign values derived from the names read the entire first column cleanly.",
            "The trilingual alignment lets each Babylonian line be checked against Old Persian sense.",
        ],
        "translations": [
            "Opening: I am Darius, the great king, king of kings, king of countries.",
            "The Lie section: the account of the rebel kings and how each was defeated.",
        ],
        "sig_pointer": ("The Signature edition re-derives the genealogy "
                        "attack as a labeled exercise: it rebuilds the "
                        "name-to-value reasoning step by step, states "
                        "assumptions openly, and claims no new readings of "
                        "the cliff text."),
        "assumptions": [
            "A1: The genealogy names kings in order (documented inscription structure).",
            "A2: Greek historians preserve the same royal names (documented cross-source).",
            "A3: Old Persian signs are largely alphabetic (Rawlinson's documented finding).",
            "A4: The three versions carry the same proclamation (documented trilingual).",
        ],
        "steps": [
            "Transcribe the Old Persian column sign by sign from the cliff copy.",
            "Isolate the repeated name-and-title formulas of the genealogy.",
            "Match the names to Darius, Hystaspes, and Arsames from Greek sources.",
            "Assign sound values to each sign from the name spellings.",
            "Read the full Old Persian text with the values and translate it.",
            "Carry the established sense into the Elamite and Babylonian versions.",
        ],
        "confirm": [
            "The Old Persian values read every other Achaemenid inscription consistently.",
            "Elamite and Babylonian versions, once unlocked, agree in sense with the Old Persian.",
            "Later-discovered trilinguals at Persepolis confirm the same sign values independently.",
        ],
        "refute": [
            "If the genealogy names were misidentified, every derived sign value would be wrong.",
            "If the three versions diverged in content, the cross-checking method would fail.",
            "If Old Persian values produced gibberish on new inscriptions, the alphabet would be exposed.",
        ],
        "not_claims": [
            "It does not claim Rawlinson worked from comfort - the copying was done on the cliff face.",
            "It does not claim the re-derivation adds readings to the established corpus.",
            "It does not claim Elamite was easy - it remained difficult long after Old Persian fell.",
        ],
        "citations": [CIT_RAWLINSON, CIT_SCHMITT, CIT_ROBINSON],
        "demo_sample": "ADAM-DARAYAVAUS-XSAYATHIYA-ADAM",
        "demo_anchor": "DARAYAVAUS",
    },
    {
        "key": "cuneiform-akkadian",
        "name": "Cuneiform - the Wedge System",
        "group": "Deciphered Scripts",
        "ladder_rank": 6,
        "ladder_tier": "foundations",
        "script": "Sumerian / Akkadian cuneiform",
        "status": "deciphered",
        "problem": ("The world's first writing system: thousands of wedge "
                    "marks pressed into clay, mixing word-signs and "
                    "syllable-signs across two unrelated languages over "
                    "three thousand years. The problem was to map a "
                    "sprawling, evolving sign inventory onto readable "
                    "Akkadian and Sumerian."),
        "background": (
            "Cuneiform began around 3400 BCE in Sumer as pictographic "
            "tokens pressed into clay, and simplified over centuries into "
            "abstract wedge combinations. The Akkadians adopted the script "
            "for their Semitic language, keeping Sumerian word-signs as "
            "logograms alongside a growing syllabary. A single sign can "
            "have a dozen values depending on context - the classic "
            "polyvalent sign. After Rawlinson's Behistun work opened Old "
            "Persian, scholars such as Hincks and Oppert extended the "
            "method to Babylonian, proving the syllabic values. The great "
            "libraries of Nineveh, excavated in the 1850s, supplied the "
            "bilingual and lexical texts - ancient dictionaries - that "
            "turned decipherment into a science. Today hundreds of "
            "thousands of tablets are readable, from epics to receipts."),
        "why_it_matters": ("Cuneiform is writing's ground zero: every "
                           "later script inherits its lessons. Its "
                           "decipherment taught scholars to handle "
                           "polyvalent signs, to use ancient dictionaries, "
                           "and to separate the Sumerian substrate from the "
                           "Akkadian superstructure."),
        "method": ("First, use the Behistun Babylonian values as the seed "
                   "syllabary. Second, exploit the ancient lexical lists - "
                   "Sumerian-Akkadian dictionaries the scribes themselves "
                   "wrote. Third, resolve polyvalent signs by context: "
                   "phonetic complements and determinatives pick the "
                   "intended value. Fourth, separate Sumerian logograms "
                   "from Akkadian syllabic spellings by testing both "
                   "readings. Fifth, confirm on dated royal inscriptions "
                   "where the historical context constrains the sense."),
        "readings": [
            "The dingir sign marks divinity and reads as the word for god in logographic use.",
            "Phonetic complements disambiguate: a syllabic sign beside a logogram fixes its reading.",
            "Lexical lists give the ancient scribes' own sign values, the ultimate authority.",
        ],
        "translations": [
            "Hammurabi's prologue: the king called by the gods to establish justice in the land.",
            "Gilgamesh opening: he who saw the deep, the foundation of the land.",
        ],
        "sig_pointer": ("The Signature edition re-derives polyvalent-sign "
                        "resolution as a labeled exercise on solved "
                        "material, stating assumptions openly and claiming "
                        "no new tablet readings."),
        "assumptions": [
            "A1: Behistun Babylonian values seed the syllabary (documented decipherment).",
            "A2: Lexical lists are the scribes' own dictionaries (documented genre).",
            "A3: Determinatives classify without being read (documented convention).",
            "A4: Royal inscriptions have historically constrained sense (documented context).",
        ],
        "steps": [
            "Seed the syllabary from the Behistun Babylonian sign values.",
            "Look up unknown signs in the ancient lexical lists first.",
            "List every value of each polyvalent sign in the sample line.",
            "Use phonetic complements and determinatives to select the intended value.",
            "Test Sumerian logographic against Akkadian syllabic readings for fit.",
            "Verify the line against a dated royal inscription for historical sense.",
        ],
        "confirm": [
            "Lexical-list values keep producing coherent readings across hundreds of thousands of tablets.",
            "Bilingual Sumerian-Akkadian texts confirm the logogram-to-translation mappings.",
            "Dated royal inscriptions read with these values match known historical events.",
        ],
        "refute": [
            "If the lexical lists were school exercises rather than standards, their authority would weaken.",
            "If polyvalent resolution were arbitrary, parallel passages would diverge in sense.",
            "If royal inscriptions contradicted known history, the sign values would be suspect.",
        ],
        "not_claims": [
            "It does not claim every rare sign value is settled - new values still emerge.",
            "It does not claim Sumerian is fully understood - its grammar still puzzles scholars.",
            "It does not claim the re-derivation revises any accepted reading.",
        ],
        "citations": [CIT_WALKER, CIT_ROUX, CIT_ROBINSON],
        "demo_sample": "LUGAL-KUR-KI-DINGIR-LUGAL",
        "demo_anchor": "LUGAL",
    },
    {
        "key": "old-persian-cuneiform",
        "name": "Old Persian Cuneiform",
        "group": "Deciphered Scripts",
        "ladder_rank": 7,
        "ladder_tier": "foundations",
        "script": "Old Persian cuneiform",
        "status": "deciphered",
        "problem": ("A 36-sign wedge script on the ruins of Persepolis, "
                    "with no bilingual and no known language. The problem "
                    "was to guess the language from the shape of the "
                    "inscriptions alone - and to prove the guess by reading "
                    "royal names nobody had seen in 2,000 years."),
        "background": (
            "Georg Friedrich Grotefend, a German schoolteacher, attacked "
            "the Persepolis inscriptions in 1802 with pure reasoning. He "
            "noticed two inscriptions with parallel structure: where one "
            "had a short royal formula, the other had a longer one, "
            "suggesting father and son. Knowing from Greek sources that "
            "Darius was followed by Xerxes, he matched the names to the "
            "sign groups and derived a dozen sign values. His guesses "
            "about the language - an ancestor of Persian - proved right. "
            "Rawlinson later confirmed and extended the alphabet at "
            "Behistun. Old Persian cuneiform turned out to be a "
            "semi-alphabetic system of 36 signs, far simpler than "
            "Babylonian, invented for royal display rather than daily "
            "administration."),
        "why_it_matters": ("Grotefend's 1802 paper is the purest "
                           "armchair decipherment ever: no bilingual, no "
                           "travel, just structural logic. It teaches the "
                           "genealogy-comparison move that later cracked "
                           "Behistun and every royal inscription since."),
        "method": ("First, find two inscriptions with parallel royal "
                   "formulas of different length. Second, hypothesize the "
                   "shorter names the father and the longer names the son. "
                   "Third, match the pairs to Darius and Xerxes from Greek "
                   "histories. Fourth, derive sign values from the name "
                   "spellings, using the repeated word for king as a "
                   "cross-check. Fifth, read the remaining text and verify "
                   "that titles and genealogy make historical sense."),
        "readings": [
            "The repeated formula reads xshayathiya, king - the anchor word.",
            "Darius and Xerxes emerge from the two parallel genealogies.",
            "The 36 signs resolve into a semi-alphabet with vowel marks.",
        ],
        "translations": [
            "Persepolis foundation formula: Darius the great king, king of kings, son of Hystaspes.",
            "Xerxes inscription: Xerxes the great king, son of Darius the king.",
        ],
        "sig_pointer": ("The Signature edition re-derives Grotefend's "
                        "parallel-genealogy reasoning as a labeled "
                        "exercise, stating assumptions openly and claiming "
                        "no new readings."),
        "assumptions": [
            "A1: Parallel inscriptions carry parallel royal formulas (documented structure).",
            "A2: Greek histories preserve the Achaemenid king order (documented cross-source).",
            "A3: The shorter formula names the father of the longer (Grotefend's documented hypothesis).",
            "A4: The repeated word is the title king (documented anchor).",
        ],
        "steps": [
            "Lay the two Persepolis inscriptions side by side and align their formulas.",
            "Identify the father-son name pair from the formula length difference.",
            "Match the names to Darius and Xerxes from Greek king lists.",
            "Derive sign values from the two name spellings.",
            "Cross-check the values on the repeated king formula.",
            "Read the full inscriptions and verify the genealogy makes historical sense.",
        ],
        "confirm": [
            "Rawlinson's Behistun work confirmed Grotefend's values on independent text.",
            "The full Achaemenid corpus reads consistently with the 36-sign alphabet.",
            "The language proved to be Old Iranian, exactly as Grotefend hypothesized.",
        ],
        "refute": [
            "If the father-son pairing were reversed, the derived names would be gibberish.",
            "If Greek king lists were wrong about the succession, the anchor would fail.",
            "If the king formula did not repeat, the cross-check would be impossible.",
        ],
        "not_claims": [
            "It does not claim Grotefend read everything - Rawlinson completed the alphabet.",
            "It does not claim the method works without a known king list - it needs one.",
            "It does not claim the re-derivation changes any accepted value.",
        ],
        "citations": [CIT_GROTEFEND, CIT_RAWLINSON, CIT_ROBINSON],
        "demo_sample": "DA-A-RA-YA-VA-U-SA-XSA-YA-THI-YA",
        "demo_anchor": "DA-A-RA-YA-VA-U-SA",
    },
    {
        "key": "hittite-cuneiform",
        "name": "Hittite Cuneiform",
        "group": "Deciphered Scripts",
        "ladder_rank": 8,
        "ladder_tier": "foundations",
        "script": "Hittite cuneiform",
        "status": "deciphered",
        "problem": ("Thousands of clay tablets from a forgotten empire, "
                    "written in familiar cuneiform signs but in a language "
                    "no one recognized. The problem was to realize the "
                    "signs were a mask: the language underneath belonged "
                    "to a family nobody expected in Bronze Age Anatolia."),
        "background": (
            "The Hittite capital Hattusa, excavated from 1906, yielded some "
            "10,000 tablets in cuneiform script. The signs were readable "
            "as Akkadian syllables, but the words made no sense in "
            "Akkadian. Bedrich Hrozny announced the solution in 1915: in a "
            "ritual text he read a sentence containing the words for bread "
            "and water, and recognized wa-a-tar as the Indo-European word "
            "for water, cognate with English water and German Wasser. The "
            "language was Indo-European - the oldest attested member of "
            "the family, ancestral to no living tongue but cousin to them "
            "all. Hittite texts include treaties, laws, rituals, and the "
            "famous diplomatic correspondence of the Late Bronze Age."),
        "why_it_matters": ("Hittite is the proof that a familiar script "
                           "can hide an unfamiliar language, and its "
                           "decipherment pushed Indo-European back a "
                           "millennium. The water sentence is the most "
                           "famous single line in decipherment history."),
        "method": ("First, read the cuneiform signs with their known "
                   "Akkadian syllabic values. Second, scan the resulting "
                   "nonsense for recognizable words, especially in "
                   "formulaic ritual contexts. Third, test the "
                   "Indo-European hypothesis by matching vocabulary "
                   "against known roots. Fourth, verify the grammar: "
                   "Hittite inflections must pattern as Indo-European. "
                   "Fifth, confirm on independent genres - laws, treaties, "
                   "letters - that the same values keep working."),
        "readings": [
            "wa-a-tar reads as water, the Indo-European anchor word.",
            "NINDA marks bread in ritual contexts, confirming the food formula.",
            "Verb endings pattern as Indo-European conjugations.",
        ],
        "translations": [
            "The bread-and-water sentence: bread thou shalt eat, water thou shalt drink.",
            "Treaty prologue: the standard Hittite vassal-treaty historical introduction.",
        ],
        "sig_pointer": ("The Signature edition re-derives the "
                        "cognate-spotting method as a labeled exercise on "
                        "solved material, stating assumptions openly and "
                        "claiming no new readings of the tablets."),
        "assumptions": [
            "A1: Cuneiform signs carry their Akkadian syllabic values (documented script).",
            "A2: Ritual texts use formulaic, guessable contexts (documented genre).",
            "A3: wa-a-tar may be Indo-European water (Hrozny's documented hypothesis).",
            "A4: Grammar must pattern with the vocabulary claim (documented test).",
        ],
        "steps": [
            "Transliterate the tablets with standard Akkadian sign values.",
            "Scan ritual passages for contextually guessable words.",
            "Isolate wa-a-tar and test it against Indo-European water cognates.",
            "Check surrounding verb forms for Indo-European inflection patterns.",
            "Extend the vocabulary test across laws, treaties, and letters.",
            "Verify that whole texts now read as coherent administration and ritual.",
        ],
        "confirm": [
            "Hundreds of cognates with known Indo-European roots accumulated after the breakthrough.",
            "The grammar proved systematically Indo-European, not just the vocabulary.",
            "New tablets from Hattusa continue to read with the same values.",
        ],
        "refute": [
            "If wa-a-tar were a loanword, the single-word proof would collapse.",
            "If the grammar had patterned as non-Indo-European, the hypothesis would fail.",
            "If new genres resisted the values, the decipherment would be genre-bound.",
        ],
        "not_claims": [
            "It does not claim one word proved the case - the grammar proof followed.",
            "It does not claim Hittite is fully transparent - rare words remain obscure.",
            "It does not claim the re-derivation revises any accepted reading.",
        ],
        "citations": [CIT_HROZNY, CIT_BRYCE, CIT_ROBINSON],
        "demo_sample": "WA-A-TAR-NINDA-AN-E-ED-ZA-TE-NI-WA-A-TAR",
        "demo_anchor": "WA-A-TAR",
    },
    {
        "key": "mayan-glyphs",
        "name": "Mayan Glyphs",
        "group": "Deciphered Scripts",
        "ladder_rank": 9,
        "ladder_tier": "foundations",
        "script": "Maya hieroglyphic",
        "status": "deciphered",
        "problem": ("A beautiful baroque script of faces, animals, and "
                    "abstract signs carved on every Maya monument - and for "
                    "a century the leading scholar insisted it could not be "
                    "read phonetically. The problem was to prove the "
                    "glyphs record a real spoken language, syllable by "
                    "syllable."),
        "background": (
            "Maya writing was used from about 300 BCE to the Spanish "
            "conquest, carved on stelae, painted on pottery, and written "
            "in bark-paper codices. Bishop de Landa's 16th-century "
            "'alphabet', recorded from Maya informants, was dismissed for "
            "centuries because it did not behave like an alphabet. Yuri "
            "Knorosov showed in 1952 that de Landa's signs are a "
            "syllabary: each sign stands for a consonant-vowel pair, and "
            "scribes spelled words by combining syllables, often dropping "
            "weak vowels. Tatiana Proskouriakoff then proved the "
            "monuments record real dynastic history by patterning dates "
            "with births, accessions, and deaths. Heinrich Berlin "
            "identified the emblem glyphs as city titles. Together these "
            "breakthroughs turned picture-writing into readable Classic "
            "Maya, a Mayan language, and today roughly nine in ten glyphs "
            "can be read."),
        "why_it_matters": ("Maya is the New World's great decipherment and "
                           "the proof that a so-called picture script can "
                           "be fully phonetic underneath. It teaches the "
                           "syllabary insight: when an 'alphabet' will not "
                           "behave, try syllables."),
        "method": ("First, treat de Landa's signs as a syllabary, not an "
                   "alphabet, following Knorosov. Second, use the day signs "
                   "of the calendar, whose names are known from colonial "
                   "sources, as phonetic anchors. Third, apply "
                   "Proskouriakoff's date-pattern method to extract the "
                   "verbs of birth, accession, and death from dated "
                   "monuments. Fourth, read emblem glyphs as city titles "
                   "anchored to known archaeological sites. Fifth, verify "
                   "the growing syllabary on pottery texts, where captions "
                   "describe the painted scenes."),
        "readings": [
            "De Landa's 'alphabet' resolves into consonant-vowel syllables.",
            "The accession verb chum anchors dynastic sequences on dated stelae.",
            "Emblem glyphs name the cities whose monuments carry them.",
        ],
        "translations": [
            "Accession formula: he was seated as king on the recorded calendar date.",
            "Dresden Codex eclipse tables: the tabulated lunar and eclipse cycles with ritual notes.",
        ],
        "sig_pointer": ("The Signature edition re-derives the syllabary "
                        "insight as a labeled exercise on solved material, "
                        "stating assumptions openly and claiming no new "
                        "readings of the monuments."),
        "assumptions": [
            "A1: De Landa's signs record a syllabary (Knorosov's documented proof).",
            "A2: Calendar day names are known from colonial sources (documented anchor).",
            "A3: Dated monuments record dynastic events (Proskouriakoff's documented method).",
            "A4: The language is Mayan, related to modern Mayan tongues (documented linguistics).",
        ],
        "steps": [
            "Reinterpret each de Landa sign as a consonant-vowel syllable.",
            "Anchor syllable values on the known calendar day names.",
            "Extract event verbs from dated monuments by date-pattern analysis.",
            "Assign emblem glyphs to their archaeological cities.",
            "Test the syllabary on pottery captions against the painted scenes.",
            "Verify that full monument texts read as coherent dynastic narrative.",
        ],
        "confirm": [
            "Pottery captions describe exactly what the paintings show, confirming the readings.",
            "Newly found monuments read with the same syllabary without adjustment.",
            "Spoken Mayan languages supply the vocabulary the glyphs spell.",
        ],
        "refute": [
            "If de Landa's informants had invented the signs, the syllabary would fail on ancient texts.",
            "If monuments did not record history, Proskouriakoff's date patterns would be coincidence.",
            "If pottery captions mismatched their scenes, the phonetic values would be exposed.",
        ],
        "not_claims": [
            "It does not claim every glyph is read - about one in ten remains uncertain.",
            "It does not credit one scholar - Knorosov, Proskouriakoff, and Berlin each broke part.",
            "It does not claim the re-derivation adds readings to the corpus.",
        ],
        "citations": [CIT_KNOROSOV, CIT_COE, CIT_STUART],
        "demo_sample": "AJAW-CHAN-AJAW-KIN-AJAW-CHAN",
        "demo_anchor": "AJAW",
    },
    {
        "key": "brahmi-script",
        "name": "Brahmi Script",
        "group": "Deciphered Scripts",
        "ladder_rank": 10,
        "ladder_tier": "foundations",
        "script": "Brahmi",
        "status": "deciphered",
        "problem": ("Pillars and rocks across India carry edicts in an "
                    "unknown script of elegant geometric signs. The problem "
                    "was to find whose voice speaks from the stones - and "
                    "then to read the earliest decipherable Indian "
                    "inscriptions ever found."),
        "background": (
            "The edicts of the Mauryan emperor Ashoka, carved around 250 "
            "BCE on pillars and rock faces from Afghanistan to southern "
            "India, are written in Brahmi and Kharosthi scripts. James "
            "Prinsep, assay-master of the Calcutta mint, attacked the "
            "short dedicatory inscriptions on the pillar capitals in the "
            "1830s. Noticing that the brief texts repeated the same "
            "formula, he isolated the royal title and, with help from "
            "Ceylonese chronicles supplied by George Turnour, identified "
            "Devanampiya Piyadasi - Beloved of the Gods - as Ashoka "
            "himself. The 1837 reading of the edicts opened early Indian "
            "epigraphy. Brahmi proved to be an alphasyllabary: each "
            "consonant carries an inherent vowel, modified by diacritic "
            "marks, the ancestor of nearly every script of South and "
            "Southeast Asia."),
        "why_it_matters": ("Brahmi's decipherment recovered the voice of "
                           "India's first great emperor and the mother "
                           "script of a continent. It teaches the formula "
                           "attack: short repeated dedications are the "
                           "softest target on any inscribed monument."),
        "method": ("First, isolate the short repeated formulas on pillar "
                   "capitals as the entry point. Second, segment the "
                   "formula into title words by comparing repetitions. "
                   "Third, match the royal epithet to chronicle sources, "
                   "identifying Devanampiya Piyadasi. Fourth, derive the "
                   "alphasyllabary values from the name spellings, noting "
                   "the inherent-vowel system. Fifth, read the long rock "
                   "edicts with the values and verify the moral and "
                   "administrative sense."),
        "readings": [
            "The pillar-capital formula yields the royal epithet Devanampiya Piyadasi.",
            "The script is an alphasyllabary: consonants carry an inherent 'a' vowel.",
            "Chronicle sources identify Piyadasi as the emperor Ashoka.",
        ],
        "translations": [
            "Edict opening: Beloved-of-the-Gods, King Piyadasi, speaks thus.",
            "The dhamma edicts: the emperor's moral instructions on tolerance and conduct.",
        ],
        "sig_pointer": ("The Signature edition re-derives the formula "
                        "attack as a labeled exercise on solved material, "
                        "stating assumptions openly and claiming no new "
                        "readings of the edicts."),
        "assumptions": [
            "A1: Pillar-capital texts repeat a royal formula (documented epigraphy).",
            "A2: Ceylonese chronicles preserve the epithet's owner (documented cross-source).",
            "A3: The script marks vowels on consonant bases (Prinsep's documented finding).",
            "A4: Rock edicts extend the same language and formula (documented corpus).",
        ],
        "steps": [
            "Collect every short pillar-capital inscription and align the repetitions.",
            "Segment the formula into its title words.",
            "Match Devanampiya Piyadasi to the chronicle identification with Ashoka.",
            "Derive consonant and vowel-mark values from the name spellings.",
            "Read the long rock edicts with the derived values.",
            "Verify the edicts read as coherent imperial moral instruction.",
        ],
        "confirm": [
            "The values read all fourteen major rock edicts coherently across the subcontinent.",
            "Bilingual Greek-Aramaic versions at Kandahar confirm the edicts' sense.",
            "The derived script family matches every later Indian script's structure.",
        ],
        "refute": [
            "If the chronicle identification were wrong, the anchor name would be a stranger.",
            "If rock edicts resisted the pillar-derived values, the reading would be local only.",
            "If the Greek versions contradicted the Brahmi sense, the translation would fail.",
        ],
        "not_claims": [
            "It does not claim Prinsep worked alone - Turnour's chronicles were essential.",
            "It does not claim every Ashokan word is certain - some remain debated.",
            "It does not claim the re-derivation changes any accepted reading.",
        ],
        "citations": [CIT_PRINSEP, CIT_SALOMON, CIT_ROBINSON],
        "demo_sample": "DEVANAMPIYA-PIYADASI-RAJA-DEVANAMPIYA",
        "demo_anchor": "PIYADASI",
    },
    {
        "key": "ugaritic-script",
        "name": "Ugaritic Script",
        "group": "Deciphered Scripts",
        "ladder_rank": 11,
        "ladder_tier": "foundations",
        "script": "Ugaritic alphabetic cuneiform",
        "status": "deciphered",
        "problem": ("Clay tablets from a Bronze Age port city, written in "
                    "wedge marks - but only thirty signs, far too few for "
                    "syllabic cuneiform. The problem was to recognize an "
                    "alphabet hiding in cuneiform dress, and to read the "
                    "mythology of a lost Canaanite city."),
        "background": (
            "The ancient city of Ugarit was discovered at Ras Shamra on "
            "the Syrian coast in 1928, and its tablets proved to be "
            "written in a cuneiform alphabet of just 30 signs. Hans Bauer, "
            "Edouard Dhorme, and Charles Virolleaud deciphered the script "
            "independently between 1930 and 1932, each working from the "
            "hypothesis that the language was Semitic. The small sign "
            "inventory was the giveaway: no syllabary needs so few signs. "
            "Cognates with Hebrew and other Semitic languages supplied the "
            "vocabulary, and the tablets revealed the Baal cycle, the "
            "oldest substantial Northwest Semitic mythology. Ugaritic is "
            "now the standard training text for the decipherment of "
            "alphabetic scripts."),
        "why_it_matters": ("Ugaritic is the fastest great decipherment - "
                           "about two years from discovery to reading - "
                           "because the solvers trusted the sign count. It "
                           "teaches the inventory insight: count the signs "
                           "first, and the script type reveals itself."),
        "method": ("First, count the signs: thirty signs means an alphabet, "
                   "not a syllabary. Second, hypothesize a Semitic "
                   "language from the Syrian coastal findspot. Third, "
                   "match frequent words against Hebrew and Aramaic "
                   "cognates, starting with divine names. Fourth, assign "
                   "consonant values and test them on administrative lists "
                   "where the sense is constrained. Fifth, read the myth "
                   "tablets and verify the narratives cohere."),
        "readings": [
            "Thirty signs resolve into a consonantal alphabet, not a syllabary.",
            "The divine name bcl reads as Baal, the storm god of the myths.",
            "Administrative lists confirm the values on constrained vocabulary.",
        ],
        "translations": [
            "Baal cycle opening: the palace-building narrative of the storm god.",
            "Administrative lists: rations and personnel of the royal palace.",
        ],
        "sig_pointer": ("The Signature edition re-derives the sign-count "
                        "insight as a labeled exercise on solved material, "
                        "stating assumptions openly and claiming no new "
                        "readings of the tablets."),
        "assumptions": [
            "A1: Thirty signs indicate an alphabet (documented decipherment logic).",
            "A2: The language is Semitic (Bauer, Dhorme, and Virolleaud's documented hypothesis).",
            "A3: Divine names are the cognate anchors (documented method).",
            "A4: Administrative lists constrain test vocabulary (documented genre).",
        ],
        "steps": [
            "Count the distinct signs across the tablet corpus.",
            "Hypothesize an alphabet and a Semitic language.",
            "Match divine names to Hebrew and Aramaic cognates.",
            "Assign consonant values from the cognate matches.",
            "Test the values on palace administrative lists.",
            "Read the myth tablets and verify narrative coherence.",
        ],
        "confirm": [
            "The Baal cycle reads as continuous, coherent mythology with the assigned values.",
            "Trilingual word lists confirm Ugaritic vocabulary against known languages.",
            "New tablets from Ras Shamra read without revising the alphabet.",
        ],
        "refute": [
            "If the language were not Semitic, the cognate matches would be systematic coincidence.",
            "If the sign count had been miscounted, the alphabet hypothesis would fail.",
            "If myths read as nonsense, the values would only suit administrative lists.",
        ],
        "not_claims": [
            "It does not credit a single decipherer - three scholars converged independently.",
            "It does not claim every Ugaritic word is certain - rare terms are debated.",
            "It does not claim the re-derivation changes any accepted value.",
        ],
        "citations": [CIT_BORDREUIL, CIT_PARPOLA_UG, CIT_ROBINSON],
        "demo_sample": "BCL-ALPHABET-BCL-TABLET-BCL",
        "demo_anchor": "BCL",
    },
    {
        "key": "oracle-bone-script",
        "name": "Oracle Bone Script",
        "group": "Deciphered Scripts",
        "ladder_rank": 12,
        "ladder_tier": "foundations",
        "script": "Jiaguwen (oracle bone script)",
        "status": "deciphered",
        "problem": ("Dragon bones sold in a Beijing pharmacy turned out to "
                    "be inscribed turtle shells three thousand years old. "
                    "The problem was to prove these scratches are the "
                    "earliest Chinese writing - and to read the divination "
                    "records of a dynasty history had called legendary."),
        "background": (
            "In 1899 the scholar Wang Yirong recognized writing on "
            "'dragon bones' - oracle bones sold as medicine - and traced "
            "them to Anyang, the last capital of the Shang dynasty. The "
            "bones and turtle plastrons carry divination records: a "
            "question was carved, heat was applied until the bone cracked, "
            "and the crack was read as the answer. Luo Zhenyu and Wang "
            "Guowei proved the inscriptions name the Shang kings in the "
            "order given by traditional histories, turning legend into "
            "documented dynasty. The script is the direct ancestor of "
            "modern Chinese characters, already mixing pictographs with "
            "phonetic loans. Over 100,000 inscribed pieces are now known, "
            "recording warfare, harvests, weather, and royal hunts around "
            "1200 BCE."),
        "why_it_matters": ("Oracle bones are the proof that Chinese "
                           "writing is 3,200 years old and that the Shang "
                           "dynasty was real. They teach the king-list "
                           "proof: when inscriptions name rulers in the "
                           "traditional order, legend becomes history."),
        "method": ("First, collect the inscribed bones and sort them by "
                   "physical and scribal features. Second, isolate the "
                   "recurring name sequences in the divination prefaces. "
                   "Third, match the name order to the traditional Shang "
                   "king list. Fourth, read the divination charges as "
                   "paired positive and negative questions, the classic "
                   "buci formula. Fifth, verify the vocabulary against "
                   "bronze inscriptions and the earliest received texts."),
        "readings": [
            "The preface name sequences match the traditional Shang king order.",
            "Divination charges come in positive-negative pairs: it will rain, it will not rain.",
            "The script already uses phonetic loans, the rebus principle of Chinese writing.",
        ],
        "translations": [
            "Weather charge: it will rain on the coming ten-day week; it will not rain.",
            "Warfare charge: the king should raise troops against the named enemy.",
        ],
        "sig_pointer": ("The Signature edition re-derives the king-list "
                        "proof as a labeled exercise on solved material, "
                        "stating assumptions openly and claiming no new "
                        "readings of the bones."),
        "assumptions": [
            "A1: Preface name sequences record Shang kings (documented epigraphy).",
            "A2: Traditional histories preserve the king order (documented cross-source).",
            "A3: Charges follow the positive-negative pair formula (documented genre).",
            "A4: The script is ancestral to Chinese characters (documented paleography).",
        ],
        "steps": [
            "Sort the inscribed pieces by scribe hand and physical type.",
            "Extract the recurring name sequences from divination prefaces.",
            "Align the name order with the traditional Shang king list.",
            "Read the charges as paired positive and negative questions.",
            "Check vocabulary against bronze inscriptions of the same period.",
            "Verify that hunts, wars, and harvests form a coherent royal calendar.",
        ],
        "confirm": [
            "The king order matches tradition across thousands of independent inscriptions.",
            "Bronze inscriptions confirm the same vocabulary and name forms.",
            "The calendar of rituals reconstructs a coherent Shang ritual year.",
        ],
        "refute": [
            "If the king order diverged from tradition, the historical proof would fail.",
            "If charges did not pair, the divination formula would be misread.",
            "If bronze inscriptions contradicted the vocabulary, the readings would be isolated.",
        ],
        "not_claims": [
            "It does not claim every bone graph is read - many remain undeciphered.",
            "It does not claim the bones record private life - they are royal divinations.",
            "It does not claim the re-derivation changes any accepted reading.",
        ],
        "citations": [CIT_KEIGHTLEY, CIT_WANG, CIT_ROBINSON],
        "demo_sample": "JIA-GU-WEN-BU-CI-JIA-GU",
        "demo_anchor": "BU-CI",
    },
    {
        "key": "luwian-hieroglyphs",
        "name": "Luwian Hieroglyphs",
        "group": "Partially Deciphered Scripts",
        "ladder_rank": 13,
        "ladder_tier": "compounded",
        "script": "Anatolian hieroglyphs",
        "status": "deciphered",
        "problem": ("Monumental picture-signs across Anatolia and Syria, "
                    "used for a thousand years, long mistaken for "
                    "'Hittite hieroglyphs' of an unknown tongue. The "
                    "problem was to separate the script from the "
                    "Hittites - and to read the last voices of the Bronze "
                    "Age kingdoms."),
        "background": (
            "Anatolian hieroglyphs were used from about 1500 to 700 BCE, "
            "first for the Luwian language of the Hittite empire's "
            "southern lands, then for the Neo-Hittite kingdoms of "
            "southeastern Anatolia and northern Syria. Emil Forrer "
            "identified the language as Luwian in 1919, and Helmuth "
            "Bossert's 1947 reading of the Karatepe bilingual - the same "
            "text in Phoenician and Luwian hieroglyphs - provided the "
            "decisive key. The script mixes logograms and syllabic signs, "
            "written in alternating direction, boustrophedon, like "
            "plowing a field. Later work by Hawkins, Morpurgo Davies, "
            "and others completed the sign values. The inscriptions "
            "record royal boasts, treaties, and building dedications of "
            "the Iron Age kingdoms."),
        "why_it_matters": ("Luwian shows that a bilingual can hide in "
                           "plain sight for decades before someone uses "
                           "it properly, and its reading recovered the "
                           "history of the kingdoms that survived the "
                           "Bronze Age collapse. It teaches the boustrophedon "
                           "rule: follow the facing of the signs."),
        "method": ("First, use the Karatepe Phoenician text as the sense "
                   "anchor for the hieroglyphic version. Second, match "
                   "proper names across the two versions to fix sign "
                   "values. Third, determine the reading direction from "
                   "the facing of the signs, alternating line by line. "
                   "Fourth, separate logograms from syllabic signs by "
                   "testing phonetic complements. Fifth, verify the values "
                   "on the long royal inscriptions of Carchemish and "
                   "Malatya."),
        "readings": [
            "Karatepe names fix the core syllabary against the Phoenician version.",
            "Boustrophedon direction is read from the facing of the figure signs.",
            "Royal titulary repeats in fixed formulas across the Neo-Hittite kingdoms.",
        ],
        "translations": [
            "Karatepe dedication: the bilingual account of Azatiwada's building works.",
            "Carchemish royal inscriptions: the boasts and curses of the city's kings.",
        ],
        "sig_pointer": ("The Signature edition re-derives the bilingual "
                        "alignment as a labeled exercise on solved "
                        "material, stating assumptions openly and claiming "
                        "no new readings."),
        "assumptions": [
            "A1: The Karatepe versions carry the same text (documented bilingual).",
            "A2: The language is Luwian, not Hittite (Forrer's documented identification).",
            "A3: Signs are read toward the direction they face (documented convention).",
            "A4: Royal formulas repeat across kingdoms (documented epigraphy).",
        ],
        "steps": [
            "Align the Karatepe Phoenician and hieroglyphic texts section by section.",
            "Fix syllabic values from the proper names shared by both versions.",
            "Establish line direction from sign facing, alternating boustrophedon.",
            "Separate logograms from syllables with phonetic-complement tests.",
            "Read the Carchemish and Malatya royal inscriptions with the values.",
            "Verify the texts read as coherent royal declarations and curses.",
        ],
        "confirm": [
            "The sign values read the entire Neo-Hittite corpus coherently.",
            "Luwian vocabulary confirmed by cuneiform Luwian texts matches the hieroglyphic readings.",
            "New inscriptions from recent excavations read without revising the syllabary.",
        ],
        "refute": [
            "If the Karatepe texts diverged in content, the bilingual anchor would fail.",
            "If the language were Hittite rather than Luwian, the vocabulary would not fit.",
            "If boustrophedon were misjudged, whole lines would read backwards.",
        ],
        "not_claims": [
            "It does not claim every rare logogram is securely read.",
            "It does not claim the re-derivation revises any accepted value.",
            "It does not claim the script is Hittite - it writes Luwian.",
        ],
        "citations": [CIT_HAWKINS, CIT_MELCHERT, CIT_ROBINSON],
        "demo_sample": "KARATEPE-BILINGUAL-KARATEPE-GATE",
        "demo_anchor": "KARATEPE",
    },
    {
        "key": "etruscan-script-decipherment",
        "name": "The Etruscan Script Decipherment",
        "group": "Partially Deciphered Scripts",
        "ladder_rank": 14,
        "ladder_tier": "compounded",
        "script": "Etruscan alphabet",
        "status": "partially deciphered",
        "problem": ("Thirteen thousand inscriptions in an alphabet anyone "
                    "can sound out - yet the language stays half silent. "
                    "The problem is the cruellest in epigraphy: perfect "
                    "phonetics with no bilingual and no living relatives, "
                    "so every sentence must be solved like a crossword "
                    "with half the clues missing."),
        "background": (
            "The Etruscans dominated western Italy before Rome, from "
            "about 700 to 100 BCE, leaving some 13,000 inscriptions, "
            "mostly short funerary and dedicatory texts. Their alphabet, "
            "borrowed from Greek, is fully readable phonetically - "
            "scholars can pronounce every inscription. But Etruscan is a "
            "language isolate of the Tyrsenian family, related only to "
            "Lemnian and Raetic, so vocabulary must be extracted from "
            "context: bilinguals are vanishingly rare, the longest being "
            "the Pyrgi gold tablets with a Phoenician parallel. Massimo "
            "Pallottino's mid-20th-century work systematized the grammar, "
            "and Helmut Rix's corpus organized the texts. We can read the "
            "sounds of Etruscan fluently; we understand perhaps half of "
            "what it says."),
        "why_it_matters": ("Etruscan is the warning every decipherer "
                           "needs: reading the script is not reading the "
                           "language. It teaches the context-extraction "
                           "method - squeezing meaning from formulas, "
                           "numbers, and the few bilinguals - that applies "
                           "to every partially understood tongue."),
        "method": ("First, read the alphabet phonetically with Greek "
                   "letter values. Second, collect the rare bilinguals, "
                   "especially the Pyrgi tablets, as vocabulary anchors. "
                   "Third, extract repeated funerary and dedicatory "
                   "formulas to fix kinship terms, ages, and offices. "
                   "Fourth, use numerals and magistrate titles, whose "
                   "sense is constrained by context, to extend the "
                   "lexicon. Fifth, test every new word against all its "
                   "occurrences for consistent sense."),
        "readings": [
            "The alphabet reads phonetically - pronunciation is not the problem.",
            "Pyrgi tablets give the Phoenician parallel that anchors key vocabulary.",
            "Funerary formulas yield kinship terms: son, daughter, wife, with ages.",
        ],
        "translations": [
            "Pyrgi dedication: the offering formula paralleled in Phoenician.",
            "Funerary formula: the standard age and family statements of the tombs.",
        ],
        "sig_pointer": ("The Signature edition re-derives the "
                        "context-extraction method as a labeled exercise, "
                        "stating assumptions openly and claiming no new "
                        "Etruscan vocabulary."),
        "assumptions": [
            "A1: Greek letter values give Etruscan pronunciation (documented alphabet).",
            "A2: The Pyrgi Phoenician text parallels the Etruscan (documented bilingual).",
            "A3: Funerary formulas repeat with fixed slots for kin and age (documented genre).",
            "A4: A word must keep one sense across all occurrences (documented method).",
        ],
        "steps": [
            "Transcribe the inscriptions phonetically with Greek values.",
            "Extract vocabulary anchors from the Pyrgi bilingual.",
            "Collect funerary formulas and fix the kinship and age slots.",
            "Extend the lexicon through numerals and office titles.",
            "Test each proposed word sense against every occurrence.",
            "Assemble the longest texts, such as the Zagreb mummy wrapping, with the secured vocabulary.",
        ],
        "confirm": [
            "Bilingual anchors keep their sense across all thirteen thousand inscriptions.",
            "Funerary formulas produce consistent ages and family relations.",
            "New inscriptions continue to yield to the formula method without contradiction.",
        ],
        "refute": [
            "If the Pyrgi parallel were loose rather than literal, the anchor vocabulary would drift.",
            "If funerary slots varied freely, the kinship terms would be unprovable.",
            "If a word demanded different senses in different texts, its reading would fail.",
        ],
        "not_claims": [
            "It does not claim Etruscan is fully understood - roughly half remains obscure.",
            "It does not claim new vocabulary - the lexicon comes from published scholarship.",
            "It does not claim the language has living relatives - it does not.",
        ],
        "citations": [CIT_BONFANTE, CIT_RIX, CIT_ROBINSON],
        "demo_sample": "MI-LARTHI-ANA-MI-VEL",
        "demo_anchor": "MI-",
    },
    {
        "key": "meroitic-script",
        "name": "Meroitic Script",
        "group": "Partially Deciphered Scripts",
        "ladder_rank": 15,
        "ladder_tier": "compounded",
        "script": "Meroitic hieroglyphic and cursive",
        "status": "partially deciphered",
        "problem": ("The script of the Kushite kings who once ruled Egypt "
                    "was cracked a century ago - and the language still "
                    "will not speak. The problem is the purest version of "
                    "the Etruscan trap: every sign value known, every "
                    "sentence still half dark."),
        "background": (
            "Meroitic was written from about 300 BCE to 400 CE in the "
            "kingdom of Kush, south of Egypt, in both a hieroglyphic and "
            "a cursive form. Francis Llewellyn Griffith worked out the "
            "phonetic values of the 23 signs in 1909 to 1911, using royal "
            "names and Egyptian parallels. We can pronounce every Meroitic "
            "text - and titles like qore, king, and kandake, queen mother, "
            "are secure. But the Meroitic language has no known relatives, "
            "so most vocabulary remains guesswork from context. Claude "
            "Rilly's 2007 grammar organized what is known and argued for "
            "distant Nilo-Saharan connections, still debated. The great "
            "stelae of the Kushite kings can be sounded out in full; "
            "their finer meaning stays locked."),
        "why_it_matters": ("Meroitic proves that phonetic decipherment is "
                           "only halftime: without a related language, "
                           "values are not understanding. It teaches the "
                           "honest boundary every solver must mark between "
                           "reading signs and reading minds."),
        "method": ("First, fix the 23 sign values from royal names shared "
                   "with Egyptian records, following Griffith. Second, "
                   "extract the secure titles - qore, kandake - from "
                   "context. Third, collect every occurrence of each "
                   "unknown word and map its contexts. Fourth, test "
                   "Nilo-Saharan cognate proposals against the secured "
                   "phonetics. Fifth, mark every unsecured word honestly "
                   "rather than forcing a translation."),
        "readings": [
            "Griffith's 23 sign values let every text be pronounced.",
            "Royal titles qore and kandake are secure from Egyptian parallels.",
            "Cursive and hieroglyphic forms are the same script in two hands.",
        ],
        "translations": [
            "Royal titulary: the standard king and queen-mother formulas of the stelae.",
            "Offering formulas: the repeated funerary provisions, partly understood.",
        ],
        "sig_pointer": ("The Signature edition re-derives the "
                        "values-without-language boundary as a labeled "
                        "exercise, stating assumptions openly and marking "
                        "unsecured words honestly."),
        "assumptions": [
            "A1: Griffith's 23 sign values are the documented standard.",
            "A2: Royal names match Egyptian records (documented cross-source).",
            "A3: Titles are secured by context (documented method).",
            "A4: Unsecured words must be marked, not forced (documented honesty rule).",
        ],
        "steps": [
            "Transcribe texts with Griffith's sign values.",
            "Fix the secure titles from Egyptian parallels.",
            "Map every occurrence of each unknown word across the corpus.",
            "Test cognate proposals against the secured phonetics.",
            "Assemble the best-available reading with honest markings.",
            "Verify that secured words keep their sense in every new text.",
        ],
        "confirm": [
            "Royal names keep matching Egyptian records with the same values.",
            "Secured titles behave consistently across the whole corpus.",
            "New stelae pronounce cleanly with Griffith's values.",
        ],
        "refute": [
            "If the sign values were wrong, the Egyptian name matches would fail.",
            "If titles shifted sense between texts, the contextual method would collapse.",
            "If a related language were found, the unsecured vocabulary could change wholesale.",
        ],
        "not_claims": [
            "It does not claim Meroitic is understood - most vocabulary is not.",
            "It does not claim any cognate proposal is proven - they are debated.",
            "It does not force translations of unsecured words.",
        ],
        "citations": [CIT_GRIFFITH, CIT_RILLY, CIT_ROBINSON],
        "demo_sample": "QORE-MEROE-QORE-KUSH",
        "demo_anchor": "QORE",
    },
    {
        "key": "carian-script",
        "name": "Carian Script",
        "group": "Partially Deciphered Scripts",
        "ladder_rank": 16,
        "ladder_tier": "compounded",
        "script": "Carian alphabet",
        "status": "deciphered",
        "problem": ("Graffiti scratched by Carian mercenaries on Egyptian "
                    "temples, in an alphabet that looks Greek but is not. "
                    "The problem was to stop reading it as bad Greek - and "
                    "to hear the Anatolian language hiding behind "
                    "familiar-looking letters."),
        "background": (
            "Carian was the language of Caria in southwestern Anatolia, "
            "written in an alphabet of about 45 signs used from the "
            "seventh to the third century BCE. Carian mercenaries serving "
            "in Egypt left graffiti on temples, including the famous "
            "Abu Simbel inscriptions, some with Egyptian parallels. For "
            "decades scholars misread the script with Greek values. In "
            "the 1970s and 1980s, John Ray proposed new values from the "
            "bilingual evidence, and Ignacio-Javier Adiego's 2007 grammar "
            "consolidated the decipherment. Carian proved to be a "
            "Luwic Anatolian language, cousin to Luwian, hiding behind "
            "letterforms borrowed from Greek. The graffiti are mostly "
            "names and short memorials - modest texts that unlocked a "
            "whole language."),
        "why_it_matters": ("Carian is the proof that familiar letterforms "
                           "can lie: the script looked Greek while the "
                           "language was Anatolian. It teaches the "
                           "bilingual-graffiti method and the discipline of "
                           "distrusting borrowed alphabets."),
        "method": ("First, collect the graffiti with Egyptian parallels, "
                   "especially Abu Simbel, as anchors. Second, discard the "
                   "Greek values and derive fresh values from the name "
                   "correspondences. Third, test the new values for "
                   "Anatolian vocabulary, following Ray. Fourth, verify "
                   "the grammar patterns as Luwic, with characteristic "
                   "endings. Fifth, confirm the values on the longer "
                   "Carian texts from Caria itself."),
        "readings": [
            "Abu Simbel name pairs fix the core alphabet against Egyptian.",
            "The values reveal Luwic Anatolian vocabulary, not Greek.",
            "Letterforms are borrowed; the language behind them is not.",
        ],
        "translations": [
            "Mercenary graffiti: name memorials of Carian soldiers in Egypt.",
            "Longer Carian texts: dedications and funerary formulas from Caria.",
        ],
        "sig_pointer": ("The Signature edition re-derives the "
                        "alphabet-distrust method as a labeled exercise on "
                        "solved material, stating assumptions openly and "
                        "claiming no new readings."),
        "assumptions": [
            "A1: Abu Simbel graffiti pair Carian and Egyptian names (documented bilingual).",
            "A2: Greek letter values are the wrong starting point (documented error).",
            "A3: The language is Anatolian, testable against Luwian (documented hypothesis).",
            "A4: Longer Carian texts must confirm graffiti-derived values (documented test).",
        ],
        "steps": [
            "Align the Abu Simbel Carian graffiti with their Egyptian name parallels.",
            "Derive fresh letter values from the name correspondences.",
            "Test the values for Anatolian vocabulary matches.",
            "Check the grammar for Luwic endings.",
            "Apply the values to the longer texts from Caria.",
            "Verify the corpus reads as coherent memorials and dedications.",
        ],
        "confirm": [
            "Adiego's grammar reads the whole Carian corpus with consistent values.",
            "Luwian cognates confirm the vocabulary across the lexicon.",
            "New graffiti continue to yield to the same alphabet.",
        ],
        "refute": [
            "If the Abu Simbel parallels were coincidental, the alphabet would rest on nothing.",
            "If the grammar failed to pattern as Anatolian, the language claim would fail.",
            "If Carian texts contradicted the values, the decipherment would be graffiti-bound.",
        ],
        "not_claims": [
            "It does not claim the corpus is large - it is mostly short texts.",
            "It does not claim every sign value is beyond debate.",
            "It does not claim the re-derivation revises Adiego's grammar.",
        ],
        "citations": [CIT_ADIEGO, CIT_RAY, CIT_ROBINSON],
        "demo_sample": "CARIAN-GRAFFITI-ABUSIMBEL-CARIAN",
        "demo_anchor": "CARIAN",
    },
    {
        "key": "iberian-scripts",
        "name": "Iberian Scripts",
        "group": "Partially Deciphered Scripts",
        "ladder_rank": 17,
        "ladder_tier": "compounded",
        "script": "Northeastern and Southeastern Iberian",
        "status": "partially deciphered",
        "problem": ("Coin legends and lead tablets across ancient Spain, "
                    "in scripts whose sign values were worked out a "
                    "century ago - for a language nobody on Earth still "
                    "speaks or understands. The problem is to read the "
                    "sounds of a vanished tongue from its money and "
                    "letters."),
        "background": (
            "The Iberian scripts were used from the fifth to the first "
            "century BCE across eastern and southern Spain, written on "
            "coins, lead tablets, and stone. Manuel Gomez-Moreno worked "
            "out the sign values in the 1920s from coin legends naming "
            "cities known from classical sources. The scripts are "
            "semi-syllabaries: stops are written with syllabic signs "
            "while continuants get alphabetic ones. We can pronounce "
            "Iberian texts reliably - but the Iberian language is "
            "unclassified and largely untranslated, with only numerals, "
            "some titles, and formulaic phrases understood. Jurgen "
            "Untermann's Monumenta corpus organized the texts. The lead "
            "tablets, many of them letters, remain readable in sound "
            "and stubborn in sense."),
        "why_it_matters": ("Iberian is Europe's great readable-unknown: "
                           "proof that coins can crack a script while the "
                           "language outlives every attempt. It teaches "
                           "the coin-legend method that also served "
                           "Brahmi and Carian."),
        "method": ("First, collect coin legends naming cities known from "
                   "Greek and Latin sources. Second, derive sign values "
                   "from the city-name spellings, following Gomez-Moreno. "
                   "Third, separate the syllabic stop signs from the "
                   "alphabetic continuants by positional analysis. "
                   "Fourth, extend the values to the lead tablets and "
                   "test formulaic phrases. Fifth, mark untranslated "
                   "passages honestly rather than forcing sense."),
        "readings": [
            "Coin legends fix the sign values against classical city names.",
            "The semi-syllabary structure explains the two sign behaviors.",
            "Lead tablets pronounce cleanly with the coin-derived values.",
        ],
        "translations": [
            "Coin legends: city names and magistrate marks of the mints.",
            "Lead tablet formulas: the repeated letter openings, partly understood.",
        ],
        "sig_pointer": ("The Signature edition re-derives the coin-legend "
                        "method as a labeled exercise, stating assumptions "
                        "openly and marking untranslated passages honestly."),
        "assumptions": [
            "A1: Coin legends name cities known from classical sources (documented anchor).",
            "A2: Gomez-Moreno's sign values are the documented standard.",
            "A3: Stops are syllabic and continuants alphabetic (documented structure).",
            "A4: Untranslated text must be marked, not forced (documented honesty rule).",
        ],
        "steps": [
            "Catalog coin legends against the classical city lists.",
            "Derive sign values from the city-name spellings.",
            "Classify each sign as syllabic stop or alphabetic continuant.",
            "Read the lead tablets with the classified values.",
            "Test formulaic phrases for repeated, constrained sense.",
            "Mark the remaining text as pronounced but untranslated.",
        ],
        "confirm": [
            "City names keep emerging correctly from new coin finds.",
            "The semi-syllabary structure holds across both Iberian scripts.",
            "Numerals and titles behave consistently in the lead tablets.",
        ],
        "refute": [
            "If city identifications were wrong, the whole value set would shift.",
            "If the syllabary structure failed, signs would behave inconsistently.",
            "If lead tablets contradicted coin values, the system would be genre-bound.",
        ],
        "not_claims": [
            "It does not claim Iberian is translated - it is not.",
            "It does not claim the language is classified - it remains unclassified.",
            "It does not force sense onto untranslated passages.",
        ],
        "citations": [CIT_GOMEZMORENO, CIT_UNTERMANN, CIT_ROBINSON],
        "demo_sample": "IBERIAN-COIN-IBERIAN-LEAD",
        "demo_anchor": "IBERIAN",
    },
    {
        "key": "linear-elamite",
        "name": "Linear Elamite",
        "group": "Partially Deciphered Scripts",
        "ladder_rank": 18,
        "ladder_tier": "compounded",
        "script": "Linear Elamite",
        "status": "partially deciphered",
        "problem": ("Forty inscriptions in a Bronze Age Iranian script, "
                    "unread for a century - until a 2022 paper claimed the "
                    "whole system cracked. The problem is the newest in "
                    "decipherment: how to treat a claimed solution that "
                    "the field has not yet accepted."),
        "background": (
            "Linear Elamite was used in southwestern Iran around 2300 to "
            "1800 BCE, surviving in about forty inscriptions, many on "
            "silver vessels with dedicatory texts. In 2022 Francois Desset "
            "and colleagues published a claimed full decipherment in the "
            "Zeitschrift fur Assyriologie, reading the texts as Elamite "
            "dedications with recurring royal names and titles. The claim "
            "rests on repeated formulas on the silver gunagi vessels and "
            "on sign sequences matching known Elamite names. As of 2026 "
            "the decipherment is not yet consensus: specialists continue "
            "to test the readings, and the responsible scholarly posture "
            "is 'claimed, under review.' The case is included here as "
            "exactly that - a live, labeled, contested claim."),
        "why_it_matters": ("Linear Elamite is decipherment in real time: "
                           "it teaches the difference between a published "
                           "claim and an accepted reading, and the "
                           "discipline of labeling contested solutions "
                           "honestly while the field does its work."),
        "method": ("First, collect the forty inscriptions, prioritizing "
                   "the silver vessel dedications. Second, isolate the "
                   "repeated formulas and royal-name candidates, following "
                   "Desset. Third, match name sequences to Elamite names "
                   "known from cuneiform sources. Fourth, derive sign "
                   "values from the name matches and test them on the "
                   "remaining texts. Fifth, submit the readings to "
                   "independent scholarly testing and report the "
                   "contested status honestly."),
        "readings": [
            "Claimed: vessel formulas yield Elamite royal names and titles.",
            "Claimed: the sign values read the dedications as coherent Elamite.",
            "Status: published 2022, under independent review, not consensus.",
        ],
        "translations": [
            "Claimed vessel dedication: the gunagi vessel formulas as Elamite offerings.",
            "Claimed royal titulary: the repeated name-and-title sequences.",
        ],
        "sig_pointer": ("The Signature edition treats the 2022 claim as a "
                        "labeled case study in contested decipherment: it "
                        "re-derives the formula reasoning, states the "
                        "non-consensus status in every line, and claims no "
                        "independent verification."),
        "assumptions": [
            "A1: The 2022 readings are a published claim, not consensus (documented status).",
            "A2: Vessel formulas repeat royal names (Desset's documented analysis).",
            "A3: Elamite names from cuneiform sources anchor the matches (documented cross-source).",
            "A4: Independent testing is still in progress (documented field status).",
        ],
        "steps": [
            "Assemble the forty-inscription corpus with the vessel texts first.",
            "Isolate repeated formulas and name candidates.",
            "Match name sequences to Elamite names from cuneiform records.",
            "Derive sign values and test them across the corpus.",
            "Check the readings against Elamite grammar as known from cuneiform.",
            "Report the contested status and await independent confirmation.",
        ],
        "confirm": [
            "If independent scholars reproduce the readings on new texts, the claim strengthens.",
            "Consistent grammar with cuneiform Elamite would support the values.",
            "The vessel formulas' coherence is the claim's current best evidence.",
        ],
        "refute": [
            "If specialists find the name matches forced, the decipherment fails.",
            "If the values do not extend beyond the vessel formulas, the claim is local.",
            "Non-consensus after full testing would leave the script undeciphered.",
        ],
        "not_claims": [
            "It does not present the 2022 claim as accepted scholarship - it is not.",
            "It does not claim independent verification - testing continues.",
            "It does not hide the contest: the status is labeled in every record.",
        ],
        "citations": [CIT_DESSET, CIT_ROBINSON],
        "demo_sample": "GUNAGI-VESSEL-GUNAGI-SILVER",
        "demo_anchor": "GUNAGI",
    },
    {
        "key": "epi-olmec-script",
        "name": "Epi-Olmec (Isthmian) Script",
        "group": "Partially Deciphered Scripts",
        "ladder_rank": 19,
        "ladder_tier": "compounded",
        "script": "Epi-Olmec / Isthmian",
        "status": "partially deciphered",
        "problem": ("A handful of monuments from Mexico's isthmus carry a "
                    "script older than the Maya's, with a Long Count date "
                    "staring back at the reader. The problem is to read "
                    "America's second-oldest writing from a corpus so small "
                    "that every new monument rewrites the rules."),
        "background": (
            "The Epi-Olmec or Isthmian script appears on a small group of "
            "monuments from Veracruz and Tabasco, dating roughly 500 BCE "
            "to 500 CE, including the La Mojarra Stela and the Tuxtla "
            "Statuette. In 1993 John Justeson and Terrence Kaufman "
            "published a decipherment reading the texts as an early "
            "Mixe-Zoquean language, using the Long Count dates as "
            "anchors and cognates with modern Mixe-Zoque languages. The "
            "reading is partially accepted and partly contested: "
            "specialists agree the script is logosyllabic and that dates "
            "anchor it, while some proposed readings remain debated. The "
            "corpus is tiny - a few thousand signs total - so every "
            "reading carries the weight of the whole script."),
        "why_it_matters": ("Epi-Olmec is the test case for deciphering "
                           "from a micro-corpus: it teaches the Long Count "
                           "anchor method and the discipline of marking "
                           "which readings are secure and which are "
                           "proposed."),
        "method": ("First, read the Long Count dates with the established "
                   "Maya calendar correlation as fixed anchors. Second, "
                   "isolate the glyphs adjacent to dates as event verbs. "
                   "Third, test the Mixe-Zoquean hypothesis with cognates "
                   "from modern Mixe-Zoque languages. Fourth, build the "
                   "logosyllabic sign values from the cognate matches. "
                   "Fifth, mark every contested reading explicitly and "
                   "test the values on each new monument."),
        "readings": [
            "Long Count dates anchor the texts in absolute time.",
            "The script is logosyllabic, mixing word signs and syllables.",
            "Mixe-Zoquean cognates supply the proposed vocabulary.",
        ],
        "translations": [
            "La Mojarra Stela: the dated narrative of a ruler's reign, partly read.",
            "Tuxtla Statuette: the early dated text with ritual content, partly read.",
        ],
        "sig_pointer": ("The Signature edition re-derives the date-anchor "
                        "method as a labeled exercise, marking contested "
                        "readings explicitly and claiming no new "
                        "decipherment."),
        "assumptions": [
            "A1: Long Count dates are read with the standard correlation (documented anchor).",
            "A2: The language may be Mixe-Zoquean (Justeson and Kaufman's documented hypothesis).",
            "A3: Date-adjacent glyphs are event verbs (documented method).",
            "A4: Contested readings must be marked, not smoothed over (documented honesty rule).",
        ],
        "steps": [
            "Fix the Long Count dates on each monument.",
            "Isolate the glyph clusters beside the dates.",
            "Test Mixe-Zoquean cognates against the clusters.",
            "Derive logosyllabic values from the matches.",
            "Read the full monuments with the derived values.",
            "Mark secure versus contested readings in the final text.",
        ],
        "confirm": [
            "Date-anchored verbs keep their sense across the monuments.",
            "Mixe-Zoquean cognates recur without forcing.",
            "New monuments, such as the Cascajal Block debate, test the system openly.",
        ],
        "refute": [
            "If the Mixe-Zoquean hypothesis failed, the vocabulary would collapse.",
            "If date correlations shifted, the anchors would move.",
            "If new monuments contradicted the values, the system would be monument-bound.",
        ],
        "not_claims": [
            "It does not claim full acceptance - parts remain contested.",
            "It does not hide which readings are proposed versus secure.",
            "It does not claim the corpus is sufficient for certainty.",
        ],
        "citations": [CIT_JUSTESON, CIT_COE],
        "demo_sample": "MOJARRA-STELA-MOJARRA-LONGCOUNT",
        "demo_anchor": "MOJARRA",
    },
    {
        "key": "zapotec-script",
        "name": "Zapotec Script",
        "group": "Partially Deciphered Scripts",
        "ladder_rank": 20,
        "ladder_tier": "compounded",
        "script": "Zapotec hieroglyphic",
        "status": "partially deciphered",
        "problem": ("Stone slabs at Monte Alban show processions of "
                    "danzante figures, each labeled with glyphs that name "
                    "the dead. The problem is to read the funerary labels "
                    "of a script whose language is still spoken in the "
                    "valleys below - but whose ancient form hides behind "
                    "terse name-glyphs."),
        "background": (
            "Zapotec writing was used from about 600 BCE to the Spanish "
            "conquest in Oaxaca, Mexico, carved on stone slabs, painted "
            "on pottery, and written in codices. The danzante slabs of "
            "Monte Alban, carved with contorted figures, carry "
            "name-glyphs identifying captives or ancestors. Alfonso "
            "Caso's excavations organized the corpus, and later work by "
            "Javier Urcid and others systematized the sign inventory of "
            "over a hundred glyphs. The script is logosyllabic, and the "
            "modern Zapotec languages supply vocabulary - but the "
            "inscriptions are so terse, mostly names and calendar dates, "
            "that extended texts remain difficult. The script is "
            "partially deciphered: the calendar, the name formulas, and "
            "many titles read cleanly, while narrative passages resist."),
        "why_it_matters": ("Zapotec is the Americas' great terse script: "
                           "it teaches the name-formula method and the "
                           "patience to let a living language illuminate - "
                           "but not dictate - its ancient ancestor."),
        "method": ("First, isolate the calendar glyphs using the known "
                   "Mesoamerican day signs as anchors. Second, extract "
                   "the name-glyph compounds from the danzante slabs. "
                   "Third, match name elements against Zapotec vocabulary "
                   "from colonial and modern sources. Fourth, identify "
                   "title glyphs by their fixed positions in the name "
                   "formulas. Fifth, test the values on pottery texts "
                   "where the sense is less constrained."),
        "readings": [
            "Calendar glyphs anchor the texts in the Mesoamerican day count.",
            "Danzante name-glyphs resolve into personal names and titles.",
            "Modern Zapotec supplies testable vocabulary for the ancient forms.",
        ],
        "translations": [
            "Danzante labels: the name and title formulas of the carved figures.",
            "Pottery texts: short dedicatory phrases, partly read.",
        ],
        "sig_pointer": ("The Signature edition re-derives the name-formula "
                        "method as a labeled exercise, stating assumptions "
                        "openly and claiming no new readings."),
        "assumptions": [
            "A1: Calendar glyphs follow the Mesoamerican day count (documented anchor).",
            "A2: Danzante labels are name formulas (documented genre).",
            "A3: Modern Zapotec illuminates ancient vocabulary (documented linguistics).",
            "A4: Title glyphs hold fixed formula positions (documented method).",
        ],
        "steps": [
            "Anchor the calendar glyphs to the known day signs.",
            "Extract name-glyph compounds from the danzante corpus.",
            "Match name elements to Zapotec vocabulary sources.",
            "Fix title glyphs by their formula positions.",
            "Test the values on pottery and codex texts.",
            "Mark narrative passages that resist reading.",
        ],
        "confirm": [
            "Name formulas repeat with consistent structure across the slabs.",
            "Calendar readings align with the Mesoamerican count.",
            "Colonial Zapotec dictionaries confirm the title vocabulary.",
        ],
        "refute": [
            "If day signs were misidentified, the calendar anchor would fail.",
            "If modern Zapotec misled the ancient forms, the vocabulary would be anachronistic.",
            "If titles shifted positions, the formula method would collapse.",
        ],
        "not_claims": [
            "It does not claim narrative texts are readable - most resist.",
            "It does not claim modern Zapotec equals the ancient language.",
            "It does not claim the re-derivation adds readings.",
        ],
        "citations": [CIT_URCID, CIT_COE],
        "demo_sample": "MONTEALBAN-GLYPH-MONTEALBAN-DANZANTE",
        "demo_anchor": "MONTEALBAN",
    },
    {
        "key": "khitan-scripts",
        "name": "Khitan Scripts",
        "group": "Partially Deciphered Scripts",
        "ladder_rank": 21,
        "ladder_tier": "compounded",
        "script": "Khitan large and small scripts",
        "status": "partially deciphered",
        "problem": ("An empire that ruled northern China for two centuries "
                    "left two different scripts - one logographic, one "
                    "half-deciphered - for a language with no living "
                    "descendants. The problem is to read the tomb "
                    "inscriptions of the Liao dynasty from epitaphs that "
                    "mix both systems."),
        "background": (
            "The Khitan Liao dynasty ruled northern China from 907 to "
            "1125 CE, using two scripts: the large script, created around "
            "920, largely logographic, and the small script, created "
            "around 925, a mixed system of several hundred signs. The "
            "key texts are the imperial tomb epitaphs, some with Chinese "
            "parallels that anchor names and dates. The small script is "
            "partially deciphered through the work of scholars including "
            "Aisin-Gioro Ulhicun and others, who used the Chinese "
            "parallels and Khitan vocabulary preserved in Chinese "
            "transcription. The large script remains less understood. "
            "The Khitan language itself is extinct, related distantly to "
            "Mongolic, so every reading is reconstructed, not confirmed "
            "by a living tongue."),
        "why_it_matters": ("Khitan is the empire that wrote twice: it "
                           "teaches the parallel-epitaph method and the "
                           "discipline of working two scripts for one "
                           "dead language without a living check."),
        "method": ("First, collect the tomb epitaphs with Chinese "
                   "parallels as bilingual anchors. Second, fix personal "
                   "names, titles, and dates from the Chinese versions. "
                   "Third, derive small-script values from the anchored "
                   "passages. Fourth, test the values on epitaphs without "
                   "parallels. Fifth, keep the large script's readings "
                   "separate and more tentative, marked by confidence."),
        "readings": [
            "Chinese-parallel epitaphs anchor names, titles, and dates.",
            "The small script yields to the parallel method; the large script resists.",
            "Khitan vocabulary preserved in Chinese transcription supplies test words.",
        ],
        "translations": [
            "Imperial epitaphs: the dated biographies of Liao emperors and consorts, partly read.",
            "Memorial texts: the standard funerary formulas, partly understood.",
        ],
        "sig_pointer": ("The Signature edition re-derives the "
                        "parallel-epitaph method as a labeled exercise, "
                        "marking confidence levels and claiming no new "
                        "readings."),
        "assumptions": [
            "A1: Chinese parallels carry the same epitaph content (documented bilingual).",
            "A2: Names and dates are the fixed anchors (documented method).",
            "A3: Small-script values extend from anchored to unanchored texts (documented test).",
            "A4: Large-script readings stay tentative (documented field status).",
        ],
        "steps": [
            "Align each epitaph with its Chinese parallel.",
            "Fix names, titles, and dates from the Chinese.",
            "Derive small-script sign values from the anchors.",
            "Read unanchored epitaphs with the derived values.",
            "Treat large-script passages with separate, tentative values.",
            "Mark every reading with its confidence level.",
        ],
        "confirm": [
            "Anchored passages keep their sense across the epitaph corpus.",
            "Transcribed Khitan vocabulary matches the derived readings.",
            "New epitaph finds continue to yield to the parallel method.",
        ],
        "refute": [
            "If Chinese parallels were free compositions, the anchors would drift.",
            "If small-script values failed on unanchored texts, the system would be parallel-bound.",
            "If the language identification were wrong, the vocabulary would not cohere.",
        ],
        "not_claims": [
            "It does not claim the large script is deciphered - it is not.",
            "It does not claim Khitan has a living check - the language is extinct.",
            "It does not present tentative readings as secure.",
        ],
        "citations": [CIT_KARA, CIT_ROBINSON],
        "demo_sample": "LIAO-TOMB-LIAO-SCRIPT-LIAO",
        "demo_anchor": "LIAO",
    },
    {
        "key": "tangut-script",
        "name": "Tangut Script",
        "group": "Partially Deciphered Scripts",
        "ladder_rank": 22,
        "ladder_tier": "compounded",
        "script": "Tangut (Xixia)",
        "status": "partially deciphered",
        "problem": ("Six thousand labyrinthine characters, each a maze of "
                    "strokes, invented for an empire erased by Genghis "
                    "Khan. The problem was to map the most complex script "
                    "ever devised - without native speakers, without a "
                    "Rosetta, using dictionaries the Tanguts wrote for "
                    "themselves."),
        "background": (
            "The Tangut or Xixia script was created in 1036 for the "
            "Western Xia empire, with some 6,000 characters of extreme "
            "visual complexity. The empire was destroyed by the Mongols "
            "in 1227, and the script died with its readers. The "
            "decipherment rests on bilingual dictionaries the Tanguts "
            "themselves compiled - notably the Fan Han Heshi Zhang "
            "Zhongzhu, a Tangut-Chinese glossary - plus Buddhist sutras "
            "translated into Tangut from known Chinese originals. "
            "E. Grinstead's 1972 Analysis of the Tangut Script "
            "systematized the character structure, and ongoing work "
            "continues to refine readings. The script is now largely "
            "readable: the dictionaries give pronunciations and meanings "
            "that the sutra parallels confirm."),
        "why_it_matters": ("Tangut proves that a dead empire's own "
                           "dictionaries can substitute for a bilingual, "
                           "and it sets the complexity record: no script "
                           "asks more of the solver's eyes. It teaches "
                           "the glossary-first method."),
        "method": ("First, mine the Tangut-Chinese glossaries for "
                   "character readings and meanings. Second, align Tangut "
                   "sutra translations with their known Chinese originals "
                   "as parallel-text checks. Third, analyze character "
                   "structure into recurring components to reduce the "
                   "6,000 to manageable patterns. Fourth, test the "
                   "glossary values on administrative documents. Fifth, "
                   "refine pronunciations through fanqie-style spelling "
                   "evidence in the glossaries."),
        "readings": [
            "The glossaries give Tangut readings directly from the scribes themselves.",
            "Sutra parallels confirm the glossary values in running text.",
            "Character-component analysis reduces 6,000 mazes to recurring patterns.",
        ],
        "translations": [
            "Sutra translations: Buddhist texts paralleled against Chinese originals.",
            "Administrative documents: the empire's records, largely readable.",
        ],
        "sig_pointer": ("The Signature edition re-derives the "
                        "glossary-first method as a labeled exercise on "
                        "solved material, stating assumptions openly and "
                        "claiming no new readings."),
        "assumptions": [
            "A1: The glossaries record genuine Tangut readings (documented source).",
            "A2: Sutra translations follow known Chinese originals (documented parallel).",
            "A3: Character components recur systematically (Grinstead's documented analysis).",
            "A4: Administrative texts test the glossary values (documented method).",
        ],
        "steps": [
            "Extract readings and meanings from the Tangut-Chinese glossaries.",
            "Align sutra translations with their Chinese originals.",
            "Decompose characters into recurring structural components.",
            "Test the values on administrative documents.",
            "Refine pronunciations with the glossaries' spelling evidence.",
            "Verify the full range of genres reads coherently.",
        ],
        "confirm": [
            "Sutra parallels confirm glossary values across thousands of characters.",
            "Administrative documents read coherently with the same values.",
            "Newly identified texts continue to yield to the glossary method.",
        ],
        "refute": [
            "If the glossaries were corrupt, the foundation values would be wrong.",
            "If sutra translations were free, the parallel checks would mislead.",
            "If components did not recur, the 6,000 characters would stay atomic.",
        ],
        "not_claims": [
            "It does not claim every character is certain - refinements continue.",
            "It does not claim Tangut pronunciation is fully recovered.",
            "It does not claim the re-derivation revises Grinstead's analysis.",
        ],
        "citations": [CIT_GRINSTEAD, CIT_NIE, CIT_ROBINSON],
        "demo_sample": "XIXIA-DICTIONARY-XIXIA-SUTRA",
        "demo_anchor": "XIXIA",
    },
    {
        "key": "linear-a",
        "name": "Linear A",
        "group": "Undeciphered Scripts",
        "ladder_rank": 23,
        "ladder_tier": "advanced",
        "script": "Linear A",
        "status": "undeciphered",
        "problem": ("The writing of the Minoans - the civilization that "
                    "built the palaces of Crete - in a script whose signs "
                    "look like Linear B but whose language is not Greek. "
                    "The problem is the most famous unsolved decipherment "
                    "in Europe: familiar signs, unknown tongue, no "
                    "bilingual."),
        "background": (
            "Linear A was used on Crete from about 1800 to 1450 BCE for "
            "the Minoan language, surviving in some 1,400 inscriptions, "
            "mostly administrative tablets and inscribed ritual vessels. "
            "Many signs resemble Linear B, and scholars can assign "
            "tentative phonetic values by analogy - but the underlying "
            "language is not Greek, so the values produce pronounceable "
            "nonsense. The corpus is small and formulaic: libation "
            "formulas repeat on stone vessels, and tablets list "
            "commodities. Louis Godart and Jean-Pierre Olivier's corpus "
            "organized the texts. Proposed identifications of the "
            "language - Semitic, Indo-European, Tyrsenian - remain "
            "unproven. Linear A is the archetype of the "
            "readable-signs-unknown-language problem."),
        "why_it_matters": ("Linear A guards the Minoans' own voice: "
                           "solving it would reveal Europe's first "
                           "civilization in its own words. It teaches the "
                           "analogy trap - Linear B values are a "
                           "hypothesis here, not a reading - and the "
                           "discipline of working a formulaic corpus."),
        "method": ("Documented scholarly method, no established solution: "
                   "first, catalog the sign inventory against Linear B "
                   "lookalikes, marking every analogy as tentative. "
                   "Second, isolate the repeated libation formulas on "
                   "stone vessels as the structural anchors. Third, map "
                   "commodity signs and numerals in the tablets, where "
                   "the administrative sense constrains the content. "
                   "Fourth, test language-family hypotheses against the "
                   "tentative readings without committing to any. Fifth, "
                   "publish every step as hypothesis, never as "
                   "decipherment."),
        "readings": [
            "Sign-by-analogy values from Linear B are tentative hypotheses, not readings.",
            "Libation formulas repeat with fixed structure on the stone vessels.",
            "Commodity signs and numerals give the tablets' administrative skeleton.",
        ],
        "translations": [
            "No established translation exists - the script is undeciphered.",
            "Proposed (unproven): libation formulas read as dedications by analogy with Linear B values.",
        ],
        "sig_pointer": ("The Signature edition offers a labeled "
                        "Signature-generated proposed reading of the "
                        "libation formulas, opened with the exact honesty "
                        "label, built step by step from stated "
                        "assumptions - and bounded: it claims no real "
                        "decipherment of Linear A."),
        "assumptions": [
            "A1: Linear B lookalike signs may carry related values (tentative analogy, not fact).",
            "A2: The stone-vessel texts are dedicatory formulas (structural hypothesis).",
            "A3: Tablet commodity signs follow administrative logic (documented genre).",
            "A4: Every value in the proposal is labeled hypothetical (honesty rule).",
        ],
        "steps": [
            "Catalog the Linear A signs against their Linear B lookalikes.",
            "Mark each analogy-derived value as tentative.",
            "Isolate the repeated vessel formulas and segment their slots.",
            "Assign the tentative values to the formula slots.",
            "Test the resulting strings against language-family hypotheses.",
            "Report the reading as a labeled proposal with all uncertainties marked.",
        ],
        "confirm": [
            "If a bilingual or long parallel text surfaced, the tentative values could be tested.",
            "Consistent formula structure across the vessels supports the segmentation.",
            "Commodity logic in the tablets constrains at least the administrative content.",
        ],
        "refute": [
            "If Linear B analogies are false friends, the values are pure fiction.",
            "If the language belongs to no tested family, the hypothesis tests prove nothing.",
            "Any claim of full decipherment without new evidence would be exposed as overreach.",
        ],
        "not_claims": [
            "It does not claim Linear A is deciphered - it is not.",
            "It does not present analogy values as readings.",
            "It does not endorse any language-family identification.",
        ],
        "citations": [CIT_GORILA, CIT_SCHOEP, CIT_ROBINSON],
        "demo_sample": "HAGIATRIDA-TABLET-HAGIATRIDA",
        "demo_anchor": "HAGIATRIDA",
    },
    {
        "key": "indus-script",
        "name": "The Indus Script",
        "group": "Undeciphered Scripts",
        "ladder_rank": 24,
        "ladder_tier": "advanced",
        "script": "Indus (Harappan) script",
        "status": "undeciphered",
        "problem": ("Four thousand seal inscriptions from the Bronze Age "
                    "cities of the Indus valley, averaging five signs "
                    "each, with no bilingual, no long texts, and no known "
                    "language. The problem is the heaviest unsolved "
                    "decipherment on Earth: the shortest corpus per sign "
                    "of any major script."),
        "background": (
            "The Indus script was used from about 2600 to 1900 BCE across "
            "the Harappan civilization's cities - Mohenjo-daro, Harappa, "
            "Dholavira - surviving on some 4,000 inscribed objects, "
            "mostly steatite seals. The average inscription is just five "
            "signs long; the longest single surface carries 26. There are "
            "about 400 distinct signs, and no bilingual text exists. "
            "Asko Parpola's Dravidian hypothesis, reading the script as "
            "an early Dravidian language, is the most developed proposal "
            "but remains unproven. Farmer, Sproat, and Witzel controversially "
            "argued the signs may be non-linguistic symbols rather than "
            "writing at all. The brevity of the texts is the fundamental "
            "obstacle: five-sign seals cannot carry the redundancy that "
            "decipherment feeds on."),
        "why_it_matters": ("The Indus script guards the voice of South "
                           "Asia's first urban civilization. It teaches "
                           "the corpus-brevity limit - the mathematical "
                           "reason some scripts may never be solved - and "
                           "the honesty of admitting it."),
        "method": ("Documented scholarly approaches, no established "
                   "solution: first, build the complete sign concordance "
                   "across all 4,000 inscriptions. Second, analyze sign "
                   "order statistics to test whether the sequences behave "
                   "like language. Third, isolate the unicorn-seal "
                   "formulas and the repeated sign clusters. Fourth, test "
                   "the Dravidian hypothesis against the clusters with "
                   "Old Tamil and Brahui cognates. Fifth, report every "
                   "result as statistical or hypothetical, never as a "
                   "reading."),
        "readings": [
            "About 400 distinct signs are cataloged across the corpus.",
            "The average text is five signs; the longest single text is 26 signs.",
            "No bilingual and no long text exist anywhere in the corpus.",
        ],
        "translations": [
            "No established translation exists - the script is undeciphered.",
            "Proposed (unproven, Parpola): seal formulas as Dravidian name-and-title strings.",
        ],
        "sig_pointer": ("The Signature edition offers a labeled "
                        "Signature-generated proposed reading of the seal "
                        "formulas, opened with the exact honesty label, "
                        "built from stated assumptions - and bounded: it "
                        "claims no real decipherment of the Indus script."),
        "assumptions": [
            "A1: The sign sequences encode language (the mainstream hypothesis, contested).",
            "A2: Repeated clusters are formulas with fixed slots (structural hypothesis).",
            "A3: The Dravidian hypothesis is the test frame (Parpola's documented proposal).",
            "A4: Every derived value is labeled hypothetical (honesty rule).",
        ],
        "steps": [
            "Concord every sign occurrence across the 4,000 inscriptions.",
            "Compute order statistics to test for language-like behavior.",
            "Isolate the repeated formula clusters on the unicorn seals.",
            "Test Dravidian cognates against the cluster slots.",
            "Check whether any reading survives across the whole corpus.",
            "Report the result as a labeled statistical proposal.",
        ],
        "confirm": [
            "Language-like order statistics would support the linguistic hypothesis.",
            "A bilingual or long text would transform the problem overnight.",
            "Consistent formula slots across thousands of seals support the segmentation.",
        ],
        "refute": [
            "If the signs are non-linguistic symbols, all phonetic proposals are void.",
            "If the corpus is too brief for statistics, no proposal can be confirmed.",
            "Any full-decipherment claim without new evidence is overreach.",
        ],
        "not_claims": [
            "It does not claim the Indus script is deciphered - it is not.",
            "It does not endorse the Dravidian hypothesis as proven.",
            "It does not dismiss the non-linguistic-symbol argument.",
        ],
        "citations": [CIT_PARPOLA_INDUS, CIT_FARMER, CIT_ROBINSON],
        "demo_sample": "MOHENJODARO-SEAL-MOHENJODARO-UNICORN",
        "demo_anchor": "MOHENJODARO",
    },
    {
        "key": "cretan-hieroglyphs",
        "name": "Cretan Hieroglyphs",
        "group": "Undeciphered Scripts",
        "ladder_rank": 25,
        "ladder_tier": "advanced",
        "script": "Cretan Hieroglyphic",
        "status": "undeciphered",
        "problem": ("The Minoans' other script - picture-signs stamped on "
                    "seal stones, older than Linear A, in a corpus of "
                    "barely 300 documents. The problem is to read the "
                    "earliest Cretan writing from seal impressions shorter "
                    "than a sentence."),
        "background": (
            "Cretan Hieroglyphic was used on Crete from about 2100 to "
            "1700 BCE, before Linear A, surviving in roughly 300 "
            "documents - mostly seal stones and sealings, plus a few "
            "clay tablets and the Malia altar stone. The signs are "
            "pictographic: figures, animals, tools, and abstract shapes, "
            "about 100 distinct signs. Arthur Evans published the first "
            "corpus in Scripta Minoa. The texts are extremely short - "
            "seal inscriptions of a few signs - and no bilingual exists. "
            "The language is presumably Minoan, the same unknown tongue "
            "as Linear A. The script is the least-worked of the Aegean "
            "scripts, its brevity defeating every statistical approach "
            "so far."),
        "why_it_matters": ("Cretan Hieroglyphs are the deep root of "
                           "Aegean writing: solving them would illuminate "
                           "both Linear A and the Minoan world. They teach "
                           "the seal-corpus limit - when texts are three "
                           "signs long, method must be structural, not "
                           "statistical."),
        "method": ("Documented scholarly approaches, no established "
                   "solution: first, catalog the hundred signs across "
                   "all seal impressions. Second, group the seals by "
                   "recurring sign sequences, the formula candidates. "
                   "Third, compare the sequences with Linear A formulas "
                   "for structural parallels. Fourth, test the Malia "
                   "altar stone's longer text as the best hope for "
                   "connected sense. Fifth, keep every proposal labeled "
                   "as structural hypothesis."),
        "readings": [
            "About 100 distinct signs are cataloged, mostly from seals.",
            "Recurring sequences suggest formulaic seal legends.",
            "The Malia altar stone carries the longest known text.",
        ],
        "translations": [
            "No established translation exists - the script is undeciphered.",
            "Proposed (unproven): seal sequences as owner names and titles.",
        ],
        "sig_pointer": ("The Signature edition offers a labeled "
                        "Signature-generated proposed reading of the seal "
                        "formulas, opened with the exact honesty label and "
                        "bounded: it claims no real decipherment."),
        "assumptions": [
            "A1: Seal sequences are formulaic legends (structural hypothesis).",
            "A2: The language is Minoan, shared with Linear A (documented hypothesis).",
            "A3: The Malia altar stone is the best connected-text hope (documented).",
            "A4: Every proposal stays labeled hypothetical (honesty rule).",
        ],
        "steps": [
            "Catalog the sign inventory across all seal impressions.",
            "Cluster the seals by recurring sign sequences.",
            "Compare the clusters structurally with Linear A formulas.",
            "Segment the Malia altar stone text into candidate words.",
            "Test owner-name-and-title readings against the clusters.",
            "Report the reading as a labeled structural proposal.",
        ],
        "confirm": [
            "A longer text or bilingual would let the clusters be tested.",
            "Consistent formula structure across the seals supports the segmentation.",
            "Parallels with Linear A formulas would strengthen the Minoan link.",
        ],
        "refute": [
            "If seal legends are not formulas, the clustering proves nothing.",
            "If the language differs from Linear A's, the parallels mislead.",
            "Three-sign texts may simply be too short for any method.",
        ],
        "not_claims": [
            "It does not claim Cretan Hieroglyphic is deciphered - it is not.",
            "It does not present cluster readings as translations.",
            "It does not claim the corpus is sufficient for a solution.",
        ],
        "citations": [CIT_OLIVIER, CIT_Evans, CIT_ROBINSON],
        "demo_sample": "CRETAN-SEAL-CRETAN-PRISM-CRETAN-SEAL",
        "demo_anchor": "SEAL",
    },
    {
        "key": "proto-elamite-script",
        "name": "Proto-Elamite Script",
        "group": "Undeciphered Scripts",
        "ladder_rank": 26,
        "ladder_tier": "advanced",
        "script": "Proto-Elamite",
        "status": "undeciphered",
        "problem": ("Sixteen hundred clay tablets from the world's first "
                    "accounting offices, covered in numerical signs and "
                    "mysterious symbols - and the language behind them is "
                    "completely unknown. The problem is to read the "
                    "bookkeeping of a civilization that left no "
                    "dictionary."),
        "background": (
            "Proto-Elamite was used in southwestern Iran around 3100 to "
            "2900 BCE, contemporary with the earliest Sumerian writing, "
            "surviving in about 1,600 tablets, mostly from Susa. The "
            "tablets are administrative: they record numbers, grain, "
            "livestock, and labor with a complex numerical notation and "
            "some 1,400 distinct signs, many appearing only once. Jacob "
            "Dahl's work showed the numerical systems are sophisticated "
            "and commodity-specific - different goods are counted in "
            "different bases. The script is unrelated to later Elamite "
            "despite the name. Because the tablets are accounts, not "
            "narratives, and the language is unknown, the script is "
            "considered among the least likely ever to be fully read."),
        "why_it_matters": ("Proto-Elamite is writing at its most "
                           "practical and most opaque: it teaches the "
                           "numerical attack - when words fail, numbers "
                           "still speak - and the limits of reading "
                           "accounts without a language."),
        "method": ("Documented scholarly approaches, no established "
                   "solution: first, decode the numerical systems by "
                   "their internal arithmetic, following Dahl. Second, "
                   "separate numerical signs from the commodity and "
                   "name signs. Third, cluster tablets by commodity to "
                   "find the accounting formulas. Fourth, compare the "
                   "sign repertoire with proto-cuneiform for shared "
                   "origins. Fifth, report the numerical readings as "
                   "secure and everything else as hypothesis."),
        "readings": [
            "The numerical systems are decoded: commodity-specific bases are documented.",
            "About 1,400 distinct signs are cataloged, many singletons.",
            "Tablet clusters reveal the accounting formulas by commodity.",
        ],
        "translations": [
            "No established translation of the non-numerical text exists.",
            "Secure: the numerical notations and their commodity systems.",
        ],
        "sig_pointer": ("The Signature edition offers a labeled "
                        "Signature-generated proposed reading of the "
                        "accounting formulas, opened with the exact "
                        "honesty label, separating secure numerical "
                        "readings from hypothetical word readings."),
        "assumptions": [
            "A1: The tablets are administrative accounts (documented genre).",
            "A2: Dahl's numerical systems are the secure foundation (documented).",
            "A3: Commodity clusters reveal formula structure (structural hypothesis).",
            "A4: Non-numerical signs stay hypothetical (honesty rule).",
        ],
        "steps": [
            "Decode each tablet's numerical notation with Dahl's systems.",
            "Separate number signs from commodity and name signs.",
            "Cluster the tablets by commodity formula.",
            "Propose readings for the formula slots from the clusters.",
            "Compare the sign stock with proto-cuneiform for origins.",
            "Report numerical readings as secure and word readings as proposals.",
        ],
        "confirm": [
            "The numerical systems' internal consistency is the secure core.",
            "A bilingual or lexical text would unlock the word signs.",
            "Commodity logic constrains the formula slots tightly.",
        ],
        "refute": [
            "If the tablets are not accounts, the numerical foundation misleads.",
            "Singleton signs may never be readable - most appear once.",
            "Without the language, word-sign proposals stay untestable.",
        ],
        "not_claims": [
            "It does not claim Proto-Elamite is readable beyond the numbers.",
            "It does not present word-sign proposals as translations.",
            "It does not claim relation to later Elamite - there is none.",
        ],
        "citations": [CIT_DAHL, CIT_ROBINSON],
        "demo_sample": "SUSA-TABLET-SUSA-ACCOUNT-SUSA",
        "demo_anchor": "SUSA",
    },
    {
        "key": "rongorongo",
        "name": "Rongorongo",
        "group": "Undeciphered Scripts",
        "ladder_rank": 27,
        "ladder_tier": "advanced",
        "script": "Rongorongo",
        "status": "undeciphered",
        "problem": ("Wooden tablets from Easter Island, carved with rows "
                    "of bird-men and strange creatures in reverse "
                    "boustrophedon - the only indigenous script of "
                    "Polynesia. The problem is to read the last voices "
                    "of Rapa Nui from two dozen tablets whose makers are "
                    "gone."),
        "background": (
            "Rongorongo survives on about 25 wooden objects from Easter "
            "Island (Rapa Nui), carved with some 120 distinct signs in "
            "reverse boustrophedon - each line upside down relative to "
            "the last. The script was still in use when Europeans "
            "arrived, but the literate elite perished in the 19th "
            "century, and no one who could read it survived. Thomas "
            "Barthel's 1958 catalog organized the corpus; Konstantin "
            "Pozdniakov's structural work showed the texts have "
            "language-like repetition patterns. A few sequences may "
            "record lunar calendar information, but no reading is "
            "established. The tablets are among the most beautiful and "
            "most silent objects in epigraphy."),
        "why_it_matters": ("Rongorongo is the script that died with its "
                           "readers in living memory: it teaches the "
                           "reverse-boustrophedon reading order and the "
                           "tragedy of a decipherment that arrived one "
                           "generation too late."),
        "method": ("Documented scholarly approaches, no established "
                   "solution: first, establish the reverse-boustrophedon "
                   "reading order from the tablets' physical layout. "
                   "Second, catalog the 120 signs with Barthel's "
                   "numbering. Third, analyze repetition structure for "
                   "language-like patterns, following Pozdniakov. Fourth, "
                   "test the lunar-calendar hypothesis against the "
                   "repeating sequences. Fifth, keep every reading "
                   "labeled as structural hypothesis."),
        "readings": [
            "Reverse boustrophedon: alternate lines are inverted.",
            "Barthel's catalog numbers the 120-sign inventory.",
            "Repetition patterns behave like language, per structural analysis.",
        ],
        "translations": [
            "No established translation exists - the script is undeciphered.",
            "Proposed (unproven): some sequences as lunar calendar records.",
        ],
        "sig_pointer": ("The Signature edition offers a labeled "
                        "Signature-generated proposed reading of the "
                        "repeating sequences, opened with the exact "
                        "honesty label and bounded: it claims no real "
                        "decipherment of Rongorongo."),
        "assumptions": [
            "A1: Reverse boustrophedon is the reading order (documented layout).",
            "A2: Barthel's sign catalog is the standard inventory (documented).",
            "A3: Repetition structure is language-like (Pozdniakov's documented analysis).",
            "A4: Every reading stays labeled hypothetical (honesty rule).",
        ],
        "steps": [
            "Fix the reading order tablet by tablet from the line inversions.",
            "Number every sign with the Barthel catalog.",
            "Extract the repeating sequences across the corpus.",
            "Test the sequences against the lunar-calendar hypothesis.",
            "Propose structural readings for the most regular sequences.",
            "Report the proposal with all uncertainties marked.",
        ],
        "confirm": [
            "A surviving reader's account would settle the question - none exists.",
            "Calendar-like sequences repeating with lunar periods would support the hypothesis.",
            "Structural regularity across all 25 objects supports the formula approach.",
        ],
        "refute": [
            "If the texts are mnemonic rather than linguistic, phonetic proposals fail.",
            "If the calendar hypothesis is wrong, the sequences need a new frame.",
            "No living check exists, so proposals stay permanently tentative.",
        ],
        "not_claims": [
            "It does not claim Rongorongo is deciphered - it is not.",
            "It does not present sequence proposals as translations.",
            "It does not claim the calendar hypothesis is proven.",
        ],
        "citations": [CIT_BARTEL, CIT_POZD, CIT_ROBINSON],
        "demo_sample": "RONGORONGO-TABLET-RONGORONGO-BARTEL",
        "demo_anchor": "RONGORONGO",
    },
    {
        "key": "phaistos-disc",
        "name": "The Phaistos Disc",
        "group": "Undeciphered Scripts",
        "ladder_rank": 28,
        "ladder_tier": "advanced",
        "script": "Phaistos Disc signs",
        "status": "undeciphered",
        "problem": ("A clay disc from Minoan Crete, stamped with 241 "
                    "picture-signs in a spiral - the world's first "
                    "printed text, and unreadable. The problem is to "
                    "read 45 distinct stamped signs with no other "
                    "example of the script anywhere on Earth."),
        "background": (
            "The Phaistos Disc was found in 1908 at the Minoan palace "
            "of Phaistos, dating to about 1700 BCE. Its 241 signs were "
            "pressed with individual stamps into the clay before firing "
            "- a true printing technology, unique in the Bronze Age. "
            "The 45 distinct signs include figures, animals, plants, and "
            "tools, arranged in a spiral on both sides, with word-"
            "divider strokes grouping them. No other text in this "
            "script has ever been found, so the entire corpus is one "
            "object. Louis Godart's work organized the sign inventory. "
            "Dozens of claimed decipherments have been published; none "
            "has survived scrutiny, because a unique text cannot be "
            "cross-checked."),
        "why_it_matters": ("The Disc is the loneliest text in "
                           "archaeology: it teaches the unique-corpus "
                           "limit - with one document and no parallels, "
                           "no method can confirm itself - and the "
                           "discipline of resisting the urge to solve it "
                           "anyway."),
        "method": ("Documented scholarly approaches, no established "
                   "solution: first, catalog the 45 stamped signs with "
                   "their stamp identities. Second, segment the spiral "
                   "into word groups using the divider strokes. Third, "
                   "analyze the group structure for repeated formulas. "
                   "Fourth, compare individual signs with Cretan "
                   "Hieroglyphic and Linear A lookalikes, marked as "
                   "tentative. Fifth, treat every proposal as "
                   "unconfirmable by the unique-corpus limit."),
        "readings": [
            "45 distinct stamps are cataloged; dividers segment the spiral into groups.",
            "The stamping technique is Bronze Age printing, unique for its time.",
            "The corpus is exactly one object - no parallel text exists.",
        ],
        "translations": [
            "No established translation exists - the disc is undeciphered.",
            "Proposed (unproven, various): hymns, inventories, and game boards have all been claimed.",
        ],
        "sig_pointer": ("The Signature edition offers a labeled "
                        "Signature-generated proposed reading of the "
                        "spiral's formula groups, opened with the exact "
                        "honesty label and bounded by the unique-corpus "
                        "limit: it claims no real decipherment."),
        "assumptions": [
            "A1: Divider strokes segment word groups (structural hypothesis).",
            "A2: Repeated groups are formulas (structural hypothesis).",
            "A3: Sign lookalikes with other Aegean scripts are tentative (honesty rule).",
            "A4: The unique-corpus limit makes proposals unconfirmable (documented limit).",
        ],
        "steps": [
            "Catalog the 45 stamps and map every impression.",
            "Segment both spiral faces at the divider strokes.",
            "Extract the repeated group formulas.",
            "Compare signs tentatively with Aegean lookalikes.",
            "Propose structural readings for the formula groups.",
            "Report the proposal as unconfirmable by the unique-corpus limit.",
        ],
        "confirm": [
            "A second disc text would transform the problem - none has appeared.",
            "Consistent formula structure is the current best evidence.",
            "Stamp-identity analysis is secure; readings are not.",
        ],
        "refute": [
            "If the dividers are not word dividers, the segmentation fails.",
            "Published 'solutions' that ignore the unique-corpus limit are methodologically void.",
            "Any claimed reading that cannot be cross-checked stays a guess.",
        ],
        "not_claims": [
            "It does not claim the disc is deciphered - it is not.",
            "It does not endorse any published solution.",
            "It does not hide the unique-corpus limit.",
        ],
        "citations": [CIT_GODART_PH, CIT_Evans, CIT_ROBINSON],
        "demo_sample": "PHAISTOS-DISC-PHAISTOS-SPIRAL-PHAISTOS",
        "demo_anchor": "PHAISTOS",
    },
    {
        "key": "byblos-syllabary",
        "name": "The Byblos Syllabary",
        "group": "Undeciphered Scripts",
        "ladder_rank": 29,
        "ladder_tier": "advanced",
        "script": "Byblos syllabary (Byblia Grammata)",
        "status": "undeciphered",
        "problem": ("Ten inscriptions from the Bronze Age port of Byblos, "
                    "in a script of about 114 signs that looks like a "
                    "bridge between hieroglyphs and the alphabet. The "
                    "problem is to read the writing of the city that gave "
                    "the Bible its name - from a corpus you could fit on "
                    "a postcard."),
        "background": (
            "The Byblos script, published by Maurice Dunand in 1945 as "
            "the Byblia Grammata, survives in about ten inscriptions "
            "from Byblos in Lebanon, dating roughly 1800 to 1400 BCE, "
            "including bronze spatulas and stone tablets. Its 114 signs "
            "are pictographic, and their number suggests a syllabary. "
            "Several signs resemble Egyptian hieroglyphs, hinting at "
            "influence from Egypt, with which Byblos traded for "
            "centuries. No bilingual exists, and the language is "
            "unknown - possibly an early Semitic tongue, possibly not. "
            "The tiny corpus has defeated every statistical and "
            "comparative approach; the script remains fully "
            "undeciphered, a bridge script whose far shore is unknown."),
        "why_it_matters": ("Byblos may be the missing link between "
                           "Egyptian writing and the alphabet: solving it "
                           "would rewrite the history of the alphabet "
                           "itself. It teaches the bridge-script method - "
                           "testing influence from both shores - and the "
                           "micro-corpus limit."),
        "method": ("Documented scholarly approaches, no established "
                   "solution: first, catalog the 114 signs across the "
                   "ten inscriptions. Second, test the syllabary "
                   "hypothesis from the sign count. Third, compare "
                   "Egyptian-looking signs with hieroglyphic values, "
                   "marked tentative. Fourth, test a Semitic language "
                   "hypothesis against the sequences. Fifth, keep every "
                   "proposal labeled by the micro-corpus limit."),
        "readings": [
            "114 signs suggest a syllabary by inventory logic.",
            "Egyptian-looking signs hint at hieroglyphic influence.",
            "The corpus is ten inscriptions - the statistical floor.",
        ],
        "translations": [
            "No established translation exists - the script is undeciphered.",
            "Proposed (unproven): spatula texts as dedications or labels.",
        ],
        "sig_pointer": ("The Signature edition offers a labeled "
                        "Signature-generated proposed reading of the "
                        "spatula texts, opened with the exact honesty "
                        "label and bounded by the micro-corpus limit."),
        "assumptions": [
            "A1: The sign count indicates a syllabary (inventory hypothesis).",
            "A2: Egyptian influence is plausible from the trade record (documented context).",
            "A3: A Semitic language is the test hypothesis (documented proposal).",
            "A4: Ten inscriptions bound what can be claimed (documented limit).",
        ],
        "steps": [
            "Catalog all 114 signs across the ten inscriptions.",
            "Segment the spatula and tablet texts into candidate words.",
            "Test Egyptian hieroglyphic values on the lookalike signs.",
            "Test Semitic vocabulary against the sequences.",
            "Propose structural readings for the most regular texts.",
            "Report the proposal bounded by the micro-corpus limit.",
        ],
        "confirm": [
            "A new inscription or bilingual would transform the problem.",
            "Consistent syllabic behavior across the ten texts would support the hypothesis.",
            "Egyptian parallels, if systematic, would anchor the values.",
        ],
        "refute": [
            "If the sign count is inflated by variants, the syllabary claim fails.",
            "If the language is not Semitic, the vocabulary tests mislead.",
            "Ten texts may simply be too few for any confirmation.",
        ],
        "not_claims": [
            "It does not claim the Byblos script is deciphered - it is not.",
            "It does not present influence hypotheses as readings.",
            "It does not hide the micro-corpus limit.",
        ],
        "citations": [CIT_DUNAND, CIT_ROBINSON],
        "demo_sample": "BYBLOS-SPATULA-BYBLOS-INSCRIPTION",
        "demo_anchor": "BYBLOS",
    },
    {
        "key": "cypro-minoan-script",
        "name": "Cypro-Minoan Script",
        "group": "Undeciphered Scripts",
        "ladder_rank": 30,
        "ladder_tier": "advanced",
        "script": "Cypro-Minoan",
        "status": "undeciphered",
        "problem": ("Cyprus's Bronze Age script, written on clay balls, "
                    "cylinders, and tablets in three regional variants - "
                    "the ancestor of the readable Cypriot syllabary, but "
                    "itself unreadable. The problem is to read the "
                    "grandparent script from texts shorter than a shopping "
                    "list."),
        "background": (
            "Cypro-Minoan was used on Cyprus from about 1550 to 1050 "
            "BCE, surviving in some 250 objects - clay balls, cylinders, "
            "tablets, and a few longer texts - in three regional "
            "variants identified by Emilia Masson. It descends from "
            "Minoan writing traditions and is the ancestor of the "
            "Cypriot syllabary, which WAS deciphered in the 19th "
            "century and reads Greek. The cruel irony: the grandchild "
            "script is readable, the grandparent is not. The texts are "
            "short, the language is unknown - possibly an early form "
            "of the Eteocypriot language - and no bilingual exists. "
            "The script sits one generation from readability and will "
            "not cross."),
        "why_it_matters": ("Cypro-Minoan is decipherment's nearest miss: "
                           "a readable descendant proves the script "
                           "family works, yet the ancestor stays dark. "
                           "It teaches the descendant-back-projection "
                           "method and its limits."),
        "method": ("Documented scholarly approaches, no established "
                   "solution: first, separate the three regional "
                   "variants cataloged by Masson. Second, project the "
                   "Cypriot syllabary's values backward onto lookalike "
                   "signs, marked tentative. Third, analyze the clay-ball "
                   "texts as the most formulaic genre. Fourth, test the "
                   "Eteocypriot language hypothesis against the "
                   "sequences. Fifth, label every back-projection as "
                   "hypothesis, not reading."),
        "readings": [
            "Three regional variants are cataloged across 250 objects.",
            "The Cypriot syllabary descendant is fully readable Greek.",
            "Clay-ball texts show the most formulaic structure.",
        ],
        "translations": [
            "No established translation exists - the script is undeciphered.",
            "Proposed (unproven): clay-ball texts as administrative tallies.",
        ],
        "sig_pointer": ("The Signature edition offers a labeled "
                        "Signature-generated proposed reading of the "
                        "clay-ball formulas, opened with the exact "
                        "honesty label and bounded: it claims no real "
                        "decipherment."),
        "assumptions": [
            "A1: The three variants are regional hands of one script (Masson's documented analysis).",
            "A2: Cypriot syllabary values may project backward (tentative hypothesis).",
            "A3: Clay-ball texts are formulaic tallies (structural hypothesis).",
            "A4: Back-projections stay labeled hypothetical (honesty rule).",
        ],
        "steps": [
            "Separate the corpus into Masson's three variants.",
            "Project Cypriot syllabary values onto lookalike signs.",
            "Mark every projected value as tentative.",
            "Segment the clay-ball texts into formula slots.",
            "Test Eteocypriot vocabulary against the sequences.",
            "Report the reading as a labeled back-projection proposal.",
        ],
        "confirm": [
            "A bilingual or long text would let the projections be tested.",
            "Consistent formula slots across the clay balls support the segmentation.",
            "Systematic sign correspondences with the Cypriot syllabary would anchor values.",
        ],
        "refute": [
            "If the scripts' values shifted over five centuries, back-projection fails.",
            "If the language is not Eteocypriot-related, the vocabulary tests mislead.",
            "Short texts may defeat even correct values.",
        ],
        "not_claims": [
            "It does not claim Cypro-Minoan is deciphered - it is not.",
            "It does not present back-projections as readings.",
            "It does not claim the descendant's readability transfers.",
        ],
        "citations": [CIT_MASSON, CIT_ROBINSON],
        "demo_sample": "ENKOMI-TABLET-ENKOMI-CYLINDER",
        "demo_anchor": "ENKOMI",
    },
    {
        "key": "voynich-cipher",
        "name": "The Voynich Cipher",
        "group": "Undeciphered Scripts",
        "ladder_rank": 31,
        "ladder_tier": "advanced",
        "script": "Voynich manuscript script",
        "status": "undeciphered",
        "problem": ("Two hundred forty pages of unknown plants, unknown "
                    "constellations, and bathing women, written in a "
                    "script of 20-odd characters that has resisted every "
                    "cryptographer for a century - including wartime "
                    "codebreakers. The problem is the world's most famous "
                    "cipher: a manuscript that behaves like language but "
                    "reads like nothing."),
        "background": (
            "The Voynich Manuscript, carbon-dated to the early 15th "
            "century, contains about 240 vellum pages of herbal, "
            "astronomical, biological, and pharmaceutical sections in "
            "an unknown script of roughly 20 to 30 characters. Wilfrid "
            "Voynich acquired it in 1912; William Friedman, the great "
            "American cryptographer, judged it a constructed language "
            "or cipher. Statistical analysis shows the text has "
            "language-like entropy and word structure - it is not random "
            "- with two distinct scribal 'hands' or dialects identified "
            "by Currier. Every claimed solution, from Roger Bacon "
            "authorship to Nahuatl readings, has collapsed under "
            "scrutiny. The manuscript is the control case for humility: "
            "a century of brilliant failure."),
        "why_it_matters": ("The Voynich is the cipher that ate a century "
                           "of codebreakers: it teaches statistical "
                           "humility - language-like behavior is not a "
                           "reading - and the discipline of publishing "
                           "negative results."),
        "method": ("Documented scholarly approaches, no established "
                   "solution: first, transcribe the text with a standard "
                   "alphabet such as EVA. Second, compute the "
                   "statistical profile - entropy, word lengths, "
                   "repetition - against natural languages. Third, "
                   "separate Currier's two hands and test them "
                   "independently. Fourth, test cipher hypotheses - "
                   "substitution, constructed language, hoax - against "
                   "the statistics. Fifth, report the manuscript as "
                   "unsolved with the statistics documented."),
        "readings": [
            "The text is statistically language-like, not random.",
            "Two scribal hands or dialects are distinguishable.",
            "No proposed solution has survived statistical scrutiny.",
        ],
        "translations": [
            "No established translation exists - the manuscript is undeciphered.",
            "Proposed (unproven, various): herbal, cipher, and constructed-language readings all claimed.",
        ],
        "sig_pointer": ("The Signature edition offers a labeled "
                        "Signature-generated proposed reading of the "
                        "herbal section's structure, opened with the "
                        "exact honesty label and bounded: it claims no "
                        "real solution to the Voynich Manuscript."),
        "assumptions": [
            "A1: The EVA transcription is the standard working text (documented).",
            "A2: Language-like statistics do not equal readability (documented caution).",
            "A3: The two Currier hands are analyzed separately (documented method).",
            "A4: Every proposal stays labeled hypothetical (honesty rule).",
        ],
        "steps": [
            "Transcribe the sample folios with the standard alphabet.",
            "Compute entropy and word-structure statistics.",
            "Separate the two hands and profile each.",
            "Test substitution and constructed-language hypotheses.",
            "Propose a structural reading of the herbal section's layout.",
            "Report the proposal as unconfirmed against the statistics.",
        ],
        "confirm": [
            "A verified parallel text or key would settle the manuscript.",
            "A proposal predicting unseen folios' statistics would be strong evidence.",
            "Consistent decipherment across all four sections would convince skeptics.",
        ],
        "refute": [
            "If the text is a hoax or glossolalia, all linguistic proposals fail.",
            "A century of failed solutions is itself evidence of the difficulty.",
            "Any 'solution' that only reads cherry-picked pages is methodologically void.",
        ],
        "not_claims": [
            "It does not claim the Voynich is solved - it is not.",
            "It does not endorse any published solution.",
            "It does not mistake statistics for a reading.",
        ],
        "citations": [CIT_DIMPERIO, CIT_DALES, CIT_ROBINSON],
        "demo_sample": "VOYNICH-FOLIO-VOYNICH-HERBAL-VOYNICH",
        "demo_anchor": "VOYNICH",
    },
    {
        "key": "rohonc-codex",
        "name": "The Rohonc Codex",
        "group": "Undeciphered Scripts",
        "ladder_rank": 32,
        "ladder_tier": "advanced",
        "script": "Rohonc Codex script",
        "status": "undeciphered",
        "problem": ("Four hundred forty-eight pages of an unknown script "
                    "with ten times more symbols than any alphabet, bound "
                    "in a Hungarian library. The problem is to read a "
                    "codex that may be cipher, shorthand, or artificial "
                    "script - with illustrations of battles and religion "
                    "as the only context clues."),
        "background": (
            "The Rohonc Codex, held by the Hungarian Academy of Sciences, "
            "runs 448 pages in an unknown script of roughly 150 distinct "
            "symbols - far more than an alphabet needs, suggesting a "
            "syllabary, a cipher, or an artificial system. Its "
            "illustrations show Christian, pagan, and battle scenes, "
            "hinting at a religious or historical content. The paper "
            "appears early modern, but the script matches nothing known. "
            "Proposals range from a cipher for Hungarian or Romanian to "
            "an invented script. No page has been read with scholarly "
            "acceptance. The codex is the Voynich's less-famous sibling: "
            "longer, stranger in symbol count, and equally silent."),
        "why_it_matters": ("The Rohonc Codex is the symbol-count puzzle: "
                           "150 signs force the solver past the alphabet "
                           "hypothesis into syllabaries and ciphers. It "
                           "teaches the inventory-first rule at its most "
                           "extreme."),
        "method": ("Documented scholarly approaches, no established "
                   "solution: first, catalog the 150 symbols with a "
                   "standard numbering. Second, use the symbol count to "
                   "rule out a simple alphabet. Third, mine the "
                   "illustrations for context - battles, religious "
                   "scenes - as semantic anchors. Fourth, test cipher "
                   "hypotheses against the repetition statistics. Fifth, "
                   "keep every proposal labeled by the unsolved status."),
        "readings": [
            "About 150 distinct symbols are cataloged - too many for an alphabet.",
            "Illustrations suggest religious and historical content.",
            "No page has an accepted reading.",
        ],
        "translations": [
            "No established translation exists - the codex is undeciphered.",
            "Proposed (unproven, various): ciphered Hungarian or Romanian readings claimed.",
        ],
        "sig_pointer": ("The Signature edition offers a labeled "
                        "Signature-generated proposed reading of the "
                        "illustrated sections' structure, opened with the "
                        "exact honesty label and bounded: it claims no "
                        "real solution."),
        "assumptions": [
            "A1: The symbol inventory is about 150 (documented catalog).",
            "A2: A simple alphabet is ruled out by the count (documented logic).",
            "A3: Illustrations are semantic anchors (documented context).",
            "A4: Every proposal stays labeled hypothetical (honesty rule).",
        ],
        "steps": [
            "Catalog the symbols with consistent numbering.",
            "Rule out alphabetic hypotheses from the inventory size.",
            "Anchor illustrated pages to their scenes' likely content.",
            "Test syllabary and cipher models against repetition statistics.",
            "Propose structural readings for the most regular pages.",
            "Report the proposal as unconfirmed.",
        ],
        "confirm": [
            "A key, parallel text, or identified language would settle the codex.",
            "A model predicting unseen pages' statistics would be strong evidence.",
            "Illustration-text correlations, if systematic, would anchor readings.",
        ],
        "refute": [
            "If the script is artificial with no language behind it, linguistic proposals fail.",
            "If illustrations are decorative, the semantic anchors vanish.",
            "No accepted reading exists after full scholarly attention.",
        ],
        "not_claims": [
            "It does not claim the Rohonc Codex is solved - it is not.",
            "It does not endorse any cipher claim.",
            "It does not present illustration guesses as readings.",
        ],
        "citations": [CIT_NEMETH, CIT_VAV, CIT_ROBINSON],
        "demo_sample": "ROHONC-CODEX-ROHONC-PAGE-ROHONC",
        "demo_anchor": "ROHONC",
    },
    {
        "key": "vinca-symbols",
        "name": "The Vinca-Turdas Symbols",
        "group": "Undeciphered Scripts",
        "ladder_rank": 33,
        "ladder_tier": "advanced",
        "script": "Vinca-Turdas symbols",
        "status": "undeciphered",
        "problem": ("Seven thousand years ago, Neolithic farmers in "
                    "southeastern Europe incised abstract signs on "
                    "pottery - two millennia before Sumerian writing. "
                    "The problem is the deepest question in the field: "
                    "are these the world's oldest writing, or the "
                    "world's oldest symbols that are not writing at "
                    "all?"),
        "background": (
            "The Vinca-Turdas culture of the Balkans, flourishing "
            "around 5500 to 4500 BCE, left thousands of incised signs "
            "on pottery, figurines, and the famous Tartaria tablets. "
            "Marija Gimbutas and later Shan Winn cataloged the sign "
            "repertoire - over 200 distinct signs in Winn's corpus. "
            "The signs repeat in structured ways that suggest more "
            "than decoration, yet no long texts exist, no bilingual "
            "is possible, and the 'language' - if any - is 7,000 "
            "years gone. Scholars divide: some see proto-writing, "
            "some see a system of religious or ownership marks. The "
            "Tartaria tablets, three small clay pieces from Romania, "
            "are the most famous and most contested artifacts."),
        "why_it_matters": ("Vinca asks whether writing was invented once "
                           "or many times - and whether symbols must be "
                           "language to matter. It teaches the "
                           "writing-versus-marks boundary, the most "
                           "philosophical line in decipherment."),
        "method": ("Documented scholarly approaches, no established "
                   "solution: first, catalog the sign repertoire with "
                   "Winn's numbering. Second, analyze repetition and "
                   "combination statistics for language-like structure. "
                   "Third, map signs to archaeological context - "
                   "pottery types, figurines, tablets. Fourth, compare "
                   "the Tartaria tablets' signs with the wider corpus. "
                   "Fifth, report the writing-versus-marks question as "
                   "open, with evidence on both sides."),
        "readings": [
            "Over 200 distinct signs are cataloged in the corpus.",
            "Signs repeat in structured combinations, beyond random decoration.",
            "The Tartaria tablets are the most famous and most contested pieces.",
        ],
        "translations": [
            "No established translation exists - the system may not be writing.",
            "Proposed (unproven): the signs as proto-writing or ritual marks.",
        ],
        "sig_pointer": ("The Signature edition offers a labeled "
                        "Signature-generated proposed reading of the "
                        "Tartaria tablet signs, opened with the exact "
                        "honesty label and bounded by the "
                        "writing-versus-marks question."),
        "assumptions": [
            "A1: Winn's sign catalog is the standard inventory (documented).",
            "A2: Structured repetition exceeds decoration (documented analysis).",
            "A3: Archaeological context constrains the signs' function (documented method).",
            "A4: The writing question stays open (documented field status).",
        ],
        "steps": [
            "Catalog the signs with the standard numbering.",
            "Compute repetition and combination statistics.",
            "Map each sign group to its archaeological context.",
            "Analyze the Tartaria tablets against the wider corpus.",
            "Propose structural readings for the most regular sequences.",
            "Report the proposal with the writing question marked open.",
        ],
        "confirm": [
            "A long text or bilingual would settle the writing question.",
            "Language-like statistics across the corpus would support proto-writing.",
            "Contextual regularity - same signs, same pottery types - supports systematic use.",
        ],
        "refute": [
            "If the signs are owners' marks, linguistic proposals fail.",
            "If the Tartaria tablets are intrusive or misdated, the famous case collapses.",
            "Seven thousand years without a language makes confirmation nearly impossible.",
        ],
        "not_claims": [
            "It does not claim Vinca is writing - the question is open.",
            "It does not present sign proposals as readings.",
            "It does not claim the Tartaria tablets are securely dated.",
        ],
        "citations": [CIT_WINN, CIT_ROBINSON],
        "demo_sample": "TARTARIA-TABLET-VINCA-SYMBOL-TARTARIA",
        "demo_anchor": "TARTARIA",
    },
    {
        "key": "cascajal-block",
        "name": "The Cascajal Block",
        "group": "Undeciphered Scripts",
        "ladder_rank": 34,
        "ladder_tier": "advanced",
        "script": "Cascajal Block signs",
        "status": "undeciphered",
        "problem": ("A serpentine block the size of a placemat, pulled "
                    "from a Mexican quarry in the 1990s, carrying 62 "
                    "signs in no obvious order - potentially the oldest "
                    "writing in the Americas. The problem is to read 62 "
                    "signs that may predate every other American script "
                    "by centuries."),
        "background": (
            "The Cascajal Block was recovered from the Arroyo Pesquero "
            "quarry in Veracruz, Mexico, and published in Science in "
            "2006 by Rodriguez Martinez and colleagues, who dated it to "
            "about 900 BCE - Olmec, centuries before the Maya script. "
            "Its 62 signs include depictions of plants, animals, and "
            "abstract forms, arranged without clear linear order. Some "
            "scholars accept it as the earliest American writing; "
            "others question the date, the context, or whether the "
            "signs constitute writing at all. The block is a unique "
            "object with no parallel text. Its 62 signs are the entire "
            "corpus of their tradition - if tradition it is."),
        "why_it_matters": ("Cascajal is the newest great mystery and the "
                           "most contested: it teaches the authentication "
                           "problem - before solving a text, prove the "
                           "text is what it claims to be - and the "
                           "unique-corpus limit at its sharpest."),
        "method": ("Documented scholarly approaches, no established "
                   "solution: first, document the 62 signs with "
                   "photography and drawing. Second, analyze the "
                   "arrangement for reading order - or its absence. "
                   "Third, compare individual signs with later "
                   "Mesoamerican scripts for continuities. Fourth, "
                   "scrutinize the archaeological context and dating "
                   "with full skepticism. Fifth, keep the "
                   "writing-versus-marks question and the dating "
                   "question both open."),
        "readings": [
            "62 distinct signs are documented on the single block.",
            "The arrangement shows no clear linear reading order.",
            "The 900 BCE date and Olmec attribution are both contested.",
        ],
        "translations": [
            "No established translation exists - the block is undeciphered.",
            "Proposed (unproven): the signs as early Mesoamerican writing.",
        ],
        "sig_pointer": ("The Signature edition offers a labeled "
                        "Signature-generated proposed reading of the "
                        "block's sign groups, opened with the exact "
                        "honesty label and bounded by the authentication "
                        "and unique-corpus limits."),
        "assumptions": [
            "A1: The 62 signs are documented from the published record.",
            "A2: The reading order is unknown and must not be assumed.",
            "A3: The date and context are contested (documented debate).",
            "A4: Every proposal stays labeled hypothetical (honesty rule).",
        ],
        "steps": [
            "Document each of the 62 signs from the published record.",
            "Map the spatial arrangement without assuming an order.",
            "Compare signs with later Mesoamerican scripts for continuities.",
            "Scrutinize the dating and context claims.",
            "Propose structural groupings for the sign clusters.",
            "Report the proposal with authentication marked open.",
        ],
        "confirm": [
            "A second block or related text would transform the problem.",
            "Secure dating and context would settle the authentication question.",
            "Systematic continuities with later scripts would support the writing claim.",
        ],
        "refute": [
            "If the date is wrong, the 'oldest writing' claim collapses.",
            "If the signs are not writing, all readings are void.",
            "A unique object cannot confirm its own decipherment.",
        ],
        "not_claims": [
            "It does not claim the block is writing - the question is open.",
            "It does not claim the 900 BCE date is secure - it is contested.",
            "It does not present sign groupings as readings.",
        ],
        "citations": [CIT_RODRIGUEZ, CIT_ROBINSON],
        "demo_sample": "CASCAJAL-BLOCK-CASCAJAL-SERPENTINE",
        "demo_anchor": "CASCAJAL",
    },
]
