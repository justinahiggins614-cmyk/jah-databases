#!/usr/bin/env python3
"""Entries for the Boredom Emotion databases (Manon's 2026-10-17 16:15 order,
emotion series).

Descriptive and educational ONLY - the database describes and simulates
boredom; it never diagnoses real people, never labels any real person with an
emotional state, and never offers therapeutic advice beyond general, safe,
everyday guidance. No clinical language, no diagnostic labels. Healthy
expression records emphasize constructive handling.

34 records, ordered by the teaching ladder (ladder_rank 1-34, increasing),
following the shared emotion-template spec:
what boredom IS -> first-person simulation -> body signals -> facial
expression -> triggers -> behavior -> healthy expression -> recognizing it
in others -> related emotions and mixes -> complex behavioral simulation.

ID prefixes: JAH-EMBO- (public) and JAH-EMBOS- (signature), verified free
in the manifest id_prefix values (2,602 databases, zero hits) and in all
jah-databases-data-1 shard record IDs (zero 'JAH-EMBO' substring hits),
2026-10-17.

Public records are real, fact-checked psychology knowledge of boredom:
attention-based models (Eastwood, Frischen, Fenske, Smilek 2012), the
Multidimensional State Boredom Scale (Fahlman et al. 2013), meaning and
challenge accounts (van Tilburg and Igou 2012), boredom as a regulatory
signal (Elpidorou 2014), flow theory (Csikszentmihalyi 1990), the
psychology of boredom (Danckert and Eastwood 2020), APA Dictionary.
Signature editions are his original Signature lens - boredom as the soul's
unspent compass, the signal of unclaimed attention and unused capacity,
clearly labeled Signature-made and never presented as authentic public
record.

Never the words "bat belt" anywhere. No website references. No Facebook.
No religious talk. Nothing hate-adjacent, profane, or inappropriate.
"""

SIG_TAIL = ("Signature original - his original Signature lens: boredom as the "
            "soul's unspent compass, the signal of unclaimed attention and "
            "unused capacity; stillness read as raw material, curiosity as the "
            "forge; clearly labeled Signature-made, never presented as "
            "authentic public record, never diagnosing any real person.")

CIT_EASTWOOD = ("Eastwood JD, Frischen A, Fenske MJ, Smilek D. The unengaged "
                "mind: Defining boredom in terms of attention. Perspectives "
                "on Psychological Science. 2012;7(5):482-495.")
CIT_FAHLMAN = ("Fahlman SA, Mercer-Lynn KB, Flora DB, Eastwood JD. "
               "Development and validation of the Multidimensional State "
               "Boredom Scale. Assessment. 2013;20(1):68-85.")
CIT_VANTILBURG = ("van Tilburg WAP, Igou ER. On boredom: Lack of challenge and "
                  "meaning as distinct boredom experiences. Motivation and "
                  "Emotion. 2012;36(2):181-194.")
CIT_ELPIDOROU = ("Elpidorou A. The bright side of boredom. Frontiers in "
                 "Psychology. 2014;5:1245.")
CIT_CSIKSZENTMIHALYI = ("Csikszentmihalyi M. Flow: The Psychology of Optimal "
                        "Experience. Harper & Row; 1990.")
CIT_DANCKERT = ("Danckert J, Eastwood JD. Out of my skull: The psychology of "
                "boredom. Harvard University Press; 2020.")
CIT_APA = ("American Psychological Association. APA Dictionary of "
           "Psychology; current edition.")
CIT_BENCH = ("Bench SW, Lench HC. On the function of boredom. Behavioral "
             "Sciences. 2013;3(3):459-472.")
CIT_STRUK = ("Struk AA, Carriere JSA, Cheyne JA, Danckert J. A short Boredom "
             "Proneness Scale (SBPS). Assessment. 2017;24(3):346-359.")
CIT_MANN = ("Mann S, Robinson A. Boredom in the lecture theatre: An "
            "investigation into the contributors, moderators and outcomes of "
            "boredom amongst university students. British Educational "
            "Research Journal. 2009;35(2):243-258.")

