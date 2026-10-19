#!/usr/bin/env python3
"""Entries for the Language Arts Quiz databases (Manon's 2026-10-17 16:15 orders:
"Test then quiz databases with answers at bottom").

Verified 2026-10-17: RAW dedupe-gate sweep of all 68 titles (34 public +
34 " (Signature Edition)") against the whole system (data/dedupe/exact):
zero collisions, zero refusals. ID prefixes JAH-QZLA- (public) and
JAH-QZLAS- (signature) verified free in the manifest id_prefix values and in
every shard index file across jah-databases-data-1 (zero hits).

This build creates two NEW databases, 34 ladder-ordered records each:

  quiz-language-arts             - The Language Arts Quiz Database
                                   (public-harvest: real, verified language
                                   arts quizzes - vocabulary, grammar,
                                   spelling and punctuation, literature,
                                   wordplay and puzzles, reading and
                                   rhetoric, poetry and prosody. EVERY record
                                   is one complete quiz of ten questions with
                                   the ANSWERS AT THE BOTTOM of the record,
                                   ladder-ordered easy -> medium -> hard,
                                   every question and answer verified correct.)
  quiz-language-arts-signature  - The Language Arts Quiz Signature Database
                                   (his original Signature Quizmaster Method:
                                   every question a trial of the tongue, every
                                   answer a sealed mark of mastery, the ladder
                                   the climb every mind must make; the same
                                   ladder through the Signature lens, titles
                                   suffixed " (Signature Edition)", src
                                   signature, clearly labeled Signature-made,
                                   never presented as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

Every demo is a real quiz runner: it prints the ten questions, grades a
simulated run, prints the computed score, asserts tight bounds (never float
exact-equality), prints the answer key at the bottom, and ends with the OK
marker. Build.py cross-checks demo stdout against entry text (Q1 and A1 must
appear verbatim) - entry text and demo output can never drift apart.

Never the words "bat belt" anywhere. No website references. No Facebook.
Screened: nothing hate-adjacent, profane, or inappropriate; no religious talk.
"""

SIG_TAIL = ("Signature original - his original Signature Quizmaster Method: "
            "every question a trial of the tongue, every answer a sealed mark "
            "of mastery, the ladder the climb every mind must make. Clearly "
            "labeled Signature-made, never presented as authentic public "
            "record.")

# ---------------------------------------------------------------- shared text

HOW_TAKE = ("How to take this quiz. Read the ten questions in order and answer "
            "each one before you look below - say the answer aloud or write it "
            "down. The answer key sits at the bottom of this record, after the "
            "questions, so there is no peeking until you finish. Scoring: 9 to "
            "10 correct is excellent, 7 to 8 is good, 5 to 6 is fair, and fewer "
            "than 5 means you should study this rung and climb it again.")

REQ = ["Answer the ten questions in order.",
       "Say or write each answer before looking below.",
       "Keep the answer key covered until you finish all ten.",
       "Score yourself honestly: 9-10 excellent, 7-8 good, 5-6 fair, "
       "under 5 means climb this rung again."]

STD_LANG = ["Merriam-Webster's Collegiate Dictionary, 11th ed. "
            "(Merriam-Webster, 2003)",
            "The Chicago Manual of Style, 18th ed. (University of Chicago "
            "Press, 2024)",
            "Purdue University Online Writing Lab (OWL): grammar, punctuation, "
            "and mechanics guides",
            "Common Core State Standards for English Language Arts"]
STD_LIT = STD_LANG + ["The Norton Anthology of English Literature "
                      "(W. W. Norton)",
                      "MLA Handbook, 9th ed. (Modern Language Association, "
                      "2021)"]
STD_POETRY = STD_LIT + ["The Princeton Encyclopedia of Poetry and Poetics, "
                        "4th ed. (Princeton University Press, 2012)"]

CIT_WEBSTER = ("Merriam-Webster's Collegiate Dictionary, 11th ed. "
               "(Merriam-Webster, 2003): word senses, spellings, and usage "
               "notes behind the answer key.")
CIT_CHICAGO = ("The Chicago Manual of Style, 18th ed. (University of Chicago "
               "Press, 2024): the punctuation and grammar rules behind the "
               "answer key.")
CIT_OWL = ("Purdue University Online Writing Lab (OWL): sentence, agreement, "
           "and modifier rules consulted for the answer key.")
CIT_NORTON = ("The Norton Anthology of English Literature (W. W. Norton): "
              "author, work, and movement facts behind the literature answer "
              "keys.")
CIT_PRINCETON = ("The Princeton Encyclopedia of Poetry and Poetics, 4th ed. "
                 "(Princeton University Press, 2012): verse forms, meter, "
                 "and sound-device definitions behind the answer key.")
CIT_OED = ("Oxford English Dictionary (Oxford University Press): word "
           "histories and form notes behind the wordplay answer keys.")
CIT_MLA = ("MLA Handbook, 9th ed. (Modern Language Association, 2021): "
           "literary research conventions behind the literature answer keys.")

SIG_LENS_QUIZ = ("Through the Signature lens this quiz is a covenant of "
                 "words: every question a trial set before the climber, every "
                 "answer a seal pressed into the record. Take it the "
                 "Signature way - in order, aloud, honestly - and let the "
                 "ladder measure how far the tongue has climbed.")

# ------------------------------------------------------------------ entries

