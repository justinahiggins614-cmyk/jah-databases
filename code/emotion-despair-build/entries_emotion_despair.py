#!/usr/bin/env python3
"""Entries for the Despair Emotion databases (Manon's 2026-10-17 16:15 order,
emotion series batch 2).

Two NEW databases, 34 ladder-ordered records each:

  emotion-despair              - The Despair Emotion Database
                                 (public-harvest: real, fact-checked
                                 psychology of despair - what it is, how it
                                 feels, body signals, facial expression,
                                 triggers, behavior, healthy expression,
                                 recognizing it in others, related emotions
                                 and mixes, full behavioral simulation;
                                 descriptive and educational only, never
                                 diagnosing real people)
  emotion-despair-signature    - The Despair Emotion Signature Database
                                 (his original Signature emotional science:
                                 despair as the archive's signal of a future
                                 that reads as closed - the mind's forecast
                                 of no way forward, a broken weather vane;
                                 the first tool is to re-open one door, one
                                 next step; src signature, titles suffixed
                                 " (Signature Edition)", never presented as
                                 authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-EMDE- (public) and JAH-EMDES- (signature), verified free
in the manifest id_prefix values and with zero hits in every shard index
file (2026-10-17).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_emotion_despair.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos.

Concurrency: this builder writes ONLY its own new untracked paths -
db/emotion-despair/, db/emotion-despair-signature/,
code/emotion-despair-build/, the data-1 shard dirs, and the fragment file.
It never touches data/manifest.json, api.json, index.html, README.md,
docs/AI_ACCESS.md, and never commits or pushes. A merger handles those.

Screening: descriptive and educational only. No diagnosing real people, no
clinical language, no therapeutic advice beyond general safe everyday
guidance, no religious talk, nothing hate-adjacent or profane. Handle the
topic with care and warmth: despair is the heaviest entry in this series,
so every record pairs honest description with a steady, human, hopeful
tone - describing the feeling fully while always showing the way back is
built in, not argued. When despair feels very heavy or stays a long time,
reaching out to trusted people - and to a counselor or professional - is
described as a strong and ordinary move.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature emotional science: "
            "despair as the archive's signal of a future that reads as "
            "closed - the mind's forecast of no way forward, a broken "
            "weather vane rather than a fact; the Signature archivist's "
            "first tool is to re-open one door, one next step, and file the "
            "forecast as weather, not destiny. Clearly labeled "
            "Signature-made, never presented as authentic public record.")

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
 "key": "emde-what-is",
 "name": "What despair is, in plain words",
 "group": "what-despair-is",
 "ladder_rank": 1, "ladder_tier": "foundations",
 "description": ("Despair is the heavy, sinking feeling that nothing will "
  "ever get better - the collapse of hope. Where sadness mourns what was "
  "lost, despair stops believing in what could still come. People describe "
  "it as the bottom falling out of the future: the plans go quiet, the "
  "energy to try drains away, and the mind starts narrating every effort "
  "as pointless before it even begins. Psychologists place despair among "
  "the most intense of the human feeling states: it is not a quiet mood "
  "but a full-body shutdown of the drive to keep going. It usually arrives "
  "after a run of defeats or one enormous loss, when the brain adds up "
  "the evidence and delivers the verdict that the story is over. That "
  "verdict is the feeling talking, not a fact about the future - and "
  "learning to tell those two apart is what this whole database is for."),
 "how_it_works": ("Despair begins with an appraisal of the future, not "
  "just the past: the mind scans tomorrow and reports back that no good "
  "path exists. That forecast - part memory, part imagination - switches "
  "the body into its deepest conservation mode. Breathing shallows, the "
  "shoulders round forward, the gaze drops or goes unfocused, and the "
  "muscles go slack as if preparing for a long stillness. Motivation "
  "evaporates because the brain has stopped issuing effort: why spend "
  "energy on a game already declared lost. The feeling feeds itself, too, "
  "because withdrawing stops new good evidence from arriving. The "
  "mechanism is old and protective in small doses - resting after defeat "
  "beats charging off a cliff - but when it locks on, the archive teaches "
  "the one counter-move it cannot resist: one small real action, which "
  "forces the forecast to update."),
 "key_points": [
  "Despair is the collapse of hope - the feeling that nothing will ever improve.",
  "It is aimed at the future, not just the past: the mind forecasts no good path.",
  "The body answers with deep conservation: stillness, slackness, effort draining away.",
  "It is self-feeding: withdrawing stops new good evidence from arriving.",
  "The verdict is the feeling talking, not a fact about the future - that is learnable."],
 "requirements": [
  "An everyday vocabulary for feelings, kept plain and free of clinical labels.",
  "The difference between a forecast and a fact: despair predicts, it does not report.",
  "The distinction between describing an emotion and diagnosing a person."],
 "standards": [
  "Lazarus appraisal theory: emotion follows the mind's verdict about what comes next.",
  "Plutchik's emotion wheel: despair as an intense compound of sadness and fear."],
 "citations": [CIT_LAZARUS, CIT_PLUTCHIK, CIT_FRIJDA],
 "sig_lens": ("Through the Signature lens, despair is the archive's "
  "signal of a future that reads as closed - the mind's forecast of no "
  "way forward. The Signature archivist files it as weather, never as "
  "destiny: a forecast can be wrong, and the archive keeps every case "
  "where the forecast broke. The first tool is always to re-open one "
  "door - one next step - because a single step is a fact the forecast "
  "has to answer to."),
},
{
 "key": "emde-family",
 "name": "Where despair sits in the emotion family",
 "group": "what-despair-is",
 "ladder_rank": 1, "ladder_tier": "foundations",
 "description": ("In the family tree of feelings, despair is a complex "
  "emotion - not one of the simple roots but a storm grown from them. "
  "Its two main parents are sadness and fear: from sadness it inherits "
  "the heaviness and the sense of loss, and from fear it inherits the "
  "dread of what comes next. That is why despair feels different from "
  "plain sadness: sadness looks backward at what was lost, while despair "
  "looks forward and sees nothing. It sits at the intense end of the "
  "hopelessness branch, with discouragement as its mild cousin, "
  "hopelessness as its sibling, and despondency as its close neighbor. "
  "Its opposite across the wheel is hope - not just cheerfulness but the "
  "felt sense that effort can still matter. Knowing the family matters "
  "because complex emotions untangle through their parents: soften the "
  "fear about tomorrow and grief-work the sadness about yesterday, and "
  "the storm loses its structure."),
 "how_it_works": ("Complex emotions assemble from simpler ingredients, "
  "and despair's recipe is one part loss (sadness), one part threat "
  "(fear), stirred together with time. The sadness ingredient supplies "
  "the weight: the low energy, the withdrawal, the tears that may or may "
  "not come. The fear ingredient supplies the future-orientation: the "
  "stomach-turning sense that the bad road keeps going. When both run at "
  "once, the mind's appraisal system converges on the darkest summary: "
  "something precious is gone AND nothing coming is good. That double "
  "appraisal is what makes despair heavier than either parent alone. "
  "The family map also shows the exits: hope is the true opposite - the "
  "belief that action can still change the outcome - and every practice "
  "that rebuilds one parent (comfort for the sadness, safety for the "
  "fear) loosens the compound."),
 "key_points": [
  "Despair is a complex emotion, built mainly from sadness plus fear.",
  "Sadness looks back at loss; despair looks forward and sees no good path.",
  "Its mild cousin is discouragement, its sibling hopelessness, its opposite hope.",
  "The two parents run at once: loss behind plus threat ahead equals the storm.",
  "Loosening either parent - comfort the sadness, calm the fear - weakens the whole."],
 "requirements": [
  "The primary emotions (sadness, fear) as building blocks of complex feelings.",
  "The mild-to-intense gradient along the hopelessness branch.",
  "Hope defined plainly: the felt sense that effort can still matter."],
 "standards": [
  "Plutchik's dyad model: complex emotions as blends of primary pairs.",
  "Izard's differential-emotions account of how basic feelings combine."],
 "citations": [CIT_PLUTCHIK, CIT_IZARD, CIT_BARRETT],
 "sig_lens": ("Through the Signature lens, the emotion family is the "
  "archive's genealogy shelf: every storm has parents, and despair's "
  "parents are filed as Loss (the sadness wing) and Threat (the fear "
  "wing). The Signature archivist untangles storms by lineage - comfort "
  "the loss, calm the threat - because a storm whose parents are handled "
  "one at a time stops being a storm and becomes weather you can dress "
  "for."),
},
{
 "key": "emde-volumes",
 "name": "Despair at different volumes: mild, moderate, intense",
 "group": "what-despair-is",
 "ladder_rank": 2, "ladder_tier": "foundations",
 "description": ("The same emotion runs at very different volumes, and "
  "despair is no exception. At mild volume it is discouragement: the "
  "plan failed, the energy dips, a person sighs and thinks 'what is the "
  "point' but still shows up the next day. At moderate volume it is "
  "hopelessness proper: effort starts to feel fake, mornings get harder, "
  "the person stops making plans because planning itself hurts, and "
  "others can see the flatness in their face and voice. At intense "
  "volume it is full despair: the future reads as sealed shut, the body "
  "goes into deep shutdown, basic tasks feel impossible, and the person "
  "may say the story is over - which is when other people need to step "
  "in close. The volume dial matters because the right response "
  "changes with it: mild despair wants a small win and some rest, "
  "moderate despair wants company and structure, and intense despair "
  "wants steady human presence and professional support nearby."),
 "how_it_works": ("Intensity in emotion follows the appraisal like a "
  "thermometer follows heat. Mild despair appraises one effort as "
  "failed; the body dips a little and recovers with rest or a small "
  "success. Moderate despair appraises a pattern: several efforts have "
  "failed, so the forecast darkens and the body starts budgeting "
  "energy as if a long winter is coming - sleep shifts, appetite shifts, "
  "the voice flattens. Intense despair appraises the whole trajectory: "
  "the forecast becomes 'nothing will ever work,' and the body answers "
  "with the deepest conservation it knows - near-total stillness, as if "
  "the organism is waiting out a storm. Because the appraisal drives "
  "the volume, feeding the mind one piece of real counter-evidence - "
  "one thing that did work, one person who showed up - turns the dial "
  "down measurably. The feeling is loud, but it is still reading a "
  "meter, and meters can move."),
 "key_points": [
  "Mild despair is discouragement: the dip after one failure, still showing up.",
  "Moderate despair is hopelessness: effort feels fake, planning hurts, flatness shows.",
  "Intense despair reads the future as sealed: deep shutdown, others must step in close.",
  "The right response changes with the volume: small wins, company, or steady presence.",
  "Appraisal drives the dial - one real piece of counter-evidence turns it down."],
 "requirements": [
  "A 1-to-10 intensity scale as shared vocabulary, without clinical labels.",
  "The rule that louder feeling is still a reading, not a verdict.",
  "Different volumes ask for different responses from the people nearby."],
 "standards": [
  "Frijda's laws of emotion: intensity tracks the strength of the appraisal.",
  "Gross's process model: the feeling can be met at the appraisal stage."],
 "citations": [CIT_FRIJDA, CIT_GROSS, CIT_LAZARUS],
 "sig_lens": ("Through the Signature lens, the volume dial is the "
  "archive's gauge panel: mild, moderate, intense are three different "
  "machines, not one machine with a mood. The Signature archivist reads "
  "the gauge first and then picks the tool - a small win for mild, "
  "company and structure for moderate, steady human presence for "
  "intense - because the right tool at the wrong volume is no tool at "
  "all."),
},
{
 "key": "emde-myths",
 "name": "Myths and misunderstandings about despair",
 "group": "what-despair-is",
 "ladder_rank": 2, "ladder_tier": "foundations",
 "description": ("Despair carries heavy myths, and they do real damage. "
  "Myth one: feeling despair means you are weak. In truth it means you "
  "cared enough to try hard and long; despair is the receipt for "
  "sustained effort against hard odds, not a character report. Myth two: "
  "you should just think positive. Forced cheerfulness insults the real "
  "losses underneath and usually deepens the feeling - what works is "
  "one honest small step, not a pep talk. Myth three: despair means "
  "nothing can help. The feeling itself is built to claim that, but the "
  "record of human lives says otherwise: forecasts break constantly, "
  "and the feeling is a notoriously bad fortune-teller. Myth four: "
  "talking about it makes it worse. Said carefully, naming it out loud "
  "to someone safe loosens it; it is silence that lets it harden. Myth "
  "five: it will pass on its own, so do nothing. Sometimes it eases, "
  "but waiting alone in the dark is the slowest possible route - company "
  "and structure beat waiting every time."),
 "how_it_works": ("Myths about despair work like bad instructions taped "
  "to a machine: people follow them and get worse results. 'Stay strong' "
  "teaches hiding, and hiding cuts off the exact thing - human contact "
  "and new evidence - that would update the dark forecast. 'Think "
  "positive' teaches arguing with the feeling, which hands the feeling "
  "a sparring partner and makes it louder. The accurate instructions are "
  "simpler and duller: name it plainly, keep one daily structure, do "
  "one small real thing, let one person sit near it with you. Each of "
  "those feeds the appraisal system something other than the forecast - "
  "a fact, a rhythm, a witness. The mechanism underneath the myth-"
  "busting is the same one that built the feeling: the mind updates on "
  "evidence, and myths are just a way of blocking the evidence door."),
 "key_points": [
  "Despair is not weakness - it is the receipt for sustained effort against hard odds.",
  "Forced positivity backfires; one honest small step beats any pep talk.",
  "The feeling claims nothing can help, but it is a notoriously bad fortune-teller.",
  "Naming it to someone safe loosens it; silence lets it harden.",
  "Waiting alone is the slowest route - company and structure beat waiting."],
 "requirements": [
  "Five myths stated plainly, each answered with the gentler truth.",
  "No clinical labels anywhere in the myth-busting.",
  "Every answer ends in something doable, not just something knowable."],
 "standards": [
  "Keltner and colleagues on the social functions of sharing emotion.",
  "Barrett on constructed emotion: labels and beliefs reshape the feeling itself."],
 "citations": [CIT_KELTNER, CIT_BARRETT, CIT_GROSS],
 "sig_lens": ("Through the Signature lens, myths are corrupted instruction "
  "cards filed in the wrong drawer of the archive. The Signature "
  "archivist pulls the bad cards, shreds them in the open, and files the "
  "true ones: name it, structure the day, take one small step, let one "
  "person stand near. An archive that keeps its instructions honest is "
  "an archive whose machines - and people - run."),
},
{
 "key": "emde-inside",
 "name": "Inside the feeling: a first-person passage of despair",
 "group": "inside-the-feeling",
 "ladder_rank": 2, "ladder_tier": "foundations",
 "description": ("It is morning and the alarm is a sound from another "
  "planet. I lie still and do the math I have done a hundred times: get "
  "up, try again, fail again - or stay here, where at least nothing else "
  "breaks. The ceiling has a crack I know better than my own plans. "
  "Everything feels far away, like watching my life through thick glass. "
  "People say the sun is out; I believe them the way you believe in a "
  "country you will never visit. My chest feels hollowed, my limbs feel "
  "borrowed and heavy. The thoughts come in a flat voice: it will not "
  "work, it never works, why did I ever think it would. I am not crying; "
  "crying would mean something is still moving. This is the still part. "
  "Somewhere under it all, tiny and stubborn, a pilot light is still on - "
  "I am reading this, I am noticing the crack in the ceiling, I am still "
  "here. That pilot light is the whole story this archive is built on: "
  "as long as it burns, the future is not finished being written."),
 "how_it_works": ("A first-person simulation works by translating the "
  "mechanics of despair into lived texture. The 'alarm from another "
  "planet' is the shutdown of the drive to act - the brain has stopped "
  "pricing effort as worthwhile, so even small tasks feel priced in a "
  "foreign currency. The 'thick glass' is attentional narrowing: the "
  "mind pulls inward and the world loses its color and nearness. The "
  "flat inner voice is the forecast mechanism running unopposed - with "
  "no new evidence coming in, the old verdict repeats. And the pilot "
  "light is the teaching payload of the passage: awareness itself is "
  "still functioning, which means the observing self has not shut down. "
  "Simulations like this one are educational instruments - they let a "
  "reader rehearse understanding of the feeling from the inside, so "
  "that if they ever meet it in themselves or a loved one, they are "
  "not meeting a stranger."),
 "key_points": [
  "The core texture: heaviness, distance, and the flat inner voice saying it will not work.",
  "Effort feels priced in a foreign currency - that is the drive shutting down, not laziness.",
  "The world goes far away behind thick glass: attention narrowing, color draining.",
  "The pilot light - simple awareness - is still on, and that is the whole leverage point.",
  "Simulations are rehearsals: meeting the feeling on paper first means not meeting a stranger."],
 "requirements": [
  "A first-person voice that is honest about the heaviness and never hopeless in tone.",
  "The pilot-light turn: every passage must end showing the way back is built in.",
  "No diagnosing, no clinical terms - only described experience."],
 "standards": [
  "Phenomenological description: first-person accounts as valid emotion data.",
  "Barrett on interoception: the body's signals become the felt story."],
 "citations": [CIT_BARRETT, CIT_PANKSEPP, CIT_IZARD],
 "sig_lens": ("Through the Signature lens, the inside passage is the "
  "archive's flight recorder: the black box of a mind mid-storm, played "
  "back so the next pilot can learn the route through. The Signature "
  "archivist never edits the recording to sound braver than it was - "
  "honesty is the instrument - but always marks where the pilot light "
  "stayed on, because that mark is the map legend for everyone who "
  "reads it later."),
},
{
 "key": "emde-timeline",
 "name": "How despair moves through time: onset, peak, fading, aftershock",
 "group": "inside-the-feeling",
 "ladder_rank": 3, "ladder_tier": "foundations",
 "description": ("Despair has a shape in time, and knowing the shape "
  "keeps people from mistaking a phase for a permanent address. Onset "
  "is usually gradual: a few defeats stack up, the inner commentary "
  "turns, sleep gets thin, and one morning the effort just does not "
  "come. Sometimes it arrives all at once after a single crushing "
  "blow - the phone call, the closed door - and the bottom drops out in "
  "an afternoon. The peak is the sealed-shut phase: hours or days where "
  "the future reads as finished and the body runs on fumes. Fading "
  "begins almost embarrassingly small: a decent meal, a laugh that "
  "escapes by accident, one task completed - and the forecast cracks a "
  "millimeter. The aftershock is the echo: weeks later a smell or a "
  "date on the calendar pulls the feeling back for an hour, weaker each "
  "time, like a bell rung once and left to quiet. The whole arc teaches "
  "the same lesson the archive repeats everywhere: feelings are "
  "weather, and weather moves."),
 "how_it_works": ("The timeline is the appraisal system learning and "
  "unlearning. Onset is the accumulation of bad evidence: each defeat "
  "deposits another stone on the scale until the forecast tips. The peak "
  "is a feedback loop: withdrawal stops new evidence, so the forecast "
  "has no competition and runs at full volume. Fading starts when any "
  "real counter-evidence gets through - a success, a kindness, a good "
  "night's sleep - and the forecast is forced to recalculate; each "
  "recalculation is slightly less dark. The aftershock is associative "
  "memory: the brain stored the peak alongside its surroundings, so "
  "similar surroundings replay a faint copy. Understanding this arc is "
  "practical, not just interesting: at onset, interrupt the evidence "
  "pile; at peak, borrow someone else's steadiness; during fading, feed "
  "the counter-evidence; at aftershock, name it as an echo and let it "
  "pass."),
 "key_points": [
  "Onset: defeats stack up (or one crushing blow), and the effort stops coming.",
  "Peak: the sealed-shut phase, running on fumes - the feedback loop at full volume.",
  "Fading: begins embarrassingly small - one meal, one laugh, one completed task.",
  "Aftershock: the echo weeks later, weaker each time, like a bell left to quiet.",
  "Every phase has its move: interrupt, borrow steadiness, feed evidence, name the echo."],
 "requirements": [
  "The four phases named and ordered: onset, peak, fading, aftershock.",
  "One practical move per phase, stated plainly.",
  "The weather metaphor carried through: phases move, nothing here is permanent."],
 "standards": [
  "Frijda on emotion episodes: feelings as processes with a temporal profile.",
  "Bonanno on resilience trajectories: most people recover their footing over time."],
 "citations": [CIT_FRIJDA, CIT_BONANNO, CIT_GROSS],
 "sig_lens": ("Through the Signature lens, the timeline is the archive's "
  "storm-tracking chart: onset plotted, peak measured, fading dated, "
  "aftershocks logged. The Signature archivist keeps the charts of a "
  "thousand storms because every one of them ended - and a library of "
  "ended storms is the strongest argument the archive owns that the "
  "current one will end too."),
},
{
 "key": "emde-low-high",
 "name": "Low despair versus high despair: two lived snapshots",
 "group": "inside-the-feeling",
 "ladder_rank": 3, "ladder_tier": "foundations",
 "description": ("Low despair, 3 out of 10: Maya misses the promotion "
  "again. She sits in her car for ten minutes, forehead on the steering "
  "wheel, and thinks 'I am never getting out of this role.' She still "
  "drives home, still eats dinner, still answers her sister's text with "
  "a joke that is only half forced. The thought is there but the life "
  "around it keeps moving; by Thursday a coworker's compliment lands and "
  "the forecast lifts a notch. High despair, 9 out of 10: the same Maya, "
  "six months later, after the layoff and the breakup in the same "
  "fortnight. She does not answer the texts. The apartment goes quiet "
  "and stays quiet. Getting up feels like lifting a car. She tells "
  "herself the story is over - not dramatically, just flatly, the way "
  "you state the weather. Her sister stops texting and starts driving "
  "over, because at 9 out of 10 the rule changes: you do not wait for "
  "the person to reach out, you go and sit in the room with them. Same "
  "emotion, different volume - and the volume decides everything about "
  "what helps."),
 "how_it_works": ("The two snapshots teach volume literacy: the same "
  "appraisal machinery at different gains. At 3 out of 10, the dark "
  "forecast is a whisper competing with a still-functioning life - "
  "routines hold, social contact continues, and small positive events "
  "still register and update the forecast. At 9 out of 10, the forecast "
  "is the only channel: routines have collapsed, contact has thinned, "
  "and the updating mechanism itself is starved of input. That is why "
  "advice that works at 3 ('take a walk, call a friend') can feel "
  "impossible at 9 - the machinery that would execute the advice is the "
  "very thing that is offline. The educational payload: always read the "
  "volume before choosing the response, in yourself and in others. Low "
  "volume wants gentle nudges; high volume wants presence, structure, "
  "and other people carrying the logistics for a while."),
 "key_points": [
  "At 3 out of 10 the dark thought whispers while life keeps moving around it.",
  "At 9 out of 10 the forecast is the only channel: routines and contact have collapsed.",
  "Advice that works at low volume can feel impossible at high volume.",
  "High volume changes the rule: do not wait for them to reach out - go and sit with them.",
  "Always read the volume first, in yourself and in others, then choose the response."],
 "requirements": [
  "Two concrete snapshots at named intensities, same person, different volume.",
  "The volume-reading rule stated as the takeaway.",
  "Warmth throughout: the high-volume snapshot must include someone showing up."],
 "standards": [
  "Frijda's intensity principle: same emotion, different action-readiness by gain.",
  "Keltner on social support as the co-regulation of intense emotion."],
 "citations": [CIT_FRIJDA, CIT_KELTNER, CIT_GROSS],
 "sig_lens": ("Through the Signature lens, the two snapshots are the "
  "archive's calibration cards: 3 and 9 held side by side so any reader "
  "can learn the gauge. The Signature archivist files them together "
  "because misreading the gauge is the costliest mistake in the whole "
  "collection - whisper advice shouted at a storm helps no one, but a "
  "sister driving over to sit in a quiet room has saved more forecasts "
  "than any speech ever has."),
},
{
 "key": "emde-dread-blend",
 "name": "Despair mixed with fear: the dread blend",
 "group": "inside-the-feeling",
 "ladder_rank": 3, "ladder_tier": "foundations",
 "description": ("Despair rarely travels alone, and its most common "
  "traveling companion is fear - the blend has its own name: dread. "
  "Pure despair says 'nothing will get better.' Pure fear says "
  "'something bad is coming.' Dread says both at once: 'something bad "
  "is coming and nothing will stop it.' It feels like standing in a "
  "hallway watching a door you cannot lock, too tired to run and too "
  "scared to sit down. The body runs two programs simultaneously: the "
  "despair program says shut down and conserve, while the fear program "
  "says stay alert and brace - so the person ends up exhausted AND "
  "wired, frozen AND trembling, the worst of both channels. This blend "
  "is the engine of the darkest hours of despair, because fear supplies "
  "the vivid worst-case movies while despair deletes the exits from "
  "every one of them. The way through is to split the blend: calm the "
  "body first (slow breath, warm hands, a steady voice nearby), because "
  "a calmer body starves the fear half - and fear half-starved is a "
  "blend half-undone."),
 "how_it_works": ("Blends work by running two appraisal programs at "
  "once. Despair's appraisal: the future holds no good path (certainty "
  "of badness). Fear's appraisal: a threat is approaching (uncertainty "
  "about when and how). Fused, they produce dread's signature: certain "
  "that it will be bad, uncertain about the shape of it - which is "
  "exactly the combination the imagination fills with the most lurid "
  "material. Physiologically the blend is a tug-of-war: despair drives "
  "parasympathetic shutdown (heaviness, stillness) while fear drives "
  "sympathetic arousal (tension, vigilance), and the body oscillates "
  "between them, which reads as jittery exhaustion. Splitting the blend "
  "is the practical move: the fear half responds to body-first calming "
  "because arousal is its fuel, and once the fear half quiets, what "
  "remains is plain despair - still heavy, but single-channeled and "
  "workable, with all the single-channel tools available."),
 "key_points": [
  "Dread is despair plus fear: 'something bad is coming and nothing will stop it.'",
  "The body runs shutdown and alarm at once: exhausted AND wired, frozen AND trembling.",
  "Fear supplies the worst-case movies; despair deletes the exits from every one.",
  "Split the blend: calm the body first, because arousal is the fear half's fuel.",
  "Fear half-starved leaves plain single-channel despair - heavy, but workable."],
 "requirements": [
  "The blend named (dread) and defined as despair plus fear.",
  "The tug-of-war body description: both programs at once.",
  "The split-the-blend move as the practical takeaway."],
 "standards": [
  "Plutchik's dyads: neighboring primaries fusing into named compounds.",
  "Izard on emotion interactions: blends as simultaneous activations."],
 "citations": [CIT_PLUTCHIK, CIT_IZARD, CIT_PANKSEPP],
 "sig_lens": ("Through the Signature lens, the dread blend is two "
  "archive wings filing at once - Loss and Threat running a joint "
  "operation. The Signature archivist's doctrine for joint operations "
  "is always the same: divide the file. Calm the Threat wing with "
  "body-first steadiness, and the Loss wing is left holding a single "
  "folder instead of a whole storm - and single folders can be worked, "
  "one page at a time."),
},
{
 "key": "emde-day",
 "name": "Despair through an ordinary day: a vignette",
 "group": "inside-the-feeling",
 "ladder_rank": 4, "ladder_tier": "foundations",
 "description": ("6:40 a.m. Daniel wakes before the alarm and stares at "
  "the ceiling, already tired. He skips the shower - what is the point, "
  "no one is coming - and eats cereal standing up. 9:00: at his desk he "
  "opens the job board, scrolls three listings, and closes the tab; "
  "applying feels like mailing letters to the ocean. 12:30: a coworker "
  "asks if he is okay and he says 'fine' a beat too fast, then feels "
  "guilty for lying and guilty for feeling guilty. 3:00 p.m.: the "
  "afternoon slump arrives like a tide; he does the minimum and watches "
  "the clock the way you watch a pot that will not boil. 6:00: home, "
  "the apartment dim; he means to cook and orders takeout instead, "
  "eating on the couch while the news plays to no one. 10:30: in bed, "
  "the day replays as evidence - see, nothing changed - and he falls "
  "asleep mid-verdict. But the archive notes what Daniel misses: he "
  "did get up, he did eat, he did answer the coworker, he did the "
  "minimum at work. The pilot light ran the whole day. Despair edits "
  "the footage to hide that - this record exists to put it back in."),
 "how_it_works": ("The vignette is a behavioral simulation in miniature: "
  "it walks despair through a normal day to show how the feeling edits "
  "reality. Each skipped action (shower, job board, cooking) is the "
  "shutdown of effort-pricing - the brain declining to spend energy on "
  "'pointless' tasks. The flat 'fine' is the mask (covered fully in "
  "record 16). The evening evidence-review is the forecast mechanism "
  "cherry-picking: it counts the closed tab and ignores the answered "
  "text, because forecasts protect themselves. The educational device "
  "is the archive's annotation: listing what Daniel actually did - got "
  "up, ate, worked, answered - against what despair told him he did "
  "(nothing). That gap, between the edited footage and the raw footage, "
  "is where every recovery starts: the day was not nothing, the "
  "forecast was just a harsh editor."),
 "key_points": [
  "Skipped small actions are the effort-pricing shutdown, not laziness.",
  "The evening evidence-review cherry-picks: it counts failures, hides the pilot light.",
  "Despair edits the footage; the archive's job is to restore the raw cut.",
  "He got up, ate, worked, answered - the day was not nothing.",
  "The gap between edited and raw footage is where every recovery starts."],
 "requirements": [
  "A full ordinary day in timestamped scenes, concrete and specific.",
  "The archive's annotation restoring what the feeling edited out.",
  "Ends with the recovery opening: the raw footage, not the edited cut."],
 "standards": [
  "Frijda on action readiness: emotion as the pricing of effort.",
  "Barrett on affective forecasting errors: the brain as a harsh editor."],
 "citations": [CIT_FRIJDA, CIT_BARRETT, CIT_GROSS],
 "sig_lens": ("Through the Signature lens, the day vignette is raw "
  "footage filed against the edited cut: Daniel's despair cut the "
  "shower, the job board, the cooking - and the Signature archivist "
  "restores every frame the feeling deleted. The archive keeps both "
  "versions because the comparison is the lesson: the forecast said "
  "nothing, the footage says he showed up all day. Trust the footage."),
},
{
 "key": "emde-body",
 "name": "What despair does in the body",
 "group": "body-signals",
 "ladder_rank": 4, "ladder_tier": "foundations",
 "description": ("Despair is not just a thought - it moves into the body "
  "and rearranges the furniture. The heart often feels heavy or slow "
  "rather than racing; some people describe a literal weight on the "
  "chest, as if the sternum is carrying something. Breathing goes "
  "shallow and sigh-heavy - the long exhale of someone who has stopped "
  "expecting the next breath to bring anything. Muscles lose their "
  "readiness: the jaw may hang slack, the hands go still in the lap, "
  "the legs feel like they belong to someone else. The stomach knots "
  "or goes numb, appetite swings toward nothing or toward constant "
  "grazing. Skin can feel cold or clammy; energy drains out through "
  "some invisible plug, leaving a tiredness that sleep does not fix. "
  "None of this is imagination - it is the conservation program "
  "running: the body budgeting every resource as if for a long winter. "
  "Knowing the signals matters because the body is the fastest way "
  "back in: you cannot always argue with the forecast, but you can "
  "always warm the hands, slow the breath, and stand up straight, and "
  "the body reports the change upstairs."),
 "how_it_works": ("The body of despair is the autonomic nervous system "
  "in deep-conservation mode. Where fear floods the body with fuel for "
  "action, despair does the opposite: sympathetic arousal dials down "
  "and the parasympathetic brake presses hard, producing the "
  "characteristic heaviness, slowness, and flatness. Shallow breathing "
  "follows from reduced metabolic demand and from the collapsed "
  "posture, which literally compresses the lungs - body and breath "
  "reinforce each other in a loop. The chest-weight sensation is "
  "interoceptive: the brain reading its own slowed cardiac and "
  "respiratory signals and narrating them as heaviness. Appetite and "
  "digestion shift because the gut is richly wired to emotional state. "
  "The practical leverage is that the loop runs both ways: deliberately "
  "changing the body - deeper breaths, upright posture, movement, "
  "warmth - sends new interoceptive data upward, and the appraisal "
  "system, which trusts the body more than it trusts arguments, "
  "recalculates. This is why body-first moves work when pep talks do "
  "not."),
 "key_points": [
  "Heavy chest, shallow sighing breath, slack muscles: the conservation program.",
  "Energy drains through an invisible plug; sleep does not seem to fix it.",
  "Collapsed posture compresses the lungs - body and breath reinforce each other.",
  "The gut shifts too: appetite swings toward nothing or toward constant grazing.",
  "The loop runs both ways: change the body and the appraisal recalculates."],
 "requirements": [
  "Heart, breath, muscles, stomach, skin, and energy each named concretely.",
  "The conservation-program explanation in plain words.",
  "The both-ways loop as the practical close."],
 "standards": [
  "Panksepp on affective neuroscience: emotion as whole-body state.",
  "Barrett on interoception: the brain reading the body and narrating it as feeling."],
 "citations": [CIT_PANKSEPP, CIT_BARRETT, CIT_IZARD],
 "sig_lens": ("Through the Signature lens, the body signals are the "
  "archive's instrument panel: heavy chest, shallow breath, slack "
  "muscles - every dial reading 'conservation mode.' The Signature "
  "archivist trusts instruments over arguments, which is why the "
  "doctrine is body-first: warm the hands, slow the breath, stand "
  "tall. Change the readings and the forecast has to file a "
  "correction - the panel, not the pep talk, moves the needle."),
},
{
 "key": "emde-posture",
 "name": "The posture and movement signature of despair",
 "group": "body-signals",
 "ladder_rank": 4, "ladder_tier": "foundations",
 "description": ("You can read despair in a silhouette. The head drops "
  "forward and slightly to the side, as if the neck has stopped "
  "volunteering. The shoulders roll in and up, guarding a chest that "
  "feels hollow. The spine curves into a question mark; the whole torso "
  "seems to be trying to take up less room in the world. Arms hang or "
  "fold tight across the middle - self-holding, the body's own attempt "
  "at comfort. Movement slows to the essential: short steps, minimal "
  "gesture, long stillnesses between actions, as if each motion has to "
  "be approved by a committee that keeps voting no. Sitting, the person "
  "sinks and spreads slightly, melting into the chair; standing, they "
  "lean on whatever is available - walls, counters, doorframes - "
  "borrowing structure from the world because their own feels spent. "
  "This posture is honest communication, evolved over millions of "
  "years: it tells the group 'I am down, I need the circle to close "
  "around me.'"),
 "how_it_works": ("Posture is emotion made visible through the "
  "musculoskeletal system, and despair's signature is maximal "
  "contraction and minimal extension. The flexor muscles win: head "
  "forward, shoulders in, spine curved - the body literally folding "
  "around its vital center, the ancient posture of an organism "
  "protecting itself while yielding. Movement slows because the "
  "action-readiness system has priced effort as worthless; every motion "
  "costs energy the budget office refuses to release. The leaning and "
  "the self-holding are compensations: seeking external support and "
  "self-soothing contact when internal resources run low. Darwin "
  "documented these serviceable habits as evolved signals, and modern "
  "research confirms the loop runs backward too - deliberately "
  "expanding the posture (chin up, shoulders back, chest open) feeds "
  "the brain evidence of readiness, which is why posture work is one "
  "of the oldest and most reliable levers against the feeling."),
 "key_points": [
  "Head dropped, shoulders in, spine curved: the body folding around its center.",
  "Movement slows to the essential; each motion waits on a committee voting no.",
  "Leaning on walls and self-holding: borrowing structure and comfort.",
  "The silhouette is honest signal: 'I am down, close the circle around me.'",
  "The loop runs backward: expanding the posture feeds readiness back to the brain."],
 "requirements": [
  "Head, shoulders, spine, arms, gait, sitting, and standing each described.",
  "The signal function of the posture stated plainly.",
  "The backward loop - posture as a lever - as the close."],
 "standards": [
  "Darwin on serviceable associated habits: posture as evolved emotional signal.",
  "Ekman on the body as a channel of emotional communication."],
 "citations": [CIT_DARWIN, CIT_EKMAN, CIT_FRIJDA],
 "sig_lens": ("Through the Signature lens, the posture signature is the "
  "archive's silhouette file: one folded shape, readable at fifty "
  "paces, saying 'close the circle.' The Signature archivist files it "
  "as a call, not a collapse - the body requesting the group - and "
  "notes the reverse entry in the margin: unfold the shape on purpose, "
  "chin up and chest open, and the instrument panel starts reporting "
  "readiness. The body files the first report; the mind reads it."),
},
{
 "key": "emde-sleep",
 "name": "Sleep, appetite, and energy under despair",
 "group": "body-signals",
 "ladder_rank": 4, "ladder_tier": "foundations",
 "description": ("Despair rearranges the three great rhythms: sleep, "
  "food, and energy. Sleep often breaks in one of two directions: the "
  "person cannot fall asleep because the flat inner commentary runs "
  "all night on repeat, or they sleep ten or twelve hours and wake "
  "unrefreshed, as if the night never filed its paperwork. Early "
  "morning is frequently the worst hour - the forecast delivers its "
  "darkest edition before the defenses are up. Appetite swings too: "
  "some people forget to eat entirely, the food going tasteless and "
  "the stomach uninterested; others graze constantly, reaching for "
  "whatever is sweet or salty for a flicker of sensation in a flat "
  "world. Energy is the cruelest shift: it is not the tiredness of a "
  "hard day's work but a drained-battery tiredness, where rest does "
  "not recharge and the simplest task feels priced like moving "
  "furniture. The archive's practical note is gentle but firm: guard "
  "the rhythms anyway. Regular meals, a fixed wake time, a short walk "
  "- these do not fix the feeling, but they keep the machinery from "
  "rusting while the feeling passes."),
 "how_it_works": ("Sleep, appetite, and energy are governed by "
  "interlocking regulatory systems - circadian, metabolic, and "
  "arousal - and despair perturbs all three. The flat rumination "
  "keeps cortical arousal high at bedtime (no sleep) or the "
  "conservation program extends sleep without restoring it (too much "
  "unrefreshing sleep), because the sleep is not serving recovery so "
  "much as escape. Appetite shifts follow the reward system going "
  "quiet: food loses its pleasure signal, so eating stops - or the "
  "person chases the few remaining strong signals, sugar and salt, "
  "for flickers of sensation. The drained-battery energy is "
  "motivational, not muscular: the muscles work fine, but the "
  "willingness-to-spend system is offline, so effort feels enormous. "
  "Guarding the rhythms works because these systems are "
  "self-stabilizing when given regular inputs: fixed wake times "
  "re-anchor the circadian clock, regular meals steady blood sugar "
  "and gut signaling, and movement - even a short walk - is the "
  "most reliable known reset for the arousal system."),
 "key_points": [
  "Sleep breaks two ways: flat commentary all night, or long sleep that never refreshes.",
  "Early morning is often the worst hour: the darkest forecast before defenses are up.",
  "Appetite swings to nothing or to constant grazing on strong sweet-salty signals.",
  "The tiredness is drained-battery, not hard-work tired: rest does not recharge it.",
  "Guard the rhythms anyway: fixed wake time, regular meals, a short walk."],
 "requirements": [
  "Sleep, appetite, and energy each given their two-direction treatment.",
  "The worst-hour note (early morning) included.",
  "The guard-the-rhythms guidance as the practical close."],
 "standards": [
  "Panksepp on the regulatory systems underlying mood and energy.",
  "Gross on behavioral regulation: stabilizing inputs to steady emotion."],
 "citations": [CIT_PANKSEPP, CIT_GROSS, CIT_BARRETT],
 "sig_lens": ("Through the Signature lens, sleep, food, and energy are "
  "the archive's three maintenance logs - and despair lets all three "
  "go unfilled. The Signature archivist's standing order is "
  "unromantic: fill the logs anyway. Fixed wake time, regular meals, "
  "a short walk - not because they fix the feeling, but because a "
  "machine under maintenance survives the storm that sinks the "
  "neglected one. Maintenance is not recovery; it is what makes "
  "recovery possible."),
},
{
 "key": "emde-differ",
 "name": "No two bodies feel despair the same way",
 "group": "body-signals",
 "ladder_rank": 5, "ladder_tier": "foundations",
 "description": ("Everything in the last three records is typical - "
  "and none of it is guaranteed. One person in despair goes still and "
  "silent; another gets restless, pacing the kitchen at midnight, "
  "unable to sit with the feeling. One loses all appetite; another "
  "eats everything in sight. One cries easily; another has not cried "
  "in years and feels the grief as a stone behind the eyes. One "
  "sleeps fourteen hours; another stares at the ceiling until dawn. "
  "Age changes it too: a teenager's despair may look like slammed "
  "doors and blasting music, an elder's like quiet withdrawal from "
  "the routines they kept for decades. Culture, temperament, health, "
  "history - all of it tunes the instrument differently. The archive "
  "insists on this because the most dangerous sentence about despair "
  "is 'you do not look despairing.' There is no single look. If the "
  "records describe a still, silent, sleepless heaviness and you meet "
  "someone pacing, tearless, and ravenous - trust the person in front "
  "of you, not the template."),
 "how_it_works": ("Individual variation in emotional response comes "
  "from the whole stack: genetics tunes baseline arousal and "
  "reactivity, personal history tunes which triggers fire hardest, "
  "culture tunes which expressions are permitted, and current "
  "physiology - illness, exhaustion, hormones - tunes the volume. "
  "Barrett's constructionist account puts it sharply: the brain "
  "builds each emotional episode from prediction plus body signals "
  "plus context, so no two constructions are identical even in the "
  "same person twice. Practically, this means every description in "
  "this archive is a map, and the person in front of you is the "
  "territory. The map is genuinely useful - it tells you what to "
  "look for and what questions to ask - but it never outranks the "
  "territory. When in doubt, ask the simple human question: 'what "
  "does it feel like for you right now' - and believe the answer."),
 "key_points": [
  "Still or restless, tearful or tearless, sleepless or oversleeping: all are real.",
  "Age, culture, temperament, health, and history all tune the instrument.",
  "There is no single look - 'you do not look despairing' is a dangerous sentence.",
  "The records are a map; the person in front of you is the territory.",
  "When in doubt: ask what it feels like for them, and believe the answer."],
 "requirements": [
  "At least four body-signal dimensions shown varying across people.",
  "The map-versus-territory rule stated plainly.",
  "The ask-and-believe guidance as the close."],
 "standards": [
  "Barrett on constructed emotion: every episode is built, never stamped.",
  "Izard on individual differences in emotional expression."],
 "citations": [CIT_BARRETT, CIT_IZARD, CIT_KELTNER],
 "sig_lens": ("Through the Signature lens, variation is the archive's "
  "anti-template rule: no entry is ever filed as 'the' way despair "
  "looks. The Signature archivist stamps every body-signal record "
  "with the same margin note - 'typical, not guaranteed' - because "
  "an archive that mistakes its map for the territory stops being a "
  "place of learning and becomes a place of misjudgment. Trust the "
  "person; consult the map."),
},
{
 "key": "emde-face",
 "name": "Reading the face of despair: eyes, brows, mouth",
 "group": "the-despair-face",
 "ladder_rank": 5, "ladder_tier": "compounded",
 "description": ("The face of despair is the saddest face the human "
  "repertoire holds, with fear's tension drawn through it. The eyes "
  "are the first tell: the gaze drops or goes unfocused, the upper "
  "lids lower as if the effort of looking has been declined, and "
  "sometimes the eyes glisten without quite crying - the grief "
  "present but dammed. The brows lift at the inner corners (the "
  "classic grief muscle) while the forehead stays oddly still, giving "
  "the whole brow a collapsed, inverted-V look. The mouth is the "
  "heaviest feature: the corners pull down and slightly outward, the "
  "lower lip may tremble or press flat, and in deep despair the jaw "
  "goes slack, the mouth hanging barely open as if speech itself has "
  "been cancelled. The micro-signs complete the portrait: a long "
  "slow blink, a swallow that has nothing to do with thirst, the "
  "nostrils flaring faintly on the inhale of a held-back sob. Held "
  "for seconds, this face is unmistakable - it is the look of a "
  "person watching the future close."),
 "how_it_works": ("Facial expression of emotion runs on dedicated "
  "muscle groups wired to affective state, and despair's face is a "
  "compound: the grief muscles (inner brow lift, mouth corners down) "
  "borrowed from sadness, plus the tension markers of fear (widened "
  "eye white at the peak, nostril flare). Darwin catalogued the "
  "grief muscles as serviceable habits - originally functional "
  "(protecting the eyes, wailing) and now pure signal - and Ekman's "
  "cross-cultural work confirmed the core components read the same "
  "worldwide. The slack jaw and unfocused gaze are the shutdown "
  "showing: the motor system idling, attention withdrawn from the "
  "visual field. The held-back-sob markers (swallow, nostril flare, "
  "trembling lip) are the interesting middle: the expression system "
  "trying to cry while the conservation program tries to stay still, "
  "and the conflict leaking out at the edges. For artists and actors "
  "(record 17) these micro-signs are the difference between a mask "
  "and a face."),
 "key_points": [
  "Eyes: gaze dropped or unfocused, lids lowered, sometimes glistening without crying.",
  "Brows: inner corners lifted, forehead still - the collapsed grief-brow.",
  "Mouth: corners down and out, lip trembling or pressed flat, jaw slack in deep despair.",
  "Micro-signs: the long slow blink, the purposeless swallow, the faint nostril flare.",
  "It is a compound face: sadness grief-muscles with fear's tension drawn through."],
 "requirements": [
  "Eyes, brows, mouth, and micro-signs each described concretely.",
  "The compound nature (sadness plus fear) named.",
  "Kept descriptive: a portrait, not a diagnosis."],
 "standards": [
  "Darwin on the grief muscles as evolved expressive habits.",
  "Ekman on the cross-cultural readability of the core components."],
 "citations": [CIT_DARWIN, CIT_EKMAN, CIT_IZARD],
 "sig_lens": ("Through the Signature lens, the face is the archive's "
  "frontispiece: grief-muscles plus fear-tension, the look of a "
  "future closing, readable worldwide without translation. The "
  "Signature archivist files it as the most honest page in the "
  "collection - the face cannot file a false report for long - and "
  "marks the micro-signs in red, because the smallest tells (the "
  "slow blink, the purposeless swallow) are where the truth lives."),
},
{
 "key": "emde-face-intensity",
 "name": "How the despair face changes with intensity",
 "group": "the-despair-face",
 "ladder_rank": 5, "ladder_tier": "compounded",
 "description": ("At low intensity the despair face is barely a face at "
  "all - a flicker. The mouth corners dip for half a second when the "
  "bad news lands, the gaze drops to the floor and comes back, the "
  "brows lift and settle. Most people miss it; a close friend catches "
  "it and asks 'what was that.' At moderate intensity the face "
  "settles in: the grief-brow holds, the mouth stays downturned, the "
  "eyes keep their unfocused middle distance, and the whole face "
  "seems to run at half brightness - expressions arrive late and "
  "leave early. Smiles, when they come, do not reach the eyes. At "
  "high intensity the face goes to its final form: slack jaw, hollow "
  "eyes, the brow collapsed, long stretches of complete stillness "
  "where the face seems to have stopped participating in being a "
  "face at all. Tears may come or may not - at the peak, even crying "
  "can feel like too much effort. The gradient matters for readers "
  "of faces: the flicker asks for a question, the settled face asks "
  "for company, the still face asks for someone to simply stay."),
 "how_it_works": ("Facial intensity tracks the underlying activation "
  "like a dimmer switch. At low activation only the fastest, most "
  "automatic components fire - the micro-flicker of the grief "
  "muscles before voluntary control catches up, which is why the "
  "low-intensity face is honest but brief. At moderate activation "
  "the expression becomes tonic: the muscles hold their positions, "
  "voluntary override weakens, and the 'half brightness' effect "
  "appears because the face's normal animation - the quick "
  "illustrators of speech and reaction - is damped by the "
  "conservation program. At high activation the system saturates: "
  "muscles either lock (the collapsed brow) or release entirely "
  "(the slack jaw), and voluntary expression effectively goes "
  "offline - hence the stillness. This is also why masking (record "
  "16) gets harder as intensity rises: the flicker can be covered "
  "with a quick smile, but the still face cannot be faked away, "
  "only waited out."),
 "key_points": [
  "Low: the flicker - half-second dip of the mouth, gaze drop and return.",
  "Moderate: the settled face - grief-brow held, half brightness, smiles that miss the eyes.",
  "High: the still face - slack jaw, hollow eyes, expression gone offline.",
  "At the peak even crying can feel like too much effort.",
  "The gradient tells readers what to do: question, company, or simply stay."],
 "requirements": [
  "Three intensity bands with distinct facial descriptions.",
  "The dimmer-switch mechanism in plain words.",
  "Each band paired with the response it asks for."],
 "standards": [
  "Ekman on the timing of genuine versus managed expression.",
  "Frijda on intensity as the gain on expressive behavior."],
 "citations": [CIT_EKMAN, CIT_FRIJDA, CIT_DARWIN],
 "sig_lens": ("Through the Signature lens, the intensity gradient is "
  "the archive's dimmer chart: flicker, settled, still - three "
  "readings on one dial. The Signature archivist teaches the chart "
  "because misreading it wastes the only currency that matters: "
  "the flicker wants a question, the settled face wants company, "
  "the still face wants a witness. Right reading, right response - "
  "that is the whole craft."),
},
{
 "key": "emde-masked",
 "name": "Hiding despair: the masked face and what leaks",
 "group": "the-despair-face",
 "ladder_rank": 6, "ladder_tier": "compounded",
 "description": ("People hide despair constantly - at work, at family "
  "dinners, in the checkout line - and the mask is almost always the "
  "same: the polite smile. But despair is a heavy mask to wear, and "
  "it leaks. The smile arrives a beat late and leaves a beat early. "
  "It does not reach the eyes: the lower lids stay flat instead of "
  "crinkling, giving the 'polite but absent' look. The voice is the "
  "second leak - flatter than the words warrant, with long pauses "
  "before answers, as if each sentence has to be hauled up from "
  "somewhere deep. The body leaks third: the smile says 'I am fine' "
  "while the shoulders stay rounded and the hands stay still. And "
  "then there are the unguarded moments - reaching for coffee, "
  "staring out a window, the second after the laugh fades - when "
  "the mask slips entirely and the real face shows for a heartbeat. "
  "The archive's note on masking is compassionate: people mask to "
  "protect others, to keep jobs, to survive the day. Do not rip the "
  "mask off. Notice the leak, remember it, and later, privately, "
  "ask the gentle question."),
 "how_it_works": ("Masking is voluntary control laid over automatic "
  "expression, and it is always partial because the two systems run "
  "on different wiring. The smile muscles (zygomatic major) take "
  "voluntary orders well, but the grief muscles (inner brow, "
  "depressor anguli oris) and the eye-crinkle muscles of a genuine "
  "smile are far less obedient - hence the smile that misses the "
  "eyes and the brow that will not quite stay down. Timing leaks "
  "because voluntary expressions have different onset and offset "
  "profiles than genuine ones: the beat-late arrival is the "
  "signature of something assembled rather than felt. The voice "
  "leaks because prosody - pitch, pace, melody - is governed "
  "largely below conscious control, and the conservation program "
  "flattens it regardless of the words. The unguarded-moment leak "
  "is attentional: maintaining a mask costs monitoring effort, and "
  "when attention goes elsewhere (the window, the coffee), the "
  "automatic face returns. All of this is why the kind response to "
  "a mask is never exposure - it is a later, private, gentle "
  "question."),
 "key_points": [
  "The mask is usually the polite smile - and despair makes it heavy to wear.",
  "Leak one: the smile misses the eyes; it arrives late and leaves early.",
  "Leak two: the voice flattens, with long hauling pauses before answers.",
  "Leak three: the body contradicts - 'fine' from the mouth, folded from the shoulders.",
  "Never rip the mask off: notice the leak, and ask the gentle question later, privately."],
 "requirements": [
  "The mask named (the polite smile) with at least three leak channels.",
  "The unguarded-moment phenomenon included.",
  "The compassionate response rule as the close."],
 "standards": [
  "Ekman on leakage: the channels voluntary control cannot fully govern.",
  "Gross on expressive suppression and its costs."],
 "citations": [CIT_EKMAN, CIT_GROSS, CIT_DARWIN],
 "sig_lens": ("Through the Signature lens, the masked face is a filed "
  "report with redactions - the smile is the redaction bar, and the "
  "leaks are the text showing through the marker. The Signature "
  "archivist is trained never to tear redactions open; you read "
  "what shows through, you note it, and you request the full file "
  "later, gently, in private. Dignity first, always - the archive "
  "collects truth, never at the cost of the person."),
},
{
 "key": "emde-drawing",
 "name": "Drawing despair: notes for artists and actors",
 "group": "the-despair-face",
 "ladder_rank": 6, "ladder_tier": "compounded",
 "description": ("For the artist: start with gravity. Everything in "
  "despair pulls downward - draw the brow's inner corners lifted but "
  "the whole face sinking, as if the features are sliding off the "
  "skull. Weight the lower lids; leave the eyes half-lidded and "
  "aimed at nothing. The mouth is your anchor: corners down and "
  "slightly out, the lower lip heavy, and in deep despair let the "
  "jaw hang a finger's width open - the most desolate line in the "
  "whole portrait. Keep the neck forward and the shoulders high "
  "and rounded; the figure should look like it is being poured "
  "slowly into the chair. Light it dimly from one side - despair "
  "does not do bright noon. For the actor: play the stillness, not "
  "the tears. Let the breath go shallow and audible through the "
  "nose. Answer questions a half-beat late, and let the eyes lose "
  "focus between lines - the audience reads unfocused eyes as a "
  "soul looking at a closed future. Do not perform sadness loudly; "
  "despair's horror is how quiet it is. The smallest gesture - one "
  "long slow blink, one purposeless swallow - will land harder "
  "than any wail."),
 "how_it_works": ("These notes work because they translate the "
  "mechanics into craft decisions. 'Everything pulls downward' is "
  "the flexor-dominance of the conservation program rendered as a "
  "drawing rule. The half-lidded unfocused eyes are attentional "
  "withdrawal made visible - the single most readable cue of a "
  "mind disengaged from the visual field. The slack jaw is motor "
  "idling: when the action system stands down, the jaw is the "
  "first visible release. For actors, the half-beat delay is "
  "processing lag - the appraisal system running slowly under "
  "conservation - and it reads as truth because audiences "
  "unconsciously know that timing. The 'play the stillness' "
  "direction is the core insight of the whole record: despair's "
  "signature is absence (of energy, of focus, of futurity), and "
  "absence is hardest to perform because performers want to add. "
  "The craft is subtraction: remove the animation, remove the "
  "focus, remove the future from the eyes - and the audience "
  "supplies the rest."),
 "key_points": [
  "Artist: gravity rules - features sliding downward, mouth as the anchor.",
  "The slack jaw, a finger's width open, is the most desolate line in the portrait.",
  "Light it dimly from one side: despair does not do bright noon.",
  "Actor: play the stillness, not the tears - half-beat delays, unfocused eyes.",
  "The craft is subtraction: remove animation, focus, futurity - the audience supplies the rest."],
 "requirements": [
  "Separate concrete notes for visual artists and for actors.",
  "At least five specific drawable/playable details.",
  "The subtraction principle as the closing insight."],
 "standards": [
  "Darwin's plates: the observational tradition of drawing emotion.",
  "Ekman on the minimal readable units of facial expression."],
 "citations": [CIT_DARWIN, CIT_EKMAN, CIT_IZARD],
 "sig_lens": ("Through the Signature lens, these notes are the "
  "archive's drafting manual: how to draw the undrawable and play "
  "the unplayable. The Signature archivist keeps them because "
  "despair must be recognizable to be reachable - a face the "
  "audience can read is a feeling the audience can meet. Draw it "
  "honestly, play it quietly, and let the subtraction do the "
  "work: the heaviest truths need the lightest hand."),
},
{
 "key": "emde-triggers",
 "name": "The classic triggers of despair",
 "group": "triggers",
 "ladder_rank": 6, "ladder_tier": "compounded",
 "description": ("Despair has a short list of classic triggers - the "
  "situations that set it off so reliably they are practically "
  "textbook. Repeated failure is the first: the job applications "
  "unanswered by the hundred, the treatments that do not take, the "
  "business kept alive month after month until the money and the "
  "hope run out together. Unbearable loss is the second: the death "
  "that rearranges the world, the relationship that was the plan "
  "for the whole future. Trapped circumstances are the third: the "
  "debt that cannot be outrun, the caregiving with no end date, the "
  "place you cannot leave and the situation you cannot change. "
  "Witnessed suffering is the fourth, quieter but real: watching "
  "someone you love sink and being unable to lift them. And the "
  "fifth is the pile-up: no single catastrophe, just one thing "
  "after another until the last small straw - a flat tire, a rude "
  "email - lands on a back already carrying everything. Knowing "
  "the list is protective: when you can name the trigger, the "
  "feeling stops being a verdict on your character and becomes "
  "what it is - a response to circumstances, and circumstances "
  "can change."),
 "how_it_works": ("Triggers work by feeding the appraisal system the "
  "evidence it needs to issue the dark forecast. Repeated failure "
  "supplies the pattern: the mind is a pattern-detector, and a "
  "dozen failures in a row is read as a law of nature, not a run "
  "of luck. Unbearable loss removes a load-bearing wall of the "
  "future - the person or plan the whole next decade was built "
  "around - and the forecast collapses with the structure. Trapped "
  "circumstances supply the 'no exit' premise: despair's forecast "
  "needs only two premises (it is bad; it cannot change), and a "
  "trap hands it the second one ready-made. The pile-up works by "
  "depleting the buffer: each small blow spends coping resources, "
  "and the final straw lands when the account is empty. The "
  "practical upshot is that triggers are also levers in reverse: "
  "break the pattern with one success, grieve the wall and rebuild, "
  "find one exit - any exit - in the trap, refill the buffer with "
  "rest and help. The forecast updates on evidence; change the "
  "evidence and the trigger loses its power."),
 "key_points": [
  "Repeated failure: the pattern-detector reads a dozen defeats as a law of nature.",
  "Unbearable loss: a load-bearing wall of the future comes down.",
  "Trapped circumstances: the trap hands the forecast its 'no exit' premise ready-made.",
  "The pile-up: no catastrophe, just an empty coping account and one last straw.",
  "Name the trigger and the feeling becomes a response to circumstances - which can change."],
 "requirements": [
  "Five classic triggers, each named and explained concretely.",
  "The appraisal-evidence mechanism underneath them.",
  "Each trigger paired with its reverse lever."],
 "standards": [
  "Lazarus on stress appraisal: triggers as person-environment transactions.",
  "Frijda on the eliciting conditions of emotion."],
 "citations": [CIT_LAZARUS, CIT_FRIJDA, CIT_BONANNO],
 "sig_lens": ("Through the Signature lens, triggers are the archive's "
  "case files: Failure-Pattern, Lost Wall, No-Exit, Witnessed "
  "Sinking, Empty Account. The Signature archivist files every "
  "trigger with its reverse lever attached - one success, one "
  "rebuilt wall, one exit, one rested helper, one refilled buffer "
  "- because a case file without a remedy is just a tragedy, and "
  "the archive files remedies, not tragedies."),
},
{
 "key": "emde-personal",
 "name": "Personal triggers: memories and anniversaries",
 "group": "triggers",
 "ladder_rank": 6, "ladder_tier": "compounded",
 "description": ("Beyond the classic list, everyone carries a private "
  "set of triggers wired to their own history. A song from the year "
  "everything fell apart. The smell of a hospital corridor. The date "
  "on the calendar when the news came - anniversaries are the most "
  "punctual triggers in the human repertoire, arriving on schedule "
  "whether invited or not. A street, a photograph, a phrase someone "
  "used to say: the brain stores the peak of despair alongside its "
  "surroundings, and the surroundings can replay a faint copy years "
  "later. These triggers confuse people because they seem "
  "'irrational' - why should a song flatten a whole afternoon - but "
  "there is nothing irrational about them: they are memory doing its "
  "job, filing by association. The archive's guidance is threefold: "
  "learn your own list (write it down; the written list is less "
  "scary than the ambush), plan for the punctual ones (the "
  "anniversary deserves a plan - company, a ritual, a walk - not a "
  "surprise), and greet the ambush ones with the sentence 'this is "
  "an echo, not a forecast.'"),
 "how_it_works": ("Personal triggers run on associative memory: the "
  "brain encodes emotional peaks together with their context - "
  "sounds, smells, dates, places - and later, encountering the "
  "context reactivates a trace of the feeling. This is the same "
  "machinery that makes a song summon a whole summer; despair just "
  "uses it for darker material. Anniversaries are especially potent "
  "because the calendar is a reliable retrieval cue and because the "
  "culture of remembrance (other people mentioning the date) "
  "reinforces it. The 'echo, not a forecast' sentence works as a "
  "cognitive label: naming the reactivation as memory rather than "
  "prediction changes the appraisal from 'it is happening again' to "
  "'I am remembering when it happened' - and the body, which "
  "responds to appraisal, stands down a notch. Planning for "
  "anniversaries works by replacing dreaded passivity with chosen "
  "structure: the day is going to come anyway; meeting it with a "
  "plan converts an ambush into an observance."),
 "key_points": [
  "Songs, smells, streets, phrases: the brain files peaks with their surroundings.",
  "Anniversaries are the most punctual triggers - they arrive on schedule.",
  "They are not irrational: they are memory filing by association, doing its job.",
  "Learn your list, plan for the punctual ones, greet ambushes as echoes.",
  "'This is an echo, not a forecast' - the sentence that stands the body down."],
 "requirements": [
  "Concrete examples of personal triggers across senses and dates.",
  "The associative-memory mechanism in plain words.",
  "The threefold guidance: list, plan, greet as echo."],
 "standards": [
  "Barrett on prediction and memory: the brain as a similarity-matcher.",
  "Bonanno on anniversary reactions in bereavement research."],
 "citations": [CIT_BARRETT, CIT_BONANNO, CIT_PANKSEPP],
 "sig_lens": ("Through the Signature lens, personal triggers are the "
  "archive's marginalia - handwritten notes in the reader's own "
  "hand, in invisible ink, appearing on schedule. The Signature "
  "archivist's rule for marginalia: read it, date it, plan for it. "
  "A trigger you have written down is a known file; a trigger that "
  "ambushes you is a stranger. The archive prefers known files - "
  "and it teaches every reader to keep their own list, because no "
  "archivist knows your shelves like you do."),
},
{
 "key": "emde-surprise",
 "name": "Surprise triggers: the odd little things",
 "group": "triggers",
 "ladder_rank": 7, "ladder_tier": "compounded",
 "description": ("Sometimes despair is set off by things that would "
  "sound absurd in a police report. A sitcom laugh track through a "
  "thin wall - everyone else laughing while you sit in the quiet. "
  "A child's birthday party glimpsed through a window. The smell "
  "of rain on hot pavement, because it rained the week it all fell "
  "apart. A stranger's kindness that breaks the dam precisely "
  "because it is undeserved. An empty chair at a table set for "
  "four. These triggers work by contrast or by ambush: contrast, "
  "because joy next door makes your own quiet feel louder; ambush, "
  "because the feeling was not braced and the guard was down. "
  "People often feel embarrassed by these - 'I fell apart over a "
  "laugh track' - and the archive is firm on this point: there is "
  "nothing to be embarrassed about. The small trigger is never "
  "the cause; it is the key turning in a lock that was already "
  "loaded. The feeling was waiting for any excuse. Blame the lock, "
  "not the key - and then, when the wave passes, oil the lock: "
  "rest, food, company, one small kind thing."),
 "how_it_works": ("Surprise triggers exploit two properties of the "
  "appraisal system: contrast amplification and unguarded "
  "processing. Contrast amplification is perceptual: the brain "
  "judges states relatively, so neighboring joy makes personal "
  "flatness feel flatter - the laugh track does not create the "
  "despair, it provides the bright background that makes the "
  "dark shape visible. Unguarded processing is attentional: "
  "defenses are routines, and routines have gaps - the stray "
  "smell, the accidental kindness - where the raw appraisal gets "
  "through before the coping commentary can dress it up. The "
  "'key in a loaded lock' metaphor is mechanistically accurate: "
  "the affective charge was already accumulated (the lock "
  "loaded), and the trivial cue merely releases it (the key "
  "turns). This is why the aftermath guidance targets the lock "
  "rather than the key: rest, food, company, and one small kind "
  "thing reduce the accumulated charge, so the next stray key "
  "finds less to release."),
 "key_points": [
  "Laugh tracks, birthday parties, rain-smell, empty chairs: the absurd-sounding triggers.",
  "Contrast: neighboring joy makes your own quiet feel louder.",
  "Ambush: the guard was down, so the raw appraisal got through undressed.",
  "The small trigger is the key, never the cause - the lock was already loaded.",
  "Blame the lock, not the key; then oil the lock: rest, food, company, one kind thing."],
 "requirements": [
  "At least five concrete odd-little triggers.",
  "The contrast and ambush mechanisms explained.",
  "The key-versus-lock metaphor with the no-embarrassment rule."],
 "standards": [
  "Frijda on the micro-conditions that release accumulated affect.",
  "Barrett on contrast effects in constructed feeling."],
 "citations": [CIT_FRIJDA, CIT_BARRETT, CIT_IZARD],
 "sig_lens": ("Through the Signature lens, surprise triggers are the "
  "archive's misfiled keys: tiny, absurd, found in the wrong "
  "drawer - a laugh track, a rain-smell - each one opening a "
  "vault it had no business opening. The Signature archivist "
  "files them under Loaded Locks, with the standing note: never "
  "blame the key. Oil the lock instead - rest, food, company, "
  "one small kind thing - and the next stray key will turn in "
  "an empty chamber."),
},
{
 "key": "emde-chains",
 "name": "Chain reactions: when despair pulls other emotions along",
 "group": "triggers",
 "ladder_rank": 7, "ladder_tier": "compounded",
 "description": ("Despair is a chain-reaction emotion: it rarely "
  "arrives alone and it never leaves the other feelings untouched. "
  "The classic cascade runs like this: a trigger lands (the "
  "rejection letter), sadness answers (the loss), fear joins (what "
  "now), and the two fuse into despair (nothing will ever work). "
  "Then despair starts recruiting: shame arrives ('everyone else "
  "manages'), anger flares at the self or the world ('this is "
  "unfair'), guilt piles on ('I should have tried harder'), and "
  "loneliness settles over the whole pile like dust ('no one "
  "understands'). Each new emotion feeds the forecast: shame says "
  "you are the problem, anger says the world is the problem, guilt "
  "says the past is the problem - and despair nods along to all "
  "three, because every problem with no solution is more evidence "
  "for the verdict. The way to break a cascade is to stop arguing "
  "with the whole chain and pick one link: usually the body link "
  "(move, breathe, eat) or the company link (one person, one "
  "honest sentence). Chains break at their weakest link, not "
  "their loudest."),
 "how_it_works": ("Emotional cascades run on appraisal spillover: "
  "one appraisal ('I have failed') activates adjacent appraisals "
  "('I am failing as a person' - shame; 'I was wronged' - anger; "
  "'I caused this' - guilt), each with its own bodily and "
  "behavioral program. The programs interfere: shame wants hiding, "
  "anger wants confrontation, despair wants stillness - and the "
  "person oscillates, exhausted, between incompatible urges. "
  "Meanwhile each emotion's evidence-feeding serves despair's "
  "forecast: shame, anger, and guilt all narrate unsolvable "
  "problems, which is exactly the premise despair needs. "
  "Interrupting at a single link works because cascades are "
  "multiplicative: remove one factor and the product shrinks "
  "disproportionately. The body link is usually weakest because "
  "it is the least cognitive - you cannot argue a cascade out "
  "of itself, but you can walk, breathe, and eat, and the "
  "physiology that funds all the appraisals shifts underneath "
  "them."),
 "key_points": [
  "The classic cascade: trigger to sadness to fear to fused despair.",
  "Then the recruits: shame, anger, guilt, loneliness - each feeding the forecast.",
  "The programs clash: hide, confront, lie still - oscillation exhausts.",
  "Every unsolvable problem narrated is more evidence for the verdict.",
  "Break the weakest link, not the loudest: usually the body link or the company link."],
 "requirements": [
  "The full cascade named step by step from trigger through recruits.",
  "The incompatible-urges exhaustion explained.",
  "The weakest-link intervention as the close."],
 "standards": [
  "Lazarus on appraisal spillover across emotion episodes.",
  "Izard on emotion-emotion interactions in complex states."],
 "citations": [CIT_LAZARUS, CIT_IZARD, CIT_FRIJDA],
 "sig_lens": ("Through the Signature lens, cascades are chain "
  "lightning: trigger, sadness, fear, despair, then shame, anger, "
  "guilt, loneliness - each bolt calling the next. The Signature "
  "archivist does not chase lightning; she grounds one rod. One "
  "walk, one breath pattern, one honest sentence to one person - "
  "ground a single link and the whole storm has nowhere to "
  "complete its circuit. File under: weakest link, not loudest."),
},
{
 "key": "emde-actions",
 "name": "What people do when despair visits",
 "group": "behavior",
 "ladder_rank": 7, "ladder_tier": "compounded",
 "description": ("Despair has a behavioral signature as readable as "
  "its face. People withdraw: they cancel plans, stop answering "
  "messages, let the dishes stack and the laundry sit - not from "
  "laziness but because every action feels priced in a currency "
  "they no longer hold. They stop starting things: the applications "
  "unsent, the calls unmade, the projects abandoned mid-sentence. "
  "Routines erode from the edges inward - first the optional joys "
  "(the hobby, the walk), then the maintenance (the shower, the "
  "cooking), until only the unavoidable remains. Some people "
  "signal: the vague late-night message, the 'I am fine' that "
  "invites a second question, the sudden giving away of things - "
  "these are flares, not manipulations, and they deserve an "
  "answer. Others go very still, conserving everything, waiting. "
  "The archive reads all of this as communication, not failure: "
  "withdrawal says 'I cannot carry this alone,' stopping says 'the "
  "effort-pricing is broken,' and the flare says 'please notice.' "
  "Each behavior is a sentence in the language of despair - and "
  "every sentence is asking for a reply."),
 "how_it_works": ("Despair's behaviors are the action-readiness "
  "system running its shutdown program. Withdrawal is "
  "stimulus-reduction: fewer inputs means fewer demands on an "
  "empty budget. Stopping new efforts is effort-pricing: the "
  "brain declines to invest where the forecast says the return "
  "is zero. Routine erosion follows a triage logic - the "
  "conservation program cuts discretionary spending first (joys), "
  "then maintenance, preserving only survival essentials - which "
  "is why the state of someone's kitchen can be a despair "
  "barometer. Signaling behaviors (the vague message, the "
  "invited second question) are the attachment system still "
  "functioning inside the shutdown: the oldest human program - "
  "cry out and the group comes - running on its last battery. "
  "Reading these as communication rather than failure changes "
  "the response completely: you do not scold a flare, you "
  "answer it; you do not lecture the shutdown, you sit inside "
  "it with the person until the pricing comes back online."),
 "key_points": [
  "Withdrawal: canceling, silencing, letting the dishes stack - stimulus reduction.",
  "Stopping: applications unsent, calls unmade - the effort-pricing is broken.",
  "Erosion runs triage: joys first, then maintenance, survival last.",
  "Signals are flares, not manipulations: the vague message invites a second question.",
  "Read it all as communication: every behavior is a sentence asking for a reply."],
 "requirements": [
  "Withdrawal, stopping, erosion, signaling, and stillness each described.",
  "The effort-pricing and triage mechanisms in plain words.",
  "The communication-not-failure reframe as the close."],
 "standards": [
  "Frijda on action readiness and its shutdown in hopeless states.",
  "Keltner on the social-signal function of emotional behavior."],
 "citations": [CIT_FRIJDA, CIT_KELTNER, CIT_PANKSEPP],
 "sig_lens": ("Through the Signature lens, despair behaviors are "
  "dispatches from a besieged station: withdrawal (reducing "
  "incoming fire), stopping (conserving ammunition), erosion "
  "(triage), flares (signaling for relief). The Signature "
  "archivist reads every dispatch as written, never as failure "
  "- and the doctrine for flares is absolute: you answer a "
  "flare. Always. That is what the archive is for."),
},
{
 "key": "emde-voice",
 "name": "What people say: the voice of despair",
 "group": "behavior",
 "ladder_rank": 7, "ladder_tier": "compounded",
 "description": ("Despair has a vocabulary, and once you know it you "
  "hear it everywhere. The signature phrases are all verdicts "
  "about the future: 'what is the point,' 'it will never work,' "
  "'nothing ever changes,' 'I am done trying.' Note the grammar: "
  "absolute words (never, nothing, always), future tense, passive "
  "construction - the language of a forecast, not a report. The "
  "tone carries more than the words: flat, slow, quiet, with long "
  "pauses between sentences, as if each one has to be hauled up "
  "from a well. Questions go unasked - despair does not inquire, "
  "it concludes. And there is the deflection vocabulary for when "
  "others ask: 'I am fine,' 'do not worry about me,' 'it is what "
  "it is' - each one a small locked door. The archive teaches "
  "two listening skills: first, hear the absolutes as the "
  "feeling talking ('never' is despair's favorite word, and it "
  "is almost always wrong); second, hear the locked doors as "
  "invitations, not rejections - 'do not worry about me' usually "
  "means 'worry about me, but gently, and do not make a scene.'"),
 "how_it_works": ("The language of despair is the forecast mechanism "
  "speaking out loud. Absolutes (never, nothing, always) are "
  "overgeneralization: the appraisal system taking a sample of "
  "failures and promoting it to a law - a known cognitive pattern "
  "in hopeless states. Future-tense verdicts ('it will never "
  "work') reveal the temporal orientation that distinguishes "
  "despair from sadness: the claim is about tomorrow, not "
  "yesterday. The flat prosody - slow, quiet, monotone - is the "
  "conservation program damping the vocal apparatus: pitch "
  "variation costs energy, and the budget office has cut it. "
  "Deflection phrases are protective scripts: they end the "
  "conversation before the mask has to work too hard, which is "
  "why pushing against them directly backfires. The listening "
  "skills work because they address the mechanism: challenging "
  "the absolute ('never? not once?') forces the forecast to "
  "produce evidence it does not have, and treating locked doors "
  "as invitations respects the protection while still walking "
  "through, gently."),
 "key_points": [
  "Signature phrases are future-tense verdicts: 'what is the point,' 'it will never work.'",
  "The grammar gives it away: absolutes (never, nothing), future tense, passive voice.",
  "Tone: flat, slow, quiet, long pauses - pitch variation cut by the budget office.",
  "Deflections are locked doors: 'I am fine' usually means 'worry gently.'",
  "Listen twice: hear absolutes as the feeling talking, and locked doors as invitations."],
 "requirements": [
  "Characteristic phrases quoted verbatim.",
  "Grammar, tone, and deflection vocabulary each covered.",
  "The two listening skills as the practical close."],
 "standards": [
  "Lazarus on the cognitive content of emotion: language as appraisal made audible.",
  "Ekman on vocal prosody as an emotional channel."],
 "citations": [CIT_LAZARUS, CIT_EKMAN, CIT_BARRETT],
 "sig_lens": ("Through the Signature lens, the voice of despair is "
  "the forecast read aloud: absolutes for adjectives, future "
  "tense for grammar, flat prosody for music. The Signature "
  "archivist is trained in forecast-auditing - 'never? show me "
  "the evidence' - because every absolute is a claim the feeling "
  "cannot prove. Audit the verbs, and the verdict starts to "
  "wobble; keep auditing, and the future reopens a crack."),
},
{
 "key": "emde-decisions",
 "name": "How despair colors decisions and judgment",
 "group": "behavior",
 "ladder_rank": 8, "ladder_tier": "compounded",
 "description": ("Despair is a terrible financial advisor, and it "
  "advises on everything. Under its influence, people systematically "
  "misjudge in three directions. First, they underprice their own "
  "agency: options that exist are read as unavailable, help that "
  "would come is assumed unwilling, doors that are open are seen "
  "as painted on. Second, they overprice costs: every effort feels "
  "enormous, every risk feels fatal, every first step feels like "
  "climbing a cliff. Third, they foreshorten time: the future "
  "collapses to the next few miserable days, so long-term goods "
  "(health, skills, relationships) get traded away for immediate "
  "relief or simply abandoned. The result is decisions that look "
  "irrational from outside - quitting the course with one exam "
  "left, refusing the interview, pushing away the friend - but "
  "are perfectly rational inside the forecast: if nothing will "
  "work, conserving the last of your energy is the smart play. "
  "The archive's rule for big decisions in despair: postpone what "
  "you can, shrink what you cannot, and borrow someone else's "
  "judgment for the rest - because the forecast is a biased "
  "witness and should not testify alone."),
 "how_it_works": ("The judgment shifts are the appraisal system "
  "doing its job with corrupted inputs. Underpriced agency is "
  "learned non-reward: after enough failures, the brain's "
  "expected-value calculator assigns near-zero probability to "
  "success, so rationally - given its numbers - it declines to "
  "invest. Overpriced cost is the conservation program's doing: "
  "when the energy budget reads empty, the subjective cost of "
  "effort inflates, the same way a hill looks steeper when you "
  "are tired. Foreshortened time is attentional narrowing: the "
  "mind can only simulate a few days ahead because simulating "
  "further ahead returns only darkness, so it stops trying. "
  "Together they form a coherent but wrong decision engine - "
  "wrong because its inputs (the forecast) are wrong. The "
  "postpone-shrink-borrow rule works by refusing to let the "
  "biased witness testify alone: postponing lets the forecast "
  "age out, shrinking reduces the stake to something the "
  "corrupted calculator can still approve, and borrowing "
  "judgment imports someone else's uncorrupted numbers."),
 "key_points": [
  "Agency gets underpriced: open doors read as painted on.",
  "Costs get overpriced: every first step feels like a cliff.",
  "Time gets foreshortened: long-term goods traded for immediate relief.",
  "The decisions are rational inside the forecast - which is exactly the problem.",
  "The rule: postpone what you can, shrink the rest, borrow judgment for big calls."],
 "requirements": [
  "The three misjudgment directions named with concrete examples.",
  "The inside-the-forecast rationality explained.",
  "The postpone-shrink-borrow rule as the close."],
 "standards": [
  "Lazarus on appraisal-driven choice: decisions follow the forecast.",
  "Frijda on action readiness as the economics of effort."],
 "citations": [CIT_LAZARUS, CIT_FRIJDA, CIT_GROSS],
 "sig_lens": ("Through the Signature lens, despair's judgment is a "
  "calculator with corrupted inputs: agency underpriced, costs "
  "overpriced, time foreshortened - every sum correct, every "
  "input wrong. The Signature archivist never lets a corrupted "
  "calculator sign the big contracts: postpone, shrink, borrow. "
  "Let the numbers sit, cut the stake, import clean figures "
  "from someone whose forecast is not running dark. File under: "
  "biased witness, do not testify alone."),
},
{
 "key": "emde-escalation",
 "name": "When despair intensifies: how behavior escalates",
 "group": "behavior",
 "ladder_rank": 8, "ladder_tier": "compounded",
 "description": ("Despair escalates along a readable ladder, and "
  "knowing the rungs lets people intervene early. Rung one is "
  "quiet quitting on life's extras: the hobby shelved, the friends "
  "seen less, the small pleasures declined. Rung two is maintenance "
  "collapse: hygiene slips, meals get skipped, the apartment tells "
  "the story. Rung three is social disappearance: messages "
  "unanswered for days, the phone face-down, the world receding "
  "behind a door that stays closed. Rung four is the verbal "
  "verdict: 'I am done,' 'there is no point anymore' - the "
  "forecast stated as fact, often to whoever is closest. Rung five "
  "is the flare: the vague alarming message, the sudden giving "
  "away of prized things, the goodbye that does not sound like "
  "see-you-later. Each rung is a louder signal, and each deserves "
  "a stronger answer: rung one wants a nudge and an invitation, "
  "rung three wants someone showing up at the door, rung five "
  "wants immediate human presence - stay with the person, call "
  "for help together, do not leave them alone with the verdict. "
  "The archive is direct here: escalation is communication getting "
  "louder because quieter signals were missed. Answer early and "
  "you rarely meet the later rungs."),
 "how_it_works": ("Escalation is the signaling system turning up its "
  "volume as earlier signals fail to get a response. This is "
  "straight attachment logic: the organism signals distress, "
  "waits, and if no relief comes, signals louder - the same "
  "program that makes a baby's fuss become a wail. Each rung "
  "also reflects deepening conservation: as the forecast "
  "darkens, the triage cuts deeper, from discretionary joys to "
  "maintenance to social contact itself. The verbal verdict at "
  "rung four is significant mechanistically: stating the "
  "forecast aloud recruits social reality - saying 'I am done' "
  "to a witness makes it feel more final, which is why the "
  "witness's response matters so much. The flare at rung five "
  "is the attachment system spending its last battery: an "
  "all-or-nothing bid for the group to close in. The matched "
  "response ladder works because it answers the signal at the "
  "volume it is sent: under-answering teaches the system to "
  "shout louder next time; answering at volume teaches it that "
  "quieter signals suffice."),
 "key_points": [
  "Rung one: the extras go - hobbies shelved, pleasures declined.",
  "Rung three: social disappearance - the world behind a closed door.",
  "Rung five: the flare - the attachment system spending its last battery.",
  "Each rung deserves a stronger answer: nudge, show up, stay - never leave them alone.",
  "Escalation is missed quiet signals getting louder: answer early."],
 "requirements": [
  "Five rungs named in order with concrete behaviors.",
  "The matched response ladder paired rung by rung.",
  "The direct close: answer early, never leave them alone at the flare."],
 "standards": [
  "Panksepp on the attachment and panic systems: signaling as biology.",
  "Keltner on escalating social signals and their co-regulation."],
 "citations": [CIT_PANKSEPP, CIT_KELTNER, CIT_FRIJDA],
 "sig_lens": ("Through the Signature lens, escalation is the "
  "distress beacon turning up its wattage: extras, maintenance, "
  "disappearance, verdict, flare - five power settings, each one "
  "louder because the last went unanswered. The Signature "
  "archivist's standing order is to answer beacons at the power "
  "they are sent, early and at volume - because a beacon "
  "answered at rung one never has to reach rung five, and no "
  "signal in this archive goes unanswered on purpose."),
},
{
 "key": "emde-healthy",
 "name": "Expressing despair in healthy ways",
 "group": "healthy-expression",
 "ladder_rank": 8, "ladder_tier": "advanced",
 "description": ("Despair needs an exit, and the healthy exits are "
  "well mapped. The first is naming it out loud to someone safe: "
  "'I feel like nothing will ever get better' - said plainly, "
  "without apology, to a person who will not flinch. Naming moves "
  "the feeling from weather-you-are-inside to weather-you-are-"
  "watching, and that distance is the beginning of leverage. The "
  "second is writing it unedited: the unsent letter, the 3 a.m. "
  "page, the list of everything that feels finished - externalized, "
  "the forecast has to show its work, and it rarely survives the "
  "showing. The third is channeling it into making: despair has "
  "produced some of humanity's most honest art, music, and building "
  "- the feeling wants to say the future is closed, and making "
  "something is a live demonstration that it is not. The fourth is "
  "asking for specific help: not 'fix my life' but 'sit with me "
  "Thursday' or 'help me make the call' - despair generalizes, so "
  "recovery specifies. None of these require feeling better first; "
  "that is the whole point. Expression is not the reward for "
  "recovery. Expression is the road."),
 "how_it_works": ("Healthy expression works by breaking the "
  "forecast's monopoly on the narrative. Naming it aloud "
  "recruits the prefrontal cortex into labeling the affect, "
  "which measurably reduces its intensity - the 'name it to tame "
  "it' effect is one of the best-replicated findings in emotion "
  "science. Writing externalizes the forecast: on paper, the "
  "absolutes ('never,' 'nothing') become visible claims that can "
  "be audited, and the audit usually fails. Making something "
  "is behavioral counter-evidence: the hands producing a real "
  "thing contradicts the premise that nothing can come of "
  "effort, and the contradiction updates the forecast from "
  "below, bypassing argument entirely. Specific help-seeking "
  "works by reversing despair's generalization: the feeling "
  "says 'everything is impossible,' and one completed specific "
  "request ('she sat with me Thursday') is a fact the "
  "generalization cannot digest. All four share the mechanism: "
  "feed the system something real, and the forecast must file "
  "a correction."),
 "key_points": [
  "Name it aloud to someone safe: from weather-you-are-inside to weather-you-watch.",
  "Write it unedited: on paper the forecast has to show its work, and rarely survives.",
  "Make something: the hands producing a real thing contradicts the closed future.",
  "Ask specifically: 'sit with me Thursday' beats 'fix my life' - recovery specifies.",
  "Expression is not the reward for recovery; expression is the road."],
 "requirements": [
  "Four healthy exits named with concrete forms.",
  "The mechanism under each stated plainly.",
  "The road-not-reward line as the close."],
 "standards": [
  "Gross on reappraisal and affect labeling: naming reduces intensity.",
  "Keltner on the social sharing of emotion as regulation."],
 "citations": [CIT_GROSS, CIT_KELTNER, CIT_BARRETT],
 "sig_lens": ("Through the Signature lens, healthy expression is the "
  "archive's pressure-valve system: name it, write it, make it, "
  "ask it - four valves, each one releasing the forecast's "
  "monopoly a notch. The Signature archivist maintains the "
  "valves the way engineers maintain steam plants: not because "
  "pressure is shameful, but because unvented pressure breaks "
  "vessels. Expression is maintenance. The archive runs on it."),
},
{
 "key": "emde-costly",
 "name": "Bottling it up or blowing up: the two costly exits",
 "group": "healthy-expression",
 "ladder_rank": 9, "ladder_tier": "advanced",
 "description": ("When despair cannot find a healthy exit, it takes "
  "one of two costly ones. Bottling it up looks like functioning: "
  "the person goes to work, smiles at the meetings, says 'fine' - "
  "and inside, the pressure builds with nowhere to go. The costs "
  "arrive on schedule: the sleep breaks, the body aches with no "
  "clear cause, the temper shortens, and one day a tiny slight "
  "detonates a reaction ten times its size because it was never "
  "about the slight. Blowing up is the other exit: the despair "
  "converts to sudden fury - at the partner, the kids, the "
  "stranger in traffic - because anger is despair with the "
  "conservation program momentarily overridden, and fury at least "
  "feels like energy. The costs here are relational: the people "
  "who could have helped get pushed away, and then the despair "
  "points at the empty room as proof that no one cares. Both exits "
  "share the same flaw: they skip the middle, where the feeling "
  "is named and met. The archive's verdict is plain: bottling "
  "rusts you from the inside, exploding burns the bridges you "
  "will need. Take the middle road - it is the only one with a "
  "destination."),
 "how_it_works": ("Bottling is expressive suppression: the voluntary "
  "system clamps down on the expression while the feeling "
  "continues underneath. Research shows suppression does not "
  "reduce the feeling - it increases physiological strain, "
  "because the body pays for both the emotion and the effort "
  "of hiding it. The detonations are pressure physics: the "
  "accumulated, unprocessed affect lowers the threshold for "
  "everything, so a minor trigger releases the stored charge. "
  "Blowing up is affect conversion: despair's shutdown is "
  "unstable, and when the conservation program momentarily "
  "fails, the stored arousal discharges as anger - which is "
  "why the fury feels energizing and then leaves the person "
  "emptier. The relational cost is a feedback loop: pushing "
  "helpers away removes the exact input (company, evidence) "
  "that would update the forecast, so the forecast darkens, "
  "so the next explosion comes sooner. The middle road - "
  "naming and meeting the feeling - is the only exit that "
  "processes rather than stores or discharges."),
 "key_points": [
  "Bottling looks like functioning while pressure builds with nowhere to go.",
  "Suppression does not reduce the feeling; it charges the body for the hiding too.",
  "Blowing up is despair converting to fury - energizing for a minute, emptier after.",
  "Explosions push helpers away, and the empty room becomes 'proof' no one cares.",
  "Bottling rusts from the inside; exploding burns the bridges. Take the middle road."],
 "requirements": [
  "Both costly exits described with their characteristic look and costs.",
  "The suppression-strain and conversion mechanisms in plain words.",
  "The middle-road verdict as the close."],
 "standards": [
  "Gross on expressive suppression: the physiology of bottling.",
  "Frijda on affect conversion and discharge dynamics."],
 "citations": [CIT_GROSS, CIT_FRIJDA, CIT_IZARD],
 "sig_lens": ("Through the Signature lens, the two costly exits are "
  "the archive's condemned routes: Bottling (pressure with no "
  "valve) and Detonation (bridges burned for a minute of false "
  "energy). The Signature archivist posts the warning at the "
  "trailhead in plain paint: rust from the inside, or ash where "
  "the bridges were - pick the middle road. It is the only "
  "route in the collection with a destination marked."),
},
{
 "key": "emde-practices",
 "name": "Small everyday practices for balance",
 "group": "healthy-expression",
 "ladder_rank": 9, "ladder_tier": "advanced",
 "description": ("Balance against despair is not built in "
  "breakthroughs; it is built in small daily practices, the way a "
  "wall is built in bricks. Keep one morning anchor: get up at the "
  "same time, make the bed, step outside for two minutes of sky - "
  "despair hates routine because routine is proof the day has a "
  "shape. Do one completable thing daily: wash the dishes, walk "
  "around the block, answer one email - finished tasks are "
  "counter-evidence the forecast cannot digest. Keep one human "
  "contact warm: the daily text, the Thursday coffee, the neighbor "
  "nod - connection is the forecast's natural enemy. Move the body "
  "a little every day: the research on movement and mood is among "
  "the sturdiest in the field, and a twenty-minute walk has "
  "outperformed many a pep talk. Write three honest lines at night: "
  "what hurt, what helped, what is one small thing for tomorrow - "
  "the archive in miniature, kept daily. And the standing rule "
  "underneath them all: when despair feels very heavy or stays a "
  "long time, reaching out to trusted people - and to a counselor "
  "or professional - is a strong and ordinary move, not a last "
  "resort. Practices do not erase the feeling. They build the "
  "scaffolding it cannot knock down."),
 "how_it_works": ("Practices work through accumulation and "
  "regularization. A morning anchor re-establishes circadian and "
  "behavioral rhythm, which the conservation program had "
  "dissolved; rhythm is the opposite of the formless drift "
  "despair prefers. Completable tasks exploit the completion "
  "effect: each finished task deposits a unit of "
  "counter-evidence ('I did a thing; things can be done') that "
  "the generalization 'nothing works' cannot absorb without "
  "cracking. Warm contact maintains the attachment system's "
  "baseline, preventing the isolation spiral that starves the "
  "forecast of competing data. Movement shifts arousal and "
  "interoceptive signaling directly - the body reporting "
  "upward that energy exists. The nightly three lines are a "
  "micro-archive: externalizing the day prevents the evening "
  "evidence-review from cherry-picking, because the written "
  "record includes what helped. None of this argues with "
  "despair; all of it out-builds it, brick by brick, until the "
  "scaffolding stands whether the feeling likes it or not."),
 "key_points": [
  "One morning anchor: same wake time, made bed, two minutes of sky.",
  "One completable thing daily: finished tasks are counter-evidence.",
  "One warm contact kept: connection is the forecast's natural enemy.",
  "Move daily: a twenty-minute walk outperforms many a pep talk.",
  "When it feels very heavy or stays long, reaching a counselor is strong and ordinary."],
 "requirements": [
  "Five concrete daily practices, each specific enough to do tomorrow.",
  "The mechanism under each in plain words.",
  "The professional-support line stated as strong and ordinary, never as last resort."],
 "standards": [
  "Gross on behavioral activation: action preceding motivation.",
  "Bonanno on the everyday mechanics of resilience."],
 "citations": [CIT_GROSS, CIT_BONANNO, CIT_PANKSEPP],
 "sig_lens": ("Through the Signature lens, practices are the "
  "archive's maintenance schedule: morning anchor, one finished "
  "task, one warm contact, daily movement, three honest lines - "
  "filed under Scaffolding, serviced daily. The Signature "
  "archivist trusts schedules over moods, because moods are "
  "weather and schedules are architecture. Build the "
  "scaffolding brick by brick, and the storm can howl all it "
  "wants: the structure stands."),
},
{
 "key": "emde-reading",
 "name": "Reading despair in others: face, body, voice, behavior",
 "group": "reading-others",
 "ladder_rank": 9, "ladder_tier": "advanced",
 "description": ("Despair in another person is readable if you know "
  "where to look - and the looking itself is an act of care. The "
  "face: the grief-brow held too long, the mouth downturned even "
  "at rest, the eyes aimed at nothing, the smile that misses the "
  "eyes. The body: the folded silhouette, the stillness between "
  "motions, the leaning on doorframes, the apartment telling the "
  "story before the person does. The voice: flat, slow, quiet, "
  "the long pauses, the absolutes ('never,' 'nothing'), the 'I am "
  "fine' delivered a beat too fast. The behavior: the canceled "
  "plans, the unanswered messages, the hobby abandoned, the flare "
  "of the vague late-night text. No single sign proves anything - "
  "people have bad weeks - but the cluster is the signal: face "
  "plus body plus voice plus behavior, all pointing the same "
  "direction, over days not hours. When you see the cluster, the "
  "archive's instruction is simple: do not diagnose, do not "
  "announce your findings. Just move closer, and open with the "
  "gentlest true sentence you own: 'I have noticed you seem heavy "
  "lately. I am here.'"),
 "how_it_works": ("Reading others runs on the same channels "
  "expression uses, in reverse: the observer's brain matches "
  "incoming faces, postures, voices, and behaviors against its "
  "library of emotional patterns - the work Ekman mapped for "
  "faces extends across every channel. The cluster rule exists "
  "because single channels are noisy: a downturned mouth might "
  "be concentration, a canceled plan might be a busy week. "
  "Convergence across channels over time is what raises the "
  "signal above the noise - four channels agreeing for days is "
  "a pattern, not a coincidence. The 'do not diagnose' rule is "
  "load-bearing: labeling someone ('you are despairing') "
  "triggers defensiveness and the mask snaps shut, while "
  "describing your own observation ('you seem heavy lately') "
  "keeps the door open because it is about your perception, "
  "which they are free to correct. The gentle opener works by "
  "lowering the cost of honesty: 'I am here' promises company "
  "without demanding confession."),
 "key_points": [
  "Read four channels: face, body, voice, behavior - the cluster is the signal.",
  "Single signs are noisy; four channels agreeing over days is a pattern.",
  "Face: grief-brow held, eyes at nothing, the smile missing the eyes.",
  "Voice: flat, slow, absolutes; behavior: canceled plans, abandoned hobbies.",
  "Never diagnose or announce: move closer and open gently - 'you seem heavy; I am here.'"],
 "requirements": [
  "All four channels with concrete readable details.",
  "The cluster-over-time rule explained.",
  "The gentle opener quoted as the close."],
 "standards": [
  "Ekman on multi-channel emotion recognition.",
  "Keltner on empathic accuracy and its social function."],
 "citations": [CIT_EKMAN, CIT_KELTNER, CIT_IZARD],
 "sig_lens": ("Through the Signature lens, reading others is the "
  "archive's field craft: four channels, cluster rule, no "
  "diagnosing, gentle opener. The Signature archivist trains "
  "readers the way naturalists train birders - by field marks, "
  "patiently, without disturbing the subject. You do not trap "
  "the bird to prove you saw it. You note the marks, you move "
  "closer quietly, and you let your presence be the invitation."),
},
{
 "key": "emde-helping",
 "name": "What helps: sitting with someone in despair",
 "group": "reading-others",
 "ladder_rank": 9, "ladder_tier": "advanced",
 "description": ("When someone near you is in despair, the most "
  "powerful thing you can do is also the simplest: be there, "
  "steadily, without trying to fix it. Sit in the room. Make the "
  "tea. Handle one small logistics item - the dishes, the ride, "
  "the form - because logistics are the first thing despair "
  "drops and the easiest thing to lift. Say true things, not "
  "bright things: 'this is a hard time' beats 'everything "
  "happens for a reason'; 'I am not going anywhere' beats 'just "
  "stay positive.' Ask open, low-pressure questions - 'what is "
  "the heaviest part right now' - and then actually listen, "
  "without rehearsing your reply. Do not rush the silence; "
  "despair speaks slowly, and hurrying it teaches the person "
  "their pace is wrong. Keep showing up after the crisis week, "
  "because despair is long and the world moves on fast - the "
  "friend who still calls in month three is doing the real work. "
  "And know your limits: you can be the steady presence, but you "
  "cannot be the whole treatment. If the despair is deep or "
  "long, gently help them toward professional support - 'would "
  "it help if I sat with you while you made the call' - and "
  "keep being the friend either way."),
 "how_it_works": ("Presence works through co-regulation: one calm "
  "nervous system steadies another, measurably - heart rates, "
  "breathing, and stress hormones synchronize between people "
  "in close contact, which is why sitting in the room is not "
  "'doing nothing.' Handling logistics works because it "
  "removes demands from an empty budget without requiring the "
  "person to decide or act - the two things offline. True-not-"
  "bright language works because it validates the appraisal "
  "('this is hard' agrees with the evidence) instead of "
  "arguing with it, which keeps trust intact for the moments "
  "when you do offer perspective. Low-pressure questions work "
  "by externalizing without interrogating: the person sets the "
  "depth. Showing up in month three works because support "
  "systems have a half-life - the initial rally fades, and "
  "despair is still there, so late presence is disproportionately "
  "valuable. The limits clause matters because helpers who try "
  "to be the whole treatment burn out and disappear, which the "
  "despair then files as more evidence; sustainable help is "
  "help that lasts."),
 "key_points": [
  "Be there steadily without fixing: presence is co-regulation, not doing nothing.",
  "Lift one logistics item: the dishes, the ride, the form - the first things dropped.",
  "Say true things, not bright things: 'this is hard' beats 'stay positive.'",
  "Keep showing up after the crisis week: the month-three friend does the real work.",
  "Know your limits: steady presence plus a bridge to professional support."],
 "requirements": [
  "Five concrete helping actions, each specific.",
  "True-not-bright language with quoted examples.",
  "The limits-and-bridge clause as the close."],
 "standards": [
  "Keltner on co-regulation: calm systems steadying distressed ones.",
  "Bonanno on the long arc of support after loss."],
 "citations": [CIT_KELTNER, CIT_BONANNO, CIT_GROSS],
 "sig_lens": ("Through the Signature lens, helping is the archive's "
  "mutual-aid protocol: presence, logistics, true language, "
  "low-pressure questions, month-three showing up - filed under "
  "Steady, with the limits clause in bold. The Signature "
  "archivist trains helpers the way lighthouse keepers are "
  "trained: keep the light on, do not swim out. The light does "
  "not rescue the ship; it lets the ship find the harbor. Keep "
  "the light on."),
},
{
 "key": "emde-backfires",
 "name": "What backfires: responses that make it worse",
 "group": "reading-others",
 "ladder_rank": 10, "ladder_tier": "advanced",
 "description": ("Good intentions misfire around despair with "
  "remarkable reliability. The pep talk ('just think positive,' "
  "'other people have it worse') backfires because it argues "
  "with the forecast instead of answering the feeling - the "
  "person hears that their pain is incorrect, and stops telling "
  "you things. The fix-it blitz (ten solutions before breakfast) "
  "backfires because despair has already tried and discarded "
  "most solutions; the blitz just proves you do not understand "
  "the terrain. The comparison ('when I went through this') "
  "backfires by moving the spotlight: the despairing person now "
  "has to comfort your story instead of being heard in theirs. "
  "The vanishing act - the friend who stops calling because 'I "
  "did not know what to say' - backfires worst of all: silence "
  "is filed by despair as evidence for the verdict. Even "
  "well-meant urgency ('you need to get help right now') can "
  "backfire if it sounds like an order; 'would it help if' "
  "opens the door that 'you need to' slams. The archive's rule "
  "is one sentence: do not argue with the feeling, do not "
  "audition your solutions, do not disappear. Just stay, tell "
  "the truth gently, and let your steadiness do the arguing."),
 "how_it_works": ("Each backfire has a mechanism. Pep talks fail "
  "through invalidation: contradicting the appraisal ('it is "
  "not that bad') without new evidence just teaches the "
  "person that this listener is unsafe, so disclosure stops - "
  "and undisclosed despair hardens. Fix-it blitzes fail "
  "through premature problem-solving: solutions offered "
  "before the feeling is heard are experienced as dismissal, "
  "and each rejected solution ('tried that') deepens the "
  "'nothing works' premise. Comparisons fail through "
  "spotlight theft: attention is a finite resource in "
  "conversation, and redirecting it starves the disclosure "
  "the person was building toward. Vanishing fails through "
  "evidence: despair's forecast predicts abandonment, and "
  "the silent friend is entered as Exhibit A. Urgency-as-"
  "order fails through reactance: the conservation program "
  "already resists demands, so orders trigger opposition "
  "instead of action. The stay-steady alternative works "
  "because it does the one thing none of the backfires do: "
  "it keeps the channel open."),
 "key_points": [
  "Pep talks argue with the forecast; the person hears their pain is incorrect.",
  "Fix-it blitzes prove you do not know the terrain: 'tried that' deepens 'nothing works.'",
  "Comparisons steal the spotlight the disclosure was building toward.",
  "Vanishing is filed as Exhibit A for the abandonment forecast.",
  "The rule: do not argue, do not audition solutions, do not disappear. Stay steady."],
 "requirements": [
  "Five backfiring responses, each with its mechanism.",
  "Quoted examples of the unhelpful phrases.",
  "The one-sentence rule as the close."],
 "standards": [
  "Gross on invalidation: contradicted appraisals without evidence.",
  "Keltner on the social costs of misattuned support."],
 "citations": [CIT_GROSS, CIT_KELTNER, CIT_LAZARUS],
 "sig_lens": ("Through the Signature lens, backfires are the "
  "archive's hazard placards: Pep Talk (invalidates), Blitz "
  "(dismisses), Comparison (steals the light), Vanishing "
  "(exhibits abandonment), Orders (triggers reactance) - five "
  "placards on the helper's trail, each with its mechanism "
  "printed underneath. The Signature archivist posts them at "
  "eye level, because the people most likely to backfire are "
  "the people trying hardest to help. Read the placards. Stay "
  "steady. Keep the channel open."),
},
{
 "key": "emde-relatives",
 "name": "The relatives of despair: telling the close cousins apart",
 "group": "relatives-and-mixes",
 "ladder_rank": 10, "ladder_tier": "advanced",
 "description": ("Despair has close cousins, and telling them apart "
  "matters because each wants a different response. Hopelessness "
  "is the sibling: nearly identical, but hopelessness can be "
  "narrow ('I will never fix this project') while despair tends "
  "to be total ('nothing will ever work') - breadth is the "
  "tell. Grief is the parent: it mourns a specific loss and "
  "moves in waves, while despair has generalized the loss into "
  "a verdict on the future - specificity versus verdict is the "
  "tell. Sorrow is the quieter cousin: deep but still tender, "
  "still able to be comforted, while despair has gone past "
  "comfort into shutdown. Resignation looks similar from "
  "outside - the stillness, the stopped effort - but "
  "resignation has made peace with the outcome while despair "
  "is still bleeding from it; peace versus wound is the tell. "
  "Defeat is the event; despair is the story told about the "
  "event afterward. And low mood - the flat, grey weeks - "
  "overlaps heavily, but mood is weather while despair is the "
  "forecast written in permanent ink; when the flat weeks "
  "harden into a total verdict on the future, that is the "
  "line where company, structure, and professional support "
  "matter most. Cousins share a family resemblance. The "
  "responses do not share a shelf."),
 "how_it_works": ("Distinguishing relatives is differential "
  "description: mapping each cousin on the same dimensions - "
  "breadth (narrow versus total), time direction (past loss "
  "versus future verdict), energy (tender versus shutdown), "
  "and stance toward the outcome (peace versus wound). "
  "Hopelessness-versus-despair turns on breadth: the narrower "
  "the forecast, the more local the intervention can be (fix "
  "the project versus rebuild the future). Grief-versus-"
  "despair turns on time direction: grief work processes a "
  "past loss, despair work must additionally reopen a future "
  "- which is why grief rituals alone sometimes do not touch "
  "despair. Sorrow-versus-despair turns on receptivity: "
  "comfort still lands in sorrow, so comfort is the move; in "
  "despair comfort slides off the shutdown, so structure and "
  "presence come first. Getting the cousin right prevents the "
  "two classic errors: treating despair like grief (waiting "
  "for waves that never come) and treating grief like despair "
  "(declaring a future closed that is merely mourning)."),
 "key_points": [
  "Hopelessness is narrow, despair is total: breadth is the tell.",
  "Grief mourns a loss in waves; despair generalizes it into a future verdict.",
  "Sorrow can still be comforted; despair has gone past comfort into shutdown.",
  "Resignation has made peace; despair is still bleeding: peace versus wound.",
  "Right cousin, right response: comfort for sorrow, structure and presence for despair."],
 "requirements": [
  "Six relatives distinguished with a one-line tell for each.",
  "The dimension system (breadth, time, energy, stance) explained.",
  "The two classic errors named as the close."],
 "standards": [
  "Izard on differential emotions: close states, distinct profiles.",
  "Plutchik on neighboring positions on the emotion wheel."],
 "citations": [CIT_IZARD, CIT_PLUTCHIK, CIT_BONANNO],
 "sig_lens": ("Through the Signature lens, the relatives are the "
  "archive's sorting shelf: Hopelessness (narrow), Grief "
  "(waves), Sorrow (tender), Resignation (peace), Defeat "
  "(event), Low Mood (weather) - six folders, six tells, six "
  "different response shelves. The Signature archivist sorts "
  "before acting, because the wrong shelf wastes the right "
  "medicine. File accurately; respond precisely."),
},
{
 "key": "emde-mixes",
 "name": "Despair in blends: four emotion mixes",
 "group": "relatives-and-mixes",
 "ladder_rank": 10, "ladder_tier": "advanced",
 "description": ("Despair blends the way paints blend - and the "
  "archive keeps four reference swatches. Despair plus fear is "
  "dread (record 8): 'something bad is coming and nothing will "
  "stop it' - exhausted and wired at once, the darkest hours of "
  "the feeling. Despair plus anger is bitterness: the shutdown "
  "with a hot edge, 'the world cheated me and I am done asking "
  "it for anything' - still seated, but the jaw is tight and the "
  "words have teeth. Despair plus sadness is desolation: the "
  "compound at full depth, grief with no horizon - the weeping "
  "that comes in waves inside a stillness that never lifts, the "
  "heaviest blend in the collection. Despair plus disgust is "
  "revulsion at fate: 'everything is rotten and I want no part "
  "of it' - withdrawal with contempt, the door closed and "
  "locked from the inside. Each blend has its tell and its "
  "key: dread wants the body calmed first (starve the fear "
  "half); bitterness wants the grievance heard before the "
  "shutdown is addressed (the hot edge guards the wound); "
  "desolation wants long steady company, no fixing; revulsion "
  "wants one clean good thing - a real kindness, a real beauty "
  "- to prove the 'everything' in 'everything is rotten' is "
  "a lie. Blends are just despair wearing a partner's coat. "
  "Name the coat, and you know which door to knock on."),
 "how_it_works": ("Blends follow Plutchik's dyad logic: two "
  "primaries (or a primary and a compound) active at once, "
  "each contributing its appraisal and its body program. "
  "Dread (despair plus fear) was dissected in record 8: "
  "certainty of badness plus uncertainty of shape. "
  "Bitterness adds anger's appraisal ('I have been wronged') "
  "to despair's shutdown, producing the paradox of energized "
  "stillness - the grievance supplies arousal the despair "
  "would otherwise lack, which is why bitter people can "
  "argue for hours about a future they claim is closed. "
  "Desolation doubles the loss channel: sadness's grief "
  "plus despair's closed future, the maximum-weight "
  "configuration. Revulsion adds disgust's rejection program "
  "('expel it') to despair's withdrawal, producing active "
  "refusal rather than passive sinking. The blend keys work "
  "by the divide-the-file doctrine: address the partner "
  "first (calm fear, hear grievance, outlast desolation's "
  "waves, falsify disgust's 'everything'), and what remains "
  "is single-channel despair - heavy, but workable with the "
  "standard tools."),
 "key_points": [
  "Dread (plus fear): exhausted and wired; key is calming the body first.",
  "Bitterness (plus anger): shutdown with a hot edge; key is hearing the grievance.",
  "Desolation (plus sadness): grief with no horizon; key is long steady company.",
  "Revulsion (plus disgust): withdrawal with contempt; key is one clean good thing.",
  "Name the partner's coat, and you know which door to knock on."],
 "requirements": [
  "Four blends named with feel, look, tell, and key.",
  "The dyad mechanism explained for each.",
  "The divide-the-file doctrine as the close."],
 "standards": [
  "Plutchik's dyads: primary pairs fusing into named compounds.",
  "Izard on the additivity of blended emotional programs."],
 "citations": [CIT_PLUTCHIK, CIT_IZARD, CIT_FRIJDA],
 "sig_lens": ("Through the Signature lens, the four blends are the "
  "archive's swatch cards: Dread, Bitterness, Desolation, "
  "Revulsion - despair wearing four different coats, each "
  "with its tell and its key filed on the back of the card. "
  "The Signature archivist's doctrine is printed on every "
  "card: divide the file. Handle the partner, and the "
  "despair underneath is single-channel again - heavy, but "
  "workable, and the archive has tools for workable."),
},
{
 "key": "emde-simulation",
 "name": "The full simulation: despair from trigger to resolution",
 "group": "relatives-and-mixes",
 "ladder_rank": 10, "ladder_tier": "advanced",
 "description": ("SCENE ONE - THE TRIGGER. October. Priya, 41, a "
  "nurse of fourteen years, gets the letter: the clinic is "
  "closing, her position eliminated. She reads it twice in the "
  "parking lot. Her inner monologue goes flat: 'Fourteen years. "
  "Gone in a paragraph.' Body: the sigh that empties her whole "
  "chest. Face: the mouth dips, the gaze drops to the asphalt. "
  "SCENE TWO - THE PILE. Over three weeks the applications go "
  "unanswered - forty-seven of them. Her mother's health dips. "
  "The savings thin. Each blow deposits its stone; the forecast "
  "assembles itself: 'I am too old, the field is shrinking, this "
  "was my last good job.' Behavior: she stops opening the job "
  "board. The apartment dims. SCENE THREE - THE PEAK. A Tuesday. "
  "She does not get up until noon. The phone has seven unanswered "
  "texts. She thinks, flatly, 'this is just what my life is now.' "
  "Her sister, reading the silence correctly, drives over with "
  "groceries and sits on the couch without asking for anything. "
  "SCENE FOUR - THE CRACK. Thursday. The sister makes her walk "
  "around the block - twenty minutes, no talking required. "
  "Friday, Priya washes the dishes. Small, completable, done. "
  "A former patient calls out of the blue to thank her; she "
  "cries for the first time in weeks, and the crying feels like "
  "thawing. SCENE FIVE - THE RESOLUTION. Not a miracle: a "
  "part-time triage line, two evenings a week, taken because the "
  "sister sat with her while she applied. The forecast does not "
  "vanish; it gets outvoted. Final annotation from the archive: "
  "no single scene saved Priya. The trigger was real, the peak "
  "was real - and so was the walk, the dishes, the sister, the "
  "phone call. Despair edits the footage to hide the second "
  "list. The simulation exists to put it back in, scene by "
  "scene, until the future reopens."),
 "how_it_works": ("The full simulation is the archive's showcase "
  "instrument: it runs every record in the database as one "
  "continuous case. Scene One demonstrates triggers (record 18) "
  "and the face at onset (records 14-15). Scene Two runs the "
  "pile-up trigger, the forecast assembly (records 1-3), and "
  "the behavior triage (record 22). Scene Three is the peak: "
  "shutdown physiology (records 10-12), the still face (record "
  "15), the verbal verdict (record 23), and the escalation "
  "ladder (record 25) - plus the correct response arriving from "
  "outside (records 29-30). Scene Four demonstrates the "
  "counter-evidence mechanism: movement, completable tasks, and "
  "an unsolicited kindness forcing forecast recalculation "
  "(records 26, 28). Scene Five resolves through the "
  "outvoted-forecast principle: the feeling does not have to "
  "vanish for the life to restart; it only has to lose the "
  "vote. As a teaching instrument, the simulation lets "
  "readers rehearse the entire arc - recognition, response, "
  "and recovery - in safety, so the real thing, met in life, "
  "is navigated rather than merely suffered."),
 "key_points": [
  "Five scenes: trigger, pile, peak, crack, resolution - the whole arc in one case.",
  "Every earlier record appears in the simulation as a working part.",
  "The sister's arrival is the correct outside response: presence, groceries, no demands.",
  "Recovery is counter-evidence, not argument: the walk, the dishes, the phone call.",
  "The forecast does not vanish; it gets outvoted - and the future reopens."],
 "requirements": [
  "A multi-scene narrative from trigger through peak to resolution.",
  "Inner monologue, body, face, dialogue, and behavior in the scenes.",
  "The archive's annotation closing with the outvoted-forecast principle."],
 "standards": [
  "Frijda on emotion episodes as extended temporal processes.",
  "Bonanno on the real trajectories of recovery after loss."],
 "citations": [CIT_FRIJDA, CIT_BONANNO, CIT_GROSS],
 "sig_lens": ("Through the Signature lens, the full simulation is "
  "the archive's master reel: Priya's October, trigger to "
  "resolution, every record in the collection playing its part "
  "in one continuous case. The Signature archivist screens it "
  "for every new reader, because a story the archive has "
  "watched end well is a proof no argument can match. The "
  "forecast said closed. The footage says reopened. Trust the "
  "footage - and when your own October comes, remember: the "
  "walk, the dishes, the sister, the call. Scene by scene, the "
  "future reopens."),
},
]
