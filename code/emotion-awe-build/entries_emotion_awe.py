#!/usr/bin/env python3
"""Entries for the Awe Emotion databases (Manon's 16:15 orders, emotion series batch 2).

Creates two NEW databases, 34 ladder-ordered records each:

  emotion-awe            - The Awe Emotion Database
                           (public-harvest: real, fact-checked psychology of
                           awe - definition, family placement, intensity,
                           first-person simulation, body signals, facial
                           expression, triggers, behavior, healthy
                           expression, recognition in others, related
                           emotions and mixes, and a full behavioral
                           simulation; descriptive and educational only -
                           never diagnosing real people; standard references
                           Keltner and Haidt 2003; Piff et al. 2015;
                           Shiota, Keltner and Mossman 2007; Maruskin,
                           Thrash and Elliot 2012; Gordon et al. 2017;
                           Rudd, Vohs and Aaker 2012; Ekman and Friesen FACS
                           1978; Russell circumplex 1980; Lazarus 1991;
                           Barrett 2017; Darwin 1872; APA Dictionary of
                           Psychology)
  emotion-awe-signature  - The Awe Emotion Signature Database
                           (his original Signature Awe Method: awe as the
                           wide-lens signal of the system - the mind
                           touching a scale larger than its own frame, the
                           self shrinking to make room, the engine going
                           quiet to listen; vastness the scale readout,
                           accommodation the refit crew, the small self the
                           cleared deck; src signature, titles suffixed
                           " (Signature Edition)", never presented as
                           authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
non-decreasing; ladder_tier foundations/compounded/advanced).
"""

SIG_TAIL = ("Signature original - his original Signature Awe Method: awe as "
            "the wide-lens signal of the system - the mind touching a scale "
            "larger than its own frame, the self shrinking to make room, "
            "the engine going quiet to listen; vastness the scale readout, "
            "accommodation the refit crew, the small self the cleared deck. "
            "Clearly labeled Signature-made, never presented as authentic "
            "public record.")

CIT_KELTNER_HAIDT = ("Keltner D, Haidt J. Approaching awe, a moral, "
                     "spiritual, and aesthetic emotion. Cogn Emot. "
                     "2003;17(2):297-314.")
CIT_PIFF = ("Piff PK, Dietze P, Feinberg M, Stancato DM, Keltner D. Awe, "
            "the small self, and prosocial behavior. J Pers Soc Psychol. "
            "2015;108(6):883-899.")
CIT_SHIOTA = ("Shiota MN, Keltner D, Mossman A. The nature of awe: "
              "elicitors, appraisals, and effects on self-concept. Cogn "
              "Emot. 2007;21(5):1157-1179.")
CIT_MARUSKIN = ("Maruskin LA, Thrash TM, Elliot AJ. The chills as a "
                "psychological construct: content universe, factor "
                "structure, affective composition, elicitors, trait "
                "antecedents, and consequences. J Pers Soc Psychol. "
                "2012;103(1):135-157.")
CIT_GORDON = ("Gordon AM, Stellar JE, Anderson CL, McNeil GD, Loew D, "
              "Keltner D. The dark side of the sublime: distinguishing a "
              "threat-based variant of awe. J Pers Soc Psychol. "
              "2017;113(2):310-328.")
CIT_RUDD = ("Rudd M, Vohs KD, Aaker J. Awe expands people's perception of "
            "time, alters decision making, and enhances well-being. "
            "Psychol Sci. 2012;23(10):1130-1136.")
CIT_STELLAR = ("Stellar JE, John-Henderson N, Anderson CL, Gordon AM, "
               "McNeil GD, Keltner D. Positive affect and markers of "
               "inflammation: discrete positive emotions predict lower "
               "levels of inflammatory cytokines. Emotion. "
               "2015;15(2):129-133.")
CIT_APA = ("American Psychological Association. APA Dictionary of "
           "Psychology. Awe entry: an emotion variously combining dread, "
           "veneration, and wonder that is inspired by authority or by the "
           "sacred or sublime.")
CIT_FACS = ("Ekman P, Friesen WV. Facial Action Coding System: A Technique "
            "for the Measurement of Facial Movement. Palo Alto: Consulting "
            "Psychologists Press; 1978.")
CIT_DARWIN = ("Darwin C. The Expression of the Emotions in Man and Animals. "
              "London: John Murray; 1872.")
CIT_RUSSELL = ("Russell JA. A circumplex model of affect. J Pers Soc Psychol. "
               "1980;39(6):1161-1178.")
CIT_LAZARUS = ("Lazarus RS. Emotion and Adaptation. New York: Oxford "
               "University Press; 1991.")
CIT_BARRETT = ("Barrett LF. How Emotions Are Made: The Secret Life of the "
               "Brain. Boston: Houghton Mifflin Harcourt; 2017.")

SIG_LENS_DEF = ("The Signature read: awe is the wide-lens signal of the "
                "system. Where public psychology charts the feeling, the "
                "Signature Awe Method treats awe as the mind touching a "
                "scale larger than its own frame - the self shrinking to "
                "make room, the engine going quiet to listen. Vastness is "
                "the scale readout, accommodation the refit crew, and the "
                "small self the cleared deck. Every awe record below "
                "carries the same public facts, reframed as his original "
                "Signature engineering of the feeling.")

