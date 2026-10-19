#!/usr/bin/env python3
"""34 ladder-ordered entries for the Shame Emotion databases
(Manon's 2026-10-17 16:15 order, emotion series).

Public edition: real, fact-checked descriptive psychology of shame -
Darwin, Ekman, Tangney, Lewis, Izard, Lazarus, Gross, Scheff, Nathanson,
APA Dictionary (src public-harvest).
Signature edition: his original Signature lens - shame as the mirror of
the true self, the honor alarm that guards who a person is becoming -
framed as signal, fuel, and mastery (src signature, titles suffixed
" (Signature Edition)").

Descriptive and educational ONLY. These entries describe and simulate
the emotion; they never diagnose real people, never label any real person
with an emotional state, and offer therapeutic advice only in the form of
general, safe, everyday guidance. No clinical language, no diagnostic
labels. Screened: nothing hate-adjacent, profane, or inappropriate; no
religious framing; no website or Facebook references.

ladder_rank runs 1..34 in template order: what shame IS (1-4) -> how it
feels (5-9) -> body signals (10-13) -> facial expression (14-17) ->
triggers (18-21) -> behavior (22-25) -> healthy expression (26-28) ->
recognizing in others (29-31) -> related emotions, mixes, full simulation
(32-34).
"""

SIG_TAIL = ("Signature original - his original Signature lens: shame as the "
            "mirror of the true self, the honor alarm that guards who a "
            "person is becoming; Signature editions frame every facet as "
            "signal, fuel, and mastery - never as a diagnosis, never labeling "
            "any real person, and never presented as authentic public record.")

CIT_APA = ("American Psychological Association. APA Dictionary of Psychology "
           "- shame: a highly unpleasant self-conscious emotion arising from "
           "the sense of being flawed or unworthy in the eyes of others or "
           "oneself; distinguished from guilt, which focuses on the act "
           "rather than the self.")
CIT_DARWIN = ("Darwin C. The Expression of the Emotions in Man and Animals "
              "(1872) - blushing described as the most human of all "
              "expressions, the visible signature of shame and shyness: "
              "reddening of the face and neck under the eyes of others.")
CIT_EKMAN = ("Ekman P. Emotions Revealed (2003) - shame discussed among the "
             "self-conscious emotions; its signal set includes gaze aversion, "
             "head lowering, and the wish to disappear from the sight of "
             "others.")
CIT_TANGNEY = ("Tangney J. P. and Dearing R. L. Shame and Guilt (2002) - the "
               "self-behavior distinction: shame judges the whole self "
               "(\"I am bad\"), guilt judges the specific act (\"I did "
               "bad\"); shame predicts withdrawal, guilt predicts repair.")
CIT_LEWIS = ("Lewis M. Shame: The Exposed Self (1992) - shame as the emotion "
             "of the exposed self: the self becomes both subject and object, "
             "seen and judged in the light of one's own standards.")
CIT_IZARD = ("Izard C. E. Human Emotions (1977) - differential emotions theory "
             "lists shame among the fundamental emotions, present from early "
             "childhood once self-awareness emerges.")
CIT_LAZARUS = ("Lazarus R. S. Emotion and Adaptation (1991) - appraisal "
              "theory: shame follows the appraisal of having failed to live "
              "up to an ego-ideal, with the self exposed before a real or "
              "imagined audience.")
CIT_GROSS = ("Gross J. J. Emotion regulation research - strategies of "
            "reappraisal, expression, and situation modification that can "
            "steer the intensity and course of self-conscious emotions such "
            "as shame.")
CIT_SCHEFF = ("Scheff T. J. Shame and the social bond (1988) - shame as the "
              "master emotion of social life: the signal of a threatened "
              "social bond, felt in every gradation from embarrassment to "
              "humiliation.")
CIT_NATHANSON = ("Nathanson D. L. Shame and Pride (1992) - affect theory: "
                "shame as the affect that interrupts interest and joy, "
                "producing the characteristic slump, averted gaze, and "
                "silence.")

