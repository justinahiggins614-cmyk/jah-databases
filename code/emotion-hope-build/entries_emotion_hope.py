#!/usr/bin/env python3
"""Entries for the Hope Emotion databases (Manon's 16:15 orders, emotion series).

Creates two NEW databases, 34 ladder-ordered records each:

  emotion-hope            - The Hope Emotion Database
                            (public-harvest: real, fact-checked psychology of
                            hope - definition, family placement, intensity,
                            first-person simulation, body signals, facial
                            expression, triggers, behavior, healthy
                            expression, recognition in others, related
                            emotions and mixes, and a full behavioral
                            simulation; descriptive and educational only -
                            never diagnosing real people; standard references
                            Snyder hope theory 2002; Snyder et al. 1991;
                            Lazarus 1999; Averill, Catlin and Chon 1990;
                            Fredrickson 2004; Ekman and Friesen FACS 1978;
                            Plutchik 1980; Russell 1980; Frijda 1986;
                            Scherer 2005; Barrett 2017; APA Dictionary of
                            Psychology)
  emotion-hope-signature  - The Hope Emotion Signature Database
                            (his original Signature Hope Method: hope as the
                            forward signal of the system - the blueprint kept
                            on the bench, the lamp lit ahead of the build;
                            agency the drive gear, pathways the rails, vision
                            the headlamp; src signature, titles suffixed
                            " (Signature Edition)", never presented as
                            authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
non-decreasing; ladder_tier foundations/compounded/advanced); the shard
index is written in ladder order so pages present simple -> compounded ->
complex.

ID prefixes: JAH-EMHO- (public) and JAH-EMHOS- (signature), verified free
in the manifest (zero EMHO hits across all id_prefix values) and zero hits
across all record IDs in jah-databases-data-1 shards.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_emotion_hope.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos. Demo outputs are
cross-checked against entry text during authoring.

Descriptive/educational only: this database describes and simulates the
emotion of hope. It never diagnoses real people, never labels any real
person with an emotional state, and offers only general, safe, everyday
guidance. No clinical language, no diagnostic labels, no religious framing.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature Hope Method: hope "
            "as the forward signal of the system - the blueprint kept on the "
            "bench, the lamp lit ahead of the build; agency the drive gear, "
            "pathways the rails, vision the headlamp. Clearly labeled "
            "Signature-made, never presented as authentic public record.")

CIT_DARWIN = ("Darwin C. The Expression of the Emotions in Man and Animals. "
              "London: John Murray; 1872.")
CIT_FACS = ("Ekman P, Friesen WV. Facial Action Coding System: A Technique "
            "for the Measurement of Facial Movement. Palo Alto: Consulting "
            "Psychologists Press; 1978.")
CIT_EKMAN1999 = ("Ekman P. Basic emotions. In: Dalgleish T, Power MJ, eds. "
                 "Handbook of Cognition and Emotion. Chichester: Wiley; "
                 "1999:45-60.")
CIT_PLUTCHIK = ("Plutchik R. Emotion: A Psychoevolutionary Synthesis. New "
                "York: Harper and Row; 1980.")
CIT_RUSSELL = ("Russell JA. A circumplex model of affect. J Pers Soc Psychol. "
               "1980;39(6):1161-1178.")
CIT_LAZARUS1991 = ("Lazarus RS. Emotion and Adaptation. New York: Oxford "
                   "University Press; 1991.")
CIT_FRIJDA = ("Frijda NH. The Emotions. Cambridge: Cambridge University "
              "Press; 1986.")
CIT_SCHERER = ("Scherer KR. What are emotions? And how can they be measured? "
               "Soc Sci Inf. 2005;44(4):695-729.")
CIT_BARRETT = ("Barrett LF. How Emotions Are Made: The Secret Life of the "
               "Brain. Boston: Houghton Mifflin Harcourt; 2017.")
CIT_APA_HOPE = ("American Psychological Association. APA Dictionary of "
                "Psychology. Hope entry: the expectation that one will have "
                "positive experiences or that a potentially threatening or "
                "negative situation will not materialize or will eventually "
                "result in a favorable state of affairs. Washington DC: APA.")
CIT_SNYDER2002 = ("Snyder CR. Hope theory: rainbows in the mind. Psychol "
                  "Inq. 2002;13(4):252-275.")
CIT_SNYDER1991 = ("Snyder CR, Harris C, Anderson JR, Holleran SA, Irving LM, "
                  "Sigmon ST, et al. The will and the ways: development and "
                  "validation of an individual-differences measure of hope. "
                  "J Pers Soc Psychol. 1991;60(4):570-585.")
CIT_LAZARUS1999 = ("Lazarus RS. Hope: an emotion and a vital coping resource "
                   "against despair. Soc Res. 1999;66(2):653-678.")
CIT_AVERILL = ("Averill JR, Catlin G, Chon KK. Rules of Hope. New York: "
               "Springer-Verlag; 1990.")
CIT_FREDRICKSON2004 = ("Fredrickson BL. The broaden-and-build theory of "
                       "positive emotions. Philos Trans R Soc Lond B Biol "
                       "Sci. 2004;359(1449):1367-1378.")
CIT_IZARD = ("Izard CE. Basic emotions, relations among emotions, and "
             "emotion-cognition relations: a review of the evidence. Psychol "
             "Rev. 1992;99(3):561-565.")

SIG_LENS_DEF = ("The Signature read: hope is the forward signal of the "
                "system. Where public psychology charts the feeling, the "
                "Signature Hope Method treats hope as the lamp lit ahead of "
                "the build - proof the blueprint is still on the bench and "
                "the work continues. Agency is the drive gear, pathways the "
                "rails, vision the headlamp. Every hope record below carries "
                "the same public facts, reframed as his original Signature "
                "engineering of the feeling.")

ENTRIES = [
    # ------------------------------------------------ 1-4 WHAT HOPE IS
    {
        "key": "definition",
        "name": "What Hope Is: A Plain-Language Definition",
        "group": "What the Emotion Is",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Hope is the feeling that a good outcome is possible, even when "
            "it is not certain - the inner sense that the future still holds "
            "an open door. In plain words, hope is the mind leaning forward: "
            "a wanted outcome, a belief that it could happen, and the will "
            "to move toward it. Psychologists describe hope as a "
            "goal-directed emotion with three working parts: goals (what is "
            "wanted), pathways (the routes that could lead there), and "
            "agency (the belief that one can walk those routes). Take away "
            "any one part and the feeling thins - a wish without a route is "
            "daydreaming, a route without the will is just a map. Hope can "
            "be about big things - recovery, a career, a reunion - or small "
            "ones, like a clear sky for a picnic. It is not the same as "
            "blind confidence; hope keeps its eyes open to the odds while "
            "still reaching. Everyone has felt it, because hope is standard "
            "equipment for a creature that plans ahead. This database "
            "describes the emotion from every angle - purely as education "
            "and description. It never diagnoses anyone and never labels "
            "any real person."
        ),
        "how_it_works": (
            "Hope works as a forward appraisal signal paired with a plan. "
            "The mind constantly evaluates the future against what matters: "
            "is there something I want that is not yet settled, and could "
            "it go well? When the appraisal returns yes-possible, the "
            "brain assembles the hope machinery: it holds the goal in view, "
            "sketches one or more pathways toward it, and generates agency - "
            "the felt fuel of I can do this. That machinery is why hope "
            "changes behavior rather than just mood: it does not merely "
            "warm the heart, it organizes action, because a person who "
            "sees routes and feels agency starts walking. Hope also works "
            "as a coping resource: when the present is difficult, hope keeps "
            "the future open instead of closed, which keeps the person "
            "trying. The signal can fire fast, like a spark on hearing good "
            "news, or build slowly as plans take shape. It is social by "
            "nature too: shared hope - a family, a team, a community "
            "carrying the same picture of a better outcome - amplifies the "
            "feeling, because pathways and agency multiply when people "
            "build them together."
        ),
        "key_points": [
            "Hope is the feeling that a good outcome is possible, not certain - the mind leaning forward toward a wanted future.",
            "It has three working parts: goals (what is wanted), pathways (routes that could lead there), and agency (the belief one can walk them).",
            "Hope organizes action, not just mood: seeing routes plus feeling agency makes people start moving.",
            "It works as a coping resource, keeping the future open instead of closed when the present is hard.",
            "Hope is social by nature: shared pictures of a better outcome amplify the feeling.",
        ],
        "requirements": [
            "A plain-language definition that an ordinary reader recognizes from their own life.",
            "The three-part structure stated: goals, pathways, agency.",
            "Clear separation from neighboring states like optimism, wishful thinking, and confidence.",
            "Coverage of both big and small hopes so the definition does not only fit milestones.",
            "A stated educational boundary: description only, never diagnosis of any real person.",
        ],
        "standards": [
            "Three-part structure follows Snyder 2002: hope as goal-directed thinking with pathways and agency.",
            "Coping-resource framing follows Lazarus 1999: hope as an emotion and a vital coping resource against despair.",
            "Dictionary definition follows the APA Dictionary of Psychology hope entry: expectation of positive experiences or favorable outcomes.",
        ],
        "citations": [CIT_APA_HOPE, CIT_SNYDER2002, CIT_LAZARUS1999],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "family",
        "name": "Where Hope Sits in the Emotion Family",
        "group": "What the Emotion Is",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Emotions are organized the way colors sit on a wheel: some are "
            "primaries, some are blends, and each has an address with fixed "
            "neighbors. Hope is a compound emotion, not a primary - it is "
            "built from the primary of anticipation blended with the "
            "pleasant, approachable warmth of the positive family. On "
            "Plutchik's wheel of emotions, the dyad of anticipation plus "
            "joy names itself optimism, and hope lives right beside that "
            "blend: anticipation giving the forward lean, joy giving the "
            "pleasant glow. Its nearest neighbors are anticipation (the "
            "looking-ahead part), optimism (the expecting-good part), "
            "trust (the confidence-in-support part), and interest (the "
            "curiosity that keeps the pathways explored). On Russell's "
            "circumplex, hope sits in the pleasant but low-to-moderate "
            "energy quadrant: pleasant, quietly activated - the opposite "
            "corner from despair, which is unpleasant and low. That address "
            "is practical knowledge: it tells you what hope turns into when "
            "it warms up (optimism, enthusiasm), what it slides into when "
            "the goal disappears (despair, resignation), and which feelings "
            "blend with it most easily (anticipation makes optimism; "
            "gratitude makes a hopeful contentment). It also separates "
            "close cousins: hope wants a specific good outcome that is still "
            "open; optimism expects good outcomes generally; wishful "
            "thinking wants without working."
        ),
        "how_it_works": (
            "The family placement works because emotions are positions in "
            "a space, not isolated flashes. The circumplex gives that space "
            "two axes: pleasantness from unpleasant to pleasant, and energy "
            "from sleepy to activated. Hope's coordinates - pleasant but "
            "gently activated - explain its behavior: pleasantness keeps the "
            "person oriented toward the good outcome, and the moderate "
            "activation supplies enough energy to plan and persist without "
            "the fireworks of ecstasy. Plutchik's wheel adds blend logic: "
            "anticipation at its compass point blends with joy to make "
            "optimism, and hope occupies the neighboring address where "
            "anticipation meets the will to act. The compound nature is why "
            "hope feels layered: you can feel the anticipation part (the "
            "future pulling) separately from the agency part (the will "
            "pushing). Modern constructionist accounts like Barrett's add "
            "that the brain assembles the feeling from body signals, past "
            "experience, and concepts - which is why two people's hope can "
            "feel different while occupying the same address on the map."
        ),
        "key_points": [
            "Hope is a compound emotion - anticipation blended with the pleasant approach-warmth of the positive family, built for goals.",
            "On Plutchik's wheel it sits beside optimism (anticipation plus joy); its neighbors are anticipation, optimism, trust, and interest.",
            "On the circumplex hope is pleasant and gently activated - the opposite corner from despair.",
            "Hope wants a specific good outcome that is still open; optimism expects good outcomes generally; wishful thinking wants without working.",
            "The compound structure is why hope feels layered: the future pulling (anticipation) plus the will pushing (agency).",
        ],
        "requirements": [
            "Placement near Plutchik's optimism dyad: anticipation plus joy, with hope as the neighboring goal-directed compound.",
            "Placement on Russell's circumplex: pleasant, low-to-moderate activation, opposite despair.",
            "Named nearest neighbors and their blending partnerships.",
            "The hope-versus-optimism-versus-wishful-thinking distinction stated plainly.",
            "Acknowledgment of constructionist refinement without dropping the classic map.",
        ],
        "standards": [
            "Blend logic follows Plutchik 1980: the anticipation-plus-joy dyad naming optimism, hope as the neighboring compound.",
            "Quadrant placement follows Russell 1980: valence by arousal coordinates for hope as pleasant, gently activated.",
            "Constructionist refinement follows Barrett 2017: emotions constructed from interoception, experience, and concepts.",
        ],
        "citations": [CIT_PLUTCHIK, CIT_RUSSELL, CIT_BARRETT],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "intensity",
        "name": "Hope at Every Volume: Mild to Intense",
        "group": "What the Emotion Is",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Hope is not one fixed loudness; it is a whole dial. At low "
            "volume it is a faint flicker - a half-formed thought that "
            "things might turn out fine, easy to miss, barely warm. At "
            "middle volume it is steady and working: the goal is named, a "
            "few routes are sketched, and there is real energy behind them "
            "each day. At full volume hope is fierce - a blaze that "
            "reorganizes a life around a goal, keeps a person moving through "
            "setbacks, and fills conversations, plans, and dreams. The same "
            "emotion runs through all three; a flicker and a blaze are "
            "family, not strangers. What changes with volume is mostly the "
            "agency component and the energy behind the pathways: the goal "
            "can be identical while the felt force behind it grows. Knowing "
            "the dial matters because people live at different settings on "
            "different days, and because a faint hope is not a failed hope - "
            "it is the most common kind there is, and flickers have started "
            "more comebacks than blazes. It also matters because intensity "
            "without pathways turns into anxious wanting, while intensity "
            "with good pathways turns into effective striving."
        ),
        "how_it_works": (
            "The volume dial works through the three components. At low "
            "volume, only the goal part is lit: the want is present but "
            "pathways are vague and agency is thin, so hope registers as a "
            "quiet leaning. As volume rises, pathways multiply - the mind "
            "starts generating if-this-then-that routes - and agency "
            "thickens as each small step succeeds, which feeds back into "
            "stronger hope. That feedback loop is the engine of the dial: "
            "pathway success raises agency, agency raises energy, energy "
            "finds more pathways. At full volume the loop runs hot and the "
            "whole system - attention, memory, planning - orients around the "
            "goal, which is why intense hope feels like a reorganization of "
            "life rather than a mood. The dial can also be turned from the "
            "outside: clear information about routes, small early wins, and "
            "supportive others all raise agency and pathway clarity, while "
            "repeated blockage with no new routes drains them."
        ),
        "key_points": [
            "Hope runs on a dial: flicker (quiet leaning), steady (working hope), and blaze (life-reorganizing force) - all the same emotion.",
            "What rises with volume is agency and pathway energy; the goal itself can stay identical.",
            "A faint hope is not a failed hope - flickers have started more comebacks than blazes.",
            "The dial runs on a feedback loop: pathway success raises agency, agency raises energy, energy finds more pathways.",
            "Intensity without pathways becomes anxious wanting; intensity with good pathways becomes effective striving.",
        ],
        "requirements": [
            "Three named volume bands with distinct descriptions of each.",
            "The three-component account of what changes across the dial.",
            "The feedback loop between pathway success, agency, and energy stated.",
            "Normalization of low hope as real and common, not defective.",
            "The anxious-wanting versus effective-striving distinction.",
        ],
        "standards": [
            "Component dynamics follow Snyder 2002: pathways and agency thinking interacting with goal pursuit.",
            "Feedback framing follows Lazarus 1991: appraisal-reappraisal cycles shaping emotion intensity.",
            "Measurement framing follows Snyder et al. 1991: agency and pathways as separable, measurable subcomponents.",
        ],
        "citations": [CIT_SNYDER2002, CIT_SNYDER1991, CIT_LAZARUS1991],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "myths",
        "name": "Myths and Misunderstandings About Hope",
        "group": "What the Emotion Is",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Hope collects myths the way attics collect boxes. Myth one: "
            "hope is just wishful thinking. It is not: wishes want without "
            "working, while hope carries pathways and agency - routes and "
            "the will to walk them. Myth two: hope means ignoring reality. "
            "Real hope keeps its eyes open; it is the clear-eyed kind of "
            "reaching that studies the odds and still moves. Myth three: "
            "hope is only for optimists, and pessimists cannot feel it. "
            "Hope is not a personality trait; it is a state that arrives "
            "with a goal and routes, and even habitual worriers feel it "
            "when the machinery assembles. Myth four: hope always makes "
            "things better, so more is always better. Hope without "
            "pathways can stall into rumination, and hope pinned on a "
            "single rigid route can shatter when that route closes - "
            "flexible hope, with backup routes, is the durable kind. Myth "
            "five: losing hope means something is broken in a person. Hope "
            "naturally ebbs when every route looks blocked; the feeling is "
            "reporting the map, not the worth of the traveler. Naming the "
            "myths matters because false rules about hope quietly govern "
            "it: people who believe hope is naive refuse to feel it, and "
            "people who believe it must be loud miss their own quiet "
            "flickers. This record is descriptive education only, not "
            "guidance for any real person's situation."
        ),
        "how_it_works": (
            "Myths work by installing false display rules and false "
            "definitions inside the appraisal machinery. If the mind has "
            "filed hope under naive, then the appraisal of a real hopeful "
            "impulse gets vetoed before it can assemble pathways - the "
            "person talks themselves out of the feeling. If hope is filed "
            "under must-be-loud, then quiet flickers go unrecognized and "
            "unfed, and the person reports having no hope while it is "
            "actually smoldering. Correcting the definition corrects the "
            "machinery: once hope is understood as goals plus pathways plus "
            "agency, a person can check the three parts separately and see "
            "exactly which one is missing - usually it is pathways, not "
            "willpower. That diagnostic clarity is the practical payoff of "
            "myth-busting: it turns I have lost hope into my routes closed "
            "and I need new ones, which is a solvable problem rather than a "
            "verdict on the person."
        ),
        "key_points": [
            "Hope is not wishful thinking: wishes want without working, hope carries pathways and agency.",
            "Real hope keeps its eyes open to the odds; it is clear-eyed reaching, not reality-denial.",
            "Hope is a state that arrives with goals and routes, not a fixed personality trait.",
            "Hope without pathways can stall; hope on a single rigid route can shatter - flexible, multi-route hope is durable.",
            "Losing hope reports the map (routes look blocked), not the worth of the traveler.",
        ],
        "requirements": [
            "At least five named myths with their corrections.",
            "The hope-versus-wishful-thinking mechanism stated through pathways and agency.",
            "The rigid-route versus flexible-routes distinction.",
            "Explanation of how false beliefs about hope govern the feeling itself.",
            "The educational boundary restated: description only, not guidance for any real person.",
        ],
        "standards": [
            "Flexible-pathways framing follows Snyder 2002: high-hope thinking generates multiple routes and reroutes around blockage.",
            "Rules-of-hope framing follows Averill, Catlin and Chon 1990: hope governed by social and cognitive rules that can be examined.",
            "Appraisal framing follows Lazarus 1991: beliefs about an emotion shape the appraisal that produces it.",
        ],
        "citations": [CIT_SNYDER2002, CIT_AVERILL, CIT_LAZARUS1991],
        "sig_lens": SIG_LENS_DEF,
    },
]

ENTRIES += [
    # ------------------------------------------------ 5-9 HOW IT FEELS
    {
        "key": "first_person",
        "name": "Inside Hope: A First-Person Passage",
        "group": "How It Feels",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "From the inside, hope feels like standing at the edge of a map "
            "that is still being drawn. There is a tightness and a "
            "lightness at once: the chest feels a little lifted, the breath "
            "comes a touch deeper, and the eyes want to look up and ahead "
            "rather than down. Thoughts do not race the way they do in "
            "excitement; they step. One thought lays down a possibility, "
            "the next thought tests it, the next one sketches a route "
            "around the obstacle - and each small route that survives the "
            "testing adds a degree of warmth, like a room heating one "
            "degree at a time. There is a particular sensation of time "
            "leaning forward: the future stops being a blank wall and "
            "becomes a corridor with doors, and the body responds as if to "
            "a corridor - shoulders squaring, jaw unclenching, feet almost "
            "ready. Underneath it all runs a quiet hum of agency: not I "
            "will definitely succeed, but I can move, and movement is "
            "allowed. It is a feeling that can coexist with fear, with "
            "grief, with exhaustion - hope does not require the present to "
            "be good, only the future to be open. This is simulation for "
            "education, not a report on any real person."
        ),
        "how_it_works": (
            "The inside of hope works through the three components "
            "rendering as felt experience. Goals render as the forward "
            "lean of attention: the mind keeps returning to the wanted "
            "outcome the way a tongue returns to a sore tooth, except the "
            "touch is pleasant. Pathways render as mental sketching: the "
            "brain runs if-this-then-that simulations, and each surviving "
            "route registers as a small release of tension, because the "
            "future just got more navigable. Agency renders as the hum "
            "underneath: the felt sense of can-do, which is partly body "
            "state (energy available) and partly memory (I have handled "
            "hard things before). Because the machinery is future-directed, "
            "it can run even when the present is painful - the corridor "
            "metaphor is literal in the brain's planning systems, which "
            "treat open futures as navigable space. That is why hope can "
            "coexist with negative feelings about now: the appraisal of "
            "the future and the appraisal of the present are separate "
            "channels."
        ),
        "key_points": [
            "Inside hope feels like standing at the edge of a map still being drawn: tightness and lightness at once, breath deeper, gaze lifting ahead.",
            "Thoughts step rather than race: each possibility tested, each surviving route adding a degree of warmth.",
            "Time leans forward: the future stops being a blank wall and becomes a corridor with doors.",
            "The quiet hum underneath is agency: not certain success, but the sense that movement is allowed.",
            "Hope can coexist with fear, grief, or exhaustion - it only needs the future to be open, not the present to be good.",
        ],
        "requirements": [
            "A sustained first-person-feeling passage written in present-tense sensory language.",
            "Coverage of body sensations, thought patterns, and time perception.",
            "The mapping of goals, pathways, and agency onto felt experience.",
            "Coexistence with negative present feelings stated explicitly.",
            "A simulation disclaimer: education, not a report on any real person.",
        ],
        "standards": [
            "Three-component felt mapping follows Snyder 2002: goals, pathways, and agency as the structure of hope.",
            "Future-oriented appraisal follows Lazarus 1999: hope as the emotion that keeps the future open under stress.",
            "Constructed-experience framing follows Barrett 2017: felt experience assembled from body signals, memory, and concepts.",
        ],
        "citations": [CIT_SNYDER2002, CIT_LAZARUS1999, CIT_BARRETT],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "time_course",
        "name": "How Hope Changes Over Time: Onset, Peak, Fade, Aftershock",
        "group": "How It Feels",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "Hope has a life cycle, and it runs in four movements. Onset "
            "is often quick: a spark when news lands, a door cracks, or a "
            "route appears where there was wall. The spark is small but "
            "noticeable - a lift, a caught breath, the mind suddenly "
            "reaching. Then comes the build: pathways get sketched, plans "
            "form, small steps get taken, and hope grows as each step "
            "succeeds - this is the peak, where the feeling is strongest "
            "and the goal feels almost within reach. After the peak comes "
            "one of two endings. If the goal arrives, hope resolves into "
            "satisfaction and gratitude and then quietly dissolves - its "
            "job done. If the goal slips away, hope fades, sometimes "
            "gently like a tide going out, sometimes sharply when a route "
            "slams shut. And then the aftershock: the memory of the hope "
            "itself lingers. A person can remember having hoped, and the "
            "memory re-warms a little of the feeling - or, if the loss was "
            "fresh, the memory stings. Knowing the cycle matters because "
            "hope is renewable: new information, new routes, or new help "
            "can restart it from a single spark, even after a long fade."
        ),
        "how_it_works": (
            "The time course works through the appraisal machinery "
            "updating its model of the future. Onset fires when the "
            "appraisal shifts from closed to open: new information arrives "
            "(a treatment exists, an application was accepted, someone "
            "offered help) and the future's probability map redraws in a "
            "moment. The build phase runs on the feedback loop - pathway "
            "attempts that succeed raise agency, which raises energy, which "
            "finds more pathways - so hope climbs as long as progress "
            "outruns blockage. Resolution into satisfaction works by goal "
            "discharge: the wanted outcome is achieved, the machinery "
            "stands down, and the lingering warmth is gratitude. Fading "
            "works by route closure: when every sketched pathway is "
            "blocked and no new one appears, the appraisal returns to "
            "closed and the feeling drains. The aftershock works through "
            "memory: episodic memory replays the hopeful state, and the "
            "body partially re-renders it - a faint echo of the corridor "
            "with doors, warm or stinging depending on what followed."
        ),
        "key_points": [
            "Hope runs in four movements: onset (the spark), build (pathways sketched, peak reached), fade or resolution, and aftershock (the memory echo).",
            "Onset is fast: a single piece of news can redraw the future's map in a moment.",
            "The build phase runs on the feedback loop: successful steps raise agency, which finds more pathways.",
            "Resolution into satisfaction discharges the machinery; fading drains it when routes close.",
            "Hope is renewable: new information, new routes, or new help can restart it from one spark.",
        ],
        "requirements": [
            "The four phases named and described: onset, peak/build, fade/resolution, aftershock.",
            "Both endings covered: goal achieved (satisfaction) and goal lost (fading, sharp or gentle).",
            "The feedback-loop mechanism of the build phase stated.",
            "Renewability stated: what restarts hope after a fade.",
            "A memory-echo mechanism for the aftershock phase.",
        ],
        "standards": [
            "Feedback-loop dynamics follow Snyder 2002: pathways and agency interacting during goal pursuit.",
            "Appraisal-update framing follows Lazarus 1991: emotion shifts as the appraisal of the situation updates.",
            "Memory-echo framing follows Frijda 1986: the laws of emotion including the persistence of affective memory.",
        ],
        "citations": [CIT_SNYDER2002, CIT_LAZARUS1991, CIT_FRIJDA],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "low_vs_high",
        "name": "Hope at Low and High Intensity: Two Lived Snapshots",
        "group": "How It Feels",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "Low hope and high hope are the same emotion at two settings, "
            "and they feel like different weather. LOW: It is early "
            "morning, and the thought arrives uninvited - maybe the job "
            "application gets a reply, maybe the test comes back clear. "
            "The feeling is thin, like light under a door. The chest does "
            "not lift; the breath stays shallow; the thought is entertained "
            "for a few seconds and set down. No plans are made. But the "
            "thought keeps returning, a few times a day, and each return "
            "is a little warmer. This is the flicker - quiet, fragile, "
            "real. HIGH: It is the same person three weeks later. The "
            "reply came, the route is real, and now the feeling is a "
            "current. Mornings start with the goal already in mind. "
            "Conversations bend toward it. Setbacks that would have ended "
            "the flicker are now problems to route around - the mind "
            "sketches alternatives before the disappointment has finished "
            "landing. The body runs warmer: sleep is lighter, appetite is "
            "steady, the walk is quicker. The person tells others, and "
            "telling feeds it back. This is the blaze - reorganizing, "
            "contagious, hard to switch off. The two snapshots share the "
            "same structure: a goal, at least one route, a little will. "
            "The difference is how many routes and how much will - and how "
            "the whole system has tilted toward the future."
        ),
        "how_it_works": (
            "The two snapshots work through the same three-component "
            "machinery at different gain. In the low snapshot, only the "
            "goal component is active: the want exists, but pathways are "
            "vague (maybe it works out) and agency is thin, so the system "
            "allocates almost no energy - a few seconds of attention, no "
            "planning. In the high snapshot, all three components run hot: "
            "the goal is specific, multiple pathways are live with backups, "
            "and agency is high from accumulated small wins, so the system "
            "allocates attention, memory, planning, and social behavior "
            "around the goal. The transition between them is the feedback "
            "loop: one answered email (a pathway confirmed) raises agency, "
            "which funds the sketching of the next pathway, which raises "
            "agency again. Contagion matters too: telling others about the "
            "hope recruits their pathways and agency into the loop, which "
            "is why the blaze snapshot includes other people and the "
            "flicker snapshot is solitary."
        ),
        "key_points": [
            "Low hope is the flicker: a thin, returning thought - maybe it works out - with no plans yet, but real.",
            "High hope is the blaze: a current that reorganizes mornings, conversations, and the body's energy around the goal.",
            "Both snapshots share the same structure: goal, at least one route, a little will - the difference is gain.",
            "The transition runs on the feedback loop: one confirmed pathway raises agency, which sketches the next pathway.",
            "The blaze recruits others: shared hope feeds the loop back, which is why high hope is contagious.",
        ],
        "requirements": [
            "Two distinct lived snapshots, one low and one high, written in concrete sensory detail.",
            "The shared three-component structure named beneath both snapshots.",
            "A named transition mechanism between the two settings.",
            "Body and behavior differences across the two settings.",
            "The social dimension of the high snapshot stated.",
        ],
        "standards": [
            "Component-gain framing follows Snyder 2002: agency and pathways thinking varying in strength.",
            "Feedback dynamics follow Snyder et al. 1991: the iterative will-and-ways loop during goal pursuit.",
            "Social amplification framing follows Fredrickson 2004: positive emotional states broadening and building shared resources.",
        ],
        "citations": [CIT_SNYDER2002, CIT_SNYDER1991, CIT_FREDRICKSON2004],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "hope_optimism_blend",
        "name": "Hope Mixed With Optimism: Its Closest Partner",
        "group": "How It Feels",
        "ladder_rank": 5,
        "ladder_tier": "foundations",
        "description": (
            "Hope's most common companion is optimism, and the two blend "
            "so smoothly that people often use one word for both. But the "
            "blend has a texture worth knowing. Pure hope is specific and "
            "working: it has a named goal, sketched routes, and the will "
            "to walk them - it is pointed at something. Pure optimism is "
            "general and expecting: a background belief that things tend to "
            "turn out well, without necessarily a plan. When they mix - "
            "which is most of the time in everyday life - the feeling is "
            "both pointed and sunny: a specific goal carried on a general "
            "faith that effort pays off. The optimism in the blend does "
            "quiet work for the hope: it keeps the person sketching routes "
            "after the third failure, it lowers the felt cost of trying "
            "again, and it makes the waiting periods bearable. The hope in "
            "the blend does work for the optimism too: it gives the sunny "
            "outlook something to do, converting a pleasant expectation "
            "into a plan. Watch the blend at a bedside, in a classroom, on "
            "a team: the optimistic part says this can turn out well, and "
            "the hopeful part says here is what we try next. Together they "
            "are steadier than either alone - optimism without hope is "
            "cheerful passivity, and hope without optimism is grim "
            "determination. The blend is the everyday engine of getting "
            "through hard stretches."
        ),
        "how_it_works": (
            "The blend works because the two emotions supply complementary "
            "parts. Optimism contributes a generalized positive expectancy - "
            "a standing prior that effort tends to be rewarded and futures "
            "tend to improve - which lowers the perceived risk of each new "
            "attempt. Hope contributes the machinery: the specific goal, "
            "the pathway sketches, the agency fuel. In appraisal terms, "
            "optimism sets a favorable base rate for the future, and hope "
            "runs the planning process on top of it. That division of "
            "labor is why the blend is resilient: when a specific pathway "
            "fails, hope's machinery reroutes (Snyder's flexible pathways), "
            "and optimism's base rate keeps the rerouting funded instead of "
            "abandoned. Without the optimism part, repeated failures can "
            "drain the base rate until the machinery stops being built; "
            "without the hope part, the favorable base rate never converts "
            "into action. The blend is also socially transmissible: an "
            "optimistic hopeful person exports both the base rate and the "
            "machinery to others through tone, planning talk, and example."
        ),
        "key_points": [
            "Hope and optimism blend constantly in everyday life; hope is pointed and working, optimism is general and expecting.",
            "In the blend, optimism keeps route-sketching funded after failures; hope gives the sunny outlook something to do.",
            "Optimism without hope is cheerful passivity; hope without optimism is grim determination - together they are the everyday engine.",
            "The blend is resilient: failed pathways reroute while the optimistic base rate keeps the rerouting funded.",
            "The blend is socially transmissible through tone, planning talk, and example.",
        ],
        "requirements": [
            "Pure hope and pure optimism each defined separately before the blend.",
            "What each partner contributes to the blend stated as a division of labor.",
            "The failure modes of each unblended state named.",
            "A concrete setting where the blend is visible.",
            "The social transmissibility of the blend stated.",
        ],
        "standards": [
            "Optimism-expectancy framing follows the general positive-expectancy literature alongside Snyder 2002 on hope.",
            "Blend logic follows Plutchik 1980: neighboring primaries forming named dyads, optimism as anticipation-plus-joy.",
            "Resilience dynamics follow Lazarus 1999: hope as the coping resource that persists under stress.",
        ],
        "citations": [CIT_SNYDER2002, CIT_PLUTCHIK, CIT_LAZARUS1999],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "day_vignette",
        "name": "A Day in the Life of Hope",
        "group": "How It Feels",
        "ladder_rank": 5,
        "ladder_tier": "foundations",
        "description": (
            "Morning: the alarm, and before the feet hit the floor the goal "
            "is already there - the application, the appointment, the "
            "project - sitting in the mind like a lamp left on overnight. "
            "The feeling is mild, a background warmth, and it organizes the "
            "morning: the email gets answered first, the call gets "
            "scheduled, the small preparatory task gets done without "
            "debate. Midday: a setback lands - a delayed reply, a form "
            "rejected, a number that is wrong. The warmth dips. For ten "
            "minutes the corridor narrows to a wall. Then the machinery "
            "kicks in: the mind sketches around the blockage - a different "
            "contact, a corrected form, a recalculated number - and as the "
            "first alternative route takes shape, the warmth returns, a "
            "degree higher for having survived the dip. Afternoon: telling "
            "someone. The hope is spoken aloud over lunch, and the telling "
            "does work: the other person offers a route that had not been "
            "seen, and the shared picture makes the goal feel nearer. "
            "Evening: the day's steps are reviewed, small wins counted, "
            "tomorrow's first step named. The feeling settles into a "
            "steady glow - not excitement, but the quiet confidence of a "
            "machine that is running. Night: falling asleep, the last "
            "thought is not worry but the next step, and the mind rests on "
            "it the way it rests on a solved problem. This is the ordinary "
            "miracle of hope: not a lightning strike, but a current running "
            "quietly under a normal day, organizing it from underneath."
        ),
        "how_it_works": (
            "The day works as a repeated cycle of the three-component "
            "machinery responding to events. Morning activation works "
            "through goal priming: the wanted outcome, held overnight in "
            "memory, re-engages attention on waking and biases the day's "
            "first choices toward pathway steps - which is why hopeful "
            "mornings feel organized without effort. The midday dip and "
            "recovery work through appraisal updating: the setback closes "
            "a route (appraisal: blocked), hope dips, then pathway "
            "generation reopens the map (appraisal: rerouted) and agency "
            "is restored by the act of sketching itself. The afternoon "
            "telling works through social pathway pooling: speaking the "
            "goal recruits another mind's route-finding, and shared "
            "agency is stronger than solitary. The evening review works "
            "through progress accounting: counting small wins converts "
            "the day's effort into agency fuel for tomorrow, and naming "
            "the next step pre-loads the morning's priming. Night rest "
            "works because an open, navigable future is processed by the "
            "brain as safety, which permits the downshift into sleep."
        ),
        "key_points": [
            "A hopeful day runs on quiet machinery: morning goal priming organizes the day's first choices without debate.",
            "Setbacks dip hope by closing routes; recovery comes from sketching around the blockage - the rerouting itself restores agency.",
            "Speaking the hope aloud pools pathways: another mind's route-finding joins the loop.",
            "Evening review converts small wins into agency fuel and pre-loads tomorrow's first step.",
            "Hope at night feels like rest on a solved problem: an open, navigable future reads as safety.",
        ],
        "requirements": [
            "A full day arc from morning through night with hope present in each segment.",
            "A midday setback with the dip-and-recovery cycle shown.",
            "The social moment (telling someone) and its mechanism.",
            "The evening accounting mechanism stated.",
            "The ordinary, non-dramatic character of the day emphasized.",
        ],
        "standards": [
            "Goal-priming framing follows Snyder 2002: goals organizing attention and action across the day.",
            "Appraisal-updating follows Lazarus 1991: emotion tracking the changing appraisal of goal progress.",
            "Progress-accounting follows the pathways-agency feedback loop of Snyder et al. 1991.",
        ],
        "citations": [CIT_SNYDER2002, CIT_LAZARUS1991, CIT_SNYDER1991],
        "sig_lens": SIG_LENS_DEF,
    },
]

ENTRIES += [
    # ------------------------------------------------ 10-13 BODY SIGNALS
    {
        "key": "body",
        "name": "Hope in the Body: Heart, Breath, Muscles, Energy",
        "group": "Body Signals",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Hope lives in the body as a quiet readiness, not a storm. The "
            "heart: steady, sometimes a touch quicker when the goal comes "
            "sharply to mind, but without the pounding of fear or the "
            "racing of excitement - a firm, even beat, like an engine at "
            "idle with the gear engaged. The breath: deeper and slower than "
            "in worry, with a tendency to lengthen the exhale, as if the "
            "body were making room. The muscles: the jaw unclenches, the "
            "shoulders drop and square, the hands open rather than fist - "
            "the classic release of a body that has stopped bracing. The "
            "stomach: the knot of dread loosens; appetite often returns "
            "because the gut is no longer receiving alarm signals. The "
            "skin: warm rather than flushed, sometimes a faint prickle at "
            "the scalp or forearms when hope spikes - the small shiver of "
            "a future suddenly feeling near. Energy: the signature body "
            "signal of hope is available energy - not jittery arousal but "
            "fuel, the felt sense that there is something in the tank for "
            "the next step. Fatigue does not vanish, but it stops being "
            "the whole story. All of this is descriptive of the general "
            "pattern; individual bodies vary, and this record never "
            "diagnoses anyone."
        ),
        "how_it_works": (
            "The body pattern works through the appraisal of the future "
            "as open and navigable. When the brain's planning systems "
            "register available pathways, they down-regulate the threat "
            "machinery: the sympathetic alarm eases, which is why the jaw "
            "unclenches, the shoulders drop, and the stomach unknots - "
            "bracing is expensive, and an open future does not require it. "
            "At the same time, the approach machinery engages at moderate "
            "gain: dopamine-linked anticipation circuits mark the goal as "
            "worth moving toward, which is felt as available energy and the "
            "readiness in the limbs. The breath deepens because the body is "
            "neither fleeing nor freezing; slow exhalation-dominant "
            "breathing is the respiratory signature of a system that feels "
            "safe enough to plan. The warmth in the skin follows from "
            "reduced vasoconstriction as threat eases. None of this is "
            "unique to hope in isolation - contentment shares the calm, "
            "excitement shares the energy - but the combination of calm "
            "body plus forward-leaning energy is hope's bodily fingerprint."
        ),
        "key_points": [
            "Hope's body signature is quiet readiness: steady heart, deeper breath, unclenched jaw, squared shoulders, open hands.",
            "The stomach unknots and appetite often returns as alarm signals ease.",
            "The signature signal is available energy - fuel for the next step, not jittery arousal.",
            "Bracing releases because an open, navigable future does not require the body's threat posture.",
            "The fingerprint is the combination: calm body plus forward-leaning energy.",
        ],
        "requirements": [
            "Coverage of heart, breath, muscles, stomach, skin, and energy.",
            "The bracing-release mechanism tied to the open-future appraisal.",
            "The available-energy signal distinguished from jittery arousal.",
            "The calm-plus-forward fingerprint stated as the distinguishing combination.",
            "The non-diagnostic, general-pattern disclaimer included.",
        ],
        "standards": [
            "Threat down-regulation framing follows Lazarus 1991: appraisal of the situation driving physiological patterning.",
            "Anticipation-circuit framing follows the general affective neuroscience of approach motivation alongside Frijda 1986 on action readiness.",
            "Component-process framing follows Scherer 2005: synchronized bodily changes as part of the emotion episode.",
        ],
        "citations": [CIT_LAZARUS1991, CIT_FRIJDA, CIT_SCHERER],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "posture",
        "name": "The Posture and Movement of Hope",
        "group": "Body Signals",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "You can read hope in how a person carries themselves before "
            "they say a word. The posture of hope is upright but not "
            "rigid: spine tall, shoulders back and level, chest open - the "
            "stance of someone facing something rather than shielding from "
            "it. The head sits level or tilts very slightly up; the gaze "
            "goes forward and slightly up, toward the middle distance where "
            "futures live, rather than down at the feet. Movement under "
            "hope is purposeful and unhurried: the walk has a steady pace "
            "with a slightly lengthened stride, gestures are open-palmed "
            "and measured, and there is a tendency to lean in - toward the "
            "conversation, toward the work, toward the other person. Hands "
            "are busy in a constructive way: sketching, listing, building, "
            "pointing at the map. Even stillness looks different: a hopeful "
            "person at rest sits forward on the chair, alert but easy, "
            "rather than collapsed back or curled in. At high intensity the "
            "movement signature sharpens - quicker steps, more expansive "
            "gestures, a bounce that was not there before. At low intensity "
            "it is subtler: just the head a fraction higher, just the "
            "stride a fraction longer. Actors and artists take note: hope "
            "is played in the vertical axis - up, forward, open - never in "
            "collapse."
        ),
        "how_it_works": (
            "The posture works as both signal and tool. As a signal, the "
            "upright open posture broadcasts navigability to others: this "
            "person sees routes and has fuel, which recruits help and "
            "cooperation - humans read posture fast and unconsciously. As "
            "a tool, the posture feeds back into the feeling itself: "
            "expansive upright postures are associated with greater "
            "feelings of agency and approach motivation, so standing tall "
            "literally helps keep the hope machinery running. The forward "
            "gaze direction works through attention: where the eyes go, "
            "planning follows, and a gaze aimed at the middle distance "
            "keeps the future in the attentional frame. The constructive "
            "hand activity works as pathway sketching made visible - the "
            "body externalizing the mind's route-finding, which both "
            "records the routes and strengthens them. The intensity "
            "scaling works through energy availability: more agency fuel "
            "means more movement amplitude, so the bounce and the "
            "expansive gestures are honest readouts of the system's "
            "charge."
        ),
        "key_points": [
            "Hope's posture is upright but not rigid: tall spine, level shoulders, open chest, head level or slightly up.",
            "The gaze goes forward and slightly up, toward the middle distance where futures live.",
            "Movement is purposeful and unhurried: steady pace, open-palmed gestures, leaning in.",
            "Posture is both signal (broadcasting navigability to others) and tool (feeding agency back into the feeling).",
            "Hope is played on the vertical axis - up, forward, open - never in collapse.",
        ],
        "requirements": [
            "Posture described joint by joint: spine, shoulders, chest, head, gaze.",
            "Movement described: walk, gestures, hand activity, stillness.",
            "The signal-and-tool dual function stated.",
            "Intensity scaling of the movement signature.",
            "The vertical-axis rule for artists and actors.",
        ],
        "standards": [
            "Posture-signal framing follows Darwin 1872: emotional expression as communicative bodily habit.",
            "Feedback framing follows the embodied-emotion literature alongside Frijda 1986 on action readiness shaping experience.",
            "Component-process framing follows Scherer 2005: motor expression as one synchronized component of the episode.",
        ],
        "citations": [CIT_DARWIN, CIT_FRIJDA, CIT_SCHERER],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "sleep_appetite",
        "name": "Sleep, Appetite, and Energy Under Hope",
        "group": "Body Signals",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Hope rearranges the body's maintenance systems in its favor. "
            "Sleep: the classic effect is easier falling-asleep, because "
            "the mind's last loops are plans rather than alarms - the "
            "future is being sketched, not dreaded, and sketching is "
            "soporific in the way that worry is not. Dreams may carry the "
            "goal forward in symbolic form. At very high intensity the "
            "pattern can flip: the blaze of hope keeps the mind sketching "
            "past bedtime, and sleep gets lighter and shorter for a few "
            "nights - not from distress but from momentum. Appetite: with "
            "threat eased, the gut settles and hunger returns to its normal "
            "rhythm; meals get eaten with attention instead of skipped or "
            "bolted. Some people eat a little more, savoring, because the "
            "future tastes good. Energy: this is hope's home territory. "
            "Available energy rises - mornings feel startable, stairs feel "
            "climbable, the day's tasks feel liftable. It is not manic "
            "energy; it does not jitter or crash. It is the steady fuel of "
            "a system that believes its efforts go somewhere, and it is "
            "why hopeful people so often look, to others, simply more "
            "alive. When hope fades, these systems are the first witnesses: "
            "sleep thins, food loses savor, the stairs get heavy again - "
            "the body's honest ledger of the feeling."
        ),
        "how_it_works": (
            "The maintenance effects work through the threat/appetitive "
            "balance. Sleep eases because the pre-sleep appraisal is open "
            "rather than closed: a mind sketching navigable futures does "
            "not trigger the vigilance that keeps worriers awake, so sleep "
            "onset shortens and depth holds. The high-intensity flip works "
            "through approach arousal: strong agency plus active pathway "
            "sketching raises cognitive arousal past the sleep threshold, "
            "the same mechanism as excitement keeping anyone up - "
            "momentum, not distress. Appetite normalizes because the gut "
            "is downstream of threat: when alarm signals ease, digestive "
            "rhythm resumes and the reward of food is processed cleanly "
            "instead of through a filter of dread. Energy rises because "
            "agency is literally the felt sense of available resources; a "
            "brain that models the future as navigable releases effort "
            "willingly, and the body reads that willingness as fuel. The "
            "ledger effect works in reverse too: when routes close, the "
            "appraisal flips to closed, threat rises, and sleep, appetite, "
            "and energy all report the change before the person has named "
            "it."
        ),
        "key_points": [
            "Sleep usually eases under hope: the mind's last loops are plans, not alarms - sketching is soporific where worry is not.",
            "At very high intensity the pattern can flip: momentum keeps the mind sketching past bedtime for a few nights.",
            "Appetite normalizes as threat eases: the gut settles, meals are eaten with attention.",
            "Available energy is hope's home territory: steady fuel, not jitter - mornings feel startable.",
            "Sleep, appetite, and energy are the body's honest ledger: they report hope's fading before the mind names it.",
        ],
        "requirements": [
            "Sleep, appetite, and energy each covered with the hope-on and hope-fading directions.",
            "The high-intensity sleep flip explained as momentum, not distress.",
            "The threat/appetitive balance mechanism stated.",
            "The ledger metaphor: maintenance systems as early reporters.",
            "Everyday, non-clinical language throughout.",
        ],
        "standards": [
            "Threat-sleep linkage follows Lazarus 1991: appraisal driving physiological readiness states.",
            "Energy-as-agency framing follows Snyder 2002: agency thinking as the felt sense of available resources.",
            "Component-process framing follows Scherer 2005: neurophysiological symptoms as one emotion component.",
        ],
        "citations": [CIT_LAZARUS1991, CIT_SNYDER2002, CIT_SCHERER],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "individual_diff",
        "name": "How Hope Feels Different in Different Bodies",
        "group": "Body Signals",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "No two bodies run hope on the same hardware. Some people feel "
            "hope high in the body - a lift behind the sternum, a lightness "
            "in the throat, the urge to look up. Others feel it low - a "
            "settling in the belly, a steadiness in the legs, the sense of "
            "ground under the plan. Some run hot: hope arrives with warmth "
            "spreading outward, cheeks flushed, hands warm. Some run cool: "
            "hope arrives as clarity, a quieting of noise, the mind's "
            "surface going glassy and still. Expressive people wear it on "
            "the outside - the face lights, the voice lifts, the body "
            "announces. Reserved people carry it inside - the same "
            "machinery, but the dials face inward, and you would need to "
            "know them well to see the straightened spine or the longer "
            "gaze. Age shades it too: the young often feel hope as "
            "electricity and speed, the old as depth and steadiness - both "
            "real, both hope. Temperament matters: the cautious feel hope "
            "tentatively, testing each route twice; the bold feel it all "
            "at once, routes sketched in broad strokes. None of these is "
            "the correct way to feel hope. The machinery - goal, pathways, "
            "agency - is the same; the rendering is personal. This record "
            "describes variation only and never sorts any real person into "
            "a type."
        ),
        "how_it_works": (
            "The variation works through three filters. First, "
            "interoceptive style: people differ in how finely they sense "
            "internal body signals, so the same moderate arousal renders "
            "as a vivid chest-lift in one person and as a vague sense of "
            "okayness in another - the signal is the same, the display "
            "resolution differs. Second, expressive habit: display rules "
            "learned across a lifetime set how much of the feeling reaches "
            "the face, voice, and posture, so reserved carriers and "
            "expressive wearers can run identical hope machinery at "
            "identical gain with completely different visibility. Third, "
            "conceptual repertoire: the brain constructs the feeling from "
            "past experience and available concepts, so a person whose "
            "history taught them that hope is dangerous (hopes dashed "
            "before) will construct a more tentative, tested version than "
            "someone whose history taught them that hope pays. Age shades "
            "the rendering through accumulated evidence: more years mean "
            "more data on which routes tend to work, which shifts the "
            "felt texture from electric to steady without changing the "
            "components."
        ),
        "key_points": [
            "Some feel hope high (chest lift, throat lightness); others feel it low (belly settling, leg steadiness) - same machinery, different rendering.",
            "Some run hot (warmth spreading); some run cool (clarity, mental stillness).",
            "Expressive people wear hope outside; reserved people carry identical machinery with the dials facing inward.",
            "The cautious test each route twice; the bold sketch in broad strokes - temperament shades the texture, not the structure.",
            "No rendering is the correct one; variation is described, never used to sort real people.",
        ],
        "requirements": [
            "At least four axes of variation: body location, temperature, expressiveness, and age or temperament.",
            "The same-machinery-different-rendering principle stated.",
            "The three-filter mechanism: interoception, expressive habit, conceptual repertoire.",
            "No rendering presented as correct or superior.",
            "The non-sorting disclaimer: variation described, never applied to real people.",
        ],
        "standards": [
            "Constructionist framing follows Barrett 2017: the brain assembling emotion from interoception, experience, and concepts.",
            "Display-rule framing follows Ekman and Friesen 1978: learned rules shaping expressive visibility.",
            "Individual-differences framing follows Snyder et al. 1991: stable differences in agency and pathways thinking.",
        ],
        "citations": [CIT_BARRETT, CIT_FACS, CIT_SNYDER1991],
        "sig_lens": SIG_LENS_DEF,
    },
    # ------------------------------------------------ 14-17 FACIAL EXPRESSION
    {
        "key": "face",
        "name": "The Face of Hope: Eyes, Brows, Mouth, and Micro-Signs",
        "group": "Facial Expression",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "The face of hope is quieter than the face of joy, but it is "
            "unmistakable once you know it. The eyes: the signature feature "
            "is the lifted gaze - eyes aimed slightly up and forward, with "
            "a soft focus rather than a hard stare, as if looking at "
            "something just beyond the present. The upper eyelids may raise "
            "a fraction, widening the eye - the look of taking in a wider "
            "horizon. The brows: raised slightly and evenly, the classic "
            "forehead of attention and openness - not the sharp arch of "
            "surprise, but a gentle lift, sometimes with the inner corners "
            "a touch higher, giving the face an listening quality. The "
            "mouth: a soft, closed-lip smile or even just the easing of "
            "the mouth's downward pull - the corners neither grinning nor "
            "drooping, but released. In the Facial Action Coding System "
            "this reads as a mild combination: slight brow raise (AU 1+2 "
            "at low intensity) plus a soft lip-corner pull (AU 12 at low "
            "intensity), with none of the cheek-raising (AU 6) of a full "
            "Duchenne smile. The micro-signs: a brief parting of the lips "
            "as if about to speak the plan; a single slow nod, almost "
            "imperceptible, as the mind confirms a route; a momentary "
            "stillness of the whole face - the sketching pause - when a new "
            "pathway clicks into place. The overall impression is of a "
            "face turned toward the future: open, attending, faintly lit "
            "from within."
        ),
        "how_it_works": (
            "The face works as a readout of the three-component machinery. "
            "The lifted gaze and raised brows render the goal and "
            "pathway components: attention aimed at the future, the visual "
            "system literally widening to take in more of the horizon - "
            "the face mirroring the mind's corridor-with-doors. The soft "
            "mouth renders the pleasant appraisal: no threat, no bracing, "
            "so the mouth releases its defensive set. The low-intensity "
            "AU 1+2 plus AU 12 combination is the muscular truth of "
            "quiet readiness: just enough lift to show engagement, not "
            "enough to signal celebration. The micro-signs render "
            "machinery events in real time: the lip parting is speech "
            "preparation as the plan forms words; the slow nod is the "
            "body's confirmation stamp on a surviving route; the "
            "sketching pause is attention narrowing onto the internal "
            "simulation while the face idles. Because the expression is "
            "low-amplitude, it is easily missed - which is why hopeful "
            "people are so often misread as merely calm, and why the "
            "recognition record in this database teaches the quiet tells."
        ),
        "key_points": [
            "The signature is the lifted gaze: eyes slightly up and forward with soft focus, as if looking just beyond the present.",
            "Brows raise slightly and evenly - openness and attention, not the sharp arch of surprise.",
            "The mouth softens to a closed-lip ease: lip corners released, neither grinning nor drooping (low AU 12, low AU 1+2, no AU 6).",
            "Micro-signs: the lip parting as the plan forms words, the slow confirming nod, the sketching pause when a route clicks.",
            "The overall impression: a face turned toward the future - open, attending, faintly lit from within.",
        ],
        "requirements": [
            "Eyes, brows, and mouth each described with specific muscular detail.",
            "FACS action units named for the core combination.",
            "At least three micro-signs described with their machinery meanings.",
            "The low-amplitude character of the expression and its misread risk.",
            "A one-line overall impression for quick recognition.",
        ],
        "standards": [
            "FACS coding follows Ekman and Friesen 1978: AU 1+2 brow raise and AU 12 lip-corner pull at low intensity.",
            "Expression-as-readout framing follows Darwin 1872: facial expression as the visible edge of inner states.",
            "Component mapping follows Scherer 2005: motor expression synchronized with appraisal and physiology.",
        ],
        "citations": [CIT_FACS, CIT_DARWIN, CIT_SCHERER],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "face_intensity",
        "name": "The Face of Hope at Every Volume",
        "group": "Facial Expression",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Hope's face changes with the dial, and each setting has its "
            "tells. At low volume - the flicker - the face barely moves: "
            "the only signs are a fractional lift of the inner brows and "
            "a gaze that drifts up and away for a second, as if checking "
            "something on the horizon. The mouth stays neutral. A "
            "stranger would see nothing; someone who knows the person "
            "would see the drift. At middle volume - steady working hope - "
            "the full quiet signature appears: brows gently raised, eyes "
            "softly widened and forward, the closed-lip ease of the "
            "mouth, and the slow confirming nod when plans land. This is "
            "the readable face of hope, the one the recognition record "
            "teaches. At high volume - the blaze - the face brightens "
            "toward joy's territory: the smile widens and the cheeks begin "
            "to engage, the eyes shine (tears held back or simply bright "
            "with arousal), gestures join the face, and the whole head may "
            "lift and turn as if addressing the future directly. The "
            "sketching pauses get shorter because routes are coming fast. "
            "One caution: at high volume the face of hope can look like "
            "the face of joy or excitement, and it often is blending with "
            "them - pure high hope without any joy in it is rare. Reading "
            "the dial means reading amplitude: how far the brows travel, "
            "how wide the mouth opens, how much of the body joins the "
            "face. Amplitude is the volume knob made visible."
        ),
        "how_it_works": (
            "The intensity scaling works through motor gain following "
            "agency gain. At low volume, agency is thin, so the motor "
            "system allocates almost nothing: only the gaze drift and the "
            "inner-brow fraction, which are the cheapest possible "
            "readouts of future-directed attention. At middle volume, "
            "agency funds the full quiet signature: the brow raise, the "
            "eye widening, the mouth ease, the nod - each a low-cost "
            "movement that tracks a live component (attention, appraisal, "
            "confirmation). At high volume, the approach system is fully "
            "engaged and the face borrows from its high-arousal neighbors: "
            "cheek engagement and wider smiles from joy's repertoire, eye "
            "shine from autonomic arousal, head movement from the urge to "
            "share and act. The blending at high volume is structural, "
            "not accidental: hope at full gain recruits the same approach "
            "circuits as joy and excitement, so the faces converge. That "
            "is why amplitude-reading is the practical skill: the "
            "components are the same at every setting, and only the gain "
            "changes - so the trained eye reads how far, not just what."
        ),
        "key_points": [
            "Low volume: only a fractional inner-brow lift and a gaze drifting up - visible only to those who know the person.",
            "Middle volume: the full quiet signature - gently raised brows, softly widened eyes, closed-lip ease, the confirming nod.",
            "High volume: the face brightens toward joy's territory - wider smile, cheek engagement, shining eyes, the head addressing the future.",
            "At high volume hope structurally blends with joy and excitement; pure high hope without joy is rare.",
            "The practical skill is reading amplitude: how far the features travel is the volume knob made visible.",
        ],
        "requirements": [
            "Three volume bands with distinct facial descriptions.",
            "The low-volume subtlety and its misread risk.",
            "The high-volume convergence with joy's face explained structurally.",
            "Amplitude as the reading skill stated plainly.",
            "FACS-level detail at least for the middle band.",
        ],
        "standards": [
            "Motor-gain framing follows Frijda 1986: action readiness scaling with emotion intensity.",
            "FACS detail follows Ekman and Friesen 1978: graded action-unit intensity.",
            "Convergence framing follows Russell 1980: neighboring high-arousal pleasant states sharing expressive features.",
        ],
        "citations": [CIT_FRIJDA, CIT_FACS, CIT_RUSSELL],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "hiding_faking",
        "name": "Hiding or Faking Hope: What Leaks Through",
        "group": "Facial Expression",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "People hide hope more often than you would think - usually to "
            "avoid disappointment being witnessed, or to avoid looking "
            "naive. The hidden-hope face is a study in suppression: the "
            "mouth is held neutral by deliberate effort, the brows are "
            "kept level, the gaze is forced down or to the side. But "
            "suppression is leaky. What escapes: the gaze keeps drifting "
            "up despite the effort, because future-directed attention is "
            "hard to leash; the inner brows lift for a fraction of a "
            "second when the goal is mentioned - the micro-expression of "
            "the corridor opening; the breathing deepens audibly once, the "
            "body's quiet yes slipping past the guard. Faking hope - "
            "performing it for others without feeling it - leaks in the "
            "opposite direction. The performed face overdoes the easy "
            "parts: a bright fixed smile that never reaches the eyes' "
            "soft focus, brows raised too high and held too long, an "
            "enthusiastic nodding that runs on a loop. What is missing "
            "gives it away: no sketching pauses (there is no real "
            "pathway work happening), no lip-parting before speech (no "
            "plan is forming words), no gaze drift to the horizon (no "
            "future is actually being attended). The performed face is "
            "all display and no machinery. The hidden face is all "
            "machinery and no display. Learn both, and you can tell which "
            "room you are standing in."
        ),
        "how_it_works": (
            "Hiding works through voluntary suppression of the voluntary "
            "muscles, and it leaks because the machinery keeps running "
            "underneath. The gaze drift escapes because attention to the "
            "future is driven by the goal component, which is not under "
            "voluntary control in the moment - you can order your eyes "
            "down, but the next mention of the goal re-aims them. The "
            "inner-brow micro-expression escapes because it is fast "
            "(under a fifth of a second) and tied to the appraisal shift "
            "itself, firing before the suppression command arrives. The "
            "breath escapes because respiratory patterning follows the "
            "autonomic state, not the facial muscles. Faking leaks "
            "inversely because performance runs top-down: the person "
            "activates the display muscles (smile, brow raise, nod) from "
            "the voluntary system without the underlying components "
            "firing, so the timing is wrong - displays are held too long, "
            "too symmetrically, without the micro-events that real "
            "machinery produces. The sketching pause cannot be faked "
            "convincingly because it is an actual attentional event: "
            "attention narrowing onto an internal simulation, which only "
            "happens when there is a simulation to attend to."
        ),
        "key_points": [
            "Hidden hope leaks upward: the gaze drifts to the horizon despite effort, the inner brows flash when the goal is mentioned, the breath deepens once.",
            "Suppression fails because the goal component re-aims attention faster than the voluntary system can leash it.",
            "Faked hope overdoes the easy parts: fixed bright smile, over-held brow raise, looping nods - all display, no machinery.",
            "What is missing gives faking away: no sketching pauses, no lip-parting, no genuine gaze drift.",
            "The hidden face is all machinery and no display; the faked face is all display and no machinery.",
        ],
        "requirements": [
            "Hiding and faking treated separately with distinct leak profiles.",
            "At least three leak channels for hidden hope with mechanisms.",
            "At least three missing-marker tells for faked hope.",
            "The speed-based mechanism of micro-expression leakage.",
            "The closing contrast line: machinery-without-display versus display-without-machinery.",
        ],
        "standards": [
            "Micro-expression timing follows Ekman and Friesen 1978: sub-second expressions escaping suppression.",
            "Display-rule framing follows Ekman 1999: voluntary management of expression and its limits.",
            "Leakage framing follows Frijda 1986: the law of the lightest load - unfelt displays betray themselves.",
        ],
        "citations": [CIT_FACS, CIT_EKMAN1999, CIT_FRIJDA],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "expression_gallery",
        "name": "Drawing Hope: Expression Gallery Notes for Artists and Actors",
        "group": "Facial Expression",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "For the artist's sketchbook and the actor's mirror - hope in "
            "five renderable frames. FRAME ONE, THE FLICKER: draw the face "
            "at rest, then change almost nothing - lift the inner brow "
            "two millimeters, turn the pupils up ten degrees. The viewer "
            "should feel the change before they can name it. FRAME TWO, "
            "THE STEADY GAZE: brows raised gently and evenly, eyes open a "
            "fraction wider with soft focus, mouth closed and easy. Light "
            "the face from slightly above-front, as if by a lamp that is "
            "not in the room yet. FRAME THREE, THE SKETCHING PAUSE: the "
            "whole face goes still mid-thought - lips parted a breath, "
            "gaze unfocused at the middle distance, one hand half-raised "
            "frozen in a gesture. This is hope doing its invisible work. "
            "FRAME FOUR, THE CONFIRMING NOD: the slow single nod, chin "
            "dipping once as a route survives testing - pair it with the "
            "exhale, the body's stamp of approval. FRAME FIVE, THE BLAZE: "
            "now let joy's repertoire in - the smile widens, the cheeks "
            "lift, the eyes shine, the head turns up and out as if the "
            "future had walked into the room. For the actor: play hope in "
            "the breath first (one deep exhale), the gaze second (up and "
            "beyond), the mouth last (release, never force). Never play "
            "hope as smiling hard - that reads as joy or performance. "
            "Play it as attending: the face of someone listening to a "
            "future that has not spoken yet."
        ),
        "how_it_works": (
            "The gallery works because each frame isolates one machinery "
            "event in renderable form. The flicker frame works on "
            "threshold perception: the smallest visible change that "
            "registers as meaning, teaching the artist how little hope "
            "needs to show. The steady-gaze frame works as the canonical "
            "readout - the full quiet signature with its lighting note "
            "(lit from a lamp not yet in the room) giving the artist the "
            "metaphor that makes the expression paintable. The sketching "
            "pause works as narrative: it shows the invisible work, the "
            "moment the audience understands that something is happening "
            "inside, which is why it is the actor's most powerful frame. "
            "The confirming nod works as punctuation: the exhale-plus-nod "
            "is a complete micro-story of a route surviving. The blaze "
            "frame works as permission: at full gain the expression is "
            "allowed to borrow joy's features, and the artist who knows "
            "this will not under-draw intense hope as merely calm. The "
            "actor's breath-first rule works because respiratory state "
            "drives the rest of the pattern downstream - set the breath, "
            "and the gaze and mouth follow honestly."
        ),
        "key_points": [
            "Five renderable frames: the flicker, the steady gaze, the sketching pause, the confirming nod, the blaze.",
            "The flicker teaches threshold perception: the smallest visible change that still reads as meaning.",
            "The sketching pause is the narrative frame: it shows the invisible work happening inside.",
            "The blaze frame gives permission to borrow joy's features at full gain - never under-draw intense hope as merely calm.",
            "For the actor: breath first (one deep exhale), gaze second (up and beyond), mouth last (release, never force).",
        ],
        "requirements": [
            "Five distinct frames, each renderable by an artist or playable by an actor.",
            "A lighting or staging note for at least one frame.",
            "The actor's ordering rule: breath, gaze, mouth.",
            "The never-smile-hard warning distinguishing hope from joy and performance.",
            "The attending metaphor as the closing direction.",
        ],
        "standards": [
            "Frame isolation follows Ekman and Friesen 1978: expressions decomposable into action-unit events.",
            "Narrative-expression framing follows Darwin 1872: expression as readable habit with communicative function.",
            "Performance ordering follows the embodied pattern of Scherer 2005: physiology leading expression.",
        ],
        "citations": [CIT_FACS, CIT_DARWIN, CIT_SCHERER],
        "sig_lens": SIG_LENS_DEF,
    },
]

ENTRIES += [
    # ------------------------------------------------ 18-21 TRIGGERS
    {
        "key": "classic_triggers",
        "name": "Classic Triggers of Hope: Situations, Words, and Events",
        "group": "Triggers",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "Certain situations trigger hope the way certain keys fit "
            "certain locks. A new option appearing: the treatment exists, "
            "the program accepts applications, the job is posted - hope "
            "fires when a closed map gains a door. Good news about the "
            "goal: the test came back clear, the reply was yes, the "
            "numbers moved in the right direction - progress reports are "
            "hope's favorite fuel. Someone offering help: a mentor's "
            "email, a neighbor with a truck, a friend who says I know "
            "someone - borrowed pathways count as pathways. Witnessing "
            "someone else's turnaround: the recovery story, the comeback, "
            "the before-and-after - proof that routes exist is itself a "
            "trigger. A deadline with a real chance: the application "
            "window is open, the audition is scheduled - structured "
            "opportunity focuses the machinery. Certain words work as "
            "triggers too: possible, eligible, approved, treatable, "
            "reversible, opening, chance, pathway, next step. And certain "
            "events: the first small win (the mechanism that starts the "
            "feedback loop), the removal of a blocker (the wall coming "
            "down), the arrival of spring after a hard winter (the "
            "calendar itself as a route). What all of these share is "
            "structure, not sentiment: each one either opens a pathway, "
            "raises agency, or sharpens a goal. That is the test of a "
            "real trigger - if it does none of the three, it is "
            "encouragement, not ignition."
        ),
        "how_it_works": (
            "Classic triggers work by changing one of the three "
            "components directly. A new option appearing works on "
            "pathways: the mental map gains a route, and the appraisal "
            "shifts from closed to open in a single update - the spark of "
            "onset. Good news works on agency: each confirmed progress "
            "signal is evidence that effort pays, which thickens the felt "
            "can-do and funds the next pathway sketch. Help offered works "
            "on both: another person's resources become borrowed pathways, "
            "and their belief becomes borrowed agency, which is why "
            "support is such a reliable trigger. Witnessed turnarounds "
            "work through vicarious pathways: seeing someone walk a route "
            "proves the route exists, and the brain treats proven routes "
            "as available ones. The trigger words work as appraisal "
            "shortcuts: possible and treatable are pre-compiled "
            "open-future appraisals, and hearing them can fire the "
            "machinery before the details arrive. The first small win "
            "works as loop ignition: it is the smallest unit of "
            "pathway-success evidence, and once the feedback loop is "
            "running, it tends to keep running."
        ),
        "key_points": [
            "Classic triggers: a new option appearing, good news about the goal, help offered, a witnessed turnaround, a real deadline.",
            "Trigger words act as appraisal shortcuts: possible, eligible, treatable, opening, next step.",
            "The first small win is loop ignition: the smallest unit of pathway-success evidence.",
            "Every real trigger changes one of the three components: it opens a pathway, raises agency, or sharpens a goal.",
            "The test of a trigger: if it does none of the three, it is encouragement, not ignition.",
        ],
        "requirements": [
            "At least five situation/event triggers named with concrete examples.",
            "Trigger words listed as a category.",
            "Each trigger mapped to the component it changes: pathways, agency, or goal.",
            "The first-small-win loop-ignition mechanism stated.",
            "The encouragement-versus-ignition test as the closing rule.",
        ],
        "standards": [
            "Component mapping follows Snyder 2002: triggers operating through goals, pathways, or agency.",
            "Vicarious-pathway framing follows the social-learning account alongside Averill, Catlin and Chon 1990 on the rules of hope.",
            "Appraisal-shortcut framing follows Lazarus 1991: rapid appraisal shifts from key information.",
        ],
        "citations": [CIT_SNYDER2002, CIT_AVERILL, CIT_LAZARUS1991],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "personal_triggers",
        "name": "Personal Triggers of Hope: Memories, Anniversaries, Private Associations",
        "group": "Triggers",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "Beyond the universal triggers, everyone carries a private set "
            "- keys cut for only their lock. A date on the calendar: the "
            "anniversary of the recovery, the season the business turned, "
            "the morning the letter arrived - the body remembers the "
            "corridor opening and replays a little of the feeling when "
            "the date returns. A place: the hospital hallway walked out "
            "of, the classroom where it clicked, the park bench where the "
            "decision was made - locations store the machinery's state "
            "like a saved game. A person: the mentor whose voice is "
            "internally replayed at hard moments, the friend who always "
            "sees the route, the grandmother whose sayings are "
            "pathway-generators in proverb form. A sensory anchor: a "
            "song from the good stretch, the smell of the workshop, the "
            "particular light of an early morning that once meant a fresh "
            "start - the senses bypass argument and fire the feeling "
            "directly. A personal proof: my own past turnaround, replayed "
            "as evidence - I have walked out of worse, the routes exist "
            "because I have used them. These private triggers are powerful "
            "precisely because they are pre-verified: the brain trusts its "
            "own history more than any stranger's encouragement. They are "
            "also why hope can seem to come from nowhere: an anniversary "
            "arrives, a song plays, and the corridor opens without any "
            "new information at all. This record describes the mechanism "
            "only; it never mines any real person's private associations."
        ),
        "how_it_works": (
            "Personal triggers work through associative memory firing the "
            "three-component machinery by pattern completion. The "
            "anniversary works through episodic replay: the date cues the "
            "stored episode of the corridor opening, and the replay "
            "partially re-renders the original appraisal - the future felt "
            "open then, so the pattern completes to open now. Places work "
            "through context-dependent memory: the location is encoded "
            "with the machinery's state, and returning to the context "
            "reloads the state. People work through internalized "
            "pathway-generation: the mentor's voice is not just comfort, "
            "it is a trained subroutine for sketching routes, and hearing "
            "it (even in memory) runs the subroutine. Sensory anchors "
            "work through the fast subcortical route: smell and music "
            "reach the emotion systems with minimal cortical filtering, "
            "so they can fire the feeling before the thinking mind has "
            "voted. Personal proof works through the strongest evidence "
            "channel there is: the self's own history of pathway success, "
            "which raises agency more efficiently than any external "
            "encouragement because the brain discounts others' data and "
            "trusts its own."
        ),
        "key_points": [
            "Private trigger sets: anniversary dates, stored places, internalized people, sensory anchors, personal proof.",
            "They are powerful because they are pre-verified: the brain trusts its own history more than strangers' encouragement.",
            "This is why hope can seem to come from nowhere: a song plays, a date arrives, and the corridor opens with no new information.",
            "The mentor's voice is a trained subroutine: hearing it in memory runs the pathway-sketching program.",
            "Personal proof - I have walked out of worse - is the strongest agency evidence channel there is.",
        ],
        "requirements": [
            "Five categories of personal trigger with concrete examples.",
            "The pre-verified trust mechanism stated.",
            "The seeming-from-nowhere phenomenon explained.",
            "A mechanism per category: replay, context, subroutine, fast route, self-evidence.",
            "The non-mining disclaimer: mechanism described, never applied to real people's associations.",
        ],
        "standards": [
            "Associative-firing framing follows Barrett 2017: emotion constructed from memory, interoception, and concepts.",
            "Context-memory framing follows the general encoding-specificity literature alongside Frijda 1986 on emotion laws.",
            "Internalized-voice framing follows the social-learning account of Averill, Catlin and Chon 1990.",
        ],
        "citations": [CIT_BARRETT, CIT_FRIJDA, CIT_AVERILL],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "surprise_triggers",
        "name": "Surprise Triggers of Hope: The Odd, Unexpected Ignitions",
        "group": "Triggers",
        "ladder_rank": 9,
        "ladder_tier": "compounded",
        "description": (
            "Some triggers of hope make no sense until you see the "
            "machinery. A stranger's small kindness - the held door, the "
            "returned wallet, the unasked-for help - can ignite hope in "
            "someone whose week was closing: it is evidence that the "
            "world contains helpers, which is a pathway component in "
            "disguise. A well-made object: a sturdy tool, a beautiful "
            "bridge, a clean piece of engineering - competence made "
            "visible reminds the mind that routes get built by hands like "
            "ours. Bad news about someone else's situation: hearing that "
            "another's wall is higher can, paradoxically, open one's own "
            "corridor - not from cruelty, but from recalibration, the map "
            "redrawing with one's own obstacles suddenly to scale. A "
            "child's question: the unguarded why or what-if that cuts "
            "through adult assumptions and reveals a route the grown-ups "
            "had filed under impossible. Exhaustion itself: at the very "
            "bottom of tiredness the mind sometimes stops defending the "
            "closed map, and in the undefended moment a small possibility "
            "slips through - hope arriving precisely because the guard "
            "was down. A song in a minor key: sad music can trigger hope "
            "because it processes the grief that was blocking the "
            "corridor, clearing the passage. The lesson of the odd "
            "triggers: the machinery does not care about the dignity of "
            "the spark. Any event that opens a pathway, raises agency, or "
            "sharpens a goal counts - even the strange ones, even the "
            "ones that arrive backwards."
        ),
        "how_it_works": (
            "Surprise triggers work because the appraisal system is "
            "opportunistic, not dignified. The stranger's kindness works "
            "through social-pathway inference: helpers exist implies help "
            "is available implies routes exist that involve others - a "
            "three-step inference the brain runs in under a second. The "
            "well-made object works through competence contagion: visible "
            "mastery activates the observer's own agency by association - "
            "if hands like mine built that, hands like mine can build my "
            "route. The recalibration trigger works through contrast "
            "appraisal: the obstacle is judged relative, not absolute, "
            "and a worse comparison shrinks it to a size the pathways can "
            "handle. The child's question works through assumption "
            "audit: the naive query forces the adult mind to re-examine "
            "a filed assumption, and filed assumptions are where dead "
            "routes go to hide. Exhaustion works through guard-lowering: "
            "defending the closed map costs energy, and when the energy "
            "runs out the defense drops, letting the goal component's "
            "quiet signal through. The minor-key song works through "
            "affective clearing: processed grief stops occupying the "
            "planning channels, freeing them for pathway sketching."
        ),
        "key_points": [
            "Odd triggers that work: a stranger's kindness, a well-made object, recalibrating bad news, a child's question, exhaustion itself, a minor-key song.",
            "The machinery is opportunistic, not dignified: any event that opens a pathway, raises agency, or sharpens a goal counts.",
            "Kindness implies helpers exist; helpers imply routes exist - a three-step inference run in under a second.",
            "Exhaustion can trigger hope by lowering the guard that was defending the closed map.",
            "Sad music can trigger hope by processing the grief that was blocking the corridor.",
        ],
        "requirements": [
            "At least five surprise triggers with concrete descriptions.",
            "A mechanism for each trigger tied to pathways, agency, or goal.",
            "The opportunistic-machinery principle stated.",
            "The backwards-arrival cases (exhaustion, sad music) explained, not just listed.",
            "The closing rule: the spark's dignity does not matter, only its component effect.",
        ],
        "standards": [
            "Inference-chain framing follows Lazarus 1991: rapid multi-step appraisal from minimal cues.",
            "Contrast-appraisal framing follows Frijda 1986: the laws of comparative judgment in emotion.",
            "Affective-clearing framing follows the emotion-regulation literature alongside Scherer 2005.",
        ],
        "citations": [CIT_LAZARUS1991, CIT_FRIJDA, CIT_SCHERER],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "chain_reactions",
        "name": "Chain Reactions: How One Hope Trigger Sets Off a Cascade",
        "group": "Triggers",
        "ladder_rank": 9,
        "ladder_tier": "compounded",
        "description": (
            "Hope rarely arrives alone; it arrives as the first domino. "
            "The cascade runs like this. STAGE ONE, IGNITION: a trigger "
            "fires - the reply came, the route opened. Hope assembles: "
            "goal sharp, first pathway sketched, agency stirring. STAGE "
            "TWO, SPILLOVER: the agency component does not respect "
            "boundaries. The can-do feeling leaks into neighboring goals: "
            "the person who just found hope about the job starts "
            "sketching routes for the health goal, the relationship goal, "
            "the project shelved last year. One corridor opening makes "
            "the whole building feel navigable. STAGE THREE, SOCIAL "
            "CONTAGION: the hopeful person tells someone, and the telling "
            "transmits the machinery - the listener borrows the pathways "
            "and the agency, and a second hope ignites. Now there are two "
            "minds sketching routes, pooling discoveries. STAGE FOUR, "
            "UPWARD SPIRAL: each small win in any of the goals feeds the "
            "shared agency pool, which funds more pathway sketching "
            "everywhere - the feedback loop running across goals and "
            "across people at once. STAGE FIVE, STABILIZATION: the cascade "
            "settles into a new baseline - not the blaze forever, but a "
            "steadier, warmer normal where the future is habitually read "
            "as navigable. Cascades can also run downward: one route "
            "slamming shut can drain neighboring hopes if the person "
            "generalizes the blockage. The practical lesson: guard the "
            "first domino. A single protected hope, fed with small wins, "
            "is the seed of the whole cascade - and a single carelessly "
            "crushed one can take the neighbors with it."
        ),
        "how_it_works": (
            "The cascade works through three transmission channels. "
            "Spillover works through agency generalization: the agency "
            "component is a global resource, not goal-locked, so success "
            "in one domain raises the felt can-do that all domains draw "
            "on - the brain does not keep separate fuel tanks per goal. "
            "Contagion works through machinery transmission: when hope is "
            "spoken, the listener receives not just the feeling but the "
            "components - the goal description, the sketched pathways, "
            "the demonstrated agency - and can assemble their own copy. "
            "The upward spiral works through the feedback loop writ "
            "large: wins anywhere raise the shared agency pool, which "
            "lowers the activation cost of pathway sketching everywhere, "
            "which produces more wins. Stabilization works through "
            "appraisal habit: repeated open-future appraisals train the "
            "default reading of the future as navigable, which is the "
            "mechanism behind lasting outlook change. The downward "
            "cascade works through blockage generalization: if the mind "
            "files one slammed route as evidence that routes in general "
            "close, the appraisal flips globally - which is why the "
            "practical lesson is to quarantine failures to their specific "
            "route and keep the other corridors open."
        ),
        "key_points": [
            "Hope arrives as the first domino: ignition, spillover, social contagion, upward spiral, stabilization.",
            "Spillover: agency is a global resource - one corridor opening makes the whole building feel navigable.",
            "Contagion: telling transmits the machinery itself - goal, pathways, agency - and the listener assembles their own copy.",
            "The upward spiral runs the feedback loop across goals and across people at once.",
            "Downward cascades generalize blockage: quarantine failures to their specific route to protect the neighbors.",
        ],
        "requirements": [
            "The five-stage cascade named and described in order.",
            "Three transmission channels with mechanisms: spillover, contagion, spiral.",
            "The downward cascade and its quarantine remedy.",
            "The global-agency-resource principle stated.",
            "The guard-the-first-domino practical lesson as the close.",
        ],
        "standards": [
            "Upward-spiral framing follows Fredrickson 2004: broaden-and-build dynamics of positive emotions.",
            "Agency-generalization follows Snyder 2002: agency as a cross-goal resource in hope theory.",
            "Contagion framing follows the social-transmission literature alongside Averill, Catlin and Chon 1990.",
        ],
        "citations": [CIT_FREDRICKSON2004, CIT_SNYDER2002, CIT_AVERILL],
        "sig_lens": SIG_LENS_DEF,
    },
    # ------------------------------------------------ 22-25 BEHAVIOR
    {
        "key": "actions",
        "name": "What People Do When They Feel Hope: Typical Actions",
        "group": "How It Shows in Behavior",
        "ladder_rank": 9,
        "ladder_tier": "compounded",
        "description": (
            "Hope is a doing emotion, and its actions are recognizable. "
            "PLANNING: the signature action - lists get made, calendars "
            "get marked, steps get sequenced. The hopeful mind externalizes "
            "its pathways onto paper, screens, and whiteboards. SEEKING "
            "INFORMATION: questions get asked, research gets done, experts "
            "get consulted - hope is hungry for route intelligence. "
            "TAKING THE FIRST STEP: the small, concrete, immediate move - "
            "the email sent, the appointment booked, the form started. "
            "Hope converts quickly into motion because the machinery is "
            "built for walking. BUILDING BACKUP ROUTES: the hopeful do not "
            "bet everything on one path; they line up plan B and plan C, "
            "sometimes before plan A has even been tried. PERSISTING: when "
            "a route closes, the hopeful reroute rather than stop - the "
            "visible behavior of flexible pathways. RECRUITING: help gets "
            "asked for, teams get assembled, the goal gets spoken aloud - "
            "hope pools its pathways socially. PREPARING: the future gets "
            "made room for - the spare room cleared, the skills practiced, "
            "the resources gathered - acting as if the corridor stays "
            "open. MARKING PROGRESS: small wins get noticed, counted, "
            "sometimes celebrated - the behavior that feeds the feedback "
            "loop on purpose. What hopeful people notably do NOT do: they "
            "do not wait passively, they do not hide the goal, and they do "
            "not spend the feeling on display instead of on steps. The "
            "actions are the proof of the machinery: where you see "
            "planning, stepping, rerouting, and recruiting, hope is "
            "running - whatever the face is doing."
        ),
        "how_it_works": (
            "The action pattern works because each behavior serves a "
            "component. Planning serves pathways: externalizing routes "
            "onto paper reduces working-memory load and makes the routes "
            "inspectable, shareable, and improvable - the mind's sketch "
            "becomes a blueprint. Information-seeking serves pathways "
            "too: every answered question is a route confirmed or a "
            "blockage mapped, and mapped blockages are reroutable. The "
            "first step serves agency: a completed small action is the "
            "cheapest possible evidence that effort moves things, and it "
            "ignites the feedback loop. Backup routes serve flexibility: "
            "multiple live pathways mean no single closure can kill the "
            "hope, which is the structural reason high-hope people look "
            "unshakable. Persisting-through-rerouting is the behavioral "
            "signature of the pathways component doing its defining work. "
            "Recruiting serves both pathways and agency socially: more "
            "minds, more routes, more fuel. Preparing serves the goal "
            "component: making room for the future is the appraisal of "
            "openness expressed in furniture and schedules. Marking "
            "progress serves the loop deliberately: counted wins are "
            "agency deposits, and hopeful people make the deposits on "
            "purpose."
        ),
        "key_points": [
            "Hope's signature actions: planning, information-seeking, taking the first step, building backup routes, persisting through rerouting, recruiting help, preparing, marking progress.",
            "Each action serves a component: planning and research feed pathways; the first step and marked wins feed agency; preparing honors the goal.",
            "Backup routes are structural: no single closure can kill hope that runs on multiple live pathways.",
            "Hope converts quickly into motion - the machinery is built for walking, not waiting.",
            "The actions are the proof: planning, stepping, rerouting, recruiting mean hope is running, whatever the face shows.",
        ],
        "requirements": [
            "At least seven distinct typical actions named with descriptions.",
            "Each action mapped to the component it serves.",
            "The backup-routes structural point stated.",
            "The notable absences: no passive waiting, no hiding the goal, no display over steps.",
            "The actions-as-proof closing rule.",
        ],
        "standards": [
            "Action-component mapping follows Snyder 2002: pathways and agency thinking expressed in goal-directed behavior.",
            "Feedback-loop behavior follows Snyder et al. 1991: iterative will-and-ways cycles in pursuit.",
            "Action-readiness framing follows Frijda 1986: emotions as states of readiness for characteristic action.",
        ],
        "citations": [CIT_SNYDER2002, CIT_SNYDER1991, CIT_FRIJDA],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "speech",
        "name": "What People Say: The Voice of Hope",
        "group": "How It Shows in Behavior",
        "ladder_rank": 9,
        "ladder_tier": "compounded",
        "description": (
            "Hope has a vocabulary, a grammar, and a music. THE "
            "VOCABULARY: possible, chance, opening, pathway, next step, "
            "option, try, when (not if), will, can. Listen for the "
            "future-positive modals: we can, there is a way, it is "
            "treatable, it is fixable. THE GRAMMAR: hopeful speech is "
            "conditional and constructive - if this, then that; here is "
            "what we try first; and if that does not work, we... The "
            "sentences contain their own backup plans. Questions are "
            "route-seeking: who knows about this, what has worked before, "
            "where do we start. THE MUSIC: the voice lifts slightly at the "
            "ends of phrases (the intonation of open futures), the pace is "
            "steady rather than rushed, and there are sketching pauses - "
            "mid-sentence silences where the route is being drawn in real "
            "time. THE SOCIAL REGISTER: hopeful people narrate the plan "
            "aloud - let me think this through with you - recruiting "
            "listeners into the pathway pool. They also future-talk: "
            "remember when we will look back on this, the corridor "
            "described as already walked. WHAT IS ABSENT: the closed "
            "vocabulary - never, impossible, always, no point - and the "
            "past-locked grammar of nothing ever changes. A useful field "
            "test: in any conversation, count the route-words versus the "
            "wall-words. The ratio is the hope content of the speech, and "
            "it predicts, better than smiles, whether the speaker will "
            "still be moving next week."
        ),
        "how_it_works": (
            "The speech pattern works as machinery made audible. The "
            "vocabulary works through appraisal labeling: saying possible "
            "and treatable is the open-future appraisal spoken aloud, and "
            "speaking it reinforces it - language feeds back into the "
            "appraisal that produced it. The conditional grammar works as "
            "pathway externalization: if-this-then-that sentences are "
            "literally routes rendered in syntax, and constructing them "
            "in speech is constructing them in the shared space where "
            "others can improve them. The route-seeking questions work as "
            "social pathway mining: each question is a request for "
            "someone else's route intelligence. The music - the lifted "
            "intonation, the steady pace - works as an honest signal: "
            "prosody is hard to fake at length, so the voice's lift is a "
            "reliable readout of the underlying appraisal. The "
            "sketching pauses work as real-time planning made audible: "
            "the silence is the sound of the machinery running. "
            "Future-talk works through mental time travel: describing the "
            "corridor as already walked pre-loads the memory of success, "
            "which the agency component spends like fuel."
        ),
        "key_points": [
            "Hope's vocabulary: possible, opening, pathway, next step, when (not if), we can - the future-positive modals.",
            "Hope's grammar is conditional and constructive: sentences contain their own backup plans.",
            "The music: lifted phrase endings, steady pace, and sketching pauses where routes are drawn in real time.",
            "Hopeful people narrate the plan aloud, recruiting listeners into the pathway pool, and future-talk the corridor as already walked.",
            "Field test: count route-words versus wall-words - the ratio predicts who will still be moving next week.",
        ],
        "requirements": [
            "Vocabulary, grammar, and music (prosody) each treated as a section.",
            "The social register: narrating aloud and future-talk.",
            "The absences: closed vocabulary and past-locked grammar.",
            "A mechanism for each speech feature tied to the machinery.",
            "The route-word versus wall-word field test as the close.",
        ],
        "standards": [
            "Language-appraisal feedback follows Barrett 2017: concepts and words shaping constructed emotion.",
            "Externalization framing follows Snyder 2002: pathways thinking rendered in shareable form.",
            "Prosody-as-signal framing follows Scherer 2005: vocal expression as a synchronized emotion component.",
        ],
        "citations": [CIT_BARRETT, CIT_SNYDER2002, CIT_SCHERER],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "decisions",
        "name": "How Hope Changes Decisions and Judgment",
        "group": "How It Shows in Behavior",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Hope does not just color decisions; it reweights the scales "
            "they are weighed on. RISK: the hopeful take more calculated "
            "risks - not reckless ones, but the kind where the downside "
            "is survivable and the upside matters. Hope raises the "
            "perceived probability of success just enough to make the "
            "worthwhile gamble look worthwhile, which is why hopeful "
            "people start things. TIME HORIZON: hope lengthens the "
            "horizon. The hopeful will invest in payoffs months or years "
            "out - education, training, slow treatments, patient building - "
            "because the future is modeled as navigable rather than blank. "
            "OPTION BREADTH: hopeful deciders keep more options live "
            "longer, delaying the pruning of alternatives - the "
            "decision-making version of backup routes. INFORMATION "
            "CHOICE: the hopeful seek diagnostic information (what works, "
            "what blocks) over comforting information, because the "
            "machinery needs route intelligence, not reassurance. SOCIAL "
            "CHOICE: hopeful people choose collaborators over solo "
            "grinding more often - the machinery knows that pooled "
            "pathways beat solitary ones. THE SHADOW SIDE: hope can bias "
            "judgment too. It can underweight base rates (this usually "
            "fails, but I feel it will work), overweight the vivid route "
            "over the probable one, and keep a person investing past the "
            "point where rerouting has become denial. The difference "
            "between the bright side and the shadow is the pathways "
            "audit: hopeful decisions stay sound as long as the routes "
            "are real, plural, and updated by evidence. When the audit "
            "stops, hope stops informing judgment and starts decorating "
            "it."
        ),
        "how_it_works": (
            "The decision effects work through appraisal-driven "
            "reweighting. Risk reweighting works through the agency "
            "component: felt can-do raises the subjective probability of "
            "success, which shifts the expected-value calculation toward "
            "action - rationally, when the probability shift is earned by "
            "real pathways, and irrationally when it is not. Horizon "
            "lengthening works through future modeling: an open, "
            "navigable future has positive expected value at distance, so "
            "discounting of delayed rewards drops and long investments "
            "pencil out. Option breadth works through the pathways "
            "component directly: a mind running multiple live routes "
            "experiences pruning as route-killing, so it delays "
            "commitment to a single path. Information choice works "
            "through machinery hunger: pathways need intelligence, so "
            "attention biases toward diagnostic data. The shadow side "
            "works through the same channels miscalibrated: agency "
            "inflates probability estimates past the evidence, the vivid "
            "route captures attention away from base rates, and the "
            "feedback loop - which normally corrects via failed attempts - "
            "gets bypassed when failures are reinterpreted instead of "
            "counted. The pathways audit is the correction mechanism: "
            "real, plural, evidence-updated routes keep the reweighting "
            "honest."
        ),
        "key_points": [
            "Hope reweights decisions: more calculated risk-taking, longer time horizons, broader option sets, diagnostic information-seeking, collaborative choices.",
            "The hopeful invest in distant payoffs because a navigable future has positive expected value at distance.",
            "Hopeful deciders delay pruning alternatives - the decision version of backup routes.",
            "Shadow side: hope can underweight base rates, overweight the vivid route, and fund persistence past the point of rerouting into denial.",
            "The pathways audit keeps it honest: routes must be real, plural, and updated by evidence.",
        ],
        "requirements": [
            "At least five decision domains with the hope effect on each.",
            "Mechanisms tied to components: agency for risk, pathways for breadth, future-modeling for horizon.",
            "The shadow side with three named biases.",
            "The pathways audit as the correction mechanism.",
            "The informing-versus-decorating distinction as the close.",
        ],
        "standards": [
            "Reweighting framing follows Lazarus 1991: appraisal shaping choice under emotion.",
            "Expected-value and discounting framing follows the judgment literature alongside Frijda 1986 on action tendencies.",
            "Bias-correction framing follows the pathways-flexibility account of Snyder 2002.",
        ],
        "citations": [CIT_LAZARUS1991, CIT_FRIJDA, CIT_SNYDER2002],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "intensity_behavior",
        "name": "Hope Under Intensity: How Behavior Escalates as the Feeling Grows",
        "group": "How It Shows in Behavior",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Watch hope's behavior across the dial and you see a "
            "predictable escalation ladder. LEVEL 1, QUIET LEANING: "
            "behavior barely changes - the person reads one article, "
            "asks one casual question, mentions the goal once in passing. "
            "The machinery is idling. LEVEL 2, ACTIVE SKETCHING: lists "
            "appear, research begins, the calendar gets its first marks. "
            "The person starts talking about the goal in the conditional - "
            "when this works out. LEVEL 3, COMMITTED MOVING: real "
            "resources move - money, time, reputation. Applications go in, "
            "appointments are kept, the first hard step is taken and the "
            "second scheduled. Backup routes are lined up. LEVEL 4, "
            "FULL MOBILIZATION: the goal reorganizes life - schedules "
            "bend, other projects pause, the team assembles, the person "
            "works the routes daily. Setbacks are rerouted within hours. "
            "LEVEL 5, THE BLAZE: the person becomes a transmitter - "
            "recruiting, teaching, telling the story, pulling others into "
            "the corridor. The behavior is now social infrastructure, not "
            "just personal striving. The escalation is usually "
            "stepwise, not smooth: hope jumps levels when a pathway is "
            "confirmed (the reply came, the test passed), and each jump "
            "unlocks the next band of behavior. It can also jump too far: "
            "escalation past the evidence - mobilizing like level 4 on "
            "level 1 information - is the behavioral form of the shadow "
            "side, and the correction is the same pathways audit. Read "
            "the level by the resources: what the person is spending - "
            "attention, then time, then money and reputation, then other "
            "people's time - tells you exactly where the dial sits."
        ),
        "how_it_works": (
            "The escalation works through resource commitment following "
            "agency gain. At level 1, agency is thin, so the system "
            "risks only cheap resources: a little attention, one question - "
            "the cost of being wrong is near zero. Each confirmed "
            "pathway raises agency, which raises the affordable stake: "
            "the system will risk more expensive resources (time, then "
            "money, then reputation) only when the felt probability of "
            "payoff justifies it. That is why the jumps follow pathway "
            "confirmations - the agency ledger must balance before the "
            "next level unlocks. Level 5's transmission behavior works "
            "through the contagion channel at full gain: with agency "
            "abundant, the cheapest way to multiply pathways is to recruit "
            "other minds, so the system spends social resources to buy "
            "route intelligence. Over-escalation works through agency "
            "outrunning evidence: the felt can-do inflates past what the "
            "pathway confirmations support, and the system spends level-4 "
            "resources on level-1 information. The resource-reading rule "
            "works because spending is the honest signal - people can "
            "misreport their hope level, but the ledger of what they "
            "spend does not lie."
        ),
        "key_points": [
            "Five escalation levels: quiet leaning, active sketching, committed moving, full mobilization, the blaze as transmission.",
            "Escalation is stepwise: hope jumps levels when a pathway is confirmed, each jump unlocking the next band of behavior.",
            "The system risks cheap resources first (attention), then expensive ones (time, money, reputation) as agency justifies the stake.",
            "At the blaze level the person becomes social infrastructure: recruiting, teaching, pulling others into the corridor.",
            "Read the level by the spending: the resource ledger is the honest signal of where the dial sits.",
        ],
        "requirements": [
            "Five named escalation levels with the behavior of each.",
            "The stepwise-jump mechanism tied to pathway confirmation.",
            "The resource-commitment logic: cheap to expensive spending.",
            "Over-escalation named as the shadow form with its correction.",
            "The read-by-spending rule as the close.",
        ],
        "standards": [
            "Resource-commitment framing follows Snyder 2002: agency scaling with pathway progress.",
            "Escalation dynamics follow the approach-motivation literature alongside Frijda 1986.",
            "Honest-signaling framing follows the costly-signaling account in line with Darwin 1872 on expression.",
        ],
        "citations": [CIT_SNYDER2002, CIT_FRIJDA, CIT_DARWIN],
        "sig_lens": SIG_LENS_DEF,
    },
]

ENTRIES += [
    # ------------------------------------------------ 26-28 HEALTHY EXPRESSION
    {
        "key": "healthy_expression",
        "name": "Expressing Hope Healthily: Saying It, Showing It, Channeling It",
        "group": "Expressing It Healthily",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Healthy hope expression has three channels, and the healthy "
            "part is that all three stay connected to real pathways. "
            "SAYING IT: speak the goal plainly, name the routes honestly "
            "(including the uncertain ones), and keep the conditional "
            "grammar - here is what we try first, and if not, then. "
            "Honest speech keeps hope calibrated: listeners can improve "
            "real routes, but they cannot improve a performance. SHOWING "
            "IT: let the quiet signature show - the lifted gaze, the "
            "steady energy, the constructive busyness. Visible hope "
            "recruits: people join corridors they can see. But show the "
            "work, not just the glow - the lists, the steps taken, the "
            "rerouting around last week's blockage. CHANNELING IT: put "
            "the energy into the machinery - one pathway sketched per day, "
            "one small step taken, one backup route kept warm. Hope that "
            "is channeled compounds; hope that is only displayed "
            "evaporates. The three channels reinforce each other: saying "
            "it recruits pathway help, showing it recruits social fuel, "
            "channeling it produces the small wins that keep both honest. "
            "Healthy expression also knows its seasons: there are times "
            "to broadcast (when recruiting) and times to tend quietly "
            "(when the routes are fragile and need protection from "
            "premature scrutiny). The test of healthy expression is "
            "always the same: does it feed the pathways, the agency, or "
            "the goal - or does it only feed the image? This record "
            "describes general patterns; it offers no guidance for any "
            "real person's situation."
        ),
        "how_it_works": (
            "Healthy expression works by keeping the display coupled to "
            "the machinery. Saying it works through calibration: honest "
            "conditional speech exposes the routes to other minds, which "
            "improves them and corrects the agency estimate - the social "
            "version of the pathways audit. Showing it works through "
            "recruitment: visible quiet hope is a low-cost honest signal "
            "that attracts collaborators, helpers, and fellow travelers, "
            "each bringing pathways. Channeling it works through the "
            "feedback loop directly: sketched pathways and taken steps "
            "are the loop's fuel, so channeled hope literally manufactures "
            "more of itself. The reinforcement triangle works because "
            "each channel feeds the others' inputs: speech brings routes, "
            "display brings people, channeling brings wins, and wins make "
            "the speech truer and the display brighter. The seasonal "
            "awareness works through protection: fragile early routes "
            "can be killed by premature criticism (which closes the "
            "appraisal before the pathway is tested), so quiet tending "
            "is the rational strategy until the routes are sturdy enough "
            "to survive scrutiny. The feed-the-machinery test works "
            "because decoupled display - hope performed without pathways - "
            "consumes social credibility without producing progress, "
            "which eventually bankrupts the agency it was meant to "
            "signal."
        ),
        "key_points": [
            "Three healthy channels: saying it (honest conditional speech), showing it (the quiet signature, work visible), channeling it (daily pathway work).",
            "The display must stay coupled to the machinery: show the work, not just the glow.",
            "The channels reinforce each other: speech recruits routes, display recruits people, channeling produces wins.",
            "Know the seasons: broadcast when recruiting, tend quietly when routes are fragile.",
            "The test: does the expression feed pathways, agency, or the goal - or only the image?",
        ],
        "requirements": [
            "Three channels named with the healthy form of each.",
            "The coupling principle: display connected to real pathways.",
            "The reinforcement triangle mechanism.",
            "Seasonal awareness: broadcast versus quiet tending with the protection rationale.",
            "The feed-the-machinery test as the close, plus the non-guidance disclaimer.",
        ],
        "standards": [
            "Calibration framing follows Snyder 2002: honest pathways thinking corrected by social feedback.",
            "Honest-signaling framing follows the signaling literature in line with Darwin 1872.",
            "Feedback-loop framing follows Snyder et al. 1991: channeled effort manufacturing agency.",
        ],
        "citations": [CIT_SNYDER2002, CIT_DARWIN, CIT_SNYDER1991],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "unhealthy_expression",
        "name": "The Costs of Mishandled Hope: Bottling It Up or Exploding",
        "group": "Expressing It Healthily",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Hope mishandled takes two familiar shapes, and both are "
            "expensive. BOTTLING IT UP: the hope is felt but never spoken, "
            "never shown, never acted on. The goal stays private, the "
            "routes stay sketched only in the head, the first step never "
            "gets taken. The costs compound quietly: without social "
            "pathway-pooling the routes stay thin; without spoken "
            "commitment the agency never gets tested against reality; "
            "without small wins the feedback loop never ignites. Bottled "
            "hope ferments into rumination - the machinery running with "
            "no output, sketching routes that are never walked, which "
            "slowly converts hope into its anxious cousin. And because "
            "no one can see it, no one can help - the most solvable "
            "problem in the system (thin pathways) goes unsolved for "
            "want of witnesses. EXPLODING: the opposite failure - hope "
            "performed at full volume with no machinery behind it. Big "
            "announcements, grand plans declared, the blaze displayed "
            "before a single route is tested. The costs arrive on "
            "schedule: when the untested routes fail (as untested routes "
            "do), the public collapse is larger than the private "
            "disappointment would have been; credibility burns, and the "
            "next real hope gets no audience; and the performer, having "
            "spent the feeling on display, has no fuel left for the "
            "actual steps. The middle path - the one this database keeps "
            "returning to - is coupled expression: hope spoken "
            "conditionally, shown quietly, channeled daily. Bottling "
            "starves the machinery of inputs; exploding spends the fuel "
            "on the image. Both are forms of decoupling, and the price "
            "in both cases is paid in pathways."
        ),
        "how_it_works": (
            "Bottling works through input starvation. The hope machinery "
            "needs three inputs to run well: route intelligence (from "
            "research and other minds), reality-testing (from attempted "
            "steps), and social fuel (from shared agency). Bottling cuts "
            "all three: the routes stay private and therefore unimproved, "
            "the steps stay untaken and therefore untested, the agency "
            "stays solitary and therefore thin. Rumination is the "
            "degenerate mode of the pathway component: sketching without "
            "walking produces routes that multiply without being pruned, "
            "and unpruned routes generate anxiety rather than agency - "
            "the machinery eating itself. Exploding works through "
            "premature commitment: public declarations lock the person "
            "to untested routes (consistency pressure), spend social "
            "credibility before any wins exist to replenish it, and "
            "convert the agency fuel into display energy, leaving the "
            "tank empty for the steps. The collapse is amplified by the "
            "audience: private failure costs a route, public failure "
            "costs the route plus the standing to try the next one. Both "
            "failures are decoupling failures - display separated from "
            "machinery in opposite directions - which is why the "
            "correction for both is the same: recouple, through "
            "conditional speech, quiet showing, and daily channeling."
        ),
        "key_points": [
            "Bottling: hope felt but never spoken, shown, or acted on - the machinery starved of route intelligence, reality-testing, and social fuel.",
            "Bottled hope ferments into rumination: sketching without walking, routes multiplying without pruning, hope converting to anxiety.",
            "Exploding: the blaze performed with no machinery behind it - big announcements on untested routes.",
            "Public collapse costs more than private disappointment: the route plus the standing to try the next one.",
            "Both are decoupling failures in opposite directions; the correction for both is recoupling.",
        ],
        "requirements": [
            "Bottling and exploding each described with their compounding costs.",
            "The three starved inputs of bottling named.",
            "Rumination as the degenerate pathway mode explained.",
            "The amplified cost of public collapse explained.",
            "The decoupling diagnosis and the recoupling correction as the close.",
        ],
        "standards": [
            "Input-starvation framing follows Snyder 2002: pathways and agency requiring social and enacted inputs.",
            "Rumination framing follows the perseverative-cognition literature alongside Lazarus 1999 on coping.",
            "Decoupling framing follows Frijda 1986: the laws of emotion and their regulation.",
        ],
        "citations": [CIT_SNYDER2002, CIT_LAZARUS1999, CIT_FRIJDA],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "everyday_practices",
        "name": "Everyday Practices That Keep Hope in Balance",
        "group": "Expressing It Healthily",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Hope, like any machinery, runs better with maintenance. These "
            "are small, ordinary practices - general patterns described "
            "for education, not prescriptions for anyone. NAME THE GOAL "
            "DAILY: one sentence, each morning, stating what the hope is "
            "for - goals kept explicit stay sharp, and sharp goals sketch "
            "better routes. SKETCH ONE ROUTE: a minute of if-this-then-"
            "that on paper - the daily deposit into the pathways account. "
            "TAKE ONE SMALL STEP: the cheapest possible forward motion - "
            "the email, the call, the five minutes - because the feedback "
            "loop runs on completed steps, not grand ones. COUNT THE "
            "WINS: each evening, three things that moved - the agency "
            "ledger balanced daily never goes bankrupt. KEEP A BACKUP "
            "ROUTE WARM: maintain at least one alternative path in "
            "outline - hope with options is hope that survives bad news. "
            "SPEAK IT WEEKLY: tell one person the goal and the current "
            "route - the social pathway pool refreshed on schedule. AUDIT "
            "MONTHLY: review the routes against evidence - which are "
            "real, which are wishes, which need rerouting - the pathways "
            "audit that keeps hope honest. REST THE MACHINERY: deliberately "
            "scheduled time with no goal-thinking - hope, like muscle, "
            "strengthens in recovery, and the corridor looks clearer after "
            "a genuine break. None of these is dramatic; that is the "
            "point. Hope is maintained the way bridges are maintained: "
            "not with ceremonies, but with inspections, small repairs, "
            "and respect for the load."
        ),
        "how_it_works": (
            "The practices work by servicing each component on a schedule. "
            "Daily goal-naming services the goal component: explicit "
            "goals resist drift and stay available to attention, which "
            "keeps the machinery aimed. Route-sketching services "
            "pathways: a minute a day compounds into a route library, "
            "and the act of sketching is itself agency-positive - the "
            "hand drawing the map believes in the territory. Small steps "
            "service the feedback loop: completed actions are the loop's "
            "fuel, and smallness is a feature - the step must be cheap "
            "enough to complete daily, because the loop needs daily "
            "feeding. Win-counting services agency directly: the ledger "
            "of counted progress is the evidence the can-do feeling draws "
            "on. Backup routes service resilience structurally: outlined "
            "alternatives mean no single closure is fatal. Weekly "
            "speaking services the social pool: regular transmission "
            "keeps borrowed pathways and agency flowing both ways. "
            "Monthly auditing services calibration: evidence review "
            "prunes wish-routes before they consume real resources. Rest "
            "services the whole system: goal-directed cognition is "
            "expensive, and scheduled recovery prevents the fatigue that "
            "masquerades as hopelessness - many supposed losses of hope "
            "are just tired machinery."
        ),
        "key_points": [
            "Seven maintenance practices: name the goal daily, sketch one route, take one small step, count the wins, keep a backup route warm, speak it weekly, audit monthly.",
            "Plus rest: scheduled time with no goal-thinking - hope strengthens in recovery like muscle.",
            "Each practice services a component: naming aims the goal, sketching builds pathways, steps and wins feed agency.",
            "Smallness is a feature: the step must be cheap enough to complete daily, because the loop needs daily feeding.",
            "Many supposed losses of hope are just tired machinery - rest is diagnostic, not indulgent.",
        ],
        "requirements": [
            "At least seven distinct practices named with one-line descriptions.",
            "Each practice mapped to the component or mechanism it services.",
            "The smallness-as-feature principle stated.",
            "The rest practice with its diagnostic rationale.",
            "The bridge-maintenance metaphor as the close, plus the non-prescription disclaimer.",
        ],
        "standards": [
            "Component-servicing framing follows Snyder 2002: goals, pathways, and agency as maintainable capacities.",
            "Feedback-loop feeding follows Snyder et al. 1991: iterative progress sustaining the will-and-ways cycle.",
            "Recovery framing follows the effort-recovery literature alongside Fredrickson 2004 on resource building.",
        ],
        "citations": [CIT_SNYDER2002, CIT_SNYDER1991, CIT_FREDRICKSON2004],
        "sig_lens": SIG_LENS_DEF,
    },
    # ------------------------------------------------ 29-31 RECOGNITION
    {
        "key": "reading_signs",
        "name": "Reading Hope in Others: Face, Body, Voice, and Behavior",
        "group": "Recognizing It in Others",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Reading hope in another person is reading quiet signals, and "
            "the skill is attention, not mind-reading. THE FACE: the "
            "lifted gaze - eyes up and forward with soft focus - is the "
            "most reliable tell; add the gently raised brows and the "
            "closed-lip ease, and you are looking at the quiet signature. "
            "Watch for the micro-events: the lip parting as a plan forms, "
            "the slow confirming nod, the sketching pause. THE BODY: the "
            "unclenched jaw, the squared shoulders, the forward lean, the "
            "constructive hands - sketching, listing, building. The walk "
            "with the slightly lengthened stride. THE VOICE: the lifted "
            "phrase endings, the conditional grammar (if this, then that; "
            "and if not, then), the route-words outnumbering the "
            "wall-words, the sketching pauses mid-sentence. THE BEHAVIOR: "
            "planning visible on paper, the first step taken, backup "
            "routes mentioned, help asked for, progress marked. No single "
            "channel is proof - the face can be managed, the voice can be "
            "performed - but the channels converge: when the gaze, the "
            "grammar, and the calendar all point forward, hope is "
            "running. And read the absences too: the person who has "
            "stopped planning, whose gaze has dropped to the floor, whose "
            "speech has gone past-locked - the corridor may have closed, "
            "and that reading matters just as much. This record teaches "
            "observation of general patterns; it never authorizes labeling "
            "any real person."
        ),
        "how_it_works": (
            "Recognition works through convergent cue integration. Each "
            "channel - face, body, voice, behavior - is a noisy readout "
            "of the underlying machinery, and each can be wrong alone: "
            "the face can be suppressed or performed, the voice can be "
            "coached, any single behavior can have other causes. But the "
            "channels are driven by the same three components, so when "
            "hope is genuinely running, they correlate: the goal "
            "component aims the gaze and the grammar forward together, "
            "the pathways component produces both the sketching pause and "
            "the visible planning, the agency component lifts both the "
            "voice and the stride. Convergence is the detection "
            "principle: three channels agreeing is strong evidence, one "
            "channel alone is a hypothesis. The absence-reading works "
            "through the same logic in reverse: when the machinery stops, "
            "all its readouts decay together - the dropped gaze, the "
            "past-locked grammar, the unplanned calendar are the "
            "corridor-closed signature. The skill improves with "
            "calibration: knowing a person's baseline (their normal gaze, "
            "their normal grammar) lets you read the delta, which is "
            "always more informative than the absolute."
        ),
        "key_points": [
            "Read four channels: face (lifted gaze, raised brows, lip ease, micro-events), body (unclenched, squared, leaning, constructive hands), voice (lifted endings, conditional grammar, route-words), behavior (planning, stepping, backup routes).",
            "No single channel is proof; convergence is the detection principle - three channels agreeing is strong evidence.",
            "Read the absences too: stopped planning, dropped gaze, past-locked speech form the corridor-closed signature.",
            "Calibration beats absolutes: knowing a person's baseline lets you read the informative delta.",
            "Observation of general patterns only - never authorization to label any real person.",
        ],
        "requirements": [
            "Four channels with specific tells for each.",
            "The convergence principle stated as the detection rule.",
            "The corridor-closed absence signature described.",
            "The baseline-calibration point stated.",
            "The non-labeling disclaimer included.",
        ],
        "standards": [
            "Cue-integration framing follows the person-perception literature alongside Ekman and Friesen 1978 on expressive channels.",
            "Convergence logic follows Scherer 2005: synchronized components producing correlated readouts.",
            "Baseline-calibration follows Frijda 1986: reading change against the individual's norm.",
        ],
        "citations": [CIT_FACS, CIT_SCHERER, CIT_FRIJDA],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "supportive_responses",
        "name": "What to Do When Someone Near You Feels Hope: Supportive Responses",
        "group": "Recognizing It in Others",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "When someone near you is carrying hope, your response can "
            "feed the machinery or starve it - and the difference is "
            "smaller than you think. FEED THE PATHWAYS: the most useful "
            "thing you can do is add routes - I know someone who, have "
            "you tried, what about. Route intelligence is the scarcest "
            "resource in the system, and donating yours is pure fuel. ASK "
            "THE SKETCHING QUESTIONS: what is the goal exactly, what is "
            "the next step, what is plan B - questions that make the "
            "machinery run better, asked with genuine curiosity rather "
            "than interrogation. LEND AGENCY: your belief, stated plainly "
            "(I think you can do this; this is a good plan), becomes "
            "borrowed agency - and borrowed agency spends like the real "
            "thing. MARK THEIR WINS: notice the small steps aloud - you "
            "did the hard call, the form is in - because counted wins are "
            "agency deposits and outside witnesses count double. PROTECT "
            "FRAGILE ROUTES: when the hope is new and the routes are "
            "thin, keep your doubts private a little longer - premature "
            "scrutiny can close an appraisal that testing would have "
            "kept open. SHARE THE LOAD: offer the concrete help - the "
            "ride, the introduction, the hour - because pooled effort is "
            "the machinery's favorite configuration. And when their hope "
            "is about something you do not share: you do not have to "
            "believe in the goal to respect the machinery - acknowledging "
            "the work (you have really thought this through) feeds it "
            "without requiring your endorsement. These are general "
            "patterns of supportive interaction, described for education - "
            "not advice for any real situation."
        ),
        "how_it_works": (
            "Supportive responses work by donating to the three "
            "components. Feeding pathways works through route-pooling: "
            "your donated route intelligence becomes their live pathway, "
            "and your sketching questions force their pathway component "
            "to generate more - questions are machinery exercise. Lending "
            "agency works through social appraisal: humans weight "
            "trusted others' evaluations heavily, so your stated belief "
            "directly raises their felt can-do - the borrowed-agency "
            "effect is one of the most replicated findings in the "
            "support literature. Marking wins works through the ledger: "
            "outside witnesses make progress feel realer (social reality "
            "testing), and realer progress deposits more agency. "
            "Protecting fragile routes works through appraisal timing: "
            "an untested route closed by criticism is a pathway lost "
            "before its evidence arrived, while the same criticism after "
            "testing is useful data - timing is the difference between "
            "killing and pruning. Sharing the load works through effort "
            "pooling: concrete help converts your resources into their "
            "pathway steps, the most direct donation possible. "
            "Respect-without-endorsement works because the machinery "
            "runs on acknowledged effort, not shared belief - recognition "
            "of the work feeds agency regardless of your position on "
            "the goal."
        ),
        "key_points": [
            "Feed the pathways: donate route intelligence - the scarcest resource in the system.",
            "Ask sketching questions: what is the goal exactly, what is the next step, what is plan B.",
            "Lend agency: your plainly stated belief becomes borrowed agency, and borrowed agency spends like the real thing.",
            "Mark their wins aloud: outside witnesses count double in the agency ledger.",
            "Protect fragile routes from premature scrutiny; share concrete load; respect the machinery even when you do not share the goal.",
        ],
        "requirements": [
            "At least six supportive responses named with descriptions.",
            "Each response mapped to the component it feeds.",
            "The borrowed-agency effect stated.",
            "The appraisal-timing rationale for protecting fragile routes.",
            "The respect-without-endorsement case covered, plus the non-advice disclaimer.",
        ],
        "standards": [
            "Social-support framing follows the support-provision literature alongside Lazarus 1999 on coping resources.",
            "Borrowed-agency framing follows Snyder 2002: agency supplemented by trusted others' belief.",
            "Appraisal-timing framing follows Frijda 1986: the temporal dynamics of emotional appraisal.",
        ],
        "citations": [CIT_LAZARUS1999, CIT_SNYDER2002, CIT_FRIJDA],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "mistakes",
        "name": "What NOT to Do: Common Mistakes That Crush Hope",
        "group": "Recognizing It in Others",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Hope is sturdy machinery but it has known vulnerabilities, "
            "and well-meaning people hit them regularly. THE REALITY "
            "HAMMER: leading with the odds - that almost never works, be "
            "realistic - before the routes have been tested. It closes "
            "the appraisal prematurely and teaches the machinery that "
            "sketching gets punished. THE FALSE REASSURANCE: I am sure it "
            "will all work out - comfort that bypasses the pathways "
            "entirely. It feels kind and feeds nothing; worse, when it "
            "proves empty, it discredits the next real encouragement. THE "
            "ROUTE THEFT: taking over the planning - here is what you "
            "should do - which replaces their pathways with yours and "
            "starves their agency. Help that removes the person's own "
            "machinery is not help. THE COMPARISON: others have it worse, "
            "or look how well she handled it - which reframes their goal "
            "as illegitimate and their struggle as failure. THE "
            "CHEERLEADER TRAP: relentless positivity that forbids doubt - "
            "you cannot say that here - which drives the real appraisal "
            "underground where it cannot be worked with. THE ABANDONED "
            "WITNESS: going silent when the route fails - the moment the "
            "machinery most needs the ledger witnessed is the moment "
            "people look away. Each mistake has the same structure: it "
            "damages one of the three components - closing pathways, "
            "draining agency, or blurring the goal - while feeling, to "
            "the person making it, like honesty or kindness. Knowing the "
            "list does not make anyone perfect at this; it just moves "
            "the errors from invisible to visible, which is where they "
            "can be caught. Described for education; not advice for any "
            "real situation."
        ),
        "how_it_works": (
            "The mistakes work by attacking components under the guise "
            "of virtue. The reality hammer works through premature "
            "appraisal closure: citing base rates before routes are "
            "tested shuts the open-future appraisal, and the shutdown "
            "generalizes - the machinery learns that generating "
            "pathways invites punishment, so it generates fewer. False "
            "reassurance works through decoupled comfort: it stimulates "
            "the pleasant feeling without touching pathways or agency, "
            "so when reality arrives the gap between the promised "
            "feeling and the actual map discredits future support. Route "
            "theft works through agency substitution: your plan "
            "replaces their planning, so their pathways component "
            "atrophies from disuse and their agency never gets the "
            "evidence of self-generated routes. Comparison works "
            "through goal invalidation: the appraisal of the goal's "
            "legitimacy drops, and without a legitimate goal the "
            "machinery has nothing to aim at. The cheerleader trap works "
            "through appraisal suppression: forbidden doubt does not "
            "vanish, it goes unprocessed, and unprocessed appraisal "
            "cannot update - the machinery freezes. The abandoned "
            "witness works through ledger bankruptcy: at the moment of "
            "failure the agency account is overdrawn, and silence "
            "confirms the worst reading - that the failure is the "
            "verdict, not a data point."
        ),
        "key_points": [
            "Six common mistakes: the reality hammer, false reassurance, route theft, comparison, the cheerleader trap, the abandoned witness.",
            "Each mistake damages a component while feeling like honesty or kindness to the person making it.",
            "Premature odds-citing teaches the machinery that sketching gets punished - it generates fewer pathways next time.",
            "Help that replaces their planning with yours starves their agency; the machinery atrophies from disuse.",
            "Going silent at the moment of failure confirms the worst reading: that the failure is the verdict, not a data point.",
        ],
        "requirements": [
            "Six named mistakes with descriptions.",
            "Each mistake mapped to the component it damages.",
            "The guise-of-virtue structure stated for the set.",
            "Mechanisms for at least the reality hammer, route theft, and abandoned witness.",
            "The visible-errors close plus the non-advice disclaimer.",
        ],
        "standards": [
            "Component-damage framing follows Snyder 2002: hope requiring intact goals, pathways, and agency.",
            "Appraisal-closure framing follows Lazarus 1991: premature closure blocking adaptive reappraisal.",
            "Support-error framing follows the support-provision literature alongside Averill, Catlin and Chon 1990.",
        ],
        "citations": [CIT_SNYDER2002, CIT_LAZARUS1991, CIT_AVERILL],
        "sig_lens": SIG_LENS_DEF,
    },
    # ------------------------------------------------ 32-34 RELATED + SIMULATION
    {
        "key": "neighbors",
        "name": "Hope's Neighbors, Opposites, and Close Cousins",
        "group": "Related Emotions and Mixes",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Hope sits in a crowded neighborhood, and telling the "
            "neighbors apart is practical skill. HOPE VS OPTIMISM: the "
            "closest cousins. Optimism is the general expectation that "
            "things turn out well; hope is the specific machinery - goal, "
            "pathways, agency - aimed at a particular outcome. You can be "
            "optimistic without hoping for anything in particular, and "
            "you can hope fiercely for one thing while expecting little "
            "in general. HOPE VS CONFIDENCE: confidence is certainty "
            "about the outcome; hope is commitment despite uncertainty. "
            "Confidence says it will happen; hope says it could happen, "
            "and I am moving. HOPE VS WISHFUL THINKING: the wish wants "
            "without working - no routes, no steps, no agency. Hope "
            "without pathways collapses into wishing; the test is always "
            "the calendar and the to-do list. HOPE VS FAITH (SECULAR "
            "SENSE): trust placed in a person, process, or future without "
            "full evidence - overlapping territory, but faith is the "
            "trust component while hope is the full three-part machinery. "
            "HOPE VS DESPAIR: the true opposite. Despair is the appraisal "
            "that no pathway exists and none will - the corridor with "
            "every door closed. Note that the opposite of hope is not "
            "fear (fear can coexist with hope) and not sadness (sadness "
            "is about the past; hope is about the future). HOPE VS "
            "EXPECTATION: expectation is the neutral prediction; hope is "
            "the prediction plus the wanting plus the working. The "
            "field test for the whole neighborhood: ask what the person "
            "is DOING. Doing nothing with a good outlook is optimism. "
            "Doing the work under uncertainty is hope. Doing nothing with "
            "a wanted outcome is wishing. Certain of the outcome is "
            "confidence. Closed to all outcomes is despair."
        ),
        "how_it_works": (
            "The distinctions work because each neighbor varies the "
            "three components differently. Optimism varies the scope: "
            "same pleasant future-appraisal, but generalized rather than "
            "goal-locked, and usually without the pathway machinery "
            "running - which is why optimists can be passive. Confidence "
            "varies the certainty: the goal component is identical, but "
            "the probability estimate is near one, which changes the "
            "behavior (less backup-route building, less contingency "
            "planning). Wishful thinking varies the pathways and agency "
            "to zero: goal plus pleasant appraisal with no machinery - "
            "structurally the degenerate case of hope. Faith (secular) "
            "varies the evidence base: the trust component runs ahead of "
            "the data, which can either fund hope's machinery (trusting "
            "the process while working the routes) or substitute for it "
            "(trusting instead of working). Despair varies the pathways "
            "to zero and locks the appraisal: not just no routes now, "
            "but the meta-appraisal that no routes will appear - which "
            "is why despair is so stable and so hard to argue with; "
            "argument targets beliefs, but despair has locked the "
            "appraisal level below belief. Expectation varies the wanting "
            "and the working to zero: pure prediction, no machinery. The "
            "doing-test works because behavior is the downstream readout "
            "of which components are actually running."
        ),
        "key_points": [
            "Hope vs optimism: specific machinery aimed at one outcome versus a general expectation that things turn out well.",
            "Hope vs confidence: commitment despite uncertainty versus certainty about the outcome.",
            "Hope vs wishful thinking: the wish wants without working - hope without pathways collapses into wishing.",
            "Hope vs despair: the true opposite - despair is the locked appraisal that no pathway exists and none will.",
            "The field test: ask what the person is doing - the doing reveals which components are running.",
        ],
        "requirements": [
            "Six neighbor distinctions: optimism, confidence, wishful thinking, faith (secular), despair, expectation.",
            "Each distinction drawn through the three-component lens.",
            "The true-opposite identification with the fear/sadness exclusion explained.",
            "The doing-test as the practical close.",
            "Faith handled in the secular sense only, no religious framing.",
        ],
        "standards": [
            "Component-variation framing follows Snyder 2002: neighbors differing in goals, pathways, agency, certainty, and scope.",
            "Opposite-identification follows Plutchik 1980: opposites as structural inversions on the wheel.",
            "Appraisal-lock framing follows Lazarus 1999: despair as the closed-future appraisal.",
        ],
        "citations": [CIT_SNYDER2002, CIT_PLUTCHIK, CIT_LAZARUS1999],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "mixes",
        "name": "Hope Blends: Hope Mixed With Other Emotions",
        "group": "Related Emotions and Mixes",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Hope rarely travels pure; here are its four most instructive "
            "blends, in the Plutchik style of named dyads. HOPE + FEAR = "
            "THE VIGIL: the corridor is open but the floor is uncertain. "
            "Feels like holding your breath while moving forward - "
            "planning carefully, double-checking routes, sleeping lightly. "
            "This is the blend of everyone awaiting results: the "
            "machinery running with the alarm on low. It looks like "
            "worry from outside but moves like hope - the doing gives it "
            "away. HOPE + GRIEF = THE LANTERN IN THE DARK: hope for what "
            "comes next carried alongside sorrow for what is gone. Feels "
            "like two weathers at once - tears and planning in the same "
            "day. The grief honors the past; the hope sketches the "
            "future; neither cancels the other. This blend is the "
            "everyday texture of recovery. HOPE + ANGER = THE FORGE: hope "
            "aimed at a wrong to be righted. Feels like heat with "
            "direction - the goal sharpens to justice or repair, the "
            "agency runs hot, the pathways get built fast. This blend "
            "moves mountains and needs the pathways audit most, because "
            "hot agency can outrun real routes. HOPE + GRATITUDE = THE "
            "FULL CIRCLE: hope for the future braided with thanks for "
            "the present and past. Feels like warmth in both directions - "
            "the corridor ahead lit by the lamps already walked past. "
            "This is the most stable blend: gratitude keeps the agency "
            "ledger full while hope spends it on the future. Reading "
            "blends is the advanced skill because pure hope is the "
            "textbook case and blended hope is the real-world case. The "
            "rule for all four: name both partners aloud. Unnamed blends "
            "get misread - the vigil as mere anxiety, the forge as mere "
            "rage - and misread blends get mishandled."
        ),
        "how_it_works": (
            "Blends work through component sharing and appraisal "
            "layering. Hope + fear works because the future-appraisal "
            "splits: hope appraises the goal as reachable (open), fear "
            "appraises the path as hazardous (threat) - two appraisals of "
            "different aspects running simultaneously, producing "
            "careful, checked, persistent motion. Hope + grief works "
            "through temporal splitting: grief appraises a past loss "
            "(closed, gone), hope appraises a future possibility (open, "
            "coming) - the brain holds two time-appraisals at once, which "
            "is why the blend feels like two weathers. Hope + anger "
            "works through goal fusion: anger's goal (right the wrong) "
            "merges with hope's machinery (routes plus agency), and the "
            "combined system runs hotter than either alone - anger "
            "supplies activation, hope supplies direction. Hope + "
            "gratitude works through ledger sharing: gratitude's "
            "appraisal (good received) fills the agency account with "
            "evidence that good outcomes happen, and hope spends that "
            "evidence on future goals - the most efficient component "
            "economy of the four. The naming rule works because "
            "labeling both partners keeps both appraisals visible to the "
            "person feeling them, which prevents either from hijacking "
            "the machinery unnoticed."
        ),
        "key_points": [
            "Hope + fear = the vigil: moving forward while holding your breath - careful, checked, persistent.",
            "Hope + grief = the lantern in the dark: tears and planning in the same day; the everyday texture of recovery.",
            "Hope + anger = the forge: heat with direction - moves mountains, needs the pathways audit most.",
            "Hope + gratitude = the full circle: the most stable blend, gratitude filling the ledger that hope spends.",
            "Name both partners aloud: unnamed blends get misread, and misread blends get mishandled.",
        ],
        "requirements": [
            "Four blends with Plutchik-style dyad names.",
            "Each blend: the felt texture, the look from outside, and the mechanism.",
            "The vigil distinguished from mere anxiety by the doing.",
            "The forge's audit warning stated.",
            "The naming rule as the close.",
        ],
        "standards": [
            "Dyad logic follows Plutchik 1980: neighboring and cross-wheel emotions forming named blends.",
            "Appraisal-layering follows Lazarus 1991: multiple simultaneous appraisals of different aspects.",
            "Temporal-splitting follows Frijda 1986: emotions anchored to different time horizons coexisting.",
        ],
        "citations": [CIT_PLUTCHIK, CIT_LAZARUS1991, CIT_FRIJDA],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "full_simulation",
        "name": "The Full Simulation: Hope From Trigger to Resolution",
        "group": "Related Emotions and Mixes",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The showcase simulation: one hope, end to end. SCENE ONE, "
            "THE SPARK: Tuesday morning. An email arrives - the training "
            "program has a seat, the application accepted, the door that "
            "was a wall for two years. The breath catches halfway. The "
            "gaze lifts to the window. Inner monologue: maybe. Just "
            "maybe. The corridor opens. SCENE TWO, THE SKETCHING: by "
            "noon the kitchen table is covered in paper. Routes multiply: "
            "the schedule rearranged, the costs mapped, the childcare "
            "solved two ways, a backup program identified in case. Each "
            "surviving route adds a degree of warmth. The slow nod, the "
            "exhale. Agency stirring: I can actually do this. SCENE THREE, "
            "THE TELLING: dinner. The hope is spoken aloud, conditionally - "
            "here is the plan, here is plan B. The listener adds a route "
            "nobody had seen (the evening class, the employer's program). "
            "The shared picture makes the goal feel nearer. Borrowed "
            "agency, spent immediately. SCENE FOUR, THE DIP: week three. "
            "A form rejected, a cost higher than mapped, a voice saying "
            "be realistic. The corridor narrows. For a day the machinery "
            "idles - the gaze drops, the grammar goes past-locked. Then "
            "the rerouting: a different form, a payment plan, the "
            "evening class from scene three promoted to plan A. The "
            "recovery itself becomes evidence - the system has now "
            "survived a closure, which is worth three sparks. SCENE FIVE, "
            "THE MOBILIZATION: weeks four through ten. The goal "
            "reorganizes life: mornings start with the next step named, "
            "small wins counted nightly, the backup route kept warm. "
            "Setbacks rerouted within hours. The walk quickens. Others "
            "are recruited - a study partner, a mentor. The blaze level: "
            "transmission. SCENE SIX, THE RESOLUTION: the first day. The "
            "goal, arrived at. Hope discharges into satisfaction and "
            "gratitude - its job done, the machinery standing down. The "
            "last image: the same kitchen table, the papers now a neat "
            "stack, and the particular quiet of a corridor fully walked. "
            "SCENE SEVEN, THE AFTERSHOCK: months later, a hard week. The "
            "memory of this hope replays - the dip survived, the "
            "rerouting, the arrival - and the replay re-warms the "
            "machinery for the next goal. This is the archive's promise "
            "in miniature: hope is not a mood but a machine, and machines "
            "can be understood, maintained, and run. All characters and "
            "events are illustrative fiction for education; no real "
            "person is described or diagnosed."
        ),
        "how_it_works": (
            "The simulation works by running every mechanism in this "
            "database in sequence, in one continuous case. The spark "
            "runs onset: a single information event flipping the "
            "future-appraisal from closed to open. The sketching runs "
            "the pathways component at full gain: multiple live routes "
            "with a backup, each confirmation feeding agency. The "
            "telling runs social pooling: transmitted machinery, "
            "borrowed agency, the listener's donated route becoming "
            "plan A later - the cascade's contagion stage in miniature. "
            "The dip runs closure and rerouting: a blocked route "
            "draining hope, then flexible pathways reopening it, with "
            "the recovery itself becoming agency evidence (survived "
            "closures are the strongest fuel). The mobilization runs "
            "the escalation ladder: resource commitment tracking agency "
            "gain, transmission behavior at the blaze level. The "
            "resolution runs goal discharge: the machinery standing "
            "down into satisfaction and gratitude. The aftershock runs "
            "memory replay: the stored episode becoming personal proof "
            "for the next goal - the private trigger set gaining a new "
            "member. Every scene is labeled with its mechanism so the "
            "simulation teaches while it shows: this is the full "
            "behavioral model of hope, executable as understanding."
        ),
        "key_points": [
            "Seven scenes: the spark, the sketching, the telling, the dip, the mobilization, the resolution, the aftershock.",
            "Every scene runs a named mechanism from this database: onset, pathways gain, social pooling, rerouting, escalation, discharge, memory replay.",
            "The dip's recovery becomes the strongest agency evidence: survived closures are worth three sparks.",
            "The telling's donated route becoming plan A shows the cascade's contagion stage in miniature.",
            "The aftershock shows the episode becoming personal proof - the private trigger set gaining a new member.",
        ],
        "requirements": [
            "At least six scenes from trigger through peak to resolution plus aftershock.",
            "Inner monologue, body signals, facial expression, dialogue, and behavior present across the scenes.",
            "Each scene tied to a named mechanism from the database.",
            "The dip-and-rerouting recovery shown as agency evidence.",
            "The illustrative-fiction disclaimer: no real person described or diagnosed.",
        ],
        "standards": [
            "Sequential-mechanism framing follows Snyder 2002: the full hope episode as goals-pathways-agency in motion.",
            "Discharge framing follows Frijda 1986: emotion resolution on goal attainment.",
            "Memory-replay framing follows Barrett 2017: stored episodes reconstructing future emotion.",
        ],
        "citations": [CIT_SNYDER2002, CIT_FRIJDA, CIT_BARRETT],
        "sig_lens": SIG_LENS_DEF,
    },
]
