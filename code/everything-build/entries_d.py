#!/usr/bin/env python3
"""PHASE D — Everything databases, entries part D: linguistics & language,
art & music, education, agriculture & food, energy.
(key, group, title, desc, points, requirements, standards, citations, demo_kind, src)
"""

ENTRIES_D = [
# ============================== LINGUISTICS & LANGUAGE ==============================
("phonetics", "Core Linguistics",
 "Phonetics: The Sounds of Speech",
 "Phonetics studies speech sounds physically: how they are produced (articulatory), transmitted "
 "(acoustic), and perceived (auditory). The vocal tract — lungs, larynx, tongue, lips — shapes airflow "
 "into consonants (classified by place, manner, and voicing) and vowels (classified by tongue height, "
 "backness, and lip rounding). The International Phonetic Alphabet assigns every distinguishable speech "
 "sound a symbol, letting linguists transcribe any language precisely. Acoustic phonetics reads sounds as "
 "waveforms and spectrograms, the basis of speech technology.",
 ["Articulatory, acoustic, and auditory branches",
  "Consonants by place, manner, voicing",
  "Vowels by height, backness, rounding",
  "IPA: one symbol per distinguishable sound",
  "Spectrograms underlie speech technology"],
 "General reading level.",
 ["IPA conventions"],
 "Standard linguistics literature (phonetics textbooks).",
 "ling", "public-harvest"),
("phonology", "Core Linguistics",
 "Phonology: Sound Patterns and Rules",
 "Phonology studies how sounds pattern in a language — which sounds contrast, which vary predictably. "
 "Phonemes are contrastive units: swapping /p/ and /b/ changes 'pat' to 'bat' in English. Allophones are "
 "predictable variants, like aspirated [pʰ] at word starts. Phonological rules describe alternations — "
 "English plural -s pronounced /s/, /z/, or /ɪz/ by environment. Syllable structure, stress, and tone "
 "organize sounds above the segment. Phonology is why accents are systematic, not sloppy.",
 ["Phonemes contrast; allophones vary predictably",
  "Minimal pairs reveal phoneme inventories",
  "Rules describe environment-driven alternations",
  "Syllable, stress, tone above the segment",
  "Accents as systematic rule differences"],
 "Phonetics basics helpful.",
 ["IPA conventions"],
 "Standard linguistics literature (phonology textbooks).",
 "ling", "public-harvest"),
("morphology", "Core Linguistics",
 "Morphology: The Structure of Words",
 "Morphology studies word structure. Morphemes — the smallest meaningful units — combine as roots, "
 "prefixes, suffixes, infixes. Inflectional morphology marks grammar (English -s for plural, -ed for past) "
 "without making new words; derivational morphology builds them (happy -> happiness). Languages range from "
 "isolating (few morphemes per word, like Mandarin) through agglutinating (long transparent chains, like "
 "Turkish) to fusional (morphemes fused, like Latin endings). Compounding joins roots — 'blackboard' — in "
 "every language family.",
 ["Morphemes: smallest meaningful units",
  "Inflection marks grammar; derivation builds words",
  "Isolating, agglutinating, fusional language types",
  "Compounding joins roots universally",
  "Word structure reveals language organization"],
 "General reading level.",
 ["Standard morphological terminology"],
 "Standard linguistics literature (morphology textbooks).",
 "ling", "public-harvest"),
("syntax", "Core Linguistics",
 "Syntax: The Structure of Sentences",
 "Syntax studies how words combine into sentences. Constituency: words group into phrases (noun phrases, "
 "verb phrases) that behave as units — movement and substitution tests reveal them. Word order varies: SVO "
 "(English), SOV (Japanese, Hindi), VSO (Irish) cover most languages. Recursion — phrases inside phrases "
 "without bound — is syntax's signature property. Agreement, case, and tense anchor the structure. Modern "
 "theories from phrase-structure rules to dependency grammars all model the same human capacity: infinite "
 "sentences from finite means.",
 ["Constituents: phrases as behavioral units",
  "Word orders: SVO, SOV, VSO and rarer patterns",
  "Recursion: unbounded phrases in phrases",
  "Agreement, case, tense anchor structure",
  "Infinite sentences from finite means"],
 "General reading level.",
 ["Standard syntactic terminology"],
 "Standard linguistics literature (syntax textbooks).",
 "ling", "public-harvest"),
("semantics", "Core Linguistics",
 "Semantics: Meaning and Reference",
 "Semantics studies linguistic meaning. Lexical semantics maps word senses — polysemy (related senses) "
 "versus homonymy (accidental sameness) — and relations like synonymy, antonymy, hyponymy. Compositional "
 "semantics builds sentence meaning from parts by rule. Truth conditions state when sentences are true; "
 "entailment tracks what follows from what. Pragmatics, semantics' neighbor, studies meaning in use: "
 "implicature (what's implied beyond what's said), speech acts, politeness. 'Can you pass the salt?' is "
 "grammatically a question and functionally a request.",
 ["Word senses: polysemy versus homonymy",
  "Compositional meaning from parts by rule",
  "Truth conditions and entailment",
  "Pragmatics: meaning in use",
  "Implicature and speech acts"],
 "General reading level.",
 ["Standard semantic terminology"],
 "Standard linguistics literature (semantics textbooks).",
 "ling", "public-harvest"),
("language-acquisition", "Applied",
 "Language Acquisition: How Children Learn Language",
 "Children acquire language on a maturational schedule: cooing, babbling, first words around twelve months, "
 "two-word combinations, then rapid grammar growth — all without instruction. The poverty-of-the-stimulus "
 "argument notes children master rules from limited, messy input, suggesting innate linguistic capacity "
 "(Universal Grammar in Chomskyan theory). Critical-period evidence: late first-language exposure yields "
 "incomplete grammar. Second-language acquisition differs — age effects, transfer from the first language, "
 "and instruction all matter. Every normal child in every culture succeeds: the most reliable learning "
 "feat humans perform.",
 ["Maturational schedule: babbling to grammar",
  "Poverty of the stimulus suggests innate capacity",
  "Critical period for first-language mastery",
  "Second-language learning differs systematically",
  "Universal success across cultures"],
 "General reading level.",
 ["Standard acquisition terminology"],
 "Standard linguistics literature (acquisition references).",
 "ling", "public-harvest"),
("sociolinguistics", "Applied",
 "Sociolinguistics: Language in Society",
 "Sociolinguistics studies language variation across social dimensions. Dialects — regional and social "
 "varieties — are rule-governed systems, not corruptions; Labov's department-store study showed "
 "stratification by class in a single sound. Code-switching moves between varieties by context. Language "
 "attitudes attach prestige or stigma to varieties with real consequences for speakers. Language contact "
 "produces pidgins (simplified trade languages) and creoles (pidgins nativized as mother tongues). "
 "Language endangerment — most of the world's 7,000 languages declining — makes documentation urgent.",
 ["Dialects as rule-governed systems",
  "Variation stratified by class, age, gender, context",
  "Code-switching by situation",
  "Pidgins and creoles from language contact",
  "Endangerment and documentation urgency"],
 "General reading level.",
 ["Standard sociolinguistic terminology"],
 "Standard linguistics literature (sociolinguistics references).",
 "ling", "public-harvest"),
("writing-systems", "Core Linguistics",
 "Writing Systems: Alphabets to Logograms",
 "Writing systems encode language visually in three great types. Logographic systems (Chinese characters) "
 "represent morphemes — thousands of signs, learned over years. Syllabaries (Japanese kana, Cherokee) "
 "represent syllables — dozens of signs. Alphabets (Latin, Greek, Cyrillic, Arabic, Devanagari) represent "
 "sounds — two to three dozen signs, the most economical. Orthographic depth varies: Spanish spelling is "
 "shallow (letters match sounds), English deep (history frozen in). Writing was invented independently at "
 "least three times: Mesopotamia, Egypt, Mesoamerica.",
 ["Logographic, syllabic, alphabetic: three great types",
  "Alphabets most economical in sign count",
  "Orthographic depth: shallow to deep spelling",
  "Independent inventions: Mesopotamia, Egypt, Mesoamerica",
  "Writing transforms memory and administration"],
 "General reading level.",
 ["Unicode terminology"],
 "Standard linguistics literature (writing-system references).",
 "ling", "public-harvest"),
("sig-grammar-engine", "Signature Linguistics",
 "Signature Grammar Engine",
 "A Signature original engine that parses sentences as deterministic Signature structures: words tagged, "
 "phrases bracketed, dependencies drawn as verifiable links — the same sentence always yields the same "
 "parse. Grammar rules are stated explicitly as the engine's constitution, so every analysis is auditable "
 "against them. Built as an educational instrument for understanding syntactic structure across languages.",
 ["Sentences as deterministic structures",
  "Tagging, bracketing, dependencies as verifiable links",
  "Same sentence, same parse, every run",
  "Grammar rules stated as an auditable constitution",
  "Educational instrument for syntactic structure"],
 "Syntax basics.",
 ["Signature system conventions"],
 "Original Signature design; facts per standard linguistics literature.",
 "ling", "signature"),
("sig-sound-analyzer", "Signature Linguistics",
 "Signature Sound Pattern Analyzer",
 "A Signature original instrument that analyzes sound patterns as Signature records: phoneme inventories "
 "cataloged, minimal pairs detected deterministically, alternation rules stated as explicit "
 "environment mappings. Accent and dialect differences become comparable rule sets rather than vague "
 "impressions. A Signature treatment of phonology as exact, comparable pattern records.",
 ["Phoneme inventories as cataloged records",
  "Minimal pairs detected deterministically",
  "Alternation rules as explicit mappings",
  "Dialect differences as comparable rule sets",
  "Phonology as exact pattern records"],
 "Phonology basics.",
 ["Signature system conventions; IPA"],
 "Original Signature design; facts per standard linguistics literature.",
 "ling", "signature"),
("sig-translation-mapper", "Signature Linguistics",
 "Signature Translation Mapper",
 "A Signature original instrument that maps translation as structured Signature records: source segments "
 "aligned to target segments, meaning preserved as annotated correspondences, divergences flagged where "
 "languages carve reality differently. The mapper is a study instrument for understanding how meaning "
 "moves between languages — it organizes human translation work, never replaces the translator's judgment.",
 ["Segments aligned as structured records",
  "Meaning as annotated correspondences",
  "Divergences flagged where languages differ",
  "Organizes translation study",
  "Supports translators; never replaces judgment"],
 "General reading level.",
 ["Signature system conventions"],
 "Original Signature design; facts per standard linguistics literature.",
 "ling", "signature"),
("sig-language-optimizer", "Signature Linguistics",
 "Signature Language Learning Optimizer",
 "A Signature original engine that builds language-study plans from established learning science: "
 "vocabulary scheduled by spaced repetition, grammar introduced in dependency order, input kept "
 "comprehensible by rule. The learner's target language becomes a Signature curriculum record; the plan "
 "is reproducible and openly reasoned. A Signature treatment of language study as transparent, "
 "well-ordered scheduling.",
 ["Vocabulary by spaced repetition",
  "Grammar in dependency order",
  "Comprehensible input scheduled by rule",
  "Curriculum as an explicit record",
  "Transparent well-ordered scheduling"],
 "General reading level.",
 ["Signature system conventions"],
 "Original Signature design; methods per standard acquisition literature.",
 "ling", "signature"),
# ============================== ART & MUSIC ==============================
("drawing-fundamentals", "Visual Art",
 "Drawing Fundamentals: Line, Form, Perspective",
 "Drawing is seeing made visible. Line describes contour and gesture; value (light to dark) models form "
 "through shading — the sphere rendered by highlight, midtone, core shadow, reflected light, cast shadow. "
 "Linear perspective organizes space: parallel lines converge at vanishing points on the horizon line, "
 "one-point for corridors, two-point for corners, three-point for towers. Proportion is measured by "
 "comparison — the head as the figure's unit. Gesture drawing captures action in seconds; sustained study "
 "builds accuracy. Every visual art rests on these foundations.",
 ["Line describes contour and gesture",
  "Value models three-dimensional form",
  "Linear perspective: vanishing points organize space",
  "Proportion by comparative measurement",
  "Gesture versus sustained study"],
 "Paper, pencil, and observation.",
 ["Standard art terminology"],
 "Standard art literature (drawing references).",
 "artmusic", "public-harvest"),
("color-theory", "Visual Art",
 "Color Theory: Hue, Value, and Harmony",
 "Color theory organizes the visible spectrum for makers. Hue names the color family; value its lightness; "
 "saturation its intensity — the three dimensions of every color. The color wheel arranges hues so "
 "relationships read geometrically: complementary pairs oppose, analogous neighbors harmonize, triads space "
 "evenly. Warm colors advance, cool recede — exploited in painting for depth. Light mixes additively "
 "(screens: red+green+blue=white); pigment mixes subtractively (print: cyan+magenta+yellow=dark). Limited "
 "palettes unify; broken color vibrates.",
 ["Hue, value, saturation: color's three dimensions",
  "Wheel geometry: complementary, analogous, triadic",
  "Warm advances; cool recedes",
  "Additive light versus subtractive pigment",
  "Limited palettes unify compositions"],
 "Basic art vocabulary.",
 ["Standard color terminology"],
 "Standard art literature (color references).",
 "artmusic", "public-harvest"),
("art-history", "Visual Art",
 "Art History: Major Movements",
 "Art history traces how cultures image their worlds. Ancient: Egyptian frontality, Greek naturalism, Roman "
 "portraiture. Medieval: Byzantine icons, Gothic cathedrals' vertical light. Renaissance: perspective, "
 "anatomy, humanism. Baroque drama, Rococo lightness, Neoclassicism's moral severity, Romanticism's "
 "emotion. Modernism shattered representation — Impressionism's light, Cubism's facets, Abstraction's "
 "pure form — then Postmodernism quoted everything. Each movement answers its moment's technology, belief, "
 "and patronage. Presented as scholarly overview.",
 ["Ancient to medieval: frontality to Gothic light",
  "Renaissance: perspective and humanism",
  "Baroque through Romanticism: drama to emotion",
  "Modernism shattered representation",
  "Movements answer their moment's conditions"],
 "General reading level.",
 ["Standard art-historical terminology"],
 "Standard art literature (art history references). Scholarly overview.",
 "artmusic", "public-harvest"),
("sculpture", "Visual Art",
 "Sculpture and Three-Dimensional Form",
 "Sculpture is form in the round — experienced by moving around it. Carving subtracts (stone, wood); "
 "modeling adds (clay, wax); casting reproduces (bronze, via lost-wax); construction assembles (steel, "
 "found objects). Relief occupies the middle ground, rising from a surface. Mass, void, and axis organize "
 "sculptural composition; scale runs from netsuke to mountainsides. Public sculpture negotiates site, "
 "memory, and community — the most socially embedded of the visual arts.",
 ["Carving, modeling, casting, construction",
  "Relief between drawing and full round",
  "Mass, void, axis organize composition",
  "Scale from miniature to monumental",
  "Public sculpture negotiates site and memory"],
 "General reading level.",
 ["Standard art terminology"],
 "Standard art literature (sculpture references).",
 "artmusic", "public-harvest"),
("music-theory", "Music",
 "Music Theory: Notes, Intervals, Scales",
 "Music theory names what ears already know. Twelve pitch classes repeat each octave; intervals measure "
 "the distance between them — seconds through octaves, each with a characteristic sound. Major scales "
 "follow whole-whole-half-whole-whole-whole-half; natural minor shifts the pattern. Key signatures collect "
 "a key's sharps or flats; the circle of fifths arranges keys by shared tones. Notation — staff, clefs, "
 "note values — writes pitch and rhythm precisely enough for strangers to reproduce a composer's intent "
 "centuries later.",
 ["Twelve pitch classes per octave",
  "Intervals: named distances with characteristic sounds",
  "Major and minor scale patterns",
  "Circle of fifths arranges key relationships",
  "Notation preserves pitch and rhythm exactly"],
 "An instrument or keyboard diagram helps.",
 ["Standard music terminology"],
 "Standard music literature (theory references).",
 "artmusic", "public-harvest"),
("rhythm-meter", "Music",
 "Rhythm and Meter",
 "Rhythm organizes musical time. Beats are the steady pulse; meter groups them — duple, triple, compound — "
 "with time signatures stating the grouping. Note values divide the beat: whole, half, quarter, eighth, "
 "down to the 128th in theory. Syncopation accents off-beats against expectation; polyrhythm layers "
 "conflicting groupings (3 against 2); swing bends straight eighths into long-short lilt. Groove is "
 "rhythm's feel — micro-timing deviations that make bodies move, measurable in milliseconds.",
 ["Beats, meter, time signatures organize time",
  "Note values divide the beat hierarchically",
  "Syncopation accents against expectation",
  "Polyrhythm layers conflicting groupings",
  "Groove as measurable micro-timing"],
 "Ability to clap a steady pulse.",
 ["Standard music terminology"],
 "Standard music literature (rhythm references).",
 "artmusic", "public-harvest"),
("harmony", "Music",
 "Harmony: Chords and Progressions",
 "Harmony stacks pitches into chords and moves them through progressions. Triads — root, third, fifth — "
 "come major, minor, diminished, augmented; seventh chords add the seventh for jazz and classical color. "
 "Inversions reorder the stack; voice leading moves each voice smoothly to the next chord. Functional "
 "harmony assigns roles: tonic (home), subdominant (departure), dominant (tension demanding resolution). "
 "The ii-V-I and the twelve-bar blues are progressions whole genres are built on. Harmony is vertical "
 "sonority unfolding in time.",
 ["Triads and seventh chords as stacked thirds",
  "Inversions and smooth voice leading",
  "Functional roles: tonic, subdominant, dominant",
  "ii-V-I and twelve-bar blues as genre foundations",
  "Harmony as vertical sonority in time"],
 "Music theory basics.",
 ["Standard music terminology"],
 "Standard music literature (harmony references).",
 "artmusic", "public-harvest"),
("music-history", "Music",
 "Music History: Eras and Styles",
 "Music history moves through eras of style. Medieval: chant and early polyphony. Renaissance: imitative "
 "polyphony perfected. Baroque: basso continuo, opera's birth, Bach's counterpoint. Classical: sonata "
 "form, Haydn, Mozart, Beethoven's bridge. Romantic: expressive expansion, the virtuoso, national schools. "
 "20th century: impressionism, atonality, jazz, rock, electronic — recording and broadcast globalizing "
 "everything. Each era's instruments, venues, and economics shaped its sound. Presented as scholarly "
 "overview.",
 ["Medieval chant to Renaissance polyphony",
  "Baroque: opera, continuo, Bach",
  "Classical form; Romantic expression",
  "20th century: recording globalizes styles",
  "Instruments and economics shape each era's sound"],
 "General reading level.",
 ["Standard musicological terminology"],
 "Standard music literature (music history references). Scholarly overview.",
 "artmusic", "public-harvest"),
("sig-composition-geometry", "Signature Art & Music",
 "Signature Composition Geometry",
 "A Signature original design that treats visual and musical composition as geometry: pictorial elements "
 "placed by measured proportion (rule of thirds, golden section, dynamic symmetry), musical phrases "
 "structured by intervallic and rhythmic proportion. Balance, tension, and resolution become readable "
 "geometric properties rather than vague impressions. The design analyzes structure — it never dictates "
 "taste. A Signature treatment of composition as measurable design intelligence.",
 ["Composition as measurable geometry",
  "Proportional systems: thirds, golden section, symmetry",
  "Balance and tension as readable properties",
  "Applies to image and musical phrase alike",
  "Analyzes structure; never dictates taste"],
 "Art or music basics helpful.",
 ["Signature system conventions"],
 "Original Signature design; principles per standard art/music literature.",
 "artmusic", "signature"),
("sig-color-harmonizer", "Signature Art & Music",
 "Signature Color Harmonizer",
 "A Signature original instrument that computes color relationships exactly: harmonies (complementary, "
 "analogous, triadic, tetradic) derived geometrically from any base color, value and saturation scales "
 "generated deterministically, accessibility contrast ratios verified against WCAG thresholds. Palettes "
 "become reproducible records rather than eyeballed guesses. A Signature treatment of color as exact, "
 "auditable relationship geometry.",
 ["Harmonies derived geometrically from any base",
  "Value and saturation scales generated exactly",
  "Contrast ratios verified against standards",
  "Palettes as reproducible records",
  "Color as auditable relationship geometry"],
 "Color theory basics.",
 ["Signature system conventions; WCAG contrast"],
 "Original Signature design; facts per standard color literature.",
 "artmusic", "signature"),
("sig-scale-engine", "Signature Art & Music",
 "Signature Scale Engine",
 "A Signature original engine that generates musical scales and modes deterministically from interval "
 "patterns: major, natural/harmonic/melodic minor, pentatonics, church modes, and world scale families — "
 "each as exact pitch-class sets with stated intervallic structure. Transposition, harmonization, and "
 "chord-scale matching execute as verified operations. A Signature treatment of scale theory as exact "
 "computable structure.",
 ["Scales from interval patterns, deterministically",
  "Major, minors, pentatonics, modes, world families",
  "Exact pitch-class sets with stated structure",
  "Transposition and harmonization as verified operations",
  "Scale theory as computable structure"],
 "Music theory basics.",
 ["Signature system conventions"],
 "Original Signature design; facts per standard music literature.",
 "artmusic", "signature"),
("sig-artwork-analyzer", "Signature Art & Music",
 "Signature Artwork Analyzer",
 "A Signature original instrument that analyzes artwork structure as measurable Signature records: "
 "compositional geometry, palette statistics, value distribution, rhythmic regularity in pattern-based "
 "work. The analyzer describes structure — it never judges quality or meaning, which remain human "
 "territory. Every measurement carries its method openly. A Signature treatment of visual analysis as "
 "transparent, reproducible description.",
 ["Compositional geometry measured, not guessed",
  "Palette and value statistics computed",
  "Pattern regularity quantified",
  "Describes structure; never judges quality",
  "Every measurement carries its method"],
 "Art basics helpful.",
 ["Signature system conventions"],
 "Original Signature design; methods per standard art literature.",
 "artmusic", "signature"),
# ============================== EDUCATION ==============================
("learning-science", "Learning Science",
 "Learning Science: Memory, Attention, Practice",
 "Learning science studies how instruction changes minds. Retrieval practice — testing yourself — "
 "strengthens memory far more than rereading. Spacing distributes practice over time; interleaving mixes "
 "problem types so learners discriminate between them. Cognitive load theory: working memory is limited, "
 "so instruction should manage intrinsic load, reduce extraneous load, and invest in germane load. "
 "Elaboration — explaining ideas in your own words — builds durable understanding. Feedback works best "
 "when timely, specific, and actionable.",
 ["Retrieval practice beats rereading",
  "Spacing distributes; interleaving discriminates",
  "Cognitive load: manage, reduce, invest",
  "Elaboration builds durable understanding",
  "Feedback: timely, specific, actionable"],
 "General reading level.",
 ["Standard educational terminology"],
 "Standard education literature (learning-science references).",
 "edu", "public-harvest"),
("curriculum-design", "Teaching",
 "Curriculum Design: Goals to Assessment",
 "Curriculum design plans learning backward from goals. Backward design (Wiggins & McTighe): identify "
 "desired results, determine acceptable evidence, then plan learning experiences. Learning objectives — "
 "stated with observable verbs via Bloom's taxonomy — make goals assessable. Alignment ensures objectives, "
 "instruction, and assessment all target the same outcomes. Scope sequences content across grades; "
 "sequence orders it within. Differentiation adapts the plan to varied learners without lowering the "
 "bar. A designed curriculum is a promise about what students will be able to do.",
 ["Backward design: results, evidence, experiences",
  "Objectives with observable verbs (Bloom's)",
  "Alignment of goals, instruction, assessment",
  "Scope and sequence organize content",
  "Differentiation adapts without lowering bars"],
 "General reading level.",
 ["Standard curriculum terminology"],
 "Standard education literature (curriculum references).",
 "edu", "public-harvest"),
("assessment", "Teaching",
 "Assessment: Measuring Learning",
 "Assessment measures learning to guide it. Formative assessment — exit tickets, questioning, drafts — "
 "informs teaching while learning happens; summative assessment — exams, final projects — judges outcomes. "
 "Validity asks whether the test measures what it claims; reliability whether it does so consistently. "
 "Rubrics make expectations explicit and grading consistent. Norm-referenced tests rank against peers; "
 "criterion-referenced tests judge against standards. Assessment for learning, not just of learning, is "
 "the modern standard.",
 ["Formative guides; summative judges",
  "Validity: measuring what is claimed",
  "Reliability: measuring consistently",
  "Rubrics make expectations explicit",
  "Assessment for learning as the standard"],
 "General reading level.",
 ["Standard assessment terminology"],
 "Standard education literature (assessment references).",
 "edu", "public-harvest"),
("classroom-management", "Teaching",
 "Classroom Management",
 "Classroom management creates conditions for learning. Prevention beats reaction: clear routines, "
 "taught procedures, and engaging instruction stop most disruption before it starts. Withitness — the "
 "teacher's communicated awareness — keeps groups on task. Consequences should be logical, consistent, "
 "and instructional rather than punitive. Restorative approaches repair harm and relationships. "
 "Culturally responsive management recognizes that behavioral norms vary and builds shared expectations "
 "explicitly. The well-managed classroom feels calm because its systems are invisible.",
 ["Prevention through routines and engagement",
  "Withitness keeps groups on task",
  "Logical, consistent, instructional consequences",
  "Restorative approaches repair harm",
  "Culturally responsive shared expectations"],
 "General reading level.",
 ["Standard educational terminology"],
 "Standard education literature (classroom management references).",
 "edu", "public-harvest"),
("diverse-learners", "Teaching",
 "Supporting Diverse Learners",
 "Learners vary, and instruction should vary with them. Universal Design for Learning offers multiple "
 "means of engagement, representation, and expression — planned from the start, not retrofitted. "
 "Scaffolding provides temporary supports (sentence frames, worked examples) faded as competence grows. "
 "Multilingual learners need comprehensible input plus academic language development. Twice-exceptional "
 "students pair gifts with disabilities. Individualized Education Programs (IEPs) document legally "
 "required accommodations in the U.S. system. Equity means matching support to need, not identical "
 "treatment.",
 ["Universal Design for Learning from the start",
  "Scaffolding faded as competence grows",
  "Academic language for multilingual learners",
  "Twice-exceptional: gifts plus disabilities",
  "Equity as matched support, not identical treatment"],
 "General reading level.",
 ["UDL framework; IDEA terminology (U.S.)"],
 "Standard education literature (special education references).",
 "edu", "public-harvest"),
("edtech", "Technology",
 "Educational Technology",
 "Educational technology amplifies good pedagogy — it cannot replace it. Learning management systems "
 "organize courses; adaptive platforms adjust difficulty to the learner; simulations make the abstract "
 "manipulable. The SAMR model ranks integration: substitution, augmentation, modification, redefinition. "
 "Evidence favors technology that increases practice, feedback, and active learning — not passive content "
 "delivery. Digital equity matters: access gaps become learning gaps. Data privacy for minors is a "
 "non-negotiable constraint on every tool choice.",
 ["Technology amplifies pedagogy; never replaces it",
  "SAMR: substitution to redefinition",
  "Evidence favors practice, feedback, activity",
  "Access gaps become learning gaps",
  "Student data privacy as a hard constraint"],
 "General reading level.",
 ["Standard edtech terminology"],
 "Standard education literature (edtech references).",
 "edu", "public-harvest"),
("literacy-instruction", "Literacy",
 "Literacy: Teaching Reading and Writing",
 "Reading science converges on five pillars: phonemic awareness, phonics, fluency, vocabulary, and "
 "comprehension. Systematic phonics — explicit letter-sound instruction — outperforms implicit approaches "
 "for beginning readers in the evidence. Fluency bridges decoding and comprehension through accurate, "
 "automatic, expressive reading. Writing develops through the full process: planning, drafting, revising, "
 "editing, publishing. Background knowledge predicts comprehension more than generic 'skills' practice. "
 "Reading volume — miles of print — builds the vocabulary and knowledge that make readers.",
 ["Five pillars: awareness, phonics, fluency, vocabulary, comprehension",
  "Systematic phonics for beginning readers",
  "Fluency bridges decoding and comprehension",
  "Writing as a full process",
  "Knowledge and volume build readers"],
 "General reading level.",
 ["Standard literacy terminology"],
 "Standard education literature (reading science references).",
 "edu", "public-harvest"),
("math-instruction", "Literacy",
 "Mathematics Instruction: Concepts to Fluency",
 "Effective math instruction builds conceptual understanding, procedural fluency, and application together — "
 "not in sequence. Concrete-representational-abstract progressions move from manipulatives through diagrams "
 "to symbols. Number sense — flexible, meaningful number relationships — underlies all later mathematics. "
 "Productive struggle with worthy problems beats answer-getting; mistakes examined are assets. Formative "
 "assessment in math means listening to student reasoning, not just checking answers. Math anxiety is real "
 "and addressable through mastery experiences and reframed errors.",
 ["Concepts, fluency, application together",
  "Concrete-representational-abstract progressions",
  "Number sense underlies later mathematics",
  "Productive struggle over answer-getting",
  "Math anxiety addressed through mastery"],
 "General reading level.",
 ["NCTM terminology"],
 "Standard education literature (math education references).",
 "edu", "public-harvest"),
("sig-learning-path", "Signature Education",
 "Signature Learning Path Engine",
 "A Signature original engine that builds personalized learning paths as deterministic Signature records: "
 "prerequisites mapped as dependency graphs, topics sequenced by rule, practice scheduled by spacing "
 "science. The learner's stated goals and current level become the input record; the engine outputs a "
 "reproducible week-by-week plan with openly stated reasoning. A Signature treatment of curriculum "
 "planning as transparent, reproducible engineering.",
 ["Prerequisites as dependency graphs",
  "Topics sequenced by stated rules",
  "Practice scheduled by spacing science",
  "Week-by-week plans, reproducible",
  "Reasoning carried openly per plan"],
 "Learning science basics.",
 ["Signature system conventions"],
 "Original Signature design; methods per standard education literature.",
 "edu", "signature"),
("sig-curriculum-mapper", "Signature Education",
 "Signature Curriculum Mapper",
 "A Signature original instrument that maps curricula as navigable Signature structures: standards, units, "
 "lessons, and assessments linked in explicit alignment chains — every assessment traceable to its "
 "objective, every objective to its standard. Gaps (objectives without assessment) and orphans "
 "(assessments without objectives) are flagged deterministically. A Signature treatment of curriculum "
 "alignment as verifiable structure.",
 ["Curricula as navigable structures",
  "Alignment chains: standard to assessment",
  "Gaps and orphans flagged deterministically",
  "Every link traceable and checkable",
  "Alignment as verifiable structure"],
 "Curriculum design basics.",
 ["Signature system conventions"],
 "Original Signature design; methods per standard education literature.",
 "edu", "signature"),
("sig-assessment-analyzer", "Signature Education",
 "Signature Assessment Analyzer",
 "A Signature original instrument that analyzes assessment results as deterministic Signature records: "
 "item difficulty and discrimination computed from response patterns, reliability estimated openly, "
 "mastery inferred by stated rules with uncertainty shown. The analyzer reports what the data supports — "
 "no more, no less — and labels every inference with its basis. A Signature treatment of educational "
 "measurement as honest, reproducible arithmetic.",
 ["Item difficulty and discrimination computed",
  "Reliability estimated openly",
  "Mastery inferred by stated rules",
  "Uncertainty shown, never hidden",
  "Honest reproducible measurement"],
 "Assessment basics.",
 ["Signature system conventions"],
 "Original Signature design; methods per standard assessment literature.",
 "edu", "signature"),
("sig-study-optimizer", "Signature Education",
 "Signature Study Optimizer",
 "A Signature original engine that turns any study list into an optimized schedule: retrieval practice "
 "placed first, spacing intervals computed deterministically, interleaving arranged by rule, sessions "
 "sized to attention limits. The plan adapts to stated exam dates and available hours, and every "
 "scheduling decision carries its reason. A Signature treatment of study planning as transparent "
 "optimization over learning science.",
 ["Retrieval practice placed first",
  "Spacing intervals computed exactly",
  "Interleaving arranged by rule",
  "Sessions sized to attention limits",
  "Every decision carries its reason"],
 "Learning science basics.",
 ["Signature system conventions"],
 "Original Signature design; methods per standard learning-science literature.",
 "edu", "signature"),
# ============================== AGRICULTURE & FOOD ==============================
("soil-farming", "Agronomy",
 "Soil Science for Farming",
 "Productive farming starts with soil: its texture (sand-silt-clay), structure, organic matter, pH, and "
 "nutrient reserves. Soil tests measure N-P-K plus pH and organic matter, guiding lime and fertilizer "
 "decisions — apply what the test says, not habit. Organic matter is the master variable: it holds water "
 "and nutrients, feeds microbes, resists erosion. Cover crops protect and build soil between cash crops; "
 "reduced tillage preserves structure; rotation breaks pest cycles. Soil is a slow-built resource: "
 "stewardship compounds over decades.",
 ["Texture, structure, organic matter, pH as master variables",
  "Soil tests guide lime and fertilizer",
  "Organic matter holds water and nutrients",
  "Cover crops, reduced tillage, rotation",
  "Stewardship compounds over decades"],
 "Basic chemistry intuition helpful.",
 ["USDA soil terminology"],
 "Standard agriculture literature (agronomy references).",
 "agri", "public-harvest"),
("crop-production", "Agronomy",
 "Crop Production: Planting to Harvest",
 "Crop production manages the plant's life cycle for yield. Variety selection matches genetics to climate, "
 "soil, and market; seeding rate and depth set the stand. Planting windows balance soil temperature, "
 "moisture, and frost risk. Growth stages (emergence, vegetative, reproductive, maturity) schedule "
 "irrigation, nutrition, and protection. Harvest timing decides quality and storability — grain moisture, "
 "fruit ripeness, forage stage. Post-harvest handling — drying, cooling, storage — preserves what the "
 "season produced. Yield is the integration of every decision.",
 ["Variety matched to climate, soil, market",
  "Seeding rate and depth set the stand",
  "Growth stages schedule management",
  "Harvest timing decides quality",
  "Post-harvest handling preserves the crop"],
 "Basic biology intuition.",
 ["Standard agronomic terminology"],
 "Standard agriculture literature (crop production references).",
 "agri", "public-harvest"),
("irrigation", "Agronomy",
 "Irrigation and Water Management",
 "Irrigation supplies water when rain falls short. Methods trade efficiency against cost: flood (cheap, "
 "wasteful), sprinkler (moderate), drip (precise, expensive) — drip can exceed 90 percent efficiency. "
 "Scheduling by soil moisture sensors or evapotranspiration models beats calendars. Water quality matters: "
 "salinity accumulates in arid soils without leaching. Drainage is irrigation's twin — waterlogged roots "
 "suffocate. In a drying world, water productivity (crop per drop) is the defining metric of irrigated "
 "agriculture.",
 ["Flood, sprinkler, drip: efficiency versus cost",
  "Drip exceeds 90 percent efficiency",
  "Schedule by sensors and ET models, not calendars",
  "Salinity management in arid soils",
  "Crop per drop as the defining metric"],
 "Basic physics intuition.",
 ["FAO irrigation terminology"],
 "Standard agriculture literature (irrigation references).",
 "agri", "public-harvest"),
("animal-husbandry", "Livestock",
 "Animal Husbandry: Care and Breeding",
 "Animal husbandry manages livestock for production and welfare together. Nutrition — balanced rations of "
 "energy, protein, minerals, vitamins — drives growth, milk, and reproduction; water, always clean and "
 "available, is the first nutrient. Breeding selects for production traits while managing inbreeding; "
 "artificial insemination spreads superior genetics widely. Health programs combine vaccination, parasite "
 "control, and biosecurity. Housing balances ventilation, space, and bedding. Welfare standards increasingly "
 "shape markets: well-kept animals produce better and sell better.",
 ["Balanced rations drive production",
  "Water as the first nutrient",
  "Breeding selects traits, manages inbreeding",
  "Vaccination, parasites, biosecurity",
  "Welfare standards shape modern markets"],
 "Basic biology intuition.",
 ["Standard animal-science terminology"],
 "Standard agriculture literature (animal husbandry references).",
 "agri", "public-harvest"),
("pest-management", "Crop Protection",
 "Pest and Disease Management",
 "Integrated pest management (IPM) controls pests economically with minimal harm. Monitoring and economic "
 "thresholds decide whether action pays — spraying on schedule regardless is the old way. Cultural controls "
 "(rotation, sanitation, resistant varieties) come first; biological controls (predators, parasitoids) "
 "second; chemical controls targeted and rotated to slow resistance. Disease triangles — susceptible host, "
 "virulent pathogen, favorable environment — show why prevention beats cure. Resistance management "
 "preserves chemistry's useful life. IPM is knowledge-intensive farming at its best.",
 ["Monitoring and thresholds decide action",
  "Cultural, biological, chemical: in that order",
  "Disease triangle: host, pathogen, environment",
  "Resistance management preserves chemistry",
  "Knowledge-intensive farming"],
 "Crop production basics helpful.",
 ["IPM terminology (FAO/EPA)"],
 "Standard agriculture literature (IPM references).",
 "agri", "public-harvest"),
("food-safety", "Food Science",
 "Food Safety: From Farm to Table",
 "Food safety prevents illness across the supply chain. Hazards are biological (pathogens like Salmonella, "
 "E. coli), chemical (pesticide residues, allergens), and physical (foreign objects). HACCP — Hazard "
 "Analysis Critical Control Points — identifies where hazards can be controlled and monitors those points. "
 "Temperature control is the great lever: cold chains slow bacterial growth, thorough cooking kills "
 "pathogens. Traceability lets recalls target precisely. Home practice matters too: separate raw and "
 "cooked, chill promptly, cook to temperature.",
 ["Biological, chemical, physical hazards",
  "HACCP: control the critical points",
  "Temperature control as the great lever",
  "Traceability targets recalls precisely",
  "Home practice: separate, chill, cook"],
 "Basic microbiology intuition helpful.",
 ["FDA Food Code concepts; HACCP principles"],
 "Standard food-science literature (food safety references).",
 "agri", "public-harvest"),
("food-preservation", "Food Science",
 "Food Preservation: Canning to Freezing",
 "Preservation defeats spoilage's agents: microbes, enzymes, oxidation. Canning uses heat plus sealed "
 "containers — pressure canning for low-acid foods where botulism threatens. Freezing slows everything "
 "without changing flavor much; blanching first stops enzyme activity in vegetables. Drying removes the "
 "water microbes need; fermentation lets beneficial microbes outcompete harmful ones while creating "
 "flavor — cheese, yogurt, sauerkraut, kimchi. Each method trades shelf life, texture, nutrition, and "
 "energy differently.",
 ["Heat plus sealing: canning, pressure for low-acid",
  "Freezing slows; blanching stops enzymes",
  "Drying removes microbial water",
  "Fermentation: beneficial microbes win",
  "Each method trades qualities differently"],
 "Basic microbiology intuition helpful.",
 ["Standard food-science terminology"],
 "Standard food-science literature (preservation references).",
 "agri", "public-harvest"),
("ag-econ", "Farm Business",
 "Agricultural Economics: The Farm Business",
 "The farm is a business exposed to weather and markets. Enterprise budgets tally variable and fixed costs "
 "against expected revenue per acre or head; breakeven analysis finds the price or yield that covers "
 "costs. Risk management layers: diversification, crop insurance, forward contracts, futures and options. "
 "Land — the largest asset — is valued by productive capacity capitalized at interest rates. Government "
 "programs (support prices, conservation payments) shape decisions at the margin. Record-keeping turns "
 "farming from gamble to managed enterprise. Educational information, not financial advice.",
 ["Enterprise budgets per acre or head",
  "Breakeven: the price or yield covering costs",
  "Risk layers: insurance, contracts, futures",
  "Land valued by capitalized productivity",
  "Records turn farming into managed enterprise"],
 "Basic economics intuition.",
 ["USDA economic terminology"],
 "Standard agriculture literature (farm management references). Educational content.",
 "agri", "public-harvest"),
("sig-yield-geometry", "Signature Agriculture",
 "Signature Yield Geometry",
 "A Signature original framework that models crop yield as geometric records: plant populations as "
 "densities, growth stages as waypoints, yield components (plants, ears, kernels, weight) as measurable "
 "factors multiplied deterministically. Estimates carry their assumptions openly — stand counts, moisture, "
 "test weight — so any figure is auditable to its inputs. A Signature treatment of yield estimation as "
 "transparent, checkable arithmetic.",
 ["Yield as geometric factor records",
  "Components multiplied deterministically",
  "Assumptions carried openly per estimate",
  "Every figure auditable to inputs",
  "Transparent checkable arithmetic"],
 "Crop production basics.",
 ["Signature system conventions"],
 "Original Signature design; methods per standard agronomy literature.",
 "agri", "signature"),
("sig-crop-planner", "Signature Agriculture",
 "Signature Crop Planner",
 "A Signature original planner that builds cropping plans as deterministic Signature records: fields with "
 "stated soil and history, crops with requirements, rotations scheduled by rule to break pest cycles and "
 "build fertility. Planting windows, input schedules, and harvest targets are computed from the plan's own "
 "data. A Signature treatment of farm planning as reproducible, rule-based scheduling.",
 ["Fields, crops, rotations as records",
  "Rotations scheduled to break pest cycles",
  "Planting windows from plan data",
  "Input and harvest schedules computed",
  "Reproducible rule-based planning"],
 "Crop production basics.",
 ["Signature system conventions"],
 "Original Signature design; methods per standard agronomy literature.",
 "agri", "signature"),
("sig-irrigation-optimizer", "Signature Agriculture",
 "Signature Irrigation Optimizer",
 "A Signature original engine that schedules irrigation as deterministic optimization: soil moisture as a "
 "tracked state, crop water demand from growth stage and weather inputs, application amounts computed to "
 "hold the root zone in its optimal band. Every recommendation carries the readings and rules behind it. "
 "A Signature treatment of water management as transparent, auditable scheduling.",
 ["Soil moisture as a tracked state",
  "Demand from growth stage and weather",
  "Applications computed for the optimal band",
  "Recommendations carry their basis",
  "Transparent auditable scheduling"],
 "Irrigation basics.",
 ["Signature system conventions"],
 "Original Signature design; methods per standard irrigation literature.",
 "agri", "signature"),
("sig-food-mapper", "Signature Agriculture",
 "Signature Food System Mapper",
 "A Signature original instrument that maps food systems as flow records: production, processing, "
 "distribution, retail, and consumption as linked stages with quantities carried deterministically. "
 "Loss and waste are measured at each stage; safety checkpoints marked where HACCP principles apply. "
 "A Signature treatment of the farm-to-table chain as an auditable flow record.",
 ["Farm to table as linked stages",
  "Quantities carried deterministically",
  "Loss and waste measured per stage",
  "Safety checkpoints marked",
  "Auditable flow records"],
 "Food safety basics helpful.",
 ["Signature system conventions"],
 "Original Signature design; methods per standard food-science literature.",
 "agri", "signature"),
# ============================== ENERGY ==============================
("energy-fundamentals", "Fundamentals",
 "Energy Fundamentals: Forms, Units, Conservation",
 "Energy is the capacity to do work, appearing as kinetic, potential, thermal, chemical, electrical, "
 "radiant, and nuclear forms. The joule (SI) and kilowatt-hour (billing) measure it; power — the rate — "
 "is measured in watts. Conservation: energy is never created or destroyed, only converted, with some "
 "always degrading to waste heat per the second law. Efficiency is useful output over total input. "
 "Understanding forms, units, and conservation is the admission ticket to every energy discussion.",
 ["Energy as the capacity to do work",
  "Forms: kinetic, potential, thermal, chemical, electrical, radiant, nuclear",
  "Joules and kilowatt-hours; watts for power",
  "Conservation with inevitable waste heat",
  "Efficiency as useful over total"],
 "Basic physics intuition.",
 ["SI units; ISO 80000 conventions"],
 "Standard energy literature (textbooks).",
 "energy", "public-harvest"),
("fossil-fuels", "Sources",
 "Fossil Fuels: Coal, Oil, and Natural Gas",
 "Fossil fuels are ancient sunlight: coal from Carboniferous forests, oil and gas from marine plankton, "
 "compressed over geologic time. Coal powered the Industrial Revolution and still generates much of the "
 "world's electricity; oil's energy density made it transport's fuel; natural gas burns cleanest of the "
 "three. Combustion releases the stored energy — and the stored carbon: fossil fuels dominate anthropogenic "
 "CO2. Reserves are finite; extraction costs rise as easy deposits deplete. The energy transition is, at "
 "root, the managed replacement of these fuels.",
 ["Ancient sunlight stored geologically",
  "Coal, oil, gas: distinct origins and uses",
  "Combustion releases energy and carbon",
  "Dominant source of anthropogenic CO2",
  "Finite reserves; rising extraction costs"],
 "Energy fundamentals.",
 ["Standard energy terminology; SI units"],
 "Standard energy literature (references).",
 "energy", "public-harvest"),
("solar-power", "Renewables",
 "Solar Power: Photovoltaics",
 "Photovoltaic cells convert light directly to electricity: photons knock electrons across a semiconductor "
 "junction, and the cell's built-in field sweeps them into current. Silicon dominates — monocrystalline for "
 "efficiency, polycrystalline for cost. Capacity factor (actual over theoretical output) runs 15-25 percent "
 "depending on sunshine; inverters convert DC to grid AC. Costs fell roughly 90 percent in a decade, making "
 "solar the cheapest new electricity in most sunny regions. Storage or grid integration handles night and "
 "clouds.",
 ["Photovoltaic effect: light to current",
  "Silicon cells dominate the market",
  "Capacity factor 15-25 percent by sunshine",
  "Inverters convert DC to grid AC",
  "Cheapest new electricity in sunny regions"],
 "Energy fundamentals.",
 ["IEC photovoltaic standards; SI units"],
 "Standard energy literature (solar references).",
 "energy", "public-harvest"),
("wind-power", "Renewables",
 "Wind Power: Turbines and Farms",
 "Wind turbines harvest moving air: blades — airfoils like wings — spin a rotor, gearboxes (or direct "
 "drive) turn generators. Power rises with the cube of wind speed, so siting in strong steady wind is "
 "everything; capacity factors run 35-55 percent at good sites. Modern turbines top 200-meter rotors on "
 "towers over 100 meters. Offshore wind taps stronger, steadier marine winds at higher installation cost. "
 "Grid integration manages variability through forecasting, geographic diversity, and storage.",
 ["Blades as airfoils spinning generators",
  "Power rises with the cube of wind speed",
  "Siting decides economics",
  "Offshore: stronger winds, higher costs",
  "Variability managed by forecasting and diversity"],
 "Energy fundamentals.",
 ["IEC wind standards; SI units"],
 "Standard energy literature (wind references).",
 "energy", "public-harvest"),
("hydropower", "Renewables",
 "Hydropower: Dams and Flow",
 "Hydropower converts falling water to electricity — the oldest and largest renewable source. Dams store "
 "water as gravitational potential; penstocks deliver it to turbines at pressure; generators produce power "
 "on demand, making hydro the grid's great balancer. Capacity factors exceed 50 percent at good sites. "
 "Trade-offs are real: reservoirs flood land and alter rivers, sediment accumulates, fish passage needs "
 "engineering. Pumped storage — pumping uphill when power is cheap, releasing when dear — is the largest "
 "deployed 'battery' on Earth.",
 ["Falling water to electricity at scale",
  "Dams store energy as gravitational potential",
  "Dispatchable: the grid's great balancer",
  "Trade-offs: flooding, sediment, fish passage",
  "Pumped storage as the largest battery"],
 "Energy fundamentals.",
 ["Standard hydropower terminology; SI units"],
 "Standard energy literature (hydro references).",
 "energy", "public-harvest"),
("nuclear-power", "Sources",
 "Nuclear Power: Fission and Reactors",
 "Nuclear fission splits heavy nuclei — uranium-235, plutonium-239 — releasing millions of times more "
 "energy per atom than chemical reactions. Reactors sustain controlled chain reactions: fuel assemblies, "
 "moderators slowing neutrons (in most designs), control rods absorbing them, coolant carrying heat to "
 "turbines. A typical plant runs above 90 percent capacity factor, the highest of any source. Waste stays "
 "hazardous for millennia and needs engineered isolation; accidents, though rare, are severe. Presented "
 "factually as established civilian energy technology; no weapons content.",
 ["Fission releases millions-fold chemical energy",
  "Controlled chain reactions in reactor designs",
  "Fuel, moderator, control rods, coolant",
  "Highest capacity factor of any source",
  "Waste isolation as the long-term challenge"],
 "Energy fundamentals; basic physics.",
 ["IAEA terminology; SI units"],
 "Standard energy literature (nuclear references). Civilian technology only.",
 "energy", "public-harvest"),
("electric-grid", "Systems",
 "The Electric Grid: Generation to Outlet",
 "The grid is the largest machine humans built. Generation (power plants of all kinds) feeds high-voltage "
 "transmission — high voltage minimizes resistive loss over distance — then substations step down through "
 "distribution to the 120/240 volts at outlets. Supply and demand must balance every second: frequency "
 "(60 Hz in North America) is the vital sign, sagging when demand exceeds supply. Operators dispatch plants "
 "in merit order, cheapest first. Smart grids add sensors, automation, and demand response to the century-old "
 "architecture.",
 ["Generation to transmission to distribution",
  "High voltage minimizes distance losses",
  "Frequency as the balance vital sign",
  "Merit-order dispatch, cheapest first",
  "Smart grids add sensing and response"],
 "Energy fundamentals.",
 ["IEEE/NERC terminology; SI units"],
 "Standard energy literature (grid references).",
 "energy", "public-harvest"),
("energy-efficiency", "Systems",
 "Energy Efficiency and Conservation",
 "The cheapest energy is the energy not used. Efficiency does the same work with less input — LED lighting "
 "(~90 percent less than incandescent), heat pumps (moving heat beats making it), efficient motors and "
 "appliances. Conservation reduces the work itself — insulation, behavior, design. Building codes, appliance "
 "standards, and industrial audits capture savings systematically. Rebound effects (savings spent on more "
 "use) are real but partial — efficiency still wins. In the transition, efficiency buys time and shrinks "
 "every other investment needed.",
 ["Efficiency: same work, less input",
  "LEDs, heat pumps, efficient motors as exemplars",
  "Conservation reduces the work itself",
  "Codes and standards capture savings systematically",
  "Rebound real but partial; efficiency wins"],
 "Energy fundamentals.",
 ["ENERGY STAR / ISO 50001 concepts; SI units"],
 "Standard energy literature (efficiency references).",
 "energy", "public-harvest"),
("sig-energy-flow", "Signature Energy",
 "Signature Energy Flow Mapper",
 "A Signature original instrument that traces energy through any system as deterministic flow records: "
 "sources, conversions, useful work, and waste heat each carried as measured stages with stated "
 "efficiencies. Sankey-style flow geometry makes losses visible at a glance; the books must balance — "
 "unaccounted energy flags a modeling error. A Signature treatment of energy accounting as verifiable "
 "flow geometry.",
 ["Energy as deterministic flow records",
  "Stages: sources, conversions, work, waste",
  "Losses visible in flow geometry",
  "Books must balance; gaps flag errors",
  "Verifiable energy accounting"],
 "Energy fundamentals.",
 ["Signature system conventions; SI units"],
 "Original Signature design; classical facts per standard energy literature.",
 "energy", "signature"),
("sig-solar-geometry", "Signature Energy",
 "Signature Solar Geometry",
 "A Signature original design that computes solar availability as exact geometry: sun position from "
 "latitude, date, and time; panel orientation optimized deterministically; shading and tilt losses "
 "calculated, not guessed. Daily and annual yield integrate from the geometry with stated weather "
 "assumptions carried openly. A Signature treatment of solar assessment as provable celestial geometry.",
 ["Sun position from latitude, date, time",
  "Panel orientation optimized deterministically",
  "Shading and tilt losses calculated",
  "Yield from geometry with open assumptions",
  "Provable celestial geometry"],
 "Solar power basics.",
 ["Signature system conventions; SI units"],
 "Original Signature design; classical facts per standard solar literature.",
 "energy", "signature"),
("sig-grid-harmonizer", "Signature Energy",
 "Signature Grid Harmonizer",
 "A Signature original instrument that models power networks as harmonic Signature structures: generators "
 "as sources, loads as sinks, lines as bounded conduits — power flow computed deterministically with "
 "balance verified at every node. Overloads and imbalances stand out geometrically before they become "
 "outages. A Signature treatment of grid analysis as verifiable network geometry.",
 ["Networks as harmonic structures",
  "Power flow computed deterministically",
  "Balance verified at every node",
  "Overloads visible geometrically",
  "Verifiable network geometry"],
 "Electric grid basics.",
 ["Signature system conventions; SI units"],
 "Original Signature design; classical facts per standard grid literature.",
 "energy", "signature"),
("sig-consumption-optimizer", "Signature Energy",
 "Signature Consumption Optimizer",
 "A Signature original engine that optimizes energy use as deterministic planning: loads profiled by "
 "stated measurements, schedules shifted by rule to cheap-rate windows, efficiency upgrades ranked by "
 "computed payback. Every recommendation carries its numbers and assumptions openly. A Signature "
 "treatment of energy management as transparent, reproducible optimization.",
 ["Loads profiled by stated measurements",
  "Schedules shifted by open rules",
  "Upgrades ranked by computed payback",
  "Recommendations carry numbers and assumptions",
  "Transparent reproducible optimization"],
 "Energy efficiency basics.",
 ["Signature system conventions; SI units"],
 "Original Signature design; methods per standard energy literature.",
 "energy", "signature"),
]
