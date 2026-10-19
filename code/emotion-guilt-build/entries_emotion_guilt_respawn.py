#!/usr/bin/env python3
"""Entries for the Guilt Emotion databases (Manon's 2026-10-17 16:15 order,
emotion series - RESPAWN; rebuilt fully from scratch, 2026-10-17).

Descriptive and educational ONLY - the database describes and simulates
guilt; it never diagnoses real people, never labels any real person with an
emotional state, and never offers therapeutic advice beyond general, safe,
everyday guidance. No clinical language, no diagnostic labels. Records that
touch on handling guilt emphasize constructive, everyday handling.

34 records, ordered by the teaching ladder (ladder_rank 1-10,
non-decreasing), following the shared emotion-template spec:
what guilt IS -> first-person simulation -> body signals -> facial
expression -> triggers -> behavior -> healthy expression -> recognizing it
in others -> related emotions and mixes -> complex behavioral simulation.

ID prefixes: JAH-EMGU- (public) and JAH-EMGUS- (signature), verified free
in the manifest id_prefix values (2,306 databases, zero hits) and in all
jah-databases-data-1 shard record IDs (zero 'JAH-EMGU' substring hits),
2026-10-17.

Public records are real, fact-checked psychology knowledge (Tangney and
Dearing, Baumeister Stillwell and Heatherton, Lewis, Tracy and Robins,
Haidt, Festinger, Lazarus, Gross, Scherer, Ekman, Keltner and Buswell,
Damasio, APA Dictionary). Signature editions are his original Signature
lens - guilt as the soul's ledger, the honest bookkeeping of the conscience:
signal, repair, and release - never presented as authentic public record.

Never the words "bat belt" anywhere. No website references. No Facebook.
No religious talk. Nothing hate-adjacent, profane, or inappropriate.
"""

SIG_TAIL = ("Signature original - his original Signature lens: guilt as the "
            "soul's ledger, the honest bookkeeping of the conscience - "
            "signal, repair, and release. Signature editions frame every "
            "facet as the ledger balancing itself: the signal that a "
            "standard was breached, the repair that sets the account "
            "straight, and the release that lets the lesson stay without "
            "the weight. Never as a diagnosis, never labeling any real "
            "person, and never presented as authentic public record.")

CIT_TANGNEY = ("Tangney JP, Dearing RL. Shame and Guilt. Guilford Press; "
               "2002.")
CIT_BAUMEISTER = ("Baumeister RF, Stillwell AM, Heatherton TF. Guilt: an "
                  "interpersonal approach. Psychological Bulletin. "
                  "1994;115(2):243-267.")
CIT_LEWIS = ("Lewis M. Shame: The Exposed Self. Free Press; 1992.")
CIT_TRACY = ("Tracy JL, Robins RW. Putting the self into self-conscious "
             "emotions: a theoretical model. Psychological Science. "
             "2004;15(2):103-113.")
CIT_HAIDT = ("Haidt J. The moral emotions. In: Davidson RJ, Scherer KR, "
             "Goldsmith HH, editors. Handbook of Affective Sciences. Oxford "
             "University Press; 2003.")
CIT_FESTINGER = ("Festinger L. A Theory of Cognitive Dissonance. Stanford "
                 "University Press; 1957.")
CIT_LAZARUS = ("Lazarus RS. Emotion and Adaptation. Oxford University Press; "
               "1991.")
CIT_GROSS = ("Gross JJ, editor. Handbook of Emotion Regulation. 2nd ed. "
             "Guilford Press; 2014.")
CIT_SCHERER = ("Scherer KR. Appraisal considered as a process of multilevel "
               "sequential checking. In: Scherer KR, Schorr A, Johnstone T, "
               "editors. Appraisal Processes in Emotion. Oxford University "
               "Press; 2001.")
CIT_EKMAN = ("Ekman P. Emotions Revealed: Recognizing Faces and Feelings to "
             "Improve Communication and Emotional Life. Holt; 2003.")
CIT_APA = ("American Psychological Association. APA Dictionary of "
           "Psychology; current edition.")
CIT_KELTNER = ("Keltner D, Buswell BN. Embarrassment: its distinct form and "
               "appeasement functions. Psychological Bulletin. "
               "1997;122(3):250-270.")
CIT_DAMASIO = ("Damasio AR. Looking for Spinoza: Joy, Sorrow, and the "
               "Feeling Brain. Harcourt; 2003.")