ENTRIES = [
    # ============================ VOCABULARY ============================
    {
        "key": "qzla_syn_easy", "name": "Easy Synonyms Quiz", "group": "Vocabulary",
        "ladder_rank": 1, "ladder_tier": "foundations",
        "intro": ("The first rung of the vocabulary ladder. Ten gentle "
                  "questions about words that mean the same thing - synonyms. "
                  "Read each one, pick the matching word, and remember the "
                  "answers wait at the bottom of this record."),
        "qa": [
            ("Which word means the same as 'happy'? (a) joyful (b) angry (c) tired (d) silent",
             "joyful", "Joyful and happy both describe feeling glad."),
            ("Which word means the same as 'fast'? (a) slow (b) quick (c) heavy (d) late",
             "quick", "Quick and fast both describe high speed."),
            ("Which word means the same as 'big'? (a) tiny (b) large (c) short (d) thin",
             "large", "Large and big both describe great size."),
            ("Which word means the same as 'smart'? (a) clever (b) sleepy (c) hungry (d) loud",
             "clever", "Clever and smart both describe intelligence."),
            ("Which word means the same as 'begin'? (a) end (b) start (c) stop (d) rest",
             "start", "Start and begin both mean to commence."),
            ("Which word means the same as 'difficult'? (a) easy (b) hard (c) fun (d) soft",
             "hard", "Hard and difficult both mean not easy."),
            ("Which word means the same as 'quiet'? (a) noisy (b) silent (c) bright (d) busy",
             "silent", "Silent and quiet both mean making little sound."),
            ("Which word means the same as 'cold'? (a) chilly (b) warm (c) sunny (d) dry",
             "chilly", "Chilly and cold both describe low temperature."),
            ("Which word means the same as 'brave'? (a) scared (b) bold (c) weak (d) shy",
             "bold", "Bold and brave both describe courage."),
            ("Which word means the same as 'pretty'? (a) ugly (b) plain (c) beautiful (d) dull",
             "beautiful", "Beautiful and pretty both describe pleasing appearance."),
        ],
        "standards": STD_LANG, "citations": [CIT_WEBSTER],
        "sig_lens": SIG_LENS_QUIZ,
    },
    {
        "key": "qzla_ant_easy", "name": "Easy Antonyms Quiz", "group": "Vocabulary",
        "ladder_rank": 2, "ladder_tier": "foundations",
        "intro": ("The second rung: words that mean the opposite - antonyms. "
                  "Ten simple questions. Opposites sharpen meaning the way a "
                  "whetstone sharpens a blade. Answers at the bottom."),
        "qa": [
            ("Which word is the opposite of 'hot'? (a) warm (b) cold (c) sunny (d) dry",
             "cold", "Cold is the direct opposite of hot."),
            ("Which word is the opposite of 'up'? (a) down (b) over (c) high (d) left",
             "down", "Down is the direct opposite of up."),
            ("Which word is the opposite of 'day'? (a) morning (b) night (c) noon (d) week",
             "night", "Night is the direct opposite of day."),
            ("Which word is the opposite of 'tall'? (a) big (b) short (c) wide (d) long",
             "short", "Short is the direct opposite of tall."),
            ("Which word is the opposite of 'win'? (a) play (b) lose (c) race (d) score",
             "lose", "Lose is the direct opposite of win."),
            ("Which word is the opposite of 'full'? (a) empty (b) packed (c) round (d) heavy",
             "empty", "Empty is the direct opposite of full."),
            ("Which word is the opposite of 'clean'? (a) dirty (b) tidy (c) neat (d) fresh",
             "dirty", "Dirty is the direct opposite of clean."),
            ("Which word is the opposite of 'early'? (a) soon (b) late (c) first (d) quick",
             "late", "Late is the direct opposite of early."),
            ("Which word is the opposite of 'strong'? (a) weak (b) tough (c) firm (d) bold",
             "weak", "Weak is the direct opposite of strong."),
            ("Which word is the opposite of 'laugh'? (a) smile (b) cry (c) sing (d) grin",
             "cry", "Cry is the opposite expression of laugh."),
        ],
        "standards": STD_LANG, "citations": [CIT_WEBSTER],
        "sig_lens": SIG_LENS_QUIZ,
    },
    {
        "key": "qzla_prefix", "name": "Common Prefixes Quiz", "group": "Vocabulary",
        "ladder_rank": 3, "ladder_tier": "foundations",
        "intro": ("Prefixes are word beginnings that change meaning - learn "
                  "ten of them and you can decode thousands of words. Each "
                  "question names a prefix inside a familiar word. Answers at "
                  "the bottom."),
        "qa": [
            ("What does the prefix 'un-' mean in 'unhappy'?",
             "not", "Un- negates: unhappy means not happy."),
            ("What does the prefix 're-' mean in 'rewrite'?",
             "again", "Re- repeats: rewrite means write again."),
            ("What does the prefix 'pre-' mean in 'preview'?",
             "before", "Pre- comes before: preview means view before."),
            ("What does the prefix 'dis-' mean in 'disagree'?",
             "the opposite of", "Dis- reverses: disagree is the opposite of agree."),
            ("What does the prefix 'mis-' mean in 'misspell'?",
             "wrongly", "Mis- means wrongly: misspell means spell wrongly."),
            ("What does the prefix 'over-' mean in 'overcook'?",
             "too much", "Over- means excess: overcook means cook too much."),
            ("What does the prefix 'under-' mean in 'underestimate'?",
             "too little", "Under- means below: underestimate means estimate too little."),
            ("What does the prefix 'bi-' mean in 'bicycle'?",
             "two", "Bi- means two: a bicycle has two wheels."),
            ("What does the prefix 'anti-' mean in 'antibiotic'?",
             "against", "Anti- means against: an antibiotic works against bacteria."),
            ("What does the prefix 'post-' mean in 'postgame'?",
             "after", "Post- means after: postgame means after the game."),
        ],
        "standards": STD_LANG, "citations": [CIT_WEBSTER, CIT_OED],
        "sig_lens": SIG_LENS_QUIZ,
    },
    {
        "key": "qzla_confused", "name": "Commonly Confused Words Quiz", "group": "Vocabulary",
        "ladder_rank": 4, "ladder_tier": "compounded",
        "intro": ("Their, there, they are - the classic traps. Ten questions "
                  "on the word pairs that trip up even strong writers. Choose "
                  "carefully; the answers wait at the bottom."),
        "qa": [
            ("Choose the correct word: '___ going to win the game.' (a) Their (b) There (c) They are",
             "They are", "They are going to win - the contraction of they are."),
            ("Choose the correct word: '___ the best player on the team.' (a) Your (b) You are",
             "You are", "You are the best player - the contraction of you are."),
            ("Choose the correct word: 'The dog wagged ___ tail.' (a) its (b) it is",
             "its", "Its is the possessive; it is would need an apostrophe."),
            ("Choose the correct word: 'Please ___ my gift.' (a) accept (b) except",
             "accept", "Accept means to receive; except means to leave out."),
            ("Choose the correct word: 'The medicine had a strong ___.' (a) affect (b) effect",
             "effect", "Effect is the noun meaning result; affect is usually the verb."),
            ("Choose the correct word: 'He paid her a nice ___.' (a) compliment (b) complement",
             "compliment", "A compliment is praise; a complement completes something."),
            ("Choose the correct word: 'The ___ of the school gave a speech.' (a) principal (b) principle",
             "principal", "The principal heads a school; a principle is a rule or belief."),
            ("Choose the correct word: '___ going to rain today.' (a) Its (b) It is",
             "It is", "It is going to rain - the contraction needs the apostrophe."),
            ("Choose the correct word: 'I do not know ___ she is coming.' (a) weather (b) whether",
             "whether", "Whether introduces a choice; weather is the atmosphere."),
            ("Choose the correct word: 'I want to come ___.' (a) to (b) too (c) two",
             "too", "Too means also; to is the preposition and two is the number."),
        ],
        "standards": STD_LANG, "citations": [CIT_WEBSTER, CIT_OWL],
        "sig_lens": SIG_LENS_QUIZ,
    },
    {
        "key": "qzla_suffix", "name": "Suffixes and Word Endings Quiz", "group": "Vocabulary",
        "ladder_rank": 5, "ladder_tier": "compounded",
        "intro": ("Suffixes are word endings that build new words and reveal "
                  "parts of speech. Ten questions on the endings that turn "
                  "adjectives into adverbs and verbs into nouns. Answers at "
                  "the bottom."),
        "qa": [
            ("What does the ending '-ly' usually form, as in 'quickly'?",
             "an adverb", "Quickly describes how she ran - an adverb."),
            ("What does the ending '-ness' form, as in 'kindness'?",
             "a noun", "Kindness names a quality - a noun."),
            ("What does the ending '-er' mean in 'teacher'?",
             "one who", "A teacher is one who teaches."),
            ("What does the ending '-ful' mean in 'hopeful'?",
             "full of", "Hopeful means full of hope."),
            ("What does the ending '-less' mean in 'fearless'?",
             "without", "Fearless means without fear."),
            ("What does the ending '-able' mean in 'readable'?",
             "able to be", "Readable means able to be read."),
            ("What part of speech is the word 'happiness'?",
             "noun", "Happiness names a state - a noun."),
            ("What part of speech is the word 'quickly'?",
             "adverb", "Quickly modifies the verb - an adverb."),
            ("What does the ending '-tion' form, as in 'action'?",
             "a noun", "Action names a thing done - a noun."),
            ("What does the ending '-est' mean in 'tallest'?",
             "the most", "Tallest is the superlative - the most tall."),
        ],
        "standards": STD_LANG, "citations": [CIT_WEBSTER, CIT_OED],
        "sig_lens": SIG_LENS_QUIZ,
    },
    {
        "key": "qzla_syn_adv", "name": "Advanced Synonyms Quiz", "group": "Vocabulary",
        "ladder_rank": 8, "ladder_tier": "advanced",
        "intro": ("Now the air gets thin: ten advanced synonyms for the "
                  "climber who has finished the lower rungs. Precise words for "
                  "precise minds. Answers at the bottom."),
        "qa": [
            ("Which word is a synonym of 'benevolent'? (a) kind (b) cruel (c) wealthy (d) strict",
             "kind", "Benevolent means kind and generous."),
            ("Which word is a synonym of 'candid'? (a) secretive (b) honest (c) rude (d) shy",
             "honest", "Candid means honest and direct."),
            ("Which word is a synonym of 'diligent'? (a) lazy (b) hardworking (c) careless (d) slow",
             "hardworking", "Diligent means hardworking and careful."),
            ("Which word is a synonym of 'ephemeral'? (a) lasting (b) brief (c) ancient (d) heavy",
             "brief", "Ephemeral means lasting a very short time."),
            ("Which word is a synonym of 'frugal'? (a) wasteful (b) thrifty (c) generous (d) rich",
             "thrifty", "Frugal means thrifty with money."),
            ("Which word is a synonym of 'gregarious'? (a) shy (b) sociable (c) proud (d) quiet",
             "sociable", "Gregarious means sociable and fond of company."),
            ("Which word is a synonym of 'innovative'? (a) original (b) old (c) dull (d) copied",
             "original", "Innovative means original and new in thinking."),
            ("Which word is a synonym of 'meticulous'? (a) careless (b) precise (c) quick (d) rough",
             "precise", "Meticulous means precise and careful about detail."),
            ("Which word is a synonym of 'resilient'? (a) fragile (b) tough (c) weak (d) rigid",
             "tough", "Resilient means tough enough to recover quickly."),
            ("Which word is a synonym of 'verbose'? (a) brief (b) wordy (c) silent (d) clear",
             "wordy", "Verbose means wordy - using more words than needed."),
        ],
        "standards": STD_LANG, "citations": [CIT_WEBSTER],
        "sig_lens": SIG_LENS_QUIZ,
    },
    {
        "key": "qzla_vocab_grad", "name": "Graduate-Level Vocabulary Quiz", "group": "Vocabulary",
        "ladder_rank": 9, "ladder_tier": "advanced",
        "intro": ("The summit of the vocabulary ladder: ten graduate-level "
                  "words that appear in serious books, tests, and speeches. "
                  "Master these and few texts can surprise you. Answers at "
                  "the bottom."),
        "qa": [
            ("What does 'ubiquitous' mean? (a) rare (b) present everywhere (c) hidden (d) ancient",
             "present everywhere", "Ubiquitous means present everywhere at once."),
            ("What does 'enigmatic' mean? (a) clear (b) mysterious (c) loud (d) simple",
             "mysterious", "Enigmatic means mysterious and hard to understand."),
            ("What does 'pragmatic' mean? (a) idealistic (b) practical (c) careless (d) emotional",
             "practical", "Pragmatic means practical rather than idealistic."),
            ("What does 'ambiguous' mean? (a) obvious (b) open to more than one meaning (c) brief (d) certain",
             "open to more than one meaning", "Ambiguous means open to more than one interpretation."),
            ("What does 'cacophony' mean? (a) harmony (b) harsh mixture of sounds (c) silence (d) melody",
             "harsh mixture of sounds", "Cacophony is a harsh, jarring mixture of sounds."),
            ("What does 'eloquent' mean? (a) silent (b) fluent and persuasive in speaking (c) rude (d) brief",
             "fluent and persuasive in speaking", "Eloquent speech is fluent and persuasive."),
            ("What does 'prolific' mean? (a) unproductive (b) producing a great amount (c) slow (d) rare",
             "producing a great amount", "Prolific means producing a great amount of work."),
            ("What does 'stoic' mean? (a) emotional (b) enduring hardship without complaint (c) cheerful (d) talkative",
             "enduring hardship without complaint", "Stoic means enduring hardship without complaint."),
            ("What does 'venerable' mean? (a) young (b) respected because of age or wisdom (c) weak (d) new",
             "respected because of age or wisdom", "Venerable means respected for age, wisdom, or character."),
            ("What does 'zealous' mean? (a) indifferent (b) passionately devoted (c) lazy (d) calm",
             "passionately devoted", "Zealous means passionately devoted to a cause."),
        ],
        "standards": STD_LANG, "citations": [CIT_WEBSTER],
        "sig_lens": SIG_LENS_QUIZ,
    },
]

