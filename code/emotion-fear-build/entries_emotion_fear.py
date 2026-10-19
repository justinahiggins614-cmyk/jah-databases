#!/usr/bin/env python3
"""Seed entries for The Fear Emotion Database (emotion-fear) and its
Signature edition (emotion-fear-signature).

Manon's 2026-10-17 16:15 order: one database per emotion — describe and
simulate the emotion of fear and human behavior around it. 34 records,
ladder-ordered simple -> compounded -> complex, following the shared
emotion template (description -> first-person simulation -> body signals ->
facial expression -> triggers -> behavior -> healthy expression ->
recognizing it in others -> mixes -> full behavioral simulation).

Public edition: real, fact-checked psychology knowledge about fear —
descriptive and educational only. Never diagnoses real people, never labels
any real person, no clinical language, no diagnostic labels, general safe
everyday guidance only.

Signature edition: the same ladder reframed through the Signature lens —
fear as the early-warning instrument of the Signature system. Titles carry
" (Signature Edition)", src is "signature", clearly labeled Signature-made,
never presented as authentic public record.
"""

SIG_TAIL = ("Signature-made record: an original Signature interpretation of "
            "this fear knowledge, clearly labeled as Signature-made and never "
            "presented as an authentic public record.")

ENTRIES = [
{
    "key": "fear-definition",
    "name": "What Fear Is: A Plain-Language Definition",
    "group": "What Fear Is",
    "ladder_rank": 1,
    "ladder_tier": "foundations",
    "description": (
        "Fear is the emotion that arrives when something feels threatening right now. "
        "It is the mind and body's alarm system: a fast, whole-body signal that says "
        "\"something here might hurt me — pay attention and get ready.\" Long before people "
        "had words for it, fear kept living things alive by making them freeze, run, or "
        "fight when danger appeared, and it still does that job today. When you feel fear, "
        "several things happen at once. Your body revs up — heart beating faster, breath "
        "quickening, muscles tensing. Your attention narrows onto the threat, the way a "
        "flashlight beam tightens in the dark. And an urge to act rises: get away, get "
        "still, get help, or stand your ground. Fear is not a character flaw and not a sign "
        "of weakness. It is information. Like pain tells you to pull your hand from a hot "
        "stove, fear tells you to take a threat seriously. The feeling itself is neutral — "
        "what matters is what it is pointing at and what you do next. Everyone feels fear. "
        "Brave people feel it too; they have simply practiced deciding what to do while "
        "the alarm is ringing. Understanding fear starts here: it is a built-in protector, "
        "old as life itself, speaking in the language of the body."
    ),
    "how_it_works": (
        "Fear works as a rapid detection-and-response loop. The senses pick up something — "
        "a sudden sound, a looming shape, a remembered warning — and the brain's threat "
        "detectors react in a fraction of a second, before deliberate thought catches up. "
        "That is why fear can hit before you know why you are afraid. The body then "
        "mobilizes: stress hormones surge, the heart pumps harder, breathing quickens, and "
        "energy is routed to the muscles. Attention locks onto the possible danger while "
        "everything else fades into the background. Finally, the urge to act pushes toward "
        "one of the classic moves — freeze, flee, fight, or call for help — and the thinking "
        "mind gets its turn, checking whether the alarm matches the real situation. When "
        "the threat passes or proves harmless, the loop winds down and the body settles."
    ),
    "key_points": [
        "Fear is an alarm signal about a present, perceived threat — not a flaw.",
        "It has three parts at once: body arousal, narrowed attention, and an urge to act.",
        "It can fire before conscious thought — the feeling may arrive before the reason.",
        "The classic action urges are freeze, flee, fight, or seek help.",
        "Fear is information; what matters is what it points at and what you do next.",
        "Courage is not the absence of fear — it is deciding well while afraid.",
    ],
    "requirements": [
        "An everyday example of a scare to picture while reading",
        "Willingness to notice what your own body does when startled",
        "A few quiet minutes — this is the foundation for the whole ladder",
    ],
    "standards": [
        "Basic-emotions framework: fear as a primary emotion (Ekman)",
        "Fight-or-flight response model (Cannon, 1915)",
        "Threat-detection circuitry (LeDoux)",
        "Appraisal theory: perceived threat drives the emotion (Lazarus)",
    ],
    "citations": [
        "Cannon, W. B. Bodily Changes in Pain, Hunger, Fear and Rage. Appleton; 1915.",
        "Ekman, P. Emotions Revealed. 2nd ed. Holt; 2007.",
        "LeDoux, J. The Emotional Brain. Simon & Schuster; 1996.",
        "Lazarus, R. S. Emotion and Adaptation. Oxford University Press; 1991.",
    ],
    "sig_lens": (
        "Through the Signature lens, fear is the early-warning instrument of the human "
        "system — the first bell in the Signature watchtower. The Signature reader does "
        "not fight the bell or worship it; he reads it. Every surge of fear is treated as "
        "a sealed message: name the threat, measure it, then answer with a chosen move. "
        "In the Signature method the alarm is a covenant — the body warns, the mind "
        "decides, and the decision is always the person's own."
    ),
},
{
    "key": "fear-family",
    "name": "Fear in the Emotion Family",
    "group": "What Fear Is",
    "ladder_rank": 1,
    "ladder_tier": "foundations",
    "description": (
        "Fear belongs to the family of basic emotions — the small set of feelings that "
        "appear across all human cultures, show on the face in the same way everywhere, "
        "and show up very early in life. Researchers who study faces and feelings place "
        "fear alongside joy, sadness, anger, surprise, and disgust as one of the core "
        "building blocks from which more complicated feelings are made. Think of basic "
        "emotions as primary colors: just as blue and yellow mix into green, fear mixes "
        "with other basics to make the subtle shades of everyday emotional life. Fear plus "
        "surprise makes the jolt of being startled. Fear plus anger makes the hot urge to "
        "fight back when cornered. Fear plus sadness makes a heavy, hopeless dread. And "
        "fear plus joy makes the strange delight of a roller coaster — scary and fun at "
        "once. Fear also has close cousins that are easy to confuse with it. Anxiety is "
        "fear's forward-looking cousin: fear answers \"danger is here,\" while anxiety "
        "answers \"danger might come.\" Startle is fear's faster, simpler sibling — a reflex "
        "blink-and-jump that fires and fades in a second, while true fear lingers and "
        "thinks. Knowing where fear sits in the family helps you name what you feel more "
        "precisely, and a precise name is the first step to handling it well."
    ),
    "how_it_works": (
        "Emotion researchers map feelings the way cartographers map land: by finding the "
        "big landmarks first. The basic emotions are the landmarks — each with its own "
        "facial expression, body pattern, and job to do. Fear's job is protection from "
        "immediate harm. From these landmarks, complex feelings are built by blending. "
        "Blending happens automatically: the brain rarely serves one pure emotion at a "
        "time, so what you feel on a hard day is usually a mix with fear as one "
        "ingredient. Learning the family works like learning instruments in an orchestra — "
        "once you can hear the fear horn by itself, you can pick it out even when the "
        "whole orchestra is playing."
    ),
    "key_points": [
        "Fear is a basic emotion: universal, early-appearing, with a signature face.",
        "Basic emotions blend like primary colors into complex everyday feelings.",
        "Fear plus surprise gives startle; fear plus anger gives the fight urge.",
        "Anxiety is fear's forward-looking cousin (might happen vs happening now).",
        "Startle is a fast reflex; fear lingers and involves appraisal.",
        "Naming the exact feeling is the first step to handling it well.",
    ],
    "requirements": [
        "The definition record fresh in mind — this one builds on it",
        "A recent mixed feeling to un-blend as a practice example",
    ],
    "standards": [
        "Basic-emotions framework (Ekman)",
        "Wheel of emotions: fear and its dyads (Plutchik)",
        "Appraisal theory (Lazarus)",
        "Two-factor theory: arousal plus interpretation (Schachter and Singer)",
    ],
    "citations": [
        "Ekman, P., and Friesen, W. V. Constants across cultures in the face and emotion. Journal of Personality and Social Psychology; 1971.",
        "Plutchik, R. Emotions and Life: Perspectives from Psychology, Biology, and Evolution. APA; 2003.",
        "Schachter, S., and Singer, J. Cognitive, social, and physiological determinants of emotional state. Psychological Review; 1962.",
        "Darwin, C. The Expression of the Emotions in Man and Animals. John Murray; 1872.",
    ],
    "sig_lens": (
        "Through the Signature lens, the emotion family is a full instrument panel, and "
        "fear is the red warning lamp among steady dials. The Signature method teaches "
        "reading the whole panel at once: when the red lamp burns alongside the anger "
        "gauge or the sorrow gauge, the wise operator names the blend before touching "
        "any control. Precision in naming is a Signature discipline — the lamp is never "
        "mistaken for the whole machine."
    ),
},
{
    "key": "fear-volumes",
    "name": "Fear at Three Volumes: Mild, Moderate, Intense",
    "group": "What Fear Is",
    "ladder_rank": 2,
    "ladder_tier": "foundations",
    "description": (
        "Fear is not one fixed size — it comes at different volumes, the way sound can be "
        "a whisper, a conversation, or a siren. At low volume it is unease: a faint "
        "restlessness, like walking down a dark hallway and feeling the hairs on your "
        "neck lift. Your body barely stirs — maybe a slightly quicker heartbeat — but your "
        "attention sharpens and you start scanning. Mild fear is often useful; it is the "
        "nudge that makes you double-check the locked door or look both ways. At medium "
        "volume it is plain fear: the heart pounds, the breath comes faster, the stomach "
        "tightens, and the urge to act gets loud — leave, hide, get help. Thinking gets "
        "narrower; it is harder to weigh options calmly because the alarm is using most of "
        "the mind's bandwidth. At high volume it is terror: the full siren. The body may "
        "shake, the mind may go blank or race, and behavior becomes urgent and simple — "
        "run now, freeze totally, scream. Afterwards people often feel shaky and wrung "
        "out, like a muscle that has been clenched too long. The same threat can play at "
        "different volumes in different people, and the volume knob is turned by how "
        "dangerous the threat seems, how much control you feel, and what happened last "
        "time. Learning to estimate the volume — \"is this a 3 or an 8?\" — is one of the "
        "most practical fear skills there is, because the response that fits a 3 would be "
        "silly for an 8, and the response for an 8 would be overkill for a 3."
    ),
    "how_it_works": (
        "The volume of fear is set by appraisal — the brain's rapid estimate of danger "
        "versus coping. A threat judged big, close, and uncontrollable turns the volume "
        "up; the same threat judged manageable turns it down. The body then matches the "
        "volume: mild fear gets a light touch of arousal, intense fear gets the full "
        "hormonal surge. Because appraisal runs partly below awareness, the volume can "
        "feel automatic — but each new piece of information (the sound was just the wind, "
        "a friend is beside me) re-runs the estimate and can lower the dial. That is why "
        "fear so often fades the moment a situation is understood."
    ),
    "key_points": [
        "Fear ranges from mild unease through plain fear to intense terror.",
        "Mild fear sharpens attention and is often useful.",
        "Moderate fear narrows thinking and shouts an urge to act.",
        "Intense fear can blank the mind and drive urgent, simple behavior.",
        "The volume knob is turned by perceived danger, control, and past experience.",
        "Estimating the volume (3 or 8?) guides a fitting response.",
    ],
    "requirements": [
        "Three personal memories: one mild scare, one medium, one strong",
        "Honesty about which volume each really was",
    ],
    "standards": [
        "Arousal-performance curve: moderate arousal can sharpen function (Yerkes and Dodson)",
        "Appraisal theory (Lazarus)",
        "Fight-or-flight graded response (Cannon)",
    ],
    "citations": [
        "Yerkes, R. M., and Dodson, J. D. The relation of strength of stimulus to rapidity of habit-formation. Journal of Comparative Neurology and Psychology; 1908.",
        "Lazarus, R. S. Emotion and Adaptation. Oxford University Press; 1991.",
        "Cannon, W. B. Bodily Changes in Pain, Hunger, Fear and Rage. Appleton; 1915.",
    ],
    "sig_lens": (
        "Through the Signature lens, fear's volume is a gauge to be read, not a storm to "
        "be obeyed. The Signature reader asks the gauge one question — \"what number are "
        "you?\" — and answers in proportion: a 3 gets a glance, an 8 gets a plan. "
        "Overreaction to a 3 and underreaction to an 8 are both failures of measurement, "
        "and the Signature method trains the measuring hand first."
    ),
},
{
    "key": "fear-myths",
    "name": "Myths and Misunderstandings About Fear",
    "group": "What Fear Is",
    "ladder_rank": 2,
    "ladder_tier": "foundations",
    "description": (
        "Fear collects myths the way old houses collect dust, and the myths make the "
        "feeling harder to carry. Myth one: feeling fear means you are weak or cowardly. "
        "False — fear is a built-in alarm, and even the bravest people hear it ring; "
        "courage is acting wisely while it rings, not never hearing it. Myth two: you "
        "should be able to think fear away instantly with logic. Feelings are not "
        "debates; telling a pounding heart \"there is nothing to fear\" is like telling a "
        "smoke detector to be quiet while the toast burns. Understanding helps, but the "
        "body needs time to stand down. Myth three: fear is always irrational and should "
        "be ignored. Sometimes fear is the only one in the room paying attention — the "
        "unease before a risky shortcut has saved many a person. The skill is checking "
        "the alarm, not smashing it. Myth four: brave people eliminate fear. In truth, "
        "people who face hard things regularly still feel fear; they have just built "
        "familiar paths through it. Myth five: if you feel no fear, you are safe. Not "
        "feeling fear can mean the alarm is broken, ignored, or drowned out — which is "
        "its own danger. Myth six: fear means something is wrong with you. Fear means "
        "something seems wrong around you. That small shift — from \"I am broken\" to "
        "\"my alarm is ringing\" — changes everything about how the feeling is carried."
    ),
    "how_it_works": (
        "Myths about fear work like bad instruction manuals: they tell people to fight "
        "the alarm instead of reading it. Shame about feeling fear adds a second layer — "
        "fear of the fear — which turns the volume up instead of down. Replacing a myth "
        "with a fact (\"this is my alarm, not my character\") removes that second layer, "
        "and the original fear becomes simpler to handle. Each myth dissolved is one less "
        "obstacle between the feeling and a good response."
    ),
    "key_points": [
        "Feeling fear is not weakness — even brave people feel it.",
        "Logic alone rarely silences fear instantly; the body needs time.",
        "Fear is sometimes the only one paying attention — check it, do not smash it.",
        "Familiarity builds paths through fear; it does not delete the feeling.",
        "No fear at all can mean a broken or ignored alarm.",
        "\"My alarm is ringing\" is kinder and truer than \"I am broken.\"",
    ],
    "requirements": [
        "One fear myth you have heard or believed",
        "Willingness to trade it for the fact",
    ],
    "standards": [
        "Basic-emotions framework (Ekman)",
        "Appraisal theory (Lazarus)",
        "Display rules and emotion regulation (Ekman and Friesen)",
    ],
    "citations": [
        "Ekman, P. Emotions Revealed. 2nd ed. Holt; 2007.",
        "Lazarus, R. S. Emotion and Adaptation. Oxford University Press; 1991.",
        "James, W. What is an emotion? Mind; 1884.",
    ],
    "sig_lens": (
        "Through the Signature lens, myths are counterfeit maps, and the Signature "
        "reader burns them. \"Fear means I am weak\" is a forged document — the true "
        "record reads \"the instrument sounded; the operator remains.\" In the Signature "
        "method, no one apologizes for the bell. They log it, read it, and answer it, "
        "and that unashamed reading is itself a form of strength."
    ),
},
{
    "key": "fear-firstperson",
    "name": "Inside Fear: A First-Person Passage",
    "group": "How Fear Feels",
    "ladder_rank": 3,
    "ladder_tier": "foundations",
    "description": (
        "Step inside the feeling for a moment — this is what fear is like from the "
        "inside, in the seconds when it owns you. It starts with a catch: something is "
        "wrong, and you know it before you know what it is. Your chest tightens as if a "
        "hand closed around your ribs. Your heart, which a moment ago was background "
        "music, becomes a drum — loud, fast, impossible to ignore. Sound changes: the "
        "room gets quieter and louder at the same time, every small noise suddenly "
        "meaningful. Your thoughts narrow to a single bright thread — the threat — and "
        "everything else, the groceries, the plans for tomorrow, slides out of reach. "
        "There is a cold feeling at the back of the neck, a lightness in the hands that "
        "want to either grip something or let go of everything. Time does something odd: "
        "it both races and stretches, so a single second feels long enough to think three "
        "thoughts in. Underneath it all runs a wordless urge — move, do something, do it "
        "now — and a smaller, quieter voice trying to do the math: how bad is this, "
        "really? what are my options? That is fear from the inside: an ancient alarm "
        "ringing in a modern mind, loud and physical and utterly convinced that this "
        "moment matters. Reading this passage is a rehearsal — the next time the alarm "
        "rings for real, some part of you will recognize the weather and remember that "
        "storms pass."
    ),
    "how_it_works": (
        "First-person simulation works as emotional rehearsal. The brain treats vividly "
        "imagined feelings partly like real ones, so walking through fear in words builds "
        "familiarity without danger. Familiarity is the enemy of panic: the second time "
        "the alarm rings, the thinking mind recognizes the pattern sooner and joins the "
        "conversation earlier. That is why this record asks you to step inside — not to "
        "scare you, but to make the feeling a known place rather than a strange one."
    ),
    "key_points": [
        "Fear announces itself first as a wordless \"something is wrong.\"",
        "The heart becomes loud and central; sound and time feel altered.",
        "Thoughts narrow to the threat; everything else slides away.",
        "A wordless urge to move runs under a smaller voice doing the math.",
        "Imagined walkthroughs build familiarity, and familiarity steadies.",
        "Recognizing the weather helps you remember that storms pass.",
    ],
    "requirements": [
        "A safe, calm setting for reading — not before sleep",
        "Permission to stop and breathe if the passage feels strong",
    ],
    "standards": [
        "Phenomenology of emotion: first-person description as data (James)",
        "Basic-emotions framework (Ekman)",
        "Appraisal theory (Lazarus)",
    ],
    "citations": [
        "James, W. What is an emotion? Mind; 1884.",
        "Ekman, P. Emotions Revealed. 2nd ed. Holt; 2007.",
        "Damasio, A. The Feeling of What Happens. Harcourt; 1999.",
    ],
    "sig_lens": (
        "Through the Signature lens, stepping inside fear is a training drill, not a "
        "punishment. The Signature reader walks the alarm corridor on purpose, in "
        "daylight, so that when the real bell rings at midnight the feet already know "
        "the floor. Every rehearsal is logged as preparation: the instrument is studied "
        "before it is needed, and the operator is never a stranger to his own signals."
    ),
},
{
    "key": "fear-arc",
    "name": "The Arc of Fear: Onset, Peak, Fading, Aftershock",
    "group": "How Fear Feels",
    "ladder_rank": 3,
    "ladder_tier": "foundations",
    "description": (
        "Fear has a shape in time — an arc with four acts. Act one is onset: the alarm "
        "trips, fast. Sometimes it is instant, a single sound flipping the whole body "
        "into alert in half a second; sometimes it creeps, a worry thickening minute by "
        "minute as the appointment approaches. Act two is the peak: the loudest moment, "
        "when the heart hammers hardest and the urge to act is strongest. Peaks are "
        "surprisingly short — the body cannot hold maximum alarm for long, and most "
        "peaks crest and start falling within minutes. Act three is fading: the threat "
        "passes, or understanding arrives (\"it was only the wind\"), or a coping move "
        "works, and the body stands down in waves. The heart slows, the breath deepens, "
        "the shoulders drop — often with a shaky laugh or a long sigh that surprises "
        "you. Act four is the aftershock: the strange echo after the fear is gone. Hands "
        "may tremble, you may feel oddly tired or oddly wired, small sounds may startle "
        "you more than usual for a while. The aftershock is not a malfunction; it is the "
        "system powering down, the way an engine ticks as it cools. Knowing the arc "
        "changes the experience of fear completely. At the peak, when it feels like it "
        "will last forever, you can remind yourself: this is act two. Act three is "
        "already on its way."
    ),
    "how_it_works": (
        "The arc follows the body's stress chemistry. Onset is the surge of adrenaline — "
        "fast in, fast out. The peak is the moment of maximum mobilization, which is "
        "metabolically expensive and cannot be sustained, so it must fall. Fading is the "
        "parasympathetic system reapplying the brakes: heart rate down, digestion back "
        "online. The aftershock is residual arousal plus a sensitized startle reflex — the "
        "alarm stays a little jumpy while it recalibrates. Each phase has its own logic, "
        "which is why fighting the peak with pure willpower fails while riding it out "
        "works."
    ),
    "key_points": [
        "Onset can be instant or creeping; both are normal.",
        "The peak is the loudest moment — and it cannot last long.",
        "Fading comes in waves as the threat passes or is understood.",
        "Aftershock (trembling, tiredness, jumpiness) is the system cooling down.",
        "Knowing the arc helps: at the peak, act three is already coming.",
    ],
    "requirements": [
        "One remembered scare to trace through the four acts",
        "A clock or timer to notice how short peaks really are",
    ],
    "standards": [
        "Fight-or-flight temporal dynamics (Cannon)",
        "Stress-response phases: alarm, resistance, recovery (Selye)",
        "Appraisal and reappraisal over time (Lazarus)",
    ],
    "citations": [
        "Cannon, W. B. Bodily Changes in Pain, Hunger, Fear and Rage. Appleton; 1915.",
        "Selye, H. The Stress of Life. McGraw-Hill; 1956.",
        "Lazarus, R. S. Emotion and Adaptation. Oxford University Press; 1991.",
    ],
    "sig_lens": (
        "Through the Signature lens, the arc of fear is a four-act protocol the body "
        "runs without asking permission — and the Signature reader learns the script by "
        "heart. Onset is the page turning; the peak is the loudest line, never the whole "
        "play; fading is the curtain easing down; aftershock is the theater emptying. "
        "Knowing the script means never mistaking act two for the ending."
    ),
},
{
    "key": "fear-low-high",
    "name": "Low Fear and High Fear: Two Lived Snapshots",
    "group": "How Fear Feels",
    "ladder_rank": 4,
    "ladder_tier": "foundations",
    "description": (
        "Two snapshots, same emotion, different volumes — compare them side by side. "
        "Snapshot one, low fear: you are home alone in the evening and hear an unfamiliar "
        "creak from the hallway. Your head turns toward the sound. Your heart gives one "
        "slightly harder thump, then settles. You listen for a second, decide it was the "
        "house settling, and go back to your book — but you notice you are reading the "
        "same paragraph twice, and your ears stay tuned to the hallway for a while. "
        "That is low fear: a ripple. It costs you almost nothing, and it bought you a "
        "moment of useful alertness. Snapshot two, high fear: you are driving at night in "
        "heavy rain when the car in front of you swerves violently and your headlights "
        "catch a dark shape sprawling across your lane. Your whole body slams into "
        "alert — hands crushing the wheel, breath stopped, stomach dropping like an "
        "elevator with cut cables. Thought vanishes; there is only brake, steer, brake. "
        "Afterwards your hands shake so hard you can barely hold the wheel, your legs "
        "feel like water, and you have to pull over and sit with your forehead on the "
        "wheel while your heart slowly remembers its normal rhythm. That is high fear: "
        "a wave that picks you up and puts you down somewhere else. Notice what the two "
        "snapshots share — the narrowed attention, the body mobilizing, the urge to act — "
        "and what differs: the volume, the duration, and how much of you the feeling "
        "gets to borrow. Low fear borrows your attention for a minute. High fear borrows "
        "your whole body for a while. Both give it back."
    ),
    "how_it_works": (
        "Both snapshots run the same machinery at different throttle settings. Low fear "
        "is a partial mobilization: enough arousal to sharpen the senses, not enough to "
        "hijack deliberate thought. High fear is full mobilization: the thinking mind is "
        "briefly demoted while fast survival circuits drive. The difference is the "
        "appraised stakes — a creak is ambiguous and probably harmless; a shape in the "
        "lane is immediate and possibly lethal. The body is an honest accountant: it "
        "spends arousal in proportion to the bill it expects."
    ),
    "key_points": [
        "Low fear is a ripple: brief alertness, tiny cost, quick return.",
        "High fear is a wave: full-body mobilization that borrows everything.",
        "Both share narrowed attention, body arousal, and an urge to act.",
        "The difference is throttle: appraisal of stakes sets the volume.",
        "Both give back what they borrow — the body always stands down.",
    ],
    "requirements": [
        "The three-volumes record as background",
        "Two of your own snapshots to compare",
    ],
    "standards": [
        "Arousal-performance curve (Yerkes and Dodson)",
        "Fight-or-flight graded response (Cannon)",
        "Appraisal theory (Lazarus)",
    ],
    "citations": [
        "Cannon, W. B. Bodily Changes in Pain, Hunger, Fear and Rage. Appleton; 1915.",
        "Yerkes, R. M., and Dodson, J. D. Journal of Comparative Neurology and Psychology; 1908.",
        "Ekman, P. Emotions Revealed. 2nd ed. Holt; 2007.",
    ],
    "sig_lens": (
        "Through the Signature lens, the two snapshots are the same instrument at two "
        "power settings — a lamp and a floodlight, one circuit. The Signature reader "
        "studies both, because the operator who only knows the floodlight will mistake "
        "every lamp for an emergency, and the one who only knows the lamp will be "
        "blinded by the floodlight. Both readings go in the log; both are honored."
    ),
},
{
    "key": "fear-anger-blend",
    "name": "Fear Mixed With Anger: The Fight-or-Flight Blend",
    "group": "How Fear Feels",
    "ladder_rank": 4,
    "ladder_tier": "foundations",
    "description": (
        "Fear rarely travels alone, and its most common traveling companion is anger. "
        "The blend of the two is the oldest argument in the body: run or fight. Picture "
        "being cornered by an aggressive dog on a narrow path. Part of you screams to "
        "back away slowly (fear), and part of you wants to shout, wave your arms, and "
        "drive it off (anger). That push-pull is the blend — two survival programs "
        "running at once, each sure it knows best. From the inside it feels hot and "
        "electric: the cold vigilance of fear plus the heat of anger, the urge to escape "
        "tangled with the urge to confront. People describe it as shaking with fury "
        "while wanting to cry, or feeling brave and terrified in the same breath. The "
        "blend is useful — anger lends fear its backbone, turning \"I must get away\" into "
        "\"I will not be moved\" — but it is volatile. Under the blend, judgment narrows "
        "twice over: fear says the threat is huge, anger says striking out will fix it, "
        "and neither is doing careful math. The way through is to name both ingredients "
        "out loud, even silently: \"I am afraid AND I am angry.\" Naming the blend loosens "
        "its grip, because each half was pretending to be the whole feeling. Once named, "
        "you can ask each half its question — fear asks \"what is the danger?\", anger asks "
        "\"what is unfair here?\" — and answer them one at a time instead of all at once."
    ),
    "how_it_works": (
        "Fear and anger share the same arousal fuel — adrenaline, pounding heart, tense "
        "muscles — but push behavior in opposite directions: away versus toward. When "
        "both appraisals fire at once (threat plus blocked goal or violation), the body "
        "gets both sets of marching orders. The result is the characteristic agitation of "
        "the blend: high energy with no single clear direction. Labeling the two "
        "components recruits the thinking mind, which can then sequence them — handle "
        "the danger first, address the unfairness second — instead of letting them shout "
        "over each other."
    ),
    "key_points": [
        "Fear plus anger is the run-or-fight argument happening inside one body.",
        "It feels hot and electric: escape urge tangled with confrontation urge.",
        "Anger lends fear backbone; fear lends anger caution.",
        "Under the blend, judgment narrows twice over — neither half does careful math.",
        "Naming both ingredients (\"afraid AND angry\") loosens the blend's grip.",
        "Sequence them: handle the danger first, the unfairness second.",
    ],
    "requirements": [
        "A memory of feeling furious and frightened at once",
        "The emotion-family record, for the blending idea",
    ],
    "standards": [
        "Wheel of emotions: dyads and blends (Plutchik)",
        "Fight-or-flight response (Cannon)",
        "Affect labeling and regulation research (Lieberman et al.)",
    ],
    "citations": [
        "Plutchik, R. Emotions and Life. APA; 2003.",
        "Cannon, W. B. Bodily Changes in Pain, Hunger, Fear and Rage. Appleton; 1915.",
        "Lieberman, M. D., et al. Putting feelings into words. Psychological Science; 2007.",
    ],
    "sig_lens": (
        "Through the Signature lens, the fear-anger blend is two instruments sounding at "
        "once — the warning bell and the battle horn. The Signature reader does not let "
        "them play over each other; he conducts. Fear is heard first (danger is "
        "immediate), anger is scheduled second (the wrong will be answered). In the "
        "Signature method, a blended signal is never answered with a blended reaction — "
        "each instrument gets its own measure."
    ),
},
{
    "key": "fear-day",
    "name": "A Day With Fear: Morning Alarm to Midnight",
    "group": "How Fear Feels",
    "ladder_rank": 5,
    "ladder_tier": "compounded",
    "description": (
        "Follow one ordinary day with fear as a quiet companion. Morning: the alarm, and "
        "a flutter in the stomach about the presentation at work — not terror, just the "
        "low hum of \"what if I freeze up there.\" You rehearse your opening line in the "
        "shower and the flutter eases; preparation is fear's favorite sedative. Midday: "
        "an email with the subject \"We need to talk\" from your manager. Your heart does "
        "the elevator drop before you even open it — and then it is about the office "
        "party. You laugh, shaky, at yourself. That is fear's favorite trick: it spends "
        "real alarm on imaginary threats, and the refund comes as relief. Afternoon: the "
        "presentation. Walking to the front of the room, your mouth goes dry, your hands "
        "are cold, your voice comes out half an octave higher than usual. Two minutes in, "
        "something steadies — the material takes over, the audience nods, and the fear "
        "drains out through your feet like water. Evening: driving home in the rain, a "
        "car drifts into your lane and you brake hard, horn blaring, heart hammering — "
        "ten seconds of pure animal alarm, then twenty minutes of shaky hands on the "
        "wheel. Midnight: lying in bed, the day replays. The presentation went fine. The "
        "email was nothing. The near-miss on the road was real. You notice something: "
        "fear visited four times today, at four volumes, for four reasons — and each "
        "time it was trying to help, in its blunt, loud, ancient way. You fall asleep "
        "mid-thought, and the companion, its shift over, finally goes quiet too."
    ),
    "how_it_works": (
        "A day shows fear's true job description: part-time guardian, full-time worrier. "
        "Most daily fear is anticipatory — rehearsals of threats that never arrive — mixed "
        "with a few genuine alarms. The anticipatory kind fades with preparation and "
        "familiarity; the genuine kind spikes and resolves with action. Tracking fear "
        "across a day reveals its pattern: it is frequent, mostly mild, often wrong, "
        "occasionally exactly right — and always temporary."
    ),
    "key_points": [
        "Most daily fear is anticipatory — rehearsals of threats that never arrive.",
        "Preparation is fear's favorite sedative.",
        "Fear spends real alarm on imaginary threats; relief is the refund.",
        "Genuine alarms spike hard and resolve with action.",
        "Across a day, fear is frequent, mostly mild, often wrong, always temporary.",
    ],
    "requirements": [
        "One of your own recent days to replay for fear visits",
        "A notebook — counting the visits makes the pattern visible",
    ],
    "standards": [
        "Appraisal theory: anticipated vs immediate threat (Lazarus)",
        "Basic-emotions framework (Ekman)",
        "Affect labeling research (Lieberman et al.)",
    ],
    "citations": [
        "Lazarus, R. S. Emotion and Adaptation. Oxford University Press; 1991.",
        "Ekman, P. Emotions Revealed. 2nd ed. Holt; 2007.",
        "Lieberman, M. D., et al. Putting feelings into words. Psychological Science; 2007.",
    ],
    "sig_lens": (
        "Through the Signature lens, a day with fear is a watch log: four entries, four "
        "volumes, four verdicts. The Signature reader logs each visit without shame — "
        "morning flutter, midday false alarm, afternoon performance surge, evening true "
        "alarm — and closes the day by reading the log back. The pattern is the lesson: "
        "the instrument sounds often, is wrong often, and is worth hearing always."
    ),
},
{
    "key": "fear-body",
    "name": "Fear in the Body: Heart, Breath, Muscles, Stomach, Skin",
    "group": "Body Signals",
    "ladder_rank": 5,
    "ladder_tier": "compounded",
    "description": (
        "Fear is one of the most physical of all emotions — you do not just think it, "
        "you wear it. Start with the heart: it pounds harder and faster, sometimes so "
        "hard you can hear it in your ears, because the body is rushing fuel to the "
        "muscles. Then the breath: it quickens and shallows, the chest doing fast "
        "sips of air instead of deep drinks, which can make you feel lightheaded if it "
        "goes on. The muscles tense all over — shoulders climb toward the ears, the jaw "
        "clenches, the hands grip or tremble — the body literally bracing for impact or "
        "coiling to run. The stomach joins in: the classic knot, the flutter, sometimes "
        "nausea, because digestion is a peacetime activity and the body has just "
        "declared an emergency — blood is routed away from the gut toward the big "
        "muscles. The skin tells the story too: going pale as surface blood pulls "
        "inward, or flushing; breaking into a cold sweat, especially on the forehead, "
        "upper lip, and palms; the hairs standing up on the arms and neck. The mouth "
        "goes dry, the pupils widen to take in more light and detail, and there may be "
        "a cold feeling at the back of the neck or a tingling in the hands and feet. "
        "Every one of these changes has the same purpose: to make you faster, stronger, "
        "and more alert for the next few minutes. The body is not betraying you — it is "
        "equipping you. And because the changes are so visible and feelable, the body is "
        "also fear's most honest reporter: long after the mind has talked itself calm, "
        "the trembling hands will tell you the alarm only just stood down."
    ),
    "how_it_works": (
        "The body changes are driven by the sympathetic nervous system and a surge of "
        "adrenaline. Heart rate and breathing rise to oxygenate blood; blood vessels in "
        "the skin constrict while those in large muscles dilate; sweat glands activate "
        "to cool the anticipated effort; digestion and saliva slow because they can "
        "wait. Pupil dilation is the visual system opening its aperture. Trembling is "
        "muscles primed and idling at high revs. It is a coordinated, whole-body "
        "retooling for emergency action — expensive, effective, and designed to switch "
        "off when the emergency ends."
    ),
    "key_points": [
        "Heart pounds, breath quickens and shallows — fuel rushed to muscles.",
        "Muscles tense and may tremble — the body bracing or coiling.",
        "Stomach knots or nauseates — digestion pauses during emergencies.",
        "Skin pales or flushes, cold sweat, hairs rise — all visible signals.",
        "Mouth dries, pupils widen, neck goes cold — the senses open up.",
        "Every change equips you; the body is fear's most honest reporter.",
    ],
    "requirements": [
        "Willingness to scan your own body while reading",
        "A recent scare to replay signal by signal",
    ],
    "standards": [
        "Fight-or-flight physiology (Cannon, 1915)",
        "Sympathetic arousal and adrenaline effects",
        "James-Lange perspective: body states shape felt emotion (James, 1884)",
    ],
    "citations": [
        "Cannon, W. B. Bodily Changes in Pain, Hunger, Fear and Rage. Appleton; 1915.",
        "James, W. What is an emotion? Mind; 1884.",
        "LeDoux, J. The Emotional Brain. Simon & Schuster; 1996.",
    ],
    "sig_lens": (
        "Through the Signature lens, the fearful body is an instrument panel lighting up "
        "in sequence — heart gauge, breath gauge, muscle gauge, skin gauge — each lamp "
        "with a known meaning. The Signature reader learns the panel the way a pilot "
        "learns a cockpit: not to fear the lights, but to fly by them. When the lamps "
        "burn, the operator knows the machine is arming itself, and he takes the "
        "controls with steady hands."
    ),
},
{
    "key": "fear-posture",
    "name": "The Posture of Fear: How the Body Carries It",
    "group": "Body Signals",
    "ladder_rank": 5,
    "ladder_tier": "compounded",
    "description": (
        "Fear has a silhouette — you can often spot it across a room before a word is "
        "spoken. The frightened body makes itself smaller: shoulders hunch forward and "
        "in, the head ducks slightly, the chest caves as if shielding the vital organs. "
        "Arms pull in close, sometimes crossing the torso or rising to guard the face "
        "and neck. The stance narrows — feet draw together or one foot angles toward "
        "the exit, weight shifting onto the balls of the feet, ready. Movement changes "
        "too, in one of two directions: freezing, where the person goes suddenly, "
        "utterly still, like a deer deciding whether it has been seen; or agitation, "
        "where the person fidgets, paces, wrings hands, touches the face repeatedly — "
        "the body's engine revving with nowhere to go. The walk of a frightened person "
        "is telling: quick, light steps, head swiveling, hugging the walls, taking the "
        "long way around anything uncertain. Even sitting fear shows: perched on the "
        "edge of the chair, leaning away, feet tucked back or pointed at the door. None "
        "of this is performed — it is the body's old choreography, written long before "
        "language, and it leaks out whether the person wants it to or not. Learning to "
        "read the silhouette helps in two directions: you can spot fear in others "
        "sooner and respond kindly, and you can notice your own body shrinking and "
        "choose, deliberately, to uncurl — because posture is a two-way street, and "
        "standing taller can send a calming memo back to the alarm."
    ),
    "how_it_works": (
        "Fear posture is protective geometry: minimize the target, shield the vitals, "
        "prepare the legs. Freezing is the oldest move — stillness avoids detection — "
        "while agitation is mobilization energy leaking through small movements. The "
        "two-way street works because the brain reads the body's posture as data: an "
        "open, grounded stance feeds back a mild \"all clear\" that can soften the alarm, "
        "while a collapsed stance confirms the danger. Posture is both signal and "
        "lever."
    ),
    "key_points": [
        "The frightened body makes itself smaller: hunched, guarded, narrowed.",
        "Feet angle toward exits; weight shifts ready to move.",
        "Freezing (utter stillness) or agitation (fidgeting, pacing) — two movement modes.",
        "The fear walk: quick light steps, head swiveling, hugging walls.",
        "Posture is a two-way street: uncurling sends a calming memo to the alarm.",
        "Reading the silhouette lets you respond kindly and sooner.",
    ],
    "requirements": [
        "A mirror or a memory — check your own fear silhouette",
        "Room to stand, uncurl, and feel the difference",
    ],
    "standards": [
        "Ethological protective postures (Darwin, 1872)",
        "Freeze response in threat circuitry (LeDoux)",
        "Embodied feedback: posture influences felt emotion",
    ],
    "citations": [
        "Darwin, C. The Expression of the Emotions in Man and Animals. John Murray; 1872.",
        "LeDoux, J. The Emotional Brain. Simon & Schuster; 1996.",
        "Ekman, P. Emotions Revealed. 2nd ed. Holt; 2007.",
    ],
    "sig_lens": (
        "Through the Signature lens, fear posture is the body writing its report in "
        "geometry — the shrinking circle, the guarded line, the foot pointed at the "
        "door. The Signature reader studies this script until he can read it at a "
        "glance, and he learns the counter-script too: the deliberate uncurling, the "
        "planted feet, the opened chest. In the Signature method, posture is a lever "
        "the operator is allowed to pull."
    ),
},
{
    "key": "fear-sleep",
    "name": "Fear, Sleep, Appetite, and Energy",
    "group": "Body Signals",
    "ladder_rank": 6,
    "ladder_tier": "compounded",
    "description": (
        "Fear does not clock out when the scare ends — it follows you to the table and "
        "to bed. Appetite is usually the first to go: the knotted stomach of fear has no "
        "interest in food, and a frightening day can leave you pushing dinner around the "
        "plate. This is the body being consistent — digestion was paused for the "
        "emergency, and it takes a while to reopen the kitchen. Some people feel the "
        "opposite later, a gnawing hunger once the alarm finally stands down, the body "
        "sending up a resupply order. Sleep is fear's favorite battleground. A mind that "
        "spent the day on alert does not power down on command: you lie awake replaying "
        "the scare, or imagining tomorrow's, while the body stays half-mobilized — "
        "tense shoulders, shallow breath — in a bed that should mean rest. Falling "
        "asleep gets harder, sleep gets lighter, and vivid, chase-flavored dreams may "
        "fill the night as the brain files the day's alarms. Energy runs a strange "
        "double pattern: during fear you may feel wired, buzzing, unable to sit still — "
        "and afterwards comes the crash, a heavy, wrung-out tiredness that no single "
        "nap quite fixes, because the body spent its reserves at emergency rates. The "
        "practical takeaway is gentle and unglamorous: on fear-heavy days, eat simply "
        "and regularly even without appetite, wind down the evening deliberately, and "
        "expect the tiredness without judging it. The system is not broken; it is "
        "refueling after a fire drill."
    ),
    "how_it_works": (
        "Appetite, sleep, and energy all answer to the same arousal system that drives "
        "fear. High arousal suppresses digestion, delays sleep onset, and spends energy "
        "at emergency rates; the rebound is hunger, lighter sleep, and fatigue. The "
        "brain's threat filing — replaying and rehearsing — keeps arousal simmering "
        "after the event, which is why the effects outlast the scare by hours. Regular "
        "meals, wind-down routines, and daylight movement give the system the raw "
        "materials and the off-ramps it needs to settle."
    ),
    "key_points": [
        "Fear usually steals appetite first — digestion pauses for emergencies.",
        "A wired mind resists sleep; the body stays half-mobilized in bed.",
        "Vivid chase-flavored dreams are the brain filing the day's alarms.",
        "Energy spikes wired, then crashes heavy — emergency spending, then refuel.",
        "Eat simply and regularly, wind down deliberately, expect the tiredness.",
        "The system is refueling after a fire drill, not broken.",
    ],
    "requirements": [
        "One fear-heavy day to review: meals, sleep, energy",
        "No late-night scare media while testing the wind-down advice",
    ],
    "standards": [
        "Stress-response phases: alarm, resistance, recovery (Selye, 1956)",
        "Sympathetic effects on digestion and sleep",
        "Sleep and emotional memory processing",
    ],
    "citations": [
        "Selye, H. The Stress of Life. McGraw-Hill; 1956.",
        "Cannon, W. B. Bodily Changes in Pain, Hunger, Fear and Rage. Appleton; 1915.",
        "Walker, M. Why We Sleep. Scribner; 2017.",
    ],
    "sig_lens": (
        "Through the Signature lens, the body after fear is a machine coming off a full "
        "power run — hot, hungry for fuel, needing its cool-down lap. The Signature "
        "reader does not scold the machine for being tired; he services it. Simple "
        "food, deliberate wind-down, honest rest: this is maintenance, not indulgence, "
        "and the Signature method logs it as part of the operation, not apart from it."
    ),
},
{
    "key": "fear-differences",
    "name": "No Two Bodies Fear Alike",
    "group": "Body Signals",
    "ladder_rank": 6,
    "ladder_tier": "compounded",
    "description": (
        "Here is something the movies get wrong: there is no single, standard-issue fear "
        "response. One person goes pale and silent; another flushes and talks a mile a "
        "minute. One freezes like a statue; another cannot stop moving. One loses all "
        "appetite; another wants to eat everything in sight once it is over. These "
        "differences are normal, and they come from several honest sources. Temperament "
        "plays a part — some nervous systems are simply more reactive, the way some car "
        "alarms trigger in a strong wind. History plays a bigger part: a body that has "
        "lived through real danger learns its own shortcuts, so a slammed door means "
        "nothing to one person and everything to another. Training matters too — people "
        "who have practiced staying functional under pressure (responders, performers, "
        "athletes) often show a calmer surface over the same inner arousal. Even the "
        "moment matters: exhaustion, hunger, illness, and caffeine all turn the alarm's "
        "volume knob. And culture writes the display rules — what a person lets show on "
        "the outside varies enormously, even when the inside is ringing. The lesson is "
        "twofold and kind: do not judge your fear by someone else's (your quiet "
        "freeze is not lesser than their loud panic, nor greater), and do not assume "
        "you know what someone else is feeling from the outside. Ask, watch, and "
        "believe the answer. The only standard fear response is that there isn't one."
    ),
    "how_it_works": (
        "Individual differences in fear come from the whole stack: genetics of "
        "reactivity, learned associations from personal history, current physiological "
        "state, and cultural display rules that govern expression. The threat circuitry "
        "is universal — every human has it — but its gain setting, its triggers, and "
        "its visible output are all tuned by a life. That is why two people can walk "
        "through the same haunted house and one laughs while the other shakes: same "
        "machinery, different calibration."
    ),
    "key_points": [
        "There is no standard-issue fear response — variation is the norm.",
        "Temperament, history, training, and current state all tune the alarm.",
        "Culture writes the display rules for what shows on the outside.",
        "Do not judge your fear by someone else's response.",
        "Do not assume you know another's feeling from the outside — ask and watch.",
        "Same machinery, different calibration.",
    ],
    "requirements": [
        "Two people you know well whose fear styles differ",
        "Curiosity instead of comparison",
    ],
    "standards": [
        "Individual differences in threat reactivity",
        "Display rules across cultures (Ekman and Friesen)",
        "Learned fear and conditioning histories",
    ],
    "citations": [
        "Ekman, P., and Friesen, W. V. Constants across cultures in the face and emotion. Journal of Personality and Social Psychology; 1971.",
        "LeDoux, J. The Emotional Brain. Simon & Schuster; 1996.",
        "Kagan, J. Galen's Prophecy. Basic Books; 1997.",
    ],
    "sig_lens": (
        "Through the Signature lens, every operator's instrument panel is calibrated "
        "differently, and the Signature method forbids comparing gauges across "
        "machines. Your panel is yours: its sensitivity, its history, its display "
        "rules. The Signature reader learns his own calibration the way a musician "
        "learns his own instrument — intimately, without apology, and without "
        "borrowing anyone else's tuning."
    ),
},
{
    "key": "fear-face",
    "name": "The Face of Fear: Eyes, Brows, Mouth, Micro-Signs",
    "group": "Facial Expression",
    "ladder_rank": 6,
    "ladder_tier": "compounded",
    "description": (
        "Of all emotions, fear may have the most readable face — it is written to be "
        "seen, because a visible alarm warns the whole group. Start at the top: the "
        "eyebrows rise high and pull together, creating horizontal wrinkles across the "
        "forehead and a worried slant. Below them, the upper eyelids lift — the eyes go "
        "wide, showing white all around the iris — while the lower lids tense and draw "
        "up slightly. Wide eyes are not decoration: they literally widen the visual "
        "field, letting in more of the scene to find the threat. The mouth is the other "
        "half of the signature: the lips stretch horizontally, pulled back and "
        "flattened, and the jaw may drop open, as if the face is preparing to gasp or "
        "cry out. Put it together and you get the classic mask — raised inner brows, "
        "staring eyes, stretched mouth — recognizable in every culture researchers have "
        "studied. Then come the micro-signs, the small print of fear: a quick nostril "
        "flare as breathing quickens; a brief tightening at the corners of the mouth; "
        "the chin pulling back; rapid blinking; a sheen of sweat on the upper lip and "
        "forehead. These flashes last fractions of a second and the person often does "
        "not know they happened. The face of fear is honest because it is fast — the "
        "muscles involved answer the alarm before the thinking mind can edit them. "
        "That is why, when words say \"I'm fine\" but the brows are up and the eyes are "
        "wide, the face is usually telling the truth."
    ),
    "how_it_works": (
        "The fear face is driven by the same rapid threat pathway that mobilizes the "
        "body. Brow raising and eyelid lifting are served by muscles that widen sensory "
        "intake — bigger visual field, more information. Lip stretching and jaw dropping "
        "prepare the airway and the vocal apparatus for gasping or screaming. Because "
        "these commands travel a fast subcortical route, they appear in about a fifth "
        "of a second — before voluntary control can intervene — which is why micro "
        "expressions of fear leak even when someone is trying to look calm."
    ),
    "key_points": [
        "Brows rise high and pull together; forehead wrinkles horizontally.",
        "Upper lids lift — wide eyes showing white; lower lids tense.",
        "Lips stretch horizontally; jaw may drop open.",
        "The pattern is recognized across cultures — a universal alarm face.",
        "Micro-signs: nostril flare, lip-corner tightening, rapid blinking, sweat sheen.",
        "The face is honest because it is fast — muscles answer before editing.",
    ],
    "requirements": [
        "A mirror — try the brow raise and feel which muscles move",
        "Attention to faces in films: spot the pattern",
    ],
    "standards": [
        "Universality of the fear expression (Ekman and Friesen, 1971)",
        "Facial Action Coding System: brow, lid, and mouth actions (Ekman and Friesen)",
        "Expression as sensory preparation",
    ],
    "citations": [
        "Ekman, P., and Friesen, W. V. Constants across cultures in the face and emotion. Journal of Personality and Social Psychology; 1971.",
        "Ekman, P., and Friesen, W. V. Facial Action Coding System. Consulting Psychologists Press; 1978.",
        "Darwin, C. The Expression of the Emotions in Man and Animals. John Murray; 1872.",
    ],
    "sig_lens": (
        "Through the Signature lens, the fear face is the alarm's public notice — posted "
        "on the front of the building for all to read. The Signature reader studies the "
        "notice the way a watchman studies signal flags: brow flags raised, eye "
        "shutters wide, mouth line stretched. He learns to read it on others in a "
        "glance, and to recognize it in his own mirror without flinching."
    ),
},
{
    "key": "fear-face-intensity",
    "name": "Fear on the Face at Different Intensities",
    "group": "Facial Expression",
    "ladder_rank": 7,
    "ladder_tier": "compounded",
    "description": (
        "The fear face is not on-or-off — it dims and brightens with the feeling. At "
        "low intensity, the signs are whispers: the inner corners of the brows lift "
        "just a fraction, the upper lids rise a millimeter, the lips press or tighten "
        "slightly at the corners. Most people would call this \"looking concerned\" rather "
        "than \"looking afraid,\" and that is exactly right — mild fear wears the face of "
        "concern. At medium intensity, the whispers become sentences: brows clearly "
        "raised and drawn together, eyes visibly widened, mouth stretched into the "
        "horizontal line. Nobody mistakes this for calm. At high intensity, the face "
        "goes full mask — every muscle in the pattern firing at once — and may add the "
        "extras: jaw dropped, nostrils flared, the whole face seeming to pull back from "
        "the threat. There is also a telling after-pattern: as fear fades, the face "
        "does not snap back like a rubber band. The brows lower in stages, the mouth "
        "softens unevenly, and a shaky half-smile often appears — relief wearing a "
        "borrowed expression. Watch for the mismatch that matters most: a calm mouth "
        "with frightened eyes. The mouth is the easiest part to control, the eyes the "
        "hardest — so when they disagree, trust the eyes. Reading intensity on the face "
        "is a practical skill: it tells you whether someone needs a steadying word, a "
        "real intervention, or simply to be left to ride out a ripple."
    ),
    "how_it_works": (
        "Facial intensity tracks arousal level: more alarm, more muscle recruitment, in "
        "a graded way. The upper face (brows, lids) is driven by the fast threat "
        "pathway and is hardest to fake or suppress; the lower face (mouth) is under "
        "stronger voluntary control and is easiest to edit. Recovery is gradual because "
        "arousal decays in waves, and the relief smile is a separate positive signal "
        "overlapping the fading fear — two expressions sharing the face for a moment."
    ),
    "key_points": [
        "Low fear whispers: slight brow lift, millimeter lid raise, lip tightening.",
        "Medium fear speaks: clear brow raise, widened eyes, stretched mouth.",
        "High fear shouts: full mask plus jaw drop and nostril flare.",
        "Recovery is gradual; a shaky relief smile often overlaps the fading fear.",
        "Calm mouth plus frightened eyes: trust the eyes — they are hardest to edit.",
        "Reading intensity guides the response: steadying word, intervention, or space.",
    ],
    "requirements": [
        "The basic fear-face record as background",
        "Practice grading faces in photos or film stills",
    ],
    "standards": [
        "Graded facial expression with arousal (Ekman)",
        "Upper-face vs lower-face controllability",
        "Facial Action Coding System intensity scoring",
    ],
    "citations": [
        "Ekman, P., and Friesen, W. V. Facial Action Coding System. Consulting Psychologists Press; 1978.",
        "Ekman, P. Emotions Revealed. 2nd ed. Holt; 2007.",
        "Darwin, C. The Expression of the Emotions in Man and Animals. John Murray; 1872.",
    ],
    "sig_lens": (
        "Through the Signature lens, the face is a dimmer switch, not a toggle — and "
        "the Signature reader learns every setting. Whisper, sentence, shout: each "
        "brightness calls for a different answer, and answering a whisper with a "
        "shout's response is its own kind of error. The Signature method grades the "
        "signal before spending the response."
    ),
},
{
    "key": "fear-hidden",
    "name": "Hiding and Faking Fear: What Leaks Through",
    "group": "Facial Expression",
    "ladder_rank": 7,
    "ladder_tier": "compounded",
    "description": (
        "People hide fear all the time — the job interview, the first date, the "
        "turbulent flight where nobody wants to be the panicking passenger. Hiding "
        "usually means neutralizing: pressing the face toward blank, relaxing the "
        "brows by force, keeping the mouth still. Some people mask instead, laying a "
        "different expression over the top — most often a smile, the social all-purpose "
        "cover. Here is what the hiders cannot fully stop: the upper face. The brow "
        "raise and eyelid lift of fear are driven by the fast alarm pathway, and "
        "voluntary control reaches them late and weakly. So the classic leak is the "
        "brow flash — a quarter-second lift of the inner brows — over an otherwise "
        "careful face. Other leaks: the eyes stay a fraction too wide; blinking speeds "
        "up; the lips press together (effort) or tremble slightly at the corners; the "
        "voice, which the face cannot guard, climbs in pitch. Faking fear — acting it "
        "for a camera or a story — has the opposite problem: the performer can arrange "
        "the mouth and even widen the eyes, but the brow-lid coordination is hard to "
        "summon on demand, which is why acted fear often looks like surprise wearing a "
        "costume. The ethical note matters: noticing leaks is a tool for kindness — "
        "spotting that a smiling friend is frightened so you can quietly help — not for "
        "exposure or advantage. Read faces to care for people, not to catch them."
    ),
    "how_it_works": (
        "Suppression works top-down: the thinking mind sends \"stay neutral\" commands to "
        "facial muscles. It succeeds best on the lower face, which has rich voluntary "
        "innervation, and worst on the upper face, where the fast threat pathway "
        "dominates. The result is asymmetry — controlled mouth, honest eyes — and brief "
        "micro-expressions when the alarm pulse outruns the suppression command. Masking "
        "with a smile adds a second voluntary pattern on top, but the underlying "
        "alarm pattern still fires underneath, producing the blended, slightly \"off\" "
        "look of a fearful smile."
    ),
    "key_points": [
        "Hiding fear usually means neutralizing the face or masking with a smile.",
        "The upper face (brows, lids) is hardest to control — it leaks first.",
        "Classic leak: the quarter-second brow flash over a careful face.",
        "The voice leaks too — pitch climbs where the face is guarded.",
        "Faked fear often looks like surprise in costume — brow-lid coordination is hard to summon.",
        "Read leaks for kindness: to help quietly, never to expose.",
    ],
    "requirements": [
        "The fear-face and intensity records as background",
        "A commitment to use this only kindly",
    ],
    "standards": [
        "Display rules and expression management (Ekman and Friesen)",
        "Micro-expressions and leakage",
        "Voluntary vs involuntary facial control",
    ],
    "citations": [
        "Ekman, P., and Friesen, W. V. Nonverbal leakage and clues to deception. Psychiatry; 1969.",
        "Ekman, P. Telling Lies. Norton; 2009.",
        "Ekman, P. Emotions Revealed. 2nd ed. Holt; 2007.",
    ],
    "sig_lens": (
        "Through the Signature lens, a hidden fear is a sealed letter with the wax "
        "cracked — the brow flash, the wide eye, the climbing voice. The Signature "
        "reader is trained to notice the crack, and trained harder in what to do with "
        "it: nothing public, everything kind. In the Signature method, a noticed leak "
        "is a private summons to gentleness, never a weapon."
    ),
},
{
    "key": "fear-artist",
    "name": "Drawing Fear: Notes for Artists and Actors",
    "group": "Facial Expression",
    "ladder_rank": 7,
    "ladder_tier": "compounded",
    "description": (
        "For the artist with a pencil or the actor with a mirror, here is fear "
        "translated into craft. The brows: draw them raised high, but not in a smooth "
        "arc — the inner corners lift and pull together, making a worried, almost "
        "triangular shape, with short horizontal creases across the forehead. The eyes: "
        "open them wider than neutral — show a thin rim of white above and below the "
        "iris — and tense the lower lid so it rides up a touch; the gaze is fixed, "
        "locked on the threat, not wandering. The mouth: stretch it horizontally, the "
        "lips pulled back and thinned, corners drawn straight back rather than up or "
        "down; at higher intensity, drop the jaw so the mouth opens into a tense oval. "
        "The nose: flare the nostrils slightly, as if mid-quick-breath. The whole head: "
        "pull it back a fraction, chin tucking, as though the face itself is trying to "
        "retreat. For the actor, add the body: shallow fast breath you can hear, hands "
        "that do not know where to go, a voice pitched half a step higher and slightly "
        "rushed. The most common mistake is playing surprise instead — wide eyes with "
        "smooth, high, arched brows and a round open mouth. Fear's brows are raised AND "
        "knitted; surprise's are raised and smooth. That knitted tension is the whole "
        "difference: surprise says \"what?!\" — fear says \"oh no.\" Get the brows right "
        "and the audience will feel it in their own stomachs before a word is spoken."
    ),
    "how_it_works": (
        "Artistic depiction works by isolating the diagnostic features — the ones "
        "viewers' threat detectors actually use. Research on expression recognition "
        "shows the brow-lid-mouth triangle carries the fear signal; exaggerating those "
        "features slightly (caricature) makes the emotion read faster and stronger. "
        "The surprise-versus-fear distinction lives almost entirely in the brows — "
        "smooth-raised versus raised-and-knitted — which is why that single detail "
        "decides whether the audience gasps or merely blinks."
    ),
    "key_points": [
        "Brows: raised high AND knitted — worried triangle, forehead creases.",
        "Eyes: wider than neutral, white showing, lower lid tense, gaze fixed.",
        "Mouth: stretched horizontally, lips thinned; jaw drops at high intensity.",
        "Head pulls back slightly, chin tucks — the face retreating.",
        "Actor's extras: audible shallow breath, restless hands, higher rushed voice.",
        "Fear vs surprise: the knitted brow is the whole difference.",
    ],
    "requirements": [
        "A pencil or a mirror — this record is meant to be tried",
        "The fear-face record as the anatomy reference",
    ],
    "standards": [
        "Facial Action Coding System feature isolation",
        "Expression recognition: diagnostic features",
        "Caricature and exaggeration in expression art",
    ],
    "citations": [
        "Ekman, P., and Friesen, W. V. Facial Action Coding System. Consulting Psychologists Press; 1978.",
        "Darwin, C. The Expression of the Emotions in Man and Animals. John Murray; 1872.",
        "Ekman, P. Emotions Revealed. 2nd ed. Holt; 2007.",
    ],
    "sig_lens": (
        "Through the Signature lens, the artist and actor are signal engineers — they "
        "rebuild the alarm face from its true parts so others can recognize it. The "
        "Signature method honors this craft: to draw fear honestly is to teach a "
        "thousand viewers to read it kindly. Every true line in the sketch is a small "
        "act of public instruction."
    ),
},
{
    "key": "fear-triggers",
    "name": "Classic Fear Triggers",
    "group": "Triggers",
    "ladder_rank": 7,
    "ladder_tier": "compounded",
    "description": (
        "Certain triggers set off human fear the way certain keys fit certain locks — "
        "they are classic because they worked on our ancestors. Sudden, loud sounds top "
        "the list: a bang, a scream, a crash with no warning. The startle they produce "
        "is the fastest fear there is. Next come looming things — objects rushing "
        "toward the face, shadows swelling on a wall — the visual system treats rapid "
        "approach as danger until proven otherwise. Heights trigger the ancient worry "
        "about falling; darkness triggers the worry about what cannot be seen; deep "
        "water, spiders, snakes, and large staring animals all appear on the classic "
        "roster across cultures. Strangers — especially in groups, at night, behaving "
        "unpredictably — trigger social fear, the old arithmetic of \"unknown intentions "
        "plus my vulnerability.\" Then there are the situational classics: being trapped "
        "with no exit, being lost, being watched, sudden pain, the sight of blood, "
        "losing control of a vehicle, turbulent flights. Words can be triggers too: "
        "\"we need to talk,\" a doctor's grave tone, a siren's particular wail. What makes "
        "them classic is not that they always mean danger — most bangs are harmless — "
        "but that the cost of missing a real one was historically so high that the "
        "alarm evolved to err on the side of ringing. False alarms are the price of a "
        "sensitive smoke detector. Knowing the classic list does two things: it "
        "normalizes your reactions (\"of course that startled me — it startles everyone\") "
        "and it speeds up the check (\"loud bang, no smoke, no screams — false alarm\")."
    ),
    "how_it_works": (
        "Classic triggers work through prepared pathways: the brain is biased to learn "
        "fear quickly for certain stimulus classes (sudden sounds, looming, heights, "
        "certain animals) because those classes were historically dangerous. The "
        "pathway is fast and crude — it reacts to the rough shape of danger before the "
        "details arrive. That is why a coiled garden hose can make you jump: the "
        "pattern-matcher fires on \"long thin curved shape\" before the thinking mind "
        "reports \"hose.\" Each false alarm is the system choosing the cheaper error."
    ),
    "key_points": [
        "Sudden loud sounds are the fastest classic trigger.",
        "Looming objects, heights, darkness, deep water are visual/spatial classics.",
        "Strangers and entrapment trigger the old vulnerability arithmetic.",
        "Words and tones (\"we need to talk\") can be triggers too.",
        "The alarm errs toward ringing — false alarms are the price of sensitivity.",
        "Knowing the list normalizes reactions and speeds up the false-alarm check.",
    ],
    "requirements": [
        "Your own top three classic triggers, named honestly",
        "One recent false alarm to re-examine kindly",
    ],
    "standards": [
        "Preparedness in fear learning",
        "Startle reflex and sudden-onset stimuli",
        "Fast crude threat pattern-matching (LeDoux)",
    ],
    "citations": [
        "LeDoux, J. The Emotional Brain. Simon & Schuster; 1996.",
        "Darwin, C. The Expression of the Emotions in Man and Animals. John Murray; 1872.",
        "Ekman, P. Emotions Revealed. 2nd ed. Holt; 2007.",
    ],
    "sig_lens": (
        "Through the Signature lens, classic triggers are the standard test tones of "
        "the alarm system — the tones every unit is built to hear. The Signature "
        "reader memorizes them the way a sailor memorizes the standard fog signals: "
        "not to fear the horn, but to know instantly which horn is sounding. Standard "
        "tones get standard checks, run calmly and fast."
    ),
},
{
    "key": "fear-personal-triggers",
    "name": "Personal Fear Triggers: Memories and Associations",
    "group": "Triggers",
    "ladder_rank": 8,
    "ladder_tier": "compounded",
    "description": (
        "Beyond the classics, everyone carries a private trigger list — written by "
        "their own life. A particular song that was playing during bad news. The smell "
        "of a hospital corridor. A date on the calendar. The specific intersection "
        "where the accident happened. A breed of dog, a tone of voice, a phrase a "
        "parent used before punishment. These triggers are not universal; they are "
        "autobiographical. They form the way all learning forms: something frightening "
        "happened once (or many times) alongside something neutral, and the alarm "
        "wired them together. After that, the neutral thing alone can ring the bell. "
        "Personal triggers are powerful precisely because they are personal — the "
        "reaction can look outsized to everyone else (\"it is just a song\") while "
        "feeling completely proportional on the inside, because the inside is hearing "
        "the whole memory, not just the song. Two things help. First, mapping them: "
        "writing down your private triggers takes them out of the shadows where they "
        "ambush you and puts them on paper where you can see them coming. Second, "
        "updating them: each time the trigger fires and nothing bad happens, the alarm "
        "gets one small vote toward standing down — especially if you stay, breathe, "
        "and let the moment pass safely. The wiring was learned, which means it can be "
        "re-learned. Be patient with other people's private triggers, and with your "
        "own: nobody chose their list, but everyone can revise it."
    ),
    "how_it_works": (
        "Personal triggers form by association: the threat system links the frightening "
        "event to its surrounding cues — sounds, smells, places, dates — and stores the "
        "bundle. Later, any strong cue from the bundle can reactivate the whole "
        "pattern, which is why the reaction feels bigger than the current situation "
        "warrants: you are responding to the memory plus the moment. Re-learning works "
        "by the same machinery in reverse — safe repetitions with the cue and without "
        "the harm gradually write a new association over the old one."
    ),
    "key_points": [
        "Personal triggers are autobiographical — written by your own life.",
        "They form by association: neutral cues wired to frightening events.",
        "Reactions can look outsized outside and feel proportional inside.",
        "Mapping them (writing them down) moves them from ambush to visibility.",
        "Safe repetitions let the alarm stand down — wiring can be re-learned.",
        "Be patient with others' lists and your own — nobody chose them.",
    ],
    "requirements": [
        "Privacy — this mapping is for your eyes",
        "Paper and pen for the trigger map",
        "Gentleness: no forcing yourself toward strong triggers",
    ],
    "standards": [
        "Associative fear learning",
        "Extinction through safe repetition",
        "Autobiographical memory and emotion",
    ],
    "citations": [
        "LeDoux, J. The Emotional Brain. Simon & Schuster; 1996.",
        "Pavlov, I. P. Conditioned Reflexes. Oxford University Press; 1927.",
        "Ekman, P. Emotions Revealed. 2nd ed. Holt; 2007.",
    ],
    "sig_lens": (
        "Through the Signature lens, personal triggers are entries in a private logbook "
        "— each one dated by experience, each one revisable by the author. The "
        "Signature reader treats his logbook as a living document: old entries are "
        "respected for what they taught, and updated when new evidence arrives. No "
        "entry is permanent unless the reader signs it so."
    ),
},
{
    "key": "fear-surprise-triggers",
    "name": "Surprise Triggers: The Odd and Unexpected",
    "group": "Triggers",
    "ladder_rank": 8,
    "ladder_tier": "compounded",
    "description": (
        "Then there are the triggers that make no sense at all — until they do. A "
        "balloon popping at a party. A phone buzzing in a silent room. A mannequin in "
        "a store caught from the corner of the eye. Your own reflection in a dark "
        "window. A moth landing on your neck. A child's toy that suddenly talks. "
        "Nobody is philosophically afraid of balloons or moths; the fear comes from "
        "the startle machinery, which does not do philosophy. It does speed: anything "
        "sudden, anything that breaks the expected pattern, gets flagged first and "
        "understood second. Surprise triggers also include the mismatch kind — the "
        "elevator that stops between floors, the step that isn't there, the familiar "
        "street that looks wrong in fog. The brain runs a constant prediction of the "
        "world, and a sharp prediction error reads as possible danger until the "
        "update arrives. There is a third odd category: triggers that borrow fear from "
        "somewhere else — being jumpy after a bad day, so the toast popping up feels "
        "like an attack. The background arousal was already high; the trivial trigger "
        "just spent it. The kindest response to surprise triggers is laughter, when it "
        "comes naturally — the body's own all-clear signal. And the practical one is "
        "context: noticing that you startle easily when tired, hungry, or already "
        "on edge turns a mysterious overreaction into an understandable one."
    ),
    "how_it_works": (
        "Surprise triggers fire the startle reflex — a brainstem-level response to "
        "sudden intense stimuli — which then recruits the fear system if arousal is "
        "high or the stimulus remains unexplained. Prediction-error triggers work "
        "through the brain's world-model: a sharp mismatch between expected and "
        "actual input is treated as potential threat until resolved. Borrowed-fear "
        "triggers are simple arithmetic: high background arousal plus a small trigger "
        "equals a big response. In all three cases, the explanation arrives after the "
        "reaction — the machinery is built that way."
    ),
    "key_points": [
        "Sudden pattern-breaks (pops, buzzes, reflections) fire the startle machinery.",
        "The startle system does speed, not philosophy — understanding comes second.",
        "Prediction errors (missing step, wrong-looking street) read as possible danger.",
        "High background arousal makes trivial triggers produce big responses.",
        "Natural laughter after a false startle is the body's all-clear signal.",
        "Tired, hungry, or on-edge states explain most \"overreactions.\"",
    ],
    "requirements": [
        "A funny surprise-trigger story of your own",
        "Noticing your background state when you startle easily",
    ],
    "standards": [
        "Startle reflex physiology",
        "Prediction-error processing",
        "Arousal summation",
    ],
    "citations": [
        "LeDoux, J. The Emotional Brain. Simon & Schuster; 1996.",
        "Ekman, P. Emotions Revealed. 2nd ed. Holt; 2007.",
        "Cannon, W. B. Bodily Changes in Pain, Hunger, Fear and Rage. Appleton; 1915.",
    ],
    "sig_lens": (
        "Through the Signature lens, surprise triggers are the alarm's hair-trigger "
        "setting — firing at shadows and echoes. The Signature reader does not "
        "apologize for the hair trigger; he calibrates it. Rest, food, and context "
        "are the calibration tools, and laughter after a false alarm is logged as a "
        "successful test, not an embarrassment."
    ),
},
{
    "key": "fear-cascade",
    "name": "Fear Chain Reactions: From One Trigger to Many",
    "group": "Triggers",
    "ladder_rank": 8,
    "ladder_tier": "compounded",
    "description": (
        "Fear is a chain reaction looking for a reason to continue. It starts with one "
        "trigger — a strange noise at night — and if the mind cannot resolve it, the "
        "chain begins. Link one: the noise. Link two: the memory it drags up (the "
        "break-in story on the news). Link three: the imagined futures (what if someone "
        "is downstairs?). Link four: the body, now fully mobilized, reporting back its "
        "own arousal as further evidence (my heart is pounding — this must be serious). "
        "Link five: every small sound in the house gets promoted to suspect. Within "
        "minutes, one unexplained creak has become a whole case file. The cruelty of "
        "the cascade is that each link feels like confirmation: the pounding heart "
        "seems to prove the danger, when it was actually caused by the earlier links. "
        "It is a loop, not a ladder — arousal feeds imagination, imagination feeds "
        "arousal. Breaking the chain means breaking any single link with authority. "
        "Check the noise (information breaks link one). Name the memory (labeling "
        "breaks link two). Ask \"what do I actually know?\" (evidence breaks link "
        "three). Slow the breath (physiology breaks link four). Turn on the light "
        "(sensory clarity breaks link five). You do not have to break every link — "
        "chains are only as strong as their weakest, and one solid break usually "
        "collapses the rest. The skill is recognizing the cascade early, while it is "
        "still three links long and not yet thirty."
    ),
    "how_it_works": (
        "Cascades run on feedback: cognitive elaboration (memories, imagined futures) "
        "raises arousal, and arousal is then misread as evidence of danger, which "
        "fuels more elaboration. This is the two-factor loop — the body provides the "
        "fuel, the mind provides the story, each intensifying the other. Interventions "
        "that target either factor (new information, slow breathing, labeling) reduce "
        "the loop's gain. Early intervention works best because each added link "
        "increases the system's momentum."
    ),
    "key_points": [
        "One unresolved trigger can chain into memories, imagined futures, and body feedback.",
        "Each link feels like confirmation — but the loop is circular, not evidential.",
        "Arousal feeds imagination; imagination feeds arousal.",
        "Break any single link with authority: check, name, question, breathe, illuminate.",
        "One solid break usually collapses the whole chain.",
        "Catch cascades early — three links are easier than thirty.",
    ],
    "requirements": [
        "A remembered cascade to trace link by link",
        "One go-to link-breaker practiced in advance",
    ],
    "standards": [
        "Two-factor theory: arousal plus interpretation (Schachter and Singer)",
        "Feedback loops in emotion escalation",
        "Appraisal and reappraisal (Lazarus)",
    ],
    "citations": [
        "Schachter, S., and Singer, J. Cognitive, social, and physiological determinants of emotional state. Psychological Review; 1962.",
        "Lazarus, R. S. Emotion and Adaptation. Oxford University Press; 1991.",
        "Ekman, P. Emotions Revealed. 2nd ed. Holt; 2007.",
    ],
    "sig_lens": (
        "Through the Signature lens, a fear cascade is a rumor spreading through the "
        "building — each floor repeating it louder. The Signature reader is the "
        "manager who walks to the source instead of listening to the echo. One verified "
        "fact, delivered to the right floor, quiets the whole building. In the "
        "Signature method, you do not argue with the rumor; you inspect the source."
    ),
},
{
    "key": "fear-actions",
    "name": "What People Do When Afraid",
    "group": "Fear in Behavior",
    "ladder_rank": 9,
    "ladder_tier": "advanced",
    "description": (
        "Watch what fear does to behavior and you will see ancient software running on "
        "modern hardware. The first move is often freeze: going suddenly still and "
        "quiet, the body buying time to assess. Next comes flight in its many modern "
        "costumes — leaving the room, canceling the appointment, crossing the street, "
        "scrolling past the scary headline, changing the subject. Avoidance is flight "
        "in slow motion, and it is fear's most common behavior by far. Then fight: "
        "snapping at the person who startled you, arguing fiercely when cornered, the "
        "aggressive driving after a near-miss. Fourth is the social move — clinging, "
        "calling someone, moving toward the group, because safety has always been a "
        "team sport. Around these big four cluster the smaller tells: checking (locks, "
        "phones, exits, repeatedly), hiding (behind people, behind humor, behind "
        "busyness), appeasing (agreeing quickly to defuse tension, laughing along), "
        "and preparing (over-packing, over-researching, rehearsing conversations). None "
        "of these are moral categories — they are strategies, and each one makes sense "
        "in context. The question to ask of any fear behavior is not \"is this brave?\" "
        "but \"is this working?\" Avoidance works today and charges interest tomorrow: "
        "every avoided thing teaches the alarm that the thing was indeed dangerous, "
        "which makes the next avoidance more likely. That is the behavior trap. The "
        "way out is graded: approach the feared thing in small, survivable steps, and "
        "let the alarm learn from experience that the steps are safe. Behavior is "
        "where fear is finally negotiated — feelings propose, actions dispose."
    ),
    "how_it_works": (
        "Fear behaviors are the output end of the threat system: freeze (assess), "
        "flight (increase distance), fight (remove the threat), affiliate (increase "
        "safety in numbers). Checking, preparing, and appeasing are instrumental "
        "strategies that reduce uncertainty or social danger. Avoidance is negatively "
        "reinforced — it removes the bad feeling immediately, which teaches the brain "
        "to repeat it — and that is why avoidance grows: the alarm never gets the "
        "disconfirming evidence that the avoided thing was safe. Graded approach works "
        "by delivering that evidence in doses the system can accept."
    ),
    "key_points": [
        "The big four: freeze, flight, fight, and affiliate (seek the group).",
        "Avoidance is flight in slow motion — fear's most common behavior.",
        "Checking, appeasing, and preparing are uncertainty-reduction strategies.",
        "Ask \"is this working?\" — not \"is this brave?\"",
        "Avoidance charges interest: it teaches the alarm the thing was dangerous.",
        "Graded approach — small survivable steps — renegotiates the behavior.",
    ],
    "requirements": [
        "One of your own avoidance patterns, named without judgment",
        "A small first step you could actually take",
    ],
    "standards": [
        "Defensive behavior systems: freeze, flight, fight, affiliate",
        "Negative reinforcement of avoidance",
        "Graded exposure principles",
    ],
    "citations": [
        "Cannon, W. B. Bodily Changes in Pain, Hunger, Fear and Rage. Appleton; 1915.",
        "LeDoux, J. The Emotional Brain. Simon & Schuster; 1996.",
        "Marks, I. M. Fears, Phobias, and Rituals. Oxford University Press; 1987.",
    ],
    "sig_lens": (
        "Through the Signature lens, fear behaviors are the crew's emergency drills — "
        "freeze, withdraw, engage, muster — each valid in its season. The Signature "
        "reader audits the drills: which ones still serve, which have become "
        "superstition. Avoidance is a drill that passed its expiry date, and the "
        "Signature method replaces it with graded advance — small, signed, survivable "
        "steps, logged as victories."
    ),
},
{
    "key": "fear-words",
    "name": "What People Say When Afraid: Words, Tone, Speech",
    "group": "Fear in Behavior",
    "ladder_rank": 9,
    "ladder_tier": "advanced",
    "description": (
        "Fear has a voice, and once you know it you will hear it everywhere. The words "
        "come first: questions, questions, questions — \"what was that?\", \"are you sure?\", "
        "\"what if...?\" — the mind trying to interrogate uncertainty into submission. "
        "Then the reassurance-seeking phrases: \"it's going to be okay, right?\", \"you'd "
        "tell me if something was wrong, right?\" Then the catastrophizing script, often "
        "half-joking: \"we're all going to die\" (turbulence), \"I'm going to fail "
        "everything\" (exam week). Listen for absolutes — always, never, everything, "
        "nothing — fear loves to deal in certainties because uncertainty is what hurts. "
        "The tone carries as much as the words: pitch climbs, sometimes a full step "
        "higher; speech speeds up or breaks into stammers and restarts; volume goes "
        "either loud (alarm-calling) or tiny (the frightened whisper). Sentences get "
        "shorter. Pauses get longer. People repeat themselves — \"are we safe, are we "
        "safe?\" — because the answer did not land the first time through the noise. "
        "There is also what fear does to listening: the frightened person hears "
        "selectively, catching the threatening words in a sentence and missing the "
        "reassuring ones, then asking you to repeat the reassurance. If you are "
        "speaking to someone afraid, this is your manual: short sentences, low steady "
        "pitch, concrete information (\"the pilot says it is normal chop, twenty more "
        "minutes\"), and patient repetition without irritation. And if the frightened "
        "voice is your own, narrating it helps: \"my voice is shaking because my alarm "
        "is up, not because I am in danger\" — naming the voice loosens its script."
    ),
    "how_it_works": (
        "Fear reshapes speech through arousal: heightened sympathetic activity tenses "
        "the vocal apparatus (raising pitch), accelerates output, and disrupts the "
        "planning of complex sentences. Question-asking and reassurance-seeking are "
        "instrumental — attempts to extract certainty from the environment. Selective "
        "listening is attentional narrowing applied to audition: threat-relevant words "
        "get priority processing. Calm, concrete, repeated input works because it "
        "supplies exactly what the narrowed system can absorb: simple, certain, "
        "slow."
    ),
    "key_points": [
        "Fear speaks in questions and reassurance-seeking phrases.",
        "Absolutes (always, never, everything) are fear's favorite grammar.",
        "Pitch climbs, speech speeds or stammers, sentences shorten.",
        "Frightened listening is selective — threat words land, reassurance slides off.",
        "To help: short sentences, low steady pitch, concrete facts, patient repetition.",
        "Narrating your own fear-voice (\"my alarm is up\") loosens its script.",
    ],
    "requirements": [
        "One remembered conversation where fear did the talking",
        "Practice hearing the tone under the words",
    ],
    "standards": [
        "Vocal correlates of arousal",
        "Attentional narrowing in audition",
        "Reassurance-seeking as uncertainty reduction",
    ],
    "citations": [
        "Ekman, P. Emotions Revealed. 2nd ed. Holt; 2007.",
        "Scherer, K. R. Vocal communication of emotion. Psychological Review; 1986.",
        "Lazarus, R. S. Emotion and Adaptation. Oxford University Press; 1991.",
    ],
    "sig_lens": (
        "Through the Signature lens, frightened speech is static on the line — "
        "questions repeating, pitch climbing, signal degrading. The Signature reader "
        "learns to transmit through static: short, low, concrete, repeated. And when "
        "the static is his own, he names the interference out loud — \"this is my "
        "alarm on the line, not the message\" — and the line clears."
    ),
},
{
    "key": "fear-decisions",
    "name": "How Fear Changes Decisions and Judgment",
    "group": "Fear in Behavior",
    "ladder_rank": 9,
    "ladder_tier": "advanced",
    "description": (
        "Fear is a terrible financial advisor and everyone takes its meetings. Under "
        "fear, decision-making changes in predictable ways. First, risk goes into "
        "hiding: the frightened mind overweights what could go wrong and underweights "
        "what could go right, so the safe-looking option wins even when the math "
        "favors boldness. Second, time horizons collapse: fear votes for relief NOW — "
        "cancel the trip, quit the course, sell at the bottom — trading long-term "
        "good for immediate calm. Third, the sample gets rigged: attention narrows to "
        "threatening information, so the evidence reviewed is the scariest evidence, "
        "which confirms the fear, which narrows attention further. Fourth, control gets "
        "mispriced: people pay too much for the illusion of control (the familiar "
        "route, the extra insurance) and too little attention to actual leverage. "
        "Fifth, other people become either lifelines or suspects — fear polarizes the "
        "social field, producing clinging or suspicion with little middle ground. None "
        "of this means fear must be locked out of the meeting. Fear is often the only "
        "one who read the risk section of the report. The skill is procedural: when "
        "the stakes are real and the alarm is loud, slow the decision down (sleep on "
        "it if you can), write the options and their real odds, ask what you would "
        "advise a friend, and separate the decision into a reversible first step. Fear "
        "may still get a vote — it earned one — but it does not get to chair the "
        "meeting alone."
    ),
    "how_it_works": (
        "Fear shifts decision-making through well-mapped biases: loss aversion "
        "intensifies, probability estimates skew toward bad outcomes, temporal "
        "discounting steepens (immediate relief outweighs future gain), and "
        "attentional narrowing rigs the evidence sample. These are features of a "
        "system optimized for surviving the next ten minutes, misapplied to choices "
        "with ten-year horizons. Procedural fixes — delay, written odds, the "
        "friend-test, reversible first steps — work by re-engaging the deliberative "
        "system the alarm had demoted."
    ),
    "key_points": [
        "Fear overweights what could go wrong and hides the upside.",
        "Time horizons collapse — immediate relief beats long-term good.",
        "Narrowed attention rigs the evidence sample toward the scariest data.",
        "People overpay for the illusion of control under fear.",
        "Slow it down: sleep, written odds, the friend-test, reversible first steps.",
        "Fear gets a vote — it read the risk section — but not the only chair.",
    ],
    "requirements": [
        "One decision you made while afraid, reviewed honestly",
        "Paper for the written-odds exercise",
    ],
    "standards": [
        "Loss aversion and framing (Kahneman and Tversky)",
        "Affect and risk perception",
        "Dual-process decision models under arousal",
    ],
    "citations": [
        "Kahneman, D., and Tversky, A. Prospect theory. Econometrica; 1979.",
        "Loewenstein, G., et al. Risk as feelings. Psychological Bulletin; 2001.",
        "Lazarus, R. S. Emotion and Adaptation. Oxford University Press; 1991.",
    ],
    "sig_lens": (
        "Through the Signature lens, fear at the decision table is the risk officer — "
        "valuable, loud, and not to be given the gavel. The Signature reader runs the "
        "meeting by protocol: the officer presents the dangers, the numbers are "
        "written down, the friend-test is taken, and the first step is made "
        "reversible. In the Signature method, no alarm ever chairs the meeting alone."
    ),
},
{
    "key": "fear-escalation",
    "name": "Fear Under Rising Intensity: Escalating Behavior",
    "group": "Fear in Behavior",
    "ladder_rank": 9,
    "ladder_tier": "advanced",
    "description": (
        "Watch fear climb its own ladder and behavior simplifies at every rung. At low "
        "intensity, behavior is strategic: the person checks, plans, asks questions, "
        "takes sensible precautions — fear working as intended, a consultant. At "
        "moderate intensity, behavior gets urgent: pacing, repeated checking, snapping "
        "at interruptions, fleeing the room or the conversation — the consultant has "
        "become a manager, issuing orders. At high intensity, behavior goes primitive: "
        "bolting, screaming, freezing rigid, shoving past people, lashing out at "
        "whoever is nearest — the manager has been replaced by the old animal "
        "software, and the thinking mind is watching from the back seat. The "
        "escalation is usually fast — seconds to minutes — which is why interventions "
        "must be matched to the rung. Reasoning works at the bottom rung and fails at "
        "the top: you cannot debate someone mid-bolt, but you can move with them, "
        "speak simply, and reduce stimulation until the rung comes down. For your own "
        "escalation, the earlier you notice the climb, the more tools you have — at "
        "rung one you can breathe and plan; at rung three you can mostly hang on and "
        "ride. This is also why de-escalation is a kindness and a skill: a calm voice, "
        "space, no sudden moves, no crowding, simple choices (\"would you like to step "
        "outside or sit here?\"). You are not arguing with the person; you are waiting "
        "out the alarm with them. Every rung comes back down. That is the one fact to "
        "hold onto when someone — including you — is at the top."
    ),
    "how_it_works": (
        "Escalation reflects progressive recruitment of faster, older defense circuits "
        "and progressive demotion of deliberative control as arousal rises. Low "
        "arousal leaves the thinking mind in charge (strategic behavior); high arousal "
        "hands control to reflexive defense programs (primitive behavior). The "
        "transition is graded but fast, and it reverses as arousal falls — which is "
        "why reducing stimulation, rather than adding argument, is the effective "
        "intervention at high rungs."
    ),
    "key_points": [
        "Low rung: strategic behavior — checking, planning, sensible precaution.",
        "Middle rung: urgent behavior — pacing, snapping, fleeing.",
        "Top rung: primitive behavior — bolting, freezing, lashing out.",
        "Reasoning works at the bottom rung and fails at the top.",
        "De-escalation: calm voice, space, no sudden moves, simple choices.",
        "Every rung comes back down — hold that fact at the top.",
    ],
    "requirements": [
        "A memory of your own climb, rung by rung",
        "One de-escalation phrase practiced in advance",
    ],
    "standards": [
        "Arousal and behavioral complexity (Yerkes and Dodson)",
        "Defensive cascade: freeze, flight, fight",
        "De-escalation practice principles",
    ],
    "citations": [
        "Yerkes, R. M., and Dodson, J. D. Journal of Comparative Neurology and Psychology; 1908.",
        "Cannon, W. B. Bodily Changes in Pain, Hunger, Fear and Rage. Appleton; 1915.",
        "Ekman, P. Emotions Revealed. 2nd ed. Holt; 2007.",
    ],
    "sig_lens": (
        "Through the Signature lens, escalation is the building's fire protocol "
        "climbing its levels — consultant, manager, old emergency crew. The Signature "
        "reader meets each level with its matching key: reason for the consultant, "
        "calm space for the crew. He never argues with the top rung; he waits it out "
        "beside it, holding the one fact the Signature method never drops — every "
        "rung comes back down."
    ),
},
{
    "key": "fear-healthy",
    "name": "Expressing Fear in Healthy Ways",
    "group": "Healthy Expression",
    "ladder_rank": 9,
    "ladder_tier": "advanced",
    "description": (
        "Fear expressed well is fear that moves through you instead of setting up "
        "residence. The healthiest first move is naming: saying, out loud or in "
        "writing, \"I am afraid of...\" — the sentence that turns a fog into an object "
        "you can look at. The second is telling someone safe: a friend, a partner, a "
        "colleague you trust. Spoken fear shrinks; it is secrecy that lets it grow in "
        "the dark. The third is the body: fear is mobilization energy, and it wants to "
        "move — a walk, a run, shaking out your hands, even cleaning the kitchen with "
        "gusto gives the arousal somewhere lawful to go. The fourth is breath: slow, "
        "deliberate exhales are a direct line to the alarm's off-switch, because the "
        "body reads long exhales as \"the emergency is over.\" The fifth is channeling: "
        "turning the fear into preparation — the worry about the presentation becomes "
        "rehearsal, the worry about the storm becomes checking supplies. Fear is "
        "excellent raw material for readiness when it is given a job. The sixth is "
        "writing it out: ten minutes of unedited \"I am afraid that...\" on paper drains "
        "the pressure like opening a valve, and the page never judges. What makes all "
        "of these healthy is the direction: the fear is moving — out through words, "
        "out through motion, out through action — instead of circling inside. You do "
        "not have to be eloquent or brave-looking. You just have to let it move."
    ),
    "how_it_works": (
        "Healthy expression works through three channels. Labeling recruits the "
        "thinking mind and reduces the alarm's monopoly on the feeling. Sharing "
        "recruits social safety — the nervous system co-regulates with trusted others, "
        "literally calming faster in company. Movement and slow breathing metabolize "
        "arousal: the mobilized body completes its stress cycle instead of idling at "
        "high revs. Channeling converts the motivational energy of fear into "
        "preparation, which addresses the threat the alarm was pointing at. Each "
        "channel moves the feeling from circulation to resolution."
    ),
    "key_points": [
        "Name it: \"I am afraid of...\" turns fog into an object.",
        "Tell someone safe — spoken fear shrinks; secrecy grows it.",
        "Move the body — arousal wants lawful motion.",
        "Slow exhales signal the alarm's off-switch directly.",
        "Channel it: turn worry into preparation and rehearsal.",
        "Write it out — ten unedited minutes drains pressure like a valve.",
    ],
    "requirements": [
        "One safe person (or one private page) for the first telling",
        "Ten minutes and something to write with",
        "Space to move — even a hallway will do",
    ],
    "standards": [
        "Affect labeling reduces arousal (Lieberman et al., 2007)",
        "Social co-regulation of the nervous system",
        "Stress-cycle completion through movement and breath",
    ],
    "citations": [
        "Lieberman, M. D., et al. Putting feelings into words. Psychological Science; 2007.",
        "Ekman, P. Emotions Revealed. 2nd ed. Holt; 2007.",
        "Selye, H. The Stress of Life. McGraw-Hill; 1956.",
    ],
    "sig_lens": (
        "Through the Signature lens, healthy expression is the alarm's proper "
        "discharge — the bell rung, read, and answered, never left ringing in an "
        "empty hall. The Signature reader gives every fear its hearing: named in the "
        "log, spoken to a trusted ear, moved through the body, set to work as "
        "preparation. In the Signature method, a feeling that moves is a feeling "
        "that serves."
    ),
},
{
    "key": "fear-unhealthy",
    "name": "Bottled or Exploding: The Costs of Unhealthy Expression",
    "group": "Healthy Expression",
    "ladder_rank": 10,
    "ladder_tier": "advanced",
    "description": (
        "Fear that is not expressed does not disappear — it goes underground and "
        "sends up invoices. The first unhealthy pattern is bottling: pushing the fear "
        "down, smiling through it, telling yourself (and everyone) that you are fine. "
        "Bottled fear leaks. It leaks as tension headaches and clenched jaws, as "
        "irritability over nothing, as exhaustion that sleep does not fix, as the "
        "sudden tears in the car after holding it together all day. The bottle always "
        "has a pressure limit, and nobody gets to choose when it blows. The second "
        "pattern is exploding: the fear converts to fury and detonates — shouting at "
        "the kids after the scary phone call, slamming doors, sending the message you "
        "regret by morning. Explosions feel powerful for about four seconds and then "
        "send their own bill: guilt, damage to repair, and the original fear still "
        "sitting there underneath, untouched. The third pattern is numbing: drowning "
        "the alarm in scrolling, snacking, drinking, or busyness — anything to not "
        "feel it. Numbing works the way holding a beach ball underwater works: the "
        "moment you stop pushing, it rockets up, often at 3 a.m. All three patterns "
        "share one trait: the fear never got its hearing. It was silenced, detonated, "
        "or drowned — but never named, never moved, never answered. The costs are "
        "real but so is the exit: any step toward healthy expression — one honest "
        "sentence, one walk, one telling — starts converting the backlog. You do not "
        "have to fix years of bottling in a day. You just have to open the valve a "
        "crack and let the pressure start moving."
    ),
    "how_it_works": (
        "Suppression keeps physiological arousal elevated while removing its outlet — "
        "the body stays mobilized with nowhere to go, which is why bottling produces "
        "tension symptoms. Explosion is the fear-anger blend discharging through the "
        "anger channel: high arousal plus a target. Numbing avoids the feeling by "
        "occupying attention, but the underlying arousal and its triggers persist "
        "unprocessed. All three maintain the alarm state instead of resolving it, "
        "which is why their costs compound over time while healthy expression "
        "compounds relief."
    ),
    "key_points": [
        "Bottled fear leaks: tension, irritability, exhaustion, sudden tears.",
        "Exploding converts fear to fury — four seconds of power, then the bill.",
        "Numbing is a beach ball held underwater — it rockets up at 3 a.m.",
        "All three skip the hearing: never named, never moved, never answered.",
        "The costs compound; so does relief, once expression starts.",
        "Open the valve a crack — one honest sentence is enough to begin.",
    ],
    "requirements": [
        "Honesty about your own default pattern — no judgment",
        "One small healthy-expression step to try this week",
    ],
    "standards": [
        "Emotion suppression and physiological cost",
        "Fear-anger blend discharge",
        "Avoidance maintenance cycles",
    ],
    "citations": [
        "Ekman, P. Emotions Revealed. 2nd ed. Holt; 2007.",
        "Lazarus, R. S. Emotion and Adaptation. Oxford University Press; 1991.",
        "Selye, H. The Stress of Life. McGraw-Hill; 1956.",
    ],
    "sig_lens": (
        "Through the Signature lens, bottling is a sealed boiler, exploding is a burst "
        "pipe, numbing is a gauge with tape over it — three ways to mistreat the same "
        "instrument. The Signature reader maintains his equipment: pressure is logged, "
        "vented on schedule, and never left to find its own way out. In the Signature "
        "method, maintenance is not weakness — it is what keeps the machine running "
        "for decades."
    ),
},
{
    "key": "fear-practices",
    "name": "Everyday Practices That Keep Fear in Balance",
    "group": "Healthy Expression",
    "ladder_rank": 10,
    "ladder_tier": "advanced",
    "description": (
        "Fear balance is not built in the crisis — it is built on Tuesdays. The "
        "practices are small, unglamorous, and cumulative. Sleep first: a rested "
        "nervous system has a calmer alarm; an exhausted one startles at shadows. "
        "Protect the last hour before bed — no scare media, no doomscrolling, nothing "
        "that rings the bell right before you ask it to sleep. Move daily: the body "
        "that regularly spends its arousal on walks, work, or play has less surplus "
        "to convert into jitters. Daylight and routine steady the system the way a "
        "metronome steadies a musician. Talk early: mention the small worry on Monday "
        "instead of presenting the large one on Friday — spoken early, fears stay "
        "small. Practice graded facing: deliberately, gently, do the slightly-scary "
        "things — the phone call, the high balcony viewed from behind glass, the "
        "honest conversation — in steps your system can absorb. Each survived step is "
        "a vote the alarm counts. Keep a fear log for a month: date, trigger, volume "
        "(1-10), what helped. Patterns emerge — the 3 a.m. worries, the pre-meeting "
        "spike — and patterns can be planned for. Limit the inputs you can limit: the "
        "news diet, the horror marathon before a stressful week, the group chat that "
        "trades in alarm. And keep one standing appointment with calm — a walk, a "
        "bath, music, prayer-free quiet sitting — whatever returns you to baseline, "
        "scheduled like medicine. None of these eliminate fear, and none should: the "
        "goal is a well-kept instrument, not a silenced one. If fear ever starts "
        "running your days — shrinking your world, costing sleep for weeks — reaching "
        "out to a trusted counselor or health professional is a strong, sensible "
        "move, the same as calling a specialist for any instrument you cannot tune "
        "alone."
    ),
    "how_it_works": (
        "Practices work by lowering background arousal and raising coping evidence. "
        "Sleep, movement, and routine reduce the system's gain — the same trigger "
        "produces a smaller response in a rested body. Early talking and graded facing "
        "supply disconfirming evidence that updates the alarm's estimates. Logging "
        "converts vague dread into specific, plannable patterns. Input limits reduce "
        "unnecessary alarm trips. Together they shift the system from reactive to "
        "maintained: fewer false alarms, faster recovery, steadier baseline."
    ),
    "key_points": [
        "Balance is built on ordinary days, not in crises.",
        "Sleep, daylight, movement, and routine lower the alarm's gain.",
        "Talk early — Monday's small worry beats Friday's large one.",
        "Graded facing: slightly-scary things in absorbable steps.",
        "Keep a fear log — patterns emerge, and patterns can be planned for.",
        "Limit alarm inputs; keep a standing appointment with calm.",
        "Persistent, world-shrinking fear deserves professional support — a strong move.",
    ],
    "requirements": [
        "One practice to start this week — just one",
        "A notebook for the month-long fear log",
        "Patience: practices compound quietly",
    ],
    "standards": [
        "Sleep and emotional regulation",
        "Graded exposure principles",
        "Stress-recovery balance (Selye)",
    ],
    "citations": [
        "Walker, M. Why We Sleep. Scribner; 2017.",
        "Selye, H. The Stress of Life. McGraw-Hill; 1956.",
        "Marks, I. M. Fears, Phobias, and Rituals. Oxford University Press; 1987.",
    ],
    "sig_lens": (
        "Through the Signature lens, these practices are the maintenance schedule of "
        "a fine instrument — oiled, tuned, and played daily so it never goes shrill. "
        "The Signature reader keeps the schedule without drama: sleep as calibration, "
        "movement as venting, the log as the service record. In the Signature method, "
        "the unglamorous daily turn of the wrench is what keeps the bell true."
    ),
},
{
    "key": "fear-reading",
    "name": "Reading Fear in Others: Face, Body, Voice, Behavior",
    "group": "Recognizing Fear in Others",
    "ladder_rank": 10,
    "ladder_tier": "advanced",
    "description": (
        "Reading fear in others is a kindness skill with a simple method: scan the "
        "four channels and believe the pattern. Channel one, the face: brows raised "
        "and knitted, eyes widened with white showing, lips stretched or pressed — "
        "even a flicker of it counts, because fear flashes fast. Channel two, the "
        "body: the shrink — shoulders up, chest caved, arms pulled in — or the "
        "freeze, sudden unnatural stillness; or the opposite, restless motion with "
        "nowhere to go. Channel three, the voice: pitch climbing, speech speeding or "
        "stumbling, the frightened whisper or the too-loud laugh that does not match "
        "the eyes. Channel four, behavior: backing away, clinging close, checking "
        "things repeatedly, going quiet in a way that is not their usual quiet, "
        "agreeing too fast just to end the tension. No single channel proves anything "
        "— a wide-eyed person might just be surprised, a quiet one might just be "
        "tired — but two or three channels together are a reliable read. Context is "
        "the fifth channel: the turbulence, the bad news just delivered, the dark "
        "parking lot. Read gently and hold your conclusions lightly; the goal is not "
        "to announce \"you're scared\" (which can shame or startle) but to adjust your "
        "own behavior — slow down, soften, offer an exit, make room. People who feel "
        "read with kindness relax faster than people who feel watched. The best fear "
        "readers are not the most analytical but the most attentive: they notice the "
        "small change — the laugh that is half a pitch too high, the hand that keeps "
        "checking the door — and they respond to it before it has to become a "
        "shout."
    ),
    "how_it_works": (
        "Multi-channel reading works because fear's outputs are partially involuntary "
        "and therefore correlated: when the alarm fires, face, body, voice, and "
        "behavior tend to shift together. Any single channel can mislead (display "
        "rules, individual differences), but convergent channels raise accuracy "
        "sharply. Context supplies the base rate — the prior probability that fear is "
        "present — which is why the same wide eyes mean different things in a horror "
        "movie and a hospital waiting room. Kind responding then feeds back: feeling "
        "safely read lowers the other person's arousal, which visibly softens the "
        "channels."
    ),
    "key_points": [
        "Scan four channels: face, body, voice, behavior — believe the pattern.",
        "Two or three channels together are a reliable read; one alone can mislead.",
        "Context is the fifth channel — same signal, different meaning per setting.",
        "Hold conclusions lightly; never announce \"you're scared\" as an accusation.",
        "Adjust yourself: slow down, soften, offer an exit, make room.",
        "The best readers are the most attentive, not the most analytical.",
    ],
    "requirements": [
        "The face, body, and voice records as background",
        "A commitment to read for kindness, never for advantage",
    ],
    "standards": [
        "Multi-channel emotion recognition",
        "Display rules and individual differences (Ekman and Friesen)",
        "Context effects on expression reading",
    ],
    "citations": [
        "Ekman, P. Emotions Revealed. 2nd ed. Holt; 2007.",
        "Ekman, P., and Friesen, W. V. Constants across cultures in the face and emotion. Journal of Personality and Social Psychology; 1971.",
        "Darwin, C. The Expression of the Emotions in Man and Animals. John Murray; 1872.",
    ],
    "sig_lens": (
        "Through the Signature lens, reading fear in others is watchman work — "
        "scanning the four channels the way a lookout scans the horizon. The "
        "Signature reader takes the watch seriously and gently: a noticed signal is "
        "answered with steadiness, never with exposure. In the Signature method, to "
        "see someone's fear clearly is to become, quietly, part of their safety."
    ),
},
{
    "key": "fear-support",
    "name": "What to Say and Do When Someone Is Afraid",
    "group": "Recognizing Fear in Others",
    "ladder_rank": 10,
    "ladder_tier": "advanced",
    "description": (
        "When someone near you is afraid, you become part of their environment — and "
        "the environment is half the feeling. Start with safety and the body: if "
        "there is real danger, address it first — move them, shield them, get help — "
        "because no words work until the threat is handled. Then be the calm in the "
        "room: slow your own voice, unclench your own shoulders; nervous systems "
        "co-regulate, and your steadiness is contagious in the best way. Say what is "
        "true and concrete: \"I am here. The door is locked. The storm will pass in "
        "about twenty minutes.\" Frightened minds cannot use abstractions — give them "
        "facts with edges. Believe them: \"that sounds really scary\" beats \"there's "
        "nothing to be afraid of\" every time, because the second sentence argues "
        "with their nervous system and loses. Offer choices, not commands: \"would you "
        "like to sit here or step outside?\" — choice restores a feeling of control, "
        "which is exactly what fear stole. Breathe with them if they are open to it — "
        "\"let's do slow breaths together\" — or simply sit nearby without demanding "
        "conversation; presence is an intervention. For children, get low, get warm, "
        "name it simply (\"that was a big scary noise\"), and stay until the body "
        "settles. What you are really doing in all of this is lending your calm "
        "nervous system as scaffolding while theirs rebuilds. You do not have to fix "
        "the fear or explain it away. You just have to be the proof, standing next "
        "to them, that safety exists."
    ),
    "how_it_works": (
        "Support works through co-regulation: calm presence, slow voice, and steady "
        "breathing entrain the frightened person's arousal downward — the social "
        "nervous system treats a trusted calm other as safety data. Concrete true "
        "statements supply the certainty the narrowed mind is starving for. Belief "
        "and validation prevent the second layer of shame-fear. Offered choices "
        "restore perceived control, which directly lowers the appraisal of threat. "
        "Each element reduces one driver of the alarm; together they let it stand "
        "down."
    ),
    "key_points": [
        "Handle real danger first — no words work until the threat is addressed.",
        "Be the calm in the room: slow voice, unclenched shoulders — steadiness is contagious.",
        "Say what is true and concrete — frightened minds need facts with edges.",
        "\"That sounds really scary\" beats \"there's nothing to be afraid of.\"",
        "Offer choices, not commands — choice restores the control fear stole.",
        "Presence is an intervention; you are scaffolding while they rebuild.",
    ],
    "requirements": [
        "Your own calm practiced first — you cannot lend what you do not have",
        "A few concrete reassuring facts ready for common scares",
    ],
    "standards": [
        "Social co-regulation of arousal",
        "Perceived control and threat appraisal (Lazarus)",
        "Supportive communication principles",
    ],
    "citations": [
        "Lazarus, R. S. Emotion and Adaptation. Oxford University Press; 1991.",
        "Ekman, P. Emotions Revealed. 2nd ed. Holt; 2007.",
        "Porges, S. W. The Polyvagal Theory. Norton; 2011.",
    ],
    "sig_lens": (
        "Through the Signature lens, supporting a frightened person is standing as "
        "the steady lighthouse while their seas run high. The Signature reader does "
        "not lecture the waves or deny the storm — he holds the light, speaks the "
        "true facts, and offers the helm back one choice at a time. In the Signature "
        "method, calm lent is never calm lost."
    ),
},
{
    "key": "fear-mistakes",
    "name": "What NOT to Do Around a Frightened Person",
    "group": "Recognizing Fear in Others",
    "ladder_rank": 10,
    "ladder_tier": "advanced",
    "description": (
        "Good intentions misfire around fear more than anywhere else, so here is the "
        "list of classic mistakes — each one common, each one fixable. Do not mock or "
        "tease: \"don't be such a baby\" does not toughen anyone; it adds shame to fear, "
        "and shame-fear is harder to soothe than plain fear. Do not startle them on "
        "purpose — the \"gotcha\" prank spends their trust for your laugh, and the "
        "nervous system keeps the receipt. Do not flood them with logic: a ten-point "
        "lecture on turbulence statistics does not reach a mind running on alarm "
        "fuel — one concrete fact at a time, or wait until the rung comes down. Do "
        "not say \"calm down\" as a command; it is heard as criticism, and nobody in "
        "history has ever calmed down from being ordered to. Do not force "
        "confrontation — dragging someone toward the thing they fear, physically or "
        "verbally, teaches the alarm that you are part of the danger. Do not tell "
        "your own horror stories (\"oh, you think THAT'S scary, once I...\") — it "
        "competes with their fear instead of comforting it. Do not disappear without "
        "a word; abandonment mid-fear reads as confirmation that the situation is "
        "indeed hopeless. And do not take their fear personally — the snapping, the "
        "clinging, the irrational demands are the alarm talking, not the person. "
        "Underneath every item on this list is one principle: do not add arousal to "
        "arousal. The frightened system is already at its limit; your job is to be "
        "the thing in the room that is not another threat."
    ),
    "how_it_works": (
        "Each mistake adds fuel to one of fear's drivers. Mockery adds social threat "
        "on top of the original threat. Forced confrontation spikes arousal past the "
        "point where learning can happen. Logic-flooding demands deliberative "
        "processing from a system that has demoted it. Commands like \"calm down\" "
        "register as social evaluation, raising arousal further. Disappearing removes "
        "the co-regulating presence the system was using as scaffolding. The "
        "principle — do not add arousal to arousal — follows directly from the "
        "escalation ladder: everything that raises stimulation pushes the rung up."
    ),
    "key_points": [
        "Do not mock — shame-fear is harder to soothe than plain fear.",
        "Do not startle on purpose — pranks spend trust; the body keeps the receipt.",
        "Do not flood with logic — one concrete fact, or wait for the rung to drop.",
        "\"Calm down\" as a command has never calmed anyone — it lands as criticism.",
        "Do not force confrontation or compete with horror stories.",
        "Do not disappear mid-fear; do not take the alarm's behavior personally.",
        "One principle: do not add arousal to arousal.",
    ],
    "requirements": [
        "One of these mistakes you have made — owned kindly",
        "A replacement move for each of your top two",
    ],
    "standards": [
        "Escalation dynamics under added stimulation",
        "Social threat and shame effects on arousal",
        "Supportive communication principles",
    ],
    "citations": [
        "Ekman, P. Emotions Revealed. 2nd ed. Holt; 2007.",
        "Lazarus, R. S. Emotion and Adaptation. Oxford University Press; 1991.",
        "Yerkes, R. M., and Dodson, J. D. Journal of Comparative Neurology and Psychology; 1908.",
    ],
    "sig_lens": (
        "Through the Signature lens, these mistakes are friendly fire — the would-be "
        "helper shelling his own position. The Signature reader studies the "
        "misfires the way an officer studies them: not to assign blame, but to stop "
        "repeating them. In the Signature method, the first duty of the steady "
        "presence is to do no further alarming."
    ),
},
{
    "key": "fear-map",
    "name": "The Neighbors and Opposites of Fear: A Related-Emotions Map",
    "group": "Emotion Mixes and Simulation",
    "ladder_rank": 10,
    "ladder_tier": "advanced",
    "description": (
        "Every emotion has a neighborhood, and fear's is worth mapping street by "
        "street. Nearest neighbors first. Anxiety: fear's forward-looking cousin — "
        "fear says \"danger is here,\" anxiety says \"danger might come.\" They share the "
        "body's arousal but differ in time: present versus future. Dread: fear with a "
        "calendar — the heavy knowing that something bad is scheduled, like waiting "
        "for test results. Alarm: fear's loudest, shortest neighbor — the siren "
        "itself, all signal and no story. Startle: the reflex blink-and-jump, faster "
        "and simpler than fear, gone in a second. Horror: fear felt as a witness — "
        "the chill of seeing or hearing about something terrible happen to someone "
        "else. Nervousness: fear's mild, social form — the flutter before performing. "
        "Now the close cousins people confuse. Fright versus startle: startle is the "
        "one-second reflex; fright is startle plus the lingering appraisal (\"am I "
        "safe?\"). Fear versus anxiety: same family, different tense — one points at "
        "now, the other at later. And the opposites, the far side of the map: calm "
        "(the settled nervous system), safety (the believed absence of threat), "
        "courage (acting well while afraid — not fear's absence but its answer), and "
        "confidence (the learned expectation that you can handle what comes). "
        "Opposites are not enemies of fear; they are its destinations. You do not "
        "delete fear to reach calm — you answer the alarm, handle the threat, and "
        "arrive at calm through the far side of the feeling. Keep this map handy: "
        "when a feeling is hard to name, check the neighbors. Precision in naming is "
        "precision in handling."
    ),
    "how_it_works": (
        "The map works by two dimensions researchers use to organize emotions: time "
        "(immediate versus anticipated threat separates fear from anxiety and dread) "
        "and self-involvement (direct threat versus witnessed threat separates fear "
        "from horror). Intensity forms the third axis — nervousness, fear, terror as "
        "one continuum. Opposites sit across the arousal and valence axes: calm is "
        "low arousal, safety is positive appraisal, courage is approach-despite-fear, "
        "confidence is expected coping. Placing a feeling on the map automatically "
        "suggests its handling: neighbors share remedies, opposites suggest goals."
    ),
    "key_points": [
        "Neighbors: anxiety (future), dread (scheduled), alarm (signal), startle (reflex), horror (witnessed), nervousness (mild/social).",
        "Fright is startle plus lingering appraisal; fear versus anxiety is present versus future tense.",
        "Opposites: calm, safety, courage, confidence — destinations, not enemies.",
        "Courage is fear's answer, not its absence.",
        "You reach calm through the far side of fear, not by deleting it.",
        "When a feeling is hard to name, check the neighbors.",
    ],
    "requirements": [
        "The emotion-family record as the map's legend",
        "Three of your own feelings to place on the map",
    ],
    "standards": [
        "Wheel of emotions: neighboring and opposite emotions (Plutchik)",
        "Time and self-involvement dimensions of threat emotions",
        "Basic-emotions framework (Ekman)",
    ],
    "citations": [
        "Plutchik, R. Emotions and Life. APA; 2003.",
        "Ekman, P. Emotions Revealed. 2nd ed. Holt; 2007.",
        "Lazarus, R. S. Emotion and Adaptation. Oxford University Press; 1991.",
    ],
    "sig_lens": (
        "Through the Signature lens, the emotion map is the territory chart every "
        "Signature reader carries — fear's streets, its neighbors' houses, the far "
        "roads to calm and courage. The Signature method navigates by this chart: "
        "name the street you are on, note the neighboring streets, and walk toward "
        "the destination deliberately. No one wanders the map by accident twice."
    ),
},
{
    "key": "fear-blends",
    "name": "Fear in Blends: Dyads With Other Emotions",
    "group": "Emotion Mixes and Simulation",
    "ladder_rank": 10,
    "ladder_tier": "advanced",
    "description": (
        "Pure fear is rare in the wild — most of the time it arrives blended, and the "
        "blends have their own weather. Fear plus anger gives defensive aggression: "
        "the cornered feeling, hot and electric, the urge to strike out at the very "
        "thing you want to flee. It looks like shaking fists and a pounding heart, "
        "and it needs sequencing — handle the danger first, the grievance second. "
        "Fear plus sadness gives despair: the heavy, sinking blend where the threat "
        "feels both terrible and unfixable. The body goes low-energy — the alarm "
        "ringing in a tired building — and what helps is one small handleable piece, "
        "not the whole mountain. Fear plus surprise gives shock: the blank, wide-eyed "
        "moment after sudden bad news, when the mind has not caught up to the ears. "
        "Shock needs time and simple repetition, not decisions. Fear plus disgust "
        "gives revulsion-with-alarm: the recoil from something threatening AND "
        "repellent — the snarling animal, the contaminated wound — with a strong urge "
        "to get away and stay away. Fear plus joy gives thrill: the roller coaster, "
        "the horror movie, the scary story told among friends — fear's arousal "
        "re-labeled as delight because the mind knows it is safe. Thrill is the "
        "proof that fear's machinery is morally neutral: the same pounding heart "
        "that means terror in an alley means delight on a coaster — context writes "
        "the meaning. Learning the blends does two things: it explains feelings that "
        "seemed contradictory (\"why am I furious AND terrified?\"), and it prescribes "
        "better: each blend has its own handling, and the wrong remedy for the blend "
        "— treating despair like simple fear, or shock like stubbornness — misses the "
        "mark. Name the ingredients, and the recipe tells you what to do."
    ),
    "how_it_works": (
        "Blends form because the brain runs appraisals in parallel: a situation can "
        "simultaneously register as threatening (fear), goal-blocking or unfair "
        "(anger), loss-laden (sadness), unexpected (surprise), or contaminating "
        "(disgust). The shared arousal pool means the blends feel unified even "
        "though their action urges differ — which is why blends feel confusing until "
        "unmixed. Thrill demonstrates reappraisal directly: identical physiology, "
        "different interpretation, different feeling. Unmixing by labeling lets each "
        "component's remedy be applied in sequence."
    ),
    "key_points": [
        "Fear plus anger: defensive aggression — sequence it, danger first.",
        "Fear plus sadness: despair — offer one small handleable piece.",
        "Fear plus surprise: shock — give time and simple repetition, not decisions.",
        "Fear plus disgust: revulsion-with-alarm — strong urge to get and stay away.",
        "Fear plus joy: thrill — same machinery, safe context, delight.",
        "Name the ingredients; the recipe tells you what to do.",
    ],
    "requirements": [
        "The fear-anger blend record as the worked example",
        "Two of your own blended feelings to unmix",
    ],
    "standards": [
        "Wheel of emotions: dyads (Plutchik)",
        "Parallel appraisal and shared arousal",
        "Reappraisal: same physiology, different meaning",
    ],
    "citations": [
        "Plutchik, R. Emotions and Life. APA; 2003.",
        "Schachter, S., and Singer, J. Psychological Review; 1962.",
        "Lazarus, R. S. Emotion and Adaptation. Oxford University Press; 1991.",
    ],
    "sig_lens": (
        "Through the Signature lens, blends are compound signals — two instruments "
        "on one wire — and the Signature reader is trained to split them. Fear-anger, "
        "fear-sorrow, fear-delight: each compound gets separated into its tones, "
        "each tone answered in its turn. In the Signature method, a mixed signal is "
        "never answered mixed; precision in, precision out."
    ),
},
{
    "key": "fear-simulation",
    "name": "Fear From Trigger to Resolution: A Full Behavioral Simulation",
    "group": "Emotion Mixes and Simulation",
    "ladder_rank": 10,
    "ladder_tier": "advanced",
    "description": (
        "This is the showcase: the whole ladder in one walkthrough. The scene — a "
        "power outage on a stormy night, home alone. Scene one, trigger: the lights "
        "die with a pop, the hum of the house stops, and for half a second there is "
        "only the rain hammering the windows. Your breath catches. Inner voice: "
        "\"what was that?\" Body: heart gives a hard thump, shoulders jump. Face: "
        "brows lift, eyes widen at the dark. You freeze — the oldest move — listening. "
        "Scene two, rise: a crash from downstairs — a branch against the window, "
        "probably, but probably is doing no work right now. The cascade starts: "
        "memory (the news story), imagination (someone downstairs), body feedback "
        "(heart hammering now — this must be serious). You back toward the wall, "
        "phone in hand, feet light. Your voice, when you whisper \"hello?\", comes "
        "out half an octave high. Scene three, peak: another bang, closer-sounding, "
        "and the wave crests — shaking hands, mouth dry, thoughts narrowed to a "
        "single bright thread: check or hide. The urge screams hide; the thinking "
        "mind, barely audible, says check with the phone flashlight from the stairs. "
        "Scene four, turning: you name it — \"I am afraid, and I am going to check "
        "one room at a time\" — and the naming itself loosens something. Slow exhale. "
        "Stairs creak under your feet; you clear the living room (branch shadow "
        "dancing on the glass — there is the culprit), the kitchen, the hall. Each "
        "cleared room is a link broken. Scene five, easing: nothing. No one. Just "
        "storm. The laugh comes out shaky and surprised. Shoulders drop two inches. "
        "You text a friend: \"power's out, storm's wild, I'm a little spooked\" — "
        "spoken fear shrinks. The friend texts back; co-regulation over the wire. "
        "Scene six, afterglow: candles lit, blanket fort on the couch, rain still "
        "hammering but reclassified as weather, not threat. Hands still tremble "
        "slightly when you lift the mug — the aftershock, the engine cooling. You "
        "notice the log your body kept: trigger, rise, peak, turning, easing, "
        "afterglow — the whole arc in forty minutes. And the quiet lesson underneath: "
        "the alarm rang, you read it, you answered it, and here you are — blanket, "
        "candlelight, storm demoted to soundtrack. That is the full simulation: not "
        "fear defeated, but fear completed."
    ),
    "how_it_works": (
        "The showcase works by chaining every mechanism in the ladder: fast threat "
        "detection (trigger), the cascade loop (rise), full mobilization (peak), "
        "labeling plus graded approach (turning), disconfirming evidence (easing), "
        "and residual arousal decay (afterglow). Each scene demonstrates a record "
        "from the database in action — body signals, face, voice, behavior, support, "
        "healthy expression — so the simulation doubles as a review of the whole "
        "archive. Walking it in imagination builds the familiarity that steadies "
        "real alarms."
    ),
    "key_points": [
        "Six scenes: trigger, rise, peak, turning, easing, afterglow.",
        "The cascade runs (memory, imagination, body feedback) — then gets broken link by link.",
        "Naming plus graded checking turns the peak.",
        "Clearing rooms is disconfirming evidence — the alarm stands down.",
        "Speaking the fear and receiving reply is co-regulation in action.",
        "The lesson: not fear defeated, but fear completed.",
    ],
    "requirements": [
        "The whole ladder behind you — this is the graduation walk",
        "A safe quiet half hour to walk it slowly",
    ],
    "standards": [
        "Full threat-response arc: detection through recovery",
        "Cascade interruption and reappraisal",
        "Co-regulation and stress-cycle completion",
    ],
    "citations": [
        "LeDoux, J. The Emotional Brain. Simon & Schuster; 1996.",
        "Lazarus, R. S. Emotion and Adaptation. Oxford University Press; 1991.",
        "Ekman, P. Emotions Revealed. 2nd ed. Holt; 2007.",
        "Cannon, W. B. Bodily Changes in Pain, Hunger, Fear and Rage. Appleton; 1915.",
    ],
    "sig_lens": (
        "Through the Signature lens, this simulation is the full drill run in "
        "daylight — every instrument sounded, every protocol executed, the log "
        "closed with a steady hand. The Signature reader walks the whole building "
        "floor by floor: alarm heard, cascade mapped, links broken, rooms cleared, "
        "fear spoken, calm restored. In the Signature method, the completed drill "
        "is the credential — the operator has proven, to himself, that the system "
        "works."
    ),
},
]
