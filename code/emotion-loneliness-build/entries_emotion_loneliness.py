#!/usr/bin/env python3
"""Entries for the Loneliness Emotion databases (Manon's 16:15 orders, emotion series).

Creates two NEW databases, 34 ladder-ordered records each:

  emotion-loneliness            - The Loneliness Emotion Database
                                  (public-harvest: real, fact-checked psychology
                                  of loneliness - definition, emotion-family
                                  placement, intensity volumes, first-person
                                  simulation, body signals, facial expression,
                                  triggers, behavior, healthy expression,
                                  recognizing it in others, related emotions
                                  and mixes, full behavioral simulation;
                                  descriptive and educational only - never
                                  diagnosing real people, no therapeutic advice
                                  beyond general safe everyday guidance;
                                  standard references APA Dictionary of
                                  Psychology; Weiss 1973; Perlman and Peplau
                                  1981; Russell 1996 UCLA Loneliness Scale v3;
                                  Cacioppo and Patrick 2008; Hawkley and
                                  Cacioppo 2010; Baumeister and Leary 1995;
                                  Bowlby 1969; Plutchik 1980; Russell 1980;
                                  Lazarus 1991; Ekman and Friesen 1978;
                                  Darwin 1872)
  emotion-loneliness-signature  - The Loneliness Emotion Signature Database
                                  (his original Signature Loneliness Method:
                                  loneliness as the empty-chair signal of the
                                  system - the unlit panel on the board that
                                  says connection is wanted, a call signal the
                                  builder answers by building bridges back to
                                  people; src signature, titles suffixed
                                  " (Signature Edition)", never presented as
                                  authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
non-decreasing; ladder_tier foundations/compounded/advanced); the shard
index is written in ladder order so pages present simple -> compounded ->
complex.

ID prefixes: JAH-EMLN- (public) and JAH-EMLNS- (signature), verified free
in the manifest (zero EMLN hits across the databases) and in every shard
index file (zero JAH-EMLN hits across the data-1 shards).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_emotion_loneliness.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos. Demo outputs are
cross-checked against entry text during authoring.

Descriptive/educational only: this database describes and simulates the
emotion of loneliness. It never diagnoses real people, never labels any real
person with an emotional state, and offers only general, safe, everyday
guidance. No clinical language, no diagnostic labels.

No website references. No Facebook. No religious talk.
"""

SIG_LENS = ("The Signature read: loneliness is the empty-chair signal of the "
            "system. Where public psychology charts the ache, the Signature "
            "Loneliness Method treats the feeling as a direction arrow, not a "
            "verdict: the unlit panel on the board that says connection is "
            "wanted, a call signal the builder answers by building bridges "
            "back to people. Every loneliness record below carries the same "
            "public facts, reframed as his original Signature engineering of "
            "the feeling.")

SIG_TAIL = ("Signature original - his original Signature Loneliness Method: "
            "loneliness as the empty-chair signal of the system, the unlit "
            "panel on the board that says connection is wanted, a call signal "
            "the builder answers by building bridges back to people. Clearly "
            "labeled Signature-made, never presented as authentic public "
            "record.")

