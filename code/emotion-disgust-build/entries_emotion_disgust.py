#!/usr/bin/env python3
"""Entries for the Disgust Emotion databases (Manon's 2026-10-17 16:15
emotion-series order, batch 1).

Verified 2026-10-17: RAW pre-check over the full manifest (2,442 databases)
plus every shard index file in jah-databases-data-1: prefixes JAH-EMDI-
(public) and JAH-EMDIS- (signature) return zero exact hits; the 68 planned
titles (34 + 34 Signature Edition) pass the whole-system dedupe gate with
zero collisions. No other emotion-* slugs exist in the manifest, so this is
the first database in the emotion series.

So this build creates two NEW databases, 34 ladder-ordered records each:

  emotion-disgust            - The Disgust Emotion Database
                               (public-harvest: real, fact-checked emotion
                               psychology - what disgust is, where it sits
                               in the emotion family, first-person
                               simulation, body signals, facial expression,
                               triggers, behavior, healthy expression,
                               recognizing it in others, related emotions
                               and mixes, full behavioral simulation;
                               standard references Darwin 1872; Rozin and
                               Fallon 1987; Rozin, Haidt and McCauley 1999;
                               Ekman 1999; Haidt, McCauley and Rozin 1994;
                               Miller 1997; Chapman et al. 2009; Tybur et
                               al. 2013)
  emotion-disgust-signature  - The Disgust Emotion Signature Database
                               (his original Signature Emotion Method: the
                               Signature system reads disgust as the first
                               and most honest boundary signal - the body's
                               original NO, the purity compass, the guardian
                               of the gates; each response a line drawn in
                               personal territory; src signature, titles
                               suffixed " (Signature Edition)", never
                               presented as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
non-decreasing; ladder_tier foundations/compounded/advanced); the shard
index is written in ladder order so pages present simple -> compounded ->
complex.

Descriptive and educational ONLY. Nothing here diagnoses any real person,
labels any real person with an emotional state, or offers therapy beyond
general, safe, everyday guidance. No clinical language, no hate-adjacent
content, no profanity, no religious talk.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature Emotion Method: the "
            "Signature system reads disgust as the first and most honest "
            "boundary signal, the body's original NO, the purity compass, "
            "the guardian of the gates. Clearly labeled Signature-made, never "
            "presented as authentic public record.")

CIT_DARWIN = ("Darwin C. The Expression of the Emotions in Man and Animals. "
              "John Murray; 1872.")
CIT_ROZIN_FALLON = ("Rozin P, Fallon AE. A perspective on disgust. "
                    "Psychological Review. 1987;94(1):23-41.")
CIT_ROZIN_HAIDT = ("Rozin P, Haidt J, McCauley CR. Disgust. In: Lewis M, "
                   "Haviland-Jones JM, eds. Handbook of Emotions. 2nd ed. "
                   "Guilford Press; 2000:637-653.")
CIT_EKMAN = ("Ekman P. Basic emotions. In: Dalgleish T, Power M, eds. "
             "Handbook of Cognition and Emotion. Wiley; 1999:45-60.")
CIT_HAIDT_DS = ("Haidt J, McCauley CR, Rozin P. Individual differences in "
                "sensitivity to disgust: A scale sampling seven domains of "
                "disgust elicitors. Personality and Individual Differences. "
                "1994;16(5):701-713.")
CIT_MILLER = ("Miller WI. The Anatomy of Disgust. Harvard University Press; "
              "1997.")
CIT_CHAPMAN = ("Chapman HA, Kim DA, Susskind JM, Anderson AK. In bad taste: "
               "Evidence for the oral origins of moral disgust. Science. "
               "2009;323(5918):1222-1226.")
CIT_TYBUR = ("Tybur JM, Lieberman D, Kurzban R, DeScioli P. Disgust: Evolved "
             "function and structure. Psychological Review. "
             "2013;120(1):65-84.")

ENTRIES = [
    # ---------------- What the emotion IS (records 1-4) ----------------
    {
        "key": "what-is",
        "name": "What Disgust Is: A Plain-Language Definition",
        "group": "Description",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Disgust is the feeling of strong distaste and rejection - the "
            "body and mind saying NO to something offensive. At its root it is "
            "a protective alarm. Long before people had words for germs, the "
            "body learned to recognize the signs of things that could poison, "
            "infect, or contaminate it: rotten food, foul smells, bodily "
            "waste, wounds, decay. Disgust is the system that pushes those "
            "things away, out, and off. It shows up as a turning away - of "
            "the nose, the face, the stomach, the whole body - and as the "
            "urge to expel: spit it out, wash it off, leave the room. That is "
            "the core of it, the original distaste that researchers call "
            "\"core disgust.\" From that seed, the same feeling grew outward. "
            "The same wrinkle of the nose that rejects spoiled milk came to "
            "reject bad company, broken rules, and cruelty. Psychologists "
            "describe disgust as the guardian of the body AND the guardian "
            "of the soul: it keeps harmful substances out of the mouth and, "
            "in its expanded form, keeps harmful ideas and acts out of the "
            "community. It is one of the basic emotions - present across "
            "cultures, visible on the face in the same way everywhere, and "
            "felt in the body before thought catches up. Disgust is not "
            "hatred, not anger, and not fear, though it often travels with "
            "them. It is simpler and older: this does not belong in me, near "
            "me, or among us. Get it away."),
        "how_it_works": (
            "A trigger is detected by the senses - smell, taste, sight, "
            "touch - and the alarm fires almost instantly. The stomach "
            "churns, the throat tightens, the nose wrinkles, the upper lip "
            "lifts, the head turns away. The body prepares to expel and to "
            "avoid. Meanwhile the mind tags the trigger as contaminated: "
            "even a clean version of it can keep feeling tainted, which is "
            "why the feeling lingers after the trigger is gone. The same "
            "circuit can fire on non-physical triggers - a cruel act, a "
            "broken taboo - producing the same rejection urge directed at "
            "behavior instead of food."),
        "key_points": [
            "Disgust is a rejection response: the body and mind pushing something offensive away, out, or off.",
            "Its original job is protection - keeping poisons, infections, and contaminants out of the body.",
            "The same feeling expanded from food and smells to bodies, hygiene, other people, and moral acts.",
            "It is one of the basic emotions: universal, recognizable on the face across cultures, felt in the body first.",
            "Disgust is not hatred, anger, or fear - it is the simpler, older message: this does not belong here.",
            "The contamination tag outlasts the trigger: the feeling can linger after the offensive thing is gone."],
        "requirements": [
            "No equipment needed - this is a reading and reflection record.",
            "A few quiet minutes to sit with the definition.",
            "Willingness to notice the feeling in everyday moments."],
        "standards": [
            "Public record in the Signature system: fact-checked emotion psychology.",
            "Descriptive and educational only - never diagnoses any real person.",
            "Human-readable sentences and paragraphs throughout."],
        "citations": [CIT_DARWIN, CIT_ROZIN_FALLON, CIT_EKMAN],
        "sig_lens": (
            "Signature lens: his Signature system reads disgust as the first "
            "and most honest boundary signal - the body's original NO, drawn "
            "long before words arrive. Where the public record maps triggers "
            "and faces, the Signature Edition treats every disgust response "
            "as a line drawn in personal territory: what enters, what stays "
            "out, what is kept clean. The archivist's move is simple - honor "
            "the signal, read the line, keep the gates working."),
    },
    {
        "key": "family",
        "name": "Where Disgust Sits in the Emotion Family",
        "group": "Description",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "In the family of emotions, disgust is a basic emotion - one of "
            "the small set of feelings that appear across cultures with the "
            "same facial signature and the same body pattern. It sits on the "
            "unpleasant side of the map, among the negative basics: anger, "
            "fear, sadness, and disgust. Each of these answers a different "
            "ancient question. Fear answers danger: something might hurt me. "
            "Anger answers blocked goals: something stands in my way. "
            "Sadness answers loss: something I valued is gone. Disgust "
            "answers contamination: something offensive is too close, in me, "
            "or among us. Researchers trace how the basic seed - distaste, "
            "the rejection of bad food - grew into a family of its own: "
            "animal-reminder disgust (reminders that we are bodies, "
            "vulnerable and mortal), interpersonal disgust (aversion to "
            "contact with certain people), and moral disgust (rejection of "
            "cruelty, cheating, and broken trust). The near neighbors matter: "
            "contempt is the cold, hierarchical cousin that looks down from "
            "above, while disgust pushes away at arm's length; anger wants "
            "to confront, while disgust wants distance. Plutchik's emotion "
            "map places disgust opposite trust and acceptance - the one pulls "
            "away what the other takes in. Complex emotions grow from it: "
            "outrage blends disgust with anger, horror blends it with fear, "
            "shame turns the rejection inward on the self. Knowing where "
            "disgust sits is practical: it tells you which tools fit. You "
            "do not fight disgust the way you fight fear - you do not "
            "confront it; you distance, you clean, you restore the boundary."),
        "how_it_works": (
            "The family map works like a neighborhood: basic emotions are "
            "the original houses, and complex emotions are built from pairs "
            "of them. Disgust's house stands on the avoidance side - its "
            "default action is always to increase distance. When another "
            "emotion moves in next door, the blend takes on a new name but "
            "keeps disgust's push-away character: add anger and the push "
            "becomes a shove (outrage); add fear and the shove becomes a "
            "flight (horror). Reading the blend correctly is the skill: "
            "name both ingredients and the action urge becomes clear."),
        "key_points": [
            "Disgust is a basic emotion, alongside anger, fear, and sadness, with a universal face and body pattern.",
            "It answers the contamination question: something offensive is too close, in me, or among us.",
            "It grew from food distaste into animal-reminder, interpersonal, and moral forms.",
            "Contempt is the cold hierarchical cousin (looks down); anger confronts while disgust distances.",
            "On Plutchik's map it sits opposite trust and acceptance - pull-away versus take-in.",
            "Complex blends keep its push-away character: outrage (plus anger), horror (plus fear), shame (turned inward)."],
        "requirements": [
            "No equipment needed - this is a reading and reflection record.",
            "Curiosity about how feelings relate to each other.",
            "A few quiet minutes to trace the family lines."],
        "standards": [
            "Public record in the Signature system: fact-checked emotion psychology.",
            "Descriptive and educational only - never diagnoses any real person.",
            "Human-readable sentences and paragraphs throughout."],
        "citations": [CIT_EKMAN, CIT_ROZIN_HAIDT, CIT_TYBUR],
        "sig_lens": (
            "Signature lens: his Signature system files disgust at the "
            "boundary gate of the emotion family - the guard post all other "
            "feelings pass through. The Signature reader asks of any blend: "
            "which ingredient is drawing the line? Follow the push-away "
            "urge and the map reads itself. The archivist keeps the family "
            "chart posted at the gate: know the neighbors and you will "
            "never mistake the signal."),
    },
    {
        "key": "intensity",
        "name": "How Strong Disgust Can Get: Mild to Intense",
        "group": "Description",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Disgust is not one fixed feeling - it is a volume knob that "
            "turns from a whisper to a scream. At the mild end it is little "
            "more than distaste: a slight nose wrinkle at a strange smell, a "
            "quiet \"not for me\" at an unfamiliar dish, a small lean-back "
            "from a messy table. The body barely moves; the mind simply "
            "files the thing under \"avoid.\" Turn the knob to the middle "
            "and the feeling gets physical: active nausea, the throat "
            "tightening, the head turning away on its own, words coming out "
            "unbidden - \"ugh,\" \"gross.\" The person steps back, puts the "
            "thing down, washes hands. At the intense end disgust takes over "
            "the whole system: gagging or retching, revulsion so strong the "
            "person cannot look, cannot stay, cannot even think about the "
            "trigger without the wave coming back. At this level the "
            "contamination tag spreads - the room feels tainted, the memory "
            "replays, the appetite is gone for hours. The same emotion runs "
            "all three levels; only the volume changes. Two things make the "
            "knob turn up: the trigger itself (how foul, how close, how "
            "inescapable) and the person (sensitivity varies widely - some "
            "people gag at a bruised apple, others clean hospital wards "
            "without flinching). The ladder matters because the response "
            "must match the level. Mild distaste needs only a small "
            "adjustment - skip the dish, open a window. Intense revulsion "
            "needs real distance and real recovery time. Treating a whisper "
            "like a scream exhausts people; treating a scream like a "
            "whisper breaks trust in the signal."),
        "how_it_works": (
            "Intensity rides two rails: trigger strength (how offensive, how "
            "close, how long the exposure) and personal sensitivity (how "
            "low the person's alarm threshold sits). The rails multiply: a "
            "strong trigger on a sensitive person peaks fast and fades "
            "slow. The body signals stack as the knob turns - face first, "
            "then stomach, then the whole posture - so reading the level is "
            "a matter of counting how many systems have joined in."),
        "key_points": [
            "Disgust runs on a volume knob: mild distaste, moderate nausea and avoidance, intense revulsion.",
            "The same emotion at every level - only the volume changes, from whisper to scream.",
            "The knob turns on two rails: trigger strength and personal sensitivity.",
            "Body signals stack with intensity: face first, then stomach, then full posture.",
            "The contamination tag spreads at high intensity: rooms, memories, and appetites stay tainted.",
            "Match the response to the level: small adjustments for whispers, real distance and recovery for screams."],
        "requirements": [
            "No equipment needed - this is a reading and reflection record.",
            "Memory of a mild and a strong disgust moment to compare.",
            "A few quiet minutes."],
        "standards": [
            "Public record in the Signature system: fact-checked emotion psychology.",
            "Descriptive and educational only - never diagnoses any real person.",
            "Human-readable sentences and paragraphs throughout."],
        "citations": [CIT_HAIDT_DS, CIT_ROZIN_HAIDT],
        "sig_lens": (
            "Signature lens: his Signature system reads intensity as the "
            "alarm's volume setting, not a different alarm. The Signature "
            "archivist calibrates by counting joined systems - face, "
            "stomach, posture - the way a watchman counts lit watchtowers. "
            "One tower lit: note it and move on. All towers lit: give the "
            "territory real distance and real recovery. Calibration is the "
            "whole art of the gate."),
    },
    {
        "key": "myths",
        "name": "Common Myths About Disgust",
        "group": "Description",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Disgust collects myths the way a kitchen collects smells, and "
            "most of them get in the way of understanding it. Myth one: "
            "disgust is only about food. In fact the same circuit fires for "
            "wounds, decay, poor hygiene, unwanted contact, and moral "
            "violations - food was only the first classroom. Myth two: only "
            "weak or squeamish people feel it. Disgust is universal; even "
            "surgeons and sanitation workers feel it, they have simply "
            "trained their response, not erased the signal. Myth three: you "
            "can reason it away in a moment. Reason helps, but the "
            "contamination tag is stubborn - people will refuse a sterilized "
            "object that once touched something foul, knowing full well it "
            "is clean. The feeling outruns the facts. Myth four: disgust is "
            "always a problem to fix. Often it is working exactly as "
            "designed - keeping a person from eating something unsafe or "
            "tolerating something cruel. The problem is not the signal but "
            "the misfire: disgust aimed at the wrong target. Myth five: "
            "everyone is disgusted by the same things. Sensitivity varies "
            "enormously across people and cultures - foods one table "
            "treasures, another table cannot face. Myth six: feeling disgust "
            "makes you a bad or judgmental person. The feeling is "
            "information; what a person DOES with it - whether they clean "
            "the kitchen or shame a neighbor - is the part that counts. "
            "Clearing the myths leaves the clean truth: disgust is a normal, "
            "universal, protective signal, variable in volume, sometimes "
            "misaimed, and always worth reading before acting on."),
        "how_it_works": (
            "Each myth works by shrinking disgust into a caricature - "
            "childish, weak, irrational, or uniform. The correction in every "
            "case is the same move: widen the frame. Disgust is broader "
            "than food, stronger than squeamishness, stickier than logic, "
            "more useful than its reputation, more variable than its myths, "
            "and morally neutral as a signal. Test any claim about disgust "
            "against those six corrections and the myths fall away."),
        "key_points": [
            "Myth: only about food. Fact: the circuit fires for wounds, decay, hygiene, contact, and moral acts too.",
            "Myth: only weak people feel it. Fact: universal - trained people manage the response, not the signal.",
            "Myth: reason erases it instantly. Fact: the contamination tag outruns the facts.",
            "Myth: always a problem. Fact: often working as designed; the issue is misfire, not the signal.",
            "Myth: same triggers for everyone. Fact: sensitivity varies widely across people and cultures.",
            "Myth: feeling it makes you judgmental. Fact: the feeling is information - the action is what counts."],
        "requirements": [
            "No equipment needed - this is a reading and reflection record.",
            "Willingness to test old assumptions.",
            "A few quiet minutes."],
        "standards": [
            "Public record in the Signature system: fact-checked emotion psychology.",
            "Descriptive and educational only - never diagnoses any real person.",
            "Human-readable sentences and paragraphs throughout."],
        "citations": [CIT_ROZIN_FALLON, CIT_MILLER, CIT_HAIDT_DS],
        "sig_lens": (
            "Signature lens: his Signature system treats each myth as fog on "
            "the watchtower glass. The Signature archivist wipes the glass "
            "with one question: is this claim about the signal or about the "
            "person? The signal is never weak, never childish, never broken "
            "- it is data. Fog cleared, the gate reads true again."),
    },
    # ---------------- How it feels (records 5-9) ----------------
    {
        "key": "first-person",
        "name": "Inside the Feeling: A First-Person Account of Disgust",
        "group": "Inner Experience",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "This is what disgust feels like from the inside, in the first "
            "person. It starts before words. You smell it or see it and your "
            "face moves on its own - nose scrunching, lip curling up like "
            "you are about to spit something out. Your stomach drops a "
            "notch, like the first dip of a ride, and your throat gets "
            "narrow. The thought arrives a half-second late: oh no. Then "
            "the urge, loud and simple: get it away from me. Your head turns "
            "before you decide to turn it. Your hand pulls back. If it is "
            "in your mouth, everything stops - chewing freezes, and the "
            "whole body organizes around one project: out. There is a wave "
            "quality to it, rising fast, and a strange focus: the offensive "
            "thing fills the whole frame. The room around it goes blurry. "
            "You can feel your skin wanting distance - a crawl along the "
            "arms, a wish to be somewhere else, anywhere else. Words come "
            "out small and clipped: no. Ugh. Get that away. If you have to "
            "stay near it - a chore, a duty - part of your mind holds its "
            "breath the whole time, counting down until you can leave and "
            "wash. Afterward there is a residue, like a smell that follows "
            "you out of the room. You replay it once, twice, and each "
            "replay brings a smaller echo of the wave. Then it settles, "
            "leaving a quieter instruction filed away: not that. Never "
            "that again. This is not a report about someone else's feeling. "
            "It is a simulation - a described passage so the archive can "
            "hold what the inside of the alarm sounds like."),
        "how_it_works": (
            "The first-person account is built from the known sequence: "
            "sensory detection, automatic facial and stomach response, the "
            "cognitive label arriving late, the expulsion and avoidance "
            "urge, narrowed attention on the trigger, clipped speech, and "
            "the lingering contamination echo. Read it as a walkthrough of "
            "the mechanism, not a diagnosis of any real person."),
        "key_points": [
            "Disgust starts before words: the face and stomach react first, the label arrives a half-second late.",
            "The core urge is simple and loud: get it away from me - expel it, leave it, wash it off.",
            "Attention narrows: the offensive thing fills the whole frame while the room goes blurry.",
            "Speech gets small and clipped: no, ugh, get that away.",
            "Enduring it means holding your breath mentally - counting down until you can leave and wash.",
            "A residue follows: replays bring smaller echoes, and a quiet instruction files away - never that again."],
        "requirements": [
            "No equipment needed - this is a reading and simulation record.",
            "Read slowly; let the sequence play like a scene.",
            "Remember this describes a feeling, not any real person."],
        "standards": [
            "Public record in the Signature system: fact-checked emotion psychology.",
            "Descriptive and educational only - a simulation, never a diagnosis.",
            "Human-readable sentences and paragraphs throughout."],
        "citations": [CIT_ROZIN_HAIDT, CIT_DARWIN],
        "sig_lens": (
            "Signature lens: his Signature system keeps this passage in the "
            "first person on purpose - the gate's own logbook, written from "
            "the watchtower floor. The Signature archivist reads it the way "
            "a commander reads a sentry's report: not as a verdict on the "
            "sentry, but as ground truth about the territory. This is what "
            "the alarm sounds like from inside the walls."),
    },
    {
        "key": "arc",
        "name": "The Arc of Disgust: Onset, Peak, and Fading",
        "group": "Inner Experience",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "Disgust has a shape in time - an arc with four phases. Phase "
            "one is onset, and it is fast. From trigger to full alarm takes "
            "about one to three seconds: the smell hits, the face twists, "
            "the stomach drops. There is almost no ramp-up; the system was "
            "built for speed because poisons do not wait. Phase two is the "
            "peak, lasting seconds to a few minutes while the trigger is "
            "present. This is the wave at its highest - gagging, revulsion, "
            "the urgent need for distance. The body is fully recruited: "
            "face, throat, stomach, posture, all saying the same thing. "
            "Phase three is fading, and it begins the moment real distance "
            "is achieved - the trigger is gone, spat out, washed off, left "
            "behind. The wave falls quickly at first, then slowly: minutes "
            "for the stomach to settle, longer for the appetite to return. "
            "Phase four is the aftershock, the part people underestimate. "
            "Hours later, a memory of the trigger - a photo, a mention, a "
            "similar smell - can summon a smaller echo of the wave. The "
            "contamination tag keeps a long half-life. A place can feel "
            "tainted for a day; a food can be off the menu for a year. The "
            "arc teaches two practical lessons. First, do not judge the "
            "feeling at the peak - it is designed to be overwhelming; judge "
            "it in the fading, when the information remains and the alarm "
            "quiets. Second, respect the aftershock: plan for echoes "
            "instead of being ambushed by them. The arc is the same whether "
            "the trigger is spoiled food or a moral violation - only the "
            "timescale of the aftershock changes, with moral disgust "
            "echoing longest of all."),
        "how_it_works": (
            "The arc follows the alarm logic: instant onset (speed beats "
            "accuracy for poisons), a peak sustained while exposure lasts, "
            "fading once distance is real, and a long-tail aftershock from "
            "the contamination tag stored in memory. Each phase has its own "
            "job: detect, recruit, recover, remember. The simulator demo "
            "models this as a curve - steep rise, plateau, exponential "
            "decay with echo bumps."),
        "key_points": [
            "Onset is nearly instant (1-3 seconds) - the alarm was built for speed, not deliberation.",
            "The peak lasts while the trigger is present: full-body recruitment, gagging, urgent distance.",
            "Fading begins with real distance - fast drop first, then a slow settle of stomach and appetite.",
            "The aftershock is the long tail: memories and reminders summon smaller echoes for hours or days.",
            "Moral disgust echoes longest; food disgust fades fastest once the body is clear.",
            "Judge the feeling in the fading, not the peak - and plan for echoes instead of being ambushed."],
        "requirements": [
            "No equipment needed - this is a reading and simulation record.",
            "Trace a past disgust moment through the four phases.",
            "A few quiet minutes."],
        "standards": [
            "Public record in the Signature system: fact-checked emotion psychology.",
            "Descriptive and educational only - never diagnoses any real person.",
            "Human-readable sentences and paragraphs throughout."],
        "citations": [CIT_ROZIN_FALLON, CIT_ROZIN_HAIDT],
        "sig_lens": (
            "Signature lens: his Signature system maps the arc as the "
            "watchtower's own shift log - alarm raised, full muster, "
            "stand-down, then the long watch after. The Signature archivist "
            "marks the aftershock phase with a flag: this is where most "
            "people misread the territory, mistaking an echo for a new "
            "alarm. Log the echo, do not re-muster for it."),
    },
    {
        "key": "low-vs-high",
        "name": "Disgust at Low Intensity vs High Intensity",
        "group": "Inner Experience",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "The same alarm at two volumes - here are the two lived "
            "snapshots side by side. LOW: You open the refrigerator and "
            "catch a faint sour note from the milk. Your nose wrinkles "
            "slightly. You sniff once more, decide it is borderline, and "
            "pour it out without drama. Your stomach does nothing at all. "
            "You make tea instead and forget about it in ten minutes. The "
            "whole event costs you thirty seconds and one small "
            "adjustment. Words in your head: \"nope, not that one.\" HIGH: "
            "You lift the lid of a trash can that has sat in summer heat "
            "for a week. The smell hits like a wall. Your face twists "
            "before you can stop it, your throat clamps, your stomach "
            "heaves, and you slam the lid and step back gasping, eyes "
            "watering. You can still smell it on your hands after washing "
            "them twice. Lunch is out of the question. For the rest of the "
            "afternoon, the memory of the smell floats up uninvited and "
            "each time your stomach tightens a notch. Words in your head: "
            "none - just the wave, and then \"never again.\" Notice what "
            "changed between the snapshots. At low volume the feeling is a "
            "note in the margin - noticed, handled, filed. At high volume "
            "it is the whole page - body recruited, attention captured, "
            "aftermath measured in hours. The trigger category did not "
            "change - both were spoiled things. Only the strength of the "
            "signal changed, and with it everything: the number of body "
            "systems involved, the duration, the contamination spread, the "
            "words available (plenty at low, none at high). This is why "
            "intensity is the first thing to read. Two people can meet the "
            "same trigger and live in different snapshots - and each one's "
            "response is proportionate to the volume they actually heard."),
        "how_it_works": (
            "The two snapshots are the same mechanism at different signal "
            "strengths. Low volume recruits only the face and a decision; "
            "high volume recruits throat, stomach, posture, attention, and "
            "memory. The comparison works as a calibration tool: match your "
            "experience to the nearer snapshot and you know how much "
            "response the level actually calls for."),
        "key_points": [
            "Low intensity is a margin note: noticed, handled with a small adjustment, forgotten in minutes.",
            "High intensity is the whole page: body recruited, attention captured, aftermath measured in hours.",
            "Same trigger category can produce either snapshot - signal strength is what changes.",
            "More volume means more systems: face only at low, throat, stomach, posture, and memory at high.",
            "Words are plentiful at low volume and vanish at high - the wave replaces language.",
            "Calibrate by matching your experience to the nearer snapshot, then respond to that level."],
        "requirements": [
            "No equipment needed - this is a reading and simulation record.",
            "Recall one mild and one strong disgust moment for comparison.",
            "A few quiet minutes."],
        "standards": [
            "Public record in the Signature system: fact-checked emotion psychology.",
            "Descriptive and educational only - never diagnoses any real person.",
            "Human-readable sentences and paragraphs throughout."],
        "citations": [CIT_HAIDT_DS, CIT_EKMAN],
        "sig_lens": (
            "Signature lens: his Signature system keeps both snapshots "
            "posted side by side at the gate, like a tide chart. The "
            "Signature archivist's rule: never judge a high-tide response "
            "by low-tide standards, and never spend high-tide effort on a "
            "low-tide signal. Two snapshots, one alarm - calibration is "
            "the discipline."),
    },
    {
        "key": "mixed-anger",
        "name": "Disgust Mixed with Anger",
        "group": "Inner Experience",
        "ladder_rank": 5,
        "ladder_tier": "foundations",
        "description": (
            "Disgust rarely travels alone, and its most common companion is "
            "anger. The blend has its own weather. Pure disgust says: get "
            "this away from me. Pure anger says: this wrong must be "
            "confronted. Put them together and you get: this foul thing "
            "must be driven out and answered for. The body shows both "
            "ingredients at once - the nose wrinkle and raised upper lip of "
            "disgust alongside the lowered brow and tightened jaw of anger; "
            "the lean-back of rejection fighting the lean-forward of "
            "attack. Inside, it feels like heat and nausea at the same "
            "time: the stomach churns while the chest tightens, the urge to "
            "spit something out tangled with the urge to say something "
            "sharp. This is the texture of moral outrage - the feeling that "
            "rises at cruelty, cheating, betrayal. The disgust ingredient "
            "supplies the contamination logic (this person, this act, is "
            "tainted), and the anger ingredient supplies the action logic "
            "(someone must pay, something must change). The blend is "
            "powerful and it is risky, because each ingredient hides the "
            "other's limits: anger borrows disgust's certainty (\"this is "
            "objectively foul\"), and disgust borrows anger's license to "
            "strike. The healthy move is to name both ingredients out loud. "
            "\"I am disgusted by what happened AND angry about it\" is a "
            "sentence that keeps the two urges honest: the disgust urge gets "
            "its distance and cleanup, the anger urge gets its words and "
            "boundaries, and neither gets to pretend it is the other. "
            "Blends are not malfunctions - they are the normal weather of a "
            "complex moment. Reading them ingredient by ingredient is the "
            "skill that keeps them from running the show."),
        "how_it_works": (
            "The blend works by addition: disgust contributes rejection, "
            "contamination tagging, and the push-away urge; anger "
            "contributes confrontation, blame, and the push-forward urge. "
            "The mixture's action tendency - drive out and hold "
            "accountable - is literally the sum. Naming the ingredients "
            "separates the urges so each can be answered appropriately."),
        "key_points": [
            "Disgust plus anger is the most common blend - the texture of moral outrage.",
            "Pure disgust says get it away; pure anger says confront it; the blend says drive it out and answer for it.",
            "The body shows both: nose wrinkle and raised lip alongside lowered brow and tight jaw.",
            "Inside it feels like heat and nausea together - the urge to spit tangled with the urge to speak sharp.",
            "The risk: each ingredient hides the other's limits - certainty borrowed one way, license the other.",
            "Name both ingredients out loud so each urge gets its honest answer: distance for disgust, words for anger."],
        "requirements": [
            "No equipment needed - this is a reading and simulation record.",
            "Recall a moment of outrage and test the two-ingredient read.",
            "A few quiet minutes."],
        "standards": [
            "Public record in the Signature system: fact-checked emotion psychology.",
            "Descriptive and educational only - never diagnoses any real person.",
            "Human-readable sentences and paragraphs throughout."],
        "citations": [CIT_CHAPMAN, CIT_ROZIN_HAIDT],
        "sig_lens": (
            "Signature lens: his Signature system files this blend as a "
            "two-alarm fire - the boundary gate and the war horn sounding "
            "together. The Signature archivist's drill is naming: call out "
            "\"gate\" and \"horn\" separately, answer each by its own "
            "protocol - distance and cleanup for the gate, words and "
            "boundaries for the horn. Two alarms answered rightly beat one "
            "alarm answered twice."),
    },
    {
        "key": "day-in-life",
        "name": "Disgust Through an Ordinary Day",
        "group": "Inner Experience",
        "ladder_rank": 5,
        "ladder_tier": "foundations",
        "description": (
            "Follow the alarm through one ordinary day and see how often it "
            "quietly does its job. 7:10 AM: you open the bathroom cabinet "
            "and the drain smells off. Nose wrinkles, you make a note to "
            "clean it Saturday, move on. Cost: five seconds. 8:40 AM: on "
            "the bus, someone's strong food smell fills your row. You turn "
            "your face toward the window, breathe through your mouth, shift "
            "one seat over at the next stop. No drama - the body handled it. "
            "12:15 PM: a coworker's leftover fish reheats in the office "
            "microwave. The whole break room leans back as one. Someone "
            "laughs, someone opens a window, the moment passes and becomes "
            "a small joke. 3:30 PM: you read a news story about a company "
            "dumping waste in a river. No smell, no taste - but the same "
            "nose-wrinkle, the same \"that's foul,\" now aimed at an act "
            "instead of a substance. You feel the push-away urge with "
            "nowhere physical to push. 6:00 PM: cooking dinner, you find a "
            "soft spot on a tomato. You cut it away generously, wash your "
            "hands, sniff the rest. The meal is saved; the tomato's "
            "contamination tag stays on the cut piece, which goes in the "
            "trash. 9:20 PM: scrolling, you see a photo of a wound from a "
            "friend's hiking accident. You look away fast, thumb moving on "
            "instinct, stomach giving one small roll. You text \"hope it "
            "heals fast\" without looking again. None of these moments "
            "became a crisis. That is the point. Disgust is not a rare "
            "emergency - it is a background sense, like balance, firing a "
            "dozen small corrections a day. The day-in-the-life view shows "
            "the alarm doing quiet, competent work: notice, adjust, file, "
            "move on. Problems only start when the small corrections stop "
            "working - when the smell will not leave, the memory will not "
            "fade, or the signal gets aimed at the wrong target."),
        "how_it_works": (
            "The vignette strings six small triggers across a day to show "
            "the alarm's normal operating rhythm: detect, micro-adjust, "
            "release. Each scene isolates one domain - hygiene, food, "
            "interpersonal, moral, contamination logic, visual - proving "
            "the same circuit serves them all. The closing turn names the "
            "failure modes: stuck signals and misaimed signals."),
        "key_points": [
            "Disgust fires a dozen small corrections on an ordinary day - it is a background sense, not a rare emergency.",
            "The normal rhythm is detect, micro-adjust, release: five seconds, one seat over, one open window.",
            "The same circuit serves smells, food, other people, photos, and moral acts.",
            "Most moments resolve cleanly and even become small jokes - the system is competent at low volume.",
            "Problems start when corrections stop working: the smell will not leave, the memory will not fade.",
            "A misaimed signal - disgust at the wrong target - is the failure mode to watch for."],
        "requirements": [
            "No equipment needed - this is a reading and simulation record.",
            "Try noticing the small corrections in your own next day.",
            "A few quiet minutes."],
        "standards": [
            "Public record in the Signature system: fact-checked emotion psychology.",
            "Descriptive and educational only - never diagnoses any real person.",
            "Human-readable sentences and paragraphs throughout."],
        "citations": [CIT_ROZIN_HAIDT, CIT_TYBUR],
        "sig_lens": (
            "Signature lens: his Signature system calls this the gate's "
            "daily patrol log - unglamorous, constant, essential. The "
            "Signature archivist honors the small corrections: a territory "
            "stays clean not by one great battle but by a hundred tiny "
            "adjustments nobody applauds. Read the patrol log and you "
            "understand the gate better than any single alarm ever teaches."),
    },
    # ---------------- Body signals (records 10-13) ----------------
    {
        "key": "body-signals",
        "name": "What Happens in the Body: The Disgust Response",
        "group": "Body Signals",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "When disgust fires, the body runs a coordinated rejection "
            "program, and it runs it in a particular order. First the face: "
            "the nose wrinkles, the upper lip lifts, the brows lower - the "
            "gates of the senses narrowing against entry. Then the throat: "
            "a tightening, sometimes a gag, the swallow reflex interrupted "
            "as if the body is deciding whether anything should go down at "
            "all. Then the stomach: the signature move of disgust - churning, "
            "dropping, heaving. Nausea is the stomach voting no. Saliva "
            "changes too, first increasing (the mouth preparing to spit) "
            "and then drying up as the wave passes. The heart does "
            "something unusual here: while most negative emotions speed it "
            "up, strong disgust can slow it down - the parasympathetic "
            "brake engaging, which is why people sometimes feel faint or "
            "pale rather than flushed. Blood leaves the face; the skin goes "
            "pale and cool, sometimes clammy. The gut and the throat are the "
            "headquarters, but the skin reports in as well - the crawl, the "
            "shiver, the wish to be elsewhere made physical. Energy drains "
            "rather than surges: disgust rarely produces the hot rush of "
            "anger or the trembling of fear. It produces a cold, heavy "
            "wish for distance. After the peak, the body runs cleanup: deep "
            "breaths, swallowing, hand-washing, the slow return of the "
            "stomach. Knowing the program matters because the body keeps "
            "its own score - a person can say \"I'm fine\" while their "
            "throat is still tight and their stomach still unsettled. The "
            "body's report is the honest one; the words catch up later."),
        "how_it_works": (
            "The rejection program is staged: sensory gates narrow first "
            "(face), then the entry tube objects (throat), then the "
            "processing chamber votes no (stomach), with the parasympathetic "
            "brake slowing the heart - the opposite of fight-or-flight. "
            "Each stage maps to an evolutionary job: keep it out of the "
            "eyes and nose, keep it out of the mouth, get it out of the "
            "gut. Read the stages in order and you can tell how far the "
            "alarm has traveled through the body."),
        "key_points": [
            "The program runs in order: face narrows the senses, throat objects, stomach votes no.",
            "Nausea is the stomach's vote - the signature body signal of disgust.",
            "Saliva first increases (preparing to spit) then dries as the wave passes.",
            "Unlike most negative emotions, strong disgust can SLOW the heart - the parasympathetic brake.",
            "Blood leaves the face: pallor, coolness, sometimes clamminess instead of flushing.",
            "The body keeps its own score - throat tight and stomach unsettled mean the wave has not finished."],
        "requirements": [
            "No equipment needed - this is a reading and reflection record.",
            "Notice the staged order in your next strong reaction.",
            "A few quiet minutes."],
        "standards": [
            "Public record in the Signature system: fact-checked emotion psychology.",
            "Descriptive and educational only - never diagnoses any real person.",
            "Human-readable sentences and paragraphs throughout."],
        "citations": [CIT_ROZIN_HAIDT, CIT_CHAPMAN],
        "sig_lens": (
            "Signature lens: his Signature system reads the body program "
            "as the gate's muster order - towers lighting in sequence, "
            "face, throat, stomach, skin. The Signature archivist drills "
            "the order until it is reflex: count the lit towers and you "
            "know the alarm's depth without asking the words, because the "
            "words always arrive late and sometimes lie."),
    },
    {
        "key": "posture",
        "name": "The Posture and Movement Signature of Disgust",
        "group": "Body Signals",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Disgust has a posture, and once you know it you can read it "
            "from across a room. The master move is withdrawal: the torso "
            "leans back, the head turns away, the chin tucks slightly as if "
            "to narrow every opening. Where fear crouches and anger "
            "advances, disgust retreats - not in panic but in refusal. The "
            "hands tell the story next. They push: palms out, a warding "
            "gesture, the universal \"stop, keep it away.\" Or they cover: "
            "hand over mouth and nose, the body's own mask. Or they busy "
            "themselves with distance - picking up the offending thing with "
            "fingertips, at arm's length, carrying it like it might bite. "
            "Gait changes too. A person walking past something disgusting "
            "will arc around it, giving it a wide berth without thinking; "
            "the path bends before the mind decides. Speed drops near the "
            "trigger (careful, don't touch) and rises after passing it "
            "(leave the zone). There is also the freeze - a half-second "
            "stillness at the first whiff or sight, the system taking its "
            "reading before committing to the retreat. At low intensity the "
            "signature shrinks to micro-moves: a fractional lean-back, a "
            "slight turn of the head, fingers drumming a small distance on "
            "the table. Actors and animators study this vocabulary because "
            "it reads instantly: show a character leaning back with a hand "
            "half-raised and every audience on earth knows the feeling "
            "without a word of dialogue. The posture is honest in a useful "
            "way - people can school their faces, but the lean-back and the "
            "wide berth usually survive the schooling."),
        "how_it_works": (
            "The movement signature is the avoidance urge made visible: "
            "every joint increases distance between the body and the "
            "trigger. Freeze (assess), lean-back (withdraw), push or cover "
            "(guard the gates), arc around (route planning), accelerate "
            "away (exit). The sequence is the body's evacuation drill, "
            "rehearsed ten thousand times since childhood."),
        "key_points": [
            "The master move is withdrawal: torso leans back, head turns away, chin tucks to narrow every opening.",
            "Fear crouches and anger advances; disgust retreats - not in panic but in refusal.",
            "Hands push (palms out), cover (over mouth and nose), or carry at arm's length with fingertips.",
            "Paths bend unconsciously: people arc wide around disgusting things without deciding to.",
            "A half-second freeze at first contact is the system taking its reading before the retreat.",
            "The posture survives face-schooling - the lean-back and the wide berth are the honest tells."],
        "requirements": [
            "No equipment needed - this is a reading and reflection record.",
            "Watch for the lean-back and the arc in everyday crowds.",
            "A few quiet minutes."],
        "standards": [
            "Public record in the Signature system: fact-checked emotion psychology.",
            "Descriptive and educational only - never diagnoses any real person.",
            "Human-readable sentences and paragraphs throughout."],
        "citations": [CIT_DARWIN, CIT_EKMAN],
        "sig_lens": (
            "Signature lens: his Signature system reads posture as the "
            "gate's ground truth - the walls themselves moving. A face can "
            "be trained to lie; a torso leaning back is the territory "
            "speaking. The Signature archivist trusts the lean, the arc, "
            "and the half-raised hand over any polished expression. Watch "
            "the ground, not the banners."),
    },
    {
        "key": "sleep-appetite",
        "name": "Sleep, Appetite, and Energy Under Disgust",
        "group": "Body Signals",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Disgust reaches past the moment and into the body's daily "
            "economy - appetite first, then energy, then sleep. Appetite is "
            "the direct casualty. The same stomach that voted no does not "
            "reopen for business on command: after a strong wave, food "
            "looks wrong for hours. Even the thought of eating can restart "
            "a smaller echo. This is the system working as designed - a "
            "body that just rejected something does not trust the next "
            "thing yet. The appetite usually returns in stages: first "
            "bland and plain foods become acceptable, then normal eating "
            "resumes, often by the next day. Energy drains rather than "
            "spikes. Sustained disgust - a bad smell that will not leave, a "
            "memory that replays - is tiring in a particular heavy way, "
            "like carrying something. People describe feeling \"drained\" "
            "or \"weighed down\" rather than wired. Sleep takes the hit "
            "indirectly. The trigger itself rarely keeps people awake; the "
            "replay does. A disgusting experience reviewed at bedtime - the "
            "smell, the image, the moral violation - can loop, and each "
            "loop brings a small stomach-tightening that pushes sleep "
            "further off. Children are especially prone to this after "
            "scary-disgusting media. The practical read: if appetite is "
            "gone, the wave has not finished; if energy is heavy, the "
            "system is still processing; if sleep loops, the memory needs "
            "an earlier off-ramp - a calming routine, a different last "
            "thought, distance from the replay. The body recovers on its "
            "own schedule. Rushing it - forcing a meal, demanding cheer - "
            "usually just adds a second problem on top of the first."),
        "how_it_works": (
            "Appetite loss is the rejection program extended in time: the "
            "gut stays on alert after the vote. Energy drain follows from "
            "sustained parasympathetic engagement - the heavy, cold "
            "fatigue of the brake rather than the hot fatigue of the "
            "accelerator. Sleep disruption comes through memory replay, "
            "each loop re-triggering a small wave. Recovery is staged: "
            "bland foods first, rest without pressure, and an off-ramp for "
            "the replay before bed."),
        "key_points": [
            "Appetite is the direct casualty: after a strong wave, food looks wrong for hours - by design.",
            "Appetite returns in stages: bland and plain first, normal eating often by the next day.",
            "Energy drains heavy, not wired - sustained disgust is tiring like carrying something.",
            "Sleep suffers through replay: bedtime loops of the trigger bring small waves that push sleep off.",
            "Gone appetite means the wave has not finished; heavy energy means the system is still processing.",
            "Do not rush recovery - forcing a meal or demanding cheer adds a second problem to the first."],
        "requirements": [
            "No equipment needed - this is a reading and reflection record.",
            "Notice appetite and energy after your next strong reaction.",
            "A few quiet minutes."],
        "standards": [
            "Public record in the Signature system: fact-checked emotion psychology.",
            "Descriptive and educational only - never diagnoses any real person.",
            "Human-readable sentences and paragraphs throughout."],
        "citations": [CIT_ROZIN_HAIDT, CIT_ROZIN_FALLON],
        "sig_lens": (
            "Signature lens: his Signature system treats appetite, energy, "
            "and sleep as the gate's supply lines - the logistics the "
            "alarm borrows and must repay. The Signature archivist's "
            "standing order: after any full muster, resupply before the "
            "next patrol. Bland food, real rest, no forced marches. A gate "
            "that never resupplies starts seeing threats in shadows."),
    },
    {
        "key": "bodies-differ",
        "name": "How Bodies Differ in Disgust",
        "group": "Body Signals",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "No two bodies run the alarm at the same setting. Sensitivity "
            "to disgust varies enormously from person to person - "
            "researchers built whole scales to measure it, and the spread "
            "is one of the widest in emotion psychology. Some people gag at "
            "a bruised apple; others work in sanitation or surgery without "
            "flinching. Neither setting is broken. Part of the difference "
            "is biology: the gag reflex, smell sensitivity, and stomach "
            "reactivity all vary, and life stages shift the dial - "
            "pregnancy, for example, famously turns the pathogen alarm up, "
            "as if the body posts extra guards while building a new "
            "person. Part is training: butchers, nurses, parents of toddlers, "
            "and plumbers all habituate - repeated, controlled exposure "
            "teaches the system which triggers are truly dangerous and "
            "which are merely unpleasant, and the alarm learns to stand "
            "down for the second kind. Part is culture: what one table "
            "treasures, another cannot face, and children absorb their "
            "household's disgust map before they can tie their shoes. The "
            "body's expression of the feeling varies too. One person's "
            "disgust lives in the stomach (nausea first), another's in the "
            "throat (gagging first), another's in the skin (the crawl). "
            "Some go pale and faint-feeling; others just go still and "
            "quiet. The practical lesson is calibration across people, not "
            "just within one body. The coworker who gags at the break-room "
            "smell is not performing; the surgeon who shrugs at it is not "
            "heartless. They are running different hardware on different "
            "settings. Judging another person's alarm by your own dial is "
            "the most common interpersonal mistake disgust causes - and the "
            "easiest to fix, once you know the dials differ."),
        "how_it_works": (
            "Sensitivity is a setpoint with three inputs: biology (reflex "
            "strength, smell acuity, life stage), training (habituation "
            "through repeated controlled exposure), and culture (the "
            "absorbed household map). The body's chosen channel - stomach, "
            "throat, or skin - is a personal style laid over the setpoint. "
            "Because both setpoint and channel vary, the same trigger "
            "produces legitimately different experiences in different "
            "people."),
        "key_points": [
            "Sensitivity varies enormously - one of the widest spreads in emotion psychology; neither end is broken.",
            "Biology sets part of the dial: gag reflex, smell acuity, and life stages like pregnancy shift it.",
            "Training habituates: repeated controlled exposure teaches the alarm to stand down for merely-unpleasant triggers.",
            "Culture writes the map early: children absorb their household's disgust settings before school age.",
            "The channel varies too: stomach-first, throat-first, or skin-first people all feel the same alarm.",
            "Never judge another person's alarm by your own dial - different hardware, different settings."],
        "requirements": [
            "No equipment needed - this is a reading and reflection record.",
            "Consider where your own dial sits and how it got there.",
            "A few quiet minutes."],
        "standards": [
            "Public record in the Signature system: fact-checked emotion psychology.",
            "Descriptive and educational only - never diagnoses any real person.",
            "Human-readable sentences and paragraphs throughout."],
        "citations": [CIT_HAIDT_DS, CIT_TYBUR],
        "sig_lens": (
            "Signature lens: his Signature system files every person's dial "
            "setting as legitimate territory data - no two gates are built "
            "alike, and a low wall is not a failed wall. The Signature "
            "archivist's rule for mixed company: calibrate to the most "
            "sensitive gate in the room, not your own. Courtesy is just "
            "calibration with manners."),
    },
    # ---------------- Facial expression (records 14-17) ----------------
    {
        "key": "face",
        "name": "The Face of Disgust: Eyes, Nose, and Mouth",
        "group": "Facial Expression",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The disgust face is one of the most recognizable expressions "
            "on earth - Darwin sketched it in 1872 and it has not changed "
            "since, because it is functional: every feature narrows an "
            "opening or prepares an exit. Start with the nose, the "
            "centerpiece. The nostrils flare and the bridge wrinkles - the "
            "levator muscles pull the sides of the nose up and in, as if "
            "trying to close the gates against a bad smell. The brows lower "
            "and draw slightly together, and the eyes narrow - less light, "
            "less sight of the offensive thing, a partial shutting of the "
            "visual gate. Then the mouth, the most telling part: the upper "
            "lip lifts and curls, exposing the upper teeth in a sneer-like "
            "lift that is really the preparation to spit. The lower lip may "
            "push up to meet it. In strong disgust the mouth opens - the "
            "gape that precedes retching, the body clearing the exit route. "
            "The cheeks lift with the nose wrinkle, bunching the skin under "
            "the eyes. Micro-signs ride along: a quick sniff or snort "
            "(testing the air), a swallow that sticks, a tongue that pushes "
            "forward slightly as if ejecting something. The whole "
            "configuration takes under a second to assemble and is read "
            "correctly across cultures at rates far above chance - show the "
            "face to anyone, anywhere, and they know: something foul is "
            "near. It is worth noting what the face is NOT: it is not the "
            "anger face (brows down and together with a hard stare and "
            "pressed lips - confrontation, not rejection), and not the "
            "contempt face (one-sided, a single lifted lip corner - cold "
            "dismissal from above, not the full bilateral wrinkle of "
            "disgust). The disgust face is symmetrical, fast, and "
            "unmistakable: the gates closing, the exits opening."),
        "how_it_works": (
            "Each feature serves the rejection program: nose wrinkle and "
            "narrowed eyes reduce sensory intake; the raised upper lip and "
            "gape prepare the oral exit; the lowered brow shields the eyes. "
            "The expression is assembled by dedicated facial muscles in a "
            "fixed pattern, which is why it is universal - the same "
            "hardware, the same wiring, in every human face."),
        "key_points": [
            "The nose is the centerpiece: wrinkled bridge and flared nostrils closing the gates against bad smells.",
            "Brows lower, eyes narrow - the visual gate partially shuts against the offensive thing.",
            "The upper lip lifts and curls: the preparation to spit, exposing the upper teeth.",
            "Strong disgust opens the mouth into the gape that precedes retching - the exit route clearing.",
            "Micro-signs: the testing sniff, the stuck swallow, the tongue pushing forward.",
            "It is symmetrical and bilateral - unlike contempt's one-sided smirk or anger's hard stare."],
        "requirements": [
            "No equipment needed - this is a reading and reflection record.",
            "A mirror helps: try the nose wrinkle and feel which muscles move.",
            "A few quiet minutes."],
        "standards": [
            "Public record in the Signature system: fact-checked emotion psychology.",
            "Descriptive and educational only - never diagnoses any real person.",
            "Human-readable sentences and paragraphs throughout."],
        "citations": [CIT_DARWIN, CIT_EKMAN, CIT_CHAPMAN],
        "sig_lens": (
            "Signature lens: his Signature system reads the face as the "
            "gate's portcullis in motion - every muscle a bar sliding "
            "down. The Signature archivist studies the portcullis the way "
            "an engineer studies a bridge: not to judge the crossing, but "
            "to know exactly how the defense works. Learn the face and you "
            "can read the gate from across any room on earth."),
    },
    {
        "key": "face-intensity",
        "name": "How the Disgust Expression Changes with Intensity",
        "group": "Facial Expression",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "The disgust face is not one mask but a slider, and each "
            "position on the slider tells you the volume of the alarm. At "
            "the faintest setting there is only a whisper of movement: the "
            "nostrils tighten a fraction, the upper lip lifts a millimeter "
            "- a micro-expression lasting less than half a second, gone "
            "before the person knows it happened. Observers often miss it; "
            "cameras in slow motion catch it. One notch up, the nose wrinkle "
            "becomes visible to anyone watching: the bridge creases, the "
            "brows come down, the lip curl is unmistakable. This is the "
            "social signal - the face now broadcasting \"something is off\" "
            "to everyone nearby, which is why one person's visible disgust "
            "can ripple through a whole table. At moderate intensity the "
            "mouth joins fully: the gape begins, the tongue may show, the "
            "head starts its turn away. The expression is no longer just a "
            "signal but a preparation - the body staging the exit. At full "
            "intensity the face becomes the whole event: eyes squeezed or "
            "averted entirely, mouth open in the retch-gape, neck muscles "
            "standing out, sometimes tears from the effort of gagging. The "
            "person cannot hold a neutral face at this level if they tried - "
            "the program overrides voluntary control. Two patterns matter "
            "for reading. First, asymmetry of control: the lower face "
            "(mouth, lip) is easier to fake or suppress than the upper face "
            "(nose wrinkle, brow) - so the nose tells the truth when the "
            "mouth is performing. Second, duration: genuine disgust flashes "
            "and fades with the trigger, while a held, posed disgust face "
            "lingers too long and looks theatrical. Read the slider, not "
            "just the mask: a whisper of nose-wrinkle at a joke's punchline "
            "and a full gape at a wound are the same alphabet at different "
            "font sizes."),
        "how_it_works": (
            "Intensity scales the expression by recruiting more muscle "
            "groups and overriding voluntary control at the top end. The "
            "upper face leads at low intensity (hard to suppress); the "
            "mouth and whole head join as volume rises. Duration and "
            "symmetry separate the genuine flash (brief, bilateral, "
            "trigger-locked) from the posed hold (lingering, often "
            "asymmetric, theatrical)."),
        "key_points": [
            "The face is a slider: micro-wrinkle, visible wrinkle, mouth joining, full gape - each step a louder alarm.",
            "Micro-expressions last under half a second and are usually missed by observers, caught by slow motion.",
            "Visible disgust is a social signal: one wrinkled nose can ripple through a whole table.",
            "At full intensity voluntary control is overridden - the program runs the face, not the person.",
            "The nose tells the truth: the upper face is harder to fake than the mouth.",
            "Genuine disgust flashes and fades with the trigger; posed disgust lingers too long and looks theatrical."],
        "requirements": [
            "No equipment needed - this is a reading and reflection record.",
            "Watch faces in a crowded food court for the slider in action.",
            "A few quiet minutes."],
        "standards": [
            "Public record in the Signature system: fact-checked emotion psychology.",
            "Descriptive and educational only - never diagnoses any real person.",
            "Human-readable sentences and paragraphs throughout."],
        "citations": [CIT_EKMAN, CIT_DARWIN],
        "sig_lens": (
            "Signature lens: his Signature system reads the slider as the "
            "portcullis's travel - how far the bars have dropped tells the "
            "watch exactly how serious the threat reads. The Signature "
            "archivist's field note: trust the nose over the mouth, the "
            "flash over the hold. The gate's honest parts are the ones the "
            "will cannot easily reach."),
    },
    {
        "key": "hide-fake",
        "name": "Hiding or Faking Disgust: What Leaks Through",
        "group": "Facial Expression",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "People hide disgust constantly - at the dinner table, in the "
            "hospital, at work - and they fake it too, performing outrage "
            "they do not feel. Both efforts leak, because the disgust "
            "program was not built to be voluntary. When someone suppresses "
            "real disgust, the leaks follow a pattern. The nose wrinkle is "
            "the hardest to kill: the person may smooth their mouth into a "
            "polite shape while the bridge of the nose still creases for a "
            "fraction of a second. The swallow gives it away next - a hard, "
            "visible swallow, the throat managing what the face denied. "
            "Then the body: the lean-back survives almost every attempt at "
            "a neutral face, and the hands betray with small distancing "
            "moves - the plate pushed a centimeter further away, the cup "
            "set down and not picked up again. The voice leaks too, going "
            "slightly higher and tighter, words clipped shorter than "
            "usual. Faking disgust leaks in the opposite direction: the "
            "performance overshoots. The posed face holds too long, the "
            "lip-curl goes asymmetric (real disgust is bilateral), the "
            "accompanying \"ugh\" arrives a beat late and a touch too loud. "
            "Real disgust is fast, symmetrical, and trigger-locked - it "
            "appears with the trigger and fades as distance grows. Faked "
            "disgust is slow, often one-sided, and oddly durable - it "
            "lingers because there is no real wave underneath to fade. "
            "There is an honest middle ground worth naming: the managed "
            "face. Nurses, parents, and hosts learn not to erase the "
            "signal but to soften its broadcast - acknowledging the "
            "feeling internally while choosing a kinder exterior. That is "
            "not deception; it is courtesy, and the small leaks that "
            "remain are simply the body being honest underneath the "
            "manners. The lesson is not to become a human lie detector. It "
            "is to read gently: the leaks tell you someone is working hard "
            "to be polite, and working hard deserves kindness, not "
            "exposure."),
        "how_it_works": (
            "Suppression fails asymmetrically: voluntary control reaches "
            "the mouth easily but barely touches the nose-wrinkle muscles, "
            "the swallow reflex, or the postural lean-back - so those "
            "channels leak first. Faking fails by overshoot: without a real "
            "wave driving it, the performance mistimes the onset, breaks "
            "the bilateral symmetry, and outlasts the trigger. The managed "
            "face is the skilled compromise: internal acknowledgment plus "
            "chosen softening."),
        "key_points": [
            "Suppression leaks in order: nose wrinkle first, then the hard swallow, then the lean-back and distancing hands.",
            "The voice leaks too - slightly higher, tighter, words clipped shorter than usual.",
            "Faked disgust overshoots: held too long, asymmetric lip-curl, the \"ugh\" a beat late and too loud.",
            "Real disgust is fast, bilateral, and trigger-locked; faked disgust is slow, one-sided, and oddly durable.",
            "The managed face - softened broadcast, honest interior - is courtesy, not deception.",
            "Read leaks gently: they usually mean someone is working hard to be polite, which deserves kindness."],
        "requirements": [
            "No equipment needed - this is a reading and reflection record.",
            "Notice your own suppression leaks before studying others.",
            "A few quiet minutes."],
        "standards": [
            "Public record in the Signature system: fact-checked emotion psychology.",
            "Descriptive and educational only - never diagnoses any real person.",
            "Human-readable sentences and paragraphs throughout."],
        "citations": [CIT_EKMAN, CIT_DARWIN],
        "sig_lens": (
            "Signature lens: his Signature system treats leaks as the "
            "gate's honest stonework showing through fresh paint. The "
            "Signature archivist does not prize catching people out - the "
            "paint is usually courtesy, and courtesy is a load-bearing "
            "wall. Read the stonework to understand, not to expose; a "
            "sentry struggling to stay polite is doing the territory a "
            "service."),
    },
    {
        "key": "drawing-guide",
        "name": "Drawing the Face of Disgust: A Descriptive Guide",
        "group": "Facial Expression",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "For the artist, the actor, or the animator: here is the "
            "disgust face as buildable geometry. Begin with the nose - it "
            "is the keystone. Draw the bridge with two short diagonal "
            "creases running from the inner eyebrows down toward the "
            "nostrils, like a tent collapsing inward; the nostrils themselves "
            "flare and pull up, becoming rounder and higher than at rest. "
            "The eyebrows lower and angle slightly inward-down, casting a "
            "small shadow over the eyes, which narrow to about two-thirds "
            "open - draw the upper lids dropping, not the lower lids "
            "rising (that would be a different emotion). The cheeks are the "
            "next structural move: the nose-wrinkle muscles drag the cheek "
            "flesh upward, bunching it under the eyes into small pouches - "
            "this is the detail that sells the whole expression, so do not "
            "skip it. Now the mouth, the most expressive element. Raise the "
            "upper lip in the center, curling it up and slightly back to "
            "expose the upper teeth and a sliver of gum; let the corners of "
            "the mouth pull down a touch. For mild disgust, keep the lips "
            "closed over the curl - a contained sneer. For strong disgust, "
            "open the mouth into the gape: jaw drops, tongue flattens or "
            "pushes slightly forward, the throat visible. Add the "
            "supporting cast: the chin may pull up and wrinkle (the "
            "mentalis muscle), the neck cords can stand out at high "
            "intensity, and the whole head tilts back a few degrees and "
            "turns a few degrees away - disgust is never drawn facing the "
            "trigger straight-on. Common mistakes: drawing only the mouth "
            "and forgetting the nose (reads as a sneer, not disgust); making "
            "it one-sided (reads as contempt); holding every muscle at "
            "maximum (reads as a mask, not a moment). Build it in layers - "
            "nose, eyes, cheeks, mouth, head angle - and check the "
            "silhouette: the disgust face has a distinctive crumpled "
            "profile, everything drawing inward and up, away from the "
            "world."),
        "how_it_works": (
            "The guide decomposes the expression into layered geometry - "
            "nose creases, narrowed eyes, bunched cheeks, curled lip, head "
            "angle - each layer corresponding to a real muscle group in the "
            "rejection program. Built in order, the layers reconstruct the "
            "universal pattern; the listed mistakes map to the known "
            "confusions (contempt's asymmetry, the sneer's missing nose)."),
        "key_points": [
            "Start with the nose: diagonal bridge creases, flared and lifted nostrils - the keystone of the expression.",
            "Eyes narrow to two-thirds via dropping upper lids; brows lower and angle inward-down.",
            "Bunched cheeks under the eyes are the detail that sells the whole face - never skip them.",
            "Mouth: upper lip raised and curled centrally; closed for mild, open gape with tongue forward for strong.",
            "The head tilts back and turns away - disgust is never drawn facing the trigger straight-on.",
            "Avoid the three mistakes: mouth-only (reads as sneer), one-sided (reads as contempt), all-maximum (reads as mask)."],
        "requirements": [
            "Pencil and paper, or any drawing tool, to try the layers.",
            "A mirror for reference on your own nose-wrinkle muscles.",
            "A few quiet minutes."],
        "standards": [
            "Public record in the Signature system: fact-checked emotion psychology.",
            "Descriptive and educational only - never diagnoses any real person.",
            "Human-readable sentences and paragraphs throughout."],
        "citations": [CIT_DARWIN, CIT_EKMAN],
        "sig_lens": (
            "Signature lens: his Signature system keeps this guide as the "
            "gate's architectural drawing - the portcullis rendered in "
            "plan and elevation so any craftsperson can rebuild it. The "
            "Signature archivist's note to makers: draw the defense "
            "honestly and the audience will feel the territory's truth "
            "without a word. Good geometry is good testimony."),
    },
    # ---------------- Triggers (records 18-21) ----------------
    {
        "key": "classic-triggers",
        "name": "The Classic Triggers of Disgust",
        "group": "Triggers",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "The classic triggers of disgust fall into nine great domains, "
            "mapped by researchers over decades. One: food - the original "
            "classroom. Spoiled, rotten, or contaminated food; strange "
            "textures; the discovery of something unexpected in the bite. "
            "Two: animals - especially the small, the swarming, and the "
            "scuttling: insects, spiders, rats, slugs. They read as "
            "contamination vectors, and the skin crawls on sight. Three: "
            "body products - the things the body expels are tagged for "
            "expulsion by everyone else: waste, vomit, mucus, blood outside "
            "the body. Four: body envelope violations - wounds, gore, "
            "surgery sights, anything showing the inside on the outside; "
            "this domain also carries the animal-reminder sting, the "
            "unwelcome news that we are fragile meat. Five: death and decay "
            "— corpses, rot, the smells of decomposition. Six: hygiene - "
            "dirt, grime, unwashed bodies and spaces, the visible history "
            "of neglect. Seven: interpersonal contact - unwanted touch, "
            "contact with strangers' bodily traces, sharing what should "
            "not be shared. Eight: the sexual domain - unwanted or "
            "taboo-breaking sexual content, which fires the same rejection "
            "circuit. Nine: moral violations - cruelty, cheating, "
            "betrayal, degradation; no smell required, the same nose "
            "wrinkles, the same \"that's foul.\" What unites all nine is "
            "the logic of contamination: each is something that should not "
            "enter the body, touch the body, or enter the community - and "
            "each threatens to spread its taint to whatever it contacts. "
            "Learn the nine and you can sort any trigger in seconds. A "
            "moldy sandwich is domain one; a wound photo is domain four; a "
            "cheating scandal is domain nine. The sorting matters because "
            "the response that fits domain one (spit it out) is not the "
            "response that fits domain nine (speak up, set the boundary) - "
            "same alarm, different correct answer."),
        "how_it_works": (
            "The nine domains are the alarm's target list, each a category "
            "of thing that historically threatened the body or the group. "
            "The contamination logic unites them: the trigger is treated as "
            "tainting whatever it touches. Sorting a trigger into its "
            "domain is the first step of a correct response, because each "
            "domain has its own fitting answer - expel, clean, distance, "
            "or confront."),
        "key_points": [
            "Nine classic domains: food, animals, body products, body envelope violations, death, hygiene, interpersonal contact, sexual, moral.",
            "Food is the original classroom; the other eight are the same circuit aimed at new targets.",
            "Body envelope violations carry the animal-reminder sting: the unwelcome news that we are fragile.",
            "Moral violations fire the same circuit with no smell required - cruelty reads as foul.",
            "Contamination logic unites all nine: each threatens to taint whatever it touches.",
            "Sort the trigger first - spit-it-out fits domain one, speak-up fits domain nine; same alarm, different answer."],
        "requirements": [
            "No equipment needed - this is a reading and reflection record.",
            "Sort your last three disgust moments into the nine domains.",
            "A few quiet minutes."],
        "standards": [
            "Public record in the Signature system: fact-checked emotion psychology.",
            "Descriptive and educational only - never diagnoses any real person.",
            "Human-readable sentences and paragraphs throughout."],
        "citations": [CIT_ROZIN_HAIDT, CIT_TYBUR, CIT_HAIDT_DS],
        "sig_lens": (
            "Signature lens: his Signature system posts the nine domains "
            "as the gate's watch sectors - nine stretches of wall, one "
            "alarm serving all. The Signature archivist drills the sort: "
            "name the sector in under three seconds and the correct "
            "protocol follows on its own. A sentry who knows the sectors "
            "never brings a mop to a moral fight or a speech to a spoiled "
            "sandwich."),
    },
    {
        "key": "personal-triggers",
        "name": "Personal Triggers: Memory and Association",
        "group": "Triggers",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Beyond the classics, everyone carries a private trigger list "
            "written by their own history - and these personal triggers can "
            "outrank the universal ones. The mechanism is association. A "
            "food that once caused food poisoning becomes permanently "
            "tagged; years later, the smell alone can turn the stomach, "
            "even when the food is fresh and safe. Psychologists call this "
            "the Garcia effect in its strong form - one bad pairing, "
            "lifelong avoidance - and it is the alarm doing exactly what it "
            "evolved to do: once burned, never again. Childhood writes deep "
            "entries. The medicine forced down at age six, the school "
            "cafeteria's mystery meat, the relative whose habits the whole "
            "family whispered about - these become reference triggers "
            "against which new experiences are judged. Anniversaries and "
            "places join the list: the restaurant where the bad night "
            "happened, the month associated with an illness, a song that "
            "was playing. The personal list also runs in reverse - "
            "sensitization upward. A person who once cleaned up after a "
            "flood may find all damp smells triggering for years; the alarm "
            "generalized from one event to a whole category. Two features "
            "make personal triggers tricky. First, they are invisible to "
            "everyone else - the trigger looks harmless, so the reaction "
            "looks disproportionate, and the person can feel embarrassed "
            "about a response that is, to their own history, perfectly "
            "logical. Second, they resist argument: you cannot reason away "
            "a tag written by the body, only overwrite it slowly with new, "
            "safe experiences. The healthy handling is straightforward: "
            "name the association (\"this is about 2019, not about this "
            "meal\"), allow the feeling without obeying it blindly, and "
            "give the body new evidence at its own pace. The history is "
            "real; it just is not always current."),
        "how_it_works": (
            "Personal triggers are learned tags: a bad outcome pairs with "
            "a neutral stimulus once, and the alarm files the pairing as "
            "permanent. The tag generalizes to similar stimuli and "
            "resists verbal counter-evidence because it was written by "
            "experience, not argument. Overwriting requires new safe "
            "experiences - slow, repeated, voluntary - which is why "
            "patience beats pressure."),
        "key_points": [
            "Personal triggers are written by history: one bad pairing can tag a food, smell, or place for years.",
            "Childhood entries run deepest - medicines, cafeteria meals, family-whispered habits become reference triggers.",
            "The alarm generalizes: one flood can tag all damp smells; the category inherits the event's tag.",
            "Personal triggers are invisible to others, so the reaction can look disproportionate and feel embarrassing.",
            "They resist argument - a body-written tag is overwritten only by new safe experiences, slowly.",
            "Name the association, allow the feeling, give the body new evidence at its own pace."],
        "requirements": [
            "No equipment needed - this is a reading and reflection record.",
            "List three of your own private triggers and their origin stories.",
            "A few quiet minutes."],
        "standards": [
            "Public record in the Signature system: fact-checked emotion psychology.",
            "Descriptive and educational only - never diagnoses any real person.",
            "Human-readable sentences and paragraphs throughout."],
        "citations": [CIT_ROZIN_FALLON, CIT_HAIDT_DS],
        "sig_lens": (
            "Signature lens: his Signature system files personal triggers "
            "as the gate's annotated map - every sentry marks the wall "
            "where they were once burned. The Signature archivist honors "
            "the annotations: the map is real, it just may be out of date. "
            "Update it with new patrols, not with arguments; stone "
            "remembers longer than speeches."),
    },
    {
        "key": "surprise-triggers",
        "name": "Surprise Triggers of Disgust",
        "group": "Triggers",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "Some triggers ambush - they are not on anyone's classic list, "
            "and that is exactly why they hit so hard. The common thread "
            "is violated expectation: the alarm fires extra loud when the "
            "world breaks a promise. The texture betrayal: biting into "
            "what looks like a crisp apple and meeting mush; the yogurt "
            "that pours wrong; ice cream with an icy crunch where cream "
            "should be. The mouth expected one thing and received another, "
            "and the mismatch itself reads as contamination. The hidden "
            "discovery: the hair in the food, the insect in the salad, the "
            "realization mid-sip that the cup was not yours. Nothing about "
            "the substance changed in that instant - only the knowledge - "
            "yet the wave arrives at full strength, proving the tag is "
            "partly informational. The context collapse: a smell that is "
            "fine in its place becomes foul out of place - food smells in "
            "a hospital corridor, a familiar cologne in a strange dark "
            "alley. The delayed realization: laughing at a joke, then "
            "getting it three seconds later and feeling the smile curdle; "
            "shaking a hand warmly, then learning whose hand it was. The "
            "body's reaction to surprise triggers runs hotter than the "
            "trigger alone would justify, because two alarms fire at once: "
            "disgust at the thing, and the startle of the ambush. The "
            "practical defense is expectation hygiene. Check before biting "
            "when something looks off; sniff the milk; glance at the cup. "
            "Small verifications cost nothing and prevent the ambushes that "
            "cost an afternoon. And when an ambush lands anyway, name the "
            "second alarm: \"part of this wave is the surprise, not the "
            "thing.\" The wave then has a shape you can wait out, instead "
            "of a mystery that owns you."),
        "how_it_works": (
            "Surprise triggers multiply the wave: the disgust response "
            "plus the startle response fire together, each amplifying the "
            "other. The mechanism is expectation violation - the brain "
            "predicted safe and received foul, and the prediction error "
            "itself is treated as threat information. Small verifications "
            "before contact defuse the multiplier by removing the "
            "surprise half of the equation."),
        "key_points": [
            "Surprise triggers ambush via violated expectation: the world broke a promise, so the alarm fires extra loud.",
            "Texture betrayals (mush where crisp was promised) read as contamination through mismatch alone.",
            "Hidden discoveries prove the tag is partly informational: knowledge alone can summon the full wave.",
            "Context collapse: a fine smell in the wrong place becomes foul - place is part of the promise.",
            "Two alarms fire at once: disgust at the thing plus the startle of the ambush, each amplifying the other.",
            "Practice expectation hygiene: sniff, glance, check - and name the surprise half when an ambush lands."],
        "requirements": [
            "No equipment needed - this is a reading and reflection record.",
            "Recall your last ambush trigger and separate the surprise from the thing.",
            "A few quiet minutes."],
        "standards": [
            "Public record in the Signature system: fact-checked emotion psychology.",
            "Descriptive and educational only - never diagnoses any real person.",
            "Human-readable sentences and paragraphs throughout."],
        "citations": [CIT_ROZIN_FALLON, CIT_MILLER],
        "sig_lens": (
            "Signature lens: his Signature system logs surprise triggers "
            "as breaches - not attacks on the wall, but moments the "
            "sentries were looking the other way. The Signature archivist's "
            "standing order is verification before contact: a glance costs "
            "a second, an ambush costs an afternoon. And when the breach "
            "lands, name both alarms - the discipline turns a mystery into "
            "a wave with a shape, and shapes can be waited out."),
    },
    {
        "key": "chain-reactions",
        "name": "Chain Reactions: When Disgust Pulls Other Emotions",
        "group": "Triggers",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "Disgust rarely ends where it starts. One trigger can set off "
            "a cascade, each emotion handing the baton to the next, until "
            "a person is feeling four things about an event that began "
            "with one smell. Learn the common chains and you can trace any "
            "cascade back to its first link. Chain one: disgust to anger. "
            "The classic moral cascade - a foul act witnessed, disgust "
            "fires, and the contamination logic demands an agent: someone "
            "DID this. Anger arrives to confront the agent. The person now "
            "feels outrage, but the first link was disgust. Chain two: "
            "disgust to shame. The trigger involves the self - a personal "
            "habit discovered, a bodily failure, a memory of something done. "
            "The rejection turns inward: I am the foul thing. Shame is "
            "disgust aimed at the self, and it is the heaviest chain "
            "because there is no distance to take from yourself. Chain "
            "three: disgust to fear. The contamination logic runs forward: "
            "if that touched me, am I tainted? Will I get sick? The worry "
            "about what the trigger carried becomes anxiety about the "
            "future - the person washes, checks, replays. Chain four: "
            "disgust to sadness. Decay witnessed - a ruined place, a "
            "wasted meal, a friendship rotted by betrayal - and the "
            "rejection softens into grief for what was lost to the rot. "
            "The cascade has a direction: it moves from the trigger "
            "outward to agents (anger), inward to self (shame), forward to "
            "consequences (fear), or backward to loss (sadness). The "
            "practical skill is chain-tracing. When you feel the fourth "
            "emotion, ask: what was the first? Find the original trigger "
            "and the cascade often collapses - the anger softens when you "
            "see it started as a smell, the fear settles when you see it "
            "started as a touch. Treat the first link and the followers "
            "frequently stand down on their own."),
        "how_it_works": (
            "Cascades follow the contamination logic outward: the mind "
            "asks what caused it (anger at an agent), whether the self is "
            "the source (shame), what it will cause next (fear of "
            "consequences), or what was lost (sadness). Each link is a "
            "question the disgust raised and another emotion answered. "
            "Chain-tracing reverses the sequence to the original trigger, "
            "which often deflates the followers."),
        "key_points": [
            "One trigger can cascade: disgust hands the baton to anger, shame, fear, or sadness.",
            "Disgust to anger: the contamination logic demands an agent - someone DID this (outrage).",
            "Disgust to shame: the rejection turns inward - I am the foul thing; no distance available.",
            "Disgust to fear: the logic runs forward - am I tainted? will I get sick? (checking, replaying).",
            "Disgust to sadness: decay witnessed softens into grief for what the rot took.",
            "Chain-trace: find the first link and treat it - the follower emotions often stand down on their own."],
        "requirements": [
            "No equipment needed - this is a reading and reflection record.",
            "Trace your last cascade back to its first link.",
            "A few quiet minutes."],
        "standards": [
            "Public record in the Signature system: fact-checked emotion psychology.",
            "Descriptive and educational only - never diagnoses any real person.",
            "Human-readable sentences and paragraphs throughout."],
        "citations": [CIT_ROZIN_HAIDT, CIT_TYBUR],
        "sig_lens": (
            "Signature lens: his Signature system charts cascades as "
            "fire-spread maps - one tower's alarm lighting the next "
            "along known lines. The Signature archivist's discipline is "
            "always the same: find the first flame. Crews sent to the "
            "fourth tower while the first still burns will chase smoke "
            "all day. Trace the chain, treat the source, watch the "
            "followers stand down."),
    },
    # ---------------- How it shows in behavior (records 22-25) ----------------
    {
        "key": "behavior-actions",
        "name": "What People Do When They Feel Disgust",
        "group": "Behavior",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "Disgust writes its signature in actions, and the actions all "
            "rhyme: increase distance, remove the trigger, clean the "
            "contact. Watch a room and you can read the feeling in what "
            "hands and feet do. The first family of actions is avoidance: "
            "stepping back, turning away, leaving the room, choosing the "
            "long way around, declining the offered food with a quick "
            "shake of the head. Avoidance is the purest expression of the "
            "urge - the body voting with its feet. The second family is "
            "expulsion: spitting out, scraping the plate, picking the "
            "offending bit out of the food, vomiting in the extreme case. "
            "What entered must exit. The third family is cleansing: "
            "hand-washing (the universal ritual), wiping the table, airing "
            "the room, changing the clothes that caught the smell. "
            "Cleansing answers the contamination tag - the feeling that "
            "the taint lingers after the thing is gone. The fourth family "
            "is barrier-building: covering the nose and mouth, putting on "
            "gloves, sealing the trash, closing the door on the smell. "
            "Barriers are avoidance made durable. The fifth family only "
            "appears with moral disgust: protest and punishment - speaking "
            "out, reporting, shunning, demanding the foul act stop. The "
            "target shifts from substance to behavior, but the grammar is "
            "identical: get it out of the community the way you would get "
            "it out of the mouth. Two cautions complete the picture. "
            "First, avoidance can become a cage: the person who will not "
            "eat in restaurants, touch handles, or meet new people is not "
            "running a healthy alarm but a hypersensitive one, and the "
            "world shrinks to the size of the safe zone. Second, cleansing "
            "can become a ritual that never satisfies: when washing stops "
            "answering the contamination tag and starts feeding it, the "
            "action has flipped from solution to symptom. Healthy disgust "
            "acts, then rests. The action completes the circuit - the "
            "trigger is gone, the hands are clean, the distance is real - "
            "and the alarm stands down."),
        "how_it_works": (
            "The five action families are the push-away urge translated "
            "into the world: avoidance (distance now), expulsion (reverse "
            "the entry), cleansing (erase the tag), barriers (durable "
            "distance), and protest (the moral form of expulsion). Each "
            "completes the circuit when it achieves real separation; the "
            "failure modes are avoidance that cages and cleansing that "
            "feeds the tag instead of erasing it."),
        "key_points": [
            "Five action families: avoidance, expulsion, cleansing, barrier-building, and protest (moral disgust).",
            "Avoidance is the purest expression - the body voting with its feet: step back, turn away, leave.",
            "Expulsion reverses entry: spit out, scrape off, pick out; vomiting is the extreme form.",
            "Cleansing answers the contamination tag: wash, wipe, air, change - erase the lingering taint.",
            "Protest is moral expulsion: speak out, report, shun - get it out of the community.",
            "Healthy disgust acts, then rests; the failure modes are avoidance that cages and cleansing that feeds the tag."],
        "requirements": [
            "No equipment needed - this is a reading and reflection record.",
            "Watch the five families in action in a busy public place.",
            "A few quiet minutes."],
        "standards": [
            "Public record in the Signature system: fact-checked emotion psychology.",
            "Descriptive and educational only - never diagnoses any real person.",
            "Human-readable sentences and paragraphs throughout."],
        "citations": [CIT_ROZIN_HAIDT, CIT_MILLER],
        "sig_lens": (
            "Signature lens: his Signature system reads the five families "
            "as the gate's standard drills - withdraw, eject, scrub, "
            "fortify, and (for moral breaches) proclaim. The Signature "
            "archivist inspects every drill by one measure: did the "
            "circuit complete? A drill that ends with the territory clean "
            "and the sentries rested is sound. A drill that never ends is "
            "not discipline - it is a jammed gate, and jammed gates get "
            "repaired, not obeyed."),
    },
    {
        "key": "behavior-speech",
        "name": "What People Say When They Feel Disgust",
        "group": "Behavior",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "Disgust has a vocabulary, and it is short. At the mild end "
            "people narrate the rejection plainly: \"nope,\" \"not for "
            "me,\" \"I'll pass,\" \"something's off.\" The words are "
            "small, almost administrative - the feeling handled like a "
            "scheduling conflict. One step up, the classic interjections "
            "arrive: \"ugh,\" \"ew,\" \"gross,\" \"nasty.\" These are "
            "barely words at all - they are vocalizations of the gag "
            "reflex given syllables, and they cross languages with "
            "suspicious ease. At moderate intensity the sentences get "
            "descriptive and distancing: \"that's disgusting,\" \"get that "
            "away from me,\" \"don't touch me with that,\" \"I can't even "
            "look at it.\" Notice the grammar: the trigger becomes \"that\" "
            "- unnamed, unhandled, held at linguistic arm's length. At "
            "high intensity language collapses: fragments, repetitions, "
            "sometimes just sounds. \"No no no. Get it off, get it off.\" "
            "The wave has taken the words. Tone carries as much as "
            "vocabulary. Disgust raises the pitch slightly and tightens "
            "it - the voice gets thinner, faster, clipped. Vowels "
            "shorten; sentences get chopped into pieces. A person "
            "describing a disgusting experience will often speak in bursts "
            "with swallows between them, the throat still managing the "
            "memory. There is also the reported-speech pattern: people "
            "recount disgusting events in vivid present tense - \"and then "
            "I see it, and it's MOVING\" - reliving the trigger as they "
            "describe it, sometimes re-triggering themselves mid-sentence. "
            "And there is the moral register: \"that's sick,\" \"filthy,\" "
            "\"how could anyone,\" the vocabulary of contamination applied "
            "to acts and people. Listening for disgust in others means "
            "listening for the short words, the raised thin pitch, the "
            "\"that\" that keeps its distance, and the swallows between "
            "bursts. The speech is the alarm's press release - brief, "
            "urgent, and honest about exactly one thing: distance wanted."),
        "how_it_works": (
            "Speech degrades along the intensity slider: administrative "
            "declines at low volume, gag-vocalizations in the middle, "
            "descriptive distancing sentences at moderate, fragmentary "
            "collapse at high. Pitch rises and tightens as the throat "
            "joins the program; the demonstrative \"that\" encodes the "
            "distancing grammar. Present-tense reliving shows the memory "
            "re-firing the circuit during narration."),
        "key_points": [
            "The vocabulary is short: nope and I'll pass at mild; ugh, ew, gross in the middle; fragments at high.",
            "Interjections are gag-reflex vocalizations given syllables - they cross languages with ease.",
            "Distancing grammar: the trigger becomes \"that\" - unnamed, unhandled, at linguistic arm's length.",
            "Tone: pitch rises slightly and tightens; vowels shorten; sentences chop into bursts with swallows between.",
            "People recount disgusting events in vivid present tense, sometimes re-triggering themselves mid-sentence.",
            "Listen for the short words, the thin pitch, the distant \"that\" - the press release always says: distance wanted."],
        "requirements": [
            "No equipment needed - this is a reading and reflection record.",
            "Listen for the vocabulary in your next three disgust conversations.",
            "A few quiet minutes."],
        "standards": [
            "Public record in the Signature system: fact-checked emotion psychology.",
            "Descriptive and educational only - never diagnoses any real person.",
            "Human-readable sentences and paragraphs throughout."],
        "citations": [CIT_DARWIN, CIT_MILLER],
        "sig_lens": (
            "Signature lens: his Signature system files disgust-speech as "
            "the gate's signal flags - short, standardized, readable at "
            "distance. The Signature archivist learns the flags the way "
            "sailors learn pennants: \"that\" means standoff distance, the "
            "thin pitch means the throat is engaged, the fragment means "
            "the wave is peaking. Read the flags and you know the harbor "
            "conditions without boarding the ship."),
    },
    {
        "key": "behavior-decisions",
        "name": "How Disgust Changes Decisions and Judgment",
        "group": "Behavior",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "Disgust does not just move bodies - it moves verdicts. The "
            "contamination logic leaks into judgment, and the leak has been "
            "measured. The classic demonstration: people will refuse to "
            "drink juice that briefly held a sterilized cockroach, or wear "
            "a sweater that belonged to someone unpleasant, even knowing "
            "with full certainty that the object is clean. The feeling "
            "votes against the facts - once tainted, always tainted, says "
            "the tag. The leak reaches moral judgment too. In famous "
            "experiments, people make harsher moral verdicts when they are "
            "sitting at a dirty desk, smelling something foul, or watching "
            "something gross - the physical disgust spills into the moral "
            "scales. A room that smells bad produces stricter judges. "
            "Disgust also prices risk. It makes the unfamiliar feel "
            "dangerous: new foods, new places, new people get marked down "
            "not on evidence but on the alarm's caution. This is protective "
            "when the unfamiliar is genuinely risky and costly when it is "
            "not - the same mechanism that kept ancestors from bad "
            "mushrooms can keep a person from a good opportunity. The "
            "practical defense is the pause-and-source check. Feeling a "
            "strong no about a decision? Ask: is this disgust at the thing "
            "itself, or disgust leaking in from somewhere nearby - the "
            "room, the memory, the headline I read at lunch? If the "
            "feeling has a source independent of the decision, discount it "
            "before it votes. None of this makes disgust an enemy of good "
            "judgment. At its best it is an early-warning consultant: the "
            "deal that \"smells wrong,\" the person whose story \"doesn't "
            "sit right.\" The skill is not silencing the consultant but "
            "checking its brief - is it reporting on this decision, or "
            "filing a report from another case entirely?"),
        "how_it_works": (
            "The contamination tag generalizes: \"once tainted, always "
            "tainted\" overrides factual knowledge of cleanliness, and the "
            "affective state spills into adjacent judgments (moral verdicts "
            "harden in foul-smelling rooms). The pause-and-source check "
            "separates signal from spill by tracing the feeling to its "
            "actual trigger before letting it vote on the decision."),
        "key_points": [
            "The feeling votes against the facts: sterilized but once-tainted objects are refused anyway.",
            "Physical disgust spills into moral scales - foul smells and dirty desks produce harsher judges.",
            "Disgust prices risk: the unfamiliar gets marked down on alarm, not evidence - protective or costly.",
            "At its best it is an early-warning consultant: the deal that smells wrong deserves a second look.",
            "The defense is pause-and-source: is this disgust at the thing, or leakage from nearby?",
            "Never silence the consultant - check its brief: which case is it actually reporting on?"],
        "requirements": [
            "No equipment needed - this is a reading and reflection record.",
            "Apply the pause-and-source check to your next strong no.",
            "A few quiet minutes."],
        "standards": [
            "Public record in the Signature system: fact-checked emotion psychology.",
            "Descriptive and educational only - never diagnoses any real person.",
            "Human-readable sentences and paragraphs throughout."],
        "citations": [CIT_ROZIN_FALLON, CIT_CHAPMAN],
        "sig_lens": (
            "Signature lens: his Signature system seats disgust at the "
            "council table as the advisor for contamination - valued, "
            "heard, and never given the deciding vote alone. The Signature "
            "archivist's procedure: let the advisor speak, then check the "
            "brief. An advisor reporting from another case gets thanked "
            "and excused. An advisor reporting on this case gets a second "
            "look. Councils that skip the check get ruled by the loudest "
            "alarm, not the wisest one."),
    },
    {
        "key": "behavior-escalation",
        "name": "Disgust Under Intensity: Escalation",
        "group": "Behavior",
        "ladder_rank": 9,
        "ladder_tier": "compounded",
        "description": (
            "As the volume rises, disgust-driven behavior climbs a ladder "
            "of its own - and each rung is harder to climb back down. Rung "
            "one is private avoidance: quietly not eating the dish, "
            "stepping around the mess, saying nothing. The feeling is "
            "managed invisibly; no one else is involved. Rung two is "
            "visible avoidance: the face shows it, the lean-back is "
            "obvious, the plate is pushed away where others can see. The "
            "signal has gone social - nearby people now catch the ripple. "
            "Rung three is active expulsion and cleansing: spitting out, "
            "washing repeatedly, airing the room, demanding the trigger be "
            "removed. The person is now reorganizing the environment around "
            "the alarm. Rung four is vocal condemnation: \"this is "
            "disgusting,\" said loudly, repeatedly, recruiting others to "
            "the verdict. With moral triggers this is where protest, "
            "shaming, and demands for punishment enter. Rung five is "
            "dehumanization risk - the danger zone, and the reason this "
            "record exists as a warning. At maximum intensity, the "
            "contamination logic can do something terrible: it can tag not "
            "just acts but people as fundamentally foul, beyond cleaning, "
            "beyond redemption. History's worst chapters run on this "
            "rung - the language of vermin and filth applied to human "
            "beings. The escalation ladder is descriptive, not prescriptive: "
            "it shows where the mechanism CAN go, so readers can recognize "
            "the climb and step off. The off-ramps exist at every rung. "
            "From rung two: manage the broadcast (the managed face). From "
            "rung three: complete the circuit and rest - the trigger is "
            "gone, stand down. From rung four: separate the act from the "
            "actor - condemn what was done without tagging the person as "
            "untouchable. From rung five: stop, name the mechanism out "
            "loud, and refuse the tag - no human being is contamination. "
            "The ladder's lesson is simple and serious: the alarm is a "
            "servant of the territory, and servants that start redrawing "
            "the map get relieved of duty."),
        "how_it_works": (
            "Escalation follows the contamination logic outward: from "
            "private management to social broadcast to environmental "
            "reorganization to recruitment of others to, at the extreme, "
            "tagging persons instead of acts. Each rung widens the blast "
            "radius. The off-ramps work by narrowing it again: manage the "
            "broadcast, complete the circuit, separate act from actor, "
            "refuse the person-tag."),
        "key_points": [
            "Rung one: private avoidance - invisible management, nobody else involved.",
            "Rung two: visible avoidance - the signal goes social and ripples to nearby people.",
            "Rung three: active expulsion and cleansing - reorganizing the environment around the alarm.",
            "Rung four: vocal condemnation - recruiting others to the verdict; protest and punishment enter.",
            "Rung five is the danger zone: the contamination tag aimed at people instead of acts - recognize and refuse it.",
            "Off-ramps at every rung: manage the broadcast, complete the circuit, separate act from actor, refuse the person-tag."],
        "requirements": [
            "No equipment needed - this is a reading and reflection record.",
            "Learn the rungs so you can recognize the climb - in yourself first.",
            "A few quiet minutes."],
        "standards": [
            "Public record in the Signature system: fact-checked emotion psychology.",
            "Descriptive and educational only - never diagnoses any real person.",
            "Human-readable sentences and paragraphs throughout."],
        "citations": [CIT_ROZIN_HAIDT, CIT_MILLER],
        "sig_lens": (
            "Signature lens: his Signature system treats the ladder as the "
            "gate's emergency protocol with a hard ceiling: no sentry, "
            "under any alarm, tags a human being as contamination. The "
            "Signature archivist's oath is posted at rung five in red: "
            "the alarm serves the territory; the moment it redraws the map "
            "to exclude people, it is relieved of duty. Read the ladder to "
            "know where the climb leads - then refuse the top rung, always."),
    },
    # ---------------- How to express it healthily (records 26-28) ----------------
    {
        "key": "healthy-expression",
        "name": "Expressing Disgust in Healthy Ways",
        "group": "Healthy Expression",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Disgust is information, and information wants an outlet. "
            "Healthy expression gives the signal somewhere useful to go. "
            "The first channel is naming it, plainly and early: \"this "
            "smell is getting to me,\" \"I'm not comfortable with this.\" "
            "Naming does two jobs - it tells the people around you what is "
            "happening before your face tells them rudely, and it tells "
            "your own system that the message was received, which by itself "
            "lowers the volume a notch. The second channel is acting on "
            "the information proportionately: leave the room, open the "
            "window, decline the food, wash your hands - the small honest "
            "actions that complete the circuit. The alarm stands down when "
            "it sees its advice was taken. The third channel is showing it "
            "without weaponizing it. There is a wide territory between "
            "suppressing the face entirely and broadcasting revulsion at "
            "someone: the managed face, the honest \"no thank you,\" the "
            "step back that does not become a scene. With moral disgust, "
            "the healthy channel is speech with a target: name the act, "
            "not the actor - \"what happened there was wrong\" lands "
            "cleaner and truer than \"you are disgusting.\" The fourth "
            "channel is channeling: disgust is excellent fuel when aimed "
            "well. It built sanitation systems, food safety laws, and "
            "countless personal standards of care. The person who feels "
            "disgust at a dirty kitchen and cleans it, or at a cruel "
            "practice and works to change it, has converted the alarm into "
            "craft. What healthy expression is NOT: it is not endless "
            "venting - repeating the revulsion does not discharge it, it "
            "rehearses it. It is not performing disgust to recruit allies "
            "or punish the already-punished. And it is not obedience: the "
            "signal advises; you decide. The test of healthy expression is "
            "the aftermath. If the circuit completed - trigger addressed, "
            "body settling, mind moving on - the expression was healthy. "
            "If the feeling is still running the show an hour later, the "
            "outlet was not an outlet; it was a loop."),
        "how_it_works": (
            "Healthy expression completes the alarm's circuit through four "
            "channels: naming (message received, volume drops), "
            "proportionate action (advice taken, alarm stands down), "
            "non-weaponized showing (honest without cruelty), and "
            "channeling (alarm converted to craft). The aftermath test "
            "distinguishes outlets from loops: completed circuits settle, "
            "loops rehearse."),
        "key_points": [
            "Name it early and plainly: the message received lowers the volume; the people around you deserve the warning.",
            "Act on it proportionately: leave, open, decline, wash - small honest actions complete the circuit.",
            "Show it without weaponizing it: the managed face, the honest no, the step back that does not become a scene.",
            "With moral disgust, target the act not the actor: what was done was wrong lands cleaner than you are disgusting.",
            "Channel it: disgust built sanitation and food safety - convert the alarm into craft.",
            "The aftermath test: if the body settles and the mind moves on, it was an outlet; if it loops, it was not."],
        "requirements": [
            "No equipment needed - this is a reading and reflection record.",
            "Practice naming the next small disgust out loud, kindly.",
            "A few quiet minutes."],
        "standards": [
            "Public record in the Signature system: fact-checked emotion psychology.",
            "Descriptive and educational only - general everyday guidance, never therapy.",
            "Human-readable sentences and paragraphs throughout."],
        "citations": [CIT_ROZIN_HAIDT, CIT_MILLER],
        "sig_lens": (
            "Signature lens: his Signature system treats healthy expression "
            "as the gate's proper reporting chain - sentry to commander, "
            "clear, prompt, proportionate. The Signature archivist's "
            "standard: a report that completes the circuit is good "
            "soldiering; a report that becomes a loop is a sentry stuck on "
            "the wall. Name it, act on it, convert it to craft - then "
            "stand the watch down."),
    },
    {
        "key": "unhealthy-expression",
        "name": "Unhealthy Expression: Bottling Up or Exploding",
        "group": "Healthy Expression",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "When disgust gets no healthy outlet, it goes one of two bad "
            "ways: inward or outward, bottling or exploding - and both "
            "charge interest. Bottling looks like composure and costs like "
            "debt. The person feels the wave and shows nothing: smiles "
            "through the meal, says nothing about the smell, swallows the "
            "revulsion along with the food. The short-term price is "
            "tension - the throat stays tight, the stomach stays unsettled, "
            "the jaw aches by evening. The long-term price is worse: "
            "unexpressed disgust ferments. It generalizes (now the whole "
            "restaurant is tainted, now the whole cuisine), it somaticizes "
            "(the stomach complaints with no meal attached), and it leaks "
            "sideways - the person who swallowed revulsion at lunch snaps "
            "at someone innocent by dinner. Bottling also trains the alarm "
            "upward: a signal consistently ignored gets louder, not "
            "quieter, because the system concludes the message is not "
            "getting through. Exploding is the opposite failure. The wave "
            "gets a megaphone: gagging theatrics at the table, loud "
            "denunciations, shaming the cook, the host, the culture that "
            "made the food. The short-term payoff is real - enormous "
            "relief, the circuit blasted open. The long-term price is "
            "relational: people remember being shamed far longer than they "
            "remember the trigger, and the exploder becomes someone others "
            "manage around rather than trust. Exploding also trains the "
            "alarm upward, because the drama rehearses the revulsion - "
            "each performance writes the tag deeper. Both failures share a "
            "root: the feeling was treated as either unspeakable or "
            "uncontrollable, when it is neither. It is speakable in "
            "measured words and controllable in measured actions. The "
            "repair for bottling is small honest outlets - name it, take "
            "the small action, let the circuit complete. The repair for "
            "exploding is the pause: feel the wave, choose the words, aim "
            "at the act not the actor. Neither repair is dramatic. That is "
            "the point - health, here, is beautifully boring."),
        "how_it_works": (
            "Bottling treats the signal as unspeakable: unexpressed, it "
            "ferments - generalizing, somaticizing, leaking sideways - "
            "while the ignored alarm escalates its volume. Exploding treats "
            "it as uncontrollable: the dramatic discharge rehearses the "
            "revulsion deeper and spends relational trust. Both train the "
            "alarm upward. The repairs are symmetric: small honest outlets "
            "for the bottler, the pause-and-aim for the exploder."),
        "key_points": [
            "Bottling looks like composure and costs like debt: tension now, fermenting generalization later.",
            "Unexpressed disgust leaks sideways - swallowed revulsion at lunch becomes a snap at someone by dinner.",
            "A consistently ignored signal gets louder, not quieter - the system concludes the message is not landing.",
            "Exploding buys immediate relief at relational prices: people remember the shaming longer than the trigger.",
            "Drama rehearses revulsion - each performance writes the contamination tag deeper.",
            "Repairs: small honest outlets for bottling; pause, choose words, aim at the act for exploding."],
        "requirements": [
            "No equipment needed - this is a reading and reflection record.",
            "Notice your own default: do you bottle or explode?",
            "A few quiet minutes."],
        "standards": [
            "Public record in the Signature system: fact-checked emotion psychology.",
            "Descriptive and educational only - general everyday guidance, never therapy.",
            "Human-readable sentences and paragraphs throughout."],
        "citations": [CIT_ROZIN_HAIDT, CIT_MILLER],
        "sig_lens": (
            "Signature lens: his Signature system files bottling as an "
            "unreported breach and exploding as a breached report - both "
            "are reporting failures, opposite in direction, identical in "
            "cost. The Signature archivist's fix is the proper chain of "
            "command restored: report up, measured and prompt, neither "
            "swallowed nor screamed. Good reporting is beautifully boring "
            "- and boring is what keeps the territory standing."),
    },
    {
        "key": "everyday-practices",
        "name": "Everyday Practices for Keeping Disgust in Balance",
        "group": "Healthy Expression",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Balance is not the absence of disgust - it is the alarm "
            "calibrated, responsive, and trusted. Small daily practices "
            "keep it there. One: the trigger journal, kept lightly. Once "
            "a day, note one disgust moment and its domain - \"break-room "
            "smell, domain six\" - and whether your response fit. A week "
            "of entries reveals your pattern: which domains fire most, "
            "where you overreact, where the alarm is wise. Two: the "
            "verification habit. Sniff the milk, glance at the date, check "
            "the cup - ten seconds of expectation hygiene prevents the "
            "ambushes that cost afternoons. Three: the breath-through. "
            "When nausea rises and you must stay - the caregiving task, "
            "the necessary chore - slow exhale breathing steadies the "
            "stomach; the wave is weather, and breath is the anchor. Four: "
            "proportionate cleansing. Wash, wipe, air - then stop. The "
            "rule: clean until the trigger is addressed, not until the "
            "feeling is zero; the feeling always lags the facts by a few "
            "minutes. Five: the exposure diet, taken gently. Deliberate, "
            "voluntary, small contacts with merely-unpleasant things - "
            "trying the unfamiliar dish, handling the garden soil - teach "
            "the alarm the difference between dangerous and merely new. "
            "Six: the moral check. When disgust fires at people or acts, "
            "pause and ask the source question - is this the act, or is it "
            "leakage, habit, or someone else's verdict I swallowed? Seven: "
            "recovery respect. After a big wave, give the body its "
            "schedule: bland food, rest, no forced cheer. None of these "
            "are dramatic. They are maintenance - the daily oiling of the "
            "gate's hinges. A maintained alarm is a trusted advisor: it "
            "fires when it should, stands down when it should, and never "
            "has to shout to be heard because it knows it will be "
            "listened to."),
        "how_it_works": (
            "Each practice tunes one part of the system: the journal maps "
            "the pattern, verification prevents ambushes, breath steadies "
            "the stomach, proportionate cleansing completes circuits "
            "without feeding loops, gentle exposure recalibrates the "
            "dangerous-versus-new distinction, the moral check filters "
            "leakage, and recovery respect repays the body's borrowed "
            "energy. Together they keep the signal-to-noise ratio high."),
        "key_points": [
            "Keep a light trigger journal: one entry a day reveals your pattern within a week.",
            "Practice verification: sniff, glance, check - ten seconds prevents afternoon-costing ambushes.",
            "Breath through the wave when you must stay: slow exhales steady the stomach; breath is the anchor.",
            "Cleanse proportionately: stop when the trigger is addressed, not when the feeling hits zero.",
            "Take a gentle exposure diet: small voluntary contacts teach the alarm dangerous versus merely new.",
            "Run the moral check on people-directed disgust, and give the body its recovery schedule after big waves."],
        "requirements": [
            "A notebook or notes app for the trigger journal.",
            "Willingness to try small daily habits.",
            "A few quiet minutes."],
        "standards": [
            "Public record in the Signature system: fact-checked emotion psychology.",
            "Descriptive and educational only - general everyday guidance, never therapy.",
            "Human-readable sentences and paragraphs throughout."],
        "citations": [CIT_HAIDT_DS, CIT_ROZIN_HAIDT],
        "sig_lens": (
            "Signature lens: his Signature system calls these the gate's "
            "maintenance roster - daily, unglamorous, non-negotiable. The "
            "Signature archivist posts it where every sentry sees it: "
            "journal the patrols, verify before contact, breathe through "
            "the weather, clean to completion not to zero, train on the "
            "merely-new, check the moral brief, resupply after musters. "
            "Maintained gates never have to shout."),
    },
    # ---------------- Recognizing it in others (records 29-31) ----------------
    {
        "key": "reading-others",
        "name": "Reading Disgust in Others",
        "group": "Recognizing It in Others",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Reading disgust in another person is a four-channel skill: "
            "face, body, voice, and behavior - and the channels rarely lie "
            "in the same direction. Start with the face: the nose wrinkle "
            "is the fastest, most honest tell. A quick crease of the "
            "bridge, a lift of the upper lip - even a flicker lasting a "
            "fraction of a second means the alarm fired. The eyes narrow, "
            "the gaze drops or slides away from the trigger. Next the "
            "body: the lean-back is the giveaway that survives politeness. "
            "Watch for the small retreat - shoulders pulling back, chin "
            "tucking, the whole torso adding inches of distance that the "
            "situation did not require. Hands go to the face (covering "
            "mouth and nose) or start managing distance (pushing the plate, "
            "setting down the cup, wiping fingers that are already clean). "
            "Then the voice: pitch rises a notch and tightens, words get "
            "shorter and more clipped, and the classic interjections slip "
            "out - \"ugh,\" \"ew\" - even from people trying to be "
            "gracious. Listen for the distancing \"that\": \"that's... "
            "interesting\" with a particular thinness means the verdict was "
            "not interesting at all. Finally behavior: declined food, "
            "untouched drinks, the sudden need to wash hands, the exit that "
            "arrives a little too promptly. Put the channels together "
            "before concluding. One channel alone can mislead - a nose "
            "wrinkle might be a bad smell in the hallway, not your cooking. "
            "Two or three channels pointing the same way is a reliable "
            "read. And read the baseline first: some people wrinkle their "
            "noses when they concentrate, some lean back when they think. "
            "The tell is the CHANGE - the wrinkle that was not there a "
            "moment ago, the lean that arrived with the dish. A final "
            "caution, and it matters: reading is for understanding, not "
            "for announcing. \"You look disgusted\" said aloud corners "
            "people; it turns a private alarm into a social incident. Read "
            "quietly, adjust kindly - open the window, change the subject, "
            "offer the alternative dish - and let your reading serve the "
            "person, not your cleverness."),
        "how_it_works": (
            "The four channels map to the rejection program's stages: face "
            "(sensory gating), body (distance), voice (throat engagement "
            "and clipped speech), behavior (avoidance, cleansing, exit). "
            "Reliability comes from convergence - two or more channels "
            "agreeing - measured against the person's baseline. The change "
            "from baseline is the signal; the absolute posture is just "
            "furniture."),
        "key_points": [
            "Read four channels: face (nose wrinkle, lip lift, averted gaze), body (lean-back, covering hands), voice (higher, tighter, clipped), behavior (declined food, washing, early exit).",
            "The nose wrinkle is the fastest, most honest tell - even a flicker means the alarm fired.",
            "The lean-back survives politeness: watch for distance the situation did not require.",
            "Listen for the distancing \"that\" - \"that's interesting\" in a thin voice is a verdict, not a compliment.",
            "Converge before concluding: two or three channels agreeing is reliable; one alone can mislead.",
            "Read the CHANGE from baseline, and read quietly - adjust kindly instead of announcing what you saw."],
        "requirements": [
            "No equipment needed - this is a reading and reflection record.",
            "Practice on crowds first, where the stakes are low.",
            "A few quiet minutes."],
        "standards": [
            "Public record in the Signature system: fact-checked emotion psychology.",
            "Descriptive and educational only - never diagnoses any real person.",
            "Human-readable sentences and paragraphs throughout."],
        "citations": [CIT_EKMAN, CIT_DARWIN],
        "sig_lens": (
            "Signature lens: his Signature system trains this as sentry "
            "observation - reading neighboring towers' flags to "
            "understand the territory's weather. The Signature archivist's "
            "code: observe to serve, never to expose. A flag read is "
            "intelligence for kindness - open the window, offer the other "
            "dish, change the subject. Sentries who announce every flag "
            "they see soon find no one wants them on the wall."),
    },
    {
        "key": "supportive-response",
        "name": "Responding Supportively to Someone Who Feels Disgust",
        "group": "Recognizing It in Others",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "When someone near you is riding the wave, the right response "
            "is simple, physical, and fast - because disgust is simple, "
            "physical, and fast. Step one: remove or reduce the trigger if "
            "you can. Open the window, take the plate away, close the lid, "
            "change the subject away from the story. Distance is the "
            "feeling's native language; speak it first. Step two: "
            "validate briefly and plainly. \"Yeah, that's rough,\" \"I "
            "see it too,\" \"let's get some air.\" Validation tells their "
            "system the alarm was heard - which, paradoxically, helps it "
            "stand down. Do not over-explain or analyze mid-wave; the "
            "thinking brain is offline and the stomach is in charge. Step "
            "three: offer the small physical comforts. Water (small sips), "
            "fresh air, a seat, a napkin, a moment alone. These are not "
            "profound gestures; they are exactly what the body is asking "
            "for. Step four: give it time without hovering. \"Take your "
            "time, no rush\" - then actually give it. The wave has a "
            "schedule and rushing it adds a second problem. With moral "
            "disgust - someone reeling from a betrayal or a cruelty "
            "witnessed - the same steps apply in translated form: reduce "
            "exposure (stop replaying the details), validate (\"what "
            "happened was wrong\"), offer steadiness (presence, not "
            "solutions), and give time. What helps across all forms: "
            "believing the feeling is real even if the trigger looks small "
            "to you. Their dial is not your dial. A trigger that is a two "
            "for you can be an eight for them, and \"it's not that bad\" "
            "is the fastest way to turn a wave into a wound. The gold "
            "standard is boring and beautiful: notice, reduce, validate, "
            "comfort, wait. No speeches. The wave passes; the kindness is "
            "remembered."),
        "how_it_works": (
            "Support works by answering the alarm's actual demands in "
            "order: distance (remove the trigger), acknowledgment "
            "(validation lowers the volume), physical reset (water, air, "
            "rest), and time (the wave's schedule honored). Believing the "
            "feeling despite dial differences prevents the secondary wound "
            "of dismissal. Each step maps to a stage of the rejection "
            "program; skipping to analysis while the stomach is in charge "
            "misfires."),
        "key_points": [
            "Speak the feeling's native language first: distance - remove the trigger, open the window, change the subject.",
            "Validate briefly and plainly: the alarm heard is the alarm that can stand down; save analysis for later.",
            "Offer small physical comforts: water in sips, fresh air, a seat, a moment alone.",
            "Give it time without hovering: the wave has a schedule, and rushing adds a second problem.",
            "For moral disgust, translate: reduce exposure to details, validate the wrongness, offer steady presence.",
            "Believe the feeling even when the trigger looks small to you - their dial is not your dial."],
        "requirements": [
            "No equipment needed - this is a reading and reflection record.",
            "Practice the five steps mentally before you need them.",
            "A few quiet minutes."],
        "standards": [
            "Public record in the Signature system: fact-checked emotion psychology.",
            "Descriptive and educational only - general everyday guidance, never therapy.",
            "Human-readable sentences and paragraphs throughout."],
        "citations": [CIT_ROZIN_HAIDT, CIT_EKMAN],
        "sig_lens": (
            "Signature lens: his Signature system treats support as "
            "allied-tower protocol - when the neighboring gate sounds its "
            "alarm, you do not debate the threat assessment; you open your "
            "postern, share water, and hold the line quietly. The "
            "Signature archivist's protocol: notice, reduce, validate, "
            "comfort, wait. Alliances are built in exactly these "
            "unremarkable minutes."),
    },
    {
        "key": "what-not-to-do",
        "name": "What Not to Do When Someone Feels Disgust",
        "group": "Recognizing It in Others",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Good intentions cause most of the damage here, because the "
            "instincts that help with sadness or fear backfire with "
            "disgust. Mistake one: mockery. Laughing at someone's gagging, "
            "calling them squeamish, performing exaggerated revulsion to "
            "tease - this turns a private alarm into a public humiliation, "
            "and the memory of the mockery will outlast the trigger by "
            "years. Mistake two: forced exposure. \"Just try it,\" "
            "\"it's all in your head,\" holding the thing closer, daring "
            "them to touch it. Forcing contact with a disgust trigger does "
            "not build toughness; it writes the tag deeper and teaches the "
            "person that you are not safe to feel around. Mistake three: "
            "minimizing. \"It's not that bad,\" \"you're overreacting.\" "
            "The feeling does not grade on your dial, and dismissal adds a "
            "second wound - now they are upset AND unheard. Mistake four: "
            "the lecture. Explaining the biology of the trigger, the "
            "statistics of its safety, the cultural relativity of disgust - "
            "while the wave is peaking. The thinking brain is offline; the "
            "lecture lands as noise, or worse, as proof you do not get it. "
            "Mistake five: making it about you. \"Well I'M not bothered,\" "
            "the competitive unflappability that turns their wave into your "
            "stage. Mistake six, the subtlest: the pity face. Exaggerated "
            "sympathy - the wide eyes, the \"oh you poor thing\" - which "
            "frames a normal alarm as a defect. What all six share: they "
            "answer the person's alarm with something about the responder "
            "- amusement, expertise, superiority, performance - instead of "
            "answering the alarm itself. The correction is always the same "
            "move: get out of the spotlight, get into the support steps. "
            "Reduce the trigger, validate briefly, offer water and air, "
            "give time. If you have already made one of these mistakes - "
            "everyone has - the repair is simple and complete: name it "
            "plainly (\"I shouldn't have laughed; that was a real wave "
            "you were riding\"), and do not repeat it. Repairs work. The "
            "alarm forgives; it is the mockery it remembers."),
        "how_it_works": (
            "Each mistake fails the same test: it responds to the "
            "responder's needs (amusement, expertise, dominance) instead "
            "of the alarm's needs (distance, validation, time). Mockery "
            "adds humiliation to the wave; forced exposure deepens the "
            "tag; minimizing adds the wound of dismissal; lecturing fires "
            "at an offline brain; self-centering steals the stage; pity "
            "frames normal as defective. The repair - plain naming plus "
            "non-repetition - works because it finally answers the alarm."),
        "key_points": [
            "Never mock: laughter at someone's gagging turns a private alarm into a humiliation remembered for years.",
            "Never force exposure: daring them to touch it writes the tag deeper and marks you unsafe.",
            "Never minimize: \"it's not that bad\" grades their wave on your dial and adds the wound of dismissal.",
            "Never lecture mid-wave: the thinking brain is offline; save the biology lesson for calm water.",
            "Never center yourself (\"well I'M not bothered\") and never pity-face a normal alarm into a defect.",
            "Made the mistake? Repair plainly - name it, do not repeat it. The alarm forgives; the mockery is what sticks."],
        "requirements": [
            "No equipment needed - this is a reading and reflection record.",
            "Honestly audit your last three responses to others' disgust.",
            "A few quiet minutes."],
        "standards": [
            "Public record in the Signature system: fact-checked emotion psychology.",
            "Descriptive and educational only - general everyday guidance, never therapy.",
            "Human-readable sentences and paragraphs throughout."],
        "citations": [CIT_EKMAN, CIT_ROZIN_HAIDT],
        "sig_lens": (
            "Signature lens: his Signature system posts these six as the "
            "allied-tower prohibitions - the things you never do when the "
            "neighboring gate is sounding. The Signature archivist is "
            "blunt: mockery, force, dismissal, lectures, stage-stealing, "
            "and pity are all ways of answering your own needs while "
            "wearing a helper's uniform. Strip the uniform off, do the "
            "simple steps, and repair plainly when you fail. Towers that "
            "follow the prohibitions hold alliances for decades."),
    },
    # ---------------- Related emotions, mixes, simulation (records 32-34) ----------------
    {
        "key": "neighbors",
        "name": "The Disgust Neighbors: Related Emotions and How to Tell Them Apart",
        "group": "Related Emotions and Simulation",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Disgust has close cousins, and mistaking one for another "
            "leads to wrong responses. Here is the neighborhood map with "
            "the tells that separate them. CONTEMPT is the nearest "
            "neighbor and the easiest confusion. Both reject, but contempt "
            "is cold and hierarchical while disgust is hot and horizontal. "
            "Contempt looks DOWN - the one-sided smirk, the eye-roll, the "
            "sense of superiority; its urge is to dismiss and diminish. "
            "Disgust pushes AWAY - the bilateral nose wrinkle, the lean-"
            "back; its urge is to expel and distance. Tell: asymmetry "
            "(contempt) versus symmetry (disgust); looking down versus "
            "pulling back. ANGER confronts where disgust retreats. Both "
            "can fire at the same moral violation, but anger wants to "
            "engage the offender and disgust wants the offender gone. "
            "Tell: the lean - forward (anger) versus back (disgust); the "
            "jaw - clenched for battle (anger) versus the lip curled for "
            "spitting (disgust). FEAR flees danger; disgust flees "
            "contamination. A snarling dog triggers fear (it might hurt "
            "me); a rotting carcass triggers disgust (it might taint me). "
            "Tell: the body - trembling readiness (fear) versus nausea and "
            "the gag (disgust); the question - \"will it harm me?\" versus "
            "\"will it foul me?\" SHAME is disgust turned inward - the "
            "same rejection, aimed at the self. The face even rhymes: the "
            "averted gaze, the wish to disappear. Tell: the target - "
            "outward at the thing (disgust) versus inward at the self "
            "(shame); the hiding - of the object versus of the face. HATRED "
            "is the long-term tenant: sustained, personalized, and cold in "
            "a way disgust rarely is. Disgust wants distance; hatred wants "
            "the other's diminishment or destruction. Tell: the timeline - "
            "disgust fades with distance, hatred feeds on rumination. "
            "ENVY and JEALOUSY live further out - they want what another "
            "has (envy) or fear losing what one has (jealousy); neither "
            "carries the nausea-gag signature. The map's practical use is "
            "triage. Name the right neighbor and the right protocol "
            "follows: contempt needs humility work, anger needs boundaries "
            "and words, fear needs safety, shame needs self-compassion and "
            "repair, hatred needs interruption. Disgust needs distance, "
            "cleansing, and circuit completion. Similar faces, different "
            "medicines - the map keeps the pharmacy straight."),
        "how_it_works": (
            "Each neighbor is separated by two axes: the action urge "
            "(dismiss, confront, flee, hide, destroy, distance) and the "
            "body signature (smirk versus wrinkle, lean-forward versus "
            "lean-back, trembling versus nausea). The tell in every case "
            "is a visible or felt difference along one of the axes. "
            "Correct identification routes to the correct protocol, "
            "because each emotion's remedy matches its urge."),
        "key_points": [
            "Contempt is cold and hierarchical (looks down, one-sided smirk); disgust is hot and horizontal (pushes away, bilateral wrinkle).",
            "Anger leans forward to confront; disgust leans back to expel - the jaw clenched versus the lip curled.",
            "Fear asks \"will it harm me?\" (trembling); disgust asks \"will it foul me?\" (nausea and gag).",
            "Shame is disgust turned inward: same rejection, target the self; the hiding is of the face, not the object.",
            "Hatred is the long-term tenant: disgust fades with distance, hatred feeds on rumination.",
            "Name the right neighbor for the right medicine: distance for disgust, boundaries for anger, safety for fear, repair for shame."],
        "requirements": [
            "No equipment needed - this is a reading and reflection record.",
            "Test the tells on your last three ambiguous feelings.",
            "A few quiet minutes."],
        "standards": [
            "Public record in the Signature system: fact-checked emotion psychology.",
            "Descriptive and educational only - never diagnoses any real person.",
            "Human-readable sentences and paragraphs throughout."],
        "citations": [CIT_ROZIN_HAIDT, CIT_EKMAN, CIT_MILLER],
        "sig_lens": (
            "Signature lens: his Signature system keeps the neighbor map "
            "posted at every gate - because the wrong protocol on the "
            "right alarm is how territories get mismanaged. The Signature "
            "archivist's triage drill: urge plus body equals name, name "
            "equals protocol. Run the drill before acting and the pharmacy "
            "stays straight; skip it and you will treat nausea with "
            "courage or fear with mops."),
    },
    {
        "key": "mixes",
        "name": "Disgust Mixes: Blends with Other Emotions",
        "group": "Related Emotions and Simulation",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Pure disgust is the laboratory case; real life serves blends. "
            "Here are the four great mixtures, each with its own weather. "
            "DISGUST plus FEAR makes HORROR. The trigger both fouls and "
            "threatens: the wound that might be infected, the dark water "
            "with something moving in it, the disease ward. The body runs "
            "both programs at once - nausea AND trembling, the gag AND the "
            "adrenaline - and the urges tangle: flee the danger, expel the "
            "contamination, in whichever order survival allows. Horror is "
            "the blend that empties rooms fastest. DISGUST plus ANGER "
            "makes OUTRAGE, the blend from record eight, revisited here as "
            "mixture: the foul act plus the demand for confrontation. The "
            "contamination tag marks the offender as tainted; the anger "
            "demands they answer. This is the weather of scandals, "
            "betrayals exposed, cruelties witnessed. Handled well it "
            "cleans communities; handled badly it becomes the mob. "
            "DISGUST plus SADNESS makes GRIEF AT DECAY. The ruined "
            "garden, the wasted feast, the friendship rotted by lies - the "
            "rejection softens into mourning for what the rot took. The "
            "body is heavy rather than heaving; the tears are for loss, "
            "not for expulsion. This blend needs comfort more than "
            "distance - the trigger is already gone; what remains is the "
            "absence. DISGUST plus SURPRISE makes SHOCK-REVULSION, the "
            "ambush blend: the unexpected discovery, the sudden sight, "
            "the joke whose punchline curdles. The startle multiplies the "
            "wave (record twenty's mechanism), and the aftermath includes "
            "a peculiar replay - the mind re-running the moment of "
            "discovery as if checking the locks. Each blend follows the "
            "same reading rule: name the ingredients, honor both urges, "
            "sequence the response. Horror: safety first, cleansing "
            "second. Outrage: distance first, words second, mob never. "
            "Grief at decay: comfort first, cleanup when ready. "
            "Shock-revulsion: ride the wave, then verify the locks once "
            "and stop. The blends are not exotic - they are the normal "
            "form of strong feeling. Learning them is learning to read "
            "weather instead of just temperature."),
        "how_it_works": (
            "Each blend adds disgust's rejection program to a partner's "
            "program: fear's flight (horror), anger's confrontation "
            "(outrage), sadness's withdrawal into mourning (grief at "
            "decay), surprise's startle multiplier (shock-revulsion). The "
            "body shows both signatures simultaneously. The response rule "
            "is sequencing: answer the louder ingredient's urge first, "
            "then the quieter, never both at once and never neither."),
        "key_points": [
            "Disgust plus fear is HORROR: nausea and trembling together; the blend that empties rooms fastest.",
            "Disgust plus anger is OUTRAGE: the foul act plus the demand for confrontation - cleans communities or becomes the mob.",
            "Disgust plus sadness is GRIEF AT DECAY: rejection softened into mourning; needs comfort more than distance.",
            "Disgust plus surprise is SHOCK-REVULSION: the ambush blend; the startle multiplies the wave.",
            "Read every blend by ingredients: name both, honor both urges, sequence the response.",
            "Blends are the normal form of strong feeling - learn weather, not just temperature."],
        "requirements": [
            "No equipment needed - this is a reading and reflection record.",
            "Identify the blend in your last strong emotional weather.",
            "A few quiet minutes."],
        "standards": [
            "Public record in the Signature system: fact-checked emotion psychology.",
            "Descriptive and educational only - never diagnoses any real person.",
            "Human-readable sentences and paragraphs throughout."],
        "citations": [CIT_ROZIN_HAIDT, CIT_TYBUR, CIT_CHAPMAN],
        "sig_lens": (
            "Signature lens: his Signature system files the four blends "
            "as combined-arms alarms - two towers sounding as one, each "
            "with its own protocol, sequenced by volume. The Signature "
            "archivist's battle drill: loudest tower first, then the "
            "second, never both at once, never neither. Outrage gets "
            "distance before words; horror gets safety before scrubbing. "
            "Sequenced alarms save territories; tangled ones burn them."),
    },
    {
        "key": "full-simulation",
        "name": "Full Behavioral Simulation: Disgust from Trigger to Resolution",
        "group": "Related Emotions and Simulation",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The archive's showcase piece: one emotion, walked all the way "
            "from trigger to resolution across five scenes. This is a "
            "simulation - described, educational, diagnosing no one. "
            "SCENE ONE: the trigger. A neighborhood potluck, late "
            "afternoon. Mara sets her famous potato salad on the table at "
            "4:40. By 6:15 it has sat in warm air for ninety minutes, and "
            "when Jonas lifts the lid the smell hits him mid-reach - sour, "
            "wrong, unmistakable. Onset is instant: his nose wrinkles, his "
            "upper lip lifts, his head turns before he decides. The inner "
            "monologue is one word: no. SCENE TWO: the peak. The wave "
            "takes the table. Two others catch the ripple - visible nose "
            "wrinkles, a pushed-back chair. Jonas sets the lid down "
            "carefully, steps back, breathes through his mouth. His "
            "stomach gives one hard roll; he swallows against it. Someone "
            "laughs nervously. Mara, arriving with cups, reads the faces "
            "in a glance - the convergence of three wrinkled noses tells "
            "her everything. Her own flash is different: embarrassment "
            "rising, the shame-adjacent heat of the host whose dish "
            "failed. SCENE THREE: the cascade. Jonas feels the chain "
            "forming - disgust at the smell, then irritation flaring "
            "(why did nobody refrigerate it?), then the check: is the "
            "irritation at anyone, or just the wave talking? He names it "
            "silently - wave first, verdict later - and the anger-ingredient "
            "stands down unfed. Mara quietly carries the bowl to the "
            "kitchen, dumps it, washes her hands twice. The cleansing "
            "answers the contamination tag; her shoulders drop a full "
            "inch. SCENE FOUR: the repair. Mara returns, frank and "
            "unforced: \"well, that one's dead - my fault, it sat too "
            "long.\" The table exhales; someone makes the joke that "
            "defuses the rest (\"the potato salad has left the "
            "building\"). Jonas, stomach settled, takes her at her word - "
            "no lecture, no mockery, no pity face. He offers to help carry "
            "things instead. The social circuit completes the way the "
            "physical one did: trigger addressed, dignity intact. SCENE "
            "FIVE: the aftershock and the filing. At 9:00 PM, home, Jonas "
            "catches a faint sour note from his own fridge and gets the "
            "echo - a half-second stomach tightening, then recognition: "
            "\"that's the echo, not a new alarm.\" He checks the milk "
            "(expectation hygiene), finds it fine, and the echo fades "
            "unfed. Mara, washing up, files her own lesson without drama: "
            "cold dishes stay cold, ninety minutes is the line. The alarm "
            "did its job - protected the table, taught the host, cost one "
            "dish and zero friendships. Walk the five scenes again and "
            "count the skills in play: instant onset read, peak ridden not "
            "fought, cascade traced to its first link, cleansing to "
            "completion, repair without mockery, echo recognized and "
            "starved. That is the whole database in one evening - the "
            "archive's complete simulation of disgust, from trigger to "
            "resolution."),
        "how_it_works": (
            "The simulation stages the full mechanism across five scenes: "
            "trigger and instant onset (sensory detection, face-first "
            "response), peak with social ripple (convergence read by the "
            "host), cascade and chain-tracing (the anger-ingredient named "
            "and stood down), repair (frank admission, humor, no mockery), "
            "and aftershock management (echo recognized, verification, "
            "lesson filed). Each scene demonstrates records from earlier "
            "in the ladder, compounding them into one continuous run."),
        "key_points": [
            "Scene one - trigger: ninety warm minutes, one lifted lid, instant onset; the inner monologue is one word: no.",
            "Scene two - peak: the ripple crosses the table; the host reads three converging noses; her flash is embarrassment.",
            "Scene three - cascade: irritation flares and is traced to the wave, not a person; cleansing completes the circuit.",
            "Scene four - repair: frank admission plus defusing humor; no lecture, no mockery, no pity face.",
            "Scene five - aftershock: the evening echo is recognized, verified, and starved; the lesson files cleanly.",
            "The whole ladder in one evening: onset read, peak ridden, cascade traced, circuit completed, echo managed."],
        "requirements": [
            "No equipment needed - this is a reading and simulation record.",
            "Read the five scenes in order, slowly, like a short film.",
            "Remember: a simulation describing the feeling, never any real person."],
        "standards": [
            "Public record in the Signature system: fact-checked emotion psychology.",
            "Descriptive and educational only - a simulation, never a diagnosis.",
            "Human-readable sentences and paragraphs throughout."],
        "citations": [CIT_ROZIN_HAIDT, CIT_EKMAN, CIT_MILLER],
        "sig_lens": (
            "Signature lens: his Signature system screens this simulation "
            "as the gate's training film - shown to every new sentry "
            "before their first solo watch. The Signature archivist's "
            "closing note on the film: this is what right looks like. "
            "Alarm sounded, wave ridden, cascade traced, circuit "
            "completed, repair made, echo starved, lesson filed - one dish "
            "lost, zero friendships lost, territory cleaner than before. "
            "Run the film until the sequence is reflex."),
    },
]

assert len(ENTRIES) == 34, "expected 34 entries, got %d" % len(ENTRIES)
_ranks = [e["ladder_rank"] for e in ENTRIES]
assert _ranks == sorted(_ranks), "entries not in ladder order"
assert all(1 <= r <= 10 for r in _ranks), "ladder_rank out of range"
_tiers = [e["ladder_tier"] for e in ENTRIES]
assert all(t in ("foundations", "compounded", "advanced") for t in _tiers)
_keys = [e["key"] for e in ENTRIES]
assert len(set(_keys)) == 34, "duplicate entry keys"
for e in ENTRIES:
    for k in ("key", "name", "group", "ladder_rank", "ladder_tier",
              "description", "how_it_works", "key_points", "requirements",
              "standards", "citations", "sig_lens"):
        assert k in e, "missing %s" % k
    assert len(e["description"]) > 200, "stub description: %s" % e["key"]
    blob = (e["description"] + e["how_it_works"] + " ".join(
        e["key_points"]) + e["sig_lens"]).lower()
    assert "facebook" not in blob
    assert "bat belt" not in blob