ENTRIES += [
    # ============================= GRAMMAR ==============================
    {
        "key": "qzla_pos", "name": "Parts of Speech Basics Quiz", "group": "Grammar",
        "ladder_rank": 1, "ladder_tier": "foundations",
        "intro": ("Every word has a job - noun, verb, adjective, and the rest. "
                  "Ten questions on the eight classic parts of speech, the "
                  "foundation every grammar rung stands on. Answers at the "
                  "bottom."),
        "qa": [
            ("What part of speech is 'dog' in 'The dog barked'?",
             "noun", "Dog names a thing - a noun."),
            ("What part of speech is 'run' in 'They run fast'?",
             "verb", "Run expresses the action - a verb."),
            ("What part of speech is 'beautiful' in 'a beautiful day'?",
             "adjective", "Beautiful describes the noun day - an adjective."),
            ("What part of speech is 'quickly' in 'She ran quickly'?",
             "adverb", "Quickly modifies the verb ran - an adverb."),
            ("What part of speech is 'and' in 'cats and dogs'?",
             "conjunction", "And joins words - a conjunction."),
            ("What part of speech is 'under' in 'under the table'?",
             "preposition", "Under shows position - a preposition."),
            ("What part of speech is 'Wow' in 'Wow, that is big'?",
             "interjection", "Wow expresses sudden feeling - an interjection."),
            ("What part of speech is 'she' in 'She sings'?",
             "pronoun", "She stands in for a noun - a pronoun."),
            ("What part of speech is 'the' in 'the book'?",
             "article", "The points to a specific noun - an article."),
            ("What part of speech is 'happy' in 'They are happy'?",
             "adjective", "Happy describes they - a predicate adjective."),
        ],
        "standards": STD_LANG, "citations": [CIT_OWL, CIT_CHICAGO],
        "sig_lens": SIG_LENS_QUIZ,
    },
    {
        "key": "qzla_sentences", "name": "Simple and Compound Sentences Quiz", "group": "Grammar",
        "ladder_rank": 2, "ladder_tier": "foundations",
        "intro": ("Simple sentences carry one idea; compound sentences join "
                  "two. Ten questions on telling them apart and joining them "
                  "correctly. Answers at the bottom."),
        "qa": [
            ("Is this simple or compound: 'The cat slept.'",
             "simple", "One independent clause makes it simple."),
            ("Is this simple or compound: 'The cat slept, and the dog barked.'",
             "compound", "Two independent clauses joined by and make it compound."),
            ("How many independent clauses does a simple sentence have?",
             "one", "A simple sentence has exactly one independent clause."),
            ("How many independent clauses does a compound sentence have?",
             "two or more", "A compound sentence joins two or more independent clauses."),
            ("Which conjunction best joins 'I was tired' and 'I kept reading'? (a) and (b) but (c) or (d) so",
             "but", "But shows the contrast: tired, yet kept reading."),
            ("Which is a compound sentence? (a) She sang. (b) She sang, and he played guitar. (c) Singing softly.",
             "She sang, and he played guitar.", "It joins two independent clauses with a comma and and."),
            ("What punctuation usually comes before the coordinating conjunction joining two independent clauses?",
             "a comma", "Use a comma before and, but, or, so, and the rest in compounds."),
            ("What error is this: 'I like apples, I like oranges.'",
             "comma splice", "Two independent clauses joined by only a comma is a comma splice."),
            ("Which mark can join 'I like apples' and 'I like oranges' with no conjunction at all?",
             "a semicolon", "A semicolon joins two closely related independent clauses."),
            ("Is this a complete sentence: 'Because I was late.'",
             "no", "It is a fragment - a dependent clause with no independent clause."),
        ],
        "standards": STD_LANG, "citations": [CIT_OWL, CIT_CHICAGO],
        "sig_lens": SIG_LENS_QUIZ,
    },
    {
        "key": "qzla_sv_agree", "name": "Subject-Verb Agreement Basics Quiz", "group": "Grammar",
        "ladder_rank": 3, "ladder_tier": "foundations",
        "intro": ("Singular subjects take singular verbs; plural subjects take "
                  "plural verbs. Ten questions on making the two ends of the "
                  "sentence shake hands. Answers at the bottom."),
        "qa": [
            ("Choose the verb: 'The dog ___ loudly.' (a) bark (b) barks",
             "barks", "The singular dog takes the singular barks."),
            ("Choose the verb: 'The dogs ___ loudly.' (a) bark (b) barks",
             "bark", "The plural dogs takes the plural bark."),
            ("Choose the verb: 'She ___ to school.' (a) go (b) goes",
             "goes", "The singular she takes goes."),
            ("Choose the verb: 'They ___ to school.' (a) go (b) goes",
             "go", "The plural they takes go."),
            ("Choose the verb: 'The list of items ___ on the table.' (a) is (b) are",
             "is", "The subject is the singular list, not items."),
            ("Choose the verb: 'Each of the students ___ a book.' (a) has (b) have",
             "has", "Each is singular and takes has."),
            ("Choose the verb: 'Neither the cat nor the dogs ___ outside.' (a) was (b) were",
             "were", "With neither-nor, the verb agrees with the nearer subject, dogs."),
            ("Choose the verb: 'Mathematics ___ my favorite subject.' (a) is (b) are",
             "is", "Mathematics is singular in form and takes is."),
            ("Choose the verb, American usage: 'The team ___ well together.' (a) plays (b) play",
             "plays", "In American usage a collective team acting as one takes plays."),
            ("Choose the verb: 'There ___ many reasons to read.' (a) is (b) are",
             "are", "The true subject reasons is plural, so are."),
        ],
        "standards": STD_LANG, "citations": [CIT_OWL, CIT_CHICAGO],
        "sig_lens": SIG_LENS_QUIZ,
    },
    {
        "key": "qzla_pronoun", "name": "Pronoun Agreement Quiz", "group": "Grammar",
        "ladder_rank": 4, "ladder_tier": "compounded",
        "intro": ("Pronouns must agree with their antecedents in number - a "
                  "singular noun earns a singular pronoun. Ten questions on "
                  "the classic agreement traps. Answers at the bottom."),
        "qa": [
            ("Choose the pronoun: 'Every student must bring ___ book.' (a) their (b) his or her (c) its",
             "his or her", "Every student is singular, so his or her."),
            ("Choose the pronoun: 'The committee made ___ decision.' (a) their (b) its (c) his",
             "its", "The committee acts as one unit, so its."),
            ("Choose the pronoun: 'Neither of the girls brought ___ lunch.' (a) their (b) her (c) his",
             "her", "Neither is singular and the girls are female, so her."),
            ("Choose the pronoun: 'Each of the players tied ___ shoes.' (a) their (b) his (c) his or her",
             "his or her", "Each is singular, so his or her."),
            ("Choose the pronoun: 'The dog wagged ___ tail.' (a) its (b) their (c) his",
             "its", "The singular dog takes the possessive its."),
            ("Choose the pronoun: 'Someone left ___ umbrella.' (a) their (b) his or her (c) its",
             "his or her", "Someone is singular, so his or her."),
            ("Choose the pronoun: 'The jury reached ___ verdict.' (a) their (b) its (c) his",
             "its", "The jury acts as one unit, so its."),
            ("Choose the pronoun: 'Both of the boys finished ___ homework.' (a) their (b) his (c) its",
             "their", "Both is plural, so their."),
            ("Choose the pronoun: 'Everybody should mind ___ manners.' (a) their (b) his or her (c) its",
             "his or her", "Everybody is singular, so his or her."),
            ("Choose the pronoun: 'The flock of birds built ___ nests.' (a) their (b) its (c) his",
             "their", "The birds built separate nests, so the plural their."),
        ],
        "standards": STD_LANG, "citations": [CIT_OWL, CIT_CHICAGO],
        "sig_lens": SIG_LENS_QUIZ,
    },
    {
        "key": "qzla_tenses", "name": "Verb Tenses Quiz", "group": "Grammar",
        "ladder_rank": 5, "ladder_tier": "compounded",
        "intro": ("Past, present, participle - ten questions on the verb forms "
                  "that carry time itself, including the irregular verbs that "
                  "refuse to follow the rules. Answers at the bottom."),
        "qa": [
            ("What is the past tense of 'go'?",
             "went", "Go becomes went in the past tense."),
            ("What is the past tense of 'eat'?",
             "ate", "Eat becomes ate in the past tense."),
            ("What is the past participle of 'write', as in 'has ___'?",
             "written", "The participle is written: has written."),
            ("Choose the verb: 'She ___ finished.' (a) has (b) have",
             "has", "The singular she takes has."),
            ("Choose the verb: 'They ___ finished.' (a) has (b) have",
             "have", "The plural they takes have."),
            ("What is the past tense of 'teach'?",
             "taught", "Teach becomes taught in the past tense."),
            ("Which is correct: 'I have went' or 'I have gone'?",
             "I have gone", "Have takes the participle gone, not went."),
            ("What is the past tense of 'bring'?",
             "brought", "Bring becomes brought in the past tense."),
            ("Choose the verb: 'By tomorrow, she will have ___.' (a) finish (b) finished",
             "finished", "Will have takes the participle finished."),
            ("What is the past tense of 'swim', as in 'Yesterday I ___'?",
             "swam", "Swim becomes swam in the past tense."),
        ],
        "standards": STD_LANG, "citations": [CIT_OWL, CIT_WEBSTER],
        "sig_lens": SIG_LENS_QUIZ,
    },
    {
        "key": "qzla_modifiers", "name": "Dangling and Misplaced Modifiers Quiz", "group": "Grammar",
        "ladder_rank": 7, "ladder_tier": "compounded",
        "intro": ("A modifier must point at the right noun, or the sentence "
                  "says something absurd. Ten questions on dangling and "
                  "misplaced modifiers - the errors that make trees run down "
                  "the street. Answers at the bottom."),
        "qa": [
            ("What is wrong with 'Running down the street, the trees blurred past'?",
             "dangling modifier", "The modifier dangles - the trees were not running."),
            ("In 'Running down the street, I saw the trees blur past', who is running?",
             "the speaker", "The modifier now correctly points at the speaker, I."),
            ("In 'She served sandwiches to the children on paper plates', what is misplaced?",
             "on paper plates", "It sounds as if the children are on paper plates."),
            ("Which is traditionally preferred: 'to go boldly' or 'to boldly go'?",
             "to go boldly", "Tradition avoids splitting the infinitive to go."),
            ("Which sentence claims pizza was the only food eaten: 'I only ate pizza' or 'I ate only pizza'?",
             "I ate only pizza", "Only before pizza limits the food; before ate it limits the action."),
            ("What do you call a phrase that describes the wrong noun?",
             "misplaced modifier", "A misplaced modifier attaches to the wrong word."),
            ("In 'After reading the book, the movie was disappointing', what dangles?",
             "After reading the book", "The movie did not read the book - the modifier dangles."),
            ("Which is correct: 'Walking home, the rain started' or 'Walking home, I got caught in the rain'?",
             "Walking home, I got caught in the rain", "Only the second gives walking a doer."),
            ("In 'The teacher gave a test to the students with blue ink', what is ambiguous?",
             "with blue ink", "It is unclear whether the test or the students have blue ink."),
            ("Name the error in 'To win the game, practice is essential.'",
             "dangling modifier", "Practice cannot win the game by itself - the doer is missing."),
        ],
        "standards": STD_LANG, "citations": [CIT_OWL, CIT_CHICAGO],
        "sig_lens": SIG_LENS_QUIZ,
    },
    {
        "key": "qzla_subjunctive", "name": "Subjunctive Mood and Parallel Structure Quiz", "group": "Grammar",
        "ladder_rank": 9, "ladder_tier": "advanced",
        "intro": ("The summit of the grammar ladder: the subjunctive mood for "
                  "wishes and demands, and parallel structure for balanced "
                  "lists. Ten questions for the advanced climber. Answers at "
                  "the bottom."),
        "qa": [
            ("Choose the verb: 'I suggest that he ___.' (a) go (b) goes",
             "go", "Suggest triggers the subjunctive: that he go."),
            ("Choose the verb: 'If I ___ taller, I would reach it.' (a) was (b) were",
             "were", "Contrary-to-fact if takes were: if I were."),
            ("Choose the verb: 'She insisted that the report ___ finished.' (a) is (b) be",
             "be", "Insisted triggers the subjunctive: that the report be."),
            ("Which is parallel: 'She likes hiking, swimming, and to bike' or 'She likes hiking, swimming, and biking'?",
             "She likes hiking, swimming, and biking", "All three items match in -ing form."),
            ("Which replacement keeps the list parallel: 'The job requires patience, skill, and ___.' (a) to be on time (b) punctuality",
             "punctuality", "Punctuality matches the nouns patience and skill."),
            ("Choose the verb: 'It is essential that every student ___ on time.' (a) arrives (b) arrive",
             "arrive", "Essential triggers the subjunctive: that every student arrive."),
            ("Which is parallel: 'He is smart, funny, and has courage' or 'He is smart, funny, and courageous'?",
             "He is smart, funny, and courageous", "All three match as adjectives."),
            ("Choose the verb: 'The committee recommended that the rule ___ changed.' (a) is (b) be",
             "be", "Recommended triggers the subjunctive: that the rule be."),
            ("What mood is used in 'Long live the king'?",
             "subjunctive", "Long live expresses a wish - the subjunctive mood."),
            ("Which is parallel: 'To succeed takes work, patience, and practicing daily' or 'To succeed takes work, patience, and daily practice'?",
             "To succeed takes work, patience, and daily practice", "All three match as nouns."),
        ],
        "standards": STD_LANG, "citations": [CIT_OWL, CIT_CHICAGO],
        "sig_lens": SIG_LENS_QUIZ,
    },
]

