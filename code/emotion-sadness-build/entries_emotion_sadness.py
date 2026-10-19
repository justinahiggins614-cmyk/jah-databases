#!/usr/bin/env python3
"""Entries for the Sadness Emotion databases (Manon's 2026-10-17 16:15 order,
emotion series batch 1).

Two NEW databases, 34 ladder-ordered records each:

  emotion-sadness              - The Sadness Emotion Database
                                 (public-harvest: real, fact-checked
                                 psychology of sadness - what it is, how it
                                 feels, body signals, facial expression,
                                 triggers, behavior, healthy expression,
                                 recognizing it in others, related emotions
                                 and mixes, full behavioral simulation;
                                 descriptive and educational only, never
                                 diagnosing real people)
  emotion-sadness-signature    - The Sadness Emotion Signature Database
                                 (his original Signature emotional science:
                                 sadness as the archive's signal of lost
                                 value, the mind weighing what mattered and
                                 marking the record; src signature, titles
                                 suffixed " (Signature Edition)", never
                                 presented as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-EMSA- (public) and JAH-EMSAS- (signature), verified free
in the manifest id_prefix values and with zero hits in every shard index
file (2026-10-17).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_emotion_sadness.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos.

Concurrency: this builder writes ONLY its own new untracked paths -
db/emotion-sadness/, db/emotion-sadness-signature/,
code/emotion-sadness-build/, the data-1 shard dirs, and the fragment file.
It never touches data/manifest.json, api.json, index.html, README.md,
docs/AI_ACCESS.md, and never commits or pushes. A merger handles those.

Screening: descriptive and educational only. No diagnosing real people, no
clinical language, no religious talk, nothing hate-adjacent or profane.
Handle the topic with care and warmth.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature emotional science: "
            "sadness as the archive's signal of lost value, the mind weighing "
            "what mattered, measuring the gap, and marking the record so the "
            "lesson is kept. Clearly labeled Signature-made, never presented "
            "as authentic public record.")

CIT_DARWIN = ("Darwin C. The Expression of the Emotions in Man and Animals. "
              "John Murray; 1872.")
CIT_EKMAN = ("Ekman P. Emotions Revealed: Recognizing Faces and Feelings to "
             "Improve Communication and Emotional Life. Times Books; 2003.")
CIT_PLUTCHIK = ("Plutchik R. The Emotions. Rev. ed. University Press of "
                "America; 1991.")
CIT_LAZARUS = ("Lazarus RS. Emotion and Adaptation. Oxford University Press; "
               "1991.")
CIT_IZARD = ("Izard CE. The Psychology of Emotions. Plenum Press; 1991.")
CIT_FRIJDA = ("Frijda NH. The Emotions. Cambridge University Press; 1986.")
CIT_PANKSEPP = ("Panksepp J. Affective Neuroscience: The Foundations of Human "
                "and Animal Emotions. Oxford University Press; 1998.")
CIT_BARRETT = ("Barrett LF. How Emotions Are Made: The Secret Life of the "
               "Brain. Houghton Mifflin Harcourt; 2017.")
CIT_BONANNO = ("Bonanno GA. The Other Side of Sadness: What the New Science "
               "of Bereavement Tells Us About Life After Loss. Basic Books; "
               "2009.")
CIT_GROSS = ("Gross JJ, editor. Handbook of Emotion Regulation. Guilford "
             "Press; 2007.")
CIT_KELTNER = ("Keltner D, Oatley K, Jenkins JM. Understanding Emotions. "
               "4th ed. Wiley; 2019.")
CIT_FREDRICKSON = ("Fredrickson BL. Positivity. Crown Publishers; 2009.")

ENTRIES = [
{
 "key": "emsad-what-is",
 "name": "What sadness is, in plain words",
 "group": "what-sadness-is",
 "ladder_rank": 1, "ladder_tier": "foundations",
 "description": ("Sadness is the heavy, low-energy feeling that arrives when "
  "something we valued is lost, broken, or out of reach. It is one of the "
  "handful of emotions every human culture recognizes, and it shows on the "
  "face in the same way across the world: the inner eyebrows lift, the "
  "corners of the mouth pull down, the gaze drops. Psychologists describe "
  "sadness as the emotion of loss and unmet need - it tells the person "
  "feeling it that something mattered and is now missing. Far from being a "
  "malfunction, sadness is part of the standard human equipment, and "
  "understanding it is the first step in this archive."),
 "how_it_works": ("Sadness begins with an appraisal: the mind registers that "
  "a valued person, goal, or state has been lost or blocked, and that the "
  "situation calls for withdrawal and reflection rather than action. The "
  "body answers by conserving energy - heart rate eases, breathing slows, "
  "muscles soften, and attention turns inward. The face broadcasts the "
  "signal to others, inviting comfort and support. In small doses this "
  "sequence helps people pause, take stock, and seek help; the feeling is "
  "designed to be noticed, felt, and then released as the situation is "
  "absorbed."),
 "key_points": [
  "Sadness is the emotion of loss - the signal that something valued is missing.",
  "It is a universal basic emotion, recognized across cultures by the same facial signs.",
  "The inner eyebrows rising and the mouth corners turning down are its signature marks.",
  "Sadness conserves energy and turns attention inward, inviting reflection and comfort.",
  "Feeling sad is normal human equipment, not a malfunction or a failure of character."],
 "requirements": [
  "An everyday vocabulary for feelings, kept plain and free of clinical labels.",
  "A willingness to treat sadness as information rather than as an enemy.",
  "The distinction between describing an emotion and diagnosing a person."],
 "standards": [
  "Ekman's basic-emotion framework: sadness as one of the universally recognized emotions.",
  "Darwin's principle of serviceable habits: the sad face as an evolved social signal."],
 "citations": [CIT_DARWIN, CIT_EKMAN, CIT_LAZARUS],
 "sig_lens": ("Through the Signature lens, sadness is the archive's signal "
  "of lost value: the mind weighing what mattered, measuring the gap left "
  "behind, and marking the record so the worth of what was lost is never "
  "forgotten. The Signature archivist files every loss under what it "
  "teaches, because a loss that is weighed becomes wisdom instead of "
  "weight."),
},
{
 "key": "emsad-family",
 "name": "Where sadness sits in the emotion family",
 "group": "what-sadness-is",
 "ladder_rank": 1, "ladder_tier": "foundations",
 "description": ("In the family tree of feelings, sadness is a primary "
  "emotion - one of the root feelings from which more complicated emotions "
  "grow. Plutchik's wheel places sadness opposite joy, paired most often "
  "with its neighbors: blended with surprise it becomes disappointment, "
  "with anger it becomes sulkiness or resentment, with fear it becomes "
  "despair, and with joy it becomes bittersweet nostalgia. Complex members "
  "of the family carry sadness inside them: grief is sadness stretched "
  "across the loss of a person, melancholy is sadness settled in for a "
  "long stay, and disappointment is sadness aimed at an unmet expectation. "
  "Knowing the family helps tell the relatives apart, which is the work of "
  "the later records in this archive."),
 "how_it_works": ("Emotion families are organized by what psychologists call "
  "appraisal patterns - the kind of judgment that sets each feeling off. "
  "Sadness belongs to the loss-and-helplessness branch: the mind judges "
  "that something good is gone and that pushing harder will not bring it "
  "back right now. When a second appraisal joins in - unfairness, danger, "
  "surprise - the blend takes on a new name and a new flavor, which is why "
  "sadness so often arrives with company. The family map in this record "
  "gives every later record a home address."),
 "key_points": [
  "Sadness is a primary emotion: a root feeling, not a blend.",
  "On Plutchik's wheel it sits opposite joy, the emotion of gain.",
  "Sadness plus surprise reads as disappointment; plus anger as resentment; plus fear as despair; plus joy as bittersweetness.",
  "Grief, melancholy, and disappointment are complex relatives built on a sadness core.",
  "The blend rule: a second appraisal (unfairness, danger, surprise) renames the feeling."],
 "requirements": [
  "Familiarity with the plain-words definition of sadness from the first record.",
  "The idea that emotions combine the way colors mix.",
  "No clinical labels - family membership is descriptive, not diagnostic."],
 "standards": [
  "Plutchik's wheel of emotions: sadness as a primary, with defined dyads.",
  "Lazarus's appraisal theory: loss appraisals define the sadness family."],
 "citations": [CIT_PLUTCHIK, CIT_LAZARUS, CIT_IZARD],
 "sig_lens": ("The Signature archivist shelves sadness at the root of the "
  "family tree, because every complex sorrow in the archive traces back to "
  "this one signal of lost value. The blends are filed as cross-references: "
  "follow the second appraisal and you find the relative. In Signature "
  "science the family tree is a map of messages, and sadness is the message "
  "that says: something precious was here."),
},
{
 "key": "emsad-volumes",
 "name": "Sadness at different volumes: mild, moderate, intense",
 "group": "what-sadness-is",
 "ladder_rank": 2, "ladder_tier": "foundations",
 "description": ("Sadness is one feeling with a volume knob. At mild "
  "intensity (about a 1 to 3 on a ten-point scale) it is a passing "
  "heaviness - the gray-afternoon feeling after a small letdown, gone by "
  "evening. At moderate intensity (about 4 to 7) it settles in: the "
  "shoulders drop, the appetite shifts, concentration thins, and the day "
  "takes on a slower rhythm. At high intensity (about 8 to 10) it becomes "
  "an all-consuming wave - tears come unbidden, the chest aches, and "
  "ordinary tasks feel far away. The emotion is the same at every level; "
  "only the volume changes, and with it the amount of care the feeling "
  "asks for. Learning to read the volume is the first skill of the "
  "archive's simulator."),
 "how_it_works": ("Intensity tracks how large the mind judges the loss to "
  "be and how central the lost thing was to the person's life. A small "
  "loss produces a small signal; a central loss produces a flood. The body "
  "scales its response in the same way: mild sadness barely moves the "
  "heart rate, while intense sadness can raise it, tighten the throat, and "
  "summon tears. The ten-point scale used across this archive is a teaching "
  "tool, not a medical instrument - it gives the simulator a common "
  "language for low, middle, and high volume."),
 "key_points": [
  "Mild sadness (1-3): a passing heaviness, gone within hours.",
  "Moderate sadness (4-7): settled-in, with posture, appetite, and focus effects.",
  "Intense sadness (8-10): an all-consuming wave with tears and chest ache.",
  "Intensity follows the judged size and centrality of the loss.",
  "The 1-10 scale is a teaching tool for the simulator, not a clinical measure."],
 "requirements": [
  "The plain-words definition and the family map from the earlier records.",
  "A ten-point intensity scale shared across the archive's simulators."],
 "standards": [
  "Dimensional models of emotion: valence and arousal scaling with judged loss.",
  "Educational intensity scaling for simulation, distinct from clinical rating scales."],
 "citations": [CIT_IZARD, CIT_FRIJDA, CIT_KELTNER],
 "sig_lens": ("Signature science reads volume as the size of the gap: a "
  "small gap hums, a wide gap roars. The archivist teaches that volume is "
  "information, not emergency - the louder the signal, the more the lost "
  "thing mattered, and the more carefully its lesson should be filed."),
},
{
 "key": "emsad-myths",
 "name": "Myths and misunderstandings about sadness",
 "group": "what-sadness-is",
 "ladder_rank": 2, "ladder_tier": "foundations",
 "description": ("Sadness collects myths the way attics collect dust. Myth "
  "one: sadness is always bad and should be switched off - in truth it is "
  "a normal signal, and silencing every signal leaves a person flying "
  "blind. Myth two: crying is weakness - in truth tears are a built-in "
  "social signal that calls in comfort, and people who cry when sad are "
  "using the equipment as designed. Myth three: feeling sad means something "
  "is wrong with you - in truth sadness visits healthy people after losses "
  "big and small. Myth four: you should cheer up immediately - in truth "
  "rushed cheerfulness usually buries the feeling, which then returns "
  "later with interest. Myth five: sad people cannot function - in truth "
  "mild and moderate sadness leave most abilities intact, only slowed. "
  "Clearing these myths makes room for the honest study that follows."),
 "how_it_works": ("Myths survive because they offer quick comfort: blame the "
  "feeling, demand a smile, move on. The science survives because it "
  "checks those stories against observation. Cross-cultural studies show "
  "sad expressions recognized on every continent; bereavement research "
  "shows sadness after loss in healthy adults; and emotion-regulation "
  "research shows that acknowledged feelings fade faster than suppressed "
  "ones. This record keeps the archive honest: every claim that follows "
  "has to survive contact with the evidence."),
 "key_points": [
  "Sadness is a normal signal, not a defect to be switched off.",
  "Crying is a designed social signal that calls in comfort.",
  "Healthy people feel sad after losses; sadness alone means nothing is wrong.",
  "Rushed cheerfulness buries the feeling; it returns later, heavier.",
  "Mild and moderate sadness slow function but rarely stop it."],
 "requirements": [
  "A myth-busting stance: test folk sayings against observation.",
  "Care with words: describing sadness is not diagnosing anyone."],
 "standards": [
  "Evidence standards for folk claims: cross-cultural and bereavement research.",
  "Emotion-regulation research on acknowledgment versus suppression."],
 "citations": [CIT_EKMAN, CIT_BONANNO, CIT_GROSS],
 "sig_lens": ("The Signature archivist files myths under hazards: a false "
  "map of sadness leads travelers to fight the signal instead of reading "
  "it. Signature science keeps one rule on the wall - the feeling is the "
  "message, never the enemy - and strikes every myth that contradicts it."),
},
{
 "key": "emsad-inside",
 "name": "Inside the feeling: a first-person passage",
 "group": "inside-the-feeling",
 "ladder_rank": 2, "ladder_tier": "foundations",
 "description": ("This record steps inside sadness and reports back in the "
  "first person, so the archive can simulate the feeling honestly. It is "
  "like this: the morning arrives a shade dimmer, as if someone turned the "
  "world's brightness down one notch while you slept. There is a weight "
  "low in the chest, not pain exactly, more like a hand resting there, "
  "reminding. Thoughts move slower and keep circling back to the same "
  "empty place, the way a tongue keeps finding the gap where a tooth used "
  "to be. Sounds are a little too loud and a little too far away at the "
  "same time. You catch yourself sighing - long, slow breaths the body "
  "takes on its own - and small kindnesses from others land strangely, "
  "both unwelcome and desperately wanted. Nothing is broken. Everything is "
  "just heavier, quieter, and grayer, and you understand, without anyone "
  "explaining, that something you cared about is gone."),
 "how_it_works": ("First-person simulation works by translating the known "
  "components of sadness - low energy, inward attention, slowed thought, "
  "the chest heaviness, sighing, sensitivity to kindness - into lived "
  "language. Writers, actors, and counselors have used this method for "
  "generations to build empathy without claiming to read any real person's "
  "mind. The passage above is a composite sketch drawn from the research "
  "literature, not a report about any individual. Its purpose is "
  "educational: to give the reader an inside view that makes the outside "
  "signs, covered in later records, easier to recognize and understand."),
 "key_points": [
  "The world seems dimmer; brightness itself feels turned down.",
  "A weight rests low in the chest; thoughts circle the empty place.",
  "Thinking slows; sighs come on their own; kindness feels both unwelcome and wanted.",
  "The passage is a composite sketch for learning, not a report on any real person.",
  "First-person simulation builds empathy without claiming to read minds."],
 "requirements": [
  "Read as a simulation: an inside view for study, not a diagnosis of anyone.",
  "A gentle pace - this record is meant to be felt slowly, not skimmed."],
 "standards": [
  "Phenomenological description standards: report the lived quality of the feeling.",
  "Composite-sketch ethics: educational simulation, never a claim about a real person."],
 "citations": [CIT_IZARD, CIT_BARRETT, CIT_FRIJDA],
 "sig_lens": ("The Signature simulator enters the feeling the way an "
  "archivist enters a vault: quietly, respectfully, and only to catalog "
  "what is there. Inside, sadness reads as a ledger being balanced - every "
  "heavy thought a line item, every sigh a page turning, until the account "
  "of what was lost is finally, carefully closed."),
},
{
 "key": "emsad-timeline",
 "name": "How sadness moves through time: onset, peak, fading, aftershock",
 "group": "inside-the-feeling",
 "ladder_rank": 3, "ladder_tier": "foundations",
 "description": ("Sadness has a shape in time, and knowing the shape helps "
  "people ride it out. Onset arrives over minutes: at a moderate intensity "
  "of 7, the first eight minutes bring the sinking recognition, the "
  "throat tightening, the eyes stinging. The peak follows at around "
  "twenty-five minutes - the heaviest point, when tears are most likely "
  "and the chest feels fullest. Then comes the long fade, with a half-life "
  "near forty minutes: each forty-minute stretch roughly halves what "
  "remains, so the feeling thins gradually rather than switching off. "
  "Finally the aftershock: a smaller echo, about fifteen minutes of "
  "renewed heaviness, that can return hours later when a reminder appears. "
  "These are teaching numbers for the simulator, and real episodes vary - "
  "but the four-phase shape holds remarkably steady across people."),
 "how_it_works": ("The timeline mirrors how the mind processes loss. Onset "
  "is the appraisal landing - the moment the loss is fully registered. The "
  "peak is the body's full mobilization: the signal broadcast at maximum "
  "strength to recruit comfort and support. The fade is regulation at work: "
  "breathing steadies, attention widens, the mind begins filing the event "
  "away. The aftershock is memory doing its job: reminders reactivate a "
  "fainter copy of the feeling so the lesson is not lost. Understanding "
  "the phases turns a frightening wave into a known coastline."),
 "key_points": [
  "Onset (about 8 minutes at intensity 7): recognition, throat tightens, eyes sting.",
  "Peak (about 25 minutes): the heaviest point, tears most likely.",
  "Fade (half-life about 40 minutes): the feeling thins gradually, not all at once.",
  "Aftershock (about 15 minutes): a fainter echo when reminders appear later.",
  "The four-phase shape is steady across people; the exact minutes are teaching numbers."],
 "requirements": [
  "The 1-10 intensity scale from the volume record.",
  "Patience with the fade: feelings thin on their own schedule."],
 "standards": [
  "Emotion-episode research: onset, peak, and recovery phases in affective events.",
  "Bereavement research on waves of grief and reminder-triggered echoes."],
 "citations": [CIT_FRIJDA, CIT_BONANNO, CIT_LAZARUS],
 "sig_lens": ("Signature science charts the timeline like a tide table: "
  "the wave always comes, always crests, always withdraws. The archivist "
  "teaches travelers to check the phase before judging the sea - at the "
  "peak everything looks permanent, and at the aftershock everything looks "
  "finished, and both readings are wrong in useful ways."),
},
{
 "key": "emsad-low-high",
 "name": "Low sadness versus high sadness: two lived snapshots",
 "group": "inside-the-feeling",
 "ladder_rank": 3, "ladder_tier": "foundations",
 "description": ("At intensity 2, sadness is a background tint. The heart "
  "beats only about four beats per minute above its resting pace, breathing "
  "stays easy near thirteen breaths a minute, tears are unlikely, and "
  "speech flows at a near-normal one hundred thirty-six words per minute - "
  "a person can work, joke, and almost forget the gray edge on the day. At "
  "intensity 9, the same emotion is a different country: the heart runs "
  "about eighteen beats fast, breathing shallows near eleven slow breaths "
  "a minute, tears come with a probability near certainty, and speech "
  "slows to about eighty-seven words per minute with long pauses between "
  "sentences. The two snapshots are the same feeling at different volumes, "
  "and the simulator uses both so learners can calibrate their eyes and "
  "ears to the whole range."),
 "how_it_works": ("The snapshots are built from the archive's scaling "
  "rules: heart-rate lift rises about two beats per intensity point, "
  "breathing eases down about a third of a breath per point, tear "
  "probability climbs steeply past intensity 6, and speech rate falls about "
  "seven words per minute per point from a baseline near one hundred "
  "fifty. These are smooth, teachable curves drawn from the direction of "
  "the research - low sadness barely moves the body, high sadness moves "
  "everything. Real people vary around the curves, which is the subject of "
  "a later record."),
 "key_points": [
  "Intensity 2: heart +4 bpm, easy breathing, tears unlikely, speech near normal.",
  "Intensity 9: heart +18 bpm, shallow slow breathing, tears near certain, halting speech.",
  "Heart lift scales about two beats per intensity point; speech falls about seven words per minute per point.",
  "Tear probability climbs steeply past intensity 6.",
  "Same emotion, different volume: calibration across the range is the skill."],
 "requirements": [
  "The volume bands and the 1-10 scale.",
  "Comfort with approximate teaching numbers rather than medical measurements."],
 "standards": [
  "Psychophysiology of sadness: modest cardiac and respiratory shifts with intensity.",
  "Speech-rate research: slowed verbal output under low mood."],
 "citations": [CIT_PANKSEPP, CIT_IZARD, CIT_KELTNER],
 "sig_lens": ("The Signature calibrator keeps both snapshots on one card: "
  "the tint and the flood. Apprentices learn to read the dial before "
  "reading the person, because the same heart can carry both, and wisdom "
  "is knowing which volume is playing before deciding what the music "
  "means."),
},
{
 "key": "emsad-mix-lonely",
 "name": "Sadness mixed with loneliness, its closest partner",
 "group": "inside-the-feeling",
 "ladder_rank": 3, "ladder_tier": "foundations",
 "description": ("Sadness rarely travels alone, and its most faithful "
  "companion is loneliness. Pure sadness says: something valued is gone. "
  "Loneliness adds: and no one is here with me in the gap. The blend feels "
  "heavier than either alone - the chest weight of sadness joined by the "
  "hollow, echoing quality of loneliness, like an empty room inside the "
  "ribs. In the archive's blend model, a sadness of intensity 7 mixed with "
  "loneliness at 6 produces a combined ache near 6.5, weighted toward "
  "whichever feeling runs hotter. The blend also changes behavior: pure "
  "sadness may still accept comfort, while the lonely blend tends to turn "
  "comfort away, convinced no one could understand. Recognizing the partner "
  "is often the key to helping, because the two halves answer to different "
  "remedies: sadness wants the loss honored, loneliness wants company."),
 "how_it_works": ("Blends form when two appraisals fire at once - loss plus "
  "social disconnection. The simulator models the blend as a weighted "
  "average of the two intensities, with the weights set by which feeling "
  "dominates attention. This matches the lived report that the mixture has "
  "its own texture, distinct from each ingredient. The practical payoff is "
  "diagnostic in the everyday sense: when comfort is refused, check for "
  "the loneliness half, because reassurance about the loss will not reach "
  "a person whose real complaint is being alone with it."),
 "key_points": [
  "Loneliness is sadness's most common partner: loss plus disconnection.",
  "The blend feels heavier than either alone, with a hollow, echoing quality.",
  "Blend intensity follows a weighted average of the two feelings.",
  "The lonely blend tends to refuse comfort; pure sadness may accept it.",
  "Different halves, different remedies: honor the loss, and offer company."],
 "requirements": [
  "The family map: how blends form from two appraisals at once.",
  "Care: describing a blend is not labeling any real person."],
 "standards": [
  "Plutchik's dyad logic: neighboring primaries blend into named mixtures.",
  "Loneliness research: perceived social disconnection as distinct from objective isolation."],
 "citations": [CIT_PLUTCHIK, CIT_LAZARUS, CIT_KELTNER],
 "sig_lens": ("Signature science files the blend under compound signals: "
  "two messages arriving on one wire. The archivist teaches apprentices to "
  "separate the wires before answering - honor the loss on the sadness "
  "wire, and send company down the loneliness wire, because a blended "
  "signal answered with half a remedy stays noisy."),
},
{
 "key": "emsad-day",
 "name": "Sadness through an ordinary day: a vignette",
 "group": "inside-the-feeling",
 "ladder_rank": 4, "ladder_tier": "foundations",
 "description": ("Seven in the morning: the alarm sounds and sadness is "
  "already there at a 5, waiting in the heaviness of getting up. By nine, "
  "work has pulled attention outward and the level eases to 3 - the "
  "background tint from the earlier snapshot. Lunch at noon brings a "
  "reminder, a song from better days, and the needle jumps to 6; the food "
  "tastes like cardboard for ten minutes. The afternoon drifts at 4, "
  "punctuated by sighs nobody notices. Six in the evening is the day's "
  "peak at 7: home, quiet rooms, the empty chair, the full weight of it. "
  "By ten the fade has done its work and the level rests at 3 again, "
  "tired more than sad. The day averages near 4.3 - a moderate day, "
  "entirely survivable, with the evening peak exactly where the research "
  "says to expect it: when the distractions end and the mind is left "
  "alone with the ledger."),
 "how_it_works": ("The vignette demonstrates the interaction of the "
  "timeline, the volume scale, and daily rhythm. Distraction lowers felt "
  "intensity by occupying attention; reminders spike it by reactivating "
  "the loss appraisal; evenings raise it because the day's scaffolding of "
  "tasks falls away. The simulator generates such days by combining a "
  "baseline intensity with scheduled events - reminders, quiet hours, "
  "social contact - each nudging the level up or down. Learners who walk "
  "through the day internalize the most useful fact in the archive: "
  "sadness is weather, and weather passes."),
 "key_points": [
  "Morning starts near 5; work distraction eases it to 3 by nine.",
  "A midday reminder spikes it to 6; the evening quiet peaks it at 7.",
  "Night fade brings it back to 3; the day averages near 4.3.",
  "Distraction lowers felt intensity; reminders and quiet hours raise it.",
  "The lesson: sadness is weather, and weather passes."],
 "requirements": [
  "The volume scale, the timeline phases, and the low-versus-high snapshots.",
  "Read as one person's imagined day - a simulation, not a case report."],
 "standards": [
  "Daily-diary emotion research: within-day fluctuation of negative affect.",
  "Attention and appraisal interaction in felt intensity."],
 "citations": [CIT_FRIJDA, CIT_BARRETT, CIT_BONANNO],
 "sig_lens": ("The Signature daybook records the weather hour by hour, "
  "because the archivist trusts patterns over moments. A single peak does "
  "not define the day; the average does. Travelers learn to read their own "
  "forecast - when the evening rise is due - and to schedule kindness for "
  "the hours that need it."),
},
{
 "key": "emsad-body",
 "name": "What sadness does in the body",
 "group": "body-signals",
 "ladder_rank": 4, "ladder_tier": "foundations",
 "description": ("Sadness writes itself across the body in a consistent "
  "script. The heart lifts modestly - about two extra beats per minute for "
  "each point of intensity, so a sadness of 6 runs roughly twelve beats "
  "above rest. Breathing slows and shallows, easing down about a third of "
  "a breath per minute per intensity point from a resting fourteen, as the "
  "body conserves energy. Muscles soften rather than tense: the shoulders "
  "round, the jaw unclenches, the whole frame seems to settle downward. "
  "The stomach often joins in with a hollow or queasy feeling, appetite "
  "dulling as the gut mirrors the low mood. Skin may pale slightly as "
  "blood flow eases, and the eyes water as tear glands prime. Energy "
  "drains in proportion to the feeling - at intensity 6 the body reports "
  "itself at about half its normal charge. None of this is damage; it is "
  "the body budgeting power for reflection instead of action."),
 "how_it_works": ("The pattern reflects the parasympathetic branch of the "
  "nervous system taking the lead: rest, digest, and withdraw rather than "
  "fight or flee. Low arousal is the physiological signature of sadness, "
  "the opposite of the racing heart of fear or anger. The simulator "
  "computes each channel from intensity with simple scaling rules - heart "
  "lift, breath easing, muscle softening, stomach unease, pallor, tear "
  "readiness, energy drain - and combines them into a body-load index that "
  "learners can read at a glance. The index is a teaching gauge, not a "
  "medical device, and every channel varies between people, as the next "
  "records explain."),
 "key_points": [
  "Heart lifts about two beats per minute per intensity point.",
  "Breathing slows and shallows; muscles soften rather than tense.",
  "Stomach hollows, appetite dulls, skin may pale, eyes water.",
  "Energy drains in proportion: at intensity 6 the body reports about half charge.",
  "The pattern is parasympathetic: rest and withdraw, the opposite of fight or flight."],
 "requirements": [
  "The 1-10 scale and the low-versus-high snapshots.",
  "Read body signs as information, never as a diagnosis of anyone."],
 "standards": [
  "Psychophysiology of sadness: low-arousal autonomic pattern.",
  "Parasympathetic dominance in loss-related affect."],
 "citations": [CIT_PANKSEPP, CIT_IZARD, CIT_KELTNER],
 "sig_lens": ("The Signature physician reads the body as an instrument "
  "panel: seven gauges, one story. When the needles swing low together, "
  "the system is not broken - it is in harbor mode, sails furled, riding "
  "out weather. The archivist logs the readings without alarm, because a "
  "harbor is not a wreck."),
},
{
 "key": "emsad-posture",
 "name": "The posture and movement of sadness",
 "group": "body-signals",
 "ladder_rank": 4, "ladder_tier": "foundations",
 "description": ("A sad body is readable from across the room. The head "
  "tips forward - about eight degrees plus two more for each point of "
  "intensity, so at intensity 6 the chin drops roughly twenty degrees. The "
  "shoulders round inward and the chest narrows, as if protecting "
  "something. The walk changes: stride shortens by about three percent per "
  "intensity point, so at 6 the step is roughly four-fifths of its normal "
  "length, and the pace slows with it. Gestures shrink - hands stay close, "
  "movements stay small, and the body touches itself more: arms crossed, "
  "hands clasped, a self-hug against the cold of the feeling. The whole "
  "posture says what the face says: energy conserved, attention inward, "
  "please approach gently. Actors learn this posture first because the "
  "audience reads it before a single word is spoken."),
 "how_it_works": ("Posture is the body's cheapest broadcast: it costs "
  "nothing and carries far. The forward head and rounded shoulders reduce "
  "the body's profile and protect the vulnerable front; the shortened "
  "stride and slowed pace match the lowered energy budget; self-touch "
  "soothes through pressure and warmth. The simulator renders posture from "
  "intensity with the scaling rules above - head angle, stride factor, "
  "gesture size - so learners can see the signature take shape as the "
  "volume rises. Like all body channels, the exact numbers vary by person, "
  "but the direction is the same everywhere."),
 "key_points": [
  "Head tips forward about eight degrees plus two per intensity point.",
  "Shoulders round, chest narrows; the body protects its front.",
  "Stride shortens about three percent per point; pace slows with it.",
  "Gestures shrink; self-touch increases: crossed arms, clasped hands.",
  "The posture broadcasts before words do: energy low, approach gently."],
 "requirements": [
  "The body-channels record: posture as one channel of the same signal.",
  "Observation at a distance: posture carries across a room."],
 "standards": [
  "Nonverbal communication research: postural correlates of dejection.",
  "Darwin's principle of antithesis: sad posture as the opposite of expansive pride."],
 "citations": [CIT_DARWIN, CIT_EKMAN, CIT_KELTNER],
 "sig_lens": ("Signature science calls the sad posture the furled sail: "
  "every line of the body drawn inward to weather the gale with minimum "
  "exposure. The archivist sketches it in three strokes - head down, "
  "shoulders round, stride short - and teaches that a furled sail is not "
  "a surrendered ship."),
},
{
 "key": "emsad-sleep",
 "name": "Sleep, appetite, and energy under sadness",
 "group": "body-signals",
 "ladder_rank": 4, "ladder_tier": "foundations",
 "description": ("Sadness rearranges the body's housekeeping. Sleep "
  "usually suffers first: falling asleep takes longer as the mind replays "
  "the loss, and the simulator budgets about fifteen lost minutes per "
  "intensity point - at intensity 6, roughly an hour and a half of sleep "
  "goes missing. Appetite typically dulls: food tastes flat, portions "
  "shrink, and the stomach's hollow feeling masquerades as fullness, "
  "though some people swing the other way and seek comfort in eating. "
  "Energy follows the drain curve - at intensity 6 the day's charge reads "
  "about half, and tasks that normally take an hour take ninety minutes. "
  "These are the slowest channels to recover: even after the feeling "
  "lifts, sleep and appetite may need several days to find their rhythm "
  "again. The record's guidance is gentle and general: keep regular hours, "
  "eat small steady meals, and let the housekeeping catch up on its own "
  "schedule."),
 "how_it_works": ("The same low-arousal shift that slows the heart also "
  "flattens the rhythms of sleep and hunger. Rumination - the mind "
  "circling the loss - competes with sleep onset; the gut's mirroring of "
  "low mood dulls hunger signals; the conserved energy budget makes every "
  "task cost more. The simulator models sleep loss, appetite change, and "
  "energy level as lagging indicators: they rise slower than the feeling "
  "and fall slower too, which is why a person can feel better emotionally "
  "while still sleeping badly for a few nights. This lag is normal and "
  "expected, not a sign of anything deeper."),
 "key_points": [
  "Sleep loss runs about fifteen minutes per intensity point; at 6, roughly ninety minutes.",
  "Appetite usually dulls; a minority swing toward comfort eating.",
  "Energy reads about half at intensity 6; tasks take roughly half as long again.",
  "Sleep, appetite, and energy are lagging indicators: they recover slower than the mood.",
  "General guidance: regular hours, small steady meals, patience with the lag."],
 "requirements": [
  "The body-channels record: sleep and appetite as downstream channels.",
  "The timeline record: why recovery lags behind the feeling."],
 "standards": [
  "Sleep and affect research: rumination effects on sleep onset.",
  "Appetite and mood literature: hedonic dulling under low affect."],
 "citations": [CIT_PANKSEPP, CIT_FRIJDA, CIT_KELTNER],
 "sig_lens": ("The Signature housekeeper tends the slow rooms last: "
  "sleep, appetite, and energy are the deep cellars of the system, and "
  "they flood last and drain last. The archivist's standing order is "
  "patience with the cellars - mop the surface feelings first, and give "
  "the deep rooms their own unhurried week."),
},
{
 "key": "emsad-differences",
 "name": "No two bodies feel it the same way",
 "group": "body-signals",
 "ladder_rank": 5, "ladder_tier": "foundations",
 "description": ("The archive's scaling rules describe the average body, "
  "but nobody is the average body. One person at intensity 6 cries freely "
  "while another at the same intensity feels only the chest weight - the "
  "tear channel runs hot in the first and cool in the second. One person's "
  "stomach rebels while another's sleeps through the whole episode "
  "untroubled. Sensitivity itself varies: some nervous systems amplify "
  "every signal, others mute them, so the same loss can read as a 4 in one "
  "body and a 7 in another. Age, fatigue, hunger, illness, and even the "
  "weather shift the gauges. The simulator handles this with person "
  "profiles - six sample temperaments whose channel sensitivities differ - "
  "and the spread between them is the point: there is no single correct "
  "way for a body to be sad, and nobody's quieter or louder grief is "
  "wrong."),
 "how_it_works": ("Individual difference comes from three sources: "
  "trait sensitivity (how strongly a nervous system responds to anything), "
  "channel tuning (which body systems speak loudest - tears, gut, muscles, "
  "fatigue), and state (how tired, hungry, or ill the person already is). "
  "The simulator multiplies the base channel values by each profile's "
  "sensitivity coefficients, producing six different bodies at the same "
  "intensity. Learners compare the profiles to absorb the archive's "
  "deepest body lesson: judge the feeling by its direction and its story, "
  "never by how loudly or quietly the body performs it."),
 "key_points": [
  "Tear, gut, muscle, and fatigue channels run hot or cool by person.",
  "Trait sensitivity shifts the whole scale: the same loss reads 4 in one body, 7 in another.",
  "State matters: fatigue, hunger, and illness amplify every channel.",
  "The simulator's six profiles show the spread at a single intensity.",
  "No single correct way to embody sadness; quiet is not wrong, loud is not wrong."],
 "requirements": [
  "All three body records: the channels whose tuning varies.",
  "A non-judgmental stance toward different expressions of the same feeling."],
 "standards": [
  "Individual-differences research in affective responding.",
  "Trait affectivity and state modulation of emotion physiology."],
 "citations": [CIT_IZARD, CIT_BARRETT, CIT_PANKSEPP],
 "sig_lens": ("The Signature instrument maker calibrates every gauge to "
  "its own owner: no two panels read alike, and the archivist forbids "
  "comparing dials across ships. What matters is each traveler's own "
  "baseline - the change from their normal - because a quiet instrument "
  "can carry a loud sea."),
},
{
 "key": "emsad-face",
 "name": "Reading the sad face: eyes, brows, mouth",
 "group": "the-sad-face",
 "ladder_rank": 5, "ladder_tier": "compounded",
 "description": ("The sad face is one of the most reliably recognized "
  "signals in human life, and it is built from four moving parts. The "
  "inner eyebrows lift and draw together - the single most diagnostic "
  "mark, almost impossible to produce voluntarily without feeling "
  "something. The upper eyelids droop, narrowing the eyes and giving the "
  "gaze its downward cast. The corners of the mouth pull down and the "
  "lower lip may push up slightly, lengthening the face into its mournful "
  "shape. And the gaze itself drops: sad eyes look down and away, breaking "
  "the social contact that other emotions seek. The simulator scores each "
  "part from intensity - inner brow lift at about twelve percent of full "
  "scale per point, lip-corner depression at eleven, lid droop at eight, "
  "gaze lowering at nine - and at intensity 6 the four parts sum to a "
  "clear, unmistakable reading of 2.4 on the expression scale."),
 "how_it_works": ("Facial-expression science codes the face into action "
  "units - single muscle movements with numbers. Sadness is action unit 1 "
  "(inner brow raise) plus action unit 4 (brow lower and draw together) "
  "plus action unit 15 (lip corner depressor), often with 64 (eyes down). "
  "The inner-brow combination is the tell: few people can fire those "
  "muscles on command, which is why the sad brow is trusted as genuine. "
  "The simulator converts intensity into action-unit strengths with the "
  "scaling rules above, giving learners a numeric feel for how the face "
  "assembles the signal piece by piece."),
 "key_points": [
  "Inner eyebrows lift and draw together: the most diagnostic mark, hard to fake.",
  "Upper lids droop; the gaze drops down and away.",
  "Mouth corners pull down; the lower lip may push up.",
  "Simulator scaling per intensity point: brow 0.12, lip corners 0.11, lids 0.08, gaze 0.09.",
  "At intensity 6 the four parts sum to 2.4: a clear, unmistakable reading."],
 "requirements": [
  "The body records: the face as the fastest broadcast channel.",
  "Action-unit vocabulary: inner brow, lip corners, lids, gaze."],
 "standards": [
  "Facial Action Coding System: AU 1+4+15 (+64) as the sadness configuration.",
  "Ekman's universality findings for the sad brow across cultures."],
 "citations": [CIT_EKMAN, CIT_DARWIN, CIT_IZARD],
 "sig_lens": ("The Signature portraitist paints the sad face in four "
  "brushstrokes and signs it with the brow: that inner lift is the "
  "archive's watermark of genuine feeling, counterfeited by almost no "
  "one. Apprentices learn the four strokes in order - brow, lids, mouth, "
  "gaze - until they can read the portrait at a glance."),
},
{
 "key": "emsad-face-intensity",
 "name": "How the sad face changes with intensity",
 "group": "the-sad-face",
 "ladder_rank": 5, "ladder_tier": "compounded",
 "description": ("Turn the volume knob and watch the face follow. At "
  "intensity 2 the signs are whispers: the inner brow lifts a fraction, "
  "the mouth corners dip barely, and most observers would call the face "
  "neutral - the simulator scores the parts at brow 0.24, lip corners "
  "0.22, lids 0.16, gaze 0.18. At intensity 5 the signal is conversational: "
  "brow 0.60, lip corners 0.55, lids 0.40, gaze 0.45 - anyone looking sees "
  "that something is wrong. At intensity 9 the face is fully mobilized: "
  "brow 1.08, lip corners 0.99, lids 0.72, gaze 0.81, and tears join the "
  "display as the eyes glisten and spill. Every part rises monotonically - "
  "no part ever decreases as intensity climbs - which is what makes the "
  "face such a trustworthy gauge: unlike words, the muscles cannot easily "
  "report a lower number than the feeling."),
 "how_it_works": ("The monotonic rise follows the scaling rules "
  "established in the previous record, applied at three sample "
  "intensities. The simulator's lesson is calibration: learners match "
  "observed faces to the three reference levels until their estimates "
  "land within a point. The key insight is the floor effect at low "
  "intensity - mild sadness is genuinely hard to see, which is why the "
  "archive teaches the body and behavior channels alongside the face. A "
  "face that looks neutral can still belong to a sadness of 3; the "
  "absence of signal is not the signal of absence."),
 "key_points": [
  "Intensity 2: whispers - most observers read the face as neutral.",
  "Intensity 5: conversational - anyone looking sees something is wrong.",
  "Intensity 9: fully mobilized, tears joining the display.",
  "Every facial part rises monotonically with intensity; none ever decreases.",
  "Mild sadness is genuinely hard to see: absence of signal is not signal of absence."],
 "requirements": [
  "The four-part sad face and its per-point scaling rules.",
  "The volume bands: matching faces to mild, moderate, and intense."],
 "standards": [
  "Intensity coding in facial expression research.",
  "Floor effects in low-intensity expression recognition."],
 "citations": [CIT_EKMAN, CIT_IZARD, CIT_KELTNER],
 "sig_lens": ("The Signature gauge maker engraves three reference marks "
  "on the dial - whisper, conversation, flood - and every apprentice "
  "learns to read between them. The gauge never lies downward: the face "
  "may understate a quiet sadness, but it will not invent one, and that "
  "one-way honesty is why the archive trusts it."),
},
{
 "key": "emsad-hide",
 "name": "Hiding sadness: the masked face and what leaks",
 "group": "the-sad-face",
 "ladder_rank": 6, "ladder_tier": "compounded",
 "description": ("People hide sadness constantly - at work, in public, in "
  "front of children - and the mask has its own anatomy. The usual cover "
  "is a pressed smile: the mouth corners pulled sideways and slightly up "
  "by effort, the eyes held deliberately bright, the voice kept level. "
  "But the simulator's leakage rule is unforgiving: leakage equals "
  "intensity squared divided by effort plus one, times one tenth. At "
  "intensity 9 with a concealment effort of 8, leakage scores 0.90 - the "
  "mask is failing. What leaks first is the brow: the inner lift flashes "
  "for a fraction of a second before the smile locks in, a micro-expression "
  "the mask cannot catch. Next the voice: it thins at the ends of "
  "sentences. Then the body: the shoulders stay rounded no matter how "
  "bright the smile. The lesson is not that hiding is wrong - sometimes "
  "privacy is exactly right - but that the feeling keeps a vote, and "
  "strong feelings outvote strong masks."),
 "how_it_works": ("Concealment is effortful control layered over automatic "
  "expression, and automatic processes are faster: the genuine brow flash "
  "fires in under a fifth of a second, before deliberate control arrives. "
  "The leakage formula captures the losing battle - leakage grows with "
  "the square of intensity but only falls linearly with effort, so "
  "doubling the feeling needs four times the effort to contain. The "
  "simulator lets learners set intensity and effort and watch the mask "
  "hold or fail, building an honest understanding of why suppressed "
  "sadness so often shows anyway, and why the kindest response to a "
  "failing mask is gentle acknowledgment rather than exposure."),
 "key_points": [
  "The standard mask: pressed smile, brightened eyes, leveled voice.",
  "Leakage = intensity squared / (effort + 1) x 0.1; at 9 with effort 8, leakage is 0.90.",
  "The brow leaks first: a micro-flash before the smile locks in.",
  "The voice thins at sentence ends; the shoulders stay rounded.",
  "Strong feelings outvote strong masks; hiding is sometimes right, but rarely complete."],
 "requirements": [
  "The four-part sad face: knowing what the mask must cover.",
  "The volume scale: leakage grows with the square of intensity."],
 "standards": [
  "Micro-expression research: brief genuine flashes under suppression.",
  "Emotion-suppression literature: costs and leakage of concealment."],
 "citations": [CIT_EKMAN, CIT_GROSS, CIT_DARWIN],
 "sig_lens": ("The Signature mask maker is honest about the craft: every "
  "mask leaks, and the leak is priced by the square of the feeling. The "
  "archivist teaches apprentices to read the leak with kindness - not to "
  "strip the mask, but to know when to offer the quiet room where the "
  "mask can come off by choice."),
},
{
 "key": "emsad-artist",
 "name": "Drawing sadness: notes for artists and actors",
 "group": "the-sad-face",
 "ladder_rank": 6, "ladder_tier": "compounded",
 "description": ("To draw or play sadness at intensity 6, start with the "
  "brow: angle the inner ends upward about twenty degrees - the simulator "
  "computes eight degrees plus two per intensity point, giving twenty at "
  "6 - while the outer ends stay level, forming the inverted-V that reads "
  "instantly as sorrow. Drop the upper lids to cover the top eighth of "
  "the iris and aim the pupils down and slightly away. Pull the mouth "
  "corners down about six millimeters on a life-size face and let the "
  "lower lip push up a touch, deepening the chin crease. Tilt the whole "
  "head forward twenty degrees, round the shoulders, and let the arms hang "
  "or fold. For the actor: slow every movement by a third, soften the "
  "voice, let sentences trail, and sigh once without forcing it. The "
  "composite reads as genuine because it follows the muscles, not the "
  "idea of sadness - draw the anatomy and the emotion arrives on its own."),
 "how_it_works": ("The notes translate the action-unit scaling rules into "
  "studio instructions: brow angle from the inner-lift rule, lid coverage "
  "from the droop rule, mouth-corner drop from the depressor rule, head "
  "tilt from the posture rule. Artists and actors have used this "
  "outside-in method for centuries - build the body and the feeling "
  "follows - and the simulator generates the measurements so every "
  "drawing or performance starts from the same anatomy. The record exists "
  "because the archive serves makers as well as learners: a database that "
  "can describe a feeling should be able to help someone portray it."),
 "key_points": [
  "Brow: inner ends up about twenty degrees at intensity 6, outer ends level.",
  "Lids cover the top eighth of the iris; pupils aim down and away.",
  "Mouth corners drop about six millimeters life-size; chin crease deepens.",
  "Head tilts forward twenty degrees; shoulders round; movement slows by a third.",
  "Build the anatomy and the emotion arrives: draw the muscles, not the idea."],
 "requirements": [
  "The four-part face and the posture record: the full measurement set.",
  "A maker's stance: the archive serves artists and actors too."],
 "standards": [
  "Anatomical illustration standards for expressive faces.",
  "Outside-in acting method: physical score preceding felt emotion."],
 "citations": [CIT_DARWIN, CIT_EKMAN, CIT_IZARD],
 "sig_lens": ("The Signature draftsman keeps a single sheet pinned above "
  "the desk: the sad face in four measurements, no more. Apprentices copy "
  "it until the hand knows what the eye already does - that sorrow is "
  "geometry before it is story, and the geometry, drawn true, tells the "
  "story by itself."),
},
{
 "key": "emsad-triggers",
 "name": "The classic triggers of sadness",
 "group": "triggers",
 "ladder_rank": 6, "ladder_tier": "compounded",
 "description": ("Certain events trigger sadness so reliably that the "
  "archive files them as classics. The death of a loved one stands at the "
  "top with a potency near 10 - the defining loss against which all "
  "others are measured. The end of a close relationship follows near 9; "
  "serious illness or injury of self or loved ones near 8; the loss of a "
  "home, job, or life's work near 7. Below them run the everyday "
  "triggers: rejection and exclusion near 6, failure at something that "
  "mattered near 5, and being forgotten or overlooked near 4. Potency "
  "scores are the simulator's teaching weights, not universal constants - "
  "a job loss can outrank a breakup for the person whose identity lives "
  "in their work. But the pattern holds: the closer the lost thing sat to "
  "the center of a life, the harder the trigger pulls."),
 "how_it_works": ("Triggers work through the appraisal mechanism: the mind "
  "weighs the lost thing's centrality and permanence, and the resulting "
  "sadness scales with the product. Death scores highest because the loss "
  "is judged total and permanent; rejection stings because belonging is "
  "central to human life; failure saddens in proportion to how much of "
  "the self was invested in the goal. The simulator ranks triggers by "
  "potency and lets learners combine them - two mid-level triggers "
  "landing together can out-pull a single classic, which is why bad days "
  "compound. Knowing the classics helps learners predict the weather "
  "instead of being surprised by it."),
 "key_points": [
  "Death of a loved one: potency near 10, the defining loss.",
  "Relationship end near 9; serious illness or injury near 8; home, job, or life's work near 7.",
  "Rejection near 6; meaningful failure near 5; being overlooked near 4.",
  "Potency follows the lost thing's centrality and permanence.",
  "Two mid-level triggers together can out-pull a single classic."],
 "requirements": [
  "The appraisal idea: sadness scales with judged centrality and permanence of loss.",
  "The volume scale: potency scores map onto the 1-10 intensity range."],
 "standards": [
  "Life-events research: ranking of loss events by reported distress.",
  "Appraisal theory: centrality and permanence as intensity drivers."],
 "citations": [CIT_LAZARUS, CIT_BONANNO, CIT_FRIJDA],
 "sig_lens": ("The Signature cartographer maps the classic triggers as "
  "the deep channels where the tide always runs strongest. Apprentices "
  "memorize the soundings - 10, 9, 8, 7 - not to fear the water but to "
  "navigate it: a known channel can be sailed, even in the dark, while an "
  "uncharted one cannot."),
},
{
 "key": "emsad-personal",
 "name": "Personal triggers: memories and anniversaries",
 "group": "triggers",
 "ladder_rank": 6, "ladder_tier": "compounded",
 "description": ("Beyond the classics, every person carries a private "
  "atlas of triggers: the song that was playing, the restaurant where the "
  "news came, the date on the calendar. Anniversaries are the most "
  "predictable - the simulator models their potency as the original "
  "strength decaying exponentially with time, potency equal to base times "
  "e to the minus years over two and a half. A loss with base potency 9 "
  "still strikes at about 6.0 one year on, near 2.7 at three years, and a "
  "faint 0.2 at ten - the curve every bereaved person recognizes, sharp "
  "early and gentle late. Memory triggers are less predictable: a smell, "
  "a street corner, a stranger's laugh can detonate a full wave years "
  "after the loss, because the mind files losses with their sensory "
  "wrappers attached. The archive's counsel is practical: map your own "
  "atlas, note the dates, and treat ambushes as weather - fierce, brief, "
  "and gone."),
 "how_it_works": ("Personal triggers work through associative memory: the "
  "loss is stored linked to its context, and any piece of the context can "
  "reactivate the whole appraisal. The exponential decay of anniversary "
  "potency matches the observed course of bereavement - intense early "
  "waves that thin over years, with the time constant near two and a half "
  "years as a teaching value. The simulator plots the decay curve and "
  "sprinkles random sensory reminders across the years, showing learners "
  "why grief is episodic rather than linear. Understanding the mechanism "
  "turns ambushes from frightening mysteries into expected, survivable "
  "events."),
 "key_points": [
  "Private atlases: songs, places, dates linked to the loss by association.",
  "Anniversary potency decays exponentially: base x e^(-years/2.5).",
  "A base-9 loss reads about 6.0 at one year, 2.7 at three, 0.2 at ten.",
  "Sensory reminders can detonate full waves years later.",
  "Map the atlas, note the dates, treat ambushes as weather: fierce, brief, gone."],
 "requirements": [
  "The classic triggers: personal triggers as the private extension.",
  "The timeline record: why grief arrives in waves rather than lines."],
 "standards": [
  "Bereavement research: the episodic course of grief over years.",
  "Associative memory models of context-triggered affect."],
 "citations": [CIT_BONANNO, CIT_BARRETT, CIT_LAZARUS],
 "sig_lens": ("The Signature archivist keeps a calendar of private "
  "tides, because the sea remembers what the mind tries to forget. The "
  "decay curve is filed as a promise: the waves thin, the ambushes "
  "shorten, and the atlas that once read as a minefield slowly becomes a "
  "map of where the treasure was buried."),
},
{
 "key": "emsad-surprise",
 "name": "Surprise triggers: the odd little things",
 "group": "triggers",
 "ladder_rank": 7, "ladder_tier": "compounded",
 "description": ("Some triggers make no sense until they do. A person "
  "steady through a funeral comes undone by a grocery store: the sight of "
  "a favorite cereal, the one the lost person always bought, and the "
  "wave arrives in aisle seven. A sunny day can trigger sadness because "
  "the brightness contrasts with the inner gray. Good news can trigger it "
  "- the promotion that would have made a lost parent proud, the joy with "
  "nowhere to send its thank-you note. The end of a beloved book or series "
  "leaves a genuine, if small, grief for an imagined world. Even relief "
  "can trigger it: the long effort ends, the adrenaline drains, and the "
  "postponed sadness finally clocks in. The simulator ranks these by "
  "unexpectedness - the cereal scores near 9 on the surprise scale while "
  "carrying a potency near 5 - teaching the archive's subtlest lesson: "
  "triggers need no permission and no logic, only an association."),
 "how_it_works": ("Surprise triggers work through the same associative "
  "machinery as personal triggers, but the associations are oblique - a "
  "contrast, a completion, a postponed feeling - so the conscious mind "
  "does not see them coming. The mismatch between expectation (I should "
  "be fine buying cereal) and reaction (I am crying in aisle seven) is "
  "what makes these episodes disorienting, and disorientation amplifies "
  "distress. The simulator's unexpectedness score teaches learners to "
  "separate the trigger's strangeness from its legitimacy: a trigger can "
  "be absurd and the sadness entirely real. That separation is the "
  "difference between shame about the feeling and simple acceptance of "
  "it."),
 "key_points": [
  "The grocery-store ambush: ordinary objects linked to the lost person.",
  "Contrast triggers: sunshine against inner gray; good news with nowhere to send thanks.",
  "Completion triggers: the end of a beloved story; relief after long effort.",
  "Unexpectedness is scored separately from potency: strange trigger, real sadness.",
  "Triggers need no permission and no logic, only an association."],
 "requirements": [
  "The personal-triggers record: associative machinery as the mechanism.",
  "A non-judgmental stance: absurd triggers carry legitimate feelings."],
 "standards": [
  "Associative network models of emotion and memory.",
  "Contrast and completion effects in affective experience."],
 "citations": [CIT_BARRETT, CIT_FRIJDA, CIT_BONANNO],
 "sig_lens": ("The Signature archivist keeps a drawer labeled odd "
  "keys: triggers that fit no lock the conscious mind knows. The drawer "
  "is not a joke - it is the most-used drawer in the building, because "
  "the strangest keys open the heaviest doors, and the archivist would "
  "rather file the odd key than pretend the door stayed shut."),
},
{
 "key": "emsad-cascade",
 "name": "Chain reactions: when sadness pulls other emotions along",
 "group": "triggers",
 "ladder_rank": 7, "ladder_tier": "compounded",
 "description": ("Sadness is a social emotion even inside one mind: it "
  "invites company. The classic cascade runs five steps. It starts with "
  "sadness at 6 over a loss. The loss's solitude breeds loneliness, which "
  "rises to join it. Loneliness curdles into withdrawal - the person stops "
  "answering messages, cancels plans. Withdrawal starves the mind of "
  "counter-evidence and feeds rumination: the loss replayed on a loop. "
  "And rumination deepens the sadness itself, which climbs from 6 toward "
  "8. The simulator models each step as a multiplier on the last, and the "
  "five-step chain peaks near 7.9 - heavier than where it began, built "
  "from nothing but the feeling feeding on its own consequences. The "
  "cascade is the archive's most practical record, because every link is "
  "also an exit: answer one message, take one walk, and the chain loses a "
  "link."),
 "how_it_works": ("Cascades are feedback loops: the feeling produces "
  "behavior, the behavior produces conditions, and the conditions "
  "intensify the feeling. Withdrawal is the critical link - it removes "
  "the social and activity inputs that would otherwise regulate the mood, "
  "leaving rumination unopposed. The simulator computes the chain "
  "step by step, each stage's intensity feeding the next, so learners can "
  "see exactly where interventions bite. Breaking any single link - a "
  "answered message, a short walk, a deliberately scheduled pleasant "
  "activity - drops the downstream multipliers and the cascade collapses "
  "back toward the original, manageable sadness."),
 "key_points": [
  "The five-step cascade: sadness, loneliness, withdrawal, rumination, deepened sadness.",
  "Each step multiplies the last; a 6 can climb toward 8 on its own consequences.",
  "Withdrawal is the critical link: it removes the inputs that would regulate the mood.",
  "The simulator computes the chain stage by stage, peak near 7.9.",
  "Every link is an exit: one message, one walk, and the chain loses a link."],
 "requirements": [
  "The loneliness blend: the cascade's second step.",
  "The timeline: rumination as the engine of the later steps."],
 "standards": [
  "Feedback-loop models of mood: behavioral and cognitive spirals.",
  "Behavioral activation literature: breaking withdrawal links."],
 "citations": [CIT_FRIJDA, CIT_GROSS, CIT_BONANNO],
 "sig_lens": ("Signature science diagrams the cascade as a chain of "
  "five links, each link stamped with its breaking tool: company for "
  "loneliness, motion for withdrawal, occupation for rumination. The "
  "archivist's rule is that no chain is stronger than its weakest link, "
  "and the weakest link is always the one a single small action can "
  "break today."),
},
{
 "key": "emsad-actions",
 "name": "What people do when sadness visits",
 "group": "behavior",
 "ladder_rank": 7, "ladder_tier": "compounded",
 "description": ("Sad behavior is the feeling made visible in choices. The "
  "most common actions form a recognizable set: withdrawing from company, "
  "canceling plans, and seeking solitude carry the highest likelihood at "
  "about 0.80; moving slowly and doing less follows near 0.72; seeking "
  "comfort - calling a friend, asking for a hug - near 0.58; crying, "
  "openly or privately, near 0.55; revisiting reminders such as photos or "
  "old messages near 0.47; and neglecting small routines - unwashed "
  "dishes, unanswered mail - near 0.41. The simulator picks the showcased "
  "action by weighted draw: with a selector of 0.40 the cumulative weights "
  "land on moving slowly and doing less, the honest center of sad "
  "behavior. None of these are character flaws; they are the low-energy "
  "program running as designed. The record's value is recognition: when "
  "these actions cluster, the feeling behind them is usually the one this "
  "archive describes."),
 "how_it_works": ("Actions follow the energy budget and the inward turn of "
  "attention. Withdrawal and solitude reduce social demands; slowness "
  "matches the conserved energy; comfort-seeking broadcasts the need the "
  "sad face advertises; revisiting reminders feeds the mind's attempt to "
  "process the loss; neglected routines are triage, not laziness - the "
  "system sheds low-priority tasks first. The simulator assigns each "
  "action a likelihood drawn from behavioral research directions and "
  "selects by weighted draw, so repeated runs show the distribution, not "
  "just the mode. Learners study the set to recognize the pattern in "
  "others without judgment, and in themselves without shame."),
 "key_points": [
  "Withdrawing and seeking solitude: likelihood about 0.80, the most common move.",
  "Moving slowly and doing less near 0.72; comfort-seeking near 0.58; crying near 0.55.",
  "Revisiting reminders near 0.47; neglected routines near 0.41.",
  "The pattern is the low-energy program running as designed, not a flaw.",
  "Clustered actions reveal the feeling behind them: recognition without judgment."],
 "requirements": [
  "The body records: behavior as the outward face of the energy budget.",
  "The cascade record: withdrawal as both symptom and link."],
 "standards": [
  "Behavioral correlates of sad mood: withdrawal, slowing, help-seeking.",
  "Triage models of reduced functioning under low affect."],
 "citations": [CIT_FRIJDA, CIT_IZARD, CIT_KELTNER],
 "sig_lens": ("The Signature naturalist observes sad behavior the way a "
  "naturalist observes wintering animals: without moralizing, noting "
  "only what the season requires. Withdrawal is burrowing, slowness is "
  "conservation, comfort-seeking is huddling for warmth. The archivist "
  "files every behavior under its function, and finds no villains in the "
  "file."),
},
{
 "key": "emsad-speech",
 "name": "What people say: the voice of sadness",
 "group": "behavior",
 "ladder_rank": 7, "ladder_tier": "compounded",
 "description": ("Sadness has a voice, and it is slower, softer, and "
  "sparser than usual. Speech rate falls about seven words per minute for "
  "each intensity point from a baseline near one hundred fifty - at "
  "intensity 6 the voice moves near one hundred eight words per minute, "
  "with long pauses where thoughts gather. Volume drops; the voice thins "
  "at the ends of sentences; sighs punctuate the flow. The vocabulary "
  "shifts too: more past tense, more loss words - gone, missing, used to "
  "be - and the characteristic phrases appear. I just feel heavy. I do "
  "not have the energy. It is not the same without them. Leave me alone "
  "for a bit, but do not go far. The simulator renders a thirty-second "
  "sample at intensity 6 - about fifty-four words, two sighs, one "
  "trailing sentence - so learners can hear the pattern in numbers before "
  "they meet it in life."),
 "how_it_works": ("Voice changes are the audible half of the low-energy "
  "program: slowed thought produces slowed speech, low arousal produces "
  "low volume, and inward attention produces the pauses. The past-tense "
  "shift reflects the mind's location - dwelling where the lost thing "
  "still existed. The simulator computes word count, pause placement, and "
  "phrase selection from intensity, generating the thirty-second sample "
  "as a teaching audio-script. The practical lesson is listening: the sad "
  "voice is not asking to be fixed or hurried. It is asking, in its slowed "
  "way, to be heard at its own pace."),
 "key_points": [
  "Speech slows about seven words per minute per intensity point from a baseline near 150.",
  "At intensity 6: near 108 words per minute, about 54 words in thirty seconds.",
  "Volume drops; the voice thins at sentence ends; sighs punctuate.",
  "Vocabulary shifts to past tense and loss words: gone, missing, used to be.",
  "Characteristic phrases: I just feel heavy; it is not the same without them."],
 "requirements": [
  "The low-versus-high snapshots: speech rate as a calibrated channel.",
  "The hiding record: the voice as the second thing to leak."],
 "standards": [
  "Speech and affect research: rate, volume, and pause changes under sad mood.",
  "Linguistic markers of loss-focused attention."],
 "citations": [CIT_IZARD, CIT_KELTNER, CIT_FRIJDA],
 "sig_lens": ("The Signature listener tunes the ear before the mouth: "
  "the sad voice is a slowed transmission, and hurrying it garbles the "
  "message. Apprentices practice the thirty-second sample until they can "
  "hear the pauses as punctuation - the silence between sad sentences is "
  "not empty; it is where the unsaid loss is sitting."),
},
{
 "key": "emsad-decisions",
 "name": "How sadness colors decisions and judgment",
 "group": "behavior",
 "ladder_rank": 8, "ladder_tier": "compounded",
 "description": ("Sadness does not just feel; it votes. Under its "
  "influence people grow cautious: the simulator's decision rule has a sad "
  "person accept a gamble only when the chance of winning exceeds fifty "
  "percent plus two points per intensity point - at intensity 7 the bar "
  "sits at sixty-four percent, where a neutral mood would take fifty. "
  "Attention narrows to risks and losses; options are weighed by what "
  "could go wrong rather than what could go right. The mind also discounts "
  "the future: why plan when the present feels gray. And judgments of "
  "other people darken - neutral faces read as colder, ambiguous remarks "
  "as criticism. None of this is irrational in the strict sense; it is "
  "the mind's loss-avoidance program running hot after a real loss. The "
  "archive's practical counsel: notice the tint, postpone the big "
  "irreversible choices until the weather clears, and let small decisions "
  "run on routine."),
 "how_it_works": ("The mechanism is mood-congruent processing: a sad mind "
  "more easily retrieves sad memories and sad interpretations, which then "
  "color the evaluation of new options. Risk aversion rises because the "
  "system, having just registered a loss, is sensitized to further loss - "
  "the same logic that makes a burned hand shy of stoves. The simulator "
  "implements the threshold rule above and demonstrates it on sample "
  "choices: at intensity 7 the sad chooser rejects gambles the neutral "
  "chooser takes, and the difference is the measurable price of the mood. "
  "Knowing the price lets travelers budget for it instead of paying it "
  "blind."),
 "key_points": [
  "The sad chooser needs win odds above 50 percent plus two points per intensity point.",
  "At intensity 7 the bar is 64 percent; the neutral bar is 50.",
  "Attention narrows to risks; the future is discounted; others read as colder.",
  "The pattern is loss-avoidance running hot after a real loss, not irrationality.",
  "Counsel: postpone big irreversible choices; let small ones run on routine."],
 "requirements": [
  "The volume scale: the decision rule is calibrated to intensity.",
  "The behavior set: caution as the cognitive face of the low-energy program."],
 "standards": [
  "Affect and decision-making research: mood-congruent judgment and risk aversion.",
  "Loss-sensitization models following real losses."],
 "citations": [CIT_LAZARUS, CIT_FRIJDA, CIT_KELTNER],
 "sig_lens": ("The Signature treasurer audits every sad decision twice: "
  "once for its merits, once for the weather it was made in. The sixty-four "
  "percent bar is filed as a storm tariff - the extra caution the gale "
  "charges. Apprentices learn to read the tariff before signing, and to "
  "let the big contracts wait for clear skies."),
},
{
 "key": "emsad-escalation",
 "name": "When sadness intensifies: how behavior escalates",
 "group": "behavior",
 "ladder_rank": 8, "ladder_tier": "compounded",
 "description": ("Left to run, sadness climbs a predictable staircase. "
  "The simulator models escalation from a starting intensity of 4, adding "
  "about 1.2 points per stage and capping at 10: stage zero rests at 4.0, "
  "stage one at 5.2, stage two at 6.4, stage three at 7.6, stage four at "
  "8.8, and stage five at the cap of 10.0. Behavior escalates with it in "
  "recognizable steps: quiet withdrawal becomes canceled plans; canceled "
  "plans become days without leaving the house; slowed speech becomes "
  "long silences; neglected routines become neglected self-care; the "
  "thoughts darken from the loss itself to the self - I miss them becomes "
  "I am too much, or not enough. The staircase is not inevitable - each "
  "stage is also a landing where the climb can stop - but knowing the "
  "steps lets travelers and their companions spot the climb early, when "
  "one conversation or one walk can still turn it around."),
 "how_it_works": ("Escalation is the cascade running without "
  "counter-pressure: each stage's behavior removes more regulating input, "
  "so the next stage starts higher. The 1.2-per-stage teaching slope and "
  "the cap at 10 give learners a concrete curve to recognize, with the "
  "behavioral markers as signposts. The simulator's key lesson is the "
  "landing principle: escalation needs fuel - isolation, rumination, "
  "neglected basics - and removing fuel at any stage flattens the curve. "
  "This is why the record pairs every step with its exit: the staircase "
  "is mapped so it can be descended, not just climbed."),
 "key_points": [
  "Escalation modeled from 4.0, plus about 1.2 per stage, capped at 10.0.",
  "Stages: 4.0, 5.2, 6.4, 7.6, 8.8, then the 10.0 cap.",
  "Behavioral signposts: withdrawal to isolation, slowness to silence, neglected routines to neglected self-care.",
  "Thoughts darken from the loss to the self.",
  "Every stage is a landing: remove fuel - isolation, rumination - and the climb stops."],
 "requirements": [
  "The cascade record: escalation as the cascade unopposed.",
  "The action set and speech record: the signposts in order."],
 "standards": [
  "Mood-escalation models: positive feedback without regulation.",
  "Early-intervention literature: the value of catching climbs early."],
 "citations": [CIT_FRIJDA, CIT_GROSS, CIT_BONANNO],
 "sig_lens": ("The Signature surveyor maps the staircase with its "
  "landings marked, because a stair is only a trap when its exits are "
  "hidden. Every step gets two labels - the signpost and the way back "
  "down - and apprentices memorize the pairs: isolation answered by one "
  "message, silence by one voice, darkness by one lamp lit on purpose."),
},
{
 "key": "emsad-healthy",
 "name": "Expressing sadness in healthy ways",
 "group": "healthy-expression",
 "ladder_rank": 8, "ladder_tier": "advanced",
 "description": ("Healthy expression gives sadness somewhere to go. The "
  "archive ranks the options by a simple health score, and the winner is "
  "naming it aloud to a trusted person - saying I am sad because, and "
  "letting the sentence finish - scoring near 9.2. Close behind: writing "
  "it out longhand, unsent letters and journals, near 8.6; crying when "
  "tears come, without apology, near 8.1; moving the body gently - walks, "
  "stretching, unhurried chores - near 7.4; and making something from it: "
  "a song, a drawing, a tended garden, near 7.0. What the winners share "
  "is outward motion with honesty: the feeling is acknowledged, given "
  "form, and released into the world or into trusted hands. The record's "
  "guidance stays general and safe - everyday practices, not treatment - "
  "and its promise is modest and true: expressed sadness moves through "
  "the timeline faster than buried sadness, because the signal delivered "
  "is a signal the system can stand down from."),
 "how_it_works": ("Expression works by completing the signal's circuit: "
  "sadness evolved partly as a call for comfort, and answering the call - "
  "even by writing the unsent letter - tells the system the message was "
  "received. Naming converts a diffuse ache into a specific, manageable "
  "statement; tears discharge physiological arousal; gentle movement "
  "restores the energy budget; making transforms the loss into meaning. "
  "The simulator scores each option on acknowledgment, release, and "
  "connection, and the ranking teaches the principle behind the list: "
  "healthy expression is any honest outward motion that neither harms the "
  "self nor burdens others unfairly."),
 "key_points": [
  "Naming it aloud to a trusted person scores near 9.2: the healthiest option.",
  "Writing it out near 8.6; crying without apology near 8.1.",
  "Gentle movement near 7.4; making something from it near 7.0.",
  "The shared principle: honest outward motion that harms no one.",
  "Expressed sadness moves through the timeline faster than buried sadness."],
 "requirements": [
  "The timeline: expression as the completion of the signal's circuit.",
  "The hiding record: healthy expression as the alternative to the mask."],
 "standards": [
  "Emotion-regulation research: expressive writing and disclosure effects.",
  "Everyday coping literature: general, safe, non-clinical guidance."],
 "citations": [CIT_GROSS, CIT_BONANNO, CIT_FREDRICKSON],
 "sig_lens": ("The Signature signal corps teaches one drill: deliver "
  "the message. A signal that reaches its station - spoken, written, wept, "
  "walked, or made - is stood down with honors; a signal jammed in the "
  "tower keeps broadcasting static. Apprentices practice delivery the "
  "way soldiers practice reporting: clearly, promptly, and to the right "
  "recipient."),
},
{
 "key": "emsad-unhealthy",
 "name": "Bottling it up or blowing up: the two costly exits",
 "group": "healthy-expression",
 "ladder_rank": 9, "ladder_tier": "advanced",
 "description": ("When expression is blocked, sadness takes one of two "
  "costly exits. Bottling it up - the mask worn permanently, the feeling "
  "never named - costs about five points per intensity point plus eight: "
  "at intensity 6 the bottle costs 38, paid in tension, numbness, and the "
  "leakage that betrays the mask anyway. Blowing up - the sadness "
  "detonating sideways as irritability, harsh words, slammed doors - costs "
  "about six per point plus eight: 44 at intensity 6, paid in damaged "
  "relationships and shame that feeds the next wave. The healthy path "
  "costs about two per point plus two: 14 at intensity 6, the cheapest "
  "exit on the board by far. The arithmetic is the archive's quiet "
  "argument: suppression and explosion are not strength and honesty. They "
  "are the two most expensive ways to handle a feeling, and the bill "
  "always comes due."),
 "how_it_works": ("The cost model encodes the research directions: "
  "suppression raises physiological strain and impairs memory and "
  "connection while failing to reduce the feeling; displaced explosion "
  "damages the social bonds that would otherwise regulate the mood, "
  "creating secondary losses that deepen the original sadness. The "
  "simulator computes all three costs at any intensity and the ordering "
  "never changes - healthy expression cheapest, bottling middle, explosion "
  "highest - which is why the record presents the numbers so bluntly. "
  "The lesson is economic, not moral: feelings are going to be paid for "
  "one way or another, so pay the cheapest price."),
 "key_points": [
  "Bottling cost: about 5 per intensity point plus 8; 38 at intensity 6.",
  "Explosion cost: about 6 per point plus 8; 44 at intensity 6.",
  "Healthy expression cost: about 2 per point plus 2; 14 at intensity 6.",
  "The ordering never changes: healthy cheapest, bottling middle, explosion highest.",
  "Suppression and explosion are the two most expensive exits; the bill always comes due."],
 "requirements": [
  "The healthy-expression record: the cheap exit for comparison.",
  "The hiding record: bottling as the permanent mask."],
 "standards": [
  "Suppression-cost literature: physiological and social costs of concealment.",
  "Displacement research: sideways detonation and its relational costs."],
 "citations": [CIT_GROSS, CIT_EKMAN, CIT_FRIJDA],
 "sig_lens": ("The Signature accountant posts the three prices on the "
  "wall where every apprentice can see them: 14, 38, 44. No lectures, no "
  "scolding - just the ledger. Travelers who have paid the 44 before "
  "recognize it instantly, and the sight of the 14 beside it does more "
  "persuading than any sermon about feelings ever could."),
},
{
 "key": "emsad-practices",
 "name": "Small everyday practices for balance",
 "group": "healthy-expression",
 "ladder_rank": 9, "ladder_tier": "advanced",
 "description": ("Balance is built from small, repeatable habits, not "
  "grand gestures. The archive's five practices each carry a daily "
  "benefit score: naming the feeling once a day in a sentence, 3 points; "
  "a twenty-minute walk, 4 points; one honest conversation a week with a "
  "trusted person, averaged to 2 points a day; keeping sleep hours "
  "regular, 3 points; and one small act of making - cooking, tending, "
  "mending - 2 points. Practiced together with a realistic adherence of "
  "seventy percent, the week yields about 68 benefit points - the "
  "simulator's arithmetic is fourteen daily points times seven days "
  "times 0.7. None of these is treatment or therapy; they are the "
  "everyday maintenance the record is allowed to recommend. Their power "
  "is compound interest: small deposits, kept up, that keep the account "
  "from going empty when the next loss arrives."),
 "how_it_works": ("Practices work by feeding the regulators that sadness "
  "starves: naming feeds acknowledgment, walking feeds the energy budget "
  "and breaks rumination, conversation feeds connection, regular sleep "
  "feeds the lagging housekeeping channels, and making feeds meaning. "
  "The simulator multiplies daily benefits by adherence to teach the "
  "central insight - consistency beats intensity. A perfect week of "
  "heroics followed by abandonment scores lower than a mediocre week "
  "repeated for a month. The record therefore preaches smallness: choose "
  "practices so easy they survive bad days, because bad days are exactly "
  "when they are needed."),
 "key_points": [
  "Five practices: naming (3/day), walking (4/day), weekly honest talk (2/day), regular sleep (3/day), small making (2/day).",
  "At seventy percent adherence the week yields about 68 benefit points.",
  "Consistency beats intensity: mediocre weeks repeated outscore heroic weeks abandoned.",
  "Choose practices easy enough to survive bad days.",
  "Compound interest: small deposits that keep the account from emptying."],
 "requirements": [
  "The healthy-expression record: practices as the maintenance schedule.",
  "The sleep record: why regular hours are on the list."],
 "standards": [
  "Behavioral maintenance literature: small repeatable habits.",
  "Adherence research: realistic compliance in benefit modeling."],
 "citations": [CIT_GROSS, CIT_FREDRICKSON, CIT_BONANNO],
 "sig_lens": ("The Signature quartermaster issues five small tools, not "
  "one great machine: a sentence, a walk, a conversation, a bedtime, a "
  "mended thing. Apprentices are drilled in maintenance, not rescue - "
  "because the archive has learned, the hard way, that travelers are "
  "saved by their habits long before they are saved by their heroes."),
},
{
 "key": "emsad-reading",
 "name": "Reading sadness in others: face, body, voice, behavior",
 "group": "reading-others",
 "ladder_rank": 9, "ladder_tier": "advanced",
 "description": ("Reading sadness in another person is a four-channel "
  "skill, and the archive teaches it as a weighted checklist. The face "
  "counts most at 0.35: look for the inner-brow lift, the drooping lids, "
  "the downturned mouth. The body counts 0.25: the rounded shoulders, the "
  "slowed walk, the self-hug. The voice counts 0.25: the slowed, softened, "
  "sigh-marked speech. Behavior counts 0.15: the canceled plans, the "
  "quiet withdrawal. The simulator scores a sample set of cues - face at "
  "0.8, body at 0.6, voice at 0.7, behavior at 0.5 - and the weighted sum "
  "lands at 0.68, which the archive reads as likely sadness, worth a "
  "gentle check-in. The record's ethics are explicit and repeated: this "
  "skill describes observable signs for the purpose of kindness. It never "
  "labels a real person, never diagnoses, and never substitutes for "
  "asking. The checklist informs the question - are you all right - it "
  "never replaces it."),
 "how_it_works": ("The weights reflect each channel's reliability: the "
  "face is hardest to fake and carries the most weight; the body and "
  "voice are strong but noisier; behavior is the weakest alone because "
  "withdrawal has many causes. The simulator multiplies each observed cue "
  "strength by its weight and sums them, then bands the result: below 0.4 "
  "unlikely, 0.4 to 0.6 possible, above 0.6 likely. Learners practice on "
  "described scenarios - text sketches, never real people or photos - and "
  "the answers explain which cues carried the reading. The goal is not "
  "certainty but calibrated attention: noticing enough to care, humbly "
  "enough to ask."),
 "key_points": [
  "Four channels weighted: face 0.35, body 0.25, voice 0.25, behavior 0.15.",
  "Sample cues score 0.68: likely sadness, worth a gentle check-in.",
  "Bands: below 0.4 unlikely, 0.4-0.6 possible, above 0.6 likely.",
  "Practice on described scenarios only: text sketches, never real people or photos.",
  "The checklist informs the question - are you all right - never replaces it."],
 "requirements": [
  "The face, posture, speech, and action records: the four channels.",
  "The ethics line: describe signs for kindness, never label a person."],
 "standards": [
  "Cue-integration models in emotion recognition.",
  "Ethical standards for observational description versus diagnosis."],
 "citations": [CIT_EKMAN, CIT_IZARD, CIT_KELTNER],
 "sig_lens": ("The Signature scout reads sign the way trackers read "
  "ground: four kinds of print, weighted by how surely each speaks, and "
  "the reading always ends in a question, never a verdict. Apprentices "
  "are graded on their gentleness as well as their accuracy - because a "
  "scout who startles the traveler has failed the mission no matter how "
  "truly the sign was read."),
},
{
 "key": "emsad-support",
 "name": "What helps: responding to sadness in another person",
 "group": "reading-others",
 "ladder_rank": 9, "ladder_tier": "advanced",
 "description": ("When someone near you is sad, the helpful responses form "
  "a ranked list, and the archive scores each by a helpfulness rating. "
  "Listening without fixing leads at 9.4: full attention, no solutions "
  "offered unless asked. Naming what you see, gently - you seem sad, is "
  "that right - follows at 8.8, because it shows the signal was received. "
  "Offering specific, concrete help - I can bring dinner Thursday - "
  "scores 8.2, far above vague let me know if you need anything. Simply "
  "being present, quietly, without demands, scores 7.9. Sharing a brief "
  "similar experience, only to show understanding and never to take the "
  "floor, scores 7.1. What the winners share is the posture of the "
  "previous record's scout: attention without presumption, care without "
  "control. The sad person is the authority on their own feeling; the "
  "helper's job is to make the feeling less lonely, not to make it go "
  "away."),
 "how_it_works": ("Helpful responses work by meeting the two needs sadness "
  "broadcasts: the need for the loss to be honored and the need for "
  "company in it. Listening honors without directing; gentle naming "
  "proves reception; concrete help removes real burdens the low-energy "
  "system cannot carry; quiet presence answers loneliness without words; "
  "brief shared experience normalizes without hijacking. The simulator "
  "scores each response on honoring, company, and non-intrusion, and the "
  "ranking teaches the meta-rule: follow the sad person's lead. Offer, "
  "do not impose; ask, do not assume; stay, do not fix. Presence is the "
  "help; everything else is packaging."),
 "key_points": [
  "Listening without fixing: 9.4, the most helpful response.",
  "Gentle naming - you seem sad, is that right - at 8.8.",
  "Specific concrete help at 8.2 beats vague offers of help.",
  "Quiet presence at 7.9; brief shared experience at 7.1, never taking the floor.",
  "The meta-rule: follow their lead - offer, do not impose; stay, do not fix."],
 "requirements": [
  "The reading record: recognizing the signs before responding.",
  "The healthy-expression record: what the sad person needs most."],
 "standards": [
  "Social-support literature: instrumental versus emotional support.",
  "Help-giving research: autonomy-supportive versus directive responses."],
 "citations": [CIT_BONANNO, CIT_KELTNER, CIT_GROSS],
 "sig_lens": ("The Signature companion's handbook has one page, and "
  "the first line is underlined: you are not the repair crew. The "
  "companion carries five tools - ears, a mirror, a casserole, a chair, "
  "and a short story - and the standing order for all five is the same: "
  "make the road less lonely, and leave the walking to the traveler."),
},
{
 "key": "emsad-mistakes",
 "name": "What backfires: responses that make it worse",
 "group": "reading-others",
 "ladder_rank": 10, "ladder_tier": "advanced",
 "description": ("Good intentions misfire in predictable ways, and the "
  "archive catalogs the misfires by their harm scores. Telling someone to "
  "cheer up or look on the bright side tops the list at 9.1: it denies "
  "the signal and shames the sender. Comparing losses - I know how you "
  "feel, my situation was worse - scores 8.4, hijacking the floor. "
  "Rushing with solutions before listening scores 7.8. Minimizing - it "
  "is not that bad, at least - scores 7.5. Avoiding the person because "
  "their sadness is uncomfortable scores 7.2, and it teaches the loneliest "
  "lesson of all: that sadness exiles. The simulator's ranking exists so "
  "learners can recognize these moves in themselves before they make "
  "them. Every misfire shares one root: answering the helper's discomfort "
  "instead of the sad person's need. The correction is always the same - "
  "return to the previous record's list, and let the sad person lead."),
 "how_it_works": ("Misfires backfire through three mechanisms: invalidation "
  "(the feeling is treated as wrong), hijacking (attention moves to the "
  "helper), and abandonment (the person is left alone with it). Cheer-up "
  "orders invalidate; comparisons hijack; avoidance abandons; premature "
  "solutions do all three at once by implying the feeling is a problem to "
  "be solved quickly. The simulator scores each misfire on those three "
  "axes and the totals produce the ranking, teaching learners to audit "
  "their own impulses: am I soothing them, or soothing myself. The "
  "record is blunt because the stakes are real - a single careless "
  "sentence can close a person for months - and gentle because everyone "
  "has made these mistakes."),
 "key_points": [
  "Cheer up / look on the bright side: harm 9.1, the worst misfire.",
  "Comparing losses and hijacking the floor: 8.4.",
  "Rushing to solutions: 7.8; minimizing: 7.5; avoidance: 7.2.",
  "Three mechanisms: invalidation, hijacking, abandonment.",
  "Every misfire answers the helper's discomfort; the correction is to follow the sad person's lead."],
 "requirements": [
  "The support record: the helpful list these misfires invert.",
  "Honesty about one's own impulses: everyone has made these mistakes."],
 "standards": [
  "Invalidation research: effects of dismissive responses on distress.",
  "Support-giving failure modes in the close-relationships literature."],
 "citations": [CIT_GROSS, CIT_BONANNO, CIT_KELTNER],
 "sig_lens": ("The Signature companion's handbook has a second page, "
  "printed in red: the five roads that lead away from the traveler. "
  "Apprentices memorize the harm scores the way medics memorize poisons - "
  "not to fear people, but to handle their own good intentions like the "
  "potent medicine they are: right dose, right moment, or not at all."),
},
{
 "key": "emsad-relatives",
 "name": "The relatives of sadness: grief, disappointment, melancholy, and how to tell them apart",
 "group": "relatives-and-mixes",
 "ladder_rank": 10, "ladder_tier": "advanced",
 "description": ("Sadness has close relatives, and the archive maps them "
  "by distance. Melancholy is the nearest neighbor at a distance of only "
  "0.15: sadness settled in for a long, reflective stay, milder but more "
  "enduring, often without a single clear cause. Disappointment stands at "
  "0.30: sadness aimed at a specific unmet expectation, sharper and more "
  "focused, fading when the expectation is revised. Grief stands at 0.45: "
  "sadness stretched across the loss of a person, deeper and wave-like, "
  "with its own multi-year course. Despair stands at 0.60: sadness plus "
  "the judgment that nothing will ever improve, the relative that most "
  "needs company and care. Apathy stands at 0.75: the flat absence where "
  "sadness used to be, feeling's opposite more than its kin. The "
  "distances are teaching values, and the telling-apart rules are "
  "practical: ask what it is about (the object), how long it has stayed "
  "(the course), and what it wants (comfort, revision, witness, hope, or "
  "rest). Close cousins are not the same person - treat each by its own "
  "name."),
 "how_it_works": ("The map is built on three distinguishing questions - "
  "object, course, and need - applied to each relative. Melancholy's "
  "object is diffuse and its course is long; disappointment's object is "
  "one expectation and its course is short; grief's object is a person "
  "and its course runs in waves over years; despair's object is the "
  "future itself; apathy has no object because the feeling has gone "
  "quiet. The simulator computes pairwise distances from these profiles "
  "and the nearest-neighbor result teaches the headline: melancholy is "
  "closest, apathy farthest. The record's deeper lesson is humility - "
  "these are descriptive distinctions for understanding, never labels to "
  "pin on a living person."),
 "key_points": [
  "Melancholy: distance 0.15, the nearest neighbor - long, reflective, diffuse.",
  "Disappointment: 0.30 - sharp, aimed at one unmet expectation, short course.",
  "Grief: 0.45 - sadness across the loss of a person, wave-like, multi-year.",
  "Despair: 0.60 - sadness plus the judgment that nothing will improve.",
  "Apathy: 0.75 - the flat absence; three questions tell them apart: object, course, need."],
 "requirements": [
  "The family record: relatives as complex members of the sadness family.",
  "The ethics line: descriptive distinctions, never labels on real people."],
 "standards": [
  "Emotion-differentiation research: object, course, and action tendency.",
  "Bereavement literature distinguishing grief from neighboring states."],
 "citations": [CIT_PLUTCHIK, CIT_BONANNO, CIT_LAZARUS],
 "sig_lens": ("The Signature genealogist charts the family with measured "
  "distances, because cousins are constantly mistaken for siblings. The "
  "map's moral is filed alongside its measurements: name the relative "
  "correctly and you bring the right remedy - comfort for grief, revision "
  "for disappointment, witness for melancholy, hope for despair, rest for "
  "apathy - and a wrong name is a wrong medicine."),
},
{
 "key": "emsad-mixes",
 "name": "Sadness in blends: four emotion mixes",
 "group": "relatives-and-mixes",
 "ladder_rank": 10, "ladder_tier": "advanced",
 "description": ("The archive's mix blender takes sadness at intensity 7 "
  "and folds in four partners, and each blend comes out a different "
  "country. With anger at 5, the blend is frustrated sorrow at about 6.2: "
  "the heaviness with heat in it, tears that arrive annoyed at "
  "themselves, the urge to both weep and argue. With surprise at 6, the "
  "blend is disappointment at about 6.5: the shock still fresh inside the "
  "heaviness, the replaying of the moment it went wrong. With fear at 8, "
  "the blend is despair at about 7.5: the heaviness with a cold edge, the "
  "future read as more of the same. With joy at 3, the blend is "
  "bittersweetness at about 5.8: the ache holding something golden, "
  "gratitude and grief in the same breath - the wedding where the empty "
  "chair is felt, the song that hurts because it was beautiful. The "
  "simulator computes each blend as a weighted profile and verifies the "
  "four are pairwise distinct: no two blends closer than 0.3 apart. The "
  "lesson is the family rule from the second record, now in full color: "
  "name the partner and you name the blend."),
 "how_it_works": ("Each blend is computed as a weighted average of the "
  "two emotion profiles - sadness at 7, the partner at its level - with "
  "weights set by relative intensity, then described through the "
  "components: inner monologue tint, body signature, facial cast, and "
  "behavioral urge. The pairwise-distinctness check guarantees the "
  "blender is not just renaming one feeling four times: frustrated "
  "sorrow, disappointment, despair, and bittersweetness genuinely differ "
  "in texture. Learners use the blender to practice the archive's core "
  "discrimination skill - when a feeling seems complicated, look for the "
  "second ingredient, because complicated feelings are usually blends "
  "waiting to be unmixed."),
 "key_points": [
  "Sadness 7 + anger 5: frustrated sorrow near 6.2 - heaviness with heat.",
  "Sadness 7 + surprise 6: disappointment near 6.5 - shock fresh inside heaviness.",
  "Sadness 7 + fear 8: despair near 7.5 - heaviness with a cold edge.",
  "Sadness 7 + joy 3: bittersweetness near 5.8 - ache holding something golden.",
  "All four blends pairwise distinct by at least 0.3: genuinely different countries."],
 "requirements": [
  "The loneliness blend: the method, now generalized to four partners.",
  "The family record: Plutchik-style dyads as the naming scheme."],
 "standards": [
  "Emotion-blend models: weighted profiles of co-occurring appraisals.",
  "Distinctness criteria for named affective mixtures."],
 "citations": [CIT_PLUTCHIK, CIT_IZARD, CIT_FRIJDA],
 "sig_lens": ("The Signature blender keeps four labeled jars on the "
  "shelf, each a different color of the same base sorrow. Apprentices "
  "learn the jars by taste - heat, shock, cold, gold - until unmixing "
  "becomes reflex: when a traveler says I feel everything at once, the "
  "archivist reaches for the jars and asks, in what proportions."),
},
{
 "key": "emsad-full-sim",
 "name": "The full simulation: sadness from trigger to resolution",
 "group": "relatives-and-mixes",
 "ladder_rank": 10, "ladder_tier": "advanced",
 "description": ("The archive's showcase simulation runs one complete "
  "episode, scene by scene. Scene one, the trigger: Mara learns her "
  "closest friend is moving across the country; the appraisal lands in "
  "about eight minutes and intensity climbs to 5. Scene two, the rise: "
  "over the afternoon the loss sinks in - the empty lunch table imagined, "
  "the routines inventoried - and intensity reaches 7.2 at the twenty-five "
  "minute peak, tears arriving unbidden. Scene three, the turn: a friend "
  "calls, Mara names the feeling aloud - I am sad because she is leaving "
  "and I will miss our ordinary days - and the circuit completes; "
  "intensity eases to 5.5. Scene four, the fade: the evening passes with "
  "the forty-minute half-life doing its work, down to 3.1. Scene five, "
  "resolution: a week of small practices later, the baseline rests at "
  "1.5 - the friendship intact in a new form, the loss filed, the lesson "
  "kept. Every number obeys the archive's scaling rules, and the "
  "resolution reads well below the peak, exactly as the timeline "
  "promises. Mara is invented, her episode is a composite, and the "
  "simulation is the whole archive in miniature: trigger, peak, "
  "expression, fade, resolution - the shape of sadness, walked end to "
  "end."),
 "how_it_works": ("The full simulation chains the archive's models in "
  "order: the trigger record supplies the event and its potency, the "
  "timeline supplies the phase durations, the volume and body records "
  "supply the intensity curve and its channels, the expression records "
  "supply the healthy exit, and the practices supply the resolution "
  "slope. Each scene prints its intensity, body state, facial cast, "
  "inner monologue line, and behavior, so learners see every subsystem "
  "moving together. The final assertion - resolution below peak - is the "
  "archive's closing promise: sadness is weather, the models describe "
  "the weather truly, and weather passes."),
 "key_points": [
  "Scene one, trigger: the news lands, intensity climbs to 5 in about eight minutes.",
  "Scene two, rise: the loss sinks in, peak 7.2 at twenty-five minutes, tears arrive.",
  "Scene three, turn: naming the feeling aloud completes the circuit, easing to 5.5.",
  "Scene four, fade: the forty-minute half-life works, down to 3.1.",
  "Scene five, resolution: a week of practices later, baseline 1.5 - below the peak, as promised."],
 "requirements": [
  "Every record before it: the full simulation chains the whole archive.",
  "Read Mara as invented: a composite showcase, never a real person."],
 "standards": [
  "Integrative simulation standards: chained sub-models with consistent parameters.",
  "Composite-scenario ethics: invented persons, educational purpose."],
 "citations": [CIT_BONANNO, CIT_GROSS, CIT_LAZARUS],
 "sig_lens": ("The Signature showcase runs the whole voyage in five "
  "charts: the squall sighted, the gale weathered, the signal delivered, "
  "the sea calming, the harbor reached. Apprentices walk Mara's episode "
  "the way sailors walk a charted passage - buoy by buoy - and graduate "
  "knowing the route by heart: every sadness has a far shore, and the "
  "archive exists to prove it."),
},
]
