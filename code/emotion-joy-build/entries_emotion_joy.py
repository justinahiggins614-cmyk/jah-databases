#!/usr/bin/env python3
"""Entries for the Joy Emotion databases (Manon's 16:15 orders, emotion series batch 1).

Creates two NEW databases, 34 ladder-ordered records each:

  emotion-joy            - The Joy Emotion Database
                           (public-harvest: real, fact-checked psychology of
                           joy - definition, family placement, intensity,
                           first-person simulation, body signals, facial
                           expression, triggers, behavior, healthy expression,
                           recognition in others, related emotions and mixes,
                           and a full behavioral simulation; descriptive and
                           educational only - never diagnosing real people;
                           standard references Ekman and Friesen FACS 1978;
                           Ekman basic emotions 1999; Plutchik 1980; Russell
                           circumplex 1980; Lazarus 1991; Frijda 1986;
                           Scherer 2005; Barrett 2017; Fredrickson 1998;
                           Izard 1992; Darwin 1872; APA Dictionary of
                           Psychology)
  emotion-joy-signature  - The Joy Emotion Signature Database
                           (his original Signature Joy Method: joy as the
                           home signal of the system - the covenant kept, the
                           build complete, the lit panel that says the engine
                           runs; gratitude the ground wire, play the cooling
                           fan, celebration the output display; src
                           signature, titles suffixed " (Signature Edition)",
                           never presented as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
non-decreasing; ladder_tier foundations/compounded/advanced); the shard
index is written in ladder order so pages present simple -> compounded ->
complex.

ID prefixes: JAH-EMJO- (public) and JAH-EMJOS- (signature), verified free
in the manifest (zero EMJO hits across 2,442 databases) and in every shard
index file (853 index files, zero JAH-EMJO hits); JAH-EM- is an existing
unrelated prefix but shares no substring collision with JAH-EMJO- since
"JAH-EMJO-..." does not start with "JAH-EM-".

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_emotion_joy.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos. Demo outputs are
cross-checked against entry text during authoring.

Descriptive/educational only: this database describes and simulates the
emotion of joy. It never diagnoses real people, never labels any real
person with an emotional state, and offers only general, safe, everyday
guidance. No clinical language, no diagnostic labels.

Never the words "bat belt" anywhere. No website references. No Facebook.
No religious talk.
"""

SIG_TAIL = ("Signature original - his original Signature Joy Method: joy as "
            "the home signal of the system - the covenant kept, the build "
            "complete, the lit panel that says the engine runs; gratitude "
            "the ground wire, play the cooling fan, celebration the output "
            "display. Clearly labeled Signature-made, never presented as "
            "authentic public record.")

CIT_DARWIN = ("Darwin C. The Expression of the Emotions in Man and Animals. "
              "London: John Murray; 1872.")
CIT_FACS = ("Ekman P, Friesen WV. Facial Action Coding System: A Technique "
            "for the Measurement of Facial Movement. Palo Alto: Consulting "
            "Psychologists Press; 1978.")
CIT_EKMAN1999 = ("Ekman P. Basic emotions. In: Dalgleish T, Power MJ, eds. "
                 "Handbook of Cognition and Emotion. Chichester: Wiley; "
                 "1999:45-60.")
CIT_PLUTCHIK = ("Plutchik R. Emotion: A Psychoevolutionary Synthesis. New "
                "York: Harper and Row; 1980.")
CIT_RUSSELL = ("Russell JA. A circumplex model of affect. J Pers Soc Psychol. "
               "1980;39(6):1161-1178.")
CIT_LAZARUS = ("Lazarus RS. Emotion and Adaptation. New York: Oxford "
               "University Press; 1991.")
CIT_FRIJDA = ("Frijda NH. The Emotions. Cambridge: Cambridge University "
              "Press; 1986.")
CIT_SCHERER = ("Scherer KR. What are emotions? And how can they be measured? "
               "Soc Sci Inf. 2005;44(4):695-729.")
CIT_BARRETT = ("Barrett LF. How Emotions Are Made: The Secret Life of the "
               "Brain. Boston: Houghton Mifflin Harcourt; 2017.")
CIT_FREDRICKSON = ("Fredrickson BL. What good are positive emotions? Rev Gen "
                   "Psychol. 1998;2(3):300-319.")
CIT_IZARD = ("Izard CE. Basic emotions, relations among emotions, and "
             "emotion-cognition relations: a review of the evidence. Psychol "
             "Rev. 1992;99(3):561-565.")
CIT_APA = ("American Psychological Association. APA Dictionary of Psychology. "
           "Joy entry: a feeling of great pleasure or happiness. Washington "
           "DC: APA.")

SIG_LENS_DEF = ("The Signature read: joy is the home signal of the system. "
                "Where public psychology charts the feeling, the Signature "
                "Joy Method treats joy as the lit panel on the engine - "
                "proof the covenant is kept and the build runs true. "
                "Gratitude is the ground wire, play the cooling fan, "
                "celebration the output display. Every joy record below "
                "carries the same public facts, reframed as his original "
                "Signature engineering of the feeling.")