ENTRIES = [
{
 "key": "shame_definition",
 "name": "What Shame Is: A Plain-Language Definition",
 "group": "Foundations", "ladder_rank": 1, "ladder_tier": "foundations",
 "description": ("Shame is the emotion of being seen as less than you want to "
  "be seen. In everyday words: shame is the hot-faced, shrinking feeling "
  "that washes over you when you believe you have fallen short - of your own "
  "standards, of other people's expectations, or of the person you are trying "
  "to be - and someone might notice. It is not about what you did so much as "
  "about who you fear you are in that moment: exposed, judged, and found "
  "wanting. Shame says, in its own wordless language, \"I am the problem,\" "
  "which is why it makes people want to hide, disappear, or sink through "
  "the floor. Unlike emotions that point outward at the world, shame points "
  "the spotlight inward, at the self, and asks the most painful question a "
  "feeling can ask: \"Am I enough?\""),
 "how_it_works": ("Shame runs on a simple three-part machine: a standard, an "
  "exposure, and an audience. First there is a standard - something you "
  "believe about who you should be: competent, honest, attractive, loyal, "
  "in control. Second, something happens that seems to show you violating "
  "that standard: a stumble, a revealed secret, a public mistake, a "
  "private thought that shames you even with no one else in the room. Third "
  "comes the audience - real or imagined - in whose eyes you now picture "
  "yourself diminished. That imagined seeing is the engine of shame; people "
  "feel ashamed alone in an empty room because the audience lives inside the "
  "mind. Once the circuit closes - standard broken, self exposed, judged by "
  "others - the body responds with the ancient submission display: gaze "
  "drops, head lowers, shoulders round, blood rushes to the face. The whole "
  "system is built to make the shamed person smaller, quieter, and less "
  "visible - the body's way of saying \"I am no threat, please do not "
  "reject me.\""),
 "key_points": [
  "Shame is a self-conscious emotion: it judges the whole self (\"I am bad\"), not just the act.",
  "Its three moving parts are a standard, an exposure, and an audience - real or imagined.",
  "Shame can fire with no one else present; the mind supplies the watching eyes.",
  "The body answers shame with a submission display: smaller posture, dropped gaze, blushing.",
  "Shame is a social emotion first: its deepest fear is rejection and loss of belonging."],
 "requirements": [
  "Describe shame in plain everyday words before any technical framing.",
  "Keep the self-versus-act distinction (shame = the self, guilt = the act) visible throughout.",
  "Never describe any real person as shamed or shameful; all examples stay fictional and general.",
  "Treat shame as one normal human emotion among many, not as a defect or disorder."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people, no therapeutic promises."],
 "citations": [CIT_APA, CIT_LEWIS],
 "sig_lens": ("The Signature lens reads shame as the mirror of the true self: "
  "the moment the soul holds up a looking glass and the reflection does not "
  "match the person you are building. It is not an enemy to be destroyed; it "
  "is an instrument reading - a signal that something you care about is "
  "unfinished, misaligned, or exposed before its time. Mastery begins by "
  "reading the instrument instead of smashing the mirror."),
},
{
 "key": "shame_emotion_family",
 "name": "Shame in the Emotion Family",
 "group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
 "description": ("Shame belongs to the family of self-conscious emotions - "
  "the feelings that need a self to look at itself, which is why small "
  "children do not show true shame until self-awareness arrives, roughly in "
  "the second year of life. Its closest relatives are guilt, embarrassment, "
  "humiliation, and pride; together they form the social thermostat that "
  "regulates how people behave around one another. In the family tree, shame "
  "sits one level down from fear and sadness - it borrows fear's alarm "
  "about social rejection and sadness's heaviness about loss - but it adds "
  "something neither has: the self as its own judge and jury. Below shame "
  "branch the milder cousins: embarrassment (brief, situational, often "
  "shared and laughed off), shyness (the anticipation of shame before "
  "strangers), and mortification (shame at its most extreme, the wish to "
  "die of shame being literal language, not poetry). Above it sits its "
  "opposite pole, pride - the warm expansion of the self under approval - "
  "which shows that the same machinery that punishes also rewards."),
 "how_it_works": ("The family works as a gradient of self-evaluation under "
  "observation. At the mild end, embarrassment flares when a small "
  "social rule is broken in front of witnesses - tripping on a flat floor, "
  "calling someone by the wrong name - and it fades as soon as the moment "
  "passes, often with shared laughter. Shyness is embarrassment projected "
  "forward: the dread of being judged before anything has happened. Shame "
  "proper is the deeper, stickier state: the failure is read as evidence "
  "about the self, not the situation, so it does not wash off with the "
  "moment. Humiliation is shame with an added perpetrator - someone "
  "deliberately exposed or degraded you - which mixes in anger at the "
  "humiliator. At the far end, toxic or chronic shame is the state where "
  "the self-judgment becomes a standing verdict, coloring everything. The "
  "family rule: the more the feeling is about the self rather than the "
  "situation, and the more deliberate the exposure, the heavier and longer "
  "the emotion runs."),
 "key_points": [
  "Shame is a self-conscious emotion; it appears only once self-awareness develops.",
  "Its nearest family: guilt, embarrassment, humiliation, shyness, mortification, pride.",
  "Embarrassment is situational and brief; shame is about the self and lingers.",
  "Humiliation adds a deliberate exposer, which mixes anger into the shame.",
  "Pride is the opposite pole - the same self-evaluation machinery running in reward mode."],
 "requirements": [
  "Place shame in the family tree before discussing any single relative in depth.",
  "Distinguish situational embarrassment from self-judging shame clearly.",
  "Use only fictional, general examples; no real person is ever labeled.",
  "Present the family as a normal regulatory system, not a catalog of problems."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people, no therapeutic promises."],
 "citations": [CIT_IZARD, CIT_SCHEFF],
 "sig_lens": ("The Signature lens maps the family as a court of the soul: "
  "embarrassment the town crier announcing a small slip, shame the judge "
  "reading the verdict, humiliation the judge with a hostile prosecutor, "
  "and pride the herald announcing a victory. Same courtroom, different "
  "sessions - and the wise learn to attend court without living there."),
},
{
 "key": "shame_intensity_scale",
 "name": "How Strong Shame Can Get: Mild, Moderate, Intense",
 "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
 "description": ("Shame is one emotion with a volume knob. At mild volume it "
  "is a passing pink flush: you mispronounce a word in a meeting, feel the "
  "warmth rise, smile it off, and forget it by lunch. The self is "
  "untouched; only the moment stung. At moderate volume the feeling settles "
  "in: a real failure in front of people who matter - bombing a "
  "presentation, being called out for a mistake, having a flaw pointed out "
  "- leaves a heaviness that follows you through the day, replays in "
  "quiet moments, and makes you rehearse what you should have said. At full "
  "intensity, shame becomes a state of being: the exposure feels total, the "
  "judgment feels permanent, and the self feels branded. Time slows, the "
  "body wants to vanish, speech dries up, and the mind loops the scene "
  "endlessly. The same machinery drives all three volumes; what changes is "
  "how central the failure feels to the self, how important the audience "
  "is, and how inescapable the exposure seems. Knowing the scale matters "
  "because mild shame is a useful social signal while intense shame is a "
  "storm to be weathered, not obeyed."),
 "how_it_works": ("The volume is set by three dials multiplied together: "
  "how central the standard is to your identity, how high-status or "
  "important the audience feels, and how public and permanent the exposure "
  "seems. A spelling error in a private note scores low on all three - mild. "
  "The same error projected on a screen in front of mentors scores high on "
  "audience and exposure - moderate to intense. When all three dials max "
  "out - a core identity standard, the people whose respect matters most, "
  "and an exposure that cannot be taken back - the knob turns all the way "
  "up and the emotion floods the whole system. Intensity also stretches "
  "time: mild shame decays in minutes, moderate shame in hours to days, "
  "intense shame can echo for years whenever a reminder appears. The "
  "practical use of the scale is triage: match the response to the volume. "
  "Mild shame wants a shrug and a smile; moderate shame wants repair or "
  "reappraisal; intense shame wants time, distance, and safe company - and "
  "never a major life decision made in the middle of the flood."),
 "key_points": [
  "Mild shame is a passing flush; the self is untouched and the moment fades fast.",
  "Moderate shame replays through the day and makes you rehearse what you should have done.",
  "Intense shame feels total and permanent, with looping thoughts and the wish to vanish.",
  "Three dials set the volume: identity-centrality, audience importance, exposure permanence.",
  "Match the response to the volume: shrug at mild, repair at moderate, weather the intense."],
 "requirements": [
  "Present the three volumes as one emotion at different settings, not three different emotions.",
  "Give a concrete fictional snapshot at each volume.",
  "Keep all guidance general and safe; no therapeutic prescriptions for intense states.",
  "Never suggest any real person is experiencing any level of shame."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people, no therapeutic promises."],
 "citations": [CIT_APA, CIT_TANGNEY],
 "sig_lens": ("The Signature lens treats the volume knob as an instrument "
  "dial: low readings are navigation pings, mid readings are course "
  "corrections, and full-scale readings are storm warnings. The master does "
  "not pretend the dial reads zero, and does not steer by the storm - he "
  "reads the gauge, logs what it says about his standards, and adjusts "
  "course in calm water."),
},
{
 "key": "shame_myths",
 "name": "Myths and Misunderstandings About Shame",
 "group": "Foundations", "ladder_rank": 4, "ladder_tier": "foundations",
 "description": ("Shame is one of the most misunderstood emotions, and the "
  "myths around it do real damage. Myth one: shame and guilt are the same "
  "thing. They are not - guilt says \"I did something bad\" and pushes "
  "toward fixing it; shame says \"I am bad\" and pushes toward hiding. Myth "
  "two: shame is always destructive and should be eliminated. In truth, "
  "mild shame is a social compass - the blush that keeps people honest, "
  "apologetic, and considerate; a person incapable of shame is not "
  "liberated but dangerous to be around. Myth three: only guilty people "
  "feel shame. Innocent people feel it constantly - survivors of "
  "mistreatment, people mocked for things they cannot control, anyone "
  "caught in public embarrassment. Myth four: shamelessness is strength. "
  "It is usually just numbness, armor, or the volume turned down so far "
  "the signal cannot get through - and the signal was carrying information. "
  "Myth five: talking about shame makes it worse. Careful, kind "
  "conversation in safe company is one of the few things that reliably "
  "shrinks it; shame grows fastest in secrecy, which is exactly where it "
  "wants you to keep it."),
 "how_it_works": ("Each myth survives because it contains a grain of truth "
  "viewed from the wrong angle. Shame and guilt do travel together - most "
  "real failures trigger both, which is why people merge them. Shame is "
  "destructive at high volume and high duration, which makes the milder, "
  "useful form invisible. Innocent people feel shame because the emotion "
  "tracks perceived exposure, not actual wrongdoing - the machinery cannot "
  "tell the difference between \"I did wrong\" and \"they are looking at "
  "me like I did.\" Shamelessness looks like strength because the "
  "shame-prone often envy the unflappable, not noticing the cost: without "
  "the signal, there is no correction. And secrecy feels protective "
  "because shame's oldest instruction is \"hide\" - but hiding is what "
  "feeds it, since nothing in the dark ever gets re-examined. Clearing the "
  "myths matters because each one pushes the same bad strategy: hide it, "
  "deny it, or mistake it for something else."),
 "key_points": [
  "Shame and guilt differ: shame judges the self, guilt judges the act.",
  "Mild shame is a useful social compass, not a defect to eliminate.",
  "Innocent people feel shame; the emotion tracks perceived exposure, not actual wrongdoing.",
  "Shamelessness is usually numbness or armor, not strength.",
  "Shame grows in secrecy and shrinks in safe, kind conversation."],
 "requirements": [
  "State each myth plainly, then correct it with the factual account.",
  "Keep the shame-versus-guilt distinction central.",
  "Avoid clinical vocabulary; describe, do not diagnose.",
  "All examples fictional and general; no real person labeled."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people, no therapeutic promises."],
 "citations": [CIT_TANGNEY, CIT_APA],
 "sig_lens": ("The Signature lens names the myths as fog on the mirror: "
  "each myth is a smudge that distorts the reading. Wipe the fog - learn "
  "what the instrument actually measures - and shame stops being a monster "
  "in the dark and becomes a gauge with a needle, a scale, and a purpose."),
},
]

ENTRIES += [
{
 "key": "shame_first_person",
 "name": "Inside Shame: A First-Person Passage",
 "group": "Foundations", "ladder_rank": 5, "ladder_tier": "foundations",
 "description": ("To know shame from the inside, imagine this: you are "
  "standing in a room and every eye has found you at once. Heat climbs your "
  "neck and face like a tide; you can feel the redness, which makes it "
  "worse, because now they can see that you know. Your gaze drops to the "
  "floor - not by decision, by gravity - and your shoulders pull inward as "
  "if your body is trying to fold itself out of sight. Time thickens. The "
  "room's sounds go distant and tinny while your own heartbeat goes loud. "
  "A single sentence loops in your head, not in words exactly but in weight: "
  "they see me, they see it, I am smaller than I was a minute ago. You want "
  "two impossible things at once: to vanish, and for everyone to "
  "immediately forget this ever happened. If you must speak, your voice "
  "comes out thinner and higher than you intended, and you hate the sound "
  "of it. If you can move, you move toward the door, the corner, anywhere "
  "with fewer eyes. This is the signature of the emotion from the inside: "
  "exposure plus judgment, felt in the skin before it is ever put into "
  "words."),
 "how_it_works": ("The first-person sequence is driven by attention: shame "
  "yanks the spotlight of awareness off the world and onto the self. "
  "Normally attention flows outward - at tasks, people, the environment. "
  "The moment shame fires, attention reverses and the self becomes the "
  "object under inspection. That reversal explains the tunnel feeling: the "
  "room recedes because perception is now aimed inward at the imagined "
  "audience's view of you. The body follows the same logic - the "
  "submission display is the organism's ancient negotiation with a "
  "stronger party: make yourself small, avoid the dominant gaze, signal "
  "no threat. Speech degrades because the vocal apparatus is now being "
  "monitored by the same harsh audience; every word is previewed, judged, "
  "and usually swallowed. The loop persists because each sign of shame - "
  "the blush, the stammer, the retreat - is itself witnessed by the inner "
  "audience and read as further evidence, feeding the feeling that produced "
  "it. Understanding this loop is the first step to stepping outside it: "
  "the feeling is a spotlight, not a verdict."),
 "key_points": [
  "Shame reverses attention: the spotlight swings off the world and onto the self.",
  "The signature inner line is exposure plus judgment - being seen and found wanting.",
  "The body folds inward by ancient reflex: smaller, quieter, gaze down, toward the exit.",
  "Speech thins because every word is previewed by the imagined audience.",
  "Shame feeds itself: each visible sign of shame becomes new evidence for the inner judge."],
 "requirements": [
  "Write the passage in second-person present tense to simulate the lived feeling.",
  "Keep it descriptive of the emotion's texture, never directed at the reader's real life.",
  "No clinical terms; use sensory, bodily language.",
  "Stay fictional and general; no real person is described as feeling this."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people, no therapeutic promises."],
 "citations": [CIT_LEWIS, CIT_DARWIN],
 "sig_lens": ("The Signature lens calls this passage the mirror-room: the "
  "soul locked in a hall of mirrors where every reflection is the same "
  "accusing face. The master's move is to notice the room itself - the "
  "feeling is weather inside a chamber, and chambers have doors. You are "
  "the one standing in the room, not the reflections on its walls."),
},
{
 "key": "shame_time_course",
 "name": "Shame Over Time: Onset, Peak, Fading, Aftershock",
 "group": "Foundations", "ladder_rank": 6, "ladder_tier": "foundations",
 "description": ("Shame has a shape in time, and knowing the shape makes it "
  "survivable. Onset is fast - seconds. One glance, one sentence, one "
  "realization, and the heat is already in your face before you have named "
  "what happened. The peak arrives within a minute or two: the full "
  "submission display, the looping thought, the wish to disappear. This is "
  "the worst of it, and it is also mercifully brief in its pure form - the "
  "body cannot hold maximum alarm indefinitely. Fading follows over "
  "minutes to hours: the heat drains, the shoulders unlock a degree, "
  "attention begins to leak back out to the world. But shame, unlike "
  "startle or surprise, has a long tail - the aftershock. Hours or days "
  "later, a quiet moment replays the scene uninvited; a similar room, a "
  "similar face, a similar risk re-triggers a smaller echo. The aftershocks "
  "decay if nothing feeds them - each replay slightly weaker - but they "
  "can be recharged by retelling the story to yourself in the same harsh "
  "words, or by avoiding every situation that resembles the original. The "
  "whole arc, from lightning onset to the last faint echo, is the normal "
  "course of the emotion doing its job and then standing down."),
 "how_it_works": ("The time course follows the body's alarm economics. "
  "Onset is fast because shame is a social-threat alarm, and alarms that "
  "arrive late are useless - the sympathetic nervous system fires the "
  "submission display before conscious appraisal finishes. The peak is "
  "capped because full arousal is metabolically expensive; the system "
  "automatically down-regulates even if the threat appraisal has not "
  "changed. Fading is the parasympathetic rebound plus cognitive "
  "reappraisal: as attention returns to the world, the imagined audience "
  "shrinks back to actual size. The aftershock is memory consolidation at "
  "work - emotionally tagged memories are rehearsed and strengthened, "
  "which is why the replay feels vivid. Each replay is also a chance for "
  "the memory to be re-encoded with new information, which is the "
  "mechanism behind the folk wisdom that time heals: it does, provided "
  "the replays gradually include the wider context - that the audience "
  "moved on, that the standard was unrealistic, that one scene is not a "
  "biography."),
 "key_points": [
  "Onset is seconds-fast; the body reacts before the mind has finished appraising.",
  "The peak is the worst and the briefest - full alarm cannot be held indefinitely.",
  "Fading takes minutes to hours as attention flows back out to the world.",
  "Aftershocks are normal: vivid replays hours or days later, decaying with each echo.",
  "Replays in the same harsh words recharge the echo; wider context lets it fade."],
 "requirements": [
  "Walk the four phases in order with concrete fictional texture at each stage.",
  "Explain the mechanism behind the shape, not just the shape itself.",
  "Keep guidance general and safe; no clinical treatment language.",
  "No real person described; the example stays hypothetical."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people, no therapeutic promises."],
 "citations": [CIT_LAZARUS, CIT_GROSS],
 "sig_lens": ("The Signature lens charts shame as a storm with a known "
  "track: landfall, eyewall, dissipation, and the outer bands that return "
  "as weather. Sailors do not curse the storm track; they learn it, "
  "respect the eyewall, and know that outer bands are not a second "
  "hurricane. The master reads the barometer and waits for clear skies."),
},
{
 "key": "shame_low_vs_high",
 "name": "Shame at Low Intensity vs High Intensity: Two Snapshots",
 "group": "Foundations", "ladder_rank": 7, "ladder_tier": "foundations",
 "description": ("Low-intensity shame: you are at a dinner table and "
  "mispronounce a guest's name. Warmth touches your cheeks; you laugh, "
  "correct yourself, the table laughs with you, and within a minute you "
  "are asking for the bread. Your sense of self never wavered - the "
  "feeling was about the moment, corrected and closed. High-intensity "
  "shame: you are presenting work you are proud of, and a respected "
  "figure dismantles it in front of the room, ending with a remark about "
  "your judgment. The heat is not a blush but a flood; your vision "
  "narrows; you hear your own voice answering and it sounds like "
  "someone drowning. For the rest of the day you replay the remark; for "
  "weeks you avoid that room; the work itself now feels contaminated, "
  "not because it changed but because the exposure changed what it means "
  "to you. Same emotion, different universe. At low intensity shame is a "
  "tap on the shoulder; at high intensity it is a hand pressing your face "
  "into the floor. The difference is not the feeling's nature but its "
  "claim on the self: low shame says \"that was awkward,\" high shame "
  "says \"you are broken.\""),
 "how_it_works": ("The two snapshots differ on the three dials: "
  "identity-centrality, audience weight, and exposure permanence. In the "
  "dinner snapshot all three read low - the standard (pronouncing names "
  "right) is peripheral, the audience is friendly, the exposure evaporates "
  "with laughter. The system fires, corrects, and stands down. In the "
  "presentation snapshot all three read high - professional competence is "
  "core identity, the critic is high-status, and the public setting makes "
  "the exposure feel permanent and widely witnessed. When the dials align "
  "at the top, the appraisal system promotes the event from \"a bad "
  "moment\" to \"evidence about the self,\" and the emotion switches from "
  "its brief corrective mode into its sustained self-reorganization mode: "
  "avoidance, rumination, and a revised, smaller self-image. Recovery "
  "tracks the same dials in reverse: shrinking any one of them - a "
  "kinder audience, a less central standard, a contained exposure - "
  "drops the volume faster than willpower ever could."),
 "key_points": [
  "Low shame is a tap on the shoulder; high shame is a hand pressing down.",
  "Low shame stays about the moment; high shame is promoted to evidence about the self.",
  "The difference is set by three dials: identity-centrality, audience weight, exposure permanence.",
  "High shame reorganizes behavior: avoidance, rumination, a smaller self-image.",
  "Recovery comes from turning down any one dial, not from fighting the feeling head-on."],
 "requirements": [
  "Give both snapshots with vivid fictional detail and equal weight.",
  "Show the same machinery at two settings; do not present two different emotions.",
  "Keep all coping notes general and safe; no clinical prescriptions.",
  "Fictional characters only; never the reader, never a real person."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people, no therapeutic promises."],
 "citations": [CIT_TANGNEY, CIT_APA],
 "sig_lens": ("The Signature lens keeps two gauges on the wall: the tap "
  "and the flood. The tap is the instrument doing its job - log it and "
  "move on. The flood is the instrument overwhelmed - do not navigate by "
  "it, do not carve its readings into stone. Gauges are for reading, not "
  "for worship."),
},
{
 "key": "shame_guilt_blend",
 "name": "Shame Mixed With Guilt: The Most Common Partnership",
 "group": "Foundations", "ladder_rank": 8, "ladder_tier": "foundations",
 "description": ("Shame rarely travels alone, and its most frequent "
  "traveling companion is guilt. Picture a student who cheated on a test "
  "and was caught. Guilt speaks first and speaks about the act: \"I broke "
  "a rule, I should make it right\" - and it pushes toward confession, "
  "apology, repair. Shame speaks a half-second later and speaks about the "
  "self: \"I am a cheater, they all know what I am\" - and it pushes toward "
  "hiding, minimizing, disappearing. The blend feels like a knot: the urge "
  "to fix tangled with the urge to flee. Untangled, the two have opposite "
  "action tendencies - guilt approaches and repairs, shame withdraws and "
  "conceals - which is why the blend is so uncomfortable: the body is "
  "being told to move in two directions at once. The partnership is so "
  "common because most real wrongs implicate both the act and the actor. "
  "The practical wisdom of the blend is to let each half do its job: let "
  "guilt drive the repair - own it, fix what can be fixed - and let the "
  "shame half be heard without being obeyed, because hiding is the one "
  "response that guarantees the knot tightens."),
 "how_it_works": ("The blend forms because a single event is appraised "
  "twice, along two tracks. Track one evaluates the act against rules: "
  "wrong act, my responsibility, repair possible - that is guilt, an "
  "approach emotion with a clear exit (make amends and it resolves). Track "
  "two evaluates the self against identity standards: this act reveals a "
  "flawed self, now exposed - that is shame, a withdrawal emotion with no "
  "clear exit (the self cannot be un-exposed). The tracks run in parallel "
  "and their outputs collide in the action system: approach versus "
  "withdrawal. Which one wins the moment depends on attention - focus on "
  "the harmed party and the fixable damage, and guilt leads; focus on the "
  "watching eyes and the permanent stain, and shame leads. The blend can "
  "also curdle: when shame dominates, its hiding urge sabotages guilt's "
  "repair urge - the apology never happens because facing the harmed "
  "person means facing the exposure. That is why the standard advice for "
  "the blend is sequence, not suppression: repair first (guilt's job), "
  "then let the self-judgment fade with the evidence that repair "
  "happened (shame's release)."),
 "key_points": [
  "Shame and guilt co-fire because one event is appraised on two tracks: act and self.",
  "Guilt pushes toward approach and repair; shame pushes toward withdrawal and hiding.",
  "The blend feels like a knot because the body is told to move in two directions at once.",
  "Whichever track gets attention leads the moment: the harmed party or the watching eyes.",
  "Sequence works: let guilt drive repair first, then let shame fade on the evidence of repair."],
 "requirements": [
  "Keep the self-versus-act distinction as the organizing principle.",
  "Show the blend through one sustained fictional example.",
  "Explain the action-tendency collision, not just the co-occurrence.",
  "No real person labeled; guidance stays general and safe."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people, no therapeutic promises."],
 "citations": [CIT_TANGNEY, CIT_LAZARUS],
 "sig_lens": ("The Signature lens sees the blend as two instruments "
  "arguing: guilt the compass pointing at the damage to be repaired, "
  "shame the mirror showing the face of the repairer. The master follows "
  "the compass first - do the repair - and the mirror's reflection "
  "changes on its own, because the face in it is now the face of someone "
  "who made things right."),
},
{
 "key": "shame_day_vignette",
 "name": "A Day With Shame: An Ordinary-Day Vignette",
 "group": "Foundations", "ladder_rank": 9, "ladder_tier": "foundations",
 "description": ("Morning: Mara wakes already rehearsing. Yesterday her "
  "manager corrected her numbers in front of the team, gently, but the "
  "scene replays while she brushes her teeth - the pause, the glances, "
  "her own too-loud laugh. She chooses a plain outfit, nothing that draws "
  "eyes. Midday: in the meeting she knows an answer but does not raise "
  "her hand; the risk of being wrong in public outweighs the reward of "
  "being right. At lunch she eats at her desk, scrolling, because the "
  "break room means small talk and small talk means chances to be seen "
  "stumbling. Afternoon: an email arrives praising her analysis. She "
  "reads it three times, waiting to feel the lift - it does not come; "
  "the praise slides off like rain on wax, while yesterday's correction "
  "still burns underneath. Evening: a friend invites her out. She "
  "invents a headache. Alone, she replays the meeting once more, then "
  "catches herself and - for the first time all day - names what has "
  "been running her: not the correction, which was minor and fair, but "
  "the shame about the correction, which has been spending her whole "
  "day. Nothing in the vignette is dramatic. That is the point. Shame "
  "does its heaviest work not in the flood but in the quiet tax it levies "
  "on ordinary hours: the hand not raised, the room not entered, the "
  "praise not received."),
 "how_it_works": ("The vignette shows shame's three taxes across a day. "
  "The anticipation tax: behavior is pre-shaped by the imagined audience - "
  "outfit, seat, silence - before anything happens. The attention tax: "
  "working memory is occupied by the replay loop, leaving less for the "
  "actual task; this is why shamed people underperform in the very "
  "situations they fear, creating the failures they dread. The reward "
  "tax: positive information is discounted - praise cannot land because "
  "the self-model has been temporarily rewritten as unworthy, and "
  "incongruent data is rejected. Together the taxes form a self-sealing "
  "system: avoidance prevents disconfirming experiences, the replay "
  "rehearses the verdict, and the discounted praise removes the "
  "counter-evidence. The crack in the system - the moment that matters - "
  "is metacognition: Mara naming the operator. Shame runs best "
  "unnamed, as background weather. Named as weather, it becomes "
  "something that can be waited out rather than obeyed."),
 "key_points": [
  "Shame taxes the day three ways: anticipation, attention, and discounted reward.",
  "Avoidance pre-shapes behavior before anything happens - the hand never rises.",
  "The replay loop eats working memory, causing the very failures that are feared.",
  "Praise slides off because the temporary self-model rejects incongruent data.",
  "Naming the operator - \"this is shame running me\" - is the crack in the sealed system."],
 "requirements": [
  "Follow one fictional character through a full ordinary day.",
  "Show the quiet taxes, not just a dramatic peak.",
  "Explain the self-sealing mechanism and the metacognitive crack.",
  "Fictional character only; the reader is never placed in the scene."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people, no therapeutic promises."],
 "citations": [CIT_SCHEFF, CIT_GROSS],
 "sig_lens": ("The Signature lens reads Mara's day as a ledger: every "
  "unraised hand, uneaten lunch, and declined invitation entered as a "
  "cost paid to an audience that had already forgotten the scene. The "
  "master audits the ledger. Most of shame's daily spending, examined in "
  "daylight, turns out to be protection money paid to no one."),
},
]

ENTRIES += [
{
 "key": "shame_body_signals",
 "name": "The Body in Shame: Heart, Breath, Muscles, Stomach, Skin, Energy",
 "group": "Compounded", "ladder_rank": 10, "ladder_tier": "compounded",
 "description": ("The body keeps its own ledger of shame, written in "
  "physiology. The skin goes first and most visibly: blood rushes to the "
  "face, neck, and ears - the blush - driven by the same vessels that "
  "flush in heat, which is why the sensation is warmth and why it feels "
  "so betraying: the body is advertising the very feeling you want to "
  "hide. The heart hammers, then seems to hesitate; breathing goes "
  "shallow and quick, as if the lungs do not want to be noticed either. "
  "Muscles do the opposite of anger's clenching - they slacken and fold: "
  "shoulders roll forward, chest caves, the whole frame tries to occupy "
  "less space. The stomach knots or drops; appetite vanishes mid-bite "
  "because digestion is a low-priority system during a social alarm. "
  "Hands fidget, touch the face, cover the mouth - improvised curtains. "
  "Energy drains rather than surges: shame is a de-activating emotion, "
  "and its aftermath feels like heaviness, a body made of wet sand. "
  "People describe wanting the floor to open; the physiology agrees - "
  "every signal is tuned toward becoming smaller, quieter, and gone."),
 "how_it_works": ("The pattern is the mammalian submission and "
  "appeasement display, conserved across social species. When the social "
  "threat system fires, the sympathetic branch raises heart rate and "
  "shunts blood - including to the face, an oddity Darwin puzzled over, "
  "since blushing serves no fight-or-flight purpose; its best explanation "
  "is signaling: the involuntary display honestly advertises \"I know I "
  "transgressed,\" which appeases the group more reliably than any "
  "performed apology. Simultaneously, postural muscles release their "
  "upright tone - the flexor-dominant collapse that reads as the slump. "
  "Shallow breathing follows from the curled posture mechanically "
  "compressing the diaphragm, which then feeds back: restricted breath "
  "sustains the alarm state, which is why slow deliberate breathing can "
  "begin to unwind it. The energy drain is the parasympathetic rebound "
  "overshooting - the freeze-flop end of the defense cascade, the body "
  "choosing immobility over action. None of this is chosen; it is "
  "reflex. Knowing it is reflex matters: the blush is not weakness of "
  "character but wiring, and wiring can be worked with rather than "
  "obeyed."),
 "key_points": [
  "The blush is the flagship signal: involuntary, visible, and honest - the body advertising what the mind wants hidden.",
  "Posture collapses by reflex: shoulders forward, chest caved, frame minimized.",
  "Breathing shallows as the curled posture compresses the diaphragm, sustaining the alarm.",
  "Shame de-activates: the aftermath is heaviness and drained energy, not agitation.",
  "The whole pattern is the ancient submission display - appeasement wiring, not character weakness."],
 "requirements": [
  "Cover heart, breath, muscles, stomach, skin, and energy systematically.",
  "Frame the pattern as conserved reflex, never as personal failing.",
  "Keep physiology descriptive; no medical claims or health advice.",
  "No real person described; examples stay fictional and general."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people, no therapeutic promises."],
 "citations": [CIT_DARWIN, CIT_IZARD],
 "sig_lens": ("The Signature lens reads the body as the honest clerk: "
  "while the mind spins stories, the clerk keeps the true ledger - heat "
  "in the face, weight in the limbs. The master does not argue with the "
  "clerk or obey him; he reads the entries, thanks the clerk for the "
  "report, and makes his own decisions standing upright."),
},
{
 "key": "shame_posture_movement",
 "name": "The Posture of Shame: How the Body Carries It",
 "group": "Compounded", "ladder_rank": 11, "ladder_tier": "compounded",
 "description": ("You can read shame from across a room by the geometry of "
  "the body. The head tilts down and often turns slightly away; the chin "
  "tucks as if to protect the throat. The shoulders roll forward and "
  "inward, the chest narrows, the spine rounds - the vertical line of the "
  "person shortens by centimeters, as though trying to resign from taking "
  "up space. Arms cross or hug the torso; hands find the face, the neck, "
  "the lap - anywhere but open at the sides. Movement shrinks with it: "
  "steps get shorter and quieter, gestures contract toward the body's "
  "center, and stillness replaces fidgeting when the shame is deepest - "
  "the freeze inside the slump. In motion, the shamed person angles away, "
  "drifts toward walls and corners, chooses the seat with the fewest "
  "sightlines. It is the photographic negative of pride's posture - chin "
  "up, chest open, movements expansive - which is why the two are so "
  "instantly legible even to children. The posture is not performed; ask "
  "someone to describe their shame and their body will often start "
  "demonstrating before the words arrive."),
 "how_it_works": ("Posture in shame is controlled by the flexor muscles "
  "winning over the extensors - the curl program. In social mammals, "
  "making the body small and protecting the front (throat, chest, belly) "
  "signals non-threat to dominants and reduces the chance of attack; "
  "humans kept the program and aimed it at social judgment. The head-down "
  "component specifically breaks eye contact, which in primate "
  "communication de-escalates confrontation - looking away says \"I "
  "concede the encounter.\" Movement toward edges and exits is the "
  "spatial half of the same program: reduce exposure by reducing "
  "visibility. The posture also feeds back into the feeling - experiments "
  "on embodied emotion show that adopting an expansive posture lightens "
  "self-evaluation while a collapsed posture deepens it, because the "
  "brain reads the body's attitude as data about the situation. This "
  "two-way street is why posture is both symptom and lever: it reveals "
  "the feeling, and deliberately - gently - opening it can begin to "
  "loosen the feeling's grip."),
 "key_points": [
  "The geometry: head down and averted, shoulders in, chest narrowed, spine rounded.",
  "Hands guard the face and torso; movement contracts toward the body's center.",
  "The shamed person drifts to edges, corners, and low-visibility seats.",
  "It is pride's photographic negative - chin up versus chin tucked, open versus closed.",
  "Posture is a two-way street: it reveals the feeling and can gently loosen it."],
 "requirements": [
  "Describe the full postural signature: head, shoulders, chest, arms, hands, gait, spatial choice.",
  "Contrast with pride's posture to make the pattern legible.",
  "Keep it observational and descriptive; no prescriptions framed as treatment.",
  "No real person described; the figure in the scene is fictional."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people, no therapeutic promises."],
 "citations": [CIT_DARWIN, CIT_EKMAN],
 "sig_lens": ("The Signature lens sees posture as the body's handwriting: "
  "pride writes in tall capitals, shame in a cramped whisper. The master "
  "learns to read his own handwriting without shame about the handwriting "
  "- and knows that straightening the page, slowly and deliberately, can "
  "help the next sentence come out clearer."),
},
{
 "key": "shame_sleep_appetite_energy",
 "name": "Shame, Sleep, Appetite, and Energy",
 "group": "Compounded", "ladder_rank": 12, "ladder_tier": "compounded",
 "description": ("Shame reaches past the moment and into the body's "
  "maintenance systems. Appetite is usually the first casualty: the "
  "knotted stomach and the social alarm together switch off hunger, and "
  "meals get skipped or pushed around the plate - eating is a vulnerable, "
  "visible act, and the shamed body wants no more visibility. Sleep "
  "suffers next, but not at onset - at the replay hour. The day's noise "
  "fades, the audience is gone, and the inner re-run begins: the scene "
  "replays on the ceiling in the dark, each loop slightly sharper, and "
  "sleep arrives late or not at all. When sleep does come it is often "
  "thin, and mornings carry the residue - waking already tired, already "
  "dreading the rooms where the exposure might continue. Energy follows "
  "the same curve as the emotion's de-activating nature: not the wired "
  "tired of anxiety but a leaden heaviness, tasks feeling twice their "
  "weight, the day's simple errands queued and re-queued. None of this is "
  "a separate condition; it is shame's weather system moving through the "
  "body's ordinary machinery, and it lifts as the emotion itself lifts."),
 "how_it_works": ("The mechanism is resource reallocation under social "
  "threat. Digestion is parasympathetic luxury - the alarm state diverts "
  "blood and attention away from the gut, hence the knot and the vanished "
  "appetite. Sleep disruption comes from the replay loop occupying the "
  "pre-sleep window: rumination is cognitive arousal, and arousal is the "
  "enemy of sleep onset; the emotionally tagged memory also gets priority "
  "in consolidation, which is why the scene feels vivid at 2 a.m. The "
  "energy drain has two sources: the physiological cost of sustained "
  "arousal followed by rebound, and the attentional cost of the loop "
  "itself - working memory spent on replay is working memory not spent on "
  "living, so everything feels effortful. The pattern is self-limiting "
  "when the shame resolves: appetite returns with the first genuinely "
  "relaxed meal, sleep with the first night the loop does not run, energy "
  "with the first day attention is free. The body is not broken; it is "
  "budgeting for a threat, and it re-budgets when the threat passes."),
 "key_points": [
  "Appetite goes first: the alarm state switches off hunger and makes eating feel exposed.",
  "Sleep suffers at the replay hour - the scene re-runs on the ceiling in the dark.",
  "The fatigue is leaden heaviness, not wired tiredness: shame de-activates.",
  "All three are resource reallocation under social threat, not separate conditions.",
  "They lift as the emotion lifts: appetite, sleep, and energy re-budget when the threat passes."],
 "requirements": [
  "Cover sleep, appetite, and energy as shame's downstream effects.",
  "Explain mechanisms plainly; no medical advice or health claims.",
  "Normalize the pattern as the emotion's weather, not a disorder.",
  "Fictional and general throughout; no real person described."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people, no therapeutic promises."],
 "citations": [CIT_LAZARUS, CIT_GROSS],
 "sig_lens": ("The Signature lens treats the body's maintenance as a "
  "garrison under siege discipline: rations cut, watches doubled, rest "
  "short. The master recognizes siege discipline for what it is - a "
  "temporary posture, not the new constitution. When the siege lifts, "
  "the garrison stands down: eat, sleep, move, and let the quartermaster "
  "do his job."),
},
{
 "key": "shame_body_differences",
 "name": "How Shame Feels Different in Different Bodies",
 "group": "Compounded", "ladder_rank": 13, "ladder_tier": "compounded",
 "description": ("No two bodies do shame identically, and the differences "
  "matter - they are why one person's account of the feeling can sound "
  "foreign to another. Some people blush crimson at the slightest "
  "exposure; others never visibly flush and feel the heat only as an "
  "internal tide. Some go silent and still; others get loud and fast, "
  "talking over the feeling in a rush of nervous speech that looks like "
  "confidence from the outside. Some feel shame as heat - face, neck, "
  "ears burning - while others feel it as cold: a hollow chill in the "
  "stomach, hands going icy. Stomach-first people get the nausea and the "
  "knot; chest-first people get the tight band and the shallow breath; "
  "throat-first people lose their voice mid-sentence. Age shifts the "
  "pattern too: children show it raw and whole-body, teenagers feel it "
  "most intensely as peer judgment peaks, adults often report it "
  "dampened but more entangled with identity. Temperament sets the "
  "baseline - the easily embarrassed carry a hair-trigger, the thick-"
  "skinned need a heavier blow to fire the same circuit. None of these "
  "variations is the \"right\" way to feel shame; they are the same "
  "ancient program running on different hardware."),
 "how_it_works": ("The variation comes from three sources. First, "
  "autonomic wiring differs: vascular reactivity determines blushing "
  "visibility, vagal tone shapes the heart and gut response, and baseline "
  "arousal sets how fast the alarm trips. Second, learned display rules "
  "layer on top of the reflex - families and cultures teach, from "
  "childhood, which expressions of shame are permitted and which must be "
  "masked, so two people with identical physiology can look opposite on "
  "the outside. Third, the cognitive appraisal differs: what counts as "
  "exposure-worthy depends on personal history, so the same event fires "
  "a full alarm in one nervous system and barely registers in another. "
  "The practical consequence is humility in reading others: the absence "
  "of a blush is not the absence of shame, and loud fast talking can be "
  "the mask of the very feeling it seems to contradict. The emotion is "
  "universal in structure - standard, exposure, audience - and individual "
  "in performance."),
 "key_points": [
  "Blushing varies: some flame visibly, others feel only an internal tide of heat.",
  "Some go silent and still; others talk fast and loud over the feeling.",
  "The feeling's address differs: face-heat people, stomach-knot people, throat-close people.",
  "Age and temperament shift the pattern; teenagers and the easily embarrassed feel it sharpest.",
  "Never read absence of visible signs as absence of the feeling."],
 "requirements": [
  "Survey the main axes of variation: vascular, vocal, thermal, developmental, temperamental.",
  "Emphasize that variation is normal; no single correct performance of shame.",
  "Warn against misreading others based on one's own pattern.",
  "All examples fictional and general; no real person described."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people, no therapeutic promises."],
 "citations": [CIT_IZARD, CIT_DARWIN],
 "sig_lens": ("The Signature lens keeps a gallery of instruments: no two "
  "gauges are calibrated identically, and a wise reader learns each "
  "instrument's personal scale. The master studies his own gauge until "
  "he can read it in the dark - and extends the same courtesy to every "
  "other gauge in the room, which will never read exactly like his."),
},
{
 "key": "shame_face",
 "name": "The Face of Shame: Eyes, Brows, Mouth, and Micro-Signs",
 "group": "Compounded", "ladder_rank": 14, "ladder_tier": "compounded",
 "description": ("The shamed face is one of the most recognizable in the "
  "human repertoire, and its grammar is subtraction: it removes the face "
  "from view. The eyes lead - gaze drops, slides sideways, or fixes on "
  "some middle distance; sustained eye contact becomes physically "
  "difficult, as if the other person's eyes were too bright to look at. "
  "The brows draw slightly together and up at the inner corners in the "
  "grief-adjacent configuration, or simply lower with the whole head. The "
  "mouth compresses: lips press together, press inward, or pull down at "
  "the corners; the full shamed mouth is a thin flattened line, sometimes "
  "trembling at the edges. The head itself is part of the face's message - "
  "tilted down, turned partially away, occasionally with a hand rising to "
  "cover part of it: the hand-to-face, the hair pulled forward as a "
  "curtain, the chin tucked to the chest. Micro-signs fill the gaps: the "
  "quick tongue dart over dry lips, the swallow that is too audible, the "
  "blink rate climbing, the attempted smile that reaches the mouth but "
  "never the eyes. And over it all, in the blush-prone, the spreading red "
  "that the face cannot hide because the face is the billboard."),
 "how_it_works": ("Each element serves the appeasement program. Gaze "
  "aversion de-escalates: in primate signaling, breaking eye contact "
  "concedes the encounter and averts the dominant's continued attention. "
  "The head-down turn reduces the face's visibility and its apparent size, "
  "the two variables that draw social attention. Lip compression is the "
  "suppression of speech made visible - the mouth literally sealing the "
  "words that the inner audience has already judged. The hand-to-face is "
  "a barrier gesture, the body's improvised attempt to do what it cannot: "
  "leave the scene while remaining in it. The blush is the honest signal "
  "underneath the attempted concealment - involuntary, unfakeable, and "
  "therefore trusted by observers as the true report, which is why people "
  "find blushers more sincere. Together the elements form a redundant "
  "message, broadcast on multiple channels at once: I concede, I submit, "
  "I am no threat, please look away. Redundancy is the point - the "
  "signal must get through even if the shamed person tries to suppress "
  "parts of it."),
 "key_points": [
  "The grammar is subtraction: the face removes itself from view.",
  "Eyes drop or slide away; sustained contact becomes physically difficult.",
  "The mouth compresses to a thin line - the suppression of speech made visible.",
  "Barrier gestures improvise concealment: hand to face, hair as curtain, chin tucked.",
  "The blush is the unfakeable honest signal underneath the attempted cover."],
 "requirements": [
  "Walk eyes, brows, mouth, head, hands, and micro-signs systematically.",
  "Explain the appeasement function behind each element.",
  "Keep it observational; this is a field guide, not a diagnostic manual.",
  "No real faces described; no real person labeled."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people, no therapeutic promises."],
 "citations": [CIT_EKMAN, CIT_DARWIN],
 "sig_lens": ("The Signature lens studies the shamed face as a flag at "
  "half-mast: the colors lowered, the pole bent, the whole nation of the "
  "self signaling distress to friendly ships. The master learns to read "
  "the flag - in himself and others - not as surrender but as a signal "
  "requiring an answer: what standard was breached, and what repair is "
  "owed?"),
},
{
 "key": "shame_face_intensity",
 "name": "The Shame Face Across Intensities",
 "group": "Compounded", "ladder_rank": 15, "ladder_tier": "compounded",
 "description": ("The shamed face is not one mask but a dimmer switch. At "
  "low intensity it is barely a face at all - a quick downward flick of "
  "the eyes, a half-second lip press, a small exhale through the nose "
  "that might be a laugh. Most observers miss it; the feeling passes "
  "before the features have finished arranging themselves. At moderate "
  "intensity the full grammar assembles: gaze down and away, head tilted, "
  "mouth compressed, the blush rising, the hand drifting toward the face. "
  "This is the face people picture when they picture shame, and it is "
  "legible across a room. At high intensity the face begins to "
  "disassemble: the features lose their coordination - eyes darting "
  "between floor and exit, mouth working without words, the blush now "
  "mottled and patchy, sometimes tears arriving uninvited at the "
  "corners. The highest intensities add the freeze: the face goes slack "
  "and masklike, not from calm but from overload, the system protecting "
  "itself by going blank. Reading the dimmer matters because the response "
  "should match the setting: the flick wants a light touch or nothing at "
  "all, the assembled face wants space and normalcy, the disassembled "
  "face wants the pressure removed, not discussed."),
 "how_it_works": ("Intensity scales the face along two axes: recruitment "
  "and coordination. Recruitment is how many muscle groups join the "
  "display - at low intensity only the fastest, cheapest signals fire "
  "(the eye flick, the lip press); as intensity rises, slower and more "
  "expensive components are recruited (head turn, hand barrier, full "
  "blush). Coordination is how well the components synchronize - moderate "
  "shame produces the classic coherent display because the system is "
  "aroused but organized; at the highest intensities arousal outruns "
  "organization and the display fragments into darting, working, "
  "mottled incoherence, then finally the protective blank of overload. "
  "The dimmer also explains misreading: a low-intensity flick is often "
  "invisible, so observers conclude \"no shame felt\" and press harder; "
  "a high-intensity blank is misread as coldness or indifference, when it "
  "is the system at maximum load. Calibrating to the dimmer - seeing the "
  "flick, respecting the blank - is the core skill of reading this face."),
 "key_points": [
  "Low: a flicker - eye dip, lip press, gone before the features arrange themselves.",
  "Moderate: the full classic grammar assembles and is legible across a room.",
  "High: the face disassembles - darting eyes, working mouth, mottled blush, uninvited tears.",
  "Overload: the protective blank, misread as coldness, is the system at maximum load.",
  "Match the response to the setting: light touch, space, or removed pressure."],
 "requirements": [
  "Present the dimmer switch across four settings with distinct texture at each.",
  "Explain recruitment and coordination as the scaling mechanism.",
  "Include the two classic misreadings: the invisible flick and the misread blank.",
  "No real faces; all figures fictional."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people, no therapeutic promises."],
 "citations": [CIT_EKMAN, CIT_IZARD],
 "sig_lens": ("The Signature lens keeps the dimmer on the workbench: low "
  "is a pilot light, moderate the working lamp, high the overloaded "
  "circuit, blank the breaker tripped. The master does not curse the "
  "dark when the breaker trips - he reduces the load, waits, and resets "
  "the circuit with patience."),
},
{
 "key": "shame_hiding_faking",
 "name": "Hiding and Faking the Shame Expression - and What Leaks Through",
 "group": "Compounded", "ladder_rank": 16, "ladder_tier": "compounded",
 "description": ("Shame is the emotion people most want to hide, and the "
  "hardest to hide well - a cruel pairing. The standard cover kit: the "
  "frozen neutral face, held a fraction too still; the over-bright smile "
  "that arrives half a second late and never reaches the eyes; the sudden "
  "busyness - checking a phone, shuffling papers - that manufactures an "
  "excuse to look down; the laugh that comes out pitched half an octave "
  "high. Faking the absence of shame usually means performing its "
  "opposite: the chin lifts a degree too far, the voice gets a notch "
  "louder, the casualness is rehearsed one degree past natural. And "
  "always, the leaks. The blush cannot be suppressed by will - the "
  "vessels do not take orders. The gaze still darts down in the first "
  "quarter-second before the cover is arranged. The hands still find the "
  "face. The swallow still lands too loud. The stillness itself becomes a "
  "tell: a face held perfectly motionless during an exposure moment is "
  "as informative as the shamed face it replaces, because neutral faces "
  "are never that still in easy moments. Experienced observers do not "
  "watch for the mask; they watch for the effort of holding it."),
 "how_it_works": ("Concealment fails asymmetrically because the shame "
  "display splits into voluntary and involuntary channels. The voluntary "
  "channels - head angle, mouth shape, hand placement - can be overridden "
  "with effort, which is why the cover kit exists. The involuntary "
  "channels - vasodilation (the blush), blink rate, vocal pitch under "
  "stress, the micro-timing of the first gaze break - run on autonomic "
  "wiring and cannot be willed off. Worse, the effort of suppression is "
  "itself visible: holding muscles against their reflex pattern produces "
  "the characteristic over-stillness and the timing lags (the late "
  "smile, the high laugh) that mark a performance. This is the ironic "
  "process at work - monitoring \"am I showing it?\" keeps attention on "
  "the feeling, which sustains the arousal, which feeds the leaks. The "
  "practical upshot is counterintuitive: the most effective concealment "
  "is not suppression but redirection - giving the body something true "
  "to do (slow breath, feet on the floor, attention on the other person) "
  "rather than commanding it to show nothing, because a body with a job "
  "leaks less than a body under orders."),
 "key_points": [
  "The cover kit: frozen neutral, late bright smile, manufactured busyness, pitched-high laugh.",
  "Faking its absence means performing its opposite - chin too high, voice too loud.",
  "The leaks are involuntary: blush, first gaze break, blink rate, vocal pitch.",
  "Over-stillness is itself a tell - easy faces are never that motionless.",
  "Suppression monitoring feeds the feeling; redirection (a true task for the body) leaks less."],
 "requirements": [
  "Catalog the cover strategies and the specific leaks for each.",
  "Explain the voluntary/involuntary channel split as the mechanism.",
  "Keep it descriptive craft knowledge, not a manipulation manual.",
  "No real person described as hiding or faking anything."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people, no therapeutic promises."],
 "citations": [CIT_EKMAN, CIT_DARWIN],
 "sig_lens": ("The Signature lens notes the paradox of the mask: the "
  "harder the hand presses the mask to the face, the more the fingers "
  "tremble. The master does not perfect the mask; he retires it. A face "
  "allowed to show a clean, brief shame - and then lift - is more "
  "dignified than any performance of unbothered, because audiences trust "
  "what is honest."),
},
{
 "key": "shame_expression_gallery",
 "name": "Drawing Shame: Expression Notes for Artists and Actors",
 "group": "Compounded", "ladder_rank": 17, "ladder_tier": "compounded",
 "description": ("For the artist's sketchbook and the actor's mirror: "
  "shame is drawn from the top down, because the head leads the whole "
  "composition. Start with the skull tilted forward fifteen to twenty "
  "degrees and rotated a quarter-turn away from the viewer - the face "
  "three-quarter hidden, not fully profile. The eyeline is the critical "
  "stroke: lids lowered, pupils aimed at a point on the floor two meters "
  "ahead, never at the viewer. Brows sit low and draw faintly together; "
  "avoid the deep furrow of anger - shame's brow is heavy, not fierce. "
  "The mouth is a study in compression: lips pressed to a thin line, "
  "corners pulled down a millimeter, the whole mouth slightly "
  "asymmetric, as if holding back different words on each side. Add the "
  "blush as a warm wash across cheekbones, nose bridge, and ears - "
  "visible, but not the clown-red of exertion; shame's red is a "
  "watercolor, not a poster paint. Shoulders roll forward so the collarbones "
  "angle down; one hand rises - fingers to lips, or palm to cheek, or "
  "both hands cradling a cup like a small shield. For the actor: the "
  "voice is the second face - drop volume by a third, let sentences "
  "trail unfinished, and allow the swallow before the hard line. The "
  "classic error is playing shame as sadness: sadness weeps outward, "
  "seeking comfort; shame folds inward, refusing it. Play the refusal, "
  "not the tears."),
 "how_it_works": ("The notes work because they encode the appeasement "
  "program in drawable, playable units. Each instruction maps to a "
  "functional element: head tilt and rotation reduce facial visibility "
  "and apparent size; the lowered eyeline breaks the viewer's gaze line, "
  "which reads as de-escalation; lip compression visualizes suppressed "
  "speech; the hand barrier literalizes the wish to block the audience's "
  "view; the forward shoulder roll collapses the chest's broad, "
  "attention-drawing plane. The blush instruction matters most for "
  "honesty of effect - audiences unconsciously treat the involuntary "
  "signal as the truth-teller, so a shame portrayal without any "
  "involuntary channel reads as performed rather than felt. The actor's "
  "vocal notes follow the same logic: reduced volume and unfinished "
  "sentences are the audible form of making oneself smaller and less "
  "exposed. The sadness distinction is functional too - sadness is an "
  "attachment emotion that solicits approach, while shame is a "
  "status emotion that refuses it; confusing them breaks the scene's "
  "truth."),
 "key_points": [
  "Compose top-down: the head's tilt and quarter-turn away lead everything.",
  "The eyeline is the critical stroke - lids low, pupils on the floor, never at the viewer.",
  "Mouth as compression: thin pressed line, corners down a millimeter, slightly asymmetric.",
  "Blush as watercolor wash, not poster paint - the involuntary truth-teller.",
  "Play the refusal, not the tears: shame folds inward where sadness reaches outward."],
 "requirements": [
  "Write as practical notes an artist or actor could directly use.",
  "Cover face, head, shoulders, hands, blush, and voice.",
  "Include the classic error (shame played as sadness) and its correction.",
  "No real person depicted or described."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people, no therapeutic promises."],
 "citations": [CIT_DARWIN, CIT_EKMAN],
 "sig_lens": ("The Signature lens hands the artist a truth about the "
  "craft: shame is the hardest emotion to perform honestly because its "
  "whole nature is concealment - you are staging the act of unstaging. "
  "The master's note in the margin: do not perform the hiding; perform "
  "the thing being hidden from. Play the audience's eyes, and the face "
  "will follow."),
},
]

ENTRIES += [
{
 "key": "shame_classic_triggers",
 "name": "The Classic Triggers of Shame",
 "group": "Compounded", "ladder_rank": 18, "ladder_tier": "compounded",
 "description": ("Shame has a classic repertoire of triggers - the "
  "situations, words, and events that set it off in almost everyone. "
  "Public failure leads the list: the mistake witnessed, the stumble on "
  "stage, the wrong answer in the meeting, the project collapsing where "
  "others can see the rubble. Exposure of the hidden runs second: the "
  "private message read aloud, the secret told, the flaw pointed out "
  "that you thought was safely concealed - shame's deepest terror is not "
  "the flaw but the unveiling. Criticism and correction in front of "
  "others comes third, especially from high-status figures; the content "
  "can be fair and still the publicity stings more than the point. "
  "Rejection and exclusion trigger it fourth: being picked last, left "
  "out of the invitation, unfollowed, unchosen - the social bond's "
  "threat made concrete. Bodily and appearance exposure is fifth: the "
  "wardrobe failure, the unflattering photo circulated, the body judged "
  "in the open. And sixth, the moral tripwire: being caught in a lie, "
  "in cheating, in cruelty - the moment the private self and the "
  "presented self are forced into the same frame. Words that trigger it "
  "share a shape: they announce that the audience has seen behind the "
  "curtain - \"everyone saw,\" \"we all know,\" \"how could you.\""),
 "how_it_works": ("Every classic trigger runs the same three-part "
  "circuit: standard, exposure, audience. Public failure supplies all "
  "three at once - the standard of competence, the visible miss, the "
  "witnesses. Hidden-exposure triggers are potent because the standard "
  "was being protected by secrecy; the unveiling converts a managed flaw "
  "into an unmanaged one, and the loss of control amplifies the alarm. "
  "Public criticism works even when the criticism is accurate because "
  "the audience component dominates: the same correction delivered "
  "privately fires mainly guilt (about the act), while delivered "
  "publicly it fires shame (about the self under eyes). Rejection "
  "triggers fire the deepest layer - the belonging system - because "
  "shame evolved as the emotion of threatened social bonds; exclusion "
  "is the bond actually breaking. The trigger words work by inflating "
  "the audience dial: \"everyone saw\" may be factually false - three "
  "people saw - but the appraisal system rounds the audience up to "
  "infinity, which is why the feeling so often exceeds the facts. "
  "Knowing the circuit lets you audit any trigger: which part is real, "
  "which part is the rounding-up."),
 "key_points": [
  "The classic six: public failure, hidden exposure, public criticism, rejection, bodily exposure, moral tripwire.",
  "Every trigger runs the circuit: standard, exposure, audience.",
  "Public criticism stings beyond its content because the audience dominates the appraisal.",
  "Trigger words inflate the audience: \"everyone saw\" rounds three witnesses up to infinity.",
  "Audit any trigger by asking which part of the circuit is real and which is rounding-up."],
 "requirements": [
  "Catalog the trigger families with concrete fictional examples for each.",
  "Show the common circuit beneath the variety.",
  "Include the trigger-word pattern and the audience inflation effect.",
  "No real person described as triggered; no shaming content."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people, no therapeutic promises."],
 "citations": [CIT_SCHEFF, CIT_LAZARUS],
 "sig_lens": ("The Signature lens files the triggers as the enemy's "
  "order of battle - not to fear the list but to know the terrain. The "
  "master studies where ambushes happen: open stages, unveiled secrets, "
  "public corrections, closed doors. Forewarned is forearmed, and a "
  "trigger mapped is a trigger half-disarmed."),
},
{
 "key": "shame_personal_triggers",
 "name": "Personal Shame Triggers: Memories, Anniversaries, Private Associations",
 "group": "Compounded", "ladder_rank": 19, "ladder_tier": "compounded",
 "description": ("Beyond the universal triggers lies a private minefield, "
  "different for every person: the triggers no one else would predict. "
  "A song from the year of a humiliation can drop the stomach through "
  "the floor in a grocery store. A date on the calendar - the "
  "anniversary of a public failure, a rejection, a loss - arrives with "
  "dread attached to nothing happening at all. A smell, a classroom's "
  "chalk-dust air, the particular blue of a uniform, can reassemble the "
  "whole feeling from a single sensory thread. Family phrases do special "
  "damage: the exact words of a parent's disappointment, stored verbatim "
  "for decades, replayed in the parent's voice at full fidelity. Certain "
  "rooms, roles, and rituals carry residue - the witness stand of a "
  "childhood dinner table where report cards were read aloud, the "
  "stretch of road where the news arrived. These triggers are not "
  "rational; they are associative. The nervous system filed the original "
  "scene under \"danger,\" and anything resembling the file folder "
  "reopens it. Outsiders cannot see the minefield, which is why personal "
  "triggers so often look like overreactions - the reaction is not to "
  "the present moment but to the archive it opened."),
 "how_it_works": ("Personal triggers are classical conditioning applied "
  "to the social-threat system. During the original shaming scene, the "
  "brain's threat circuitry binds the intense affect to the neutral "
  "context - the song, the smell, the date, the phrase - in a single "
  "trial, because single-trial learning is the threat system's specialty. "
  "Later, the conditioned cue alone reactivates the affect before "
  "conscious memory catches up, which is why the feeling arrives "
  "\"about nothing\" - the body remembers the file before the mind "
  "reads the label. Anniversaries work through temporal conditioning: "
  "the calendar itself becomes the cue, and anticipatory dread builds "
  "for days beforehand. The residue in rooms and roles is context "
  "renewal - the same setting re-primes the same appraisal. Extinction "
  "is possible and follows the standard rule: the cue must be "
  "encountered repeatedly without the original consequence - the song "
  "heard in safe company, the date passing uneventfully - until the "
  "nervous system files an update. Avoidance prevents exactly this "
  "update, which is why the minefield persists for years in people who "
  "steer around every buried charge."),
 "key_points": [
  "Personal triggers are associative, not rational: songs, smells, dates, phrases, rooms.",
  "They form by single-trial conditioning - the threat system learns the file folder in one pass.",
  "The feeling arrives before the memory: the body reads the label before the mind does.",
  "They look like overreactions because outsiders cannot see the archive that opened.",
  "Avoidance preserves them; safe re-encounter without consequence files the update."],
 "requirements": [
  "Give the gallery of personal trigger types with fictional examples.",
  "Explain the conditioning mechanism in plain language.",
  "Normalize the \"about nothing\" arrival of the feeling.",
  "No real person described; no real memories referenced."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people, no therapeutic promises."],
 "citations": [CIT_LAZARUS, CIT_NATHANSON],
 "sig_lens": ("The Signature lens maps the minefield with the care of a "
  "surveyor, not the fear of a trespasser: every charge marked, dated, "
  "and traced to its original laying. The master walks the field "
  "deliberately, in daylight, on ground he has chosen - and each safe "
  "crossing redraws the map with fewer red marks."),
},
{
 "key": "shame_surprise_triggers",
 "name": "Surprise Triggers: The Odd, Unexpected Ones",
 "group": "Compounded", "ladder_rank": 20, "ladder_tier": "compounded",
 "description": ("Some shame arrives from directions no one guards. "
  "Being praised can trigger it - the compliment in front of others "
  "turns every eye toward you, and the spotlight itself, not the words, "
  "fires the alarm; the praised person blushes, deflects, changes the "
  "subject. Being helped publicly can do it: the offered seat, the "
  "carried bag, the explained joke all whisper \"you cannot manage,\" "
  "and the kindness lands as exposure of inadequacy. Success can "
  "trigger it - the promotion announced at the gathering, the award "
  "with your name called - because elevation is also visibility, and "
  "visibility is shame's native habitat. Intimacy triggers it: being "
  "truly seen, even lovingly, can feel like the curtain pulled back "
  "too far. Laughter nearby with an unknown cause - the table across "
  "the room erupting - gets claimed by the shame system as evidence: "
  "\"they are laughing at me.\" Even rest can trigger it in the "
  "over-driven: the quiet Sunday with nothing to prove feels like "
  "exposure of the self without its armor of busyness. The surprise "
  "triggers share one trait: they catch the standard-exposure-audience "
  "circuit firing on inputs the conscious mind had filed as safe, which "
  "is why they confuse people most."),
 "how_it_works": ("Surprise triggers work because the shame circuit is "
  "dumb in a specific way: it monitors exposure and audience, not "
  "valence. Praise, help, success, and intimacy all increase social "
  "visibility - more eyes, more evaluation - and the circuit reads "
  "rising visibility as rising risk regardless of whether the evaluation "
  "is positive. The praised person's alarm is not about the compliment's "
  "content but about the sudden audience inflation: ten faces turned at "
  "once is ten chances to be found wanting. The laughter-across-the-room "
  "effect is the self-referential bias of the threat system: under "
  "arousal, ambiguous social data is resolved in the threatening "
  "direction, because false alarms are cheaper than missed detections. "
  "The rest-trigger is the armor theory: busyness functions as a "
  "managed presentation of the self, and stillness removes the "
  "management, leaving the raw self under the inner audience's gaze. "
  "Understanding the pattern converts confusion into recognition: the "
  "circuit is not malfunctioning at these moments, it is doing exactly "
  "what it was built to do - guarding visibility - on inputs you had not "
  "classified as visibility."),
 "key_points": [
  "Praise, public help, success, intimacy, nearby laughter, and even rest can trigger shame.",
  "The circuit monitors visibility, not valence - positive attention is still attention.",
  "Ambiguous social data gets resolved in the threatening direction under arousal.",
  "Busyness can function as armor; stillness removes it and exposes the raw self.",
  "Surprise triggers confuse most because the conscious mind had filed the input as safe."],
 "requirements": [
  "Catalog the surprise triggers with fictional vignettes.",
  "Explain the visibility-not-valence principle clearly.",
  "Normalize the confusion these triggers cause.",
  "No real person described; examples fictional."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people, no therapeutic promises."],
 "citations": [CIT_APA, CIT_SCHEFF],
 "sig_lens": ("The Signature lens posts sentries on the unexpected "
  "roads: praise hill, success ridge, intimacy pass, the quiet valley of "
  "rest. The master is not ambushed twice by the same terrain - once a "
  "surprise trigger is mapped, it joins the known country, and known "
  "country can be traveled with open eyes."),
},
{
 "key": "shame_chain_reactions",
 "name": "Chain Reactions: How One Trigger Sets Off a Cascade",
 "group": "Compounded", "ladder_rank": 21, "ladder_tier": "compounded",
 "description": ("Shame rarely detonates singly; it chain-detonates. A "
  "single trigger - a fumbled answer in a meeting - fires the first "
  "charge, and the blast sets off the neighboring charges in sequence. "
  "First comes the meta-shame: shame about being ashamed - the blush "
  "noticed, the shaking hands seen, and now a second wave of exposure "
  "about the visible first wave. Then the archive opens: the current "
  "scene summons every similar scene on file, and the mind runs a "
  "highlight reel of humiliations stretching back years, each one "
  "re-felt at partial strength. Then the generalization spreads: from "
  "\"I botched that answer\" to \"I am bad at this job\" to \"I am a "
  "fraud here\" - the verdict widening from moment to role to self. "
  "Then the social prediction: the future is pre-played as a series of "
  "exposures - tomorrow's meeting, next week's review - each imagined "
  "scene firing a smaller advance charge. Finally the behavioral "
  "cascade: withdrawal, cancellation, silence, the shrinking of the "
  "life to fit the smaller self the chain has built. One fumbled "
  "answer, honestly appraised, deserved thirty seconds of pink cheeks. "
  "The chain turned it into a season."),
 "how_it_works": ("The cascade runs on four amplifiers. "
  "Self-referential processing turns the feeling into its own trigger: "
  "noticing your own shame display re-fires the exposure circuit, "
  "because the audience now includes yourself watching yourself. "
  "Associative memory spreads activation to similar scenes - the "
  "network logic of the archive: nodes linked by resemblance fire "
  "together. Overgeneralization widens the verdict because the "
  "appraisal system, under arousal, trades precision for speed - \"this "
  "went badly\" becomes \"I am bad\" before the slower, accurate "
  "appraisal can intervene. And affective forecasting projects the "
  "current feeling forward, pre-loading future scenes with dread that "
  "then functions as advance exposure. Each amplifier feeds the next: "
  "meta-shame raises arousal, arousal speeds overgeneralization, "
  "generalization darkens the forecast, the forecast justifies "
  "withdrawal, withdrawal prevents disconfirmation. Breaking the chain "
  "means breaking any single link - usually the earliest: naming the "
  "meta-shame (\"I am embarrassed about blushing, which is normal\"), "
  "containing the archive (\"that was then\"), or shrinking the "
  "verdict back to the moment (\"one answer, not a career\")."),
 "key_points": [
  "Shame chain-detonates: meta-shame, archive replay, generalization, dread forecast, withdrawal.",
  "Meta-shame re-fires the circuit: the audience now includes yourself watching yourself.",
  "Under arousal, appraisal trades precision for speed: one answer becomes a career verdict.",
  "Each amplifier feeds the next in a self-sealing loop.",
  "Break any single link - earliest is best - and the chain loses its fuel."],
 "requirements": [
  "Walk the cascade in order through one sustained fictional example.",
  "Name the four amplifiers and how they feed each other.",
  "Show where the chain can be broken, in general safe terms.",
  "No real person described; no clinical language."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people, no therapeutic promises."],
 "citations": [CIT_TANGNEY, CIT_GROSS],
 "sig_lens": ("The Signature lens diagrams the chain as a row of powder "
  "kegs with a single fuse: the master's art is fuse-cutting. You cannot "
  "unlight the first keg - the fumbled answer happened - but the "
  "second keg only blows if the fuse reaches it. Cut it early, cut it "
  "with naming, and the season shrinks back to thirty seconds of pink "
  "cheeks."),
},
{
 "key": "shame_behavior_actions",
 "name": "What People Do in Shame: Actions and Reactions",
 "group": "Advanced", "ladder_rank": 22, "ladder_tier": "advanced",
 "description": ("Shame writes its signature across behavior in a "
  "recognizable choreography. Withdrawal leads: the early departure, "
  "the cancelled plan, the unanswered message, the seat at the edge, "
  "the sudden need to be anywhere else. Concealment follows: the story "
  "edited, the failure minimized or reframed, the evidence tidied away "
  "before visitors arrive - not from dishonesty as a trait but from the "
  "emotion's prime directive, hide. Deflection is the social version: "
  "the joke that changes the subject, the counter-accusation (\"well, "
  "you did worse\"), the sudden interest in someone else's flaws - "
  "anything to move the spotlight. Overcompensation appears in the "
  "proud: the flawless performance, the excessive generosity, the "
  "perfectionism that is really camouflage - if nothing is ever wrong, "
  "nothing can be exposed. And in some, the pressure inverts into "
  "aggression: the humiliated person humiliating back, the exposed "
  "person exposing someone else - shame flipped outward into attack, "
  "the spotlight thrown like a weapon. Beneath all five moves runs the "
  "same program: reduce exposure, restore the hidden self, survive the "
  "audience."),
 "how_it_works": ("The five behaviors are strategies serving one goal - "
  "exposure management. Withdrawal reduces the audience to zero, the "
  "most reliable fix. Concealment reduces the exposure while keeping "
  "the audience, a riskier bargain. Deflection keeps both but moves "
  "the spotlight's target - effective in the moment, costly in "
  "relationships. Overcompensation tries to eliminate future exposure "
  "by eliminating future failure, an impossible contract that "
  "manufactures chronic pressure. Aggression inverts the circuit: "
  "instead of managing one's own exposure, it creates exposure in "
  "another, which temporarily relieves the self-focus by relocating it. "
  "Each strategy works in the short term - that is why people use them - "
  "and each charges interest: withdrawal starves the person of the "
  "disconfirming experiences that would shrink the shame; concealment "
  "requires constant vigilance; deflection corrodes trust; "
  "overcompensation exhausts; aggression multiplies enemies. The "
  "behavioral signature of shame is thus tragically self-extending: "
  "every move that relieves the moment feeds the conditions for the "
  "next one."),
 "key_points": [
  "The five moves: withdrawal, concealment, deflection, overcompensation, inverted aggression.",
  "All serve one goal: exposure management - reduce the audience, the exposure, or the spotlight's target.",
  "Each works short-term and charges interest long-term.",
  "Withdrawal starves the person of the disconfirming experiences that would shrink the shame.",
  "The signature is self-extending: relief now feeds the conditions for next time."],
 "requirements": [
  "Catalog the five behavioral moves with fictional examples.",
  "Show the single goal beneath the variety and the interest each charges.",
  "Keep it descriptive; no moral judgment of the behaviors.",
  "No real person described as doing any of these."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people, no therapeutic promises."],
 "citations": [CIT_TANGNEY, CIT_NATHANSON],
 "sig_lens": ("The Signature lens lists the five moves as the standard "
  "retreats of a routed army - each orderly in the moment, each ceding "
  "ground the army will have to retake later. The master's alternative "
  "is the disciplined stand: remain visible, keep the ranks (the "
  "relationships), and let the enemy - the feeling, not the people - "
  "spend itself against a line that does not break."),
},
{
 "key": "shame_speech_patterns",
 "name": "The Voice of Shame: Speech Patterns",
 "group": "Advanced", "ladder_rank": 23, "ladder_tier": "advanced",
 "description": ("Shame has an accent, and you can hear it before you see "
  "it. Volume drops first - the shamed voice gets quieter, as if "
  "loudness were exposure. Pitch often rises slightly and tightens; "
  "the relaxed resonance drains out and the voice goes thin. Pace "
  "changes two ways: the rush - sentences tumbling over each other to "
  "get the exposed moment over with - or the stall - long pauses, "
  "false starts, sentences abandoned halfway when the inner audience "
  "vetoes them. The characteristic phrases are all minimizers and "
  "pre-apologies: \"sorry, this is probably stupid, but...\", \"I "
  "know this sounds bad...\", \"never mind, forget it\" - the content "
  "disclaiming itself before the audience can. Self-reference spikes: "
  "\"I\" statements multiply, but they are all verdicts - \"I'm such "
  "an idiot,\" \"I always do this\" - the self put on trial in its "
  "own mouth. Questions replace assertions: everything comes out as "
  "\"does that make sense?\" seeking the absolution of agreement. "
  "And underneath it all, the laugh - the small breathy laugh after "
  "one's own sentence, discounting it in advance, inviting the "
  "listener to join in dismissing what was just said."),
 "how_it_works": ("The vocal pattern is the appeasement program applied "
  "to the voicebox. Lower volume and reduced resonance physically shrink "
  "the speaker's acoustic footprint - less space taken in the room's "
  "air, matching the body's spatial shrinking. The pitch rise is "
  "arousal leaking through the vocal cords: tension shortens the "
  "vibrating length, raising frequency, the same physics as a tightened "
  "guitar string. The rush-or-stall pacing reflects the approach-"
  "avoidance conflict playing out in real time - the urge to get "
  "through the exposure (rush) fighting the urge to not be heard at "
  "all (stall). The minimizers and pre-apologies are verbal "
  "submission displays, functionally identical to the averted gaze: "
  "\"I concede before you judge.\" The self-verdict \"I\" statements "
  "externalize the inner trial, recruiting the listener as a second "
  "judge - which is why they feel so uncomfortable to hear. The "
  "discounting laugh is the most economical move in the repertoire: a "
  "puff of air that tries to delete the sentence it follows."),
 "key_points": [
  "Volume drops and resonance thins - the acoustic footprint shrinks with the body.",
  "Pace splits: the rush to get through it, or the stall of vetoed sentences.",
  "Minimizers and pre-apologies are verbal submission displays.",
  "Self-verdict \"I\" statements put the self on trial in its own mouth.",
  "The discounting laugh tries to delete the sentence it follows."],
 "requirements": [
  "Cover volume, pitch, pace, phrasing, self-reference, and the laugh.",
  "Explain the appeasement function behind each vocal feature.",
  "Keep examples fictional; quote only invented phrases.",
  "No real person's speech described or diagnosed."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people, no therapeutic promises."],
 "citations": [CIT_EKMAN, CIT_SCHEFF],
 "sig_lens": ("The Signature lens tunes the ear to the accent: the "
  "master hears the minimizers not as weakness but as intelligence - "
  "the speaker is running a full threat assessment in real time and "
  "negotiating with an audience. The discipline is to let the voice "
  "take its natural size again: full breath, finished sentences, no "
  "pre-apology. A voice allowed its volume is a self allowed its "
  "space."),
},
{
 "key": "shame_decisions_judgment",
 "name": "Shame and Judgment: What It Makes People Choose",
 "group": "Advanced", "ladder_rank": 24, "ladder_tier": "advanced",
 "description": ("Shame is a quiet legislator: it does not announce its "
  "laws, it just vetoes options. Under its influence, people "
  "systematically choose the smaller life. Opportunities get declined - "
  "the application not sent, the audition skipped, the introduction not "
  "made - not from lack of desire but from the pre-played exposure: the "
  "mind has already staged the failure and the audience, and the "
  "decision is made inside that theater. Risks get mispriced: the "
  "downside of trying is inflated (\"everyone will see me fail\") while "
  "the downside of not trying is invisible (the life not lived leaves "
  "no footage). Relationships get filtered: people gravitate toward "
  "audiences that feel safe - the uncritical, the familiar, the "
  "lower-stakes - and avoid the very mentors, partners, and stages "
  "that could actually change their standing. Spending follows: money "
  "flows toward concealment and camouflage - the clothes that hide, the "
  "grooming that armors, the credentials collected as shields. And "
  "truth-telling gets taxed: the shamed person edits, omits, and "
  "deflects in conversations where honesty would cost exposure, which "
  "slowly starves relationships of the intimacy they need. None of "
  "these are decisions in the deliberative sense; they are the "
  "emotion's vetoes wearing the costume of preferences."),
 "how_it_works": ("The mechanism is affect-as-information applied to "
  "choice: the feeling is consulted as data about the option. An "
  "opportunity that triggers shame-preview feels dangerous, and the "
  "decision system - which cannot distinguish \"feels dangerous\" from "
  "\"is dangerous\" without effort - codes it as a bad bet. Loss "
  "aversion multiplies the effect: the vivid, immediate, social loss "
  "of exposure outweighs the abstract, delayed gain of trying, so the "
  "expected-value math comes out wrong in a predictable direction. "
  "The audience-filtering is risk management by the threat system: "
  "choosing low-judgment company reduces the exposure dial, which "
  "genuinely lowers shame in the short run - at the price of never "
  "updating the self-model with evidence from higher-stakes rooms. The "
  "concealment spending is impression management made material. And "
  "the honesty tax compounds: each edited truth makes the presented "
  "self more fragile (more to protect), which raises future exposure "
  "risk, which raises the editing - the legislator passing stricter "
  "laws every session. Seeing the vetoes as vetoes, rather than as "
  "taste or personality, is what returns the decisions to their owner."),
 "key_points": [
  "Shame vetoes options quietly: the smaller life chosen as if by preference.",
  "Risks get mispriced: vivid exposure-loss outweighs invisible not-trying loss.",
  "Audiences get filtered toward the safe and familiar, away from growth rooms.",
  "Resources flow to camouflage: hiding, armoring, credential-shielding.",
  "Honesty gets taxed, which makes the presented self more fragile, which raises future risk."],
 "requirements": [
  "Show the five decision domains: opportunity, risk, relationships, spending, honesty.",
  "Explain the affect-as-information mechanism in plain terms.",
  "Frame the vetoes as the emotion's work, not the person's character.",
  "Fictional examples only; no real person described."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people, no therapeutic promises."],
 "citations": [CIT_LAZARUS, CIT_TANGNEY],
 "sig_lens": ("The Signature lens audits the legislator: the master "
  "pulls the veto record and reads each rejected option aloud - the "
  "unsent application, the skipped stage, the unmade introduction. Most "
  "vetoes, examined in daylight, were cast by fear wearing a judge's "
  "robe. The discipline is re-vote: return each real decision to its "
  "owner, and let the owner - not the weather - cast it."),
},
{
 "key": "shame_escalation",
 "name": "Shame Under Intensity: How Actions Escalate",
 "group": "Advanced", "ladder_rank": 25, "ladder_tier": "advanced",
 "description": ("As shame intensifies, behavior escalates through a "
  "predictable staircase. Step one is freezing: the person goes quiet "
  "and still mid-scene, the system overloaded, words stopped at the "
  "throat. Step two is flight: the abrupt exit, the cancelled "
  "everything, the disappearing act - sometimes literal (leaving the "
  "room) and sometimes social (going unreachable for days). Step three "
  "is the cover-up campaign: the story gets actively managed - "
  "evidence deleted, witnesses charmed or avoided, alibis constructed - "
  "the concealment of step two industrialized. Step four is "
  "counterattack: the shamed person goes on offense, exposing or "
  "attacking others, picking fights, manufacturing scandals - the "
  "spotlight thrown outward as a weapon because inward has become "
  "unbearable. Step five, at the extreme, is self-erasure: quitting "
  "the job, the school, the city, the relationship - burning the "
  "whole context so the exposure cannot follow. Each step is more "
  "expensive than the last, and each is an attempt to solve the "
  "previous step's failure: flight when freezing did not end it, "
  "cover-up when flight left the story alive, attack when cover-up "
  "failed, erasure when everything failed. The staircase is logical "
  "from inside the feeling and ruinous from outside it."),
 "how_it_works": ("Escalation follows the defense cascade pushed past "
  "its normal limits. Freeze is the first defense when neither fight "
  "nor flight seems viable in a social exposure - immobility as "
  "invisibility. When the exposure continues despite freezing, the "
  "system promotes to flight: remove the self from the audience "
  "entirely. When flight fails - the story follows, the archive "
  "replays - the system escalates to active concealment, recruiting "
  "planning and deception in service of the original hide directive. "
  "Counterattack is the fight branch finally engaging, but displaced: "
  "the threat is the audience's judgment, which cannot be fought "
  "directly, so aggression lands on available targets. Self-erasure is "
  "the terminal logic of exposure management: if the self cannot be "
  "hidden within the context, abandon the context. The through-line is "
  "that each step preserves the core error - treating the feeling as "
  "a fact about the self rather than a signal about a moment - while "
  "raising the price of the strategy. De-escalation runs the staircase "
  "in reverse: the cheapest effective intervention is early, at the "
  "freeze, before the expensive steps get funded."),
 "key_points": [
  "The staircase: freeze, flight, cover-up campaign, counterattack, self-erasure.",
  "Each step tries to solve the previous step's failure, at rising cost.",
  "Counterattack is the fight branch displaced: judgment cannot be fought, so targets substitute.",
  "Self-erasure is exposure management's terminal logic: abandon the context.",
  "De-escalation runs the staircase in reverse; earliest intervention is cheapest."],
 "requirements": [
  "Walk the five steps in order with fictional texture at each.",
  "Explain the defense-cascade logic driving the escalation.",
  "Show the rising cost and the core error preserved at every step.",
  "No real person described; no graphic or harmful detail."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people, no therapeutic promises."],
 "citations": [CIT_NATHANSON, CIT_IZARD],
 "sig_lens": ("The Signature lens posts the staircase on the war-room "
  "wall with costs tallied beside each step: freeze is free, flight is "
  "cheap, cover-up is dear, counterattack is ruinous, erasure is "
  "bankruptcy. The master's doctrine: never fund step two with step "
  "three's money. Meet the feeling at the freeze - name it, breathe, "
  "stay - and the expensive steps never get their appropriation."),
},
{
 "key": "shame_healthy_expression",
 "name": "Expressing Shame Healthily: Saying It, Showing It, Channeling It",
 "group": "Advanced", "ladder_rank": 26, "ladder_tier": "advanced",
 "description": ("Shame can be expressed well, and the skill is learnable. "
  "Saying it is the first art: naming the feeling out loud to a safe "
  "person - \"I feel ashamed about what happened in there\" - does what "
  "secrecy never can, which is move the feeling from the hidden archive "
  "into shared air, where it almost always turns out smaller than it felt "
  "in the dark. The naming must be of the feeling, not a confession "
  "extorted by it: there is a difference between \"I feel ashamed\" "
  "(a report) and the shame-driven oversharing that tries to pre-empt "
  "judgment by judging oneself first. Showing it is the second art: "
  "allowing the brief, honest display - the dropped gaze, the honest "
  "blush, the \"that was embarrassing\" - instead of the frozen mask; "
  "audiences consistently respond to clean, brief shame with warmth, "
  "because the honest signal reads as trustworthiness. Channeling it is "
  "the third: converting the signal into its message - shame points at "
  "a standard you care about, so the healthy response is to serve the "
  "standard: apologize where apology is owed, practice where practice "
  "was lacking, repair what can be repaired. Expressed this way, shame "
  "completes its circuit: signal received, message read, action taken, "
  "circuit closed."),
 "how_it_works": ("Healthy expression works by giving the emotion what "
  "it evolved to produce: social repair. Naming it to a safe person "
  "recruits co-regulation - another nervous system helping to down-"
  "regulate yours - and it corrects the audience inflation, because "
  "the real listener's actual reaction replaces the imagined "
  "catastrophe. Allowing the brief honest display works through the "
  "honest-signal mechanism: the involuntary components (blush, gaze "
  "drop) are trusted by observers as sincere, which elicits appeasement "
  "and affiliation rather than judgment - the mask, by contrast, reads "
  "as hiding something worse. Channeling works through the standard: "
  "shame's information content is \"a valued standard was breached,\" "
  "so action serving the standard resolves the appraisal that fired "
  "the emotion - the circuit closes because its job is done. The three "
  "together form the complete healthy sequence: disclose (break "
  "secrecy), display briefly (let the honest signal work), and act on "
  "the standard (close the circuit). Skipping straight to action "
  "without disclosure leaves the secrecy feeding the next round; "
  "disclosure without action leaves the standard unserved."),
 "key_points": [
  "Say it: naming the feeling to a safe person moves it from archive to air, where it shrinks.",
  "Name the feeling, not a self-prosecution: \"I feel ashamed\" is a report, not a trial.",
  "Show it briefly: the honest display reads as trustworthiness and draws warmth.",
  "Channel it: shame points at a valued standard - serve the standard to close the circuit.",
  "The complete sequence: disclose, display briefly, act on the standard."],
 "requirements": [
  "Teach the three arts: saying, showing, channeling, in order.",
  "Distinguish healthy naming from shame-driven self-prosecution.",
  "Keep all guidance general, safe, and everyday; no therapeutic prescriptions.",
  "Fictional examples only; no real person described."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people, no therapeutic promises."],
 "citations": [CIT_TANGNEY, CIT_GROSS],
 "sig_lens": ("The Signature lens frames healthy expression as the "
  "honorable discharge of a signal: the sentry reports, the report is "
  "heard, the orders that follow serve the standard the sentry was "
  "guarding. The master does not shoot the sentry for bringing bad news "
  "and does not let the sentry command the army. Report, hear, act - "
  "then stand down."),
},
]

ENTRIES += [
{
 "key": "shame_unhealthy_expression",
 "name": "The Two Costly Paths: Bottling Up and Melting Down",
 "group": "Advanced", "ladder_rank": 27, "ladder_tier": "advanced",
 "description": ("Shame mishandled takes two opposite roads to the same "
  "ruin. Bottling up is the first: the feeling is sealed, never named, "
  "never shown - the frozen smile in the meeting, the \"I'm fine\" "
  "through clenched teeth, the subject changed with practiced speed. "
  "The seal holds for a while, and the price accrues invisibly: the "
  "replay loop runs hotter in private, the body keeps the ledger (the "
  "tension, the thin sleep, the knotted stomach), and the pressure "
  "finds side exits - irritability at safe targets, numb scrolling, "
  "the drink that quiets the audience for an evening. Melting down is "
  "the second: the feeling floods past all containment - the sobbing "
  "confession to near-strangers, the rage at the person who witnessed "
  "it, the dramatic resignation fired off at midnight. The flood feels "
  "like honesty but it is the feeling driving, not the person: words "
  "are said that cannot be unsaid, bridges burned that were never the "
  "problem. Both paths share one error - the feeling is treated as "
  "either unspeakable or unstoppable, when it is neither. Bottling "
  "says \"this must never be seen\"; melting says \"this is all there "
  "is.\" The middle road - named, brief, channeled - is available to "
  "both travelers the moment they stop."),
 "how_it_works": ("Bottling up is chronic suppression, and suppression "
  "has a known profile: it reduces the outward display while leaving "
  "the inner arousal intact or elevated - the audience is fooled, the "
  "body is not. The monitoring required (\"am I showing it?\") keeps "
  "attention locked on the feeling, which sustains it; the unprocessed "
  "material accumulates as the replay loop, the somatic ledger, and "
  "the side exits. Melting down is the collapse of regulation under "
  "overload: the prefrontal braking fails, the feeling floods the "
  "action system, and behavior becomes emotion-driven rather than "
  "value-driven - the midnight resignation, the bridge-burning text. "
  "The flood then creates secondary shame (about the meltdown), which "
  "is why meltdowns so often lead to bottling: the person seals the "
  "next round tighter to prevent another flood, and the cycle "
  "alternates. Both are regulation failures in opposite directions - "
  "too much brake versus no brake - and both are maintained by the "
  "same belief: that the feeling, honestly met in moderate doses, "
  "would be unsurvivable. It is survivable; the evidence is that "
  "everyone who has ever named it briefly to a safe person has "
  "survived it."),
 "key_points": [
  "Bottling up: the seal holds publicly while arousal, replay, and somatic cost accrue privately.",
  "Suppression fools the audience but not the body; monitoring the mask sustains the feeling.",
  "Melting down: regulation collapses, the feeling drives, words and bridges burn.",
  "The flood creates secondary shame, which often leads to tighter bottling - the alternating cycle.",
  "Both share one error: treating the feeling as unspeakable or unstoppable, when it is neither."],
 "requirements": [
  "Present both paths with fictional texture and their distinct cost profiles.",
  "Explain the suppression profile and the flood-then-seal cycle.",
  "Keep it descriptive; no judgment of people who use these paths.",
  "No real person described; guidance stays general and safe."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people, no therapeutic promises."],
 "citations": [CIT_GROSS, CIT_TANGNEY],
 "sig_lens": ("The Signature lens names the two roads the sealed vault "
  "and the breached dam - both failures of water management, neither "
  "the river's fault. The master builds the sluice instead: controlled "
  "release, measured flow, the water doing its work in the channel "
  "instead of rotting the vault or drowning the valley."),
},
{
 "key": "shame_everyday_practices",
 "name": "Everyday Practices That Keep Shame in Balance",
 "group": "Advanced", "ladder_rank": 28, "ladder_tier": "advanced",
 "description": ("Balance with shame is maintained the way fitness is - "
  "by small repeated practices, not by heroic interventions. The "
  "naming habit: when the heat rises, silently label it - \"shame, "
  "moderate, about the meeting\" - which moves the experience from "
  "flooded to filed. The audience audit: ask, concretely, who actually "
  "saw, who actually cares, and what they are probably thinking about "
  "right now (usually their own day) - the inflation deflates under "
  "specifics. The standard check: is the breached standard yours, or "
  "one you inherited and never chose? Many chronic shames are loyal "
  "service to standards the person would not endorse on reflection. "
  "The exposure budget: deliberately taking small, survivable "
  "exposures - asking the question, posting the work, telling the "
  "small truth - which files the updates that avoidance never files. "
  "The repair reflex: when something genuinely was wrong, doing the "
  "small repair promptly - the apology, the correction, the redo - "
  "which closes circuits before they become archives. And the "
  "body practice: uncurling on purpose - shoulders back, breath deep, "
  "feet on the floor - not as performance but as a message to the "
  "nervous system that the threat has passed. None of these is "
  "dramatic. That is why they work: they are maintenance, and shame "
  "is a maintenance problem."),
 "how_it_works": ("Each practice targets one link in the shame circuit. "
  "Naming recruits the labeling effect: putting a precise label on an "
  "affect reduces amygdala-region reactivity and engages the "
  "observing stance - the feeling becomes data rather than weather. "
  "The audience audit corrects the appraisal inflation directly: the "
  "circuit's \"everyone saw\" cannot survive the concrete census of "
  "three distracted colleagues. The standard check works upstream of "
  "the emotion: standards you would not endorse cannot survive "
  "endorsement review, and a standard dissolved is a trigger "
  "disarmed. The exposure budget is graded extinction in plain "
  "clothes: small survivals teach the threat system that visibility "
  "is not catastrophe, updating the file one safe entry at a time. "
  "The repair reflex closes the guilt half of the blend promptly, "
  "which starves the shame half of its favorite fuel - the unrepaired "
  "act rehearsed nightly. The body practice uses the two-way street: "
  "posture and breath are inputs to the threat system, not just "
  "outputs, so deliberately opening them sends \"all clear\" up the "
  "same wires that sent the alarm down. Together they form a daily "
  "hygiene: none sufficient alone, all compounding quietly."),
 "key_points": [
  "Naming: label it precisely - \"shame, moderate, about the meeting\" - and it becomes data, not weather.",
  "Audience audit: the concrete census (who saw, who cares) deflates \"everyone saw.\"",
  "Standard check: many chronic shames serve standards you never chose and would not endorse.",
  "Exposure budget: small survivable exposures file the updates avoidance never files.",
  "Repair reflex plus body practice: close circuits promptly, send \"all clear\" up the wires."],
 "requirements": [
  "Present six concrete practices in plain everyday language.",
  "Explain the mechanism each practice targets.",
  "Keep everything general wellness-level; no therapeutic prescriptions.",
  "Fictional examples only; no real person described."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people, no therapeutic promises."],
 "citations": [CIT_GROSS, CIT_APA],
 "sig_lens": ("The Signature lens keeps these practices as the daily "
  "orders of the garrison: name the weather, audit the watchers, "
  "inspect the standards, drill small exposures, repair promptly, "
  "stand at ease. The master does not wait for the siege to practice "
  "the drill - the drill is what keeps the siege from ever quite "
  "arriving."),
},
{
 "key": "shame_reading_others",
 "name": "Reading the Signs: Shame in Other People",
 "group": "Advanced", "ladder_rank": 29, "ladder_tier": "advanced",
 "description": ("Reading shame in others is a literacy worth having, "
  "because the shamed rarely announce themselves - announcement would "
  "be more exposure. The face gives it first: the gaze that will not "
  "hold yours, dropping at the exact moment of the tender subject; "
  "the mouth pressed thin; the blush rising while the words stay "
  "steady. The body seconds it: the sudden stillness, the angling "
  "away, the hand finding the face, the person becoming physically "
  "smaller in their chair. The voice confirms: volume dropping, "
  "sentences trailing, the pre-apology before the content, the "
  "discounting laugh after it. Behavior completes the picture: the "
  "topic changed with unnatural speed, the joke deployed as a "
  "smokescreen, the early exit, the message left unanswered. Context "
  "is the final lens: these signs mean most right after an exposure "
  "moment - a correction, a revelation, a comparison, a spotlight. "
  "The same averted gaze at a funeral is grief; after a public "
  "mistake it is shame. Read the cluster, not the single cue, and "
  "read it against the moment. And read it to understand, never to "
  "expose: the whole point of the literacy is to handle the person "
  "more gently, not to demonstrate your perception."),
 "how_it_works": ("The reading works because the shame display is "
  "redundant - face, body, voice, and behavior broadcast the same "
  "message on parallel channels, so the cluster is far more reliable "
  "than any single cue. The context rule exists because most "
  "individual cues are shared with other states: gaze aversion also "
  "marks thoughtfulness and cultural deference, stillness also marks "
  "attention, quiet voice also marks fatigue. Base rates matter: "
  "immediately after an exposure event, the probability that the "
  "cluster means shame spikes, because the circuit's trigger "
  "(standard, exposure, audience) has just been satisfied in plain "
  "view. The developmental note matters too: children show it "
  "whole-body and unmasked, adults show it in fragments - a flicker "
  "here, a laugh there - because display rules have layered the "
  "reflex. The ethical constraint is functional, not just polite: "
  "naming someone's shame aloud (\"you look ashamed\") re-fires the "
  "exposure circuit with you as the audience, which is the opposite "
  "of help. Literacy is for calibration of your own behavior - softer "
  "voice, normal pace, no spotlight - not for diagnosis."),
 "key_points": [
  "Read the cluster across face, body, voice, and behavior - never a single cue.",
  "Context is the lens: the same signs mean most right after an exposure moment.",
  "Adults show it in fragments; children show it whole-body and unmasked.",
  "Most single cues are shared with other states; base rates decide the reading.",
  "Read to handle gently, never to expose: naming it aloud re-fires the circuit."],
 "requirements": [
  "Teach the four channels and the context rule.",
  "Explain why clusters beat single cues and why base rates matter.",
  "Include the ethical constraint: literacy serves gentleness, not exposure.",
  "No real person read or labeled; all figures fictional."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people, no therapeutic promises."],
 "citations": [CIT_EKMAN, CIT_SCHEFF],
 "sig_lens": ("The Signature lens treats this literacy as scoutcraft: "
  "the master reads sign - the bent grass of the averted gaze, the "
  "broken twig of the trailing sentence - to know the ground he walks "
  "with another traveler. And the scout's first law: you read sign to "
  "guide your own steps softly, never to shout what you have seen "
  "across the valley."),
},
{
 "key": "shame_supportive_responses",
 "name": "What to Say and Do When Someone Near You Feels Shame",
 "group": "Advanced", "ladder_rank": 30, "ladder_tier": "advanced",
 "description": ("When someone near you is in shame, your job is to "
  "shrink the audience, not join it. First, normalize without "
  "dismissing: \"That happens to everyone\" lands; \"don't be silly, "
  "it's nothing\" does not - the first joins them, the second "
  "overrules their feeling. Second, keep your own face and voice "
  "ordinary: steady gaze offered but not forced, normal pace, no "
  "spotlight behaviors like announcing their moment to the room or "
  "making it a teaching example. Third, offer the specific "
  "counter-evidence their loop is deleting: not generic praise but "
  "the concrete true thing - \"your analysis was the reason we "
  "caught it in time.\" Fourth, give them a graceful role: a small "
  "useful task, a question only they can answer - nothing says \"you "
  "belong here\" like being needed. Fifth, protect their exit: make "
  "leaving easy and returning easier - \"take whatever time you "
  "need; we'll be here.\" What you are doing, underneath the "
  "techniques, is lending them your nervous system as proof that the "
  "audience is safe - co-regulation in plain clothes. And afterward, "
  "do not bring it up again unless they do; the kindest epilogue to "
  "a shame scene is its quiet burial."),
 "how_it_works": ("Each move targets a dial of the shame circuit. "
  "Normalizing without dismissing validates the feeling while "
  "correcting the verdict: \"everyone\" shrinks the imagined audience "
  "from a tribunal to a crowd of fellow stumblers. The ordinary face "
  "and voice work through social referencing - people in alarm read "
  "the faces around them to calibrate threat, and a calm ordinary "
  "face is data that the situation is survivable. Specific "
  "counter-evidence works where generic praise fails because the "
  "shame loop has a fact-checker that rejects incongruent data; a "
  "concrete, verifiable true thing gets past it. The graceful role "
  "restores belonging - the deepest wound shame inflicts - by making "
  "the person functionally included rather than merely tolerated. "
  "The protected exit removes the trapped feeling that escalates "
  "freeze into flight; knowing escape is available often makes "
  "escape unnecessary. And the quiet burial afterward prevents the "
  "scene from becoming archive material - unrehearsed by others, it "
  "fades faster. Together the moves say, in the only language the "
  "alarm understands: the bond is intact."),
 "key_points": [
  "Shrink the audience, never join it: normalize without dismissing.",
  "Keep face and voice ordinary; offer steady gaze without forcing it.",
  "Counter the loop with specific true counter-evidence, not generic praise.",
  "Give a graceful role: being needed says \"you belong\" louder than reassurance.",
  "Protect the exit, and bury the scene quietly afterward unless they raise it."],
 "requirements": [
  "Give five concrete moves with example phrasing.",
  "Explain the circuit dial each move targets.",
  "Distinguish normalizing from dismissing clearly.",
  "Fictional scenarios only; no real person described."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people, no therapeutic promises."],
 "citations": [CIT_TANGNEY, CIT_GROSS],
 "sig_lens": ("The Signature lens frames the helper as the steady "
  "torchbearer walking beside someone in a dark stretch: you do not "
  "grab their arm, lecture about the dark, or shine the torch in "
  "their face - you walk at their pace, keep the light on the path, "
  "and let your unhurried steps prove the ground is solid. That is "
  "the whole art."),
},
{
 "key": "shame_mistakes_to_avoid",
 "name": "What NOT to Do: The Mistakes That Make Shame Worse",
 "group": "Advanced", "ladder_rank": 31, "ladder_tier": "advanced",
 "description": ("Good intentions pave several roads into deeper shame. "
  "Mistake one: spotlighting - \"Everyone, listen to what happened to "
  "poor Sam!\" - retelling their scene, even sympathetically, re-fires "
  "the exposure with a larger audience. Mistake two: the pep-talk "
  "overcorrection - \"You're amazing, this is nothing, forget it!\" - "
  "which the shame loop hears as \"you don't understand,\" widening "
  "the gap between their feeling and your response. Mistake three: "
  "the fix-it rush - immediately problem-solving, advising, "
  "strategizing - which skips past the feeling to the repair and "
  "signals that the feeling itself is unacceptable. Mistake four: "
  "teasing it light - the affectionate joke about the incident, meant "
  "to defuse, which lands as confirmation that the scene is now "
  "public property. Mistake five: the tribunal of concern - gathering "
  "others to \"help,\" which multiplies the audience dial at the "
  "worst moment. Mistake six: confusing the mask for the person - "
  "treating the counterattack or the withdrawal as character rather "
  "than weather, and responding to the strategy instead of the "
  "feeling underneath. And mistake seven, the quietest: keeping "
  "score - remembering their shame scene and referencing it later, "
  "even fondly, which converts a fading moment into permanent "
  "archive. Every one of these is avoidable the moment you see the "
  "mechanism: each mistake inflates one of the three dials - audience, "
  "exposure, or verdict."),
 "how_it_works": ("Each mistake maps to a dial. Spotlighting and the "
  "tribunal of concern inflate the audience dial directly - more eyes, "
  "more evaluation, more alarm. Teasing it light and keeping score "
  "inflate the exposure dial: the moment is made permanent and public, "
  "uncontainable, which is exactly what the circuit fears most. The "
  "pep-talk overcorrection and the fix-it rush attack the verdict dial "
  "from the wrong side: by denying the feeling's legitimacy they "
  "confirm the person's isolation - \"no one here understands what "
  "this is like\" - which deepens the self-focus. Confusing the mask "
  "for the person misreads a defense as an identity, which locks the "
  "person into the strategy: treated as hostile, they stay hostile; "
  "treated as fragile, they stay hidden. The common thread is "
  "audience behavior that the threat system cannot distinguish from "
  "threat: good intentions do not register on the circuit - only "
  "exposure, eyes, and verdict do. The correction for every mistake "
  "is the same shape: fewer eyes, smaller exposure, lighter verdict."),
 "key_points": [
  "Spotlighting and tribunals of concern inflate the audience dial.",
  "Teasing and score-keeping inflate the exposure dial - the moment made permanent.",
  "Pep talks and fix-it rushes deny the feeling's legitimacy and deepen isolation.",
  "Confusing the mask for the person locks the defense in place.",
  "Every correction has the same shape: fewer eyes, smaller exposure, lighter verdict."],
 "requirements": [
  "Catalog seven concrete mistakes with the mechanism each feeds.",
  "Map each mistake to the dial it inflates.",
  "Keep tone instructive, not shaming of the reader.",
  "Fictional scenarios only; no real person described."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people, no therapeutic promises."],
 "citations": [CIT_SCHEFF, CIT_TANGNEY],
 "sig_lens": ("The Signature lens posts these mistakes as the seven "
  "traps on the helper's trail, each marked with its mechanism: here "
  "the ground inflates audiences, here it makes moments permanent, "
  "here it mistakes weather for character. The master walks the trail "
  "often enough to know every trap by feel - and steps around them "
  "without breaking stride."),
},
{
 "key": "shame_related_emotions",
 "name": "Shame's Neighbors: Guilt, Embarrassment, Humiliation, Pride",
 "group": "Advanced", "ladder_rank": 32, "ladder_tier": "advanced",
 "description": ("Shame's neighborhood is crowded, and the neighbors are "
  "easy to confuse. Guilt is the closest: both follow a transgression, "
  "but guilt's spotlight is on the act (\"I did a bad thing\" - repair "
  "it) while shame's is on the self (\"I am a bad person\" - hide). "
  "The test: if imagining the act undone would fix the feeling, it is "
  "guilt; if the feeling would survive the repair, shame is in the "
  "mix. Embarrassment is shame's lighter cousin: same blush, same "
  "gaze-drop, but brief, situational, and often shared - tripping on "
  "flat ground in front of friends ends in laughter, not in a "
  "rewritten self. The test: embarrassment fades when the moment "
  "passes; shame follows you home. Humiliation is shame with a "
  "perpetrator: someone deliberately exposed or degraded you, which "
  "adds fury at the exposer to the self-collapse - the signature is "
  "the hot urge for revenge riding alongside the wish to vanish. "
  "Pride is the mirror opposite: the self expanded under approval "
  "where shame contracts it under judgment - authentic pride (\"I did "
  "well\") steadies, hubristic pride (\"I am superior\") inflates, "
  "and both are legible in the same posture channels shame uses. "
  "Learn the four borders and you can name the weather precisely - "
  "and precise names are the beginning of precise responses."),
 "how_it_works": ("The neighbors separate along three axes. Axis one is "
  "the object of evaluation: act (guilt), self (shame), self-in-"
  "situation (embarrassment), self-under-attack (humiliation), self-"
  "approved (pride). Axis two is agency of exposure: self-caused "
  "(guilt, embarrassment), self-revealed (shame), other-inflicted "
  "(humiliation), other-confirmed (pride). Axis three is action "
  "tendency: repair (guilt), hide (shame), laugh-it-off (embarrassment), "
  "retaliate (humiliation), expand (pride). The confusion between "
  "them is natural because real events rarely fire one cleanly - a "
  "public moral failure fires guilt about the act, shame about the "
  "self, embarrassment about the scene, and humiliation if someone "
  "broadcast it. The practical value of the map is triage: each "
  "neighbor wants a different response - guilt wants repair, shame "
  "wants the audience shrunk and the standard examined, embarrassment "
  "wants a laugh and a change of subject, humiliation wants safety "
  "and the perpetrator addressed, pride wants savoring. Treating "
  "shame with guilt's medicine (repair alone) leaves the self-verdict "
  "untouched; treating guilt with shame's medicine (hiding) sabotages "
  "the repair."),
 "key_points": [
  "Guilt = the act (repair it); shame = the self (hide). The undone-act test tells them apart.",
  "Embarrassment = shame's brief situational cousin; it fades when the moment passes.",
  "Humiliation = shame plus a perpetrator; fury at the exposer rides with the collapse.",
  "Pride = the mirror opposite; the same channels run in expansion instead of contraction.",
  "Each neighbor wants different medicine; mismatched treatment leaves the real problem untouched."],
 "requirements": [
  "Map all four neighbors with distinguishing tests for each.",
  "Explain the three axes: object of evaluation, agency of exposure, action tendency.",
  "Show why real events fire blends and why triage matters.",
  "No real person labeled with any of these emotions."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people, no therapeutic promises."],
 "citations": [CIT_TANGNEY, CIT_APA],
 "sig_lens": ("The Signature lens keeps the neighborhood plat on the "
  "wall with every border surveyed: guilt's lot, embarrassment's "
  "cottage, humiliation's fortified house, pride's hall of mirrors - "
  "and shame's own grounds in the center. The master does not "
  "trespass lots or confuse addresses; he knocks on the right door "
  "with the right errand, and every neighbor answers better for it."),
},
{
 "key": "shame_emotion_mixes",
 "name": "Shame Blends: Plutchik-Style Dyads",
 "group": "Advanced", "ladder_rank": 33, "ladder_tier": "advanced",
 "description": ("Shame blended with other emotions produces compounds "
  "with their own weather. Shame plus anger makes humiliated fury: the "
  "collapse of the self with a live wire of retaliation - the person "
  "who was exposed and now wants someone to pay, the insult answered "
  "with disproportionate force. It looks like pure aggression from "
  "outside; inside it is still the wish to vanish, armed. Shame plus "
  "fear makes anticipatory dread: the social anxiety compound - not "
  "fear of the event but fear of the exposure inside the event, the "
  "party dreaded for weeks because of the imagined audience. Shame "
  "plus sadness makes the heavy withdraw: grief for the self that "
  "failed, the long quiet after the scene, the curtains drawn for "
  "days - mourning a verdict rather than a loss. Shame plus disgust "
  "makes self-contamination: the feeling of being unclean or tainted, "
  "the shower taken twice, the clothes thrown away - the self judged "
  "not just flawed but polluted. And shame plus joy makes the "
  "bittersweet wince: the promotion celebrated through the blush, the "
  "compliment that pleases and pains at once - visibility arriving "
  "with the reward, the spotlight inseparable from the prize. Each "
  "blend inherits shame's core - the self under eyes - and the "
  "partner's action tendency, which is why blends are harder to read "
  "and harder to weather than either parent alone."),
 "how_it_works": ("Blends form by appraisal fusion: the event is "
  "evaluated on two tracks simultaneously and the outputs combine. "
  "Shame's track always contributes the same elements - self as "
  "object, exposure, audience - while the partner contributes its "
  "own appraisal and, crucially, its action tendency. Anger "
  "contributes the blocked-goal/violated-boundary appraisal and the "
  "approach-attack tendency, which is why humiliated fury moves "
  "toward targets while pure shame moves away. Fear contributes "
  "threat appraisal and avoidance, stretching shame forward in time "
  "into dread. Sadness contributes loss appraisal and withdrawal, "
  "deepening the collapse into mourning. Disgust contributes "
  "contamination appraisal and expulsion, turning the verdict "
  "somatic. Joy contributes reward appraisal and approach, creating "
  "the paradox of wanting the prize and fearing its spotlight. "
  "The reading rule for blends: identify shame's signature first "
  "(the self under eyes - gaze, blush, shrinking), then read the "
  "partner's tendency (toward, away, down, out). The response rule: "
  "address the partner's need (safety for fear, repair for anger's "
  "grievance) while keeping shame's dials low - fewer eyes, smaller "
  "exposure - because every blend is still, underneath, an audience "
  "problem."),
 "key_points": [
  "Shame + anger = humiliated fury: the wish to vanish, armed.",
  "Shame + fear = anticipatory dread: fear of the exposure inside the event.",
  "Shame + sadness = heavy withdraw: mourning a verdict rather than a loss.",
  "Shame + disgust = self-contamination: the self judged polluted, not just flawed.",
  "Shame + joy = bittersweet wince: the prize inseparable from its spotlight."],
 "requirements": [
  "Describe five blends with distinct texture for each.",
  "Explain appraisal fusion: shame's core plus the partner's action tendency.",
  "Give the reading rule and the response rule for blends.",
  "Fictional examples only; no real person described."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people, no therapeutic promises."],
 "citations": [CIT_IZARD, CIT_NATHANSON],
 "sig_lens": ("The Signature lens keeps the blends as alloy samples in "
  "the assay office: shame-iron fused with anger-sulfur, fear-quicksilver, "
  "sadness-lead, disgust-ash, joy-gold. Each alloy has its own temper "
  "and its own working instructions. The master assayer identifies the "
  "alloy before striking - you do not work fury-iron with the tools for "
  "grief-lead."),
},
{
 "key": "shame_full_simulation",
 "name": "The Full Shame Simulation: Trigger to Resolution",
 "group": "Advanced", "ladder_rank": 34, "ladder_tier": "advanced",
 "description": ("The archive's showcase simulation, in five scenes. "
  "Scene one, the trigger: Dev, a junior analyst, is presenting his "
  "first major forecast when a senior voice cuts in - \"Those numbers "
  "don't hold up, do they?\" - and the room's attention swings to him "
  "like a searchlight. His face floods; his throat closes on the "
  "answer he had ready. Scene two, the peak: the meeting moves on but "
  "Dev does not - he sits through the remaining forty minutes inside "
  "the replay, hearing his own silence on loop, mapping every glance "
  "as judgment, his shoulders inching toward his ears. Scene three, "
  "the cascade: by evening the archive has opened - the stumble in "
  "the interview three years ago, the professor's correction in "
  "college - and the verdict has generalized from \"bad slide\" to "
  "\"fraud in this role\"; he drafts a resignation email and deletes "
  "it twice. Scene four, the turn: at home he names it aloud to his "
  "partner - \"I am drowning in shame about today\" - and says the "
  "concrete facts: one challenged slide, one fair question, a room "
  "that moved on by lunch. She offers the specific true thing: his "
  "model caught the error the senior missed last quarter. Scene five, "
  "the resolution: next morning he rechecks the numbers, finds the "
  "senior was half-right, and sends the correction with a brief "
  "note - the repair closing guilt's circuit while the disclosed, "
  "examined shame drains to its proper size: a bad ten minutes, not "
  "a verdict. The simulation's lesson is the whole database in "
  "miniature: trigger, peak, cascade, naming, repair, proportion "
  "restored."),
 "how_it_works": ("The simulation demonstrates the complete shame "
  "system in operation. The trigger satisfies the circuit - standard "
  "(competence), exposure (public challenge), audience (the room) - "
  "and the body fires the submission display before appraisal "
  "finishes. The peak shows attention reversal and the replay loop "
  "occupying working memory. The cascade demonstrates all four "
  "amplifiers: meta-shame (shame at the visible fluster), archive "
  "replay, overgeneralization (slide to fraud), and dread forecast "
  "(the resignation draft as pre-emptive self-erasure). The turn "
  "demonstrates the three healthy arts in sequence: disclosure "
  "(naming it to a safe person), the audience audit (the concrete "
  "census - a room that moved on), and specific counter-evidence "
  "defeating the loop's fact-checker. The resolution demonstrates "
  "circuit closure: the standard is served (numbers rechecked, "
  "correction sent), which resolves the guilt half, while the shame "
  "half drains through examination rather than obedience - the "
  "feeling kept as information (\"check the work\") and released as "
  "verdict (\"fraud\"). The simulation is descriptive throughout: "
  "it shows the machinery, it does not prescribe for any real "
  "person."),
 "key_points": [
  "Scene one: the trigger - standard, exposure, audience align in a single public moment.",
  "Scene two: the peak - attention reverses, the replay loop occupies the mind.",
  "Scene three: the cascade - meta-shame, archive, generalization, pre-emptive self-erasure.",
  "Scene four: the turn - disclosure, audience audit, specific counter-evidence.",
  "Scene five: resolution - the standard served, the feeling kept as information, released as verdict."],
 "requirements": [
  "Walk five scenes from trigger through peak, cascade, turn, to resolution.",
  "Show the database's machinery operating inside the story.",
  "Keep the character fictional and the telling descriptive, never prescriptive for real people.",
  "End with the lesson the simulation teaches about proportion."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people, no therapeutic promises."],
 "citations": [CIT_TANGNEY, CIT_GROSS],
 "sig_lens": ("The Signature lens screens this simulation as the "
  "master's own training film: watch Dev take the hit, ride the "
  "cascade, and - the move that matters - name the weather instead of "
  "obeying it. The film's final frame is the moral of the whole "
  "Signature: the feeling is an instrument, the person is the "
  "instrument's master, and mastery is not the absence of storms but "
  "the art of sailing through them with the cargo intact."),
},
]

assert len(ENTRIES) == 34, "expected 34 entries, got %d" % len(ENTRIES)
assert [e["ladder_rank"] for e in ENTRIES] == list(range(1, 35)), "ladder ranks must be 1..34"
assert len({e["key"] for e in ENTRIES}) == 34, "duplicate entry keys"
