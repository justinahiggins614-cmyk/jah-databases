#!/usr/bin/env python3
"""34 ladder-ordered full entries for The Anticipation Emotion Database.

Public records: real, fact-checked emotion psychology knowledge
(Plutchik's basic-emotion model, appraisal theory, affective science
landmarks cited per record). Signature records: the same ladder through
his original Signature lens, clearly labeled Signature-made.

Apostrophes are avoided in all strings to keep downstream JS embedding clean.
"""

CIT = [
    "Plutchik R. (1980). Emotion: A Psychoevolutionary Synthesis. Harper and Row.",
    "Lazarus R. S. (1991). Emotion and Adaptation. Oxford University Press.",
    "Russell J. A. (1980). A circumplex model of affect. Journal of Personality and Social Psychology.",
    "Frijda N. H. (1986). The Emotions. Cambridge University Press.",
    "Scherer K. R. (2001). Appraisal considered as a process of multilevel sequential checking.",
]

SIG_TAIL = ("Signature lens: his original Signature interpretation of the emotional "
            "landscape - clearly labeled Signature-made, never presented as authentic "
            "public record.")

ENTRIES = [
# ---------------- 1-4: What anticipation IS ----------------
dict(key="e01", ladder_rank=1, ladder_tier="foundations", group="Description",
 name="What Anticipation Is: A Plain-Language Definition",
 description=("Anticipation is the feeling of leaning forward in time. It is what you feel "
  "when something has not happened yet, and your mind and body are already moving toward it. "
  "Waiting for exam results, counting the days before a trip, watching a package cross the map "
  "on a delivery tracker - these are all anticipation. The feeling has a direction: it points "
  "toward a future event. Unlike looking backward at the past, anticipation looks ahead, and "
  "the looking itself is an activity - the brain rehearses what might happen, the body prepares "
  "to act, and attention narrows onto the coming moment. Anticipation can be pleasant, as when "
  "a much-wanted visit approaches, or uncomfortable, as when a difficult conversation is "
  "scheduled. The pleasure or discomfort comes not from the event itself, which has not happened, "
  "but from the brain's preview of it. In that sense anticipation is imagination with a pulse: "
  "the preview feels real enough to move the heart rate, warm the face, and change how the day "
  "feels long before anything arrives."),
 how_it_works=("Psychologists describe anticipation as a forward-looking emotion built from three "
  "parts: expectation (the belief that something is coming), appraisal (judging whether it will be "
  "good or bad), and arousal (the body warming up to meet it). When a future event is noticed, the "
  "brain runs a simulation - it builds a model of what is likely, borrows feeling from that model, "
  "and hands the body the resulting instructions. That is why the body can react to a calendar entry "
  "as if it were a small emergency or a small celebration. The stronger the expected event matters to "
  "the person, and the closer it is in time, the stronger the anticipation usually becomes."),
 key_points=[
  "Anticipation points at the future, never the past.",
  "It has three parts: expectation, appraisal, and bodily arousal.",
  "It can be pleasant or unpleasant depending on the previewed outcome.",
  "The brain builds a simulation of what is coming and reacts to the simulation.",
  "Importance of the event and closeness in time both raise its strength.",
  "It is a distinct emotion, not just impatience or excitement.",
 ],
 requirements=[
  "Keep the description free of clinical or diagnostic language.",
  "Use everyday examples from ordinary life.",
  "Cover both pleasant and unpleasant forms.",
  "Explain the simulation idea in plain words.",
 ],
 standards=["Plutchik basic-emotion model", "Lazarus appraisal framework"],
 citations=list(CIT),
 sig_lens=("The Signature lens names anticipation the compass emotion. A compass does not make "
  "the traveler arrive, but it changes every step - pointing the eyes, the feet, and the heart "
  "toward what has not happened yet. In his system, anticipation is the earliest instrument of "
  "intention: before a plan is built, the feeling of the future arrives and begins tuning the "
  "body like an engine warming before the run.")),
dict(key="e02", ladder_rank=1, ladder_tier="foundations", group="Description",
 name="Where Anticipation Sits in the Emotion Family",
 description=("In Robert Plutchik's wheel of emotions, anticipation is one of the eight basic "
  "emotions, standing opposite surprise. Its mild form is called interest - the quiet pull toward "
  "something new. Its intense form is called vigilance - a sharp, sustained readiness. This tells "
  "you what anticipation is at heart: the emotion of attention aimed at what is coming. Other "
  "primary emotions feed it constantly. Fear feeds it when danger is expected, turning it toward "
  "dread. Joy feeds it when a good outcome is expected, turning it toward eager waiting. Anger "
  "can feed it when a confrontation is scheduled, sharpening it into a ready stance. Trust feeds "
  "it when something is believed to be reliable, warming it into hope. So anticipation is both "
  "a basic emotion in its own right and a carrier: it blends easily with other feelings, which is "
  "why it shows up inside so many emotional mixes. Expectation without feeling is just a calendar "
  "note; anticipation is what happens when the note starts mattering to the heart."),
 how_it_works=("Emotion-family models place anticipation on the axis of time orientation: past "
  "emotions (like guilt or nostalgia) face backward, while anticipation faces forward. Plutchik's "
  "model further gives anticipation its own opposite (surprise - what happens when the unpreviewed "
  "arrives) and its own dyads: anticipation blended with joy makes optimism, and anticipation "
  "blended with trust makes hope. Understanding the family position helps learners recognize that "
  "when they feel mixed emotions about the future, anticipation is usually the base layer, with "
  "fear, joy, anger, or trust supplying the flavor."),
 key_points=[
  "Plutchik lists anticipation as one of the eight basic emotions, opposite surprise.",
  "Mild form: interest. Intense form: vigilance.",
  "It blends with joy to form optimism and with trust to form hope.",
  "Fear, anger, joy, and trust all feed into anticipation and flavor it.",
  "It is the base layer under most mixed feelings about the future.",
  "Time orientation is its defining axis: it faces forward.",
 ],
 requirements=[
  "Explain Plutchik's wheel in plain language.",
  "Name the mild and intense forms and the opposite.",
  "Name the two classic dyads: optimism and hope.",
  "Keep it educational, never diagnostic.",
 ],
 standards=["Plutchik psychoevolutionary synthesis", "Russell circumplex"],
 citations=list(CIT),
 sig_lens=("In the Signature system, emotions are arranged not as a circle but as an instrument "
  "panel. Anticipation is the forward gauge - the one that reads what has not arrived. His lens "
  "treats the family blends as calibrations: joy calibrates the gauge toward eagerness, fear "
  "calibrates it toward readiness, and the skilled traveler learns to read the gauge itself "
  "rather than mistaking every reading for the weather.")),
dict(key="e03", ladder_rank=1, ladder_tier="foundations", group="Description",
 name="Anticipation from Mild to Intense: The Same Feeling at Different Volumes",
 description=("Anticipation comes in volumes, and the same emotion sounds different at each one. "
  "At mild volume it is interest: a light leaning-in, like noticing a new book on a shelf and "
  "wondering what is inside. The body barely stirs; attention just tilts. At moderate volume it "
  "is full anticipation: plans get checked twice, the calendar gets opened for no reason, the "
  "future event starts coloring ordinary moments. You are waiting for a guest, so the kitchen is "
  "cleaned early and cleaned again. At intense volume it becomes vigilance: the senses go on "
  "standby, sleep gets thin, small sounds carry large meanings. A parent waiting for a teen to "
  "arrive home late at night lives at this volume. The ladder matters because the same advice "
  "does not work at every level. Mild anticipation needs no management at all - it is pleasant "
  "seasoning. Moderate anticipation benefits from small preparations and schedules. Intense "
  "anticipation, the vigilance level, needs deliberate calming practices, because a body held at "
  "standby too long grows tired and jumpy. Learning the volumes lets a person match the response "
  "to the level instead of treating all anticipation as either nothing or an emergency."),
 how_it_works=("Arousal theory treats emotional intensity as a continuum driven by perceived "
  "importance, perceived uncertainty, and temporal closeness. Mild anticipation arises when "
  "uncertainty is low and the event is distant or trivial. Moderate anticipation arises when "
  "importance rises or the date draws near. Intense anticipation arises when importance is high "
  "and uncertainty is high at the same time - the brain cannot finish the simulation, so it keeps "
  "running it, which keeps the body activated. This is why uncertainty stretches anticipation: a "
  "definite bad outcome is often calmer to wait for than an unknown one."),
 key_points=[
  "Mild anticipation is interest; intense anticipation is vigilance.",
  "Importance, uncertainty, and closeness in time control the volume.",
  "Each volume calls for a different response, not the same one.",
  "Uncertainty stretches anticipation longer than bad news does.",
  "Moderate anticipation is usually the most productive level.",
  "Knowing the volume prevents overreacting to mild feelings.",
 ],
 requirements=[
  "Give concrete examples at all three volumes.",
  "Explain what raises and lowers the volume.",
  "Note that management differs per volume.",
  "Stay descriptive, not clinical.",
 ],
 standards=["Arousal theory", "Plutchik intensity gradients"],
 citations=list(CIT),
 sig_lens=("His lens calls the three volumes low watch, full watch, and night watch. A sailor on "
  "low watch enjoys the horizon; on full watch the crew works the ropes; on night watch nobody "
  "sleeps and every sound is a signal. The Signature lesson: the watch level is information, not "
  "a command - the skilled reader adjusts the watch instead of letting the watch run the crew.")),
dict(key="e04", ladder_rank=1, ladder_tier="foundations", group="Description",
 name="Myths and Misunderstandings About Anticipation",
 description=("Several stubborn myths surround anticipation. The first is that anticipation is "
  "always pleasant - the myth of the pure countdown. In truth, dread is anticipation too, and a "
  "large share of waiting is uncomfortable. The second myth is that it is harmless: just a "
  "feeling while you wait. But sustained high-intensity anticipation genuinely wears the body "
  "down - thin sleep, tight stomachs, shortened patience - so it deserves the same care as any "
  "strong emotion. The third myth is that excitement and anticipation are the same thing. They "
  "are close cousins: excitement is joy about what is coming, while anticipation is the waiting "
  "itself, which can carry joy, fear, or both. The fourth myth is that worrying is just strong "
  "anticipation. Worry is anticipation plus a stuck loop of negative previews; it is a related "
  "but different process that keeps rehearsing the worst case instead of preparing for the likely "
  "one. The fifth myth is that the feeling proves the outcome: if the waiting feels terrible, the "
  "event must be terrible. But the preview is not the event. A wedding morning can be full of "
  "nerves and turn out joyful; a feared test result can arrive benign. Anticipation is a "
  "forecast, and forecasts are sometimes wrong."),
 how_it_works=("These myths persist because anticipation mixes feeling with prediction, and people "
  "naturally treat strong feeling as strong evidence. Affective forecasting research shows that "
  "people systematically overestimate how strongly future events will affect them, which feeds "
  "the fifth myth. Clearing the myths gives learners a cleaner instrument: they can feel the "
  "pull of the future without mistaking the pull for the future itself."),
 key_points=[
  "Anticipation is not always pleasant; dread is also anticipation.",
  "It is not harmless at high intensity; the body pays for sustained vigilance.",
  "Excitement is joy about the future; anticipation is the waiting itself.",
  "Worry is anticipation plus a stuck negative loop, a different process.",
  "The preview is a forecast, not the event, and forecasts can be wrong.",
  "Strong feeling is not strong evidence about what will happen.",
 ],
 requirements=[
  "Name and correct at least four common myths.",
  "Separate anticipation from excitement and worry.",
  "Explain affective forecasting briefly.",
  "Keep all corrections educational and gentle.",
 ],
 standards=["Affective forecasting literature", "Plutchik emotion distinctions"],
 citations=list(CIT),
 sig_lens=("The Signature myth-busting rule: never mistake the gauge for the territory. His lens "
  "teaches that the needle pointing hard is still just a needle - it reports pressure, not "
  "destiny. Each corrected myth is framed as instrument calibration: clean gauges make better "
  "voyages, and a traveler who stops arguing with the gauge can finally steer by it.")),
# ---------------- 5-9: How it feels ----------------
dict(key="e05", ladder_rank=2, ladder_tier="foundations", group="Lived Experience",
 name="Inside the Feeling: A First-Person Passage of Anticipation",
 description=("It starts as a small tilt. You are doing something ordinary - washing a cup, "
  "scrolling, walking to the bus - and underneath it there is a second track running, quieter "
  "but persistent, playing the coming thing on loop. The day has a hinge in it now: everything "
  "before the event and everything after, and you are standing on the before side, leaning. "
  "Time feels elastic. The hours are the same length they always were, but they pass slower, as "
  "if the day knows you are watching the clock. Your thoughts keep rehearsing: what it will look "
  "like, what you will say, what could go sideways. The rehearsals are not plans; they are scenes "
  "you watch yourself in. Your body joins in without being asked. There is a light fullness in "
  "the chest, a restlessness in the legs, a wish to be doing something with your hands. You "
  "check things: the bag, the ticket, the message thread - checked twice already, checked again. "
  "This is the texture of anticipation from the inside: ordinary life running on the surface, and "
  "the future humming underneath like a refrigerator you only notice when the room goes quiet."),
 how_it_works=("First-person simulation passages teach by immersion rather than definition. "
  "This one layers the known components of anticipation - temporal elasticity, involuntary "
  "rehearsal, preparatory restlessness, checking behavior - into a single continuous scene so "
  "the learner can recognize the pattern from the inside. Recognition from the inside is what "
  "lets a person name the feeling in real time instead of only analyzing it afterward."),
 key_points=[
  "Time feels slower while waiting, a well-documented effect.",
  "The mind rehearses scenes involuntarily.",
  "Restlessness and checking behaviors are the body's contribution.",
  "The feeling runs underneath ordinary activity.",
  "Recognition from inside is the point of the passage.",
  "It is a simulation, never a diagnosis of the reader.",
 ],
 requirements=[
  "Write in present tense, second person.",
  "Cover thought, body, time perception, and behavior.",
  "Keep it relatable and non-clinical.",
  "End on recognition, not on advice.",
 ],
 standards=["Phenomenological description", "Lazarus appraisal components"],
 citations=list(CIT),
 sig_lens=("His lens renders the first-person passage as a helm log. The traveler notes the "
  "tide pulling before the ship moves, the crew restless before the order is given, the horizon "
  "occupying more of the eye than the deck. The Signature log teaches the same lesson as the "
  "compass: record the pull faithfully, and the pull becomes data instead of weather.")),
dict(key="e06", ladder_rank=2, ladder_tier="foundations", group="Lived Experience",
 name="The Timeline of Anticipation: Onset, Peak, Fading, Aftershock",
 description=("Anticipation has a shape over time, like a wave with four sections. Onset is the "
  "moment the future event enters awareness: an email arrives, a date is set, a rumor lands. "
  "The feeling is small and curious at first - a seed. The build is the long middle: the event "
  "approaches, the seed grows, rehearsals multiply, preparations stack. This is where the "
  "feeling lives most of its life, rising as the date nears and spiking whenever a reminder "
  "appears. The peak arrives in the hours just before the event, sometimes minutes before: the "
  "body is fully warmed, attention is fully narrowed, and everything else in the day dims. Then "
  "the event happens, and fading begins - often faster than people expect. The wave breaks and "
  "the body lets go, sometimes into relief, sometimes into a strange flatness. The aftershock is "
  "the part people forget to expect: echoes of the feeling that return after the event - "
  "replaying what happened, comparing it to the preview, feeling a second, smaller wave of the "
  "waiting itself. Knowing the timeline matters because the worst hour of anticipation is almost "
  "never the event; it is the hour before it, and the fastest exit from that hour is the event "
  "itself arriving."),
 how_it_works=("Affective dynamics research maps emotions as trajectories rather than static "
  "states: rise time, peak, decay, and recovery. Anticipation is unusual because its peak is "
  "pinned to an external future event, which makes its timeline more predictable than most "
  "emotions. The aftershock reflects comparison processes: the brain checks the outcome against "
  "the preview, and the mismatch or match produces a secondary wave."),
 key_points=[
  "Onset: the event enters awareness; the feeling is small.",
  "Build: the long rise as the date nears and reminders land.",
  "Peak: hours or minutes before the event; attention fully narrowed.",
  "Fading: often faster than expected once the event begins.",
  "Aftershock: echoes as the brain compares outcome to preview.",
  "The worst hour is usually the hour before, not the event.",
 ],
 requirements=[
  "Name all four phases plus the aftershock.",
  "Explain what drives each phase.",
  "Give the practical insight: the peak is before, not during.",
  "No clinical language.",
 ],
 standards=["Affective dynamics", "Lazarus appraisal"],
 citations=list(CIT),
 sig_lens=("In his system the timeline is a tide chart: flood, slack before the turn, high water, "
  "ebb, and the backwash after. The Signature navigator learns that the tide cannot be argued "
  "with - it can only be read. Read it well and the traveler stops fearing the flood and starts "
  "scheduling around it.")),
dict(key="e07", ladder_rank=2, ladder_tier="foundations", group="Lived Experience",
 name="Anticipation at Low Intensity vs High Intensity: Two Lived Snapshots",
 description=("Low intensity. Sunday morning. You have tickets to a concert next month, and the "
  "thought drifts through while you make coffee: the venue, the lights, the friend going with "
  "you. The feeling is a warm coin in the pocket - you notice it when you reach in, and the rest "
  "of the time it just adds a small richness to the day. Your body is unchanged; your plans are "
  "unchanged; the future is simply flavored. High intensity. The night before a job interview "
  "that decides the next five years. You have laid out clothes, rehearsed answers, set two "
  "alarms. Sleep comes in shallow patches. You wake at 3 a.m. with the opening sentence of your "
  "introduction running in your head like a stuck song. Your stomach is tight, your shoulders "
  "are up near your ears, and the hours until morning have to be gotten through, not lived. The "
  "same emotion lives in both scenes. The difference is volume: importance is high, the outcome "
  "is uncertain, and the event is close. Neither snapshot is wrong. The coffee-morning version "
  "is anticipation doing its lightest work - flavoring the future. The 3 a.m. version is "
  "anticipation doing its heaviest work - preparing the organism for what matters most. The "
  "skill is knowing which snapshot you are in, and not treating the 3 a.m. one as if it will "
  "last, or the coffee one as if it were nothing."),
 how_it_works=("Contrast snapshots teach intensity discrimination: the ability to tell volumes "
  "apart from the inside. The low snapshot shows anticipation as pure seasoning - minimal "
  "arousal, minimal behavior change. The high snapshot shows full mobilization - sleep "
  "disruption, rehearsal loops, preparatory behavior. Both are the same mechanism; the inputs "
  "(importance, uncertainty, closeness) differ."),
 key_points=[
  "Low intensity flavors the day; high intensity reorganizes it.",
  "Sleep and appetite only change at higher volumes.",
  "Both snapshots are the same mechanism with different inputs.",
  "Intensity discrimination is a learnable skill.",
  "The high version is temporary; the peak passes.",
  "Neither volume is a malfunction of the feeling.",
 ],
 requirements=[
  "Give two vivid, contrasting present-tense scenes.",
  "Name the inputs that differ between them.",
  "Close with the skill: knowing which volume you are in.",
  "Keep both scenes ordinary and relatable.",
 ],
 standards=["Arousal theory", "Phenomenological description"],
 citations=list(CIT),
 sig_lens=("His Signature comparison sets the two snapshots side by side as sea states: a calm "
  "swell and a storm watch. Same ocean, different weather. The Signature sailor does not scold "
  "the storm for being a storm; the sailor reefs the sails, checks the lines, and remembers "
  "that every storm in the log eventually blew itself out.")),
dict(key="e08", ladder_rank=2, ladder_tier="foundations", group="Lived Experience",
 name="Anticipation Mixed with Excitement: Its Most Common Partner",
 description=("Excitement is anticipation's most common traveling companion, and the two blur so "
  "easily that many people have no separate name for anticipation at all. Here is the seam: "
  "excitement is joy aimed at the future, the bright feeling that something good is coming. "
  "Anticipation is the waiting itself - the lean, the rehearsal, the hum. When the future looks "
  "good, they travel together and the blend is eagerness: the birthday trip that is three days "
  "away, planned down to the snacks, with every reminder a small jolt of pleasure. When the "
  "future looks mixed, they separate and you can feel the seam: a job offer that is also a move "
  "away from friends brings excitement about the work and dread about the leaving, both riding "
  "the same waiting. Learning to feel the two layers separately is useful. If the excitement is "
  "strong but the anticipation is painful - the planning feels like dread - then something about "
  "the coming event needs attention before it arrives. If the anticipation is sweet but the "
  "excitement is thin - you are waiting eagerly for something you are not actually thrilled "
  "about - then the waiting itself may be doing the work: the event has become a symbol of "
  "change, and the feeling is about the change, not the tickets."),
 how_it_works=("Plutchik's dyads name the blends: anticipation plus joy equals optimism; the "
  "close neighbor excitement is the high-arousal form of that same blend. Emotion-mixing "
  "research shows that mixed feelings are the norm, not the exception, and that people who can "
  "label the layers (affect labeling) regulate better. The seam between anticipation and "
  "excitement is therefore a practical teaching point: name both layers and each can be handled "
  "on its own terms."),
 key_points=[
  "Excitement is joy about the future; anticipation is the waiting itself.",
  "The pleasant blend is eagerness; the mixed blend carries both layers.",
  "Feeling the seam lets each layer be handled separately.",
  "Affect labeling improves regulation of mixed feelings.",
  "Painful waiting inside exciting news signals something to examine.",
  "Sweet waiting for a thin prize signals the event is a symbol of change.",
 ],
 requirements=[
  "Draw the seam between the two feelings clearly.",
  "Give examples of both the pleasant and the mixed blend.",
  "Teach affect labeling as the practical skill.",
  "Avoid clinical or therapeutic claims.",
 ],
 standards=["Plutchik dyads", "Affect labeling research"],
 citations=list(CIT),
 sig_lens=("The Signature lens treats the blend as two currents in one strait: the bright "
  "surface current of excitement and the deep pull of the waiting. A navigator who cannot tell "
  "currents apart gets carried; one who can read both sets the sails for each. His rule: name "
  "the waters before you sail them.")),
dict(key="e09", ladder_rank=3, ladder_tier="foundations", group="Lived Experience",
 name="A Day in the Life of Anticipation",
 description=("6:40 a.m. The alarm, and before the eyes are fully open the thought is there: "
  "today is the day the results post. The stomach registers it first, a small hollow note. "
  "8:15. Commute. The phone is checked twice for messages that cannot possibly have arrived yet. "
  "A song from the summer the course started plays, and it lands differently - it belongs to the "
  "before-time now. 10:30. Work, but the work is surface; underneath, rehearsals run: opening the "
  "portal, seeing the number, the two versions of the afternoon. Lunch is eaten without tasting "
  "it. 12:05. A friend texts, asking if you have heard. The phone buzzes and the heart jumps "
  "before the brain even reads the screen - that is the peak arriving early, triggered by a "
  "false alarm. 2:00 p.m. The portal is refreshed. Nothing. The afternoon stretches like warm "
  "candy. Small tasks are done with unusual thoroughness - the desk gets organized, because "
  "organizing is something the hands can do while the mind waits. 4:47. It posts. The number is "
  "read three times to be sure. The wave breaks: shoulders drop, breath deepens, and there is "
  "laughter that has nothing to do with humor. Evening. The results are told and retold, and "
  "underneath the telling there is a quieter feeling - the aftershock, the body still echoing "
  "the waiting it no longer needs. The day is over. Anticipation ran underneath every hour of "
  "it, and never once touched the actual event until the last scene."),
 how_it_works=("The day-in-the-life vignette compounds every earlier component - onset, build, "
  "false-alarm peak, preparatory behavior, fading, aftershock - into one continuous realistic "
  "arc. Compounded simulation like this trains pattern recognition across a full day, which is "
  "how the emotion is actually met in life: not as a labeled moment but as an undertone that "
  "colors everything."),
 key_points=[
  "Anticipation runs as an undertone across a whole day.",
  "False alarms trigger early peaks - the heart jumps before the brain reads.",
  "Preparatory busywork is the hands helping the mind wait.",
  "The break of the wave is physical: shoulders, breath, laughter.",
  "The aftershock echoes after the event is over.",
  "The vignette is a teaching story, not a diagnosis.",
 ],
 requirements=[
  "Cover a full day with timestamps.",
  "Include onset, build, false alarm, busywork, break, aftershock.",
  "Keep the scenario ordinary and universal.",
  "No clinical language.",
 ],
 standards=["Affective dynamics", "Phenomenological description"],
 citations=list(CIT),
 sig_lens=("His Signature day-log reads the same hours as a watch schedule: first light with "
  "the lookout posted, midday with the crew restless, the false sail on the horizon at noon, "
  "landfall at last light, and the strange quiet of the deck after. The log's lesson: the whole "
  "day was the voyage, not just the arrival.")),
dict(key="e10", ladder_rank=3, ladder_tier="foundations", group="Body Signals",
 name="The Body of Anticipation: Heart, Breath, Muscles, Stomach, Skin, Energy",
 description=("The body treats an anticipated event like a rehearsal for action, and it shows. "
  "The heart quickens - not the pounding of terror, but a lifted resting rate, a drummer warming "
  "up. Breathing moves higher and faster; sighs appear as the body tries to reset itself. "
  "Muscles take on tone without being used: the jaw sets, the shoulders lift, the hands want "
  "tasks. The stomach is the most honest reporter - butterflies at low intensity, a hollow or "
  "churning feeling at high intensity, appetite swinging either up or down. Skin responds too: "
  "warmth in the face, coolness in the hands, occasional prickling at the scalp when the peak "
  "nears. Energy feels mislabeled: there is plenty of it, but it is jittery, hard to spend on "
  "the task in front of you because the body has earmarked it for the future event. None of this "
  "is malfunction. It is mobilization - the organism getting ready. The signals are strongest "
  "in the hours before the event and usually release quickly once the event begins, which is why "
  "people often report feeling strangely calm the moment the waited-for thing actually starts."),
 how_it_works=("The physiology follows the sympathetic branch of the autonomic nervous system: "
  "anticipation is a mild preparatory stress response. The brain's preview of a coming demand "
  "raises catecholamine activity, which lifts heart rate and muscle tone and shifts blood toward "
  "large muscles - hence cool hands, warm face. The release at event onset reflects the "
  "resolution of uncertainty: preparation ends, performance begins."),
 key_points=[
  "Heart: lifted resting rate, like a drummer warming up.",
  "Breath: higher, faster, with resetting sighs.",
  "Muscles: tone without use - jaw, shoulders, hands.",
  "Stomach: butterflies to churning; appetite swings.",
  "Skin: warm face, cool hands, scalp prickling near the peak.",
  "Energy: plentiful but jittery, earmarked for the future event.",
 ],
 requirements=[
  "Cover heart, breath, muscles, stomach, skin, and energy.",
  "Distinguish from the terror response.",
  "Note the release when the event begins.",
  "Plain language, no medical advice.",
 ],
 standards=["Autonomic physiology", "Stress-response literature"],
 citations=list(CIT),
 sig_lens=("His lens reads the body as an engine room: the heart the throttle opening, the "
  "breath the intake, the muscles the crew at standby stations, the stomach the ballast "
  "shifting. The Signature mechanic checks every gauge without alarm - a warming engine is "
  "not a failing engine, it is an engine getting ready to run.")),
dict(key="e11", ladder_rank=3, ladder_tier="foundations", group="Body Signals",
 name="Posture and Movement: How the Body Carries Anticipation",
 description=("Watch a person who is waiting for something that matters, and the body tells the "
  "story before the mouth does. The posture leans: weight shifts forward, chin lifts slightly, "
  "as if the body is trying to arrive early. The eyes do the most work - scanning, checking the "
  "door, the clock, the phone, returning to the same spots in a loop. Hands stay busy with "
  "small, purposeless tasks: tapping, straightening, picking up and setting down the same "
  "object. Walking changes too - the pace quickens, or the walk becomes a series of short "
  "bursts with stops. At high intensity the movement gets bigger: pacing back and forth along "
  "the same line, the classic corridor walk of the waiting room. The body is rehearsing "
  "approach. Even standing still, an anticipating person is rarely still - there is a visible "
  "readiness, like a sprinter in the blocks before the gun. Children show it most honestly: the "
  "bouncing leg, the craning neck, the inability to sit back in the chair. Adults learn to "
  "suppress the bouncing, but the forward lean and the scanning eyes usually survive the "
  "polish."),
 how_it_works=("Posture research links forward lean and approach behaviors to appetitive "
  "motivation - the body physically orienting toward what it expects. The repetitive small "
  "movements are displacement behaviors: motor energy with nowhere to go, spent in loops. The "
  "eye scanning reflects attention narrowed onto the sources of news about the coming event: "
  "doors, screens, clocks."),
 key_points=[
  "The signature posture is the forward lean - trying to arrive early.",
  "Eyes scan in loops: door, clock, phone.",
  "Hands do small purposeless tasks - displacement behavior.",
  "Walking becomes bursts, stops, or full pacing.",
  "Children show it openly; adults polish it but keep the lean.",
  "Stillness under anticipation is a visible, loaded stillness.",
 ],
 requirements=[
  "Describe posture, eyes, hands, and walking.",
  "Include the pacing image.",
  "Note the child/adult difference.",
  "Keep it observational, not diagnostic.",
 ],
 standards=["Embodied emotion research", "Displacement behavior literature"],
 citations=list(CIT),
 sig_lens=("The Signature observer reads posture like rigging: the forward lean is a sail "
  "catching wind that has not arrived, the pacing a crew walking the deck before the order. "
  "His lens adds the discipline of the still watch - the traveler who can hold the lean "
  "without fidgeting has mastered the posture without suppressing the signal.")),
dict(key="e12", ladder_rank=4, ladder_tier="compounded", group="Body Signals",
 name="Sleep, Appetite, and Energy Effects of Anticipation",
 description=("When anticipation runs hot enough and long enough, it starts taxing the body's "
  "basics. Sleep is the first to go: the mind that rehearses all day rehearses all night too. "
  "Falling asleep takes longer because the preview loop is still running; staying asleep gets "
  "lighter, with vivid dreams about the coming event; and early waking arrives with the thought "
  "already in place, as if the brain posted a sentry. Appetite splits: some people cannot eat - "
  "the stomach is too unsettled, food looks uninteresting - while others graze constantly, "
  "feeding the restlessness. Both are the same mechanism: arousal overriding the normal hunger "
  "rhythms. Energy follows a boom-and-bust pattern. The waiting itself is energizing - the body "
  "is mobilized - but mobilization is expensive, so the days drag into tired evenings where the "
  "person is simultaneously wired and exhausted. After the event, there is often a crash: the "
  "mobilization ends, the bill comes due, and a deep tiredness arrives that sleep alone does "
  "not fix for a day or two. None of this means anything is wrong; it is the cost of running "
  "the engine at standby. The practical lesson is budgeting: a big anticipation week is not the "
  "week to also skip sleep, skip meals, and take on extra load."),
 how_it_works=("Sustained anticipatory arousal keeps the hypothalamic-pituitary-adrenal axis "
  "engaged, which fragments sleep architecture and suppresses or dysregulates appetite. The "
  "post-event crash reflects the withdrawal of mobilization: the body downshifts, and the "
  "accumulated sleep and energy debt surfaces. Sleep hygiene and regular meals do not remove "
  "anticipation, but they lower the volume at which the body pays for it."),
 key_points=[
  "Sleep: harder to fall asleep, lighter sleep, early waking with the thought ready.",
  "Appetite splits - lost in some, grazing in others.",
  "Energy runs wired-and-tired: mobilized by day, drained by evening.",
  "The post-event crash is the bill for standby coming due.",
  "It is a cost of mobilization, not a malfunction.",
  "Budgeting rest and meals lowers the price of a big waiting week.",
 ],
 requirements=[
  "Cover sleep, appetite, and energy separately.",
  "Explain the wired-and-tired pattern.",
  "Include the post-event crash.",
  "Offer only general everyday guidance, nothing clinical.",
 ],
 standards=["Sleep and stress literature", "Autonomic physiology"],
 citations=list(CIT),
 sig_lens=("His lens treats the body as a ship's stores: anticipation draws on them like a long "
  "voyage draws on provisions. The Signature quartermaster plans for it - extra rest before "
  "the long wait, real meals during it, and no surprise when the stores run low after landfall. "
  "A well-provisioned ship weathers any watch.")),
dict(key="e13", ladder_rank=4, ladder_tier="compounded", group="Body Signals",
 name="No Two Bodies Anticipate Alike: Individual Differences in Body Signals",
 description=("One person waits for big news with a churning stomach and steady hands; another "
  "has a calm gut and shaking hands; a third feels nothing in the body at all until the peak "
  "hour, and then everything at once. There is no single correct bodily signature for "
  "anticipation. Temperament sets the baseline: high-reactivity people mobilize faster and "
  "harder, low-reactivity people stay nearer their resting state until the event is close. "
  "History writes the rest: a body that has waited through hard outcomes before may go quiet "
  "and braced, while a body with a history of good surprises may hum with energy. Age matters "
  "too - children show anticipation in their whole bodies because they have not learned to "
  "hold it, and older adults often show it in sleep and digestion before they feel it as a "
  "named emotion. Even the channel differs: stomach people, chest people, hand people, head "
  "people. The practical point is calibration to yourself, not to a textbook. Learn your own "
  "early signals - the personal tell that the waiting has started - and you get the information "
  "hours before the peak. Someone else's calm is not evidence that your butterflies are "
  "excessive; someone else's pacing is not evidence that your stillness means you do not care."),
 how_it_works=("Individual differences in affective physiology come from temperament (reactivity), "
  "interoceptive sensitivity (how strongly internal signals are felt), and learning history "
  "(which channels the body has practiced). Research on interoception shows wide variation in "
  "how accurately people read their own heartbeats and gut signals - so two people can have "
  "identical arousal and report completely different experiences."),
 key_points=[
  "No single bodily signature is correct for anticipation.",
  "Temperament sets the mobilization baseline.",
  "Learning history shapes which channel speaks loudest.",
  "Age changes where the feeling shows first.",
  "Interoceptive sensitivity varies widely between people.",
  "Calibrate to your own early signals, not to others.",
 ],
 requirements=[
  "Give varied concrete examples of different bodies.",
  "Cover temperament, history, age, and channels.",
  "End with self-calibration as the skill.",
  "Never label anyone's response as wrong.",
 ],
 standards=["Temperament research", "Interoception literature"],
 citations=list(CIT),
 sig_lens=("The Signature instrument-maker knows no two gauges read alike: one ship's compass "
  "swings wide, another's barely trembles, and both can be true. His lens teaches personal "
  "calibration - learn the quirks of your own instruments, mark your own early-warning line, "
  "and never judge your gauge by another ship's.")),
# ---------------- 14-17: Facial expression ----------------
dict(key="e14", ladder_rank=4, ladder_tier="compounded", group="Facial Expression",
 name="The Face of Anticipation: Eyes, Brows, Mouth, and Micro-Signs",
 description=("The face of anticipation is the face of attention aimed forward. The eyes widen "
  "slightly - not the round whites of fear, but an alert opening, the upper lids lifting to take "
  "in more. The gaze fixes and tracks: it locks onto the door, the screen, the speaker, and "
  "follows movement with unusual persistence. The brows lift and draw slightly together, the "
  "classic combination of interest and concentration - raised to admit information, knitted to "
  "work on it. The mouth tells the valence story: in pleasant anticipation the lips part "
  "slightly or pull into the beginnings of a smile that never quite arrives; in dread the lips "
  "press and thin, the corners pulling down or tightening. The micro-signs are where the "
  "leakage lives: rapid blinking when the peak nears, a quick tongue touch to the lips, the "
  "nostrils flaring slightly on the inhale, a jaw muscle flickering as it sets and releases. "
  "Children's faces broadcast all of this at full brightness; adult faces run it dimmer but "
  "rarely switch it off. The whole expression can be read in a glance once you know the "
  "grammar: open eyes for attention, lifted-knit brows for working attention, and the mouth "
  "for whether the future looks kind."),
 how_it_works=("Facial expression research (Ekman and successors) maps anticipation-related "
  "displays onto attention and appraisal components: brow raise (frontalis) admits visual "
  "information, brow knitting (corrugator) marks cognitive effort, and mouth configuration "
  "reflects the valence of the appraisal. The micro-signs are autonomic leakage - brief, "
  "involuntary movements that escape deliberate control."),
 key_points=[
  "Eyes: slight widening and persistent tracking of news sources.",
  "Brows: lifted and slightly knitted - interest plus effort.",
  "Mouth: parted or pre-smile when pleasant; pressed and thin when dreading.",
  "Micro-signs: rapid blinking, lip touches, nostril flare, jaw flicker.",
  "Adult faces run the display dimmer but rarely off.",
  "Grammar: eyes for attention, brows for work, mouth for valence.",
 ],
 requirements=[
  "Cover eyes, brows, mouth, and at least three micro-signs.",
  "Distinguish pleasant from dreadful anticipation in the face.",
  "Note the adult/child difference.",
  "Keep it descriptive for artists, actors, and observers.",
 ],
 standards=["Ekman facial expression research", "FACS action-unit mapping"],
 citations=list(CIT),
 sig_lens=("His lens studies the face as a signal flag: eyes the lookout glass raised, brows "
  "the rigging tensioned, mouth the flag that flies the colors - fair winds or foul. The "
  "Signature reader learns the flag code so thoroughly that a glance across the room reads "
  "like a dispatch.")),
dict(key="e15", ladder_rank=5, ladder_tier="compounded", group="Facial Expression",
 name="How the Expression of Anticipation Changes with Intensity",
 description=("At low intensity, anticipation barely touches the face - it is a look of mild "
  "interest: eyes a touch brighter, a small lift at the corners of the mouth, the face relaxed "
  "and open. Someone watching would call it a pleasant, attentive look and might not name it as "
  "anticipation at all. At moderate intensity the attention components engage: the brows lift "
  "and knit, the gaze starts its checking loops, the mouth settles into its valence shape - "
  "parted for the good-awaited, pressed for the dreaded. The face now clearly says waiting. At "
  "high intensity the display goes stark. The eyes widen further and fix; blinking speeds up or "
  "stops in long stares; the jaw sets visibly, sometimes with the masseter muscle standing out; "
  "the lips may be bitten or pressed white. The face can look almost grim even when the awaited "
  "event is happy - a bride the morning of the wedding, a finalist before the announcement - "
  "because at this volume the machinery of waiting overwhelms the flavor of what is waited for. "
  "After the peak breaks, the face transforms in seconds: the brows drop, the jaw releases, and "
  "the whole face softens into relief or crumples into the emotion the event actually delivered. "
  "Readers of faces should remember the grimace rule: at maximum intensity, the face of "
  "anticipation stops advertising the outcome and starts advertising only the effort of "
  "waiting."),
 how_it_works=("Intensity scales facial displays along two dimensions: the attention components "
  "(brow, gaze) strengthen roughly linearly, while the tension components (jaw, lips, blink "
  "rate) escalate sharply near the peak. At extreme arousal the valence signal degrades - the "
  "face shows effort, not flavor - which is why highly anticipating faces look similar whether "
  "the news will be good or bad."),
 key_points=[
  "Low: mild interest, relaxed open face, barely nameable.",
  "Moderate: brows lift and knit, gaze loops, mouth takes its valence shape.",
  "High: stark display - wide fixed eyes, set jaw, bitten or white lips.",
  "At maximum intensity the face shows waiting effort, not outcome flavor.",
  "The break of the peak transforms the face in seconds.",
  "Grimace rule: do not read good/bad from a maximum-intensity face.",
 ],
 requirements=[
  "Describe the face at three intensity levels.",
  "Explain why high-intensity faces look alike regardless of valence.",
  "Include the post-peak transformation.",
  "Keep it practical for observers.",
 ],
 standards=["Ekman facial expression research", "Arousal-display scaling"],
 citations=list(CIT),
 sig_lens=("The Signature scale runs from fair-weather pennant to storm flag: the same mast, "
  "the same cloth, flown harder as the wind rises until the flag flies straight and its "
  "colors blur. His lesson: read the wind from how hard the flag flies, not from the blur "
  "of its colors.")),
dict(key="e16", ladder_rank=5, ladder_tier="compounded", group="Facial Expression",
 name="Hiding and Faking Anticipation: What Leaks Through",
 description=("People hide anticipation for good reasons: the poker player, the job candidate "
  "who does not want to seem desperate, the host who must look calm while the guests are late. "
  "The hiding strategy is usually suppression - holding the face neutral, stilling the hands, "
  "slowing the voice. It works on the big features: the mouth can be kept neutral, the posture "
  "can be arranged. What leaks are the small, fast, and autonomic things. The eyes betray first: "
  "the checking loops continue - glances at the door, the clock, the phone - because attention "
  "cannot be fully faked, only redirected. Blink rate gives the game away under pressure. The "
  "hands leak through micro-fidgets: a thumb rubbing a finger, a pen clicked once and set down "
  "too carefully. Swallowing increases; the throat works when the mouth is being managed. The "
  "voice, if the person must speak, runs slightly fast with clipped endings, or overly slow "
  "with careful control - both are departures from baseline. Faking anticipation - pretending "
  "to look forward to something - leaks in the opposite direction: the big features perform "
  "eagerness while the small ones stay flat, the smile arrives without the eye involvement, the "
  "voice emphasizes without the body leaning in. The asymmetry is the tell: real anticipation "
  "is coordinated from the eyes down; performed anticipation is painted on from the mouth up."),
 how_it_works=("Deception and suppression research shows that deliberate control covers voluntary "
  "muscles (mouth, posture) far better than autonomic or habitual channels (gaze patterns, "
  "blink rate, swallowing, vocal timing). Anticipation is especially leaky because its core is "
  "attention, and attention direction is one of the hardest things to fake - the eyes keep "
  "going where the mind is."),
 key_points=[
  "Suppression covers big features; small fast things leak.",
  "Eyes betray first: checking loops survive deliberate control.",
  "Hands leak micro-fidgets; swallowing increases.",
  "Voice runs fast-clipped or slow-careful under suppression.",
  "Faked anticipation is painted mouth-up; real is coordinated eyes-down.",
  "Asymmetry between channels is the reliable tell.",
 ],
 requirements=[
  "Cover hiding strategies and what leaks.",
  "Cover faking and its opposite-direction leakage.",
  "Name the asymmetry tell.",
  "Frame as observation skill, never as lie-detection claims.",
 ],
 standards=["Ekman leakage research", "Attention and gaze literature"],
 citations=list(CIT),
 sig_lens=("His lens calls the leaks signal flags the crew cannot strike: the captain may order "
  "the decks cleared, but the lookout still turns toward the horizon and the rigging still "
  "creaks. The Signature reader watches the flags that cannot be lowered - they fly the true "
  "orders.")),
dict(key="e17", ladder_rank=5, ladder_tier="compounded", group="Facial Expression",
 name="Expression Gallery Notes: Drawing and Playing Anticipation",
 description=("For the artist: draw the eyes first. Give them a slight widening - upper lids "
  "lifted, irises fully shown - and aim them at something outside the frame; the viewer should "
  "feel the gaze has a target. Lift the inner brows a touch and draw the faintest horizontal "
  "lines on the forehead; add a slight knitting between the brows, one short vertical crease. "
  "The mouth decides the story: for pleasant anticipation, part the lips a few millimeters and "
  "lift the corners just short of a smile; for dread, press the lips into a thin line and pull "
  "the corners down a fraction. Add the leaks sparingly - one is enough: a hand half-raised "
  "toward a phone, or fingers lightly touching the lips. Tilt the whole head a few degrees "
  "forward and to the side, the listening lean. For the actor: the work is in the eyes and the "
  "stillness between checks. Let the gaze go to the door, hold it, and come back - the audience "
  "reads the loop, not the stare. Keep the jaw lightly engaged, as if about to speak, and let "
  "the breath sit high. The voice, when it comes, should be a touch quicker than your baseline, "
  "with sentences that trail toward the future - verbs in the coming tense, questions about "
  "when. Do not play excitement unless the scene calls for it; play the waiting, and let the "
  "audience supply the excitement. The difference between playing anticipation and playing "
  "anxiety on stage is the direction of the energy: anticipation leans toward the event, "
  "anxiety curls away from it."),
 how_it_works=("These notes translate the expression research into craft instructions. The "
  "artist's version isolates the diagnostic features (gaze target, brow configuration, mouth "
  "valence) so a static image carries the emotion. The actor's version uses the temporal "
  "features (checking loops, breath placement, verb tense) because performance unfolds in "
  "time. The anticipation/anxiety distinction gives performers the directional key: approach "
  "versus avoidance."),
 key_points=[
  "Artist: eyes aimed off-frame, lifted-knit brows, mouth sets the story.",
  "One leak detail is enough: a hand, a finger at the lips.",
  "Head tilts forward into the listening lean.",
  "Actor: play the checking loop and the high breath, not the stare.",
  "Voice runs quick with future-tense verbs and when-questions.",
  "Stage key: anticipation leans toward; anxiety curls away.",
 ],
 requirements=[
  "Give separate notes for visual artists and actors.",
  "Include the mouth-valence distinction.",
  "Include the anticipation vs anxiety stage key.",
  "Keep it craft-focused and practical.",
 ],
 standards=["FACS action-unit mapping", "Performance studies"],
 citations=list(CIT),
 sig_lens=("The Signature gallery master teaches the portrait as a chart: every line a sounding, "
  "every shadow a depth mark. His actors rehearse the lean until the audience leans with them - "
  "for in his theater, the waiting is the performance and the event is only the curtain.")),
# ---------------- 18-21: Triggers ----------------
dict(key="e18", ladder_rank=6, ladder_tier="compounded", group="Triggers",
 name="The Classic Triggers of Anticipation",
 description=("Certain situations trigger anticipation so reliably they are practically its "
  "natural habitat. Scheduled evaluations lead the list: exams, interviews, medical test "
  "results, performance reviews - any event where a verdict about you is coming. Countdowns "
  "are second: holidays, trips, releases, due dates - the calendar itself becomes a trigger, "
  "each crossed-off day raising the volume. Third are arrivals: waiting for a person, a "
  "package, a message, a call - anything whose arrival is expected but whose timing is not "
  "fully in your hands. Fourth are competitions and contests: the game, the match, the "
  "audition, where the outcome is uncertain and public. Fifth are thresholds: graduations, "
  "weddings, moves, first days - moments that divide life into before and after. What unites "
  "them is the formula: importance times uncertainty, divided by distance in time. High "
  "importance, high uncertainty, short distance - maximum trigger. Words trigger it too: "
  "\"we need to talk,\" \"the results are in,\" \"guess what\" - each is a verbal starting "
  "gun for the waiting. Even good triggers follow the formula, which is why the most joyful "
  "countdowns can still fray the nerves in the final hours."),
 how_it_works=("Appraisal theory explains triggers as events appraised high on relevance "
  "(this matters to me), uncertainty (the outcome is not settled), and imminence (it is "
  "coming soon). The classic trigger list is the set of life events that reliably score high "
  "on all three. Verbal triggers work by announcing that an appraisal-relevant event has "
  "entered the timeline."),
 key_points=[
  "Scheduled evaluations: exams, interviews, results, reviews.",
  "Countdowns: the calendar itself as a rising trigger.",
  "Arrivals: people, packages, messages with uncertain timing.",
  "Competitions and thresholds: uncertain outcomes, before-and-after moments.",
  "Formula: importance times uncertainty, divided by time distance.",
  "Verbal starting guns: we need to talk, the results are in, guess what.",
 ],
 requirements=[
  "List the five classic trigger families with examples.",
  "State the importance-uncertainty-time formula.",
  "Include verbal triggers.",
  "Note that joyful triggers follow the same formula.",
 ],
 standards=["Lazarus appraisal theory", "Scherer sequential checking"],
 citations=list(CIT),
 sig_lens=("His lens charts the classic triggers as known shoals on every navigator's map: "
  "the evaluation reef, the countdown current, the arrival harbor, the contest strait, the "
  "threshold crossing. The Signature chart marks them not as dangers but as waters that "
  "reward a prepared crew - every sailor learns where they lie.")),
dict(key="e19", ladder_rank=6, ladder_tier="compounded", group="Triggers",
 name="Personal Triggers: Memories, Anniversaries, and Private Associations",
 description=("Beyond the universal triggers, everyone carries a private set - the triggers that "
  "would mean nothing to a stranger but light up anticipation in one particular nervous "
  "system. A song from the summer before a big move can restart the waiting feeling years "
  "later, even in a different context. The smell of a certain food, tied to holiday eves in "
  "childhood, can bring the whole countdown feeling back with the aroma. Anniversaries work "
  "like clockwork triggers: the week before the date each year, the body starts its preparations "
  "before the mind has named the reason. Places are potent too - driving past the building "
  "where the interview happened, or the restaurant where the news was once received, can "
  "switch the feeling on like a light. These personal triggers form through association: the "
  "brain filed the waiting feeling together with the sensory details around it, and now the "
  "details alone can reopen the file. They are usually stronger than people expect and harder "
  "to explain to others, which is why someone can feel suddenly, unreasonably on-edge in a "
  "grocery store aisle that smells like December. The practical move is mapping: notice which "
  "sensory details reopen the file, and the trigger stops being mysterious and becomes "
  "manageable - a known bell that rings on schedule."),
 how_it_works=("Classical conditioning explains personal triggers: a neutral stimulus (a song, "
  "a smell, a date) paired repeatedly with the arousal of waiting becomes a conditioned cue "
  "that elicits the response alone. Anniversary reactions add a temporal conditioning layer - "
  "the calendar date itself becomes the cue. Mapping the cues converts an implicit trigger "
  "into explicit knowledge, which reduces its surprise power."),
 key_points=[
  "Personal triggers are conditioned cues: songs, smells, places, dates.",
  "Anniversaries trigger the body before the mind names the reason.",
  "They form by association - the brain files feeling with sensory detail.",
  "They feel unreasonable because the link is invisible to others.",
  "Mapping the cues converts mystery into manageability.",
  "Everyone's set is different; that is normal.",
 ],
 requirements=[
  "Give sensory examples: song, smell, place, date.",
  "Explain anniversary reactions.",
  "Explain the conditioning mechanism in plain words.",
  "End with mapping as the practical skill.",
 ],
 standards=["Classical conditioning", "Anniversary reaction literature"],
 citations=list(CIT),
 sig_lens=("The Signature logbook keeps a page of private soundings: the cove where the tide "
  "always turns early, the star that always rises before the storm. His navigator marks "
  "personal triggers on the chart in red ink - not to avoid those waters, but to enter them "
  "with the crew already briefed.")),
dict(key="e20", ladder_rank=6, ladder_tier="compounded", group="Triggers",
 name="Surprise Triggers of Anticipation",
 description=("Some triggers of anticipation arrive sideways, from directions nobody would "
  "predict. A completely ordinary Tuesday can start humming because a stranger mentioned a "
  "city you once dreamed of visiting - and suddenly the old dream wakes up and starts "
  "counting down to a trip you have not planned. A weather forecast can do it: the first "
  "snow prediction of the year starts the holiday countdown in people who thought they were "
  "done with that. An overheard fragment - \"they are announcing it Friday\" - can hook the "
  "attention even when you do not know what \"it\" is; the brain starts waiting for the "
  "reveal of the reveal. Technology multiplies these: the typing indicator in a message "
  "thread (those three dots) is a tiny anticipation engine, and the \"your package is eight "
  "stops away\" notification turns an afternoon into a countdown. Even relief can trigger "
  "it: the moment a long dreaded task is postponed, anticipation of the new date starts "
  "immediately, sometimes before the relief has finished. The lesson of the surprise "
  "triggers is that anticipation is cheap to start and expensive to run - the brain will "
  "begin waiting on very thin evidence, and then charge full price in attention and arousal "
  "for a wait that may have no event at the end of it."),
 how_it_works=("Surprise triggers work through partial cues: the brain's prediction machinery "
  "responds to fragments (a city name, three dots, a date) by spinning up a full simulation "
  "from incomplete data. This is predictive processing doing its normal job - better to "
  "prepare for a maybe-event than to be caught flat. The cost is false alarms: simulations "
  "that consume real arousal for events that never arrive."),
 key_points=[
  "Thin cues - a city name, three dots, a forecast - can start full waiting.",
  "The brain prefers preparing for maybe-events over being caught flat.",
  "Technology manufactures micro-triggers: typing indicators, tracking maps.",
  "Relief can instantly convert into anticipation of the new date.",
  "Anticipation is cheap to start and expensive to run.",
  "False alarms cost real arousal for events that never arrive.",
 ],
 requirements=[
  "Give at least four unexpected trigger examples.",
  "Include a technology example.",
  "Explain the cheap-to-start, expensive-to-run principle.",
  "Keep the tone observational and light.",
 ],
 standards=["Predictive processing", "Appraisal theory"],
 citations=list(CIT),
 sig_lens=("His lens names these the will-o-the-wisps: lights on the marsh that look like "
  "harbor lamps and lead the unwary into the mud. The Signature navigator learns to check "
  "every light against the chart - chase the real lamps, note the wisps, and never spend "
  "the crew's strength on a glow with no harbor behind it.")),
dict(key="e21", ladder_rank=7, ladder_tier="compounded", group="Triggers",
 name="Chain Reactions: How Anticipation Sets Off Emotional Cascades",
 description=("Anticipation rarely travels alone for long; it is a first domino. The chain "
  "usually starts like this: a trigger announces a coming event, anticipation rises, and the "
  "rising arousal makes the mind search for what to do - which summons planning, and planning "
  "summons its own emotions. If the plan looks solid, confidence arrives and the anticipation "
  "sweetens into eagerness. If the plan has holes, worry arrives, and the anticipation sours "
  "into dread. Dread then summons avoidance - the urge to not think about it - and avoidance "
  "lets the unpreparedness grow, which feeds the dread further. That is a full cascade from "
  "one starting trigger. Positive cascades exist too: anticipation of a reunion triggers "
  "remembering, remembering triggers warmth, warmth triggers reaching out, and the reaching "
  "out makes the reunion itself better - the cascade improves the event it was waiting for. "
  "The key insight is that the cascade is steerable at the early links. Intervene at the "
  "planning link - make the plan concrete, or deliberately set the worry aside until a chosen "
  "time - and the whole downstream chain changes shape. Wait until the dread-avoidance loop "
  "is spinning, and steering takes ten times the effort. Anticipation is the handle on the "
  "cascade; whoever holds the handle early steers the whole train."),
 how_it_works=("Emotion cascades follow appraisal-feedback loops: each emotional state changes "
  "the appraisal of the situation, which generates the next state. Anticipation's high arousal "
  "plus uncertainty makes it a strong cascade initiator. Early intervention works because the "
  "feedback loops have not yet amplified - this is the same principle behind scheduled worry "
  "time and implementation intentions in the coping literature."),
 key_points=[
  "Anticipation is a first domino; arousal summons planning, planning summons emotion.",
  "Solid plans sweeten it into eagerness; holey plans sour it into dread.",
  "Dread plus avoidance forms a self-feeding loop.",
  "Positive cascades can improve the awaited event itself.",
  "The chain is steerable at the early links, costly to steer late.",
  "Anticipation is the handle on the whole cascade.",
 ],
 requirements=[
  "Walk through a negative cascade link by link.",
  "Walk through a positive cascade link by link.",
  "Teach early intervention at the planning link.",
  "Keep it descriptive, not prescriptive therapy.",
 ],
 standards=["Appraisal-feedback loops", "Coping literature"],
 citations=list(CIT),
 sig_lens=("In his system the cascade is a towline: anticipation takes the strain first, and "
  "every emotion behind it follows the line it sets. The Signature deck officer tends the "
  "towline at the bow, where one hand on the rope steers the whole tow - tend it late, at "
  "the stern, and the sea steers you.")),
# ---------------- 22-25: Behavior ----------------
dict(key="e22", ladder_rank=7, ladder_tier="compounded", group="Behavior",
 name="What People Do When They Feel Anticipation: Typical Actions",
 description=("Anticipation is a doing emotion - it pushes the body toward preparation. The "
  "most universal action is checking: refreshing the page, re-reading the message, looking out "
  "the window, asking \"any news?\" Checking is information foraging; the brain is trying to "
  "close the uncertainty gap. Second is preparing: laying out clothes, packing early, "
  "rehearsing routes, charging devices - converting nervous energy into readiness. Third is "
  "nesting and ordering: cleaning, organizing, making lists - imposing order on the "
  "surroundings when the future will not be ordered. Fourth is seeking company or solitude, "
  "depending on temperament: some people want witnesses to the waiting, others want no audience "
  "for it. Fifth is ritual: the lucky socks, the same breakfast on exam day, the playlist in a "
  "fixed order - small ceremonies that give the waiting a shape. At high intensity the actions "
  "can turn compulsive: the page refreshed forty times, the bag packed and repacked. The line "
  "between preparing and looping is whether the action changes anything: packing once is "
  "preparation; packing four times is the loop wearing a preparation costume. Watching what "
  "people do under anticipation is watching the oldest human strategy for the future: get "
  "ready, and while getting ready is impossible, look busy getting ready."),
 how_it_works=("These behaviors map onto uncertainty-reduction and control-restoration motives. "
  "Checking forages for information; preparing converts arousal into instrumental action; "
  "nesting restores perceived control over the environment; ritual provides predictability "
  "when the event offers none. Compulsive repetition marks the point where the behavior stops "
  "serving its function and starts serving the arousal itself."),
 key_points=[
  "Checking: information foraging to close the uncertainty gap.",
  "Preparing: converting nervous energy into readiness.",
  "Nesting and ordering: controlling surroundings when the future will not comply.",
  "Company or solitude, by temperament; ritual gives waiting a shape.",
  "The preparation/loop line: does the action change anything?",
  "All of it is the old human strategy: get ready.",
 ],
 requirements=[
  "Name five typical action families with the motive behind each.",
  "Draw the preparation vs looping line.",
  "Keep examples everyday and relatable.",
  "Observational tone, no diagnosis.",
 ],
 standards=["Control-restoration research", "Uncertainty-reduction literature"],
 citations=list(CIT),
 sig_lens=("His lens musters the waiting as a crew: the lookouts checking, the deckhands "
  "preparing, the stewards ordering, the chaplain leading the rituals. The Signature captain "
  "inspects the muster with one question - does this work ready the ship, or only tire the "
  "crew? - and stands down whatever only tires.")),
dict(key="e23", ladder_rank=7, ladder_tier="compounded", group="Behavior",
 name="What People Say: The Language and Tone of Anticipation",
 description=("Anticipation has a dialect, and you can hear it in three features. First, verb "
  "tense: the future crowds out the present. \"When it happens,\" \"once we know,\" \"after "
  "Friday\" - the conversation lives ahead of itself. Second, questions about timing and "
  "detail: \"Has anyone heard anything?\" \"What time exactly?\" \"Do you think it will be "
  "morning or afternoon?\" - the mind trying to nail down the un-nailable. Third, rehearsal "
  "speech: people narrate the coming scene out loud - \"So I will walk in and say...\" - or "
  "they run the branches: \"If it goes well, then... but if not, then...\" Tone carries the "
  "valence: pleasant anticipation speaks quickly, with lifted pitch and frequent laughter; "
  "dreadful anticipation speaks either fast and clipped or slow and heavy, with more pauses "
  "and more sighs. There are also the characteristic phrases: \"I just want to know already,\" "
  "\"the waiting is the worst part,\" \"I cannot wait\" (which always means: I am waiting, "
  "and it is costing me). Listen for the ratio of future-tense to present-tense verbs in "
  "someone's speech - when the future tense takes over, anticipation is driving the "
  "conversation, whatever the topic claims to be."),
 how_it_works=("Linguistic markers of anticipation follow from its cognitive structure: future "
  "orientation drives verb tense; uncertainty drives information-seeking questions; simulation "
  "drives rehearsal narration. Prosody (pitch, rate, pausing) reflects arousal and valence. "
  "The future-to-present verb ratio is a simple, teachable listening metric grounded in "
  "these links."),
 key_points=[
  "Verb tense: the future crowds out the present.",
  "Questions cluster on timing and detail.",
  "Rehearsal speech narrates the coming scene and its branches.",
  "Tone: quick and lifted when pleasant; clipped or heavy when dreading.",
  "Signature phrases: I just want to know already; the waiting is the worst part.",
  "Listening metric: the future-tense to present-tense verb ratio.",
 ],
 requirements=[
  "Name the three language features with examples.",
  "Cover tone for both valences.",
  "List characteristic phrases.",
  "Give the verb-ratio listening metric.",
 ],
 standards=["Psycholinguistics of emotion", "Prosody and affect"],
 citations=list(CIT),
 sig_lens=("The Signature listener tunes the ear like a radio officer: verb tenses are "
  "frequencies, and when the band fills with future-tense traffic, the station is identified. "
  "His operators log the phrases the way signalmen log calls - I just want to know already is "
  "always the same transmission, whatever the words around it.")),
dict(key="e24", ladder_rank=8, ladder_tier="advanced", group="Behavior",
 name="How Anticipation Changes Decisions and Judgment",
 description=("Anticipation does not just color the wait; it edits the choices made during it. "
  "First, it shortens time horizons: the waiting mind discounts everything past the event - "
  "diet, budget, and long plans all blur because the brain has parked the future at the "
  "event's doorstep. \"After the results, I will...\" becomes the container for all deferred "
  "life. Second, it inflates the event's importance: the longer the wait, the bigger the "
  "event grows in the mind, which is why people make oversized decisions right before "
  "long-awaited moments - quitting, confessing, proposing - riding the wave's peak rather "
  "than the calm after. Third, it biases risk: pleasant anticipation makes people risk-seeking "
  "(the good thing is coming, so a gamble feels safe), while dread makes people risk-averse "
  "to the point of freezing (do not move until the bad thing passes). Fourth, it narrows "
  "information search: the mind samples evidence that fits the preview - hopeful waiters "
  "collect good omens, dreadful waiters collect warnings - which is confirmation bias wearing "
  "a waiting costume. The practical defense is the calendar rule: never make the big, "
  "irreversible decision at the peak of the wait. Let the event arrive, let the wave break, "
  "sleep once, and then decide with the horizon restored."),
 how_it_works=("These effects trace to well-studied mechanisms: temporal discounting steepens "
  "when a salient future event dominates attention; the affect heuristic lets the feeling "
  "about the wait stand in for judgment about the options; arousal shifts risk preference by "
  "valence; and motivated reasoning narrows evidence sampling to fit the preview. The "
  "calendar rule is a commitment device that moves the decision past the arousal peak."),
 key_points=[
  "Time horizons shorten: life gets deferred to after the event.",
  "The event inflates in importance the longer the wait.",
  "Pleasant waiting encourages risk; dreadful waiting encourages freezing.",
  "Information search narrows to fit the preview - confirmation bias.",
  "Peak-of-wait decisions ride the wave, not judgment.",
  "Calendar rule: decide after the wave breaks, not on its crest.",
 ],
 requirements=[
  "Name four decision effects with mechanisms.",
  "Explain the risk split by valence.",
  "Teach the calendar rule.",
  "Keep it educational, not financial or life advice beyond general guidance.",
 ],
 standards=["Temporal discounting", "Affect heuristic"],
 citations=list(CIT),
 sig_lens=("His lens posts the warning on the chart itself: no course changes at the crest of "
  "the wave. The Signature navigator holds the helm steady through the peak, lets the sea "
  "settle, takes the morning sight, and only then lays the new course - for decisions made "
  "at the crest belong to the wave, not to the captain.")),
dict(key="e25", ladder_rank=8, ladder_tier="advanced", group="Behavior",
 name="Behavior Under High Intensity: How Actions Escalate",
 description=("As anticipation climbs toward its peak, behavior escalates along a predictable "
  "staircase. Step one is increased checking: the page refreshed hourly becomes every ten "
  "minutes. Step two is social broadcasting: the waiting gets announced - posts, messages, "
  "\"tell me the moment you hear\" - recruiting others into the watch. Step three is "
  "preparation overflow: packing expands to contingencies for contingencies; the plan grows "
  "baroque. Step four is displacement and friction: snapping at small things, restless "
  "arguments about nothing, because the arousal needs an outlet and the event will not "
  "provide one yet. Step five is the freeze or the flood: some people go still and quiet, "
  "conserving everything for the moment; others become torrentially busy, filling every "
  "minute so no empty minute can hold the waiting. Neither is better; both are the same "
  "overload wearing different masks. The escalation matters because each step costs more - "
  "in attention, in relationships, in sleep - while buying less: the fortieth refresh buys "
  "nothing the first did not. Recognizing the staircase lets a person step off it: notice "
  "the broadcast urge, the baroque plan, the snap - and name the step. Naming the step does "
  "not end the waiting, but it stops the waiting from spending the household budget."),
 how_it_works=("Escalation follows diminishing returns on uncertainty-reduction: each checking "
  "act yields less information while arousal stays high, so the behavior rate increases to "
  "compensate. Social broadcasting recruits co-regulation; displacement vents arousal onto "
  "safe targets; freeze and flood are the two classic overload responses (conservation versus "
  "occupation). Step-recognition is affect labeling applied to behavior, which research links "
  "to reduced escalation."),
 key_points=[
  "Five steps: checking, broadcasting, preparation overflow, friction, freeze or flood.",
  "Each step costs more and buys less - diminishing returns.",
  "Broadcasting recruits others into the watch.",
  "Freeze and flood are the same overload in different masks.",
  "The fortieth refresh buys nothing the first did not.",
  "Naming the step is the off-ramp.",
 ],
 requirements=[
  "Walk the five-step staircase with examples.",
  "Explain diminishing returns on checking.",
  "Cover freeze and flood as equal overload responses.",
  "End with step-recognition as the skill.",
 ],
 standards=["Uncertainty-reduction literature", "Affect labeling research"],
 citations=list(CIT),
 sig_lens=("The Signature storm drill names every step on the muster list: lookouts doubling, "
  "signals flying, stores over-provisioned, tempers short, the crew either lashed still or "
  "running. His captain reads the drill board, calls the step by name, and stands the crew "
  "down from whatever the storm does not require - for a crew spent before landfall is a "
  "ship unready for the harbor.")),
# ---------------- 26-28: Healthy expression ----------------
dict(key="e26", ladder_rank=8, ladder_tier="advanced", group="Healthy Expression",
 name="Expressing Anticipation Healthily: Saying It, Showing It, and Channeling It",
 description=("Healthy expression of anticipation has three channels, and the healthiest "
  "waiters use all three. Saying it means naming the feeling out loud, plainly and early: "
  "\"I am nervous about Friday,\" \"I am so excited I can barely sit still.\" Naming converts "
  "the hum into a sentence, and sentences can be worked with. Showing it means letting the "
  "body do its honest, moderate version: the bounce in the step, the grin that keeps "
  "appearing, the admitted fidget - not performed, not suppressed, just not hidden. People "
  "around a honestly-shown waiter usually respond with warmth; hidden waiting, by contrast, "
  "reads as tension and makes rooms uneasy. Channeling it means giving the mobilized energy "
  "somewhere real to go: the preparation that actually prepares, the workout that spends the "
  "jitter, the creative work that the heightened attention feeds surprisingly well - many "
  "people do their most focused work in the waiting days, because attention is already "
  "narrowed and only needs a target. The unhealthy alternatives are the two edges: "
  "suppression, which bottles the arousal until it leaks as irritability or insomnia, and "
  "flooding, which lets the waiting colonize every conversation until others start avoiding "
  "the waiter. The middle path is simple to state and takes practice to hold: name it, show "
  "it at honest volume, and put the energy to work."),
 how_it_works=("The three channels map onto evidence-based regulation strategies: affect "
  "labeling (saying it) reduces amygdala reactivity; expressive honesty at moderate volume "
  "avoids the physiological costs of suppression documented in the emotion-regulation "
  "literature; and channeling uses the arousal instrumentally, consistent with the "
  "process model of emotion regulation (situation modification and attentional deployment)."),
 key_points=[
  "Saying it: name the feeling plainly and early.",
  "Showing it: honest moderate display, neither performed nor suppressed.",
  "Channeling it: spend the mobilized energy on real preparation or focused work.",
  "Suppression bottles arousal until it leaks.",
  "Flooding colonizes every conversation and drives people away.",
  "Middle path: name it, show it at honest volume, put it to work.",
 ],
 requirements=[
  "Teach the three channels with concrete examples.",
  "Name both unhealthy edges and their costs.",
  "Keep guidance general and everyday, never clinical.",
  "Encourage practice, not perfection.",
 ],
 standards=["Gross process model of emotion regulation", "Affect labeling research"],
 citations=list(CIT),
 sig_lens=("His lens rigs the three channels as sail, signal, and engine: say it to signal the "
  "fleet, show it to let the sails honestly fill, channel it to put the engine's steam to "
  "the propellers. The Signature seaman neither strikes the colors nor fires the guns in "
  "celebration - the ship sails the waiting under honest canvas.")),
dict(key="e27", ladder_rank=9, ladder_tier="advanced", group="Healthy Expression",
 name="Unhealthy Expression: Bottling Up or Exploding Anticipation",
 description=("Anticipation goes wrong in two classic ways. Bottling it up looks like composure "
  "and costs like a loan: the waiter insists \"I am fine,\" holds the face still, and refuses "
  "the subject - while the body keeps the books. Sleep thins, the jaw aches, patience shortens, "
  "and the feeling leaks sideways into irritability over small things that have nothing to do "
  "with the wait. Bottlers often pride themselves on not making a fuss, and the people around "
  "them pay the fuss's price in atmosphere. The second failure is the explosion: the waiting "
  "takes over the personality. Every conversation is steered back to the event; reassurance is "
  "demanded repeatedly and no reassurance holds; minor delays become catastrophes; and when the "
  "event finally arrives, the exploder is too depleted to meet it well. Exploders are not "
  "stronger feelers than bottlers - both feel the same wave; they just spend it differently, "
  "one by containment and one by broadcast. The costs are mirror images: bottling taxes the "
  "body and the room's mood; exploding taxes relationships and the waiter's own reserves. Both "
  "patterns usually started as sensible strategies in childhood - the quiet house where "
  "feelings were not discussed, or the loud house where only the loudest feeling got answered - "
  "and both can be updated. The update is the same for both: small, regular, honest releases - "
  "a named feeling, a real preparation, a scheduled time to think about it and then done - "
  "instead of all-or-nothing."),
 how_it_works=("Suppression research (Gross) documents the physiological costs of expressive "
  "suppression: elevated sympathetic arousal with no reduction in felt emotion. The "
  "explosion pattern reflects failed down-regulation: repeated reassurance-seeking that "
  "habituates, so each round needs more. Both are stable regulation styles with developmental "
  "roots; both respond to the same graded alternative - regular, bounded expression."),
 key_points=[
  "Bottling looks like composure and costs like a loan.",
  "The body keeps the books: sleep, jaw, patience.",
  "Exploding colonizes conversations and depletes reserves.",
  "Both feel the same wave; they spend it differently.",
  "Both patterns usually started as childhood strategies.",
  "The update: small, regular, honest releases instead of all-or-nothing.",
 ],
 requirements=[
  "Describe both patterns and their mirror-image costs.",
  "Note the developmental roots without blaming.",
  "Teach the graded alternative.",
  "No diagnostic labels, no clinical claims.",
 ],
 standards=["Gross suppression research", "Emotion regulation styles"],
 citations=list(CIT),
 sig_lens=("The Signature engineer reads both failures as pressure-vessel errors: the bottler "
  "seals every valve until the seams groan, the exploder opens every valve until the boiler "
  "runs dry. His engine room runs neither way - the pressure is bled on schedule, a little "
  "at a time, through the proper cocks, and the vessel holds.")),
dict(key="e28", ladder_rank=9, ladder_tier="advanced", group="Healthy Expression",
 name="Everyday Practices That Keep Anticipation in Balance",
 description=("A handful of small practices keep anticipation at working volume. First, the "
  "named wait: say out loud what you are waiting for and when it ends - \"results Friday, "
  "then it is over.\" Bounded waits are cheaper than open-ended ones. Second, scheduled "
  "checking: decide when you will check for news (twice a day, say) and let the urge pass "
  "between times; the urge always passes. Third, preparation with a finish line: make the "
  "list, do the list, close the list - preparation without an end becomes looping. Fourth, "
  "body spending: walk, run, swim, or work with the hands; mobilized energy spent on purpose "
  "is energy that cannot become jitter. Fifth, the second track: keep one absorbing activity "
  "running through the waiting days - a project, a book, a build - so attention has somewhere "
  "to land besides the countdown. Sixth, sleep protection: same bedtime, no screens in the "
  "last hour, because the waiting mind will take any available screen time and convert it to "
  "rehearsal. Seventh, the witness: tell one person you are waiting and how it feels; shared "
  "waiting is lighter waiting. None of these remove anticipation, and none should - the "
  "feeling is doing a job. They keep it at the volume where it prepares instead of "
  "consuming."),
 how_it_works=("Each practice targets a known mechanism: naming bounds the appraisal; scheduled "
  "checking breaks the variable-reward loop of constant checking; finished preparation closes "
  "the control loop; exercise metabolizes arousal; the second track gives attention an "
  "alternative target (attentional deployment); sleep protection preserves recovery; the "
  "witness provides co-regulation. Together they form a low-effort regulation kit."),
 key_points=[
  "Name the wait and its end date - bounded waits cost less.",
  "Schedule checking; let the between-times urges pass.",
  "Prepare with a finish line; close the list.",
  "Spend the body: exercise or hand-work metabolizes arousal.",
  "Keep a second absorbing track running.",
  "Protect sleep; tell one witness.",
 ],
 requirements=[
  "Give seven concrete practices.",
  "Tie each to its mechanism in plain words.",
  "Emphasize the feeling is kept, not removed.",
  "General everyday guidance only.",
 ],
 standards=["Gross process model", "Co-regulation literature"],
 citations=list(CIT),
 sig_lens=("His lens issues the practices as standing orders for the long watch: post the "
  "lookout schedule, muster the crew at fixed bells, work the ship while waiting for the "
  "tide, keep one hand always on useful rope, guard the sleep of the off-watch, and never "
  "stand a long watch alone. The Signature crew follows standing orders - and the long "
  "watch stays a watch, not a storm.")),
# ---------------- 29-31: Recognition ----------------
dict(key="e29", ladder_rank=9, ladder_tier="advanced", group="Recognition",
 name="Reading Anticipation in Others: Face, Body, Voice, and Behavior Cues",
 description=("Reading anticipation in another person is a four-channel skill. Face: look for "
  "the lifted-knit brows, the eyes that keep traveling to the door, the clock, or the phone, "
  "and the mouth held in its valence shape - pre-smile or pressed line. Body: the forward "
  "lean, the busy hands, the pacing or the loaded stillness. Voice: future-tense verbs taking "
  "over, timing questions, rehearsal narration - and the prosody, quick and bright or clipped "
  "and heavy. Behavior: the checking loops, the over-preparation, the sudden thoroughness "
  "with small tasks. The channels rarely lie in the same direction by accident; when three of "
  "four point to waiting, the reading is solid. Two cautions keep the skill honest. First, "
  "baseline: a naturally fidgety person fidgets without waiting, so read change from the "
  "person's normal, not from a textbook picture. Second, valence: do not assume the waiting "
  "is happy because the person is smiling, or terrible because they look grim - at high "
  "intensity the face advertises effort, not outcome. The best confirmation is the gentlest: "
  "ask. \"You seem like you are waiting on something big - am I reading that right?\" People "
  "are usually relieved to have the hum named, and the ask itself is the kindest part of the "
  "skill."),
 how_it_works=("Multi-channel cue integration improves recognition accuracy over any single "
  "channel, consistent with Brunswik's lens model: each observable cue is a probabilistic "
  "indicator, and accuracy comes from combining them against the person's baseline. The "
  "valence caution reflects the intensity-degradation of valence signals documented in "
  "expression research."),
 key_points=[
  "Four channels: face, body, voice, behavior.",
  "Three of four agreeing makes a solid reading.",
  "Read change from the person's baseline, not a textbook.",
  "Do not infer happy or terrible from intensity alone.",
  "Asking gently is both confirmation and kindness.",
  "The skill is observational; it never labels the person.",
 ],
 requirements=[
  "Teach all four channels with concrete cues.",
  "Include the baseline caution and the valence caution.",
  "End with asking as confirmation.",
  "Stress: describe, never diagnose.",
 ],
 standards=["Brunswik lens model", "Ekman expression research"],
 citations=list(CIT),
 sig_lens=("The Signature lookout is trained on all four horizons: the flag signals of the "
  "face, the trim of the body, the wireless traffic of the voice, the wake of behavior. His "
  "standing rule: three bearings make a fix, one bearing makes a guess - and the finest "
  "instrument on the bridge is the simple hail: ship ahoy, are you waiting on the tide?")),
dict(key="e30", ladder_rank=10, ladder_tier="advanced", group="Recognition",
 name="What to Say and Do When Someone Near You Feels Anticipation",
 description=("When someone near you is deep in the wait, a few responses genuinely help and "
  "most of the usual ones do not. What helps: name it with them - \"this waiting sounds "
  "brutal\" - which tells their nervous system the hum is seen. Ask what would help right "
  "now, and accept practical answers: company, distraction, help with a preparation, or "
  "simply being left to pace in peace. Offer bounded reassurance - one honest, specific "
  "reassurance beats ten vague ones: \"you prepared thoroughly; whatever Friday brings, "
  "the preparation was real.\" Lend your calm body: sit with them, keep your own pace slow, "
  "because arousal is contagious and so is steadiness. Mark the end date with them - \"after "
  "Friday this is over either way\" - which shrinks the open-ended dread. What does not "
  "help: \"just relax\" (a command the body cannot obey), \"do not worry\" (a ban on the "
  "feeling), endless speculation about outcomes (which feeds the rehearsal loop), and "
  "toxic cheer - \"it will definitely be fine!\" - which the waiter knows you cannot promise "
  "and which teaches them not to trust your comfort. If the waiting is long, check in on a "
  "schedule rather than waiting to be asked; the ask is often the hardest part for the "
  "waiter. And when the event passes, remember the aftershock: the day after deserves a "
  "follow-up, because the echo is loneliest when everyone else has moved on."),
 how_it_works=("Effective support combines validation (naming the feeling, shown to reduce "
  "arousal), instrumental help (practical assistance with preparations), co-regulation "
  "through calm presence (arousal contagion works both directions), and temporal bounding "
  "(making the wait finite). The unhelpful responses fail because they attempt suppression, "
  "offer false certainty, or feed the simulation loop."),
 key_points=[
  "Name it with them: the hum, seen, is lighter.",
  "Ask what would help; accept practical answers.",
  "One honest specific reassurance beats ten vague ones.",
  "Lend calm: steadiness is contagious too.",
  "Mark the end date together.",
  "Check in on schedule; follow up after the aftershock.",
 ],
 requirements=[
  "List helpful responses with the reason each works.",
  "List unhelpful responses with the reason each fails.",
  "Include the aftershock follow-up.",
  "Warm, practical, non-clinical tone.",
 ],
 standards=["Social support literature", "Co-regulation research"],
 citations=list(CIT),
 sig_lens=("His lens musters the support as a harbor crew: the pilot boat that names the "
  "channel, the steady tug that lends its calm mass to the rolling ship, the harbor master "
  "who posts the tide table so the wait has an end. The Signature harbor never shouts at "
  "the ship to calm its own sea - it sends boats.")),
dict(key="e31", ladder_rank=10, ladder_tier="advanced", group="Recognition",
 name="What NOT to Do: Mistakes That Make Anticipation Worse",
 description=("The mistakes people make around someone else's anticipation are consistent enough "
  "to list like hazards. One: minimizing - \"it is not a big deal,\" which tells the waiter "
  "their gauge is broken and adds shame to the waiting. Two: commandeering the wait - taking "
  "over their preparations, refreshing the page for them, which steals the control their "
  "preparing was restoring. Three: speculation spirals - \"but what if...\" conversations that "
  "feel like helping and function as rehearsal fuel. Four: the reassurance treadmill - "
  "answering the same worry the twentieth time with the same comfort, which trains the "
  "worry to return rather than resolving it; better to answer once, honestly, and then "
  "redirect to action. Five: timing ambushes - raising unrelated difficult subjects during "
  "the peak wait, when the person's bandwidth is fully spent; the calendar rule applies to "
  "others too. Six: post-event scorekeeping - \"you worried for nothing,\" which punishes "
  "the feeling retroactively and teaches the waiter to hide the next one. Seven: confusing "
  "your wait with theirs - projecting your own dread or excitement onto their different "
  "feeling. The common thread: every mistake either fights the feeling, feeds the loop, or "
  "steals the waiter's agency. The correction is always the same direction: respect the "
  "feeling, starve the loop, protect the agency."),
 how_it_works=("Each mistake maps to a mechanism: minimizing invalidates (increasing shame "
  "arousal); commandeering removes control (raising helplessness); speculation feeds "
  "simulation; the reassurance treadmill habituates without resolving; ambushes overload an "
  "already-taxed system; scorekeeping punishes expression (raising future suppression); "
  "projection misreads the appraisal. The correction direction follows from the same "
  "mechanisms in reverse."),
 key_points=[
  "Do not minimize: it adds shame to the waiting.",
  "Do not commandeer their preparations: it steals restored control.",
  "Do not spiral speculation: it fuels the rehearsal loop.",
  "Do not ride the reassurance treadmill: answer once, then redirect.",
  "Do not ambush with other hard topics at the peak.",
  "No post-event scorekeeping; no projecting your wait onto theirs.",
 ],
 requirements=[
  "List seven mistakes with the mechanism each harms.",
  "Give the correction direction.",
  "Keep the tone firm but kind.",
  "No clinical language.",
 ],
 standards=["Invalidation research", "Emotion regulation literature"],
 citations=list(CIT),
 sig_lens=("The Signature harbor posts its hazards on the breakwater for every pilot to read: "
  "no minimizing the sea, no seizing another captain's helm, no feeding the storm with "
  "speculation, no endless bailing that never patches the hull. His rule for every harbor: "
  "respect the vessel, starve the storm, guard the helm - and every ship leaves your waters "
  "steadier than it came.")),
# ---------------- 32-34: Related emotions and mixes + simulation ----------------
dict(key="e32", ladder_rank=10, ladder_tier="advanced", group="Related Emotions and Simulation",
 name="The Related Emotions Map: Neighbors, Opposites, and Close Cousins",
 description=("Anticipation sits at a busy intersection, and its neighbors are worth mapping. "
  "Nearest neighbors: excitement (joy about the future - the bright twin), hope (anticipation "
  "plus trust - the warm twin), anxiety (anticipation plus threat appraisal - the dark twin), "
  "and curiosity (interest in the unknown - the mild cousin). Opposites: surprise is the "
  "formal opposite - what arrives unpreviewed - and contentment is the functional opposite, "
  "the feeling of nothing pending. Close cousins that get confused: impatience is "
  "anticipation plus frustration at the delay - the complaint about the wait, not the wait "
  "itself. Worry is anticipation plus a stuck negative loop - the rehearsal that will not "
  "release. Eagerness is anticipation plus strong joy - the pleasant extreme. Dread is "
  "anticipation plus strong fear - the unpleasant extreme. Vigilance is anticipation at "
  "maximum intensity regardless of valence. The telling-apart tests: ask about the time "
  "direction (anticipation always faces forward - nostalgia never confuses with it), ask "
  "about the complaint (if the feeling is about the slowness, it is impatience layered on "
  "top), and ask what would end it (if only the event's arrival would end it, it is "
  "anticipation at the core; if information alone would end it, curiosity was driving)."),
 how_it_works=("The map uses three relation types: structural neighbors (shared appraisal "
  "components), formal opposites (Plutchik's wheel), and functional cousins (phenomenological "
  "overlap with distinct cores). The telling-apart tests operationalize the distinctions as "
  "questions a learner can actually ask - time direction, complaint locus, and resolution "
  "condition - which makes the map usable, not just drawable."),
 key_points=[
  "Neighbors: excitement, hope, anxiety, curiosity.",
  "Opposites: surprise (formal), contentment (functional).",
  "Cousins: impatience, worry, eagerness, dread, vigilance.",
  "Test one: time direction - anticipation always faces forward.",
  "Test two: is the complaint about the slowness? Then impatience is layered on.",
  "Test three: what would end it - the event, or just information?",
 ],
 requirements=[
  "Map neighbors, opposites, and at least five cousins.",
  "Give three practical telling-apart tests.",
  "Keep definitions crisp and distinct.",
  "Educational tone throughout.",
 ],
 standards=["Plutchik wheel relations", "Appraisal-component analysis"],
 citations=list(CIT),
 sig_lens=("His lens draws the map as a proper chart: neighboring ports, opposing headlands, "
  "and the cousin coves that look alike from offshore but have different bottoms. The "
  "Signature navigator carries three sounding leads - time, complaint, and resolution - and "
  "takes soundings before naming any water.")),
dict(key="e33", ladder_rank=10, ladder_tier="advanced", group="Related Emotions and Simulation",
 name="Anticipation Blends: Dyads with Excitement, Fear, Hope, and Anxiety",
 description=("Blended with excitement, anticipation becomes eagerness: the countdown to the "
  "concert, the trip planned to the snack level - bright, busy, and generous; the waiter "
  "wants to share it. The body is light, the talk is fast, the preparations are joyful. "
  "Blended with fear, anticipation becomes dread: the waiting for the difficult results, the "
  "night before the hard conversation - heavy, narrow, and private; the waiter goes quiet or "
  "snaps. The body is braced, the talk loops on worst cases, preparations feel like armor. "
  "Blended with trust, anticipation becomes hope: the waiting for the loved one's recovery, "
  "the application sent to the right place - warm, patient, and steady; the waiter can wait "
  "long without fraying because the preview includes a trusted outcome. The body is calm, "
  "the talk is gentle, the waiting itself feels meaningful. Blended with anxiety, "
  "anticipation becomes the full alarm state: the waiting for the unknown verdict with no "
  "trusted information - electric, scattered, and exhausting; the waiter checks everything "
  "and is calmed by nothing. The body is wired, the talk spirals, sleep goes first. The "
  "practical value of the blends: name the partner and you know the playbook. Eagerness wants "
  "sharing and channeling; dread wants bounded preparation and a witness; hope wants "
  "protecting and patience; the alarm state wants information first - uncertainty is its "
  "fuel - and only then the calming practices. Most real waiting is a blend, and the blend "
  "can shift partners mid-wait: eagerness curdling into dread as new information lands is "
  "one of the most human emotional events there is."),
 how_it_works=("Plutchik's dyad theory formalizes two of these blends (anticipation plus joy "
  "equals optimism; anticipation plus trust equals hope); the fear and anxiety blends follow "
  "the same compositional logic with threat appraisals. Blend-shifting reflects appraisal "
  "updating: new information re-weights the partner emotion while the anticipation base "
  "persists. The playbook mapping follows from each partner's regulation needs."),
 key_points=[
  "Plus excitement: eagerness - bright, busy, wants sharing.",
  "Plus fear: dread - heavy, narrow, goes quiet or snaps.",
  "Plus trust: hope - warm, patient, waits long without fraying.",
  "Plus anxiety: alarm state - electric, scattered, calmed by nothing yet.",
  "Name the partner to know the playbook.",
  "Blends can shift partners mid-wait as information lands.",
 ],
 requirements=[
  "Describe four blends with body, talk, and behavior each.",
  "Give the response playbook per blend.",
  "Note mid-wait blend shifting.",
  "Keep it descriptive and practical.",
 ],
 standards=["Plutchik dyads", "Appraisal updating"],
 citations=list(CIT),
 sig_lens=("The Signature blender reads each dyad as a mixed paint: eagerness the bright "
  "gold, dread the iron grey, hope the warm amber, alarm the electric white. His colorist "
  "knows that naming the pigment tells you how it dries, how it covers, and what it can "
  "be painted over - and that the bravest painting of all is watching gold turn grey "
  "mid-canvas and keeping the brush steady.")),
dict(key="e34", ladder_rank=10, ladder_tier="advanced", group="Related Emotions and Simulation",
 name="Full Behavioral Simulation: Anticipation from Trigger to Resolution",
 description=("Scene one, the trigger. Tuesday, 9:12 a.m. Maya gets the email: final-round "
  "interview, Thursday 10 a.m., downtown office. Onset: a small lift in the chest, the date "
  "written three times - calendar, sticky note, phone alarm. She tells one friend; the "
  "telling makes it real. Scene two, the build. Tuesday afternoon to Wednesday night. The "
  "rehearsals start: walking in, the handshake, the first question. She lays out the suit, "
  "researches the company, prints spare resumes - preparation with a finish line, mostly. "
  "Sleep Tuesday is thin; she wakes at 4 a.m. rehearsing answers and writes them down, which "
  "lets her sleep again - the named worry, parked on paper. Scene three, the peak. Thursday "
  "7:30 to 9:55 a.m. The morning is a staircase: checking the route four times, leaving an "
  "hour early, sitting in a cafe nearby with a jaw she has to consciously unclench. The "
  "barista asks if she is okay; she laughs - the honest, moderate show. At 9:55 she walks in, "
  "and something unexpected happens: the moment the waiting ends, the wave breaks. Scene "
  "four, the event. The interview itself is almost calm - the body, done preparing, simply "
  "performs. She answers well, asks good questions, and notices the room instead of her "
  "nerves. Scene five, fading and aftershock. Thursday afternoon: the crash - tired in a way "
  "sleep will fix tonight. Friday: the echo - replaying answers, grading herself, the "
  "aftershock wave. She names it - \"that is the echo, not new information\" - and lets it "
  "pass. The following Tuesday: the offer email. New anticipation begins - the start date, "
  "the first day - and this time she recognizes the hum at onset, schedules her checking, "
  "and protects her sleep. The simulation's lesson, compressed: the trigger starts it, the "
  "build grows it, the peak is the worst hour, the event ends it, the echo follows, and the "
  "next wait is cheaper because the pattern is now known."),
 how_it_works=("The showcase simulation compounds every record in the database into one "
  "continuous arc: trigger (18-21), body signals (10-13), facial expression (14-17), "
  "behavior (22-25), healthy expression (26-28), timeline (6), and aftershock. It is the "
  "archive's demonstration that the components compose into a realistic whole - the "
  "multi-scene proof of the teaching ladder."),
 key_points=[
  "Five scenes: trigger, build, peak, event, fading and aftershock.",
  "Every earlier record's content appears in the arc.",
  "The peak is the worst hour; the event itself is often calm.",
  "Parking the 4 a.m. worry on paper demonstrates the practices.",
  "Naming the echo demonstrates the recognition skills.",
  "The next wait is cheaper: the pattern is now known.",
 ],
 requirements=[
  "Five scenes minimum, named character, realistic arc.",
  "Weave in body, face, behavior, and practices from earlier records.",
  "End with the compressed lesson.",
  "Fictional character; descriptive and educational only.",
 ],
 standards=["Affective dynamics", "Emotion regulation literature"],
 citations=list(CIT),
 sig_lens=("His lens stages the same five scenes as a voyage log: the dispatch received, the "
  "fitting-out, the night watch before landfall, the harbor entry, and the quiet deck after. "
  "The Signature log closes with the entry every navigator writes sooner or later: the sea "
  "was the teacher, the waiting was the lesson, and the next tide will find a better sailor.")),
]

assert len(ENTRIES) == 34