ENTRIES = [
    # ------------------------------------------------ 1-4 WHAT JOY IS
    {
        "key": "definition",
        "name": "What Joy Is: A Plain-Language Definition",
        "group": "What the Emotion Is",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Joy is the feeling of gladness that arrives when something good "
            "happens - a success, a reunion, a surprise gone right, a small "
            "pleasure landing exactly where it was needed. In plain words, "
            "joy is the inner yes: the body and mind agreeing at once that "
            "things are good. Psychologists count joy among the basic "
            "emotions, which means it shows up across cultures with a "
            "recognizable face, a recognizable body state, and a "
            "recognizable set of causes. It is not the same as calm "
            "contentment or quiet satisfaction, though they are cousins: joy "
            "has energy in it. There is lift. A contented person sits "
            "peacefully with what is; a joyful person wants to move, to "
            "share, to mark the moment somehow. Joy can be about the big "
            "things - a birth, a win, a return - and about the small ones, "
            "like the first warm day or a message from an old friend. Size "
            "does not define it; the yes does. Everyone has felt it, and "
            "everyone will feel it again, because joy is part of the "
            "standard equipment of being human. This database describes the "
            "emotion from every angle - what it is, how it feels, how it "
            "shows, and how it can be expressed well - purely as education "
            "and description. It never diagnoses anyone and never labels "
            "any real person."
        ),
        "how_it_works": (
            "Joy works as an appraisal signal. The mind is constantly, "
            "mostly unconsciously, evaluating events against what matters: "
            "is this good for me and mine, did something I wanted come "
            "true, did an obstacle lift? When the appraisal comes back "
            "positive - a goal reached, a person welcomed back, an "
            "unexpected gift - the brain flags the event as worth repeating "
            "and worth sharing, and joy is the felt form of that flag. That "
            "is why joy tends to make people approach, repeat, and share: "
            "the feeling is the system's way of stamping the moment with "
            "\"do more of this.\" It is fast: the appraisal can happen in a "
            "fraction of a second, before any deliberate thought. And it is "
            "social by design: humans evolved to signal joy outward so "
            "others can share and amplify it, which is why joyful moments "
            "grow when they are told, shown, or celebrated together."
        ),
        "key_points": [
            "Joy is the felt inner yes when something good happens: the body and mind agreeing at once that things are good.",
            "It is a basic emotion - recognizable across cultures in face, body, and cause.",
            "Joy has energy in it: unlike quiet contentment, it moves people to act, share, and celebrate.",
            "Size does not define it: a birth and a warm first day can both be real joy.",
            "Joy is an appraisal signal - the mind stamping an event as good, worth repeating, and worth sharing.",
        ],
        "requirements": [
            "A plain-language definition that an ordinary reader recognizes from their own life.",
            "Clear separation from neighboring states like contentment, satisfaction, and pleasure.",
            "Coverage of both big and small joys so the definition does not only fit milestones.",
            "The signal function stated: what joy marks, what it motivates, what it is for.",
            "A stated educational boundary: description only, never diagnosis of any real person.",
        ],
        "standards": [
            "Definitions follow the APA Dictionary of Psychology joy entry: a feeling of great pleasure or happiness.",
            "Basic-emotion framing follows Ekman 1999: distinct, cross-culturally recognized, with characteristic signals.",
            "Appraisal account follows Lazarus 1991: emotions as signals of events appraised as relevant to goals and well-being.",
        ],
        "citations": [CIT_APA, CIT_EKMAN1999, CIT_LAZARUS],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "family",
        "name": "Where Joy Sits in the Emotion Family",
        "group": "What the Emotion Is",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Emotions are organized by psychologists the way colors are "
            "organized on a wheel: some are primaries, some are blends, and "
            "each sits at a fixed address with fixed neighbors. Joy is one "
            "of the primaries - a basic emotion, not a blend. On Plutchik's "
            "wheel of emotions, joy sits opposite sadness, with serenity as "
            "its milder sibling and ecstasy as its fiercer one. Its nearest "
            "neighbors are anticipation (which leans into joy when good "
            "news is coming) and trust (which joy tends to build toward "
            "others). On Russell's circumplex, joy lives in the high "
            "pleasantness, high energy quadrant - pleasant and activated, "
            "the opposite corner from depressed or sluggish. This placement "
            "is practical knowledge: it tells you what joy turns into when "
            "it cools (contentment, serenity), what it becomes when it "
            "heats (ecstasy, exuberance), and which emotions it blends with "
            "most easily (anticipation makes optimism; trust makes love in "
            "Plutchik's blends). Knowing the address also helps tell close "
            "cousins apart: joy and happiness-as-trait are different things "
            "- joy is the momentary surge, while a happy person is someone "
            "for whom the surge comes often and the baseline sits high."
        ),
        "how_it_works": (
            "The family placement works because emotions are not isolated "
            "flashes but positions in a space. The circumplex model gives "
            "that space two axes: pleasantness (valence) from unpleasant to "
            "pleasant, and energy (arousal) from sleepy to activated. Every "
            "feeling has coordinates. Joy's coordinates - pleasant and "
            "activated - explain its behavior: pleasantness draws people "
            "toward the cause, activation supplies the energy to act on it. "
            "Plutchik's wheel adds the blend logic: primary emotions sit at "
            "fixed compass points, neighbors blend into dyads, and "
            "opposites explain why joy and sadness can cancel or alternate. "
            "The intensity ring on the wheel explains the mild-to-intense "
            "ladder: the same emotion, written at different font sizes. "
            "Modern constructionist accounts like Barrett's add a "
            "refinement - that the brain assembles the emotion from body "
            "signals, past experience, and concepts - but the map itself "
            "still holds as a description of where joy lives."
        ),
        "key_points": [
            "Joy is a primary, basic emotion - not a blend of other emotions.",
            "On Plutchik's wheel joy sits opposite sadness, with serenity (mild) and ecstasy (intense) as its intensity siblings.",
            "On the circumplex joy is pleasant plus activated: high pleasantness, high energy.",
            "Its nearest neighbors - anticipation and trust - are its most natural blending partners.",
            "Joy is the momentary surge; a happy person is someone whose baseline sits high and whose surges come often.",
        ],
        "requirements": [
            "Placement on Plutchik's wheel: joy opposite sadness, neighbors anticipation and trust, intensity ring serenity to ecstasy.",
            "Placement on Russell's circumplex: pleasant-and-activated quadrant with the two axes named.",
            "The distinction between the momentary emotion (joy) and the trait (happiness) stated plainly.",
            "Blend logic explained: how neighbors combine into named dyads.",
            "Acknowledgment of constructionist refinement without dropping the classic map.",
        ],
        "standards": [
            "Wheel placement follows Plutchik 1980: joy opposite sadness, adjacent to anticipation and trust.",
            "Quadrant placement follows Russell 1980: valence by arousal coordinates for joy as pleasant-activated.",
            "Constructionist refinement follows Barrett 2017: emotions constructed from interoception, experience, and concepts.",
        ],
        "citations": [CIT_PLUTCHIK, CIT_RUSSELL, CIT_BARRETT],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "intensity",
        "name": "Joy at Every Volume: Mild to Intense",
        "group": "What the Emotion Is",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Joy is not one fixed loudness; it is a whole dial. At low "
            "volume it is a warm hum - a smile that comes and goes, a "
            "lightness in the chest, the quiet thought that this is nice. "
            "Psychologists sometimes call the mild end serenity or gladness: "
            "the pleasure is real but the energy is modest, and the outside "
            "world may see nothing at all. At middle volume it is bright "
            "and unmistakable: laughing out loud, wanting to tell someone, "
            "the feeling spilling into the voice and the walk. At full "
            "volume it is exuberance or ecstasy: jumping, shouting, hugging "
            "whoever is near, the body unable to sit still, the feeling so "
            "large it temporarily crowds out everything else. The same "
            "emotion runs through all three - a mild joy and an ecstatic "
            "one are family, not strangers. What changes with volume is "
            "mostly energy and expressiveness: pleasantness is high at "
            "every setting, but activation climbs. Knowing the dial matters "
            "because people live at different settings on different days, "
            "and because a mild joy is not a failed joy - it is the most "
            "common kind there is, and it counts in full."
        ),
        "how_it_works": (
            "Intensity works through activation, the arousal axis of the "
            "circumplex. The pleasantness of joy - the goodness - can be "
            "fully present while activation varies widely, which is why the "
            "same trigger can produce a quiet smile in one person and a "
            "shout in another, or a quiet smile in the same person on a "
            "tired day and a shout on a rested one. Physiologically, "
            "intensity tracks with sympathetic arousal: heart rate, breath "
            "rate, and muscle readiness climb as the volume climbs, up to a "
            "ceiling where the system is saturated and the feeling plateaus. "
            "Expression intensity tracks arousal but is also filtered by "
            "display rules - the cultural and personal norms about how much "
            "feeling may show - so felt intensity and shown intensity are "
            "two dials, not one. Appraisal explains the setting: the bigger "
            "the perceived gain, the more surprising it is, and the more "
            "central it is to the person's goals, the higher the volume."
        ),
        "key_points": [
            "Joy is a dial, not a switch: mild (serenity/gladness), middle (bright joy), and intense (exuberance/ecstasy) are the same emotion at different volumes.",
            "Pleasantness stays high at every setting; what changes is energy and expressiveness.",
            "Felt intensity and shown intensity are two dials: display rules can mute or amplify what others see.",
            "A mild joy is not a failed joy - it is the most common kind and counts in full.",
            "Volume tracks perceived gain, surprise, and goal-relevance of the triggering event.",
        ],
        "requirements": [
            "Three named volume bands with the lived character of each.",
            "The mild-end vocabulary (serenity, gladness) and intense-end vocabulary (exuberance, ecstasy) both stated.",
            "The two-dial model: felt intensity vs shown intensity, mediated by display rules.",
            "The appraisal drivers of intensity: gain size, surprise, goal relevance.",
            "Validation of mild joy as fully real, not a lesser or broken form.",
        ],
        "standards": [
            "Intensity levels follow Plutchik 1980: serenity to ecstasy as the mild-to-intense ring for joy.",
            "Arousal framing follows Russell 1980: intensity variation as movement along the arousal axis.",
            "Display rules follow Ekman's account of cultural modulation of emotional expression.",
        ],
        "citations": [CIT_PLUTCHIK, CIT_RUSSELL, CIT_EKMAN1999],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "myths",
        "name": "Myths and Misunderstandings About Joy",
        "group": "What the Emotion Is",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Joy collects myths the way attics collect boxes, and the myths "
            "do real damage because they teach people to mistrust a "
            "feeling that is trying to help them. Myth one: joy must be "
            "earned by big achievements. In truth some of the most reliable "
            "joys are small and unearned - a song, a flavor, a message. "
            "Myth two: feeling joy when others are suffering is wrong. In "
            "truth emotions are not zero-sum; a person can grieve and still "
            "feel a genuine lift at good news, and the lift is not "
            "disloyalty. Myth three: joy means everything is fine. In truth "
            "joy is a momentary signal, not a weather report for the whole "
            "life; it can flash during hard seasons and that is normal. "
            "Myth four: chasing joy directly is the path to it. In truth "
            "joy is mostly a byproduct - it arrives while people are "
            "absorbed in people, work, or play they care about, and direct "
            "pursuit often strangely repels it. Myth five: some people are "
            "just not wired for joy. In truth the capacity is universal; "
            "what differs is access, habit, and circumstance, and all three "
            "can shift. Myth six: joy is shallow compared to the serious "
            "emotions. In truth joy does serious work - it builds bonds, "
            "broadens thinking, and repairs stress. This record exists so "
            "the reader can spot these myths in the wild and set them "
            "down. The database as a whole stays descriptive and "
            "educational; nothing here diagnoses anyone or prescribes "
            "treatment."
        ),
        "how_it_works": (
            "Myths about joy work by installing false rules in the "
            "appraisal system. If a person believes joy must be earned, the "
            "appraisal quietly disqualifies small good events before they "
            "can register, and the person feels less joy without ever "
            "noticing the disqualification. If a person believes joy during "
            "hard times is disloyal, guilt gets scheduled to arrive "
            "immediately after every lift, which trains the system to "
            "suppress the lift. The direct-pursuit myth works differently: "
            "monitoring one's own happiness as a target creates a constant "
            "comparison between the target and the moment, and the gap "
            "itself becomes the dominant feeling. Research on positive "
            "emotion consistently finds the byproduct pattern - joy arrives "
            "as the side effect of engagement, connection, and meaning - "
            "which is why the myths that reframe it as a prize, a betrayal, "
            "or a shallow luxury all reliably reduce it. Debunking works "
            "the same way in reverse: naming the false rule lets the "
            "appraisal system stop enforcing it."
        ),
        "key_points": [
            "Joy does not need to be earned by big achievements: small, unearned joys are real and reliable.",
            "Feeling joy during others' suffering is not disloyalty: emotions are not zero-sum.",
            "Joy is a momentary signal, not a verdict on the whole life: it can flash during hard seasons.",
            "Joy is mostly a byproduct of engagement, connection, and meaning - direct pursuit often repels it.",
            "The capacity for joy is universal; what differs is access, habit, and circumstance, and all three can shift.",
        ],
        "requirements": [
            "At least five named myths with a plain refutation for each.",
            "The appraisal mechanism by which each myth reduces joy, stated in non-technical language.",
            "The byproduct finding: joy as the side effect of engagement, connection, and meaning.",
            "The zero-sum fallacy named and rejected for joy alongside grief or hardship.",
            "Educational boundary restated: description only, no diagnosis, no treatment advice.",
        ],
        "standards": [
            "Byproduct pattern follows Fredrickson 1998: positive emotions arising from engagement and broadening resources.",
            "Appraisal interference follows Lazarus 1991: beliefs and commitments shaping emotional appraisal.",
            "The broaden-and-build framing for joy's serious function follows Fredrickson 1998.",
        ],
        "citations": [CIT_FREDRICKSON, CIT_LAZARUS, CIT_BARRETT],
        "sig_lens": SIG_LENS_DEF,
    },
    # ------------------------------------------------ 5-9 HOW IT FEELS
    {
        "key": "first_person",
        "name": "Inside Joy: A First-Person Passage",
        "group": "How It Feels",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "From the inside, joy feels like this. It starts as a small "
            "catch - a breath that stops halfway because something good just "
            "landed - and then warmth spreads outward from the center of "
            "the chest like tea poured into cold hands. There is a lightness "
            "that is almost physical, as if gravity turned itself down a "
            "notch; walking feels springier, shoulders sit higher without "
            "being told to. Thoughts speed up but in a bright direction: "
            "ideas about what to do next, who to tell, how to stretch this "
            "moment a little longer. Time does something odd - it either "
            "slows so the moment can be savored, or it flies because "
            "everything is moving at once. There is an urge to share it, "
            "almost a pressure: joy kept entirely to oneself feels like a "
            "song sung to an empty room, still good but unfinished. The "
            "face does things on its own - the mouth curves, the eyes "
            "narrow in the particular way that only real gladness makes. And "
            "underneath it all there is a quiet, almost surprised gratitude: "
            "this happened, and it happened to me, and for right now the "
            "world and I are on the same side. This passage is a "
            "simulation - a described example of what the feeling is like - "
            "written for education, not a claim about any real person's "
            "inner life."
        ),
        "how_it_works": (
            "The first-person texture of joy comes from several channels "
            "firing at once. The catch in the breath and the chest warmth "
            "are the autonomic nervous system shifting: a quick orienting "
            "response followed by a parasympathetic-leaning ease once the "
            "event is appraised as good. The lightness and springiness are "
            "muscular: positive affect lowers the sense of effort and "
            "raises movement readiness, so the same walk literally costs "
            "less perceived energy. The bright fast thoughts are the "
            "broaden effect: positive emotion widens the scope of attention "
            "and the menu of action ideas, which the person experiences as "
            "the mind opening up. The urge to share is the social channel: "
            "joy evolved partly as a broadcast signal, and the felt pressure "
            "to tell someone is the subjective side of that broadcasting "
            "instinct. The face moving on its own reflects how practiced "
            "the expression is - the neural path from feeling to smile is "
            "short and well-worn."
        ),
        "key_points": [
            "Inside, joy begins with a catch of breath and warmth spreading from the chest outward.",
            "There is a physical lightness: movement feels easier, shoulders rise, walking gets springier.",
            "Thoughts speed up in a bright direction: ideas, plans, who to tell, how to stretch the moment.",
            "Joy carries a pressure to share it: kept entirely inside it feels like a song sung to an empty room.",
            "The passage is a described simulation for education, not a claim about any real person's inner life.",
        ],
        "requirements": [
            "A sustained first-person passage, present tense, covering body, thought, time, and social urge.",
            "The chest-warmth and lightness rendered as concrete physical sensations.",
            "The broaden effect rendered as lived thought, not as a theory name.",
            "The share-urge rendered as felt pressure with the empty-room image.",
            "The simulation disclaimer: described example for education, not a diagnosis of anyone.",
        ],
        "standards": [
            "The broaden effect described follows Fredrickson 1998: positive emotion broadening attention and action repertoires.",
            "Autonomic and motor descriptions follow Frijda 1986: action readiness and bodily patterning of emotion.",
            "Appraisal-to-feeling sequence follows Scherer 2005: stimulus evaluation checks producing the felt change.",
        ],
        "citations": [CIT_FREDRICKSON, CIT_FRIJDA, CIT_SCHERER],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "time_course",
        "name": "The Time Course of Joy: Onset, Peak, and Fade",
        "group": "How It Feels",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "Joy has a shape in time, and knowing the shape keeps people "
            "from misreading it. The onset is fast - sometimes instant. Good "
            "news lands, the appraisal fires, and within seconds the feeling "
            "is there; surprise-joys can arrive before the person has "
            "finished processing what happened. The peak follows quickly "
            "after: this is the brightest minute, when the feeling is "
            "largest and most physical, the part people remember and "
            "describe. Peaks are short by design - the nervous system cannot "
            "hold maximum activation indefinitely, and even the best news "
            "stops being news. Then comes the fade, which is gradual and "
            "usually pleasant: the bright peak settles into a warm glow, "
            "then into a background sense that things are good, which can "
            "last hours or be rekindled by remembering. The aftershock is "
            "the interesting part: a single joyful event can send small "
            "echoes for days - retelling the story, catching oneself "
            "smiling, the memory reliably re-warming the feeling. None of "
            "this means joy is unreliable; it means joy is honest about "
            "being a signal. Signals are supposed to rise and fall. "
            "Expecting the peak to last forever is the fastest way to turn a "
            "good memory into a disappointment."
        ),
        "how_it_works": (
            "The time course works because joy is an event-locked signal "
            "riding on arousal, and arousal is expensive. The fast onset "
            "reflects the speed of affective appraisal - the brain's "
            "relevance check runs before conscious deliberation, so the "
            "feeling can lead the understanding. The short peak reflects "
            "both neural limits (sustained maximum activation is "
            "metabolically costly) and informational logic: once the good "
            "event is fully registered, the signal has done its job and "
            "there is no reason to keep shouting. The pleasant fade "
            "reflects the shift from high-arousal joy toward lower-arousal "
            "positive states like contentment, which are cheaper to sustain. "
            "Aftershocks work through memory: each recall re-runs a weaker "
            "version of the original appraisal, producing a weaker but real "
            "echo of the feeling, which is why savoring and retelling "
            "extend joy's life. Hedonic adaptation - the fading of response "
            "to a repeated stimulus - is the same mechanism viewed over "
            "weeks: the appraisal system recalibrates, and yesterday's "
            "peak becomes today's baseline."
        ),
        "key_points": [
            "Joy's time course: fast onset, short bright peak, gradual pleasant fade, and echoing aftershocks.",
            "The peak is short by design: arousal is expensive and the signal has done its job once the news registers.",
            "The fade is not a failure: joy settles into contentment, which is cheaper for the body to sustain.",
            "Aftershocks are real: memory re-runs the appraisal, so retelling and savoring extend joy's life.",
            "Expecting the peak to last forever turns a good memory into a disappointment.",
        ],
        "requirements": [
            "Four named phases: onset, peak, fade, aftershock, each with its lived character.",
            "The fast onset explained via pre-conscious appraisal speed.",
            "The short peak explained via arousal cost and signal logic.",
            "The pleasant fade framed as a transition to contentment, not a loss.",
            "Aftershocks explained via memory re-appraisal; savoring and retelling named as extenders.",
        ],
        "standards": [
            "Appraisal speed and sequence follow Scherer 2005: sequential evaluation checks with rapid early relevance detection.",
            "Arousal-cost framing follows Frijda 1986: emotion as action readiness with physiological regulation limits.",
            "Adaptation dynamics follow the standard hedonic treadmill account in the positive-emotion literature.",
        ],
        "citations": [CIT_SCHERER, CIT_FRIJDA, CIT_FREDRICKSON],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "low_vs_high",
        "name": "Low Joy and High Joy: Two Lived Snapshots",
        "group": "How It Feels",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "Low joy, first. It is a Tuesday evening and the light through "
            "the window is the exact color of honey. Nothing has happened, "
            "exactly - dinner is simple, the house is quiet - but there is a "
            "small warm coin of gladness sitting in the chest, and every so "
            "often it turns over and catches the light. The body is still; "
            "the face is mostly neutral, but the mouth keeps threatening to "
            "curve. Thoughts are unhurried: this is nice, I am glad about "
            "this small thing, I do not need anything else right now. It "
            "could be mistaken for nothing at all, and that is its "
            "superpower: it asks for nothing, disturbs nothing, and still "
            "the evening is better for it. Now high joy. The news comes "
            "through the phone - the thing hoped for, the thing half given "
            "up on, is real - and the body stands up before being asked. "
            "There is a sound, half laugh and half something else, and the "
            "hands do not know where to go. The chest feels too small for "
            "what is in it. The next hour is a blur of telling people, "
            "re-reading the message, laughing at nothing, the feeling "
            "sloshing over the edges of every ordinary task. Same emotion. "
            "Different weather. The low one is a candle; the high one is a "
            "bonfire; both give light, and neither is the wrong size."
        ),
        "how_it_works": (
            "The two snapshots work because intensity scales the same "
            "mechanism. At low intensity, the appraisal registers a small "
            "good - pleasantness high, arousal low - so the body barely "
            "moves, the face barely shows, and the main effect is a "
            "background tint on attention: the world looks slightly better "
            "and slightly more worth engaging. At high intensity, the "
            "appraisal registers a large, often surprising good - "
            "pleasantness high, arousal high - so the sympathetic system "
            "floods the body with readiness, expression runs unfiltered, "
            "and attention narrows onto the cause and the sharing of it. "
            "The candle and the bonfire differ in arousal, expressiveness, "
            "and duration - low joy can hum for hours, high joy peaks and "
            "must fade - but they share the appraisal core: this is good, "
            "this matters, do more of this. Display rules shape which one "
            "others see more than which one is felt."
        ),
        "key_points": [
            "Low joy is a candle: quiet, steady, a warm coin of gladness that asks for nothing and improves the evening.",
            "High joy is a bonfire: loud, physical, the body standing before being asked, the hour a blur of sharing.",
            "Same mechanism at different arousal: pleasantness high in both, energy low in one and high in the other.",
            "Low joy can hum for hours; high joy peaks and must fade - different durations are normal.",
            "Neither is the wrong size: the candle is not a failed bonfire.",
        ],
        "requirements": [
            "Two concrete present-tense snapshots, one low and one high, with sensory detail.",
            "The candle/bonfire image carried through as the structural metaphor.",
            "The shared appraisal core named beneath the difference.",
            "Duration difference stated: low hums long, high peaks short.",
            "Display rules noted as shaping what is seen more than what is felt.",
        ],
        "standards": [
            "Intensity scaling follows Plutchik 1980: serenity-to-ecstasy as one emotion at different volumes.",
            "Arousal differentiation follows Russell 1980: shared valence, varying activation.",
            "Action-readiness scaling follows Frijda 1986.",
        ],
        "citations": [CIT_PLUTCHIK, CIT_RUSSELL, CIT_FRIJDA],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "joy_relief_blend",
        "name": "Joy Mixed with Relief: The Most Common Pairing",
        "group": "How It Feels",
        "ladder_rank": 5,
        "ladder_tier": "foundations",
        "description": (
            "Joy rarely travels alone, and its most frequent companion is "
            "relief. The pairing has a logic: relief is the feeling of a "
            "threat lifting, and a lifted threat is itself good news, so "
            "the two appraisals often fire together - the exam is passed, "
            "the test result is clear, the loved one is safe. From the "
            "inside, joy-with-relief has a distinctive two-layer texture. "
            "The bottom layer is the exhale: shoulders dropping, breath "
            "deepening, the body standing down from a readiness it had been "
            "holding, sometimes for weeks. The top layer is the lift: the "
            "gladness, the smile, the urge to celebrate. Together they make "
            "a feeling people describe as the best kind of tired - the "
            "exhaustion of the ordeal plus the brightness of the outcome, "
            "held at once. It is why good news after a scare feels "
            "different from good news out of the blue: the relief "
            "contributes its own flavor, a kind of earned lightness, and "
            "the joy rides on top of it. The blend also explains a common "
            "puzzle - why people sometimes cry at happy endings. The "
            "release of long-held tension and the surge of gladness arrive "
            "together, and the body, given two strong signals at once, "
            "sometimes answers with tears that belong to both."
        ),
        "how_it_works": (
            "The blend works because the two appraisals share a timeline. "
            "Relief's appraisal is \"a danger or burden has passed\"; joy's "
            "is \"something good has happened.\" When the passing of the "
            "burden IS the good thing, both fire on the same event, and "
            "the feeling system sums them. Physiologically the sequence is "
            "visible: the threat period holds the body in sympathetic "
            "readiness (tension, vigilance), the resolution triggers a "
            "parasympathetic rebound (the exhale, the dropping shoulders), "
            "and the joy appraisal adds its own activation on top - so the "
            "body is simultaneously standing down and lighting up, which is "
            "exactly the \"best kind of tired\" texture. On the circumplex, "
            "relief sits pleasant but lower-arousal than joy; the blend "
            "lands between them, which is why joy-with-relief feels "
            "warmer and less frantic than pure surprise-joy. The tears at "
            "happy endings reflect overflow: two appraisals, one body, and "
            "the lacrimal response serving as a general release valve."
        ),
        "key_points": [
            "Relief is joy's most common companion: the lifting of a threat is itself good news, so both appraisals fire together.",
            "The blend has two layers: the exhale of released tension underneath, the lift of gladness on top.",
            "It produces the best kind of tired: ordeal-exhaustion held together with outcome-brightness.",
            "Good news after a scare feels different from good news out of the blue - relief adds an earned lightness.",
            "Tears at happy endings are the blend's signature: release plus gladness arriving in one body at once.",
        ],
        "requirements": [
            "The pairing named as the most common, with the shared-timeline logic.",
            "The two-layer texture described in felt, physical terms.",
            "The best-kind-of-tired image stated.",
            "The scare-then-news vs out-of-the-blue distinction drawn.",
            "Tears at happy endings explained as the blend's overflow signature.",
        ],
        "standards": [
            "Blend logic follows Plutchik 1980: adjacent and co-occurring emotions forming dyads.",
            "Appraisal pairing follows Lazarus 1991: relief as the passing of threat appraised against goals.",
            "Rebound physiology follows the standard autonomic account in Frijda 1986.",
        ],
        "citations": [CIT_PLUTCHIK, CIT_LAZARUS, CIT_FRIJDA],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "day_vignette",
        "name": "A Day with Joy: An Ordinary Day Vignette",
        "group": "How It Feels",
        "ladder_rank": 5,
        "ladder_tier": "foundations",
        "description": (
            "Morning: the alarm is not yet an enemy because the day holds "
            "something looked-forward-to - a friend visiting at noon - and "
            "the anticipation has already tinted everything slightly gold. "
            "Coffee tastes better than it has any right to; the walk to the "
            "shop has a bounce in it that was not there yesterday. Midday: "
            "the friend arrives, and the greeting is louder than planned, "
            "both talking at once, the particular laughter that only old "
            "friends can produce on demand. Lunch stretches; nobody checks "
            "the time; the food is unremarkable and somehow perfect. "
            "Afternoon: a small surprise - a message with good news about a "
            "project - and the day's gladness gets a second wind, brighter "
            "and more physical this time, a grin that keeps reappearing "
            "uninvited. Errands that would normally drag feel easy; the "
            "cashier's small talk lands as genuine warmth. Evening: "
            "tiredness arrives but it is the good kind, the day well spent, "
            "and there is a quiet inventory-taking - replaying the best "
            "moments, already telling the story in the head for later. "
            "Night: falling asleep is easy, and the last thought is simple "
            "gladness that the day happened. Nothing extraordinary occurred. "
            "That is the point of the vignette: joy does not require "
            "extraordinary days. It requires attention, company, small "
            "goodnesses noticed, and the willingness to let a good day be "
            "a good day. This is a described simulation for education, not "
            "a claim about any real person's life."
        ),
        "how_it_works": (
            "The vignette works because joy accumulates. Anticipation in "
            "the morning pre-tints appraisal: the same coffee, the same "
            "walk, evaluated by a mind already leaning pleasant, registers "
            "as better - this is affect coloring perception, the mood "
            "setting the baseline for the next appraisal. The midday peak "
            "works through shared joy: social laughter and mutual "
            "attention amplify the signal, each person's expression "
            "re-appraised by the other as more evidence of goodness, in a "
            "feedback loop. The afternoon second wind works through "
            "surprise plus success: the unexpected good news re-fires the "
            "appraisal at higher arousal. The evening inventory works "
            "through savoring: deliberate replay re-runs the appraisals at "
            "low intensity and banks the day as evidence that life "
            "contains such days, which raises tomorrow's baseline "
            "slightly. The whole day is an ordinary demonstration of the "
            "broaden-and-build cycle: good moments, noticed and shared, "
            "build the resources - bonds, memories, resilience - that make "
            "the next good moments more likely."
        ),
        "key_points": [
            "Morning anticipation pre-tints the day: a mind leaning pleasant appraises the same coffee as better.",
            "Midday shared joy amplifies in a loop: each person's laughter becomes the other's evidence of goodness.",
            "An afternoon surprise gives the day a second wind: unexpected good news re-fires the appraisal brighter.",
            "Evening inventory banks the day: replaying the best moments extends joy and raises tomorrow's baseline.",
            "The point of the vignette: joy needs attention, company, and noticed small goodnesses - not extraordinary days.",
        ],
        "requirements": [
            "A full day arc: morning, midday, afternoon, evening, night, each with its joy mechanism.",
            "Anticipation tinting, social amplification, surprise second-wind, and savoring inventory each named.",
            "The broaden-and-build cycle named as the day's underlying engine.",
            "The thesis stated plainly: ordinary days can carry joy; attention and company are the requirements.",
            "Simulation disclaimer: described example for education, not a claim about any real person.",
        ],
        "standards": [
            "Affect-coloring-perception follows the mood-congruence literature consistent with Lazarus 1991.",
            "Social amplification follows the shared-positive-affect account in Fredrickson 1998.",
            "Savoring mechanics follow the positive-emotion regulation literature.",
        ],
        "citations": [CIT_LAZARUS, CIT_FREDRICKSON, CIT_BARRETT],
        "sig_lens": SIG_LENS_DEF,
    },
]

