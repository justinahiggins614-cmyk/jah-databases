#!/usr/bin/env python3
"""Full record entries for the Calm Emotion databases
(Manon's 16:15 orders, emotion series batch 1).

34 ladder-ordered full entries (ladder_rank 1-10, non-decreasing;
ladder_tier foundations -> compounded -> advanced). Public entries are
real, fact-checked psychology of calm (public-harvest): definition,
family placement, intensity volumes, first-person simulation, body
signals, facial expression, triggers, behavior, healthy expression,
recognition in others, related emotions and mixes, and a full
behavioral simulation. Descriptive and educational only - never
diagnosing real people, never labeling any real person, and no
therapeutic advice beyond general, safe, everyday guidance.

Standard references used across entries: Ekman and Friesen FACS 1978;
Ekman 1999 on basic emotions; Plutchik 1980; Russell 1980 circumplex;
Lazarus 1991; Lazarus and Folkman 1984; Frijda 1986; Scherer 2005;
Barrett 2017; Izard 1992; Darwin 1872; Fredrickson 1998;
Benson 1975 (the relaxation response); Kabat-Zinn 1990 (mindfulness);
Porges 2011 (polyvagal theory); APA Dictionary of Psychology.

Signature entries (sig_lens per entry) reframe each topic as his
original Signature Calm Method: calm as the home frequency of the
system - the steady green board, the engine at idle holding ready;
calm is not the absence of power, it is power held in reserve; the
covenant that the system answers only when commanded. Clearly labeled
Signature-made, never presented as authentic public record.
"""

SIG_TAIL = ("Signature original - his original Signature Calm Method: calm "
            "as the home frequency of the system - the steady green board, "
            "the engine at idle holding ready; power held in reserve, the "
            "covenant that the system answers only when commanded. Clearly "
            "labeled Signature-made, never presented as authentic public "
            "record.")