ENTRIES += [
    # ==================== SPELLING AND PUNCTUATION ====================
    {
        "key": "qzla_spell_basic", "name": "Basic Spelling Quiz", "group": "Spelling and Punctuation",
        "ladder_rank": 1, "ladder_tier": "foundations",
        "intro": ("Ten everyday words, each hiding a common misspelling. "
                  "Pick the correct form - the small words are where spelling "
                  "is won or lost. Answers at the bottom."),
        "qa": [
            ("Which is the correct spelling? (a) house (b) hous (c) howse",
             "house", "House is spelled h-o-u-s-e."),
            ("Which is the correct spelling? (a) freind (b) friend (c) frend",
             "friend", "Friend follows i before e: f-r-i-e-n-d."),
            ("Which is the correct spelling? (a) becuase (b) because (c) becasue",
             "because", "Because is spelled b-e-c-a-u-s-e."),
            ("Which is the correct spelling? (a) definately (b) definitely (c) definetly",
             "definitely", "Definitely is spelled d-e-f-i-n-i-t-e-l-y."),
            ("Which is the correct spelling? (a) seperate (b) separate (c) seprate",
             "separate", "Separate is spelled s-e-p-a-r-a-t-e."),
            ("Which is the correct spelling? (a) recieve (b) receive (c) receeve",
             "receive", "Receive follows i before e except after c."),
            ("Which is the correct spelling? (a) neccessary (b) necessary (c) necesary",
             "necessary", "Necessary has one c and two s's."),
            ("Which is the correct spelling? (a) occassion (b) occasion (c) ocassion",
             "occasion", "Occasion has two c's and one s."),
            ("Which is the correct spelling? (a) writting (b) writing (c) writeing",
             "writing", "Writing drops the silent e before -ing."),
            ("Which is the correct spelling? (a) tommorow (b) tomorrow (c) tomorow",
             "tomorrow", "Tomorrow has one m and two r's."),
        ],
        "standards": STD_LANG, "citations": [CIT_WEBSTER],
        "sig_lens": SIG_LENS_QUIZ,
    },
    {
        "key": "qzla_plurals", "name": "Plurals Quiz", "group": "Spelling and Punctuation",
        "ladder_rank": 2, "ladder_tier": "foundations",
        "intro": ("Most plurals just add s - but the rebels refuse. Ten "
                  "questions on regular plurals and the irregular ones every "
                  "writer must memorize. Answers at the bottom."),
        "qa": [
            ("What is the plural of 'cat'?",
             "cats", "Regular nouns add s: cats."),
            ("What is the plural of 'box'?",
             "boxes", "Nouns ending in x add es: boxes."),
            ("What is the plural of 'baby'?",
             "babies", "Consonant plus y becomes ies: babies."),
            ("What is the plural of 'leaf'?",
             "leaves", "Leaf changes f to ves: leaves."),
            ("What is the plural of 'child'?",
             "children", "Child is irregular: children."),
            ("What is the plural of 'mouse'?",
             "mice", "Mouse is irregular: mice."),
            ("What is the plural of 'tooth'?",
             "teeth", "Tooth changes oo to ee: teeth."),
            ("What is the plural of 'sheep'?",
             "sheep", "Sheep is unchanged in the plural: sheep."),
            ("What is the plural of 'potato'?",
             "potatoes", "Potato adds es: potatoes."),
            ("What is the plural of 'woman'?",
             "women", "Woman is irregular: women."),
        ],
        "standards": STD_LANG, "citations": [CIT_WEBSTER, CIT_OWL],
        "sig_lens": SIG_LENS_QUIZ,
    },
    {
        "key": "qzla_apostrophe", "name": "Apostrophes Quiz", "group": "Spelling and Punctuation",
        "ladder_rank": 4, "ladder_tier": "compounded",
        "intro": ("The apostrophe does two jobs - possession and contraction - "
                  "and mixing them up is the most visible error in English. "
                  "Ten questions on its, it is, and whose belongs to whom. "
                  "Answers at the bottom."),
        "qa": [
            ("Choose the word: 'The dog lost ___ bone.' (a) its (b) it is",
             "its", "Its is the possessive; it is needs the apostrophe."),
            ("Choose the word: '___ a beautiful day.' (a) Its (b) It is",
             "It is", "It is a beautiful day - the contraction needs the apostrophe."),
            ("Write it correctly: 'the girls books' (the books of two girls)",
             "the girls' books", "The plural possessive puts the apostrophe after the s."),
            ("Which is the correct contraction of 'cannot'? (a) cant (b) can't",
             "can't", "The contraction of cannot is can't, with the apostrophe."),
            ("Write it correctly: 'the childrens toys'",
             "the children's toys", "Children is already plural, so add apostrophe s."),
            ("Which of these is the contraction of 'they are'? (a) their (b) theyre (c) they're",
             "they're", "The contraction of they are is they're."),
            ("Write it correctly: 'the cats toy' (the toy of one cat)",
             "the cat's toy", "One cat takes apostrophe s: the cat's toy."),
            ("Which is correct for a decade: (a) the 1990s (b) the 1990's",
             "the 1990s", "Decades take no apostrophe: the 1990s."),
            ("Write it correctly: 'Lets go'",
             "Let's go", "Let us contracts to let's with the apostrophe."),
            ("Which is the possessive form of 'it'? (a) its (b) it is",
             "its", "The possessive its never takes an apostrophe."),
        ],
        "standards": STD_LANG, "citations": [CIT_CHICAGO, CIT_OWL],
        "sig_lens": SIG_LENS_QUIZ,
    },
    {
        "key": "qzla_commas", "name": "Commas Quiz", "group": "Spelling and Punctuation",
        "ladder_rank": 5, "ladder_tier": "compounded",
        "intro": ("Commas separate, clarify, and save sentences from "
                  "nonsense. Ten questions on lists, introductions, "
                  "addresses, dates, and the mighty comma splice. Answers at "
                  "the bottom."),
        "qa": [
            ("Add the commas: 'I bought apples oranges and bananas.'",
             "I bought apples, oranges, and bananas.", "Commas separate the items in a list."),
            ("Add the comma: 'After dinner we went home.'",
             "After dinner, we went home.", "An introductory phrase takes a comma."),
            ("Which implies the speaker has just one brother: (a) 'My brother Sam is here.' (b) 'My brother, Sam, is here.'",
             "My brother, Sam, is here.", "The commas make Sam extra information - there is only one brother."),
            ("Fix the comma splice: 'It rained, we stayed inside.'",
             "It rained, so we stayed inside.", "A conjunction after the comma repairs the splice."),
            ("Add the comma: 'Yes I will help.'",
             "Yes, I will help.", "Yes at the start of a sentence takes a comma."),
            ("Add the commas: 'She is tall dark and handsome.'",
             "She is tall, dark, and handsome.", "Coordinate adjectives are separated by commas."),
            ("Does 'The big red ball bounced' need a comma between big and red?",
             "no", "Big and red are cumulative, not coordinate - no comma."),
            ("Add the comma: 'However we must try.'",
             "However, we must try.", "However as a sentence opener takes a comma."),
            ("Add the comma: 'July 4 1776'",
             "July 4, 1776", "A comma separates the day from the year."),
            ("Add the comma: 'He lives in Paris France.'",
             "He lives in Paris, France.", "A comma separates a city from its country or state."),
        ],
        "standards": STD_LANG, "citations": [CIT_CHICAGO, CIT_OWL],
        "sig_lens": SIG_LENS_QUIZ,
    },
    {
        "key": "qzla_spell_tricky", "name": "Tricky Spellings Quiz", "group": "Spelling and Punctuation",
        "ladder_rank": 6, "ladder_tier": "compounded",
        "intro": ("Double letters, silent letters, and traps laid by "
                  "history: ten of the most misspelled words in English. Only "
                  "the careful survive this rung. Answers at the bottom."),
        "qa": [
            ("Which is correct? (a) accommodate (b) accomodate (c) acommodate",
             "accommodate", "Accommodate has two c's and two m's."),
            ("Which is correct? (a) embarrass (b) embarass (c) embbarrass",
             "embarrass", "Embarrass has two r's and two s's."),
            ("Which is correct? (a) maintenance (b) maintainance (c) maintenence",
             "maintenance", "Maintenance keeps the ain of maintain."),
            ("Which is correct? (a) occurrence (b) occurance (c) ocurrence",
             "occurrence", "Occurrence doubles both the c and the r."),
            ("Which is correct? (a) rhythm (b) rythm (c) rhythem",
             "rhythm", "Rhythm is spelled r-h-y-t-h-m."),
            ("Which is correct? (a) vacuum (b) vaccuum (c) vacum",
             "vacuum", "Vacuum has one c and two u's."),
            ("Which is correct? (a) misspell (b) mispell (c) miss spell",
             "misspell", "Mis plus spell keeps both s's: misspell."),
            ("Which is correct? (a) cemetery (b) cemetary (c) cematery",
             "cemetery", "Cemetery is spelled with three e's."),
            ("Which is correct? (a) liaison (b) liason (c) liaision",
             "liaison", "Liaison is spelled l-i-a-i-s-o-n."),
            ("Which is correct? (a) pronunciation (b) pronounciation (c) pronuciation",
             "pronunciation", "Pronunciation drops the o of pronounce."),
        ],
        "standards": STD_LANG, "citations": [CIT_WEBSTER],
        "sig_lens": SIG_LENS_QUIZ,
    },
    # ============================ LITERATURE ============================
    {
        "key": "qzla_childlit", "name": "Classic Childrens Literature Quiz", "group": "Literature",
        "ladder_rank": 2, "ladder_tier": "foundations",
        "intro": ("The books of childhood are the foundation of a reading "
                  "life. Ten questions on the beloved classics every reader "
                  "meets first. Answers at the bottom."),
        "qa": [
            ("Who wrote 'Charlotte's Web'?",
             "E. B. White", "E. B. White wrote Charlotte's Web (1952)."),
            ("Who wrote 'Where the Wild Things Are'?",
             "Maurice Sendak", "Maurice Sendak wrote and illustrated it (1963)."),
            ("What is the name of the lion in 'The Lion, the Witch and the Wardrobe'?",
             "Aslan", "Aslan is the great lion of Narnia."),
            ("Who wrote 'Matilda'?",
             "Roald Dahl", "Roald Dahl wrote Matilda (1988)."),
            ("Who wrote 'Goodnight Moon'?",
             "Margaret Wise Brown", "Margaret Wise Brown wrote Goodnight Moon (1947)."),
            ("What is the name of the wooden boy in Carlo Collodi's tale?",
             "Pinocchio", "Pinocchio is the wooden puppet who becomes a real boy."),
            ("Who wrote 'The Very Hungry Caterpillar'?",
             "Eric Carle", "Eric Carle wrote and illustrated it (1969)."),
            ("Who wrote 'The Tale of Peter Rabbit'?",
             "Beatrix Potter", "Beatrix Potter wrote it in 1902."),
            ("What does the very hungry caterpillar turn into at the end?",
             "a butterfly", "The caterpillar becomes a beautiful butterfly."),
            ("Who wrote 'Green Eggs and Ham'?",
             "Dr. Seuss", "Dr. Seuss (Theodor Geisel) wrote it in 1960."),
        ],
        "standards": STD_LIT, "citations": [CIT_NORTON],
        "sig_lens": SIG_LENS_QUIZ,
    },
    {
        "key": "qzla_litterms", "name": "Literary Terms Basics Quiz", "group": "Literature",
        "ladder_rank": 4, "ladder_tier": "compounded",
        "intro": ("To talk about stories you need the vocabulary of stories. "
                  "Ten questions on the essential literary terms - "
                  "protagonist, plot, theme, and their kin. Answers at the "
                  "bottom."),
        "qa": [
            ("What is the main character of a story called?",
             "the protagonist", "The protagonist is the central character."),
            ("What is the character who opposes the protagonist called?",
             "the antagonist", "The antagonist works against the protagonist."),
            ("What is the time and place of a story called?",
             "the setting", "The setting is where and when the story happens."),
            ("What is the sequence of events in a story called?",
             "the plot", "The plot is the ordered chain of events."),
            ("What is the turning point of a story called?",
             "the climax", "The climax is the moment of highest tension."),
            ("What is the central message or insight of a story called?",
             "the theme", "The theme is the story's central idea."),
            ("What is a comparison using 'like' or 'as' called?",
             "a simile", "A simile compares with like or as."),
            ("What is a direct comparison without 'like' or 'as' called?",
             "a metaphor", "A metaphor states the comparison directly."),
            ("What is the narrator's attitude toward the subject called?",
             "the tone", "Tone is the attitude the writing conveys."),
            ("What is giving human qualities to nonhuman things called?",
             "personification", "Personification lends human traits to the nonhuman."),
        ],
        "standards": STD_LIT, "citations": [CIT_NORTON, CIT_MLA],
        "sig_lens": SIG_LENS_QUIZ,
    },
    {
        "key": "qzla_openings", "name": "Famous Opening Lines Quiz", "group": "Literature",
        "ladder_rank": 5, "ladder_tier": "compounded",
        "intro": ("Great novels announce themselves in a single line. Ten "
                  "questions matching immortal opening lines to the books "
                  "they begin. Answers at the bottom."),
        "qa": [
            ("'Call me Ishmael.' opens which novel?",
             "Moby-Dick", "Herman Melville's Moby-Dick (1851) begins 'Call me Ishmael.'"),
            ("'It was the best of times, it was the worst of times.' opens which novel?",
             "A Tale of Two Cities", "Charles Dickens's A Tale of Two Cities (1859)."),
            ("'All happy families are alike; each unhappy family is unhappy in its own way.' opens which novel?",
             "Anna Karenina", "Leo Tolstoy's Anna Karenina (1878)."),
            ("'It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.' opens which novel?",
             "Pride and Prejudice", "Jane Austen's Pride and Prejudice (1813)."),
            ("'In a hole in the ground there lived a hobbit.' opens which novel?",
             "The Hobbit", "J. R. R. Tolkien's The Hobbit (1937)."),
            ("'Last night I dreamt I went to Manderley again.' opens which novel?",
             "Rebecca", "Daphne du Maurier's Rebecca (1938)."),
            ("'It was a bright cold day in April, and the clocks were striking thirteen.' opens which novel?",
             "Nineteen Eighty-Four", "George Orwell's Nineteen Eighty-Four (1949)."),
            ("'You better not never tell nobody but God.' opens which novel?",
             "The Color Purple", "Alice Walker's The Color Purple (1982)."),
            ("'The past is a foreign country; they do things differently there.' opens which novel?",
             "The Go-Between", "L. P. Hartley's The Go-Between (1953)."),
            ("'All children, except one, grow up.' opens which novel?",
             "Peter Pan", "J. M. Barrie's Peter Pan (1911 novel form)."),
        ],
        "standards": STD_LIT, "citations": [CIT_NORTON],
        "sig_lens": SIG_LENS_QUIZ,
    },
    {
        "key": "qzla_amclassics", "name": "American Classics Quiz", "group": "Literature",
        "ladder_rank": 6, "ladder_tier": "compounded",
        "intro": ("The shelf of American classics: ten questions on the "
                  "novels, authors, and characters that shaped American "
                  "letters. Answers at the bottom."),
        "qa": [
            ("Who wrote 'The Great Gatsby'?",
             "F. Scott Fitzgerald", "F. Scott Fitzgerald published it in 1925."),
            ("Who wrote 'To Kill a Mockingbird'?",
             "Harper Lee", "Harper Lee published it in 1960."),
            ("Who narrates 'The Great Gatsby'?",
             "Nick Carraway", "Nick Carraway tells Gatsby's story."),
            ("Who wrote 'The Adventures of Huckleberry Finn'?",
             "Mark Twain", "Mark Twain (Samuel Clemens) published it in 1884."),
            ("In what fictional town is 'To Kill a Mockingbird' set?",
             "Maycomb", "Maycomb, Alabama is the novel's fictional town."),
            ("Who wrote 'Moby-Dick'?",
             "Herman Melville", "Herman Melville published it in 1851."),
            ("What is Captain Ahab hunting in 'Moby-Dick'?",
             "the white whale", "Ahab hunts the white whale, Moby Dick."),
            ("Who wrote 'The Scarlet Letter'?",
             "Nathaniel Hawthorne", "Nathaniel Hawthorne published it in 1850."),
            ("What letter must Hester Prynne wear in 'The Scarlet Letter'?",
             "the letter A", "Hester wears a scarlet letter A for adultery."),
            ("Who wrote 'Of Mice and Men'?",
             "John Steinbeck", "John Steinbeck published it in 1937."),
        ],
        "standards": STD_LIT, "citations": [CIT_NORTON],
        "sig_lens": SIG_LENS_QUIZ,
    },
    {
        "key": "qzla_shakespeare", "name": "Shakespeare Quiz", "group": "Literature",
        "ladder_rank": 8, "ladder_tier": "advanced",
        "intro": ("Four centuries on, the Bard still sets the bar. Ten "
                  "questions on the plays, characters, and lines every "
                  "educated reader should know. Answers at the bottom."),
        "qa": [
            ("In which play does the line 'To be, or not to be' appear?",
             "Hamlet", "Hamlet speaks the famous soliloquy in Act 3."),
            ("Which play tells the story of Romeo and Juliet?",
             "Romeo and Juliet", "The tragedy of the star-crossed lovers."),
            ("Who is Hamlet's uncle, the man who murdered Hamlet's father?",
             "Claudius", "Claudius marries Gertrude and takes the throne."),
            ("In 'Macbeth', what do the witches predict for Macbeth?",
             "that Macbeth will become king", "The witches hail him as future king."),
            ("Which comedy features the sparring lovers Beatrice and Benedick?",
             "Much Ado About Nothing", "Beatrice and Benedick wage their merry war there."),
            ("In which play does Jacques say 'All the world's a stage'?",
             "As You Like It", "The Seven Ages of Man speech is in As You Like It."),
            ("Who is the Moor of Venice?",
             "Othello", "Othello is Shakespeare's Moorish general."),
            ("In 'Julius Caesar', who delivers the 'Friends, Romans, countrymen' speech?",
             "Mark Antony", "Antony's funeral oration turns the crowd."),
            ("Which play features the moneylender Shylock?",
             "The Merchant of Venice", "Shylock demands his pound of flesh there."),
            ("How many sonnets did Shakespeare write?",
             "154", "Shakespeare's sonnet sequence holds 154 sonnets."),
        ],
        "standards": STD_LIT, "citations": [CIT_NORTON],
        "sig_lens": SIG_LENS_QUIZ,
    },
    {
        "key": "qzla_movements", "name": "Literary Movements Quiz", "group": "Literature",
        "ladder_rank": 9, "ladder_tier": "advanced",
        "intro": ("Literature moves in waves - ten questions on the great "
                  "movements from Neoclassicism to Postmodernism. Name the "
                  "wave from its shape. Answers at the bottom."),
        "qa": [
            ("Which movement prized emotion, nature, and individualism in the late 1700s to mid-1800s?",
             "Romanticism", "Romanticism celebrated feeling and nature."),
            ("Which movement sought to depict life exactly as it is, without idealization?",
             "Realism", "Realism rendered ordinary life faithfully."),
            ("Which movement used stream of consciousness and fragmented narratives?",
             "Modernism", "Modernism broke narrative into fragments and interior monologue."),
            ("Which literary movement of the late 1600s and 1700s prized reason, order, and classical models?",
             "Neoclassicism", "Neoclassicism revived classical ideals of reason and order."),
            ("Which American movement included Emerson and Thoreau and stressed self-reliance and nature?",
             "Transcendentalism", "Transcendentalism centered on the soul, nature, and self-reliance."),
            ("Which movement portrayed heredity and environment as determining human fate?",
             "Naturalism", "Naturalism applied determinism to fiction."),
            ("Which movement rejected absolute truth and embraced irony and pastiche after World War II?",
             "Postmodernism", "Postmodernism plays with irony, parody, and fragmentation."),
            ("Which movement featured spontaneous prose and the writers of the Beat Generation?",
             "the Beat movement", "The Beats wrote spontaneous, jazz-inflected prose and poetry."),
            ("Which movement belonged to the Black writers and artists of 1920s Harlem?",
             "the Harlem Renaissance", "The Harlem Renaissance flowered in 1920s New York."),
            ("Which movement used rich sensory imagery and symbols to suggest moods, flourishing in late-1800s France?",
             "Symbolism", "Symbolism suggested states of soul through image and symbol."),
        ],
        "standards": STD_LIT, "citations": [CIT_NORTON, CIT_MLA],
        "sig_lens": SIG_LENS_QUIZ,
    },
]