ENTRIES += [
    # ------------------------------------------------ 10-13 BODY SIGNALS
    {
        "key": "body",
        "name": "What Joy Does in the Body",
        "group": "Body Signals",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Joy is not only a mental event; it is a full-body event, and "
            "the body keeps its own ledger. The heart typically quickens a "
            "little - not the hammering of fear, but a brightened tempo, "
            "as if the circulation has somewhere pleasant to be. Breathing "
            "deepens and often quickens slightly; many people notice a "
            "catch or a laugh riding on the exhale. Muscles do something "
            "distinctive: the big muscles of the face, shoulders, and "
            "limbs take on a readiness that reads as lightness - tension "
            "drops in the jaw and neck while energy rises in the legs, "
            "which is why joyful people bounce, pace, or cannot sit still. "
            "The stomach is usually quiet during joy; nausea and knotting "
            "belong to the alarm emotions, and their absence is part of "
            "what makes joy feel safe in the body. The skin warms - "
            "flushing of the cheeks is common - and people often report a "
            "spreading warmth from the chest outward. Energy is the "
            "headline: joy is one of the few emotions that reliably leaves "
            "people feeling more energized than before it arrived, the "
            "opposite of emotions that drain. None of this is identical in "
            "everyone, and none of it is required for the feeling to be "
            "real - but this is the standard pattern the research "
            "describes, and most people will recognize their own version "
            "of it."
        ),
        "how_it_works": (
            "The body pattern works because joy mobilizes without "
            "alarming. The sympathetic branch of the autonomic nervous "
            "system raises heart rate and breath rate - the readiness part "
            "- while the appraisal of safety and goodness keeps the "
            "threat branch quiet, so there is activation without the "
            "stomach-knotting and vigilance of fear or anger. The muscle "
            "lightness comes from reduced defensive tension combined with "
            "increased motor readiness: the body is prepared to approach, "
            "celebrate, and share, which are approach behaviors, and "
            "approach runs on a different muscular setting than defense. "
            "The warmth and flushing are vasodilation - blood moving toward "
            "the skin and the face, part of the broadcast system that "
            "makes joy visible to others. The energy surplus is partly "
            "real (arousal mobilizes glucose) and partly perceived "
            "(positive affect lowers the sense of effort), and both "
            "contribute to the well-documented finding that joyful people "
            "report feeling more capable of action."
        ),
        "key_points": [
            "The heart quickens brightly: a lifted tempo, not the hammering of alarm emotions.",
            "Breathing deepens and may catch or carry a laugh; the jaw and neck release tension while the legs gain energy.",
            "The stomach stays quiet: the absence of knotting and nausea is part of what makes joy feel safe in the body.",
            "Skin warms and cheeks flush: vasodilation moves blood to the face as part of joy's broadcast system.",
            "Energy is the headline: joy reliably leaves people feeling more energized than before it arrived.",
        ],
        "requirements": [
            "Coverage of heart, breath, muscles, stomach, skin, and energy - the full six-channel ledger.",
            "The mobilize-without-alarm distinction: sympathetic readiness with the threat branch quiet.",
            "The lightness explained as reduced defensive tension plus increased approach readiness.",
            "Flushing and warmth tied to the broadcast function of the expression.",
            "The energy surplus split into real (glucose mobilization) and perceived (lowered effort sense) parts.",
        ],
        "standards": [
            "Autonomic patterning follows Frijda 1986: emotion-specific bodily patterning with action readiness.",
            "Approach-vs-defense motor settings follow the standard affective neuroscience account.",
            "Effort-sense effects follow the positive-affect and perceived-exertion literature.",
        ],
        "citations": [CIT_FRIJDA, CIT_SCHERER, CIT_FREDRICKSON],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "posture",
        "name": "The Posture and Movement of Joy",
        "group": "Body Signals",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Joy has a silhouette. The classic joyful posture is expanded: "
            "chest open, shoulders back and down rather than hunched, chin "
            "slightly lifted, arms more likely to be out or up than "
            "crossed and guarded. It is the physical opposite of the "
            "collapsed, protected postures of sadness or shame - joy takes "
            "up space because it has nothing to defend. Movement under joy "
            "gets bigger and faster: steps lengthen, gestures widen, the "
            "whole body seems to be operating at a slightly higher frame "
            "rate. There are also the signature movements that cultures "
            "everywhere recognize: the jump, the fist pump, the spin, the "
            "arms-thrown-wide, the impromptu dance step in the kitchen. "
            "These are not taught; children do them before anyone "
            "demonstrates them, which suggests they are wired in rather "
            "than learned. At low intensity the signature is subtler - a "
            "straighter sit, a springier step, hands that gesture a little "
            "more - but the direction is the same: outward, upward, open. "
            "Actors and animators have known this forever: to play joy you "
            "do not just smile, you uncurl. The posture is part of the "
            "feeling, not just its advertisement."
        ),
        "how_it_works": (
            "The posture works through the approach system. Emotions that "
            "involve approaching something good expand the body: opening "
            "the chest and lifting the chin literally orient the sensory "
            "organs toward the world and signal to others that approach is "
            "safe. Emotions that involve withdrawing or defending collapse "
            "the body to protect the vitals. Joy, being the purest "
            "approach emotion, produces the purest expansion - which is why "
            "the posture reads so clearly even in silhouette. The bigger, "
            "faster movements come from the arousal component: activation "
            "raises motor readiness across the board, and with no threat to "
            "aim the energy at, it discharges as celebratory movement. The "
            "universality of the jump and the arms-wide suggests these are "
            "not cultural inventions but motor programs tied to the "
            "emotion itself - the body celebrating in its native language. "
            "And the loop runs both ways: deliberately uncurling the "
            "posture can nudge the feeling, because the brain reads the "
            "body's state as evidence about the emotion."
        ),
        "key_points": [
            "Joy's silhouette is expanded: open chest, back-and-down shoulders, lifted chin, arms out or up.",
            "It is the physical opposite of the collapsed postures of sadness or shame: joy takes up space because it has nothing to defend.",
            "Movement gets bigger and faster under joy: longer steps, wider gestures, a higher frame rate.",
            "Signature moves - the jump, fist pump, spin, arms-wide, kitchen dance step - appear untrained in children.",
            "The loop runs both ways: uncurling the posture can nudge the feeling, because the brain reads the body as evidence.",
        ],
        "requirements": [
            "The expanded posture described part by part: chest, shoulders, chin, arms.",
            "The approach-vs-defense contrast with collapsed postures of sadness and shame.",
            "Movement changes: scale and tempo, with concrete examples.",
            "Signature celebratory movements named, with the untrained-in-children universality point.",
            "The bidirectional loop: posture as part of the feeling, not just its advertisement.",
        ],
        "standards": [
            "Approach-expansion account follows the embodiment literature consistent with Frijda 1986 action readiness.",
            "Universality of celebratory motor programs follows Darwin 1872 on expression.",
            "Bidirectional body-to-feeling effects follow the facial-feedback and embodiment research tradition.",
        ],
        "citations": [CIT_DARWIN, CIT_FRIJDA, CIT_BARRETT],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "sleep_appetite",
        "name": "Joy, Sleep, Appetite, and Energy",
        "group": "Body Signals",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Joy rearranges the body's maintenance schedule in mostly "
            "pleasant ways. Sleep: mild and moderate joy are compatible "
            "with good sleep, and a good day often ends in easy, deep "
            "rest - the system standing down satisfied. Intense joy is a "
            "different story: the arousal that makes the peak so bright "
            "also makes sleep elusive that night, and people report lying "
            "awake replaying the day with a grin, too lit up to power "
            "down. This is normal and self-correcting; the arousal spends "
            "itself. Appetite: joy tends to restore or sharpen appetite "
            "rather than kill it - celebratory eating is nearly universal, "
            "and food genuinely tastes better in a good mood, because "
            "pleasant affect heightens the perceived reward of flavors. "
            "Energy: as noted in the body record, joy is energizing; the "
            "day after a joyful event people often report unusual stamina "
            "for ordinary tasks, the aftershock working as fuel. The "
            "practical upshot is simple: ordinary joy needs no management, "
            "intense joy may cost a night of sleep and repay it in energy, "
            "and celebratory appetite is one of the body's oldest ways of "
            "marking that something good happened. None of this is medical "
            "advice - it is a description of the standard pattern, and "
            "persistent sleep or appetite changes belong in a conversation "
            "with a professional, not a database."
        ),
        "how_it_works": (
            "The maintenance effects work through arousal and reward. "
            "Sleep onset requires arousal to fall below a threshold; "
            "intense joy holds arousal above that threshold through "
            "replay and rumination-on-the-good, which is why the bright "
            "day becomes the bright night. Mild joy, with low arousal, "
            "does not block the threshold and may even ease the "
            "transition, since the absence of worry removes the usual "
            "barrier. Appetite effects work through the reward system: "
            "dopamine-linked pleasant affect raises the hedonic value of "
            "food, so flavors register as more rewarding and the "
            "motivation to eat rises - the same mechanism that makes "
            "everything taste better on vacation. The energy aftershock "
            "works through the broaden-and-build residue: positive affect "
            "leaves behind broadened attention and a sense of resource, "
            "which the person experiences as stamina. All three effects "
            "are self-limiting in ordinary joy, which is why no "
            "intervention is needed for the standard pattern."
        ),
        "key_points": [
            "Mild and moderate joy are compatible with good sleep; a good day often ends in easy, deep rest.",
            "Intense joy can cost a night of sleep: replay keeps arousal above the sleep threshold - normal and self-correcting.",
            "Joy restores or sharpens appetite: food genuinely tastes better in a good mood through heightened reward.",
            "The day after a joyful event often brings unusual stamina: the aftershock works as fuel.",
            "Persistent sleep or appetite changes belong with a professional, not a database - this record describes the standard pattern only.",
        ],
        "requirements": [
            "Sleep effects split by intensity: mild compatible, intense disruptive-but-normal.",
            "Appetite effects: restoration and sharpening, celebratory eating, flavor enhancement mechanism.",
            "Energy aftershock: next-day stamina as broaden-and-build residue.",
            "The self-limiting nature of all three effects in ordinary joy.",
            "The professional-referral boundary for persistent changes, stated plainly.",
        ],
        "standards": [
            "Arousal-sleep threshold account follows standard sleep physiology.",
            "Reward-hedonic effects follow the positive-affect and reward literature consistent with Fredrickson 1998.",
            "Resource-residue framing follows Fredrickson 1998 broaden-and-build.",
        ],
        "citations": [CIT_FREDRICKSON, CIT_FRIJDA, CIT_SCHERER],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "individual_diff",
        "name": "Why Joy Feels Different in Every Body",
        "group": "Body Signals",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The standard pattern is real, but no two bodies read it "
            "identically - and the differences are not defects. Some "
            "people feel joy primarily in the chest, a warmth and "
            "expansion; others feel it first in the face, the smile "
            "arriving before the feeling has a name; others feel it as "
            "restlessness in the limbs, a need to move. Some people run "
            "hot: their joy is loud, physical, tearful at the edges. "
            "Others run cool: their joy is a quiet brightening, visible "
            "only to those who know them well, but no less real for being "
            "unbroadcast. Temperament sets the baseline - some nervous "
            "systems amplify, some dampen. Culture sets the display rules "
            "but also seeps inward: people raised where exuberance is "
            "prized may genuinely feel the peaks higher, because the "
            "permission to feel is part of the feeling. Personal history "
            "matters too: someone whose joys were punished or interrupted "
            "may feel a flinch of wariness inside the gladness, a learned "
            "brake on the signal. Age matters: children's joy is "
            "whole-body and immediate, adults' joy more often layered with "
            "meaning and memory. The takeaway is practical and kind: there "
            "is no correct way for joy to feel in the body. The quiet "
            "person's candle and the loud person's bonfire are the same "
            "emotion in different instruments, and both instruments are "
            "playing it right. This record describes variation; it does "
            "not sort people into types or diagnose anyone."
        ),
        "how_it_works": (
            "Individual differences work through three stacked layers. The "
            "bottom layer is constitution: nervous-system gain - how "
            "strongly a given appraisal drives autonomic and motor "
            "output - varies between people the way height varies, partly "
            "inherited, largely stable. The middle layer is learning: the "
            "brain builds its emotion concepts from past instances, so a "
            "person whose joys were celebrated builds a bigger, brighter "
            "joy concept that fires more readily, while a person whose "
            "joys were interrupted builds a concept with a brake in it. "
            "The top layer is context: display rules, current fatigue, "
            "even posture and setting modulate how much of the signal "
            "reaches awareness. Barrett's construction account captures "
            "this neatly: the brain constructs each emotional instance "
            "from body signals plus past experience plus the current "
            "situation, so the same nominal emotion is literally assembled "
            "differently in different people. The standard pattern "
            "describes the center of the distribution; the variation "
            "describes its honest width."
        ),
        "key_points": [
            "Joy's address in the body varies: chest-warmth people, face-first people, limb-restlessness people.",
            "Some run hot (loud, physical, tearful-edged) and some run cool (quiet brightening) - both are the real emotion.",
            "Three layers stack: constitutional nervous-system gain, learned emotion concepts, and immediate context.",
            "History can install a brake: joys that were punished or interrupted may carry a flinch of wariness.",
            "There is no correct way for joy to feel in the body: same emotion, different instruments, all playing it right.",
        ],
        "requirements": [
            "At least three body-address variants named with felt detail.",
            "The hot/cool temperamental axis stated without ranking either above the other.",
            "The three-layer model: constitution, learning, context.",
            "The learned-brake mechanism for interrupted joys.",
            "Explicit anti-typing boundary: describes variation, does not sort or diagnose people.",
        ],
        "standards": [
            "Construction of individual instances follows Barrett 2017: body signals plus experience plus situation.",
            "Learned emotion concepts follow Barrett 2017.",
            "Display-rule modulation follows the Ekman tradition.",
        ],
        "citations": [CIT_BARRETT, CIT_EKMAN1999, CIT_FRIJDA],
        "sig_lens": SIG_LENS_DEF,
    },
    # ------------------------------------------------ 14-17 FACIAL EXPRESSION
    {
        "key": "face",
        "name": "The Face of Joy: Eyes, Brows, Mouth",
        "group": "Facial Expression",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "The joyful face is one of the most recognized sights in "
            "human life, and it has a precise anatomy. The mouth is the "
            "headline: the corners pull up and back, the lips part, and "
            "in full joy the teeth show - this is Action Unit 12 in the "
            "Facial Action Coding System, the zygomatic major at work. "
            "But the mouth alone does not make a genuine joy face. The "
            "eyes are the tell: the muscle around the eyes (orbicularis "
            "oculi, Action Unit 6) contracts, crinkling the outer corners "
            "into the famous crow's feet and pushing the cheeks upward. "
            "This eye involvement is what separates the Duchenne smile - "
            "named for the 19th-century researcher Duchenne de Boulogne, "
            "who mapped it with electrical stimulation - from the social "
            "smile, which moves the mouth but leaves the eyes out of it. "
            "The brows are mostly quiet in joy, perhaps lifting slightly; "
            "there is no furrow, no press. The whole face seems to lift: "
            "cheeks rise, the skin under the eyes bunches softly, and the "
            "face widens. Micro-signs complete the picture: a brief "
            "brightening of the eyes just before the smile, a quick "
            "upward glance, the head tilting very slightly. Newborns "
            "smile in their sleep; blind children smile without ever "
            "seeing one - the face of joy is wired in, not taught."
        ),
        "how_it_works": (
            "The face works as joy's broadcast tower because the relevant "
            "muscles are hard to fake and easy to read at a distance. AU12 "
            "(zygomatic major) is under relatively voluntary control, which "
            "is why the mouth can smile on command. AU6 (orbicularis oculi, "
            "pars orbitalis) is much less voluntary - most people cannot "
            "contract it deliberately - which is why the eyes are the "
            "honesty marker: genuine positive affect recruits it "
            "automatically, deliberate posing usually does not. The "
            "combination is the Duchenne marker, and observers across "
            "cultures read it as authentic gladness within fractions of a "
            "second. The upward cheek push and eye crinkle also serve a "
            "mechanical function in intense joy: they narrow the eye "
            "opening slightly, which is part of the same protective "
            "squint seen in the eye region during strong positive affect. "
            "That the pattern appears in blind children and sleeping "
            "newborns indicates the motor program is innate, with culture "
            "adding only the display rules about when it may show."
        ),
        "key_points": [
            "The mouth (AU12, zygomatic major): corners pull up and back, lips part, teeth may show.",
            "The eyes are the tell (AU6, orbicularis oculi): outer corners crinkle, cheeks push upward.",
            "The Duchenne smile - mouth plus eyes - is the genuine-joy marker; the mouth-only smile is the social one.",
            "Brows stay quiet in joy: perhaps a slight lift, never a furrow.",
            "The pattern is wired in: blind children and sleeping newborns smile without ever seeing one.",
        ],
        "requirements": [
            "AU12 and AU6 named with their muscles and visible effects.",
            "The Duchenne vs social smile distinction with the voluntariness explanation.",
            "Brows, cheeks, and eye-region described as parts of the whole-face lift.",
            "Micro-signs named: pre-smile eye brightening, upward glance, slight head tilt.",
            "Innateness evidence: blind children, newborn sleep smiles.",
        ],
        "standards": [
            "Action-unit anatomy follows Ekman and Friesen 1978 (FACS).",
            "Duchenne marker account follows the Ekman tradition on genuine vs deliberate smiles.",
            "Innateness evidence follows Darwin 1872 and the blindness studies in the Ekman tradition.",
        ],
        "citations": [CIT_FACS, CIT_EKMAN1999, CIT_DARWIN],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "face_intensity",
        "name": "How the Joyful Face Changes with Intensity",
        "group": "Facial Expression",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "The joyful face is not one fixed mask; it scales with the "
            "feeling. At low intensity the face barely moves: the mouth "
            "corners lift a few millimeters, the eyes gain a soft "
            "brightness, and a stranger might miss it entirely - but "
            "someone who knows the person catches it instantly. This is "
            "the face of the warm coin of gladness: present, real, and "
            "quiet. At middle intensity the full Duchenne assembly comes "
            "online: AU12 pulls the mouth into a clear smile, AU6 crinkles "
            "the eyes, cheeks rise, and the face is unmistakably joyful to "
            "anyone in the room. At high intensity the face overflows its "
            "borders: the mouth opens wide in laughter, the eyes squeeze "
            "nearly shut, the whole head may tip back, and the neck and "
            "shoulders join in - the expression stops being a face and "
            "becomes a whole upper body. There is also a time dimension: "
            "low-intensity joy can sit on the face for minutes as a "
            "resting brightness, while the high-intensity version flashes "
            "and releases in seconds, often in waves with laughter. "
            "Readers use these gradations constantly without thinking: "
            "everyone can tell the difference between a polite lift of "
            "the mouth, a genuine smile, and helpless laughter, because "
            "the face is a volume knob and humans are fluent in reading "
            "its settings."
        ),
        "how_it_works": (
            "The scaling works because facial muscle recruitment follows "
            "arousal. Low arousal recruits only the most practiced, "
            "lowest-threshold movement - the slight AU12 lift - because "
            "the motor drive is weak. Rising arousal recruits AU6 and the "
            "cheek raisers as the genuine-affect pathway engages more "
            "strongly; the two action units scale together in authentic "
            "joy, which is why the eye crinkle deepens in step with the "
            "mouth. At peak arousal the drive overflows the face: the jaw "
            "opens for laughter (a respiratory-vocal event, not just a "
            "facial one), the eyes squeeze as the orbicularis contracts "
            "hard, and head and torso movements join because the motor "
            "activation has exceeded what the face alone can discharge. "
            "The time course follows the same logic: low drive sustains a "
            "steady low-level contraction for minutes, while peak drive "
            "discharges in rhythmic bursts - laughter's waves - because "
            "maximum contraction cannot be held. Observers read the "
            "gradation through configural processing: the whole pattern "
            "at once, matched against a lifetime of exemplars."
        ),
        "key_points": [
            "Low joy: millimeters of mouth lift plus eye brightness - caught instantly by those who know the person, missed by strangers.",
            "Middle joy: the full Duchenne assembly - AU12 plus AU6 plus rising cheeks, unmistakable across the room.",
            "High joy: the face overflows - wide laughter, squeezed eyes, tipped head, the upper body joining in.",
            "Duration scales inversely with intensity: low joy can rest on the face for minutes, peak joy flashes in waves.",
            "Humans read the gradations fluently: polite lift, genuine smile, and helpless laughter are instantly distinct.",
        ],
        "requirements": [
            "Three intensity bands with the specific muscle recruitment of each.",
            "The AU12/AU6 co-scaling in authentic joy stated.",
            "The overflow mechanism at peak: laughter as respiratory-vocal, head and torso joining.",
            "The duration rule: low sustains, peak discharges in waves.",
            "Observer fluency noted: the face as a volume knob humans read without training.",
        ],
        "standards": [
            "Action-unit scaling follows Ekman and Friesen 1978 (FACS intensity scoring).",
            "Configural face reading follows the standard face-perception literature.",
            "Laughter as a respiratory-vocal event follows the standard affective science account.",
        ],
        "citations": [CIT_FACS, CIT_EKMAN1999, CIT_DARWIN],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "hiding_faking",
        "name": "Hiding or Faking Joy: What Leaks Through",
        "group": "Facial Expression",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "People hide joy and fake joy for ordinary reasons: hiding it "
            "to stay professional during good news in a serious meeting, "
            "or to spare someone who just got bad news; faking it to be "
            "polite at a gift opening, or to reassure someone who needs "
            "to see a smile. Both are performances, and both leak. When "
            "joy is hidden, the leaks are small rebellions of the face: "
            "the mouth corners twitch upward and get pressed back down, "
            "the eyes brighten for a fraction of a second before the "
            "neutral mask returns, the cheeks lift almost invisibly. The "
            "body leaks too: a bounce in the step on the way out of the "
            "room, humming under the breath. Suppression has a cost - "
            "holding the face still while the feeling surges is effortful, "
            "and the effort itself can show as stiffness. When joy is "
            "faked, the leak is the missing piece: the mouth smiles but "
            "the eyes stay out of it, the timing is slightly off (the "
            "smile arrives too fast or lingers too long), and the rest of "
            "the face and body do not join in. Observers are surprisingly "
            "good at catching both: humans evolved reading these signals "
            "because the difference between real and performed gladness "
            "mattered for trust. None of this is a lie-detector manual - "
            "it is a description of how the signal system behaves under "
            "load, for education only."
        ),
        "how_it_works": (
            "Leakage works because the genuine-joy pathway and the "
            "voluntary pathway are different circuits. Genuine joy drives "
            "the face through the older, less voluntary route that "
            "recruits AU6 automatically; deliberate smiling drives the "
            "face through the cortical voluntary route that reaches AU12 "
            "easily but AU6 poorly. So hidden joy leaks through the "
            "involuntary route in microbursts - the feeling fires the "
            "muscles before the suppression command, issued a fraction "
            "later, can cancel them - producing the twitch-and-press "
            "pattern. Faked joy fails through the same asymmetry in "
            "reverse: the voluntary route cannot convincingly recruit "
            "AU6, so the eyes stay flat while the mouth performs. Timing "
            "leaks because genuine expressions have a characteristic "
            "onset-apex-offset envelope (smooth rise, brief hold, smooth "
            "release) that is hard to imitate deliberately; posed smiles "
            "tend to snap on, hold too long, and snap off. The "
            "suppression cost is real: inhibiting a strong motor drive "
            "consumes executive resources, which is why suppressed joy "
            "often shows as generalized stiffness."
        ),
        "key_points": [
            "Hidden joy leaks as micro-rebellions: twitching mouth corners pressed back down, a fraction-of-a-second eye brightening.",
            "The body leaks hidden joy too: the bounce in the step, humming under the breath, after the mask is on.",
            "Suppression is effortful: holding the face still during a surge shows as stiffness - the cost of the performance.",
            "Faked joy leaks through absence: the mouth smiles while the eyes stay flat, timing snaps on and off.",
            "Humans are good at catching both because reading real vs performed gladness mattered for trust.",
        ],
        "requirements": [
            "Ordinary motives for hiding and faking stated without judgment.",
            "Hidden-joy leaks: facial microbursts plus bodily leaks, with the twitch-and-press pattern.",
            "Faked-joy leaks: the AU6 absence, timing envelope errors, unjoined face and body.",
            "The two-circuit explanation: involuntary genuine route vs voluntary deliberate route.",
            "The suppression-cost point and the educational-only boundary (not a lie-detector manual).",
        ],
        "standards": [
            "Two-route account follows the Ekman tradition on voluntary vs involuntary facial control.",
            "Microexpression timing follows the standard microexpression literature.",
            "Suppression costs follow the emotion-regulation literature.",
        ],
        "citations": [CIT_FACS, CIT_EKMAN1999, CIT_BARRETT],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "expression_gallery",
        "name": "Drawing Joy: Notes for the Artist or Actor",
        "group": "Facial Expression",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "For the artist with a pencil or the actor with a mirror, joy "
            "is a technical problem with known solutions. Start with the "
            "mouth: draw the corners lifted and pulled slightly back, the "
            "upper lip raised a touch, the lower lip relaxed; in full joy "
            "part the lips and show the upper teeth, but keep the jaw "
            "easy - a clenched jaw reads as effort, not gladness. Then "
            "the eyes, which make or break it: narrow the eye opening "
            "slightly from below, push the lower lids up, add the "
            "crow's-feet lines radiating from the outer corners - three "
            "short strokes suggest them - and lift the cheeks so the "
            "skin under the eyes bunches softly. Without the eye work "
            "the face reads polite; with it, it reads glad. Brows: keep "
            "them neutral or lifted a breath, never drawn together - a "
            "furrow kills joy instantly in a drawing. The whole face "
            "tilts toward lift: think of the features as drawn slightly "
            "upward at the outer edges, the way a balloon string pulls. "
            "For the actor: the face follows the body, so uncurl first - "
            "open the chest, lift the sternum, let the breath drop - and "
            "the smile that arrives will recruit the eyes on its own. "
            "Think of something genuinely funny for one beat before the "
            "scene; the remembered gladness puts the real assembly on "
            "the face, and the camera, like the human eye, knows the "
            "difference. For low joy, do less: soften the eyes, let the "
            "mouth rest a millimeter from smiling, and let the stillness "
            "carry it. These are craft notes for depicting the emotion, "
            "not claims about any real person's face."
        ),
        "how_it_works": (
            "The craft notes work because depiction runs the recognition "
            "system in reverse. Viewers read faces configurally - the "
            "whole pattern at once - so the artist must supply the full "
            "Duchenne configuration, not just the mouth, or the "
            "viewer's pattern-matcher files it under politeness. The "
            "crow's-feet strokes work as a visual shorthand: a few lines "
            "at the outer eye corners are enough to trigger the "
            "genuine-joy template in the viewer's mind. The actor's "
            "body-first instruction works through the bidirectional "
            "loop: opening the posture and deepening the breath shift "
            "the autonomic state toward the genuine-joy pattern, and the "
            "face follows the state more honestly than it follows direct "
            "muscle commands - trying to pose AU6 directly usually "
            "fails, while recalling a funny memory recruits it "
            "automatically. The low-joy instruction (do less, let "
            "stillness carry it) works because observers are exquisitely "
            "sensitive to small deviations from neutral in a familiar "
            "face; a millimeter of lift on a still face reads louder "
            "than a broad grin on an already animated one."
        ),
        "key_points": [
            "Draw the mouth lifted and slightly back, upper teeth in full joy, jaw easy - a clenched jaw reads as effort, not gladness.",
            "The eyes make or break it: narrowed from below, lower lids up, crow's-feet strokes, cheeks lifting the under-eye skin.",
            "Brows stay neutral or breathe upward; a furrow kills joy instantly in a drawing.",
            "For the actor: uncurl the body first - open chest, lifted sternum, dropped breath - and the eyes join the smile on their own.",
            "For low joy, do less: softened eyes and a millimeter-from-smiling mouth on a still face reads louder than a broad grin.",
        ],
        "requirements": [
            "Mouth construction notes: corners, lips, teeth, jaw.",
            "Eye construction notes: narrowing, lower lids, crow's-feet shorthand, cheek lift.",
            "The brow rule and the furrow-kills-joy warning.",
            "Actor's body-first method with the memory-recall trick for AU6.",
            "Low-joy minimalism: stillness carrying the signal.",
        ],
        "standards": [
            "Configuration notes follow Ekman and Friesen 1978 (FACS).",
            "Viewer pattern-matching follows the configural face-perception literature.",
            "Body-first acting method follows the embodiment and facial-feedback traditions.",
        ],
        "citations": [CIT_FACS, CIT_DARWIN, CIT_EKMAN1999],
        "sig_lens": SIG_LENS_DEF,
    },
]

