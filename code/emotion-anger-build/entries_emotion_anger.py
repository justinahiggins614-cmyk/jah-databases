#!/usr/bin/env python3
"""Entries for the Anger Emotion databases (Manon's 2026-10-17 16:15 order,
emotion series batch 1).

Descriptive and educational ONLY - the database describes and simulates
anger; it never diagnoses real people, never labels any real person with an
emotional state, and never offers therapeutic advice beyond general, safe,
everyday guidance. No clinical language, no diagnostic labels. Healthy
expression records emphasize constructive handling.

34 records, ordered by the teaching ladder (ladder_rank 1-10,
non-decreasing), following the shared emotion-template spec:
what anger IS -> first-person simulation -> body signals -> facial
expression -> triggers -> behavior -> healthy expression -> recognizing it
in others -> related emotions and mixes -> complex behavioral simulation.

ID prefixes: JAH-EMAN- (public) and JAH-EMANS- (signature), verified free
in the manifest id_prefix values (2,442 databases, zero hits) and in all
jah-databases-data-1 shard index files (1,132,703 index lines, zero
'JAH-EMAN' substring hits), 2026-10-17.

Public records are real, fact-checked psychology knowledge (Ekman,
Plutchik, Lazarus, Gross, Scherer, Izard, Cannon, Schachter and Singer,
Averill, Lerner and Tiedens, APA Dictionary). Signature editions are his
original Signature lens - anger as the soul's pressure forge, signal and
fuel mastered, never presented as authentic public record.

Never the words "bat belt" anywhere. No website references. No Facebook.
No religious talk. Nothing hate-adjacent, profane, or inappropriate.
"""

SIG_TAIL = ("Signature original - his original Signature lens: anger as the "
            "soul's pressure forge, the honest alarm of a violated boundary; "
            "Signature editions frame every facet as signal, fuel, and "
            "mastery - never as a diagnosis, never labeling any real person, "
            "and never presented as authentic public record.")

CIT_EKMAN = ("Ekman P. Emotions Revealed: Recognizing Faces and Feelings to "
             "Improve Communication and Emotional Life. Holt; 2003.")
CIT_PLUTCHIK = ("Plutchik R. Emotion: A Psychoevolutionary Synthesis. "
                "Harper & Row; 1980.")
CIT_LAZARUS = ("Lazarus RS. Emotion and Adaptation. Oxford University Press; "
               "1991.")
CIT_GROSS = ("Gross JJ, editor. Handbook of Emotion Regulation. 2nd ed. "
             "Guilford; 2014.")
CIT_SCHERER = ("Scherer KR. Appraisal considered as a process of multilevel "
               "sequential checking. In: Scherer KR, Schorr A, Johnstone T, "
               "editors. Appraisal Processes in Emotion. Oxford; 2001.")
CIT_IZARD = ("Izard CE. The Psychology of Emotions. Plenum; 1991.")
CIT_CANNON = ("Cannon WB. Bodily Changes in Pain, Hunger, Fear and Rage. "
              "2nd ed. Appleton; 1929.")
CIT_SCHACHTER = ("Schachter S, Singer JE. Cognitive, social, and "
                 "physiological determinants of emotional state. "
                 "Psychological Review. 1962;69(5):379-399.")
CIT_AVERILL = ("Averill JR. Anger and Aggression: An Essay on Emotion. "
               "Springer; 1982.")
CIT_LERNER = ("Lerner JS, Tiedens LZ. Portrait of the angry decision maker: "
              "How appraisal tendencies shape anger's influence on "
              "cognition. Journal of Behavioral Decision Making. "
              "2006;19(2):115-137.")
CIT_APA = ("American Psychological Association. APA Dictionary of "
           "Psychology; current edition.")
CIT_DAMASIO = ("Damasio AR. Looking for Spinoza: Joy, Sorrow, and the "
               "Feeling Brain. Harcourt; 2003.")
CIT_SCHERER_WALLBOTT = ("Scherer KR, Wallbott HG. Evidence for universality "
                        "and cultural variation of differential emotion "
                        "response patterning. Journal of Personality and "
                        "Social Psychology. 1994;66(2):310-328.")
CIT_NOVACO = ("Novaco RW. Anger as a risk factor for violence among the "
              "mentally disordered. In: Monahan J, Steadman HJ, editors. "
              "Violence and Mental Disorder. University of Chicago Press; "
              "1994.")

