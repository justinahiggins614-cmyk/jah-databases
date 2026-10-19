#!/usr/bin/env python3
"""Entries for the Jealousy Emotion databases (Manon's 2026-10-17 16:15 order,
emotion series).

Descriptive and educational ONLY - the database describes and simulates
jealousy; it never diagnoses real people, never labels any real person with
an emotional state, and never offers therapeutic advice beyond general, safe,
everyday guidance. No clinical language, no diagnostic labels. Healthy
expression records emphasize constructive handling.

34 records, ordered by the teaching ladder (ladder_rank 1-34,
non-decreasing; tiers foundations 1-9 / compounded 10-21 / advanced 22-34),
following the shared emotion-template spec: what jealousy IS ->
first-person simulation -> body signals -> facial expression -> triggers ->
behavior -> healthy expression -> recognizing it in others -> related
emotions and mixes -> complex behavioral simulation.

ID prefixes: JAH-EMJE- (public) and JAH-EMJES- (signature), verified free
in the manifest id_prefix values and in all jah-databases-data-1 shard
index files (zero 'JAH-EMJE' substring hits), 2026-10-17.

Public records are real, fact-checked psychology knowledge (Buss, White and
Mullen, Salovey, Pines, Ekman, Plutchik, Lazarus, Gross, Scherer, Izard,
Schachter and Singer, APA Dictionary). Signature editions are his original
Signature lens - jealousy as the soul's sentinel at the gate of what is
loved, value honored through watchfulness and trust-building, never
presented as authentic public record.

Never the words "bat belt" anywhere. No website references. No Facebook.
No religious talk. Nothing hate-adjacent, profane, or inappropriate.
"""

SIG_TAIL = ("Signature original - his original Signature lens: jealousy as the "
            "soul's sentinel at the gate of what is loved; the guardian alarm "
            "that fires when a valued bond feels threatened. Signature editions "
            "frame every facet as value, watchfulness, and trust-building - "
            "never as a diagnosis, never labeling any real person, and never "
            "presented as authentic public record.")

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
CIT_SCHACHTER = ("Schachter S, Singer JE. Cognitive, social, and "
                 "physiological determinants of emotional state. "
                 "Psychological Review. 1962;69(5):379-399.")
CIT_APA = ("American Psychological Association. APA Dictionary of "
           "Psychology; current edition.")
CIT_BUSS = ("Buss DM. The Dangerous Passion: Why Jealousy Is As Necessary "
            "As Love and Sex. Free Press; 2000.")
CIT_WHITE = ("White GL, Mullen PE. Jealousy: Theory, Research, and Clinical "
             "Strategies. Guilford; 1989.")
CIT_SALOVEY = ("Salovey P, editor. The Psychology of Jealousy and Envy. "
               "Guilford; 1991.")
CIT_PINES = ("Pines AM. Romantic Jealousy: Causes, Symptoms, Cures. "
             "Routledge; 1998.")