ENTRIES += [
    # ------------------------------------------------ 18-21 TRIGGERS
    {
        "key": "classic_triggers",
        "name": "The Classic Triggers of Joy",
        "group": "Triggers",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "Certain triggers set off joy so reliably that they are "
            "practically part of the emotion's definition. Achievement: "
            "finishing something hard, passing, winning, being chosen - "
            "the goal-reached appraisal in its purest form. Reunion: "
            "seeing a loved person after absence, the embrace at the "
            "airport, the friend at the door - belonging restored. Good "
            "news: the clear test result, the accepted offer, the phone "
            "call that changes things - uncertainty resolving in your "
            "favor. Surprise pleasures: the unexpected gift, the "
            "compliment from nowhere, the perfect weather on the day it "
            "matters - goodness that was not budgeted for hits harder. "
            "Play and humor: laughter with others, games, the joke that "
            "lands - joy as the native climate of play. Beauty and "
            "wonder: music that lifts the chest, a view that stops the "
            "walk, art that rearranges something inside - the world "
            "being briefly, overwhelmingly good. Giving and kindness: "
            "making someone else's day, the thank-you that lands - "
            "generosity reliably produces the giver's glow. Sensory "
            "pleasures: the first bite, the warm sun, the good smell - "
            "the body reporting that the world is good at the most basic "
            "level. These are the classics because they map directly "
            "onto the appraisal: something I wanted came true, someone I "
            "love is here, the world is good. Knowing the list is useful "
            "because it is also a menu: a person arranging more of these "
            "into life is arranging more joy, not by chasing the feeling "
            "but by planting its causes."
        ),
        "how_it_works": (
            "Classic triggers work because each one is a clean hit on the "
            "joy appraisal: goal attainment, belonging restoration, "
            "favorable uncertainty resolution, unexpected gain, social "
            "play, aesthetic reward, prosocial efficacy, sensory pleasure. "
            "The appraisal system is essentially a relevance detector, and "
            "these eight are the canonical relevance patterns - they recur "
            "across cultures because the underlying concerns (goals, "
            "bonds, safety, resources, beauty, generosity, the senses) "
            "recur across cultures. Surprise amplifies because the "
            "appraisal weights unexpected gains more heavily - the "
            "prediction-error bonus. Social triggers amplify because joy "
            "is a broadcast emotion: shared gladness gets re-appraised "
            "by each participant as further evidence of goodness, in a "
            "loop. The menu function works because triggers are causes, "
            "not correlates: arranging reunions, play, beauty, and "
            "kindness into life reliably increases the appraisal's hit "
            "rate, which is the byproduct path to joy rather than the "
            "direct-pursuit path that so often fails."
        ),
        "key_points": [
            "The eight classics: achievement, reunion, good news, surprise pleasures, play and humor, beauty and wonder, giving and kindness, sensory pleasures.",
            "Each is a clean hit on the joy appraisal: a goal reached, belonging restored, uncertainty resolved in your favor.",
            "Surprise amplifies: goodness that was not budgeted for hits harder through the prediction-error bonus.",
            "Social triggers amplify in a loop: shared gladness becomes further evidence of goodness for everyone present.",
            "The list is a menu: plant the causes - reunions, play, beauty, kindness - and joy follows as a byproduct.",
        ],
        "requirements": [
            "Eight named trigger families with a concrete example for each.",
            "Each family tied to its appraisal pattern (goal, belonging, uncertainty, gain, play, beauty, generosity, senses).",
            "The surprise-amplification mechanism named.",
            "The social-amplification loop named.",
            "The menu framing: causes planted vs feeling chased.",
        ],
        "standards": [
            "Appraisal patterns follow Lazarus 1991: goal relevance, congruence, and ego-involvement.",
            "Universality of trigger families follows the cross-cultural emotion literature in the Ekman tradition.",
            "Byproduct path follows Fredrickson 1998.",
        ],
        "citations": [CIT_LAZARUS, CIT_EKMAN1999, CIT_FREDRICKSON],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "personal_triggers",
        "name": "Personal Triggers: Memories and Private Associations",
        "group": "Triggers",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "Beyond the classics, every person carries a private trigger "
            "map - associations no one else would predict. A particular "
            "song from a particular summer. The smell of a specific "
            "kitchen. A street corner, a brand of tea, the first cold "
            "morning of the year, a phrase a grandparent used to say. "
            "These triggers work through memory: the stimulus reopens a "
            "stored joyful episode, and the feeling arrives with the "
            "memory, sometimes stronger than the original moment because "
            "memory has had years to polish it. Anniversaries are the "
            "calendar version: the date itself becomes the trigger, and "
            "the gladness arrives on schedule whether or not anything "
            "new happens. Personal triggers are powerful precisely "
            "because they are private: nobody can schedule them for you, "
            "and nobody can take them away by argument. They are also "
            "fragile in one way - overuse can wear them smooth, the way a "
            "favorite song played on repeat stops lifting. The practical "
            "wisdom is to notice your own map and tend it: keep the "
            "associations, revisit them deliberately rather than "
            "constantly, and let anniversaries do their annual work. A "
            "person who knows their own triggers owns a renewable source "
            "of joy that costs nothing and cannot be confiscated. This "
            "record describes the mechanism in general terms; it does not "
            "interpret any real person's memories."
        ),
        "how_it_works": (
            "Personal triggers work through associative memory and "
            "affect reactivation. When a joyful episode is encoded, the "
            "context - song, smell, place, date - is stored alongside the "
            "feeling as part of the memory trace. Later, the context cue "
            "alone reactivates the trace, and the reactivated trace "
            "includes the affective component: the body re-runs a "
            "weakened version of the original appraisal and produces a "
            "weakened but real echo of the joy. The polishing effect "
            "comes from reconsolidation: each recall slightly rewrites "
            "the memory, and memories tend to be rewritten toward their "
            "emotional highlights, so the stored joy can grow brighter "
            "than the lived moment was. The wearing-smooth effect is "
            "habituation: repeated cueing without renewal of the "
            "association weakens the affective response, which is why "
            "deliberate, spaced revisiting preserves the trigger better "
            "than constant exposure. Anniversaries work through the same "
            "mechanism with the calendar as the cue."
        ),
        "key_points": [
            "Everyone carries a private trigger map: songs, smells, corners, phrases, first-cold-mornings - unpredictable to anyone else.",
            "The mechanism is associative memory: the cue reactivates the stored episode, feeling included.",
            "Memory polishes: reconsolidation rewrites recollections toward their highlights, so the echo can outshine the original.",
            "Overuse wears triggers smooth: spaced, deliberate revisiting preserves them better than constant exposure.",
            "Knowing your own map is owning a renewable, free, unconfiscatable source of joy.",
        ],
        "requirements": [
            "Concrete examples of private triggers across senses and categories.",
            "The associative-reactivation mechanism stated plainly.",
            "The polishing effect via reconsolidation explained.",
            "The wearing-smooth effect via habituation, with the spaced-revisiting guidance.",
            "Anniversaries named as the calendar version of the same mechanism.",
        ],
        "standards": [
            "Associative reactivation follows standard memory-and-affect science.",
            "Reconsolidation effects follow the memory reconsolidation literature.",
            "Habituation follows the standard learning literature.",
        ],
        "citations": [CIT_BARRETT, CIT_LAZARUS, CIT_SCHERER],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "surprise_triggers",
        "name": "Surprise Triggers: The Odd Joy Setters-Off",
        "group": "Triggers",
        "ladder_rank": 9,
        "ladder_tier": "compounded",
        "description": (
            "Then there are the triggers that make no sense until they "
            "happen - the odd, sideways setters-off of joy that no list "
            "would predict. Finding money in a winter coat. A dog choosing "
            "your lap at a party. The exact right parking spot in the rain. "
            "A stranger's laugh that sounds precisely like someone you "
            "miss. The typo in a formal email that is somehow perfect. A "
            "pigeon doing something with undeniable confidence. These "
            "work, when they work, for three converging reasons. First, "
            "surprise itself is an amplifier: the unbudgeted good gets "
            "the prediction-error bonus, so small delights can produce "
            "disproportionate gladness. Second, incongruity tickles the "
            "same machinery as humor: the world briefly violating "
            "expectations in a harmless way is intrinsically pleasing to "
            "a pattern-hungry brain. Third, and most interesting, these "
            "moments are pure evidence of a friendly universe: nothing "
            "was earned, nothing was planned, and still something good "
            "happened - which the appraisal system reads, correctly or "
            "not, as the world being on your side. People who notice "
            "these moments - who have the habit of attention for small "
            "absurd goodnesses - report more joy overall, not because "
            "their lives contain more of them but because their "
            "appraisal system is tuned to catch them. The odd triggers "
            "are a reminder that joy's causes are wider than the "
            "serious list, and that playfulness of attention is itself "
            "a skill."
        ),
        "how_it_works": (
            "Odd triggers work through the intersection of three "
            "mechanisms. The prediction-error mechanism: the brain "
            "continuously predicts incoming experience, and positive "
            "prediction errors - reality better than expected - generate "
            "a phasic reward signal; the less predicted, the larger the "
            "error, the larger the signal, which is why the coat money "
            "outperforms the expected paycheck emotionally. The "
            "incongruity mechanism: harmless expectation violations "
            "activate the same reward circuitry as humor, because "
            "resolving the incongruity (the pigeon's confidence, the "
            "perfect typo) is intrinsically rewarding to a prediction "
            "machine. The benevolent-world inference: unearned goods are "
            "appraised as evidence about the environment's friendliness, "
            "and a friendlier appraised world lowers the threshold for "
            "the next joy appraisal - a small upward spiral. The "
            "attention habit matters because prediction errors only "
            "register if noticed: two people can walk past the same "
            "absurd pigeon, and only the one whose attention catches it "
            "gets the joy. Tuning attention is tuning the trigger rate."
        ),
        "key_points": [
            "The odd triggers: coat money, the lap-choosing dog, the rain parking spot, the perfect typo, the confident pigeon.",
            "Surprise amplifies through prediction error: the less predicted the good, the larger the reward signal.",
            "Harmless incongruity tickles humor's machinery: the pattern-hungry brain enjoys resolving the violation.",
            "Unearned goods read as evidence of a friendly universe, lowering the threshold for the next joy.",
            "Attention is the skill: the trigger only fires if noticed, so playfulness of attention tunes the joy rate.",
        ],
        "requirements": [
            "At least five concrete odd-trigger examples.",
            "The three mechanisms named: prediction error, incongruity resolution, benevolent-world inference.",
            "The prediction-error bonus tied to expectedness explicitly.",
            "The upward-spiral effect of benevolent-world inference.",
            "Attention-as-skill: noticing as the rate-limiting step.",
        ],
        "standards": [
            "Prediction-error reward follows the standard reward-prediction-error literature.",
            "Incongruity-humor mechanism follows the standard humor science account.",
            "Appraisal-threshold dynamics follow Lazarus 1991.",
        ],
        "citations": [CIT_LAZARUS, CIT_SCHERER, CIT_FREDRICKSON],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "chain_reactions",
        "name": "Chain Reactions: Joy Setting Off Cascades",
        "group": "Triggers",
        "ladder_rank": 9,
        "ladder_tier": "compounded",
        "description": (
            "Joy is a social and sequential emotion: one instance tends to "
            "set off others, in chains that can run for hours or days. "
            "The intrapersonal chain: good news in the morning tints the "
            "appraisal of everything after it - the compliment lands "
            "better, the setback stings less, the evening's small "
            "pleasure registers more brightly - because the pleasant "
            "baseline raises the hit rate of subsequent joy appraisals. "
            "The interpersonal chain: expressed joy is contagious; the "
            "smile, the laugh, the good news told with animation "
            "re-appraises the listener's situation upward, and the "
            "listener's answering joy re-appraises the teller's - the "
            "feedback loop described in the day vignette. The behavioral "
            "chain: joyful people are more generous, more creative, more "
            "willing to engage, and those behaviors create the very "
            "conditions - kindness returned, ideas landing, connections "
            "made - that trigger further joy. The memory chain: each "
            "joyful episode becomes a personal trigger for the future, "
            "so today's chain plants tomorrow's. Chains can also run in "
            "reverse - one person's withheld or mocked joy can dampen a "
            "room - which is why the record on mistakes matters. But the "
            "default direction of a shared, expressed joy is outward and "
            "onward: gladness, given room, multiplies. Understanding "
            "cascades is understanding that joy is not a private event "
            "with a fence around it; it is a small fire that, tended, "
            "warms the whole campsite."
        ),
        "how_it_works": (
            "Cascades work through four linked mechanisms. Affect "
            "priming: a pleasant state biases subsequent appraisals "
            "toward the pleasant interpretation, so the threshold for "
            "the next joy lowers - the intrapersonal chain. Emotional "
            "contagion: humans automatically mimic and then feel the "
            "expressions they perceive, so one person's Duchenne smile "
            "literally nudges the observer's face and then the "
            "observer's feeling - the interpersonal chain, running "
            "through the face-feedback loop. Behavioral mediation: "
            "positive affect broadens the action repertoire toward "
            "prosocial and creative behavior, which changes the "
            "environment in joy-producing ways - the behavioral chain. "
            "Memory banking: each episode is stored with its affective "
            "tag and becomes a future personal trigger - the memory "
            "chain. The reverse cascade works through the same channels "
            "inverted: mocked joy raises others' thresholds via "
            "evaluative threat. The campsite-fire image holds because "
            "all four mechanisms are multiplicative rather than "
            "additive: each link strengthens the next link's input."
        ),
        "key_points": [
            "The intrapersonal chain: morning good news tints the day's appraisals, raising the hit rate of later joys.",
            "The interpersonal chain: expressed joy is contagious through mimicry and the face-feedback loop.",
            "The behavioral chain: joyful people act more generously and creatively, creating the conditions for further joy.",
            "The memory chain: each episode becomes a future personal trigger, so today's joy plants tomorrow's.",
            "Cascades multiply: each link strengthens the next link's input - gladness, given room, multiplies.",
        ],
        "requirements": [
            "Four named chains: intrapersonal, interpersonal, behavioral, memory.",
            "The mechanism of each chain stated: priming, contagion, behavioral mediation, memory banking.",
            "The reverse cascade acknowledged: mocked or withheld joy dampening a room.",
            "The multiplicative (not additive) character of cascades stated.",
            "The campsite-fire image as the structural summary.",
        ],
        "standards": [
            "Affect priming follows the mood-congruence literature.",
            "Emotional contagion follows the standard contagion account with facial feedback.",
            "Behavioral mediation follows Fredrickson 1998 broaden-and-build.",
        ],
        "citations": [CIT_FREDRICKSON, CIT_BARRETT, CIT_LAZARUS],
        "sig_lens": SIG_LENS_DEF,
    },
]

