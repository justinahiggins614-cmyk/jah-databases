#!/usr/bin/env python3
"""Entries for the Guilt Emotion databases (Manon's 2026-10-17 16:15 order,
emotion series).

Descriptive and educational ONLY - the database describes and simulates
guilt; it never diagnoses real people, never labels any real person with an
emotional state, and never offers therapeutic advice beyond general, safe,
everyday guidance. No clinical language, no diagnostic labels. Healthy
expression records emphasize constructive handling.

34 records, ordered by the teaching ladder (ladder_rank 1-10,
non-decreasing), following the shared emotion-template spec:
what guilt IS -> first-person simulation -> body signals -> facial
expression -> triggers -> behavior -> healthy expression -> recognizing it
in others -> related emotions and mixes -> complex behavioral simulation.

ID prefixes: JAH-EMGU- (public) and JAH-EMGUS- (signature), verified free
in the manifest id_prefix values (zero hits) and in all
jah-databases-data-1 shard index files (zero 'JAH-EMGU' substring hits),
2026-10-17.

Public records are real, fact-checked psychology knowledge (Tangney and
Dearing, Baumeister Stillwell and Heatherton, Lewis, Tracy and Robins,
Haidt, Festinger, Lazarus, Gross, Scherer, Ekman, APA Dictionary).
Signature editions are his original Signature lens - guilt as the soul's
ledger, the honest bookkeeping of the conscience: signal, repair, and
release - never presented as authentic public record.

Never the words "bat belt" anywhere. No website references. No Facebook.
No religious talk. Nothing hate-adjacent, profane, or inappropriate.
"""

SIG_TAIL = ("Signature original - his original Signature lens: guilt as the "
            "soul's ledger, the honest bookkeeping of the conscience - "
            "signal, repair, and release. Signature editions frame every "
            "facet as the ledger balancing itself: the signal that a "
            "standard was breached, the repair that sets the account "
            "straight, and the release that lets the lesson stay without "
            "the weight. Never as a diagnosis, never labeling any real "
            "person, and never presented as authentic public record.")

CIT_TANGNEY = ("Tangney JP, Dearing RL. Shame and Guilt. Guilford Press; "
               "2002.")
CIT_BAUMEISTER = ("Baumeister RF, Stillwell AM, Heatherton TF. Guilt: an "
                  "interpersonal approach. Psychological Bulletin. "
                  "1994;115(2):243-267.")
CIT_LEWIS = ("Lewis M. Shame: The Exposed Self. Free Press; 1992.")
CIT_TRACY = ("Tracy JL, Robins RW. Putting the self into self-conscious "
             "emotions: a theoretical model. Psychological Science. "
             "2004;15(2):103-113.")
CIT_HAIDT = ("Haidt J. The moral emotions. In: Davidson RJ, Scherer KR, "
             "Goldsmith HH, editors. Handbook of Affective Sciences. Oxford "
             "University Press; 2003.")
CIT_FESTINGER = ("Festinger L. A Theory of Cognitive Dissonance. Stanford "
                 "University Press; 1957.")
CIT_LAZARUS = ("Lazarus RS. Emotion and Adaptation. Oxford University Press; "
               "1991.")
CIT_GROSS = ("Gross JJ, editor. Handbook of Emotion Regulation. 2nd ed. "
             "Guilford Press; 2014.")
CIT_SCHERER = ("Scherer KR. Appraisal considered as a process of multilevel "
               "sequential checking. In: Scherer KR, Schorr A, Johnstone T, "
               "editors. Appraisal Processes in Emotion. Oxford University "
               "Press; 2001.")
CIT_EKMAN = ("Ekman P. Emotions Revealed: Recognizing Faces and Feelings to "
             "Improve Communication and Emotional Life. Holt; 2003.")
CIT_APA = ("American Psychological Association. APA Dictionary of "
           "Psychology; current edition.")
CIT_KELTNER = ("Keltner D, Buswell BN. Embarrassment: its distinct form and "
               "appeasement functions. Psychological Bulletin. "
               "1997;122(3):250-270.")
CIT_DAMASIO = ("Damasio AR. Looking for Spinoza: Joy, Sorrow, and the "
               "Feeling Brain. Harcourt; 2003.")

