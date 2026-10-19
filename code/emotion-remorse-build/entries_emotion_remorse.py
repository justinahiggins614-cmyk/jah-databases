#!/usr/bin/env python3
"""34 ladder-ordered entries for the Remorse Emotion databases
(Manon's 2026-10-17 16:15 order, emotion series).

Public edition: real, fact-checked descriptive psychology of remorse -
APA Dictionary, Tangney and Dearing, Lewis, Ekman, Lazarus, Gross,
Baumeister, Izard, Darwin (src public-harvest).
Signature edition: his original Signature lens - remorse as the
conscience's honest audit, the inward review that forges integrity -
framed as signal, fuel, and mastery (src signature, titles suffixed
" (Signature Edition)").

Descriptive and educational ONLY. These entries describe and simulate
the emotion; they never diagnose real people, never label any real person
with an emotional state, and offer therapeutic advice only in the form of
general, safe, everyday guidance. No clinical language, no diagnostic
labels. Screened: nothing hate-adjacent, profane, or inappropriate; no
religious framing; no website or Facebook references.

ladder_rank runs 1..34 in template order: what remorse IS (1-4) -> how it
feels (5-9) -> body signals (10-13) -> facial expression (14-17) ->
triggers (18-21) -> behavior (22-25) -> healthy expression (26-28) ->
recognizing in others (29-31) -> related emotions, mixes, full simulation
(32-34).
"""

SIG_TAIL = ("Signature original - his original Signature lens: remorse as the "
            "conscience's honest audit, the inward review that forges integrity; "
            "Signature editions frame every facet as signal, fuel, and mastery - "
            "never as a diagnosis, never labeling any real person, and never "
            "presented as authentic public record.")

CIT_APA = ("American Psychological Association. APA Dictionary of Psychology "
           "- remorse: a strong feeling of guilt or regret over having done "
           "something wrong; a moral emotion arising from the perception that "
           "one has violated a standard of conduct one accepts.")
CIT_TANGNEY = ("Tangney J. P. and Dearing R. L. Shame and Guilt (2002) - the "
               "self-behavior distinction: guilt (and its deeper register, "
               "remorse) judges the specific act (\"I did bad\") rather than "
               "the whole self, and predicts repair: confession, apology, and "
               "changed conduct.")
CIT_LEWIS = ("Lewis M. Shame: The Exposed Self (1992) - self-conscious emotions "
             "require a self that can be an object to itself; remorse needs the "
             "same machinery: an inner standard, self-awareness, and the "
             "capacity to judge one's own conduct.")
CIT_EKMAN = ("Ekman P. Emotions Revealed (2003) - self-conscious emotions show "
             "in gaze aversion, lowered head, and subdued movement; remorse's "
             "visible signal blends sadness cues with the lowered, inward "
             "posture of self-reproach.")
CIT_LAZARUS = ("Lazarus R. S. Emotion and Adaptation (1991) - appraisal theory: "
               "remorse follows the appraisal that one has violated a moral "
               "standard one genuinely endorses, with the self as both judge "
               "and defendant.")
CIT_GROSS = ("Gross J. J. Emotion regulation research - strategies of "
             "reappraisal, expression, and situation modification that can "
             "steer the intensity and course of moral emotions such as "
             "remorse.")
CIT_BAUMEISTER = ("Baumeister R. F. research on guilt as a prosocial moral "
                  "emotion - guilt motivates apology, restitution, and changed "
                  "behavior; remorse is guilt's deeper register and carries "
                  "the same reparative drive toward making things right.")
CIT_IZARD = ("Izard C. E. Human Emotions (1977) - moral and social emotions "
             "develop alongside self-awareness and conscience; remorse is a "
             "mature self-conscious emotion that depends on an internalized "
             "sense of right and wrong.")
CIT_DARWIN = ("Darwin C. The Expression of the Emotions in Man and Animals "
              "(1872) - self-conscious states register in averted gaze, "
              "lowered head, and the subdued bearing of a person turning "
              "judgment inward.")