ENTRIES += [
    # ------------------------------------------------ 22-25 BEHAVIOR
    {
        "key": "actions",
        "name": "What People Do When They Feel Joy",
        "group": "How It Shows in Behavior",
        "ladder_rank": 9,
        "ladder_tier": "compounded",
        "description": (
            "Joy moves people, literally and figuratively, in patterns "
            "so consistent they are recognizable across cultures. The "
            "approach moves: people move toward the source of the joy - "
            "toward the person with the news, toward the stage, toward "
            "the window with the view - because joy's action tendency is "
            "approach, not withdrawal. The sharing moves: telling "
            "someone, calling, posting, gathering people - joy seeks "
            "witnesses, and the telling is often as pleasurable as the "
            "event. The celebratory moves: the jump, the spin, the "
            "raised arms, the impromptu dance, the toast - the body's "
            "native language for marking that something good happened. "
            "The generous moves: joyful people tip better, help more, "
            "forgive faster - the broadened state makes other people's "
            "needs more visible and one's own resources feel more "
            "ample. The savoring moves: lingering, re-reading, "
            "photographing, returning to the spot - behaviors that "
            "stretch the moment and bank it as memory. The creative "
            "moves: starting the project, calling the friend with the "
            "idea, playing with possibilities - the broadened mind "
            "proposing new actions. What people notably do NOT do in joy "
            "is also informative: they do not guard, hide, or brace - "
            "the defensive repertoire stands down, which is why joy is "
            "the emotion of open doors. This record describes typical "
            "patterns; it does not prescribe behavior or judge anyone's "
            "actions."
        ),
        "how_it_works": (
            "The action patterns work because each is the behavioral "
            "output of joy's appraisal plus its arousal. Approach "
            "follows directly from the appraisal \"this is good\": the "
            "motor system orients toward appraised goods the way it "
            "orients away from appraised threats. Sharing follows from "
            "the broadcast design: joy evolved partly as a social "
            "signal, and the felt urge to tell is the subjective side "
            "of a system built to recruit witnesses who will amplify "
            "and remember the event with you. Celebration follows from "
            "arousal discharge: the activation has to go somewhere, and "
            "with no threat to spend it on, it spends as expansive "
            "movement. Generosity follows from broaden-and-build: "
            "positive affect widens attention to include others' needs "
            "and raises perceived resource availability, lowering the "
            "subjective cost of helping. Savoring follows from the "
            "memory-banking function: behaviors that re-expose the "
            "person to the trigger strengthen the stored trace and its "
            "future trigger power. Creativity follows from broadened "
            "cognition: more associations active means more novel "
            "combinations proposed."
        ),
        "key_points": [
            "Approach moves: people move toward the source - the person, the stage, the view - because joy's tendency is approach.",
            "Sharing moves: telling, calling, gathering - joy seeks witnesses, and the telling rivals the event in pleasure.",
            "Celebratory moves: jump, spin, raised arms, toast - arousal discharging as expansive movement.",
            "Generous moves: better tipping, more helping, faster forgiving - broadened attention meeting ample-feeling resources.",
            "Savoring and creative moves: lingering and banking the moment; starting projects and proposing ideas.",
        ],
        "requirements": [
            "Six named action families: approach, sharing, celebratory, generous, savoring, creative.",
            "Each family tied to its mechanism: appraisal, broadcast design, arousal discharge, broaden-and-build, memory banking, broadened cognition.",
            "The notable absence stated: no guarding, hiding, or bracing - joy as the emotion of open doors.",
            "The descriptive-only boundary: patterns described, nothing prescribed, no one judged.",
            "Cross-cultural recognizability noted for the core patterns.",
        ],
        "standards": [
            "Action tendencies follow Frijda 1986: emotion-specific action readiness.",
            "Broaden-and-build behavioral effects follow Fredrickson 1998.",
            "Broadcast design follows the social-functional account of emotion.",
        ],
        "citations": [CIT_FRIJDA, CIT_FREDRICKSON, CIT_EKMAN1999],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "speech",
        "name": "What Joy Sounds Like: Words, Tone, Speech",
        "group": "How It Shows in Behavior",
        "ladder_rank": 9,
        "ladder_tier": "compounded",
        "description": (
            "Joy has a soundtrack, and it is recognizable before a single "
            "word is understood. The voice rises: pitch climbs, the range "
            "widens, and speech gets faster and more melodic - the "
            "opposite of the flattened, slowed speech of low moods. "
            "Laughter punctuates: not just at jokes but woven through "
            "sentences, the small exhaled laughs that mark sentences as "
            "glad. The characteristic phrases are exclamations and "
            "sharings: \"You won't believe this,\" \"Listen to what "
            "happened,\" \"I'm so glad,\" \"This is wonderful\" - joy "
            "speaks in announcements and appreciations. Questions change "
            "too: joyful people ask more, and ask differently - curious, "
            "forward-leaning questions rather than guarded ones. Tone "
            "carries the signature even when words do not: warmth in the "
            "timbre, a smile audible in the vowels, the voice seeming to "
            "lean toward the listener. There is also a volume effect: "
            "joyful speech is often simply louder, spilling past indoor "
            "voice without noticing. And the listening changes: joyful "
            "people interrupt more - not from rudeness but from eager "
            "overlap, the conversation moving too fast for turn-taking. "
            "Writers and actors use all of this as dialogue technique: to "
            "write a joyful character, raise the pitch, quicken the pace, "
            "add the exclamations, and let the sentences tumble over each "
            "other. This record describes the vocal pattern; it does not "
            "analyze any real person's speech."
        ),
        "how_it_works": (
            "The vocal pattern works because the voice is a direct "
            "readout of arousal and affect. Raised pitch and widened "
            "range come from increased tension in the laryngeal muscles "
            "plus greater respiratory drive - the same arousal that "
            "brightens the body brightens the voice. Faster tempo comes "
            "from the broadened, accelerated cognition: more ideas "
            "arriving per second means more words per second, with "
            "laughter woven in as the respiratory system discharges "
            "arousal between phrases. The announcement phrasing (\"you "
            "won't believe\") follows from the broadcast design: the "
            "utterances are engineered, unconsciously, to recruit "
            "attention and share the appraisal. The audible smile is "
            "mechanical: smiling shortens the vocal tract and raises "
            "formant frequencies, literally brightening the timbre, so "
            "listeners hear the face in the voice. Eager overlap comes "
            "from approach motivation applied to conversation: the "
            "impulse to connect outruns the discipline of turn-taking."
        ),
        "key_points": [
            "Pitch rises and range widens: the voice gets faster, more melodic - the opposite of flattened low-mood speech.",
            "Laughter weaves through sentences: small exhaled laughs marking utterances as glad.",
            "Joy speaks in announcements and appreciations: exclamations, sharings, curious forward-leaning questions.",
            "The smile is audible: smiling shortens the vocal tract and brightens the timbre - listeners hear the face.",
            "Eager overlap: joyful people interrupt from enthusiasm, not rudeness - connection outrunning turn-taking.",
        ],
        "requirements": [
            "Vocal-acoustic features: pitch, range, tempo, volume.",
            "Laughter placement described as woven-through, not only at jokes.",
            "Characteristic phrasing with quoted examples of announcements and appreciations.",
            "The audible-smile mechanism: vocal-tract shortening and formant brightening.",
            "The writer/actor application: dialogue technique for joyful characters.",
        ],
        "standards": [
            "Vocal-acoustic correlates of positive affect follow the standard vocal-expression literature.",
            "Broadcast phrasing follows the social-functional account of emotion.",
            "Formant effects of smiling follow standard speech science.",
        ],
        "citations": [CIT_SCHERER, CIT_EKMAN1999, CIT_FRIJDA],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "decisions",
        "name": "How Joy Changes Decisions and Judgment",
        "group": "How It Shows in Behavior",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Joy does not just color the moment; it tilts the machinery "
            "of choice. The well-documented effects run in several "
            "directions at once. Risk: joyful people tend to see "
            "opportunities as more likely and setbacks as more manageable "
            "- optimism rises, and with it the willingness to try. "
            "Generosity: as the actions record notes, helping and giving "
            "increase - the world looks like a place where generosity "
            "pays. Creativity: problem-solving gets more flexible and "
            "original; the broadened mind finds the third option that the "
            "narrowed mind missed. Speed: decisions come faster, with less "
            "agonizing - confidence in the appraisal reduces the felt "
            "need for exhaustive deliberation. Social judgment: other "
            "people are evaluated more warmly; strangers seem kinder, "
            "partners seem more attractive, the benefit of the doubt gets "
            "granted freely. The shadow side is real and worth naming: "
            "the same optimism can underestimate real risks, the same "
            "speed can skip due diligence, the same warmth can extend "
            "trust where caution was warranted. Joy is not a bias to "
            "eliminate - its effects are mostly beneficial and often "
            "accurate, since a good mood frequently reflects genuinely "
            "good conditions. It is a lens to know you are wearing: on a "
            "bright day, the wise move is to enjoy the broader view while "
            "keeping one deliberate checkpoint for the decisions that "
            "truly matter. This record describes tendencies, not rules, "
            "and offers no advice about any real person's choices."
        ),
        "how_it_works": (
            "The decision effects work through affect-as-information and "
            "through broadening. Affect-as-information: the brain treats "
            "the current feeling as data about the world - feeling good "
            "is (usually correctly) read as evidence that things are "
            "going well, which rationally justifies more optimistic "
            "probability estimates and warmer social judgments. Broadening: "
            "positive affect widens the scope of attention and the set of "
            "action ideas under consideration, which directly improves "
            "creative problem-solving (more candidates) and speeds "
            "decisions (the good options are more salient, so search "
            "terminates earlier). The shadow side is the same mechanisms "
            "overshooting: affect-as-information misfires when the good "
            "mood comes from an irrelevant source (the sunny day "
            "inflating a financial judgment), and broadened search can "
            "terminate before the due-diligence option is examined. The "
            "checkpoint advice works because deliberation is a separate, "
            "slower system that can audit the fast system's output "
            "without canceling the benefits of the broadened state."
        ),
        "key_points": [
            "Risk tilts optimistic: opportunities look likelier, setbacks look more manageable, willingness to try rises.",
            "Generosity and warmth rise: others are judged more kindly, the benefit of the doubt gets granted freely.",
            "Creativity improves: the broadened mind finds the third option the narrowed mind missed.",
            "Decisions speed up: confidence in the appraisal reduces agonizing; good options are more salient.",
            "The lens to know: enjoy the broader view, keep one deliberate checkpoint for the decisions that truly matter.",
        ],
        "requirements": [
            "Five named decision effects: risk, generosity, creativity, speed, social judgment.",
            "The shadow side named honestly: underestimated risks, skipped diligence, misplaced trust.",
            "The affect-as-information mechanism stated plainly.",
            "The broadening mechanism tied to creativity and speed specifically.",
            "The checkpoint guidance framed as lens-awareness, with the no-advice-about-real-choices boundary.",
        ],
        "standards": [
            "Affect-as-information follows the standard affect-and-judgment literature.",
            "Broadening effects on cognition follow Fredrickson 1998.",
            "Optimism and risk effects follow the positive-affect and decision literature.",
        ],
        "citations": [CIT_FREDRICKSON, CIT_LAZARUS, CIT_BARRETT],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "intensity_behavior",
        "name": "Joy at Full Volume: Behavior Under Intensity",
        "group": "How It Shows in Behavior",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "As joy climbs toward its ceiling, behavior escalates along a "
            "recognizable curve - and the curve has a far end worth "
            "knowing about. Early escalation is pure amplification: "
            "bigger gestures, louder laughter, more people told, the "
            "celebration expanding to fill the available space and time. "
            "Mid escalation brings disinhibition: the usual filters "
            "loosen - dancing in public, singing to strangers, grand "
            "promises, extravagant generosity - behaviors the person "
            "would moderate at lower volume. This is usually harmless "
            "and often delightful; it is the wedding-dance-floor zone, "
            "and cultures build whole rituals to house it safely. Late "
            "escalation is where the cautions live: judgment narrows "
            "even as confidence peaks, spending and promises can outrun "
            "tomorrow's resources, and the drive to keep the peak going "
            "can lead to overindulgence of whatever is at hand. None of "
            "this makes intense joy dangerous in itself - it is one of "
            "the safest peaks in the emotional repertoire - but the "
            "combination of high confidence, low inhibition, and "
            "narrowed judgment deserves the same respect as any powerful "
            "state. The practical pattern that experienced people "
            "follow, usually without articulating it: celebrate fully, "
            "spend moderately, promise carefully, and let the peak pass "
            "without chasing it. The peak will pass; the memories and "
            "the strengthened bonds remain, and they are the part that "
            "was always the point."
        ),
        "how_it_works": (
            "The escalation curve works because arousal and disinhibition "
            "scale together while executive control scales inversely past "
            "a point. Rising arousal increases motor drive and reward "
            "sensitivity - hence bigger gestures and grander impulses - "
            "while the prefrontal systems that normally veto impulses "
            "are partly captured by the positive appraisal (everything "
            "seems like a good idea when everything is going well). The "
            "wedding-dance-floor zone is safe because the disinhibited "
            "behaviors there are socially scaffolded: the ritual "
            "contains the escalation the way a fireplace contains the "
            "fire. The late-stage cautions come from the narrowing that "
            "accompanies peak arousal: attention locks onto the "
            "celebration and the immediate reward, and the future - "
            "tomorrow's budget, next week's promise - fades from the "
            "decision frame. The experienced pattern (celebrate fully, "
            "spend moderately, promise carefully) works because it "
            "separates the expressive channel, which should run free, "
            "from the commitment channel, which should stay deliberate."
        ),
        "key_points": [
            "Early escalation is pure amplification: bigger gestures, louder laughter, the celebration expanding to fill space and time.",
            "Mid escalation brings disinhibition: loosened filters, public dancing, grand promises - usually harmless, often delightful.",
            "Cultures build rituals (the wedding-dance-floor zone) to house mid-escalation safely - the fireplace containing the fire.",
            "Late escalation narrows judgment while confidence peaks: spending and promises can outrun tomorrow's resources.",
            "The experienced pattern: celebrate fully, spend moderately, promise carefully, let the peak pass without chasing it.",
        ],
        "requirements": [
            "Three named escalation phases with the behavioral character of each.",
            "The ritual-containment point: social scaffolding housing disinhibition safely.",
            "Late-stage cautions stated honestly without pathologizing intense joy.",
            "The arousal-disinhibition vs executive-control mechanism.",
            "The expressive-vs-commitment channel separation as the practical pattern.",
        ],
        "standards": [
            "Arousal-disinhibition dynamics follow standard affective science.",
            "Ritual containment follows the social-functional account of celebration.",
            "Decision-narrowing under high arousal follows the standard attention literature.",
        ],
        "citations": [CIT_FRIJDA, CIT_SCHERER, CIT_FREDRICKSON],
        "sig_lens": SIG_LENS_DEF,
    },
]