ENTRIES = [
# ---------------------------------------------------------------- 1-4: what boredom IS
dict(
    key="boredom_definition", name="What Boredom Is: A Plain-Language Definition",
    group="Foundations", ladder_rank=1, ladder_tier="foundations",
    description=(
        "Boredom is the restless ache of wanting to be engaged and finding "
        "nothing to engage with. In everyday words: boredom is the mind's "
        "signal that the current situation offers too little to hold "
        "attention - too little challenge, too little meaning, or too little "
        "that feels worth doing. Psychologists describe it as an aversive "
        "state that arises when attention cannot lock onto anything "
        "satisfying; researchers call the unengaged mind the core of the "
        "feeling. Unlike tiredness, which is a lack of energy, boredom is a "
        "lack of fitting engagement - a person can be fully rested and "
        "deeply bored at the same time. Unlike sadness, which points at a "
        "loss, boredom points at an emptiness: the desire to do something "
        "worthwhile with no worthwhile thing in reach. The word covers a "
        "whole volume range, from the mild drag of a slow afternoon to the "
        "heavy, gnawing restlessness of long confinement with nothing to do. "
        "Boredom is not inherently good or bad; it is information. It tells "
        "a person that their capacity for engagement is going unused, and "
        "that something needs to change - the situation, the task, or the "
        "attention being given to it."),
    how_it_works=(
        "The boredom sequence runs in four beats: unmet need, disengaged "
        "attention, the time drag, and the urge for change. First, the mind "
        "registers an unmet need for engagement - a mismatch between how "
        "much the person wants to be involved and how much the situation "
        "offers. Attention researchers describe this as a failure to engage: "
        "the mind tries to connect with the present activity and finds "
        "nothing to grip. Second, attention disengages - it drifts, skims, "
        "and wanders, because there is nothing rewarding enough to hold it. "
        "Third comes the time drag: with attention unmoored, time feels "
        "stretched and slow; minutes crawl. Fourth, the urge for change "
        "builds - boredom is functionally a push toward novelty, meaning, "
        "or challenge, which is why people fidget, scroll, pace, or dream "
        "up escapes. Understanding this chain is the key to everything else "
        "in this database: supply genuine engagement - challenge matched to "
        "skill, or meaning matched to values - and the boredom dissolves; "
        "suppress the urge with numb distraction, and it returns heavier."),
    key_points=[
        "Boredom is an aversive state of unengaged attention - wanting to be involved with nothing satisfying to engage with.",
        "It is a lack of fitting engagement, not a lack of energy; a rested person can be deeply bored.",
        "The sequence is unmet need -> disengaged attention -> time drag -> urge for change.",
        "Time stretches under boredom because attention has nothing to grip; minutes feel like hours.",
        "The feeling is information - a push toward challenge, meaning, or novelty - not a verdict on the person.",
    ],
    requirements=[
        "Everyday definition a student or writer can quote",
        "Clear contrast between boredom, tiredness, and sadness",
        "The four-beat sequence stated in plain words",
    ],
    standards=["APA Dictionary of Psychology definition of boredom and emotion"],
    citations=[CIT_APA, CIT_EASTWOOD],
    sig_lens=(
        "His Signature lens reads boredom as the soul's unspent compass: the "
        "inner needle swinging because the engine has fuel and no road. In "
        "this lens boredom is never emptiness - it is unclaimed capacity, "
        "attention standing at full readiness with no worthy post to guard. "
        "The ache is the proof of appetite: a mind that wants more from life "
        "than the moment is serving. Stillness becomes raw material; "
        "curiosity becomes the forge. The Signature move is not to flee the "
        "drag but to hear the compass - to ask what worthy thing the unused "
        "energy is pointing toward, and then to build or seek that thing. "
        "Boredom, mastered, is a scout that returns with maps.")),
dict(
    key="boredom_emotion_family", name="Where Boredom Sits in the Emotion Family",
    group="Foundations", ladder_rank=2, ladder_tier="foundations",
    description=(
        "Boredom belongs to the family of engagement emotions - feelings that "
        "report on how well a person's attention and capacities are matched "
        "to the moment. It sits near restlessness (its most common partner), "
        "apathy (its quieter cousin), and curiosity (its opposite number). "
        "Psychologists do not count boredom among the small set of basic "
        "emotions with universal facial signals; it is a complex, "
        "cognitive-affective state built from attention, meaning, and time "
        "perception. Its roots reach into two feeds: the frustration family "
        "(the blocked-goal ache when engagement is wanted but denied) and "
        "the meaning family (the hollow feeling when nothing seems to "
        "matter). What separates boredom from its neighbors: unlike apathy, "
        "the bored person still wants to engage - apathy has stopped wanting. "
        "Unlike restlessness alone, boredom includes the judgment that the "
        "situation is at fault - there is nothing here for me. Unlike "
        "sadness, there is no loss to grieve, only an unfilled appetite. "
        "And unlike simple tiredness, rest does not cure it. Place boredom "
        "on the map as the crossroads emotion: attention, meaning, "
        "challenge, and time all meeting at one restless point."),
    how_it_works=(
        "The family tree grows from a single root: the unengaged mind. From "
        "that root, partner ingredients branch it into named states. Add "
        "blocked goals and you get frustrated boredom - the meeting that "
        "wastes your time. Add fading meaning and you get existential "
        "boredom - the slow Sunday that makes you question the week. Add "
        "restlessness and you get agitated boredom - pacing, fidgeting, "
        "checking the phone. Add low energy and you get lethargic boredom - "
        "the couch-heavy kind where even the urge for change feels tired. "
        "Researchers distinguish these faces because each needs a different "
        "answer: agitated boredom wants novelty and movement, lethargic "
        "boredom wants rest first and gentle re-entry after, meaning-hollow "
        "boredom wants purpose, not stimulation. The practical rule: name "
        "the branch before treating the root, because the wrong remedy - "
        "more noise for meaning-hollow boredom - deepens the state."),
    key_points=[
        "Boredom is a complex engagement emotion, not a basic emotion; it reports on the match between attention and the moment.",
        "Nearest neighbors: restlessness, apathy, frustration, and curiosity as the opposite number.",
        "Boredom differs from apathy - the bored person still wants to engage; apathy has stopped wanting.",
        "Branches: frustrated, meaning-hollow, agitated, and lethargic boredom - each needs a different answer.",
        "Name the branch before treating the root; the wrong remedy deepens the state.",
    ],
    requirements=[
        "Map of boredom among neighboring emotions",
        "Clear contrasts with apathy, restlessness, sadness, tiredness",
        "Branch names with their different remedies",
    ],
    standards=["Plutchik-style emotion family structure; Eastwood attention-based definition"],
    citations=[CIT_EASTWOOD, CIT_DANCKERT],
    sig_lens=(
        "His Signature lens plants boredom at the crossroads of the inner "
        "kingdom: attention, meaning, challenge, and time meeting at one "
        "gate. In this lens the family is a council, not a crowd - each "
        "neighbor has a voice, and boredom is the herald that announces "
        "which councilor is missing. Frustration knocks when goals are "
        "blocked; restlessness when the body is caged; meaning-hunger when "
        "the soul finds no worthy banner. The Signature move is council "
        "work: hear which voice the boredom is carrying, and answer that "
        "voice directly instead of drowning the herald in noise. Curiosity "
        "sits across the table as boredom's twin - same appetite, answered "
        "instead of ignored.")),
dict(
    key="boredom_intensity_scale", name="The Three Volumes: Mild, Moderate, and Intense Boredom",
    group="Foundations", ladder_rank=3, ladder_tier="foundations",
    description=(
        "Boredom comes in volumes, and the same person can meet all three in "
        "one ordinary week. Mild boredom is the gentle drag - a slow "
        "afternoon, a dull errand, the feeling that the day could be better "
        "used. It is easy to shake: a change of task, a short walk, a "
        "conversation, and it lifts. Moderate boredom is heavier and more "
        "stubborn - the long meeting with nothing at stake, the empty "
        "evening stretching ahead, the sense of being trapped in "
        "unsatisfying time. It brings real restlessness: sighing, fidgeting, "
        "checking the clock, a low hum of irritation at everything and "
        "nothing. Intense boredom is a different animal - a gnawing, "
        "oppressive state where time seems to stop and the urge to escape "
        "feels almost physical. Researchers note that sustained intense "
        "boredom is linked with risk-taking, because the mind will pay "
        "almost any price for stimulation. The three volumes share one "
        "signal - unengaged attention - but differ in how loudly the signal "
        "screams and how desperately the mind works to answer it. Knowing "
        "the volume matters: mild boredom is a nudge, moderate boredom is a "
        "warning, and intense boredom is an alarm that should be answered "
        "with real engagement, not numbing."),
    how_it_works=(
        "Think of boredom volume as a dial fed by three inputs: how much "
        "engagement the person wants, how little the situation offers, and "
        "how long the mismatch has lasted. Mild boredom is a small gap held "
        "briefly - the dial reads low because escape is easy and near. "
        "Moderate boredom is a wider gap held longer - the dial climbs "
        "because the person feels stuck in the mismatch. Intense boredom is "
        "a wide gap with no visible exit and a long duration - the dial "
        "pegs because the mind reads the situation as inescapable dead "
        "time. Duration is the multiplier: a dull ten minutes is mild; the "
        "same dullness stretched over a whole day, with no choice about it, "
        "turns intense. This is why people can tolerate a boring queue but "
        "suffer in a boring job - choice and horizon set the volume. The "
        "dial model gives a practical rule: shrink the gap (add challenge "
        "or meaning), shorten the duration (break it into pieces), or "
        "restore the sense of choice, and the volume drops."),
    key_points=[
        "Mild boredom is a gentle drag, easily shaken by a change of task or scene.",
        "Moderate boredom brings real restlessness - sighing, fidgeting, clock-checking.",
        "Intense boredom is gnawing and oppressive; sustained, it can push people toward risky stimulation-seeking.",
        "Volume is set by the engagement gap times duration, divided by the sense of choice.",
        "Match the answer to the volume: nudge, warning, or alarm.",
    ],
    requirements=[
        "Three clearly separated volumes with everyday examples",
        "The dial model in plain words",
        "Why duration and choice change the volume",
    ],
    standards=["MSBS intensity dimensions (Fahlman et al. 2013); APA intensity definitions"],
    citations=[CIT_FAHLMAN, CIT_BENCH],
    sig_lens=(
        "His Signature lens hears the three volumes as three horns of the "
        "same watchman. The soft horn is a counselor's whisper - a gentle "
        "nudge that the day could be better spent. The middle horn is a "
        "herald's call - restlessness rising, attention demanding better "
        "work. The great horn is an alarm bell - the soul announcing that "
        "its capacities are going to waste and will not be quiet about it. "
        "The Signature discipline is to answer the whisper before the bell "
        "must ring: small course corrections, made early, keep the compass "
        "calibrated. Ignoring the whisper does not silence the watchman; it "
        "only guarantees the bell.")),
dict(
    key="boredom_myths", name="Myths and Misunderstandings About Boredom",
    group="Foundations", ladder_rank=4, ladder_tier="foundations",
    description=(
        "Boredom carries a stack of myths that make it harder to handle "
        "well. Myth one: only boring people get bored. In truth, boredom "
        "strikes the curious and capable most sharply - it is the appetite "
        "for engagement, not its absence, that makes the ache. Highly "
        "creative people report some of the deepest boredom, because their "
        "minds demand more from the moment. Myth two: boredom is harmless "
        "idleness. Research links chronic boredom with real costs: "
        "risk-taking, low mood, and disengagement from work and school that "
        "compounds over time. Myth three: the cure is more stimulation - "
        "louder, faster, more. But stimulation without meaning or fitting "
        "challenge leaves people just as bored, only more tired; this is "
        "why hours of scrolling can end in deeper boredom than they began. "
        "Myth four: boredom means you need entertainment. Often it means "
        "you need purpose, mastery, or connection - the cure for "
        "meaning-hollow boredom is significance, not spectacle. Myth five: "
        "boredom is a character flaw. It is a signal, and signals are "
        "neutral data about the fit between a person and their situation. "
        "Clearing these myths matters because each one points at the wrong "
        "remedy; the right remedy starts from what boredom actually is."),
    how_it_works=(
        "Each myth misreads the signal and prescribes the wrong medicine. "
        "'Only boring people get bored' shames the sufferer, so they hide "
        "the feeling instead of answering it - but the ache belongs to "
        "appetite, and appetite is a strength misfed. 'It is harmless' "
        "invites neglect, so the state deepens until the mind pays any "
        "price for stimulation - the cheap, risky kind. 'More stimulation "
        "fixes it' feeds the loop: novelty without meaning spikes attention "
        "briefly and then drops it lower, which is the mechanics of the "
        "endless scroll. 'You need entertainment' aims at amusement when "
        "the deficit is purpose, so the hollow stays hollow. 'It is a flaw' "
        "turns a useful instrument reading into self-attack, which adds "
        "shame to boredom and makes both harder to move. The myth-busting "
        "method is simple: state the myth, show what the research actually "
        "finds, and point at the remedy the truth implies. Truthful "
        "remedies work because they match the real deficit - challenge, "
        "meaning, agency, or connection."),
    key_points=[
        "Boredom strikes the curious and capable hardest - it is appetite, not emptiness.",
        "Chronic boredom carries real costs; it is not harmless idleness.",
        "More stimulation without meaning deepens boredom; scrolling often ends worse than it began.",
        "The deficit is often purpose, mastery, or connection - not entertainment.",
        "Each myth prescribes the wrong remedy; the truth points at the real deficit.",
    ],
    requirements=[
        "Five myths stated and refuted with research",
        "The wrong remedy each myth implies",
        "Plain-language myth-busting method",
    ],
    standards=["Elpidorou on boredom's regulatory function; Danckert and Eastwood review findings"],
    citations=[CIT_ELPIDOROU, CIT_DANCKERT],
    sig_lens=(
        "His Signature lens treats myths as fog over the compass - "
        "well-meaning lies that keep the needle unreadable. 'Only boring "
        "people get bored' is the fog of shame; the Signature answer is "
        "that appetite is nobility misfed, never a flaw. 'More stimulation "
        "fixes it' is the fog of noise; the Signature answer is that the "
        "soul wants a worthy post, not a louder parade. Each cleared myth "
        "is a wiped lens. The Signature discipline is ruthless clarity: see "
        "the signal for what it is - unclaimed capacity calling for worthy "
        "work - and let no proverb talk you out of the truth your own "
        "restlessness is telling you.")),
# ---------------------------------------------------------------- 5-9: how it feels
dict(
    key="boredom_first_person", name="Inside the Feeling: A First-Person Account of Boredom",
    group="Foundations", ladder_rank=5, ladder_tier="foundations",
    description=(
        "From the inside, boredom feels like this: you are sitting in a "
        "room where nothing is happening, and the nothing is loud. Your "
        "eyes keep landing on things - the clock, the window, your own "
        "hands - and nothing holds them. Thoughts start, then stall, then "
        "start again somewhere else, like a car engine turning over without "
        "catching. There is a restless itch under the skin of the moment, a "
        "sense that you should be doing something, coupled with the flat "
        "conviction that there is nothing worth doing. Time has changed "
        "texture: the last ten minutes felt like an hour, and the next hour "
        "looks like a desert. You sigh without deciding to. You check your "
        "phone, find nothing, put it down, and check it again two minutes "
        "later as if something might have changed. There is a low irritation "
        "at everything - the room, the people, yourself - and underneath it "
        "a hollow want: not for any specific thing, but for the feeling of "
        "being absorbed in something that matters. This is the lived core "
        "the whole database describes from the outside: unengaged attention, "
        "stretched time, and the urge for change, felt from within."),
    how_it_works=(
        "The first-person passage works because it translates the model's "
        "three pillars - attention, meaning, time - into felt texture. "
        "'Eyes landing on nothing' is disengaged attention rendered as "
        "experience. 'Thoughts starting and stalling' is the mind's "
        "searching behavior when no stimulus earns sustained focus. 'Time "
        "changed texture' is the well-documented stretching of perceived "
        "duration under boredom. 'Checking the phone twice' is the urge "
        "for change expressing itself as cheap stimulation-seeking. 'Hollow "
        "want' is the meaning deficit: not hunger for a thing, but hunger "
        "for absorption. Reading it slowly, a learner can match each "
        "sentence to a mechanism, which is the point of the simulation "
        "records in this database: to make the abstract structure feel "
        "recognizable, so that when the state arrives in real life it is "
        "met with understanding instead of confusion. Recognition is the "
        "first tool of mastery."),
    key_points=[
        "From inside, boredom is loud nothing: attention that cannot land anywhere.",
        "Thoughts start and stall; time stretches; the phone gets checked twice for nothing.",
        "The hollow want is not for a specific thing but for the feeling of absorption.",
        "Each felt detail maps to a mechanism: attention, meaning, time perception, urge for change.",
        "Recognition from the inside is the first tool of mastery.",
    ],
    requirements=[
        "Vivid first-person passage in plain language",
        "Each felt detail mapped to a mechanism",
        "No diagnosing any real person",
    ],
    standards=["Phenomenological description; Eastwood attention-based account"],
    citations=[CIT_EASTWOOD, CIT_DANCKERT],
    sig_lens=(
        "His Signature lens steps inside the passage and finds not a void "
        "but a waiting room of the soul - attention pacing the floor, "
        "checking the door, finding no worthy errand. The Signature reading "
        "of 'loud nothing' is a court with no case to try: the judges are "
        "seated, the lamps are lit, and no matter has been brought. The "
        "first-person account becomes, in this lens, a roll call of "
        "capacities standing ready. To feel boredom from the inside, "
        "Signature-style, is to take attendance of your own powers - and "
        "then to give them their assignment.")),
dict(
    key="boredom_time_course", name="How Boredom Moves Through Time: Onset, Peak, Fading, Aftershock",
    group="Foundations", ladder_rank=6, ladder_tier="foundations",
    description=(
        "Boredom has a shape in time, and knowing the shape helps a person "
        "ride it instead of drowning in it. Onset is quiet: the task that "
        "held you lets go, or the waiting begins, and attention starts to "
        "skim. There is a brief window here where the feeling is just a "
        "nudge - this is the easiest moment to redirect it. Then the climb: "
        "attention fails to re-engage, the mind registers the gap, and the "
        "restlessness builds. Sighs deepen, fidgeting starts, the clock "
        "gets checked. The peak arrives when the mismatch feels total - "
        "nothing here, nothing coming, time stopped. At the peak, the urge "
        "for change is strongest, and so is the temptation toward cheap "
        "escape: the scroll, the snack, the argument. Then fading: either "
        "the situation ends, or something genuinely engaging arrives, or "
        "the person finds a way to reframe the moment - and attention "
        "locks on, time resumes its normal pace, the ache drains away. The "
        "aftershock is the part people forget: after heavy boredom, there "
        "is often a residue - a flat tiredness, a wariness of stillness, "
        "or a rebound hunger for stimulation that can overshoot into "
        "restless overactivity. Knowing the full arc turns a confusing "
        "suffering into a legible process with an end."),
    how_it_works=(
        "The time course follows the attention system like a tide chart. "
        "At onset, attention is still partially engaged, so the cost of "
        "redirecting it is low - a small novelty or a reframed purpose can "
        "recapture it. During the climb, disengagement deepens: each failed "
        "attempt to find something satisfying raises the threshold for what "
        "counts as satisfying, which is why the climb accelerates. The peak "
        "is the point of maximum mismatch between wanted and offered "
        "engagement, and the urge for change is the system's alarm at full "
        "volume. Fading begins the moment attention genuinely locks onto "
        "something - challenge, meaning, or novelty that actually fits - "
        "because locked attention restores normal time perception and "
        "drains the ache. The aftershock is the nervous system's settling: "
        "prolonged unengaged arousal leaves a fatigue debt, and the rebound "
        "appetite is the system overcorrecting toward stimulation. The "
        "practical lesson is timing: intervene at onset with small "
        "redirects, endure the peak with structure rather than cheap "
        "escape, and expect the aftershock so it is not mistaken for a new "
        "problem."),
    key_points=[
        "Onset is quiet and is the cheapest moment to redirect the feeling.",
        "The climb accelerates because each failed search raises the bar for what counts as satisfying.",
        "The peak is maximum mismatch; the urge for change and the temptation of cheap escape are both strongest.",
        "Fading begins the moment attention genuinely locks onto something fitting.",
        "The aftershock - flat tiredness or rebound restlessness - is normal settling, not a new problem.",
    ],
    requirements=[
        "Five phases described in plain language",
        "Why the climb accelerates",
        "Practical timing lesson for each phase",
    ],
    standards=["Gross on regulation timing; Eastwood attention dynamics"],
    citations=[CIT_EASTWOOD, CIT_BENCH],
    sig_lens=(
        "His Signature lens reads the time course as a tide the soul can "
        "learn to sail. Onset is the harbor - still cheap to change course. "
        "The climb is the current strengthening - the wise sailor sets the "
        "rudder early rather than fighting the full flow. The peak is the "
        "storm's eye - hold structure, do not chase wreckage. Fading is the "
        "wind returning - catch it with real canvas, not paper sails. The "
        "aftershock is the settling sea - respect it, rest in it, do not "
        "mistake the swell for a second storm. The Signature sailor learns "
        "the tide table by heart and never again fears the water.")),
dict(
    key="boredom_low_vs_high", name="Boredom at Low vs High Intensity: Two Lived Snapshots",
    group="Foundations", ladder_rank=7, ladder_tier="foundations",
    description=(
        "Low-intensity boredom, a Tuesday afternoon: the errands are done, "
        "the next thing starts in an hour, and the in-between stretches a "
        "little thin. You drift to the window, watch the street for a "
        "while, feel a mild wish that something interesting would happen. "
        "Your body is loose, your breathing easy; the feeling is a light "
        "weight, easily set down. A friend calls, or you start tidying a "
        "drawer, and it is gone before you remember it was there. "
        "High-intensity boredom, a long confinement with nothing to do: the "
        "same unengaged attention, but turned up until it hurts. Time does "
        "not stretch - it stops. Every surface of the room has been "
        "examined. The restlessness is physical now: legs bounce, fingers "
        "drum, the body seems to be searching the air for something to do. "
        "Thoughts loop and snag; irritation flares at small things - a "
        "ticking clock, a humming light. There is a gnawing sense of life "
        "being wasted, minute by minute, and a desperate hunger for any "
        "change, almost any change, that would break the spell. The two "
        "snapshots share one mechanism - attention with nowhere satisfying "
        "to go - but they are different experiences the way a drizzle and a "
        "flood are both water. The low snapshot teaches recognition; the "
        "high snapshot teaches respect."),
    how_it_works=(
        "The two snapshots differ along the same dials that set boredom "
        "volume: engagement gap, duration, and choice. In the low snapshot, "
        "the gap is small (the afternoon is only mildly underfilled), the "
        "duration is short (an hour), and choice is intact (you could call "
        "the friend, tidy the drawer) - so the system stays in the nudge "
        "range. In the high snapshot, the gap is wide (nothing on offer), "
        "the duration is long and open-ended, and choice feels absent - so "
        "the alarm runs at full volume and the body joins the protest. "
        "Attention behaves differently at the two settings: at low "
        "intensity it skims pleasantly, still able to land; at high "
        "intensity it thrashes, unable to land anywhere, which is why the "
        "high state feels so much more miserable than a mere scaling-up "
        "would predict. The comparison is a calibration tool: learners who "
        "can place their own state on this spectrum can match the remedy to "
        "the reading instead of using a sledgehammer on a nudge or a "
        "whisper on an alarm."),
    key_points=[
        "Low boredom is a light, easily lifted drag; high boredom is gnawing and physical.",
        "Both share one mechanism - unengaged attention - at different dial settings.",
        "At high intensity, attention thrashes instead of skimming, which multiplies the misery.",
        "Gap, duration, and choice set which snapshot you are living in.",
        "Calibration lets you match the remedy to the reading.",
    ],
    requirements=[
        "Two vivid lived snapshots, same mechanism",
        "Dial settings compared across the snapshots",
        "Calibration as a practical tool",
    ],
    standards=["MSBS intensity structure; Lazarus appraisal-to-state model"],
    citations=[CIT_FAHLMAN, CIT_DANCKERT],
    sig_lens=(
        "His Signature lens sets the two snapshots side by side like a "
        "before-and-after of the same compass. The Tuesday afternoon is the "
        "needle trembling - a gentle reminder that the day wants shaping. "
        "The long confinement is the needle spinning - the soul declaring "
        "that its capacities are being wasted and demanding an answer. The "
        "Signature reader learns to honor both: the tremble is answered "
        "with small craft, the spin with great work. Neither is feared; "
        "both are heard. The drizzle teaches you to carry an umbrella; the "
        "flood teaches you to build on high ground.")),
dict(
    key="boredom_restlessness_blend", name="Boredom Mixed With Restlessness: The Most Common Blend",
    group="Foundations", ladder_rank=8, ladder_tier="foundations",
    description=(
        "Boredom rarely travels alone, and its most faithful companion is "
        "restlessness. The blend feels like this: the flat emptiness of "
        "boredom with an engine running underneath it. You cannot settle - "
        "sitting still feels wrong - but you also cannot find anything "
        "worth doing, so the energy has nowhere to go. The result is the "
        "classic fidget: leg bouncing, pen clicking, phone picked up and "
        "put down, rooms paced. The mind mirrors the body - thoughts "
        "start, abort, restart; plans are made and discarded in minutes. "
        "This is agitated boredom, and it is more uncomfortable than plain "
        "boredom because two alarms are ringing at once: the mind's alarm "
        "(nothing here engages me) and the body's alarm (I need to move, "
        "to act, to spend this energy). The blend explains behaviors that "
        "pure boredom would not: why a bored person snaps at a harmless "
        "question, why they start arguments or take sudden risks, why they "
        "cannot simply sit with the feeling. The restlessness wants "
        "discharge; the boredom withholds direction. Understanding the blend "
        "is the key to answering it: the body needs motion and the mind "
        "needs meaning, and giving only one leaves the other still ringing."),
    how_it_works=(
        "The blend forms when two systems misfire together. The attention "
        "system reports failed engagement - that is the boredom half. The "
        "arousal system, meanwhile, is running hot - the body is primed for "
        "action with no action assigned - that is the restlessness half. "
        "Normally these two coordinate: high arousal pairs with high "
        "engagement (excitement, urgency), and low arousal pairs with low "
        "engagement (calm, rest). The blend is the mismatched pairing: "
        "high arousal with low engagement, which the nervous system reads "
        "as an emergency with no instructions. That is why the blend feels "
        "urgent and miserable at once. The remedy must serve both masters: "
        "discharge the arousal through movement - a walk, exercise, "
        "physical work - and then give the calmed attention something "
        "worthy to engage with. Doing only the walk leaves the mind still "
        "hungry; doing only the puzzle leaves the body still buzzing. The "
        "order matters too: move first, then engage, because a buzzing "
        "body will not let attention settle."),
    key_points=[
        "The most common blend: flat boredom with an engine running underneath.",
        "Two alarms ring at once: the mind's (nothing engages me) and the body's (I must move).",
        "The blend explains snapping, fidgeting, and sudden risk-taking.",
        "Remedy both halves: discharge the body first, then engage the mind.",
        "Order matters - a buzzing body will not let attention settle.",
    ],
    requirements=[
        "The blend described from the inside",
        "Why the blend is worse than either half alone",
        "Two-part remedy with the order explained",
    ],
    standards=["Arousal-attention mismatch model; Eastwood attention account"],
    citations=[CIT_EASTWOOD, CIT_BENCH],
    sig_lens=(
        "His Signature lens sees the blend as a warhorse with no battle: "
        "the body pawing the ground, the rider scanning an empty field. "
        "The Signature answer honors both horse and rider - the horse gets "
        "its run, the rider gets its campaign. To move first and then "
        "engage is the ancient discipline of the restless strong: sweat "
        "before study, march before council. The blend, mastered, becomes a "
        "two-stroke engine - motion feeding focus, focus directing motion - "
        "and the person who learns its rhythm gains a power the merely "
        "calm never touch.")),
dict(
    key="boredom_day_vignette", name="A Day in the Life: Boredom Running Through an Ordinary Day",
    group="Foundations", ladder_rank=9, ladder_tier="foundations",
    description=(
        "Morning: the alarm, the routine, the commute - the day starts on "
        "rails, and boredom is nowhere to be found while attention has "
        "work to do. Mid-morning: the tasks thin out. Emails answered, the "
        "next meeting an hour away. Attention starts to skim; the clock "
        "gets its first check. A low hum of restlessness sets in, barely "
        "noticed. Lunch: the break helps - food, a walk, a conversation - "
        "and the dial drops back down. Early afternoon: the long flat "
        "stretch. Repetitive tasks, nothing at stake, the room too warm. "
        "This is the day's boredom peak: sighs, heavy eyes that are not "
        "sleepy, the phone checked eleven times, time moving like cold "
        "honey. A small irritation flares at a coworker's humming. Late "
        "afternoon: a genuinely interesting problem lands, and attention "
        "locks on - the boredom vanishes so completely it feels like it "
        "was never there. This is the signature move of boredom: it "
        "evaporates the instant real engagement arrives. Evening: the day "
        "is done, and the residue lingers - a flat tiredness that is not "
        "from work but from unengaged hours, plus a rebound hunger for "
        "stimulation that makes the evening scroll go longer than planned. "
        "The vignette shows the whole database in one day: onset, climb, "
        "peak, release, and aftershock."),
    how_it_works=(
        "The day works as a teaching model because it displays every "
        "mechanism in sequence. The mid-morning skim shows onset: attention "
        "losing its grip as task-demand falls. The afternoon peak shows "
        "the full mismatch: low challenge, low meaning, long duration, "
        "little choice - every dial turned the wrong way. The phone checks "
        "show the urge for change expressing itself as cheap "
        "stimulation-seeking. The late-afternoon rescue shows the cure in "
        "action: genuine engagement - a problem with real stakes - "
        "recaptures attention instantly, proving boredom was never about "
        "energy but about fit. The evening residue shows the aftershock: "
        "fatigue debt from unengaged arousal plus rebound appetite. Walk a "
        "learner through this day slowly and they gain a template for "
        "reading their own days: where is my dial right now, which phase "
        "am I in, and what would genuine engagement look like here? The "
        "vignette turns the abstract model into a familiar story, which is "
        "how understanding becomes usable."),
    key_points=[
        "Boredom peaks in the day's flat stretches - low challenge, low meaning, long duration.",
        "The signature move: boredom evaporates instantly when genuine engagement arrives.",
        "Phone-checking and sighing are the urge for change seeking cheap outlets.",
        "Evening residue - flat tiredness plus rebound scrolling - is the aftershock.",
        "The day is a template for reading your own hours: which phase am I in?",
    ],
    requirements=[
        "Full-day arc with five phases",
        "Each phase mapped to a mechanism",
        "The template made usable for self-reading",
    ],
    standards=["Ecological momentary description; MSBS state structure"],
    citations=[CIT_FAHLMAN, CIT_MANN],
    sig_lens=(
        "His Signature lens walks the day as a steward walks his fields: "
        "morning rails, mid-morning thinning, afternoon fallow, the rescue "
        "of real work, the evening settling. The Signature reading finds "
        "the day's moral in the late-afternoon rescue - the instant "
        "evaporation of boredom before genuine engagement proves the soul "
        "was never broken, only unassigned. The steward's lesson: farm the "
        "flat stretches. Plant challenge in the morning's plan, meaning in "
        "the afternoon's tasks, and the fallow hours shrink to nothing. A "
        "well-stewarded day has no desert in it.")),
]
# ---------------------------------------------------------------- 10-13: body signals
ENTRIES += [
dict(
    key="boredom_body_signals", name="What Happens in the Body During Boredom",
    group="Compounded", ladder_rank=10, ladder_tier="compounded",
    description=(
        "Boredom writes itself across the body in a quiet, heavy script. The "
        "heart does not race as it does in fear or anger; it idles - steady, "
        "unhurried, sometimes seeming to beat slower as arousal sinks. "
        "Breathing grows shallow and sigh-heavy: the bored body sighs "
        "without deciding to, long exhalations that vent the restlessness "
        "the moment cannot spend. Muscles go slack rather than tense - "
        "shoulders droop, the jaw hangs a little open, the whole frame "
        "seems to settle downward as if gravity had increased. The stomach "
        "is usually quiet; boredom is not a gut-churning emotion. The skin "
        "may feel oddly alert to small irritations - a tag on a shirt, a "
        "hum in the room - because with attention unoccupied, minor "
        "sensations get promoted. Energy drains in a peculiar way: not the "
        "clean tiredness after hard work, but a flat heaviness, as if the "
        "body were conserving fuel for something that never comes. And yet, "
        "underneath the slackness, there can be a buzzing - the agitated "
        "face of boredom keeps the engine idling high while the wheels do "
        "not turn. Reading these signals matters because the body reports "
        "boredom before the mind names it: the sighs arrive before the "
        "thought 'I am bored' does."),
    how_it_works=(
        "The body pattern follows from the attention-arousal mismatch. "
        "With no engaging target, the sympathetic nervous system has "
        "nothing to mobilize for, so gross arousal stays low - the slack "
        "muscles, the idling heart, the heavy energy. But the urge for "
        "change keeps a thread of arousal alive, which leaks out as sighs, "
        "fidgets, and skin-level irritability. Sighing is the tell: "
        "research on boredom-adjacent states treats the spontaneous sigh as "
        "a reset attempt, the body trying to break the stalemate. The "
        "heaviness is conservation - the system idling its engine while it "
        "waits for instructions that do not come. The skin irritability is "
        "attention with nowhere to go, spilling onto the nearest channel. "
        "Two body profiles emerge from the same mechanism: the lethargic "
        "profile, where arousal sinks and the body melts into the chair, "
        "and the agitated profile, where arousal stays up and the body "
        "fidgets against the stillness. Both are the same unengaged "
        "attention wearing different arousal clothes - which is why the "
        "remedies differ: rest and gentle re-entry for the melted, movement "
        "first for the buzzing."),
    key_points=[
        "The bored body sighs, slacks, and heavies - heart idles, muscles droop, energy flattens.",
        "Sighing is the tell: the body trying to break the stalemate.",
        "Minor skin irritations get promoted because unoccupied attention spills onto them.",
        "Two profiles: lethargic (melted into the chair) and agitated (buzzing against stillness).",
        "The body reports boredom before the mind names it - read the sighs early.",
    ],
    requirements=[
        "Six body channels described: heart, breath, muscles, stomach, skin, energy",
        "The two arousal profiles with their different remedies",
        "Why sighing is the signature tell",
    ],
    standards=["Psychophysiology of boredom; MSBS disengagement items"],
    citations=[CIT_FAHLMAN, CIT_DANCKERT],
    sig_lens=(
        "His Signature lens reads the bored body as a garrison at ease "
        "with no orders: banners furled, sentries leaning, the gates "
        "unbarred - yet every soldier still in armor. The slackness is not "
        "weakness but readiness without assignment; the sigh is the "
        "garrison's collective exhale, waiting for the commander's voice. "
        "The Signature commander does not scold the garrison for idleness - "
        "he gives it a campaign. Movement first for the buzzing troops, "
        "rest and rally for the melted ones, and then a worthy objective "
        "that makes every muscle remember its purpose. A body with orders "
        "never sighs at the walls.")),
dict(
    key="boredom_posture_movement", name="The Posture and Movement Signature of Boredom",
    group="Compounded", ladder_rank=11, ladder_tier="compounded",
    description=(
        "You can spot boredom across a room by posture alone. The classic "
        "bored posture is the melt: chin propped on a hand, elbow on the "
        "table, spine curved like a question mark, the whole upper body "
        "leaning on whatever is nearest. The head tilts or lolls; the gaze "
        "drifts to windows, ceilings, and middle distance. Then there is "
        "the fidget suite - the movement signature of agitated boredom: "
        "foot tapping, pen clicking, hair twisting, chair rocking, the "
        "endless small motions of a body trying to spend energy the moment "
        "will not accept. Pacing is the full-body version: short, aimless "
        "walks to nowhere - to the window, to the fridge, back to the "
        "chair - each trip a small expedition in search of something to "
        "happen. People also perform displacement activities: rearranging "
        "objects, doodling, checking devices, tidying things that do not "
        "need tidying. These are not random tics; they are the urge for "
        "change wearing a disguise, manufacturing tiny novelties when the "
        "world provides none. Posture and movement are boredom's most "
        "honest channel - harder to fake than the face, harder to hide "
        "than words - because the body cannot help acting out what "
        "attention is failing to do."),
    how_it_works=(
        "Posture follows attention the way a shadow follows a body. When "
        "attention engages, the body orients: spine straightens, head "
        "levels, hands go still and ready. When attention disengages, the "
        "orientation system powers down, and the body collapses into its "
        "lowest-energy shape - the melt. The fidget suite is the arousal "
        "half of the blend leaking through: with the urge for change "
        "active but no target assigned, the motor system discharges in "
        "small, purposeless loops. Pacing and displacement activities are "
        "the same mechanism scaled up - the system manufacturing its own "
        "micro-novelty. This is why the posture channel is so reliable for "
        "readers of others: people can school their faces and choose their "
        "words, but the slow melt of the spine and the unconscious foot-tap "
        "escape management. For the bored person themselves, the channel "
        "works in reverse too - deliberately straightening up and moving "
        "with purpose can feed back into attention, because the body and "
        "the mind keep a two-way line. Change the posture, and attention "
        "often follows the body back to work."),
    key_points=[
        "The melt - chin on hand, curved spine, drifting gaze - is boredom's classic posture.",
        "The fidget suite - tapping, clicking, rocking - is the urge for change in disguise.",
        "Pacing and displacement activities manufacture micro-novelty when the world provides none.",
        "Posture is the most honest channel: harder to fake than the face, harder to hide than words.",
        "The line runs both ways - deliberate upright posture can help recall attention.",
    ],
    requirements=[
        "Classic posture described precisely",
        "Fidget suite and displacement activities explained",
        "Why posture is the most honest channel",
    ],
    standards=["Behavioral observation literature; Eastwood attention account"],
    citations=[CIT_EASTWOOD, CIT_MANN],
    sig_lens=(
        "His Signature lens sees posture as the body's oath about the "
        "mind's state. The melt is a flag lowered - attention striking its "
        "colors because no worthy wind fills them. The fidget is a drum "
        "beating without a march - energy demanding a destination. The "
        "Signature discipline is to raise the flag by hand: spine tall, "
        "gaze leveled, movements chosen rather than leaked. This is not "
        "pretense - it is command. The body is the most obedient soldier "
        "in the kingdom, and when the commander stands tall, attention "
        "falls in beside him. Posture is where mastery of boredom begins, "
        "because it is the one channel you can set by pure decision.")),
dict(
    key="boredom_sleep_appetite_energy", name="Boredom, Sleep, Appetite, and Energy",
    group="Compounded", ladder_rank=12, ladder_tier="compounded",
    description=(
        "Boredom tangles with the body's basic systems in confusing ways. "
        "Sleep: boredom is not sleepiness, but it borrows sleep's costume. "
        "The heavy eyes, the yawning, the urge to nap in the middle of the "
        "day - these are disengagement wearing drowsiness as a disguise. "
        "Real sleep debt feels different: it lifts with rest. Boredom's "
        "heaviness does not lift with a nap; people often wake from a "
        "boredom-nap feeling worse, because the unengaged hours simply "
        "continued in dreams. Appetite: the bored hand reaches for snacks it "
        "is not hungry for. Eating is one of the cheapest available "
        "novelties - flavor, texture, the small event of it - so the urge "
        "for change recruits the mouth. This is why empty afternoons fill "
        "with grazing: not hunger, but the search for something to happen. "
        "Energy: boredom drains it without spending it. The day ends with "
        "the peculiar exhaustion of having done nothing - the fatigue debt "
        "of sustained unengaged arousal. The cruel loop is that this flat "
        "tiredness then blocks the very engagement that would cure it: too "
        "tired to start something worthwhile, too unengaged to rest "
        "properly. Breaking the loop means recognizing which tiredness you "
        "are feeling - the clean tiredness of effort, which wants rest, or "
        "the flat tiredness of boredom, which wants engagement."),
    how_it_works=(
        "Each tangle has its own mechanics. The sleep confusion happens "
        "because disengaged attention and sleep onset share signals - heavy "
        "eyes, yawning, drifting thought - so the bored brain misreads its "
        "own state and prescribes the wrong cure. Napping on boredom fails "
        "because the deficit was never energy; it was engagement, and "
        "sleep does not supply that. The appetite link runs through the "
        "urge for change: with novelty scarce, the brain promotes any "
        "available micro-event, and food is the most reliable one in a "
        "modern room - hence grazing without hunger. The energy drain is "
        "the cost of the stalemate: maintaining unengaged arousal - the "
        "engine idling, the attention searching - burns fuel without "
        "producing anything, like a car stuck in traffic with the motor "
        "running. The flat tiredness that results then raises the bar for "
        "starting anything worthwhile, which deepens the boredom, which "
        "deepens the tiredness. The exit is diagnosis before prescription: "
        "ask whether rest would genuinely help; if the answer is no, the "
        "tiredness is boredom's, and the cure is engagement, not the couch."),
    key_points=[
        "Boredom borrows sleep's costume - heavy eyes and yawning - but naps do not cure it.",
        "Boredom-grazing is not hunger; it is the urge for change recruiting the mouth.",
        "Boredom drains energy without spending it - the fatigue debt of the stalemate.",
        "Flat tiredness then blocks the engagement that would cure it: the cruel loop.",
        "Diagnose before prescribing: clean tiredness wants rest, flat tiredness wants engagement.",
    ],
    requirements=[
        "Sleep, appetite, and energy each untangled from boredom",
        "Why the boredom-nap fails and grazing happens",
        "The cruel loop and how to break it",
    ],
    standards=["MSBS items on time and disengagement; sleep-boredom differentiation literature"],
    citations=[CIT_FAHLMAN, CIT_DANCKERT],
    sig_lens=(
        "His Signature lens treats the body's confusions as false messengers "
        "to be questioned at the gate. The yawning messenger claims the "
        "kingdom needs sleep; interrogation reveals it needs purpose. The "
        "grazing messenger claims hunger; interrogation reveals hunger for "
        "events. The tired messenger claims exhaustion; interrogation "
        "reveals unspent fuel, not spent fuel. The Signature steward "
        "questions every messenger before obeying any: is this clean "
        "tiredness or flat tiredness, true hunger or hollow hunger? False "
        "messengers obeyed become true problems - the nap that deepens the "
        "fog, the snack that feeds nothing. Questioned at the gate, they "
        "dissolve, and the true need stands revealed.")),
dict(
    key="boredom_body_differences", name="How Boredom Feels Different in Different Bodies",
    group="Compounded", ladder_rank=13, ladder_tier="compounded",
    description=(
        "No two bodies do boredom exactly alike, and the differences "
        "matter for recognition and remedy. Some people live mostly in the "
        "agitated profile: their boredom is all fidget and pace, the "
        "engine loud, sleep impossible during it. Others live in the "
        "lethargic profile: their boredom is melt and heaviness, the body "
        "sinking, naps tempting. Age shifts the pattern: children show "
        "boredom as pure motion - they cannot sit with it and explode into "
        "activity or mischief - while older adults more often show the "
        "quiet melt. Temperament sets the threshold: highly curious, "
        "high-energy people feel the mismatch sooner and louder, because "
        "their appetite for engagement is larger; they are not weaker for "
        "it, only hungrier. Habit shapes the channel: the habitual scroller "
        "feels boredom as an itch toward the phone, the habitual snacker "
        "as an itch toward the kitchen - the urge for change wears the "
        "grooves of past escapes. Health and state modulate everything: "
        "poor sleep, low mood, or hormonal shifts can all lower the "
        "threshold, so the same afternoon that was fine last week feels "
        "unbearable today. The lesson is personal calibration: learn your "
        "own body's dialect of boredom - melt or buzz, phone or fridge, "
        "morning or afternoon - because the remedy that works is the one "
        "fitted to your pattern, not to someone else's."),
    how_it_works=(
        "The differences arise because boredom is built from shared "
        "mechanisms running on different hardware. The attention-arousal "
        "mismatch is universal, but baseline arousal varies: high-arousal "
        "temperaments produce the buzzing profile, low-arousal "
        "temperaments the melting one. Developmental stage sets the "
        "behavioral repertoire: children lack the learned stillness that "
        "lets adults sit with disengagement, so their urge for change "
        "expresses as motion. Appetite size - curiosity, energy, need for "
        "stimulation - sets the gain on the mismatch signal: bigger "
        "appetite, louder alarm at the same objective dullness. Learned "
        "grooves explain the channel differences: the brain, seeking the "
        "cheapest novelty, replays whatever escape worked before, "
        "strengthening that path each time. State factors like sleep debt "
        "lower the threshold by degrading attention's ability to engage at "
        "all. None of this changes the core model - it only changes the "
        "accent. A complete account of boredom must therefore be "
        "two-layered: the universal mechanism, plus the personal dialect. "
        "Teach the mechanism first, then invite the learner to map their "
        "own dialect onto it."),
    key_points=[
        "Agitated vs lethargic profiles are the two main body dialects of boredom.",
        "Children show boredom as motion; adults more often as the quiet melt.",
        "Bigger appetites for engagement mean louder boredom - hunger, not weakness.",
        "The urge for change wears the grooves of past escapes: phone, fridge, pace.",
        "Calibrate personally: learn your own dialect to fit the remedy.",
    ],
    requirements=[
        "Profiles, age, temperament, habit, and state differences",
        "Why bigger appetites mean louder boredom",
        "Personal calibration as the takeaway",
    ],
    standards=["Individual-differences literature; SBPS trait boredom proneness"],
    citations=[CIT_STRUK, CIT_DANCKERT],
    sig_lens=(
        "His Signature lens honors the dialects as regimental colors: every "
        "soul's garrison flies its own flag in the waiting, and the wise "
        "commander learns his own colors by heart. The buzzer's flag is "
        "motion; the melter's is stillness; the child's is eruption; the "
        "hungry mind's is a louder alarm. The Signature error is to envy "
        "another regiment's colors - wishing your buzz were someone else's "
        "calm. The Signature discipline is to drill your own troops as "
        "they are: move-first remedies for the buzzing, gentle re-entry "
        "for the melting, worthy campaigns sized to your own appetite. "
        "Know your colors, and no waiting ever catches you unformed.")),
# ---------------------------------------------------------------- 14-17: facial expression
dict(
    key="boredom_face", name="The Face of Boredom: Eyes, Brows, Mouth, and Micro-Signs",
    group="Compounded", ladder_rank=14, ladder_tier="compounded",
    description=(
        "Boredom's face is the face of attention leaving the room. The "
        "eyes are the headline: gaze drifts to the middle distance, "
        "focus softens, blinking slows or becomes heavy-lidded. The "
        "classic tell is the unfocused stare - looking at something "
        "without seeing it, the eyes pointed at a speaker while attention "
        "is elsewhere. The brows sit neutral to slightly raised in the "
        "middle, giving a faintly mournful cast; there is none of anger's "
        "drawn-together intensity. The mouth goes slack: lips part "
        "slightly or press into a flat, downturned line, the corners "
        "drooping. The jaw may hang a fraction open. Micro-signs complete "
        "the portrait: the slow blink, the suppressed yawn (or the "
        "unsuppressed one), the brief eye-roll when the dullness is "
        "another person's doing, the chin sinking toward the propping "
        "hand. Unlike the basic emotions, boredom has no single universal "
        "muscle signature - researchers note it is read more from the "
        "whole configuration, and especially from the eyes, than from any "
        "one feature. The face is honest because attention is hard to "
        "fake: you can arrange your mouth, but you cannot arrange your "
        "gaze to look engaged when it is not - the unfocused stare always "
        "leaks through."),
    how_it_works=(
        "The face follows the same attention logic as the body. Engaged "
        "attention drives the orienting response: eyes lock, lids lift, "
        "brows set, the face aims itself at the target. Disengaged "
        "attention withdraws the drive, and the facial muscles return to "
        "their resting state - which reads as slackness, droop, and drift. "
        "The eyes are the most reliable channel because gaze direction and "
        "focus are under tight coupling with attention itself; you cannot "
        "sustain a genuinely focused gaze while attention is elsewhere, "
        "which is why the thousand-yard stare is the giveaway. The yawn "
        "and slow blink are the arousal system signaling its idle state. "
        "The eye-roll is a social overlay - a commentary on the source of "
        "the dullness, not part of the core signal. Because there is no "
        "dedicated 'boredom muscle,' readers integrate the whole pattern: "
        "slack mouth plus drifting eyes plus still brows equals the "
        "verdict. This configural reading is also why boredom is sometimes "
        "misread as sadness (the droop) or tiredness (the lids) - the "
        "disambiguator is context plus the restless micro-movements that "
        "sadness and tiredness lack."),
    key_points=[
        "The eyes headline: drifting gaze, softened focus, the unfocused stare.",
        "Mouth goes slack, corners droop; brows sit neutral, not knitted.",
        "Micro-signs: slow blink, yawn, eye-roll, chin sinking to hand.",
        "No single universal muscle signature - the whole configuration is read, eyes first.",
        "The unfocused stare always leaks; attention cannot be faked in the gaze.",
    ],
    requirements=[
        "Eyes, brows, mouth, and micro-signs each described",
        "Why the gaze is the most reliable channel",
        "How boredom's face is misread as sadness or tiredness",
    ],
    standards=["Facial expression literature; configural emotion recognition"],
    citations=[CIT_EASTWOOD, CIT_DANCKERT],
    sig_lens=(
        "His Signature lens reads the bored face as a castle with its "
        "windows dark: the eyes are the windows, and when attention "
        "departs, the lamps go out - no arrangement of curtains can fake "
        "the light. The slack mouth is the lowered drawbridge; the "
        "drifting gaze, the watchman asleep at his post. The Signature "
        "sentinel learns to keep the lamps lit by will: gaze deliberately "
        "placed, lids lifted, the face aimed at the matter at hand. This "
        "is not deception - it is duty. A commander who keeps his windows "
        "lit finds that attention, like a loyal guard, returns to a lit "
        "post sooner than to a dark one.")),
dict(
    key="boredom_face_intensity", name="How Boredom's Expression Changes With Intensity",
    group="Compounded", ladder_rank=15, ladder_tier="compounded",
    description=(
        "At mild intensity, boredom's face is barely a whisper: a slightly "
        "longer blink, a gaze that wanders for a second before returning, "
        "a mouth that relaxes out of its attentive set. An observer might "
        "read it as mere thoughtfulness. At moderate intensity, the "
        "signals consolidate: the stare lengthens and empties, the lids "
        "grow heavy, sighs become audible, the chin finds the hand. The "
        "face now clearly reports disengagement, though it stays "
        "socially acceptable - the polite mask of the bored meeting-goer, "
        "attention gone but manners intact. At high intensity, the mask "
        "slips: open yawning, frank staring past people, the eye-roll, "
        "exaggerated sighs, the head lolling or dropping. The face stops "
        "pretending and starts protesting. There is also a qualitative "
        "shift people miss: at low intensity the face shows drifting "
        "attention, but at high intensity it shows suffering attention - "
        "the features do not just go slack, they contort slightly with "
        "the effort of enduring, brows lifting in the middle in a "
        "near-mournful cast. Reading intensity from the face is a "
        "practical skill: the whisper needs only a small redirect, the "
        "consolidated mask needs real engagement or release, and the "
        "protest means the situation itself must change."),
    how_it_works=(
        "Intensity scales the expression through two mechanisms: signal "
        "strength and control failure. As the engagement gap widens, the "
        "underlying signal - disengaged attention, idle arousal - grows "
        "stronger, so the slackness deepens and the drift lengthens. At "
        "the same time, the effort of masking has a cost, and as "
        "restlessness rises, control resources drain - the polite mask is "
        "expensive to hold, and the high-intensity face is what leaks when "
        "the budget runs out. The qualitative shift from drifting to "
        "suffering reflects the blend tipping toward the agitated pole: "
        "the mournful brow-cast and the contortion are the urge for change "
        "pressing against the social requirement to sit still. This gives "
        "readers a two-axis tool: how slack is the face (signal strength) "
        "and how much protest is showing (control failure). High slack "
        "with good control means deep but managed boredom; high slack "
        "with protest means the person is near the limit of endurance and "
        "the situation - not the person - needs to change."),
    key_points=[
        "Mild: the whisper - longer blinks, brief gaze wanders, easily mistaken for thoughtfulness.",
        "Moderate: the consolidated mask - empty stare, heavy lids, chin on hand, manners intact.",
        "High: the protest - open yawning, eye-rolls, exaggerated sighs, the mask slipped.",
        "Intensity scales through signal strength plus control failure.",
        "Read two axes: slackness (how deep) and protest (how near the limit).",
    ],
    requirements=[
        "Three intensity faces described distinctly",
        "The drift-to-suffering qualitative shift",
        "Two-axis reading tool for observers",
    ],
    standards=["Expression-intensity scaling literature; display-rule research"],
    citations=[CIT_DANCKERT, CIT_MANN],
    sig_lens=(
        "His Signature lens watches the face through the three watches of "
        "the night: the whisper-watch, where the sentry merely nods; the "
        "mask-watch, where discipline still holds the post; the "
        "protest-watch, where the garrison openly demands relief. The "
        "Signature officer respects what each watch reports: the whisper "
        "asks for a small redirect, the mask for real engagement, the "
        "protest for a changed situation. And he trains his own face as "
        "he trains his troops - to hold the mask-watch with dignity when "
        "duty requires it, and to answer the protest-watch honestly by "
        "changing the orders, not by breaking.")),
dict(
    key="boredom_hiding_faking", name="Hiding Boredom and Faking Interest: What Leaks Through",
    group="Compounded", ladder_rank=16, ladder_tier="compounded",
    description=(
        "People hide boredom constantly - in meetings, classrooms, "
        "conversations - and the standard toolkit is familiar: the "
        "arranged nod, the fixed smile, the strategic 'mm-hmm,' the pen "
        "held as if taking notes. Faking interest uses the same props in "
        "reverse: leaning slightly forward, eyebrows raised in performed "
        "curiosity, questions asked from duty rather than appetite. Both "
        "performances leak, and they leak in the same places. The gaze is "
        "the first traitor: the unfocused stare returns within seconds, "
        "because sustained fake focus is cognitively expensive. The blink "
        "rate betrays: slow, heavy blinks puncture the performance. "
        "Micro-sighs escape. The body contradicts the face: the mouth "
        "smiles while the foot taps, the head nods while the shoulders "
        "melt. Timing gives it away too - the nod comes a beat late, the "
        "'mm-hmm' lands after the pause where a real response would have "
        "been. And there is the rebound tell: the moment the performance "
        "can drop - the meeting ends, the guest leaves - the face "
        "collapses into the full melt all at once, revealing how much "
        "effort the mask was costing. None of this makes the hider "
        "dishonest; masking boredom is usually politeness, not deceit. "
        "But knowing the leaks helps both sides: the performer can learn "
        "cleaner masking, and the observer can learn kinder reading - "
        "seeing the leak not as rudeness but as a signal that the "
        "situation needs more life."),
    how_it_works=(
        "Masking fails asymmetrically because the channels differ in "
        "controllability. The mouth and the nod are under voluntary "
        "control and can be arranged; the gaze, blink rate, and sighing "
        "are tightly coupled to attention and arousal and resist "
        "arrangement. This is the classic leakage hierarchy: what is "
        "closest to the underlying state leaks most. Sustained fake "
        "engagement is also resource-hungry - it requires simulating the "
        "very attention that is absent - so the performance degrades over "
        "time, with leaks increasing the longer the mask is held. The "
        "timing tells (late nods, delayed mm-hmms) come from the same "
        "source: without real engagement driving responses, the performer "
        "must consciously generate each one, adding a processing delay. "
        "The rebound collapse is the release of the control budget all at "
        "once. For the observer, the practical rule is to read the "
        "cheapest channels - eyes, blinks, posture - and to interpret "
        "leaks as data about the situation, not as verdicts on the "
        "person. For the performer, the honest options are better masking "
        "through genuine micro-engagement (finding one interesting thread "
        "to actually follow) or changing the situation so no mask is "
        "needed."),
    key_points=[
        "The toolkit: arranged nods, fixed smiles, strategic mm-hmms, the note-taking pen.",
        "The gaze is the first traitor - fake focus is cognitively expensive.",
        "Leakage hierarchy: eyes, blinks, and sighs resist control; mouth and nods can be arranged.",
        "Timing tells: late nods and delayed responses reveal conscious generation.",
        "Read leaks as data about the situation, not verdicts on the person.",
    ],
    requirements=[
        "Hiding and faking toolkits described",
        "Leakage hierarchy explained",
        "Kinder reading framed for observers",
    ],
    standards=["Display-rule and leakage research; Ekman on controllable vs autonomic channels"],
    citations=[CIT_DANCKERT, CIT_EASTWOOD],
    sig_lens=(
        "His Signature lens treats the mask as a soldier's parade uniform: "
        "honorable when duty requires it, exhausting to wear all day, and "
        "never to be mistaken for the soldier. The leaks are not failures "
        "of character but the truth reporting for duty through the "
        "channels no uniform covers. The Signature performer has two "
        "honorable options: wear the uniform well by finding one true "
        "thread of interest to actually follow - a real engagement inside "
        "the required performance - or change the orders so no uniform is "
        "needed. What the Signature code forbids is contempt for the "
        "leak: the eye-roll at another's mask is the one true rudeness, "
        "because it punishes honesty for showing.")),
dict(
    key="boredom_expression_gallery", name="Expression Gallery Notes: Boredom for Artists and Actors",
    group="Compounded", ladder_rank=17, ladder_tier="compounded",
    description=(
        "For the artist or actor who must render boredom: begin with the "
        "eyes, because everything else is commentary. Paint or play the "
        "gaze unfocused - not looking down (that reads as sadness) and "
        "not looking away sharply (that reads as contempt), but looking "
        "through: the focal point set somewhere behind the visible world. "
        "Soften the lids to three-quarter mast; let one slow blink carry "
        "the whole performance. The brows rest neutral, perhaps with the "
        "inner corners lifted a fraction - the faintest mournful cast, "
        "never knitted. The mouth: let it slacken open a finger's width, "
        "or press it into a flat line with the corners weighted down. "
        "Avoid the smile entirely - even a polite one - because the "
        "audience reads smiles as engagement. Set the head at a slight "
        "tilt or let it sink toward the propping hand; the chin-on-fist is "
        "boredom's most legible prop. The shoulders round forward and "
        "down. For agitated boredom, add the counterpoint: still face, "
        "busy extremities - the tapping foot, the drumming fingers - "
        "because the blend's truth is calm above the neck and storm below "
        "it. For the late-stage mask-slip, add the yawn caught half-open "
        "or the eye-roll frozen mid-arc. Light it flat and even - boredom "
        "has no dramatic shadows; its drama is the absence of drama. The "
        "final note for the actor: do not play the feeling of boredom, "
        "play the failure of attention - let your eyes genuinely lose "
        "their target, and the audience will feel the room go quiet."),
    how_it_works=(
        "The gallery notes work because they translate the configural "
        "signal into renderable instructions. 'Looking through' captures "
        "the unfocused stare more precisely than any muscle code: it tells "
        "the artist where to set the focal point rather than which muscle "
        "to move. The warnings - not down (sadness), not away sharply "
        "(contempt) - teach discrimination between neighboring "
        "configurations, which is the core skill of expression rendering. "
        "The agitated-boredom counterpoint (still face, busy hands) encodes "
        "the blend's two-system structure in a single stage picture. The "
        "lighting note captures a truth about the emotion's phenomenology: "
        "boredom flattens salience, so dramatic chiaroscuro would lie "
        "about the inner state. The actor's final note - play the failure "
        "of attention, not the feeling - is methodologically sound: "
        "genuinely disengaging attention produces the authentic facial "
        "configuration automatically, while 'acting bored' from the "
        "outside produces caricature. These notes make the database's "
        "expression records usable by makers, not just readers."),
    key_points=[
        "Start with the eyes: the unfocused stare, looking through rather than at.",
        "Lids at three-quarter mast; one slow blink can carry the performance.",
        "Discriminate neighbors: not down (sadness), not sharply away (contempt).",
        "Agitated boredom is a stage picture: still face, busy extremities.",
        "The actor's rule: play the failure of attention, not the feeling of boredom.",
    ],
    requirements=[
        "Renderable instructions for eyes, brows, mouth, head, shoulders",
        "Neighbor discrimination notes",
        "Agitated variant and mask-slip variant",
    ],
    standards=["Configural expression rendering; performance methodology"],
    citations=[CIT_DANCKERT, CIT_EASTWOOD],
    sig_lens=(
        "His Signature lens hands the artist a deeper commission: do not "
        "paint the empty room - paint the lit lamps waiting in it. The "
        "unfocused stare, in this lens, is attention standing at the "
        "window looking for its assignment; render the readiness inside "
        "the vacancy, and the portrait becomes noble instead of pathetic. "
        "The Signature portrait of boredom shows a guardian between "
        "duties, not a hollow shell - the slack mouth as a sheathed "
        "sword, the drifting gaze as a scout scanning the horizon. Paint "
        "that, and the viewer will not pity the subject; they will want "
        "to hand him a quest.")),
# ---------------------------------------------------------------- 18-21: triggers
dict(
    key="boredom_classic_triggers", name="The Classic Triggers of Boredom",
    group="Compounded", ladder_rank=18, ladder_tier="compounded",
    description=(
        "Certain situations trigger boredom so reliably they are practically "
        "laboratories for it. The waiting room: enforced stillness, nothing "
        "to engage with, duration unknown - every dial turned wrong. The "
        "dull meeting: low challenge, low meaning, no choice about "
        "attending, attention required but unrewarded. Repetitive tasks: "
        "the assembly line, the data entry, the hundredth identical form - "
        "challenge far below skill, the mind starving while the hands "
        "work. The empty stretch: the long afternoon with no plans, the "
        "cancelled event, the gap between things - unstructured time with "
        "nothing to fill it. The captive audience: lectures, sermons, "
        "briefings where the content is over-familiar or irrelevant and "
        "leaving is not permitted. The familiar loop: the commute, the "
        "routine, the day identical to yesterday - novelty at zero. "
        "Confinement: the traffic jam, the delayed flight, the sickbed - "
        "the body caged and the mind unoccupied at once. Each classic "
        "trigger shares the same skeleton: wanted engagement high, offered "
        "engagement low, duration long, choice low. Learn the skeleton and "
        "you can predict boredom before it arrives - and redesign the "
        "situation, where you have the power, so the skeleton never "
        "assembles."),
    how_it_works=(
        "The triggers work by assembling the mismatch from standard parts. "
        "Waiting rooms remove choice and novelty while stretching duration "
        "into the unknown - uncertainty about duration is itself a "
        "multiplier, because the mind cannot budget its patience. Dull "
        "meetings combine low challenge with low meaning and add the "
        "insult of required attention: the system must spend focus and "
        "gets nothing back, which breeds resentment alongside the "
        "boredom. Repetitive tasks starve the challenge channel while the "
        "skill sits idle - the flow model predicts this exactly: skill "
        "high, challenge low, the result is boredom by definition. Empty "
        "stretches remove structure, and structure is attention's "
        "scaffolding; without it the mind must self-generate engagement, "
        "which is effortful and fails often. Confinement adds the body's "
        "protest to the mind's, tipping the blend toward agitation. The "
        "practical use of the catalog is twofold: prediction (see the "
        "skeleton assembling, intervene early with challenge, meaning, "
        "novelty, or choice) and design (where you control the situation - "
        "a meeting you run, a classroom you teach - break the skeleton "
        "apart before it forms)."),
    key_points=[
        "Seven classics: waiting rooms, dull meetings, repetitive tasks, empty stretches, captive audiences, familiar loops, confinement.",
        "Every trigger shares one skeleton: high wanted engagement, low offered engagement, long duration, low choice.",
        "Uncertain duration multiplies the effect - the mind cannot budget patience.",
        "Repetitive tasks are flow theory's boredom quadrant: skill high, challenge low.",
        "Learn the skeleton to predict boredom early and design situations that never assemble it.",
    ],
    requirements=[
        "Seven classic triggers with their mechanics",
        "The shared skeleton stated plainly",
        "Prediction and design as practical uses",
    ],
    standards=["Flow theory quadrants (Csikszentmihalyi 1990); MSBS trigger items"],
    citations=[CIT_CSIKSZENTMIHALYI, CIT_MANN],
    sig_lens=(
        "His Signature lens names the seven triggers the seven sieges: "
        "standard formations by which dullness besieges the soul, each "
        "with known walls and known weak points. The waiting room falls "
        "to the prepared mind carrying its own campaign - a book, a "
        "problem, a plan. The dull meeting falls to the attendee who "
        "sets himself a private worthy objective inside the required "
        "hour. The repetitive task falls to the craftsman who races his "
        "own record. The Signature defender does not merely endure sieges; "
        "he studies their engineering, and finding every siege built from "
        "the same four timbers - low challenge, low meaning, long "
        "duration, no choice - he learns to knock out one timber before "
        "the walls close.")),
dict(
    key="boredom_personal_triggers", name="Personal Triggers: Memories, Anniversaries, and Private Associations",
    group="Compounded", ladder_rank=19, ladder_tier="compounded",
    description=(
        "Beyond the universal triggers, everyone carries a private set - "
        "situations that bore them specifically because of their history. "
        "The hobby gone stale: the instrument, sport, or craft that once "
        "absorbed you completely and now feels like going through motions "
        "- the challenge that used to fit has been outgrown, and the "
        "activity triggers boredom precisely because you remember when it "
        "did not. The place with a past: the town you grew up in, the "
        "routine visit to family, where every street is over-familiar and "
        "novelty died years ago. The anniversary effect: the same week "
        "every year when life feels flat - not from any event, but from "
        "the accumulated association of flatness with the season. The "
        "person-specific trigger: the acquaintance whose stories you have "
        "heard eleven times, the colleague whose meetings always drain - "
        "boredom conditioned to a face. The post-achievement hollow: the "
        "week after the big project ships, the goal reached, and suddenly "
        "nothing on the calendar matters - the meaning channel emptied all "
        "at once. Personal triggers are stickier than classic ones because "
        "they carry memory: the boredom arrives pre-loaded with the "
        "knowledge that this used to be better, which adds a sting of loss "
        "to the flatness. Mapping your private set is advanced "
        "self-knowledge - it turns 'I am just bored lately' into 'my "
        "challenge channel emptied after the project, and these three "
        "situations are where it shows.'"),
    how_it_works=(
        "Personal triggers form by association and by outgrowing. The "
        "association path is conditioning: a situation repeatedly paired "
        "with unengaged attention becomes a cue that pre-loads the state - "
        "the brain, efficient as ever, starts the boredom before the "
        "situation even proves dull. The outgrowing path is structural: "
        "skills rise with practice while the activity's challenge stays "
        "fixed, so the fit that once produced flow decays into the "
        "boredom quadrant - this is the hobby gone stale, and it is "
        "actually a compliment to the learner's growth. The anniversary "
        "effect runs on seasonal and contextual cues that re-evoke last "
        "year's state. The post-achievement hollow is a meaning deficit "
        "with a clear cause: the goal that organized months of attention "
        "is gone, and no successor has been appointed. Because personal "
        "triggers are specific, their remedies can be surgical: raise the "
        "challenge to meet the grown skill, appoint a successor goal "
        "before the old one ends, break the conditioned cue with deliberate "
        "novelty. The general rule: personal boredom is information about "
        "your history with a situation, and histories can be rewritten."),
    key_points=[
        "Private triggers: the stale hobby, the over-familiar place, the flat anniversary, the draining acquaintance, the post-achievement hollow.",
        "They sting more because they carry the memory of when it was better.",
        "Formed by conditioning (cue pre-loads the state) or outgrowing (skill rose past the challenge).",
        "The stale hobby is a compliment to your growth, not a failure.",
        "Remedies are surgical: raise the challenge, appoint a successor goal, break the cue.",
    ],
    requirements=[
        "Five personal trigger types with examples",
        "Conditioning vs outgrowing mechanisms",
        "Surgical remedies for each type",
    ],
    standards=["Flow theory skill-challenge dynamics; associative learning accounts"],
    citations=[CIT_CSIKSZENTMIHALYI, CIT_DANCKERT],
    sig_lens=(
        "His Signature lens reads personal triggers as old maps: charts "
        "of waters you have already sailed, now too familiar to thrill. "
        "The stale hobby is a sea you have mastered - the Signature "
        "sailor does not mourn the mastered sea; he seeks deeper waters "
        "or teaches others to sail it. The post-achievement hollow is the "
        "quiet after the campaign - the Signature commander appoints the "
        "next campaign before the banners of the last are folded, because "
        "an army without orders drills itself into dullness. Old maps are "
        "not curses; they are proof of how far you have come. Honor them, "
        "file them, and set sail for uncharted water.")),
dict(
    key="boredom_surprise_triggers", name="Surprise Triggers: The Odd Things That Set Boredom Off",
    group="Compounded", ladder_rank=20, ladder_tier="compounded",
    description=(
        "Some triggers surprise people because they look like the opposite "
        "of boring. Too much choice: the streaming menu with ten thousand "
        "titles, the restaurant with forty pages - abundance paralyzes the "
        "choosing mind, and the paralysis reads as flatness; people report "
        "feeling bored while surrounded by options. Success without "
        "struggle: the goal achieved too easily, the game with no worthy "
        "opponent - the win lands hollow because the challenge channel "
        "was never fed. Constant novelty: the endless feed, the channel "
        "surfing - each new thing arrives before attention can settle, so "
        "nothing engages, and the blur of stimulation produces the very "
        "flatness it was meant to cure. Being over-helped: the task done "
        "for you, the problem solved before you could wrestle it - agency "
        "removed, engagement impossible. The too-comfortable: the resort "
        "with nothing to do, the perfect Sunday with no plans - comfort "
        "without purpose curdles within hours. Social abundance without "
        "depth: the party full of small talk, the gathering where no real "
        "conversation happens - surrounded by people and starved of "
        "connection. Each surprise trigger teaches the same lesson from a "
        "new angle: boredom is not about the amount of input but the fit "
        "of it - challenge matched to skill, meaning matched to values, "
        "novelty paced for attention to land."),
    how_it_works=(
        "The surprise triggers all break the naive model that boredom "
        "equals understimulation. Too much choice overloads the decision "
        "system; with choosing exhausted, engagement never starts, and "
        "the flatness that follows is decision fatigue wearing boredom's "
        "mask. Easy success starves the challenge channel while feeding "
        "the reward channel - the mismatch proves that satisfaction needs "
        "the struggle, not just the prize. Constant novelty defeats the "
        "attention system it aims to please: engagement needs dwell time, "
        "and the feed never grants it, so arousal spikes and attention "
        "starves simultaneously. Being over-helped removes agency, and "
        "agency is engagement's prerequisite - you cannot be absorbed in "
        "what you did not choose or shape. Comfort without purpose shows "
        "that the meaning channel is independent: all needs met, nothing "
        "mattering, the soul still restless. Social abundance without "
        "depth starves the connection channel specifically. Together they "
        "refine the model: boredom is fit-failure across four channels - "
        "challenge, meaning, agency, connection - and any channel can "
        "fail even when the others are flooded."),
    key_points=[
        "Six surprise triggers: too much choice, easy success, constant novelty, being over-helped, pure comfort, shallow social abundance.",
        "Each looks stimulating but starves one of the four channels: challenge, meaning, agency, connection.",
        "The endless feed defeats attention by never granting dwell time.",
        "Satisfaction needs the struggle, not just the prize.",
        "Boredom is fit-failure, not input-failure.",
    ],
    requirements=[
        "Six surprise triggers with mechanisms",
        "The four-channel model: challenge, meaning, agency, connection",
        "Why the naive understimulation model fails",
    ],
    standards=["Choice-overload literature; flow theory; meaning-maintenance accounts"],
    citations=[CIT_VANTILBURG, CIT_CSIKSZENTMIHALYI],
    sig_lens=(
        "His Signature lens calls these the gilded traps: cages built of "
        "gold that still cage. The endless menu, the effortless win, the "
        "perfect idle Sunday - each gleams, each starves. The Signature "
        "eye is trained to see through gilding to the four channels "
        "beneath: does this feed my challenge, my meaning, my agency, my "
        "connection? If not, it is a trap no matter how it shines, and "
        "the wise soul walks past gold to find work. The deepest Signature "
        "lesson of the surprise triggers: abundance is not nourishment. "
        "A feast of sawdust still starves; the soul needs its proper food, "
        "and it knows the difference even when the eyes are dazzled.")),
dict(
    key="boredom_chain_reactions", name="Chain Reactions: How One Boredom Trigger Cascades",
    group="Compounded", ladder_rank=21, ladder_tier="compounded",
    description=(
        "Boredom rarely stays where it starts; it cascades. The classic "
        "chain begins with a single trigger - the dull afternoon - which "
        "produces the urge for change. The urge reaches for the cheapest "
        "novelty, the phone. The phone delivers stimulation without "
        "engagement, which deepens the flatness. The deepened flatness "
        "raises irritability, so a harmless remark from a housemate "
        "sparks a snap. The snap produces guilt, and guilt - low, heavy, "
        "self-attacking - makes genuine engagement even harder to start. "
        "Now the evening is ruined, and the ruined evening becomes "
        "tomorrow's dread, which pre-loads the next day's boredom before "
        "it begins. Each link is small and each feels inevitable in the "
        "moment, but the chain is not fate - it is a sequence of "
        "choice-points, and breaking any single link stops the cascade. "
        "Other chains branch differently: boredom to risk-taking (the "
        "drive too fast, the bet too big, because the alarm will pay any "
        "price for stimulation), boredom to overeating (the mouth recruited "
        "as novelty-seeker), boredom to picking fights (conflict as cheap "
        "engagement), boredom to doomscrolling paralysis (the search for "
        "something happening that never arrives). Mapping your own chains "
        "is the advanced skill: know your first link, and you can cut the "
        "fuse before the powder catches."),
    how_it_works=(
        "Chains propagate because each stage degrades the resources needed "
        "to stop the next. Cheap novelty (the phone) fails to engage "
        "attention but spends the willingness to try - each failed attempt "
        "raises the threshold for what counts as satisfying, so the next "
        "attempt must be stronger. Irritability rises as the engagement "
        "gap persists, lowering the fuse for conflict; conflict then "
        "consumes the emotional resources that engagement would need. "
        "Guilt and self-attack further drain the initiative required to "
        "start something worthwhile - the cruel loop from the energy "
        "record, now extended across the evening. The risk-taking branch "
        "runs on a different logic: the alarm at full volume overrides "
        "the caution system, discounting future costs against present "
        "flatness. The doomscrolling branch is a search loop with no exit "
        "condition - the brain keeps checking because the cost of one more "
        "check feels tiny, while the cumulative cost is enormous. Every "
        "chain has the same weak point: the first link, where resources "
        "are still intact and the choice is still cheap. Interventions "
        "therefore aim upstream - at the urge for change itself, answered "
        "with genuine engagement before the cheap novelty gets its vote."),
    key_points=[
        "The classic chain: trigger to urge to cheap novelty to irritability to conflict to guilt to dread.",
        "Each link degrades the resources needed to stop the next.",
        "Branch chains: risk-taking, overeating, picking fights, doomscrolling paralysis.",
        "Every chain's weak point is the first link, where choice is still cheap.",
        "Map your own chains; cut the fuse before the powder catches.",
    ],
    requirements=[
        "Full classic chain narrated link by link",
        "Four branch chains with their logic",
        "Upstream intervention principle",
    ],
    standards=["Risk-sensitivity under boredom (Bench and Lench); self-regulation depletion accounts"],
    citations=[CIT_BENCH, CIT_DANCKERT],
    sig_lens=(
        "His Signature lens sees chains as enemy supply lines: each link "
        "feeding the next, each vulnerable at exactly one point - the "
        "first. The Signature strategist does not fight the whole line; "
        "he cuts it at the source, answering the urge for change with "
        "genuine engagement before cheap novelty casts its vote. The "
        "branches - risk, quarrel, gorge, scroll - are the enemy's "
        "flanking maneuvers, each aiming to spend your resources before "
        "the real battle. Know your first link the way a general knows "
        "his terrain, post your guard there, and no cascade ever reaches "
        "your walls. The chain is not fate; it is logistics, and "
        "logistics can be cut.")),
]
# ---------------------------------------------------------------- 22-25: behavior
ENTRIES += [
dict(
    key="boredom_behavior_actions", name="What People Do When They Are Bored",
    group="Advanced", ladder_rank=22, ladder_tier="advanced",
    description=(
        "Bored behavior is the urge for change made visible. The small "
        "repertoire comes first: fidgeting, sighing, clock-watching, "
        "phone-checking, the aimless lap to the window and back. Then the "
        "seeking repertoire: scrolling for something interesting, "
        "channel-surfing, opening the fridge without hunger, starting "
        "small tasks and abandoning them - each an attempt to manufacture "
        "novelty. Then the social repertoire: texting people out of the "
        "blue, prolonging conversations past their natural end, dropping "
        "by unannounced, stirring mild drama - other people are the "
        "richest available stimulation. Then the escape repertoire: "
        "sudden walks, impulse errands, the drive with no destination. "
        "And at the far end, the risky repertoire: fast driving, "
        "reckless bets, picking fights, the drink too many - the alarm at "
        "full volume paying any price for stimulation. What unites all "
        "five repertoires is that they are search behaviors: the organism "
        "casting about for something to engage with. Judged morally they "
        "look scattered or self-destructive; read functionally they are "
        "all the same sentence - 'give me something worth my attention' - "
        "spoken in different dialects. The practical art is translation: "
        "hear the sentence under the behavior, and answer the sentence "
        "instead of punishing the dialect."),
    how_it_works=(
        "The five repertoires escalate along two axes: cost and "
        "desperation. Small behaviors cost nothing and signal low "
        "desperation; the system is still hoping the situation will "
        "improve on its own. Seeking behaviors cost a little time and "
        "signal the system taking matters into its own hands - still "
        "within safe bounds. Social behaviors recruit other nervous "
        "systems as stimulation sources, which works but taxes "
        "relationships. Escape behaviors break the situation's frame "
        "entirely - leaving the room, the road, the plan. Risky behaviors "
        "appear when the alarm overrides caution: the brain discounts "
        "future costs steeply against present flatness, which is the "
        "standard mechanism of boredom-driven risk-taking. The escalation "
        "is orderly, not random, which makes it predictable: if the small "
        "repertoire is active and unanswered, expect the seeking "
        "repertoire next. This predictability is the intervention map - "
        "answer at the small stage with genuine engagement and the later "
        "stages never arrive. Wait until the risky stage and you are no "
        "longer managing boredom but managing consequences."),
    key_points=[
        "Five repertoires: small, seeking, social, escape, and risky - all are search behaviors.",
        "They escalate along cost and desperation in a predictable order.",
        "Every behavior speaks one sentence: give me something worth my attention.",
        "Answer the sentence, not the dialect - translate before judging.",
        "Intervene at the small stage; the risky stage is consequences, not boredom.",
    ],
    requirements=[
        "Five repertoires with examples",
        "Escalation axes and predictability",
        "Translation as the practical art",
    ],
    standards=["Boredom-driven risk-taking literature; functional behavior analysis"],
    citations=[CIT_BENCH, CIT_DANCKERT],
    sig_lens=(
        "His Signature lens reads the five repertoires as a scout's "
        "escalating signals: the pebble tossed, the shout, the beacon "
        "fire, the rider dispatched, the fortress torched. Each is louder "
        "than the last, each saying the same thing - the territory ahead "
        "is empty, send orders. The Signature commander answers the "
        "pebble so he never has to answer the torch: genuine engagement "
        "at the small stage, worthy work before the seeking begins. And "
        "he trains his scouts - his own habits - to report early and "
        "clearly, because a signal honored at whisper-volume never needs "
        "to become a scream. The behaviors are not the enemy; they are "
        "dispatches. Read them.")),
dict(
    key="boredom_speech_patterns", name="What Bored People Say: Phrases, Tone, and Speech Patterns",
    group="Advanced", ladder_rank=23, ladder_tier="advanced",
    description=(
        "Boredom has a recognizable voice. The phrases are its flag: 'I "
        "am so bored,' 'there is nothing to do,' 'this is taking forever,' "
        "'are we done yet,' 'whatever,' 'I guess.' Note the grammar of "
        "disengagement - passive constructions, the situation as the "
        "actor ('this is dragging'), the self as the sufferer. The tone "
        "is flat and slow: pitch range narrows, speech slows, energy "
        "drains out of the vowels - the voice of a system running on "
        "idle. Then there is the sigh punctuating sentences, the yawn "
        "mid-word, the trailing off - thoughts abandoned before "
        "completion because attention could not sustain them. Questions "
        "change character: genuine curiosity asks to learn, boredom asks "
        "to be rescued - 'so what else is going on,' 'got anything fun "
        "happening,' the interrogation of the room for entertainment. "
        "Complaints multiply and shrink at once: everything is wrong, "
        "nothing is specifically wrong - the grievance is with the "
        "moment itself. And there is the performative boredom of the "
        "young, announced loudly as identity: boredom declared as a "
        "verdict on the world rather than a report from within. Hearing "
        "these patterns accurately matters: the phrases are not always "
        "requests for entertainment - often they are untranslated reports "
        "of unengaged attention, and answering the translation ('your mind "
        "needs something worthy') works better than answering the literal "
        "words ('here is something shiny')."),
    how_it_works=(
        "Speech patterns follow the underlying state through three "
        "channels. Prosody - the flat tone, slow pace, narrow pitch - is "
        "the arousal system speaking directly; low engaged arousal flattens "
        "the voice the way it flattens everything else. Content - the "
        "complaints, the 'nothings,' the rescue-questions - is the "
        "appraisal system reporting the mismatch: wanted engagement high, "
        "offered low, verdict rendered. Discourse behavior - trailing off, "
        "abandoned thoughts, the late mm-hmm - is attention failing to "
        "sustain the thread. The performative variant adds a social layer: "
        "announcing boredom as identity recruits the audience as either "
        "entertainers or fellow sufferers. For the listener, the skill is "
        "hearing through all three channels to the single underlying "
        "report - attention unengaged - and responding to that rather "
        "than to any single utterance. Correct the prosody with energy "
        "alone and you get louder flatness; supply shiny distractions "
        "and you feed the scroll-loop; but offer genuine engagement - a "
        "real question, a worthy task, an honest conversation - and the "
        "voice reanimates from the inside out."),
    key_points=[
        "Flag phrases: the grammar of disengagement - passive, the situation as actor, the self as sufferer.",
        "Tone goes flat and slow: the voice of a system on idle.",
        "Bored questions ask to be rescued; curious questions ask to learn.",
        "Trailing off and late responses show attention failing to sustain the thread.",
        "Answer the translation (unengaged attention needs worthy work), not the literal words.",
    ],
    requirements=[
        "Phrases, tone, and discourse patterns each described",
        "Three channels: prosody, content, discourse behavior",
        "Listening skill framed for the hearer",
    ],
    standards=["Affective prosody literature; discourse analysis of disengagement"],
    citations=[CIT_DANCKERT, CIT_EASTWOOD],
    sig_lens=(
        "His Signature lens hears bored speech as dispatches from the "
        "waiting garrison: flat, slow, trailing - the voice of troops "
        "with no orders. The Signature listener does not mock the "
        "dispatch nor merely obey its literal request; he reads the "
        "report beneath - attention unengaged, capacities idle - and "
        "answers with a campaign, not a parade. A real question, a "
        "worthy task, an honest conversation: these are orders, and "
        "orders reanimate the voice from within. And the Signature "
        "speaker watches his own dispatches: when his phrases go passive "
        "and his tone goes flat, he hears his own garrison reporting - "
        "and issues himself new orders before the flatness becomes the "
        "man.")),
dict(
    key="boredom_decisions_judgment", name="How Boredom Changes Decisions and Judgment",
    group="Advanced", ladder_rank=24, ladder_tier="advanced",
    description=(
        "Boredom is a quiet saboteur of good judgment. Its first effect is "
        "on time horizons: the bored mind discounts the future steeply - "
        "later consequences feel unreal against the vivid pain of present "
        "flatness - so choices tilt toward immediate stimulation regardless "
        "of cost. Its second effect is on risk: with the alarm at full "
        "volume, the brain prices stimulation higher and danger lower; "
        "this is the mechanism behind boredom-driven speeding, gambling, "
        "and reckless social choices. Its third effect is on standards: "
        "the threshold for 'worth doing' drops as desperation rises, so "
        "the bored person says yes to things the engaged person would "
        "refuse - the dull invitation, the sketchy plan, the third hour "
        "of scrolling. Its fourth effect is on patience: deliberation "
        "feels unbearable when time is already dragging, so decisions get "
        "rushed - not from confidence but from the need for something, "
        "anything, to happen. Its fifth effect is on meaning-weighting: "
        "options are judged by their stimulation value rather than their "
        "alignment with values, so the exciting wrong choice beats the "
        "quiet right one. The defense is procedural, not heroic: never "
        "make the big decision inside the peak. Write the rule before the "
        "flatness arrives - the speed limit, the budget, the 'I do not "
        "decide this while bored' list - and let the calm self govern the "
        "bored self by prior arrangement."),
    how_it_works=(
        "Each distortion follows from the core mismatch plus the urge for "
        "change. Steep future-discounting happens because the present "
        "state is intensely aversive - the brain will pay almost any "
        "future price to end present suffering, the same logic as pain. "
        "Risk inflation happens because the alarm overrides the caution "
        "system: stimulation becomes the dominant goal, and goals "
        "reorganize perception around themselves. Dropping standards is "
        "threshold dynamics - the same mechanism as the climbing phase, "
        "where each failed search lowers the bar for what counts. Rushed "
        "deliberation is time-perception distortion weaponized: when "
        "minutes feel like hours, 'sleeping on it' feels like a sentence. "
        "Meaning de-weighting is attention's doing - with the meaning "
        "channel starved, the brain stops consulting it, judging options "
        "purely as stimulation sources. The procedural defense works "
        "because it moves the decision to a different state: pre-commitment "
        "rules, cooling-off delays, and accountability partners all "
        "function as the engaged self governing the bored self by prior "
        "arrangement. This is not weakness - it is engineering, building "
        "the guardrails before the fog rolls in."),
    key_points=[
        "Boredom steepens future-discounting: present flatness outweighs future cost.",
        "Risk gets underpriced; stimulation becomes the dominant goal.",
        "Standards drop as desperation rises; patience evaporates as time drags.",
        "Options get judged by stimulation value instead of alignment with values.",
        "The defense is procedural: decide by prior arrangement, never inside the peak.",
    ],
    requirements=[
        "Five judgment distortions with mechanisms",
        "Why each follows from the core mismatch",
        "Procedural defenses, not heroic ones",
    ],
    standards=["Intertemporal choice under aversive states; risk-sensitivity literature"],
    citations=[CIT_BENCH, CIT_VANTILBURG],
    sig_lens=(
        "His Signature lens treats bored judgment as a council meeting "
        "held during a siege: the members are brave but the walls are "
        "shaking, and every vote tilts toward whatever ends the shaking "
        "fastest. The Signature ruler does not hold council during the "
        "siege - he issued his standing orders in peacetime: the speed "
        "limit, the budget, the list of decisions never made under "
        "flatness. This is not distrust of the self; it is the highest "
        "trust - the calm commander protecting his besieged garrison from "
        "its own desperation. Let the peacetime self govern the wartime "
        "self by prior arrangement, and the siege passes without a "
        "surrender.")),
dict(
    key="boredom_escalation", name="Escalation: How Boredom Behaviors Intensify",
    group="Advanced", ladder_rank=25, ladder_tier="advanced",
    description=(
        "Left unanswered, boredom escalates through a predictable ladder "
        "of its own. Stage one is private and small: the sigh, the fidget, "
        "the glance at the clock - signals visible only to the self. Stage "
        "two goes seeking: the phone, the fridge, the aimless browse - "
        "still harmless, still reversible. Stage three goes social: the "
        "provocative text, the prolonged complaint, the stirring of mild "
        "drama - other people recruited as stimulation, relationships "
        "starting to pay the price. Stage four goes structural: the "
        "abandoned project, the skipped class, the job done at the "
        "minimum - disengagement spreading from the moment to the life. "
        "Stage five goes risky: the speeding, the gambling, the substance, "
        "the fight - the alarm overriding caution entirely. Each stage "
        "feels like a reasonable response to the last - 'well, that did "
        "not work, so try this' - which is why escalation is so hard to "
        "see from inside. The exits narrow as the stages climb: stage one "
        "needs only a small redirect, stage three needs relationship "
        "repair alongside re-engagement, stage five needs intervention "
        "beyond self-help. The master skill is stage recognition: name "
        "where you are on the ladder, and you know both how urgent the "
        "answer is and how strong it must be. Catch it at stage one a "
        "thousand times and you will never meet stage five."),
    how_it_works=(
        "Escalation runs on the threshold mechanism compounded by "
        "habituation. Each unanswered stage raises the bar for what "
        "counts as satisfying - the phone that worked at stage two fails "
        "at stage three, so the system reaches for stronger medicine. "
        "Simultimeously, each stage spends a different resource: stage two "
        "spends time, stage three spends social capital, stage four spends "
        "life structure, stage five spends safety. The spending is what "
        "makes later stages harder to reverse - you cannot un-send the "
        "provocative text or un-take the risk, and the consequences become "
        "new sources of flatness and dread that feed the next cycle. The "
        "'reasonable response' illusion comes from local logic: at each "
        "step, the next stage genuinely looks like the smallest thing "
        "that might work, because the system evaluates options against "
        "the current threshold, not the original one. Breaking escalation "
        "therefore requires either early interception (answer stage one "
        "with genuine engagement) or threshold reset (a period of "
        "deliberate low stimulation that lets the bar fall back down - "
        "the logic behind digital fasts and quiet retreats)."),
    key_points=[
        "Five stages: private signals, seeking, social recruitment, structural disengagement, risk.",
        "Each stage raises the threshold, so the next stage looks like the smallest thing that might work.",
        "Each stage spends a different resource: time, social capital, life structure, safety.",
        "Later stages are harder to reverse because consequences become new triggers.",
        "Master skill: stage recognition - name where you are to know the urgency and strength of answer needed.",
    ],
    requirements=[
        "Five escalation stages with examples",
        "Threshold and resource-spending mechanisms",
        "Early interception vs threshold reset",
    ],
    standards=["Escalation dynamics; habituation and threshold models"],
    citations=[CIT_BENCH, CIT_DANCKERT],
    sig_lens=(
        "His Signature lens maps escalation as five rings of a fortress "
        "undermined from within: the outer whisper, the seeking sally, "
        "the social breach, the structural crumbling, the final torch. "
        "The Signature defender's doctrine is absolute: never let the "
        "enemy past the first ring. Answer the whisper with worthy work, "
        "and the deeper rings never fall. But the doctrine has a second "
        "clause for the honest commander who finds the breach already "
        "deep: do not waste strength shoring the outer wall while the "
        "inner burns - reset the threshold, repair what the stages spent, "
        "and rebuild outward. Fortresses are retaken the same way they "
        "are held: one ring at a time, starting from where you stand.")),
# ---------------------------------------------------------------- 26-28: healthy expression
dict(
    key="boredom_healthy_expression", name="Expressing Boredom Well: Saying It, Showing It, Channeling It",
    group="Advanced", ladder_rank=26, ladder_tier="advanced",
    description=(
        "Boredom expressed well becomes useful information instead of "
        "corrosive complaint. Saying it well means translating the raw "
        "feeling into its true report: not 'this is boring' (a verdict on "
        "the world) but 'my mind needs something more engaging right now' "
        "(a report from within) - or, to another person, 'I am having "
        "trouble staying engaged; can we find the interesting thread here?' "
        "The honest sentence recruits help; the verdict recruits "
        "defensiveness. Showing it well means letting the signal show "
        "without weaponizing it: the honest sigh is information, the "
        "exaggerated eye-roll is an attack - same feeling, different "
        "ethics. Channeling it well is the master move: boredom is "
        "unclaimed capacity, and capacity can be claimed. The bored "
        "meeting becomes the meeting where you take the notes that "
        "actually get used; the dull wait becomes the wait where the "
        "plan gets written; the flat afternoon becomes the afternoon the "
        "drawer gets organized, the letter gets written, the skill gets "
        "practiced. Channeling does not mean grim productivity - play "
        "counts, curiosity counts, the walk that clears the head counts. "
        "It means giving the unengaged attention somewhere worthy to go, "
        "so the signal that said 'nothing here' becomes the action that "
        "says 'I brought something here.'"),
    how_it_works=(
        "Healthy expression works by keeping the signal's information "
        "while changing its vehicle. The raw feeling carries true data - "
        "attention unengaged, capacity idle - wrapped in a crude vehicle: "
        "complaint, sigh, fidget. Translation preserves the data and "
        "upgrades the vehicle: 'I need engagement' instead of 'this is "
        "boring' delivers the same information in a form others can act "
        "on. Non-weaponized showing preserves honesty while respecting "
        "the social contract: the signal is shared as data, not deployed "
        "as punishment. Channeling is the deepest mechanism - it does not "
        "merely express the state, it resolves it: by assigning the idle "
        "capacity to worthy work, the engagement gap closes, attention "
        "locks on, and the feeling that needed expressing evaporates "
        "because its cause is gone. This is why channeling outperforms "
        "venting in the long run: venting discharges the feeling's "
        "pressure while leaving its cause intact, but channeling removes "
        "the cause. The three moves form a progression - say it true, "
        "show it clean, channel it well - and each is available at "
        "different moments: saying for when others are involved, showing "
        "for when honesty is owed, channeling always."),
    key_points=[
        "Say it as a report from within ('my mind needs engagement'), not a verdict on the world.",
        "Show it honestly without weaponizing it: the sigh informs, the eye-roll attacks.",
        "Channel it: assign the idle capacity to worthy work and the cause dissolves.",
        "Channeling outperforms venting because it removes the cause, not just the pressure.",
        "Play and curiosity count as channeling - worthy includes joyful.",
    ],
    requirements=[
        "Saying, showing, and channeling each with examples",
        "Translation technique: data preserved, vehicle upgraded",
        "Why channeling beats venting",
    ],
    standards=["Emotion regulation: reappraisal and situation modification (Gross)"],
    citations=[CIT_ELPIDOROU, CIT_BENCH],
    sig_lens=(
        "His Signature lens elevates expression into statecraft. The "
        "translated sentence is diplomacy: the true report delivered in "
        "words that build bridges instead of burning them. The clean "
        "showing is honest heraldry: the banner flown straight, never "
        "dipped as a weapon. The channeling is the master stroke of "
        "generalship: idle troops given a campaign, the waiting garrison "
        "marched out to build roads, plant fields, raise walls. In this "
        "lens, boredom well-expressed is never waste - it is the "
        "recruiting sergeant of the soul, turning every idle hour into "
        "enlistment for worthy work. The feeling that said 'nothing here' "
        "becomes, by Signature alchemy, the deed that says 'I brought "
        "something here.'")),
dict(
    key="boredom_unhealthy_expression", name="Bottling It Up or Exploding: What Each Costs",
    group="Advanced", ladder_rank=27, ladder_tier="advanced",
    description=(
        "Boredom handled badly takes two familiar shapes, and both charge "
        "interest. Bottling it up looks like virtue: the jaw set, the "
        "mask held, the dull hours endured in silence. But suppressed "
        "boredom does not dissipate - it ferments. The engagement gap "
        "stays open, the urge for change keeps pressing, and the pressure "
        "leaks sideways: into irritability at small things, into the "
        "evening scroll that goes too long, into a flatness that spreads "
        "from the boring hours into the good ones. The bottler pays in "
        "spreading numbness - life narrows as more and more situations "
        "get filed under 'endure.' Exploding looks like honesty: the "
        "snapped remark, the slammed door, the dramatic 'I cannot take "
        "this anymore.' The explosion does discharge pressure - briefly. "
        "But it spends social capital to buy a moment's relief, and the "
        "relief fades while the costs remain: the apologizing, the "
        "walking on eggshells afterward, the reputation as volatile. "
        "Worse, explosions teach the brain that intensity is the only "
        "volume that gets answered, training future boredom to skip "
        "straight to the scream. Both shapes share one error: they treat "
        "the feeling as the problem to be managed rather than the signal "
        "to be answered. The bottler manages the signal into silence; "
        "the exploder manages it into noise. The signal itself - "
        "unclaimed capacity calling for worthy work - goes unanswered "
        "either way, which is why both shapes end in the same place: "
        "deeper boredom, wearing a new disguise."),
    how_it_works=(
        "Bottling fails through the suppression paradox: holding the mask "
        "consumes the very control resources that could have been spent "
        "on re-engagement, while the unaddressed gap keeps generating the "
        "signal - effort up, cause untouched, net loss. The sideways leaks "
        "are the pressure finding cheaper exits: irritability, "
        "compulsive scrolling, spreading flatness. Over time, chronic "
        "bottling trains avoidance - situations get pre-labeled as "
        "'endure,' the repertoire of engagement shrinks, and the "
        "person's world contracts. Exploding fails through cost "
        "asymmetry: the relief is immediate and the costs are delayed, "
        "so the brain learns the wrong lesson - that escalation works. "
        "Each explosion also raises the threshold: next time, a smaller "
        "explosion will not feel like enough. Socially, explosions tax "
        "the relationships that could have supplied engagement, "
        "shrinking the very resources recovery needs. Both shapes are "
        "feedback loops with the same structure: the response addresses "
        "the feeling's expression while ignoring its information. The "
        "exit from either loop is the same - stop managing the signal "
        "and start answering it: translate it, show it cleanly, channel "
        "the capacity it reports into worthy work."),
    key_points=[
        "Bottling ferments: suppressed boredom leaks sideways into irritability, compulsive scrolling, spreading flatness.",
        "Bottling trains avoidance; the engaged world contracts.",
        "Exploding buys brief relief at the price of social capital and future calm.",
        "Explosions teach the brain that only screams get answered - the threshold ratchets up.",
        "Both shapes manage the signal instead of answering it; both end in deeper boredom.",
    ],
    requirements=[
        "Bottling and exploding each with their cost ledgers",
        "The feedback-loop structure both share",
        "The common exit: answer the signal",
    ],
    standards=["Suppression costs (Gross); escalation and threshold dynamics"],
    citations=[CIT_BENCH, CIT_DANCKERT],
    sig_lens=(
        "His Signature lens condemns both shapes as failed generalship. "
        "The bottler is the commander who receives the scout's dispatch "
        "and burns it unread - the garrison still waits, the orders still "
        "never come, and the unread dispatches pile up until the "
        "headquarters catch fire. The exploder is the commander who "
        "answers the dispatch by shelling his own town - pressure "
        "released, everything else destroyed. The Signature commander "
        "does neither: he reads the dispatch, honors the scout, and "
        "issues the campaign. The feeling is never the enemy; it is the "
        "messenger. Shoot the messenger and you rule blind; burn the "
        "dispatch and you rule deaf. Read it, and you rule.")),
dict(
    key="boredom_everyday_practices", name="Everyday Practices That Keep Boredom in Balance",
    group="Advanced", ladder_rank=28, ladder_tier="advanced",
    description=(
        "Balance with boredom is built from small, repeatable practices, "
        "not heroic interventions. The engagement audit: once a day, ask "
        "where your attention actually went and whether it was fed - the "
        "five-minute review that catches flat stretches before they "
        "compound. The challenge dial: deliberately tune one routine task "
        "a notch harder - the race against your own record, the tighter "
        "constraint, the new technique - keeping skill and challenge in "
        "speaking terms. The meaning thread: tie one daily task to a "
        "value you hold, even artificially at first; the thread thickens "
        "with use. The novelty ration: one small new thing per day - a "
        "different route, an unfamiliar food, a question you have never "
        "asked - feeding curiosity its daily bread. The stillness "
        "practice: brief, deliberate periods of low stimulation - the "
        "walk without the phone, the waiting without the scroll - that "
        "retrain the threshold downward so ordinary moments satisfy "
        "again. The transition ritual: a small ceremony between "
        "activities - the desk cleared, the breath taken - that helps "
        "attention land instead of skimming across the gap. The worthy "
        "list: three things that would make the day feel well-spent, "
        "chosen each morning, so the engagement gap gets measured "
        "against something real. None of these is dramatic; together "
        "they are a maintenance system for the attention-meaning "
        "machinery, the way brushing teeth maintains the mouth. Boredom "
        "visits everyone; the practiced simply host it better - shorter "
        "stays, cleaner exits, useful information extracted from every "
        "visit."),
    how_it_works=(
        "Each practice targets one component of the boredom machinery. "
        "The audit targets awareness: you cannot answer a signal you do "
        "not notice, and the daily review builds the noticing muscle. "
        "The challenge dial targets the skill-challenge fit directly, "
        "manufacturing flow-quadrant conditions inside fixed routines. "
        "The meaning thread targets the meaning channel, which is the "
        "hardest to feed on demand - artificial tying works because "
        "meaning is partly constructed, and constructed meaning still "
        "engages. The novelty ration targets curiosity's baseline "
        "appetite with small, sustainable portions - feast-or-famine "
        "novelty trains the threshold upward. The stillness practice is "
        "threshold reset in miniature: deliberate low-stimulation periods "
        "let the bar for 'satisfying' fall back down. The transition "
        "ritual targets the onset phase, where redirection is cheapest - "
        "a marked boundary helps attention disengage from the old and "
        "commit to the new. The worthy list targets the gap measurement "
        "itself: with the day's meaning defined in advance, flat "
        "stretches get noticed early and filled deliberately. Small and "
        "daily beats large and occasional because the machinery drifts "
        "daily - maintenance must match the drift rate."),
    key_points=[
        "Seven practices: audit, challenge dial, meaning thread, novelty ration, stillness, transition ritual, worthy list.",
        "Each targets one component: awareness, fit, meaning, curiosity, threshold, onset, measurement.",
        "Stillness practice resets the threshold downward so ordinary moments satisfy again.",
        "Small and daily beats large and occasional - maintenance must match the drift rate.",
        "The practiced host boredom better: shorter stays, cleaner exits, useful information.",
    ],
    requirements=[
        "Seven practices with their targets",
        "Why small-and-daily outperforms heroic-and-rare",
        "The maintenance-system framing",
    ],
    standards=["Behavioral maintenance models; attention-training literature"],
    citations=[CIT_CSIKSZENTMIHALYI, CIT_ELPIDOROU],
    sig_lens=(
        "His Signature lens frames the seven practices as the daily drill "
        "of the garrison: the audit as morning roll call, the challenge "
        "dial as weapons practice, the meaning thread as the colors "
        "ceremony, the novelty ration as the scout's patrol, stillness as "
        "the night watch, the transition ritual as the changing of the "
        "guard, the worthy list as the commander's orders for the day. "
        "No army stays ready without drill, and no soul stays engaged "
        "without practice. The Signature life is not the life without "
        "boredom - it is the life so well-drilled that boredom's visits "
        "are short, its reports are read, and its departures leave the "
        "garrison stronger than it found it. Drill daily, and the "
        "fortress holds.")),
# ---------------------------------------------------------------- 29-31: recognizing in others
dict(
    key="boredom_reading_others", name="Reading Boredom in Others: Face, Body, Voice, Behavior",
    group="Advanced", ladder_rank=29, ladder_tier="advanced",
    description=(
        "Reading boredom in another person means integrating four "
        "channels at once. The face: the unfocused stare, the heavy lids, "
        "the slack mouth - attention visibly elsewhere. The body: the "
        "melt into the chair, or the counter-pattern of still torso with "
        "busy extremities - the tapping foot that contradicts the polite "
        "nod. The voice: flattened tone, slowed pace, the sigh between "
        "sentences, answers that shrink to 'yeah' and 'mm-hmm.' The "
        "behavior: clock-checking, phone-checking, the question that "
        "asks to be rescued rather than informed. No single channel is "
        "decisive - the stare alone could be thoughtfulness, the sigh "
        "alone could be tiredness - but the configuration converges: "
        "when three channels report disengagement at once, the reading is "
        "solid. Context is the fifth channel: the same signals in a dull "
        "meeting mean something different than in a deep conversation - "
        "always ask what the situation offers before judging the person. "
        "And read generously: the bored face in your meeting is usually "
        "data about the meeting, not a verdict on you. The skilled reader "
        "uses the reading as an instrument panel, not a weapon - "
        "information about the room's engagement level, to be acted on "
        "with curiosity rather than offense."),
    how_it_works=(
        "Configural reading works because the channels are partially "
        "independent: the face leaks attention state, the body leaks "
        "arousal state, the voice leaks both, and behavior shows the "
        "urge for change in action. Independence is what makes "
        "convergence powerful - when four semi-independent instruments "
        "agree, the reading is robust in a way no single cue can be. "
        "The common errors are all single-channel: reading the stare "
        "without the context (thoughtfulness misread), reading the sigh "
        "without the body (tiredness misread), reading the phone-check "
        "without the history (rudeness misread). Base rates matter too: "
        "in a lecture hall at 3pm, boredom is the likely state and the "
        "bar for the reading should be low; in a crisis meeting, the "
        "same signals more likely mean shock or overload, and the bar "
        "should be high. The generous reading is not just kindness - it "
        "is accuracy: most boredom is situational, and the situational "
        "attribution is usually correct. Train the reading by narrating "
        "it silently - 'three channels, dull context, likely boredom' - "
        "until the integration becomes automatic."),
    key_points=[
        "Four channels: face, body, voice, behavior - plus context as the fifth.",
        "Convergence across channels is what makes the reading solid; no single cue decides.",
        "Common errors are all single-channel readings.",
        "Use base rates: the same signals mean different things in different situations.",
        "Read generously and instrumentally - data about the room, not a verdict on you.",
    ],
    requirements=[
        "Four channels plus context described",
        "Convergence principle and common errors",
        "Generous, instrumental reading framed",
    ],
    standards=["Configural emotion recognition; Brunswik lens model of cue integration"],
    citations=[CIT_EASTWOOD, CIT_DANCKERT],
    sig_lens=(
        "His Signature lens trains the reader as a scout reading distant "
        "signals: four banners on four hills, the fifth the lay of the "
        "land itself. The scout does not charge at the first banner - he "
        "waits for convergence, reads the terrain, and reports what he "
        "sees without embroidery. And the Signature scout reports "
        "generously: the dark windows are data about the night, not "
        "treason by the watchman. To read another's boredom well is a "
        "commander's skill - it tells you the state of your troops, "
        "your audience, your room - and the commander who reads it "
        "clearly can issue the orders that relight the lamps: a better "
        "question, a worthier task, a changed pace.")),
dict(
    key="boredom_supportive_responses", name="What to Say and Do When Someone Near You Is Bored",
    group="Advanced", ladder_rank=30, ladder_tier="advanced",
    description=(
        "When someone near you is bored, the unhelpful instincts are to "
        "entertain them, scold them, or take it personally. The helpful "
        "responses aim at the actual deficit. Offer genuine engagement, "
        "not shiny distraction: the real question beats the funny video - "
        "'what has been on your mind lately' outperforms any spectacle, "
        "because it feeds the meaning and connection channels. Offer "
        "agency: 'want to pick what we do next' or 'how would you tackle "
        "this' - choice restores the sense of control that boredom "
        "erodes. Offer challenge: the interesting problem, the friendly "
        "competition, the task with real stakes - matched to their skill, "
        "not beneath it. Change the frame: the walk-and-talk instead of "
        "the sit-and-talk, the working session instead of the status "
        "meeting - new containers let attention land fresh. Name it "
        "kindly: 'this part is pretty dry - want to find the interesting "
        "thread together' - the shared acknowledgment dissolves the "
        "shame that makes boredom lonelier. And respect the signal: "
        "sometimes the kindest response is to let the boring thing end - "
        "the meeting cut short, the visit concluded gracefully - rather "
        "than performing engagement nobody feels. What to avoid is the "
        "mirror trap: catching their flatness and going flat yourself, "
        "or the offense trap: reading their wandering attention as "
        "disrespect. Their boredom is data about the fit between them "
        "and the moment; your response can change the moment."),
    how_it_works=(
        "Supportive responses work by supplying the missing channel. "
        "Genuine questions feed meaning and connection; agency restores "
        "the control prerequisite for engagement; challenge feeds the "
        "skill-channel; reframing supplies novelty without the scroll's "
        "empty calories. Kind naming works through shame reduction: "
        "boredom carries a stigma of ingratitude ('how can you be bored "
        "when...'), and stigma drives masking, which blocks the honest "
        "collaboration that could fix the situation. Letting things end "
        "works through the duration dial - shortening the mismatch is "
        "sometimes the only honest move. The traps fail for symmetric "
        "reasons: entertaining with spectacle feeds the novelty channel "
        "while starving meaning, deepening the real deficit; scolding "
        "adds shame to flatness, producing masked boredom plus "
        "resentment; taking offense misattributes a situational signal "
        "to the relationship, manufacturing conflict from data. The "
        "underlying principle: treat their boredom the way you would "
        "want yours treated - as a legible signal about the moment, "
        "answerable by changing the moment, not by judging the person."),
    key_points=[
        "Offer genuine engagement over shiny distraction: the real question beats the funny video.",
        "Offer agency, challenge, and reframing - each feeds a starved channel.",
        "Name it kindly and share the acknowledgment; shame makes boredom lonelier.",
        "Sometimes the kindest response is to let the boring thing end.",
        "Avoid the mirror trap (going flat yourself) and the offense trap (reading it as disrespect).",
    ],
    requirements=[
        "Five helpful responses with their channel logic",
        "Kind naming and graceful endings included",
        "Traps explained: entertain, scold, take offense",
    ],
    standards=["Social support and co-regulation literature"],
    citations=[CIT_ELPIDOROU, CIT_BENCH],
    sig_lens=(
        "His Signature lens casts the supporter as the ally commander "
        "riding to a neighboring garrison: he does not mock their dark "
        "windows, nor bombard them with fireworks, nor take their "
        "flatness as insult to his own campaign. He brings what sieges "
        "actually need: a worthy objective (challenge), a voice in the "
        "planning (agency), a real conversation (meaning), a change of "
        "ground (reframing) - or, when the position is truly untenable, "
        "the honest order to withdraw with dignity. The Signature ally "
        "knows the deepest support is not rescue but reinforcement: not "
        "carrying the garrison's watch, but helping relight its lamps so "
        "it can stand its own walls again.")),
dict(
    key="boredom_mistakes_to_avoid", name="What NOT to Do: Mistakes That Make Boredom Worse",
    group="Advanced", ladder_rank=31, ladder_tier="advanced",
    description=(
        "The classic mistakes all share one shape: they answer the wrong "
        "deficit. Mistake one: the stimulation dump - louder music, "
        "faster content, more tabs open - feeding novelty while meaning "
        "starves, which deepens the real boredom underneath the noise. "
        "Mistake two: shaming it - 'you should be grateful,' 'other "
        "people would love this opportunity' - which adds guilt to "
        "flatness and drives the feeling underground, where it ferments. "
        "Mistake three: the endless scroll as remedy - the cheapest "
        "novelty that never grants dwell time, training the threshold "
        "upward with every session. Mistake four: forcing cheer - the "
        "gritted-teeth performance of enthusiasm, which exhausts the "
        "control budget and leaves the underlying gap untouched. Mistake "
        "five: outsourcing the cure - waiting for someone else to make "
        "it interesting, the entertainer never arriving, passivity "
        "deepening as agency atrophies. Mistake six: numbing it - the "
        "drink, the binge, the anything to not feel the flatness - which "
        "borrows against tomorrow's engagement to pay for tonight's "
        "oblivion. Mistake seven: treating it as identity - 'I am just a "
        "bored person' - which converts a situational signal into a life "
        "sentence and stops the search for better fit. Each mistake is "
        "understandable; each is a local logic that fails globally. The "
        "antidote to all seven is the same question, asked honestly: "
        "which channel is actually starving - challenge, meaning, agency, "
        "or connection - and what would genuinely feed it?"),
    how_it_works=(
        "The mistakes fail through distinct mechanisms that all converge "
        "on threshold or resource damage. The stimulation dump and the "
        "scroll train the threshold upward: each intense-but-empty hit "
        "raises the bar for what counts as satisfying, so ordinary "
        "engagement gets harder. Shaming and forced cheer spend control "
        "resources on masking while the gap persists - effort up, cause "
        "untouched. Outsourcing atrophies agency, the prerequisite of "
        "engagement, in a use-it-or-lose-it dynamic. Numbing borrows "
        "neurochemical credit: the rebound flatness is worse than the "
        "original, and the cycle tightens. Identity-labeling is the most "
        "insidious because it operates at the belief level: once boredom "
        "is 'who I am,' situations stop being evaluated for fit - the "
        "search function itself is disabled. The single diagnostic "
        "question works because it bypasses all seven failure modes at "
        "once: it reframes the state as situational and specific (not "
        "identity, not shameful), it identifies the true deficit (not "
        "the shiny decoy), and it points at genuine feeding (not numbing "
        "or masking). Teach the question until it is reflex, and the "
        "seven mistakes lose their recruits."),
    key_points=[
        "Seven mistakes: stimulation dump, shaming, scroll-as-remedy, forced cheer, outsourcing, numbing, identity-labeling.",
        "Stimulation without meaning trains the threshold upward.",
        "Shame and forced cheer spend control resources while the gap persists.",
        "Identity-labeling disables the search function itself - the most insidious mistake.",
        "One antidote question: which channel is starving, and what would genuinely feed it?",
    ],
    requirements=[
        "Seven mistakes with mechanisms",
        "Why each fails globally despite local logic",
        "The single antidote question",
    ],
    standards=["Maladaptive regulation strategies (Gross); threshold dynamics"],
    citations=[CIT_BENCH, CIT_DANCKERT],
    sig_lens=(
        "His Signature lens posts the seven mistakes as warnings on the "
        "garrison wall, each with its true name beneath the friendly "
        "mask: the noise that starves, the shame that ferments, the "
        "scroll that raises the bar, the grin that exhausts, the "
        "waiting that atrophies, the draught that borrows, the label "
        "that imprisons. The Signature soldier learns the wall by heart, "
        "not from fear but from craft - a fortress is kept as much by "
        "knowing what not to do as by knowing what to do. And above the "
        "seven warnings hangs the single standing order, in letters of "
        "gold: ASK WHICH CHANNEL STARVES, AND FEED IT TRULY. One order, "
        "honestly kept, defeats seven enemies.")),
]
# ---------------------------------------------------------------- 32-34: related emotions, mixes, full simulation
ENTRIES += [
dict(
    key="boredom_related_emotions", name="The Boredom Neighborhood: Neighbors, Opposites, and Close Cousins",
    group="Advanced", ladder_rank=32, ladder_tier="advanced",
    description=(
        "Boredom's neighborhood is crowded, and telling the neighbors "
        "apart is a genuine skill. Apathy is the closest cousin and the "
        "most important distinction: boredom wants engagement and cannot "
        "find it; apathy has stopped wanting. The bored person is "
        "restless with appetite; the apathetic person is flat without "
        "hunger. Misreading one as the other mistreats both - the bored "
        "need worthy work, the apathetic need care beyond this database's "
        "scope. Restlessness is boredom's roommate: pure restlessness "
        "wants motion, boredom wants meaning - the blend was mapped in "
        "its own record. Frustration is the blocked-goal neighbor: "
        "frustration knows what it wants and cannot have it; boredom "
        "does not know what it wants, only that this is not it. "
        "Loneliness borders the connection channel: the crowded party "
        "with no real conversation can read as either, but loneliness "
        "aches for people while boredom aches for engagement - the "
        "remedies differ. Weariness is the energy neighbor: genuine "
        "tiredness wants rest and takes it gladly; boredom's heaviness "
        "refuses rest's cure. Melancholy is the meaning neighbor at a "
        "deeper register: a passing hollow afternoon versus a settling "
        "grey - duration and depth draw the line. The opposites complete "
        "the map: curiosity (attention happily engaged), flow (skill and "
        "challenge in full embrace), and enthusiasm (energy with "
        "direction). The neighborhood map is a diagnostic instrument: "
        "place the feeling correctly, and the remedy follows; misplace "
        "it, and the treatment misses."),
    how_it_works=(
        "Discrimination works by testing each neighbor against the four "
        "channels - challenge, meaning, agency, connection - plus the "
        "appetite question. Apathy fails the appetite test: no hunger "
        "for engagement, so the boredom remedies (worthy work) misfire - "
        "this is the critical safety distinction, because persistent "
        "apathy deserves professional attention, not productivity tips. "
        "Restlessness passes appetite but fails the meaning test - it "
        "wants discharge, not depth. Frustration names its blocked goal "
        "while boredom cannot name what it wants - ask 'what would fix "
        "this' and frustration answers specifically, boredom answers "
        "vaguely. Loneliness fails the connection channel specifically "
        "while other channels read fine. Weariness fails the energy "
        "test: offer genuine rest and weariness accepts with relief, "
        "boredom refuses the cure. Melancholy is distinguished by depth "
        "and duration - the grey that settles over weeks is beyond "
        "boredom's remit. The opposites are defined by channel fullness: "
        "curiosity is attention fed, flow is challenge met, enthusiasm "
        "is energy aimed. Teach the map as a flowchart - appetite? which "
        "channel? how long? - and learners gain a reliable instrument "
        "for placing any flat feeling they meet."),
    key_points=[
        "Apathy vs boredom is the critical distinction: appetite present or absent.",
        "Frustration knows what it wants; boredom only knows this is not it.",
        "Loneliness aches for people; boredom aches for engagement.",
        "Weariness accepts rest's cure; boredom refuses it.",
        "Opposites: curiosity, flow, enthusiasm - each defined by channel fullness.",
    ],
    requirements=[
        "Six neighbors discriminated with tests",
        "Three opposites mapped by channel",
        "Flowchart-style discrimination method",
    ],
    standards=["Differential description methodology; APA definitional boundaries"],
    citations=[CIT_APA, CIT_DANCKERT],
    sig_lens=(
        "His Signature lens surveys the neighborhood as a king surveys "
        "border provinces: each with its own customs, each requiring its "
        "own diplomacy. Apathy is the province in mourning - send "
        "counselors, not taskmasters. Frustration is the province under "
        "siege - send relief to the specific breach. Loneliness is the "
        "province without roads - build connections, not spectacles. "
        "The Signature cartographer maps before marching, because armies "
        "sent to the wrong province lose the campaign before it begins. "
        "And the opposites - curiosity, flow, enthusiasm - are the allied "
        "kingdoms across the border, proof that every flat province can "
        "be cultivated back to fertility. No land is cursed; some only "
        "await their proper crop.")),
dict(
    key="boredom_emotion_mixes", name="Boredom Blends: Four Mixes and What Each Feels Like",
    group="Advanced", ladder_rank=33, ladder_tier="advanced",
    description=(
        "Boredom blended with other emotions produces distinct compounds, "
        "each with its own weather. Boredom plus restlessness is agitated "
        "boredom - the fidgeting, pacing, phone-checking storm mapped in "
        "its own record: high energy, no direction, the engine screaming "
        "in neutral. Boredom plus irritation is the short fuse: the "
        "flatness curdles into prickliness, small things offend, the "
        "voice sharpens - this is the blend behind the snapped remark in "
        "the dull meeting, and it asks for both engagement and a cooling "
        "of the fuse. Boredom plus melancholy is the grey blend: the "
        "hollow deepens into a quiet sorrow without a clear object, "
        "afternoons feel heavy with unspecified loss - gentler than the "
        "agitated storm but harder to lift, because it borrows sadness's "
        "weight. Boredom plus curiosity is the promising blend: the "
        "restless appetite meets an open mind, and the flatness becomes "
        "a searching energy - the 'there must be something interesting "
        "here' state that precedes discovery. This last blend is the "
        "proof that boredom is raw material: same unengaged attention, "
        "but paired with curiosity's forward lean, it becomes the "
        "launchpad of exploration rather than the pit of flatness. The "
        "practical art is blend identification: name the partner, and "
        "the remedy doubles - answer the boredom with engagement AND "
        "answer the partner on its own terms (cool the irritation, "
        "honor the melancholy's weight, follow the curiosity's lead)."),
    how_it_works=(
        "Blends follow the dyad logic: each partner contributes its "
        "appraisal and its action tendency, and the compound inherits "
        "both. Restlessness contributes high arousal plus the urge to "
        "move; boredom contributes disengaged attention plus the urge "
        "for change - the compound is high-energy searching with no "
        "target. Irritation contributes lowered provocation thresholds; "
        "boredom contributes the flat appraisal that everything is "
        "unsatisfying - the compound snaps at whatever is nearest. "
        "Melancholy contributes the meaning-channel deficit at depth; "
        "boredom contributes the attention deficit at the surface - the "
        "compound is hollow in two registers at once. Curiosity "
        "contributes the forward lean of engaged searching; boredom "
        "contributes the appetite without the object - the compound is "
        "appetite with a compass. The identification method is "
        "subtractive: describe the total state, subtract what pure "
        "boredom would feel like, and the remainder names the partner. "
        "The double-remedy principle follows from the structure: single "
        "remedies fail because they leave half the compound unfed - cool "
        "the irritation but leave the flatness, and the fuse relights; "
        "feed engagement but ignore the melancholy's weight, and the "
        "grey returns. Name both, feed both."),
    key_points=[
        "Four blends: agitated (restlessness), short-fuse (irritation), grey (melancholy), promising (curiosity).",
        "Each blend inherits both partners' appraisal and action tendency.",
        "The curiosity blend proves boredom is raw material: appetite with a compass becomes exploration.",
        "Identify by subtraction: total state minus pure boredom names the partner.",
        "Double-remedy principle: feed the boredom AND answer the partner on its own terms.",
    ],
    requirements=[
        "Four blends with felt descriptions",
        "Dyad logic: what each partner contributes",
        "Subtractive identification and double-remedy principle",
    ],
    standards=["Plutchik dyad structure; componential blend analysis"],
    citations=[CIT_BENCH, CIT_ELPIDOROU],
    sig_lens=(
        "His Signature lens reads the blends as alloys: boredom the base "
        "metal, each partner the element that transforms it. Restlessness "
        "forges it brittle and sparking; irritation tempers it sharp; "
        "melancholy casts it heavy and grey; curiosity - the noble "
        "element - transmutes it into the keen steel of exploration. "
        "The Signature metallurgist does not curse the base metal; he "
        "chooses his alloying elements with care, and when the wrong "
        "alloy forms, he re-melts with intention: cool the sharp, lighten "
        "the grey, and whenever possible, add curiosity - the element "
        "that turns the dullest ore into a blade. Every blend is "
        "re-forgeable; no alloy is final.")),
dict(
    key="boredom_full_simulation", name="Full Behavioral Simulation: Boredom From Trigger to Resolution",
    group="Advanced", ladder_rank=34, ladder_tier="advanced",
    description=(
        "The showcase simulation: one boredom episode, walked from first "
        "trigger to full resolution. Scene one - the trigger: Saturday, "
        "2pm, plans cancelled by rain. The apartment is familiar to the "
        "point of invisibility. Wanted engagement: high (a free day "
        "stretched ahead). Offered: nothing. The mismatch registers "
        "quietly - attention's first skim. Scene two - the climb: an "
        "hour passes in micro-decisions. The fridge is opened, closed. "
        "Three streaming menus are browsed, nothing chosen - too much "
        "choice paralyzing the start. The phone is checked, put down, "
        "checked again. Sighs deepen; the clock is consulted with "
        "growing disbelief. Inner monologue: 'I should do something... "
        "there is nothing to do... this day is wasted.' Scene three - "
        "the peak: restlessness joins - the blend. Pacing begins. A "
        "small irritation flares at a neighbor's music. The urge for "
        "change is now physical, almost painful; the temptation toward "
        "cheap escape peaks - the scroll, the snack, the argument. This "
        "is the chain-reaction danger zone, where one wrong link could "
        "spoil the evening. Scene four - the turn: instead of the cheap "
        "escape, the practices engage. The audit names it: challenge "
        "channel starving, meaning thread thin. The worthy list is "
        "consulted: the letter unwritten for a month, the shelf "
        "unbuilt, the walk untaken. Agency is claimed - the day gets "
        "an author again. Scene five - resolution: the shelf project "
        "begins. Measuring, sawing, fitting - challenge matched to "
        "skill, hands busy, attention locking on. Time resumes its "
        "normal pace; the flatness drains like water from a tub. By "
        "evening there is the clean tiredness of effort, not the flat "
        "tiredness of nothing - and the small pride of a shelf that "
        "did not exist at noon. The simulation's lesson, stated once: "
        "boredom is unclaimed capacity; the claim is always available; "
        "the only question is whether it gets claimed by intention or "
        "by accident."),
    how_it_works=(
        "The simulation is constructed to exercise every mechanism in "
        "the database in sequence. Scene one assembles the classic "
        "trigger skeleton - high wanted engagement, low offered, open "
        "duration, low choice (rain). Scene two demonstrates onset "
        "mechanics: the skim, the too-much-choice paralysis, the cheap "
        "novelty loop. Scene three stages the blend (restlessness "
        "joining), the peak dials, and the chain-reaction danger - the "
        "moment where escalation becomes possible. Scene four applies "
        "the instrument panel: reading the state (audit), asking the "
        "antidote question (which channel starves), consulting the "
        "worthy list, reclaiming agency - the full healthy-expression "
        "toolkit in action. Scene five demonstrates resolution "
        "mechanics: challenge matched to skill producing engagement, "
        "time perception normalizing, flat tiredness replaced by clean "
        "tiredness. As a teaching artifact, the simulation lets a "
        "learner rehearse the entire arc mentally before living it - "
        "recognition without the suffering, practice without the cost. "
        "Run it in the mind twice and the real Saturday goes "
        "differently: the trigger is spotted at scene one, the turn is "
        "made at scene two, and scenes three through five become a "
        "shorter, kinder story."),
    key_points=[
        "Five scenes: trigger, climb, peak, turn, resolution - the full arc in one episode.",
        "Scene three is the danger zone: blend, peak dials, chain-reaction risk.",
        "Scene four applies the whole toolkit: audit, antidote question, worthy list, reclaimed agency.",
        "Resolution mechanics: challenge matched to skill, attention locking, time normalizing.",
        "Mental rehearsal lets learners practice the arc before living it.",
    ],
    requirements=[
        "Five-scene arc with inner monologue and behavior",
        "Every database mechanism exercised in sequence",
        "Rehearsal value stated for the learner",
    ],
    standards=["Scenario-based affective training; integrative case method"],
    citations=[CIT_ELPIDOROU, CIT_CSIKSZENTMIHALYI],
    sig_lens=(
        "His Signature lens stages the simulation as the commander's "
        "finest hour in miniature: the rained-out Saturday as a siege, "
        "the climb as the enemy's sapping, the peak as the assault on "
        "the walls, the turn as the commander's rally - audit, worthy "
        "list, reclaimed agency, the orders given at last - and the "
        "resolution as the sortie that breaks the siege: the shelf "
        "built, the day retaken, the clean tiredness of victory. In "
        "this lens the episode is not a suffering endured but a battle "
        "won, and its retelling is a war-story for the garrison: "
        "remember the Saturday, remember the turn, and no siege of "
        "flatness will ever again find these walls uncommanded. The "
        "showcase piece earns its place: it proves the whole doctrine "
        "in a single day.")),
]

assert len(ENTRIES) == 34, "expected 34 entries, got %d" % len(ENTRIES)
_ranks = [e["ladder_rank"] for e in ENTRIES]
assert _ranks == sorted(_ranks) == list(range(1, 35)), "ladder ranks must be 1-34 in order"
_tiers = [e["ladder_tier"] for e in ENTRIES]
assert _tiers == ["foundations"] * 9 + ["compounded"] * 12 + ["advanced"] * 13, "tier bands wrong"
for e in ENTRIES:
    for k in ("key", "name", "group", "ladder_rank", "ladder_tier", "description",
              "how_it_works", "key_points", "requirements", "standards",
              "citations", "sig_lens"):
        assert k in e, "missing %s" % k
    assert len(e["description"]) > 200, "stub description in %s" % e["key"]
    assert len(e["key_points"]) >= 4, "thin key_points in %s" % e["key"]
    blob = (e["description"] + e["how_it_works"] + e["sig_lens"]).lower()
    assert "facebook" not in blob and "bat belt" not in blob
