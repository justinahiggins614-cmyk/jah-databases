#!/usr/bin/env python3
"""Record entries for the Contempt Emotion databases (Manon's 2026-10-17 16:15
emotion-series order, batch 2).

34 ladder-ordered full records (public-harvest: real, fact-checked emotion
psychology; sig_lens: his original Signature Emotion Method interpretation).
Descriptive and educational ONLY - never diagnoses real people, never labels
any real person with an emotional state, never offers therapeutic advice
beyond general, safe, everyday guidance.
"""

C_EKMAN = ("Ekman P, Friesen WV. A new pan-cultural facial expression of "
           "emotion. Motivation and Emotion. 1986;10(2):159-168.")
C_CAD = ("Rozin P, Lowery L, Imada S, Haidt J. The CAD triad hypothesis: "
         "A mapping between three moral emotions (contempt, anger, disgust) "
         "and three moral codes (community, autonomy, and divinity). "
         "Journal of Personality and Social Psychology. "
         "1999;76(4):574-586.")
C_GOTTMAN = ("Gottman JM. Why Marriages Succeed or Fail. "
             "Simon and Schuster; 1994.")
C_HAIDT = ("Haidt J. The moral emotions. In: Davidson RJ, Scherer KR, "
           "Goldsmith HH, eds. Handbook of Affective Sciences. "
           "Oxford University Press; 2003:852-870.")
C_HG = ("Hutcherson CA, Gross JJ. The moral emotions: A "
        "social-functionalist account of anger, disgust, and contempt. "
        "Journal of Personality and Social Psychology. "
        "2011;100(4):719-737.")
C_FR = ("Fischer AH, Roseman IJ. Beat them or ban them: The "
        "characteristics and social functions of anger and contempt. "
        "Journal of Personality and Social Psychology. "
        "2007;93(1):103-115.")
C_MELWANI = ("Melwani S, Mueller JS, Overbeck JR. Looking down: The "
             "influence of contempt and compassion on emergent leadership "
             "in task groups. Journal of Personality and Social Psychology. "
             "2012;103(6):1171-1185.")
C_IZARD = "Izard CE. Human Emotions. Plenum Press; 1977."
C_DARWIN = ("Darwin C. The Expression of the Emotions in Man and Animals. "
            "John Murray; 1872.")

SIG_TAIL = ("Signature original - his original Signature Emotion Method: "
            "the Signature system reads contempt as the hierarchy signal - "
            "the cold weight of the scale, the measure that finds another "
            "person wanting; the archive's honesty test about pride and "
            "humility - clearly labeled Signature-made, never presented as "
            "authentic public record.")

