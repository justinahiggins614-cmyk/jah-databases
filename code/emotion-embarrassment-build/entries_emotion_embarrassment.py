#!/usr/bin/env python3
"""Entries for the Embarrassment Emotion databases (Manon's 2026-10-17 16:15
order, emotion series batch 2).

Descriptive and educational ONLY - the database describes and simulates
embarrassment; it never diagnoses real people, never labels any real person
with an emotional state, and never offers therapeutic advice beyond general,
safe, everyday guidance. No clinical language, no diagnostic labels. Healthy
expression records emphasize graceful recovery and kindness toward oneself.

34 records, ordered by the teaching ladder (ladder_rank 1-34, non-decreasing),
following the shared emotion-template spec: what embarrassment IS ->
first-person simulation -> body signals -> facial expression -> triggers ->
behavior -> healthy expression -> recognizing it in others -> related emotions
and mixes -> complex behavioral simulation.

ID prefixes: JAH-EMEB- (public) and JAH-EMEBS- (signature), verified free in
the manifest id_prefix values and in all jah-databases-data-1 shard record
IDs, 2026-10-17.

Public records are real, fact-checked psychology knowledge (Darwin, Goffman,
Keltner and Buswell, Miller, Tangney and Dearing, Lewis, Leary, Edelmann,
Modigliani, APA Dictionary). Signature editions are his original Signature
lens - embarrassment as the soul's honest social signal, the bright blush
that proves a person cares about belonging; every facet framed as signal,
repair, and mastery - never presented as authentic public record.

Never the words "bat belt" anywhere. No website references. No Facebook.
No religious talk. Nothing hate-adjacent, profane, or inappropriate.
"""

SIG_TAIL = ("Signature original - his original Signature lens: embarrassment "
            "as the soul's honest social signal, the bright blush that proves "
            "a person cares about belonging and connection; Signature editions "
            "frame every facet as signal, repair, and mastery - never as a "
            "diagnosis, never labeling any real person, and never presented as "
            "authentic public record.")

CIT_DARWIN = ("Darwin C. The Expression of the Emotions in Man and Animals. "
              "Murray; 1872.")
CIT_GOFFMAN = ("Goffman E. The Presentation of Self in Everyday Life. "
               "Doubleday; 1959.")
CIT_GOFFMAN_IR = ("Goffman E. Interaction Ritual: Essays on Face-to-Face "
                  "Behavior. Aldine; 1967.")
CIT_KELTNER = ("Keltner D, Buswell BN. Embarrassment: its distinct form of "
               "nonverbal display and consequences for social interaction. "
               "Journal of Personality and Social Psychology. 1997;73(4):"
               "757-772.")
CIT_MILLER = ("Miller RS. Embarrassment: Poise and Peril in Everyday Life. "
              "Guilford; 1996.")
CIT_TANGNEY = ("Tangney JP, Dearing RL. Shame and Guilt. Guilford; 2002.")
CIT_LEWIS = ("Lewis M. Shame: The Exposed Self. Free Press; 1992.")
CIT_LEARY = ("Leary MR. Self-Presentation: Impression Management and "
             "Interpersonal Behavior. Westview; 1996.")
CIT_EDELMANN = ("Edelmann RJ. The Psychology of Embarrassment. Wiley; 1987.")
CIT_MODIGLIANI = ("Modigliani A. Embarrassment, facework, and eye contact: "
                  "testing a theory of embarrassment. Journal of Personality "
                  "and Social Psychology. 1971;17(1):15-24.")
CIT_APA = ("American Psychological Association. APA Dictionary of Psychology; "
           "current edition.")

STD = [
    "Every record is the full fully-formed entry with all data - never a title or description stub.",
    "Record renders as human-readable sentences and paragraphs - never garbled or one-letter-at-a-time text.",
    "Descriptive and educational only: the record describes and simulates embarrassment; it never diagnoses any real person and never labels any real person with an emotional state.",
    "Screened content: no hate-adjacent or profane material, no religious framing, no clinical or diagnostic language.",
]