ENTRIES += [
    # ------------------------------------------------ 26-28 HEALTHY EXPRESSION
    {
        "key": "healthy_expression",
        "name": "Expressing Joy Well: Saying, Showing, Channeling",
        "group": "Expressing It Healthily",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Joy expressed well does three jobs at once: it honors the "
            "feeling, it shares it without imposing it, and it banks it "
            "for later. Saying it is the most direct channel: telling "
            "people what happened and how glad you are, in plain words - "
            "\"I'm really happy about this\" is underrated as a "
            "sentence. Showing it is the broadcast channel: the smile, "
            "the laugh, the visible lightness - letting the face and body "
            "do what they are designed to do, which gives others "
            "permission to feel it too. Channeling it is the craft "
            "channel: putting the energy into something - the "
            "celebration arranged, the thank-you written, the project "
            "started, the kindness passed on - so the arousal becomes "
            "action instead of just noise. The sharing etiquette "
            "matters: expressed joy lands best when it invites rather "
            "than performs - \"come celebrate with me\" rather than a "
            "broadcast that demands applause. Reading the room is part "
            "of expressing well: full volume at the wedding, softer "
            "volume at the bedside of someone grieving - not hiding the "
            "joy, but sizing it to the context, which is consideration "
            "rather than suppression. And the banking habit completes "
            "it: the journal line, the photo, the retelling - deliberate "
            "savoring that converts today's peak into tomorrow's "
            "personal trigger. Expressed well, joy is generous: it leaves "
            "everyone involved slightly richer than it found them. This "
            "record offers general everyday guidance only - the ordinary "
            "practices of a feeling well handled - not therapeutic "
            "advice for any real person."
        ),
        "how_it_works": (
            "Healthy expression works because it aligns the three output "
            "channels with joy's design. Saying it works through "
            "affect labeling and social recruitment: naming the feeling "
            "consolidates the appraisal, and telling recruits witnesses "
            "whose shared joy amplifies and remembers the event. Showing "
            "it works through contagion: the visible Duchenne assembly "
            "nudges observers' faces and feelings, spreading the good "
            "and building the bond - expression as a social gift. "
            "Channeling it works through arousal use: activation seeks "
            "discharge, and directed discharge (the celebration, the "
            "project, the kindness) converts the energy into lasting "
            "goods rather than letting it dissipate as restlessness. The "
            "invitation-not-performance etiquette works because "
            "autonomy matters to recipients: invited joy is received as "
            "inclusion, demanded applause as dominance. Room-reading "
            "works through the same appraisal machinery in others: "
            "sizing the volume to context avoids triggering others' "
            "threat or envy appraisals. Banking works through "
            "reconsolidation: deliberate savoring strengthens the "
            "stored trace into a future trigger."
        ),
        "key_points": [
            "Saying it: plain words - \"I'm really happy about this\" - consolidate the appraisal and recruit witnesses.",
            "Showing it: the visible smile and lightness give others permission to feel it too - expression as a social gift.",
            "Channeling it: celebration arranged, thank-you written, project started, kindness passed on - arousal becoming action.",
            "Invite, don't perform: \"come celebrate with me\" lands; demanded applause doesn't.",
            "Bank it: the journal line, the photo, the retelling - deliberate savoring converting today's peak into tomorrow's trigger.",
        ],
        "requirements": [
            "Three named channels: saying, showing, channeling, each with mechanism and examples.",
            "The invitation-vs-performance etiquette stated.",
            "Room-reading: sizing volume to context as consideration, distinguished from suppression.",
            "The banking habit: savoring practices that convert peaks into future triggers.",
            "The general-guidance-only boundary: everyday practices, not therapeutic advice.",
        ],
        "standards": [
            "Affect labeling effects follow the standard emotion-regulation literature.",
            "Contagion benefits follow the social-functional account of positive expression.",
            "Savoring mechanics follow the positive-emotion regulation literature.",
        ],
        "citations": [CIT_FREDRICKSON, CIT_LAZARUS, CIT_BARRETT],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "unhealthy_expression",
        "name": "The Costs of Bottling Up or Exploding Joy",
        "group": "Expressing It Healthily",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Joy mishandled does not vanish; it converts into costs, and "
            "the two classic mishandlings are opposites with opposite "
            "price tags. Bottling it up - feeling the surge and clamping "
            "the lid down, the smile swallowed, the news untold - costs "
            "first in effort: suppression is metabolically and mentally "
            "expensive, and the stiffness shows. It costs second in "
            "amplification foregone: unshared joy does not get the "
            "contagion loop, the witnesses, or the memory-banking that "
            "telling provides, so the same event yields less total "
            "gladness. It costs third in signal to others: people read "
            "the clamp-down as distance or disapproval, and relationships "
            "pay a small tax. Habitual bottling teaches the appraisal "
            "system that joy is unwelcome, and the system obliges by "
            "sending less of it. Exploding it - the peak with no "
            "governor, the celebration that tramples the context, the "
            "joy that demands everyone match its volume - costs first in "
            "collateral: other people's feelings, plans, and boundaries "
            "run over. It costs second in credibility: the promises made "
            "at peak volume come due at normal volume. It costs third in "
            "rebound: the harder the peak is chased and forced, the "
            "flatter the aftermath feels by contrast. The healthy middle "
            "is not moderation of the feeling but stewardship of its "
            "expression: feel it fully, show it honestly, size it to the "
            "room, and channel the surplus into something that lasts. "
            "This record describes patterns and costs in general terms; "
            "it does not diagnose anyone's habits or prescribe treatment."
        ),
        "how_it_works": (
            "The costs work through the mechanisms already described, "
            "run in reverse. Bottling costs effort because suppression "
            "is active inhibition of a strong motor drive - the "
            "executive system working against the affective system, "
            "which consumes resources and produces the observable "
            "stiffness. It forfeits amplification because the contagion "
            "loop, the witness memory-banking, and the social "
            "re-appraisal all require visible expression as input; no "
            "signal out, no loop. Habitual suppression retrains the "
            "appraisal through learning: the brain tracks which emotions "
            "get expressed and socially rewarded, and down-regulates the "
            "ones that are consistently clamped. Exploding costs "
            "collateral because ungoverned expression ignores others' "
            "appraisal states - the volume that delights at the wedding "
            "threatens at the bedside. It costs credibility through "
            "state-dependent commitment: promises encoded at peak "
            "arousal are evaluated at normal arousal later, and the gap "
            "reads as unreliability. The rebound cost is contrast: the "
            "appraisal system calibrates to recent peaks, so a forced "
            "maximum resets the baseline upward and ordinary gladness "
            "temporarily reads as flat."
        ),
        "key_points": [
            "Bottling costs effort: suppression is the executive system fighting the affective system, and the stiffness shows.",
            "Bottling forfeits amplification: no visible signal means no contagion loop, no witnesses, no banked memory.",
            "Habitual bottling retrains the system: consistently clamped joy gets sent less often.",
            "Exploding costs collateral, credibility, and rebound: trampled contexts, peak-volume promises, contrast-flat aftermaths.",
            "The middle is stewardship, not moderation: feel fully, show honestly, size to the room, channel the surplus.",
        ],
        "requirements": [
            "Both mishandlings named with three costs each, stated concretely.",
            "The suppression-effort mechanism and the observable stiffness.",
            "The forfeited-amplification mechanism: which loops require visible expression.",
            "The retraining mechanism for habitual bottling.",
            "The stewardship summary as the constructive close, with the descriptive-only boundary.",
        ],
        "standards": [
            "Suppression costs follow the emotion-regulation literature.",
            "State-dependent commitment effects follow standard judgment research.",
            "Contrast/hedonic-calibration effects follow the adaptation literature.",
        ],
        "citations": [CIT_BARRETT, CIT_FREDRICKSON, CIT_LAZARUS],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "everyday_practices",
        "name": "Everyday Practices That Keep Joy in Balance",
        "group": "Expressing It Healthily",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Joy, like a garden, responds to tending - not forcing, "
            "tending. The practices that keep it in balance are small, "
            "repeatable, and ordinary. Notice: the two-minute daily "
            "inventory of what went well - the good message, the decent "
            "meal, the small kindness - which trains the appraisal "
            "system to register hits it would otherwise walk past. "
            "Share: telling one person one good thing per day, which "
            "feeds the contagion loop and banks the memory. Move: the "
            "walk, the stretch, the uncurling of the posture, which "
            "keeps the body's joy channels open through the "
            "bidirectional loop. Play: a daily ration of something done "
            "for the fun of it - the game, the joke, the aimless making "
            "- because play is joy's native climate and scheduled play "
            "is scheduled joy. Give: the small deliberate kindness, "
            "which reliably produces the giver's glow and plants a "
            "trigger in someone else's day. Savor: lingering over the "
            "good bite, the good view, the good minute instead of "
            "rushing past - attention as the rate-limiting step. Rest: "
            "protecting sleep and downtime, because an exhausted "
            "appraisal system sends less joy and a rested one sends "
            "more. None of these manufacture joy on demand - that is "
            "the direct-pursuit trap - but each raises the probability "
            "that joy's causes will be noticed, shared, and repeated, "
            "which is the byproduct path in daily form. These are "
            "general everyday habits, not a program and not advice for "
            "any real person's situation."
        ),
        "how_it_works": (
            "The practices work because each tunes one link in joy's "
            "causal chain. Noticing tunes the appraisal threshold: "
            "deliberate daily registration of small goods trains the "
            "relevance detector to fire on smaller inputs, raising the "
            "hit rate without changing the world. Sharing tunes the "
            "social loop: each telling runs the contagion and "
            "memory-banking machinery, multiplying the day's yield. "
            "Moving tunes the body channel: posture and activity feed "
            "the bidirectional loop, keeping the physical substrate of "
            "joy available. Play tunes the cause directly: play "
            "situations are engineered joy triggers, so scheduled play "
            "is scheduled exposure to the trigger class. Giving tunes "
            "both the giver's appraisal (prosocial efficacy is a "
            "classic trigger) and the recipient's future triggers. "
            "Savoring tunes attention: since noticing is the "
            "rate-limiting step, deliberate lingering converts "
            "would-be-misses into registrations. Rest tunes the "
            "substrate: sleep deprivation raises threat appraisal and "
            "lowers reward sensitivity, so protected rest keeps the "
            "system's gain staging favorable to joy."
        ),
        "key_points": [
            "Notice: a two-minute daily inventory of what went well trains the appraisal system to register hits it would walk past.",
            "Share: one good thing told to one person per day feeds the contagion loop and banks the memory.",
            "Move and play: the walk and the uncurled posture keep the body channel open; scheduled play is scheduled joy.",
            "Give and savor: the small deliberate kindness glows the giver; lingering attention converts misses into registrations.",
            "Rest: protected sleep keeps the system's gain staging favorable - exhaustion sends less joy, rest sends more.",
        ],
        "requirements": [
            "Seven named practices: notice, share, move, play, give, savor, rest.",
            "Each practice tied to the specific link in the causal chain it tunes.",
            "The byproduct framing: raising probability, not manufacturing on demand.",
            "Attention named as the rate-limiting step in the savoring practice.",
            "The general-habits boundary: not a program, not advice for any real person's situation.",
        ],
        "standards": [
            "Gratitude-noticing effects follow the positive-psychology intervention literature.",
            "Savoring mechanics follow the positive-emotion regulation literature.",
            "Sleep-affect interactions follow standard sleep science.",
        ],
        "citations": [CIT_FREDRICKSON, CIT_BARRETT, CIT_LAZARUS],
        "sig_lens": SIG_LENS_DEF,
    },
]

