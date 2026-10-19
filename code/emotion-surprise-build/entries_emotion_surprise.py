#!/usr/bin/env python3
"""Entries for The Surprise Emotion Database (emotion-surprise / -signature).

Manon's 2026-10-17 16:15 order: one database per emotion. The archive must be
able to describe or simulate emotions and human behavior. Shared 34-record
spec: what the emotion IS -> first-person simulation -> body signals ->
facial expression -> triggers -> behavior -> healthy expression ->
recognizing it in others -> related emotions and mixes -> full behavioral
simulation. DESCRIPTIVE/EDUCATIONAL ONLY - never diagnoses real people, never
labels any real person with an emotional state, never offers therapeutic
advice beyond general safe everyday guidance.

Public edition: real, fact-checked psychology knowledge about surprise -
basic-emotion theory (Ekman, Plutchik), appraisal theory (Lazarus, Scherer),
circumplex models (Russell), facial expression research (Ekman and Friesen
FACS), startle and orienting-response neuroscience (Panksepp, LeDoux),
expressed in plain human-readable sentences and paragraphs.

Signature edition: the same teaching ladder through the Signature lens -
surprise read as the Signature Signal Bell, the mind's early-warning
instrument: novelty is incoming data, the body is the alarm panel, and the
healthy response is to let the bell ring, read the message, and choose the
next move. src 'signature', titles suffixed ' (Signature Edition)', clearly
labeled Signature-made, never presented as authentic public record.

Screening: nothing hate-adjacent, nothing profane, nothing inappropriate, no
religious talk. Every record is the FULL fully-formed entry, never a stub.
Records are ladder-ordered (ladder_rank 1-10 non-decreasing, tiers
foundations/compounded/advanced).
"""

SIG_TAIL = ("Signature original - his original Signature lens on the human "
            "emotional system: surprise as the Signal Bell of the mind, the "
            "early-warning instrument that turns novelty into data. Clearly "
            "labeled Signature-made, never presented as authentic public "
            "record.")

CIT_EKMAN = ("Ekman P. An argument for basic emotions. Cognition and "
             "Emotion 1992;6(3-4):169-200.")
CIT_PLUTCHIK = ("Plutchik R. Emotion: A Psychoevolutionary Synthesis. "
                "Harper and Row; 1980.")
CIT_EKMAN_FRIESEN = ("Ekman P, Friesen WV. Facial Action Coding System "
                     "(FACS). Consulting Psychologists Press; 1978.")
CIT_LAZARUS = ("Lazarus RS. Emotion and Adaptation. Oxford University "
               "Press; 1991.")
CIT_SCHERER = ("Scherer KR. Appraisal considered as a process of multilevel "
               "sequential checking. In: Scherer KR, Schorr A, Johnstone T "
               "(eds). Appraisal Processes in Emotion. Oxford University "
               "Press; 2001:92-120.")
CIT_RUSSELL = ("Russell JA. A circumplex model of affect. Journal of "
               "Personality and Social Psychology 1980;39(6):1161-1178.")
CIT_PANKSEPP = ("Panksepp J. Affective Neuroscience. Oxford University "
                "Press; 1998.")
CIT_SOKOLOV = ("Sokolov EN. Higher nervous functions: the orienting "
               "reflex. Annual Review of Physiology 1963;25:545-580.")
CIT_SCHACHTER = ("Schachter S, Singer JE. Cognitive, social, and "
                 "physiological determinants of emotional state. "
                 "Psychological Review 1962;69(5):379-399.")
CIT_BARRETT = ("Barrett LF. How Emotions Are Made. Houghton Mifflin "
               "Harcourt; 2017.")
CIT_LEDOUX = ("LeDoux JE. The Emotional Brain. Simon and Schuster; 1996.")
CIT_GROSS = ("Gross JJ. Emotion regulation: affective, cognitive, and "
             "social consequences. Psychophysiology 2002;39(3):281-291.")

SIG_LENS_BELL = ("Through the Signature lens, surprise is the mind's Signal "
                 "Bell - the early-warning instrument of the Signature "
                 "system. The bell does not judge; it announces. The body is "
                 "its alarm panel, the face its beacon, and the healthy "
                 "response is the Signature habit: let it ring, read the "
                 "message, then choose the next move on purpose.")

