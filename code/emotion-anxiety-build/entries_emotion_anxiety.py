#!/usr/bin/env python3
"""Seed entries for The Anxiety Emotion Database (emotion-anxiety) and its
Signature edition (emotion-anxiety-signature).

Manon's 2026-10-17 16:15 order: one database per emotion — describe and
simulate the emotion of anxiety and human behavior around it. 34 records,
ladder-ordered 1-34, simple -> compounded -> complex, following the shared
emotion template (description -> first-person simulation -> body signals ->
facial expression -> triggers -> behavior -> healthy expression ->
recognizing it in others -> mixes -> full behavioral simulation).

Public edition: real, fact-checked psychology knowledge about anxiety —
descriptive and educational only. Never diagnoses real people, never labels
any real person, no clinical language, no diagnostic labels, general safe
everyday guidance only.

Signature edition: the same ladder reframed through the Signature lens —
anxiety as the forecast instrument of the human system: the mind's weather
system reading the road ahead. Titles carry " (Signature Edition)", src is
"signature", clearly labeled Signature-made, never presented as authentic
public record.
"""

SIG_TAIL = ("Signature-made record: an original Signature interpretation of "
            "this anxiety knowledge, clearly labeled as Signature-made and "
            "never presented as an authentic public record.")

ENTRIES = [
{
    "key": "anxiety-definition",
    "name": "What Anxiety Is: A Plain-Language Definition",
    "group": "What Anxiety Is",
    "ladder_rank": 1,
    "ladder_tier": "foundations",
    "description": (
        "Anxiety is the emotion that arrives when the future feels uncertain and "
        "the mind starts preparing for what might go wrong. If fear is the alarm "
        "for danger right in front of you, anxiety is the weather forecast: a "
        "forward-looking signal that says \"something ahead might need your "
        "attention.\" It is the mind and body's way of rehearsing the unknown — "
        "scanning possibilities, running mental test runs, and getting the body "
        "ready just in case. When anxiety shows up, several things happen at "
        "once. The body revs up: heart beating a little faster, breath going "
        "shallow, muscles holding tension, stomach doing flips. Attention narrows "
        "and locks onto whatever is uncertain — a test, a conversation, a plane "
        "ride, a medical appointment. And the mind starts its forecasting loop: "
        "what if this happens, then what, then what. Anxiety is not a broken "
        "mind. It is a protective system working ahead of schedule, and like all "
        "protective systems it sometimes over-prepares. Everyone feels it. The "
        "student before the exam, the parent at the airport, the performer backstage "
        "— all are feeling the same forecast machinery. Anxiety becomes useful "
        "when it is read as information: what is uncertain, what can be prepared, "
        "and what is just noise from the forecast machine running too loud. "
        "Understanding anxiety starts here: it is the mind looking ahead, trying "
        "to keep you safe from what has not happened yet."
    ),
    "how_it_works": (
        "Anxiety works as an anticipation-and-preparation loop. The senses or the "
        "memory register something uncertain ahead — a deadline, a message not yet "
        "answered, a strange sound at night — and the mind's forecasting system "
        "starts generating possible futures. The body mobilizes the same machinery "
        "as fear: stress hormones rise, the heart quickens, breathing shallows, "
        "muscles tense for action. But because the threat is not here yet, the "
        "energy has nowhere to go — so it pools as restlessness, stomach churn, "
        "and a mind that will not settle. Attention locks onto the uncertain "
        "thing while everything else fades, and the thinking mind starts rehearsing: "
        "if this goes wrong, I will do that. When the uncertain event resolves — "
        "the test is taken, the news arrives, the plane lands — the loop usually "
        "winds down and the body settles. Anxiety is the forecast, not the weather: "
        "it describes what might come, and like any forecast it can be wrong about "
        "both timing and severity."
    ),
    "key_points": [
        "Anxiety is a forward-looking emotion: it responds to uncertain futures, not present danger.",
        "It has three parts at once: body arousal, narrowed attention, and mental rehearsal of what might happen.",
        "It is a protective system that sometimes over-prepares — the alarm is real, the forecast may be wrong.",
        "Anxiety is universal: students, parents, performers, travelers all run the same machinery.",
        "The useful question is never 'how do I kill this feeling' but 'what is it pointing at'.",
        "It is information about uncertainty, and uncertainty can often be prepared for.",
    ],
    "requirements": [
        "A personal memory of waiting on uncertain news to picture while reading",
        "Willingness to notice what your own body does while waiting",
        "A few quiet minutes — this is the foundation for the whole ladder",
    ],
    "standards": [
        "Anticipatory anxiety framework (Barlow, 2002)",
        "Appraisal theory: uncertainty as the appraisal driving the emotion (Lazarus, 1991)",
        "Fight-or-flight mobilization model (Cannon, 1915)",
        "Basic-emotions and affective forecasting literature",
    ],
    "citations": [
        "Barlow, D. H. Anxiety and Its Disorders. 2nd ed. Guilford Press; 2002.",
        "Lazarus, R. S. Emotion and Adaptation. Oxford University Press; 1991.",
        "Cannon, W. B. Bodily Changes in Pain, Hunger, Fear and Rage. Appleton; 1915.",
        "Loewenstein, G., et al. Risk as Feelings. Psychological Bulletin; 2001.",
    ],
    "sig_lens": (
        "Through the Signature lens, anxiety is the forecast instrument of the "
        "human system — the mind's weather service reading the road ahead. The "
        "Signature reader does not live inside the forecast and does not silence "
        "it either; he reads it the way a captain reads the sky. Every anxious "
        "surge is treated as an early report: name the uncertainty, separate what "
        "can be prepared from what is only noise, and answer with a chosen move. "
        "In the Signature method the forecast serves the traveler — never the "
        "other way around."
    ),
},
{
    "key": "anxiety-family",
    "name": "Anxiety in the Emotion Family",
    "group": "What Anxiety Is",
    "ladder_rank": 2,
    "ladder_tier": "foundations",
    "description": (
        "Anxiety belongs to the emotion family, and knowing its relatives makes "
        "it easier to recognize. Its closest sibling is fear: both are protective "
        "emotions running on the same body machinery — racing heart, fast breath, "
        "tense muscles. The difference is timing. Fear answers a threat that is "
        "here right now; anxiety answers a threat that might be coming. Fear is "
        "the fire alarm; anxiety is the smoke detector with a vivid imagination. "
        "Anxiety also sits downstream of anticipation — the neutral act of looking "
        "ahead. Anticipation plus a sense of threat equals anxiety; anticipation "
        "plus a sense of reward equals excitement, and the two can feel almost "
        "identical in the body. Close cousins include worry (the mental, talky "
        "side of anxiety — the thought loop), nervousness (anxiety's mild, "
        "everyday form), dread (anxiety with a specific dark event attached), and "
        "apprehension (the quiet, low-volume cousin). On the far side of the family "
        "sits calm — not the absence of all feeling but the signal that the "
        "forecast is clear. Psychologists who map emotions, like Plutchik with his "
        "emotion wheel, place anxiety near fear and anticipation, blending into "
        "both. Seeing where anxiety sits in the family does two jobs: it explains "
        "why anxiety feels so much like fear in the body, and it gives the mind "
        "more precise names — because a feeling you can name precisely is a "
        "feeling you can handle better."
    ),
    "how_it_works": (
        "Emotion families work by shared machinery and different triggers. The "
        "threat-protection branch — fear, anxiety, startle — shares one body "
        "engine: adrenaline, quickened pulse, narrowed focus. What differs is the "
        "appraisal, the mind's read of the situation. 'Danger is here' produces "
        "fear; 'danger might be coming' produces anxiety; 'something sudden "
        "happened' produces startle. Meanwhile the anticipation branch — "
        "anticipation, excitement, anxiety — shares the forward-looking machinery: "
        "the mind projecting futures and the body preparing. The valence differs: "
        "positive expectation tilts toward excitement, negative toward anxiety. "
        "This is why people sometimes confuse anxiety with excitement before a big "
        "event — the body is running the same warm-up. Naming the family member "
        "correctly changes the response: fear wants immediate action, anxiety wants "
        "preparation, excitement wants to proceed."
    ),
    "key_points": [
        "Anxiety's closest sibling is fear: same body machinery, different timing.",
        "Fear answers a present threat; anxiety answers an uncertain future.",
        "Worry is anxiety's mental side — the talky thought loop on top of the feeling.",
        "Anxiety and excitement share the same forward-looking machinery; expectation decides which you feel.",
        "Plutchik-style emotion maps place anxiety near fear and anticipation.",
        "Precise naming is practical: the response that fits fear is not the one that fits anxiety.",
    ],
    "requirements": [
        "Willingness to compare two past feelings: one scare, one anxious wait",
        "A mental picture of an emotion wheel or family tree",
        "Curiosity about the exact word for a feeling",
    ],
    "standards": [
        "Plutchik emotion wheel: fear-anticipation neighborhood",
        "Basic emotions framework (Ekman, 2007)",
        "Appraisal theory of emotion differentiation (Lazarus, 1991)",
        "Affective circumplex: arousal by valence mapping",
    ],
    "citations": [
        "Plutchik, R. Emotion: A Psychoevolutionary Synthesis. Harper & Row; 1980.",
        "Ekman, P. Emotions Revealed. 2nd ed. Holt; 2007.",
        "Lazarus, R. S. Emotion and Adaptation. Oxford University Press; 1991.",
        "Russell, J. A. A Circumplex Model of Affect. Journal of Personality and Social Psychology; 1980.",
    ],
    "sig_lens": (
        "Through the Signature lens, the emotion family is the crew of the ship, "
        "and anxiety is the lookout in the crow's nest — scanning the horizon "
        "while fear guards the deck. The Signature reader learns every crew "
        "member by name, because a captain who knows who is shouting gives the "
        "right order. Mistaking the lookout's warning for the deck guard's alarm "
        "is how people prepare for the wrong storm."
    ),
},
{
    "key": "anxiety-volumes",
    "name": "Anxiety at Three Volumes: Mild, Moderate, Intense",
    "group": "What Anxiety Is",
    "ladder_rank": 3,
    "ladder_tier": "foundations",
    "description": (
        "Anxiety is not one fixed state — it is the same emotion at different "
        "volumes, and the volume changes everything about how it feels and what "
        "it does. At mild volume, anxiety is a background hum: butterflies before "
        "a meeting, a light restlessness the night before a trip, checking the "
        "locks twice. The body is slightly alert — a little extra energy, a little "
        "extra attention. Mild anxiety is often useful: it is the nudge that makes "
        "people prepare, double-check, and show up ready. At moderate volume, "
        "anxiety takes the stage: the heart is noticeably faster, the stomach is "
        "tight, thoughts start looping on the uncertain thing, and it gets harder "
        "to concentrate on anything else. This is the level where people describe "
        "feeling 'on edge' — functional, but uncomfortable, and starting to cost "
        "sleep or appetite. At intense volume, anxiety floods the system: the "
        "heart pounds, breathing goes fast and shallow, hands may shake or go "
        "numb, thoughts race or freeze, and the world can feel unreal for a stretch. "
        "Intense anxiety demands the whole stage and can make ordinary tasks feel "
        "impossible for a while. The same protective machinery runs at every "
        "volume — what changes is how much of the system it commandeers. Knowing "
        "the volume matters because the response should match it: mild anxiety "
        "often just needs a plan, moderate anxiety needs active calming and "
        "preparation, and intense anxiety needs the body settled first before any "
        "thinking can work."
    ),
    "how_it_works": (
        "Volume in anxiety is set by two dials: how bad the imagined outcome is, "
        "and how uncertain or uncontrollable it feels. Mild anxiety comes from "
        "small stakes or high controllability — the outcome matters a little, or "
        "the person knows exactly what to do. The body mobilizes a little "
        "arousal, the mind runs a few test scenarios, and the loop closes quickly. "
        "Moderate anxiety comes from real stakes with real uncertainty — the job "
        "interview, the medical test. Arousal climbs, attention narrows hard onto "
        "the threat, and the forecasting loop runs longer because no scenario "
        "resolves the uncertainty. Intense anxiety comes when stakes feel huge "
        "and control feels near zero — the body's alarm fires at full strength, "
        "adrenaline floods, and the thinking brain gets crowded out by the sheer "
        "noise of the signal. This is why intense anxiety can feel like it arrives "
        "from nowhere: the forecast machinery can spin up on a single vivid "
        "thought. Volume is also habit: a system that has run hot for a long time "
        "can learn to default to higher volumes faster."
    ),
    "key_points": [
        "Mild anxiety is a background hum — often useful, the nudge to prepare.",
        "Moderate anxiety takes the stage — uncomfortable, harder to concentrate, costs sleep.",
        "Intense anxiety floods the system — body and mind both commandeered.",
        "Volume is set by two dials: imagined stakes and felt control.",
        "The same machinery runs at every volume; only the share of the system changes.",
        "Match the response to the volume: plan, calm-and-prepare, or settle-the-body-first.",
    ],
    "requirements": [
        "Three memories: a mild worry, a real anxious stretch, and the worst wave",
        "Honesty about which volume shows up most often",
        "No judgment — volume is information, not a grade",
    ],
    "standards": [
        "Yerkes-Dodson arousal-performance curve (1908)",
        "Subjective Units of Distress scaling (Wolpe, 1969)",
        "Barlow's triple-vulnerability framing of anxiety intensity",
        "Appraisal-stakes model (Lazarus, 1991)",
    ],
    "citations": [
        "Yerkes, R. M., & Dodson, J. D. The Relation of Strength of Stimulus to Rapidity of Habit-Formation. Journal of Comparative Neurology; 1908.",
        "Wolpe, J. The Practice of Behavior Therapy. Pergamon; 1969.",
        "Barlow, D. H. Anxiety and Its Disorders. 2nd ed. Guilford Press; 2002.",
    ],
    "sig_lens": (
        "Through the Signature lens, the three volumes are three readings on the "
        "same instrument. Mild anxiety is a whisper from the lookout — log it and "
        "prepare. Moderate anxiety is a raised voice — stop, calm the deck, then "
        "plan. Intense anxiety is the bell hammering — the Signature reader's "
        "first job is not thinking but settling the body, because no captain "
        "charts a course while the ship is shaking. Read the volume, then answer "
        "at its level."
    ),
},
{
    "key": "anxiety-myths",
    "name": "Myths and Misunderstandings About Anxiety",
    "group": "What Anxiety Is",
    "ladder_rank": 4,
    "ladder_tier": "foundations",
    "description": (
        "Anxiety collects myths the way old houses collect dust, and the myths "
        "make the feeling harder to handle than it needs to be. Myth one: anxiety "
        "means something is wrong with you. In truth anxiety is standard human "
        "equipment — every nervous system ships with a forecast function, and "
        "feeling it is as normal as feeling hunger. Myth two: calm people never "
        "feel anxious. They do; they have usually just practiced reading the "
        "signal instead of fighting it. Myth three: anxiety is always bad and "
        "should be eliminated. Mild anxiety improves performance — it is the "
        "reason people rehearse, pack carefully, and arrive early. The goal was "
        "never zero anxiety; it is anxiety at a volume that helps instead of "
        "hurts. Myth four: if you feel anxious, the danger must be real. The "
        "forecast can be wrong — vividly, confidently wrong. Feeling strongly "
        "about an outcome does not make the outcome likely. Myth five: thinking "
        "your way out always works. At high volume the thinking brain is crowded "
        "out, which is why body-first calming (slow breath, loosened muscles) "
        "often works when arguing with the thoughts does not. Myth six: talking "
        "about anxiety makes it worse. Done well, naming and describing it "
        "usually shrinks it — the vague dread becomes a specific, handleable "
        "thing. Clearing the myths does not remove anxiety, but it removes the "
        "second layer of suffering: the anxiety about having anxiety."
    ),
    "how_it_works": (
        "Myths about anxiety work by adding a second appraisal on top of the "
        "first. The first appraisal is the emotion itself: 'the future is "
        "uncertain.' The myth adds a second one: 'and feeling this means I am "
        "broken / weak / in real danger.' That second appraisal feeds back into "
        "the forecasting loop as new threat material — now the person is anxious "
        "about being anxious, and the loop tightens. This is why myth-busting is "
        "practical, not just philosophical: removing the false second appraisal "
        "cuts the fuel supply to the loop. Accurate beliefs about anxiety act "
        "like a pressure valve. 'This is my forecast system running hot' is a "
        "neutral, true description that lets the person act on the feeling without "
        "being ruled by it. The myths persist because anxiety feels so physical "
        "and so certain — the body reports danger with total conviction, and the "
        "mind trusts the body. Education breaks the spell by teaching the "
        "difference between a loud signal and a true one."
    ),
    "key_points": [
        "Anxiety is standard equipment, not a personal defect.",
        "Calm people feel anxiety too — they have practiced reading it.",
        "Mild anxiety helps; the goal is useful volume, not zero feeling.",
        "A loud forecast is not a true forecast — feeling is not evidence.",
        "At high volume, body-first calming beats arguing with thoughts.",
        "Naming anxiety precisely usually shrinks it instead of feeding it.",
    ],
    "requirements": [
        "One anxiety myth you have believed, named honestly",
        "Willingness to test a belief against how anxiety actually works",
        "A notebook line for the replacement belief",
    ],
    "standards": [
        "Psychoeducation model in anxiety literature (Barlow, 2002)",
        "Cognitive appraisal and reappraisal (Lazarus; Gross, 2002)",
        "Metacognitive beliefs about emotion (Wells, 2009)",
    ],
    "citations": [
        "Barlow, D. H. Anxiety and Its Disorders. 2nd ed. Guilford Press; 2002.",
        "Gross, J. J. Emotion Regulation: Affective, Cognitive, and Social Consequences. Psychophysiology; 2002.",
        "Wells, A. Metacognitive Therapy for Anxiety and Depression. Guilford Press; 2009.",
    ],
    "sig_lens": (
        "Through the Signature lens, myths are fog on the lookout's lens — they "
        "do not change the horizon, they only corrupt the reading. The Signature "
        "reader wipes the lens first: anxiety is equipment, not identity; a loud "
        "signal, not a true one; a forecast, not a verdict. With the lens clean, "
        "the reading is honest, and an honest reading is always answerable."
    ),
},
{
    "key": "anxiety-firstperson",
    "name": "Inside the Feeling: Anxiety in First Person",
    "group": "How Anxiety Feels",
    "ladder_rank": 5,
    "ladder_tier": "foundations",
    "description": (
        "From the inside, anxiety does not announce itself as an emotion — it "
        "announces itself as a state of the world. The room feels slightly too "
        "bright. Time feels slightly too fast. There is a tightness low in the "
        "chest, like a hand resting there, and the breath will not go all the way "
        "down no matter how deliberately you pull it in. The stomach is busy — "
        "churning, hollow, or knotted — and the hands want something to do: tap, "
        "fidget, scroll, grip. Thinking becomes a corridor with one door at the "
        "end: the uncertain thing. You try to think about dinner and the mind "
        "slides back to the test, the message, the appointment, as if the corridor "
        "is tilted. Scenarios play on repeat — the bad version, then the worse "
        "version, then the bad version again with new details. The body feels "
        "simultaneously tired and wired: exhausted from the loop, too charged to "
        "rest. Sounds are sharper. Small delays feel enormous — the elevator "
        "taking ten seconds feels like a personal insult. And underneath it all "
        "runs a single sentence the mind keeps whispering: something is not "
        "settled yet. That is the whole of it. Anxiety from the inside is the "
        "experience of living one step ahead of the present, in a future that has "
        "not been decided, with a body braced for all of its versions at once."
    ),
    "how_it_works": (
        "The first-person texture of anxiety is produced by the forecasting loop "
        "running in high gear. Interoception — the brain's read of the body's "
        "internal state — picks up the arousal: heart, breath, gut. Because "
        "humans interpret bodily arousal through context, and the context here is "
        "uncertainty, the arousal gets labeled as dread rather than, say, "
        "excitement. Meanwhile the mind's simulation engine generates futures and "
        "the attention system keeps dragging focus back to them — that tilted-"
        "corridor feeling is attention being repeatedly recaptured by the threat "
        "simulation. The tired-but-wired sensation comes from sustained arousal "
        "with no discharge: the body is mobilized for action, but there is nothing "
        "to act on yet, so the energy pools as restlessness. The sharpened senses "
        "are threat monitoring — the system turning up the gain on every channel. "
        "None of this is chosen. It is the forecast machinery doing exactly what "
        "it evolved to do, in a modern world where most threats are appointments "
        "and inboxes rather than predators."
    ),
    "key_points": [
        "From inside, anxiety feels like a property of the world, not a feeling in the mind.",
        "The tilted corridor: attention keeps sliding back to the uncertain thing.",
        "Tired-but-wired: mobilized body with nowhere to discharge the energy.",
        "Scenarios replay with escalating detail — the simulation engine at full speed.",
        "Senses sharpen; small delays and noises feel enormous.",
        "All of it is the forecast machinery working — misplaced, not broken.",
    ],
    "requirements": [
        "A quiet minute and one real memory of waiting anxiously",
        "Attention to body sensations as you read",
        "No fixing — just noticing, for this record",
    ],
    "standards": [
        "Interoception and emotion labeling (Schachter & Singer, 1962)",
        "Attentional bias in anxiety (MacLeod et al.)",
        "Mental simulation and affective forecasting (Gilbert & Wilson, 2007)",
    ],
    "citations": [
        "Schachter, S., & Singer, J. E. Cognitive, Social, and Physiological Determinants of Emotional State. Psychological Review; 1962.",
        "Gilbert, D. T., & Wilson, T. D. Prospection: Experiencing the Future. Science; 2007.",
        "Barlow, D. H. Anxiety and Its Disorders. 2nd ed. Guilford Press; 2002.",
    ],
    "sig_lens": (
        "Through the Signature lens, the first-person passage is the lookout's "
        "log — a faithful record of what the watch feels like from the crow's "
        "nest. The Signature reader keeps such logs, because a captain who knows "
        "exactly how the warning feels can tell the difference between weather "
        "and weather-report. Feel it fully, log it honestly, then climb down and "
        "decide on deck."
    ),
},
{
    "key": "anxiety-arc",
    "name": "The Arc of Anxiety: Onset, Peak, Fading, Aftershock",
    "group": "How Anxiety Feels",
    "ladder_rank": 6,
    "ladder_tier": "foundations",
    "description": (
        "Anxiety has a shape in time, and knowing the shape is half the battle. "
        "Onset: it rarely starts at full volume. There is a first flicker — a "
        "thought about the upcoming thing, a calendar glance, a message tone that "
        "reads wrong. The body answers before the mind has finished the sentence: "
        "a small tightening, a shallower breath. If the uncertain thing stays "
        "uncertain, the loop feeds itself and the feeling climbs. Rise: the "
        "forecasting engine is fully engaged now. Scenarios multiply. The body "
        "stays mobilized — heart up, muscles tense, stomach active. Attention is "
        "captured; ordinary pleasures feel flat because the system has decided "
        "they are not relevant to survival. Peak: the crest. This is the worst it "
        "gets, and it feels endless while it lasts — but it is not endless. Peaks "
        "are expensive for the body to maintain, so they always break. Fading: "
        "the uncertain thing resolves, or the system simply tires. The breath "
        "deepens on its own. The shoulders drop an inch. Thoughts slow and the "
        "corridor widens — other topics become thinkable again. Aftershock: the "
        "echo. Hours later a small reminder can re-trigger a brief flicker, or "
        "the body stays tender — startling easier, tiring faster — while it "
        "recovers. The aftershock is not a relapse; it is the system cooling "
        "down. People who fear the peak often try to prevent the onset entirely, "
        "but the arc shows a kinder truth: anxiety is a wave, and every wave "
        "breaks."
    ),
    "how_it_works": (
        "The arc follows the arousal curve. Onset is appraisal: the mind flags "
        "uncertainty and the body releases the first pulse of arousal chemicals. "
        "Rise is positive feedback: arousal makes the threat feel more serious, "
        "which raises arousal further — the loop climbs because each circuit adds "
        "fuel. Peak is the ceiling of the feedback loop: the body cannot sustain "
        "maximum mobilization indefinitely, and the mind's scenario generator "
        "starts repeating itself, which reduces novelty and therefore alarm. "
        "Fading begins when the appraisal changes — the event resolves, new "
        "information arrives, or exhaustion simply caps the loop — and the "
        "parasympathetic system starts the long work of standing the body down. "
        "Aftershock is sensitization: recently fired threat circuits stay warm, "
        "so smaller triggers can briefly re-fire them while the system returns to "
        "baseline. Knowing the arc matters because each phase has its own best "
        "response: early phases reward preparation, the peak rewards riding it "
        "out with the body, and the fade rewards rest rather than analysis."
    ),
    "key_points": [
        "Anxiety follows an arc: onset, rise, peak, fading, aftershock.",
        "The rise is a feedback loop — arousal feeding appraisal feeding arousal.",
        "Peaks are expensive for the body; they always break.",
        "Fading begins when the appraisal changes or the system tires.",
        "Aftershock is the warm circuit cooling — an echo, not a relapse.",
        "Each phase has its own best response; match the move to the phase.",
    ],
    "requirements": [
        "One past anxious episode to trace along the arc",
        "A sense of where your own peaks usually break",
        "Patience — the arc cannot be rushed, only ridden",
    ],
    "standards": [
        "Arousal feedback models (Barlow, 2002)",
        "Autonomic recovery and parasympathetic rebound",
        "Sensitization and recovery curves in threat circuitry",
    ],
    "citations": [
        "Barlow, D. H. Anxiety and Its Disorders. 2nd ed. Guilford Press; 2002.",
        "Craske, M. G., et al. Anxiety Disorders. Nature Reviews Disease Primers; 2017.",
        "LeDoux, J. The Emotional Brain. Simon & Schuster; 1996.",
    ],
    "sig_lens": (
        "Through the Signature lens, the arc is the storm's chart — onset to "
        "aftershock, drawn from the crow's nest over many voyages. The Signature "
        "reader studies the chart until he trusts it: no wave in history has "
        "failed to break. Preparation belongs to the onset, endurance to the "
        "peak, and rest to the fading — the right move at the wrong phase is the "
        "wrong move."
    ),
},
{
    "key": "anxiety-low-high",
    "name": "Anxiety at Low and High Intensity: Two Lived Snapshots",
    "group": "How Anxiety Feels",
    "ladder_rank": 7,
    "ladder_tier": "foundations",
    "description": (
        "Low anxiety: It is Tuesday morning and there is a dentist appointment "
        "Thursday. You think about it while making coffee — a brief flicker, a "
        "small tightening in the stomach, one mental rehearsal of the waiting "
        "room. Then the email loads and the thought is gone. It returns twice "
        "more that day, each time lighter, each time easier to set aside. Your "
        "hands are steady. You sleep fine. The anxiety is doing its job: it has "
        "put 'Thursday' on the mental checklist, and you will probably leave "
        "early to be on time. It costs you maybe ninety seconds of attention "
        "total, and it buys you preparedness. This is anxiety as a good "
        "assistant — quiet, brief, useful, gone when the task is handled. "
        "High anxiety: It is the night before the results come out — exam, "
        "medical, legal, the kind that rearranges a life. The flicker from the "
        "morning never left; it grew roots. Your chest feels compressed, as if "
        "the air in the room is thinner. Thoughts do not visit the uncertain "
        "thing — they live there now, running the same three scenarios on a "
        "loop with rising dread each pass. Your hands shake slightly when you "
        "hold your phone. Food sits untouched; the stomach has closed for "
        "business. You try to watch something and realize ten minutes passed "
        "without you seeing any of it. Sleep comes in shallow snatches between "
        "checks of the clock. This is the same assistant, but now it has taken "
        "over the whole office — every channel, every sense, every thought, all "
        "forecasting. The two snapshots are not two different emotions. They are "
        "the same machinery at different volumes, and the difference between "
        "them is why volume literacy matters: low anxiety needs a checklist, "
        "high anxiety needs the body settled before any checklist can work."
    ),
    "how_it_works": (
        "The two snapshots differ in how much of the system the forecasting "
        "loop has captured. At low intensity, the appraisal ('Thursday might be "
        "unpleasant') generates a small arousal pulse and a brief simulation. "
        "Attention is captured for seconds, then released — the prefrontal "
        "systems stay in charge and the loop closes. The feeling registers as "
        "information. At high intensity, the appraisal ('tomorrow changes "
        "everything') generates sustained arousal, and the feedback loop takes "
        "over: arousal amplifies the appraisal's seriousness, which amplifies "
        "arousal. Attention is captured continuously — the tilted corridor "
        "becomes a locked room. The body's stress systems stay mobilized for "
        "hours, suppressing appetite, fragmenting sleep, and crowding out working "
        "memory, which is why concentration collapses. Same loop, different "
        "gain. This is also why high anxiety cannot simply be reasoned away in "
        "the moment: the reasoning hardware is the part most crowded out by the "
        "signal."
    ),
    "key_points": [
        "Low anxiety is a good assistant: brief, quiet, useful, gone when handled.",
        "High anxiety is the assistant taking over the whole office.",
        "The difference is system capture — how much of attention and body the loop owns.",
        "Low anxiety costs seconds of attention; high anxiety costs sleep, appetite, focus.",
        "Same machinery, different gain — not two different emotions.",
        "Match the response to the snapshot: checklist for low, body-first for high.",
    ],
    "requirements": [
        "Both snapshots pictured honestly — no minimizing, no catastrophizing",
        "A personal example of each volume",
        "Recognition that the high snapshot always ends",
    ],
    "standards": [
        "Arousal-performance curve (Yerkes & Dodson, 1908)",
        "Attentional capture in anxiety (Barlow, 2002)",
        "Working memory under threat load",
    ],
    "citations": [
        "Yerkes, R. M., & Dodson, J. D. Journal of Comparative Neurology; 1908.",
        "Barlow, D. H. Anxiety and Its Disorders. 2nd ed. Guilford Press; 2002.",
        "Eysenck, M. W., et al. Anxiety and Cognitive Performance: Attentional Control Theory. Emotion; 2007.",
    ],
    "sig_lens": (
        "Through the Signature lens, the two snapshots are the same sea at "
        "different swells — a ripple and a storm, both water. The Signature "
        "reader learns to read swell height at a glance, because the ripple "
        "wants a checklist and the storm wants ballast. Misreading the swell is "
        "how captains founder: checklists do not calm storms, and ballast is "
        "wasted on ripples."
    ),
},
{
    "key": "anxiety-irritation-blend",
    "name": "When Anxiety Meets Irritation: The Most Common Blend",
    "group": "How Anxiety Feels",
    "ladder_rank": 8,
    "ladder_tier": "foundations",
    "description": (
        "Anxiety rarely travels alone, and its most frequent traveling companion "
        "is irritation. The blend has a recognizable signature. It starts as "
        "pure anxiety — the uncertain thing looming, the stomach tight, the "
        "scenarios looping. Then something small goes wrong: a slow driver, a "
        "dropped pen, a message that says 'we need to talk' with no context. "
        "And the feeling changes temperature. The dread sharpens into edge. The "
        "restlessness turns outward — suddenly everyone is too slow, too loud, "
        "too much. The jaw that was merely tense starts to ache from clenching. "
        "Words come out shorter than intended, with a snap at the end. From the "
        "inside, the blend feels like this: part of you is braced for the future "
        "and part of you is furious that the present will not cooperate. The "
        "irritation is not really about the slow driver — it is the anxiety's "
        "trapped energy looking for somewhere to discharge. The body is mobilized "
        "for action and there is no action to take about the uncertain future, "
        "so the mobilization leaks into the nearest available target: the "
        "present moment's small frictions. Recognizing the blend matters because "
        "the two halves want different things. The anxiety wants preparation and "
        "reassurance; the irritation wants the obstacle removed. Treating the "
        "irritation as the real problem — snapping at people, slamming things — "
        "feeds the anxiety instead of releasing it. The skill is to hear the "
        "blend for what it is: one feeling wearing two faces, both pointing back "
        "to the same uncertain future."
    ),
    "how_it_works": (
        "The blend forms because anxiety and irritation share an engine: "
        "arousal with blocked goals. Anxiety is arousal aimed at an uncertain "
        "future; irritation is arousal aimed at a blocked present. When the "
        "anxious system is already running hot, its baseline arousal is high, "
        "so small present-moment frictions — which would normally register as "
        "mild annoyance — arrive on top of an already-mobilized body and read as "
        "much bigger. The appraisal system, already in threat mode from the "
        "anxiety, interprets the friction as further evidence that things are "
        "going wrong. Meanwhile the trapped mobilization energy seeks discharge, "
        "and irritation provides a target: unlike the abstract future, the slow "
        "driver is right there. This is why anxious people so often describe "
        "themselves as 'snappy' — the snap is misdirected preparation energy. "
        "The blend resolves fastest when the anxiety half is addressed: once "
        "the uncertain future has a plan, the arousal drops, and the irritation "
        "evaporates with it — revealing that it was never really about the "
        "traffic."
    ),
    "key_points": [
        "Anxiety's most common partner is irritation — the blend is everywhere.",
        "The irritation is usually misdirected: trapped preparation energy seeking a target.",
        "Small frictions feel huge because they land on an already-mobilized body.",
        "The two halves want different things: preparation vs obstacle removal.",
        "Snapping at the present feeds the anxiety instead of releasing it.",
        "Address the anxiety half and the irritation often evaporates on its own.",
    ],
    "requirements": [
        "One memory of being snappy while worried about something else",
        "Honesty about what the snap was really about",
        "Willingness to separate the two faces of the blend",
    ],
    "standards": [
        "Emotion blend theory (Plutchik, 1980)",
        "Frustration-aggression and arousal transfer (Zillmann)",
        "Appraisal interaction in mixed emotions",
    ],
    "citations": [
        "Plutchik, R. Emotion: A Psychoevolutionary Synthesis. Harper & Row; 1980.",
        "Zillmann, D. Excitation Transfer in Communication-Mediated Aggressive Behavior. Journal of Experimental Social Psychology; 1971.",
        "Barlow, D. H. Anxiety and Its Disorders. 2nd ed. Guilford Press; 2002.",
    ],
    "sig_lens": (
        "Through the Signature lens, the anxiety-irritation blend is the lookout "
        "shouting at the deck crew — the warning meant for the horizon landing "
        "on the nearest sailor. The Signature reader catches the misdirection in "
        "real time: the snap is information about the forecaster, not the "
        "forecast. He thanks the lookout, turns back to the horizon, and leaves "
        "the crew in peace."
    ),
},
{
    "key": "anxiety-day",
    "name": "A Day in the Life: Anxiety Running Through an Ordinary Day",
    "group": "How Anxiety Feels",
    "ladder_rank": 9,
    "ladder_tier": "foundations",
    "description": (
        "Morning: the alarm goes off and before the eyes are fully open the mind "
        "is already at the 2 p.m. meeting. The body answers the thought with a "
        "small surge — stomach tightens, breath shortens. Coffee tastes like "
        "nothing; the system has decided flavor is not relevant today. "
        "Mid-morning: the inbox has a message from the boss with no subject line. "
        "The forecasting engine ignites. Scenarios bloom: criticism, reassignment, "
        "the meeting going badly. Hands hover over the keyboard, typing and "
        "deleting. Every notification sound is a small electric shock. "
        "Lunch: food is mechanical. Colleagues are laughing about something and "
        "it sounds far away, like a radio in another room — attention is "
        "elsewhere, locked on 2 p.m. Someone asks if you are okay and you say "
        "'fine, just tired,' which is true in the way shadows are true. "
        "Afternoon: the meeting happens. It is fine. Utterly, boringly fine. "
        "The boss wanted to discuss the project timeline. All morning's scenarios "
        "evaporate in four minutes of ordinary conversation. The body does not "
        "get the memo immediately — the shoulders stay up for another hour, the "
        "stomach stays knotted through the commute. Evening: the fading. Dinner "
        "actually tastes like dinner. A show is actually funny. The aftershock "
        "visits once — a flicker while brushing teeth, 'what about tomorrow's "
        "deadline' — but it is smaller now, and it passes. In bed, the honest "
        "accounting: the anxiety cost about six hours of presence and bought "
        "about four minutes of preparation. That is the ordinary day with "
        "anxiety — a tax paid in attention, levied by a forecast that was mostly "
        "wrong, on a day that turned out fine."
    ),
    "how_it_works": (
        "The day vignette shows the forecasting loop running as a background "
        "process all day. Each phase of the day supplies fresh appraisal "
        "material — the calendar, the subject-less email — and each appraisal "
        "re-fires the arousal pulse, which is why the feeling persists for "
        "hours rather than minutes. Attention capture explains the flat coffee, "
        "the distant laughter, the unwatched show: the attention system has "
        "limited bandwidth, and the threat simulation is consuming most of it. "
        "The meeting's four fine minutes demonstrate the forecast-error at the "
        "heart of anxiety: the simulation engine generates vivid futures, but "
        "vividness is not probability. The slow bodily fade after the good news "
        "shows the arousal curve lagging behind the appraisal — the body needs "
        "time to stand down even after the mind knows it is safe. And the "
        "evening flicker is the warm circuit: recently fired threat pathways "
        "re-fire easily. The day is ordinary because this is what anxiety "
        "usually is — not a crisis, but a steady tax on presence."
    ),
    "key_points": [
        "A full anxious day is usually a tax on presence, not a crisis.",
        "Each part of the day supplies fresh appraisal material that re-fires the loop.",
        "Attention capture explains why food, laughter, and shows go flat.",
        "The forecast is vivid but vividness is not probability.",
        "The body stands down slower than the mind — the fade lags the good news.",
        "Evening flickers are warm circuits cooling, not new emergencies.",
    ],
    "requirements": [
        "One of your own ordinary anxious days to compare",
        "An honest ledger: what the anxiety cost vs what it bought",
        "Compassion for the version of you living that day",
    ],
    "standards": [
        "Ecological momentary assessment of anxiety in daily life",
        "Attentional resource models (Eysenck et al., 2007)",
        "Affective forecasting error (Gilbert & Wilson, 2007)",
    ],
    "citations": [
        "Gilbert, D. T., & Wilson, T. D. Prospection: Experiencing the Future. Science; 2007.",
        "Eysenck, M. W., et al. Anxiety and Cognitive Performance: Attentional Control Theory. Emotion; 2007.",
        "Barlow, D. H. Anxiety and Its Disorders. 2nd ed. Guilford Press; 2002.",
    ],
    "sig_lens": (
        "Through the Signature lens, the ordinary anxious day is logged like a "
        "ship's day in rough-but-manageable seas — every watch noted, every "
        "false alarm counted. The Signature reader keeps the ledger honestly: "
        "six hours of presence paid, four minutes of preparation bought. The "
        "ledger is what turns a bad day into navigation data for the next "
        "voyage."
    ),
},
{
    "key": "anxiety-body",
    "name": "What Happens in the Body: The Physical Signals of Anxiety",
    "group": "Body Signals",
    "ladder_rank": 10,
    "ladder_tier": "compounded",
    "description": (
        "Anxiety is a full-body event, and the body keeps a detailed log. "
        "Heart: it beats faster and often harder — the classic pounding chest. "
        "Some people feel it as a flutter or a skipped beat that then triggers "
        "more anxiety about the heart itself. Breath: it goes shallow and quick, "
        "staying high in the chest instead of dropping into the belly. At high "
        "volume this can tip into over-breathing, which brings tingling and "
        "dizziness — frightening, but a known mechanical effect of the breathing "
        "pattern. Muscles: they tense and stay tense — jaw, shoulders, neck, "
        "lower back. Long anxious stretches end with the peculiar soreness of a "
        "workout you never did. Hands may tremble; legs may feel weak or "
        "jittery, as if the floor is slightly unreliable. Stomach and gut: the "
        "digestive system is the anxiety bulletin board — nausea, churning, "
        "knots, sudden hunger or sudden loss of appetite, the urgent need for a "
        "bathroom before the big event. Skin: flushing or sudden pallor, sweating "
        "(palms, forehead, underarms), goosebumps, or a crawling prickly "
        "sensation. Mouth goes dry; swallowing feels deliberate. Energy: the "
        "signature tired-but-wired state — exhausted from sustained arousal, too "
        "charged to rest. None of these signals mean the body is malfunctioning. "
        "They are the threat-preparation machinery doing its ancient job: more "
        "blood to the muscles, more oxygen in the lungs, digestion paused, senses "
        "up. The machinery cannot tell an inbox from a predator — it only knows "
        "the appraisal said 'uncertain future,' and it prepares accordingly."
    ),
    "how_it_works": (
        "The body signals of anxiety are orchestrated by the autonomic nervous "
        "system's mobilization branch. The appraisal of uncertain threat "
        "activates the sympathetic system: adrenaline and related chemicals "
        "surge, heart rate and contractility rise, breathing quickens to load "
        "oxygen, blood is routed toward large muscles and away from digestion "
        "and skin (hence the gut effects and pallor or flushing as vessels "
        "shift). Muscle tension is preparation for action — the body literally "
        "bracing. Sweating cools a body expecting exertion. The dry mouth comes "
        "from reduced saliva as digestion stands down. Trembling is the visible "
        "edge of muscles held at high readiness. Because the trigger is a "
        "forecast rather than a present event, the mobilization has no natural "
        "discharge — there is nothing to run from or fight yet — so the arousal "
        "pools and sustains, which is why anxious body signals can last for "
        "hours. When the appraisal resolves, the parasympathetic system reverses "
        "the whole pattern: heart slows, breath deepens, digestion resumes, "
        "muscles release — often with a wave of tiredness as the bill comes due."
    ),
    "key_points": [
        "Heart, breath, muscles, gut, skin, and energy all log the anxiety signal.",
        "Every signal is threat-preparation machinery: fuel to muscles, oxygen to lungs, digestion paused.",
        "The machinery cannot tell an inbox from a predator — it follows the appraisal.",
        "Sustained signals come from mobilization with no discharge — energy pools instead of releasing.",
        "Tired-but-wired is the signature state: exhausted and charged at once.",
        "Resolution reverses the pattern — the body stands down, often with a wave of tiredness.",
    ],
    "requirements": [
        "A body scan: which three signals show up first in your own anxiety",
        "Permission to treat the signals as information, not malfunction",
        "A glass of water — dry mouth is real",
    ],
    "standards": [
        "Autonomic mobilization model (Cannon, 1915; Barlow, 2002)",
        "Interoceptive awareness literature",
        "Respiratory physiology of over-breathing effects",
    ],
    "citations": [
        "Cannon, W. B. Bodily Changes in Pain, Hunger, Fear and Rage. Appleton; 1915.",
        "Barlow, D. H. Anxiety and Its Disorders. 2nd ed. Guilford Press; 2002.",
        "Craske, M. G., et al. Anxiety Disorders. Nature Reviews Disease Primers; 2017.",
    ],
    "sig_lens": (
        "Through the Signature lens, the body is the ship and every signal is a "
        "gauge on the bridge — heart the engine tachometer, breath the bellows, "
        "gut the ballast indicator, skin the hull thermometer. The Signature "
        "reader learns his gauges the way a captain learns his ship: not to "
        "fear the needles, but to read them. A gauge is never the storm; it is "
        "the report of one."
    ),
},
{
    "key": "anxiety-posture",
    "name": "Posture and Movement: How the Body Carries Anxiety",
    "group": "Body Signals",
    "ladder_rank": 11,
    "ladder_tier": "compounded",
    "description": (
        "Anxiety has a posture — you can read it across a room. The shoulders "
        "rise and roll forward, as if bracing for impact. The head tips slightly "
        "down and forward, the chin tucking — the body making itself smaller. "
        "Arms cross or hands clasp, fidget, or find pockets; the hands especially "
        "betray anxiety, with tapping fingers, pen-clicking, nail-picking, or a "
        "phone gripped like a lifeline. The jaw sets. The brow stays faintly "
        "knit even at rest. Movement under anxiety has two modes, and people "
        "tend toward one. The pacers: restless locomotion — walking the hallway, "
        "bouncing the leg, shifting weight foot to foot, unable to be still "
        "because the mobilized body demands motion. The freezers: going statue-"
        "still — perched on the edge of the chair, movements small and careful, "
        "as if any sudden motion might trigger the uncertain thing. Both are the "
        "same arousal with different discharge strategies. Gait changes too: "
        "anxious walking is often quicker with shorter steps, eyes scanning "
        "rather than settling — the threat-monitoring system running the legs. "
        "Voice posture matters as well: the breath held high in the chest "
        "shortens the voice and hurries it. The good news is the channel runs "
        "both ways. Deliberately dropping the shoulders, unclenching the jaw, "
        "planting both feet, and slowing the exhale sends the all-clear back up "
        "the same wiring — the body can talk the mind down as surely as the "
        "mind winds the body up."
    ),
    "how_it_works": (
        "Anxious posture is the musculoskeletal half of threat preparation. "
        "Raised, forward-rolled shoulders and tucked chin are protective "
        "configurations — guarding the neck and vital areas, the body's ancient "
        "bracing pattern. Fidgeting and pacing are partial discharges of "
        "mobilization energy: the sympathetic system has prepared the muscles "
        "for action, and small repetitive movements bleed off some of that "
        "readiness without committing to a full action the situation does not "
        "allow. Freezing is the alternative ancient program — stillness as "
        "camouflage and assessment, the body holding position while the threat "
        "is evaluated. Short, quick steps with scanning eyes are the locomotor "
        "expression of threat monitoring. The two-way channel works through "
        "proprioceptive feedback: the brain continuously reads the body's "
        "posture as evidence about safety. A braced body is read as 'danger,' "
        "sustaining the appraisal; a deliberately settled body is read as "
        "'safe,' which is why posture interventions can unwind the loop from "
        "the bottom up."
    ),
    "key_points": [
        "Anxious posture: raised shoulders, tucked chin, crossed arms, busy hands.",
        "Two movement modes: pacing (discharge) vs freezing (assessment) — same arousal.",
        "Anxious gait is quicker, shorter-stepped, with scanning eyes.",
        "The channel runs both ways: settling the body talks the mind down.",
        "Jaw, brow, and hands are the most reliable tells.",
        "Posture is the body voting on safety — change the vote deliberately.",
    ],
    "requirements": [
        "A mirror or a window reflection for one honest look",
        "Noticing your own default: pacer or freezer",
        "One deliberate shoulder-drop to feel the channel work",
    ],
    "standards": [
        "Embodied emotion and proprioceptive feedback literature",
        "Protective postural configurations in threat response",
        "Psychomotor agitation vs inhibition patterns",
    ],
    "citations": [
        "Ekman, P. Emotions Revealed. 2nd ed. Holt; 2007.",
        "Barlow, D. H. Anxiety and Its Disorders. 2nd ed. Guilford Press; 2002.",
        "Riskind, J. H., & Gotay, C. C. Physical Posture: Could It Have Regulatory or Feedback Effects on Motivation and Emotion? Motivation and Emotion; 1982.",
    ],
    "sig_lens": (
        "Through the Signature lens, posture is the ship's trim — how she sits "
        "in the water tells the captain her state before a single gauge is "
        "read. The Signature reader trims deliberately: shoulders down, jaw "
        "unclenched, feet planted. A well-trimmed ship does not fear the swell; "
        "she meets it. The body is ballast the captain can shift at will."
    ),
},
{
    "key": "anxiety-sleep",
    "name": "Sleep, Appetite, and Energy Under Anxiety",
    "group": "Body Signals",
    "ladder_rank": 12,
    "ladder_tier": "compounded",
    "description": (
        "Anxiety leaves footprints across the three foundations of the day: "
        "sleep, appetite, and energy. Sleep: anxiety is the enemy of the off-"
        "switch. The mind that has rehearsed futures all day does not stop at "
        "bedtime — it holds a final review session the moment the lights go out. "
        "Falling asleep takes longer because arousal and sleep are opposites; "
        "the body cannot be both mobilized and drifting off. Sleep, when it "
        "comes, is lighter — more waking, more vivid dreaming, the threat "
        "simulation continuing in the dream theater. Mornings arrive unrefreshed, "
        "which lowers the next day's resilience, which raises the next night's "
        "anxiety — the classic loop. Appetite: the gut is anxiety's bulletin "
        "board, so meals get strange. Some people lose all interest in food — "
        "the mobilized body has paused digestion, and eating feels wrong. Others "
        "eat faster, or crave quick energy, or graze all day without tasting "
        "anything — the system seeking fuel for a marathon it is not actually "
        "running. Nausea before big events is so common it is practically a "
        "scheduled appointment. Energy: the paradox budget. Anxiety spends "
        "energy at a furious rate — sustained muscle tension, racing thoughts, "
        "broken sleep — while simultaneously blocking recovery. The result is "
        "the tired-but-wired account: overdrawn and overcharged at the same "
        "time. Small tasks feel heavy because the budget is already spent on "
        "forecasting. The footprint is practical information: when sleep, "
        "appetite, and energy all shift together, the common cause is usually "
        "the anxiety loop, and settling the loop often settles all three."
    ),
    "how_it_works": (
        "The footprint follows from sustained mobilization. Sleep onset requires "
        "the arousal system to stand down — core temperature dropping, heart "
        "rate slowing, muscle tone releasing — and an anxious system resists all "
        "three, which is why the mind races at lights-out and sleep is shallow. "
        "Appetite shifts because the sympathetic branch suppresses digestive "
        "activity (blood routed to muscles) while the gut's own dense nerve "
        "network — highly sensitive to stress chemistry — generates nausea, "
        "churn, and urgency. Craving quick energy is the body requesting fuel "
        "for the exertion it believes is coming. The energy paradox is "
        "accounting: anxiety is metabolically expensive (tension, vigilance, "
        "cognitive rehearsal all burn fuel) while impairing the recovery "
        "systems (sleep fragmentation, poor nutrition), so net energy goes "
        "negative even on days with no physical exertion. The loop closes when "
        "depleted sleep and fuel lower the threshold for the next day's "
        "appraisals — a tired brain forecasts darker futures."
    ),
    "key_points": [
        "Anxiety fights the off-switch: longer to fall asleep, lighter sleep, vivid dreams.",
        "Appetite swings both ways — lost interest or urgent grazing — via the gut-brain link.",
        "Nausea before big events is the mobilized gut, not illness.",
        "Energy runs a paradox budget: spending furiously while blocking recovery.",
        "Tired brains forecast darker futures — the loop feeds itself overnight.",
        "When all three shift together, look for the anxiety loop as the common cause.",
    ],
    "requirements": [
        "One week of noticing: sleep, meals, energy vs worry level",
        "No drastic fixes — observation first",
        "A regular wind-down hour as an experiment, not a prescription",
    ],
    "standards": [
        "Sleep-arousal interaction literature",
        "Gut-brain axis and stress-related GI effects",
        "Energy expenditure in sustained anxiety states",
    ],
    "citations": [
        "Harvey, A. G. A Cognitive Model of the Maintenance of Insomnia. Behaviour Research and Therapy; 2002.",
        "Mayer, E. A. Gut Feelings: The Emerging Biology of Gut-Brain Communication. Nature Reviews Neuroscience; 2011.",
        "Barlow, D. H. Anxiety and Its Disorders. 2nd ed. Guilford Press; 2002.",
    ],
    "sig_lens": (
        "Through the Signature lens, sleep, appetite, and energy are the ship's "
        "stores — food, water, and rest for the crew. The Signature reader "
        "watches the stores during long anxious voyages, because a captain who "
        "lets the stores run dry will face the next storm with an exhausted "
        "crew. Guard the stores and the ship can weather any forecast."
    ),
},
{
    "key": "anxiety-differences",
    "name": "Different Bodies, Different Anxiety: How Signals Vary",
    "group": "Body Signals",
    "ladder_rank": 13,
    "ladder_tier": "compounded",
    "description": (
        "No two bodies do anxiety the same way, and expecting yours to match "
        "the textbook can make you miss your own signals. One person gets the "
        "racing heart and the sweating palms; another gets the stomach in knots "
        "and the jaw aching by noon; a third gets cold hands, a tight throat, "
        "and a mind that goes blank instead of racing. Some people feel anxiety "
        "mostly above the neck — dizziness, pressure in the head, vision "
        "slightly off. Others feel it mostly below — gut churn, bladder urgency, "
        "heavy legs. Some get hot, some get cold. Some cannot sit still; some "
        "go statue-still. The variation comes from several sources. Genetics "
        "deals the baseline sensitivity of the alarm system. Past experience "
        "teaches the body which channel to use — a person whose anxiety once "
        "peaked with a pounding heart will watch the heart forever after. "
        "Interoceptive style matters too: some people are finely tuned to "
        "internal signals and notice every flutter, while others feel anxiety "
        "mostly as thoughts and only notice the body when it shouts. Culture "
        "and family shape which signals get attention — in some households the "
        "stomach is the accepted messenger, in others it is the headache. Age "
        "changes the mix as well: children often report stomachaches and "
        "headaches, adults more often the chest and the racing mind. The "
        "practical point is personal cartography. Your anxiety has a signature "
        "pattern — your first three signals, in your usual order. Learn that "
        "pattern and you get early warning: the moment signal one appears, you "
        "know the loop is starting, while it is still small enough to steer."
    ),
    "how_it_works": (
        "Signal variation arises because the anxiety response is assembled from "
        "multiple semi-independent channels — cardiac, respiratory, "
        "gastrointestinal, muscular, thermoregulatory — and individuals differ "
        "in each channel's gain. Genetic differences in autonomic reactivity set "
        "baseline gains. Associative learning then tunes the system: the "
        "channels most active during a person's most memorable anxious episodes "
        "become the default broadcast band, because the brain learns to monitor "
        "what once mattered. Interoceptive sensitivity — how precisely the brain "
        "reads internal signals — determines whether the person experiences "
        "anxiety as a body event or a thought event; high interoceptive "
        "awareness amplifies the felt intensity of whichever channel fires. "
        "Cultural and family display rules shape attention and reporting: the "
        "signals a household names become the signals its members notice. None "
        "of this changes the underlying loop — appraisal, arousal, rehearsal — "
        "but it changes the dashboard each person sees. Personal cartography "
        "works because the pattern is stable within a person: the same channels "
        "fire first most of the time, making early detection trainable."
    ),
    "key_points": [
        "Anxiety's channels vary: heart, gut, head, muscles, skin — everyone has a mix.",
        "Your first three signals in your usual order are your personal early-warning pattern.",
        "Past peak episodes teach the body which channel to broadcast on.",
        "Interoceptive style decides whether anxiety feels like a body event or a thought event.",
        "Culture, family, and age shape which signals get noticed and named.",
        "Learn your pattern and you catch the loop while it is still small.",
    ],
    "requirements": [
        "A personal signal map: your usual first, second, third signals",
        "Comparing notes with one other person — notice the differences",
        "Dropping the idea that your anxiety should look like anyone else's",
    ],
    "standards": [
        "Individual differences in autonomic reactivity",
        "Interoceptive sensitivity literature (Garfinkel et al.)",
        "Somatic symptom presentation across cultures",
    ],
    "citations": [
        "Garfinkel, S. N., et al. Knowing Your Own Heart: Distinguishing Interoceptive Accuracy. Biological Psychology; 2015.",
        "Barlow, D. H. Anxiety and Its Disorders. 2nd ed. Guilford Press; 2002.",
        "Kirmayer, L. J. Cultural Variations in the Clinical Presentation of Depression and Anxiety. Journal of Clinical Psychiatry; 2001.",
    ],
    "sig_lens": (
        "Through the Signature lens, every ship has its own creaks — one groans "
        "at the bow, another at the mast. The Signature reader learns his own "
        "vessel's sounds instead of listening for someone else's. Your three "
        "signals in your order are your private alarm code. Know the code and "
        "no storm takes you by surprise."
    ),
},
{
    "key": "anxiety-face",
    "name": "The Face of Anxiety: Eyes, Brows, Mouth, and Micro-Signs",
    "group": "Facial Expression",
    "ladder_rank": 14,
    "ladder_tier": "compounded",
    "description": (
        "The anxious face is a face on watch. Eyes: widened slightly, with more "
        "white showing, and moving — quick glances, scanning, checking the room, "
        "the door, the exits. The gaze rarely settles; it samples. In "
        "conversation the eyes may dart away and back, or fix a little too "
        "intently, as if trying to read the other person's verdict in advance. "
        "Brows: raised and drawn together — the classic worried brow. The inner "
        "corners lift while the center knits, producing the faint horizontal "
        "worry lines across the forehead that deepen with years of the "
        "expression. Mouth: the lips press together, thin out, or pull slightly "
        "down at the corners. The jaw sets; some people show a faint tremor at "
        "the chin. Smiles, when they appear, are often asymmetrical or tight — "
        "the social smile pasted over the watchful face, never quite reaching "
        "the eyes. Micro-signs — the brief, honest flashes: the quick lip bite, "
        "the nostril flare on a sharp inhale, the swallow that moves the throat, "
        "the blink rate climbing. The whole face carries a particular tension "
        "signature: the muscles around the eyes and mouth held at low readiness, "
        "like a sprinter in the blocks. It is not a dramatic mask — anxiety "
        "rarely looks theatrical. It looks like someone listening very hard for "
        "something, because that is exactly what the face is doing: the threat-"
        "monitoring system, made visible."
    ),
    "how_it_works": (
        "The anxious face is assembled by the same threat system that runs the "
        "body. Widened eyes increase the visual field — more data for the "
        "monitoring system. Raised, knitted brows are the brow-lowering and "
        "raising muscles firing in the worry configuration, an expression "
        "researchers find across cultures for distress and concern. Pressed lips "
        "and set jaw are the facial half of whole-body bracing. Rapid scanning "
        "eye movements are overt attention — the visual system sampling the "
        "environment for threat the way radar sweeps. Micro-signs leak because "
        "facial muscles receive some of the fastest neural signals in the body; "
        "brief expressions fire before deliberate control can suppress them. The "
        "tight, asymmetrical smile is a voluntary overlay — the social display "
        "muscles working against the involuntary worry pattern, which is why it "
        "looks pasted: the eyes keep the watchful configuration while the mouth "
        "performs reassurance. Reading the face works because the configuration "
        "is largely involuntary and therefore honest — the face reports the "
        "monitoring state whether the person wants it to or not."
    ),
    "key_points": [
        "Eyes widen and scan — the visual system sampling for threat.",
        "The worried brow: raised inner corners, knitted center, forehead lines.",
        "Mouth presses thin or pulls down; jaw sets; smiles look pasted.",
        "Micro-signs leak: lip bite, nostril flare, throat swallow, fast blinking.",
        "The whole face holds low readiness — a sprinter in the blocks.",
        "It looks like listening hard, because that is what it is.",
    ],
    "requirements": [
        "A mirror and the worried brow — try it, feel the muscles",
        "One remembered face: who wore this expression and when",
        "Attention to eyes first — they lead the configuration",
    ],
    "standards": [
        "Facial Action Coding System: brow and eye units in distress (Ekman & Friesen)",
        "Cross-cultural recognition of worry/distress expressions",
        "Micro-expression leakage literature",
    ],
    "citations": [
        "Ekman, P., & Friesen, W. V. Facial Action Coding System. Consulting Psychologists Press; 1978.",
        "Ekman, P. Emotions Revealed. 2nd ed. Holt; 2007.",
        "Shariff, A. F., & Tracy, J. L. What Are Emotion Expressions For? Current Directions in Psychological Science; 2011.",
    ],
    "sig_lens": (
        "Through the Signature lens, the anxious face is the lookout's face — "
        "eyes sweeping the horizon, brow working the glass. The Signature "
        "reader studies this face in others the way he studies his own gauges: "
        "not to judge the watch, but to know the weather it is watching. A face "
        "on watch deserves a steady deck, not a startled one."
    ),
},
{
    "key": "anxiety-face-intensity",
    "name": "How the Anxious Face Changes With Intensity",
    "group": "Facial Expression",
    "ladder_rank": 15,
    "ladder_tier": "compounded",
    "description": (
        "The anxious face is not one mask but a dial, and it turns with the "
        "volume. At mild intensity, the signs are whispers: the brow knits "
        "faintly and releases, the lips press for a second during a pause, the "
        "eyes do one extra sweep of the room. Most people would not notice; the "
        "person might not notice either. The face is still socially fluent — "
        "smiles land, expressions shift normally, the worry is a background "
        "process. At moderate intensity, the configuration locks in. The brow "
        "stays raised and knitted. The eyes stay wide and keep scanning — "
        "conversation partners start to feel watched rather than seen. The "
        "mouth thins and the jaw visibly works. The pasted smile appears here: "
        "the mouth performing 'I am fine' while the upper face keeps watch. "
        "Blink rate climbs. People nearby begin to read 'something is wrong' "
        "even if they cannot name it. At high intensity, the face can do two "
        "opposite things. Some faces flood: every muscle in the worry "
        "configuration fires at once — wide staring eyes, deeply furrowed brow, "
        "mouth pulled down or trembling, visible pallor or flushing. Others "
        "freeze: the face goes oddly blank and still, eyes fixed or unfocused, "
        "as if the system has put all its energy into the interior and left the "
        "face unpowered. Both are high-volume readings on the same dial. The "
        "practical skill is calibration: matching the face to the volume tells "
        "you whether someone needs a plan (mild), active help settling "
        "(moderate), or simply a steady, undemanding presence while the wave "
        "passes (high)."
    ),
    "how_it_works": (
        "Facial intensity tracks autonomic arousal almost linearly at low and "
        "moderate levels: more arousal recruits more facial muscle units, holds "
        "them longer, and defeats voluntary override more often — which is why "
        "the pasted smile fails increasingly as volume rises. The scanning eyes "
        "and rising blink rate track the attention system's sampling rate: "
        "higher threat appraisal means more frequent environmental checks. At "
        "high intensity the two divergent patterns — flood vs freeze — reflect "
        "the two ancient threat programs. Flooding is full mobilization made "
        "visible: every expressive muscle recruited. Freezing is the stillness "
        "program: motor output inhibited while assessment runs, leaving the "
        "face blank because the face is motor output too. Which pattern a "
        "person shows is a stable individual tendency, the same pacer-vs-"
        "freezer split seen in body movement. Either way, the upper face — "
        "brows and eyes — stays the most honest region across all volumes, "
        "because those muscles are hardest to voluntarily control."
    ),
    "key_points": [
        "Mild: whispers — a faint knit, one extra glance, socially fluent.",
        "Moderate: the configuration locks — pasted smile, scanning eyes, working jaw.",
        "High: flood (every muscle firing) or freeze (blank, unpowered face).",
        "Both high patterns are the same volume on the same dial.",
        "Upper face — brows and eyes — stays the most honest region.",
        "Calibrate your response to the volume the face is showing.",
    ],
    "requirements": [
        "Three faces from memory: one mild, one moderate, one high",
        "Noticing which high pattern your own face uses: flood or freeze",
        "Matching your response to the volume, not the drama",
    ],
    "standards": [
        "Dose-response in facial expression intensity (Ekman)",
        "Voluntary vs involuntary facial control gradients",
        "Freeze vs mobilization expressive patterns",
    ],
    "citations": [
        "Ekman, P. Emotions Revealed. 2nd ed. Holt; 2007.",
        "Ekman, P., & Friesen, W. V. Facial Action Coding System. Consulting Psychologists Press; 1978.",
        "LeDoux, J. The Emotional Brain. Simon & Schuster; 1996.",
    ],
    "sig_lens": (
        "Through the Signature lens, the face-dial is the signal lamp on the "
        "mast — dim at mild, bright at moderate, flashing or dark at high. The "
        "Signature reader reads lamp-brightness the way he reads swell height: "
        "it tells him which tools the moment wants. A dim lamp wants a plan; a "
        "flashing lamp wants a steady hand on the rail and no new orders until "
        "the sea settles."
    ),
},
{
    "key": "anxiety-hidden",
    "name": "Hiding Anxiety: Masks and What Leaks Through",
    "group": "Facial Expression",
    "ladder_rank": 16,
    "ladder_tier": "compounded",
    "description": (
        "People hide anxiety constantly — in meetings, on dates, at family "
        "dinners, in every situation where 'I am fine' is the required uniform. "
        "The masks are well practiced. The competent mask: brisk efficiency, "
        "extra preparation, humor deployed like smoke — the person looks like "
        "the most together one in the room. The casual mask: studied looseness, "
        "the laugh that comes a beat too fast, the 'no worries' said with a jaw "
        "you could strike a match on. The busy mask: perpetual motion and "
        "over-scheduling, so there is never a quiet moment for the feeling to "
        "surface. The cheerful mask: brightness turned up two notches past "
        "natural, warmth as camouflage. All four masks work — for a while, on "
        "most people. What leaks through is the involuntary layer. The hands: "
        "tapping, picking, gripping, the phone checked eleven times. The voice: "
        "a pitch half-step higher than the person's normal, speech slightly "
        "rushed, laughter slightly sharp. The body: the shoulder that will not "
        "come down, the foot going under the table, the stillness that is too "
        "still. The timing: answers that come too fast (rehearsed) or too slow "
        "(the mind was elsewhere). And the eyes — always the eyes — doing their "
        "quick sweeps while the mouth performs calm. The leaks matter for two "
        "reasons. For the hider: maintaining the mask is exhausting, and the "
        "exhaustion feeds the anxiety — the performance becomes part of the "
        "problem. For the observer: the leaks are an invitation, not an "
        "accusation. The kindest response to a leaking mask is to make the room "
        "safe enough that the mask can come down on its own."
    ),
    "how_it_works": (
        "Masking works through voluntary override of expressive behavior — the "
        "deliberate control systems driving the face, voice, and posture into "
        "the 'fine' configuration. It succeeds partially because much of social "
        "perception runs on the voluntary channel: people mostly register the "
        "performed expression. Leakage happens because the threat system drives "
        "expressive output through faster, less voluntary pathways — "
        "autonomic effects (voice pitch, sweating, blinking), overlearned habits "
        "(fidgeting), and micro-expressions that fire before suppression can "
        "engage. The harder the mask is held, the more arousal the effort "
        "itself generates — suppression is physiologically expensive — which "
        "increases the very signals being suppressed. This is the masking "
        "paradox: the performance of calm raises the body's alarm, producing "
        "more leaks. Observers detect leaks through the same fast pathways: "
        "humans are exquisitely sensitive to mismatches between voluntary and "
        "involuntary channels, which is why 'something is off' registers before "
        "any specific sign can be named."
    ),
    "key_points": [
        "Four common masks: competent, casual, busy, cheerful — all practiced, all partial.",
        "Leaks come from the fast involuntary layer: hands, voice pitch, eyes, timing.",
        "The eyes almost always keep watch while the mouth performs calm.",
        "Masking is physiologically expensive — the performance feeds the alarm.",
        "Observers feel 'something is off' before they can name a sign.",
        "Leaks are an invitation to make the room safer, not evidence to confront.",
    ],
    "requirements": [
        "One mask you wear — named without shame",
        "Noticing what it costs you to hold it",
        "One room where the mask could come down safely",
    ],
    "standards": [
        "Expressive suppression and its physiological costs (Gross, 2002)",
        "Micro-expression and leakage (Ekman)",
        "Channel-mismatch detection in social perception",
    ],
    "citations": [
        "Gross, J. J. Emotion Regulation: Affective, Cognitive, and Social Consequences. Psychophysiology; 2002.",
        "Ekman, P. Telling Lies. Norton; 2009.",
        "Butler, E. A., et al. The Social Consequences of Expressive Suppression. Emotion; 2003.",
    ],
    "sig_lens": (
        "Through the Signature lens, the mask is a flag flown for the harbor — "
        "'all is well' — while the lookout keeps sweeping the horizon behind "
        "it. The Signature reader respects the flag: it was raised for a "
        "reason. But he also reads the real weather, in himself and others, "
        "because a captain who believes every harbor flag sails into storms "
        "unprepared. Lower your own flag where it is safe; never tear down "
        "another's."
    ),
},
{
    "key": "anxiety-artist",
    "name": "Drawing Anxiety: Notes for Artists and Actors",
    "group": "Facial Expression",
    "ladder_rank": 17,
    "ladder_tier": "compounded",
    "description": (
        "To draw or play anxiety convincingly, forget the scream — anxiety is "
        "quieter than drama and more specific. Start with the eyes: widen them "
        "slightly, show a sliver more white, and aim the gaze just past the "
        "other person rather than at them — the look of someone monitoring the "
        "room while talking. Add the brow: lift the inner corners, knit the "
        "center, lay in the short horizontal worry lines. Keep it subtle — at "
        "rest the anxious brow is a suggestion, not a canyon. The mouth: press "
        "the lips together until they thin, or pull the corners down a few "
        "millimeters. If the character is masking, give the mouth a smile that "
        "the eyes refuse to join — the audience will feel the mismatch before "
        "they understand it. Hands are the supporting cast: one thumb worrying "
        "the other, fingers tapping a silent rhythm, a cup held with both hands "
        "like an anchor. Posture: shoulders up a centimeter and rolled forward, "
        "weight shifted as if ready to leave the chair. For the actor: the key "
        "is divided attention. Play a person whose body is in this conversation "
        "but whose mind keeps slipping to the 2 p.m. meeting — let the eyes "
        "drift, let answers come a half-beat late, let the breath stay high and "
        "quick. The voice should sit slightly higher than the character's "
        "normal and move slightly faster, with the laugh arriving too quickly. "
        "For escalation across a scene: start with just the brow and the hands, "
        "add the scanning eyes, then the pasted smile, then — at the peak — "
        "either the flood (everything firing) or the freeze (the terrible "
        "stillness). Audiences recognize anxiety instantly when it is specific, "
        "because everyone has worn this face."
    ),
    "how_it_works": (
        "Convincing portrayal works by reproducing the involuntary configuration "
        "rather than the stereotype. Audiences detect authenticity through the "
        "same channel-mismatch sensitivity they use in life: a performance that "
        "shows only the voluntary signals (wrung hands, theatrical gasps) reads "
        "as acting, while one that includes the involuntary layer — the upper-"
        "face worry pattern, the scanning gaze, the high quick breath audible "
        "in the voice — reads as real. The divided-attention direction works "
        "because it reproduces the actual cognitive state: the actor genuinely "
        "splitting attention produces the genuine micro-behaviors (delayed "
        "responses, gaze drift) without having to manufacture them. Escalation "
        "across a scene mirrors the real arousal curve, so the audience's own "
        "threat-detection systems track the rising tension — this is why "
        "well-played anxiety is contagious in a theater. The stillness option "
        "at peak works because audiences know the freeze program from their own "
        "bodies; the absence of expression at high stakes reads as more "
        "alarming than any grimace."
    ),
    "key_points": [
        "Forget the scream: anxiety is quiet, specific, and watchful.",
        "Eyes lead — widened, scanning, aimed just past the other person.",
        "The pasted smile the eyes refuse to join is the most telling mask.",
        "Hands are the supporting cast: tapping, worrying, anchoring.",
        "For actors: play divided attention — body here, mind at the 2 p.m. meeting.",
        "Escalate across the scene: brow, hands, scanning eyes, mask, then flood or freeze.",
    ],
    "requirements": [
        "A mirror and five minutes for the brow alone",
        "One film performance of anxiety to study frame by frame",
        "Trying the divided-attention exercise in a real conversation",
    ],
    "standards": [
        "FACS-based expression construction for performance",
        "Stanislavski-derived attention-splitting technique",
        "Audience threat-detection and emotional contagion",
    ],
    "citations": [
        "Ekman, P., & Friesen, W. V. Facial Action Coding System. Consulting Psychologists Press; 1978.",
        "Hatfield, E., et al. Emotional Contagion. Cambridge University Press; 1994.",
        "Konijn, E. A. Acting Emotions. Amsterdam University Press; 2000.",
    ],
    "sig_lens": (
        "Through the Signature lens, the artist and actor are the chart-makers — "
        "their drawings and performances become the maps by which others learn "
        "to read the weather. The Signature reader honors precise portrayal, "
        "because a true chart of the anxious face teaches a thousand lookouts. "
        "Draw it honestly: the quiet watch, the divided mind, the specific "
        "small tells. Truth in the chart saves ships."
    ),
},
{
    "key": "anxiety-triggers",
    "name": "Classic Triggers: What Commonly Sets Anxiety Off",
    "group": "Triggers",
    "ladder_rank": 18,
    "ladder_tier": "compounded",
    "description": (
        "Certain triggers set off anxiety in people everywhere — the classics, "
        "the ones almost everyone's forecast machinery recognizes. "
        "Evaluation: tests, interviews, performances, reviews — any situation "
        "where you are measured and the verdict is pending. The uncertainty "
        "plus the stakes make this the most universal trigger on the list. "
        "Health: a strange symptom, a waiting room, a test result pending — "
        "the body is both the sensor and the stakes, which doubles the signal. "
        "Money: bills, debt, job insecurity — uncertainty about survival "
        "resources speaks directly to the oldest part of the alarm system. "
        "Social judgment: parties, dates, meeting new people, speaking up — "
        "the tribe's verdict once meant survival, and the machinery still votes "
        "that way. Separation and travel: airports, goodbyes, unfamiliar "
        "places — the system dislikes leaving the known. Conflict: "
        "confrontations pending, difficult conversations scheduled — the forecast "
        "of a social storm. Deadlines and overload: too much to do, too little "
        "time — the future arriving faster than preparation can handle. News "
        "and waiting: the unanswered message, the ringing phone at odd hours, "
        "the results not yet in — pure uncertainty, the trigger in its most "
        "concentrated form. What unites the classics is the formula: something "
        "matters, the outcome is uncertain, and control feels limited. Learn "
        "your personal top three from this list and you have mapped most of "
        "your anxiety's territory — because while the details are yours, the "
        "categories are nearly universal."
    ),
    "how_it_works": (
        "Classic triggers work through the appraisal formula: high stakes plus "
        "high uncertainty plus low perceived control. Evaluation triggers "
        "threaten status and belonging — the social survival currencies the "
        "threat system evolved to guard. Health triggers collapse the distance "
        "between sensor and threat: the body reporting on itself creates a "
        "feedback loop with no outside reference. Money triggers tap resource "
        "security, one of the oldest alarm circuits. Social judgment triggers "
        "work because exclusion was historically dangerous; the brain treats "
        "the tribe's pending verdict as a survival variable. Travel and "
        "separation triggers fire on unfamiliarity — the monitoring system must "
        "work harder where it has no map. Conflict triggers forecast social "
        "damage. Overload triggers fire when demand exceeds the preparation "
        "budget — the forecast says 'you cannot get ready in time.' Waiting "
        "triggers are uncertainty in pure form: no information means the "
        "simulation engine runs unconstrained, generating worst cases without "
        "correction. The universality of the list reflects shared human "
        "stakes: status, health, resources, belonging, and control."
    ),
    "key_points": [
        "The classics: evaluation, health, money, social judgment, travel, conflict, overload, waiting.",
        "The formula: something matters + outcome uncertain + control feels limited.",
        "Waiting is uncertainty in pure form — the trigger at full concentration.",
        "Health triggers double the signal: the body is both sensor and stakes.",
        "Your personal top three from this list map most of your anxiety's territory.",
        "The categories are nearly universal; only the details are personal.",
    ],
    "requirements": [
        "Your personal top three triggers, ranked honestly",
        "Noticing the formula at work in each one",
        "One trigger to prepare for this week — concretely",
    ],
    "standards": [
        "Stakes-uncertainty-control appraisal model",
        "Social-evaluative threat literature",
        "Intolerance of uncertainty construct (Dugas et al.)",
    ],
    "citations": [
        "Dugas, M. J., et al. Intolerance of Uncertainty and Worry. Cognitive Therapy and Research; 1998.",
        "Dickerson, S. S., & Kemeny, M. E. Acute Stressors and Cortisol Responses. Psychological Bulletin; 2004.",
        "Barlow, D. H. Anxiety and Its Disorders. 2nd ed. Guilford Press; 2002.",
    ],
    "sig_lens": (
        "Through the Signature lens, the classic triggers are the charted reefs "
        "— marked on every captain's map because every ship meets them. The "
        "Signature reader does not pretend the reefs are not there; he studies "
        "the chart, marks his own course through them, and prepares the crew "
        "before the water gets shallow. Know your three reefs. Sail them "
        "deliberately."
    ),
},
{
    "key": "anxiety-personal-triggers",
    "name": "Personal Triggers: Memory, Dates, and Private Associations",
    "group": "Triggers",
    "ladder_rank": 19,
    "ladder_tier": "compounded",
    "description": (
        "Beyond the universal classics, every person carries a private set of "
        "triggers — wired by their own history, invisible to everyone else. A "
        "particular ringtone that once delivered bad news, and now the stomach "
        "drops before the mind remembers why. The smell of a hospital corridor. "
        "The anniversary week of a hard year — the calendar itself becomes a "
        "trigger, the body bracing days before the conscious mind connects the "
        "date. A song from the summer everything went wrong. The specific "
        "intersection where the accident happened; the route changes, the "
        "detour becomes permanent. A phrase a critical parent used, heard now "
        "from a boss, landing with twenty years of weight. These triggers are "
        "powerful precisely because they are personal: the forecast machinery "
        "learned them the hard way, in a moment of real stakes, and it does not "
        "unlearn easily. They are also confusing, because they fire without a "
        "visible reason — the person feels anxious 'for no reason' while the "
        "reason sits one layer down, in memory. Mapping them is detective work: "
        "when the anxiety spikes, ask what just happened — what did I see, "
        "hear, smell, what date is it, what does this resemble. The answer is "
        "often embarrassingly specific: the elevator music from the building "
        "where I got the bad diagnosis. Once mapped, a personal trigger loses "
        "much of its power — not because the memory vanishes, but because the "
        "person can now say 'that is the anniversary, not a new emergency,' and "
        "the forecast gets corrected by the facts."
    ),
    "how_it_works": (
        "Personal triggers are built by associative learning — the same "
        "machinery that teaches all threat responses, applied to individual "
        "experience. When a neutral cue (a ringtone, a date, a smell) coincides "
        "with a moment of high stakes and high arousal, the brain binds them: "
        "the cue becomes a predictor, and future encounters with the cue fire "
        "the forecast loop automatically, before conscious recognition. "
        "Anniversary reactions work through temporal conditioning — the nervous "
        "system tracks seasonal and calendar patterns below awareness. The "
        "'no reason' quality comes from the speed of the pathway: the "
        "association fires through fast subcortical routes while the slower "
        "conscious mind is still catching up, so the feeling arrives before "
        "the explanation. Mapping works through reconsolidation and "
        "reappraisal: naming the link ('this is the hospital smell, and I am "
        "not in the hospital now') gives the slower systems a chance to update "
        "the prediction. The association may never fully erase — the cue may "
        "always carry a flicker — but the flicker stops being mistaken for a "
        "fresh emergency."
    ),
    "key_points": [
        "Personal triggers are privately wired by your own history — invisible to others.",
        "Ringtones, smells, songs, dates, intersections, phrases: the cue list is endlessly specific.",
        "They fire 'for no reason' because the reason sits one layer down, in memory.",
        "Anniversary reactions: the calendar itself can become a trigger.",
        "Mapping is detective work: what just happened, what does this resemble.",
        "A named trigger loses power — 'that is the anniversary, not a new emergency.'",
    ],
    "requirements": [
        "One personal trigger, mapped: the cue and the original moment",
        "The detective question asked at the next unexplained spike",
        "Compassion for the part of you that learned it the hard way",
    ],
    "standards": [
        "Associative fear/anxiety conditioning (Pavlov; LeDoux)",
        "Anniversary and temporal conditioning effects",
        "Reconsolidation and reappraisal mechanisms",
    ],
    "citations": [
        "LeDoux, J. The Emotional Brain. Simon & Schuster; 1996.",
        "Mineka, S., & Zinbarg, R. A Contemporary Learning Theory Perspective on Anxiety Disorders. Current Directions in Psychological Science; 2006.",
        "Barlow, D. H. Anxiety and Its Disorders. 2nd ed. Guilford Press; 2002.",
    ],
    "sig_lens": (
        "Through the Signature lens, personal triggers are the uncharted rocks "
        "— not on any standard map, known only to the captain who struck them "
        "once. The Signature reader charts his own rocks deliberately, marking "
        "each with its true name and date. A rock on the chart is a hazard "
        "managed; a rock unmarked is a wreck waiting. No shame in the striking "
        "— only in refusing to chart it."
    ),
},
{
    "key": "anxiety-surprise-triggers",
    "name": "Surprise Triggers: The Odd and Unexpected",
    "group": "Triggers",
    "ladder_rank": 20,
    "ladder_tier": "compounded",
    "description": (
        "Then there are the triggers nobody would predict — the odd ones that "
        "make people feel irrational until they understand the machinery. "
        "Good news can trigger anxiety: the promotion, the acceptance letter, "
        "the 'yes' — because any big change, even a welcome one, is uncertain, "
        "and the forecast machinery does not grade on pleasantness. Quiet can "
        "trigger it: the house finally silent after a chaotic week, and the "
        "mind, unemployed, starts scanning for problems to solve. Boredom, "
        "rest, the Sunday evening with nothing scheduled — idleness gives the "
        "simulation engine an empty stage. Physical states masquerade as "
        "triggers: too much caffeine and the heart is already racing, so the "
        "mind reads the body and concludes something must be wrong; low blood "
        "sugar, dehydration, and exhaustion all lower the threshold until the "
        "loop starts on almost nothing. Other people's moods: a partner's "
        "sigh, a friend's short reply — the social monitoring system flags a "
        "possible rift and the forecast runs ahead of the facts. Even feeling "
        "calm can trigger it in veterans of long anxiety: the quiet feels "
        "suspicious, 'too quiet,' and the system manufactures a worry to fill "
        "the silence. The lesson of the surprise triggers is humility about "
        "the machinery. It is not rational and not personal — it is a "
        "pattern-matching engine with a hair trigger, and sometimes the pattern "
        "it matches is just 'heart beating fast' or 'nothing happening.' "
        "Knowing the odd triggers exist turns 'I am anxious for no reason' "
        "into 'my system is reading the caffeine / the quiet / the good news' "
        "— and that sentence alone often starts the unwind."
    ),
    "how_it_works": (
        "Surprise triggers work through misattribution and threshold effects. "
        "Good news triggers anxiety because the appraisal system responds to "
        "uncertainty and change, not valence — a promotion is a high-stakes "
        "unknown, which is the full trigger formula regardless of how welcome "
        "it is. Quiet and idleness trigger it because the simulation engine is "
        "always running; without external task load, spare capacity defaults "
        "to threat simulation — the mind abhors an unfilled future. "
        "Physiological triggers work through interoceptive misreading: the "
        "brain infers emotion partly from body state, so a caffeine-raised "
        "heart rate is read as 'I must be anxious about something,' and the "
        "forecast then obligingly invents the something. Low fuel states lower "
        "the appraisal threshold — a tired, dehydrated brain appraises more "
        "things as threatening. Social micro-cues trigger the belonging-"
        "monitoring system, which is tuned to false-positive: better to check "
        "a sigh that meant nothing than miss one that meant trouble. Calm "
        "triggering anxiety is the sensitized system treating the absence of "
        "its familiar signal as itself a signal — the watchdog barking at the "
        "quiet."
    ),
    "key_points": [
        "Good news triggers anxiety: change is uncertain regardless of pleasantness.",
        "Quiet, rest, and boredom give the simulation engine an empty stage.",
        "Caffeine, low blood sugar, exhaustion: the body fakes the signal, the mind believes it.",
        "A partner's sigh can launch a full forecast — the belonging monitor false-positives by design.",
        "Long-time worriers can find calm itself suspicious.",
        "'No reason' usually means the reason is physiological or situational, not emotional.",
    ],
    "requirements": [
        "One surprise trigger from your own life, identified",
        "Checking the basics first: fuel, rest, stimulants",
        "Remembering the machinery is pattern-matching, not judging",
    ],
    "standards": [
        "Misattribution of arousal (Schachter & Singer, 1962)",
        "Interoceptive inference models",
        "Default-mode threat simulation",
    ],
    "citations": [
        "Schachter, S., & Singer, J. E. Psychological Review; 1962.",
        "Dutton, D. G., & Aron, A. P. Misattribution of Arousal. Journal of Personality and Social Psychology; 1974.",
        "Barlow, D. H. Anxiety and Its Disorders. 2nd ed. Guilford Press; 2002.",
    ],
    "sig_lens": (
        "Through the Signature lens, surprise triggers are the false contacts "
        "on the scope — whales mistaken for submarines, clouds for sails. The "
        "Signature reader does not court-martial the scope operator; he "
        "calibrates the instrument. Check the caffeine, check the fuel, check "
        "the quiet — then ask whether the contact is real. Most false contacts "
        "dissolve under one honest look."
    ),
},
{
    "key": "anxiety-cascade",
    "name": "Chain Reactions: How One Trigger Starts a Cascade",
    "group": "Triggers",
    "ladder_rank": 21,
    "ladder_tier": "compounded",
    "description": (
        "Anxiety's most exhausting trick is the cascade: one trigger fires, "
        "and the feeling recruits reinforcements until the original worry is "
        "buried under an avalanche. It starts small. The 2 p.m. meeting is "
        "tomorrow. By 10 a.m. the meeting has recruited the presentation, which "
        "has recruited the promotion, which has recruited the mortgage, which "
        "has recruited the children's future, which has recruited a vague "
        "dread about everything. Each link feels logical in the moment — each "
        "'and then what' is a reasonable question — but the chain has traveled "
        "from a meeting to the meaning of life in six steps. The body cannot "
        "tell the difference between link one and link six: the arousal is "
        "real at every step, so the far end of the chain feels as urgent as "
        "the near end. This is why cascades are so convincing — the feeling "
        "validates each link as it forms. The cascade also recruits the past "
        "and the body: link four reminds you of the time it did go wrong, link "
        "five notices the heart pounding, which becomes new evidence that "
        "something is truly wrong. Breaking a cascade does not require solving "
        "link six. It requires catching link two — noticing the moment the "
        "mind leaves the actual trigger and starts its recruitment drive. The "
        "practical move is the chain audit: write the links down, literally, "
        "and watch the absurdity become visible. Link one is usually a real, "
        "preparable thing. Link six is usually a philosophical question wearing "
        "a worry costume. Solve link one; let link six wait for a calmer hour."
    ),
    "how_it_works": (
        "Cascades run on associative chaining plus arousal validation. Each "
        "worry activates semantically and emotionally linked worries — the "
        "brain's associative networks are organized so that threat nodes "
        "connect to other threat nodes, and activation spreads along those "
        "links. 'And then what' is the mind following the strongest "
        "associative path, which under arousal is always the threat path. "
        "Arousal validates each link because the body responds to imagined "
        "futures almost as strongly as real ones — the pounding heart at link "
        "five is misread as evidence for link five's importance rather than as "
        "residue from link one. Memory recruitment adds fuel: past failures "
        "are more accessible under threat mood (mood-congruent memory), so the "
        "chain keeps finding 'proof.' The chain audit breaks the cascade "
        "through externalization and appraisal correction: writing the links "
        "down moves them from the fast associative system to the slow "
        "deliberate one, where the probability drop-off between links becomes "
        "visible — each 'and then' multiplies uncertainty, so link six is "
        "usually orders of magnitude less likely than it feels."
    ),
    "key_points": [
        "Cascades: one trigger recruits linked worries until the original is buried.",
        "Each 'and then what' feels logical; the chain travels from meeting to meaning of life.",
        "Arousal validates every link — the body cannot tell link one from link six.",
        "Mood-congruent memory supplies 'proof' from past failures.",
        "Catch link two: the moment the mind leaves the actual trigger.",
        "The chain audit: write the links, solve link one, let link six wait.",
    ],
    "requirements": [
        "One recent cascade, written out link by link",
        "Noticing where your chains usually jump the rails",
        "A pen — the audit works better on paper than in the head",
    ],
    "standards": [
        "Associative network models of emotion (Bower, 1981)",
        "Mood-congruent memory effects",
        "Worry chain and catastrophizing literature (Vasey & Borkovec)",
    ],
    "citations": [
        "Bower, G. H. Mood and Memory. American Psychologist; 1981.",
        "Vasey, M. W., & Borkovec, T. D. A Catastrophizing Assessment of Worrisome Thoughts. Cognitive Therapy and Research; 1992.",
        "Barlow, D. H. Anxiety and Its Disorders. 2nd ed. Guilford Press; 2002.",
    ],
    "sig_lens": (
        "Through the Signature lens, the cascade is a mutiny of the imagination "
        "— one worried sailor recruiting the whole crew deck by deck until the "
        "ship is sailing to rescue a future that does not exist. The Signature "
        "reader puts down the mutiny at the second deck: he writes the chain, "
        "reads it aloud, and watches the crew laugh at link six. Then he gives "
        "link one its orders and sends the rest below."
    ),
},
{
    "key": "anxiety-actions",
    "name": "What People Do: Typical Actions and Reactions Under Anxiety",
    "group": "Anxiety in Behavior",
    "ladder_rank": 22,
    "ladder_tier": "advanced",
    "description": (
        "Anxiety writes itself into behavior in recognizable patterns. "
        "Avoidance: the headline act. The invitation declined, the call not "
        "made, the route changed, the appointment postponed — each avoidance "
        "buys immediate relief and charges long-term interest, because the "
        "unfaced thing grows in the imagination. Checking and reassurance-"
        "seeking: the locks checked three times, the message re-read, the "
        "'are you mad at me' text, the symptom searched at 1 a.m. — attempts "
        "to manufacture the certainty the future refuses to give. "
        "Over-preparation: the bag packed for every scenario, the presentation "
        "rehearsed eleven times, the research that never ends — preparation "
        "past the point of usefulness, where it becomes the anxiety wearing a "
        "disguise. Procrastination's anxious twin: delay as avoidance, the task "
        "untouched because starting it would make the uncertainty real. "
        "Numbing and escape: scrolling, snacking, drinking, anything to turn "
        "the volume down without addressing the signal. Control behaviors: "
        "lists, schedules, rigid routines — attempts to shrink uncertainty by "
        "shrinking the world. And the social patterns: going quiet in groups, "
        "over-talking to fill silence, arriving early to scout, leaving early "
        "to escape, the smile that agrees with everything to avoid any ripple. "
        "None of these are character flaws. Each is a strategy the system "
        "invented to handle uncertainty — and each can be evaluated the same "
        "way: does it shrink the anxiety over time, or does it rent relief by "
        "the hour while the price keeps rising."
    ),
    "how_it_works": (
        "Anxious behaviors are operant strategies — actions the system has "
        "learned because they change the feeling. Avoidance works through "
        "negative reinforcement: leaving the situation drops arousal fast, "
        "which teaches the brain that avoidance is the solution — while "
        "preventing the disconfirming experience that would shrink the fear. "
        "Checking and reassurance-seeking are uncertainty-reduction attempts; "
        "they fail long-term because reassurance habituates — each dose wears "
        "off faster, requiring more. Over-preparation is the preparation "
        "instinct overshooting: useful up to the point of diminishing returns, "
        "then it becomes rumination with a clipboard. Procrastination-as-"
        "avoidance keeps the threat abstract, and abstract threats are always "
        "scarier than concrete ones. Numbing behaviors work through arousal "
        "dampening without appraisal change — the signal is muted, not "
        "answered. Control behaviors reduce uncertainty by reducing the "
        "world, which works until the world refuses to stay small. The "
        "evaluation question — does it shrink anxiety over time — separates "
        "coping from maintenance: coping changes the appraisal or builds "
        "tolerance; maintenance rents relief while preserving the loop."
    ),
    "key_points": [
        "Avoidance buys immediate relief and charges long-term interest.",
        "Checking manufactures certainty the future refuses to give — and habituates.",
        "Over-preparation is anxiety in a useful disguise; watch for the overshoot.",
        "Numbing turns the volume down without answering the signal.",
        "Control behaviors shrink the world to shrink the uncertainty.",
        "The test for any strategy: does it shrink anxiety over time, or rent relief by the hour.",
    ],
    "requirements": [
        "Your top three anxious behaviors, named without judgment",
        "Running each through the over-time test",
        "One maintenance behavior to experiment with reducing",
    ],
    "standards": [
        "Operant maintenance of avoidance (Mowrer, two-factor theory)",
        "Reassurance-seeking and habituation literature",
        "Safety behavior models (Salkovskis)",
    ],
    "citations": [
        "Mowrer, O. H. Learning Theory and Behavior. Wiley; 1960.",
        "Salkovskis, P. M. The Importance of Behaviour in the Maintenance of Anxiety. Behaviour Research and Therapy; 1991.",
        "Barlow, D. H. Anxiety and Its Disorders. 2nd ed. Guilford Press; 2002.",
    ],
    "sig_lens": (
        "Through the Signature lens, anxious behaviors are the crew's "
        "improvised drills — some smart, some merely busy. The Signature "
        "reader musters the crew and reviews every drill against one standard: "
        "does it make the ship safer over time, or does it just keep the crew "
        "running in circles? He keeps the drills that work, retires the ones "
        "that only look like work, and never confuses motion with seamanship."
    ),
},
{
    "key": "anxiety-words",
    "name": "What People Say: Words, Tone, and Speech Patterns",
    "group": "Anxiety in Behavior",
    "ladder_rank": 23,
    "ladder_tier": "advanced",
    "description": (
        "Anxiety has a dialect, and once you learn it you hear it everywhere. "
        "The vocabulary: 'what if' opens almost every anxious sentence — 'what "
        "if it goes wrong,' 'what if they think,' 'what if I can't.' Hedging "
        "multiplies: 'maybe,' 'probably,' 'I guess,' 'sort of,' 'kind of' — "
        "the language of a mind refusing to commit to any single future. "
        "Catastrophe words appear early: 'disaster,' 'terrible,' 'unbearable,' "
        "'can't handle' — the forecast stated at maximum volume. Reassurance "
        "questions loop: 'are you sure,' 'do you think it'll be okay,' 'you "
        "don't think they're mad, right' — the same question in new costumes. "
        "Apology inflation: 'sorry' for things that need no apology, preemptive "
        "apologies for futures that have not happened. The tone: pitch sits a "
        "half-step higher than the person's baseline, the voice thinner — "
        "breath held high in the chest starves the voice of its full resonance. "
        "Pace hurries; anxious speech often runs ahead of itself, sentences "
        "colliding. Or the opposite: long pauses mid-sentence where the mind "
        "went to check the forecast. Laughter comes too fast and too sharp, a "
        "discharge of tension rather than amusement. The speech patterns: "
        "rehearsing out loud ('so I'll say... and then if they say...'), "
        "narrating the worry to anyone nearby, asking the same question of "
        "three people, talking through the plan for the fourth time. None of "
        "this is a flaw in the speaker. It is the forecasting loop made "
        "audible — the mind thinking out loud because thinking quietly was not "
        "containing it."
    ),
    "how_it_works": (
        "Anxious speech is the verbal overflow of the forecasting loop. 'What "
        "if' constructions are literally the simulation engine's output format "
        "— each what-if is a generated future being voiced. Hedging reflects "
        "the appraisal state: with the future genuinely uncertain to the "
        "speaker, commitment to any single statement feels dangerous, so "
        "language stays provisional. Catastrophe words are the alarm's volume "
        "made verbal — high arousal biases word choice toward extremes. "
        "Reassurance questions are external uncertainty-reduction: outsourcing "
        "the appraisal to another mind. Apology inflation is social-threat "
        "management — preemptive submission to keep the tribe's verdict "
        "favorable. The vocal changes are mechanical: high chest breathing "
        "raises laryngeal tension (higher pitch), arousal speeds motor output "
        "(faster pace), and cognitive load from the background simulation "
        "causes pauses and restarts. Rehearsing aloud and repeat-narrating are "
        "attempts to close the loop externally — if saying it does not settle "
        "it, the loop says it again. Hearing the dialect lets you respond to "
        "the loop, not just the words."
    ),
    "key_points": [
        "'What if' is the simulation engine's output format, spoken aloud.",
        "Hedging is language staying provisional while the future is uncertain.",
        "Reassurance questions outsource the appraisal to another mind.",
        "Voice goes higher and thinner; pace hurries or stalls mid-sentence.",
        "Apology inflation is preemptive social-threat management.",
        "The dialect is the forecasting loop made audible — respond to the loop, not just the words.",
    ],
    "requirements": [
        "Listening for 'what if' in your own speech for one day",
        "Noticing your pitch and pace when the loop is running",
        "One reassurance question caught and answered internally first",
    ],
    "standards": [
        "Verbal markers of worry (Borkovec et al.)",
        "Vocal acoustics under stress/arousal",
        "Reassurance-seeking discourse patterns",
    ],
    "citations": [
        "Borkovec, T. D., et al. The Nature of Worry. Behaviour Research and Therapy; 1983.",
        "Scherer, K. R. Vocal Communication of Emotion. Handbook of Emotions; 2003.",
        "Barlow, D. H. Anxiety and Its Disorders. 2nd ed. Guilford Press; 2002.",
    ],
    "sig_lens": (
        "Through the Signature lens, anxious speech is the lookout calling down "
        "every sighting — 'sail ho, maybe, possibly, what if it's a warship.' "
        "The Signature reader trains his lookout's reports: state the contact, "
        "state the bearing, state your confidence, then stand by. 'What if' "
        "without end is not a report; it is static. Clear reports, calm ship."
    ),
},
{
    "key": "anxiety-decisions",
    "name": "Anxious Decisions: How Anxiety Shapes Choices",
    "group": "Anxiety in Behavior",
    "ladder_rank": 24,
    "ladder_tier": "advanced",
    "description": (
        "Anxiety does not just color feelings — it votes in every decision, "
        "and it votes for safety. The anxious decision-maker overweights "
        "downside: the 5 percent chance of embarrassment feels like 50 "
        "percent, because the simulation engine renders the bad outcome in "
        "high definition while the good outcomes stay blurry. This produces "
        "the classic distortions. Risk estimates inflate: the flight, the "
        "investment, the conversation all look more dangerous than their base "
        "rates. Options narrow: the mind presents two choices — the safe one "
        "and the catastrophe — while the reasonable middle options never make "
        "it to the table. Decisions get postponed: 'I need more information' "
        "becomes a permanent address, because deciding would end the "
        "uncertainty and the system, paradoxically, prefers familiar worry to "
        "unfamiliar resolution. Or decisions get rushed: grabbing the first "
        "safe option to end the discomfort of choosing. Other people get "
        "recruited as decision-makers — the endless polling of friends, the "
        "deferral to authority — outsourcing the choice to dodge the regret. "
        "And reversibility becomes the supreme value: the anxious chooser will "
        "pay a premium, in money or in life, for the option that can be undone. "
        "The counter-skill is decision hygiene: separate the forecast from the "
        "facts, get base rates where they exist, set a decision deadline in "
        "advance, and judge the choice by the process, not by the anxiety it "
        "produced. Anxiety is a consultant with a known bias — listen to its "
        "risk report, then check its math."
    ),
    "how_it_works": (
        "Anxiety shapes decisions through well-mapped cognitive biases. "
        "Probability overestimation: arousal amplifies the perceived "
        "likelihood of threat outcomes — the affect heuristic, where feeling "
        "drives judged frequency. Loss aversion steepens: the same potential "
        "loss feels larger under anxiety, so safe options gain disproportionate "
        "value. The option set narrows through attentional capture: the "
        "threat simulation consumes working memory, leaving less capacity to "
        "generate creative middle options. Postponement is avoidance applied "
        "to choosing — deciding collapses uncertainty, and the anxious system "
        "treats the familiar worry as safer than the unfamiliar aftermath. "
        "Rushing is the same avoidance at higher speed: ending the aversive "
        "state of indecision. Outsourcing the decision is responsibility "
        "transfer — if someone else chooses, the regret belongs to them. "
        "Decision hygiene works because it moves the choice from the fast "
        "threat system to the slow deliberate one: base rates correct the "
        "inflated probabilities, pre-set deadlines defeat postponement, and "
        "process-based evaluation prevents the anxiety itself from being read "
        "as evidence against the option."
    ),
    "key_points": [
        "Anxiety votes for safety in every decision — and it overweights downside.",
        "The 5 percent risk feels like 50 percent: vividness is mistaken for probability.",
        "Options narrow to 'safe vs catastrophe'; the reasonable middle vanishes.",
        "Postponement and rushing are both avoidance of the discomfort of choosing.",
        "Outsourcing the choice is responsibility transfer, not wisdom.",
        "Decision hygiene: base rates, deadlines, judge the process — check anxiety's math.",
    ],
    "requirements": [
        "One pending decision to run through decision hygiene",
        "Base rates looked up, not guessed",
        "A deadline set before the research begins",
    ],
    "standards": [
        "Affect heuristic (Slovic et al.)",
        "Loss aversion under anxiety (Kahneman & Tversky)",
        "Judgment and decision-making under emotion",
    ],
    "citations": [
        "Slovic, P., et al. Risk as Analysis and Risk as Feelings. Risk Analysis; 2004.",
        "Kahneman, D., & Tversky, A. Prospect Theory. Econometrica; 1979.",
        "Lerner, J. S., & Keltner, D. Fear, Anger, and Risk. Journal of Personality and Social Psychology; 2001.",
    ],
    "sig_lens": (
        "Through the Signature lens, anxiety at the decision table is the "
        "cautious navigator — valuable, biased, and never the captain. The "
        "Signature reader gives the navigator his hearing: the risk report is "
        "logged and respected. Then the captain checks the charts, sets the "
        "deadline, and gives the order. A ship that only sails safe waters "
        "never reaches any harbor worth naming."
    ),
},
{
    "key": "anxiety-escalation",
    "name": "Escalation: How Behavior Changes as Anxiety Grows",
    "group": "Anxiety in Behavior",
    "ladder_rank": 25,
    "ladder_tier": "advanced",
    "description": (
        "Watch anxiety climb and the behavior climbs with it, in a predictable "
        "ladder of its own. At low volume, behavior stays strategic: the "
        "person prepares a little more, double-checks the important things, "
        "asks one good question. The anxiety is working as designed — a "
        "consultant, not a commander. At moderate volume, the strategies "
        "multiply and start costing: the checking becomes triple-checking, "
        "preparation eats the evening, reassurance-seeking starts to strain "
        "relationships, avoidance quietly edits the calendar. The person is "
        "still functioning — working, socializing, deciding — but a growing "
        "share of the day's budget goes to managing the feeling rather than "
        "living the life. Sleep shortens, patience thins, the snap appears. At "
        "high volume, behavior becomes about the anxiety itself: the day "
        "organizes around avoiding triggers, the reassurance-seeking becomes "
        "urgent and hard to satisfy, numbing behaviors escalate, and ordinary "
        "demands — the phone call, the errand, the small talk — feel "
        "disproportionately heavy. Thinking narrows to the threat; everything "
        "else is triage. At the crest, some people freeze into inaction while "
        "others discharge into frantic busyness — opposite behaviors, same "
        "overload. The escalation ladder matters because interventions have "
        "an order. Low: plan and prepare — the anxiety is usable. Moderate: "
        "add active calming and cut the maintenance behaviors — stop feeding "
        "the loop. High: settle the body first, shrink the demands to the "
        "essential, and let the wave pass before any big thinking. Trying to "
        "'think through it' at the crest is like charting a course in a "
        "hurricane — the skill at high volume is not navigation but seamanship: "
        "hold the ship together until the sea settles."
    ),
    "how_it_works": (
        "Escalation follows the arousal curve's capture of behavior. At low "
        "arousal, the prefrontal systems stay dominant: behavior is goal-"
        "directed, flexible, proportional — preparation serves the actual "
        "task. As arousal climbs into the moderate range, the threat system "
        "gains priority: attention narrows, working memory fills with "
        "simulation, and behavior shifts from task-serving to threat-serving — "
        "checking, seeking, avoiding. These are still organized behaviors, but "
        "their master has changed from the goal to the feeling. At high "
        "arousal, the capture is near-total: the behaviors become urgent and "
        "rigid because the system is treating the situation as survival-"
        "relevant, where speed beats nuance. Freeze and frantic busyness are "
        "the two overload outputs — inhibition vs discharge — the same split "
        "seen in posture and facial expression. The intervention order mirrors "
        "the capture order: cognitive strategies work where cognition is still "
        "online (low to moderate); at high arousal the body must be settled "
        "first because the cognitive hardware is the occupied territory. This "
        "is why the same advice — 'just make a plan' — helps at low volume "
        "and fails at the crest."
    ),
    "key_points": [
        "Low: strategic behavior — the anxiety works as a consultant.",
        "Moderate: threat-serving behavior — checking, seeking, avoiding multiply and cost.",
        "High: the day organizes around the anxiety itself; demands feel disproportionate.",
        "Freeze and frantic busyness are opposite outputs of the same overload.",
        "Interventions have an order: plan, then calm-and-cut, then settle-the-body.",
        "'Think through it' fails at the crest — seamanship before navigation.",
    ],
    "requirements": [
        "Locating your last escalation on the ladder honestly",
        "Noticing which rung your maintenance behaviors live on",
        "Matching the intervention to the rung, not the wish",
    ],
    "standards": [
        "Arousal-cognition capture gradients",
        "Safety behavior escalation models",
        "Stepped-care logic in anxiety management",
    ],
    "citations": [
        "Barlow, D. H. Anxiety and Its Disorders. 2nd ed. Guilford Press; 2002.",
        "Salkovskis, P. M. Behaviour Research and Therapy; 1991.",
        "Eysenck, M. W., et al. Attentional Control Theory. Emotion; 2007.",
    ],
    "sig_lens": (
        "Through the Signature lens, escalation is the sea state rising — and "
        "every sea state has its seamanship. The Signature reader does not "
        "sail a storm the way he sails a swell: low water gets charts and "
        "plans, rising water gets the crew mustered and the loose gear "
        "secured, and the full gale gets one order — hold together. Match the "
        "seamanship to the sea and every storm is survivable."
    ),
},
{
    "key": "anxiety-healthy",
    "name": "Healthy Expression: Saying It, Showing It, Channeling It",
    "group": "Healthy Expression",
    "ladder_rank": 26,
    "ladder_tier": "advanced",
    "description": (
        "Anxiety expressed well is anxiety put to work — the signal honored "
        "and the energy used. Saying it: naming the feeling out loud, "
        "specifically. 'I am anxious about the presentation tomorrow because "
        "the client is unpredictable' beats 'I am stressed' the way a street "
        "address beats 'somewhere in the city.' Specific naming tells the "
        "forecasting loop it has been heard, which often turns the volume "
        "down, and it tells other people what is actually happening, which "
        "lets them respond to the real thing. Showing it: letting the feeling "
        "be visible where it is safe — the honest 'I am nervous about this' "
        "before the big moment, the hand that is allowed to shake instead of "
        "being wrestled still. Paradoxically, permitted anxiety is smaller "
        "anxiety; the war against the feeling is usually what enlarges it. "
        "Channeling it: giving the mobilized energy a job. The body prepared "
        "for action — so give it action: the walk before the interview, the "
        "tidying before the call, the rehearsal that ends at a set time, the "
        "preparation list worked through and then closed. Anxiety channeled "
        "into preparation is the emotion fulfilling its purpose; the loop "
        "closes because the future it was forecasting has been prepared for. "
        "The three moves share a principle: anxiety is a messenger, and "
        "messengers stop shouting once the message is received. Say it to "
        "receive it, show it where it is safe to stop fighting it, channel it "
        "to answer it. What is left after the message is received is usually "
        "much smaller than what arrived."
    ),
    "how_it_works": (
        "Healthy expression works by closing the forecasting loop through its "
        "designed exits. Naming works through affect labeling: putting the "
        "feeling into precise words reduces amygdala reactivity and engages "
        "prefrontal regulation — the label literally turns down the alarm's "
        "gain. Specificity matters because the loop quiets when the appraisal "
        "is resolved; 'stressed' resolves nothing, while 'anxious about the "
        "client's unpredictability' identifies a preparable target. Showing "
        "it works by ending suppression: expressive suppression is "
        "physiologically expensive and sustains arousal, so dropping the "
        "performance lets the arousal curve fall naturally. Channeling works "
        "through discharge and completion: mobilization energy given real "
        "action (walking, preparing, rehearsing) gets the discharge the "
        "situation denied it, and completed preparation updates the appraisal "
        "— the future is now more predictable, so the forecast quiets. All "
        "three are loop-closing moves: they give the signal its designed "
        "outcome (preparation, communication, action) instead of trapping it "
        "in rehearsal."
    ),
    "key_points": [
        "Say it specifically: a street address beats 'somewhere in the city.'",
        "Naming the feeling precisely turns down the alarm's gain.",
        "Permitted anxiety is smaller anxiety — the war against it enlarges it.",
        "Channel the mobilized energy: walk, prepare, rehearse — then close the list.",
        "All three are loop-closing moves: the messenger stops shouting once heard.",
        "What remains after the message is received is usually much smaller.",
    ],
    "requirements": [
        "One specific naming: the feeling, the trigger, the reason",
        "One safe person or place to drop the performance",
        "One physical channel for the next anxious surge",
    ],
    "standards": [
        "Affect labeling and neural down-regulation (Lieberman et al., 2007)",
        "Expressive suppression costs (Gross, 2002)",
        "Behavioral activation and preparation effects",
    ],
    "citations": [
        "Lieberman, M. D., et al. Putting Feelings Into Words. Psychological Science; 2007.",
        "Gross, J. J. Psychophysiology; 2002.",
        "Barlow, D. H. Anxiety and Its Disorders. 2nd ed. Guilford Press; 2002.",
    ],
    "sig_lens": (
        "Through the Signature lens, healthy expression is the lookout's "
        "proper report — clear, specific, delivered to the captain, then "
        "stood down. The Signature reader trains this discipline: name the "
        "contact precisely, deliver it once, then give the mobilized crew "
        "their orders. A messenger heard is a messenger quieted. The ship "
        "runs on received messages, not on shouting."
    ),
},
{
    "key": "anxiety-unhealthy",
    "name": "Unhealthy Expression: Bottling Up or Boiling Over",
    "group": "Healthy Expression",
    "ladder_rank": 27,
    "ladder_tier": "advanced",
    "description": (
        "Anxiety denied its exits takes two costly roads: the bottle and the "
        "boil. Bottling up: the feeling is pushed down, the mask is held, "
        "'I'm fine' is performed on schedule. The costs are quiet but compounding. "
        "Physiologically, suppression keeps arousal elevated — the body stays "
        "mobilized while the mind insists nothing is happening, which is "
        "exhausting. Psychologically, the unfaced forecast keeps running in "
        "the background, uncorrected by reality, growing stranger and darker "
        "for lack of daylight. Socially, the bottled person becomes harder to "
        "reach — present but absent — and the relationships pay. And the bottle "
        "always leaks or bursts: the snap at the wrong person, the 2 a.m. "
        "spiral, the sudden tears over something small. Boiling over: the "
        "feeling floods the controls. The frantic over-preparation that ruins "
        "the night before, the reassurance-seeking that exhausts the people "
        "around, the panicked decisions, the lashing out — the anxiety-"
        "irritation blend at full volume. The costs are loud: burned bridges, "
        "regretted messages, decisions made to end the feeling rather than "
        "serve the future. Both roads share a root error: treating the "
        "messenger as the enemy. The bottle shoots the messenger; the boil "
        "lets the messenger seize the ship. The middle road — receive the "
        "message, answer it, stand the messenger down — is the only one that "
        "closes the loop. Most people have a default road; knowing yours is "
        "the first step off it."
    ),
    "how_it_works": (
        "Bottling works through expressive and cognitive suppression: the "
        "voluntary systems clamp down on the feeling's expression while the "
        "threat system keeps firing underneath. Suppression reliably raises "
        "physiological arousal even as it hides the outward signs — the "
        "person looks calm while the body runs hot, which is why bottlers "
        "often report exhaustion without visible cause. Uncorrected forecasts "
        "drift darker because the simulation engine, denied real-world "
        "feedback, iterates on its own output — a closed loop that "
        "catastrophizes by recursion. Boiling over is the same loop at "
        "unsustainable gain: arousal exceeds the regulatory capacity of the "
        "prefrontal systems, and behavior becomes threat-driven and urgent. "
        "Reassurance-seeking escalates through habituation — each dose soothes "
        "less, so the dose rises. Panicked decisions are avoidance at speed: "
        "any choice that ends the aversive state. Both roads maintain the "
        "disorder they express: bottling preserves the loop by preventing "
        "disconfirmation, boiling preserves it by preventing regulation. The "
        "middle road works because it is the only path that updates the "
        "appraisal — the actual mechanism that winds the loop down."
    ),
    "key_points": [
        "The bottle: suppression looks calm while the body runs hot — exhaustion without visible cause.",
        "Uncorrected forecasts drift darker in the dark — the loop catastrophizes by recursion.",
        "The boil: arousal exceeds regulatory capacity; behavior goes urgent and threat-driven.",
        "Reassurance habituates: each dose soothes less, so the dose keeps rising.",
        "Both roads treat the messenger as the enemy — one shoots it, one lets it seize the ship.",
        "Know your default road; it is the first step off it.",
    ],
    "requirements": [
        "Your default road, named honestly: bottle or boil",
        "One cost from each road you have personally paid",
        "One middle-road move to practice this week",
    ],
    "standards": [
        "Suppression: physiological costs (Gross, 2002)",
        "Reassurance habituation dynamics",
        "Regulatory capacity and arousal overload",
    ],
    "citations": [
        "Gross, J. J. Emotion Regulation: Affective, Cognitive, and Social Consequences. Psychophysiology; 2002.",
        "Butler, E. A., et al. The Social Consequences of Expressive Suppression. Emotion; 2003.",
        "Barlow, D. H. Anxiety and Its Disorders. 2nd ed. Guilford Press; 2002.",
    ],
    "sig_lens": (
        "Through the Signature lens, the bottle is a messenger locked below "
        "deck — still shouting through the floorboards, driving the crew mad "
        "with the muffled noise. The boil is the messenger handed the wheel. "
        "The Signature reader does neither: he brings the messenger to the "
        "bridge, takes the report, issues the orders, and sends the messenger "
        "below to rest. Command is the middle road."
    ),
},
{
    "key": "anxiety-practices",
    "name": "Everyday Practices: Small Habits That Keep Anxiety in Balance",
    "group": "Healthy Expression",
    "ladder_rank": 28,
    "ladder_tier": "advanced",
    "description": (
        "Anxiety is managed the way fitness is built: not in heroic episodes "
        "but in small daily practices that keep the system in balance. The "
        "breath practice: a few slow exhales — longer out than in — whenever "
        "the loop starts. It is not mysticism; the long exhale is the body's "
        "own stand-down signal, and it works in under a minute. The worry "
        "window: give the forecasting loop a scheduled appointment — fifteen "
        "minutes a day to worry on paper, deliberately — and outside the "
        "window, worries get deferred to it. The loop, given its hearing, "
        "quiets between sessions. The preparation close: turn open loops into "
        "closed plans. Anxiety feeds on the unprepared-for; a concrete next "
        "step, written down, is worth an hour of rehearsal. The body budget: "
        "regular sleep hours, real meals, daily movement — the stores guarded, "
        "because a depleted system forecasts darker. The stimulant audit: "
        "notice what caffeine, alcohol, and the 1 a.m. news scroll do to the "
        "next day's volume, and adjust like an engineer, not a moralist. The "
        "exposure habit: small, deliberate approaches to the mildly avoided "
        "things — the call made, the route taken — which teach the system, "
        "one disconfirmation at a time, that the forecast was overstated. The "
        "evening review: two minutes noting what the anxiety predicted today "
        "versus what happened — the ledger that gradually corrects the "
        "forecaster's bias. None of these is dramatic. Together they are a "
        "maintenance schedule for the forecast machinery — the daily seamanship "
        "that keeps small weather from becoming a storm."
    ),
    "how_it_works": (
        "Each practice targets a link in the loop. Slow exhales stimulate the "
        "vagus nerve and the parasympathetic branch — the physiological "
        "stand-down pathway — directly lowering arousal regardless of the "
        "thoughts. The worry window works through stimulus control: confining "
        "worry to a time and place breaks the association between every "
        "context and rehearsal, and scheduled, written worry habituates faster "
        "than scattered worry. The preparation close updates the appraisal: a "
        "concrete plan reduces uncertainty, which is the loop's fuel. The body "
        "budget raises the appraisal threshold — a rested, fed, moved body "
        "appraises fewer things as threatening. The stimulant audit removes "
        "false arousal that the mind would otherwise misattribute. Small "
        "exposures work through inhibitory learning: each approach without "
        "catastrophe writes a competing 'safe' association that weakens the "
        "threat prediction. The evening review corrects the forecaster's "
        "calibration through tracked base rates — the mind learns, from its "
        "own ledger, how often the forecast was wrong. Small, repeated, "
        "mechanical: that is why they compound."
    ),
    "key_points": [
        "Slow exhales are the body's own stand-down signal — under a minute.",
        "The worry window: fifteen scheduled minutes; the loop quiets between sessions.",
        "Turn open loops into closed plans — a written next step beats an hour of rehearsal.",
        "Guard the body budget: sleep, meals, movement raise the threat threshold.",
        "Small deliberate approaches teach the system the forecast was overstated.",
        "The evening ledger corrects the forecaster with its own track record.",
    ],
    "requirements": [
        "One practice chosen — the smallest one you will actually do",
        "A week of doing it before judging it",
        "The ledger: predicted vs happened, two minutes nightly",
    ],
    "standards": [
        "Stimulus control for worry (Borkovec)",
        "Inhibitory learning in exposure (Craske)",
        "Sleep hygiene and arousal threshold literature",
    ],
    "citations": [
        "Borkovec, T. D., et al. Stimulus Control Applications to Worry. Behavior Therapy; 1983.",
        "Craske, M. G., et al. Maximizing Exposure Therapy. Behaviour Research and Therapy; 2014.",
        "Harvey, A. G. Behaviour Research and Therapy; 2002.",
    ],
    "sig_lens": (
        "Through the Signature lens, these practices are the daily orders — "
        "the standing routine that keeps any ship ready: gauges checked, "
        "stores guarded, crew drilled, log kept. The Signature reader does "
        "not wait for the storm to practice seamanship. He runs the drills in "
        "calm water, so that when the forecast turns, the crew already knows "
        "its stations."
    ),
},
{
    "key": "anxiety-reading",
    "name": "Reading the Signs: Anxiety Cues in Other People",
    "group": "Recognizing Anxiety in Others",
    "ladder_rank": 29,
    "ladder_tier": "advanced",
    "description": (
        "Reading anxiety in others is a practical kindness — it lets you "
        "respond to what is actually happening instead of the surface. Start "
        "with the face: the worried brow that stays knitted, the eyes doing "
        "their quick sweeps, the mouth pressed thin, the smile that does not "
        "reach the eyes. Then the body: the shoulder that will not drop, the "
        "hands in motion — tapping, picking, phone-checking — the stillness "
        "that is too still, the weight shifting foot to foot. Then the voice: "
        "pitch a half-step up, pace hurried or oddly paused, the laugh that "
        "arrives too fast. Then the words: the 'what ifs,' the hedging, the "
        "reassurance questions in new costumes, the preemptive apologies. Then "
        "the behavior: the declined invitation with a thin excuse, the "
        "over-preparation, the early arrival to scout the room, the early "
        "departure, the sudden busyness when a topic turns uncertain. Read the "
        "clusters, not single signs — one fidget means nothing; the brow plus "
        "the hands plus the hedging plus the early exit means the loop is "
        "running. Calibrate for the person: some people broadcast anxiety "
        "loudly, others run silent — the quiet ones show it in withdrawal and "
        "over-control rather than fidgeting. And hold the reading lightly. You "
        "are not diagnosing; you are noticing, the way you would notice someone "
        "shivering and think 'they might be cold.' The point of reading is "
        "never to announce your finding — 'you seem anxious' lands as an "
        "accusation. The point is to adjust yourself: slow down, make room, "
        "offer the steady presence that anxious systems borrow courage from."
    ),
    "how_it_works": (
        "Reading works because anxiety's signals are largely involuntary and "
        "therefore honest — the threat system broadcasts through fast "
        "pathways that deliberate control cannot fully suppress. Observers "
        "detect the pattern through configural perception: the brain does not "
        "read single cues but whole configurations, which is why clusters are "
        "reliable while isolated signs are noisy. Individual calibration is "
        "necessary because expressive style varies — high self-monitors mask "
        "more, low self-monitors leak more — so the baseline for each person "
        "must be learned before deviations mean anything. The 'hold it "
        "lightly' rule reflects the base-rate problem: many anxiety cues "
        "overlap with tiredness, excitement, or habit, so any single reading "
        "is probabilistic. The adjustment response — slowing down, making "
        "room — works through co-regulation: calm, unhurried presence from "
        "another person measurably lowers the observer's arousal via the same "
        "social-safety pathways that raise it under threat. You lend your "
        "nervous system as ballast."
    ),
    "key_points": [
        "Read clusters, not single signs — the brow plus hands plus hedging plus early exit.",
        "Face, body, voice, words, behavior: five channels, one pattern.",
        "Calibrate per person — loud broadcasters vs silent runners.",
        "Hold the reading lightly: you are noticing, not diagnosing.",
        "Never announce the finding — 'you seem anxious' lands as accusation.",
        "Adjust yourself: slow down, make room, lend your calm as ballast.",
    ],
    "requirements": [
        "One person's baseline learned before judging deviations",
        "Practicing cluster-reading in low-stakes settings",
        "A personal rule: notice, adjust yourself, never announce",
    ],
    "standards": [
        "Configural emotion perception literature",
        "Co-regulation and social baseline theory (Beckes & Coan)",
        "Expressive style and self-monitoring differences",
    ],
    "citations": [
        "Beckes, L., & Coan, J. A. Social Baseline Theory. Social and Personality Psychology Compass; 2011.",
        "Ekman, P. Emotions Revealed. 2nd ed. Holt; 2007.",
        "Hatfield, E., et al. Emotional Contagion. Cambridge University Press; 1994.",
    ],
    "sig_lens": (
        "Through the Signature lens, reading others is standing the night "
        "watch for the fleet — scanning not your own horizon but your "
        "neighbor's, and noting whose lamp is burning worried-bright. The "
        "Signature reader never shouts his reading across the water. He simply "
        "trims his own sails to give the other ship steadier wind — slowing, "
        "steadying, making room — until their lamp burns calm again."
    ),
},
{
    "key": "anxiety-support",
    "name": "What to Say and Do When Someone Near You Is Anxious",
    "group": "Recognizing Anxiety in Others",
    "ladder_rank": 30,
    "ladder_tier": "advanced",
    "description": (
        "When someone near you is anxious, you become part of their weather — "
        "and the right moves are simpler than people think. First, regulate "
        "yourself: slow your own pace, lower your voice half a notch, unhurry "
        "your movements. Anxious systems borrow calm from nearby calm systems; "
        "your steadiness is the intervention. Second, acknowledge without "
        "amplifying: 'This sounds like a lot' or 'Of course this has you on "
        "edge' — naming their state as understandable, not as a problem to fix. "
        "Third, ask what would help, and offer concrete options: 'Do you want "
        "to talk it through, make a plan, or just sit for a bit' — the anxious "
        "mind struggles with open-ended choices, so options beat questions. "
        "Fourth, help close one loop: pick the smallest preparable piece and "
        "do it together — the email drafted, the bag packed, the route checked. "
        "Action is the antidote to rehearsal. Fifth, stay for the fade: do not "
        "declare victory the moment they calm; the aftershock is real, and "
        "your continued ordinary presence is what lets the system fully stand "
        "down. What to say, in plain phrases: 'I'm here.' 'Take your time.' "
        "'What's the actual worry underneath?' 'Let's handle one piece.' 'It "
        "makes sense you feel this way.' What matters most is not the script "
        "but the signal underneath it: I am not frightened by your feeling, I "
        "am not in a hurry to fix it, and I am not going anywhere. Anxious "
        "people are braced for judgment and abandonment; your calm, staying "
        "presence is the direct refutation of both."
    ),
    "how_it_works": (
        "Support works through co-regulation and appraisal assistance. Your "
        "slowed pace and lowered voice provide the anxious person's threat "
        "system with safety evidence through the fastest channel — another "
        "mammal's calm physiology is read as 'the tribe is not alarmed, so "
        "perhaps I need not be.' Acknowledgment without amplification validates "
        "the appraisal ('this is genuinely uncertain') while refusing to add "
        "fuel — validation lowers the secondary alarm about having the "
        "feeling. Concrete options work because open-ended questions demand "
        "exactly the executive resources the anxious mind has least available; "
        "options outsource the structuring. Closing one loop together updates "
        "the appraisal through real preparation and through social proof — "
        "'we handled a piece' is stronger evidence than 'I thought about a "
        "piece.' Staying for the fade matters because premature 'all better' "
        "signals can re-trigger the loop ('they think I should be fine, but "
        "I'm not — something must be wrong with me'); continued ordinary "
        "presence lets the parasympathetic completion run its course. The "
        "meta-signal — not frightened, not hurried, not leaving — directly "
        "counters the anxious system's two deepest sub-fears: that the "
        "feeling is dangerous and that it will cost connection."
    ),
    "key_points": [
        "Regulate yourself first — your steadiness is the intervention.",
        "Acknowledge without amplifying: understandable, not a problem to fix.",
        "Offer concrete options; the anxious mind cannot do open-ended well.",
        "Close one loop together — action is the antidote to rehearsal.",
        "Stay for the fade; premature 'all better' can re-trigger the loop.",
        "The meta-signal: not frightened, not hurried, not going anywhere.",
    ],
    "requirements": [
        "Your own calm practiced before you lend it",
        "Three plain phrases ready, in your own words",
        "The discipline to stay past the first calm",
    ],
    "standards": [
        "Co-regulation and social baseline theory (Beckes & Coan, 2011)",
        "Validation in emotion support literature",
        "Interpersonal emotion regulation models",
    ],
    "citations": [
        "Beckes, L., & Coan, J. A. Social Baseline Theory. Social and Personality Psychology Compass; 2011.",
        "Zaki, J., & Williams, W. C. Interpersonal Emotion Regulation. Emotion; 2013.",
        "Barlow, D. H. Anxiety and Its Disorders. 2nd ed. Guilford Press; 2002.",
    ],
    "sig_lens": (
        "Through the Signature lens, supporting an anxious person is coming "
        "alongside in heavy weather — matching speed, holding station, no "
        "sudden moves. The Signature reader does not tow the other ship or "
        "shout instructions across the waves. He holds steady off their beam, "
        "signals 'I am here,' helps work one line at a time, and stays until "
        "both ships are through. Presence is the seamanship."
    ),
},
{
    "key": "anxiety-mistakes",
    "name": "What Not to Do: Common Mistakes That Make Anxiety Worse",
    "group": "Recognizing Anxiety in Others",
    "ladder_rank": 31,
    "ladder_tier": "advanced",
    "description": (
        "Good intentions misfire around anxiety with depressing regularity. "
        "Here are the classic mistakes, so you can avoid paying their tuition. "
        "'Just relax' / 'calm down': the most useless sentence in the language. "
        "It asks the person to do the one thing the feeling prevents, and adds "
        "a layer of failure for not managing it. 'There's nothing to worry "
        "about': it argues with the forecast instead of hearing it. The "
        "anxious system reads dismissal as evidence that it must shout louder "
        "to be taken seriously. Logic-bombing: the twenty-minute lecture on "
        "why the worry is statistically unfounded. At high volume the thinking "
        "brain is crowded out — the lecture cannot land, and the lecturer's "
        "frustration becomes new threat material. False reassurance on repeat: "
        "'it'll be fine, it'll be fine' — each dose soothes less and teaches "
        "the system that relief comes from others, deepening dependence. "
        "Problem-solving too early: jumping to fix-it mode before the feeling "
        "has been acknowledged. The anxious person hears 'your feeling is an "
        "obstacle to my solution' and the loop tightens. Matching their "
        "urgency: getting frantic alongside them — now there are two alarmed "
        "systems and no ballast. Taking it personally: reading their "
        "irritability or withdrawal as being about you, and responding with "
        "hurt or counter-attack — the anxiety-irritation blend's favorite "
        "trap. And the quietest mistake: disappearing. Withdrawing because "
        "their anxiety is uncomfortable to be around confirms the system's "
        "deepest fear — that the feeling costs connection. The pattern across "
        "all of these: they respond to the noise instead of the signal. The "
        "signal always wants the same three things: to be heard, to be "
        "answered with something concrete, and to be given time."
    ),
    "how_it_works": (
        "Each mistake fails through a specific mechanism. 'Calm down' fails "
        "because it demands top-down regulation from systems currently "
        "occupied by the alarm — like ordering someone to lift with a broken "
        "arm — and the failure becomes a secondary appraisal ('I can't even "
        "calm down'), adding fuel. Dismissal fails because invalidation "
        "raises the stakes of being heard; the system escalates expression to "
        "achieve acknowledgment. Logic-bombing fails on timing: cognitive "
        "restructuring requires available working memory, which high arousal "
        "has captured — the facts literally cannot be processed until the "
        "body settles. Repeated false reassurance fails through habituation "
        "and dependency: the soothing effect decays while the contingency "
        "('I need them to settle me') strengthens. Early problem-solving "
        "fails because it skips the acknowledgment step the appraisal needs "
        "before it can update — unheard warnings do not stand down. Matching "
        "urgency fails through emotional contagion: two escalated systems "
        "resonate. Taking it personally fails by converting their threat "
        "response into a relationship threat, doubling the alarm. Disappearing "
        "fails by confirming abandonment expectancy — the cost the system "
        "feared most. All seven share the error of answering the expression "
        "rather than the appraisal beneath it."
    ),
    "key_points": [
        "'Calm down' demands regulation from occupied systems — and adds failure-fuel.",
        "Dismissal makes the system shout louder to be heard.",
        "Logic cannot land while working memory is captured — settle the body first.",
        "Repeated 'it'll be fine' habituates and deepens dependence.",
        "Fix-it mode before acknowledgment reads as 'your feeling is my obstacle.'",
        "Never match their urgency, take it personally, or disappear.",
    ],
    "requirements": [
        "One mistake you have made — named, forgiven, retired",
        "The pause before responding: signal or noise",
        "Remembering the three wants: heard, answered concretely, given time",
    ],
    "standards": [
        "Invalidation effects in emotion literature",
        "Reassurance habituation and dependency",
        "Emotional contagion under stress",
    ],
    "citations": [
        "Zaki, J., & Williams, W. C. Interpersonal Emotion Regulation. Emotion; 2013.",
        "Butler, E. A., et al. The Social Consequences of Expressive Suppression. Emotion; 2003.",
        "Barlow, D. H. Anxiety and Its Disorders. 2nd ed. Guilford Press; 2002.",
    ],
    "sig_lens": (
        "Through the Signature lens, these mistakes are bad seamanship in "
        "company — shouting at the struggling ship, lecturing its captain on "
        "wave statistics, or sailing off and leaving it. The Signature reader "
        "holds station instead: no shouting across the water, no premature "
        "towing, no abandoning. Read the signal under the noise, answer it "
        "plainly, and stay until the sea settles."
    ),
},
{
    "key": "anxiety-map",
    "name": "The Anxiety Neighborhood: Related Emotions and Close Cousins",
    "group": "Emotion Mixes and Simulation",
    "ladder_rank": 32,
    "ladder_tier": "advanced",
    "description": (
        "Anxiety lives in a crowded neighborhood, and telling the neighbors "
        "apart is a genuine skill. Anxiety vs fear: the timing test — threat "
        "here now is fear; threat possibly later is anxiety. Same body, "
        "different clock. Anxiety vs worry: worry is the mental half — the "
        "talky thought loop — while anxiety is the full package with the body "
        "included. You can worry without the pounding heart; you cannot be "
        "anxious without it. Anxiety vs nervousness: nervousness is anxiety's "
        "mild, short-lived form — the pre-game jitters. Same machinery, lower "
        "volume, quicker fade. Anxiety vs dread: dread has a specific dark "
        "object — the diagnosis, the verdict — while anxiety can be free-"
        "floating, attached to nothing nameable. Anxiety vs stress: stress is "
        "the load — too much demand on the system — while anxiety is the "
        "forecast about the load. They travel together but answer different "
        "questions. Anxiety vs excitement: the body twins. Both are arousal "
        "aimed at the future; the difference is the appraisal — threat vs "
        "opportunity. Reappraising 'I am anxious' as 'I am excited' sometimes "
        "works precisely because the body cannot tell them apart. Anxiety vs "
        "guilt: guilt looks backward at what was done; anxiety looks forward "
        "at what might happen. They meet in the middle over future "
        "consequences of past actions. The opposites, for orientation: calm "
        "is the quiet forecast — the all-clear. Confidence is the appraisal "
        "that preparation is sufficient. Boredom is the system's idleness — "
        "though as the surprise triggers showed, idleness can invite anxiety "
        "back in. The map's purpose is precision. Each neighbor wants a "
        "different response, and mislabeling sends the wrong crew to the "
        "wrong deck."
    ),
    "how_it_works": (
        "Neighbor distinctions rest on the appraisal dimensions that generate "
        "each emotion. Timing (present vs future threat) separates fear from "
        "anxiety — the appraisal's temporal focus, not the body, which is "
        "shared. The cognitive-somatic split separates worry (verbal-linguistic "
        "rehearsal) from anxiety (full autonomic mobilization plus rehearsal); "
        "they dissociate because the thought loop can run without triggering "
        "full mobilization. Intensity and duration separate nervousness (low, "
        "brief) from anxiety proper. Object specificity separates dread "
        "(specific anticipated harm) from free-floating anxiety (uncertainty "
        "without a fixed object). Demand vs forecast separates stress "
        "(appraisal of current load exceeding resources) from anxiety "
        "(appraisal of future threat). Valence of the future separates "
        "excitement (positive anticipation) from anxiety (negative) — with "
        "identical arousal, which is why reappraisal between them can work. "
        "Temporal direction separates guilt (past-focused) from anxiety "
        "(future-focused). Precision matters functionally: fear wants immediate "
        "action, anxiety wants preparation, excitement wants approach, guilt "
        "wants repair — and applying fear's response to anxiety's problem is "
        "the most common mislabeling error."
    ),
    "key_points": [
        "Fear vs anxiety: the timing test — threat now vs threat later.",
        "Worry is the mental half; anxiety is the full package with the body.",
        "Nervousness is low-volume, short-lived anxiety; dread has a specific dark object.",
        "Stress is the load; anxiety is the forecast about the load.",
        "Excitement is anxiety's body twin — same arousal, opposite appraisal.",
        "Each neighbor wants a different response; mislabeling sends the wrong crew.",
    ],
    "requirements": [
        "Three recent feelings, each placed on the map",
        "The timing test applied to your most common confusion",
        "Trying the excitement reappraisal once, as an experiment",
    ],
    "standards": [
        "Appraisal-dimension differentiation of emotions",
        "Cognitive vs somatic anxiety components",
        "Reappraisal between high-arousal states (Brooks, 2014)",
    ],
    "citations": [
        "Brooks, A. W. Get Excited: Reappraising Pre-Performance Anxiety. Journal of Experimental Psychology; 2014.",
        "Lazarus, R. S. Emotion and Adaptation. Oxford University Press; 1991.",
        "Barlow, D. H. Anxiety and Its Disorders. 2nd ed. Guilford Press; 2002.",
    ],
    "sig_lens": (
        "Through the Signature lens, the neighborhood map is the coastal chart "
        "— every inlet named, every look-alike headland distinguished, so the "
        "captain never mistakes one harbor for another in the fog. The "
        "Signature reader keeps his chart current and consults it before "
        "giving orders. Right name, right crew, right deck — that is all "
        "navigation ever is."
    ),
},
{
    "key": "anxiety-blends",
    "name": "Emotion Mixes: Anxiety Blended With Other Emotions",
    "group": "Emotion Mixes and Simulation",
    "ladder_rank": 33,
    "ladder_tier": "advanced",
    "description": (
        "Pure anxiety is rare; the blends are the daily reality. In the "
        "Plutchik spirit — where neighboring emotions combine into dyads — "
        "here is what anxiety makes with its most frequent partners. "
        "Anxiety + irritation = the edgy blend (record 8): dread with a short "
        "fuse, the snap at small frictions, trapped preparation energy "
        "leaking into the present. Anxiety + sadness = the heavy blend: the "
        "future looks bad and the past feels heavy — low energy, tearful "
        "edges, the 'what's the point' undertow beneath the 'what if.' The "
        "body is tired, the forecast is dark, motivation drains from both "
        "ends. Anxiety + excitement = the electric blend: the job interview, "
        "the first date, the launch day — threat and opportunity appraised "
        "simultaneously. It feels like buzzing: the same arousal read two "
        "ways at once, which is why these moments are both thrilling and "
        "nauseating. Anxiety + shame = the shrinking blend: the worry that "
        "everyone can see you worrying — the blush at the blush, the fear of "
        "the trembling hands being noticed. It drives hiding, which drives "
        "more anxiety about the hiding. Anxiety + anger = the fight blend: "
        "the forecast turns combative — rehearsing confrontations, jaw set, "
        "the urge to attack the uncertain thing preemptively. Each blend has "
        "its own weather and its own handling. The edgy blend wants the "
        "anxiety half addressed. The heavy blend wants one small doable thing "
        "to break the paralysis. The electric blend wants the excitement half "
        "named and ridden. The shrinking blend wants the hiding permitted to "
        "stop. The fight blend wants the rehearsal redirected into real "
        "preparation. The master skill is blend literacy: feeling the mix, "
        "naming both ingredients, and answering each half in its own language."
    ),
    "how_it_works": (
        "Blends form because the appraisal system can hold two appraisals at "
        "once — the future can be simultaneously threatening and promising, "
        "the self simultaneously exposed and judged. Each appraisal drives "
        "its own response tendencies, and the body runs the shared arousal "
        "underneath both, which is why blends feel like one big feeling "
        "rather than two small ones. The specific blends follow from appraisal "
        "combinations: threat + blocked goals = anxiety-irritation; threat + "
        "loss = anxiety-sadness; threat + opportunity = anxiety-excitement; "
        "threat + social exposure = anxiety-shame; threat + violation = "
        "anxiety-anger. Handling differs because each partner emotion wants "
        "something different: irritation wants obstacle removal, sadness wants "
        "comfort and activation, excitement wants approach, shame wants "
        "concealment (which must be gently refused), anger wants confrontation "
        "(which must be redirected). Blend literacy works through "
        "decomposition: naming both ingredients lets the person apply two "
        "targeted responses instead of one confused one — and the anxiety half "
        "almost always responds to preparation, regardless of its partner."
    ),
    "key_points": [
        "Pure anxiety is rare; blends are the daily reality.",
        "Edgy (irritation), heavy (sadness), electric (excitement), shrinking (shame), fight (anger).",
        "Blends feel like one big feeling because the body runs shared arousal underneath.",
        "Each partner wants something different — name both ingredients.",
        "The anxiety half almost always answers to preparation, whatever the partner.",
        "Blend literacy: feel the mix, name both, answer each in its own language.",
    ],
    "requirements": [
        "Your three most frequent blends, named",
        "One blend handled by its two halves this week",
        "Noticing which partner shows up with your anxiety most",
    ],
    "standards": [
        "Plutchik dyad theory (1980)",
        "Mixed-emotion appraisal models",
        "Blended affect in daily experience sampling",
    ],
    "citations": [
        "Plutchik, R. Emotion: A Psychoevolutionary Synthesis. Harper & Row; 1980.",
        "Larsen, J. T., et al. Can People Feel Happy and Sad at the Same Time? Journal of Personality and Social Psychology; 2001.",
        "Barlow, D. H. Anxiety and Its Disorders. 2nd ed. Guilford Press; 2002.",
    ],
    "sig_lens": (
        "Through the Signature lens, blends are combined weather — wind with "
        "rain, swell with fog — and the Signature reader never navigates "
        "combined weather as if it were one thing. He names each system, "
        "answers each in its own seamanship, and holds the course through "
        "both. Two weathers, two answers, one steady ship."
    ),
},
{
    "key": "anxiety-simulation",
    "name": "Full Simulation: Anxiety From Trigger to Resolution",
    "group": "Emotion Mixes and Simulation",
    "ladder_rank": 34,
    "ladder_tier": "advanced",
    "description": (
        "The showcase: one full arc, scene by scene, everything in this "
        "database working together. Scene 1 — Onset: Maya has a performance "
        "review on Friday. It is Monday. The calendar notification appears "
        "while she is making lunch, and the flicker starts — stomach tightens, "
        "breath shortens. The forecast machinery wakes. Scene 2 — Build: By "
        "Wednesday the loop is fully engaged. Scenarios multiply: the critical "
        "comment, the stalled promotion, the mortgage math. Her shoulders have "
        "been up for two days; her jaw aches. She checks her work obsessively, "
        "rehearses answers in the shower, snaps at her partner over dishes — "
        "the anxiety-irritation blend leaking into the present. Sleep is "
        "shallow; the 3 a.m. review session runs without her permission. "
        "Scene 3 — Peak: Thursday night. The cascade is at full stretch — "
        "review to promotion to mortgage to the children's college to the "
        "meaning of her career. Her hands shake holding her phone. She writes "
        "the chain audit on paper and stares at link six: absurd, and suddenly "
        "visible as absurd. She closes the laptop, does the slow exhales, and "
        "lets the wave crest without steering into it. Scene 4 — Turning "
        "point: Friday morning she names it precisely: 'I am anxious about "
        "the review because the criteria are unclear and my manager is "
        "unpredictable.' The vague dread becomes two preparable items. She "
        "prepares her accomplishments list and three questions about criteria "
        "— the preparation close. The loop, answered, begins to quiet. "
        "Scene 5 — Easing: The review happens. It is fine — genuinely fine. "
        "Two compliments, one growth area, criteria clarified for next "
        "quarter. Walking out, her shoulders drop for the first time in four "
        "days. The body lags the news by an hour; she gives it the hour. "
        "Scene 6 — Settling: Friday evening. Dinner tastes like dinner. She "
        "runs the ledger: predicted catastrophe, actual ordinary Friday. The "
        "forecaster's bias gets one more correction written into the log. An "
        "aftershock flickers on Sunday — 'what about next quarter' — and she "
        "recognizes the warm circuit for what it is, smiles, and lets it pass. "
        "The simulation is complete: trigger to resolution, the whole ladder "
        "in one voyage."
    ),
    "how_it_works": (
        "The showcase integrates every mechanism in the database. Onset shows "
        "appraisal firing the first arousal pulse. Build shows the feedback "
        "loop, attention capture, the anxiety-irritation blend, sleep "
        "disruption, and maintenance behaviors (checking, rehearsal, "
        "snapping). Peak shows the cascade at full stretch and the crest of "
        "the arousal curve — plus the first skilled intervention: the chain "
        "audit externalizing the loop and slow exhales engaging the "
        "parasympathetic brake. The turning point shows affect labeling and "
        "the preparation close updating the appraisal — the loop's designed "
        "exit. Easing shows forecast error (vividness vs probability) and the "
        "body's lagged stand-down. Settling shows the ledger correcting "
        "calibration and the aftershock recognized as a warm circuit rather "
        "than a new emergency. The arc demonstrates the central thesis: "
        "anxiety is a forecasting loop, and every phase has its answer — "
        "preparation at onset, loop-breaking at build, seamanship at peak, "
        "naming and closing at the turn, rest at the fade, and logging at the "
        "end so the next voyage starts with a better chart."
    ),
    "key_points": [
        "The full arc in one voyage: onset, build, peak, turning point, easing, settling.",
        "Every record in the ladder appears as a working part of the story.",
        "The chain audit and slow exhales break the peak from the inside.",
        "Precise naming plus the preparation close turn the loop at its hinge.",
        "The body lags the good news — give it the hour.",
        "The ledger at the end is how the forecaster learns.",
    ],
    "requirements": [
        "Reading the whole simulation in one sitting",
        "Mapping your own last full arc onto the six scenes",
        "Writing your ledger entry for it",
    ],
    "standards": [
        "Integrated anxiety episode modeling",
        "Affect labeling + preparation-close intervention sequence",
        "Calibration learning through outcome ledgers",
    ],
    "citations": [
        "Barlow, D. H. Anxiety and Its Disorders. 2nd ed. Guilford Press; 2002.",
        "Lieberman, M. D., et al. Putting Feelings Into Words. Psychological Science; 2007.",
        "Gilbert, D. T., & Wilson, T. D. Prospection: Experiencing the Future. Science; 2007.",
    ],
    "sig_lens": (
        "Through the Signature lens, the full simulation is the completed "
        "voyage — logged from first flicker to final settling, every watch "
        "noted, every intervention recorded, the chart improved for next "
        "time. The Signature reader files it with the others. Enough voyages "
        "logged honestly, and no weather surprises him: he has sailed it "
        "before, he knows its shape, and he knows, always, that every wave "
        "breaks."
    ),
},
]