ENTRIES = [
# ---------------------------------------------------------------- 1-4: what guilt IS
dict(
    key="guilt_definition", name="What Guilt Is: A Plain-Language Definition",
    group="Foundations", ladder_rank=1, ladder_tier="foundations",
    description=(
        "Guilt is the emotion you feel when you believe you have done "
        "something wrong - or failed to do something right - and someone was "
        "affected by it. In everyday words: guilt is the mind's way of "
        "flagging a personal standard you crossed. Psychologists describe it "
        "as a self-conscious emotion, which means it needs a sense of self "
        "to exist: you have to be able to picture yourself, picture what you "
        "did, and measure the two against each other. That measuring is "
        "guilt's engine. The classic sentence people use is 'I did a bad "
        "thing,' and that wording matters - guilt points at the ACTION, not "
        "at the person. Researchers Tangney and Dearing made this the "
        "central distinction in the field: guilt says 'I did something bad,' "
        "while its close cousin shame says 'I AM bad.' That single "
        "difference decides almost everything about what follows. Guilt "
        "pulls a person toward repair - apologizing, fixing, making amends. "
        "It is other-focused: at its core sits a concern for someone who was "
        "harmed, disappointed, or let down. Guilt is not proof of wrongdoing "
        "on its own - it is the feeling that a wrong MAY have happened, and "
        "like every emotion, it can misfire. But its basic job is social "
        "glue: it keeps people answerable to their own standards and to the "
        "people around them."),
    how_it_works=(
        "Guilt runs on a three-beat appraisal: standard, breach, and "
        "responsibility. First, a standard is active - a personal rule like "
        "'I keep my promises' or a shared one like 'I do not hurt people.' "
        "Second, the mind judges that the standard was breached by something "
        "done or left undone. Third, and most important, the mind assigns "
        "responsibility: I could have acted differently, and my choice "
        "mattered. That third beat is what separates guilt from mere regret "
        "or sadness about a bad outcome. If the same harm happened but the "
        "person sees no way they could have prevented it, the feeling shifts "
        "toward sorrow rather than guilt. Once the three beats land, the "
        "body and mind produce the familiar package - tension, replay, and "
        "an urge to set things right. Understanding this chain gives the "
        "whole database its leverage: guilt eases when the breach is "
        "repaired, when responsibility is reassessed honestly, or when the "
        "standard itself is examined and found to be unfair."),
    key_points=[
        "Guilt is a self-conscious emotion: it needs a sense of self to compare action against standard.",
        "The appraisal chain is standard -> breach -> responsibility; the third beat is what makes it guilt rather than sorrow.",
        "Guilt points at the ACTION ('I did a bad thing'), which is why it motivates repair rather than hiding.",
        "It is other-focused at its core: someone was harmed, disappointed, or let down.",
        "Guilt is a signal, not a verdict - it can misfire, and it needs honest checking, not blind obedience.",
    ],
    requirements=[
        "Everyday definition a student or writer can quote",
        "The guilt-points-at-action distinction stated plainly",
        "The three-beat appraisal chain in plain words",
        "No diagnostic language anywhere in the record",
    ],
    standards=["APA Dictionary of Psychology definition of guilt"],
    citations=[CIT_APA, CIT_TANGNEY, CIT_BAUMEISTER],
    sig_lens=(
        "The Signature lens reads guilt as the soul's ledger opening its "
        "books: the moment the inner accountant flags that an entry does "
        "not balance. Where public psychology calls the three beats "
        "appraisal, the Signature method calls them the ledger's audit - "
        "standard, breach, responsibility - and treats the repair urge as "
        "the books demanding to be balanced. The ledger is honest by "
        "design: it records what was done, not who the person is. Clearly "
        "labeled Signature-made, never presented as authentic public "
        "record."),
),
dict(
    key="guilt_emotion_family", name="Guilt in the Emotion Family: Self-Conscious Roots and Moral Branches",
    group="Foundations", ladder_rank=1, ladder_tier="foundations",
    description=(
        "Guilt sits in a special branch of the emotion map: the "
        "self-conscious emotions. Unlike basic feelings such as fear or "
        "surprise, which arrive fast and need little thought, guilt cannot "
        "fire until the mind does real cognitive work. Tracy and Robins "
        "describe the requirement precisely: a person must hold a stable "
        "sense of self, be aware of social standards, and be able to "
        "evaluate their own behavior against those standards. That is why "
        "guilt shows up later in childhood than the basic emotions - "
        "typically around ages two to three, alongside the child's growing "
        "awareness of rules and of other minds. On the family tree, guilt "
        "is also one of the moral emotions described by Haidt: feelings "
        "that exist to regulate social life. Its nearest neighbors are "
        "shame, embarrassment, and pride - the other self-conscious "
        "emotions - and its close working partners are empathy and "
        "compassion, which supply the other-focused concern that guilt "
        "needs. Guilt's feeders are therefore twofold: the cognitive "
        "machinery of self-evaluation, and the social machinery of caring "
        "what one's actions do to others. Take away the self-awareness and "
        "there is no guilt, only reflex. Take away the care for others and "
        "guilt thins into a cold rule-check with no heart in it."),
    how_it_works=(
        "The family position explains guilt's timing and triggers. Because "
        "it is self-conscious, guilt is always about the self IN RELATION "
        "to something - a standard, another person, a group. The mind runs "
        "a comparison: the real self (what I did) against the ought self "
        "(what I believe I should have done). The gap between the two is "
        "measured, and the size of the gap sets the volume. Because it is a "
        "moral emotion, the comparison that matters most is interpersonal: "
        "did my action harm someone, or threaten a bond I value? Baumeister "
        "and colleagues argue this interpersonal core is guilt's true "
        "function - it is the feeling that maintains relationships by "
        "making breaches expensive to the conscience and repairs rewarding. "
        "This is why guilt's family tree matters for everything later in "
        "this database: every trigger, body signal, and behavior described "
        "here grows out of that comparison - self against standard, action "
        "against its effect on another."),
    key_points=[
        "Guilt is a self-conscious emotion: it needs self-awareness, standards, and self-evaluation - which is why it appears later in childhood than basic emotions.",
        "It is also a moral emotion: its job is regulating social life and protecting relationships.",
        "The mechanism is a comparison between the real self (what was done) and the ought self (what should have been done).",
        "Nearest neighbors: shame, embarrassment, pride; working partners: empathy and compassion.",
        "Guilt's feeders are self-evaluation machinery plus genuine concern for others.",
    ],
    requirements=[
        "Self-conscious emotion requirements stated in plain words",
        "Moral-emotion framing with the relationship-maintenance function",
        "The real-self versus ought-self comparison explained",
        "No diagnostic language anywhere in the record",
    ],
    standards=["Tracy and Robins model of self-conscious emotions"],
    citations=[CIT_TRACY, CIT_HAIDT, CIT_BAUMEISTER],
    sig_lens=(
        "The Signature lens places guilt on the ledger's family tree: the "
        "branch where the books are kept not for survival but for "
        "rightness. Where public psychology maps self-conscious emotions, "
        "the Signature method maps the ledger's departments - the auditors "
        "(standards), the witnesses (empathy for others), and the clerks "
        "(the ought-self records). His reading: a conscience is simply a "
        "ledger that cares who else is affected by its entries. Clearly "
        "labeled Signature-made, never presented as authentic public "
        "record."),
),
dict(
    key="guilt_intensity_scale", name="Guilt at Every Volume: Mild, Moderate, and Intense",
    group="Foundations", ladder_rank=2, ladder_tier="foundations",
    description=(
        "Guilt is not one fixed feeling - it is a whole volume range, and "
        "the same emotion behaves very differently at different settings. "
        "At MILD volume, guilt is a passing twinge: the small pang after "
        "forgetting to thank someone, the brief wince at a sharp tone used "
        "in a hurry. It flickers, delivers its message, and fades within "
        "minutes or hours. At MODERATE volume, guilt settles in and stays "
        "awhile: the lingering weight of a broken promise, a harsh word "
        "that keeps replaying through the evening. It asks for something - "
        "an apology, a correction, a second try - and it does not fully "
        "release until that something is addressed. At INTENSE volume, guilt "
        "becomes heavy and consuming: the sleepless replay of a serious "
        "harm, the feeling of carrying something that will not set down. "
        "Appetite, sleep, and focus can all bend under it. What sets the "
        "volume? Research points to four dials: how much harm was done (or "
        "seems to have been done), how close the relationship is, how much "
        "responsibility the person assigns to themselves, and whether the "
        "harm can be undone. A small slight to a stranger with easy repair "
        "stays mild; a serious harm to a loved one with no way back plays "
        "at full volume. The dials explain why two people can do the same "
        "thing and feel wildly different guilt - they are turning different "
        "dials."),
    how_it_works=(
        "The volume model works like a mixing board with four faders: "
        "perceived harm, closeness of the bond, self-assigned "
        "responsibility, and irreversibility. Each fader runs from low to "
        "high, and the overall volume is roughly their combination - turn "
        "up any one and the feeling grows. This is why guilt is so "
        "personal: the faders are set by the individual's own appraisal, "
        "not by any outside judge. Two people can witness the same event "
        "and set the faders differently, because they weigh harm, closeness, "
        "and responsibility differently. The model also explains guilt's "
        "famous misfires: when the responsibility fader is cranked too high "
        "- the person blames themselves for something no one could have "
        "prevented - the volume screams even though a fair audit would set "
        "it low. Learning to check each fader honestly is one of the most "
        "practical skills in this whole database: is the harm real or "
        "imagined? Is the responsibility mine, shared, or nobody's?"),
    key_points=[
        "Guilt runs mild (passing twinge) to moderate (lingering, asks for repair) to intense (heavy, consumes sleep and focus).",
        "Four dials set the volume: perceived harm, closeness of the bond, self-assigned responsibility, irreversibility.",
        "The dials are set by personal appraisal, which is why the same act produces different guilt in different people.",
        "Misfires happen when a dial - especially responsibility - is set too high for the facts.",
        "Checking each dial honestly is a practical skill for keeping guilt proportionate.",
    ],
    requirements=[
        "Three volumes described as lived experience, not abstractions",
        "The four dials named and explained",
        "Why the same act produces different guilt in different people",
        "No diagnostic language anywhere in the record",
    ],
    standards=["Baumeister and colleagues on guilt intensity and interpersonal function"],
    citations=[CIT_BAUMEISTER, CIT_LAZARUS],
    sig_lens=(
        "The Signature lens reads the volume scale as the ledger's alarm "
        "bell: mild guilt is a clerk's quiet note in the margin, moderate "
        "guilt is a flagged entry demanding review, intense guilt is the "
        "whole ledger glowing red until the account is settled. His "
        "reading of the four dials: harm is the size of the entry, "
        "closeness is whose account it sits in, responsibility is the "
        "signature on the line, and irreversibility is whether the ink is "
        "permanent. Turn down a dial honestly and the bell quiets - that "
        "is the ledger working as designed. Clearly labeled "
        "Signature-made, never presented as authentic public record."),
),
dict(
    key="guilt_myths", name="Myths and Misunderstandings About Guilt",
    group="Foundations", ladder_rank=2, ladder_tier="foundations",
    description=(
        "Guilt carries more folklore than almost any other emotion, and the "
        "myths cause real trouble. MYTH ONE: guilt proves you did something "
        "wrong. It does not - guilt proves you BELIEVE you did something "
        "wrong, and beliefs can be mistaken, inherited, or installed by "
        "other people's expectations. Plenty of people feel guilty for "
        "things no fair judge would blame them for. MYTH TWO: guilt and "
        "shame are the same thing. They are close cousins with opposite "
        "impulses: guilt says 'fix what you did,' shame says 'hide who you "
        "are.' Mixing them up turns a repairable action into a verdict on "
        "the self. MYTH THREE: guilt is always bad and should be eliminated. "
        "Guilt is information - a signal that a standard matters to you. "
        "Killing the signal does not remove the standard; it just removes "
        "your awareness of breaching it. MYTH FOUR: feeling guilty makes you "
        "a good person, and not feeling guilty makes you a bad one. Guilt "
        "correlates with caring about others, but it is neither a moral "
        "report card nor a substitute for actual repair - the apology "
        "matters more than the ache. MYTH FIVE: one apology wipes the slate "
        "clean. Sometimes repair takes time, repeated effort, or changed "
        "behavior, and the other person gets a say in when the account is "
        "settled. MYTH SIX: if you just think about it hard enough, the "
        "guilt will resolve. Rumination usually feeds guilt rather than "
        "digesting it - replay without repair is a loop, not a process."),
    how_it_works=(
        "Myths persist because they simplify something uncomfortable. "
        "Each myth above collapses a two-sided truth into a one-sided "
        "rule, and the collapse creates the problem. 'Guilt proves "
        "wrongdoing' collapses the appraisal into the fact - but appraisal "
        "is a judgment that can be wrong, so the rule punishes the "
        "conscientious and excuses the oblivious. 'Eliminate all guilt' "
        "collapses signal into noise - but a silenced signal leaves the "
        "standard unguarded, so the rule trades discomfort for "
        "carelessness. The healthy stance treats each myth as a question "
        "instead of a law: is the belief of wrongdoing accurate? Is this "
        "guilt or shame talking? Is the signal proportionate to the facts? "
        "Has repair actually happened, or only been imagined? Turning myths "
        "into questions restores guilt to its proper job - an honest "
        "reporter, not a judge, jury, and jailer."),
    key_points=[
        "Guilt proves a BELIEF of wrongdoing, not wrongdoing itself - beliefs can be mistaken.",
        "Guilt and shame are cousins with opposite impulses: repair the action versus hide the self.",
        "Guilt is information, not an enemy; silencing it removes the warning, not the standard.",
        "Feeling guilty is not a moral report card - repair matters more than the ache.",
        "Rumination feeds guilt; replay without repair is a loop, not a process.",
        "Turn each myth into a question: is the belief accurate? Is repair real or only imagined?",
    ],
    requirements=[
        "At least five named myths, each corrected plainly",
        "The guilt-versus-shame confusion addressed directly",
        "Why myths persist, explained without jargon",
        "No diagnostic language anywhere in the record",
    ],
    standards=["Tangney and Dearing on guilt versus shame distinctions"],
    citations=[CIT_TANGNEY, CIT_BAUMEISTER],
    sig_lens=(
        "The Signature lens treats myths as smudged ledger entries - old "
        "handwriting from other people's books copied into your own. 'Guilt "
        "proves wrongdoing' is someone else's audit stamped on your page. "
        "His method: hold every inherited rule up to the ledger's own "
        "light and ask whether the entry is really yours. A smudged entry "
        "gets corrected, not obeyed. Clearly labeled Signature-made, never "
        "presented as authentic public record."),
),
# ------------------------------------------------- 5-9: first-person simulation
dict(
    key="guilt_first_person", name="Inside the Feeling: Guilt in the First Person",
    group="Foundations", ladder_rank=2, ladder_tier="foundations",
    description=(
        "This is what guilt feels like from the inside, right now. It "
        "starts as a catch in the chest - not pain exactly, more like a "
        "hand closing around something soft. Then the replay begins, "
        "uninvited: the moment plays again, and this time you see the "
        "version where you did it differently. You said the thing. You "
        "didn't call. You took the last one and told yourself nobody would "
        "mind, and now you know somebody minded. The scene loops with small "
        "variations, each pass finding a new detail you missed - the look "
        "on their face you didn't register at the time, the pause before "
        "they answered. Underneath the replay sits a heaviness, as if your "
        "limbs gained weight while you weren't looking. There is also an "
        "itch to DO something: apologize, explain, fix, confess - the urge "
        "is physical, like needing to scratch. And threaded through it all "
        "is a quieter thought, the one the feeling is really about: I am "
        "someone who does things like that, and I don't want to be. That "
        "last thought is why guilt stings more than simple regret - it is "
        "not just about the act, it is about what the act says, and the "
        "mind keeps turning it over like a stone with a sharp edge."),
    how_it_works=(
        "The first-person passage above is built from guilt's documented "
        "components, and each maps to a mechanism. The 'catch in the chest' "
        "is the body's arousal response - mild sympathetic activation that "
        "marks the feeling as urgent. The replay loop is the mind's attempt "
        "to re-run the appraisal: each pass re-checks standard, breach, and "
        "responsibility, hunting for a version of events that balances. The "
        "heaviness is the action urge with nowhere to go - guilt is an "
        "approach emotion, pulling toward repair, and when repair is "
        "delayed the urge pools as physical weight. The 'what this says "
        "about me' thought is the self-evaluation component firing: the "
        "ought-self comparison running in the background of every replay. "
        "Simulations like this one are the database's teaching engine: by "
        "walking the feeling beat by beat, a reader learns to recognize "
        "each component in their own experience - and recognition is the "
        "first step to working with the feeling instead of drowning in it."),
    key_points=[
        "The inside of guilt has four moving parts: the chest-catch (arousal), the replay (re-appraisal), the heaviness (blocked repair urge), and the self-thought (ought-self comparison).",
        "The replay loop is the mind hunting for a version of events that balances - it stops when repair happens, not when thinking stops.",
        "Guilt is an approach emotion: the urge points TOWARD the person harmed, which is why avoidance feels so wrong inside it.",
        "The sting comes from the self-implication: the act seems to say something about who you are.",
        "Recognizing each component by name is the first step to working with the feeling.",
    ],
    requirements=[
        "A vivid first-person passage a reader can recognize themselves in",
        "Each element of the passage mapped to its mechanism",
        "The approach-urge explained in felt terms",
        "No diagnostic language anywhere in the record",
    ],
    standards=["Tangney and Dearing on the phenomenology of guilt"],
    citations=[CIT_TANGNEY, CIT_DAMASIO],
    sig_lens=(
        "The Signature lens reads the inner passage as the ledger's audit "
        "in progress: the replay is the accountant re-reading the entry, "
        "the heaviness is the unbalanced page pressing on the chest, the "
        "itch to act is the books demanding their balancing line. His "
        "reading insists the audit is not punishment - it is the ledger "
        "doing the only job it has, keeping the accounts true. Clearly "
        "labeled Signature-made, never presented as authentic public "
        "record."),
),
dict(
    key="guilt_time_course", name="How Guilt Changes Over Time: Onset, Peak, Fading, Aftershock",
    group="Foundations", ladder_rank=3, ladder_tier="foundations",
    description=(
        "Guilt has a shape in time, and knowing the shape helps you ride it. "
        "ONSET is usually sudden: the moment of realization - the email sent "
        "in anger, the promise remembered too late, the face falling in "
        "real time. The appraisal lands all at once and the body answers "
        "within seconds: heat, tension, the stomach dropping. PEAK arrives "
        "minutes to hours later, when the replay loop is running at full "
        "speed. This is guilt at its loudest: the scene replays with "
        "variations, responsibility feels total, and the urge to repair is "
        "almost physical. Most people try to act at the peak - the "
        "midnight apology text, the rehearsed confession - because the "
        "feeling insists that only immediate action will quiet it. FADING "
        "begins when one of three things happens: genuine repair (the "
        "apology made, the harm fixed), honest reassessment (the "
        "responsibility dial turned down to its fair setting), or simple "
        "time and distraction wearing the loop down. Fading is gradual - "
        "the replay gets shorter, the chest-catch weaker, the days between "
        "pangs longer. AFTERSHOCK is the part nobody warns about: months "
        "later, a song, a place, an anniversary replays the scene in full "
        "color for thirty seconds. Aftershocks are normal; they are memory, "
        "not a new verdict. Each one is weaker than the last, provided the "
        "original account was actually settled and not just buried."),
    how_it_works=(
        "The time course follows the appraisal machinery. Onset is fast "
        "because the standard-breach-responsibility check can complete in a "
        "single flash of recognition - Lazarus notes that appraisals need "
        "not be slow or deliberate to be cognitively rich. Peak is the "
        "period of maximum re-appraisal cycling: the mind keeps re-running "
        "the check because no resolution has been reached, and each cycle "
        "re-arouses the body. Fading tracks resolution: repair satisfies "
        "the action urge, reassessment corrects the appraisal, and time "
        "reduces the accessibility of the memory. Aftershocks are "
        "cue-triggered retrievals - the same memory network firing when a "
        "matching cue appears, producing a brief echo of the original "
        "appraisal. Understanding the curve matters practically: the peak "
        "is the worst time to make big decisions (the responsibility dial "
        "is maxed), and aftershocks are the worst thing to interpret as "
        "evidence the guilt was never resolved."),
    key_points=[
        "Guilt's time shape: sudden onset (appraisal lands) -> peak (replay at full speed) -> fading (repair, reassessment, or time) -> aftershock (cue-triggered echoes).",
        "The peak is when the repair urge is strongest - and the worst time for big decisions, because the responsibility dial is maxed.",
        "Fading needs one of three things: genuine repair, honest reassessment, or time wearing the loop down.",
        "Aftershocks are memory echoes, not new verdicts; they weaken with each occurrence if the account was settled.",
        "Burying the feeling without repair does not fade it - it schedules stronger aftershocks.",
    ],
    requirements=[
        "Four phases described as lived experience with their triggers",
        "Why the peak is a bad time for big decisions",
        "Aftershocks normalized as memory, not relapse",
        "No diagnostic language anywhere in the record",
    ],
    standards=["Lazarus on appraisal timing; Gross on emotion time course"],
    citations=[CIT_LAZARUS, CIT_GROSS],
    sig_lens=(
        "The Signature lens reads the time course as the ledger's "
        "settlement cycle: onset is the entry being written in red, peak "
        "is the accountant refusing to close the books, fading is the "
        "balancing line being drawn, aftershock is an old page fluttering "
        "open in a draft. His rule: never confuse a fluttering page for a "
        "new debt - check whether the account was settled before paying "
        "twice. Clearly labeled Signature-made, never presented as "
        "authentic public record."),
),
dict(
    key="guilt_low_vs_high", name="Guilt at Low Intensity Versus High Intensity: Two Lived Snapshots",
    group="Foundations", ladder_rank=3, ladder_tier="foundations",
    description=(
        "The same emotion, two different weathers. LOW INTENSITY: You "
        "realize at lunch that you forgot to reply to a friend's message "
        "from three days ago. A small pang lands - brief, specific, almost "
        "polite. You think, 'I should text them,' and the thought comes "
        "with a little warmth, not dread. You send the text, they reply "
        "with a laughing emoji, and the whole thing is over before your "
        "sandwich is. The guilt did its job: a nudge, a correction, a "
        "release. Your evening is untouched. HIGH INTENSITY: You said "
        "something cutting to someone you love in an argument last month, "
        "and you have replayed it every night since. The scene arrives "
        "uninvited - while driving, while trying to sleep - and each "
        "replay adds a detail: the exact pause before they answered, the "
        "way their voice thinned. Your chest feels heavy by afternoon. You "
        "have drafted the apology eleven times and deleted it eleven times, "
        "because no wording seems big enough and every attempt feels like "
        "it would make things worse. Food tastes flat. You catch yourself "
        "being short with other people and feel guilty about THAT too, a "
        "second layer forming over the first. The difference between the "
        "two snapshots is not the kind of feeling - it is the dials. Low "
        "intensity means small harm, easy repair, shared or light "
        "responsibility. High intensity means serious harm (or serious "
        "seeming), a close bond, total self-blame, and no clear path to "
        "fix it."),
    how_it_works=(
        "Both snapshots run the same three-beat appraisal; only the dial "
        "settings differ. In the low-intensity case, perceived harm is "
        "small, repair is one text message away (low irreversibility), and "
        "responsibility is light - so the loop closes fast. In the "
        "high-intensity case, all four dials are cranked: the harm feels "
        "large, the bond is close, responsibility is total, and the words "
        "cannot be unsaid (high irreversibility). The second-layer guilt - "
        "feeling guilty about being short with others - shows how "
        "high-intensity guilt leaks: the depleted, preoccupied mind "
        "mishandles new situations, creating fresh breaches to feel guilty "
        "about. This is why high-intensity guilt needs a different "
        "strategy than low: the low version resolves with a single repair "
        "act, while the high version needs the dials checked one by one - "
        "is the responsibility truly total? Is repair truly impossible, or "
        "just frightening?"),
    key_points=[
        "Low-intensity guilt is a nudge: brief, specific, resolved by one small repair act.",
        "High-intensity guilt is weather: replay loops, heaviness, flat appetite, second-layer guilt about new mishaps.",
        "Same appraisal machinery in both - only the four dial settings differ.",
        "High-intensity guilt leaks: a preoccupied mind creates fresh breaches, layering new guilt over old.",
        "Low intensity needs a repair act; high intensity needs the dials audited one by one.",
    ],
    requirements=[
        "Two concrete lived snapshots, same emotion, clearly contrasted",
        "The dial model applied to explain the difference",
        "Second-layer guilt explained",
        "No diagnostic language anywhere in the record",
    ],
    standards=["Baumeister and colleagues on guilt intensity"],
    citations=[CIT_BAUMEISTER, CIT_LAZARUS],
    sig_lens=(
        "The Signature lens reads the two snapshots as the same ledger at "
        "different balances: low intensity is a penny out of place, found "
        "and pocketed by lunch; high intensity is a page torn out, with "
        "the accountant searching the floorboards every night. His "
        "direction: match the response to the balance - do not launch a "
        "full audit over a penny, and do not pocket-search your way out of "
        "a torn page. Clearly labeled Signature-made, never presented as "
        "authentic public record."),
),
dict(
    key="guilt_shame_blend", name="Guilt Mixed With Shame: The Most Common Partner Emotion",
    group="Foundations", ladder_rank=3, ladder_tier="foundations",
    description=(
        "Guilt rarely travels alone, and its most frequent companion is "
        "shame. The blend is so common that most people use one word for "
        "both - but the mixture has a texture worth learning to taste. "
        "Pure guilt says: 'I did a bad thing; I should fix it.' Pure shame "
        "says: 'I am a bad person; I should hide.' The BLEND says both at "
        "once: 'I did a bad thing, and it proves I am a bad person, and "
        "everyone will see.' The blend feels heavier than guilt alone "
        "because it adds exposure to the injury - not just 'I harmed "
        "someone' but 'I am the kind of person who harms.' Behaviorally, "
        "the blend pulls in two directions at once: guilt's urge to "
        "approach and repair fights shame's urge to withdraw and hide. "
        "That is why the blend is so paralyzing - the person wants to "
        "apologize AND wants to disappear, and the two urges cancel into "
        "frozen rumination. The blend usually forms when the action feels "
        "like a revelation: the harsh words didn't just hurt someone, they "
        "'showed who I really am.' Untangling it starts with a single "
        "question: am I upset about what I DID, or about what it supposedly "
        "PROVES about me? The first half is guilt and can be repaired. The "
        "second half is shame talking, and it needs a different answer: one "
        "act does not write a biography."),
    how_it_works=(
        "Tangney and Dearing's framework explains the blend mechanically. "
        "Guilt and shame share the same trigger event and the same "
        "self-evaluation machinery - they differ only in the FOCUS of "
        "attention. When attention rests on the specific behavior ('that "
        "thing I did'), the output is guilt with its repair urge. When "
        "attention slides to the global self ('what kind of person does "
        "that'), the output is shame with its hiding urge. The blend is "
        "rapid oscillation between the two foci - behavior, self, "
        "behavior, self - several times a minute, which is why it feels "
        "like a single heavy feeling rather than two. The paralysis is "
        "real: approach and withdrawal are incompatible motor programs, "
        "and the nervous system cannot execute both. The practical "
        "untangling technique - asking whether the distress is about the "
        "act or about the self - works because it forces attention to "
        "settle on one focus at a time, letting each half be addressed "
        "with its proper tool: repair for the act, perspective for the "
        "self."),
    key_points=[
        "The blend says both at once: 'I did a bad thing' (guilt) AND 'I am a bad person' (shame).",
        "It forms when the action feels like a revelation about the self, not just a mistake.",
        "The blend paralyzes because repair (approach) and hiding (withdrawal) are incompatible urges.",
        "Guilt and shame share machinery; they differ only in focus - behavior versus global self.",
        "Untangle with one question: am I upset about what I DID, or about what it supposedly PROVES about me?",
    ],
    requirements=[
        "The blend described as a distinct felt experience, not just two definitions",
        "Why the blend paralyzes, explained mechanically",
        "The attention-focus mechanism from Tangney and Dearing",
        "A practical untangling question",
        "No diagnostic language anywhere in the record",
    ],
    standards=["Tangney and Dearing; Lewis on guilt/shame focus of attention"],
    citations=[CIT_TANGNEY, CIT_LEWIS],
    sig_lens=(
        "The Signature lens reads the blend as two ledger problems stapled "
        "together: a real entry that needs balancing (guilt) and a forged "
        "verdict stamped across the whole book (shame). His method: "
        "separate the staple. Balance the entry with repair; strike the "
        "forged verdict as counterfeit - no single entry ever defines the "
        "ledger. Clearly labeled Signature-made, never presented as "
        "authentic public record."),
),
dict(
    key="guilt_day_vignette", name="A Day With Guilt: An Ordinary Day, One Unsettled Feeling",
    group="Foundations", ladder_rank=3, ladder_tier="foundations",
    description=(
        "MORNING: You wake up and for three seconds everything is fine. "
        "Then it lands - yesterday you snapped at your sister on the phone, "
        "told her she never listens, hung up too fast. The replay starts "
        "before your feet hit the floor. You rehearse the apology in the "
        "shower; it sounds stiff. You rehearse it again; it sounds "
        "groveling. MIDDAY: At work you are half-present. A colleague asks "
        "if you're okay and you say 'tired,' which is true but not the "
        "truth. You type the text to your sister four times. Version one "
        "is too long. Version two sounds like excuses. Version three is "
        "just 'I'm sorry about yesterday' and your thumb hovers - sending "
        "it feels like jumping. You don't send it. AFTERNOON: The guilt "
        "leaks sideways. You're short with a cashier and instantly guilty "
        "about that too. You buy the expensive coffee as a small "
        "self-punishment that helps for eleven minutes. EVENING: You call "
        "instead of texting. Your voice shakes on the first sentence. She "
        "is quiet, then says she was hurt, then says she's glad you "
        "called. The conversation lasts nine minutes. NIGHT: The replay "
        "tries to start once more, out of habit - but the scene it replays "
        "now includes the call, and the loop has nowhere to land. You fall "
        "asleep before midnight. The day's lesson, learned the slow way: "
        "guilt is heaviest in the hours between the breach and the repair, "
        "and the repair is almost always smaller than the dread of it."),
    how_it_works=(
        "The vignette compresses the full guilt cycle into one day so each "
        "mechanism can be seen in motion. Morning shows onset-plus-peak: "
        "the appraisal from yesterday re-fires on waking, and rehearsal is "
        "the mind pre-running the repair. Midday shows the approach urge "
        "blocked by fear - the unsent texts are repair attempts aborted at "
        "the threshold, which keeps the loop cycling. Afternoon shows "
        "leakage: depleted attention creates secondary breaches (the "
        "cashier), and the coffee is a textbook self-punishment substitute "
        "- a small cost paid to the conscience when the real repair feels "
        "too big. Evening shows genuine repair: specific acknowledgment, "
        "voice contact, the other person's response received - which is "
        "what actually closes the loop. Night shows the loop starved of "
        "fuel: with the repair in the memory, replay finds no unresolved "
        "breach to chew on. The vignette's teaching point is structural: "
        "every hour of dread was the repair urge with nowhere to go, and "
        "the nine-minute call did what eleven drafted texts could not."),
    key_points=[
        "Guilt is heaviest in the gap between breach and repair - the dread of repair usually exceeds the repair itself.",
        "Rehearsal without action keeps the loop cycling; aborted repairs (unsent texts) don't count as repair.",
        "Guilt leaks sideways into unrelated interactions when the mind is depleted.",
        "Substitute self-punishment (the expensive coffee) briefly soothes but doesn't settle the account.",
        "Genuine repair needs the other person's response - a sent apology closes loops that drafted ones can't.",
    ],
    requirements=[
        "A full ordinary day, morning to night, with guilt woven through",
        "Each beat mapped to its mechanism in how_it_works",
        "The dread-versus-repair size lesson stated plainly",
        "No diagnostic language anywhere in the record",
    ],
    standards=["Baumeister and colleagues on guilt and relationship repair"],
    citations=[CIT_BAUMEISTER, CIT_GROSS],
    sig_lens=(
        "The Signature lens reads the day as a ledger settling itself: "
        "morning is the red entry glaring from yesterday's page, midday is "
        "the accountant pacing instead of posting, evening is the "
        "balancing line finally drawn in the nine-minute call, night is "
        "the books closing on their own. His margin note: the dread is "
        "interest charged on a debt you could have paid at noon. Clearly "
        "labeled Signature-made, never presented as authentic public "
        "record."),
),
# ------------------------------------------------- 10-13: body signals
dict(
    key="guilt_body_signals", name="What Happens in the Body: Guilt's Physical Signature",
    group="Compounded", ladder_rank=4, ladder_tier="compounded",
    description=(
        "Guilt lives in the body as much as in the mind, and its physical "
        "signature is distinctive. The CHEST feels it first: a tightness or "
        "heaviness, as if something were sitting on the sternum. Breathing "
        "goes shallow - not the gasping of panic, but a quiet constriction, "
        "as if the lungs agreed to take up less room. The STOMACH knots or "
        "churns; appetite often drops because the gut and the conscience "
        "seem to share wiring. MUSCLES tense in the shoulders, jaw, and "
        "neck - the body bracing as if for a blow that never comes. The "
        "FACE heats: blushing is guilt's most visible tell, blood rising to "
        "the cheeks unasked. HANDS get restless - fidgeting, picking, "
        "wringing - small movements that discharge tension the body can't "
        "otherwise place. ENERGY drains in a particular way: not the wired "
        "tiredness of anxiety but a weighted fatigue, limbs feeling heavier "
        "than they should. The HEART may beat a little faster at onset, "
        "then settle into a heavy, deliberate rhythm. None of these signals "
        "is unique to guilt - bodies reuse the same hardware for many "
        "feelings - but the CLUSTER is the signature: chest weight plus "
        "stomach knot plus heat in the face plus restless hands, all "
        "arriving together with a replaying mind. Learn the cluster and "
        "you can catch guilt in yourself before the replay has run ten "
        "laps."),
    how_it_works=(
        "Each signal traces to the appraisal machinery. Chest tightness and "
        "shallow breathing come from mild sympathetic arousal - the body's "
        "urgency system marking the breach as important, though far below "
        "fight-or-flight levels. The stomach knot is the gut-brain axis "
        "responding to the same arousal; digestion is deprioritized when "
        "the mind declares something urgent. Shoulder and jaw tension are "
        "preparatory bracing - the body readying for the social cost it "
        "anticipates (the hard conversation, the confession). Blushing is "
        "the most socially interesting signal: blood vessel dilation in the "
        "face is involuntary and visible, which is exactly why researchers "
        "treat it as an appeasement display - the body signaling "
        "remorsefulness to others without words. Restless hands are "
        "displacement activity, leftover motor energy from an approach urge "
        "(go repair) that has no immediate outlet. The weighted fatigue is "
        "attentional: the replay loop consumes working memory, leaving "
        "less for everything else, which the body reads as heaviness. "
        "Damasio's somatic-marker view fits here: the body isn't just "
        "accompanying guilt, it's part of how the mind WEIGHS the breach."),
    key_points=[
        "Guilt's cluster: chest weight + stomach knot + face heat + restless hands + shallow breath + weighted fatigue.",
        "Blushing is involuntary and visible - researchers read it as the body's wordless remorse signal to others.",
        "No single signal is unique to guilt; the CLUSTER arriving with a replaying mind is the signature.",
        "Restless hands are displacement: the repair urge's motor energy with nowhere to go.",
        "The body is part of the weighing, not just decoration - heaviness tracks how seriously the mind takes the breach.",
    ],
    requirements=[
        "Head-to-toe body tour in plain felt language",
        "Each signal given a plain-words mechanism",
        "Blushing explained as social signal",
        "The cluster-not-single-signal point made explicit",
        "No diagnostic language anywhere in the record",
    ],
    standards=["Damasio on somatic markers; Scherer on response patterning"],
    citations=[CIT_DAMASIO, CIT_SCHERER, CIT_KELTNER],
    sig_lens=(
        "The Signature lens reads the body as the ledger's alarm system: "
        "the chest weight is the red entry pressing through the page, the "
        "blush is the ledger glowing where others can see it, restless "
        "hands are the accountant's fingers drumming for the balancing "
        "pen. His observation: the body never lies about the books - it "
        "posts the entry before the mind finishes writing it. Clearly "
        "labeled Signature-made, never presented as authentic public "
        "record."),
),
dict(
    key="guilt_posture_movement", name="Posture and Movement: How the Body Carries Guilt",
    group="Compounded", ladder_rank=4, ladder_tier="compounded",
    description=(
        "You can often see guilt from across the room before a word is "
        "spoken, because the body carries it in a recognizable posture. "
        "The SHOULDERS round forward and draw inward, as if making the "
        "torso a smaller target. The HEAD tips down and slightly to one "
        "side - not the bowed head of grief, but a tilted, averted hang, "
        "as if the neck agreed with the verdict. The GAZE drops or slides "
        "away; sustained eye contact becomes difficult, and when it "
        "happens it flickers. The body takes up LESS SPACE: arms cross or "
        "fold close, legs draw together, the person angles slightly away "
        "rather than squaring up. HANDS stay busy - touching the face, "
        "rubbing the neck, picking at sleeves - self-soothing gestures "
        "that also keep the hands from hanging accused at the sides. "
        "MOVEMENT slows and shrinks: steps get shorter, gestures get "
        "smaller, the person seems to move as if trying not to disturb the "
        "air. In conversation, the guilty body LEANS BACK fractionally at "
        "the moment of the difficult sentence, then leans in with the "
        "repair - the posture itself acting out approach and avoidance. "
        "None of this is deliberate; ask a guilty-feeling person to stand "
        "tall and meet your eyes and they can do it for about ten seconds "
        "before the posture sags back. The body keeps the score it was "
        "given."),
    how_it_works=(
        "The guilt posture is the body acting out the appraisal. Making "
        "oneself smaller is appeasement: across social species, reducing "
        "size and averting gaze signals non-threat and submission, which "
        "is exactly what a mind that believes it harmed someone wants to "
        "broadcast. The averted gaze has a second function - it reduces "
        "input: the face of the person harmed is the strongest trigger "
        "for the replay loop, so looking away is the body's attempt to "
        "turn down the stimulus. Self-touch (face, neck, arms) is "
        "self-soothing that also occupies the hands, discharging the "
        "restless motor energy described in the body-signals record. The "
        "lean-back-then-lean-in pattern during confession mirrors the "
        "underlying urges precisely: withdrawal from the anticipated "
        "social cost, then approach toward the repair. Keltner and "
        "Buswell's work on appeasement displays in embarrassment extends "
        "naturally here - guilt's posture is the body negotiating for "
        "forgiveness before the mouth has found the words."),
    key_points=[
        "The guilt posture: rounded shoulders, tilted-down head, averted flickering gaze, smaller footprint, busy self-soothing hands.",
        "Making oneself smaller is appeasement - the body broadcasting non-threat to the person harmed.",
        "Averted gaze reduces input: the harmed person's face fuels the replay loop, so the body looks away to turn it down.",
        "Movement shrinks: shorter steps, smaller gestures, as if trying not to disturb the air.",
        "The lean-back-then-lean-in during confession acts out withdrawal-then-approach in the body itself.",
    ],
    requirements=[
        "Full-body posture portrait in observable detail",
        "Movement changes described, not just static posture",
        "Appeasement function explained in plain words",
        "No diagnostic language anywhere in the record",
    ],
    standards=["Keltner and Buswell on appeasement displays"],
    citations=[CIT_KELTNER, CIT_EKMAN],
    sig_lens=(
        "The Signature lens reads the posture as the ledger made visible: "
        "rounded shoulders are pages curling inward to hide the red "
        "entry, the averted gaze is the accountant unable to meet the "
        "auditor's eyes, the lean-in at the repair is the books being "
        "opened voluntarily. His note: the body confesses before the "
        "mouth does - watch the shoulders and you read the ledger. "
        "Clearly labeled Signature-made, never presented as authentic "
        "public record."),
),
dict(
    key="guilt_sleep_appetite_energy", name="Sleep, Appetite, and Energy Under Guilt",
    group="Compounded", ladder_rank=5, ladder_tier="compounded",
    description=(
        "Guilt is a nighttime emotion - it waits for the lights to go out. "
        "SLEEP is where guilt hits hardest, because the replay loop loves "
        "a quiet dark room with no competition. The pattern is familiar: "
        "exhausted all evening, wired the moment the head hits the pillow, "
        "the day's breach replaying in high definition at 1 a.m., then at "
        "2:30, then at 4. Falling asleep is the problem more than staying "
        "asleep - the mind will not grant unconsciousness while an account "
        "feels unsettled. APPETITE usually drops first: the knotted "
        "stomach from the body-signals record has no interest in food, and "
        "meals get pushed around the plate. In some people the pattern "
        "flips - eating becomes the quickest available self-soothing, and "
        "the guilt then recruits the eating itself as fresh material ('I "
        "have no discipline either'). ENERGY follows attention: because "
        "the replay loop is running constantly in the background, working "
        "memory is crowded, and everything else feels effortful. People "
        "describe it as 'running with a weighted vest' - the day's tasks "
        "are the same, but each costs more. The cruel loop: poor sleep "
        "worsens the next day's emotional regulation, which makes the "
        "guilt feel bigger, which worsens the next night's sleep. Breaking "
        "it rarely requires fixing the sleep directly - settling the "
        "account, even partially (the apology sent, the plan made), quiets "
        "the loop more reliably than any bedtime routine."),
    how_it_works=(
        "The sleep effect is attentional competition. Sleep onset needs "
        "the mind's arousal to fall below a threshold; the replay loop is "
        "a high-arousal process (unresolved breach plus approach urge), so "
        "it holds arousal above the threshold - the exhausted-but-wired "
        "pattern. Appetite suppression runs through the gut-brain axis: "
        "sympathetic arousal deprioritizes digestion, and nausea is the "
        "extreme end of the same signal. The flipped pattern (eating for "
        "soothing) is the repair urge displaced onto the nearest "
        "available reward. Energy drain is working-memory economics: the "
        "replay loop occupies the same limited workspace that daily tasks "
        "need, so everything else runs slower and feels heavier - Gross's "
        "work on regulation costs applies directly, since suppressing or "
        "managing the feeling all day is itself expensive. The "
        "sleep-guilt-sleep loop is a positive feedback cycle, which is why "
        "it escalates: each night of poor sleep lowers the next day's "
        "threshold for intense feeling, raising the volume on the same "
        "breach."),
    key_points=[
        "Guilt is a nighttime emotion: the replay loop loves a quiet dark room, making sleep onset the hardest part.",
        "Appetite usually drops (knotted stomach); in some it flips to soothing-eating, which guilt then recruits as fresh material.",
        "Energy drains because the replay loop crowds working memory - everything costs more, like a weighted vest.",
        "Poor sleep lowers the next day's threshold, making the same guilt feel bigger: a feedback loop.",
        "Settling the account (even partially) quiets the loop more reliably than targeting sleep directly.",
    ],
    requirements=[
        "Sleep, appetite, and energy each covered as lived experience",
        "The exhausted-but-wired pattern explained",
        "The feedback loop described plainly",
        "No diagnostic language anywhere in the record",
    ],
    standards=["Gross on emotion regulation costs and sleep"],
    citations=[CIT_GROSS, CIT_DAMASIO],
    sig_lens=(
        "The Signature lens reads the night as the ledger's overtime "
        "shift: with the day's noise gone, the accountant works the red "
        "entry under a single lamp - which is why 2 a.m. guilt feels "
        "larger than noon guilt over the same act. His counsel: do the "
        "day's balancing before dark, because the night clerk charges "
        "double and never approves the books. Clearly labeled "
        "Signature-made, never presented as authentic public record."),
),
dict(
    key="guilt_body_differences", name="No Two Bodies Alike: How Guilt's Signals Differ Between People",
    group="Compounded", ladder_rank=5, ladder_tier="compounded",
    description=(
        "Everything in the body-signals record is a tendency, not a law - "
        "because no two bodies run guilt the same way. Some people feel "
        "guilt almost entirely in the GUT: nausea, churning, appetite gone, "
        "while their chest feels fine. Others feel it in the CHEST and "
        "throat: tightness, a lump that won't swallow, while their stomach "
        "is unbothered. Some go HOT - blushing, sweating, face burning. "
        "Others go COLD - hands icy, a chill under the ribs. Some get "
        "restless and fidgety; others go still and heavy, barely moving "
        "for hours. TEMPERAMENT sets the baseline: high-reactivity people "
        "feel every signal louder, low-reactivity people feel the same "
        "guilt as a quiet pressure with little body noise. UPBRINGING "
        "tunes the instrument: in families where mistakes were met with "
        "warmth and repair, the body learned guilt as a mild nudge; in "
        "families where mistakes were met with fury or cold silence, the "
        "body learned guilt as a full alarm, and it still fires that way "
        "decades later over small things. CULTURE writes the display "
        "rules: some cultures expect visible remorse (the signals are "
        "allowed out), others prize composure (the signals get driven "
        "inward, where they show up as stomach trouble or tension "
        "headaches). AGE matters too: children's guilt is loud and "
        "physical - crying, clinging, tummy aches - while adults have "
        "usually learned to route it into quieter channels. The practical "
        "point: never use someone else's body as the template for your "
        "own. Learn YOUR cluster - where YOU feel it first, how YOUR "
        "signals scale - and you'll read yourself faster than any general "
        "description can."),
    how_it_works=(
        "The variation comes from three layers. The bottom layer is "
        "physiology: autonomic reactivity differs between people the way "
        "eyesight does - some nervous systems simply amplify more. The "
        "middle layer is learning history: Scherer's response-patterning "
        "work shows that emotional responses are tuned by repeated "
        "experience, so a childhood of harsh punishment wires a hair-trigger "
        "guilt body, while a childhood of calm repair wires a "
        "proportionate one. The top layer is display rules - Ekman's term "
        "for the cultural and family norms about which feelings may show "
        "where. Display rules don't erase the signal; they reroute it. A "
        "person taught never to show distress won't blush less - they'll "
        "feel it as a stomach knot instead, because the arousal has to go "
        "somewhere. This is why the record insists on the cluster idea "
        "rather than a checklist: the reliable move is learning your own "
        "pattern across several episodes, not matching a universal list."),
    key_points=[
        "Guilt's body varies: gut people, chest people, hot responders, cold responders, fidgeters, freezers.",
        "Temperament sets the volume knob; upbringing tunes what the alarm learned to mean.",
        "Display rules reroute signals rather than erasing them - suppressed blushing often becomes a stomach knot.",
        "Children's guilt is loud and physical; adults route it into quieter channels.",
        "Learn YOUR cluster across several episodes instead of matching a universal checklist.",
    ],
    requirements=[
        "Multiple variation axes: physiology, temperament, upbringing, culture, age",
        "The rerouting-not-erasing point about display rules",
        "Practical takeaway: learn your own cluster",
        "No diagnostic language anywhere in the record",
    ],
    standards=["Ekman on display rules; Scherer on response patterning"],
    citations=[CIT_EKMAN, CIT_SCHERER],
    sig_lens=(
        "The Signature lens reads bodily differences as different ledger "
        "bindings: some books are bound in gut-leather, some in "
        "chest-vellum - the entries are the same, the covers differ. "
        "Upbringing is the bindery where the cover was tooled: harsh "
        "hands stamp the alarm deep. His instruction: read your own "
        "binding, not your neighbor's - the entries are yours either way. "
        "Clearly labeled Signature-made, never presented as authentic "
        "public record."),
),
# ------------------------------------------------- 14-17: facial expression
dict(
    key="guilt_facial_expression", name="The Face of Guilt: Eyes, Brows, Mouth, and Micro-Signs",
    group="Compounded", ladder_rank=5, ladder_tier="compounded",
    description=(
        "Guilt's face is quiet - it doesn't announce itself like a grin "
        "or a sob, which is why you have to know where to look. The EYES "
        "lead: gaze drops or slides sideways, and when eye contact happens "
        "it is brief and flickering - held a beat too short, released a "
        "beat too early. The eyelids may lower slightly, hooding the eyes "
        "as if to dim the scene. The BROWS tell the subtlest story: the "
        "inner corners lift a fraction, borrowing the brow shape of "
        "sadness - the 'please forgive' brow that appears for a second "
        "when the difficult sentence is spoken. The MOUTH is the busiest "
        "part: lips press together and thin out, or pull down at the "
        "corners; lip-biting and lip-licking appear in waves; some people "
        "cover the mouth briefly with fingers at the exact moment of "
        "confession, as if the hand tried to take the words back. The "
        "micro-signs are where guilt hides in plain sight: a quick "
        "swallow before the hard sentence, a single slow blink held a "
        "moment too long, the jaw tightening then releasing, a blush "
        "blooming from the cheeks outward. Watch a person saying 'I'm "
        "sorry' and you'll often see the whole sequence in three seconds: "
        "gaze drops, inner brows lift, lips press, blush rises, swallow. "
        "It is not a mask the face wears - it is the face negotiating in "
        "real time between the urge to hide and the urge to repair."),
    how_it_works=(
        "Each facial element traces to the underlying urges. Gaze aversion "
        "is the withdrawal component: looking away from the harmed "
        "person's face reduces the strongest trigger of the replay loop. "
        "The inner-brow raise is shared with sadness and functions as an "
        "appeasement signal - Keltner and Buswell's appeasement work shows "
        "these displays evolved to deflect aggression and invite "
        "reconciliation, which is precisely what a guilty mind wants. Lip "
        "pressing and biting are self-directed tension behaviors: the "
        "mouth is where the confession must exit, so tension pools there. "
        "The hand-to-mouth cover is the most literal gesture in the set - "
        "the body physically attempting to retract the words. Blushing is "
        "involuntary vasodilation, impossible to fake and hard to suppress, "
        "which is why observers instinctively trust it: the face is "
        "showing a signal the person didn't choose to send. Ekman's "
        "micro-expression research applies here with a caveat - guilt has "
        "no single universal 'guilt face' the way fear does; what it has "
        "is this reliable cluster of appeasement and tension signs "
        "arriving together."),
    key_points=[
        "Eyes: dropped, sliding, flickering contact - held a beat too short, released a beat too early.",
        "Inner brows lift a fraction (the 'please forgive' brow); mouth presses, thins, bites, or gets briefly covered.",
        "Micro-signs: the pre-confession swallow, the overlong slow blink, jaw tighten-release, the blooming blush.",
        "Blushing can't be faked or easily suppressed - observers instinctively trust it for that reason.",
        "Guilt has no single universal face; it has a reliable CLUSTER of appeasement-plus-tension signs.",
    ],
    requirements=[
        "Eyes, brows, and mouth each described in observable detail",
        "Micro-signs listed as a watchable sequence",
        "The no-single-guilt-face caveat stated",
        "No diagnostic language anywhere in the record",
    ],
    standards=["Ekman on facial expression; Keltner and Buswell on appeasement"],
    citations=[CIT_EKMAN, CIT_KELTNER],
    sig_lens=(
        "The Signature lens reads the guilty face as the ledger held up "
        "to the light: the dropped gaze is the page turned down, the "
        "lifted inner brow is the margin note pleading 'read kindly,' the "
        "blush is the red entry glowing through the paper for all to see. "
        "His note to the observer: the face is already confessing - "
        "listening is the only audit required. Clearly labeled "
        "Signature-made, never presented as authentic public record."),
),
dict(
    key="guilt_expression_intensity", name="How Guilt's Expression Changes With Intensity",
    group="Compounded", ladder_rank=6, ladder_tier="compounded",
    description=(
        "The face of guilt is not one face but a dimmer switch. At LOW "
        "intensity, the signs are fleeting and easy to miss: a half-second "
        "gaze dip when the topic brushes the breach, a quick lip press "
        "that releases, a blush so faint it could be the room's warmth. "
        "The person recovers instantly - the expression flashes and the "
        "normal face returns, because the appraisal underneath is light. "
        "Observers usually register nothing; the person themselves may not "
        "notice they showed anything. At MODERATE intensity, the signs "
        "sustain: the gaze stays down through whole sentences, the inner "
        "brows hold their lift, lip-biting comes in waves, the blush is "
        "unmistakable. The voice joins in - softer, slower, with small "
        "pauses before the hard words. This is the face people picture when "
        "they picture guilt: readable, sustained, clearly costing the "
        "person something. At HIGH intensity, the expression can paradoxically "
        "go FLAT: the face empties, the eyes fix on nothing, the mouth "
        "sets in a still line. This isn't calm - it's overload. The "
        "appraisal is so heavy that the expressive system shuts down to "
        "protect itself, the way a circuit breaker trips. Watch for the "
        "leakage around the flatness: the hands still fidget, the swallow "
        "still comes, the breathing stays shallow. Readers of faces make "
        "two classic errors: missing low-intensity guilt entirely (it "
        "flashes past), and misreading high-intensity flatness as "
        "indifference (it's the opposite - the feeling is so big the face "
        "gave up showing it)."),
    how_it_works=(
        "The dimmer-switch pattern follows arousal and regulation. Low "
        "intensity means low arousal plus successful regulation - the "
        "expression system fires briefly and the person damps it without "
        "effort, so only flashes escape. Moderate intensity means the "
        "arousal exceeds easy regulation: the signals sustain because the "
        "damping can't keep up, which is why moderate guilt is the most "
        "readable - the system is working at full visible capacity. High "
        "intensity triggers protective shutdown: when arousal passes a "
        "threshold, the expressive muscles go still - a freeze-adjacent "
        "response that conserves resources. The leakage (hands, swallow, "
        "breath) continues because those channels are harder to shut down "
        "voluntarily than the face. This is why the flat face of intense "
        "guilt fools observers: people expect expression to scale linearly "
        "with feeling, but the system is non-linear - it shows more, then "
        "more, then suddenly shows nothing while feeling everything."),
    key_points=[
        "Low intensity: fleeting flashes - half-second gaze dips, quick lip presses - easy to miss entirely.",
        "Moderate intensity: sustained and readable - downcast gaze, lifted inner brows, waves of lip-biting, unmistakable blush.",
        "High intensity: paradoxical flatness - the face empties under overload while the hands and breath keep leaking.",
        "Two classic observer errors: missing low-intensity flashes, and misreading high-intensity flatness as indifference.",
        "Expression doesn't scale linearly with feeling: it shows more, then more, then suddenly nothing.",
    ],
    requirements=[
        "Three intensities with distinct observable faces",
        "The high-intensity flatness paradox explained",
        "The two classic observer errors named",
        "No diagnostic language anywhere in the record",
    ],
    standards=["Ekman on expression intensity; Scherer on response patterning"],
    citations=[CIT_EKMAN, CIT_SCHERER],
    sig_lens=(
        "The Signature lens reads the dimmer switch as the ledger's "
        "visibility settings: low intensity is pencil in the margin, "
        "moderate is red ink on the page, high intensity is the book "
        "slammed shut - not because the entry vanished, but because the "
        "accountant cannot bear to look at it yet. His warning to readers "
        "of faces: the slammed book holds the largest debt. Clearly "
        "labeled Signature-made, never presented as authentic public "
        "record."),
),
dict(
    key="guilt_hiding_faking", name="Hiding and Faking Guilt: What Leaks Through",
    group="Compounded", ladder_rank=6, ladder_tier="compounded",
    description=(
        "People try to hide guilt constantly - at work, in arguments, in "
        "front of the mirror - and the attempts follow recognizable "
        "scripts. The most common is OVERCOMPENSATION: excessive cheer, "
        "loud laughter, sudden generosity, all tuned a notch too high. It "
        "reads as wrong because it is: the energy is performing "
        "innocence rather than feeling anything. Next is DEFLECTION: "
        "changing the subject with suspicious speed, answering a question "
        "with a joke, getting busy with sudden urgent tasks when the "
        "topic nears the breach. Then there's the FLAT DENIAL face - "
        "studied neutrality, even breathing, direct eye contact held a "
        "beat too long (real ease doesn't try this hard). What LEAKS "
        "through despite all of it: the timing is off - the laugh comes "
        "half a second late, the subject-change lands too hard. The hands "
        "keep their own counsel - fidgeting under the table while the face "
        "smiles above it. The blush cannot be negotiated with; it arrives "
        "on its own schedule. And the voice betrays what the face hides: "
        "pitch rises slightly, speech speeds up, or the person over-explains "
        "with three reasons where one would do. FAKING guilt - performing "
        "remorse you don't feel - fails in the opposite direction: it's "
        "too smooth. Real guilt stumbles, pauses, swallows, loses the "
        "thread; performed guilt flows like a rehearsed speech because it "
        "is one. The irony observers should know: the harder someone works "
        "to look innocent, the more the leakage shows - effort itself is "
        "the tell."),
    how_it_works=(
        "Hiding fails because expression is multi-channel and "
        "regulation is single-focus. A person can control the face OR the "
        "hands OR the voice with effort, but not all three at once - "
        "attention is limited, so the unguarded channels leak. This is "
        "Ekman's leakage hypothesis applied to guilt: the channels hardest "
        "to control voluntarily (blushing, voice pitch, hand fidgeting) "
        "are the most honest. Overcompensation fails for a subtler reason: "
        "it mismatches the context's emotional baseline - cheer at the "
        "wrong volume reads as protest, and observers detect the mismatch "
        "even when they can't name it. Faked guilt fails because genuine "
        "guilt disrupts fluency: the real appraisal is still cycling, "
        "which produces pauses, restarts, and swallows - disfluencies "
        "that a performer, running no such cycle, doesn't produce. The "
        "practical upshot for readers of people: don't watch the channel "
        "they're managing (usually the face); watch the channels they "
        "forgot (hands, timing, voice)."),
    key_points=[
        "Common hiding scripts: overcompensation (cheer tuned too high), deflection (suspicious subject changes), studied flat neutrality.",
        "Leakage points: off timing, fidgeting hands under a smiling face, the un-negotiable blush, rising voice pitch, over-explaining.",
        "Faked guilt is too smooth - real guilt stumbles, pauses, swallows; performance flows because no real appraisal is cycling.",
        "Hiding fails because regulation is single-focus but expression is multi-channel; the unguarded channels leak.",
        "Read the channels they forgot (hands, timing, voice), not the one they're managing (the face).",
    ],
    requirements=[
        "Hiding scripts and faking both covered with observable tells",
        "The multi-channel leakage mechanism explained plainly",
        "Why faked guilt looks too smooth",
        "No diagnostic language anywhere in the record",
    ],
    standards=["Ekman on leakage and deception cues"],
    citations=[CIT_EKMAN, CIT_KELTNER],
    sig_lens=(
        "The Signature lens reads hiding as the accountant cooking the "
        "visible books while the real ledger bleeds through the pages: "
        "the smiling face is the forged summary, the fidgeting hands are "
        "the true entries showing through thin paper. His dry note: a "
        "forged book always smells of fresh ink - effort is the scent. "
        "Clearly labeled Signature-made, never presented as authentic "
        "public record."),
),
dict(
    key="guilt_expression_gallery", name="Expression Gallery: Describing Guilt So an Artist or Actor Could Play It",
    group="Compounded", ladder_rank=6, ladder_tier="compounded",
    description=(
        "FOR THE ARTIST - draw guilt in three studies. STUDY ONE, the "
        "quiet admission: head tilted down ten degrees and turned a "
        "quarter away; eyes looking down-left, lids lowered; inner brow "
        "corners lifted just enough to crease the forehead's center; lips "
        "pressed thin, corners pulled down a fraction; a faint blush high "
        "on the cheeks. STUDY TWO, the confession moment: hand half-raised "
        "toward the mouth, fingers not quite touching the lips; gaze "
        "flicking up for one frame of eye contact then dropping; shoulders "
        "rolled forward; the whole torso angled slightly away as if the "
        "body apologized for its own size. STUDY THREE, the heavy "
        "carrying: seated, elbows on knees, head in hands but fingers "
        "splayed so the eyes show through - exhausted, not weeping; the "
        "mouth a flat line; everything about the pose saying 'the weight "
        "is still there.' FOR THE ACTOR - play guilt from the breath "
        "outward. Start with the swallow: let the throat work once before "
        "the hard line. Drop the gaze on the verb that names what you did "
        "- not before, not after, ON the verb. Press the lips together "
        "during the other person's reply, as if holding words back. Let "
        "the hands find the face or the sleeve without being told. The "
        "voice: softer than your scene partner expects, with a pause "
        "before the apology that you do NOT fill - let the silence do the "
        "work. The cardinal rule for both: guilt never performs itself. "
        "The moment it looks acted, it's shame or theater. Guilt on a face "
        "is always the face trying NOT to show something and failing by "
        "degrees."),
    how_it_works=(
        "The gallery notes are a translation layer: they convert the "
        "research findings of the previous three records into drawable, "
        "playable instructions. Each direction encodes a mechanism. The "
        "ten-degree head tilt and quarter-turn encode appeasement "
        "miniaturization. The gaze dropping ON the verb encodes the "
        "withdrawal reflex firing at the moment of maximum self-exposure. "
        "The pre-line swallow encodes the throat tension of anticipated "
        "social cost. The unfilled pause encodes the approach-avoidance "
        "freeze - the body caught between confessing and fleeing, which "
        "reads as authenticity because it IS the real conflict made "
        "visible. The 'never performs itself' rule encodes the "
        "disfluency finding: genuine guilt disrupts smooth expression, "
        "so any polished performance reads as false. For artists, the "
        "three studies map the intensity curve from the previous record: "
        "study one is low-moderate, study two is moderate, study three is "
        "the high-intensity flatness rendered as exhaustion."),
    key_points=[
        "Artist: three studies - quiet admission (tilted head, lifted inner brows, faint blush), confession (hand to mouth, flickering gaze), heavy carrying (head in hands, flat mouth).",
        "Actor: play from the breath outward - the pre-line swallow, gaze dropping ON the verb, the unfilled pause before the apology.",
        "The cardinal rule: guilt never performs itself; polished delivery reads as false because real guilt disrupts fluency.",
        "Every direction encodes a mechanism: appeasement, withdrawal reflex, throat tension, approach-avoidance freeze.",
        "The studies map the intensity curve: low-moderate, moderate, and high-intensity flatness as exhaustion.",
    ],
    requirements=[
        "Drawable instructions for an artist (three studies)",
        "Playable instructions for an actor (breath, gaze, voice, pause)",
        "The authenticity rule stated and explained",
        "No diagnostic language anywhere in the record",
    ],
    standards=["Ekman on expression; Keltner and Buswell on appeasement displays"],
    citations=[CIT_EKMAN, CIT_KELTNER],
    sig_lens=(
        "The Signature lens hands the artist his own brief: draw the "
        "ledger, not the criminal - the tilted head is the page canted "
        "toward the light, the hand at the mouth is the accountant "
        "stalling the entry, the head in hands is the books too heavy to "
        "close. His direction in one line: show the hiding, and the "
        "feeling shows itself. Clearly labeled Signature-made, never "
        "presented as authentic public record."),
),
# ------------------------------------------------- 18-21: triggers
dict(
    key="guilt_classic_triggers", name="The Classic Triggers: What Commonly Sets Guilt Off",
    group="Compounded", ladder_rank=6, ladder_tier="compounded",
    description=(
        "Guilt has a greatest-hits list of triggers - the situations that "
        "set it off in most people, most of the time. HARMING SOMEONE is "
        "the headliner: saying the cruel thing, the careless mistake that "
        "cost someone, the physical bump that was your fault. BREAKING A "
        "PROMISE runs a close second: the commitment made sincerely and "
        "kept casually - the call not made, the help not given, the "
        "deadline let slide while someone waited. LYING, even small: the "
        "white lie that worked too well, the omission that felt like "
        "protection at the time and feels like betrayal later. NEGLECTING "
        "someone who needed you: the parent not visited, the friend in a "
        "hard season you meant to check on, the child handed a screen "
        "instead of attention. TAKING MORE THAN YOUR SHARE: the last "
        "slice, the credit for shared work, the advantage you didn't "
        "quite earn. VIOLATING YOUR OWN CODE: the diet broken, the temper "
        "lost, the value preached but not practiced - guilt doesn't need "
        "another person to fire, only a standard you hold. BENEFITING FROM "
        "ANOTHER'S LOSS: the promotion that came from a colleague's "
        "stumble, the good fortune that arrived while others struggled. "
        "What unites the list: each trigger runs the three-beat appraisal "
        "cleanly - a standard you endorse, a breach you can point to, and "
        "responsibility you can't talk your way out of. Learn the list and "
        "you'll recognize the onset of guilt in the wild within seconds, "
        "which is early enough to choose the response instead of being "
        "chosen by it."),
    how_it_works=(
        "Classic triggers are classic because they satisfy the appraisal "
        "with minimum ambiguity. Harming someone delivers all three beats "
        "at once: the standard (don't hurt people) is universal, the "
        "breach is observable, and responsibility is hard to dodge. "
        "Promise-breaking is potent because the standard was EXPLICITLY "
        "set by the person themselves - self-authored standards produce "
        "stronger guilt than inherited ones, since there's no one else to "
        "blame for the rule. Neglect triggers work through omission: the "
        "appraisal counts failures to act, not just acts, which is why "
        "'I didn't do anything' is no defense against guilt. "
        "Benefiting-from-loss triggers fire through the closeness dial: "
        "the better you know the loser, the louder the guilt. "
        "Self-code violations show the appraisal needs no victim at all - "
        "the 'other' can be your own future self or your own values. "
        "Baumeister's interpersonal account predicts exactly this "
        "ranking: the triggers that most threaten bonds produce the most "
        "guilt, because guilt's job is bond maintenance."),
    key_points=[
        "The greatest-hits list: harming, promise-breaking, lying, neglecting, taking more than fair share, violating your own code, benefiting from another's loss.",
        "Classic triggers run the three-beat appraisal with minimum ambiguity - standard, breach, and responsibility all obvious.",
        "Self-authored standards (promises YOU made) produce stronger guilt than inherited rules.",
        "Omissions count: 'I didn't do anything' is no defense - the appraisal scores failures to act.",
        "Guilt needs no victim: violating your own code fires it with only your values as the 'other.'",
    ],
    requirements=[
        "At least six classic triggers, each with a concrete example",
        "Why these triggers are 'classic' explained via the appraisal",
        "Omissions explicitly covered",
        "No diagnostic language anywhere in the record",
    ],
    standards=["Baumeister and colleagues on interpersonal triggers of guilt"],
    citations=[CIT_BAUMEISTER, CIT_LAZARUS],
    sig_lens=(
        "The Signature lens files the classic triggers as the ledger's "
        "standard chart of accounts: harm is filed under Damages, broken "
        "promises under Debts Owed, neglect under Accounts Unattended. His "
        "observation: every classic trigger is an entry the accountant "
        "cannot lose - the books are designed so these post themselves. "
        "Clearly labeled Signature-made, never presented as authentic "
        "public record."),
),
dict(
    key="guilt_personal_triggers", name="Personal Triggers: Memories, Anniversaries, and Private Associations",
    group="Compounded", ladder_rank=7, ladder_tier="compounded",
    description=(
        "Beyond the classics, everyone carries a private trigger map - "
        "guilt buttons installed by their own history that no general list "
        "could predict. The SONG that was playing when the bad news came; "
        "hearing it in a store can drop the whole scene back into the "
        "chest in four bars. The DATE on the calendar: the anniversary of "
        "the argument, the birthday of someone no longer spoken to, the "
        "season when it happened - autumn light through a particular "
        "window. The PLACE: the restaurant, the street corner, the room "
        "in a house you still have to walk through. The OBJECT: the gift "
        "never thanked-for sitting in a drawer, the sweater borrowed and "
        "never returned, now unwearable for the memory sewn into it. The "
        "PHRASE: words someone said - 'I thought I could count on you' - "
        "that now echo whenever anyone says anything faintly similar. The "
        "RITUAL missed: the call every Sunday that stopped, the grave not "
        "visited, the tradition you let lapse and now can't restart "
        "without announcing the lapse. Personal triggers are powerful "
        "precisely because they're PRIVATE: nobody else knows why you went "
        "quiet when that song came on, which means no one can talk you "
        "out of it in the moment. They also don't fade on schedule - a "
        "personal trigger can fire at full strength twenty years later, "
        "because it was never the event alone being stored, it was the "
        "unresolved appraisal attached to it. Mapping your own triggers - "
        "actually writing them down - is one of the highest-leverage "
        "exercises in this database: a trigger you can name is a trigger "
        "you can prepare for."),
    how_it_works=(
        "Personal triggers are cue-triggered appraisal retrievals. When "
        "the original breach was never fully repaired or reassessed, the "
        "memory network stores the event WITH its appraisal tags - "
        "standard, breach, responsibility - still active. A matching cue "
        "(song, date, place) reactivates the whole network, and the "
        "appraisal re-fires as if the event were present. This is the "
        "aftershock mechanism from the time-course record, specialized: "
        "aftershocks are generic echoes, personal triggers are the "
        "specific cues wired to YOUR unresolved entries. They resist "
        "fading because each firing re-encodes the memory - the loop "
        "refreshes its own storage. Writing them down works through "
        "externalization: a trigger held in working memory ambushes; a "
        "trigger on paper becomes a forecast ('Thursday is the "
        "anniversary; I'll feel it at dinner') and forecasts can be "
        "prepared for. Preparation doesn't prevent the feeling - it "
        "prevents the feeling from driving."),
    key_points=[
        "Private trigger map: songs, dates, places, objects, phrases, missed rituals - installed by your own history.",
        "Personal triggers are powerful because they're private: no one else knows why you went quiet, so no one can talk you down in the moment.",
        "They fire at full strength years later because the memory stored the UNRESOLVED appraisal, not just the event.",
        "Each firing re-encodes the memory - the loop refreshes its own storage, resisting fade.",
        "Write them down: a named trigger becomes a forecast, and forecasts can be prepared for.",
    ],
    requirements=[
        "At least five categories of personal trigger with concrete examples",
        "Why they stay potent for years, explained",
        "The write-them-down exercise with its mechanism",
        "No diagnostic language anywhere in the record",
    ],
    standards=["Lazarus on appraisal and memory; Gross on cue-triggered emotion"],
    citations=[CIT_LAZARUS, CIT_GROSS],
    sig_lens=(
        "The Signature lens files personal triggers as the ledger's "
        "dog-eared pages: the song is a page corner folded down, the "
        "anniversary is a date circled in red that the calendar keeps "
        "returning to. His practice: unfold the corners deliberately, one "
        "at a time, in daylight - a page reviewed on purpose loses its "
        "power to ambush. Clearly labeled Signature-made, never presented "
        "as authentic public record."),
),
dict(
    key="guilt_surprise_triggers", name="Surprise Triggers: The Unexpected Things That Set Guilt Off",
    group="Compounded", ladder_rank=7, ladder_tier="compounded",
    description=(
        "Some guilt arrives from directions nobody expects, and the "
        "surprise itself becomes part of the sting - 'why do I feel guilty "
        "about THAT?' GOOD FORTUNE guilt: the promotion landed, the "
        "diagnosis was benign, the storm missed your house - and instead "
        "of pure relief there's a shadow: why me and not them? RESTING "
        "guilt: the day off while colleagues grind, the nap while the "
        "to-do list glares - rest itself feels like theft. OUTGROWING "
        "guilt: the friendship you quietly left, the hometown you don't "
        "miss, the beliefs you shed - growth feels like betrayal of the "
        "people still where you were. LAUGHING guilt: catching yourself "
        "laughing at something funny during a hard season - as if joy were "
        "disloyal to the seriousness of the situation. BEING HELPED "
        "guilt: someone carries your bag, covers your shift, forgives you "
        "fast - and their kindness feels like a debt you didn't agree to. "
        "SAYING NO guilt: the boundary set cleanly and kindly still rings "
        "the alarm, because the standard 'always be available' was never "
        "officially repealed. NOT FEELING WORSE guilt: the meta-level "
        "oddity - feeling guilty that you're not guilty ENOUGH about "
        "something, as if insufficient ache proved insufficient care. What "
        "unites them: each fires the appraisal through a SIDE DOOR. The "
        "standard isn't 'don't harm' but some quieter rule - 'don't have "
        "more,' 'don't rest while others work,' 'don't leave people "
        "behind,' 'take nothing you can't repay.' Surprise triggers "
        "reveal the standards you didn't know you held - which makes them "
        "diagnostically precious: each one maps a hidden rule, and hidden "
        "rules can be examined, kept, or repealed once they're visible."),
    how_it_works=(
        "Surprise triggers work because the appraisal system runs "
        "standards the conscious mind never filed. Festinger's "
        "dissonance work is the ancestor here: the mind holds many "
        "evaluative rules implicitly, and guilt fires when behavior "
        "collides with one - even if the person couldn't have stated the "
        "rule beforehand. Good-fortune guilt collides with an implicit "
        "fairness rule ('good things should be evenly spread'); resting "
        "guilt collides with an internalized industriousness rule; "
        "outgrowing guilt collides with a loyalty rule that treats change "
        "as abandonment. The meta-guilt case ('not guilty enough') is the "
        "system auditing ITSELF - the appraisal turned on its own output, "
        "using ache as a proxy for caring. The practical move with "
        "surprise triggers is always the same: drag the hidden rule into "
        "the light and read it aloud. 'I seem to believe rest must be "
        "earned by exhaustion.' Once stated, the rule can be evaluated "
        "like any standard: is it fair? Is it mine? Would I impose it on "
        "someone I love? Most surprise-trigger rules fail that audit - "
        "which is exactly why they hid."),
    key_points=[
        "Surprise triggers: good fortune, resting, outgrowing people, laughing in hard seasons, being helped, saying no, not feeling 'guilty enough.'",
        "Each fires the appraisal through a side door - a quiet implicit rule, not the obvious 'don't harm' standard.",
        "They reveal hidden standards you didn't know you held, which makes them diagnostically precious.",
        "The move is always the same: state the hidden rule aloud, then audit it - is it fair? Is it mine?",
        "Most hidden rules fail the audit ('would I impose this on someone I love?') - which is why they hid.",
    ],
    requirements=[
        "At least six surprise triggers with the 'why guilty about THAT?' framing",
        "The hidden-rule mechanism explained via dissonance",
        "The state-it-aloud audit technique",
        "No diagnostic language anywhere in the record",
    ],
    standards=["Festinger on cognitive dissonance and implicit standards"],
    citations=[CIT_FESTINGER, CIT_LAZARUS],
    sig_lens=(
        "The Signature lens reads surprise triggers as entries in "
        "invisible ink: the ledger holds rules written so long ago the "
        "hand forgot them, and they only appear when warmed by an event. "
        "His method is the reveal: hold each warmed rule to the light and "
        "ask whose handwriting it is - keep what is yours, wash out what "
        "isn't. Clearly labeled Signature-made, never presented as "
        "authentic public record."),
),
dict(
    key="guilt_chain_reactions", name="Chain Reactions: How One Trigger Sets Off a Cascade",
    group="Compounded", ladder_rank=7, ladder_tier="compounded",
    description=(
        "Guilt rarely stays a single feeling for long - one trigger can "
        "set off a whole cascade, each emotion feeding the next. It "
        "usually starts clean: you snap at someone, guilt fires - the "
        "honest signal, repair-worthy. Then the SECOND wave: shame slides "
        "in beside it ('what kind of person snaps like that?'), and now "
        "the urge to apologize fights the urge to hide. Third: ANXIETY "
        "about the consequences - will they tell others, will this change "
        "things permanently, what if the apology makes it worse? Fourth: "
        "ANGER, often at yourself ('I always do this') but sometimes "
        "deflected outward ('they provoked me') - the mind hunting for "
        "somewhere to put the pressure. Fifth: SADNESS as the energy "
        "drains and the situation feels bigger than your ability to fix "
        "it. Sixth, the quiet killer: WITHDRAWAL - you stop texting first, "
        "skip the gathering, go quiet - which creates FRESH guilt about "
        "the withdrawal itself. And the cascade has a feedback loop: every "
        "new emotion re-triggers the appraisal, so the original breach "
        "gets re-felt through each new lens. By evening, the person isn't "
        "feeling one guilt about one snap - they're feeling a weather "
        "system. The way out is always the same and always unglamorous: "
        "go back to the FIRST domino. Name the original breach in one "
        "sentence. Ask what repair it actually needs. The cascade is "
        "almost always bigger than the breach - which means settling the "
        "breach starves the whole chain at its root."),
    how_it_works=(
        "Cascades run on appraisal generalization. The original "
        "standard-breach-responsibility check creates arousal and "
        "attentional narrowing; in that narrowed, aroused state, the mind "
        "re-appraises EVERYTHING through the breach - Scherer's sequential "
        "checking keeps cycling because no check returns 'resolved.' "
        "Shame joins when attention slides from act to self; anxiety joins "
        "when the checking turns future-oriented (consequence scanning); "
        "anger joins as the approach system misfires onto the nearest "
        "target, often the self; sadness joins as energy depletes; "
        "withdrawal is the behavioral output of shame plus depleted "
        "energy. The feedback loop is the key structure: each new emotion "
        "carries its own appraisal, and each appraisal re-activates the "
        "original breach memory - so the chain is self-feeding. "
        "Interventions that target the LATER dominoes (calming the anxiety, "
        "arguing with the shame) help briefly but the chain re-forms, "
        "because the root appraisal is still open. Repairing or honestly "
        "reassessing the FIRST breach closes the root, and the downstream "
        "emotions - deprived of their fuel - fade in order."),
    key_points=[
        "The typical cascade: guilt -> shame -> anxiety -> anger (at self or deflected) -> sadness -> withdrawal -> fresh guilt about the withdrawal.",
        "Each new emotion re-triggers the original appraisal - the chain is self-feeding.",
        "By evening the person feels a weather system, not a single feeling - but the cascade is almost always bigger than the breach.",
        "Targeting later dominoes helps briefly; the chain re-forms while the root appraisal stays open.",
        "The way out: name the original breach in one sentence, settle it, starve the chain at its root.",
    ],
    requirements=[
        "A named cascade sequence with each link explained",
        "The self-feeding feedback loop described",
        "Why root-settling beats domino-treating",
        "No diagnostic language anywhere in the record",
    ],
    standards=["Scherer on sequential appraisal checking; Lazarus on emotion cascades"],
    citations=[CIT_SCHERER, CIT_LAZARUS],
    sig_lens=(
        "The Signature lens reads the cascade as one red entry photocopied "
        "down the whole ledger: each new emotion stamps the same breach "
        "onto a fresh page until the book is nothing but copies. His "
        "intervention is ruthlessly simple: find the original page, settle "
        "it, and shred the photocopies - they were never separate debts. "
        "Clearly labeled Signature-made, never presented as authentic "
        "public record."),
),
# ------------------------------------------------- 22-25: behavior
dict(
    key="guilt_behavior_actions", name="What People Do When They Feel Guilty: Typical Actions and Reactions",
    group="Advanced", ladder_rank=8, ladder_tier="advanced",
    description=(
        "Guilt is one of the most ACTION-driving emotions - it rarely sits "
        "still. The headline behavior is REPAIR: apologizing, confessing, "
        "fixing what was broken, replacing what was taken, doing the "
        "thing that was neglected - the direct approach toward the person "
        "harmed. When direct repair feels too big, people reach for "
        "PROXY repair: being extra kind to everyone EXCEPT the person "
        "harmed, donating, volunteering, over-tipping - goodness "
        "dispensed sideways. AVOIDANCE is the shadow twin: not calling, "
        "taking the long way around, staying busy - anything to dodge the "
        "face that triggers the replay. Some people CONFESS EXCESSIVELY: "
        "telling everyone, repeating the story, posting the apology - "
        "trying to outsource the absolution to an audience. Others go for "
        "SELF-PUNISHMENT: skipping the dessert, declining the invitation, "
        "working punishing hours - paying a private fine to a private "
        "court. PEOPLE-PLEASING spikes: sudden yes-saying, gift-giving, "
        "favor-doing - pre-paying against future breaches. And some "
        "RUMINATE as action: replaying the scene for the hundredth time, "
        "which FEELS productive (it's effortful) but changes nothing - the "
        "mind's treadmill. The health of the response isn't in the "
        "category but in the FIT: repair fits when the breach is real and "
        "the person is reachable; proxy repair fits when direct repair is "
        "truly impossible; avoidance never fits - it only schedules the "
        "aftershocks; excessive confession fits nobody, since audiences "
        "can't settle accounts they weren't party to."),
    how_it_works=(
        "Every behavior on the list is the approach urge finding - or "
        "failing to find - its target. Direct repair is the urge "
        "discharged correctly: approach the harmed person, close the "
        "breach, loop ends. Proxy repair is the urge discharged at a "
        "substitute target: the motor program runs, tension drops "
        "briefly, but the original appraisal stays open - which is why "
        "proxy repair needs repeating. Avoidance is the urge COLLIDING "
        "with shame's withdrawal urge (see the blend record): the two "
        "cancel into frozen non-action, and the open appraisal keeps the "
        "loop cycling. Excessive confession is the repair urge plus "
        "reassurance-seeking: each telling buys a moment of relief, but "
        "relief without repair teaches the loop that telling IS the "
        "repair - a confusion that deepens with repetition. "
        "Self-punishment is the ledger metaphor made literal: the mind "
        "levies a fine against itself, and the fine feels like settlement "
        "- but fines paid to yourself don't reach the harmed person's "
        "account. Baumeister's interpersonal account predicts the ranking: "
        "behaviors that actually restore the bond work; behaviors that "
        "only manage the feeling don't."),
    key_points=[
        "The behavior menu: direct repair, proxy repair, avoidance, excessive confession, self-punishment, people-pleasing, rumination-as-action.",
        "Health is in the FIT, not the category: repair fits real reachable breaches; proxy fits impossible direct repair; avoidance never fits.",
        "Proxy repair discharges tension briefly but leaves the appraisal open - which is why it needs repeating.",
        "Excessive confession confuses telling with repairing; audiences can't settle accounts they weren't party to.",
        "Self-punishment pays fines to a private court - the harmed person's account never receives them.",
    ],
    requirements=[
        "At least six typical behaviors with plain descriptions",
        "The fit-not-category principle stated",
        "Why proxy repair and self-punishment don't settle the account",
        "No diagnostic language anywhere in the record",
    ],
    standards=["Baumeister and colleagues on guilt-driven reparative behavior"],
    citations=[CIT_BAUMEISTER, CIT_GROSS],
    sig_lens=(
        "The Signature lens sorts the behaviors by where the payment "
        "lands: direct repair pays the harmed account, proxy repair pays "
        "a stranger's account and calls it done, avoidance pays nothing "
        "and lets interest accrue, self-punishment pays the accountant "
        "himself - who was never the creditor. His audit question for "
        "every guilty act: which account received the payment? Clearly "
        "labeled Signature-made, never presented as authentic public "
        "record."),
),
dict(
    key="guilt_behavior_speech", name="What Guilty People Say: Phrases, Tone, and Speech Patterns",
    group="Advanced", ladder_rank=8, ladder_tier="advanced",
    description=(
        "Guilt has a dialect, and once you hear it you can't unhear it. "
        "The PHRASES are the giveaway: 'I'm sorry' repeated past the "
        "point of function - once for the breach, then again for the "
        "awkwardness, then again for having apologized badly. 'I feel "
        "terrible about...' - the feeling announced as a down payment on "
        "the repair. 'It's all my fault' - total responsibility claimed "
        "up front, sometimes before the facts are even established. 'I "
        "didn't mean to, I swear' - intention audited aloud. 'Can I make "
        "it up to you?' - the repair bid. 'You must think I'm awful' - "
        "fishing for the absolution the speaker can't grant themselves. "
        "The TONE: softer than the speaker's baseline, slower, with the "
        "volume dropping on the words that name the act - as if saying "
        "them quietly made them smaller. Pitch often rises slightly at "
        "the ends of sentences, turning statements into questions "
        "seeking verdicts. The PATTERNS: over-explaining - three reasons "
        "where one would do, the timeline rehearsed in excessive detail "
        "(disfluency performing thoroughness). Hedging - 'kind of,' "
        "'sort of,' 'a little bit' padding the confession. Repeating - "
        "circling back to the apology two topics later, unable to leave "
        "it closed. And the tell of tells: the UNPROMPTED confession - "
        "volunteering the breach before anyone asked, because the replay "
        "loop couldn't wait for an audience. Listen for the cluster: "
        "softened tone plus repeated apology plus over-explanation, and "
        "you're hearing guilt speak."),
    how_it_works=(
        "Guilty speech is the repair urge routed through language, and "
        "each feature serves it. Repeated apologies are multiple repair "
        "bids: the speaker doesn't trust that one bid settled the "
        "account, so they keep bidding - which, ironically, can annoy the "
        "harmed person and create a fresh breach. Total-responsibility "
        "claims ('all my fault') are pre-emptive: by judging themselves "
        "first and hardest, the speaker hopes to disarm the other's "
        "judgment - a verbal appeasement display matching the body's. "
        "Over-explaining is the re-appraisal made audible: the mind is "
        "still cycling standard-breach-responsibility, and the mouth "
        "narrates the cycling. The softened tone and dropped volume on "
        "the act-words are literal minimization attempts - smaller sound "
        "for a smaller-seeming breach. Rising terminal pitch (uptalk) "
        "turns declarations into verdict-requests: the speaker is asking "
        "the listener to complete the appraisal for them. The "
        "unprompted confession is the approach urge at its purest - it "
        "couldn't wait for permission."),
    key_points=[
        "The phrasebook: repeated 'I'm sorry,' 'I feel terrible,' 'it's all my fault,' 'I didn't mean to,' 'can I make it up,' 'you must think I'm awful.'",
        "Tone: softer, slower, volume dropping on the act-words; pitch rising into verdict-seeking questions.",
        "Patterns: over-explaining (three reasons for one), hedging, circling back, the unprompted confession.",
        "'It's all my fault' is pre-emptive self-judgment - a verbal appeasement display.",
        "The cluster to listen for: softened tone + repeated apology + over-explanation.",
    ],
    requirements=[
        "Characteristic phrases quoted as people actually say them",
        "Tone and speech patterns described observably",
        "Each feature given its function in plain words",
        "No diagnostic language anywhere in the record",
    ],
    standards=["Baumeister and colleagues; Keltner and Buswell on appeasement"],
    citations=[CIT_BAUMEISTER, CIT_KELTNER],
    sig_lens=(
        "The Signature lens hears guilty speech as the ledger read aloud: "
        "the repeated apology is the entry read twice in case the first "
        "reading didn't post, the over-explanation is the accountant "
        "showing all his work, the softened tone is the page turned down "
        "so the red shows less. His editing note: read the entry once, "
        "clearly, then close the book - re-reading never re-balances. "
        "Clearly labeled Signature-made, never presented as authentic "
        "public record."),
),
dict(
    key="guilt_decisions_judgment", name="How Guilt Changes Decisions and Judgment",
    group="Advanced", ladder_rank=8, ladder_tier="advanced",
    description=(
        "Guilt doesn't just feel - it VOTES. A guilty mind decides "
        "differently than a clear one, in predictable directions. "
        "RISK goes down: the guilty become cautious, choosing the safe "
        "option, declining the gamble - the mind that just caused harm "
        "is in no mood to risk more. GENEROSITY goes up: study after "
        "study finds guilt increases giving, helping, and cooperating - "
        "the repair urge generalized into 'be good everywhere.' "
        "SELF-PUNISHMENT gets a vote: guilty deciders choose worse "
        "outcomes for themselves - the smaller slice, the harder task, "
        "the declined opportunity - as if the decision itself could pay "
        "the fine. STANDARDS get stricter: after a breach, people judge "
        "themselves (and sometimes others) more harshly - the dials "
        "recalibrate upward, and yesterday's acceptable becomes today's "
        "suspicious. DECISION PARALYSIS sets in on anything resembling "
        "the breach domain: the person who snapped at family agonizes "
        "over every word at dinner for a week. And CONFESSION gets "
        "over-weighted: guilty minds overestimate how much others want "
        "the full disclosure, and underestimate how much repair can be "
        "done quietly. None of this is irrational in the moment - each "
        "shift is the appraisal system trying to prevent the next breach. "
        "The cost is proportion: guilt-tinted decisions are systematically "
        "too cautious, too generous, too harsh, too frozen. The practical "
        "rule: big decisions made at guilt's peak deserve a second look "
        "after the feeling fades - decide with the lesson, not with the "
        "ache."),
    how_it_works=(
        "Each decision shift is the appraisal machinery applied "
        "forward. Risk aversion comes from the responsibility dial stuck "
        "high: a mind that just assigned itself total blame for one "
        "outcome assigns itself total blame for hypothetical ones too, so "
        "it avoids creating new ones. Generosity spikes are the repair "
        "urge generalized: the approach system, denied its specific "
        "target, seeks any target - Baumeister's work shows guilt reliably "
        "increases prosocial behavior even toward uninvolved third "
        "parties. Self-punishing choices are the private-court fine made "
        "decisional: choosing the worse option FEELS like paying, and the "
        "feeling is mistaken for settlement. Stricter standards are "
        "dissonance prevention (Festinger): having breached once, the "
        "mind tightens the rules to avoid the pain of breaching again - "
        "an overcorrection that usually relaxes with time. Paralysis in "
        "the breach domain is the replay loop colonizing deliberation: "
        "every option gets run through the breach scene. The 'second "
        "look' rule works because the dials normalize as the feeling "
        "fades - the lesson (don't snap) survives, the distortion (every "
        "word is dangerous) doesn't."),
    key_points=[
        "Guilt votes: risk down, generosity up, self-punishing choices up, standards stricter, breach-domain decisions frozen.",
        "Generosity spikes generalize the repair urge - guilt reliably increases helping even toward uninvolved third parties.",
        "Self-punishing choices feel like paying the fine, but the feeling is mistaken for settlement.",
        "Stricter standards are dissonance prevention: the mind overcorrects to avoid breaching again.",
        "Big decisions at guilt's peak deserve a second look later - decide with the lesson, not the ache.",
    ],
    requirements=[
        "At least five decision/judgment shifts described concretely",
        "Each shift given its mechanism in plain words",
        "The second-look rule with its reasoning",
        "No diagnostic language anywhere in the record",
    ],
    standards=["Baumeister and colleagues on guilt and prosocial behavior; Festinger on dissonance prevention"],
    citations=[CIT_BAUMEISTER, CIT_FESTINGER],
    sig_lens=(
        "The Signature lens reads guilt-tinted decisions as the "
        "accountant voting his own anxieties: the cautious vote is the "
        "books locked early, the generous vote is overpayment to every "
        "account, the self-punishing vote is the fine levied from the "
        "wrong pocket. His standing order: let the accountant report, "
        "never let him chair the meeting - decisions need the lesson, not "
        "the ache. Clearly labeled Signature-made, never presented as "
        "authentic public record."),
),
dict(
    key="guilt_escalation", name="Behavior Under Intensity: How Actions Escalate as the Feeling Grows",
    group="Advanced", ladder_rank=9, ladder_tier="advanced",
    description=(
        "Watch guilt climb its own ladder and the behaviors climb with "
        "it. At LOW intensity, behavior is light and proportionate: the "
        "quick text, the small favor, the 'my bad' with a grin - repair "
        "acts sized to the breach, delivered and done. The person stays "
        "functional; life continues around the feeling. At MODERATE "
        "intensity, behavior gets HEAVIER: the long apology letter, the "
        "repeated check-ins ('are we okay?'), the grand gesture that "
        "costs more than the breach did. The person starts organizing "
        "their day around the guilt - avoiding the person, rehearsing "
        "conversations, the breach becoming a scheduling factor. At HIGH "
        "intensity, behavior can turn SELF-DESTRUCTIVE in the broad "
        "sense: punishing routines (grueling workouts as penance, "
        "deliberate sleep deprivation), sabotaging good things ('I don't "
        "deserve this'), pushing people away before they can be "
        "disappointed again, confessing to people who weren't involved "
        "just to spread the weight. The escalation pattern is consistent: "
        "as the feeling grows, the repair target gets vaguer. Low "
        "intensity aims at the breach; moderate aims at the relationship; "
        "high intensity aims at the SELF - and the self is not a repairable "
        "target, so the actions spin without settling anything. That's "
        "the paradox to memorize: the bigger the guilt, the more the "
        "behavior misses the actual breach. De-escalation always means "
        "re-aiming: bring the target back from the self to the "
        "relationship to the specific act - and act THERE, at the "
        "smallest true size of what happened."),
    how_it_works=(
        "Escalation follows the blend gradient. At low intensity, the "
        "feeling is mostly pure guilt (act-focused), so behavior targets "
        "the act - precise and effective. As intensity rises, shame "
        "increasingly joins the blend (see the blend record): attention "
        "slides from act to self, and behavior follows attention - from "
        "repairing the thing, to repairing the relationship, to punishing "
        "the person. Self-punishing behaviors feel productive because "
        "they're costly, and the mind confuses cost with settlement - but "
        "cost paid to the self never reaches the harmed party's account, "
        "so the appraisal stays open and the feeling persists, demanding "
        "more cost. It's a treadmill with a paywall. The sabotage "
        "behaviors ('I don't deserve this') are dissonance reduction in "
        "reverse: instead of changing the belief to fit the good thing, "
        "the person destroys the good thing to fit the belief. Re-aiming "
        "works because it restores the act-focus: the moment behavior "
        "targets the specific breach again, the loop has something it can "
        "actually close."),
    key_points=[
        "Escalation ladder: low = light proportionate repair; moderate = heavy gestures, day organized around guilt; high = self-punishing routines, sabotage, confession-spreading.",
        "As feeling grows, the repair target gets vaguer: from the act, to the relationship, to the self - and the self can't be repaired, only punished.",
        "The paradox: the bigger the guilt, the more behavior misses the actual breach.",
        "Costly behavior feels like settlement but isn't - cost paid to yourself never reaches the harmed party's account.",
        "De-escalation = re-aiming: bring the target back to the specific act and act at the smallest true size of what happened.",
    ],
    requirements=[
        "Three intensity levels with distinct behavior sets",
        "The target-gets-vaguer pattern explained",
        "The cost-versus-settlement confusion named",
        "De-escalation as re-aiming",
        "No diagnostic language anywhere in the record",
    ],
    standards=["Tangney and Dearing on guilt/shame and behavior; Baumeister on self-punishment"],
    citations=[CIT_TANGNEY, CIT_BAUMEISTER],
    sig_lens=(
        "The Signature lens reads escalation as the accountant losing the "
        "original invoice: low intensity pays the exact bill, moderate "
        "pays the bill plus imagined interest, high intensity burns down "
        "the office to punish the clerk. His fire code: when the payment "
        "exceeds the invoice, stop paying and find the invoice - it is "
        "always smaller than the fire. Clearly labeled Signature-made, "
        "never presented as authentic public record."),
),
# ------------------------------------------------- 26-28: healthy expression
dict(
    key="guilt_healthy_expression", name="Healthy Expression: Saying It, Showing It, and Channeling It Well",
    group="Advanced", ladder_rank=9, ladder_tier="advanced",
    description=(
        "Healthy expression of guilt is the repair beat executed well, "
        "and it has a shape. SAYING IT: the apology that works names the "
        "specific act ('I missed your call and I said I would call'), "
        "accepts responsibility without hedging ('it was my fault, not "
        "the traffic'), acknowledges the impact ('I know that left you "
        "waiting'), and offers a concrete repair ('I will call every "
        "Sunday; I have set the reminder'). What it does NOT do: grovel, "
        "repeat itself into the ground, demand instant forgiveness, or "
        "smuggle in excuses. SHOWING IT: letting the feeling be visible "
        "in proportion - the lowered eyes, the serious tone - without "
        "performing it; honesty reads in the willingness to be "
        "uncomfortable, not in theatrics. CHANNELING IT: converting the "
        "repair urge into changed behavior - the system fixed so the "
        "breach can't recur, the lesson installed as a habit rather than "
        "carried as a weight. The three share one principle: "
        "proportion. Healthy guilt expression matches the response to the "
        "breach - no more, no less. Under-responding (the shrug, the "
        "'whatever') leaves the account open. Over-responding (the "
        "grovel, the grand gesture) creates a NEW imbalance - now the "
        "other person owes YOU comfort for your distress, which is a "
        "strange kind of theft. The test of healthy expression is simple: "
        "afterward, is the breach smaller and the relationship steadier? "
        "If yes, the guilt did its job and can be released."),
    how_it_works=(
        "Each element of healthy expression closes a specific part of "
        "the appraisal. Naming the act precisely satisfies the breach "
        "beat: the mind stops cycling 'what exactly did I do' when the "
        "act is stated plainly. Unh hedged responsibility satisfies the "
        "responsibility beat: no more arguing with the dial. "
        "Acknowledging impact addresses the interpersonal core - "
        "Baumeister's account says guilt exists to protect bonds, and "
        "bonds are repaired by felt understanding, not just by words. "
        "Concrete repair gives the approach urge its proper target and "
        "discharges it. Changed behavior prevents recurrence, which is "
        "what lets the lesson survive after the feeling fades - the "
        "feeling is temporary, the system change is durable. Proportion "
        "matters because both errors re-open the appraisal: "
        "under-responding leaves the breach beat unsatisfied (the loop "
        "continues), over-responding creates a NEW breach beat (now I've "
        "burdened them with my guilt about my guilt). The release at the "
        "end isn't forgetting - it's the appraisal returning 'resolved.'"),
    key_points=[
        "Saying it: name the act, own it without hedging, acknowledge the impact, offer concrete repair - no groveling, no excuse-smuggling.",
        "Showing it: visible in proportion; honesty reads in willingness to be uncomfortable, not theatrics.",
        "Channeling it: convert the urge into changed behavior - the lesson installed as habit, not carried as weight.",
        "The governing principle is proportion: under-responding leaves the account open; over-responding creates a new imbalance.",
        "The test: afterward, is the breach smaller and the relationship steadier? Then release it.",
    ],
    requirements=[
        "Saying, showing, and channeling each given concrete shape",
        "The anatomy of a working apology spelled out",
        "Proportion as the governing principle, with both errors named",
        "No diagnostic language anywhere in the record",
    ],
    standards=["Baumeister and colleagues on reparative behavior; Tangney and Dearing on adaptive guilt"],
    citations=[CIT_BAUMEISTER, CIT_TANGNEY],
    sig_lens=(
        "The Signature lens reads healthy expression as the ledger's "
        "proper closing procedure: say the entry aloud (name it), show "
        "the page honestly (no forged summaries), post the balancing "
        "line (repair), then rule the account closed (release). His "
        "bookkeeping law: a closed account is never re-audited - the "
        "lesson lives in the new procedure, not in re-reading the old "
        "page. Clearly labeled Signature-made, never presented as "
        "authentic public record."),
),
dict(
    key="guilt_unhealthy_expression", name="Unhealthy Expression: Bottling It Up or Exploding - What Each Costs",
    group="Advanced", ladder_rank=9, ladder_tier="advanced",
    description=(
        "Guilt mishandled goes wrong in two opposite directions, and "
        "both are expensive. BOTTLING IT UP looks like control but works "
        "like storage: the feeling gets pushed down - no apology, no "
        "mention, the breach never named aloud. What it costs: the "
        "replay loop doesn't stop, it just goes underground, running "
        "quieter but longer. The body pays the storage fee - tension, "
        "stomach trouble, the 2 a.m. sessions from the sleep record. "
        "Behavior warps around the hidden thing: avoidance of the person, "
        "irritability with everyone, the strange coldness that the other "
        "person feels but can't name. And the account never settles - "
        "bottled guilt has a half-life measured in years, surfacing at "
        "anniversaries and in unrelated arguments ('this isn't about the "
        "dishes and you know it'). EXPLODING looks like honesty but works "
        "like arson: the confession detonated all at once - the tearful "
        "3 a.m. monologue, the apology that includes five other breaches, "
        "the self-lacerating speech that forces the harmed person to "
        "become the comforter. What it costs: the other person's pain "
        "gets buried under the confessor's bigger performance; the "
        "repair becomes about managing YOUR feelings, which is a second "
        "breach wearing the costume of a repair. Exploders often feel "
        "wonderful afterward - catharsis - while the harmed person feels "
        "worse, which tells you who the explosion actually served. Both "
        "patterns share a root: the repair urge misdirected. Bottling "
        "aims it at no one; exploding aims it at everyone. Healthy "
        "expression - the previous record - aims it at the breach, once, "
        "in proportion."),
    how_it_works=(
        "Bottling is suppression, and Gross's regulation research is "
        "clear on its price: suppression doesn't reduce the feeling, it "
        "reduces its EXPRESSION while keeping the arousal - sometimes "
        "raising it. The replay loop continues because the appraisal "
        "never gets its resolution input; suppression just hides the "
        "output. The underground loop is actually more durable: without "
        "the other person's response, there's no disconfirming feedback, "
        "so the worst-case version of the breach goes unchallenged for "
        "years. Exploding is the opposite regulation failure: instead "
        "of over-control, under-control - the approach urge discharges "
        "at maximum volume with no targeting. The catharsis the exploder "
        "feels is arousal discharge, not resolution; the appraisal stays "
        "open because no clean repair was actually delivered (the harmed "
        "person was too busy managing the confessor to receive anything). "
        "Worse, the explosion typically ADDS a shame layer - now the "
        "person is guilty about the breach AND embarrassed about the "
        "meltdown. The cost asymmetry is the diagnostic: bottling taxes "
        "the bottler for years; exploding taxes everyone in the room "
        "tonight."),
    key_points=[
        "Bottling: pushed down, never named - the loop goes underground, the body pays storage fees, the account stays open for years.",
        "Exploding: the confession detonated - catharsis for the confessor, a second breach for the harmed person forced into the comforter role.",
        "Suppression doesn't reduce feeling, only expression - arousal stays, sometimes rises.",
        "Bottled guilt's half-life is measured in years; it surfaces at anniversaries and inside unrelated arguments.",
        "Both misdirect the repair urge: bottling aims it at no one, exploding aims it at everyone; health aims it at the breach.",
    ],
    requirements=[
        "Both patterns described with their specific costs",
        "Why suppression fails, in plain mechanism terms",
        "Why catharsis isn't resolution",
        "The cost asymmetry stated",
        "No diagnostic language anywhere in the record",
    ],
    standards=["Gross on suppression costs; Tangney and Dearing on maladaptive guilt"],
    citations=[CIT_GROSS, CIT_TANGNEY],
    sig_lens=(
        "The Signature lens reads the two failures as bookkeeping crimes: "
        "bottling is the entry hidden in a drawer - unposted, accruing "
        "interest in the dark; exploding is the ledger hurled across the "
        "room so everyone gets paper cuts. His law covers both: post the "
        "entry once, legibly, to the right account - then close the book. "
        "Clearly labeled Signature-made, never presented as authentic "
        "public record."),
),
dict(
    key="guilt_everyday_practices", name="Everyday Practices: Small Habits That Keep Guilt in Balance",
    group="Advanced", ladder_rank=9, ladder_tier="advanced",
    description=(
        "Guilt stays healthy the way teeth stay healthy: small daily "
        "habits, not dramatic interventions. REPAIR PROMPTLY: the "
        "24-hour rule - if you owe an apology, deliver it within a day. "
        "Fresh breaches are small and repairable; day-three breaches have "
        "grown a shame layer and a dread surcharge. KEEP PROMISES SMALL: "
        "most promise-guilt comes from promises that were too big to "
        "begin with - promise the call, not the rescue; the coffee, not "
        "the career. Small kept promises build a record the conscience "
        "can point to. THE EVENING REVIEW: two minutes before sleep - "
        "anything I owe anyone? Anything I did today that needs a word "
        "tomorrow? Write it down, sleep clean, handle it in the morning. "
        "This single habit prevents most bottled guilt. THE PROPORTION "
        "CHECK: when guilt fires, ask the dial questions - how bad was "
        "the harm really? Is the responsibility truly all mine? Can this "
        "be repaired? Ten seconds of audit prevents hours of loop. "
        "SEPARATE THE LAYERS: when the feeling is huge, ask 'what did I "
        "do' versus 'what does it prove about me' - repair the first, "
        "dismiss the second. APOLOGIZE WELL OR NOT AT ALL: a hedged, "
        "rushed, or repeated apology is worse than silence - it spends "
        "the repair bid without settling anything. FORGIVE THE SMALL "
        "STUFF IN OTHERS: practicing proportion outward calibrates it "
        "inward - people who grant others grace find their own dials "
        "easier to set fairly. None of these is dramatic. That's the "
        "point: guilt is a daily emotion, and it yields to daily tools."),
    how_it_works=(
        "Each practice targets a specific failure mode from earlier "
        "records. The 24-hour rule prevents the shame-layer accretion "
        "described in the blend record: fresh guilt is act-focused and "
        "repairable; aged guilt has usually slid toward self-focus. "
        "Small promises work through the responsibility dial: big vague "
        "promises create huge breach surfaces, while small specific ones "
        "are either kept (no guilt) or cleanly repaired. The evening "
        "review is externalization: moving open loops from working memory "
        "to paper stops the 2 a.m. replay (the mind trusts written "
        "capture and releases the rehearsal). The proportion check is "
        "deliberate re-appraisal - manually resetting dials that the "
        "automatic system set too high, which is exactly what Lazarus's "
        "model predicts will change the feeling. Layer-separation "
        "implements the blend record's untangling question as a habit. "
        "Outward forgiveness calibrates the standard itself: standards "
        "are partly learned by watching what we accept in others, so "
        "practicing proportion outward gradually rewrites the inward "
        "rulebook. Together they're a maintenance schedule for the "
        "appraisal system - not therapy, just hygiene."),
    key_points=[
        "The 24-hour rule: fresh breaches are small and repairable; day-three breaches have grown a shame layer and dread surcharge.",
        "Keep promises small: big vague promises create huge breach surfaces; small specific ones are kept or cleanly repaired.",
        "The evening review: two minutes, write down what you owe - the mind trusts paper and releases the 2 a.m. rehearsal.",
        "The proportion check: ten seconds auditing the dials prevents hours of loop.",
        "Separate the layers (act vs self), apologize well or not at all, and practice proportion outward to calibrate inward.",
    ],
    requirements=[
        "At least five concrete daily practices",
        "Each practice tied to the failure mode it prevents",
        "Framed as hygiene, not treatment",
        "No diagnostic language anywhere in the record",
    ],
    standards=["Gross on regulation strategies; Baumeister on habit and self-regulation"],
    citations=[CIT_GROSS, CIT_BAUMEISTER],
    sig_lens=(
        "The Signature lens reads the practices as the ledger's daily "
        "close: post today's entries before dark (evening review), keep "
        "invoices small enough to pay (small promises), audit the red "
        "entries before believing them (proportion check). His motto for "
        "the whole record: a ledger closed daily never needs a midnight "
        "audit. Clearly labeled Signature-made, never presented as "
        "authentic public record."),
),
dict(
    key="guilt_reading_others", name="Reading the Signs: Guilt in Other People",
    group="Advanced", ladder_rank=9, ladder_tier="advanced",
    description=(
        "Reading guilt in others is a learnable skill - and a "
        "responsibility, because misreading it causes real harm. Start "
        "with the CLUSTER, never a single sign: downcast or flickering "
        "gaze PLUS pressed lips or lip-biting PLUS restless hands PLUS "
        "softened, hesitant speech - one of these means little, all four "
        "together mean a lot. Watch for TIMING: guilt signals spike "
        "around the topic - the gaze drops exactly when the subject "
        "nears the breach, the voice softens on the specific sentence. "
        "That's the signature of guilt versus general anxiety: guilt is "
        "TOPIC-BOUND, anxiety is free-floating. Listen for the VERBAL "
        "tells from the speech record: the repeated apology, the "
        "unprompted confession, the over-detailed timeline. Notice the "
        "BEHAVIORAL tells: sudden generosity toward you, avoidance of "
        "you, the favor that comes from nowhere - all classic repair "
        "bids wearing disguises. And read the BASELINE first: some "
        "people are quiet, some avoid eye contact habitually, some "
        "fidget always - guilt is a CHANGE from baseline, not a trait. "
        "The ethics matter as much as the skill. Reading guilt is for "
        "UNDERSTANDING, not for prosecution: the moment you use the read "
        "to corner someone ('I can tell you're guilty'), you've turned "
        "an observation into a weapon, and the blend record predicts "
        "exactly what happens next - shame joins, hiding begins, and "
        "you'll never get the honest conversation you wanted. Read to "
        "open doors, never to build cases."),
    how_it_works=(
        "The cluster rule exists because no single channel is reliable "
        "alone - each has innocent explanations (tired eyes drop too, "
        "shy people avoid gaze). Reliability comes from CONVERGENCE: "
        "independent channels (face, hands, voice, topic-timing) all "
        "firing together is unlikely by chance. Topic-binding is the "
        "strongest single cue because it ties the signal to the "
        "appraisal: guilt's signals are driven by the breach "
        "representation, so they modulate with the breach's presence in "
        "conversation - near the topic, strong; away from it, fading. "
        "Baseline comparison is signal-detection basics: without knowing "
        "a person's normal, every reading is noise. The ethics warning "
        "is mechanistic, not just moral: confronting someone with a "
        "guilt-read ('I know you're guilty') shifts their attention "
        "from act to self - manufacturing the shame blend on the spot - "
        "which triggers hiding instead of honesty. The read is most "
        "useful when it stays PRIVATE and shapes YOUR behavior: soften "
        "your tone, offer an opening, make repair easy - and let them "
        "walk through the door themselves."),
    key_points=[
        "Read the CLUSTER (gaze + lips + hands + speech), never a single sign - one channel means little, four together mean a lot.",
        "Guilt is TOPIC-BOUND: signals spike as conversation nears the breach - that's what separates it from free-floating anxiety.",
        "Read the baseline first: guilt is a CHANGE from a person's normal, not a trait.",
        "Behavioral tells: sudden generosity, avoidance, favors from nowhere - repair bids in disguise.",
        "Read to open doors, never to build cases: weaponized reads manufacture shame and hiding.",
    ],
    requirements=[
        "Observable signs across face, voice, timing, and behavior",
        "The topic-bound distinction from anxiety",
        "Baseline comparison explained",
        "The ethics of reading stated plainly with its mechanism",
        "No diagnostic language anywhere in the record",
    ],
    standards=["Ekman on expression reading; Tangney and Dearing on guilt cues"],
    citations=[CIT_EKMAN, CIT_TANGNEY],
    sig_lens=(
        "The Signature lens reads other people's guilt as their ledger "
        "showing through: the topic-bound flicker is the red entry "
        "catching the light as the page turns near it. His rule for the "
        "reader: you may notice another's books, you may never audit "
        "them aloud - hold the lamp steady, say nothing of what you see, "
        "and leave the balancing to its owner. Clearly labeled "
        "Signature-made, never presented as authentic public record."),
),
dict(
    key="guilt_supportive_responses", name="What to Say and Do When Someone Near You Feels Guilty",
    group="Advanced", ladder_rank=10, ladder_tier="advanced",
    description=(
        "Someone you care about is carrying guilt, and you want to help "
        "without making it worse. FIRST, LISTEN FULLY: let them say the "
        "whole thing before you respond - guilty people expect "
        "interruption-as-judgment, and an uninterrupted hearing is itself "
        "a relief. SECOND, VALIDATE THE STANDARD, NOT JUST THE FEELING: "
        "'It makes sense you feel bad - keeping promises matters to you' "
        "works better than 'don't feel bad,' because it honors the value "
        "underneath instead of arguing with the signal. THIRD, HELP WITH "
        "PROPORTION - gently: 'It was a missed call, not a betrayal - "
        "what would you tell me if I'd done it?' The role-reversal "
        "question lets them audit their own dials without feeling "
        "lectured. FOURTH, MAKE REPAIR CONCRETE: guilty minds spiral in "
        "abstraction ('I'm a terrible friend'); pull it down to earth - "
        "'What would actually help her right now? A call? A visit "
        "Saturday?' A repair with a date on it starves the loop. FIFTH, "
        "DON'T ABSOLVE WHAT ISN'T YOURS TO ABSOLVE: 'I'm sure they don't "
        "mind' feels kind but teaches nothing and can read as dismissal - "
        "especially if they DO mind. You can say 'that sounds worth a "
        "real apology' - honest and more useful. SIXTH, STAY AFTER THE "
        "CONFESSION: the moment after someone admits something is when "
        "shame rushes in - your steady, unchanged presence in that minute "
        "is the whole intervention. What you're really doing across all "
        "six: keeping their attention on the ACT (repairable) instead of "
        "the SELF (not), and keeping yourself on their side of the table "
        "while they do the work only they can do."),
    how_it_works=(
        "Each move targets a mechanism from earlier records. Full "
        "listening counters the expected-judgment appraisal: the guilty "
        "mind predicts condemnation, and sustained non-judgmental "
        "attention disconfirms it in real time. Validating the standard "
        "works because it separates the value (worth keeping) from the "
        "volume (worth adjusting) - arguing with the feeling attacks "
        "both. The role-reversal question is a dial audit by proxy: "
        "people apply fairer standards to others than to themselves, so "
        "borrowing their 'other-mind' gets a cleaner reading. Concrete "
        "repair planning converts the abstract approach urge into a "
        "scheduled act - implementation intentions ('Saturday, 10 a.m., "
        "I call') are far more likely to execute than vague resolve. "
        "Refusing false absolution matters because premature 'it's fine' "
        "short-circuits the repair the guilt was trying to produce - the "
        "bond doesn't get its maintenance. Staying after the confession "
        "catches the shame spike at its most volatile moment: the "
        "self-focus is peaking, and an unchanged, warm presence is live "
        "evidence against the 'I'm unlovable now' appraisal."),
    key_points=[
        "Listen fully first: guilty people expect interruption-as-judgment; an uninterrupted hearing is itself relief.",
        "Validate the STANDARD ('keeping promises matters to you'), not just the feeling - honor the value, adjust the volume.",
        "Help with proportion via role-reversal: 'what would you tell me if I'd done it?'",
        "Make repair concrete with a date on it - scheduled acts starve the loop; vague resolve feeds it.",
        "Don't absolve what isn't yours to absolve; and stay present in the minute after the confession, when shame spikes.",
    ],
    requirements=[
        "At least five concrete supportive moves",
        "Each move tied to its mechanism",
        "The false-absolution warning included",
        "No diagnostic language anywhere in the record",
    ],
    standards=["Baumeister and colleagues on interpersonal regulation of guilt"],
    citations=[CIT_BAUMEISTER, CIT_TANGNEY],
    sig_lens=(
        "The Signature lens casts the supporter as the lamp-holder: you "
        "do not touch another's ledger - you hold the light steady while "
        "they read their own page. Listening is the steady hand, "
        "proportion is adjusting the flame, concrete repair is pointing "
        "at the balancing pen without picking it up. His law: the only "
        "lawful touch on another's books is light. Clearly labeled "
        "Signature-made, never presented as authentic public record."),
),
dict(
    key="guilt_mistakes_to_avoid", name="What Not to Do: The Mistakes That Make Guilt Worse",
    group="Advanced", ladder_rank=10, ladder_tier="advanced",
    description=(
        "Good intentions pave most of these. MISTAKE ONE: 'Don't feel "
        "guilty.' It argues with the signal instead of the appraisal - "
        "the person hears that their feeling is wrong, not that their "
        "dials are off, so they now feel guilty AND misunderstood. "
        "MISTAKE TWO: instant absolution - 'I'm sure it's fine, forget "
        "it.' It dismisses the breach before repair, teaching the "
        "conscience that its signals get waved away - the loop learns to "
        "shout louder next time. MISTAKE THREE: the shame upgrade - "
        "'How could you DO that?' Moving the focus from act to self "
        "manufactures the blend on the spot; hiding begins within the "
        "hour. MISTAKE FOUR: weaponizing it later - 'Well, YOU'RE the one "
        "who...' deployed in the next argument. Nothing teaches a "
        "conscience to hide faster than learning confessions become "
        "ammunition. MISTAKE FIVE: the guilt competition - 'You feel "
        "bad? Let me tell you what I did.' It hijacks the repair moment "
        "into a contest nobody wins. MISTAKE SIX: forced cheer - dragging "
        "them out, insisting on fun, performing normalcy at them. It "
        "signals that their feeling is an inconvenience to be scheduled "
        "around. MISTAKE SEVEN: the endless inquest - 'But WHY did you do "
        "it? What were you THINKING?' Past a point, analysis becomes "
        "interrogation, and interrogation manufactures defensiveness, "
        "not insight. The pattern across all seven: each mistake either "
        "attacks the feeling (instead of auditing the appraisal), "
        "dismisses the breach (instead of repairing it), or upgrades the "
        "focus from act to self (manufacturing shame). Do the opposite on "
        "each axis and you're back in the previous record's territory."),
    how_it_works=(
        "'Don't feel guilty' fails because feelings don't take orders - "
        "the instruction creates a second appraisal ('I'm feeling wrong "
        "about feeling wrong') without touching the first. Instant "
        "absolution fails through premature closure: the approach urge "
        "never discharges, so it re-fires - louder, per the loop "
        "mechanics. The shame upgrade is the most structurally damaging: "
        "it deliberately slides attention from behavior to global self, "
        "and the Tangney/Dearing framework predicts the exact outcome - "
        "withdrawal and concealment, the opposite of repair. Weaponizing "
        "is operant conditioning against honesty: confession gets "
        "punished, so confession stops - and unrepaired breaches go "
        "underground for years (see the bottling record). The guilt "
        "competition and forced cheer both communicate the same meta "
        "message - 'your feeling is too much for me' - which the guilty "
        "mind translates as confirmation of its worst appraisal. The "
        "endless inquest crosses from appraisal-audit into threat: "
        "repeated why-questions signal that the questioner has already "
        "rendered a verdict and is collecting evidence. Every mistake, "
        "mechanically, either blocks repair, feeds the loop, or "
        "manufactures shame."),
    key_points=[
        "Seven classic mistakes: 'don't feel guilty,' instant absolution, the shame upgrade, weaponizing later, guilt competition, forced cheer, the endless inquest.",
        "'Don't feel guilty' creates a second appraisal without touching the first - now they're guilty AND misunderstood.",
        "The shame upgrade ('how could you DO that?') manufactures the blend on the spot; hiding begins within the hour.",
        "Weaponizing confessions as later ammunition teaches the conscience to never confess again.",
        "Every mistake blocks repair, feeds the loop, or manufactures shame - do the opposite on each axis.",
    ],
    requirements=[
        "At least six named mistakes with what each costs",
        "The mechanism behind each mistake in plain words",
        "The unifying pattern across all mistakes",
        "No diagnostic language anywhere in the record",
    ],
    standards=["Tangney and Dearing on shame induction; Gross on invalidation effects"],
    citations=[CIT_TANGNEY, CIT_GROSS],
    sig_lens=(
        "The Signature lens files the mistakes as tampering with "
        "another's ledger: 'don't feel guilty' tears out the page, "
        "instant absolution forges the balancing line, the shame upgrade "
        "stamps the verdict across the whole book, weaponizing photocopies "
        "the entry for later use. His law is absolute: never touch "
        "another's books - not to tear, forge, stamp, or copy. Hold the "
        "lamp. Clearly labeled Signature-made, never presented as "
        "authentic public record."),
),
# ------------------------------------------------- 32-34: related emotions, mixes, full simulation
dict(
    key="guilt_related_emotions", name="The Guilt Neighborhood: Nearest Neighbors, Opposites, and Close Cousins",
    group="Advanced", ladder_rank=10, ladder_tier="advanced",
    description=(
        "Guilt lives in a crowded neighborhood - learn the neighbors and "
        "you'll stop confusing them. SHAME is the closest cousin and the "
        "most confused-with: guilt = 'I did a bad thing' (focus on act, "
        "urge to repair); shame = 'I am a bad thing' (focus on self, urge "
        "to hide). Test: if the imagined fix is an APOLOGY, it's guilt; "
        "if the imagined fix is DISAPPEARING, it's shame. REMORSE is "
        "guilt's deeper sibling - same act-focus, but heavier and more "
        "sorrowful, usually reserved for serious harms; remorse is what "
        "guilt grows into when the harm is grave. REGRET is the cooler "
        "neighbor: 'I wish I'd chosen differently' - it evaluates the "
        "DECISION, not the moral weight; you can regret a stock pick "
        "without guilt, but guilt almost always brings regret along. "
        "EMBARRASSMENT is the social cousin: it's about being SEEN in a "
        "flawed moment (tripping on stage), not about harming someone - "
        "embarrassment wants the audience to look away, guilt wants the "
        "harmed person to be made whole. MORAL DISGUST points outward at "
        "others' violations; guilt points inward at your own - same "
        "standard, opposite direction. On the far side of the street: "
        "PRIDE IN INTEGRITY ('I handled that right') and the quiet "
        "CLEAR CONSCIENCE - not the absence of standards but the "
        "satisfaction of meeting them; these are guilt's true opposites, "
        "and they're worth cultivating deliberately, because a conscience "
        "that only ever reports breaches starts to feel like an enemy. "
        "The neighborhood map matters practically: each neighbor needs a "
        "different response - repair for guilt, perspective for shame, "
        "better decision process for regret, a laugh and time for "
        "embarrassment. Treating shame with guilt's tools (more apology) "
        "deepens it; treating guilt with shame's tools (hiding) rots it."),
    how_it_works=(
        "The map is organized by two axes from the research: FOCUS "
        "(act versus self) and DIRECTION (inward versus outward). Guilt "
        "is act-focused, inward. Shame is self-focused, inward - same "
        "direction, different focus, which is why they blend so easily "
        "(see the blend record). Remorse shares guilt's coordinates but "
        "at higher harm-weight: it's guilt with the irreversibility dial "
        "maxed. Regret is act-focused but morally neutral - it runs the "
        "comparison without the standard-breach weight, evaluating "
        "outcomes instead. Embarrassment is self-focused but "
        "audience-dependent: remove the witnesses and it evaporates, "
        "while guilt persists alone at 2 a.m. - the audience test "
        "distinguishes them cleanly. Moral disgust is act-focused, "
        "OUTWARD: the same standard applied to others' behavior. The "
        "opposites (integrity-pride, clear conscience) are what the "
        "appraisal returns when the check comes back clean - they're not "
        "separate systems but the same machinery reporting success. "
        "The practical rule - match the tool to the coordinate - works "
        "because each coordinate has a different open loop: guilt's loop "
        "closes with repair, shame's with self-perspective, regret's "
        "with process change, embarrassment's with time."),
    key_points=[
        "Guilt vs shame: 'I did a bad thing' (repair urge) vs 'I am bad' (hide urge) - the apology-vs-disappearing test tells them apart.",
        "Remorse = guilt's deeper sibling for grave harms; regret = cooler, evaluates the decision not the moral weight.",
        "Embarrassment needs an audience (remove witnesses, it evaporates); guilt persists alone at 2 a.m.",
        "Moral disgust points the same standard OUTWARD at others; guilt points it INWARD.",
        "True opposites: pride in integrity and the clear conscience - cultivate them so the conscience isn't only ever bad news.",
        "Match the tool to the coordinate: repair for guilt, perspective for shame, process change for regret, time for embarrassment.",
    ],
    requirements=[
        "At least five neighbors distinguished from guilt with tests",
        "True opposites named and their cultivation recommended",
        "The two-axis organization explained",
        "The match-the-tool rule stated",
        "No diagnostic language anywhere in the record",
    ],
    standards=["Tangney and Dearing; Lewis; Haidt on moral emotions"],
    citations=[CIT_TANGNEY, CIT_LEWIS, CIT_HAIDT],
    sig_lens=(
        "The Signature lens maps the neighborhood as adjacent ledgers: "
        "shame is the same book with the verdict stamped on the COVER "
        "instead of the page, regret is the book of a gambler (outcomes, "
        "not morals), embarrassment is a book left open on a park bench, "
        "moral disgust is your neighbor's book held at arm's length. His "
        "filing rule: never shelve another ledger's entries in your own "
        "- read the right book for the feeling you actually have. Clearly "
        "labeled Signature-made, never presented as authentic public "
        "record."),
),
dict(
    key="guilt_emotion_mixes", name="Guilt Blends: Mixes With Four Partner Emotions",
    group="Advanced", ladder_rank=10, ladder_tier="advanced",
    description=(
        "In the Plutchik tradition, complex feelings are blends of simpler "
        "ones - and guilt blends distinctively with four partners. "
        "GUILT + SHAME = the heavy blend (see the dedicated record): 'I "
        "did a bad thing and it proves I'm a bad person' - repair urge "
        "fighting hide urge, the most paralyzing mix, the most common. "
        "GUILT + ANGER (at yourself) = the punishing blend: the fury has "
        "nowhere outward to go, so it turns inward - harsh self-talk, "
        "the 3 a.m. courtroom where you're prosecution and defendant. It "
        "feels like taking responsibility but it's actually the blend "
        "dodging repair: as long as you're busy punishing yourself, you "
        "don't have to face the person. GUILT + ANXIETY = the dread blend: "
        "not just 'I did wrong' but 'and the consequences are coming' - "
        "the mind runs disaster previews on loop. This blend is the "
        "insomnia specialist from the sleep record; it also drives the "
        "excessive confession (confess fast, maybe they'll go easy). "
        "GUILT + SADNESS = the hollow blend: the energy drains out and "
        "what's left is a flat, grey remorse without the repair urge's "
        "heat - 'what's the point, it's done.' This is the blend most "
        "likely to be mistaken for the guilt being 'over' - it isn't over, "
        "it's just out of fuel; the appraisal is still open underneath "
        "the flatness. Reading a blend means asking which partner is "
        "driving: the shame-driven blend needs perspective on the self, "
        "the anger-driven needs the punishment confused with repair to be "
        "named, the anxiety-driven needs the consequences faced one by "
        "one, the sadness-driven needs rest and refueling before any "
        "repair is attempted. Blends are the advanced level of this "
        "database for a reason: most real-world guilt arrives already "
        "mixed, and the pure form is the laboratory case."),
    how_it_works=(
        "Blends form when the guilt appraisal shares the stage with a "
        "second appraisal running concurrently. Guilt+shame: the act-focus "
        "and self-focus appraisals alternate (the blend record's "
        "mechanism). Guilt+anger: the breach appraisal plus a "
        "frustration appraisal - the approach system, blocked from its "
        "repair target (by fear or shame), redirects its energy onto the "
        "self as the nearest available target; the harsh self-talk is "
        "literally the attack program with its direction flipped. "
        "Guilt+anxiety: the breach appraisal plus future-oriented threat "
        "scanning (Scherer's sequential checking turned forward) - the "
        "mind simulates consequences the way it replays the past, and "
        "each simulation re-arouses the body. Guilt+sadness: the breach "
        "appraisal plus an appraisal of irreparable loss - when the "
        "irreversibility dial maxes AND the energy depletes, the repair "
        "urge loses its heat but the appraisal stays open, producing the "
        "flat grey state. The 'which partner is driving' diagnostic works "
        "because each secondary appraisal has its own intervention: you "
        "can't settle anger-driven guilt with repair alone while the "
        "punishment program is still running - it will just re-punish "
        "after the repair."),
    key_points=[
        "Four canonical blends: guilt+shame (paralyzing, most common), guilt+self-anger (punishing, dodges repair), guilt+anxiety (dread, insomnia), guilt+sadness (hollow, out of fuel).",
        "Self-anger feels like responsibility but is the blend dodging repair: punishing yourself replaces facing the person.",
        "The sadness blend is most mistaken for 'over it' - the appraisal is still open under the flatness.",
        "Each blend forms from a second appraisal running concurrently with the breach appraisal.",
        "Diagnose the driver first: each secondary appraisal needs its own intervention before repair can land.",
    ],
    requirements=[
        "Four blends described as distinct felt experiences",
        "Each blend's formation mechanism in plain words",
        "The driver-diagnostic with per-blend interventions",
        "The pure-form-as-laboratory-case point",
        "No diagnostic language anywhere in the record",
    ],
    standards=["Plutchik-style dyad analysis; Tangney and Dearing; Scherer"],
    citations=[CIT_TANGNEY, CIT_SCHERER, CIT_HAIDT],
    sig_lens=(
        "The Signature lens reads the blends as the red entry photocopied "
        "onto colored paper: shame's copy is stamped VERDICT, anger's is "
        "stamped PUNISH, anxiety's is stamped WARNING, sadness's is "
        "stamped CLOSED (falsely). His instruction: read the stamp before "
        "the entry - the color tells you which tool to pick up first. "
        "Clearly labeled Signature-made, never presented as authentic "
        "public record."),
),
dict(
    key="guilt_full_simulation", name="Full Behavioral Simulation: One Guilt From Trigger to Resolution",
    group="Advanced", ladder_rank=10, ladder_tier="advanced",
    description=(
        "The archive's showcase: one guilt, start to finish. SCENE ONE - "
        "THE TRIGGER (Tuesday, 6:40 p.m.): Maya promised her father she'd "
        "call about his test results. The day ran over; she remembered at "
        "dinner, phone in hand, thumb hovering - and then her kid needed "
        "help with homework, and the call slid to 'tomorrow.' The "
        "appraisal fires mid-homework: standard (I call when I say I "
        "will), breach (I didn't), responsibility (I chose homework-help "
        "over the call - defensible, but it was still my choice). Mild "
        "guilt, honest signal. SCENE TWO - THE PEAK (11:20 p.m.): In bed, "
        "the replay runs: her father's voice last week, smaller than "
        "usual. The blend creeps in - 'a good daughter wouldn't forget' "
        "(act sliding toward self). She drafts a text, deletes it - too "
        "small for the feeling. Shoulders tight, stomach knotted, the "
        "2 a.m. pattern loading. SCENE THREE - THE LEAK (Wednesday): "
        "Short with a coworker over nothing; instant second-layer guilt. "
        "Avoids calling at lunch - 'he'll hear it in my voice' (shame "
        "driving avoidance now). The dread of the call grows larger than "
        "any call could be. SCENE FOUR - THE TURN (Wednesday, 5:15 p.m.): "
        "She catches it: names the breach in one sentence ('I said I'd "
        "call Tuesday and I didn't'), audits the dials (harm: he waited "
        "and worried - real; responsibility: mine, though shared with a "
        "chaotic day; repair: one call, fully possible). The blend "
        "untangled: the act needs a call, the 'bad daughter' verdict gets "
        "dismissed - one missed call doesn't write the biography. SCENE "
        "FIVE - THE REPAIR (5:22 p.m., nine minutes): She calls. Names it "
        "plainly, no hedging: 'Dad, I said I'd call yesterday and I "
        "didn't - I'm sorry, that was my fault.' Acknowledges impact: 'I "
        "know you were waiting on those results alone.' He is quiet, then "
        "warm: 'You're here now.' They talk about the results (benign), "
        "about the homework, about Sunday dinner - which she now "
        "schedules, concrete, on the calendar. SCENE SIX - THE RELEASE "
        "(10:40 p.m.): The replay tries to start out of habit - but the "
        "scene it replays now includes the call, and the loop finds no "
        "open breach to chew. Sleep comes clean. The ledger for Tuesday "
        "is ruled closed - not forgotten (the Sunday dinner is the "
        "installed lesson), just balanced. Total elapsed dread: twenty "
        "hours. Total repair: nine minutes. The database's final lesson, "
        "demonstrated: the dread is always larger than the deed, and the "
        "books close the moment the entry is honestly posted."),
    how_it_works=(
        "The simulation is a composed demonstration of every major "
        "mechanism in this database, sequenced in narrative order. Scene "
        "One shows the three-beat appraisal firing on an omission "
        "(failures to act count). Scene Two shows peak dynamics: the "
        "replay loop, the shame-blend forming as attention slides from "
        "act to self, the body cluster (shoulders, stomach), the sleep "
        "pattern loading. Scene Three shows leakage (second-layer guilt "
        "with the coworker) and avoidance as the blend's withdrawal urge "
        "winning over the repair urge. Scene Four is the intervention "
        "suite: one-sentence breach-naming, the dial audit (harm, "
        "responsibility, repairability), and the blend-untangling question "
        "separating act from self-verdict. Scene Five executes the "
        "healthy-expression template exactly: named act, unhedged "
        "responsibility, acknowledged impact, concrete forward repair "
        "(Sunday dinner scheduled). Scene Six shows loop starvation: with "
        "the repair in memory, replay finds no open appraisal and stops "
        "- plus the lesson installed as a system (calendar), not carried "
        "as weight. The 20-hours-to-9-minutes ratio is the database's "
        "thesis in numbers: dread scales with avoidance, not with breach "
        "size."),
    key_points=[
        "Six scenes: trigger (omission appraisal) -> peak (replay + blend forming) -> leak (second-layer guilt, avoidance) -> turn (naming + dial audit + untangling) -> repair (nine-minute call, full template) -> release (loop starved, lesson installed).",
        "Every mechanism from the database appears in narrative order - this record is the capstone.",
        "The turn hinges on three moves: one-sentence breach naming, the dial audit, separating act from self-verdict.",
        "The repair follows the healthy-expression template exactly: named act, owned fault, acknowledged impact, concrete next step.",
        "The thesis in numbers: twenty hours of dread, nine minutes of repair - dread scales with avoidance, not breach size.",
    ],
    requirements=[
        "Multi-scene narrative from trigger through peak to resolution",
        "Every scene tied to database mechanisms in how_it_works",
        "The healthy-expression template demonstrated, not just described",
        "The dread-versus-deed thesis stated",
        "Descriptive/educational only; no real persons; no diagnostic language",
    ],
    standards=["Capstone synthesis of Tangney and Dearing; Baumeister; Gross; Lazarus"],
    citations=[CIT_TANGNEY, CIT_BAUMEISTER, CIT_GROSS, CIT_LAZARUS],
    sig_lens=(
        "The Signature lens reads the six scenes as the ledger's perfect "
        "day: the red entry posted honestly (trigger), the accountant "
        "pacing instead of posting (peak), the book carried into every "
        "room (leak), the lamp lit and the page read aloud (turn), the "
        "balancing line drawn in nine minutes (repair), the books ruled "
        "closed with the lesson filed under Procedures (release). His "
        "closing line for the whole database: the ledger never wanted "
        "your suffering - only your honesty. Clearly labeled "
        "Signature-made, never presented as authentic public record."),
),
]