ENTRIES += [
    # ------------------------------------------------ 29-31 RECOGNIZING IN OTHERS
    {
        "key": "reading_signs",
        "name": "Reading Joy in Others: Face, Body, Voice, Behavior",
        "group": "Recognizing It in Others",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Recognizing joy in another person is a four-channel read, "
            "and the channels check each other. Face: look for the "
            "Duchenne assembly - mouth corners up and back plus the eye "
            "crinkle and cheek lift; the mouth alone may be politeness, "
            "but the eyes joining in is the genuine marker. Body: the "
            "uncurl - open chest, lifted posture, bigger and springier "
            "movement; joyful people take up a little more space and "
            "move a little faster. Voice: raised pitch, widened range, "
            "quickened tempo, laughter woven through the sentences, the "
            "smile audible in the vowels. Behavior: the approach and "
            "sharing moves - moving toward people, telling the news, "
            "the celebratory gestures, the sudden generosity. The "
            "skilled read weights the channels by honesty: the eyes and "
            "the body leak more truth than the mouth, because AU6 is "
            "harder to fake than AU12 and posture is harder to pose "
            "than a smile. Context is the fifth channel: the same grin "
            "means different things at a wedding and at a layoff "
            "announcement, and the wise reader always asks what just "
            "happened before concluding what the face means. And the "
            "humblest rule of reading: hold the read lightly. You are "
            "inferring a feeling from its signals, not observing the "
            "feeling itself - so treat the read as a good hypothesis "
            "to check gently, never as a label to stick on a person. "
            "This record teaches signal-reading as a social skill; it "
            "does not authorize diagnosing or labeling any real person."
        ),
        "how_it_works": (
            "The four-channel read works because each channel carries "
            "partially independent information about the same underlying "
            "state, and agreement across channels raises confidence "
            "while disagreement lowers it - the same logic as "
            "triangulation. The honesty weighting works through the "
            "voluntariness asymmetry: channels under less voluntary "
            "control (AU6, posture shifts, vocal pitch) are harder to "
            "pose, so they carry more diagnostic weight. Context works "
            "as a Bayesian prior: the base rate of genuine joy is high "
            "at celebrations and low at funerals, so the same signal "
            "strength updates to different conclusions. The hold-lightly "
            "rule works because expression-to-feeling inference is "
            "probabilistic: display rules, individual differences, and "
            "blended emotions all add noise, so even a skilled reader "
            "holds residual uncertainty - and acting on the read as if "
            "it were certain is where social errors come from. The "
            "educational framing matters: signal-reading is a tool for "
            "responding well, not a license for labeling."
        ),
        "key_points": [
            "Four channels: face (the Duchenne assembly), body (the uncurl), voice (raised, quickened, laughter-woven), behavior (approach and sharing moves).",
            "Weight by honesty: eyes and body leak more truth than the mouth - AU6 is harder to fake than AU12.",
            "Context is the fifth channel: the same grin means different things at a wedding and at a layoff announcement.",
            "Triangulate: agreement across channels raises confidence, disagreement lowers it.",
            "Hold the read lightly: infer, don't label - a good hypothesis to check gently, never a sticker for a person.",
        ],
        "requirements": [
            "Four named channels with the specific signals of each.",
            "The honesty weighting with the voluntariness-asymmetry explanation.",
            "Context as Bayesian prior with the wedding/funeral contrast.",
            "Triangulation logic: agreement and disagreement rules.",
            "The hold-lightly rule and the explicit no-labeling boundary.",
        ],
        "standards": [
            "Channel anatomy follows Ekman and Friesen 1978 (FACS) and the vocal-expression literature.",
            "Voluntariness asymmetry follows the Ekman tradition.",
            "Probabilistic inference framing follows Barrett 2017 on constructed emotion perception.",
        ],
        "citations": [CIT_FACS, CIT_EKMAN1999, CIT_BARRETT],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "supportive_responses",
        "name": "What to Say and Do Around Someone Feeling Joy",
        "group": "Recognizing It in Others",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Someone else's joy is an opportunity disguised as a "
            "moment: respond well and the joy multiplies for both of "
            "you. The core skill has a name in relationship research - "
            "active-constructive responding - and it is simple: meet "
            "the good news with genuine interest and enthusiasm. Ask "
            "for the story: \"Tell me everything - how did it happen?\" "
            "People with good news want to relive it, and the "
            "retelling is the savoring. Match the energy without "
            "hijacking it: celebrate at their volume, not yours, and "
            "keep the spotlight on their news rather than pivoting to "
            "your own. Mark it: the toast, the congratulations, the "
            "small ritual of acknowledgment - being witnessed is part "
            "of what makes the event feel real. Ask about meaning: "
            "\"What does this mean for what's next?\" - which honors "
            "the event as a chapter, not just a moment. And protect "
            "it: don't problem-solve the good news, don't forecast the "
            "downsides, don't compete with a bigger story of your own "
            "- there will be time for realism later, and the moment of "
            "gladness is short. None of this requires performing "
            "feelings you don't have; interested questions and warm "
            "attention are honest even on your tired days. Responded "
            "to well, another person's joy becomes a small shared "
            "celebration - one of the cheapest and most reliable "
            "builders of closeness that exists. This is general social "
            "guidance, not advice about any real relationship."
        ),
        "how_it_works": (
            "Active-constructive responding works through the same "
            "amplification machinery as sharing: the teller's joy "
            "needs witnesses to run the contagion loop and the "
            "memory-banking, and an engaged listener supplies both. "
            "Asking for the story works through savoring: the retelling "
            "re-runs the appraisal at low intensity, extending and "
            "deepening the feeling while converting the listener into "
            "a co-owner of the memory. Energy-matching works through "
            "attunement: the teller's nervous system reads the "
            "listener's response as social evidence about the event's "
            "value, so matched enthusiasm validates while hijacking "
            "re-centers. Marking works through ritual: formal "
            "acknowledgment tags the event as significant in shared "
            "memory, which strengthens its future trigger power for "
            "both people. Protecting the moment works by withholding "
            "the threat and problem appraisals that would compete: "
            "realism introduced too early re-appraises the event "
            "downward before the joy has finished its work. The "
            "closeness dividend is the relationship-level broaden-and-"
            "build: shared positive events become shared resources."
        ),
        "key_points": [
            "Meet good news with genuine interest and enthusiasm: active-constructive responding is the core skill.",
            "Ask for the story: \"Tell me everything\" - the retelling is the savoring, and it makes you a co-owner of the memory.",
            "Match their energy without hijacking: celebrate at their volume, keep the spotlight on their news.",
            "Mark it: the toast, the congratulations, the small ritual - being witnessed makes the event feel real.",
            "Protect it: no problem-solving the good news, no forecasted downsides, no competing story - realism can wait.",
        ],
        "requirements": [
            "The named skill (active-constructive responding) with its plain definition.",
            "Five concrete behaviors: ask for the story, match energy, mark it, ask about meaning, protect it.",
            "Quoted example phrasings for the story and meaning questions.",
            "The hijacking warning: spotlight discipline.",
            "The honesty note: interested questions work even on tired days; general guidance, not relationship advice.",
        ],
        "standards": [
            "Active-constructive responding follows the capitalization research in relationship science.",
            "Savoring-through-retelling follows the positive-emotion regulation literature.",
            "Shared-resource framing follows Fredrickson 1998 broaden-and-build.",
        ],
        "citations": [CIT_FREDRICKSON, CIT_LAZARUS, CIT_BARRETT],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "mistakes",
        "name": "The Mistakes That Make Joy Feel Worse",
        "group": "Recognizing It in Others",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Responding poorly to someone's joy is easy, common, and "
            "fixable - the mistakes are a short list. The minimizer: "
            "\"That's nice\" in a flat tone, the good news acknowledged "
            "and shelved - which reads as the event not mattering, and "
            "the teller feels foolish for having felt so much. The "
            "one-upper: answering good news with bigger news of one's "
            "own - which converts the teller's moment into an audience "
            "for yours. The realist: immediately forecasting problems - "
            "\"just don't spend it all\" - which re-appraises the event "
            "downward before the joy finishes its work. The interrogator: "
            "grilling the good news for flaws and catches - which turns "
            "celebration into defense. The ghost: changing the subject, "
            "checking the phone - which signals that the joy is boring "
            "or unwelcome. The moralist: \"must be nice\" with an edge, "
            "or the lecture on gratitude - which taxes the gladness with "
            "guilt. Each mistake has the same shape underneath: the "
            "responder's own state - envy, anxiety, fatigue, discomfort "
            "with emotion - leaking into the response and taxing someone "
            "else's good moment. The fix is equally uniform: notice the "
            "leak, set it aside for the three minutes the celebration "
            "needs, and give the good news its clean run. People "
            "remember, for years, who celebrated with them and who "
            "rained on it - which makes this small skill one of the "
            "highest-leverage social habits there is. General guidance "
            "only; not a judgment of any real interaction."
        ),
        "how_it_works": (
            "The mistakes work - that is, they damage - through "
            "re-appraisal interference. The teller's joy is mid-flight, "
            "sustained by the appraisal \"this is good and shared\"; each "
            "mistake injects a competing appraisal. Minimizing injects "
            "\"this doesn't matter to others,\" which downgrades the "
            "social-evidence component. One-upping injects \"your news "
            "is the opening act,\" re-centering attention. Realism "
            "injects threat/problem appraisals that compete directly "
            "with the gladness for the same attentional resources. "
            "Interrogation injects evaluative threat, converting the "
            "teller's state toward defense. Ghosting injects social "
            "rejection, which the appraisal system weighs heavily. "
            "Moralizing injects guilt, which schedules itself to arrive "
            "with every future lift. The common shape - the responder's "
            "state leaking - works through affect spillover: unmanaged "
            "envy, anxiety, or fatigue seeks expression, and the good "
            "news becomes its occasion. The three-minute fix works "
            "because celebrations are short: the joy needs only a brief "
            "clean run to complete its amplification and banking work."
        ),
        "key_points": [
            "The minimizer (\"that's nice,\" flat), the one-upper, the realist, the interrogator, the ghost, the moralist - six classic mistakes.",
            "Each injects a competing appraisal: irrelevance, re-centering, threat, defense, rejection, guilt.",
            "The common shape: the responder's own envy, anxiety, fatigue, or discomfort leaking into the response.",
            "The fix is uniform: notice the leak, set it aside for the three minutes the celebration needs, give the news its clean run.",
            "People remember for years who celebrated with them - small skill, highest-leverage social habit.",
        ],
        "requirements": [
            "Six named mistakes with the characteristic line or behavior of each.",
            "The competing-appraisal mechanism for each mistake.",
            "The common-shape diagnosis: responder-state spillover.",
            "The three-minute fix stated as the uniform remedy.",
            "The long-memory point and the general-guidance boundary.",
        ],
        "standards": [
            "Response-style taxonomy follows the capitalization research (active-constructive vs destructive responses).",
            "Re-appraisal interference follows Lazarus 1991.",
            "Affect spillover follows standard emotion science.",
        ],
        "citations": [CIT_LAZARUS, CIT_FREDRICKSON, CIT_BARRETT],
        "sig_lens": SIG_LENS_DEF,
    },
]