ENTRIES = [
    {
        "key": "definition",
        "name": "What Loneliness Is: A Plain-Language Definition",
        "group": "What the Emotion Is",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Loneliness is the felt gap between the connection a person wants "
            "and the connection they believe they have. It is not the same as "
            "being alone. A person can feel lonely in a crowded room full of "
            "friends and feel completely content on a quiet solo evening - "
            "the difference is not headcount, it is perceived closeness. "
            "Psychologists call this the discrepancy model: loneliness rises "
            "when the social world someone actually experiences falls short "
            "of the social world they want or need. That gap can be about "
            "companionship (no one to spend time with), intimacy (no one who "
            "truly knows them), or belonging (no group that feels like "
            "theirs). Researcher Robert Weiss divided it into two kinds that "
            "still organize the field today: emotional loneliness, the ache "
            "of missing a close bond, and social loneliness, the sense of "
            "not belonging to a circle or community. Both are signals, not "
            "verdicts - the feeling says something about a person's social "
            "appetite, not about their worth. The APA Dictionary of "
            "Psychology defines loneliness as an affective and cognitive "
            "discomfort or uneasiness from being or perceiving oneself to be "
            "alone or otherwise solitary. Notice the key word: perceiving. "
            "Loneliness lives in perception, which is exactly why it can be "
            "answered - perceptions change as connections are rebuilt."),
        "how_it_works": (
            "Loneliness works as a biological alarm for disconnection, in the "
            "same family as hunger and thirst. Psychologist John Cacioppo "
            "described it as an aversive signal that evolved to prompt "
            "reconnection: humans survived in groups, so a brain that punishes "
            "isolation and rewards reunion keeps the social animal social. "
            "The mechanism runs in a loop. First, a perceived gap opens "
            "between wanted and actual connection. Second, the alarm fires: "
            "attention narrows toward social threats, the person scans for "
            "signs of rejection and starts expecting coldness from others. "
            "Third, that defensive posture changes behavior - the person "
            "withholds, tests, or withdraws - which often produces the cool "
            "responses they feared, confirming the original gap. Researchers "
            "call this the lonely self-reinforcing loop. The cruel twist is "
            "that the alarm meant to pull people toward others can, when it "
            "rings too long, push them further away. Understanding the loop "
            "matters because each step is a place where the cycle can be "
            "interrupted: the gap can be named, the scanning can be noticed, "
            "and one small genuine contact can restart the reconnection the "
            "alarm was calling for."),
        "key_points": [
            "Loneliness is the perceived gap between wanted and actual connection - not a headcount of people nearby.",
            "Being alone and being lonely are different things; solitude can be full and a crowd can be empty.",
            "Weiss divided it into emotional loneliness (missing a close bond) and social loneliness (missing a circle).",
            "It works as a biological alarm for disconnection, evolved to push the social animal back toward others.",
            "Long bouts can self-reinforce: expecting rejection changes behavior in ways that invite cooler responses.",
        ],
        "requirements": [
            "A plain-language definition that an ordinary reader recognizes from their own life.",
            "Clear separation from neighboring states: solitude, isolation, and simply being alone.",
            "Coverage of both emotional and social loneliness so the definition does not only fit one kind.",
            "The signal function stated: what loneliness marks, what it motivates, what it is for.",
            "A stated educational boundary: description only, never diagnosis of any real person.",
        ],
        "standards": [
            "Definitions follow the APA Dictionary of Psychology loneliness entry: affective and cognitive discomfort from being or perceiving oneself to be alone.",
            "The discrepancy account follows Perlman and Peplau 1981: loneliness as the felt shortfall between desired and actual social relations.",
            "The two-kind account follows Weiss 1973: emotional loneliness (attachment figure) and social loneliness (network).",
        ],
        "citations": [
            "American Psychological Association. APA Dictionary of Psychology. Loneliness entry: affective and cognitive discomfort or uneasiness from being or perceiving oneself to be alone or otherwise solitary. Washington DC: APA.",
            "Perlman D, Peplau LA. Toward a social psychology of loneliness. In: Duck S, Gilmour R, eds. Personal Relationships in Disorder. London: Academic Press; 1981:31-56.",
            "Weiss RS. Loneliness: The Experience of Emotional and Social Isolation. Cambridge MA: MIT Press; 1973.",
        ],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "family",
        "name": "Where Loneliness Sits in the Emotion Family",
        "group": "What the Emotion Is",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Loneliness is a complex social emotion, not one of the six "
            "basic emotions Ekman identified (happiness, sadness, anger, "
            "fear, disgust, surprise). It belongs to the family of emotions "
            "built around belonging - the need to be bonded and included "
            "that Baumeister and Leary argued is as fundamental as hunger. "
            "Inside that family, loneliness is the alarm that sounds when "
            "the need goes unmet. Its nearest feeds are sadness (the weight "
            "of loss), fear (the dread of rejection or of staying alone), "
            "and shame (the false story that disconnection proves unworth). "
            "Attachment theory adds the deep root: Bowlby showed that human "
            "infants are wired to protest separation and settle on reunion, "
            "and that wiring never fully retires - adults still run a "
            "quieter version of the same program. On Plutchik's wheel, "
            "loneliness is not a primary spoke but a compound state sitting "
            "near sadness, grief, and pensiveness, leaning toward the "
            "territory between sadness and fear. On Russell's circumplex it "
            "lands in the unpleasant, low-to-mid activation quadrant: heavy, "
            "dragging, not the hot agitation of anger but the cold ache of "
            "absence. Placing loneliness this way matters because it tells "
            "the reader what kind of tool to reach for: it answers to "
            "connection the way sadness answers to comfort and fear answers "
            "to safety."),
        "how_it_works": (
            "Family placement works as a map for the feeling's causes and "
            "cures. Because loneliness is built from the belonging family "
            "rather than the threat family, its natural resolution is "
            "contact, not control - it does not end by managing danger the "
            "way fear does, it ends by restoring felt membership. The feeds "
            "interact: sadness supplies the heaviness, fear supplies the "
            "scanning for rejection, shame supplies the story that the "
            "person is the problem. That is why loneliness can masquerade as "
            "its neighbors: a person may report feeling sad when the core "
            "signal is social, or feel afraid when the real want is "
            "inclusion. Naming the family lets a reader sort the mixture. "
            "The belonging root also explains why loneliness is universal: "
            "attachment wiring is species equipment, not a personal defect. "
            "Studies across the lifespan find it in children, teenagers, "
            "adults, and the elderly alike - the object of the want changes "
            "(a friend, a partner, a circle, a purpose) but the alarm "
            "remains the same instrument, tuned to the distance between "
            "wanted and felt connection."),
        "key_points": [
            "Loneliness is a complex social emotion in the belonging family, not one of Ekman's basic six.",
            "It is fed by sadness, fear, and shame - which is why it can masquerade as any of them.",
            "Attachment theory gives it a deep root: separation protest and reunion relief, quieted but never retired in adults.",
            "On the circumplex it sits unpleasant and low-to-mid activation: the cold ache of absence, not hot agitation.",
            "The family tells the reader the remedy class: connection answers loneliness the way comfort answers sadness.",
        ],
        "requirements": [
            "Placement relative to the basic emotions with loneliness correctly outside the basic six.",
            "The belonging need stated as the family root, with the fundamental-motivation account referenced.",
            "The three feeder emotions named and their roles explained (heaviness, scanning, self-story).",
            "A map position given on both Plutchik's wheel and Russell's circumplex.",
            "An explicit non-pathology frame: universal wiring, not a personal defect.",
        ],
        "standards": [
            "The belonging-need account follows Baumeister and Leary 1995: the desire for interpersonal attachments as a fundamental human motivation.",
            "The attachment root follows Bowlby's Attachment and Loss: separation protest and reunion relief as lifelong wiring.",
            "Map positions follow Plutchik 1980 and Russell 1980 as descriptive tools, not diagnostic instruments.",
        ],
        "citations": [
            "Baumeister RF, Leary MR. The need to belong: desire for interpersonal attachments as a fundamental human motivation. Psychol Bull. 1995;117(3):497-529.",
            "Bowlby J. Attachment and Loss, Vol 1: Attachment. New York: Basic Books; 1969.",
            "Plutchik R. Emotion: A Psychoevolutionary Synthesis. New York: Harper & Row; 1980.",
        ],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "intensity",
        "name": "How Strong Loneliness Can Get: Mild, Moderate, Intense",
        "group": "What the Emotion Is",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Loneliness has a volume dial, and the same emotion at different "
            "settings feels like almost different weather. Mild loneliness "
            "is a passing twinge: an evening alone that feels a little "
            "hollow, a moment at a party where the conversation does not "
            "include you, a Sunday that drags. It arrives and leaves, more "
            "information than burden. Moderate loneliness settles in and "
            "stays for the day or the week: the apartment feels too quiet, "
            "meals taste duller eaten alone, the phone stays face-down "
            "because checking it only confirms the silence. Concentration "
            "thins, energy dips, and the person starts organizing life "
            "around avoiding the empty slots. Intense loneliness is a "
            "physical weight: a hollow ache in the chest, weekends that feel "
            "endless, the sense of watching life happen through glass. At "
            "this setting it colors everything - food, sleep, work, even "
            "memory, which obligingly serves up every past rejection. The "
            "dial usually moves with two inputs: how wide the perceived gap "
            "is, and how long it has been open. Brief, narrow gaps make "
            "twinges; wide, chronic gaps make the heavy weather. Knowing "
            "the dial matters because the response scales with the "
            "setting: a twinge needs a phone call, the heavy weather needs "
            "a rebuilt routine and steady company, sought gently and often."),
        "how_it_works": (
            "Intensity works through accumulation and attention. The "
            "perceived gap feeds the alarm, and time feeds the gap: the "
            "longer a person feels disconnected, the more their attention "
            "locks onto signs of rejection, which widens the perceived gap "
            "further. Cacioppo's research described this as hypervigilance "
            "for social threat - at high intensity the mind becomes a "
            "smoke detector that rings at steam. Physiologically, the "
            "dial shows up as mounting tension: shallow breathing, a "
            "knotted stomach, restless limbs at mild levels; a leaden "
            "heaviness, fatigue, and disrupted sleep as it climbs. The "
            "dial is not linear - moving from 7 to 9 on the ten-point "
            "felt scale costs far more than moving from 2 to 4, because "
            "the higher settings recruit the whole body and the memory "
            "system, which replays old exclusions as evidence. That is "
            "also why the same trigger can land differently on different "
            "days: a quiet evening after a connected week is a twinge, the "
            "same evening after a month of distance is the weight. Reading "
            "the dial correctly is the first skill of the whole database: "
            "everything after this assumes the reader can tell a twinge "
            "from the heavy weather."),
        "key_points": [
            "Mild loneliness is a passing twinge; moderate settles in for days; intense is a physical weight that colors everything.",
            "The dial moves with two inputs: how wide the perceived gap is, and how long it has stayed open.",
            "At high intensity the mind becomes a smoke detector that rings at steam - hypervigilance for social threat.",
            "The scale is not linear: the top end recruits body and memory, replaying old exclusions as evidence.",
            "The response scales with the setting: a twinge needs a call, the heavy weather needs a rebuilt routine.",
        ],
        "requirements": [
            "Three distinct intensity bands described as lived experience, not clinical grades.",
            "The two inputs to intensity named: gap width and gap duration.",
            "The non-linearity of the dial explained (top end costs more than the middle).",
            "Hypervigilance for social threat explained as the high-intensity mechanism.",
            "The response scaling with the setting stated as a practical rule.",
        ],
        "standards": [
            "The hypervigilance account follows Cacioppo and Patrick 2008 and Hawkley and Cacioppo 2010: loneliness heightens attention to social threat.",
            "Intensity-as-lived-experience follows the UCLA Loneliness Scale tradition of graded self-report, descriptive only.",
            "All intensity language is non-clinical: bands describe felt experience, never diagnostic categories.",
        ],
        "citations": [
            "Cacioppo JT, Patrick W. Loneliness: Human Nature and the Need for Social Connection. New York: Norton; 2008.",
            "Hawkley LC, Cacioppo JT. Loneliness matters: a theoretical and empirical review of consequences and mechanisms. Ann Behav Med. 2010;40(2):218-227.",
            "Russell DW. UCLA Loneliness Scale (Version 3): reliability, validity, and factor structure. J Pers Assess. 1996;66(1):20-40.",
        ],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "myths",
        "name": "Common Myths and Misunderstandings About Loneliness",
        "group": "What the Emotion Is",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Loneliness carries a cargo of myths, and the myths make the "
            "feeling harder to carry. Myth one: only unpopular people get "
            "lonely. False - research finds loneliness in married people, "
            "popular students, and crowded households; it tracks perceived "
            "closeness, not popularity. Myth two: loneliness is the same as "
            "being alone. False - solitude is chosen and often full; "
            "loneliness is unwanted distance, and the two can exist without "
            "each other entirely. Myth three: feeling lonely means "
            "something is wrong with you. False - it is species equipment, "
            "an alarm every social mammal carries; the presence of the "
            "feeling says the alarm works, not that the person is broken. "
            "Myth four: admitting loneliness will make it worse, so hide "
            "it. Backward - hiding it cuts off the very contact that "
            "answers it, while naming it plainly to one trusted person "
            "often halves its weight. Myth five: modern technology ended "
            "loneliness because everyone is connected. False - scrolling "
            "past other people's gatherings can widen the perceived gap; "
            "what answers the alarm is felt mutual closeness, not message "
            "volume. Myth six: loneliness is selfish when others care "
            "about you. False - the feeling measures perceived connection, "
            "and perception can lag behind reality; guilt about the feeling "
            "only adds a second weight. Clearing these myths matters "
            "because each one is a rule the mind enforces: name the false "
            "rule and the feeling gets lighter at once."),
        "how_it_works": (
            "Myths work as appraisal rules - hidden if-then programs that "
            "tell the mind what the feeling means. If loneliness means I "
            "am unlovable, then the alarm triggers shame alongside the "
            "ache, and shame says hide, which deepens the gap the alarm "
            "was reporting. Each myth adds a second emotion or a second "
            "rule on top of the original signal: the alone-myth adds "
            "confusion (why do I feel this in a crowd?), the "
            "brokenness-myth adds shame, the technology-myth adds "
            "hopelessness (I am connected and still feel this), the "
            "hide-it myth adds silence. Dismantling a myth works by "
            "substitution, not argument: the reader does not debate the "
            "mind, they replace the rule with a truer one - loneliness is "
            "an alarm, alarms are equipment, equipment is maintained not "
            "ashamed of. That is why this record sits early in the "
            "ladder: everything downstream - the body signals, the "
            "triggers, the healthy expression - reads differently once "
            "the myths stop taxing the feeling with false meanings."),
        "key_points": [
            "Popular, partnered, and surrounded people all get lonely - it tracks perceived closeness, not headcount.",
            "Being alone and being lonely are different; solitude can be full, loneliness is unwanted distance.",
            "Loneliness is an alarm every social mammal carries; the feeling proves the equipment works.",
            "Hiding it cuts off the contact that answers it; naming it plainly to one trusted person often halves it.",
            "Message volume does not answer the alarm - felt mutual closeness does.",
        ],
        "requirements": [
            "At least five distinct myths named and corrected, each with its false version and the truer version.",
            "The popularity myth corrected with the perceived-closeness finding.",
            "The hide-it myth corrected with the naming-it mechanism.",
            "The technology myth corrected with the felt-closeness distinction.",
            "The appraisal-rule mechanism explained: myths as if-then programs that add second emotions to the signal.",
        ],
        "standards": [
            "Myth corrections stay descriptive and educational; no claim treats a myth as a medical misconception.",
            "The perceived-closeness finding follows the discrepancy literature (Perlman and Peplau 1981).",
            "Naming-as-relief is framed as ordinary emotional expression, not a therapeutic technique.",
        ],
        "citations": [
            "Perlman D, Peplau LA. Toward a social psychology of loneliness. In: Duck S, Gilmour R, eds. Personal Relationships in Disorder. London: Academic Press; 1981:31-56.",
            "Cacioppo JT, Patrick W. Loneliness: Human Nature and the Need for Social Connection. New York: Norton; 2008.",
            "Qualter P et al. Loneliness across the life span. Perspect Psychol Sci. 2015;10(1):250-264.",
        ],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "first_person",
        "name": "Inside the Feeling: A First-Person Passage",
        "group": "How It Feels",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "It starts as a quietness that is not quiet. The apartment is "
            "still but the stillness hums - every small sound belongs to "
            "me alone and that is the whole problem. I make tea and the "
            "kettle's click feels loud because there is no other voice to "
            "share the kitchen with. My chest has a hollow place in it, "
            "not pain exactly, more like a room with the furniture "
            "missing. I scroll through messages and the names blur; there "
            "are people, I know there are people, but reaching feels like "
            "lifting something heavy, and what would I even say - hey, "
            "I am sitting here feeling the shape of your absence? "
            "Evening comes early in the windows. Someone laughs in the "
            "hallway and the laugh lands on me like a small stone; I am "
            "glad for them and hollowed by them at once. I catch myself "
            "rehearsing conversations that will never happen, whole "
            "friendships conducted in my head because the real ones feel "
            "too far to start. The strangest part is the double vision: "
            "I can see my life clearly - the job, the couch, the tea - "
            "and simultaneously see the life where someone is in the "
            "other chair, and the gap between the two is where I live "
            "right now. Nothing is wrong, exactly. That is what makes it "
            "hard to name. Everything is fine and everything is missing, "
            "and the missing has a weight I carry from room to room."),
        "how_it_works": (
            "This passage works by simulation: it hands the reader a "
            "controlled, second-hand experience of the feeling so the "
            "abstract definition gains a body. Each image is chosen to "
            "encode one documented feature of loneliness. The humming "
            "stillness and loud kettle encode hyper-awareness of the "
            "environment when social input is absent. The hollow chest "
            "encodes the somatic signature - the felt hollowness "
            "researchers find in self-reports. The heavy phone encodes "
            "the paradox of approach motivation: the alarm calls for "
            "contact while the defensive posture makes contact feel "
            "costly. The hallway laugh encodes social comparison pain, "
            "the rehearsed conversations encode compensatory fantasy, "
            "and the double vision encodes the discrepancy model "
            "directly - wanted life held against actual life, the gap "
            "itself becoming the address the person lives at. "
            "First-person simulation is an educational instrument, not a "
            "diagnosis: it teaches recognition of the feeling's texture "
            "so the reader can name it in themselves or spot it in "
            "others, which is the skill every later record in this "
            "database assumes."),
        "key_points": [
            "The passage renders the discrepancy model as lived texture: wanted life held against actual life.",
            "Every image encodes a documented feature - hyper-awareness, somatic hollowness, heavy-phone paradox.",
            "The double vision (fine and missing at once) is the signature phenomenology of the feeling.",
            "Simulation is an educational instrument: it teaches the feeling's texture for recognition, not diagnosis.",
            "The passage models naming without shame: nothing is wrong, exactly, and the missing has weight.",
        ],
        "requirements": [
            "A sustained first-person passage of at least ten sentences, present tense, concrete sensory detail.",
            "At least five documented features of loneliness encoded as images, not as lecture.",
            "The discrepancy model rendered experientially (the two lives, the gap as an address).",
            "The heavy-phone paradox shown: the alarm calls for contact while contact feels costly.",
            "An explicit framing: simulation for recognition, never diagnosis of the reader.",
        ],
        "standards": [
            "First-person simulation follows the educational-simulation canon of the emotion series: descriptive, bounded, non-clinical.",
            "Encoded features follow Cacioppo and Patrick 2008 (hypervigilance, approach-avoidance, social comparison).",
            "The passage contains no advice, no clinical terms, and no claim about the reader's own state.",
        ],
        "citations": [
            "Cacioppo JT, Patrick W. Loneliness: Human Nature and the Need for Social Connection. New York: Norton; 2008.",
            "Perlman D, Peplau LA. Toward a social psychology of loneliness. In: Duck S, Gilmour R, eds. Personal Relationships in Disorder. London: Academic Press; 1981:31-56.",
            "Weiss RS. Loneliness: The Experience of Emotional and Social Isolation. Cambridge MA: MIT Press; 1973.",
        ],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "time_course",
        "name": "How Loneliness Changes Over Time: Onset, Peak, Fading, Aftershock",
        "group": "How It Feels",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "Loneliness has a weather pattern, and it helps to know the "
            "forecast. Onset is usually quiet: a canceled plan that is not "
            "rescheduled, a friend's reply that comes slower than it used "
            "to, the first evening in a new apartment where the boxes are "
            "unpacked and the silence unpacks with them. The mind barely "
            "registers it at first - a twinge filed under tired or bored. "
            "Then the peak builds, often at the week's empty edges: Friday "
            "night when everyone else seems to have plans, Sunday "
            "afternoon when the hours pool and stagnate. At the peak the "
            "feeling stops being a thought and becomes a climate - the "
            "chest hollow, the rooms too big, the future narrowed to more "
            "of this. Fading rarely arrives as a revelation; it arrives "
            "as a Tuesday. One genuine conversation, a neighbor who "
            "remembers your name, a week with the calendar honestly full - "
            "and the hollow fills from the edges inward, almost "
            "unnoticed, until one evening you realize the apartment "
            "sounds normal again. The aftershock is the part people "
            "forget to expect: weeks later a song, a smell, an "
            "anniversary of the lonely stretch can summon a pale echo of "
            "the feeling for an hour. It is not a relapse, it is memory "
            "doing its job - the echo passes faster each time and proves "
            "the weather has genuinely changed."),
        "how_it_works": (
            "The time course works through the same loop that creates the "
            "feeling, run forward. Onset begins when the perceived gap "
            "opens faster than the person updates their expectations - "
            "the social map still says connected while the territory has "
            "shifted. The peak is the loop at full spin: hypervigilance "
            "finds rejection everywhere, withdrawal deepens the gap, the "
            "gap feeds the vigilance. Peaks cluster at the week's empty "
            "edges because contrast is the amplifier - loneliness is felt "
            "most sharply against the background of other people's "
            "visible togetherness, the Friday-night effect. Fading works "
            "by gap-closing: real contact updates the perceived "
            "connection faster than the mind's threat-scanning can "
            "re-widen it, especially when the contact is repeated and "
            "mutual. The aftershock is associative memory: the brain "
            "stored the lonely stretch with its sensory tags (the song, "
            "the season, the room), and a tag can re-evoke a diluted "
            "version of the state. Knowing the pattern defuses the peak's "
            "worst lie - that this is permanent. Weather passes; the "
            "record of past passings becomes evidence against the lie."),
        "key_points": [
            "Onset is quiet: a gap opens faster than expectations update, first filed under tired or bored.",
            "The peak clusters at the week's empty edges - contrast with others' visible togetherness is the amplifier.",
            "Fading arrives as a Tuesday: repeated genuine contact closes the perceived gap from the edges inward.",
            "The aftershock is associative memory, not relapse - sensory tags re-evoke a diluted echo that passes.",
            "Knowing the pattern defuses the peak's worst lie: that this weather is permanent.",
        ],
        "requirements": [
            "Four phases described as lived experience: onset, peak, fading, aftershock.",
            "The Friday-night/Sunday-afternoon contrast effect explained as the peak amplifier.",
            "The fading mechanism named: repeated mutual contact closing the perceived gap.",
            "The aftershock distinguished from relapse via associative memory.",
            "The permanence-lie named and countered with the record of past passings.",
        ],
        "standards": [
            "The time-course account stays descriptive; no phase is framed as a clinical stage.",
            "The contrast-amplifier follows the social-comparison literature in the loneliness field.",
            "The aftershock account follows standard associative-memory principles, educationally framed.",
        ],
        "citations": [
            "Cacioppo JT, Patrick W. Loneliness: Human Nature and the Need for Social Connection. New York: Norton; 2008.",
            "Qualter P et al. Loneliness across the life span. Perspect Psychol Sci. 2015;10(1):250-264.",
            "Weiss RS. Loneliness: The Experience of Emotional and Social Isolation. Cambridge MA: MIT Press; 1973.",
        ],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "low_vs_high",
        "name": "The Same Loneliness at Low and High Intensity: Two Snapshots",
        "group": "How It Feels",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "Low intensity, Tuesday, 7 pm. Maya finishes dinner alone and "
            "the quiet has a soft edge to it. She notices she has not "
            "really talked to anyone since lunch, and the noticing is "
            "mild - a small hollow behind the ribs, like hunger for "
            "conversation. She texts her sister a photo of the weird "
            "clouds, gets a laughing emoji back, and the hollow closes "
            "before the tea cools. The evening continues: a show, a book, "
            "bed. The loneliness was a twinge, a signal answered, gone "
            "by morning. High intensity, three months later, Sunday, 4 "
            "pm. Maya has not had a real conversation in days. The "
            "apartment is the same apartment but the rooms feel larger "
            "and the silence has texture, a pressure against the ears. "
            "The hollow is not behind the ribs anymore, it is the ribs - "
            "a broad ache that makes her press her palm to her sternum "
            "without thinking. Her sister's name is on the phone and "
            "Maya stares at it the way you stare at a door you are "
            "afraid is locked: what if she is busy, what if I am "
            "bothering her, what if she hears how I sound. She puts the "
            "phone down. She rehearses a call she does not make. The "
            "evening does not continue, it pools. Same person, same "
            "alarm, same apartment - but the dial has moved from a "
            "message that connection is wanted to a weather system that "
            "makes connection feel unreachable. The difference is not "
            "character and not circumstance alone; it is duration times "
            "the loop, the vigilance feeding the withdrawal feeding the "
            "gap."),
        "how_it_works": (
            "The two snapshots work as a controlled comparison: one "
            "variable - intensity - changed while the person, the place, "
            "and the alarm stay fixed. At low intensity the appraisal is "
            "clean: the gap is noticed, labeled correctly as a want for "
            "contact, and answered with a small bid that succeeds. The "
            "loop barely starts. At high intensity the same appraisal "
            "system is running corrupted inputs: hypervigilance has "
            "taught the mind to read neutral data (an unanswered text, a "
            "busy sister) as rejection, so the bid never launches. The "
            "snapshot pair also demonstrates the approach-avoidance "
            "paradox at its two settings: low dial, approach wins; high "
            "dial, avoidance wins, and avoidance is misread by the person "
            "as evidence that the gap is unbridgeable. Educationally, "
            "the pair trains the reader's dial-reading: the symptoms "
            "that distinguish weather from twinge are duration (days "
            "not hours), pervasiveness (every room, not one evening), "
            "and bid-failure (the phone stared at, not picked up). "
            "Recognizing the setting is what lets the later records' "
            "guidance scale correctly."),
        "key_points": [
            "Same person, same alarm, same apartment - the dial alone changes the entire weather.",
            "Low intensity: the gap is noticed, labeled, and answered with a small bid that succeeds.",
            "High intensity: hypervigilance corrupts the inputs, so the bid never launches.",
            "The tell-tale signs of the high setting: duration in days, pervasiveness across rooms, bid-failure.",
            "Dial-reading is the master skill: every later record's guidance scales with the setting.",
        ],
        "requirements": [
            "Two sustained vignettes, one low and one high intensity, same character and setting.",
            "The low snapshot shows the full signal-answered arc within an evening.",
            "The high snapshot shows the heavy-phone moment: the bid considered and not made.",
            "At least three distinguishing signs of the high setting named explicitly.",
            "The approach-avoidance paradox shown at both settings.",
        ],
        "standards": [
            "The vignettes are fictional teaching instruments; no real person is depicted or implied.",
            "The hypervigilance mechanism follows Cacioppo and Patrick 2008.",
            "No clinical language: the snapshots describe felt experience, never diagnostic states.",
        ],
        "citations": [
            "Cacioppo JT, Patrick W. Loneliness: Human Nature and the Need for Social Connection. New York: Norton; 2008.",
            "Hawkley LC, Cacioppo JT. Loneliness matters: a theoretical and empirical review of consequences and mechanisms. Ann Behav Med. 2010;40(2):218-227.",
            "Perlman D, Peplau LA. Toward a social psychology of loneliness. In: Duck S, Gilmour R, eds. Personal Relationships in Disorder. London: Academic Press; 1981:31-56.",
        ],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "loneliness_grief_blend",
        "name": "Loneliness Mixed with Grief: The Most Common Blend",
        "group": "How It Feels",
        "ladder_rank": 5,
        "ladder_tier": "foundations",
        "description": (
            "Grief is loneliness's most frequent companion, because the "
            "commonest cause of a sudden wide gap is a person-shaped hole. "
            "When someone dies, leaves, or a relationship ends, two "
            "alarms ring at once: grief mourns the one who is gone, "
            "loneliness reports the empty place they held. The blend has "
            "a distinctive texture. Grief comes in waves - a smell, a "
            "date, a song knocks the breath out, then recedes. Loneliness "
            "is the tide underneath the waves: the steady, daily "
            "awareness that the chair is empty, the phone will not ring "
            "with that voice, the stories of the day have nowhere "
            "appointed to go. Together they make the evenings double-"
            "heavy: the wave crashes and the tide is still there when it "
            "recedes. The blend also confuses the sufferer, because the "
            "two wants feel like one - I miss them becomes I am alone "
            "becomes nobody will ever know me like that, each true and "
            "each a different signal. Sorting them helps: grief is "
            "answered by mourning, by ritual, by letting the love have "
            "its long goodbye; loneliness is answered by connection, by "
            "new chairs filled slowly, by the deliberate rebuilding of "
            "the daily social fabric. One can grieve well and still be "
            "lonely, and one can be less lonely while grief still waves - "
            "they are housemates, not the same person."),
        "how_it_works": (
            "The blend works through two alarms sharing one trigger. A "
            "loss simultaneously removes an attachment figure (grief's "
            "object) and removes daily social input (loneliness's "
            "object). Weiss's distinction maps cleanly: bereavement is "
            "the textbook case of emotional loneliness, the ache of "
            "missing a close bond, arriving fused with grief's mourning. "
            "The two signals interact. Grief's waves temporarily widen "
            "the perceived gap - during an acute wave the person feels "
            "utterly alone even in a full room of mourners, because the "
            "specific bond is what the loneliness alarm is measuring. "
            "Conversely, the steady tide of loneliness can be misread as "
            "grief that is not healing, which alarms the sufferer "
            "further. The practical value of the sort is response-"
            "matching: mourning rituals do not fill the daily-contact "
            "gap, and new friendships do not perform the goodbye. "
            "People navigating the blend need both tracks running - "
            "space for the waves, and steady small rebuildings for the "
            "tide. The blend also explains a common stuck point: when "
            "grief eases but loneliness remains, the person may feel "
            "guilty for still aching, not realizing the remaining ache "
            "is a different alarm asking for a different answer."),
        "key_points": [
            "Grief mourns the one who is gone; loneliness reports the empty place they held - two alarms, one trigger.",
            "Grief comes in waves; loneliness is the steady tide underneath them.",
            "During a grief wave the person can feel utterly alone in a full room - the alarm measures the specific bond.",
            "Mourning rituals do not fill the daily-contact gap; new friendships do not perform the goodbye - both tracks are needed.",
            "When grief eases but loneliness remains, the leftover ache is a different alarm asking for a different answer.",
        ],
        "requirements": [
            "The wave/tide distinction rendered as the blend's signature texture.",
            "Weiss's emotional loneliness mapped to bereavement as the textbook case.",
            "The misreading named: loneliness mistaken for grief that is not healing.",
            "Response-matching stated: mourning answers grief, connection answers loneliness.",
            "The guilty-after-grief stuck point explained and normalized.",
        ],
        "standards": [
            "The blend is described educationally; no claim is made about grief stages or timelines.",
            "The Weiss mapping follows Weiss 1973 on emotional loneliness and attachment bonds.",
            "No therapeutic advice is offered; the record describes, it does not prescribe treatment.",
        ],
        "citations": [
            "Weiss RS. Loneliness: The Experience of Emotional and Social Isolation. Cambridge MA: MIT Press; 1973.",
            "Bowlby J. Attachment and Loss, Vol 3: Loss, Sadness and Depression. New York: Basic Books; 1980.",
            "Stroebe M, Schut H. The dual process model of coping with bereavement. Death Stud. 1999;23(3):197-224.",
        ],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "day_vignette",
        "name": "A Day in the Life: Loneliness Running Through an Ordinary Day",
        "group": "How It Feels",
        "ladder_rank": 5,
        "ladder_tier": "foundations",
        "description": (
            "6:40 am. Daniel wakes before the alarm and the first thought "
            "is the apartment's temperature of quiet - no shower running, "
            "no one else's morning sounds. He makes coffee for one; the "
            "second mug stays in the cabinet and he notices that he "
            "noticed. 8:15. The bus is full and he is anonymous in it, "
            "which usually feels fine but today feels like evidence. "
            "Everyone has earbuds in; he puts his in too, though nothing "
            "is playing. 12:30. Lunch at his desk because the break room "
            "means performing okay-ness for coworkers who have their "
            "own tables. He eats scrolling, and a photo of two old "
            "friends at a cabin stops his thumb. He likes it. He does "
            "not comment. 5:45. The commute home is the day's hinge: "
            "the city streams toward people while he streams toward the "
            "empty apartment, and the contrast does its work. 7:20. He "
            "heats dinner, eats standing at the counter, and the "
            "standing feels like a small confession. 9:00. The heavy-"
            "phone hour. He opens three conversations, types half a "
            "message in each, deletes them. Too needy, too random, too "
            "late. 10:30. In bed, the day replays with the loneliness "
            "as its narrator: the bus, the break room, the counter. "
            "11:15. A text arrives - his brother, a meme, nothing "
            "important. Daniel laughs out loud in the dark, and the "
            "laugh surprises him, and for a minute the apartment feels "
            "like a place someone lives instead of a place someone "
            "waits. He falls asleep before the feeling can file its "
            "objection. The day held maybe four minutes of actual "
            "connection, and they carried the other twenty-three hours "
            "and fifty-six minutes. That is the arithmetic of the "
            "feeling: it is not the absence of people that defines the "
            "day, it is the ratio of felt contact to felt distance - "
            "and four true minutes can outweigh a day of distance."),
        "how_it_works": (
            "The vignette works as a full-day field recording of the "
            "lonely loop in its ordinary clothes. Each hour encodes a "
            "mechanism: the morning quiet encodes baseline "
            "hyper-awareness; the bus encodes social comparison; the "
            "break-room avoidance encodes defensive withdrawal; the "
            "commute encodes contrast amplification; the counter dinner "
            "encodes the erosion of self-care rituals; the heavy-phone "
            "hour encodes bid-failure; the bedtime replay encodes "
            "ruminative review. The brother's meme is the record's "
            "thesis in miniature: the alarm is answered not by grand "
            "interventions but by small genuine contacts, and the "
            "response is disproportionate to the input - four minutes "
            "carrying a day. That disproportion is the hopeful core of "
            "the whole database: because loneliness measures perceived "
            "connection, small real perceptions move the needle "
            "faster than the sufferer expects. The vignette also models "
            "the day's hinge moments honestly - the commute, the "
            "evening - so readers learn where their own days are most "
            "vulnerable and where a small bid would land hardest."),
        "key_points": [
            "The vignette encodes a full day of mechanisms: comparison, withdrawal, contrast, bid-failure, rumination.",
            "The day's hinges are the commute and the evening - contrast with others' togetherness does its work there.",
            "Four minutes of genuine contact carried twenty-three hours of distance: small inputs move the needle.",
            "The heavy-phone hour shows bid-failure in the wild: three drafts, three deletions, three invented reasons.",
            "Because loneliness measures perceived connection, small real perceptions outweigh the sufferer's expectations.",
        ],
        "requirements": [
            "A dawn-to-night arc with at least eight timestamped beats.",
            "At least five documented mechanisms encoded as ordinary moments.",
            "The heavy-phone hour rendered with the specific self-talk that kills the bids.",
            "A genuine small contact that lands disproportionately, stated as the record's thesis.",
            "The closing arithmetic: the ratio of felt contact to felt distance.",
        ],
        "standards": [
            "The vignette is a fictional teaching instrument; no real person is depicted or implied.",
            "Encoded mechanisms follow Cacioppo and Patrick 2008 and the discrepancy literature.",
            "The thesis (small contacts carry the day) is framed as observed pattern, not a prescription.",
        ],
        "citations": [
            "Cacioppo JT, Patrick W. Loneliness: Human Nature and the Need for Social Connection. New York: Norton; 2008.",
            "Perlman D, Peplau LA. Toward a social psychology of loneliness. In: Duck S, Gilmour R, eds. Personal Relationships in Disorder. London: Academic Press; 1981:31-56.",
            "Qualter P et al. Loneliness across the life span. Perspect Psychol Sci. 2015;10(1):250-264.",
        ],
        "sig_lens": SIG_LENS,
    },
]
ENTRIES += [
    {
        "key": "body",
        "name": "What Happens in the Body: The Physical Signature of Loneliness",
        "group": "Body Signals",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Loneliness is felt in the body before it is named by the mind, "
            "and the body has a consistent signature. The chest carries the "
            "headline symptom: a hollow ache or a band of pressure behind "
            "the sternum, the physical rhyme of the emotional hollowness. "
            "Breathing goes shallow and high - short sips of air that never "
            "quite reach the bottom of the lungs, as if the body has "
            "forgotten how to sigh fully. The stomach knots or goes "
            "queasy; appetite swings either way, toward grazing without "
            "hunger or toward skipping meals that feel pointless to cook "
            "for one. Muscles hold a low-grade tension, especially the jaw, "
            "the shoulders, and the hands, which fidget with phones, cups, "
            "and sleeves. The skin runs cool - lonely people often report "
            "cold hands and feet, and researchers have found the body "
            "perceive lower temperature alongside social coldness in "
            "self-reports. Energy drains in a specific way: not the clean "
            "tiredness after work but a leaden, gray fatigue that rest "
            "does not fix, because the fatigue is not from effort, it is "
            "from the alarm running all day. None of this is imagination; "
            "the social alarm shares circuitry with physical pain "
            "processing, which is why rejection can literally ache and why "
            "the chest hollow feels so stubbornly real. Reading these "
            "signals correctly matters because the body reports the "
            "feeling before the mind admits it - the jaw was clenched an "
            "hour before the person knew they were lonely."),
        "how_it_works": (
            "The body signature works through the alarm's ancient wiring. "
            "The brain regions that register social disconnection overlap "
            "with those that register physical pain - the dorsal anterior "
            "cingulate cortex responds to both a burn and a cold shoulder - "
            "so the feeling arrives with genuine somatic weight rather "
            "than as a metaphor. Shallow breathing and muscle tension are "
            "the threat system's idling engine: the hypervigilance that "
            "scans for social threat keeps the body braced, and a braced "
            "body breathes high and clenches small muscles. The stomach "
            "effects follow the gut-brain axis under sustained unease. "
            "The cold hands and the temperature reports trace to the "
            "metaphor made flesh: social warmth and physical warmth share "
            "processing, and the lonely body behaves as if the room were "
            "colder. The gray fatigue is the cost of the alarm's "
            "uptime - threat-scanning is metabolically expensive, and a "
            "mind running it for weeks is a mind running a background "
            "program that never sleeps. This is why the body is the "
            "earliest instrument: it registers the gap while the conscious "
            "mind is still filing the feeling under tired, busy, or fine."),
        "key_points": [
            "The chest hollow and sternal pressure are the headline somatic signals - the physical rhyme of the emotional gap.",
            "Breathing goes shallow and high; the jaw, shoulders, and hands hold low-grade bracing tension.",
            "Social disconnection shares pain-processing circuitry with physical pain, so the ache is literally real.",
            "Cold hands and perceived chill trace to shared processing of social and physical warmth.",
            "The gray fatigue is the alarm's uptime cost: threat-scanning is metabolically expensive and rest does not clear it.",
        ],
        "requirements": [
            "Coverage of heart/chest, breath, muscles, stomach, skin/temperature, and energy in one pass.",
            "The pain-circuitry overlap stated as the reason the ache feels physical.",
            "The temperature effect described from self-report literature, not overstated.",
            "The gray fatigue distinguished from effort-tiredness via the alarm-uptime mechanism.",
            "The early-warning function stated: the body reports before the mind admits.",
        ],
        "standards": [
            "The pain-overlap account follows the social-pain neuroscience literature (dorsal anterior cingulate findings), described educationally.",
            "Temperature and embodiment effects follow the social-warmth embodiment literature, framed as reported patterns.",
            "All physiology is descriptive of felt experience; no medical claims or health advice is made.",
        ],
        "citations": [
            "Eisenberger NI, Lieberman MD, Williams KD. Does rejection hurt? An fMRI study of social exclusion. Science. 2003;302(5643):290-292.",
            "Hawkley LC, Cacioppo JT. Loneliness matters: a theoretical and empirical review of consequences and mechanisms. Ann Behav Med. 2010;40(2):218-227.",
            "Bargh JA, Shalev I. The substitutability of physical and social warmth in daily life. Emotion. 2012;12(1):154-162.",
        ],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "posture",
        "name": "Posture and Movement: How the Body Carries Loneliness",
        "group": "Body Signals",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "You can read loneliness in a silhouette. The shoulders roll "
            "forward and in, as if the chest is being guarded; the head "
            "tips slightly down and the gaze drops to the middle "
            "distance, the floor, or the phone - anywhere but the faces "
            "that might confirm the feeling. The arms cross or the hands "
            "find pockets, props, or the phone: self-hugging postures "
            "that substitute for the contact that is missing. Walking "
            "slows and shrinks - shorter steps, less arm swing, the body "
            "taking up minimum space, as if apologizing for its "
            "unaccompanied state. In groups the lonely person stations "
            "themselves at edges and doorways: near enough to watch, "
            "positioned for quiet exit, angled half-away from the "
            "circle. Gestures get smaller and fewer; the hands that "
            "would illustrate a story stay still, because there is no "
            "audience imagined for the story. The face follows the body "
            "down: the mouth rests in a neutral-to-down line, the eyes "
            "lose their scanning brightness and settle into a soft, "
            "unfocused watchfulness. None of this is performed - it is "
            "the threat system arranging the body for low visibility. "
            "The cruelty is that the posture is legible: closed bodies "
            "invite less approach, and less approach confirms the gap, "
            "another turn of the loop. Actors learn this silhouette "
            "first when they play the feeling, because the audience "
            "recognizes it before a word is spoken."),
        "how_it_works": (
            "Posture works as both signal and strategy. As a strategy, "
            "the closed silhouette is the defensive system minimizing "
            "exposure: small, still, edge-positioned bodies are harder "
            "to reject publicly, and the half-away angle pre-builds the "
            "exit the hypervigilant mind expects to need. Darwin noted "
            "the general principle in 1872 - dejected emotional states "
            "collapse the frame, the head bows, the body contracts - and "
            "loneliness follows the dejection pattern with its own "
            "social twist: the contraction is aimed at the social field, "
            "making the person literally smaller in the space where "
            "others might judge them. As a signal, the posture is "
            "honest and therefore costly: humans read closed postures "
            "as do-not-approach within seconds, so the protective "
            "arrangement reduces the approaches that would answer the "
            "alarm. This is the loop made visible - protection that "
            "prolongs the need for protection. The practical edge is "
            "that posture is partly voluntary: deliberately opening the "
            "frame - shoulders back, gaze up, phone away - does not "
            "cure the feeling, but it stops the body from actively "
            "broadcasting unavailability while the person works on the "
            "rest."),
        "key_points": [
            "The silhouette: shoulders in, head down, gaze dropped, arms crossed or pocketed, steps shortened.",
            "In groups the lonely person takes edges and doorways: near enough to watch, angled for quiet exit.",
            "The posture is the threat system minimizing exposure - protection arranged against expected rejection.",
            "The cruelty: closed bodies are read as do-not-approach, so protection prolongs the gap it guards.",
            "Posture is partly voluntary: opening the frame stops the body broadcasting unavailability.",
        ],
        "requirements": [
            "The full silhouette described: shoulders, head, gaze, arms, gait, group positioning.",
            "The edge-and-doorway positioning named as the characteristic group behavior.",
            "The Darwin dejection-collapse principle referenced as the root pattern.",
            "The signal-cost explained: closed posture reduces the approaches that would answer the alarm.",
            "The voluntary-opening edge stated honestly, without promising it cures the feeling.",
        ],
        "standards": [
            "The dejection-collapse pattern follows Darwin 1872 on the expression of dejected states.",
            "Posture-as-signal follows the nonverbal communication literature, described educationally.",
            "The voluntary-opening note is framed as behavioral observation, not therapeutic instruction.",
        ],
        "citations": [
            "Darwin C. The Expression of the Emotions in Man and Animals. London: John Murray; 1872.",
            "Mehrabian A. Nonverbal Communication. Chicago: Aldine-Atherton; 1972.",
            "Cacioppo JT, Patrick W. Loneliness: Human Nature and the Need for Social Connection. New York: Norton; 2008.",
        ],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "sleep_appetite",
        "name": "Sleep, Appetite, and Energy Under Loneliness",
        "group": "Body Signals",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Loneliness gets into the maintenance systems. Sleep is "
            "usually the first to show it: the lonely sleeper reports "
            "taking longer to fall asleep, waking more in the night, and "
            "rising unrefreshed even after full hours in bed. Researchers "
            "describe this as fragmented, non-restorative sleep - the "
            "threat system will not fully stand down, so the night is "
            "patrolled instead of rested. The pattern is worst on the "
            "empty evenings, when the day's contrast has done its work "
            "and the mind replays conversations that never happened. "
            "Appetite swings both ways and both are recognizable. Some "
            "lonely people graze through the evening - hand-to-mouth "
            "eating that fills the hours rather than hunger, the kitchen "
            "visited the way one visits a room hoping someone is in it. "
            "Others lose appetite entirely: cooking for one feels "
            "pointless, meals shrink to toast or nothing, and the body "
            "runs a quiet deficit that deepens the gray fatigue. Energy "
            "follows the worse of the two: poor sleep plus erratic fuel "
            "plus the alarm's uptime cost equals days that feel like "
            "wading. The person is not lazy - they are running three "
            "deficits at once and the deficits are invisible. Naming "
            "this triad matters because it breaks a misattribution: "
            "people blame their character for what is actually their "
            "maintenance system under strain, and character-blame feeds "
            "the shame that feeds the withdrawal."),
        "how_it_works": (
            "The triad works through the alarm's refusal to stand down. "
            "Sleep fragments because hypervigilance is a daytime program "
            "that leaks into the night: the mind that spent the day "
            "scanning for social threat does not switch off at lights-"
            "out, so sleep is light, broken, and unrefreshing. "
            "Researchers have measured this as poorer sleep efficiency "
            "and more micro-awakenings in lonelier sleepers, even when "
            "total time in bed matches. Appetite dysregulation follows "
            "two paths: the soothing path, where eating substitutes for "
            "the comfort of company and becomes timed to the empty "
            "evening hours; and the futility path, where the social "
            "meaning of meals (cooking for, eating with) collapses and "
            "food loses its occasion. Energy is the sum: fragmented "
            "sleep plus erratic fuel plus the metabolic cost of "
            "threat-scanning equals the leaden wading feeling. The "
            "practical read is sequencing - the triad is downstream of "
            "the gap, so it eases as the gap closes rather than by "
            "being attacked directly, though steady sleep hours and "
            "regular meals are the ordinary maintenance any strained "
            "system deserves."),
        "key_points": [
            "Sleep fragments first: longer to fall asleep, more night waking, unrefreshing even after full hours.",
            "The threat system will not stand down at lights-out, so the night is patrolled instead of rested.",
            "Appetite swings both ways: evening grazing that fills hours, or meals shrinking to toast from futility.",
            "Energy is the sum of three deficits - poor sleep, erratic fuel, alarm uptime - and the deficits are invisible.",
            "The triad is downstream of the gap: it eases as connection returns, and it is not a character flaw.",
        ],
        "requirements": [
            "Sleep, appetite, and energy each described with their loneliness-specific pattern.",
            "The fragmented non-restorative sleep pattern explained via nighttime hypervigilance leak.",
            "Both appetite directions described (grazing and futility-shrinkage) with their mechanisms.",
            "The triple-deficit energy account stated as a sum, not a mystery.",
            "The misattribution broken explicitly: maintenance strain, not character.",
        ],
        "standards": [
            "Sleep findings follow the loneliness-and-sleep literature (fragmentation, efficiency), described not prescribed.",
            "No medical claims are made; patterns are reported as documented self-report and measurement findings.",
            "The closing maintenance note is ordinary everyday guidance, not medical advice.",
        ],
        "citations": [
            "Hawkley LC, Preacher KJ, Cacioppo JT. Loneliness impairs daytime functioning but not sleep duration. Health Psychol. 2010;29(2):124-129.",
            "Cacioppo JT et al. Loneliness within a nomological net: an evolutionary perspective. J Res Pers. 2006;40(6):1054-1085.",
            "Hawkley LC, Cacioppo JT. Loneliness matters: a theoretical and empirical review of consequences and mechanisms. Ann Behav Med. 2010;40(2):218-227.",
        ],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "individual_diff",
        "name": "How Loneliness Differs Between People: No Two Alarms Alike",
        "group": "Body Signals",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The alarm is universal; the ringtone is personal. Temperament "
            "sets the baseline: highly sensitive people feel the gap "
            "sooner and louder, while others can go days solo before "
            "the twinge arrives - neither setting is better, they are "
            "different factory calibrations of the same instrument. "
            "Attachment history tunes it further: people raised with "
            "steady, responsive closeness tend to trust that gaps close, "
            "so their loneliness stays a signal; people raised with "
            "unpredictable closeness tend to read gaps as verdicts, so "
            "theirs arrives fused with shame. Introversion is widely "
            "misread here - introverts are not lonelier by nature, they "
            "simply need fewer, deeper contacts to feel connected, and "
            "their loneliness when it comes is about depth, not number. "
            "Age changes the object: teenagers ache for peer belonging, "
            "young adults for a circle in a new city, parents for adult "
            "conversation inside the beautiful isolation of caregiving, "
            "older adults for the daily contact that retirement and loss "
            "thin out. Culture sets the display rules: some cultures "
            "voice the ache openly, others treat it as private weather, "
            "and neither style predicts the feeling's strength. Even "
            "bodies differ - the chest-hollow person, the stomach-knot "
            "person, the restless-limbs person, the heavy-eyed person. "
            "The practical point is anti-template: there is no single "
            "correct way to feel lonely, so no one should grade their "
            "own feeling against someone else's description - including "
            "the descriptions in this database, which map the common "
            "territory, not your exact address."),
        "how_it_works": (
            "Differences work through calibration and context. The "
            "alarm's sensitivity is set partly by temperament - "
            "research on sensitivity and neuroticism finds louder "
            "affective responses to the same social shortfall - and "
            "partly by learned expectations from attachment history, "
            "which set the mind's prior on whether gaps close. The "
            "object of the want shifts with life stage because the "
            "social tasks shift: belonging to peers, building a "
            "network, maintaining intimacy under load, replacing "
            "thinned contacts. Culture operates on expression and "
            "interpretation rather than on the alarm itself: the gap "
            "is felt everywhere, but what it means (personal failing "
            "versus shared condition) and what may be said about it "
            "varies. Bodily differences follow individual somatic "
            "styles - where a person habitually carries stress is "
            "where loneliness will set up its local office. "
            "Understanding this variance protects the reader twice: "
            "it stops the false inference that a differently-shaped "
            "loneliness is not real loneliness, and it stops the "
            "comparison that turns someone else's easy sociability "
            "into evidence against oneself."),
        "key_points": [
            "Temperament sets the alarm's sensitivity; attachment history sets whether gaps read as signals or verdicts.",
            "Introverts are not lonelier by nature - their loneliness is about depth of contact, not number.",
            "The object of the want shifts with life stage: peers, circles, adult conversation, daily contact.",
            "Culture tunes expression and meaning, not the alarm itself - the gap is felt everywhere.",
            "No single correct shape exists: differently-shaped loneliness is still loneliness.",
        ],
        "requirements": [
            "At least five axes of difference covered: temperament, attachment, introversion, life stage, culture, plus bodily style.",
            "The introversion myth corrected explicitly.",
            "Life-stage objects of the want enumerated across at least four stages.",
            "The anti-template point stated: no grading one's feeling against others' descriptions.",
            "The database's own descriptions framed as common territory, not exact addresses.",
        ],
        "standards": [
            "Temperament and attachment accounts follow the personality and developmental literature, educationally framed.",
            "Life-span variation follows Qualter et al. 2015 on loneliness across the life span.",
            "All differences are descriptive; none is ranked as better or healthier.",
        ],
        "citations": [
            "Qualter P et al. Loneliness across the life span. Perspect Psychol Sci. 2015;10(1):250-264.",
            "Mikulincer M, Shaver PR. Attachment in Adulthood: Structure, Dynamics, and Change. New York: Guilford; 2007.",
            "Cacioppo JT, Patrick W. Loneliness: Human Nature and the Need for Social Connection. New York: Norton; 2008.",
        ],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "face",
        "name": "The Face of Loneliness: Eyes, Brows, Mouth, and Micro-Signs",
        "group": "Facial Expression",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Loneliness does not have a single famous face the way joy "
            "has the smile, but it has a recognizable composite, "
            "borrowed mostly from the sadness family with a watchful "
            "overlay. The eyes are the headline: gaze drops or drifts "
            "to the middle distance, the upper lids sit a fraction low, "
            "and the brightness that comes with social engagement dims "
            "to a soft, unfocused watchfulness. The inner corners of "
            "the brows lift - the AU1 inner-brow raise of the Facial "
            "Action Coding System, the same movement that marks sadness "
            "and the plea for comfort - often held at low intensity, "
            "a few millimeters that change the whole face. The mouth "
            "rests in a neutral line tipped downward at the corners, "
            "or presses into a thin, held line when the person is "
            "actively hiding the feeling. The micro-signs are where "
            "the truth leaks: a brief lip compression when someone "
            "asks how they are, a flicker of the gaze away at the "
            "moment of a warm remark, a half-second delay before the "
            "social smile arrives - and the smile, when it comes, "
            "stays in the mouth while the eyes keep their dim "
            "watchfulness. The cheeks and jaw carry the day's tension "
            "in a faint tightness. The overall read is not dramatic; "
            "it is the face of someone conserving something - energy, "
            "hope, or simply the effort of appearing fine."),
        "how_it_works": (
            "The face works as an honest billboard the person did not "
            "order. The brow raise (AU1) is driven by the same "
            "protest-and-plea circuitry that Bowlby described in "
            "separation: the infant's cry-face, quieted in the adult "
            "to a millimeter lift that still asks for comfort. The "
            "dimmed eyes follow attentional withdrawal - the "
            "hypervigilant mind is scanning the social field, not the "
            "person in front of it, so the gaze goes distant even "
            "mid-conversation. The mouth's pressed line is active "
            "suppression: the feeling is being held behind the teeth, "
            "and the orbicularis oris betrays the effort. The "
            "half-second smile delay is the most reliable tell, "
            "because genuine social smiles are fast and the "
            "performed one must be assembled - the assembly time "
            "shows. None of these are under full voluntary control, "
            "which is why the face is the record's honesty anchor: "
            "people can arrange their words and their posture, but "
            "the brow and the eyes file their own report. Reading "
            "this face in others is a kindness skill, not a "
            "detection trick - the point is to notice and draw "
            "nearer, never to announce what you see."),
        "key_points": [
            "The composite: dimmed downcast eyes, inner-brow lift (AU1), mouth neutral-to-down or pressed thin.",
            "The brow raise is the adult-quieted version of the separation cry-face - still asking for comfort.",
            "The most reliable tell is the half-second delay before the social smile, which stays mouth-only.",
            "Micro-leaks: lip compression on how-are-you, gaze flicker at warm remarks, faint jaw tightness.",
            "The face is the honesty anchor: words and posture can be arranged, the brow and eyes file their own report.",
        ],
        "requirements": [
            "Eyes, brows, mouth, and micro-signs each described with specific muscular detail.",
            "The AU1 inner-brow raise named and linked to the separation-plea circuitry.",
            "The smile-delay tell explained via assembly time of performed vs genuine smiles.",
            "At least three micro-signs named with their trigger moments.",
            "The kindness framing: notice to draw nearer, never to announce.",
        ],
        "standards": [
            "Facial-action language follows Ekman and Friesen 1978 (FACS), used descriptively not diagnostically.",
            "The separation-cry-face link follows Bowlby's attachment account of protest expressions.",
            "Reading others' faces is framed as a kindness skill, explicitly not a detection or labeling trick.",
        ],
        "citations": [
            "Ekman P, Friesen WV. Facial Action Coding System. Palo Alto: Consulting Psychologists Press; 1978.",
            "Darwin C. The Expression of the Emotions in Man and Animals. London: John Murray; 1872.",
            "Bowlby J. Attachment and Loss, Vol 1: Attachment. New York: Basic Books; 1969.",
        ],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "face_intensity",
        "name": "How the Expression Changes with Intensity",
        "group": "Facial Expression",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "At low intensity the face of loneliness is almost invisible "
            "- a good day with a thin spot in it. The eyes are normal "
            "brightness with a occasional drift, the brow rests flat, "
            "the mouth is neutral. The only tell is timing: the gaze "
            "goes distant for a breath at the mention of weekend plans, "
            "then returns. Friends would describe this face as fine, "
            "maybe a little tired. At moderate intensity the composite "
            "assembles and stays. The brow holds its millimeter lift "
            "through conversations, the eyes keep their dimmed "
            "watchfulness even while the mouth smiles, and the smile "
            "itself gets assembled a beat late. The face starts to "
            "look conserved - as if expression costs money and the "
            "budget is tight. Strangers read it as reserved or sad; "
            "people who know the person read it as off. At high "
            "intensity the mask work fails and the face goes either "
            "flat or fractured. Flat is the more common: features "
            "settled into stillness, eyes unfocused, mouth a line, the "
            "whole face like a house with the lights out - the person "
            "has stopped spending energy on appearing fine. Fractured "
            "is rarer and more visible: the brow lifts hard while the "
            "mouth forces cheer, the two halves of the face telling "
            "different stories, tears close enough to change the "
            "voice. The intensity scale reads in the eyes first, the "
            "mouth second, the brow third - and in the effort budget: "
            "how much of the face is still being managed, and how "
            "much has been surrendered to the weather."),
        "how_it_works": (
            "The intensity scale works through the economics of "
            "suppression. At low dial settings the feeling is brief "
            "and the face needs no management - the micro-drift is "
            "all that escapes. At moderate settings the person is "
            "actively managing the display: the smile is assembled, "
            "the brow is negotiated down, the eyes are the hardest "
            "to fake and so they carry the truest signal. Suppression "
            "has a metabolic cost, which is why the moderate face "
            "looks conserved - expression is literally being "
            "budgeted. At high settings the budget runs out. The "
            "flat face is suppression abandoned: the threat system "
            "has decided that appearing fine is not worth the spend, "
            "so the features settle to their unmodulated state, "
            "which reads as emptiness. The fractured face is "
            "suppression failing mid-attempt: the voluntary cheer "
            "and the involuntary plea fire simultaneously, and the "
            "observer sees both. This is why the read-order is eyes, "
            "mouth, brow: the eyes are least voluntary, the mouth "
            "most managed, and the gap between them is the dial."),
        "key_points": [
            "Low intensity is nearly invisible: one breath of distant gaze at weekend-plans talk, then back.",
            "Moderate assembles the composite and holds it: lifted brow, dimmed eyes, the beat-late smile.",
            "High goes flat (features surrendered, house with the lights out) or fractured (cheer and plea at once).",
            "Suppression has a metabolic cost - the moderate face looks conserved because expression is being budgeted.",
            "Read order is eyes, mouth, brow: the gap between the least and most voluntary features is the dial.",
        ],
        "requirements": [
            "Three intensity bands rendered as visible faces, not abstract grades.",
            "The conserved/budgeted metaphor tied explicitly to the metabolic cost of suppression.",
            "Both high-intensity outcomes described: flat and fractured, with their different mechanisms.",
            "The read-order rule stated: eyes first, mouth second, brow third.",
            "Observer perspectives included: what strangers read vs what intimates read at moderate intensity.",
        ],
        "standards": [
            "The suppression-cost account follows the emotion-regulation literature, described educationally.",
            "All face-reading is framed as descriptive pattern recognition, never as diagnosis of any person.",
            "The fractured-face description avoids clinical terms; it describes visible features only.",
        ],
        "citations": [
            "Ekman P, Friesen WV. Facial Action Coding System. Palo Alto: Consulting Psychologists Press; 1978.",
            "Gross JJ. Emotion regulation: affective, cognitive, and social consequences. Psychophysiology. 2002;39(3):281-291.",
            "Darwin C. The Expression of the Emotions in Man and Animals. London: John Murray; 1872.",
        ],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "hiding_faking",
        "name": "Hiding Loneliness and Faking Fine: What Leaks Through",
        "group": "Facial Expression",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Loneliness is one of the most-hidden feelings, because the "
            "myths say admitting it is confessing failure. So people "
            "perform fine, and the performance has a standard repertoire. "
            "The performed smile is the lead actor: mouth wide, eyes "
            "uninvolved, arriving a beat late and leaving a beat early. "
            "Over-talkativeness is the understudy - the lonely person "
            "fills every silence at the gathering, asking bright "
            "questions, laughing first and loudest, because silence "
            "might let the feeling show. Busyness is the costume: the "
            "calendar packed, the phone always in hand mid-scroll, the "
            "constant small errands that prove - to whom? - that the "
            "person is in demand. Deflection is the script: I'm fine "
            "lands a half-second too fast, how are you boomerangs every "
            "question back, and self-deprecating jokes do the feeling's "
            "confessing for it (someone has to laugh at my thrilling "
            "Friday night). What leaks anyway: the eyes keep their dim "
            "watchfulness inside the bright performance; the laugh "
            "arrives loud but the face resets to neutral the instant "
            "attention moves on; the phone gets checked in the middle "
            "of the fun; goodbyes land a little too hard, the hug held "
            "a breath too long. The deepest leak is temporal: the "
            "performance cannot be sustained, so the person leaves "
            "early, cancels next time, or goes quiet for days after - "
            "and the withdrawal is misread by others as disinterest, "
            "which is the loop's cruelest turn."),
        "how_it_works": (
            "Hiding works as impression management under the shame-tax. "
            "The myths (admitting loneliness equals failure) make the "
            "feeling socially expensive to show, so the person spends "
            "energy on a display of fine. Each tactic serves the "
            "display: the performed smile borrows joy's face, "
            "over-talkativeness borrows extraversion's soundtrack, "
            "busyness borrows importance's costume, deflection borrows "
            "politeness's script. The leaks happen because the display "
            "is assembled from voluntary muscles while the feeling "
            "lives partly in involuntary ones - the eyes, the brow, "
            "the timing. Ekman's work on leakage showed that "
            "suppressed affect escapes in brief, uncontrollable "
            "fragments, and loneliness follows the rule: the held hug, "
            "the phone check, the too-fast I'm fine are all fragments "
            "of the true state escaping the performance. The temporal "
            "leak is structural: impression management is expensive, "
            "so it can only run in bursts, and the recovery periods "
            "read as withdrawal. For the reader, the lesson is "
            "two-sided: your own performance is more transparent than "
            "it feels, and other people's brightness may be a "
            "repertoire too - which is a reason for gentleness, not "
            "suspicion."),
        "key_points": [
            "The hiding repertoire: performed smile, over-talkativeness, busyness-as-costume, deflection scripts.",
            "The myths make the feeling socially expensive to show, so energy goes into the display of fine.",
            "Leaks are involuntary fragments: dim eyes inside bright performance, the held-too-long goodbye, the phone check.",
            "The deepest leak is temporal: the performance runs in bursts, and recovery reads as withdrawal.",
            "Two-sided lesson: your performance is more transparent than it feels; others' brightness may be repertoire too.",
        ],
        "requirements": [
            "At least four hiding tactics named with their mechanism (what each borrows or proves).",
            "At least four specific leaks named with their moments.",
            "The shame-tax explained as the motive for hiding, linking back to the myths record.",
            "The temporal leak explained via the metabolic cost of impression management.",
            "The closing two-sided lesson: transparency of self, gentleness toward others.",
        ],
        "standards": [
            "The leakage account follows Ekman's work on the leakage of suppressed affect, educationally framed.",
            "Hiding is described as a common human strategy, never as deception or a character flaw.",
            "The gentleness-not-suspicion close is explicit: the record teaches kindness, not detection.",
        ],
        "citations": [
            "Ekman P, Friesen WV. Unmasking the Face. Englewood Cliffs: Prentice-Hall; 1975.",
            "Goffman E. The Presentation of Self in Everyday Life. New York: Doubleday; 1959.",
            "Cacioppo JT, Patrick W. Loneliness: Human Nature and the Need for Social Connection. New York: Norton; 2008.",
        ],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "expression_gallery",
        "name": "Expression Gallery Notes: Drawing and Playing Loneliness",
        "group": "Facial Expression",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "For the artist: start with the eyes, because everything "
            "else is commentary. Draw them at three-quarter attention - "
            "lids a fraction low, pupils resting on nothing in "
            "particular, the highlight in the eye smaller and dimmer "
            "than in a joyful face. The inner brow lifts two "
            "millimeters; that tiny lift is the whole plea, so do not "
            "overdraw it or the face becomes tragedy instead of "
            "loneliness. The mouth is a study in restraint: a neutral "
            "line, corners eased down a degree, or the pressed thin "
            "line of someone holding the feeling behind the teeth. "
            "Keep the jaw soft - clenched jaws read as anger, and "
            "loneliness is not angry, it is conserved. The head tilts "
            "forward five degrees; the shoulders follow. Leave space "
            "around the figure - loneliness is drawn as much in the "
            "empty chair, the second coffee cup unused, the doorway "
            "the figure stands beside but not in. For the actor: the "
            "feeling plays in stillness, not in tears. Let the voice "
            "go a semitone flatter and trail the ends of sentences; "
            "let the laugh come half a beat late and leave the eyes "
            "out of it. The signature gesture is the aborted reach - "
            "the hand that starts toward the phone and returns to the "
            "lap. Play the wanting, not the sadness: the character "
            "wants the room to include them, and the audience should "
            "feel the want like a hand extended just out of frame. "
            "The most powerful choice is the contrast beat - one "
            "genuine smile at a real kindness, full face, eyes and "
            "all, then the slow fade back as the moment passes. That "
            "fade teaches the audience what the feeling costs."),
        "how_it_works": (
            "The gallery works by translating the science into craft "
            "decisions. Each note encodes a mechanism in drawable or "
            "playable form: the dimmed eye-highlight encodes "
            "attentional withdrawal; the two-millimeter brow lift "
            "encodes the AU1 plea without tipping into melodrama; the "
            "soft jaw distinguishes the feeling from anger's clench; "
            "the negative space (empty chair, unused cup) encodes the "
            "discrepancy model itself - the wanted life drawn as "
            "absence. For the actor, the stillness direction encodes "
            "the conservation principle: the lonely character is "
            "budgeting expression, so restraint reads truer than "
            "display. The aborted reach is the approach-avoidance "
            "paradox made into a single gesture - the hand obeying "
            "both the alarm's call and the defense's veto in one "
            "motion. The contrast beat (genuine smile, then fade) "
            "encodes the thesis of the whole database: the alarm "
            "answers to real contact, and the fade shows the gap "
            "reopening when contact passes. Craft notes like these "
            "are why the database serves simulators and storytellers: "
            "accurate feeling, rendered from the inside, teaches "
            "recognition better than any diagram."),
        "key_points": [
            "Draw the eyes at three-quarter attention with a dimmed highlight; the two-millimeter brow lift is the whole plea.",
            "Keep the jaw soft - clenched reads as anger, and loneliness is conserved, not angry.",
            "Draw the discrepancy itself as negative space: the empty chair, the unused second cup.",
            "Play it in stillness: flatter voice, trailing sentences, the half-beat-late laugh, the aborted reach.",
            "The contrast beat - one genuine full-face smile at a real kindness, then the slow fade - teaches the cost.",
        ],
        "requirements": [
            "Separate artist notes and actor notes, each with at least five concrete craft decisions.",
            "The two-millimeter brow rule stated with the overdraw warning.",
            "The jaw distinction (soft vs clenched) explained as the loneliness/anger separator.",
            "Negative space named as the visual encoding of the discrepancy model.",
            "The contrast beat described as the encoding of the database's thesis.",
        ],
        "standards": [
            "All craft notes derive from the documented features in the face records; nothing is invented for drama.",
            "The notes serve simulation and storytelling education; they do not instruct anyone to perform distress.",
            "No real person is referenced; all figures are hypothetical craft subjects.",
        ],
        "citations": [
            "Ekman P, Friesen WV. Facial Action Coding System. Palo Alto: Consulting Psychologists Press; 1978.",
            "Darwin C. The Expression of the Emotions in Man and Animals. London: John Murray; 1872.",
            "Cacioppo JT, Patrick W. Loneliness: Human Nature and the Need for Social Connection. New York: Norton; 2008.",
        ],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "classic_triggers",
        "name": "The Classic Triggers: Situations That Commonly Set It Off",
        "group": "Triggers",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "Certain situations trigger loneliness so reliably that "
            "they are the field's greatest hits. Moving to a new city "
            "is the classic: the entire social map is wiped in a week, "
            "and the person eats, commutes, and evenings alone while "
            "the brain keeps expecting the old circle to be there. "
            "Relationship endings - breakups, divorce, the death of "
            "someone close - remove both a bond and the daily contact "
            "that bond carried, the double hit that Weiss mapped. "
            "Starting a new school or job drops a person into a formed "
            "social world where everyone else's ease is on display and "
            "entry feels like auditioning. The empty nest and "
            "retirement are the slow versions: the house or the week "
            "empties by degrees until one day the quiet has texture. "
            "Living alone after years of company, the first holidays "
            "after a loss, the hospital waiting room at 2 am, the "
            "business trip dinner in a strange city - all share one "
            "structure: a contrast between the contact the situation "
            "seems to promise and the contact actually available. "
            "Even happy events trigger it: weddings, reunions, and "
            "new-baby seasons confront the unpartnered or the "
            "childless with a vivid picture of the belonging they do "
            "not have. The trigger is never the event alone - it is "
            "the event minus the expected company, the gap opening in "
            "real time, which is why the same event with the right "
            "person beside you triggers nothing at all."),
        "how_it_works": (
            "Classic triggers work by opening the perceived gap "
            "suddenly or visibly. The mechanism is always contrast: "
            "the mind holds a template of expected contact (my "
            "friends at dinner, my partner beside me, my kids in the "
            "house), the situation delivers less, and the discrepancy "
            "alarm fires on the difference. Moves and new starts work "
            "by wiping the contact inventory while the expectation "
            "template still shows the old world - the brain keeps "
            "reaching for a circle that is three time zones away. "
            "Endings work by removing a high-value bond that also "
            "served as a social hub: the partner was not only company "
            "but the plus-one, the dinner companion, the person who "
            "made rooms feel populated. Slow triggers (empty nest, "
            "retirement) work by erosion: each small loss is below "
            "the noticing threshold until the cumulative gap crosses "
            "it all at once, which is why the quiet gets its texture "
            "on an ordinary Tuesday. Happy-event triggers work by "
            "forced comparison: the celebration displays the very "
            "belonging the person lacks, turning joy's scenery into "
            "loneliness's evidence. Knowing the structure lets a "
            "reader predict their vulnerable windows - the move, the "
            "first holiday, the reunion - and pre-fill them with "
            "planned contact instead of meeting the gap unarmed."),
        "key_points": [
            "The greatest hits: moves, endings, new schools/jobs, empty nest, retirement, first holidays after loss.",
            "Every trigger shares one structure: expected company minus actual company, the gap opening in real time.",
            "Moves wipe the contact inventory while the expectation template still shows the old world.",
            "Slow triggers work by erosion - each loss below threshold until the cumulative gap crosses it at once.",
            "Happy events trigger by forced comparison: celebration scenery becomes loneliness's evidence.",
        ],
        "requirements": [
            "At least eight classic trigger situations named with their specific gap mechanism.",
            "The shared contrast structure stated as the universal trigger formula.",
            "The double hit of endings named: bond removed plus daily contact removed.",
            "The erosion mechanism explained for slow triggers.",
            "The predictive use stated: readers can pre-fill vulnerable windows with planned contact.",
        ],
        "standards": [
            "Trigger situations are drawn from the life-events literature in loneliness research, described not diagnosed.",
            "The Weiss double-hit account follows Weiss 1973 on the social provisions of relationships.",
            "The predictive framing is ordinary planning guidance, not clinical prevention advice.",
        ],
        "citations": [
            "Weiss RS. Loneliness: The Experience of Emotional and Social Isolation. Cambridge MA: MIT Press; 1973.",
            "Perlman D, Peplau LA. Toward a social psychology of loneliness. In: Duck S, Gilmour R, eds. Personal Relationships in Disorder. London: Academic Press; 1981:31-56.",
            "Qualter P et al. Loneliness across the life span. Perspect Psychol Sci. 2015;10(1):250-264.",
        ],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "personal_triggers",
        "name": "Personal Triggers: Memories, Anniversaries, and Private Associations",
        "group": "Triggers",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "Beyond the classic situations, everyone carries a private "
            "set of triggers wired by their own history. A song from "
            "the summer of a great friendship can drop the listener "
            "into the gap in four bars. A restaurant, a park bench, a "
            "stretch of highway holds the ghost of who used to be "
            "there, and passing it replays the absence. Anniversaries "
            "are the calendar's triggers: the date of a move, a "
            "breakup, a death - the body often remembers before the "
            "mind checks the date, and the person feels inexplicably "
            "heavy until the calendar explains it. Objects trigger: "
            "the extra toothbrush still in the holder, the book never "
            "returned, the saved voicemail that is now the only place "
            "the voice lives. Smells are the fastest - cut grass from "
            "childhood summers, a particular detergent from a shared "
            "apartment, rain on hot pavement from the city where "
            "everything was still possible. Rituals trigger: the "
            "Sunday call that no longer comes, the group chat gone "
            "quiet, the holiday dish with no one left who knows the "
            "recipe. These triggers are immune to logic - the person "
            "knows the song is just a song, and feels the gap anyway, "
            "because associative memory does not consult the rational "
            "mind before firing. The kindest response to a personal "
            "trigger is not to argue with it but to translate it: the "
            "song hurts because the friendship mattered, and mattering "
            "is the thing the alarm is trying to protect."),
        "how_it_works": (
            "Personal triggers work through associative memory: the "
            "brain stores emotional states bound to their sensory "
            "context, and a fragment of the context re-evokes a "
            "diluted version of the state. The lonely stretch of a "
            "person's life gets filed with its tags - the season, the "
            "soundtrack, the rooms - and any tag can reopen the file. "
            "Anniversaries work through temporal conditioning: the "
            "body learns the calendar the way it learns any repeated "
            "pairing, which is why the heaviness can arrive before "
            "conscious recall of the date. Smells are fastest because "
            "olfaction has the shortest path to the emotion and "
            "memory systems, bypassing the thalamic relay that other "
            "senses use. Objects work as discrepancy made tangible: "
            "the extra toothbrush is the wanted life sitting in the "
            "actual life's bathroom, the gap you can hold. Ritual "
            "triggers work by broken pattern: the mind runs the "
            "Sunday-call program, finds no one on the other end, and "
            "the error signal reads as loneliness. None of this is "
            "under rational control, which is why arguing with a "
            "trigger fails and translating it works: naming what the "
            "association is protecting converts the ambush into "
            "information."),
        "key_points": [
            "Private triggers are wired by personal history: songs, places, anniversaries, objects, smells, broken rituals.",
            "The body often remembers anniversaries before the mind checks the date - temporal conditioning.",
            "Smells are fastest: olfaction takes the shortest path to emotion and memory systems.",
            "Objects are discrepancy made tangible: the extra toothbrush is the wanted life in the actual bathroom.",
            "Arguing with a trigger fails; translating it works - the song hurts because the friendship mattered.",
        ],
        "requirements": [
            "At least six categories of personal trigger named with concrete examples.",
            "The anniversary mechanism explained via temporal conditioning and body-before-mind recall.",
            "The olfactory speed advantage explained neurologically in plain language.",
            "The extra-toothbrush image used to show discrepancy made tangible.",
            "The translate-don't-argue rule stated as the kindest response.",
        ],
        "standards": [
            "The associative-memory account follows standard learning and memory principles, educationally framed.",
            "The olfactory claim follows established neuroscience on olfaction-emotion pathways, plainly stated.",
            "No therapeutic technique is prescribed; translation is framed as ordinary sense-making.",
        ],
        "citations": [
            "Herz RS. Are odors the best cues to memory? A cross-modal comparison of associative memory stimuli. Ann N Y Acad Sci. 1998;855:670-674.",
            "Weiss RS. Loneliness: The Experience of Emotional and Social Isolation. Cambridge MA: MIT Press; 1973.",
            "Cacioppo JT, Patrick W. Loneliness: Human Nature and the Need for Social Connection. New York: Norton; 2008.",
        ],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "surprise_triggers",
        "name": "Surprise Triggers: The Odd, Unexpected Things That Set It Off",
        "group": "Triggers",
        "ladder_rank": 9,
        "ladder_tier": "compounded",
        "description": (
            "Some triggers ambush from directions no one guards. A "
            "crowded, joyful room can trigger loneliness harder than an "
            "empty one - the laughter is proof of the very thing that "
            "feels missing, and being unseen in a crowd is lonelier "
            "than being alone, because aloneness at least matches the "
            "scenery. A silent phone on a Friday night: nothing has "
            "happened, no one has rejected anyone, but the absence of "
            "the buzz is read by the scanning mind as a verdict. A "
            "perfectly sunny Saturday can do it - the day is built for "
            "sharing and there is no one to share it with, so the "
            "weather feels like an invitation addressed to someone "
            "else. Other people's inside jokes, overheard in a cafe, "
            "land like small locked doors. Sitting among couples at a "
            "dinner, the only single chair, the conversation pairing "
            "off around you. The grocery store on a Sunday evening, "
            "everyone shopping for a household and you shopping for "
            "one. A child's drawing on a coworker's desk. The "
            "particular cruelty of surprise triggers is their "
            "innocence: nothing bad occurred, which leaves the person "
            "feeling foolish for feeling anything - and the "
            "foolishness adds shame to the ache. But the mechanism is "
            "lawful, not foolish: each surprise is a contrast event, "
            "the wanted life flashing briefly against the actual one, "
            "and the alarm is doing exactly what it evolved to do."),
        "how_it_works": (
            "Surprise triggers work through unguarded contrast. The "
            "classic triggers are at least expected - the mover knows "
            "the move will be hard - so the mind braces. Surprise "
            "triggers arrive where the guard is down: the person is "
            "not thinking about loneliness at all, and then the "
            "crowded room, the sunny day, or the overheard joke "
            "flashes the discrepancy without warning. The unguarded "
            "mind has no suppression ready, so the full signal lands "
            "at once - which is why a sunny Saturday can hit harder "
            "than the lonely Sunday the person saw coming. The "
            "silent-phone trigger works through the hypervigilant "
            "read of absence: the scanning mind treats no-signal as "
            "signal, filling the quiet with the worst interpretation. "
            "The crowd trigger works through the cruelest arithmetic "
            "of the field: loneliness measures perceived connection, "
            "so a room full of visible connection that excludes you "
            "maximizes the perceived gap. The shame add-on works "
            "through the myths: if loneliness only strikes the "
            "broken, then feeling it over something innocent must "
            "mean something is wrong with me - the myth taxing a "
            "lawful alarm. Naming the mechanism disarms the shame: "
            "the trigger is contrast, contrast is the alarm's native "
            "language, and no one is foolish for hearing it."),
        "key_points": [
            "Joyful crowds can trigger harder than empty rooms: being unseen in a crowd maximizes the perceived gap.",
            "The silent phone is read by the scanning mind as a verdict - absence of signal becomes signal.",
            "Sunny Saturdays and shared rituals ambush because the guard is down where loneliness is not expected.",
            "The innocence of the trigger adds shame via the myths - feeling foolish for feeling anything.",
            "The mechanism is lawful, not foolish: unguarded contrast, the alarm's native language.",
        ],
        "requirements": [
            "At least six surprise triggers named, each with its contrast mechanism.",
            "The crowd paradox explained via the perceived-gap arithmetic.",
            "The silent-phone mechanism explained via hypervigilant absence-reading.",
            "The unguarded-contrast principle stated: no suppression ready, full signal lands.",
            "The shame add-on traced to the myths and disarmed by naming the mechanism.",
        ],
        "standards": [
            "All surprise triggers are ordinary situations; none is framed as pathological or abnormal.",
            "The contrast account follows the discrepancy model applied to unexpected contexts.",
            "The shame-disarming close is educational reframing, not therapeutic intervention.",
        ],
        "citations": [
            "Perlman D, Peplau LA. Toward a social psychology of loneliness. In: Duck S, Gilmour R, eds. Personal Relationships in Disorder. London: Academic Press; 1981:31-56.",
            "Cacioppo JT, Patrick W. Loneliness: Human Nature and the Need for Social Connection. New York: Norton; 2008.",
            "Masi CM et al. A meta-analysis of interventions to reduce loneliness. Pers Soc Psychol Rev. 2011;15(3):219-266.",
        ],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "chain_reactions",
        "name": "Chain Reactions: How One Trigger Sets Off a Cascade",
        "group": "Triggers",
        "ladder_rank": 9,
        "ladder_tier": "compounded",
        "description": (
            "Loneliness rarely travels alone for long - one trigger "
            "sets off a cascade, and the cascade is where a bad "
            "evening becomes a bad month. The classic chain starts "
            "with a small trigger: a friend cancels dinner. The "
            "loneliness alarm fires a twinge. Then shame arrives with "
            "its story - they canceled because I am too much, or not "
            "enough - and shame says hide the feeling. Hiding means "
            "the person does not reschedule, does not call someone "
            "else, performs fine at work the next day. The "
            "performance costs energy; the un-rescheduled weekend "
            "arrives empty; the empty weekend confirms the original "
            "story. Now the cascade recruits the body: poor sleep "
            "Friday, gray fatigue Saturday, the phone stared at and "
            "put down Sunday. By Monday the person is not dealing "
            "with a canceled dinner anymore - they are dealing with "
            "a week of evidence that they are alone, manufactured "
            "largely by the chain itself. Other chains branch "
            "differently: trigger to anger (they always do this, "
            "people are unreliable) to pushing people away to the "
            "isolation the anger predicted. Trigger to fear (this "
            "is my life now) to clinging - the triple text, the "
            "overlong call - to the other person's withdrawal to "
            "the confirmation of the fear. Every chain shares the "
            "shape: the original signal is small and answerable, "
            "and each link adds a second emotion that makes the "
            "answer harder. Breaking a chain never requires fixing "
            "the original trigger - it requires refusing one link: "
            "rescheduling the dinner, naming the shame, picking up "
            "the phone. One refused link starves the whole cascade."),
        "how_it_works": (
            "Chains work through emotion-to-behavior-to-evidence "
            "loops. Each link has the same three parts: a feeling "
            "generates a behavior, the behavior changes the social "
            "environment, the changed environment is read as evidence "
            "for the feeling. Cancel to shame to hiding to empty "
            "weekend to confirmation: the hiding behavior manufactures "
            "the very isolation the shame predicted. The anger branch "
            "works through pushing-away behavior that manufactures "
            "rejection; the fear branch works through clinging "
            "behavior that manufactures withdrawal. The reason chains "
            "accelerate is that each link recruits a new system - "
            "shame recruits hiding, hiding recruits the empty "
            "calendar, the empty calendar recruits the body triad - "
            "so the cascade gains mass as it runs. The intervention "
            "point is structural, not emotional: you cannot argue a "
            "chain out of feeling lonely, but you can refuse a "
            "behavioral link, and a refused link breaks the "
            "evidence-manufacturing cycle. This is the most practical "
            "record in the triggers section, because chains are where "
            "readers actually live - not in single triggers but in "
            "the weeks the triggers start."),
        "key_points": [
            "The classic chain: canceled dinner to shame to hiding to empty weekend to manufactured evidence.",
            "The anger branch manufactures rejection by pushing away; the fear branch manufactures withdrawal by clinging.",
            "Every link is feeling to behavior to evidence: the behavior creates the proof the feeling predicted.",
            "Chains accelerate because each link recruits a new system - shame, calendar, body triad.",
            "Breaking a chain means refusing one behavioral link, not fixing the original trigger.",
        ],
        "requirements": [
            "The full classic chain rendered link by link with the three-part structure visible.",
            "Two branch chains described: the anger/push-away branch and the fear/clinging branch.",
            "The feeling-behavior-evidence loop named as the universal link shape.",
            "The acceleration mechanism explained via system recruitment.",
            "The refused-link intervention stated as structural, with a concrete example.",
        ],
        "standards": [
            "Chains are described as common patterns, never as disorders or syndromes.",
            "The intervention framing is ordinary behavioral observation, not clinical advice.",
            "All branches use hypothetical persons; no real individual is depicted.",
        ],
        "citations": [
            "Cacioppo JT, Patrick W. Loneliness: Human Nature and the Need for Social Connection. New York: Norton; 2008.",
            "Hawkley LC, Cacioppo JT. Loneliness matters: a theoretical and empirical review of consequences and mechanisms. Ann Behav Med. 2010;40(2):218-227.",
            "Perlman D, Peplau LA. Toward a social psychology of loneliness. In: Duck S, Gilmour R, eds. Personal Relationships in Disorder. London: Academic Press; 1981:31-56.",
        ],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "actions",
        "name": "What People Do: The Typical Actions and Reactions",
        "group": "How It Shows in Behavior",
        "ladder_rank": 9,
        "ladder_tier": "compounded",
        "description": (
            "Loneliness has a behavioral repertoire, and it splits "
            "into two great families: reaching and retreating. The "
            "reaching behaviors are the alarm doing its job - texting "
            "old friends out of the blue, lingering after meetings, "
            "saying yes to invitations that do not even sound fun, "
            "adopting the office stray cat of a conversation. The "
            "retreating behaviors are the defense doing its job - "
            "canceling plans, leaving gatherings early, declining the "
            "invitation before it can be declined, the slow fade from "
            "the group chat. Most lonely people do both in the same "
            "week, sometimes the same evening: the text sent at 9 pm "
            "and regretted at 9:05, the party attended and left at "
            "9:40. Then there are the fillers, the behaviors that "
            "neither reach nor retreat but occupy the hours: "
            "doomscrolling through other people's togetherness, "
            "reorganizing closets at midnight, the third episode "
            "becoming the sixth, long drives with no destination. "
            "And the substitutes: the pet talked to like a person, "
            "the plants fussed over, the parasocial friendships with "
            "hosts and characters who cannot leave. None of these "
            "are character flaws - they are a social animal's "
            "inventory of moves when the herd is out of reach. The "
            "tragedy is only in the ratio: when retreating and "
            "filling outnumber reaching for weeks, the repertoire "
            "itself becomes the cage. The hopeful note is also in "
            "the ratio: one genuine reach per day, sustained, "
            "outperforms a month of fillers."),
        "how_it_works": (
            "The repertoire works as the alarm and the defense "
            "negotiating through behavior. Reaching is approach "
            "motivation: the loneliness signal driving contact-"
            "seeking, from the impulsive (the 9 pm text) to the "
            "planned (joining the recurring group). Retreating is "
            "avoidance motivation: the hypervigilant defense "
            "minimizing exposure to anticipated rejection, from the "
            "polite (leaving early) to the preemptive (declining "
            "first). The two systems fire on different schedules - "
            "the alarm is loudest in the empty evening, the defense "
            "is loudest at the moment of the bid - which is why the "
            "same person reaches and retreats within hours. Fillers "
            "are displacement: energy with no social target, routed "
            "into scrolling, organizing, and streaming. Substitutes "
            "are the attachment system accepting partial payment: a "
            "pet or a plant or a beloved host provides some of the "
            "felt-presence the alarm wants, which is why they "
            "genuinely help and genuinely do not suffice. Reading "
            "the repertoire in oneself is the skill: noticing which "
            "family ran the day tells the person whether the alarm "
            "or the defense is driving, and the driver determines "
            "the next move."),
        "key_points": [
            "The repertoire splits into reaching (the alarm's moves) and retreating (the defense's moves).",
            "Most lonely people do both in the same week - the 9 pm text and the 9:40 exit are the same evening.",
            "Fillers (scrolling, reorganizing, streaming) occupy the hours; substitutes (pets, plants, hosts) take partial payment.",
            "The two systems fire on different schedules, which is why reaching and retreating alternate.",
            "The ratio is the cage and the key: one genuine reach a day outperforms a month of fillers.",
        ],
        "requirements": [
            "The reaching family and retreating family each given at least four concrete behaviors.",
            "The same-evening alternation shown as the normal pattern, not inconsistency.",
            "Fillers and substitutes distinguished with their different mechanisms.",
            "The different firing schedules of alarm and defense explained.",
            "The ratio rule stated as both the trap and the way out.",
        ],
        "standards": [
            "All behaviors are described as a social animal's normal inventory, never as flaws or symptoms.",
            "The approach-avoidance account follows standard motivation theory, educationally framed.",
            "Substitutes are described as genuinely helping and genuinely insufficient, without judgment.",
        ],
        "citations": [
            "Cacioppo JT, Patrick W. Loneliness: Human Nature and the Need for Social Connection. New York: Norton; 2008.",
            "Baumeister RF, Leary MR. The need to belong: desire for interpersonal attachments as a fundamental human motivation. Psychol Bull. 1995;117(3):497-529.",
            "Perlman D, Peplau LA. Toward a social psychology of loneliness. In: Duck S, Gilmour R, eds. Personal Relationships in Disorder. London: Academic Press; 1981:31-56.",
        ],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "speech",
        "name": "What People Say: Phrases, Tone, and Speech Patterns",
        "group": "How It Shows in Behavior",
        "ladder_rank": 9,
        "ladder_tier": "compounded",
        "description": (
            "Loneliness has a voice, and it is quieter than the "
            "person thinks. The signature phrase is I'm fine - "
            "delivered a half-second too fast, with a brightness "
            "that does not reach the eyes, closing the topic before "
            "it opens. No worries and all good do the same work: "
            "the all-purpose sealant over any crack the feeling "
            "might show through. The lonely person's questions "
            "boomerang - how are you is returned instantly, keeping "
            "the spotlight safely on the other chair. Self-"
            "deprecating jokes do the confessing sideways: thrilling "
            "Friday night over here, my plants are my social life "
            "now - laughter invited at the feeling so no one has to "
            "sit with it seriously. Tone goes flat and trailing: "
            "sentences lose their ends, the voice drops a semitone, "
            "stories get told in summary instead of scenes, as if "
            "detail were an imposition. The deeper pattern is "
            "initiation decay: the lonely person stops starting. "
            "Texts get shorter and more reactive, calls are returned "
            "but never placed, invitations are accepted but never "
            "issued. In groups they become the questioner, the "
            "listener, the laugh-track - every role that keeps them "
            "present without being exposed. Listening for this "
            "voice in others is one of the kindest skills in the "
            "database: the person saying I'm fine in that "
            "particular flat brightness is often the person most "
            "in need of a second, slower question."),
        "how_it_works": (
            "The speech pattern works as verbal impression "
            "management. I'm fine and its cousins are closers: "
            "they answer the social check-in while refusing the "
            "emotional one, satisfying politeness and starving "
            "honesty in a single move. The boomerang question "
            "works as deflection with manners - it looks like "
            "interest while functioning as evasion. Self-"
            "deprecation works as controlled disclosure: the "
            "feeling is admitted but framed as comedy, which "
            "lets the speaker test whether the listener will "
            "take it seriously without risking a serious "
            "rejection. The flat trailing tone is the "
            "conservation principle made audible: expression "
            "budgeted, detail withheld, the voice matching the "
            "dimmed face. Initiation decay is the defense "
            "system's veto on bids: each un-placed call is a "
            "rejection preempted, and the preemption feels like "
            "safety while functioning as isolation. The "
            "questioner role in groups is the safest seat in the "
            "room - present, useful, unexposed. For the reader, "
            "the practical skill is bid-detection in reverse: "
            "when you hear the closers and the boomerangs, do "
            "not accept the first answer. Ask the second, "
            "slower question, and mean it."),
        "key_points": [
            "I'm fine, no worries, all good: closers that satisfy politeness while starving honesty.",
            "The boomerang question looks like interest and functions as evasion.",
            "Self-deprecating jokes are controlled disclosure: the feeling admitted as comedy to test the listener.",
            "Initiation decay is the signature: texts shorten, calls are returned never placed, invitations accepted never issued.",
            "The kindest skill: hear the closers, then ask the second, slower question - and mean it.",
        ],
        "requirements": [
            "At least five signature phrases or phrase-families named with their function.",
            "Tone described: flat, trailing, semitone down, summary-not-scenes.",
            "Initiation decay defined with its three observable forms.",
            "The group questioner role named as the safest seat.",
            "The second-slower-question skill stated as the reader's takeaway.",
        ],
        "standards": [
            "Speech patterns are described as common strategies, never as lies or manipulation.",
            "The analysis stays at the level of observable communication, not mind-reading.",
            "The takeaway is framed as kindness toward others, not as self-surveillance.",
        ],
        "citations": [
            "Goffman E. The Presentation of Self in Everyday Life. New York: Doubleday; 1959.",
            "Cacioppo JT, Patrick W. Loneliness: Human Nature and the Need for Social Connection. New York: Norton; 2008.",
            "Mehrabian A. Nonverbal Communication. Chicago: Aldine-Atherton; 1972.",
        ],
        "sig_lens": SIG_LENS,
    },
]
ENTRIES += [
    {
        "key": "decisions",
        "name": "How Loneliness Changes Decisions and Judgment",
        "group": "How It Shows in Behavior",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Loneliness is not just a feeling; it is a lens, and the "
            "lens bends judgment. The best-documented bend is the "
            "threat read: lonely people systematically interpret "
            "ambiguous social data as rejection - the delayed text "
            "means disinterest, the neutral face means disapproval, "
            "the laugh across the room means being laughed at. "
            "Cacioppo's labs showed this as hypervigilance for "
            "social threat, measurable in attention tasks, not just "
            "self-report. The second bend is in social risk: the "
            "lonely mind both craves and fears the bid, so decisions "
            "oscillate - the impulsive 11 pm text to an ex-friend "
            "followed by the week of declining every invitation. "
            "The third bend is in generosity accounting: feeling "
            "unseen makes people track who reached out last, who "
            "owes whom a call, and the ledger-keeping poisons the "
            "very spontaneity that connection needs. The fourth is "
            "in time horizon: chronic loneliness shortens it. The "
            "person stops investing in slow-build friendships "
            "because the alarm screams for contact now, and chooses "
            "the quick hit - the party with strangers, the marathon "
            "scroll - over the slow cultivation that actually "
            "closes the gap. The fifth is self-assessment: the "
            "lonely judge themselves harsher social performers than "
            "any observer does, so they decline the gathering they "
            "would have been fine at. None of these are stupidity; "
            "they are a threat system doing threat-system math on "
            "social data. The correction is not willpower but "
            "calibration: noticing the lens, naming it as lens, and "
            "letting one small piece of contrary evidence - the "
            "warm reply, the good evening - update the prescription."),
        "how_it_works": (
            "The judgment bends work through the hypervigilant "
            "prior. In Bayesian terms the lonely mind runs a high "
            "prior on rejection, so ambiguous evidence gets sorted "
            "into the rejection bin - the delayed text is not "
            "ambiguous to this mind, it is confirmatory. The "
            "oscillation in social risk follows the two-system "
            "schedule: the alarm drives impulsive bids when the "
            "gap screams loudest (late evening, weekends), and the "
            "defense vetoes planned bids when exposure is "
            "imagined in advance. Ledger-keeping is the mind "
            "trying to make connection fair and safe by "
            "accounting it, which backfires because felt closeness "
            "grows from uncounted generosity. The shortened time "
            "horizon is the alarm's urgency misapplied: hunger "
            "wants food now, and the social hunger borrows that "
            "urgency, preferring the quick hit to the slow build "
            "even though only the slow build stocks the pantry. "
            "The harsh self-assessment is the spotlight effect "
            "with a threat filter: the person overestimates both "
            "how much they are noticed and how poorly they "
            "perform. Calibration works because priors update: "
            "each warm reply is data, and deliberately logging "
            "the data - the evening that went fine, the text "
            "that was welcomed - retrains the prior faster than "
            "argument ever could."),
        "key_points": [
            "The threat read: ambiguous social data gets systematically sorted into the rejection bin.",
            "Social risk oscillates: impulsive late-night bids alternate with weeks of declined invitations.",
            "Ledger-keeping (who reached out last) poisons the uncounted generosity that closeness needs.",
            "Chronic loneliness shortens the time horizon: quick hits chosen over the slow build that stocks the pantry.",
            "The correction is calibration, not willpower: notice the lens, name it, log the contrary evidence.",
        ],
        "requirements": [
            "At least five judgment bends named: threat read, risk oscillation, ledger-keeping, time horizon, self-assessment.",
            "The hypervigilance finding attributed to Cacioppo's attention-task research.",
            "The Bayesian-prior framing used to explain ambiguous-evidence sorting.",
            "The urgency-misapplication explained: social hunger borrowing hunger's now.",
            "The calibration correction stated with the evidence-logging mechanism.",
        ],
        "standards": [
            "Cognitive effects are described as documented patterns, never as thinking errors or disorders.",
            "The Bayesian framing is an educational metaphor, not a clinical model.",
            "The correction is framed as ordinary noticing and logging, not as therapy.",
        ],
        "citations": [
            "Cacioppo JT et al. Loneliness as a specific risk factor for depressive symptoms. Psychol Aging. 2006;21(2):140-151.",
            "Hawkley LC, Cacioppo JT. Loneliness matters: a theoretical and empirical review of consequences and mechanisms. Ann Behav Med. 2010;40(2):218-227.",
            "Baumeister RF, Leary MR. The need to belong: desire for interpersonal attachments as a fundamental human motivation. Psychol Bull. 1995;117(3):497-529.",
        ],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "intensity_behavior",
        "name": "Behavior Under Intensity: How Actions Escalate as the Feeling Grows",
        "group": "How It Shows in Behavior",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Watch the repertoire across the dial and a pattern "
            "emerges: mild loneliness reaches, moderate loneliness "
            "manages, intense loneliness sabotages. At mild "
            "settings the behaviors are clean and effective - the "
            "text sent, the plan made, the evening salvaged. The "
            "alarm is a whisper and the person obeys it simply. "
            "At moderate settings management takes over: the "
            "calendar is curated, the performance of fine is "
            "maintained, bids are placed carefully and only where "
            "success is likely. The person is functioning, but a "
            "visible fraction of their energy goes to handling the "
            "feeling rather than living. At high settings the "
            "defense outruns the alarm and the behaviors turn "
            "against the person's own interests. Plans get "
            "canceled the morning of, with reasons invented that "
            "even the inventor half-believes. Invitations are "
            "declined preemptively, then the decliner grieves the "
            "evening they refused. Tests are administered: the "
            "unanswered text left unanswered to see if they chase, "
            "the vague I'm fine deployed to see who asks twice - "
            "and the tests are graded on a curve no one can pass, "
            "because the hypervigilant grader finds the flaw in "
            "every response. The cruelest escalation is the "
            "push-pull: pursuing someone warmly for a week, then "
            "going cold the moment warmth is returned, because "
            "returned warmth raises the stakes of the feared "
            "rejection. At the extreme the person may pick fights "
            "to end things first, or disappear from circles "
            "entirely - controlling the loss by authoring it. "
            "None of this is malice; it is a defense system "
            "with the gain turned past the point of usefulness, "
            "protecting the person from rejections by "
            "guaranteeing the isolation."),
        "how_it_works": (
            "Escalation works through the changing balance of the "
            "two systems. At low dial the alarm dominates and its "
            "instructions are simple: seek contact. Behavior is "
            "adaptive because the signal is clean. As the dial "
            "rises, the defense system - hypervigilance, shame, "
            "rejection-expectation - gains authority, and behavior "
            "becomes a compromise between seeking and guarding: "
            "careful bids, curated calendars, managed displays. "
            "Past a threshold the defense takes command. Its "
            "instructions are all forms of preemption: cancel "
            "first, decline first, test first, leave first. "
            "Preemption feels like control, which is why it is so "
            "seductive at high intensity - authoring the loss "
            "beats suffering it. But every preemptive behavior "
            "manufactures the evidence the defense predicted, so "
            "the threshold keeps ratcheting: each sabotaged plan "
            "is proof that plans fail, each failed test is proof "
            "that people fail. The push-pull is the two systems "
            "alternating at high gain: approach wins the week, "
            "avoidance wins the moment warmth arrives. The way "
            "back down the dial is the same in reverse - small "
            "un-sabotaged bids, kept plans, tests retired - "
            "letting the alarm's simple instructions run "
            "unopposed until the defense stands down."),
        "key_points": [
            "Mild reaches, moderate manages, intense sabotages: the dial sets which system commands behavior.",
            "At high intensity the defense preempts: cancel first, decline first, test first, leave first.",
            "Tests are graded on a curve no one can pass - the hypervigilant grader finds the flaw in every response.",
            "The push-pull is the two systems alternating at high gain: approach wins the week, avoidance wins the warm moment.",
            "The way back is un-sabotage: kept plans, retired tests, small bids run unopposed until the defense stands down.",
        ],
        "requirements": [
            "The three-band escalation arc rendered behaviorally: reach, manage, sabotage.",
            "At least four sabotage behaviors named: morning-of cancellations, preemptive declines, tests, push-pull, authored exits.",
            "The test mechanism explained: unpassable grading via hypervigilant flaw-finding.",
            "Preemption framed as seductive control that manufactures its own evidence.",
            "The reversal path stated: un-sabotage as the way back down the dial.",
        ],
        "standards": [
            "Escalation is described as a defense system past useful gain, never as self-destruction or pathology.",
            "All behaviors are framed as understandable under the mechanism, without excusing their costs.",
            "The reversal path is ordinary behavioral description, not clinical guidance.",
        ],
        "citations": [
            "Cacioppo JT, Patrick W. Loneliness: Human Nature and the Need for Social Connection. New York: Norton; 2008.",
            "Hawkley LC, Cacioppo JT. Loneliness matters: a theoretical and empirical review of consequences and mechanisms. Ann Behav Med. 2010;40(2):218-227.",
            "Mikulincer M, Shaver PR. Attachment in Adulthood: Structure, Dynamics, and Change. New York: Guilford; 2007.",
        ],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "healthy_expression",
        "name": "Healthy Expression: Saying It, Showing It, Channeling It Well",
        "group": "Expressing It Healthily",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Healthy expression of loneliness has three channels, "
            "and they all beat hiding. The first is saying it "
            "plainly: I've been feeling lonely lately lands "
            "differently than the myths predict. Said to the right "
            "person - a friend, a sibling, a trusted coworker - it "
            "is usually met not with judgment but with relief and "
            "recognition, because the listener has felt it too. "
            "The plain statement works because it converts the "
            "feeling from a secret into a fact, and facts can be "
            "acted on while secrets can only be carried. The "
            "second channel is showing it appropriately: letting "
            "the face and voice carry a little of the truth - "
            "admitting the weekend was quiet, accepting the "
            "invitation with visible gladness instead of performed "
            "casualness, lingering after the meeting because the "
            "company is wanted. The third channel is channeling: "
            "putting the feeling's energy into forms that build "
            "the bridge it wants. Loneliness has funded some of "
            "humanity's best letters, songs, and long walks that "
            "ended at a friend's door; the ache converts cleanly "
            "into making, because making is a bid the maker "
            "controls. What makes all three healthy is direction: "
            "the feeling is moved outward - into words, into "
            "visible want, into work - instead of being sealed "
            "inward where it ferments into shame. None of this "
            "requires a dramatic confession. The unit of healthy "
            "expression is small and repeatable: one honest "
            "sentence, one undisguised gladness, one made thing "
            "shared."),
        "how_it_works": (
            "Healthy expression works by breaking the secrecy that "
            "feeds the loop. Saying it plainly attacks the "
            "hide-it myth directly: the predicted judgment does "
            "not arrive, and the non-arrival is data that updates "
            "the shame prior. It also recruits help honestly - "
            "people cannot answer an alarm they cannot hear, and "
            "the plain statement is the alarm made audible. "
            "Showing it appropriately works through legibility: "
            "the visible want (gladness undisguised, lingering "
            "admitted) gives others accurate data about what the "
            "person needs, replacing the fine-performance that "
            "told everyone nothing was wanted. Channeling works "
            "through sublimation's ordinary form: the feeling's "
            "arousal is routed into making, and the made thing "
            "becomes a social object - a letter sent, a song "
            "shared, a meal cooked for someone - which is a bid "
            "the maker controls end to end. All three share the "
            "outward direction, which is the structural opposite "
            "of the bottling that ferments shame. The small-and-"
            "repeatable unit matters because expression is a "
            "skill strengthened by reps, not a confession "
            "strengthened by drama."),
        "key_points": [
            "Three channels beat hiding: saying it plainly, showing it appropriately, channeling it into making.",
            "The plain statement converts the feeling from a secret into a fact - facts can be acted on.",
            "The predicted judgment usually does not arrive; its non-arrival updates the shame prior.",
            "Visible want gives others accurate data; the fine-performance gave them nothing to answer.",
            "The unit is small and repeatable: one honest sentence, one undisguised gladness, one made thing shared.",
        ],
        "requirements": [
            "Three distinct healthy channels described with concrete examples of each.",
            "The secret-to-fact conversion named as the core mechanism of plain speech.",
            "The shame-prior update explained via the non-arrival of predicted judgment.",
            "Channeling illustrated with the made-thing-as-bid mechanism.",
            "The small-and-repeatable unit stated as the skill-building principle.",
        ],
        "standards": [
            "Expression guidance is general, safe, everyday communication advice - not therapeutic instruction.",
            "The plain-speech examples are ordinary sentences any adult might say; nothing clinical.",
            "No promise is made about others' responses; the typical reception is described, not guaranteed.",
        ],
        "citations": [
            "Pennebaker JW. Opening Up by Writing It Down. New York: Guilford; 1997.",
            "Cacioppo JT, Patrick W. Loneliness: Human Nature and the Need for Social Connection. New York: Norton; 2008.",
            "Masi CM et al. A meta-analysis of interventions to reduce loneliness. Pers Soc Psychol Rev. 2011;15(3):219-266.",
        ],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "unhealthy_expression",
        "name": "Unhealthy Expression: Bottling It Up or Exploding - What Each Costs",
        "group": "Expressing It Healthily",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Mishandled loneliness goes two directions, and both "
            "charge interest. Bottling is the commoner: the feeling "
            "is sealed behind fine, and the seal holds for weeks. "
            "The costs compound quietly. First the numbness - the "
            "sealed feeling does not stay sealed, it spreads, "
            "dulling everything until good news lands flat too. "
            "Then the bitterness: unexpressed want ferments into "
            "resentment toward the very people whose company is "
            "wanted - they should have noticed, they never call - "
            "and the resentment makes reaching out feel like "
            "surrender. Then the body collects: the jaw, the "
            "sleep, the gray fatigue, the triad running on the "
            "sealed pressure. Exploding is rarer and louder: the "
            "seal breaks all at once - the 2 am message three "
            "paragraphs long, the tears at the office party, the "
            "accusation (you never include me) fired at people "
            "who had no idea there was a war on. The costs are "
            "immediate: embarrassment, the listeners' "
            "bewilderment, sometimes real damage to the "
            "relationships the feeling was about. And the "
            "aftermath cost is the worst - the exploder concludes "
            "that expression itself is dangerous and bottles "
            "harder next time, which is how the two unhealthy "
            "forms feed each other in the same person. The "
            "difference between the healthy channels and these "
            "two is not honesty versus dishonesty - the exploder "
            "is honest. It is dosage and timing: small, chosen, "
            "repeatable expression versus sealed pressure or "
            "unsealed flood."),
        "how_it_works": (
            "Bottling works through suppression's known costs. "
            "Sealing the feeling does not remove it; it removes "
            "it from the person's deliberate handling while "
            "leaving it active in the background, where it "
            "generalizes - numbness is suppressed affect "
            "spreading to all affect. The bitterness is "
            "attribution under pressure: the mind needs a "
            "reason for the ongoing ache and the nearest "
            "available reasons are other people's failures, so "
            "resentment grows toward the wanted company itself. "
            "Exploding works through pressure dynamics: the "
            "sealed system accumulates until a small trigger - "
            "a kind word at the wrong moment, one drink too "
            "many - breaches it, and the release is "
            "disproportionate to the trigger because it is "
            "proportional to the backlog. The bewilderment of "
            "the listeners is structural: they are responding "
            "to the trigger-sized event while the exploder is "
            "releasing the backlog-sized feeling, so the two "
            "sides are having different conversations. The "
            "aftermath lesson (expression is dangerous) is the "
            "loop's final tax: one flood teaches the person to "
            "seal harder, guaranteeing the next flood. The "
            "healthy alternative is visible in contrast - "
            "dosage and timing, the pressure released in small "
            "chosen amounts before it becomes backlog."),
        "key_points": [
            "Bottling's costs compound: numbness spreading to all feeling, bitterness toward the wanted company, the body collecting.",
            "Exploding's costs are immediate: bewilderment, embarrassment, sometimes real relationship damage.",
            "The aftermath tax is worst: one flood teaches that expression is dangerous, so the person bottles harder.",
            "The two forms feed each other in the same person: seal, flood, seal harder.",
            "The difference from healthy expression is dosage and timing, not honesty - small chosen releases beat backlog floods.",
        ],
        "requirements": [
            "Both unhealthy directions described with at least three specific costs each.",
            "The numbness-spread mechanism explained via suppression generalization.",
            "The bitterness mechanism explained via attribution under pressure.",
            "The backlog-vs-trigger mismatch named as the structural cause of listener bewilderment.",
            "The seal-flood-seal cycle named as the self-feeding loop.",
        ],
        "standards": [
            "Unhealthy patterns are described as common human strategies with costs, never as disorders.",
            "The suppression account follows the emotion-regulation literature, educationally framed.",
            "No clinical terms are used; the language stays at observable behavior and felt experience.",
        ],
        "citations": [
            "Gross JJ. Emotion regulation: affective, cognitive, and social consequences. Psychophysiology. 2002;39(3):281-291.",
            "Pennebaker JW. Opening Up by Writing It Down. New York: Guilford; 1997.",
            "Cacioppo JT, Patrick W. Loneliness: Human Nature and the Need for Social Connection. New York: Norton; 2008.",
        ],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "everyday_practices",
        "name": "Everyday Practices: Small Habits That Keep Connection in Balance",
        "group": "Expressing It Healthily",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The practices that keep loneliness in balance are "
            "small, boring, and repeatable - which is exactly why "
            "they work. Keep one recurring thing on the calendar: "
            "the weekly call with a sibling, the Tuesday trivia "
            "team, the Saturday morning walk with a neighbor. "
            "Recurring beats spontaneous because the lonely mind "
            "is bad at spontaneous - the bid-failure mechanism "
            "eats one-off plans, but a standing appointment "
            "bypasses the whole negotiation. Greet people by name: "
            "the barista, the neighbor, the coworker in the hall. "
            "Named greetings are micro-contacts, and the research "
            "on weak ties says they punch far above their weight "
            "in felt belonging. Keep three threads alive: not "
            "thirty contacts, three - three people you message "
            "often enough that no reopening is ever needed. "
            "Move the body outdoors daily: the walk does double "
            "duty, clearing the gray fatigue and manufacturing "
            "low-stakes proximity to other humans. Volunteer "
            "somewhere regular: the food bank shift, the park "
            "cleanup - structured contact with a shared task, "
            "which is the easiest kind for the guarded to enter. "
            "End each day by naming one contact, however small: "
            "the practice trains the mind's prior on connection "
            "instead of absence. None of these require "
            "confidence, charisma, or a personality transplant. "
            "They require a calendar and repetition. The alarm "
            "is answered by evidence, and evidence is built one "
            "kept appointment at a time."),
        "how_it_works": (
            "The practices work through evidence and bypass. "
            "Recurring appointments bypass the bid-failure "
            "mechanism structurally: the decision to attend was "
            "made once, long ago, so the heavy-phone negotiation "
            "never runs. Weak-tie greetings work through the "
            "belonging math: felt connection sums over many "
            "small contacts, and a dozen named hellos a week is "
            "a real quantity of perceived membership. The three "
            "threads work through maintenance economics: "
            "relationships decay without contact, and three is "
            "few enough to maintain honestly. Outdoor movement "
            "works through two channels at once - physiological "
            "(clearing the fatigue and tension of the body "
            "triad) and social (ambient proximity, the "
            "possibility-space of encounters). Volunteering "
            "works through task-mediated contact: the shared "
            "job gives the guarded person a role to inhabit "
            "and a reason to be there besides wanting company, "
            "which lowers the exposure the defense fears. The "
            "evening naming works through prior-updating: the "
            "mind that logs one contact daily gradually "
            "recalibrates its estimate of how connected the "
            "person actually is. Together they are a system, "
            "not tips: each practice feeds the others, and the "
            "compound interest is a life with the gap mostly "
            "closed."),
        "key_points": [
            "One recurring thing beats ten spontaneous plans: standing appointments bypass the bid-failure negotiation.",
            "Named greetings are micro-contacts; weak ties punch far above their weight in felt belonging.",
            "Keep three threads alive - few enough to maintain honestly, enough that no reopening is ever needed.",
            "Volunteering gives task-mediated contact: a role to inhabit and a reason besides wanting company.",
            "Name one contact each evening: the practice retrains the mind's prior from absence to connection.",
        ],
        "requirements": [
            "At least six concrete practices named, each with its mechanism.",
            "The recurring-beats-spontaneous principle explained via bid-failure bypass.",
            "Weak ties included with the belonging-math justification.",
            "The three-thread rule justified via maintenance economics.",
            "The compound-interest close: practices as a system, not tips.",
        ],
        "standards": [
            "All practices are general, safe, everyday habits - ordinary life guidance, not clinical prescription.",
            "The weak-ties claim follows the social-connection literature (Granovetter's strength of weak ties, applied).",
            "No practice requires disclosure of the feeling; all work without any confession.",
        ],
        "citations": [
            "Granovetter MS. The strength of weak ties. Am J Sociol. 1973;78(6):1360-1380.",
            "Masi CM et al. A meta-analysis of interventions to reduce loneliness. Pers Soc Psychol Rev. 2011;15(3):219-266.",
            "Cacioppo JT, Patrick W. Loneliness: Human Nature and the Need for Social Connection. New York: Norton; 2008.",
        ],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "reading_signs",
        "name": "Reading the Signs: Face, Body, Voice, and Behavior Cues in Others",
        "group": "Recognizing It in Others",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Spotting loneliness in others is a kindness skill, "
            "and it reads across four channels at once. The face: "
            "the dimmed downcast eyes inside the bright social "
            "smile, the millimeter brow lift that never quite "
            "relaxes, the laugh that leaves the eyes out of it. "
            "The body: the edge-and-doorway positioning at "
            "gatherings, the early exits, the phone that comes "
            "out mid-conversation like a shield. The voice: the "
            "flat trailing tone, the I'm fine delivered too fast, "
            "the boomerang questions that keep every topic pointed "
            "away from them. The behavior: the cancellations with "
            "thin reasons, the invitations accepted but never "
            "issued, the overlong hug at goodbye, the person who "
            "is always the listener and never the teller. No "
            "single cue means anything - the tired parent and the "
            "lonely neighbor share half these signs. The read "
            "comes from the pattern across channels plus the "
            "context: the new-in-town coworker, the recently "
            "widowed neighbor, the friend whose group chat went "
            "quiet. And the golden rule of this skill: the read "
            "is never announced. You do not tell someone they "
            "look lonely - that is the shame-tax collected out "
            "loud. You use the read silently, as targeting data "
            "for the next record's responses: the second "
            "invitation, the slower question, the specific plan. "
            "Recognition is reconnaissance for kindness, not a "
            "diagnosis delivered to the subject."),
        "how_it_works": (
            "The skill works through pattern-plus-context "
            "matching. Each channel carries weak signal alone - "
            "the flat tone could be fatigue, the early exit "
            "could be an early meeting - but the channels are "
            "not independent: the same underlying state (the "
            "gap plus the defense) drives all four, so their "
            "co-occurrence is the signal. Context multiplies "
            "it: the cues in a new arrival, a recent loser of "
            "a bond, or someone in a life-stage transition "
            "read far stronger than the same cues in a "
            "well-connected regular. The never-announce rule "
            "is structural, not just polite: announcing the "
            "read triggers the shame-tax and the hiding "
            "repertoire, which destroys the very openness the "
            "recognition was for. Silent use preserves the "
            "person's dignity and keeps the door open for the "
            "supportive responses to work. This is also why "
            "the skill is framed as reconnaissance: its "
            "output is not a label but a targeting solution - "
            "who needs the second invitation, who needs the "
            "slower question, who needs the specific plan. "
            "Trained this way, recognition becomes one of the "
            "most useful social instruments an ordinary person "
            "can carry."),
        "key_points": [
            "Four channels: dimmed eyes in the bright smile, edge positioning, flat trailing voice, canceled-but-never-issuing behavior.",
            "No single cue means anything; the read is the co-occurrence across channels plus the context.",
            "Context multiplies: the same cues read far stronger in the new arrival or the recently bereaved.",
            "The golden rule: the read is never announced - announcing it collects the shame-tax out loud.",
            "Recognition is reconnaissance for kindness: its output is a targeting solution, not a label.",
        ],
        "requirements": [
            "At least three concrete cues per channel across face, body, voice, and behavior.",
            "The weak-signal-alone principle stated with the co-occurrence rule.",
            "Context multipliers named: new arrival, recent loss, life-stage transition.",
            "The never-announce rule justified structurally (shame-tax, hiding repertoire).",
            "The reconnaissance framing: output as targeting solution for supportive responses.",
        ],
        "standards": [
            "The skill is explicitly framed as kindness reconnaissance, never as diagnosis or labeling of any person.",
            "All cues are described as observable patterns any person might show; no one is pathologized.",
            "The never-announce rule is absolute in this record.",
        ],
        "citations": [
            "Ekman P, Friesen WV. Unmasking the Face. Englewood Cliffs: Prentice-Hall; 1975.",
            "Cacioppo JT, Patrick W. Loneliness: Human Nature and the Need for Social Connection. New York: Norton; 2008.",
            "Goffman E. The Presentation of Self in Everyday Life. New York: Doubleday; 1959.",
        ],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "supportive_responses",
        "name": "What to Say and Do When Someone Near You Is Feeling This",
        "group": "Recognizing It in Others",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Responding well to someone's loneliness is a craft "
            "of small, specific moves. First, invite specifically: "
            "not let us hang out sometime but I'm getting tacos "
            "Thursday, come with me. Vague invitations die in the "
            "lonely person's negotiation with themselves; "
            "specific ones bypass it - the decision is small, the "
            "plan is real, the yes is easy. Second, invite twice: "
            "the first decline is often the defense, not the "
            "person. A warm, pressure-free second ask - no "
            "worries if not, but the offer stands Thursday - "
            "tells the hypervigilant mind that the door is "
            "actually open. Third, ask the second question: when "
            "I'm fine arrives too fast, follow with a slower one "
            "- how has the week actually been - and then do the "
            "hard part, which is listening without fixing. Fourth, "
            "offer structured contact: the recurring walk, the "
            "standing game night, the shared task. Structure "
            "carries the relationship past the weeks when "
            "spontaneity fails. Fifth, include visibly: the "
            "introduced-by-name at the gathering, the chair "
            "pulled out, the inside joke explained instead of "
            "laughed over. Lonely people watch for evidence of "
            "membership; make the evidence unmistakable. What "
            "runs under all five is steadiness: show up when "
            "you said you would, text back, remember the thing "
            "they told you. The hypervigilant mind is running "
            "a trust audit at all times, and steadiness is the "
            "only currency it accepts."),
        "how_it_works": (
            "Each move works by defeating one specific defense. "
            "Specific invitations defeat bid-failure-by-proxy: "
            "the lonely person struggles to initiate, so the "
            "other person does the initiating work for them, "
            "reducing the yes to a single low-cost decision. "
            "The second invitation defeats the defense's first "
            "veto: the initial decline was preemption, and a "
            "pressure-free re-ask proves the door was real, "
            "updating the rejection prior with disconfirming "
            "data. The second question defeats the closer: I'm "
            "fine ends the topic at the politeness layer, and "
            "the slower follow-up reopens it at the honesty "
            "layer, while listening-without-fixing avoids the "
            "advice reflex that makes the speaker feel like a "
            "problem. Structured contact defeats spontaneity "
            "decay: the standing plan survives the weeks when "
            "neither party feels like organizing. Visible "
            "inclusion defeats the membership doubt directly: "
            "the lonely mind scans for evidence of belonging, "
            "and unmistakable evidence is the fastest updater. "
            "Steadiness underwrites all of it because trust "
            "audits compound: each kept promise is a deposit, "
            "and the account must stay positive for the "
            "defense to stand down."),
        "key_points": [
            "Invite specifically: I'm getting tacos Thursday beats let us hang out sometime - small decision, real plan.",
            "Invite twice: the first decline is often the defense; a pressure-free re-ask proves the door is real.",
            "Ask the second, slower question - then listen without fixing; the advice reflex makes people feel like problems.",
            "Offer structured contact: standing plans survive the weeks when spontaneity fails.",
            "Include visibly and stay steady: the trust audit accepts only kept promises as currency.",
        ],
        "requirements": [
            "At least five concrete supportive moves, each with a worked example phrase.",
            "Each move paired with the specific defense it defeats.",
            "The vague-vs-specific invitation contrast explained via the initiation burden.",
            "The listening-without-fixing rule stated with the advice-reflex warning.",
            "Steadiness framed as the currency of the trust audit.",
        ],
        "standards": [
            "All guidance is ordinary interpersonal kindness - not counseling, not intervention, not clinical.",
            "No move requires the other person's disclosure; all work without any confession.",
            "The pressure-free qualifier on re-invitation is explicit: persistence must never become pressure.",
        ],
        "citations": [
            "Cacioppo JT, Patrick W. Loneliness: Human Nature and the Need for Social Connection. New York: Norton; 2008.",
            "Masi CM et al. A meta-analysis of interventions to reduce loneliness. Pers Soc Psychol Rev. 2011;15(3):219-266.",
            "Weiss RS. Loneliness: The Experience of Emotional and Social Isolation. Cambridge MA: MIT Press; 1973.",
        ],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "mistakes",
        "name": "What NOT to Do: The Common Mistakes That Make It Worse",
        "group": "Recognizing It in Others",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Good intentions misfire in predictable ways around "
            "loneliness, and the misfires all share a shape: they "
            "answer a different feeling than the one present. "
            "Minimizing - you have so many friends, you are "
            "never alone - disputes the person's perceived "
            "reality, and disputed reality does not feel argued "
            "with, it feels unseen; the gap stays and now the "
            "person is alone with it. Pitying - oh you poor "
            "thing - collects the shame-tax out loud and "
            "positions the helper above the helped, which is the "
            "opposite of membership. Advice-bombing - you should "
            "join a club, just put yourself out there - treats "
            "the feeling as a logistics problem and the person "
            "as a project; the lonely already know the "
            "logistics, it is the doing that the defense vetoes. "
            "Forced cheer - cheer up, it is a beautiful day - "
            "asks the person to perform fine for the helper's "
            "comfort, which is the hiding repertoire with an "
            "audience of one. Interrogating - but why are you "
            "lonely, what happened - demands an account the "
            "person may not have, turning a feeling into a "
            "testimony. Comparing - I was lonely once and I "
            "just... - relocates the spotlight to the helper. "
            "And the quietest mistake: the one-time grand "
            "gesture instead of steady small presence - the "
            "surprise party that overwhelms, then silence for a "
            "month. The audit is simple: before any move, ask "
            "whether it gives the person evidence of membership "
            "or evidence of being managed. Membership heals; "
            "management, however loving, does not."),
        "how_it_works": (
            "Each mistake works by misattuning to the alarm's "
            "actual message. Minimizing misattunes by denying "
            "the perceived gap; since loneliness lives in "
            "perception, denying the perception denies the "
            "person. Pity misattunes by establishing hierarchy; "
            "the belonging need wants membership among equals, "
            "not rescue from above. Advice-bombing misattunes "
            "by answering the logistics while the blockage is "
            "motivational - the defense vetoes bids, and more "
            "ideas do not disarm a veto. Forced cheer "
            "misattunes by recruiting the person into managing "
            "the helper's discomfort, adding performance cost "
            "to the existing load. Interrogation misattunes by "
            "demanding causal narrative; the feeling often has "
            "no single why, and the demand implies there should "
            "be one. Comparison misattunes by shifting "
            "attentional resources to the helper's story. The "
            "grand-gesture mistake misattunes on dosage: the "
            "hypervigilant system distrusts spikes and trusts "
            "patterns, so one large event updates the prior "
            "less than ten small kept promises. The "
            "membership-vs-management audit works because it "
            "tests every move against the belonging need "
            "itself - the only question the alarm is asking."),
        "key_points": [
            "Minimizing disputes perceived reality; the person ends up alone with the gap instead of argued out of it.",
            "Pity establishes hierarchy; the belonging need wants membership among equals, not rescue from above.",
            "Advice-bombing answers logistics while the blockage is motivational - more ideas do not disarm a veto.",
            "Forced cheer recruits the person into managing the helper's discomfort - performance cost on top of the load.",
            "The audit: does this move give evidence of membership or evidence of being managed? Only membership heals.",
        ],
        "requirements": [
            "At least six distinct mistakes named, each with a quoted example and its mechanism.",
            "Each mistake's misattunement explained: which need it misses and how.",
            "The grand-gesture-vs-steady-presence contrast included with the dosage argument.",
            "The membership-vs-management audit stated as the universal pre-move test.",
            "The tone stays instructive about helpers' behavior, never shaming the helper.",
        ],
        "standards": [
            "Mistakes are framed as predictable misfires of good intentions, never as moral failures.",
            "All guidance concerns ordinary interpersonal conduct, not clinical intervention.",
            "The audit question is framed as a practical test, not a therapeutic tool.",
        ],
        "citations": [
            "Cacioppo JT, Patrick W. Loneliness: Human Nature and the Need for Social Connection. New York: Norton; 2008.",
            "Weiss RS. Loneliness: The Experience of Emotional and Social Isolation. Cambridge MA: MIT Press; 1973.",
            "Masi CM et al. A meta-analysis of interventions to reduce loneliness. Pers Soc Psychol Rev. 2011;15(3):219-266.",
        ],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "neighbors",
        "name": "Related Emotions Map: Neighbors, Opposites, and Close Cousins",
        "group": "Related Emotions and Mixes",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Loneliness sits in a crowded neighborhood, and "
            "telling the neighbors apart is practical, not "
            "academic - each wants a different answer. Solitude "
            "is the friendly cousin: chosen aloneness, full and "
            "restorative. The test is the want - the solitary "
            "person chose the quiet and would not trade it; the "
            "lonely person did not choose and would. Isolation "
            "is the objective cousin: the measurable state of "
            "having few contacts. Isolation can cause "
            "loneliness but they are separable - the hermit may "
            "be isolated and content, the popular student "
            "surrounded and lonely. Aloneness is the neutral "
            "cousin: simply being by oneself, the raw material "
            "that becomes solitude when chosen and loneliness "
            "when unwanted. Homesickness is the geographic "
            "cousin: loneliness aimed at a place and its "
            "people, sharpest in the relocated, usually fading "
            "as the new place accumulates meaning. Grief is the "
            "bereaved cousin, mapped in its own record: mourning "
            "for the gone, where loneliness reports the empty "
            "place. Boredom is the mislabeled cousin: the "
            "restless flat feeling that is sometimes loneliness "
            "in disguise - the person says nothing to do when "
            "the truth is no one to do it with. The opposites: "
            "belonging, the felt sense of membership; "
            "companionship, the easy daily contact; intimacy, "
            "the being-known. The map's use is response-"
            "matching: solitude needs protecting, isolation "
            "needs contacts, homesickness needs roots, grief "
            "needs mourning, boredom-needing-company needs "
            "people not projects - and loneliness needs the "
            "perceived gap closed, whatever its address."),
        "how_it_works": (
            "The map works by separating the objective from the "
            "subjective and the chosen from the imposed. "
            "Isolation is objective and countable; loneliness "
            "is subjective and felt - the two-by-two of "
            "objective/subjective by present/absent gives four "
            "rooms, and people live in all of them. Solitude "
            "versus loneliness is the chosen/imposed axis: same "
            "objective aloneness, opposite felt states, which "
            "proves the feeling is about the want, not the "
            "headcount. Homesickness is loneliness with a "
            "geographic object: the gap is between the place-"
            "embedded network left behind and the thin network "
            "so far, and it resolves through root-building "
            "rather than generic socializing. Grief overlaps "
            "through the shared object of an absent bond but "
            "differs in tense: grief faces the past (what was), "
            "loneliness faces the present (what is missing "
            "now). Boredom overlaps phenomenologically - flat, "
            "restless, time dragging - and the differential "
            "test is the fantasy: the bored person fantasizes "
            "about interesting activity, the lonely person "
            "fantasizes about company. The opposites are not "
            "mere absences: belonging, companionship, and "
            "intimacy are distinct positive states, and each "
            "answers a different kind of gap - the circle, the "
            "daily contact, the being-known."),
        "key_points": [
            "Solitude is chosen aloneness (full); loneliness is unwanted distance - the test is the want.",
            "Isolation is objective and countable; loneliness is subjective and felt - four rooms, people live in all.",
            "Homesickness is loneliness with a geographic object; it resolves through root-building.",
            "Boredom is the mislabeled cousin: the differential test is the fantasy - activity vs company.",
            "The opposites are distinct positives: belonging answers the circle-gap, companionship the daily-gap, intimacy the being-known gap.",
        ],
        "requirements": [
            "At least six neighbors distinguished: solitude, isolation, aloneness, homesickness, grief, boredom.",
            "The chosen/imposed axis stated as the solitude-vs-loneliness separator with the want-test.",
            "The objective/subjective two-by-two stated with all four rooms acknowledged.",
            "The boredom differential test (fantasy content) given as a practical tool.",
            "Three distinct opposites named, each matched to the gap it answers.",
        ],
        "standards": [
            "All distinctions are descriptive and educational; no category is framed clinically.",
            "The grief cross-reference points to the blend record without restating clinical material.",
            "Response-matching is framed as ordinary practical reasoning, not treatment selection.",
        ],
        "citations": [
            "Weiss RS. Loneliness: The Experience of Emotional and Social Isolation. Cambridge MA: MIT Press; 1973.",
            "Perlman D, Peplau LA. Toward a social psychology of loneliness. In: Duck S, Gilmour R, eds. Personal Relationships in Disorder. London: Academic Press; 1981:31-56.",
            "Baumeister RF, Leary MR. The need to belong: desire for interpersonal attachments as a fundamental human motivation. Psychol Bull. 1995;117(3):497-529.",
        ],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "mixes",
        "name": "Emotion Mixes: Loneliness Blended with Four Partners",
        "group": "Related Emotions and Mixes",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Loneliness rarely arrives pure; it blends, and each "
            "blend has its own weather. Loneliness plus joy makes "
            "bittersweet: the wedding where you are genuinely happy "
            "for the couple and hollowed by the empty chair beside "
            "you, the laugh that is real and the ache underneath it "
            "that is real too. Bittersweet is the blend that proves "
            "feelings are not mutually exclusive - the heart holds "
            "both readings of the day at once. Loneliness plus fear "
            "makes social dread: not just the gap but the terror "
            "that the gap is permanent, the party invitation read "
            "as a trial, the future imagined as an endless series "
            "of empty evenings. Dread narrows; the person stops "
            "auditioning for a future they have already decided "
            "against. Loneliness plus anger makes abandonment rage: "
            "the canceled plan is not a disappointment but a "
            "betrayal, the friend's busyness is proof nobody cares, "
            "the want curdles into grievance. Rage feels powerful "
            "next to the ache, which is why the blend is seductive "
            "- but it spends the very goodwill the loneliness "
            "needs. Loneliness plus anticipation makes hopeful "
            "aching: the new city's first week, the reunion "
            "counted down on the calendar, the gap felt sharply "
            "precisely because closing it is imaginable. This is "
            "the kindest blend - the want with a direction, the "
            "alarm with an answer scheduled. Reading blends "
            "matters because the partner changes the handling: "
            "bittersweet wants savoring-with-ache, dread wants "
            "the future re-opened gently, rage wants the "
            "grievance translated back into want, hopeful "
            "aching wants the countdown protected."),
        "how_it_works": (
            "Blends work through signal superposition: two alarms "
            "ring at once and the mind hears the chord, not the "
            "notes. Plutchik's dyad idea - primary emotions "
            "combining into compound states - describes the "
            "structure, even though loneliness itself is a "
            "compound: the blends here are compounds of "
            "compounds, which is why they feel so textured. "
            "Bittersweet works through parallel appraisal: the "
            "event is appraised as good (joy's signal) and as "
            "excluding (loneliness's signal) simultaneously, and "
            "neither appraisal cancels the other. Social dread "
            "works through temporal extension: fear projects "
            "the present gap onto the future, converting a "
            "current state into a predicted fate, which is why "
            "it paralyzes - fates are not acted upon. "
            "Abandonment rage works through attribution: the "
            "gap's cause is assigned to others' failures rather "
            "than to circumstance, converting want into "
            "grievance, which feels stronger but spends social "
            "capital. Hopeful aching works through scheduled "
            "resolution: anticipation gives the gap an end "
            "date, which transforms the alarm from a verdict "
            "into a countdown. The handling follows the "
            "partner: each blend's second emotion is the one "
            "that must be addressed first, because it is the "
            "partner that distorts the loneliness underneath."),
        "key_points": [
            "Bittersweet (loneliness + joy): parallel appraisal - the event is good and excluding at once; neither cancels the other.",
            "Social dread (loneliness + fear): the gap projected onto the future becomes a fate, and fates paralyze.",
            "Abandonment rage (loneliness + anger): want curdled into grievance - feels powerful, spends the goodwill the ache needs.",
            "Hopeful aching (loneliness + anticipation): the gap with an end date - the alarm becomes a countdown.",
            "Handle the partner first: the second emotion is what distorts the loneliness underneath.",
        ],
        "requirements": [
            "Four distinct blends rendered as lived weather, each with a concrete scene.",
            "The Plutchik dyad structure referenced as the descriptive frame.",
            "Each blend's mechanism named: parallel appraisal, temporal extension, attribution, scheduled resolution.",
            "The seductiveness of the rage blend named honestly (power vs cost).",
            "The handle-the-partner-first rule stated as the practical takeaway.",
        ],
        "standards": [
            "Blends are described as common emotional experiences, never as disorders or complexes.",
            "The Plutchik reference is descriptive framing, not a diagnostic system.",
            "All blend scenes use hypothetical persons; no real individual is depicted.",
        ],
        "citations": [
            "Plutchik R. Emotion: A Psychoevolutionary Synthesis. New York: Harper & Row; 1980.",
            "Lazarus RS. Emotion and Adaptation. New York: Oxford University Press; 1991.",
            "Cacioppo JT, Patrick W. Loneliness: Human Nature and the Need for Social Connection. New York: Norton; 2008.",
        ],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "full_simulation",
        "name": "Full Behavioral Simulation: From Trigger Through Peak to Resolution",
        "group": "Related Emotions and Mixes",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Scene one: the trigger. Priya, 29, moves to a new city "
            "for a job she wanted. The first week is logistics - "
            "boxes, keys, the internet installer. The second week "
            "the logistics end, and on a Thursday evening she "
            "realizes she has not had a single unplanned "
            "conversation in twelve days. The gap opens quietly: "
            "expected company (her old circle, three time zones "
            "away) minus actual company (the installer, the "
            "landlord). She feels the twinge and files it under "
            "tired. Scene two: the loop starts. Friday night, "
            "the group chat from home lights up with bar photos. "
            "Contrast does its work - she is happy for them and "
            "hollowed, the bittersweet blend. She types a reply, "
            "deletes it (too needy), sends a short one instead. "
            "The hypervigilance begins: was that reply too short, "
            "did they notice she was not there. She scrolls until "
            "1 am. Scene three: the peak. Three weeks in, a rainy "
            "Sunday. She has canceled a coworker's casual coffee "
            "twice - preemptive decline, the defense's work. The "
            "apartment has texture now, the silence with pressure "
            "against the ears. She stares at her sister's name on "
            "the phone for a full minute and puts it down. The "
            "body triad is running: jaw clenched, sleep broken, "
            "toast for dinner. The peak's lie arrives on schedule: "
            "this is just my life now. Scene four: the refused "
            "link. Monday, the coworker - Maya - tries a third "
            "time, specific this time: tacos Thursday, come with "
            "me. Priya's defense prepares the decline; something "
            "older - the alarm's original instruction - says yes "
            "before the defense finishes. Scene five: the "
            "fading, as a Tuesday. Tacos are fine, not magical. "
            "But Maya introduces her to two people by name, "
            "visible inclusion, and one of them runs a Saturday "
            "hiking group - a recurring thing, the calendar's "
            "bypass around bid-failure. Priya goes. Then goes "
            "again. The hollow fills from the edges: a named "
            "greeting from the barista she now sees weekly, three "
            "threads alive, the evening walk with actual "
            "footsteps nearby. Scene six: the aftershock, two "
            "months later. A song from the old city plays in a "
            "store and the gap flashes - four bars of the old "
            "weather. She feels it, translates it (the song "
            "hurts because those friendships mattered), texts "
            "one of them, and keeps walking beside her new "
            "neighbor. The simulation's thesis, in one line: "
            "the gap opened through contrast and erosion, the "
            "loop manufactured its own evidence, one refused "
            "link starved the cascade, and small kept "
            "appointments rebuilt the perceived world."),
        "how_it_works": (
            "The simulation works as the database's capstone: "
            "every major mechanism from the previous 33 records "
            "appears in its natural habitat, in causal order. "
            "The trigger scene encodes the move-as-classic-"
            "trigger and the quiet onset filed under tired. "
            "The loop scene encodes contrast amplification "
            "(bar photos), the bittersweet blend, bid-"
            "shaping (deleted reply), and the birth of "
            "hypervigilance. The peak scene encodes the "
            "defense's preemptive declines, the body triad, "
            "the heavy-phone moment, and the permanence lie. "
            "The refused-link scene encodes the chain-"
            "breaking principle and the specific-invitation "
            "mechanism from the supportive-responses record - "
            "Maya's tacos Thursday is the second invitation "
            "doing its work. The fading scene encodes the "
            "recurring-appointment bypass, visible inclusion, "
            "weak-tie greetings, and the three threads. The "
            "aftershock encodes associative memory and the "
            "translate-don't-argue rule, with the text sent "
            "instead of the spiral. The arc demonstrates the "
            "database's central claim dynamically: loneliness "
            "is a perceived gap, perception updates on "
            "evidence, and evidence is built one kept "
            "appointment at a time. As a simulator's showcase, "
            "it also models the demo pattern - situation, "
            "intensity, scene-by-scene unfolding to resolution "
            "- that the page's interactive simulator lets "
            "readers run with their own situations."),
        "key_points": [
            "Six scenes in causal order: trigger, loop, peak, refused link, fading, aftershock.",
            "Every major mechanism from the 33 prior records appears in its natural habitat.",
            "Maya's specific second invitation (tacos Thursday) is the refused link that starves the cascade.",
            "The fading is built from the practices record: recurring group, named greetings, three threads.",
            "The thesis: the loop manufactured its own evidence; one refused link plus kept appointments rebuilt the perceived world.",
        ],
        "requirements": [
            "A multi-scene narrative (at least five scenes) walking trigger through peak to resolution.",
            "Named characters, concrete sensory detail, and the internal monologue of the mechanisms.",
            "At least eight prior-record mechanisms visibly encoded in the scenes.",
            "The refused-link moment dramatized as the cascade-breaking turn.",
            "The aftershock included to model the echo-not-relapse principle, ending in forward motion.",
        ],
        "standards": [
            "All characters are fictional; the simulation depicts no real person and diagnoses no one.",
            "The simulation is framed as the archive's showcase teaching piece, descriptive throughout.",
            "No clinical language appears; the arc resolves through ordinary social means.",
        ],
        "citations": [
            "Cacioppo JT, Patrick W. Loneliness: Human Nature and the Need for Social Connection. New York: Norton; 2008.",
            "Weiss RS. Loneliness: The Experience of Emotional and Social Isolation. Cambridge MA: MIT Press; 1973.",
            "Masi CM et al. A meta-analysis of interventions to reduce loneliness. Pers Soc Psychol Rev. 2011;15(3):219-266.",
        ],
        "sig_lens": SIG_LENS,
    },
]