ENTRIES = [
# ---------------------------------------------------------------- 1-4: what jealousy IS
dict(
    key="jealousy_definition", name="What Jealousy Is: A Plain-Language Definition",
    group="Foundations", ladder_rank=1, ladder_tier="foundations",
    description=(
        "Jealousy is the emotion you feel when something you value - a "
        "relationship, a place in someone's heart, a position that matters "
        "to you - feels threatened by a rival. In everyday words: jealousy "
        "is the mind's guardian alarm for a valued bond. Psychologists "
        "describe it as a complex emotion, built from simpler feelings - "
        "fear of loss, anger at the unfairness, sadness at the imagined "
        "outcome - fused into one experience. It is not the same as envy: "
        "envy wants what someone else has, while jealousy fears losing what "
        "it already holds to someone else. That three-cornered shape - the "
        "person, the valued bond, and the rival - is jealousy's defining "
        "geometry. The alarm can be a quiet twinge when a friend laughs "
        "with a newcomer, or a storm when a partner seems to drift toward "
        "someone else; the family name is the same because the signal is "
        "the same: something treasured may be slipping, and attention is "
        "demanded. Jealousy is information, not a verdict. What matters is "
        "what a person does with the signal."),
    how_it_works=(
        "The jealousy sequence runs in five beats: value, threat, "
        "appraisal, alarm, and urge. First there is something valued - a "
        "relationship, a friendship, a role - that the person cares about "
        "keeping. Second comes a perceived threat: a rival's attention, a "
        "changed routine, an ambiguous message. Third, the mind appraises "
        "the threat - how real is it, how much does this bond matter, what "
        "would losing it cost - which is why the same event alarms one "
        "person and barely registers with another. Fourth, the alarm fires: "
        "the body tightens, attention narrows onto the rival, the mind "
        "starts scanning for evidence. Fifth comes the urge: to check, to "
        "question, to cling, to compete, or to withdraw before being hurt. "
        "Understanding this chain is the key to everything else in this "
        "database: change the appraisal, and the alarm shifts; soothe the "
        "body, and the urge eases; check the evidence, and imagined threats "
        "shrink."),
    key_points=[
        "Jealousy is a complex emotion with a three-cornered shape: the person, the valued bond, and the rival.",
        "It differs from envy: envy wants what another has; jealousy fears losing what it holds to another.",
        "The core signal is: something valued feels threatened, and the mind demands attention.",
        "The sequence is value -> threat -> appraisal -> alarm -> urge; each step is a place the feeling can be worked with.",
        "The feeling itself is information, not a verdict; what matters is what follows.",
    ],
    requirements=[
        "Everyday definition a student or writer can quote",
        "Clear contrast between jealousy and envy",
        "The five-beat sequence stated in plain words",
        "No diagnostic language anywhere in the record",
    ],
    standards=["APA Dictionary of Psychology definition of jealousy and envy"],
    citations=[CIT_APA, CIT_SALOVEY, CIT_BUSS],
    sig_lens=(
        "The Signature lens reads jealousy as the sentinel at the gate of "
        "what is loved: proof that something has value, sounded as an "
        "alarm. Where public psychology names the five-beat sequence, the "
        "Signature method calls it the sentinel's rounds - value named, "
        "threat sighted, alarm weighed, urge aimed. The alarm is never the "
        "enemy; a sentinel that fires at shadows is, and the work is "
        "teaching it to tell shadows from true approach. Clearly labeled "
        "Signature-made, never presented as authentic public record."),
),
dict(
    key="jealousy_emotion_family", name="Jealousy in the Emotion Family: A Complex Emotion's Roots",
    group="Foundations", ladder_rank=2, ladder_tier="foundations",
    description=(
        "Jealousy sits among the complex emotions - feelings assembled from "
        "simpler ones rather than arriving as a single basic note. Most "
        "emotion researchers place fear at its core: the fear of losing "
        "something treasured. Around that core gather anger at the "
        "perceived unfairness, sadness at the imagined loss, and the love "
        "or attachment that made the bond worth guarding in the first "
        "place. Remove the love and there is nothing to guard; remove the "
        "fear and there is no alarm. Jealousy is often confused with its "
        "neighbors. Envy looks outward at what another has and wants it; "
        "jealousy looks inward at what it has and fears losing it. "
        "Suspicion is the cold cognitive cousin - the doubt without the "
        "heat. Possessiveness is jealousy hardened into a stance. Seeing "
        "these family lines matters, because each ingredient can be worked "
        "with on its own: calm the fear and the whole blend cools, even if "
        "the anger has not yet been addressed."),
    how_it_works=(
        "Think of jealousy as a recipe with a fixed core and variable "
        "seasoning. The core is always the threatened bond - the valued "
        "relationship or position. Fear of loss is the first and largest "
        "ingredient: threat appraisal research shows that the stronger the "
        "perceived threat to something valued, the stronger the alarm. "
        "Anger is the second ingredient, rising when the threat feels "
        "unfair - when the rival seems undeserving, or the bond feels "
        "betrayed. Sadness is the third, the grief for the loss that has "
        "not happened but is vividly imagined. Love or attachment is the "
        "base note underneath them all: the deeper the attachment, the "
        "louder the alarm. The proportions shift from person to person and "
        "from trigger to trigger, which is why two jealous episodes can "
        "feel like different emotions entirely."),
    key_points=[
        "Jealousy is a complex emotion: fear of loss at its core, blended with anger, sadness, and love.",
        "Envy wants what another has; jealousy guards what it has; suspicion is doubt without the heat.",
        "The deeper the attachment, the louder the alarm - the love is the base note.",
        "Each ingredient can be worked with separately: calm the fear and the blend cools.",
        "Knowing the family lines turns one overwhelming feeling into several manageable parts.",
    ],
    requirements=[
        "Place jealousy correctly among complex emotions",
        "Name the four ingredients with their roles",
        "Distinguish jealousy, envy, suspicion, and possessiveness",
        "No diagnostic language anywhere in the record",
    ],
    standards=["Plutchik's model of complex emotions as blends of primary emotions"],
    citations=[CIT_PLUTCHIK, CIT_LAZARUS, CIT_SALOVEY],
    sig_lens=(
        "The Signature lens reads the family tree as the sentinel's "
        "lineage: fear is the watchman's horn, anger the drawn blade, "
        "sadness the mourning for a loss not yet suffered, and love the "
        "treasure being guarded. His reading treats the ingredients as the "
        "sentinel's tools - each with a proper use and each dangerous when "
        "wielded blind. The mastery is knowing which tool is sounding: "
        "answer the horn with watchfulness, not the blade. Clearly labeled "
        "Signature-made, never presented as authentic public record."),
),
dict(
    key="jealousy_intensity_scale", name="How Strong Jealousy Can Get: Mild, Moderate, and Intense",
    group="Foundations", ladder_rank=3, ladder_tier="foundations",
    description=(
        "The same jealousy plays at three volumes. Mild jealousy is a "
        "twinge: a brief pang when a friend spends the evening with someone "
        "new, gone by morning, often unnoticed by anyone else. It is the "
        "body's way of marking that the bond matters. Moderate jealousy is "
        "a pressure: the pang lingers for hours, thoughts keep returning to "
        "the rival, questions start forming - who was that, how long have "
        "you known them - and the person may act a little colder or a "
        "little clingier than usual. Intense jealousy is a storm: the "
        "threat fills the mind completely, sleep and appetite suffer, "
        "checking and questioning become compulsive, and ordinary events "
        "get read as evidence. The three volumes share one signal - the "
        "valued bond feels threatened - but the stakes feel different "
        "because the appraisal differs: mild jealousy appraises the threat "
        "as small or uncertain, intense jealousy appraises it as large and "
        "nearly certain. Volume is set by three dials: how much the bond "
        "matters, how real the threat seems, and how much load the person "
        "is already carrying."),
    how_it_works=(
        "Intensity is the product of three appraisals multiplied together. "
        "First, bond value: a casual acquaintance's new friend barely "
        "registers, while a life partner's new closeness can shake the "
        "floor. Second, threat certainty: a confirmed betrayal rings far "
        "louder than an ambiguous glance, and ambiguity itself is a dial - "
        "the less certain the facts, the more the imagination fills in, "
        "usually with the worst case. Third, background load: tiredness, "
        "stress, and old wounds turn the volume up, because a depleted mind "
        "appraises everything as more dangerous. When all three dials run "
        "high, mild triggers produce intense storms; when they run low, "
        "even real threats produce manageable pangs. This is why the same "
        "event - a partner laughing with a coworker - is a shrug on a good "
        "day and a crisis on a bad one."),
    key_points=[
        "Mild jealousy is a twinge that marks the bond as valued and passes quickly.",
        "Moderate jealousy is a pressure: lingering thoughts, forming questions, colder or clingier behavior.",
        "Intense jealousy is a storm: the threat fills the mind, sleep and appetite suffer, checking turns compulsive.",
        "Three dials set the volume: bond value, threat certainty, and background load.",
        "The same trigger lands differently on different days because the dials move.",
    ],
    requirements=[
        "Describe all three volumes with lived detail",
        "Name the three intensity dials",
        "Explain why one trigger varies in effect across days",
        "No diagnostic language anywhere in the record",
    ],
    standards=["APA Dictionary of Psychology entries on emotion intensity and appraisal"],
    citations=[CIT_APA, CIT_LAZARUS, CIT_BUSS],
    sig_lens=(
        "The Signature lens reads the three volumes as the sentinel's three "
        "horns: the soft note that marks the treasure, the sustained call "
        "that summons the watch, and the war horn that musters everything "
        "at once. His method treats volume as a report from the three "
        "dials, not a verdict on the facts - a war horn on a shadow day is "
        "information about the watchman, not the gate. Mastery is tuning "
        "the dials before answering the horn. Clearly labeled "
        "Signature-made, never presented as authentic public record."),
),
dict(
    key="jealousy_myths", name="Myths and Misunderstandings About Jealousy",
    group="Foundations", ladder_rank=4, ladder_tier="foundations",
    description=(
        "Jealousy carries more folklore than almost any emotion. The most "
        "famous myth: jealousy is proof of love. It is not. Jealousy is "
        "proof that something is valued and feels threatened - it can guard "
        "love, but it can also guard pride, status, or control, and love "
        "thrives in many people who rarely feel jealous at all. The second "
        "myth: only insecure people feel jealous. In fact, jealousy is "
        "near-universal; what varies is how people handle it, not whether "
        "the alarm exists. The third myth: jealousy and envy are the same "
        "thing - they are not, as this database's second record shows. The "
        "fourth myth: a little jealousy is always healthy, or jealousy is "
        "always toxic. Neither is true on its own: the feeling is a signal, "
        "and signals are judged by what they reveal and what they cause, "
        "not by their volume. The fifth myth: jealousy always means the "
        "threat is real. Ambiguity, tiredness, and old memories can sound "
        "the alarm over nothing. Clearing these myths matters because each "
        "one misdirects the response: chasing proof of love through "
        "jealousy, shaming oneself for feeling it, or trusting every alarm "
        "as fact."),
    how_it_works=(
        "Myths persist because each one contains a half-truth. Jealousy "
        "does travel with love - the bond it guards is often a loving one - "
        "so the myth that it proves love feels true. Insecurity does "
        "amplify jealousy, so the myth that only insecure people feel it "
        "feels true. The correction is always the same move: separate the "
        "signal from the story. The signal is real - the body tightened, "
        "the attention narrowed - but the story the mind tells about the "
        "signal (this proves love, this means I am broken, this means the "
        "threat is real) is interpretation, and interpretations can be "
        "checked. The practical version: treat every jealous episode as a "
        "question, not an answer. What is valued here? What is the actual "
        "evidence? What would I do if the threat were real, and what would "
        "I do if it were imagined?"),
    key_points=[
        "Jealousy is not proof of love; it is proof that something is valued and feels threatened.",
        "Jealousy is near-universal; people differ in how they handle it, not in whether the alarm exists.",
        "Jealousy and envy are different emotions with different shapes.",
        "The feeling is a signal, judged by what it reveals and causes, not by its volume.",
        "Every jealous episode is a question to investigate, not an answer to obey.",
    ],
    requirements=[
        "Refute at least five common myths with corrections",
        "Explain the half-truth that keeps each myth alive",
        "Offer the signal-versus-story correction move",
        "No diagnostic language anywhere in the record",
    ],
    standards=["Public understanding of emotion concepts per APA Dictionary of Psychology"],
    citations=[CIT_APA, CIT_BUSS, CIT_PINES],
    sig_lens=(
        "The Signature lens reads each myth as a cracked lens over the "
        "sentinel's eyes: the proof-of-love myth turns the alarm into a "
        "test the bond must pass; the insecurity myth shames the watchman "
        "for standing his post; the always-real myth arms every shadow. "
        "His method replaces each cracked lens with a clear one - the "
        "alarm reports value under watch, nothing more, nothing less - and "
        "insists the sentinel be thanked for the warning before his report "
        "is questioned. Clearly labeled Signature-made, never presented as "
        "authentic public record."),
),
# ---------------------------------------------------------------- 5-9: how jealousy feels
dict(
    key="jealousy_first_person", name="Inside the Feeling: Jealousy in the First Person",
    group="Foundations", ladder_rank=5, ladder_tier="foundations",
    description=(
        "It starts in the stomach before it reaches the mind. A party, a "
        "laugh across the room - your partner leaning in to hear someone "
        "else over the noise - and something cold drops through you like a "
        "stone in water. Your smile stays on because the room is watching, "
        "but your attention has already left the conversation you were "
        "having and crossed the floor. Every detail sharpens: how long the "
        "laugh lasts, the hand that lands briefly on an arm, the way they "
        "turn toward each other. Inside, the thoughts stack faster than you "
        "can argue with them: who is that, have they met before, why is "
        "she standing so close. Underneath the thoughts runs something "
        "older and wordless, a heat behind the ribs and a hollowing in the "
        "gut, as if your body already knows a verdict your mind is still "
        "debating. You are of two minds at once - the reasonable one "
        "saying it is nothing, a laugh at a party, and the watching one "
        "counting seconds and cataloguing gestures. That split attention "
        "is the signature of jealousy from the inside: half of you still "
        "at the party, half of you already somewhere else, guarding a door."),
    how_it_works=(
        "First-person jealousy is the appraisal machinery running at full "
        "speed while the body sounds its alarm. Attention narrows onto the "
        "rival - researchers call this attentional bias toward threat - so "
        "ordinary moments get examined frame by frame. The mind fills gaps "
        "with worst cases because the alarm system is built to prefer false "
        "alarms over missed threats: better to suspect a rival wrongly "
        "than to lose the bond unguarded. Meanwhile the body runs its own "
        "commentary - gut clench, chest heat, jaw set - which the mind "
        "reads as further evidence that something is wrong, in a loop. The "
        "two-minds feeling comes from two systems reporting at once: the "
        "fast alarm system saying danger, and the slower reasoning system "
        "saying probably nothing. Naming both voices is the first step to "
        "hearing them clearly instead of obeying the louder one."),
    key_points=[
        "Jealousy from the inside begins in the body - gut drop, chest heat - before the mind names it.",
        "Attention narrows onto the rival and examines ordinary moments frame by frame.",
        "The alarm prefers false alarms over missed threats, so the mind fills gaps with worst cases.",
        "Two systems report at once: the fast alarm says danger, the slower reason says probably nothing.",
        "Naming both voices lets a person hear them clearly instead of obeying the louder one.",
    ],
    requirements=[
        "Write the passage in present-tense first person",
        "Show both the bodily and the mental layers",
        "Include the split-attention signature",
        "No diagnostic language anywhere in the record",
    ],
    standards=["First-person phenomenology of emotion per Schachter and Singer two-factor account"],
    citations=[CIT_SCHACHTER, CIT_LAZARUS, CIT_WHITE],
    sig_lens=(
        "The Signature lens reads the first-person storm as the sentinel's "
        "night watch: the gut is the first bell, the narrowed attention "
        "the watchman's lantern sweeping the wall, the racing thoughts the "
        "relief guard being roused. His method honors the watch - the body "
        "stood its post - and then asks the oldest sentinel's question: "
        "what did you actually see, and what did the dark suggest? Clearly "
        "labeled Signature-made, never presented as authentic public record."),
),
dict(
    key="jealousy_time_course", name="How Jealousy Changes Over Time: Onset, Peak, and Fading",
    group="Foundations", ladder_rank=6, ladder_tier="foundations",
    description=(
        "Jealousy has a weather pattern, and knowing it helps a person "
        "wait it out. Onset is fast - often under a minute from trigger to "
        "full alarm: the sight of the rival, the odd text message, the "
        "changed plan. The first minutes are the hottest, when the body is "
        "at full arousal and the mind is generating worst cases at top "
        "speed. The peak usually arrives within the first hour, when "
        "checking and questioning feel most urgent; this is when people do "
        "the things they later regret, because the urge to act is "
        "strongest while the facts are thinnest. Then comes the long "
        "plateau: hours or days of a lower, grinding watchfulness - "
        "replaying the scene, scanning for new evidence, mood darkened, "
        "sleep lighter. Fading begins when the alarm finds no fresh fuel: "
        "a reassuring conversation, an ordinary uneventful day, or simply "
        "exhaustion. The aftershock can linger longest of all - a residue "
        "of wariness that flares at small reminders for weeks. Episodes "
        "rarely end in a single moment; they dissolve in layers, and each "
        "layer is a chance to check the evidence with a cooler head."),
    how_it_works=(
        "The time course follows the body's arousal curve plus the mind's "
        "evidence hunt. Arousal spikes fast and decays slowly - the heart "
        "can calm in twenty minutes while the suspicion runs for days, "
        "because suspicion is cognitive fuel the mind keeps adding. The "
        "peak's urgency is partly chemical: at high arousal, the brain's "
        "impulse control is at its weakest, which is why the worst "
        "decisions cluster in the first hour. The plateau persists because "
        "the mind keeps the case open, treating every new ambiguity as "
        "related evidence - a phenomenon researchers call confirmation "
        "search. Fading requires the case to close: either new evidence "
        "settles it, or the mind accepts uncertainty, or the arousal "
        "simply runs out. The aftershock is memory doing its job: the "
        "alarm system tags the trigger for future reference, which is "
        "useful when the threat was real and noisy when it was not."),
    key_points=[
        "Onset is fast - under a minute from trigger to full alarm - and the first minutes run hottest.",
        "The peak brings the strongest urge to act, when facts are thinnest; the worst decisions cluster here.",
        "The plateau is a long grinding watchfulness of replaying and evidence-scanning.",
        "Fading needs the case to close: new evidence, accepted uncertainty, or spent arousal.",
        "The aftershock - wariness flaring at small reminders - can linger for weeks.",
    ],
    requirements=[
        "Map all five phases: onset, peak, plateau, fading, aftershock",
        "Explain why the worst decisions cluster at the peak",
        "Give the practical value of knowing the weather pattern",
        "No diagnostic language anywhere in the record",
    ],
    standards=["Emotion time-course research per Scherer appraisal and Gross regulation frameworks"],
    citations=[CIT_SCHERER, CIT_GROSS, CIT_WHITE],
    sig_lens=(
        "The Signature lens reads the weather as the sentinel's campaign: "
        "the first alarm, the muster at the gate, the long siege watch, "
        "the standing down, and the veterans' memory that flinches at "
        "drums. His method teaches the watchman his own rhythm - the "
        "storm's first hour is for holding the gate, not for riding out - "
        "and treats the aftershock as an old soldier's scar, honored but "
        "not obeyed. Clearly labeled Signature-made, never presented as "
        "authentic public record."),
),
dict(
    key="jealousy_low_vs_high", name="Jealousy at Low Intensity Versus High Intensity",
    group="Foundations", ladder_rank=7, ladder_tier="foundations",
    description=(
        "Low intensity: It is Tuesday, and your closest friend mentions "
        "she had lunch with someone from her new job - twice this week. A "
        "small tug pulls somewhere behind your ribs. You notice it, you "
        "smile, you ask what the new job is like, and by the time the "
        "coffee arrives you have forgotten the tug entirely. The evening "
        "is normal. The friendship is normal. The tug was just the bond "
        "marking itself as valued, and then the day moved on. High "
        "intensity: It is 2 a.m., and your partner's phone lights up with "
        "a name you have been turning over in your mind for a week. Your "
        "chest goes tight before you are fully awake. You lie there doing "
        "math - who texts at 2 a.m., what did that laugh at dinner really "
        "mean - and every memory of the week rearranges itself into "
        "evidence. You get up, you check, you hate yourself for checking, "
        "you find nothing, and the nothing does not help, because now you "
        "are wondering what was deleted. The morning is ruined, the "
        "questions come out sideways over breakfast, and the whole day "
        "tilts. Same alarm, different volume: at low intensity the "
        "feeling visits and leaves; at high intensity it moves in and "
        "rearranges the furniture."),
    how_it_works=(
        "The two snapshots differ in every dial at once. At low intensity, "
        "bond value is moderate, threat certainty is low, and background "
        "load is light - so the appraisal resolves quickly and the arousal "
        "has nowhere to build. Attention returns to the present within "
        "minutes. At high intensity, the bond is central to the person's "
        "life, the threat feels highly certain (or the ambiguity feels "
        "intolerable), and the background load is heavy - tiredness, "
        "stress, older wounds. Arousal stays high for hours, attention "
        "locks onto the threat, and the mind's evidence hunt manufactures "
        "certainty out of ambiguity. The cruel detail of the high-intensity "
        "snapshot - that finding nothing does not help - is the "
        "confirmation trap: once the alarm is certain, absence of evidence "
        "reads as evidence of concealment. This is why arguing with "
        "high-intensity jealousy using facts alone so often fails; the "
        "facts are being processed by an alarm that has already decided."),
    key_points=[
        "Low-intensity jealousy visits and leaves; high-intensity jealousy moves in and rearranges the day.",
        "The snapshots differ in all three dials at once: bond value, threat certainty, background load.",
        "At high intensity, finding nothing does not help - absence of evidence reads as concealment.",
        "Arguing with high-intensity jealousy using facts alone fails because the alarm has already decided.",
        "Recognizing which snapshot you are in tells you which tools will work.",
    ],
    requirements=[
        "Two concrete lived snapshots, low and high",
        "Show the same alarm at different volumes",
        "Explain the confirmation trap of high intensity",
        "No diagnostic language anywhere in the record",
    ],
    standards=["Appraisal-intensity relationships per Lazarus emotion theory"],
    citations=[CIT_LAZARUS, CIT_BUSS, CIT_PINES],
    sig_lens=(
        "The Signature lens reads the two snapshots as the sentinel on a "
        "quiet day and the sentinel during a siege: the first notes the "
        "stranger, logs him, and returns to his rounds; the second has not "
        "slept, sees armies in dust clouds, and burns the very bridge he "
        "was set to guard. His method asks first which watch you are "
        "standing - the tools of the quiet day cannot hold a siege, and "
        "the tools of the siege will wreck a quiet day. Clearly labeled "
        "Signature-made, never presented as authentic public record."),
),
dict(
    key="jealousy_fear_blend", name="Jealousy Mixed with Fear: The Feeling's Most Common Partner",
    group="Foundations", ladder_rank=8, ladder_tier="foundations",
    description=(
        "Jealousy rarely travels alone, and its most constant companion "
        "is fear - specifically the fear of loss. The blend has its own "
        "texture: jealousy supplies the heat and the focus on the rival, "
        "fear supplies the cold undertow and the vivid preview of life "
        "after the loss. Together they make the feeling both urgent and "
        "dreadful - the person wants to act now and dreads what acting "
        "might confirm. In the body, the blend shows as the classic "
        "jealous tightness in the chest wrapped around a hollow, sinking "
        "stomach. In the mind, it shows as rehearsal: the person plays "
        "out the loss in advance - the empty chair, the unanswered calls, "
        "the rival's face where theirs used to be - and each rehearsal "
        "makes the threat feel more real. The blend is also what makes "
        "jealousy so hard to argue away: fear does not respond to "
        "reassurance the way anger responds to apology, because fear is "
        "about the future, and the future cannot be proven safe. Working "
        "with the blend means addressing the two partners separately: "
        "the jealousy wants evidence and boundaries; the fear wants "
        "safety and steadiness."),
    how_it_works=(
        "Fear and jealousy share the same appraisal root - threat to "
        "something valued - which is why they fuse so readily. Jealousy "
        "adds the rival and the injustice appraisal; fear adds the "
        "anticipation of harm and the urge to protect or flee. The "
        "rehearsal loop is the blend's engine: imagining the loss "
        "activates the same alarm as perceiving it, so each mental "
        "rehearsal re-fires the body. This is why the blend escalates "
        "even in a quiet room with no new information. The two partners "
        "also pull behavior in different directions: jealousy urges "
        "approach - confront, check, compete - while fear urges "
        "protection - cling, withdraw, brace. The person caught between "
        "them may swing wildly between clinging and coldness, which "
        "looks erratic from outside but is perfectly legible once the "
        "blend is named. Separate the partners, and each becomes "
        "workable: evidence for the jealousy, steadiness for the fear."),
    key_points=[
        "Fear of loss is jealousy's most constant companion; the blend is both urgent and dreadful.",
        "Jealousy supplies the heat and the rival-focus; fear supplies the cold undertow and the preview of loss.",
        "Mental rehearsal of the loss re-fires the alarm even with no new information.",
        "The blend pulls behavior two ways: jealousy urges approach, fear urges protection.",
        "Work the partners separately: evidence and boundaries for the jealousy, safety and steadiness for the fear.",
    ],
    requirements=[
        "Describe the blend's distinct texture in body and mind",
        "Explain the rehearsal loop as the escalation engine",
        "Show the two-directional behavioral pull",
        "No diagnostic language anywhere in the record",
    ],
    standards=["Emotion blend dynamics per Plutchik and Lazarus appraisal theory"],
    citations=[CIT_PLUTCHIK, CIT_LAZARUS, CIT_WHITE],
    sig_lens=(
        "The Signature lens reads the blend as the sentinel joined by the "
        "scout who has seen the city fall in a dream: the sentinel watches "
        "the gate, the scout describes the burning streets, and between "
        "them the watch becomes a siege that exists only in the telling. "
        "His method separates the two voices - the sentinel reports what "
        "is seen, the scout reports what is feared - and answers each in "
        "its own tongue: watchfulness for the seen, steadiness for the "
        "feared. Clearly labeled Signature-made, never presented as "
        "authentic public record."),
),
dict(
    key="jealousy_day_in_life", name="A Day in the Life: Jealousy Running Through an Ordinary Day",
    group="Foundations", ladder_rank=9, ladder_tier="foundations",
    description=(
        "Morning: the alarm goes off and the first thought is already "
        "there - the party last night, the laugh, the hand on the arm. "
        "Coffee tastes like nothing. On the commute, the mind replays the "
        "scene for the twentieth time, and each replay adds a detail that "
        "was not there before. Midday: a text arrives - running late, see "
        "you at seven - and the ordinary message gets read three times "
        "for tone. Work drags; a coworker's innocent question about "
        "weekend plans lands wrong and gets a short answer. Lunch is "
        "half-eaten while scrolling, not for news but for distraction "
        "that does not come. Afternoon: the resolve forms - just ask "
        "casually, just one question - and then unforms, because the "
        "question will sound like an accusation and the answer will not "
        "be believed anyway. Evening: they arrive, they are warm, they "
        "are normal, and for an hour the alarm quiets. Then the phone "
        "buzzes face-down on the table, and the whole weather system "
        "rolls back in. Night: lying awake, making plans to check, "
        "ashamed of the plans, making them anyway. Nothing happened "
        "today. That is the point of the vignette: jealousy does not "
        "need events. It runs on attention, and it can fill an ordinary "
        "day to the brim with weather about nothing."),
    how_it_works=(
        "The vignette shows every mechanism from the earlier records "
        "running in sequence: the morning replay is the evidence hunt, "
        "the triple-read text is ambiguity feeding the alarm, the short "
        "answer to the coworker is the narrowed attention spilling over, "
        "the forming-and-unforming resolve is the approach-avoidance "
        "pull of the fear blend, the evening quiet is the alarm finding "
        "no fresh fuel, the face-down phone is a new trigger restarting "
        "the cycle, and the night plans are the peak-urge to act when "
        "facts are thinnest. The day also shows the background-load dial "
        "at work: tiredness by evening makes every ambiguity heavier. "
        "Reading the vignette as a map, a person can spot their own "
        "day in it and name which hour they are in - and the naming "
        "itself loosens the weather, because a mapped storm is smaller "
        "than an unmapped one."),
    key_points=[
        "Jealousy can fill an ordinary day with weather about nothing - it runs on attention, not events.",
        "The vignette strings every earlier mechanism into one lived sequence.",
        "Evening tiredness turns up the background-load dial, making late-day ambiguity heaviest.",
        "The forming-and-unforming resolve shows the approach-avoidance pull of the fear blend.",
        "Naming which hour you are in loosens the weather; a mapped storm is smaller than an unmapped one.",
    ],
    requirements=[
        "Walk a full ordinary day morning to night",
        "Show the mechanisms from earlier records in action",
        "End with the nothing-happened point",
        "No diagnostic language anywhere in the record",
    ],
    standards=["Ecological description of emotion episodes per Scherer component process model"],
    citations=[CIT_SCHERER, CIT_WHITE, CIT_PINES],
    sig_lens=(
        "The Signature lens reads the ordinary day as the sentinel's "
        "longest watch: no enemy comes, yet the watchman paces the wall "
        "from dawn to midnight, wearing a groove in the stone with his "
        "own feet. His method does not mock the pacing - the watch was "
        "honest - but points to the groove and asks what the wall would "
        "look like if the same devotion patrolled the treasure instead "
        "of the horizon. Clearly labeled Signature-made, never presented "
        "as authentic public record."),
),
# ---------------------------------------------------------------- 10-13: body signals
dict(
    key="jealousy_body_signals", name="Jealousy in the Body: Heart, Breath, Muscles, Stomach, and Skin",
    group="Compounded", ladder_rank=10, ladder_tier="compounded",
    description=(
        "Jealousy writes itself across the body in a recognizable "
        "signature. The heart is first: it quickens at the trigger and "
        "may pound during the peak, the classic alarm-system surge. The "
        "breath goes shallow and fast, or catches - people often hold "
        "their breath for a beat when the trigger lands, as if bracing. "
        "The muscles tense in a pattern: jaw clenches, shoulders rise "
        "toward the ears, hands curl or grip - the body preparing either "
        "to confront or to hold itself back. The stomach is jealousy's "
        "loudest organ for many: a dropping, hollow, or churning "
        "sensation, sometimes real nausea, because the gut and the alarm "
        "system share wiring. The skin runs hot and cold by turns - "
        "flushing in the face and chest, then a cold prickle as the fear "
        "blend underneath surfaces. Energy swings: a wired, restless "
        "surge at onset that makes sitting still impossible, collapsing "
        "later into a heavy, drained flatness when the plateau sets in. "
        "None of these signals is unique to jealousy - they are the "
        "body's general alarm kit - but the combination, arriving with "
        "the narrowed attention on a rival, is the fingerprint."),
    how_it_works=(
        "The body pattern is the threat system doing its ancient job. The "
        "alarm signal releases adrenaline, which raises heart rate, "
        "quickens breath, and tenses muscles for action - the same "
        "machinery behind every fight-or-flight response. The gut "
        "sensation comes from blood being routed away from digestion "
        "toward the muscles, which is why strong jealousy can genuinely "
        "kill appetite or turn the stomach. The hot-cold skin swings "
        "track the two partners of the blend: heat with the jealous "
        "approach urge, cold with the fear underneath. The energy arc - "
        "wired then drained - follows arousal economics: the body cannot "
        "hold peak alarm for long, so the surge spends itself and leaves "
        "fatigue. Reading the body is practical, not just descriptive: "
        "the signals arrive seconds before the thoughts, so a person who "
        "knows their own signature gets an early warning and a head start "
        "on choosing a response."),
    key_points=[
        "The jealous body signature: quickened heart, shallow breath, clenched jaw, raised shoulders, gripping hands.",
        "The stomach is often the loudest organ - dropping, hollow, churning - because gut and alarm share wiring.",
        "Skin runs hot with the jealous approach urge and cold with the fear underneath.",
        "Energy arcs from a wired restless surge to a heavy drained flatness.",
        "Body signals arrive seconds before thoughts, giving an early warning to anyone who knows their signature.",
    ],
    requirements=[
        "Cover heart, breath, muscles, stomach, skin, and energy",
        "Explain the physiology in plain words",
        "Note the signals are the general alarm kit, not unique to jealousy",
        "No diagnostic language anywhere in the record",
    ],
    standards=["Physiological arousal in emotion per Schachter and Singer and Cannon"],
    citations=[CIT_SCHACHTER, CIT_LAZARUS, CIT_IZARD],
    sig_lens=(
        "The Signature lens reads the body as the sentinel's garrison: "
        "the heart the war drum, the breath the held watch, the jaw and "
        "fists the guard at the gate, the stomach the hollow courtyard "
        "where the alarm echoes loudest. His method teaches the watchman "
        "to read his own garrison - the drumbeat is the earliest true "
        "report, arriving before any rumor - and to steady the garrison "
        "before riding out, because no clear report ever came from a "
        "panicked guard. Clearly labeled Signature-made, never presented "
        "as authentic public record."),
),
dict(
    key="jealousy_posture", name="Posture and Movement: How the Body Carries Jealousy",
    group="Compounded", ladder_rank=11, ladder_tier="compounded",
    description=(
        "Jealousy has a posture, and rooms can read it before a word is "
        "spoken. The still version: the body goes rigid and watchful - "
        "spine straight, chin slightly down, eyes fixed or tracking the "
        "rival across the room. Movement narrows to the threat: the "
        "person angles toward the partner and the rival, feet planted, "
        "as if holding ground. Hands do the quiet work - arms crossed "
        "tight, fingers interlaced hard, or one hand gripping the other "
        "wrist. The restless version: pacing, shifting weight, touching "
        "the face and neck, checking the phone with quick jerky motions, "
        "unable to settle in a chair. Toward the partner, the body "
        "oscillates: leaning in close and proprietary - a hand on the "
        "shoulder, standing between the partner and the rival - then "
        "pulling away cold, turned shoulder, stepped-back distance, when "
        "the fear blend takes over. Gait changes too: the jealous walk "
        "is faster and harder-heeled than usual, or it slows into a "
        "deliberate stalk when the person is trying to look unbothered "
        "and failing. Actors and observers alike can read the state from "
        "ten feet away, which is why the posture record matters for "
        "recognition as much as for self-knowledge."),
    how_it_works=(
        "Posture is the alarm system made visible. The rigid watchful "
        "stance is threat monitoring: the body orients its sensors - "
        "eyes, ears - toward the danger and freezes nonessential motion "
        "to process it. The proprietary leaning is mate-guarding "
        "behavior, the body's old strategy for marking the bond; the "
        "cold withdrawal is the fear partner's protection urge. The "
        "oscillation between them is the approach-avoidance conflict "
        "playing out in space: come closer, pull away, come closer. "
        "Restlessness is unspent arousal - the adrenaline has prepared "
        "the muscles for action and, with no action taken, leaks out as "
        "fidgeting and pacing. The failed casualness - the deliberate "
        "slow walk - is the body trying to perform calm while the "
        "alarm still runs the muscles; the mismatch is exactly what "
        "observers pick up on."),
    key_points=[
        "The still jealous posture: rigid, watchful, angled toward the threat, holding ground.",
        "The restless version: pacing, fidgeting, jerky phone-checking - unspent arousal leaking out.",
        "Toward the partner the body oscillates: proprietary leaning in, then cold withdrawal.",
        "The failed-casual slow walk is the mismatch observers read instantly.",
        "Posture is the alarm system made visible - recognition starts here.",
    ],
    requirements=[
        "Describe still, restless, and oscillating postures",
        "Explain the physiology behind each in plain words",
        "Note the observer's ten-foot read",
        "No diagnostic language anywhere in the record",
    ],
    standards=["Emotion expression in posture per Ekman and Izard frameworks"],
    citations=[CIT_EKMAN, CIT_IZARD, CIT_WHITE],
    sig_lens=(
        "The Signature lens reads posture as the sentinel's stance at the "
        "wall: feet planted on the parapet, lantern fixed on the "
        "horizon, one hand on the gate and one on his own wrist to keep "
        "it from drawing. His method treats the stance as honest - the "
        "body cannot lie about the watch it stands - and teaches the "
        "watchman that the wall is held by standing it, not by pacing it "
        "to dust. Clearly labeled Signature-made, never presented as "
        "authentic public record."),
),
dict(
    key="jealousy_sleep_appetite", name="Sleep, Appetite, and Energy Under Jealousy",
    group="Compounded", ladder_rank=12, ladder_tier="compounded",
    description=(
        "Jealousy is expensive, and the body pays in sleep, food, and "
        "fuel. Sleep goes first: the mind that has been running evidence "
        "all day does not switch off at midnight. People lie awake "
        "replaying the trigger scene, rehearsing confrontations, doing "
        "threat math - and when sleep comes it is light, broken by vivid "
        "dreams in which the rival wins. Appetite splits two ways: most "
        "people lose it, the churning gut refusing food, meals skipped or "
        "pushed around the plate; a smaller number eat for comfort, "
        "seeking the one steadying signal available. Energy follows the "
        "arousal arc: the wired surge of onset burns through the day's "
        "fuel by afternoon, leaving a flat, grey exhaustion that looks "
        "like sadness and is often mistaken for it. Concentration thins - "
        "work, study, and conversation all compete with the background "
        "threat-scan running underneath. The cruel loop: poor sleep and "
        "poor fuel raise the background-load dial, which turns up the "
        "next day's jealousy, which wrecks the next night's sleep. "
        "Breaking any single link - one protected night of sleep, one "
        "real meal - measurably lowers the volume."),
    how_it_works=(
        "The mechanism is arousal economics plus cognitive load. Sustained "
        "alarm keeps the stress system engaged, and an engaged stress "
        "system suppresses sleep onset and fragments sleep architecture - "
        "the brain will not fully stand down while it believes a threat "
        "is active. Appetite loss follows the gut-blood routing described "
        "in the body-signals record; comfort eating follows the "
        "self-soothing drive, food being the fastest available calm "
        "signal. The energy crash is simple depletion: hours of muscular "
        "tension and mental scanning burn real fuel. The concentration "
        "thinning is attention economics - the threat-scan is a background "
        "process consuming working memory, leaving less for everything "
        "else. The loop closes because a tired, underfueled brain "
        "appraises ambiguous events as more threatening, which is "
        "well-established in appraisal research."),
    key_points=[
        "Jealousy taxes sleep first: replaying, rehearsing, and threat math keep the mind lit past midnight.",
        "Appetite usually drops from the churning gut; some people eat for comfort instead.",
        "Energy arcs from wired surge to flat grey exhaustion that mimics sadness.",
        "The threat-scan runs as a background process, thinning concentration for everything else.",
        "Poor sleep and poor fuel raise the background-load dial - breaking one link lowers the volume.",
    ],
    requirements=[
        "Cover sleep, appetite, energy, and concentration",
        "Explain the self-reinforcing loop",
        "Give the practical break-one-link advice",
        "No diagnostic language anywhere in the record",
    ],
    standards=["Sleep and appetite effects of sustained arousal per psychophysiology literature"],
    citations=[CIT_SCHACHTER, CIT_GROSS, CIT_PINES],
    sig_lens=(
        "The Signature lens reads the drained body as a garrison after a "
        "false siege: the stores eaten, the wells low, the watchmen "
        "asleep at their posts - and therefore the next rumor hits "
        "harder, because an exhausted guard mistakes every shadow for "
        "an army. His method's first order after any alarm is always the "
        "same: feed the garrison, rest the watch. A sentinel who sleeps "
        "sees truly; a starved one sees enemies. Clearly labeled "
        "Signature-made, never presented as authentic public record."),
),
dict(
    key="jealousy_body_differences", name="How Jealousy Feels in Different Bodies: No Two Alike",
    group="Compounded", ladder_rank=13, ladder_tier="compounded",
    description=(
        "The jealousy signature in the last three records is the common "
        "pattern, but no two bodies read it the same way. Some people "
        "live the feeling almost entirely in the gut - nausea, churning, "
        "a hollow that food cannot fill - while their heart barely "
        "changes pace. Others feel nothing in the stomach and everything "
        "in the chest: tightness, pounding, heat rising up the neck. "
        "Some go hot - flushed face, sweating palms, the approach-urge "
        "dominant - while others go cold - pale, still, stomach dropped, "
        "the fear blend dominant. Age, fitness, and health reshape the "
        "pattern: a conditioned heart recovers faster from the surge, "
        "while chronic tension or illness can make the muscle pattern "
        "louder and longer. Temperament matters too: expressive people "
        "may feel the feeling as big body weather they cannot hide, "
        "while restrained people feel it as a small tight knot they "
        "carry silently - same alarm, different volume knob on the body. "
        "Past experience tunes the instrument: someone whose trust was "
        "broken before may feel the gut-drop at triggers others would "
        "not notice. The practical point is personal: nobody else's "
        "body is the reference. Learning one's own signature - where it "
        "lands first, how it moves, how long it lasts - is what turns "
        "the body from a confusing noise into an early-warning "
        "instrument."),
    how_it_works=(
        "Individual differences come from three sources. First, "
        "physiology: baseline heart rate, gut sensitivity, and muscle "
        "tension habits vary person to person, so the same adrenaline "
        "surge lands in different organs. Second, interoception - how "
        "finely a person senses internal signals: high-interoception "
        "people feel the gut-drop vividly, low-interoception people may "
        "only notice the thoughts. Third, learning history: the alarm "
        "system is a prediction machine shaped by past outcomes, so old "
        "wounds lower the trigger threshold and amplify the response in "
        "the channels that were active last time. None of this changes "
        "the underlying sequence - value, threat, appraisal, alarm, urge "
        "- it only changes where the alarm rings loudest. That is why "
        "self-knowledge beats comparison: the question is never 'do I "
        "feel it like others do' but 'where does mine land, and what is "
        "it telling me'."),
    key_points=[
        "Some bodies feel jealousy in the gut, others in the chest; some go hot, others go cold.",
        "Physiology, interoception, and learning history create the differences.",
        "Old wounds lower the threshold and amplify the channels active last time.",
        "Expressive people feel big body weather; restrained people carry a small tight knot - same alarm.",
        "Learn your own signature: where it lands first, how it moves, how long it lasts.",
    ],
    requirements=[
        "Give concrete variation examples across organs and patterns",
        "Name the three sources of difference",
        "Warn against comparing one's body to others",
        "No diagnostic language anywhere in the record",
    ],
    standards=["Individual differences in emotion physiology per Izard and Scherer"],
    citations=[CIT_IZARD, CIT_SCHERER, CIT_WHITE],
    sig_lens=(
        "The Signature lens reads each body as a different watchtower: "
        "one rings its bell in the courtyard, another lights its beacon "
        "on the roof, a third sends runners - same alarm, different "
        "tower. His method forbids comparing towers: the wise commander "
        "learns his own tower's voice - which bell rings first, how long "
        "the beacon burns - until the garrison's noise becomes a "
        "language. Clearly labeled Signature-made, never presented as "
        "authentic public record."),
),
# ---------------------------------------------------------------- 14-17: facial expression
dict(
    key="jealousy_face", name="The Face of Jealousy: Eyes, Brows, Mouth, and Micro-Signs",
    group="Compounded", ladder_rank=14, ladder_tier="compounded",
    description=(
        "Jealousy has no single universal face the way some basic emotions "
        "do - it borrows its features - but the borrowed face is "
        "recognizable. The eyes do the most work: narrowed, fixed, "
        "tracking. The jealous gaze locks onto the rival or flicks "
        "between the partner and the rival, measuring. The brows draw "
        "down and together, the classic threat-watch furrow, sometimes "
        "with the inner corners lifted in the fear blend's signature. "
        "The mouth tightens: lips pressed into a thin line, corners "
        "pulled down or pulled sideways in contempt's near-neighbor, the "
        "jaw visibly set. Micro-signs flash and vanish in fractions of "
        "a second: the quick nostril flare at the trigger moment, the "
        "single hard blink, the lip press that lasts half a second too "
        "long, the glance that darts to the rival and snaps away when "
        "caught. The overall impression is of a face doing two jobs at "
        "once - watching and hiding the watching - which gives jealousy "
        "its characteristic look: attention aimed like a weapon, "
        "expression clamped down around it. Because the feeling is "
        "socially awkward to display, much of the face is suppression, "
        "and suppression itself becomes the tell."),
    how_it_works=(
        "The face assembles from component expressions because jealousy "
        "is a complex emotion: the narrowed eyes and lowered brows come "
        "from the anger/threat-watch component, the inner-brow lift and "
        "widened eyes from the fear component, the pressed lips from the "
        "effort of control. Micro-signs are leakage - the feeling "
        "firing the facial muscles before the control system can "
        "countermand them, typically in the first half-second after the "
        "trigger. The tracking gaze is attentional bias made visible: "
        "the visual system prioritizes the threat, and the eyes obey. "
        "The suppression look - the clamped, over-neutral face - is "
        "itself informative: a face working hard to show nothing is "
        "showing the work. Researchers of expression note that blended "
        "emotions produce blended faces, and jealousy is a textbook "
        "case: read the parts separately - the anger in the brow, the "
        "fear in the eyes, the control in the mouth - and the whole "
        "becomes legible."),
    key_points=[
        "Jealousy borrows its face: narrowed tracking eyes, lowered brows, pressed lips, set jaw.",
        "Micro-signs - nostril flare, hard blink, overlong lip press, darting glance - flash in fractions of a second.",
        "The face does two jobs: watching and hiding the watching; the suppression itself is the tell.",
        "Read the parts separately: anger in the brow, fear in the eyes, control in the mouth.",
        "The tracking gaze is attentional bias made visible - the eyes obey the threat priority.",
    ],
    requirements=[
        "Describe eyes, brows, mouth, and micro-signs in detail",
        "Explain why suppression becomes the tell",
        "Give the read-the-parts method",
        "No diagnostic language anywhere in the record",
    ],
    standards=["Facial expression of blended emotions per Ekman Emotions Revealed"],
    citations=[CIT_EKMAN, CIT_IZARD, CIT_WHITE],
    sig_lens=(
        "The Signature lens reads the jealous face as the sentinel's "
        "lantern behind a shutter: the light fixed on the horizon, the "
        "shutter half-closed to hide the watching, the hand trembling on "
        "the shutter-string. His method teaches that a guarded lantern "
        "still casts light - the very effort of hiding the watch "
        "announces it - and that the honorable watchman learns to lower "
        "the shutter openly rather than let it rattle. Clearly labeled "
        "Signature-made, never presented as authentic public record."),
),
dict(
    key="jealousy_face_intensity", name="How the Jealous Expression Changes with Intensity",
    group="Compounded", ladder_rank=15, ladder_tier="compounded",
    description=(
        "At mild intensity, the face shows almost nothing - and that "
        "almost is the whole story. A half-second narrowing of the eyes "
        "when the rival's name lands, a brief press of the lips, a "
        "glance that lingers a beat too long on the pair across the "
        "room. Anyone not watching would miss it; the person feeling it "
        "may not even know their face moved. At moderate intensity, the "
        "suppression starts to show its effort: the smile goes fixed and "
        "slightly asymmetrical, the eyes keep returning to the threat "
        "like a tongue to a sore tooth, the jaw works. Conversations "
        "develop a tight, bright quality - too much laugh, too quick "
        "agreement - as the person performs ease. At high intensity, "
        "control breaks down: the stare becomes open and hard, the mouth "
        "draws into a thin downturned line, the brows lock in the furrow, "
        "and the face may flush or go pale in patches. The voice joins "
        "the face - clipped, edged - and the whole presentation turns "
        "confrontational or icy. The progression is really a story about "
        "control budgets: mild jealousy is fully affordable to hide, "
        "moderate jealousy costs visible effort, and intense jealousy "
        "bankrupts the control system entirely."),
    how_it_works=(
        "Expression intensity tracks arousal against control capacity. At "
        "low arousal, the facial muscles receive only a whisper of the "
        "alarm, producing micro-signs that the control system easily "
        "overrides - hence the half-second tells. At moderate arousal, "
        "the alarm signal strengthens and the control system must work "
        "continuously to countermand it; continuous countermanding "
        "produces its own artifacts - the fixed smile, the over-bright "
        "tone - because the face is now performing two programs at once. "
        "At high arousal, the alarm overwhelms control: the threat-watch "
        "expression runs unopposed, and the autonomic signs - flushing, "
        "pallor - appear because they were never under voluntary control "
        "at all. The practical reading rule: the harder a face is working "
        "to look neutral, the stronger the feeling underneath. Ease is "
        "cheap; performed ease is expensive, and the expense shows."),
    key_points=[
        "Mild: half-second tells - eye narrowing, lip press, lingering glance - easy to miss.",
        "Moderate: suppression shows its effort - fixed smile, returning gaze, working jaw, over-bright tone.",
        "High: control bankrupts - open hard stare, thin downturned mouth, locked furrow, flushing or pallor.",
        "The progression is a story about control budgets: affordable, effortful, overwhelmed.",
        "Reading rule: the harder a face works to look neutral, the stronger the feeling underneath.",
    ],
    requirements=[
        "Describe the face at all three intensities",
        "Explain the control-budget mechanism",
        "Give the practical reading rule",
        "No diagnostic language anywhere in the record",
    ],
    standards=["Expression intensity and control per Ekman and Gross regulation research"],
    citations=[CIT_EKMAN, CIT_GROSS, CIT_WHITE],
    sig_lens=(
        "The Signature lens reads the three faces as the sentinel's "
        "three watches: the quiet note in the logbook, the shutter "
        "rattling in its frame, and the lantern thrown wide open, "
        "flooding the wall with light. His method notes the honest "
        "arithmetic - a shutter that rattles is guarding something "
        "real, whatever the watchman's words - and teaches that the "
        "lantern thrown wide is the moment to stand down the watch, "
        "not to charge the dark. Clearly labeled Signature-made, never "
        "presented as authentic public record."),
),
dict(
    key="jealousy_hiding_faking", name="Hiding and Faking Jealousy: What Leaks Through",
    group="Compounded", ladder_rank=16, ladder_tier="compounded",
    description=(
        "People hide jealousy more than almost any emotion, because "
        "showing it feels like confessing weakness and accusing the "
        "partner at once. The hiding toolkit is familiar: the "
        "over-casual shrug, the too-quick 'I'm fine,' the sudden "
        "intense interest in the phone, the laugh pitched one note too "
        "high. What leaks through anyway is the timing, not the "
        "content: the pause half a beat too long before answering who "
        "that was, the questions that arrive disguised as small talk - "
        "so how do you two know each other, again - the attention that "
        "keeps sliding back to the rival like a compass needle. Faking "
        "is the reverse performance: pretending jealousy to test a "
        "partner, to provoke reassurance, or to mask a different "
        "feeling. Faked jealousy leaks in the opposite direction - it "
        "is too clean, too narrated, missing the involuntary tells: no "
        "gut-drop timing, no micro-signs, the anger performed but the "
        "fear absent. Real jealousy is messy and badly timed; performed "
        "jealousy is tidy and well-timed. The deepest leak of all is "
        "physiological: nobody can fake or suppress the autonomic "
        "signs - the flush, the pupil change, the caught breath - which "
        "is why the body remains the honest witness when the face is "
        "negotiating."),
    how_it_works=(
        "Hiding works through the voluntary control system countermanding "
        "the expression program, but countermanding is imperfect in three "
        "ways. First, timing: the feeling fires the muscles in under a "
        "second, while the cover story takes longer to assemble, so the "
        "first half-second is always honest. Second, attention: "
        "suppression consumes working memory, so the hidden feeling "
        "steals resources from the performance - hence the overlong "
        "pauses and the too-high laugh. Third, autonomy: the flush, the "
        "breath catch, and the pupil response run on the autonomic "
        "system, which takes no orders. Faking fails in reverse: the "
        "performer can produce the voluntary components - the furrowed "
        "brow, the hard tone - but cannot summon the autonomic ones on "
        "demand, and cannot reproduce the bad timing of the real thing. "
        "Observers who watch timing and physiology instead of words "
        "read both performances correctly."),
    key_points=[
        "Hiding leaks through timing: the half-beat pause, the disguised questions, the compass-needle attention.",
        "Faked jealousy is too clean and well-timed; real jealousy is messy and badly timed.",
        "The first half-second is always honest - the feeling fires before the cover story assembles.",
        "Nobody can fake or suppress the autonomic signs: flush, breath catch, pupil change.",
        "Watch timing and physiology, not words, to read either performance.",
    ],
    requirements=[
        "Describe the hiding toolkit and its leaks",
        "Describe faking and how it leaks in reverse",
        "Explain the three imperfections of suppression",
        "No diagnostic language anywhere in the record",
    ],
    standards=["Expression suppression and leakage per Ekman and Gross"],
    citations=[CIT_EKMAN, CIT_GROSS, CIT_WHITE],
    sig_lens=(
        "The Signature lens reads hiding as the sentinel shuttering his "
        "lantern and claiming the wall is dark - while the light leaks "
        "around every edge of the shutter. His method is gentle with the "
        "hiding watchman: the shuttering is honorable, the leaks are not "
        "betrayal but physics. And it reads faking as a false alarm rung "
        "for attention - the one offense against the watch, because a "
        "sentinel who cries threat for sport teaches the whole garrison "
        "to sleep through the true horn. Clearly labeled Signature-made, "
        "never presented as authentic public record."),
),
dict(
    key="jealousy_expression_gallery", name="Expression Gallery Notes: Drawing and Playing Jealousy",
    group="Compounded", ladder_rank=17, ladder_tier="compounded",
    description=(
        "For the artist: draw the jealous face in three-quarter view, "
        "gaze locked off-canvas toward the unseen rival. Narrow the eyes "
        "to slits but keep them wide enough to show the fixed attention - "
        "the white of the eye reduced, the lower lid raised. Draw the "
        "brows low and drawn together, with the inner corners tugged "
        "upward a fraction - the fear blend's contribution, easy to miss "
        "and essential. Press the lips into a thin horizontal line; pull "
        "one corner down a millimeter for the downturn, or sideways for "
        "the contempt neighbor. Set the jaw - show the masseter muscle's "
        "edge. Angle the head slightly down and forward, chin leading, "
        "the posture of someone holding ground. Add the hands: one "
        "gripping the opposite wrist behind the back, or arms crossed "
        "with the fingers digging in. For the actor: the jealousy is not "
        "in the big gestures but in the stillness between them. Let your "
        "eyes do the tracking - lock, flick away, return. Let the smile "
        "arrive a beat late and leave a beat early. Keep the breath "
        "shallow and audible in the quiet moments. The key direction: "
        "play a person watching and hiding the watching. Every choice "
        "serves the double job - the attention aimed like a weapon, the "
        "expression clamped around it - and the audience will read the "
        "feeling before a single jealous word is spoken."),
    how_it_works=(
        "These notes work because they assemble the component expressions "
        "identified in the face record into a performable whole. The "
        "three-quarter gaze gives the tracking eyes something to track; "
        "the brow specification encodes the anger-fear blend in drawable "
        "geometry; the mouth and jaw encode the control effort; the head "
        "angle and hands encode the posture record's holding-ground "
        "stance. For the actor, the direction exploits the suppression "
        "principle: audiences read effort, so playing the effort of "
        "hiding reads more truthfully than playing the feeling directly. "
        "The late-arriving smile and the shallow breath are timing and "
        "physiology - the two channels that cannot be faked - which is "
        "why they convince. A gallery note is a compression of the "
        "science into craft: every drawable line traces back to an "
        "appraisal, an arousal, or a control effort."),
    key_points=[
        "Artist: three-quarter view, tracking gaze, low drawn brows with inner-corner lift, pressed lips, set jaw.",
        "The hands tell the story too: gripping the opposite wrist, or arms crossed with digging fingers.",
        "Actor: play the stillness between gestures; let the eyes track, lock, flick away, return.",
        "The smile arrives a beat late and leaves a beat early; the breath stays shallow and audible.",
        "Direction: play a person watching and hiding the watching - the audience reads it before any jealous word.",
    ],
    requirements=[
        "Give drawable specifics for eyes, brows, mouth, jaw, head, hands",
        "Give playable direction for the actor",
        "Ground every choice in the earlier face and posture records",
        "No diagnostic language anywhere in the record",
    ],
    standards=["Applied expression craft informed by Ekman facial action description"],
    citations=[CIT_EKMAN, CIT_IZARD, CIT_WHITE],
    sig_lens=(
        "The Signature lens reads the gallery as the sentinel's portrait "
        "for the hall: not the battle, but the watch - lantern shuttered, "
        "eyes on the horizon, hand on the gate. His method asks the "
        "artist to paint the devotion inside the vigilance, and the actor "
        "to play the love inside the guarding, because a sentinel painted "
        "only as suspicion is a slander, and played only as fury is a "
        "caricature. The true portrait shows what the watch is for. "
        "Clearly labeled Signature-made, never presented as authentic "
        "public record."),
),
# ---------------------------------------------------------------- 18-21: triggers
dict(
    key="jealousy_classic_triggers", name="The Classic Triggers of Jealousy",
    group="Compounded", ladder_rank=18, ladder_tier="compounded",
    description=(
        "The classic triggers are the situations that set off jealousy in "
        "most people, most of the time. The rival's attention: a partner "
        "laughing with someone attractive, a best friend forming a new "
        "close friendship, a sibling praised where you were overlooked. "
        "Secrecy signals: the phone turned face-down, the vague answer "
        "about where the evening went, the new password. Changed patterns: "
        "the late nights that started last month, the sudden interest in "
        "appearance, the old jokes no longer shared. Exclusion moments: "
        "the inside joke you are not inside, the plan made without you, "
        "the photo from the gathering you were not invited to. Comparison "
        "scenes: watching the partner light up for someone else the way "
        "they once lit up for you. Each classic trigger works the same "
        "way: it presents the three-cornered shape - you, the bond, the "
        "rival - in a single vivid scene, and the appraisal system does "
        "the rest. Knowing the classics is protective twice over: a person "
        "can recognize the trigger as a known pattern rather than a "
        "unique catastrophe, and can also avoid carelessly staging these "
        "scenes for someone they love."),
    how_it_works=(
        "Classic triggers are appraisal shortcuts: each one delivers "
        "threat-to-a-valued-bond in a form the mind processes instantly, "
        "without deliberation. Secrecy signals work because concealment "
        "implies something worth concealing - the mind treats hidden "
        "information as threatening by default. Changed patterns work "
        "because the prediction system flags deviations: the bond had a "
        "shape, the shape changed, and change near something valued "
        "demands explanation. Exclusion works through the belonging "
        "system, one of the mind's deepest monitors; being left out "
        "registers as a bond threat even when no rival is visible. "
        "Comparison scenes are the most direct: they show the valued "
        "response - the laugh, the light - being given to someone else, "
        "which is the threat in its purest form. The universality of "
        "these triggers is why they are classic: they press the same "
        "appraisal buttons in nearly every human mind."),
    key_points=[
        "Classic triggers: rival attention, secrecy signals, changed patterns, exclusion moments, comparison scenes.",
        "Each trigger presents the three-cornered shape - you, the bond, the rival - in one vivid scene.",
        "Secrecy works because concealment implies something worth concealing.",
        "Changed patterns trip the prediction system: the bond had a shape, and the shape moved.",
        "Knowing the classics lets a person recognize a pattern instead of a unique catastrophe.",
    ],
    requirements=[
        "Catalog at least five classic trigger types with examples",
        "Explain the appraisal shortcut each one exploits",
        "Note the double protective value of knowing them",
        "No diagnostic language anywhere in the record",
    ],
    standards=["Jealousy trigger taxonomy per White and Mullen and Buss"],
    citations=[CIT_WHITE, CIT_BUSS, CIT_PINES],
    sig_lens=(
        "The Signature lens reads the classics as the known approaches to "
        "the gate: the stranger's laugh in the courtyard, the shuttered "
        "window, the changed patrol route, the feast to which the "
        "watchman was not bid. His method posts these approaches on the "
        "gate itself - every sentinel learns the classic roads by which "
        "trouble walks - so that a known road is met with a known "
        "watch, not with panic at a surprise. Clearly labeled "
        "Signature-made, never presented as authentic public record."),
),
dict(
    key="jealousy_personal_triggers", name="Personal Triggers: Memories, Anniversaries, and Private Associations",
    group="Compounded", ladder_rank=19, ladder_tier="compounded",
    description=(
        "Beyond the classics, every person carries a private trigger map "
        "drawn by their own history. A song that played during the "
        "breakup years ago can drop the gut in a grocery store. A "
        "restaurant, a cologne, a particular laugh - any of them can be "
        "wired to an old alarm. Anniversaries are calendar triggers: the "
        "month the trust broke last time, the season of the old rival, "
        "dates the conscious mind forgot but the body kept. Private "
        "associations are the subtlest: being the overlooked middle "
        "child makes a partner's praise of a sibling's friend land like "
        "a verdict; growing up as the new kid makes every new person in "
        "a friend's life feel like a replacement being auditioned. "
        "Personal triggers are unfair in a specific way: they import an "
        "old threat's certainty into a new situation's ambiguity, so the "
        "alarm rings with the confidence of memory about the facts of "
        "now. The partner sees an overreaction to nothing; the person "
        "feels an accurate reaction to something real - because the "
        "something is real, it is just not happening now. Mapping one's "
        "own triggers - writing down which scenes detonate and what they "
        "rhyme with - is the single most practical jealousy skill, "
        "because a named rhyme loses half its power to hijack the present."),
    how_it_works=(
        "Personal triggers work through associative memory: the alarm "
        "system tags experiences with emotional markers, and later "
        "experiences that share sensory or structural features reactivate "
        "the tag. This is the same machinery behind all emotional "
        "learning, applied to jealousy: the song is not sad, the song is "
        "tagged. Anniversaries work through temporal context - the "
        "calendar as a retrieval cue. The unfairness mechanism is "
        "appraisal contamination: the old episode's high threat-certainty "
        "bleeds into the new episode's appraisal, so ambiguity gets read "
        "with borrowed confidence. The partner's confusion is genuine "
        "because they are appraising the present; the person's "
        "conviction is genuine because they are feeling the past. Both "
        "are right about different things. The mapping practice works "
        "because explicit recall moves the memory from the fast alarm "
        "system to the slow reasoning system, where it can be dated: "
        "this happened then, it is echoing now."),
    key_points=[
        "Private trigger maps are drawn by personal history: songs, places, scents, anniversaries, old roles.",
        "Personal triggers import an old threat's certainty into a new situation's ambiguity.",
        "The partner sees overreaction to nothing; the person feels accurate reaction to something real - from the past.",
        "Mapping the triggers - which scenes detonate, what they rhyme with - is the top practical skill.",
        "A named rhyme loses half its power to hijack the present.",
    ],
    requirements=[
        "Give concrete examples of memory, anniversary, and association triggers",
        "Explain appraisal contamination clearly",
        "Validate both the partner's and the person's perspective",
        "No diagnostic language anywhere in the record",
    ],
    standards=["Associative emotional memory per Lazarus and LeDoux-adjacent appraisal literature"],
    citations=[CIT_LAZARUS, CIT_WHITE, CIT_PINES],
    sig_lens=(
        "The Signature lens reads personal triggers as old battlefields "
        "under new roads: the watchman flinches at a bend in the path "
        "because men died at such a bend before - the flinch is "
        "honorable, and the road is new. His method walks the old "
        "battlefield in daylight with the watchman, naming each fallen "
        "marker, until the bend is only a bend again. The past is "
        "honored as teacher and retired as commander. Clearly labeled "
        "Signature-made, never presented as authentic public record."),
),
dict(
    key="jealousy_surprise_triggers", name="Surprise Triggers: The Unexpected Things That Spark Jealousy",
    group="Compounded", ladder_rank=20, ladder_tier="compounded",
    description=(
        "Some triggers surprise even the person they strike, because they "
        "do not look like the classics. A partner's absorbed, happy "
        "silence while reading - no rival anywhere - can sting, because "
        "the contentment is not shared. A friend's success can trigger "
        "jealousy disguised as envy: the promotion is envied, but the "
        "fear underneath is that the friendship will not survive the new "
        "altitude. A pet's devotion to a visitor, a child's preference "
        "for the other parent on a given evening, a mentor's praise for "
        "a junior colleague - all can sound the alarm, and all embarrass "
        "the person they strike, which is why surprise triggers are the "
        "least confessed and the most shamed. Technology manufactures "
        "new ones constantly: the read receipt with no reply, the "
        "follower count, the tagged photo from an event you did not "
        "know about, the algorithm surfacing an ex's face unasked. "
        "Fiction triggers too: jealousy of a partner's favorite "
        "character, of a past lover who exists only in stories. The "
        "surprise in every case is the same discovery: the alarm does "
        "not check whether the rival is real, present, or even human "
        "before ringing. It checks only whether something valued feels "
        "attended-to elsewhere. Naming surprise triggers without shame "
        "is the work of this record - the alarm's taste in threats is "
        "wider and stranger than dignity prefers to admit."),
    how_it_works=(
        "Surprise triggers expose the alarm's actual logic, which is "
        "cruder than the classics suggest: it monitors the valued bond's "
        "attention share, not the rival's credentials. The absorbed "
        "reading stings because shared attention is the bond's currency "
        "and it is being spent elsewhere - on a book, which cannot "
        "compete, which is exactly why the sting is embarrassing. The "
        "friend's promotion threatens the friendship's future shape, a "
        "genuine bond threat wearing envy's clothes. Technology triggers "
        "work through ambiguity plus permanence: the read receipt is "
        "ambiguous, the tagged photo is permanent and public, and the "
        "algorithm is an endless rival-generator. Fiction triggers show "
        "the system at its most literal: the appraisal tags the "
        "character as a rival because the partner's emotional attention "
        "is visibly going there. The embarrassment is itself "
        "informative - shame about a trigger is a sign the reasoning "
        "system already knows the threat is thin, which is useful data "
        "for the person willing to hear it."),
    key_points=[
        "Surprise triggers: a partner's absorbed silence, a friend's success, a pet's devotion, a read receipt, a fictional character.",
        "The alarm monitors the bond's attention share, not the rival's credentials.",
        "Technology manufactures new triggers through ambiguity plus permanence.",
        "Embarrassment about a trigger is useful data: the reasoning system already knows the threat is thin.",
        "The alarm's taste in threats is wider and stranger than dignity admits - naming them without shame is the work.",
    ],
    requirements=[
        "Catalog genuinely surprising trigger types",
        "Explain the attention-share logic behind them",
        "Cover technology and fiction triggers",
        "No diagnostic language anywhere in the record",
    ],
    standards=["Attention-based appraisal in jealousy per White and Mullen"],
    citations=[CIT_WHITE, CIT_BUSS, CIT_SALOVEY],
    sig_lens=(
        "The Signature lens reads surprise triggers as the sentinel "
        "sounding the horn at a traveling player's painted dragon: the "
        "horn is honest - something moved on the wall - and the dragon "
        "is canvas. His method forbids shaming the watchman for the "
        "painted dragon; it teaches him to walk up and touch the canvas, "
        "laugh once with relief, and log the lesson. A sentinel who may "
        "confess his false alarms without shame will never hide a true "
        "one. Clearly labeled Signature-made, never presented as "
        "authentic public record."),
),
dict(
    key="jealousy_chain_reactions", name="Chain Reactions: How One Jealous Trigger Sets Off a Cascade",
    group="Compounded", ladder_rank=21, ladder_tier="compounded",
    description=(
        "One trigger rarely travels alone. The cascade usually runs "
        "like this: the initial trigger - the laugh across the room - "
        "fires the alarm. The alarm narrows attention, and the narrowed "
        "attention finds a second trigger that was always there but "
        "unnoticed: the partner has been distracted all week. The second "
        "trigger raises arousal, and raised arousal loosens the control "
        "system, so an old personal trigger surfaces - the song, the "
        "anniversary month - and now the past is testifying about the "
        "present. The person checks the phone, finds an ambiguous "
        "message, and ambiguity under high arousal reads as confirmation. "
        "Confrontation follows, badly timed and badly phrased; the "
        "partner gets defensive; defensiveness reads as guilt; and by "
        "midnight a single laugh has become a case file. The cascade "
        "feeds on its own products: each step manufactures the evidence "
        "the next step needs. Interrupting it requires catching any "
        "single link - the narrowed attention, the old memory, the "
        "checking urge, the badly timed confrontation - because the "
        "chain is only as strong as its weakest link, and every link is "
        "a choice point wearing the disguise of inevitability."),
    how_it_works=(
        "Cascades are positive feedback loops across the systems "
        "described in earlier records. Attention narrowing (record 5) "
        "manufactures new triggers; arousal (record 10) degrades control "
        "and appraisal accuracy; associative memory (record 19) imports "
        "old certainty; ambiguity (record 3) resolves toward threat "
        "under load; and confrontational behavior (record 22) provokes "
        "defensiveness that the alarm reads as guilt. Each loop "
        "increases the next loop's gain, which is why cascades "
        "accelerate: the midnight case file feels inevitable because "
        "each step raised the stakes for the next. The intervention "
        "logic is loop-breaking, not willpower: sleep breaks the "
        "arousal link, writing breaks the memory link, waiting breaks "
        "the confrontation link, and asking a calm question breaks the "
        "ambiguity link. Any single broken link starves the loop, "
        "because feedback needs every link to keep feeding itself."),
    key_points=[
        "Cascades run: trigger -> narrowed attention -> new triggers -> old memories -> checking -> bad confrontation -> defensiveness read as guilt.",
        "Each step manufactures the evidence the next step needs; the chain accelerates.",
        "Every link is a choice point wearing the disguise of inevitability.",
        "Interrupt any single link - sleep, writing, waiting, one calm question - to starve the loop.",
        "The midnight case file feels inevitable only in hindsight; it was a chain of breakable links.",
    ],
    requirements=[
        "Walk a full cascade step by step",
        "Name the feedback mechanism at each link",
        "Give loop-breaking interventions per link",
        "No diagnostic language anywhere in the record",
    ],
    standards=["Emotion escalation loops per Gross regulation and Scherer process models"],
    citations=[CIT_GROSS, CIT_SCHERER, CIT_WHITE],
    sig_lens=(
        "The Signature lens reads the cascade as a siege that the "
        "garrison lays to itself: the first horn startles the archers, "
        "the archers loose at shadows, the shadows return fire in the "
        "telling, and by midnight the fortress is bombarding its own "
        "fields. His method stations a calm officer at every link of "
        "the chain with one order: hold this post, and the siege ends. "
        "The fortress was never under attack; it only needed one "
        "steady voice to say so in time. Clearly labeled "
        "Signature-made, never presented as authentic public record."),
),
# ---------------------------------------------------------------- 22-25: behavior
dict(
    key="jealousy_actions", name="What People Do When They Feel Jealous: Actions and Reactions",
    group="Advanced", ladder_rank=22, ladder_tier="advanced",
    description=(
        "Jealousy moves the body before it moves the mind's arguments, "
        "and the action menu is remarkably consistent. Checking: the "
        "phone, the messages, the location, the social feed - the "
        "evidence hunt made physical. Questioning: the casual "
        "interrogation disguised as conversation, the same question "
        "asked three ways across an evening. Guarding: standing "
        "between the partner and the rival, monopolizing the partner's "
        "time, filling the calendar so no gap remains for the threat. "
        "Testing: the staged scenario - mentioning the rival to watch "
        "the reaction, arriving unannounced - designed to produce the "
        "evidence the alarm already believes in. Clinging: the sudden "
        "affection surge, the need for constant contact, reassurance "
        "sought hourly. Withdrawing: the cold shoulder, the cancelled "
        "plan, the preemptive distance - hurting first before being "
        "hurt, or punishing the partner for the alarm. Competing: the "
        "sudden self-improvement campaign, the pointed display of "
        "value, trying to outshine the rival. Each action is the urge "
        "from the five-beat sequence looking for an outlet, and each "
        "carries a cost ledger: checking buys brief relief and sells "
        "long-term trust, guarding buys presence and sells freedom, "
        "testing buys certainty and usually manufactures the opposite."),
    how_it_works=(
        "The actions sort into two strategies the research literature "
        "has long described: vigilance and guarding. Vigilance actions - "
        "checking, questioning, testing - serve the evidence hunt; "
        "their payoff is uncertainty reduction, and their trap is that "
        "under high arousal, no evidence ever suffices (record 7's "
        "confirmation trap). Guarding actions - monopolizing time, "
        "physical positioning, competing - serve bond defense; their "
        "payoff is reduced rival access, and their trap is that the "
        "partner experiences defense as control. Clinging and "
        "withdrawing are the fear blend's two poles: approach the bond "
        "for safety, or abandon it first to avoid the pain of losing "
        "it. Every action makes short-term sense to the alarm system - "
        "that is why they are so compelling - and long-term cost to the "
        "bond, which is why the ledger matters. The educational move "
        "is not to shame the actions but to price them honestly, so "
        "the person can choose with open eyes."),
    key_points=[
        "The consistent action menu: checking, questioning, guarding, testing, clinging, withdrawing, competing.",
        "Vigilance actions serve the evidence hunt; guarding actions serve bond defense.",
        "Each action has a cost ledger: checking buys brief relief and sells long-term trust.",
        "Clinging and withdrawing are the fear blend's two poles: approach for safety, or leave first.",
        "Price the actions honestly instead of shaming them, so choices are made with open eyes.",
    ],
    requirements=[
        "Catalog the seven action types with examples",
        "Sort them into vigilance and guarding strategies",
        "Give the cost ledger for each",
        "No diagnostic language anywhere in the record",
    ],
    standards=["Mate-retention and jealousy behavior tactics per Buss"],
    citations=[CIT_BUSS, CIT_WHITE, CIT_PINES],
    sig_lens=(
        "The Signature lens reads the action menu as the garrison's "
        "standard drills: the scouts sent out, the patrols doubled, "
        "the gate barred, the decoy sortie, the desperate embrace of "
        "the walls, the burned bridge, the polished armor. His method "
        "honors the drills - they are what garrisons are for - and then "
        "audits them: which drill protected the treasure, and which "
        "only exhausted the troops and alienated the town? The sentinel "
        "keeps the drills that guard and retires the drills that "
        "besiege his own people. Clearly labeled Signature-made, never "
        "presented as authentic public record."),
),
dict(
    key="jealousy_speech", name="What Jealous People Say: Phrases, Tone, and Speech Patterns",
    group="Advanced", ladder_rank=23, ladder_tier="advanced",
    description=(
        "Jealousy has a dialect, and its grammar is accusation wearing "
        "the clothes of curiosity. The disguised questions: 'So how do "
        "you two know each other, again?' - asked lightly, listened to "
        "heavily. 'You seemed to be having fun tonight' - a statement "
        "shaped like an observation, functioning as a charge. The "
        "tests: 'If you had to choose...' - hypotheticals designed to "
        "force ranking. The comparisons: 'You never laugh like that "
        "with me anymore' - the past weaponized against the present. "
        "The ultimatum family: 'It's me or them,' 'If you cared you'd "
        "stop talking to him' - control phrased as need. The "
        "reassurance loops: 'Do you love me? Really? But do you?' - "
        "the same question asked until the answer stops working. Tone "
        "does half the talking: the too-casual brightness that fools "
        "no one, the clipped coldness, the edge that turns ordinary "
        "sentences into cross-examination. Speech patterns shift too: "
        "rapid-fire questions, interrupting, circling back to the "
        "rival every few minutes no matter the topic, and the long "
        "silences that punish. People rarely announce 'I am jealous'; "
        "the dialect announces it for them, which is why learning to "
        "hear it - in oneself first - is a recognition skill."),
    how_it_works=(
        "The dialect is the evidence hunt and the control urge speaking "
        "through the mouth. Disguised questions are information-seeking "
        "with plausible deniability: the asker gets the data without "
        "paying the social price of admitting suspicion. Tests and "
        "ultimatums are the guarding strategy verbalized - attempts to "
        "restructure the partner's world by speech. Reassurance loops "
        "are the fear blend talking: no answer suffices because the "
        "question is about the future, which no answer can settle. The "
        "tone effects follow arousal directly - clipped speech is the "
        "body's tension in the vocal cords, rapid-fire questioning is "
        "the racing mind out loud. The circling-back pattern is "
        "attentional bias in conversation: the threat is the mind's "
        "priority topic, so discourse keeps returning to it like a "
        "tongue to a sore tooth. Hearing the dialect in oneself is the "
        "first intervention, because every phrase type has a plain "
        "translation - and the plain version ('I feel threatened and I "
        "need reassurance') works better than the disguised one."),
    key_points=[
        "The dialect: disguised questions, tests, comparisons, ultimatums, reassurance loops.",
        "Tone does half the talking: false brightness, clipped coldness, cross-examination edge.",
        "Patterns: rapid-fire questions, interrupting, circling back to the rival, punishing silences.",
        "Every phrase type has a plain translation, and the plain version works better.",
        "People rarely announce jealousy; learning to hear the dialect - in oneself first - is a recognition skill.",
    ],
    requirements=[
        "Give verbatim-style example phrases for each type",
        "Explain the function behind each phrase type",
        "Provide the plain-translation intervention",
        "No diagnostic language anywhere in the record",
    ],
    standards=["Jealousy communication patterns per White and Mullen and Guerrero-adjacent research"],
    citations=[CIT_WHITE, CIT_PINES, CIT_BUSS],
    sig_lens=(
        "The Signature lens reads the dialect as the watchman's coded "
        "reports: 'all quiet on the eastern wall' meaning 'I saw him "
        "looking at you,' the too-loud laugh in the mess hall meaning "
        "'reassure me.' His method teaches the watchman plain speech - "
        "a sentinel who says 'the gate feels thin tonight, stand with "
        "me' gets the garrison; one who speaks in code gets confusion "
        "and, eventually, a garrison that stops listening. Clearly "
        "labeled Signature-made, never presented as authentic public "
        "record."),
),
dict(
    key="jealousy_judgment", name="How Jealousy Changes Decisions and Judgment",
    group="Advanced", ladder_rank=24, ladder_tier="advanced",
    description=(
        "Jealousy does not just feel bad; it decides badly. Under its "
        "influence, the mind's normal decision machinery gets quietly "
        "rewired. Risk assessment skews: the jealous person overestimates "
        "the likelihood of betrayal and underestimates the cost of "
        "accusation - the very error that manufactures the confrontations "
        "of record 21's cascade. Time horizons shrink: long-term bond "
        "health gets traded for the short-term relief of checking or "
        "confronting, the way a thirsty person trades tomorrow's water "
        "for today's sip. Evidence standards collapse: the same person "
        "who demands proof at work accepts a vibe as verdict at home, "
        "because the alarm has already ruled and the reasoning is now "
        "just the clerk stamping the paperwork. Social judgment narrows: "
        "friends become potential informants or potential rivals, neutral "
        "parties get sorted into sides. Generosity of interpretation - "
        "the everyday habit of assuming benign motives - is the first "
        "casualty; every ambiguous act by the partner gets the worst "
        "available reading. Perhaps most costly: jealousy makes people "
        "decide about the relationship from inside the storm, when the "
        "data is worst and the judgment is weakest. The practical rule "
        "research supports is boring and effective: no bond-level "
        "decisions during peak alarm. Let the weather pass, then decide "
        "with the full mind."),
    how_it_works=(
        "The rewiring follows from the appraisal and arousal mechanics "
        "already established. High arousal impairs the prefrontal "
        "functions - working memory, impulse control, perspective-taking "
        "- which is why complex judgments degrade first. The threat "
        "appraisal sets a prior probability of betrayal near certainty, "
        "and Bayesian-style updating from that prior means even neutral "
        "evidence gets absorbed as confirmation. The shortened time "
        "horizon is the alarm system's design: it is built for immediate "
        "threats, so it discounts the future heavily - the same reason "
        "the checking urge feels irresistible now and regrettable later. "
        "The collapse of evidence standards is motivated reasoning: the "
        "conclusion is set, and cognition works backward to support it. "
        "The no-decisions-during-peak rule works because arousal decays "
        "faster than the underlying facts change; waiting restores the "
        "judge without losing any real information."),
    key_points=[
        "Jealousy rewires decisions: betrayal overestimated, accusation costs underestimated.",
        "Time horizons shrink: long-term bond health traded for short-term relief.",
        "Evidence standards collapse: the alarm rules first, reasoning becomes the clerk.",
        "Generosity of interpretation is the first casualty; ambiguity gets the worst reading.",
        "The practical rule: no bond-level decisions during peak alarm - let the weather pass, then decide.",
    ],
    requirements=[
        "Name at least five decision distortions",
        "Explain the mechanism behind each",
        "Give the no-decisions-during-peak rule with its rationale",
        "No diagnostic language anywhere in the record",
    ],
    standards=["Emotion effects on judgment per Lerner-and-Tiedens-adjacent appraisal tendency research"],
    citations=[CIT_LAZARUS, CIT_GROSS, CIT_BUSS],
    sig_lens=(
        "The Signature lens reads clouded judgment as the war council "
        "held during the alarm: every councilor shouting, the maps "
        "upside down, the vote taken before the scouts return. His "
        "method imposes the sentinel's oldest law - no orders are given "
        "from the wall during the horn; the council meets at dawn, "
        "with the scouts' true report and rested minds. A decision made "
        "in the storm belongs to the storm. Clearly labeled "
        "Signature-made, never presented as authentic public record."),
),
dict(
    key="jealousy_escalation", name="Jealousy Under Intensity: How Actions Escalate",
    group="Advanced", ladder_rank=25, ladder_tier="advanced",
    description=(
        "Escalation is the action menu of record 22 with the volume knob "
        "turned past reason, and it follows a grim, predictable ladder. "
        "It begins with quiet surveillance: the occasional glance at the "
        "phone becomes a nightly audit; the casual question becomes a "
        "standing interrogation. Then comes restriction: the partner's "
        "friendships get reviewed, outings get vetoed, the social world "
        "shrinks to what the alarm can monitor. Then confrontation as a "
        "lifestyle: accusations delivered as greetings, fights picked "
        "over trivia because the real subject cannot be named. Then the "
        "tests get crueler: staged scenes designed to force a confession, "
        "traps set for the partner to fail. At the far end lies the "
        "territory this database describes only to warn against: "
        "intimidation, threats, and control that curdles into coercion - "
        "patterns that destroy the bond they claim to protect and that "
        "no one should face alone. The escalation ladder is powered by "
        "tolerance: each step buys less relief than the last, so the "
        "next step must be bigger. Recognizing the ladder early is the "
        "whole point: the first rungs feel like vigilance and love, "
        "which is why they are so easy to climb and so important to "
        "name. Anyone finding themselves high on this ladder - or facing "
        "someone who is - should reach a trusted friend, counselor, or "
        "support service rather than handling it alone."),
    how_it_works=(
        "Escalation runs on the same feedback economics as the cascade "
        "of record 21, extended across weeks instead of hours. Each "
        "surveillance act temporarily lowers uncertainty, but the "
        "relief habituates - the alarm recalibrates, demanding more "
        "surveillance for the same quiet. This is tolerance, identical "
        "in structure to any habituating reward. Restriction follows "
        "because a smaller world is easier to monitor; confrontation "
        "becomes routine because the unspoken subject pressurizes every "
        "interaction; crueler tests follow because gentle tests stopped "
        "producing the certainty hit. The far end is where the guarding "
        "strategy fully devours the bond: control replaces trust, and "
        "the partner's compliance - if it comes - is read as proof the "
        "control was necessary, closing the loop. The exit ramps are "
        "early and specific: name the rung, break the surveillance "
        "habit for one week, tell one trusted person the whole truth, "
        "and seek outside perspective before the ladder's logic becomes "
        "the only logic available."),
    key_points=[
        "Escalation ladder: quiet surveillance -> standing interrogation -> restriction -> routine confrontation -> cruel tests -> coercion.",
        "Each step buys less relief than the last - tolerance demands bigger steps.",
        "The first rungs feel like vigilance and love, which is why they are easy to climb.",
        "At the far end, control replaces trust and destroys the bond it claims to protect.",
        "Exit ramps are early: name the rung, pause surveillance, tell one trusted person, seek outside perspective.",
    ],
    requirements=[
        "Walk the escalation ladder rung by rung",
        "Explain the tolerance mechanism",
        "Warn clearly about the far end without graphic detail",
        "Include the reach-out guidance; no diagnostic language",
    ],
    standards=["Escalation dynamics in jealousy per White and Mullen and Pines"],
    citations=[CIT_WHITE, CIT_PINES, CIT_BUSS],
    sig_lens=(
        "The Signature lens reads escalation as the garrison that begins "
        "by guarding the treasure and ends by imprisoning it: the patrols "
        "become a curfew, the curfew a cage, and at last the treasure "
        "itself is the prisoner the walls were built to protect. His "
        "method sounds the recall at the first rung - a sentinel who "
        "must be told that the town he polices is the town he serves - "
        "and insists that no watchman climbs this ladder alone: the "
        "recall is always sounded with another's voice beside his. "
        "Clearly labeled Signature-made, never presented as authentic "
        "public record."),
),
# ---------------------------------------------------------------- 26-28: healthy expression
dict(
    key="jealousy_healthy_expression", name="Healthy Expression: Saying, Showing, and Channeling Jealousy Well",
    group="Advanced", ladder_rank=26, ladder_tier="advanced",
    description=(
        "Jealousy expressed well becomes useful information for the "
        "relationship instead of weather in it. Saying it well means "
        "plain speech at a calm hour: 'I felt jealous when...' rather "
        "than 'You always...' - the feeling owned, the trigger named, "
        "the partner invited rather than accused. Timing is half the "
        "skill: not during the peak (record 24's rule), not as a "
        "greeting, not in front of an audience. Showing it well means "
        "letting the vulnerability show without weaponizing it: tears "
        "or a shaky voice are honest signals, and honest signals invite "
        "care; the same signals used as leverage invite resentment. "
        "Channeling it well means giving the arousal somewhere to go "
        "before the conversation: a walk, a workout, twenty minutes of "
        "writing the unsent letter - the alarm's energy spent on "
        "something that is not the partner. The deeper channel is "
        "conversion: the jealous urge to guard becomes the question "
        "'what does this bond need more of?' - and the answer is usually "
        "attention, play, or plain time together, which the jealous "
        "person can provide rather than police. Healthy expression also "
        "has a listening half: hearing the partner's reassurance without "
        "cross-examining it, which is a skill and can be practiced. The "
        "measure of healthy expression is simple: after it, the bond is "
        "closer or clearer than before."),
    how_it_works=(
        "Healthy expression works because it routes each component of "
        "jealousy to its proper address. Plain 'I felt' speech sends "
        "the appraisal to the partner as information instead of as "
        "accusation, which keeps the partner's defenses down and their "
        "empathy available. Calm timing sends the conversation to the "
        "reasoning system instead of the alarm system - both people's. "
        "Pre-channeling the arousal works through the body: spent "
        "adrenaline cannot fuel the cross-examination tone, so the "
        "words land as intended. Conversion - guarding into providing - "
        "works because it answers the underlying need: the alarm fired "
        "over threatened connection, and connection is built by giving "
        "attention, not by auditing it. Receiving reassurance without "
        "cross-examination works through trust practice: each accepted "
        "reassurance slightly lowers the next alarm's gain. None of "
        "this requires the feeling to be small; it requires the "
        "expression to be aimed."),
    key_points=[
        "Say it plain at a calm hour: 'I felt jealous when...' - feeling owned, trigger named, partner invited.",
        "Show the vulnerability without weaponizing it; honest signals invite care, leverage invites resentment.",
        "Channel the arousal first: walk, workout, or the unsent letter before the conversation.",
        "Convert guarding into providing: ask what the bond needs more of, then provide it.",
        "The measure: after healthy expression, the bond is closer or clearer than before.",
    ],
    requirements=[
        "Give the plain-speech formula with examples",
        "Cover saying, showing, and channeling as three channels",
        "Include the listening/receiving half",
        "No diagnostic language; general safe guidance only",
    ],
    standards=["Constructive jealousy communication per White and Mullen and Pines"],
    citations=[CIT_WHITE, CIT_PINES, CIT_GROSS],
    sig_lens=(
        "The Signature lens reads healthy expression as the sentinel's "
        "true report, delivered at dawn in plain words: 'The eastern "
        "approach worries me; walk it with me.' His method holds that "
        "the watchman's honor is not in silent suffering but in the "
        "clear report - and that the greatest conversion of the watch "
        "is this: the sentinel who feared losing the treasure becomes "
        "the gardener who tends it, and a tended treasure needs no "
        "guard. Clearly labeled Signature-made, never presented as "
        "authentic public record."),
),
dict(
    key="jealousy_unhealthy_expression", name="Unhealthy Expression: Bottling Up or Exploding - What Each Costs",
    group="Advanced", ladder_rank=27, ladder_tier="advanced",
    description=(
        "Jealousy mishandled takes two classic shapes, and both charge "
        "interest. Bottling up looks like maturity: the person says "
        "nothing, performs ease, and files the feeling away. The costs "
        "arrive on schedule anyway. The unspoken alarm keeps running its "
        "evidence hunt in the background, so suspicion grows without "
        "anyone to correct it. The body keeps the score - the tension, "
        "the broken sleep, the churning gut - with no outlet. And the "
        "bottle always leaks: the coldness, the sarcasm, the fight about "
        "the dishes that is really about the laugh across the room. "
        "Exploding is the opposite failure: the peak-hour confrontation, "
        "the accusation delivered as verdict, the ultimatum, the cruel "
        "test. Its costs are immediate and visible: the partner's "
        "defensiveness, the trust dented, the things said that cannot be "
        "unsaid - and the alarm, briefly satisfied by the drama, returns "
        "louder next time, having learned that explosions get attention. "
        "Both shapes share one root error: the feeling is treated as "
        "either unspeakable or as orders. It is neither. It is a report, "
        "and reports are meant to be delivered - clearly, at the right "
        "hour, to the right person. The price list of this record is the "
        "motivation for the practices of the next: every cost named here "
        "is a habit waiting to be built in record 28."),
    how_it_works=(
        "Bottling up fails through suppression economics: the control "
        "effort is continuous and expensive, the unexamined suspicion "
        "compounds without correction, and the physiological arousal "
        "with no outlet converts into chronic tension and sleep "
        "disruption. The leaks are the control system failing under "
        "load - suppression always fails first at the edges, in tone "
        "and timing. Exploding fails through the peak-impairment "
        "mechanism of record 24: the confrontation is staged when "
        "judgment is weakest and arousal highest, so it maximizes "
        "damage and minimizes information. The alarm's learning is the "
        "cruelest part: explosive expression gets a big response, and "
        "the alarm system logs big responses as effective, raising the "
        "gain for next time. The middle path - the report delivered "
        "clearly at the right hour - works because it gives the feeling "
        "an outlet (defusing the bottle) without giving it command "
        "(defusing the explosion)."),
    key_points=[
        "Bottling up: suspicion compounds uncorrected, the body keeps the score, and the bottle always leaks.",
        "Exploding: peak-hour confrontation maximizes damage, minimizes information, and teaches the alarm to escalate.",
        "Both share one root error: treating the feeling as unspeakable or as orders - it is neither, it is a report.",
        "Suppression fails first at the edges: tone, timing, the fight about the dishes.",
        "The middle path gives the feeling an outlet without giving it command.",
    ],
    requirements=[
        "Price both failure modes honestly with their mechanisms",
        "Show the shared root error",
        "Point forward to record 28's practices",
        "No diagnostic language; general safe guidance only",
    ],
    standards=["Suppression and dysregulation costs per Gross emotion regulation research"],
    citations=[CIT_GROSS, CIT_WHITE, CIT_PINES],
    sig_lens=(
        "The Signature lens reads the two failures as the sentinel's "
        "two disgraces: the watchman who sees the approach and says "
        "nothing, letting the enemy walk in while he polishes his "
        "silence - and the watchman who rings the war horn at a "
        "traveler's lantern and burns the village in the panic. His "
        "method restores the watchman's true office: neither silent nor "
        "screaming, but reporting - the clear voice at the clear hour "
        "that has saved more gates than any horn. Clearly labeled "
        "Signature-made, never presented as authentic public record."),
),
dict(
    key="jealousy_everyday_practices", name="Everyday Practices: Small Habits That Keep Jealousy in Balance",
    group="Advanced", ladder_rank=28, ladder_tier="advanced",
    description=(
        "Balance is not a single insight but a set of small habits, "
        "practiced on ordinary days so they are available on hard ones. "
        "The evidence habit: when the alarm sounds, write the facts in "
        "two columns - what happened, and what I am adding - before any "
        "action. The waiting habit: a personal rule, agreed with "
        "oneself in advance, to take no bond-level action for a set "
        "number of hours after a trigger. The body habit: protect sleep "
        "like a guard post, eat real meals, move the arousal through "
        "the muscles with a walk or workout - the background-load dial "
        "turned down daily. The plain-speech habit: a weekly "
        "low-stakes check-in with the partner - appreciations first, "
        "small worries second - so big feelings have a small, regular "
        "door. The attention habit: deliberately noticing what is going "
        "right in the bond each day, training the threat-scan to share "
        "the watch with a gratitude-scan. The outside-voice habit: one "
        "trusted friend who hears the unedited version and is allowed "
        "to say 'that sounds like the alarm, not the facts.' The "
        "history habit: knowing one's own trigger map (record 19) and "
        "greeting the old rhyme by name when it echoes. None of these "
        "is dramatic. That is the point: jealousy is weather, and "
        "weather is managed by climate - by the steady, boring, daily "
        "conditions in which storms either form or do not."),
    how_it_works=(
        "Each practice targets a specific link in the machinery. The "
        "two-column evidence habit moves appraisal from the fast alarm "
        "system to the slow reasoning system, where ambiguity can be "
        "held without resolving toward threat. The waiting habit "
        "exploits arousal decay: the urge is strongest when facts are "
        "thinnest, and time starves it. The body habit lowers the "
        "background-load dial directly - rested, fed, moved bodies "
        "appraise ambiguity as less threatening. The weekly check-in "
        "prevents pressure buildup: small regular disclosures keep the "
        "bottle from filling (record 27). The attention habit retrains "
        "the attentional bias over weeks, giving the threat-scan a "
        "competitor. The outside voice imports a second appraisal "
        "system, one not running the alarmed person's prior. The "
        "history habit dates the echoes, moving them from present "
        "threat to past memory. Together they do not eliminate the "
        "alarm - nothing should - they tune it, so it rings for "
        "approaches, not shadows."),
    key_points=[
        "The evidence habit: two columns - what happened, what I am adding - before any action.",
        "The waiting habit: no bond-level action for a set number of hours after a trigger.",
        "The body habit: sleep, real meals, movement - the background-load dial turned down daily.",
        "The plain-speech habit: weekly low-stakes check-ins give big feelings a small regular door.",
        "Balance is climate, not weather: steady daily conditions in which storms either form or do not.",
    ],
    requirements=[
        "Give at least seven concrete practices",
        "Map each practice to the mechanism it targets",
        "Keep guidance general, safe, and everyday",
        "No diagnostic language anywhere in the record",
    ],
    standards=["Applied emotion regulation strategies per Gross"],
    citations=[CIT_GROSS, CIT_PINES, CIT_WHITE],
    sig_lens=(
        "The Signature lens reads the practices as the sentinel's "
        "standing orders, posted on the gatehouse wall: log the watch, "
        "hold the horn till dawn, feed the garrison, walk the wall "
        "together weekly, count the harvests as well as the horizons, "
        "keep a second watchman you trust, and know your old "
        "battlefields by name. His method insists the orders are "
        "ordinary on purpose - gates are not held by heroes on the hard "
        "nights, but by habits kept on the hundred quiet ones before. "
        "Clearly labeled Signature-made, never presented as authentic "
        "public record."),
),
# ---------------------------------------------------------------- 29-31: recognizing in others
dict(
    key="jealousy_reading_others", name="Reading the Signs: Jealousy in Other People",
    group="Advanced", ladder_rank=29, ladder_tier="advanced",
    description=(
        "Reading jealousy in others is an act of observation, not "
        "accusation - the goal is understanding, never labeling a real "
        "person. Start with the face from records 14 to 16: the narrowed "
        "tracking gaze that keeps returning to the third person in the "
        "room, the pressed lips, the smile that arrives late and leaves "
        "early. Add the body from records 10 and 11: the stillness that "
        "is too still, or the restlessness that cannot settle; the "
        "proprietary hand on your shoulder that appears only when the "
        "rival is near. Listen for the dialect of record 23: the "
        "disguised questions about the other person, the comparisons "
        "with the past, the reassurance loops. Watch the behavior menu "
        "of record 22: the sudden schedule-filling, the phone that gets "
        "checked mid-conversation, the cold withdrawal after a warm "
        "evening. Context is the multiplier: these signs mean the most "
        "when a classic trigger (record 18) just occurred - the new "
        "coworker, the old friend in town, the changed routine. And the "
        "golden rule of reading: one sign is noise, three signs are a "
        "pattern, and a pattern is still only a hypothesis until the "
        "person confirms it. The ethical line is bright: observations "
        "are for responding with care, never for diagnosing, confronting "
        "with 'you're just jealous,' or using the read as a weapon."),
    how_it_works=(
        "The reading method layers the earlier records into a single "
        "observation stack: face plus body plus speech plus behavior "
        "plus context. Each layer is individually noisy - a pressed lip "
        "can mean concentration, a checked phone can mean boredom - but "
        "the layers are independent channels, and independent channels "
        "agreeing is strong evidence. The context multiplier works "
        "because jealousy is trigger-driven: the same behaviors without "
        "a trigger are far less diagnostic. The one-three-pattern rule "
        "is base-rate discipline: most single signs have innocent "
        "explanations most of the time, so disciplined observers wait "
        "for convergence. The hypothesis framing matters because minds "
        "love to complete patterns prematurely - treating the read as a "
        "question ('could they be feeling threatened?') keeps the "
        "observer curious instead of certain, which is what makes the "
        "response in the next record possible. Certainty about another "
        "person's inner state is the fastest route to the mistakes of "
        "record 31."),
    key_points=[
        "Layer the channels: face + body + speech + behavior + context; independent channels agreeing is strong evidence.",
        "Context multiplies meaning: signs count most right after a classic trigger.",
        "One sign is noise, three signs are a pattern, and a pattern is still only a hypothesis.",
        "Observation is for responding with care, never for labeling or weaponizing.",
        "Treat the read as a question, not a verdict - curiosity enables care, certainty enables mistakes.",
    ],
    requirements=[
        "Give the layered observation method",
        "Provide the one-three-pattern rule",
        "Draw the ethical line explicitly",
        "No diagnostic language anywhere in the record",
    ],
    standards=["Behavioral observation ethics per APA Dictionary guidance on labeling"],
    citations=[CIT_EKMAN, CIT_WHITE, CIT_APA],
    sig_lens=(
        "The Signature lens reads the observer as the second watchman on "
        "the wall: his duty is to notice when his fellow's lantern "
        "shutters and his step quickens - not to relieve him by force, "
        "not to mock the shuttered light, but to stand nearer, steady "
        "his own lantern, and be ready. His method's law of the wall: "
        "you watch your fellow to serve him, never to expose him. The "
        "read is a trust, and trusts are carried, not brandished. "
        "Clearly labeled Signature-made, never presented as authentic "
        "public record."),
),
dict(
    key="jealousy_supportive_responses", name="What to Say and Do When Someone Near You Feels Jealous",
    group="Advanced", ladder_rank=30, ladder_tier="advanced",
    description=(
        "When someone near you is in jealousy's weather, your job is "
        "steadiness, not adjudication. Do name what you see gently: 'You "
        "seem unsettled tonight - is something on your mind?' - an "
        "invitation, not a diagnosis. Do offer plain reassurance without "
        "being cross-examined into exhaustion: one clear, warm statement "
        "of the bond's value beats ten defensive answers. Do reduce "
        "ambiguity where you honestly can: the vague plan made concrete, "
        "the unnamed friend named - secrecy signals (record 18) are fuel, "
        "and clarity is water. Do keep your own steadiness: the jealous "
        "person's alarm is contagious, and a calm nervous system in the "
        "room is worth a hundred arguments. Do invite the plain version: "
        "'Tell me what you're afraid of' opens the door the disguised "
        "questions are circling. Do protect the bond's rituals - the "
        "regular time together, the small attentions - because the alarm "
        "fired over threatened connection, and connection is the "
        "answer. What you are doing, underneath all of it, is lending "
        "your calm appraisal system to someone whose own is running hot: "
        "not deciding for them, not dismissing them, just standing as a "
        "second, steadier witness until their weather passes."),
    how_it_works=(
        "Supportive responses work by addressing the jealous person's "
        "actual mechanisms rather than their surface demands. Gentle "
        "naming externalizes the feeling - once spoken, it can be "
        "examined instead of obeyed. Plain reassurance, given once and "
        "warmly, feeds the fear blend's need for safety; repeated "
        "defensive reassurance feeds the interrogation loop instead, "
        "which is why the dose matters. Reducing honest ambiguity "
        "starves the alarm of its favorite fuel without conceding to "
        "surveillance - there is a bright line between volunteering "
        "clarity and submitting to audits, and the supporter must hold "
        "it. Steadiness works through co-regulation: nervous systems "
        "entrain to each other, so calm is literally contagious. "
        "Inviting the plain version converts the dialect (record 23) "
        "into the report (record 26), which is the form feelings take "
        "when they are ready to be worked with. Protecting rituals "
        "answers the underlying need directly: the bond threatened was "
        "connection, and connection, tended, quiets the alarm."),
    key_points=[
        "Name it gently as an invitation, not a diagnosis: 'You seem unsettled - is something on your mind?'",
        "One clear warm reassurance beats ten defensive answers; dose matters.",
        "Volunteer honest clarity to starve ambiguity-fuel - but hold the line against submitting to audits.",
        "Lend your calm: steadiness is contagious, and a calm nervous system beats a hundred arguments.",
        "Protect the bond's rituals: the alarm fired over threatened connection, and connection is the answer.",
    ],
    requirements=[
        "Give concrete do-statements with example phrasing",
        "Explain the mechanism behind each response",
        "Draw the clarity-vs-audit line",
        "No diagnostic language; general safe guidance only",
    ],
    standards=["Supportive communication principles per White and Mullen and Pines"],
    citations=[CIT_WHITE, CIT_PINES, CIT_GROSS],
    sig_lens=(
        "The Signature lens reads the supporter as the watchman who "
        "brings his fellow a cloak and stands the cold hour with him: "
        "not taking the lantern from his hands, not telling him the "
        "horizon is empty, but standing close enough that his own "
        "steady breathing steadies the watch. His method's rule of the "
        "shared wall: you do not argue a watchman out of his alarm - "
        "you stand the watch with him until dawn shows what is really "
        "there. Clearly labeled Signature-made, never presented as "
        "authentic public record."),
),
dict(
    key="jealousy_mistakes_to_avoid", name="What NOT to Do: Mistakes That Make Jealousy Worse",
    group="Advanced", ladder_rank=31, ladder_tier="advanced",
    description=(
        "Good intentions pave most of these mistakes. Do not say 'you're "
        "just jealous' - the label ends the conversation and starts the "
        "war; the person hears dismissal, not insight. Do not lie, even "
        "kindly, to calm the storm: discovered soothing lies become "
        "permanent evidence that reassurance cannot be trusted, which "
        "raises every future alarm's gain. Do not submit to audits - "
        "handing over passwords, accepting surveillance - because "
        "compliance buys one quiet evening and sells the precedent that "
        "the alarm gets to set the terms; the next alarm will demand "
        "more. Do not stage provocations to 'teach a lesson' or test "
        "devotion; manufactured triggers manufacture real damage. Do not "
        "recruit allies or triangulate - telling the rival, enlisting "
        "friends as spies - because third parties turn a bond problem "
        "into a social fire. Do not answer the 2 a.m. interrogation as "
        "if it were a daytime question: peak-hour engagement (record "
        "24) produces the worst of both people; the kindest answer is "
        "'we will talk about this properly tomorrow.' And do not match "
        "the storm with your own - jealousy answered with jealousy, "
        "coldness with coldness, only doubles the weather. Every "
        "mistake on this list feels effective in the moment; that is "
        "exactly why the list exists."),
    how_it_works=(
        "Each mistake backfires through a specific mechanism. Labeling "
        "('you're just jealous') triggers the partner's defensiveness, "
        "which the alarm reads as guilt (record 21) - the observation "
        "becomes fuel. Soothing lies corrupt the reassurance channel "
        "itself: trust is the medium reassurance travels in, and lies "
        "poison the medium. Audit compliance operates on intermittent "
        "reinforcement - the most addictive schedule - training the "
        "alarm to escalate demands. Provocations and tests manufacture "
        "the very evidence patterns the alarm hunts, sometimes creating "
        "real wounds from staged ones. Triangulation multiplies the "
        "threat surface: every new person who knows is a new channel "
        "for the story to mutate through. Peak-hour engagement fails "
        "because both parties' judgment is at its worst (record 24). "
        "Storm-matching fails through emotional contagion: two alarmed "
        "nervous systems entrain upward, not downward. The unifying "
        "principle: never feed the mechanism you are trying to calm."),
    key_points=[
        "Never label: 'you're just jealous' ends the conversation and starts the war.",
        "Never soothe with lies: discovered lies permanently corrupt the reassurance channel.",
        "Never submit to audits: compliance buys one quiet evening and sells the precedent.",
        "Never engage the 2 a.m. interrogation as a daytime question - defer to tomorrow.",
        "The unifying principle: never feed the mechanism you are trying to calm.",
    ],
    requirements=[
        "Name at least seven concrete mistakes with their backfire mechanisms",
        "Explain why each feels effective in the moment",
        "Give the unifying principle",
        "No diagnostic language; general safe guidance only",
    ],
    standards=["Counterproductive responses to jealousy per White and Mullen and Pines"],
    citations=[CIT_WHITE, CIT_PINES, CIT_GROSS],
    sig_lens=(
        "The Signature lens reads each mistake as a way of besieging "
        "one's own gate: barring the report-bearer, salting the well "
        "the garrison drinks from, paying the raiders to return, "
        "staging false attacks for practice, inviting the countryside "
        "into the council, holding the war council at midnight, and "
        "answering the horn with a second horn. His method posts these "
        "beside the standing orders as the forbidden drills - not from "
        "harshness, but because the gate cannot survive its own "
        "defenders' errors. Clearly labeled Signature-made, never "
        "presented as authentic public record."),
),
# ---------------------------------------------------------------- 32-34: related emotions, mixes, simulation
dict(
    key="jealousy_related_emotions", name="The Jealousy Neighborhood: Related Emotions, Opposites, and Close Cousins",
    group="Advanced", ladder_rank=32, ladder_tier="advanced",
    description=(
        "Jealousy lives in a crowded neighborhood, and misaddressed "
        "mail is the norm. Nearest neighbors: envy (wants what another "
        "has; two-cornered, no bond threatened), suspicion (the cold "
        "cognitive doubt without jealousy's heat), possessiveness "
        "(jealousy hardened into a permanent stance toward the bond), "
        "and insecurity (the background soil jealousy grows in, not the "
        "plant itself). Close cousins that get confused: resentment "
        "(jealousy aged in the barrel - the threat is past, the grievance "
        "kept warm), betrayal (what jealousy fears has actually happened; "
        "the alarm confirmed), and competitiveness (the drive to outdo, "
        "without the threatened bond). Opposites and antidotes: trust "
        "(the settled expectation of goodwill - jealousy's true "
        "counterweight, built slowly and spent quickly), compersion (the "
        "uncommon joy in a loved one's other joys), and secure "
        "contentment (the bond at rest, the sentinel dozing in the sun). "
        "Telling cousins apart is practical: envy is treated by working "
        "with wanting, jealousy by working with threat; suspicion is "
        "answered with evidence, possessiveness with boundary work; "
        "resentment needs the past addressed, while live jealousy needs "
        "the present secured. The map's deepest lesson: most 'jealousy "
        "problems' are actually neighborhood problems - the wrong "
        "cousin being treated, while the real one goes unaddressed."),
    how_it_works=(
        "The neighborhood sorts along two axes: the shape of the "
        "triangle and the temperature. Envy is two-cornered (self and "
        "other, no guarded bond); jealousy is three-cornered (self, "
        "bond, rival) - the shape test alone separates them. Suspicion "
        "shares the triangle but runs cold: it is appraisal without the "
        "full alarm cascade, which is why suspicious people can be "
        "perfectly calm and jealous people rarely are. Possessiveness "
        "shares the heat but has dropped the specific rival: it guards "
        "the bond against the world in general. Resentment is jealousy "
        "plus time: the threat episode is over, but the appraisal was "
        "never updated, so the alarm's echo keeps firing. Betrayal is "
        "the confirmed case - jealousy's feared outcome realized - and "
        "it runs on grief more than alarm. The antidotes work by "
        "counter-appraisal: trust is the accumulated evidence that "
        "threats here are rare, which lowers the prior; compersion "
        "reframes the rival's gain as the loved one's joy, dissolving "
        "the triangle; contentment is low background load, the dial "
        "turned down. Misdiagnosis wastes the treatment: evidence does "
        "not cure possessiveness, and boundary work does not cure envy."),
    key_points=[
        "The shape test: envy is two-cornered, jealousy is three-cornered (self, bond, rival).",
        "Suspicion is jealousy's cold cousin: the triangle without the heat.",
        "Possessiveness is jealousy hardened into a permanent stance; resentment is jealousy aged in the barrel.",
        "True counterweights: trust (accumulated safety evidence), compersion, secure contentment.",
        "Most 'jealousy problems' are neighborhood problems - the wrong cousin being treated.",
    ],
    requirements=[
        "Map neighbors, cousins, and opposites with distinguishing tests",
        "Give the two-axis sorting method",
        "Explain why misdiagnosis wastes treatment",
        "No diagnostic language anywhere in the record",
    ],
    standards=["Emotion differentiation per Plutchik and Lazarus appraisal dimensions"],
    citations=[CIT_PLUTCHIK, CIT_LAZARUS, CIT_SALOVEY],
    sig_lens=(
        "The Signature lens reads the neighborhood as the lands around "
        "the fortress: the envious village that covets the harvest, the "
        "cold watchtower of suspicion, the walled town of possessiveness "
        "that admits no traveler, the old battlefield of resentment, "
        "the burned granary of betrayal - and across the valley, the "
        "sunlit fields of trust, where the sentinel dozes because the "
        "roads have been safe for years. His method teaches the "
        "commander his maps: send evidence to the cold tower, boundary "
        "stones to the walled town, and harvesters to the envious "
        "village - and never mistake one land for another. Clearly "
        "labeled Signature-made, never presented as authentic public "
        "record."),
),
dict(
    key="jealousy_blends", name="Jealousy Blends: This Emotion Mixed with Four Others",
    group="Advanced", ladder_rank=33, ladder_tier="advanced",
    description=(
        "In the Plutchik tradition, complex states are dyads - two "
        "emotions blended - and jealousy forms vivid ones. Jealousy + "
        "fear = dread: the full record-8 blend, the cold undertow "
        "beneath the heat, rehearsal of the loss on endless loop. "
        "Jealousy + anger = righteous fury: the threat appraised as "
        "betrayal and unfairness, the approach urge armed - this is the "
        "blend behind the peak-hour confrontation, hot, certain, and "
        "loud. Jealousy + sadness = mournful clinging: the loss "
        "pre-grieved, the person already mourning a bond that still "
        "exists, tenderness and tears alternating with accusations - "
        "the blend most likely to be mistaken for depression. Jealousy "
        "+ love = fierce devotion: the guard dog and the treasure in "
        "one heart - intense protectiveness, grand gestures, the "
        "passionate conviction that the bond is worth any watch. Each "
        "blend has its own face (record 14's component method), its own "
        "body (record 10's signature, tilted), its own dialect (record "
        "23, with an accent), and its own best response: dread needs "
        "safety and steadiness, fury needs a cooled hour and plain "
        "speech, mournful clinging needs the present tense restored - "
        "the bond is here, now - and fierce devotion needs channeling "
        "into tending rather than guarding. Blends are the advanced "
        "course because real episodes are almost always blends; pure "
        "single-note jealousy is the textbook case, and life is not a "
        "textbook."),
    how_it_works=(
        "Blends follow the ingredient logic of record 2, with a second "
        "full emotion added to the base. The arithmetic is not simple "
        "addition: the added emotion reshapes the appraisal. Fear "
        "added to jealousy raises the threat prior and adds future "
        "rehearsal; anger added converts the unfairness appraisal from "
        "suspicion to verdict, which is why the fury blend feels so "
        "certain; sadness added shifts the time focus from threatened "
        "future to grieved present, producing the mourning quality; love "
        "added amplifies bond value, turning up every dial at once. The "
        "response logic follows the added partner: each blend's best "
        "response targets the addition, not the jealousy core - calm "
        "the fear in dread, cool the anger in fury, restore the present "
        "in mournful clinging, convert the guarding in fierce devotion. "
        "This is the general principle of blend work: name both "
        "partners, treat the loudest one first, and watch the whole "
        "mixture settle."),
    key_points=[
        "Jealousy + fear = dread: cold undertow, endless loss rehearsal; answer with safety and steadiness.",
        "Jealousy + anger = righteous fury: threat as verdict; answer with a cooled hour and plain speech.",
        "Jealousy + sadness = mournful clinging: pre-grieved loss; answer by restoring the present tense.",
        "Jealousy + love = fierce devotion: the guard dog and the treasure; channel guarding into tending.",
        "Blend-work principle: name both partners, treat the loudest first, watch the mixture settle.",
    ],
    requirements=[
        "Describe four blends with face, body, and dialect notes",
        "Give the tailored best response for each",
        "State the general blend-work principle",
        "No diagnostic language anywhere in the record",
    ],
    standards=["Emotion dyads per Plutchik's psychoevolutionary synthesis"],
    citations=[CIT_PLUTCHIK, CIT_SALOVEY, CIT_WHITE],
    sig_lens=(
        "The Signature lens reads the blends as the sentinel joined by "
        "allies at the wall: the scout who has dreamed the city's fall "
        "(dread), the captain with his blade half-drawn (fury), the "
        "widow already veiled for a husband still living (mournful "
        "clinging), and the gardener who loves the treasure so fiercely "
        "he paces its walls all night (fierce devotion). His method "
        "greets each ally by name and gives each their proper orders - "
        "for a wall held by four watchmen in confusion holds nothing, "
        "but four watchmen in concert hold everything. Clearly labeled "
        "Signature-made, never presented as authentic public record."),
),
dict(
    key="jealousy_full_simulation", name="Full Behavioral Simulation: Jealousy from Trigger to Resolution",
    group="Advanced", ladder_rank=34, ladder_tier="advanced",
    description=(
        "Scene one, the trigger: Maya is at a work dinner when her "
        "partner Daniel laughs - really laughs, head back - at something "
        "a new colleague, Priya, just said. The gut-drop lands before "
        "Maya has decided to feel anything (record 5). Her attention "
        "narrows; she watches the rest of the evening in frames (record "
        "14's tracking gaze, record 11's stillness). Scene two, the "
        "plateau: over the next three days Maya replays the laugh, "
        "notices Daniel texting more, and remembers that Priya joined "
        "the project Daniel is excited about - a classic trigger "
        "stacking with a changed pattern (records 18, 21). Sleep "
        "thins; the background-load dial rises (record 12). Scene "
        "three, the peak: on Thursday Maya asks, too casually, how "
        "Priya is doing - the dialect's disguised question (record 23). "
        "Daniel, tired, answers shortly; the shortness reads as guilt. "
        "The urge to check the phone rises like a tide (record 25's "
        "first rung). Scene four, the choice point: Maya catches the "
        "surge and names it - the alarm, the old rhyme of being the "
        "overlooked middle child (record 19), the three dials all "
        "running high. She runs the two-column evidence habit (record "
        "28): what happened - a laugh, some texts; what she is adding - "
        "an affair, a replacement. She waits the night out (record 24's "
        "rule). Scene five, the resolution: Friday evening, calm hour, "
        "plain speech (record 26): 'I felt jealous at dinner when you "
        "laughed with Priya, and I've been spinning since. I don't "
        "think anything happened; I wanted you to know where I've "
        "been.' Daniel listens, names Priya plainly - new on the team, "
        "funny, nothing more - and they keep the Friday ritual they "
        "have protected for years (record 30). The alarm does not "
        "vanish; it quiets, the way a watchman stands down at dawn. "
        "This is the archive's showcase: every record in the database, "
        "walking one ordinary week from trigger to resolution - proof "
        "that the machinery described here is not theory but a map of "
        "real weather, and that maps are for navigating."),
    how_it_works=(
        "The simulation is a worked integration of the whole database: "
        "each scene exercises specific records, cited inline, so the "
        "reader can trace every beat back to its mechanism. Scene one "
        "runs the five-beat sequence (record 1) and the first-person "
        "storm (record 5) with the face and posture records visible. "
        "Scene two runs the cascade (record 21) across days rather than "
        "hours, with the sleep/appetite tax (record 12) raising the "
        "dials. Scene three stages the dialect (record 23) and the "
        "escalation ladder's first rung (record 25) as the choice "
        "point. Scene four is the intervention suite: naming (record "
        "5), the trigger map (record 19), the evidence habit and the "
        "waiting rule (records 28, 24). Scene five performs healthy "
        "expression (record 26) and the supporter's steadiness (record "
        "30). The simulation's educational function is transfer: a "
        "reader who has walked Maya's week can recognize their own "
        "Tuesday in it, name the scene they are in, and reach for the "
        "matching record's tools - which is the entire purpose of the "
        "archive."),
    key_points=[
        "Five scenes: trigger, plateau, peak, choice point, resolution - one ordinary week.",
        "Every beat traces back to a specific record's mechanism, cited inline.",
        "The choice point is the whole database in miniature: naming, trigger map, evidence habit, waiting rule.",
        "Resolution comes through plain speech at a calm hour, not through the alarm being obeyed.",
        "The simulation's function is transfer: recognize your own Tuesday, name the scene, reach for the tools.",
    ],
    requirements=[
        "Five scenes from trigger through resolution",
        "Cite the operative records inline per scene",
        "Use fictional characters, no real people",
        "No diagnostic language; general safe guidance only",
    ],
    standards=["Integrative case simulation per Lazarus and White and Mullen frameworks"],
    citations=[CIT_LAZARUS, CIT_WHITE, CIT_PINES],
    sig_lens=(
        "The Signature lens reads Maya's week as the sentinel's "
        "complete campaign: the horn at the feast, the long watch, the "
        "near-charge at midnight, the dawn report delivered plainly, "
        "and the standing down. His method holds this week as the "
        "proof of the whole teaching: the sentinel kept his post, "
        "questioned his own alarm, spoke truly at the true hour, and "
        "the treasure was never in danger - it was only ever loved. "
        "That is the watchman's whole art, and this archive's. "
        "Clearly labeled Signature-made, never presented as authentic "
        "public record."),
),
]
