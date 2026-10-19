#!/usr/bin/env python3
"""Entries for the Personality databases (Manon's 16:15 orders, 2026-10-17).

The Personality Database (public-harvest) and The Personality Signature
Database (signature): 34 ladder-ordered records each covering personality
psychology - the major trait models (Big Five, HEXACO), personality types,
how traits show up in behavior, and how to understand one's own and other
people's personalities. Each record is a FULL fully-formed entry: trait/type
description, behaviors, strengths, growth edges, and how to work with it.

Public records are real, fact-checked psychology knowledge. Standard
references: Costa PT, McCrae RR. The Revised NEO Personality Inventory
(NEO-PI-R); Professional Manual; 1992. Ashton MC, Lee K. The HEXACO model
of personality structure; Journal of Personality; 2007. Goldberg LR. An
alternative "description of personality": The Big-Five factor structure;
Journal of Personality and Social Psychology; 1990. John OP, Srivastava S.
The Big Five trait taxonomy: History, measurement, and theoretical
perspectives; Handbook of Personality; 1999. McCrae RR, Costa PT. The
five-factor theory of personality; Handbook of Personality; 1999.
Eysenck HJ. The Biological Basis of Personality; 1967. Jung CG.
Psychological Types; 1921. Myers IB, Myers PB. Gifts Differing; 1980.
Riso DR, Hudson R. Personality Types; 1996. Marston WM. Emotions of Normal
People; 1928. Allport GW. Personality: A Psychological Interpretation;
1937. Cattell RB. The 16PF Personality Questionnaire; 1949/1993.
Roberts BW, Mroczek DK. Personality trait change in adulthood; Current
Directions in Psychological Science; 2008. Mischel W. Personality and
Assessment; 1968. Mischel W, Shoda Y. A cognitive-affective system theory
of personality; Psychological Review; 1995. McCrae RR et al. Universal
features of personality traits from the observer's perspective;
Journal of Personality and Social Psychology; 2005. APA Dictionary of
Psychology; American Psychological Association.

Signature editions are his original Signature Personality Method - the same
ladder read through the Signature lens: every trait a signature frequency,
every profile a chord, growth the deliberate retuning of the chord. Clearly
labeled Signature-made, never presented as authentic public record.

Teaching ladder (rank 1-10, tiers foundations/compounded/advanced):
Foundations (1-4): what personality is, traits vs states vs types, the Big
Five, the five domains one by one, HEXACO, facets, measurement sources,
nature and nurture. Compounded (5-7): type models (Jung/MBTI, Enneagram,
DISC, temperaments, 16PF), reading full profiles, personality at work and
in relationships, reliability and validity, the person-situation debate,
team chemistry. Advanced (8-10): stability and change across the lifespan,
the maturity principle, decision-making, ethical reading of others,
leadership, culture, conflict styles, deliberate growth, the integrated
view of all models together.

Screening: nothing hate-adjacent, profane, or inappropriate; no religious
talk; no diagnosis of real people and no clinical disorder content - this
database covers normal-range personality psychology only.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature Personality Method: "
            "every trait a signature frequency, every profile a chord of "
            "frequencies, growth the deliberate retuning of the chord. "
            "Clearly labeled Signature-made, never presented as authentic "
            "public record.")

CIT_NEO = ("Costa PT, McCrae RR. The Revised NEO Personality Inventory "
           "(NEO-PI-R); Professional Manual. Psychological Assessment "
           "Resources; 1992.")
CIT_HEXACO = ("Ashton MC, Lee K. Empirical, theoretical, and practical "
              "advantages of the HEXACO model of personality structure. "
              "Personality and Social Psychology Review; 2007.")
CIT_GOLDBERG = ("Goldberg LR. An alternative 'description of personality': "
                "The Big-Five factor structure. Journal of Personality and "
                "Social Psychology; 1990.")
CIT_BIGFIVE_TAX = ("John OP, Srivastava S. The Big Five trait taxonomy: "
                   "History, measurement, and theoretical perspectives. In "
                   "Handbook of Personality: Theory and Research. 2nd ed. "
                   "Guilford Press; 1999.")
CIT_FFT = ("McCrae RR, Costa PT. The five-factor theory of personality. In "
           "Handbook of Personality: Theory and Research. 2nd ed. Guilford "
           "Press; 1999.")
CIT_EYSENCK = ("Eysenck HJ. The Biological Basis of Personality. Charles C. "
               "Thomas; 1967.")
CIT_JUNG = ("Jung CG. Psychological Types. Princeton University Press; 1921.")
CIT_MBTI = ("Myers IB, Myers PB. Gifts Differing: Understanding Personality "
            "Type. Consulting Psychologists Press; 1980.")
CIT_ENNEAGRAM = ("Riso DR, Hudson R. Personality Types: Using the Enneagram "
                 "for Self-Discovery. Houghton Mifflin; 1996.")
CIT_DISC = ("Marston WM. Emotions of Normal People. Harcourt, Brace; 1928.")
CIT_ALLPORT = ("Allport GW. Personality: A Psychological Interpretation. "
               "Henry Holt; 1937.")
CIT_16PF = ("Cattell RB. The 16PF Personality Questionnaire. Institute for "
            "Personality and Ability Testing; 1949, 5th ed. 1993.")
CIT_MATURITY = ("Roberts BW, Mroczek DK. Personality trait change in "
                "adulthood. Current Directions in Psychological Science; "
                "2008.")
CIT_MISCHEL = ("Mischel W. Personality and Assessment. Wiley; 1968.")
CIT_CAPS = ("Mischel W, Shoda Y. A cognitive-affective system theory of "
            "personality: Reconceptualizing situations, dispositions, "
            "dynamics, and invariance in personality structure. "
            "Psychological Review; 1995.")
CIT_CULTURE = ("McCrae RR et al. Universal features of personality traits "
               "from the observer's perspective: Data from 50 cultures. "
               "Journal of Personality and Social Psychology; 2005.")
CIT_APA = ("APA Dictionary of Psychology. American Psychological "
           "Association.")

STD_BIGFIVE = ("Big Five terminology follows Costa & McCrae (1992) and John "
               "& Srivastava (1999): Openness, Conscientiousness, "
               "Extraversion, Agreeableness, Neuroticism.")
STD_HEXACO = ("HEXACO terminology follows Ashton & Lee (2007): "
              "Honesty-Humility, Emotionality, eXtraversion, Agreeableness, "
              "Conscientiousness, Openness to Experience.")
STD_TYPES = ("Type descriptions follow the named model's own published "
             "framework; types are preferences and patterns, not boxes - "
             "everyone uses all functions and styles to some degree.")

ENTRIES = [
    {
        "key": "what_is",
        "name": "What Personality Is",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Personality is the characteristic pattern of thoughts, feelings, "
            "and behaviors that makes a person distinctively themselves. "
            "Psychologists define it as the relatively stable individual "
            "differences in how people tend to think, feel, and act across "
            "situations and over time (Allport, 1937; APA Dictionary). It is "
            "not a mood that changes by the hour and not a role put on for an "
            "occasion - it is the underlying tendencies that make one "
            "person reliably more outgoing, more careful, more curious, or "
            "more even-tempered than another, year after year. Personality "
            "shows up everywhere: in the words a person chooses, in how they "
            "handle a deadline, in whether they recharge alone or with "
            "people, in how they argue and how they apologize. Because it is "
            "patterned, it can be studied: researchers measure it with "
            "questionnaires, observe it in behavior, and find that the "
            "patterns predict real outcomes - job performance, health "
            "habits, relationship satisfaction, and longevity. This record is "
            "the doorway to the whole database: everything that follows is "
            "one way of mapping those stable patterns, from broad trait "
            "models to type systems to the practical art of reading and "
            "working with personalities - your own and other people's."
        ),
        "how_it_works": (
            "Personality works as a set of dispositions: tendencies to "
            "respond to the world in certain ways. A disposition toward "
            "sociability does not force a person to talk at every gathering, "
            "but it tilts every gathering in that direction - more "
            "initiating, more energy from the room, more disappointment when "
            "the room is empty. These tilts aggregate: one outgoing act "
            "proves little, but thousands of small tilts across years add "
            "up to a life that looks unmistakably sociable. Researchers "
            "capture the tilts with trait adjectives - thousands of words in "
            "every language describe stable differences (curious, punctual, "
            "warm, anxious) - and factor analysis groups those words into "
            "families, which is how the Big Five and HEXACO models were "
            "discovered. Measurement turns the pattern into numbers: a "
            "person rates how well statements describe them, and the scores "
            "place them on each dimension relative to other people. The "
            "numbers are comparative, not grades - high extraversion is not "
            "better than low extraversion, it is simply a different setting "
            "with different strengths and different costs."
        ),
        "key_points": [
            "Personality is the stable pattern of thinking, feeling, and behaving that distinguishes one person from another across situations and time.",
            "Traits are tendencies, not guarantees: a sociable person can be quiet at one party, but the pattern across hundreds of parties is unmistakable.",
            "Trait words cluster into families in every language studied, which is why the same broad models keep emerging from the data.",
            "Personality scores are comparative placements on a dimension, not grades - every setting has strengths and costs.",
            "Because patterns aggregate over time, personality predicts real-life outcomes: work, health, relationships, and longevity.",
        ],
        "requirements": [
            "A clear distinction between personality (stable tendencies), mood (temporary states), and roles (situational performances).",
            "A vocabulary of trait words large enough to describe differences precisely - vague labels hide real patterns.",
            "A comparative frame: scores mean something only against the distribution of other people's scores.",
            "Honesty about limits: personality explains tendencies well and single moments poorly.",
        ],
        "standards": [
            STD_BIGFIVE,
            "Personality defined per Allport (1937) and the APA Dictionary: characteristic patterns of thought, emotion, and behavior.",
        ],
        "citations": [CIT_ALLPORT, CIT_APA, CIT_FFT],
        "sig_lens": (
            "The Signature reading hears personality as the instrument's "
            "base tuning: before any single note is played, the strings are "
            "already tightened to a pitch. Traits are those string tensions - "
            "set early, adjustable with work, and sounding through every "
            "piece the person plays."
        ),
    },
    {
        "key": "traits_states_types",
        "name": "Traits, States, and Types",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Three different words get mixed up constantly, so this record "
            "separates them. A trait is a stable tendency - being generally "
            "punctual, generally curious, generally calm. A state is a "
            "temporary condition - feeling punctuality-pressured today, "
            "curious about this one topic, calm this morning. States fluctuate "
            "by the hour; traits are the average around which states "
            "fluctuate. A type is a category - a named pattern that a person "
            "is sorted into, like the sixteen Myers-Briggs types or the nine "
            "Enneagram types. Traits are dimensions (everyone has a "
            "position on each one); types are boxes (each person is placed in "
            "one). Most modern personality science works with traits, "
            "because people vary by degrees rather than by kind - almost "
            "nobody is purely one type with no trace of the others. Types "
            "remain useful as shorthand and as conversation starters, and "
            "this database covers the major type systems honestly, including "
            "what each one can and cannot claim. The practical payoff: when "
            "someone acts out of character, ask whether you saw a state "
            "(the morning, the stress, the bad news) or the trait (the "
            "pattern across months). Confusing the two is the most common "
            "mistake in reading people."
        ),
        "how_it_works": (
            "Think of a trait as a climate and a state as the weather. The "
            "climate of a coastline is mild, but any given day can storm; "
            "the climate of a desert is dry, but any given day can rain. "
            "Judging climate from one day's weather is the error people make "
            "when they meet someone once and decide who they are. "
            "Psychologists separate the two by aggregation: many "
            "measurements across many days reveal the stable average, and "
            "that average is the trait. Types work differently - they draw "
            "boundaries on a continuous landscape. Extraversion is a smooth "
            "slope from very quiet to very outgoing, and a type system "
            "paints a line on the slope and calls one side 'introvert' and "
            "the other 'extravert'. The line is a convenience, not a cliff: "
            "people near the line share more with each other than with the "
            "extremes of their own side. Good type systems admit this and "
            "describe the center as its own pattern; weaker ones pretend the "
            "boxes are airtight."
        ),
        "key_points": [
            "Traits are stable averages; states are momentary fluctuations around that average - never judge a trait from a single state.",
            "Traits are dimensions (positions on a slope); types are categories (boxes drawn on the slope).",
            "Modern science favors traits because human variation is mostly by degree, not by kind.",
            "Type boundaries are conveniences: people near the line resemble each other more than they resemble their box's extremes.",
            "Aggregation - many observations over time - is what turns noisy daily behavior into a readable trait signal.",
        ],
        "requirements": [
            "A vocabulary that keeps trait, state, and type distinct in every description.",
            "Multiple observations before any trait claim about a real person.",
            "Type labels used as shorthand for patterns, never as verdicts on a whole person.",
            "Attention to the middle of every dimension, where most people actually live.",
        ],
        "standards": [
            STD_BIGFIVE,
            "State-trait distinction per the standard personality literature; type theory per Jung (1921) and Myers & Briggs (1980).",
        ],
        "citations": [CIT_APA, CIT_JUNG, CIT_MBTI],
        "sig_lens": (
            "The Signature reading separates the string's tuning (trait) "
            "from the note being played right now (state) from the named "
            "chord shape (type). Tune by the tuning, not by one plucked "
            "note; name the chord shape only as shorthand for the tuning "
            "beneath it."
        ),
    },
    {
        "key": "big_five_glance",
        "name": "The Big Five at a Glance",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The Big Five is the most researched model in personality "
            "psychology: five broad dimensions that capture the major ways "
            "people differ. Openness to Experience is imagination, curiosity, "
            "and appetite for novelty versus preference for the familiar. "
            "Conscientiousness is organization, discipline, and follow-through "
            "versus spontaneity and flexibility. Extraversion is energy from "
            "people and the outer world versus energy from solitude and the "
            "inner world. Agreeableness is warmth, cooperation, and trust "
            "versus skepticism and competitiveness. Neuroticism is the "
            "tendency to experience negative emotions - anxiety, sadness, "
            "irritability - versus emotional steadiness. The model was not "
            "invented by one theorist; it emerged independently from many "
            "researchers factor-analyzing trait words (Goldberg, 1990) and "
            "questionnaires (Costa & McCrae, 1992), and it replicates across "
            "languages and cultures. The five are mostly independent: knowing "
            "someone is highly extraverted tells you almost nothing about "
            "their conscientiousness. Together they form a compact map of a "
            "person - five numbers that sketch the territory, with the "
            "details filled in by the records that follow."
        ),
        "how_it_works": (
            "The Big Five works like five independent dials. Each dial runs "
            "from low to high with most people near the middle, and each "
            "dial predicts different things: conscientiousness predicts "
            "reliability and work outcomes; extraversion predicts social "
            "behavior and positive emotion; openness predicts creativity "
            "and interest in ideas; agreeableness predicts cooperation and "
            "relationship warmth; neuroticism predicts stress reactivity and "
            "vulnerability to low mood. Because the dials are independent, "
            "there are 32 rough combinations of high/low settings and "
            "effectively infinite fine gradations - which is why two people "
            "can share one trait and be utterly different people. "
            "Measurement is usually a questionnaire of 40 to 240 statements "
            "rated for agreement; the answers are averaged per domain and "
            "compared against population norms. The model's strength is "
            "empirical: decades of studies converge on these five as the "
            "broadest useful level of description. Its limit is breadth: a "
            "domain score summarizes a lot, and two people with the same "
            "score can arrive there through different facets - the subject "
            "of the facets record."
        ),
        "key_points": [
            "The five domains are Openness, Conscientiousness, Extraversion, Agreeableness, and Neuroticism - remembered as OCEAN.",
            "The model emerged from data across many researchers and replicates across languages and cultures.",
            "The domains are largely independent: each person is a unique combination of five separate settings.",
            "Each domain predicts different life outcomes, from work reliability to relationship warmth to stress reactivity.",
            "Domain scores are broad summaries; the facets record shows the finer structure inside each one.",
        ],
        "requirements": [
            "All five domains assessed together - a profile on one domain alone is not a personality picture.",
            "Norms for comparison: a raw score means nothing until placed against the population distribution.",
            "Independence respected: never infer one domain from another.",
            "Breadth acknowledged: domain scores summarize; they do not capture every nuance.",
        ],
        "standards": [STD_BIGFIVE],
        "citations": [CIT_NEO, CIT_GOLDBERG, CIT_BIGFIVE_TAX, CIT_FFT],
        "sig_lens": (
            "The Signature reading takes the five domains as the five "
            "master strings of the instrument. Every personality chord is "
            "voiced from these five strings; every later record in this "
            "database is a study of one string, one fret, or one way the "
            "five ring together."
        ),
    },
]

ENTRIES.extend([
    {
        "key": "openness",
        "name": "Openness to Experience",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Openness to Experience is the Big Five domain of imagination, "
            "curiosity, and appetite for novelty. High scorers are drawn to "
            "new ideas, art, unusual experiences, and abstract thinking; "
            "they enjoy questioning, exploring, and imagining alternatives. "
            "Low scorers prefer the familiar, the concrete, and the tried "
            "and true; they value tradition, practicality, and staying with "
            "what works. The NEO-PI-R breaks openness into six facets: "
            "fantasy, aesthetics, feelings, actions, ideas, and values "
            "(Costa & McCrae, 1992). Openness is the strongest personality "
            "correlate of creativity and intellectual engagement, and it "
            "predicts interests - artistic, investigative, and cultural - "
            "more than it predicts job performance. Strengths of high "
            "openness: originality, adaptability to new paradigms, rich "
            "inner life. Growth edges: can chase novelty past the point of "
            "usefulness, may undervalue routine maintenance. Strengths of "
            "low openness: reliability, respect for proven methods, steady "
            "focus. Growth edges: can resist needed change, may dismiss "
            "unfamiliar ideas before examining them. Working with high "
            "openness: offer variety, invite ideas, explain the why. Working "
            "with low openness: offer stability, respect experience, "
            "introduce change gradually with evidence."
        ),
        "how_it_works": (
            "Openness works as a dial on the mind's appetite for the "
            "unfamiliar. Turned up, attention is pulled toward what is new, "
            "ambiguous, or beautiful - the person seeks out unfamiliar "
            "music, reads widely, entertains strange hypotheses, and finds "
            "routine slightly suffocating. Turned down, attention rests on "
            "what is known and workable - the person perfects the familiar, "
            "trusts tested methods, and finds constant novelty slightly "
            "exhausting. The six facets show the dial's texture: a person "
            "can be high on ideas (loves abstract debate) but moderate on "
            "actions (keeps the same daily routine), which is why facet "
            "scores sharpen the picture. Openness interacts with intellect "
            "but is not the same as intelligence: a brilliant person can be "
            "closed (applying great ability to familiar problems) and a "
            "person of average ability can be open (exploring widely with "
            "modest tools). In groups, openness diversity matters: the open "
            "members generate options, the less open members test them "
            "against reality."
        ),
        "key_points": [
            "Openness spans imagination, curiosity, and appetite for novelty versus preference for the familiar and concrete.",
            "Its six facets are fantasy, aesthetics, feelings, actions, ideas, and values - a person can be high on some and moderate on others.",
            "It is the strongest personality correlate of creativity and intellectual and cultural interests.",
            "Openness is not intelligence: it describes appetite for ideas, not ability with them.",
            "High openness generates options; lower openness tests them against reality - teams need both.",
        ],
        "requirements": [
            "Facet-level detail when the domain score needs explaining - the average can hide a split profile.",
            "Separation of openness from ability: praise curiosity without implying brilliance, and vice versa.",
            "Strengths named for both ends: novelty-seeking and tradition-honoring are both assets in the right role.",
            "Change introduced to low-openness people gradually, with evidence and respect for what already works.",
        ],
        "standards": [STD_BIGFIVE, "Six facets per Costa & McCrae (1992): fantasy, aesthetics, feelings, actions, ideas, values."],
        "citations": [CIT_NEO, CIT_BIGFIVE_TAX],
        "sig_lens": (
            "The Signature reading hears openness as the string's "
            "willingness to be retuned: high openness retunes eagerly for "
            "every new piece, low openness holds its pitch and plays the "
            "repertoire flawlessly. Both are tunings; the music decides "
            "which the moment needs."
        ),
    },
    {
        "key": "conscientiousness",
        "name": "Conscientiousness: The Big Five Discipline Domain",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Conscientiousness is the Big Five domain of organization, "
            "discipline, and follow-through - and the single best personality "
            "predictor of work performance across occupations. High scorers "
            "are reliable, planful, careful, and persistent: they keep "
            "promises, meet deadlines, and finish what they start. Low "
            "scorers are spontaneous, flexible, and comfortable with "
            "looseness: they adapt quickly, improvise well, and dislike "
            "being boxed in by plans. The six facets are competence, order, "
            "dutifulness, achievement striving, self-discipline, and "
            "deliberation (Costa & McCrae, 1992). Conscientiousness also "
            "predicts health habits and longevity - careful people take "
            "better care of themselves. Strengths of high "
            "conscientiousness: trustworthiness, thoroughness, steady "
            "progress. Growth edges: perfectionism, rigidity, difficulty "
            "delegating. Strengths of low conscientiousness: spontaneity, "
            "creativity under pressure, tolerance for mess. Growth edges: "
            "unreliability, chronic lateness, unfinished commitments. "
            "Working with high conscientiousness: give clear expectations "
            "and deadlines, respect their systems. Working with low "
            "conscientiousness: keep requests small and concrete, build in "
            "checkpoints, celebrate finished work."
        ),
        "how_it_works": (
            "Conscientiousness works as the mind's project manager. Turned "
            "up, the manager is always on: goals get broken into steps, "
            "steps get scheduled, impulses get weighed against the plan, "
            "and the discomfort of an unfinished task nags until it is "
            "done. This is why high scorers look reliable from the outside - "
            "reliability is the visible exhaust of an internal system that "
            "hates loose ends. Turned down, the manager is on call rather "
            "than on duty: the person responds to the moment, follows "
            "energy and interest, and treats plans as suggestions. The "
            "facets reveal the machinery: achievement striving drives "
            "ambition, order drives tidiness, dutifulness drives "
            "promise-keeping, deliberation drives careful decision-making - "
            "and a person can be high on achievement but low on order (the "
            "brilliant messy achiever). Because it governs impulse control, "
            "conscientiousness shapes health, money, and work through "
            "thousands of small daily choices that compound over a "
            "lifetime."
        ),
        "key_points": [
            "Conscientiousness is the strongest personality predictor of work performance across occupations.",
            "Its six facets are competence, order, dutifulness, achievement striving, self-discipline, and deliberation.",
            "It predicts health habits and longevity through thousands of small daily choices.",
            "Facet splits explain the paradoxes: high achievement with low order, high dutifulness with low deliberation.",
            "It is the most trainable-feeling domain: systems and habits can scaffold it even where the trait is modest.",
        ],
        "requirements": [
            "Facet detail for any hiring or coaching use - the domain average alone misleads.",
            "Both ends honored: discipline and spontaneity each serve real functions.",
            "Expectations matched to the setting: high-conscientiousness people need clear targets; low-conscientiousness people need small concrete steps.",
            "Perfectionism watched as the shadow of high conscientiousness, not its virtue.",
        ],
        "standards": [STD_BIGFIVE, "Six facets per Costa & McCrae (1992): competence, order, dutifulness, achievement striving, self-discipline, deliberation."],
        "citations": [CIT_NEO, CIT_BIGFIVE_TAX, CIT_MATURITY],
        "sig_lens": (
            "The Signature reading treats conscientiousness as the "
            "discipline of the practice room: high scorers rehearse until "
            "the piece is clean, low scorers improvise brilliantly on "
            "stage. The Signature method borrows from both - the "
            "rehearsal ethic of the one, the live courage of the other."
        ),
    },
    {
        "key": "extraversion",
        "name": "Extraversion: The Big Five Energy Domain",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Extraversion is the Big Five domain of energy, sociability, and "
            "engagement with the outer world. High scorers are outgoing, "
            "talkative, and energized by people and activity; they tend to "
            "experience more positive emotion and to seek stimulation. Low "
            "scorers - introverts - are reserved, quiet, and energized by "
            "solitude and the inner world; they tend to think before "
            "speaking and to prefer depth over breadth in relationships. The "
            "six facets are warmth, gregariousness, assertiveness, activity, "
            "excitement seeking, and positive emotions (Costa & McCrae, "
            "1992). Extraversion is the most visible trait: it shows in the "
            "first minutes of meeting someone. Strengths of high "
            "extraversion: social ease, enthusiasm, leadership presence, "
            "resilience through connection. Growth edges: can dominate "
            "conversations, may act before reflecting, discomfort with "
            "solitude. Strengths of low extraversion: deep focus, careful "
            "listening, independent judgment. Growth edges: can be "
            "overlooked, may avoid needed visibility. Working with high "
            "extraversion: give the floor, decide out loud, provide social "
            "channels. Working with low extraversion: give advance notice, "
            "allow written input, respect recharge time."
        ),
        "how_it_works": (
            "Extraversion works as the dial on reward sensitivity to the "
            "outer world. Turned up, social interaction, novelty, and "
            "activity register as rewarding - the brain leans toward the "
            "room, the conversation, the next event, and solitude starts to "
            "feel like deprivation after a while. Turned down, the same "
            "inputs register as costly: the room is stimulating but "
            "draining, the conversation is pleasant but tiring, and "
            "solitude restores. This is why the common advice to introverts "
            "to 'just be more social' misses the mechanism - it is not "
            "fear, it is economics of energy. The facets show the dial is "
            "not one thing: assertiveness (social dominance) and warmth "
            "(friendliness) can split, producing the assertive introvert who "
            "leads quietly or the warm extravert who befriends everyone. "
            "Extraversion also colors emotion: high scorers report more "
            "frequent positive moods, which is part of why extraversion "
            "predicts well-being."
        ),
        "key_points": [
            "Extraversion is energy economics: extraverts gain energy from people and activity, introverts spend it there and recover alone.",
            "Its six facets are warmth, gregariousness, assertiveness, activity, excitement seeking, and positive emotions.",
            "It is the most visible trait, readable within minutes of meeting someone.",
            "Facets can split: assertiveness and warmth vary independently, producing quiet leaders and friendly loners.",
            "High extraversion predicts more frequent positive emotion, which feeds well-being.",
        ],
        "requirements": [
            "Energy respected as the mechanism - never treat introversion as a defect to fix.",
            "Facet splits honored: quiet does not mean unassertive, outgoing does not mean warm.",
            "Social settings designed with both ends in mind: airtime for extraverts, quiet channels for introverts.",
            "Visibility gaps watched: low-extraversion contributors need deliberate inclusion.",
        ],
        "standards": [STD_BIGFIVE, "Six facets per Costa & McCrae (1992): warmth, gregariousness, assertiveness, activity, excitement seeking, positive emotions."],
        "citations": [CIT_NEO, CIT_EYSENCK, CIT_BIGFIVE_TAX],
        "sig_lens": (
            "The Signature reading hears extraversion as the string's "
            "projection: high extraversion projects the chord outward to "
            "fill the hall, low extraversion plays it inward for the "
            "player's own ear. Both are music; the Signature method learns "
            "to project on purpose and to withdraw on purpose."
        ),
    },
    {
        "key": "agreeableness",
        "name": "Agreeableness: The Big Five Warmth Domain",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Agreeableness is the Big Five domain of warmth, cooperation, "
            "and concern for others. High scorers are trusting, kind, and "
            "accommodating; they default to giving the benefit of the doubt "
            "and prefer harmony to victory. Low scorers are skeptical, "
            "direct, and competitive; they default to questioning motives "
            "and prefer honest friction to false peace. The six facets are "
            "trust, straightforwardness, altruism, compliance, modesty, and "
            "tender-mindedness (Costa & McCrae, 1992). Agreeableness "
            "predicts relationship quality, teamwork, and prosocial "
            "behavior; low agreeableness, channeled well, predicts "
            "negotiating strength and willingness to deliver hard truths. "
            "Strengths of high agreeableness: loyalty, empathy, "
            "conflict-smoothing, generosity. Growth edges: difficulty saying "
            "no, conflict avoidance, being taken advantage of. Strengths of "
            "low agreeableness: candor, toughness in negotiation, "
            "independent judgment. Growth edges: abrasiveness, cynicism, "
            "damaged relationships. Working with high agreeableness: be "
            "kind, give them permission to disagree, protect them from "
            "overload. Working with low agreeableness: be direct, bring "
            "evidence, do not mistake bluntness for hostility."
        ),
        "how_it_works": (
            "Agreeableness works as the dial on the default stance toward "
            "other people. Turned up, the mind's first hypothesis about "
            "others is generous - they mean well, the misunderstanding is "
            "accidental, cooperation will work - and social friction feels "
            "physically uncomfortable, which motivates smoothing it over. "
            "Turned down, the first hypothesis is skeptical - what is the "
            "angle, where is the catch - and friction feels like "
            "information rather than pain, which motivates pressing the "
            "point. Neither stance is reality; each is a prior that gets "
            "updated by evidence, and the evidence of a lifetime teaches "
            "each person when their default serves them. The facets matter "
            "enormously here: trust (expecting good faith) and compliance "
            "(yielding in conflict) are separable, so a person can be "
            "trusting but unyielding - warm in motive, firm in position. "
            "That combination is the profile of the principled negotiator, "
            "and it is invisible to anyone who reads only the domain score."
        ),
        "key_points": [
            "Agreeableness sets the default hypothesis about other people: generous until proven otherwise, or skeptical until proven otherwise.",
            "Its six facets are trust, straightforwardness, altruism, compliance, modesty, and tender-mindedness.",
            "High agreeableness predicts relationship quality and teamwork; low agreeableness, well-channeled, predicts candor and negotiating strength.",
            "Trust and compliance separate: a person can be warm in motive and firm in position.",
            "The growth edge of high agreeableness is the unspoken no; of low agreeableness, the unnecessary wound.",
        ],
        "requirements": [
            "Facet splits read before judging: trusting is not the same as yielding.",
            "Directness from low-agreeableness people received as data, not hostility.",
            "High-agreeableness people explicitly invited to dissent - they will not volunteer it.",
            "Cynicism and people-pleasing both named as the failure modes of the two ends.",
        ],
        "standards": [STD_BIGFIVE, "Six facets per Costa & McCrae (1992): trust, straightforwardness, altruism, compliance, modesty, tender-mindedness."],
        "citations": [CIT_NEO, CIT_BIGFIVE_TAX],
        "sig_lens": (
            "The Signature reading hears agreeableness as the string's "
            "sympathy: high agreeableness resonates with every nearby "
            "string, low agreeableness holds its own pitch against the "
            "ensemble. The Signature player learns both - to resonate on "
            "purpose and to hold the line on purpose."
        ),
    },
    {
        "key": "neuroticism",
        "name": "Emotional Stability and Neuroticism",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Neuroticism is the Big Five domain of emotional reactivity - "
            "the tendency to experience anxiety, sadness, irritability, and "
            "self-consciousness. Its opposite pole is emotional stability: "
            "steadiness, calm under pressure, and quick recovery from "
            "upset. High scorers feel negative emotions more frequently and "
            "intensely and take longer to settle; low scorers stay even and "
            "bounce back fast. The six facets are anxiety, angry hostility, "
            "depression, self-consciousness, impulsiveness, and "
            "vulnerability to stress (Costa & McCrae, 1992). This is the "
            "domain most tied to well-being: high neuroticism predicts "
            "vulnerability to stress, low mood, and health complaints, while "
            "emotional stability predicts resilience. Strengths of high "
            "neuroticism, honestly named: vigilance, sensitivity to real "
            "risks, deep emotional range that feeds art and empathy. Growth "
            "edges: rumination, catastrophizing, stress that impairs "
            "decisions. Strengths of emotional stability: calm leadership, "
            "clear thinking under fire. Growth edges: can miss real warning "
            "signals, may seem unfeeling. Working with high neuroticism: "
            "reduce uncertainty, give reassurance with evidence, never "
            "mock the worry. This record is educational, not clinical - it "
            "describes normal-range variation, not disorders, and never "
            "diagnoses anyone."
        ),
        "how_it_works": (
            "Neuroticism works as the gain knob on the brain's threat and "
            "punishment systems. Turned up, the same setback rings louder "
            "and longer: a critical email replays for hours, a risk looks "
            "larger than its odds, the body stays mobilized after the "
            "danger passes. Turned down, the same setback registers briefly "
            "and fades: the email is answered, the risk is weighed "
            "coolly, the body stands down. The facets show the knob has "
            "channels: anxiety (worry about the future), angry hostility "
            "(irritable reactivity), depression (low mood and hopelessness "
            "as a trait tendency), self-consciousness (social unease), "
            "impulsiveness (trouble resisting urges under emotion), and "
            "vulnerability (feeling overwhelmed by stress). A person can be "
            "high on anxiety but low on angry hostility - the worrier who "
            "never snaps. Because the knob amplifies whatever passes "
            "through it, high neuroticism intensifies both suffering and "
            "sensitivity: the same reactivity that makes criticism sting "
            "makes beauty move and danger visible early."
        ),
        "key_points": [
            "Neuroticism is the gain knob on emotional reactivity; its opposite pole is emotional stability.",
            "Its six facets are anxiety, angry hostility, depression, self-consciousness, impulsiveness, and vulnerability to stress.",
            "It is the Big Five domain most tied to well-being, stress reactivity, and resilience.",
            "High reactivity amplifies everything: suffering, sensitivity to risk, and emotional depth.",
            "This is normal-range psychology: the record describes trait tendencies, never diagnoses, and never substitutes for professional help.",
        ],
        "requirements": [
            "Clinical humility: trait descriptions stay in the normal range; distress that impairs life deserves professional care, not a database entry.",
            "Both poles honored: vigilance is a real strength of the sensitive; calm is a real strength of the stable.",
            "Worry never mocked - reassurance works through evidence and reduced uncertainty, not dismissal.",
            "Facet channels separated: the worrier, the snapper, and the overwhelmed are different patterns.",
        ],
        "standards": [STD_BIGFIVE, "Six facets per Costa & McCrae (1992): anxiety, angry hostility, depression, self-consciousness, impulsiveness, vulnerability."],
        "citations": [CIT_NEO, CIT_EYSENCK, CIT_BIGFIVE_TAX],
        "sig_lens": (
            "The Signature reading treats neuroticism as the string's "
            "resonance: high gain rings long after the pluck, low gain "
            "damps quickly. The Signature method does not fight the "
            "resonance - it tunes the room: fewer surprises, clearer "
            "signals, and a deliberate cool-down ritual after the loud "
            "passages."
        ),
    },
    {
        "key": "hexaco",
        "name": "The HEXACO Model",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "HEXACO is the six-factor personality model developed by Ashton "
            "and Lee from lexical studies across languages: Honesty-Humility, "
            "Emotionality, eXtraversion, Agreeableness, Conscientiousness, "
            "and Openness to Experience. It resembles the Big Five but "
            "differs in two important ways. First, it adds Honesty-Humility "
            "as a sixth domain - sincerity, fairness, greed avoidance, and "
            "modesty - which the Big Five folds awkwardly into "
            "agreeableness. Second, it rotates the emotional and "
            "interpersonal domains: HEXACO Emotionality covers "
            "sentimentality, anxiety, and dependence (without the anger "
            "found in Big Five neuroticism), and HEXACO Agreeableness "
            "covers patience and gentleness (without the sentimentality). "
            "Cross-language research finds the six-factor structure in many "
            "languages, which is the empirical case for taking the sixth "
            "domain seriously. HEXACO's practical edge is in predicting "
            "integrity-related behavior: Honesty-Humility predicts "
            "workplace delinquency, exploitation, and unethical choices "
            "better than any Big Five domain. For most everyday purposes "
            "the Big Five suffices; when fairness, greed, and exploitation "
            "matter, HEXACO earns its place."
        ),
        "how_it_works": (
            "HEXACO works like the Big Five with a recalibrated compass. "
            "Imagine the Big Five map of personality, then notice that "
            "around the region labeled 'agreeableness' there is a distinct "
            "territory the map smudges: the difference between being "
            "cooperative and being honest, between yielding in a conflict "
            "and refusing to exploit. Lexical studies - analyzing which "
            "trait words cluster together in language after language - kept "
            "finding this sixth cluster, and Ashton and Lee gave it its "
            "name: Honesty-Humility. The rotation matters too: in HEXACO, "
            "the quickness to anger moves from the emotional domain to the "
            "agreeableness domain (as its opposite - patience), and "
            "sentimentality moves from agreeableness to emotionality. The "
            "result is cleaner predictions: want to know who cuts corners, "
            "who games expenses, who exploits trust? Honesty-Humility "
            "answers better than any Big Five scale. The two models are not "
            "rivals so much as different map projections - same territory, "
            "different distortions, chosen by what you need to navigate."
        ),
        "key_points": [
            "HEXACO adds a sixth domain - Honesty-Humility - covering sincerity, fairness, greed avoidance, and modesty.",
            "It rotates two domains: anger moves toward (low) agreeableness, sentimentality toward emotionality.",
            "The six-factor structure emerges from lexical studies across multiple languages.",
            "Honesty-Humility is the best personality predictor of integrity-related behavior and workplace delinquency.",
            "Big Five and HEXACO are different map projections of the same territory - choose by what you need to predict.",
        ],
        "requirements": [
            "The sixth domain named explicitly whenever integrity, fairness, or exploitation is the question.",
            "Both models' terminology kept straight - HEXACO agreeableness is not Big Five agreeableness.",
            "Cross-language evidence cited for the structure, not asserted from one culture.",
            "Model choice justified by the prediction task, not by habit.",
        ],
        "standards": [STD_HEXACO],
        "citations": [CIT_HEXACO, CIT_GOLDBERG],
        "sig_lens": (
            "The Signature reading prizes the sixth string: "
            "Honesty-Humility is the tuning peg of integrity, the part of "
            "the instrument that keeps every other string honest. A "
            "Signature profile is read with all six strings, because the "
            "chord is only as true as its most compromised note."
        ),
    },
    {
        "key": "honesty_humility",
        "name": "Honesty-Humility",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Honesty-Humility is HEXACO's sixth domain and one of the most "
            "practically important traits in the whole database: sincerity, "
            "fairness, greed avoidance, and modesty. High scorers are "
            "genuine, fair-minded, unimpressed by wealth and status, and "
            "uninterested in exploiting others; they follow rules even when "
            "no one is watching. Low scorers are strategic about honesty, "
            "comfortable bending rules for advantage, drawn to status and "
            "luxury, and willing to exploit - the profile most associated "
            "with manipulation, entitlement, and the darker personality "
            "patterns. Its four facets are sincerity, fairness, greed "
            "avoidance, and modesty (Ashton & Lee, 2007). This domain "
            "predicts workplace delinquency, cheating, and unethical "
            "decisions better than any Big Five scale. Strengths of high "
            "honesty-humility: trustworthiness, fairness, freedom from "
            "status games. Growth edges: can be exploited by the "
            "strategic, may undervalue legitimate self-promotion. The low "
            "end has no celebrated strengths - only risks to name honestly: "
            "manipulation, entitlement, exploitation - which is exactly why "
            "the domain matters for hiring, partnerships, and trust. "
            "Working with high scorers: be straight, share credit, keep "
            "promises. Around low scorers: verify, document, align "
            "incentives - trust but structure."
        ),
        "how_it_works": (
            "Honesty-Humility works as the dial on the willingness to "
            "exploit. Turned up, exploiting feels wrong from the inside - "
            "the person does not need surveillance to stay honest, because "
            "the dishonest option simply does not present itself as "
            "attractive. Turned down, exploiting feels like cleverness - "
            "rules look like obstacles for other people, status looks like "
            "the real game, and other people's trust looks like a resource "
            "to mine. The four facets show the machinery: sincerity "
            "governs genuineness versus flattery and deceit; fairness "
            "governs rule-following versus corner-cutting; greed avoidance "
            "governs desire for wealth and status; modesty governs "
            "entitlement versus humility. Because this dial predicts who "
            "cheats when they can get away with it, it is the trait that "
            "matters most where verification is expensive - partnerships, "
            "fiduciary roles, and positions of unsupervised power. The "
            "honest response to a low score is not moral panic but clear "
            "structure: incentives, audits, and transparency that make "
            "exploitation unprofitable."
        ),
        "key_points": [
            "Honesty-Humility covers sincerity, fairness, greed avoidance, and modesty - the integrity domain.",
            "It predicts cheating, workplace delinquency, and unethical choices better than any Big Five domain.",
            "High scorers stay honest without surveillance; low scorers treat rules as obstacles and trust as a resource.",
            "The four facets are sincerity, fairness, greed avoidance, and modesty.",
            "The practical answer to low honesty-humility in a role is structure: aligned incentives, verification, transparency.",
        ],
        "requirements": [
            "Integrity-relevant roles assessed on this domain explicitly, not inferred from agreeableness.",
            "Low scores met with structure and verification, never with moral theater.",
            "High scorers protected from exploitation and encouraged in legitimate self-advocacy.",
            "Facet detail used: a person can be sincere yet status-hungry, fair yet immodest.",
        ],
        "standards": [STD_HEXACO, "Four facets per Ashton & Lee (2007): sincerity, fairness, greed avoidance, modesty."],
        "citations": [CIT_HEXACO],
        "sig_lens": (
            "The Signature reading calls Honesty-Humility the covenant "
            "string: the Signature system is built on the oath between "
            "builder and work, and this string is where the oath lives. "
            "Every Signature profile is checked here first, because a "
            "brilliant chord voiced on a false string is still false."
        ),
    },
    {
        "key": "facets",
        "name": "Facets: The Six Faces of Every Domain",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "Every broad trait domain is a family of narrower facets, and "
            "the facets are where personality gets personal. The NEO-PI-R "
            "divides each Big Five domain into six facets - thirty in all "
            "(Costa & McCrae, 1992). Conscientiousness, for example, "
            "contains competence, order, dutifulness, achievement striving, "
            "self-discipline, and deliberation. Two people can share the "
            "same domain score through completely different facet patterns: "
            "one is conscientious through order and dutifulness (the "
            "reliable organizer), the other through achievement striving "
            "and competence (the driven achiever who lives in chaos). The "
            "domain score is the average; the facets are the explanation. "
            "Facets also predict more precisely: when a specific outcome "
            "matters - leadership emergence, health behavior, creative "
            "output - the right facet usually out-predicts the broad "
            "domain. The practical rule: use domains for the map and facets "
            "for the territory. If a domain score surprises you, or two "
            "people with the same score behave differently, the answer is "
            "always in the facets. HEXACO similarly divides its six domains "
            "into four facets each (Ashton & Lee, 2007)."
        ),
        "how_it_works": (
            "Facets work like the instruments in an orchestra section. The "
            "domain score is the section's overall volume - 'the strings "
            "are loud' - but the facets tell you whether that volume comes "
            "from violins, cellos, or both. Statistically, facets are "
            "clusters of items within a domain that hang together a little "
            "more tightly with each other than with the domain as a whole. "
            "This structure is why facet scores are more stable and more "
            "interpretable than any single questionnaire item, yet more "
            "specific than the domain. Reading a profile facet-first "
            "changes the advice: telling a low-conscientiousness person to "
            "'be more organized' fails if their actual gap is "
            "self-discipline (starting) rather than order (tidying) - the "
            "fix for starting is deadlines and accountability, the fix for "
            "tidying is systems and bins. Facet-level reading is the "
            "difference between a horoscope and a consultation."
        ),
        "key_points": [
            "Each Big Five domain divides into six facets (thirty total in the NEO-PI-R); each HEXACO domain into four.",
            "Identical domain scores can hide opposite facet patterns - the reliable organizer versus the chaotic achiever.",
            "Facets usually out-predict broad domains for specific outcomes like leadership, health, and creativity.",
            "The practical rule: domains for the map, facets for the territory.",
            "Good advice targets the facet, not the domain - starting problems and tidying problems need different fixes.",
        ],
        "requirements": [
            "Any serious profile reading done at facet level, not domain level alone.",
            "Facet splits named explicitly when two same-scored people differ.",
            "Advice matched to the specific facet gap, not the domain label.",
            "Facet names used from the published model, not invented paraphrases.",
        ],
        "standards": [STD_BIGFIVE, STD_HEXACO, "Thirty NEO-PI-R facets per Costa & McCrae (1992); twenty-four HEXACO facets per Ashton & Lee (2007)."],
        "citations": [CIT_NEO, CIT_HEXACO, CIT_BIGFIVE_TAX],
        "sig_lens": (
            "The Signature reading treats each domain as a string and "
            "each facet as a fret: the string sets the pitch family, the "
            "fret sets the exact note. Signature profiles are always read "
            "fret by fret, because the chord's true voicing lives in the "
            "frets, not the strings."
        ),
    },
    {
        "key": "measurement_sources",
        "name": "Self-Reports, Observer Ratings, and Bias",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "Personality is measured from three main vantage points, and "
            "each sees something the others miss. Self-reports - "
            "questionnaires where people rate their own typical behavior - "
            "are the workhorse: cheap, broad, and privileged, because only "
            "you know your inner life. Their weakness is bias: people shade "
            "answers toward looking good (social desirability), toward "
            "consistency, or toward the middle of every scale. Observer "
            "ratings - friends, partners, or colleagues rating you - see "
            "the outside that you cannot: how you actually come across. "
            "Self-observer agreement is moderate (around .40), higher for "
            "visible traits like extraversion, lower for inner ones like "
            "neuroticism. Behavioral measures - what people actually do in "
            "recorded situations - are the ground truth but expensive to "
            "collect. The honest approach triangulates: self-report for the "
            "inside, observers for the outside, behavior for the proof. Any "
            "single source lies a little; together they converge on the "
            "truth. Practical uses: 360-degree feedback at work, asking a "
            "partner 'how do I handle stress' before trusting your own "
            "answer, and discounting any personality quiz taken in a mood."
        ),
        "how_it_works": (
            "Each measurement source works like a different camera angle. "
            "The self-report is the selfie camera: intimate, always "
            "available, but flattering by default - people unconsciously "
            "pose, choosing the slightly braver, kinder, more organized "
            "version of themselves, and extreme honesty requires deliberate "
            "effort. The observer rating is the security camera: unposed "
            "and behavioral, but blind to motive - the observer sees that "
            "you left early, not that you left to care for a sick parent. "
            "Agreement between the two cameras runs around .40, which is "
            "both humbling and encouraging: humbling because your self-view "
            "is partly fiction, encouraging because two flawed angles still "
            "converge. The classic biases have names worth knowing: social "
            "desirability (looking good), acquiescence (agreeing with "
            "everything), extreme responding (only 1s and 5s), and the "
            "better-than-average effect (most people rating themselves "
            "above average on desirable traits - a mathematical "
            "impossibility that reveals the bias). Good instruments fight "
            "back with reverse-scored items, lie scales, and forced choices."
        ),
        "key_points": [
            "Three vantage points: self-reports (the inside), observer ratings (the outside), behavioral measures (the proof).",
            "Self-observer agreement is moderate, around .40 - higher for visible traits, lower for inner ones.",
            "Classic biases: social desirability, acquiescence, extreme responding, and the better-than-average effect.",
            "Good instruments defend with reverse-scored items, validity scales, and forced-choice formats.",
            "Triangulation is the honest method: never trust a single source, especially not a quiz taken in a mood.",
        ],
        "requirements": [
            "Source named for every personality claim: who rated whom, and how.",
            "Bias named and discounted, not ignored - especially social desirability in high-stakes settings.",
            "Observer input sought for visible traits; self input trusted more for inner experience.",
            "Mood and context noted at measurement time; a bad week is not a trait.",
        ],
        "standards": [
            "Self-observer agreement benchmarks per the personality assessment literature (Funder, 1999).",
            "Validity and bias controls per standard psychometric practice.",
        ],
        "citations": [CIT_BIGFIVE_TAX, CIT_APA],
        "sig_lens": (
            "The Signature reading tunes the instrument with three ears: "
            "the player's own hearing (self-report), the audience's "
            "hearing (observers), and the recording (behavior). The "
            "Signature profile is the mix of all three tracks - any single "
            "track is a demo, not the master."
        ),
    },
    {
        "key": "nature_nurture",
        "name": "Nature, Nurture, and the Sources of Traits",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "Where do personality traits come from? Twin and adoption "
            "studies give the clearest answer psychology has: roughly half "
            "of the variation in personality traits is genetic, and most of "
            "the rest is non-shared environment - the unique experiences, "
            "peers, accidents, and choices that differ even between siblings "
            "raised together. The surprise is what barely matters: shared "
            "family environment - the parenting style, the household, the "
            "neighborhood both siblings share - accounts for little of the "
            "adult differences in personality. Heritability around .40 to "
            ".60 does not mean traits are fixed: genes set the starting "
            "range and the tilt, while life writes the actual story within "
            "that range. It also does not mean parents do not matter - they "
            "matter enormously for values, knowledge, and opportunity, just "
            "less for the temperamental dials. The practical takeaways: stop "
            "blaming a single cause for who someone is; expect siblings to "
            "differ despite identical upbringings; and remember that "
            "'genetic influence' is an invitation to work with the grain "
            "of a person's nature, not an excuse to stop growing."
        ),
        "how_it_works": (
            "Behavioral genetics works by comparing resemblances. "
            "Identical twins share all their genes; fraternal twins share "
            "about half. If identical twins resemble each other more on a "
            "trait than fraternal twins do, genes are implicated - and the "
            "standard estimate, heritability, is roughly twice the "
            "difference between the two correlations. Across dozens of "
            "studies, personality traits land near .50: half the variation "
            "traces to genetic differences. Adoption studies confirm it: "
            "adopted children's personalities resemble their biological "
            "parents more than their adoptive parents. The remaining "
            "variation splits into shared environment (near zero for adult "
            "personality - the family you share with your siblings) and "
            "non-shared environment (large - everything that happened to "
            "you and not to them). Think of genes as the instrument's wood "
            "and build: the wood sets the possible tone, but the player, "
            "the practice, and the years decide the music. Heritability "
            "describes variation in a population, not destiny in a person - "
            "a trait can be highly heritable and still change, as the "
            "lifespan records will show."
        ),
        "key_points": [
            "About half of personality variation is genetic; most of the rest is non-shared environment.",
            "Shared family environment accounts for surprisingly little of adult personality differences.",
            "Heritability is about population variation, not personal destiny - heritable traits still change.",
            "Parents matter enormously for values, knowledge, and opportunity, less for temperamental dials.",
            "The practical moral: work with the grain of a person's nature instead of fighting it or blaming one cause.",
        ],
        "requirements": [
            "Heritability stated as a population statistic, never as a personal fixed percentage.",
            "Both twin and adoption evidence acknowledged - one method alone is not the case.",
            "Shared vs non-shared environment distinguished precisely.",
            "No fatalism: genetic influence framed as the starting tilt, not the final score.",
        ],
        "standards": [
            "Behavioral genetics estimates per the twin/adoption literature (Bouchard & Loehlin, 2001).",
        ],
        "citations": [CIT_FFT, CIT_APA],
        "sig_lens": (
            "The Signature reading honors the wood and the player both: "
            "the grain of the wood (nature) decides which tones come "
            "easily, the years of playing (nurture) decide which tones "
            "actually sound. The Signature method never fights the grain - "
            "it carves with it."
        ),
    },
])

ENTRIES.extend([
    {
        "key": "mbti",
        "name": "The Sixteen Types of Jung and Myers-Briggs",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The Myers-Briggs Type Indicator (MBTI), built on Jung's "
            "Psychological Types (1921) by Isabel Myers and Katharine "
            "Briggs, sorts people into sixteen types from four preference "
            "pairs: Extraversion or Introversion (where you focus energy), "
            "Sensing or Intuition (how you take in information), Thinking "
            "or Feeling (how you decide), Judging or Perceiving (how you "
            "organize the outer world). Each type is a four-letter code - "
            "INTJ, ESFP, and the fourteen others - with a characteristic "
            "pattern of strengths: INTJs architect systems, ESFPs light up "
            "rooms, INFJs counsel, ESTJs organize. The honest account "
            "includes the limits, and this database gives them straight: "
            "test-retest reliability is modest (many people get a different "
            "type on retake), the dichotomies cut continuous dimensions at "
            "arbitrary lines, and the types predict job performance weakly "
            "compared with trait measures. What the MBTI does well is give "
            "people a language for differences: teams use it to understand "
            "why the INTJ wants the plan and the ENFP wants the "
            "possibilities, and that conversation has real value even where "
            "the psychometrics are thin. Use it as a mirror for reflection "
            "and a vocabulary for differences - never as a hiring filter, "
            "a verdict, or a cage."
        ),
        "how_it_works": (
            "The MBTI works by forced choice: for each of the four pairs, "
            "questions push you to one side or the other, and your four "
            "choices combine into one of sixteen codes (2 x 2 x 2 x 2 = "
            "16). Beneath the codes sits Jung's deeper machinery, the "
            "cognitive functions: each type leads with a dominant function "
            "(for example, introverted intuition in the INTJ) supported by "
            "an auxiliary, with the weaker functions trailing. In practice "
            "people recognize themselves in the type portraits because the "
            "portraits are well-written and the Barnum effect is real - "
            "vague-enough descriptions feel personal. The scientific "
            "critique is specific: the bimodal distributions the theory "
            "predicts do not appear (scores pile up near the middle, not at "
            "the poles), and cutting a bell curve in half discards "
            "information. The practical synthesis: keep the vocabulary and "
            "the self-reflection, drop the boxes. 'I lean introverted and "
            "decide by values' is useful; 'I am an INFP so I cannot lead "
            "meetings' is the theory misused."
        ),
        "key_points": [
            "Sixteen types from four preference pairs: E/I, S/N, T/F, J/P - 2 x 2 x 2 x 2 = 16.",
            "Built on Jung's Psychological Types (1921) by Myers and Briggs; cognitive functions sit beneath the four-letter codes.",
            "Honest limits: modest retest reliability, arbitrary cut points on continuous dimensions, weak job-performance prediction.",
            "Genuine value: a shared vocabulary for differences and a mirror for self-reflection.",
            "Use as language and mirror - never as a hiring filter, verdict, or cage.",
        ],
        "requirements": [
            "The four dichotomies named and defined in the model's own terms.",
            "Limits stated plainly alongside the uses - no hype, no debunking theater.",
            "Type descriptions framed as patterns with variation, not destinies.",
            "No employment decisions made on type; the evidence does not support it.",
        ],
        "standards": [STD_TYPES, "Jung's functions per Psychological Types (1921); MBTI per Myers & Briggs (1980)."],
        "citations": [CIT_JUNG, CIT_MBTI],
        "sig_lens": (
            "The Signature reading treats the sixteen types as sixteen "
            "named chord shapes: useful shorthand for voicings players "
            "recognize, but every real performance bends the shape. Learn "
            "the shapes, then play the music - never let the shape name "
            "decide what your hands may do."
        ),
    },
    {
        "key": "intro_ambivert",
        "name": "Introversion, Extraversion, and Ambiversion in Daily Life",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Beyond the textbook definition, this record is the field guide "
            "to living on the extraversion dimension. Introverts recharge "
            "in solitude, think before speaking, prefer one deep "
            "conversation to ten light ones, and do their best work with "
            "uninterrupted focus. Extraverts recharge with people, think "
            "out loud, work the room naturally, and do their best work "
            "with buzz and collaboration. Ambiverts - the large middle, "
            "where most people actually score - flex both ways: social when "
            "it matters, solitary when it counts, often the most adaptable "
            "of all. Daily-life implications are concrete. Meetings: "
            "introverts need the agenda in advance and a written channel; "
            "extraverts need airtime and live discussion. Social battery: "
            "an introvert's evening out costs energy that must be repaid "
            "in quiet; an extravert's quiet weekend costs energy repaid in "
            "people. Conflict: introverts withdraw to process, extraverts "
            "talk to process - each mistakes the other's method for "
            "avoidance or aggression. Leadership: quiet leaders lead "
            "through depth and listening; expressive leaders through energy "
            "and presence. Neither is the 'correct' personality; each is a "
            "correct personality with a user's manual."
        ),
        "how_it_works": (
            "The dimension works through stimulation economics, and daily "
            "life is where the accounting shows. Every social situation "
            "makes simultaneous deposits and withdrawals: novelty and "
            "people deposit for the extravert and withdraw for the "
            "introvert; quiet and solitude deposit for the introvert and "
            "withdraw for the extravert. The ambivert runs a balanced "
            "account, spending and earning in both currencies, which is why "
            "the middle of the dimension is so functional - it is not "
            "indecision, it is range. Problems arise at the translation "
            "layer: the introvert's silence in a meeting reads as "
            "disagreement, the extravert's thinking-aloud reads as a final "
            "decision, the introvert's need to leave the party reads as "
            "rejection, the extravert's need for the after-party reads as "
            "neediness. All four readings are translation errors. The fix "
            "is explicit protocols: agendas in advance, written channels "
            "alongside verbal ones, stated recharge needs treated as "
            "logistics rather than insults."
        ),
        "key_points": [
            "Introverts recharge alone and think before speaking; extraverts recharge with people and think out loud; ambiverts flex both ways.",
            "Most people score near the middle - ambiversion is the common condition, not a failure to pick a side.",
            "Conflict styles diverge: introverts withdraw to process, extraverts talk to process.",
            "Translation errors cause most friction: silence misread as disagreement, thinking-aloud misread as deciding.",
            "Explicit protocols - agendas, written channels, stated recharge needs - dissolve most introvert-extravert friction.",
        ],
        "requirements": [
            "The middle of the dimension treated as its own valid pattern, not a watered-down version of the poles.",
            "Energy economics, not moral judgment: neither pole pathologized.",
            "Concrete protocols for meetings, social plans, and conflict - not just descriptions.",
            "Leadership honored in both styles: depth and presence are different instruments, not better and worse.",
        ],
        "standards": [STD_BIGFIVE, "Extraversion facets per Costa & McCrae (1992)."],
        "citations": [CIT_NEO, CIT_EYSENCK, CIT_BIGFIVE_TAX],
        "sig_lens": (
            "The Signature reading scores daily life like a set list: "
            "loud numbers and quiet numbers both belong, and the wise "
            "player paces them. Know your instrument's projection, schedule "
            "the quiet passages deliberately, and never apologize for the "
            "volume your strings were built to play."
        ),
    },
    {
        "key": "enneagram",
        "name": "The Enneagram: Nine Motivational Patterns",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The Enneagram describes nine personality patterns organized "
            "around core motivations rather than surface behaviors. The "
            "nine: the Reformer (driven by integrity and correctness), the "
            "Helper (driven by love and being needed), the Achiever (driven "
            "by success and admiration), the Individualist (driven by "
            "authenticity and depth), the Investigator (driven by "
            "understanding and competence), the Loyalist (driven by security "
            "and guidance), the Enthusiast (driven by joy and freedom), the "
            "Challenger (driven by strength and autonomy), and the "
            "Peacemaker (driven by harmony and wholeness). Each type has a "
            "wing - the neighboring type that flavors it - and lines of "
            "stress and growth connecting it to two other types, mapping "
            "how the pattern shifts under pressure and in health. The "
            "modern system was developed by Oscar Ichazo and Claudio "
            "Naranjo and popularized by Don Riso and Russ Hudson. The "
            "honest account: the Enneagram's empirical base is thinner than "
            "the Big Five's, and typing by test alone is unreliable. Its "
            "strength is motivational depth - it asks why a behavior "
            "happens, not just what happens - which makes it a powerful "
            "mirror for self-understanding and growth work, used as "
            "reflection rather than measurement."
        ),
        "how_it_works": (
            "The Enneagram works by naming the hidden engine. Two people "
            "can both work late: the Achiever works late to succeed, the "
            "Loyalist works late to feel secure, the Helper works late to "
            "be indispensable. Same behavior, three engines - and the "
            "Enneagram claims the engine matters more than the behavior for "
            "predicting what the person will do next. Each type's engine is "
            "a core desire tangled with a core fear: the Reformer desires "
            "goodness and fears corruption, the Enthusiast desires freedom "
            "and fears pain, the Challenger desires autonomy and fears "
            "being controlled. The wings add flavor (a 7 with an 8 wing is "
            "bolder than a 7 with a 6 wing), and the stress/growth lines "
            "map movement: under strain the patterns contract toward their "
            "stress point, in health they expand toward their growth "
            "point. Because it is a wisdom tradition more than a "
            "measurement system, it works best as structured "
            "self-inquiry - reading the types, recognizing the engine, and "
            "doing the growth work the system prescribes."
        ),
        "key_points": [
            "Nine types organized by core motivation: what drives the pattern, not just what the pattern looks like.",
            "Same behavior can run on different engines - the Enneagram reads the engine.",
            "Wings flavor each type; stress and growth lines map how patterns shift under pressure and in health.",
            "Empirical base is thinner than trait models; typing by test alone is unreliable.",
            "Greatest strength is as a mirror for self-understanding and deliberate growth, used as reflection rather than measurement.",
        ],
        "requirements": [
            "Core desire and core fear named for each type - motivation, not just behavior.",
            "Wings and stress/growth lines included; a type without its movement is half the system.",
            "Empirical limits stated honestly; the system presented as wisdom tradition and mirror.",
            "Growth direction given for each pattern, not just the description.",
        ],
        "standards": [STD_TYPES, "Nine-type framework per Riso & Hudson (1996); origins in Ichazo and Naranjo."],
        "citations": [CIT_ENNEAGRAM],
        "sig_lens": (
            "The Signature reading hears the nine types as nine reasons "
            "to pick up the instrument: the Reformer plays to get it "
            "right, the Enthusiast plays for the joy of sound, the "
            "Challenger plays to be heard. Tune the reason and the playing "
            "follows - the Signature growth work starts at the engine, "
            "not the fingers."
        ),
    },
    {
        "key": "disc",
        "name": "DISC: Four Behavioral Styles",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "DISC is a four-style behavioral model widely used in workplaces: "
            "Dominance (direct, results-driven, decisive), Influence "
            "(enthusiastic, persuasive, people-driven), Steadiness (patient, "
            "loyal, team-driven), and Conscientiousness (careful, precise, "
            "quality-driven). It comes from William Marston's Emotions of "
            "Normal People (1928), developed into assessments by later "
            "practitioners. DISC describes observable behavior - how a "
            "person tends to act - rather than inner traits or motivations, "
            "which is both its limit and its workplace value: managers can "
            "see style and adapt to it. High D: give the bottom line, offer "
            "options, move fast. High I: be warm, recognize publicly, keep "
            "energy up. High S: be patient, provide stability, avoid "
            "surprises. High C: be precise, provide data, allow analysis "
            "time. The honest account: DISC is a practical communication "
            "tool with modest psychometric foundations - useful for "
            "adapting your approach to colleagues, not for deep "
            "personality assessment or hiring decisions. Everyone blends "
            "all four styles; the profile shows the emphasis, and style "
            "shifts with role and setting."
        ),
        "how_it_works": (
            "DISC works on two axes: outgoing versus reserved, and "
            "task-focused versus people-focused. The four quadrants are the "
            "four styles: outgoing plus task-focused is Dominance; outgoing "
            "plus people-focused is Influence; reserved plus people-focused "
            "is Steadiness; reserved plus task-focused is Conscientiousness. "
            "Assessment places a person in the quadrants by asking about "
            "behavioral preferences, producing a profile of relative "
            "emphasis rather than a single box. In practice it functions as "
            "a translation device: once you can read a colleague's style, "
            "you can adjust pace, detail level, and decision process to "
            "match. The D wants the decision; the C wants the data behind "
            "the decision; the I wants to discuss the decision with the "
            "team; the S wants to know the decision will not disrupt the "
            "team. None of these wants is wrong; each is a different "
            "definition of a good process. The model breaks when it is "
            "treated as destiny - style is adaptable, and the same person "
            "leads with D in a crisis and S with their family."
        ),
        "key_points": [
            "Four styles: Dominance, Influence, Steadiness, Conscientiousness - describing observable behavior.",
            "Two axes generate the styles: outgoing/reserved by task-focused/people-focused.",
            "Everyone blends all four; the profile shows emphasis, and emphasis shifts with role and setting.",
            "Workplace value is adaptation: adjust pace, detail, and process to the other person's style.",
            "Practical tool with modest psychometrics - for communication, not for hiring or deep assessment.",
        ],
        "requirements": [
            "Behavioral focus kept clear: DISC describes how people act, not why or how they feel inside.",
            "Adaptation advice given for each style - the model's whole point is adjusting your approach.",
            "Blends and context-shifts acknowledged; no one is a pure single style everywhere.",
            "Hiring and clinical uses excluded; the evidence does not support them.",
        ],
        "standards": [STD_TYPES, "DISC framework originating in Marston (1928)."],
        "citations": [CIT_DISC],
        "sig_lens": (
            "The Signature reading treats the four styles as four ways "
            "of handling the instrument on stage: the D drives the tempo, "
            "the I works the crowd, the S holds the groove, the C tunes "
            "between songs. A Signature ensemble learns to hear all four "
            "and give each its passage."
        ),
    },
    {
        "key": "temperaments",
        "name": "The Four Temperaments",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The four temperaments are the oldest personality system in "
            "the West, originating with Hippocrates and developed by "
            "Galen: the Sanguine (warm, lively, sociable, optimistic), the "
            "Choleric (bold, driven, quick to act and to anger), the "
            "Melancholic (thoughtful, sensitive, perfectionistic, deep), "
            "and the Phlegmatic (calm, steady, easygoing, consistent). "
            "Galen tied them to bodily humors - blood, yellow bile, black "
            "bile, phlegm - a physiology long discarded, but the behavioral "
            "patterns survived because they keep matching observation. "
            "Modern readers will recognize the Big Five in them: Sanguine "
            "maps toward extraversion, Choleric toward low agreeableness "
            "with high assertiveness, Melancholic toward neuroticism with "
            "high conscientiousness, Phlegmatic toward emotional stability "
            "with low extraversion. The system's value today is narrative: "
            "it gives memorable characters for patterns people already "
            "see, and it reminds us that personality description is "
            "ancient, not invented. Its limit is precision - four boxes "
            "cannot carry what five or six dimensions do. Use the "
            "temperaments as stories and entry points; use the trait "
            "models when precision matters."
        ),
        "how_it_works": (
            "The temperaments work on two ancient axes: warm versus cool "
            "(emotional reactivity) and moist versus dry (which Galen "
            "associated with flexibility versus rigidity). Warm and "
            "flexible is Sanguine; warm and rigid is Choleric; cool and "
            "rigid is Melancholic; cool and flexible is Phlegmatic. Forget "
            "the humors; keep the geometry - it is an early discovery that "
            "personality varies along a few broad dimensions, the same "
            "discovery factor analysis would remake two thousand years "
            "later. In practice the temperaments function as archetypes: "
            "the Sanguine friend who lights up gatherings, the Choleric "
            "colleague who charges at obstacles, the Melancholic artist who "
            "feels everything deeply, the Phlegmatic anchor who never "
            "panics. Archetypes teach fast because stories stick; they "
            "mislead when the story replaces the person. The honest modern "
            "use is pedagogical: meet the temperaments first as characters, "
            "then graduate to the trait dimensions that explain why the "
            "characters work."
        ),
        "key_points": [
            "The oldest Western personality system: Sanguine, Choleric, Melancholic, Phlegmatic (Hippocrates, Galen).",
            "The humoral physiology is discarded; the behavioral patterns survived because they match observation.",
            "Modern trait models echo the temperaments: each maps onto a region of Big Five space.",
            "Value is narrative and pedagogical: memorable characters that teach pattern recognition fast.",
            "Limit is precision: four boxes cannot carry what dimensional models do - graduate to traits when precision matters.",
        ],
        "requirements": [
            "Historical framing honest: ancient origins, discarded physiology, surviving patterns.",
            "Mapping to modern trait space shown, not just asserted.",
            "Archetypes used as entry points and stories, never as final assessments.",
            "The graduation path named: temperaments first, trait dimensions next.",
        ],
        "standards": [STD_TYPES, "Classical four-temperament framework (Hippocrates; Galen)."],
        "citations": [CIT_EYSENCK, CIT_BIGFIVE_TAX],
        "sig_lens": (
            "The Signature reading honors the four old voices: the "
            "Sanguine sparkle on the high strings, the Choleric attack, "
            "the Melancholic depth on the low strings, the Phlegmatic "
            "steady rhythm underneath. Every Signature player carries all "
            "four voices; mastery is knowing which voice the passage "
            "needs."
        ),
    },
])

ENTRIES.extend([
    {
        "key": "sixteen_pf",
        "name": "The Sixteen Personality Factors",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The 16PF (Sixteen Personality Factor Questionnaire), developed "
            "by Raymond Cattell, measures sixteen primary personality "
            "factors - a finer-grained map than the Big Five, built for "
            "applied settings like career counseling and clinical "
            "screening. The sixteen: Warmth, Reasoning, Emotional "
            "Stability, Dominance, Liveliness, Rule-Consciousness, Social "
            "Boldness, Sensitivity, Vigilance, Abstractedness, Privateness, "
            "Apprehension, Openness to Change, Self-Reliance, Perfectionism, "
            "and Tension. Scores are reported as stens - standard ten "
            "scores from 1 to 10, with 5.5 as the population average - "
            "which makes profiles easy to read at a glance. The sixteen "
            "factors roll up into five global factors that closely resemble "
            "the Big Five, so the 16PF can be read at two resolutions: the "
            "fine grain for detail, the global factors for the big "
            "picture. Strengths: depth, a long research history, and "
            "genuinely useful career and counseling applications. Limits: "
            "complexity - sixteen scales demand trained interpretation - "
            "and the proprietary instrument. The lesson for this database: "
            "resolution is a choice. Five factors for the map, sixteen for "
            "the survey, thirty facets for the close-up."
        ),
        "how_it_works": (
            "The 16PF works by factor-analyzing deeper than the Big Five. "
            "Where the Big Five stops at five broad domains, Cattell's "
            "analysis kept splitting until sixteen stable primary factors "
            "remained - the level where the clusters were narrow enough to "
            "describe specific tendencies but broad enough to measure "
            "reliably. Each factor is scored on the sten scale: raw scores "
            "convert to 1-10, with 4-7 as the average band, 1-3 as low, "
            "8-10 as high. A profile of sixteen stens is read as a "
            "landscape - peaks and valleys, not single numbers - and "
            "trained interpreters look at factor combinations: high "
            "Dominance with high Social Boldness reads as natural "
            "leadership; high Vigilance with high Apprehension reads as "
            "guarded worry. The five global factors (Extraversion, Anxiety, "
            "Tough-Mindedness, Independence, Self-Control) then summarize "
            "the landscape for quick communication. This two-resolution "
            "design is the 16PF's enduring contribution: measure fine, "
            "summarize broad, and let the question choose the resolution."
        ),
        "key_points": [
            "Sixteen primary factors from Cattell's deeper factor analysis - a finer-grained map than the Big Five.",
            "Scores report as stens (1-10, average 5.5): profiles read as landscapes of peaks and valleys.",
            "The sixteen roll up into five global factors resembling the Big Five - two resolutions, one instrument.",
            "Strengths: depth, research history, career and counseling applications; limits: complexity and trained interpretation needed.",
            "The general lesson: resolution is a choice - five factors for the map, sixteen for the survey, thirty facets for the close-up.",
        ],
        "requirements": [
            "Factor names used from the published 16PF, not paraphrased.",
            "Sten scale explained with its bands (1-3 low, 4-7 average, 8-10 high).",
            "Profiles read as combinations and landscapes, never as isolated single scores.",
            "Trained interpretation acknowledged as the requirement for applied use.",
        ],
        "standards": ["16PF primary and global factors per Cattell (1949; 5th ed. 1993)."],
        "citations": [CIT_16PF, CIT_BIGFIVE_TAX],
        "sig_lens": (
            "The Signature reading admires the sixteen-fret neck: more "
            "frets, finer notes. The Signature player learns the full "
            "fretboard but solos with the five strings - detail in the "
            "practice room, clarity on the stage."
        ),
    },
    {
        "key": "full_profile",
        "name": "How Traits Combine: Reading a Full Profile",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "A personality is not five separate scores - it is the "
            "combination, and combinations have emergent meanings that no "
            "single trait carries. High extraversion with high "
            "agreeableness reads as the warm connector; the same "
            "extraversion with low agreeableness reads as the competitive "
            "challenger. High conscientiousness with high neuroticism is "
            "the anxious perfectionist - reliable but suffering; high "
            "conscientiousness with emotional stability is the calm "
            "professional - reliable and at ease. High openness with low "
            "conscientiousness is the brilliant improviser; high openness "
            "with high conscientiousness is the systematic innovator. "
            "Reading profiles means reading interactions: look first at "
            "the highest and lowest scores (the peaks define the person), "
            "then at the pairs (the peaks modify each other), then at the "
            "middle scores (the quiet background). The common errors: "
            "adding traits like ingredients instead of letting them "
            "interact, and overweighting the most dramatic score while "
            "ignoring the moderating ones. A profile is a chord, not a "
            "playlist - the notes sound together, and the meaning is in "
            "the harmony."
        ),
        "how_it_works": (
            "Profile reading works in three passes. First pass: find the "
            "extremes. Scores in the top and bottom fifths are the "
            "person's signature - the traits everyone who knows them would "
            "name. Second pass: pair the extremes. Each extreme is modified "
            "by the others: high assertiveness (extraversion facet) plus "
            "high trust (agreeableness facet) produces the encouraging "
            "leader; the same assertiveness plus low trust produces the "
            "intimidating one. The modifier is often more informative than "
            "the trait. Third pass: read the middle. Scores near the "
            "average are not 'no information' - they are flexibility. A "
            "mid-range extravert can work a room or work alone; a "
            "mid-range conscientious person can plan or improvise. In "
            "combination, profiles also reveal compensations: low "
            "self-discipline compensated by high dutifulness (keeps "
            "promises to others even when self-promises slip), high anxiety "
            "compensated by high deliberation (worries, then plans). The "
            "art is holding the whole pattern lightly: a profile suggests "
            "tendencies, and the person in front of you is always more "
            "than the pattern."
        ),
        "key_points": [
            "Combinations have emergent meanings no single trait carries - the chord, not the playlist.",
            "Read in three passes: extremes first (the signature), pairs second (the modifiers), middle scores third (the flexibility).",
            "Modifiers often matter more than traits: assertiveness plus trust versus assertiveness plus suspicion are different people.",
            "Middle scores mean flexibility, not absence of personality.",
            "Profiles reveal compensations: strengths in one facet covering gaps in another.",
        ],
        "requirements": [
            "Three-pass reading performed in order; no jumping to a single dramatic score.",
            "Interactions named explicitly - every interpretation states which traits modify which.",
            "Compensations and flexibility read alongside extremes.",
            "The person held as larger than the pattern; profiles suggest, they do not sentence.",
        ],
        "standards": [STD_BIGFIVE, "Profile interpretation per standard NEO-PI-R clinical and counseling practice (Costa & McCrae, 1992)."],
        "citations": [CIT_NEO, CIT_BIGFIVE_TAX],
        "sig_lens": (
            "The Signature reading is profile reading by ear: the "
            "Signature player does not hear five separate strings but one "
            "chord, and names the chord's quality - bright, tense, warm, "
            "driving. Train the ear on combinations and single notes stop "
            "fooling you."
        ),
    },
    {
        "key": "at_work",
        "name": "Personality at Work",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Personality shapes work life through fit: the match between a "
            "person's traits and a role's demands. Conscientiousness "
            "predicts performance across nearly all jobs - reliability is "
            "universally useful. Extraversion predicts performance in "
            "sales, management, and other people-intensive roles, and "
            "predicts leadership emergence: extraverts get noticed. "
            "Openness predicts success in creative, investigative, and "
            "change-heavy roles. Agreeableness predicts teamwork and "
            "service quality, and low agreeableness predicts negotiating "
            "strength. Emotional stability predicts performance under "
            "pressure everywhere. But fit cuts both ways: the highly open "
            "innovator withers in rigid routine; the highly conscientious "
            "perfectionist burns out in chaos; the introverted analyst "
            "thrives in deep work and drowns in constant meetings. Smart "
            "organizations hire for the traits the role actually needs, "
            "design roles around real human patterns, and manage to the "
            "person: give the conscientious clear targets, the extravert "
            "airtime, the open mind problems worth solving, the agreeable "
            "team protection from overload, the sensitive steady "
            "predictability. Personality is not a hiring verdict - it is a "
            "management manual."
        ),
        "how_it_works": (
            "Work fit works through demands and supplies. Every role makes "
            "demands: this one demands constant social energy, that one "
            "demands meticulous follow-through, the other demands comfort "
            "with ambiguity. Every person supplies traits: energy for "
            "people, discipline for detail, appetite for novelty. Fit is the "
            "match between the two lists, and misfit is expensive in both "
            "directions - the person suffers and the work suffers. The "
            "research pattern is consistent: conscientiousness helps "
            "almost everywhere (the universal supply), while the other "
            "traits help where the role demands them (the specific "
            "supplies). Two management moves follow. First, select and "
            "place honestly: put the people-demanding roles on people who "
            "gain energy from people. Second, manage the misfit you cannot "
            "hire away: the introvert in the people role needs recovery "
            "time designed in; the low-conscientiousness creative needs "
            "scaffolding, not scolding. Personality at work is not about "
            "labeling employees - it is about designing work humans can "
            "actually do well."
        ),
        "key_points": [
            "Conscientiousness predicts performance across nearly all jobs; the other traits predict where the role demands them.",
            "Fit is the match between role demands and trait supplies; misfit is expensive for both person and work.",
            "Extraversion predicts leadership emergence; openness predicts creative and change-heavy roles; agreeableness predicts teamwork.",
            "Two management moves: place honestly for the role, and scaffold the misfit you cannot hire away.",
            "Personality is a management manual, not a hiring verdict - design work humans can do well.",
        ],
        "requirements": [
            "Role demands listed before any trait is invoked - traits answer demands, not the other way around.",
            "Conscientiousness honored as the universal predictor without making it the only one that matters.",
            "Misfit addressed with design (recovery time, scaffolding), not with blame.",
            "No trait used as a verdict on a person's worth or potential.",
        ],
        "standards": [STD_BIGFIVE, "Work-performance relations per Barrick & Mount (1991) meta-analysis."],
        "citations": [CIT_BIGFIVE_TAX, CIT_NEO],
        "sig_lens": (
            "The Signature reading casts work as repertoire: every role "
            "is a piece with technical demands, and the Signature manager "
            "is the arranger - matching players to pieces, transposing "
            "passages that do not fit, and never blaming the violin for "
            "not being a drum."
        ),
    },
    {
        "key": "relationships",
        "name": "Personality in Relationships",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Personality runs every relationship from underneath. "
            "Similarity attracts: partners and close friends tend to match "
            "on values, openness, and conscientiousness - shared rhythms "
            "make daily life smooth. But complementarity has its place: "
            "one partner's calm steadies the other's intensity, one "
            "friend's planning covers the other's spontaneity. "
            "Agreeableness is the relationship trait: high scorers build "
            "warmth and repair ruptures; low scorers need explicit care to "
            "keep friction from eroding goodwill. Neuroticism is the risk "
            "trait: high reactivity strains bonds unless both people "
            "understand the pattern - the sensitive partner needs "
            "reassurance with evidence, the stable partner needs to know "
            "reassurance is maintenance, not weakness. Extraversion sets "
            "the social thermostat: mismatched social batteries are a top "
            "couples' friction, solved by negotiation rather than "
            "conversion. The deepest practical skill is translating: your "
            "partner's withdrawal is processing, not rejection; their "
            "talking is processing, not attack; their need for plans is "
            "care, not control. Personality does not decide whether love "
            "lasts - how people handle their differences does."
        ),
        "how_it_works": (
            "Relationships work as two personality systems coupled "
            "together, and coupling creates dynamics neither person has "
            "alone. The pursuer-distancer pattern is the classic: one "
            "partner's anxiety about the bond drives pursuit (more "
            "contact, more reassurance-seeking), which triggers the "
            "other's need for space (withdrawal), which confirms the "
            "first partner's fear - a loop powered by trait differences, "
            "not by lack of love. Breaking the loop requires seeing it: "
            "naming the pattern as the enemy instead of each other. "
            "Similarity smooths the coupling - matched conscientiousness "
            "means never fighting about the dishes' schedule; matched "
            "openness means shared curiosity. Complementarity stabilizes "
            "it - the planner and the improviser cover more of life "
            "together than two planners. The master skill is trait "
            "translation in real time: hearing the criticism inside the "
            "bluntness (low agreeableness, high honesty), the care inside "
            "the planning (conscientiousness), the love inside the "
            "reassurance-seeking (neuroticism asking for safety)."
        ),
        "key_points": [
            "Similarity on values, openness, and conscientiousness smooths daily life; complementarity can stabilize it.",
            "Agreeableness builds and repairs bonds; neuroticism strains them unless the pattern is understood.",
            "Mismatched social batteries are a top friction - negotiated, never converted.",
            "Couple dynamics like pursuer-distancer are trait-powered loops, broken by naming the pattern.",
            "The master skill is translation: hearing the care inside the other person's trait expression.",
        ],
        "requirements": [
            "Both similarity and complementarity honored - neither romanticized alone.",
            "Loops named as the enemy, not the partner.",
            "Reassurance framed as maintenance for the sensitive, not weakness.",
            "Translation practiced explicitly: state what you hear beneath the trait.",
        ],
        "standards": [STD_BIGFIVE, "Assortative mating and relationship correlates per the personality and close-relationships literature."],
        "citations": [CIT_BIGFIVE_TAX, CIT_FFT],
        "sig_lens": (
            "The Signature reading hears relationships as duets: two "
            "instruments with different tunings learning one piece. The "
            "Signature duet is not played by making both instruments "
            "identical - it is played by learning each other's tuning "
            "and arranging the piece so both sound their best."
        ),
    },
    {
        "key": "reliability_validity",
        "name": "Measuring Personality: Reliability and Validity",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "A personality test is only as good as its measurement, and "
            "measurement has two questions. Reliability asks: does the "
            "test give consistent results? A reliable scale gives similar "
            "scores on retake (test-retest reliability) and its items hang "
            "together (internal consistency, measured by Cronbach's alpha - "
            ".70 is acceptable, .80 is good, .90 is excellent). Validity "
            "asks: does the test measure what it claims? A valid "
            "extraversion scale correlates with sociable behavior, peer "
            "ratings of sociability, and number of friends - not just with "
            "itself. The validity hierarchy matters: face validity (looks "
            "right) is the weakest; convergent validity (agrees with other "
            "measures of the same trait), discriminant validity (disagrees "
            "with measures of different traits), and predictive validity "
            "(forecasts real outcomes) are the real tests. Practical "
            "guidance: distrust any quiz that cannot show reliability "
            "numbers; distrust any type test with low retest stability; "
            "trust instruments with published manuals, norms, and validity "
            "studies - the NEO-PI-R, the 16PF, the HEXACO-PI-R. A test "
            "without psychometrics is entertainment, and entertainment is "
            "fine as long as it is labeled."
        ),
        "how_it_works": (
            "Reliability works like a scale that weighs you the same each "
            "morning: internal consistency checks that the items agree "
            "with each other (if you endorse 'I love parties' you should "
            "also endorse 'I start conversations'), and test-retest checks "
            "that the score survives the weeks between measurements. "
            "Cronbach's alpha quantifies the item agreement from the "
            "average inter-item correlation and the item count - more "
            "coherent items, higher alpha. Validity works like checking "
            "the scale against a known weight: convergent evidence piles "
            "up when the scale correlates with peer ratings, behavioral "
            "counts, and other scales of the same trait; discriminant "
            "evidence when it does not correlate with unrelated traits; "
            "predictive evidence when it forecasts outcomes measured "
            "later - job performance, relationship stability, health. The "
            "two can split: a test can be reliable but invalid (consistently "
            "measuring the wrong thing, like a scale always five pounds "
            "heavy) but never valid without reliability (noise cannot "
            "correlate with truth). This is why the serious instruments "
            "publish manuals thick with numbers, and why a ten-question "
            "internet quiz cannot carry weight no matter how fun it is."
        ),
        "key_points": [
            "Reliability is consistency (retest stability, internal consistency); validity is truth (measuring what is claimed).",
            "Cronbach's alpha benchmarks: .70 acceptable, .80 good, .90 excellent.",
            "The validity hierarchy: convergent, discriminant, and predictive evidence outweigh face validity.",
            "A test can be reliable but invalid; it can never be valid without reliability.",
            "Trust instruments with published manuals, norms, and validity studies; label the rest entertainment.",
        ],
        "requirements": [
            "Reliability numbers demanded before any test is taken seriously.",
            "Validity evidence specified by kind - convergent, discriminant, predictive - not just claimed.",
            "Internet quizzes without psychometrics labeled entertainment, not assessment.",
            "Retest stability checked for any type system before its categories are trusted.",
        ],
        "standards": ["Psychometric standards per the Standards for Educational and Psychological Testing (AERA/APA/NCME)."],
        "citations": [CIT_NEO, CIT_16PF, CIT_HEXACO],
        "sig_lens": (
            "The Signature reading tunes by measurement: the Signature "
            "player checks the tuner (reliability) before trusting the "
            "ear (validity), and distrusts any tuner that gives a "
            "different reading every time it is clipped on. Tune the "
            "tools, then tune the instrument."
        ),
    },
    {
        "key": "person_situation",
        "name": "The Person-Situation Debate",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "In 1968 Walter Mischel dropped a bomb on personality "
            "psychology: he reviewed the evidence and found that trait "
            "scores predicted single behaviors at only about .30 - the "
            "'personality coefficient.' If traits are real, he asked, why "
            "do they predict any one act so weakly? The field spent "
            "decades answering, and the answer is the modern synthesis. "
            "First, aggregation: traits predict aggregated behavior "
            "beautifully - one act is noisy, but the average of many acts "
            "is the trait speaking clearly. Second, the situation was "
            "underestimated: strong situations (a funeral, a job "
            "interview) constrain everyone alike, while weak situations "
            "(a free evening) let personality bloom. Third, people choose "
            "their situations: extraverts join clubs, the conscientious "
            "choose structured jobs - traits shape the situations that "
            "then shape behavior. Mischel himself helped build the "
            "resolution: his cognitive-affective processing system (CAPS, "
            "1995) describes personality as stable if-then patterns - if "
            "criticized, then withdraws; if praised, then shines. The "
            "debate's legacy is wisdom: never predict a single act from "
            "a trait, never ignore the situation, and look for the "
            "person's stable patterns across their chosen situations."
        ),
        "how_it_works": (
            "The debate works as a lesson in signal and noise. A single "
            "behavior is mostly noise: the extravert is quiet at this "
            "particular dinner because of a headache, a worry, a seating "
            "chart. Correlating that one dinner with the trait score "
            "yields the famous .30 - real but modest. But average fifty "
            "dinners and the headache nights cancel out, leaving the "
            "signal: the extravert's average sociability across dinners "
            "correlates strongly with the trait. This is the Spearman-Brown "
            "logic: aggregation kills noise. The situation side works "
            "through constraint: personality predicts best where the "
            "situation is silent - unstructured time, free choice, "
            "private behavior. And the deepest resolution is that people "
            "are not randomly assigned to situations: the trait selects "
            "the niche, the niche rewards the trait, and the loop "
            "strengthens both. The if-then formulation captures the "
            "stability that survives all this: the person is not 'always "
            "aggressive' but 'aggressive when provoked by peers, gentle "
            "with family' - a stable signature written in conditionals."
        ),
        "key_points": [
            "Mischel (1968) found traits predict single acts at only ~.30 - the personality coefficient that started the debate.",
            "Aggregation resolves it: traits predict averaged behavior strongly; single acts are mostly noise.",
            "Strong situations constrain everyone; weak situations let personality show; people also choose their situations.",
            "The CAPS resolution (1995): personality as stable if-then patterns, not context-free consistency.",
            "The legacy: never predict one act from a trait, never ignore the situation, look for patterns across chosen situations.",
        ],
        "requirements": [
            "Single-act predictions from traits refused as a matter of method.",
            "Situation strength assessed before any behavioral prediction.",
            "Situation selection (niches people choose) included in every explanation.",
            "If-then patterns used where simple trait labels fail.",
        ],
        "standards": ["Person-situation synthesis per Mischel (1968) and Mischel & Shoda (1995)."],
        "citations": [CIT_MISCHEL, CIT_CAPS, CIT_FFT],
        "sig_lens": (
            "The Signature reading knows the room shapes the music: the "
            "same string sounds different in a cathedral and a closet. "
            "The Signature player studies both the instrument and the "
            "venue - and writes the set list as if-then wisdom: if this "
            "room, then this voicing."
        ),
    },
    {
        "key": "team_chemistry",
        "name": "Team Chemistry: Traits in Groups",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Teams are personality systems, and their chemistry follows "
            "patterns. Conscientiousness helps teams almost universally: "
            "a team's average conscientiousness predicts its performance, "
            "and one highly unreliable member can drag the whole group - "
            "the 'bad apple' effect is real. Extraversion is double-edged: "
            "extraverts energize and lead, but too many competing for "
            "airtime creates noise; the best teams balance voices. "
            "Agreeableness smooths collaboration but a team of only "
            "high-agreeableness members avoids necessary conflict - every "
            "team needs someone willing to say the uncomfortable true "
            "thing. Openness diversity fuels innovation: the open members "
            "generate options while the less open members reality-test "
            "them. Emotional stability steadies the group under pressure; "
            "a highly reactive member can set the emotional temperature "
            "for everyone. Practical team design: cover the functions "
            "(driving, generating, organizing, harmonizing, challenging), "
            "watch the minimum more than the average (the lowest "
            "conscientiousness often matters most), build explicit norms "
            "so style differences do not become personal, and give "
            "airtime protocols so the quietest expert is heard."
        ),
        "how_it_works": (
            "Team chemistry works through composition and norms. "
            "Composition is who is in the room: the blend of traits sets "
            "the team's default behaviors - its energy level, its "
            "tolerance for conflict, its discipline, its creativity. "
            "Research finds the mean matters less than the minimum for "
            "some traits: team performance tracks the least "
            "conscientious member because unreliability is contagious - "
            "missed handoffs cascade. Norms are the team's operating "
            "system, and they can amplify or mute the composition: a norm "
            "of written pre-reads mutes extraversion's airtime advantage; "
            "a norm of explicit dissent mutes agreeableness's "
            "conflict-avoidance. The skilled team builder therefore works "
            "both levers: compose for coverage (every function filled, no "
            "fatal gap) and norm for fairness (protocols that let every "
            "style contribute). Diversity of traits beats uniformity: the "
            "all-extravert team is loud and shallow, the "
            "all-conscientious team is thorough and slow, the mixed team - "
            "well-normed - gets both energy and depth."
        ),
        "key_points": [
            "Team conscientiousness predicts performance; the minimum often matters more than the average - unreliability cascades.",
            "Extraversion energizes but needs airtime balance; agreeableness smooths but needs a licensed dissenter.",
            "Openness diversity fuels innovation: generators plus reality-testers.",
            "Norms are the operating system: good protocols mute style advantages and let every trait contribute.",
            "Compose for coverage, norm for fairness - trait diversity with good norms beats uniformity.",
        ],
        "requirements": [
            "Functions covered explicitly: driving, generating, organizing, harmonizing, challenging.",
            "The minimum watched alongside the average, especially for conscientiousness.",
            "Protocols designed so the quietest expert is heard and dissent is safe.",
            "Style differences treated as design inputs, never as personal failings.",
        ],
        "standards": [STD_BIGFIVE, "Team composition effects per the work-team personality literature (Bell, 2007)."],
        "citations": [CIT_BIGFIVE_TAX, CIT_NEO],
        "sig_lens": (
            "The Signature reading assembles the ensemble deliberately: "
            "no band of five lead guitars, no orchestra of only cellos. "
            "The Signature arranger covers every chair, writes parts that "
            "fit each player's tuning, and sets the house rules so every "
            "instrument is heard in the mix."
        ),
    },
])

ENTRIES.extend([
    {
        "key": "stability_change",
        "name": "Trait Stability and Change Across the Lifespan",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Personality is both stable and changeable, and the paradox "
            "dissolves once you separate two kinds of stability. "
            "Rank-order stability - whether the most extraverted teen "
            "becomes the most extraverted adult - is high: correlations "
            "across decades run .50 to .70, meaning people's relative "
            "positions hold remarkably well. Mean-level change - whether "
            "the average person changes - is real and patterned: "
            "conscientiousness and agreeableness tend to rise with age, "
            "neuroticism tends to fall, openness rises through young "
            "adulthood then gently declines, extraversion's social "
            "vitality softens while its assertiveness holds. The biggest "
            "changes happen in young adulthood, when roles - work, "
            "partnership, parenthood - press personality into new shapes. "
            "The practical meaning: your traits are not a life sentence, "
            "but they are a strong tendency. Deliberate change is "
            "possible - the growth record shows how - and it works with "
            "the grain: years of acting a trait etch it deeper, which is "
            "why the roles you choose become, slowly, who you are."
        ),
        "how_it_works": (
            "The two stabilities work like a marathon's leaderboard. "
            "Rank-order stability means the runners keep their relative "
            "order: the leader at mile five is probably still leading at "
            "mile twenty, even though everyone has moved forward - that is "
            "the .50 to .70 correlation across decades. Mean-level change "
            "means the whole pack moves: the average runner gets more "
            "conscientious, more agreeable, less neurotic with the miles. "
            "Both are true at once because they measure different things. "
            "Change happens through two engines: roles and repetition. "
            "Roles press from the outside - the job demands punctuality, "
            "the child demands patience, and years of meeting the demand "
            "etch the trait. Repetition presses from the inside - "
            "deliberately practicing a behavior (starting conversations, "
            "keeping a schedule) lays down the habit, and habits "
            "consolidate into traits. This is why personality change is "
            "slow but real: no one becomes a different person in a month, "
            "but a decade of chosen roles and practiced behaviors moves "
            "the dials measurably."
        ),
        "key_points": [
            "Rank-order stability is high (.50-.70 across decades): relative positions hold.",
            "Mean-level change is real and patterned: conscientiousness and agreeableness rise, neuroticism falls with age.",
            "The biggest changes come in young adulthood, when new roles press personality into new shapes.",
            "Two engines of change: roles that demand new behavior, and repetition that turns behavior into habit into trait.",
            "Traits are a strong tendency, not a life sentence - deliberate change works with the grain, slowly.",
        ],
        "requirements": [
            "The two stabilities distinguished in every claim - rank-order versus mean-level.",
            "Change described as slow and real, never instant and never impossible.",
            "Role and repetition named as the mechanisms, not willpower alone.",
            "Young adulthood identified as the window of maximum plasticity.",
        ],
        "standards": ["Lifespan trait development per Roberts & Mroczek (2008) and Roberts et al. (2006)."],
        "citations": [CIT_MATURITY, CIT_FFT],
        "sig_lens": (
            "The Signature reading treats the lifespan as the long "
            "seasoning of the wood: the instrument's voice deepens and "
            "steadies with the years, and the player who chooses good "
            "roles and repeats good passages literally becomes a better "
            "instrument. Time is the final luthier."
        ),
    },
    {
        "key": "maturity_principle",
        "name": "Personality Development: The Maturity Principle",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The maturity principle is the best-replicated finding in "
            "personality development: as people age, they tend to become "
            "more conscientious, more agreeable, and less neurotic - in "
            "plain words, more responsible, kinder, and calmer. The "
            "pattern appears across cultures and cohorts, strongest from "
            "the twenties through the forties. The leading explanation is "
            "social investment: adult roles - committed work, partnership, "
            "parenthood, community - reward reliability, cooperation, and "
            "steadiness, and people adapt to what their lives reward. "
            "Investing deeply in age-graded roles predicts the maturity "
            "gains; drifting without commitment predicts stagnation. "
            "There are honest exceptions: trauma, chronic stress, and "
            "adversity can raise neuroticism; not everyone matures on "
            "schedule. But the principle reframes aging: the typical "
            "trajectory is not decline but ripening. Practically, it "
            "means the twenties are the high-leverage decade - the roles "
            "you invest in then write the personality you inhabit later - "
            "and it means judging a young person's traits as unfinished "
            "is not charity but accuracy."
        ),
        "how_it_works": (
            "The maturity principle works through reward shaping. Adult "
            "life is a long operant chamber: the workplace pays the "
            "reliable and fires the flaky, partnerships reward the kind "
            "and punish the cruel, parenting demands patience daily. Over "
            "years, the rewarded behaviors become automatic - the "
            "conscientious choice stops feeling like effort and starts "
            "feeling like self. This is the corresponsive principle: the "
            "traits that lead you into roles are deepened by those roles - "
            "the responsible young adult takes the demanding job, and the "
            "demanding job makes them more responsible. Investment is the "
            "key variable: merely occupying a role changes little, but "
            "psychologically investing in it - caring about the work, the "
            "partner, the child - predicts the gains. The mechanism is "
            "behavioral repetition consolidated into disposition: act "
            "patient a thousand times because the toddler requires it, and "
            "patience becomes, measurably, more you."
        ),
        "key_points": [
            "The maturity principle: with age, people tend toward higher conscientiousness, higher agreeableness, lower neuroticism.",
            "The pattern replicates across cultures and cohorts, strongest from the twenties through the forties.",
            "Mechanism is social investment: adult roles reward reliability, cooperation, and steadiness.",
            "Investment, not mere occupancy: caring about the role predicts the gains; drifting predicts stagnation.",
            "The corresponsive principle: traits lead into roles, and roles deepen the traits.",
        ],
        "requirements": [
            "The principle stated as a tendency with documented exceptions, not a law.",
            "Social investment named as the leading explanation with its evidence.",
            "Investment distinguished from occupancy - caring is the active ingredient.",
            "Young people's traits framed as unfinished, accurately rather than charitably.",
        ],
        "standards": ["Maturity and social investment principles per Roberts & Mroczek (2008); Roberts et al. (2005)."],
        "citations": [CIT_MATURITY],
        "sig_lens": (
            "The Signature reading calls the maturity principle the "
            "seasoning of the player: the years of showing up, keeping "
            "promises, and steadying others tune the instrument truer. "
            "The Signature path invests on purpose - choosing the roles "
            "that demand the virtues and letting the years do the tuning."
        ),
    },
    {
        "key": "decision_making",
        "name": "Personality and Decision-Making",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Personality tilts every decision before the facts arrive. "
            "High openness decides by exploring: generating options, "
            "questioning assumptions, comfortable with novel solutions - "
            "and sometimes over-exploring past the point of deciding. High "
            "conscientiousness decides by process: gathering information, "
            "weighing deliberately, deciding once - and sometimes "
            "over-deliberating past the window. High extraversion decides "
            "out loud and fast, energized by action; introversion decides "
            "quietly and carefully, needing processing time. High "
            "agreeableness decides by consensus, protecting relationships - "
            "and may avoid the necessary hard call. High neuroticism "
            "decides under the amplification of worry: risks look larger, "
            "losses loom bigger, and reassurance-seeking can masquerade as "
            "due diligence. The practical art is decision hygiene matched "
            "to the decider: pre-commit to criteria before options seduce "
            "(for the open), set decision deadlines (for the "
            "conscientious), require a written dissent (for the "
            "agreeable), separate the worry from the odds (for the "
            "reactive), and give the quiet a channel before the vote (for "
            "the introverted). Know your tilt, then design against its "
            "failure mode."
        ),
        "how_it_works": (
            "Decision tilts work through what each trait treats as "
            "salient. The open mind spotlights novelty - the unusual "
            "option glows. The conscientious mind spotlights completeness "
            "- the missing datum itches. The extraverted mind spotlights "
            "momentum - deciding feels like progress. The agreeable mind "
            "spotlights harmony - the option nobody hates glows. The "
            "reactive mind spotlights threat - the downside scenario plays "
            "on loop. None of these spotlights is the truth; each is a "
            "trait-powered attention bias, and good decisions come from "
            "knowing which spotlight is on. The hygiene follows directly: "
            "write the criteria before seeing options (blinds the novelty "
            "spotlight), set a decide-by date (caps the completeness "
            "itch), require written pre-mortems (gives threat-spotting a "
            "legitimate channel), poll quietly before discussing aloud "
            "(protects the introverted and the agreeable from the loudest "
            "voice). Groups get a bonus tilt - the composition effects in "
            "the team record - which is why the best decision processes "
            "are designed, not improvised."
        ),
        "key_points": [
            "Each trait spotlights different information: novelty, completeness, momentum, harmony, threat.",
            "Spotlights are attention biases, not truth - good decisions start by naming which light is on.",
            "Decision hygiene is matched to the tilt: criteria first, deadlines, written dissent, quiet polling.",
            "Know your tilt, then design against its failure mode - over-exploring, over-deliberating, over-harmonizing.",
            "Group decisions need designed processes because composition adds its own tilts.",
        ],
        "requirements": [
            "Each trait's decision spotlight named concretely with its failure mode.",
            "Hygiene prescribed per tilt, not generic 'decide better' advice.",
            "Worry separated from odds explicitly for high-neuroticism deciders.",
            "Quiet and agreeable voices protected by process before any vote.",
        ],
        "standards": [STD_BIGFIVE, "Trait-decision relations per the judgment and decision-making personality literature."],
        "citations": [CIT_BIGFIVE_TAX, CIT_FFT],
        "sig_lens": (
            "The Signature reading treats decisions as choosing the next "
            "piece: the Signature player knows their ear's biases - the "
            "pull toward the flashy piece, the stall on the safe one - "
            "and writes the set list by criteria before the crowd's "
            "noise. Play the program, not the impulse."
        ),
    },
    {
        "key": "reading_ethically",
        "name": "Reading Others Ethically",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "The power to read personality carries obligations, and this "
            "record states them. First, consent and purpose: read people "
            "to understand and serve them - to manage better, love "
            "better, collaborate better - never to manipulate, expose, or "
            "control. Second, humility: your read is a hypothesis, not a "
            "verdict; hold it lightly, update it with evidence, and prefer "
            "asking over assuming. Third, no secret dossiers: never use "
            "personality knowledge to ambush someone with insights about "
            "them they did not invite ('you are just being your "
            "Enneagram 8'). Fourth, no determinism: a trait pattern "
            "suggests tendencies; the person chooses, grows, and "
            "surprises - treat every read as describing the past, not "
            "dictating the future. Fifth, privacy: personality inferences "
            "are personal data; do not share your reads about someone "
            "with third parties. Sixth, power awareness: reading "
            "downward (boss reading employee, parent reading child) "
            "demands extra care, because the power gap turns casual "
            "labels into cages. The ethical reader's motto: use "
            "personality to enlarge people, never to shrink them."
        ),
        "how_it_works": (
            "Ethical reading works by keeping three questions live. 'What "
            "is my purpose?' filters every inference: understanding that "
            "serves the other person passes; understanding that serves "
            "your leverage over them fails. 'How sure am I, really?' "
            "enforces the base rates: your one-observation read is mostly "
            "noise, the aggregated pattern is signal, and the honest "
            "reader says which one they have. 'Would I say this to their "
            "face, kindly?' tests the inference: if the read only works as "
            "a weapon behind their back, it is not insight but gossip "
            "with jargon. In practice this means leading with curiosity "
            "('help me understand how you decide'), offering reads as "
            "gifts not verdicts ('I notice you seem to recharge alone - "
            "does that fit?'), and dropping the read the moment the "
            "person corrects it - they are the authority on themselves. "
            "The deepest ethic is asymmetry: grant others the complexity "
            "you grant yourself. You know your own contradictions; extend "
            "the same interior vastness to everyone you read."
        ),
        "key_points": [
            "Read to understand and serve, never to manipulate, expose, or control.",
            "Every read is a hypothesis: hold lightly, update with evidence, prefer asking over assuming.",
            "No secret dossiers and no ambush insights - offer reads as invited gifts, not verdicts.",
            "Traits describe tendencies, never dictate futures; the person is the authority on themselves.",
            "Grant others the interior complexity you grant yourself - enlarge people, never shrink them.",
        ],
        "requirements": [
            "Purpose checked before every inference: service, not leverage.",
            "Confidence calibrated: one observation is noise, patterns are signal - say which you have.",
            "Reads offered kindly and droppable the moment the person corrects them.",
            "Power gaps acknowledged: reading downward demands extra care against labeling.",
        ],
        "standards": ["Ethical principles consistent with APA Ethical Principles of Psychologists regarding assessment and privacy."],
        "citations": [CIT_APA, CIT_BIGFIVE_TAX],
        "sig_lens": (
            "The Signature reading is bound by the player's oath: the "
            "trained ear is for making music with people, not for "
            "exposing them. Hear the tuning to serve the ensemble - and "
            "the moment hearing becomes leverage, put the instrument "
            "down."
        ),
    },
    {
        "key": "leadership",
        "name": "Personality and Leadership",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Personality predicts who becomes a leader and partly how "
            "they lead. Extraversion is the strongest predictor of "
            "leadership emergence - extraverts get noticed, speak up, and "
            "project confidence - though not of leadership effectiveness, "
            "where the advantage narrows. Conscientiousness predicts "
            "effective leadership through reliability and organization. "
            "Openness predicts visionary and change leadership. "
            "Agreeableness is nuanced: warmth builds trust and "
            "followership, but the most effective leaders pair it with "
            "the firmness to make hard calls. Emotional stability "
            "predicts calm under fire - followers take their emotional "
            "cues from the leader. Beyond traits, styles matter: "
            "transformational leaders inspire through vision and "
            "individual attention; transactional leaders through clear "
            "exchanges; servant leaders through developing people. The "
            "practical synthesis: there is no one leadership "
            "personality - quiet, systematic introverts lead superbly, "
            "as do charismatic extraverts - but every leader must cover "
            "the functions: direction, energy, trust, and steadiness. "
            "Know your profile, staff your gaps, and lead from your "
            "genuine strengths rather than performing someone else's."
        ),
        "how_it_works": (
            "Leadership emergence works through visibility: groups "
            "promote the people they notice, and extraversion, "
            "assertiveness, and social boldness manufacture notice - the "
            "babble effect, where the most talkative are rated most "
            "leaderlike regardless of content. Effectiveness works "
            "through different machinery: trust (agreeableness plus "
            "honesty-humility), competence signals (conscientiousness), "
            "direction (openness to vision, conscientiousness to plan), "
            "and emotional contagion (the leader's steadiness regulates "
            "the group's nervous system). This split explains the "
            "familiar disappointment of the charismatic incompetent: "
            "emergence selected for visibility, effectiveness requires "
            "substance. The style layer sits on top: transformational "
            "behaviors - idealized influence, inspirational motivation, "
            "intellectual stimulation, individualized consideration - can "
            "be learned and predict effectiveness beyond traits. So the "
            "full picture is traits select the leader, behaviors make "
            "the leader, and the wise organization selects for substance "
            "while training the behaviors."
        ),
        "key_points": [
            "Extraversion predicts leadership emergence most strongly; effectiveness depends more on conscientiousness, openness, and stability.",
            "The babble effect: groups mistake talkativeness for leaderlikeness - select for substance, not visibility.",
            "Agreeableness builds trust but must pair with firmness; emotional stability regulates the whole group.",
            "Transformational behaviors can be learned and add effectiveness beyond traits.",
            "No single leadership personality: cover the functions (direction, energy, trust, steadiness) from genuine strengths.",
        ],
        "requirements": [
            "Emergence and effectiveness distinguished in every leadership claim.",
            "Visibility biases named and corrected in selection.",
            "Style behaviors taught as learnable skills, not treated as fixed traits.",
            "Leaders directed to staff their gaps and lead from genuine strengths.",
        ],
        "standards": [STD_BIGFIVE, "Trait-leadership relations per Judge et al. (2002) meta-analysis."],
        "citations": [CIT_BIGFIVE_TAX, CIT_NEO],
        "sig_lens": (
            "The Signature reading treats leadership as first chair: the "
            "first chair is heard most, so the Signature leader tunes "
            "with extra care - steadiness for the section's nerves, "
            "warmth for its trust, vision for its direction. Lead the "
            "ensemble by deserving the chair, not by taking it."
        ),
    },
    {
        "key": "culture",
        "name": "Personality Across Cultures",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Personality is both universal and cultural. The Big Five "
            "structure replicates across dozens of cultures and languages "
            "(McCrae et al., 2005) - the same five families of traits "
            "emerge whether the trait words are English, Chinese, or "
            "Turkish. But culture shapes expression and ideals: "
            "individualist cultures prize and reward extraversion and "
            "openness more openly; collectivist cultures prize "
            "agreeableness, modesty, and emotional restraint, and the "
            "same behavior reads differently - assertiveness as "
            "leadership in one place, arrogance in another. Mean levels "
            "differ modestly across nations, though within-culture "
            "variation dwarfs between-culture differences: two strangers "
            "from the same city differ more than the average citizens of "
            "two countries. Practical rules for cross-cultural reading: "
            "never mistake expression norms for trait levels (the "
            "reserved culture is not a nation of introverts); learn the "
            "local ideals before judging (modesty norms hide honest "
            "self-promotion); and hold the universal structure while "
            "respecting the local performance. Personality gives the "
            "shared human keyboard; culture writes the local music."
        ),
        "how_it_works": (
            "The universality works through the lexical hypothesis: "
            "every language evolves words for the differences that "
            "matter socially, and factor-analyzing those words keeps "
            "finding the same broad families - which is strong evidence "
            "the families are human, not Western. The cultural shaping "
            "works through display rules and ideals: cultures teach "
            "which trait expressions earn approval, so members amplify "
            "approved expressions and mute disapproved ones. The result "
            "is a layered personality: the trait dial underneath, the "
            "cultural equalizer on top. Misreading happens at the "
            "equalizer: the observer mistakes the muted expression for "
            "the dial setting. The correction is structural: compare "
            "people against their own culture's norms first, and treat "
            "cross-cultural score comparisons as suggestive rather than "
            "precise. The deepest practical move is curiosity over "
            "calibration: ask how respect, warmth, and strength are "
            "performed here before deciding what you are seeing."
        ),
        "key_points": [
            "The Big Five structure replicates across dozens of cultures and languages - the families are human, not Western.",
            "Culture shapes expression and ideals through display rules: the same behavior reads differently across norms.",
            "Within-culture variation dwarfs between-culture differences.",
            "Never mistake expression norms for trait levels; compare against local norms first.",
            "The shared keyboard, the local music: universal structure, culturally performed.",
        ],
        "requirements": [
            "Universality evidence cited (multi-culture replication), not assumed.",
            "Expression separated from trait level in every cross-cultural read.",
            "Local ideals learned before any judgment of individuals.",
            "Cross-cultural score comparisons treated as suggestive, not precise.",
        ],
        "standards": [STD_BIGFIVE, "Cross-cultural replication per McCrae et al. (2005)."],
        "citations": [CIT_CULTURE, CIT_BIGFIVE_TAX],
        "sig_lens": (
            "The Signature reading hears one human instrument played in "
            "many halls: the strings are the same everywhere, but each "
            "hall's acoustics - its culture - shapes what the audience "
            "hears. The Signature traveler learns each hall before "
            "judging the playing."
        ),
    },
    {
        "key": "conflict_styles",
        "name": "Conflict Styles and Personality",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "People handle conflict in patterned ways, and the patterns "
            "trace to traits. The five classic styles: competing (assert "
            "your way), collaborating (solve it together), compromising "
            "(split the difference), avoiding (leave it alone), and "
            "accommodating (yield to keep peace). High extraversion, "
            "especially assertiveness, tilts toward competing and "
            "collaborating - engaging directly. High agreeableness tilts "
            "toward accommodating and avoiding - preserving harmony. High "
            "neuroticism intensifies whatever style is used and tilts "
            "toward avoiding (fear of the blowup) or explosive competing. "
            "High conscientiousness tilts toward collaborating with "
            "preparation - the documented, principled approach. High "
            "openness tilts toward reframing the conflict itself. No "
            "style is universally best: competing saves the burning "
            "building, avoiding lets the trivial pass, accommodating "
            "protects the vital relationship, compromising resolves the "
            "deadlock, collaborating solves the important problem. "
            "Mastery is range: know your default, recognize what the "
            "situation actually needs, and stretch deliberately into the "
            "non-default styles. The growth edge for every pattern is "
            "its overuse - the avoider who never engages, the competitor "
            "who turns everything into war."
        ),
        "how_it_works": (
            "Conflict styles work on two axes: assertiveness (pursuing "
            "your own concerns) and cooperativeness (pursuing the other "
            "person's concerns). Competing is high assertiveness, low "
            "cooperation; accommodating is the reverse; avoiding is low "
            "on both; collaborating is high on both; compromising is the "
            "middle. Personality sets the default position on these axes: "
            "the assertive extravert starts near competing, the agreeable "
            "introvert near accommodating, and stress pushes everyone "
            "toward their corners. The situation should choose the style, "
            "not the trait: emergencies need competing, trivial "
            "irritations deserve avoiding, vital relationships merit "
            "accommodating on small things, deadlocks need compromising, "
            "and important complex problems repay collaborating. Stretch "
            "works by deliberate practice in low stakes: the avoider "
            "practices naming small disagreements early, the competitor "
            "practices asking one genuine question before stating a "
            "position. Over time the practiced style becomes available "
            "under pressure - range, not replacement."
        ),
        "key_points": [
            "Five styles on two axes (assertiveness x cooperativeness): competing, collaborating, compromising, avoiding, accommodating.",
            "Personality sets the default: assertiveness tilts toward competing, agreeableness toward accommodating, reactivity intensifies.",
            "No universally best style: the situation should choose - emergencies, trivia, relationships, deadlocks, and complex problems each want different styles.",
            "Mastery is range: know your default, stretch deliberately into non-default styles in low stakes.",
            "Every pattern's growth edge is its overuse.",
        ],
        "requirements": [
            "The two axes taught explicitly so styles are understood, not just memorized.",
            "Defaults traced to traits honestly, including stress effects.",
            "Situational fit prescribed: each style matched to the situations it serves.",
            "Stretch practiced in low stakes before it is needed in high stakes.",
        ],
        "standards": ["Thomas-Kilmann conflict mode framework; trait correlates per the personality literature."],
        "citations": [CIT_BIGFIVE_TAX, CIT_NEO],
        "sig_lens": (
            "The Signature reading treats conflict as dissonance: every "
            "ensemble hits it, and the Signature player knows five ways "
            "to resolve the chord - drive through it, voice it together, "
            "meet in the middle, let it ring out, or yield the note. "
            "Mastery is knowing which resolution the passage needs."
        ),
    },
    {
        "key": "growth",
        "name": "Growing on Purpose: Developing Your Traits",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Traits change, and they can be changed on purpose - slowly, "
            "through behavior, not by wishing. The evidence-based path "
            "has four steps. First, pick one facet, not a domain: not "
            "'become conscientious' but 'keep every promise this week' "
            "(dutifulness) or 'clear the desk nightly' (order). Second, "
            "design the behavior into your life: implementation intentions "
            "('when X, I will do Y'), environment design (the running "
            "shoes by the door), and accountability (a person who checks). "
            "Third, repeat past the awkward phase: months of the behavior, "
            "because traits consolidate from sustained repetition, not "
            "from insight. Fourth, measure: re-take the facet scale "
            "quarterly and watch the line move. What works per domain: "
            "conscientiousness yields to systems and routines; "
            "extraversion to graduated social exposure; agreeableness to "
            "practiced assertiveness scripts and scheduled generosity; "
            "neuroticism to sleep, exercise, cognitive reappraisal, and "
            "worry scheduling; openness to deliberate novelty - new "
            "routes, new genres, new conversations. What does not work: "
            "affirmations without behavior, one-week challenges, and "
            "trying to change everything at once. The honest promise: a "
            "year of deliberate practice moves a facet meaningfully; a "
            "decade of chosen roles moves the domain."
        ),
        "how_it_works": (
            "Deliberate trait change works through the same machinery as "
            "natural change, aimed on purpose. The corresponsive "
            "principle runs in reverse: instead of waiting for roles to "
            "shape you, you adopt the behaviors of the trait you want "
            "until the behaviors become the trait. Psychologically this "
            "is bottom-up: states repeated become habits, habits "
            "repeated become dispositions - the person who acts "
            "outgoing three times a week for a year is measurably more "
            "extraverted, because the brain generalizes from its own "
            "behavior ('I keep doing this, so this must be me'). "
            "Implementation intentions work by pre-loading the decision: "
            "'when the meeting starts, I will ask one question' bypasses "
            "the in-the-moment negotiation that the old trait always "
            "wins. Environment design works by removing the negotiation "
            "entirely. Measurement closes the loop: quarterly facet "
            "scores turn a vague aspiration into a visible trend, and "
            "visible trends sustain effort through the flat middle "
            "months when nothing feels different. The timeline is the "
            "point: behavior in weeks, habits in months, traits in "
            "years. Anyone promising faster is selling something."
        ),
        "key_points": [
            "Change works bottom-up: repeated states become habits, habits become traits - behavior first, disposition follows.",
            "The method: one facet, implementation intentions, environment design, accountability, months of repetition, quarterly measurement.",
            "Per-domain levers: systems for conscientiousness, graduated exposure for extraversion, scripts for agreeableness, reappraisal for neuroticism, novelty for openness.",
            "What fails: affirmations without behavior, one-week challenges, changing everything at once.",
            "Honest timeline: behavior in weeks, habits in months, traits in years.",
        ],
        "requirements": [
            "Facet-level targets, never domain-level wishes.",
            "Behavior specified as implementation intentions with triggers.",
            "Environment and accountability designed in, not left to willpower.",
            "Quarterly measurement with a real scale; timelines stated honestly.",
        ],
        "standards": ["Volitional personality change per Hudson & Fraley (2015) and the intervention literature."],
        "citations": [CIT_MATURITY, CIT_BIGFIVE_TAX],
        "sig_lens": (
            "The Signature reading makes growth the whole point of the "
            "instrument: the Signature player chooses the piece that "
            "demands the missing technique and practices it until the "
            "fingers obey. Retune deliberately, one string at a time, "
            "and let the years compound the practice."
        ),
    },
    {
        "key": "integrated_view",
        "name": "The Integrated View: One Person, Many Models",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The final record puts the whole database together on one "
            "person. Take Maya: Big Five high openness, high "
            "conscientiousness, mid extraversion, high agreeableness, "
            "low neuroticism. HEXACO adds high honesty-humility. MBTI "
            "reads INTJ - the architect. Enneagram reads Type 1 with a 9 "
            "wing - the principled reformer softened by the peacemaker. "
            "DISC reads high C with S - the careful stabilizer. "
            "Temperament reads melancholic-phlegmatic. Notice what "
            "happens: the models converge. Different languages, same "
            "person - principled, systematic, calm, improving things "
            "quietly. Where models disagree, the disagreement is "
            "information: the MBTI's introversion plus the Big Five's "
            "mid-range extraversion says 'socially capable, "
            "selectively social' - a finer truth than either alone. The "
            "integration rules: use traits for precision, types for "
            "narrative; let models cross-examine each other; trust "
            "convergence, investigate divergence; and always end where "
            "this database began - the person is larger than every map. "
            "Models are the scaffolding; the person is the building. "
            "Take the scaffolding down when the understanding stands."
        ),
        "how_it_works": (
            "Integration works by triangulation across model families. "
            "Each model is a projection of the same underlying "
            "personality onto different axes - traits project onto "
            "dimensions, types project onto categories, the Enneagram "
            "projects onto motivations, DISC onto workplace behaviors. "
            "Projections of the same object agree where the object is "
            "clear and diverge where it is ambiguous, so convergence "
            "across models is strong evidence ('every lens sees the "
            "principled systematizer') and divergence is a question to "
            "investigate ('why does the type system see an introvert "
            "where the traits see an ambivert?'). The practical method: "
            "write the one-paragraph portrait from the trait profile "
            "first (precision), then translate it into each type "
            "language (narrative), then check the translations against "
            "each other and against the real person. Keep what "
            "converges, explore what diverges, discard what the person "
            "rejects - they remain the authority. The integrated view "
            "is not a super-model; it is the habit of holding many "
            "lenses at once and never mistaking any lens for the eye."
        ),
        "key_points": [
            "One person, many projections: traits, types, motivations, and workplace styles describe the same underlying personality.",
            "Convergence across models is strong evidence; divergence is a question to investigate, not an error to hide.",
            "Method: trait portrait first for precision, type translations second for narrative, the real person as final authority.",
            "Use traits for precision and types for narrative - each family has its proper job.",
            "The person is larger than every map: take the scaffolding down when the understanding stands.",
        ],
        "requirements": [
            "At least two model families triangulated in any integrated read.",
            "Convergences trusted, divergences investigated explicitly.",
            "The person's own correction treated as authoritative over every model.",
            "No super-model claimed: integration is a habit of multiple lenses, not a new box.",
        ],
        "standards": [STD_BIGFIVE, STD_HEXACO, STD_TYPES, "Integrative personality assessment per the multi-method literature."],
        "citations": [CIT_NEO, CIT_HEXACO, CIT_ENNEAGRAM, CIT_MBTI],
        "sig_lens": (
            "The Signature reading ends where the music begins: all the "
            "tunings, frets, chord shapes, and set lists studied, and "
            "then the player simply plays. The Signature master holds "
            "every lens lightly and hears the person directly - the "
            "instrument, at last, understood whole."
        ),
    },
])