ENTRIES = [
    # -------------------------------------------------- WHAT SURPRISE IS
    {
        "key": "def1",
        "name": "What Surprise Is: A Plain-Language Definition",
        "group": "What Surprise Is",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Surprise is the feeling you get when the world does something you did not see coming. "
            "It is the shortest of the basic emotions - often over in a second or two - and it is "
            "the brain's way of hitting the brakes on whatever you were doing so you can pay "
            "attention to something new. A phone rings and you jump. A friend jumps out from behind "
            "a door and you gasp. Someone tells you news you never expected and for a moment your "
            "mind goes blank. That blank, open moment is surprise doing its job.\n\n"
            "Psychologists describe surprise as an emotion of novelty and mismatch. Your brain is "
            "always predicting what happens next - the next word in a sentence, the next step on a "
            "familiar staircase, the next thing a friend will say. When reality breaks the "
            "prediction, surprise fires. The bigger the break between what you expected and what "
            "actually happened, the bigger the surprise. A slightly different ringtone is a small "
            "surprise. Winning a prize you never entered is a huge one.\n\n"
            "Surprise is special among emotions because it has no fixed feeling attached to it. "
            "Happiness feels good and sadness feels bad, but surprise can be either. A surprise "
            "party feels wonderful; a sudden loud bang feels terrible. Surprise is neutral at its "
            "core - it is the alert before the verdict. That is why surprise so often arrives in "
            "pairs, blending with joy, fear, anger, or amusement in the seconds after the shock.\n\n"
            "Another defining trait is that surprise is brief and honest. It rises faster than "
            "almost any other emotion and fades fast too, usually within seconds. Because it "
            "appears so quickly, it is very hard to fake or hide: the face shows it before a person "
            "can decide to cover it. Researchers have long treated surprise as one of the small "
            "set of basic emotions found in people everywhere, because its trigger - the "
            "unexpected - and its signature face - wide eyes, raised brows, open mouth - show up "
            "in every culture studied."
        ),
        "how_it_works": (
            "Surprise unfolds like a doorbell circuit with three stages. First comes the "
            "mismatch: the brain compares incoming sensory data against its prediction and "
            "finds a gap. This comparison happens in milliseconds, below conscious awareness - "
            "your ears hear the pop before your mind has a name for it. Second comes the "
            "interruption: attention is yanked off whatever it was doing and pointed at the "
            "new thing. Ongoing plans, speech, and movement pause - the famous freeze of "
            "surprise. Third comes the appraisal: the brain asks, good or bad, big or small, "
            "what do I do now. This third stage is where surprise hands off to its partner "
            "emotions. If the news is good, joy rushes in; if it is threatening, fear takes "
            "over; if it is harmless and funny, amusement follows. In a scenario, imagine a "
            "quiet kitchen, a pot lid rattling, then a loud pop from the microwave: the ears "
            "register the pop, the body freezes mid-step, the eyes widen toward the sound, and "
            "within a second the mind decides it was just popcorn - surprise dissolves into "
            "relief and a small laugh. That is the whole circuit, mismatch to verdict, in "
            "about three seconds."
        ),
        "key_points": [
            "Surprise is the brain's response to a broken prediction - novelty is its trigger.",
            "It is one of the shortest-lived basic emotions, typically seconds, not minutes.",
            "Surprise itself is neutral - good or bad arrives with the partner emotion that follows.",
            "It interrupts attention and freezes ongoing action so the new thing can be evaluated.",
            "The expression - wide eyes, raised brows, open mouth - is recognized across cultures.",
            "Its strength grows with the gap between expectation and reality.",
        ],
        "requirements": [
            "No prior psychology background needed - everyday examples carry the idea.",
            "Notice one small surprise in your own day to anchor the definition.",
            "Separate the shock itself from what you felt right after it.",
        ],
        "standards": [
            "Basic-emotion theory (Ekman): surprise as a pan-cultural basic emotion.",
            "Appraisal theory: novelty and mismatch as the appraisal behind surprise.",
            "Orienting response (Sokolov): the interrupt-and-attend function.",
        ],
        "citations": [CIT_EKMAN, CIT_SCHERER, CIT_SOKOLOV],
        "sig_lens": (
            SIG_LENS_BELL + " At the plainest level, the bell is a broken-prediction detector. "
            "Every surprise is the system flagging one line in its map of the world and saying, "
            "'this line is wrong - redraw it.'"
        ),
    },
    {
        "key": "family",
        "name": "Where Surprise Sits in the Emotion Family",
        "group": "What Surprise Is",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "If emotions are a family, surprise is the quick-witted messenger child - the one who "
            "bursts into the room with news and then lets the grown-ups take over. Psychologists "
            "group the basic emotions into a small set - happiness, sadness, fear, anger, disgust, "
            "and surprise - and surprise sits among them as the only one without a home on the "
            "pleasant-to-unpleasant axis. The others each lean toward good or bad; surprise stands "
            "in the middle, ready to tip either way.\n\n"
            "On Robert Plutchik's famous emotion wheel, surprise sits directly opposite "
            "anticipation. That pairing tells a story: anticipation is the mind reaching forward "
            "into the future, and surprise is what happens when the future arrives wearing a "
            "different face. The two are opposites the way an exhale is the opposite of an "
            "inhale - one predicts, the other reports that the prediction failed. When surprise "
            "blends with its neighbors on the wheel, it forms named mixes: surprise plus joy "
            "makes delight, surprise plus fear makes alarm, surprise plus sadness makes "
            "disappointment.\n\n"
            "Surprise also has a special relationship with fear and with curiosity. Fear is "
            "surprise's closest sibling in the body - both speed the heart, widen the eyes, and "
            "ready the muscles - which is why a startled person can feel afraid for a second "
            "even when there is nothing to fear. Curiosity is surprise's friendlier twin: the "
            "same novelty that startles can also attract, if the mind decides the new thing is "
            "interesting rather than dangerous. A strange sound in the dark is fear-flavored; a "
            "strange sound in a museum is curiosity-flavored. The raw material is the same "
            "surprise - the verdict differs.\n\n"
            "Researchers sometimes call surprise an 'epistemic' emotion - one tied to knowing. "
            "Like curiosity and confusion, it is about the gap between what we know and what is "
            "happening. That is why surprise is so central to learning: the moment of 'wait, "
            "what?' is the moment the brain opens a new file. Teachers, storytellers, and game "
            "designers all work with this on purpose, arranging small surprises so attention "
            "stays awake and memory sticks."
        ),
        "how_it_works": (
            "Picture the emotion family as a map with two axes: pleasant-to-unpleasant running "
            "left to right, and calm-to-energized running bottom to top. Happiness sits right "
            "and up; sadness sits left and down; fear sits left and up. Surprise sits at the "
            "top center - high energy, zero pleasantness, a perfect vertical. From that spot it "
            "can slide in any direction within a second: down-right into delighted laughter, "
            "down-left into fear, sideways into anger if the surprise is an insult. In a "
            "scenario, a person hears an unexpected knock at midnight: raw surprise spikes at "
            "top-center, then the appraisal engine slides the dot - if it is a friend with good "
            "news, the dot glides right into joy; if it is a stranger pounding, it dives left "
            "into fear. The map explains why surprise feels so changeable: it is the one "
            "emotion parked exactly at the crossroads."
        ),
        "key_points": [
            "Surprise is a basic emotion with no fixed pleasantness - it is the neutral one.",
            "On Plutchik's wheel it sits opposite anticipation: prediction vs prediction-failure.",
            "Fear is its closest bodily sibling; curiosity is its friendly twin.",
            "Named blends: delight (surprise+joy), alarm (surprise+fear), disappointment (surprise+sadness).",
            "It is an epistemic emotion - tied to knowing - which makes it central to learning.",
        ],
        "requirements": [
            "Picture the two-axis emotion map with surprise at top center.",
            "Notice which partner emotion your own surprises usually hand off to.",
        ],
        "standards": [
            "Basic-emotion theory (Ekman): surprise among the basic set.",
            "Plutchik's psychoevolutionary wheel: dyads and opposites.",
            "Circumplex model (Russell): valence-arousal placement.",
        ],
        "citations": [CIT_EKMAN, CIT_PLUTCHIK, CIT_RUSSELL],
        "sig_lens": (
            SIG_LENS_BELL + " On the family map, the bell hangs at the crossroads of the "
            "system - every road out of surprise leads to a different department, and the "
            "Signature reader learns to watch which road the dot slides down."
        ),
    },
    {
        "key": "volumes",
        "name": "Mild, Moderate, Intense: The Volume of Surprise",
        "group": "What Surprise Is",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Surprise comes in volumes, the way sound does. At the lowest volume it is barely a "
            "ripple: you notice the coffee shop rearranged its chairs, and for half a second "
            "your step hesitates. Nobody would call that a big emotional event - but it is the "
            "same machinery running quietly. Mild surprise is the brain's routine correction, "
            "the small edit it makes to its map dozens of times a day without asking your "
            "permission.\n\n"
            "Moderate surprise is the everyday kind people mean when they say 'that surprised "
            "me.' A colleague says something you did not expect. A plot twist lands in a "
            "movie. Your name is called when you were sure you were unnoticed. The body "
            "reacts - eyebrows lift, breath catches, a small sound escapes - and the mind "
            "needs a beat to reorganize. This is the volume at which surprise starts to be "
            "memorable: the moderate surprises of a day are the ones you tell other people "
            "about later.\n\n"
            "Intense surprise is a full-system event. The startle at a thunderclap, the shock "
            "of life-changing news, the gasp when a car swerves into your lane - the body "
            "floods with adrenaline, the face opens wide, the mind can go blank for whole "
            "seconds. Intense surprise can knock the wind out of a person, literally: the "
            "gasp reflex snatches a sharp breath. It can also briefly erase memory of the "
            "moments right before, because attention was so fully captured by the new event "
            "that the recorder stopped writing.\n\n"
            "What sets the volume is mostly the size of the prediction gap - how far reality "
            "landed from expectation - multiplied by how much was at stake. A huge gap about "
            "something trivial (a friend jumping out to say boo) startles loudly but fades "
            "fast. A medium gap about something that matters (an unexpected medical result) "
            "can ring for hours. And the same event hits different volumes in different "
            "people, because predictions are personal: the lifelong city dweller and the "
            "country visitor hear the same midnight siren at very different volumes."
        ),
        "how_it_works": (
            "Think of surprise volume as a three-dial panel. Dial one is novelty: how far the "
            "event was from prediction, from 'slightly off' to 'impossible until a second ago.' "
            "Dial two is significance: how much the event matters - a surprise about dinner "
            "plans vs a surprise about a loved one's safety. Dial three is suddenness: how "
            "fast it arrived, from a slow-dawning realization to a bang with no warning. "
            "Multiply the three and you get the felt volume. In a scenario, two people hear "
            "the same unexpected announcement at work - 'the office is moving.' For the "
            "person who heard rumors (low novelty), it is a mild ripple. For the person who "
            "signed a new lease nearby (high significance), it is intense. The announcement is "
            "identical; the dials are personal, so the volumes differ."
        ),
        "key_points": [
            "Mild surprise is the brain's quiet routine correction, happening dozens of times daily.",
            "Moderate surprise freezes the body briefly and becomes a story you tell later.",
            "Intense surprise floods the body with adrenaline and can blank short-term memory.",
            "Volume = size of prediction gap x significance x suddenness.",
            "The same event lands at different volumes for different people.",
        ],
        "requirements": [
            "Recall one mild, one moderate, and one intense surprise from your own life.",
            "Ask which of the three dials was turned highest in each.",
        ],
        "standards": [
            "Appraisal theory: novelty and goal-relevance as intensity drivers.",
            "Arousal models: physiological scaling with stimulus significance.",
        ],
        "citations": [CIT_SCHERER, CIT_LAZARUS],
        "sig_lens": (
            SIG_LENS_BELL + " The bell has a volume knob, and the Signature reader learns to "
            "read the knob before reacting - a loud bell about a small matter deserves a small "
            "response, whatever the body is shouting."
        ),
    },
    {
        "key": "myths",
        "name": "Myths and Misunderstandings About Surprise",
        "group": "What Surprise Is",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Myth one: surprise is always pleasant or always unpleasant. People argue about "
            "whether surprises are 'good' - surprise parties versus nasty shocks - but the "
            "research picture is clear: surprise itself is neutral. The pleasantness comes "
            "from whatever the surprise turns out to be. Treating all surprises as threats "
            "makes a person flinch at birthday parties; treating all surprises as treats "
            "makes a person slow to dodge real danger. The accurate view is the flexible one: "
            "surprise is the alert, and the verdict comes after.\n\n"
            "Myth two: being easily surprised means something is wrong with you. Startle "
            "sensitivity varies enormously and mostly reflects wiring, sleep, stress, and "
            "history - not character. A person running on three hours of sleep startles at "
            "everything; so does a person whose past taught them that sudden sounds meant "
            "trouble. Neither is broken. The threshold moves with the state of the nervous "
            "system, and it moves back.\n\n"
            "Myth three: surprise means you were not paying attention. In fact surprise is "
            "proof that attention was working: the brain can only be surprised by what it was "
            "actively predicting. You cannot be surprised by a language you do not speak, "
            "because you had no prediction to break. The expert is surprised by the subtle "
            "anomaly the beginner never noticed. Being surprised often means you knew enough "
            "to have an expectation.\n\n"
            "Myth four: you can fully control or suppress surprise. Because the first burst "
            "fires in milliseconds, before conscious control comes online, the honest answer "
            "is no - not the first half-second. What can be trained is everything after: the "
            "recovery, the appraisal, the response. Soldiers, athletes, and emergency workers "
            "do not stop being surprised; they get faster at the second half - the calm "
            "evaluation and the chosen action that follow the unavoidable jolt."
        ),
        "how_it_works": (
            "Each myth gets tested the same way: state the claim, check it against the "
            "mismatch model, and watch it fail. Claim: 'surprises are bad.' Test: a surprise "
            "birthday party and a surprise tax bill use the identical interrupt-and-attend "
            "circuit in the first half-second - the difference is the appraisal that follows, "
            "not the surprise itself. Claim: 'easy startle means weakness.' Test: measure the "
            "same person's startle after a full night's sleep vs after a night shift - the "
            "threshold moves with fatigue, which is a state, not a trait. In a teaching "
            "scenario, a trainer has a student list their beliefs about surprise, then walks "
            "them through a real recent surprise asking 'what was the mismatch, what was the "
            "appraisal, what came half a second later' - and the myths dissolve because the "
            "student can now see the machinery for themselves."
        ),
        "key_points": [
            "Surprise is neutral - pleasantness comes from the appraisal that follows.",
            "Startle sensitivity is a moving state (sleep, stress, history), not a character trait.",
            "Being surprised proves prediction was working, not that attention failed.",
            "The first half-second cannot be suppressed; the recovery can be trained.",
        ],
        "requirements": [
            "Pick one surprise myth you have believed and test it against a real memory.",
            "Separate the shock from the verdict in that memory.",
        ],
        "standards": [
            "Basic-emotion theory: valence-neutrality of surprise.",
            "Startle-reflex literature: state-dependence of thresholds.",
            "Emotion-regulation research: control of response vs control of onset.",
        ],
        "citations": [CIT_EKMAN, CIT_GROSS, CIT_LEDOUX],
        "sig_lens": (
            SIG_LENS_BELL + " The myths are all the same error: blaming the bell for the "
            "news. The Signature habit is to thank the bell for ringing and then read the "
            "message with clear eyes."
        ),
    },
    # -------------------------------------------------- HOW IT FEELS
    {
        "key": "firstperson",
        "name": "Inside Surprise: A First-Person Passage",
        "group": "How It Feels",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "From the inside, surprise feels like the world skipping a frame. One moment you are "
            "mid-thought, mid-step, mid-sentence - and then there is a tiny blank, a hitch in "
            "the film. Your breath catches without asking. Your eyes go wide on their own, as "
            "if trying to take in more of whatever just happened. For a second or two there "
            "are no words in your head at all, just a bright, buzzing alertness, like a room "
            "where every light just flicked on at once.\n\n"
            "Then the questions arrive, all at once and out of order: what was that, where did "
            "it come from, am I okay, what does this mean. The mind scrambles to catch up with "
            "the senses, which got there first. If the surprise is small - a phone buzzing when "
            "you expected silence - the passage is a flicker: hitch, glance, shrug, resume. If "
            "it is large, the inner monologue stutters. Thoughts arrive half-formed. You might "
            "hear yourself say something involuntary - a gasp, a laugh, a name, a nonsense word - "
            "because the careful, edited speaker in your head has not rebooted yet.\n\n"
            "Underneath it all is a strange double feeling: exposure and aliveness at once. "
            "Exposure, because your map of the moment just tore and you are standing in the "
            "tear. Aliveness, because every sense is suddenly turned all the way up - colors "
            "sharper, sounds louder, skin more awake. People often describe intense surprise "
            "as time slowing down, and in a way it does: attention samples the world faster "
            "during those seconds, so more gets packed into each moment, and the memory of it "
            "feels stretched.\n\n"
            "Finally there is the landing. The mind finds its footing - 'oh, it is just the "
            "cat,' 'oh, we won,' 'oh no' - and the partner emotion moves in to take the room: "
            "relief, joy, fear, laughter. The surprise itself is already gone by then. What "
            "you remember afterward is mostly the landing, not the fall - but the fall, that "
            "bright blank second, is the feeling this passage is about."
        ),
        "how_it_works": (
            "Walk it second by second. Second zero: the trigger - a balloon pops behind you at "
            "a party. Milliseconds 0-200: the mismatch registers; breath snatches; the body "
            "freezes mid-gesture. Milliseconds 200-500: eyes widen and turn toward the sound; "
            "brows lift; mouth opens slightly; the inner monologue is still blank - there are "
            "no words yet, only alertness. Seconds 1-2: the questions flood in - what, where, "
            "danger? - and the senses report back: latex smell, laughing faces, no threat. "
            "Seconds 2-4: appraisal lands - harmless prank - and amusement rushes into the "
            "space surprise vacated; you laugh, maybe shaky. Seconds 5+: the body settles, "
            "heart rate easing, and the story of it begins forming: 'you should have seen my "
            "face.' The whole passage runs the same track every time; only the landing "
            "changes."
        ),
        "key_points": [
            "Inside, surprise is a bright blank - a hitch where words stop for a second.",
            "Senses arrive before thoughts; the body reacts before the mind names it.",
            "Time feels stretched because attention samples faster during the alert.",
            "The landing - relief, joy, fear, laughter - is what memory keeps, not the fall.",
            "Involuntary sounds escape because the edited inner speaker has not rebooted yet.",
        ],
        "requirements": [
            "Read the passage slowly and match it against one real memory of being startled.",
            "Notice the order: senses first, questions second, verdict last.",
        ],
        "standards": [
            "Phenomenology of emotion: first-person report as data.",
            "Orienting response: attentional capture and sampling-rate increase.",
        ],
        "citations": [CIT_SOKOLOV, CIT_BARRETT],
        "sig_lens": (
            SIG_LENS_BELL + " The Signature reader practices visiting this passage on purpose - "
            "replaying the bright blank second - until the hitch itself feels familiar instead "
            "of frightening. A bell you have heard before is easier to answer calmly."
        ),
    },
    {
        "key": "timecourse",
        "name": "Onset, Peak, Fade: How Surprise Moves Through Time",
        "group": "How It Feels",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Surprise has one of the fastest onsets of any emotion. From trigger to full "
            "expression takes roughly two to five tenths of a second - faster than a blink's "
            "decision, faster than any deliberate movement. The startle reflex, surprise's "
            "bodily cousin, can begin in as little as 20 to 50 milliseconds after a sudden "
            "loud sound. By the time you have consciously registered 'that was loud,' your "
            "eyelids have already blinked, your shoulders have already hunched, and your "
            "breath has already caught. The emotion is already at full volume before the mind "
            "has finished hearing the news.\n\n"
            "The peak is brief. Full surprise - the wide-eyed, open-mouthed, frozen moment - "
            "typically lasts one to three seconds. This is not a flaw; it is the design. "
            "Surprise is an interrupt, and an interrupt that lingers would be a malfunction. "
            "Its job is to stop the current program and hand control to the appraisal system, "
            "and the handoff is meant to be fast. Anything still going strong after five "
            "seconds is no longer surprise - it is whatever surprise handed off to: fear, "
            "anger, joy, confusion.\n\n"
            "The fade has two parts. First the body stands down: the heart rate that spiked "
            "begins to ease, the held breath releases, the frozen muscles unlock. This takes "
            "seconds to a minute. Then comes the aftershock: a lingering alertness, a "
            "readiness to startle again at the next small thing. After a big scare, a dropped "
            "spoon can make you jump - the threshold has been temporarily lowered, the system "
            "left on high alert until it is convinced the world is predictable again. The "
            "aftershock can last minutes to hours, long after the surprise itself is gone.\n\n"
            "Repetition changes the curve. The tenth identical pop startles less than the "
            "first - the brain updates its prediction, and the mismatch shrinks. This "
            "habituation is why surprise is self-extinguishing: every surprise teaches the "
            "brain, and the lesson makes the next identical event less surprising. The curve "
            "also explains why interrupted surprises feel so strange: if the trigger vanishes "
            "before appraisal finishes - a sound with no source found - the system stays "
            "revved with nowhere to land, and the aftershock stretches."
        ),
        "how_it_works": (
            "Run the timeline of a dropped tray in a quiet restaurant. T-zero: the crash. "
            "Plus 30 milliseconds: the startle reflex fires - blink, hunch. Plus 300 "
            "milliseconds: full surprise expression - head turns, eyes widen, breath catches; "
            "the diner is frozen mid-bite. Plus 1-2 seconds: peak - the mind's questions "
            "arrive, eyes locate the fallen tray, appraisal begins. Plus 3-5 seconds: the "
            "verdict - no danger, just noise - and relief or amusement moves in; the body "
            "unlocks, a breath releases, maybe a sympathetic wince. Plus 30 seconds: heart "
            "rate settling, conversation resuming. Plus 10 minutes: the aftershock - a chair "
            "scrapes and the diner flinches slightly, the threshold still lowered. By the "
            "next visit to the same restaurant, the curve is already flatter: the brain has "
            "filed 'trays sometimes drop here,' and the mismatch - and the surprise - shrinks."
        ),
        "key_points": [
            "Onset takes 0.2-0.5 seconds; the startle reflex can begin in 20-50 ms.",
            "The peak lasts 1-3 seconds - anything longer is the handoff emotion, not surprise.",
            "Fade has two parts: bodily stand-down (seconds) and aftershock alertness (minutes to hours).",
            "Repetition habituates: the brain updates its prediction and the mismatch shrinks.",
            "Interrupted surprises leave the system revved with nowhere to land.",
        ],
        "requirements": [
            "Time one real surprise in memory: trigger, freeze, verdict, settle.",
            "Notice whether an aftershock followed and how long it lasted.",
        ],
        "standards": [
            "Startle-reflex latency literature (20-50 ms acoustic startle).",
            "Emotion time-course models: onset-peak-offset decomposition.",
            "Habituation: prediction-update accounts of diminished response.",
        ],
        "citations": [CIT_LEDOUX, CIT_SOKOLOV, CIT_SCHERER],
        "sig_lens": (
            SIG_LENS_BELL + " The Signature reader times the bell: ring (milliseconds), "
            "message (seconds), echo (minutes). Knowing the echo is normal keeps a person from "
            "mistaking aftershock for a second emergency."
        ),
    },
    {
        "key": "lowhigh",
        "name": "A Whisper vs a Thunderclap: Low and High Intensity Surprise",
        "group": "How It Feels",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Low-intensity surprise is a whisper the mind barely notices it heard. You reach "
            "for the light switch in a familiar hallway and it is not quite where your hand "
            "expected - a half-second of blankness, a tiny correction, and you are already "
            "moving on. The body barely joins in: maybe the eyebrows flicker, maybe the step "
            "falters. There is no story to tell afterward. Yet these whispers are the most "
            "common surprises in a human life, and they do quiet, constant work - each one a "
            "small edit to the brain's map, keeping it accurate without drama.\n\n"
            "High-intensity surprise is a thunderclap that takes the whole system. The classic "
            "laboratory version is the sudden 100-decibel burst: heart rate leaps, palms sweat, "
            "muscles brace, the face opens wide, and thought can blank completely for a beat. "
            "In real life the thunderclaps are the phone call with impossible news, the car "
            "appearing from nowhere, the lottery ticket that turns out to be real. The body "
            "responds as if to a threat first and asks questions later - adrenaline first, "
            "appraisal second - because at high intensity the system cannot afford to wait for "
            "the verdict before preparing.\n\n"
            "The lived difference is not just volume but texture. Low surprise feels like a "
            "hiccup in the smooth film of the day - noticeable, slightly interesting, gone. "
            "High surprise feels like being picked up and set down somewhere else: "
            "disorienting, total, and followed by a period of reassembly where the person "
            "checks the world is still the world. Low surprise updates a line in the map; "
            "high surprise can redraw the page. People often laugh after low surprises and "
            "shake after high ones - the body discharging the different amounts of mobilized "
            "energy.\n\n"
            "Between them lies a useful middle most people can learn to read. The moderate "
            "surprises - the unexpected guest, the plot twist, the changed plan - are where "
            "choice lives. At whisper volume there is nothing to choose; at thunderclap "
            "volume choice arrives late. In the middle, a person can feel the jolt and still "
            "steer the landing - which is exactly the skill this archive is built to teach."
        ),
        "how_it_works": (
            "Two snapshots, side by side. Snapshot one, whisper: Maya reaches for her usual "
            "mug and finds a different one - someone washed the dishes and rearranged the "
            "shelf. Her hand pauses a quarter-second; her brows lift a millimeter; she "
            "thinks 'oh, new spot,' and pours. Total event time: two seconds. No heart-rate "
            "change worth naming. Snapshot two, thunderclap: Maya is driving and a truck "
            "blows a tire beside her with a cannon-crack. Her hands clamp the wheel, her "
            "breath snatches, her vision tunnels to the truck, her heart hammers at 130, "
            "and for two full seconds there is no thought at all - only the body driving. "
            "Then appraisal: the truck holds its lane, danger passes, and her hands start to "
            "tremble as the adrenaline has nowhere to go. Same emotion, same circuit; the "
            "dials - novelty, significance, suddenness - were set to opposite ends."
        ),
        "key_points": [
            "Whisper surprises are tiny map-edits; thunderclaps are full-system events.",
            "Low intensity: a flicker of brows, a paused hand, no story afterward.",
            "High intensity: adrenaline first, appraisal second - the body prepares before the verdict.",
            "After low surprises people laugh; after high ones they shake - discharging mobilized energy.",
            "The middle volumes are where steering the landing is still possible.",
        ],
        "requirements": [
            "Place your own recent surprises on the whisper-to-thunderclap line.",
            "Notice the different textures: hiccup vs being picked up and set down.",
        ],
        "standards": [
            "Arousal continuum models: intensity scaling of autonomic response.",
            "Startle literature: graded response with stimulus intensity.",
        ],
        "citations": [CIT_LEDOUX, CIT_RUSSELL],
        "sig_lens": (
            SIG_LENS_BELL + " Whisper or thunderclap, the bell is the same bell - only the "
            "hammer differs. The Signature reader answers whispers with a note in the margin "
            "and thunderclaps with a full stop, a breath, and then a chosen move."
        ),
    },
    {
        "key": "mixfear",
        "name": "Surprise Mixed with Fear: The Most Common Blend",
        "group": "How It Feels",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "Ask people what their last big surprise felt like and most will describe fear - "
            "not because surprise is fear, but because the two arrive as a pair so often "
            "that memory fuses them. The pairing has a simple cause: the body's preparation "
            "for surprise and its preparation for fear are nearly identical. Both widen the "
            "eyes to take in more visual information. Both speed the heart and tense the "
            "muscles. Both freeze ongoing action. So when surprise fires, the body is already "
            "standing in fear's posture - and if the appraisal that follows finds anything "
            "threatening, fear walks straight in without knocking.\n\n"
            "From the inside, the blend feels like surprise with an edge. The bright blank "
            "of pure surprise gains a cold undertow: the stomach tightens, the breath gets "
            "shallow, the mind's questions turn from 'what was that' to 'am I safe.' A "
            "balloon popping at a party is pure surprise dissolving into laughter. The same "
            "pop heard alone at night in an unfamiliar house is surprise dissolving into "
            "fear - the pop is identical; the context steers the blend. This is why startle "
            "pranks can misfire so badly: the prankster ordered surprise, but the body "
            "delivered fear, and fear does not find pranks funny.\n\n"
            "The blend also explains the aftershock. Pure surprise fades in seconds, but "
            "surprise-with-fear leaves the threat system switched on: the person startles "
            "more easily, sleeps lightly, replays the moment. Each replay is the brain "
            "running the appraisal again, checking whether it missed a danger the first "
            "time. Understanding the blend gives a person a useful sentence for the "
            "moment: 'I am not in danger; I am surprised, and my body added fear on top.' "
            "Naming the layers does not erase them, but it stops the fear from borrowing "
            "surprise's speed to feel like a fact.\n\n"
            "There is a gentler cousin of this blend worth knowing: surprise mixed with "
            "excitement. The physiology is close - fast heart, wide eyes, buzzing alertness - "
            "but the appraisal reads 'opportunity' instead of 'threat.' Roller coasters, "
            "sports, and stage fright before a good performance all live here. The line "
            "between the fear blend and the excitement blend is thin and mostly made of "
            "context and control: the same drop feels like terror on a broken elevator and "
            "like thrill on a ride you chose."
        ),
        "how_it_works": (
            "Run the blend in a hallway scenario. Leo walks down a dark hallway; a door "
            "slams somewhere behind him. Millisecond 0-300: pure surprise - freeze, widened "
            "eyes, snatched breath. Second 1: appraisal begins, and the context feeds the "
            "blend - it is night, he is alone, the slam was close. The fear layer engages: "
            "stomach knots, breath shallows, muscles stay braced instead of releasing. "
            "Seconds 2-5: the questions are fear-flavored - 'who is there, am I safe' - and "
            "the body holds its readiness. Second 6: the wind slams the door again, visibly "
            "this time - appraisal updates to 'just the wind,' and the fear layer drains "
            "while the surprise layer has already been gone for seconds. What remains is "
            "the aftershock: Leo startles at the next small sound, laughs at himself, and "
            "sleeps with the hallway light on. The surprise lasted three seconds; the blend "
            "ran the evening."
        ),
        "key_points": [
            "Surprise and fear share nearly identical bodily preparation - the body stands in fear's posture already.",
            "Context steers the blend: the same pop is funny at a party, frightening alone at night.",
            "The blend explains the aftershock: the threat system stays on after surprise fades.",
            "Naming the layers - 'surprised, with fear on top' - keeps fear from feeling like fact.",
            "The excitement blend uses the same arousal with an 'opportunity' appraisal.",
        ],
        "requirements": [
            "Recall a surprise that turned frightening and find the moment the blend tipped.",
            "Practice the naming sentence: surprised first, fear second.",
        ],
        "standards": [
            "Two-factor theory (Schachter-Singer): arousal plus appraisal labels the feeling.",
            "Fear-potentiated startle: shared circuitry of surprise and fear.",
            "Appraisal theory: context as the blender.",
        ],
        "citations": [CIT_SCHACHTER, CIT_LEDOUX, CIT_SCHERER],
        "sig_lens": (
            SIG_LENS_BELL + " The bell rings the same for wind and for wolves - it is the "
            "watchman's report that differs. The Signature reader learns to ask, after every "
            "loud ring: was that the bell, or the watchman shouting on top of it?"
        ),
    },
    {
        "key": "dayinlife",
        "name": "A Day in the Life with Surprise",
        "group": "How It Feels",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "Follow surprise through an ordinary Tuesday and it turns out to be everywhere, "
            "quietly doing its job. The alarm sounds different - snoozed twice, a slightly "
            "wrong tone - and there is a half-second of 'what?' before the day starts. The "
            "shower runs cold for two seconds before the hot arrives: a small full-body "
            "flinch, a laugh, a note to fix the heater. The commute brings a road closed "
            "with no warning - a moderate surprise, the route replanned mid-drive, a flicker "
            "of annoyance as the partner emotion moves in. None of these make the diary. "
            "All of them are the mismatch detector earning its keep.\n\n"
            "Midday brings the social surprises. A coworker compliments work you thought "
            "went unnoticed - a warm little jolt, surprise blending with pleasure, the day "
            "brightening a shade. An email arrives with a subject line you did not expect - "
            "the stomach does its tiny drop before the mind has read a word. Someone tells "
            "a story with an ending you never saw coming and the table erupts - shared "
            "surprise is one of the great social glues, the collective gasp that says 'we "
            "are all in this moment together.'\n\n"
            "Evening brings the chosen surprises - the ones people seek out on purpose. The "
            "plot twist in the show, the game with the hidden level, the friend who texts "
            "'check your porch' and hangs up. Humans are novelty-seekers; a day with zero "
            "surprise feels flat and gray, and people pay good money for roller coasters, "
            "mystery novels, and surprise parties to fix that. The appetite for surprise is "
            "the appetite for aliveness - the same circuit that flinches at the cold shower "
            "delights in the plot twist.\n\n"
            "And through it all, the pattern holds: hitch, attention, appraisal, landing. "
            "The cold shower, the closed road, the compliment, the twist - each runs the "
            "same four beats at its own volume. A person who learns to notice the beats "
            "starts to see surprise not as interruption but as rhythm: the day's small "
            "syncopations, keeping the mind awake and the map current. The vignette's "
            "lesson is simple - surprise is not the exception in a day. It is the texture."
        ),
        "how_it_works": (
            "Tally the Tuesday. 6:42 AM: alarm tone wrong - whisper surprise, 1 second, "
            "appraisal 'snooze glitch,' landing: mild amusement. 7:15: cold shower - "
            "low-moderate, full-body flinch, landing: laughter. 8:30: road closed - moderate, "
            "route replan, landing: annoyance then acceptance. 12:10: unexpected compliment "
            "- moderate, warm jolt, landing: pleasure. 3:45: strange email subject - "
            "whisper, stomach flicker, landing: curiosity, email opened. 8:00 PM: plot twist "
            "- moderate-high, gasp, landing: delight, rewound to rewatch. 9:30: 'check your "
            "porch' - moderate, hallway dash, landing: joy, gift from a friend. Count: eight "
            "surprises, volumes from whisper to moderate-high, landings spanning amusement, "
            "annoyance, pleasure, curiosity, delight, and joy. The circuit ran eight times; "
            "the person never once thought the word 'surprise' until bedtime. That is the "
            "vignette's quiet point: the most important emotion of the day is the one nobody "
            "noticed."
        ),
        "key_points": [
            "An ordinary day holds many small surprises - the mismatch detector works constantly.",
            "Social surprises (compliments, stories, gasps) are bonding events.",
            "People deliberately seek surprise: twists, games, parties - novelty is an appetite.",
            "Every instance runs the same four beats: hitch, attention, appraisal, landing.",
            "A day with zero surprise feels flat; surprise is the texture of aliveness.",
        ],
        "requirements": [
            "Count your own surprises tomorrow - aim to catch at least five.",
            "Note each landing emotion; watch how varied the handoffs are.",
        ],
        "standards": [
            "Ecological emotion sampling: frequency of everyday affective events.",
            "Novelty-seeking and play: the appetitive side of surprise.",
        ],
        "citations": [CIT_PLUTCHIK, CIT_BARRETT],
        "sig_lens": (
            SIG_LENS_BELL + " The Signature reader keeps a bell-log for one Tuesday - every "
            "ring, every landing - and discovers the instrument was ringing all day. A "
            "well-kept bell is a well-kept map."
        ),
    },
    # -------------------------------------------------- BODY SIGNALS
    {
        "key": "body",
        "name": "What Happens in the Body During Surprise",
        "group": "Body Signals",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "Surprise is a whole-body event, and it starts before thought. The fastest "
            "response is the startle reflex: eyelids blink, the head jerks slightly "
            "forward, shoulders hunch, arms flex - a protective crouch assembled in "
            "milliseconds. This is ancient machinery, shared with most mammals, and it "
            "fires before the conscious mind has identified the trigger. The blink "
            "protects the eyes; the hunch protects the neck and torso; the arm flexion "
            "brings the hands up toward the face. The body defends first and identifies "
            "later.\n\n"
            "The heart joins within a beat or two. Heart rate jumps - often by 10 to 30 "
            "beats per minute in a strong startle - driven by a burst of adrenaline from "
            "the sympathetic nervous system. Blood pressure rises with it. Breathing "
            "changes in a characteristic way: a sharp intake, the gasp, sometimes followed "
            "by a held breath while attention locks on. The gasp is functional - it floods "
            "the lungs with air for whatever comes next, fight or flight or simply a "
            "closer look.\n\n"
            "The muscles tell the rest of the story. Ongoing movement freezes - the "
            "mid-step halt, the suspended spoon - because the motor system yields the floor "
            "to the sensory systems: stop moving so you can see and hear better. Then the "
            "muscles brace: jaw, neck, shoulders, and hands tense, ready to act on the "
            "appraisal's verdict. Skin responds too - goosebumps can rise, palms may sweat, "
            "and some people feel a wave of heat or a cold wash across the scalp and neck. "
            "The stomach often joins with the famous 'drop' - actually a brief shift in "
            "gut tension as blood is redirected toward the large muscles.\n\n"
            "Energy floods the system and then needs somewhere to go. Adrenaline mobilizes "
            "glucose; the body is fueled for action it may not take. If the appraisal says "
            "'harmless,' that mobilized energy discharges as laughter, trembling, or a "
            "shaky exhale - the familiar 'whew' after a false alarm. If the appraisal says "
            "'threat,' the energy feeds the fear response. Either way, the body of surprise "
            "is a body briefly converted into a coiled spring, and the seconds afterward "
            "are the spring either releasing or staying coiled."
        ),
        "how_it_works": (
            "Trace the signal path of a thunderclap. The sound hits the ears; the auditory "
            "nerve fires to the brainstem, which triggers the startle circuit before the "
            "signal even reaches conscious cortex - blink, hunch, arm flexion in under 50 "
            "milliseconds. Simultaneously the amygdala and hypothalamus wake the "
            "sympathetic system: adrenaline releases, heart rate climbs from 72 to 105, "
            "breathing snatches into the gasp. The motor cortex hits pause - the person "
            "freezes mid-step on the porch. Eyes widen and swivel toward the sound; pupils "
            "dilate to take in more light. Then the cortex catches up, identifies "
            "'thunder, distant, no danger,' and sends the stand-down: parasympathetic "
            "signals ease the heart back down, the held breath releases in a laugh, the "
            "shoulders drop. Total time from crack to laugh: about four seconds. The body "
            "ran a full emergency drill for a drill that turned out to be nothing - and "
            "that, the scenario shows, is exactly what the machinery is for."
        ),
        "key_points": [
            "The startle reflex fires in milliseconds: blink, hunch, arm flexion - defense before identification.",
            "Heart rate jumps 10-30 bpm; the gasp floods the lungs for whatever comes next.",
            "Movement freezes so the senses get the floor; then muscles brace for the verdict.",
            "Goosebumps, palm sweat, and the stomach 'drop' are blood and tension redirecting.",
            "Mobilized energy discharges as laughter or trembling when the verdict is 'harmless.'",
        ],
        "requirements": [
            "Recall your last gasp - what did your shoulders and hands do?",
            "Notice the freeze next time: what were you doing when it stopped?",
        ],
        "standards": [
            "Acoustic startle reflex: brainstem circuitry, 20-50 ms latency.",
            "Sympathetic activation: adrenaline, heart rate, and respiration changes.",
            "Orienting vs defense responses in the body.",
        ],
        "citations": [CIT_LEDOUX, CIT_SOKOLOV, CIT_PANKSEPP],
        "sig_lens": (
            SIG_LENS_BELL + " The body is the bell's alarm panel, and every light on it "
            "means something: the gasp is the intake light, the freeze is the hold light, "
            "the braced shoulders are the ready light. The Signature reader learns the "
            "panel until its signals read like plain text."
        ),
    },
    {
        "key": "posture",
        "name": "Posture and Movement: The Surprised Body",
        "group": "Body Signals",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "The surprised body has a signature shape, and it unfolds in two acts. Act one "
            "is the crouch: the chin tucks, the shoulders rise and roll forward, the arms "
            "bend with hands lifting toward the face or chest, the knees soften. This is "
            "the startle posture - the body's ancient turtle move, making the vital organs "
            "smaller targets and the head harder to strike. It is not a decision; people "
            "do it in their sleep when a loud noise hits. Watch slow-motion footage of a "
            "crowd hearing an unexpected bang and the whole crowd performs the same "
            "choreography at once.\n\n"
            "Act two is the orient: the freeze breaks, and the body turns toward the "
            "novelty. The head swivels, the torso follows, the eyes lead - the whole "
            "upper body becomes a pointer aimed at the new thing. Hands may rise higher, "
            "palms open, in the universal 'what is that' gesture. The stance widens "
            "slightly for balance, as if the body expects it might need to move fast. "
            "This is the body switching from defense to investigation: act one protected "
            "the instrument, act two points the instrument at the data.\n\n"
            "Movement during surprise has a staccato quality - stop, turn, lean, step - "
            "because each motion waits on a fresh sample of information. A person "
            "approaching a strange sound does not glide; they advance in little bursts "
            "with pauses between, the body negotiating with uncertainty step by step. "
            "Hands become the narrators: they fly to the mouth in astonishment, press to "
            "the chest in relief-tinged surprise, or shoot out palm-up in the 'can you "
            "believe this' shrug that accompanies told surprises.\n\n"
            "Afterward comes the discharge - the body shedding the mobilization. People "
            "shake their hands out, roll their shoulders, pace a few steps, laugh "
            "suddenly. These are not random fidgets; they are the spring unwinding. "
            "Athletes and performers know this phase well and work with it deliberately, "
            "using a shake-out or a breath to tell the body the alert is over. The "
            "posture of surprise, from crouch to orient to discharge, is a complete "
            "physical sentence with a beginning, middle, and end."
        ),
        "how_it_works": (
            "Stage the scene: a quiet library, a book slides off a high shelf and slaps "
            "the floor. Act one, 0-300 ms: the nearest reader's chin tucks, shoulders jump "
            "toward ears, hands freeze above the book they were holding - the crouch, "
            "performed identically by three other readers in the same instant. Act two, "
            "300 ms-2 s: heads swivel toward the sound in near-unison; one reader leans "
            "forward, another half-rises, a third's hands fly palm-up - the orient, the "
            "body as pointer. Act three, 2-6 s: appraisal lands - 'just a book' - and the "
            "discharge begins: the half-risen reader sits back down with a shaky laugh, "
            "another rolls their neck, a third shakes their hands out once, sharply. By "
            "second ten, postures have returned to reading positions, but looser - the "
            "spring unwound, the sentence complete. Anyone watching from the balcony could "
            "read the whole emotion off the bodies alone, no faces needed."
        ),
        "key_points": [
            "Act one is the crouch: chin tuck, shoulder hunch, hands rising - defense first.",
            "Act two is the orient: the body becomes a pointer aimed at the novelty.",
            "Surprised movement is staccato - stop, turn, lean - negotiating with uncertainty.",
            "Hands narrate: to the mouth, to the chest, palm-up in disbelief.",
            "The discharge - shaking out, laughing, pacing - unwinds the mobilized spring.",
        ],
        "requirements": [
            "Watch a crowd's bodies (not faces) the next time a sudden sound hits.",
            "Try the shake-out discharge deliberately after your next startle.",
        ],
        "standards": [
            "Startle-posture ethology: the protective crouch across mammals.",
            "Orienting response: head-turn and approach kinematics.",
            "Somatic discharge: trembling and movement after arousal.",
        ],
        "citations": [CIT_SOKOLOV, CIT_PANKSEPP, CIT_LEDOUX],
        "sig_lens": (
            SIG_LENS_BELL + " Crouch, orient, discharge - the Signature reader treats the "
            "three acts as drill steps. Crouch protects the instrument, orient aims it, "
            "discharge resets it. A body that knows its drill answers the bell cleanly."
        ),
    },
    {
        "key": "sleep",
        "name": "Sleep, Appetite, and Energy in Surprise",
        "group": "Body Signals",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Surprise itself is too brief to rearrange sleep or appetite the way longer "
            "emotions do - nobody loses sleep over a popped balloon. But strong or "
            "repeated surprises leave footprints in all three. After an intense "
            "startle, especially one that blended with fear, the body stays on alert: "
            "the threshold for the next startle drops, and that lowered threshold can "
            "follow a person to bed. The parent who heard the window smash at midnight "
            "may lie awake listening, every house-creak amplified - not because the "
            "surprise is still happening, but because the aftershock keeps the alarm "
            "panel lit. One bad night rarely matters; a week of jumpy evenings can.\n\n"
            "Appetite responds to the same mobilization. The stomach 'drop' of surprise "
            "is blood and tension shifting away from digestion toward the big muscles - "
            "useful if you must run, unhelpful if you were about to eat. After a strong "
            "surprise, food can seem unappealing for a while; the gut needs time to be "
            "told the emergency is over. Conversely, the discharge phase can swing the "
            "other way: the shaky laughter after a false alarm is often followed by "
            "sudden hunger, the body restocking the fuel it mobilized. Neither response "
            "is a disorder - they are the fuel system doing its accounting.\n\n"
            "Energy is where surprise's effect is most visible. A big surprise spends "
            "energy like a sprint: adrenaline mobilizes glucose, the heart works hard, "
            "muscles brace - and if no action follows, the bill still comes due. People "
            "often feel oddly tired after an intense scare that turned out to be "
            "nothing, and they are puzzled by it: 'nothing happened, why am I "
            "exhausted?' Something did happen - a full emergency mobilization with no "
            "outlet. The fatigue is real and honest. Gentle movement, food, and rest "
            "settle the accounts; the body knows how to close the books if given the "
            "chance.\n\n"
            "The practical upshot is small and humane: after a big surprise, expect the "
            "body to need a little recovery - a quieter evening, a real meal, an early "
            "night - and give it that without making a story of it. And when surprises "
            "come in clusters - a chaotic week of alarms and upsets - the sleep, "
            "appetite, and energy effects stack, which is worth noticing before they "
            "stack into something bigger. The bell rings; the panel lights; the wise "
            "response includes letting the panel go dark again."
        ),
        "how_it_works": (
            "Follow the fuel through a scare. Noon: Dana gets the call - a family "
            "member in the emergency room (it turns out to be a false alarm from a "
            "misread chart, but she does not know that for two hours). Minute 0-5: "
            "adrenaline floods, heart pounds, stomach clenches - lunch sits forgotten. "
            "Hour 1-2: sustained alertness burns glucose; hands tremble slightly; she "
            "cannot sit still. Hour 3: the all-clear arrives - relief, laughter, "
            "shaking. Hour 4: sudden ravenous hunger; she eats a full meal. That night: "
            "sleep comes but light, with two wake-ups at small sounds - the lowered "
            "threshold. Next day: a tiredness out of proportion to the day's activity - "
            "the sprint's bill. Day three: normal. The scenario maps the whole "
            "economy: mobilize, spend, discharge, restock, recover. Nothing "
            "pathological happened at any step; it was all the fuel system doing "
            "exactly its job."
        ),
        "key_points": [
            "Brief surprises barely touch sleep or appetite; strong or repeated ones leave footprints.",
            "Aftershock alertness can lighten sleep the night after a big scare.",
            "The stomach 'drop' pauses digestion; the discharge phase often brings rebound hunger.",
            "A big false alarm spends sprint-level energy - the tiredness afterward is honest.",
            "Recovery is simple: quieter evening, real food, rest; clustered surprises stack, so notice.",
        ],
        "requirements": [
            "After your next big startle, notice what your stomach and energy do in the hour after.",
            "Give the body recovery time without dramatizing it.",
        ],
        "standards": [
            "Autonomic mobilization and recovery: sympathetic-parasympathetic rebound.",
            "Stress and sleep: hyperarousal effects on sleep onset and continuity.",
            "Metabolic cost of acute stress responses.",
        ],
        "citations": [CIT_PANKSEPP, CIT_LEDOUX],
        "sig_lens": (
            SIG_LENS_BELL + " Every ring of the bell spends fuel, and the Signature "
            "reader budgets for it - a loud day gets a quiet evening. The panel is not "
            "meant to stay lit; rest is how the system turns the lights back off."
        ),
    },
    {
        "key": "differences",
        "name": "Different Bodies, Different Surprises",
        "group": "Body Signals",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "No two bodies answer the bell the same way. Startle sensitivity - how big "
            "a jolt a given trigger produces - varies enormously between people, and "
            "most of the variation is ordinary. Some of it is wiring: the acoustic "
            "startle circuit runs through the brainstem, and small differences in that "
            "circuitry make some people jump at a dropped book while others barely "
            "blink. Some of it is state: the same person startles far more when tired, "
            "caffeinated, stressed, or ill. And some of it is history: a person whose "
            "past paired sudden sounds with danger will have a lower threshold, "
            "sometimes for years, because the prediction system learned that novelty "
            "is expensive.\n\n"
            "Age bends the curve too. Infants startle at almost anything - their "
            "prediction maps are mostly blank, so nearly everything is novel. Children "
            "startle big and recover fast, often laughing within seconds. Adults vary "
            "widely. Older adults may startle less strongly in the body but take "
            "longer to settle afterward, the recovery phase stretching as the "
            "autonomic system ages. None of these are flaws; they are the instrument "
            "tuned differently at different life stages.\n\n"
            "Culture and habit shape the expression more than the reflex. The blink "
            "and the hunch are involuntary everywhere, but what happens next - the "
            "gasp or the silence, the laugh or the apology, the hand to the mouth or "
            "the steady stare - is learned. Some families narrate every startle out "
            "loud; some go quiet. Some workplaces treat visible surprise as "
            "unprofessional and train it down; performers train it up. The underlying "
            "bell is the same; the etiquette around the bell is local.\n\n"
            "The practical point is comparison: never measure your own surprise "
            "against someone else's. The friend who laughs at horror movies and the "
            "friend who hides behind a cushion are not brave and cowardly - they are "
            "differently tuned. What matters is knowing your own instrument: your "
            "threshold today, what lowers it, what raises it, and how long your "
            "aftershock runs. A person who knows their own bell can plan around it - "
            "rest before the haunted house, earplugs at the fireworks, a breath "
            "before the announcement."
        ),
        "how_it_works": (
            "Put three people in front of the same popped balloon. Ana blinks hard, "
            "laughs instantly, and is telling the story before the echo fades - high "
            "sensitivity, fast recovery, amusement landing. Ben barely flinches - low "
            "sensitivity, the reflex damped by years of stage work where bangs are "
            "routine - and calmly keeps talking. Cara startles hard, goes quiet, and "
            "stays on edge for twenty minutes - high sensitivity, slow recovery, the "
            "aftershock running long because a car accident years ago taught her "
            "system that sudden noise can mean real danger. Same balloon, three "
            "bodies, three honest answers. The scenario's lesson: the trigger is "
            "shared, but the instrument is personal - wiring, state, and history all "
            "turning the same three dials to different settings."
        ),
        "key_points": [
            "Startle sensitivity varies widely: wiring, current state, and history all tune it.",
            "Infants startle at nearly everything; recovery speed varies across life.",
            "The reflex is universal; what follows it - laugh, silence, apology - is learned.",
            "Never compare your bell to someone else's; learn your own threshold and aftershock.",
            "Thresholds move with sleep, stress, caffeine, and past pairings of novelty with danger.",
        ],
        "requirements": [
            "Notice your own startle level across one week - what days is it higher?",
            "Identify one thing that reliably lowers your threshold.",
        ],
        "standards": [
            "Individual differences in startle reactivity.",
            "Developmental trajectory of the orienting and startle responses.",
            "Display rules: cultural shaping of emotional expression.",
        ],
        "citations": [CIT_EKMAN, CIT_PANKSEPP],
        "sig_lens": (
            SIG_LENS_BELL + " Every bell is cast differently - some ring at a touch, "
            "some need a hammer. The Signature reader does not wish for a different "
            "bell; they learn the exact tone of the one they have."
        ),
    },
    {
        "key": "face",
        "name": "The Face of Surprise: Eyes, Brows, Mouth",
        "group": "Facial Expression",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The surprised face is one of the most readable in the human repertoire, "
            "and it is built from three moves that happen almost together. First the "
            "brows shoot up - the forehead lifts, often wrinkling in horizontal lines "
            "across its full width. Second the eyes widen - the upper lids rise, the "
            "lower lids drop slightly, exposing more of the white around the iris "
            "than usual. Third the jaw drops - the mouth falls open, not in a shaped "
            "'o' at first but in a loose, slack opening, as if the face forgot what "
            "it was doing. Brows up, eyes wide, jaw down: the three moves together "
            "are surprise's signature, recognized across every culture studied.\n\n"
            "Each move has a function, which is why the face looks the way it does. "
            "Raised brows and widened eyes enlarge the visual field - literally more "
            "of the world gets in, and the eyes can swivel faster to locate the "
            "novelty. The dropped jaw is partly the gasp reflex opening the airway "
            "and partly the speech system halting mid-program - the mouth opens "
            "because the words stopped. The whole face becomes an intake device: "
            "maximum information, minimum output.\n\n"
            "Researchers code these moves precisely. In the Facial Action Coding "
            "System, surprise is brow raise (action units 1 and 2), upper-lid raise "
            "(unit 5), and jaw drop (unit 26 or 27). The combination is so "
            "distinctive that even partial versions read clearly: brows plus wide "
            "eyes without the jaw still says surprise; the jaw drop alone is "
            "ambiguous and needs context. Timing matters too - in genuine surprise "
            "the three moves onset within about half a second of each other and the "
            "whole expression is over in a few seconds.\n\n"
            "The micro-signs ride along: the nostrils may flare slightly with the "
            "gasp, the skin of the forehead stretches smooth then wrinkles, the head "
            "often pulls back a fraction as the eyes go forward - the body "
            "simultaneously approaching with the senses and withdrawing with the "
            "skull. Actors study these details for years; the rest of us read them "
            "in a glance without ever naming them, which is exactly what the "
            "expression evolved for - instant, wordless broadcast of 'something "
            "unexpected is happening.'"
        ),
        "how_it_works": (
            "Freeze the frame at the pop of a champagne cork across a dinner table. "
            "Frame one (100 ms): brows begin rising, forehead wrinkling. Frame two "
            "(250 ms): upper lids lift, whites show above and below the iris, pupils "
            "already dilating. Frame three (400 ms): jaw drops open, the gasp begins, "
            "head tilts back a few degrees. Frame four (800 ms): the full tableau - "
            "every face at the table wearing some version of the three moves, aimed "
            "at the bottle. Frame five (2 s): appraisal lands - 'just the cork, "
            "nobody hurt' - and the faces begin dissolving into laughter, brows "
            "settling, mouths reshaping into smiles. The whole broadcast took under "
            "a second to assemble and did its job: everyone at the table knew, "
            "without a word, that something unexpected had happened and where to "
            "look."
        ),
        "key_points": [
            "Three moves: brows up, eyes widened, jaw dropped - onset within half a second.",
            "Each move is functional: wider visual field, faster locating, open airway.",
            "FACS codes it as action units 1+2 (brow raise), 5 (lid raise), 26/27 (jaw drop).",
            "The full combination is pan-cultural; partial versions still read clearly.",
            "Micro-signs: nostril flare, forehead wrinkling, slight head withdrawal.",
        ],
        "requirements": [
            "Watch for the three moves separately next time someone is startled.",
            "Notice how fast the whole tableau assembles - under a second.",
        ],
        "standards": [
            "Facial Action Coding System (Ekman and Friesen): AU 1+2, 5, 26/27.",
            "Cross-cultural recognition studies of the surprise face.",
            "Functional accounts of expression morphology.",
        ],
        "citations": [CIT_EKMAN_FRIESEN, CIT_EKMAN],
        "sig_lens": (
            SIG_LENS_BELL + " The face is the bell's beacon - the part of the panel "
            "visible to the whole room. Brows up is the flag raised, eyes wide is the "
            "lens opened, jaw down is the speaker cut. The Signature reader learns to "
            "read the beacon in others and to let their own fly honestly."
        ),
    },
    {
        "key": "intensityface",
        "name": "The Surprise Expression at Different Intensities",
        "group": "Facial Expression",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The surprised face is not one face but a dial. At the lowest setting - "
            "the mild 'oh?' - only the brows move: a quick lift, a brief horizontal "
            "creasing of the forehead, and it is over in under a second. The eyes "
            "may widen a fraction; the mouth stays as it was. This is the face of "
            "routine correction, and people wear it dozens of times a day without "
            "noticing - in conversation, while reading, while driving. It is "
            "surprise's quiet working face.\n\n"
            "Turn the dial to moderate and the full trio assembles: brows up, eyes "
            "wide with visible white, jaw dropped open. The expression holds for a "
            "second or two - long enough for anyone watching to read it clearly. "
            "This is the face of the plot twist, the unexpected guest, the sudden "
            "announcement. The features move further and stay longer, and the head "
            "often joins with a small pull-back or tilt. At this setting the face "
            "is doing public work: broadcasting the news to the room.\n\n"
            "At maximum - the thunderclap face - everything goes further and the "
            "expression can look almost distorted. Brows hit their highest, eyes "
            "their widest, jaw at full drop; the whole face seems to stretch. The "
            "head may snap toward the trigger or jerk back. The expression can hold "
            "for several seconds because appraisal is still catching up - the face "
            "waits, frozen open, for the verdict. In photographs of disaster "
            "survivors and lottery winners, this is the face you see: the human "
            "face at its most open, mid-rewrite of its map.\n\n"
            "Reading the dial is a learnable skill with real uses. A negotiator "
            "watching brows flicker knows a number landed unexpectedly. A teacher "
            "watching jaws drop knows the demonstration worked. A friend watching a "
            "face go from trio to frozen-open knows this surprise is big and the "
            "verdict is still out - which is exactly when to stay close and stay "
            "quiet. The face reports the volume honestly because the muscles move "
            "before the mind can edit them."
        ),
        "how_it_works": (
            "Three faces, one trigger type - unexpected news, different volumes. "
            "Face one: 'the meeting moved to Thursday.' Brows lift for half a "
            "second, forehead creases, mouth unchanged - the quiet working face, "
            "already rescheduling. Face two: 'the meeting is in Tokyo tomorrow.' "
            "Full trio - brows high, eyes wide, jaw dropped - holding two seconds "
            "while the mind replays the calendar; the head pulls back slightly. "
            "Face three: 'the company was sold overnight and everyone is "
            "relocated.' Maximum - face stretched open, frozen for four seconds, "
            "then the hands come up to cover the mouth as the verdict begins "
            "forming. Same three moves in all three faces; the dial settings - "
            "amplitude and duration - tell the watcher exactly how big the gap "
            "between expectation and reality just was."
        ),
        "key_points": [
            "Low: brows only, under a second - surprise's quiet working face.",
            "Moderate: full trio, 1-2 seconds - the public broadcast face.",
            "Maximum: features at full stretch, frozen open while appraisal catches up.",
            "Amplitude and duration of the moves encode the volume honestly.",
            "Watching the dial has real uses: negotiation, teaching, friendship.",
        ],
        "requirements": [
            "Catch the quiet brow-lift version in yourself three times today.",
            "Compare its duration to a bigger surprise face you remember.",
        ],
        "standards": [
            "FACS intensity scoring: graded action-unit amplitude.",
            "Expression dynamics: onset, apex, and offset timing.",
        ],
        "citations": [CIT_EKMAN_FRIESEN, CIT_EKMAN],
        "sig_lens": (
            SIG_LENS_BELL + " The beacon has brightness settings, and the Signature "
            "reader calibrates their eye to all of them - the flicker, the flare, "
            "and the full blaze - because each brightness asks for a different "
            "response."
        ),
    },
    {
        "key": "hidefake",
        "name": "Hiding and Faking Surprise: What Leaks Through",
        "group": "Facial Expression",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Surprise is famously hard to hide, and the reason is speed. The genuine "
            "expression assembles in under half a second - before the conscious "
            "mind can issue the order to suppress it. By the time a person decides "
            "'do not react,' the brows have already lifted. What suppression can "
            "do is cut the expression short: clamp the jaw shut, drop the brows "
            "back down, smooth the face - but the first flicker usually escapes. "
            "Trained observers, and anyone watching closely, catch the flicker even "
            "when the cover-up is fast. This is why surprise is trusted as an "
            "honest signal: it is the emotion that testifies before the witness "
            "can be coached.\n\n"
            "Faking surprise is the mirror problem, and it fails in the opposite "
            "direction. Acted surprise tends to be too slow, too symmetrical, and "
            "too long: the brows rise deliberately, the 'oh!' is placed rather "
            "than escaping, the wide eyes hold for the audience. Genuine surprise "
            "is fast, slightly asymmetrical, and brief - the body does not pose. "
            "The acted version also misses the accompaniments: the real gasp's "
            "ragged intake, the genuine freeze of the hands, the authentic "
            "aftershock. Actors who play surprise well study exactly these "
            "details, which tells you how hard they are to invent from scratch.\n\n"
            "What leaks through during hiding attempts follows a pattern. The "
            "upper face leaks most - brow flashes are the hardest to suppress "
            "because the forehead muscles are fast and poorly represented in "
            "conscious body-image. The mouth is easier to control, so a suppressed "
            "surprise often shows as brows-up with a clamped or tightened mouth - "
            "a combination that reads as startled-but-containing-it. The body "
            "leaks too: the suppressed face may be smooth while the hands still "
            "freeze or the breath still catches. Leak-hunters watch the whole "
            "person, not just the face.\n\n"
            "There is an ethical footnote worth stating plainly: skill at reading "
            "leaks is for understanding, not for trapping. The honest-signal "
            "quality of surprise makes it tempting to use as a lie detector - the "
            "gotcha question, the staged reveal. But leaks are clues, not proof, "
            "and people have many honest reasons for a flicker. This archive "
            "teaches the reading so people can understand each other better, not "
            "so they can ambush each other."
        ),
        "how_it_works": (
            "The scenario is a surprise party that almost worked. Maya opens the "
            "door; the shout goes up. Her genuine response fires first: brows flash "
            "up, eyes widen, a real gasp escapes - 300 milliseconds of unedited "
            "truth. Then, because she half-suspected (a friend was acting shifty), "
            "the suppression arrives: she clamps her mouth into a smile, drops her "
            "brows, laughs 'you got me!' The room sees the sequence - flash, then "
            "cover - and reads it correctly: genuinely startled, quickly composed. "
            "Contrast the guest who was warned and tries to act surprised: the "
            "brows rise a beat late, the 'oh wow!' lands on a rehearsed pitch, the "
            "eyes widen and hold too long, and there is no gasp, no freeze, no "
            "aftershock - the accompaniments are missing. Everyone can feel the "
            "difference even if nobody can name it. The leak is the truth; the "
            "performance is the effort."
        ),
        "key_points": [
            "Genuine surprise is too fast to suppress - the first flicker escapes before the cover order.",
            "Suppression cuts it short (clamped jaw, dropped brows) but rarely erases the onset.",
            "Faked surprise is too slow, too symmetrical, too long - and misses the gasp, freeze, aftershock.",
            "The upper face leaks most; the body leaks what the face hides.",
            "Leaks are clues for understanding, not proof for trapping.",
        ],
        "requirements": [
            "Watch for the flash-then-cover sequence in a real moment this week.",
            "Notice the difference between a gasp that escapes and an 'oh' that is placed.",
        ],
        "standards": [
            "Micro-expression research: leakage and the timing of genuine vs posed expressions.",
            "Display rules and suppression: what control can and cannot do.",
        ],
        "citations": [CIT_EKMAN, CIT_EKMAN_FRIESEN, CIT_GROSS],
        "sig_lens": (
            SIG_LENS_BELL + " The bell cannot be unrung, and the beacon cannot be "
            "unlit in the first half-second - that is the Signature guarantee of "
            "honesty. The reader trusts the flash, discounts the performance, and "
            "never uses the reading as a weapon."
        ),
    },
    {
        "key": "artist",
        "name": "The Artist's Notes: Describing the Surprised Look",
        "group": "Facial Expression",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "For the painter, the actor, or the writer, here is the surprised look "
            "in working notes. Start with the forehead: draw it lifted, the whole "
            "brow line arched high, with horizontal creases running across the full "
            "width - not the worried vertical lines between the brows, but smooth "
            "horizontal waves. The brows themselves sit higher than neutral, their "
            "inner ends raised as much as the outer, giving the face its open, "
            "un guarded quality. This is the single most important feature: get "
            "the brows wrong and the face reads as fear or worry instead.\n\n"
            "Next the eyes: open them wider than you think. The upper lid should "
            "clear the top of the iris entirely, showing a sliver of white above; "
            "the lower lid drops a touch, showing white below as well. The iris "
            "looks smaller by contrast, which is why surprised eyes read as "
            "'staring.' Add a slight forward push of the eyeballs - the gaze "
            "locks onto the trigger point. For the actor: do not just widen the "
            "eyes; aim them. The aim is half the meaning.\n\n"
            "Then the mouth: let the jaw hang. Not pursed, not shaped - slack. "
            "The lips part without tension, the lower jaw drops straight down, and "
            "the chin pulls slightly back. In strong surprise the mouth is a dark "
            "oval; in mild surprise it may only part a finger's width. Writers: "
            "the mouth is where 'astonished' lives on the page - 'her mouth fell "
            "open' is a cliche because it is accurate. Pair it with the arrested "
            "gesture - the hand stopped mid-air, the spoon hovering - and the "
            "reader sees the whole freeze.\n\n"
            "Finally the whole: tilt the head back a few degrees or turn it "
            "sharply toward the imagined trigger; lift the shoulders a fraction; "
            "let the hands rise, palms open or flying to the mouth. Light the face "
            "from the front so the widened eyes catch it. And remember the timing "
            "note for performers: the look should arrive all at once, fast, and "
            "then either dissolve into the landing emotion or freeze while the "
            "verdict forms. A surprise held too long on stage reads as comedy or "
            "confusion - which, in the right play, is exactly the point."
        ),
        "how_it_works": (
            "A director blocks the moment: the letter is opened on stage. Beat "
            "one - the actor's brows fly up, forehead creasing horizontally, eyes "
            "widening to show white above the iris, gaze snapping to the page. "
            "Beat two - the jaw drops slack, the hand holding the letter freezes "
            "mid-air, the other hand rises palm-open. Beat three - the head pulls "
            "back a fraction while the eyes push forward, shoulders lifting. The "
            "audience reads it in under a second: something in that letter broke "
            "the character's world. Then the director's choice: dissolve into joy "
            "(the letter is good news - brows stay high, mouth reshapes to a "
            "smile) or freeze into dread (the letter is bad - the open face "
            "stays open while the eyes lose focus). Same three moves, two "
            "landings, and the blocking notes above are all the company needs to "
            "play either."
        ),
        "key_points": [
            "Brows: high arch, horizontal forehead creases - the most important feature.",
            "Eyes: white above and below the iris, gaze aimed at the trigger.",
            "Mouth: slack jaw drop, lips parted without tension.",
            "Whole: head back or turned, shoulders up, hands rising or frozen mid-gesture.",
            "Timing: all at once, fast - then dissolve into the landing or freeze for the verdict.",
        ],
        "requirements": [
            "Sketch or describe one surprised face from memory using the notes.",
            "Check each feature: brows, eyes, mouth, head, hands.",
        ],
        "standards": [
            "FACS: the visual specification behind the notes.",
            "Acting method: physical score for the surprise beat.",
        ],
        "citations": [CIT_EKMAN_FRIESEN],
        "sig_lens": (
            SIG_LENS_BELL + " The artist draws the beacon so others can recognize "
            "it at a glance - and in drawing it faithfully, the Signature artist "
            "honors the honest signal: brows high, eyes open, jaw slack, nothing "
            "hidden."
        ),
    },
    # -------------------------------------------------- TRIGGERS
    {
        "key": "classictriggers",
        "name": "Classic Triggers of Surprise",
        "group": "Triggers",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Certain triggers surprise nearly everyone, because they break "
            "predictions almost every human shares. Sudden loud sounds top the "
            "list: thunderclaps, balloons popping, doors slamming, a shout in a "
            "quiet room. The auditory startle circuit is ancient and fast, and "
            "loudness is a prediction-breaker that needs no learning - even "
            "newborns startle at a sharp clap. Close behind are sudden visual "
            "events: something appearing where nothing was, rapid motion in the "
            "periphery, a face looming close without warning. The visual system "
            "is a change-detector, and abrupt onsets are its native alarm.\n\n"
            "The second family is news - information that rewrites the map. "
            "Unexpected praise, sudden bad news, a plot twist, a result nobody "
            "predicted: these are cognitive surprises, slower than the startle "
            "but often deeper. Their power comes from the size of the belief "
            "they overturn. Being told you won something you never entered "
            "outranks being told dinner is ready, because the prediction gap is "
            "enormous. Gossip, headlines, and stories all run on this fuel - "
            "the human appetite for 'you will not believe what happened' is "
            "the appetite for cognitive surprise.\n\n"
            "The third family is social: people doing the unexpected. The "
            "friend who appears at the door unannounced, the quiet colleague "
            "who suddenly sings, the stranger who knows your name. Social "
            "predictions run constantly - we forecast each other's behavior "
            "all day - so social violations surprise reliably. Surprise "
            "parties weaponize this on purpose, stacking all three families: "
            "the sudden shout (sound), the crowd appearing (vision), the "
            "people you love in your living room at an impossible hour "
            "(social news).\n\n"
            "The fourth family is the body itself: the step that is not there, "
            "the phone buzzing in a silent pocket, the sneeze that arrives "
            "without warning. Proprioceptive and tactile surprises remind us "
            "the prediction system covers the body too - the brain forecasts "
            "the next stair, and the missing stair is one of life's most "
            "universal small shocks. Catalogued together, the classic triggers "
            "form a map of what humans collectively expect: quiet, continuity, "
            "predictable people, and solid stairs."
        ),
        "how_it_works": (
            "Run the haunted-house walkthrough as a trigger catalog in motion. "
            "Room one: a sudden air blast and bang - auditory startle, pure and "
            "instant, no learning required. Room two: a figure lunges from the "
            "dark into the flashlight beam - visual onset plus looming, the "
            "change-detector screaming. Room three: the guide, who has been "
            "reassuring, suddenly screams too - social prediction broken, the "
            "trusted person becoming the threat. Room four: the floor drops an "
            "inch underfoot - proprioceptive surprise, the missing stair. Each "
            "room fires a different family, and the walkthrough works because "
            "the designers know the catalog: hit the ancient circuits (sound, "
            "vision, body) for the jumps, and the social circuits for the "
            "lingering unease. The same catalog, used kindly, builds the "
            "surprise party, the magic trick, and the great plot twist."
        ),
        "key_points": [
            "Four classic families: sudden sounds, sudden visual events, map-rewriting news, unexpected people.",
            "Loud sounds need no learning - the auditory startle is innate.",
            "News surprises scale with the size of the belief overturned.",
            "Social prediction runs all day, so social violations surprise reliably.",
            "The body has its own triggers: the missing stair, the phantom buzz.",
        ],
        "requirements": [
            "Sort your last five surprises into the four families.",
            "Notice which family startles you most - that is your sensitive channel.",
        ],
        "standards": [
            "Startle-eliciting stimuli: acoustic, visual, tactile taxonomies.",
            "Appraisal theory: novelty detection across modalities.",
        ],
        "citations": [CIT_SOKOLOV, CIT_SCHERER],
        "sig_lens": (
            SIG_LENS_BELL + " The catalog is the bell-maker's handbook: four "
            "families of hammers. The Signature reader learns the catalog not to "
            "startle others carelessly, but to recognize which hammer just struck "
            "their own bell."
        ),
    },
    {
        "key": "personaltriggers",
        "name": "Personal Triggers: Memories and Private Associations",
        "group": "Triggers",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Beyond the universal triggers lies a private catalog that no one "
            "else shares: the surprises only you would feel. A song from a "
            "specific summer, heard in a grocery store, can stop a person "
            "mid-aisle - not because the song is startling, but because the "
            "memory it unlocks arrives all at once, uninvited. A smell, a "
            "street corner, a phrase someone used to say: these are prediction "
            "breaks of a personal kind, where the 'expectation' was the quiet "
            "assumption that the past would stay in the past.\n\n"
            "Anniversaries are the calendar version. The body often remembers "
            "dates the mind has filed away - a heaviness or jumpiness on a "
            "day that turns out to be the anniversary of a loss or a shock. "
            "This is not mysticism; it is associative learning doing its "
            "ordinary work. The prediction system tags seasons, weather, and "
            "light with past outcomes, and when the tags match, the alarm "
            "primes itself. The surprise, when it comes, is the realization: "
            "'oh - that is what today is.'\n\n"
            "Private associations also tune sensitivity up or down. The nurse "
            "startles at a monitor beep that visitors do not hear; the veteran "
            "flinches at a backfire; the new parent wakes at a whimper two "
            "rooms away. Each has a trained prediction system with custom "
            "alarms installed by experience. These are not overreactions - "
            "they are expertise misfiring in a safe context, the instrument "
            "doing exactly what it was trained to do.\n\n"
            "The gentle handling of personal triggers is a social skill. "
            "Because they are invisible to everyone else, they are easily "
            "dismissed: 'it was just a song, why are you crying.' The "
            "understanding response recognizes that the trigger is never "
            "'just' the song - it is the song plus the whole associative "
            "network behind it, arriving in one unannounced package. Mapping "
            "your own private triggers - the songs, dates, smells, phrases - "
            "turns ambushes into known terrain. You still feel them, but you "
            "are no longer blindsided by your own history."
        ),
        "how_it_works": (
            "Mara is fine all morning - and then the bakery plays the song from "
            "her wedding, the marriage that ended two years ago. The trigger "
            "chain: the first notes (auditory match) unlock the associative "
            "network in under a second - the dance floor, the light, the "
            "vows, the ending - and the prediction 'today is an ordinary "
            "Tuesday' shatters. Her step falters mid-aisle; her eyes fill "
            "before she has decided to feel anything; she stands among the "
            "bread holding a basket, surprised by grief she thought was "
            "finished. A friend finds her and says the wrong thing - 'it is "
            "just a song' - and then, catching herself, the right thing: "
            "'that one has history.' They wait until the wave passes. The "
            "scenario shows the personal trigger's structure: a small public "
            "stimulus, a huge private network, and a surprise that belongs "
            "entirely to one person's map."
        ),
        "key_points": [
            "Private triggers unlock whole associative networks in under a second.",
            "Anniversaries: the body tags dates and seasons; the alarm primes itself.",
            "Training installs custom alarms - the nurse, the veteran, the new parent.",
            "Invisible triggers are easily dismissed; 'just a song' is never just the song.",
            "Mapping your own triggers turns ambushes into known terrain.",
        ],
        "requirements": [
            "List three of your own private triggers - song, date, smell, phrase.",
            "Notice the network behind one of them: what arrives with it?",
        ],
        "standards": [
            "Associative learning and emotional memory.",
            "Context-dependent memory and anniversary reactions.",
            "Two-factor theory: the label comes from the network, not just the stimulus.",
        ],
        "citations": [CIT_LEDOUX, CIT_SCHACHTER],
        "sig_lens": (
            SIG_LENS_BELL + " Every bell carries engravings from its casting - "
            "the private triggers are the Signature reader's own inscriptions. "
            "Knowing where they are lets the reader pad the spots that ring too "
            "loud and polish the ones that ring sweet."
        ),
    },
    {
        "key": "oddtriggers",
        "name": "Odd and Unexpected Triggers of Surprise",
        "group": "Triggers",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Then there are the triggers nobody would predict - the odd ones "
            "that reveal how strange and personal the prediction system really "
            "is. A familiar voice saying an unfamiliar word. A pet doing "
            "something it has never done in twelve years. A typo in a beloved "
            "book, in a sentence you have read twenty times. The wrongness is "
            "tiny and the surprise is real, because the prediction was held "
            "with total confidence: of course the book says what it always "
            "said. High confidence is the secret ingredient of odd triggers - "
            "the more certain the prediction, the bigger the jolt when it "
            "breaks.\n\n"
            "Absence is a rich source of odd surprise. The clock that always "
            "ticks, suddenly silent. The dog that always greets, not at the "
            "door. The email that always arrives by nine, missing. The brain "
            "predicts continuities, not just events, and a missing expected "
            "thing is a full prediction break. People often cannot name what "
            "startled them in these moments - 'something feels off' - because "
            "the trigger is a hole where a thing should be.\n\n"
            "Timing violations are another vein. The joke told too late, the "
            "applause starting before the performance ends, the reply "
            "arriving instantly to a message sent hours ago - each breaks a "
            "temporal prediction most people never knew they held. Comedians "
            "mine this deliberately: the pause held one beat too long turns "
            "expectation into surprise, and the laugh that follows is the "
            "discharge of the broken timing.\n\n"
            "The lesson of the odd triggers is humility about the prediction "
            "system. It is vastly larger and more detailed than the conscious "
            "mind suspects - it predicts the book's sentences, the clock's "
            "ticking, the dog's greeting - and its depth is revealed only when "
            "something small goes wrong. Odd surprises are the system showing "
            "its work: look how much I was tracking, it says, without ever "
            "telling you."
        ),
        "how_it_works": (
            "Collect four odd triggers into one afternoon. 2 PM: the office "
            "clock, ticking for six years, stops - and three people look up "
            "at once, unable to say why the room feels wrong (absence "
            "trigger). 3 PM: a colleague's parrot, silent for a decade, says "
            "'hello' - the room erupts; a twelve-year prediction just broke "
            "(high-confidence violation). 4 PM: a text reply arrives eleven "
            "seconds after a message sent that morning - the timing is "
            "impossible, the mind stalls (temporal violation). 5 PM: rereading "
            "a favorite novel, a reader finds a typo in the most-quoted line - "
            "a tiny wrongness, a genuine jolt (familiar-text violation). None "
            "of these appear in any standard trigger catalog, yet each ran "
            "the full circuit: mismatch, freeze, appraisal, landing. The odd "
            "triggers prove the rule by breaking it - the prediction system "
            "is everywhere, so surprise can come from anywhere."
        ),
        "key_points": [
            "High confidence is the secret ingredient: the surer the prediction, the bigger the jolt.",
            "Absence triggers: the missing tick, the ungreeted door - a hole where a thing should be.",
            "Timing violations: the too-late joke, the instant reply to an old message.",
            "Odd surprises reveal the prediction system's hidden depth.",
            "Comedians mine timing violations deliberately - the held pause.",
        ],
        "requirements": [
            "Catch one odd trigger this week - something tiny that still jolted you.",
            "Ask what confident prediction it broke.",
        ],
        "standards": [
            "Predictive processing: the brain as a prediction machine.",
            "Expectation violation across modalities and timescales.",
        ],
        "citations": [CIT_BARRETT, CIT_SCHERER],
        "sig_lens": (
            SIG_LENS_BELL + " The odd triggers are the bell ringing in rooms the "
            "reader forgot the house had. The Signature habit: when an odd ring "
            "sounds, go look at the room - there is a prediction there worth "
            "knowing about."
        ),
    },
    {
        "key": "chains",
        "name": "Chain Reactions: One Surprise Begets Another",
        "group": "Triggers",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Surprises rarely travel alone. One prediction break loosens the "
            "whole map, and the loosened map breaks more easily - so a single "
            "surprise often starts a cascade. The mechanism is simple: after "
            "the first shock, attention is wide open and the threshold is "
            "lowered, which means the next small novelty that would normally "
            "pass unnoticed now registers as a second surprise. The dropped "
            "tray startles; while still settling, the chair scraping makes "
            "you jump; the jump makes you laugh; the laugh draws looks; the "
            "looks embarrass - four emotions deep from one dropped tray.\n\n"
            "Cascades also run through meaning, not just startle. News "
            "surprises chain by implication: 'we are moving' implies 'new "
            "schools,' which implies 'goodbye to friends,' which implies 'a "
            "new life' - each link its own small shock, each landing its own "
            "emotion. The first surprise opens the door; the implications walk "
            "through one by one. This is why big announcements need pacing: "
            "delivering five implications at once does not make one big "
            "surprise, it makes a cascade, and cascades overwhelm the "
            "appraisal system that has to land each one.\n\n"
            "Social cascades are the most contagious. One person's gasp "
            "triggers the next person's orient, which triggers the next - a "
            "wave of widening eyes moving through a crowd faster than any "
            "explanation could. Emergency planners know this wave well: the "
            "crowd's cascade can outrun the facts, which is why clear, early "
            "information matters - it gives each person's appraisal something "
            "solid to land on instead of borrowing the neighbor's alarm.\n\n"
            "The skill is cascade management: recognizing 'this is the third "
            "surprise in ten minutes, my threshold is on the floor' and "
            "choosing to pause rather than react to each new ring as if it "
            "were the first. A person who can name the cascade - 'I am in a "
            "chain reaction right now' - regains the appraisal seat. The "
            "surprises keep coming, but they stop driving."
        ),
        "how_it_works": (
            "Stage the cascade: a fire alarm in an office. Surprise one: the "
            "alarm itself - auditory startle, everyone freezes (0-3 s). "
            "Surprise two: the stairwell is full of smoke - visual novelty, "
            "the map breaks again, threshold already lowered (10 s). Surprise "
            "three: a colleague shouts 'the elevators are out' - social "
            "trigger, the plan rewrites mid-step (30 s). Surprise four: "
            "outside, someone says 'it is just a drill' - cognitive whiplash, "
            "the threat appraisal collapses into embarrassment and laughter "
            "(5 min). Four surprises, four landings - startle, fear, urgency, "
            "sheepish relief - each one priming the next. Now replay with "
            "cascade management: after surprise two, a floor warden names it - "
            "'alarm is real, smoke is from the drill machine, walk, do not "
            "run' - and the chain breaks at link two because appraisal got "
            "solid ground. The scenario's moral: cascades are broken by "
            "information, delivered early, naming what is happening."
        ),
        "key_points": [
            "One surprise lowers the threshold, so the next small novelty surprises again.",
            "News cascades run by implication - each 'which means' is its own small shock.",
            "Social cascades spread person to person faster than explanations.",
            "Big announcements need pacing; five implications at once overwhelm appraisal.",
            "Naming the cascade - 'I am in a chain reaction' - returns the appraisal seat.",
        ],
        "requirements": [
            "Recall a day when surprises cascaded; count the links.",
            "Find the moment information (or its absence) steered the chain.",
        ],
        "standards": [
            "Emotional cascade models: sequential appraisal under lowered thresholds.",
            "Social contagion of affect: expression-to-expression transmission.",
            "Crisis communication: information pacing under alarm.",
        ],
        "citations": [CIT_SCHERER, CIT_LAZARUS],
        "sig_lens": (
            SIG_LENS_BELL + " One bell can set the whole carillon ringing - that "
            "is a cascade. The Signature reader learns the fire-warden's move: "
            "name what is happening, give the facts early, and ring the "
            "all-clear before the echoes multiply."
        ),
    },
    # -------------------------------------------------- BEHAVIOR
    {
        "key": "behaviors",
        "name": "What People Do When They Feel Surprise",
        "group": "Behavior",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "The first thing people do when surprised is nothing - the freeze. "
            "Ongoing action halts: the step stops mid-air, the sentence stops "
            "mid-word, the hand stops mid-reach. This is not indecision; it is "
            "the motor system yielding to the senses, buying a few hundred "
            "milliseconds of clean data before committing to a response. The "
            "freeze is so reliable that its absence is informative: a person "
            "who does not pause at startling news may not have registered it, "
            "or may be suppressing hard.\n\n"
            "What follows the freeze depends on the appraisal, and it follows "
            "fast. The orient: turning toward the trigger, approaching in "
            "small bursts, leaning in - the body investigating. The recoil: "
            "stepping back, hands up, creating distance - the body protecting. "
            "The reach: grabbing a companion's arm, pointing, waving others "
            "over - the body recruiting. These three - investigate, protect, "
            "recruit - cover most surprised behavior, and people often do all "
            "three in sequence: step back, lean in, grab a friend.\n\n"
            "Hands deserve their own paragraph because they are the most "
            "expressive part of surprised behavior. They fly to the mouth in "
            "astonishment, press flat to the chest in 'my heart' moments, "
            "shoot palm-up in disbelief, cover the face in overwhelm, or grip "
            "whatever is nearest for stability. The hands act before the mind "
            "edits, which makes them honest witnesses - interrogators and "
            "poker players alike watch hands, not faces, for the first "
            "unfiltered reaction.\n\n"
            "Finally there is the social behavior: telling. Surprises are "
            "among the most-told stories in human life - 'you will never "
            "guess what happened' - because telling replays the mismatch for "
            "an audience and harvests their gasps as a second helping of the "
            "feeling. Shared surprise bonds; retold surprise bonds again. "
            "The behavior of surprise, from freeze to telling, is the "
            "complete arc of a mind updating its map and then filing the "
            "update where others can find it."
        ),
        "how_it_works": (
            "Watch a plaza when a street performer suddenly breathes fire. "
            "Millisecond 0-500: the freeze - a dozen pedestrians halt mid-step, "
            "conversations cut off mid-syllable. Seconds 1-3: the orient - heads "
            "and bodies turn, a loose semicircle forms, phones rise; two people "
            "step back (recoil), one grabs their companion's sleeve (recruit). "
            "Seconds 3-10: hands narrate - to mouths, to chests, palm-up "
            "disbelief - and the first laughs and gasps ripple through the "
            "semicircle. Minutes later: the telling begins - strangers "
            "describing it to latecomers, videos sent with 'you had to be "
            "there,' the story already forming. The whole behavioral arc - "
            "freeze, orient, recoil, recruit, narrate, tell - ran in under "
            "five minutes, performed identically by people who had never met, "
            "because the behavior is the circuit made visible."
        ),
        "key_points": [
            "First behavior is the freeze: action halts so the senses get clean data.",
            "Then three moves: orient (investigate), recoil (protect), recruit (grab others).",
            "Hands are the honest witnesses: to mouth, to chest, palm-up, gripping.",
            "Telling the story afterward replays the mismatch and bonds the group.",
            "Absence of the freeze is informative - unregistered or suppressed.",
        ],
        "requirements": [
            "Watch hands, not faces, at the next surprising moment.",
            "Notice your own freeze: what were you doing when it stopped?",
        ],
        "standards": [
            "Behavioral ethology of the orienting response.",
            "Freeze as attentional-motor tradeoff.",
            "Social sharing of emotion: retelling as bonding.",
        ],
        "citations": [CIT_SOKOLOV, CIT_PANKSEPP],
        "sig_lens": (
            SIG_LENS_BELL + " Freeze, orient, act - the Signature drill for the "
            "hands as well as the head. The reader trains the sequence until it "
            "runs clean: stop, look, then move on purpose, never on reflex "
            "alone."
        ),
    },
    {
        "key": "speech",
        "name": "What Surprised People Say: Phrases and Speech",
        "group": "Behavior",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Surprised speech has a sound before it has words. The gasp, the "
            "'oh!', the sharp intake that is half-breath and half-voice - "
            "these are the unedited first utterances, produced before language "
            "comes online. They are nearly universal: every language has its "
            "surprise interjections, and they all share the open vowel and "
            "the rising pitch - the vocal equivalent of the widened eyes. "
            "Linguists note that these sounds sit at the border of language "
            "and reflex, which is why they survive translation: a gasp needs "
            "no dictionary.\n\n"
            "The first real words are almost always questions. 'What?' 'What "
            "was that?' 'Are you serious?' 'What just happened?' - the mind "
            "demanding the data its prediction missed. Repetition is common: "
            "'what, what, what' or 'no, no, no' - the speech system stuttering "
            "while appraisal catches up. Exclamations follow: 'unbelievable,' "
            "'no way,' 'I do not believe it' - each one literally narrating "
            "the prediction break. Listen to any crowd after a surprise and "
            "the soundtrack is questions and disbelief, the mind thinking out "
            "loud.\n\n"
            "Speech patterns change measurably. Rate speeds up or breaks into "
            "bursts - the rush to get the questions out. Pitch rises, "
            "sometimes dramatically; the voice gets higher because the whole "
            "vocal apparatus is tensed by the same arousal that widened the "
            "eyes. Volume jumps. Fluency drops: false starts, restarts, "
            "half-sentences - 'I - did you - wait, what?' Coherence returns "
            "as appraisal lands, usually within seconds, and the story of the "
            "surprise starts forming in complete sentences.\n\n"
            "There is also the speech of the surprise-giver to study: the "
            "build-up, the pause, the reveal. 'Close your eyes... okay, "
            "open!' - the pacing is a technology for manufacturing the "
            "prediction break at maximum size. Magicians, storytellers, and "
            "party planners are all engineers of surprised speech, designing "
            "the silence before the gasp. And the kindest version is the "
            "gentle reveal - soft voice, warning first - which shrinks the "
            "startle while keeping the delight."
        ),
        "how_it_works": (
            "Transcribe thirty seconds after unexpected news - 'the flight is "
            "cancelled, but you have been rebooked first class.' Second 1: "
            "the gasp - pure sound, no words. Seconds 2-4: 'what? wait, "
            "what?' - pitch up a full third, speech in bursts, the questions "
            "firing before answers exist. Seconds 5-10: 'no way - first "
            "class? are you serious?' - volume up, fluency still broken, "
            "disbelief narrating the prediction break. Seconds 10-20: "
            "appraisal lands - 'that is actually amazing' - pitch settling, "
            "sentences completing, laughter entering. Seconds 20-30: the "
            "telling begins - turning to a seatmate: 'you will not believe "
            "this.' The transcript shows the whole arc in miniature: reflex "
            "sound, questions, disbelief, landing, telling - the voice "
            "walking the same path as the body, half a second behind."
        ),
        "key_points": [
            "First utterances are pre-verbal: gasps and 'oh!' with open vowels and rising pitch.",
            "First words are questions and disbelief - the mind thinking out loud.",
            "Speech speeds up or bursts; pitch and volume rise; fluency drops, then recovers.",
            "The surprise-giver's pacing - build-up, pause, reveal - engineers the break.",
            "Gentle reveals shrink the startle while keeping the delight.",
        ],
        "requirements": [
            "Listen for the gasp-before-words in your next surprise.",
            "Notice your own pitch: how high does it go before settling?",
        ],
        "standards": [
            "Interjections at the language-reflex border.",
            "Prosody under arousal: pitch, rate, and fluency effects.",
        ],
        "citations": [CIT_SCHERER, CIT_PANKSEPP],
        "sig_lens": (
            SIG_LENS_BELL + " The voice is the bell's second beacon - the gasp "
            "is the ring made audible. The Signature reader lets the first "
            "sound out honestly, then brings the words back under command for "
            "the questions that matter."
        ),
    },
    {
        "key": "judgment",
        "name": "Surprise and Judgment: How It Tilts Decisions",
        "group": "Behavior",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Surprise does not just interrupt action - it tilts the machinery "
            "that makes decisions. The first tilt is toward caution: in the "
            "seconds after a prediction break, the mind discounts its own "
            "forecasts, because a forecast just failed publicly. People "
            "become temporarily more risk-averse, more likely to gather "
            "information, more inclined to wait. This is usually wise - the "
            "map just proved itself wrong, so driving slower while it "
            "redraws is simple prudence.\n\n"
            "The second tilt is in attention: surprise narrows focus to the "
            "trigger and starves everything else. In experiments, people "
            "shown a surprising image remember it vividly but forget what "
            "came right before and after - the attentional spotlight is so "
            "tight that the surroundings go dark. In real decisions this "
            "means the surprise gets overweighted: the shocking headline "
            "dominates the meeting, the startling number dominates the "
            "negotiation, while the quiet context that matters goes "
            "unconsidered. Good decision hygiene after a surprise is "
            "deliberately widening the spotlight again.\n\n"
            "The third tilt is emotional carryover. Surprise hands off to a "
            "partner emotion, and the partner colors the next decision - "
            "even unrelated ones. A startled investor may sell sound "
            "holdings; a pleasantly surprised diner may tip generously and "
            "agree to anything. The feeling is real but its target is "
            "borrowed: the arousal belongs to the surprise, the decision "
            "belongs to something else. Naming the carryover - 'I am deciding "
            "this while still buzzing from that' - is often enough to break "
            "its grip.\n\n"
            "The fourth tilt is the most useful: surprise improves learning. "
            "The prediction error that defines surprise is also the teaching "
            "signal the brain learns from - the mismatch is what updates the "
            "map. Decisions made after a surprise, once the arousal settles, "
            "are often better informed than decisions made before it, "
            "because the map is newer. The wise response to being surprised "
            "is not to decide faster or slower on principle, but to let the "
            "tilt pass, keep the lesson, and then decide with the updated "
            "map."
        ),
        "how_it_works": (
            "A hiring panel gets surprising news mid-deliberation: the top "
            "candidate just accepted elsewhere. Watch the tilts. Tilt one - "
            "caution: the panel suddenly doubts its second choice, although "
            "nothing about the second choice changed; forecasts feel "
            "untrustworthy. Tilt two - spotlight: the discussion fixates on "
            "the lost candidate for twenty minutes while the remaining "
            "candidates' files sit unopened. Tilt three - carryover: the "
            "disappointment bleeds into the evaluation, and solid candidates "
            "start looking gray. Then the chair intervenes with hygiene: a "
            "ten-minute break (let the arousal pass), a return to the files "
            "(widen the spotlight), and a re-vote (decide with the updated "
            "map). The second vote picks a candidate the panel is genuinely "
            "pleased with a month later. The surprise was real; the tilts "
            "were managed; the lesson - move faster on top candidates - was "
            "kept."
        ),
        "key_points": [
            "Tilt one: caution - forecasts feel untrustworthy right after one fails.",
            "Tilt two: spotlight - the surprise gets overweighted, context goes dark.",
            "Tilt three: carryover - the handoff emotion colors unrelated decisions.",
            "Tilt four: the useful one - prediction error is the brain's teaching signal.",
            "Hygiene: pause, widen the spotlight, name the carryover, then decide.",
        ],
        "requirements": [
            "After your next surprise, delay one decision by ten minutes and compare.",
            "Ask: am I deciding this, or is the buzz deciding it?",
        ],
        "standards": [
            "Affect and decision-making: arousal effects on risk and attention.",
            "Prediction-error learning: surprise as a teaching signal.",
            "Attentional narrowing under emotional arousal.",
        ],
        "citations": [CIT_LAZARUS, CIT_SCHERER, CIT_BARRETT],
        "sig_lens": (
            SIG_LENS_BELL + " The bell tilts the table - that is its nature. "
            "The Signature reader does not decide on a tilted table: they "
            "wait for it to level, keep the lesson the tilt taught, and then "
            "place their move deliberately."
        ),
    },
    {
        "key": "escalation",
        "name": "Escalation: Behavior Under Strong Surprise",
        "group": "Behavior",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "As surprise intensifies, behavior escalates through recognizable "
            "stages - and knowing the stages keeps a person from mistaking "
            "stage three for a character flaw. Stage one is the freeze and "
            "orient already described: stillness, then turning toward the "
            "trigger. This holds through moderate intensities and is fully "
            "functional. Stage two adds vocalization and recruitment: shouts, "
            "gasps, grabbing others, pointing - the individual response "
            "becoming a social one. The person is no longer just updating "
            "their own map; they are broadcasting the update.\n\n"
            "Stage three is where control starts to thin. At high intensity, "
            "the body may act before appraisal finishes: ducking, fleeing a "
            "step, shoving, shouting something unplanned. These are not "
            "decisions; they are the defense programs running on the raw "
            "mismatch before the verdict arrives. Afterward people often say "
            "'I do not know why I did that' - and they are telling the truth. "
            "The action belonged to the milliseconds before the mind caught "
            "up. Understanding this prevents the shame spiral: the shove was "
            "the circuit, not the character.\n\n"
            "Stage four is overload: the system takes in more novelty than "
            "appraisal can process. Behavior becomes disorganized - freezing "
            "that does not break, laughter at the wrong moment, contradictory "
            "actions, going blank. This is the mind's circuit breaker tripping "
            "to protect itself, and the correct response from bystanders is "
            "radical simplicity: one calm voice, one clear instruction, "
            "reduce input. Overload passes as the system catches up, usually "
            "within minutes, but pushing more information into it extends the "
            "trip.\n\n"
            "The escalation ladder matters most for people who work with "
            "surprise professionally - emergency responders, performers, "
            "teachers, parents. Their training is essentially stage "
            "management: recognizing which stage a person is in and matching "
            "it. Do not reason with stage three; give it a single clear "
            "action. Do not crowd stage four; reduce input and wait. And for "
            "oneself: the stages are weather, not identity. Everyone has all "
            "four stages in them; the difference is only where each person's "
            "thresholds sit."
        ),
        "how_it_works": (
            "A ceiling tile crashes down in a crowded waiting room. Stage one "
            "(0-2 s): forty people freeze mid-gesture, then orient - every "
            "head turns to the debris. Stage two (2-8 s): gasps and shouts, "
            "a woman grabs her child's arm, a man points and yells 'look "
            "out' - the response goes social. Stage three (8-20 s): a man "
            "near the debris shoves backward into the crowd, knocking someone "
            "over - no decision, just the defense program firing on raw "
            "mismatch; he apologizes, bewildered, seconds later. Stage four "
            "(20 s-2 min): an elderly woman stands frozen, laughing a little "
            "while tears run - contradictory, disorganized, the breaker "
            "tripped. The responder's stage management: to the shover, a "
            "single instruction - 'sir, step this way'; to the frozen woman, "
            "reduced input - a hand on her arm, 'you are safe, sit here,' "
            "nothing more. Within five minutes the room is orderly. The "
            "escalation ran its course; the management matched each stage."
        ),
        "key_points": [
            "Stage one: freeze and orient - functional through moderate intensity.",
            "Stage two: vocalize and recruit - the response goes social.",
            "Stage three: defense programs act before appraisal - 'I do not know why I did that' is true.",
            "Stage four: overload - disorganized behavior; answer with radical simplicity.",
            "Match the stage: single clear actions for stage three, reduced input for stage four.",
        ],
        "requirements": [
            "Learn to spot which stage you are in during your next strong surprise.",
            "Practice the bystander moves: one calm voice, one clear instruction.",
        ],
        "standards": [
            "Defense cascade: freeze, flight, fight sequencing under threat.",
            "Peritraumatic responses: disorganization under overwhelming novelty.",
            "Crisis intervention: input reduction and single-instruction techniques.",
        ],
        "citations": [CIT_LEDOUX, CIT_PANKSEPP],
        "sig_lens": (
            SIG_LENS_BELL + " The bell has four alarm levels, and the Signature "
            "reader learns all four the way a sailor learns weather - not to "
            "fear the storm, but to know which sail to set. Stage-matched "
            "response is the advanced drill."
        ),
    },
    # -------------------------------------------------- HEALTHY EXPRESSION
    {
        "key": "healthyexpr",
        "name": "Expressing Surprise Well",
        "group": "Healthy Expression",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Healthy expression of surprise starts with permission: let the "
            "first half-second happen. The gasp, the widened eyes, the freeze "
            "are the honest signal doing its job, and fighting them costs "
            "more than it saves - suppressed startles leak anyway, and the "
            "effort of suppression adds tension to an already aroused "
            "system. People who express surprise cleanly look more "
            "trustworthy, not less; the unedited reaction reads as honesty, "
            "and honesty is socially rewarded.\n\n"
            "The second step is narration - giving the surprise words once "
            "appraisal lands. 'Whoa, I did not expect that.' 'That startled "
            "me.' 'Give me a second.' These small sentences do large work: "
            "they tell the people around you what happened internally, they "
            "buy the seconds appraisal needs, and they convert a raw reflex "
            "into a shared event. The alternative - going silent and rigid - "
            "leaves others guessing, and guessed-at emotions are usually "
            "guessed wrong.\n\n"
            "The third step is channeling: putting the mobilized energy "
            "somewhere on purpose. Laughter is the classic channel - the "
            "shaky laugh after a false alarm is the body discharging on its "
            "own, and joining it consciously helps. Movement works too: the "
            "shake-out, the walk to the window, the deliberate breath. For "
            "pleasant surprises, channeling means savoring - letting the "
            "delight land fully instead of rushing past it to the logistics. "
            "For unpleasant ones, it means the pause before the response: "
            "feel the jolt, name it, then choose.\n\n"
            "The advanced form is the deliberate surprise - using the "
            "machinery on purpose and kindly. The well-timed reveal, the "
            "thoughtful plot twist in a toast, the gift hidden where it will "
            "be found: these are surprise expressions aimed outward, giving "
            "others the bright blank second as a gift. The ethics are simple: "
            "surprise given should delight, never endanger. A prank that "
            "risks the fear blend is not a gift; it is a gamble with someone "
            "else's nervous system."
        ),
        "how_it_works": (
            "Nadia gets the promotion she did not expect - announced in a "
            "meeting, all eyes on her. Healthy expression, step by step. Step "
            "one - permission: she gasps, her hands fly to her mouth, she "
            "does not fight it; the room sees the honest half-second and "
            "smiles. Step two - narration: 'Oh my god - I had no idea. Give "
            "me a second, I am - wow.' The words buy appraisal time and let "
            "everyone share the moment. Step three - channeling: she laughs, "
            "a real shaky one, stands, hugs the manager - the mobilized "
            "energy goes into warmth instead of freezing into stiffness. "
            "Later, savoring: she lets herself replay the announcement "
            "instead of jumping straight to the new responsibilities. "
            "Contrast the suppressed version - frozen smile, 'thanks,' "
            "sitting very still - which the room reads as odd and which "
            "leaves Nadia buzzing with unspent arousal for an hour. "
            "Permission, narration, channeling: the three-step expression "
            "that lets the bell ring clean."
        ),
        "key_points": [
            "Step one: permission - let the honest half-second happen; suppression costs more than it saves.",
            "Step two: narration - small sentences ('that startled me') buy appraisal time and share the event.",
            "Step three: channeling - laughter, movement, breath for the energy; savoring for the delight.",
            "Clean expression reads as honesty and is socially rewarded.",
            "Deliberate surprise given to others should delight, never endanger.",
        ],
        "requirements": [
            "Practice the narration sentences until they are automatic.",
            "After your next pleasant surprise, savor it for sixty seconds before the logistics.",
        ],
        "standards": [
            "Emotion expression and social trust: honest signals.",
            "Emotion regulation: response-focused strategies (Gross).",
            "Savoring: prolonging positive emotional experience.",
        ],
        "citations": [CIT_GROSS, CIT_EKMAN],
        "sig_lens": (
            SIG_LENS_BELL + " Permission, narration, channeling - the Signature "
            "three-step for a clean ring. The bell is rung to be heard; the "
            "reader lets it sound, names the note, and spends the echo well."
        ),
    },
    {
        "key": "unhealthy",
        "name": "Bottled Up or Blown Up: The Costs",
        "group": "Healthy Expression",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Surprise mishandled goes two directions, and both charge "
            "interest. Bottling up means suppressing the expression and "
            "pretending the jolt did not happen: the frozen smile, the "
            "'I am fine' through a pounding heart, the meeting continued as "
            "if nothing broke. The cost is physiological - suppression keeps "
            "the sympathetic system engaged longer, so the heart works "
            "harder and the tension has nowhere to go. It is social too: "
            "unexpressed surprise reads as coldness or indifference, and "
            "people who never show surprise are trusted less, because the "
            "honest signal never arrives.\n\n"
            "Worse, bottled surprise ferments. An unacknowledged startle "
            "does not vanish; it joins the aftershock account, lowering the "
            "threshold for the next one. A person who swallows three "
            "surprises before lunch is primed to snap at the fourth - not "
            "because the fourth was big, but because the account is full. "
            "The explosion that follows looks disproportionate to "
            "bystanders and feels shameful to the exploder, but the "
            "accounting is straightforward: unspent arousal plus lowered "
            "threshold equals overreaction.\n\n"
            "Blowing up is the other direction: letting every surprise "
            "drive behavior at full volume. The screamed reaction to the "
            "prank, the furious email after the schedule change, the "
            "melodrama over the minor plot twist of the day - each one "
            "spends social capital and trains the people around the "
            "exploder to manage them like weather. Chronic overreaction "
            "also trains the exploder's own system: the threshold drops "
            "further, the aftershocks lengthen, and ordinary novelty "
            "starts feeling like assault. The bell gets louder because it "
            "is rung harder.\n\n"
            "The middle path is not the absence of reaction but the "
            "right-sized one: feel it fully, express it cleanly, land it "
            "quickly. Both extremes share a root error - treating the "
            "surprise as bigger than it is. The bottler treats it as too "
            "dangerous to show; the exploder treats it as too big to "
            "contain. The accurate read - 'a jolt, now landing' - fits the "
            "response to the stimulus, and the books balance."
        ),
        "how_it_works": (
            "Two coworkers, same surprising email - the project is "
            "cancelled. Bottler: reads it, face still, says 'okay,' keeps "
            "typing. Inside: heart at 110, jaw clenched, the unspent "
            "arousal joining the morning's two earlier swallowed "
            "surprises. At 4 PM a printer jams and he shouts - the "
            "bystanders stare; the printer did not deserve it; he goes home "
            "ashamed and exhausted. Exploder: reads it, gasps loudly, "
            "stands up, announces the disaster to the floor, fires off an "
            "angry email to the client - then spends the afternoon managing "
            "the fallout of the email while colleagues quietly route around "
            "her. Middle path: reads it, exhales audibly - 'whoa, did not "
            "see that coming' - takes a walk, comes back, asks what the "
            "pivot is. Same email, three accountings. The books balance "
            "only in the third."
        ),
        "key_points": [
            "Bottling keeps the sympathetic system engaged longer - suppression has a physiological price.",
            "Unexpressed surprise ferments: the aftershock account fills, and the fourth small thing detonates it.",
            "Blowing up spends social capital and trains the threshold ever lower.",
            "Both extremes share the error: treating the surprise as bigger than it is.",
            "The middle path: feel fully, express cleanly, land quickly - books balanced.",
        ],
        "requirements": [
            "Audit your own pattern: bottler, exploder, or middle-path - and when each appears.",
            "Watch for the fermenting account: irritability after swallowed surprises.",
        ],
        "standards": [
            "Emotion suppression: physiological costs (Gross).",
            "Arousal accumulation and disproportionate responding.",
            "Display rules: social costs of chronic over- and under-expression.",
        ],
        "citations": [CIT_GROSS, CIT_EKMAN],
        "sig_lens": (
            SIG_LENS_BELL + " A bell rung and muffled still vibrates - the "
            "bottler's error. A bell hammered at every breeze cracks - the "
            "exploder's error. The Signature reader rings true: full tone, "
            "clean strike, and then silence until the next real news."
        ),
    },
    {
        "key": "practices",
        "name": "Everyday Practices That Keep Surprise in Balance",
        "group": "Healthy Expression",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Balance with surprise is not a single skill but a set of small "
            "habits, each cheap and each compounding. First: the recovery "
            "breath. After any startle, one slow exhale - longer out than in "
            "- tells the nervous system the alert is over. It takes four "
            "seconds and it works because the exhale directly engages the "
            "parasympathetic brake. People who practice it find their "
            "aftershocks shortening within weeks; the body learns the "
            "all-clear signal.\n\n"
            "Second: the narration habit. Keeping the small sentences ready - "
            "'that got me,' 'give me a moment,' 'okay, what now' - means "
            "appraisal gets its seconds without awkwardness. Third: the "
            "threshold audit. Once a week, notice what startled you and "
            "whether the threshold was fair - the tired Tuesday when "
            "everything jolted is information, not failure, and it prescribes "
            "rest, not self-criticism. Fourth: deliberate novelty. Seeking "
            "small chosen surprises - a new route, an unfamiliar food, a "
            "genre you never read - keeps the prediction system supple and "
            "the delight channel open. A system that never practices novelty "
            "treats all novelty as threat.\n\n"
            "Fifth: the gentle-reveal practice for others. Warning before "
            "the loud news, softening the prank, giving the 'heads up' - "
            "these are courtesies to other people's nervous systems, and "
            "they cost nothing. Sixth: the savoring pause. After pleasant "
            "surprises, sixty seconds of deliberate enjoyment - replaying "
            "the moment, telling someone - which trains the system to file "
            "surprise under 'sometimes wonderful,' balancing the ledger "
            "against the startles.\n\n"
            "None of these require a program or a purchase. They are "
            "housekeeping for the instrument: breathe after the ring, name "
            "the note, audit the threshold, practice novelty, warn others "
            "kindly, savor the good ones. Done daily, they keep the bell "
            "true - sensitive enough to warn, steady enough not to clamor "
            "at shadows."
        ),
        "how_it_works": (
            "A month of practice, compressed. Week one: after every startle, "
            "the recovery breath - four seconds, exhale long. The aftershock "
            "after the car backfire: three minutes instead of twenty. Week "
            "two: the narration sentences deployed at work - 'that got me, "
            "give me a moment' - and colleagues respond with patience "
            "instead of awkwardness. Week three: the threshold audit reveals "
            "the pattern - Thursdays, after the late meeting, everything "
            "jolts; the prescription is an earlier night, not a character "
            "flaw. Week four: deliberate novelty - a new running route, a "
            "mystery novel - and the delight channel visibly reopens; small "
            "surprises start landing as pleasure again. The gentle-reveal "
            "habit softens two pranks that would have misfired; the savoring "
            "pause banks the promotion news properly. None of it dramatic. "
            "All of it compounding. The bell, a month later, rings true."
        ),
        "key_points": [
            "The recovery breath: one slow exhale engages the parasympathetic brake - four seconds.",
            "Narration sentences ready in advance buy appraisal time gracefully.",
            "Weekly threshold audits turn 'everything jolts' into information, not failure.",
            "Deliberate novelty keeps the system supple and the delight channel open.",
            "Gentle reveals for others; sixty-second savoring for the good ones.",
        ],
        "requirements": [
            "Install the recovery breath this week - use it after every startle.",
            "Run one threshold audit: which day startled you most, and why?",
        ],
        "standards": [
            "Breathing-based autonomic regulation: extended exhale effects.",
            "Emotion-regulation habits: antecedent and response-focused practices.",
            "Savoring interventions in positive psychology.",
        ],
        "citations": [CIT_GROSS, CIT_LAZARUS],
        "sig_lens": (
            SIG_LENS_BELL + " Housekeeping for the instrument - the Signature "
            "reader maintains the bell the way a musician maintains an "
            "instrument: tuned, cleaned, played regularly, never left to "
            "rust or to clang unheeded."
        ),
    },
    # -------------------------------------------------- RECOGNIZING IT IN OTHERS
    {
        "key": "reading",
        "name": "Reading Surprise in Others: Face, Body, Voice, Behavior",
        "group": "Recognizing It in Others",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Reading surprise in others is the easiest read in the emotional "
            "repertoire, because the signal is designed to be read. Start "
            "with the face: the brow flash is the fastest tell - a quarter- "
            "second lift that precedes everything else. Then the trio: eyes "
            "widening, jaw dropping. In real time you will rarely analyze "
            "these separately; the gestalt hits as 'startled face,' and your "
            "own orienting response will have you looking at what they are "
            "looking at before you finish the thought.\n\n"
            "The body confirms: the freeze is the great corroborator. A "
            "person whose face flashes surprise and whose body halts mid- "
            "motion is genuinely interrupted - the two channels agree. Watch "
            "the hands: the freeze of the hands, the rise to the mouth or "
            "chest, the palm-up spread. A still face with frozen hands is "
            "suppressed surprise; an animated face with relaxed hands may be "
            "performed. The voice adds the third channel: the gasp, the "
            "pitch jump, the burst-pattern speech. Three channels agreeing "
            "is near-certain; one channel alone is a hypothesis.\n\n"
            "Context is the fourth channel and the one beginners skip. The "
            "same wide eyes mean different things at a surprise party "
            "(delight incoming), in a dark parking lot (fear incoming), and "
            "in a meeting where the numbers just changed (recalculation "
            "incoming). Read the room, not just the face: what just "
            "happened, what was expected, what is at stake. The skilled "
            "reader asks silently, 'what prediction just broke for this "
            "person?' - and the answer usually explains the whole tableau.\n\n"
            "Calibration matters more than talent. Everyone misreads "
            "sometimes - the brow flash of surprise vs the brow flash of "
            "skepticism, the gasp of delight vs the gasp of dismay. The "
            "fix is checking, not staring harder: 'you look surprised - "
            "what just landed?' People are usually glad to be asked, "
            "because being accurately read feels like being known. The goal "
            "of reading is never the gotcha; it is the bridge - seeing the "
            "interrupt so you can meet the person inside it."
        ),
        "how_it_works": (
            "A manager watches her team hear the reorganization news. Face "
            "channel: four brow flashes in the first second, two jaw drops. "
            "Body channel: three people freeze mid-note-taking; one leans "
            "back sharply; hands stop everywhere. Voice channel: a collective "
            "intake of breath, then burst-pattern questions - 'wait, what "
            "does that mean for -'. Context channel: the reorg was rumored "
            "but denied last week, so the prediction break is large and the "
            "stakes are jobs. Four channels agree: genuine, strong, "
            "negatively-tipped surprise. Her reading complete in five "
            "seconds, she does not plow ahead with the slides - she names "
            "it: 'That is a lot. Let us take ten minutes before questions.' "
            "The read was not the point; the response it enabled was. "
            "Contrast the misread version: plowing ahead while the room's "
            "bells are still ringing, and losing the room for the day."
        ),
        "key_points": [
            "The brow flash is the fastest tell; the trio (eyes, jaw) is the clearest.",
            "The freeze corroborates: face plus halted body means genuinely interrupted.",
            "Three channels agreeing (face, body, voice) is near-certain; one alone is a hypothesis.",
            "Context is the fourth channel: what prediction just broke, and what is at stake?",
            "Check, do not just stare: 'you look surprised - what just landed?'",
        ],
        "requirements": [
            "Practice the four-channel read on one real moment this week.",
            "When unsure, ask - being accurately read feels like being known.",
        ],
        "standards": [
            "Multichannel emotion recognition: face, body, voice integration.",
            "Context in emotion perception: situation as information.",
            "Active listening and checking as social skills.",
        ],
        "citations": [CIT_EKMAN, CIT_BARRETT],
        "sig_lens": (
            SIG_LENS_BELL + " The Signature reader reads others' beacons the "
            "way a sailor reads others' lights - not to judge the ship, but "
            "to navigate the shared water. Four channels, one question: what "
            "prediction just broke for them?"
        ),
    },
    {
        "key": "support",
        "name": "What to Say and Do When Someone Is Surprised",
        "group": "Recognizing It in Others",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "The first rule of meeting someone's surprise is timing: do not "
            "rush the landing. In the first seconds - the freeze, the wide "
            "eyes, the gasp - the person's appraisal is still forming, and "
            "anything you say becomes part of the data they are appraising. "
            "A calm presence and a quiet face are the best first response; "
            "they give the other nervous system something steady to "
            "synchronize with. The worst first response is more novelty - "
            "loud reassurance, sudden touch, a barrage of questions - which "
            "just rings the bell again.\n\n"
            "The second rule is naming without claiming. 'That startled "
            "you.' 'That was unexpected.' These sentences validate the "
            "interrupt without assigning it a meaning the person has not "
            "chosen yet. Avoid the verdict-stealers: 'it is nothing,' 'do "
            "not worry,' 'calm down' - each one argues with a nervous system "
            "that has not finished its own assessment, and argued-with "
            "nervous systems dig in. If the surprise is clearly pleasant, "
            "shared delight is the natural move - laugh with them, not at "
            "them. If it is clearly bad, the move is steady practicality: "
            "one clear piece of information, one simple next step.\n\n"
            "The third rule is pacing the aftermath. After a big surprise, "
            "people need the aftershock respected: lower the stimulation, "
            "offer the recovery breath by modeling it (breathe slowly "
            "yourself - it is contagious), and do not demand immediate "
            "decisions. 'We do not have to decide this now' is one of the "
            "kindest sentences in the language. For children, add "
            "translation: help them name what happened - 'the balloon "
            "popped and it was loud, and you are safe' - because children "
            "are still building the appraisal machinery and borrow yours.\n\n"
            "The fourth rule is the long game: remember. A person whose "
            "surprise you met well will trust you with the next one. A "
            "person whose startle you mocked will hide the next one - and "
            "hidden surprises ferment. The reputation for being safe to be "
            "startled around is built one well-met jolt at a time, and it "
            "is one of the finest reputations a person can hold."
        ),
        "how_it_works": (
            "Two responses to the same event: a friend opens the wrong door "
            "and finds the surprise party. Response A: the crowd screams "
            "louder, someone grabs her shoulders, three people shout "
            "questions - her freeze extends, the bell rings twice, and her "
            "first real feeling is overwhelm, not joy. Response B: the shout "
            "goes up once, then the nearest friend steps in with a calm "
            "smile and a hand - 'surprise! take a second, it is all friends "
            "here' - naming without claiming, pacing the aftermath. Her "
            "appraisal lands on 'safe and loved' within seconds, and the "
            "delight arrives clean. Same party, same guest, different "
            "first thirty seconds. The scenario's lesson in one line: meet "
            "the freeze with steadiness, the appraisal with naming, and the "
            "aftershock with patience - and the surprise becomes a gift "
            "instead of a second shock."
        ),
        "key_points": [
            "First: do not rush the landing - calm presence beats loud reassurance.",
            "Name without claiming: 'that startled you' validates without stealing the verdict.",
            "Avoid 'calm down' and 'it is nothing' - they argue with an unfinished appraisal.",
            "Pace the aftermath: lower stimulation, model slow breathing, defer decisions.",
            "For children, translate: name what happened and confirm safety - they borrow your appraisal.",
        ],
        "requirements": [
            "Memorize the three sentences: 'that startled you,' 'take a second,' 'we do not have to decide now.'",
            "Practice modeling the slow breath - it is contagious.",
        ],
        "standards": [
            "Co-regulation: calm presence and physiological synchrony.",
            "Emotion coaching: naming and validating without directing.",
            "Trauma-informed basics: safety, pacing, and choice after shock.",
        ],
        "citations": [CIT_GROSS, CIT_LAZARUS],
        "sig_lens": (
            SIG_LENS_BELL + " When another's bell rings, the Signature reader "
            "becomes the steady room the echo can settle in - no second "
            "ringing, no stolen verdicts, just steadiness, naming, and "
            "patience until the tone clears."
        ),
    },
    {
        "key": "nottodo",
        "name": "What Not to Do When Someone Is Surprised",
        "group": "Recognizing It in Others",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "The catalogue of mistakes is short and worth memorizing, "
            "because each one is common. Mistake one: startling on purpose "
            "without consent. The jump-scare prank, the air horn behind the "
            "desk, the 'boo' in the dark hallway - these borrow someone "
            "else's nervous system for entertainment, and they risk the "
            "fear blend, the stage-three defense response, and genuine "
            "distress. Consent is the entire ethics of deliberate surprise: "
            "haunted houses are fine because everyone opted in; the office "
            "is not a haunted house.\n\n"
            "Mistake two: mocking the reaction. Laughing at the flinch, "
            "replaying the gasp, the 'scaredy-cat' commentary - these punish "
            "the honest signal and teach the person to suppress next time. "
            "Suppressed surprise ferments, thresholds warp, and trust "
            "erodes. Laugh with the person once they are laughing; never "
            "make the laugh about the flinch itself.\n\n"
            "Mistake three: flooding the landing. Piling questions, "
            "information, or decisions onto someone mid-appraisal - 'are you "
            "okay what happened do you need -' - extends the freeze and can "
            "push stage two into stage four. The surprised mind processes "
            "serially; parallel input is noise. One voice, one sentence, "
            "then wait.\n\n"
            "Mistake four: correcting the feeling. 'You should not be "
            "surprised,' 'I told you this might happen,' 'overreacting much?' "
            "- each one denies the prediction break that just occurred in "
            "that person's map. Their map, their break, their feeling: "
            "arguing with it does not unring the bell, it just adds "
            "loneliness to the surprise. Mistake five: using the moment. "
            "The gotcha question, the staged reveal to win an argument, the "
            "surprise announcement deployed for maximum compliance - "
            "weaponized surprise spends trust at ruinous rates, because the "
            "person learns that novelty around you is unsafe. The common "
            "thread: every mistake treats the other person's bell as a toy, "
            "a target, or a tool. It is none of those. It is an instrument - "
            "handle it like one."
        ),
        "how_it_works": (
            "Replay the meeting where the layoffs were announced as a "
            "surprise. Mistake version: the news drops cold, the presenter "
            "plows into Q&A while faces are still frozen (flooding the "
            "landing), a manager chuckles at someone's audible gasp "
            "(mocking), another says 'we have been signaling this for "
            "months, nobody should be surprised' (correcting the feeling), "
            "and the whole thing was timed to prevent pushback (using the "
            "moment). Result: a room of people whose bells were mishandled "
            "in four ways at once - trust in leadership craters, and the "
            "aftershock lasts months. Repair version: the news is warned a "
            "day ahead ('difficult news tomorrow'), delivered plainly, "
            "followed by silence and then 'take the time you need; no "
            "decisions today,' with no mockery, no correction, no leverage. "
            "Same news. The difference is entirely in how the bells were "
            "handled - and the room remembers the handling longer than the "
            "headlines."
        ),
        "key_points": [
            "Never startle without consent - pranks risk the fear blend and real distress.",
            "Do not mock the flinch; punished honest signals get suppressed, and suppression ferments.",
            "Do not flood the landing: one voice, one sentence, then wait.",
            "Do not correct the feeling: their map, their break, their feeling.",
            "Never weaponize surprise - gotcha reveals spend trust at ruinous rates.",
        ],
        "requirements": [
            "Retire one startle-prank habit this month.",
            "Catch yourself before the mocking laugh - laugh with, never at the flinch.",
        ],
        "standards": [
            "Consent and autonomy in emotion elicitation.",
            "Psychological safety: the social costs of punished expression.",
            "Ethics of surprise in leadership and media.",
        ],
        "citations": [CIT_EKMAN, CIT_GROSS],
        "sig_lens": (
            SIG_LENS_BELL + " The Signature code for others' bells is simple "
            "and absolute: never ring one for sport, never mock its tone, "
            "never use its ringing as leverage. Bells are instruments, not "
            "toys - the reader's hands stay gentle."
        ),
    },
    # -------------------------------------------------- MIXES AND SIMULATION
    {
        "key": "emomap",
        "name": "The Surprise Emotion Map: Neighbors, Opposites, Cousins",
        "group": "Mixes and Simulation",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Place surprise on the map and its relationships come into focus. "
            "Nearest neighbors first: astonishment and amazement sit closest - "
            "both are surprise held a beat longer with the appraisal leaning "
            "positive, the 'wow' family. Startle is the bodily neighbor, the "
            "reflex without the cognitive appraisal - all alarm, no meaning "
            "yet. Bewilderment and confusion are the cousins who arrive when "
            "the prediction break does not resolve: surprise is the knock, "
            "confusion is the knock unanswered. Telling them apart matters: "
            "surprise wants information ('what was that?'), confusion wants "
            "explanation ('what does it mean?').\n\n"
            "Opposites: anticipation is surprise's true opposite - the "
            "forward-reaching forecast vs the forecast's failure. Boredom is "
            "the experiential opposite: the state of zero prediction breaks, "
            "the flat day with no bells. Interestingly, people flee boredom "
            "toward surprise-seeking - the appetite for novelty is partly the "
            "appetite to escape the flatline. Complacency is the attitudinal "
            "opposite: the settled certainty that nothing unexpected will "
            "happen, which is exactly the posture most vulnerable to the "
            "largest surprises.\n\n"
            "The close cousins need careful telling apart. Surprise vs "
            "shock: shock is surprise plus harm, the blend tipped hard "
            "negative with the system overwhelmed - all surprises interrupt, "
            "but only shocks injure. Surprise vs fear: the bodies match but "
            "the appraisals differ - fear has identified a threat, surprise "
            "has not finished looking. Surprise vs delight: delight is what "
            "surprise becomes when the news is good - the blend, not the "
            "raw material. Surprise vs wonder: wonder is surprise stretched "
            "over time and aimed upward - the sustained, reverent version, "
            "less interrupt and more contemplation.\n\n"
            "The map's practical use is diagnostic in the everyday sense: "
            "when a feeling is muddy, locating it on the map clarifies what "
            "it needs. Knock unanswered (confusion) needs explanation, not "
            "more data. Raw alarm without meaning (startle) needs the "
            "all-clear, not analysis. Delight needs savoring, not problem- "
            "solving. Each neighbor has its own handling, and the map is the "
            "index that says which page to open."
        ),
        "how_it_works": (
            "Run four muddy feelings through the map. Feeling one: 'I feel "
            "weird since the announcement.' Map check: the knock came but "
            "the meaning never landed - that is confusion, the unanswered "
            "knock; prescription: explanation, ask what it means for you. "
            "Feeling two: 'I keep jumping at small sounds since the alarm.' "
            "Map check: raw alarm, no new meaning - startle aftershock; "
            "prescription: the all-clear routine, recovery breaths, not "
            "analysis. Feeling three: 'I cannot stop smiling since the news.' "
            "Map check: the knock landed good - delight, the blend; "
            "prescription: savor it, tell someone, bank it. Feeling four: "
            "'I am flat and nothing surprises me anymore.' Map check: the "
            "experiential opposite - boredom, zero bells; prescription: "
            "deliberate novelty, wake the instrument. Same starting "
            "sentence - 'I feel weird' - four map locations, four different "
            "handlings. The map earns its keep."
        ),
        "key_points": [
            "Nearest neighbors: astonishment, amazement (the 'wow' family); startle (alarm without meaning).",
            "Bewilderment/confusion: the knock unanswered - surprise wants data, confusion wants explanation.",
            "Opposites: anticipation (forecast vs forecast-failure), boredom (zero bells), complacency.",
            "Cousins: shock (surprise plus harm), fear (threat identified), delight (good-news blend), wonder (sustained).",
            "The map is an index: locate the feeling to find its handling.",
        ],
        "requirements": [
            "Place your last three surprises on the map - which neighbor was each closest to?",
            "Practice the confusion vs surprise distinction: data or explanation?",
        ],
        "standards": [
            "Plutchik's wheel: adjacency, opposites, and dyads.",
            "Circumplex placement: surprise among neighboring states.",
            "Emotion differentiation: granularity and its benefits.",
        ],
        "citations": [CIT_PLUTCHIK, CIT_RUSSELL, CIT_BARRETT],
        "sig_lens": (
            SIG_LENS_BELL + " The map is the bell-founder's chart: every bell "
            "in the carillon, its neighbors, its opposite, its cousins. The "
            "Signature reader navigates by it - and when a feeling is muddy, "
            "they do not guess; they triangulate."
        ),
    },
    {
        "key": "blends",
        "name": "Surprise Blends: Four Famous Mixes",
        "group": "Mixes and Simulation",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Surprise rarely travels alone for long, and its most famous "
            "partnerships have names. Blend one: surprise plus joy equals "
            "delight. This is the surprise party that works, the gift that "
            "lands, the good news out of nowhere. Delight keeps surprise's "
            "brightness and adds joy's warmth - the gasp followed by the "
            "grin that will not leave. It is the blend humans chase most "
            "deliberately: whole industries - gifts, parties, plot twists, "
            "proposals - exist to manufacture it. Delight's signature is the "
            "laugh that comes easily and the story told for years.\n\n"
            "Blend two: surprise plus fear equals alarm. The midnight knock, "
            "the swerving car, the test result - the bright blank with the "
            "cold undertow. Alarm is the blend that keeps people safe and "
            "the one that misfires most: the prank that terrifies, the false "
            "alarm that ruins the night. Its handling is the fear protocol - "
            "safety first, information second, comfort third - because the "
            "fear layer, once engaged, must be stood down before the "
            "surprise layer can be appreciated.\n\n"
            "Blend three: surprise plus anger equals outrage. The betrayal "
            "revealed, the promise broken in public, the insult out of "
            "nowhere - the prediction break lands on something the person "
            "cared about, and the appraisal assigns blame. Outrage keeps "
            "surprise's interrupt power and aims it: the gasp becomes the "
            "'how dare you.' It is the most socially contagious blend - "
            "outrage recruits outrage - and the hardest to land well, "
            "because the anger layer wants action while the surprise layer "
            "is still updating the map.\n\n"
            "Blend four: surprise plus sadness equals disappointment. The "
            "hoped-for thing that was not, the news that quietly deflates - "
            "the bright blank followed not by a bang but by a sinking. "
            "Disappointment is surprise's gentlest loud blend: low arousal, "
            "long fade, the map updated downward. Its handling is the "
            "opposite of alarm's - not safety but meaning: grieving the "
            "forecast that failed, then redrawing it. Together the four "
            "blends show surprise's range as a mixer: the same neutral "
            "interrupt, four different landings, four different human "
            "stories."
        ),
        "how_it_works": (
            "One trigger, four blends - the cancelled flight, told four "
            "ways. Delight version: 'cancelled - but you are rebooked first "
            "class with lounge access.' The gasp becomes a grin; the story "
            "gets told for years. Alarm version: 'cancelled - and the "
            "replacement leaves in ten minutes from the far terminal.' The "
            "gasp stays a gasp; the body runs. Outrage version: 'cancelled - "
            "and the airline knew yesterday and told no one.' The gasp "
            "becomes 'how dare you'; the complaint is filed before the "
            "appraisal finishes. Disappointment version: 'cancelled - the "
            "trip is off, no alternatives.' The gasp sinks; the shoulders "
            "drop; the map redraws downward. Same raw material - one "
            "prediction break - four blends, four bodies, four stories. The "
            "blend is not in the trigger; it is in the landing, and the "
            "landing is where the skill lives."
        ),
        "key_points": [
            "Delight (surprise+joy): the chased blend - gasp to grin, stories told for years.",
            "Alarm (surprise+fear): the protector - handle with the fear protocol first.",
            "Outrage (surprise+anger): the contagious one - blame assigned mid-update.",
            "Disappointment (surprise+sadness): the gentle deflation - needs meaning, not safety.",
            "The blend is in the landing, not the trigger - that is where the skill lives.",
        ],
        "requirements": [
            "Sort your recent surprises into the four blends.",
            "Notice which blend you land in most - that is your default landing.",
        ],
        "standards": [
            "Plutchik's dyads: primary dyad formation rules.",
            "Blended affect: co-activation of appraisal systems.",
        ],
        "citations": [CIT_PLUTCHIK, CIT_SCHERER],
        "sig_lens": (
            SIG_LENS_BELL + " One bell, four peals - delight, alarm, outrage, "
            "disappointment. The Signature reader learns to hear which peal "
            "is sounding in themselves and others, because each peal asks "
            "for different handling."
        ),
    },
    {
        "key": "fullsim",
        "name": "From Trigger to Resolution: A Full Surprise Simulation",
        "group": "Mixes and Simulation",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "This is the archive's showcase: a complete surprise, simulated "
            "from trigger to resolution, with every layer this database has "
            "taught running at once. The scene: a quiet Saturday morning. "
            "Elena is making coffee, half-listening to the radio, thinking "
            "about nothing. The prediction map is at its most settled - "
            "home, morning, routine - which means the gap, when it comes, "
            "will be at its widest. Through the kitchen window she sees "
            "something that cannot be there: her brother's car in the "
            "driveway. Her brother lives three thousand miles away and was "
            "'definitely not coming' for the holidays. The mismatch is "
            "total.\n\n"
            "Milliseconds 0-300: the freeze. Her hand stops mid-pour; "
            "coffee overflows the cup unnoticed. The startle circuit was "
            "not even needed - this is pure cognitive surprise, no bang - "
            "but the orient fires anyway: head turns, eyes lock on the car, "
            "brows fly up, jaw drops. The radio keeps playing to an empty "
            "room. Second 1-3: the questions flood - 'is that his car, is "
            "he here, what is happening' - and the body joins late: heart "
            "rate climbing, breath shallow, a strange lightness in the "
            "limbs. The aftershock has not started; this is still the "
            "peak, the bright blank at full brightness.\n\n"
            "Seconds 3-10: the door opens and he is really there, grinning, "
            "arms open - and the appraisal lands like sunlight. The blend "
            "tips hard toward delight: the gasp becomes a shriek of joy, "
            "the frozen hand finally sets down the pot, and she is across "
            "the kitchen before thought resumes. The discharge is total - "
            "laughter, tears, shaking hands, repeated 'I cannot believe "
            "you are here.' The neighbors, hearing the shriek, get the "
            "social cascade version: their own small surprise, orienting "
            "toward the sound, landing on curiosity.\n\n"
            "Minutes 10-60: the telling begins, and it will continue for "
            "years - 'you should have seen my face.' The map updates: "
            "brother is the kind of person who flies three thousand miles "
            "unannounced. The aftershock runs warm: every small sound that "
            "morning gets a glance, the threshold lowered but the valence "
            "positive - the house feels more alive. That evening, the "
            "savoring: replaying the moment at dinner, the story already "
            "polished. The simulation's ledger: one total prediction break, "
            "a three-second peak, a delight landing, a map permanently "
            "updated, a story for the family archive. Every layer - "
            "definition, time-course, body, face, trigger, behavior, "
            "expression, recognition, blend - ran in under a minute, in "
            "order, exactly as this database describes. That is what the "
            "archive means by simulation: the whole instrument, playing "
            "the whole piece."
        ),
        "how_it_works": (
            "Replay the simulation as a scored timeline, the way the "
            "archive's scenario simulator would run it. T+0.0s: trigger - "
            "brother's car in driveway; prediction gap: maximum (certainty "
            "'not coming' vs reality 'here'). T+0.3s: freeze - hand "
            "mid-pour, coffee overflowing; orient - head turn, brow flash, "
            "jaw drop. T+1-3s: peak - bright blank, questions flooding, "
            "heart rate 72 to 104, breath shallow. T+3-10s: appraisal - "
            "brother confirmed, safe, joyful; blend locks to delight; "
            "discharge - shriek, laughter, tears, shaking. T+10s-10min: "
            "telling begins; social cascade to neighbors; map updates "
            "'brother flies in unannounced.' T+10-60min: warm aftershock, "
            "lowered threshold, heightened aliveness; savoring at dinner. "
            "T+years: the story, retold, the map's permanent edit. Each "
            "timestamp carries the layer it demonstrates - freeze (body), "
            "brow flash (face), questions (speech), delight (blend), "
            "telling (behavior), update (learning). The simulator's output "
            "is this timeline: the emotion as a scored piece of music, "
            "every instrument audible."
        ),
        "key_points": [
            "The showcase: every layer of the database running at once, in order.",
            "Cognitive surprise needs no bang - a total prediction break suffices.",
            "The peak is seconds; the telling lasts years - the story outlives the feeling.",
            "Warm aftershock: lowered threshold with positive valence feels like aliveness.",
            "The map's permanent edit: 'he is the kind of person who does this.'",
            "The simulator's output is a scored timeline - the emotion as music.",
        ],
        "requirements": [
            "Score one of your own big surprises as a timeline: trigger, freeze, peak, appraisal, discharge, telling.",
            "Notice which layers you can now name that you could not before this database.",
        ],
        "standards": [
            "Full time-course integration: onset through narrative consolidation.",
            "Autobiographical memory: surprise as a story anchor.",
            "Simulation as pedagogy: scored scenarios for emotion learning.",
        ],
        "citations": [CIT_SCHERER, CIT_BARRETT, CIT_PLUTCHIK],
        "sig_lens": (
            SIG_LENS_BELL + " The full peal: trigger, freeze, peak, appraisal, "
            "discharge, telling, update - the bell rung, heard, answered, and "
            "filed. The Signature reader who can score a surprise like this "
            "can meet any ringing with steadiness, because they have heard "
            "the whole piece before."
        ),
    },
]