ENTRIES += [
    # ------------------------------------------------ 32-34 RELATED + SIMULATION
    {
        "key": "neighbors",
        "name": "Joy's Neighbors: Related Emotions and How to Tell Them Apart",
        "group": "Related Emotions and Mixes",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Joy lives in a crowded neighborhood, and telling the "
            "neighbors apart is a genuine skill. Contentment: the "
            "closest cousin - pleasant like joy but low-energy; joy "
            "wants to move and share, contentment wants to sit still "
            "and stay. The test is the body: restless lightness means "
            "joy, settled ease means contentment. Pride: joy about the "
            "self's achievement - the appraisal adds \"I did this\"; "
            "pure joy can be about anything good, pride is about the "
            "self's agency in it. Amusement: joy's playful sibling - "
            "shorter, lighter, tied to the funny; amusement is joy "
            "with a punchline. Relief: covered in its own record - the "
            "exhale underneath; joy-with-relief is the most common "
            "blend, and the relief layer is what distinguishes it from "
            "pure surprise-joy. Gratitude: joy with a benefactor - the "
            "appraisal adds \"someone gave this to me\"; gratitude "
            "points outward in thanks where joy simply glows. Hope: "
            "joy's forward-looking cousin - pleasant anticipation of a "
            "good future; hope is joy about what hasn't happened yet. "
            "Love (in Plutchik's sense): the joy-plus-trust blend - "
            "warm, affiliative, directed at a person; joy alone needs "
            "no object person. Ecstasy: not a neighbor but joy at "
            "maximum volume - same family, top of the dial. Envy is "
            "the informative opposite-neighbor: it is what joy looks "
            "like from the outside when someone else has the good "
            "thing - recognizing the pair helps readers understand "
            "both. The practical use of the map: when a feeling is "
            "hard to name, check the neighbors - the distinctive "
            "appraisal (who did it? is it funny? is someone owed "
            "thanks? hasn't it happened yet?) usually identifies the "
            "address. Descriptive mapping only; no labeling of real "
            "people."
        ),
        "how_it_works": (
            "The neighbor map works because each related emotion is joy "
            "plus or minus one appraisal ingredient, which makes "
            "discrimination a matter of checking ingredients. "
            "Contentment is joy minus arousal: same pleasantness, "
            "different energy, hence the body test. Pride is joy plus "
            "self-agency appraisal: the event is good AND I caused it. "
            "Amusement is joy plus benign-violation appraisal: the "
            "incongruity-resolution machinery firing on something "
            "funny. Gratitude is joy plus benefactor appraisal: the "
            "good came FROM someone, adding the thankfulness vector. "
            "Hope is joy displaced in time: the good is appraised as "
            "probable-future rather than present. Love (Plutchik's "
            "dyad) is joy plus trust: the affiliative bond ingredient "
            "added. Ecstasy is joy scaled to maximum arousal: same "
            "ingredients, maximum volume. Envy is the social-comparison "
            "inversion: another's good appraised as one's own lack. "
            "Because the ingredients are appraisals, the discrimination "
            "questions (who did it? funny? thanks owed? future?) work "
            "reliably: each question tests for one ingredient."
        ),
        "key_points": [
            "Contentment is joy minus arousal: restless lightness vs settled ease - the body is the test.",
            "Pride is joy plus self-agency (\"I did this\"); gratitude is joy plus a benefactor (\"someone gave this\").",
            "Amusement is joy with a punchline: the benign-violation machinery firing on something funny.",
            "Hope is joy about the future; love (Plutchik's dyad) is joy plus trust, directed at a person.",
            "Ecstasy is joy at maximum volume; envy is the informative opposite-neighbor - joy seen from outside.",
        ],
        "requirements": [
            "Eight neighbors mapped: contentment, pride, amusement, relief, gratitude, hope, love, ecstasy, plus envy as opposite-neighbor.",
            "Each neighbor defined as joy plus/minus one appraisal ingredient.",
            "A concrete discrimination test for the closest pairs (especially joy vs contentment).",
            "The ingredient-question method: who did it? funny? thanks owed? future?",
            "Descriptive-mapping boundary: no labeling of real people.",
        ],
        "standards": [
            "Dyad logic follows Plutchik 1980: joy plus trust as love, adjacent blends.",
            "Ingredient-appraisal analysis follows Lazarus 1991 and Scherer 2005.",
            "Circumplex neighbor relations follow Russell 1980.",
        ],
        "citations": [CIT_PLUTCHIK, CIT_LAZARUS, CIT_SCHERER],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "mixes",
        "name": "Joy Blends: Emotion Mixes, Plutchik-Style",
        "group": "Related Emotions and Mixes",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Pure joy is the laboratory case; lived joy is usually a "
            "blend. Plutchik's dyad logic - neighboring primaries "
            "combining into named compounds - gives the classic menu, "
            "and joy stars in several. Joy plus trust is love: the warm "
            "affiliative glow directed at a person - the feeling at the "
            "wedding, the reunion, the birth - gladness braided with "
            "safety. Joy plus anticipation is optimism: the bright "
            "forward lean - glad about now and confident about next; the "
            "morning-anticipation tint from the day vignette is optimism "
            "in daily dress. Joy plus surprise is delight: the "
            "unbudgeted good landing all at once - brighter, more "
            "physical, more laugh-prone than planned-for joy. Joy plus "
            "sadness is the bittersweet blend: the graduation, the last "
            "day, the child leaving home - gladness and ache held at "
            "once, each sharpening the other, the blend people describe "
            "as the most meaningful feeling there is. Joy plus anger's "
            "opposite... more usefully: joy plus fear (the roller "
            "coaster, the stage before the applause) is the thrill "
            "blend - activation from both, pleasantness winning. Each "
            "blend has its own face, body, and behavior: delight laughs "
            "harder, optimism plans, love embraces, bittersweet tears "
            "while smiling. The blender's rule: name both ingredients "
            "and the blend explains itself - the feeling is never "
            "mysterious once its components are on the table. These are "
            "described simulations of blends, not analyses of real "
            "people's feelings."
        ),
        "how_it_works": (
            "Blends work through appraisal summation on shared arousal. "
            "Each primary contributes its appraisal (joy: this is good; "
            "trust: this person is safe; anticipation: good is coming; "
            "surprise: this was unpredicted; sadness: something valued "
            "is lost; fear: threat is near) and its arousal contribution, "
            "and the feeling system integrates them into one state whose "
            "character reflects the mixture. Love feels warm and safe "
            "because joy's pleasantness sums with trust's safety while "
            "arousal stays moderate. Optimism leans forward because "
            "anticipation adds future-orientation to joy's present "
            "gladness. Delight startles because surprise adds the "
            "prediction-error spike to joy's pleasantness. Bittersweet "
            "aches because sadness's loss appraisal runs alongside "
            "joy's gain appraisal - the rare blend where the two "
            "valences coexist, which is why it feels deep rather than "
            "confused: both appraisals are true. Thrill buzzes because "
            "fear contributes arousal while joy's pleasantness wins the "
            "valence contest. The face and body of each blend are "
            "likewise summations: delight's harder laugh, love's embrace, "
            "bittersweet's tearful smile."
        ),
        "key_points": [
            "Joy plus trust is love: gladness braided with safety, directed at a person.",
            "Joy plus anticipation is optimism: the bright forward lean - glad now, confident about next.",
            "Joy plus surprise is delight: the unbudgeted good, brighter, more physical, more laugh-prone.",
            "Joy plus sadness is bittersweet: gladness and ache at once, each sharpening the other - often called the most meaningful feeling.",
            "The blender's rule: name both ingredients and the blend explains itself.",
        ],
        "requirements": [
            "Five named blends with both ingredients and the felt character of each.",
            "The thrill blend (joy plus fear) included as the arousal-sharing case.",
            "Each blend's distinctive face/body/behavior noted.",
            "The bittersweet mechanism: coexisting valences, both appraisals true.",
            "The blender's rule as the structural close; described-simulation boundary.",
        ],
        "standards": [
            "Dyad formation follows Plutchik 1980.",
            "Appraisal summation follows Lazarus 1991 and Scherer 2005.",
            "Bittersweet co-activation follows the mixed-emotions literature.",
        ],
        "citations": [CIT_PLUTCHIK, CIT_LAZARUS, CIT_SCHERER],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "full_simulation",
        "name": "The Full Joy Simulation: From Trigger to Resolution",
        "group": "Related Emotions and Mixes",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "This is the archive's showcase: joy simulated end to end, "
            "every system from the earlier records running at once. "
            "Scene one, the trigger: Maya has been waiting three weeks "
            "for the message about the community garden grant - the "
            "anticipation record's forward lean, the personal-stakes "
            "appraisal primed. The phone buzzes at 2:14 PM. Scene two, "
            "onset: she reads the first line - \"we are delighted to\" - "
            "and the appraisal fires before comprehension finishes: "
            "breath catches, chest warms, the AU12+AU6 assembly lands on "
            "her face uncommanded. Scene three, the peak: she is on her "
            "feet without deciding to stand, laughing the bright "
            "surprise-laugh of delight (joy plus surprise - the "
            "prediction-error bonus, since she had braced for no), "
            "calling her co-organizer with the announcement phrasing - "
            "\"you won't believe this\" - voice raised and quickened, "
            "the smile audible. Scene four, the blend: relief arrives "
            "underneath as the three-week tension exhales out of her "
            "shoulders - joy-with-relief, the best kind of tired "
            "already forming - and gratitude braids in toward the "
            "funder: joy plus trust plus benefactor, the love-adjacent "
            "warmth. Scene five, the cascade: she tells the team; the "
            "contagion loop runs; the evening meeting becomes a small "
            "celebration with the toast and the marking; the generous "
            "moves appear - she stays late helping a neighbor with "
            "their plot. Scene six, the fade and banking: by night the "
            "peak has settled into the warm glow; she writes the "
            "journal line, sends the thank-you, replays the phone call "
            "twice - savoring converting peak into trigger. Scene "
            "seven, the aftershock: for days the memory re-warms on "
            "recall; the garden itself becomes a personal trigger; "
            "next season's baseline sits slightly higher. Every record "
            "in this database appears in the seven scenes: definition, "
            "family, intensity, myth (she had braced - the myth that "
            "hope is dangerous - and the record corrects it), the "
            "first-person texture, the time course, the snapshots, the "
            "blend, the vignette structure, the body, the posture, the "
            "sleep that night (bright, short, normal), the individual "
            "grain (she runs hot - tearful at the edges), the face, "
            "its scaling, the nearly-hidden joy in the serious meeting "
            "that afternoon (suppressed, leaking at the mouth corners), "
            "the artist's notes incarnate, the classic triggers "
            "(achievement, good news, giving), the personal ones (the "
            "garden's smell), the surprise (the timing), the chain "
            "reactions, the actions, the speech, the decisions (she "
            "says yes to expanding the plots - optimistic, checkpointed), "
            "the full-volume behavior (kept to the wedding-zone by the "
            "team's ritual), the healthy expression (said, shown, "
            "channeled, banked), the costs avoided, the practices "
            "embodied, the reading (her co-organizer reads her face "
            "instantly), the support (active-constructive, the story "
            "asked for twice), the mistakes avoided, the neighbors "
            "(optimism, delight, gratitude distinguished), the blends "
            "named. A described simulation for education - Maya is an "
            "illustrative figure, not a real person, and nothing here "
            "diagnoses anyone."
        ),
        "how_it_works": (
            "The showcase works by running the database's full causal "
            "chain in one continuous timeline, so the reader sees the "
            "records not as isolated topics but as one system. The "
            "trigger scene runs anticipation-primed appraisal; onset "
            "runs the fast appraisal-to-feeling sequence with the "
            "Duchenne assembly; the peak runs arousal discharge plus "
            "the delight blend plus broadcast speech; the blend scene "
            "runs appraisal summation (relief underneath, gratitude "
            "braiding in); the cascade scene runs all four chain "
            "mechanisms (priming, contagion, behavioral mediation, "
            "memory banking); the fade scene runs the arousal-cost "
            "settling plus deliberate savoring and reconsolidation; "
            "the aftershock scene runs the trigger-formation loop that "
            "raises the next baseline. The embedded cross-references "
            "work as a teaching-ladder demonstration: the simple "
            "records (definition, face, triggers) appear as the "
            "simulation's visible surface, the compounded records "
            "(body, blends, chains) as its machinery, and the advanced "
            "records (expression stewardship, decision checkpointing, "
            "cascade management) as its wisdom layer. Maya being "
            "illustrative rather than real keeps the simulation inside "
            "the descriptive boundary: every mechanism shown is general, "
            "none is a claim about a person."
        ),
        "key_points": [
            "Seven scenes: trigger, onset, peak, blend, cascade, fade-and-banking, aftershock - the full time course in one timeline.",
            "Every earlier record appears as a working part: the face assembly, the blends, the chains, the expression channels, the decision checkpoint.",
            "The simulation demonstrates the teaching ladder: simple records as surface, compounded as machinery, advanced as wisdom.",
            "Maya runs hot (tearful-edged), suppresses joy once in a serious meeting (leaking at the mouth corners), checkpoints the optimistic decision.",
            "Maya is an illustrative figure, not a real person: every mechanism general, none a claim about anyone.",
        ],
        "requirements": [
            "Seven named scenes in order, each running specific mechanisms from earlier records.",
            "Explicit cross-references to the earlier records woven into the scenes.",
            "The three ladder layers mapped onto the simulation (surface/machinery/wisdom).",
            "Individual grain included (runs hot; one suppression moment; one checkpointed decision).",
            "The illustrative-figure boundary stated: not a real person, no diagnosis.",
        ],
        "standards": [
            "Causal-chain integration follows the appraisal-to-expression sequence in Scherer 2005.",
            "Blend and cascade mechanics follow Plutchik 1980 and Fredrickson 1998.",
            "Teaching-ladder demonstration follows the database's own ladder specification.",
        ],
        "citations": [CIT_SCHERER, CIT_PLUTCHIK, CIT_FREDRICKSON],
        "sig_lens": SIG_LENS_DEF,
    },
]