ENTRIES = [
    # ------------------------------------------------ 1-4 WHAT AWE IS
    {
        "key": "definition",
        "name": "What Awe Is: A Plain-Language Definition",
        "group": "What the Emotion Is",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Awe is the feeling that arrives when you meet something vast "
            "that your mind cannot quite fit into its usual frames - a "
            "canyon rim dropping away below you, the night sky wheeling "
            "overhead, a cathedral of sound in a concert hall, a newborn's "
            "hand closing around a finger. In plain words, awe is the mind "
            "going quiet in front of something bigger than its own habits. "
            "Psychologists Dacher Keltner and Jonathan Haidt gave this "
            "feeling its modern definition in 2003: awe comes from two "
            "ingredients taken together - perceived vastness (something "
            "huge in size, scope, complexity, or meaning) and a need for "
            "accommodation (your mental frames have to stretch to take it "
            "in). That is why awe feels the way it does: vastness does the "
            "stopping, accommodation does the changing. Awe is not the same "
            "as ordinary surprise, though surprise can be one of its "
            "ingredients. Surprise is quick and gone; awe lingers, because "
            "the frame is still being rebuilt. It is not the same as fear "
            "either, though the two often arrive together - that pairing "
            "has its own name, threat-based awe, and its own record here. "
            "And it is not the same as admiration, which is aimed at "
            "another person; awe is aimed at the vastness itself. Everyone "
            "has felt it, because everyone has met something too big for "
            "the usual drawers. This database describes the emotion from "
            "every angle - what it is, how it feels, how it shows, and how "
            "it can be expressed well - purely as education and "
            "description. It never diagnoses anyone and never labels any "
            "real person."
        ),
        "how_it_works": (
            "Awe works as a two-part appraisal. First the mind registers "
            "vastness: something physical, social, or conceptual that is "
            "perceptually large, conceptually rich, or personally "
            "significant beyond the ordinary - the Grand Canyon, a "
            "symphony's climax, the idea of deep time. Second, the mind "
            "registers that its current frames cannot hold the thing "
            "without stretching - this is the need for accommodation, "
            "borrowed from the developmental psychologist Jean Piaget's "
            "word for updating mental models. When both register at once, "
            "the system does two things: it stills the body (to take the "
            "input in) and it shrinks the felt self (to make room). That "
            "shrunk self is the famous small-self effect: people in awe "
            "report feeling smaller, quieter, and more connected to "
            "something larger. The frame-stretching is the lasting part - "
            "after awe, the mental model is a little bigger than before, "
            "which is why awe experiences are remembered for years and "
            "often described as perspective-changing."
        ),
        "key_points": [
            "Awe is the mind going quiet in front of something bigger than its own habits: vastness plus the need to stretch your frames.",
            "Its two ingredients are perceived vastness and the need for accommodation (Keltner and Haidt 2003).",
            "Vastness does the stopping - the body stills; accommodation does the changing - the mental model grows.",
            "Awe is not surprise (which is quick and gone), not fear (though they often pair), and not admiration (which targets a person).",
            "The after-effect is the small self: feeling smaller, quieter, and more connected - plus a stretched mental frame that lasts.",
        ],
        "requirements": [
            "A plain-language definition an ordinary reader recognizes from their own life.",
            "The two-part Keltner-Haidt appraisal stated: perceived vastness plus need for accommodation.",
            "Clear separation from surprise, fear, and admiration.",
            "The small-self after-effect and the frame-stretching stated as the signature consequences.",
            "A stated educational boundary: description only, never diagnosis of any real person.",
        ],
        "standards": [
            "Definition follows Keltner and Haidt 2003: awe from perceived vastness and need for accommodation.",
            "Dictionary framing follows the APA Dictionary of Psychology awe entry.",
            "Appraisal account follows Lazarus 1991: emotions as signals of events appraised against goals and well-being.",
        ],
        "citations": [CIT_KELTNER_HAIDT, CIT_APA, CIT_LAZARUS],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "family",
        "name": "Where Awe Sits in the Emotion Family",
        "group": "What the Emotion Is",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Emotions are organized by psychologists the way colors are "
            "organized on a wheel: some are primaries, some are blends, and "
            "each sits at a fixed address with fixed neighbors. Awe is a "
            "complex emotion, not a basic one - it is built from simpler "
            "ingredients rather than arriving pre-assembled. Its nearest "
            "neighbors are wonder (curiosity leaning toward the vast), "
            "amazement (surprise leaning toward the vast), admiration (awe "
            "aimed at another person's excellence), and reverence (awe aimed "
            "at something held in deep respect). Fear sits close by too, "
            "which is why the threat-based variant of awe is so common: the "
            "same canyon that inspires can also intimidate. On Russell's "
            "circumplex, awe is harder to pin than joy, because its "
            "pleasantness swings: positive awe is pleasant and moderately "
            "activated, while threat-based awe is unpleasant and highly "
            "activated. What stays constant is the energy - awe always "
            "carries arousal - and the direction of attention: outward and "
            "upward, away from the self. Knowing the address is practical: "
            "it tells you what awe blends with most easily (fear makes the "
            "sublime; joy makes wonder; sadness makes the bittersweet "
            "sublime) and which cousins to check before naming the feeling. "
            "The confusion that matters most is awe versus admiration: if "
            "the feeling is aimed at a person's skill or virtue, it is "
            "admiration; if it is aimed at the vastness itself, it is awe."
        ),
        "how_it_works": (
            "The family placement works because awe is assembled, not "
            "atomic. Constructionist accounts like Barrett's describe the "
            "brain as building emotions from body signals, past experience, "
            "and concepts - and awe is a showcase case: the same vast "
            "stimulus can assemble into positive awe, threat-based awe, or "
            "mere surprise depending on the context the brain brings. The "
            "circumplex placement explains the two flavors: the energy "
            "stays high in both, but pleasantness swings with the appraisal "
            "of safety. The neighbor map explains the blends: neighbors on "
            "the wheel combine most naturally, so awe sits one step from "
            "wonder, amazement, admiration, reverence, and fear. And the "
            "complex-not-basic status explains the individual variation - "
            "because awe is assembled from parts, different people assemble "
            "it differently, which is why two people at the same canyon "
            "rim can feel two different things and both be right."
        ),
        "key_points": [
            "Awe is a complex emotion, assembled from simpler ingredients - not a basic emotion.",
            "Its nearest neighbors are wonder, amazement, admiration, reverence, and fear.",
            "On the circumplex, awe is always activated; its pleasantness swings between positive awe and threat-based awe.",
            "Attention always points outward and upward, away from the self - the signature of the address.",
            "Awe versus admiration: aimed at vastness itself it is awe; aimed at a person's excellence it is admiration.",
        ],
        "requirements": [
            "Awe's complex-not-basic status stated with the consequence: assembled differently by different people.",
            "The neighbor map: wonder, amazement, admiration, reverence, fear.",
            "Circumplex placement: high arousal in both flavors, pleasantness swinging with safety appraisal.",
            "The awe-versus-admiration distinction stated as a practical rule.",
            "Constructionist refinement acknowledged alongside the classic map.",
        ],
        "standards": [
            "Complex-emotion framing follows Keltner and Haidt 2003: awe as a response requiring accommodation.",
            "Quadrant logic follows Russell 1980: valence-by-arousal coordinates.",
            "Constructionist refinement follows Barrett 2017: emotions assembled from interoception, experience, and concepts.",
        ],
        "citations": [CIT_KELTNER_HAIDT, CIT_RUSSELL, CIT_BARRETT],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "intensity",
        "name": "Awe at Every Volume: Mild to Intense",
        "group": "What the Emotion Is",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Awe comes with a volume knob, and the same emotion at setting "
            "three and setting nine are genuinely different experiences. "
            "At the mild end is the glimpse: the brief widening at a "
            "sunset between buildings, a line of music that lifts the "
            "chest for a second, the small intake of breath at a clever "
            "idea. Mild awe is frequent, easy, and social - it is the "
            "stuff of shared looks and pointed fingers. In the middle "
            "sits bright awe: the full stop-and-stare, the goosebumps "
            "running up the arms, the mouth slightly open, the sense that "
            "time has slowed a notch. This is the Grand Canyon rim, the "
            "choir's final chord, the telescope's first clear ring of "
            "Saturn - awe doing its classic work. At the intense end is "
            "the overwhelming sublime: awe so strong the frame cannot "
            "stretch fast enough. The body freezes, the eyes water, the "
            "throat tightens, and the feeling tips toward fear - this is "
            "threat-based awe, where vastness outruns accommodation and "
            "the system registers danger alongside wonder. The knob is "
            "turned by two things: how vast the stimulus is, and how much "
            "stretching the current frame needs. A familiar sunset is a "
            "three; the same sunset seen for the first time after a year "
            "indoors can be an eight. Learning the knob matters because "
            "each band asks for something different: mild awe wants "
            "sharing, bright awe wants savoring, and intense awe wants "
            "grounding first."
        ),
        "how_it_works": (
            "Intensity in awe is driven by the gap between stimulus and "
            "frame. Small gap, small awe: the sunset fits existing frames "
            "of pretty skies, so the accommodation demand is low and the "
            "feeling stays mild. Large gap, large awe: the canyon does not "
            "fit any stored frame of big holes, so the accommodation "
            "demand spikes and the feeling runs hot. This is why novelty "
            "turns the knob so hard - the first view always outranks the "
            "hundredth - and why knowledge can turn it too: the geologist "
            "feels more awe at the canyon, not less, because her frames "
            "are richer and the gap, once measured, is larger. The "
            "threat-based tip-over happens when accommodation demand "
            "exceeds processing speed: the frame cannot stretch fast "
            "enough, the system flags uncertainty as danger, and fear "
            "joins the blend. Two dials run at once, felt versus shown: "
            "social rules can mute the visible awe (the visitor who "
            "pretends the canyon is no big deal), while the felt dial "
            "stays pegged."
        ),
        "key_points": [
            "Awe runs on a volume knob: mild glimpses, bright full-stop awe, and the overwhelming sublime are one emotion at different settings.",
            "The knob is turned by the gap between stimulus and frame: bigger gap, bigger awe.",
            "Novelty turns the knob up; deep knowledge can turn it up too, by making the gap measurable.",
            "Threat-based awe is the tip-over point: when the frame cannot stretch fast enough, fear joins the blend.",
            "Each band asks for something different: mild awe wants sharing, bright awe wants savoring, intense awe wants grounding first.",
        ],
        "requirements": [
            "Three bands named and distinguished: mild glimpses, bright awe, the overwhelming sublime.",
            "The frame-gap mechanism stated as the intensity driver.",
            "Novelty and knowledge both explained as knob-turners.",
            "The threat-based tip-over explained: accommodation demand exceeding processing speed.",
            "The felt-versus-shown two-dial point included.",
        ],
        "standards": [
            "Two-ingredient account follows Keltner and Haidt 2003: vastness plus need for accommodation.",
            "Threat-based variant follows Gordon et al. 2017: a distinct variant of awe with fear appraisals.",
            "Display-rule logic follows Ekman 1999 conventions on felt versus shown emotion.",
        ],
        "citations": [CIT_KELTNER_HAIDT, CIT_GORDON, CIT_SHIOTA],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "myths",
        "name": "Myths and Misunderstandings About Awe",
        "group": "What the Emotion Is",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Awe collects myths the way attics collect boxes, and the myths "
            "cost people the feeling. Myth one: awe requires mountains, "
            "cathedrals, or the cosmos. In truth the most common awe "
            "triggers in daily-life studies are ordinary - a kind act, a "
            "piece of music, a child's question, morning light doing "
            "something unexpected. Vastness is about the frame-gap, not "
            "the altitude. Myth two: awe is always pleasant. The research "
            "says otherwise: threat-based awe, with its fear and "
            "overwhelm, is a documented variant, and even bright awe "
            "carries an ache of smallness that not everyone enjoys. Myth "
            "three: awe is rare, a once-a-year event. Daily-diary studies "
            "find people report awe-like moments weekly when they are "
            "asked to notice - rarity is an attention problem, not a "
            "supply problem. Myth four: only deep or artistic people feel "
            "awe. Awe is standard human equipment; what varies is not "
            "capacity but noticing - and noticing is trainable. Myth five: "
            "awe makes you passive and small in a bad way. The small self "
            "is real, but the research links it to generosity, humility, "
            "and connection, not helplessness - Piff and colleagues showed "
            "awe reliably increases prosocial behavior. Myth six: you "
            "cannot seek awe on purpose; it must ambush you. Planned awe "
            "works fine - the telescope was booked, the trail was chosen, "
            "and the feeling arrived on schedule. Clearing the attic does "
            "not make awe smaller; it makes it available."
        ),
        "how_it_works": (
            "Myths work by setting false appraisal rules, and appraisal "
            "rules gate emotion. If the rule says awe requires the Grand "
            "Canyon, the mind files the morning-light moment under "
            "pretty instead of awe, and the accommodation - the lasting "
            "frame-stretch - never gets its chance. Each myth in this "
            "record names the false rule and the real one: vastness is "
            "frame-relative, not altitude-absolute; pleasantness swings "
            "with the safety appraisal; frequency follows attention; "
            "capacity is universal and noticing is trainable; the small "
            "self predicts generosity, not passivity; and intention does "
            "not spoil the feeling. Naming the rule is the intervention: "
            "once the mind knows that a child's question counts, it "
            "starts counting them, and the count itself feeds the "
            "emotion. That is why the myths section sits in the "
            "foundations tier - it is load-bearing for everything after."
        ),
        "key_points": [
            "Awe does not require mountains: the frame-gap is relative, and daily life supplies vastness constantly.",
            "Awe is not always pleasant: threat-based awe with fear is a documented variant.",
            "Awe is not rare: diary studies find weekly awe-like moments once people are asked to notice.",
            "Awe capacity is universal; what varies is noticing, and noticing is trainable.",
            "The small self predicts generosity and connection, not passivity; and planned awe works fine.",
        ],
        "requirements": [
            "Six myths named, each paired with the research-backed correction.",
            "The frame-relative nature of vastness used to retire the mountains-only myth.",
            "Threat-based awe cited to retire the always-pleasant myth.",
            "Diary-study frequency used to retire the rarity myth.",
            "The mechanism stated: false appraisal rules gate the emotion, and naming them is the intervention.",
        ],
        "standards": [
            "Daily-frequency claim follows Shiota, Keltner and Mossman 2007 on awe elicitors in everyday life.",
            "Prosocial consequence follows Piff et al. 2015: awe, the small self, and prosocial behavior.",
            "Threat-based variant follows Gordon et al. 2017.",
        ],
        "citations": [CIT_SHIOTA, CIT_PIFF, CIT_GORDON],
        "sig_lens": SIG_LENS_DEF,
    },

    # ------------------------------------------------ 5-9 HOW IT FEELS
    {
        "key": "first_person",
        "name": "Inside Awe: A First-Person Passage",
        "group": "How It Feels",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "From the inside, awe feels like this. You come around the "
            "bend and the canyon is simply there - too much, too fast, "
            "too far down. The first thing that happens is nothing: your "
            "feet stop, your hands go still, the sentence you were saying "
            "dies halfway out. Then the breath changes - a short catch, "
            "then a long slow draw in, as if the body is trying to take "
            "the whole thing in at once. The eyes widen and stay wide; "
            "the brows lift; the mouth comes slightly open without "
            "permission. A shiver runs up the back of the arms - not cold, "
            "not exactly, just the skin registering something the mind has "
            "not finished. Thoughts thin out. The usual running commentary "
            "- the errands, the arguments, the plans - goes silent, and "
            "in its place there is a single stretched feeling of "
            "smallness, not the bad kind, the quiet kind: you are very "
            "little and the world is very large and somehow that is a "
            "relief. Time slows. A minute at the rim feels like five. "
            "And underneath it all there is a pull - toward the edge, "
            "toward the others standing there, toward saying something "
            "out loud even though no words fit, so what comes out is "
            "\"wow,\" breathed, not spoken. This is positive awe at full "
            "strength: stillness, wideness, smallness, and the pull to "
            "share. Nobody in this passage is diagnosed with anything; "
            "this is what the research says the inside of the feeling "
            "reports, described so a reader can recognize it and a "
            "simulator can stage it."
        ),
        "how_it_works": (
            "The first-person texture works because each inner event maps "
            "to a mechanism. The stop - feet, hands, speech - is the "
            "orienting freeze: the system halts motor output to free "
            "attention for the vast input. The breath change is the body "
            "shifting into intake mode: slow deep breaths accompany "
            "absorbed attention. The wide eyes and lifted brows are the "
            "face maximizing the intake aperture. The shiver is "
            "piloerection - goosebumps - the classic awe chills documented "
            "by Maruskin and colleagues as a marker of being moved by "
            "vastness. The thinning of thought is the small self: the "
            "default-mode self-narrative quiets, and attention goes "
            "outward. The slowed time is the Rudd, Vohs and Aaker effect: "
            "awe expands perceived time because attention is fully "
            "present. And the pull to share is the social function: awe "
            " evolved to be told, which is why the passage ends at "
            "\"wow.\" The passage is a composite of these reported and "
            "measured components - a simulation script, not a person."
        ),
        "key_points": [
            "The inside of awe opens with stillness: feet stop, hands still, speech dies - the orienting freeze freeing attention.",
            "The body shifts into intake: breath deepens, eyes widen, brows lift, the mouth opens slightly.",
            "Goosebumps and chills mark the peak: the skin registering what the mind has not finished.",
            "Thought thins and time slows: the small self quiets the commentary and attention goes fully present.",
            "It ends in a pull: toward the edge, toward others, toward a breathed 'wow' - awe evolved to be shared.",
        ],
        "requirements": [
            "A continuous first-person passage, sensory and concrete, not a list.",
            "The signature beats present: stillness, intake, chills, small self, slowed time, the pull to share.",
            "Each beat traceable to a published mechanism, stated in how_it_works.",
            "No real person described; the passage is a composite simulation script.",
            "The educational boundary implicit in the final sentence: description, not diagnosis.",
        ],
        "standards": [
            "Chills description follows Maruskin, Thrash and Elliot 2012 on the chills as a psychological construct.",
            "Time expansion follows Rudd, Vohs and Aaker 2012: awe expands perceived time.",
            "Small-self mechanism follows Piff et al. 2015.",
        ],
        "citations": [CIT_MARUSKIN, CIT_RUDD, CIT_PIFF],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "time_course",
        "name": "The Time Course of Awe: Onset, Peak, and Fade",
        "group": "How It Feels",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "Awe has a shape in time, and knowing the shape lets you "
            "recognize where you are inside it. Onset is fast - the first "
            "sight of the vast thing lands in under a second, and the "
            "body answers before thought does: the stop, the catch of "
            "breath, the widening. This is the fastest part of the "
            "feeling and the most physical. The climb to peak takes "
            "longer, roughly half a minute to a few minutes: the mind "
            "keeps taking in more of the vastness - the canyon gets "
            "deeper the longer you look, the chord keeps resolving - and "
            "the accommodation demand rises with it. Peak is the "
            "overwhelm point: maximum stillness, maximum smallness, the "
            "chills at their strongest, the frame stretching at full "
            "speed. For most everyday awe the peak passes in minutes; "
            "for the great ones - the eclipse, the birth - it can hold "
            "for the better part of an hour, waxing and waning. The fade "
            "is slower than the onset and gentler than the peak: the "
            "body loosens first, then speech returns in fragments "
            "(\"that was... I can't...\"), then the commentary mind "
            "boots back up. What does not fade on the same schedule is "
            "the aftershock. Hours later the memory replays uninvited; "
            "days later the perspective shift is still there - the "
            "problems that felt huge feel right-sized. The aftershock is "
            "the accommodation settling: the frame, stretched, does not "
            "fully spring back. That is why people remember exactly "
            "where they were when the big awe hit, years later, the way "
            "they remember little else."
        ),
        "how_it_works": (
            "The time course works because the two ingredients run on "
            "different clocks. Vastness registration is fast - perception "
            "flags the scale mismatch almost immediately, which is why "
            "onset is physical and pre-verbal. Accommodation is slow - "
            "updating mental models takes sustained processing, which is "
            "why the climb and the peak stretch over minutes and why the "
            "aftershock outlasts the feeling itself. The fade is the "
            "system declaring the frame updated enough to resume normal "
            "operations: motor output unlocks, speech returns, the "
            "default-mode narrative reboots. The aftershock is "
            "consolidation: the stretched frame gets written into long-"
            "term structure, which is why awe memories are unusually "
            "durable and why the perspective shift persists. Threat-based "
            "awe follows the same curve but with a sharper peak and a "
            "longer aftershock - fear consolidates harder, so the memory "
            "burns deeper."
        ),
        "key_points": [
            "Onset is fast and physical: under a second, the stop and the catch of breath arrive before thought.",
            "The climb to peak takes minutes: the mind keeps taking in more vastness and the accommodation demand rises.",
            "Peak is maximum stillness, maximum smallness, strongest chills - the frame stretching at full speed.",
            "The fade is gentle: body loosens, speech returns in fragments, the commentary mind reboots.",
            "The aftershock outlasts the feeling: replayed memories for hours, a right-sized perspective for days, durable memories for years.",
        ],
        "requirements": [
            "Five phases named and timed: onset, climb, peak, fade, aftershock.",
            "Onset explained as fast perception; climb and aftershock explained as slow accommodation.",
            "The aftershock given its mechanism: consolidation of the stretched frame.",
            "Threat-based awe's sharper peak and longer aftershock noted.",
            "The durable-memory fact included: people remember where they were for years.",
        ],
        "standards": [
            "Two-clock account follows Keltner and Haidt 2003: fast vastness registration, slow accommodation.",
            "Aftershock durability follows Shiota, Keltner and Mossman 2007 on awe and self-concept effects.",
            "Threat-based consolidation follows Gordon et al. 2017.",
        ],
        "citations": [CIT_KELTNER_HAIDT, CIT_SHIOTA, CIT_GORDON],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "low_vs_high",
        "name": "Low Awe and High Awe: Two Lived Snapshots",
        "group": "How It Feels",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "The same emotion at two volumes, side by side. LOW AWE, "
            "Tuesday, 7:40 in the morning. The kitchen window faces east "
            "and the sunrise is doing something unusual with the clouds - "
            "a band of rose-gold under a slab of gray. You stop mid-pour "
            "of the coffee. The brows lift a fraction, the breath catches "
            "once, and there is a small widening, a small quieting. You "
            "think, \"look at that,\" and you say it out loud to no one, "
            "and you take the phone out and photograph it, and by the "
            "time the coffee is poured the moment is over. It lasted "
            "maybe twenty seconds. The day goes on unchanged, except "
            "that at noon you are still faintly glad you looked. That is "
            "low awe: brief, mild, social, gone by breakfast - and real. "
            "HIGH AWE, Saturday, 11:15 at night. The observatory's "
            "telescope is finally pointed at Saturn and it is your turn "
            "at the eyepiece. You bend, you look - and there it is, "
            "impossibly crisp, a ringed jewel hanging in blackness, "
            "realer than every photograph. Your knees go weak. Your hand "
            "grips the rail. The breath stops entirely for three seconds, "
            "then comes back ragged. Goosebumps sheet up both arms. Your "
            "mouth is open and you do not close it. The small self "
            "arrives like a tide: you are nothing, a mote, and the "
            "nothingness is not frightening but flooding - a fullness, "
            "awe with joy braided through it. You straighten up and your "
            "eyes are wet and you laugh once, disbelieving, and the "
            "person behind you whispers \"oh my God\" and you nod because "
            "there is nothing else. You will remember this night in "
            "thirty years. That is high awe: total, physical, "
            "perspective-rewriting, and permanent in memory. Same "
            "emotion. Same machinery. Different volume, different life "
            "of the moment after."
        ),
        "how_it_works": (
            "The two snapshots work as a controlled comparison: same "
            "emotion, same appraisal structure, different frame-gap. In "
            "the sunrise the gap is small - the sky fits existing frames "
            "with one novel band of color, so accommodation demand is "
            "low, the body response is a whisper, and the aftershock is "
            "a faint gladness at noon. In the Saturn view the gap is "
            "enormous - no stored frame holds a live ringed planet - so "
            "accommodation demand spikes, the body goes full intake and "
            "freeze, the small self floods in, and consolidation writes "
            "a thirty-year memory. The snapshots also show the social "
            "difference: low awe is shared casually (the photograph, the "
            "remark to no one); high awe is shared reverently (the "
            "whisper, the nod). And they show the time difference: "
            "seconds versus a permanent entry in the autobiography. The "
            "comparison teaches the knob better than any dial diagram "
            "because the reader has lived both."
        ),
        "key_points": [
            "Low awe is the sunrise through the kitchen window: twenty seconds, a caught breath, a photograph, a faint gladness at noon.",
            "High awe is Saturn in the eyepiece: weak knees, stopped breath, sheeting goosebumps, wet eyes, a thirty-year memory.",
            "Same machinery, different frame-gap: the sunrise needs a small stretch, Saturn needs a total refit.",
            "Sharing differs by volume: low awe is remarked casually, high awe is whispered reverently.",
            "The aftershock scales with the volume: hours of gladness versus a permanent autobiographical entry.",
        ],
        "requirements": [
            "Two concrete, sensory, time-stamped snapshots - one low, one high.",
            "Both traceable to the same appraisal structure with different frame-gaps.",
            "The social and memory differences between volumes made explicit.",
            "No real persons; both are composite illustrative scenes.",
            "The comparison explicitly teaches the intensity knob.",
        ],
        "standards": [
            "Frame-gap account follows Keltner and Haidt 2003.",
            "Memory durability follows Shiota, Keltner and Mossman 2007.",
            "Time and self effects follow Rudd, Vohs and Aaker 2012 and Piff et al. 2015.",
        ],
        "citations": [CIT_KELTNER_HAIDT, CIT_SHIOTA, CIT_RUDD],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "awe_fear_blend",
        "name": "Awe Mixed with Fear: The Most Common Pairing",
        "group": "How It Feels",
        "ladder_rank": 5,
        "ladder_tier": "foundations",
        "description": (
            "Awe's most common partner is fear, and the blend has a name: "
            "the sublime. Stand at the canyon rim and feel the pull of "
            "the drop as well as the glory of the view; watch the storm "
            "front stack up black over the plains; stand under the "
            "skyscraper and feel your neck crane and your stomach tighten "
            "at once. The blend is not a malfunction - it is the "
            "threat-based variant of awe that Gordon and colleagues "
            "documented, distinct from the purely positive kind. From the "
            "inside it feels like this: the wideness is all there - the "
            "eyes wide, the breath caught, the small self - but braided "
            "through it is a wire of alarm. The body wants to approach "
            "and withdraw at the same time, so it does neither fully: "
            "you lean toward the rail and grip it harder. Thoughts split "
            "between \"this is incredible\" and \"this could kill me,\" "
            "and the split is the signature of the blend. The ratio "
            "matters. Mostly-awe with a thread of fear is the classic "
            "sublime - thrilling, memorable, sought out. Mostly-fear "
            "with a thread of awe is something else: the tornado on the "
            "horizon is awesome in the old sense and terrifying in the "
            "immediate one, and the wise response is the car, not the "
            "camera. Learning to read the ratio is the practical skill "
            "here: the body reports both signals honestly, and the "
            "reader's job is to hear which one is louder. The blend is "
            "also the doorway to courage: people who have stood in the "
            "sublime and stayed - the rail gripped, the breath managed - "
            "report a specific confidence afterward, as if the frame, "
            "stretched under load, came back stronger."
        ),
        "how_it_works": (
            "The blend works because vastness and threat share an "
            "appraisal ancestor: both flag that the current frame is "
            "inadequate to what is in front of you. In positive awe the "
            "inadequacy reads as \"stretch to meet this\"; in threat-based "
            "awe it reads as \"this could overwhelm you.\" The body "
            "runs both programs at once - approach (lean in, gaze, "
            "intake) and withdrawal (grip, freeze, muscle tension) - "
            "which is why the blend feels like being pulled in two "
            "directions. The ratio is set by the safety appraisal: "
            "perceived control and distance tilt it toward the sublime, "
            "perceived helplessness tilts it toward fear. Gordon and "
            "colleagues showed the threat-based variant is not just "
            "\"awe plus a little fear\" but a distinct profile with its "
            "own appraisals, physiology, and consequences - including a "
            "stronger small-self effect and, afterward, the load-tested "
            "confidence. The blend is the most common because the "
            "world's vast things are very often also its dangerous "
            "things: oceans, storms, heights, crowds, the night."
        ),
        "key_points": [
            "Awe's most common partner is fear, and the blend is the sublime - well-documented as threat-based awe.",
            "From the inside: all the wideness of awe braided with a wire of alarm; the body leans in and grips the rail at once.",
            "The ratio is the skill: mostly-awe is thrilling and sought; mostly-fear is a signal to withdraw, not to savor.",
            "Safety appraisal sets the ratio: perceived control tilts toward the sublime, helplessness toward fear.",
            "Afterward comes load-tested confidence: the frame stretched under load comes back stronger.",
        ],
        "requirements": [
            "The blend named (the sublime / threat-based awe) and its status as the most common pairing stated.",
            "A first-person-feel description of the dual pull: approach and withdrawal at once.",
            "The ratio rule stated plainly: read which signal is louder and act accordingly.",
            "The safety-appraisal mechanism given as the ratio-setter.",
            "The after-effect (load-tested confidence) included.",
        ],
        "standards": [
            "Threat-based variant follows Gordon et al. 2017: distinct profile with fear appraisals.",
            "Two-ingredient base follows Keltner and Haidt 2003.",
            "Approach-withdrawal framing follows Lazarus 1991 on core relational themes.",
        ],
        "citations": [CIT_GORDON, CIT_KELTNER_HAIDT, CIT_LAZARUS],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "day_vignette",
        "name": "A Day with Awe: An Ordinary Day Vignette",
        "group": "How It Feels",
        "ladder_rank": 5,
        "ladder_tier": "foundations",
        "description": (
            "Awe does not only visit on vacation; it threads an ordinary "
            "day if the noticing is switched on. Morning: the bus is "
            "late, you are annoyed, and then a child two seats up asks "
            "her mother, in a carrying voice, whether the clouds get "
            "tired of being up so high. The whole back of the bus "
            "smiles. Your annoyance does not vanish, but it gets "
            "smaller, set beside a question no adult would think to ask - "
            "a small frame-gap, a small awe, twenty seconds. Midday: the "
            "office hallway, where a colleague has pinned a photograph "
            "from the new space telescope - a field of galaxies, each "
            "smudge a hundred billion suns. You stop. People edge around "
            "you. For a full minute the deadlines go quiet and there is "
            "only the vertigo of scale, the small self arriving politely "
            "between meetings. You take a photo of the photo. Afternoon: "
            "the thunderstorm builds over the parking lot, black and "
            "towering, and everyone drifts to the windows. The first "
            "crack of thunder rolls through the building's bones and "
            "someone says \"whoa\" and nobody is embarrassed - threat-"
            "based awe, mild, shared, the sublime doing team-building. "
            "Evening: on the walk home a street musician is playing "
            "something with a cello that stops you mid-step. The music "
            "does the frame-stretching without any vast landscape at "
            "all - vastness of feeling, vastness of craft. You stand "
            "until the piece ends, you put money in the case, and you "
            "walk the rest of the way home slightly taller and slightly "
            "smaller at once. Night: from the porch, the sky is clear "
            "enough for the Milky Way's faint band. You look up longer "
            "than you meant to. Five moments, none planned, none "
            "requiring travel or money. The day was ordinary. The awe "
            "was not."
        ),
        "how_it_works": (
            "The vignette works by demonstrating the myth-busting in "
            "action: every trigger in the day is ordinary, local, and "
            "free, yet each carries a genuine frame-gap. The child's "
            "question is conceptual vastness - a novel frame on a "
            "familiar thing. The telescope photo is scale vastness "
            "delivered by proxy. The thunderstorm is threat-based "
            "vastness with the safety of walls. The cello is aesthetic "
            "vastness - craft and feeling exceeding the frame. The Milky "
            "Way is the classic, available nightly. The day also shows "
            "the social function running throughout: the bus smiles "
            "together, the windows gather a crowd, the \"whoa\" is "
            "communal. And it shows the noticing mechanism: none of "
            "these moments were sought, but all were caught - the "
            "trainable skill the myths record names. The vignette is the "
            "foundations tier's proof of concept: awe is not a "
            "destination, it is a setting on the attention."
        ),
        "key_points": [
            "An ordinary day holds five genuine awe moments: a child's question, a telescope photo, a thunderstorm, a cello, the Milky Way.",
            "Every trigger is ordinary, local, and free - vastness is frame-relative, not altitude-absolute.",
            "The social function runs all day: the bus smiles together, the windows gather a crowd, the 'whoa' is communal.",
            "None were sought, all were caught: noticing is the trainable skill.",
            "The proof of concept: awe is not a destination, it is a setting on the attention.",
        ],
        "requirements": [
            "A full day arc, morning to night, with at least five distinct awe moments.",
            "Each moment carrying a different kind of vastness (conceptual, scale, threat-based, aesthetic, classic).",
            "The social/shared dimension visible in at least two moments.",
            "The noticing-as-skill theme explicit.",
            "No real persons; composite illustrative scenes.",
        ],
        "standards": [
            "Everyday elicitors follow Shiota, Keltner and Mossman 2007.",
            "Noticing mechanism follows the diary-study frequency literature on awe in daily life.",
            "Social function follows Piff et al. 2015 on awe and connection.",
        ],
        "citations": [CIT_SHIOTA, CIT_PIFF, CIT_KELTNER_HAIDT],
        "sig_lens": SIG_LENS_DEF,
    },

    # ------------------------------------------------ 10-13 BODY SIGNALS
    {
        "key": "body",
        "name": "What Awe Does in the Body",
        "group": "Body Signals",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Awe writes itself across the body in a signature pattern. "
            "The skin goes first and most famously: goosebumps rise on "
            "the arms, the back of the neck, sometimes the scalp - "
            "piloerection, the hair standing up, accompanied by the "
            "shiver called chills. Maruskin and colleagues documented "
            "chills as a marker of being moved by vastness, and they "
            "arrive in waves, strongest at the peak. The breath changes "
            "next: a short catch at onset, then slow deep draws as the "
            "system shifts into intake mode. The heart's behavior is "
            "less dramatic than in fear - no pounding sprint - but the "
            "rate often slows slightly as attention locks outward; the "
            "body is not preparing to run, it is preparing to receive. "
            "The muscles do something distinctive: they still. Hands "
            "stop mid-gesture, the stride halts, the shoulders drop a "
            "fraction as the orienting freeze takes hold. The stomach "
            "may flutter or drop - the classic lurch at heights, the "
            "hollow feeling when scale registers. The throat tightens in "
            "strong awe, which is why voices come out hushed or break; "
            "the eyes water in many people at peak, not from sadness "
            "but from the sheer pressure of the intake. Energy after "
            "awe is unusual: not the buzz of excitement, not the drain "
            "of fear, but a quiet fullness - the body tired the way it "
            "is tired after deep attention, and oddly rested at the "
            "same time. None of this is a medical claim about any "
            "reader; it is the documented pattern, described so it can "
            "be recognized and simulated."
        ),
        "how_it_works": (
            "The body pattern works as an intake-and-stillness program. "
            "Goosebumps are the ancient mammalian response to the "
            "sublime - in our furry ancestors piloerection made the "
            "animal look larger before something vast; in us it "
            "remains as the skin's applause meter for vastness. The "
            "breath shift serves attention: slow deep breathing "
            "accompanies absorbed focus and damps the sympathetic "
            "surge, which is why awe feels still rather than frantic. "
            "The heart's slight slowing is the orienting response - "
            "the cardiac signature of attention locking onto a "
            "stimulus, the opposite of the fight-or-flight "
            "acceleration. The muscular stilling frees processing: "
            "with motor output halted, more bandwidth goes to the "
            "accommodation work. The throat tightening and eye "
            "watering at peak are spillover - the system running at "
            "full intake with the overflow valves open. The quiet "
            "fullness afterward is the parasympathetic rebound: the "
            "frame updated, the system stands down into a restful "
            "alertness that people describe as peace."
        ),
        "key_points": [
            "Goosebumps and chills are the signature skin response: the body's applause meter for vastness, strongest at peak.",
            "Breath shifts into intake mode: a catch at onset, then slow deep draws as attention locks.",
            "The heart often slows slightly - the orienting response - because the body prepares to receive, not to run.",
            "Muscles still: hands stop, stride halts, shoulders drop - motor output halted to free accommodation bandwidth.",
            "Afterward comes quiet fullness: tired like after deep attention, rested like after peace - the parasympathetic rebound.",
        ],
        "requirements": [
            "Six body systems covered: skin, breath, heart, muscles, stomach/throat, and post-awe energy.",
            "Chills documented with the Maruskin reference.",
            "The stillness distinguished from fear's freeze: intake-oriented, not escape-oriented.",
            "Each signal given its functional explanation in how_it_works.",
            "No medical claims about the reader; the pattern described as documented and recognizable.",
        ],
        "standards": [
            "Chills account follows Maruskin, Thrash and Elliot 2012.",
            "Orienting-response framing follows the psychophysiology of attention (cardiac deceleration with stimulus intake).",
            "Intake-versus-action distinction follows Lazarus 1991 on action tendencies.",
        ],
        "citations": [CIT_MARUSKIN, CIT_LAZARUS, CIT_KELTNER_HAIDT],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "posture",
        "name": "The Posture and Movement of Awe",
        "group": "Body Signals",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Watch a person in awe from across the room and the posture "
            "tells the story before the face does. The first thing is "
            "the stop: mid-step, mid-gesture, mid-sentence, the body "
            "arrests. Then the orientation: the head tilts up and the "
            "gaze lifts - awe looks up, toward the sky, the rim, the "
            "vaulted ceiling, the screen. The chin rises, the neck "
            "extends, the whole upper body opens toward the vast thing "
            "like a plant toward light. The arms do one of two things: "
            "they hang loose and still at the sides, forgotten, or they "
            "rise slightly, hands open, in the ancient gesture of "
            "receiving. The mouth comes open a fraction - not the yawn "
            "of boredom, the aperture of intake. As the feeling deepens, "
            "the body gets smaller in a specific way: the shoulders round "
            "forward a touch, the chest narrows, the person seems to "
            "take up less room - the postural form of the small self. "
            "Movement, when it returns, is slow: the awed person drifts "
            "rather than walks, turns the head slowly to take in more, "
            "reaches out a hand toward the vast thing without thinking "
            "about touching it. In threat-based awe the posture adds the "
            "grip: hands find the rail, the wall, another person's arm - "
            "approach and anchor at once. Actors and artists take note: "
            "the two tells that read most clearly at distance are the "
            "arrest (everything stops) and the lift (everything tilts "
            "up). Get those two and the audience feels the awe before a "
            "single facial muscle moves."
        ),
        "how_it_works": (
            "The posture works as a single intake-and-shrink program. "
            "The arrest is the orienting freeze: stopping movement is "
            "the cheapest way to reallocate attention, and it happens "
            "before conscious choice. The upward tilt serves the eyes: "
            "vast things are very often above - sky, mountains, "
            "ceilings, screens - and the head follows the stimulus. "
            "The open hands and lifted chin are approach signals: the "
            "body configuring itself to receive rather than to act. "
            "The shrinking - rounded shoulders, narrowed chest - is "
            "the embodied small self, the posture of deference that "
            "Darwin noted in reverence and that modern work links to "
            "the humility component of awe. The slow return of "
            "movement is graded re-engagement: the system brings motor "
            "output back online in proportion to how updated the frame "
            "is. The grip in threat-based awe is the withdrawal "
            "program running alongside approach: anchor the body while "
            "the eyes keep taking in. Together the posture is a "
            "readable sentence: I have stopped, I am looking up, I am "
            "small before this, and I am staying."
        ),
        "key_points": [
            "The arrest comes first: mid-step, mid-gesture, mid-sentence - everything stops before the face changes.",
            "Then the lift: head tilts up, gaze rises, chin lifts - awe looks up toward the vast thing.",
            "Hands hang forgotten or rise open in receiving; the mouth opens a fraction as an intake aperture.",
            "Deepening awe shrinks the body: rounded shoulders, narrowed chest - the postural small self.",
            "Movement returns slowly - drifting, slow head turns - and threat-based awe adds the grip: approach and anchor at once.",
        ],
        "requirements": [
            "The full postural sequence described in order: arrest, lift, open, shrink, slow return.",
            "Both hand positions covered: hanging forgotten and rising open.",
            "The small-self posture (rounded shoulders, narrowed chest) named.",
            "The threat-based grip distinguished from the pure-approach posture.",
            "The two distance-tells (arrest and lift) flagged for artists and actors.",
        ],
        "standards": [
            "Deference-posture framing follows Darwin 1872 on reverence and submission displays.",
            "Small-self embodiment follows Piff et al. 2015 and Shiota, Keltner and Mossman 2007.",
            "Orienting-freeze framing follows the attention psychophysiology literature.",
        ],
        "citations": [CIT_DARWIN, CIT_PIFF, CIT_SHIOTA],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "sleep_appetite",
        "name": "Awe, Sleep, Appetite, and Energy",
        "group": "Body Signals",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Awe's effects on the body's housekeeping - sleep, appetite, "
            "energy - are subtler than its fireworks, but they are part "
            "of the pattern. Sleep first: people often report sleeping "
            "deeply and well after a day with strong awe, and the "
            "mechanism is straightforward - the frame-stretching is "
            "cognitively expensive, and the system pays the bill in "
            "rest. The mind also replays: the canyon, the chord, the "
            "eyepiece view return uninvited at the edge of sleep, not "
            "as worry but as savoring, and dream reports after "
            "awe-heavy days skew toward vast landscapes. Appetite "
            "during awe itself usually drops - nobody is thinking about "
            "lunch at the canyon rim, because intake is pointed at the "
            "vast thing, not at food - and returns afterward often with "
            "a social flavor: the post-awe meal, eaten together, talked "
            "through, is one of the oldest human rituals for "
            "consolidating the feeling. Energy follows the quiet-"
            "fullness curve: during the peak the body spends little - "
            "stillness is cheap - and afterward there is a calm, "
            "available energy, the opposite of the wired crash after "
            "excitement. Rudd and colleagues found that awe expands "
            "perceived time, and people with more perceived time make "
            "less harried, more generous choices - including about rest: "
            "the awed person is less likely to burn the evening in "
            "frantic catch-up. The practical read: awe is one of the "
            "few intense emotions that leaves the housekeeping better "
            "than it found it."
        ),
        "how_it_works": (
            "The housekeeping effects work through the accommodation "
            "budget. Frame-stretching is metabolically and cognitively "
            "costly - updating core models of scale, self, and world is "
            "deep work - so the system schedules recovery as sleep "
            "pressure and replays the material at the sleep edge for "
            "consolidation, the same way it replays the day's learning. "
            "Appetite suppression during the peak is attentional "
            "triage: interoceptive hunger signals are deprioritized "
            "while exteroceptive vastness holds the channel. The "
            "social post-awe meal serves consolidation: narrating the "
            "experience to others rehearses the stretched frame and "
            "the shared telling amplifies the small-self connection. "
            "The calm energy afterward is the parasympathetic rebound "
            "plus the time-expansion effect - with the frame updated "
            "and perceived time widened, the system downshifts out of "
            "urgency mode. None of this replaces rest or nutrition as "
            "health guidance; it is the documented pattern of how "
            "this emotion treats the body's routines."
        ),
        "key_points": [
            "Sleep deepens after strong awe: frame-stretching is expensive and the system pays in rest, with vast dreams at the edges.",
            "Appetite drops during the peak - intake is pointed at the vast thing - and returns afterward with a social flavor: the consolidating shared meal.",
            "Energy follows the quiet-fullness curve: stillness is cheap during, calm available energy after - the opposite of the wired crash.",
            "Awe's time-expansion effect unhurries the evening: less frantic catch-up, more generous choices about rest.",
            "The practical read: awe is one of the few intense emotions that leaves the body's housekeeping better than it found it.",
        ],
        "requirements": [
            "All three housekeeping systems covered: sleep, appetite, energy.",
            "The replay-at-the-sleep-edge and vast-dreams detail included.",
            "The post-awe shared meal framed as a consolidation ritual.",
            "The Rudd time-expansion finding connected to rest choices.",
            "No health advice beyond describing the documented pattern.",
        ],
        "standards": [
            "Time-expansion effect follows Rudd, Vohs and Aaker 2012.",
            "Consolidation framing follows Shiota, Keltner and Mossman 2007 on awe and self-concept.",
            "Attentional-triage account follows Lazarus 1991.",
        ],
        "citations": [CIT_RUDD, CIT_SHIOTA, CIT_LAZARUS],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "individual_diff",
        "name": "Why Awe Feels Different in Every Body",
        "group": "Body Signals",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "No two bodies do awe exactly alike, and the variation is "
            "not noise - it is the signature of an assembled emotion. "
            "Some people are chill-responders: the goosebumps arrive "
            "at the first note of the overture, strong and reliable. "
            "Others never get chills at all and feel awe as a widening "
            "in the chest, a pressure behind the eyes, a stillness in "
            "the hands. Some weep at peak awe - the eyes watering is "
            "one of the most commonly reported signals - while others "
            "find the idea of crying at a landscape baffling. The "
            "triggers vary just as much: one person is leveled by the "
            "ocean and unmoved by cathedrals; another is undone by a "
            "single violin and bored by mountains. Openness to "
            "experience - the personality trait covering curiosity, "
            "imagination, and appetite for novelty - predicts awe "
            "frequency more strongly than any other trait: high-"
            "openness people report more awe, seek more of it, and "
            "assemble it faster. Expertise reshapes the feeling too: "
            "the astronomer and the child feel different awes at the "
            "same sky, because their frames differ and so do their "
            "gaps. Culture tunes the expression: where to look, how "
            "long to stay still, whether the \"wow\" is voiced or "
            "swallowed, what vastness is permitted to move you. Age "
            "matters as well - children's awe is frequent and "
            "unembarrassed, adult awe is rarer and more regulated, and "
            "older adults often report a return of the child's "
            "willingness. The lesson for the simulator: there is no "
            "single correct awe body. Build the core pattern - "
            "stillness, intake, small self - and then vary the "
            "instruments."
        ),
        "how_it_works": (
            "The variation works because awe is assembled from parts, "
            "and every assembler differs. The chills channel depends on "
            "piloerection sensitivity, which varies genetically and with "
            "age - hence reliable chill-responders and lifelong "
            "non-responders, both normal. The weeping channel depends on "
            "how the individual's system handles overflow at peak "
            "intake; some vent through the eyes, others through the "
            "throat, others through the skin. Trigger variation follows "
            "frame history: vastness is frame-relative, so the frames "
            "you were given - ocean childhoods, music households, "
            "city skylines - set your gaps. Openness to experience "
            "predicts frequency because high-openness minds maintain "
            "looser frames, which means more gaps and faster "
            "accommodation. Expertise enriches frames, which deepens "
            "the gap once measured - the astronomer's awe has more "
            "content than the child's, though not more sincerity. "
            "Cultural display rules then edit the output: the felt awe "
            "may be identical while the shown awe differs by upbringing. "
            "The simulator's rule: core pattern constant, instruments "
            "variable."
        ),
        "key_points": [
            "Chill-responders, weepers, chest-wideners, hand-stillers: the signal channel varies by body, and all are normal.",
            "Trigger maps are personal: ocean childhoods make ocean awe; music households make music awe - vastness is frame-relative.",
            "Openness to experience predicts awe frequency more strongly than any other trait.",
            "Expertise deepens the gap: the astronomer's awe has more content than the child's, not more sincerity.",
            "Culture edits the shown awe, age reshapes its frequency: the simulator varies the instruments, never the core pattern.",
        ],
        "requirements": [
            "At least four dimensions of variation covered: signal channel, trigger map, personality, expertise/culture/age.",
            "Chill-responders versus non-responders both normalized.",
            "Openness to experience named as the strongest frequency predictor.",
            "The frame-relative explanation used for trigger variation.",
            "The simulator rule stated: core pattern constant, instruments variable.",
        ],
        "standards": [
            "Assembled-emotion account follows Barrett 2017.",
            "Trait prediction follows the openness-to-experience literature on awe proneness.",
            "Frame-relative vastness follows Keltner and Haidt 2003.",
        ],
        "citations": [CIT_BARRETT, CIT_KELTNER_HAIDT, CIT_SHIOTA],
        "sig_lens": SIG_LENS_DEF,
    },

    # ------------------------------------------------ 14-17 FACIAL EXPRESSION
    {
        "key": "face",
        "name": "The Face of Awe: Eyes, Brows, Mouth",
        "group": "Facial Expression",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "The face of awe is the face of maximal intake, and it is "
            "readable at a glance. The brows go first: the inner corners "
            "lift - in the Facial Action Coding System, action units 1 "
            "and 2, the brow raiser - pulling the whole brow up and "
            "slightly together, widening the eye opening and wrinkling "
            "the forehead in horizontal lines. The eyes go second: the "
            "upper lids raise (action unit 5), the eyes widen, the gaze "
            "fixes and holds - the stare of absorption, distinct from "
            "the darting of fear or the softening of love. The mouth "
            "goes third: the jaw drops slightly open (action units 25, "
            "26, 27 depending on how far), the lips part, the lower face "
            "relaxes into an oval of reception. The whole configuration "
            "says one thing: more input, please. Darwin noted the raised "
            "brows and open mouth of astonishment in 1872, and modern "
            "coding confirms the pattern holds across cultures for the "
            "awe family. The micro-signs are what separate awe from its "
            "cousins: in awe the brow raise is inner-weighted (the "
            "middle of the brow lifts more than the ends), the widening "
            "holds steady rather than flickering, and the mouth opens "
            "without the teeth-baring of fear or the smile-muscles of "
            "joy. The head usually tilts up with the face, presenting "
            "the expression to the sky rather than to another person - "
            "awe's face is aimed at the vastness, not at an audience. "
            "There is no single muscle that means awe alone; it is the "
            "chord that matters, and the chord is brows up, eyes wide, "
            "mouth open, gaze fixed upward."
        ),
        "how_it_works": (
            "The face works as an aperture control system. Raising the "
            "brows and lids physically enlarges the visual field - more "
            "photons, more data, wider intake - which serves the "
            "vastness-registration half of the appraisal. Parting the "
            "lips and dropping the jaw opens a second intake channel "
            "and, just as importantly, stills the speech apparatus: an "
            "open mouth is a mouth not talking, which keeps the channel "
            "clear for input. The fixed gaze is attention locked: unlike "
            "the scanning of threat or the glancing of shame, awe's "
            "eyes stay put because the stimulus rewards sustained "
            "looking. The inner weighting of the brow raise is the "
            "tell that separates awe from mere surprise: surprise "
            "raises the whole brow evenly and briefly, while awe's "
            "raise is sustained and centered, reflecting the ongoing "
            "accommodation effort rather than a momentary startle. The "
            "upward head tilt aims the whole aperture at the typical "
            "location of vast things. Together the face is not "
            "expressing an inner state so much as configuring the "
            "hardware for the job: take in as much as possible, for as "
            "long as possible."
        ),
        "key_points": [
            "Brows lift from the inner corners (FACS AU 1+2), widening the eyes and wrinkling the forehead - the intake aperture opening.",
            "Upper lids raise (AU 5), eyes widen, gaze fixes and holds: the stare of absorption, not the dart of fear.",
            "The jaw drops slightly (AU 25/26/27), lips part: an open mouth is a mouth not talking, keeping the channel clear.",
            "The micro-tells: inner-weighted brow raise, steady widening, mouth open without fear's teeth or joy's smile-muscles.",
            "The head tilts up with the face: awe's expression is aimed at the vastness, not at an audience.",
        ],
        "requirements": [
            "All three facial regions covered: brows, eyes, mouth, with FACS action units named.",
            "The aperture-control function explained for each region.",
            "Micro-signs distinguishing awe from surprise, fear, and joy stated.",
            "Darwin 1872 noted as the classic observation, FACS 1978 as the modern coding.",
            "The upward aim of the whole configuration included.",
        ],
        "standards": [
            "Action-unit coding follows Ekman and Friesen FACS 1978.",
            "Classic observation follows Darwin 1872 on astonishment.",
            "Awe-face description follows Shiota, Keltner and Mossman 2007 on awe displays.",
        ],
        "citations": [CIT_FACS, CIT_DARWIN, CIT_SHIOTA],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "face_intensity",
        "name": "How the Awe Face Changes with Intensity",
        "group": "Facial Expression",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "The awe face is not one face but a gradient, and each "
            "intensity band writes itself differently. At low intensity "
            "- the sunrise glimpse - the face barely moves: the brows "
            "lift a few millimeters, the eyes widen a fraction, the "
            "lips part almost imperceptibly. A stranger would miss it; "
            "a friend catches it in the stillness around the eyes. The "
            "expression is brief, a few seconds, and the face returns "
            "to neutral cleanly. At middle intensity - bright awe at "
            "the rim - the full chord sounds: brows high with visible "
            "forehead lines, eyes at maximum comfortable widening, jaw "
            "dropped to a clear oval, gaze locked. The face holds this "
            "configuration for as long as the stimulus holds attention "
            "- minutes, not seconds - and it is unmistakable at "
            "distance. At high intensity - the overwhelming sublime - "
            "the face adds the overflow channels: the eyes water and "
            "may spill, the throat works visibly as the voice tries and "
            "fails to form words, the mouth may open wider into the "
            "gasp configuration. In threat-based awe the gradient adds "
            "fear's signature: the brow raise pulls more horizontal, "
            "the lips stretch and tighten at the corners, the widening "
            "takes on the tense edge of alarm. The gradient matters "
            "for the simulator because the face is the fastest "
            "readable dial: body stillness says something is happening, "
            "but the face says how much. And it matters for the "
            "recognition trainer later in this database: trainees learn "
            "to read the band, not just the chord."
        ),
        "how_it_works": (
            "The gradient works because each action unit has its own "
            "activation curve against the accommodation demand. Low "
            "demand recruits only the cheapest units - a partial brow "
            "raise, a slight lid lift - because the frame-gap is small "
            "and the intake need is modest. Rising demand recruits the "
            "full set at increasing amplitude: the aperture widens in "
            "proportion to how much there is to take in. At the top of "
            "the curve the system hits the overflow point, where intake "
            "demand exceeds channel capacity and the spillover "
            "channels - tearing, throat constriction, gasping - "
            "activate. The threat-based additions follow the fear "
            "program's own gradient running in parallel: lip "
            "stretching and brow horizontalization are fear's aperture "
            "plus alarm, blended with awe's aperture plus absorption. "
            "The hold duration scales with sustained attention: the "
            "face stays configured as long as the vastness holds the "
            "gaze, which is why middle-intensity awe faces are "
            "measured in minutes. The simulator's rule: scale every "
            "unit's amplitude with the band, add overflow at the top, "
            "blend fear's units by the threat ratio."
        ),
        "key_points": [
            "Low intensity: millimeters of brow lift, a fraction of widening, seconds of hold - missed by strangers, caught by friends.",
            "Middle intensity: the full chord at full amplitude - brows high, eyes maximally wide, jaw a clear oval, held for minutes.",
            "High intensity: overflow channels join - watering eyes, working throat, gasp configuration.",
            "Threat-based awe adds fear's units: horizontal brow pull, lip stretch and tightening, the tense edge of alarm.",
            "The face is the fastest readable dial: stillness says something is happening, the face says how much.",
        ],
        "requirements": [
            "Three bands described with specific facial amplitudes and hold durations.",
            "The overflow channels (tearing, throat, gasp) placed at the top of the gradient.",
            "Threat-based additions distinguished from pure-awe units.",
            "The amplitude-with-demand mechanism stated in how_it_works.",
            "The simulator rule given: scale amplitudes, add overflow, blend by threat ratio.",
        ],
        "standards": [
            "Action-unit gradients follow Ekman and Friesen FACS 1978 intensity scoring conventions.",
            "Overflow account follows the intake-capacity framing of Keltner and Haidt 2003.",
            "Threat-blend units follow Gordon et al. 2017 on the threat-based variant.",
        ],
        "citations": [CIT_FACS, CIT_KELTNER_HAIDT, CIT_GORDON],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "hiding_faking",
        "name": "Hiding or Faking Awe: What Leaks Through",
        "group": "Facial Expression",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "People try to hide awe and fake awe, and both attempts leak. "
            "Hiding awe - the teenager determined not to be impressed by "
            "the museum, the executive keeping composure at the "
            "observatory - runs into a structural problem: the awe face "
            "is largely an intake configuration, and you cannot take in "
            "maximally while displaying minimally. What leaks: the brow "
            "still lifts a few millimeters before the will catches it; "
            "the gaze still fixes a beat too long; the breath still "
            "catches audibly; the goosebumps still rise on the forearms "
            "where no will reaches. The most reliable leak is the "
            "stillness itself - the person who has decided to be "
            "unimpressed still stops moving, and arrested motion in a "
            "vast place is a confession. Faking awe - the tourist "
            "performing wonder for the camera, the guest feigning "
            "rapture at the host's art - leaks in the opposite "
            "direction. The performed face gets the big units right "
            "(wide eyes, open mouth) but misses the micro-timing: the "
            "brow raise is even rather than inner-weighted, the widening "
            "flickers instead of holding, the gaze darts to check the "
            "audience instead of fixing on the vastness. The body "
            "betrays the performance fastest: the faker keeps shifting "
            "weight, keeps the shoulders up, keeps talking - the "
            "orienting stillness never arrives, because there is no "
            "vastness to orient to. The practical rule: real awe is "
            "caught by the stillness and the sustained gaze; performed "
            "awe is caught by the motion and the checking."
        ),
        "how_it_works": (
            "The leaks work because the reliable muscles are the "
            "involuntary ones. Brow raising and lid lifting have both "
            "voluntary and involuntary pathways, but the involuntary "
            "pathway fires first and fastest - the will can suppress "
            "the expression only after it has begun, which is why the "
            "millimeters of lift escape before composure lands. "
            "Goosebumps have no voluntary pathway at all: piloerection "
            "is pure autonomic, so the forearms testify whatever the "
            "face claims. The gaze-fixation is attentional, not "
            "muscular: a person can force the eyes to move, but the "
            "dwell time on the vast stimulus still runs long, because "
            "attention genuinely is captured. On the faking side, the "
            "leaks come from the missing appraisal: with no real "
            "vastness registered, there is no accommodation demand, so "
            "the sustaining signals - the hold, the stillness, the "
            "slow return - never engage, and the performer must "
            "consciously maintain each unit, which produces the "
            "flicker and the checking. The simulator stages both: "
            "suppression as damped amplitudes with autonomic leaks, "
            "performance as correct big units with wrong micro-timing."
        ),
        "key_points": [
            "Hiding awe leaks through the involuntary pathway: millimeters of brow lift escape before the will catches up.",
            "Goosebumps cannot be suppressed at all - the forearms testify whatever the face claims.",
            "The most reliable leak of hidden awe is the stillness itself: arrested motion in a vast place is a confession.",
            "Faked awe gets the big units right but misses micro-timing: even brow raise, flickering widening, darting checking gaze.",
            "The faker's body betrays fastest: shifting weight, raised shoulders, continued talking - the orienting stillness never arrives.",
        ],
        "requirements": [
            "Both directions covered: hiding (suppression) and faking (performance).",
            "At least three specific leaks named for each direction.",
            "The voluntary-versus-involuntary pathway mechanism explained.",
            "The practical recognition rule stated: stillness plus sustained gaze versus motion plus checking.",
            "The simulator staging note included for both.",
        ],
        "standards": [
            "Voluntary/involuntary pathway distinction follows Ekman and Friesen FACS 1978 and the leakage literature.",
            "Piloerection as autonomic follows Maruskin, Thrash and Elliot 2012.",
            "Display-rule framing follows Ekman 1999 conventions.",
        ],
        "citations": [CIT_FACS, CIT_MARUSKIN, CIT_SHIOTA],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "expression_gallery",
        "name": "Drawing Awe: Notes for the Artist or Actor",
        "group": "Facial Expression",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "For the artist with the pencil and the actor with the "
            "mirror: here is the awe face as build instructions. Start "
            "with the brow: lift the inner two-thirds high, keep the "
            "outer ends lower - the center of the brow should sit "
            "noticeably above its resting line, drawing two or three "
            "horizontal creases across the forehead. The lift is "
            "sustained, not surprised: think of someone watching, not "
            "someone startled. The eyes: open them to their comfortable "
            "maximum, upper lids high, the full iris visible with a "
            "sliver of white above. The gaze is the hard part - it must "
            "be fixed and slightly upward, the focus of a person "
            "looking at something far and large, not the vacancy of a "
            "daydream. The mouth: part the lips and let the jaw drop "
            "until the opening is a soft oval, roughly a finger's width "
            "- no teeth bared, no corners pulled, the lower face "
            "entirely relaxed around the opening. The head: tilt it "
            "back five to ten degrees, chin lifted, the whole face "
            "offered upward. The neck: long, the throat exposed - awe "
            "does not guard the throat the way fear does. For the body "
            "around the face: still the shoulders, drop them a fraction, "
            "let the arms hang or open slightly. The common errors: "
            "playing surprise instead (too fast, too even across the "
            "brow, gaze darting); playing fear instead (lips stretched "
            "tight, brow pulled flat and horizontal, throat guarded); "
            "playing joy instead (the smile muscles engaged, cheeks "
            "lifted, eyes crinkled at the corners - awe's eyes stay "
            "open and uncrinkled). The check: cover the lower face and "
            "the upper face alone should still read as absorbed "
            "wideness; cover the upper face and the open mouth alone "
            "should still read as reception, not speech. When both "
            "halves read correctly alone, the chord is right."
        ),
        "how_it_works": (
            "The build instructions work because they assemble the "
            "chord unit by unit in the order the face assembles it: "
            "brow first (the aperture frame), eyes second (the aperture "
            "itself), mouth third (the secondary channel), head and "
            "body last (the aiming and the stillness). The "
            "inner-weighted brow is specified because it is the "
            "single most diagnostic unit - get it wrong and the face "
            "reads as generic surprise. The gaze direction is "
            "specified because the eyes carry the attention story: "
            "fixed and upward means absorbed by the vast, darting "
            "means checking the room. The throat exposure is "
            "specified because it is the fastest fear-versus-awe "
            "discriminator an artist can draw: guarded throat reads "
            "threat, open throat reads reception. The error catalog "
            "works by naming the three confusions the face most "
            "often falls into - surprise, fear, joy - each with its "
            "diagnostic unit, so the artist can check the drawing "
            "against the specific failure. The half-face check works "
            "because the awe chord is redundant: each half carries "
            "enough signal to read alone, which is also why the "
            "feeling survives bad lighting, distance, and quick "
            "glances."
        ),
        "key_points": [
            "Brow: inner two-thirds lifted high, outer ends lower, two to three forehead creases - sustained watching, not startle.",
            "Eyes: comfortable maximum opening, full iris plus a sliver of white, gaze fixed and slightly upward.",
            "Mouth: soft oval a finger's width, no bared teeth, no pulled corners, lower face relaxed.",
            "Head tilted back five to ten degrees, throat exposed: awe does not guard the throat the way fear does.",
            "The three confusions to avoid: surprise (too fast, even brow), fear (stretched lips, guarded throat), joy (smile muscles, crinkled eyes).",
        ],
        "requirements": [
            "Step-by-step build order: brow, eyes, mouth, head, body.",
            "Concrete measurements given (millimeters of lift, finger's width of mouth, degrees of tilt).",
            "The three confusion errors named with their diagnostic units.",
            "The half-face redundancy check included.",
            "Written so a non-specialist artist or actor can execute it.",
        ],
        "standards": [
            "Unit specifications follow Ekman and Friesen FACS 1978.",
            "Display description follows Shiota, Keltner and Mossman 2007 on awe displays.",
            "Classic reference follows Darwin 1872 on astonishment.",
        ],
        "citations": [CIT_FACS, CIT_SHIOTA, CIT_DARWIN],
        "sig_lens": SIG_LENS_DEF,
    },

    # ------------------------------------------------ 18-21 TRIGGERS
    {
        "key": "classic_triggers",
        "name": "The Classic Triggers of Awe",
        "group": "Triggers",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "The classic triggers of awe are classic because they work "
            "on nearly everyone, and they cluster into families. "
            "Nature's vastness comes first in every survey: the Grand "
            "Canyon and its kin, the ocean from a cliff, the night sky "
            "far from city lights, waterfalls, storms, the view from a "
            "summit. These are perceptual vastness in its purest form - "
            "the stimulus is literally larger than the frame. Built "
            "vastness comes second: cathedrals, temples, mosques, and "
            "skyscrapers; the great concert halls at the final chord; "
            "bridges and dams that make engineering feel like geology. "
            "Human vastness comes third and surprises people: the birth "
            "of a child, the sight of a crowd moving as one, a "
            "parade, a stadium singing in unison - social scale doing "
            "what landscapes do. Aesthetic vastness comes fourth: the "
            "overture's climax, the choir, the film's wide shot held a "
            "beat too long, the novel's final page - craft so complete "
            "it exceeds the frame for how things are made. Conceptual "
            "vastness comes fifth: the idea of deep time, the number of "
            "stars, the double-slit experiment, the family tree going "
            "back forty generations - vastness with no picture at all, "
            "carried entirely by thought. And moral vastness comes "
            "sixth: the act of selfless courage, the forgiveness that "
            "should be impossible, the stranger's generosity at scale - "
            "goodness so large the frame for human behavior has to "
            "stretch. The families overlap constantly - the cathedral "
            "is built and aesthetic and often moral at once - and the "
            "simulator should treat them as a palette, not a filing "
            "system."
        ),
        "how_it_works": (
            "The classic triggers work because each family delivers one "
            "or both of the two ingredients at high dose. Nature "
            "delivers perceptual vastness directly - the retina "
            "reports scale the frame cannot hold. Built vastness "
            "delivers perceptual vastness plus conceptual vastness: the "
            "cathedral is big and it is also the product of "
            "generations, so the gap is doubled. Human vastness "
            "delivers social vastness: the self is small against the "
            "many, and the many moving as one adds the coordination "
            "miracle. Aesthetic vastness delivers the gap through "
            "craft: the frame for what music or story can do is "
            "exceeded, and accommodation rebuilds the frame for art "
            "itself. Conceptual vastness is pure accommodation demand "
            "with no perceptual component - the mind stretches on "
            "thought alone. Moral vastness stretches the frame for "
            "what people are: the cynic's model of humanity fails to "
            "predict the act, and the model must grow. The reason the "
            "same families recur across cultures is that the frame-gap "
            "mechanism is universal even when the local vast things "
            "differ - every culture has its sky, its gatherings, its "
            "craft, its unthinkable kindnesses."
        ),
        "key_points": [
            "Nature's vastness: canyons, oceans, night skies, waterfalls, storms, summits - perceptual vastness in purest form.",
            "Built vastness: cathedrals, skyscrapers, concert halls, bridges - scale doubled by the generations behind it.",
            "Human vastness: births, crowds moving as one, stadiums singing - social scale doing what landscapes do.",
            "Aesthetic vastness: the overture's climax, the film's held wide shot - craft exceeding the frame for how things are made.",
            "Conceptual and moral vastness: deep time and the double-slit; the unthinkable kindness - frames stretched by thought and goodness alone.",
        ],
        "requirements": [
            "Six trigger families named with concrete examples in each.",
            "Each family mapped to which ingredient(s) it delivers: perceptual, conceptual, social, moral vastness.",
            "The cross-cultural recurrence explained via the universal frame-gap mechanism.",
            "The palette-not-filing-system note: families overlap and combine.",
            "Examples concrete enough to stage in the simulator.",
        ],
        "standards": [
            "Elicitor families follow Shiota, Keltner and Mossman 2007 on the nature of awe.",
            "Moral vastness follows Keltner and Haidt 2003 on moral and spiritual elicitors.",
            "Aesthetic chills follow Maruskin, Thrash and Elliot 2012.",
        ],
        "citations": [CIT_SHIOTA, CIT_KELTNER_HAIDT, CIT_MARUSKIN],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "personal_triggers",
        "name": "Personal Triggers: Memories and Private Associations",
        "group": "Triggers",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "Beyond the classics, everyone carries a private atlas of "
            "awe triggers - places, sounds, and moments that would move "
            "no one else the same way. The song that played on the "
            "drive home the night the good news came: hearing it years "
            "later in a grocery store, the frame-gap of that night "
            "reopens and the chills arrive on schedule. The overlook "
            "where a parent once stood silent beside you, both of you "
            "looking at the same valley: returning alone, the vastness "
            "is doubled by the absence. The smell of a particular "
            "woodsmoke that means the cabin, the mountain, the week "
            "the world felt large and kind. These triggers work "
            "differently from the classics: the vastness is not in the "
            "stimulus, it is in the association. The grocery-store song "
            "is three minutes of pop; the awe is the reopened frame of "
            "the night everything changed. Anniversaries are the "
            "calendar form of this: the date itself becomes a trigger, "
            "and the body starts the intake program before the mind "
            "catches up - the throat tightens on the drive past the "
            "hospital, the eyes widen at the trailhead, unbidden. "
            "Private associations also explain the strongest "
            "disagreements about what is awesome: the canyon leaves "
            "one traveler cold and undoes another, because the second "
            "traveler scattered a private meaning across it years ago. "
            "The simulator's lesson: personal triggers are not weaker "
            "versions of classic triggers. For the person who owns "
            "them, they are stronger - the frame-gap is pre-built, the "
            "accommodation is rehearsed, and the feeling arrives at "
            "full volume from a whisper of a cue."
        ),
        "how_it_works": (
            "Personal triggers work through associative reactivation of "
            "the stretched frame. When awe first stretched a frame - "
            "the night of the good news, the valley with the parent - "
            "the memory encoded not just the event but the frame state: "
            "the wideness, the smallness, the chills. Later, a cue "
            "linked to that memory - the song, the overlook, the "
            "woodsmoke - reactivates the frame state directly, bypassing "
            "the need for fresh vastness. This is why the trigger can "
            "be objectively small: the work was done years ago, and "
            "the cue is just the key turning. Anniversaries work "
            "through temporal conditioning: the date has been paired "
            "with the frame state often enough that the calendar "
            "itself becomes the cue, and the body begins the program "
            "on schedule. The disagreement effect follows: two people "
            "at the same canyon have different associative histories "
            "layered over the same stimulus, so their gaps differ and "
            "their awes differ. For the simulator, personal triggers "
            "are modeled as multiplier keys: small cue times large "
            "stored gap equals full-volume feeling."
        ),
        "key_points": [
            "Everyone carries a private atlas: songs, overlooks, smells that reopen old frame-gaps at full volume.",
            "The vastness in a personal trigger is in the association, not the stimulus - the grocery-store song is ordinary, the reopened night is not.",
            "Anniversaries are calendar triggers: the date becomes the cue and the body starts the program on schedule.",
            "Private associations explain awe disagreements: same canyon, different layered histories, different gaps.",
            "Personal triggers are not weaker classics: pre-built gap plus rehearsed accommodation means full volume from a whisper of cue.",
        ],
        "requirements": [
            "The private-atlas concept introduced with at least three concrete examples.",
            "The association-not-stimulus mechanism stated plainly.",
            "Anniversaries covered as the calendar form.",
            "The disagreement explanation included.",
            "The simulator modeling note: small cue times large stored gap.",
        ],
        "standards": [
            "Associative reactivation follows the memory-consolidation account of Shiota, Keltner and Mossman 2007.",
            "Frame-relative vastness follows Keltner and Haidt 2003.",
            "Constructed-emotion variation follows Barrett 2017.",
        ],
        "citations": [CIT_SHIOTA, CIT_KELTNER_HAIDT, CIT_BARRETT],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "surprise_triggers",
        "name": "Surprise Triggers: The Odd Awe Setters-Off",
        "group": "Triggers",
        "ladder_rank": 9,
        "ladder_tier": "compounded",
        "description": (
            "Then there are the triggers nobody would put on a list, "
            "the odd ones that ambush people in ordinary places. The "
            "murmuration: a thousand starlings folding themselves into "
            "ribbons over a parking lot at dusk, and a grown adult "
            "stands with the mouth open at the sheer coordination of "
            "it - no vast landscape, just vast organization. The "
            "perfectly timed kindness: the stranger who pays for the "
            "groceries of the person counting coins, and the witnesses "
            "feel the chills - moral vastness in a checkout line. The "
            "machine that exceeds its frame: the old telescope in the "
            "club observatory resolving Saturn's rings, the 3D print "
            "coming off the bed impossibly fine, the code compiling on "
            "the first try after a week of failure - craft vastness, "
            "the frame for what things can do breaking quietly. The "
            "child's question from the day vignette: conceptual "
            "vastness wearing a small voice. The coincidence with "
            "weight: running into the old friend in the foreign city "
            "on the one day, the book falling open to the exact page - "
            "not supernatural, just the frame for chance stretching a "
            "notch. The body doing the impossible: the gymnast's "
            "landing stuck cold, the surgeon's hands in the "
            "documentary, the free diver's single breath - human "
            "capability exceeding the frame for bodies. What unites "
            "the odd triggers is the ambush quality: no one went "
            "looking, no frame was prepared, so the gap is at maximum "
            "and the awe arrives at full strength from nothing. The "
            "simulator should keep a drawer of these: the best awe "
            "scenes are often the ones the audience did not see "
            "coming."
        ),
        "how_it_works": (
            "The odd triggers work through unprepared gaps. Classic "
            "triggers come with warning - you drive to the canyon "
            "expecting vastness, and the frame loosens in advance, "
            "which slightly reduces the gap. The odd triggers arrive "
            "with the frame fully tight: the parking lot was not "
            "supposed to contain a miracle of coordination, the "
            "checkout line was not supposed to contain moral "
            "vastness. The accommodation demand therefore spikes "
            "harder relative to the stimulus size - the gap is the "
            "whole distance between the ordinary frame and the "
            "extraordinary event, with no pre-loosening. This is why "
            "small odd triggers can out-awe large expected ones: the "
            "murmuration over the parking lot can move a person more "
            "than the canyon on the itinerary, because the itinerary "
            "canyon got a prepared frame and the parking lot got "
            "none. The mechanism is the same two-ingredient appraisal "
            "as ever - perceived vastness plus need for accommodation "
            " - with the accommodation term maximized by surprise. "
            "For the simulator, the rule is: expected vastness gets a "
            "discounted gap, ambush vastness gets the full gap."
        ),
        "key_points": [
            "The murmuration over the parking lot: vast organization with no vast landscape - coordination exceeding the frame.",
            "The checkout-line kindness: moral vastness in the most ordinary place, chills on schedule.",
            "The machine exceeding its frame: Saturn's rings in the club telescope, craft breaking the frame quietly.",
            "The child's question, the weighted coincidence, the impossible body: small cues, unprepared frames, maximum gaps.",
            "The ambush rule: expected vastness gets a discounted gap; ambush vastness gets the full gap.",
        ],
        "requirements": [
            "At least six odd triggers named, each with its vastness type identified.",
            "The ambush-quality mechanism explained: unprepared frames maximize the gap.",
            "The comparison made: small odd triggers can out-awe large expected ones.",
            "The simulator rule stated: discount expected gaps, keep ambush gaps full.",
            "All examples ordinary-place, no-travel-required.",
        ],
        "standards": [
            "Two-ingredient account follows Keltner and Haidt 2003.",
            "Novelty-amplification follows the accommodation-demand logic of Shiota, Keltner and Mossman 2007.",
            "Moral-vastness elicitors follow Keltner and Haidt 2003.",
        ],
        "citations": [CIT_KELTNER_HAIDT, CIT_SHIOTA, CIT_MARUSKIN],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "chain_reactions",
        "name": "Chain Reactions: Awe Setting Off Cascades",
        "group": "Triggers",
        "ladder_rank": 9,
        "ladder_tier": "compounded",
        "description": (
            "Awe rarely travels alone; it sets off cascades, and the "
            "cascades are where the feeling does its lasting work. "
            "The classic chain runs: awe to humility to gratitude to "
            "generosity. It starts at the rim: the vastness registers, "
            "the small self arrives - that is the humility link, the "
            "felt sense of being one small part of a large whole. The "
            "humility link fires the gratitude link almost automatically: "
            "the small self, feeling held by something larger, "
            "registers the holding as a gift - and gratitude is the "
            "emotion of recognized gifts. Piff and colleagues showed "
            "the next link experimentally: people fresh from awe give "
            "more, help more, and choose the prosocial option more "
            "often - the small self, less preoccupied with its own "
            "wants, spends its resources outward. A second chain runs "
            "through curiosity: awe to wonder to exploration. The "
            "accommodation demand - the frame that must stretch - is "
            "felt as a question, and questions motivate seeking: the "
            "telescope line forms, the book gets bought, the trail gets "
            "walked again with new eyes. A third chain runs through "
            "connection: awe to the small self to belonging. The "
            "diminished self is also a connected self - less separate, "
            "more merged - and people leave awe experiences wanting "
            "contact: the shared look at the rim, the retelling at "
            "dinner, the photograph sent instantly. A fourth, darker "
            "chain runs from threat-based awe: awe to fear to "
            "vigilance to avoidance - the storm-watcher who never "
            "stands that close again has learned, and the learning is "
            "the accommodation doing protective work. The simulator's "
            "job with chains is sequencing: awe is the first domino, "
            "never the last, and a simulation that ends at the "
            "\"wow\" has stopped the story halfway."
        ),
        "how_it_works": (
            "The chains work because accommodation is never a single "
            "update - it is a reorganization, and reorganizations "
            "propagate. The humility link is direct: the vastness "
            "appraisal includes the self as small-by-comparison, which "
            "is the core relational theme of humility. Gratitude "
            "follows because the small self appraises its place in "
            "the large whole as held rather than threatened - "
            "contingent on the positive flavor; threat-based awe "
            "routes to vigilance instead. Generosity follows from "
            "the reduced self-focus: with the self quiet, resources "
            "flow outward, which is the Piff finding. The curiosity "
            "chain is the accommodation demand experienced from the "
            "inside: an open frame-gap feels like a question, and "
            "open questions drive information-seeking. The connection "
            "chain is the small self's social corollary: diminished "
            "boundaries mean increased merging, and merging seeks "
            "contact. The dark chain is the same machinery with the "
            "safety appraisal flipped: the frame stretches around a "
            "threat model instead of a wonder model, and the "
            "reorganization is protective. Each chain is the "
            "accommodation settling into a different region of the "
            "mental architecture - values, knowledge, relationships, "
            "or safety."
        ),
        "key_points": [
            "The classic chain: awe to humility (the small self) to gratitude (the holding felt as gift) to generosity (resources flowing outward).",
            "The curiosity chain: awe to wonder to exploration - the open frame-gap felt as a question that drives seeking.",
            "The connection chain: awe to the small self to belonging - diminished boundaries seeking contact and retelling.",
            "The dark chain: threat-based awe to fear to vigilance to avoidance - the frame stretching around a threat model.",
            "The simulator rule: awe is the first domino, never the last - a simulation ending at 'wow' stops halfway.",
        ],
        "requirements": [
            "Four chains named and sequenced: generosity, curiosity, connection, and the dark protective chain.",
            "Each link's mechanism given in how_it_works.",
            "The Piff prosocial finding cited for the generosity chain.",
            "The safety-appraisal flip explained as the router between the bright and dark chains.",
            "The simulator sequencing rule stated.",
        ],
        "standards": [
            "Prosocial chain follows Piff et al. 2015: awe, the small self, and prosocial behavior.",
            "Small-self mechanism follows Shiota, Keltner and Mossman 2007.",
            "Threat routing follows Gordon et al. 2017.",
        ],
        "citations": [CIT_PIFF, CIT_SHIOTA, CIT_GORDON],
        "sig_lens": SIG_LENS_DEF,
    },

    # ------------------------------------------------ 22-25 HOW IT SHOWS IN BEHAVIOR
    {
        "key": "actions",
        "name": "What People Do When They Feel Awe",
        "group": "How It Shows in Behavior",
        "ladder_rank": 9,
        "ladder_tier": "compounded",
        "description": (
            "Awe has a behavioral signature as readable as its face. "
            "First, people stop: the arrest is the universal opener - "
            "mid-step, mid-task, the body halts to give attention the "
            "channel. Second, people orient: they turn toward the vast "
            "thing, lift the gaze, sometimes physically move closer - "
            "the rim draws feet the way the stage draws eyes. Third, "
            "people reach: a hand extends toward the vastness without "
            "any plan to touch it, the classic useless beautiful "
            "gesture of the canyon rim. Fourth, people share: they "
            "point, they beckon, they grab the sleeve of whoever is "
            "nearest - \"look, look\" - because awe's social function "
            "demands witnesses. Fifth, people capture: the photograph, "
            "the video, the quick sketch - an attempt to hold the "
            "unholdable, and also a way to extend the sharing beyond "
            "the moment. Sixth, people linger: the awed do not check "
            "watches; dwell time at vast things is the behavioral "
            "measure researchers actually use, and it stretches with "
            "intensity. Seventh, people ritualize: they return to the "
            "overlook yearly, they play the piece again, they tell the "
            "story until it is family property - the accommodation "
            "maintained by repetition. In threat-based awe the list "
            "adds the anchor behaviors: gripping the rail, stepping "
            "back from the edge, positioning the body behind the wall - "
            "approach and safety negotiated step by step. What people "
            "do not do in awe is equally diagnostic: they do not "
            "multitask, they do not rush, they do not narrate over the "
            "moment - the commentary mind is quiet, and the behavior "
            "shows it."
        ),
        "how_it_works": (
            "The action list works as the behavioral output of the "
            "two-ingredient appraisal. Stopping and orienting serve "
            "vastness registration: the system maximizes input by "
            "halting competing motor programs and aiming the sensors. "
            "Reaching is the approach program running without a "
            "consummatory target - the hand extends because approach "
            "is activated, though there is nothing to grasp. Sharing "
            "serves the social function: awe evolved to be witnessed, "
            "so the system recruits others to co-register the "
            "vastness, which amplifies and validates the appraisal. "
            "Capturing is sharing extended in time plus a hedge "
            "against the aftershock fading - the photograph is a "
            "re-cue device for the stretched frame. Lingering is "
            "dwell time tracking accommodation: the system stays "
            "until the frame-gap narrows enough to release attention. "
            "Ritualizing is maintenance: repeated re-exposure keeps "
            "the stretched frame from springing back. The anchor "
            "behaviors in threat-based awe are the withdrawal program "
            "negotiating with approach: close enough to register, far "
            "enough to survive. The absences - no multitasking, no "
            "rushing - are the small self quieting the agenda."
        ),
        "key_points": [
            "People stop first: the arrest is the universal opener, halting competing programs to free attention.",
            "People orient and reach: turning toward the vast thing, the hand extending with no plan to touch it.",
            "People share and capture: pointing, beckoning, photographing - awe demands witnesses and re-cue devices.",
            "People linger and ritualize: dwell time tracks accommodation, and return visits maintain the stretched frame.",
            "Threat-based awe adds anchor behaviors: gripping the rail, stepping back - approach and safety negotiated step by step.",
        ],
        "requirements": [
            "Seven signature actions named in sequence: stop, orient, reach, share, capture, linger, ritualize.",
            "Threat-based anchor behaviors distinguished.",
            "The diagnostic absences included: no multitasking, no rushing, no narrating over the moment.",
            "Each action mapped to its function in how_it_works.",
            "Dwell time noted as the researchers' behavioral measure.",
        ],
        "standards": [
            "Action-tendency framing follows Lazarus 1991 and Frijda on emotion action readiness.",
            "Social-sharing function follows Piff et al. 2015.",
            "Dwell-time measure follows the awe elicitation literature (Shiota, Keltner and Mossman 2007).",
        ],
        "citations": [CIT_LAZARUS, CIT_PIFF, CIT_SHIOTA],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "speech",
        "name": "What Awe Sounds Like: Words, Tone, Speech",
        "group": "How It Shows in Behavior",
        "ladder_rank": 9,
        "ladder_tier": "compounded",
        "description": (
            "Awe has a sound, and it is mostly the sound of language "
            "giving up gracefully. The characteristic utterance is "
            "minimal: \"wow,\" \"oh,\" \"oh my,\" \"whoa\" - single "
            "syllables or short breaths, voiced low and slow, often "
            "more exhaled than spoken. Full sentences arrive late or "
            "not at all; when they come they are fragments - \"that "
            "is... I can't... look at...\" - the syntax breaking where "
            "the frame breaks. The voice itself changes: pitch drops, "
            "volume falls to a hush, pace slows to a crawl. People "
            "whisper in cathedrals and at canyon rims without being "
            "told, as if loudness would be a category error. There is "
            "a second speech pattern, the retrospective one: minutes "
            "or hours later, the story comes out in a rush - the "
            "retelling at dinner, the phone call from the trailhead - "
            "and here the sentences are complete but looping, circling "
            "the vastness, trying approaches: \"and then the light, "
            "and you could see all the way to...\" The vocabulary of "
            "awe is notably impoverished at the peak and rich "
            "afterward: during, there are no words; after, there are "
            "too many, none sufficient. Profanity appears in some "
            "people's awe speech - the startled oath as the frame "
            "breaks - and it is not irreverence but overflow. "
            "Questions replace statements in the curiosity chain: "
            "\"how deep is it,\" \"how old is that,\" \"how do they "
            "do that\" - the open frame-gap speaking. The simulator's "
            "dialogue rule: at peak awe, characters should run out of "
            "language; eloquence about awe belongs to the retelling, "
            "never to the moment."
        ),
        "how_it_works": (
            "The speech pattern works because language and "
            "accommodation compete for the same processing. At peak "
            "awe the frame is being rebuilt in real time, which "
            "consumes the resources that syntax needs - hence the "
            "fragments, the single syllables, the giving up. The "
            "hushed volume is social deference running on the small "
            "self: the diminished self does not broadcast, it "
            "receives, and the voice follows the posture. The "
            "retrospective rush is consolidation speaking: once the "
            "frame has stretched, the system rehearses the new "
            "configuration by narrating it, and the looping is the "
            "narrative equivalent of turning the vast thing over in "
            "the mind. The impoverished-then-rich vocabulary curve "
            "tracks the accommodation curve exactly: no words while "
            "the gap is open, many words once it starts closing. The "
            "oath at the break is the startle pathway firing through "
            "the speech channel before the will edits it. The "
            "questions are the curiosity chain made audible - the "
            "open gap asking to be filled. For dialogue writing, the "
            "rule is physiological: eloquence requires a closed gap."
        ),
        "key_points": [
            "Peak awe speech is minimal: 'wow,' 'oh,' 'whoa' - breathed more than spoken, low and slow.",
            "Sentences fragment where the frame breaks: 'that is... I can't... look at...' - syntax failing with the model.",
            "Volume falls to a hush unbidden: loudness feels like a category error before vastness.",
            "The retelling rush comes later: complete but looping sentences, circling the vastness, vocabulary rich but never sufficient.",
            "Questions replace statements in the curiosity chain: the open gap asking to be filled.",
        ],
        "requirements": [
            "Both speech phases covered: the minimal peak phase and the retrospective retelling phase.",
            "Vocal changes specified: pitch drop, volume hush, slowed pace.",
            "The fragment pattern exemplified with quoted fragments.",
            "The oath and the questions both accounted for.",
            "The dialogue-writing rule stated: eloquence belongs to the retelling, never the moment.",
        ],
        "standards": [
            "Resource-competition account follows the cognitive-load framing of accommodation (Keltner and Haidt 2003).",
            "Deference-vocal pattern follows the small-self literature (Piff et al. 2015).",
            "Retelling as consolidation follows Shiota, Keltner and Mossman 2007.",
        ],
        "citations": [CIT_KELTNER_HAIDT, CIT_PIFF, CIT_SHIOTA],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "decisions",
        "name": "How Awe Changes Decisions and Judgment",
        "group": "How It Shows in Behavior",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Awe does not just feel large; it makes thinking large, "
            "and large thinking decides differently. The best-"
            "documented effect is the prosocial shift: Piff and "
            "colleagues showed across multiple studies that people "
            "fresh from awe give more to strangers, volunteer more "
            "time, and choose the generous option more often - the "
            "small self, less knotted around its own wants, spends "
            "outward. The second effect is time expansion: Rudd, Vohs "
            "and Aaker found that awe makes people feel they have more "
            "time available, and time-rich people decide more "
            "patiently - less discounting of the future, less frantic "
            "optimization, more willingness to wait for the better "
            "option. The third effect is reduced materialism: the awed "
            "mind, its frame stretched around vastness, temporarily "
            "devalues accumulation - the new car matters less at the "
            "canyon rim, and the effect lingers into the week's "
            "spending choices. The fourth effect is increased "
            "humility in judgment: the small self doubts its own "
            "certainties more readily, listens longer, and updates "
            "faster - awe is, among other things, a practiced lesson "
            "in being wrong about scale. The fifth is risk "
            "recalibration, and it cuts both ways: positive awe "
            "broadens the sense of possibility (people attempt more), "
            "while threat-based awe sharpens caution (people attempt "
            "more carefully). The practical use: schedule the big "
            "generous decisions - the donation, the forgiveness, the "
            "long-view choice - for after the overlook, not before. "
            "And the caution: awe's judgment effects are real but "
            "temporary, measured in hours and days, not character "
            "transplants - the frame stretches, it does not become a "
            "different person."
        ),
        "how_it_works": (
            "The decision effects work through the small self and the "
            "stretched frame operating as judgment inputs. Prosocial "
            "choice rises because the utility calculation changes: "
            "with the self diminished, other-regarding outcomes gain "
            "weight relative to self-regarding ones - the same "
            "resources, reweighted. Patience rises because perceived "
            "time expands: discounting models show that people "
            "discount the future less when they feel time-abundant, "
            "and awe manufactures time-abundance. Materialism falls "
            "because the comparison set changes: against the canyon, "
            "the car is small, and the reweighted comparison lingers "
            "while the frame stays stretched. Humility in judgment "
            "is the accommodation habit generalizing: a mind freshly "
            "practiced in revising its model of scale revises other "
            "models more readily. Risk recalibration splits by flavor "
            "because the safety appraisal splits: positive awe "
            "signals a benign vast world (attempt more), threat-based "
            "awe signals a dangerous vast world (attempt carefully). "
            "The temporariness follows the aftershock curve: as the "
            "frame settles, the old weights return - which is why "
            "the wise schedule the decision inside the window."
        ),
        "key_points": [
            "The prosocial shift: fresh awe makes people give more, help more, choose the generous option - the small self spending outward.",
            "Time expansion: awe manufactures felt time-abundance, and time-rich people decide patiently, discounting the future less.",
            "Reduced materialism: against the canyon the car is small, and the reweighted comparison lingers for days.",
            "Humility in judgment: the freshly stretched mind doubts its certainties, listens longer, updates faster.",
            "Risk recalibrates by flavor: positive awe broadens possibility, threat-based awe sharpens caution - and all of it is temporary, measured in hours and days.",
        ],
        "requirements": [
            "Five decision effects named: prosocial shift, time expansion, reduced materialism, judgment humility, risk recalibration.",
            "Each effect given its mechanism in how_it_works.",
            "The Piff and Rudd findings cited for the first two effects.",
            "The both-ways risk effect split by awe flavor.",
            "The temporariness stated plainly with the scheduling advice.",
        ],
        "standards": [
            "Prosocial effect follows Piff et al. 2015.",
            "Time-expansion effect follows Rudd, Vohs and Aaker 2012.",
            "Reweighting account follows the small-self literature (Shiota, Keltner and Mossman 2007).",
        ],
        "citations": [CIT_PIFF, CIT_RUDD, CIT_SHIOTA],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "intensity_behavior",
        "name": "Awe at Full Volume: Behavior Under Intensity",
        "group": "How It Shows in Behavior",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "As awe intensifies, behavior escalates along a predictable "
            "curve - and the curve has a bend where the wise slow "
            "down. At low intensity the behavior is casual: the pause, "
            "the photograph, the remark, the day continuing. At middle "
            "intensity the behavior commits: the itinerary changes - "
            "the extra hour at the rim, the second viewing, the "
            "canceled afternoon - because the system has decided the "
            "vastness outranks the schedule. People rearrange travel "
            "around eclipses; they drive the extra three hundred miles "
            "for the telescope night; they stand in the rain for the "
            "overture. At high intensity the behavior surrenders: plans "
            "dissolve entirely, the person follows the vastness - the "
            "storm chaser's logic, the pilgrim's logic - and the "
            "ordinary agenda goes quiet for hours or days. This is "
            "where the curve bends: high-intensity awe also escalates "
            "the risks. The rim's edge gets closer, the storm gets "
            "nearer, the crowd gets denser - the approach program, "
            "running hot, overrides the safety appraisal, and "
            "threat-based awe's alarm wire is the only thing still "
            "arguing for distance. The escalation also changes the "
            "social behavior: low awe is shared lightly, middle awe is "
            "shared urgently (the sleeve-grab, the phone call), high "
            "awe goes silent - at the peak there are no witnesses "
            "recruited because there is no speech to recruit them "
            "with. Afterward the curve reverses into devotion: the "
            "returned-to overlook, the annual eclipse trip, the piece "
            "played every year on the same date - high awe writes "
            "itself into the calendar. The practical read: let middle "
            "awe rearrange the day, let high awe rearrange the week, "
            "but keep the alarm wire's vote counted at the rim's edge."
        ),
        "how_it_works": (
            "The escalation works because accommodation demand "
            "outbids competing goals in proportion to its size. Low "
            "demand loses to the schedule - the sunrise gets twenty "
            "seconds because the day's agenda outbids it. Middle "
            "demand wins against the schedule - the rim gets the "
            "afternoon because the frame-gap is now the day's most "
            "important open process. High demand wins against "
            "everything - the system goes all-in on the vastness "
            "because an unaccommodated vastness is processed as the "
            "highest-priority anomaly. The risk bend is the approach "
            "program outrunning the safety appraisal: approach "
            "scales with vastness, while safety appraisal scales "
            "with perceived control, and at high intensity the two "
            "curves cross - the vastness keeps pulling while control "
            "perception lags. The social silence at peak is the "
            "speech shutdown from the speech record: no language, no "
            "recruiting. The post-peak devotion is consolidation "
            "scheduling: the system that paid heavily for a frame "
            "update protects the investment with repetition. The "
            "simulator escalates by re-bidding: at each intensity "
            "band, re-rank the character's goals with the awe demand "
            "weighted by the band."
        ),
        "key_points": [
            "Low awe loses to the schedule: twenty seconds, then the day continues.",
            "Middle awe beats the schedule: itineraries change, afternoons cancel, miles get driven - the vastness outranks the plan.",
            "High awe dissolves the schedule: the person follows the vastness for hours or days, pilgrim-logic.",
            "The risk bend: at high intensity the approach program outruns the safety appraisal - the rim's edge gets closer.",
            "Afterward comes devotion: the annual return, the eclipse trip, the same-date ritual - high awe writes itself into the calendar.",
        ],
        "requirements": [
            "The escalation curve described across three bands with the schedule as the bidding opponent.",
            "The risk bend explained: approach outrunning safety appraisal, with the alarm wire's vote.",
            "The social-silence-at-peak point included.",
            "The post-peak devotion pattern included.",
            "The simulator re-bidding rule stated.",
        ],
        "standards": [
            "Goal-competition account follows Lazarus 1991 on emotion and goal priority.",
            "Accommodation-priority framing follows Keltner and Haidt 2003.",
            "Threat-bend account follows Gordon et al. 2017 on the threat-based variant.",
        ],
        "citations": [CIT_LAZARUS, CIT_KELTNER_HAIDT, CIT_GORDON],
        "sig_lens": SIG_LENS_DEF,
    },

    # ------------------------------------------------ 26-28 EXPRESSING IT HEALTHILY
    {
        "key": "healthy_expression",
        "name": "Expressing Awe Well: Saying, Showing, Channeling",
        "group": "Expressing It Healthily",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Awe expressed well is awe completed: the feeling runs its "
            "course through the body, the frame, and the social world, "
            "and nothing is left stuck. Saying it comes first and "
            "simplest: voice the minimal honest thing - \"wow,\" "
            "\"look at that,\" \"come see this\" - without apology "
            "and without performance. The research on sharing shows "
            "the telling amplifies the feeling rather than spending "
            "it; awe is one of the emotions that grows when spoken. "
            "Showing it is the body allowed its program: stop when "
            "the vastness arrives, let the gaze lift, let the "
            "stillness happen in public without embarrassment. The "
            "people around you will usually join rather than judge - "
            "the orienting response is contagious. Channeling it is "
            "where awe becomes fuel: write the paragraph, take the "
            "photograph, learn the geology, plan the return. The "
            "accommodation demand is an open question, and open "
            "questions are energy - the curiosity chain from the "
            "triggers section is healthy expression wearing work "
            "clothes. The social channeling matters most: tell the "
            "story at dinner, send the photograph, bring someone next "
            "time. Shared awe consolidates harder - the retelling "
            "rehearses the stretched frame - and it pays the social "
            "dividend the feeling evolved for: the small self, "
            "connected. The creative channeling is the long game: "
            "awe has a documented relationship with inspiration, and "
            "the stretched frame is raw material - the painting, the "
            "song, the design, the changed plan. None of this "
            "requires talent; it requires only that the feeling be "
            "let through instead of around. The check for healthy "
            "expression is simple: a month later, is the frame still "
            "wider? If yes, the awe was expressed well."
        ),
        "how_it_works": (
            "Healthy expression works by completing each phase of the "
            "awe program instead of interrupting it. Voicing the "
            "minimal honest thing completes the social signal: the "
            "system evolved to broadcast awe, and the broadcast "
            "closes the loop - unvoiced awe leaves the sharing "
            "program running in the background. Allowing the body "
            "its stillness completes the intake phase: suppressed "
            "stillness means suppressed intake, which means the "
            "accommodation starts from a thinner registration. "
            "Channeling into learning or making completes the "
            "accommodation phase: the open frame-gap gets filled "
            "with content rather than left as a raw opening, which "
            "is why the curiosity chain feels so satisfying - it is "
            "the demand being met. Social retelling completes "
            "consolidation: each retelling rehearses the stretched "
            "frame and the shared telling adds the connection "
            "dividend. Creative channeling completes the longest "
            "loop: the stretched frame becomes generative, producing "
            "new frames for others. The month-later check works "
            "because completed awe leaves a wider frame and "
            "interrupted awe does not - the frame is the receipt."
        ),
        "key_points": [
            "Say the minimal honest thing - 'wow,' 'look at that' - without apology: the telling amplifies awe rather than spending it.",
            "Let the body run its program in public: stop, lift the gaze, be still - the orienting response is contagious, not embarrassing.",
            "Channel the open question: write it, photograph it, learn the geology, plan the return - curiosity is awe in work clothes.",
            "Tell the story socially: shared awe consolidates harder and pays the connection dividend the feeling evolved for.",
            "The month-later check: is the frame still wider? Completed awe leaves a wider frame; interrupted awe does not.",
        ],
        "requirements": [
            "Three channels covered: saying, showing (bodily), channeling (into learning/making).",
            "The social retelling given its consolidation mechanism.",
            "The creative channeling framed as the long game.",
            "The amplification-not-spending point about sharing stated.",
            "The month-later frame check given as the practical test.",
        ],
        "standards": [
            "Sharing-amplification follows the social function literature (Piff et al. 2015).",
            "Consolidation-through-retelling follows Shiota, Keltner and Mossman 2007.",
            "Accommodation-completion follows Keltner and Haidt 2003.",
        ],
        "citations": [CIT_PIFF, CIT_SHIOTA, CIT_KELTNER_HAIDT],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "unhealthy_expression",
        "name": "The Costs of Bottling Up or Exploding Awe",
        "group": "Expressing It Healthily",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Awe mishandled does not vanish; it goes somewhere, and "
            "the somewheres cost. Bottling is the first mishandling: "
            "the determined unimpressedness - the teenager's shrug at "
            "the museum, the adult's \"seen it\" at the overlook. The "
            "cost is straightforward: suppressed intake means the "
            "accommodation never starts, so the frame never stretches, "
            "so the person pays the price of the vastness (the trip, "
            "the ticket, the moment) without receiving the goods. "
            "Chronic bottling has a second cost: the noticing muscle "
            "atrophies. The frame stays tight, the gaps stop "
            "registering, and the world gradually flattens into the "
            "familiar - which is one working definition of cynicism. "
            "The third cost is social: the bottler's stillness never "
            "comes, so the contagious orienting never fires, and the "
            "people around them get a dimmer experience too - "
            "unimpressedness is also contagious. Exploding is the "
            "second mishandling and it looks different for awe than "
            "for anger: awe exploding is the chase. The person who "
            "felt the sublime once and now pursues it compulsively - "
            "bigger mountains, stronger doses of vastness, the "
            "itinerary as addiction - discovers the hedonic treadmill "
            "wearing an awe costume: the frame adapts, the gaps "
            "shrink, and ever-larger vastness is needed for the same "
            "feeling. The chase also hollows the ordinary: the "
            "sunrise glimpse stops registering because only the "
            "sublime counts, which is the rarity myth as a "
            "self-inflicted wound. The third mishandling is "
            "freezing at the bend: threat-based awe mismanaged as "
            "pure terror, the person who never goes back to heights "
            "or crowds or the ocean - the accommodation routed "
            "entirely to avoidance, and a whole family of vastness "
            "closed off. The common thread: in every case the frame "
            "stops stretching, which is the one thing awe is for."
        ),
        "how_it_works": (
            "The costs work through the interrupted program. Bottling "
            "interrupts at intake: the will suppresses the orienting "
            "response, registration stays thin, and with no gap "
            "registered there is nothing to accommodate - the system "
            "skips the update while paying the exposure cost. Chronic "
            "bottling trains the appraisal: frames that are never "
            "asked to stretch learn not to offer gaps, which is the "
            "atrophy mechanism behind the flattening. The social cost "
            "is emotional contagion running in reverse: the "
            "suppressed display gives others' systems no signal to "
            "orient to. Exploding - the chase - interrupts at the "
            "hedonic level: repeated high-intensity exposure raises "
            "the accommodation baseline, so the same stimulus "
            "produces a smaller gap - tolerance, formally identical "
            "to the treadmill in other reward domains. The hollowing "
            "of the ordinary is contrast: with the baseline set at "
            "the sublime, mild vastness falls below the registration "
            "threshold. Freezing mismanages the threat-based variant "
            "by letting the fear program capture the whole "
            "accommodation: the frame stretches, but around avoidance "
            "rather than around wonder, and the avoidance "
            "generalizes. Every mishandling converges on the same "
            "failure: the frame stops stretching."
        ),
        "key_points": [
            "Bottling: suppressed intake means no gap registered, no accommodation, the price paid without the goods received.",
            "Chronic bottling atrophies noticing: the world flattens into the familiar - cynicism as a trained appraisal.",
            "Unimpressedness is contagious too: the bottler's missing stillness dims the experience for everyone nearby.",
            "Exploding is the chase: tolerance builds, ever-larger vastness is needed, and the ordinary stops registering.",
            "Freezing misroutes threat-based awe entirely into avoidance, closing off whole families of vastness.",
        ],
        "requirements": [
            "Three mishandlings covered: bottling, exploding (the chase), and freezing.",
            "Each given its mechanism and its specific costs.",
            "The tolerance/hedonic-treadmill mechanism explained for the chase.",
            "The social contagion cost of bottling included.",
            "The common thread stated: the frame stops stretching.",
        ],
        "standards": [
            "Suppression costs follow the emotion-regulation literature on expressive suppression.",
            "Tolerance mechanism follows the accommodation-baseline account (Keltner and Haidt 2003).",
            "Avoidance generalization follows Gordon et al. 2017 on the threat-based variant.",
        ],
        "citations": [CIT_KELTNER_HAIDT, CIT_GORDON, CIT_SHIOTA],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "everyday_practices",
        "name": "Everyday Practices That Keep Awe in Balance",
        "group": "Expressing It Healthily",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Awe is trainable, and the training is small enough to fit "
            "a Tuesday. The lookout practice: once a day, stop for "
            "sixty seconds at something larger than the routine - the "
            "sky, the tree, the building's crown - and let the gaze "
            "lift. Sixty seconds is enough for the orienting response "
            "to fire and the frame to loosen a notch. The noticing "
            "log: write down one vast thing per day, however small - "
            "the cloud band, the chord, the question. The log trains "
            "the appraisal the way a tally trains attention: what "
            "gets counted gets seen, and what gets seen starts "
            "counting as awe. The vastness walk: a weekly twenty-"
            "minute walk with the single assignment of finding "
            "something that exceeds a frame - the week's architecture, "
            "the park's oldest tree, the river's width. The shared "
            "tell: recount one awe moment per week to another person, "
            "out loud, with the looping and the insufficient words - "
            "the retelling is consolidation and the listener gets a "
            "secondhand frame-stretch. The learning follow: when awe "
            "opens a question - how deep, how old, how - follow it "
            "for fifteen minutes. The curiosity chain is the cheapest "
            "awe amplifier ever documented: the gap, once opened, "
            "wants filling, and the filling deepens the next gap. The "
            "scale check: when a problem feels enormous, deliberately "
            "set it beside something genuinely vast - the night sky, "
            "deep time - and let the small self right-size it. This "
            "is the perspective tool working as designed, not as "
            "avoidance. The seasonal pilgrimage: once a season, go to "
            "the big thing on purpose - the overlook, the concert, "
            "the dark-sky park - planned awe, unembarrassed. None of "
            "these are treatments for anything; they are practices, "
            "like stretching, for the emotion this database describes. "
            "The dose that the diary studies suggest: weekly noticed "
            "awe is the threshold where the frame stays loose and the "
            "small self stays available."
        ),
        "how_it_works": (
            "The practices work by training the two ingredients "
            "separately. The lookout and the walk train vastness "
            "registration: repeated deliberate exposure lowers the "
            "threshold at which the frame-gap is noticed, which is "
            "the trainable part of the myths record. The log trains "
            "the appraisal label: writing \"vast thing\" rehearses "
            "the categorization, and categorized experiences "
            "consolidate better. The shared tell trains the social "
            "loop: voicing completes the broadcast program and the "
            "listener's co-registration amplifies the appraisal. "
            "The learning follow trains accommodation directly: each "
            "followed question is a completed frame update, and "
            "completed updates keep the accommodation machinery "
            "willing - the system that gets to finish its work "
            "volunteers for more. The scale check uses the small "
            "self as a tool: deliberately invoking the vast frame "
            "re-weights the problem's apparent size, which is the "
            "perspective effect working intentionally. The seasonal "
            "pilgrimage is dose maintenance: the diary literature "
            "suggests weekly noticed awe as the threshold, and the "
            "pilgrimage is the quarterly booster that keeps the "
            "weekly practice honest. Together they are a training "
            "program for the frame: notice gaps, label them, share "
            "them, fill them, use them."
        ),
        "key_points": [
            "The lookout: sixty seconds a day at something larger than the routine - enough for the orienting response to fire.",
            "The noticing log: one vast thing per day written down - what gets counted gets seen.",
            "The vastness walk and the shared tell: weekly seeking plus weekly retelling - consolidation with a witness.",
            "The learning follow: fifteen minutes on the question awe opens - the cheapest awe amplifier documented.",
            "The scale check and the seasonal pilgrimage: deliberate perspective-right-sizing plus quarterly planned awe.",
        ],
        "requirements": [
            "At least six concrete practices, each with a dose (seconds, minutes, weekly).",
            "Each practice mapped to which ingredient or phase it trains.",
            "The weekly-noticed-awe threshold cited from the diary literature.",
            "Practices framed as training, explicitly not as treatment for anything.",
            "The program summarized as a single training loop.",
        ],
        "standards": [
            "Frequency threshold follows the daily-diary awe literature (Shiota, Keltner and Mossman 2007).",
            "Training logic follows the noticing-as-trainable claim of the myths record.",
            "Consolidation mechanism follows Piff et al. 2015 and the retelling literature.",
        ],
        "citations": [CIT_SHIOTA, CIT_PIFF, CIT_KELTNER_HAIDT],
        "sig_lens": SIG_LENS_DEF,
    },

    # ------------------------------------------------ 29-31 RECOGNIZING IT IN OTHERS
    {
        "key": "reading_signs",
        "name": "Reading Awe in Others: Face, Body, Voice, Behavior",
        "group": "Recognizing It in Others",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Reading awe in another person is a four-channel skill, "
            "and the channels confirm each other. The face channel: "
            "brows lifted from the inner corners, eyes widened and "
            "fixed, mouth slightly open, gaze aimed up or outward at "
            "the vast thing - the intake chord from the face record. "
            "At a distance the face may be unreadable, which is when "
            "the body channel takes over: the arrest is the "
            "long-range signal - the person has stopped mid-stride, "
            "mid-gesture, and is not moving. Orientation is the "
            "second body tell: turned toward the vastness, head "
            "tilted up, the whole body aimed like an antenna. The "
            "voice channel: listen for the hush - volume dropped, "
            "pace slowed, the minimal syllables (\"wow,\" \"oh\") "
            "breathed rather than projected. Silence itself is a "
            "voice cue in awe: the talkative person gone quiet at "
            "the rim is reporting the feeling by omission. The "
            "behavior channel: pointing without looking at you (the "
            "finger goes to the vastness while the eyes stay on it), "
            "the sleeve-grab, the photograph raised but the person "
            "not looking through it yet - capturing can wait, "
            "registering cannot. The skin channel, when you are close "
            "enough: goosebumps on the forearms, the visible shiver. "
            "The confirmation rule: any two channels agreeing is a "
            "read; three is certainty. The most common misread is "
            "mistaking the arrest for confusion or the hush for "
            "boredom - the correction is the orientation: confused "
            "people look around, bored people look away, awed people "
            "look up and stay. And the threat-based tell: if the "
            "stillness comes with white knuckles on the rail, read "
            "the blend, not the pure flavor - the person is in the "
            "sublime and may need the anchor more than the view."
        ),
        "how_it_works": (
            "The four-channel read works because awe's program is "
            "redundant by design: the same appraisal drives the face "
            "(aperture), the body (arrest and orient), the voice "
            "(hush), and the behavior (share and capture) in "
            "parallel, so the channels corroborate. The "
            "two-channel confirmation rule manages the base rates: "
            "any single channel can misfire - a widened eye can be "
            "surprise, a hush can be a library - but two independent "
            "channels agreeing drives the false-positive rate down "
            "sharply, and three makes it negligible. The orientation "
            "correction works because attention direction "
            "discriminates the confusions: confusion scans (seeking "
            "information to resolve), boredom averts (withdrawing "
            "attention), awe fixes upward (sustaining intake). The "
            "threat-based tell works because the grip is the "
            "withdrawal program's visible component running alongside "
            "approach: white knuckles mean the safety appraisal is "
            "active, which changes what the person needs from a "
            "companion. The read is descriptive, never diagnostic: "
            "it names the visible pattern so the observer can "
            "respond well, not to label the person."
        ),
        "key_points": [
            "Four channels: the intake face, the arrested and oriented body, the hushed minimal voice, the pointing-and-capturing behavior.",
            "The arrest is the long-range signal: stopped mid-stride in a vast place reads before any face does.",
            "Silence is a voice cue: the talkative person gone quiet at the rim reports by omission.",
            "The confirmation rule: two channels agreeing is a read, three is certainty - orientation corrects the confusion/boredom misreads.",
            "The threat-based tell: stillness plus white knuckles means the blend - the person may need the anchor more than the view.",
        ],
        "requirements": [
            "Four channels described with specific tells in each.",
            "The long-range (arrest) and close-range (skin) signals distinguished.",
            "The confirmation rule stated with the false-positive logic.",
            "The two most common misreads named with their corrections.",
            "The descriptive-not-diagnostic boundary stated.",
        ],
        "standards": [
            "Channel redundancy follows the multi-component emotion account (Scherer-style component model; Keltner and Haidt 2003).",
            "Display description follows Shiota, Keltner and Mossman 2007.",
            "Threat-blend tell follows Gordon et al. 2017.",
        ],
        "citations": [CIT_KELTNER_HAIDT, CIT_SHIOTA, CIT_GORDON],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "supportive_responses",
        "name": "What to Say and Do Around Someone Feeling Awe",
        "group": "Recognizing It in Others",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Someone near you is in awe - at the rim, in the concert "
            "hall, under the sky - and the right response is mostly "
            "about not breaking the spell while keeping the door open. "
            "Do: be still with them. The shared stillness is the "
            "deepest form of company awe allows; the orienting "
            "response is contagious, and joining it says \"I see it "
            "too\" without spending a word. Do: follow their gaze. "
            "Look where they are looking, not at them - the vastness "
            "is the third party in the conversation. Do: offer the "
            "minimal syllable when it comes naturally - a breathed "
            "\"wow\" in return is communion, not interruption. Do: "
            "wait for the retelling. The story will come - minutes "
            "later, at dinner, on the drive home - and that is when "
            "your full attention pays: ask the open question (\"what "
            "was the moment for you\"), let the looping run, do not "
            "rush to your own version. Do: in threat-based awe, be "
            "the anchor - a steady presence near the rail, no "
            "pressure toward or away from the edge, your calm lending "
            "their safety appraisal a data point. Do: later, invite "
            "the return - \"we should bring them next time\" turns "
            "the moment into a ritual and the ritual into a bond. "
            "The underlying principle: awe is the one emotion where "
            "the best support is co-presence rather than intervention. "
            "You are not fixing, cheering, or processing - you are "
            "witnessing alongside, which is exactly what the feeling "
            "evolved to recruit."
        ),
        "how_it_works": (
            "The supportive responses work by cooperating with the awe "
            "program instead of competing with it. Shared stillness "
            "works through contagion and validation: the companion's "
            "arrest confirms the appraisal (this is worth stopping "
            "for) and the co-orientation amplifies it - two systems "
            "registering the same vastness each raise the other's "
            "signal. Gaze-following works because it honors the "
            "attention economics: the awed person's channel is fully "
            "allocated to the vastness, and demanding eye contact or "
            "conversation would tax the accommodation. The minimal "
            "syllable works as a social ping at near-zero cost: it "
            "signals co-presence without requiring processing. "
            "Waiting for the retelling works because consolidation "
            "needs the narration phase: the open question scaffolds "
            "the rehearsal that writes the stretched frame into "
            "memory. Anchor-presence in threat-based awe works on the "
            "safety appraisal directly: a calm companion is evidence "
            "of manageability, which tilts the blend toward the "
            "sublime and away from fear. Inviting the return works "
            "as ritual formation: shared repetition is how the "
            "connection dividend compounds. The principle holds "
            "because awe's social function is witnessing, not "
            "rescuing."
        ),
        "key_points": [
            "Be still with them: shared stillness is the deepest company awe allows - contagious orienting that says 'I see it too.'",
            "Follow their gaze, not their face: the vastness is the third party in the conversation.",
            "Offer the minimal syllable naturally and wait for the retelling - then give the looping story your full attention.",
            "In threat-based awe, be the anchor: steady presence near the rail, no pressure either way, your calm as safety data.",
            "Later, invite the return: turning the moment into a shared ritual compounds the connection dividend.",
        ],
        "requirements": [
            "At least five supportive actions, each with its mechanism.",
            "The co-presence-not-intervention principle stated.",
            "The threat-based anchor role distinguished from the pure-awe role.",
            "The retelling phase given its scaffolding questions.",
            "The ritual-formation payoff included.",
        ],
        "standards": [
            "Contagion and co-registration follow Piff et al. 2015 on awe and connection.",
            "Consolidation scaffolding follows Shiota, Keltner and Mossman 2007.",
            "Safety-appraisal support follows Gordon et al. 2017.",
        ],
        "citations": [CIT_PIFF, CIT_SHIOTA, CIT_GORDON],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "mistakes",
        "name": "The Mistakes That Make Awe Feel Worse",
        "group": "Recognizing It in Others",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Awe is fragile mid-flight, and the people around it break "
            "it in predictable ways. Mistake one: narrating over the "
            "moment - the running commentary (\"this reminds me of the "
            "time we...\", \"did you know this canyon is...\") while "
            "the other person is in full intake. The commentary taxes "
            "the exact channel the accommodation needs, and the spell "
            "breaks like a dropped call. Mistake two: rushing - "
            "\"okay, got the photo, let's go\" - which aborts the "
            "dwell the system was using to finish the frame update; "
            "the person leaves with the gap half-open and the "
            "aftershock never comes. Mistake three: performing "
            "unimpressedness - the shrug, the \"it's just rocks\" - "
            "which does not merely withhold validation but actively "
            "contracts the social field: the awed person, reading the "
            "dismissal, often suppresses the rest of the feeling out "
            "of embarrassment, and the suppression costs them the "
            "accommodation. Mistake four: making it about you - "
            "hijacking the retelling with your own bigger story "
            "(\"that's nothing, you should see...\") - which steals "
            "the consolidation phase the teller needed. Mistake five: "
            "forcing the interpretation - telling the awed person what "
            "the moment means, especially in the first minutes. The "
            "frame is still stretching; premature meaning is a cast "
            "on a growing bone. Mistake six, specific to threat-based "
            "awe: mocking the fear - \"don't be scared, it's just a "
            "view\" - which shames the alarm wire that was doing "
            "legitimate safety work and teaches the person to distrust "
            "the blend's honest signal. The repair for every mistake "
            "is the same shape: stop, be still, follow the gaze, and "
            "let the moment re-inflate - awe is remarkably "
            "re-coverable if the vastness is still there."
        ),
        "how_it_works": (
            "The mistakes work - destructively - by attacking the awe "
            "program's scarcest resources. Narrating over the moment "
            "attacks the attentional channel: accommodation is "
            "cognitively expensive, and competing verbal input forces "
            "a task-switch that collapses the intake state. Rushing "
            "attacks dwell time: the frame update is incomplete, and "
            "an incomplete update consolidates poorly - hence the "
            "missing aftershock. Performed unimpressedness attacks "
            "the social validation loop: the appraisal is partly "
            "socially constructed, and a dismissive witness "
            "down-regulates the vastness appraisal itself, not just "
            "its display. Hijacking the retelling attacks "
            "consolidation: the narrator needs the rehearsal to write "
            "the frame, and the interruption leaves the update "
            "unwritten. Forced interpretation attacks the open gap: "
            "meaning imposed before accommodation finishes gets "
            "encoded as the frame, which is smaller than the frame "
            "the vastness would have built. Mocking the fear attacks "
            "the safety appraisal's legitimacy: the alarm wire, "
            "shamed, either goes silent (risk blindness next time) "
            "or gets louder (the person avoids all vastness). The "
            "repair works because the stimulus persists: re- "
            "establishing stillness and gaze re-opens the intake "
            "channel and the program resumes where it left off."
        ),
        "key_points": [
            "Narrating over the moment breaks the spell: commentary taxes the exact channel accommodation needs.",
            "Rushing aborts the dwell: the frame update stays half-open and the aftershock never comes.",
            "Performed unimpressedness contracts the social field: the awed person suppresses from embarrassment and loses the update.",
            "Hijacking the retelling steals consolidation; forcing early interpretation casts the still-growing frame.",
            "Mocking the fear in threat-based awe shames legitimate safety work - and every mistake repairs the same way: stop, be still, follow the gaze.",
        ],
        "requirements": [
            "Six mistakes named, each with its mechanism of damage.",
            "The threat-based-specific mistake (mocking the fear) included.",
            "Each mistake mapped to which awe resource it attacks.",
            "The universal repair given.",
            "Tone corrective but not shaming: mistakes described as predictable, repairs as simple.",
        ],
        "standards": [
            "Attentional-channel account follows the accommodation-cost framing (Keltner and Haidt 2003).",
            "Social-construction of appraisal follows Barrett 2017.",
            "Safety-appraisal legitimacy follows Gordon et al. 2017.",
        ],
        "citations": [CIT_KELTNER_HAIDT, CIT_BARRETT, CIT_GORDON],
        "sig_lens": SIG_LENS_DEF,
    },

    # ------------------------------------------------ 32-34 RELATED EMOTIONS AND MIXES
    {
        "key": "neighbors",
        "name": "Awe's Neighbors: Related Emotions and How to Tell Them Apart",
        "group": "Related Emotions and Mixes",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Awe's neighborhood is crowded, and the cousins get "
            "confused constantly. Here is the map with the tell-apart "
            "rules. WONDER is awe's closest neighbor: the difference "
            "is curiosity-forward versus vastness-forward. Wonder asks "
            "questions; awe receives scale. Tell-apart: if the dominant "
            "urge is to investigate (lean in, ask how), it is wonder; "
            "if the dominant state is arrested reception (stopped, "
            "staring, small), it is awe. They blend constantly - the "
            "telescope line is wonder walking into awe. AMAZEMENT is "
            "surprise leaning toward the vast: faster onset, shorter "
            "duration, less small-self. Tell-apart: amazement startles "
            "then recovers; awe stills then lingers. The dropped jaw "
            "at the magic trick is amazement; the twenty-minute "
            "silence after is awe arriving late. ADMIRATION is awe "
            "aimed at a person: the virtuoso, the hero, the moral "
            "exemplar. Tell-apart: admiration wants to be like the "
            "target (approach and emulate); awe wants to be near the "
            "vastness (approach and receive). You admire the "
            "climber; you are awed by the mountain. REVERENCE is awe "
            "aimed at the deeply respected, with deference added: "
            "slower, quieter, more bowed. Tell-apart: reverence "
            "guards its behavior (hushed, careful); awe forgets its "
            "behavior (arrested, open). FEAR is the neighbor across "
            "the safety line: same vastness, flipped appraisal. "
            "Tell-apart: fear wants distance and plans escape; "
            "threat-based awe wants the rail and stays. SURPRISE is "
            "the brief neighbor: pure novelty with no vastness "
            "requirement. Tell-apart: surprise resolves in seconds "
            "into another emotion; awe is the destination, not the "
            "doorway. ELEVATION (the warm uplift at moral beauty) is "
            "the heart-neighbor: tell-apart by the body - elevation "
            "warms the chest and moves people to tears of tenderness; "
            "awe widens the eyes and stills the limbs. The map's "
            "practical use: name the neighbor correctly and the "
            "response follows - wonder wants answers, amazement wants "
            "a replay, admiration wants a model, reverence wants "
            "care, fear wants distance, surprise wants a moment, "
            "elevation wants to give, and awe wants witnesses and "
            "time."
        ),
        "how_it_works": (
            "The tell-apart rules work because each neighbor differs "
            "from awe on at least one of the two ingredients or the "
            "action program. Wonder shares the accommodation demand "
            "but aims it at investigation rather than reception - "
            "different action tendency, same stretch. Amazement "
            "shares the vastness flash but not the sustained "
            "accommodation - shorter time course, no small self. "
            "Admiration shares the positive appraisal of something "
            "greater but targets an agent, which changes the "
            "relational theme from vastness to excellence and the "
            "action from receiving to emulating. Reverence adds "
            "deference to awe's reception - the behavioral program "
            "gains inhibition, which is why reverence looks careful "
            "where awe looks arrested. Fear shares the stimulus "
            "(the vast thing) but flips the safety appraisal, which "
            "flips the action program from approach-receive to "
            "avoid-escape. Surprise shares only the novelty onset - "
            "no vastness requirement, no accommodation demand beyond "
            "the orienting. Elevation shares the moral-vastness "
            "elicitor class but runs a warmth-and-tenderness body "
            "program rather than a wideness-and-stillness one. The "
            "response-follows rule works because each program's "
            "needs differ: answers for wonder, time for awe."
        ),
        "key_points": [
            "Wonder asks questions, awe receives scale: investigate-urge means wonder, arrested reception means awe.",
            "Amazement startles then recovers; awe stills then lingers - the magic trick versus the twenty-minute silence.",
            "Admiration targets a person and wants emulation; awe targets vastness and wants reception - the climber versus the mountain.",
            "Reverence adds deference: hushed and careful where awe is arrested and open.",
            "Fear flips the safety appraisal (distance and escape); surprise is the brief doorway; elevation warms where awe widens.",
        ],
        "requirements": [
            "Seven neighbors mapped: wonder, amazement, admiration, reverence, fear, surprise, elevation.",
            "Each with a concrete tell-apart rule stated as a behavioral test.",
            "Each difference grounded in ingredients or action program in how_it_works.",
            "The response-follows summary: each neighbor's distinct need.",
            "Examples concrete (climber/mountain, magic trick, telescope line).",
        ],
        "standards": [
            "Neighbor distinctions follow Keltner and Haidt 2003 on awe's elicitor classes and variants.",
            "Relational-theme framing follows Lazarus 1991.",
            "Elevation distinction follows the moral-elevation literature (Haidt's elevation work).",
        ],
        "citations": [CIT_KELTNER_HAIDT, CIT_LAZARUS, CIT_SHIOTA],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "mixes",
        "name": "Awe Blends: Emotion Mixes, Plutchik-Style",
        "group": "Related Emotions and Mixes",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Awe blends the way colors do, and the blends have their "
            "own weather. AWE plus FEAR is the sublime, covered in its "
            "own record: wideness braided with alarm, the rail gripped, "
            "the frame stretching under load. It is the most common "
            "blend because the world's vast things are so often its "
            "dangerous things, and it is the blend with the sharpest "
            "after-effect - load-tested confidence. AWE plus JOY is "
            "wonder-struck delight: the eyepiece Saturn with the laugh, "
            "the choir's climax with the grin breaking through the "
            "tears. The small self and the inner yes arrive together, "
            "and the result is the most sought-after feeling in the "
            "whole neighborhood - expansive and warm at once, the "
            "reason people chase eclipses. The tell: the awe face with "
            "the smile muscles joining late, the \"wow\" turning into "
            "laughter. AWE plus SADNESS is the bittersweet sublime: "
            "the overlook visited after the loss, the vastness holding "
            "the grief without fixing it. The small self meets the "
            "heavy heart and the combination is strangely consoling - "
            "the grief is not smaller, but the world is larger around "
            "it, which is sometimes exactly the proportion that helps. "
            "The tell: watering eyes with no smile, the long exhale, "
            "the gaze that stays on the distance. AWE plus LOVE is "
            "devotion: the vastness and the beloved in the same frame - "
            "the partner beside you at the rim, the child asleep in "
            "the vast quiet house. The small self and the bonded self "
            "coincide, and the result is the feeling people describe "
            "with the fewest words and the most certainty. The tell: "
            "the hand found without looking, the shared stillness that "
            "needs no sleeve-grab. AWE plus DISGUST is the dark "
            "sublime's stranger cousin: the vastness that repels - the "
            "charnel vastness of the battlefield memorial, the "
            "overwhelming scale of a disaster's aftermath. The frame "
            "stretches around horror rather than wonder, and the "
            "accommodation is the hardest kind: making room for what "
            "should not be. The simulator's blending rule: name the "
            "partner, set the ratio, and let each ingredient keep its "
            "own program - the blend is a duet, not a new solo."
        ),
        "how_it_works": (
            "The blends work because awe's two ingredients combine "
            "independently with the partner's program. In awe plus "
            "fear, the vastness appraisal is shared and the safety "
            "appraisal splits - approach-receive and avoid-escape run "
            "in parallel, producing the rail-grip. In awe plus joy, "
            "the positive appraisals align: vastness plus goal-"
            "conduciveness, small self plus inner yes - the programs "
            "reinforce, which is why the blend is the most euphoric. "
            "In awe plus sadness, the vastness appraisal meets the "
            "loss appraisal: the frame stretches around the grief "
            "rather than resolving it, which is why the consolation "
            "is proportional rather than curative - the world gets "
            "bigger, the loss stays the same size, and the ratio "
            "heals. In awe plus love, the small self meets the "
            "bonded self: diminished boundaries plus attachment "
            "produce merging without loss of the vastness - the rare "
            "blend where both programs point outward. In awe plus "
            "disgust, the accommodation demand meets the rejection "
            "program: the frame must stretch to include what the "
            "system wants to expel, which is why this blend is the "
            "most effortful and the most transformative when it "
            "completes. The duet rule holds because the ingredients "
            "do not fuse - each keeps its appraisal, its body, its "
            "action tendency, and the felt blend is their "
            "counterpoint."
        ),
        "key_points": [
            "Awe plus fear is the sublime: wideness braided with alarm, the rail gripped, load-tested confidence after.",
            "Awe plus joy is wonder-struck delight: the small self and the inner yes together - the most sought-after feeling in the neighborhood.",
            "Awe plus sadness is the bittersweet sublime: the world gets larger around the grief, and the proportion consoles.",
            "Awe plus love is devotion: the small self and the bonded self coinciding, the hand found without looking.",
            "Awe plus disgust is the dark sublime's cousin: the frame stretching around horror - the hardest, most transformative accommodation.",
        ],
        "requirements": [
            "Five blends described: fear, joy, sadness, love, disgust.",
            "Each blend with its felt texture, its tell, and its after-effect.",
            "Each blend's mechanism given in how_it_works via the duet rule.",
            "The bittersweet proportion-consolation explained, not just named.",
            "The blending rule stated for the simulator: duet, not solo.",
        ],
        "standards": [
            "Blend logic follows the dyad tradition (Plutchik-style combination of neighboring emotions).",
            "Sublime blend follows Gordon et al. 2017.",
            "Prosocial/warm blends follow Piff et al. 2015 and Shiota, Keltner and Mossman 2007.",
        ],
        "citations": [CIT_GORDON, CIT_PIFF, CIT_SHIOTA],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "full_simulation",
        "name": "The Full Awe Simulation: From Trigger to Resolution",
        "group": "Related Emotions and Mixes",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The archive's showcase: one awe, whole, from trigger to "
            "resolution, in scenes. SCENE ONE - THE APPROACH. Late "
            "afternoon, a coastal trail, two friends walking. The "
            "conversation is ordinary - work, the car, the week. The "
            "trail bends. Neither of them has been here before. "
            "SCENE TWO - THE TRIGGER. The bend opens onto the headland "
            "and the ocean is simply there: gray-green to the horizon, "
            "the cliffs falling three hundred feet to white water, a "
            "sea stack standing offshore like something placed. Both "
            "of them stop mid-step. The talking dies. Friend A: "
            "breath catches audibly. Friend B: \"oh -\" and nothing "
            "after. The vastness registers: perceptual, immediate, "
            "unprepared - the ambush gap at full width. SCENE THREE "
            "- THE PEAK. Ninety seconds in. Both are at the rail - "
            "there is a rail, thankfully, because the drop is real "
            "and the alarm wire is humming underneath the wonder: "
            "threat-based awe at a 70-30 ratio, mostly sublime. "
            "Brows high, eyes wide, mouths open. Goosebumps on A's "
            "forearms, visible. B's eyes are wet. A's hand finds the "
            "rail and grips; B's hand finds A's sleeve and holds. "
            "The small self arrives: the week, the car, the work "
            "argument - all of it correctly sized at last, which is "
            "to say, small. Time slows; the ninety seconds feel like "
            "ten minutes. SCENE FOUR - THE TURN. Minute four. The "
            "peak loosens by a notch. A breathes out - the long "
            "exhale - and laughs once, disbelieving. B says \"look "
            "at that light,\" pointing at the sun breaking under the "
            "cloud bank and turning the water to hammered copper. "
            "The sharing program engages: they are witnesses for "
            "each other now, and the feeling doubles in the telling. "
            "A takes the photograph; both know it will not hold it. "
            "SCENE FIVE - THE CHAIN. Minute ten, walking back along "
            "the cliff path, slower than they came. The conversation "
            "is different now: the gratitude link fires first (\"we "
            "are lucky to -\"), then the connection link (plans to "
            "bring the kids, the parents), then the curiosity link "
            "(how old is the stack, how far the horizon). The "
            "generosity link will fire at dinner, when the tip is "
            "larger than usual and neither mentions why. SCENE SIX "
            "- THE RESOLUTION. Night, the porch, the day nearly done. "
            "A looks up: the sky is clear enough for stars. The "
            "morning's frame is still loose - the stars get a longer "
            "look than they would have yesterday. The aftershock "
            "schedule: tonight the headland replays at the sleep "
            "edge; this week the work problems stay right-sized; "
            "this year the trail becomes the annual walk; in thirty "
            "years both friends will remember the copper water. The "
            "frame stretched, and did not spring all the way back. "
            "That is the whole of it: trigger, peak, turn, chain, "
            "resolution - the emotion completing its program, the "
            "archive's proof that awe can be simulated faithfully, "
            "scene by scene, with nothing diagnosed and no one "
            "labeled."
        ),
        "how_it_works": (
            "The full simulation works by sequencing every mechanism "
            "in this database in its documented order. The approach "
            "establishes the tight frame: ordinary conversation, "
            "ordinary concerns, no preparation - maximizing the gap "
            "for the ambush rule. The trigger fires the two-"
            "ingredient appraisal at full width: perceptual vastness "
            "plus maximum accommodation demand, producing the "
            "arrest, the caught breath, the dying sentence. The "
            "peak runs the body program at full amplitude - "
            "brows, eyes, mouth, goosebumps, watering eyes - with "
            "the threat-based blend set at 70-30, so the rail-grip "
            "and sleeve-hold appear as the approach-withdrawal "
            "duet. The small self arrives on schedule with the "
            "time-slowing, both documented effects. The turn shows "
            "the fade beginning: the long exhale, the disbelieving "
            "laugh, the sharing program engaging - witnesses "
            "recruited, the photograph as re-cue device. The chain "
            "runs the cascade record in order: gratitude, "
            "connection, curiosity, with generosity deferred to "
            "dinner as the Piff link. The resolution runs the "
            "aftershock schedule: sleep-edge replay, week-long "
            "right-sizing, annual ritual formation, thirty-year "
            "memory - the consolidation curve from the time-course "
            "record. Every beat is traceable to a record above; the "
            "simulation is the database performing itself."
        ),
        "key_points": [
            "Scene one, the approach: tight ordinary frame, no preparation - the ambush gap at maximum width.",
            "Scene two, the trigger: the headland, the arrest, the dying sentence - the two-ingredient appraisal firing.",
            "Scene three, the peak: full body program plus the 70-30 threat blend - rail gripped, sleeve held, small self arriving.",
            "Scene four, the turn: the exhale, the laugh, the sharing program - witnesses recruited, the photograph taken.",
            "Scenes five and six, the chain and the resolution: gratitude to generosity, then the aftershock schedule - replay, right-sizing, ritual, thirty-year memory.",
        ],
        "requirements": [
            "Six scenes in documented order: approach, trigger, peak, turn, chain, resolution.",
            "Every beat traceable to an earlier record in this database.",
            "The threat-based blend given an explicit ratio (70-30).",
            "The aftershock schedule concretized: tonight, this week, this year, thirty years.",
            "No real persons; composite illustrative characters. Nothing diagnosed, no one labeled.",
        ],
        "standards": [
            "Sequencing follows the time-course record (onset, climb, peak, fade, aftershock).",
            "Blend ratio follows Gordon et al. 2017 on the threat-based variant.",
            "Chain order follows Piff et al. 2015 and the chain-reactions record.",
        ],
        "citations": [CIT_KELTNER_HAIDT, CIT_GORDON, CIT_PIFF],
        "sig_lens": SIG_LENS_DEF,
    },
]

assert len(ENTRIES) == 34, "expected 34 entries, got %d" % len(ENTRIES)