ENTRIES = [
# ------------------------------------------------- 1-4: what embarrassment IS
dict(
    key="embarrassment_definition", name="What Embarrassment Is: A Plain-Language Definition",
    group="Foundations", ladder_rank=1, ladder_tier="foundations",
    description=(
        "Embarrassment is the hot, self-conscious flush you feel when you have "
        "slipped in front of others - tripped on a step, said the wrong thing, "
        "been caught not knowing something everyone else knows. In everyday "
        "words: embarrassment is the mind's social alarm that says, \"everyone "
        "saw that, and it was not the me I wanted them to see.\" It is one of "
        "the self-conscious emotions - the feelings that only switch on when "
        "we imagine how we look through other people's eyes. Unlike fear, which "
        "responds to danger, embarrassment responds to a threat to your "
        "public image: the gap between the person you meant to present and "
        "the person everyone just watched. Its signature is physical and "
        "immediate - the blush, the heat in the cheeks, the urge to vanish - "
        "and it usually fades within minutes, often leaving a rueful smile "
        "behind. Embarrassment is not a verdict on your worth; it is a brief, "
        "human signal that you care about how you connect with other people."),
    how_it_works=(
        "The embarrassment sequence runs in five beats: exposure, appraisal, "
        "arousal, display, and repair. First, something exposes you - a slip, "
        "a mistake, an accident - in front of witnesses, real or imagined. "
        "Second, the mind appraises it socially: did that break an expectation "
        "of how I should look, sound, or act? The appraisal is fast and "
        "automatic, which is why the feeling can hit before you have even "
        "finished thinking about what happened. Third, the body arouses: blood "
        "vessels in the face and neck widen, producing the blush; heart rate "
        "climbs; attention narrows onto the audience. Fourth comes the "
        "involuntary display - the blush, the downward gaze, the nervous grin "
        "- a set of signals that researchers have found actually communicate "
        "remorse and social awareness to witnesses, often earning sympathy "
        "rather than scorn. Fifth, the person repairs: an apology, a joke "
        "about the slip, a change of subject. Understanding this chain is the "
        "key to the whole database: embarrassment is not an enemy to destroy "
        "but a social signal to read, ride, and repair."),
    key_points=[
        "Embarrassment is a self-conscious emotion: it switches on when you imagine how you look through other people's eyes.",
        "The core signal is a gap between the self you meant to present and the self everyone just saw.",
        "The sequence is exposure -> appraisal -> arousal -> display -> repair; each step is a place the feeling can be worked with.",
        "The blush is involuntary and universal - a social signal that often earns sympathy rather than judgment.",
        "The feeling is brief and normal; it means you care about connection, not that anything is wrong with you.",
    ],
    requirements=[
        "Everyday definition a student or writer can quote",
        "Clear contrast with fear (danger) and shame (worth)",
        "The five-beat sequence stated in plain words",
        "The blush explained as social signal, not flaw",
        "Reassurance: normal, brief, and human",
    ],
    standards=STD,
    citations=[CIT_DARWIN, CIT_GOFFMAN, CIT_KELTNER, CIT_MILLER, CIT_APA],
    sig_lens=(
        "In the Signature lens, embarrassment is the soul's honest social "
        "signal - proof of belonging in the heart. The blush is not a "
        "malfunction; it is the Signature of a person who shows up in "
        "public, who risks being seen, who cares enough about others to "
        "feel the miss. Signal: your belonging-sense is working exactly as "
        "designed. Repair: the joke, the apology, the laugh - these are "
        "crafts, not grovels. Mastery: the person who can blush and keep "
        "walking owns the room more than the person who never blushes at "
        "all.")),
dict(
    key="embarrassment_emotion_family", name="Where Embarrassment Sits in the Emotion Family",
    group="Foundations", ladder_rank=2, ladder_tier="foundations",
    description=(
        "Embarrassment belongs to the self-conscious emotions - the family "
        "that includes shame, guilt, pride, and embarrassment itself - "
        "emotions that require a self that can look at itself. Where the "
        "basic emotions (fear, anger, joy, sadness, surprise, disgust) can be "
        "felt alone on a desert island, the self-conscious emotions need an "
        "audience: real, remembered, or imagined. Within the family, "
        "embarrassment sits closest to shame as its milder, briefer cousin, "
        "but the two are distinct. Shame says \"I am bad\" and aims at the "
        "whole self; embarrassment says \"that looked bad\" and aims at a "
        "specific moment. Guilt says \"I did wrong\" and aims at an action "
        "toward someone harmed. Embarrassment is the lightest of the three - "
        "it fades in minutes, often dissolves in laughter, and carries no "
        "lasting stain. It also has a special social job: while shame drives "
        "people to hide and guilt drives them to repair, embarrassment's "
        "blush displays awareness and appeases the audience, keeping the "
        "person in the group."),
    how_it_works=(
        "Think of the emotion family as a tree. The roots are the basic "
        "emotions - fast, physical, shared with animals. One branch grows "
        "into the social emotions, and from it sprouts the self-conscious "
        "cluster. Embarrassment occupies the twig where three things meet: "
        "self-awareness (you see yourself being seen), norm-awareness (you "
        "know the expectation you missed), and exposure (someone could have "
        "noticed). Remove any one of these and embarrassment cannot form: "
        "without an audience there is no embarrassment, only a private "
        "mistake; without a norm there is no slip, only an event; without "
        "self-awareness there is no feeling, only an observation. This is why "
        "toddlers, who lack stable self-awareness, rarely blush with "
        "embarrassment, and why the feeling intensifies in adolescence, when "
        "the imagined audience is loudest. Knowing embarrassment's family "
        "address tells you exactly which levers change it: shrink the "
        "audience, reframe the norm, or anchor the self - and the feeling "
        "shrinks with them."),
    key_points=[
        "Embarrassment is a self-conscious emotion: it needs a self, a norm, and an audience - remove one and it cannot form.",
        "Its nearest cousins are shame (aims at the whole self) and guilt (aims at a harmed action); embarrassment aims at a single exposed moment.",
        "Embarrassment is the lightest of the three - it fades in minutes and often dissolves in shared laughter.",
        "Its social job is appeasement: the blush displays awareness and keeps the person in the group.",
        "It emerges with self-awareness in development and peaks when the imagined audience is loudest.",
    ],
    requirements=[
        "Map embarrassment among the self-conscious emotions",
        "Distinguish embarrassment from shame and guilt in one clear contrast each",
        "Name the three ingredients: self, norm, audience",
        "Explain the appeasement function plainly",
        "Note the developmental appearance with self-awareness",
    ],
    standards=STD,
    citations=[CIT_LEWIS, CIT_TANGNEY, CIT_KELTNER, CIT_GOFFMAN_IR, CIT_MILLER],
    sig_lens=(
        "In the Signature lens, the family map is a map of belonging. Basic "
        "emotions guard the body; self-conscious emotions guard the bond. "
        "Embarrassment is the lightest guard on the bond's wall - the "
        "sentinel who taps the shoulder instead of sounding the war horn. "
        "Signal: you belong somewhere worth guarding. Repair: knowing the "
        "cousins apart - embarrassment is a moment, shame is a mirror, guilt "
        "is a debt - lets you answer each with the right tool. Mastery: "
        "answer the moment and the mirror stops cracking.")),
dict(
    key="embarrassment_intensity_scale", name="Mild, Moderate, and Intense: Embarrassment at Three Volumes",
    group="Foundations", ladder_rank=3, ladder_tier="foundations",
    description=(
        "Embarrassment is one feeling with a volume knob. At mild volume, it "
        "is a warm ripple: you mispronounce a word in a small meeting, a "
        "gentle blush rises, you correct yourself with a smile, and the "
        "moment is gone before the coffee cools. The body barely registers it "
        "- a touch of heat in the cheeks, attention briefly doubled. At "
        "moderate volume, the heat deepens: you realize you have been singing "
        "along to the wrong lyrics while the carpool can hear, or you call "
        "the teacher \"mom\" in front of the class. The blush is visible, the "
        "heart knocks, the laugh is nervous, and the story gets retold at "
        "dinner with everyone's good humor. At intense volume, embarrassment "
        "is a flood: pants split on stage, the wrong name spoken at a wedding "
        "toast, a private message sent to the whole company. Heat pours up "
        "the neck, the ears burn, the hands shake, and the single thought is "
        "escape. Yet even at full volume, embarrassment has a built-in "
        "ceiling: unlike grief or rage, it almost always fades within minutes "
        "to hours, and the very people who witnessed it usually forget it "
        "far sooner than the person who felt it."),
    how_it_works=(
        "The volume knob turns on three dials: exposure (how many people saw, "
        "and how long the moment lasted), stakes (how much the slip clashed "
        "with the image you value), and audience power (how much you care "
        "about these particular witnesses). Mild is low on all three: a "
        "slip, low stakes, familiar kind faces. Moderate mixes them: maybe "
        "high exposure but low stakes (tripping in a mall crowd of strangers "
        "you will never see again). Intense maxes two or three at once: high "
        "exposure, high stakes, powerful audience - the boss, the crush, the "
        "whole room. A useful rule: the volume you feel is set by YOUR dials, "
        "not by the audience's memory. Research on the spotlight effect shows "
        "people vastly overestimate how much others notice and remember their "
        "slips. So the felt volume is real, but the lasting damage the "
        "volume predicts almost never arrives. Turn down any one dial - "
        "shrink the audience, lower the stakes, shorten the exposure - and "
        "the volume follows."),
    key_points=[
        "Mild embarrassment is a warm ripple that fades before the coffee cools; intense is a flood with a single thought of escape.",
        "The volume turns on three dials: exposure, stakes, and audience power.",
        "Even intense embarrassment has a built-in ceiling - it fades within minutes to hours, unlike grief or rage.",
        "The spotlight effect means people overestimate how much others notice and remember their slips.",
        "Turn down any one dial - audience, stakes, or exposure - and the volume follows.",
    ],
    requirements=[
        "Three lived volume levels with concrete examples",
        "The three dials named and explained",
        "The spotlight effect stated plainly",
        "The built-in ceiling of the feeling",
        "A usable rule for turning the volume down",
    ],
    standards=STD,
    citations=[CIT_MILLER, CIT_EDELMANN, CIT_LEARY, CIT_MODIGLIANI, CIT_APA],
    sig_lens=(
        "In the Signature lens, the volume knob is a belonging gauge. Mild "
        "is a tap on the shoulder - adjust and smile. Moderate is a flare - "
        "laugh it off and the room laughs with you. Intense is a bonfire - "
        "and here is the mastery: the bonfire burns loudest in the person "
        "who cares most. Signal: the volume tells you how much the moment "
        "mattered, not how much damage it did. Repair: shrink one dial at a "
        "time. Mastery: a person who has survived their bonfires stops "
        "fearing the spark.")),
dict(
    key="embarrassment_myths", name="Common Myths and Misunderstandings About Embarrassment",
    group="Foundations", ladder_rank=4, ladder_tier="foundations",
    description=(
        "Myth one: embarrassment means something is wrong with you. It means "
        "the opposite - studies of the blush find it signals social "
        "awareness, and people who blush are rated as more trustworthy and "
        "likable, not less. Myth two: confident people never get embarrassed. "
        "Everyone blushes; the difference is that practiced people recover "
        "faster, not that they never slip. Myth three: other people remember "
        "your embarrassing moments as vividly as you do. They do not - the "
        "spotlight effect shows witnesses forget fast and think of their own "
        "moments instead. Myth four: the best response is to pretend it did "
        "not happen. Ignoring a visible slip usually looks colder than owning "
        "it; a quick laugh or light apology repairs the image far better "
        "than stone silence. Myth five: embarrassment is just shame-lite, a "
        "small shame. They are different feelings with different targets - "
        "embarrassment points at a moment, shame at the self - and they need "
        "different answers. Myth six: if you feel embarrassed a lot, you are "
        "too sensitive. Frequent embarrassment usually means a strong "
        "belonging-sense working overtime in high-exposure settings, not a "
        "broken character. Clearing these myths matters because myths turn a "
        "two-minute feeling into a two-day verdict."),
    how_it_works=(
        "Myths persist because embarrassment feels like a public trial, and "
        "trials invite verdicts. The correction is always the same "
        "structure: name the felt claim, show the observed evidence, and hand "
        "back a smaller, truer story. Felt claim: \"everyone is judging me.\" "
        "Evidence: witnesses rate blushers as more likable and trustworthy, "
        "and forget the moment within hours. Smaller truer story: \"I slipped; "
        "the room moved on.\" This myth-busting works because embarrassment "
        "is an appraisal-driven feeling - change the appraisal and the "
        "feeling's tail shortens. Each myth is really a misreading of one "
        "part of the five-beat sequence: myths about the self misread the "
        "appraisal beat; myths about the audience misread the exposure beat; "
        "myths about recovery misread the repair beat. Learn to spot which "
        "beat a myth distorts, and you can correct it in the moment, before "
        "it turns a blush into a bruise."),
    key_points=[
        "Blushing signals social awareness; blushers are rated more trustworthy and likable, not less.",
        "Confident people get embarrassed too - they just recover faster.",
        "Witnesses forget fast; the spotlight effect is a myth about their memory, not a fact.",
        "Owning a visible slip with a laugh or light apology repairs better than pretending it never happened.",
        "Embarrassment is not shame-lite; each myth usually misreads one beat of the five-beat sequence.",
    ],
    requirements=[
        "Six myths stated and corrected",
        "Evidence behind each correction",
        "The spotlight effect explained",
        "Owning vs ignoring contrasted",
        "The appraisal link: myths live in the appraisal beat",
    ],
    standards=STD,
    citations=[CIT_KELTNER, CIT_MILLER, CIT_TANGNEY, CIT_MODIGLIANI, CIT_APA],
    sig_lens=(
        "In the Signature lens, a myth is a smudge on the belonging glass - "
        "it makes the moment look like a verdict on the soul. Signal: when a "
        "myth speaks (\"everyone is judging me\"), hear the misread beat, "
        "not the truth. Repair: hand the myth the smaller truer story, out "
        "loud, until it becomes habit. Mastery: the person who has busted "
        "their own myths stops renting out rooms in their head to an "
        "audience that already left.")),

# -------------------------------------- 5-9: how it feels (first-person sim)
dict(
    key="embarrassment_inside", name="Inside the Feeling: Embarrassment in the First Person",
    group="Foundations", ladder_rank=5, ladder_tier="foundations",
    description=(
        "It starts before thought: a hot tide rising from the chest to the "
        "cheeks, as if someone turned a lamp on inside your face. Time "
        "stretches - the two seconds after the slip feel like a scene played "
        "in slow motion. Your eyes drop on their own; looking up feels "
        "impossible, as if every face in the room were a spotlight. The "
        "inner voice arrives all at once: they saw that, they are laughing, "
        "how could I, I want to disappear. The body wants motion - flee, "
        "cover, shrink - but you are frozen in the middle of the stage, and "
        "the freeze itself is embarrassing. Then, usually, a mercy: someone "
        "laughs kindly, or you manage a shaky grin, and the spell cracks. "
        "The heat drains downward like a tide going out. Your own laugh "
        "sounds strange to you, too loud or too late. For a while afterward "
        "the moment replays - did I really say that? - each replay a little "
        "less hot. This is what it is like to feel embarrassment from the "
        "inside: a brief, burning exposure, followed by a slow return to "
        "yourself, with the odd after-effect of feeling oddly fond of the "
        "people who let you off the hook."),
    how_it_works=(
        "First-person simulation works because emotions are states of the "
        "whole person - body, attention, and story all at once. Reading or "
        "imagining the inside view teaches the recognition cues without "
        "requiring the slip to happen to you. The inside of embarrassment "
        "has four layers happening at once. The physical layer is heat and "
        "tension: blush, quickened heart, tightened shoulders. The "
        "attentional layer is the spotlight reversal - your attention, which "
        "normally points outward, snaps back onto yourself as an object in "
        "other people's view. The narrative layer is the instant story: "
        "\"they saw, they judge, I am exposed.\" The motivational layer is "
        "the twin urge: hide and repair. These layers explain why "
        "embarrassment feels so total despite being so brief - it colonizes "
        "body, attention, story, and urge in a single second. It also "
        "explains why the feeling responds to attention tricks: anything "
        "that moves attention back outward - a kind face, a task, a laugh - "
        "begins the cooling."),
    key_points=[
        "The inside of embarrassment is heat rising, time stretching, and the eyes dropping on their own.",
        "Four layers fire at once: physical heat, attention snapping onto the self, an instant judging story, and the twin urge to hide and repair.",
        "The inner voice speaks in verdicts: they saw, they judge, I want to disappear.",
        "The crack in the spell usually comes from kindness or a shaky grin - then the tide goes out.",
        "Simulation teaches recognition: you can learn the inside view without living the slip.",
    ],
    requirements=[
        "A first-person passage in present tense",
        "All four layers named: physical, attentional, narrative, motivational",
        "The spotlight reversal explained",
        "The recovery beat: the mercy moment",
        "The after-effect: replays that cool with time",
    ],
    standards=STD,
    citations=[CIT_MILLER, CIT_EDELMANN, CIT_MODIGLIANI, CIT_GOFFMAN, CIT_APA],
    sig_lens=(
        "In the Signature lens, the inside view is the soul reading its own "
        "belonging-meter in real time. Signal: the heat is the meter "
        "working, not failing - it only burns where belonging matters. "
        "Repair: ride the four layers instead of fighting them; the "
        "attentional layer is the steering wheel, and pointing it outward "
        "cools the rest. Mastery: a person who has mapped their own inside "
        "view stops being ambushed by it - the tide still rises, but they "
        "know exactly where the shore is.")),
dict(
    key="embarrassment_time_course", name="Onset, Peak, Fade, Aftershock: The Time Course of Embarrassment",
    group="Foundations", ladder_rank=6, ladder_tier="foundations",
    description=(
        "Embarrassment has one of the cleanest time courses of any emotion. "
        "Onset is nearly instant - the blush can begin within two to three "
        "seconds of the slip, sometimes before the person has fully "
        "registered what happened, because the social appraisal runs faster "
        "than deliberate thought. The peak arrives fast too: roughly ten to "
        "thirty seconds in, heat at maximum, heart knocking, the urge to "
        "vanish at its strongest. Then the fade begins, usually within one "
        "to three minutes, as attention returns to the surroundings and the "
        "body's arousal drains. By ten minutes, for most slips, the feeling "
        "is a warm residue rather than a burn. The aftershock is the mental "
        "part: the replay loop, where the moment returns uninvited over "
        "hours or days - in the shower, at bedtime - each replay "
        "manufacturing a fresh, smaller blush. The aftershock is not the "
        "emotion itself continuing; it is memory rehearsing the emotion. "
        "Knowing the four phases gives a person a map: this is the peak, not "
        "the permanent state; this is a replay, not a new disaster. Most "
        "people's suffering from embarrassment lives in the aftershock, not "
        "the event."),
    how_it_works=(
        "The curve is driven by two different systems running at two "
        "different speeds. The fast system is the body's arousal machinery: "
        "adrenaline and blood flow shift in seconds and clear in minutes, "
        "which sets the onset-peak-fade arc. You cannot think your way out "
        "of the blush in the first thirty seconds because the vascular "
        "system does not take suggestions - but you can outlast it, because "
        "it always clears. The slow system is memory and appraisal: every "
        "replay re-appraises the slip (\"they must think I am an idiot\"), "
        "and each appraisal re-lights a small arousal response, which is the "
        "aftershock. The practical consequence is a two-tool strategy. "
        "During onset and peak, the only tools that work are physical and "
        "attentional: breathe slowly, unclench, look at a friendly face, "
        "give the body its minute. During the aftershock, the tools are "
        "cognitive: catch the replay, run the reality check (who remembers "
        "this besides me?), and close the loop with a decisive repair - an "
        "apology made, a joke owned, a lesson filed. The emotion obeys the "
        "clock; the aftershock obeys the story. Change the story and the "
        "replays stop."),
    key_points=[
        "Onset is nearly instant (2-3 seconds); peak hits at 10-30 seconds; fade clears within 1-3 minutes.",
        "The aftershock is memory rehearsing the emotion - replays over hours or days, each manufacturing a smaller blush.",
        "Two systems drive the curve: fast body arousal (clears in minutes) and slow memory appraisal (re-lights the feeling).",
        "During onset and peak, use physical and attentional tools; during the aftershock, use cognitive tools.",
        "Most suffering lives in the aftershock, not the event - the story, not the slip.",
    ],
    requirements=[
        "Four phases with realistic time windows",
        "The two-speed systems explanation",
        "The replay loop described",
        "Two-tool strategy matched to the phases",
        "The closing line: the story, not the slip",
    ],
    standards=STD,
    citations=[CIT_MILLER, CIT_EDELMANN, CIT_KELTNER, CIT_APA, CIT_DARWIN],
    sig_lens=(
        "In the Signature lens, the time course is the soul's weather "
        "system: storms arrive fast, pass fast, and the puddles are what "
        "trip you. Signal: the peak's speed is information - fast onset "
        "means high belonging-stakes, not high danger. Repair: during the "
        "storm, hold the umbrella (breathe, unclench, wait the minute); "
        "after, drain the puddles (close the loop with a decisive repair). "
        "Mastery: the person who trusts the clock stops negotiating with "
        "the peak - they know it always, always passes.")),
dict(
    key="embarrassment_low_vs_high", name="Two Snapshots: Embarrassment at Low and High Intensity",
    group="Foundations", ladder_rank=7, ladder_tier="foundations",
    description=(
        "Low intensity, 9:04 AM: Maya waves back at someone who was waving "
        "at the person behind her. Her cheeks warm a degree. She laughs - a "
        "short, genuine ha - mouths \"oh!\" and turns back to her phone. By "
        "9:05 the moment is data, not feeling. Her inner voice: \"classic "
        "Maya,\" affectionate, not cruel. The body barely filed a report. "
        "High intensity, 2:15 PM: during her presentation, Maya's laptop "
        "projects her group chat, where she called the client \"a sentient "
        "spreadsheet.\" The heat does not rise - it detonates. Her ears "
        "burn, her hands shake on the clicker, her voice climbs half an "
        "octave. She laughs, but it comes out wrong, a bark. She apologizes "
        "three times too many, and the apology becomes its own event. For "
        "the rest of the meeting she cannot look at the client; at dinner "
        "she replays it eleven times. Same emotion, same woman, same day. "
        "The difference is not character but chemistry and context: the "
        "dials of exposure, stakes, and audience power were near zero in "
        "the morning and near maximum in the afternoon. Comparing the two "
        "snapshots side by side teaches the essential lesson of the volume "
        "knob - the feeling scales, the person stays the same, and the "
        "recovery tools that worked at 9:04 (laugh, own, move on) are the "
        "same tools that work at 2:15, applied with more patience."),
    how_it_works=(
        "The two snapshots are the same mechanism at different gains. In "
        "both, the five beats run: exposure, appraisal, arousal, display, "
        "repair. At low gain, the appraisal is gentle (\"harmless mix-up\"), "
        "the arousal is a ripple, the display is a smile, and the repair is "
        "instant and unconscious. At high gain, the appraisal is harsh "
        "(\"career-damaging insult, witnessed\"), the arousal is a flood, "
        "the display is a full blush with shaking hands, and the repair "
        "needs deliberate work. Notice what does NOT change: the blush "
        "still signals awareness, the audience still moves on, and the "
        "recovery still follows the same arc, only slower. This is why the "
        "low-intensity snapshot is a training ground: every small "
        "embarrassment successfully ridden - laughed off, owned, survived - "
        "is a rehearsal for the large ones. The nervous system learns from "
        "completed cycles. People who never let a small slip complete its "
        "cycle (by ruminating for hours over the wave-back) keep the gain "
        "high for everything; people who complete the cycle (laugh, file, "
        "move on) teach their system that peaks pass."),
    key_points=[
        "Same emotion, same person, same day: the difference between low and high intensity is the dials, not character.",
        "At low gain the appraisal is gentle and repair is instant; at high gain the appraisal is harsh and repair takes deliberate work.",
        "The mechanism never changes - the five beats run in both snapshots, only the gain differs.",
        "Small embarrassments ridden well are rehearsals: completed cycles teach the nervous system that peaks pass.",
        "The recovery tools are the same at both volumes; high intensity only asks for more patience.",
    ],
    requirements=[
        "Two concrete same-person snapshots, low and high",
        "The same-day framing for the character lesson",
        "The gain metaphor applied to all five beats",
        "The rehearsal principle: small cycles train the system",
        "Identical recovery tools at both volumes",
    ],
    standards=STD,
    citations=[CIT_MILLER, CIT_EDELMANN, CIT_KELTNER, CIT_LEARY, CIT_APA],
    sig_lens=(
        "In the Signature lens, the two snapshots are the soul at practice "
        "and at performance. Signal: low-gain slips are the training gym - "
        "every laughed-off wave-back is a rep. Repair: apply the 9:04 "
        "protocol at 2:15 - laugh, own, move on - just give it the longer "
        "clock the higher gain requires. Mastery: the person with a "
        "thousand completed small cycles meets the big one like an old "
        "sparring partner: respected, not feared.")),
dict(
    key="embarrassment_blend_anxiety", name="Embarrassment Mixed with Its Most Common Partner: Anxiety",
    group="Foundations", ladder_rank=8, ladder_tier="foundations",
    description=(
        "Embarrassment rarely travels alone; its most common companion is "
        "anxiety, and the pair has a distinct flavor. Pure embarrassment "
        "is retrospective - the slip already happened, the blush is the "
        "receipt. Add anxiety and the feeling gains a future tense: "
        "\"what if it happens again, what if they keep thinking about it, "
        "what if I walk in tomorrow and everyone remembers?\" The blend "
        "feels like a hot stone in the stomach that will not cool, because "
        "the embarrassment keeps supplying fresh footage and the anxiety "
        "keeps projecting it forward. The body shows both signatures at "
        "once: the blush of embarrassment plus the restless energy of "
        "anxiety - fidgeting, shallow breathing, scanning the room for "
        "reactions that are not there. The inner voice splits into two "
        "channels: the embarrassment channel replays the past (\"I cannot "
        "believe I said that\"), the anxiety channel previews the future "
        "(\"tomorrow will be awful\"). The blend is stickier than either "
        "feeling alone, because each feeds the other: anxiety makes the "
        "next social moment feel dangerous, which makes the person act "
        "stiffly, which creates fresh material for embarrassment. The way "
        "out is to address the two channels separately: cool the past with "
        "repair and reality-checking, cool the future with preparation and "
        "exposure to the feared moment in small doses."),
    how_it_works=(
        "Blends work by sharing machinery. Embarrassment and anxiety both "
        "run on the social-threat system - the brain's radar for \"how am I "
        "being seen?\" - so they combine without friction, like two "
        "instruments playing the same note in different octaves. "
        "Embarrassment occupies the present-past (the slip, the blush); "
        "anxiety occupies the future (the dreaded repeat). Together they "
        "cover all of time, which is why the blend feels inescapable: there "
        "is no tense left to rest in. The treatment follows from the "
        "structure. First, separate the tenses: name what belongs to the "
        "past (the actual slip, which is over and repairable) and what "
        "belongs to the future (the feared repeat, which has not happened). "
        "Second, give each tense its own tool: the past gets repair (apology "
        "made, joke owned, lesson filed) and the spotlight reality-check; "
        "the future gets preparation (rehearse the next encounter) and "
        "graded exposure (walk in, stay, notice nothing happens). The blend "
        "dissolves when the tenses are unmixed - and that unmixing is a "
        "skill, not a personality trait."),
    key_points=[
        "Embarrassment's most common partner is anxiety: the past-tense slip plus the future-tense dread of a repeat.",
        "The blend feels inescapable because together the two feelings cover all of time - no tense left to rest in.",
        "The body shows both signatures: the blush plus restless fidgeting and shallow breathing.",
        "The inner voice splits: one channel replays the slip, the other previews tomorrow.",
        "The way out is to unmix the tenses: repair the past, prepare for the future, separately.",
    ],
    requirements=[
        "The tense distinction: past vs future",
        "Both body signatures described together",
        "The split inner voice",
        "The feedback loop: anxiety stiffens behavior, creating new embarrassment material",
        "The unmixing method: separate tools for separate tenses",
    ],
    standards=STD,
    citations=[CIT_MILLER, CIT_EDELMANN, CIT_LEARY, CIT_KELTNER, CIT_APA],
    sig_lens=(
        "In the Signature lens, the blend is the belonging-meter stuck on "
        "scan - checking the past and the future at once, finding static "
        "in both. Signal: the stickiness is information about caring, not "
        "evidence of brokenness. Repair: unmix the tenses deliberately - "
        "write the past's repair on paper, write the future's preparation "
        "beside it, and let each channel close. Mastery: the person who can "
        "name which tense is talking stops being ruled by either.")),
dict(
    key="embarrassment_day_vignette", name="A Day in the Life: Embarrassment Running Through an Ordinary Day",
    group="Foundations", ladder_rank=9, ladder_tier="foundations",
    description=(
        "6:40 AM: Dev opens his front door and realizes his shirt is inside "
        "out - the delivery driver has already seen it. A half-blush, a "
        "laugh, shirt fixed; the day's first tiny cycle completes before "
        "coffee. 8:15 AM: on the team call he says \"you too\" when the "
        "manager says \"happy birthday to my daughter.\" The chat fills "
        "with laughing emojis. Dev's ears burn through his headphones, but "
        "he types \"new company policy: everyone gets birthday wishes\" and "
        "the room laughs with him. 12:30 PM: he waves at a stranger he "
        "mistook for his cousin across the cafeteria. Low heat, quick grin, "
        "filed and forgotten. 3:00 PM: the big one - he calls the new client "
        "by the old client's name, twice, in the pitch meeting. The blush "
        "is a flood; he corrects himself, apologizes once, cleanly, and "
        "moves on, though his hands shake for ten minutes. 7:00 PM: at "
        "dinner he tells the story of the pitch meeting himself, before "
        "anyone else can. His friends laugh; he laughs hardest. 11:00 PM: "
        "in bed, the pitch meeting replays once. He runs the reality check "
        "- the client signed off on the next step an hour later - and lets "
        "it go. Five embarrassments, one ordinary day, zero damage. The "
        "vignette shows the database's whole arc in miniature: slips are "
        "constant, recovery is a skill, and the people who tell the story "
        "first own it."),
    how_it_works=(
        "The day works as a teaching tool because it compresses the full "
        "ladder into twelve hours. The morning slips demonstrate low volume "
        "and completed cycles - the shirt, the birthday, the wave - each "
        "closed with a laugh and filed away, each one a rehearsal rep for "
        "the nervous system. The afternoon pitch meeting demonstrates high "
        "volume: same mechanism, higher dials, recovery by the book - one "
        "clean apology, no groveling, keep going. The evening demonstrates "
        "the master move: telling the story first, which converts the "
        "aftershock's raw material (the replay) into social currency (the "
        "funny story). This is the deep principle of the vignette: "
        "embarrassment's power comes from secrecy and surprise - \"nobody "
        "can know\" and \"it came from nowhere.\" Owning the story removes "
        "both. The replay at bedtime demonstrates the aftershock handled "
        "correctly: noticed, reality-checked against evidence (the client "
        "signed off), released. A day like Dev's is not a bad day; it is a "
        "well-managed one. Frequency of slips is not the variable - "
        "completion of cycles is."),
    key_points=[
        "An ordinary day holds five embarrassments: slips are constant, damage is optional.",
        "Small completed cycles in the morning are rehearsal reps for the big one in the afternoon.",
        "The master move is telling the story first - converting replay material into social currency.",
        "One clean apology beats three groveling ones; keep going is the recovery.",
        "Frequency of slips is not the variable - completion of cycles is.",
    ],
    requirements=[
        "A full-day timeline with at least five moments",
        "Low and high volumes in the same day",
        "The tell-it-first master move",
        "The bedtime aftershock handled correctly",
        "The closing principle: completion over frequency",
    ],
    standards=STD,
    citations=[CIT_MILLER, CIT_GOFFMAN, CIT_KELTNER, CIT_EDELMANN, CIT_APA],
    sig_lens=(
        "In the Signature lens, Dev's day is the belonging workout: five "
        "reps, five completions, strength gained. Signal: a day full of "
        "slips is a day fully lived in public - the hermit never blushes. "
        "Repair: the evening retelling is the master craft - whoever tells "
        "the story first sets its meaning. Mastery: the person who ends the "
        "day with stories instead of replays has turned exposure into "
        "belonging.")),

# ---------------------------------------------------- 10-13: body signals
dict(
    key="embarrassment_body", name="What Happens in the Body: The Physiology of Embarrassment",
    group="Foundations", ladder_rank=10, ladder_tier="foundations",
    description=(
        "Embarrassment is one of the most physical emotions there is - it "
        "announces itself in the body before the mind has finished its "
        "sentence. The headline act is the blush: blood vessels in the face, "
        "ears, and neck widen, flooding the skin with warm blood. Unlike "
        "most emotional responses, the blush is involuntary and essentially "
        "unfakeable - you cannot blush on command, and you cannot stop one "
        "once it starts. The heart joins in, beating faster and harder, "
        "sometimes pounding audibly in the person's own ears. Breathing "
        "turns shallow and quick; some people feel they cannot get a full "
        "breath until the moment passes. Muscles tense, especially in the "
        "shoulders, neck, and jaw - the body bracing as if for a blow that "
        "never comes. The stomach may churn or drop; the hands may tremble "
        "or grow damp. Skin prickles with heat, and many people report a "
        "tingling scalp, as if every hair were listening. Energy spikes and "
        "then drains: the arousal surge is followed by a tired, wrung-out "
        "feeling once the peak passes. All of this is the body's ancient "
        "alarm system doing its job - mobilizing for a social threat the "
        "same way it mobilizes for a physical one, even though the threat "
        "is only an image."),
    how_it_works=(
        "The physiology runs on the sympathetic nervous system - the same "
        "fight-or-flight machinery behind fear and anger - but embarrassment "
        "adds a unique vascular signature. The blush comes from the "
        "widening of small blood vessels under facial skin, driven by "
        "adrenaline and by a quirk of human anatomy: the face and neck have "
        "an unusually dense network of these vessels, and humans, uniquely "
        "among primates, have visible skin that shows the change. That "
        "visibility is not an accident; researchers argue the blush evolved "
        "precisely because it can be seen - an involuntary, unfakeable "
        "signal of awareness that tells witnesses \"I know I slipped, and I "
        "care.\" The rest of the cascade follows the standard arousal "
        "script: heart rate up, breathing shallow, muscles tense, digestion "
        "paused (hence the churning stomach), sweat glands active (hence "
        "damp hands). The energy drain afterward is the parasympathetic "
        "rebound - the body's calm-down system overshooting slightly as it "
        "restores baseline. Understanding the machinery demystifies the "
        "feeling: the heat is blood, the pounding is the heart doing its "
        "job, and none of it is dangerous. It is also why physical tools "
        "work fastest in the first minute - slow breathing and unclenching "
        "speak directly to the system that is actually running the show."),
    key_points=[
        "The blush is involuntary and unfakeable - widening blood vessels in the face, ears, and neck, driven by adrenaline.",
        "The full cascade is sympathetic arousal: fast heart, shallow breath, tense muscles, churning stomach, damp hands.",
        "Humans are uniquely built to show the blush - visible skin over dense facial vessels, likely evolved as an honest signal.",
        "The wrung-out feeling afterward is the parasympathetic rebound restoring baseline.",
        "Physical tools work fastest in the first minute because they speak to the system actually running the show.",
    ],
    requirements=[
        "The blush mechanism explained plainly",
        "Full-body cascade: heart, breath, muscles, stomach, skin, energy",
        "The evolutionary signaling argument",
        "The rebound explained",
        "Why physical tools work first",
    ],
    standards=STD,
    citations=[CIT_DARWIN, CIT_KELTNER, CIT_MILLER, CIT_EDELMANN, CIT_APA],
    sig_lens=(
        "In the Signature lens, the body is the soul's broadcast tower, "
        "and the blush is its honest flag. Signal: every physical symptom "
        "is the tower working - heat means blood, pounding means heart, "
        "none of it is damage. Repair: thank the tower instead of cursing "
        "it - breathe with it, unclench with it, let the minute pass. "
        "Mastery: the person who knows their own broadcast pattern stops "
        "being surprised by the transmission and starts reading it like "
        "weather.")),
dict(
    key="embarrassment_posture", name="Posture and Movement: How the Body Carries Embarrassment",
    group="Foundations", ladder_rank=11, ladder_tier="foundations",
    description=(
        "Watch a person in the grip of embarrassment and the body tells the "
        "story before the mouth opens. The signature posture is the shrink: "
        "shoulders roll forward and in, the chest caves slightly, the head "
        "drops and often turns aside, the whole frame trying to occupy less "
        "space. It is the physical opposite of pride's expansion - where "
        "pride puffs up, embarrassment folds down. The hands get busy: "
        "covering the mouth or face, touching the neck or hair, fidgeting "
        "with sleeves, pockets, or objects - self-touch that soothes the "
        "nervous system the way a child hugs a blanket. The gaze drops or "
        "darts; sustained eye contact becomes nearly impossible, as if "
        "looking at witnesses would confirm what they saw. Movement turns "
        "either jerky or frozen: some people rush - hurrying past the scene, "
        "talking fast to fill the silence - while others lock up entirely, "
        "rooted to the spot in the worst possible place. The smile, when it "
        "comes, is the nervous grin: tight, brief, often paired with a "
        "downward glance. Researchers have cataloged this as the "
        "embarrassment display - gaze down, head turn, controlled smile, "
        "face touch - and found it remarkably consistent across cultures, "
        "because the body is broadcasting the same message everywhere: \"I "
        "know, I care, please let me stay.\""),
    how_it_works=(
        "The posture is not random; it is a negotiation. Every element of "
        "the embarrassment display manages the same problem: how to stay in "
        "the group while the group's attention is painfully fixed on you. "
        "Shrinking reduces the target - less of you to look at. Gaze aversion "
        "breaks the feedback loop - if you cannot see them seeing you, the "
        "spotlight dims. The nervous smile and face touch are appeasement "
        "signals, the human equivalent of a dog rolling over: they tell "
        "witnesses \"no threat here, I submit to the norm.\" The freeze-or-"
        "rush split reflects the two ancient options for a caught animal: "
        "play dead or bolt. None of this is chosen; it runs below conscious "
        "control, which is why trying to \"act natural\" during embarrassment "
        "usually fails - the display leaks through deliberate performance. "
        "The practical insight is counterintuitive: because the display is "
        "an appeasement signal, letting it happen briefly actually speeds "
        "recovery. Witnesses read the shrink-and-smile as awareness and "
        "respond with sympathy; fighting it - standing rigid, forcing eye "
        "contact - reads as defiance or coldness and slows the repair. The "
        "body knows the diplomacy; the skill is to let it finish the "
        "handshake."),
    key_points=[
        "The signature posture is the shrink: shoulders in, chest caved, head dropped - the physical opposite of pride.",
        "The hands self-soothe: face covering, neck touching, fidgeting - the adult version of hugging a blanket.",
        "Gaze drops or darts because seeing witnesses seeing you feeds the spotlight.",
        "The display - gaze down, head turn, controlled smile, face touch - is consistent across cultures.",
        "Letting the brief display happen speeds recovery; witnesses read it as awareness and respond with sympathy.",
    ],
    requirements=[
        "The shrink described as pride's opposite",
        "Hands, gaze, and movement covered",
        "The nervous grin identified",
        "The cross-cultural consistency noted",
        "The counterintuitive insight: let the display finish",
    ],
    standards=STD,
    citations=[CIT_KELTNER, CIT_DARWIN, CIT_GOFFMAN_IR, CIT_MODIGLIANI, CIT_APA],
    sig_lens=(
        "In the Signature lens, the shrink is the soul bowing - not broken, "
        "bowing - the oldest gesture of staying in the circle. Signal: the "
        "fold is diplomacy, not defeat; it says \"I value this group enough "
        "to bend.\" Repair: let the bow complete - a brief, honest fold "
        "followed by rising again. Mastery: the person who can fold and "
        "rise in one motion has learned the deepest social craft - humility "
        "with a spine.")),
dict(
    key="embarrassment_sleep_appetite", name="Sleep, Appetite, and Energy: Embarrassment's Quiet After-Effects",
    group="Foundations", ladder_rank=12, ladder_tier="foundations",
    description=(
        "A single embarrassment rarely touches sleep or appetite - the "
        "feeling is too brief. But embarrassment has a long tail when it "
        "repeats, and the tail reaches the quiet systems. The aftershock "
        "replay loop is the bridge: a person who replays a lunchtime slip at "
        "11 PM is running social-threat appraisal in bed, and the body "
        "cannot tell a remembered audience from a real one - heart rate "
        "rises, muscles tense, sleep onset delays. Do this for several "
        "nights around a big event (a botched presentation, a public "
        "mistake) and the pattern looks like mild insomnia: trouble falling "
        "asleep, thin sleep, waking with the replay already running. "
        "Appetite responds to the arousal too: some people lose their "
        "appetite entirely in the hours after a strong embarrassment - the "
        "churning stomach and paused digestion of the arousal cascade - "
        "while others eat for soothing later, seeking comfort food to close "
        "the emotional loop. Energy follows the spike-and-drain curve: the "
        "arousal surge burns fuel, and the rebound leaves a flat, wrung-out "
        "tiredness that is not sleepiness but depletion. The reassuring fact "
        "is proportionality: these effects scale with the aftershock, not "
        "the event. Shorten the replay loop and the quiet systems settle on "
        "their own - no special regimen required, just a closed loop."),
    how_it_works=(
        "The mechanism is the replay loop's hijacking of rest systems. Sleep "
        "requires the threat system to stand down; replaying a social threat "
        "keeps it on duty. The body responds to imagined audiences with a "
        "fraction of the real response - enough to delay sleep, not enough "
        "to feel like a full emotion - which is why the effect is subtle "
        "and often misattributed (\"I am just a bad sleeper this week\"). "
        "Appetite effects run through the same arousal channel: sympathetic "
        "activation suppresses digestion (stomach churn, no hunger), and the "
        "later rebound can swing the other way as the body seeks quick fuel "
        "and soothing. Energy depletion is the cost of the surge - arousal "
        "is metabolically expensive, and a day of repeated embarrassment "
        "cycles spends real fuel. The intervention point is always the loop, "
        "never the stomach or the bed: close the embarrassment cycle with a "
        "decisive repair (apology made, lesson filed, story told first), run "
        "the spotlight reality-check on the replay, and schedule a "
        "\"worry window\" earlier in the evening so the replay has a "
        "contained time to run. When the loop closes, sleep, appetite, and "
        "energy restore themselves - they were never broken, only borrowed."),
    key_points=[
        "One embarrassment rarely touches sleep; repeated replays do - the body cannot tell a remembered audience from a real one.",
        "The replay loop at bedtime delays sleep onset and thins sleep; the effect is often misattributed.",
        "Appetite swings both ways: suppressed during arousal, comfort-seeking during the rebound.",
        "Energy follows spike-and-drain: arousal is metabolically expensive, and repeated cycles spend real fuel.",
        "The intervention point is always the loop - close the cycle and the quiet systems settle on their own.",
    ],
    requirements=[
        "Sleep effects traced to the replay loop",
        "Both appetite directions explained",
        "The energy curve: spike and drain",
        "The misattribution warning",
        "The loop-closing intervention",
    ],
    standards=STD,
    citations=[CIT_EDELMANN, CIT_MILLER, CIT_LEARY, CIT_APA, CIT_KELTNER],
    sig_lens=(
        "In the Signature lens, the quiet systems are the soul's night "
        "shift - they keep working the belonging-books after hours. Signal: "
        "restless sleep after a slip is not insomnia, it is an unclosed "
        "loop asking for its paperwork. Repair: give the loop its "
        "paperwork - the repair made, the lesson filed, the story told - and "
        "the night shift clocks out. Mastery: the person who closes loops "
        "by dinner sleeps like the audience already left, because it has.")),
dict(
    key="embarrassment_individual_differences", name="No Two Bodies React Identically: How Embarrassment Differs Between People",
    group="Foundations", ladder_rank=13, ladder_tier="foundations",
    description=(
        "Embarrassment is universal, but its volume and flavor vary "
        "dramatically from person to person. Researchers describe "
        "embarrassability - the trait of how readily and strongly a person "
        "embarrasses - and it runs on a wide spectrum. At one end are "
        "people who blush at a compliment; at the other, people who can "
        "trip on stage, bow, and keep going with barely a flush. The "
        "differences come from several sources. Temperament sets the "
        "baseline: reactive nervous systems arouse faster and cool slower. "
        "Self-focus sets the gain: people who habitually monitor how they "
        "appear turn the social radar up, catching more slips. Culture sets "
        "the norms: what counts as a slip varies enormously - some cultures "
        "treat public praise as embarrassing, others treat silence as the "
        "slip. Personal history sets the triggers: the person once mocked "
        "for their laugh will guard their laugh for decades. Age shifts the "
        "curve: embarrassability typically peaks in adolescence, when the "
        "imagined audience is loudest and the self is newest, then settles "
        "as identity stabilizes. Even the display differs: some people blush "
        "vividly but recover in seconds; others barely flush but replay for "
        "days. None of these positions is a diagnosis or a defect - they are "
        "settings on a normal human instrument, and every setting can learn "
        "the recovery skills in this database."),
    how_it_works=(
        "Think of embarrassability as an equalizer with five sliders. "
        "Slider one, physiological reactivity: how fast your arousal system "
        "fires and how slowly it clears - largely temperamental, stable "
        "across life. Slider two, public self-focus: how much of your "
        "attention habitually sits on \"how do I look right now\" - "
        "trainable downward with practice. Slider three, norm strictness: "
        "how narrow your culture's and family's rules for acceptable "
        "behavior are - the stricter the rules, the more events count as "
        "slips. Slider four, history weight: how many past embarrassments "
        "are still unclosed, each one adding gain to similar situations. "
        "Slider five, audience calibration: how accurately you estimate what "
        "witnesses actually notice - most people overestimate, and the "
        "overestimation is correctable. The equalizer model matters because "
        "it replaces the single cruel question (\"what is wrong with me?\") "
        "with five adjustable ones. You cannot change your temperament much, "
        "but you can retrain attention, update old rules, close old loops, "
        "and recalibrate the audience estimate. Two people can feel "
        "completely different embarrassments at the same event and both be "
        "entirely normal - the event is shared, the equalizers are not."),
    key_points=[
        "Embarrassability is a trait on a wide spectrum - from blushing at a compliment to bowing after a stage trip.",
        "Five sliders set it: physiological reactivity, public self-focus, norm strictness, history weight, and audience calibration.",
        "Culture decides what counts as a slip; adolescence is the typical peak of the curve.",
        "The display differs too: vivid blushers may recover fast while non-blushers replay for days.",
        "The equalizer replaces one cruel question with five adjustable ones - every setting can learn recovery.",
    ],
    requirements=[
        "Embarrassability defined as a spectrum",
        "The five sliders named and explained",
        "Culture and age effects",
        "The display-vs-recovery distinction",
        "The reframing: settings, not defects",
    ],
    standards=STD,
    citations=[CIT_MILLER, CIT_EDELMANN, CIT_LEARY, CIT_KELTNER, CIT_APA],
    sig_lens=(
        "In the Signature lens, the equalizer is the soul's custom "
        "belonging-instrument - no two are tuned alike, and none is out of "
        "tune. Signal: your settings are information about your history "
        "and wiring, never a verdict. Repair: adjust the sliders you can "
        "reach - attention, old rules, old loops, audience estimates - and "
        "honor the ones you cannot. Mastery: the person who knows their own "
        "equalizer stops comparing their blush to someone else's bow.")),

# -------------------------------------- 14-17: facial expression (compounded)
dict(
    key="embarrassment_face", name="The Face of Embarrassment: Eyes, Brows, Mouth, and Micro-Signs",
    group="Compounded", ladder_rank=14, ladder_tier="compounded",
    description=(
        "The embarrassed face is one of the most recognizable expressions in "
        "the human repertoire, and researchers have mapped it precisely. The "
        "eyes go first: gaze drops downward or slides away to the side, and "
        "the eyelids lower - the face literally trying to reduce its own "
        "visibility. The brows may lift briefly in the middle, a flash of "
        "the appeasement brow. The mouth forms the signature: a controlled, "
        "pressed smile - lips pressed together or stretched thin, often "
        "pulled to one side - the \"embarrassment smile\" that is visibly "
        "different from a joy smile because the eyes do not join it. Then "
        "the blush blooms across the cheeks, sometimes spreading to the "
        "ears, neck, and upper chest. The head tilts down and often turns "
        "slightly away; a hand may rise to touch the face, mouth, or neck. "
        "The micro-signs complete the picture: a quick lip press or lip "
        "lick, a single sharp exhale or nervous laugh, a swallow. What makes "
        "the expression remarkable is its honesty: because the blush and the "
        "gaze aversion are involuntary, the face cannot lie about "
        "embarrassment the way it can fake a smile. Witnesses read the whole "
        "display in under a second, and - crucially - they read it as "
        "awareness and goodwill, not as guilt or weakness."),
    how_it_works=(
        "The face works as a billboard because every element solves part of "
        "the social problem. Gaze aversion reduces incoming information - "
        "you cannot watch them watching you - which damps the spotlight "
        "loop. The head-down posture shrinks the visible face, the same "
        "logic as the body shrink. The pressed smile is the key innovation: "
        "it borrows the smile's friendly signal while withholding the "
        "enjoyment signal, producing a display that says \"I am with you\" "
        "without saying \"I am happy about this.\" The blush is the "
        "unfakeable seal of authenticity - because it cannot be produced "
        "voluntarily, its presence certifies that the rest of the display "
        "is genuine. This is why the embarrassed face works as appeasement: "
        "witnesses unconsciously run the logic \"involuntary signal means "
        "real awareness; real awareness means they respect the norm; norm-"
        "respecters are safe to keep around.\" The face is doing diplomacy "
        "at a speed and honesty that words cannot match - which is also why "
        "trying to arrange your face during embarrassment usually backfires: "
        "the billboard is already broadcasting, and fighting it only adds a "
        "second, stranger signal on top."),
    key_points=[
        "The mapped display: gaze down or away, lowered lids, pressed thin smile, blush, head tilt, face touch.",
        "The embarrassment smile differs from joy: the mouth smiles while the eyes do not join it.",
        "The blush is the unfakeable seal - involuntary, so its presence certifies the display is genuine.",
        "Micro-signs: lip press, quick exhale or nervous laugh, swallow, single-sided mouth pull.",
        "Witnesses read it in under a second as awareness and goodwill - the face does diplomacy faster than words.",
    ],
    requirements=[
        "Each facial region described: eyes, brows, mouth",
        "The embarrassment smile vs joy smile contrast",
        "The blush as authenticity seal",
        "Micro-signs listed",
        "The witness-reading speed and meaning",
    ],
    standards=STD,
    citations=[CIT_KELTNER, CIT_DARWIN, CIT_MODIGLIANI, CIT_GOFFMAN_IR, CIT_APA],
    sig_lens=(
        "In the Signature lens, the face is the soul's honest billboard - "
        "and embarrassment is the one ad it cannot take down. Signal: the "
        "billboard's honesty is your asset, not your exposure; it is doing "
        "the apologizing before your mouth finds the words. Repair: let the "
        "billboard run its thirty seconds - the pressed smile, the glance "
        "away - instead of plastering a fake calm over it. Mastery: the "
        "person who trusts their face stops performing and starts "
        "communicating.")),
dict(
    key="embarrassment_face_intensity", name="How the Expression Changes with Intensity",
    group="Compounded", ladder_rank=15, ladder_tier="compounded",
    description=(
        "The embarrassed face is not one mask but a gradient, and each "
        "level adds elements. At low intensity, the display is minimal: a "
        "brief downward glance, the corners of the mouth tightening for a "
        "second, a faint warming of the cheeks that only the person feels. "
        "To a witness it may read as nothing more than a shy smile. At "
        "moderate intensity, the full display assembles: sustained gaze "
        "aversion, the pressed smile held for several seconds, a visible "
        "blush spreading across cheeks and ears, the head turning aside, a "
        "hand rising to the mouth or neck, the nervous laugh escaping. The "
        "witness cannot miss it - and that visibility is the point, the "
        "appeasement working at full strength. At high intensity, the "
        "display overflows its bounds: the blush deepens to the neck and "
        "chest, the hands may cover the whole face, the body turns fully "
        "away or crouches, laughter becomes uncontrolled or flips into "
        "tears of overwhelm, speech fragments into false starts. At this "
        "level the display stops being purely appeasing and starts "
        "broadcasting distress, which is why witnesses at high intensity "
        "shift from amusement to concern and often intervene - changing the "
        "subject, offering an exit. Reading the gradient matters because "
        "the right response changes with it: low needs nothing, moderate "
        "needs a laugh-with, high needs a rescue."),
    how_it_works=(
        "The gradient reflects arousal dose. Low arousal activates only the "
        "cheapest, fastest components - eye and mouth muscles, a whisper of "
        "vasodilation - because the system is metering its response to the "
        "threat level. As arousal climbs, the system recruits more "
        "components in a fixed order: gaze, then mouth, then blush, then "
        "head, then hands, then whole-body orientation. This fixed "
        "recruitment order is why the expression is so readable - witnesses "
        "unconsciously count the components to gauge the intensity, the way "
        "you count alarm bells to gauge a fire. At the top of the gradient, "
        "a phase change occurs: the display switches from appeasement "
        "(\"I know, I care\") to distress signaling (\"I am overwhelmed\"), "
        "and the audience's program switches with it, from amusement to "
        "care. This switch is deeply useful to know. If you are the "
        "embarrassed person at high intensity, the kindest thing you can do "
        "for yourself is accept the rescue - let someone change the subject, "
        "take the offered exit. If you are the witness, the component count "
        "tells you which program to run: smile-with for the mid-gradient, "
        "rescue for the top."),
    key_points=[
        "The display is a gradient: low adds only glance and mouth-tightening; moderate assembles the full display; high overflows into distress.",
        "Components recruit in a fixed order - gaze, mouth, blush, head, hands, body - which is why witnesses read intensity unconsciously.",
        "At the top of the gradient a phase change occurs: appeasement flips to distress signaling.",
        "The audience's program flips with it: amusement becomes concern, and witnesses offer rescue.",
        "The right response follows the gradient: low needs nothing, moderate needs a laugh-with, high needs a rescue.",
    ],
    requirements=[
        "Three gradient levels with component lists",
        "The fixed recruitment order explained",
        "The appeasement-to-distress phase change",
        "The witness program flip",
        "Response guidance per level",
    ],
    standards=STD,
    citations=[CIT_KELTNER, CIT_DARWIN, CIT_MILLER, CIT_MODIGLIANI, CIT_APA],
    sig_lens=(
        "In the Signature lens, the gradient is the soul's volume meter "
        "made visible - each added component is another decibel of caring. "
        "Signal: count your own components and you will know your level "
        "without guessing. Repair: match the response to the level - ride "
        "the low, laugh the middle, accept rescue at the top. Mastery: the "
        "person who can read their own gradient stops either minimizing or "
        "catastrophizing and simply meets the moment at its true size.")),
dict(
    key="embarrassment_hiding_faking", name="Hiding It, Faking It: What Leaks Through",
    group="Compounded", ladder_rank=16, ladder_tier="compounded",
    description=(
        "People try to hide embarrassment constantly - and the attempt "
        "itself is one of the most reliable tells. The hiding strategies "
        "are familiar: the forced casual face, the sudden busy-ness (phone "
        "checked, papers shuffled), the over-loud laugh meant to signal "
        "\"I am fine,\" the quick subject change, the deadpan \"anyway.\" "
        "What leaks through is the involuntary layer: the blush cannot be "
        "suppressed, the gaze keeps dropping no matter how the mouth is "
        "arranged, the voice climbs half an octave or thins, the hands keep "
        "finding the face. Researchers call this leakage, and embarrassment "
        "leaks more than most emotions because its core signal - the blush - "
        "is autonomic. Faking embarrassment is the mirror problem: the "
        "performed \"oh, how embarrassing\" with the hand to the forehead. "
        "It fails for the same reason hiding fails - the voluntary "
        "components (the gesture, the words) are present but the involuntary "
        "ones (the blush, the genuine gaze aversion) are absent, and "
        "witnesses feel the gap without knowing why. The performed version "
        "reads as theater; the suppressed version reads as tension. Both "
        "miss the mark that the genuine display hits effortlessly. The "
        "lesson is not that control is impossible - the voluntary layer can "
        "be managed, and recovery can be graceful - but that the honest "
        "signal underneath is doing the real social work, and cooperating "
        "with it beats fighting it."),
    how_it_works=(
        "Leakage happens because the face has two control systems that do "
        "not fully overlap. The voluntary system drives the big, deliberate "
        "movements - the arranged smile, the held gaze, the spoken words. "
        "The involuntary system drives the autonomic layer - blush, pupil "
        "changes, micro-timing of the glance, vocal pitch under stress. "
        "Embarrassment is unusual in how much of its display lives in the "
        "involuntary system, which is why it is the hardest emotion to hide "
        "and the hardest to fake. Hiding fails asymmetrically: you can "
        "suppress the mouth, but the cheeks still bloom; you can hold the "
        "gaze, but the blink rate and pitch betray you. Witnesses do not "
        "analyze this consciously - they simply feel that something is "
        "\"off,\" which often reads worse than the embarrassment itself "
        "would have. This creates the hiding paradox: the effort to look "
        "unembarrassed makes a person look less trustworthy than the blush "
        "would have. The practical craft is therefore selective: manage "
        "what is manageable (breathe, unclench, choose your words), and let "
        "the involuntary layer do its honest work. A visible blush plus "
        "composed words is the strongest combination - the body certifies "
        "awareness while the mouth demonstrates control."),
    key_points=[
        "Hiding strategies - forced casualness, sudden busy-ness, the over-loud laugh - are themselves reliable tells.",
        "What leaks is the involuntary layer: the blush, the dropping gaze, the climbing voice, the face-seeking hands.",
        "Faking fails in reverse: voluntary gestures present, involuntary signals absent, and witnesses feel the gap.",
        "The hiding paradox: effort to look unembarrassed often reads worse than the blush would have.",
        "The strongest combination is visible blush plus composed words - honesty certified, control demonstrated.",
    ],
    requirements=[
        "Common hiding strategies listed",
        "The leakage mechanism: two control systems",
        "Faking analyzed as the mirror failure",
        "The hiding paradox stated",
        "The practical craft: manage the voluntary, allow the involuntary",
    ],
    standards=STD,
    citations=[CIT_KELTNER, CIT_DARWIN, CIT_MODIGLIANI, CIT_MILLER, CIT_APA],
    sig_lens=(
        "In the Signature lens, hiding is the soul trying to take down its "
        "own honest billboard - and the billboard always wins. Signal: the "
        "leak is loyalty; your involuntary system refuses to lie about "
        "caring. Repair: stop fighting the blush and start directing the "
        "words - the body handles the honesty, you handle the grace. "
        "Mastery: the person who lets the leak happen and speaks calmly "
        "through it is more believed than any performer.")),
dict(
    key="embarrassment_expression_gallery", name="Expression Gallery Notes: Drawing and Playing Embarrassment",
    group="Compounded", ladder_rank=17, ladder_tier="compounded",
    description=(
        "For the artist: draw the head at a three-quarter turn, chin tucked "
        "a fraction down, eyes looking down and to the side - never meeting "
        "the viewer's gaze. The mouth is the critical line: press the lips "
        "into a thin, slightly crooked line, one corner tugged higher than "
        "the other, the classic nervous half-smile. Shade the blush as a "
        "soft wash across the cheekbones, deepening toward the ears - not a "
        "cartoon red circle but a diffuse warmth, strongest high on the "
        "cheek. Add the hand: fingers lightly touching the mouth corner, or "
        "one hand at the back of the neck, elbow tucked in. The shoulders "
        "rise and roll forward; the whole figure narrows. For the actor: "
        "start with the breath - take the line, then let a short exhale "
        "escape through the nose as the realization lands. Drop the gaze "
        "on the key word, not before; let the smile arrive half a beat "
        "late, as if the face negotiated with itself. Touch your neck or "
        "mouth once, briefly - the gesture reads as truth only if it is "
        "quick and unrepeated. Let the voice rise slightly and speed up, "
        "then catch it and slow down for the recovery line. The laugh, if "
        "there is one, should be one short burst, not a run. The difference "
        "between playing embarrassment and playing shame is the recovery "
        "arc: embarrassment's face is already looking for the way back - "
        "the glance that checks whether the audience is smiling too. Play "
        "that checking glance and the audience will forgive the character "
        "anything."),
    how_it_works=(
        "These notes work because they translate the researched display "
        "into craft decisions. Every instruction maps to a component of the "
        "real expression: the averted gaze to the spotlight-damping, the "
        "pressed crooked smile to the appeasement display, the diffuse blush "
        "wash to the vascular reality, the single face-touch to the "
        "self-soothing gesture, the narrowed shoulders to the shrink. The "
        "timing notes matter most: real embarrassment has a choreography - "
        "the realization beat, the display beat, the checking glance, the "
        "recovery beat - and performances that skip the checking glance "
        "read as shame (no hope of return) while performances that skip the "
        "realization beat read as mere shyness. The actor's breath note is "
        "physiology: the short nasal exhale is the body's actual response "
        "to the arousal spike, and reproducing it triggers a whisper of the "
        "real feeling, which then plays the face from the inside. The "
        "artist's blush note corrects the common error of painting "
        "embarrassment as anger's red: embarrassment's warmth is diffuse "
        "and high on the cheek, anger's is concentrated and low. Details "
        "like these are what let a drawing or a performance read as true "
        "rather than indicated."),
    key_points=[
        "Artist: three-quarter head, tucked chin, averted eyes, thin crooked pressed smile, diffuse blush wash high on the cheek, one quick face-touch, narrowed shoulders.",
        "Actor: the breath-led realization beat, the half-beat-late smile, the single neck-touch, the checking glance.",
        "The choreography has four beats: realization, display, checking glance, recovery - skip one and it reads as a different emotion.",
        "Embarrassment's red is diffuse and high; anger's is concentrated and low - paint them differently.",
        "The checking glance is the soul of the performance: the face already looking for the way back.",
    ],
    requirements=[
        "Concrete drawing instructions for head, eyes, mouth, blush, hand, shoulders",
        "Concrete acting instructions for breath, gaze timing, gesture, voice, laugh",
        "The four-beat choreography named",
        "Embarrassment vs shame vs shyness distinguished for performers",
        "The blush-vs-anger painting correction",
    ],
    standards=STD,
    citations=[CIT_KELTNER, CIT_DARWIN, CIT_GOFFMAN_IR, CIT_MODIGLIANI, CIT_APA],
    sig_lens=(
        "In the Signature lens, the gallery notes are the soul's stage "
        "directions - the honest choreography of a feeling that cannot lie. "
        "Signal: every true detail (the late smile, the checking glance) "
        "is the belonging instinct made visible. Repair: for the performer "
        "of life, not just the actor - borrow the choreography: realize, "
        "display briefly, check the room, recover. Mastery: the person who "
        "knows the four beats can walk any stage, because they know exactly "
        "where the scene ends.")),
# ------------------------------------------------------ 18-21: triggers
dict(
    key="embarrassment_classic_triggers", name="The Classic Triggers: What Commonly Sets It Off",
    group="Compounded", ladder_rank=18, ladder_tier="compounded",
    description=(
        "The classic triggers of embarrassment form a recognizable parade. "
        "Bodily slips lead it: tripping, stumbling, spilling food or drink "
        "on yourself, loud stomach growls in quiet rooms, sneezing attacks, "
        "clothing malfunctions - the body misbehaving in public. Verbal "
        "slips march next: calling someone by the wrong name, the \"you "
        "too\" reply to \"happy birthday,\" mispronouncing a common word, "
        "saying the quiet part out loud, the joke that lands wrong. "
        "Competence slips follow: blanking on a name you should know, "
        "fumbling with simple technology in front of an audience, getting "
        "lost while leading the way, the presentation typo projected "
        "ten feet tall. Exposure triggers: being caught singing, dancing, "
        "or talking to yourself; the private message sent to the group; "
        "the browser history glimpsed; walking in on something or being "
        "walked in on. Status slips: being corrected publicly, praised "
        "excessively in front of peers, crying in a professional setting, "
        "needing help with something \"everyone\" can do. What unites them "
        "all is the formula: a norm (graceful, competent, composed, "
        "private) plus a visible miss plus witnesses. Learn the parade and "
        "you can spot a trigger forming a second early - and that second is "
        "often enough to choose the recovery before the feeling chooses it "
        "for you."),
    how_it_works=(
        "Triggers work through the appraisal beat of the five-beat "
        "sequence: the mind matches the event against its library of norms "
        "and flags the mismatch. The classic triggers are classic because "
        "the norms they violate are near-universal in social life: bodies "
        "should be controlled, speech should be accurate, competence should "
        "be smooth, private things should stay private, status should be "
        "steady. The witness multiplier explains why the same slip alone is "
        "nothing: trip in an empty hallway and there is no embarrassment, "
        "only annoyance - the appraisal finds no audience and the sequence "
        "never starts. The trigger's power also depends on suddenness: "
        "embarrassment favors the ambush, the slip you did not see coming, "
        "because suddenness denies the mind its preparation time and the "
        "appraisal lands at full force. This is why rehearsed performances "
        "rarely embarrass even when flawed - the performer expected "
        "imperfection - while casual moments detonate. The practical use of "
        "the parade is pre-loading: knowing your personal top five triggers "
        "lets you rehearse the recovery line in advance, converting the "
        "ambush into a handled moment. The trigger still fires; the "
        "suffering does not have to."),
    key_points=[
        "The parade: bodily slips, verbal slips, competence slips, exposure triggers, status slips.",
        "Every trigger follows the formula: a norm plus a visible miss plus witnesses.",
        "The same slip alone is nothing - without witnesses the appraisal finds no audience and the sequence never starts.",
        "Embarrassment favors the ambush: suddenness denies preparation time and the appraisal lands at full force.",
        "Knowing your personal top five triggers lets you pre-load the recovery line and convert ambush into handled moment.",
    ],
    requirements=[
        "Five trigger families with multiple examples each",
        "The unifying formula stated",
        "The empty-hallway contrast proving the witness requirement",
        "Suddenness explained",
        "The pre-loading practice",
    ],
    standards=STD,
    citations=[CIT_MILLER, CIT_GOFFMAN, CIT_EDELMANN, CIT_LEARY, CIT_APA],
    sig_lens=(
        "In the Signature lens, the parade is the soul's obstacle course - "
        "everyone runs it, nobody designed it, and finishing is the whole "
        "sport. Signal: each trigger names a norm you carry; the course map "
        "is a map of what you value. Repair: pre-load your top five - the "
        "recovery line rehearsed is the ambush disarmed. Mastery: the "
        "person who has walked the whole parade stops fearing new floats - "
        "they have seen every costume.")),
dict(
    key="embarrassment_personal_triggers", name="Personal Triggers: Memories, Anniversaries, and Private Associations",
    group="Compounded", ladder_rank=19, ladder_tier="compounded",
    description=(
        "Beyond the classics, everyone carries a private trigger library - "
        "situations that embarrass them specifically because of their own "
        "history. The mechanisms are associative: a neutral situation gets "
        "wired to an old embarrassment, and thereafter the situation alone "
        "can fire the feeling. The person once laughed at for their accent "
        "feels heat rising before they even open their mouth in a new "
        "group. The anniversary trigger is temporal: the date of the big "
        "public mistake returns each year with a phantom blush, even though "
        "no one else remembers. Place triggers work the same way: the "
        "cafeteria table, the conference room, the street corner where it "
        "happened - walking past can warm the cheeks with no new event at "
        "all. People triggers: the specific witness from the original "
        "scene, whose mere presence re-arms the alarm. Word triggers: the "
        "mispronounced word, the wrong name, the phrase from the incident, "
        "heard in a completely innocent context. These personal triggers "
        "feel irrational from the outside (\"why would THAT embarrass "
        "you?\") and completely reasonable from the inside, because the "
        "nervous system does not distinguish the echo from the event. "
        "Mapping your own library is one of the highest-value exercises in "
        "this database: unnamed triggers ambush; named triggers can be "
        "defused."),
    how_it_works=(
        "Personal triggers form through associative learning - the same "
        "machinery that makes a song remind you of a summer. During the "
        "original embarrassment, the arousal spike stamps the surrounding "
        "details (place, people, words, date) into memory with unusual "
        "strength; emotion is memory's highlighter. Later, any one of those "
        "details can reactivate a fraction of the original arousal, which "
        "the appraisal system reads as a fresh signal: heat rising, "
        "therefore danger now. The cruel part is the generalization "
        "gradient: the trigger spreads to similar situations - one mocked "
        "presentation makes all presentations warm the cheeks. The "
        "liberating part is that associative links weaken with safe "
        "re-exposure: each time the trigger situation occurs WITHOUT a new "
        "embarrassment, the link loses strength, a process psychologists "
        "call extinction. This gives a precise method for defusing personal "
        "triggers. First, map them: write the situations, places, people, "
        "and words that warm your cheeks disproportionately, and trace each "
        "to its original scene. Second, test the link: ask what actually "
        "happened then versus what is happening now. Third, re-enter "
        "gradually: collect small, safe completions in the trigger "
        "situation until the nervous system updates its file. The library "
        "does not have to be carried forever; it can be checked out, read, "
        "and returned."),
    key_points=[
        "Personal triggers form by association: the arousal spike stamps surrounding details into memory, and the details later re-fire the feeling.",
        "The library includes anniversary triggers, place triggers, people triggers, and word triggers.",
        "The generalization gradient spreads one mocked presentation to all presentations.",
        "Associative links weaken with safe re-exposure - each safe completion updates the nervous system's file.",
        "The defusing method: map the library, trace each trigger to its scene, test then-vs-now, re-enter gradually.",
    ],
    requirements=[
        "The associative mechanism explained",
        "Four personal trigger types with examples",
        "The generalization gradient",
        "Extinction through safe re-exposure",
        "The four-step defusing method",
    ],
    standards=STD,
    citations=[CIT_MILLER, CIT_EDELMANN, CIT_LEARY, CIT_TANGNEY, CIT_APA],
    sig_lens=(
        "In the Signature lens, the private library is the soul's old "
        "case files - every trigger a folder from a day the belonging felt "
        "at risk. Signal: a trigger firing is a file asking to be closed, "
        "not a verdict being repeated. Repair: open the folder on purpose "
        "- name the scene, date the file, collect the safe completions. "
        "Mastery: the person who has read their whole library walks past "
        "the old street corner and feels only weather.")),
dict(
    key="embarrassment_surprise_triggers", name="Surprise Triggers: The Odd, Unexpected Things That Set It Off",
    group="Compounded", ladder_rank=20, ladder_tier="compounded",
    description=(
        "Some triggers embarrass by their sheer oddness - no norm seems "
        "broken, yet the cheeks burn. Being praised unexpectedly in front "
        "of a group: the spotlight lands without a slip, and the body "
        "blushes at attention itself. Being helped with something easy: "
        "the kindness implies incompetence, and the gratitude comes mixed "
        "with heat. Laughing at the wrong moment - at a funeral's "
        "tender anecdote, during a serious meeting - where nothing was "
        "intended and everything was witnessed. The compliment that "
        "misfires: \"you look tired\" meant as concern, received as "
        "exposure. Being caught being kind: the donation noticed, the good "
        "deed seen, the private generosity made public - virtue exposed "
        "feels strangely like a slip. The body betraying you without cause: "
        "blushing when you have nothing to hide, which then becomes its own "
        "trigger as you blush about blushing. Technology ambushes: the "
        "camera turning on unannounced, the microphone hot when you thought "
        "it was muted, autocorrect's public confessions. These surprise "
        "triggers share a structure: the appraisal finds exposure without "
        "a clear offense, so the mind gropes for what went wrong - and the "
        "groping itself prolongs the feeling. The remedy is to name the "
        "structure: \"I am blushing at attention, not at a fault.\" Nothing "
        "was broken; the alarm simply misfired. Alarms misfire; that is "
        "what alarms do."),
    how_it_works=(
        "Surprise triggers work because the appraisal system is tuned for "
        "speed over accuracy. Faced with sudden exposure, it fires the "
        "embarrassment sequence first and investigates second - better to "
        "blush needlessly than to miss a real social threat. This "
        "shoot-first design explains the whole category: praise, kindness "
        "caught, attention without offense - all produce the exposure half "
        "of the formula (witnesses plus sudden self-consciousness) without "
        "the offense half, and the system fires anyway. The blush-about-"
        "blushing loop is the purest example: the first blush is the "
        "misfire, the second blush is embarrassment about the visible "
        "misfire, each layer certified real by the last. Breaking the loop "
        "requires the one move the system resists: a calm, accurate label "
        "applied mid-feeling. \"This is attention, not offense\" tells the "
        "appraisal system to stand down, and because the system is fast but "
        "also updateable, the label usually works within seconds. With "
        "repetition, the system learns the new category - praised-without-"
        "slip stops firing - which is how people become comfortable being "
        "seen. The surprise triggers are thus the training ground for the "
        "deepest lesson: the alarm is a servant, and servants can be "
        "retrained."),
    key_points=[
        "Surprise triggers - unexpected praise, caught kindness, misfiring compliments, hot microphones - embarrass without any clear offense.",
        "The appraisal system is tuned for speed over accuracy: it fires on exposure first and investigates second.",
        "Blushing about blushing is the purest loop: each layer of misfire certifies the last as real.",
        "The remedy is a calm mid-feeling label: this is attention, not offense.",
        "With repetition the system learns the new category - the alarm is a servant that can be retrained.",
    ],
    requirements=[
        "At least five odd trigger examples",
        "The shared structure: exposure without offense",
        "The speed-over-accuracy design principle",
        "The blush-about-blushing loop dissected",
        "The relabeling remedy and retraining",
    ],
    standards=STD,
    citations=[CIT_MILLER, CIT_EDELMANN, CIT_KELTNER, CIT_LEARY, CIT_APA],
    sig_lens=(
        "In the Signature lens, the surprise trigger is the soul's smoke "
        "detector going off at burnt toast - loud, wrong, and working as "
        "designed. Signal: a misfire is still information - it marks where "
        "your attention-sensitivity lives. Repair: label it mid-feeling - "
        "\"attention, not offense\" - and let the detector learn. Mastery: "
        "the person comfortable being seen has simply retrained more "
        "detectors than the person still hiding from the toast.")),
dict(
    key="embarrassment_chain_reactions", name="Chain Reactions: How One Trigger Sets Off a Cascade",
    group="Compounded", ladder_rank=21, ladder_tier="compounded",
    description=(
        "Embarrassment loves company: one trigger often detonates a chain. "
        "The classic cascade starts with a small slip - tripping on the "
        "stairs - which spikes arousal; the arousal makes the person clumsy "
        "and self-focused, which produces the second slip - dropping the "
        "papers they were carrying; the second slip in front of the same "
        "witnesses multiplies the appraisal (\"now they really think I am "
        "a mess\"); the multiplied appraisal spikes arousal further, which "
        "degrades coordination and judgment further - the apology comes out "
        "mangled, the laugh too loud. Each link in the chain has the same "
        "structure: embarrassment impairs the exact faculties - poise, "
        "timing, smooth speech, fine motor control - that would prevent the "
        "next embarrassment. The chain can also jump emotions: embarrassment "
        "about the trip becomes frustration at the clumsiness, becomes "
        "anger at the laughing witness, becomes shame about the anger - a "
        "four-emotion cascade from one stair. Or it jumps people: your "
        "visible embarrassment makes your companion embarrassed for you, "
        "whose discomfort makes you more embarrassed - the empathic loop. "
        "Chains feel like proof that the day is cursed; they are actually "
        "proof of a feedback loop, and feedback loops have circuit "
        "breakers."),
    how_it_works=(
        "The cascade runs on a simple engine: arousal degrades performance, "
        "degraded performance creates new triggers, new triggers raise "
        "arousal. Arousal narrows attention onto the threat (the watching "
        "eyes), which steals resources from coordination, timing, and word-"
        "finding - the precise skills social smoothness requires. So the "
        "embarrassed person is neurologically least equipped to be graceful "
        "at the exact moment grace is most needed. The emotion-jumping "
        "chain adds appraisal shifts: each new feeling re-appraises the "
        "situation (\"this is unfair\" for anger, \"I am defective\" for "
        "shame), and each re-appraisal justifies more arousal. The empathic "
        "loop adds a second nervous system: humans catch embarrassment "
        "like a yawn, and the caught discomfort feeds back. The circuit "
        "breaker is always the same: interrupt the arousal leg, because it "
        "is the only leg fully under short-term control. Stop moving - "
        "plant your feet, set down what you are carrying, pause the "
        "talking. One full slow breath. Let the witnesses' attention move "
        "on (it will, in seconds). Then resume at half speed. Chains need "
        "momentum; stillness starves them. The person who learns to freeze "
        "gracefully - to pause instead of flail - never meets the third "
        "link."),
    key_points=[
        "The cascade engine: arousal degrades poise, degraded poise creates new triggers, new triggers raise arousal.",
        "Embarrassment impairs exactly the faculties - timing, smooth speech, coordination - that would prevent the next slip.",
        "Chains jump emotions (embarrassment to frustration to anger to shame) and jump people (the empathic loop).",
        "Chains feel like a cursed day; they are a feedback loop, and feedback loops have circuit breakers.",
        "The breaker: stop moving, one slow breath, let attention pass, resume at half speed - stillness starves chains.",
    ],
    requirements=[
        "A concrete multi-link cascade example",
        "The engine stated as a loop",
        "The cruel irony: impaired faculties named",
        "Emotion-jumping and people-jumping chains",
        "The circuit breaker procedure",
    ],
    standards=STD,
    citations=[CIT_MILLER, CIT_EDELMANN, CIT_KELTNER, CIT_LEARY, CIT_APA],
    sig_lens=(
        "In the Signature lens, the chain is the soul's avalanche - one "
        "loose stone, then the whole slope, then the story that the "
        "mountain hates you. Signal: the second slip is never about the "
        "stair; it is about the arousal the stair left behind. Repair: be "
        "the circuit breaker - plant, breathe, pause, half-speed. Mastery: "
        "the person who can freeze gracefully has learned the rarest "
        "belonging skill - stillness under eyes.")),

# -------------------------------------------- 22-25: how it shows in behavior
dict(
    key="embarrassment_actions", name="What People Do: The Typical Actions and Reactions",
    group="Compounded", ladder_rank=22, ladder_tier="compounded",
    description=(
        "When embarrassment hits, behavior falls into a recognizable menu. "
        "The flight family: leaving the scene quickly, turning away, "
        "burying the face in hands, suddenly needing to be elsewhere - the "
        "body voting with its feet for disappearance. The cover family: "
        "laughing - the nervous laugh that buys time and signals \"no "
        "threat\"; joking about the slip immediately, getting the laugh "
        "first; the quick self-deprecating comment that defuses the room. "
        "The repair family: apologizing (once, cleanly, is the gold "
        "standard), fixing what can be fixed (picking up the papers, "
        "correcting the name), explaining briefly without over-explaining. "
        "The freeze family: going still, going quiet, the deer-in-headlights "
        "pause while the mind reboots. And the overcorrection family, the "
        "most expensive: apologizing five times, explaining for ten "
        "minutes, laughing too long, complimenting the witnesses "
        "desperately - behaviors that extend the spotlight instead of "
        "closing it. Most people run a personal greatest-hits mix of two or "
        "three families. The menu is worth studying because each family has "
        "a cost profile: flight ends the exposure but skips the repair; "
        "cover is fast but can read as not taking it seriously; repair is "
        "the gold standard but requires composure; freeze buys time but "
        "looks strange if held; overcorrection feels safest and costs the "
        "most. Knowing your default family is the first step to choosing "
        "instead of defaulting."),
    how_it_works=(
        "Each behavior family serves one of the twin urges from the "
        "motivational layer: hide or repair. Flight and freeze serve hide - "
        "they reduce exposure, the fastest way to lower arousal. Cover and "
        "repair serve repair - they manage the audience's impression, the "
        "way to close the loop. Overcorrection is hide and repair "
        "malfunctioning together: the person tries to repair so hard that "
        "they extend the exposure they were trying to end. The cost "
        "profiles follow from the audience's reading. Witnesses forgive "
        "quickly when they see the standard script - slip, signal, repair, "
        "move on - because it matches their mental model of a normal "
        "person having a normal moment. Deviations from the script cost: "
        "fleeing without repair leaves the story untold (witnesses fill it "
        "in); overcorrection breaks the script's timing (the scene runs "
        "too long). This is why the gold standard is so simple: one clean "
        "apology or one light joke, fix what is fixable, then resume. It "
        "is not about perfection; it is about giving the audience the "
        "script they expect so their attention can move on - which is all "
        "the audience ever wanted."),
    key_points=[
        "Five behavior families: flight, cover, repair, freeze, and the expensive overcorrection.",
        "Flight and freeze serve the hide urge; cover and repair serve the repair urge.",
        "The gold standard: one clean apology or one light joke, fix what is fixable, then resume.",
        "Witnesses forgive fast when they see the standard script: slip, signal, repair, move on.",
        "Overcorrection feels safest and costs the most - it extends the spotlight it was trying to end.",
    ],
    requirements=[
        "Five families with concrete behaviors each",
        "The twin-urge mapping: hide vs repair",
        "Cost profile per family",
        "The gold standard stated",
        "The audience-script explanation",
    ],
    standards=STD,
    citations=[CIT_GOFFMAN, CIT_GOFFMAN_IR, CIT_MILLER, CIT_KELTNER, CIT_APA],
    sig_lens=(
        "In the Signature lens, the menu is the soul's emergency toolkit - "
        "five tools, each honest, each with a price tag. Signal: your "
        "default family is your history talking; hear which tool you grab "
        "before you judge the grab. Repair: reach past the default for the "
        "gold standard - one clean apology, one light joke, resume. "
        "Mastery: the person with all five tools but a favorite gold "
        "standard never has to improvise under fire.")),
dict(
    key="embarrassment_speech", name="What People Say: Phrases, Tone, and Speech Patterns",
    group="Compounded", ladder_rank=23, ladder_tier="compounded",
    description=(
        "Embarrassment has a dialect, and fluent speakers recognize it "
        "instantly. The apology cluster: \"oh my god, I am so sorry,\" "
        "\"I cannot believe I just did that,\" \"please ignore that\" - "
        "often repeated, often stacked three deep. The deflection cluster: "
        "\"anyway!\" \"so, as I was saying,\" the abrupt subject change "
        "that pretends the last ten seconds did not happen. The self-"
        "deprecation cluster: \"classic me,\" \"smooth, real smooth,\" "
        "\"and that is why I am not allowed to...\" - the pre-emptive "
        "strike that robs witnesses of the first joke. The over-explanation "
        "cluster: the five-minute backstory for a two-second slip, the "
        "context nobody asked for, the justification that becomes its own "
        "event. The laugh track: \"ha!\" deployed as punctuation, the "
        "nervous giggle between sentences, laughter that arrives before "
        "the joke. Tone shifts are as telling as words: pitch climbs, "
        "speed increases, volume wobbles - the voice of a person talking "
        "slightly faster than their composure. Then the recovery dialect, "
        "the fluent speaker's upgrade: the single clean \"my mistake,\" "
        "the light \"well, that happened,\" the warm \"thanks for rolling "
        "with that\" - brief, owned, forward-moving. Learning the dialect "
        "serves two ways: you can hear it in others and respond with grace, "
        "and you can audit your own speech and upgrade from the apology "
        "cluster to the recovery dialect one phrase at a time."),
    how_it_works=(
        "Speech under embarrassment is the mouth trying to do the repair "
        "beat at talking speed. The clusters map to strategies: apologies "
        "perform remorse, deflection performs normalcy, self-deprecation "
        "performs awareness, over-explanation performs justification, the "
        "laugh track performs ease. The problem is dosage: one apology "
        "performs remorse; five apologies perform anxiety, and the audience "
        "starts comforting the apologizer instead of moving on. The vocal "
        "changes - pitch, speed, wobble - are arousal leaking into the "
        "speech muscles, the same sympathetic activation that tightens the "
        "shoulders; they cannot be fully suppressed, which is why the "
        "recovery dialect works with them instead of against them. The "
        "recovery phrases succeed for three reasons: they are short (the "
        "spotlight gets no new material), they are owned (\"my mistake\" "
        "admits without groveling), and they are forward-moving (\"thanks "
        "for rolling with that\" hands the audience its next line). "
        "Upgrading the dialect is a mechanical practice: pick your most "
        "used cluster, write its replacement phrase, rehearse it three "
        "times aloud. The mouth learns scripts the way the hands learn "
        "chords - by repetition, not by insight."),
    key_points=[
        "The dialect has six clusters: apology, deflection, self-deprecation, over-explanation, laugh track, and the recovery dialect.",
        "Dosage is everything: one apology performs remorse; five perform anxiety and flip the audience into comforting you.",
        "Pitch climbs, speed increases, volume wobbles - arousal leaking into the speech muscles.",
        "The recovery dialect wins on three counts: short, owned, forward-moving.",
        "Upgrading is mechanical: pick a cluster, write the replacement, rehearse it aloud three times.",
    ],
    requirements=[
        "Six speech clusters with example phrases",
        "The dosage principle",
        "Vocal changes explained physiologically",
        "The recovery dialect with examples",
        "The mechanical upgrade practice",
    ],
    standards=STD,
    citations=[CIT_GOFFMAN, CIT_GOFFMAN_IR, CIT_MILLER, CIT_EDELMANN, CIT_APA],
    sig_lens=(
        "In the Signature lens, the dialect is the soul's repair language - "
        "and most people speak it with an apology accent. Signal: hear "
        "your own cluster and you will hear your strategy. Repair: learn "
        "the recovery dialect phrase by phrase - \"my mistake,\" \"well, "
        "that happened,\" \"thanks for rolling with that.\" Mastery: the "
        "person fluent in recovery speaks for ten seconds and the room "
        "moves on - the shortest sentences carry the most grace.")),
dict(
    key="embarrassment_judgment", name="How Embarrassment Changes Decisions and Judgment",
    group="Advanced", ladder_rank=24, ladder_tier="advanced",
    description=(
        "Embarrassment does not just feel bad; it tilts the steering wheel. "
        "In the heat of it, judgment narrows to a single question - \"how "
        "do I look right now?\" - and everything else goes soft. Decisions "
        "made in this state share a profile: they are fast, avoidant, and "
        "overpriced. The person cancels the second date because the first "
        "had an awkward pause; declines the presentation slot because the "
        "last one wobbled; over-apologizes to a colleague and then avoids "
        "them for a month, converting a two-minute slip into a "
        "relationship debt. Risk assessment skews: the embarrassed mind "
        "treats social risks as larger than they are (that audience "
        "definitely remembers) and treats avoidance as cheaper than it is "
        "(skipping the meeting costs nothing - except the opportunity). "
        "Memory tilts too: the slip gets encoded in high resolution while "
        "the recovery gets encoded in low, so the mental file reads worse "
        "than the event was. Perhaps most costly is the identity "
        "generalization: \"I embarrassed myself\" quietly becomes \"I am "
        "an embarrassing person,\" and future decisions get made by that "
        "identity - smaller rooms, safer roles, fewer auditions. The "
        "counter-move is procedural, not heroic: no big social decisions "
        "in the first hour after a strong embarrassment; write the "
        "decision down and revisit it tomorrow; ask what you would advise "
        "a friend with the same footage. The feeling passes in minutes; "
        "the decisions it tilts can last years. Give the steering wheel "
        "back to the cooler driver."),
    how_it_works=(
        "The tilt runs through three channels. First, attentional "
        "narrowing: arousal focuses the mind on the threat (the watching "
        "eyes) and starves everything else - consequences, alternatives, "
        "base rates - of processing power. Decisions made with a starved "
        "processor are simple and defensive. Second, the affect heuristic: "
        "the bad feeling gets used as information (\"I feel awful, so it "
        "must be awful\"), inflating the perceived size of the social "
        "damage and deflating the perceived value of re-engaging. Third, "
        "memory asymmetry: the brain's threat system stores the slip in "
        "detail and the mundane recovery barely at all, so every later "
        "recall re-appraises a highlight reel of the worst seconds. "
        "Together they produce the classic post-embarrassment decision "
        "errors: withdrawal (avoid the people, the place, the activity), "
        "overpayment (apologize, explain, compensate far beyond the debt), "
        "and identity shrinkage (take up less space next time). The "
        "procedural counter-move works because it does not fight the "
        "feeling - it sidesteps it in time. An hour later the arousal is "
        "gone; tomorrow the memory has cooled; the friend's-advice frame "
        "borrows an unafflicted processor. None of this requires the "
        "embarrassment to be \"managed\" in the moment - it only requires "
        "the decisions to wait their turn."),
    key_points=[
        "Decisions made mid-embarrassment are fast, avoidant, and overpriced - the steering wheel tilts to a single question.",
        "Three channels drive the tilt: attentional narrowing, the affect heuristic, and memory asymmetry.",
        "The classic errors: withdrawal, overpayment, and identity shrinkage - each converts minutes of feeling into months of cost.",
        "\"I embarrassed myself\" quietly becomes \"I am an embarrassing person\" unless the generalization is caught.",
        "The counter-move is procedural: no big social decisions for an hour, write it down, revisit tomorrow, use the friend's-advice frame.",
    ],
    requirements=[
        "The tilted decision profile described",
        "Three channels explained",
        "Three classic errors named",
        "The identity generalization caught",
        "The procedural counter-move",
    ],
    standards=STD,
    citations=[CIT_LEARY, CIT_MILLER, CIT_EDELMANN, CIT_TANGNEY, CIT_APA],
    sig_lens=(
        "In the Signature lens, tilted judgment is the soul driving with "
        "the belonging-meter taped over the windshield - every turn serves "
        "the meter, none serves the road. Signal: the urge to decide NOW "
        "is the arousal talking, not the wisdom. Repair: park the decision "
        "- an hour, a night, a friend's-advice frame - and let the cooler "
        "driver take the wheel. Mastery: the person who never lets a blush "
        "sign contracts keeps every door the feeling tried to close.")),
dict(
    key="embarrassment_escalation", name="Behavior Under Intensity: How Actions Escalate as the Feeling Grows",
    group="Advanced", ladder_rank=25, ladder_tier="advanced",
    description=(
        "Watch embarrassment scale and the behavior escalates in a "
        "predictable staircase. Step one, mild: the person smiles, makes "
        "the light comment, moves on - behavior stays social and smooth. "
        "Step two, moderate: the repair efforts multiply - the joke, then "
        "the apology, then the explanation, then the second joke; the "
        "person is working visibly harder than the situation requires, and "
        "witnesses begin to notice the working rather than the slip. Step "
        "three, strong: behavior fragments - sentences trail off, the "
        "person repeats themselves, laughter comes at wrong moments, hands "
        "fidget uncontrollably; the repair attempts start generating their "
        "own embarrassment, the chain reaction from record 21. Step four, "
        "severe: the system flips from repair to escape - abrupt departure, "
        "tears, freezing completely, or the desperate overcorrection of "
        "confessing far more than the moment required. The staircase "
        "matters because each step has a different correct response, and "
        "the most common error is responding to step three with step-one "
        "tools (\"just laugh it off\" - the person cannot) or to step one "
        "with step-four tools (fleeing a tiny slip, which manufactures a "
        "bigger scene). The escalation also has a tell: the ratio of repair "
        "effort to slip size. When the effort dwarfs the slip, you are "
        "watching escalation, not the event - and the right move, whether "
        "you are the person or the witness, is to de-escalate the effort, "
        "not re-litigate the slip."),
    how_it_works=(
        "The staircase is arousal dose plus feedback. Each step up adds "
        "arousal, and arousal does two things: it degrades the smooth "
        "performance the repair requires, and it raises the felt stakes, "
        "which demands more repair effort, which - performed clumsily under "
        "arousal - creates new slips. This is the escalation engine, and it "
        "runs until something breaks the loop: the arousal clears (time), "
        "the audience leaves or laughs kindly (social circuit breaker), or "
        "the person deliberately downshifts (the freeze-gracefully move "
        "from record 21). The effort-to-slip ratio is the diagnostic: a "
        "healthy recovery spends effort proportional to the slip; "
        "escalation spends effort proportional to the fear. Teaching the "
        "staircase gives both roles their script. The embarrassed person "
        "learns to recognize their step and apply the matching tool: step "
        "two needs one repair and a stop; step three needs stillness and a "
        "breath before any words; step four needs permission to exit "
        "gracefully and return later. The witness learns to read the step "
        "too: do not demand a laugh from step three, do not chase step "
        "four's exit - offer the bridge (\"let's grab air\") and let the "
        "person cross it."),
    key_points=[
        "The staircase: smooth recovery, multiplied repair, fragmented behavior, flip to escape - each step predictable.",
        "The escalation engine: arousal degrades repair performance, degraded repair creates new slips, new slips raise arousal.",
        "The diagnostic is the effort-to-slip ratio: when effort dwarfs the slip, you are watching escalation, not the event.",
        "The common error is mismatched tools: step-one tools for step three, or step-four tools for step one.",
        "Each step has its matching tool: one repair and stop; stillness then words; permission to exit and return.",
    ],
    requirements=[
        "Four staircase steps described behaviorally",
        "The escalation engine as a loop",
        "The effort-to-slip ratio diagnostic",
        "The mismatched-tools error",
        "Matching tools per step, for the person and the witness",
    ],
    standards=STD,
    citations=[CIT_MILLER, CIT_EDELMANN, CIT_KELTNER, CIT_GOFFMAN_IR, CIT_APA],
    sig_lens=(
        "In the Signature lens, the staircase is the soul climbing the "
        "wrong way - each step up is effort spent against the belonging "
        "instead of for it. Signal: when your repair effort dwarfs the "
        "slip, the staircase has you, not the moment. Repair: name your "
        "step and use its tool - stop, stillness, or graceful exit. "
        "Mastery: the person who can step DOWN the staircase on purpose - "
        "from frantic to still in one breath - has the rarest social "
        "superpower: command of their own escalation.")),
# ----------------------------------------- 26-28: healthy expression
dict(
    key="embarrassment_healthy_expression", name="Healthy Expression: Saying It, Showing It, Channeling It Well",
    group="Advanced", ladder_rank=26, ladder_tier="advanced",
    description=(
        "Healthy expression of embarrassment is not the absence of the "
        "feeling - it is the feeling completing its honest cycle. Saying "
        "it well means the brief, owned acknowledgment: \"well, that "
        "happened,\" \"my mistake - let me fix that,\" said once, warmly, "
        "without groveling and without deflection. The words give the "
        "audience the script they need and give the speaker the dignity of "
        "authorship. Showing it well means letting the natural display run "
        "its thirty seconds - the smile, the glance away, the blush - "
        "instead of plastering over it; witnesses trust the honest signal "
        "and move on faster. Channeling it well is the advanced art: "
        "turning the slip into material - the self-told funny story, the "
        "lesson filed and shared (\"here is the mistake I will not make "
        "twice\"), the warmth toward others in the same spot (\"I have "
        "been exactly there\"). The three share a principle: embarrassment "
        "handled openly shrinks, embarrassment handled secretly grows. The "
        "healthy expresser also knows the aftercare: the replay gets its "
        "reality check, the lesson gets filed, the self gets the same "
        "kindness they would offer a friend. None of this requires "
        "fearlessness - the blush still comes. It requires only the "
        "decision, made in advance, that the feeling will be ridden rather "
        "than fought, spoken rather than swallowed, and finished rather "
        "than fed."),
    how_it_works=(
        "Healthy expression works because it cooperates with the "
        "five-beat sequence instead of jamming it. Saying it cleanly "
        "completes the repair beat on schedule - the audience gets its "
        "signal, the loop closes, attention moves on. Showing it honestly "
        "lets the display beat do its appeasement work - the blush "
        "certifies awareness, witnesses respond with sympathy, and the "
        "interaction warms instead of cooling. Channeling converts the "
        "aftershock's raw material into social currency or stored wisdom, "
        "which is the only move that actually shrinks future embarrassment: "
        "the filed lesson prevents repeats, and the told story proves to "
        "the nervous system that exposure is survivable. The aftercare "
        "matters because the sequence's weakest point is the replay loop - "
        "an unclosed loop re-fires the feeling for days, while a closed "
        "loop teaches the system that peaks pass. The pre-decision is the "
        "master key: people who decide in advance (\"when I slip, I will "
        "own it lightly and move on\") execute gracefully under arousal, "
        "because arousal degrades improvisation but spares rehearsed "
        "scripts. Healthy expression is therefore less a personality trait "
        "than a prepared script - and scripts can be written by anyone."),
    key_points=[
        "Healthy expression is the feeling completing its honest cycle - not the absence of the blush.",
        "Say it: one brief owned acknowledgment. Show it: let the thirty-second display run. Channel it: turn the slip into story or lesson.",
        "The principle: embarrassment handled openly shrinks; handled secretly grows.",
        "Aftercare closes the loop: reality-check the replay, file the lesson, offer yourself a friend's kindness.",
        "The master key is the pre-decision - a rehearsed script survives arousal because arousal spares scripts, not improvisation.",
    ],
    requirements=[
        "Saying, showing, and channeling each described with examples",
        "The open-vs-secret principle",
        "Aftercare: replay, lesson, self-kindness",
        "Cooperation with the five-beat sequence explained",
        "The pre-decision as master key",
    ],
    standards=STD,
    citations=[CIT_GOFFMAN, CIT_KELTNER, CIT_MILLER, CIT_LEARY, CIT_APA],
    sig_lens=(
        "In the Signature lens, healthy expression is the soul's clean "
        "craft - the blush ridden like a wave instead of fought like a "
        "fire. Signal: the urge to hide is the old script; the decision "
        "to ride is the new one, and decisions beat urges when they are "
        "made in advance. Repair: write your script now - the one line, "
        "the thirty seconds, the story later. Mastery: the person whose "
        "script is ready does not perform grace under pressure; they "
        "simply follow the rehearsal, and it looks like grace.")),
dict(
    key="embarrassment_unhealthy_expression", name="Unhealthy Expression: Bottling It Up or Exploding - What Each Costs",
    group="Advanced", ladder_rank=27, ladder_tier="advanced",
    description=(
        "Embarrassment mishandled takes two classic bad shapes. Bottling "
        "it up looks like composure: the person says nothing, shows "
        "nothing, files the slip in the private library - and then pays in "
        "installments. The unclosed loop replays for days; the replay "
        "manufactures fresh arousal; the arousal gets misread as evidence "
        "the slip was catastrophic; the person starts avoiding the people, "
        "the place, the activity. The costs compound quietly: narrowed "
        "life, stale shame where a blush belonged, and the eventual leak - "
        "the bottled feeling bursting out months later over something "
        "small, baffling everyone including the person. Exploding looks "
        "like the opposite: the person floods the scene - tearful "
        "over-apology, angry defensiveness (\"stop laughing!\"), dramatic "
        "exit, or the confession spiral that tells the room far more than "
        "the slip required. The costs are immediate and social: the "
        "audience's sympathy curdles into discomfort, the moment gets "
        "memorable for the wrong reason, and the person learns that "
        "feelings are dangerous, which feeds the next bottling. Both shapes "
        "share a root: the refusal to let the feeling complete its short, "
        "honest cycle. Bottling refuses the display and repair beats; "
        "exploding skips the repair beat and jumps to discharge. The "
        "healthy middle - brief honest display, one clean repair, move on - "
        "costs thirty seconds. The unhealthy shapes cost days, "
        "relationships, and rooms of one's life."),
    how_it_works=(
        "Bottling fails through the replay loop: without the repair beat, "
        "the sequence never closes, and the appraisal system keeps the "
        "file open indefinitely, re-firing arousal on each replay. The "
        "avoidance that follows is negatively reinforced - each avoided "
        "lunchroom brings relief, which teaches the system that lunchrooms "
        "are dangerous - so the world shrinks one avoided room at a time. "
        "The eventual leak happens because suppressed arousal does not "
        "decay; it waits, and a small later trigger gets the whole stored "
        "charge. Exploding fails through the audience: the display beat is "
        "designed to be brief, and when it runs ten times too long or ten "
        "times too hot, witnesses switch from the amusement program to the "
        "discomfort program - they stop seeing a relatable slip and start "
        "seeing a scene, and scenes are what people actually remember. The "
        "confession spiral adds a second cost: over-disclosure hands "
        "witnesses material the slip never contained. Both shapes are "
        "maintained by the same belief - that the feeling itself is the "
        "danger - when the evidence of this database says the opposite: "
        "the feeling is a thirty-second signal, and the danger is entirely "
        "in refusing its cycle. The correction for bottling is scheduled "
        "expression (tell the story to one safe person within 24 hours); "
        "the correction for exploding is the pause-and-halve rule (say "
        "half as much, then stop)."),
    key_points=[
        "Bottling looks like composure and pays in installments: replays, avoidance, narrowed life, and the eventual baffling leak.",
        "Exploding floods the scene: over-apology, defensiveness, dramatic exit, confession spiral - sympathy curdles into discomfort.",
        "Both share a root: refusing to let the feeling complete its short honest cycle.",
        "Bottling is maintained by negative reinforcement - each avoidance teaches the system the room is dangerous.",
        "Corrections: scheduled expression within 24 hours for bottling; the pause-and-halve rule for exploding.",
    ],
    requirements=[
        "Both shapes described with their cost profiles",
        "The shared root named",
        "Bottling's quiet compounding explained",
        "Exploding's audience-switch explained",
        "One concrete correction per shape",
    ],
    standards=STD,
    citations=[CIT_MILLER, CIT_EDELMANN, CIT_TANGNEY, CIT_LEARY, CIT_APA],
    sig_lens=(
        "In the Signature lens, bottling is the soul filing the blush in "
        "a drawer that never closes, and exploding is the soul setting the "
        "drawer on fire in public. Signal: both are the cycle refused - "
        "hear the refusal, not the character flaw. Repair: bottlers, "
        "schedule the telling; exploders, halve the words. Mastery: the "
        "person who gives every embarrassment its thirty honest seconds "
        "never pays the installment plan and never burns the room.")),
dict(
    key="embarrassment_everyday_practices", name="Everyday Practices: Small Habits That Keep Embarrassment in Balance",
    group="Advanced", ladder_rank=28, ladder_tier="advanced",
    description=(
        "Balance with embarrassment is built from small, repeatable habits, "
        "not from personality transplants. The morning habit: decide the "
        "day's script in advance - \"when I slip today, I will own it "
        "lightly and move on\" - the pre-decision that survives arousal. "
        "The in-the-moment habit: the three-second pause - breath, unclench, "
        "choose one repair - before the mouth runs its default cluster. "
        "The same-day habit: the story told first - recount the slip to a "
        "friend with humor before the replay loop gets exclusive rights to "
        "the footage. The evening habit: the two-minute audit - what "
        "embarrassed me today, what did I learn, is the loop closed? - "
        "written, not ruminated, because writing closes loops and "
        "rumination feeds them. The weekly habit: the exposure rep - "
        "deliberately doing one small thing that risks a tiny slip "
        "(asking the question, taking the class, telling the joke), "
        "collecting completed cycles on purpose. The relationship habit: "
        "being the kind witness - laughing with, never at; changing the "
        "subject gracefully for others; remembering that today's witness "
        "is tomorrow's embarrassed person. None of these takes more than "
        "minutes. Together they do what no single insight can: they give "
        "the nervous system a long track record of survived exposures, and "
        "a nervous system with a track record stops sounding the alarm at "
        "everyday static."),
    how_it_works=(
        "Habits work where insight cannot because embarrassment is a fast, "
        "arousal-driven system and insight is a slow, cool process - the "
        "two rarely meet in the moment. Habits bridge them by pre-loading "
        "behavior: the pre-decision installs the script before arousal "
        "arrives; the three-second pause installs a circuit breaker before "
        "the chain reaction starts; the story-told-first installs a "
        "competing narrative before the replay loop monopolizes the "
        "footage. The evening audit works through externalization - a "
        "written loop-closure is processed by the brain as completed "
        "business in a way that thought-loops are not. The weekly exposure "
        "rep works through extinction: each safe, small, survived exposure "
        "weakens the associative links that keep the alarm gain high. The "
        "kind-witness habit works socially: groups that handle each "
        "other's slips gracefully become low-embarrassment environments, "
        "which lowers everyone's dials - you are literally training your "
        "future audiences. The compounding is the point: no single habit "
        "transforms anything, but six small habits, repeated daily, rewrite "
        "the system's priors within weeks. Balance is not a state to "
        "achieve; it is a maintenance schedule to keep."),
    key_points=[
        "Six small habits: the morning pre-decision, the three-second pause, the story told first, the evening audit, the weekly exposure rep, the kind witness.",
        "Habits beat insight because they pre-load behavior before arousal arrives - arousal spares scripts, not improvisation.",
        "Writing closes loops; rumination feeds them - the evening audit must be written, not thought.",
        "Weekly exposure reps use extinction: safe small exposures weaken the alarm's gain.",
        "Being the kind witness trains your future audiences - grace given is grace banked.",
    ],
    requirements=[
        "Six habits, each concrete and minutes-long",
        "The habits-vs-insight mechanism",
        "The pre-loading principle",
        "Written audit vs rumination contrast",
        "The compounding claim: weeks, not years",
    ],
    standards=STD,
    citations=[CIT_MILLER, CIT_EDELMANN, CIT_LEARY, CIT_KELTNER, CIT_APA],
    sig_lens=(
        "In the Signature lens, the six habits are the soul's belonging "
        "maintenance - small daily tunings of the instrument. Signal: "
        "balance is not a trait you are given; it is a schedule you keep. "
        "Repair: start with one habit, the morning pre-decision - the "
        "cheapest, highest-leverage rep. Mastery: the person who keeps the "
        "schedule stops managing embarrassment entirely, because the system "
        "maintains itself - and that is what mastery always was: "
        "maintenance, made invisible by repetition.")),

# --------------------------------------- 29-31: recognizing it in others
dict(
    key="embarrassment_reading_others", name="Reading the Signs: Recognizing Embarrassment in Other People",
    group="Advanced", ladder_rank=29, ladder_tier="advanced",
    description=(
        "Reading embarrassment in others is a kindness skill, and the signs "
        "are generous once you know them. The face: the sudden downward "
        "glance, the pressed thin smile that does not reach the eyes, the "
        "blush blooming - the whole display from record 14, now worn by "
        "someone else. The body: the shrink - shoulders rolling in, head "
        "dropping, the person suddenly taking up less space; the face-touch, "
        "the neck-touch, the fidget. The voice: pitch climbing, speed "
        "increasing, the laugh that arrives as punctuation rather than joy. "
        "The behavior: the apology cluster firing on repeat, the abrupt "
        "\"anyway!\" subject change, the over-explanation, the sudden "
        "busy-ness. Context is the multiplier: these signs after a visible "
        "slip mean embarrassment; the same signs with no visible trigger "
        "may mean the person is replaying a private aftershock - be "
        "gentler, not more curious. The skill has three levels. Level one: "
        "spot the display. Level two: gauge the gradient - low (needs "
        "nothing), moderate (needs a laugh-with), high (needs a rescue). "
        "Level three: read the person's strategy - the coverer needs the "
        "joke joined, the freezer needs time without stares, the "
        "overcorrector needs a merciful interruption (\"we have all been "
        "there - tell me about the rest of the trip\"). Reading well is not "
        "about catching people; it is about catching them before they fall "
        "further."),
    how_it_works=(
        "Recognition works because the embarrassment display is one of the "
        "most honest and consistent signals humans produce - the "
        "involuntary components guarantee authenticity, and the recruitment "
        "order guarantees readability. Your brain already reads it "
        "unconsciously; training makes the reading conscious and therefore "
        "usable. The gradient-gauging is the critical upgrade: most people "
        "either miss embarrassment entirely or treat all of it as severe, "
        "and both errors cost - the missed person gets no bridge, the "
        "over-read person gets a rescue they did not need, which is itself "
        "embarrassing. The strategy-reading is the advanced layer: the "
        "same display plus different default behaviors (cover, freeze, "
        "overcorrect) calls for different responses, and matching the "
        "response to the strategy is what makes a witness feel like a "
        "friend rather than an audience. One caution governs the whole "
        "skill: never announce the reading. Saying \"you look embarrassed\" "
        "spotlights the very feeling the person is trying to survive; the "
        "skilled reader acts on the reading without naming it - the laugh "
        "joined, the subject changed, the bridge offered - and lets the "
        "person keep their dignity. Recognition is for response, not for "
        "commentary."),
    key_points=[
        "The signs are generous: the face display, the body shrink, the climbing voice, the apology cluster, the sudden busy-ness.",
        "Context multiplies: signs after a visible slip mean embarrassment; signs with no trigger may mean a private aftershock.",
        "Three levels: spot the display, gauge the gradient, read the person's strategy.",
        "Match the response to the strategy: join the coverer's joke, give the freezer unstared time, mercifully interrupt the overcorrector.",
        "Never announce the reading - act on it without naming it; recognition is for response, not commentary.",
    ],
    requirements=[
        "Signs organized by channel: face, body, voice, behavior",
        "The context multiplier explained",
        "Three skill levels",
        "Strategy-matched responses",
        "The never-announce rule",
    ],
    standards=STD,
    citations=[CIT_KELTNER, CIT_MODIGLIANI, CIT_GOFFMAN_IR, CIT_MILLER, CIT_APA],
    sig_lens=(
        "In the Signature lens, reading others is the soul's belonging "
        "radar turned outward - the same instrument that feels your blush, "
        "tuned to catch someone else's. Signal: the display you can spot "
        "is a person asking, without words, to be let back in. Repair: "
        "answer the ask with action, not announcement - the joined laugh, "
        "the changed subject, the offered bridge. Mastery: the person who "
        "reads embarrassment well becomes the room's safest audience, and "
        "safe audiences are remembered longer than any slip.")),
dict(
    key="embarrassment_supporting", name="What to Say and Do: Supportive Responses That Actually Help",
    group="Advanced", ladder_rank=30, ladder_tier="advanced",
    description=(
        "When someone near you is embarrassed, the right response is a "
        "rescue disguised as normalcy. The laugh-with: join their nervous "
        "laugh genuinely and briefly - not at them, with them - which "
        "converts the spotlight from judgment to shared humanity. The "
        "normalizer: \"that happens to everyone,\" \"I did worse last "
        "month,\" said lightly and truthfully - the specific worse story "
        "is gold, because it proves the claim. The bridge: change the "
        "subject smoothly to something that includes them (\"anyway, you "
        "were saying about the trip?\") - not a panicked swerve, which "
        "spotlights the rescue, but a natural handoff. The exit: when the "
        "gradient is high, offer a dignified way out - \"let's grab some "
        "air,\" \"walk with me to refill?\" - movement breaks the freeze "
        "and privacy lets the arousal clear. The later check-in: \"you "
        "handled that well, by the way\" - said once, later, privately - "
        "which rewrites the replay loop's footage with a kinder "
        "narration. What makes these work is their shared structure: each "
        "one reduces exposure, supplies the recovery script, or rewrites "
        "the aftershock - the three things the embarrassed person cannot "
        "do for themselves mid-arousal. The meta-rule: your job is to be "
        "boring about their slip. Treat it as unremarkable and the room "
        "takes your cue; treat it as a big deal and the room takes that "
        "cue instead. Audiences are cue-followers. Be the cue."),
    how_it_works=(
        "Supportive responses work by lending the embarrassed person the "
        "faculties that arousal has stolen. The laugh-with and the "
        "normalizer lend appraisal: they supply the \"this is normal\" "
        "reading the person's own appraisal system cannot produce "
        "mid-spike. The bridge lends attention management: it moves the "
        "room's spotlight, which the person cannot move themselves while "
        "frozen. The exit lends arousal clearance: privacy and movement "
        "let the sympathetic surge drain, which no amount of willpower "
        "achieves under eyes. The later check-in lends memory editing: the "
        "replay loop replays whatever narration is available, and a kind "
        "witness's line becomes part of the footage. The boring-about-it "
        "meta-rule works through social proof: witnesses calibrate their "
        "reactions to the highest-status calm person in the room, so your "
        "unruffled response literally sets the room's verdict. This is why "
        "the supporter's composure matters more than their words - a calm "
        "face plus any reasonable line beats brilliant words delivered "
        "with visible pity. And the later check-in deserves emphasis: most "
        "support happens in the moment, but the aftershock is where most "
        "suffering lives, and a single kind sentence, delivered privately "
        "hours later, can close a loop that would otherwise replay for a "
        "week."),
    key_points=[
        "Five moves: the laugh-with, the normalizer, the bridge, the exit, the later check-in.",
        "Each move lends a stolen faculty: appraisal, attention management, arousal clearance, or memory editing.",
        "The meta-rule: be boring about their slip - audiences are cue-followers, so your calm sets the room's verdict.",
        "The specific worse story is gold: it proves the normalizer's claim.",
        "The later check-in targets the aftershock, where most suffering actually lives.",
    ],
    requirements=[
        "Five moves with example lines",
        "The lending-faculties mechanism per move",
        "The boring-about-it meta-rule with the social-proof mechanism",
        "The specific-story upgrade for normalizers",
        "The later check-in emphasized",
    ],
    standards=STD,
    citations=[CIT_GOFFMAN_IR, CIT_KELTNER, CIT_MILLER, CIT_LEARY, CIT_APA],
    sig_lens=(
        "In the Signature lens, the supporter is the soul's bridge-builder - "
        "laying planks across someone else's spotlight so they can walk "
        "back to the group. Signal: your calm is the cue; the room will "
        "follow your face before your words. Repair: lend what arousal "
        "stole - the normal reading, the moved spotlight, the private "
        "minute, the kinder footage. Mastery: the person who builds "
        "bridges for others finds their own slips met with bridges - "
        "belonging, banked and returned with interest.")),
dict(
    key="embarrassment_mistakes_to_avoid", name="What NOT to Do: The Common Mistakes That Make It Worse",
    group="Advanced", ladder_rank=31, ladder_tier="advanced",
    description=(
        "Good intentions pave several roads to worse embarrassment. The "
        "spotlight callout: \"oh no, are you embarrassed?\" or \"look, "
        "you are blushing!\" - naming the feeling pins it to the wall "
        "while everyone watches. The replay: retelling the slip later for "
        "laughs (\"remember when you...?\") - the story the person told "
        "first is theirs to tell; your retelling is a re-exposure. The "
        "teasing escalation: the joke that was funny once, repeated until "
        "the person's smile goes thin - affectionate teasing has a "
        "half-life, and past it, it is just spotlight rental. The pity "
        "face: the exaggerated sympathy, the hand on the shoulder held too "
        "long, the \"oh, you poor thing\" - pity confirms the catastrophe "
        "framing the person is trying to escape. The fix-it lecture: "
        "explaining what they should have done, mid-blush - instruction "
        "requires a cool processor, and theirs is offline. The ignoring "
        "that is actually freezing: going silent and staring, the room "
        "holding its breath - attention without warmth reads as judgment. "
        "The comparison: \"that is nothing, one time I...\" deployed to "
        "minimize - intended as comfort, received as dismissal of their "
        "feeling. Each mistake shares a structure: it extends exposure, "
        "certifies the catastrophe, or steals the person's authorship of "
        "the moment. The universal correction is the same: shorten the "
        "spotlight, warm the room, return the pen. When in doubt, do less, "
        "warmly."),
    how_it_works=(
        "Each mistake worsens embarrassment through one of three mechanisms. "
        "Exposure extension: the callout, the replay, the extended teasing, "
        "and the frozen staring all keep the spotlight on past its natural "
        "thirty seconds, and every extra second is extra arousal with no "
        "repair. Catastrophe certification: the pity face and the fix-it "
        "lecture both signal \"this is a big deal,\" which the appraisal "
        "system believes - the witness's framing becomes the person's "
        "framing, upgrading a slip to an incident. Authorship theft: the "
        "retelling and the minimizing comparison both take the story out of "
        "the person's hands; the master move of telling it first only works "
        "if the telling stays theirs. The three mechanisms explain why "
        "these mistakes feel so bad out of proportion to their intent: they "
        "attack the exact three things recovery needs - a short spotlight, "
        "a normal framing, and the person's own pen. The universal "
        "correction inverts all three: shorten (move on quickly), warm "
        "(treat it as normal), return the pen (let them tell it, or not). "
        "\"Do less, warmly\" is not passivity; it is precision - the "
        "recognition that in the thirty seconds after a slip, the most "
        "helpful thing a witness can do is get out of the spotlight's way "
        "while keeping the room kind."),
    key_points=[
        "Seven classic mistakes: the spotlight callout, the replay, teasing escalation, the pity face, the fix-it lecture, frozen staring, the minimizing comparison.",
        "Each worsens through one of three mechanisms: exposure extension, catastrophe certification, or authorship theft.",
        "Witness framing becomes the person's framing - pity and lectures upgrade a slip to an incident.",
        "The retelling rule: the story the person told first is theirs; your retelling is a re-exposure.",
        "The universal correction: shorten the spotlight, warm the room, return the pen - do less, warmly.",
    ],
    requirements=[
        "Seven mistakes with the mechanism of each",
        "The three worsening mechanisms named",
        "The framing-contagion point",
        "The retelling rule",
        "The universal correction",
    ],
    standards=STD,
    citations=[CIT_GOFFMAN_IR, CIT_MILLER, CIT_KELTNER, CIT_LEARY, CIT_APA],
    sig_lens=(
        "In the Signature lens, the mistakes are the soul's friendly fire - "
        "every one meant kindly, every one landing on the belonging wound. "
        "Signal: good intent does not excuse the mechanism; watch what "
        "your move does to the spotlight, the framing, and the pen. "
        "Repair: invert all three - shorten, warm, return authorship. "
        "Mastery: the person who has memorized the seven mistakes never "
        "commits friendly fire, and their presence becomes the safest "
        "place in the room to be human.")),
# --------------------------------- 32-34: related emotions + simulation
dict(
    key="embarrassment_related_map", name="Related Emotions Map: Neighbors, Opposites, and Close Cousins",
    group="Advanced", ladder_rank=32, ladder_tier="advanced",
    description=(
        "Embarrassment sits in a crowded neighborhood, and knowing the "
        "neighbors prevents the most common mislabeling. Shame is the "
        "closest cousin and the most confused: embarrassment says \"that "
        "moment looked bad,\" shame says \"I am bad\" - embarrassment "
        "points at the event and fades in minutes, shame points at the "
        "self and can linger for years. Guilt is the next-door neighbor: "
        "guilt says \"I harmed someone\" and drives repair toward the "
        "harmed person; embarrassment says \"I looked foolish\" and drives "
        "repair toward the audience. Awkwardness is the mild sibling: "
        "social friction without the heat - the stalled conversation, the "
        "mistimed hug - uncomfortable but blushless. Humiliation is the "
        "dark cousin: embarrassment with a perpetrator - someone intended "
        "the exposure, and the feeling carries anger at them mixed with "
        "the heat. Stage fright is the anticipatory neighbor: the same "
        "machinery pointed at the future, embarrassment before the slip. "
        "Pride is the opposite pole: the same self-conscious machinery "
        "producing expansion instead of shrink, \"they saw me at my best\" "
        "instead of \"at my worst.\" The map's practical value is "
        "prescription: each neighbor needs different handling - shame "
        "needs self-compassion work, guilt needs amends, humiliation needs "
        "the perpetrator addressed, stage fright needs rehearsal - and "
        "treating embarrassment's thirty-second signal with shame's "
        "heavy tools is like using a fire hose on a candle."),
    how_it_works=(
        "The map is organized by three questions. What is the target - the "
        "moment, the self, or the harmed other? Embarrassment targets the "
        "moment, shame the self, guilt the other. What is the time course - "
        "minutes, or months? Embarrassment clears in minutes; shame and "
        "humiliation can persist indefinitely because their appraisals "
        "keep re-firing. Was there intent - accident, or perpetrator? "
        "Embarrassment is usually accidental exposure; humiliation adds "
        "someone who meant it, which is why anger rides along. These three "
        "questions sort any self-conscious feeling in seconds, and the "
        "sorting matters because the interventions do not transfer: the "
        "laugh-it-off that cures embarrassment insults shame; the amends "
        "that cure guilt are irrelevant to embarrassment (there is no "
        "harmed party, only witnesses); the perpetrator-confrontation that "
        "humiliation needs would be absurd for a tripped stair. The "
        "opposite pole, pride, completes the map by showing the machinery's "
        "range: identical self-awareness, identical audience-sensitivity, "
        "opposite appraisal - and the shrink-to-expansion flip is visible "
        "in real time when an embarrassing moment gets rescued brilliantly "
        "and the person glows instead of burns. Neighbors share walls; "
        "they are not the same house."),
    key_points=[
        "Three sorting questions - target, time course, intent - place any self-conscious feeling on the map in seconds.",
        "Shame targets the self and lingers; guilt targets the harmed other and drives amends; embarrassment targets the moment and clears in minutes.",
        "Humiliation is embarrassment with a perpetrator - hence the anger riding along; awkwardness is the blushless mild sibling; stage fright is the anticipatory neighbor.",
        "Pride is the opposite pole: same machinery, opposite appraisal, shrink flipped to expansion.",
        "Interventions do not transfer across neighbors - match the tool to the feeling or miss entirely.",
    ],
    requirements=[
        "Six neighbors mapped: shame, guilt, awkwardness, humiliation, stage fright, pride",
        "The three sorting questions",
        "Embarrassment vs shame vs guilt in one contrast each",
        "The non-transfer of interventions",
        "The pride flip: shrink to expansion",
    ],
    standards=STD,
    citations=[CIT_TANGNEY, CIT_LEWIS, CIT_MILLER, CIT_KELTNER, CIT_APA],
    sig_lens=(
        "In the Signature lens, the neighborhood is the soul's district of "
        "mirrors - each house reflecting a different angle of being seen. "
        "Signal: mislabeling the house sends you to the wrong address for "
        "help; sort first, then act. Repair: give each neighbor its own "
        "tool - the laugh for embarrassment, the compassion for shame, "
        "the amends for guilt, the boundary for humiliation. Mastery: the "
        "person who knows the whole district never again fights a candle "
        "with a fire hose.")),
dict(
    key="embarrassment_blends", name="Emotion Mixes: Embarrassment Blended with Four Partners",
    group="Advanced", ladder_rank=33, ladder_tier="advanced",
    description=(
        "Embarrassment plus amusement: the blend everyone knows - the "
        "slip is genuinely funny, the person laughs through the blush, "
        "and the room's laughter feels like being held, not held up. The "
        "body shows both: heat plus the loose, shaking laughter of real "
        "amusement. This is the blend to cultivate; it is embarrassment at "
        "its most social and least costly. Embarrassment plus anger: the "
        "dark blend - the slip gets laughed at unkindly, or the person "
        "feels set up, and heat mixes with a hot flash of resentment. The "
        "jaw sets under the blush; the laugh, if any, is sharp. This blend "
        "is the on-ramp to humiliation - the anger names a perpetrator, "
        "and the feeling stops being about the moment and starts being "
        "about the person who caused it. Embarrassment plus sadness: the "
        "quiet blend - the slip confirms a feared story (\"I never fit "
        "in\"), the blush fades but the heaviness stays, the person "
        "withdraws instead of repairing. The danger here is the identity "
        "generalization from record 24 taking root. Embarrassment plus "
        "pride: the strange, useful blend - the person is embarrassed by "
        "the slip but proud of the recovery (the bow after the stage trip), "
        "and the two feelings time-share: heat first, glow after. This "
        "blend is the template for mastery - it proves the machinery can "
        "produce expansion from the same event that produced shrink. "
        "Blends are not exotic; most real embarrassments arrive mixed. "
        "The skill is tasting the blend - naming the partner - because "
        "each partner changes the prescription: amusement wants joining, "
        "anger wants the perpetrator question, sadness wants the story "
        "challenged, pride wants to be noticed and grown."),
    how_it_works=(
        "Blends form the way colors mix: each emotion contributes its "
        "appraisal, its arousal signature, and its action urge, and the "
        "result is genuinely new, not just two feelings side by side. "
        "Embarrassment contributes the social-exposure appraisal and the "
        "blush; the partner contributes its own appraisal (amusement: "
        "\"this is funny\"; anger: \"this is unfair\"; sadness: \"this "
        "confirms loss\"; pride: \"I handled that\") and its urge (laugh, "
        "confront, withdraw, expand). The dominant partner is usually "
        "decided by the audience's behavior: kind laughter recruits "
        "amusement, cruel laughter recruits anger, indifference recruits "
        "sadness, applause for the recovery recruits pride. This is why "
        "the same slip blends differently in different rooms - the blend "
        "is co-authored by the witnesses. The tasting skill works because "
        "naming the partner emotion activates its specific regulation "
        "knowledge: once you know anger is in the mix, you know to ask the "
        "perpetrator question (was this actually aimed at me?) instead of "
        "applying embarrassment's laugh-it-off, which would suppress the "
        "anger into resentment. Blend literacy is the advanced level of "
        "this database for a reason: it requires holding two appraisals "
        "at once and answering both."),
    key_points=[
        "Four blends: with amusement (the blend to cultivate), anger (the on-ramp to humiliation), sadness (the identity-risk blend), pride (the mastery template).",
        "Blends are genuinely new feelings, not two side by side - each partner contributes appraisal, arousal, and urge.",
        "The audience co-authors the blend: kind laughter recruits amusement, cruel laughter recruits anger, applause recruits pride.",
        "The tasting skill - naming the partner - selects the right prescription for the mix.",
        "Mismatched tools are the risk: laugh-it-off on an anger blend suppresses it into resentment.",
    ],
    requirements=[
        "Four blends with body, feeling, and trajectory each",
        "The color-mixing mechanism",
        "Audience co-authorship",
        "The tasting skill and its payoff",
        "One mismatched-tool warning",
    ],
    standards=STD,
    citations=[CIT_KELTNER, CIT_MILLER, CIT_TANGNEY, CIT_LEWIS, CIT_APA],
    sig_lens=(
        "In the Signature lens, the blends are the soul's chords - single "
        "notes are rare, music is the norm. Signal: taste the chord and "
        "you will hear which strings are sounding. Repair: answer every "
        "string, not just the loudest - the anger in the humiliation, "
        "the sadness under the blush. Mastery: the person who can play "
        "the embarrassment-plus-pride chord on purpose - heat, then glow - "
        "has turned the whole instrument to their hand.")),
dict(
    key="embarrassment_full_simulation", name="Full Behavioral Simulation: From Trigger to Resolution",
    group="Advanced", ladder_rank=34, ladder_tier="advanced",
    description=(
        "Scene one, the trigger - 10:00 AM, open-plan office: Priya "
        "presents the quarterly numbers and her slide reads \"pubic "
        "relations\" instead of \"public relations,\" ten feet tall, in "
        "front of forty people including the CEO. The typo detonates the "
        "room's laughter. Scene two, onset and peak - 10:00:15: heat "
        "floods Priya's face and neck; her gaze drops to the laptop; the "
        "nervous laugh barks out wrong; her hands shake on the clicker. "
        "The inner voice: forty people, the CEO, I want the floor to open. "
        "Her default family is overcorrection - she can feel the five "
        "apologies lining up. Scene three, the circuit breaker - 10:00:40: "
        "she plants her feet, one slow breath, and uses the pre-decided "
        "script: \"Well - that is one way to get everyone's attention. The "
        "numbers, however, are fully clothed.\" The room laughs with her. "
        "One clean acknowledgment, no groveling, and she advances the "
        "slide. Scene four, the aftermath - 10:20 AM: the presentation "
        "lands; two colleagues grin at her in the hallway; the CEO says "
        "\"nice recovery.\" Her hands still tingle. Scene five, the "
        "aftershock - 11:00 PM: the replay starts in bed. She runs the "
        "reality check: the laughter was with-her (she heard the warmth), "
        "the CEO's comment is evidence, nobody will remember the typo next "
        "quarter. She files the lesson (proofread slides aloud, always) "
        "and the story (she will tell it first at Friday lunch). Scene "
        "six, resolution - Friday: she tells the story herself, the table "
        "howls, a junior colleague admits a worse typo, and the moment "
        "becomes team lore - belonging, banked. The simulation shows the "
        "entire database in motion: the five beats, the gradient, the "
        "display, the gold-standard repair, the aftershock handled, the "
        "story told first. This is what the archive is for: not just "
        "describing the feeling, but rehearsing the human through it."),
    how_it_works=(
        "The simulation is constructed as a teaching engine: each scene "
        "demonstrates specific records from this database, in ladder "
        "order. Scene one is the classic trigger (record 18) with maximum "
        "dials - high exposure, high stakes, powerful audience (record 3). "
        "Scene two runs the five beats (record 1), the time course's onset "
        "and peak (record 6), the full facial and postural display "
        "(records 14, 15, 11), and the low-vs-high snapshot (record 7). "
        "Scene three deploys the circuit breaker (record 21), the gold-"
        "standard repair (record 22), the recovery dialect (record 23), "
        "and the pre-decision script (records 26, 28) - the hinge of the "
        "whole piece, where training converts to performance. Scene four "
        "shows the witness program working correctly: amusement, not "
        "judgment (records 29, 30). Scene five is the aftershock handled "
        "by the book: noticed, reality-checked, lesson filed (records 6, "
        "12, 28). Scene six is the master move - telling it first (records "
        "9, 26) - converting replay material into social currency and "
        "closing the loop permanently. The simulation's deeper lesson is "
        "structural: at no point does Priya control the feeling - the "
        "blush comes regardless. Control was never the goal; authorship "
        "was. She authors the repair, the story, and the meaning, and "
        "that authorship is what the audience remembers. The feeling is "
        "weather; the person is the sailor. This record is the archive's "
        "showcase because it proves the database's promise: describe the "
        "feeling truly, simulate the human honestly, and the reader walks "
        "away rehearsed."),
    key_points=[
        "Six scenes: trigger, onset and peak, circuit breaker, aftermath, aftershock, resolution - the full arc in one narrative.",
        "Each scene demonstrates specific database records in ladder order - the simulation is the curriculum in motion.",
        "The hinge is scene three: the pre-decided script converting training into performance under arousal.",
        "The master move closes the piece: telling the story first converts replay material into belonging.",
        "The structural lesson: control of the feeling was never the goal; authorship of the repair, the story, and the meaning was.",
    ],
    requirements=[
        "Six scenes with times and concrete detail",
        "The five beats, gradient, display, and dials visible in the scenes",
        "The pre-decision script deployed at the hinge",
        "The aftershock handled by the book",
        "The authorship-vs-control closing lesson",
    ],
    standards=STD,
    citations=[CIT_MILLER, CIT_GOFFMAN, CIT_KELTNER, CIT_EDELMANN, CIT_APA],
    sig_lens=(
        "In the Signature lens, Priya's six scenes are the soul's hero "
        "journey in miniature - exposure, ordeal, return with the elixir. "
        "Signal: the blush was never the enemy; it was the call to "
        "adventure. Repair: the script, the breath, the story told first - "
        "these are the hero's tools, learnable by anyone. Mastery: the "
        "person who authors the meaning of their worst slide becomes the "
        "person the room trusts with the next one - for the soul's honest "
        "signal, once ridden, becomes its brightest credential.")),
]