ENTRIES += [
    # ========================= WORDPLAY AND PUZZLES =========================
    {
        "key": "qzla_anagrams", "name": "Anagrams Quiz", "group": "Wordplay and Puzzles",
        "ladder_rank": 3, "ladder_tier": "foundations",
        "intro": ("An anagram rearranges the letters of a word into a new "
                  "one - the alphabet's favorite magic trick. Ten questions "
                  "on spotting and solving them. Answers at the bottom."),
        "qa": [
            ("Which of these is an anagram of 'listen'? (a) silent (b) list (c) tin (d) net",
             "silent", "Listen rearranged spells silent."),
            ("What word is an anagram of 'dusty'?",
             "study", "Dusty rearranged spells study."),
            ("What word is an anagram of 'night'?",
             "thing", "Night rearranged spells thing."),
            ("What word is an anagram of 'acts'?",
             "cats", "Acts rearranged spells cats."),
            ("Which of these is an anagram of 'save'? (a) vase (b) saves (c) very (d) safe",
             "vase", "Save rearranged spells vase."),
            ("What word is an anagram of 'below'?",
             "elbow", "Below rearranged spells elbow."),
            ("Which of these is an anagram of 'evil'? (a) veil (b) live (c) vile (d) all of these",
             "all of these", "Veil, live, and vile all use the letters of evil."),
            ("What word is an anagram of 'married'?",
             "admirer", "Married rearranged spells admirer."),
            ("What famous phrase is an anagram of 'a gentleman'?",
             "elegant man", "A gentleman rearranged spells elegant man."),
            ("What famous phrase is an anagram of 'astronomer'?",
             "moon starer", "Astronomer rearranged spells moon starer."),
        ],
        "standards": STD_LANG, "citations": [CIT_OED, CIT_WEBSTER],
        "sig_lens": SIG_LENS_QUIZ,
    },
    {
        "key": "qzla_palindromes", "name": "Palindromes and Word Patterns Quiz", "group": "Wordplay and Puzzles",
        "ladder_rank": 4, "ladder_tier": "compounded",
        "intro": ("Palindromes read the same forward and backward - words "
                  "that look in a mirror and see themselves. Ten questions on "
                  "these and other word patterns. Answers at the bottom."),
        "qa": [
            ("Which word is a palindrome? (a) level (b) lemon (c) ladder (d) lantern",
             "level", "Level reads the same backward and forward."),
            ("Which word is a palindrome? (a) radar (b) radio (c) rapid (d) river",
             "radar", "Radar reads the same backward and forward."),
            ("'A man, a plan, a canal: Panama' is famous as what?",
             "a palindrome", "Ignoring spaces and punctuation, it reads the same both ways."),
            ("What do you call a word that reads the same backward and forward?",
             "a palindrome", "That is the definition of a palindrome."),
            ("Is 'madam' a palindrome?",
             "yes", "Madam reads the same backward and forward."),
            ("Which is NOT a palindrome? (a) civic (b) kayak (c) motor (d) refer",
             "motor", "Civic, kayak, and refer are palindromes; motor is not."),
            ("Which five-letter word for a small boat is a palindrome?",
             "kayak", "Kayak reads the same backward and forward."),
            ("'Was it a car or a cat I saw' is an example of what?",
             "a palindrome", "The whole sentence mirrors itself."),
            ("Which phrase is a palindrome ignoring spaces: (a) 'never odd or even' (b) 'hello world'",
             "never odd or even", "Never odd or even mirrors itself."),
            ("What is a semordnilap - 'palindromes' spelled backward?",
             "a word that becomes a different word when reversed", "Like stressed becoming desserts."),
        ],
        "standards": STD_LANG, "citations": [CIT_OED, CIT_WEBSTER],
        "sig_lens": SIG_LENS_QUIZ,
    },
    {
        "key": "qzla_riddles", "name": "Riddles and Word Riddles Quiz", "group": "Wordplay and Puzzles",
        "ladder_rank": 5, "ladder_tier": "compounded",
        "intro": ("Riddles are questions wearing disguises. Ten classic "
                  "riddles to test whether you can see through the costume. "
                  "Answers at the bottom - no peeking."),
        "qa": [
            ("What has keys but cannot open locks?",
             "a piano", "A piano has keys that play notes, not locks."),
            ("What gets wetter the more it dries?",
             "a towel", "A towel absorbs water as it dries you."),
            ("What has a face and hands but no body?",
             "a clock", "A clock has a face and hands that tell time."),
            ("What runs but never walks?",
             "a river", "A river runs constantly but never walks."),
            ("The more you take, the more you leave behind. What is it?",
             "footsteps", "Each step you take leaves a footprint behind."),
            ("What has words but never speaks?",
             "a book", "A book holds words in silence."),
            ("What goes up but never comes down?",
             "your age", "Your age only ever increases."),
            ("What can you catch but never throw?",
             "a cold", "You catch a cold but cannot throw one."),
            ("What is full of holes but still holds water?",
             "a sponge", "A sponge is full of holes yet holds water."),
            ("What belongs to you but others use it more than you do?",
             "your name", "Others say your name more than you do."),
        ],
        "standards": STD_LANG, "citations": [CIT_WEBSTER],
        "sig_lens": SIG_LENS_QUIZ,
    },
    {
        "key": "qzla_cryptic", "name": "Cryptic-Style Wordplay Quiz", "group": "Wordplay and Puzzles",
        "ladder_rank": 7, "ladder_tier": "compounded",
        "intro": ("Cryptic crosswords are the black belt of wordplay: every "
                  "clue hides a definition and a trick. Ten questions on the "
                  "signals and a few gentle solves. Answers at the bottom."),
        "qa": [
            ("In a cryptic clue, what does a word like 'confused' or 'mixed up' signal?",
             "an anagram", "Confusion words signal an anagram."),
            ("In a cryptic clue, what does 'sounds like' signal?",
             "a homophone", "Sounds-like signals a homophone."),
            ("In a cryptic clue, what does 'hidden in' signal?",
             "a hidden word", "Hidden-in signals a word buried in the clue text."),
            ("Solve it: 'Mixed up tea (3)'",
             "eat", "Tea mixed up spells eat."),
            ("Solve it: 'Heard the flower (4)'",
             "rows", "A flower is a rose; heard, it becomes rows."),
            ("What two parts does every cryptic clue contain?",
             "a definition and wordplay", "Every cryptic clue has a definition and wordplay."),
            ("Solve it: 'Broken spear (5)'",
             "spare", "Spear broken spells spare."),
            ("In a down clue, what does a word like 'back' or 'returned' signal?",
             "a reversal", "Back and returned signal reading backward."),
            ("Solve it: 'Wild animal returned (3)'",
             "god", "A wild animal reversed - dog returned is god."),
            ("In a cryptic clue, where does the definition usually sit?",
             "the first or last word", "The definition is at one end of the clue."),
        ],
        "standards": STD_LANG, "citations": [CIT_OED],
        "sig_lens": SIG_LENS_QUIZ,
    },
    # ========================= READING AND RHETORIC =========================
    {
        "key": "qzla_figurative", "name": "Figurative Language Quiz", "group": "Reading and Rhetoric",
        "ladder_rank": 3, "ladder_tier": "foundations",
        "intro": ("Writers rarely say things straight - they bend language "
                  "into shapes. Ten questions on simile, metaphor, and the "
                  "rest of the figurative toolbox. Answers at the bottom."),
        "qa": [
            ("'He runs like the wind.' What device is this?",
             "simile", "Like signals a simile."),
            ("'She is a shining star.' What device is this?",
             "metaphor", "The direct comparison is a metaphor."),
            ("'The wind whispered through the trees.' What device is this?",
             "personification", "The wind is given the human act of whispering."),
            ("'I have told you a million times.' What device is this?",
             "hyperbole", "The million is deliberate exaggeration."),
            ("'The classroom was a zoo.' What device is this?",
             "metaphor", "The classroom is directly called a zoo."),
            ("'Peter Piper picked a pepper.' What device is this?",
             "alliteration", "The repeated p sound is alliteration."),
            ("'The sizzle of the bacon.' What device is this?",
             "onomatopoeia", "Sizzle imitates the sound it names."),
            ("'Parting is such sweet sorrow.' What device is this?",
             "oxymoron", "Sweet and sorrow contradict in one phrase."),
            ("'The pen is mightier than the sword.' What device is this?",
             "metonymy", "Pen stands for writing, sword for military force."),
            ("'Speech is silver, silence is golden.' What device is this?",
             "antithesis", "The balanced opposites form an antithesis."),
        ],
        "standards": STD_LIT, "citations": [CIT_NORTON, CIT_PRINCETON],
        "sig_lens": SIG_LENS_QUIZ,
    },
    {
        "key": "qzla_rhetoric", "name": "Rhetorical Devices Quiz", "group": "Reading and Rhetoric",
        "ladder_rank": 6, "ladder_tier": "compounded",
        "intro": ("Rhetoric is the art of persuasion in words. Ten questions "
                  "on the devices speakers have used since ancient Athens - "
                  "anaphora, chiasmus, and their kin. Answers at the bottom."),
        "qa": [
            ("Repeating a word at the start of successive clauses, as in 'We shall fight on the beaches', is called what?",
             "anaphora", "Anaphora repeats the opening word or phrase."),
            ("Repeating a word at the end of successive clauses is called what?",
             "epistrophe", "Epistrophe repeats the closing word or phrase."),
            ("Addressing an absent person or abstraction, as in 'O Death', is called what?",
             "apostrophe", "The rhetorical apostrophe addresses the absent."),
            ("'I came, I saw, I conquered' shows what structure?",
             "parallelism", "The three matching clauses are parallel."),
            ("What do you call a question asked for effect, with no answer expected?",
             "a rhetorical question", "A rhetorical question persuades rather than asks."),
            ("Calling a huge problem 'a minor hiccup' is an example of what?",
             "understatement", "Deliberate understatement minimizes for effect."),
            ("'The White House announced today' - the building standing for its people - is what?",
             "metonymy", "The place stands for the institution: metonymy."),
            ("Substituting a part for the whole, as in 'all hands on deck', is what?",
             "synecdoche", "Hands stand for sailors: synecdoche."),
            ("Deliberate exaggeration for effect is called what?",
             "hyperbole", "Hyperbole is strategic overstatement."),
            ("Reversing grammatical structure, as in 'Ask not what your country can do for you - ask what you can do for your country', is called what?",
             "chiasmus", "The ABBA reversal is chiasmus."),
        ],
        "standards": STD_LIT, "citations": [CIT_NORTON, CIT_PRINCETON],
        "sig_lens": SIG_LENS_QUIZ,
    },
    {
        "key": "qzla_inference", "name": "Reading Inference Quiz", "group": "Reading and Rhetoric",
        "ladder_rank": 7, "ladder_tier": "compounded",
        "intro": ("Strong readers see what the page does not say. Ten "
                  "mini-scenes - read each one and infer what must be true. "
                  "Answers at the bottom."),
        "qa": [
            ("'Mara grabbed her umbrella and raincoat before heading out.' What can you infer about the weather?",
             "it is raining or about to rain", "Umbrella and raincoat mean rain."),
            ("'The dog nosed his empty bowl across the kitchen floor.' What does the dog probably want?",
             "food", "An empty bowl pushed toward you means feed me."),
            ("'Jake's hands shook as he stepped onto the stage.' What is Jake probably feeling?",
             "nervous", "Shaking hands before a performance mean nerves."),
            ("'The streets were empty, the shops dark, and a single streetlamp flickered.' What time is it probably?",
             "late at night", "Empty dark streets mean the small hours."),
            ("'She set three plates on the table, though only two people lived there.' What can you infer?",
             "she is expecting a guest", "The third plate means company is coming."),
            ("'His suitcase was packed, his passport on the counter, and a taxi waited outside.' What is he about to do?",
             "take a trip", "Packed bags and a passport mean travel."),
            ("'The teacher smiled and wrote Excellent in red ink at the top.' How did the student do?",
             "very well", "Excellent in red ink means top marks."),
            ("'Leaves crunched underfoot and the air smelled of woodsmoke.' What season is it?",
             "autumn", "Falling leaves and woodsmoke mean autumn."),
            ("'She read the same paragraph four times without understanding a word.' What is true about her focus?",
             "she is distracted", "Rereading without absorbing means her mind is elsewhere."),
            ("'The line at the box office stretched around the block.' What can you infer about the show?",
             "it is very popular", "A line around the block means high demand."),
        ],
        "standards": STD_LANG, "citations": [CIT_OWL],
        "sig_lens": SIG_LENS_QUIZ,
    },
    # ========================== POETRY AND PROSODY ==========================
    {
        "key": "qzla_poetry_forms", "name": "Poetry Forms Quiz", "group": "Poetry and Prosody",
        "ladder_rank": 8, "ladder_tier": "advanced",
        "intro": ("Sonnets, haiku, villanelles - ten questions on the fixed "
                  "forms poets have filled for centuries. Know the shape and "
                  "you can hear the poem. Answers at the bottom."),
        "qa": [
            ("How many lines does a sonnet have?",
             "14", "A sonnet is fourteen lines."),
            ("How many lines does a haiku have?",
             "3", "A haiku is three lines."),
            ("What is the syllable pattern of a traditional haiku?",
             "5-7-5", "Haiku runs five, seven, then five syllables."),
            ("How many lines does a limerick have?",
             "5", "A limerick is five lines."),
            ("What is the rhyme scheme of a limerick?",
             "AABBA", "Limericks rhyme AABBA."),
            ("What do you call a nineteen-line poem built on two repeating refrains?",
             "a villanelle", "The villanelle weaves two refrains through nineteen lines."),
            ("How many lines does a ballad stanza usually have?",
             "4", "The ballad stanza is a quatrain: four lines."),
            ("What does an ode do?",
             "praises its subject", "An ode is a lyric poem praising its subject."),
            ("What is an elegy?",
             "a poem mourning the dead", "An elegy laments loss, often death."),
            ("What is free verse?",
             "poetry without regular rhyme or meter", "Free verse drops fixed meter and rhyme."),
        ],
        "standards": STD_POETRY, "citations": [CIT_PRINCETON, CIT_NORTON],
        "sig_lens": SIG_LENS_QUIZ,
    },
    {
        "key": "qzla_meter", "name": "Meter and Sound Devices Quiz", "group": "Poetry and Prosody",
        "ladder_rank": 10, "ladder_tier": "advanced",
        "intro": ("The top of the ladder: the music of verse itself. Ten "
                  "questions on iambs, trochees, and the sound devices that "
                  "make lines sing. Answers at the bottom."),
        "qa": [
            ("What is an iamb?",
             "unstressed then stressed", "An iamb is an unstressed syllable followed by a stressed one."),
            ("What is a trochee?",
             "stressed then unstressed", "A trochee is a stressed syllable followed by an unstressed one."),
            ("How many metrical feet are in a line of iambic pentameter?",
             "5", "Penta means five: five iambic feet."),
            ("How many syllables are in a line of iambic pentameter?",
             "10", "Five feet of two syllables make ten."),
            ("What is the stress pattern of a dactyl?",
             "stressed, unstressed, unstressed", "A dactyl falls: stressed, unstressed, unstressed."),
            ("What is the stress pattern of an anapest?",
             "unstressed, unstressed, stressed", "An anapest rises: unstressed, unstressed, stressed."),
            ("What is alliteration?",
             "repetition of initial consonant sounds", "Alliteration repeats opening consonants."),
            ("What is assonance?",
             "repetition of vowel sounds", "Assonance repeats vowel sounds within words."),
            ("What is consonance?",
             "repetition of consonant sounds", "Consonance repeats consonant sounds within or ending words."),
            ("'Shall I compare thee to a summer's day' is written in what meter?",
             "iambic pentameter", "Shakespeare's sonnet line is ten syllables of iambs."),
        ],
        "standards": STD_POETRY, "citations": [CIT_PRINCETON],
        "sig_lens": SIG_LENS_QUIZ,
    },
]

assert len(ENTRIES) == 34, "expected 34 entries, got %d" % len(ENTRIES)
assert all(len(e["qa"]) == 10 for e in ENTRIES), "every quiz must hold 10 questions"
assert len({e["key"] for e in ENTRIES}) == 34, "duplicate keys"
assert len({e["name"] for e in ENTRIES}) == 34, "duplicate names"
_ranks = [e["ladder_rank"] for e in ENTRIES]
assert all(1 <= r <= 10 for r in _ranks), "ladder_rank out of range"