ENTRIES = [
# ---------------------------------------------------------------- 1-4: what guilt IS
dict(
    key="guilt_definition", name="What Guilt Is: A Plain-Language Definition",
    group="Foundations", ladder_rank=1, ladder_tier="foundations",
    description=(
        "Guilt is the emotion you feel when you believe you have done "
        "something wrong - when your own actions fall short of your own "
        "standards. In everyday words: guilt is the conscience's "
        "bookkeeping, the inner signal that an account between you and "
        "someone else (or you and yourself) is out of balance. "
        "Psychologists describe it as a self-conscious, moral emotion - "
        "one of the feelings that only arises when a person can look at "
        "their own behavior and judge it against a standard of right and "
        "wrong. That is why young children, who have not yet built a "
        "stable set of standards, feel it later and less reliably than "
        "adults. Guilt points at what you did, not at who you are - and "
        "that distinction is the most important thing to carry into the "
        "rest of this database. The feeling comes with a built-in "
        "instruction: repair what was broken. Guilt is not inherently "
        "good or bad; it is information. What matters is whether the "
        "signal leads to honest repair or gets ignored, denied, or "
        "carried forever."),
    how_it_works=(
        "The guilt sequence runs in four beats: standard, transgression, "
        "attribution, and repair urge. First, a person holds a standard - "
        "a rule about how people should be treated, learned from family, "
        "community, and experience. Second, an event seems to break that "
        "standard: a promise forgotten, a sharp word said, a shortcut "
        "taken at someone else's expense. Third comes the attribution "
        "step, which is where guilt is decided: the person judges "
        "themselves responsible for the breach, at least in part. Without "
        "that self-attribution there is no guilt - there may be "
        "disappointment, anger, or sadness instead. Fourth, the repair "
        "urge arrives: apologize, confess, fix, make amends. Researchers "
        "call guilt an interpersonal emotion because its job is social "
        "glue - it pressures the person who caused harm to restore the "
        "relationship. Understanding this chain is the key to everything "
        "else in this database: dispute the attribution and the guilt "
        "shifts; honor the repair urge and the guilt settles."),
    key_points=[
        "Guilt is a self-conscious, moral emotion: it needs a standard and a self that can judge itself against it.",
        "The core signal is: I did something that broke one of my own standards.",
        "The sequence is standard -> transgression -> self-attribution -> repair urge; the attribution step is where guilt is decided.",
        "Guilt points at what was done, not at who the person is - that is what separates it from shame.",
        "The feeling itself is information; what matters is whether it leads to honest repair.",
    ],
    requirements=[
        "Everyday definition a student or writer can quote",
        "Clear statement that guilt needs a standard and self-judgment",
        "The four-beat sequence stated in plain words",
        "No diagnostic language anywhere in the record",
    ],
    standards=["APA Dictionary of Psychology definition of guilt as a self-conscious emotion"],
    citations=[CIT_APA, CIT_TANGNEY],
    sig_lens=(
        "The Signature lens reads guilt as the soul's ledger: an honest "
        "bookkeeping in which every entry is something you did against "
        "your own code. Where public psychology calls it attribution, the "
        "Signature method calls it the ledger check - the built-in audit "
        "that runs when a standard is breached. The three-beat ledger "
        "cycle is signal, repair, and release: the signal names the "
        "debt, the repair pays it, and the release keeps the lesson "
        "without carrying the weight. A ledger that is never read rots "
        "into denial; a ledger that is never closed rots into carrying. "
        "Clearly labeled Signature-made, never presented as authentic "
        "public record."),
),
dict(
    key="guilt_emotion_family", name="Guilt in the Emotion Family: Basic Roots and Complex Branches",
    group="Foundations", ladder_rank=2, ladder_tier="foundations",
    description=(
        "Guilt does not sit with the basic emotions like anger, fear, "
        "joy, sadness, disgust, and surprise. It belongs to a second "
        "family: the self-conscious emotions, alongside shame, "
        "embarrassment, and pride. What makes this family different is "
        "that every member needs a self that can be evaluated - the "
        "feeling only switches on when a person measures themselves "
        "against a standard. From the guilt root, branches grow into "
        "more specific forms. Remorse is guilt deepened by the weight "
        "of a serious wrong. Regret is guilt's close cousin aimed at "
        "outcomes and missed choices rather than moral breach. "
        "Survivor guilt is guilt that appears when a person is spared "
        "while others suffer, even without any wrongdoing. Anticipatory "
        "guilt is the feeling arriving in advance, warning before a "
        "standard is broken - which is why it works as a deterrent. "
        "Collective guilt is guilt felt on behalf of a group one "
        "belongs to, for wrongs the group committed. Each branch keeps "
        "guilt's core - a perceived breach of a standard - and adds a "
        "time direction, a group, or a target. Knowing the family tree "
        "matters because each branch asks for something different: "
        "remorse wants amends, anticipatory guilt wants a better choice "
        "now, and survivor guilt wants the attribution examined, since "
        "there may be no real wrong to repair."),
    how_it_works=(
        "Emotion researchers sort guilt among the moral emotions - the "
        "set of feelings that bind people to their groups by rewarding "
        "and punishing social behavior. The moral-emotion view explains "
        "why guilt is so sensitive to relationships: its intensity "
        "tracks closeness, so a broken promise to a loved one stings "
        "far more than the same act toward a stranger. The family view "
        "also explains guilt's special partner: because guilt judges "
        "an action and shame judges the self, the two arrive together "
        "constantly - nearly every serious guilt episode drags some "
        "shame along with it. Developmental research shows the "
        "self-conscious family comes online later than the basic "
        "emotions, as children internalize standards and learn to "
        "evaluate themselves. The root stays the same across all the "
        "branches; the branch names tell you which message the guilt "
        "is carrying and what kind of response will settle it."),
    key_points=[
        "Guilt is a self-conscious, moral emotion - not one of the basic emotions.",
        "Complex branches include remorse, regret, survivor guilt, anticipatory guilt, and collective guilt.",
        "Guilt intensity tracks relationship closeness: the nearer the person harmed, the stronger the signal.",
        "Guilt almost always arrives with shame nearby, since both involve self-evaluation.",
        "Naming the exact branch matters because each one asks for a different response.",
    ],
    requirements=[
        "State guilt's place among self-conscious and moral emotions",
        "List at least five complex branches with their distinguishing marks",
        "Explain why guilt tracks closeness",
    ],
    standards=["Tangney and Dearing self-conscious emotion framework; Haidt moral emotions model"],
    citations=[CIT_TANGNEY, CIT_HAIDT, CIT_LEWIS],
    sig_lens=(
        "The Signature lens reads the guilt family as the ledger's "
        "branch offices: each branch keeps the same honest bookkeeping "
        "but audits a different kind of account. Remorse audits the "
        "heavy debts, regret audits the roads not taken, survivor "
        "guilt audits accounts where no debt was ever owed, "
        "anticipatory guilt is the ledger warning before an entry is "
        "written, and collective guilt is the shared ledger of a "
        "group. The Signature method treats the family tree as a map "
        "of accounts: name the right account, and the repair goes to "
        "the right place. Clearly labeled Signature-made, never "
        "presented as authentic public record."),
),
dict(
    key="guilt_intensity_scale", name="Guilt at Three Volumes: Mild, Moderate, and Intense",
    group="Foundations", ladder_rank=2, ladder_tier="foundations",
    description=(
        "The same guilt can arrive at very different volumes, and the "
        "volume changes almost everything about it. Mild guilt is the "
        "faint tug - the small sting of forgetting to reply to a "
        "message, the passing thought that a comment landed badly. It "
        "lasts minutes, nudges a quick fix, and clears on its own. "
        "Moderate guilt is the steady ache - knowing you let someone "
        "down in a way that mattered, replaying the moment through "
        "the evening. It calls for real repair: an apology, a change "
        "of plan, a concrete make-up. Intense guilt is the full "
        "weight - the feeling that follows causing real harm, betraying "
        "a trust, or acting against a deeply held value. It can fill "
        "days, color sleep and appetite, and demand sustained repair. "
        "The three volumes share one mechanism - a perceived breach "
        "plus self-attribution - but they differ in what dials are "
        "turned up: how much harm was done, how close the person "
        "harmed is, how clear the responsibility is, and how central "
        "the broken standard is to the person's identity. Learning to "
        "read the volume is a practical skill: mild guilt wants a "
        "small, quick repair; intense guilt wants patient, proportionate "
        "work - and mistaking one for the other is how small mistakes "
        "get dramatized and serious ones get dismissed."),
    how_it_works=(
        "Three dials set the volume knob of guilt. The first dial is "
        "perceived harm: how much damage the action seems to have done. "
        "The second is closeness: how much the harmed person matters "
        "to the one feeling guilt. The third is responsibility clarity: "
        "how completely the person believes the breach was their doing. "
        "Turn all three up and the result is intense; turn them down "
        "and the same structure produces only a tug. A fourth, quieter "
        "dial is standard centrality - how deeply the broken rule is "
        "woven into the person's identity. This is why two people can "
        "commit the same act and feel completely different volumes: "
        "their dials are set differently by upbringing, culture, and "
        "experience. The volume model also explains why guilt can feel "
        "disproportionate: when responsibility clarity is cranked to "
        "maximum while actual harm was small, mild events produce "
        "intense feelings - and the work is in recalibrating the dials "
        "honestly, not in pretending the signal is meaningless."),
    key_points=[
        "Mild, moderate, and intense guilt share one mechanism but differ in dial settings.",
        "The three dials are perceived harm, closeness to the harmed person, and responsibility clarity.",
        "Standard centrality is the quiet fourth dial: identity-level rules produce heavier guilt.",
        "Reading the volume correctly is practical: small repairs for tugs, sustained work for weights.",
        "Disproportionate guilt usually means one dial is cranked too high for the actual event.",
    ],
    requirements=[
        "Describe all three volumes with concrete examples",
        "Name the dials that set the volume",
        "Explain disproportionate guilt through the dial model",
    ],
    standards=["Appraisal-theory account of guilt intensity (Lazarus; Scherer)"],
    citations=[CIT_LAZARUS, CIT_SCHERER, CIT_BAUMEISTER],
    sig_lens=(
        "The Signature lens reads the three volumes as three sizes of "
        "ledger debt: a small entry, a standing balance, and a debt "
        "that shadows the whole account. The Signature method treats "
        "the volume knob as the ledger's honesty meter - mild debts "
        "are paid with quick entries, heavy debts need sustained "
        "repayment plans. His rule: never pay a small debt with a "
        "large punishment, and never pay a large debt with a shrug. "
        "The ledger balances only when the payment matches the debt. "
        "Clearly labeled Signature-made, never presented as authentic "
        "public record."),
),
dict(
    key="guilt_myths", name="Myths and Misunderstandings About Guilt",
    group="Foundations", ladder_rank=3, ladder_tier="foundations",
    description=(
        "Several stubborn myths surround guilt, and they make the "
        "feeling harder to handle than it needs to be. Myth one: guilt "
        "means you did something wrong. In fact, guilt means you believe "
        "you did something wrong - and beliefs can be mistaken. "
        "Survivor guilt, misplaced childhood guilt, and guilt over "
        "things outside anyone's control all prove the signal can fire "
        "on a false alarm. Myth two: guilt and shame are the same "
        "thing. They are close cousins but different judgments: guilt "
        "says 'I did a bad thing,' shame says 'I am a bad person,' and "
        "the difference decides whether the response is repair or "
        "hiding. Myth three: feeling guilty proves you are a good "
        "person. Guilt correlates with caring about standards, but the "
        "feeling alone repairs nothing - only the repair does. Myth "
        "four: the way to handle guilt is to stop feeling it. "
        "Suppressing the signal usually just reroutes it into rumination "
        "or irritability. Myth five: apologizing always clears guilt. "
        "A rushed or hollow apology can leave the ledger still open, "
        "and some guilt only settles after sustained changed behavior. "
        "Myth six: guilt is useless suffering. Research on guilt's "
        "interpersonal function shows it is one of the main forces "
        "that keeps relationships repaired - the myth confuses the "
        "pain of the signal with a lack of purpose."),
    how_it_works=(
        "Myths about guilt persist because the feeling is private and "
        "people rarely compare notes about it. Each myth works by "
        "freezing one part of the guilt sequence into a false rule. "
        "'Guilt means you did wrong' freezes the attribution step as "
        "infallible, when attribution is exactly the step most open "
        "to error - memory is partial, responsibility is shared, and "
        "hindsight inflates how obvious the right choice seemed. "
        "'Guilt equals shame' freezes the judgment target, hiding the "
        "action-versus-self distinction that decides whether repair or "
        "concealment follows. 'Feeling it proves goodness' freezes the "
        "sequence at the feeling and skips the repair beat entirely, "
        "which is how guilt becomes a performance instead of a "
        "practice. Clearing each myth restores the full sequence: "
        "check the attribution honestly, name the exact breach, aim "
        "the response at repair, and let the feeling finish its job "
        "so it can fade."),
    key_points=[
        "Guilt signals a believed breach, not a proven one - the attribution step can be wrong.",
        "Guilt judges an action; shame judges the self; the difference decides repair versus hiding.",
        "Feeling guilty repairs nothing by itself - only repair repairs.",
        "Suppressing guilt reroutes it; hollow apologies leave the account open.",
        "Guilt is a relationship-repair mechanism, not useless suffering.",
    ],
    requirements=[
        "Debunk at least six common myths with corrections",
        "Explain the action-versus-self distinction as the key correction",
        "Show how each myth freezes one step of the guilt sequence",
    ],
    standards=["Tangney and Dearing guilt-versus-shame distinction; Baumeister interpersonal function of guilt"],
    citations=[CIT_TANGNEY, CIT_BAUMEISTER, CIT_LEWIS],
    sig_lens=(
        "The Signature lens reads each myth as a smudge on the ledger: "
        "a false entry, a mislabeled account, a payment recorded that "
        "was never made. The Signature method treats myth-clearing as "
        "ledger hygiene - wipe the smudge and the true balance shows. "
        "His correction for the loudest myth: the ledger records what "
        "you believe you owe, and belief must be audited like any other "
        "entry. Clearly labeled Signature-made, never presented as "
        "authentic public record."),
),
# ------------------------------------------------- 5-9: how it feels
dict(
    key="guilt_first_person", name="Inside the Feeling: A First-Person Passage of Guilt",
    group="Foundations", ladder_rank=3, ladder_tier="foundations",
    description=(
        "It starts as a sinking recognition, not a blow. You replay the "
        "moment - the words you said, the thing you did not do - and a "
        "heaviness settles behind the breastbone, like something pulling "
        "downward from the inside. Your stomach feels hollow and slightly "
        "sick at once. Thoughts loop: you see the other person's face at "
        "the exact instant, you hear your own voice saying it again, you "
        "try out the version where you acted differently and it plays "
        "too cleanly, which somehow makes it worse. There is a restless "
        "urge to fix it right now - to call, to text, to explain - mixed "
        "with a dread of the conversation, so you pace between the two. "
        "Your eyes drop without being told to; meeting anyone's gaze "
        "feels like being seen through. Time does something strange: "
        "the guilty moment feels both very recent and very far away, "
        "like it happened to a slightly different version of you, except "
        "the feeling in your chest insists it was you. Underneath it all "
        "is a single sentence on repeat, in your own voice: I should "
        "have known better. That sentence is the whole feeling in "
        "compressed form - the standard, the breach, and the "
        "self-attribution in one line."),
    how_it_works=(
        "The first-person texture of guilt comes from where attention "
        "goes: inward and backward. Unlike anger, which aims attention "
        "outward at the offender, guilt aims it at the self and at the "
        "past - at the moment of the breach and the standard it broke. "
        "The looping replay is the mind re-running the attribution "
        "step, testing whether the responsibility really belongs to the "
        "self; each replay that confirms it deepens the feeling. The "
        "bodily heaviness and stomach unease are the somatic markers "
        "the brain attaches to self-blame, and the gaze aversion is the "
        "social half of the feeling: the breached standard was a "
        "relational one, so the eyes avoid the imagined witness. The "
        "restless fix-it urge is the repair beat of the sequence already "
        "pushing for expression. Reading this passage as a simulation - "
        "as what the feeling is like from the inside - is the point of "
        "the record: recognition without diagnosis, description without "
        "prescription."),
    key_points=[
        "Guilt aims attention inward and backward: at the self and at the moment of the breach.",
        "The looping replay is the mind re-testing the attribution of responsibility.",
        "Heaviness, stomach unease, and gaze aversion are the feeling's signature texture.",
        "The restless fix-it urge is the repair beat already pushing for expression.",
        "This is simulation for recognition and education, never a diagnosis of any real person.",
    ],
    requirements=[
        "A vivid first-person passage of at least 200 words",
        "Cover bodily sensation, thought loops, and the repair urge",
        "State plainly that this is simulation, not diagnosis",
    ],
    standards=["Phenomenological description consistent with Tangney and Dearing; Lazarus appraisal account"],
    citations=[CIT_TANGNEY, CIT_LAZARUS],
    sig_lens=(
        "The Signature lens reads the inner passage as the ledger page "
        "turning itself: the self reading its own entries in its own "
        "handwriting. The Signature method calls the looping replay "
        "the audit loop - the conscience re-checking the entry until "
        "the balance is confirmed or corrected. His note on the heavy "
        "sentence: 'I should have known better' is the ledger speaking "
        "in first person, which is why arguing with it never works - "
        "only a new entry, a repair, changes the page. Clearly labeled "
        "Signature-made, never presented as authentic public record."),
),
dict(
    key="guilt_time_course", name="The Time Course of Guilt: Onset, Peak, Fading, and Aftershock",
    group="Foundations", ladder_rank=4, ladder_tier="foundations",
    description=(
        "Guilt has a characteristic time signature, and it is slower "
        "than most emotions. Onset is rarely instant: there is usually "
        "a delay between the act and the feeling, because the "
        "attribution step needs time - the person must register what "
        "happened, connect it to a standard, and accept a share of "
        "responsibility. Sometimes the delay is minutes; sometimes the "
        "guilt arrives hours later, in the quiet after the event, or "
        "even days later when new information reveals the harm. The "
        "peak is the rumination phase: the replay loop at full speed, "
        "the heaviest bodily feeling, the strongest repair urge. For "
        "mild guilt the peak passes in an hour; for serious breaches "
        "it can hold for days. Fading begins when repair starts - the "
        "apology made, the amends begun, the behavior changed - or "
        "when the attribution is honestly revised. But guilt is famous "
        "for its aftershock: the feeling can go quiet and then flare "
        "again weeks or months later, triggered by an anniversary, a "
        "similar situation, or an idle moment. The aftershock is not a "
        "failure of the first fading; it is the ledger re-opening an "
        "account that was never fully closed. Knowing the time course "
        "matters practically: it explains why guilt feels worse at "
        "night, why it ambushes people long after they thought it was "
        "done, and why quick fixes often fail - the sequence runs on "
        "its own slower clock."),
    how_it_works=(
        "The slow onset reflects the cognitive work guilt requires: "
        "unlike fear, which can fire on a crude threat cue, guilt needs "
        "a completed appraisal of standard, breach, and responsibility. "
        "The peak's rumination is the attribution step cycling - each "
        "pass through the replay either strengthens or weakens the "
        "self-blame, which is why the peak feels like being stuck. "
        "Fading is tied to resolution of the sequence: the repair beat "
        "executed, or the attribution honestly corrected, lets the "
        "system stand down. The aftershock works through associative "
        "memory: the breach is stored with its context, and any "
        "contextual cue - a place, a date, a similar choice - can "
        "re-activate the appraisal. This is also why suppression "
        "backfires: pushing the feeling away skips the repair beat, "
        "leaving the account open for the next cue to re-open. The "
        "time course is descriptive, not prescriptive - it maps what "
        "the feeling tends to do, not what anyone should do about it."),
    key_points=[
        "Guilt onset is delayed: the attribution step needs time to complete.",
        "The peak is the rumination phase, where the replay loop runs at full speed.",
        "Fading begins with repair or honest attribution revision - not with suppression.",
        "Aftershocks are normal: contextual cues can re-open an account that was never fully closed.",
        "Suppression skips the repair beat and sets up the next aftershock.",
    ],
    requirements=[
        "Describe all four phases with typical durations",
        "Explain the delayed onset through the appraisal steps",
        "Explain aftershocks through associative memory",
    ],
    standards=["Appraisal-theory time course (Scherer); rumination literature consistent with Gross"],
    citations=[CIT_SCHERER, CIT_GROSS, CIT_TANGNEY],
    sig_lens=(
        "The Signature lens reads the time course as the ledger's "
        "settlement schedule: entries post late, balances peak while "
        "under audit, accounts close when paid, and old accounts "
        "re-open when a matching entry appears. The Signature method "
        "treats the aftershock as proof of an unpaid balance, not as "
        "a malfunction - the ledger is doing its job by remembering. "
        "His rule: a closed account stays closed; a quiet account is "
        "not a closed one. Clearly labeled Signature-made, never "
        "presented as authentic public record."),
),
dict(
    key="guilt_low_vs_high", name="Guilt at Low Intensity and at High Intensity: Two Lived Snapshots",
    group="Foundations", ladder_rank=4, ladder_tier="foundations",
    description=(
        "Low-intensity guilt, lived: You are halfway through the "
        "morning when you remember the birthday message you meant to "
        "send yesterday. A small wince, a warm flicker behind the "
        "eyes, a quick mental note - send it now, with a line "
        "acknowledging the lateness. The feeling is gone before "
        "lunch, replaced by the small satisfaction of the repair. "
        "Your body barely registers it: a momentary tightness, a "
        "half-second of looking down, then the day continues. The "
        "whole episode is a tug and a fix, and by evening you would "
        "struggle to recall it without prompting. "
        "High-intensity guilt, lived: It is 2 a.m. and you are awake "
        "replaying the argument - the exact sentence, the look on "
        "their face, the silence after. Your chest feels compressed, "
        "your stomach turns, and every position in bed is wrong. You "
        "have drafted the apology four times and deleted it four "
        "times, because every version sounds either too small or "
        "too self-serving. The day ahead looks gray at the edges; "
        "food has no appeal; concentration keeps sliding back to "
        "the same scene. What you want, more than anything, is to "
        "undo the hour - and since you cannot, the wanting itself "
        "becomes the feeling's second layer. The two snapshots are "
        "the same emotion at different volumes: the same sinking "
        "recognition, the same repair urge, the same looping replay "
        "- but at high intensity every element is larger, longer, "
        "and harder to set down."),
    how_it_works=(
        "The two snapshots differ along the same dials that set the "
        "volume: perceived harm, closeness, responsibility clarity, "
        "and standard centrality. In the low-intensity snapshot, all "
        "four dials sit low - small harm, ordinary closeness, clear "
        "but minor responsibility, a light standard. The repair beat "
        "executes quickly and the sequence closes. In the "
        "high-intensity snapshot, the dials are near maximum - real "
        "harm to someone close, undeniable responsibility, a core "
        "value breached. The repair beat cannot execute quickly "
        "because no quick repair matches the scale, so the sequence "
        "stalls at the peak and the rumination phase stretches. The "
        "sleep and appetite effects at high intensity are the body's "
        "stress systems staying engaged while the appraisal stays "
        "unresolved. The practical lesson of the pair: match the "
        "response to the volume - quick repairs for tugs, sustained "
        "proportionate work for weights - and expect the high-volume "
        "version to run on the slower clock described in the time "
        "course record."),
    key_points=[
        "Low and high intensity guilt are the same mechanism at different dial settings.",
        "Low intensity: a tug and a quick fix, gone by lunch.",
        "High intensity: sustained rumination, bodily effects, and a repair that cannot be rushed.",
        "The volume dials are harm, closeness, responsibility clarity, and standard centrality.",
        "Match the response to the volume; expect high-intensity guilt to run on a slow clock.",
    ],
    requirements=[
        "Two vivid lived snapshots, low and high intensity",
        "Tie the difference explicitly to the volume dials",
        "Practical takeaway on matching response to volume",
    ],
    standards=["Appraisal-theory intensity model; descriptive phenomenology"],
    citations=[CIT_LAZARUS, CIT_SCHERER],
    sig_lens=(
        "The Signature lens reads the two snapshots as a small ledger "
        "entry versus a debt that shadows the account: one closes "
        "with a single payment, the other needs a repayment plan. "
        "The Signature method warns against the two classic errors - "
        "paying the small debt with a large punishment, and paying "
        "the large debt with a shrug. His measure of the account: "
        "the right payment is the one that matches the true balance, "
        "audited honestly. Clearly labeled Signature-made, never "
        "presented as authentic public record."),
),
dict(
    key="guilt_shame_blend", name="Guilt Mixed With Its Most Common Partner: Shame",
    group="Foundations", ladder_rank=5, ladder_tier="foundations",
    description=(
        "Guilt's most common partner is shame, and the two arrive "
        "together so reliably that most people use one word for both. "
        "The blend feels like this: the guilt half says 'I did a bad "
        "thing' and pushes toward repair - apologize, fix, make it "
        "right. The shame half says 'I am a bad person' and pushes "
        "toward hiding - avoid the person, change the subject, wish "
        "the whole thing would disappear. The two urges fight in real "
        "time: you pick up the phone to apologize and set it back "
        "down, you start the sentence and swallow it. The body shows "
        "both at once: the heaviness and stomach-knot of guilt with "
        "the shrinking, gaze-averting, face-covering impulses of "
        "shame. The blend is more painful than either feeling alone, "
        "because the repair urge and the hiding urge cancel each "
        "other - nothing gets fixed and nothing gets faced. "
        "Untangling them is the practical skill: ask which sentence "
        "is louder. If 'I did a bad thing' dominates, the path is "
        "repair - name the act, make amends, change the behavior. If "
        "'I am a bad person' dominates, the path is different: the "
        "judgment has slid from the act to the self, and repair of "
        "the act gets blocked until the self-judgment is examined. "
        "Most real episodes are a mix with one half louder, and the "
        "work is in hearing which is which."),
    how_it_works=(
        "The guilt-shame blend forms because both feelings share the "
        "self-evaluation machinery: the same breached standard and the "
        "same witnessed self produce two different verdicts. Research "
        "distinguishes them by attribution target - behavior versus "
        "global self - and by action tendency: guilt motivates repair "
        "and confession, shame motivates withdrawal and concealment. "
        "When both fire, the action tendencies conflict, which is why "
        "the blend feels like paralysis. The blend also explains a "
        "common trap: shame's hiding urge can block guilt's repair "
        "urge, so the breach never gets addressed, which generates "
        "more guilt, which drags in more shame - a loop. Breaking the "
        "loop means separating the verdicts: keep the action-level "
        "judgment (which is accurate and useful) and set the "
        "global-self verdict aside for examination (which is usually "
        "overbroad). The blend record is descriptive: it maps what "
        "the mixture feels like and why it behaves the way it does."),
    key_points=[
        "Shame is guilt's most constant partner; the two share self-evaluation machinery.",
        "Guilt says 'I did a bad thing' and pushes toward repair; shame says 'I am a bad person' and pushes toward hiding.",
        "The blend feels like paralysis because the two action urges cancel each other.",
        "Shame's hiding can block guilt's repair, creating a self-feeding loop.",
        "Untangling means asking which sentence is louder and aiming the response at the act, not the self.",
    ],
    requirements=[
        "Describe the blend from the inside with both urges present",
        "State the behavior-versus-self distinction clearly",
        "Explain the loop where hiding blocks repair",
    ],
    standards=["Tangney and Dearing guilt/shame distinction; Lewis self-conscious emotion theory"],
    citations=[CIT_TANGNEY, CIT_LEWIS, CIT_TRACY],
    sig_lens=(
        "The Signature lens reads the guilt-shame blend as two ledger "
        "entries written in the same ink: one records a debt, the "
        "other condemns the accountant. The Signature method insists "
        "the two be separated on the page - the debt is real and can "
        "be paid; the condemnation of the accountant pays nothing and "
        "blocks every payment. His rule: audit the entry, never the "
        "auditor. Clearly labeled Signature-made, never presented as "
        "authentic public record."),
),
dict(
    key="guilt_day_vignette", name="A Day With Guilt: A Day-in-the-Life Vignette",
    group="Foundations", ladder_rank=5, ladder_tier="foundations",
    description=(
        "Morning: You wake already mid-thought about yesterday's "
        "missed call from your father - you saw it, meant to call "
        "back, and did not. The guilt is waiting like weather. You "
        "tell yourself you will call at lunch, and the promise "
        "lightens it by half. Midday: lunch comes and goes in a "
        "rush of errands; the call does not happen. The guilt "
        "returns heavier, now with a second layer - guilt about the "
        "broken promise to yourself. You rehearse the call while "
        "driving, and the rehearsal makes it feel both easier and "
        "more overdue. Afternoon: a coworker mentions their own "
        "father, and the comment lands like a cue - the replay loop "
        "starts, the missed call joining a small archive of similar "
        "misses, each one making the others feel larger. Evening: "
        "you finally call. He is glad to hear from you; the "
        "conversation is ordinary and warm. The guilt drains out in "
        "minutes, and what replaces it is almost embarrassing in its "
        "simplicity - relief, and the clear knowledge that the "
        "dread was always larger than the deed. Night: lying in "
        "bed, a faint aftershock - a thought of how many such small "
        "debts are still open. You make a note to call Sunday. The "
        "day shows guilt's whole shape in miniature: the morning "
        "signal, the midday compounding, the afternoon cascade, the "
        "evening repair, the night aftershock - and the standing "
        "lesson that the feeling is almost always heavier before "
        "the repair than after it."),
    how_it_works=(
        "The vignette compresses the full guilt sequence into a "
        "single ordinary day. The morning signal is the attribution "
        "completing overnight; the midday compounding shows how a "
        "missed repair adds a second entry to the ledger; the "
        "afternoon cascade shows associative memory pulling related "
        "breaches into the appraisal; the evening repair shows the "
        "sequence closing when the repair beat executes; the night "
        "aftershock shows the account re-opening on a cue. Each "
        "phase maps to a record in this database - the time course, "
        "the chain reactions, the body signals, the healthy "
        "expression. The vignette's practical point is the "
        "dread-versus-deed gap: anticipatory dread of the repair "
        "conversation consistently exceeds the actual cost of having "
        "it, which is why the repair urge deserves trust even when "
        "it feels daunting. The day is a simulation for teaching, "
        "not a description of any real person."),
    key_points=[
        "One ordinary day can show guilt's whole shape: signal, compounding, cascade, repair, aftershock.",
        "Missed repairs add second-layer guilt about the broken promise to oneself.",
        "Associative memory pulls related breaches into the current appraisal.",
        "The dread of the repair conversation consistently exceeds its actual cost.",
        "The vignette is a teaching simulation, not a description of any real person.",
    ],
    requirements=[
        "A full day arc in at least five time-stamped beats",
        "Show compounding and the dread-versus-deed gap",
        "Map each beat to the database's concepts",
    ],
    standards=["Descriptive narrative consistent with appraisal and rumination literature"],
    citations=[CIT_LAZARUS, CIT_BAUMEISTER],
    sig_lens=(
        "The Signature lens reads the day as a single ledger page "
        "turned in daylight: morning entry, midday interest, "
        "afternoon audit, evening payment, night review. The "
        "Signature method draws one standing lesson from the "
        "vignette: the dread of payment is always larger than the "
        "payment, which is why the ledger rewards prompt settlers. "
        "His shorthand: pay early, pay honestly, sleep well. "
        "Clearly labeled Signature-made, never presented as "
        "authentic public record."),
),
# ------------------------------------------------- 10-13: body signals
dict(
    key="guilt_body_signals", name="The Body in Guilt: Heart, Breath, Muscles, Stomach, Skin, and Energy",
    group="Compounded", ladder_rank=5, ladder_tier="compounded",
    description=(
        "Guilt lives in the body as heaviness and inward pull rather "
        "than heat and outward push. The heart may beat a little "
        "faster during the acute recognition, but the signature "
        "sensation is a weight behind the breastbone - a compressed, "
        "sinking feeling that people describe as heaviness, pressure, "
        "or a knot. Breathing tends to shallow: short, quiet breaths, "
        "sometimes with a long sigh that seems to come from nowhere - "
        "the sigh is the body's small attempt at release. Muscles do "
        "not brace for action as in anger; they slacken and fold: "
        "shoulders round forward, the head dips, the whole frame seems "
        "to get slightly smaller. The stomach is guilt's loudest "
        "organ: nausea, hollowness, churning, loss of appetite - the "
        "gut responds to self-blame with unusual reliability. Skin "
        "effects are mild but real: a warm flush across the face and "
        "neck when the guilt is witnessed or confessed, sometimes a "
        "cold clamminess in the hands during dread of the repair. "
        "Energy drops: guilt is tiring, not mobilizing. Unlike fear's "
        "adrenaline surge or anger's heat, guilt drains - the person "
        "feels leaden, slow, reluctant to start things. Researchers "
        "note that guilt lacks the sharp, distinctive autonomic "
        "signature of the basic emotions; its body pattern is quieter "
        "and more postural, which is one reason other people often "
        "miss it until the person speaks."),
    how_it_works=(
        "The body pattern of guilt follows from its appraisal "
        "structure. Because guilt judges the self rather than an "
        "external threat, it does not trigger the fight-or-flight "
        "mobilization of fear or anger - there is nothing to flee "
        "from or strike at, since the accused and the accuser are "
        "the same person. The inward-folding posture reflects the "
        "social half of the emotion: a breached relational standard "
        "activates appeasement and submission displays, the body's "
        "ancient way of signaling 'I mean no further harm.' The "
        "stomach's strong response is consistent with the gut's role "
        "in disgust and self-evaluation - the body treats a moral "
        "breach a little like something ingested that should not have "
        "been. The energy drain comes from rumination's cognitive "
        "cost: the replay loop consumes attention and working memory, "
        "leaving less for everything else. The sighing and shallow "
        "breathing are the respiratory system's response to a "
        "sustained, low-arousal negative state. None of this is "
        "diagnostic of anything in any real person - it is the "
        "described pattern of the feeling, for education and "
        "recognition."),
    key_points=[
        "Guilt's body pattern is heaviness and inward pull, not heat and outward push.",
        "Signature sensations: breastbone weight, shallow breathing, sighing, stomach churn or hollowness.",
        "Posture folds inward - shoulders round, head dips - an appeasement display.",
        "Guilt drains energy rather than mobilizing it; rumination consumes attention.",
        "Guilt lacks the sharp autonomic signature of basic emotions; its pattern is quieter and postural.",
    ],
    requirements=[
        "Cover heart, breath, muscles, stomach, skin, and energy",
        "Contrast with fear/anger mobilization",
        "State the pattern is descriptive, not diagnostic",
    ],
    standards=["Psychophysiology of self-conscious emotions (Tracy and Robins); Damasio somatic marker account"],
    citations=[CIT_TRACY, CIT_DAMASIO, CIT_TANGNEY],
    sig_lens=(
        "The Signature lens reads the guilty body as the ledger made "
        "flesh: the breastbone weight is the debt felt as mass, the "
        "folded posture is the accountant bowing over the books, the "
        "sigh is the page turning. The Signature method treats body "
        "signals as the ledger's early-warning system - they arrive "
        "before the mind finishes the audit, which is why the stomach "
        "often knows before the thoughts do. His practice: read the "
        "body's entry first, then check it against the facts. Clearly "
        "labeled Signature-made, never presented as authentic public "
        "record."),
),
dict(
    key="guilt_posture_movement", name="Posture and Movement: How Guilt Carries the Body",
    group="Compounded", ladder_rank=6, ladder_tier="compounded",
    description=(
        "Guilt has one of the most readable postures in the emotion "
        "family, because the body tries to get smaller. The head "
        "tilts down and slightly away; the chin tucks; the gaze drops "
        "to the floor or fixes on something neutral at middle "
        "distance. The shoulders round forward and inward, narrowing "
        "the chest. The arms tend to cross, fold, or find something "
        "to hold - a cup, a sleeve, the edge of a table - as if the "
        "hands need an assignment to avoid fidgeting. The torso may "
        "lean very slightly away from the person associated with the "
        "breach. Movement under guilt is hesitant and reduced: "
        "slower walking, smaller gestures, a reluctance to take up "
        "space - the opposite of anger's expansive stride. There is "
        "often a stillness, too: the guilty person goes quiet and "
        "motionless when the replay loop takes over, freezing "
        "mid-gesture as attention turns fully inward. In "
        "confrontation or confession, the body may show a rocking or "
        "swaying micro-motion, and the hands may rise briefly to the "
        "face - covering the mouth, rubbing the forehead - before "
        "dropping again. Actors and artists take note: guilt is played "
        "from the spine and the eyes first, the mouth last. The "
        "whole posture says 'I wish to be less visible,' which is "
        "exactly what the feeling is doing socially - reducing the "
        "self's claim on the group's attention after a breach."),
    how_it_works=(
        "The shrinking posture of guilt is an appeasement display with "
        "deep roots: across social species, a subordinate or "
        "offending individual reduces its apparent size to signal no "
        "further threat after a conflict. In humans this ancient "
        "program runs through the same self-evaluation that produces "
        "the feeling - the judged self physically withdraws. Gaze "
        "aversion serves double duty: it avoids the imagined judgment "
        "in the other person's eyes, and it reduces the social "
        "information coming in while the mind is occupied with the "
        "replay loop. The hesitation in movement reflects the "
        "conflict between the repair urge (approach) and the "
        "shame-adjacent hiding urge (withdrawal) - the body stalls "
        "between the two. The hand-to-face gestures are self-soothing "
        "behaviors, brief tactile comfort during distress. The "
        "freezing during replay loops is attention capture: the "
        "internal simulation is so demanding that the motor system "
        "idles. All of this is described as the typical pattern for "
        "education - individual bodies vary, and no posture proves "
        "anything about any real person."),
    key_points=[
        "Guilt's posture is shrinking: head down, shoulders rounded, gaze averted, body narrowed.",
        "Movement becomes hesitant, smaller, and slower - the opposite of anger's expansion.",
        "Gaze aversion avoids imagined judgment and reduces incoming social information.",
        "Hand-to-face gestures and micro-swaying are self-soothing during distress.",
        "The pattern is an appeasement display: signaling no further harm after a breach.",
    ],
    requirements=[
        "Describe head, gaze, shoulders, arms, torso, and gait",
        "Cover stillness/freezing and self-soothing gestures",
        "Explain the appeasement-display function",
    ],
    standards=["Ethological appeasement-display literature; Keltner and Buswell appeasement functions"],
    citations=[CIT_KELTNER, CIT_TRACY, CIT_EKMAN],
    sig_lens=(
        "The Signature lens reads the guilty posture as the ledger's "
        "physical handwriting: the bowed head is the accountant bent "
        "over the books, the averted gaze is the refusal to meet the "
        "creditor's eyes, the narrowed frame is the self making room "
        "for the debt. The Signature method treats posture as the "
        "fastest-read page of the ledger - before a word is spoken, "
        "the body has filed its report. His note for the repair: the "
        "posture straightens not with pride but with payment - "
        "standing tall again is the body's receipt for work done. "
        "Clearly labeled Signature-made, never presented as authentic "
        "public record."),
),
dict(
    key="guilt_sleep_appetite_energy", name="Sleep, Appetite, and Energy Under Guilt",
    group="Compounded", ladder_rank=6, ladder_tier="compounded",
    description=(
        "Guilt reaches into the body's maintenance systems, most "
        "noticeably at night. Sleep is where guilt does its loudest "
        "work: the replay loop that was manageable during the day's "
        "distractions runs unchecked in the dark, and many people "
        "report that guilt feels two to three times heavier at 2 a.m. "
        "than at 2 p.m. Falling asleep gets harder because the mind "
        "will not release the scene; staying asleep gets lighter "
        "because the stress system stays half-engaged. Appetite "
        "usually drops: the stomach's unease translates directly into "
        "skipped meals, picked-at plates, and food that tastes like "
        "nothing. A smaller number of people eat more instead - quick "
        "comfort food as self-soothing - but the dominant pattern is "
        "loss of interest in eating. Energy follows the same downward "
        "slope: guilt is cognitively expensive, and the bill comes "
        "due as fatigue, heaviness in the limbs, and a reluctance to "
        "begin tasks. Concentration frays because working memory is "
        "occupied by the loop. The practical shape of all this: guilt "
        "creates the exact conditions - tired, hungry or overfull, "
        "underslept - that make the next day's judgments worse and "
        "the next breach more likely. Breaking the cycle at the "
        "maintenance level - regular sleep, real meals, movement - is "
        "not a cure for guilt, but it restores the resources the "
        "repair work needs."),
    how_it_works=(
        "The sleep disruption follows from rumination's timing: "
        "without daytime tasks competing for attention, the replay "
        "loop dominates, and the bed becomes associated with the "
        "looping. The appetite loss follows from the gut-brain "
        "connection in self-evaluative distress - nausea and "
        "hollowness suppress hunger signals directly. The energy "
        "drain is the cost of sustained cognitive control: each "
        "cycle of replay, suppression, and re-appraisal draws on "
        "the same limited attentional resources that daytime "
        "functioning needs. This creates a feedback loop well "
        "described in emotion-regulation research: depleted "
        "resources weaken regulation, weakened regulation lets the "
        "loop run longer, the longer loop depletes further. The "
        "record's practical point is structural, not medical: the "
        "maintenance systems are where the feeling's costs "
        "compound, so they are also where small stabilizing habits "
        "pay the largest dividends. Nothing here is medical advice "
        "for any real person - it is a description of the pattern "
        "for education."),
    key_points=[
        "Guilt hits hardest at night: the replay loop runs unchecked without daytime distraction.",
        "Appetite usually drops via stomach unease; a minority self-soothes with comfort food.",
        "Energy drains because rumination is cognitively expensive.",
        "Poor sleep, poor fuel, and depleted attention create a compounding feedback loop.",
        "Stabilizing sleep, meals, and movement restores the resources repair work needs.",
    ],
    requirements=[
        "Cover sleep onset, sleep quality, appetite, and energy/concentration",
        "Explain the nighttime amplification",
        "Describe the depletion feedback loop without giving medical advice",
    ],
    standards=["Emotion-regulation resource models (Gross); rumination and sleep literature"],
    citations=[CIT_GROSS, CIT_TANGNEY],
    sig_lens=(
        "The Signature lens reads the night's amplification as the "
        "ledger doing its audit after hours: when the day's noise "
        "stops, the books come out. The Signature method treats "
        "sleep, food, and movement as the ledger's operating budget - "
        "the audit cannot be completed on an empty account. His "
        "standing practice: never try to settle a heavy entry at 2 "
        "a.m.; log it, sleep on the logged entry, and open the books "
        "in daylight with a fed body. Clearly labeled Signature-made, "
        "never presented as authentic public record."),
),
dict(
    key="guilt_body_differences", name="No Two Bodies Guilt Alike: How Body Signals Differ Between People",
    group="Compounded", ladder_rank=7, ladder_tier="compounded",
    description=(
        "The guilt patterns in this database are typical, not "
        "universal - individual bodies write the feeling "
        "differently. Some people feel guilt almost entirely in the "
        "gut: nausea and hollowness with barely a thought-loop to "
        "match. Others feel it almost entirely in the head: "
        "relentless replay with a body that seems oddly calm. Some "
        "flush visibly at the slightest twinge; others show nothing "
        "on the surface while churning inside. Age changes the "
        "pattern: children show guilt more behaviorally - "
        "confession, hiding, sudden clinginess - because they lack "
        "the inner vocabulary; older adults often report the "
        "feeling as weariness and heaviness more than acute sting. "
        "Temperament matters: highly reactive people get the full "
        "sympathetic surge - racing heart, sweating - while calmer "
        "temperaments get the quiet postural version. Culture "
        "shapes expression: in settings where emotional restraint "
        "is prized, the outward signs shrink to micro-signs; where "
        "expressiveness is normal, the same feeling may come with "
        "tears and audible sighs. Personal history sets the "
        "sensitivity: someone raised with harsh, unpredictable "
        "punishment may feel intense bodily guilt over trivial "
        "breaches, while someone else barely registers the same "
        "events. The lesson is practical and ethical at once: never "
        "read the absence of visible signs as the absence of the "
        "feeling, and never treat your own body's version as the "
        "template for everyone else's."),
    how_it_works=(
        "Individual differences in guilt's body pattern come from "
        "three sources. First, interoceptive sensitivity - how "
        "finely a person perceives internal signals - varies "
        "widely, so the same gut churn is deafening to one person "
        "and background noise to another. Second, display rules "
        "learned in childhood and culture govern which signals are "
        "allowed out: the feeling may be identical while the "
        "visible pattern differs completely. Third, the appraisal "
        "itself differs: what counts as a breach, how responsibility "
        "is assigned, and how central the standard is all vary by "
        "upbringing, which changes both intensity and texture. "
        "Developmental research adds the age dimension: the "
        "self-evaluative machinery matures through childhood, so "
        "the feeling's form genuinely changes as the machinery "
        "does. The record's point is anti-stereotype: the database "
        "describes central tendencies for teaching, but every real "
        "body is a variation, and the variation is normal."),
    key_points=[
        "Guilt's body pattern varies: gut-dominant, head-dominant, visible, or hidden.",
        "Children show it behaviorally; adults report it as heaviness and weariness.",
        "Temperament, culture, and personal history all reshape the pattern.",
        "Absence of visible signs is not absence of the feeling.",
        "Never use your own body's version as the template for others.",
    ],
    requirements=[
        "Give at least four dimensions of variation with examples",
        "Cover age, temperament, culture, and personal history",
        "State the ethical point about not reading absence as absence",
    ],
    standards=["Individual-differences literature in emotion; display-rule research (Ekman)"],
    citations=[CIT_EKMAN, CIT_TRACY, CIT_TANGNEY],
    sig_lens=(
        "The Signature lens reads bodily differences as different "
        "handwritings in the same ledger: every accountant keeps "
        "books, but no two hands write alike. The Signature method "
        "warns against the common error of auditing someone else's "
        "books by your own handwriting - the entries are real even "
        "when the script is unfamiliar. His rule for reading "
        "others: look for the pattern, not your pattern. Clearly "
        "labeled Signature-made, never presented as authentic public "
        "record."),
),
# ------------------------------------------------- 14-17: facial expression
dict(
    key="guilt_face", name="The Face of Guilt: Eyes, Brows, Mouth, and Micro-Signs",
    group="Compounded", ladder_rank=7, ladder_tier="compounded",
    description=(
        "Here is guilt's most famous facial fact: unlike anger, fear, "
        "or disgust, guilt has no single universal facial expression. "
        "Researchers have never found a prototypical 'guilt face' that "
        "observers recognize across cultures the way they recognize a "
        "smile or a scowl. What guilt has instead is a cluster of "
        "micro-signs, mostly about the eyes and the downward pull. "
        "The eyes: gaze drops or slides away from the other person, "
        "eyelids lower, blinking may increase; in confession the gaze "
        "may flick up briefly to check the listener's reaction, then "
        "drop again. The brows: the inner corners may lift slightly - "
        "the same movement seen in sadness - giving the face a "
        "worried, pleading cast; or the brow may simply go slack and "
        "heavy. The mouth: lips press together or disappear inward, "
        "corners pull down faintly; there may be a brief lip-bite or "
        "a quick, tight, one-sided mouth movement that reads as "
        "wincing. The head: tilts down and often turns a few degrees "
        "away, which amplifies every other sign. The tell-tale "
        "micro-signs are the timing: the gaze aversion that arrives "
        "a half-beat too fast when a topic is raised, the swallow "
        "before answering, the blink-rate spike during the "
        "explanation. None of these proves anything - they are the "
        "described cluster, useful for artists, actors, and writers "
        "depicting the feeling, and for understanding why guilt is so "
        "often missed: the face of guilt is the face of someone "
        "trying not to have a face about it."),
    how_it_works=(
        "The absence of a universal guilt face follows from the "
        "emotion's structure: basic emotions signal to others "
        "('stay back,' 'come closer'), so they evolved readable "
        "displays; guilt's message is to the self, so there was "
        "less pressure for a broadcast signal. What observers do "
        "read is the appeasement cluster - gaze aversion, head "
        "lowering, reduced facial animation - which overlaps with "
        "shame and embarrassment displays, the whole "
        "self-conscious family sharing the shrinking program. The "
        "inner-brow lift shared with sadness reflects the shared "
        "distress component. The lip-pressing and lip-biting are "
        "tension and self-restraint made visible. For recognition "
        "purposes the cluster works probabilistically: several "
        "signs together, timed to a topic or a question, suggest "
        "the feeling more than any single sign does. The record is "
        "for depiction and education - it does not license reading "
        "guilt into any real person's face."),
    key_points=[
        "Guilt has no single universal facial expression - a famous finding in emotion research.",
        "The cluster centers on the eyes: gaze aversion, lowered lids, increased blinking.",
        "Brows may show the sadness-like inner lift; the mouth presses, bites, or winces.",
        "The signs overlap with shame and embarrassment - the self-conscious family shares the shrinking program.",
        "Read the cluster and its timing, never a single sign; never read it into a real person.",
    ],
    requirements=[
        "Cover eyes, brows, mouth, and head position",
        "State the no-universal-face finding plainly",
        "List the tell-tale micro-signs and their timing",
    ],
    standards=["Ekman on the absence of a prototypical guilt expression; Keltner and Buswell appeasement displays"],
    citations=[CIT_EKMAN, CIT_KELTNER, CIT_TRACY],
    sig_lens=(
        "The Signature lens reads the guilty face as the ledger with "
        "its cover half-closed: the eyes will not meet the reader, "
        "the mouth seals the page, the head bows over the entry. "
        "The Signature method notes the honest paradox - the face "
        "tries to hide the account while the micro-signs file a "
        "full report. His guidance for the depicted: play the "
        "aversion, not the announcement; guilt whispers on the "
        "face even when the voice is steady. Clearly labeled "
        "Signature-made, never presented as authentic public record."),
),
dict(
    key="guilt_face_intensity", name="How the Guilty Face Changes With Intensity",
    group="Compounded", ladder_rank=7, ladder_tier="compounded",
    description=(
        "At mild intensity, the guilty face is almost nothing: a "
        "half-second gaze dip when the topic comes up, a slightly "
        "tighter mouth, a blink that arrives a beat early. Most "
        "observers miss it entirely; the person themselves may not "
        "know they showed anything. The expression is brief because "
        "the appraisal is brief - a tug, a note to fix it, done. At "
        "moderate intensity, the cluster becomes readable: sustained "
        "gaze aversion during the relevant conversation, the inner "
        "brow lift holding for seconds, visible lip-pressing, the "
        "head staying lowered. The face may go through waves - "
        "composing itself, then leaking again when the replay loop "
        "refreshes the feeling. At high intensity, the face can "
        "collapse into the full appeasement display: eyes down or "
        "closed, head bowed, hand rising to cover the mouth or "
        "forehead, shoulders visibly rounded. Tears may come - not "
        "the sobbing of grief but a quiet leaking, quickly wiped. "
        "The voice, though not strictly the face, joins in: thinner, "
        "quieter, with audible swallows. One more intensity effect: "
        "duration. Mild signs flash and vanish; intense signs "
        "persist and recur, because the underlying appraisal keeps "
        "re-firing. For anyone depicting the feeling - actor, "
        "artist, writer - the practical scale is: mild is a flicker, "
        "moderate is a held cluster, intense is a sustained "
        "collapse with waves."),
    how_it_works=(
        "Facial intensity tracks appraisal intensity through the "
        "same mechanism that drives the body: stronger "
        "self-attribution and higher perceived harm produce "
        "stronger motor activation of the appeasement program. At "
        "low intensity the activation is sub-threshold for most "
        "muscles, so only the fastest, smallest movements leak - "
        "the gaze dip, the blink. At moderate intensity the program "
        "runs openly but the person can still intermittently "
        "suppress it, producing the wave pattern of leaking and "
        "composing. At high intensity the program overwhelms "
        "suppression; the parasympathetic signs (tears, throat "
        "tightness, swallowing) join the picture. The duration "
        "effect comes from re-appraisal: as long as the replay loop "
        "re-confirms the breach, the face keeps re-displaying. This "
        "is why the intense guilty face looks episodic rather than "
        "steady - it pulses with the loop. The scale is descriptive "
        "for depiction and education."),
    key_points=[
        "Mild: a flicker - half-second gaze dip, tighter mouth, early blink; usually missed.",
        "Moderate: a held cluster - sustained aversion, brow lift, lip-pressing, in waves.",
        "Intense: sustained collapse - bowed head, covered face, quiet tears, thin voice.",
        "Duration scales with intensity because the replay loop keeps re-firing the display.",
        "The scale is for depiction and education: flicker, held cluster, collapse.",
    ],
    requirements=[
        "Describe the face at three intensities with concrete signs",
        "Explain the wave pattern at moderate intensity",
        "Give the practical depiction scale",
    ],
    standards=["Display intensity literature (Ekman); appeasement-display gradation"],
    citations=[CIT_EKMAN, CIT_KELTNER],
    sig_lens=(
        "The Signature lens reads the intensity scale as the ledger "
        "cover opening by degrees: a flicker is the cover lifting a "
        "corner, the held cluster is the page half-shown, the "
        "collapse is the book laid open. The Signature method uses "
        "the face as the honesty gauge of the account - the longer "
        "the display persists, the larger the unpaid balance the "
        "body is reporting. His note: the waves are the ledger "
        "re-opening itself; each wave is another chance to pay. "
        "Clearly labeled Signature-made, never presented as "
        "authentic public record."),
),
dict(
    key="guilt_hiding_faking", name="Hiding and Faking Guilt: What Leaks Through",
    group="Compounded", ladder_rank=8, ladder_tier="compounded",
    description=(
        "People hide guilt constantly - in negotiations, in "
        "families, in any situation where admitting the breach "
        "feels costly - and the hiding itself has a pattern. The "
        "hider over-controls: the face goes oddly still, the voice "
        "flattens into careful neutrality, gestures shrink to "
        "nothing. But the appeasement program leaks around the "
        "edges: the gaze still slides away at the key moment, the "
        "swallow still comes before the careful answer, the blink "
        "rate still spikes. Over-explaining is the classic verbal "
        "leak - the innocent explanation is usually short, while "
        "the hidden-guilt explanation keeps adding details nobody "
        "asked for. Deflection is another: answering a different "
        "question than the one asked, or turning the topic back on "
        "the questioner. Faking guilt - performing remorse that is "
        "not felt - has its own tells, mostly in timing and "
        "proportion: the apology arrives too polished, the sad face "
        "switches on and off too cleanly between audiences, the "
        "words of contrition come without any concrete offer of "
        "repair. Real guilt is clumsy about repair and reluctant "
        "about display; faked guilt is fluent about display and "
        "vague about repair. The asymmetry is the practical key: "
        "hiding leaks through the body, faking leaks through the "
        "absence of real repair. Neither pattern proves anything "
        "about any real person - they are described tendencies for "
        "education, depiction, and fiction, not tools for "
        "accusation."),
    how_it_works=(
        "Hiding guilt means running two programs at once: the "
        "appeasement display pushing out and the suppression system "
        "pushing down. The conflict produces the over-controlled "
        "stillness plus the micro-leaks - suppression is good at "
        "stopping large movements and bad at stopping fast, small "
        "ones, which is why the eyes and the throat betray what the "
        "mouth conceals. Cognitive load adds the verbal leaks: "
        "maintaining a false account consumes working memory, so "
        "the story gets longer (filling silence feels safer than "
        "pausing) and less consistent. Faked guilt fails "
        "differently: because the underlying appraisal never "
        "fired, the display is assembled from the outside - from "
        "what remorse is supposed to look like - and assembled "
        "displays have clean edges that real ones lack. The repair "
        "asymmetry follows from motivation: real guilt wants the "
        "account settled and reaches for concrete amends; performed "
        "guilt wants the audience satisfied and reaches for "
        "impressive wording. The record describes; it does not "
        "authorize judging real people."),
    key_points=[
        "Hiding guilt produces over-controlled stillness plus micro-leaks: gaze slides, swallows, blink spikes.",
        "Over-explaining and deflection are the classic verbal leaks of hidden guilt.",
        "Faked guilt is too polished: clean on/off switching, fluent display, vague on repair.",
        "Real guilt is clumsy about display and concrete about repair; faked guilt is the reverse.",
        "These are described tendencies for education and depiction - never tools for accusing real people.",
    ],
    requirements=[
        "Describe the hiding pattern: stillness plus specific leaks",
        "Describe the faking pattern: timing, proportion, repair asymmetry",
        "State plainly these are not accusation tools",
    ],
    standards=["Deception and leakage literature (Ekman); cognitive-load accounts of concealment"],
    citations=[CIT_EKMAN, CIT_TANGNEY],
    sig_lens=(
        "The Signature lens reads hidden guilt as a ledger kept in "
        "a locked drawer - the lock is visible, which is itself an "
        "entry. The Signature method reads faked guilt as a forged "
        "receipt: the handwriting is too neat, the amount too round, "
        "and no money ever changes hands. His test of the account: "
        "real books show payments, not just paperwork. Clearly "
        "labeled Signature-made, never presented as authentic public "
        "record."),
),
dict(
    key="guilt_expression_gallery", name="Drawing and Playing Guilt: Expression Gallery Notes",
    group="Compounded", ladder_rank=8, ladder_tier="compounded",
    description=(
        "For the artist, the actor, or the writer: guilt is drawn "
        "and played from the top down and the inside out. Start "
        "with the spine - guilt shortens it. The head pitches "
        "forward ten to fifteen degrees; the chin tucks; the whole "
        "figure loses an inch of height it actually has. The eyes "
        "are the second decision: lids at half-mast, gaze directed "
        "down and to the side, never at the viewer or the scene "
        "partner - the guilty figure looks at the floor the way a "
        "reader looks at a difficult page. Brows: lift the inner "
        "corners a few millimeters for the worried cast, or let "
        "them go heavy and flat for the dulled, ruminating version. "
        "The mouth: press the lips until they thin, or bite the "
        "lower lip at one corner; avoid the open-mouth shapes of "
        "surprise or grief - guilt's mouth is closed, sealing. "
        "Hands: give them something to do - wringing, sleeve- "
        "pulling, one hand covering the mouth, both hands clasped "
        "too tightly. Staging notes for actors: guilt rarely "
        "enters a room; it is already there when noticed. Play the "
        "stillness between lines, not the lines - the guilty "
        "character goes motionless when the topic lands, then "
        "moves too much in the recovery. The voice: drop the "
        "volume a third, slow the pace, let sentences trail into "
        "qualifiers. Lighting and composition for visual artists: "
        "guilt reads in shadow and in profile - the averted face "
        "in three-quarter turn, the figure placed slightly apart "
        "from the group, negative space doing the work of "
        "isolation. The through-line for every medium: guilt is "
        "the emotion of the half-hidden - show the hiding, and the "
        "feeling shows itself."),
    how_it_works=(
        "The gallery notes work because they translate the "
        "appeasement program into craft decisions. The shortened "
        "spine and averted gaze are the visual shorthand every "
        "audience already reads unconsciously; using them "
        "deliberately lets the depiction land without "
        "explanation. The closed mouth versus open mouth "
        "distinction separates guilt from grief and surprise at a "
        "glance. The busy hands externalize the inner restlessness "
        "of the repair urge with nowhere to go. The actor's note "
        "about stillness follows from attention capture: the "
        "replay loop freezes the body, so playing the freeze "
        "plays the feeling. The voice direction follows from "
        "the conflict between confession urge and concealment "
        "urge - quieter, slower, trailing off. The composition "
        "note follows from the social meaning: guilt isolates, "
        "so the frame should isolate. Together the notes give "
        "makers a complete, consistent vocabulary for the "
        "feeling across media."),
    key_points=[
        "Draw guilt top-down: shortened spine, pitched-forward head, half-mast averted eyes.",
        "The mouth is closed and sealing - pressed, thinned, or bitten - never open.",
        "Give the hands work: wringing, covering, clasping too tightly.",
        "Actors: play the stillness between lines; the voice drops a third in volume.",
        "Composition: shadow, profile, three-quarter averted turn, negative space for isolation.",
    ],
    requirements=[
        "Concrete craft notes for visual artists, actors, and writers",
        "Cover spine, eyes, brows, mouth, hands, voice, and composition",
        "Ground each note in the appeasement program",
    ],
    standards=["Performance and depiction craft; appeasement-display ethology"],
    citations=[CIT_KELTNER, CIT_EKMAN],
    sig_lens=(
        "The Signature lens reads the gallery as the ledger "
        "illustrated: every craft note is a way of drawing the "
        "half-closed book. The Signature method gives makers one "
        "image to hold - the accountant who cannot meet the "
        "creditor's eyes - and lets every choice flow from it: the "
        "spine bows, the gaze drops, the hands fidget with the "
        "unpaid page. His direction in one line: show the hiding, "
        "and the feeling shows itself. Clearly labeled "
        "Signature-made, never presented as authentic public record."),
),
# ------------------------------------------------- 18-21: triggers
dict(
    key="guilt_classic_triggers", name="The Classic Triggers of Guilt",
    group="Advanced", ladder_rank=8, ladder_tier="advanced",
    description=(
        "The classic triggers of guilt are the situations where a "
        "standard is breached in the most recognizable ways. "
        "Breaking a promise: the explicit commitment made and then "
        "not kept - the missed call, the forgotten favor, the "
        "deadline let slide. Causing harm: words or actions that "
        "hurt someone, from the careless sharp remark to the "
        "serious injury - the clearer the causal line from act to "
        "harm, the stronger the trigger. Neglect and omission: not "
        "the thing done but the thing not done - the visit never "
        "made, the help never offered, the warning never given; "
        "omission guilt is quieter but often longer-lasting than "
        "commission guilt. Betrayal of trust: confiding a secret "
        "that was told in confidence, siding against an ally, the "
        "small disloyalties of everyday life. Selfish advantage: "
        "taking the larger share, cutting the corner, benefiting "
        "from someone else's loss. Violating a personal code: "
        "acting against a deeply held value - the vegetarian who "
        "eats meat, the honest person who lies - where the witness "
        "is entirely internal. Failing a role: the parent who "
        "misses the recital, the friend who is not there, the "
        "professional who cuts a corner - guilt anchored to an "
        "identity standard. Each classic trigger shares the same "
        "structure: a standard, a breach, and a self that accepts "
        "responsibility. Learn the list and you can see guilt "
        "coming - in stories, in simulations, and in your own "
        "planning, where anticipating the trigger is the cheapest "
        "prevention there is."),
    how_it_works=(
        "Classic triggers work because they complete the guilt "
        "sequence with unusual efficiency: the standard is clear, "
        "the breach is observable, and responsibility is hard to "
        "dodge. Promise-breaking is the cleanest case - the "
        "standard was stated aloud, so the appraisal has almost "
        "nothing to argue about. Harm-causing adds the victim's "
        "visible distress, which feeds the perceived-harm dial "
        "directly. Omission triggers work more slowly: because "
        "nothing happened, the breach must be constructed by "
        "counterfactual thinking - 'if I had acted, things would "
        "be different' - which is why omission guilt arrives late "
        "and lingers. Role-failure triggers hit the standard- "
        "centrality dial: the standard is woven into identity, so "
        "the breach threatens the self-concept, not just the "
        "record. The practical use of the catalog is preventive: "
        "anticipatory guilt fires on imagined triggers, which "
        "means walking through this list before a decision is one "
        "of the most reliable ways to avoid the feeling after it."),
    key_points=[
        "Seven classic triggers: promise-breaking, harm-causing, omission, betrayal, selfish advantage, code violation, role failure.",
        "Each shares the structure: a clear standard, an observable breach, hard-to-dodge responsibility.",
        "Omission guilt arrives late and lingers, built by counterfactual thinking.",
        "Role-failure triggers hit identity-level standards and threaten the self-concept.",
        "The catalog's practical use is preventive: anticipatory guilt fires on imagined triggers.",
    ],
    requirements=[
        "List and describe at least seven classic triggers with examples",
        "Explain why omission guilt has a different time profile",
        "State the preventive use of the catalog",
    ],
    standards=["Appraisal-theory trigger taxonomy; Baumeister interpersonal contexts of guilt"],
    citations=[CIT_BAUMEISTER, CIT_LAZARUS, CIT_TANGNEY],
    sig_lens=(
        "The Signature lens reads the classic triggers as the "
        "ledger's standard chart of accounts: seven columns where "
        "debts are most often posted. The Signature method treats "
        "the catalog as a pre-audit checklist - run the planned "
        "action past the seven columns before acting, and most "
        "debts are never incurred. His shorthand: the cheapest "
        "payment is the one never owed. Clearly labeled "
        "Signature-made, never presented as authentic public record."),
),
dict(
    key="guilt_personal_triggers", name="Personal Triggers: Memories, Anniversaries, and Private Associations",
    group="Advanced", ladder_rank=9, ladder_tier="advanced",
    description=(
        "Beyond the classic triggers, every person carries a "
        "private set - triggers that would mean nothing to anyone "
        "else. A song that was playing during the argument; the "
        "smell of a hospital corridor; a date on the calendar that "
        "marks the anniversary of the breach; the particular "
        "intersection where the accident happened; a phrase - "
        "'you always' or 'never mind' - that was the last thing "
        "said. These triggers work through associative memory: "
        "the breach was encoded together with its context, and "
        "any piece of the context can re-activate the whole "
        "appraisal. Anniversaries are the most predictable: the "
        "year-mark of a loss or a wrongdoing reliably re-opens the "
        "account, often catching the person by surprise even when "
        "they knew the date was coming. Private associations are "
        "the least predictable: a stranger's laugh with the same "
        "timbre, a brand of tea, a weather pattern. Personal "
        "triggers explain why two people can walk through the same "
        "day and only one of them gets ambushed - the day is "
        "neutral; the associations are not. They also explain the "
        "aftershock pattern: most aftershocks are not random, they "
        "are personal triggers firing on schedule. Mapping one's "
        "own set is practical self-knowledge: once a trigger is "
        "named - 'every October,' 'that song,' 'hospitals' - its "
        "ambush power drops, because the appraisal can be met "
        "with recognition instead of surprise."),
    how_it_works=(
        "Personal triggers form through episodic encoding: the "
        "emotional peak of the guilt episode tags surrounding "
        "details - sensory, temporal, linguistic - into the same "
        "memory trace. Later, any tagged detail can cue retrieval "
        "of the trace, and retrieval re-runs the appraisal: the "
        "standard, the breach, the self-attribution all fire again "
        "as if fresh. Anniversaries work through temporal tagging "
        "plus anticipation - the calendar itself becomes a cue, "
        "and dread of the date can start the loop before the date "
        "arrives. The reason naming a trigger weakens it is "
        "re-appraisal: when the cue is recognized as a cue ('this "
        "is the song, not the event'), the attribution step can be "
        "met with the knowledge that the account was already "
        "settled, which lets the sequence close instead of "
        "re-opening. Unnamed triggers keep their power because "
        "each firing feels like new evidence rather than an old "
        "recording. The record maps the mechanism for education; "
        "it does not prescribe any technique for any real person."),
    key_points=[
        "Personal triggers are private associations: songs, smells, dates, phrases, places.",
        "They form through episodic encoding - the breach's context gets tagged into the memory trace.",
        "Anniversaries are the most predictable triggers; private associations the least.",
        "Most aftershocks are personal triggers firing on schedule, not random events.",
        "Naming a trigger weakens its ambush power by enabling recognition over surprise.",
    ],
    requirements=[
        "Give concrete examples across sensory, temporal, and linguistic channels",
        "Explain anniversary effects and the ambush mechanism",
        "Explain why naming a trigger reduces its power",
    ],
    standards=["Associative memory and emotion literature; anniversary-reaction research"],
    citations=[CIT_TANGNEY, CIT_DAMASIO],
    sig_lens=(
        "The Signature lens reads personal triggers as the ledger's "
        "margin notes: small marks beside old entries that re-open "
        "the page whenever they are seen. The Signature method "
        "treats trigger-mapping as indexing the archive - once every "
        "margin note is cataloged, no page can surprise its keeper. "
        "His practice: write the trigger next to the entry it "
        "re-opens; an indexed ambush is just a reminder. Clearly "
        "labeled Signature-made, never presented as authentic public "
        "record."),
),
dict(
    key="guilt_surprise_triggers", name="Surprise Triggers: The Unexpected Things That Set Off Guilt",
    group="Advanced", ladder_rank=9, ladder_tier="advanced",
    description=(
        "Some guilt arrives from directions nobody was watching. "
        "Good news can trigger it: the promotion that means a "
        "friend was passed over, the recovery while someone else "
        "is still ill - the feeling that one's good fortune is "
        "someone else's loss. Rest can trigger it: the day off "
        "while colleagues work, the nap while the house needs "
        "cleaning - idleness appraised as dereliction. Pleasure "
        "can trigger it: enjoying a meal, a purchase, a holiday "
        "while others go without - sometimes called luxury guilt "
        "or privilege guilt, the breach being against a standard "
        "of fairness or solidarity. Being believed can trigger it: "
        "receiving trust or praise one feels is undeserved - the "
        "impostor-adjacent sting of 'if they knew.' Outgrowing can "
        "trigger it: the success that distances you from family or "
        "old friends, the education or income that changes the "
        "relationship - loyalty appraised as betrayal. Even "
        "someone else's kindness can trigger it: the gift you "
        "cannot reciprocate, the help you cannot repay - the "
        "account opened in your favor that you cannot close. What "
        "makes these surprising is that no standard was "
        "deliberately broken; the appraisal constructs the breach "
        "from circumstance - from comparison, from luck, from "
        "asymmetry. Surprise triggers are worth cataloging because "
        "they are the ones people feel most confused by, and "
        "confusion about guilt usually means the attribution step "
        "deserves a second look: is there really a breach here, "
        "or only a circumstance wearing a breach's clothes?"),
    how_it_works=(
        "Surprise triggers work through the same sequence as "
        "classic ones, but the transgression step is built by "
        "comparison rather than by action. Good-news guilt "
        "compares outcomes and assigns the self a share of "
        "responsibility for the asymmetry - often inaccurately, "
        "since luck is not agency. Rest and pleasure guilt apply "
        "a productivity or solidarity standard to a neutral "
        "state, manufacturing a breach where none occurred. "
        "Being-believed guilt applies an honesty standard to a "
        "self-assessment ('I am not as competent as they think'), "
        "which may itself be miscalibrated. Outgrowing guilt "
        "applies a loyalty standard to a life change, treating "
        "growth as abandonment. The common thread is an "
        "overactive attribution step: the self claims "
        "responsibility for circumstances - luck, asymmetry, "
        "change - that are not breaches of any standard the "
        "person would endorse on reflection. This is why the "
        "record's key question matters: the attribution step is "
        "exactly where surprise guilt most often goes wrong, and "
        "auditing it is the whole work."),
    key_points=[
        "Surprise triggers include good news, rest, pleasure, being believed, outgrowing, and unrepayable kindness.",
        "No standard is deliberately broken; the breach is constructed by comparison or circumstance.",
        "The common thread is an overactive attribution step claiming responsibility for luck or asymmetry.",
        "Confusion about guilt is a signal to audit the attribution step.",
        "Cataloging surprise triggers turns confusion into a recognizable pattern.",
    ],
    requirements=[
        "Describe at least six surprise triggers with the mechanism of each",
        "Explain the comparison-built breach versus the action-built breach",
        "Give the attribution-audit question as the key tool",
    ],
    standards=["Attribution theory; moral emotion and comparison literature (Haidt)"],
    citations=[CIT_HAIDT, CIT_TANGNEY, CIT_LAZARUS],
    sig_lens=(
        "The Signature lens reads surprise triggers as ledger "
        "entries written in invisible ink: they appear on the page "
        "without any transaction behind them. The Signature method "
        "treats every surprise entry as guilty-until-audited - hold "
        "the feeling, check for a real transaction, and erase the "
        "entry if none is found. His rule: circumstance is not "
        "conduct, and the ledger records conduct. Clearly labeled "
        "Signature-made, never presented as authentic public record."),
),
dict(
    key="guilt_chain_reactions", name="Chain Reactions: When One Trigger Ignites a Cascade",
    group="Advanced", ladder_rank=9, ladder_tier="advanced",
    description=(
        "Guilt rarely travels alone - one trigger often ignites a "
        "cascade. It starts with the primary breach: the forgotten "
        "promise, the sharp word. The replay loop begins, and the "
        "loop is a search engine: as it replays the scene, it "
        "retrieves similar scenes - the other forgotten promises, "
        "the other sharp words - and each retrieved scene brings "
        "its own guilt online. Now the feeling is no longer about "
        "one act; it is about a pattern, and patterns feel like "
        "character: 'I always do this,' 'this is who I am.' The "
        "cascade then recruits partner emotions: shame arrives "
        "with its global verdict, anxiety arrives with its "
        "forecasting of consequences, sadness arrives with its "
        "sense of loss. Each partner amplifies the others - the "
        "shame makes the guilt feel deserved, the anxiety makes "
        "repair feel urgent and impossible at once, the sadness "
        "drains the energy repair would need. Defensive reactions "
        "can join the chain too: irritability at anyone who "
        "notices, withdrawal from the people who could help, "
        "rationalization that hardens into resentment. The full "
        "cascade can turn a single missed call into a day-long "
        "storm. Breaking a cascade means intervening at the "
        "joints: name the primary trigger separately from the "
        "retrieved archive ('this is about today, not about "
        "every time'), address the partners one at a time, and "
        "execute one concrete repair - cascades feed on "
        "abstraction and starve on specifics."),
    how_it_works=(
        "Cascades form through three mechanisms working together. "
        "First, associative retrieval: the replay loop's search "
        "for context pulls in similar episodes, and each one "
        "re-fires its own appraisal. Second, abstraction creep: "
        "repeated similar breaches get summarized into a trait "
        "judgment ('I am unreliable'), which converts guilt's "
        "action-level signal into shame's self-level verdict and "
        "widens the feeling's scope. Third, emotion recruitment: "
        "the arousal and negative valence of guilt lower the "
        "threshold for partner emotions, so shame, anxiety, and "
        "sadness ignite more easily than they would alone. The "
        "defensive reactions are secondary appraisals - the mind "
        "coping with the cascade by attacking the witnesses "
        "(irritability), avoiding the cues (withdrawal), or "
        "rewriting the record (rationalization). Intervention at "
        "the joints works because each mechanism has a weak point: "
        "retrieval is weakened by specificity (dating each breach "
        "separately), abstraction is weakened by behavioral "
        "language ('I missed the call' not 'I am unreliable'), "
        "and recruitment is weakened by addressing one feeling at "
        "a time. The record describes the cascade for recognition "
        "and education."),
    key_points=[
        "One trigger ignites a cascade via associative retrieval of similar breaches.",
        "Abstraction creep converts 'I did' into 'I am,' widening guilt into shame.",
        "Partner emotions (shame, anxiety, sadness) are recruited and amplify each other.",
        "Defensive reactions - irritability, withdrawal, rationalization - can join the chain.",
        "Break cascades at the joints: specificity against retrieval, behavioral language against abstraction, one repair against the storm.",
    ],
    requirements=[
        "Trace a cascade from primary trigger through at least three stages",
        "Name the three cascade mechanisms",
        "Give the joint-by-joint intervention for each mechanism",
    ],
    standards=["Associative network models of emotion; rumination cascade literature"],
    citations=[CIT_TANGNEY, CIT_GROSS, CIT_DAMASIO],
    sig_lens=(
        "The Signature lens reads the cascade as the ledger "
        "avalanche: one entry's audit pulls every related entry "
        "off the shelf at once, and the pile buries the "
        "accountant. The Signature method fights avalanches with "
        "shelving discipline - one entry, one date, one payment at "
        "a time - because the pile is always scarier than the "
        "sum of its pages. His rule: never audit the whole "
        "archive in one sitting; settle today's entry today. "
        "Clearly labeled Signature-made, never presented as "
        "authentic public record."),
),
# ------------------------------------------------- 22-25: behavior
dict(
    key="guilt_behavior_actions", name="What People Do When Guilty: Typical Actions and Reactions",
    group="Advanced", ladder_rank=9, ladder_tier="advanced",
    description=(
        "Guilt moves people, and the movements fall into recognizable "
        "patterns. Repair actions come first: apologizing, confessing "
        "without being asked, offering to fix or replace what was "
        "damaged, doing extra favors for the harmed person, changing "
        "the behavior going forward. These are the feeling's native "
        "language - the repair urge made visible. Appeasement actions "
        "come second: excessive agreeableness, nervous laughter, "
        "over-thanking, bringing small gifts, hovering helpfully - "
        "behaviors aimed at restoring goodwill rather than fixing "
        "the specific breach. Avoidance actions come third: dodging "
        "the person, changing the subject when the topic nears, "
        "staying late at work to miss dinner, the thousand small "
        "evasions of someone who cannot face the account. "
        "Self-punishment actions come fourth: skipping pleasures, "
        "working to exhaustion, declining things they want - the "
        "ledger balanced by suffering instead of by repair. "
        "Defensive actions come fifth: denial, minimization ('it was "
        "nothing'), blame-shifting, rationalization, and the "
        "preemptive strike of getting angry first so the other "
        "person goes on defense instead. Most real episodes mix "
        "several patterns - an apology followed by avoidance, "
        "appeasement curdling into irritability. The practical "
        "reading key: repair actions close the sequence; avoidance "
        "and defensive actions stall it; self-punishment mimics "
        "repair while changing nothing for the harmed person."),
    how_it_works=(
        "The five action patterns map onto the guilt sequence's "
        "possible exits. Repair actions execute the repair beat "
        "directly and are the only ones that close the sequence - "
        "which is why they reliably reduce the feeling. Appeasement "
        "actions address the relationship without addressing the "
        "breach; they soothe the social channel while leaving the "
        "account open, which is why they often need repeating. "
        "Avoidance actions are the shame-partner taking the wheel: "
        "the hiding urge overrides the repair urge, and the "
        "sequence stalls with the account still open. "
        "Self-punishment is a misdirected repair beat - the "
        "suffering is real but it pays the wrong creditor, since "
        "the harmed person receives nothing. Defensive actions are "
        "the attribution step being rewritten under pressure: if "
        "the breach was not mine, there is nothing to repair - a "
        "solution that protects the self-image at the cost of the "
        "relationship and usually at the cost of the truth. "
        "Recognizing which pattern is running is the first step to "
        "choosing the one that actually settles the account."),
    key_points=[
        "Five patterns: repair, appeasement, avoidance, self-punishment, and defensive actions.",
        "Only repair actions close the sequence; the rest stall it, soothe around it, or misdirect it.",
        "Appeasement restores goodwill without fixing the breach - which is why it needs repeating.",
        "Self-punishment pays the wrong creditor: suffering instead of amends.",
        "Defensive actions rewrite the attribution step to protect self-image at the relationship's cost.",
    ],
    requirements=[
        "Describe all five action patterns with concrete behaviors",
        "Explain which patterns close the sequence and which stall it",
        "Give the reading key for recognizing the running pattern",
    ],
    standards=["Baumeister interpersonal approach: reparative behaviors; Tangney action tendencies"],
    citations=[CIT_BAUMEISTER, CIT_TANGNEY],
    sig_lens=(
        "The Signature lens reads the five patterns as five ways "
        "of handling a debt: pay it, sweeten the creditor, dodge "
        "the creditor, punish yourself instead of paying, or forge "
        "the books. The Signature method recognizes only the first "
        "as payment; the rest are ledger theater - motion that "
        "looks like settling but moves no money. His audit "
        "question for any guilty action: who receives the payment? "
        "Clearly labeled Signature-made, never presented as "
        "authentic public record."),
),
dict(
    key="guilt_speech_patterns", name="What People Say When Guilty: Phrases, Tone, and Speech Patterns",
    group="Advanced", ladder_rank=10, ladder_tier="advanced",
    description=(
        "Guilty speech has a sound, and once you hear it you cannot "
        "unhear it. The characteristic phrases: 'I'm sorry, I'm "
        "sorry, I'm so sorry' - repetition doing the work that "
        "conviction cannot; 'I feel terrible about this' - the "
        "feeling announced as a substitute for the fix; 'I didn't "
        "mean to' - true or not, the intent defense; 'You know I "
        "would never' - the character witness called early; 'It "
        "wasn't that big a deal' - minimization arriving in the "
        "same breath as the apology; 'But you...' - the pivot to "
        "counter-accusation. The tone: quieter than usual, faster "
        "than usual or halting, with audible swallows and throat- "
        "clearing; pitch may rise with anxiety or drop with "
        "dejection. The patterns: over-explaining - the timeline "
        "told in unnecessary detail, as if completeness could "
        "substitute for accountability; hedging - 'sort of,' "
        "'kind of,' 'a little' softening every verb; preemptive "
        "confession - blurting it out before being asked, in a "
        "rush, to control the telling; and the question that is "
        "not a question - 'Are you mad at me?' asked repeatedly, "
        "fishing for absolution. Silence is part of the pattern "
        "too: the guilty person goes quiet when the topic "
        "approaches, answers in monosyllables, or fills the air "
        "with nervous chatter about anything else. Writers and "
        "actors take note: guilty dialogue is not about the words "
        "but about the work the words are doing - confessing, "
        "deflecting, minimizing, or fishing - and the work shows "
        "in the rhythm before it shows in the vocabulary."),
    how_it_works=(
        "Guilty speech patterns are the verbal half of the "
        "appeasement and repair programs. Over-explaining comes "
        "from the same cognitive load as hidden-guilt leakage: "
        "managing the account in real time consumes working "
        "memory, and the mouth fills the gaps the mind cannot "
        "afford to leave. Hedging is the attribution step spoken "
        "aloud - the self negotiating how much responsibility to "
        "accept, syllable by syllable. The apology-repetition "
        "pattern reflects the repair urge firing without a "
        "concrete repair plan: the words are offered because no "
        "action is ready. Minimization and counter-accusation are "
        "the defensive exit, rewriting the attribution mid- "
        "sentence. The absolution-fishing question is the repair "
        "urge outsourcing its completion: if the other person "
        "declares the account closed, the feeling can stand down "
        "without the work. Tone changes follow arousal: the "
        "quieter-faster-halting cluster is the body running the "
        "appeasement program while the mind runs the replay loop. "
        "The record is for depiction and recognition in fiction "
        "and education - not for diagnosing real speakers."),
    key_points=[
        "Characteristic phrases: repeated apologies, intent defenses, minimization, counter-accusation pivots.",
        "Tone: quieter, faster or halting, with swallows and throat-clearing.",
        "Patterns: over-explaining, hedging, preemptive confession, absolution-fishing questions.",
        "Silence and nervous chatter are both part of the pattern.",
        "Read the work the words are doing - confessing, deflecting, minimizing, fishing - not just the vocabulary.",
    ],
    requirements=[
        "Quote at least six characteristic phrases with the work each does",
        "Describe tone and at least four speech patterns",
        "Cover silence as part of the pattern",
    ],
    standards=["Discourse patterns in apology and account literature; Tangney confession tendencies"],
    citations=[CIT_TANGNEY, CIT_BAUMEISTER],
    sig_lens=(
        "The Signature lens reads guilty speech as the ledger read "
        "aloud: the stammering is the accountant struggling with "
        "the entry, the over-explaining is footnotes multiplying, "
        "the fishing question is asking the creditor to close the "
        "books early. The Signature method judges spoken accounts "
        "by one measure - does the telling end in a payment plan "
        "or in applause for the telling? His rule for the guilty "
        "speaker: short confession, concrete repair, then stop "
        "talking. Clearly labeled Signature-made, never presented "
        "as authentic public record."),
),
dict(
    key="guilt_decisions_judgment", name="How Guilt Changes Decisions and Judgment",
    group="Advanced", ladder_rank=10, ladder_tier="advanced",
    description=(
        "Guilt is a thumb on the scale of judgment, and it presses "
        "in consistent directions. First, it narrows the field of "
        "concern: the harmed person and the breach fill the frame, "
        "and everything else - costs, alternatives, the bigger "
        "picture - shrinks. Decisions made in this frame "
        "overweight repair: the guilty person agrees to too much, "
        "promises too fast, and accepts terms they would refuse "
        "calm. Second, guilt inflates perceived responsibility "
        "going forward: after a breach, people overestimate their "
        "control over outcomes and take on obligations that are "
        "not theirs - the over-functioning that follows many "
        "guilt episodes. Third, guilt distorts risk: it can make "
        "people risk-averse (avoiding any action that might "
        "create another breach) or paradoxically risk-seeking "
        "(the 'in for a penny' effect, where the account already "
        "feels ruined so further costs feel free). Fourth, guilt "
        "biases moral judgment outward: the guilty judge others' "
        "similar breaches more harshly - the confessed cheat "
        "becomes the fiercest critic of cheating - because "
        "condemning the act in others distances it from the self. "
        "Fifth, guilt impairs the very judgment repair needs: "
        "depleted attention, poor sleep, and the replay loop's "
        "monopoly on working memory make for worse decisions "
        "exactly when good ones matter most. The practical "
        "countermeasure is structural, not willpower-based: delay "
        "big decisions until the peak passes, write the options "
        "down to widen the frame beyond the breach, and check "
        "any promise made under guilt against what you would "
        "agree to calm - the calm self is the better negotiator."),
    how_it_works=(
        "The judgment effects follow from guilt's appraisal "
        "machinery running in the background of every decision. "
        "The narrowed frame is attention capture: the replay "
        "loop holds working memory, so deliberation literally "
        "has less room for other factors. Inflated "
        "responsibility is the attribution step overgeneralizing "
        "- once the self has been found responsible, the "
        "threshold for finding it responsible again drops. The "
        "risk distortion runs through the account metaphor the "
        "mind actually uses: a breached standard feels like a "
        "debt, and debt psychology is well mapped - some debtors "
        "become hyper-cautious, others figure the credit is "
        "already ruined. Harsh outward moral judgment is "
        "self-distancing: condemning the act in others is an "
        "attempt to re-file the self on the judges' side of the "
        "ledger. The impaired-decision effect is resource "
        "depletion, the same mechanism behind the sleep and "
        "energy record. The countermeasures work because they "
        "are external: paper widens the frame, delay lets the "
        "peak pass, the calm-self check imports a second "
        "appraiser. The record describes tendencies for "
        "education, not rules for any real person's choices."),
    key_points=[
        "Guilt narrows the decision frame to the breach and overweights repair.",
        "Perceived responsibility inflates: the guilty overestimate their control and take on others' obligations.",
        "Risk distorts both ways - hyper-caution or 'in for a penny' recklessness.",
        "The guilty judge others' similar breaches more harshly (self-distancing).",
        "Countermeasures are structural: delay big decisions, write options down, check promises against the calm self.",
    ],
    requirements=[
        "Describe at least five judgment effects with mechanisms",
        "Explain the risk distortion in both directions",
        "Give structural countermeasures, not willpower advice",
    ],
    standards=["Affect and decision-making literature; Baumeister on guilt and self-regulation"],
    citations=[CIT_BAUMEISTER, CIT_LAZARUS, CIT_GROSS],
    sig_lens=(
        "The Signature lens reads guilt-tinted judgment as the "
        "ledger auditing everything at once: every open account "
        "colors every new entry. The Signature method bars major "
        "decisions during an active audit - the accountant is "
        "compromised while the books are unbalanced. His "
        "procedure: log the decision, close the urgent account "
        "first, then decide with clean books. The calm self is "
        "the senior partner; the guilty self is the junior doing "
        "the audit - juniors advise, seniors decide. Clearly "
        "labeled Signature-made, never presented as authentic "
        "public record."),
),
dict(
    key="guilt_escalation", name="Guilt Under Rising Intensity: How Actions Escalate",
    group="Advanced", ladder_rank=10, ladder_tier="advanced",
    description=(
        "Watch guilt climb the volume dial and the actions climb "
        "with it, through a recognizable staircase. Step one, the "
        "tug: a private wince, a mental note, a quick fix - the "
        "text sent, the small apology made. Step two, the ache: "
        "repeated apologies, checking whether the person is still "
        "upset, small reparative gestures stacking up - the extra "
        "favor, the unasked-for help. Step three, the weight: "
        "confession expands - telling more people, in more detail, "
        "seeking absolution from audiences beyond the harmed "
        "person; self-punishment begins - pleasures declined, "
        "standards for the self raised to punishing heights. Step "
        "four, the flood: the cascade fully open - every related "
        "breach retrieved, partners recruited, sleep and appetite "
        "disrupted; behavior becomes erratic - grandiose promises "
        "of change, sudden avoidance of everyone involved, "
        "irritability at anyone who witnesses the state. Step "
        "five, the breaking point: one of three exits - genuine "
        "repair finally executed at full scale (the real apology, "
        "the real amends, the changed behavior sustained), "
        "collapse into withdrawal (cutting off the people and "
        "places that cue the guilt), or defensive hardening "
        "(the attribution rewritten permanently: it was not my "
        "fault, they deserved it, the standard was wrong). The "
        "staircase is not inevitable - intervention at any step "
        "changes the climb. The earlier the honest repair, the "
        "shorter the staircase. And the exits matter: only the "
        "first one closes the account; withdrawal just moves the "
        "ledger to a drawer, and hardening forges the books."),
    how_it_works=(
        "Escalation is the guilt sequence failing to close at "
        "each step and re-firing at higher gain. At step one the "
        "repair beat is small and sufficient; if it is skipped - "
        "through busyness, dread, or denial - the appraisal "
        "re-confirms and the next firing carries the backlog. "
        "Each unfixed cycle adds retrieved breaches (the cascade "
        "mechanism) and recruited partners, so the feeling grows "
        "even though the original act has not changed - this is "
        "why old guilt feels larger than the event warrants. The "
        "confession-expansion at step three is the repair urge "
        "seeking new creditors when the original one feels "
        "insufficient or unreachable. The erratic behavior at step "
        "four is resource depletion plus partner-emotion "
        "recruitment: the system is running hot with no "
        "resolution. The three exits are the sequence's only "
        "stable endpoints: repair closes it, withdrawal shelves "
        "it (cue-dependent, so it re-opens), hardening corrupts "
        "it (the standard itself is edited to acquit the self). "
        "The record's practical point is the staircase's "
        "reversibility: every step up was a skipped repair, so "
        "every step down is a repair finally made."),
    key_points=[
        "Escalation climbs a staircase: tug, ache, weight, flood, breaking point.",
        "Each step up is a skipped repair; the feeling grows while the original act stays the same.",
        "Confession expands to new audiences when the original creditor feels insufficient.",
        "Three exits: genuine repair (closes), withdrawal (shelves), defensive hardening (corrupts).",
        "The staircase is reversible: every step down is a repair finally made.",
    ],
    requirements=[
        "Describe all five steps with concrete behaviors",
        "Explain why the feeling grows while the act stays the same",
        "Name and evaluate the three exits",
    ],
    standards=["Escalation dynamics in rumination literature; Baumeister on guilt and self-regulation failure"],
    citations=[CIT_BAUMEISTER, CIT_GROSS, CIT_TANGNEY],
    sig_lens=(
        "The Signature lens reads escalation as compound interest "
        "on an unpaid debt: every skipped payment adds penalties, "
        "and the balance outgrows the original loan. The Signature "
        "method treats the staircase as a payment schedule in "
        "reverse - the way down is the way up, walked backward: "
        "flood to weight to ache to tug to closed, one honest "
        "payment per step. His warning on the exits: withdrawal "
        "is the debt moved offshore, hardening is the debt "
        "forgiven by fraud - only payment closes the books. "
        "Clearly labeled Signature-made, never presented as "
        "authentic public record."),
),
# ------------------------------------------------- 26-28: healthy expression
dict(
    key="guilt_healthy_expression", name="Healthy Expression: Saying It, Showing It, and Channeling It Well",
    group="Advanced", ladder_rank=10, ladder_tier="advanced",
    description=(
        "Healthy expression of guilt is the repair beat executed "
        "well, and it has a shape. Saying it: the apology that "
        "works names the specific act ('I missed your call and I "
        "said I would call'), accepts responsibility without "
        "hedging ('it was my fault, not the traffic'), "
        "acknowledges the impact ('I know that left you waiting'), "
        "and offers a concrete repair ('I will call every Sunday; "
        "I have set the reminder'). What it does not do: grovel, "
        "repeat itself into the ground, demand instant forgiveness, "
        "or smuggle in excuses. Showing it: letting the feeling be "
        "visible in proportion - the lowered eyes, the serious "
        "tone - without performing it; honesty reads in the "
        "willingness to be uncomfortable, not in theatrics. "
        "Channeling it: converting the repair urge into changed "
        "behavior - the system fixed so the breach cannot recur, "
        "the habit built, the standard clarified for next time. "
        "The deeper healthy move is the attribution audit: before "
        "the big apology, check honestly whether the responsibility "
        "is really yours and in what share - healthy guilt repairs "
        "real breaches and releases false ones. And the final "
        "healthy move is proportion: the repair matches the breach "
        "- a missed call gets a call and a system, not a month of "
        "self-punishment; a serious harm gets sustained amends, not "
        "a quick 'sorry.' Healthy expression closes the account: "
        "after it, the replay loop has nothing to replay, because "
        "the story now ends with the repair."),
    how_it_works=(
        "Healthy expression works because it completes every open "
        "step of the guilt sequence. Naming the act specifically "
        "stops the replay loop's vagueness - the mind cannot loop "
        "on 'the thing' once 'the thing' has a name and a date. "
        "Accepting responsibility without hedging settles the "
        "attribution step instead of leaving it to cycle. "
        "Acknowledging impact addresses the interpersonal half: "
        "the harmed person's experience is entered into the "
        "record, which is what the relationship needed. Concrete "
        "repair gives the repair urge its proper object - action, "
        "not suffering. Changed behavior prevents recurrence, "
        "which is the only thing that stops the same guilt from "
        "being re-earned. The attribution audit prevents the "
        "whole machinery from running on false breaches: "
        "releasing what was never owed is as healthy as repairing "
        "what was. Proportion prevents the two classic errors - "
        "the shrug and the self-flagellation - by matching the "
        "payment to the debt. The record describes the pattern; "
        "it offers general educational guidance, not advice for "
        "any real person's situation."),
    key_points=[
        "The working apology: name the act, accept responsibility, acknowledge impact, offer concrete repair.",
        "Show the feeling in proportion - honesty reads in willingness to be uncomfortable, not theatrics.",
        "Channel the repair urge into changed behavior so the breach cannot recur.",
        "Audit the attribution first: repair real breaches, release false ones.",
        "Proportion the repair to the breach: match the payment to the debt.",
    ],
    requirements=[
        "Give the four-part apology structure with an example",
        "Cover saying, showing, and channeling as three modes",
        "Include the attribution audit and the proportion rule",
    ],
    standards=["Apology and reconciliation literature; Baumeister reparative behavior findings"],
    citations=[CIT_BAUMEISTER, CIT_TANGNEY, CIT_GROSS],
    sig_lens=(
        "The Signature lens reads healthy expression as the ledger "
        "properly closed: entry named, amount agreed, payment made, "
        "page turned. The Signature method has a closing ceremony - "
        "speak the entry plainly, pay it concretely, change the "
        "system that created it, then close the book and mean it. "
        "His measure of a closed account: you can recall the entry "
        "without re-feeling the debt. The lesson stays; the weight "
        "goes. Clearly labeled Signature-made, never presented as "
        "authentic public record."),
),
dict(
    key="guilt_unhealthy_expression", name="Unhealthy Expression: Bottling It Up or Exploding - What Each Costs",
    group="Advanced", ladder_rank=10, ladder_tier="advanced",
    description=(
        "Guilt goes wrong in two classic directions, and both are "
        "expensive. Bottling it up: the breach is never named, the "
        "apology never made, the repair never attempted. The costs "
        "compound quietly - the replay loop runs unchecked, sleep "
        "and appetite degrade, irritability leaks onto innocent "
        "parties, and the relationship carries an invisible crack "
        "that widens with every avoided conversation. Bottled guilt "
        "also ferments: months later it erupts over something "
        "trivial, bewildering everyone, because the pressure was "
        "never about the trivial thing. The bottler's deeper cost "
        "is self-knowledge: each suppressed breach teaches the "
        "system that breaches have no consequences, which makes "
        "the next breach easier. Exploding: the opposite failure - "
        "the guilt discharged all at once in a flood of "
        "confession, self-attack, or dramatic amends. The costs "
        "are different but real: the harmed person is forced into "
        "the role of comforter ('no, no, it's fine'), which "
        "reverses the repair direction; the grand gesture "
        "substitutes for sustained change; the self-attack "
        "('I'm the worst') fishing for contradiction is "
        "manipulation wearing remorse's clothes. Exploded guilt "
        "also burns out the repair urge in one blaze, leaving "
        "nothing for the long work. Between the two failures sits "
        "the third unhealthy pattern: weaponized guilt - using "
        "one's own guilt to control others ('after all I've done, "
        "how could you'), or cultivating guilt in others as "
        "leverage. The common price of all three: the account "
        "never actually closes, so the feeling keeps charging "
        "interest."),
    how_it_works=(
        "Bottling fails because suppression does not complete any "
        "step of the guilt sequence - the attribution stays "
        "unexamined, the repair beat never fires, and the "
        "associative trace stays armed for every cue. Research on "
        "thought suppression shows the rebound effect clearly: "
        "the suppressed content returns more frequently, which is "
        "why bottled guilt erupts over trivial triggers. Exploding "
        "fails differently: the flood discharges arousal without "
        "executing repair - confession without a plan, amends "
        "without proportion, self-attack without change. The "
        "harmed person's forced comforting is a role reversal "
        "that adds a second breach (now they owe comfort) to the "
        "first. Weaponized guilt corrupts the signal entirely: "
        "the feeling becomes a tool, which teaches everyone "
        "involved to distrust it - including the person wielding "
        "it, whose own future guilt signals lose credibility. All "
        "three share one mechanism of failure: the sequence is "
        "interrupted or misdirected before the repair beat "
        "completes, so the system keeps the account open and "
        "keeps charging."),
    key_points=[
        "Bottling: never named, never repaired; costs compound as rumination, leakage, and eventual eruption.",
        "Suppression rebounds: bottled guilt erupts over trivial triggers months later.",
        "Exploding: flood of confession or grand gesture discharges arousal without executing real repair.",
        "Exploded guilt forces the harmed person into comforting - a role reversal that adds a second breach.",
        "Weaponized guilt corrupts the signal; all three failures leave the account open and charging interest.",
    ],
    requirements=[
        "Describe bottling and exploding with their distinct costs",
        "Explain the suppression rebound and the role-reversal effect",
        "Cover weaponized guilt as the third pattern",
    ],
    standards=["Thought-suppression rebound literature; Gross on suppression costs; Baumeister on guilt dynamics"],
    citations=[CIT_GROSS, CIT_BAUMEISTER, CIT_TANGNEY],
    sig_lens=(
        "The Signature lens reads the unhealthy patterns as three "
        "ways of cooking the books: bottling hides the ledger in "
        "a drawer, exploding sets the ledger on fire for show, "
        "weaponizing forges entries in other people's books. The "
        "Signature method allows only one handling of a debt: open "
        "the book, read the entry, pay it. His warning: a hidden "
        "ledger still accrues interest, a burned ledger still has "
        "a creditor, and a forged ledger destroys the forger's "
        "credit first. Clearly labeled Signature-made, never "
        "presented as authentic public record."),
),
dict(
    key="guilt_everyday_practices", name="Everyday Practices: Small Habits That Keep Guilt in Balance",
    group="Advanced", ladder_rank=10, ladder_tier="advanced",
    description=(
        "Guilt stays in balance through small, unglamorous habits "
        "- not through grand resolutions. The prompt-repair habit: "
        "a standing rule to address small breaches within the day "
        "- the quick text, the brief apology, the fixed mistake - "
        "before the replay loop can build them into architecture. "
        "The ledger habit: a brief end-of-day review - what did I "
        "promise, what did I break, what is still open - written "
        "down, because written accounts do not loop the way mental "
        "ones do. The attribution-check habit: when guilt fires, "
        "one honest question before the spiral - 'what share of "
        "this is actually mine?' - asked in writing, answered with "
        "evidence. The standard-clarity habit: knowing your actual "
        "rules - writing down the five standards you truly hold - "
        "so the feeling cannot draft new rules retroactively in "
        "the dark. The maintenance habit: sleep, meals, movement "
        "- the operating budget the audit needs, protected "
        "especially during heavy weeks. The repair-system habit: "
        "when a breach recurs, fix the system not just the "
        "instance - the reminder set, the process changed, the "
        "conversation had about the pattern. The release habit: a "
        "practice for closed accounts - once repair is complete "
        "and proportionate, the entry is marked closed and the "
        "replay is met with 'settled' rather than re-litigation. "
        "None of these are dramatic; that is the point. Guilt is "
        "a daily bookkeeping emotion, and daily bookkeeping is "
        "done in small entries, not in annual crises."),
    how_it_works=(
        "Each practice targets a specific failure point in the "
        "guilt sequence. Prompt repair closes the sequence before "
        "the replay loop can compound - speed matters because "
        "every unfixed cycle adds retrieved breaches. The written "
        "ledger externalizes working memory: the loop persists "
        "partly because the mind is trying not to forget the open "
        "account, and paper relieves it of that job. The "
        "attribution check interrupts the most error-prone step "
        "before it can inflate. Standard clarity prevents the "
        "midnight drafting of impossible rules - many guilt "
        "spirals run on standards the person would not endorse in "
        "daylight. Maintenance protects the resources regulation "
        "needs. System-fixing addresses recurrence at its source: "
        "the same breach repeated is a process failure, not a "
        "character failure, and processes can be redesigned. The "
        "release practice trains the discrimination between open "
        "and closed accounts - without it, settled entries keep "
        "getting re-audited. Together the habits form a complete "
        "operating system for the emotion: fast intake, honest "
        "audit, proportionate payment, clean close. The record "
        "offers general educational practices, not personal advice."),
    key_points=[
        "Prompt repair: address small breaches within the day, before the loop builds.",
        "Written ledger: externalize open accounts so the mind stops looping to remember them.",
        "Attribution check: 'what share is actually mine?' - asked in writing, answered with evidence.",
        "Standard clarity: know your real rules so midnight cannot draft impossible ones.",
        "System-fixing for recurrences, maintenance for resources, release practice for closed accounts.",
    ],
    requirements=[
        "Describe at least seven concrete daily practices",
        "Map each practice to the sequence failure point it targets",
        "Frame as general educational habits, not personal advice",
    ],
    standards=["Implementation-intention and habit literature; Gross emotion-regulation strategies"],
    citations=[CIT_GROSS, CIT_BAUMEISTER],
    sig_lens=(
        "The Signature lens reads the practices as the ledger's "
        "daily routine: post promptly, audit honestly, pay "
        "proportionately, close cleanly. The Signature method "
        "treats bookkeeping as a craft - the master accountant is "
        "not the one with no debts but the one with no stale "
        "entries. His daily close: every account either paid, "
        "scheduled, or released - nothing left to loop at 2 a.m. "
        "Clearly labeled Signature-made, never presented as "
        "authentic public record."),
),
# ------------------------------------------------- 29-31: recognizing in others
dict(
    key="guilt_reading_others", name="Reading Guilt in Others: Face, Body, Voice, and Behavior Cues",
    group="Advanced", ladder_rank=10, ladder_tier="advanced",
    description=(
        "Reading guilt in another person means assembling a "
        "cluster, never trusting a single sign. The face: gaze "
        "that drops or slides away when the topic lands, lids "
        "lowered, the inner-brow lift of worry, lips pressed or "
        "briefly bitten - the shrinking program running on the "
        "features. The body: the slight forward fold, shoulders "
        "rounding, the person seeming physically smaller than a "
        "moment before; hands finding work - wringing, covering "
        "the mouth, rubbing the forehead. The voice: quieter, "
        "with swallows and throat-clearing before the difficult "
        "sentence; speech that over-explains or hedges; the "
        "repeated 'are you mad at me' fishing for reassurance. "
        "The behavior: sudden helpfulness disproportionate to the "
        "situation, the preemptive confession blurted before "
        "being asked, avoidance of the person or the place, "
        "nervous laughter at the wrong moment. Timing is the "
        "master cue: the cluster means the most when it arrives "
        "with the topic - the gaze drops exactly when the missed "
        "deadline is mentioned, the over-explaining starts "
        "exactly at the question about the evening. Context is "
        "the second master cue: the same signs mean little "
        "without a plausible breach in the picture. And the "
        "ethical frame is non-negotiable: these cues suggest "
        "where a caring conversation might go; they never prove "
        "anything, never license accusation, and never justify "
        "treating the person as convicted. The skilled reader "
        "uses the cluster to open a door - 'you seem weighed "
        "down; is something on your mind?' - not to deliver a "
        "verdict."),
    how_it_works=(
        "The cluster works because guilt's appeasement program "
        "produces correlated outputs across channels - face, "
        "body, voice, and behavior all serve the same social "
        "goal of signaling no further harm and seeking "
        "restored goodwill. No single channel is reliable alone: "
        "gaze aversion also signals shyness, over-explaining "
        "also signals anxiety, helpfulness also signals "
        "kindness. The diagnostic power - such as it is - comes "
        "from convergence: multiple channels shifting together, "
        "time-locked to a topic, in a context containing a "
        "plausible breach. This is basic signal-detection logic: "
        "each cue is weak evidence, but weak evidence "
        "multiplies when the cues are independent. The timing "
        "cue works because the appraisal re-fires on the topic, "
        "releasing the display fresh. The ethical constraint is "
        "not politeness but accuracy: base rates of these "
        "behaviors are high in innocent people too, so "
        "accusation from cues alone is mostly error. The "
        "record teaches the cluster for understanding and "
        "fiction, and for opening caring conversations - never "
        "for judging real people."),
    key_points=[
        "Read a cluster across face, body, voice, and behavior - never a single sign.",
        "Timing is the master cue: the cluster arriving time-locked to a topic.",
        "Context is the second master cue: no plausible breach, no reading.",
        "Each cue is weak alone; convergence across channels is what carries weight.",
        "The cues open a caring conversation; they never prove anything or license accusation.",
    ],
    requirements=[
        "Cover all four channels with concrete cues",
        "Explain timing and context as the master cues",
        "State the ethical constraint prominently",
    ],
    standards=["Signal-detection logic in nonverbal research; Ekman on leakage and context"],
    citations=[CIT_EKMAN, CIT_KELTNER, CIT_TANGNEY],
    sig_lens=(
        "The Signature lens reads the cluster as the ledger "
        "showing through the accountant's coat: no single page "
        "visible, but the bulk of the book unmistakable. The "
        "Signature method trains the reader in restraint - the "
        "best auditor never announces the audit. His rule for "
        "reading others: the cluster is an invitation to ask, "
        "never a verdict to deliver. Clearly labeled "
        "Signature-made, never presented as authentic public "
        "record."),
),
dict(
    key="guilt_supportive_responses", name="What to Say and Do When Someone Near You Feels Guilty",
    group="Advanced", ladder_rank=10, ladder_tier="advanced",
    description=(
        "When someone near you is carrying guilt, the helpful "
        "responses follow the shape of the feeling. Listen first: "
        "let the account be told without interruption, without "
        "the face that says 'here we go again' - the telling is "
        "the repair urge seeking an exit, and blocking it bottles "
        "the feeling. Acknowledge without judging: 'I can see "
        "this is weighing on you' names the feeling without "
        "endorsing or dismissing the verdict - it keeps the "
        "attribution step open for honest audit instead of "
        "slamming it shut with premature absolution ('don't be "
        "silly, it was nothing') or premature condemnation. Ask "
        "the repair question: 'what would make this right?' or "
        "'what do you want to do about it?' - this aims the "
        "person at the repair beat, which is the only exit that "
        "closes the account. Offer proportion, gently: if the "
        "self-punishment is clearly oversized, say so plainly - "
        "'you missed a call; you don't need to miss sleep over "
        "it' - not to absolve but to calibrate. Do not absolve "
        "on their behalf: 'I forgive you' when you are not the "
        "harmed party is empty currency, and even when you are, "
        "instant forgiveness can short-circuit the repair the "
        "person needs to make. Stay for the long repair: the "
        "most supportive thing is often just not withdrawing - "
        "remaining present while the person does the slow work. "
        "And know the boundary: you can support the repair, but "
        "you cannot perform it - the account is theirs to close, "
        "and taking it over teaches dependence, not resolution."),
    how_it_works=(
        "Supportive responses work by assisting the guilt "
        "sequence rather than replacing it. Listening without "
        "interruption lets the confession beat complete - "
        "unspoken guilt keeps the replay loop running because "
        "the account has never been entered anywhere outside "
        "the mind. Non-judgmental acknowledgment keeps the "
        "attribution step honest: premature absolution corrupts "
        "the audit (the breach gets filed as nothing), while "
        "premature condemnation inflates it. The repair question "
        "is the key intervention because it redirects energy "
        "from rumination to action - from the loop to the beat "
        "that closes it. Proportion-calibration addresses the "
        "most common distortion, the oversized self-punishment, "
        "without denying the real breach. Refusing false "
        "absolution protects the integrity of the sequence: a "
        "forgiven-without-repair account re-opens at the next "
        "cue. Presence during the long repair works through the "
        "interpersonal core of guilt - the feeling is about a "
        "relationship, and the relationship's steadiness is "
        "itself part of the settlement. The boundary matters "
        "because outsourced repair does not update the person's "
        "own ledger. The record offers general guidance for "
        "everyday situations, not advice for any real person's "
        "circumstances."),
    key_points=[
        "Listen first: let the account be told; the telling is the repair urge seeking exit.",
        "Acknowledge without judging: name the weight, neither absolve nor condemn prematurely.",
        "Ask the repair question: 'what would make this right?' aims at the only exit that closes.",
        "Calibrate proportion gently; refuse false absolution, including your own.",
        "Stay present for the long repair; support it but do not perform it for them.",
    ],
    requirements=[
        "Give concrete things to say for each of five responses",
        "Explain why premature absolution corrupts the audit",
        "State the boundary: support the repair, do not perform it",
    ],
    standards=["Social support and reconciliation literature; Baumeister on interpersonal repair"],
    citations=[CIT_BAUMEISTER, CIT_TANGNEY],
    sig_lens=(
        "The Signature lens reads the supporter as the "
        "accountant's assistant: you may hold the lamp, but you "
        "may not sign the books. The Signature method gives the "
        "supporter three tools - the open ear, the honest mirror, "
        "and the steady chair - and forbids the fourth, the pen. "
        "His rule: help them read their ledger; never write in "
        "it. Clearly labeled Signature-made, never presented as "
        "authentic public record."),
),
dict(
    key="guilt_mistakes_to_avoid", name="What Not to Do: The Mistakes That Make Guilt Worse",
    group="Advanced", ladder_rank=10, ladder_tier="advanced",
    description=(
        "The common mistakes around someone's guilt all share one "
        "trait: they interrupt the sequence instead of assisting "
        "it. Dismissing it - 'don't feel guilty, it was nothing' "
        "- invalidates the signal and teaches the person to "
        "distrust their own ledger; the feeling goes underground "
        "and returns as irritability or a bigger eruption later. "
        "Weaponizing it - bringing up the breach in unrelated "
        "arguments, keeping it as leverage - corrupts the "
        "relationship's books permanently; once guilt becomes a "
        "tool, every future apology is suspect. Rushing "
        "forgiveness - demanding or granting instant closure - "
        "short-circuits the repair the person needs to complete; "
        "the account closes on paper and re-opens at the next cue. "
        "Piling on - adding your own list of grievances to their "
        "confession - converts their repair moment into your "
        "trial of them, and the original breach never gets its "
        "hearing. Performing comfort instead of honesty - "
        "reassuring reflexively when the breach was real - "
        "leaves them alone with the accurate part of the feeling. "
        "Diagnosing them - labeling the person ('you're so "
        "guilt-ridden,' 'you have issues') - moves the judgment "
        "from the act to the self, which is the shame conversion "
        "the feeling least needs. Broadcasting it - telling "
        "others about their confession - destroys the safety the "
        "repair required. Each mistake is avoidable once named, "
        "and naming them is the record's whole job: the people "
        "around guilt do as much to shape its course as the "
        "person feeling it."),
    how_it_works=(
        "Each mistake maps to a specific sequence corruption. "
        "Dismissal corrupts the signal-validity step: the person "
        "learns the ledger lies, so future signals get ignored - "
        "including accurate ones. Weaponizing corrupts the "
        "interpersonal trust the repair needs: reconciliation "
        "requires the harmed party to be a safe creditor, and "
        "leverage destroys that safety. Rushed forgiveness "
        "corrupts the repair beat by declaring it complete "
        "before it is - the behavioral record shows the loop "
        "re-opens because the brain tracks completed actions, "
        "not declared states. Piling on corrupts the confession "
        "beat: the account being settled gets replaced mid- "
        "hearing by a different docket. Reflexive comfort "
        "corrupts the attribution audit by filing the breach as "
        "nothing when it was something. Diagnosing performs the "
        "guilt-to-shame conversion externally, relocating the "
        "verdict from act to self. Broadcasting corrupts the "
        "confession context - private repair requires private "
        "space, and its violation teaches the person never to "
        "open the books again. The record is educational: it "
        "names the failure modes so they can be avoided in "
        "everyday life."),
    key_points=[
        "Dismissing invalidates the signal; the feeling goes underground and returns worse.",
        "Weaponizing guilt as leverage corrupts the relationship's books permanently.",
        "Rushed forgiveness declares the repair complete before it is; the account re-opens.",
        "Piling on, reflexive comfort, diagnosing, and broadcasting each corrupt a different step.",
        "The people around guilt shape its course as much as the person feeling it.",
    ],
    requirements=[
        "Name and explain at least seven mistakes",
        "Map each mistake to the sequence step it corrupts",
        "Keep the framing educational, not accusatory",
    ],
    standards=["Reconciliation and social-support failure modes; Baumeister interpersonal findings"],
    citations=[CIT_BAUMEISTER, CIT_TANGNEY, CIT_GROSS],
    sig_lens=(
        "The Signature lens reads each mistake as tampering with "
        "someone else's ledger: dismissing tears out the page, "
        "weaponizing forges new entries, rushing stamps it paid "
        "before payment, piling on changes the subject of the "
        "audit, diagnosing condemns the accountant, broadcasting "
        "publishes private books. The Signature method bars all "
        "tampering with another's accounts - the only lawful "
        "touch is the lamp held steady while they read. Clearly "
        "labeled Signature-made, never presented as authentic "
        "public record."),
),
# ------------------------------------------------- 32-34: related emotions, mixes, simulation
dict(
    key="guilt_related_emotions", name="The Guilt Neighborhood: Nearest Neighbors, Opposites, and Close Cousins",
    group="Advanced", ladder_rank=10, ladder_tier="advanced",
    description=(
        "Guilt's neighborhood on the emotion map is crowded, and "
        "the residents are easy to confuse. Shame is the nearest "
        "neighbor - same street, adjacent house: both are "
        "self-conscious, both involve a breached standard, but "
        "guilt judges the act ('I did bad') while shame judges "
        "the self ('I am bad'), and the action urges oppose - "
        "repair versus hiding. Regret is the close cousin: it "
        "shares the backward look and the counterfactual thinking "
        "('if only'), but regret centers on outcomes and missed "
        "options rather than moral breach - you can regret a bad "
        "investment without guilt, and feel guilty about a "
        "harmless lie you do not regret telling. Remorse is guilt "
        "deepened: the same structure at higher weight, usually "
        "reserved for serious wrongs, carrying a stronger pledge "
        "of change. Embarrassment is the social cousin: it needs "
        "an audience and a gaffe, not a moral breach - tripping "
        "on stage embarrasses, lying to a friend guilts. "
        "Disappointment in oneself sits nearby but lacks the "
        "relational breach - you can disappoint yourself without "
        "owing anyone. The opposites: pride in one's conduct is "
        "the direct opposite - the ledger balanced and the self "
        "approved; shamelessness is the structural opposite - the "
        "audit function switched off entirely, breaches posted "
        "without entries. Telling the neighbors apart is not "
        "taxonomy for its own sake: each one prescribes a "
        "different response - regret wants better deciding next "
        "time, embarrassment wants the moment to pass, shame "
        "wants the self-verdict examined, and only guilt wants "
        "the specific repair."),
    how_it_works=(
        "The neighborhood is organized by two axes: judgment "
        "target (act versus self) and breach type (moral versus "
        "non-moral, relational versus private). Guilt occupies "
        "the act-targeted, moral-breach, relational quadrant - "
        "move the target to the self and you are in shame; move "
        "the breach to non-moral and you are in regret; remove "
        "the audience requirement's opposite - add an audience "
        "to a gaffe - and you are in embarrassment; deepen the "
        "weight and you are in remorse. The opposites sit across "
        "the map: pride is the same machinery returning a "
        "positive verdict, shamelessness is the machinery "
        "powered down. The axes explain the common confusions: "
        "guilt and shame blur because they share the "
        "self-evaluation machinery and usually co-fire; guilt "
        "and regret blur because both run counterfactuals; "
        "guilt and embarrassment blur because both trigger "
        "appeasement displays. The practical test for telling "
        "them apart is the prescription test: ask what would "
        "settle it - if the answer is a specific repair to a "
        "specific person, it is guilt's neighborhood; if the "
        "answer is different, you are visiting a neighbor."),
    key_points=[
        "Shame is the nearest neighbor: same machinery, but judges the self where guilt judges the act.",
        "Regret centers on outcomes and missed options, not moral breach.",
        "Remorse is guilt deepened; embarrassment needs an audience and a gaffe, not a breach.",
        "Opposites: pride (positive verdict) and shamelessness (audit switched off).",
        "The prescription test tells them apart: only guilt is settled by specific repair to a specific person.",
    ],
    requirements=[
        "Distinguish at least six neighbors with the act/self and breach-type axes",
        "Name the two opposites and place them on the map",
        "Give the prescription test as the practical discriminator",
    ],
    standards=["Tangney and Dearing taxonomy; Tracy and Robins self-conscious emotion model"],
    citations=[CIT_TANGNEY, CIT_TRACY, CIT_LEWIS],
    sig_lens=(
        "The Signature lens reads the neighborhood as the "
        "ledger's district: shame is the house next door with "
        "the same architecture, regret is the cousin across the "
        "street who keeps different books, remorse is the same "
        "house with heavier furniture, embarrassment is the "
        "neighbor who only cares what the street thinks, pride "
        "is the balanced account, shamelessness the abandoned "
        "building. The Signature method navigates by address: "
        "knock on the right door, and the right payment gets "
        "made. Clearly labeled Signature-made, never presented "
        "as authentic public record."),
),
dict(
    key="guilt_emotion_mixes", name="Guilt Blends: Mixes With Four Partner Emotions",
    group="Advanced", ladder_rank=10, ladder_tier="advanced",
    description=(
        "Guilt rarely arrives pure; it blends, and each blend has "
        "its own weather. Guilt plus shame - the classic dyad: the "
        "blend feels like being both the criminal and the crime, "
        "the repair urge fighting the hiding urge to a standstill; "
        "it looks like confession that keeps collapsing into "
        "withdrawal - the phone picked up and set down, the "
        "sentence started and swallowed. Guilt plus sadness - the "
        "remorseful dyad: the blend feels heavy and wet, the "
        "breach mourned like a loss; it looks like quiet tears, "
        "slow speech, the long gaze out the window - grief for "
        "what the act cost. Guilt plus fear - the dread dyad: the "
        "blend feels like waiting for a verdict, the breach plus "
        "the anticipated consequences; it looks like vigilance - "
        "checking the phone, rehearsing explanations, startling "
        "at notifications - the appeasement program running on "
        "high alert. Guilt plus anger at the self - the "
        "self-reproach dyad: the blend feels hot and corrosive, "
        "the standard enforced with fury; it looks like "
        "self-punishment, harsh self-talk spoken aloud, "
        "deliberately declined pleasures - the ledger balanced "
        "with suffering instead of repair. Each blend changes "
        "the prescription: the shame blend needs the verdicts "
        "separated before repair can start; the sadness blend "
        "needs the loss acknowledged alongside the amends; the "
        "fear blend needs the actual consequences faced rather "
        "than rehearsed; the anger blend needs the fury "
        "redirected from the self to the problem. Blends are the "
        "advanced level of the database because real episodes "
        "are almost always blends - pure guilt is the textbook "
        "case, and the blends are the field."),
    how_it_works=(
        "Blends form because guilt's appraisal shares machinery "
        "with its partners: the breached standard plus "
        "self-attribution creates the guilt core, and whichever "
        "other appraisal fires alongside contributes its own "
        "action tendency. Shame contributes the global-self "
        "verdict and the hiding urge - hence the standstill. "
        "Sadness contributes the loss appraisal ('something "
        "good is damaged') and the low-energy withdrawal - "
        "hence the mourning quality. Fear contributes the "
        "threat appraisal ('punishment or rejection is coming') "
        "and vigilance - hence the dread. Anger at the self "
        "contributes the violated-standard fury turned inward - "
        "hence the corrosive self-punishment. The blends are "
        "more than sums: the interaction creates properties "
        "neither partner has alone - the standstill of the "
        "shame blend, for instance, is not present in pure "
        "guilt or pure shame. This follows the classic dyad "
        "logic of emotion-mixing models: adjacent or co-firing "
        "appraisals produce emergent action tendencies. The "
        "prescription differences follow from the added "
        "tendency: each blend's extra urge must be addressed "
        "before, or alongside, the guilt core's repair urge. "
        "The record maps the four most common blends for "
        "education and depiction."),
    key_points=[
        "Guilt plus shame: repair urge versus hiding urge in standstill; separate the verdicts first.",
        "Guilt plus sadness: the breach mourned like a loss; acknowledge the loss alongside the amends.",
        "Guilt plus fear: breach plus anticipated consequences; face actual consequences rather than rehearsing.",
        "Guilt plus self-anger: corrosive self-punishment; redirect the fury from the self to the problem.",
        "Blends have emergent properties neither partner has alone; pure guilt is the textbook case, blends are the field.",
    ],
    requirements=[
        "Describe four blends with feel, look, and prescription for each",
        "Explain the emergent-property point with an example",
        "Ground blends in co-firing appraisals",
    ],
    standards=["Emotion-blend/dyad logic (Plutchik-style); Tangney on guilt-shame co-occurrence"],
    citations=[CIT_TANGNEY, CIT_LEWIS, CIT_LAZARUS],
    sig_lens=(
        "The Signature lens reads the blends as compound ledger "
        "entries: guilt-shame is a debt stapled to a condemnation, "
        "guilt-sadness a debt with a mourning attached, guilt-fear "
        "a debt with interest accruing daily, guilt-anger a debt "
        "being paid in the accountant's own blood. The Signature "
        "method un-staples before paying: separate the entries, "
        "settle each in its own currency - repair for the debt, "
        "examination for the condemnation, facing for the fear, "
        "redirection for the fury. Clearly labeled Signature-made, "
        "never presented as authentic public record."),
),
dict(
    key="guilt_full_simulation", name="Full Behavioral Simulation: One Guilt From Trigger to Resolution",
    group="Advanced", ladder_rank=10, ladder_tier="advanced",
    description=(
        "Scene one, the trigger - Tuesday, 6:40 p.m. Maya promised "
        "her sister she would pick up their mother from the "
        "clinic. A work crisis hits at 5:30; Maya handles it well "
        "and completely forgets the pickup until her sister's "
        "text at 6:40: 'where are you?? mom's been waiting 40 "
        "min.' The attribution completes before she finishes "
        "reading: her promise, her failure, no one else's. Scene "
        "two, the peak - 7:15 p.m. Driving over, the replay loop "
        "runs at full speed: the morning's promise replayed, the "
        "moment she chose work over the reminder, her mother's "
        "face imagined in the waiting room. Her chest is heavy, "
        "her stomach turns, her grip on the wheel is too tight. "
        "Shame arrives as a partner: 'I'm the unreliable one, "
        "always.' She rehearses the apology and hates every "
        "version. Scene three, the encounter - 7:50 p.m. Her "
        "mother is fine, reading a magazine, mildly annoyed; her "
        "sister is furious. Maya's gaze drops; her voice comes "
        "out quieter and faster than usual; she over-explains the "
        "work crisis in unnecessary detail. Her mother waves it "
        "off; her sister does not. The repair urge and the hiding "
        "urge fight visibly - Maya starts toward her sister, "
        "stops, looks at the floor. Scene four, the repair - "
        "Wednesday. Maya calls her sister and delivers the "
        "four-part apology: the specific act named, responsibility "
        "taken without hedging, the impact acknowledged ('I left "
        "you holding it and mom waiting'), and a concrete system "
        "('I put every family commitment in the shared calendar "
        "with two alarms; here, look'). She does not grovel, does "
        "not demand instant forgiveness, does not explain a fifth "
        "time. Scene five, the settling - the following week. "
        "The calendar system holds; the replay loop, finding the "
        "story now ends with repair, quiets; a faint aftershock "
        "on Sunday evening is met with 'settled' and passes. Her "
        "sister's anger thaws over the month as the changed "
        "behavior accumulates. The simulation shows the whole "
        "database in motion: standard, breach, attribution, peak, "
        "partner emotions, body signals, speech patterns, the "
        "four-part repair, the system fix, and the close. This "
        "is the archive's showcase: guilt described and simulated "
        "from trigger to resolution, for teaching - never a "
        "real person, never a diagnosis, only the pattern made "
        "visible."),
    how_it_works=(
        "The simulation is constructed by running the database's "
        "full model end to end. Scene one executes the four-beat "
        "appraisal: standard (the promise), transgression (the "
        "forgotten pickup), attribution (self, complete), repair "
        "urge (immediate). Scene two shows the peak mechanics: "
        "the replay loop at full speed, the body signals "
        "(breastbone weight, stomach churn, tight grip), the "
        "shame-partner recruitment and its standstill effect on "
        "the apology rehearsal. Scene three displays the "
        "expression and behavior records: gaze aversion, "
        "quieter-faster speech, over-explaining, the visible "
        "approach-avoidance conflict. Scene four executes the "
        "healthy-expression record verbatim: the four-part "
        "apology plus the system fix, with the groveling and "
        "absolution-fishing explicitly omitted. Scene five shows "
        "the time course closing: the loop quieting because the "
        "narrative now ends in repair, the aftershock met with "
        "recognition, the relationship settling through "
        "accumulated changed behavior rather than a single grand "
        "gesture. Every beat is traceable to a record in this "
        "database, which is what makes it a simulation rather "
        "than a story: it is the model, run."),
    key_points=[
        "Five scenes: trigger, peak, encounter, repair, settling - the full sequence run end to end.",
        "Every beat is traceable to a specific record in this database.",
        "The peak shows replay, body signals, shame recruitment, and the apology-rehearsal standstill.",
        "The repair executes the four-part apology plus a system fix - no groveling, no absolution-fishing.",
        "Settling comes from accumulated changed behavior, not a single grand gesture.",
    ],
    requirements=[
        "At least five scenes from trigger through resolution",
        "Show body signals, speech patterns, partner emotions, and the repair structure",
        "Map each scene to the database's model explicitly",
    ],
    standards=["Integrative simulation consistent with all cited frameworks in this database"],
    citations=[CIT_TANGNEY, CIT_BAUMEISTER, CIT_LAZARUS, CIT_GROSS],
    sig_lens=(
        "The Signature lens reads the simulation as a complete "
        "ledger cycle performed in five acts: the entry posted, "
        "the audit endured, the creditor faced, the payment made "
        "and the system mended, the book closed. The Signature "
        "method stages it as the masterclass because it contains "
        "every move in the repertoire - signal honored, verdicts "
        "separated, repair proportioned, system fixed, release "
        "granted. His closing line on the whole database: a clean "
        "ledger is not a life without debts; it is a life where "
        "every debt is read, paid, and released. Clearly labeled "
        "Signature-made, never presented as authentic public record."),
),
]

assert len(ENTRIES) == 34, "expected 34 entries, got %d" % len(ENTRIES)
_ranks = [e["ladder_rank"] for e in ENTRIES]
assert _ranks == sorted(_ranks), "entries not in ladder order"
assert all(1 <= r <= 10 for r in _ranks), "ladder_rank out of range"