ENTRIES = [
# ---------------------------------------------------------------- 1-4: what anger IS
dict(
    key="anger_definition", name="What Anger Is: A Plain-Language Definition",
    group="Foundations", ladder_rank=1, ladder_tier="foundations",
    description=(
        "Anger is the emotion you feel when something feels wrong, unfair, "
        "or blocking your way. In everyday words: anger is the mind's alarm "
        "that a boundary has been crossed, a goal has been blocked, or an "
        "injustice has been witnessed. Psychologists describe it as a basic, "
        "primary emotion - one of the small family of feelings that show up "
        "across cultures and appear early in life. Unlike moods, which drift "
        "in without a clear cause and linger for hours, anger usually arrives "
        "with a clear trigger: something happened, and the feeling points "
        "at it. That pointing quality - the sense of 'this made me angry' - "
        "is one of anger's defining traits. The word covers a whole volume "
        "range, from the faint annoyance of a slow queue to the full blaze "
        "of outrage, but the family name is the same because the underlying "
        "signal is the same: something needs to change. Anger is not "
        "inherently good or bad; it is information. What matters is what a "
        "person does with the signal."),
    how_it_works=(
        "The anger sequence runs in four beats: appraisal, arousal, urge, "
        "and action. First the mind appraises an event - this is unfair, "
        "this blocks me, someone meant to do this - which is why the same "
        "event angers one person and amuses another. Appraisal researchers "
        "describe this as a rapid check of relevance, fairness, and who is "
        "responsible. Second, the body arouses: heart rate climbs, muscles "
        "tense, attention narrows onto the trigger. Third comes the action "
        "urge: anger is an 'approach' emotion, pulling a person toward the "
        "obstacle rather than away from it, which is what makes it feel so "
        "different from fear. Fourth, the person acts on the urge - speaking "
        "up, pushing back, fixing the problem - or works with the feeling in "
        "some other way. Understanding this chain is the key to everything "
        "else in this database: change the appraisal, and the anger shifts; "
        "give the arousal somewhere to go, and the urge eases."),
    key_points=[
        "Anger is a basic, primary emotion with a clear trigger - unlike moods, it points at something.",
        "The core signal is: a boundary crossed, a goal blocked, or an injustice witnessed.",
        "The sequence is appraisal -> arousal -> urge -> action; each step is a place the feeling can be worked with.",
        "Anger is an approach emotion - it pulls a person toward the obstacle, which is why it feels so different from fear.",
        "The feeling itself is information, not a verdict; what matters is what follows.",
    ],
    requirements=[
        "Everyday definition a student or writer can quote",
        "Clear contrast between emotion and mood",
        "The four-beat sequence stated in plain words",
        "No diagnostic language anywhere in the record",
    ],
    standards=["APA Dictionary of Psychology definition of anger and emotion"],
    citations=[CIT_APA, CIT_LAZARUS],
    sig_lens=(
        "The Signature lens reads anger as the soul's pressure forge: the "
        "alarm that fires when a boundary of the true self is crossed. "
        "Where public psychology calls it appraisal, the Signature method "
        "calls it the boundary sense - the built-in instrument that reports "
        "when the world pushes against what is right. His reading treats "
        "the four-beat sequence as a forge cycle: signal, heat, strike, "
        "and temper. The heat is never the enemy; an untempered strike is. "
        "Clearly labeled Signature-made, never presented as authentic "
        "public record."),
),
dict(
    key="anger_emotion_family", name="Anger in the Emotion Family: Basic Roots and Complex Branches",
    group="Foundations", ladder_rank=2, ladder_tier="foundations",
    description=(
        "Anger sits near the center of the emotion map. Most emotion "
        "researchers count it among the basic or primary emotions - the "
        "small set that appears across cultures, shows in the face the same "
        "way everywhere, and arrives early in development. From this root, "
        "branches grow into more complex forms. Irritation and annoyance "
        "are the mild shoots. Frustration is anger mixed with a blocked "
        "goal. Outrage is anger mixed with moral judgment. Contempt blends "
        "anger with a sense of superiority. Resentment is anger that has "
        "been stored over time. Jealousy blends anger with fear of loss. "
        "Each complex branch keeps anger's core - the violated boundary or "
        "blocked goal - and adds a partner feeling or a time dimension. "
        "Knowing the family tree matters because it changes what to do: "
        "irritation wants a small fix, resentment wants an old wound "
        "examined, and outrage wants a wrong addressed. Treating them all "
        "as 'just anger' misses the message each one carries."),
    how_it_works=(
        "Emotion-family models like Plutchik's wheel arrange feelings by "
        "similarity and intensity, and anger sits opposite fear on the "
        "wheel - approach versus avoidance. The wheel also shows blends: "
        "anger plus anticipation makes aggression, anger plus disgust makes "
        "contempt, anger plus sadness makes sulkiness. These blends are not "
        "poetry; researchers have found that people reliably report them as "
        "distinct experiences. The family view also explains why anger "
        "changes partners so easily: because its core signal (something is "
        "wrong) attaches to almost any other feeling. Add surprise and you "
        "get shock-turning-hot; add shame and you get the heat of "
        "humiliation; add love for the wronged person and you get protective "
        "fury. The root stays the same; the branches tell you which message "
        "the anger is carrying."),
    key_points=[
        "Anger is a basic, primary emotion recognized across cultures.",
        "Complex forms (resentment, contempt, outrage, frustration) are anger plus a partner feeling or a time dimension.",
        "Plutchik's wheel places anger opposite fear: approach versus avoidance.",
        "Naming the exact branch matters because each one asks for a different response.",
    ],
    requirements=[
        "State anger's place among basic emotions",
        "List at least six complex branches with their partners",
        "Explain why the blend names are useful, not just labels",
    ],
    standards=["Plutchik wheel structure; Ekman basic-emotion criteria"],
    citations=[CIT_PLUTCHIK, CIT_EKMAN],
    sig_lens=(
        "The Signature lens maps the emotion family as a forge with many "
        "anvils: the same heat shaped into different tools. His method "
        "names each branch as a distinct instrument - the chisel of "
        "irritation, the stored ember of resentment, the hammer of outrage "
        "- and teaches that a master smith picks the right instrument for "
        "the work. The core heat is one; the crafted tools are many. "
        "Clearly labeled Signature-made, never presented as authentic "
        "public record."),
),
dict(
    key="anger_intensity_scale", name="Anger at Three Volumes: Mild, Moderate, and Intense",
    group="Foundations", ladder_rank=2, ladder_tier="foundations",
    description=(
        "Anger is one emotion with a volume knob. At the mild end sits "
        "annoyance and irritation: the feeling is light, thinking stays "
        "clear, and the body barely notices. A person at this level can "
        "name the feeling, laugh about it, and fix the cause with a small "
        "action. At the moderate level - plain anger - the feeling has "
        "weight. The heart beats faster, the voice tightens, attention "
        "locks onto the trigger, and thinking narrows: the rest of the "
        "world fades while the cause fills the frame. Decisions get faster "
        "and blunter. At the intense end - rage and fury - the body is "
        "flooded. Fine motor control drops, the voice shakes or booms, "
        "hearing seems to tunnel, and judgment narrows to a single channel: "
        "the threat. Researchers note that at the highest intensities the "
        "thinking brain is partly overridden by older alarm circuits, which "
        "is why people later say 'I was not myself.' The same emotion, "
        "three volumes - and each volume needs a different response. Mild "
        "anger wants a conversation; moderate anger wants a pause and a "
        "plan; intense anger wants the body calmed before any words are "
        "chosen."),
    how_it_works=(
        "Intensity rises with three dials: importance of the blocked goal, "
        "perceived unfairness or intent, and the body's current load. A "
        "trivial slight on a rested day is a whisper; the same slight after "
        "a sleepless night and three earlier insults is a shout. The "
        "arousal system has no separate channels for these - it sums them. "
        "This is why anger so often seems 'out of proportion': the visible "
        "trigger is only the last coin dropped into a jar that was already "
        "nearly full. The volume also feeds back on itself: higher arousal "
        "narrows appraisal, narrowed appraisal finds more threat, more "
        "threat raises arousal. Breaking that loop - by lowering any one "
        "dial - is how the volume comes down. Cooling the body, rechecking "
        "the intent, or shrinking the stakes all turn the same knob."),
    key_points=[
        "Mild: annoyance - light, clear thinking, small fix works.",
        "Moderate: anger - arousal up, attention narrowed, needs a pause and a plan.",
        "Intense: rage - flooded body, tunneled judgment, the body must calm before words.",
        "Intensity sums three dials: goal importance, perceived unfairness or intent, and existing load.",
        "The 'out of proportion' reaction is usually a full jar meeting its last coin.",
    ],
    requirements=[
        "Three clearly separated volume levels with lived detail",
        "The three intensity dials named and explained",
        "The feedback loop between arousal and appraisal stated",
    ],
    standards=["Lazarus appraisal-to-arousal model; APA intensity definitions"],
    citations=[CIT_LAZARUS, CIT_AVERILL],
    sig_lens=(
        "The Signature lens reads the volume knob as the forge's bellows: "
        "the same flame, fanned harder. His method teaches reading the "
        "bellows rather than blaming the flame - a smith does not curse "
        "the fire for being hot. The three dials become three bellows "
        "handles: the stakes, the insult, and the load already carried. "
        "Mastery is learning to ease each handle in turn until the flame "
        "is working heat, not wildfire. Clearly labeled Signature-made, "
        "never presented as authentic public record."),
),
dict(
    key="anger_myths", name="Myths and Misunderstandings About Anger",
    group="Foundations", ladder_rank=3, ladder_tier="foundations",
    description=(
        "Anger carries more myths than almost any other emotion, and the "
        "myths cause real harm. Myth one: anger is always bad or wrong. In "
        "fact researchers document anger as a signal with real functions - "
        "it flags injustice, energizes action, and communicates that a "
        "boundary matters. Myth two: venting anger gets it out of the "
        "system. Studies of venting find the opposite: rehearsing angry "
        "thoughts and actions usually feeds the feeling and raises "
        "aggression, because the brain practices what it repeats. Myth "
        "three: anger always leads to aggression. Most angry episodes end "
        "without any aggression at all - in talking, in problem-solving, in "
        "walking away. Myth four: you can tell an angry person is dangerous "
        "by how angry they look. Appearance predicts poorly; behavior "
        "history predicts far better. Myth five: feeling anger means you "
        "are an angry person. Emotions are weather, not climate: a person "
        "can feel anger often or rarely, handle it well or badly, and the "
        "feeling alone says nothing about their character. Clearing these "
        "myths matters because they steer people wrong: the myths say "
        "suppress it or explode, while the evidence says express it "
        "clearly, early, and well."),
    how_it_works=(
        "Each myth survives because it contains a grain of truth wrapped "
        "in a wrong conclusion. Venting does feel relieving in the moment - "
        "the grain - but the relief comes from the pause and the "
        "expression, not from the rehearsal of hostility, and the rehearsal "
        "is what trains the next episode to be hotter. Anger does sometimes "
        "precede aggression - the grain - but the link runs through "
        "choices, habits, and context, not through the feeling itself. Two "
        "people can feel identical anger; one talks, one throws. The "
        "difference is not the feeling but the trained response to it. "
        "This is the practical payoff of the myths record: once a person "
        "sees the feeling and the action as two separate things, the whole "
        "database opens up - every later record is about working the space "
        "between feeling anger and choosing what follows."),
    key_points=[
        "Anger is a signal with functions, not a moral failure.",
        "Venting usually feeds anger rather than releasing it.",
        "Most anger episodes end without aggression; feeling and action are separate.",
        "A loud appearance does not predict danger; behavior history does.",
        "Emotions are weather, not climate: the feeling says nothing about character.",
    ],
    requirements=[
        "Five myths, each with the research finding against it",
        "The grain-of-truth explanation for why myths survive",
        "Bridge to the feeling-versus-action separation",
    ],
    standards=["Bushman et al. catharsis findings via Gross Handbook; Averill on anger without aggression"],
    citations=[CIT_GROSS, CIT_AVERILL],
    sig_lens=(
        "The Signature lens calls the myths 'soot on the forge window' - "
        "they cloud the reading of a clean signal. His method replaces "
        "each myth with a smith's rule: the fire is not the sin, the "
        "untended fire is; rehearsing the strike tempers nothing, it only "
        "sharpens the wrong edge; weather is not climate, and a storm "
        "crossing the sky does not make the sky a storm. Clearly labeled "
        "Signature-made, never presented as authentic public record."),
),
# ---------------------------------------------------------------- 5-9: how it feels
dict(
    key="anger_first_person", name="Inside the Feeling: A First-Person Passage of Anger",
    group="Foundations", ladder_rank=3, ladder_tier="foundations",
    description=(
        "This record is a simulation - a described passage written so a "
        "reader, writer, or actor can know what anger feels like from the "
        "inside. It describes no real person. 'It starts as a tightening, "
        "like a hand closing around my ribs. My jaw finds itself clenched "
        "before I decide anything. The room gets louder and narrower at the "
        "same time: every small sound sharp, everything except the cause "
        "fading to the edges. There is a heat behind my eyes and a pressure "
        "in my chest that wants to push outward, as if the feeling needs "
        "more room than my body gives it. My thoughts start arriving "
        "pre-sharpened - every memory of the person or the situation comes "
        "back with its worst detail first. Time feels sped up and slowed "
        "down together: I want to act now, this second, and yet each second "
        "drags while I hold the words in. Underneath the heat there is "
        "something strangely clear, a certainty: this is wrong, and I "
        "know it. The feeling is not asking for my opinion. It is "
        "presenting a fact and waiting for me to move.' Writers use "
        "passages like this to render anger honestly; readers use them to "
        "recognize the shape of a universal human experience in words."),
    how_it_works=(
        "First-person simulation works because emotions have a stable "
        "phenomenology - the 'what it is like' of anger is similar across "
        "people even when triggers differ. The passage above was built "
        "from the documented components: the appraisal of wrongness, the "
        "autonomic arousal (tightening, heat, pressure), the narrowed "
        "attention, the sharpened and selective memory, the approach urge "
        "('act now'), and the felt certainty that researchers call the "
        "certainty appraisal of anger. Simulation records like this one are "
        "the archive's descriptive instruments: they let a reader compare "
        "their own experience against a documented pattern, which is "
        "educational, and they let creators render the emotion faithfully, "
        "which is craft. The record never claims this is what any specific "
        "real person feels; it claims this is the shape the feeling "
        "commonly takes."),
    key_points=[
        "Simulation is description, not diagnosis: it renders the common shape of the feeling.",
        "The passage assembles documented components: appraisal, arousal, narrowed attention, selective memory, approach urge, felt certainty.",
        "Anger's felt certainty ('this is wrong, and I know it') is one of its most reported features.",
        "The record serves readers (recognition) and creators (faithful rendering).",
    ],
    requirements=[
        "A first-person passage in present tense",
        "Every element of the passage traceable to documented anger features",
        "Explicit statement that no real person is described",
    ],
    standards=["Phenomenological description per Izard; appraisal components per Scherer"],
    citations=[CIT_IZARD, CIT_SCHERER],
    sig_lens=(
        "The Signature lens treats first-person simulation as 'stepping "
        "into the forge' - feeling the heat from the smith's side of the "
        "anvil rather than watching from the door. His method holds that "
        "anger can only be mastered from the inside: the hand that knows "
        "the heat can shape with it, while the hand that only reads about "
        "heat keeps getting burned. The passage above is the forge door "
        "opened. Clearly labeled Signature-made, never presented as "
        "authentic public record."),
),
dict(
    key="anger_time_course", name="The Time Course of Anger: Onset, Peak, Fading, and Aftershock",
    group="Foundations", ladder_rank=4, ladder_tier="foundations",
    description=(
        "Anger has a shape in time, and knowing the shape helps a person "
        "ride it instead of being ridden. Onset is fast: from trigger to "
        "full feeling often takes seconds, because the appraisal system is "
        "built for speed. The peak arrives quickly too - most anger "
        "episodes studied by researchers crest within the first minutes, "
        "which is why the worst words usually come early. Then comes the "
        "fading: if nothing feeds the feeling, arousal decays over minutes "
        "to tens of minutes, the way a struck bell's tone dies. Thinking "
        "clears as the body settles. But anger has a fourth phase other "
        "emotions often lack: the aftershock. Hours later, a reminder - a "
        "name, a place, the drive home - can re-fire a smaller, sharper "
        "echo of the original episode. Rumination stretches the whole "
        "curve: replaying the trigger re-strikes the bell, so the fading "
        "never finishes. This is why the oldest anger advice is also the "
        "most evidence-backed: wait. Not to suppress the feeling, but to "
        "let the curve do its natural work before choosing words."),
    how_it_works=(
        "The curve is driven by two clocks: the fast alarm clock of the "
        "autonomic nervous system and the slow clock of conscious "
        "appraisal. Adrenaline and related arousal chemicals clear from "
        "the bloodstream on a scale of minutes, which sets the natural "
        "decay rate - the bell cannot ring forever. But the appraisal "
        "clock can re-trigger the alarm indefinitely: every mental replay "
        "of the insult is processed as a fresh event by the fast system. "
        "Researchers call this the rumination effect, and it is the main "
        "reason some angers last minutes and others last weeks. The "
        "aftershock is the appraisal clock firing on a cue - a reminder "
        "that re-opens the file. Interventions map onto the curve exactly: "
        "slow breathing and movement cool the fast clock; reframing and "
        "problem-solving quiet the slow clock; and refusing the replay "
        "lets the bell's tone die on its own schedule."),
    key_points=[
        "Onset is seconds-fast; most episodes crest within the first minutes.",
        "Without fuel, arousal decays over minutes to tens of minutes like a struck bell.",
        "Aftershock: a later cue can re-fire a smaller, sharper echo hours afterward.",
        "Rumination re-strikes the bell - it is the main reason some angers last weeks.",
        "Waiting works because it lets the natural decay curve finish before words are chosen.",
    ],
    requirements=[
        "Four phases named and timed in plain language",
        "The two clocks (autonomic and appraisal) explained",
        "Rumination identified as the curve-stretcher",
    ],
    standards=["Cannon on autonomic arousal; Gross on rumination and regulation timing"],
    citations=[CIT_CANNON, CIT_GROSS],
    sig_lens=(
        "The Signature lens reads the time course as the cooling curve of "
        "forged steel: strike while the metal is hot, but quench - cool - "
        "before the final shaping. His method teaches the smith to know "
        "the metal's clock: the bell's tone dies on its own, the "
        "aftershock is the ember hiding in the ash, and rumination is "
        "stoking a fire you meant to let go out. Patience is not "
        "passivity; it is metallurgy. Clearly labeled Signature-made, "
        "never presented as authentic public record."),
),
dict(
    key="anger_low_vs_high", name="Anger at Low Intensity and at High Intensity: Two Lived Snapshots",
    group="Foundations", ladder_rank=4, ladder_tier="foundations",
    description=(
        "Two snapshots, same emotion, different volumes - both simulations, "
        "describing no real person. Snapshot one, low intensity: 'The "
        "email is rude in a small, careless way. I feel a flicker behind "
        "my ribs, like a match struck and blown out. My shoulders lift a "
        "fraction. I read the line twice, notice the annoyance the way "
        "you notice weather through a window, and type a reply that is "
        "shorter than I want it to be and warmer than I feel. By the time "
        "I stand up for coffee, the feeling has thinned to a memory of "
        "itself. I am already thinking about something else.' Snapshot two, "
        "high intensity: 'The betrayal lands all at once. Sound goes flat "
        "and close, like hearing through water. My hands are shaking and I "
        "did not tell them to. The room narrows to one face, one sentence, "
        "replaying. Every past slight lines up behind this one like "
        "witnesses. My chest is too small for what is in it. Words are "
        "stacking up behind my teeth and they all want out at once, and I "
        "know - with a cold thread under the heat - that the next sixty "
        "seconds will decide what this costs me.' The contrast teaches the "
        "core lesson of the volume knob: low anger is a messenger that "
        "can be read calmly; high anger is a flood that must be waited "
        "out before its message is answered."),
    how_it_works=(
        "The two snapshots differ along every documented dimension of "
        "intensity. Physiologically: a flicker of tension versus shaking "
        "hands and a pounding chest. Attentionally: noticing-through-a-"
        "window versus the room narrowing to one face. Cognitively: the "
        "mind stays on its errands versus past slights lining up as "
        "witnesses - the selective-memory effect that intensifies with "
        "arousal. Temporally: thinning to a memory within minutes versus a "
        "felt certainty that the next sixty seconds decide the cost. "
        "Researchers use exactly this kind of contrast to show that "
        "intensity is not just 'more of the same' - at high volumes the "
        "feeling recruits different systems and the person's capacities "
        "genuinely change. The low snapshot demonstrates anger's everyday "
        "manageability; the high snapshot demonstrates why the standard "
        "advice for peak anger is to change the body's state first and "
        "choose words second."),
    key_points=[
        "Low intensity: flicker of tension, attention stays wide, the feeling thins within minutes.",
        "High intensity: shaking, tunneled attention, selective memory, words stacking behind the teeth.",
        "Intensity is not just more-of-the-same: different systems are recruited at high volumes.",
        "The practical split: read the messenger calmly at low volume; wait out the flood at high volume.",
    ],
    requirements=[
        "Two present-tense first-person snapshots",
        "Each dimension of contrast named (body, attention, thought, time)",
        "The 'not just more of the same' research point stated",
    ],
    standards=["Averill on anger episodes; Schachter and Singer on arousal interpretation"],
    citations=[CIT_AVERILL, CIT_SCHACHTER],
    sig_lens=(
        "The Signature lens sets the two snapshots side by side as the "
        "apprentice's first lesson at the forge: the same fire at banked "
        "coals and at full bellows. His method trains the eye to read "
        "which fire is burning before choosing the tool - you do not shape "
        "with tongs what needs the quench bucket. The cold thread under "
        "the heat, the witness that watches the flood, is the Signature "
        "self learning its trade. Clearly labeled Signature-made, never "
        "presented as authentic public record."),
),
dict(
    key="anger_frustration_blend", name="Anger Mixed With Its Most Common Partner: Frustration",
    group="Foundations", ladder_rank=5, ladder_tier="foundations",
    description=(
        "Ask people what they were feeling in their last angry episode and "
        "the most common partner named is frustration - so common that "
        "everyday speech treats them as one word. They are not. Frustration "
        "is the feeling of a blocked goal: the printer jams before the "
        "deadline, the code will not compile, the door will not open. "
        "Anger is the feeling of a wrong: someone or something is at "
        "fault. The blend - frustrated anger - is the most frequent anger "
        "in daily life, and it feels like this (simulation): 'The form "
        "rejects my application for the third time and nobody can tell me "
        "why. The blockage is the frustration - the wall I keep hitting. "
        "The heat toward the unhelpful clerk is the anger - somebody built "
        "this wall and somebody is paid to stand at it. I am furious at a "
        "wall and at a person at the same time, and the two feelings keep "
        "trading places: the wall makes me blame the person, the person "
        "makes the wall feel personal.' Untangling the blend is practical: "
        "the frustration half wants problem-solving (another route around "
        "the wall), while the anger half wants communication (the wall "
        "should not be here). Treating the whole blend as pure anger picks "
        "fights with people when the real enemy is the wall; treating it "
        "as pure frustration tinkers with the wall while the unfairness "
        "festers."),
    how_it_works=(
        "Frustration and anger share the blocked-goal appraisal but split "
        "on agency: frustration's appraisal is 'my path is blocked,' "
        "anger's is 'someone blocked my path' or 'this should not be "
        "blocked.' Appraisal theory predicts exactly this blend pattern - "
        "when a blocked goal also carries a whiff of unfairness or "
        "blameworthy agency, the two feelings fuse. The fusion is why the "
        "blend is so common: modern life is full of blocked goals with "
        "human fingerprints on them - bureaucracies, bad design, other "
        "drivers. The blend also explains the classic 'displaced' anger: "
        "the frustration half has no person to address (the printer cannot "
        "listen), so the anger half borrows the nearest person. Naming the "
        "two halves gives each its proper tool: fix the wall with "
        "engineering, address the person with words - and check which one "
        "the heat is really about before choosing."),
    key_points=[
        "Frustration = blocked goal; anger = wrong or fault; the blend is daily life's most frequent anger.",
        "The blend fuses when a blocked goal carries unfairness or blameworthy agency.",
        "Displaced anger is often frustration with no one to address, borrowing the nearest person.",
        "Untangle first: problem-solve the wall, communicate about the person.",
    ],
    requirements=[
        "Clean definitions separating frustration from anger",
        "A first-person blend passage",
        "The displacement mechanism explained",
        "Two-tool prescription (engineer the wall, address the person)",
    ],
    standards=["Lazarus and Scherer appraisal dimensions: goal blockage vs agency"],
    citations=[CIT_LAZARUS, CIT_SCHERER],
    sig_lens=(
        "The Signature lens names the blend 'the wall and the warden' - "
        "the obstacle and the one who stands at it. His method teaches "
        "the smith to strike the wall with engineering and address the "
        "warden with words, never confusing the two targets. A hammer "
        "swung at a person when the wall is the problem breaks the wrong "
        "thing; words spent on a wall when a warden blocks the way move "
        "nothing. Read the blend, split the targets, choose the tool. "
        "Clearly labeled Signature-made, never presented as authentic "
        "public record."),
),
dict(
    key="anger_day_vignette", name="A Day With Anger: A Day-in-the-Life Vignette",
    group="Foundations", ladder_rank=5, ladder_tier="foundations",
    description=(
        "A simulation of anger moving through one ordinary day - describing "
        "no real person. Morning: the alarm fails and the bus leaves early. "
        "Irritation flickers - low volume, handled with a joke to a fellow "
        "passenger, gone by the second stop. Mid-morning: a coworker takes "
        "credit for the idea in the meeting. The flicker returns with "
        "weight this time; the jaw tightens. The feeling is named silently "
        "- 'I am angry because my work was claimed' - and a note is made "
        "to raise it privately later. Naming it keeps it at moderate "
        "volume instead of letting it ferment. Lunch: the sandwich order is "
        "wrong for the third time this week. The morning's stored heat "
        "joins it - the jar nearly full, the last coin. A sharp sigh, a "
        "decision to eat it anyway, and a mental note that the real "
        "problem is the morning, not the sandwich. Afternoon: the private "
        "conversation happens. The anger is expressed as a clear sentence "
        "- 'When my work is presented as yours, I feel undermined, and I "
        "need us to fix how credit works' - and the coworker, to "
        "everyone's surprise including the narrator's, apologizes and "
        "fixes it. Evening: the day's heat has somewhere to go - a long "
        "walk, dinner, the body settling. The aftershock tries once, on "
        "the drive home, replaying the meeting. It is noticed, labeled "
        "'replay,' and let pass. The day ends with the anger spent the way "
        "a day's work is spent: used, not stored."),
    how_it_works=(
        "The vignette is a teaching instrument that threads every "
        "foundations concept through one narrative: the volume knob "
        "(flicker to weight to near-full jar), the time course (onset, "
        "peak, fading, aftershock), the frustration-anger blend (the "
        "sandwich versus the meeting), naming as a regulation tool, and "
        "expression as a clear sentence rather than an explosion or a "
        "bottling. Each beat demonstrates a principle in action so the "
        "reader sees the whole system working, not just listed. The "
        "structure also models the healthy pattern the later records teach "
        "in detail: notice early, name precisely, separate the triggers, "
        "express clearly, discharge the body, and let the replay pass. A "
        "day-in-the-life record is the ladder's hinge - it turns abstract "
        "knowledge into a recognizable human day, which is what makes the "
        "compounded records that follow feel like continuations rather "
        "than new subjects."),
    key_points=[
        "One day threads all foundations concepts: volume, time course, blends, naming, expression.",
        "The sandwich scene demonstrates the full-jar effect: stored heat joining a small trigger.",
        "The meeting scene demonstrates clear-sentence expression versus exploding or bottling.",
        "The drive-home scene demonstrates noticing and releasing an aftershock replay.",
        "The vignette is the ladder's hinge: abstract knowledge becomes a recognizable day.",
    ],
    requirements=[
        "A full day arc: morning, mid-morning, lunch, afternoon, evening",
        "Each scene tied to a foundations concept",
        "Healthy handling modeled without preaching",
    ],
    standards=["Averill on everyday anger episodes; Gross on situation-level regulation"],
    citations=[CIT_AVERILL, CIT_GROSS],
    sig_lens=(
        "The Signature lens reads the day as a smith's full shift at the "
        "forge: small heats worked cleanly, one real forging done well, "
        "the ash swept at evening. His method honors the narrator's "
        "craft - each heat named, each strike aimed, nothing stored in "
        "the walls to smolder overnight. A day spent this way is the "
        "Signature ideal: the fire serves the work, and the smith goes "
        "home clean. Clearly labeled Signature-made, never presented as "
        "authentic public record."),
),
# ---------------------------------------------------------------- 10-13: body signals
dict(
    key="anger_body_signals", name="The Body in Anger: Heart, Breath, Muscles, Stomach, Skin, and Energy",
    group="Compounded", ladder_rank=5, ladder_tier="compounded",
    description=(
        "Anger is a full-body event, and the body keeps the most honest "
        "record of it. The heart speeds up - often by twenty to thirty "
        "beats per minute in a strong episode - pumping blood toward the "
        "muscles that anger is preparing for action. Breathing quickens "
        "and shallows, moving up into the chest. The big muscles tense: "
        "jaw, neck, shoulders, fists - the classic anger posture is a body "
        "gathering itself. The stomach often knots or churns as digestion "
        "is deprioritized; some people feel nausea at high intensity. The "
        "skin flushes as blood vessels dilate - the visible reddening of "
        "the face and neck - and may prickle with heat or break into a "
        "light sweat. Energy surges: anger is one of the most energizing "
        "emotions, which is why angry people pace, gesture broadly, and "
        "feel they must move. Researchers describe this as the "
        "fight-or-flight mobilization Cannon first mapped: the body cannot "
        "tell a blocked goal from a physical threat, so it prepares for "
        "both the same way. Learning to read these signals is the "
        "earliest warning system anger offers - the body usually knows a "
        "full minute before the mind admits it."),
    how_it_works=(
        "The signal chain runs through the sympathetic nervous system: the "
        "appraisal of threat or violation activates alarm circuits, which "
        "release adrenaline and related chemicals, which raise heart rate, "
        "tense muscles, shunt blood to the limbs, and sharpen the senses. "
        "This is fast, automatic, and older than conscious thought - which "
        "is why the body reacts before a person has 'decided' to be angry. "
        "The mobilization is metabolically expensive, so it cannot be "
        "sustained indefinitely; the natural decay of the chemicals sets "
        "the fading phase of the time course. Each body channel is also a "
        "regulation lever: slow diaphragmatic breathing directly counters "
        "the quickened breath, unclenching the jaw and dropping the "
        "shoulders sends safety signals back up the chain, and vigorous "
        "movement burns off the mobilized energy the way it was designed "
        "to be used. The body is both the alarm and the control panel."),
    key_points=[
        "Heart rate climbs, breathing quickens and shallows, jaw/neck/shoulders/fists tense.",
        "Stomach knots, skin flushes with heat, energy surges toward movement.",
        "The pattern is Cannon's fight-or-flight mobilization: the body prepares for a blocked goal like a physical threat.",
        "The body usually signals a full minute before the mind admits the anger - it is the earliest warning system.",
        "Each channel is a regulation lever: breath, muscle release, and movement all cool the chain.",
    ],
    requirements=[
        "Six body systems covered: heart, breath, muscles, stomach, skin, energy",
        "The sympathetic chain explained in plain words",
        "Body-as-control-panel: each signal paired with its lever",
    ],
    standards=["Cannon 1929 fight-or-flight; Schachter and Singer arousal"],
    citations=[CIT_CANNON, CIT_SCHACHTER],
    sig_lens=(
        "The Signature lens reads the body as the forge's own "
        "instrumentation: the bellows-rate of the breath, the heat-gauge "
        "of the skin, the tension of the tongs in the jaw and fists. His "
        "method trains the smith to read the gauges before the metal "
        "overheats - the body is the honest apprentice that reports what "
        "the proud mind denies. Every signal is both alarm and handle: "
        "the breath can be slowed, the shoulders dropped, the mobilized "
        "energy walked into work. Clearly labeled Signature-made, never "
        "presented as authentic public record."),
),
dict(
    key="anger_posture_movement", name="Posture and Movement: How Anger Carries the Body",
    group="Compounded", ladder_rank=6, ladder_tier="compounded",
    description=(
        "Long before a word is spoken, anger rearranges the body in space. "
        "The posture signature is expansion and forwardness: chest "
        "broadened, shoulders squared, chin level or lifted, weight "
        "shifted forward onto the balls of the feet. Where fear shrinks "
        "the body to present a smaller target, anger enlarges it - the "
        "body is making itself bigger for the confrontation it expects. "
        "Gestures grow larger and sharper: hands chop the air, fingers "
        "point, arms cross hard across the chest as a barricade or swing "
        "wide for emphasis. The stride changes - faster, heavier, more "
        "deliberate; angry walking is famously recognizable from a "
        "distance. Micro-movements leak too: foot tapping, pen clicking, "
        "the jaw working side to side. At high intensity the movements can "
        "turn jerky as fine motor control degrades under arousal. Actors "
        "and animators study exactly this signature because it reads "
        "instantly across a room: the forward lean, the squared shoulders, "
        "the chopping hand. And the signature works in reverse as well - "
        "deliberately softening the posture, uncrossing the arms, and "
        "slowing the stride sends calming feedback to the feeling itself, "
        "a lever the healthy-expression records return to."),
    how_it_works=(
        "Posture is the visible end of the approach system: anger prepares "
        "the organism to move toward the obstacle, so the body organizes "
        "for forward motion - weight forward, chest open, limbs ready. "
        "This is partly display (many species enlarge themselves in "
        "conflict) and partly mechanics (a body braced to act). The "
        "leakage movements - tapping, clicking, jaw-working - are "
        "mobilized energy with nowhere to go, the engine idling hard. "
        "Researchers of embodied emotion have shown the loop runs both "
        "directions: adopting an expansive forward posture can raise "
        "feelings of power and assertiveness, while deliberately softening "
        "it damps them. That bidirectionality is why posture is both a "
        "reading cue for observers and a regulation tool for the person "
        "feeling the anger. Change the carriage, and the feeling follows "
        "at a short distance."),
    key_points=[
        "Signature: expansion and forwardness - squared shoulders, chin level, weight forward.",
        "Fear shrinks the body; anger enlarges it for expected confrontation.",
        "Leakage movements (tapping, jaw-working) are mobilized energy idling.",
        "The loop runs both ways: softening posture damps the feeling - a regulation lever.",
        "The signature reads across a room, which is why actors and animators study it.",
    ],
    requirements=[
        "Posture, gesture, gait, and micro-movements all described",
        "The fear-versus-anger contrast stated",
        "Bidirectionality: posture as cue and as lever",
    ],
    standards=["Ekman on bodily display; embodied-emotion findings via Gross Handbook"],
    citations=[CIT_EKMAN, CIT_GROSS],
    sig_lens=(
        "The Signature lens reads posture as the smith's stance at the "
        "anvil: squared, forward, ready to strike. His method teaches "
        "that stance is a choice even when the heat is not - the master "
        "smith can stand at full readiness and still choose which blow "
        "to land, or whether to set the hammer down. Softening the "
        "stance is not surrender; it is the decision to work the metal "
        "with tongs instead of fists. Clearly labeled Signature-made, "
        "never presented as authentic public record."),
),
dict(
    key="anger_sleep_appetite_energy", name="Sleep, Appetite, and Energy Under Anger",
    group="Compounded", ladder_rank=6, ladder_tier="compounded",
    description=(
        "Anger does not clock out when the episode ends; it bills the "
        "body afterward. Sleep is the first creditor. Arousal and anger "
        "are chemically opposed to sleep onset: the mobilized body does "
        "not downshift on command, and the replaying mind - the "
        "rumination that re-strikes the bell - keeps the appraisal clock "
        "ticking past midnight. People report lying awake rehearsing what "
        "they should have said, then waking unrefreshed into a shorter "
        "fuse the next day, which is how one angry evening manufactures "
        "the next day's anger. Appetite splits: some people lose all "
        "interest in food while the stomach is knotted, eating nothing "
        "until the feeling passes; others eat urgently, seeking the "
        "soothing chemistry of a full stomach. Neither pattern is "
        "orderly, and both are the body spending its budget on the alarm "
        "instead of maintenance. Energy follows a spike-and-debt curve: "
        "the surge of the episode feels like power, but the mobilization "
        "is expensive, and the aftermath often brings a flat, grey "
        "fatigue - the crash after the flood. Understanding this billing "
        "cycle reframes anger management as energy management: protect "
        "sleep, eat on schedule, and spend the surge on movement, and the "
        "next day's fuse stays long."),
    how_it_works=(
        "The mechanism is resource competition. The sympathetic arousal "
        "that powers anger draws on the same budget as sleep onset, "
        "digestion, and sustained attention - the body cannot fully fund "
        "an alarm state and maintenance at once. Cortisol and related "
        "stress chemistry, elevated during angry episodes, directly "
        "interfere with the sleep architecture, fragmenting rest even "
        "when sleep comes. Rumination extends the funding: every replay "
        "re-authorizes the alarm budget. The next-day short fuse is then "
        "simple arithmetic - a tired, underfed, unrestored system has "
        "fewer reserves for the appraisal work that keeps small triggers "
        "small. This is why the everyday-practices record treats sleep "
        "hygiene and regular meals as anger tools rather than general "
        "wellness advice: they are literally fuse-length maintenance."),
    key_points=[
        "Anger bills the body afterward: sleep, appetite, and energy all pay.",
        "Rumination past midnight manufactures the next day's short fuse.",
        "Appetite splits - lost or urgent - as the body funds alarm over maintenance.",
        "Energy spikes then crashes: the surge feels like power, the aftermath is flat fatigue.",
        "Sleep and meals are fuse-length maintenance, not generic wellness tips.",
    ],
    requirements=[
        "Sleep, appetite, and energy each given a mechanism",
        "The next-day short fuse explained as resource arithmetic",
        "Reframe: anger management as energy management",
    ],
    standards=["Selye stress physiology; sleep-arousal findings via Gross Handbook"],
    citations=[CIT_CANNON, CIT_GROSS],
    sig_lens=(
        "The Signature lens reads the billing cycle as the forge's fuel "
        "ledger: every heat drawn must be paid for in coal, and a smith "
        "who burns the night's fuel on replay wakes to cold iron. His "
        "method keeps strict books - sleep guarded like the coal shed, "
        "meals taken on schedule like stoking times, the surge spent on "
        "real work rather than on pacing the floor. A master never "
        "borrows tomorrow's heat for today's replay. Clearly labeled "
        "Signature-made, never presented as authentic public record."),
),
dict(
    key="anger_body_differences", name="No Two Bodies Anger Alike: How Body Signals Differ Between People",
    group="Compounded", ladder_rank=7, ladder_tier="compounded",
    description=(
        "The anger body has a common blueprint, but every person builds "
        "it differently. One person's anger lives in the jaw - clenched "
        "teeth, aching temples. Another's lives in the hands - fists "
        "before thoughts. A third feels it as stomach churn and nausea, a "
        "fourth as heat rising up the neck into the ears, a fifth as a "
        "cold, still focus with almost no visible arousal at all. Some "
        "people flush crimson; some go pale as blood routes to the core. "
        "Some get loud and fast; some get quiet and precise, which "
        "observers often misread as calm. These differences come from "
        "genetics, from training - athletes and performers often show "
        "different arousal patterns - from culture's display rules, and "
        "from sheer habit: the body learns where it keeps its anger the "
        "way a river learns its channel. The practical lesson is "
        "humility in reading others: the quiet, pale, still person may be "
        "at full volume inside, and the loud, red, pacing person may be at "
        "moderate volume with an expressive style. Never diagnose a "
        "feeling from its costume. For the self, the lesson is to learn "
        "one's own channel - where does MY anger live? - because the "
        "personal early-warning signal is always the fastest lever."),
    how_it_works=(
        "Individual differences in anger physiology arise at three "
        "levels. The hardware level: autonomic reactivity varies "
        "genetically, so the same trigger produces different heart-rate "
        "and adrenaline responses in different people. The software "
        "level: display rules learned in family and culture dictate which "
        "channels are allowed - a child punished for shouting learns to "
        "route anger into the jaw or the stomach. The habit level: "
        "repeated episodes carve preferred channels, so the tenth anger "
        "flows where the first nine went. Researchers measuring "
        "physiology during anger provocation consistently find this "
        "spread: the average pattern is real, but the individual "
        "deviations are large. This is why the recognition records teach "
        "clusters of cues rather than single tells, and why the "
        "first-person records in this database are offered as common "
        "shapes, not universal scripts. The map is shared; the territory "
        "is personal."),
    key_points=[
        "Common blueprint, personal build: jaw, hands, stomach, neck-heat, or cold stillness.",
        "Flushing versus paling, loud versus quiet - style is not volume.",
        "Differences come from genetics, display rules, and carved habit channels.",
        "Reading others requires cue clusters, never a single tell; never diagnose from the costume.",
        "Everyone should learn their own channel - the personal early-warning signal.",
    ],
    requirements=[
        "At least five distinct personal channels described",
        "The style-is-not-volume warning stated plainly",
        "Three levels of difference: hardware, software, habit",
    ],
    standards=["Scherer and Wallbott on individual and cultural variation"],
    citations=[CIT_SCHERER_WALLBOTT, CIT_IZARD],
    sig_lens=(
        "The Signature lens honors the personal channel as the smith's "
        "own forge layout: no two forges vent heat through the same "
        "chimney. His method forbids reading another's chimney as a "
        "diagnosis - the quiet forge may burn hottest - and commands "
        "knowing one's own: where does my heat rise first, and what is "
        "my earliest gauge? Mastery begins at home, at one's own anvil. "
        "Clearly labeled Signature-made, never presented as authentic "
        "public record."),
),
# ---------------------------------------------------------------- 14-17: facial expression
dict(
    key="anger_face", name="The Face of Anger: Eyes, Brows, Mouth, and Micro-Signs",
    group="Compounded", ladder_rank=7, ladder_tier="compounded",
    description=(
        "The angry face is one of the most universally recognized human "
        "signals, and its components are precise. The brows lower and draw "
        "together - the single most diagnostic feature, creating the "
        "vertical furrow between the eyebrows. The eyes narrow: the upper "
        "lids lower and the gaze hardens into a stare, sometimes with the "
        "whites showing above or below the iris in extreme cases. The "
        "nostrils may flare as breathing quickens. The mouth compresses - "
        "lips press together into a thin line, or the jaw sets with the "
        "teeth bared in a square-mouthed grimace at higher intensities. "
        "The micro-signs are what betray the feeling before the person "
        "chooses to show it: a flicker of the brow furrow lasting a "
        "fraction of a second, a quick compression of the lips, a single "
        "hard blink, the nostril flare that precedes the words. "
        "Researchers cataloging facial actions found this configuration "
        "recognized across cultures, including in societies with no "
        "exposure to outside media - the face of anger appears to be part "
        "of the human blueprint. For readers of others, the rule is "
        "clusters: brow plus eyes plus mouth together mean far more than "
        "any one feature, and the micro-signs are the early warning - the "
        "face usually knows before the voice does."),
    how_it_works=(
        "Each feature serves the approach system. The lowered, drawn-"
        "together brows shade and focus the eyes for the confrontation "
        "ahead - the glare is literally an aiming posture. The narrowed "
        "eyes reduce visual input to the target, matching the narrowed "
        "attention of the feeling. The compressed mouth and set jaw ready "
        "the vocal apparatus for forceful speech and, at the oldest level, "
        "for biting. The nostril flare feeds the quickened breathing. "
        "Micro-expressions - the sub-second leakages - occur because the "
        "facial muscles receive the emotional signal before conscious "
        "control can mask it; the feeling fires the face first and the "
        "mask arrives a fraction later. This timing gap is why trained "
        "observers watch the first half-second of a reaction: the "
        "unmasked face appears there, before the social face is put on. "
        "The universality finding matters for the whole database: when "
        "the text says 'the face of anger,' it describes a pattern "
        "recognized on every continent."),
    key_points=[
        "Brow lower-and-draw-together is the most diagnostic feature; eyes narrow into a stare; mouth compresses.",
        "Micro-signs - brow flicker, lip compression, nostril flare - fire before conscious masking.",
        "Each feature serves approach: the glare is an aiming posture, the set jaw readies forceful speech.",
        "The configuration is recognized across cultures, including media-isolated societies.",
        "Read clusters, not single features; watch the first half-second for the unmasked face.",
    ],
    requirements=[
        "Brows, eyes, nostrils, mouth, and micro-signs each described",
        "Functional explanation for each feature",
        "The universality finding stated",
    ],
    standards=["Ekman basic-emotion facial criteria; facial action coding"],
    citations=[CIT_EKMAN, CIT_SCHERER_WALLBOTT],
    sig_lens=(
        "The Signature lens reads the angry face as the forge's warning "
        "placard, hung by nature on every human door: the brow the "
        "lowered beam, the stare the aimed tongs, the compressed mouth "
        "the sealed furnace door. His method teaches reading the placard "
        "without fear and without diagnosis - it is information, posted "
        "by the body's honest apprentice before the mind's censor "
        "arrives. The smith who reads faces well never needs to guess "
        "at weather. Clearly labeled Signature-made, never presented as "
        "authentic public record."),
),
dict(
    key="anger_face_intensity", name="How the Angry Face Changes With Intensity",
    group="Compounded", ladder_rank=7, ladder_tier="compounded",
    description=(
        "The angry face is not one mask but a slider. At low intensity - "
        "annoyance - the signs are minimal: the brow lowers a few "
        "millimeters, the lips press once, the gaze holds a beat too long. "
        "A casual observer misses it; someone who knows the person catches "
        "it instantly. At moderate intensity the configuration assembles "
        "fully: the brow furrow deepens and locks, the eyes narrow into "
        "the sustained stare, the mouth sets into its line, the jaw "
        "begins its sideways work. Color joins the signal as the face and "
        "neck flush. At high intensity the face distorts: the brow drives "
        "down hard, the eyes may bulge with the whites showing, the mouth "
        "opens into the square grimace or shouts, veins stand out at the "
        "temples and neck, and the whole head may thrust forward. "
        "Asymmetry often appears at the peak - one side of the mouth "
        "pulling harder - because fine control is degrading. Then, as the "
        "episode fades, the face dismantles in reverse: the mouth softens "
        "first, the brow releases last, and a residual tightness can linger "
        "around the eyes for minutes. Knowing the slider matters for "
        "timing: the low-intensity face is the moment when a calm word "
        "still lands; the high-intensity face is the moment to give the "
        "body time before any words are chosen."),
    how_it_works=(
        "Facial intensity tracks muscular recruitment: low arousal fires "
        "only the most practiced muscles (the brow lowerers), moderate "
        "arousal recruits the full configuration, and high arousal "
        "over-recruits - extra muscles join, symmetry breaks down, and "
        "the vascular system adds color. The dismantling order reflects "
        "control returning: the mouth, under the most conscious control "
        "for speech, is released first when the person starts choosing "
        "words again; the brow, closer to the automatic system, holds its "
        "furrow longest. Observers can use the slider diagnostically - "
        "not to label the person, but to time their own response. "
        "Researchers note that people are surprisingly good at reading "
        "this slider in others when they attend to it; the skill is "
        "mostly a matter of looking. The record's practical rule: match "
        "your intervention to the face's volume, the same way you match "
        "it to the feeling's volume."),
    key_points=[
        "Low: millimeters of brow, one lip-press, a held gaze - caught only by those who know the person.",
        "Moderate: full configuration locks in - furrow, stare, set mouth, jaw work, flushing.",
        "High: distortion - bulging eyes, square grimace, visible veins, asymmetry as control degrades.",
        "The face dismantles in reverse: mouth softens first, brow releases last.",
        "Read the slider to time responses: calm words land at low volume, not at peak.",
    ],
    requirements=[
        "Three intensity stages of the face with concrete detail",
        "The dismantling order explained",
        "Practical timing rule for observers",
    ],
    standards=["Ekman on intensity and facial action; Scherer appraisal-intensity links"],
    citations=[CIT_EKMAN, CIT_SCHERER],
    sig_lens=(
        "The Signature lens reads the face-slider as the forge's "
        "temperature colors: the faint straw of annoyance, the orange "
        "of full anger, the white of the peak that warps the metal. His "
        "method trains the smith's eye to read color before touching - "
        "straw can be worked with words, orange needs the tongs of "
        "patience, white must cool before any shaping is attempted. "
        "Reading heat-color is the oldest skill at any forge. Clearly "
        "labeled Signature-made, never presented as authentic public "
        "record."),
),
dict(
    key="anger_hiding_faking", name="Hiding and Faking Anger: What Leaks Through",
    group="Compounded", ladder_rank=8, ladder_tier="compounded",
    description=(
        "People hide anger constantly - in meetings, at family tables, in "
        "customer service - and they fake it too, performing anger for "
        "effect in negotiations or on stage. The hidden anger leaks "
        "through the channels that conscious control reaches last. The "
        "brow is the worst liar: the furrow flickers even when the mouth "
        "smiles, because the upper face is less voluntarily controlled "
        "than the lower. The voice leaks next - tightened pitch, clipped "
        "consonants, the too-careful politeness that sounds like courtesy "
        "and feels like a warning. The body leaks after that: the "
        "foot tapping under the table, the pen gripped too hard, the "
        "shoulders that will not drop. Timing leaks as well: the smile "
        "that arrives a half-second late, the laugh that ends too "
        "abruptly. Faked anger leaks in the opposite direction - it is "
        "too symmetrical, too sustained, missing the micro-flickers of "
        "the real thing, and it often overplays the mouth while the brow "
        "stays oddly calm. Actors study this asymmetry deliberately: real "
        "anger starts in the brow, performed anger starts in the mouth. "
        "The ethical note matters here: noticing leakage is a tool for "
        "understanding, not for accusation. 'Your brow says otherwise' is "
        "a weapon; 'you seem tense - is something wrong?' is an "
        "invitation. The same observation serves cruelty or care "
        "depending on the hands that hold it."),
    how_it_works=(
        "The leakage hierarchy follows neuroanatomy: the lower face "
        "(mouth, jaw) has richer voluntary cortical control, while the "
        "upper face (brow, eyelids) is more directly wired to the "
        "emotional systems - so masking the mouth is easy and masking "
        "the brow is hard. Micro-expressions exploit the timing gap: the "
        "emotional signal reaches the face in milliseconds, while the "
        "voluntary mask takes a few hundred milliseconds to deploy, "
        "leaving a window where the true configuration flashes. Voice "
        "leaks because pitch and tension are regulated partly by the "
        "aroused autonomic system, which does not take orders politely. "
        "Faked anger fails the same tests in reverse: without the "
        "genuine autonomic surge, the performer must construct every "
        "channel consciously, and conscious construction produces "
        "symmetry, sustain, and the wrong onset order - mouth first, brow "
        "never quite committing. Knowing both directions serves the "
        "recognition records: real hidden anger shows brow-first leakage, "
        "performed anger shows mouth-first construction."),
    key_points=[
        "The brow is the worst liar: upper face is less voluntarily controlled than the mouth.",
        "Leakage hierarchy: brow flicker, then voice tension, then body, then timing.",
        "Faked anger is too symmetrical and sustained, mouth-first, brow oddly calm.",
        "Real anger starts in the brow; performed anger starts in the mouth.",
        "Noticing leakage is for understanding, never for accusation.",
    ],
    requirements=[
        "Hidden anger: four leakage channels in hierarchy order",
        "Faked anger: the reverse tells",
        "The ethical note on use versus accusation",
    ],
    standards=["Ekman on micro-expressions and voluntary control asymmetry"],
    citations=[CIT_EKMAN],
    sig_lens=(
        "The Signature lens calls leakage 'heat through the furnace "
        "seams' - no door seals perfectly, and the honest apprentice "
        "reports through the cracks. His method teaches reading the "
        "seams with respect: the flicker is information offered "
        "unintentionally, and using it to corner someone is the act of "
        "a poor smith. Faked heat, meanwhile, is paint on cold iron - "
        "symmetrical, sustained, and wrong in the brow - and the trained "
        "eye spots paint instantly. Clearly labeled Signature-made, "
        "never presented as authentic public record."),
),
dict(
    key="anger_expression_gallery", name="Drawing and Playing Anger: Expression Gallery Notes",
    group="Compounded", ladder_rank=8, ladder_tier="compounded",
    description=(
        "This record is a toolkit for artists, actors, animators, and "
        "writers who need to render anger faithfully - a gallery in "
        "words. For the illustrator: start with the brow - two short, "
        "heavy strokes angled down toward the center, with a vertical "
        "crease between them. Set the upper lids low over the eyes and "
        "angle the whole eye-line slightly downward at the inner corners. "
        "Draw the mouth as a single pressed line, thinner at the center, "
        "or as the square grimace with the corners pulled down and out. "
        "Add the neck tendons and a hint of flush high on the cheeks. For "
        "the actor: find the jaw first - set it, feel the temples engage - "
        "then let the breath move up into the chest and quicken. Fix the "
        "gaze on a single point and narrow it; let the hands want to chop "
        "or grip, then still them - the held-back gesture reads angrier "
        "than the released one. For the writer: anger on the page lives "
        "in verbs and in the unsaid - short sentences, interrupted "
        "rhythm, dialogue that answers the previous line's subtext "
        "instead of its text. For the animator: lead with the brow by "
        "four to six frames, let the head push forward on the peak, and "
        "hold the micro-flicker before the mask goes on - audiences read "
        "the flicker as truth. Across all crafts the same rule holds: "
        "build from the brow outward, keep it asymmetrical at the peak, "
        "and remember that restrained anger - the stillness holding the "
        "heat - reads stronger than flailing."),
    how_it_works=(
        "The gallery works because all four crafts are rendering the same "
        "underlying configuration documented in the face records - the "
        "notes translate the science into craft instructions. The "
        "'brow-first' rule for drawing and animation mirrors the "
        "neurological onset order: the brow fires first in real anger, so "
        "leading with it reads as authentic. The actor's 'held-back "
        "gesture' rule mirrors the approach urge under voluntary control - "
        "the audience perceives the contained energy, which is the actual "
        "phenomenology of managed anger. The writer's 'short sentences "
        "and subtext' rule mirrors the narrowed attention and sharpened "
        "cognition of the feeling. The animator's frame counts come from "
        "the micro-expression timing window. In each case the craft note "
        "is not invented style but the documented pattern wearing a "
        "costume - which is why audiences across cultures recognize the "
        "rendering: they are seeing their own blueprint reflected."),
    key_points=[
        "Illustrator: brow-first construction, angled eye-line, pressed mouth, neck tendons, cheek flush.",
        "Actor: jaw set, chest breath, fixed narrowed gaze, held-back gestures read angrier than released ones.",
        "Writer: short sentences, interrupted rhythm, dialogue answering subtext.",
        "Animator: lead with the brow by 4-6 frames, head push on peak, hold the pre-mask flicker.",
        "Universal craft rule: build brow-outward, allow peak asymmetry, restraint reads stronger than flailing.",
    ],
    requirements=[
        "Concrete instructions for four crafts: illustration, acting, writing, animation",
        "Each instruction tied to the documented facial/bodily pattern",
        "The restraint principle stated",
    ],
    standards=["Ekman facial configuration as the shared source pattern"],
    citations=[CIT_EKMAN, CIT_IZARD],
    sig_lens=(
        "The Signature lens treats the gallery as the smith's pattern "
        "book: the measured drawings by which apprentices learn the "
        "shapes before touching hot metal. His method insists the "
        "patterns be true - a false pattern teaches a false craft, and "
        "audience eyes, like metal, reveal every lie in the work. The "
        "restraint principle is his oldest teaching: the master shows "
        "the heat by the stillness that contains it, never by flailing "
        "at the air. Clearly labeled Signature-made, never presented as "
        "authentic public record."),
),
# ---------------------------------------------------------------- 18-21: triggers
dict(
    key="anger_classic_triggers", name="The Classic Triggers of Anger",
    group="Compounded", ladder_rank=8, ladder_tier="compounded",
    description=(
        "Across studies of everyday anger, the same triggers appear "
        "again and again. Being treated unfairly tops every list: the "
        "stolen credit, the broken promise, the rule applied to you and "
        "not to others. Close behind is being blocked - the goal "
        "obstructed by incompetence, bureaucracy, or another person "
        "standing in the way. Then comes disrespect: the insult, the "
        "dismissal, the contemptuous tone, being treated as if you do "
        "not matter. Betrayal of trust ranks high: the friend who shares "
        "the secret, the partner who lies. Being harmed or seeing harm "
        "done to someone you care about fires the protective variant. "
        "Being deceived or manipulated - discovering the game was rigged "
        "- triggers a particularly hot form, because it combines "
        "unfairness with insult to intelligence. And being powerless in "
        "the face of any of these multiplies the heat: the same unfair "
        "event angers more when nothing can be done about it. Notice the "
        "pattern underneath the list: every classic trigger is an "
        "appraisal of wrongness plus agency - something wrong happened, "
        "and someone or something is responsible. Triggers without "
        "agency (a storm ruins the picnic) produce frustration or "
        "sadness; add a responsible agent and the same event produces "
        "anger."),
    how_it_works=(
        "Triggers work through the appraisal check described in the "
        "definition record: the mind scans events for goal relevance, "
        "unfairness, and responsible agency, and anger fires when the "
        "scan returns 'wrong' plus 'someone's fault.' The classic list "
        "is simply the situations where that scan most often returns "
        "positive: social life is dense with fairness expectations and "
        "attributable agents, so unfairness, disrespect, betrayal, and "
        "deception dominate. The powerlessness multiplier works through "
        "the coping check - the appraisal of whether anything can be "
        "done. When coping looks possible, anger stays instrumental "
        "(fix the wrong); when coping looks impossible, the same anger "
        "turns ruminative and hot. This is why the healthiest first "
        "response to a trigger is the coping question - 'what can "
        "actually be done here?' - asked before the heat decides. The "
        "trigger list is also the map for the later records: each "
        "trigger type gets its matched healthy response."),
    key_points=[
        "Top triggers: unfairness, blocked goals, disrespect, betrayal, harm to loved ones, deception.",
        "Powerlessness multiplies the heat of any trigger.",
        "The pattern: wrongness appraisal plus responsible agency; without agency it is frustration, not anger.",
        "The coping question - 'what can actually be done?' - is the healthiest first response.",
        "Each trigger type maps to a matched healthy response in later records.",
    ],
    requirements=[
        "At least six classic triggers with examples",
        "The wrongness-plus-agency pattern stated",
        "The powerlessness multiplier explained",
    ],
    standards=["Averill on everyday anger precipitants; Lazarus appraisal dimensions"],
    citations=[CIT_AVERILL, CIT_LAZARUS],
    sig_lens=(
        "The Signature lens catalogs the classic triggers as the "
        "standard ores of the forge - the materials every smith learns "
        "to recognize by sight: unfairness-iron, betrayal-steel, "
        "disrespect-copper, deception-lead. His method teaches that "
        "knowing the ore predicts the heat: each standard ore fires at "
        "a known temperature and takes a known temper. The powerlessness "
        "multiplier is the closed damper - same ore, less air for "
        "action, hotter and smokier burn. Ask the coping question "
        "first: it opens the damper. Clearly labeled Signature-made, "
        "never presented as authentic public record."),
),
dict(
    key="anger_personal_triggers", name="Personal Triggers: Memories, Anniversaries, and Private Associations",
    group="Advanced", ladder_rank=9, ladder_tier="advanced",
    description=(
        "Beyond the classic triggers lies a private arsenal: the "
        "triggers only one person has. A particular tone of voice that "
        "matches a critical parent. A date on the calendar that marks an "
        "old betrayal - the anniversary effect, where the body remembers "
        "before the mind checks the date. A song, a smell, a street that "
        "reopens a closed file. A specific phrase - 'calm down,' 'you "
        "always,' 'whatever' - that has become fused with past "
        "conflicts through repetition. Being corrected in front of "
        "others, if humiliation was the childhood tax on mistakes. These "
        "triggers fire hotter and faster than classic ones because they "
        "bypass the appraisal check: the association is pre-compiled, so "
        "the alarm sounds before the mind has evaluated the current "
        "event. The person is reacting to the past wearing the present's "
        "clothes. The work with personal triggers is detective work: "
        "noticing the disproportion - 'why did THAT make me so angry?' - "
        "tracing the heat back to its original file, and relabeling the "
        "present event as present. None of this excuses acting on the "
        "trigger; it explains the trigger so the action can be chosen "
        "fresh. Everyone carries a few of these; maturity is knowing "
        "their names."),
    how_it_works=(
        "Personal triggers are learned associations - classical "
        "conditioning applied to emotion. An originally neutral cue (a "
        "tone, a date, a phrase) paired repeatedly with angry episodes "
        "becomes a conditioned trigger that fires the full response on "
        "its own. The anniversary effect adds state-dependent memory: "
        "the body encodes the season, the light, the context of the "
        "original wound, and the returning context re-activates the "
        "encoding. Because the association lives in fast memory systems, "
        "it outruns the slow appraisal check - the heat arrives with a "
        "pre-written story ('this is THAT again') that may not fit the "
        "current facts. The detective work that defuses them is "
        "re-appraisal with history: separating the then from the now. "
        "Each time the trigger fires and the person correctly relabels "
        "it, the association weakens a little - the clinical term is "
        "extinction, and it works through repetition, not through force. "
        "Knowing one's personal triggers by name is therefore not "
        "indulgence but maintenance: the named trigger can be watched "
        "for, while the unnamed one drives."),
    key_points=[
        "Personal triggers bypass appraisal: pre-compiled associations fire before evaluation.",
        "Common forms: tones, dates, songs, smells, fused phrases, public correction.",
        "The disproportion question - 'why did THAT make me so angry?' - starts the detective work.",
        "Relabeling then-versus-now weakens the association through extinction.",
        "Knowing them by name is maintenance, not indulgence; it never excuses the action.",
    ],
    requirements=[
        "At least five forms of personal trigger with examples",
        "The conditioning mechanism in plain words",
        "The detective-work method: notice, trace, relabel",
    ],
    standards=["Conditioning and state-dependent memory; Gross on reappraisal"],
    citations=[CIT_GROSS, CIT_SCHACHTER],
    sig_lens=(
        "The Signature lens names personal triggers 'old burns' - the "
        "places where the smith was seared long ago and now flinches "
        "from warm air. His method treats old burns with the respect "
        "due to real injuries: map them, name them, and never let an "
        "old burn choose today's strike. The detective work is the "
        "master's inventory - walking the forge, touching each scar, "
        "and saying 'that was then, this is now' until the flinch "
        "unlearns itself. Clearly labeled Signature-made, never "
        "presented as authentic public record."),
),
dict(
    key="anger_surprise_triggers", name="Surprise Triggers: The Unexpected Things That Set Off Anger",
    group="Advanced", ladder_rank=9, ladder_tier="advanced",
    description=(
        "Some triggers surprise everyone, including the person they "
        "fire in. Being startled - a sudden noise, someone appearing "
        "silently behind - often produces a flash of anger rather than "
        "fear, because the startle spikes arousal and the mind, finding "
        "no threat to flee, assigns the arousal to the nearest person: "
        "the classic misattribution. Hunger, exhaustion, and pain lower "
        "the threshold so far that trivial events - a slow elevator, a "
        "misplaced pen - detonate: the jar was already full, and the "
        "body's distress masquerades as anger at the elevator. "
        "Unexpected kindness after a long stretch of hostility can "
        "trigger tears of anger - the contrast cracks the armor. Having "
        "one's competence questioned in an area of pride, being laughed "
        "at when trying to be serious, the particular frequency of a "
        "chewing sound at the next table - the list of odd triggers is "
        "endless because association is personal. What unites them is "
        "the mechanism: high background arousal plus a small event plus "
        "the mind's habit of explaining arousal with the nearest story. "
        "The defense is the threshold check: 'am I hungry, tired, sore, "
        "or startled right now?' Asked honestly, that question dissolves "
        "a remarkable fraction of mysterious angers - the feeling was "
        "real, but its address was wrong."),
    how_it_works=(
        "Surprise triggers run on misattribution of arousal, the "
        "Schachter-Singer mechanism: the body produces arousal from one "
        "source (startle, hunger, fatigue, pain, heat, noise), and the "
        "mind, seeking an explanation, attaches it to whatever is "
        "nearby - usually a person or a small frustration. The arousal "
        "is real; the story about its cause is constructed, and the "
        "construction borrows anger's script because anger is the "
        "emotion of 'something is wrong and someone is responsible.' "
        "This is also why the triggers feel so convincing in the moment: "
        "the body is genuinely alarmed, so the mind's story feels true. "
        "The threshold check works by giving the arousal its correct "
        "address - food, rest, quiet - which starves the anger script of "
        "its fuel. Researchers note this is one of the most practical "
        "findings in emotion science: a large share of everyday anger is "
        "background arousal wearing a trigger's clothes, and the "
        "wardrobe change is often enough."),
    key_points=[
        "Startle, hunger, exhaustion, and pain lower the threshold until trivial events detonate.",
        "The mechanism is misattribution: real arousal from one source gets the nearest story.",
        "The feeling is real but its address is wrong - the elevator did not do it.",
        "The threshold check ('hungry, tired, sore, startled?') dissolves many mysterious angers.",
        "Odd triggers are endless because association is personal; the mechanism is shared.",
    ],
    requirements=[
        "At least five surprise triggers with the mechanism for each",
        "Schachter-Singer misattribution explained in plain words",
        "The threshold check as the practical defense",
    ],
    standards=["Schachter and Singer 1962 misattribution of arousal"],
    citations=[CIT_SCHACHTER, CIT_LAZARUS],
    sig_lens=(
        "The Signature lens calls surprise triggers 'stray sparks' - "
        "heat from another fire landing on dry thatch. His method "
        "teaches the smith to ask where the spark came from before "
        "blaming the thatch: the hunger-fire, the fatigue-fire, the "
        "startle-flash. A master does not curse the spark's landing "
        "place; he traces it to its source and tends that fire. The "
        "threshold check is the morning inspection of all the forge's "
        "fires before the day's work begins. Clearly labeled "
        "Signature-made, never presented as authentic public record."),
),
dict(
    key="anger_chain_reactions", name="Chain Reactions: When One Trigger Ignites a Cascade",
    group="Advanced", ladder_rank=9, ladder_tier="advanced",
    description=(
        "Anger rarely travels alone - one trigger often ignites a "
        "cascade. The pattern is familiar: a bad morning (the alarm, the "
        "traffic) primes the system; a coworker's curt email, harmless "
        "on a good day, lands on primed arousal and sparks real anger; "
        "the anger narrows attention, so the lunch line's slowness "
        "registers as a fresh insult; by afternoon the person is snapping "
        "at a friend over nothing, and the shame of snapping adds its own "
        "heat. Each link has its own logic: priming raises the baseline, "
        "narrowed attention manufactures new triggers, expression "
        "without repair creates new causes (the snapped-at friend is now "
        "genuinely upset), and secondary emotions - shame, guilt, "
        "anxiety about the anger itself - join the fire. Researchers "
        "call the spread 'affect generalization': the feeling colors "
        "everything it touches until the world looks like one long "
        "provocation. Breaking a cascade means breaking any link: cool "
        "the body to drop the baseline, widen attention deliberately "
        "(name three neutral things in the room), repair quickly after a "
        "snap so it does not become a new trigger, and refuse the "
        "secondary shame-spiral by treating the anger as weather that "
        "passed, not as a verdict on character. Cascades feel inevitable "
        "from the inside; from the outside they are a chain, and chains "
        "have links."),
    how_it_works=(
        "The cascade runs on four linked mechanisms. Priming: residual "
        "arousal from an earlier event keeps the alarm half-cocked, so "
        "smaller triggers cross the threshold. Attentional narrowing: "
        "anger focuses perception on threat-relevant cues, which means "
        "an angry person literally notices more provocations - the world "
        "has not changed, the filter has. Behavioral spillover: angry "
        "actions create real interpersonal consequences (the snapped-at "
        "friend withdraws), which become genuine new triggers. Secondary "
        "appraisal: the person appraises their own anger ('I should not "
        "feel this'), generating shame or anxiety that adds arousal to "
        "the same pool. Each mechanism feeds the next, which is why "
        "cascades accelerate. Interventions are link-breakers: the body "
        "lever (movement, breath) attacks priming; deliberate attention-"
        "widening attacks the filter; quick repair attacks spillover; "
        "self-compassionate relabeling ('weather, not character') attacks "
        "the secondary appraisal. One broken link is often enough - the "
        "chain needs all of them to keep accelerating."),
    key_points=[
        "Cascades link priming, narrowed attention, behavioral spillover, and secondary emotions.",
        "Narrowed attention manufactures new triggers: the filter changes, not the world.",
        "Snapping creates real consequences that become genuine new triggers.",
        "Shame about the anger adds fuel; 'weather, not character' starves it.",
        "Break any one link - body, attention, repair, or relabeling - and the chain stalls.",
    ],
    requirements=[
        "A full cascade narrative from morning to afternoon",
        "Four mechanisms named with plain explanations",
        "Four matched link-breakers",
    ],
    standards=["Affect generalization; Gross on the anger-rumination spiral"],
    citations=[CIT_GROSS, CIT_AVERILL],
    sig_lens=(
        "The Signature lens reads the cascade as a forge fire jumping "
        "the firebreaks: one unattended heat catching the next bench, "
        "then the next, until the whole shop is involved. His method "
        "is firebreak discipline - cool the first heat, widen the gaze "
        "past the smoke, repair the scorched bench immediately, and "
        "never feed the fire with shame about the fire. A master "
        "smith's shop has firebreaks built in; the apprentice learns "
        "them by watching one cascade and vowing 'never again.' "
        "Clearly labeled Signature-made, never presented as authentic "
        "public record."),
),
# ---------------------------------------------------------------- 22-25: behavior
dict(
    key="anger_behavior_actions", name="What People Do When Angry: Typical Actions and Reactions",
    group="Advanced", ladder_rank=9, ladder_tier="advanced",
    description=(
        "Anger's action repertoire is wide, and most of it is not "
        "violence. The most common actions researchers observe are "
        "verbal and social: confronting, complaining, arguing, demanding "
        "an explanation, withdrawing coldly, or complaining to a third "
        "party. Then come the instrumental actions: fixing the problem, "
        "leaving the situation, writing the letter, making the call - "
        "anger as fuel for getting things done. Displacement actions "
        "follow: slamming a door, punching a pillow, driving too fast, "
        "cleaning the house with unusual violence - the energy discharged "
        "sideways. Avoidance actions appear too: the silent treatment, "
        "canceled plans, the cold shoulder - anger expressed as "
        "absence. And at the far end, the rare but real aggressive acts: "
        "shoving, throwing, hitting. The crucial research finding is the "
        "distribution: the verbal, instrumental, and avoidant actions "
        "account for the overwhelming majority of angry behavior; direct "
        "aggression is the exception, not the rule. This matters because "
        "the feeling-action separation lives here: a person can feel the "
        "full heat and still choose from the whole menu. The menu is "
        "learned - families and cultures teach which actions are on it - "
        "which means the menu can be deliberately expanded. Every "
        "healthy-expression record in this database is, at bottom, about "
        "adding better items to the menu."),
    how_it_works=(
        "Actions flow from the approach urge through the filter of "
        "learned scripts. The urge says 'move toward the obstacle'; the "
        "scripts - absorbed from family, peers, and culture - say how. A "
        "child who watched conflicts resolved with shouting learns "
        "shouting as the default script; one who watched calm "
        "confrontation learns that. Under high arousal the default "
        "script runs automatically, which is why people 'act like their "
        "parents' when furious: the newest learning is the first thing "
        "arousal disables. But scripts are rewritable through the same "
        "mechanism that wrote them - repetition under gradually rising "
        "heat. Practicing the clear-sentence confrontation at low "
        "intensity installs it as an available script; rehearsing the "
        "walk-away installs that. The behavior record's lesson is "
        "therefore hopeful and mechanical at once: nobody is stuck with "
        "their default menu, because menus are made of practice, and "
        "practice can be chosen."),
    key_points=[
        "The common actions are verbal, social, instrumental, and avoidant - aggression is the rare exception.",
        "Feeling-action separation: full heat still leaves the whole menu available.",
        "The menu is learned from family and culture - scripts, not instincts.",
        "High arousal runs the default script; new scripts are installed by practice at low intensity.",
        "Expanding the menu is the mechanical core of all healthy-expression work.",
    ],
    requirements=[
        "Five action families with examples",
        "The distribution finding: aggression as exception",
        "Scripts-learned-and-rewritable mechanism",
    ],
    standards=["Averill on anger action patterns; social-learning accounts"],
    citations=[CIT_AVERILL, CIT_LAZARUS],
    sig_lens=(
        "The Signature lens lays the action menu on the workbench like "
        "a smith's tools: the tongs of confrontation, the file of the "
        "clear sentence, the quench bucket of the walk-away, the broom "
        "of sideways discharge - and, hung highest and rusting, the "
        "war-hammer nobody needs. His method judges a smith by the "
        "tools, not the heat: the heat is given, the tools are chosen. "
        "Apprentices inherit a bench; masters curate it, adding better "
        "tools one practice at a time. Clearly labeled Signature-made, "
        "never presented as authentic public record."),
),
dict(
    key="anger_speech_patterns", name="What People Say When Angry: Phrases, Tone, and Speech Patterns",
    group="Advanced", ladder_rank=10, ladder_tier="advanced",
    description=(
        "Anger has a dialect, and fluent speakers are instantly "
        "recognizable. The characteristic phrases are absolutes and "
        "accusations: 'you always,' 'you never,' 'this is ridiculous,' "
        "'I cannot believe you,' 'after everything I have done.' The "
        "pronoun shifts to second person - 'you' does the damage, 'I' "
        "disappears - which is why the classic advice is to reverse it. "
        "Questions become weapons: 'are you serious right now?' is not "
        "a question. Tone carries more than words: pitch rises and "
        "tightens, volume climbs, consonants sharpen into clipping, "
        "pace accelerates - or, in the cold variant, pace slows to a "
        "deliberate, icy precision while volume drops. Speech patterns "
        "fragment: sentences shorten, interruptions multiply, the "
        "listener's replies get talked over, and the topic slides from "
        "the present issue to the entire history of grievances - the "
        "'kitchen sink' argument. Silence speaks too: the clipped 'fine,' "
        "the one-word answers, the door of conversation slammed shut. "
        "Writers use this dialect for instant characterization; "
        "listeners can use it as information. The phrases reveal the "
        "appraisal underneath - 'you always' means the trigger feels "
        "like a pattern, 'this is ridiculous' means the coping check "
        "failed. Hearing the dialect as data, rather than as attack, is "
        "the first skill of the recognition records."),
    how_it_works=(
        "The dialect is the appraisal system speaking aloud. Absolutes "
        "('always,' 'never') are the narrowed attention and selective "
        "memory made verbal - the mind, locked on threat, retrieves only "
        "confirming instances. The second-person pronoun is the agency "
        "appraisal with a target painted on it. Rising pitch and clipped "
        "consonants are the aroused vocal apparatus - tightened muscles "
        "act on the voice box the way they act on the jaw. The kitchen-"
        "sink slide is rumination entering the conversation: every past "
        "grievance the mind rehearsed now demands its hearing. The cold "
        "variant - slow, quiet, precise - is anger under heavy voluntary "
        "control, the heat forced through a narrow channel, which "
        "observers often find more alarming than shouting because the "
        "containment itself signals magnitude. Knowing the machinery "
        "behind the dialect gives both the speaker and the listener "
        "levers: the speaker can deliberately reinsert 'I' and the "
        "present issue; the listener can translate 'you always' back "
        "into 'this feels like a pattern to them.'"),
    key_points=[
        "Phrases: absolutes, accusations, weaponized questions; pronoun shifts to 'you.'",
        "Tone: pitch up, volume up, clipped consonants - or the icy slow quiet variant.",
        "Patterns: short sentences, interruptions, kitchen-sink slide into history.",
        "The dialect is appraisal speaking aloud: absolutes are narrowed memory made verbal.",
        "Hearing it as data ('this feels like a pattern to them') is the listener's first skill.",
    ],
    requirements=[
        "Characteristic phrases quoted",
        "Tone and pace changes described, including the cold variant",
        "The kitchen-sink pattern named",
        "Appraisal-to-dialect mapping for each feature",
    ],
    standards=["Scherer on vocal expression of emotion; Averill on anger discourse"],
    citations=[CIT_SCHERER, CIT_AVERILL],
    sig_lens=(
        "The Signature lens hears the anger dialect as the forge's own "
        "language: the clang of absolutes, the hiss of the cold "
        "variant, the bellows-roar of rising pitch. His method teaches "
        "the smith to translate clang back into meaning - 'you always' "
        "is the apprentice crying 'the pattern burns me' - and to speak "
        "the forge language deliberately rather than letting the fire "
        "shout through him. The master chooses his words the way he "
        "chooses his hammer: weight matched to the work. Clearly "
        "labeled Signature-made, never presented as authentic public "
        "record."),
),
dict(
    key="anger_decisions_judgment", name="How Anger Changes Decisions and Judgment",
    group="Advanced", ladder_rank=10, ladder_tier="advanced",
    description=(
        "Anger does not just feel strong - it thinks differently, and "
        "the differences are measurable. The angry decision-maker feels "
        "certain: anger carries an appraisal of certainty and control "
        "that makes options look clearer than they are. Risk looks "
        "smaller - studies find angry people choose riskier gambles and "
        "judge dangers as less likely, the opposite of fear's effect. "
        "Blame looks simpler: complex causes collapse into a single "
        "villain, and punishment feels more deserved. Stereotypes get "
        "stronger: under anger, people lean harder on group-based "
        "judgments and notice less individuating detail. Optimism "
        "inflates oddly - the angry person overestimates their own "
        "chances, which is why angry negotiations produce bold demands "
        "and angry driving produces close calls. None of this is "
        "stupidity; it is the approach system doing its job - certainty, "
        "simplified blame, and discounted risk are exactly the settings "
        "for charging an obstacle. The problem is only the mismatch: "
        "those settings misfire on decisions that need caution, nuance, "
        "and other minds. The practical rule researchers suggest is "
        "procedural, not heroic: never finalize an important decision at "
        "peak anger; write the angry decision down, sleep on it, and "
        "re-read it at baseline. The paper does not get angry; the "
        "re-reader does the deciding."),
    how_it_works=(
        "The mechanism is appraisal tendency: each emotion carries its "
        "appraisal settings into unrelated judgments. Anger's settings "
        "are high certainty, high control, and other-person blame - so "
        "the angry mind applies certainty to uncertain gambles, control "
        "to uncontrollable outcomes, and blame to ambiguous events. "
        "Lerner and Tiedens documented the full portrait: anger "
        "increases heuristic processing (mental shortcuts), reduces "
        "depth of thought about the other side, and inflates optimistic "
        "risk estimates. The effect persists after the feeling fades - "
        "the 'carryover' finding - because the appraisal settings linger "
        "like an aftertaste. This is why the procedural rule works: "
        "writing the decision down externalizes it, and re-reading at "
        "baseline re-runs the appraisal with normal settings. The "
        "record's lesson is not 'never decide while angry' - sometimes "
        "the obstacle genuinely needs charging - but 'never finalize "
        "while peaked,' with the paper as the honest broker between the "
        "two states."),
    key_points=[
        "Anger inflates certainty, discounts risk, simplifies blame, and strengthens stereotypes.",
        "The settings suit charging obstacles - and misfire on decisions needing caution and nuance.",
        "Appraisal tendencies carry over: the effect lingers after the feeling fades.",
        "Procedural rule: write the decision at peak, finalize it at baseline.",
        "The paper is the honest broker between the angry self and the deciding self.",
    ],
    requirements=[
        "Five judgment effects with the research behind each",
        "Appraisal-tendency mechanism in plain words",
        "The carryover finding stated",
        "The write-then-reread procedure",
    ],
    standards=["Lerner and Tiedens 2006 appraisal-tendency framework"],
    citations=[CIT_LERNER, CIT_SCHERER],
    sig_lens=(
        "The Signature lens reads angry judgment as 'striking at white "
        "heat' - the metal looks ready before it is, the smith feels "
        "certain, the blow lands bold and often wrong. His method "
        "imposes the cooling rule for all great decisions: write the "
        "strike-plan while hot, execute it when the color is right. The "
        "paper on the bench is the master's second self - unheated, "
        "unhurried, honest. Boldness is a tool for the obstacle; "
        "patience is the tool for the decision. Clearly labeled "
        "Signature-made, never presented as authentic public record."),
),
dict(
    key="anger_escalation", name="Anger Under Rising Intensity: How Actions Escalate",
    group="Advanced", ladder_rank=10, ladder_tier="advanced",
    description=(
        "Escalation follows a ladder of its own, and each rung is a "
        "choice point. Rung one is internal: the feeling builds, the jaw "
        "sets, nothing visible yet - the private moment when naming it "
        "still works easily. Rung two is leakage: the sigh, the clipped "
        "tone, the door closed a little too firmly - signals the people "
        "nearby can read. Rung three is verbal engagement: the sharp "
        "remark, the raised voice, the argument joined - the point where "
        "the other person's response starts shaping what happens next. "
        "Rung four is entrenchment: positions harden, the kitchen sink "
        "opens, winning replaces solving - and each side's escalation "
        "becomes the other's trigger, the classic conflict spiral. Rung "
        "five is the threshold of harm: threats, thrown objects, physical "
        "intimidation - the rare end of the ladder, and the point where "
        "the only correct move is disengagement and, if needed, help from "
        "others. The vital fact about the ladder is that descending is "
        "always possible and always cheaper the earlier it happens: a "
        "pause at rung two costs a breath, a repair at rung three costs "
        "an apology, de-escalation at rung four costs pride, and rung "
        "five costs far more. Every rung has its exit - naming, pausing, "
        "softening the voice, taking space, repairing - and the "
        "healthy-expression records are essentially a catalog of exits, "
        "organized by rung."),
    how_it_works=(
        "Escalation is driven by reciprocal appraisal: each person's "
        "angry behavior becomes the other person's trigger, so the "
        "system has positive feedback built in. Arousal adds its own "
        "ratchet - each rung raises physiological activation, which "
        "narrows the next appraisal, which justifies the next rung. "
        "Audience effects stiffen rung four: with witnesses, backing "
        "down feels like losing status, so pride welds the positions in "
        "place. The exits work by breaking the specific mechanism of "
        "their rung: naming breaks the internal pressure buildup, "
        "pausing breaks the arousal ratchet, softening the voice breaks "
        "the reciprocal trigger (a calm voice is hard to stay angry at), "
        "taking space breaks the feedback loop physically, and repair "
        "rewrites the other person's appraisal from 'enemy' to 'partner "
        "having a bad moment.' The ladder model is used in conflict "
        "training precisely because it replaces the vague advice 'calm "
        "down' with rung-specific exits - the right tool for the height."),
    key_points=[
        "Five rungs: internal buildup, leakage, verbal engagement, entrenchment, threshold of harm.",
        "Reciprocal appraisal builds positive feedback in: each side's anger triggers the other's.",
        "Descending is always possible and always cheaper the earlier it happens.",
        "Each rung has its exit: naming, pausing, softening, taking space, repairing.",
        "At the threshold of harm the only correct move is disengagement and help if needed.",
    ],
    requirements=[
        "Five rungs with visible markers for each",
        "Three escalation mechanisms: reciprocity, arousal ratchet, audience pride",
        "Rung-matched exits",
        "Clear safety line at rung five",
    ],
    standards=["Conflict-escalation models; Averill on anger sequences"],
    citations=[CIT_AVERILL, CIT_GROSS],
    sig_lens=(
        "The Signature lens reads escalation as heat climbing a "
        "ladder the smith built himself, rung by rung - and every rung "
        "has a way down, because the smith built those too. His method "
        "drills the exits until they are reflexes: name it at the "
        "first rung, breathe at the second, soften at the third, step "
        "back at the fourth, leave at the fifth. Pride is the rung "
        "greased with oil - the master knows the shine is a trap. The "
        "strongest smith is the one who climbs down early. Clearly "
        "labeled Signature-made, never presented as authentic public "
        "record."),
),
# ---------------------------------------------------------------- 26-28: healthy expression
dict(
    key="anger_healthy_expression", name="Healthy Expression: Saying It, Showing It, and Channeling It Well",
    group="Advanced", ladder_rank=10, ladder_tier="advanced",
    description=(
        "Healthy expression of anger is a skill with three branches: "
        "saying it, showing it, and channeling it. Saying it means the "
        "clear sentence, spoken early and at moderate volume: what "
        "happened, how it landed, and what is needed - 'when the "
        "deadline moved without telling me, I felt blindsided, and I "
        "need a heads-up next time.' The formula works because it keeps "
        "the appraisal (what happened), the feeling (how it landed), "
        "and the request (what is needed) all on the table, giving the "
        "other person something to actually do. Showing it means letting "
        "the feeling be visible without weaponizing it: the serious "
        "face, the firm tone, the direct gaze - honesty about the "
        "feeling, aimed at solving rather than wounding. People can "
        "tell the difference between anger that wants repair and anger "
        "that wants pain, and they respond to the two very differently. "
        "Channeling it means giving the mobilized energy its proper "
        "work: the hard conversation held, the unfair policy challenged, "
        "the run run, the letter written, the boundary set and kept. "
        "Anger channeled well has built movements, ended abuses, and "
        "fixed systems - the feeling is fuel, and fuel is neutral until "
        "it is burned toward something. The thread through all three "
        "branches is timing: early beats late, moderate beats peak, and "
        "the body settled beats the body flooded. Expression is not the "
        "opposite of control; done well, it IS control - the feeling "
        "doing its job instead of doing damage."),
    how_it_works=(
        "Each branch works through a documented mechanism. The clear "
        "sentence works because 'I' statements plus specific behavior "
        "plus concrete request bypass the other person's defensiveness - "
        "there is no absolute to argue with and no character attack to "
        "defend against, only a solvable problem. Showing without "
        "weaponizing works through signal honesty: displayed emotion "
        "that matches the words builds trust, while performed or "
        "suppressed emotion breeds suspicion. Channeling works through "
        "the approach system itself: anger's energy is designed to move "
        "toward obstacles, so aiming it at the actual obstacle - the "
        "policy, the problem, the workout - satisfies the urge instead "
        "of fighting it. Timing matters because of the intensity curve: "
        "early expression meets a flexible listener and a manageable "
        "feeling, while delayed expression meets a surprised listener "
        "and a fermented feeling. The research consensus is steady: "
        "assertive expression predicts better outcomes than suppression "
        "or aggression across relationships, workplaces, and health "
        "measures."),
    key_points=[
        "Say it: the clear sentence - what happened, how it landed, what is needed.",
        "Show it: visible feeling aimed at repair, never weaponized; people can tell the difference.",
        "Channel it: aim the mobilized energy at the actual obstacle - the problem, the policy, the workout.",
        "Timing: early beats late, moderate beats peak, settled body beats flooded body.",
        "Expression done well IS control: the feeling doing its job instead of doing damage.",
    ],
    requirements=[
        "Three branches with concrete how-to for each",
        "The clear-sentence formula with an example",
        "The mechanism behind each branch",
        "Timing principle stated",
    ],
    standards=["Assertiveness research; Gross on antecedent-focused regulation"],
    citations=[CIT_GROSS, CIT_AVERILL],
    sig_lens=(
        "The Signature lens names healthy expression 'the master's "
        "three strikes': the measured blow of the clear sentence, the "
        "true temper of honest showing, and the long forging of "
        "channeling heat into work that outlasts the day. His method "
        "holds that a smith is known by what his fire builds: "
        "movements, mended systems, kept boundaries, finished work. "
        "The fire that only scorches is an apprentice's fire; the fire "
        "that forges is a master's. Strike early, strike true, strike "
        "at the real metal. Clearly labeled Signature-made, never "
        "presented as authentic public record."),
),
dict(
    key="anger_unhealthy_expression", name="Unhealthy Expression: Bottling It Up or Exploding - What Each Costs",
    group="Advanced", ladder_rank=10, ladder_tier="advanced",
    description=(
        "Anger mishandled tends toward two opposite failures, and both "
        "are expensive. Bottling it up - suppression - looks calm from "
        "the outside while the inside keeps the full pressure. The costs "
        "accumulate quietly: the body stays mobilized with nowhere to "
        "go, which researchers link to elevated cardiovascular strain "
        "over time; the mind rehearses the grievance, fermenting "
        "irritation into resentment; and the relationship rots from "
        "underneath, because the other person senses the withdrawal "
        "without ever getting the information that would let them fix "
        "it. Then, often, the bottle breaks - months of stored anger "
        "detonating over a trivial trigger, which convinces everyone "
        "involved that the person is unstable rather than unheard. "
        "Exploding - aggression - pays its costs loudly and immediately: "
        "words that cannot be unsaid, the other person's defensiveness "
        "or fear, damaged trust that takes ten repairs to rebuild, and "
        "in the worst cases physical harm and its consequences. The "
        "explosion also trains the brain: each outburst rehearses the "
        "script, making the next one easier and hotter. Both failures "
        "share a root error - treating the feeling and the action as "
        "one thing. The bottler believes feeling anger means acting "
        "angry, so the only safe move is to feel nothing; the exploder "
        "believes the same equation from the other side. The healthy "
        "middle this database teaches - feel it fully, choose the "
        "action deliberately - dissolves the false equation both "
        "failures are built on."),
    how_it_works=(
        "Suppression fails through the ironic process: trying not to "
        "feel or show an emotion keeps attention locked on it, and the "
        "physiological arousal continues unabated beneath the calm "
        "mask - studies show suppressors often have higher arousal than "
        "expressers. The stored grievances undergo memory consolidation, "
        "getting more entrenched and more available with each replay, "
        "which is why bottled anger resurfaces as resentment with "
        "interest. Explosion fails through rehearsal and reciprocity: "
        "each aggressive act strengthens the neural script for the next "
        "one while simultaneously creating real-world retaliation and "
        "fear in others, manufacturing future triggers. Both patterns "
        "are self-reinforcing loops, which is why willpower alone "
        "rarely breaks them - the loop must be replaced with a practiced "
        "alternative, the clear-sentence script or the walk-away script, "
        "rehearsed at low intensity until it can compete with the "
        "default at high intensity. The cost ledger is the motivator; "
        "the replacement script is the mechanism."),
    key_points=[
        "Bottling: hidden pressure, cardiovascular strain, grievance fermentation, relationships rotting underneath.",
        "The bottle breaks over trivia - stored months detonating looks like instability, not unheard pain.",
        "Exploding: unsayable words, damaged trust, rehearsed scripts making the next outburst easier.",
        "Both share the root error: treating feeling and action as one thing.",
        "The fix is replacement, not willpower: practice the clear sentence and the walk-away at low intensity.",
    ],
    requirements=[
        "Both failures with their distinct cost ledgers",
        "The ironic-process mechanism for suppression",
        "The rehearsal mechanism for explosion",
        "The shared root error named",
    ],
    standards=["Gross on suppression costs; Averill on anger and aggression patterns"],
    citations=[CIT_GROSS, CIT_AVERILL],
    sig_lens=(
        "The Signature lens shows the two failures as the apprentice's "
        "twin mistakes: capping the crucible until it bursts, and "
        "spilling the melt across the floor. His method teaches the "
        "third way between the sealed lid and the spill - the ladle: "
        "draw the heat out deliberately, pour it where it belongs, a "
        "measured stream, not a flood and not a bomb. Both failures "
        "waste good metal; the ladle wastes none. The apprentice learns "
        "the ladle by practice at low heat until the hand is steady. "
        "Clearly labeled Signature-made, never presented as authentic "
        "public record."),
),
dict(
    key="anger_everyday_practices", name="Everyday Practices: Small Habits That Keep Anger in Balance",
    group="Advanced", ladder_rank=10, ladder_tier="advanced",
    description=(
        "Anger balance is mostly maintenance, and maintenance is made "
        "of small habits. Sleep comes first: a full night's rest is the "
        "longest fuse there is, because the appraisal system does its "
        "finest work on a restored brain. Regular meals come second - "
        "the threshold check from the surprise-triggers record, made "
        "daily, so hunger never gets to wear anger's clothes. Movement "
        "comes third: the mobilized energy of anger is designed to be "
        "spent physically, and people who move daily give the arousal "
        "system its proper outlet before it overflows. Fourth is the "
        "naming habit: a two-second internal label - 'irritation, low' "
        "or 'anger, moderate, about the deadline' - which researchers "
        "find measurably damps the feeling, because labeling recruits "
        "the thinking brain alongside the alarm. Fifth is the pause "
        "ritual: a personal, pre-chosen move for the hot moment - three "
        "slow breaths, a sip of water, stepping to the window - "
        "installed in calm times so it is available in hot ones. Sixth "
        "is the repair habit: circling back after a sharp moment with a "
        "short, honest acknowledgment, which keeps small ruptures from "
        "becoming stored resentment. Seventh is the wind-down: a daily "
        "practice that discharges residue - writing the unsent letter, "
        "the evening walk, ten minutes of quiet - so the jar starts "
        "each morning empty. None of these is dramatic. Together they "
        "are the difference between a person who is occasionally angry "
        "and a person who is ruled by it."),
    how_it_works=(
        "Each practice targets a specific link in the anger chain. Sleep "
        "and meals lengthen the fuse by keeping baseline arousal low and "
        "the appraisal system well-resourced - the intensity dials from "
        "the volume record, turned down at the source. Movement metabolizes "
        "the mobilized energy the way the system was designed to spend "
        "it, preventing the idling-pressure buildup. Naming works through "
        "affect labeling: putting a word to the feeling engages "
        "prefrontal regions that down-regulate the alarm response - a "
        "small, well-replicated effect. The pause ritual is a pre-"
        "installed script that competes with the default script at the "
        "moment arousal tries to run it - implementation intentions ('if "
        "heat rises, then I breathe') are among the most reliable "
        "behavior-change tools studied. Repair prevents the spillover "
        "link of the cascade record. Wind-down practices block the "
        "rumination that stretches the time course. The set is "
        "deliberately ordinary: anger balance is not a technique applied "
        "in crisis but a lifestyle that makes crises rarer and smaller."),
    key_points=[
        "Sleep: the longest fuse; the appraisal system works best restored.",
        "Meals and movement: keep baseline arousal low and spend mobilized energy properly.",
        "Naming: a two-second label measurably damps the feeling (affect labeling).",
        "Pause ritual: a pre-chosen move, installed calm, available hot.",
        "Repair and wind-down: keep ruptures small and start each morning with an empty jar.",
    ],
    requirements=[
        "Seven practices, each with its mechanism",
        "Framed as maintenance, not crisis technique",
        "General safe everyday guidance only, no clinical prescriptions",
    ],
    standards=["Affect-labeling findings; implementation-intention research via Gross Handbook"],
    citations=[CIT_GROSS, CIT_LAZARUS],
    sig_lens=(
        "The Signature lens keeps the practices as the smith's daily "
        "discipline: bank the coals at night (sleep), stoke on schedule "
        "(meals), swing the hammer daily (movement), read the gauges "
        "aloud (naming), keep the quench bucket at hand (pause ritual), "
        "mend the scorched bench the same day (repair), sweep the shop "
        "at evening (wind-down). His method holds that mastery is not "
        "a single great forging but ten thousand small disciplines - "
        "the shop kept in order, the fire kept in service. Clearly "
        "labeled Signature-made, never presented as authentic public "
        "record."),
),
# ---------------------------------------------------------------- 29-31: recognizing in others
dict(
    key="anger_reading_others", name="Reading Anger in Others: Face, Body, Voice, and Behavior Cues",
    group="Advanced", ladder_rank=10, ladder_tier="advanced",
    description=(
        "Reading anger in another person is a four-channel skill, and "
        "the channels are checked in order of honesty. The face comes "
        "first: the brow furrow, the narrowed stare, the compressed "
        "mouth - and the micro-flickers that precede the social mask. "
        "The body comes second: the squared shoulders, the forward "
        "weight, the chopping gestures, the stillness that is too still "
        "or the pacing that is too fast. The voice comes third: pitch "
        "tightened, consonants clipped, pace accelerated or slowed to "
        "ice - and the too-careful politeness that seasoned listeners "
        "recognize as the final warning before the mask drops. Behavior "
        "comes fourth: the short answers, the interrupted replies, the "
        "topic sliding toward grievance history, the withdrawal that "
        "is not rest but pressure building. The master rule is clusters "
        "over singles: one cue is noise, three cues across two channels "
        "is signal. The second rule is baseline: know how the person "
        "acts at rest, and read the deviation, not the absolute - the "
        "naturally loud friend shouting is less signal than the quiet "
        "colleague going quieter. The third rule is the ethical one, "
        "and it is absolute: reading is for understanding and care, "
        "never for labeling, cornering, or diagnosing a real person. "
        "'You seem tense - is something wrong?' opens a door; 'you're "
        "angry, admit it' slams one."),
    how_it_works=(
        "The four channels differ in controllability, which is why the "
        "order matters. The face's upper region leaks first (hard to "
        "control), the body leaks through gross posture and leakage "
        "movements (partly controllable), the voice leaks through pitch "
        "and tension (arousal-driven), and behavior is the most "
        "controllable - and therefore the most ambiguous - channel. "
        "Checking them in honesty order weights the evidence correctly. "
        "The cluster rule follows signal-detection logic: any single "
        "cue has many innocent causes (a furrowed brow can be "
        "concentration), but independent cues converging raise the "
        "probability sharply. The baseline rule corrects for individual "
        "differences documented in the body-differences record - the "
        "quiet person's anger looks nothing like the expressive "
        "person's. Together the three rules turn casual observation "
        "into a disciplined skill: check channels in order, require "
        "clusters, compare against baseline, and use everything learned "
        "only for care."),
    key_points=[
        "Four channels in honesty order: face, body, voice, behavior.",
        "Clusters over singles: three cues across two channels is signal; one cue is noise.",
        "Baseline rule: read the deviation from the person's rest state, not the absolute.",
        "Reading is for understanding and care - never for labeling or cornering anyone.",
        "'You seem tense - is something wrong?' opens a door; accusation slams it.",
    ],
    requirements=[
        "Four channels with concrete cues each",
        "Three rules: clusters, baseline, ethics",
        "The honesty-order rationale",
    ],
    standards=["Ekman on leakage hierarchy; Scherer on vocal cues"],
    citations=[CIT_EKMAN, CIT_SCHERER],
    sig_lens=(
        "The Signature lens teaches reading others as reading a "
        "fellow smith's forge from the doorway: the color of the heat, "
        "the set of the shoulders, the ring of the hammer - information "
        "for offering help, never for judgment. His method binds the "
        "skill with an oath: what the eye learns at another's forge "
        "is used to steady, never to shame. The master reads heat to "
        "know when to bring water, not to declare the fire wrong. "
        "Clearly labeled Signature-made, never presented as authentic "
        "public record."),
),
dict(
    key="anger_supportive_responses", name="What to Say and Do When Someone Near You Is Angry",
    group="Advanced", ladder_rank=10, ladder_tier="advanced",
    description=(
        "When someone near you is angry, your behavior is part of their "
        "trigger system - the reciprocal loop from the escalation record "
        "runs through you. What works is a short, learnable set. First, "
        "regulate yourself: slow your own breath, drop your shoulders, "
        "keep your voice low and unhurried - a calm nervous system is "
        "contagious in the useful direction. Second, acknowledge without "
        "agreeing: 'I can see this really matters to you' validates the "
        "feeling without conceding the facts, which lowers defensiveness "
        "on both sides. Third, listen past the dialect: translate 'you "
        "always' into 'this feels like a pattern to them' and respond to "
        "the hurt underneath the heat. Fourth, ask what is needed: 'what "
        "would help right now?' turns the approach energy toward solving. "
        "Fifth, offer space without abandonment: 'I'm here - want a few "
        "minutes, or want to talk it through?' respects the flooded "
        "body's need for time. What to do physically matters too: give "
        "room, keep your posture open, avoid crowding or towering, and "
        "never match the volume - volume-matching is the fastest way to "
        "climb the escalation ladder together. If the anger turns "
        "threatening, the script changes entirely: disengage, leave, and "
        "get help - no conversation is worth anyone's safety. The "
        "through-line: you cannot regulate another person, but you can "
        "refuse to be their next trigger, and that refusal is often "
        "enough."),
    how_it_works=(
        "Each move targets the reciprocal loop. Self-regulation first "
        "because emotional contagion is real - an agitated listener "
        "raises the speaker's arousal through voice, face, and posture "
        "cues, while a settled listener damps it. Acknowledgment without "
        "agreement works on the appraisal: feeling heard reduces the "
        "'nobody understands' amplifier that escalates many conflicts. "
        "Listening past the dialect prevents the listener's own "
        "defensive anger - the most common way helpers become second "
        "combatants. Asking what is needed redirects the approach urge "
        "toward the actual obstacle instead of toward the helper. "
        "Offered space respects the intensity curve: the flooded body "
        "cannot process words well, and time is the cheapest "
        "de-escalator available. The safety exception exists because "
        "threat changes the situation from emotional to physical - "
        "different domain, different rules, no negotiation. The set is "
        "small on purpose: in a hot moment nobody executes a twelve-"
        "step plan, but most people can breathe, acknowledge, and ask."),
    key_points=[
        "Regulate yourself first: a calm nervous system is contagious in the useful direction.",
        "Acknowledge without agreeing: 'I can see this really matters to you.'",
        "Listen past the dialect: respond to the hurt underneath the heat.",
        "Ask what is needed; offer space without abandonment.",
        "Never match the volume; if it turns threatening, disengage and get help.",
    ],
    requirements=[
        "Five supportive moves with exact example phrasing",
        "Physical positioning guidance",
        "The safety exception stated plainly",
        "Mechanism for each move",
    ],
    standards=["Conflict de-escalation practice; Gross on interpersonal regulation"],
    citations=[CIT_GROSS, CIT_AVERILL],
    sig_lens=(
        "The Signature lens frames the helper as the water-bearer at "
        "another's forge: you cannot cool their metal for them, but "
        "you can keep your own hands steady, offer the quench bucket "
        "without tipping it over them, and never throw oil on their "
        "fire to prove a point. His method teaches that the "
        "water-bearer's first duty is to his own steadiness - a "
        "shaking hand spills. And when the fire escapes the forge "
        "entirely, the water-bearer leaves and calls the brigade: no "
        "forge is worth a life. Clearly labeled Signature-made, never "
        "presented as authentic public record."),
),
dict(
    key="anger_mistakes_to_avoid", name="What Not to Do: The Mistakes That Make Anger Worse",
    group="Advanced", ladder_rank=10, ladder_tier="advanced",
    description=(
        "A short catalog of the classic errors, each with what it costs. "
        "Saying 'calm down': it commands the impossible - the aroused "
        "body cannot obey on order - and it signals that the feeling "
        "itself is the problem, which adds insult to injury. Matching "
        "the volume: shouting back feels like standing your ground but "
        "functions as reciprocal triggering, climbing the ladder "
        "together. Correcting the facts mid-flood: the narrowed, certain "
        "mind cannot process counter-evidence at peak, so the correction "
        "registers only as opposition. Bringing up history: the kitchen-"
        "sink move in reverse - it tells the person their current "
        "feeling is really about old business, which is experienced as "
        "dismissal. Laughing it off or minimizing: 'it's not a big deal' "
        "denies the appraisal, and denied appraisals get louder, not "
        "quieter. Threatening consequences to force calm: it adds fear "
        "to anger, producing the volatile blend the mixes record "
        "describes, and it trades the relationship for compliance. "
        "Diagnosing the person - 'you have anger issues,' 'you're "
        "being irrational' - labels the human instead of addressing the "
        "situation, guaranteeing defensiveness. Walking away with a "
        "slammed door and no words: space helps, but unexplained "
        "disappearance reads as abandonment or contempt. Each mistake "
        "shares a structure: it fights the feeling instead of working "
        "with the person. The corrective is equally simple in "
        "structure: address the person, respect the feeling, and pick "
        "the timing the intensity allows."),
    how_it_works=(
        "Every mistake on the list fails through the same three "
        "mechanisms. First, invalidation: telling an aroused person "
        "their feeling is wrong, excessive, or laughable attacks the "
        "appraisal, and attacked appraisals defend themselves by "
        "intensifying - the feeling gets louder to be heard. Second, "
        "reciprocal triggering: matching volume, correcting mid-flood, "
        "or threatening adds new triggers to a system already at "
        "capacity, feeding the escalation loop. Third, timing mismatch: "
        "cognitive interventions (facts, history, labels) are offered "
        "to a brain running on alarm settings, where they cannot land. "
        "The corrective structure - person first, feeling respected, "
        "timing matched - works because it reverses all three: "
        "validation quiets the appraisal defense, non-triggering "
        "responses starve the loop, and waiting for the body to settle "
        "puts the thinking brain back online before asking it to "
        "work. Memorizing the mistake list is less important than "
        "absorbing the structure: never fight the feeling, always work "
        "with the person, and let the intensity set the schedule."),
    key_points=[
        "'Calm down' commands the impossible and insults the injury.",
        "Volume-matching, mid-flood corrections, and threats all feed the reciprocal loop.",
        "Minimizing and diagnosing attack the appraisal - attacked feelings get louder.",
        "Unexplained walkouts read as abandonment; space needs words around it.",
        "The structure: never fight the feeling, work with the person, let intensity set the schedule.",
    ],
    requirements=[
        "Eight mistakes, each with its cost",
        "The three shared failure mechanisms",
        "The corrective structure stated",
    ],
    standards=["Invalidation findings; conflict-escalation research"],
    citations=[CIT_GROSS, CIT_LAZARUS],
    sig_lens=(
        "The Signature lens posts the mistake list on the forge wall "
        "as 'what never to pour on a fire': the oil of 'calm down,' "
        "the bellows of matched shouting, the cold water of mockery "
        "thrown on white-hot metal - which cracks it. His method "
        "teaches apprentices to read the wall before touching "
        "another's heat: the wrong help is worse than no help, and "
        "the right help is simple - tend the smith, respect the "
        "fire, watch the clock. Clearly labeled Signature-made, never "
        "presented as authentic public record."),
),
# ---------------------------------------------------------------- 32-34: related + simulation
dict(
    key="anger_related_emotions", name="The Anger Neighborhood: Nearest Neighbors, Opposites, and Close Cousins",
    group="Advanced", ladder_rank=10, ladder_tier="advanced",
    description=(
        "Anger lives in a crowded neighborhood, and telling the "
        "neighbors apart is a practical skill. Nearest neighbors: "
        "frustration (blocked goal, no agent to blame - the wall "
        "without the warden), irritation (anger's mild shoot), "
        "indignation (anger wearing moral robes), and hostility (anger "
        "as a standing attitude toward someone rather than a reaction "
        "to an event). Close cousins that get confused: envy (wanting "
        "what another has - no violated boundary, just a painful "
        "comparison) versus jealousy (fear of losing what one has to a "
        "rival - anger blended with fear of loss); guilt ('I did wrong' "
        "- the arrow points inward) versus shame ('I am wrong in "
        "others' eyes' - the arrow points outward to the audience); "
        "contempt (anger plus superiority, looking down) versus disgust "
        "(rejection, pushing away). The opposites: calm is not the "
        "opposite of anger but its absence; the true functional "
        "opposites are compassion (suffering-with, which dissolves the "
        "adversarial appraisal) and amusement at the trigger (which "
        "re-appraises the wrong as absurd). The telling-apart tests are "
        "simple questions: is there a blocked goal or a wrong? (anger "
        "versus frustration). Is someone blamed? (anger versus sadness). "
        "Is the heat about loss? (jealousy). About comparison? (envy). "
        "About the self? (guilt, shame). Each answer points to a "
        "different response - which is the whole point of the map: the "
        "right tool for the real feeling."),
    how_it_works=(
        "The neighborhood map is organized by appraisal dimensions: "
        "goal-blockage, agency, fairness, and self-versus-other focus. "
        "Neighbors share most dimensions and differ on one - "
        "frustration and anger share blockage but split on agency; "
        "guilt and shame share self-focus but split on audience. This "
        "is why confusion is so common: the feelings genuinely overlap "
        "in experience, differing only in the appraisal fine print. "
        "Opposites are defined functionally rather than geometrically: "
        "compassion opposes anger because its appraisal (the other's "
        "suffering matters) is incompatible with anger's adversarial "
        "stance - the two cannot fully co-occupy the same moment. The "
        "telling-apart questions work because they query the "
        "dimensions directly, bypassing the noisy surface of arousal "
        "and expression, which neighbors share. For the database's "
        "teaching ladder, this record is the map key: it lets every "
        "earlier record be filed correctly and prevents the most "
        "common emotional mislabeling from sending people to the wrong "
        "tools."),
    key_points=[
        "Neighbors: frustration, irritation, indignation, hostility - each one appraisal-step from anger.",
        "Cousins: envy vs jealousy, guilt vs shame, contempt vs disgust - told apart by simple questions.",
        "Functional opposites: compassion and amusement dissolve the adversarial appraisal.",
        "The telling-apart tests query appraisal dimensions directly: blocked goal or wrong? blamed? loss? self?",
        "Right label, right tool: the map exists to match feelings to responses.",
    ],
    requirements=[
        "Four neighbors, four cousin-pairs, two opposites, each distinguished",
        "The appraisal-dimension organization explained",
        "Telling-apart questions for each confusion",
    ],
    standards=["Plutchik wheel adjacencies; Lazarus appraisal dimensions"],
    citations=[CIT_PLUTCHIK, CIT_LAZARUS],
    sig_lens=(
        "The Signature lens draws the neighborhood as the streets "
        "around the forge: frustration the dead-end alley, indignation "
        "the courthouse steps, hostility the neighbor who never "
        "leaves his porch, envy the house with the bigger chimney, "
        "compassion the well in the square. His method teaches the "
        "smith to know every street by name - because the wrong "
        "street taken in heat leads nowhere good, and the right one "
        "leads home. The map is walked, not memorized. Clearly "
        "labeled Signature-made, never presented as authentic public "
        "record."),
),
dict(
    key="anger_emotion_mixes", name="Anger Blends: Mixes With Four Partner Emotions",
    group="Advanced", ladder_rank=10, ladder_tier="advanced",
    description=(
        "Pure anger is rarer than the blends, and the blends have "
        "their own names and natures. Anger plus fear makes the "
        "volatile mix: the cornered feeling - lashing out while wanting "
        "to flee, unpredictable because two action systems pull "
        "opposite ways. It feels like heat over ice, and it is the "
        "blend most likely to surprise everyone involved. Anger plus "
        "sadness makes the heavy mix: the aggrieved feeling - wronged "
        "and wounded together, often showing as bitter tears or the "
        "quiet, cutting remark. The sadness slows the anger's charge "
        "and deepens its memory; this blend stores the longest. Anger "
        "plus disgust makes contempt: the cold mix - looking down while "
        "pushing away, the sneer, the dismissal. Contempt is anger that "
        "has decided the other is beneath engagement, and researchers "
        "flag it as the most corrosive blend in close relationships. "
        "Anger plus joy - the righteous mix - makes triumph and "
        "glee at the opponent's defeat: the heat of battle plus the "
        "lift of winning, felt by fans, partisans, and anyone who has "
        "savored a rival's fall. It feels glorious and deserves "
        "caution, because the joy rewards the anger and trains it to "
        "return. Each blend (simulations, describing no real person) "
        "follows the Plutchik-style dyad logic: two primaries, one "
        "compound, with properties neither parent has alone - which is "
        "why blends need their own records instead of being filed "
        "under 'anger.'"),
    how_it_works=(
        "Blends form when two appraisal sets fire together: the mind "
        "registers both a wrong (anger) and a threat (fear), a wrong "
        "and a loss (sadness), a wrong and a revulsion (disgust), or a "
        "wrong righted in one's favor (joy). The compound inherits "
        "features from both parents and generates emergent properties: "
        "the volatile mix inherits anger's approach and fear's "
        "avoidance, producing the oscillation neither parent shows; "
        "contempt inherits anger's blame and disgust's rejection, "
        "producing the permanent dismissal neither parent sustains. "
        "The blends also differ in action readiness and duration: the "
        "volatile mix is high-energy and short, the heavy mix is "
        "low-energy and long, contempt is low-energy and potentially "
        "permanent, the righteous mix is high-energy and self-"
        "rewarding. Recognizing which blend is present changes the "
        "response entirely - the volatile mix needs safety and space "
        "first, the heavy mix needs the wound acknowledged, contempt "
        "needs the superiority appraisal dismantled, and the righteous "
        "mix needs the victory decoupled from the cruelty."),
    key_points=[
        "Anger + fear = the volatile mix: cornered, oscillating, needs safety and space first.",
        "Anger + sadness = the heavy mix: aggrieved, bitter, stores the longest, needs the wound acknowledged.",
        "Anger + disgust = contempt: cold dismissal, the most corrosive blend in close relationships.",
        "Anger + joy = the righteous mix: triumph at a rival's fall; the joy rewards the anger.",
        "Blends have emergent properties neither parent has - they need their own records and responses.",
    ],
    requirements=[
        "Four blends with names, feels, and looks",
        "Dyad logic: two primaries, emergent properties",
        "Matched response for each blend",
    ],
    standards=["Plutchik dyad theory; contempt findings in relationship research"],
    citations=[CIT_PLUTCHIK, CIT_EKMAN],
    sig_lens=(
        "The Signature lens reads the blends as alloy steels: anger "
        "the iron, each partner a different alloying metal - fear the "
        "volatile flux, sadness the deep carbon, disgust the cold "
        "nickel, joy the bright chromium. His method teaches that "
        "alloys are not impurities but materials with their own "
        "temperatures and tempers: the smith who mistakes an alloy "
        "for plain iron ruins the work. Know the alloy, set the heat "
        "accordingly, forge what the metal actually is. Clearly "
        "labeled Signature-made, never presented as authentic public "
        "record."),
),
dict(
    key="anger_full_simulation", name="Full Behavioral Simulation: One Anger From Trigger to Resolution",
    group="Advanced", ladder_rank=10, ladder_tier="advanced",
    description=(
        "The archive's showcase simulation: one anger walked from "
        "trigger through peak to resolution, scene by scene - "
        "describing no real person. Scene one, the trigger (9:14 AM): "
        "Mara learns her project proposal was presented by her "
        "manager as his own in the leadership meeting. Appraisal: "
        "unfairness plus clear agency. Her inner monologue: 'He "
        "smiled while he did it.' Body: jaw sets, heat rises up the "
        "neck, hands grip the chair arms. Face: the brow furrow "
        "flickers before she smooths it. Intensity: moderate, rising. "
        "Scene two, the escalation window (9:15-9:40): back at her "
        "desk, the replay starts - each retelling of the meeting to "
        "herself adds a past slight to the witness stand. Her "
        "breathing shallows; she catches it and names it silently: "
        "'anger, moderate, about the credit.' The naming steadies her "
        "enough to choose: not the hallway confrontation (peak is "
        "coming), but a note - facts, dates, the slide numbers - "
        "written while hot, to be sent when cool. Scene three, the "
        "peak (11:05): passing his office, she hears him telling the "
        "story again, with a laugh. The jar overflows: heat floods, "
        "vision tunnels, words stack behind her teeth. She uses the "
        "pause ritual - three breaths, water, the window - and walks "
        "past. The flood crests without a word spent. Scene four, the "
        "fading (afternoon): arousal decays; she re-reads the morning "
        "note at baseline, edits out two hot sentences, and sends the "
        "clear version requesting a private meeting. Scene five, the "
        "resolution (next day): the meeting. Clear sentence: 'When "
        "my proposal was presented as yours, I felt undermined, and I "
        "need us to fix how credit works.' He deflects, then - faced "
        "with dates, not heat - corrects the record in writing. "
        "Scene six, the aftershock (one week later): hearing his laugh "
        "in the hallway, the echo fires - smaller, sharper. She "
        "labels it 'replay,' lets it pass, and notices the victory: "
        "the feeling visited, and she chose everything it did. The "
        "simulation demonstrates the whole database in motion: "
        "appraisal, volume, time course, body signals, the face, "
        "triggers, behavior choices, healthy expression, and the "
        "aftershock met with skill."),
    how_it_works=(
        "The simulation is constructed as a teaching machine: each "
        "scene exercises specific records. Scene one runs the "
        "definition record (appraisal: unfairness plus agency) and the "
        "face record (the pre-mask flicker). Scene two runs the time-"
        "course record (the replay re-striking the bell) and the "
        "everyday-practices record (naming as regulation, writing hot "
        "to send cool). Scene three runs the volume record (the jar "
        "overflowing into flood) and the escalation record (the rung-"
        "two exit: pause ritual, walk past). Scene four runs the "
        "decisions record (re-reading at baseline) and the healthy-"
        "expression record (the edited clear sentence). Scene five "
        "runs the supportive-communication pattern from the other "
        "side - the clear sentence meeting defensiveness with facts. "
        "Scene six runs the aftershock and the relabeling skill. The "
        "character is fictional, the mechanisms are documented, and "
        "the through-line is the database's central thesis: the "
        "feeling is given, every action is chosen, and skill is the "
        "space between them made wide through practice."),
    key_points=[
        "Six scenes: trigger, escalation window, peak, fading, resolution, aftershock.",
        "Each scene exercises specific earlier records - the database in motion.",
        "The peak is survived by ritual, not willpower: three breaths, water, the window, walk past.",
        "Resolution comes from the edited clear sentence: facts at baseline, not heat at peak.",
        "The thesis: the feeling is given, every action is chosen, skill widens the space between.",
    ],
    requirements=[
        "Six scenes with times, inner monologue, body, face, and behavior",
        "Each scene mapped to the records it demonstrates",
        "Fictional character, documented mechanisms",
    ],
    standards=["Full-ladder synthesis; Averill episode structure"],
    citations=[CIT_AVERILL, CIT_GROSS, CIT_LAZARUS],
    sig_lens=(
        "The Signature lens reads Mara's day as the masterwork piece: "
        "the apprentice's journeyman trial at the forge, one full heat "
        "from ore to finished blade. His method grades the work not by "
        "the absence of fire - the fire came, as fire does - but by "
        "every choice made inside it: the naming, the note written hot "
        "and sent cool, the walked-past peak, the clear sentence, the "
        "labeled aftershock. This is the Signature ideal rendered as a "
        "life: heat in service, never in command. Clearly labeled "
        "Signature-made, never presented as authentic public record."),
),
]

assert len(ENTRIES) == 34, "expected 34 entries, got %d" % len(ENTRIES)
_ranks = [e["ladder_rank"] for e in ENTRIES]
assert _ranks == sorted(_ranks), "ladder ranks not non-decreasing"
assert all(1 <= r <= 10 for r in _ranks)
assert all(e["ladder_tier"] in ("foundations", "compounded", "advanced") for e in ENTRIES)
for e in ENTRIES:
    for k in ("key", "name", "group", "ladder_rank", "ladder_tier",
              "description", "how_it_works", "key_points", "requirements",
              "standards", "citations", "sig_lens"):
        assert k in e, "missing %s" % k
    assert len(e["description"]) > 200, "stub description in %s" % e["key"]
    assert len(e["key_points"]) >= 4, "thin key_points in %s" % e["key"]
    blob = (e["description"] + e["how_it_works"] + e["sig_lens"]).lower()
    assert "facebook" not in blob and "bat belt" not in blob