ENTRIES = [
{
 "key": "remorse_definition",
 "name": "What Remorse Is: A Plain-Language Definition",
 "group": "Foundations", "ladder_rank": 1, "ladder_tier": "foundations",
 "description": ("Remorse is the heavy, aching feeling that arrives after you "
  "have done something you believe was wrong. In everyday words: remorse is "
  "the inward voice that says, \"I should not have done that,\" and means it "
  "all the way down. It is guilt's deeper register - not a passing twinge, "
  "but a sustained reckoning with a choice you made, a word you said, or an "
  "action you took that hurt someone or broke a rule you actually believe in. "
  "Remorse points backward at the deed and forward at the debt: it replays "
  "what happened and insists that something is owed - an apology, a repair, "
  "a change. Where simple regret says \"I wish that had gone differently,\" "
  "remorse says \"I was wrong to do that, and I must answer for it.\" That "
  "sense of moral debt is what makes remorse one of the most human emotions "
  "there is: it only fires in a mind that can judge itself."),
 "how_it_works": ("Remorse runs on a three-part circuit: a standard, a deed, "
  "and a reckoning. First there is a standard - a rule about right and wrong "
  "that you genuinely hold, whether you learned it from family, from your "
  "community, or forged it yourself through experience. Second comes a deed - "
  "something you did (or failed to do) that seems to violate that standard: "
  "a lie, a betrayal, a cruelty, a cowardice, a neglected duty. Third comes "
  "the reckoning: the mind replays the deed, measures it against the "
  "standard, and delivers a verdict - guilty. That verdict is not a cold "
  "thought; it arrives with the full weight of feeling: a heaviness in the "
  "chest, a replaying of the scene, an urge to undo what cannot be undone. "
  "The circuit keeps looping because the mind is trying to solve an "
  "unsolvable problem - rewriting the past - and the loop only quiets when "
  "the energy is redirected forward, into repair, apology, or changed "
  "conduct. That is why remorse is, at its root, a moral emotion with a job "
  "to do: it exists to make the next choice better than the last one."),
 "key_points": [
  "Remorse is guilt's deeper register: a sustained reckoning with a wrongdoing, not a passing twinge.",
  "Its circuit is standard, deed, reckoning: a believed rule, a violating act, and the mind's guilty verdict.",
  "Remorse points backward at the deed and forward at the debt - apology, repair, changed conduct.",
  "It only fires where a conscience exists: the mind must be able to judge itself to feel remorse.",
  "Simple regret wishes things had gone differently; remorse insists \"I was wrong\" and seeks to answer for it."],
 "requirements": [
  "Describe remorse in plain everyday words before any technical framing.",
  "Keep the remorse-versus-regret distinction (moral debt vs wished-different outcome) visible.",
  "Never describe any real person as remorseful or remorseless; all examples stay fictional and general.",
  "Treat remorse as a normal, functional human emotion, not a defect or disorder."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people, no therapeutic promises."],
 "citations": [CIT_APA, CIT_TANGNEY],
 "sig_lens": ("The Signature lens reads remorse as the conscience's honest audit: "
  "the moment the mind replays a choice and the heart marks it wrong. It is not a "
  "wound to hide from; it is a forge reading. Remorse proves the compass still "
  "works - a person who feels it has a working moral instrument, and the pain of "
  "the reading is the proof. Signal: it points to the exact value you care about. "
  "Fuel: it powers repair, apology, and change. Mastery: owned honestly and acted "
  "on, remorse converts a past mistake into future integrity.")
},
{
 "key": "remorse_emotion_family",
 "name": "Remorse in the Emotion Family",
 "group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
 "description": ("Remorse belongs to the family of moral, self-conscious "
  "emotions - the feelings that require a self that can judge itself. Its "
  "closest relatives are guilt and regret, and it sits one generation deeper "
  "than both: guilt is the broad feeling of having done wrong, regret is the "
  "wish that events had unfolded differently, and remorse is where the two "
  "fuse and deepen - the aching conviction that what you did was wrong and "
  "that you are answerable for it. Shame is remorse's cousin, but the two "
  "point in different directions: shame judges the whole self (\"I am bad\") "
  "while remorse judges the deed (\"I did bad\"). Remorse's neighbors also "
  "include contrition (remorse turned toward making amends), self-reproach "
  "(the inner scolding voice), and moral anguish (remorse at its most "
  "intense). On the far side of the family sit remorse's opposites: "
  "self-justification, defiance, and indifference - the states that refuse "
  "the reckoning remorse demands. Understanding this placement matters "
  "because it explains remorse's function: it is not a flaw in the system, "
  "it is the system's alarm bell, the feeling that keeps a conscience "
  "honest."),
 "how_it_works": ("Emotions sort into families the way colors sort into a "
  "spectrum, and remorse's address is the moral district of the "
  "self-conscious neighborhood. Basic emotions like fear and anger fire fast "
  "from old brain circuitry; self-conscious emotions like remorse fire "
  "slower because they need a working model of the self, a set of internal "
  "standards, and the ability to compare the two - machinery that matures "
  "through childhood as conscience develops. Remorse inherits guilt's "
  "act-focus (the deed, not the person) and regret's backward look (the "
  "replayed scene), then adds depth: a felt moral debt and a drive to make "
  "things right. That is why remorse almost always travels with its "
  "relatives - a flash of shame at being the kind of person who could do "
  "that, a wash of sadness at the harm caused, a flicker of fear about "
  "consequences. The family resemblances are not accidents; they are the "
  "same underlying appraisal - \"I violated what I believe\" - viewed from "
  "different angles."),
 "key_points": [
  "Remorse is a moral, self-conscious emotion: it needs a self that can judge itself.",
  "Its closest relatives are guilt (act-focused wrongdoing) and regret (wished-different outcome).",
  "Remorse fuses and deepens both: the aching conviction of wrongdoing plus a felt moral debt.",
  "Shame is its cousin but points at the self (\"I am bad\"); remorse points at the deed (\"I did bad\").",
  "Its opposites - self-justification, defiance, indifference - refuse the reckoning remorse demands."],
 "requirements": [
  "Place remorse clearly among guilt, regret, shame, and contrition with the distinctions stated plainly.",
  "Explain why remorse is classed as a self-conscious emotion requiring a mature conscience.",
  "Keep all examples fictional and general; never label any real person's emotional state.",
  "Present remorse's function (the conscience's alarm) as normal and healthy."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people, no therapeutic promises."],
 "citations": [CIT_IZARD, CIT_LEWIS],
 "sig_lens": ("The Signature lens places remorse at the center of the moral "
  "compass: it is the needle swinging back to true north after a deviation. Guilt "
  "is the tap on the shoulder, regret is the backward glance, but remorse is the "
  "full audit - the deep reckoning that forges integrity. In the Signature system, "
  "remorse is honored as proof of a working conscience: the instrument reading is "
  "painful because the standard matters. Mastery means reading the needle honestly, "
  "then steering by it.")
},
{
 "key": "remorse_intensity_scale",
 "name": "How Strong Remorse Can Get: Mild, Moderate, Intense",
 "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
 "description": ("Remorse is not one fixed volume; it is the same emotion "
  "played at different loudness levels, and the level changes everything "
  "about how it feels and what it does. At mild intensity, remorse is a "
  "passing pang - a wince when you remember snapping at someone, gone by the "
  "next hour, leaving only a small lesson behind. At moderate intensity, it "
  "settles in for a stay: a heaviness that colors the day, replaying the "
  "scene in quiet moments, nudging you toward an apology you keep meaning to "
  "make. At intense intensity, remorse becomes a storm: sleep-breaking, "
  "appetite-killing, concentration-shredding anguish that can dominate weeks "
  "or months, sometimes years for the gravest wrongs. Three dials set the "
  "volume: how central the violated value is (a core value breached screams "
  "louder than a minor rule), how serious the harm feels (irreversible harm "
  "echoes longest), and how inescapable the memory is (triggers everywhere "
  "keep the volume up). The same deed can play at any volume in different "
  "people - or in the same person at different times of life - because the "
  "dials are set by conscience, circumstance, and how the story gets told "
  "inside the mind."),
 "how_it_works": ("Think of remorse as an alarm with a volume knob wired to "
  "three dials. Dial one is value centrality: the more the broken rule "
  "defines who you believe you are - honesty for the truthful person, "
  "loyalty for the faithful friend - the louder the alarm. Dial two is "
  "perceived harm: a wrong that can be fixed plays quieter than one that "
  "cannot be undone, because the mind's repair drive has somewhere to go. "
  "Dial three is memory stickiness: every reminder, every anniversary, every "
  "similar situation re-triggers the circuit and holds the volume up. The "
  "knob position determines the emotion's whole character: low volumes "
  "produce brief pangs that teach and fade; mid volumes produce the classic "
  "remorse experience - heavy, looping, apology-seeking; high volumes produce "
  "moral anguish, where the replay loop runs constantly and the body pays "
  "the price in sleep, appetite, and energy. Importantly, the dials are not "
  "fixed: making amends turns down dial two, time and distance turn down "
  "dial three, and re-examining an over-harsh standard can turn down dial "
  "one. The volume is adjustable, even when it does not feel that way in "
  "the storm."),
 "key_points": [
  "Remorse plays at three volumes - mild pang, moderate heaviness, intense moral anguish - and the volume changes its whole character.",
  "Dial one: how central the violated value is to the person's identity.",
  "Dial two: how serious and irreversible the perceived harm feels.",
  "Dial three: how sticky the memory is - reminders and triggers hold the volume up.",
  "The volume is adjustable: repair, time, distance, and fairer self-judgment all turn the dials down."],
 "requirements": [
  "Present mild, moderate, and intense remorse as the same emotion at different volumes, not different emotions.",
  "Name the three dials (value centrality, perceived harm, memory stickiness) in plain words.",
  "Keep examples fictional and general; never assess any real person's remorse level.",
  "End with the adjustable-volume truth: repair and time genuinely lower the volume."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people, no therapeutic promises."],
 "citations": [CIT_LAZARUS, CIT_GROSS],
 "sig_lens": ("The Signature lens treats intensity as the audit's depth, not "
  "its danger. A mild pang is a routine inspection; moderate heaviness is a "
  "full review; intense anguish is a deep forensic audit of the soul. Each level "
  "carries proportional signal: the deeper the ache, the more central the value "
  "at stake. Mastery is not silencing the alarm - it is reading the volume as "
  "information about what matters most, then converting the loudest readings "
  "into the strongest repairs.")
},
{
 "key": "remorse_myths",
 "name": "Myths and Misunderstandings About Remorse",
 "group": "Foundations", "ladder_rank": 4, "ladder_tier": "foundations",
 "description": ("Remorse is surrounded by folk wisdom that gets it wrong, "
  "and the myths do real damage because they tell people to mistrust a "
  "healthy signal. Myth one: feeling remorse means you are a bad person. "
  "The truth runs the other way - remorse fires only in a working "
  "conscience; the people who never feel it are the ones to worry about. "
  "Myth two: remorse is just self-pity in a moral costume. Real remorse "
  "focuses on the harm done and the debt owed, not on the sufferer's own "
  "comfort; self-pity asks for soothing, remorse asks for repair. Myth "
  "three: if you truly feel remorse you will never do it again. Remorse "
  "motivates change, but human beings are creatures of habit and pressure; "
  "the feeling is a compass, not a lock on the door. Myth four: remorse "
  "must be suffered through alone and in silence. In fact, spoken "
  "acknowledgment - apology, confession, restitution - is the emotion's "
  "natural completion; silence starves it. Myth five: time erases remorse, "
  "so just wait it out. Time dulls the ache, but unaddressed remorse tends "
  "to resurface at anniversaries and reminders; what actually resolves it "
  "is repair, honest self-examination, and changed conduct - not the "
  "calendar."),
 "how_it_works": ("Myths about remorse persist because the emotion itself is "
  "uncomfortable to think about clearly, so culture fills the gap with "
  "slogans. Each myth works by mislabeling one of remorse's moving parts. "
  "\"Remorse means you are bad\" mistakes the alarm for the fire: the "
  "feeling is the conscience working, not the conscience failing. "
  "\"Remorse is self-pity\" mistakes the sufferer for the subject: track "
  "where the mind's attention goes - to the harmed person and the debt, or "
  "to the self and its comfort - and the two separate cleanly. \"True "
  "remorse guarantees change\" mistakes motivation for mechanism: remorse "
  "supplies the why, but habits, pressures, and circumstances still supply "
  "the how, and change takes practice. \"Suffer in silence\" mistakes the "
  "symptom for the cure: the looping replay is the mind begging for the "
  "circuit to complete through acknowledgment and repair. \"Time heals\" "
  "mistakes fading for resolving: the volume drops, but the ledger entry "
  "remains open until it is answered. Correcting each myth does not just "
  "fix a belief - it frees the emotion to do its actual job."),
 "key_points": [
  "Myth: remorse means you are bad. Truth: it means your conscience works.",
  "Myth: remorse is self-pity. Truth: remorse focuses on the harm and the debt, not on self-comfort.",
  "Myth: true remorse guarantees you will never repeat it. Truth: it motivates change; change still takes practice.",
  "Myth: suffer in silence. Truth: acknowledgment, apology, and restitution are the emotion's natural completion.",
  "Myth: time erases remorse. Truth: time dulls it, but repair and changed conduct are what resolve it."],
 "requirements": [
  "State five common myths with their corrections, each tied to a moving part of the emotion.",
  "Keep the tone corrective but kind - the reader may currently believe these myths.",
  "All examples fictional and general; no real people assessed or labeled.",
  "Reinforce that remorse is a functional signal, not evidence of a broken character."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people, no therapeutic promises."],
 "citations": [CIT_BAUMEISTER, CIT_TANGNEY],
 "sig_lens": ("The Signature lens treats every myth as static over the signal. "
  "\"Remorse means you are bad\" is the instrument misread: the gauge shows "
  "pressure, and pressure means the system is sealed and working, not broken. "
  "\"Suffer in silence\" is the audit filed away unread. The Signature reading "
  "is blunt: myths keep the ledger open and the forge cold. Mastery burns through "
  "the myths by testing each one against the mechanism - and the mechanism always "
  "says the same thing: feel it, read it, repair it, grow from it.")
},
{
 "key": "remorse_first_person",
 "name": "Inside Remorse: A First-Person Passage",
 "group": "Foundations", "ladder_rank": 5, "ladder_tier": "foundations",
 "description": ("This is what remorse feels like from the inside, in the "
  "words of someone living through it - a fictional composite, not any real "
  "person. It starts as a replay: I am brushing my teeth and there it is "
  "again, the scene, frame by frame, exactly as it happened - the words I "
  "said, the look on their face, the half-second where I could have stopped "
  "and did not. My chest goes heavy, like something is sitting on it. I try "
  "to think about something else and the scene just waits, patient as "
  "gravity, and pulls me back. There is a specific flavor to the ache: it is "
  "not anger, it is not sadness exactly, it is the feeling of being on "
  "trial in a courtroom where I am the defendant, the witness, and the "
  "judge, all at once. I keep rehearsing what I should have done instead, "
  "and each better version of the scene makes the real one hurt more. "
  "Underneath it all is a debt I can feel in my body: something is owed, "
  "and until it is paid - the apology, the fix, the changed behavior - the "
  "trial does not adjourn. That is the inside of remorse: a courtroom that "
  "travels with you, convening at odd hours, until the debt is answered."),
 "how_it_works": ("A first-person simulation works because emotions are, at "
  "their core, experiences - and the way to understand an experience is to "
  "stand inside a faithful model of it. The passage above models remorse's "
  "signature mechanics: the involuntary replay (the mind's attempt to "
  "re-solve the past), the chest heaviness (the body's alarm posture), the "
  "triple role of defendant-witness-judge (the self turned into its own "
  "courtroom), the counterfactual rehearsal (\"what I should have done\" - "
  "the mind generating the lesson), and the felt debt (the reparative "
  "drive). None of this describes any real person; it is a composite "
  "built from the emotion's documented features, the way a flight simulator "
  "models a plane without being any particular flight. Reading it, most "
  "people will recognize the courtroom - remorse is one of the most widely "
  "shared human experiences - and recognition is the point: to know the "
  "feeling from the inside is to understand what the emotion is for."),
 "key_points": [
  "Inside remorse is a traveling courtroom: defendant, witness, and judge are all the self.",
  "The involuntary replay is the mind trying to re-solve an unsolvable past - the signature mental loop.",
  "Counterfactual rehearsal (\"what I should have done\") is the mind generating the lesson from the pain.",
  "The felt debt - something is owed - is the reparative drive made conscious.",
  "First-person simulation builds understanding from the inside; the composite describes no real person."],
 "requirements": [
  "Write the passage in present-tense first person as a fictional composite, never any real person.",
  "Cover the replay, the heaviness, the courtroom roles, the counterfactuals, and the felt debt.",
  "Keep the tone honest and human, never clinical and never melodramatic.",
  "Follow with a plain explanation of what the passage models and why."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people, no therapeutic promises."],
 "citations": [CIT_TANGNEY, CIT_LAZARUS],
 "sig_lens": ("The Signature lens reads the inner courtroom as the audit "
  "chamber: every replay is the evidence being re-examined, every "
  "counterfactual is the auditor drafting the corrective action plan. The "
  "heaviness is not punishment - it is the weight of a standard that matters. "
  "In the Signature system, sitting honestly in that chamber is the first act "
  "of mastery: the people who refuse the audit stay the same, and the people "
  "who complete it come out with forged integrity.")
},
{
 "key": "remorse_time_course",
 "name": "Remorse Over Time: Onset, Peak, Fading, Aftershock",
 "group": "Foundations", "ladder_rank": 6, "ladder_tier": "foundations",
 "description": ("Remorse has a characteristic shape in time, and knowing "
  "the shape helps people recognize where they are inside it. Onset: the "
  "feeling often arrives with a delay - in the moment of the deed there may "
  "be adrenaline, anger, or numbness, and remorse walks in later, sometimes "
  "minutes later, sometimes in the small hours of the night, when the mind "
  "finally replays what happened against what it believes. Peak: the replay "
  "loop runs hottest in the days after, when the scene is fresh and the "
  "debt feels largest; this is when sleep suffers most and the urge to "
  "confess or repair is strongest. Fading: as days become weeks, the loop "
  "loses frequency - not because the ledger closed, but because the mind "
  "cannot sustain peak alarm indefinitely; the ache becomes background "
  "rather than foreground. Aftershock: months or years later, a trigger - "
  "an anniversary, a similar situation, a song, a place - can reopen the "
  "scene at near-original intensity for minutes or hours. The aftershock is "
  "not a relapse or a failure; it is the ledger entry resurfacing for "
  "review. People who make genuine repair tend to find the aftershocks "
  "gentler over time: the entry is marked \"answered,\" even if it is never "
  "fully erased."),
 "how_it_works": ("The time course follows from the circuit's mechanics. "
  "Onset is delayed because the appraisal needs quiet: during the deed, "
  "attention is on action and consequence-management, and only afterward "
  "does the mind get the stillness to measure the deed against the "
  "standard. Peak intensity tracks the freshness of the memory and the "
  "size of the unaddressed debt - the loop runs hot because the repair "
  "drive has not yet discharged. Fading is habituation plus competing "
  "demands: the alarm cannot ring at full volume forever, and daily life "
  "reclaims attention, so the loop drops to background. Aftershocks are "
  "state-dependent memory: the scene was encoded with strong emotion, and "
  "matching cues - dates, places, sensory details - retrieve it with its "
  "original charge. Genuine repair changes the encoding: the memory gets "
  "filed with its resolution attached (\"I apologized; I changed\"), so "
  "later retrievals arrive with the answer, not just the question. That is "
  "why the same memory can torment one person for years and sit quietly in "
  "another: the difference is whether the ledger entry was ever answered."),
 "key_points": [
  "Onset is often delayed: remorse arrives when the mind gets quiet enough to replay the deed.",
  "Peak hits in the days after, when the memory is fresh and the debt feels largest.",
  "Fading is the alarm losing volume over weeks - background ache, not resolution.",
  "Aftershocks are trigger-reopened scenes at near-original intensity, months or years later - normal, not failure.",
  "Genuine repair softens aftershocks: the memory gets filed with its resolution attached."],
 "requirements": [
  "Walk through all four phases - onset, peak, fading, aftershock - in plain words.",
  "Explain the mechanism behind each phase, not just the timeline.",
  "Normalize aftershocks as ordinary memory mechanics, not relapse.",
  "Keep examples fictional and general; never timeline any real person's experience."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people, no therapeutic promises."],
 "citations": [CIT_LAZARUS, CIT_GROSS],
 "sig_lens": ("The Signature lens reads the time course as the audit's lifecycle: "
  "onset is the evidence surfacing, peak is the full review in session, fading is "
  "the file going to background, and aftershock is the file pulled for re-review "
  "when a matching case appears. Mastery means working the lifecycle deliberately: "
  "answer the debt during the peak, when the drive to repair is strongest, and the "
  "aftershocks arrive as quiet confirmations of a closed file rather than reopened "
  "wounds.")
}
,
{
 "key": "remorse_low_vs_high",
 "name": "Remorse at Low Intensity vs High Intensity: Two Snapshots",
 "group": "Foundations", "ladder_rank": 7, "ladder_tier": "foundations",
 "description": ("Two lived snapshots of the same emotion at different "
  "volumes - both fictional, both ordinary. Low intensity: Maya, a team "
  "lead, realizes in the shower that she took credit for an intern's idea "
  "in yesterday's meeting. She winces, makes a face at the tiles, and "
  "decides to correct the record at standup. The whole episode costs her "
  "ninety seconds of discomfort and one honest sentence the next morning; "
  "by lunch it is a lesson, not a weight. High intensity: Daniel, a "
  "father, replays the evening he chose work over his daughter's recital "
  "and learned, too late, that it was her last performance before the "
  "family moved away. The scene ambushes him at red lights, in grocery "
  "lines, at 3 a.m. He has apologized, she has forgiven him, and still the "
  "courtroom convenes: he cannot undo the empty seat. The difference is "
  "not the mechanism - both run the standard-deed-reckoning circuit - it "
  "is the dials: how central the value (fairness vs fatherhood), how "
  "reversible the harm (a corrected credit vs an unrecoverable evening), "
  "how sticky the memory (a meeting vs a daughter's face). Same emotion, "
  "same machinery; one is a pang that teaches, the other is an ache that "
  "accompanies."),
 "how_it_works": ("The two snapshots work as a controlled comparison: hold "
  "the emotion constant and vary only the volume, and every difference "
  "traces back to the three dials. Maya's case: the value (fairness at "
  "work) matters but is not identity-central; the harm is fully reversible "
  "(the record can be corrected); the memory has few triggers. The circuit "
  "completes quickly - pang, repair, lesson - and the loop closes. Daniel's "
  "case: the value (being present for his child) is identity-central; the "
  "harm is irreversible (the evening cannot be re-lived); the memory is "
  "sticky (children, recitals, evenings all trigger it). The circuit cannot "
  "complete through repair of the original deed, so the loop keeps running "
  "and the mind must find other completions: changed conduct going forward, "
  "honest acknowledgment, self-forgiveness earned through a changed life. "
  "The comparison teaches the key diagnostic-free insight: intensity is not "
  "a measure of the person's goodness or brokenness - it is a measure of "
  "the dials. And the dials explain why good people can carry heavy remorse "
  "for years: the values at stake are the ones that define them."),
 "key_points": [
  "Low-intensity remorse is a pang that teaches and closes: wince, repair, lesson.",
  "High-intensity remorse is an ache that accompanies: the loop runs because the deed cannot be undone.",
  "The difference is the three dials - value centrality, harm reversibility, memory stickiness - not the person's character.",
  "Irreversible harm forces the circuit to complete through changed conduct rather than repair of the deed.",
  "Intensity measures the stakes of the values involved, never the goodness of the person."],
 "requirements": [
  "Tell two fictional snapshots at clearly different intensities of the same emotion.",
  "Trace every difference back to the three dials in plain words.",
  "Never imply the high-intensity person is worse or the low-intensity person is shallow.",
  "Keep both characters fictional and general; no real people."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people, no therapeutic promises."],
 "citations": [CIT_LAZARUS, CIT_BAUMEISTER],
 "sig_lens": ("The Signature lens reads the two snapshots as audits of different "
  "depth: Maya's is a spot check - quick, clean, closed the same week. Daniel's "
  "is a full forensic review of an unrecoverable entry. The Signature insight is "
  "that depth is not damage: the deepest audits belong to the people with the "
  "highest standards. Mastery at high intensity means accepting that some ledger "
  "entries close through a changed life rather than a fixed past - and then "
  "living the change so thoroughly that the audit becomes the foundation of "
  "integrity rather than its wreckage.")
},
{
 "key": "remorse_guilt_blend",
 "name": "Remorse Mixed With Guilt: The Most Common Partnership",
 "group": "Foundations", "ladder_rank": 8, "ladder_tier": "foundations",
 "description": ("Remorse almost never travels alone, and its most constant "
  "companion is guilt - the broader, everyday feeling of having done wrong. "
  "The two are so close that most people use the words interchangeably, but "
  "the blend has a texture worth naming. Guilt is the wide river: the "
  "general unease after cutting corners, the nagging sense of owing better. "
  "Remorse is the deep pool within it: the concentrated, aching reckoning "
  "with a specific wrong that violated a value you actually hold dear. When "
  "they mix, the experience goes like this: guilt sounds the general alarm "
  "(\"that was not right\"), and remorse focuses it into a beam (\"that "
  "specific choice, that person's face, that harm - and I am answerable\"). "
  "The blend is more motivating than either alone: guilt supplies the "
  "restless energy, remorse supplies the moral clarity about what exactly "
  "was wrong and what would make it right. People in this blend tend to do "
  "three things: confess or acknowledge the specific deed, make concrete "
  "restitution, and change the pattern that allowed it. The danger of the "
  "blend is only when the beam never widens back out - when a person stays "
  "locked on one deed so long that the reckoning becomes rumination, and "
  "the drive to repair curdles into self-punishment. The healthy version "
  "keeps the focus on the debt and the repair, not on endless self-trial."),
 "how_it_works": ("The partnership works because guilt and remorse share a "
  "circuit but play different roles in it. Guilt is the early-warning "
  "system: it fires fast, broadly, and often - the background conscience "
  "hum that flags questionable choices. Remorse is the deep-review system: "
  "it fires slower, narrower, and harder, reserved for violations of "
  "core values. When a deed trips both systems, they amplify each other: "
  "guilt's restlessness keeps the case open, remorse's depth keeps the "
  "focus on the specific wrong, and together they generate the strongest "
  "reparative drive in the moral-emotion family. The blend resolves the "
  "way a good investigation resolves: acknowledgment of the specific "
  "deed, restitution sized to the harm, and pattern change so it does not "
  "recur. It goes wrong the way investigations go wrong: when the "
  "investigator falls in love with the case and keeps re-trying it after "
  "the verdict is in and the sentence served. The line between remorse "
  "and rumination is the line between reviewing the evidence to act and "
  "reviewing the evidence to suffer - and the blend stays healthy exactly "
  "as long as the energy flows toward repair."),
 "key_points": [
  "Guilt is the broad early-warning hum; remorse is the deep, focused reckoning - the pool within the river.",
  "In the blend, guilt sounds the general alarm and remorse focuses it into a beam on the specific deed.",
  "Together they generate the strongest reparative drive: acknowledgment, restitution, pattern change.",
  "The blend turns unhealthy when the reckoning becomes rumination - re-trying the case after the verdict.",
  "Healthy remorse-guilt keeps the energy flowing toward repair, not toward endless self-punishment."],
 "requirements": [
  "Distinguish guilt and remorse clearly, then describe their blend as the most common partnership.",
  "Show both the motivating power and the rumination danger of the blend.",
  "Keep all illustrations fictional and general; no real people.",
  "Frame the blend as normal and functional, with a clear picture of its healthy resolution."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people, no therapeutic promises."],
 "citations": [CIT_TANGNEY, CIT_BAUMEISTER],
 "sig_lens": ("The Signature lens honors this blend as the conscience's full "
  "instrument panel: guilt is the warning light, remorse is the detailed "
  "diagnostic readout. Together they give both urgency and precision - the "
  "two things any real repair requires. The Signature caution is about the "
  "stall: a diagnostic that never leads to a fix is just a light left "
  "blinking. Mastery means letting the blend do its complete work - alarm, "
  "focus, repair, pattern change - and then letting the panel go dark, the "
  "case closed, the lesson forged into conduct.")
},
{
 "key": "remorse_day_vignette",
 "name": "A Day With Remorse: The Emotion Running Through an Ordinary Day",
 "group": "Foundations", "ladder_rank": 9, "ladder_tier": "foundations",
 "description": ("Follow one ordinary day with remorse riding along - a "
  "fictional composite, no real person. 6:40 a.m.: Elena wakes before the "
  "alarm, and before coffee the replay starts - yesterday's argument with "
  "her brother, the thing she said about his marriage that she knew was "
  "unfair even as it left her mouth. Her chest tightens. 9:15 a.m.: at her "
  "desk, she catches herself re-reading the same email three times; the "
  "scene keeps inserting itself between her and the screen. She drafts a "
  "text to him, deletes it, drafts it again. 12:30 p.m.: lunch with a "
  "friend, and when the friend mentions family, Elena goes quiet for a "
  "beat too long, then changes the subject a little too fast. The friend "
  "notices; Elena notices her noticing. 4:00 p.m.: the urge to confess "
  "spikes - she picks up the phone, puts it down. What would she even say? "
  "\"I am sorry\" feels too small for the unfairness of it and too big to "
  "say casually. 7:20 p.m.: cooking dinner, her hands on autopilot, the "
  "counterfactuals run: what she could have said, the pause she could have "
  "taken. 10:45 p.m.: in bed, the courtroom convenes for its nightly "
  "session. But something has shifted: during the day, the debt clarified. "
  "It is not a vague heaviness anymore; it is a specific apology owed, "
  "with specific words. She falls asleep mid-sentence, composing it. The "
  "day did not resolve the remorse - but it refined it, from fog into a "
  "task. That is what a day with remorse does: it distills the ache into "
  "an assignment."),
 "how_it_works": ("The vignette shows remorse's daily mechanics in motion. "
  "Morning ambush: the mind replays during low-demand moments (waking, "
  "showering, commuting) because the appraisal circuit finally has idle "
  "cycles. Attention hijacking: the loop inserts the scene between the "
  "person and the present task, which is why concentration frays - the "
  "replay is literally competing for working memory. Social leakage: the "
  "beat-too-long pause and the too-fast subject change are the emotion "
  "showing at the edges, the body and speech carrying what the mouth will "
  "not say. Approach-avoidance: the drafted-and-deleted text is the "
  "reparative drive colliding with fear of the conversation, so the urge "
  "oscillates. Counterfactual autopilot: during routine physical tasks, "
  "the mind rehearses better versions of the scene - the lesson being "
  "written. Nightly session: with the day's noise gone, the courtroom gets "
  "the floor, and the day's distillation turns fog into assignment. The "
  "arc of the day is the emotion doing its job: converting raw ache into "
  "a specific, actionable debt. Days like this repeat until the assignment "
  "is carried out - and that repetition is not malfunction, it is the "
  "system refusing to file an open ledger entry."),
 "key_points": [
  "Remorse ambushes during low-demand moments - waking, commuting, routine tasks - when the mind has idle cycles.",
  "The replay competes for working memory, which is why concentration frays during remorse.",
  "Social leakage (pauses, subject changes) shows the emotion at the edges before it is ever spoken.",
  "Draft-and-delete cycles are the reparative drive colliding with fear of the conversation.",
  "A day with remorse distills fog into assignment: the ache refines into a specific debt to pay."],
 "requirements": [
  "Tell the day as a timestamped vignette with a fictional character, ordinary and relatable.",
  "Show at least five distinct daily mechanics (ambush, hijacking, leakage, approach-avoidance, nightly session).",
  "End with the distillation insight: the day refines ache into assignment.",
  "No real people; keep the tone human and non-clinical throughout."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people, no therapeutic promises."],
 "citations": [CIT_LAZARUS, CIT_GROSS],
 "sig_lens": ("The Signature lens reads Elena's day as an audit in progress: every "
  "ambush is evidence surfacing, every deleted draft is the repair plan being "
  "revised, and the nightly session is the auditor writing up findings. The "
  "Signature lesson is the distillation itself - remorse, given honest daylight, "
  "does not stay fog; it becomes a work order. Mastery is not a day without the "
  "ache but a day that ends with the assignment written: specific words, specific "
  "repair, specific change. The forge runs all day; the master schedules the "
  "pour.")
},
{
 "key": "remorse_body_signals",
 "name": "What Remorse Does in the Body",
 "group": "Compounded", "ladder_rank": 10, "ladder_tier": "compounded",
 "description": ("Remorse is not just a thought with a bad mood attached; "
  "it moves through the body with a recognizable signature. The chest is "
  "usually first: a heaviness, tightness, or ache at the sternum, as if "
  "something were sitting on it - the classic \"heavy heart.\" The stomach "
  "follows: nausea, knotting, or a hollow gnawing, especially when the "
  "replay is vivid. Breathing turns shallow and sigh-heavy; people in "
  "remorse sigh more, long exhalations that the body uses to discharge "
  "tension. The heart may beat faster during acute spikes (the moment of "
  "confession, the confrontation) and settle into a dull, low-energy thrum "
  "during the long ache. Muscles carry it as tension in the jaw, neck, and "
  "shoulders, or as a drained, leaden fatigue in the limbs. Skin can flush "
  "or go pale; hands may tremble or go cold. Energy drops overall - remorse "
  "is expensive, and the body budgets accordingly, which is why a person "
  "deep in remorse can feel physically exhausted by nothing more than "
  "sitting and thinking. None of these signals are the emotion's "
  "\"symptoms\" in a medical sense; they are the body's side of the "
  "courtroom - the alarm sounding in flesh while the mind holds trial."),
 "how_it_works": ("The body signals follow from what remorse asks the "
  "organism to do: hold still, attend inward, and prepare for social "
  "repair. The chest heaviness and gut knot are the ancient alarm "
  "circuitry - the same systems that brace the body for threat - now "
  "aimed at a social-moral threat: the risk of being judged, rejected, or "
  "diminished in the eyes of others and oneself. Sighing is the body's "
  "pressure valve, resetting breathing patterns that go shallow under "
  "sustained attention to the replay. The jaw-neck-shoulder tension is the "
  "body bracing, as if for a blow, because the inner trial feels like one. "
  "The leaden fatigue is resource economics: the replay loop is "
  "cognitively expensive, burning the same fuel as hard mental work, so "
  "the body down-regulates everything else. The trembling hands and cold "
  "extremities are adrenaline's fingerprints during acute spikes - the "
  "confession moment, the apology, the feared confrontation - when the "
  "social stakes peak. Understanding the signals as functional - the body "
  "gearing for acknowledgment and repair - keeps them from being "
  "misread as mere breakdown."),
 "key_points": [
  "The chest heaviness (\"heavy heart\") and gut knot are remorse's most reported body signals.",
  "Breathing turns shallow and sigh-heavy; sighing is the body's pressure valve.",
  "Jaw, neck, and shoulder tension is the body bracing for the inner trial.",
  "Leaden fatigue is resource economics: the replay loop burns fuel like hard mental work.",
  "Acute spikes (confession, confrontation) add adrenaline fingerprints: racing heart, trembling, cold hands."],
 "requirements": [
  "Cover heart, breath, muscles, stomach, skin, and energy in plain words.",
  "Explain each signal functionally (what the body is gearing for), never clinically.",
  "Do not present any signal as a medical symptom or a diagnosis of anything.",
  "Keep examples fictional and general; no real people."],
 "standards": ["Descriptive and educational only - no diagnosis, no medical claims, no labels on real people."],
 "citations": [CIT_EKMAN, CIT_DARWIN],
 "sig_lens": ("The Signature lens reads the body as the audit's instrument panel "
  "made flesh: the heavy chest is the gauge showing load, the gut knot is the "
  "tension on the line, the sighs are the pressure releases. The body is not "
  "betraying the person - it is reporting, faithfully, the size of the debt the "
  "mind is carrying. Mastery listens to the panel instead of fighting it: the "
  "heaviness marks the value at stake, the fatigue marks the cost of an open "
  "ledger, and both ease as the repair work gets done.")
},
{
 "key": "remorse_posture_movement",
 "name": "The Posture and Movement Signature of Remorse",
 "group": "Compounded", "ladder_rank": 11, "ladder_tier": "compounded",
 "description": ("Remorse has a posture, and once you know it you will see "
  "it everywhere: the body makes itself smaller. The head lowers or tilts "
  "down, the gaze drops to the floor or fixes on some middle distance, the "
  "shoulders round forward and in, the chest caves slightly as if "
  "protecting the ache inside it. People in remorse touch their own faces "
  "more - a hand over the mouth, fingers pressed to the forehead or "
  "temples, the classic head-in-hands collapse when the wave peaks. "
  "Movement slows: the walk gets heavier, gestures shrink, the person "
  "takes up less space in chairs and doorways. There is a characteristic "
  "restlessness too - pacing during the replay, then sudden stillness when "
  "the scene grips. Some people go the other way and get busy with their "
  "hands: cleaning, fixing, organizing - the reparative drive leaking out "
  "as physical making-amends to the nearest available object. The walk of "
  "a person going to apologize is its own study: slow approach, pauses, "
  "the deep breath at the door. All of it is the body speaking the "
  "emotion's grammar: I am diminished, I am turned inward, I am preparing "
  "to make this right."),
 "how_it_works": ("The posture signature is a submission-and-repair display "
  "with deep roots. Making the body smaller - lowered head, averted gaze, "
  "rounded shoulders - is the ancient social signal of non-threat: \"I am "
  "no danger, do not cast me out.\" In remorse this display turns inward as "
  "well as outward; the person is signaling submission to their own "
  "judgment, not just to others'. The face-touching and head-holding are "
  "self-soothing behaviors, the body's way of applying comfort where no "
  "other comfort is available. The slowed, shrunken movement reflects the "
  "inward attention: the mind is in the replay, so the body idles. The "
  "pacing-then-stillness rhythm tracks the loop's intensity - pacing while "
  "the mind searches for the repair, stillness when the scene has full "
  "capture. The busy-hands phenomenon is the reparative drive finding the "
  "nearest outlet: unable to fix the past yet, the hands fix the present. "
  "Read together, posture and movement are remorse's most honest channel - "
  "harder to fake than words, quicker to read than confession."),
 "key_points": [
  "The core signature is making the body smaller: lowered head, dropped gaze, rounded shoulders.",
  "Face-touching and head-in-hands are self-soothing during peak waves.",
  "Movement slows and shrinks as attention turns inward to the replay.",
  "Pacing-then-stillness tracks the loop: searching for repair, then captured by the scene.",
  "Busy hands (cleaning, fixing) are the reparative drive leaking into the nearest available task."],
 "requirements": [
  "Describe the full posture signature - head, gaze, shoulders, chest, hands - in plain words.",
  "Cover movement: slowed gait, shrunken gestures, pacing, and the busy-hands outlet.",
  "Explain the signature functionally as a submission-and-repair display, never clinically.",
  "Keep all descriptions general and fictional; no real people."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people, no therapeutic promises."],
 "citations": [CIT_DARWIN, CIT_EKMAN],
 "sig_lens": ("The Signature lens reads the shrunken posture as the auditor "
  "bowing over the evidence - not groveling, but leaning in close to read the "
  "fine print of what happened. The body makes itself small because the "
  "attention has gone deep. And the busy hands are the forge already warming "
  "up: repair energy looking for a first outlet. Mastery straightens the "
  "spine at the right moment - not to deny the debt, but to walk it to the "
  "creditor's door. The bowed head reads the ledger; the lifted head pays it.")
},
{
 "key": "remorse_sleep_appetite_energy",
 "name": "Remorse, Sleep, Appetite, and Energy",
 "group": "Compounded", "ladder_rank": 12, "ladder_tier": "compounded",
 "description": ("Ask anyone who has carried heavy remorse and they will "
  "tell you: it gets into the basics - sleep, food, and fuel. Sleep is "
  "usually hit first and hardest. The replay loop loves the dark and the "
  "quiet: with the day's noise gone, the courtroom gets the floor, and "
  "people find themselves staring at the ceiling running the scene on a "
  "loop. Falling asleep gets difficult; staying asleep gets fragile; "
  "3 a.m. wakefulness with the full trial in session is the classic "
  "pattern. Appetite typically drops - the gut knot and nausea make food "
  "unappealing, and some people simply forget to eat, running on coffee "
  "and momentum. A smaller number go the other way, eating for the brief "
  "comfort and distraction it provides. Energy follows the loop's budget: "
  "the replay is cognitively expensive, so the body rations everything "
  "else - the leaden limbs, the canceled plans, the sense of moving "
  "through water. Concentration frays because working memory is occupied. "
  "None of this is mysterious once the mechanism is visible: a mind "
  "running a high-priority background process will starve every other "
  "process of resources. The good news hidden in the pattern is that the "
  "basics recover as the ledger closes - apology made, repair underway, "
  "pattern changed - and sleep is often the first thing to come back, "
  "like a signal that the trial has adjourned."),
 "how_it_works": ("The mechanism is resource competition plus arousal. The "
  "replay loop is a high-priority cognitive process: it demands working "
  "memory, attention, and emotional processing, and the brain pays for it "
  "out of the same budget as everything else - hence the fatigue, the "
  "frayed concentration, the sense of heaviness. Sleep suffers for two "
  "reasons: cognitive arousal (the loop will not release the mind at bedtime) "
  "and the loss of the day's distractions that normally keep the loop at "
  "background volume. Appetite drops because the gut is part of the alarm "
  "circuitry - nausea and knotting are the enteric nervous system responding "
  "to sustained emotional arousal - and because eating requires the body to "
  "stand down from alert, which it will not do mid-trial. The minority "
  "pattern of overeating is the same circuitry seeking the brief "
  "parasympathetic soothing that food provides. Recovery of the basics is "
  "therefore a genuine signal, not a coincidence: when sleep returns, it "
  "means the loop has released its priority claim - usually because the "
  "reparative drive found its outlet and the ledger entry got its answer."),
 "key_points": [
  "Sleep is hit first: the replay loop loves the dark, producing ceiling-staring and 3 a.m. trial sessions.",
  "Appetite usually drops - gut alarm plus the body's refusal to stand down from alert; a minority eat for comfort.",
  "Energy drains because the replay is cognitively expensive: the brain rations fuel away from everything else.",
  "Concentration frays: working memory is occupied by the loop.",
  "Recovery of sleep and appetite is a real signal that the ledger is closing - the trial adjourning."],
 "requirements": [
  "Cover sleep, appetite (both directions), energy, and concentration in plain words.",
  "Explain each through resource competition and arousal, never in clinical terms.",
  "Do not present any pattern as a medical symptom or diagnosis.",
  "End with the recovery signal: the basics returning means the loop is releasing."],
 "standards": ["Descriptive and educational only - no diagnosis, no medical claims, no labels on real people."],
 "citations": [CIT_GROSS, CIT_LAZARUS],
 "sig_lens": ("The Signature lens treats the ravaged basics as the audit's "
  "overtime bill: a full review running around the clock burns the body's "
  "reserves, and the 3 a.m. sessions are the auditors working the night "
  "shift. The Signature reading is practical, not fearful: protect the "
  "basics where you can - regular meals, wind-down routines, daylight - "
  "because a depleted auditor makes poor judgments. And watch for the "
  "return of sleep as the earliest instrument reading that the repair is "
  "working: the forge cooling because the pouring is done.")
}
,
{
 "key": "remorse_body_differences",
 "name": "How Remorse Feels Different in Different Bodies",
 "group": "Compounded", "ladder_rank": 13, "ladder_tier": "compounded",
 "description": ("No two bodies carry remorse identically, and the "
  "differences are not random - they follow temperament, habit, and "
  "history. Some people feel remorse primarily in the chest: the heavy "
  "heart dominates, and the emotion announces itself as pressure behind "
  "the sternum. Others feel it in the gut: nausea, knotting, appetite "
  "loss lead, and the chest is quiet. Some get the hot version - flushed "
  "face, restless pacing, an urge to move - while others get the cold "
  "version: stillness, pallor, a drained heaviness in the limbs. Expressive "
  "temperaments externalize quickly: tears, audible sighs, visible "
  "agitation. Reserved temperaments go still and silent, and the storm "
  "is all interior - which can mislead observers into thinking nothing "
  "is happening. Age matters too: children tend to feel remorse as a "
  "global, physical misery and confess quickly to end it; adults localize "
  "it more (chest, gut, jaw) and can sustain the loop far longer. People "
  "with harsh inner standards feel remorse louder and longer for the same "
  "deed than people with flexible standards - the same alarm, different "
  "calibration. None of these patterns is more \"real\" than the others. "
  "The emotion is the same circuit; the body it runs on, the temperament "
  "it filters through, and the standards it answers to make each person's "
  "remorse their own."),
 "how_it_works": ("The variation comes from three sources. First, "
  "physiology: people differ in interoception - how strongly they feel "
  "internal body signals - so the same alarm registers as chest pressure "
  "in one person and gut churn in another. Second, temperament and "
  "learned expression style: high-expressiveness people discharge arousal "
  "outward (tears, pacing, sighs), low-expressiveness people hold it "
  "inward (stillness, silence), and both are feeling the full emotion. "
  "Third, calibration: the inner standard's strictness sets the alarm's "
  "gain, so identical deeds produce different volumes in different "
  "consciences - and the same person can feel a deed differently at "
  "twenty and at fifty, as standards mature. Developmental stage adds a "
  "fourth factor: the self-conscious machinery deepens with age, so "
  "children's remorse is simpler, more physical, and shorter-lived, "
  "while adult remorse can sustain complex replay and moral abstraction "
  "for years. The practical upshot: never judge the depth of someone's "
  "remorse by how loudly their body performs it. The quietest carrier in "
  "the room may be running the heaviest loop."),
 "key_points": [
  "Some bodies lead with the chest, others with the gut; some run hot (flushed, restless), others cold (still, drained).",
  "Expressive temperaments discharge outward; reserved temperaments hold the storm interior - both feel it fully.",
  "Children feel remorse as global physical misery and confess fast; adults localize it and sustain the loop longer.",
  "Inner-standard strictness calibrates the alarm's gain: same deed, different volumes in different consciences.",
  "Never judge remorse's depth by its volume: the quietest carrier may run the heaviest loop."],
 "requirements": [
  "Describe at least four axes of difference: body location, hot vs cold, expressive vs reserved, age.",
  "Explain each axis through physiology, temperament, or calibration - never clinically.",
  "Warn explicitly against judging depth by outward volume.",
  "Keep all illustrations fictional and general; no real people."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people, no therapeutic promises."],
 "citations": [CIT_IZARD, CIT_EKMAN],
 "sig_lens": ("The Signature lens reads bodily difference as instrument "
  "variation, not instrument failure: the same audit runs on different "
  "hardware, and every panel reports in its own dialect. The Signature "
  "discipline is to learn your own panel's language - where YOUR remorse "
  "lives, how YOUR loop signals - because mastery of the emotion starts "
  "with literacy in your own body. And the same discipline applies outward: "
  "read others' panels in their dialect, not yours, before you decide what "
  "they are carrying.")
},
{
 "key": "remorse_face",
 "name": "The Face of Remorse: Eyes, Brows, Mouth, and Micro-Signs",
 "group": "Compounded", "ladder_rank": 14, "ladder_tier": "compounded",
 "description": ("Remorse writes itself on the face in a script made of "
  "small, downward movements. The eyes: gaze drops or slides away, "
  "especially during the moment of acknowledgment; when the eyes do meet "
  "another's, they are often wet or reddened, with a pleading softness - "
  "the look of someone asking to be seen as sorry. The brows: the inner "
  "corners lift and draw together, the classic grief-muscle pattern that "
  "remorse shares with sadness - the forehead may show short horizontal "
  "creases in the center. The mouth: corners pull down and slightly back, "
  "lips press together or tremble; in the apology moment the mouth may "
  "open and close without words at first, the body rehearsing what the "
  "voice is afraid to say. The micro-signs are where remorse leaks most "
  "honestly: the quick downward flick of the eyes when the deed is named, "
  "the swallow before the hard sentence, the brief nose-wrinkle of "
  "self-disgust at the memory, the hand that rises halfway to the face "
  "and stops. The whole face tends downward and inward - nothing in "
  "remorse's expression reaches outward or up. It is the face of a person "
  "turned toward an inner courtroom, with the proceedings showing at the "
  "windows."),
 "how_it_works": ("The face of remorse is a composite signal built from "
  "borrowed parts. The inner-brow raise is shared with sadness and grief - "
  "it is the face's general \"loss and pain\" marker, and remorse borrows "
  "it because remorse includes the pain of the harm done. The gaze "
  "aversion and lowered head are the submission display: breaking eye "
  "contact reduces the social threat of being seen and judged, which is "
  "why the eyes drop hardest exactly when the deed is named aloud. The "
  "down-turned mouth and pressed lips are the suppression signature - the "
  "face holding back what the voice is not ready to release, whether tears "
  "or confession. The micro-signs (the flick, the swallow, the aborted "
  "hand) are leakage: brief moments when the control system slips and the "
  "underlying affect shows through for a fraction of a second. Together "
  "they form one of the most readable faces in the emotion family, because "
  "remorse's signal is designed to be read: it is an appeasement display, "
  "evolved to show the group \"I acknowledge the wrong; do not cast me "
  "out,\" and readability is its function."),
 "key_points": [
  "Eyes drop or slide away, hardest at the moment the deed is named; when held, they are wet and pleading.",
  "Inner brows lift and draw together - the grief-muscle pattern remorse shares with sadness.",
  "Mouth corners pull down, lips press or tremble; the mouth may rehearse wordlessly before the apology comes.",
  "Micro-signs leak most honestly: the eye flick, the swallow, the nose-wrinkle of self-disgust, the aborted hand.",
  "The whole face moves down and inward - remorse's expression is built to be read as appeasement."],
 "requirements": [
  "Describe eyes, brows, mouth, and at least four micro-signs in plain, concrete words.",
  "Explain each region functionally (submission, suppression, leakage), never clinically.",
  "Note that the face is designed to be readable - appeasement is its function.",
  "No real people, no real faces described; keep everything general."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people."],
 "citations": [CIT_EKMAN, CIT_DARWIN],
 "sig_lens": ("The Signature lens reads the remorseful face as the audit made "
  "visible: every downward movement is the attention turning inward to the "
  "evidence, every micro-sign is a finding escaping before the report is "
  "written. The face is honest because the emotion's function demands "
  "honesty - appeasement only works if it is believed. The Signature "
  "discipline: let the face tell the truth it is trying to tell. A face "
  "allowed to show remorse is already halfway to the apology; a face forced "
  "to hide it bottles the audit and starves the repair.")
},
{
 "key": "remorse_face_intensity",
 "name": "The Face of Remorse Across Intensities",
 "group": "Compounded", "ladder_rank": 15, "ladder_tier": "compounded",
 "description": ("The face of remorse is not one mask but a gradient, and "
  "the gradient tells you where in the emotion a person is. At low "
  "intensity: a brief wince - the eyes flick down for half a second, the "
  "mouth corners dip, and then the face resets; most observers miss it "
  "entirely, and the person may not even know they showed it. At moderate "
  "intensity: the expression settles in and stays - sustained gaze "
  "aversion, the inner-brow lift held for minutes, pressed lips, the "
  "occasional deep sigh through the nose; the face looks weighed down, "
  "and strangers can read that something is wrong even if they cannot "
  "name it. At high intensity: the face comes apart at the edges - tears "
  "or the visible fight against them, the mouth trembling openly, the "
  "head dropping into the hands, the whole countenance crumpling under "
  "the load; this is the face people remember from the apology that "
  "mattered, the confession that cost everything. The gradient matters "
  "for reading others: a flicker means a pang is passing through, a "
  "settled heaviness means the loop is running, and a crumpling face "
  "means the peak is here and the person needs either space or a witness - "
  "rarely advice. And it matters for honesty with oneself: the face often "
  "shows the true volume before the mind admits it."),
 "how_it_works": ("Facial intensity tracks the underlying arousal and the "
  "control system's load. At low intensity, the affect is brief and the "
  "control system easily overrides it - hence the half-second flicker: "
  "the signal fires, control catches it, the face resets. At moderate "
  "intensity, the affect is sustained and control can only dampen, not "
  "erase, the display - hence the settled heaviness: the signal is "
  "continuously generated and continuously half-suppressed. At high "
  "intensity, the affect overwhelms control - hence the crumpling: the "
  "suppression system fails and the full display breaks through, including "
  "the autonomic components (tears, trembling) that cannot be willed "
  "away. This is why the face is a reliable volume meter: unlike words, "
  "which can be edited, the face's gradient reflects the real-time "
  "balance between feeling and control. Observers intuitively read this "
  "gradient - the flicker gets a pass, the heaviness gets a concerned "
  "look, the crumpling gets an arm around the shoulder or a respectful "
  "withdrawal - because the appeasement function scales with the display."),
 "key_points": [
  "Low: a half-second wince - eyes flick down, mouth dips, face resets; usually missed.",
  "Moderate: sustained heaviness - held gaze aversion, pressed lips, the face looks weighed down.",
  "High: the face crumples - tears or the fight against them, trembling mouth, head in hands.",
  "The gradient reflects the real-time balance between feeling and control - a reliable volume meter.",
  "Observers intuitively scale their response: a pass for the flicker, concern for the heaviness, space or witness for the crumple."],
 "requirements": [
  "Describe the face at three clearly separated intensities with concrete visible detail.",
  "Explain the gradient through the feeling-vs-control balance, never clinically.",
  "Give the practical reading guidance: what each level calls for from an observer.",
  "No real people or faces; keep everything general."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people."],
 "citations": [CIT_EKMAN, CIT_GROSS],
 "sig_lens": ("The Signature lens reads the gradient as the audit's progress bar "
  "made visible: the flicker is a finding noted in passing, the heaviness is the "
  "review in session, the crumple is the full reckoning breaking through. The "
  "Signature discipline is to match the response to the reading - never demand "
  "a crumple for a flicker-level debt, and never wave away a crumple as "
  "overreaction. Mastery reads the true volume in the face, honors what it "
  "reports, and answers at the scale the reading requires.")
},
{
 "key": "remorse_hiding_faking",
 "name": "Hiding or Faking Remorse: What Leaks Through",
 "group": "Compounded", "ladder_rank": 16, "ladder_tier": "compounded",
 "description": ("People try to hide remorse and fake remorse for opposite "
  "reasons, and the face and body betray both attempts in characteristic "
  "ways. Hiding: the person feeling remorse who cannot afford to show it - "
  "at work, in a negotiation, before someone they fear - will clamp the "
  "display down: jaw tightens, face goes flat, eyes lock into deliberate "
  "neutral. What leaks: the suppression itself shows - the too-still face, "
  "the swallow that comes from nowhere, the blink rate climbing, the hands "
  "suddenly busy or suddenly frozen. The voice often gives it away first: "
  "flattened tone with micro-tremors on the hard words. Faking: the person "
  "performing remorse they do not feel - the strategic apology - will "
  "overplay the vocabulary (long, polished apologies with no specific "
  "deed named) and underplay the involuntary: the brow lift is held a beat "
  "too long, the sigh is placed rather than escaping, the eyes perform "
  "downwardness while the body stays relaxed and open. What leaks: the "
  "absence of the hard parts - no tremor, no genuine swallow, no "
  "micro-flicker when the deed is named, because there is no inner "
  "courtroom running. The timing is wrong too: real remorse's face moves "
  "before the words; performed remorse's words arrive first and the face "
  "follows like a costume change. None of this makes anyone a human lie "
  "detector - the signs are tendencies, not proof - but they explain why "
  "instinct so often distrusts the polished apology and trusts the "
  "stumbling one."),
 "how_it_works": ("Hiding fails because suppression is itself visible: the "
  "control system can dampen the voluntary muscles of the face, but the "
  "autonomic components (swallowing, blinking, vocal tremor) and the "
  "timing of the display escape deliberate control, and observers - who "
  "evolved to read appeasement - pick up the mismatch between the flat "
  "mask and the leaking channels. Faking fails in the opposite direction: "
  "the performer can stage the voluntary components (the words, the "
  "posed brow, the placed sigh) but cannot stage the involuntary ones, "
  "because there is no underlying affect driving them - and crucially, "
  "cannot stage the timing, because real remorse's display leads the "
  "words (the face knows before the mouth speaks) while performed "
  "remorse's display follows them. The asymmetry is the tell: hiding "
  "leaks feeling through control, faking leaks control through feeling's "
  "absence. This is also why the stumbling apology reads as true: the "
  "disfluencies, the wrong words, the face moving ahead of the mouth are "
  "exactly what the real circuit produces, and exactly what a performance "
  "smooths away."),
 "key_points": [
  "Hiding leaks through suppression itself: the too-still face, the nowhere swallow, climbing blink rate, micro-tremors in the voice.",
  "Faking leaks through absence: no tremor, no genuine swallow, no flicker when the deed is named - no inner courtroom running.",
  "Timing is the deepest tell: real remorse's face moves before the words; performed remorse's words arrive first.",
  "The polished apology reads false and the stumbling one reads true because disfluency is what the real circuit produces.",
  "These are tendencies, not proof - no one becomes a human lie detector from a checklist."],
 "requirements": [
  "Cover hiding and faking separately, with distinct leakage signatures for each.",
  "Name the timing asymmetry (face-before-words vs words-before-face) as the deepest tell.",
  "Include the explicit caution: tendencies, not proof; no lie-detector claims.",
  "Keep all illustrations fictional and general; no real people."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people."],
 "citations": [CIT_EKMAN, CIT_GROSS],
 "sig_lens": ("The Signature lens treats hidden remorse as an audit conducted "
  "in a locked room - the findings are real, but no one can act on them, "
  "including the auditor. The Signature counsel: find one safe witness, "
  "because an audit with no reader never closes. And faked remorse is the "
  "audit report written before the evidence was examined - the Signature "
  "system rejects it outright, because a forged audit corrupts the whole "
  "ledger. Mastery demands the real thing in both directions: show what "
  "you feel, and feel what you show.")
},
{
 "key": "remorse_expression_gallery",
 "name": "Remorse in Words for Artists and Actors",
 "group": "Compounded", "ladder_rank": 17, "ladder_tier": "compounded",
 "description": ("For the painter, the actor, the writer: here is remorse "
  "as a set of playable, drawable instructions. The baseline: a person "
  "sitting slightly collapsed, as if the chair were a size too big - "
  "spine curved, shoulders rolled forward, head tipped down ten degrees "
  "past neutral. The eyes: looking down and to the side, or fixed on "
  "nothing; when they lift to another face, they arrive wet and drop "
  "again within two seconds - the gaze cannot hold. The brows: inner "
  "corners raised, pulling the forehead into short center creases; hold "
  "this and the whole face reads as pained sincerity. The mouth: "
  "press the lips, pull the corners down a fraction, and let the lower "
  "lip tremble once before stilling it - that single tremble is worth a "
  "page of dialogue. The hands: one hand half-raised toward the face, "
  "fingers hovering, then dropping - or both hands clasped too tightly "
  "in the lap, knuckles pale. For the apology scene: start with the "
  "swallow - visible in the throat - then the eyes drop, then the words "
  "come out in the wrong order, then the face moves ahead of the mouth "
  "into the crumple the speaker is fighting. For the solitary scene: "
  "head in hands is the cliché because it is true - but the fresher "
  "choice is the paused doorway: the character stops mid-step, hand on "
  "the frame, staring at nothing for three beats while the replay runs. "
  "The color of the scene is always inward and down; nothing in remorse "
  "reaches up or out."),
 "how_it_works": ("These notes work because they translate the emotion's "
  "mechanics into craft: every instruction is a real signal from the "
  "display system, sequenced the way the circuit actually fires. The "
  "collapsed baseline is the submission posture; the two-second gaze "
  "limit is the appeasement timing; the single lip tremble is the "
  "suppression system slipping once - more would be melodrama, less "
  "would be numbness. The apology-scene sequence (swallow, eye-drop, "
  "wrong-order words, face ahead of mouth) reproduces the real "
  "temporal order: autonomic leak, submission display, cognitive "
  "disfluency, affect overwhelming control. The paused doorway works "
  "because it shows the replay's signature interruption of motion - the "
  "body idling while the mind is captured - which audiences read "
  "instantly without a word of explanation. The craft principle "
  "throughout: remorse is downward, inward, and slightly behind the "
  "words. Play the delay - the beat between the feeling and its "
  "expression - and the audience will supply the courtroom themselves."),
 "key_points": [
  "Baseline: collapsed sitting, head tipped down, shoulders rolled - the chair a size too big.",
  "Eyes drop and cannot hold another's gaze longer than about two seconds.",
  "The single lip tremble, then stilled, is worth a page of dialogue.",
  "Apology sequence: swallow, eye-drop, wrong-order words, face moving ahead of the mouth.",
  "The paused doorway - stopped mid-step, staring at nothing - shows the replay capturing the body."],
 "requirements": [
  "Write as direct craft instructions for artists, actors, and writers.",
  "Cover baseline posture, eyes, brows, mouth, hands, the apology scene, and the solitary scene.",
  "Ground each instruction in the real signal mechanics, in plain words.",
  "Keep the tone practical and vivid, never clinical."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people."],
 "citations": [CIT_DARWIN, CIT_EKMAN],
 "sig_lens": ("The Signature lens gives the artist one governing image: the "
  "auditor bowed over the evidence. Every choice - the downward head, the "
  "hovering hand, the paused step - serves that single picture of a person "
  "examining what they did with unbearable closeness. The Signature note to "
  "the performer: do not play the suffering, play the examination. Suffering "
  "is the exhaust; the examination is the engine. Play the engine - the "
  "replay running behind the eyes, the verdict forming - and the suffering "
  "will arrive on its own, honest and unforced.")
},
{
 "key": "remorse_classic_triggers",
 "name": "The Classic Triggers of Remorse",
 "group": "Compounded", "ladder_rank": 18, "ladder_tier": "compounded",
 "description": ("Certain situations trigger remorse so reliably they are "
  "practically the emotion's native habitat. The spoken wound: words said "
  "in anger or carelessness that cannot be unsaid - the insult, the "
  "revelation, the cruel honesty - with the other person's face at the "
  "moment of impact burned into memory. The betrayal: breaking a trust "
  "placed in you - the affair, the leaked secret, the promise made and "
  "quietly abandoned - where the wrong is measured against the trust that "
  "preceded it. The neglected duty: the call not made, the visit "
  "postponed, the help not offered, especially when the window closes "
  "permanently - the empty chair at the recital, the hospital visit that "
  "came a day late. The harm by action: the reckless drive, the careless "
  "mistake at work that cost someone, the physical carelessness with "
  "real consequences. The moral compromise: the corner cut, the lie told "
  "for advantage, the silence kept when speaking up was owed - wrongs "
  "against the person's own code, witnessed by no one but the conscience. "
  "And the words of others: the direct accusation (\"you knew what you "
  "were doing\"), the disappointed quiet of someone respected, the "
  "victim's plain account of what it felt like - each one a key turning "
  "in the circuit. What unites them: a deed (or omission) that collides "
  "with a believed standard, plus a harm - to another or to the self's "
  "own code - that the mind cannot un-know."),
 "how_it_works": ("Each classic trigger fires the same three-part circuit, "
  "which is why they feel like variations on one theme. The spoken wound "
  "and the betrayal supply the deed plus vivid encoding - the other "
  "person's face at impact gives the memory its stickiness. The neglected "
  "duty is the omission variant: the circuit fires on what was NOT done, "
  "and the permanence of the closed window (the recital that will not be "
  "repeated) maximizes the irreversibility dial. Harm by action adds "
  "causal clarity - the line from choice to consequence is unbroken, so "
  "the verdict lands without appeal. Moral compromise is the pure "
  "conscience variant: no victim need be present, because the standard "
  "violated is the person's own code, and the audience is internal. The "
  "words of others work as external appraisals that force the internal "
  "one: the accusation, the disappointed quiet, the victim's account each "
  "supply the perspective the mind uses to judge itself. Triggers are not "
  "the emotion; they are the keys. The circuit - standard, deed, "
  "reckoning - is the lock, and it only turns where a conscience is "
  "already installed."),
 "key_points": [
  "The spoken wound: cruel or careless words that cannot be unsaid, with the impact-face burned into memory.",
  "Betrayal and neglected duty: trust broken, or the call unmade before the window closed permanently.",
  "Harm by action and moral compromise: clear causal lines, or wrongs against one's own code with no witness but conscience.",
  "Others' words - accusation, disappointed quiet, the victim's account - force the internal appraisal.",
  "Every trigger is a key; the standard-deed-reckoning circuit is the lock, and it only turns where conscience is installed."],
 "requirements": [
  "Name and describe at least six classic trigger families in plain words.",
  "Include both acts and omissions, and both harms to others and wrongs against one's own code.",
  "Explain the shared circuit behind the variety.",
  "All scenarios fictional and general; no real people or events."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people."],
 "citations": [CIT_LAZARUS, CIT_BAUMEISTER],
 "sig_lens": ("The Signature lens catalogs the triggers as the audit's standard "
  "case files: the spoken wound, the broken trust, the closed window, the "
  "careless harm, the compromised code. Every auditor should know these files "
  "by heart - not to fear them, but to recognize the investigation the moment "
  "it opens. The Signature discipline: when a classic trigger fires, open the "
  "file deliberately instead of letting it ambush you at 3 a.m. Name the deed, "
  "name the standard, name the debt - and the trigger becomes the first page "
  "of the repair plan instead of the first night of the siege.")
}
,
{
 "key": "remorse_personal_triggers",
 "name": "Personal Triggers: Memory, Anniversaries, Private Associations",
 "group": "Compounded", "ladder_rank": 19, "ladder_tier": "compounded",
 "description": ("Beyond the universal triggers, every person carries a "
  "private set - keys cut for their lock alone. Anniversaries: the date "
  "of the deed, the birthday of the person harmed, the season when it "
  "happened - the calendar itself becomes a trigger, and the week before "
  "the date the loop starts warming up without any new event. Places: "
  "the restaurant where the words were said, the street, the house - "
  "returning to the coordinates replays the scene at full volume. "
  "Sensory keys: a song that was playing, a smell, a particular quality "
  "of evening light - the memory was encoded with these details, and "
  "they retrieve it whole. Private associations: the joke that is no "
  "longer funny because of what followed it, the photograph that now "
  "reads differently, the object that was a gift from the person harmed - "
  "ordinary things conscripted into the replay. Milestones: watching "
  "someone else's child reach the age yours was, attending the event you "
  "missed the second time around - the present staging a reenactment the "
  "past cannot attend. These triggers are invisible to everyone but the "
  "carrier, which is why personal remorse can look motiveless from the "
  "outside: a person goes quiet at a dinner party and no one knows the "
  "song playing is the one from that night. The privacy of the trigger "
  "is part of its power - and part of why speaking the deed aloud, to "
  "one trusted witness, loosens its grip."),
 "how_it_works": ("Personal triggers work through state-dependent and "
  "cue-dependent memory: the scene of the deed was encoded under strong "
  "emotion, and strong encoding binds the central event to its context - "
  "dates, places, sensory details, associated objects. Later, any bound "
  "cue retrieves the whole package with its original emotional charge, "
  "which is why a song can reopen a years-old case in four bars. "
  "Anniversaries add anticipation: the mind, having learned the pattern, "
  "begins the loop ahead of the date - a kind of emotional muscle memory. "
  "Milestones work by comparison: the present supplies the counterfactual "
  "the mind would otherwise have to construct (\"this is what that evening "
  "could have been\"), making the replay unusually vivid. The invisibility "
  "to others follows from the privacy of the binding: no one else was "
  "there for the encoding, so no one else can see the cue for what it is. "
  "Speaking the association aloud works because it moves the trigger from "
  "the private, automatic system into shared, deliberate discourse - the "
  "cue loses some of its ambush power once it has been named and witnessed."),
 "key_points": [
  "Anniversaries turn the calendar into a trigger; the loop often warms up in the week before the date.",
  "Places, songs, smells, and light retrieve the encoded scene whole - cue-dependent memory.",
  "Ordinary objects (gifts, photographs, jokes) get conscripted into the replay.",
  "Milestones stage reenactments: the present supplies the counterfactual the mind would otherwise construct.",
  "The triggers are invisible to others, which is why personal remorse can look motiveless - naming them loosens their grip."],
 "requirements": [
  "Cover anniversaries, places, sensory keys, private associations, and milestones.",
  "Explain the memory mechanics (cue-dependent retrieval) in plain words.",
  "Address the invisibility-to-others aspect and the relief of naming the trigger.",
  "All illustrations fictional and general; no real people."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people."],
 "citations": [CIT_LAZARUS, CIT_GROSS],
 "sig_lens": ("The Signature lens files personal triggers as the audit's "
  "private evidence locker: case files only the auditor can open, keyed to "
  "dates, places, and songs no one else would recognize. The Signature "
  "discipline is to inventory the locker deliberately - write down the dates, "
  "name the songs - because an ambush you have cataloged is a review you "
  "can schedule. Mastery turns the private triggers from landmines into "
  "calendar entries: known, expected, prepared for, and each year a little "
  "quieter as the repairs accumulate.")
},
{
 "key": "remorse_surprise_triggers",
 "name": "Surprise Triggers: The Unexpected Sparks of Remorse",
 "group": "Compounded", "ladder_rank": 20, "ladder_tier": "compounded",
 "description": ("Some remorse arrives from nowhere - no anniversary, no "
  "obvious reminder, just an ordinary moment that unexpectedly opens the "
  "case file. The stranger's story: a podcast guest describes a deed "
  "uncomfortably close to yours, and suddenly you are not listening to "
  "them anymore - you are re-trying your own case. The child's question: "
  "a kid asks an innocent moral question (\"why would someone lie about "
  "that?\") and the simplicity of it lands like a gavel. The fiction "
  "ambush: a novel, film, or song stages your exact situation with "
  "fictional people, and the distance that should make it safe is "
  "precisely what lets the guard down. The praise that stings: someone "
  "compliments your integrity, and instead of warming you it indicts you - "
  "the gap between the compliment and the hidden deed becomes the whole "
  "room. The good fortune of others: witnessing someone enjoy the very "
  "thing your deed damaged in another - the intact friendship, the "
  "unbroken trust - and feeling the contrast like a weight. The quiet "
  "moment: no trigger at all that you can name, just stillness, and into "
  "the stillness walks the scene, uninvited. Surprise triggers share one "
  "trait: they bypass the defenses that the known triggers have trained. "
  "You have armor for the anniversary; you have none for the child's "
  "question. That is why they hit so hard - and why, paradoxically, they "
  "are often the moments when the real work finally begins, because the "
  "unguarded mind cannot dodge the verdict."),
 "how_it_works": ("Surprise triggers work by approaching the circuit "
  "sideways. The known triggers - anniversaries, places - are guarded: "
  "the mind has built anticipatory defenses (bracing, distraction "
  "plans, scheduled busyness). The surprise trigger carries no such "
  "warning, so it reaches the appraisal system unopposed. Each type has "
  "its own sideways route: the stranger's story and the fiction ambush "
  "use identification - the mind maps the fictional deed onto the real "
  "one before the defenses recognize the mapping. The child's question "
  "uses moral simplicity - the uncluttered standard against which the "
  "deed looks stark. The stinging praise uses contrast - the believed "
  "standard is held up shining, and the deed's shadow falls across it. "
  "The good fortune of others uses counterfactual vividness - the "
  "undamaged version made visible. The quiet moment uses undefended "
  "attention - with nothing else occupying working memory, the loop "
  "claims it by default. The paradoxical productivity of surprise "
  "triggers follows: because the verdict lands unguarded, the mind is "
  "more likely to accept it fully - and acceptance is the doorway to "
  "genuine repair."),
 "key_points": [
  "Surprise triggers bypass the defenses built for known triggers - no armor for the child's question.",
  "The stranger's story and fiction ambush work through identification: the mind maps the fictional deed onto the real one.",
  "Stinging praise works through contrast: the shining standard makes the deed's shadow fall harder.",
  "The quiet moment works through undefended attention: stillness lets the loop claim working memory by default.",
  "Because the verdict lands unguarded, surprise triggers often start the real repair work."],
 "requirements": [
  "Describe at least five surprise trigger types with the sideways route each one takes.",
  "Explain why they hit harder than guarded triggers, in plain words.",
  "End with the paradox: unguarded verdicts often begin genuine repair.",
  "All illustrations fictional and general; no real people."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people."],
 "citations": [CIT_LAZARUS, CIT_IZARD],
 "sig_lens": ("The Signature lens treats surprise triggers as unannounced "
  "inspections: the auditors arrive without warning, and the facility is "
  "seen as it truly is. The Signature response is not to dread them but "
  "to use them - the unguarded verdict is the most honest reading the "
  "instrument ever gives. Mastery keeps a notebook by the ambush: when "
  "the child's question or the stranger's story opens the file, write "
  "down what the unguarded mind concluded. That note, taken without "
  "armor, is often the truest page in the whole audit.")
},
{
 "key": "remorse_chain_reactions",
 "name": "Chain Reactions: One Trigger, a Cascade of Emotions",
 "group": "Compounded", "ladder_rank": 21, "ladder_tier": "compounded",
 "description": ("Remorse rarely arrives as a single feeling; one trigger "
  "typically sets off a cascade, and the cascade has a recognizable order. "
  "First, the shock of recognition: the trigger lands and the scene "
  "replays - a half-second of pure remorse, the deed seen clearly. Second, "
  "shame arrives: the focus slides from the deed to the self - \"what kind "
  "of person does that?\" - and the face heats, the gaze drops. Third, "
  "sadness: the harm itself comes into view - the other person's pain, "
  "the thing lost - and the chest heaviness deepens into grief for what "
  "cannot be restored. Fourth, anger - often at the self: the jaw "
  "tightens, the inner voice turns vicious (\"stupid, stupid\"), and some "
  "people feel the flash outward too, snapping at whoever is nearest, "
  "which then becomes a fresh source of remorse. Fifth, fear: of "
  "consequences, of being found out, of the relationship's future - the "
  "mind starts running threat scenarios. Sixth, if the cascade runs its "
  "course honestly, resolve: the reparative drive gathers the scattered "
  "energy and points it forward - apology, restitution, change. The whole "
  "sequence can run in minutes or stretch across weeks, and it can stall "
  "at any stage: stuck at shame becomes hiding, stuck at anger becomes "
  "self-punishment, stuck at fear becomes cover-up. Knowing the cascade "
  "matters because each stage needs something different - and because the "
  "final stage, resolve, is where the chain converts from suffering into "
  "work."),
 "how_it_works": ("The cascade follows from the appraisal unfolding in "
  "layers. Recognition fires first because the deed-memory is the "
  "fastest retrieval. Shame follows because the self is implicated in "
  "the deed - the appraisal naturally widens from act to actor. Sadness "
  "follows because the harm, once attended to, is processed as loss - "
  "and loss is sadness's native trigger. Anger follows because the mind, "
  "confronted with a self-caused loss, generates the thwarted-drive "
  "response: the goal (being a good person, having the intact "
  "relationship) is blocked by one's own past action, and anger is what "
  "blocked goals produce - aimed at the self first, leaking outward "
  "second. Fear follows because the social consequences come into "
  "computation once the emotional storm quiets enough for planning. "
  "Resolve can follow because the reparative drive is remorse's built-in "
  "forward gear - it was there from the first stage, waiting for the "
  "storm to organize around it. Stalls happen when a stage's needs go "
  "unmet: shame without acknowledgment becomes hiding, anger without "
  "direction becomes self-punishment, fear without honesty becomes "
  "cover-up. The cascade is therefore not a malfunction but a process - "
  "and processes can be guided to completion."),
 "key_points": [
  "The cascade order: recognition (remorse) -> shame -> sadness -> anger -> fear -> resolve.",
  "Each stage follows from the appraisal unfolding in layers: deed, then self, then harm, then blocked goals, then consequences.",
  "Anger in the cascade is usually self-aimed first and can leak outward, creating fresh remorse.",
  "Stalls convert the process into suffering: shame->hiding, anger->self-punishment, fear->cover-up.",
  "Resolve is the built-in forward gear: the reparative drive organizing the storm into work."],
 "requirements": [
  "Walk the cascade stage by stage in its recognizable order, with the feeling of each.",
  "Explain the mechanism moving the chain from one stage to the next.",
  "Name the three classic stalls and what each becomes.",
  "End with resolve as the completion stage; keep everything fictional, general, non-clinical."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people."],
 "citations": [CIT_LAZARUS, CIT_TANGNEY],
 "sig_lens": ("The Signature lens reads the cascade as the full audit committee "
  "convening: recognition opens the file, shame reviews the auditor's own "
  "conduct, sadness inventories the damages, anger demands accountability, "
  "fear assesses exposure, and resolve writes the corrective action plan. "
  "Every member has a legitimate seat - the Signature error is letting one "
  "member filibuster. Mastery chairs the meeting: hear each stage fully, "
  "give it its due, and keep the agenda moving toward the final item, which "
  "is always the same - what we do now to make it right.")
},
{
 "key": "remorse_behavior_actions",
 "name": "What People Do When They Feel Remorse",
 "group": "Advanced", "ladder_rank": 22, "ladder_tier": "advanced",
 "description": ("Remorse moves people, and the movements fall into "
  "recognizable patterns. The reparative set - the emotion's native "
  "direction: confessing or acknowledging the deed, apologizing (often "
  "repeatedly, often clumsily), making restitution (paying back, fixing "
  "what can be fixed), and changing the pattern (the drinker pouring out "
  "the bottles, the gossip becoming scrupulously careful with others' "
  "stories). The seeking set: pursuing the harmed person to make contact, "
  "writing the long letter at 2 a.m., showing up with the repair already "
  "in hand. The self-punishing set - where the drive overshoots: "
  "excessive self-denial, refusing comfort or forgiveness, staying in "
  "relationships or situations as penance, working to exhaustion. The "
  "avoidance set - where the drive is blocked: dodging the harmed person, "
  "avoiding the place, changing the subject, staying busy enough that the "
  "loop cannot get a word in. And the symbolic set: the grand gesture "
  "(the donation, the pilgrimage, the dramatic life change), which can be "
  "genuine repair or can be the reparative drive performing for an "
  "audience - the difference shows in whether the harmed person's actual "
  "needs were consulted. Underneath all five sets is one engine: the felt "
  "debt demanding to be paid. Healthy action pays it to the right "
  "creditor, in the currency they actually need; unhealthy action pays it "
  "to the self, in the currency of suffering."),
 "how_it_works": ("The action patterns are the reparative drive finding "
  "channels. Confession and apology discharge the acknowledgment need: "
  "the deed, spoken aloud to a witness, moves from the private loop into "
  "shared reality, which is why the loop often quiets measurably after a "
  "real apology. Restitution discharges the debt need: the harm is "
  "answered in kind, and the ledger entry gets its matching credit. "
  "Pattern change discharges the prevention need: the mind's forward "
  "gear, ensuring the audit produces a new procedure, not just a paid "
  "fine. Self-punishment is the drive with no external creditor available "
  "(the harmed person is gone, or will not receive the repair), so it "
  "turns inward and pays the debt in suffering - which balances nothing, "
  "because suffering was never the currency owed. Avoidance is the drive "
  "colliding with fear of the encounter, so the energy goes into "
  "evasion - which keeps the ledger open, because the creditor was never "
  "approached. The symbolic gesture is the drive seeking a visible "
  "completion; it heals when it serves the harmed, and merely performs "
  "when it serves the performer. The practical test for any remorse-driven "
  "action: does this pay the actual debt to the actual creditor?"),
 "key_points": [
  "The reparative set is the native direction: confession, apology, restitution, pattern change.",
  "The seeking set pursues contact: the 2 a.m. letter, showing up with the repair in hand.",
  "Self-punishment is the drive overshooting: paying the debt to the self in suffering, which balances nothing.",
  "Avoidance is the drive blocked by fear: dodging the person and the place keeps the ledger open.",
  "The test for any action: does it pay the actual debt to the actual creditor, in currency they need?"],
 "requirements": [
  "Describe all five action sets - reparative, seeking, self-punishing, avoidance, symbolic - in plain words.",
  "Explain each through the reparative drive and the felt debt, never clinically.",
  "Give the practical test (actual debt, actual creditor) for sorting healthy from unhealthy action.",
  "All illustrations fictional and general; no real people."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people."],
 "citations": [CIT_BAUMEISTER, CIT_TANGNEY],
 "sig_lens": ("The Signature lens sorts every remorse-driven action through the "
  "audit's payment window: valid payments go to the actual creditor in the "
  "currency of repair - acknowledgment, restitution, changed conduct. "
  "Self-punishment is paying the fine to yourself and calling the case "
  "closed; avoidance is refusing to approach the window at all. The "
  "Signature standard is exacting and simple: the ledger closes when the "
  "creditor is paid, not when the debtor has suffered enough. Mastery "
  "walks to the window, pays in full, changes the procedure that caused "
  "the loss - and then closes the file.")
},
{
 "key": "remorse_speech_patterns",
 "name": "What People Say When They Feel Remorse",
 "group": "Advanced", "ladder_rank": 23, "ladder_tier": "advanced",
 "description": ("Remorse has a voice, and it sounds like someone arguing "
  "with themselves out loud. The characteristic phrases: \"I should "
  "have...\" and \"If only I had...\" - the counterfactuals spoken "
  "aloud, the better version of the scene rehearsed in front of a "
  "witness. \"I am so sorry\" - repeated, sometimes to the point where "
  "the words wear thin, because the feeling outlasts the vocabulary. "
  "\"It was my fault\" and \"I take full responsibility\" - the "
  "acknowledgment phrases, which land as true when they name the "
  "specific deed and as hollow when they stay general. \"Can you ever "
  "forgive me?\" - the debt made audible, the creditor asked to close "
  "the ledger. \"I do not know why I did it\" - the honest confession "
  "of the gap between values and action. The tone underneath: slower "
  "speech, lower pitch, longer pauses - the voice of a person choosing "
  "each word carefully because the words matter now. Disfluency is the "
  "hallmark: false starts, repetitions, sentences abandoned halfway - "
  "the mouth struggling to carry what the courtroom keeps revising. "
  "Written remorse runs longer: the 2 a.m. letter, the text rewritten "
  "six times, the apology that arrives as three paragraphs when one "
  "sentence would do - because writing lets the loop run to completion "
  "without a witness's face interrupting it. And the silences: the "
  "things not said - the deed unnamed, the apology that circles the "
  "subject - which speak as loudly as any phrase about where the fear "
  "still holds the drive in check."),
 "how_it_works": ("The speech patterns are the inner trial made audible. "
  "The counterfactual phrases (\"I should have...\") are the lesson-"
  "generation process leaking into speech: the mind is still computing "
  "the better version, and the mouth narrates the computation. The "
  "repetition of \"I am so sorry\" is the debt outlasting the vocabulary: "
  "the feeling regenerates faster than language can discharge it, so the "
  "speaker loops the available phrase. The specificity effect - named "
  "deeds landing true, generalities landing hollow - follows from the "
  "circuit: the reckoning is about a specific deed measured against a "
  "specific standard, so language that matches that specificity "
  "resonates and language that evades it rings false. The slowed, "
  "lowered, disfluent delivery is cognitive load made audible: the "
  "speaker is simultaneously managing the replay, the self-judgment, "
  "the witness's face, and the sentence construction - four tasks on a "
  "system built for one. Written remorse runs long because writing "
  "removes the witness's face from the load, freeing capacity for the "
  "loop to complete. The silences mark where fear still outranks the "
  "reparative drive: the unnamed deed is the ledger entry the speaker "
  "is not yet ready to file publicly."),
 "key_points": [
  "\"I should have...\" and \"If only...\" are the counterfactual lesson-generator leaking into speech.",
  "Repeated \"I am so sorry\" is the debt outlasting the vocabulary - the feeling regenerates faster than words discharge it.",
  "Specificity is the truth test: named deeds land true, careful generalities ring hollow.",
  "Slowed, lowered, disfluent speech is cognitive load made audible - four tasks on a one-task system.",
  "The silences speak too: the unnamed deed marks where fear still outranks the drive to repair."],
 "requirements": [
  "Quote the characteristic phrases and explain what each one reveals, in plain words.",
  "Cover tone, pace, disfluency, written remorse, and the significant silences.",
  "Explain the specificity effect (named vs general) clearly.",
  "All examples fictional and general; no real people's words."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people."],
 "citations": [CIT_TANGNEY, CIT_EKMAN],
 "sig_lens": ("The Signature lens hears remorseful speech as the audit report "
  "being dictated live: the false starts are the auditor checking the "
  "figures mid-sentence, the repetitions are the findings too large for "
  "one telling, the silences are the pages not yet ready for release. "
  "The Signature counsel on apology: dictate the specific findings. Name "
  "the deed, name the standard, name the repair - the three sentences that "
  "close more ledgers than a thousand \"I am so sorry\"s. Mastery speaks "
  "the audit plainly, once, completely - and then lets the changed conduct "
  "do the repeating.")
},
{
 "key": "remorse_decisions_judgment",
 "name": "How Remorse Changes Decisions and Judgment",
 "group": "Advanced", "ladder_rank": 24, "ladder_tier": "advanced",
 "description": ("Remorse is not just a feeling about the past; it is a "
  "thumb on the scale of every decision made while it runs. Risk judgment "
  "shifts: the person becomes more cautious, sometimes wisely (the driver "
  "who caused the accident now drives like a chauffeur) and sometimes "
  "excessively (refusing any decision that resembles the original, even "
  "when the resemblance is superficial). Moral judgment sharpens and "
  "distorts at once: sharper, because the violated standard is now vivid "
  "and the person spots similar wrongs everywhere; distorted, because the "
  "inner judge, mid-trial, tends to over-convict - seeing wrongdoing in "
  "ambiguous situations and judging others harshly for the very fault "
  "being tried within. Generosity spikes: the reparative drive "
  "generalizes, and people in remorse give more, help more, volunteer "
  "more - the debt seeking any creditor, even unrelated ones. Self-trust "
  "drops: \"I was wrong about that, so I may be wrong about this\" - "
  "which produces healthy humility in measure and paralyzing "
  "second-guessing in excess. Time horizon stretches: the remorseful mind "
  "weighs long-term consequences more heavily, having just paid the price "
  "of short-term thinking. The net effect is a decision-maker who is "
  "kinder, more careful, and more future-minded - but also more anxious, "
  "more self-doubting, and more prone to see the world through the lens "
  "of the trial. Remorse improves judgment the way a hard lesson improves "
  "a student: genuinely, and at a cost."),
 "how_it_works": ("Each distortion traces to the circuit's demands. "
  "Caution rises because the appraisal system has fresh evidence that "
  "this person's choices can cause real harm - the risk model updates, "
  "sometimes over-updates. Moral sharpening happens because the violated "
  "standard is hyper-accessible in memory: what is vivid is seen "
  "everywhere, including in others (the over-conviction is projection "
  "of the inner trial outward). Generalized generosity is the reparative "
  "drive with its specific creditor unavailable or already paid: the "
  "energy, still generated, seeks any outlet - a well-documented "
  "redirect of moral emotion into prosocial behavior. Self-trust drops "
  "because the self-model has new counter-evidence: the person who "
  "chose wrong once must discount their own judgment until the new "
  "pattern proves itself. The stretched time horizon is the "
  "counterfactual machinery applied forward: a mind practiced at "
  "\"what if I had...\" naturally becomes practiced at \"what if I "
  "do...\" The improvements are real - remorse is one of the mind's "
  "legitimate teachers - and the costs are real too, which is why the "
  "goal is integration (the lesson kept, the trial adjourned) rather "
  "than permanent residence in the courtroom."),
 "key_points": [
  "Risk judgment shifts cautious: wisely (genuine care) or excessively (avoiding superficial resemblances).",
  "Moral judgment sharpens and distorts: the vivid standard is spotted everywhere, including over-conviction of others.",
  "Generosity spikes: the reparative drive generalizes, seeking any creditor when the specific one is unavailable.",
  "Self-trust drops: healthy humility in measure, paralyzing second-guessing in excess.",
  "Time horizon stretches: practiced counterfactuals turn forward into better consequence-weighing."],
 "requirements": [
  "Cover risk, moral judgment, generosity, self-trust, and time horizon - each with the wise and excessive versions.",
  "Explain each shift through the circuit's mechanics, never clinically.",
  "End with integration as the goal: lesson kept, trial adjourned.",
  "All illustrations fictional and general; no real people."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people."],
 "citations": [CIT_BAUMEISTER, CIT_LAZARUS],
 "sig_lens": ("The Signature lens reads the shifted judgment as the audit's "
  "new procedures being drafted in real time: the caution is the revised "
  "risk policy, the sharpened moral eye is the updated inspection checklist, "
  "the generosity is the restitution fund opened to all comers, the stretched "
  "horizon is the new long-range planning requirement. The Signature caution "
  "is against over-correction: a procedure written in the heat of the audit "
  "should be reviewed in the cool of the quarter. Mastery keeps the genuine "
  "improvements - the care, the humility, the foresight - and retires the "
  "excesses, filing the lesson as policy rather than living it as punishment.")
}
,
{
 "key": "remorse_escalation",
 "name": "Remorse Under Pressure: How Behavior Escalates",
 "group": "Advanced", "ladder_rank": 25, "ladder_tier": "advanced",
 "description": ("As remorse intensifies, behavior escalates along "
  "predictable tracks - and knowing the tracks helps people recognize "
  "where they are before the escalation runs away. Track one, the "
  "confession spiral: the urge to acknowledge grows until the person is "
  "confessing to everyone - the harmed person, mutual friends, "
  "strangers, the internet - seeking a witness who can declare the debt "
  "paid, and each confession that fails to quiet the loop raises the "
  "stakes for the next. Track two, the restitution race: repair efforts "
  "accelerate beyond what the harm requires - the over-apology, the "
  "extravagant gift, the life reorganized around penance - until the "
  "repair itself becomes a burden on the very people it was meant to "
  "serve. Track three, the self-punishment climb: denied comforts, "
  "refused forgiveness, exhausted overwork - the debt paid in suffering "
  "because suffering is the only currency the person will accept from "
  "themselves. Track four, the avoidance fortress: dodging the harmed "
  "person, the place, the topic, until daily life is reorganized around "
  "not-facing-it - which keeps the loop permanently fueled, because the "
  "unfaced debt never gets its hearing. Track five, the numbness exit: "
  "when the loop's pain exceeds what the person can carry, the system "
  "can shut the feeling down entirely - flatness, detachment, the "
  "courtroom emptied by force - which looks like peace and functions "
  "like a paused trial. Every track is the same drive - the debt "
  "demanding payment - with the payment routed wrong. The de-escalation "
  "is the same in every case: route the payment correctly - specific "
  "acknowledgment to the actual person harmed, restitution sized to the "
  "actual harm, pattern changed going forward - and the escalation "
  "loses its fuel."),
 "how_it_works": ("Escalation happens when the reparative drive cannot "
  "discharge through its proper channel, so pressure builds and finds "
  "side channels. The confession spiral is the acknowledgment need "
  "unmet: no single witness's absolution quiets an internal verdict, so "
  "the person seeks more witnesses, louder ones - but the verdict is "
  "internal, and external absolution cannot overrule it. The restitution "
  "race is the debt need with no agreed amount: without the creditor's "
  "actual accounting, the debtor keeps raising the payment, hoping "
  "quantity will substitute for the missing settlement. The "
  "self-punishment climb is the debt need turned inward when the "
  "creditor is unreachable: suffering becomes the currency because it is "
  "the only payment the debtor can make unilaterally. The avoidance "
  "fortress is the drive colliding with fear: every evasion postpones "
  "the hearing, and the postponed hearing grows in imagined terror, "
  "which increases the evasion - a feedback loop. The numbness exit is "
  "the system's circuit breaker: sustained unresolvable arousal trips "
  "the shutdown, trading pain for flatness. All five de-escalate through "
  "the same mechanism: give the drive its proper channel - the actual "
  "creditor, the actual harm, the actual change - and the side channels "
  "drain."),
 "key_points": [
  "The confession spiral: seeking ever-louder witnesses because no external absolution overrules an internal verdict.",
  "The restitution race: raising the payment endlessly when the creditor's actual accounting is missing.",
  "The self-punishment climb: paying the debt in suffering when the creditor is unreachable.",
  "The avoidance fortress: evasion postponing the hearing, the postponed hearing growing in imagined terror - a feedback loop.",
  "The numbness exit: the circuit breaker tripping - flatness that looks like peace and functions like a paused trial."],
 "requirements": [
  "Describe all five escalation tracks with the wrong-routed payment in each.",
  "Explain each track's mechanism in plain words, never clinically.",
  "Give the single de-escalation: route the payment correctly to the actual creditor.",
  "All illustrations fictional and general; no real people."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people."],
 "citations": [CIT_BAUMEISTER, CIT_GROSS],
 "sig_lens": ("The Signature lens reads escalation as the audit's pressure "
  "seeking any release valve: the spiral, the race, the climb, the "
  "fortress, the shutdown are all the same steam escaping sideways. The "
  "Signature correction is plumbing, not willpower: close the side valves "
  "by opening the main one. Walk to the actual creditor, state the actual "
  "findings, pay the actual amount, change the actual procedure. Pressure "
  "properly channeled does the work it was built for - and the forge, "
  "fed correctly, tempers instead of exploding.")
},
{
 "key": "remorse_healthy_expression",
 "name": "Healthy Expression of Remorse",
 "group": "Advanced", "ladder_rank": 26, "ladder_tier": "advanced",
 "description": ("Healthy remorse is the emotion completing its circuit: "
  "felt honestly, spoken plainly, paid specifically, and then released "
  "into changed conduct. It has four movements. First, honest feeling: "
  "allowing the ache without either drowning in it or numbing it - "
  "naming it inwardly (\"this is remorse; I did wrong\") rather than "
  "disguising it as irritation or fatigue. Second, plain speech: telling "
  "the truth about the deed to the person harmed - specifically, without "
  "euphemism and without the self-protective editing that turns "
  "confession into public relations. The healthy apology names the deed, "
  "names the harm as the other person experienced it, takes "
  "responsibility without the word \"but,\" and asks what repair would "
  "matter - then listens to the answer. Third, specific payment: "
  "restitution sized to the actual harm, made in the currency the "
  "harmed person actually needs - which is sometimes money or labor, "
  "sometimes simply the steady demonstration over time that the pattern "
  "has changed. Fourth, release into conduct: the ledger entry closed "
  "not by forgetting but by the lived proof of the lesson - the person "
  "who was careless with trust becoming reliably trustworthy, not as "
  "performance but as procedure. Healthy remorse ends. That is its "
  "signature: the courtroom adjourns, the file is marked answered, and "
  "the energy that ran the loop is freed for the future. It does not "
  "mean the memory vanishes - it means the memory arrives with its "
  "resolution attached."),
 "how_it_works": ("Each movement discharges one of the circuit's demands. "
  "Honest feeling lets the appraisal complete: the verdict, faced "
  "directly, stops generating the evasive side-loops (irritation, "
  "numbness, busyness) that keep the case open. Plain speech moves the "
  "deed from the private loop into shared reality: a witnessed "
  "acknowledgment is processed by the mind as an event with a timestamp, "
  "which the loop can file, where unwitnessed replay is timeless and "
  "unfillable. Specific payment answers the debt need in the correct "
  "currency: the mind's accounting closes when the creditor's actual "
  "needs are met, not when the debtor has performed enough suffering. "
  "Release into conduct answers the prevention need: the forward gear of "
  "the emotion - \"never again\" - is satisfied by the demonstrated "
  "pattern, and the loop loses its reason to keep rehearsing the "
  "warning. The four movements are sequential because each unlocks the "
  "next: unfelt remorse cannot be spoken, unspoken remorse cannot be "
  "paid, unpaid remorse cannot be released. Skipped steps are why "
  "apologies fail: the words without the feeling ring hollow, the "
  "payment without the acknowledgment feels like a bribe, the change "
  "without the speech leaves the witness unconvinced."),
 "key_points": [
  "Movement one - honest feeling: name it inwardly instead of disguising it as irritation or fatigue.",
  "Movement two - plain speech: name the deed specifically, take responsibility without 'but,' ask what repair would matter.",
  "Movement three - specific payment: restitution sized to the actual harm, in currency the harmed person needs.",
  "Movement four - release into conduct: the lesson lived as procedure until the pattern proves itself.",
  "Healthy remorse ends: the courtroom adjourns, the file marked answered, the energy freed for the future."],
 "requirements": [
  "Present the four movements in order, each with its plain-language practice.",
  "Explain what each movement discharges in the circuit, in plain words.",
  "Show why skipped steps make apologies fail.",
  "Keep guidance general and everyday; no therapeutic promises, no real people."],
 "standards": ["Descriptive and educational only - no diagnosis, no therapeutic promises, no labels on real people."],
 "citations": [CIT_TANGNEY, CIT_BAUMEISTER],
 "sig_lens": ("The Signature lens formalizes healthy remorse as the audit's "
  "proper closeout procedure: findings faced, report filed with the "
  "affected party, restitution paid per the actual damages, corrective "
  "action implemented and verified over time. This is not softness - it "
  "is the hardest procedure in the book, because it requires facing the "
  "evidence without flinching and paying without haggling. The Signature "
  "mark of mastery: a closed file. The auditor who completes all four "
  "movements earns the quietest instrument reading there is - a conscience "
  "at rest, and a future built on the tempered steel of the lesson.")
},
{
 "key": "remorse_unhealthy_expression",
 "name": "Unhealthy Expression: Bottling Up or Boiling Over",
 "group": "Advanced", "ladder_rank": 27, "ladder_tier": "advanced",
 "description": ("Remorse goes wrong in two opposite directions, and both "
  "keep the ledger open. Bottling up: the person feels the verdict but "
  "refuses the proceedings - no acknowledgment, no apology, no repair. "
  "The loop, denied its outlet, goes underground: the replay continues "
  "in private, the body carries the tension, and the unexpressed drive "
  "leaks sideways - irritability with no clear cause, numb busyness, the "
  "3 a.m. sessions that never get their day in court. Bottled remorse "
  "often ferments into its neighbors: hidden guilt becomes chronic "
  "self-reproach, unacknowledged debt becomes avoidance of everyone "
  "connected to it, and the pressure can surface years later at a "
  "surprise trigger with the full original charge. Boiling over: the "
  "opposite failure - the feeling floods the controls and the reparative "
  "drive discharges everywhere at once. The confession spiral (telling "
  "everyone), the restitution race (paying far beyond the harm), the "
  "self-punishment climb (suffering as currency), the dramatic gestures "
  "that serve the performer's relief more than the harmed person's "
  "needs. Boiled-over remorse exhausts everyone in the blast radius and "
  "still leaves the actual debt unpaid, because the energy went into "
  "discharge rather than repair. The two failures look opposite but share "
  "one root: the proper channel - specific acknowledgment to the actual "
  "person, restitution sized to the actual harm - was never used. "
  "Bottling starves it; boiling floods past it. Health is the middle "
  "path: feel it fully, speak it plainly, pay it precisely."),
 "how_it_works": ("Bottling fails because the circuit's demands do not "
  "decay with ignoring: the appraisal (deed vs standard) remains true, "
  "the debt remains felt, and the reparative drive keeps generating "
  "energy with nowhere to go - so it pressurizes the system, leaks into "
  "unrelated channels, and preserves the memory at full charge for "
  "future ambush. The fermentation into neighboring states follows from "
  "the unmet needs: unacknowledged wrongdoing keeps the shame channel "
  "open, unpaid debt keeps the avoidance channel open, unexpressed "
  "arousal keeps the body braced. Boiling over fails for the mirror "
  "reason: the drive discharges, but discharge is not payment. "
  "Confessing to everyone discharges the acknowledgment need without "
  "ever giving the actual creditor their hearing; extravagant "
  "restitution discharges the debt need without ever learning the "
  "creditor's actual accounting; self-punishment discharges the energy "
  "into suffering, which no ledger accepts as currency. Both failures "
  "leave the loop running - the bottled version as pressure, the boiled "
  "version as noise - because the loop only closes on its proper "
  "completion: the specific deed, acknowledged to the actual witness, "
  "paid in the actual currency, changed in actual conduct."),
 "key_points": [
  "Bottling up: no acknowledgment, no repair - the loop goes underground, pressurizes, and leaks sideways.",
  "Bottled remorse ferments: into chronic self-reproach, avoidance, and surprise-trigger ambushes years later.",
  "Boiling over: the drive discharges everywhere - confession spirals, restitution races, self-punishment climbs.",
  "Boiled-over remorse exhausts everyone nearby and still leaves the actual debt unpaid: discharge is not payment.",
  "Both share one root: the proper channel - specific acknowledgment, sized restitution - was never used."],
 "requirements": [
  "Describe bottling and boiling as the two opposite failures, each with its downstream effects.",
  "Explain the shared root (proper channel unused) in plain words.",
  "Keep the tone descriptive, never shaming the reader for either pattern.",
  "No clinical language, no real people, no therapeutic promises."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people."],
 "citations": [CIT_GROSS, CIT_TANGNEY],
 "sig_lens": ("The Signature lens marks both failures as audit malpractice: "
  "bottling is the findings buried in a drawer - the evidence intact, the "
  "report never filed, the corruption spreading quietly through every "
  "connected system. Boiling over is the report screamed through a "
  "bullhorn at the whole town instead of filed with the affected party - "
  "maximum noise, zero settlement. The Signature standard admits neither: "
  "the findings are faced, the report goes to the actual affected party, "
  "the payment matches the actual damages. Anything else is theater - "
  "silent or loud - and the ledger does not accept theater as payment.")
},
{
 "key": "remorse_everyday_practices",
 "name": "Everyday Practices That Keep Remorse in Balance",
 "group": "Advanced", "ladder_rank": 28, "ladder_tier": "advanced",
 "description": ("Remorse does not have to run your life to do its job; "
  "small, ordinary practices keep it in its proper place - advisor, not "
  "ruler. The evening review: five quiet minutes before sleep, asking "
  "three questions - what did I do today that I am proud of, what do I "
  "wish I had done differently, and is there anything I owe anyone? - "
  "which gives the appraisal circuit its daily hearing so it does not "
  "demand the 3 a.m. session. The prompt apology: when the pang fires, "
  "acting within the day - the quick, specific \"I was wrong to say "
  "that; I am sorry\" - which closes small ledger entries before they "
  "accrue interest. The repair list: writing down open debts (the call "
  "owed, the thanks unsaid, the fix promised) and working them like any "
  "other list - because remorse kept as tasks gets completed, while "
  "remorse kept as mood gets ruminated. The standard check: periodically "
  "asking whether the inner judge is being fair - would I condemn a "
  "friend for this? - which keeps a harsh conscience from over-convicting. "
  "The conduct proof: deliberately practicing the opposite pattern - the "
  "person remorseful about carelessness becoming meticulously careful - "
  "which gives the forward gear its work and quiets the loop with "
  "evidence. And the release ritual: when a debt is truly paid and the "
  "pattern truly changed, a deliberate marking of the close - a walk, a "
  "journal entry, a spoken \"that is answered\" - giving the mind the "
  "timestamp it needs to file the entry. None of these are treatments "
  "for anything; they are housekeeping for a healthy conscience - the "
  "daily maintenance that keeps the instrument calibrated and the ledger "
  "current."),
 "how_it_works": ("Each practice works on one part of the circuit. The "
  "evening review gives the appraisal system its scheduled hearing: a "
  "mind that knows it will get its daily five minutes stops ambushing "
  "its owner at 3 a.m. - the loop quiets because its demand for "
  "attention is met on schedule. The prompt apology closes entries "
  "while they are small: fresh deeds have low stickiness and willing "
  "creditors, so same-day repair costs little and prevents the "
  "interest-accrual of delay. The repair list externalizes the debt: "
  "written tasks engage the planning system instead of the rumination "
  "system, converting mood into agenda. The standard check recalibrates "
  "the judge: harsh inner standards over-convict, and the friend-test "
  "imports the fairer calibration we naturally apply to others. The "
  "conduct proof feeds the prevention need with evidence: the loop "
  "rehearses warnings until the new pattern demonstrates the warning "
  "is handled. The release ritual supplies the timestamp: the mind "
  "files completed events by their closing markers, and a deliberate "
  "marker tells the filing system the case is closed. Together they "
  "are preventive maintenance - keeping the audit current so it never "
  "needs to become a siege."),
 "key_points": [
  "The evening review: five minutes, three questions - gives the appraisal its scheduled hearing, preventing 3 a.m. ambushes.",
  "The prompt apology: same-day, specific repair closes small entries before they accrue interest.",
  "The repair list: written debts become tasks (planning system) instead of moods (rumination system).",
  "The standard check: 'would I condemn a friend for this?' recalibrates a harsh inner judge.",
  "The conduct proof and release ritual: live the changed pattern, then deliberately mark the file closed."],
 "requirements": [
  "Present at least six concrete everyday practices in plain, doable words.",
  "Explain what part of the circuit each practice serves.",
  "Frame everything as housekeeping for a healthy conscience, never as treatment.",
  "No therapeutic promises, no clinical language, no real people."],
 "standards": ["Descriptive and educational only - general everyday guidance, no therapeutic promises."],
 "citations": [CIT_GROSS, CIT_BAUMEISTER],
 "sig_lens": ("The Signature lens treats these practices as the auditor's daily "
  "discipline: the evening review is the day's books balanced before close, "
  "the prompt apology is same-day settlement, the repair list is the open-items "
  "ledger, the standard check is calibration of the instruments, the conduct "
  "proof is the corrective action verified in the field, the release ritual is "
  "the file stamped closed. Auditors who keep daily books never face the "
  "decade-end reckoning. The Signature standard: a conscience maintained daily "
  "is an instrument you can trust - and a ledger kept current is a mind at "
  "peace.")
},
{
 "key": "remorse_reading_others",
 "name": "Reading Remorse in Other People",
 "group": "Advanced", "ladder_rank": 29, "ladder_tier": "advanced",
 "description": ("Recognizing remorse in others is a practical skill - it "
  "tells you when an apology is real, when someone needs space, and when "
  "the door is open for repair. Read the face first: the sustained "
  "downward gaze, the inner-brow lift held rather than flashed, the "
  "pressed lips and the swallow before the hard sentence - remorse's face "
  "is downward and inward, and it arrives before the words. Read the body: "
  "the shrunken posture, the slowed movement, the hands that fidget or "
  "clasp - the body making itself smaller while the mind runs the trial. "
  "Read the speech: the disfluency (false starts, repetitions), the "
  "specific naming of the deed (generalities suggest performance; "
  "specifics suggest the real circuit), the repeated return to the "
  "subject - the loop audible in conversation. Read the behavior: the "
  "approach (showing up, the letter, the repair already in hand) versus "
  "the avoidance (dodging, subject-changing, busyness as armor) - both "
  "are remorse-shaped, and they tell you where the person is in the "
  "process. Read the timing: remorse that appears promptly after the "
  "deed, unprompted, is the circuit firing cleanly; remorse that appears "
  "only after exposure may still be real - the exposure forced the "
  "hearing - but watch whether the focus stays on the deed or slides to "
  "damage control. And read your own certainty with humility: the signs "
  "are tendencies, not instruments. The quiet person may be running the "
  "heaviest loop in the room, and the tearful one may be performing. "
  "Use what you read to respond wisely - never to convict."),
 "how_it_works": ("Reading works because remorse's display is an "
  "appeasement signal designed to be read: the face, body, speech, and "
  "behavior patterns are the circuit's outputs, and they correlate with "
  "the internal state because they are produced by it. The face-before-"
  "words timing is the most reliable single indicator, since the "
  "involuntary display precedes deliberate speech. Specificity in "
  "language tracks the circuit's own specificity: the reckoning is about "
  "a particular deed, so real remorse names it, while performed remorse "
  "stays general to avoid the cost of the truth. Approach-versus-"
  "avoidance reveals the reparative drive's state: approaching means the "
  "drive has a channel, avoiding means fear currently outranks it - both "
  "confirm the emotion is present, at different stages. The humility "
  "caution follows from base rates and individual variation: expressive "
  "temperaments amplify the display, reserved ones dampen it, and no "
  "checklist overrides that variation. The skill's purpose is response, "
  "not judgment: reading remorse well tells you whether to open the "
  "door (approach), wait (avoidance), or simply witness (peak) - and "
  "that is the whole of its legitimate use."),
 "key_points": [
  "Face first: sustained downward gaze, held inner-brow lift, pressed lips, the swallow before the hard sentence.",
  "Body: shrunken posture, slowed movement, fidgeting or clasped hands - the body smaller while the mind is at trial.",
  "Speech: disfluency, specific naming of the deed (specifics = real circuit; generalities = performance), looping back to the subject.",
  "Behavior: approach (showing up, letter, repair in hand) vs avoidance (dodging, armor-busyness) - both remorse-shaped, different stages.",
  "Humility: tendencies, not instruments - read to respond wisely, never to convict."],
 "requirements": [
  "Cover face, body, speech, behavior, and timing as five reading channels.",
  "Include the specificity test and the face-before-words timing as key indicators.",
  "State the humility caution explicitly: variation, no checklists-as-proof.",
  "Frame the skill's purpose as response, never judgment; no real people."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people."],
 "citations": [CIT_EKMAN, CIT_TANGNEY],
 "sig_lens": ("The Signature lens trains the reader as a fellow auditor, not a "
  "prosecutor: you are reading another person's books only to know how to "
  "meet them - door open, waiting, or witnessing. The Signature discipline "
  "is the humility clause made operational: never audit someone who has not "
  "hired you. Read the face, honor what it reports, respond to the stage "
  "they are in - and keep your own verdicts in your own ledger. Mastery of "
  "reading remorse is measured not by how accurately you catch people, but "
  "by how wisely you receive them.")
},
{
 "key": "remorse_supportive_responses",
 "name": "How to Respond When Someone Feels Remorse",
 "group": "Advanced", "ladder_rank": 30, "ladder_tier": "advanced",
 "description": ("When someone comes to you carrying remorse - the "
  "stumbling apology, the 2 a.m. letter, the confession they have been "
  "rehearsing for weeks - your response can help the circuit complete or "
  "jam it further. What helps: listen first, fully, without rushing to "
  "the absolution. Let the specific deed be named and heard; the "
  "acknowledgment needs its witness, and cutting it short with \"it is "
  "fine, forget it\" can feel like the hearing was adjourned without "
  "being held. Acknowledge the harm as they describe it: \"I hear how "
  "much this weighs on you, and I understand why\" - which validates the "
  "appraisal without either inflating or dismissing it. Be honest about "
  "the impact: false reassurance (\"it was nothing\") insults the "
  "person's judgment, while honest accounting (\"it did hurt, and here "
  "is what would help\") gives the reparative drive its true target. "
  "Name what repair would actually matter to you, if you are the harmed "
  "party - the circuit needs the creditor's real accounting, not guesses. "
  "If you are a bystander, point toward the proper channel: \"have you "
  "told them directly?\" rather than offering yourself as a substitute "
  "witness. And allow the timeline: genuine repair takes the time it "
  "takes, and hovering for instant reassurance (\"are we good now?\") "
  "can restart the loop. What you are doing, in all of this, is serving "
  "as the fair witness the inner courtroom needs - neither the hanging "
  "judge nor the defense attorney, but the honest magistrate who hears "
  "the case fully and states the true terms of settlement."),
 "how_it_works": ("Each helpful response serves one of the circuit's "
  "needs. Full listening serves the acknowledgment need: the deed, "
  "witnessed completely, becomes a fileable event instead of a timeless "
  "loop. Validating the appraisal (\"I understand why this weighs on "
  "you\") confirms the verdict the inner judge already delivered, which "
  "paradoxically quiets the judge - it no longer has to shout to be "
  "heard. Honest impact accounting serves the debt need with true "
  "figures: the reparative drive can only pay the correct amount when "
  "it knows the correct amount, and false reassurance leaves it "
  "guessing. Naming the real repair gives the drive its proper channel "
  "instead of the side channels (spirals, races, self-punishment). "
  "Bystander redirection (\"tell them directly\") prevents the "
  "substitute-witness trap, where confession to a third party "
  "discharges the urge without ever reaching the creditor. Allowing the "
  "timeline respects that pattern-change - the final movement - is "
  "demonstrated over weeks and months, not declared in an afternoon. "
  "The unhelpful responses all fail the same test: they serve the "
  "responder's comfort (reassure quickly, end the awkwardness) rather "
  "than the circuit's completion - and the circuit, uncompleted, simply "
  "reschedules."),
 "key_points": [
  "Listen fully first: the acknowledgment needs its witness; rushed absolution adjourns the hearing unheld.",
  "Validate the appraisal honestly: 'I understand why this weighs on you' - neither inflating nor dismissing.",
  "Give true accounting, not false reassurance: the drive needs the real figures to pay the real amount.",
  "Name the repair that would actually matter - the circuit needs the creditor's real terms.",
  "Bystanders redirect to the proper channel ('tell them directly'); everyone allows the genuine timeline."],
 "requirements": [
  "Give concrete helpful responses for the listener, the harmed party, and the bystander.",
  "Explain what circuit need each response serves, in plain words.",
  "Contrast with the comfort-serving responses that jam the circuit.",
  "Keep guidance general and everyday; no therapeutic promises, no real people."],
 "standards": ["Descriptive and educational only - general everyday guidance, no therapeutic promises."],
 "citations": [CIT_BAUMEISTER, CIT_TANGNEY],
 "sig_lens": ("The Signature lens casts the supporter as the fair magistrate: "
  "not the hanging judge who maximizes the sentence, not the defense "
  "attorney who argues the deed away, but the honest officer of the court "
  "who hears the case fully and states the true terms of settlement. The "
  "Signature standard for the witness: hear completely, account honestly, "
  "name the real repair, and then - this is the hard part - step back and "
  "let the debtor pay it. Mastery in support is restraint in service of "
  "completion: you cannot serve another person's sentence, and attempting "
  "to only restarts their trial.")
}
,
{
 "key": "remorse_mistakes_to_avoid",
 "name": "Mistakes to Avoid Around Someone Feeling Remorse",
 "group": "Advanced", "ladder_rank": 31, "ladder_tier": "advanced",
 "description": ("Good intentions misfire around remorse with remarkable "
  "reliability; here are the classic mistakes. The instant absolution: "
  "\"It is fine, do not worry about it\" - delivered before the deed "
  "has been fully named. It feels kind, but it adjourns the hearing "
  "without holding it: the acknowledgment never got its witness, and "
  "the loop reschedules. The ledger weapon: storing the person's "
  "confession and withdrawing it later as ammunition (\"well, YOU "
  "admitted that you...\") - which teaches everyone watching that "
  "honesty gets punished, and guarantees the next remorse goes "
  "underground. The suffering audit: deciding their remorse is "
  "insufficient and demanding more visible pain - which confuses the "
  "currency (suffering was never owed; repair was) and turns the "
  "reparative drive into performance. The comparison verdict: \"other "
  "people have done worse\" - meant to comfort, but it argues with the "
  "person's own standard, which only they can calibrate. The fix-it "
  "takeover: seizing the repair process (calling the harmed party "
  "yourself, dictating the apology) - which robs the debtor of the "
  "payment that would have closed their ledger. The endless probation: "
  "accepting the apology and then re-trying the case for months - "
  "which tells the circuit its completion will never be honored, so it "
  "never completes. And the mirror trial: responding to their remorse "
  "with your own unrelated grievances - which changes the subject from "
  "their debt to your docket. Every one of these serves the responder, "
  "not the circuit. The alternative is simpler than it feels: hear the "
  "case fully, state the true terms, and then honor the completion when "
  "it comes."),
 "how_it_works": ("Each mistake jams one of the circuit's movements. "
  "Instant absolution blocks acknowledgment: the witnessed hearing is "
  "the mechanism that converts timeless replay into fileable event, "
  "and skipping it leaves the loop running. The ledger weapon "
  "punishes the acknowledgment channel itself: the mind learns that "
  "confession is dangerous, so future remorse takes the avoidance or "
  "bottling tracks - the circuit's proper channel gets boarded up. The "
  "suffering audit misstates the debt: the circuit demands repair, not "
  "pain, so demanded suffering discharges nothing and teaches the "
  "performer to emote rather than mend. The comparison verdict argues "
  "with the appraisal instead of witnessing it: the standard is the "
  "person's own, and external re-calibration attempts read as "
  "dismissal. The fix-it takeover steals the payment: the ledger "
  "closes on the debtor's action, and action performed by proxy does "
  "not register. Endless probation dishonors completion: a circuit "
  "that completes and is re-opened learns that completion is futile. "
  "The mirror trial abandons the case for a different one: the "
  "original debt never gets its hearing. The pattern across all seven: "
  "the responder's needs (comfort, control, leverage, speed) override "
  "the circuit's needs (witness, truth, proper payment, honored "
  "completion) - and the circuit always collects what it is owed, "
  "eventually, with interest."),
 "key_points": [
  "Instant absolution adjourns the hearing unheld: the acknowledgment never got its witness.",
  "Weaponizing a confession teaches everyone watching that honesty gets punished.",
  "Demanding visible suffering confuses the currency: repair was owed, never pain.",
  "'Others did worse' argues with the person's own standard - which only they can calibrate.",
  "Takeover, endless probation, and the mirror trial all dishonor the circuit's proper completion."],
 "requirements": [
  "Name and explain at least six classic mistakes with the circuit-harm each one causes.",
  "Keep the tone instructive, never scolding; the reader may recognize themselves.",
  "Show the shared pattern: responder's needs overriding the circuit's needs.",
  "End with the simple alternative; no real people, no clinical language."],
 "standards": ["Descriptive and educational only - general everyday guidance, no therapeutic promises."],
 "citations": [CIT_TANGNEY, CIT_GROSS],
 "sig_lens": ("The Signature lens posts these mistakes on the courtroom wall as "
  "the magistrate's code of conduct: hear the case before ruling, never "
  "weaponize testimony, sentence in repair not suffering, respect the "
  "defendant's own statutes, let the debtor pay their own fine, honor a "
  "served sentence, and keep your own docket off their trial. The "
  "Signature magistrate is neither lenient nor severe - the magistrate is "
  "exact. Exactness is the kindness: true terms, truly stated, truly "
  "honored. Everything else is the court serving itself instead of "
  "justice.")
},
{
 "key": "remorse_related_emotions",
 "name": "The Remorse Neighborhood: Guilt, Regret, Shame, Contrition",
 "group": "Advanced", "ladder_rank": 32, "ladder_tier": "advanced",
 "description": ("Remorse lives in a crowded neighborhood, and telling the "
  "neighbors apart is one of the most useful emotional skills there is. "
  "Guilt is the nearest neighbor: the broad, everyday sense of having "
  "done wrong. Tell them apart by depth and duration - guilt is the "
  "alarm, remorse is the full investigation; guilt says \"that was "
  "wrong,\" remorse says \"that was wrong, and here is the whole case "
  "file, and I am answerable.\" Regret is the backward-looking neighbor: "
  "it wishes the outcome had differed, and it can fire with no "
  "wrongdoing at all (regretting a lost opportunity, a rainy picnic). "
  "Tell them apart by the moral charge: regret without wrongdoing is "
  "just wishing; remorse always carries the verdict. Shame is the "
  "cousin across the street: it judges the self where remorse judges "
  "the deed. Tell them apart by the sentence: shame says \"I am bad\" "
  "and wants to hide; remorse says \"I did bad\" and wants to repair - "
  "which is why shame predicts withdrawal and remorse predicts apology. "
  "Contrition is remorse's purposeful sibling: remorse turned explicitly "
  "toward making amends, the feeling plus the vow. Tell them apart by "
  "direction: contrition faces forward (what I will do), remorse faces "
  "backward (what I did) - healthy remorse matures into contrition the "
  "way an investigation matures into a verdict and sentence. The "
  "opposites on the far side: self-justification (the verdict "
  "overturned on appeal to oneself), defiance (the court rejected), and "
  "indifference (no court convened). Knowing the neighborhood matters "
  "because each neighbor needs different handling: guilt needs "
  "acknowledgment, regret needs acceptance of the unchangeable, shame "
  "needs the focus moved from self to deed, and remorse needs its proper "
  "payment - the specific repair that closes the specific ledger."),
 "how_it_works": ("The neighbors separate along three axes. Axis one, "
  "the object of judgment: remorse, guilt, and contrition judge the "
  "deed; shame judges the self; regret judges the outcome. This single "
  "axis predicts the action tendency: deed-judgment drives repair, "
  "self-judgment drives hiding, outcome-judgment drives wishing. Axis "
  "two, moral charge: remorse and guilt require a violated standard; "
  "regret does not - which is why regret is the only neighbor that can "
  "fire over a rained-out picnic. Axis three, depth and duration: guilt "
  "is the broad, brief alarm; remorse is the deep, sustained "
  "investigation; contrition is remorse with its forward gear engaged. "
  "The opposites - self-justification, defiance, indifference - are "
  "defined by the circuit's refusal at each stage: justification "
  "overturns the verdict, defiance rejects the court, indifference "
  "never convenes it. Misidentification has costs: treating remorse as "
  "shame (\"you are a bad person\") pushes the deed-focused repair "
  "drive into self-focused hiding; treating shame as remorse (demanding "
  "apology from someone who needs self-compassion) misfires the same "
  "way. Correct identification routes each feeling to its proper "
  "completion - which is the entire practical point of the map."),
 "key_points": [
  "Guilt is the alarm, remorse the full investigation: depth and duration separate them.",
  "Regret wishes the outcome differed and needs no wrongdoing; remorse always carries the moral verdict.",
  "Shame judges the self ('I am bad,' wants hiding); remorse judges the deed ('I did bad,' wants repair).",
  "Contrition is remorse facing forward: the feeling plus the vow, investigation matured into sentence.",
  "Misidentification misfires: shaming remorse pushes repair into hiding; each neighbor needs its own completion."],
 "requirements": [
  "Map remorse against guilt, regret, shame, and contrition with a clear tell-apart test for each.",
  "Name the opposites (self-justification, defiance, indifference) and what each refuses.",
  "Explain the three axes (object of judgment, moral charge, depth) in plain words.",
  "Show the cost of misidentification; no real people, no clinical language."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people."],
 "citations": [CIT_TANGNEY, CIT_LEWIS, CIT_APA],
 "sig_lens": ("The Signature lens keeps this map on the auditor's wall: every "
  "case that enters the office gets correctly filed before it is worked, "
  "because a guilt case worked as a shame case gets the wrong procedure "
  "and the wrong close. The Signature filing rule: judge the deed (remorse), "
  "never the soul (shame's territory); carry the verdict (remorse), not just "
  "the wish (regret); and always move the file forward into contrition - "
  "the vow and the changed procedure. An auditor who misfiles, misfires; "
  "an auditor who files true, closes true.")
},
{
 "key": "remorse_emotion_mixes",
 "name": "Remorse Blends: Dyads With Four Partner Emotions",
 "group": "Advanced", "ladder_rank": 33, "ladder_tier": "advanced",
 "description": ("Remorse blends with other emotions the way colors mix: "
  "the result is not either parent but a third thing with its own "
  "character. Remorse + sadness: the most common blend after guilt - "
  "the deed's wrongness fused with the harm's pain. It feels like "
  "grieving what you yourself broke: heavy, tearful, tender toward the "
  "harmed. The face shows the full grief-muscle pattern; the drive "
  "leans toward gentle, careful restitution. Remorse + anger (at the "
  "self): the verdict with a gavel - the inner voice turns prosecutorial "
  "and the body braces. It feels hot and restless: pacing, jaw tight, "
  "the urge to punish the self or to fix everything immediately. The "
  "danger is the overshoot into self-punishment; the gift is energy - "
  "this blend moves. Remorse + fear: the reckoning plus the threat "
  "assessment - \"I was wrong, and now what happens?\" It feels cold "
  "and vigilant: the loop runs consequence scenarios alongside the "
  "replay, and the drive can tilt toward cover-up if fear outranks "
  "honesty. Handled well, the fear supplies useful caution about making "
  "the repair wisely. Remorse + hope: the least expected and most "
  "redemptive blend - the verdict plus the belief that repair is "
  "possible. It feels like dawn during the trial: the ache remains, but "
  "the forward gear engages - apology drafted, amends planned, the "
  "future re-entering the picture. This is the blend that healthy "
  "remorse matures into: the debt acknowledged, the payment underway, "
  "the person becoming someone the deed does not define. Each dyad is "
  "a different instrument reading on the same audit - and learning to "
  "name the blend is learning to work with it rather than being worked "
  "by it."),
 "how_it_works": ("Blends work by superposition: the two emotions' "
  "appraisals run simultaneously, and the experience is their "
  "interaction, not their sum. Remorse + sadness: the deed-appraisal "
  "(\"I did wrong\") plus the loss-appraisal (\"something precious was "
  "damaged\") - the loss gives the wrongness its weight and its "
  "tenderness, producing the grieving-the-broken-thing quality. Remorse "
  "+ self-anger: the verdict-appraisal plus the blocked-goal appraisal "
  "(\"my own action thwarted who I mean to be\") - anger's energy "
  "fuses with remorse's direction, which is why this blend moves fast "
  "but risks overshooting into punishment. Remorse + fear: the "
  "verdict-appraisal plus the threat-appraisal (\"what will this cost "
  "me?\") - the two compete for the drive's steering, honesty pulling "
  "toward confession and fear pulling toward concealment, and whichever "
  "wins determines whether the blend heals or corrupts. Remorse + hope: "
  "the verdict-appraisal plus the possibility-appraisal (\"repair can "
  "work\") - hope does not erase the verdict but gives the reparative "
  "drive its confidence, converting the loop's energy from rehearsal "
  "into construction. The practical skill is blend literacy: name both "
  "parents, and you can serve each - comfort the sadness, channel the "
  "anger, steady the fear, feed the hope - instead of treating the "
  "blend as one undifferentiated storm."),
 "key_points": [
  "Remorse + sadness: grieving what you broke - heavy, tender, leaning toward gentle restitution.",
  "Remorse + self-anger: the verdict with a gavel - hot, restless energy that moves fast but risks overshooting.",
  "Remorse + fear: verdict vs threat - honesty pulls toward confession, fear toward concealment; the winner decides the outcome.",
  "Remorse + hope: the redemptive blend - the ache remains but the forward gear engages; healthy remorse matures here.",
  "Blend literacy: name both parents to serve each one, instead of treating the mix as one storm."],
 "requirements": [
  "Describe four dyads (sadness, self-anger, fear, hope) each with its felt character and action tendency.",
  "Explain each blend through appraisal superposition in plain words.",
  "End with blend literacy as the practical skill.",
  "All illustrations fictional and general; no real people, no clinical language."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people."],
 "citations": [CIT_IZARD, CIT_LAZARUS],
 "sig_lens": ("The Signature lens reads the blends as the audit committee in "
  "joint session: sadness inventories the damages with care, anger demands "
  "the corrective action with force, fear reviews the exposure with "
  "prudence, hope underwrites the repair plan with confidence. The master "
  "auditor chairs the joint session the same way as the single one: hear "
  "each member, give each its legitimate work, and keep the agenda moving "
  "to the close. The remorse-hope blend is the committee's unanimous vote "
  "to rebuild - and a unanimous committee is how forges get their hottest "
  "fires.")
},
{
 "key": "remorse_full_simulation",
 "name": "Full Simulation: Remorse From Trigger to Resolution",
 "group": "Advanced", "ladder_rank": 34, "ladder_tier": "advanced",
 "description": ("The showcase: one complete arc of remorse, trigger to "
  "resolution, in five scenes - a fictional composite demonstrating "
  "every system in this archive working together. Scene one, the deed: "
  "Marcus, a supervisor, publicly corrects a junior colleague, Priya, "
  "with a sharpness that humiliates her in front of the team. In the "
  "moment he feels efficient; the appraisal has not fired yet. Scene "
  "two, the onset: that evening, driving home, the replay starts - "
  "Priya's face, the room's silence, his own voice. The verdict lands "
  "by the second red light: that was wrong, and he knew better. Chest "
  "heaviness, gut knot, the courtroom convening. Scene three, the "
  "cascade: over three days the chain runs - shame (\"what kind of "
  "leader does that?\"), sadness (her face), self-anger (pacing, jaw "
  "tight), fear (will she quit? will the team trust him?). Sleep "
  "frays; he drafts and deletes the apology text four times. The "
  "avoidance track tempts him - just be extra nice, never name it - "
  "but the loop will not accept the substitute. Scene four, the "
  "repair: on day four he asks Priya for ten minutes, names the "
  "specific deed (\"I humiliated you in front of the team on Tuesday\"), "
  "takes responsibility without 'but,' describes the harm as she "
  "experienced it, and asks what would help. She asks for two things: "
  "a public correction of the record, and that he never do it again. "
  "He does the first that afternoon - awkward, stumbling, face ahead "
  "of his words - and commits to the second as procedure: feedback "
  "in private, always. Scene five, the resolution: weeks later, the "
  "aftershock visits once - same conference room, a similar moment, "
  "the scene flashing - but it arrives with its resolution attached: "
  "\"I answered that.\" The loop, finding the ledger closed, releases. "
  "What remains is not the ache but the procedure: the leader who "
  "corrects in private. The audit is complete - findings faced, report "
  "filed, restitution paid, corrective action verified. The forge did "
  "its work: the mistake became the method."),
 "how_it_works": ("The simulation integrates every mechanism in the "
  "archive. The delayed onset shows the appraisal needing quiet; the "
  "cascade shows the layered appraisal unfolding (deed, self, harm, "
  "blocked goal, threat); the draft-and-delete cycles show the "
  "reparative drive colliding with fear; the temptation of the "
  "avoidance track shows the side channel; the four-movement repair "
  "(honest feeling, plain specific speech, sized restitution, conduct "
  "change) shows the proper channel discharging each demand in order; "
  "the stumbling public correction shows the face-before-words timing "
  "and the disfluency of real remorse; the aftershock-with-resolution "
  "shows cue-dependent retrieval meeting a filed-with-answer memory. "
  "Nothing in the arc is magic: each scene follows from the circuit, "
  "and the resolution follows from completing the circuit's proper "
  "movements rather than its side channels. That is the archive's "
  "central claim, demonstrated rather than asserted: remorse is a "
  "functional system with a designed completion, and the completion is "
  "available to anyone willing to walk the four movements. The "
  "simulation is the proof of the system - the whole emotion, from "
  "trigger to resolution, running clean."),
 "key_points": [
  "Scene one (deed) to scene two (onset): the appraisal fires in the quiet after, verdict by the second red light.",
  "Scene three (cascade): shame, sadness, self-anger, fear in order; draft-and-delete; the avoidance temptation refused.",
  "Scene four (repair): the four movements - specific naming, no-'but' responsibility, her actual terms, public correction plus new procedure.",
  "Scene five (resolution): the aftershock arrives with its answer attached; the loop releases on a closed ledger.",
  "The arc's claim, demonstrated: remorse is a functional system with a designed completion - the four movements walked in order."],
 "requirements": [
  "Tell five scenes - deed, onset, cascade, repair, resolution - as one continuous fictional arc.",
  "Weave in at least ten named mechanisms from earlier records (onset delay, cascade order, draft-delete, face-before-words, etc.).",
  "Make the repair follow the four movements exactly; make the resolution show the filed-with-answer memory.",
  "End with the archive's central claim demonstrated; no real people, no clinical language."],
 "standards": ["Descriptive and educational only - no diagnosis, no labels on real people."],
 "citations": [CIT_TANGNEY, CIT_BAUMEISTER, CIT_LAZARUS],
 "sig_lens": ("The Signature lens presents this arc as the master audit, "
  "executed to the Signature standard: evidence faced without flinching, "
  "findings reported to the affected party in plain specific language, "
  "restitution per her actual accounting, corrective action implemented as "
  "permanent procedure and verified over weeks. Marcus does not merely feel "
  "remorse - he works it, the way a master works the forge: heat, hammer, "
  "quench, temper. The mistake became the method. That transmutation - "
  "wrongdoing converted through honest audit into trustworthy procedure - "
  "is the Signature definition of integrity, and this simulation is its "
  "portrait.")
}
]