ENTRIES = [
    {
        "key": "what-is",
        "name": "What Contempt Is: A Plain-Language Definition",
        "group": "Description",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Contempt is the feeling of looking down on someone - a cool, judging "
            "sense that another person is beneath consideration, unworthy of respect, "
            "or simply less. Where anger wants to confront and disgust wants to push "
            "away, contempt wants to dismiss: the other person is not even worth the "
            "effort of anger. Psychologists call contempt one of the moral emotions, "
            "part of the CAD triad of contempt, anger, and disgust. It is the emotion "
            "of hierarchy and status: it arises when someone is judged to have failed "
            "as a person - not just failed at a task, but failed in character, "
            "competence, or standing. Its classic signal is distance, not heat: the "
            "contemptuous person feels above the other, calm and certain in the "
            "judgment. Contempt can be quiet or cutting, private or performed. At its "
            "core it carries a verdict: you are less than me, and I do not have to "
            "take you seriously. That verdict is what makes contempt so socially "
            "corrosive and so personally revealing - it tells you where the feeler "
            "places themselves on the ladder."
        ),
        "how_it_works": (
            "Something happens - a person acts foolishly, cruelly, incompetently, or "
            "shamelessly - and the mind appraises it against a standard: how a person "
            "ought to be. When the gap between the standard and the person looks like "
            "a permanent flaw rather than a passing mistake, contempt fires. The "
            "appraisal is comparative and top-down: the feeler ranks themselves above "
            "the target. The body responds with cool, low-arousal signals - a still "
            "posture, a one-sided mouth movement, a slow exhale - rather than the hot "
            "surge of anger. The social function is exclusion and status marking: "
            "contempt signals that someone has fallen below the group's bar, and it "
            "teaches everyone watching where that bar is."
        ),
        "key_points": [
            "Contempt is looking down on someone - judging them as beneath respect or beneath consideration.",
            "It is one of the moral emotions, part of the contempt-anger-disgust triad of social judgment.",
            "The core appraisal is hierarchy: the other person has failed in character or standing, not just in a task.",
            "Contempt is cool and dismissive rather than hot - it excludes instead of confronting.",
            "Its function is status marking: it signals where the feeler believes the bar is, and who fell under it.",
            "The verdict feeling - you are less than me - is what makes contempt socially corrosive and personally revealing.",
        ],
        "requirements": [
            "No equipment needed - this is a reading and reflection record.",
            "A few quiet minutes to sit with the definition.",
            "Willingness to notice the feeling in everyday moments.",
        ],
        "standards": [
            "Public record in the Signature system - descriptive, educational.",
            "Definitions follow standard emotion psychology terminology.",
            "Never diagnoses any real person with any emotional state.",
        ],
        "citations": [C_CAD, C_HAIDT, C_HG],
        "sig_lens": (
            "The Signature lens reads contempt as the hierarchy signal - the cold weight "
            "of the scale. Where the public record describes the appraisal, the Signature "
            "Method adds the measurement reading: every contempt judgment is a self-measurement "
            "printed backwards. The system treats the feeling as the archive's honesty test "
            "about pride and humility: the weight on the scale always tells two stories at once."
        ),
    },
    {
        "key": "family",
        "name": "Contempt in the Emotion Family: The Moral Emotions and the CAD Triad",
        "group": "Description",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Contempt belongs to the family of moral emotions - the feelings that watch "
            "over how people treat each other. The best-known map is the CAD triad: "
            "contempt, anger, and disgust, each matched to a moral code. Contempt answers "
            "to the code of community and hierarchy - the rules about rank, duty, respect, "
            "and how people in different stations ought to behave. Anger answers to the "
            "code of autonomy - harm and fairness, rights violated. Disgust answers to the "
            "code of divinity or purity - the sacred kept clean. So contempt is the "
            "emotion of someone stepping out of their proper place, or of someone proving "
            "unfit for respect. It sits among the complex, social emotions rather than the "
            "fast reflexes: it needs a judgment, a comparison, and a standard. Its closest "
            "relatives are disdain and scorn, both forms of looking down; its partner is "
            "often anger, and the two blend into indignation; its opposite is respect and "
            "admiration, which look up instead of down."
        ),
        "how_it_works": (
            "The family map works by appraisal. First the mind reads the situation: what "
            "happened, who did it, and what code it breaks. If the reading is violation of "
            "hierarchy or community standards - someone beneath their role, someone "
            "shameless, someone incompetent in a position of trust - the contempt branch "
            "of the family activates. If the reading is harm or unfairness, anger takes "
            "the lead. The two share territory and frequently co-occur: researchers find "
            "contempt often rides alongside anger when a target is seen as both wrong and "
            "beneath the feeler. Knowing the family tells you which code was felt to be "
            "broken, and therefore what the feeling is really about."
        ),
        "key_points": [
            "Contempt is a moral emotion in the CAD triad: contempt, anger, and disgust.",
            "It answers to the community and hierarchy code: rank, duty, respect, proper place.",
            "Anger answers to autonomy (harm, fairness); disgust answers to purity (the sacred kept clean).",
            "It is a complex social emotion - it needs a judgment, a comparison, and a standard.",
            "Closest relatives: disdain and scorn; frequent partner: anger; opposite: respect and admiration.",
            "Placing the feeling on the map reveals which moral code was felt to be broken.",
        ],
        "requirements": [
            "No equipment needed - this is a reading and reflection record.",
            "Familiarity with the basic definition of contempt helps.",
            "Willingness to compare contempt with its neighboring emotions.",
        ],
        "standards": [
            "Public record in the Signature system - descriptive, educational.",
            "Family map follows the CAD triad hypothesis literature.",
            "Never diagnoses any real person with any emotional state.",
        ],
        "citations": [C_CAD, C_HAIDT, C_IZARD],
        "sig_lens": (
            "The Signature Method draws the family as a council of watchers: contempt is the "
            "watcher of the stairs, anger the watcher of the road, disgust the watcher of the "
            "gate. In the Signature reading, knowing which watcher sounded tells you which "
            "territory of life the mind believes was crossed - stairs, road, or gate."
        ),
    },
    {
        "key": "intensity",
        "name": "How Strong Contempt Gets: Mild Disdain to Intense Scorn",
        "group": "Description",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Contempt comes in volumes. At the mild end it is a light disdain: a raised "
            "eyebrow at a silly opinion, a private smirk at someone's clumsy attempt, a "
            "feeling that barely interrupts the day. The person is still treated as a "
            "person - just a slightly ridiculous one. In the middle range it becomes "
            "dismissal: the target's words stop landing, their presence gets tuned out, "
            "their name arrives with a curl of the lip. Conversation becomes "
            "performance - polite on the surface, hollow underneath. At the intense end "
            "it becomes scorn and utter rejection: the person is written off entirely, "
            "their whole character judged and filed away. Nothing they do can score "
            "points anymore; even their kindness reads as manipulation. Intensity in "
            "contempt is mostly about permanence: mild contempt judges the moment, "
            "intense contempt judges the person, forever. The stronger it gets, the less "
            "reversible it feels."
        ),
        "how_it_works": (
            "Intensity scales with two things: how deep the judged flaw runs, and how "
            "settled the verdict feels. A single clumsy act produces mild, "
            "moment-bound disdain that fades when the moment passes. A pattern of acts "
            "that the mind reads as character - chronic incompetence, repeated "
            "shamelessness, confirmed inferiority - pushes the dial up, and the verdict "
            "hardens from this act was beneath me to this person is beneath me. At high "
            "intensity the appraisal generalizes: one domain of failure spreads to the "
            "whole person. That is why intense contempt is so stable and so hard to undo "
            "— the mind has reclassified the target, not just reacted to them."
        ),
        "key_points": [
            "Mild contempt is light disdain - a raised eyebrow, a private smirk, barely interrupting the day.",
            "Moderate contempt is dismissal - the target's words stop landing, politeness goes hollow.",
            "Intense contempt is scorn and total rejection - the whole person written off, permanently.",
            "Intensity tracks permanence: mild judges the moment, intense judges the person.",
            "High intensity generalizes: one domain of failure spreads to the whole character.",
            "Intense contempt is unusually stable - the mind has reclassified the target, not just reacted.",
        ],
        "requirements": [
            "No equipment needed - this is a reading and reflection record.",
            "Recall one mild and one strong instance from observation or fiction.",
            "Willingness to notice how verdicts harden with repetition.",
        ],
        "standards": [
            "Public record in the Signature system - descriptive, educational.",
            "Intensity described on a descriptive scale, not a clinical one.",
            "Never diagnoses any real person with any emotional state.",
        ],
        "citations": [C_HG, C_FR, C_HAIDT],
        "sig_lens": (
            "The Signature Method reads the volume dial as the depth of the engraving: mild "
            "contempt writes in pencil on the moment, intense contempt carves the verdict into "
            "the person-file. The Signature honesty test applies at every volume - the deeper "
            "the carving, the louder the question about who is holding the chisel."
        ),
    },
    {
        "key": "myths",
        "name": "Myths and Misunderstandings About Contempt",
        "group": "Description",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Contempt is widely misunderstood. Myth one: contempt is just a stronger anger. "
            "In fact they are different tools - anger confronts and wants change, contempt "
            "dismisses and wants distance; anger is hot and approach-oriented, contempt is "
            "cool and exclusionary. Myth two: contempt is always unjustified snobbery. "
            "Sometimes it is earned judgment: feeling contempt for cruelty or corruption "
            "is the moral emotion doing its job. Myth three: contempt means you hate the "
            "person. Hatred wants the target harmed; contempt often wants nothing at all "
            "from the target - just absence. Myth four: contempt is rare. Research on "
            "relationships shows it is common in everyday life, from marriages to "
            "workplaces to comment sections. Myth five: expressing contempt honestly is "
            "harmless because it is just an opinion. In close relationships it is one of "
            "the most damaging things a person can repeatedly express - the verdict of "
            "worthlessness corrodes trust faster than almost any other message."
        ),
        "how_it_works": (
            "The myths survive because contempt hides inside politeness. Unlike anger, "
            "which announces itself, contempt can be delivered with a smile, a joke, or "
            "silence - so observers misread it as calm, humor, or indifference. People "
            "also confuse the coolness of contempt with control: the feeling looks "
            "mastered, but the judgment underneath is doing steady damage to the "
            "relationship. Clearing the myths matters because it changes what you do "
            "with the feeling: if you think it is anger, you confront; if you recognize "
            "it as contempt, you examine the verdict itself."
        ),
        "key_points": [
            "Contempt is not stronger anger - anger confronts, contempt dismisses; anger is hot, contempt is cool.",
            "Contempt is not always snobbery - it can be earned moral judgment of cruelty or corruption.",
            "Contempt is not hatred - hatred wants harm, contempt often just wants absence.",
            "Contempt is not rare - it shows up in marriages, workplaces, and public life constantly.",
            "Contempt is not harmless honesty - in close relationships it corrodes trust faster than most messages.",
            "The myths hide contempt inside politeness; clearing them changes what you do with the feeling.",
        ],
        "requirements": [
            "No equipment needed - this is a reading and reflection record.",
            "Willingness to question first impressions of the feeling.",
            "A few quiet minutes to sit with each myth.",
        ],
        "standards": [
            "Public record in the Signature system - descriptive, educational.",
            "Myths framed as common misunderstandings, not personal accusations.",
            "Never diagnoses any real person with any emotional state.",
        ],
        "citations": [C_FR, C_GOTTMAN, C_HAIDT],
        "sig_lens": (
            "The Signature Method treats each myth as a fog panel over the scale: myth-fog makes "
            "the weight look like something else - humor, calm, honesty. The Method's job is "
            "defogging: name the panel, lift it, and look at the actual weight sitting on the scale."
        ),
    },
]
ENTRIES += [
    {
        "key": "first-person",
        "name": "Inside the Feeling: A First-Person Passage Through Contempt",
        "group": "Inner Experience",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "There is a specific stillness to it. You are listening to someone explain "
            "themselves, and halfway through the second sentence something in you "
            "steps back. Not in shock, not in pain - in assessment. Your breathing "
            "slows a fraction. Your eyes narrow, not from focus but from distance, "
            "like you are watching through glass. A thought forms, whole and calm: "
            "this person does not know how small they look right now. There is no "
            "heat in your chest, no clenched jaw - there is a kind of cold clarity, "
            "almost pleasant, the satisfaction of having measured someone and found "
            "the measure true. Your mouth wants to do one small thing - one corner "
            "tightening, almost a smile, but it is not warmth. The other person keeps "
            "talking, unaware, and their voice starts to sound far away, like a radio "
            "in another room. You are already somewhere else: above, outside, finished "
            "with them. That is the inside of contempt - not fury, not fear, just the "
            "quiet, certain feeling of looking down."
        ),
        "how_it_works": (
            "The first-person experience of contempt is built from three ingredients "
            "arriving together. First, a comparative appraisal: the mind places the "
            "other below the self on some ladder of worth. Second, a cooling of "
            "arousal: unlike anger's surge, contempt settles the body into low-energy "
            "certainty. Third, a withdrawal of engagement: attention thins out, the "
            "other's words lose their claim on you. The calm is the signature - the "
            "feeling presents itself as clear-sightedness, which is why people trust "
            "it so completely while they are inside it."
        ),
        "key_points": [
            "The inside of contempt is stillness, not heat - a stepping back in assessment.",
            "Attention thins: the other person's voice starts to sound far away.",
            "A cold clarity arrives - the satisfaction of having measured someone and found the measure true.",
            "One corner of the mouth wants to tighten: almost a smile, but not warmth.",
            "The feeling presents itself as clear-sightedness, which is why it is trusted so completely.",
            "The core sensation is finishedness: already above, already outside, already done with them.",
        ],
        "requirements": [
            "No equipment needed - this is a reading and reflection record.",
            "Read slowly; the passage is meant to be felt, not scanned.",
            "Willingness to recognize the stillness in your own past moments.",
        ],
        "standards": [
            "Public record in the Signature system - descriptive, educational.",
            "First-person simulation is illustrative, not a report of any real person.",
            "Never diagnoses any real person with any emotional state.",
        ],
        "citations": [C_HG, C_FR, C_IZARD],
        "sig_lens": (
            "The Signature Method stages the first-person passage as standing on the high step "
            "of the scale-house: the view is wide, the air is cool, and everything below looks "
            "small. The Method whispers the test question here: is the step high because you "
            "climbed, or because you lowered the ground?"
        ),
    },
    {
        "key": "arc",
        "name": "The Arc of Contempt: Onset, Peak, Fading, and Aftershock",
        "group": "Inner Experience",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "Contempt has a distinctive time-shape. Onset is fast and quiet: a single "
            "moment - a foolish remark, a shameless act, a revealed incompetence - "
            "clicks the appraisal into place, often in under a second. There is no "
            "build-up like anger's simmer; the verdict arrives all at once. The peak is "
            "not a spike but a plateau: a cool, sustained certainty that can hold for "
            "minutes, hours, or days without much effort. It does not exhaust itself "
            "the way hot emotions do, because it runs on low energy. Fading is gradual "
            "and conditional: contempt eases only when the verdict is revised - the "
            "person proves themselves, the judgment is questioned, or time simply "
            "buries the trigger. The aftershock is the residue: even after the feeling "
            "fades, the reclassification lingers. The person is remembered as lesser. "
            "That is why contempt leaves a longer shadow than its intensity suggests - "
            "the arc ends, but the file stays edited."
        ),
        "how_it_works": (
            "The arc follows the appraisal, not the body. Onset is the moment the mind "
            "completes the judgment - this person is beneath the standard. The plateau "
            "persists because the judgment is stored as a belief, and beliefs do not "
            "need fresh energy to survive. Fading requires new evidence or deliberate "
            "reappraisal - the verdict has to be appealed. The aftershock is memory "
            "consolidation: the emotional tag gets written into the person's long-term "
            "profile, so the next encounter starts from the edited file. This "
            "belief-based persistence is what separates contempt's arc from the "
            "body-based arcs of fear or disgust."
        ),
        "key_points": [
            "Onset is fast and quiet: the verdict clicks into place, often in under a second.",
            "The peak is a plateau of cool certainty, not a spike - low energy, long lasting.",
            "Fading is gradual and conditional: the verdict must be revised or buried by time.",
            "The aftershock is reclassification: the person is remembered as lesser after the feeling fades.",
            "The arc follows the appraisal, not the body - beliefs persist without fresh energy.",
            "Contempt leaves a longer shadow than its intensity suggests: the file stays edited.",
        ],
        "requirements": [
            "No equipment needed - this is a reading and reflection record.",
            "Trace one remembered arc from trigger to residue.",
            "Willingness to notice how long the residue lasts.",
        ],
        "standards": [
            "Public record in the Signature system - descriptive, educational.",
            "Arc described as a typical time-shape, not a clinical timeline.",
            "Never diagnoses any real person with any emotional state.",
        ],
        "citations": [C_HG, C_FR, C_IZARD],
        "sig_lens": (
            "The Signature Method maps the arc as a carving in four cuts: the strike (onset), the "
            "polish (plateau), the weathering (fading), and the inscription that remains "
            "(aftershock). The Method's interest is the fourth cut - the inscription - because "
            "that is the one that keeps shaping every future measurement of that person."
        ),
    },
    {
        "key": "low-vs-high",
        "name": "Contempt at Low Intensity vs High Intensity: Two Lived Snapshots",
        "group": "Inner Experience",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "Low intensity: You are in a meeting and a colleague makes a suggestion so "
            "naive it is almost charming. Your lips press together for half a second "
            "to hold back a smile - not a kind smile, a superior one. Inside there is "
            "a small private warmth: I know better than that. The moment passes. You "
            "still respect the colleague; you just enjoyed, for three seconds, being "
            "the cleverer one. Nothing changes between you. High intensity: It is "
            "months later and the same colleague has now, in your file, become the "
            "person who never gets it. You hear their voice in the hallway and your "
            "whole body goes still and cold. You do not just doubt this idea - you "
            "doubt everything about them. When they speak in the meeting, you are "
            "already composing the dismissive reply, already certain. Afterward you "
            "catch yourself describing them to someone else with that one-sided "
            "smile, and the description is not about the idea anymore - it is about "
            "who they are. Low intensity judged a moment and moved on. High intensity "
            "judged a person and set up permanent residence."
        ),
        "how_it_works": (
            "The two snapshots differ in scope and staying power. Low-intensity contempt "
            "targets an act and stays local: the appraisal is this was beneath me, the "
            "arousal is a flicker, the residue is zero. High-intensity contempt targets "
            "the person and goes global: the appraisal is you are beneath me, the "
            "arousal is a sustained cold state, the residue is a rewritten profile. "
            "The transition between them is repetition plus generalization - the same "
            "small verdict, applied again and again, until the mind promotes it from "
            "incident to identity. Recognizing which snapshot you are in is the "
            "practical skill: one needs nothing, the other needs an appeal."
        ),
        "key_points": [
            "Low intensity: a flicker of superiority at a naive moment, then it passes with no residue.",
            "High intensity: a sustained cold state where the whole person, not the act, is judged.",
            "The difference is scope: low judges an act, high judges a person.",
            "The difference is staying power: low leaves no residue, high rewrites the person's profile.",
            "The transition is repetition plus generalization: small verdicts promoted from incident to identity.",
            "The practical skill is recognizing which snapshot you are in: one needs nothing, one needs an appeal.",
        ],
        "requirements": [
            "No equipment needed - this is a reading and reflection record.",
            "Compare a mild and a strong moment from observation or fiction.",
            "Willingness to spot the repetition-to-identity transition.",
        ],
        "standards": [
            "Public record in the Signature system - descriptive, educational.",
            "Snapshots are illustrative composites, not reports of real people.",
            "Never diagnoses any real person with any emotional state.",
        ],
        "citations": [C_HG, C_FR, C_GOTTMAN],
        "sig_lens": (
            "The Signature Method frames the two snapshots as pencil versus chisel: the low "
            "snapshot writes the verdict in pencil on the day's page and it smudges away by "
            "evening; the high snapshot takes up the chisel and carves the verdict into the "
            "person-file. The Method's question at the workbench: who authorized the chisel?"
        ),
    },
    {
        "key": "mixed-anger",
        "name": "Contempt Mixed With Anger: The Indignation Blend",
        "group": "Inner Experience",
        "ladder_rank": 5,
        "ladder_tier": "foundations",
        "description": (
            "Contempt's most common partner is anger, and the blend has a name: "
            "indignation. Pure contempt is cool and dismissive - it wants the target "
            "gone from consideration. Pure anger is hot and confrontational - it wants "
            "the target to change. Indignation is both at once: the heat of anger "
            "fused with the looking-down of contempt. It feels like righteous "
            "certainty - not only are you wrong, you are beneath me for being wrong. "
            "The body shows the mix: the jaw and voice of anger riding on the "
            "stillness and the one-sided smile of contempt. Speech in this blend has "
            "a signature texture: moral vocabulary delivered with dismissive "
            "condescension - lectures, corrections, and verdicts pronounced as if to "
            "a child. Researchers note this blend is common because the appraisals "
            "overlap: the same act can be both unfair (anger) and beneath standards "
            "(contempt). Indignation feels powerful and justified, which is exactly "
            "why it deserves a second look - the contempt in it can smuggle "
            "superiority into what presents itself as principle."
        ),
        "how_it_works": (
            "The blend forms when two appraisals fire together. The anger appraisal "
            "reads: a wrong was done, someone must answer. The contempt appraisal "
            "reads: the wrongdoer is beneath the standard of a decent person. Each "
            "appraisal feeds the other: anger's urgency makes contempt's verdict feel "
            "pressing, and contempt's certainty makes anger's demand feel "
            "unquestionable. The result is a self-sealing state - doubt has nowhere "
            "to enter, because the heat supplies conviction and the cold supplies "
            "dismissal of counter-evidence. That is why indignation is so stable and "
            "so hard to argue with from the outside."
        ),
        "key_points": [
            "Contempt's most common partner is anger; the blend is called indignation.",
            "Pure contempt dismisses, pure anger confronts - indignation does both at once.",
            "The blend feels like righteous certainty: not only wrong, but beneath me for being wrong.",
            "The body shows the mix: anger's jaw and voice on contempt's stillness and one-sided smile.",
            "The appraisals overlap: one act can be both unfair (anger) and beneath standards (contempt).",
            "Indignation is self-sealing: heat supplies conviction, cold dismisses counter-evidence.",
        ],
        "requirements": [
            "No equipment needed - this is a reading and reflection record.",
            "Familiarity with the basic definitions of contempt and anger.",
            "Willingness to examine righteous feelings with a second look.",
        ],
        "standards": [
            "Public record in the Signature system - descriptive, educational.",
            "Blend described via appraisal theory, not clinical terms.",
            "Never diagnoses any real person with any emotional state.",
        ],
        "citations": [C_FR, C_HG, C_HAIDT],
        "sig_lens": (
            "The Signature Method reads indignation as the scale with a furnace underneath: the "
            "cold weight of contempt heated by anger's fire. The Method's warning label is "
            "plain - a heated scale weighs nothing accurately. Let the metal cool before trusting "
            "the reading."
        ),
    },
    {
        "key": "day-in-life",
        "name": "A Day in the Life: Contempt Running Through an Ordinary Day",
        "group": "Inner Experience",
        "ladder_rank": 5,
        "ladder_tier": "foundations",
        "description": (
            "Morning: the commute, and the driver ahead hesitates at a green light. "
            "A small curl at the corner of your mouth - some people should not be "
            "allowed behind the wheel. It passes by the next intersection. Midday: a "
            "coworker presents work full of errors, again. This time the feeling is "
            "thicker. You stop really listening halfway through; you are composing "
            "the email you will send instead. Your tone in the meeting stays polite, "
            "but there is a new edge - a slow, careful way of explaining things, as "
            "if to someone much younger. Afternoon: the news shows a public figure "
            "caught in something shabby, and the feeling arrives fully dressed: "
            "scorn, complete, with commentary. You say the words out loud - what did "
            "you expect - and enjoy the clean certainty of them. Evening: a family "
            "member repeats a story you have heard four times. The contempt is tired "
            "now, almost affectionate in its dismissal: that is just how they are. "
            "The day's thread is visible in hindsight: contempt started as flickers, "
            "grew with repetition, and ended by sorting the whole cast of the day "
            "into above and below. Nothing dramatic happened. That is the point - "
            "contempt does most of its work in ordinary hours."
        ),
        "how_it_works": (
            "The vignette shows contempt's daily mechanics: frequent low-grade "
            "appraisals, each one cheap and quick. The mind is constantly ranking - "
            "competence, manners, sense - and each ranking that comes back low "
            "deposits a drop of contempt. Most drops evaporate. But drops aimed at "
            "the same person accumulate, and accumulation is what turns flickers into "
            "files. The day also shows the feeling's favorite disguises: humor, "
            "patience, world-weariness. Each disguise lets the verdict pass without "
            "inspection - which is why the end-of-day review, the honest look back, "
            "is the practice that matters."
        ),
        "key_points": [
            "Contempt works mostly in ordinary hours: commutes, meetings, news, family.",
            "The mind ranks constantly; each low ranking deposits a drop of the feeling.",
            "Most drops evaporate - but drops aimed at one person accumulate into a file.",
            "The feeling's favorite disguises are humor, patience, and world-weariness.",
            "Each disguise lets the verdict pass without inspection.",
            "The end-of-day honest review is the practice that catches what the day deposited.",
        ],
        "requirements": [
            "No equipment needed - this is a reading and reflection record.",
            "A willingness to review one ordinary day honestly.",
            "No judgment of yourself required - observation only.",
        ],
        "standards": [
            "Public record in the Signature system - descriptive, educational.",
            "Vignette is an illustrative composite, not a report of any real person.",
            "Never diagnoses any real person with any emotional state.",
        ],
        "citations": [C_HG, C_IZARD, C_HAIDT],
        "sig_lens": (
            "The Signature Method keeps a day-ledger for this record: each small contempt a line "
            "item, each repeated target a running balance. The Method's end-of-day audit is simple "
            "- total the ledger and ask whether the day's rankings measured the world, or only "
            "measured the measurer's mood."
        ),
    },
]
ENTRIES += [
    {
        "key": "body-signals",
        "name": "What Happens in the Body: Heart, Breath, Muscles, and Energy",
        "group": "Body Signals",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Contempt is a low-arousal emotion, and the body shows it. The heart does "
            "not race the way it does in anger or fear; the pulse stays near resting, "
            "sometimes slowing slightly as the body settles into its verdict. "
            "Breathing grows slow and shallow, occasionally punctuated by a deliberate "
            "exhale through the nose - the sigh-snort that is contempt's audible "
            "signature. Muscle tension is selective rather than total: the jaw may set, "
            "one side of the mouth engages, the neck and shoulders stiffen into a "
            "held posture, but there is no whole-body bracing for action. The stomach "
            "stays mostly quiet - contempt is not the gut-churn of disgust. Skin "
            "shows little: no flush of anger, no pallor of fear, just a composed, "
            "controlled surface. Energy drops into a still, conserved state; the body "
            "is not preparing to fight or flee, it is preparing to withhold - "
            "attention, warmth, engagement. The overall impression is of a system "
            "powering down its connection to the other person while keeping full "
            "power for itself."
        ),
        "how_it_works": (
            "The body pattern follows the appraisal's demands. Contempt's job is "
            "exclusion and status marking, not combat or escape, so the autonomic "
            "nervous system stays near baseline - there is nothing to fight and "
            "nothing to run from. The selective tension in the face and neck serves "
            "the expression: the one-sided mouth movement and the held head position "
            "are the signal being broadcast. The slow exhale functions as both "
            "release and display. Because arousal stays low, the state is cheap to "
            "maintain - which is why contempt can be held for hours while anger "
            "burns out in minutes."
        ),
        "key_points": [
            "Contempt is low-arousal: heart rate stays near resting, sometimes slowing slightly.",
            "Breathing is slow and shallow, punctuated by the deliberate exhale - the sigh-snort.",
            "Muscle tension is selective: jaw, one side of the mouth, neck and shoulders hold; no whole-body bracing.",
            "The stomach stays quiet; the skin shows no flush or pallor - a composed surface.",
            "Energy drops into stillness: the body withholds attention, warmth, and engagement.",
            "Low arousal makes contempt cheap to maintain - it can be held for hours while anger burns out.",
        ],
        "requirements": [
            "No equipment needed - this is a reading and reflection record.",
            "Notice your own breath and shoulders the next time the feeling visits.",
            "Compare with how anger feels in the body - the contrast teaches.",
        ],
        "standards": [
            "Public record in the Signature system - descriptive, educational.",
            "Body signals described as typical patterns, not medical claims.",
            "Never diagnoses any real person with any emotional state.",
        ],
        "citations": [C_HG, C_FR, C_EKMAN],
        "sig_lens": (
            "The Signature Method reads the body of contempt as the scale-house at rest: no "
            "furnace roaring, no alarm bells - just the quiet tick of the mechanism and the "
            "deliberate exhale of the weigher. The Method notes the economy of it: a cool "
            "machine can run all day, which is why the honest weigher checks the calibration "
            "often."
        ),
    },
    {
        "key": "posture",
        "name": "Posture and Movement: How the Body Carries Contempt",
        "group": "Body Signals",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Contempt has a posture, and it is the posture of height. The head tilts "
            "back a fraction and turns slightly away, the chin lifts - the body "
            "literally looks down its nose. The torso leans back, away from the "
            "target, creating distance without stepping away. Shoulders go back and "
            "settle; the stance widens a touch, taking up space with ease rather "
            "than aggression. Movement slows and becomes deliberate: gestures get "
            "smaller and more precise, as if the body refuses to spend energy on "
            "someone unworthy of it. Hands may do the work of dismissal - a small "
            "wave-off, a turn of the wrist, fingers steepling under the chin in "
            "judgment. Walking changes too: the contemptuous walk is unhurried, "
            "measured, with the gaze fixed past the target rather than on them. "
            "Every element says the same thing: I am above this, and above you."
        ),
        "how_it_works": (
            "Posture is the body's broadcast of the hierarchy appraisal. Raising the "
            "head and chin physically enacts looking down; leaning back enacts "
            "withdrawal; slowed movement enacts the judgment that the target is not "
            "worth full energy. These are not conscious poses - they are the "
            "appraisal leaking into motor control. Because they are readable, they "
            "also function socially: observers pick up the status claim instantly, "
            "often before they register the feeling. That is why contempt posture in "
            "a meeting or a family gathering can shift the whole room's sense of who "
            "ranks where."
        ),
        "key_points": [
            "The head tilts back and turns slightly away; the chin lifts - literally looking down the nose.",
            "The torso leans back, creating distance without stepping away.",
            "Movement slows and becomes deliberate: small, precise gestures that refuse to spend energy.",
            "Hands dismiss: the wave-off, the wrist turn, the steepled fingers of judgment.",
            "The contemptuous walk is unhurried and measured, gaze fixed past the target.",
            "Posture is readable status broadcast: observers register the hierarchy claim instantly.",
        ],
        "requirements": [
            "No equipment needed - this is a reading and reflection record.",
            "Observe posture in films or plays where a character judges another.",
            "Notice your own chin and shoulders in moments of dismissal.",
        ],
        "standards": [
            "Public record in the Signature system - descriptive, educational.",
            "Posture described as typical expressive patterns, not certainties.",
            "Never diagnoses any real person with any emotional state.",
        ],
        "citations": [C_EKMAN, C_DARWIN, C_FR],
        "sig_lens": (
            "The Signature Method stages posture as the weigher climbing the step-stool: chin up, "
            "body back, movements rationed. The Method's stage direction is gentle but firm - "
            "every actor should know when they have climbed the stool, because the audience "
            "always does."
        ),
    },
    {
        "key": "sleep-appetite",
        "name": "Sleep, Appetite, and Energy Effects of Contempt",
        "group": "Body Signals",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Because contempt runs cool, its effects on sleep and appetite are "
            "quieter than those of hot emotions - but they are real. A contempt "
            "that is held, especially toward someone you live or work with, keeps "
            "the mind rehearsing verdicts at night: the replayed conversation, the "
            "imagined better retort, the mental re-ranking. Sleep comes, but it can "
            "be thin and argumentative, full of unfinished business. Appetite is "
            "rarely disturbed the way disgust or anxiety disturb it; contempt does "
            "not churn the stomach. What it does affect is the appetite for company: "
            "meals with the target become chores, shared tables feel long, the "
            "feeler starts eating alone or scheduling around the person. Energy "
            "follows a particular curve: contempt feels energizing in the moment - "
            "the clean high of certainty - but it is expensive over time. "
            "Maintaining a verdict, rehearsing it, performing politeness over it, "
            "drains the same reserves that attention and warmth would use. Long-held "
            "contempt leaves people tired in a specific way: not exhausted, just "
            "unwilling."
        ),
        "how_it_works": (
            "The sleep effect comes from cognitive rehearsal: verdicts are beliefs, "
            "and beliefs get replayed, especially in the quiet hours. The appetite "
            "effect is social, not digestive: the target becomes someone the body "
            "does not want to be near, and nearness includes meals. The energy curve "
            "reflects the cost of sustained low-grade appraisal - the mind running a "
            "background process of ranking and re-ranking. It is the tiredness of a "
            "machine left idling with the brakes on: no single moment is costly, but "
            "the hours add up."
        ),
        "key_points": [
            "Held contempt keeps the mind rehearsing verdicts at night - sleep can be thin and argumentative.",
            "Appetite for food is rarely disturbed; appetite for the target's company is.",
            "Meals with the target become chores; the feeler starts scheduling around them.",
            "Contempt feels energizing in the moment - the clean high of certainty.",
            "Over time it is expensive: maintaining the verdict drains attention and warmth reserves.",
            "Long-held contempt leaves a specific tiredness: not exhausted, just unwilling.",
        ],
        "requirements": [
            "No equipment needed - this is a reading and reflection record.",
            "Notice sleep quality during weeks of sustained friction with someone.",
            "General wellness information only, not medical advice.",
        ],
        "standards": [
            "Public record in the Signature system - descriptive, educational.",
            "Effects described as typical patterns; not medical or therapeutic advice.",
            "Never diagnoses any real person with any emotional state.",
        ],
        "citations": [C_HG, C_GOTTMAN, C_IZARD],
        "sig_lens": (
            "The Signature Method reads the tiredness as the scale-house running all night: the "
            "weigher gone home, the machine still ticking, re-weighing the same parcel by "
            "lamplight. The Method's housekeeping rule - close the shop at night, or the "
            "morning's measurements will all be wrong."
        ),
    },
    {
        "key": "bodies-differ",
        "name": "How Body Signals Differ Between People",
        "group": "Body Signals",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "No two bodies do contempt exactly the same way. Some people broadcast "
            "it on the face - the one-sided smile is unmistakable, a billboard. "
            "Others show almost nothing facially, but their body goes still and "
            "their voice drops half a tone into condescension; you hear their "
            "contempt before you see it. Some get the sigh-snort, the audible "
            "exhale that says everything; others go silent, and the silence is the "
            "signal. Culture shapes the display: in settings where direct "
            "disrespect is costly, contempt goes underground into exquisite "
            "politeness - the overly careful explanation, the smile that does not "
            "reach the eyes. Age and habit matter too: people who have practiced "
            "contempt for years can deliver it with a perfectly pleasant face, the "
            "verdict carried entirely in timing and word choice. The lesson is "
            "humility about reading bodies: the classic signals are real and "
            "well-studied, but any single person's contempt has its own dialect. "
            "Learn the language, then learn the speaker."
        ),
        "how_it_works": (
            "Display differences come from three sources. Biology sets the "
            "baseline: facial expressiveness varies widely between individuals. "
            "Learning sets the habits: families and workplaces teach which displays "
            "are safe and which are punished, and bodies adapt. Intention sets the "
            "mask: contempt is one of the easiest emotions to perform politely, "
            "because its coolness looks like composure. The result is a layered "
            "system - a universal core signal with deep individual and cultural "
            "variation on top. Reading contempt well means holding both: know the "
            "textbook, and watch the person."
        ),
        "key_points": [
            "Some broadcast contempt on the face; others carry it in voice, stillness, or silence.",
            "The sigh-snort is audible in some; in others, silence itself is the signal.",
            "Where disrespect is costly, contempt goes underground into exquisite politeness.",
            "Practiced contempt can wear a perfectly pleasant face, carried by timing and word choice.",
            "Biology, learned habits, and deliberate masking all shape the display.",
            "Know the textbook signals, then watch the individual - every contempt has its own dialect.",
        ],
        "requirements": [
            "No equipment needed - this is a reading and reflection record.",
            "Observe variation across people you know well - privately, without labeling.",
            "Resist one-size-fits-all reading of body signals.",
        ],
        "standards": [
            "Public record in the Signature system - descriptive, educational.",
            "Variation described to prevent overconfident mind-reading.",
            "Never diagnoses any real person with any emotional state.",
        ],
        "citations": [C_EKMAN, C_HG, C_IZARD],
        "sig_lens": (
            "The Signature Method keeps a dialect atlas for this record: the same weight measured "
            "in different scale-houses, each with its own local customs of weighing. The Method's "
            "caution to apprentices - never certify a reading in a dialect you have not studied."
        ),
    },
    {
        "key": "face",
        "name": "The Face of Contempt: Eyes, Brows, Mouth, and the Tell-Tale Micro-Signs",
        "group": "Facial Expression",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Contempt has the most one-sided face in the emotional repertoire, and that "
            "asymmetry is its signature. The mouth: one corner tightens and pulls up "
            "and back - the unilateral lip curl - while the other side stays neutral. "
            "It can be subtle, a mere tightening, or pronounced, a clear smirk. The "
            "eyes: the gaze steadies and narrows slightly, often with the head tilted "
            "back so the look travels down the nose; the eyelids may lower a fraction, "
            "the look of someone viewing something small at a distance. The brows: "
            "usually neutral or slightly raised on one side - contempt rarely knits "
            "the brow the way anger does; the forehead stays smooth, which is part of "
            "the coolness. The micro-signs: a quick unilateral tightening that flashes "
            "and vanishes in under a second; a slight head shake, small and slow, as "
            "if negating the target's worth; the nostril flare on one side that "
            "sometimes accompanies the mouth movement. Researchers found this "
            "expression recognized across cultures - the one-sidedness is what makes "
            "it unmistakable once you know to look for it."
        ),
        "how_it_works": (
            "The face of contempt is produced by unilateral action of the mouth "
            "muscles - principally the buccinator and zygomatic muscles on one side - "
            "which is unusual: most emotional expressions are bilateral. That "
            "one-sidedness is the tell. The narrowed eyes and lifted chin arrange the "
            "gaze geometry of looking down. Because the expression is low-energy, it "
            "can be held or flashed with little effort, and because it is "
            "asymmetric, it is hard to produce convincingly by accident - which is "
            "why observers read it as deliberate judgment rather than reflex."
        ),
        "key_points": [
            "The signature is asymmetry: one mouth corner tightens and pulls up while the other stays neutral.",
            "The eyes narrow slightly; the head tilts back so the gaze travels down the nose.",
            "Brows stay mostly neutral - the smooth forehead is part of the coolness.",
            "Micro-signs: the sub-second unilateral flash, the small slow head shake, the one-sided nostril flare.",
            "The expression is recognized across cultures - the one-sidedness makes it unmistakable.",
            "Its asymmetry reads as deliberate judgment, not reflex - observers take it as a verdict.",
        ],
        "requirements": [
            "No equipment needed - this is a reading and reflection record.",
            "A mirror helps: try the one-sided tightening to feel the muscles involved.",
            "Study the asymmetry in filmed performances of judgmental characters.",
        ],
        "standards": [
            "Public record in the Signature system - descriptive, educational.",
            "Facial description follows published expression research.",
            "Never diagnoses any real person with any emotional state.",
        ],
        "citations": [C_EKMAN, C_DARWIN, C_HG],
        "sig_lens": (
            "The Signature Method frames the one-sided face as the scale's own emblem: the beam "
            "tipped, one pan raised, the other resting. The Method teaches apprentices to spot "
            "the emblem the way a coin collector spots a mint mark - small, off-center, and "
            "decisive."
        ),
    },
    {
        "key": "face-intensity",
        "name": "How the Expression Changes With Intensity",
        "group": "Facial Expression",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "At low intensity, the face of contempt is barely there: a fractional "
            "tightening at one mouth corner, gone in half a second, easily mistaken "
            "for a suppressed smile. The eyes do most of the work - a slight "
            "narrowing, a gaze that goes just past the person. At moderate "
            "intensity, the asymmetry becomes unmistakable: the unilateral curl is "
            "held, the chin lifts, the head turns a few degrees away. The whole "
            "face composes itself into the look of assessment - smooth forehead, "
            "steady gaze, one-sided mouth. This is the face people picture when "
            "they picture contempt. At high intensity, the expression spreads: the "
            "curl deepens into a sneer, the nostril flares, the head shake becomes "
            "visible, the eyes may roll - the full dismissal performed for an "
            "audience. And there is a fourth register worth knowing: the masked "
            "high-intensity face, where strong contempt is ironed flat into "
            "politeness. The mouth is neutral, the eyes are pleasant - but the "
            "timing is off by a beat, the smile arrives late, the gaze slides away "
            "too quickly. Intensity does not always mean visibility; sometimes it "
            "means control."
        ),
        "how_it_works": (
            "Expression intensity tracks two dials: felt intensity and display "
            "permission. Felt intensity drives the muscle engagement - more verdict "
            "certainty, deeper curl. Display permission, set by the social setting, "
            "drives the masking - a boardroom permits less than a living room. The "
            "fourth register, masked high-intensity, happens when the dials "
            "diverge: strong feeling, strict setting. The leakage then moves to "
            "channels the masker forgets - timing, gaze duration, the beat before "
            "the smile. Reading intensity accurately means reading both dials, not "
            "just the mouth."
        ),
        "key_points": [
            "Low intensity: a fractional one-sided tightening, easily mistaken for a suppressed smile.",
            "Moderate intensity: the held unilateral curl, lifted chin, composed assessment face.",
            "High intensity: the curl deepens to a sneer, nostril flares, eye roll - dismissal performed.",
            "Masked high intensity: strong contempt ironed into politeness; leakage moves to timing and gaze.",
            "Expression tracks two dials: felt intensity and the setting's display permission.",
            "Intensity does not always mean visibility - sometimes it means control.",
        ],
        "requirements": [
            "No equipment needed - this is a reading and reflection record.",
            "Watch for the masked register in formal settings - timing tells.",
            "A mirror helps calibrate the low-intensity version.",
        ],
        "standards": [
            "Public record in the Signature system - descriptive, educational.",
            "Registers described as typical patterns, not certainties.",
            "Never diagnoses any real person with any emotional state.",
        ],
        "citations": [C_EKMAN, C_HG, C_FR],
        "sig_lens": (
            "The Signature Method reads the four registers as the scale's four voices: the "
            "whisper (low), the pronouncement (moderate), the proclamation (high), and the "
            "sealed letter (masked). The Method trains the ear for the sealed letter most of "
            "all - the loudest verdicts are often the quietest."
        ),
    },
    {
        "key": "hide-fake",
        "name": "Hiding and Faking Contempt: What Leaks Through",
        "group": "Facial Expression",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Contempt is one of the easiest emotions to hide and one of the hardest "
            "to fake convincingly - and the reasons are the same. Hiding works "
            "because contempt is cool: unlike anger's heat or fear's tremor, there "
            "is little arousal to suppress. A practiced person can hold a neutral "
            "or even warm face while the verdict runs underneath. What leaks: the "
            "timing of the smile (a beat late), the gaze that slides off the target "
            "a fraction too soon, the over-careful politeness, the small exhale "
            "before answering. Faking is harder because the signature is "
            "asymmetric: most people, asked to look contemptuous, produce a "
            "symmetric sneer - both mouth corners up - which reads as disgust or "
            "mockery, not contempt. Genuine contempt's one-sidedness is difficult "
            "to perform on command without looking theatrical. Actors learn it as a "
            "technique: relax the face completely, then engage only one corner, and "
            "let the eyes do the distance. The practical upshot: when you see "
            "effortless one-sided contempt, it is usually real; when you see a "
            "broad symmetric sneer labeled as contempt, someone is performing."
        ),
        "how_it_works": (
            "Hiding succeeds through low arousal plus deliberate masking - the face "
            "is set to neutral while attention does the withdrawing. Leakage moves "
            "to unmanaged channels: timing, gaze, breath, word choice. Faking fails "
            "through the asymmetry problem: bilateral expressions are the default, "
            "and unilateral control of the mouth corner is a fine motor skill most "
            "people have never trained. This asymmetry between hiding (easy) and "
            "faking (hard) is unusual among emotions, and it makes contempt a "
            "particularly honest signal when it does show: the face rarely produces "
            "it by accident."
        ),
        "key_points": [
            "Contempt is easy to hide: low arousal means little to suppress; a neutral face covers it.",
            "Leakage moves to unmanaged channels: smile timing, gaze duration, the exhale before answering.",
            "Contempt is hard to fake: the one-sided signature resists deliberate performance.",
            "Amateurs produce symmetric sneers, which read as disgust or mockery, not contempt.",
            "Actors learn it as technique: relax the face, engage one corner, let the eyes create distance.",
            "Effortless one-sided contempt is usually real; the face rarely produces it by accident.",
        ],
        "requirements": [
            "No equipment needed - this is a reading and reflection record.",
            "Compare genuine and performed contempt in filmed performances.",
            "Notice leakage channels rather than staring at the mouth.",
        ],
        "standards": [
            "Public record in the Signature system - descriptive, educational.",
            "Hiding and faking described as typical patterns, not detection certainties.",
            "Never diagnoses any real person with any emotional state.",
        ],
        "citations": [C_EKMAN, C_HG, C_DARWIN],
        "sig_lens": (
            "The Signature Method calls this the honest-counterfeit rule of the scale: the true "
            "weight is easy to pocket and hard to forge. The Method's authentication test is "
            "the asymmetry - the mint mark that counterfeiters always get wrong."
        ),
    },
    {
        "key": "drawing-guide",
        "name": "Drawing Contempt: Notes for Artists and Actors",
        "group": "Facial Expression",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "To draw or play contempt, start with asymmetry - everything else is "
            "secondary. The mouth: raise and tighten one corner only, pulling it up "
            "and slightly back, as if a string tugged that side; keep the other "
            "corner soft and neutral. Add a faint nasolabial line deepening on the "
            "active side. The eyes: narrow the lids a fraction and direct the gaze "
            "slightly downward past the viewer, not at them - contempt looks through "
            "more than at. Tilt the head back five degrees and turn it a few degrees "
            "away; lift the chin. Keep the brow smooth - no furrow, no raise; the "
            "calm forehead is what separates contempt from anger on the page and on "
            "stage. For the body: lean the torso back, settle the weight, slow every "
            "gesture to half speed. The hands can steeple, or one hand can make the "
            "small dismissive turn of the wrist. For actors, the inner action is "
            "assessment, not attack: play the thought I have already decided about "
            "you, and let the face follow. The most common mistake is heat - "
            "playing contempt with anger's energy. Contempt is refrigerated; keep it "
            "cold and the audience will feel the chill."
        ),
        "how_it_works": (
            "The guide works because it builds the expression from its researched "
            "components rather than from stereotype. Asymmetry first, because it is "
            "the diagnostic feature; gaze geometry second, because looking down is "
            "the appraisal made visible; smooth brow third, because the absence of "
            "anger's furrow is what keeps the read cold. The inner action for "
            "actors - I have already decided about you - generates the low-arousal "
            "certainty that makes the face believable: the body follows the "
            "appraisal, exactly as it does in life."
        ),
        "key_points": [
            "Start with asymmetry: one mouth corner raised and tightened, the other soft.",
            "Narrow the lids slightly; aim the gaze downward past the viewer, not at them.",
            "Tilt the head back, turn slightly away, lift the chin - the geometry of looking down.",
            "Keep the brow smooth: no furrow, no raise - the calm forehead separates contempt from anger.",
            "Slow the body to half speed; lean back; let hands steeple or dismiss.",
            "The actor's inner action is assessment, not attack: I have already decided about you.",
        ],
        "requirements": [
            "Paper and pencil, or a mirror and a scene to play.",
            "Study the asymmetry in a mirror before committing it to the page.",
            "Keep it cold - the most common mistake is playing contempt with anger's heat.",
        ],
        "standards": [
            "Public record in the Signature system - descriptive, educational.",
            "Guide built from published expression research components.",
            "Never diagnoses any real person with any emotional state.",
        ],
        "citations": [C_EKMAN, C_DARWIN, C_IZARD],
        "sig_lens": (
            "The Signature Method issues this guide as the scale-house portrait manual: how to "
            "paint the weigher at the moment of measurement. The Method's portrait rule - paint "
            "the asymmetry first, for without the tipped beam the painting is of some other "
            "emotion entirely."
        ),
    },
]
ENTRIES += [
    {
        "key": "classic-triggers",
        "name": "The Classic Triggers: Situations, Words, and Events",
        "group": "Triggers",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Contempt has a recognizable trigger menu - the situations that most "
            "reliably summon it. Incompetence on display: the person who confidently "
            "does the job badly, the expert who turns out to know nothing, the "
            "leader who cannot lead. Shamelessness: the person caught out who shows "
            "no embarrassment, the apology that is obviously performed, the "
            "wrongdoer who smirks. Status violations: someone acting above their "
            "station with no self-awareness, or someone in high station behaving "
            "beneath it - both directions trigger the hierarchy appraisal. "
            "Moral failure: cruelty, cheating, betrayal of trust, especially when "
            "the perpetrator seems pleased with themselves. Weakness performed as "
            "strength: boasting that reveals insecurity, authority asserted without "
            "competence behind it. Certain words act as triggers too: the "
            "condescending actually, the dismissive whatever, the told-you-so "
            "delivered with a smile. And events: public humiliations, failed "
            "auditions, leaders exposed, experts debunked - any spectacle of "
            "someone falling from a claimed height. The common thread is the "
            "gap: between the person's pretensions and their reality, contempt "
            "rushes into the space between."
        ),
        "how_it_works": (
            "Each classic trigger presents the same structure to the appraisal "
            "system: a claim to worth (by status, by boasting, by role) followed by "
            "evidence of unworth. The mind compares the claim against the evidence, "
            "finds the person wanting, and the verdict fires. Triggers are "
            "culturally tuned - what counts as shameless or above one's station "
            "varies - but the structure is stable: pretension exposed. That is why "
            "public falls trigger collective contempt so reliably: the exposure is "
            "visible, the gap is undeniable, and the audience gets to do the "
            "ranking together."
        ),
        "key_points": [
            "Incompetence on display: confident, visible failure at a claimed skill.",
            "Shamelessness: being caught and showing no embarrassment, the performed apology.",
            "Status violations in both directions: acting above one's station, or beneath a high one.",
            "Moral failure with self-satisfaction: cruelty or cheating worn proudly.",
            "Trigger words: the condescending actually, the dismissive whatever, the smiling told-you-so.",
            "The common thread is the gap: pretension exposed, and contempt rushes into the space between.",
        ],
        "requirements": [
            "No equipment needed - this is a reading and reflection record.",
            "Notice which triggers on the menu move you most - that reveals your standards.",
            "Observe triggers in stories and news, not in live judgment of real people.",
        ],
        "standards": [
            "Public record in the Signature system - descriptive, educational.",
            "Triggers listed as commonly reported patterns, not universal laws.",
            "Never diagnoses any real person with any emotional state.",
        ],
        "citations": [C_CAD, C_HG, C_HAIDT],
        "sig_lens": (
            "The Signature Method catalogs the triggers as the standard parcels arriving at the "
            "scale-house: each one labeled with a claimed weight, each one re-weighed on arrival. "
            "The Method's receiving rule - always re-weigh; the label is the sender's hope, not "
            "the parcel's truth."
        ),
    },
    {
        "key": "personal-triggers",
        "name": "Personal Triggers: Memories, Anniversaries, and Private Associations",
        "group": "Triggers",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Beyond the classic menu, everyone carries a private trigger set - "
            "contempts that belong to their history alone. A certain laugh that "
            "sounds exactly like the laugh of someone who humiliated you years "
            "ago. An anniversary: the date a trusted person revealed themselves, "
            "which arrives each year with the verdict pre-loaded. A phrase - a "
            "pet name, a slogan, a way of saying obviously - that is "
            "permanently stained by the person who used it while looking down on "
            "you. Professional scars: the manager who dismissed your work in "
            "front of everyone, so that now every manager's sigh carries the old "
            "weight. Family patterns: the sibling dynamic where one was always the "
            "competent one, so competence itself became a contempt trigger. "
            "These personal triggers are powerful because they bypass the "
            "appraisal: the verdict was filed years ago, and the trigger just "
            "reopens the file. The feeling arrives with the force of the original "
            "wound wearing the clothes of the present moment - which is why it "
            "can feel so disproportionate, and why arguing with it in the moment "
            "rarely works. The work is archival: find the original filing, and "
            "the present trigger loses its borrowed force."
        ),
        "how_it_works": (
            "Personal triggers work through associative memory. The original "
            "contempt verdict gets stored with sensory tags - a sound, a date, a "
            "phrase, a setting. When a tag recurs, the stored verdict reactivates "
            "before the current situation is appraised: the feeling is a memory "
            "wearing a costume. This is efficient - the mind reuses old judgments - "
            "but it misfires whenever the present person is not the past person. "
            "Disentangling requires the slow work of noticing the disproportion, "
            "tracing the tag to its origin, and re-filing the verdict under its "
            "true date."
        ),
        "key_points": [
            "Everyone carries a private trigger set: laughs, dates, phrases stained by past verdicts.",
            "Anniversaries can arrive with the contempt pre-loaded from the original event.",
            "Professional and family scars generalize: one manager's sigh carries the old weight.",
            "Personal triggers bypass fresh appraisal: the old file simply reopens.",
            "The feeling is a memory in costume - disproportionate because it borrows the past's force.",
            "The work is archival: find the original filing, and the present trigger loses its borrowed force.",
        ],
        "requirements": [
            "No equipment needed - this is a reading and reflection record.",
            "Private reflection only; no need to share or confront anyone.",
            "Curiosity about your own patterns, not self-accusation.",
        ],
        "standards": [
            "Public record in the Signature system - descriptive, educational.",
            "Personal triggers discussed as common patterns; general guidance only.",
            "Never diagnoses any real person with any emotional state.",
        ],
        "citations": [C_HG, C_IZARD, C_FR],
        "sig_lens": (
            "The Signature Method files personal triggers in the archive's cold storage: old "
            "verdicts in sealed envelopes, each tagged with its true date. The Method's archival "
            "rule - a verdict filed in 2019 has no jurisdiction over a person met in 2026. "
            "Re-file it, and the present moment gets its own clean scale."
        ),
    },
    {
        "key": "surprise-triggers",
        "name": "Surprise Triggers: The Odd, Unexpected Things That Set It Off",
        "group": "Triggers",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "Contempt does not only arrive through grand moral failures; it has a "
            "side door of small, strange triggers. Bad taste held confidently: "
            "someone passionately defending an opinion that reveals they have never "
            "thought about it. Misused vocabulary: the confident misuse of a big "
            "word in a meeting, which tells the listener everything about the "
            "speaker's reading habits. Helplessness performed as charm: the adult "
            "who weaponizes incompetence - I am just not a tech person - while "
            "others do the work. Sentimentality about the wrong things: gushing "
            "over trivia while remaining cold to real suffering. Fandom "
            "snobbery in reverse: the person who likes only obscure things, "
            "performing taste as superiority. The un-self-aware selfie: not vanity "
            "itself, but the caption that reveals the person thinks this is "
            "profound. These triggers surprise people because they seem petty - and "
            "the pettiness is the point. Contempt is a ranking emotion, and ranking "
            "never really stops; the small triggers are the ranking system "
            "idling. Noticing them is useful data about your own ladder: the "
            "things that trigger your surprise-contempt are a map of what you "
            "secretly pride yourself on."
        ),
        "how_it_works": (
            "Surprise triggers work because the appraisal system runs continuously "
            "in the background, ranking everything - taste, competence, "
            "self-awareness - not just moral conduct. Most of these rankings stay "
            "below consciousness; a trigger is simply one that crosses the "
            "threshold into feeling. The pettiness people feel about these "
            "triggers is itself informative: it shows the ranking system was "
            "operating unexamined. Bringing a surprise trigger into awareness - "
            "naming what standard was applied and whether you endorse it - is how "
            "the background ranker gets supervised."
        ),
        "key_points": [
            "Contempt has a side door: confidently held bad taste, misused vocabulary, weaponized helplessness.",
            "Sentimentality about trivia, performed obscure taste, and un-self-aware profundity all trigger it.",
            "The triggers seem petty - and the pettiness is the point: ranking never stops.",
            "Small triggers are the ranking system idling in the background.",
            "Your surprise-contempts are a map of what you secretly pride yourself on.",
            "Naming the hidden standard is how the background ranker gets supervised.",
        ],
        "requirements": [
            "No equipment needed - this is a reading and reflection record.",
            "Keep a private note of your own surprise triggers for a week.",
            "Read them as data about your ladder, not as verdicts on others.",
        ],
        "standards": [
            "Public record in the Signature system - descriptive, educational.",
            "Surprise triggers presented as common observations, not judgments.",
            "Never diagnoses any real person with any emotional state.",
        ],
        "citations": [C_HG, C_HAIDT, C_IZARD],
        "sig_lens": (
            "The Signature Method keeps a curiosity cabinet for surprise triggers: small odd "
            "weights, each labeled with the secret pride that made it heavy. The Method's "
            "cabinet rule - every strange weight in the drawer is a mirror with dust on it. "
            "Wipe the dust, see whose pride is reflected."
        ),
    },
    {
        "key": "chain-reactions",
        "name": "Chain Reactions: How One Trigger Sets Off a Cascade",
        "group": "Triggers",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "One contempt rarely travels alone. The cascade works like this: a "
            "trigger fires contempt at a person - say, a colleague's sloppy "
            "work. The verdict, once active, lowers the threshold for the next "
            "appraisal: now everything the colleague does gets ranked, and "
            "ranked harshly. Their laugh is suddenly irritating (contempt "
            "spreading to mannerisms). Their ally in the office becomes suspect "
            "by association (contempt spreading to associates). The critic's own "
            "standards inflate - now everyone seems a little beneath the bar "
            "(contempt spreading to the world). And if the target pushes back, "
            "anger joins the mix, which licenses the contempt to speak aloud, "
            "which draws in onlookers who pick a side. Within an hour, a single "
            "sloppy report has become a whole climate. Researchers call this "
            "kind of spread affective generalization: the appraisal style, once "
            "switched on, keeps applying itself. The practical insight is the "
            "circuit breaker: cascades need the second and third appraisals to "
            "keep going. Refuse the second ranking - notice it and set it down - "
            "and the chain starves."
        ),
        "how_it_works": (
            "Cascades run on threshold-lowering. Each contempt appraisal primes "
            "the ranking system, making the next low ranking easier and faster - a "
            "kind of emotional momentum. Association spreads the verdict outward "
            "from the person to their mannerisms, allies, and eventually the "
            "general environment. Anger's arrival adds fuel because it converts "
            "private verdict into public action, recruiting social confirmation. "
            "The chain is self-reinforcing until something interrupts the "
            "appraisal loop: new evidence, a deliberate reframe, exhaustion, or "
            "simply noticing the cascade while it is happening."
        ),
        "key_points": [
            "One contempt lowers the threshold for the next: the ranking system gains momentum.",
            "The verdict spreads: from the person to their mannerisms, their allies, the whole climate.",
            "Anger often joins mid-cascade, converting private verdict into public action.",
            "Onlookers get recruited; a single trigger can become a group climate within an hour.",
            "The mechanism is affective generalization: the appraisal style keeps applying itself.",
            "The circuit breaker is refusing the second ranking - notice it and set it down.",
        ],
        "requirements": [
            "No equipment needed - this is a reading and reflection record.",
            "Replay a past cascade and spot where the second appraisal happened.",
            "Practice naming the cascade while it is happening.",
        ],
        "standards": [
            "Public record in the Signature system - descriptive, educational.",
            "Cascades described as common patterns; general guidance only.",
            "Never diagnoses any real person with any emotional state.",
        ],
        "citations": [C_FR, C_HG, C_GOTTMAN],
        "sig_lens": (
            "The Signature Method diagrams the cascade as a row of domino-scales: one tipped "
            "beam knocking the next. The Method's engineering note is plain - the dominoes only "
            "fall if they are standing close together. Widen the gap at the second appraisal, "
            "and the chain cannot complete."
        ),
    },
    {
        "key": "behavior-actions",
        "name": "What People Do When They Feel Contempt",
        "group": "Behavior",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "Contempt's actions are actions of withdrawal and demotion. The "
            "contemptuous person stops consulting the target: decisions get made "
            "around them, information stops flowing their way, their input is "
            "solicited as formality and then ignored. In conversation, there is "
            "the slow nod that means I have stopped listening, the glance at a "
            "phone or watch mid-sentence, the turning of the body a few degrees "
            "away. Socially, contempt demotes: the target gets seated at the edge "
            "of things - invited but not included, cc'd but not consulted. "
            "Mockery is contempt's public performance: the imitation of the "
            "target's mannerisms for an audience, the joke that is really a "
            "verdict, the nickname that sticks because it encodes the judgment. "
            "At its most severe, contempt acts through erasure: the person is "
            "simply not acknowledged - walked past, talked over, treated as "
            "furniture. Every one of these actions does the same work: it "
            "enacts the hierarchy the feeling perceives, moving the target down "
            "a rung in the shared social space."
        ),
        "how_it_works": (
            "The behaviors are the appraisal made physical. Withdrawal enacts "
            "the judgment that the target is not worth engagement; demotion enacts "
            "the ranking; mockery enacts the verdict for an audience, recruiting "
            "social confirmation of the hierarchy; erasure is the logical "
            "endpoint - someone fully beneath consideration needs no acknowledgment "
            "at all. Because these actions are mostly cool and controlled, they "
            "can be hard to confront: each one is deniable in isolation - I was "
            "just busy, it was just a joke. The pattern, not the incident, is "
            "what reveals the feeling."
        ),
        "key_points": [
            "Contempt withdraws: decisions made around the target, information stops flowing.",
            "Conversation shows it: the slow nod, the mid-sentence glance away, the turned body.",
            "Socially it demotes: invited but not included, cc'd but not consulted.",
            "Mockery is the public performance: imitation, verdict-jokes, the nickname that encodes judgment.",
            "At its extreme it erases: the target walked past, talked over, treated as furniture.",
            "Each act is deniable alone - I was just busy, it was just a joke - the pattern reveals the feeling.",
        ],
        "requirements": [
            "No equipment needed - this is a reading and reflection record.",
            "Look for patterns across incidents, not single acts.",
            "Observe in stories and group dynamics, not as accusations.",
        ],
        "standards": [
            "Public record in the Signature system - descriptive, educational.",
            "Behaviors described as typical patterns, not certainties about any person.",
            "Never diagnoses any real person with any emotional state.",
        ],
        "citations": [C_GOTTMAN, C_FR, C_MELWANI],
        "sig_lens": (
            "The Signature Method logs these actions as the scale's paperwork: the un-sent memo "
            "(withdrawal), the refiled folder (demotion), the margin note read aloud (mockery), "
            "the shredded file (erasure). The Method's audit question - which of these papers "
            "have you signed this month, and were the measurements behind them honest?"
        ),
    },
    {
        "key": "behavior-speech",
        "name": "What People Say: Phrases, Tone, and Speech Patterns of Contempt",
        "group": "Behavior",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "Contempt has a voice, and it is the voice of the patient teacher "
            "addressing a slow student. The tone: slightly slowed, over-enunciated, "
            "pitched a touch lower, with the particular music of someone explaining "
            "the obvious. Characteristic phrases: well, actually... delivered as a "
            "correction wrapped in patience; bless your heart and its regional "
            "cousins - kindness as a weapon; I am sure you tried - praise that "
            "demotes; that is... an interesting choice - the pause doing the "
            "verdict's work; we have already covered this - the royal we of "
            "exclusion. Questions become verdicts: do you even understand what we "
            "are discussing? Speech patterns: the rhetorical question that needs "
            "no answer, the summary that subtly rewrites what the target said into "
            "something smaller, the third-person reference while the person is "
            "present - as he was saying. Laughter is a channel too: the short "
            "exhale-laugh that greets the target's earnest statement, doing in one "
            "sound what a paragraph could not. The genius of contemptuous speech "
            "is its deniability: every phrase has an innocent reading, which is "
            "exactly why the pattern across phrases is what convicts."
        ),
        "how_it_works": (
            "Contemptuous speech works through implicature - meaning carried "
            "between the lines. The literal words stay polite; the verdict rides "
            "in tone, timing, and framing. The slowed teacher-voice implies the "
            "listener is slow; the over-patient correction implies the error was "
            "beneath an adult; the third-person reference implies the target is "
            "not a full participant. Because the verdict is never stated, it "
            "cannot be directly answered - which is the point. The target feels "
            "diminished but cannot point to the sentence that did it. That "
            "unanswerability is what makes contemptuous speech so effective and "
            "so corrosive."
        ),
        "key_points": [
            "The tone is the patient teacher addressing a slow student: slowed, over-enunciated, pitched low.",
            "well, actually... - the correction wrapped in patience; bless your heart - kindness as a weapon.",
            "I am sure you tried - praise that demotes; the pause in that is... an interesting choice.",
            "Questions become verdicts: do you even understand what we are discussing?",
            "The third-person reference while present - as he was saying - demotes by grammar.",
            "Every phrase has an innocent reading; the pattern across phrases is what convicts.",
        ],
        "requirements": [
            "No equipment needed - this is a reading and reflection record.",
            "Listen for the music underneath the words, not just the words.",
            "Study the patterns in dialogue writing and filmed arguments.",
        ],
        "standards": [
            "Public record in the Signature system - descriptive, educational.",
            "Speech patterns described as typical forms, not diagnostics.",
            "Never diagnoses any real person with any emotional state.",
        ],
        "citations": [C_GOTTMAN, C_FR, C_HG],
        "sig_lens": (
            "The Signature Method transcribes contemptuous speech as margin notes in the "
            "scale-house ledger: written in the politest hand, carrying the coldest figures. "
            "The Method's reading lesson - the verdict is never in the sentence; it is in the "
            "space between the sentences, where the tone lives."
        ),
    },
    {
        "key": "behavior-decisions",
        "name": "How Contempt Changes Decisions and Judgment",
        "group": "Behavior",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "Contempt is a decision-distorting lens: once the verdict is filed, it "
            "starts making choices on its own. Hiring and promotion: the "
            "contemptuous evaluator cannot see the target's strengths - good work "
            "gets attributed to luck or help, mistakes get attributed to "
            "character. This is the classic asymmetry: successes discounted, "
            "failures diagnostic. Resource decisions: the target gets the smaller "
            "budget, the worse slot, the last pick - not from policy but from the "
            "quiet certainty that they are not worth the investment. Relationship "
            "decisions: contempt makes exit feel rational and repair feel "
            "pointless - why fix something with someone beneath fixing? Risk "
            "judgment skews too: the contemptuous person underestimates the "
            "target systematically, which is how the underestimated keep winning. "
            "Group decisions are the most dangerous ground: one contemptuous voice "
            "with authority can steer a whole committee to write someone off, "
            "because the verdict arrives packaged as confident judgment, and "
            "confidence is contagious. The corrective is procedural: when you "
            "notice the verdict in yourself, force the decision through criteria "
            "written before the feeling arrived."
        ),
        "how_it_works": (
            "The distortion runs through motivated evaluation. Contempt sets the "
            "conclusion first - this person is lesser - and then the mind "
            "evaluates evidence to fit it: confirmatory successes get explained "
            "away, confirmatory failures get weighted heavily. This is not "
            "deliberate dishonesty; it is the appraisal system protecting its "
            "verdict. The effect compounds in groups through authority bias: a "
            "confident contemptuous judgment from a high-status voice resets the "
            "room's priors. Written criteria work as a corrective because they "
            "were set by a cooler mind - they force the evidence to be weighed "
            "before the verdict is consulted."
        ),
        "key_points": [
            "Contempt sets the conclusion first, then evaluates evidence to fit it.",
            "Successes get attributed to luck, failures to character - the classic asymmetry.",
            "Resource decisions quietly starve the target: smaller budgets, worse slots, last picks.",
            "In relationships, contempt makes exit feel rational and repair feel pointless.",
            "The contemptuous systematically underestimate the target - which is how the underestimated keep winning.",
            "The corrective is procedural: decide through criteria written before the feeling arrived.",
        ],
        "requirements": [
            "No equipment needed - this is a reading and reflection record.",
            "Review one past decision for the conclusion-first pattern.",
            "Write decision criteria before evaluating people, not after.",
        ],
        "standards": [
            "Public record in the Signature system - descriptive, educational.",
            "Decision effects described as documented biases; general guidance only.",
            "Never diagnoses any real person with any emotional state.",
        ],
        "citations": [C_MELWANI, C_FR, C_HG],
        "sig_lens": (
            "The Signature Method calls this the rigged weigh-in: the verdict written on the tag "
            "before the parcel is placed on the scale. The Method's procedural fix is the oldest "
            "in the scale-house - write the standard on the wall before the weighing begins, and "
            "weigh against the wall, not the tag."
        ),
    },
    {
        "key": "behavior-escalation",
        "name": "Contempt Under Intensity: How Actions Escalate",
        "group": "Behavior",
        "ladder_rank": 9,
        "ladder_tier": "compounded",
        "description": (
            "As contempt intensifies, the behaviors climb a ladder of their own. "
            "Rung one is private: the verdict stays internal - the eye-roll nobody "
            "sees, the muttered aside. Rung two is social: the verdict gets an "
            "audience - the joke at the target's expense, the knowing look exchanged "
            "with an ally, the story told about the target that encodes the "
            "judgment. Rung three is structural: the verdict gets built into "
            "arrangements - the target excluded from the meeting, the role quietly "
            "reassigned, the social circle redrawn without them. Rung four is "
            "open: the verdict is stated - the public dressing-down, the scornful "
            "review, the character assassination delivered as honesty. Each rung "
            "feels like a natural next step from the last, which is why escalation "
            "is so hard to notice from inside: at every stage, the action feels "
            "proportionate to the verdict, because the verdict itself has been "
            "growing. The de-escalation insight runs the ladder in reverse: "
            "interrupt the structural rung by re-including, interrupt the social "
            "rung by refusing the audience, interrupt the private rung by "
            "appealing the verdict. You cannot argue someone out of rung four; "
            "you starve rung one."
        ),
        "how_it_works": (
            "Escalation is driven by the verdict's growth plus social "
            "recruitment. Each enacted rung makes the verdict feel more real - "
            "acting on a judgment strengthens it - and each audience recruited "
            "validates it. The ladder is sticky downward: people rarely climb "
            "back down voluntarily because descending would mean admitting the "
            "earlier rungs were wrong. That is why intervention works best at "
            "the lowest active rung, and why the most effective de-escalation is "
            "early: appeal the private verdict before it hires an audience."
        ),
        "key_points": [
            "Rung one is private: the unseen eye-roll, the muttered aside.",
            "Rung two is social: the verdict gets an audience - jokes, knowing looks, encoding stories.",
            "Rung three is structural: exclusion built into arrangements - meetings, roles, circles redrawn.",
            "Rung four is open: the public dressing-down, scorn as honesty.",
            "Each rung feels proportionate from inside, because the verdict has been growing too.",
            "De-escalate in reverse: re-include, refuse the audience, appeal the private verdict - early.",
        ],
        "requirements": [
            "No equipment needed - this is a reading and reflection record.",
            "Locate the highest rung you have observed in group life.",
            "Practice spotting rung two - the audience - as the key intervention point.",
        ],
        "standards": [
            "Public record in the Signature system - descriptive, educational.",
            "Escalation ladder is a descriptive model; general guidance only.",
            "Never diagnoses any real person with any emotional state.",
        ],
        "citations": [C_GOTTMAN, C_MELWANI, C_FR],
        "sig_lens": (
            "The Signature Method charts escalation as the scale-house expanding: a private "
            "ledger entry becomes a posted notice, becomes a rebuilt counter, becomes a "
            "public proclamation. The Method's fire code is posted at rung one - the cheapest "
            "place to stop a fire is before it leaves the room where it started."
        ),
    },
]
ENTRIES += [
    {
        "key": "healthy-expression",
        "name": "Healthy Expression: Saying It, Showing It, Channeling It Well",
        "group": "Healthy Expression",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Contempt is information - it tells you a standard of yours has been "
            "breached - and healthy expression starts by treating it as data, not "
            "as orders. Saying it well means translating the verdict back into the "
            "standard: instead of you are pathetic, the healthy version is I "
            "expect people in this role to do X, and that is not happening. The "
            "feeling becomes a sentence about the standard, which can be discussed, "
            "instead of a verdict about the person, which cannot. Showing it well "
            "means letting the coolness do honest work: contempt's low arousal is "
            "an asset - it lets you state a hard judgment calmly, without the heat "
            "that turns feedback into combat. Channeling it well means aiming the "
            "ranking energy at systems, not souls: the contempt for sloppy work "
            "becomes a better checklist; the contempt for shamelessness becomes a "
            "clearer boundary. And sometimes healthy expression is expression "
            "declined: noticing the verdict, checking whether the standard is one "
            "you actually endorse, and letting the feeling pass unvoiced when the "
            "standard fails your own inspection. The measure of healthy "
            "expression is simple: after it, the standard is clearer and the "
            "person is still intact."
        ),
        "how_it_works": (
            "Healthy expression works by separating the feeling's two components: "
            "the standard (legitimate information about what you value) and the "
            "verdict (the ranking of the person). The standard can be voiced, "
            "negotiated, and built into better systems; the verdict, voiced raw, "
            "only wounds and entrenches. Translation - turning you are beneath "
            "me into this standard matters to me - preserves the information "
            "while discarding the hierarchy. Declined expression works through "
            "standard-auditing: many contempt verdicts rest on standards the "
            "feeler would not defend on reflection, and those dissolve under "
            "inspection."
        ),
        "key_points": [
            "Treat contempt as data, not orders: it signals a breached standard of yours.",
            "Translate the verdict into the standard: I expect X in this role becomes discussable.",
            "Use the coolness as an asset: low arousal lets hard judgments be stated calmly.",
            "Channel ranking energy at systems, not souls: better checklists, clearer boundaries.",
            "Sometimes healthiest is declined: audit the standard, let the feeling pass unvoiced.",
            "The measure: after healthy expression, the standard is clearer and the person is still intact.",
        ],
        "requirements": [
            "No equipment needed - this is a reading and reflection record.",
            "Practice the translation: verdict into standard, out loud, alone first.",
            "General everyday guidance only, not therapeutic advice.",
        ],
        "standards": [
            "Public record in the Signature system - descriptive, educational.",
            "Guidance is general and everyday; not clinical or therapeutic advice.",
            "Never diagnoses any real person with any emotional state.",
        ],
        "citations": [C_HG, C_HAIDT, C_GOTTMAN],
        "sig_lens": (
            "The Signature Method treats healthy expression as honest weighing done in the open: "
            "the standard posted on the wall, the measurement read aloud, the parcel handled "
            "with care. The Method's hallmark of the master weigher - the scale is public, the "
            "hands are steady, and nothing weighed is ever diminished by the weighing."
        ),
    },
    {
        "key": "unhealthy-expression",
        "name": "Unhealthy Expression: Bottling Up or Exploding - What Each Costs",
        "group": "Healthy Expression",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Contempt goes wrong in two directions. Bottling it up looks like "
            "peace: the verdict never gets voiced, the politeness never cracks. "
            "But the unvoiced verdict does not disappear - it ferments. The "
            "feeler starts keeping score silently: every interaction filtered "
            "through the hidden ranking, every kindness from the target read as "
            "manipulation. The relationship hollows out from the inside while "
            "looking fine from the outside, and the eventual discovery - that "
            "you have been judged for months - lands harder than any honest "
            "argument would have. Exploding looks like honesty: the verdict "
            "delivered raw - you are pathetic, everyone knows it. The cost is "
            "immediate and total: the target hears a verdict on their worth, not "
            "a complaint about behavior, and worth-verdicts do not get argued "
            "with, they get fled from or fought to the death. Relationships "
            "rarely survive a direct contempt explosion; the research on "
            "marriages shows contempt expressed openly and repeatedly is among "
            "the strongest predictors of breakdown. Both directions share one "
            "root: the verdict was never translated into a standard. Bottling "
            "keeps the verdict and hides it; exploding keeps the verdict and "
            "hurls it. Health is the third road: keep the standard, retire the "
            "verdict."
        ),
        "how_it_works": (
            "Bottling costs through accumulation: each suppressed verdict adds "
            "weight to the hidden file, and the file eventually distorts all "
            "perception of the target - the mind cannot hold a secret ranking "
            "without it coloring everything. Exploding costs through finality: "
            "a worth-verdict, once spoken, cannot be unheard, and it redefines "
            "the relationship as hierarchical combat. Both bypass the only "
            "move that resolves the underlying standard-breach: stating what "
            "is expected, plainly and early, while the verdict is still small "
            "enough to translate."
        ),
        "key_points": [
            "Bottling looks like peace but ferments: the hidden verdict hollows the relationship from inside.",
            "Silent score-keeping distorts perception: every kindness reads as manipulation.",
            "Exploding looks like honesty but delivers a worth-verdict, which cannot be argued with.",
            "Openly and repeatedly expressed contempt is among the strongest predictors of relationship breakdown.",
            "Both directions share one root: the verdict was never translated into a standard.",
            "The third road: keep the standard, retire the verdict - state expectations plainly and early.",
        ],
        "requirements": [
            "No equipment needed - this is a reading and reflection record.",
            "Notice which direction you default to: bottle or explode.",
            "General everyday guidance only, not therapeutic advice.",
        ],
        "standards": [
            "Public record in the Signature system - descriptive, educational.",
            "Costs described as documented patterns; general guidance only.",
            "Never diagnoses any real person with any emotional state.",
        ],
        "citations": [C_GOTTMAN, C_HG, C_FR],
        "sig_lens": (
            "The Signature Method files the two failures as the sealed vault (bottling) and the "
            "smashed scale (exploding): one hides the weights until they rot the floor, the "
            "other breaks the instrument in public. The Method keeps the third road lit - the "
            "open counter, where standards are posted and parcels are weighed in daylight."
        ),
    },
    {
        "key": "everyday-practices",
        "name": "Everyday Practices: Small Habits That Keep Contempt in Balance",
        "group": "Healthy Expression",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Balance with contempt is maintenance, not mastery - small habits, "
            "repeated. The verdict audit: once a day, pick one person you ranked "
            "low and ask what standard you applied and whether you endorse it; "
            "most daily verdicts fail this audit and dissolve. The competence "
            "inventory: when contempt says someone is incompetent, list three "
            "things they do adequately - the exercise breaks the generalization "
            "that feeds the feeling. The hierarchy holiday: deliberately spend "
            "time in a domain where you are the beginner - a new skill, a new "
            "game - and feel what it is like to be the ranked one; humility is "
            "contempt's natural solvent. The translation drill: catch one "
            "contemptuous thought a day and restate it as a standard - he is "
            "useless in meetings becomes I need meetings to have clear "
            "preparation. The direct channel: when a standard truly matters, say "
            "so early and plainly to the person, before the verdict has time to "
            "harden. None of these eliminate contempt - it is a built-in "
            "ranking system, and ranking is part of social life. They keep it "
            "honest: verdicts that survive the audit are usually worth voicing "
            "as standards, and the rest were never measurements at all."
        ),
        "how_it_works": (
            "Each practice targets one link in contempt's machinery. The audit "
            "targets unexamined standards; the inventory targets generalization; "
            "the hierarchy holiday targets the feeler's own position blindness; "
            "the translation drill targets the verdict-to-standard conversion; "
            "the direct channel targets hardening over time. Together they form "
            "a supervision system for the background ranker: the feeling still "
            "fires, but every firing gets reviewed. Practices work because they "
            "are small and repeatable - contempt is maintained by hundreds of "
            "tiny unexamined verdicts, so it is dismantled the same way."
        ),
        "key_points": [
            "The verdict audit: daily, test one low ranking against a standard you actually endorse.",
            "The competence inventory: list three things the target does adequately to break generalization.",
            "The hierarchy holiday: be the beginner somewhere; humility is contempt's natural solvent.",
            "The translation drill: restate one contemptuous thought daily as a plain standard.",
            "The direct channel: voice real standards early, before verdicts harden.",
            "The goal is honest ranking, not no ranking: audited verdicts become voicable standards.",
        ],
        "requirements": [
            "No equipment needed - small daily habits only.",
            "A private notebook helps for the audit and inventory.",
            "General everyday guidance only, not therapeutic advice.",
        ],
        "standards": [
            "Public record in the Signature system - descriptive, educational.",
            "Practices are general wellness habits; not clinical or therapeutic advice.",
            "Never diagnoses any real person with any emotional state.",
        ],
        "citations": [C_HG, C_HAIDT, C_GOTTMAN],
        "sig_lens": (
            "The Signature Method keeps these practices as the scale-house maintenance log: "
            "daily calibration checks, each one small, each one dated. The Method's craftsman's "
            "motto - a scale that is never calibrated eventually weighs only the weigher's mood. "
            "Calibrate daily."
        ),
    },
    {
        "key": "reading-others",
        "name": "Reading the Signs: Recognizing Contempt in Others",
        "group": "Recognizing It in Others",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Reading contempt in others is reading a verdict someone is trying "
            "not to announce. Start with the face: the one-sided mouth "
            "tightening, the gaze that narrows and slides past you, the smooth "
            "forehead that rules out anger. Then the voice: the slowed, "
            "over-patient teacher tone, the small exhale before answering, the "
            "laugh that is really an exhale. Then the body: the lean-back, the "
            "chin lift, the gestures slowing to half speed. Then the pattern "
            "across time: are you being consulted less, informed later, invited "
            "but not included? Single signs mean little - anyone can have an "
            "off moment. The read becomes reliable when channels agree: face, "
            "voice, and body all telling the same cool story, sustained across "
            "interactions. Two cautions matter. First, contempt is the most "
            "deniable emotion to confront - I was just tired covers almost any "
            "single signal, so gather the pattern before you name it. Second, "
            "never read contempt into strangers from one glance: the "
            "one-sided resting face exists, and misreading it starts conflicts "
            "that the other person never signed up for. Read to understand, "
            "not to accuse - the goal is information about the relationship, "
            "not ammunition."
        ),
        "how_it_works": (
            "Reliable reading works through channel convergence: no single cue "
            "is diagnostic, but face plus voice plus body plus behavioral "
            "pattern, sustained over time, is strong evidence. The deniability "
            "problem is handled by patience: patterns defeat denials, incidents "
            "do not. The false-positive problem - resting asymmetry, cultural "
            "politeness norms, simple fatigue - is handled by base rates: know "
            "the person's normal before you read deviations. The purpose "
            "constraint matters most: reading to understand lets you address "
            "the underlying standard-breach; reading to accuse just starts the "
            "escalation ladder from the other side."
        ),
        "key_points": [
            "Read the verdict being withheld: one-sided mouth, sliding gaze, smooth forehead.",
            "Add the voice: teacher-tone, the exhale before answering, the laugh that is an exhale.",
            "Add the body: lean-back, chin lift, half-speed gestures; then the pattern across time.",
            "Single signs mean little; channels agreeing over time is what makes the read reliable.",
            "Contempt is maximally deniable - gather the pattern before naming it.",
            "Read to understand, not to accuse: the goal is information, not ammunition.",
        ],
        "requirements": [
            "No equipment needed - this is a reading and reflection record.",
            "Know a person's normal before reading deviations.",
            "Restraint: never confront on a single cue.",
        ],
        "standards": [
            "Public record in the Signature system - descriptive, educational.",
            "Reading guidance emphasizes patterns and cautions against accusation.",
            "Never diagnoses any real person with any emotional state.",
        ],
        "citations": [C_EKMAN, C_GOTTMAN, C_HG],
        "sig_lens": (
            "The Signature Method trains reading as apprentice work at the scale-house window: "
            "watch the weigher, not the weights. The Method's apprentice oath - observe the "
            "channels, wait for convergence, and never announce a reading you would not defend "
            "with the full pattern."
        ),
    },
    {
        "key": "supportive-response",
        "name": "What to Say and Do When Someone Near You Feels Contempt",
        "group": "Recognizing It in Others",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "When someone near you is holding contempt - for a third person, or "
            "worse, for you - the supportive move is to address the standard, "
            "not the verdict. If a friend is contemptuous toward someone else: "
            "ask about the standard, not the person - what did you expect them "
            "to do? This invites translation without confrontation, and it "
            "often reveals that the standard was unclear or unfair. Do not join "
            "the verdict: the knowing laugh, the added insult, the recruited "
            "audience - all of these escalate rung two and make you a party to "
            "someone else's ranking. If the contempt is aimed at you: stay "
            "with the observable - I have noticed I am being looped in late; "
            "is there an expectation I am missing? This names the pattern "
            "without naming the feeling, which gives the other person room to "
            "translate their own verdict. Do not grovel and do not counter-attack: "
            "groveling confirms the hierarchy, counter-contempt starts a war. "
            "The steady middle is curiosity about standards plus dignity about "
            "worth: I want to meet the real expectation; I do not accept the "
            "verdict on my worth. Sometimes the supportive response is distance: "
            "if someone's contempt for you is settled and structural, the "
            "healthy move is not to win the ranking but to leave the scale-house."
        ),
        "how_it_works": (
            "Standard-focused responses work because they give the contemptuous "
            "person an honorable exit from the verdict: translating a ranking "
            "into an expectation preserves their information while retiring "
            "their hierarchy. Refusing the audience works because rung-two "
            "escalation needs recruits; without them, the social performance "
            "starves. Pattern-naming without feeling-naming works because it "
            "is undeniable (the late loop-ins happened) without being "
            "accusatory (no one is charged with feeling contempt). Dignity "
            "plus curiosity works because it separates the two things contempt "
            "fuses: the standard, which deserves discussion, and the worth-"
            "verdict, which deserves refusal."
        ),
        "key_points": [
            "Address the standard, not the verdict: ask what was expected, not who is lesser.",
            "Do not join the verdict: the knowing laugh recruits you to someone else's ranking.",
            "If it is aimed at you, name the observable pattern, not the feeling.",
            "Neither grovel nor counter-attack: groveling confirms the hierarchy, war starts one.",
            "Hold dignity plus curiosity: discuss the expectation, refuse the worth-verdict.",
            "Sometimes the healthy move is distance: leave the scale-house rather than win the ranking.",
        ],
        "requirements": [
            "No equipment needed - this is a reading and reflection record.",
            "Practice standard-questions in low-stakes moments first.",
            "General everyday guidance only, not therapeutic advice.",
        ],
        "standards": [
            "Public record in the Signature system - descriptive, educational.",
            "Responses are general social guidance; not clinical or therapeutic advice.",
            "Never diagnoses any real person with any emotional state.",
        ],
        "citations": [C_GOTTMAN, C_HG, C_FR],
        "sig_lens": (
            "The Signature Method scripts the supportive response as the honest broker's lines: "
            "read the standard aloud, decline the ranking, keep the counter clean. The Method's "
            "broker rule - you can mediate a measurement dispute, but you cannot mediate a "
            "verdict on someone's worth. Know which room you are in."
        ),
    },
    {
        "key": "what-not-to-do",
        "name": "What Not to Do: Mistakes That Make Contempt Worse",
        "group": "Recognizing It in Others",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Certain responses pour fuel on contempt - in yourself and in others. "
            "Do not perform the verdict for an audience: the joke at the target's "
            "expense, the story that encodes the judgment - every telling hardens "
            "the file and recruits the room to rung two. Do not confuse contempt "
            "with insight: the cold clarity feels like clear-sightedness, but a "
            "verdict that flatters the judge deserves extra scrutiny, not less. "
            "Do not try to shame the contemptuous person out of it: shaming "
            "someone for looking down just starts a ranking war about who gets to "
            "rank. Do not answer contempt with contempt: mutual verdicts do not "
            "cancel, they compound - two scale-houses weighing each other, "
            "neither ever satisfied. Do not treat the feeling as a fact about "
            "the target: contempt is always a report on the relationship between "
            "your standard and their behavior, never a measurement of their "
            "worth. And do not rush to voice it: contempt's coolness makes "
            "early voicing feel safe, but the verdict hardens the moment it is "
            "spoken to others - keep it private until it has survived your own "
            "audit. The common thread: everything that makes the verdict more "
            "public, more certain, or more permanent makes the contempt worse."
        ),
        "how_it_works": (
            "Each mistake feeds one of contempt's engines. Performing feeds the "
            "social engine: audiences validate and harden verdicts. Trusting the "
            "clarity feeds the certainty engine: unexamined verdicts feel true "
            "because they feel cool. Shaming and counter-contempt feed the "
            "hierarchy engine: ranking wars have no natural end. Treating the "
            "feeling as fact feeds the generalization engine: the person-file "
            "gets edited instead of the standard getting examined. Early voicing "
            "feeds the commitment engine: spoken verdicts become positions to "
            "defend. Avoiding all five starves every engine at once - which is "
            "why the list, though simple, is powerful in combination."
        ),
        "key_points": [
            "Do not perform the verdict for an audience: every telling hardens the file.",
            "Do not confuse contempt with insight: verdicts that flatter the judge need extra scrutiny.",
            "Do not shame the contemptuous: shaming starts a ranking war about who gets to rank.",
            "Do not answer contempt with contempt: mutual verdicts compound, they do not cancel.",
            "Do not treat the feeling as a fact about the target: it reports your standard, not their worth.",
            "Do not voice it early: keep the verdict private until it survives your own audit.",
        ],
        "requirements": [
            "No equipment needed - this is a reading and reflection record.",
            "Memorize the five engines; spot which one a situation is feeding.",
            "General everyday guidance only, not therapeutic advice.",
        ],
        "standards": [
            "Public record in the Signature system - descriptive, educational.",
            "Mistakes framed as common patterns; general guidance only.",
            "Never diagnoses any real person with any emotional state.",
        ],
        "citations": [C_GOTTMAN, C_FR, C_HG],
        "sig_lens": (
            "The Signature Method posts this record as the warning placard on the scale-house "
            "wall: five ways to break the instrument, each illustrated. The Method's safety "
            "inspector reads it aloud to every apprentice - the scale is a precision tool; "
            "these are the five ways apprentices have broken it."
        ),
    },
    {
        "key": "neighbors",
        "name": "The Related Emotions Map: Neighbors, Opposites, and Close Cousins",
        "group": "Related Emotions and Simulation",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Contempt's neighborhood is crowded, and the borders matter. "
            "Disdain is the closest cousin - nearly identical, slightly lighter, "
            "more about taste than worth; if contempt is the verdict, disdain is "
            "the raised eyebrow before the verdict. Scorn is contempt performed: "
            "the same looking-down, made public and theatrical. Derision adds "
            "laughter - contempt with an audience laughing along. Snobbery is "
            "contempt as lifestyle: the ranking system made into an identity. "
            "Pity looks similar from the outside - the same looking-down posture - "
            "but the appraisal is opposite: pity says you are unfortunate, "
            "contempt says you are unworthy; pity can coexist with warmth, "
            "contempt cannot. Disgust is the famous cousin: disgust rejects "
            "contamination and wants distance from the thing; contempt judges "
            "inferiority and wants distance from the person - disgust says get "
            "it away from me, contempt says you are beneath me. Anger is the "
            "frequent neighbor: anger confronts to change behavior, contempt "
            "dismisses because change seems pointless. The opposite pole is "
            "respect and admiration: the same ranking machinery pointed upward, "
            "looking up instead of down. The map's practical use: when the "
            "feeling is unclear, check the borders - the direction of the gaze "
            "(up or down), the temperature (hot or cool), and the target (act "
            "or person) will place you."
        ),
        "how_it_works": (
            "The map is organized by three axes. Gaze direction: contempt, "
            "disdain, scorn, and snobbery look down; respect and admiration look "
            "up; pity looks down but with warmth. Temperature: contempt and "
            "disdain run cool; anger and derision run hot. Target: anger and "
            "disgust target acts and things; contempt targets the person. "
            "Placing a feeling on the three axes locates it in the neighborhood "
            "and, more importantly, reveals what the appraisal actually was - "
            "which is the information you need to respond well."
        ),
        "key_points": [
            "Disdain: the closest cousin - lighter, more about taste; the raised eyebrow before the verdict.",
            "Scorn: contempt performed publicly; derision: contempt with a laughing audience; snobbery: contempt as identity.",
            "Pity looks similar but appraises opposite: unfortunate vs unworthy; pity allows warmth, contempt does not.",
            "Disgust vs contempt: disgust rejects contamination (get it away), contempt judges inferiority (you are beneath me).",
            "Anger vs contempt: anger confronts to change behavior; contempt dismisses as change seeming pointless.",
            "Opposite pole: respect and admiration - the same ranking machinery pointed upward.",
        ],
        "requirements": [
            "No equipment needed - this is a reading and reflection record.",
            "Use the three axes - gaze, temperature, target - to place unclear feelings.",
            "Familiarity with the basic definitions of the neighboring emotions.",
        ],
        "standards": [
            "Public record in the Signature system - descriptive, educational.",
            "Map follows standard emotion-differentiation literature.",
            "Never diagnoses any real person with any emotional state.",
        ],
        "citations": [C_HG, C_FR, C_CAD],
        "sig_lens": (
            "The Signature Method draws this map as the surveyor's chart of the high country: "
            "every neighboring peak labeled, every border walked. The Method's surveyor note - "
            "the most expensive mistakes in the hills are made at the borders, where one "
            "territory looks exactly like another. Check the axes before you plant your flag."
        ),
    },
    {
        "key": "mixes",
        "name": "Emotion Mixes: Contempt Blended With Other Emotions",
        "group": "Related Emotions and Simulation",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Contempt rarely travels pure; its blends each have their own character. "
            "Contempt plus anger is indignation: righteous certainty, hot and cold "
            "at once - not only wrong, but beneath me for being wrong; the blend "
            "that lectures. Contempt plus disgust is utter revulsion at a person: "
            "the target is both inferior and contaminating - judged and untouchable; "
            "this is the blend behind shunning and social exile. Contempt plus "
            "amusement is mockery: the looking-down made entertaining, the verdict "
            "delivered as comedy; the audience's laughter is the blend's fuel, and "
            "the target's humiliation is its product. Contempt plus pity is "
            "condescension: warmth and dismissal in one gesture - the pat on the "
            "head, the there-there that diminishes; the blend that helps while "
            "keeping the hierarchy intact. Contempt plus fear is the bully's "
            "blend: looking down on someone while fearing their power produces "
            "the preemptive strike - diminish them before they can diminish you. "
            "Each blend can be read by its signature: indignation lectures, "
            "revulsion shuns, mockery performs, condescension pats, the bully's "
            "blend strikes first. Knowing the blends matters because pure contempt "
            "is manageable, but the blends recruit other engines - and engines "
            "in combination are what do the real damage."
        ),
        "how_it_works": (
            "Blends form when two appraisals fire on the same target: the "
            "hierarchy appraisal (contempt) plus a second appraisal - wrongness "
            "(anger), contamination (disgust), absurdity (amusement), misfortune "
            "(pity), threat (fear). Each appraisal contributes its action "
            "tendency, and the tendencies combine: dismiss plus confront becomes "
            "the lecture; dismiss plus avoid becomes shunning; dismiss plus play "
            "becomes mockery. The blends are more stable than pure contempt "
            "because each appraisal validates the other - which is why "
            "identifying the blend is the first step to dismantling it: "
            "address the appraisals separately."
        ),
        "key_points": [
            "Contempt + anger = indignation: righteous certainty; the blend that lectures.",
            "Contempt + disgust = revulsion at a person: judged and untouchable; the blend behind shunning.",
            "Contempt + amusement = mockery: the verdict delivered as comedy; laughter is the fuel.",
            "Contempt + pity = condescension: the pat on the head; help that keeps the hierarchy intact.",
            "Contempt + fear = the bully's blend: diminish them before they can diminish you.",
            "Blends are more stable than pure contempt: each appraisal validates the other; address them separately.",
        ],
        "requirements": [
            "No equipment needed - this is a reading and reflection record.",
            "Practice naming the blend when the feeling is compound.",
            "Familiarity with the basic definitions of the partner emotions.",
        ],
        "standards": [
            "Public record in the Signature system - descriptive, educational.",
            "Blends described via appraisal theory, not clinical terms.",
            "Never diagnoses any real person with any emotional state.",
        ],
        "citations": [C_HG, C_CAD, C_FR],
        "sig_lens": (
            "The Signature Method keeps the blends as alloy samples in the assay office: each one "
            "stamped with its composition - contempt-angler, contempt-disgust, contempt-mirth. "
            "The Method's assayer rule - pure metals bend; it is the alloys that cut. Test the "
            "composition before handling the blade."
        ),
    },
    {
        "key": "full-simulation",
        "name": "Full Behavioral Simulation: From Trigger Through Peak to Resolution",
        "group": "Related Emotions and Simulation",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Scene one, the trigger. A team meeting. A colleague - call him the "
            "presenter - walks the room through a plan riddled with errors he "
            "does not see. He is confident, expansive, wrong. Halfway through "
            "slide three, the appraisal clicks in a watcher: this person should "
            "know better, and does not. The onset is instant and quiet - a "
            "fractional tightening at one mouth corner, a fractional slowing of "
            "the breath. Scene two, the plateau. The watcher stops listening and "
            "starts composing: the corrections, the questions that are really "
            "verdicts. The body settles - lean back, chin up, gestures at half "
            "speed. When the presenter finishes, the watcher delivers the "
            "teacher-voice: well, actually... followed by a demolition disguised "
            "as clarification. The room feels the temperature drop; two colleagues "
            "exchange the knowing look - rung two, the audience recruited. "
            "Scene three, the cascade. Over the next weeks the verdict "
            "generalizes: the presenter's laugh irritates, his emails get skimmed, "
            "his name arrives with the curl. He is looped in late, then not at "
            "all - rung three, structural. The watcher feels the clean, cold "
            "certainty of it and mistakes it for leadership. Scene four, the "
            "reckoning. A missed deadline traceable to the exclusion surfaces; "
            "a senior colleague asks the plain question: what standard is he "
            "failing? The watcher is forced to state it - preparation, rigor - "
            "and in stating it, hears how discussable it always was. Scene five, "
            "resolution. The standard gets posted: every plan reviewed against "
            "a checklist, presenter's included, watcher's included. The verdict "
            "is retired; the standard remains. The presenter is still not the "
            "watcher's favorite colleague - but he is a colleague again, not a "
            "file. The simulation's lesson, stated plainly: contempt did its "
            "real job in scene one - flagging a breached standard - and then "
            "kept working long after the job was done. Resolution is not the "
            "absence of the feeling; it is the feeling translated, audited, "
            "and retired on schedule."
        ),
        "how_it_works": (
            "The simulation walks the full machinery in order: trigger "
            "appraisal, cool plateau, behavioral enactment (teacher-voice, "
            "audience recruitment), cascade and generalization, structural "
            "exclusion, the reckoning question that forces translation, and "
            "resolution through posted standards. Each scene demonstrates one "
            "record's lesson in motion: onset speed, the plateau's low cost, "
            "rung-by-rung escalation, the conclusion-first distortion, the "
            "translation that resolves. The arc is the archive's showcase "
            "because it shows the whole system - feeling, face, body, speech, "
            "behavior, and repair - as one continuous human event."
        ),
        "key_points": [
            "Scene one: the trigger - confident error, the appraisal clicking, the quiet one-sided onset.",
            "Scene two: the plateau - teacher-voice demolition, the knowing look, the audience recruited.",
            "Scene three: the cascade - generalization, structural exclusion, certainty mistaken for leadership.",
            "Scene four: the reckoning - the plain question about the standard forces translation.",
            "Scene five: resolution - the standard posted, the verdict retired, the colleague restored.",
            "The lesson: contempt flagged a real standard in scene one, then kept working after the job was done.",
        ],
        "requirements": [
            "No equipment needed - this is a reading and reflection record.",
            "Read straight through; the scenes build on each other.",
            "All characters are fictional composites for illustration.",
        ],
        "standards": [
            "Public record in the Signature system - descriptive, educational.",
            "Simulation uses fictional characters; never about any real person.",
            "Never diagnoses any real person with any emotional state.",
        ],
        "citations": [C_GOTTMAN, C_FR, C_HG],
        "sig_lens": (
            "The Signature Method stages this simulation as the scale-house's demonstration day: "
            "the full instrument run from first parcel to final audit, apprentices watching "
            "from the gallery. The Method's closing line to the gallery - you have now seen "
            "the machine do everything it does. The question that remains is the one the "
            "machine cannot answer for you: who calibrates the calibrator?"
        ),
    },
]
