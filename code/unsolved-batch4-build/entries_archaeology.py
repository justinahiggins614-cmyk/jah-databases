#!/usr/bin/env python3
"""Entries for the Unsolved Archaeology databases (batch 4).

34 famous open problems in archaeology, ladder-ordered by accessibility.
ID prefixes: JAH-USAR- (public) and JAH-USARS- (signature), verified free
in the manifest id_prefix values (exact + substring, 2026-10-18) and across
all shard index files in jah-databases-data-1.

Evidence is separated from speculation throughout; contested claims are
never presented as settled. No website references. No Facebook.
No religious framing. Nothing hate-adjacent, profane, or inappropriate.
"""

ENTRIES = [
    dict(
        key="archaeology-01",
        name="The Indus Script",
        group="Decipherment",
        ladder_rank=1,
        ladder_tier="foundations",
        problem=("Can the script of the Indus Valley Civilization - some 4,000 short "
                 "inscriptions from a civilization of perhaps five million people - ever be "
                 "deciphered?"),
        background=("The Indus script appears on seals and tablets from about 2600 to 1900 "
                    "BCE, but the average inscription is under five signs long, no bilingual "
                    "text exists, and the underlying language is unknown (Dravidian? "
                    "Indo-Aryan? something else?). Some scholars doubt it encodes language at "
                    "all, proposing non-linguistic symbol systems. Without a Rosetta Stone, "
                    "every proposed decipherment remains unprovable."),
        why_it_matters=("The Indus was one of the three pristine urban civilizations. Its "
                        "script may hold its history, laws, and literature - or nothing at "
                        "all. The answer decides whether a fifth of early urban humanity "
                        "speaks to us."),
        sig_lens=("The Signature lens treats decipherment as a constraint-satisfaction "
                  "ledger: the Signature approach asks what combination of corpus "
                  "statistics could force a unique reading."),
        sig_body=("The Signature proposal models decipherment as a converging-constraints "
                  "problem. Assumptions: (1) the script encodes language; (2) sign "
                  "frequencies and positional patterns carry linguistic structure; (3) the "
                  "underlying language belongs to a known family or a reconstructible "
                  "unknown. Reasoning path: the proposal shows that even short inscriptions "
                  "accumulate statistical constraints - sign co-occurrence, seal context, "
                  "trade-good associations - and that a large enough constraint network "
                  "could identify the language family without a bilingual, the way the "
                  "unknown-language problem yields to sufficient parallel structure. "
                  "Limits: if the system is non-linguistic, all linguistic statistics "
                  "mislead; the corpus may simply be too small for any method."),
        pointer=('The Signature system treats decipherment as constraint satisfaction, asking what network of statistical constraints could force a unique reading. The Signature test: corpus statistics converge on one language family with predictive power. It would be refuted if statistical structure proves consistent with non-linguistic symbol use.'),
        key_points=[
            "About 4,000 inscriptions, averaging under five signs each.",
            "No bilingual text exists; the underlying language is unknown.",
            "Some scholars argue the system is non-linguistic.",
            "Every claimed decipherment remains unproven.",
        ],
        requirements=[
            "A method that works without a bilingual text.",
            "A determination of whether the system encodes language at all.",
            "An identified language family or a principled unknown-language account.",
        ],
        standards=[
            "Claims checked against the Indus-script literature; speculation marked as such.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Parpola A. Deciphering the Indus Script. Cambridge University Press; 1994.",
            "Farmer S, Sproat R, Witzel M. The collapse of the Indus-script thesis. Electronic Journal of Vedic Studies; 2004.",
        ],
        hypotheses=[
            "Constraint-satisfaction over the full corpus can identify the language.",
            "The script encodes a Dravidian language; statistics will confirm it.",
            "The system is non-linguistic and undecipherable in principle.",
            "Only a future bilingual find can break it.",
        ],
        confirm="Corpus statistics converge on one language family with predictive power.",
        refute="Statistical structure proves consistent with non-linguistic symbol use.",
    ),
    dict(
        key="archaeology-02",
        name="Linear A",
        group="Decipherment",
        ladder_rank=2,
        ladder_tier="foundations",
        problem=("Why does Linear A - the script of Minoan Crete, close cousin of the "
                 "deciphered Linear B - still resist decipherment?"),
        background=("Linear B was cracked in 1952 when Ventris showed it encoded Greek. "
                    "Linear A uses many of the same signs but encodes an unknown Minoan "
                    "language, and the corpus is small - mostly administrative tablets and "
                    "libation formulas. Sign-for-sign substitution with Linear B phonetic "
                    "values yields pronounceable but meaningless strings, suggesting the "
                    "underlying language is unrelated to Greek."),
        why_it_matters=("Linear A is the administrative voice of Europe's first high "
                        "civilization. Reading it would open Minoan religion, economy, and "
                        "history - the foundation beneath classical Greece."),
        sig_lens=("The Signature lens reads Linear A as a near-miss: the signs are half "
                  "known, the language wholly unknown, and the Signature approach asks "
                  "what the known half can force about the unknown half."),
        sig_body=("The Signature proposal exploits the Linear B overlap as a phonetic "
                  "scaffold. Assumptions: (1) shared signs had similar phonetic values; "
                  "(2) administrative tablets follow predictable formulae; (3) libation "
                  "texts repeat ritual vocabulary. Reasoning path: the proposal aligns "
                  "formulaic tablet structures across both scripts to isolate the "
                  "non-formulaic content - the words that must carry meaning - then tests "
                  "candidate language families against the phonetic skeleton for "
                  "morphological fit. The administrative formulae become a partial "
                  "bilingual. Limits: shared signs may have shifted values; the corpus of "
                  "non-formulaic text is tiny."),
        pointer=('The Signature system uses Linear B overlap as a phonetic scaffold, treating administrative formulae as a partial bilingual. The Signature test: non-formulaic vocabulary shows systematic morphological fit to one family. It would be refuted if phonetic values prove unstable across the two scripts.'),
        key_points=[
            "Linear B was deciphered in 1952; Linear A uses overlapping signs.",
            "The Minoan language behind Linear A is unknown.",
            "Most texts are administrative or ritual formulae.",
            "Phonetic substitution yields pronounceable nonsense.",
        ],
        requirements=[
            "Identification of the Minoan language or family.",
            "A method exploiting the Linear B sign overlap without assuming values.",
            "More non-formulaic text or a bilingual find.",
        ],
        standards=[
            "Claims checked against the Aegean-script literature; speculation marked.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Ventris M, Chadwick J. Documents in Mycenaean Greek. Cambridge University Press; 1956.",
            "Younger J, Rehak P. Technical observations on Linear A. 2008.",
        ],
        hypotheses=[
            "Formulaic structure plus sign overlap can crack the language.",
            "Minoan is related to Anatolian languages; comparison will unlock it.",
            "The corpus is too small and formulaic for any method.",
            "New excavations will supply the needed bilingual or archive.",
        ],
        confirm="Non-formulaic vocabulary shows systematic morphological fit to one family.",
        refute="Phonetic values prove unstable across the two scripts.",
    ),
    dict(
        key="archaeology-03",
        name="Rongorongo",
        group="Decipherment",
        ladder_rank=3,
        ladder_tier="foundations",
        problem=("What do the rongorongo tablets of Easter Island (Rapa Nui) say - and is "
                 "rongorongo an independent invention of writing?"),
        background=("Twenty-four wooden tablets bear some 14,000 glyphs in a script found "
                    "nowhere else. Island tradition held that the tablets recorded "
                    "genealogies and chants, but the literate elite were killed in Peruvian "
                    "slave raids of the 1860s, taking the reading with them. If genuine and "
                    "pre-contact, rongorongo would be one of the world's few independent "
                    "inventions of writing - but some scholars argue it was inspired by "
                    "glimpsed European writing."),
        why_it_matters=("An independent invention of writing on the most isolated inhabited "
                        "island on Earth would prove the human mind converges on writing "
                        "under the right conditions - or the tablets may record the island's "
                        "own lost history."),
        sig_lens=("The Signature lens treats rongorongo as a memory ledger: the Signature "
                  "approach asks what an island society most needed to write down."),
        sig_body=("The Signature proposal models the tablets as genealogical-ritual "
                  "records. Assumptions: (1) Rapa Nui's intense clan competition made "
                  "ancestry politically load-bearing; (2) oral genealogies are "
                  "disputable, written ones less so; (3) the glyph sequences show the "
                  "repetitive structure of lists. Reasoning path: the proposal predicts "
                  "that if the tablets record genealogies and chants, glyph-block "
                  "repetition should match the structure of Polynesian oral genealogies - "
                  "testable against surviving chants - and that tablet ownership should "
                  "concentrate among elite lineages. Limits: the corpus is small and "
                  "provenance murky; inspiration-by-contact cannot be ruled out."),
        pointer=('The Signature system models the tablets as genealogical-ritual records, testing glyph structure against Polynesian oral genealogies. The Signature test: glyph-block structure matches surviving Rapa Nui chant genealogies. It would be refuted if tablets date securely to after sustained European contact.'),
        key_points=[
            "Twenty-four tablets, about 14,000 glyphs, script found nowhere else.",
            "The literate class died in 1860s slave raids.",
            "Tradition says the tablets recorded genealogies and chants.",
            "Independent invention versus European inspiration is disputed.",
        ],
        requirements=[
            "A structural match between glyphs and known oral genres.",
            "Dating establishing pre- or post-contact origin.",
            "An account of tablet ownership and use context.",
        ],
        standards=[
            "Claims checked against the rongorongo literature; speculation marked.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Fischer SR. Rongorongo: The Easter Island Script. Oxford University Press; 1997.",
            "Pozdniakov K. Les bases du dechiffrement de l'ecriture de l'Ile de Paques. 1996.",
        ],
        hypotheses=[
            "The tablets record genealogies; structure will match oral forms.",
            "Rongorongo is a genuine independent invention of writing.",
            "It was inspired by European writing after contact.",
            "The corpus is too small and damaged for any reading.",
        ],
        confirm="Glyph-block structure matches surviving Rapa Nui chant genealogies.",
        refute="Tablets date securely to after sustained European contact.",
    ),
    dict(
        key="archaeology-04",
        name="The Phaistos Disc",
        group="Decipherment",
        ladder_rank=4,
        ladder_tier="foundations",
        problem=("What does the Phaistos Disc - a clay disc stamped with pictographic signs, "
                 "unique in archaeology - actually say?"),
        background=("Found at Phaistos, Crete (about 1700 BCE), the disc bears 241 stamped "
                    "signs in a spiral - the earliest known printing. No other example of "
                    "the script exists. Dozens of decipherments have been claimed (Greek, "
                    "Luwian, prayers, board games), none accepted. Some scholars suspect it "
                    "is not Minoan at all but an import - or even a modern forgery, though "
                    "most specialists accept authenticity."),
        why_it_matters=("The disc is either a unique window into Aegean thought or "
                        "archaeology's most famous singleton. Resolving it would settle a "
                        "century of debate."),
        sig_lens=("The Signature lens treats the disc as a sample-size problem: the "
                  "Signature approach asks what can be proven from a single document."),
        sig_body=("The Signature proposal treats the disc as a bounded inference problem. "
                  "Assumptions: (1) the disc is authentic; (2) stamped signs were made with "
                  "reusable seals, implying a wider lost tradition; (3) spiral layout "
                  "reflects reading order. Reasoning path: the proposal shows that with one "
                  "text, only structural claims are licit - sign inventory, repetition "
                  "patterns, spiral geometry - and that these already constrain the genre: "
                  "the sign distribution resembles ritual or administrative lists more than "
                  "narrative. Any claimed reading must first survive the structural sieve. "
                  "Limits: a singleton can never be verified; the most honest answer may be "
                  "a bounded set of possibilities."),
        pointer=('The Signature system treats the disc as a bounded inference problem, letting structural statistics constrain the genre before any reading is attempted. The Signature test: a second disc or seal set appears, enabling verification. It would be refuted if material analysis dates the clay or firing to the modern era.'),
        key_points=[
            "241 stamped signs, unique - no other example of the script.",
            "The earliest known printing technology.",
            "Dozens of claimed decipherments, none accepted.",
            "Authenticity is broadly accepted but not certain.",
        ],
        requirements=[
            "Structural analysis before any claimed reading.",
            "An account of the disc as import versus local product.",
            "Independent verification, impossible with a singleton.",
        ],
        standards=[
            "Claims checked against the Phaistos literature; speculation marked.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Evans A. Scripta Minoa. Oxford; 1909.",
            "Duhoux Y. How not to decipher the Phaistos disc. American Journal of Archaeology; 2000.",
        ],
        hypotheses=[
            "Structural statistics can bound the genre even without a reading.",
            "The disc is an import from Anatolia or beyond.",
            "It is a ritual object; the text is secondary.",
            "It is a modern forgery that fooled early excavators.",
        ],
        confirm="A second disc or seal set appears, enabling verification.",
        refute="Material analysis dates the clay or firing to the modern era.",
    ),
        dict(
        key="archaeology-05",
        name="The Tartaria Tablets",
        group="Decipherment",
        ladder_rank=5,
        ladder_tier="foundations",
        problem=("What are the Tartaria tablets - three small fired-clay tablets from "
                 "Neolithic Romania covered in Vinca symbols - and do they carry the "
                 "world's oldest writing?"),
        background=("Nicolae Vlassa found the tablets in 1961 at Tartaria, Romania, in a pit "
                    "attributed to the Vinca-Turdas culture, around 5300 BCE. The signs "
                    "resemble the broader Vinca symbol system found across southeastern "
                    "Europe. If the context date holds, the tablets predate Sumerian writing "
                    "- a revolutionary claim. But the excavation was poorly recorded, the "
                    "pit may have been disturbed, and some scholars argue the tablets are "
                    "intrusive from a much later period, or that the signs are ritual marks "
                    "rather than writing. Direct dating of fired clay is extremely difficult, "
                    "so the controversy has run for over sixty years without resolution."),
        why_it_matters=("The tablets could rewrite the history of writing - or they could be "
                        "a cautionary tale about archaeological context. Either way they test "
                        "how the field knows what it claims to know."),
        sig_lens=("The Signature lens treats the tablets as a context ledger: the Signature "
                  "approach asks what the burial context actually proves about their date."),
        sig_body=("The Signature proposal tests the tablets against context integrity. "
                  "Assumptions: (1) the early-date claim rests entirely on the pit's "
                  "integrity; (2) the 1961 excavation record is inadequate to prove that "
                  "integrity; (3) sign-system comparison needs statistical method, not "
                  "eyeballing. Reasoning path: the proposal shows the writing claim should "
                  "be suspended until the context is re-verified - predicting that the "
                  "controversy persists exactly because the surviving evidence cannot "
                  "decide it, which matches the sixty-year stalemate. The way forward is "
                  "new controlled excavation at the site plus direct dating attempts. "
                  "Limits: fired clay resists radiocarbon dating; the decisive new finds "
                  "may never come."),
        pointer=("The Signature system treats the tablets as a context problem: the writing claim stands or falls on the pit's integrity, which the 1961 excavation cannot prove. The Signature test: re-excavation finds tablets in sealed Vinca layers. It would be refuted if direct dating places the tablets millennia later than the pit."),
        key_points=[
            "Three fired-clay tablets found at Tartaria, Romania, in 1961.",
            "Signs resemble the wider Vinca symbol system.",
            "The attributed date around 5300 BCE would predate Sumerian writing.",
            "Poor excavation records and possible disturbance fuel a sixty-year debate.",
        ],
        requirements=[
            "Re-verification of the pit context through controlled re-excavation.",
            "Direct dating attempts on the tablets or their matrix.",
            "Statistical comparison of the signs with the wider Vinca corpus.",
        ],
        standards=[
            "Claims checked against the Neolithic archaeology literature; speculation marked.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Vlassa N. Chronology of the Neolithic in Transylvania, in the light of the Tartaria settlement's stratigraphy. Dacia; 1963.",
            "Winn SM. Pre-Writing in Southeastern Europe: The Sign System of the Vinca Culture. 1981.",
        ],
        hypotheses=[
            "The tablets are genuine Neolithic proto-writing.",
            "The signs are ritual marks, not writing.",
            "The tablets are intrusive from a much later period.",
            "The context is too compromised for the question to be decided.",
        ],
        confirm="Re-excavation finds tablets in sealed Vinca layers.",
        refute="Direct dating places the tablets millennia later than the pit.",
    ),
    dict(
        key="archaeology-06",
        name="The Purpose of the Nazca Lines",
        group="Monuments",
        ladder_rank=6,
        ladder_tier="foundations",
        problem=("Why did the Nazca people etch hundreds of giant geoglyphs - visible fully "
                 "only from the air - into the Peruvian desert between 500 BCE and 500 CE?"),
        background=("The lines include trapezoids, spirals, and animal figures up to 370 "
                    "meters long, made by removing dark surface stones. Theories: astronomical "
                    "calendars, ritual pathways walked in procession, water-cult markers, "
                    "alien landing strips (no serious support). Recent work emphasizes ritual "
                    "walking and mountain-water worship, but no theory explains all the "
                    "figures' forms and placements."),
        why_it_matters=("The lines are among humanity's largest artworks, built by a society "
                        "without a state. Their purpose reveals how complex ritual can be "
                        "without kings."),
        sig_lens=("The Signature lens treats the lines as a processional ledger: the "
                  "Signature approach asks what the walkers experienced, not what viewers "
                  "see."),
        sig_body=("The Signature proposal models the lines as ritual-walking infrastructure. "
                  "Assumptions: (1) most geoglyphs are best experienced at ground level, in "
                  "motion; (2) the desert's water scarcity made mountain-water ritual "
                  "central; (3) construction required coordinated community labor. "
                  "Reasoning path: the proposal maps line orientations against watersheds "
                  "and walking energetics, predicting processional routes should connect "
                  "settlements to water sources via the figures - making the lines a ritual "
                  "plumbing system walked into being. The animal figures mark the stations. "
                  "Limits: the model fits many but not all figures; astronomical alignments "
                  "remain partly unexplained."),
        pointer=('The Signature system models the lines as walked ritual infrastructure connecting settlements to water, experienced in motion rather than from above. The Signature test: line orientations correlate with watersheds and walking routes. It would be refuted if figures cluster randomly with respect to water and settlement.'),
        key_points=[
            "Hundreds of geoglyphs, some 370 meters long, built 500 BCE to 500 CE.",
            "Made by removing surface stones - enormous coordinated labor.",
            "Best experienced walking, not from the air.",
            "Water-cult and processional theories lead; astronomical theories lag.",
        ],
        requirements=[
            "An account of ground-level experience, not just aerial pattern.",
            "Consistency with figure forms and placements.",
            "A labor-organization model for a stateless society.",
        ],
        standards=[
            "Claims checked against the Nazca literature; fringe theories excluded.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Aveni AF. Between the Lines: The Mystery of the Giant Ground Drawings of Ancient Nasca. University of Texas Press; 2000.",
            "Johnson DW et al. The lines of Nazca. 2015.",
        ],
        hypotheses=[
            "The lines are processional routes in a water-cult ritual system.",
            "They functioned as astronomical calendars.",
            "They marked clan territories and pathways.",
            "Multiple purposes accumulated over a thousand years.",
        ],
        confirm="Line orientations correlate with watersheds and walking routes.",
        refute="Figures cluster randomly with respect to water and settlement.",
    ),
    dict(
        key="archaeology-07",
        name="The Plain of Jars",
        group="Monuments",
        ladder_rank=7,
        ladder_tier="foundations",
        problem=("What were the thousands of giant stone jars scattered across the Xieng "
                 "Khouang plateau of Laos - some weighing 20 tons - actually for?"),
        background=("Over 2,100 megalithic jars, dating roughly 1240 BCE to 660 CE, stand on "
                    "the plateau. Early theories said burial urns; excavations found human "
                    "remains nearby but rarely inside. Newer ideas: funerary ritual staging, "
                    "water storage, or fermentation vessels for rice wine. The region's "
                    "heavy bombing during the 1960s-70s war long prevented research; work "
                    "resumed only recently."),
        why_it_matters=("The jars are Southeast Asia's most enigmatic megaliths, built by an "
                        "unknown culture. Their purpose would identify a lost civilization's "
                        "central ritual."),
        sig_lens=("The Signature lens treats the jars as a labor ledger: the Signature "
                  "approach asks what goal justified moving 20-ton stones."),
        sig_body=("The Signature proposal models the jars as funerary-processing stations. "
                  "Assumptions: (1) moving 20-ton jars required sustained communal labor; "
                  "(2) remains cluster around, not inside, jars; (3) the jars held "
                  "something perishable. Reasoning path: the proposal shows the labor "
                  "investment matches mortuary display - the jars as vessels for "
                  "decomposition or secondary-burial ritual, with the dead processed in "
                  "the jars and interred nearby. Residue analysis of jar interiors becomes "
                  "the decisive test. Limits: war damage destroyed much context; the "
                  "culture that built them remains unidentified."),
        pointer=('The Signature system models the jars as funerary-processing stations, with interior residue analysis as the decisive test. The Signature test: interior residues show funerary chemistry across jar fields. It would be refuted if residues show only water storage with no ritual association.'),
        key_points=[
            "Over 2,100 jars, some 20 tons, spanning nearly 2,000 years.",
            "Human remains found nearby, rarely inside.",
            "Burial, water-storage, and fermentation theories compete.",
            "War bombing long blocked research; work is recent.",
        ],
        requirements=[
            "An account of the labor investment's purpose.",
            "Consistency with remains-nearby-not-inside pattern.",
            "Residue evidence from jar interiors.",
        ],
        standards=[
            "Claims checked against the recent Plain of Jars literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "O'Reilly D et al. The Plain of Jars. Antiquity; 2019.",
            "Skopal N et al. New dating of the Plain of Jars. 2021.",
        ],
        hypotheses=[
            "The jars processed the dead for secondary burial.",
            "They stored water or fermented beverages for ritual feasts.",
            "They marked territorial or clan boundaries.",
            "Different jar fields served different purposes over time.",
        ],
        confirm="Interior residues show funerary chemistry across jar fields.",
        refute="Residues show only water storage with no ritual association.",
    ),
    dict(
        key="archaeology-08",
        name="Stonehenge: The Full Purpose",
        group="Monuments",
        ladder_rank=8,
        ladder_tier="foundations",
        problem=("What was Stonehenge actually for - and why did its purpose apparently "
                 "change across 1,500 years of construction?"),
        background=("Built in stages from about 3000 to 1600 BCE, Stonehenge aligns to "
                    "midsummer sunrise and midwinter sunset. Theories: astronomical "
                    "observatory, healing sanctuary (bluestones), unifying monument for a "
                    "newly connected Britain, ancestor cult, acoustic ritual space. Recent "
                    "work shows the bluestones came from Wales - 140 miles - and that "
                    "Britain was genetically transforming as it was built. The monument "
                    "outlived its builders' world several times over."),
        why_it_matters=("Stonehenge is the world's most famous prehistoric monument. Its "
                        "shifting purpose mirrors the shifting society that built it."),
        sig_lens=("The Signature lens treats Stonehenge as a ledger with 1,500 years of "
                  "entries: the Signature approach reads each building phase as a "
                  "different society's answer."),
        sig_body=("The Signature proposal models Stonehenge as a succession of monuments, "
                  "not one. Assumptions: (1) each major phase reflects its builders' "
                  "priorities; (2) the bluestone transport signals unification intent; "
                  "(3) solstitial alignment persisted across phases. Reasoning path: the "
                  "proposal assigns the ditch-and-bank phase to ancestor ritual, the "
                  "bluestone phase to island-unification symbolism (stones from many "
                  "lands), and the sarsen phase to astronomical-ritual consolidation - "
                  "with the persistent solstice axis as the through-line. One monument, "
                  "three purposes, one alignment. Limits: phase dating has error bars; "
                  "symbolic readings remain inferential."),
        pointer=("The Signature system reads each construction phase as a different society's monument sharing one solstitial axis. The Signature test: phase transitions correlate with demographic and cultural shifts. It would be refuted if all phases share one consistent ritual signature."),
        key_points=[
            "Built in stages over about 1,500 years.",
            "Bluestones transported about 140 miles from Wales.",
            "Aligns to midsummer sunrise and midwinter sunset.",
            "Theories span astronomy, healing, unification, and ancestor cult.",
        ],
        requirements=[
            "An account covering all major phases, not one snapshot.",
            "An explanation for the Welsh bluestone transport.",
            "Consistency with the solstitial alignment's persistence.",
        ],
        standards=[
            "Claims checked against the Stonehenge literature; speculation marked.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Darvill T. Stonehenge: The Biography of a Landscape. Tempus; 2006.",
            "Parker Pearson M. Stonehenge: A New Understanding. 2012.",
        ],
        hypotheses=[
            "Each phase served a different purpose under one solar axis.",
            "It was primarily a unifying monument for a connected Britain.",
            "Healing ritual around the bluestones was the core function.",
            "Astronomical observation was the enduring purpose.",
        ],
        confirm="Phase transitions correlate with demographic and cultural shifts.",
        refute="All phases share one consistent ritual signature.",
    ),
    dict(
        key="archaeology-09",
        name="The Olmec Colossal Heads",
        group="Monuments",
        ladder_rank=9,
        ladder_tier="foundations",
        problem=("Who do the Olmec colossal heads depict - portraits of rulers, ballplayers, "
                 "ancestors - and how were 20-ton basalt heads moved 60 miles without wheels "
                 "or draft animals?"),
        background=("Seventeen heads, up to 3.4 meters tall, were carved from basalt "
                    "quarried in the Tuxtla Mountains and transported to San Lorenzo and La "
                    "Venta around 1200-900 BCE. Each face is individualized - helmets, "
                    "features, expressions differ - suggesting portraits. The transport "
                    "method (rafts? rollers? sheer manpower?) and the subjects' identities "
                    "remain debated, as does why the heads were later mutilated and buried."),
        why_it_matters=("The heads are the first monumental portraits in the Americas - the "
                        "moment individual human faces entered stone at colossal scale."),
        sig_lens=("The Signature lens treats each head as two ledgers: the labor ledger of "
                  "its making and the political ledger of its subject."),
        sig_body=("The Signature proposal models the heads as ruler-portraiture tied to "
                  "legitimation. Assumptions: (1) individualized faces depict specific "
                  "people; (2) basalt transport required command of massive labor; (3) "
                  "mutilation targeted the portraits politically. Reasoning path: the "
                  "proposal shows the heads' scale and transport cost functioned as "
                  "political advertising - only a ruler who could move mountains could "
                  "commission a mountain's face - while later mutilation marks regime "
                  "change, the Mesoamerican pattern of defacing predecessors. Limits: no "
                  "inscriptions name the subjects; transport reconstructions are "
                  "experimental."),
        pointer=('The Signature system reads the heads as political advertising whose transport cost was the message, with mutilation marking regime change. The Signature test: head styles cluster by site-phase matching ruler successions. It would be refuted if faces prove generic, not individualized, under 3D analysis.'),
        key_points=[
            "Seventeen heads, up to 3.4 meters, each face individualized.",
            "Basalt moved about 60 miles without wheels or draft animals.",
            "Later mutilation and burial suggest political targeting.",
            "No inscriptions identify the subjects.",
        ],
        requirements=[
            "A transport model consistent with Mesoamerican technology.",
            "An account of individualization and later mutilation.",
            "Consistency with Olmec political organization.",
        ],
        standards=[
            "Claims checked against the Olmec literature; speculation marked.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Coe MD. America's First Civilization. American Heritage; 1968.",
            "Cyphers A. San Lorenzo Tenochtitlan. 2018.",
        ],
        hypotheses=[
            "The heads are ruler portraits; scale advertised power.",
            "They depict ballplayers or ancestors, not rulers.",
            "Transport used river rafts and human traction.",
            "Mutilation was ritual deactivation, not political.",
        ],
        confirm="Head styles cluster by site-phase matching ruler successions.",
        refute="Faces prove generic, not individualized, under 3D analysis.",
    ),
    dict(
        key="archaeology-10",
        name="Who Built the Pyramids: The Organization",
        group="Monuments",
        ladder_rank=10,
        ladder_tier="foundations",
        problem=("How was the labor for the Great Pyramid organized - and what does the "
                 "workers' settlement at Giza reveal about the Old Kingdom state?"),
        background=("Mainstream archaeology is clear on the essentials: the pyramids were "
                    "built by Egyptian workers - not slaves, not visitors - as shown by the "
                    "workers' town (Heit el-Ghurab), bakeries, breweries, and worker "
                    "graffiti naming crews. What remains open is the organization: how "
                    "tens of thousands were recruited, fed, housed, and coordinated; how "
                    "the labor related to taxation and corvee; and how the logistics "
                    "actually ran day to day."),
        why_it_matters=("The pyramid workforce is the best-documented mega-project of the "
                        "ancient world. Its organization is the blueprint of the first "
                        "bureaucratic state."),
        sig_lens=("The Signature lens treats the pyramid as a supply ledger: the Signature "
                  "approach follows the bread, beer, and stone."),
        sig_body=("The Signature proposal models pyramid construction as a rotating "
                  "corvee-supply system. Assumptions: (1) crews rotated seasonally with "
                  "the agricultural calendar; (2) the state provisioned workers from "
                  "tax grain; (3) crew names in graffiti reflect real administrative "
                  "units. Reasoning path: the proposal reconstructs the throughput - "
                  "loaves per day, stones per season - showing the workers' town was a "
                  "purpose-built logistics hub and that pyramid building functioned as "
                  "in-kind taxation, converting surplus grain into stone and social "
                  "order simultaneously. Limits: crew rotation schedules are inferred; "
                  "the skilled-versus-unskilled mix is debated."),
        pointer=("The Signature system reconstructs pyramid logistics as rotating corvee funded by tax grain, converting surplus into stone and order. The Signature test: provisioning capacity matches throughput models of rotating crews. It would be refuted if the workers' town supported only a small permanent population."),
        key_points=[
            "Workers were Egyptians, provisioned by the state - bakeries and breweries excavated.",
            "Crew graffiti names administrative work gangs.",
            "Recruitment, rotation, and daily logistics remain open questions.",
            "Fringe theories are rejected; the open questions are organizational.",
        ],
        requirements=[
            "Throughput estimates consistent with the workers' town capacity.",
            "An account linking labor to taxation systems.",
            "Separation of established fact from open organizational questions.",
        ],
        standards=[
            "Mainstream consensus stated clearly; fringe claims excluded.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Lehner M. The Complete Pyramids. Thames and Hudson; 1997.",
            "Hawass Z, Lehner M. Giza and the Pyramids. Thames and Hudson; 2017.",
        ],
        hypotheses=[
            "Rotating seasonal corvee funded by tax grain built the pyramids.",
            "A permanent skilled core plus seasonal unskilled labor.",
            "Labor service was the primary form of Old Kingdom taxation.",
            "Construction logistics drove the invention of new administration.",
        ],
        confirm="Provisioning capacity matches throughput models of rotating crews.",
        refute="The workers' town supported only a small permanent population.",
    ),
    dict(
        key="archaeology-11",
        name="The Copper Scroll Treasure",
        group="Lost Treasures",
        ladder_rank=11,
        ladder_tier="foundations",
        problem=("Does the treasure of the Copper Scroll - a list of 64 caches of gold and "
                 "silver - exist, and if so, whose was it?"),
        background=("Unlike the other Dead Sea Scrolls, the Copper Scroll (about 50-100 CE) "
                    "is engraved on copper and lists enormous quantities of buried treasure "
                    "with hiding places. Theories: Temple treasure hidden before the Roman "
                    "destruction, a legendary inventory, or Essene funds. No cache has been "
                    "found; the amounts described strain credulity, yet the scroll's "
                    "matter-of-fact style suggests a real inventory."),
        why_it_matters=("If real, the treasure would be the largest ancient hoard ever found - "
                        "and its ownership would rewrite the economics of Second Temple "
                        "Judaism."),
        sig_lens=("The Signature lens treats the scroll as an inventory ledger: the "
                  "Signature approach asks what institution needed 64 hiding places."),
        sig_body=("The Signature proposal models the scroll as a dispersed-institution "
                  "inventory. Assumptions: (1) the quantities, while large, match Temple-scale "
                  "wealth; (2) 64 caches imply an organization expecting to recover them; "
                  "(3) the Roman war of 66-73 CE provides the dispersal motive. Reasoning "
                  "path: the proposal shows the cache pattern - many small dispersed hides "
                  "rather than one vault - matches a community hiding operating funds ahead "
                  "of an expected siege, and predicts recovery markers (which are absent, "
                  "suggesting the hiders died). Limits: the amounts may be inflated or "
                  "symbolic; no cache has ever been verified."),
        pointer=('The Signature system reads the scroll as a dispersed-institution inventory, with the cache pattern matching a community hiding funds before a siege. The Signature test: a cache matching a scroll description is excavated. It would be refuted if metallurgical analysis shows the scroll is a much later composition.'),
        key_points=[
            "Engraved on copper, listing 64 caches of gold and silver.",
            "Dated about 50-100 CE, near the First Jewish-Roman War.",
            "No cache has ever been found.",
            "Temple treasure, Essene funds, and legend all have defenders.",
        ],
        requirements=[
            "An account of the 64-cache dispersal pattern.",
            "Consistency with Second Temple economics.",
            "A reason no cache has been recovered.",
        ],
        standards=[
            "Claims checked against the Copper Scroll literature; speculation marked.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Milik JT. The Copper Scroll. Oxford University Press; 1962.",
            "Lefkovits J. The Copper Scroll. 2000.",
        ],
        hypotheses=[
            "Temple authorities dispersed operating funds before the Roman siege.",
            "The scroll inventories Essene community wealth.",
            "The amounts are legendary or symbolic, not literal.",
            "Caches exist but the location descriptions are now undecipherable.",
        ],
        confirm="A cache matching a scroll description is excavated.",
        refute="Metallurgical analysis shows the scroll is a much later composition.",
    ),
    dict(
        key="archaeology-12",
        name="The Amber Room",
        group="Lost Treasures",
        ladder_rank=12,
        ladder_tier="compounded",
        problem=("Where is the Amber Room - the 18th-century chamber of carved amber panels "
                 "dismantled by Nazi looters from Catherine Palace in 1945?"),
        background=("Built in Prussia and gifted to Peter the Great, the Amber Room held "
                    "six tons of amber in carved panels - called the Eighth Wonder of the "
                    "World. In 1945 the Germans dismantled it at Tsarskoye Selo; it vanished "
                    "in the chaos of Konigsberg's fall. Theories: destroyed in the bombing "
                    "or castle fire, hidden in a mine, sunk in the Baltic, or secretly "
                    "recovered. A full replica was completed in 2003, but the original's "
                    "fate is unknown."),
        why_it_matters=("The Amber Room is the most famous lost artwork of WWII. Its fate "
                        "would close the largest open case in art looting."),
        sig_lens=("The Signature lens treats the disappearance as a logistics ledger: the "
                  "Signature approach asks what 27 crates of amber could physically have "
                  "done in collapsing Konigsberg."),
        sig_body=("The Signature proposal models the disappearance as a transport "
                  "impossibility. Assumptions: (1) the panels packed into 27 crates "
                  "weighing tons; (2) Konigsberg in early 1945 was under siege with "
                  "failing transport; (3) heavy crates need cranes, trucks, and intact "
                  "roads. Reasoning path: the proposal shows the logistics window for "
                  "evacuating tons of fragile amber closed before the dismantling "
                  "finished - predicting the crates never left the city and were "
                  "destroyed in the castle fire or bombing, which matches the absence of "
                  "any postwar trace. Limits: witness testimony is contradictory; absence "
                  "of evidence is not conclusive."),
        pointer=('The Signature system models the disappearance as a transport impossibility, predicting the crates never left Konigsberg. The Signature test: excavation finds amber-panel fragments in the castle ruins. It would be refuted if a crate with documented provenance surfaces in a private collection.'),
        key_points=[
            "Six tons of carved amber panels, dismantled in 1945.",
            "Packed into 27 crates; vanished during Konigsberg's fall.",
            "Destroyed, hidden, sunk, and recovered theories all circulate.",
            "No verified postwar trace has ever surfaced.",
        ],
        requirements=[
            "A logistics model for moving tons of amber under siege.",
            "An account of the contradictory witness testimony.",
            "Consistency with the complete absence of postwar traces.",
        ],
        standards=[
            "Claims checked against the WWII looting literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Scott-Clark C, Levy A. The Amber Room. Atlantic; 2004.",
            "Nicholas L. The Rape of Europa. Knopf; 1994.",
        ],
        hypotheses=[
            "The crates were destroyed in the Konigsberg castle fire.",
            "They were hidden in a mine or bunker, still undiscovered.",
            "They were sunk in the Baltic during evacuation.",
            "Soviet teams recovered them secretly after the war.",
        ],
        confirm="Excavation finds amber-panel fragments in the castle ruins.",
        refute="A crate with documented provenance surfaces in a private collection.",
    ),
    dict(
        key="archaeology-13",
        name="The Sea Peoples",
        group="Lost Peoples",
        ladder_rank=13,
        ladder_tier="compounded",
        problem=("Who were the Sea Peoples whose attacks coincide with the Bronze Age "
                 "collapse around 1200 BCE - invaders, migrants, or a symptom?"),
        background=("Egyptian records (Medinet Habu) describe coalitions - Peleset, "
                    "Sherden, Shekelesh - attacking by land and sea. They are linked to "
                    "the fall of Mycenaean palaces, the Hittite Empire, and Ugarit. But "
                    "no homeland is identified, no single material culture unites them, "
                    "and some scholars argue they were refugees and mercenaries - a "
                    "symptom of collapsing systems rather than a cause."),
        why_it_matters=("The Sea Peoples stand at the hinge of the Bronze Age collapse, "
                        "history's first dark age. Their identity decides whether the "
                        "collapse was invasion or systems failure."),
        sig_lens=("The Signature lens treats the Sea Peoples as a displacement ledger: "
                  "the Signature approach asks what pushed whole populations to sea."),
        sig_body=("The Signature proposal models the Sea Peoples as climate-driven "
                  "displacement. Assumptions: (1) the eastern Mediterranean suffered "
                  "severe drought around 1200 BCE; (2) palace economies were brittle, "
                  "optimized for surplus extraction; (3) displaced groups armed "
                  "themselves from collapsing arsenals. Reasoning path: the proposal "
                  "shows drought can synchronize crop failures across the palace world, "
                  "producing simultaneous refugees who become raiders - explaining why "
                  "no single homeland or culture unites them: they were the system's "
                  "own debris in motion. Limits: drought evidence is regionally "
                  "uneven; some destructions predate the drought signal."),
        pointer=("The Signature system models the Sea Peoples as drought-displaced populations turned raiders - the palace system's own debris in motion. The Signature test: destruction layers track drought proxies across the eastern Mediterranean. It would be refuted if a unified homeland and material culture is identified."),
        key_points=[
            "Egyptian records name coalitions attacking around 1200 BCE.",
            "No homeland or unifying material culture is identified.",
            "Destructions span Mycenaeans, Hittites, and Levantine cities.",
            "Invaders-versus-symptom remains the core dispute.",
        ],
        requirements=[
            "An account of the multi-ethnic, homeland-less pattern.",
            "Consistency with drought and destruction chronologies.",
            "Separation of Egyptian propaganda from events.",
        ],
        standards=[
            "Claims checked against the collapse literature; speculation marked.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Cline EH. 1177 B.C.: The Year Civilization Collapsed. Princeton University Press; 2014.",
            "Drews R. The End of the Bronze Age. Princeton University Press; 1993.",
        ],
        hypotheses=[
            "Drought-displaced populations became the Sea Peoples.",
            "They were primarily mercenaries and pirates exploiting collapse.",
            "A specific migration (western Anatolia, Sardinia) drove events.",
            "They are largely an Egyptian literary construct.",
        ],
        confirm="Destruction layers track drought proxies across the eastern Mediterranean.",
        refute="A unified homeland and material culture is identified.",
    ),
    dict(
        key="archaeology-14",
        name="The Etruscan Origins",
        group="Lost Peoples",
        ladder_rank=14,
        ladder_tier="compounded",
        problem=("Where did the Etruscans come from - eastern migrants as Herodotus claimed, "
                 "or indigenous Italians as Dionysius argued?"),
        background=("The Etruscans built the civilization that taught Rome urbanism, yet "
                    "their non-Indo-European language isolates them. Herodotus said they "
                    "sailed from Lydia; ancient DNA now suggests continuity with local "
                    "Iron Age populations - the language may have arrived without mass "
                    "migration, or survived as a pre-Indo-European relic. The debate has "
                    "run for 2,500 years."),
        why_it_matters=("The Etruscans shaped Rome, which shaped the West. Their origin "
                        "decides whether a key Western root is native or transplanted."),
        sig_lens=("The Signature lens treats the origin as a language-genes ledger: the "
                  "Signature approach asks how a language can migrate without people."),
        sig_body=("The Signature proposal models Etruscan as a relic language of a "
                  "maritime network. Assumptions: (1) ancient DNA shows population "
                  "continuity; (2) the language is genuinely non-Indo-European; (3) "
                  "Tyrrhenian seafaring connected distant coasts. Reasoning path: the "
                  "proposal shows a small seafaring elite can spread a prestige language "
                  "without demographic replacement - as with later maritime lingua "
                  "francas - reconciling Herodotus (a real eastern connection) with the "
                  "DNA (local continuity). The Etruscans were locals speaking a sea "
                  "language. Limits: the mechanism needs a plausible prestige source; "
                  "the linguistic relatives remain unidentified."),
        pointer=('The Signature system models Etruscan as a prestige sea-language spread by a small elite over a continuous local population. The Signature test: prestige-language markers concentrate in elite contexts first. It would be refuted if mass eastern migration appears in the DNA record.'),
        key_points=[
            "Etruscan is non-Indo-European, isolating its speakers linguistically.",
            "Ancient DNA suggests population continuity with Iron Age Italians.",
            "Herodotus claimed Lydian migration 2,500 years ago.",
            "The Etruscans profoundly shaped early Rome.",
        ],
        requirements=[
            "Reconciliation of DNA continuity with a non-local language.",
            "A mechanism for language spread without migration.",
            "Identification of linguistic relatives or a relic account.",
        ],
        standards=[
            "Claims checked against the Etruscan literature; speculation marked.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Barker G, Rasmussen T. The Etruscans. Blackwell; 1998.",
            "Posth C et al. The origin and legacy of the Etruscans. Science Advances; 2021.",
        ],
        hypotheses=[
            "A maritime elite spread a prestige language over locals.",
            "Etruscan is an indigenous pre-Indo-European relic.",
            "A genuine eastern migration occurred but left little DNA trace.",
            "The language arrived via Anatolian trade networks gradually.",
        ],
        confirm="Prestige-language markers concentrate in elite contexts first.",
        refute="Mass eastern migration appears in the DNA record.",
    ),
    dict(
        key="archaeology-15",
        name="The Tomb of Genghis Khan",
        group="Lost Tombs",
        ladder_rank=15,
        ladder_tier="compounded",
        problem=("Where is the burial of Genghis Khan - hidden in 1227 by guards who "
                 "killed every witness, according to legend?"),
        background=("The Secret History says Khan died in 1227 and was buried in secret "
                    "on Burkhan Khaldun, his sacred mountain; the escort party allegedly "
                    "killed everyone they met. No tomb has been found despite satellite "
                    "surveys, ground-penetrating radar, and expeditions. Mongolian "
                    "tradition opposes disturbing the mountain; some scholars doubt a "
                    "grand tomb exists at all - a steppe khan might lie in an unmarked "
                    "grave by design."),
        why_it_matters=("The tomb would be the richest undisturbed burial in Asian history "
                        "- and its absence is itself a statement about how the Mongols "
                        "wanted their founder remembered."),
        sig_lens=("The Signature lens treats the tomb as a secrecy ledger: the Signature "
                  "approach asks what burial a secrecy-obsessed culture would actually "
                  "build."),
        sig_body=("The Signature proposal models the burial as designed unfindability. "
                  "Assumptions: (1) Mongol tradition forbade marking the grave; (2) the "
                  "escort-secrecy accounts are partly legendary but reflect real "
                  "practice; (3) Burkhan Khaldun's terrain defeats remote sensing. "
                  "Reasoning path: the proposal shows that a culture optimizing for "
                  "non-discovery would choose an unmarked pit in difficult terrain - "
                  "predicting that all high-tech surveys fail precisely because there "
                  "is no monument to find, only a grave. The legend's extravagance "
                  "then functions as misdirection. Limits: the model cannot be "
                  "distinguished from no-tomb-at-all without excavation that tradition "
                  "forbids."),
        pointer=('The Signature system models the burial as designed unfindability - an unmarked grave whose legend functions as misdirection. The Signature test: non-invasive survey finds an anomaly matching a simple pit burial. It would be refuted if excavation-quality evidence shows no burial on the mountain.'),
        key_points=[
            "Khan died in 1227; tradition places burial on Burkhan Khaldun.",
            "Legend says the escort killed all witnesses.",
            "Satellites and radar have found nothing conclusive.",
            "Mongolian tradition opposes excavation of the mountain.",
        ],
        requirements=[
            "An account consistent with survey failures.",
            "Respect for Mongolian cultural prohibitions.",
            "Separation of Secret History narrative from evidence.",
        ],
        standards=[
            "Claims checked against the Mongol archaeology literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Weatherford J. Genghis Khan and the Making of the Modern World. Crown; 2004.",
            "The Secret History of the Mongols. 13th century.",
        ],
        hypotheses=[
            "An unmarked grave on Burkhan Khaldun, designed to be unfindable.",
            "A grand tomb exists but terrain defeats remote sensing.",
            "The burial was elsewhere; the mountain tradition is later.",
            "No recoverable tomb survives after eight centuries.",
        ],
        confirm="Non-invasive survey finds an anomaly matching a simple pit burial.",
        refute="Excavation-quality evidence shows no burial on the mountain.",
    ),
    dict(
        key="archaeology-16",
        name="The Sutton Hoo Ship Burial",
        group="Burials",
        ladder_rank=16,
        ladder_tier="compounded",
        problem=("Who lay in the great ship burial at Sutton Hoo - and why was no body "
                 "ever found?"),
        background=("The 1939 excavation revealed a 27-meter ship holding the richest "
                    "early-medieval burial in Europe: gold, garnet work, Byzantine silver, "
                    "an iron helmet - but no body; the acidic soil likely dissolved it. "
                    "The leading candidate is Raedwald, king of East Anglia (died about "
                    "624 CE), but the coins suggest about 625 and no inscription names "
                    "anyone. The burial's blend of pagan ship rite and Christian objects "
                    "mirrors England's conversion era."),
        why_it_matters=("Sutton Hoo rewrote the Dark Ages: it proved early England was "
                        "rich, connected, and sophisticated. The occupant's identity would "
                        "name the king who bridged pagan and Christian worlds."),
        sig_lens=("The Signature lens treats the burial as a conversion ledger: the "
                  "Signature approach asks what a king hedging between two religions "
                  "would take to the grave."),
        sig_body=("The Signature proposal models the burial as deliberate religious "
                  "ambiguity. Assumptions: (1) the occupant died during the conversion "
                  "generation; (2) grave goods signal allegiances to the living; (3) "
                  "Raedwald famously kept both pagan and Christian altars. Reasoning "
                  "path: the proposal shows the mixed assemblage - ship rite plus "
                  "Christian silver - is exactly what a hedging king would commission: "
                  "legible to both constituencies, committing to neither. The missing "
                  "body is then taphonomy, not mystery. Limits: the Raedwald "
                  "identification rests on coin dates, not names; another East Anglian "
                  "elite fits nearly as well."),
        pointer=("The Signature system reads the mixed assemblage as a hedging king's deliberate religious ambiguity. The Signature test: new dating or inscriptional evidence names Raedwald. It would be refuted if the coin hoard dates definitively outside Raedwald's reign."),
        key_points=[
            "Richest early-medieval burial in Europe, excavated 1939.",
            "A 27-meter ship; no body survived the acidic soil.",
            "Raedwald of East Anglia (died about 624) is the leading candidate.",
            "Pagan rite plus Christian objects mirror the conversion era.",
        ],
        requirements=[
            "An account of the missing body consistent with soil chemistry.",
            "A candidate matching the coin dates (about 625).",
            "An explanation for the religious mixing.",
        ],
        standards=[
            "Claims checked against the Sutton Hoo literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Carver M. Sutton Hoo: Burial Ground of Kings? University of Pennsylvania Press; 1998.",
            "Bruce-Mitford R. The Sutton Hoo Ship-Burial. British Museum; 1975.",
        ],
        hypotheses=[
            "Raedwald, hedging between pagan and Christian constituencies.",
            "Another East Anglian king of the conversion generation.",
            "The burial is a cenotaph; the body was never there.",
            "The assemblage is diplomatic gift display, not personal belief.",
        ],
        confirm="New dating or inscriptional evidence names Raedwald.",
        refute="The coin hoard dates definitively outside Raedwald's reign.",
    ),
    dict(
        key="archaeology-17",
        name="The Tarim Basin Mummies",
        group="Burials",
        ladder_rank=17,
        ladder_tier="compounded",
        problem=("Who were the Europoid-looking mummies of the Tarim Basin - some 4,000 "
                 "years old, wearing woolens and felt hats - buried in what is now "
                 "western China?"),
        background=("Naturally preserved by desert salts, the mummies (Qawrighul, "
                    "Xiaohe, and others) have light hair, long noses, and woven textiles "
                    "resembling European weaves. DNA shows mixed ancestry - western "
                    "Eurasian and local. Theories range from Tocharian speakers to "
                    "lost Indo-European migrations to an isolated local population. "
                    "Chinese authorities long restricted access, politicizing the finds."),
        why_it_matters=("The mummies are the human face of Bronze Age Eurasian contact - "
                        "proof that the Silk Road's peoples were mixing millennia before "
                        "the Silk Road."),
        sig_lens=("The Signature lens treats the mummies as a contact ledger: the "
                  "Signature approach asks what migration pattern produces their exact "
                  "genetic mix."),
        sig_body=("The Signature proposal models the Tarim population as a Bronze Age "
                  "oasis isolate. Assumptions: (1) the DNA shows both western Eurasian "
                  "and Ancient North Eurasian ancestry; (2) the desert oases were "
                  "habitable islands; (3) textile similarities track contact, not "
                  "identity. Reasoning path: the proposal shows an early migration "
                  "followed by long isolation predicts exactly the observed pattern - "
                  "mixed ancestry frozen by endogamy, distinctive textiles preserved - "
                  "making the mummies neither lost Europeans nor simple locals but a "
                  "distinct Bronze Age people. Limits: sampling is limited and "
                  "politicized; the linguistic identity (Tocharian?) remains "
                  "unproven."),
        pointer=('The Signature system models the mummies as an early-migration oasis isolate, with mixed ancestry frozen by endogamy. The Signature test: broader DNA sampling confirms the isolate model across oases. It would be refuted if the mummies prove to be recent intrusive burials, not Bronze Age.'),
        key_points=[
            "Naturally mummified, up to 4,000 years old, Europoid features.",
            "DNA shows mixed western Eurasian and local ancestry.",
            "Textiles resemble European weaves.",
            "Access has been restricted and politicized.",
        ],
        requirements=[
            "A migration model matching the mixed DNA.",
            "An account of textile similarities.",
            "Separation of scientific findings from political framing.",
        ],
        standards=[
            "Claims checked against the Tarim literature; politics excluded from analysis.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Mallory JP, Mair VH. The Tarim Mummies. Thames and Hudson; 2000.",
            "Ning C et al. Ancient genomes from the Tarim Basin. 2021.",
        ],
        hypotheses=[
            "An early migration followed by long oasis isolation.",
            "Tocharian speakers of the later historical record.",
            "Continuous contact maintained the mixed ancestry.",
            "A local population with western admixture, not migrants.",
        ],
        confirm="Broader DNA sampling confirms the isolate model across oases.",
        refute="The mummies prove to be recent intrusive burials, not Bronze Age.",
    ),
    dict(
        key="archaeology-18",
        name="The Minoan Eruption Date",
        group="Dating",
        ladder_rank=18,
        ladder_tier="compounded",
        problem=("When exactly did Thera (Santorini) erupt - the Bronze Age catastrophe "
                 "that may have ended Minoan dominance?"),
        background=("Archaeology long placed the eruption about 1500 BCE, late in the "
                    "Minoan sequence. But radiocarbon dates - from an olive branch buried "
                    "in the ash - point to about 1600 BCE, a century earlier, which would "
                    "decouple the eruption from the Mycenaean takeover of Crete. Ice cores, "
                    "tree rings, and calibration curves are all contested; the high versus "
                    "low chronology dispute has run for decades."),
        why_it_matters=("A century's difference decides whether a volcano ended Europe's "
                        "first civilization or merely wounded it - and anchors the entire "
                        "Aegean Bronze Age timeline."),
        sig_lens=("The Signature lens treats the date as a calibration ledger: the "
                  "Signature approach asks which clock - pots or atoms - is lying."),
        sig_body=("The Signature proposal models the dispute as a calibration artifact. "
                  "Assumptions: (1) radiocarbon dates need regional calibration; (2) the "
                  "olive branch may include old wood; (3) archaeological synchronisms "
                  "with Egypt carry their own errors. Reasoning path: the proposal "
                  "shows the high and low chronologies each assume one clock is clean - "
                  "but if both clocks carry modest systematic error in the same "
                  "direction, the true date falls between, around 1550 BCE, decoupling "
                  "the eruption from the final Minoan collapse while keeping it a "
                  "major shock. Limits: the model needs better regional calibration "
                  "data; the olive-branch old-wood problem is unresolved."),
        pointer=('The Signature system models the dispute as dual clock error, placing the eruption between the rival dates. The Signature test: regional calibration converges both clocks near 1550 BCE. It would be refuted if a clean annual-resolution date fixes one chronology exactly.'),
        key_points=[
            "Archaeology says about 1500 BCE; radiocarbon says about 1600 BCE.",
            "The gap decides whether the eruption ended Minoan dominance.",
            "Ice cores, tree rings, and calibration are all contested.",
            "The dispute has run for decades without resolution.",
        ],
        requirements=[
            "Reconciliation of radiocarbon with archaeological synchronisms.",
            "Regional calibration for Aegean radiocarbon.",
            "An account of the olive-branch old-wood problem.",
        ],
        standards=[
            "Dating claims checked against the Thera literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Manning SW et al. Chronology for the Aegean Late Bronze Age. Science; 2006.",
            "Friedrich WL et al. Santorini eruption radiocarbon dated to 1627-1600 BCE. Science; 2006.",
        ],
        hypotheses=[
            "Both clocks carry error; the true date falls between.",
            "The high chronology (about 1600 BCE) is correct.",
            "The low chronology (about 1500 BCE) is correct.",
            "The eruption was a prolonged sequence, not one event.",
        ],
        confirm="Regional calibration converges both clocks near 1550 BCE.",
        refute="A clean annual-resolution date fixes one chronology exactly.",
    ),
    dict(
        key="archaeology-19",
        name="The Antikythera Mechanism",
        group="Technology",
        ladder_rank=19,
        ladder_tier="compounded",
        problem=("What could the Antikythera mechanism - a 2,000-year-old geared bronze "
                 "computer from a Greek shipwreck - actually do, and who built it?"),
        background=("Recovered in 1901, the mechanism contains at least 37 interlocking "
                    "gears predicting eclipses, calendrical cycles, and planetary positions. "
                    "X-ray tomography revealed inscriptions - a user manual. Yet questions "
                    "remain: the full gear train, whether it modeled all five planets, who "
                    "manufactured it (Rhodes? Syracuse? linked to Archimedes?), and how "
                    "such technology vanished for a millennium."),
        why_it_matters=("The mechanism proves ancient technology was a thousand years ahead "
                        "of the textbooks. Its full function rewrites the history of "
                        "science."),
        sig_lens=("The Signature lens treats the mechanism as a production ledger: the "
                  "Signature approach asks what workshop could cut such gears - and make "
                  "more."),
        sig_body=("The Signature proposal models the mechanism as a luxury product of a "
                  "Hellenistic workshop tradition. Assumptions: (1) the gear-cutting "
                  "precision implies specialized tooling; (2) the instruction inscriptions "
                  "imply users, hence production; (3) no other examples survive because "
                  "bronze was recycled. Reasoning path: the proposal shows the mechanism "
                  "fits a known Hellenistic pattern - astronomical showpieces for wealthy "
                  "patrons, like the later Islamic astrolabe tradition - predicting a "
                  "workshop (probably Rhodes) that made several, with the shipwreck "
                  "example being cargo. The technology did not vanish; its medium was "
                  "melted down. Limits: no workshop has been found; the full planetary "
                  "display remains reconstructed, not observed."),
        pointer=('The Signature system models the mechanism as a workshop luxury product, with bronze recycling explaining why no others survive. The Signature test: a second mechanism or workshop debris is found. It would be refuted if gear analysis proves the surviving train cannot drive planets.'),
        key_points=[
            "At least 37 gears; predicts eclipses and planetary positions.",
            "Inscriptions form a user manual.",
            "Full gear train and planetary scope still reconstructed.",
            "No other example survives; the maker is unknown.",
        ],
        requirements=[
            "A complete, working gear-train reconstruction.",
            "Identification of the manufacturing tradition.",
            "An account of why the technology left no descendants.",
        ],
        standards=[
            "Claims checked against the Antikythera research literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Freeth T et al. Decoding the ancient Greek astronomical calculator. Nature; 2006.",
            "Jones A. A Portable Cosmos. Oxford University Press; 2017.",
        ],
        hypotheses=[
            "A Rhodian workshop produced several such devices for patrons.",
            "It was a unique royal commission, not a product line.",
            "The tradition continued into Islamic astronomy via lost intermediaries.",
            "It modeled all five planets; reconstructions will confirm it.",
        ],
        confirm="A second mechanism or workshop debris is found.",
        refute="Gear analysis proves the surviving train cannot drive planets.",
    ),
    dict(
        key="archaeology-20",
        name="The Baghdad Battery",
        group="Technology",
        ladder_rank=20,
        ladder_tier="compounded",
        problem=("Was the so-called Baghdad Battery - a Parthian-era clay pot with copper "
                 "cylinder and iron rod - actually an electric battery?"),
        background=("Excavated in 1936 near Baghdad and dated to about 200 BCE-200 CE, the "
                    "artifact resembles a galvanic cell: Wilhelm Konig proposed it "
                    "electroplated gold onto silver. Replicas produce small voltages with "
                    "vinegar or grape juice. Skeptics note no wires, no electroplated "
                    "artifacts from the period, and alternative uses (storage vessel, "
                    "ritual object). The debate is a Rorschach test for ancient "
                    "technology."),
        why_it_matters=("A working battery 1,800 years before Volta would rewrite the "
                        "history of electricity - or the artifact is a cautionary tale "
                        "about seeing modern tech in ancient objects."),
        sig_lens=("The Signature lens treats the battery as a use-ledger: the Signature "
                  "approach asks what job the object did, regardless of what it could "
                  "do."),
        sig_body=("The Signature proposal separates capability from use. Assumptions: (1) "
                  "the artifact can generate small voltages - replicas prove it; (2) no "
                  "Parthian wires or electroplated goods exist; (3) the pots were found "
                  "in a settlement context. Reasoning path: the proposal shows the "
                  "object occupies a design space where storage vessels and accidental "
                  "cells overlap - and that without a circuit (wires, applications), "
                  "capability is irrelevant: it was a vessel that happened to be "
                  "battery-shaped. The lesson is methodological: function requires a "
                  "system, not a component. Limits: a ritual electroplating use cannot "
                  "be fully excluded; the sample is tiny."),
        pointer=('The Signature system separates what the pot could do from what it did, arguing function needs a system, not a component. The Signature test: parthian wires or electroplated goods appear in context. It would be refuted if residue analysis shows only storage of scrolls or sacred texts.'),
        key_points=[
            "Clay pot, copper cylinder, iron rod; Parthian era.",
            "Replicas generate small voltages with acidic electrolytes.",
            "No wires or electroplated artifacts from the period exist.",
            "Storage, ritual, and battery uses all have defenders.",
        ],
        requirements=[
            "Evidence of a circuit: wires, terminals, applications.",
            "Electroplated artifacts from the period if plating was the use.",
            "A use consistent with the archaeological context.",
        ],
        standards=[
            "Claims checked against the primary literature; speculation marked.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Konig W. Ein galvanisches Element aus der Partherzeit? Forschungen und Fortschritte; 1940.",
            "Keyser PT. The purpose of the Parthian galvanic cells. Journal of Near Eastern Studies; 1993.",
        ],
        hypotheses=[
            "It was a storage vessel that happens to be battery-shaped.",
            "It electroplated ritual objects on a small scale.",
            "It had a medicinal or ritual electric function.",
            "It was a genuine battery in a lost technological tradition.",
        ],
        confirm="Parthian wires or electroplated goods appear in context.",
        refute="Residue analysis shows only storage of scrolls or sacred texts.",
    ),
    dict(
        key="archaeology-21",
        name="Roman Concrete: The Full Recipe",
        group="Technology",
        ladder_rank=21,
        ladder_tier="compounded",
        problem=("What exactly made Roman concrete self-healing and millennia-durable - "
                 "and can we fully reproduce it?"),
        background=("Roman harbors and the Pantheon have survived 2,000 years, while "
                    "modern concrete crumbles in decades. Research found the Romans used "
                    "volcanic ash (pozzolana), lime clasts that enable self-healing cracks, "
                    "and hot mixing. But the full recipe - proportions, mixing sequences, "
                    "curing - varied by site, and modern reproductions have not matched "
                    "Roman longevity in seawater."),
        why_it_matters=("Cement production causes about 8 percent of global CO2. Roman "
                        "concrete's durability and lower firing temperatures could "
                        "decarbonize construction - if we can truly copy it."),
        sig_lens=("The Signature lens treats the concrete as a process ledger, not a "
                  "recipe: the Signature approach asks what the mixing did, not just "
                  "what went in."),
        sig_body=("The Signature proposal models Roman concrete as hot-mixed process, "
                  "not formula. Assumptions: (1) lime clasts are remnants of hot mixing, "
                  "not sloppy work; (2) self-healing needs calcium-rich reservoirs; (3) "
                  "seawater interaction strengthens the matrix over time. Reasoning path: "
                  "the proposal shows the key variable is thermal history - quicklime "
                  "mixed hot creates the clasts that later dissolve into cracks - making "
                  "reproduction a matter of process control, not ingredient lists. Modern "
                  "copies fail because they mix cold. Limits: site-to-site variation is "
                  "large; the full parameter space is unmapped."),
        pointer=('The Signature system models the concrete as a hot-mixing process, with thermal history as the key variable modern copies miss. The Signature test: hot-mixed reproductions match Roman seawater longevity. It would be refuted if cold-mixed pozzolana concrete proves equally durable.'),
        key_points=[
            "Roman marine concrete survives 2,000 years; modern fails in decades.",
            "Lime clasts enable self-healing of cracks.",
            "Hot mixing is the leading process explanation.",
            "Cement causes about 8 percent of global CO2 emissions.",
        ],
        requirements=[
            "A process model reproducing self-healing in the lab.",
            "Site-to-site variation mapped to parameters.",
            "Seawater longevity demonstrated in reproductions.",
        ],
        standards=[
            "Materials claims checked against the recent concrete literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Seymour LM et al. Hot mixing: mechanistic insights into the durability of Roman concrete. Science Advances; 2023.",
            "Jackson MD et al. Material and elastic properties of Al-tobermorite in ancient Roman seawater concrete. 2017.",
        ],
        hypotheses=[
            "Hot-mixing process control is the reproducible key.",
            "Pozzolana chemistry matters more than process.",
            "Seawater interaction is the main durability driver.",
            "Each site had its own recipe; no single key exists.",
        ],
        confirm="Hot-mixed reproductions match Roman seawater longevity.",
        refute="Cold-mixed pozzolana concrete proves equally durable.",
    ),
    dict(
        key="archaeology-22",
        name="Greek Fire",
        group="Technology",
        ladder_rank=22,
        ladder_tier="compounded",
        problem=("What was the formula of Greek fire - the Byzantine naval incendiary that "
                 "burned on water - and how was it projected?"),
        background=("From the 7th century CE, Byzantine ships sprayed an unquenchable "
                    "flame that saved Constantinople repeatedly. The formula was a state "
                    "secret, lost with the empire. Candidates: petroleum distillates, "
                    "quicklime-water reactions, saltpeter mixtures. The siphon projector "
                    "is equally mysterious - a pump, a flamethrower, heated reservoirs? "
                    "Modern reconstructions burn but match no account fully."),
        why_it_matters=("Greek fire was the medieval weapon of mass destruction, deciding "
                        "the fate of Constantinople and with it European history. Its "
                        "secret died with its makers."),
        sig_lens=("The Signature lens treats Greek fire as a systems ledger: the "
                  "Signature approach asks what combination of fuel, projector, and "
                  "tactics made it work."),
        sig_body=("The Signature proposal models Greek fire as a weapons system, not a "
                  "substance. Assumptions: (1) no single chemical matches all accounts; "
                  "(2) projection mechanics matter as much as fuel; (3) state secrecy "
                  "fragmented knowledge. Reasoning path: the proposal shows the accounts "
                  "describe different components - a petroleum-based fuel, a heated "
                  "siphon projector, specialized tactics - and that the 'secret' was the "
                  "system integration, lost when the workshops and crews were lost. "
                  "Reconstruction then needs all three, explaining why fuel-only "
                  "experiments disappoint. Limits: the projector mechanics remain the "
                  "weakest link; no siphon survives."),
        pointer=('The Signature system models Greek fire as an integrated weapons system, with the secret in the integration rather than one chemical. The Signature test: an integrated reconstruction matches all account details. It would be refuted if one simple chemical matches every historical description.'),
        key_points=[
            "Burned on water; saved Constantinople multiple times from the 7th century.",
            "The formula was a guarded state secret, now lost.",
            "Petroleum, quicklime, and saltpeter theories compete.",
            "The siphon projector is as mysterious as the fuel.",
        ],
        requirements=[
            "A fuel matching the burn-on-water accounts.",
            "A workable projector reconstruction.",
            "An account of how the secret was kept and lost.",
        ],
        standards=[
            "Claims checked against the Byzantine military literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Haldon J, Byrne M. A possible solution to the problem of Greek fire. Byzantinische Zeitschrift; 1977.",
            "Pryor JH, Jeffreys EM. The Age of the Dromon. Brill; 2006.",
        ],
        hypotheses=[
            "The secret was system integration, not one chemical.",
            "Petroleum distillates were the core fuel.",
            "Quicklime-water exothermic reaction was the base.",
            "The projector was a simple pump; the fuel did the work.",
        ],
        confirm="An integrated reconstruction matches all account details.",
        refute="One simple chemical matches every historical description.",
    ),
        dict(
        key="archaeology-23",
        name="The Shugborough Inscription",
        group="Decipherment",
        ladder_rank=23,
        ladder_tier="compounded",
        problem=("What does the Shugborough inscription - ten letters carved on an "
                 "18th-century English monument - actually say?"),
        background=("The Shepherd's Monument at Shugborough Hall in Staffordshire bears the "
                    "sequence O U O S V A V V above the letters D M, carved in the 1700s. "
                    "Proposed readings include a Latin dedication's initials, a Templar or "
                    "Masonic cipher, and a personal message from the monument's patron. "
                    "Bletchley Park veterans and modern codebreakers have tried their hands; "
                    "no reading has stuck, because ten letters without a key admit far too "
                    "many solutions. The monument and its patron are well documented - only "
                    "the meaning is missing."),
        why_it_matters=("A famous unsolved cipher sits in plain sight on a country estate. It "
                        "tests the limits of codebreaking: what can be solved without a crib, "
                        "and what cannot."),
        sig_lens=("The Signature lens treats the inscription as a crib ledger: the Signature "
                  "approach asks what known plaintext would be enough to crack it."),
        sig_body=("The Signature proposal models the inscription as crib-starved. "
                  "Assumptions: (1) ten letters admit too many consistent readings for "
                  "cryptanalysis alone to decide; (2) historical context - the patron's "
                  "papers, the monument's commission - narrows the field; (3) a genuine "
                  "solution should predict independently verifiable details. Reasoning "
                  "path: the proposal predicts the inscription should yield, if at all, "
                  "to archival evidence rather than pure codebreaking - explaining why "
                  "decades of cipher attacks failed. The answer, if it comes, will come "
                  "from the archives, not the algorithms. Limits: the archives may be "
                  "silent; some puzzles are simply lost to time."),
        pointer=("The Signature system models the inscription as crib-starved: ten letters admit too many solutions, so archives rather than algorithms must crack it. The Signature test: the patron's papers yield a matching phrase. It would be refuted if a cipher solution predicts independently verifiable details."),
        key_points=[
            "Ten letters O U O S V A V V above D M on an 18th-century monument.",
            "Readings proposed include Latin initials and secret-society ciphers.",
            "Codebreakers including Bletchley veterans have failed.",
            "Short crib-less ciphers are mathematically underdetermined.",
        ],
        requirements=[
            "Archival research into the patron's papers and the commission.",
            "A reading that predicts verifiable details beyond the letters.",
            "An account of why pure cryptanalysis cannot decide it.",
        ],
        standards=[
            "Claims checked against the historical-cipher literature; speculation marked.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Kahn D. The Codebreakers. Macmillan; 1967.",
            "Singh S. The Code Book. Doubleday; 1999.",
        ],
        hypotheses=[
            "The letters are the initials of a Latin dedication.",
            "The inscription encodes a Masonic or Templar message.",
            "It is a personal message from the patron.",
            "The meaning is lost and unrecoverable.",
        ],
        confirm="The patron's papers yield a matching phrase.",
        refute="A cipher solution predicts independently verifiable details.",
    ),
    dict(
        key="archaeology-24",
        name="The Piri Reis Map Sources",
        group="Cartography",
        ladder_rank=24,
        ladder_tier="advanced",
        problem=("What source maps did the Ottoman admiral Piri Reis use for his 1513 world "
                 "map - and do they include genuinely lost ancient charts?"),
        background=("The 1513 map shows South America's east coast with surprising accuracy "
                    "and has fueled claims of ancient maps of Antarctica. Mainstream "
                    "scholarship traces its sources to Portuguese charts, Columbus's lost "
                    "map, and Arab cartography - but the map's second fragment is lost, "
                    "its projections are idiosyncratic, and the accuracy debates continue. "
                    "The fringe has claimed far more than the evidence supports."),
        why_it_matters=("The map is a window into the lost cartographic libraries of the "
                        "Age of Discovery - including charts that no longer survive in any "
                        "other copy."),
        sig_lens=("The Signature lens treats the map as a source ledger: the Signature "
                  "approach separates what Piri Reis drew from what his sources drew."),
        sig_body=("The Signature proposal models the map as a compilation with traceable "
                  "seams. Assumptions: (1) Piri Reis annotated his sources in the "
                  "marginal notes; (2) different coastlines show different projection "
                  "habits; (3) Portuguese, Spanish, and Arab charts had distinct "
                  "conventions. Reasoning path: the proposal maps each coastline segment "
                  "to a source tradition by its errors and conventions - the accurate "
                  "Brazilian coast to Portuguese charts, the Caribbean to Columbus's "
                  "tradition - showing the map's marvels are compilation, not mystery. "
                  "The Antarctic claims dissolve under source analysis. Limits: the lost "
                  "second fragment limits the analysis; some segments resist "
                  "attribution."),
        pointer=('The Signature system decomposes the map into source traditions by their errors and conventions, dissolving the mystery into compilation. The Signature test: every coastline segment attributes cleanly to a known source tradition. It would be refuted if a coastline appears that no 16th-century source could have supplied.'),
        key_points=[
            "1513 Ottoman map with an accurately rendered South American coast.",
            "Marginal notes describe the admiral's sources.",
            "Fringe claims of Antarctic mapping lack support.",
            "The map's second fragment is lost.",
        ],
        requirements=[
            "Source attribution for each coastline segment.",
            "Separation of mainstream findings from fringe claims.",
            "An account of the map's projection idiosyncrasies.",
        ],
        standards=[
            "Claims checked against the cartographic-history literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "McIntosh GC. The Piri Reis Map of 1513. University of Georgia Press; 2000.",
            "Soucek S. Piri Reis and Turkish Mapmaking After Columbus. Oxford University Press; 1996.",
        ],
        hypotheses=[
            "The map is a compilation of Portuguese, Spanish, and Arab charts.",
            "Lost ancient source charts contributed unknown coastlines.",
            "The accuracy is overstated by selective modern readings.",
            "The lost fragment held the key to the remaining puzzles.",
        ],
        confirm="Every coastline segment attributes cleanly to a known source tradition.",
        refute="A coastline appears that no 16th-century source could have supplied.",
    ),
    dict(
        key="archaeology-25",
        name="Yonaguni: Natural or Artificial",
        group="Contested Sites",
        ladder_rank=25,
        ladder_tier="advanced",
        problem=("Are the stepped terraces off Yonaguni Island, Japan - looking like a "
                 "drowned pyramid - natural geology or a 10,000-year-old human structure?"),
        background=("Discovered in 1986, the formations show striking right angles, "
                    "terraces, and a 'staircase' at 25 meters depth. Geologists note the "
                    "region's sandstone fractures naturally into blocks, and no tools, "
                    "habitation, or artifacts have been found. Proponents cite tool-like "
                    "marks and a carved 'face.' If artificial and pre-sea-level-rise, it "
                    "would be the oldest monumental architecture known - hence the "
                    "stakes."),
        why_it_matters=("The verdict decides between a geological curiosity and the oldest "
                        "monument on Earth - and tests how archaeology handles "
                        "extraordinary claims."),
        sig_lens=("The Signature lens treats Yonaguni as a null-hypothesis ledger: the "
                  "Signature approach asks what natural processes must be exhausted "
                  "before invoking builders."),
        sig_body=("The Signature proposal formalizes the natural-first test. Assumptions: "
                  "(1) the local sandstone has well-bedded strata that fracture "
                  "orthogonally; (2) underwater erosion sharpens edges; (3) human "
                  "structures leave tool marks, quarries, and debris. Reasoning path: the "
                  "proposal shows the formations' geometry falls within the natural "
                  "fracture envelope of the bedrock, while the expected human "
                  "signatures - quarries, spoil, tools - are entirely absent. The "
                  "burden of proof therefore rests on the artificial claim, which has "
                  "not met it. Limits: absence of evidence underwater is weaker than "
                  "on land; a pre-existing natural terrace could have been modified."),
        pointer=('The Signature system applies a natural-first test: the geometry fits bedrock fracture, while human signatures are absent. The Signature test: tool marks, quarries, or artifacts appear in situ. It would be refuted if fracture analysis reproduces every feature naturally.'),
        key_points=[
            "Stepped terraces at 25 meters depth off Yonaguni, found 1986.",
            "Right angles and terraces resemble architecture.",
            "Local sandstone fractures naturally into blocks.",
            "No tools, quarries, or artifacts have been found.",
        ],
        requirements=[
            "Exhaustion of natural explanations before human ones.",
            "Positive human signatures: tools, quarries, modifications.",
            "Dating consistent with pre-inundation construction if artificial.",
        ],
        standards=[
            "Claims checked against the geological and archaeological literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Kimura M. Yonaguni kaitei chikei. 2004.",
            "Schoch R. Yonaguni enigma. 2006.",
        ],
        hypotheses=[
            "The formations are entirely natural sandstone fracturing.",
            "Natural terraces were modified by humans.",
            "A pre-inundation culture built the complex around 10,000 BCE.",
            "The site mixes natural geology with later human additions.",
        ],
        confirm="Tool marks, quarries, or artifacts appear in situ.",
        refute="Fracture analysis reproduces every feature naturally.",
    ),
    dict(
        key="archaeology-26",
        name="The Lost Library of Alexandria",
        group="Lost Knowledge",
        ladder_rank=26,
        ladder_tier="advanced",
        problem=("What was actually lost when the Library of Alexandria declined - and "
                 "how much of antiquity's knowledge vanished with it?"),
        background=("The Library's end is itself a mystery: Julius Caesar's fire (48 "
                    "BCE), Aurelian, Diocletian, Christian mobs, Arab conquerors - each "
                    "blamed, none proven as the single end. Scholars now see a long "
                    "decline, not one fire. The deeper question is the counterfactual: "
                    "how many works existed only there? Estimates range from "
                    "civilization-altering to marginal, since most important texts "
                    "survived in other copies."),
        why_it_matters=("The Library is the symbol of lost knowledge. Quantifying the "
                        "real loss separates history from romance - and tells us what "
                        "fragility means for knowledge today."),
        sig_lens=("The Signature lens treats the Library as a redundancy ledger: the "
                  "Signature approach asks what existed in exactly one copy."),
        sig_body=("The Signature proposal models ancient knowledge as a copy network. "
                  "Assumptions: (1) important texts were copied across cities; (2) the "
                  "Library's unique holdings were disproportionately obscure works; (3) "
                  "decline was gradual, allowing salvage. Reasoning path: the proposal "
                  "shows the catastrophic-loss narrative requires single-copy "
                  "uniqueness at scale - but the surviving record suggests most "
                  "significant works had multiple copies, and the real losses were the "
                  "long tail of minor works. The Library's fall was a tragedy of the "
                  "margins, not the canon. Limits: the catalog itself is lost; "
                  "uniqueness ratios are estimated."),
        pointer=('The Signature system models ancient texts as a copy network, arguing the real losses were the long tail of minor works, not the canon. The Signature test: copy-network analysis shows low single-copy ratios for major works. It would be refuted if the catalog surfaces, revealing vast unique holdings.'),
        key_points=[
            "No single destruction event is proven; decline was gradual.",
            "Multiple culprits are blamed across eight centuries.",
            "Most important texts survived in other copies.",
            "The true catalog is lost, so losses are estimated.",
        ],
        requirements=[
            "Separation of the destruction myth from the decline evidence.",
            "Estimates of single-copy uniqueness in the collection.",
            "An account of what the surviving record implies about losses.",
        ],
        standards=[
            "Claims checked against the Library scholarship; myths marked.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Canfora L. The Vanished Library. University of California Press; 1990.",
            "El-Abbadi M. Life and Fate of the Ancient Library of Alexandria. UNESCO; 1992.",
        ],
        hypotheses=[
            "Losses were concentrated in obscure works; the canon survived.",
            "A catastrophic fire destroyed unique holdings at scale.",
            "The decline was institutional; texts dispersed rather than burned.",
            "Christian and later destructions were the decisive blows.",
        ],
        confirm="Copy-network analysis shows low single-copy ratios for major works.",
        refute="The catalog surfaces, revealing vast unique holdings.",
    ),
    dict(
        key="archaeology-27",
        name="The Bronze Age Collapse",
        group="Collapses",
        ladder_rank=27,
        ladder_tier="advanced",
        problem=("What caused the Bronze Age collapse - the near-simultaneous fall of "
                 "palace civilizations across the eastern Mediterranean around 1200 BCE?"),
        background=("Within decades, Mycenaean palaces, the Hittite Empire, and Levantine "
                    "cities fell; Egypt survived weakened. Candidates: Sea Peoples, "
                    "earthquakes, drought, systems collapse, revolts. Eric Cline argues "
                    "for a 'perfect storm' of interacting stresses. The deeper puzzle is "
                    "synchronicity: why did independent kingdoms fail together?"),
        why_it_matters=("The collapse is history's first systems failure - a Bronze Age "
                        "globalization unraveling. Its mechanics may be the mechanics of "
                        "all civilizational collapses."),
        sig_lens=("The Signature lens treats the collapse as a network ledger: the "
                  "Signature approach asks what the palace economies shared that "
                  "failed everywhere at once."),
        sig_body=("The Signature proposal models the palace world as a brittle network. "
                  "Assumptions: (1) palace economies were deeply interdependent "
                  "(tin, grain, prestige goods); (2) each was optimized for surplus "
                  "extraction, not resilience; (3) drought hit the network's food "
                  "base. Reasoning path: the proposal shows interdependence converts "
                  "local shocks into system-wide cascades - a drought here, a revolt "
                  "there, raiders everywhere - explaining synchronicity without a "
                  "single cause. The Sea Peoples become the network's debris, not its "
                  "destroyers. Limits: cascade models need trade-volume data that "
                  "barely exists; some destructions resist the network account."),
        pointer=('The Signature system models the palace world as a brittle interdependent network, where local shocks cascaded system-wide. The Signature test: trade-network models reproduce the synchronized failure pattern. It would be refuted if kingdoms with no network ties collapse in the same window.'),
        key_points=[
            "Multiple kingdoms fell within decades around 1200 BCE.",
            "Palace economies were interdependent on tin, grain, and prestige goods.",
            "Drought evidence is strong but regionally uneven.",
            "Synchronicity is the core puzzle - independent failures should not align.",
        ],
        requirements=[
            "A mechanism producing synchronized multi-kingdom failure.",
            "Consistency with Egypt's partial survival.",
            "Separation of triggers from structural vulnerability.",
        ],
        standards=[
            "Claims checked against the collapse literature; speculation marked.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Cline EH. 1177 B.C.: The Year Civilization Collapsed. Princeton University Press; 2014.",
            "Kaniewski D et al. Drought and societal collapse 3200 years ago. PLoS ONE; 2013.",
        ],
        hypotheses=[
            "Interdependent-network cascade explains the synchronicity.",
            "Drought was the prime mover; everything else followed.",
            "The Sea Peoples were the primary destroyers.",
            "Internal revolts against palace elites drove the falls.",
        ],
        confirm="Trade-network models reproduce the synchronized failure pattern.",
        refute="Kingdoms with no network ties collapse in the same window.",
    ),
    dict(
        key="archaeology-28",
        name="The Maya Collapse",
        group="Collapses",
        ladder_rank=28,
        ladder_tier="advanced",
        problem=("Why did the Classic Maya cities of the southern lowlands collapse in "
                 "the 9th century CE while northern cities survived?"),
        background=("Between about 800 and 900 CE, dozens of southern lowland cities "
                    "were abandoned amid warfare, monument defacement, and population "
                    "crash. Drought evidence from lake cores is strong; warfare "
                    "intensified; elites may have lost legitimacy. Yet the Maya as a "
                    "people never vanished - millions live today - and northern "
                    "cities like Chichen Itza thrived. 'Collapse' may misdescribe a "
                    "political transformation."),
        why_it_matters=("The Maya collapse is the most studied societal failure in the "
                        "Americas - and a test case for how climate, war, and politics "
                        "interact."),
        sig_lens=("The Signature lens treats the collapse as a legitimacy ledger: the "
                  "Signature approach asks what kings owed their people that drought "
                  "made unpayable."),
        sig_body=("The Signature proposal models the collapse as a legitimacy bankruptcy. "
                  "Assumptions: (1) Maya kings legitimized rule through ritual "
                  "control of rain and fertility; (2) prolonged drought made the "
                  "rituals visibly fail; (3) warfare consumed the remaining surplus. "
                  "Reasoning path: the proposal shows drought alone rarely topples "
                  "states - but drought that falsifies the king's core claim does. "
                  "Southern divine kingship was drought-fragile; northern cities with "
                  "different political structures survived. The abandonment was then "
                  "political exit, not demographic extinction. Limits: warfare's "
                  "independent role is debated; the drought chronology has gaps."),
        pointer=("The Signature system models the collapse as legitimacy bankruptcy: drought falsified divine kingship's core claim. The Signature test: abandonment tracks legitimacy-crisis markers better than drought alone. It would be refuted if southern cities with intact kingship survive the drought episodes."),
        key_points=[
            "Southern lowland cities abandoned about 800-900 CE.",
            "Lake cores show severe drought episodes.",
            "Warfare and monument defacement intensified.",
            "Northern cities survived; Maya peoples never vanished.",
        ],
        requirements=[
            "An account of the north-south divergence.",
            "A mechanism linking drought to political failure.",
            "Separation of political collapse from demographic extinction.",
        ],
        standards=[
            "Claims checked against the Maya literature; speculation marked.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Diamond J. Collapse. Viking; 2005.",
            "Aimers JJ. What Maya collapse? Journal of Archaeological Science; 2007.",
        ],
        hypotheses=[
            "Drought bankrupted divine-kingship legitimacy.",
            "Endemic warfare consumed the surplus independently.",
            "Environmental degradation (deforestation, erosion) was primary.",
            "It was political transformation, not collapse.",
        ],
        confirm="Abandonment tracks legitimacy-crisis markers better than drought alone.",
        refute="Southern cities with intact kingship survive the drought episodes.",
    ),
    dict(
        key="archaeology-29",
        name="The Rapa Nui Revision",
        group="Collapses",
        ladder_rank=29,
        ladder_tier="advanced",
        problem=("Did Easter Island's people really destroy their own environment "
                 "in 'ecocide' - or is the famous collapse story wrong?"),
        background=("The classic story: Rapa Nui islanders cut every tree, triggering "
                    "war, starvation, and toppling the moai. Recent work challenges "
                    "nearly every element: rats may have eaten the palm nuts, the "
                    "'collapse' predates European contact weakly, and the population "
                    "was likely stable until disease and slave raids devastated it. "
                    "The ecocide narrative may say more about modern anxieties than "
                    "island history."),
        why_it_matters=("Rapa Nui is the parable of self-inflicted environmental "
                        "collapse, cited in every sustainability debate. If the parable "
                        "is wrong, the lesson changes."),
        sig_lens=("The Signature lens treats the island as a blame ledger: the "
                  "Signature approach asks what each version of the story is used "
                  "to prove."),
        sig_body=("The Signature proposal models the island's history as resilient "
                  "adaptation misread as collapse. Assumptions: (1) the palm decline "
                  "involved rats plus human use; (2) lithic mulch gardens sustained "
                  "agriculture without trees; (3) European disease and slave raids "
                  "caused the documented population crash. Reasoning path: the "
                  "proposal shows the archaeological signal - continued monument "
                  "building, garden intensification - matches adaptation, not "
                  "collapse, until contact. The 'ecocide' then becomes a projection "
                  "of modern fears onto an ambiguous record. Limits: the deforestation "
                  "agents remain debated; pre-contact population trends are "
                  "uncertain."),
        pointer=("The Signature system reads the island's record as resilient adaptation until contact, with ecocide as modern projection. The Signature test: pre-contact populations prove stable through the deforestation period. It would be refuted if secure pre-contact evidence shows demographic collapse."),
        key_points=[
            "The classic ecocide story blames islanders for deforestation and collapse.",
            "Rats, gardens, and adaptation evidence challenge the story.",
            "Documented population crash follows European contact.",
            "The narrative is widely used in sustainability debates.",
        ],
        requirements=[
            "Separation of pre-contact from post-contact population trends.",
            "An account of palm decline agents.",
            "Consistency with continued monument construction.",
        ],
        standards=[
            "Claims checked against the recent Rapa Nui literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Hunt TL, Lipo CP. The human transformation of Rapa Nui. American Scientist; 2009.",
            "Diamond J. Collapse. Viking; 2005.",
        ],
        hypotheses=[
            "Adaptation, not ecocide; contact caused the real crash.",
            "Classic ecocide occurred but earlier and less totally.",
            "Rats were the primary deforestation agent.",
            "Inter-clan warfare drove a genuine pre-contact decline.",
        ],
        confirm="Pre-contact populations prove stable through the deforestation period.",
        refute="Secure pre-contact evidence shows demographic collapse.",
    ),
    dict(
        key="archaeology-30",
        name="The Lost City of Ubar",
        group="Lost Cities",
        ladder_rank=30,
        ladder_tier="advanced",
        problem=("Was a lost frankincense-trade city - Ubar, the 'Atlantis of the Sands' "
                 "- actually found by satellite archaeology in Oman?"),
        background=("In 1992, satellite imagery guided expeditions to Shisr in Oman, "
                    "where a collapsed limestone sinkhole-fortress was proclaimed Ubar. "
                    "Critics note the site is small, the identification rests on "
                    "medieval legends, and frankincense-trade infrastructure was "
                    "decentralized. The discovery pioneered space archaeology - but "
                    "whether it found a legend or a waystation remains disputed."),
        why_it_matters=("Ubar was the test case for satellite archaeology. Its verdict "
                        "calibrates every space-based discovery claim since."),
        sig_lens=("The Signature lens treats Ubar as an identification ledger: the "
                  "Signature approach asks what a legend-city must leave behind."),
        sig_body=("The Signature proposal models the identification as a category "
                  "error. Assumptions: (1) frankincense trade used dispersed "
                  "waystations, not one great city; (2) medieval legends conflate "
                  "multiple sites; (3) Shisr is a real, significant fortress. "
                  "Reasoning path: the proposal shows Shisr matches a trade "
                  "waystation perfectly and a legend-city poorly - the satellite "
                  "found something real, but the name came from legend. The "
                  "methodological win (space archaeology works) survives the "
                  "identification loss. Limits: legend may preserve genuine memory; "
                  "the full trade network is unmapped."),
        pointer=("The Signature system separates the real waystation the satellites found from the legend-city name attached to it. The Signature test: trade-network mapping shows dispersed waystations, no center. It would be refuted if shisr's scale proves far larger than a waystation."),
        key_points=[
            "Satellite imagery guided the 1992 Shisr expedition.",
            "The site is a collapsed fortress over a sinkhole.",
            "Critics call it a waystation, not a lost great city.",
            "The case pioneered satellite archaeology methods.",
        ],
        requirements=[
            "Evidence distinguishing waystation from great city.",
            "Source criticism of the Ubar legends.",
            "Mapping of the actual frankincense trade network.",
        ],
        standards=[
            "Claims checked against the Ubar literature; speculation marked.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Clapp N. The Road to Ubar. Houghton Mifflin; 1999.",
            "Zarins J. Environmental disruption and human response. 1997.",
        ],
        hypotheses=[
            "Shisr is a waystation; Ubar is composite legend.",
            "Shisr is genuinely the legendary city.",
            "The trade network had no single great city.",
            "A larger Ubar remains undiscovered nearby.",
        ],
        confirm="Trade-network mapping shows dispersed waystations, no center.",
        refute="Shisr's scale proves far larger than a waystation.",
    ),
    dict(
        key="archaeology-31",
        name="Doggerland: The Drowned Mesolithic",
        group="Deep History",
        ladder_rank=31,
        ladder_tier="advanced",
        problem=("What was life like in Doggerland - the inhabited North Sea plain that "
                 "connected Britain to Europe until about 6500 BCE - and what did its "
                 "drowning do to Mesolithic societies?"),
        background=("Doggerland was larger than many modern countries, inhabited for "
                    "millennia, then drowned by rising seas - possibly catastrophically "
                    "in the Storegga tsunami. Fishing trawlers recover bones, tools, "
                    "and even worked wood. Seismic survey maps its rivers and hills. "
                    "But no settlement has been excavated in situ, and the human story "
                    "- population size, response to the flooding - is almost entirely "
                    "inferred."),
        why_it_matters=("Doggerland is Europe's lost inhabited country - a whole Mesolithic "
                        "world under the sea. Its story is the deep history of "
                        "climate displacement."),
        sig_lens=("The Signature lens treats Doggerland as a displacement ledger: the "
                  "Signature approach asks how fast the water came and where the "
                  "people went."),
        sig_body=("The Signature proposal models the drowning as a graded retreat, not "
                  "a single catastrophe. Assumptions: (1) sea-level rise was mostly "
                  "gradual with tsunami punctuations; (2) the plain's rivers and "
                  "hills structured settlement; (3) neighboring uplands could absorb "
                  "migrants. Reasoning path: the proposal maps habitable area against "
                  "sea-level curves to show the drowning took millennia - time enough "
                  "for orderly retreat, with the Storegga tsunami as a punctuation, "
                  "not the story. The archaeological signal should then be "
                  "abandonment gradients, not mass death. Limits: no in-situ "
                  "settlement confirms the model; population estimates are rough."),
        pointer=('The Signature system models the drowning as a millennia-long graded retreat, with the tsunami as punctuation rather than the story. The Signature test: abandonment gradients match the graded-retreat model. It would be refuted if in-situ sites show sudden catastrophic abandonment everywhere.'),
        key_points=[
            "Doggerland connected Britain to Europe until about 6500 BCE.",
            "Seismic surveys map its rivers, hills, and coastlines.",
            "Trawlers recover bones, tools, and worked wood.",
            "No settlement has been excavated in situ.",
        ],
        requirements=[
            "Sea-level curves matched to habitable-area loss.",
            "An account of where displaced populations went.",
            "In-situ settlement evidence to test the models.",
        ],
        standards=[
            "Claims checked against the Doggerland literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Gaffney V, Fitch S, Smith D. Europe's Lost World. Council for British Archaeology; 2009.",
            "Coles BJ. Doggerland: a speculative survey. 1998.",
        ],
        hypotheses=[
            "Gradual retreat over millennia absorbed the population.",
            "The Storegga tsunami caused catastrophic displacement.",
            "Doggerland was densely populated; its loss reshaped Mesolithic Europe.",
            "It was marginal land, sparsely used.",
        ],
        confirm="Abandonment gradients match the graded-retreat model.",
        refute="In-situ sites show sudden catastrophic abandonment everywhere.",
    ),
    dict(
        key="archaeology-32",
        name="The Terracotta Army Workshops",
        group="Monuments",
        ladder_rank=32,
        ladder_tier="advanced",
        problem=("How was the Terracotta Army actually produced - 8,000 individualized "
                 "figures in a few decades - and what does the production system reveal "
                 "about the Qin state?"),
        background=("The figures combine mold-made parts with individualized finishing; "
                    "inscriptions name workshops and supervisors. Recent work shows "
                    "assembly-line production with quality control, yet each face "
                    "differs. Open questions: the full workshop layout, labor "
                    "recruitment (convict? corvee? artisan?), production rate, and how "
                    "the project related to Qin administrative innovations."),
        why_it_matters=("The army is ancient history's largest known manufacturing project. "
                        "Its production system is the Qin state made visible."),
        sig_lens=("The Signature lens treats the army as a production ledger: the "
                  "Signature approach reconstructs the factory from the figures."),
        sig_body=("The Signature proposal models production as modular assembly with "
                  "artisan finishing. Assumptions: (1) body parts were mold-made in "
                  "batches; (2) faces were individualized after assembly; (3) "
                  "inscriptions track workshop accountability. Reasoning path: the "
                  "proposal shows the figure variation clusters by workshop - molds "
                  "shared within teams, finishing styles marking artisans - revealing "
                  "a cellular production system where teams competed on quality. "
                  "Throughput estimates then date the project's phases. Limits: "
                  "workshop sites are only partly excavated; labor-source evidence "
                  "is thin."),
        pointer=('The Signature system reconstructs a cellular workshop system from figure variation, with teams competing on quality. The Signature test: excavated workshops match the cellular variation model. It would be refuted if figures show no workshop clustering; production was fully centralized.'),
        key_points=[
            "About 8,000 figures, mold-made parts with individualized faces.",
            "Inscriptions name workshops and supervisors.",
            "Production combined assembly-line methods with artisan finishing.",
            "Workshop sites are only partly excavated.",
        ],
        requirements=[
            "Throughput estimates consistent with the construction timeline.",
            "Workshop archaeology confirming the cellular model.",
            "Evidence on labor recruitment and organization.",
        ],
        standards=[
            "Claims checked against the Terracotta Army literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Ledderose L. Ten Thousand Things. Princeton University Press; 2000.",
            "Quinn P et al. Organisation of the Terracotta Army workshops. Antiquity; 2017.",
        ],
        hypotheses=[
            "Cellular workshops with mold-sharing and artisan finishing.",
            "Centralized imperial factory with strict standardization.",
            "Convict labor under military-style organization.",
            "Production spanned decades longer than assumed.",
        ],
        confirm="Excavated workshops match the cellular variation model.",
        refute="Figures show no workshop clustering; production was fully centralized.",
    ),
    dict(
        key="archaeology-33",
        name="The Vinland Map: Genuine or Forgery",
        group="Contested Sites",
        ladder_rank=33,
        ladder_tier="advanced",
        problem=("Is the Vinland Map - showing Norse America decades before Columbus, "
                 "dated by some to 1440 - genuine or a 20th-century forgery?"),
        background=("The map surfaced in the 1950s bound with medieval manuscripts. "
                    "It depicts Vinland with surprising accuracy. Scientific tests "
                    "split: 1970s ink analysis found modern anatase (forgery), but "
                    "later work questioned the sampling, and radiocarbon dates the "
                    "parchment to about 1434. Yale authenticates; many scholars "
                    "doubt. The stakes: proof of pre-Columbian Norse cartography of "
                    "America."),
        why_it_matters=("The map would be the earliest cartographic record of America - "
                        "or the most audacious map forgery ever made. The methods used "
                        "to judge it calibrate forgery detection everywhere."),
        sig_lens=("The Signature lens treats the map as a materials ledger: the "
                  "Signature approach asks what the ink, parchment, and wormholes "
                  "each independently say."),
        sig_body=("The Signature proposal models the evidence as independent material "
                  "clocks. Assumptions: (1) parchment date constrains but does not "
                  "prove map date (old parchment can be reused); (2) ink chemistry "
                  "reflects manufacture era; (3) wormholes shared with the bound "
                  "manuscripts prove contemporaneous binding. Reasoning path: the "
                  "proposal shows the clocks disagree - old parchment, disputed ink - "
                  "which is exactly the signature of a forgery on genuinely old "
                  "material OR a genuine map with contaminated sampling. The "
                  "wormhole evidence becomes decisive: shared holes mean the map "
                  "was bound with the manuscripts centuries ago. Limits: the ink "
                  "sampling controversy is unresolved; access to the map is "
                  "restricted."),
        pointer=('The Signature system treats parchment, ink, and wormholes as independent clocks, with shared wormholes as the decisive test. The Signature test: independent ink analysis with clean sampling shows medieval ink. It would be refuted if controlled re-testing confirms modern ink throughout.'),
        key_points=[
            "Surfaced in the 1950s; depicts Norse Vinland.",
            "Parchment radiocarbon-dated to about 1434.",
            "Ink analysis split: modern anatase found, then questioned.",
            "Wormholes shared with bound manuscripts suggest old binding.",
        ],
        requirements=[
            "Independent ink analysis with documented sampling.",
            "Reconciliation of the parchment and ink clocks.",
            "An account of the wormhole evidence.",
        ],
        standards=[
            "Claims checked against the Vinland Map literature; speculation marked.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Skelton RA et al. The Vinland Map and the Tartar Relation. Yale University Press; 1965.",
            "Cummings A et al. Raman spectroscopy of the Vinland Map ink. 2002.",
        ],
        hypotheses=[
            "Genuine 15th-century map on 15th-century parchment.",
            "Modern forgery drawn on genuinely old parchment.",
            "The ink tests were contaminated; re-testing will vindicate it.",
            "It is a composite: old map copied later onto old parchment.",
        ],
        confirm="Independent ink analysis with clean sampling shows medieval ink.",
        refute="Controlled re-testing confirms modern ink throughout.",
    ),
    dict(
        key="archaeology-34",
        name="The Theory Wars: Can Archaeology Unify",
        group="Methods",
        ladder_rank=34,
        ladder_tier="advanced",
        problem=("After sixty years of processual versus post-processual warfare, can "
                 "archaeology build a unified theory - or is the field permanently "
                 "divided between science and story?"),
        background=("Processualists (Binford) demanded hypothesis-testing science; "
                    "post-processualists (Hodder, Shanks) insisted meaning, agency, "
                    "and politics cannot be quantified. The wars cooled into "
                    "pragmatic pluralism, but the core tension remains: can one "
                    "discipline be both a science of the past and a humanity of "
                    "meaning? Ancient DNA and big data have tilted the field back "
                    "toward science - provoking new resistance."),
        why_it_matters=("This is archaeology's philosophy made practical: the answer "
                        "determines what counts as evidence, what explanations are "
                        "allowed, and what the field can claim to know."),
        sig_lens=("The Signature lens treats the wars as a levels ledger: the "
                  "Signature approach asks which questions belong to which level "
                  "of explanation."),
        sig_body=("The Signature proposal models the divide as a levels confusion. "
                  "Assumptions: (1) archaeological questions span physical, "
                  "biological, and meaningful levels; (2) methods fit levels, not "
                  "fields; (3) both camps overclaim jurisdiction. Reasoning path: "
                  "the proposal assigns dating, diet, and demography to scientific "
                  "methods and meaning, identity, and experience to interpretive "
                  "ones - with the bridge being middle-range theory that translates "
                  "between them. Unity comes not from one method but from a "
                  "disciplined division of labor. Limits: the boundary cases - "
                  "ritual, collapse, inequality - resist clean assignment; "
                  "practitioners may reject the truce."),
        pointer=('The Signature system assigns methods to levels of explanation, proposing unity through disciplined division of labor rather than one method. The Signature test: bridge theories produce verified predictions across levels. It would be refuted if no middle-range translation survives testing.'),
        key_points=[
            "Processualism demanded scientific hypothesis-testing.",
            "Post-processualism insisted on meaning, agency, and politics.",
            "Ancient DNA and big data tilted the field back toward science.",
            "Pragmatic pluralism prevails, but the tension is unresolved.",
        ],
        requirements=[
            "A framework assigning methods to question types.",
            "Middle-range theory bridging material pattern and human meaning.",
            "Testable claims about where each approach works.",
        ],
        standards=[
            "Claims checked against the archaeological-theory literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Binford LR. In Pursuit of the Past. Thames and Hudson; 1983.",
            "Hodder I. Reading the Past. Cambridge University Press; 1986.",
        ],
        hypotheses=[
            "A levels-based division of labor can unify the field.",
            "The divide is philosophical and permanent.",
            "Big data will dissolve the interpretive side.",
            "Interpretive critique will dissolve the scientistic side.",
        ],
        confirm="Bridge theories produce verified predictions across levels.",
        refute="No middle-range translation survives testing.",
    ),
]