ENTRIES = [
    # ------------------------------------------------- 1. definition
    {
        "key": "calm_definition",
        "name": "What Calm Is: A Plain-Language Definition",
        "group": "What the Emotion Is",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Calm is the feeling of steady quiet inside - the sense that "
            "nothing is urgent, nothing is threatening, and the mind can "
            "rest its hands open on the table. In plain words, calm is the "
            "body and mind agreeing that the moment is safe and manageable. "
            "It is not emptiness and not numbness; it is a positive state "
            "with a texture: breathing slows, the shoulders drop, the "
            "thoughts stop racing and start walking. Psychologists describe "
            "calm as a low-arousal, pleasant state - low in energy, high in "
            "ease. It can arrive on its own, like the quiet after a storm "
            "passes, or it can be cultivated, the way a room can be tidied. "
            "A calm person is not necessarily doing nothing; surgeons, "
            "pilots, and athletes perform their hardest work in calm. The "
            "key difference between calm and other quiet states is choice "
            "and readiness: a calm person could act in a heartbeat but "
            "chooses stillness, while a numb person cannot act and an "
            "anxious person cannot stop. Everyone knows calm from ordinary "
            "moments - the deep breath after finishing a hard task, the "
            "hush of a house at night, the pause before something good "
            "begins. This database describes the emotion from every angle - "
            "what it is, how it feels, how it shows, and how it can be "
            "kept in balance - purely as education and description. It "
            "never diagnoses anyone and never labels any real person."
        ),
        "how_it_works": (
            "Calm works as an appraisal-and-settling process. The mind is "
            "always, mostly unconsciously, scanning events against two "
            "questions: am I safe, and can I handle this? When the answers "
            "come back yes - no threat detected, resources sufficient - the "
            "nervous system stands down from its alert footing. The "
            "parasympathetic branch, often called the rest-and-digest "
            "system, takes the lead: heart rate eases, breathing deepens, "
            "muscles release. At the same time the mind stops treating "
            "everything as a problem to solve, which is why calm feels "
            "like the mental chatter turning down. Calm also works as a "
            "platform: with arousal low and attention free, people think "
            "more clearly, listen better, and choose more wisely, which is "
            "why calm is the state people return to when they want to do "
            "their best thinking. It is maintained by the same machinery "
            "that creates it - slow breathing, released muscles, and "
            "appraisals of safety and capability keep the parasympathetic "
            "system in charge."
        ),
        "key_points": [
            "Calm is a low-arousal, pleasant state: low energy, high ease, "
            "with a distinct texture of steadiness.",
            "Calm is not emptiness or numbness - a calm person is ready to "
            "act but chooses stillness.",
            "It arises when the mind appraises the moment as safe and "
            "manageable, and the parasympathetic nervous system takes the lead.",
            "Calm can arrive on its own or be cultivated through breathing, "
            "posture, and thought habits.",
            "As a platform state, calm supports clearer thinking, better "
            "listening, and wiser choices.",
        ],
        "requirements": [
            "Describe the emotion only - no diagnosing real people, no "
            "labeling anyone with an emotional state.",
            "Keep language plain and human-readable; no clinical jargon "
            "posing as authority.",
            "Distinguish calm from numbness, apathy, and suppression.",
        ],
        "standards": [
            "Basic-emotion and appraisal-theory vocabulary used consistently "
            "(arousal, valence, appraisal).",
            "Calm kept distinct from neighboring states: contentment, "
            "serenity, boredom, apathy.",
            "Every claim descriptive and educational, never therapeutic "
            "advice for a real condition.",
        ],
        "citations": [
            "Russell, J. A. (1980). A circumplex model of affect.",
            "Lazarus, R. S. (1991). Emotion and adaptation.",
            "Porges, S. W. (2011). The Polyvagal Theory.",
            "APA Dictionary of Psychology - calm.",
            "Benson, H. (1975). The Relaxation Response.",
        ],
        "sig_lens": (
            "The Signature read: calm is the home frequency of the system - "
            "the steady green board that says all circuits hold. Where "
            "public psychology charts a low-arousal pleasant state, the "
            "Signature Calm Method treats calm as the commanded baseline: "
            "the engine at idle, power held in reserve, the system answering "
            "only when called."
        ),
    },
    # ------------------------------------------------- 2. family
    {
        "key": "calm_family",
        "name": "Calm in the Emotion Family: Where It Sits",
        "group": "What the Emotion Is",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Every emotion has relatives, and calm is no exception. On the "
            "standard map of feelings - the circumplex model with pleasant-"
            "unpleasant on one axis and energized-drowsy on the other - "
            "calm sits in the pleasant, low-energy quadrant: near "
            "serenity, contentment, and relief, across from anxiety, which "
            "shares the high-energy, unpleasant corner with fear and anger. "
            "Calm is fed by appraisals of safety and goal-congruence: "
            "things are going fine, nothing needs fighting or fleeing. "
            "Whether calm counts as a 'basic' emotion depends on which "
            "list a researcher uses. On strict lists built around facial "
            "expressions, calm often appears as the absence of emotion "
            "rather than one of the six; on broader functional lists, calm "
            "earns its seat because it has a distinct appraisal (safe and "
            "manageable), a distinct physiology (parasympathetic lead), and "
            "a distinct job (restoration and readiness). Its closest "
            "cousins each shade it differently: serenity is calm with a "
            "spiritual flavor, contentment is calm plus satisfaction with "
            "what one has, relief is calm arriving after fear passes, and "
            "tranquility is calm stretched across a whole scene or season. "
            "Its opposites are anxiety and agitation - the same body with "
            "the alarm still on. Knowing the family matters because "
            "emotions blend at their borders: what feels like 'pure calm' "
            "is often calm tinted with relief, or contentment, or quiet "
            "happiness, and naming the tint sharpens the description."
        ),
        "how_it_works": (
            "The emotion family is organized by what triggers each member "
            "and what each member does. Calm's trigger appraisal is safety "
            "plus sufficiency: no threat, enough resources, nothing urgent. "
            "Its function is restoration - the system repairs, stores "
            "energy, and stays ready without spending anything. This is "
            "why calm sits near the recovery emotions (relief, relaxation, "
            "contentment): they all follow arousal back down to baseline. "
            "In Plutchik's wheel, calm-like states live between acceptance "
            "and serenity on the low-intensity rim, far from rage and "
            "terror. In appraisal terms (Lazarus, Scherer), calm comes from "
            "goal-congruent events judged certain and controllable. The "
            "family placement explains calm's social role too: a calm "
            "presence regulates others, the way one steady voice quiets a "
            "room, because human nervous systems co-regulate - they borrow "
            "each other's baselines."
        ),
        "key_points": [
            "On the circumplex map, calm sits in the pleasant, low-energy "
            "quadrant - near serenity, contentment, and relief.",
            "Calm's appraisal is safety plus sufficiency; its job is "
            "restoration and readiness without spending energy.",
            "Closest cousins: serenity, contentment, relief, tranquility - "
            "each a different tint on the same base.",
            "Opposites: anxiety and agitation - same body, alarm still on.",
            "A calm presence regulates others because nervous systems "
            "co-regulate.",
        ],
        "requirements": [
            "Place calm on the standard emotion maps without claiming a "
            "single official family tree.",
            "Name close cousins and opposites precisely; no blurred labels.",
            "Keep the mapping descriptive - no diagnosing readers.",
        ],
        "standards": [
            "Circumplex, Plutchik, and appraisal-theory terms used "
            "consistently and attributed.",
            "Cousin emotions distinguished by their appraisal difference, "
            "not just by name.",
            "Co-regulation claim kept to its plain meaning: people settle "
            "each other.",
        ],
        "citations": [
            "Russell, J. A. (1980). A circumplex model of affect.",
            "Plutchik, R. (1980). Emotion: A psychoevolutionary synthesis.",
            "Lazarus, R. S. (1991). Emotion and adaptation.",
            "Scherer, K. R. (2005). What are emotions? And how can they be measured?",
            "Barrett, L. F. (2017). How Emotions Are Made.",
        ],
        "sig_lens": (
            "The Signature read: in the family map, calm is the home row of "
            "the Signature panel - every other state is measured as "
            "deviation from it. The Signature Calm Method treats the "
            "emotion family as a dashboard: calm is the green baseline "
            "light, and every cousin and opposite is read by how far its "
            "needle swings from the home frequency."
        ),
    },
    # ------------------------------------------------- 3. intensity
    {
        "key": "calm_intensity_scale",
        "name": "Mild, Moderate, Intense: Calm at Different Volumes",
        "group": "What the Emotion Is",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Calm is the same emotion at every volume, but the volume "
            "changes the experience. Mild calm is a light easing - the "
            "tension in the jaw softens, the shoulders drop half an inch, "
            "and the day feels a little less sharp. It is the calm of a "
            "good chair, a warm drink, a few slow breaths: noticeable "
            "mainly because the edge comes off. Moderate calm is deeper - "
            "breathing is slow and full, thoughts come one at a time "
            "instead of crowding, and there is a sense of spaciousness, "
            "like a room with the windows open. This is the calm people "
            "describe after a walk, after good news settles in, after a "
            "long exhale they did not know they were holding. Intense calm "
            "- sometimes called deep calm or profound stillness - is a "
            "full-body state: the mind goes nearly silent, the body feels "
            "heavy and light at once, time seems to slow, and the person "
            "may feel profoundly at ease for minutes at a stretch. "
            "Meditators, people floating in quiet water, or someone sitting "
            "in a hospital waiting room when the doctor finally says the "
            "words they hoped for, all know this volume. The three volumes "
            "share the same signature - safety, ease, slowed physiology - "
            "but they differ in depth, duration, and how much of the "
            "person they occupy. Recognizing the volumes matters because "
            "mild calm can be reached in seconds with a single slow breath, "
            "while intense calm usually needs time, safety, and practice."
        ),
        "how_it_works": (
            "Intensity in calm tracks how fully the parasympathetic system "
            "has taken over and how completely the threat-appraisal "
            "machinery has stood down. At mild volumes, only the surface "
            "settles: muscle tension eases and breathing slows a little "
            "while the mind stays mostly busy. At moderate volumes, the "
            "shift reaches the autonomic core: heart rate variability "
            "rises, digestion resumes, the stress hormones begin clearing. "
            "At intense volumes, the change is systemic - cortical "
            "chatter quiets, the default-mode rumination loop powers down, "
            "and attention can rest on a single object without effort. "
            "Depth and duration trade off: mild calm is quick and "
            "repeatable all day; intense calm builds slowly and usually "
            "needs sustained safety. The volume also changes what the "
            "state is good for: mild calm suits quick resets between "
            "tasks, moderate calm suits good decisions and hard "
            "conversations, and intense calm suits recovery, insight, and "
            "rest."
        ),
        "key_points": [
            "Mild calm: a light easing - jaw softens, shoulders drop, the "
            "edge comes off; reachable in seconds.",
            "Moderate calm: slow full breathing, thoughts one at a time, a "
            "sense of spaciousness; suits decisions and hard talks.",
            "Intense calm: near-silent mind, heavy-and-light body, slowed "
            "time; needs safety, time, and practice.",
            "All three volumes share the signature - safety, ease, slowed "
            "physiology - differing in depth and duration.",
            "Volume matches use: quick resets, deep decisions, or full "
            "recovery.",
        ],
        "requirements": [
            "Describe all three volumes of the same emotion; no separate "
            "emotions invented for intensity levels.",
            "Give a concrete everyday example for each volume.",
            "No therapeutic prescriptions - general everyday description only.",
        ],
        "standards": [
            "Intensity described as depth plus duration, consistently.",
            "Physiology matched to volume without overstating measurement.",
            "Every volume tied to ordinary situations readers recognize.",
        ],
        "citations": [
            "Russell, J. A. (1980). A circumplex model of affect.",
            "Benson, H. (1975). The Relaxation Response.",
            "Kabat-Zinn, J. (1990). Full Catastrophe Living.",
            "APA Dictionary of Psychology - relaxation.",
        ],
        "sig_lens": (
            "The Signature read: the three volumes are the system's throttle "
            "positions - idle, cruise, and full rest. The Signature Calm "
            "Method trains the operator to select the volume the job "
            "needs: idle for quick resets, cruise for decisions, full rest "
            "for recovery - power held in reserve at every setting."
        ),
    },
    # ------------------------------------------------- 4. myths
    {
        "key": "calm_myths",
        "name": "Common Myths and Misunderstandings About Calm",
        "group": "What the Emotion Is",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Calm is widely misunderstood, and the myths cost people the "
            "real thing. Myth one: calm means feeling nothing. In truth "
            "calm is a felt state with texture - ease, steadiness, "
            "spaciousness - and a person in genuine calm feels more, not "
            "less, because the noise is gone. Feeling nothing is numbness, "
            "and numbness is a different state entirely. Myth two: calm "
            "people never get angry or afraid. Calm is not the absence of "
            "other emotions; it is the baseline people return to. A calm "
            "person can feel anger fully and then settle - the skill is "
            "the return, not the exemption. Myth three: calm is weakness "
            "or passivity. Watch a surgeon, a pilot in turbulence, or a "
            "firefighter walking into a burning building: their power is "
            "calm, and calm is what lets power be aimed. Panic is the "
            "weak state - it spends energy on nothing. Myth four: you "
            "either have a calm temperament or you do not. Temperament "
            "sets the starting point, but calm is trainable: breathing "
            "patterns, muscle habits, and appraisal habits all shift the "
            "baseline with practice, the way training shifts a runner's "
            "resting heart rate. Myth five: calm means the absence of "
            "problems. Calm coexists with problems constantly - it is the "
            "state of meeting problems without being owned by them. The "
            "hospital corridor can hold both terrible news and a calm "
            "visitor; the calm does not deny the news, it steadies the "
            "hands that must deal with it."
        ),
        "how_it_works": (
            "Myths about calm persist because calm is often confused with "
            "its look-alikes. Numbness looks calm from the outside - "
            "still face, quiet voice - but inside there is shutdown, not "
            "ease; the difference is readiness, which only the person can "
            "feel. Suppression also looks calm - the jaw set, the feelings "
            "pushed down - but suppression keeps the alarm running "
            "underneath, and the body pays for it in tension and fatigue. "
            "True calm has a signature the fakes lack: slow easy "
            "breathing, released muscles, and a mind that can turn toward "
            "a problem without flinching. The trainability myth falls "
            "apart against the physiology: the parasympathetic system "
            "responds to practice like a muscle, and appraisal habits - "
            "how automatically the mind reads 'safe and manageable' - are "
            "learned patterns that can be relearned. Understanding the "
            "myths matters because chasing fake calm (numbness, "
            "suppression) never delivers the benefits of the real thing."
        ),
        "key_points": [
            "Myth: calm means feeling nothing. Truth: calm has texture - "
            "ease and steadiness; feeling nothing is numbness.",
            "Myth: calm people never feel anger or fear. Truth: the skill "
            "is the return to baseline, not exemption.",
            "Myth: calm is weakness. Truth: panic spends power on nothing; "
            "calm aims it.",
            "Myth: temperament decides. Truth: calm is trainable - breath, "
            "muscle, and appraisal habits shift the baseline.",
            "Myth: calm means no problems. Truth: calm meets problems "
            "without being owned by them.",
        ],
        "requirements": [
            "Pair every myth with the plain truth; no myth left standing "
            "unanswered.",
            "Distinguish calm from numbness and suppression explicitly.",
            "No diagnosing, no clinical claims - descriptive only.",
        ],
        "standards": [
            "Each myth-truth pair testable against the calm signature "
            "(breath, muscle, appraisal).",
            "Look-alike states named and separated, not lumped.",
            "Everyday examples carry the explanations.",
        ],
        "citations": [
            "Lazarus, R. S. (1991). Emotion and adaptation.",
            "Benson, H. (1975). The Relaxation Response.",
            "Barrett, L. F. (2017). How Emotions Are Made.",
            "APA Dictionary of Psychology - calm; emotional suppression.",
        ],
        "sig_lens": (
            "The Signature read: the myths are misreadings of the panel. "
            "Numbness is a dead gauge, suppression is a pinned needle - "
            "neither is the green light. The Signature Calm Method teaches "
            "the operator to read the true home frequency: ready, "
            "steady, and answering only when commanded."
        ),
    },
    # ------------------------------------------------- 5. inside
    {
        "key": "calm_inside",
        "name": "Inside the Feeling: What Calm Is Like Right Now",
        "group": "How It Feels",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "From the inside, calm feels like the room of the mind getting "
            "bigger. Thoughts that were crowding and shouting step back "
            "and stand in a line; there is space between them, and in "
            "that space you can finally hear yourself think. The body "
            "reports in first: a warmth behind the eyes, the jaw "
            "unclenching like a fist opening, the shoulders sliding down "
            "from the ears where they had crept up. Breathing changes "
            "without being told - slower, deeper, the exhale a little "
            "longer than the inhale, as if the body has remembered "
            "something it always knew. There is a quality of time "
            "shifting: urgency drains out of the next hour, and 'later' "
            "stops feeling like a threat. Sensations get slightly "
            "sharper, oddly - colors a touch clearer, sounds a touch "
            "rounder - because attention is no longer spending itself on "
            "scanning for trouble. People describe it as being held, as "
            "solid ground, as the mental equivalent of clean sheets. It "
            "is not excitement; nothing sparkles. It is the deep "
            "satisfaction of a system at rest - the feeling of enough. "
            "And underneath it runs a quiet readiness: you could get up "
            "and act in a moment, but there is no rush to, and that lack "
            "of rush is itself the pleasure."
        ),
        "how_it_works": (
            "The inside of calm is the felt side of a physiological "
            "handoff. As the parasympathetic system takes the lead, the "
            "brain receives a changed stream of body signals - slower "
            "heartbeat, deeper breath, released muscle tension - and "
            "constructs the feeling of calm from that stream, the way it "
            "constructs all feelings from body plus context (Barrett). "
            "Attention shifts because the threat-detection network "
            "powers down: the amygdala-driven scanning that narrows "
            "focus onto danger eases, and the perceptual field widens, "
            "which is why colors and sounds seem richer. The sense of "
            "time slowing comes from the same shift - urgency is a "
            "threat signal, and when the signal stops, the future stops "
            "pressing. The quiet readiness underneath is real "
            "physiology too: calm is a high-vagal-tone state, and high "
            "vagal tone is the body's way of keeping the brakes on while "
            "the engine stays warm - able to release instantly into "
            "action or deeper rest."
        ),
        "key_points": [
            "Inside calm, the mind's room gets bigger: thoughts line up "
            "with space between them.",
            "The body reports first - unclenching jaw, dropping shoulders, "
            "slower deeper breath.",
            "Urgency drains from the future; 'later' stops feeling like a "
            "threat.",
            "Attention widens as threat-scanning powers down, so the world "
            "seems slightly sharper.",
            "Underneath runs quiet readiness: able to act in a moment, in "
            "no rush to.",
        ],
        "requirements": [
            "First-person, present-tense, sensory - a lived passage, not a "
            "definition.",
            "No diagnosing the reader; the passage describes, never labels.",
            "Keep it general and safe - an ordinary calm moment, nothing "
            "clinical.",
        ],
        "standards": [
            "Felt texture (body, time, attention) covered, not just the "
            "label 'calm'.",
            "Physiology matched to the felt report without overclaiming.",
            "Readiness distinguished from tension throughout.",
        ],
        "citations": [
            "Barrett, L. F. (2017). How Emotions Are Made.",
            "Porges, S. W. (2011). The Polyvagal Theory.",
            "Frijda, N. H. (1986). The Emotions.",
            "APA Dictionary of Psychology - calm.",
        ],
        "sig_lens": (
            "The Signature read: the inside passage is the operator's "
            "log from the home frequency - every sensation a gauge "
            "reading green. The Signature Calm Method trains recognition "
            "of this exact interior: jaw open, shoulders down, breath "
            "slow, future unthreatening - the baseline log entry against "
            "which all deviations are measured."
        ),
    },
    # ------------------------------------------------- 6. time course
    {
        "key": "calm_time_course",
        "name": "How Calm Changes Over Time: Onset, Peak, Fading, Aftershock",
        "group": "How It Feels",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Calm has a shape in time, and knowing the shape helps you "
            "recognize each phase. Onset: calm rarely arrives all at "
            "once. It begins as a loosening - one slow breath that actually "
            "works, a muscle letting go, a thought finishing instead of "
            "looping. These small releases stack, and somewhere around "
            "the third or fourth, the person notices: oh, I am calming "
            "down. Peak: the full state holds - breath slow, body easy, "
            "mind spacious. Peaks of calm are quieter than peaks of joy "
            "or anger; there is no fireworks moment, just a stretch of "
            "minutes where everything is simply fine, and the person may "
            "not even mark it until later. Fading: calm fades the way it "
            "came, gradually, unless something interrupts it. A phone "
            "buzz, a remembered deadline, a sudden noise - any of these "
            "can snap the state like a twig, or the person can simply "
            "drift out of it as attention moves on. Aftershock: calm "
            "leaves a residue. For a while after a real stretch of calm, "
            "the body stays slower, reactions stay softer, and the next "
            "annoyance lands on a cushion instead of a nerve. People who "
            "practice settling into calm regularly report that the "
            "aftershock stretches longer each time - the baseline itself "
            "drifts toward ease."
        ),
        "how_it_works": (
            "The time course of calm follows the physiology of "
            "arousal decay. Onset is the parasympathetic system "
            "accumulating small wins: each slow exhale nudges vagal "
            "tone higher, each released muscle removes one stream of "
            "tension feedback to the brain, and the effects compound "
            "over tens of seconds to minutes. The peak is a stable "
            "attractor - with threat appraisal off and the body "
            "signaling safety, the state is self-maintaining until "
            "something new enters. Fading happens two ways: interruption "
            "(a new stimulus re-arouses the threat system, which is "
            "fast - arousal spikes in seconds) or drift (attention "
            "moves on and the state decays over minutes). The aftershock "
            "is real biochemistry: stress hormones clear slowly, so for "
            "a window after deep calm the system is buffered - it takes "
            "a bigger stimulus to re-arouse it. Repeated practice "
            "lengthens the buffer, which is the mechanism behind "
            "'getting calmer with practice.'"
        ),
        "key_points": [
            "Onset is gradual: small releases stack - a breath, a muscle, "
            "a finished thought - until the person notices.",
            "The peak is quiet: a stretch of minutes where everything is "
            "simply fine, often marked only in hindsight.",
            "Fading comes by interruption (fast - arousal spikes in "
            "seconds) or by drift (slow, over minutes).",
            "Aftershock: a biochemical buffer window where the next "
            "annoyance lands on a cushion.",
            "Repeated practice lengthens the aftershock; the baseline "
            "drifts toward ease.",
        ],
        "requirements": [
            "Cover all four phases: onset, peak, fading, aftershock.",
            "Give the time scale of each phase in ordinary terms.",
            "No clinical claims; general everyday description.",
        ],
        "standards": [
            "Phase transitions tied to physiology, not magic.",
            "Interruption vs drift distinguished as two different "
            "fade mechanisms.",
            "Practice effect stated as baseline drift, not transformation.",
        ],
        "citations": [
            "Frijda, N. H. (1986). The Emotions.",
            "Porges, S. W. (2011). The Polyvagal Theory.",
            "Benson, H. (1975). The Relaxation Response.",
            "Scherer, K. R. (2005). What are emotions?",
        ],
        "sig_lens": (
            "The Signature read: the time course is the system's "
            "power-down and power-up curve, logged like an engine "
            "telemetry trace. The Signature Calm Method charts each "
            "phase - onset ramp, peak hold, fade slope, aftershock "
            "buffer - so the operator can read where the system is in "
            "its cycle at a glance."
        ),
    },
    # ------------------------------------------------- 7. low vs high
    {
        "key": "calm_low_vs_high",
        "name": "Calm at Low Intensity vs High Intensity: Two Lived Snapshots",
        "group": "How It Feels",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "Snapshot one - low intensity. It is Tuesday, mid-morning. "
            "Mara has three deadlines and a inbox that keeps refilling, "
            "but she just made tea and took one slow breath at the "
            "window. Her jaw unclenches. The deadlines are still there, "
            "still real, but they sit in a row instead of a pile. She "
            "answers one email with a clear head, and the tea is warm "
            "in her hands. This is mild calm: a thin but real layer of "
            "ease over an ordinary busy day. Nothing is resolved; "
            "everything is just... manageable. Snapshot two - high "
            "intensity. It is Sunday, late afternoon. Mara is lying on "
            "the grass in the park, no phone, no plans, the sun warm on "
            "her face. Her breathing has gone slow and deep without her "
            "deciding it. Thoughts arrive like clouds and drift on; she "
            "watches them without following. Her body feels heavy and "
            "light at the same time, and she could stay here forever - "
            "not from laziness but from completeness, as if this "
            "moment needs nothing added. An hour passes like twenty "
            "minutes. This is deep calm: the whole system at rest, the "
            "mind nearly silent, time itself loosened. Same emotion, "
            "different depth. The Tuesday version is a tool she uses; "
            "the Sunday version is a place she visits. Both are calm, "
            "and both are unmistakable from the inside."
        ),
        "how_it_works": (
            "The two snapshots differ in how far the settling has "
            "spread. In the low-intensity snapshot, the parasympathetic "
            "shift is partial: one slow breath raises vagal tone "
            "slightly, the appraisal 'I can handle this' holds for the "
            "next task, but background arousal stays elevated - the "
            "system is calm at the surface, busy underneath. In the "
            "high-intensity snapshot, the shift is systemic: sustained "
            "safety plus time lets arousal decay fully, the default-mode "
            "rumination network quiets, and attention rests without "
            "effort on simple sensations. The low version is "
            "interruptible - one urgent email can break it - because "
            "arousal is only dampened, not cleared. The high version "
            "has momentum: the biochemical buffer is deep, so small "
            "disturbances wash off. Both snapshots share the same "
            "felt signature - ease, steadiness, slowed breath - which "
            "is how the person knows it is the same emotion at "
            "different depths."
        ),
        "key_points": [
            "Low intensity: a thin real layer of ease over a busy day - "
            "manageable, not resolved; a tool used between tasks.",
            "High intensity: the whole system at rest - near-silent mind, "
            "loosened time; a place visited, not a tool grabbed.",
            "The difference is spread: partial settling vs systemic shift "
            "of arousal and attention.",
            "Low calm is interruptible; high calm has momentum and a deep "
            "buffer.",
            "Same felt signature at both depths - ease, steadiness, slowed "
            "breath - marks it as one emotion.",
        ],
        "requirements": [
            "Two concrete lived snapshots, same emotion, clearly different "
            "depths.",
            "Everyday settings; no one is diagnosed or labeled.",
            "Show what each depth is good for.",
        ],
        "standards": [
            "Depth difference tied to physiology (partial vs systemic "
            "settling).",
            "Interruptibility difference explained, not just asserted.",
            "Snapshots stay in the descriptive lane - no advice framing.",
        ],
        "citations": [
            "Russell, J. A. (1980). A circumplex model of affect.",
            "Porges, S. W. (2011). The Polyvagal Theory.",
            "Kabat-Zinn, J. (1990). Full Catastrophe Living.",
        ],
        "sig_lens": (
            "The Signature read: the two snapshots are the throttle at "
            "idle and at full rest - Tuesday's thin layer is the system "
            "holding ready under load, Sunday's depth is the system fully "
            "parked. The Signature Calm Method logs both as valid "
            "readings of the home frequency, differing only in how far "
            "the power-down has spread."
        ),
    },
    # ------------------------------------------------- 8. partner mix
    {
        "key": "calm_partner_mix",
        "name": "Calm Mixed With Relief: Its Most Common Partner",
        "group": "How It Feels",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "Calm's most common partner is relief, and the blend is one "
            "of the best feelings a person can have. Relief is what "
            "arrives when a feared thing does not happen: the test "
            "results are clear, the storm misses the town, the child "
            "who was late walks through the door. When relief lands, it "
            "almost always brings calm with it, and the two braid "
            "together into something richer than either alone. From the "
            "inside, the mix feels like this: first the sharp exhale of "
            "relief - a near-laugh, a hand to the chest, the body "
            "suddenly lighter - and then, as the lightness settles, the "
            "deep steadying of calm spreads underneath it. Relief is the "
            "wave; calm is the water it lands in. People describe the "
            "blend as 'I can breathe again' followed by 'everything is "
            "going to be fine,' and the second sentence is the calm "
            "doing its work - taking the momentary release of relief "
            "and turning it into a durable state. The blend has a "
            "signature rhythm: spike of release, then a long slow "
            "settling, like a bell struck once ringing down into "
            "silence. It is why good news feels so physical - the body "
            "has been holding tension for the feared outcome, and the "
            "blend is the feeling of all that tension being given back."
        ),
        "how_it_works": (
            "Relief and calm are natural partners because they share an "
            "appraisal: the threat is gone. Relief is the dynamic part - "
            "the sudden removal of anticipated harm, which produces a "
            "fast parasympathetic rebound (the sharp exhale, the laugh). "
            "Calm is the steady-state part - the continued appraisal of "
            "safety that keeps the system settled after the rebound. "
            "Neurologically, relief involves the reward system "
            "registering 'better than expected,' while calm involves "
            "sustained vagal tone; the blend is reward plus regulation. "
            "This is why the mix feels like a sequence: the reward "
            "spike comes first and fast, the regulation spreads after "
            "and slow. The partnership also explains why relief without "
            "calm feels incomplete - if the feared thing passes but new "
            "worries crowd in, the person gets the exhale but not the "
            "settling, and the blend never forms."
        ),
        "key_points": [
            "Relief is calm's most common partner: the feared thing "
            "passes, and calm spreads underneath the release.",
            "The blend has a rhythm: sharp exhale of relief, then long "
            "slow settling of calm - wave, then water.",
            "Relief is the dynamic rebound (reward: better than "
            "expected); calm is the durable steady state (sustained "
            "safety).",
            "The mix feels physical because the body gives back tension "
            "it was holding for the feared outcome.",
            "Relief without calm feels incomplete - the exhale without "
            "the settling.",
        ],
        "requirements": [
            "Describe the blend as a lived sequence, not just two labels.",
            "Name relief as the partner; keep other blends for the mixes "
            "record.",
            "No diagnosing; descriptive only.",
        ],
        "standards": [
            "Each partner's contribution distinguished (dynamic vs steady).",
            "The sequence rhythm stated explicitly.",
            "Incomplete-blend case included for contrast.",
        ],
        "citations": [
            "Lazarus, R. S. (1991). Emotion and adaptation.",
            "Frijda, N. H. (1986). The Emotions.",
            "Porges, S. W. (2011). The Polyvagal Theory.",
        ],
        "sig_lens": (
            "The Signature read: relief is the alarm clearing, calm is "
            "the panel returning to green - the blend is the system's "
            "full reset cycle. The Signature Calm Method treats the "
            "relief-calm sequence as the canonical restoration "
            "telemetry: spike, settle, hold - the home frequency "
            "reacquired after a threat passes."
        ),
    },
    # ------------------------------------------------- 9. day vignette
    {
        "key": "calm_day",
        "name": "A Day in the Life: Calm Running Through an Ordinary Day",
        "group": "How It Feels",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "Dawn: Elena wakes before the alarm, and for a moment she "
            "just lies there, listening to the house. No rush yet. She "
            "breathes slowly, and the day feels like a field before "
            "anyone walks across it. Morning: the commute is crowded, "
            "but she has her seat and her book, and the jostling stays "
            "outside her. A delay is announced; she feels the old "
            "irritation start, takes one long exhale, and it passes "
            "like a cloud. Midday: a hard meeting. Her colleague "
            "criticizes her proposal, and Elena notices her shoulders "
            "rising - then deliberately drops them, slows her voice a "
            "notch, and answers the substance instead of the tone. The "
            "calm is not automatic; it is chosen, breath by breath. "
            "Afternoon: good news arrives - the project is approved. "
            "She smiles, feels the warm spread of it, and lets it "
            "settle instead of spinning up. Evening: cooking dinner, "
            "she chops vegetables with full attention, the rhythm of "
            "the knife steadying her the way it always does. Night: in "
            "bed, she runs through the day once, notes the meeting "
            "went better than feared, and lets the review dissolve. "
            "Sleep comes easily. Nothing extraordinary happened - and "
            "that is the point. Calm is not the absence of a life; it "
            "is the way a life can be carried: steady hands, open "
            "attention, the day's weather passing through instead of "
            "sticking."
        ),
        "how_it_works": (
            "The vignette shows calm as a practiced baseline with "
            "repeated micro-returns. Each scene contains the same "
            "mechanism: a disturbance registers (delay, criticism, good "
            "news), the body starts its arousal response, and Elena "
            "interrupts it early with a regulator - a slow exhale, a "
            "deliberate posture shift, a redirect of attention. Early "
            "interruption is cheap: arousal caught in the first seconds "
            "costs one breath to clear, while arousal left to build "
            "costs twenty minutes. The day also shows calm's "
            "accumulating effect: each successful return leaves a "
            "slightly deeper buffer, so the afternoon's good news "
            "settles instead of spiking and the evening's review "
            "dissolves instead of looping. This is the aftershock "
            "mechanism working across a whole day - calm begetting "
            "calm, the baseline drifting toward ease with each return."
        ),
        "key_points": [
            "Calm through a day is a practiced baseline with repeated "
            "micro-returns, not one unbroken state.",
            "Each return uses a regulator: slow exhale, posture shift, "
            "attention redirect - cheap when caught early.",
            "Arousal caught in seconds costs one breath; left to build, "
            "it costs twenty minutes.",
            "Successful returns accumulate: the buffer deepens across "
            "the day, so later disturbances land softer.",
            "The point: calm is how a life is carried, not the absence "
            "of one.",
        ],
        "requirements": [
            "Walk a full ordinary day, scene by scene; no extraordinary "
            "events.",
            "Show both automatic calm and deliberately chosen calm.",
            "No diagnosing Elena or the reader; descriptive only.",
        ],
        "standards": [
            "Every scene shows the disturbance-then-return mechanism.",
            "Accumulation effect stated, not just implied.",
            "The day stays ordinary - no crises, no miracles.",
        ],
        "citations": [
            "Lazarus, R. S. (1991). Emotion and adaptation.",
            "Kabat-Zinn, J. (1990). Full Catastrophe Living.",
            "Benson, H. (1975). The Relaxation Response.",
        ],
        "sig_lens": (
            "The Signature read: Elena's day is a full shift log at the "
            "home frequency - disturbance, regulator, return, repeated. "
            "The Signature Calm Method treats the ordinary day as the "
            "proving ground: not the absence of weather but the steady "
            "hands that carry the system through it, green board all day."
        ),
    },
    # ------------------------------------------------- 10. body
    {
        "key": "calm_body",
        "name": "What Happens in the Body: Heart, Breath, Muscles, and More",
        "group": "Body Signals",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The body of calm is the body at ease, and it can be read "
            "system by system. Heart: the beat slows and steadies - not "
            "to a crawl, but to an unhurried rhythm, and the variation "
            "between beats grows, which is the signature of a flexible, "
            "well-regulated system. Breath: slower and deeper, the belly "
            "rising more than the chest, the exhale naturally longer than "
            "the inhale; a calm person breathes like someone with all "
            "the time in the world. Muscles: the big tension-holders let "
            "go - jaw unclenches, shoulders drop, the forehead smooths, "
            "hands open. Long-held tension may release in small shudders "
            "or sighs as the body catches up. Stomach: digestion, paused "
            "during alarm, resumes - the gut unclenches, appetite returns "
            "to normal, the 'knot' loosens. Skin: the flush or pallor of "
            "arousal fades toward a neutral tone; hands warm as blood "
            "returns to the extremities. Energy: not the buzzing energy "
            "of excitement but a quiet availability - the body feels "
            "rested and ready at once, like a well-kept engine idling. "
            "Taken together, these signals are unmistakable from the "
            "inside: the body stops bracing. Everything that was held - "
            "breath, muscle, gut - is released, and the release itself "
            "is the feeling."
        ),
        "how_it_works": (
            "Every signal traces to the autonomic handoff from "
            "sympathetic (alarm) to parasympathetic (rest-and-digest) "
            "dominance, with the vagus nerve as the main brake. Slow "
            "deep breathing stimulates the vagus directly - this is why "
            "the exhale matters: exhaling activates the parasympathetic "
            "brake on the heart, lowering rate beat by beat. Muscle "
            "release works in reverse too: the brain reads tension as "
            "evidence of threat, so deliberately releasing muscles "
            "removes threat-evidence and the brain stands down further - "
            "a feedback loop that deepens calm. The gut has its own "
            "dense neural network and responds quickly to the handoff; "
            "the 'knot' loosening is blood flow returning as the alarm "
            "releases its grip on digestion. Warm hands are the same "
            "mechanism at the periphery: arousal pulls blood to the "
            "core, calm lets it flow back out. Heart-rate variability "
            "rises because the brake is being applied and released "
            "moment to moment - a flexible system, constantly adjusting, "
            "which is the physiological meaning of resilience."
        ),
        "key_points": [
            "Heart: slower, steadier beat with greater beat-to-beat "
            "variation - the mark of a flexible regulated system.",
            "Breath: slow, deep, belly-led, exhale longer than inhale.",
            "Muscles: jaw, shoulders, forehead, hands release; old tension "
            "may leave in shudders or sighs.",
            "Stomach and skin: digestion resumes, the gut-knot loosens, "
            "hands warm as blood returns outward.",
            "Energy: quiet availability - rested and ready at once, like "
            "an engine idling.",
        ],
        "requirements": [
            "Cover heart, breath, muscles, stomach, skin, and energy - no "
            "system skipped.",
            "Plain language first; technical terms explained, not flaunted.",
            "Descriptive physiology only - no medical advice.",
        ],
        "standards": [
            "Each signal tied to the autonomic handoff mechanism.",
            "The feedback-loop nature (body informs brain) stated.",
            "Heart-rate variability explained in plain terms.",
        ],
        "citations": [
            "Porges, S. W. (2011). The Polyvagal Theory.",
            "Benson, H. (1975). The Relaxation Response.",
            "Frijda, N. H. (1986). The Emotions.",
            "APA Dictionary of Psychology - parasympathetic nervous system.",
        ],
        "sig_lens": (
            "The Signature read: the body systems are the instrument "
            "panel - heart the tachometer settling, breath the airflow "
            "gauge, muscles the tension meters dropping to green. The "
            "Signature Calm Method teaches the operator to read every "
            "gauge: the body at ease is the system reporting all "
            "circuits nominal."
        ),
    },
    # ------------------------------------------------- 11. posture
    {
        "key": "calm_posture",
        "name": "Posture and Movement Signature: How the Body Carries Calm",
        "group": "Body Signals",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Calm has a posture, and it can be read from across a room. "
            "The spine is upright but not rigid - stacked, not braced. "
            "The shoulders sit low and back, away from the ears, and the "
            "chest is open rather than caved. The head balances over the "
            "spine instead of jutting forward, and the jaw hangs loose. "
            "Hands rest open - palms visible, fingers soft - rather than "
            "clenched or fidgeting. In motion, calm moves at an "
            "unhurried tempo: gestures are smooth and complete, not "
            "jerky or cut short; walking has an even stride; the person "
            "turns the whole body toward what interests them instead of "
            "just flicking the eyes. Stillness in calm is different "
            "from stillness in fear: the calm body is still because it "
            "chooses to be, and the stillness has weight and ease - the "
            "person could move in any direction in a heartbeat. Watch "
            "for the tells: the slow blink, the unhurried nod, the way "
            "a calm person sets things down instead of putting them "
            "down. Actors learn this posture because audiences read it "
            "instantly: open, grounded, unhurried means safe, in "
            "control, and unafraid."
        ),
        "how_it_works": (
            "Posture is both signal and control. As a signal, the open "
            "unhurried body broadcasts safety to others - human "
            "nervous systems read posture faster than words, which is "
            "why one calm person can settle a room. As a control, "
            "posture feeds back into the owner's state: expansive open "
            "postures reduce the brain's threat-evidence, while the "
            "slow tempo of movement prevents the arousal spike that "
            "fast jerky motion can trigger. The 'could move in a "
            "heartbeat' quality is real physiology - calm is high "
            "readiness with the brakes on, not low readiness; the "
            "muscles are released but the system is primed. Movement "
            "tempo matters because the motor system and the arousal "
            "system are coupled: hurrying the body hurries the mind, "
            "and slowing the body slows the mind. This coupling is why "
            "'act calm to become calm' works - the posture is a lever "
            "on the state, not just its expression."
        ),
        "key_points": [
            "The calm posture: spine stacked not braced, shoulders low, "
            "chest open, jaw loose, hands open and soft.",
            "Movement is unhurried: smooth complete gestures, even stride, "
            "whole-body turns.",
            "Calm stillness has weight and readiness - still by choice, "
            "able to move in a heartbeat; fear's stillness is frozen.",
            "Posture is a signal (settles others) and a lever (slowing "
            "the body slows the mind).",
            "Tells: slow blink, unhurried nod, setting things down gently.",
        ],
        "requirements": [
            "Describe the full posture head to toe, plus movement tempo.",
            "Distinguish calm stillness from frozen stillness.",
            "No diagnosing; descriptive only.",
        ],
        "standards": [
            "Signal vs control functions of posture both covered.",
            "Readiness-with-brakes distinguished from low readiness.",
            "Actor-readable detail: concrete, visual, imitable.",
        ],
        "citations": [
            "Ekman, P., & Friesen, W. V. (1978). Facial Action Coding System.",
            "Darwin, C. (1872). The Expression of the Emotions in Man and Animals.",
            "Frijda, N. H. (1986). The Emotions.",
        ],
        "sig_lens": (
            "The Signature read: posture is the system's physical "
            "attitude indicator - stacked and open reads level flight. "
            "The Signature Calm Method trains the body as the first "
            "instrument: set the posture to home-frequency position - "
            "spine stacked, hands open, tempo unhurried - and the "
            "internal gauges follow."
        ),
    },
    # ------------------------------------------------- 12. sleep/appetite
    {
        "key": "calm_sleep_appetite",
        "name": "Sleep, Appetite, and Energy Effects of Calm",
        "group": "Body Signals",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Calm reaches into the body's maintenance systems - sleep, "
            "appetite, and energy - and steadies all three. Sleep: a "
            "calm day leads to easier nights. When the mind is not "
            "carrying unresolved arousal into bed, sleep comes faster "
            "and runs deeper; the person falls asleep without the "
            "tossing review of the day, and wakes feeling restored "
            "rather than wrung out. Chronic agitation does the reverse - "
            "it fragments sleep, and fragmented sleep makes the next "
            "day's calm harder to find, which is why the two travel "
            "together in a loop, for better or worse. Appetite: under "
            "alarm, appetite goes strange - some people cannot eat, "
            "others eat urgently and thoughtlessly. Calm restores the "
            "normal signals: hunger arrives as a clear message rather "
            "than a craving or a void, meals are tasted rather than "
            "inhaled, and the person stops when satisfied because the "
            "body's 'enough' signal is audible again. Energy: calm "
            "does not feel like the fizz of excitement; it feels like "
            "a full tank. Because nothing is being spent on bracing, "
            "scanning, or looping, the day's energy budget stretches "
            "further - calm people often report getting more done with "
            "less tiredness, not because they worked less but because "
            "less of their fuel burned on friction. The three systems "
            "reinforce each other: good sleep steadies appetite, steady "
            "appetite steadies energy, and steady energy makes the next "
            "night's sleep easier - calm as a flywheel."
        ),
        "how_it_works": (
            "The mechanism is the autonomic handoff applied to "
            "maintenance. Sleep onset requires arousal to drop below a "
            "threshold; a calm nervous system is already near that "
            "threshold at bedtime, so the transition is short, while an "
            "agitated system must burn down hours of residual arousal "
            "first. Appetite regulation runs through the same handoff: "
            "the alarm state suppresses digestion and distorts hunger "
            "signals (the gut-brain axis throttled by sympathetic "
            "dominance), while the rest state restores normal signaling - "
            "ghrelin and satiety messages get through clearly. Energy "
            "is a budget: bracing muscles, scanning attention, and "
            "ruminating thought all consume glucose and attention, and "
            "calm simply stops the spending, leaving the budget for "
            "chosen work. The flywheel effect is positive feedback - "
            "each steadied system lowers the load on the others, so "
            "calm in one domain makes calm cheaper in the rest."
        ),
        "key_points": [
            "Sleep: calm days lead to faster sleep onset and deeper "
            "sleep; agitation fragments sleep, which makes tomorrow's "
            "calm harder - a loop either way.",
            "Appetite: calm restores clear hunger and satiety signals; "
            "meals are tasted, and 'enough' is audible again.",
            "Energy: calm feels like a full tank - less fuel burned on "
            "bracing and looping, more available for chosen work.",
            "The three systems form a flywheel: each steadied system "
            "lowers the load on the others.",
            "General everyday description only - not medical advice.",
        ],
        "requirements": [
            "Cover sleep, appetite, and energy - all three, no skipping.",
            "State the loop (calm-sleep-calm) in both directions.",
            "No medical advice, no diagnosing sleep or eating issues.",
        ],
        "standards": [
            "Mechanism stated per system (arousal threshold, gut-brain "
            "axis, energy budget).",
            "Flywheel framing kept consistent across the three.",
            "Everyday language; technical terms explained once.",
        ],
        "citations": [
            "Porges, S. W. (2011). The Polyvagal Theory.",
            "Benson, H. (1975). The Relaxation Response.",
            "APA Dictionary of Psychology - sleep; appetite.",
        ],
        "sig_lens": (
            "The Signature read: sleep, appetite, and energy are the "
            "system's maintenance readouts - overnight recharge, fuel "
            "intake, and power budget. The Signature Calm Method treats "
            "the flywheel as scheduled maintenance: hold the home "
            "frequency and every subsystem's gauges drift into green "
            "together."
        ),
    },
    # ------------------------------------------------- 13. body differences
    {
        "key": "calm_body_differences",
        "name": "How Body Signals Differ Between People",
        "group": "Body Signals",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "No two bodies do calm exactly the same way, and the "
            "differences are normal. Some people feel calm first in "
            "the chest - the breath deepening, the heart slowing, a "
            "warmth spreading under the ribs. Others feel it first in "
            "the hands and feet, which warm and tingle as blood returns "
            "to the edges. Some feel it as heaviness, like sinking into "
            "the chair; others as lightness, like the body got a little "
            "easier to carry. Temperament sets the range: a naturally "
            "high-energy person may experience calm as a pleasant "
            "slowing that still hums a little underneath, while a "
            "naturally low-energy person may experience the same state "
            "as near-stillness. Age matters too - children's calm is "
            "often wiggly, arriving in bursts between activity, while "
            "older adults often describe a steadier, deeper settle. "
            "Body history matters most of all: someone who has spent "
            "years braced may first feel calm as strangeness or even "
            "unease - the absence of tension feels unfamiliar - and "
            "only with repetition does it start to feel like home. "
            "None of these differences mean the calm is fake or "
            "broken; the signature is the same underneath - safety, "
            "ease, slowed physiology - wearing different clothes on "
            "different bodies."
        ),
        "how_it_works": (
            "Individual differences in calm come from three sources. "
            "First, baseline physiology: resting heart rate, vagal "
            "tone, and habitual muscle tension differ person to person, "
            "so the same shift lands on different starting points and "
            "feels different. Second, interoception - how finely a "
            "person senses internal signals: high-interoception people "
            "notice the chest and gut changes vividly, low-"
            "interoception people notice mainly the behavioral signs "
            "(slower speech, looser hands). Third, learning history: "
            "the brain predicts what states mean from past experience, "
            "so someone whose past paired stillness with danger may "
            "initially read calm's stillness as a warning - the "
            "unfamiliar-ease effect - until new experience rewrites the "
            "prediction. Culture shapes expression too: some cultures "
            "display calm expansively, others prize a contained "
            "stillness, but the underlying physiology of the handoff "
            "is the same human machinery."
        ),
        "key_points": [
            "First-signal location differs: chest, hands and feet, "
            "heaviness, lightness - all normal.",
            "Temperament sets the range: high-energy people feel calm "
            "as pleasant slowing; low-energy people as near-stillness.",
            "Body history matters: years of bracing can make early calm "
            "feel strange before it feels like home.",
            "Interoception differs: some feel the inside vividly, others "
            "read mainly the outward signs.",
            "Same signature underneath - safety, ease, slowed physiology "
            "- different clothes on different bodies.",
        ],
        "requirements": [
            "Normalize variation; never rank bodies as better or worse "
            "at calm.",
            "Include the unfamiliar-ease effect for braced bodies.",
            "No diagnosing; descriptive only.",
        ],
        "standards": [
            "Three sources of difference named: baseline physiology, "
            "interoception, learning history.",
            "Culture's role in expression vs physiology kept distinct.",
            "Every difference illustrated with a concrete felt example.",
        ],
        "citations": [
            "Barrett, L. F. (2017). How Emotions Are Made.",
            "Frijda, N. H. (1986). The Emotions.",
            "Porges, S. W. (2011). The Polyvagal Theory.",
        ],
        "sig_lens": (
            "The Signature read: different bodies are different hardware "
            "running the same home-frequency firmware - the green light "
            "looks the same on every panel even though the gauges "
            "differ. The Signature Calm Method calibrates per operator: "
            "learn your own first-signal location and read your own "
            "panel, not someone else's."
        ),
    },
    # ------------------------------------------------- 14. face
    {
        "key": "calm_face",
        "name": "The Face of Calm: Eyes, Brows, Mouth, and Micro-Signs",
        "group": "Facial Expression",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The face of calm is the face at rest - but a particular "
            "rest, and the details matter. Eyes: the gaze is soft and "
            "steady, lids at their natural level (not widened, not "
            "heavy), blinking at an unhurried pace. There is no fixed "
            "stare and no darting; the eyes rest on things rather than "
            "grabbing at them. Brows: level and smooth, neither raised "
            "in alarm nor drawn together in effort; the forehead is "
            "unlined, the small muscles between the brows released. "
            "Mouth: closed or gently parted, lips soft and unpressed, "
            "the corners at neutral or lifted just slightly - not a "
            "smile, exactly, but the absence of any downward pull. The "
            "jaw hangs loose; there is often a tiny gap between the "
            "teeth. Micro-signs: the slow blink is calm's most reliable "
            "tell - lids lowering and rising without hurry. The "
            "swallow is easy. The nostrils are still (no flaring). The "
            "whole face has a quality of symmetry and softness, like a "
            "lake with no wind. This face is hard to fake well because "
            "it is defined by absences - no tension anywhere - and the "
            "face has dozens of small muscles that betray held tension "
            "to anyone who knows where to look."
        ),
        "how_it_works": (
            "The calm face is the product of the same autonomic handoff "
            "that settles the body, applied to the face's dense "
            "musculature. Under alarm, the face prepares: brows rise or "
            "knit, eyes widen, lips press or stretch - all driven by "
            "sympathetic activation of the facial muscles. When the "
            "parasympathetic system takes over, that activation simply "
            "stops, and the face returns to its neutral architecture - "
            "which reads as calm because the human visual system is "
            "exquisitely tuned to detect tension in faces. The slow "
            "blink is a parasympathetic signature: blink rate tracks "
            "arousal, and the unhurried lid is the visible form of a "
            "settled system. The slightly lifted mouth corners come "
            "from released depressor muscles rather than activated "
            "smile muscles - which is why the calm mouth looks "
            "content but not grinning, and why a forced smile over "
            "tension looks wrong: the lift is there but the release "
            "is not."
        ),
        "key_points": [
            "Eyes: soft steady gaze, natural lids, unhurried blinking - "
            "resting on things, not grabbing.",
            "Brows: level and smooth, forehead unlined; mouth: lips soft, "
            "corners neutral or faintly lifted, jaw loose.",
            "Micro-signs: the slow blink, easy swallow, still nostrils, "
            "overall symmetry and softness.",
            "The face is defined by absences - no tension anywhere - "
            "which is why it is hard to fake.",
            "Calm mouth corners lift from released muscles, not from a "
            "smile; forced cheer over tension reads wrong.",
        ],
        "requirements": [
            "Cover eyes, brows, mouth, and micro-signs - no region skipped.",
            "Distinguish the calm face from a neutral-mask and from a "
            "forced smile.",
            "Descriptive only; no labeling real people's faces.",
        ],
        "standards": [
            "Each feature tied to the underlying muscle state.",
            "Absence-defined expression explained as a fakery barrier.",
            "FACS-consistent vocabulary (brows, lids, lip corners).",
        ],
        "citations": [
            "Ekman, P., & Friesen, W. V. (1978). Facial Action Coding System.",
            "Darwin, C. (1872). The Expression of the Emotions in Man and Animals.",
            "Ekman, P. (1999). Basic emotions.",
        ],
        "sig_lens": (
            "The Signature read: the face is the system's status display "
            "to the outside world - every muscle a pixel, and calm is "
            "the all-green screen. The Signature Calm Method reads the "
            "display like an operator: slow blink, level brows, loose "
            "jaw - the home frequency made visible, broadcasting safety "
            "to every other system in the room."
        ),
    },
    # ------------------------------------------------- 15. face intensity
    {
        "key": "calm_face_intensity",
        "name": "How the Calm Expression Changes With Intensity",
        "group": "Facial Expression",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The calm face deepens with the state, and the changes are "
            "readable. At mild calm, the face looks almost ordinary - "
            "the only signs are small: the forehead smooths, the blink "
            "slows a touch, the mouth unpresses. A stranger might not "
            "notice; someone who knows the person sees the edge come "
            "off. At moderate calm, the signs are unmistakable: the "
            "whole face softens, the eyes take on a steady warmth, the "
            "mouth corners rest faintly up, and the face seems somehow "
            "more symmetrical - tension was pulling it slightly off "
            "true, and now it sits straight. At deep calm, the face "
            "goes almost still in a way that reads as profound ease: "
            "lids lower to a natural half-rest, the gaze turns inward "
            "or goes soft-focused on nothing, the mouth relaxes "
            "completely, and the face can look younger - years of "
            "habitual tension-bracing simply switched off. There is a "
            "continuum, not steps: watch someone settling into a "
            "massage or a long exhale after good news and you can see "
            "the face travel it in real time - smoothing, softening, "
            "stillness. One caution: at the deepest levels the calm "
            "face can resemble sleep or sadness to an untrained eye, "
            "because all three share lowered muscle tone. The "
            "difference is in the mouth and the brow: deep calm keeps "
            "the faint upward rest and the smooth brow, while sadness "
            "pulls the corners down and sleep simply powers everything "
            "off."
        ),
        "how_it_works": (
            "The intensity gradient on the face tracks the depth of "
            "parasympathetic takeover in the facial musculature. Mild "
            "calm releases only the most voluntarily controlled "
            "muscles - the forehead smooths because brow tension is "
            "partly conscious - while deeper habitual bracing (jaw, "
            "mouth corners) stays. Moderate calm reaches the "
            "habitual layer: the depressor muscles release, the "
            "orbicularis around the eyes softens, and the face's "
            "resting symmetry returns. Deep calm reaches the tonic "
            "floor: even background muscle tone drops, lids lower, "
            "gaze softens - the face at its minimum-energy "
            "configuration. The resemblance to sleep and sadness at "
            "depth is a shared-mechanism effect: all three lower "
            "facial muscle tone, but the appraisal behind each "
            "differs, and the mouth corners plus brow carry the "
            "distinguishing signal - calm's faint lift and smooth "
            "brow vs sadness's downturned pull."
        ),
        "key_points": [
            "Mild: small signs - smoothed forehead, slower blink, "
            "unpressed mouth; visible mainly to those who know the person.",
            "Moderate: unmistakable softening - steady warm eyes, faint "
            "upward rest of the mouth, returned symmetry.",
            "Deep: near-stillness of profound ease - lowered lids, "
            "soft-focused gaze, the face looking younger.",
            "The gradient is a continuum, watchable in real time as "
            "someone settles.",
            "Deep calm vs sleep vs sadness: mouth corners and brow carry "
            "the distinguishing signal.",
        ],
        "requirements": [
            "Show the face at three depths on a continuum.",
            "Include the sleep/sadness confusion and how to resolve it.",
            "No labeling real people; descriptive only.",
        ],
        "standards": [
            "Each depth tied to which muscle layer has released.",
            "Continuum framing, not rigid steps.",
            "Distinguishing features named precisely (mouth corners, brow).",
        ],
        "citations": [
            "Ekman, P., & Friesen, W. V. (1978). Facial Action Coding System.",
            "Darwin, C. (1872). The Expression of the Emotions in Man and Animals.",
            "Izard, C. E. (1992). Basic emotions, relations among emotions.",
        ],
        "sig_lens": (
            "The Signature read: the face's depth gradient is the "
            "display dimming through its settings - mild, moderate, "
            "deep, each a lower power state of the same green screen. "
            "The Signature Calm Method trains the operator to read "
            "the depth at a glance and to know the floor: minimum "
            "energy, maximum ease, home frequency holding."
        ),
    },
    # ------------------------------------------------- 16. hide/fake
    {
        "key": "calm_hide_fake",
        "name": "Hiding and Faking Calm: What Leaks Through",
        "group": "Facial Expression",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "People hide the absence of calm and fake its presence "
            "constantly - in negotiations, in parenting, in any room "
            "where steadiness is expected - and the disguise always "
            "leaks somewhere. The faker's strategy is to control the "
            "big signals: they slow their voice, still their hands, "
            "arrange their face into smoothness. What they cannot "
            "control are the small fast things. The blink rate stays "
            "quick - arousal drives blinking and no amount of will "
            "slows it for long. The breath stays shallow and high in "
            "the chest even while the voice sounds measured; watch the "
            "shoulders and you will see them rise slightly with each "
            "inhale. The jaw holds - the faker's mouth may look "
            "relaxed but the masseter muscle stands out faintly, or "
            "the lips press for a fraction of a second between "
            "sentences. Hands betray: still hands that are too still, "
            "fingers interlaced a little too tightly, a thumb pressing "
            "into a knuckle. And the eyes: the gaze may be steady, but "
            "it is a held steadiness, effortful, and every so often it "
            "darts or hardens. Genuine calm, by contrast, is "
            "unbothered about being watched - it does not perform "
            "stillness, it simply has nothing to hide, and that "
            "effortlessness is itself the hardest thing to counterfeit."
        ),
        "how_it_works": (
            "Faked calm fails because the face and body have two "
            "control systems and only one of them obeys the will. "
            "Voluntary control handles the big slow signals - posture, "
            "voice pace, hand placement - which is why fakers can look "
            "convincing at a glance. But blink rate, breathing depth, "
            "micro-tension in the jaw, and pupil behavior run on "
            "autonomic control, which answers to arousal, not "
            "intention. As long as the threat appraisal is still "
            "running underneath, the sympathetic system keeps "
            "firing these small signals no matter what the voluntary "
            "system stages. This is the classic leakage pattern "
            "described in deception research: the channels with the "
            "least voluntary control leak the most truth. Genuine "
            "calm shows the reverse pattern - the small fast signals "
            "agree with the big slow ones, because both are driven by "
            "the same settled appraisal. Congruence across channels "
            "is the real signature; any single channel can be staged, "
            "but staging all of them at once exceeds what attention "
            "can manage."
        ),
        "key_points": [
            "Fakers control the big slow signals (voice pace, posture, "
            "hand placement) but cannot control the small fast ones.",
            "Leaks: quick blink rate, shallow high breathing, held jaw, "
            "overly-still hands, effortful held gaze.",
            "Blink, breath depth, jaw micro-tension, and pupils run on "
            "autonomic control - they answer to arousal, not will.",
            "Genuine calm is congruent: small fast signals agree with "
            "big slow ones.",
            "Effortlessness is the unfakeable part - real calm does not "
            "perform stillness.",
        ],
        "requirements": [
            "Name the specific leak channels; no vague 'body language' "
            "claims.",
            "Explain why faking fails in mechanism terms.",
            "Descriptive only - this is education, not interrogation "
            "training.",
        ],
        "standards": [
            "Voluntary vs autonomic control distinction carried "
            "throughout.",
            "Leakage pattern consistent with established expression "
            "research.",
            "Congruence framed as the real signature.",
        ],
        "citations": [
            "Ekman, P., & Friesen, W. V. (1978). Facial Action Coding System.",
            "Ekman, P. (1999). Basic emotions.",
            "Darwin, C. (1872). The Expression of the Emotions in Man and Animals.",
        ],
        "sig_lens": (
            "The Signature read: faked calm is a spoofed display - the "
            "big pixels staged green while the small fast gauges still "
            "flash amber underneath. The Signature Calm Method teaches "
            "channel congruence as the authenticity test: when every "
            "gauge agrees, the home frequency is real; when the fast "
            "gauges disagree, the panel is staged."
        ),
    },
    # ------------------------------------------------- 17. gallery
    {
        "key": "calm_gallery",
        "name": "Expression Gallery Notes: Drawing and Playing Calm",
        "group": "Facial Expression",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "For the artist or actor who must render calm, here is the "
            "look in reproducible notes. The overall geometry: draw the "
            "face at its natural resting proportions - no feature "
            "displaced from neutral. Resist the urge to add a smile; "
            "calm's mouth is neutral-to-faintly-lifted, and a drawn "
            "smile turns it into contentment or pleasantry. Eyes: lids "
            "at mid-level, the upper lid neither raised nor drooping; "
            "the gaze directed, not staring - give the pupils a soft "
            "focus, slightly relaxed. Catch the slow blink mid-fall for "
            "the single most readable calm cue in a still image. Brows: "
            "a smooth unbroken line, no peak, no furrow; the forehead "
            "a clean plane. Mouth and jaw: lips together without "
            "pressure, or parted a breath; show the faintest upturn at "
            "the corners - one or two degrees, no more; drop the jaw a "
            "millimeter to suggest release. Lighting and context do "
            "half the work: soft even light flatters the smooth "
            "forehead, and an unhurried body posture in the frame sells "
            "what the face only suggests. For the actor: the work is "
            "subtractive - release the forehead, unclench the jaw, let "
            "the breath drop into the belly, slow the blink, and then "
            "do less. The audience reads calm in what is absent, so "
            "every added bit of business (a tight smile, a quick nod) "
            "subtracts from it. Common failure modes: the 'serene mask' "
            "(too still, reads as vacant), the 'pleasant mask' (smile "
            "without release, reads as polite tension), and the "
            "'sleepy' (lids too low, reads as drowsy). Aim between "
            "them: present, at ease, and in no hurry."
        ),
        "how_it_works": (
            "Rendering calm works because viewers read faces with the "
            "same threat-detection machinery that reads real people: "
            "the visual system scans for tension - furrowed brows, "
            "pressed lips, widened eyes - and its absence registers as "
            "safety. The artist's job is therefore to remove every "
            "tension cue while keeping the signs of life (directed "
            "gaze, natural lid level) so the face reads as calm rather "
            "than blank. The faint mouth-corner lift matters "
            "disproportionately: with all tension removed, the face "
            "needs one small positive signal to read as pleasant-"
            "calm rather than neutral-flat, and the released "
            "depressor muscles provide exactly that. For the actor, "
            "the subtractive method works through the same body-to-"
            "brain feedback as real calm: releasing the forehead and "
            "jaw and slowing the breath genuinely lowers the "
            "performer's arousal, so the performance becomes the "
            "state - the oldest acting truth, that the body leads the "
            "feeling."
        ),
        "key_points": [
            "Geometry: every feature at natural resting position - no "
            "displacement, no added smile.",
            "The slow blink caught mid-fall is the single most readable "
            "calm cue in a still image.",
            "Mouth: faintest upturn (one or two degrees), jaw dropped a "
            "millimeter - release, not grin.",
            "Actor's method is subtractive: release forehead, unclench "
            "jaw, belly breath, slow blink, then do less.",
            "Failure modes: serene mask (vacant), pleasant mask (polite "
            "tension), sleepy (drowsy) - aim between them.",
        ],
        "requirements": [
            "Give concrete reproducible notes for drawing and for acting.",
            "Name the failure modes and the correction for each.",
            "Keep it a craft guide, not a psychology lecture.",
        ],
        "standards": [
            "Every note tied to a visible feature, not a vibe.",
            "The one-positive-signal principle (faint lift) explained.",
            "Actor notes use the body-leads-feeling mechanism.",
        ],
        "citations": [
            "Ekman, P., & Friesen, W. V. (1978). Facial Action Coding System.",
            "Darwin, C. (1872). The Expression of the Emotions in Man and Animals.",
        ],
        "sig_lens": (
            "The Signature read: the gallery notes are the spec sheet "
            "for rendering the home frequency - every pixel placed to "
            "spec, nothing extra. The Signature Calm Method treats the "
            "craft as calibration: draw or play the green panel exactly "
            "to the instrument readings, and every viewer’s threat-"
            "scanner will confirm the system is nominal."
        ),
    },
    # ------------------------------------------------- 18. triggers classic
    {
        "key": "calm_triggers_classic",
        "name": "The Classic Triggers: What Commonly Brings Calm",
        "group": "Triggers",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Certain situations bring calm the way certain keys open "
            "certain locks - reliably, across most people. Nature is "
            "the great one: water (a lake, the sea, rain on a roof), "
            "green growing things, open sky, the rhythmic sounds of "
            "wind and waves. Humans settle in natural settings so "
            "consistently that researchers have a name for the "
            "effect, and hospital patients with a view of trees "
            "recover measurably better. Slow rhythmic input is "
            "second: rocking, a steady drum, a metronome, a lullaby - "
            "anything with a slow predictable beat entrains the "
            "body's rhythms downward. Warmth and comfort come third: "
            "a warm bath, a heavy blanket, a familiar chair - the "
            "body reads warmth and support as safety. Completion is "
            "fourth: finishing a hard task, handing in the work, the "
            "deep exhale after the deadline - the mind releases its "
            "grip when the job is done. Trusted company is fifth: "
            "the presence of someone safe - a partner's breathing in "
            "the dark, a friend's unhurried voice - settles the "
            "nervous system by co-regulation. And quiet itself, "
            "sixth: the absence of demand - an empty house, a paused "
            "inbox, a morning with nothing scheduled - lets arousal "
            "decay on its own. These are the classics because they "
            "all speak the same language to the nervous system: you "
            "are safe, nothing is required, you can stand down."
        ),
        "how_it_works": (
            "Classic triggers work through two shared mechanisms. "
            "First, safety signaling: nature scenes, warmth, trusted "
            "company, and quiet all reduce the brain's threat-"
            "evidence - there is nothing to fight or flee, so the "
            "alarm stands down and the parasympathetic system takes "
            "over. Second, rhythm entrainment: slow predictable "
            "rhythms (waves, rocking, lullabies, even slow breathing "
            "itself) pull heart rate and neural oscillation toward "
            "their tempo - the body synchronizes with slow input the "
            "way it synchronizes with fast input under alarm. "
            "Completion works differently, through appraisal: the "
            "open loop of unfinished business is itself a low-grade "
            "threat ('something is undone'), and closing it removes "
            "the threat, releasing the held arousal all at once - "
            "the famous post-deadline exhale. Trusted company works "
            "through co-regulation: the nervous system reads another "
            "calm nervous system as safety evidence, which is why a "
            "steady voice can settle a panicking person faster than "
            "any argument."
        ),
        "key_points": [
            "The classics: nature (water, green, sky), slow rhythms, "
            "warmth and comfort, completion, trusted company, quiet.",
            "They all speak one language to the nervous system: safe, "
            "nothing required, stand down.",
            "Two mechanisms: safety signaling (threat-evidence removed) "
            "and rhythm entrainment (slow input pulls the body slow).",
            "Completion releases held arousal by closing the open loop "
            "of unfinished business.",
            "Trusted company works through co-regulation - one calm "
            "nervous system settling another.",
        ],
        "requirements": [
            "Name the classic trigger families with concrete examples.",
            "Give the shared mechanism, not just a list.",
            "Descriptive only; no prescribing trigger-seeking as treatment.",
        ],
        "standards": [
            "Each family tied to safety-signaling or entrainment.",
            "Completion and co-regulation given their distinct mechanisms.",
            "Examples ordinary and recognizable.",
        ],
        "citations": [
            "Lazarus, R. S. (1991). Emotion and adaptation.",
            "Benson, H. (1975). The Relaxation Response.",
            "Porges, S. W. (2011). The Polyvagal Theory.",
            "Kabat-Zinn, J. (1990). Full Catastrophe Living.",
        ],
        "sig_lens": (
            "The Signature read: the classic triggers are the system's "
            "approved shutdown commands - nature, rhythm, warmth, "
            "completion, trusted company, quiet. The Signature Calm "
            "Method keeps the command list posted by the panel: when "
            "the operator needs the home frequency, these are the "
            "verified inputs that bring the green board up."
        ),
    },
    # ------------------------------------------------- 19. triggers personal
    {
        "key": "calm_triggers_personal",
        "name": "Personal Triggers: Memories, Places, and Private Associations",
        "group": "Triggers",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Beyond the classics, everyone carries a private set of "
            "calm triggers - forged by their own history, meaningless "
            "to anyone else, and often more powerful than the "
            "universals. A particular song from a safe summer. The "
            "smell of a grandmother's kitchen. The exact weight of a "
            "childhood blanket. A bus route taken every day for years, "
            "whose turns the body knows by heart. The sound of a "
            "specific person's key in the door. These work by "
            "association: the trigger was present during past calm, "
            "and the nervous system filed it under safety - now the "
            "cue alone can call up the state. Anniversaries work the "
            "same way in reverse: the date the hard thing ended can "
            "bring a wave of calm every year, the body's memorial to "
            "its own survival. Personal triggers are also the most "
            "fragile: if the safe place becomes unsafe, or the person "
            "is lost, the trigger can flip - the song that calmed now "
            "aches. People curate these triggers instinctively: the "
            "mug they always reach for, the chair that is theirs, the "
            "evening walk with its fixed route. It looks like habit; "
            "underneath, it is a personal calm infrastructure, built "
            "one association at a time, and it deserves the same "
            "respect as any other foundation."
        ),
        "how_it_works": (
            "Personal triggers run on associative learning - the same "
            "machinery as classical conditioning, but for safety "
            "instead of fear. When a neutral cue (a song, a smell, a "
            "route) repeatedly co-occurs with the parasympathetic "
            "state of calm, the brain links them: the cue becomes a "
            "conditioned safety signal, able to nudge the autonomic "
            "system toward rest on its own. This is why the triggers "
            "are idiosyncratic - they are autobiographical, written by "
            "the individual's own reinforcement history. The "
            "fragility follows the same law: if the cue later "
            "co-occurs with distress, the association updates - "
            "extinction and counter-conditioning apply to safety "
            "signals too. The curation instinct is the person "
            "instinctively maintaining their conditioned safety "
            "environment, the way an animal maintains its burrow. "
            "Deliberately building such triggers - pairing a breath "
            "pattern or a place with regular calm - is one of the "
            "oldest self-regulation techniques, because it recruits "
            "the brain's own association machinery as an ally."
        ),
        "key_points": [
            "Personal triggers are autobiographical: a song, a smell, "
            "a route, a key in the door - meaningless to others, "
            "powerful to the owner.",
            "They work by associative learning: the cue co-occurred "
            "with past calm and became a conditioned safety signal.",
            "They are fragile: if the safe context turns unsafe, the "
            "association updates and the trigger can flip.",
            "People curate them instinctively - the mug, the chair, "
            "the fixed walk - building personal calm infrastructure.",
            "New safety associations can be deliberately built by "
            "pairing a cue with regular calm.",
        ],
        "requirements": [
            "Give concrete private-trigger examples; keep them ordinary.",
            "Explain the conditioning mechanism in plain words.",
            "Include the fragility/flip case honestly.",
        ],
        "standards": [
            "Association mechanism stated without jargon walls.",
            "Autobiographical nature emphasized - no universalizing.",
            "Deliberate building framed as an old technique, not a "
            "new discovery.",
        ],
        "citations": [
            "Lazarus, R. S. (1991). Emotion and adaptation.",
            "Frijda, N. H. (1986). The Emotions.",
            "Barrett, L. F. (2017). How Emotions Are Made.",
        ],
        "sig_lens": (
            "The Signature read: personal triggers are the operator's "
            "custom hotkeys to the home frequency - programmed by "
            "their own history, faster than any manual command. The "
            "Signature Calm Method respects the custom layout: map "
            "your own hotkeys, protect the associations, and keep the "
            "personal panel calibrated to your own hand."
        ),
    },
    # ------------------------------------------------- 20. surprise triggers
    {
        "key": "calm_triggers_surprise",
        "name": "Surprise Triggers: The Odd, Unexpected Routes to Calm",
        "group": "Triggers",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Some triggers of calm make no sense until they do. The "
            "sound of a vacuum cleaner putting a baby - and some "
            "adults - straight to sleep: white noise at the right "
            "pitch masks the startling small sounds that keep the "
            "threat system awake. Doing dishes by hand: warm water, "
            "repetitive motion, a small completable task - people "
            "report their minds quieting at the sink more reliably "
            "than on the meditation cushion. Driving a familiar "
            "highway at night: the lane markers ticking past, the "
            "engine's drone, no decisions required - the perfect "
            "low-demand cocoon. Organizing a drawer: the tiny satisfactions "
            "of order, each object finding its place, the world "
            "narrowed to something fixable. Watching someone else "
            "work with skill - a craftsperson, a street sweeper with "
            "a practiced rhythm: the observer's nervous system "
            "borrows the worker's unhurried competence. Even mild "
            "monotony can do it: the long meeting that asks nothing, "
            "the waiting room with its soft hum. The pattern "
            "underneath the oddness: low demand plus gentle rhythm "
            "plus a thread of order. The threat system, finding "
            "nothing to do and a steady beat to follow, stands down "
            "out of sheer boredom - and boredom, given a rhythm, "
            "becomes calm."
        ),
        "how_it_works": (
            "Surprise triggers work because the threat system is "
            "cheap to fool in one specific way: it monitors for "
            "novelty and demand, and when both stay low, it powers "
            "down regardless of how dignified the setting is. White "
            "noise works by masking - the auditory startle circuit "
            "never fires, so arousal never spikes. Repetitive manual "
            "tasks work through entrainment plus completable order: "
            "the rhythm pulls physiology slow while each finished "
            "micro-task (a clean plate, a sorted drawer) delivers a "
            "tiny completion signal, closing micro-loops of "
            "unfinished business. Skilled-work watching works "
            "through a mix of co-regulation and attentional capture: "
            "attention rests on the rhythm instead of scanning, and "
            "the observed competence reads as safety. The highway "
            "case adds sensory cocooning - steady drone, predictable "
            "visual flow, minimal decisions - the exact inverse of "
            "the alarm recipe (novelty plus demand). None of this "
            "requires the person's belief or intention, which is "
            "why these triggers surprise: the body settles first, "
            "and the mind notices after."
        ),
        "key_points": [
            "Odd triggers: vacuum hum, hand-washing dishes, night "
            "highway driving, organizing drawers, watching skilled work.",
            "The pattern: low demand plus gentle rhythm plus a thread "
            "of order.",
            "White noise works by masking startle cues; repetition "
            "works by entrainment plus micro-completions.",
            "Skilled-work watching settles through co-regulation and "
            "captured attention.",
            "The body settles first and the mind notices after - no "
            "belief or intention required.",
        ],
        "requirements": [
            "Give genuinely odd, concrete triggers - not the classics "
            "repeated.",
            "State the underlying pattern that unites them.",
            "Keep it descriptive; no prescribing.",
        ],
        "standards": [
            "Each odd trigger gets its mechanism, not just its name.",
            "The novelty-plus-demand inverse stated as the alarm recipe.",
            "Body-first ordering emphasized.",
        ],
        "citations": [
            "Porges, S. W. (2011). The Polyvagal Theory.",
            "Benson, H. (1975). The Relaxation Response.",
            "Frijda, N. H. (1986). The Emotions.",
        ],
        "sig_lens": (
            "The Signature read: surprise triggers are undocumented "
            "inputs that still drive the panel green - the system "
            "accepts more shutdown commands than the manual lists. "
            "The Signature Calm Method logs them without snobbery: "
            "if the dishes or the highway bring the home frequency, "
            "they are valid commands, filed under operator notes."
        ),
    },
    # ------------------------------------------------- 21. chain reactions
    {
        "key": "calm_chain_reactions",
        "name": "Chain Reactions: How One Calm Trigger Cascades",
        "group": "Triggers",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Calm spreads in chains - one trigger unlocking the next, "
            "each making the following one easier. It starts small: "
            "Daniel gets home, kicks off his shoes, and sits down for "
            "one minute of doing nothing. That minute of stillness "
            "slows his breathing. The slower breathing loosens his "
            "shoulders. The loosened shoulders make the chair feel "
            "more comfortable, so he stays. Staying still, he "
            "notices the evening light on the wall - and noticing it, "
            "he feels a flicker of contentment. The contentment "
            "reminds him the day went adequately; the adequate day "
            "lets him release the last work thought; releasing it, "
            "his stomach unclenches and he realizes he is hungry in "
            "the pleasant way. By dinner he is thoroughly, deeply "
            "calm - and it all chained from one minute of sitting "
            "down. The cascade runs on a simple rule: each settling "
            "lowers the bar for the next. A slightly calmer body "
            "notices pleasant things it would have missed; noticing "
            "them deepens the calm; the deeper calm releases more "
            "tension; the released tension frees attention further. "
            "Chains can also be social: one calm person slows a "
            "room, the slowed room keeps everyone calmer, and the "
            "evening steadies itself. The practical upshot is "
            "encouraging: you do not need to achieve calm all at "
            "once. You only need the first link - one slow breath, "
            "one minute of stillness - and the chain does the rest."
        ),
        "how_it_works": (
            "Cascades work through positive feedback between "
            "physiology, attention, and appraisal. The first link is "
            "always physiological or behavioral - a breath, a "
            "posture, a minute of stillness - because the body is "
            "the fastest lever. The slowed body changes what "
            "attention can do: threat-scanning eases, so attention "
            "lands on pleasant neutral detail (light on a wall), "
            "which the appraisal system reads as safety evidence, "
            "which deepens the physiological settling further. "
            "Each loop lowers arousal a notch, and lower arousal "
            "makes the next loop easier - the threshold for "
            "noticing good things drops as calm rises. Social "
            "chains add co-regulation: calm physiology is "
            "contagious through posture, voice tempo, and facial "
            "softness, so one settled nervous system becomes "
            "safety evidence for every other system in range. "
            "This is why calm practices emphasize the first "
            "small step so heavily: the chain is self-"
            "amplifying, so the only expensive link is the "
            "first one."
        ),
        "key_points": [
            "Calm cascades: one trigger (a minute of stillness) unlocks "
            "the next (slower breath), each lowering the bar further.",
            "The loop: settled body frees attention, freed attention "
            "finds safety evidence, safety evidence deepens settling.",
            "Chains go social: one calm person slows a room through "
            "co-regulation.",
            "The mechanism is positive feedback - self-amplifying once "
            "started.",
            "You only need the first link; the chain does the rest.",
        ],
        "requirements": [
            "Walk a concrete chain link by link; no abstract claims "
            "without the walk.",
            "Include the social chain, not just the solo one.",
            "Descriptive; the practical upshot stays general.",
        ],
        "standards": [
            "Each link's mechanism named (physiology, attention, "
            "appraisal).",
            "First-link-is-cheapest principle stated.",
            "Social chain tied to co-regulation.",
        ],
        "citations": [
            "Porges, S. W. (2011). The Polyvagal Theory.",
            "Lazarus, R. S. (1991). Emotion and adaptation.",
            "Fredrickson, B. L. (1998). What good are positive emotions?",
        ],
        "sig_lens": (
            "The Signature read: the chain reaction is the system's "
            "auto-sequence - pull the first lever and the panel walks "
            "itself to green, gauge by gauge. The Signature Calm "
            "Method programs the sequence deliberately: first link "
            "manual, the rest automatic - the home frequency as a "
            "self-running routine."
        ),
    },
    # ------------------------------------------------- 22. actions
    {
        "key": "calm_actions",
        "name": "What People Do: Typical Actions of the Calm",
        "group": "How It Shows in Behavior",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Calm has a behavioral signature - things calm people "
            "reliably do. They pause: before answering, before "
            "deciding, before reacting - the pause is the visible "
            "form of unhurried appraisal. They move deliberately: "
            "setting things down rather than dropping them, closing "
            "doors rather than letting them slam, turning to face "
            "people fully. They simplify: a calm person in a messy "
            "situation starts tidying - not from anxiety but from "
            "the settled impulse to make order where they can. They "
            "listen longer: without the pressure to respond, they let "
            "the other person finish, ask the second question, and "
            "hear what was actually said. They help steadily: calm "
            "is the state from which people do sustained good work - "
            "the nurse's unhurried rounds, the teacher's patient "
            "re-explanation, the friend who just stays. They also "
            "disengage cleanly: a calm person can leave an argument, "
            "close the laptop, or end the day without the trailing "
            "static of unfinished arousal - the off-switch works. "
            "None of this is passivity. The calm firefighter advances "
            "on the fire; the calm surgeon makes the cut; the calm "
            "parent holds the boundary. Calm does not remove action - "
            "it removes the noise around action, so the action lands "
            "clean."
        ),
        "how_it_works": (
            "Calm's actions all flow from two conditions: low "
            "arousal and freed attention. The pause comes from "
            "unhurried appraisal - with no alarm demanding an "
            "instant answer, the slower deliberative systems get "
            "their say, which is why calm decisions age better. "
            "Deliberate movement comes from the motor-arousal "
            "coupling running in reverse: the settled system moves "
            "at its own tempo rather than at alarm tempo. The "
            "simplifying impulse reflects the appraisal of "
            "manageability - the mind, finding the world workable, "
            "extends the workability outward. Longer listening is "
            "freed attention: without threat-scanning consuming "
            "bandwidth, the full channel goes to the other person. "
            "Steady helping is calm's action tendency in its "
            "purest form - approach and tend, the parasympathetic "
            "counterpart to fight-or-flight's attack and flee. "
            "Clean disengagement is the off-switch working: with "
            "no residual arousal demanding resolution, the person "
            "can simply stop."
        ),
        "key_points": [
            "The pause: calm's visible form - unhurried appraisal "
            "before answering, deciding, reacting.",
            "Deliberate movement, simplifying impulse, longer "
            "listening, steady helping, clean disengagement.",
            "Calm is not passivity: the firefighter advances, the "
            "surgeon cuts - calm removes the noise around action.",
            "All actions flow from low arousal plus freed attention.",
            "Steady helping is calm's action tendency: approach and "
            "tend.",
        ],
        "requirements": [
            "List the characteristic actions with concrete examples.",
            "Refute the passivity reading explicitly.",
            "No diagnosing; descriptive only.",
        ],
        "standards": [
            "Each action tied to its condition (low arousal, freed "
            "attention).",
            "Action tendency named: approach and tend.",
            "High-stakes examples included (firefighter, surgeon).",
        ],
        "citations": [
            "Frijda, N. H. (1986). The Emotions.",
            "Lazarus, R. S. (1991). Emotion and adaptation.",
            "Fredrickson, B. L. (1998). What good are positive emotions?",
        ],
        "sig_lens": (
            "The Signature read: calm's actions are the system "
            "executing at home frequency - every move deliberate, "
            "every pause placed, no wasted motion. The Signature "
            "Calm Method treats behavior as the output log: pause, "
            "deliberate move, simplify, listen, help, disengage "
            "clean - the green-board operator's standard procedure."
        ),
    },
    # ------------------------------------------------- 23. speech
    {
        "key": "calm_speech",
        "name": "What People Say: The Speech Patterns of Calm",
        "group": "How It Shows in Behavior",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "You can hear calm before you see it. The voice drops a "
            "little in pitch and slows in pace - not drawling, just "
            "unhurried, with natural pauses between thoughts. Volume "
            "settles to conversational; calm people rarely need to "
            "raise their voices because they are not competing with "
            "their own arousal. The characteristic phrases are "
            "hedged and spacious: 'Let's think this through,' 'Take "
            "your time,' 'One thing at a time,' 'We'll figure it "
            "out.' Questions outnumber declarations - calm asks "
            "before it tells, because it can afford the wait. There "
            "is a notable absence of intensifiers: fewer 'always,' "
            "'never,' 'terrible,' 'amazing' - the calm speaker "
            "describes rather than inflames. Tone carries the rest: "
            "even, warm at the edges, with a downward inflection at "
            "the ends of sentences that signals completion rather "
            "than alarm. In disagreement, the calm voice does "
            "something distinctive: it gets quieter, not louder. "
            "'I see it differently' lands softly and therefore "
            "lands harder. And in crisis, the calm voice is the one "
            "people obey - the pilot's 'brace, brace,' the nurse's "
            "'look at me, breathe with me' - because a steady voice "
            "is safety evidence, and frightened nervous systems "
            "follow it like a lighthouse."
        ),
        "how_it_works": (
            "Calm speech is the vocal tract under parasympathetic "
            "dominance. Lower pitch comes from released laryngeal "
            "tension; slower pace from unhurried respiratory rhythm - "
            "the voice literally rides the slow breath. The "
            "phrase patterns reflect freed deliberative capacity: "
            "with working memory not consumed by threat-monitoring, "
            "the speaker can hold nuance, ask genuine questions, and "
            "skip the intensifiers that aroused speech uses as "
            "shortcuts. The downward end-of-sentence inflection is "
            "the prosodic form of completion - the speaker's system "
            "signaling 'this thought is finished, no alarm attached.' "
            "Getting quieter in disagreement is strategic without "
            "being calculated: low arousal removes the volume "
            "escalation reflex, and the contrast makes the words "
            "more salient. The crisis-voice effect is co-regulation "
            "through audition - the listener's nervous system reads "
            "the steady prosody as safety evidence and entrains to "
            "it, which is why the calm voice in an emergency is "
            "obeyed before it is understood."
        ),
        "key_points": [
            "Voice: slightly lower pitch, unhurried pace, conversational "
            "volume, natural pauses.",
            "Phrases: 'Let's think this through,' 'One thing at a time' "
            "- questions outnumber declarations; intensifiers vanish.",
            "Tone: even, warm-edged, downward inflections signaling "
            "completion, not alarm.",
            "In disagreement the calm voice gets quieter - and lands "
            "harder.",
            "In crisis the steady voice is obeyed before it is "
            "understood: prosody as safety evidence.",
        ],
        "requirements": [
            "Cover voice qualities, characteristic phrases, and tone.",
            "Include disagreement and crisis as special cases.",
            "Descriptive only; no labeling speakers.",
        ],
        "standards": [
            "Each speech feature tied to its mechanism (laryngeal "
            "release, breath rhythm, freed working memory).",
            "Quieter-in-disagreement explained, not just noted.",
            "Crisis effect tied to co-regulation.",
        ],
        "citations": [
            "Porges, S. W. (2011). The Polyvagal Theory.",
            "Scherer, K. R. (2005). What are emotions?",
            "Frijda, N. H. (1986). The Emotions.",
        ],
        "sig_lens": (
            "The Signature read: the calm voice is the system's "
            "audio output at home frequency - low, unhurried, "
            "complete. The Signature Calm Method treats speech as "
            "the broadcast channel: set the voice to the green-board "
            "setting and every listener's panel starts drifting "
            "toward green with it."
        ),
    },
    # ------------------------------------------------- 24. decisions
    {
        "key": "calm_decisions",
        "name": "How Calm Changes Decisions and Judgment",
        "group": "How It Shows in Behavior",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Calm changes what people choose, and the changes are "
            "systematic. Time horizon lengthens: the calm decider "
            "weighs next month alongside next hour, while the "
            "agitated decider discounts the future steeply - urgency "
            "makes everything about now. Risk reads accurately: "
            "calm neither inflates threats (as fear does) nor "
            "dismisses them (as excitement can); the calm investor, "
            "surgeon, or parent sees the odds closer to their true "
            "size. Other people stay human: under alarm, others "
            "become obstacles or tools; in calm, they remain people "
            "with their own reasons, which is why calm negotiators "
            "find trades that frantic ones miss. Reversibility is "
            "respected: calm decision-makers prefer the choice that "
            "can be undone, and they build in checkpoints - not from "
            "timidity but from the spacious sense that there is time "
            "to correct. Perhaps most importantly, calm tolerates "
            "not deciding: the agitated mind must choose now to end "
            "the discomfort, while the calm mind can hold a question "
            "open, gather one more fact, sleep on it. People who "
            "make their biggest decisions calm - the house, the "
            "job, the apology - consistently report fewer regrets, "
            "not because calm is magic but because it removes the "
            "two great distorters: the rush and the dread."
        ),
        "how_it_works": (
            "Decision quality under calm follows from the "
            "neurochemistry of low arousal. High arousal floods the "
            "system with norepinephrine and cortisol, which narrow "
            "attention, steepen temporal discounting (the future "
            "matters less), and bias appraisal toward threat - the "
            "classic 'tunnel' of stress. Calm reverses each: "
            "moderate arousal restores prefrontal function, so "
            "working memory holds more options, time horizons "
            "widen, and probabilities are estimated with less "
            "distortion. The other-people effect is attentional: "
            "threat-scanning consumes the bandwidth needed for "
            "perspective-taking, and calm returns it. Tolerance "
            "for not deciding is the deepest mechanism - "
            "deciding-to-end-discomfort is an arousal-driven "
            "motive, and when arousal is low the motive "
            "evaporates, leaving the decision to be made on its "
            "merits. None of this guarantees good outcomes; it "
            "only removes systematic distortion, which is why calm "
            "improves the odds rather than ensuring them."
        ),
        "key_points": [
            "Time horizon lengthens: next month weighed alongside next "
            "hour; urgency's now-bias fades.",
            "Risk reads accurately: threats neither inflated nor "
            "dismissed - odds seen near true size.",
            "Others stay human: perspective-taking bandwidth returns, "
            "so trades and solutions appear.",
            "Reversibility respected: undoable choices preferred, "
            "checkpoints built in.",
            "Not deciding is tolerated: the question can stay open "
            "until it is ripe.",
        ],
        "requirements": [
            "Name the specific judgment shifts; no vague 'better "
            "decisions' claims.",
            "Keep the guarantee honest: improves odds, ensures nothing.",
            "Descriptive; no financial or life advice framing.",
        ],
        "standards": [
            "Each shift tied to its mechanism (discounting, prefrontal "
            "function, attention).",
            "The two great distorters (rush and dread) named.",
            "Honesty guardrail: no outcome guarantees.",
        ],
        "citations": [
            "Lazarus, R. S. (1991). Emotion and adaptation.",
            "Frijda, N. H. (1986). The Emotions.",
            "Barrett, L. F. (2017). How Emotions Are Made.",
        ],
        "sig_lens": (
            "The Signature read: calm decisions are computations run "
            "at home frequency - full bandwidth, no distortion, the "
            "odds read true. The Signature Calm Method makes it "
            "procedure: no big call leaves the panel until the green "
            "board is confirmed - decide from the home frequency, "
            "never from the alarm."
        ),
    },
    # ------------------------------------------------- 25. under intensity
    {
        "key": "calm_under_intensity",
        "name": "Behavior Under Intensity: How Calm Actions Escalate",
        "group": "How It Shows in Behavior",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Deep calm does not just intensify mild calm's behaviors - "
            "it transforms them. The pause becomes spaciousness: at "
            "high intensity the calm person does not merely wait a "
            "beat before answering - they can hold silence for a full "
            "minute without discomfort, and the silence does work "
            "that words cannot. Deliberate movement becomes "
            "economy: every gesture counts, nothing is wasted; watch "
            "a master craftsperson or a veteran nurse and the "
            "efficiency looks like grace. Listening becomes total: "
            "the deeply calm listener tracks not just words but the "
            "pauses between them, hearing what the speaker has not "
            "said yet. Helping becomes presence: beyond doing things "
            "for people, the deeply calm person steadies by being "
            "there - the hand that does not tremble, the voice that "
            "does not waver, in the hospital room or the hard "
            "conversation. And disengagement becomes release: at "
            "depth, letting go is not a decision but a condition - "
            "grudges, deadlines, and urgencies simply stop sticking. "
            "There is a threshold quality to all of this: below it, "
            "calm behaviors are skills being practiced; above it, "
            "they are simply how the person is. People who live "
            "much of their lives past that threshold are the ones "
            "others describe as 'a calming presence' - not because "
            "they do calming things, but because their baseline "
            "re-tunes every room they enter."
        ),
        "how_it_works": (
            "The transformation at intensity is a phase change in "
            "arousal economics. At mild calm, settled behaviors cost "
            "effort - the pause is held, the listening is worked at - "
            "because residual arousal keeps pulling toward hurry. "
            "Past a threshold of depth, the economics flip: arousal "
            "is so fully cleared that hurrying would cost effort and "
            "stillness is free. The pause becomes spacious because "
            "there is genuinely nothing urging speech; movement "
            "becomes economical because the motor system is no "
            "longer fighting alarm-driven jitter. Total listening "
            "is freed attention at its maximum - with threat-"
            "scanning fully offline, the entire attentional budget "
            "goes to the other person, including their subtext. "
            "Presence-as-help is co-regulation at full strength: a "
            "deeply settled nervous system is the strongest safety "
            "signal one person can give another. The 'calming "
            "presence' effect is this mechanism made durable - a "
            "person whose baseline sits past the threshold "
            "continuously broadcasts the signal, re-tuning rooms "
            "without trying."
        ),
        "key_points": [
            "Intensity transforms rather than merely scaling: pause "
            "becomes spaciousness, movement becomes economy.",
            "Listening becomes total - tracking pauses and subtext; "
            "helping becomes presence - steadying by being there.",
            "Disengagement becomes release: grudges and urgencies stop "
            "sticking as a condition, not a decision.",
            "The mechanism is a phase change in arousal economics: "
            "past the threshold, stillness is free and hurrying costs.",
            "'A calming presence' is a baseline past the threshold, "
            "re-tuning rooms without trying.",
        ],
        "requirements": [
            "Show transformation, not just more-of-the-same.",
            "Name the threshold quality explicitly.",
            "No mysticism; keep the mechanism plain.",
        ],
        "standards": [
            "Phase-change framing carried through each behavior.",
            "Arousal economics stated as the mechanism.",
            "Presence effect tied to co-regulation.",
        ],
        "citations": [
            "Frijda, N. H. (1986). The Emotions.",
            "Porges, S. W. (2011). The Polyvagal Theory.",
            "Fredrickson, B. L. (1998). What good are positive emotions?",
        ],
        "sig_lens": (
            "The Signature read: at intensity the home frequency "
            "stops being a setting and becomes the system's nature - "
            "the panel is not set to green, it is green. The "
            "Signature Calm Method aims past the threshold on "
            "purpose: practice until stillness is free, and the "
            "operator becomes the calming presence - the walking "
            "green board."
        ),
    },
    # ------------------------------------------------- 26. healthy
    {
        "key": "calm_healthy",
        "name": "Healthy Expression: Saying It, Showing It, Channeling It",
        "group": "Expressing It Healthily",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Calm is expressed healthily when it is shown, shared, "
            "and put to work - not hoarded. Saying it: naming the "
            "state out loud - 'I'm feeling calm about this,' 'Let's "
            "slow down a moment' - gives others permission to "
            "settle and makes the state itself more durable, "
            "because declared calm is harder to abandon. Showing "
            "it: the open posture, the unhurried voice, the "
            "willingness to be visibly at ease even when the room "
            "is not - this is not performance but broadcast, and "
            "it steadies others through co-regulation. Channeling "
            "it: calm is fuel, and healthy expression spends it on "
            "something - the hard conversation held gently, the "
            "careful work done well, the help given steadily. A "
            "person who channels calm into the difficult email, "
            "the patient explanation, or the steady hand in a "
            "crisis is expressing the emotion at its full value. "
            "Healthy expression also includes protecting it: "
            "stepping away before the buffer empties, saying no to "
            "the extra demand, keeping the evening walk sacred. "
            "This is not selfishness - it is maintenance. The "
            "calm that is spent wisely and replenished regularly "
            "becomes a durable trait; the calm that is treated as "
            "infinite gets spent down to fumes, and then there is "
            "nothing left to express."
        ),
        "how_it_works": (
            "Healthy expression works through three channels that "
            "reinforce the state itself. Naming the state recruits "
            "the prefrontal cortex into partnership with the "
            "feeling - affect labeling research shows that putting "
            "feelings into words modestly damps arousal and "
            "increases regulatory control, and declared states "
            "create social accountability that steadies them. "
            "Showing it works through co-regulation in both "
            "directions: broadcasting calm settles others, and "
            "their settling becomes safety evidence that deepens "
            "your own - the social chain reaction as maintenance. "
            "Channeling it works through the action tendency: "
            "emotions are built to be spent on their function, and "
            "calm's function is steady effective action - using it "
            "completes the circuit, while hoarding it leaves the "
            "energy with nowhere to go. Protecting it is resource "
            "economics: the calm buffer is real but finite "
            "within a day, and replenishment (rest, quiet, "
            "rhythm) restores it - treating it as renewable "
            "rather than infinite is what makes it durable."
        ),
        "key_points": [
            "Saying it: naming calm aloud steadies it and gives others "
            "permission to settle.",
            "Showing it: visible ease broadcasts safety and steadies "
            "others through co-regulation.",
            "Channeling it: spending calm on its function - hard "
            "conversations, careful work, steady help - completes the "
            "circuit.",
            "Protecting it: stepping away, saying no, keeping "
            "restorative habits sacred - maintenance, not selfishness.",
            "Calm spent wisely and replenished regularly becomes a "
            "durable trait.",
        ],
        "requirements": [
            "Cover saying, showing, channeling, and protecting - all four.",
            "Frame protection as maintenance, not selfishness.",
            "General everyday guidance only; no clinical advice.",
        ],
        "standards": [
            "Each channel tied to its mechanism (labeling, "
            "co-regulation, action tendency, resource economics).",
            "The renewable-not-infinite framing explicit.",
            "Examples ordinary and actionable.",
        ],
        "citations": [
            "Lazarus, R. S. (1991). Emotion and adaptation.",
            "Frijda, N. H. (1986). The Emotions.",
            "Porges, S. W. (2011). The Polyvagal Theory.",
        ],
        "sig_lens": (
            "The Signature read: healthy expression is running the "
            "home frequency at full output - declared on the panel, "
            "broadcast to the room, spent on the work, and recharged "
            "on schedule. The Signature Calm Method treats calm as "
            "the system's prime export: generated at the home "
            "frequency, transmitted to every connected system."
        ),
    },
    # ------------------------------------------------- 27. unhealthy
    {
        "key": "calm_unhealthy",
        "name": "Unhealthy Expression: Bottling Calm and Faking It",
        "group": "Expressing It Healthily",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Calm goes wrong in two directions, and both are costly. "
            "Bottling: the person feels agitation but performs calm - "
            "jaw set, voice measured, everything held in. From the "
            "outside it looks like composure; inside, the alarm is "
            "still running at full volume, and the effort of holding "
            "the lid on consumes enormous energy. The costs arrive on "
            "schedule: tension headaches, a stomach in knots, sleep "
            "that will not come, and eventually the lid blows - the "
            "'calm' person erupts over something small, to everyone's "
            "shock including their own. Suppressed arousal does not "
            "decay; without the body's natural discharge (movement, "
            "breath, expression), it ferments. Faking: the person is "
            "not agitated but not calm either - flat, checked out - "
            "and performs serenity as a social strategy. The costs "
            "here are subtler: other people sense the incongruence "
            "(the fast blink, the held breath) and trust the person "
            "less; the faker, receiving no genuine co-regulation "
            "because nothing real was broadcast, stays dysregulated "
            "underneath the mask. Both failures share a root: the "
            "confusion of the appearance of calm with the state of "
            "calm. The appearance can be staged in seconds; the state "
            "must be built - breath by breath, release by release - "
            "and there are no shortcuts. The honest alternative to "
            "both is simple to state and hard to practice: feel "
            "what is actually there, and settle it for real."
        ),
        "how_it_works": (
            "Bottling fails through the physiology of suppression. "
            "Holding the lid on requires continuous sympathetic "
            "activation (the bracing itself is arousal) plus "
            "continuous inhibitory effort from the prefrontal cortex "
            "- two expensive systems running at once, which is why "
            "suppression is exhausting. Worse, suppression blocks "
            "the natural arousal-decay pathways: the slow exhale, "
            "the muscle release, the expressive discharge that "
            "would clear the activation never happen, so arousal "
            "stays elevated far longer than it would with "
            "expression. The eventual eruption is hydraulic: "
            "pressure held long enough finds the weakest seam. "
            "Faking fails through the social channel: human "
            "threat-detection reads micro-incongruence (fast "
            "blink over slow voice) as untrustworthiness, so the "
            "faker pays in lost trust while gaining no real "
            "settling - the autonomic system cannot be fooled by "
            "its owner's staging. Both cost more than honesty "
            "because both run the alarm and the mask "
            "simultaneously, doubling the load instead of "
            "clearing it."
        ),
        "key_points": [
            "Bottling: performing calm while agitated - the alarm runs "
            "underneath, the lid-holding exhausts, and eruption follows.",
            "Suppressed arousal does not decay; blocked from natural "
            "discharge, it ferments.",
            "Faking: performing serenity while flat - others sense the "
            "incongruence and trust less; nothing real settles.",
            "Both confuse the appearance of calm with the state; the "
            "appearance stages in seconds, the state builds breath by breath.",
            "The honest alternative: feel what is actually there, and "
            "settle it for real.",
        ],
        "requirements": [
            "Cover both failure modes with their distinct costs.",
            "Explain the eruption mechanism plainly.",
            "No diagnosing; descriptive only.",
        ],
        "standards": [
            "Suppression physiology stated (dual-system cost, blocked "
            "decay).",
            "Faking cost tied to the social trust channel.",
            "Root confusion (appearance vs state) named explicitly.",
        ],
        "citations": [
            "Frijda, N. H. (1986). The Emotions.",
            "Lazarus, R. S. (1991). Emotion and adaptation.",
            "APA Dictionary of Psychology - emotional suppression.",
        ],
        "sig_lens": (
            "The Signature read: bottling is running the alarm with "
            "the display taped green; faking is a staged panel with "
            "amber gauges underneath - both are instrument fraud. "
            "The Signature Calm Method forbids spoofed readings: feel "
            "the true state, then earn the green board for real, "
            "breath by breath."
        ),
    },
    # ------------------------------------------------- 28. practices
    {
        "key": "calm_practices",
        "name": "Everyday Practices: Small Habits That Keep Calm in Balance",
        "group": "Expressing It Healthily",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Calm is kept the way fitness is kept: not by heroic "
            "effort but by small habits, repeated. The one-breath "
            "reset: a single slow exhale, longer than the inhale, "
            "used at every transition - before answering the phone, "
            "before opening the email, before walking into the room. "
            "It takes four seconds and it works because the exhale "
            "is a direct lever on the vagus nerve. The daily walk: "
            "twenty unhurried minutes, same route, no phone - rhythm "
            "plus mild movement plus a thread of the familiar, the "
            "surprise-trigger recipe made deliberate. The evening "
            "review: five minutes before bed, running the day once "
            "without judgment, filing the unfinished under tomorrow - "
            "closing the loops so arousal has nothing to chew on "
            "overnight. The protected hour: one block of the week "
            "with nothing scheduled, defended like an appointment - "
            "the quiet trigger, kept on retainer. The tidy margin: "
            "leaving ten minutes between commitments so the day never "
            "runs at redline - transitions are where calm dies, and "
            "margins are where it survives. None of these is dramatic, "
            "and that is the point: calm is a baseline, and baselines "
            "are built by the unremarkable things done daily. People "
            "who keep these habits report the same thing - not that "
            "life got easier, but that they got steadier, and the "
            "steadiness compounds like interest."
        ),
        "how_it_works": (
            "Small habits work through dose and timing, not intensity. "
            "The one-breath reset exploits the exhale-vagus lever: "
            "each long exhale nudges parasympathetic tone upward, and "
            "used at transitions it catches arousal at its cheapest "
            "point - before it builds. The daily walk combines three "
            "calm mechanisms at low dose: rhythmic entrainment from "
            "steady stepping, mild vagal stimulation from easy "
            "movement, and safety signaling from the familiar route. "
            "The evening review works through loop-closure: "
            "unfinished business is a low-grade threat, and "
            "explicitly filing it under tomorrow removes the "
            "threat-evidence, letting arousal decay before sleep. "
            "The protected hour and tidy margins work through demand "
            "management: calm dies at transitions and under time "
            "pressure, so removing the pressure removes the killer. "
            "The compounding effect is the aftershock mechanism "
            "accumulated daily - each day's practice leaves a "
            "slightly deeper buffer, and buffers stack across weeks "
            "into a genuinely shifted baseline."
        ),
        "key_points": [
            "The one-breath reset: a single long exhale at every "
            "transition - four seconds, direct vagus lever.",
            "The daily walk: twenty unhurried minutes - rhythm, mild "
            "movement, familiar route.",
            "The evening review: five minutes filing the day under "
            "tomorrow - closing loops before sleep.",
            "The protected hour and tidy margins: defended unscheduled "
            "time and buffers between commitments - demand management.",
            "Baselines are built by unremarkable things done daily; the "
            "steadiness compounds like interest.",
        ],
        "requirements": [
            "Give concrete small habits with their timing and dose.",
            "Explain why small beats heroic.",
            "General everyday guidance only; no clinical framing.",
        ],
        "standards": [
            "Each habit tied to its mechanism.",
            "Dose and timing stated, not just the activity.",
            "Compounding framed as accumulated aftershock.",
        ],
        "citations": [
            "Benson, H. (1975). The Relaxation Response.",
            "Kabat-Zinn, J. (1990). Full Catastrophe Living.",
            "Porges, S. W. (2011). The Polyvagal Theory.",
        ],
        "sig_lens": (
            "The Signature read: the practices are the scheduled "
            "maintenance log for the home frequency - daily checks, "
            "small adjustments, buffers kept full. The Signature "
            "Calm Method runs on routine, not heroics: tend the "
            "panel daily and the green board holds for years."
        ),
    },
    # ------------------------------------------------- 29. reading others
    {
        "key": "calm_reading_others",
        "name": "Reading the Signs: Calm in Other People",
        "group": "Recognizing It in Others",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Recognizing calm in others is a practical skill - it "
            "tells you who is steady, who can be leaned on, and "
            "whether the room is safe. Read the face first: the "
            "smooth forehead, the unhurried blink, the mouth at "
            "rest with its faint lift - the absence of tension "
            "anywhere. Read the body second: shoulders low, hands "
            "open and still (not fidgeting, not clenched), posture "
            "stacked and easy, movements unhurried and complete. "
            "Read the voice third: slightly lower, slightly slower, "
            "pauses between thoughts, no edge of urgency - and in "
            "disagreement, quieter rather than louder. Read behavior "
            "fourth: the pause before answering, the willingness to "
            "listen to the end, the tidy handling of objects, the "
            "clean disengagement when something ends. Then check "
            "for congruence - the master test: do the fast small "
            "signals agree with the big slow ones? A person whose "
            "voice is measured but whose blink is rapid and whose "
            "jaw is set is performing calm, not inhabiting it. "
            "Context matters too: the surgeon before the incision, "
            "the pilot in turbulence, the friend who answers the "
            "3 a.m. call without a tremor in the voice - calm in "
            "hard places is the most reliable kind, because there "
            "is nothing easy about the situation doing the work. "
            "And remember the look-alikes: deep calm can resemble "
            "sadness (check the mouth corners - up faintly, not "
            "down) or exhaustion (check the eyes - present, not "
            "vacant)."
        ),
        "how_it_works": (
            "Reading calm works because the human visual and "
            "auditory systems are tuned threat-detectors: they "
            "scan faces and voices for tension automatically, and "
            "calm is recognized largely by the absence of alarm "
            "cues across channels. The four-channel read (face, "
            "body, voice, behavior) works because genuine calm "
            "is congruent - the same settled appraisal drives all "
            "channels at once - while performed calm leaks in "
            "the least voluntary channels (blink, breath, jaw). "
            "The congruence check is therefore the diagnostic "
            "core of the skill: agreement across channels means "
            "the state is real. Context weighting is Bayesian: "
            "calm displayed where calm is easy carries little "
            "information, while calm displayed where alarm would "
            "be expected carries a great deal - the observer's "
            "brain correctly treats hard-place calm as strong "
            "evidence of a genuinely settled system. The "
            "look-alike check prevents the two classic errors: "
            "mistaking low-tone sadness or exhaustion for calm, "
            "resolved by the mouth-corner and eye-presence tests."
        ),
        "key_points": [
            "Four-channel read: face (smooth, unhurried), body (low "
            "shoulders, open hands), voice (lower, slower, pausing), "
            "behavior (pausing, listening, clean disengagement).",
            "The congruence check is the master test: fast small "
            "signals must agree with big slow ones.",
            "Context weights the reading: calm in hard places is the "
            "most reliable kind.",
            "Look-alikes: check mouth corners (faintly up, not down) "
            "and eye presence (present, not vacant) to rule out "
            "sadness and exhaustion.",
            "The skill tells you who is steady, who can be leaned on, "
            "and whether the room is safe.",
        ],
        "requirements": [
            "Give the channel-by-channel read with concrete cues.",
            "Include the congruence test and the look-alike checks.",
            "Descriptive; never a license to label real people.",
        ],
        "standards": [
            "Each channel's cues concrete and observable.",
            "Congruence framed as the core test.",
            "Context weighting explained, not just asserted.",
        ],
        "citations": [
            "Ekman, P., & Friesen, W. V. (1978). Facial Action Coding System.",
            "Darwin, C. (1872). The Expression of the Emotions in Man and Animals.",
            "Porges, S. W. (2011). The Polyvagal Theory.",
        ],
        "sig_lens": (
            "The Signature read: reading others is remote telemetry - "
            "four channels of incoming data, checked for congruence "
            "before the reading is trusted. The Signature Calm Method "
            "trains the operator's instruments: face, body, voice, "
            "behavior - and never certifies a green board on a single "
            "channel alone."
        ),
    },
    # ------------------------------------------------- 30. support
    {
        "key": "calm_support",
        "name": "What to Say and Do When Someone Near You Needs Calm",
        "group": "Recognizing It in Others",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "When someone near you is agitated and needs settling, "
            "your calm is the tool - and how you use it matters. "
            "First, settle yourself: one slow exhale, drop your own "
            "shoulders, slow your voice half a notch. You cannot "
            "lend what you do not have, and an agitated helper "
            "escalates. Second, be the steady signal: unhurried "
            "voice, open posture, soft gaze - broadcast safety "
            "without announcing it. Third, say the settling things: "
            "'I'm here.' 'Take your time.' 'One thing at a time.' "
            "'We'll figure this out.' Short sentences, downward "
            "inflections, no rush between them. Fourth, do the "
            "grounding things: offer water, suggest sitting down, "
            "slow your own breathing audibly so theirs can follow - "
            "nervous systems entrain, and yours is the steadier "
            "metronome. Fifth, listen longer than feels necessary: "
            "let them finish, then wait one more beat - the extra "
            "silence often brings the real sentence. What you are "
            "doing, underneath it all, is co-regulation: your "
            "settled nervous system is safety evidence for theirs, "
            "and borrowed calm becomes owned calm within minutes. "
            "This works on children mid-meltdown, colleagues mid-"
            "panic, and friends mid-crisis - the mechanism does not "
            "care about the relationship, only about the signal."
        ),
        "how_it_works": (
            "Supportive settling works through co-regulation, the "
            "same mechanism as the classic triggers. The helper's "
            "slow voice, open posture, and unhurried breathing are "
            "read by the other person's threat-detection as safety "
            "evidence - 'someone near me is unafraid, so the danger "
            "must be manageable' - which stands down their alarm "
            "and lets their parasympathetic system take over. "
            "Audible slow breathing adds entrainment: respiratory "
            "rhythms synchronize between people in close contact, "
            "so the helper's breath literally paces the other's. "
            "The settling phrases work through appraisal: 'one "
            "thing at a time' reframes an overwhelming whole into "
            "a manageable next step, and manageability is calm's "
            "core appraisal. Listening longer works through "
            "felt-safety: being fully heard without interruption "
            "signals that the situation is under control enough "
            "for patience, which is itself calming. Self-settling "
            "first is not optional - an agitated helper broadcasts "
            "alarm cues (fast voice, tense face) that the other's "
            "system reads as confirmation of danger."
        ),
        "key_points": [
            "Settle yourself first: one slow exhale, dropped shoulders, "
            "voice slowed half a notch - you cannot lend what you lack.",
            "Be the steady signal: unhurried voice, open posture, soft "
            "gaze - broadcast safety without announcing it.",
            "Say the settling things: 'I'm here.' 'Take your time.' "
            "'One thing at a time.' Short, downward, unrushed.",
            "Do the grounding things: water, sitting, audible slow "
            "breathing - your rhythm paces theirs.",
            "Listen longer than feels necessary; the extra silence often "
            "brings the real sentence.",
        ],
        "requirements": [
            "Give concrete sayings and doings, in order.",
            "Self-settling first - non-negotiable and explained.",
            "General everyday guidance; no clinical framing.",
        ],
        "standards": [
            "Each step tied to co-regulation or appraisal mechanism.",
            "Phrases short, quotable, and in the calm voice.",
            "Mechanism relationship-independent, stated plainly.",
        ],
        "citations": [
            "Porges, S. W. (2011). The Polyvagal Theory.",
            "Lazarus, R. S. (1991). Emotion and adaptation.",
            "Benson, H. (1975). The Relaxation Response.",
        ],
        "sig_lens": (
            "The Signature read: supporting another is transmitting "
            "the home frequency - your green board becomes their "
            "reference signal until their own panel steadies. The "
            "Signature Calm Method treats it as a relay procedure: "
            "stabilize your own panel first, then broadcast - the "
            "strongest transmitter in the room sets the frequency."
        ),
    },
    # ------------------------------------------------- 31. mistakes
    {
        "key": "calm_mistakes",
        "name": "What NOT to Do: Mistakes That Wreck Someone's Calm",
        "group": "Recognizing It in Others",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "The common mistakes are all ways of adding alarm to a "
            "person who needs less of it. Rushing them: 'Hurry up,' "
            "'We don't have time for this' - urgency is contagious, "
            "and importing your deadline into their nervous system "
            "detonates whatever settling had begun. Minimizing: 'Calm "
            "down,' 'It's not a big deal,' 'You're overreacting' - "
            "these do not reduce arousal; they add insult to it, "
            "because the person now must defend the legitimacy of "
            "their feeling on top of feeling it. The phrase 'calm "
            "down' has probably never calmed anyone down. Mirroring "
            "the agitation: raising your voice to match theirs, "
            "pacing because they pace - your alarm becomes their "
            "evidence that the situation is as bad as it feels. "
            "Problem-solving too early: launching into fixes while "
            "they are still flooded - the thinking brain is offline "
            "during high arousal, so solutions bounce off and the "
            "person feels unheard on top of upset. And the quiet "
            "one: withdrawing - going silent, leaving the room "
            "without a word - which the agitated system reads as "
            "abandonment, spiking alarm further. The pattern in "
            "every mistake is the same: it either adds threat-"
            "evidence or removes safety-evidence. The correction "
            "is equally uniform: subtract alarm, add safety - "
            "slow down, stay present, and let the settling happen "
            "at its own pace."
        ),
        "how_it_works": (
            "Each mistake works by feeding the threat system. "
            "Rushing adds time-pressure, which the appraisal "
            "system reads as 'insufficient resources for the "
            "demand' - the direct opposite of calm's safety-plus-"
            "sufficiency appraisal. Minimizing adds social threat: "
            "being told your feeling is illegitimate registers as "
            "a status/rejection cue, layering a second alarm over "
            "the first - which is why 'calm down' backfires so "
            "reliably. Mirroring works through co-regulation in "
            "reverse: the other's system reads your agitation as "
            "confirmation of danger, amplifying their own. Early "
            "problem-solving fails on neurochemistry: high "
            "arousal suppresses prefrontal function, so complex "
            "input cannot be processed - and the attempt "
            "signals 'you should be thinking clearly,' adding "
            "performance pressure. Withdrawal removes the "
            "strongest safety signal available - a present calm "
            "other - which the alarm system reads as isolation "
            "during threat, one of its oldest triggers. All five "
            "are alarm-adders or safety-removers; effective "
            "support is always the reverse."
        ),
        "key_points": [
            "Rushing them imports your urgency into their nervous "
            "system and detonates the settling.",
            "Minimizing ('calm down,' 'you're overreacting') adds "
            "social threat on top of the original alarm.",
            "'Calm down' has probably never calmed anyone down.",
            "Mirroring agitation, problem-solving too early, and "
            "silent withdrawal all feed the threat system.",
            "Every mistake adds threat-evidence or removes safety-"
            "evidence; the correction is always the reverse.",
        ],
        "requirements": [
            "Name each mistake with its typical phrasing.",
            "Explain the mechanism of backfire for each.",
            "Descriptive; the correction stays general.",
        ],
        "standards": [
            "Threat-evidence vs safety-evidence framing unifies the list.",
            "The 'calm down' failure given its own emphasis.",
            "Each mistake's correction implied by the mechanism.",
        ],
        "citations": [
            "Lazarus, R. S. (1991). Emotion and adaptation.",
            "Porges, S. W. (2011). The Polyvagal Theory.",
            "Frijda, N. H. (1986). The Emotions.",
        ],
        "sig_lens": (
            "The Signature read: the mistakes are interference on "
            "the channel - noise injected into a system trying to "
            "find its frequency. The Signature Calm Method lists "
            "them as prohibited transmissions: never rush, never "
            "minimize, never mirror, never abandon - protect the "
            "signal while the other panel finds green."
        ),
    },
    # ------------------------------------------------- 32. related map
    {
        "key": "calm_related_map",
        "name": "Related Emotions Map: Neighbors, Opposites, Close Cousins",
        "group": "Related Emotions and Mixes",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Calm's neighborhood on the emotion map, walked street by "
            "street. Nearest neighbors: serenity (calm with a "
            "luminous, almost spiritual quality - the difference is "
            "flavor, not structure), contentment (calm plus "
            "satisfaction with what one has - add 'my life is good' "
            "to calm and you get contentment), relief (calm arriving "
            "fresh after fear - the exhale still audible in it), "
            "relaxation (calm of the body specifically - the muscles' "
            "version of the same state), tranquility (calm stretched "
            "across a scene or a season - a place or time rather than "
            "a moment). Close cousins often confused: peace (calm as "
            "a condition of the world, not just the person - "
            "interpersonal or global), patience (calm under delay "
            "specifically - the willingness to wait without friction), "
            "equanimity (calm under provocation specifically - the "
            "steadiness that does not wobble when pushed). Opposites: "
            "anxiety (the same body with the alarm on - threat "
            "appraised, resources doubted), agitation (alarm with "
            "motion - the fidgeting, pacing version), panic (alarm "
            "at full volume - the system's fire bell). Telling "
            "cousins apart is a practical art: ask what the state "
            "is about. If it is about safety in this moment, it is "
            "calm. If it is about satisfaction with one's life, "
            "contentment. If it is about the world being at rest, "
            "peace. If it is about waiting well, patience. If it is "
            "about not wobbling when pushed, equanimity. The map "
            "matters because the wrong label sends you to the wrong "
            "tools - but the right neighborhood tells you that "
            "calm's tools (breath, release, safety-evidence) work, "
            "with adjustments, on the whole street."
        ),
        "how_it_works": (
            "The map is organized by appraisal differences - what "
            "each state is 'about' - because appraisal is what "
            "separates neighbors that share physiology. Calm, "
            "serenity, contentment, and relief all run the "
            "parasympathetic profile, but their appraisals differ: "
            "calm appraises the moment as safe and manageable; "
            "contentment adds a positive life-evaluation; relief "
            "adds the recent removal of threat; serenity adds a "
            "quality of uplift or transcendence. The cousins are "
            "separated by scope: peace scopes the state to the "
            "world, patience to delay, equanimity to provocation - "
            "same steadiness, different test. The opposites share "
            "the body's arousal machinery run in reverse: anxiety "
            "is calm's appraisal inverted (threat, insufficient "
            "resources), agitation adds motor restlessness, panic "
            "maxes the volume. This appraisal-first organization "
            "is why the 'what is it about' question resolves "
            "confusion so reliably - it queries the exact "
            "dimension that distinguishes the neighbors."
        ),
        "key_points": [
            "Neighbors: serenity, contentment, relief, relaxation, "
            "tranquility - same family, different tints.",
            "Cousins: peace (world at rest), patience (waiting well), "
            "equanimity (steady under provocation) - same steadiness, "
            "different test.",
            "Opposites: anxiety, agitation, panic - the arousal "
            "machinery run in reverse at rising volumes.",
            "The separator is appraisal: ask what the state is about.",
            "Right neighborhood, right tools: calm's toolkit works "
            "across the street with adjustments.",
        ],
        "requirements": [
            "Map neighbors, cousins, and opposites with the "
            "distinguishing question for each.",
            "Give the 'what is it about' test explicitly.",
            "No diagnosing; descriptive only.",
        ],
        "standards": [
            "Appraisal-first organization throughout.",
            "Each neighbor distinguished by its added element.",
            "Opposites graded by volume (anxiety, agitation, panic).",
        ],
        "citations": [
            "Russell, J. A. (1980). A circumplex model of affect.",
            "Plutchik, R. (1980). Emotion: A psychoevolutionary synthesis.",
            "Lazarus, R. S. (1991). Emotion and adaptation.",
            "Scherer, K. R. (2005). What are emotions?",
        ],
        "sig_lens": (
            "The Signature read: the map is the full panel layout - "
            "calm at home position, neighbors on adjacent dials, "
            "opposites on the far side of the board. The Signature "
            "Calm Method navigates by it: know every gauge's home "
            "reading and you will never mistake one signal for "
            "another."
        ),
    },
    # ------------------------------------------------- 33. mixes
    {
        "key": "calm_mixes",
        "name": "Emotion Mixes: Calm Blended With Other Emotions",
        "group": "Related Emotions and Mixes",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Calm blends the way colors do - and the blends have "
            "their own names and feels. Calm plus joy: cheerful "
            "ease - the picnic mood, the good-day glow; energy "
            "without edge, warmth without urgency. The body is "
            "settled and the spirits are up - the blend people "
            "mean by 'happy' on an ordinary good day. Calm plus "
            "sadness: quiet melancholy, or bittersweet - the "
            "rainy-window feeling; the ache is present but held, "
            "not fought, and there is a strange comfort in letting "
            "it be. Grief, in its later stages, often wears this "
            "blend. Calm plus anticipation: poised readiness - the "
            "athlete before the start, the speaker before the "
            "talk; the body is quiet but primed, attention "
            "gathered like a wave about to break. This is the "
            "blend of all good performance. Calm plus love: tender "
            "steadiness - the long-married couple on the porch, "
            "the parent rocking the child; affection without "
            "clutching, closeness without demand. In Plutchik's "
            "terms these are dyads - two primaries combined into "
            "a stable compound - and calm is a generous partner: "
            "it lends its steadiness to whatever it joins without "
            "erasing the partner's character. The practical note: "
            "blends are not dilutions. Bittersweet is not half-"
            "sadness; it is its own complete state, with its own "
            "texture and its own uses - and learning to recognize "
            "blends as wholes is what turns emotional literacy "
            "from a list of labels into a working instrument."
        ),
        "how_it_works": (
            "Blends work because appraisal and physiology combine "
            "independently. Calm contributes its parasympathetic "
            "profile and its safety-manageability appraisal to "
            "every mix; the partner contributes its own appraisal "
            "and arousal coloring. Calm plus joy: calm's low "
            "arousal steadies joy's higher energy, producing the "
            "sustainable glow rather than the spike - physiologically, "
            "vagal tone stays high while reward circuits hum. "
            "Calm plus sadness: the sadness appraisal (loss) "
            "persists while calm's safety appraisal contains it - "
            "'something is lost and I am still okay' - which is why "
            "the blend aches without overwhelming. Calm plus "
            "anticipation: calm's steadiness holds while the "
            "anticipation appraisal (something important is coming) "
            "primes the motor system - readiness without alarm, the "
            "vagal brake applied to an engaged engine. Calm plus "
            "love: the attachment system's warmth runs on calm's "
            "settled physiology, producing closeness without the "
            "clutching that anxious attachment adds. In each case "
            "the blend is stable because the appraisals are "
            "compatible - none of the partners demands alarm, so "
            "the parasympathetic floor holds."
        ),
        "key_points": [
            "Calm + joy: cheerful ease - settled body, spirits up; "
            "the ordinary good-day glow.",
            "Calm + sadness: bittersweet - the ache present but held, "
            "not fought; grief's later clothing.",
            "Calm + anticipation: poised readiness - quiet but primed; "
            "the blend of all good performance.",
            "Calm + love: tender steadiness - affection without "
            "clutching, closeness without demand.",
            "Blends are not dilutions - each is its own complete state; "
            "calm lends steadiness without erasing the partner.",
        ],
        "requirements": [
            "Blend calm with four partners, each with its lived feel.",
            "Use the dyad framing; keep it descriptive.",
            "End with the blends-as-wholes point.",
        ],
        "standards": [
            "Each blend gets appraisal plus physiology, not just a name.",
            "Compatibility (no partner demands alarm) stated as the "
            "stability condition.",
            "Lived examples carry each blend.",
        ],
        "citations": [
            "Plutchik, R. (1980). Emotion: A psychoevolutionary synthesis.",
            "Russell, J. A. (1980). A circumplex model of affect.",
            "Frijda, N. H. (1986). The Emotions.",
            "Fredrickson, B. L. (1998). What good are positive emotions?",
        ],
        "sig_lens": (
            "The Signature read: the blends are mixed signals on the "
            "panel - home frequency carrying a second channel, both "
            "readable at once. The Signature Calm Method treats calm "
            "as the carrier wave: modulate it with joy, sadness, "
            "anticipation, or love, and the steadiness transmits "
            "cleanly underneath every partner."
        ),
    },
    # ------------------------------------------------- 34. full simulation
    {
        "key": "calm_full_simulation",
        "name": "Full Behavioral Simulation: From Trigger Through Peak to Resolution",
        "group": "Related Emotions and Mixes",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The archive's showcase simulation - calm walking a full "
            "arc, scene by scene. Scene one, the trigger: It is 4:47 "
            "p.m. Tomas has been bracing all day - a performance "
            "review at five, his shoulders up around his ears since "
            "lunch, breath shallow. The trigger is not dramatic: he "
            "steps out of the office stairwell into the late-"
            "afternoon light, and something in the warmth and the "
            "open sky gives his system permission. He takes one "
            "long exhale - longer than the inhale - and feels his "
            "jaw unclench. Scene two, the onset: Walking to his car, "
            "the releases stack. Shoulders drop. The death-grip on "
            "his bag loosens. He notices the air smells like cut "
            "grass, and noticing it, he smiles faintly - the first "
            "genuine one since morning. His stride slows without "
            "him deciding it; his body is choosing its own tempo "
            "now. Scene three, the peak: Driving home on the "
            "familiar route, the radio low, Tomas settles into deep "
            "calm. Breath slow and full. Thoughts come one at a time "
            "and mostly do not come at all. The review is still at "
            "five tomorrow - rescheduled, the email said - and the "
            "thought of it arrives, is examined without flinching, "
            "and is set down. His hands rest open on the wheel. "
            "Scene four, the test: His phone rings - his sister, "
            "upset about their mother. Old Tomas would have "
            "tightened; this Tomas takes one breath, keeps his "
            "voice low and slow, and listens to the end. 'We'll "
            "figure it out,' he says, and means it. The agitation "
            "touches him and does not take hold - the buffer is "
            "deep. Scene five, the resolution: Home. He sits on "
            "the porch for ten minutes, doing nothing, letting the "
            "day's last light do its work. Dinner tastes like "
            "dinner. In bed, the review gets one calm look - "
            "preparation, not rumination - and sleep comes easily. "
            "The arc is complete: trigger, onset, peak, test, "
            "resolution. Nothing about the day changed except the "
            "state carrying him through it - and that changed "
            "everything."
        ),
        "how_it_works": (
            "The simulation demonstrates every mechanism in the "
            "archive working as one arc. The trigger scene shows "
            "the classic safety-signal plus the exhale-vagus lever: "
            "warmth, open sky, and one long exhale initiate the "
            "parasympathetic handoff. The onset scene shows the "
            "cascade - each release lowering the bar for the next, "
            "attention freeing to notice pleasant detail, the "
            "chain reaction in motion. The peak scene shows the "
            "systemic shift: slowed breath, single-file thoughts, "
            "the rescheduled review appraised without flinching - "
            "calm's safety-manageability appraisal handling a "
            "genuine stressor. The test scene shows the buffer at "
            "work: deep calm's aftershock absorbing a real "
            "disturbance, plus co-regulation as Tomas steadies his "
            "sister with the low slow voice. The resolution scene "
            "shows the flywheel: porch stillness, tasted dinner, "
            "easy sleep - each steadied system lowering the load "
            "on the rest, the day banked as safety evidence for "
            "tomorrow. The closing line states the archive's "
            "central claim about calm: it changes nothing in the "
            "world and everything in the carrying of it."
        ),
        "key_points": [
            "Five scenes: trigger (light, sky, one long exhale), onset "
            "(stacking releases), peak (systemic settle), test (the "
            "phone call absorbed), resolution (porch, dinner, sleep).",
            "Every archive mechanism appears: vagus lever, cascade, "
            "appraisal, buffer, co-regulation, flywheel.",
            "The stressor is real (review, family worry) - calm meets "
            "problems without being owned by them.",
            "The test proves the buffer: agitation touches and does "
            "not take hold.",
            "Central claim: calm changes nothing in the world and "
            "everything in the carrying of it.",
        ],
        "requirements": [
            "Multi-scene arc: trigger, onset, peak, test, resolution - "
            "all five.",
            "Inner monologue, body signals, facial expression, "
            "dialogue, and behavior all present across scenes.",
            "Real stressors included; no sanitized day.",
        ],
        "standards": [
            "Each scene demonstrates named archive mechanisms.",
            "The test scene proves the buffer rather than asserting it.",
            "Showcase quality: the richest single piece in the database.",
        ],
        "citations": [
            "Lazarus, R. S. (1991). Emotion and adaptation.",
            "Porges, S. W. (2011). The Polyvagal Theory.",
            "Frijda, N. H. (1986). The Emotions.",
            "Benson, H. (1975). The Relaxation Response.",
        ],
        "sig_lens": (
            "The Signature read: the full simulation is the "
            "acceptance run - the system taken from alarm through "
            "every phase back to the home frequency, under load, "
            "and holding. The Signature Calm Method certifies on "
            "this arc: trigger, onset, peak, test, resolution - "
            "five scenes, all gauges green at the end, the operator "
            "proven on the home frequency."
        ),
    },
]
