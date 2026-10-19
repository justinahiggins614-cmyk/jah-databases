#!/usr/bin/env python3
"""Entries for the Gratitude Emotion databases (Manon's 16:15 orders, emotion series).

Creates two NEW databases, 34 ladder-ordered records each:

  emotion-gratitude            - The Gratitude Emotion Database
                           (public-harvest: real, fact-checked psychology of
                           gratitude - definition, family placement, intensity,
                           first-person simulation, body signals, facial
                           expression, triggers, behavior, healthy expression,
                           recognition in others, related emotions and mixes,
                           full behavioral simulation; descriptive and
                           educational only - never diagnosing real people;
                           standard references Emmons and McCullough 2003;
                           McCullough, Kilpatrick, Emmons and Larson 2001;
                           Emmons 2007; Watkins, Woodward, Stone and Kolts
                           2003; Wood, Froh and Geraghty 2010; Algoe 2012;
                           Fredrickson 2004; Bartlett and DeSteno 2006;
                           Lazarus and Lazarus 1994; Ortony, Clore and
                           Collins 1988; Plutchik 1980; Russell 1980; Ekman
                           1999; Frijda 1986; Scherer 2005; Barrett 2017;
                           Izard 1992; Darwin 1872; Ekman and Friesen FACS
                           1978; APA Dictionary of Psychology)
  emotion-gratitude-signature  - The Gratitude Emotion Signature Database
                           (his original Signature Gratitude Method:
                           gratitude as the ground wire of the system - the
                           return path that closes the loop: notice the
                           good, name the giver, send the current back,
                           watch the whole system brighten; src signature,
                           titles suffixed " (Signature Edition)", never
                           presented as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
non-decreasing; ladder_tier foundations/compounded/advanced); the shard
index is written in ladder order so pages present simple -> compounded ->
complex.

ID prefixes: JAH-EMGT- (public) and JAH-EMGTS- (signature), verified free
in the manifest (zero EMGT hits across all id_prefix values) and in every
shard record ID (zero JAH-EMGT hits across all data/manifest.json id_prefix
values AND all record IDs in jah-databases-data-1/data/); JAH-EM- is an
existing unrelated prefix but shares no substring collision with JAH-EMGT-
since "JAH-EMGT-..." does not start with "JAH-EM-".

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_emotion_gratitude.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos. Demo outputs were
cross-checked against entry text during authoring.

Descriptive/educational only: this database describes and simulates the
emotion of gratitude. It never diagnoses real people, never labels any real
person with an emotional state, and offers only general, safe, everyday
guidance. No clinical language, no diagnostic labels. No religious framing.

Never the words "bat belt" anywhere. No website references. No Facebook.
No religious talk.
"""

SIG_TAIL = ("Signature original - his original Signature Gratitude Method: "
            "gratitude as the ground wire of the system, the return path "
            "that closes the loop - notice the good, name the giver, send "
            "the current back, watch the whole system brighten. Clearly "
            "labeled Signature-made, never presented as authentic public "
            "record.")

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
CIT_LAZARUS1994 = ("Lazarus RS, Lazarus BN. Passion and Reason: Making Sense "
                   "of Our Emotions. New York: Oxford University Press; "
                   "1994.")
CIT_FRIJDA = ("Frijda NH. The Emotions. Cambridge: Cambridge University "
              "Press; 1986.")
CIT_SCHERER = ("Scherer KR. What are emotions? And how can they be measured? "
               "Soc Sci Inf. 2005;44(4):695-729.")
CIT_BARRETT = ("Barrett LF. How Emotions Are Made: The Secret Life of the "
               "Brain. Boston: Houghton Mifflin Harcourt; 2017.")
CIT_IZARD = ("Izard CE. Basic emotions, relations among emotions, and "
             "emotion-cognition relations: a review of the evidence. Psychol "
             "Rev. 1992;99(3):561-565.")
CIT_APA = ("American Psychological Association. APA Dictionary of Psychology. "
           "Gratitude entry: a sense of thankfulness and happiness in "
           "response to receiving a gift, either a tangible benefit or a "
           "moment of peaceful bliss. Washington DC: APA.")
CIT_EMMONS2003 = ("Emmons RA, McCullough ME. Counting blessings versus "
                  "burdens: an experimental investigation of gratitude and "
                  "subjective well-being in daily life. J Pers Soc Psychol. "
                  "2003;84(2):377-389.")
CIT_MCCULLOUGH2001 = ("McCullough ME, Kilpatrick SD, Emmons RA, Larson DB. "
                      "Is gratitude a moral affect? Psychol Bull. "
                      "2001;127(2):249-266.")
CIT_EMMONS2007 = ("Emmons RA. Thanks! How the New Science of Gratitude Can "
                  "Make You Happier. Boston: Houghton Mifflin; 2007.")
CIT_WATKINS2003 = ("Watkins PC, Woodward K, Stone T, Kolts RL. Gratitude and "
                   "happiness: development of a measure of gratitude, and "
                   "relationships with subjective well-being. Soc Behav "
                   "Pers. 2003;31(8):431-452.")
CIT_WOOD2010 = ("Wood AM, Froh JJ, Geraghty AWA. Gratitude and well-being: "
                "a review and theoretical integration. Clin Psychol Rev. "
                "2010;30(7):890-905.")
CIT_ALGOE2012 = ("Algoe SB. Find, remind, and bind: the functions of "
                 "gratitude in everyday relationships. Soc Personal Psychol "
                 "Compass. 2012;6(6):455-469.")
CIT_FREDRICKSON2004 = ("Fredrickson BL. Gratitude, like other positive "
                       "emotions, broadens and builds. In: Emmons RA, "
                       "McCullough ME, eds. The Psychology of Gratitude. New "
                       "York: Oxford University Press; 2004:145-166.")
CIT_BARTLETT2006 = ("Bartlett MY, DeSteno D. Gratitude and prosocial "
                    "behavior: helping when it costs you. Psychol Sci. "
                    "2006;17(8):319-325.")
CIT_ORTONY1988 = ("Ortony A, Clore GL, Collins A. The Cognitive Structure of "
                  "Emotions. Cambridge: Cambridge University Press; 1988.")
CIT_KUMAR2018 = ("Kumar A, Epley N. Undervaluing gratitude: expressers "
                 "misunderstand the consequences of showing appreciation. "
                 "Psychol Sci. 2018;29(9):1423-1435.")

SIG_LENS_DEF = ("The Signature read: gratitude is the ground wire of the "
                "system. Where public psychology charts the feeling, the "
                "Signature Gratitude Method treats gratitude as the return "
                "path - the current that flows back to the source, closing "
                "the loop. Joy is the home signal; gratitude is what keeps "
                "the circuit alive: notice the good, name the giver, send "
                "the current back, watch the whole system brighten. Every "
                "gratitude record below carries the same public facts, "
                "reframed as his original Signature engineering of the "
                "feeling.")

ENTRIES = [
    # ------------------------------------------------ 1-4 WHAT GRATITUDE IS
    {
        "key": "definition",
        "name": "What Gratitude Is: A Plain-Language Definition",
        "group": "What the Emotion Is",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Gratitude is the feeling of thankful gladness that arrives when "
            "you recognize that something good came to you from outside "
            "yourself - from another person, from circumstance, from the way "
            "the day happened to turn out. In plain words, gratitude is the "
            "felt thank-you: the mind registering a benefit received, and "
            "the heart warming toward whatever brought it. The psychology "
            "reference books describe it as a sense of thankfulness and "
            "happiness in response to receiving a gift, whether that gift is "
            "a tangible favor or simply a moment of peaceful gladness. It "
            "is not the same as pleasure, which needs no giver, and not the "
            "same as pride, which looks inward at what you did. Gratitude "
            "looks outward and slightly upward: something or someone helped, "
            "and you know it. It can be about the big things - a rescue, a "
            "second chance, years of quiet support - and about the small "
            "ones, like a stranger holding a door or a friend remembering "
            "your birthday. Size does not define it; the recognition does. "
            "Everyone has felt it, because everyone has received more than "
            "they earned. This database describes the emotion from every "
            "angle - what it is, how it feels, how it shows, and how it can "
            "be expressed well - purely as education and description. It "
            "never diagnoses anyone and never labels any real person."
        ),
        "how_it_works": (
            "Gratitude works as an appraisal with two parts. First the mind "
            "detects a benefit: something good landed in your lap. Then it "
            "detects a source: the benefit came from somewhere outside your "
            "own doing - a person who helped, a turn of luck, a generous "
            "moment. When both appraisals fire, the feeling of gratitude "
            "rises, and with it an urge to acknowledge the source: to say "
            "thank you, to repay the kindness, to pass it onward. "
            "Researchers describe gratitude as a moral affect with three "
            "jobs: it acts as a barometer that tells you a benefit has been "
            "received, as a motive that pushes you to act kindly in return, "
            "and as a reinforcer that encourages the giver to keep giving. "
            "That is why gratitude strengthens bonds: the feeling is the "
            "system's way of marking who helped you and pulling you closer "
            "to them. It is fast - the appraisal can happen in a fraction "
            "of a second, before any deliberate thought - and it is social "
            "by design: gratitude exists to keep the give-and-take of human "
            "life flowing."
        ),
        "key_points": [
            "Gratitude is the felt thank-you: the mind registering a benefit received from outside yourself, and warming toward its source.",
            "It is a complex social emotion - not one of the basic six, but built from appreciation plus the recognition of a giver.",
            "Two appraisals make it: a benefit detected, and a source outside your own doing detected.",
            "Gratitude works as a moral affect: a barometer of benefits, a motive to repay kindness, and a reinforcer that keeps givers giving.",
            "Size does not define it: a rescue and a held door can both be real gratitude - the recognition does the work.",
        ],
        "requirements": [
            "A plain-language definition that an ordinary reader recognizes from their own life.",
            "Clear separation from neighboring states like pleasure, pride, contentment, and admiration.",
            "Coverage of both big and small gratitude so the definition does not only fit milestones.",
            "The two-part appraisal (benefit + source) stated plainly.",
            "A stated educational boundary: description only, never diagnosis of any real person.",
        ],
        "standards": [
            "Definitions follow the APA Dictionary of Psychology gratitude entry: thankfulness and happiness in response to receiving a gift.",
            "The moral-affect account follows McCullough, Kilpatrick, Emmons and Larson 2001: barometer, motive, and reinforcer functions.",
            "The appraisal structure follows Ortony, Clore and Collins 1988: approval of another's praiseworthy action plus pleasure at a desirable outcome.",
        ],
        "citations": [CIT_APA, CIT_MCCULLOUGH2001, CIT_ORTONY1988],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "family",
        "name": "Where Gratitude Sits in the Emotion Family",
        "group": "What the Emotion Is",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Gratitude sits in the warm, pleasant neighborhood of the emotion "
            "family, right where joy meets trust. On Plutchik's emotion "
            "wheel, the closest thing to gratitude is the blend of joy and "
            "acceptance - the gladness of joy aimed at a trusted source. It "
            "is not a basic emotion in the classic sense: it has no single "
            "universal facial signal the way anger or fear do, and it "
            "requires a small piece of thinking - the recognition of a "
            "benefit and a giver - before it can fully form. That makes it "
            "a complex, or secondary, emotion: built from simpler parts, "
            "colored by thought. Its nearest cousins are appreciation (the "
            "warm noticing of good things, without needing a giver), "
            "admiration (warmth toward someone's excellence, without "
            "needing to benefit from it), and relief (the glad exhale when "
            "danger passes). Its most common partners are joy, which it "
            "often arrives with, and love, which it deepens. On Russell's "
            "circumplex map of feelings, gratitude lands in the pleasant, "
            "moderately activated quadrant: warm and upbeat, but calmer than "
            "ecstasy and softer than triumph. Knowing its address helps you "
            "recognize it: gratitude is the warm, directed, thankful feeling "
            "that points back toward whoever or whatever helped."
        ),
        "how_it_works": (
            "Emotion families are organized by what the feeling is about and "
            "what it moves you to do. Gratitude's subject is always a "
            "benefit traced to a source, and its action tendency is always "
            "toward the source: approach, acknowledge, repay, strengthen the "
            "bond. That is what puts it in the prosocial branch of the "
            "family, alongside love, compassion, and admiration - the "
            "emotions whose business is connection. Researchers who study "
            "the structure of feelings place gratitude among the empathic "
            "emotions, the ones that arise from recognizing what someone "
            "else did for you. The blend account explains its flavor: take "
            "joy's warm gladness, aim it at a trusted benefactor, and add "
            "the slight humility of knowing you did not earn it alone - "
            "that compound is gratitude. Because it is built from parts, it "
            "blends easily: it mixes with joy into celebration, with relief "
            "into deliverance, with sadness into bittersweet thankfulness, "
            "and with awe into reverence. The family map is not just "
            "taxonomy; it predicts behavior. Emotions in the prosocial "
            "branch reliably make people more generous, more cooperative, "
            "and more willing to help strangers - and gratitude is one of "
            "the strongest of them at doing exactly that."
        ),
        "key_points": [
            "Gratitude is a complex (secondary) emotion: joy's warmth aimed at a trusted source, plus the recognition of a benefit.",
            "It has no single universal facial signal like the basic emotions - it is built from parts and colored by thought.",
            "Nearest cousins: appreciation, admiration, relief; most common partners: joy and love.",
            "On the circumplex it sits in the pleasant, moderately activated quadrant - warm and upbeat but calm.",
            "It belongs to the prosocial branch: the emotions whose business is connection and generosity.",
        ],
        "requirements": [
            "Placement of gratitude as complex/secondary rather than basic, with the reason stated.",
            "The blend account: which simpler feelings combine into gratitude.",
            "Named nearest cousins and partners, with one-line distinctions.",
            "Circumplex coordinates stated: pleasant, moderately activated.",
            "The behavioral prediction: what the prosocial branch reliably makes people do.",
        ],
        "standards": [
            "The blend placement follows Plutchik 1980: gratitude near the joy-acceptance region of the wheel.",
            "The circumplex placement follows Russell 1980: pleasant valence with moderate activation.",
            "The empathic-emotion classification follows Lazarus and Lazarus 1994.",
        ],
        "citations": [CIT_PLUTCHIK, CIT_RUSSELL, CIT_LAZARUS1994],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "intensity",
        "name": "The Gratitude Dial: Mild, Moderate, and Intense",
        "group": "What the Emotion Is",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Gratitude comes with a volume dial. At the low end is quiet "
            "appreciation: you notice the good thing, nod inwardly, and move "
            "on - the warm flicker when the barista remembers your order. In "
            "the middle is full thankfulness: the heart warms, the smile "
            "comes unbidden, you say thank you and mean it, and the moment "
            "stays with you for a while. At the high end is overwhelming "
            "gratitude: the throat tightens, the eyes fill, words fail, and "
            "the feeling takes over the whole body - the moment a stranger's "
            "kindness at your lowest point, or a loved one's sacrifice "
            "finally understood, lands all at once. The same emotion runs "
            "through all three; what changes is the size of the benefit, "
            "how much it cost the giver, how much you needed it, and how "
            "surprised you are. Researchers who measure the grateful "
            "disposition find the same dial in people: some run warm most "
            "of the time, noticing gifts everywhere, while others feel "
            "gratitude only when the benefit is large and obvious. Neither "
            "setting is a diagnosis - they are simply different tunings of "
            "the same instrument. Learning the dial matters because the "
            "volume tells you something: mild gratitude says a good thing "
            "happened; intense gratitude says something that mattered deeply "
            "just changed your ledger."
        ),
        "how_it_works": (
            "The intensity of gratitude is computed from a small set of "
            "inputs. Benefit size counts: the bigger the good received, the "
            "louder the feeling. Cost to the giver counts: a favor that "
            "clearly cost someone time, money, or effort feels heavier than "
            "an easy one. Need counts: help that arrives when you are "
            "desperate registers far louder than the same help on an easy "
            "day. Surprise counts: the unexpected kindness hits harder than "
            "the expected one, because the appraisal system weights "
            "novelty. And perceived intention counts: help given freely and "
            "warmly outranks help given grudgingly, because the mind reads "
            "the giver's heart as part of the gift. These inputs combine "
            "into the felt volume, which then sets the output: mild "
            "gratitude produces a nod and a brief thank-you; moderate "
            "gratitude produces warmth, a real smile, and the urge to repay; "
            "intense gratitude can produce tears, speechlessness, and "
            "life-redirecting resolves. The pleasantness stays high at every "
            "setting - gratitude never turns bitter at volume the way anger "
            "does. Only the energy changes. That is why the dial is a "
            "useful instrument: same feeling, same direction, more or less "
            "current flowing."
        ),
        "key_points": [
            "Gratitude runs mild (quiet appreciation) to moderate (warm thankfulness) to intense (overwhelming, sometimes tearful).",
            "Five inputs set the volume: benefit size, cost to the giver, your need, surprise, and perceived intention.",
            "Pleasantness stays high at every setting - only the energy changes, never the direction.",
            "People differ in their default tuning: some run warm most of the time, others only at large benefits.",
            "The volume carries information: mild says a good thing happened; intense says your ledger just changed.",
        ],
        "requirements": [
            "Three named bands with lived examples at each level.",
            "The five intensity inputs stated with the mechanism each works through.",
            "The constant-pleasantness rule stated explicitly.",
            "Individual tuning differences described without diagnosing anyone.",
            "The informational reading of intensity: what each volume means.",
        ],
        "standards": [
            "The benefit and cost appraisal inputs follow Ortony, Clore and Collins 1988.",
            "The grateful-disposition tuning differences follow Watkins, Woodward, Stone and Kolts 2003.",
            "The intensity structure follows the appraisal-intensity account in Scherer 2005.",
        ],
        "citations": [CIT_ORTONY1988, CIT_WATKINS2003, CIT_SCHERER],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "myths",
        "name": "Myths and Misunderstandings About Gratitude",
        "group": "What the Emotion Is",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Gratitude is widely praised and widely misunderstood. The first "
            "myth is that gratitude means pretending everything is fine: "
            "that a grateful person has no complaints and no grief. In "
            "truth, gratitude coexists with pain perfectly well - you can be "
            "grateful for the nurse while furious at the illness, thankful "
            "for a friend while grieving a loss. The second myth is that "
            "gratitude requires a benefactor with a face: but people feel "
            "genuine gratitude toward luck, toward nature, toward the "
            "anonymous stranger, toward the way things turned out. The third "
            "myth is that saying thank you is the whole of it: but the "
            "feeling and the expression are different things, and a "
            "well-mannered thank-you with no warmth behind it is manners, "
            "not gratitude. The fourth myth is that gratitude is just "
            "positive thinking dressed up: in fact it is specific and "
            "evidence-based, a response to an actual benefit received, not a "
            "vague optimism about life. The fifth myth is that feeling "
            "grateful puts you in someone's debt: genuine gratitude feels "
            "like warmth, not owing - the heavy indebted feeling is a "
            "different emotion wearing gratitude's clothes. The sixth myth "
            "is that gratitude is automatic if you just list good things: "
            "the listing helps, but the feeling arrives when the benefit "
            "and the source are truly recognized, which is why the same "
            "exercise moves some people deeply and leaves others cold. "
            "Clearing these myths matters because each one blocks the real "
            "thing: people who believe gratitude means denying pain will "
            "refuse it when they hurt most, which is exactly when it helps "
            "most."
        ),
        "how_it_works": (
            "Myths about gratitude work by mislabeling the appraisal. The "
            "'everything is fine' myth tells people that noticing pain "
            "cancels thankfulness, when the two appraisals run on separate "
            "tracks: one evaluates what hurts, the other evaluates what "
            "helped. Research on benefit-finding shows people can hold both "
            "at full strength. The 'must have a benefactor' myth narrows "
            "the source slot, when the mind happily fills it with "
            "circumstance, nature, or chance - the appraisal needs a source, "
            "not necessarily a person. The 'thanks equals gratitude' myth "
            "confuses the display rule with the feeling: saying the words "
            "is the social signal, and it can run with the tank empty. The "
            "'positive thinking' myth mistakes a specific, evidence-based "
            "appraisal for a general attitude, which is why gratitude "
            "responds to concrete benefits and not to slogans. The "
            "'gratitude equals debt' myth confuses two different emotions: "
            "indebtedness is the heavy, obligated feeling that pushes you "
            "to repay to restore balance, while gratitude is the warm "
            "feeling that pulls you toward the giver - they can co-occur, "
            "but they are not the same circuit. Each correction restores a "
            "piece of the real mechanism, and the real mechanism is what "
            "the rest of this database describes."
        ),
        "key_points": [
            "Gratitude coexists with pain: you can be thankful for the nurse while furious at the illness.",
            "No human benefactor is required: luck, nature, circumstance, and anonymous strangers all count as sources.",
            "Saying thank you is the signal, not the feeling - manners can run with the tank empty.",
            "Gratitude is specific and evidence-based, not vague optimism: it responds to actual benefits received.",
            "Gratitude is not indebtedness: warmth toward the giver is one circuit, heavy obligation is another.",
            "Listing good things helps only when the benefit and source are truly recognized.",
        ],
        "requirements": [
            "Six named myths, each stated and corrected with the mechanism.",
            "The pain-coexistence correction with a concrete example.",
            "The benefactor myth corrected with the source-slot account.",
            "The thanks-vs-feeling distinction stated plainly.",
            "The gratitude-vs-indebtedness distinction stated as two circuits.",
        ],
        "standards": [
            "The gratitude-indebtedness distinction follows Watkins and colleagues 2006 and the moral-affect account of McCullough, Kilpatrick, Emmons and Larson 2001.",
            "The specificity claim follows Emmons and McCullough 2003: gratitude responds to concrete benefits.",
            "The review-level grounding follows Wood, Froh and Geraghty 2010.",
        ],
        "citations": [CIT_MCCULLOUGH2001, CIT_EMMONS2003, CIT_WOOD2010],
        "sig_lens": SIG_LENS_DEF,
    },
    # ------------------------------------------------ 5-9 HOW IT FEELS
    {
        "key": "first_person",
        "name": "Inside the Feeling: Gratitude in the First Person",
        "group": "How It Feels",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "From the inside, gratitude feels like warmth with an address. "
            "It starts as a small catch in the chest - the moment the mind "
            "finishes the sentence 'they did not have to do that, and they "
            "did it anyway.' Then comes the spreading: a loosening behind "
            "the ribs, a softening of the face you did not order, a sense "
            "of being, for a moment, held rather than holding everything "
            "up yourself. Time slows a fraction; the thing you were rushing "
            "toward matters slightly less, and the person in front of you "
            "matters slightly more. There is often a specific image that "
            "replays: their hands doing the thing, the exact words they "
            "used, the look on their face - the mind seems to want to keep "
            "the evidence. Underneath the warmth there is usually a quiet "
            "humility, not the crushing kind, just the plain recognition: "
            "I could not have done this alone, and I did not have to. "
            "Then the urge arrives, and it is not an obligation - it feels "
            "more like pressure behind a dam: you want to say it, to do "
            "something, to make sure they know. If you let it out - the "
            "thank-you, the returned favor, the note - the warmth completes "
            "itself and settles into a glow that can last for hours. If you "
            "swallow it, it does not vanish; it sits, warm and slightly "
            "aching, waiting for its exit. That is the inside of gratitude: "
            "recognition, warmth, replay, humility, and the urge to send "
            "something back."
        ),
        "how_it_works": (
            "The first-person sequence of gratitude follows the appraisal "
            "chain in real time. The catch in the chest marks the benefit "
            "detection: the mind has registered that something good arrived "
            "unearned. The spreading warmth marks the source attribution: "
            "the good is traced to someone or something outside the self, "
            "and the body's reward circuitry answers with the same warm "
            "chemistry it uses for social bonding. The replay of the image "
            "is the memory system flagging the event as worth keeping - "
            "gratitude is, among other things, a memory tag that says 'this "
            "person helped; remember them.' The humility is the self-model "
            "updating: the story shifts from 'I handle everything' to 'I "
            "am helped,' which is why gratitude reliably deflates arrogance "
            "without touching self-respect. The urge to send something back "
            "is the moral-motive function firing: the prosocial circuitry "
            "priming repayment or pay-it-forward behavior. And the settling "
            "glow after expression is the loop closing: the social bond is "
            "confirmed, the ledger feels balanced, and the nervous system "
            "stands down. Each phase is observable from the outside, which "
            "is why the later records on face, body, and behavior can read "
            "this same sequence in another person."
        ),
        "key_points": [
            "From the inside, gratitude is warmth with an address: the mind finishes 'they did not have to, and they did.'",
            "The sequence runs: recognition, chest warmth, image replay, quiet humility, then the urge to send something back.",
            "The replay is a memory tag: 'this person helped; remember them.'",
            "The humility updates the self-model from 'I handle everything' to 'I am helped.'",
            "Expression closes the loop: the warmth settles into a glow; swallowed thanks sit warm and aching.",
        ],
        "requirements": [
            "A continuous first-person passage covering the feeling as it happens.",
            "The five-phase sequence named and ordered.",
            "The memory-tag function of the replay stated.",
            "The humility phase described as self-model update, not self-punishment.",
            "The expression-vs-swallowing fork stated with its different endings.",
        ],
        "standards": [
            "The appraisal sequence follows Lazarus 1991 and Ortony, Clore and Collins 1988.",
            "The moral-motive phase follows McCullough, Kilpatrick, Emmons and Larson 2001.",
            "The constructionist framing follows Barrett 2017: the feeling as the brain's read-out of the appraisal chain.",
        ],
        "citations": [CIT_LAZARUS1991, CIT_MCCULLOUGH2001, CIT_BARRETT],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "time_course",
        "name": "How Gratitude Moves Through Time",
        "group": "How It Feels",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "Gratitude has a characteristic shape in time. The onset is "
            "quick: the benefit lands, the source is recognized, and the "
            "warmth arrives within seconds - sometimes mid-sentence, while "
            "the thank-you is still forming. The peak comes minutes later, "
            "when the full weight of what happened sinks in: this is the "
            "phase of the tight throat, the bright eyes, the need to say it "
            "properly. Then the fading begins, and it is gentler than most "
            "emotions' fade: gratitude does not crash, it settles. The sharp "
            "warmth softens into a background glow that can last hours, and "
            "with each remembering - the replay of the moment later that "
            "day - a smaller echo of the feeling returns. That is the "
            "aftershock pattern: gratitude is re-triggerable by its own "
            "memory, so a single kindness can warm you three or four times "
            "as you retell it. Over days, the acute feeling resolves into "
            "something quieter but more durable: a changed attitude toward "
            "the giver, a stored readiness to help them back, a small "
            "permanent brightening of the relationship. And underneath all "
            "of it runs the slow background version - the grateful "
            "disposition, the trait-level tuning that makes some people "
            "notice gifts everywhere. State gratitude is the weather; trait "
            "gratitude is the climate. The weather passes in hours; the "
            "climate shapes years."
        ),
        "how_it_works": (
            "The time course of gratitude follows the decay pattern of "
            "appraisal-driven emotions with one special feature: "
            "re-triggerability. Onset is fast because the appraisal is "
            "simple - benefit detected, source detected, done - and the "
            "body answers immediately with the warm chemistry of social "
            "reward. The peak lags the onset because full comprehension "
            "takes longer than detection: the mind needs a minute to total "
            "up what the benefit cost the giver and what it means for you. "
            "The fade is slow because there is no threat to resolve and no "
            "goal to abandon; nothing pushes the system to stand down "
            "quickly, so the feeling decays on the slow metabolic schedule "
            "of positive affect. The aftershocks come from the memory tag: "
            "each recall of the event re-runs a diluted copy of the "
            "appraisal, producing a smaller echo of the feeling - which is "
            "why telling the story of a kindness re-warms the teller. The "
            "resolution into attitude change is the learning system doing "
            "its job: the benefactor's entry in your social ledger is "
            "permanently upgraded. The trait level underneath is the "
            "dispositional tuning studied by gratitude researchers: a "
            "standing readiness to run this whole sequence, which predicts "
            "how often the weather of state gratitude will visit."
        ),
        "key_points": [
            "Onset is quick (seconds), the peak lags by minutes as the full weight sinks in, and the fade is gentle - gratitude settles, it does not crash.",
            "The aftershock pattern: remembering the kindness re-triggers a smaller echo, so one gift can warm you several times.",
            "Over days the acute feeling resolves into a changed attitude: an upgraded ledger entry for the giver.",
            "State gratitude is the weather (hours); trait gratitude is the climate (years).",
            "The fade is slow because there is no threat to resolve and no goal to abandon.",
        ],
        "requirements": [
            "Four named phases: onset, peak, fading, aftershock, each with its timing.",
            "The aftershock mechanism explained via the memory tag.",
            "The resolution into lasting attitude change stated.",
            "The state-vs-trait distinction stated plainly.",
            "The slow-fade mechanism explained (no threat, no abandoned goal).",
        ],
        "standards": [
            "The appraisal-timing account follows Scherer 2005 and Lazarus 1991.",
            "The state-trait distinction follows the grateful-disposition literature: Watkins, Woodward, Stone and Kolts 2003; Emmons and McCullough 2003.",
            "The positive-affect decay framing follows Fredrickson 2004.",
        ],
        "citations": [CIT_SCHERER, CIT_WATKINS2003, CIT_FREDRICKSON2004],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "low_vs_high",
        "name": "Gratitude at Low and High Intensity: Two Lived Snapshots",
        "group": "How It Feels",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "Low gratitude, level two on the dial: you are at the counter, "
            "the cashier slides your change across with a tired smile and "
            "says have a good one. Something in you registers it - a small "
            "warmth, a nod, a 'you too' that you actually mean. The feeling "
            "is light and brief: a flicker behind the ribs, gone by the "
            "time you reach the door, but it leaves the next ten minutes "
            "slightly brighter. You do not replay it. You do not need to "
            "tell anyone. It is the emotional equivalent of noticing the "
            "weather is nice. High gratitude, level nine: it is late, your "
            "car has died on an empty road, and a stranger stops, spends "
            "forty minutes in the cold getting you going, and waves off "
            "your money with 'just help somebody else sometime.' Your "
            "throat closes. Your eyes fill before you can stop them. The "
            "warmth is not a flicker but a flood - chest, face, hands. "
            "Words feel insultingly small; 'thank you' comes out cracked "
            "and you say it three times anyway. You replay his face for "
            "days. You tell the story for years. You actually do help "
            "somebody else, months later, and think of him while you do "
            "it. Same emotion in both scenes - benefit recognized, source "
            "outside yourself, warmth toward the giver. The difference is "
            "only the current: a trickle versus a river. Learning to feel "
            "both, and to honor the trickle instead of waiting for the "
            "river, is most of what the gratitude practices teach."
        ),
        "how_it_works": (
            "The two snapshots differ only in the inputs to the same "
            "appraisal circuit. In the low scene, the benefit is small (a "
            "kind word), the cost to the giver is tiny, the need is low, "
            "and the surprise is mild - so the felt volume stays at a "
            "flicker, enough to register and brighten the minutes after, "
            "not enough to demand expression or replay. In the high scene, "
            "every input is maxed: the benefit is large (rescue from real "
            "trouble), the cost is high (forty cold minutes), the need is "
            "acute (stranded at night), the surprise is total (a stranger), "
            "and the intention is pure (money refused). The same circuit "
            "outputs a flood: tears, speechlessness, days of replay, and a "
            "behavioral resolve that actually fires months later. The "
            "pleasantness is high in both - even the flicker feels good - "
            "which is why the dial metaphor holds: one instrument, one "
            "direction, different current. The practical lesson sits in the "
            "middle: most of life's gratitude opportunities are low-level "
            "flickers, and the people who report the warmest lives are not "
            "the ones who wait for rivers but the ones who learn to notice "
            "trickles. The appraisal circuit does not care about scale; it "
            "cares about recognition. Train the recognition, and the dial "
            "spends more of the day above zero."
        ),
        "key_points": [
            "Low gratitude is a flicker: noticed, brief, brightening the minutes after, needing no replay.",
            "High gratitude is a flood: tears, cracked words, days of replay, resolves that fire months later.",
            "Both run the same appraisal circuit - only the five inputs differ in strength.",
            "Pleasantness is high at both levels: the dial changes current, never direction.",
            "Most of life's gratitude is low-level; the warmest lives come from noticing trickles, not waiting for rivers.",
        ],
        "requirements": [
            "Two concrete lived snapshots, one low and one high, with sensory detail.",
            "The same-circuit claim stated: identical appraisal, different input strengths.",
            "The input-by-input comparison across the two scenes.",
            "The constant-pleasantness rule restated for the pair.",
            "The practical lesson: training recognition of low-level moments.",
        ],
        "standards": [
            "The appraisal-input account follows Ortony, Clore and Collins 1988.",
            "The recognition-training lesson follows Emmons and McCullough 2003 and Emmons 2007.",
            "The intensity-band structure follows the appraisal-intensity account in Scherer 2005.",
        ],
        "citations": [CIT_ORTONY1988, CIT_EMMONS2007, CIT_SCHERER],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "gratitude_joy_blend",
        "name": "Gratitude Mixed with Joy: Its Most Common Partner",
        "group": "How It Feels",
        "ladder_rank": 5,
        "ladder_tier": "foundations",
        "description": (
            "Gratitude rarely travels alone, and its most faithful companion "
            "is joy. The blend has its own unmistakable flavor: the glad "
            "lift of joy aimed at a giver, the celebration of a good thing "
            "that came to you. Picture the surprise party that actually "
            "worked: the lights come up, the people you love are all there, "
            "and two feelings arrive in the same breath - the bright, "
            "bouncing gladness that this is happening, and the warm, "
            "throat-tight thankfulness toward the people who made it "
            "happen. The joy supplies the energy: laughter, movement, the "
            "urge to mark the moment. The gratitude supplies the direction: "
            "the hugs go to specific people, the thanks name specific "
            "efforts, the warmth has addresses. Without the joy, gratitude "
            "can be quiet and solemn; without the gratitude, joy can be "
            "bright but diffuse, gladness with nowhere to land. Together "
            "they make the feeling people describe at weddings, reunions, "
            "recoveries, and homecomings: I am so happy, and I am so "
            "thankful - said as one sentence, because in the body they are "
            "one event. Researchers note that this blend is part of why "
            "gratitude is so socially powerful: joy makes the moment "
            "shareable, gratitude makes it bond-forming, and the pair "
            "together turn a good event into a good relationship."
        ),
        "how_it_works": (
            "The blend works because the two emotions share machinery and "
            "divide the labor. Joy's appraisal is 'something good happened'; "
            "gratitude's appraisal is 'something good happened and someone "
            "brought it.' Run both appraisals on the same event and the "
            "body gets a double signal: the bright activation of joy plus "
            "the warm directedness of gratitude. On the circumplex map, joy "
            "sits at high pleasantness and high activation while gratitude "
            "sits at high pleasantness and moderate activation; their blend "
            "lands between, which matches the felt character exactly: "
            "upbeat but tender, celebratory but personal. The joy component "
            "drives the shareable behaviors - laughing, telling, raising a "
            "glass - while the gratitude component drives the bonding "
            "behaviors - hugging the right people, naming what they did, "
            "promising to return it. This division of labor is why the "
            "blend is the engine of celebrations: joy makes people want to "
            "mark the moment, gratitude makes sure the marking lands on the "
            "people who earned it. The blend also explains a common "
            "observation: pure joy fades fast, but joy mixed with gratitude "
            "lingers, because the gratitude component tags the memory and "
            "schedules the aftershocks."
        ),
        "key_points": [
            "Gratitude's most common partner is joy: the blend is celebration with an address.",
            "Joy supplies the energy (laughter, movement, marking the moment); gratitude supplies the direction (which people, what they did).",
            "On the circumplex the blend lands between joy's high activation and gratitude's moderate activation: upbeat but tender.",
            "Without joy, gratitude can be solemn; without gratitude, joy can be diffuse gladness with nowhere to land.",
            "The blend lingers longer than pure joy because gratitude's memory tag schedules aftershocks.",
        ],
        "requirements": [
            "The blend named as gratitude's most common partner with a concrete scene.",
            "The division of labor stated: what each component contributes.",
            "The circumplex position of the blend stated.",
            "The without-each-component contrast stated.",
            "The lingering mechanism explained via the memory tag.",
        ],
        "standards": [
            "The blend structure follows Plutchik 1980: adjacent pleasant emotions combine into richer compounds.",
            "The circumplex positioning follows Russell 1980.",
            "The social-bonding function follows Algoe 2012: find, remind, and bind.",
        ],
        "citations": [CIT_PLUTCHIK, CIT_RUSSELL, CIT_ALGOE2012],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "day_vignette",
        "name": "A Day in the Life of Gratitude",
        "group": "How It Feels",
        "ladder_rank": 5,
        "ladder_tier": "foundations",
        "description": (
            "Morning: the alarm goes off and for once you do not grab the "
            "phone. You lie still for a minute and notice, actually notice, "
            "that the bed is warm and the day has not asked anything of you "
            "yet. A small flicker - nobody gave you this, exactly, but the "
            "day did, and the flicker counts. Mid-morning: a coworker "
            "covers your meeting without being asked, and texts 'got you.' "
            "The warmth is stronger now, with an address; you reply with "
            "real thanks instead of the usual thumbs-up, and the reply "
            "takes ten seconds longer and feels ten times better. Lunch: "
            "an old friend calls out of nowhere, and halfway through the "
            "call you realize you have been smiling for five minutes "
            "straight. Nobody did anything grand; the gift is simply that "
            "someone remembered you exist and acted on it. Afternoon: the "
            "bus driver waits eight extra seconds while you run, and you "
            "catch his eye in the mirror and mouth thank you, and he nods "
            "like it is a small treaty between strangers. Evening: your "
            "neighbor brings over soup because she heard you were sick "
            "last week - she remembered for a week, and acted. This one "
            "lands harder; your throat does the thing. You eat the soup "
            "slowly. Night: before sleep you run the day back, and the "
            "moments line up like small lamps: the bed, the text, the "
            "call, the bus, the soup. None of them was large. Together "
            "they are the whole day. That is a day in the life of "
            "gratitude: not one big feeling but a dozen small recognitions, "
            "each one brief, each one real, adding up to a day that felt, "
            "on balance, given rather than merely survived."
        ),
        "how_it_works": (
            "The vignette works by accumulation, which is how gratitude "
            "actually operates in daily life. No single moment in the day "
            "crosses the threshold of a peak experience; each runs the "
            "appraisal circuit at low to moderate volume - benefit detected "
            "(warm bed, covered meeting, remembered birthday of attention), "
            "source detected (the day, the coworker, the friend, the "
            "driver, the neighbor). Each firing deposits a small amount of "
            "warmth and, more importantly, a memory tag. The evening "
            "replay - running the day back - is the aftershock mechanism "
            "doing its scheduled work: each recalled moment re-fires a "
            "diluted copy of its feeling, so the day gets felt twice. The "
            "progression across the day also shows the widening of the "
            "source slot: it starts with circumstance (the warm bed), moves "
            "through small human kindnesses, and lands on the week's-old "
            "remembering of the neighbor - the most affecting, because the "
            "cost and intention inputs are highest there. The final "
            "accounting - 'given rather than merely survived' - is the "
            "attitude-level resolution: a day of small gratitudes leaves "
            "the ledger feeling positive, which is the mechanism behind "
            "the gratitude-journal findings. The day is ordinary on "
            "purpose: the lesson is that the instrument works on ordinary "
            "material."
        ),
        "key_points": [
            "A gratitude day is not one big feeling but a dozen small recognitions, each brief, each real.",
            "The mechanism is accumulation: small appraisals deposit warmth and memory tags all day.",
            "The evening replay re-fires each moment's feeling: the day gets felt twice.",
            "The source slot widens across the day: from circumstance to strangers to the neighbor who remembered for a week.",
            "The ordinary material is the point: the instrument works on normal days, not just milestones.",
        ],
        "requirements": [
            "A full-day vignette with at least five distinct gratitude moments.",
            "Moments spanning low to moderate intensity, none a peak experience.",
            "The accumulation mechanism stated as the explanatory frame.",
            "The evening replay tied to the aftershock mechanism.",
            "The closing accounting stated as attitude-level resolution.",
        ],
        "standards": [
            "The daily-accumulation account follows Emmons and McCullough 2003: counting blessings in daily life.",
            "The replay mechanism follows the aftershock account grounded in Scherer 2005.",
            "The widening source slot follows the appraisal structure of Ortony, Clore and Collins 1988.",
        ],
        "citations": [CIT_EMMONS2003, CIT_SCHERER, CIT_ORTONY1988],
        "sig_lens": SIG_LENS_DEF,
    },
    # ------------------------------------------------ 10-13 BODY SIGNALS
    {
        "key": "body",
        "name": "Gratitude in the Body: Heart, Breath, Muscles, and Warmth",
        "group": "Body Signals",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The body of gratitude is a body standing down. The heart does "
            "not pound the way it does in fear or excitement; it settles "
            "into a slow, full beat, sometimes with a felt warmth spreading "
            "across the chest that people describe, across cultures, as "
            "heat behind the breastbone. The breath deepens and slows: "
            "grateful people exhale longer than they inhale, the classic "
            "sigh of relief and contentment, and the shoulders drop a "
            "fraction as they do. The muscles unclench - jaw, hands, "
            "stomach - the small holdings of the day releasing one by one, "
            "as if the body has decided, for the moment, that it does not "
            "have to brace. The stomach settles; appetite neither spikes "
            "nor vanishes. The skin may warm, especially the face, and in "
            "strong moments the eyes fill - gratitude is one of the few "
            "pleasant emotions that routinely brings tears, the tearful "
            "thank-you being nearly universal. Energy does not surge the "
            "way it does in triumph; it steadies. People describe feeling "
            "simultaneously relaxed and somehow more alive, calm in the "
            "limbs and bright in the chest. At high intensity the signature "
            "addition is the throat: the tightening that makes speech "
            "crack, the body's way of marking that the feeling has passed "
            "the size that words were built for. None of this is dramatic "
            "from the outside - gratitude is a quiet emotion in the flesh - "
            "but on the inside it is unmistakable: the whole system "
            "registering, at once, that it is safe, helped, and held."
        ),
        "how_it_works": (
            "The body pattern of gratitude follows from what the appraisal "
            "tells the nervous system: a benefit has arrived, the source is "
            "friendly, no action is urgently required. With no threat to "
            "fight and no prize to chase, the sympathetic branch stands "
            "down and the parasympathetic branch - the rest-and-connect "
            "system - takes the lead. That shift explains the slow full "
            "heartbeat, the lengthened exhale, and the muscular unclenching: "
            "these are the textbook signatures of parasympathetic "
            "dominance. The chest warmth maps to the same warm social "
            "chemistry the body uses for bonding - the reason gratitude "
            "feels physically close to love and tenderness. The tears at "
            "high intensity are the overflow valve: when the feeling "
            "exceeds the capacity of speech and gesture, the lacrimal "
            "system vents the surplus, which is why the tearful thank-you "
            "reads as authentic across cultures. The throat tightening is "
            "the same mechanism at lower volume: the vocal apparatus "
            "registering load. The steadied rather than surging energy "
            "reflects gratitude's moderate activation on the circumplex: "
            "arousal rises enough to motivate the thank-you and the return "
            "favor, but not enough to drive frantic action. The body is "
            "doing exactly what the emotion is for: settling into "
            "connection, primed to acknowledge and repay, in no hurry."
        ),
        "key_points": [
            "Gratitude is a standing-down body: slow full heartbeat, lengthened exhale, unclenching jaw, hands, and stomach.",
            "The signature sensation is warmth behind the breastbone - the social-bonding chemistry answering the appraisal.",
            "Gratitude is one of the few pleasant emotions that routinely brings tears: the overflow valve for feelings too big for words.",
            "At high intensity the throat tightens and speech cracks - the vocal apparatus registering load.",
            "Energy steadies rather than surges: calm limbs, bright chest, primed to acknowledge and repay, in no hurry.",
        ],
        "requirements": [
            "Coverage of heart, breath, muscles, stomach, skin, eyes, throat, and energy.",
            "The parasympathetic mechanism stated as the unifying explanation.",
            "The tear mechanism explained as overflow, with the authenticity read noted.",
            "The moderate-activation link to the circumplex stated.",
            "The quiet-from-outside, unmistakable-from-inside contrast stated.",
        ],
        "standards": [
            "The autonomic pattern follows the component-process account in Scherer 2005.",
            "The circumplex activation level follows Russell 1980.",
            "The social-bonding chemistry framing follows Fredrickson 2004 and the broaden-and-build account.",
        ],
        "citations": [CIT_SCHERER, CIT_RUSSELL, CIT_FREDRICKSON2004],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "posture",
        "name": "Posture and Movement: How the Body Carries Gratitude",
        "group": "Body Signals",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Gratitude opens the body. The chest comes forward and up, not "
            "thrust out in pride but offered: the sternum tilts slightly "
            "toward the benefactor as if to show there is nothing hidden. "
            "The shoulders, which spend most of the day creeping toward the "
            "ears, drop and roll back. The head often tilts a few degrees "
            "to one side - the universal listening angle, the posture of "
            "someone receiving. Hands do the most talking: they come "
            "together in front of the chest, palm to palm or one over the "
            "heart, the gesture people make on every continent when words "
            "fall short. The nod is gratitude's metronome - small, "
            "repeated, involuntary dips of the chin that say 'yes, I "
            "receive this' while the mouth is still finding words. "
            "Movement slows and gentles: grateful people do not fidget or "
            "pace; they settle, turn fully toward the giver, and give the "
            "moment their whole front. At high intensity the body may bow "
            "slightly - a forward inclination of the torso that appears in "
            "culture after culture as the physical grammar of thankfulness - "
            "or go still altogether, the freeze of being overwhelmed. What "
            "gratitude never does with the body is close it: no crossed "
            "arms, no turned shoulder, no step back. The posture is always, "
            "in every degree, an opening - the body making room for the "
            "giver and the gift."
        ),
        "how_it_works": (
            "Posture in gratitude is the approach system made visible. The "
            "appraisal has classified the source as friendly and the benefit "
            "as good, so the motor system does what it does for all "
            "welcomed things: it orients, opens, and reduces distance. The "
            "forward chest and uncrossed arms are the opposite of the "
            "defensive crouch - the body is displaying vulnerability on "
            "purpose, signaling trust to the benefactor. The head tilt is "
            "the receiving posture shared with listening and tenderness: "
            "the neck exposed, the attention fully allocated. The hand-to-"
            "heart gesture is doubly functional: it marks the felt location "
            "of the emotion (the chest warmth) and it is a visible, "
            "hard-to-fake signal of sincerity to the giver. The nod runs on "
            "the affirmation circuit: the same vertical head movement that "
            "means agreement across cultures, here meaning 'I accept this "
            "kindness.' The bow at high intensity is the appeasement "
            "display borrowed from hierarchy: lowering the body to honor "
            "the giver, which is why it reads as respect rather than "
            "submission when gratitude drives it. The stillness of "
            "overwhelm is the orienting response at maximum: all movement "
            "pauses while the system processes a large input. Every element "
            "serves the emotion's social job: showing the giver, in a "
            "language older than words, that the gift landed."
        ),
        "key_points": [
            "Gratitude opens the body: chest offered forward, shoulders dropped, arms uncrossed, full front turned to the giver.",
            "The hand-to-heart or palms-together gesture is gratitude's universal overflow signal when words fall short.",
            "The nod is gratitude's metronome: small repeated dips meaning 'yes, I receive this.'",
            "At high intensity the torso bows slightly - the physical grammar of thankfulness across cultures.",
            "What gratitude never does is close the body: no crossed arms, no turned shoulder, no step back.",
        ],
        "requirements": [
            "Named postural elements: chest, shoulders, head tilt, hands, nod, torso, stillness.",
            "The approach-system mechanism stated as the unifying explanation.",
            "The hand-to-heart gesture explained as both felt-location marking and sincerity signal.",
            "The bow explained via the appeasement display, distinguished from submission.",
            "The never-closes rule stated as the diagnostic contrast.",
        ],
        "standards": [
            "The display grammar follows Darwin 1872 on the serviceable associated habits of expression.",
            "The approach-orientation account follows Frijda 1986 on action readiness.",
            "The signal-function framing follows the moral-affect account of McCullough, Kilpatrick, Emmons and Larson 2001.",
        ],
        "citations": [CIT_DARWIN, CIT_FRIJDA, CIT_MCCULLOUGH2001],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "sleep_appetite",
        "name": "Sleep, Appetite, and Energy Under Gratitude",
        "group": "Body Signals",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Gratitude is gentle with the body's routines. Sleep is the "
            "clearest beneficiary: people who spend a few minutes noting "
            "what they are thankful for before bed consistently report "
            "falling asleep faster and sleeping more soundly, and the "
            "reason is straightforward - the mind that has just finished "
            "replaying kindnesses has less room for replaying worries. The "
            "pre-sleep worry loop is gratitude's direct competitor for the "
            "same mental stage, and the gratitude replay tends to win "
            "because it is warmer. Appetite under gratitude is mostly "
            "untouched: unlike anxiety, which kills hunger, or celebration, "
            "which can spike it, gratitude leaves eating alone - though "
            "grateful people often report food tasting slightly better, "
            "the savoring spillover of an appreciative mind. Energy under "
            "gratitude is the steadied kind described in the body record: "
            "not the wired buzz of excitement, not the lead of sadness, "
            "but a calm availability - the sense that you could get up and "
            "do something kind right now if you wanted to. That readiness "
            "is not an accident; it is the moral-motive function idling, "
            "the engine warm for the return favor. The overall picture is "
            "of an emotion that asks little of the body and gives back "
            "steadiness: no crash follows it, no hangover, no wired "
            "aftermath. Of all the strong feelings, gratitude is among the "
            "cheapest to feel and the most repaying to the systems that "
            "feel it."
        ),
        "how_it_works": (
            "The sleep effect runs through cognitive competition. Pre-sleep "
            "thought content predicts sleep onset: worry and rumination "
            "delay it, warm benign content shortens it. A brief gratitude "
            "practice fills the pre-sleep window with specific, warm, "
            "resolved memories - the opposite of the open-loop worries "
            "that keep the mind scanning. With the threat-scanning quieted, "
            "the parasympathetic shift already described can complete, and "
            "sleep onset shortens. The appetite neutrality follows from "
            "gratitude's moderate activation: the gut-brain axis responds "
            "strongly to high-arousal states in both directions, but "
            "gratitude's arousal sits in the middle band where digestion "
            "proceeds normally. The savoring spillover is an attentional "
            "effect: a mind trained by gratitude to notice and linger on "
            "good things applies the same lingering to flavor. The calm "
            "availability of energy is the action-readiness component of "
            "the emotion - Frijda's action tendency - tuned to prosocial "
            "action rather than urgent action: the system is primed to "
            "thank, repay, and help, which feels like readiness without "
            "restlessness. The absence of a crash follows from the same "
            "moderate activation: there is no sympathetic spike to recover "
            "from, so the feeling can end without a bill."
        ),
        "key_points": [
            "Sleep benefits most: pre-sleep gratitude replay competes with the worry loop for the same mental stage - and wins.",
            "Appetite is largely untouched; the savoring spillover can make food taste slightly better.",
            "Energy steadies into calm availability: readiness to thank, repay, and help, without restlessness.",
            "The readiness is the moral-motive function idling - the engine warm for the return favor.",
            "No crash follows gratitude: moderate activation means no sympathetic spike and no recovery bill.",
        ],
        "requirements": [
            "Sleep, appetite, and energy each covered with the mechanism.",
            "The cognitive-competition account of the sleep effect stated.",
            "The savoring spillover explained as attentional lingering.",
            "The moral-motive idling frame for the energy state.",
            "The no-crash claim tied to moderate activation.",
        ],
        "standards": [
            "The sleep findings follow Wood, Froh and Geraghty 2010 and the gratitude-and-well-being review literature.",
            "The action-readiness framing follows Frijda 1986.",
            "The moderate-activation account follows Russell 1980.",
        ],
        "citations": [CIT_WOOD2010, CIT_FRIJDA, CIT_RUSSELL],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "individual_diff",
        "name": "How Gratitude Differs Between People",
        "group": "Body Signals",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "No two bodies do gratitude identically. Some people are criers: "
            "their gratitude goes straight to the eyes at moderate "
            "intensity, and they have learned to carry tissues to weddings. "
            "Others are warmers: no tears ever, but the chest heat and the "
            "long exhale give them away. Some go still and quiet, the "
            "feeling turning them inward, while others become effusive - "
            "hugging, exclaiming, telling everyone in the room. None of "
            "these is the 'correct' gratitude; they are different "
            "instrument tunings playing the same note. Underneath the "
            "surface variation runs the deeper difference researchers "
            "measure: the grateful disposition. Some people are tuned to "
            "notice benefits everywhere - the trait-level gratitude that "
            "makes the world look generous - while others need the benefit "
            "to be large and obvious before the circuit fires. This tuning "
            "is partly temperament, partly training: the noticing habit can "
            "be built, which is what the gratitude practices do. Culture "
            "writes the display rules: some cultures thank profusely and "
            "physically, others consider effusive thanks embarrassing and "
            "prefer a quiet, sustained reciprocity - the debt repaid over "
            "years rather than the speech made in the moment. Age changes "
            "the pattern too: children feel gratitude brightly but briefly, "
            "and often need prompting to connect the feeling to the giver; "
            "older adults tend to feel it more readily and express it more "
            "deliberately. The lesson for reading others is the only one "
            "that matters: never mistake a quiet instrument for an empty "
            "one. The still person with the warm eyes may be feeling more "
            "than the effusive one - they are simply playing it on a "
            "different instrument."
        ),
        "how_it_works": (
            "The variation runs on three separate dials. The first is "
            "physiological tuning: how readily a given nervous system "
            "converts the appraisal into tears, warmth, or stillness - "
            "largely temperament, stable across a lifetime. The second is "
            "the dispositional threshold: how large a benefit must be "
            "before the benefit-detection appraisal fires. People with a "
            "strong grateful disposition have a low threshold - small "
            "kindnesses register - which is why the world looks more "
            "generous to them; the world is the same, the detector is more "
            "sensitive. This threshold is trainable: repeated noticing "
            "practice lowers it, which is the mechanism behind the "
            "gratitude-journal effects. The third dial is the display rule "
            "set: the culturally learned mapping from felt intensity to "
            "shown intensity. Some cultures apply a gain greater than one - "
            "feel a little, show a lot - others apply a gain below one, "
            "and the same felt warmth produces a bow, a nod, or a years-"
            "long quiet reciprocity. Age effects run through cognitive "
            "development: connecting a benefit to its giver requires the "
            "perspective-taking that matures through childhood, while the "
            "readiness of older adults reflects a lifetime of lowered "
            "thresholds and practiced noticing. Reading another person "
            "means solving for all three dials at once - which is why the "
            "recognition records teach cues in clusters, never single "
            "tells."
        ),
        "key_points": [
            "Surface styles vary: criers, warmers, the effusive, the still - different instruments, same note.",
            "The deep difference is the dispositional threshold: how large a benefit must be before the circuit fires.",
            "The threshold is trainable: noticing practice lowers it, which is how the gratitude practices work.",
            "Culture sets the display gain: effusive thanks in one place, quiet years-long reciprocity in another.",
            "Children feel it brightly but briefly; older adults feel it readily and express it deliberately.",
            "Never mistake a quiet instrument for an empty one: stillness can carry the most feeling.",
        ],
        "requirements": [
            "Surface-style variation described with named types.",
            "The dispositional-threshold account stated with the trainability claim.",
            "Cultural display-rule variation with the gain metaphor.",
            "Age-related variation covered for children and older adults.",
            "The reading lesson stated: quiet is not empty.",
        ],
        "standards": [
            "The grateful-disposition construct follows Watkins, Woodward, Stone and Kolts 2003.",
            "The trainability claim follows Emmons and McCullough 2003 and Emmons 2007.",
            "The display-rule framing follows Ekman 1999 on cultural display rules.",
        ],
        "citations": [CIT_WATKINS2003, CIT_EMMONS2007, CIT_EKMAN1999],
        "sig_lens": SIG_LENS_DEF,
    },
    # ------------------------------------------------ 14-17 FACIAL EXPRESSION
    {
        "key": "face",
        "name": "The Face of Gratitude: Eyes, Brows, Mouth, and Micro-Signs",
        "group": "Facial Expression",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Gratitude has no single stamped facial signal - you will not "
            "find it on the classic list of universal expressions - but it "
            "has a face, and once you know it you cannot unsee it. The eyes "
            "lead: they soften and brighten at once, the upper lids "
            "dropping a fraction, the gaze holding steady on the giver "
            "rather than darting. In genuine moments the outer corners "
            "crinkle - the Duchenne marker, the tiny crow's-feet that the "
            "face cannot produce on command - and the eyes may shine with "
            "the first film of tears. The brows do something subtle: they "
            "rise slightly in the middle and relax at the edges, the brow "
            "of someone moved rather than surprised, lowering the forehead "
            "lines of worry and replacing them with a smooth, open brow. "
            "The mouth forms the warm smile: lip corners pulled up and "
            "slightly outward, the smile that reaches the eyes rather than "
            "stopping at the mouth, sometimes parting just enough to show "
            "the upper teeth in the unguarded moments. The micro-signs "
            "complete the picture: a slight head tilt, a single slow nod, "
            "the chin dipping as the thank-you forms, sometimes the quick "
            "press of lips together - the effort not to cry - right before "
            "the smile wins. The whole face says one sentence in the "
            "oldest language: I see what you did, and it reached me. It is "
            "a quiet face, easy to miss in a crowd, unmistakable at a "
            "table for two."
        ),
        "how_it_works": (
            "The face of gratitude is assembled from parts borrowed from "
            "neighboring expressions, which is why it reads clearly despite "
            "having no dedicated signal. The eye crinkle (orbicularis "
            "oculi, outer portion) is the Duchenne marker shared with "
            "genuine joy: it fires only when the positive feeling is real, "
            "because that muscle resists voluntary control - which is why "
            "the crinkle is the authenticity stamp. The softened gaze and "
            "lowered lids come from the parasympathetic shift: the same "
            "system that slows the heart relaxes the muscles around the "
            "eye. The mid-brow raise with relaxed edges is the 'moved' "
            "configuration, blending the attention brow of interest with "
            "the release of worry - the face of someone taking something "
            "in. The warm smile (zygomatic major pulling the lip corners up "
            "and out) is joy's mouth with gratitude's moderation: full "
            "enough to be unmistakable, rarely the wide grin of triumph. "
            "The lip press is the emotion-regulation micro-sign: the "
            "orbicularis oris containing the feeling for a half-second "
            "before expression wins - and its presence paradoxically "
            "increases perceived sincerity, because it shows the feeling "
            "was strong enough to need containing. Together the parts form "
            "a configural signal: no single muscle defines gratitude, but "
            "the combination - crinkled warm eyes, moved brow, genuine "
            "smile, held gaze - is recognized reliably, because the brain "
            "reads faces as whole patterns, not parts lists."
        ),
        "key_points": [
            "Gratitude has no single universal signal, but it has a recognizable face: soft bright eyes, moved brow, warm genuine smile.",
            "The eyes lead: steady gaze on the giver, lowered lids, and the un-fakeable outer-corner crinkle of genuine feeling.",
            "The brow rises slightly in the middle and relaxes at the edges: the brow of someone moved, not surprised.",
            "Micro-signs: the slow nod, the chin dip, the quick lip press of someone trying not to cry before the smile wins.",
            "The brain reads the configuration whole: crinkled eyes plus genuine smile plus held gaze equals gratitude, reliably.",
        ],
        "requirements": [
            "Eyes, brows, and mouth each described with the specific muscular signs.",
            "The Duchenne crinkle named as the authenticity stamp with the voluntariness reason.",
            "Micro-signs listed: nod, chin dip, lip press, head tilt.",
            "The configural-reading claim stated: the pattern, not the parts.",
            "The no-single-signal honesty stated up front.",
        ],
        "standards": [
            "The muscular descriptions follow Ekman and Friesen FACS 1978: orbicularis oculi, zygomatic major, orbicularis oris.",
            "The Duchenne-marker account follows the genuine-smile literature grounded in Ekman 1999.",
            "The configural face-reading claim follows Barrett 2017.",
        ],
        "citations": [CIT_FACS, CIT_EKMAN1999, CIT_BARRETT],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "face_intensity",
        "name": "How the Face of Gratitude Changes with Intensity",
        "group": "Facial Expression",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Turn the dial and the face changes in lawful ways. At mild "
            "intensity - the flicker of the held door - the face barely "
            "moves: the eyes brighten a fraction, the lip corners lift a "
            "few millimeters, the nod is single and small. A stranger "
            "watching would see politeness; someone who knows the "
            "instrument sees the beginning of warmth. At moderate "
            "intensity the full configuration assembles: the crinkle "
            "appears at the eyes' outer corners, the brow does its moved "
            "rise, the smile becomes unmistakably genuine, the gaze holds "
            "on the giver a beat longer than conversation requires. The "
            "head tilt joins, the hand may rise toward the chest. This is "
            "the face of the real thank-you, the one people remember. At "
            "high intensity the face starts to break its own composition: "
            "the smile widens past neatness, the eyes fill and the gaze "
            "may drop for a second as the person fights the tears, the "
            "lip press appears - that quick compression of someone holding "
            "back a sob or a flood of words - and then either the tears "
            "come or the laugh comes, sometimes both at once, the face "
            "cycling between smiling and crumpling faster than any "
            "photograph could catch. The progression is not just 'more of "
            "the same': each level adds new elements - the crinkle at "
            "moderate, the lip press and tear film at high - so the face "
            "can be read like a gauge. And the gauge runs both ways: when "
            "the elements are missing at claimed high intensity - the big "
            "words with the flat eyes - the face is telling you the dial "
            "is not where the words say it is."
        ),
        "how_it_works": (
            "The intensity scaling of the face follows the recruitment "
            "order of the facial musculature under rising affect. At low "
            "activation, only the most voluntary and cheapest muscles fire: "
            "a small zygomatic pull, a brightening of gaze - the social "
            "minimum, enough to signal acknowledgment. As activation "
            "rises into the moderate band, the involuntary markers join: "
            "the orbicularis oculi crinkle, which cannot be summoned at "
            "will, appears only when the feeling is genuinely strong "
            "enough - making the crinkle a threshold indicator, not a "
            "volume knob. The brow's moved configuration and the held gaze "
            "are attentional: rising feeling commands more of the face's "
            "bandwidth. At high activation the regulation signs appear: "
            "the lip press, the gaze drop, the cycling between smile and "
            "crumple - these are not expressions of the feeling but "
            "expressions of the system managing the feeling, the visible "
            "work of containing an overflow. That is why the high-"
            "intensity face looks 'broken' compared to the composed "
            "moderate face: you are seeing feeling plus effort at once. "
            "The diagnostic value runs in reverse: because the involuntary "
            "markers (crinkle, tear film, lip press) cannot be produced "
            "without the underlying activation, their absence at claimed "
            "high intensity is informative - the face leaks the true dial "
            "setting, which is the mechanism the hiding-and-faking record "
            "builds on."
        ),
        "key_points": [
            "Mild: barely moves - brightened eyes, millimeters of smile, one small nod; politeness to strangers, warmth to those who know.",
            "Moderate: the full configuration - crinkle, moved brow, genuine smile, held gaze, head tilt, hand to chest.",
            "High: the composition breaks - widened smile, tear film, lip press, cycling between smiling and crumpling.",
            "Each level adds new elements rather than just amplifying: the face reads like a gauge with threshold markers.",
            "The gauge runs in reverse: missing involuntary markers at claimed high intensity reveal the true dial setting.",
        ],
        "requirements": [
            "Three intensity bands with the specific facial elements at each.",
            "The threshold-marker account of the Duchenne crinkle stated.",
            "The regulation-sign account of the high-intensity face stated.",
            "The additive-not-just-amplified structure stated.",
            "The reverse-diagnostic use stated, bridging to the hiding record.",
        ],
        "standards": [
            "The muscular recruitment account follows Ekman and Friesen FACS 1978.",
            "The involuntary-marker claims follow Ekman 1999 on the voluntariness of facial actions.",
            "The threshold structure follows the component-process intensity account in Scherer 2005.",
        ],
        "citations": [CIT_FACS, CIT_EKMAN1999, CIT_SCHERER],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "hiding_faking",
        "name": "Hiding and Faking Gratitude: What Leaks Through",
        "group": "Facial Expression",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Gratitude is both hidden and faked constantly, and the face is "
            "bad at both deceptions. Hiding it looks like this: the person "
            "feels the warmth but will not show it - the proud patient who "
            "will not thank the nurse, the teenager mortified to be moved "
            "in front of friends. The mouth stays flat, the words stay "
            "short, but the eyes do not get the memo: the softening and "
            "the brightness leak through, the gaze holds a half-beat too "
            "long, the nod escapes once before being caught. Swallowed "
            "gratitude also leaks downward: the throat works, the chest "
            "rises in the long exhale, the hand starts toward the heart "
            "and is rerouted to a pocket. Faking it is the mirror image: "
            "the words are effusive - 'oh my god, thank you SO much, you "
            "are AMAZING' - while the face stays in the shallow end. The "
            "tells of the fake are the missing involuntaries: the smile "
            "is wide but the eyes do not crinkle, the gaze skitters instead "
            "of holding, the brow never does its moved rise, the whole "
            "performance is a fraction too fast and a decibel too loud. "
            "Real gratitude has a tempo - the pause before the thank-you, "
            "the held gaze, the slow nod - and the fake rushes it, because "
            "the faker is performing the script rather than feeling the "
            "appraisal. The deepest fake is the strategic one: gratitude "
            "performed to obligate, flatter, or manipulate. It can fool "
            "the room for an evening, but it rarely fools the target for "
            "long - humans are exquisitely tuned to the difference between "
            "warmth with an address and warmth as a tactic, because "
            "getting it wrong was expensive for our ancestors."
        ),
        "how_it_works": (
            "Hiding fails because of the voluntariness gradient of the "
            "face. The mouth is the most voluntary territory - easy to "
            "hold flat - while the eyes' outer corners, the tear film, and "
            "the throat are the least voluntary; the hider can lock the "
            "mouth but cannot order the eyes not to soften, which is why "
            "leakage concentrates in the upper face and the body below the "
            "neck. Faking fails for the symmetrical reason: the faker can "
            "drive the voluntary muscles - the wide zygomatic smile, the "
            "animated brow - but cannot summon the involuntary markers, "
            "the crinkle and the tear shine, without the underlying "
            "activation. The tempo difference is cognitive: real gratitude "
            "runs the appraisal first and the expression follows, "
            "producing the characteristic pause-and-hold; the fake runs "
            "the script first, producing the rushed, slightly-too-much "
            "performance. The strategic fake adds a motivational tell: "
            "because its goal is effect rather than acknowledgment, it "
            "overshoots - too effusive, too public, too repeated - while "
            "genuine gratitude is usually specific and proportionate. The "
            "detection system in observers is the configural face reader "
            "plus the tempo reader plus the proportionality check, running "
            "below awareness; that is why people so often 'just feel' that "
            "thanks were hollow without being able to say which muscle "
            "gave it away. The practical rule: trust the involuntary "
            "markers, distrust the volume."
        ),
        "key_points": [
            "Hiding fails at the eyes: the mouth can be held flat but the softening, brightness, and held gaze leak through.",
            "Swallowed gratitude leaks downward too: the working throat, the long exhale, the hand rerouted from the heart.",
            "Faking fails at the involuntaries: wide smile with no eye crinkle, skittering gaze, performance a fraction too fast.",
            "Real gratitude has a tempo - pause, held gaze, slow nod - and the fake rushes it.",
            "Strategic gratitude (performed to obligate or flatter) overshoots: too effusive, too public, too repeated.",
            "The detection rule: trust the involuntary markers, distrust the volume.",
        ],
        "requirements": [
            "Hiding described with the specific leakage points (eyes, throat, hand).",
            "Faking described with the missing-involuntary tells and the tempo tell.",
            "The voluntariness gradient stated as the mechanism for both failures.",
            "The strategic-manipulative fake distinguished from the merely polite fake.",
            "The observer's detection system described as configural plus tempo plus proportionality.",
        ],
        "standards": [
            "The voluntariness gradient follows Ekman 1999 and Ekman and Friesen FACS 1978.",
            "The leakage account follows the classic expression-leakage literature grounded in Darwin 1872.",
            "The configural detection claim follows Barrett 2017.",
        ],
        "citations": [CIT_EKMAN1999, CIT_FACS, CIT_DARWIN],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "expression_gallery",
        "name": "Drawing Gratitude: Gallery Notes for the Artist",
        "group": "Facial Expression",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "For the artist, the actor, or the animator: here is gratitude "
            "as drawable parameters. Start with the eyes, because the "
            "audience reads them first. Draw the upper lids lowered about "
            "a tenth of their travel - not sleepy, softened - and put the "
            "catchlight slightly larger and warmer than neutral; gratitude "
            "eyes shine. Add the crow's-feet: two or three short radiating "
            "lines at each outer corner, shallow at mild intensity, deeper "
            "at moderate - these lines are the honesty certificate, and an "
            "audience will trust a face that has them and doubt one that "
            "does not. The brows: raise the inner third by a few degrees "
            "and let the outer two-thirds relax flat; erase any vertical "
            "worry furrow between them - gratitude smooths that region. "
            "The mouth: pull the corners up and slightly outward, a curve "
            "shallower than joy's grin but warmer than politeness; at "
            "moderate intensity part the lips a few millimeters, at high "
            "intensity let the lower lip tremble or press the lips once "
            "before the smile returns. The head: tilt five to eight degrees "
            "toward the giver, chin dipped a fraction. The hands, if the "
            "frame includes them: one palm over the sternum, or both palms "
            "pressed lightly together below the chin. Light the face warm "
            "and from slightly below eye level - gratitude looks up more "
            "often than it looks down. For the actor: find the pause. Real "
            "gratitude never rushes the thank-you; play the half-second "
            "where the feeling arrives before the words, hold the gaze "
            "one beat past comfortable, and let the nod come once, slowly. "
            "The audience will do the rest - they have all felt this, and "
            "recognition does your work for you."
        ),
        "how_it_works": (
            "The gallery notes work because they translate the muscular "
            "facts into the parameters that image-makers actually control: "
            "lid height, line placement, curve depth, head angle, hand "
            "position, lighting direction, and - for the actor - timing. "
            "Each parameter maps to a FACS action: the lowered lids and "
            "crow's-feet to the orbicularis oculi, the inner brow raise to "
            "the frontalis medial portion, the mouth curve to zygomatic "
            "major, the lip press to orbicularis oris. The reason the notes "
            "insist on the crow's-feet is perceptual: viewers weight the "
            "eye region heaviest in sincerity judgments, and the crinkle "
            "is the region's honesty signal - a drawing without it reads "
            "as polite, with it reads as moved. The head tilt and dipped "
            "chin are compositional: they angle the face toward the "
            "imagined giver, telling the viewer where the feeling points - "
            "gratitude always has an address, and the composition should "
            "show it. The lighting note is about association: warm low "
            "light reads as intimacy and safety, the context gratitude "
            "belongs to. The actor's note about the pause encodes the "
            "appraisal-then-expression sequence: playing the pause plays "
            "the appraisal, and the audience's own gratitude machinery "
            "recognizes the sequence and fires in sympathy - which is why "
            "a well-played thank-you can move a room that a rushed one "
            "leaves cold."
        ),
        "key_points": [
            "Eyes first: lids lowered a tenth, larger warm catchlight, crow's-feet at the outer corners - the honesty certificate.",
            "Brows: inner third raised a few degrees, worry furrow erased - the smoothed brow of being moved.",
            "Mouth: corners up and slightly out, shallower than joy's grin; lip press or tremble at high intensity.",
            "Composition: head tilted toward the giver, chin dipped, hand to sternum - show the feeling's address.",
            "For the actor: play the pause - the half-second where the feeling arrives before the words - and let the nod come once, slowly.",
        ],
        "requirements": [
            "Drawable parameters for eyes, brows, mouth, head, and hands.",
            "The FACS mapping stated for each parameter.",
            "The crow's-feet insistence justified via sincerity perception.",
            "Lighting and composition notes included.",
            "Separate actor direction covering tempo: the pause, the held gaze, the slow nod.",
        ],
        "standards": [
            "The muscular mappings follow Ekman and Friesen FACS 1978.",
            "The sincerity-perception claims follow the genuine-expression literature grounded in Ekman 1999.",
            "The expression-description method follows Darwin 1872 on the visible signs of emotion.",
        ],
        "citations": [CIT_FACS, CIT_EKMAN1999, CIT_DARWIN],
        "sig_lens": SIG_LENS_DEF,
    },
    # ------------------------------------------------ 18-21 TRIGGERS
    {
        "key": "classic_triggers",
        "name": "The Classic Triggers of Gratitude",
        "group": "Triggers",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "Certain situations set off gratitude the way a struck match "
            "sets off dry grass - reliably, across cultures, across "
            "centuries. Receiving help in a moment of need is the "
            "archetype: the stranded driver, the overwhelmed new parent, "
            "the patient in the frightening ward - need plus rescue is "
            "gratitude's native habitat. Gifts given freely come next, "
            "especially the ones that show the giver was paying attention: "
            "the book on the exact subject you mentioned once, the meal "
            "that arrived the day the news was bad. Unexpected kindness "
            "from strangers ranks high because the surprise input is maxed: "
            "the fare paid by the person ahead of you in line, the tire "
            "changed by someone who just stopped. Being remembered is a "
            "quiet classic: the birthday call from the old friend, the "
            "condolence note weeks after everyone else moved on - the "
            "trigger here is not the object but the evidence that you "
            "occupy space in someone's mind. Forgiveness and mercy form "
            "their own family of triggers: the debt forgiven, the mistake "
            "overlooked, the second chance granted - benefits measured not "
            "in what was given but in what was withheld. Rescue from "
            "danger, even by luck: the near-miss on the highway produces a "
            "flood of gratitude with no human giver at all, aimed at "
            "circumstance itself. And the beauty trigger: the sunset that "
            "stops you mid-step, the music that fills the room - no "
            "benefactor, no favor, just the world offering something for "
            "nothing, and the heart answering with thanks. Learn this list "
            "and you can see gratitude coming: wherever need meets "
            "generosity, wherever attention meets remembering, wherever "
            "danger meets deliverance, the feeling is already on its way."
        ),
        "how_it_works": (
            "Each classic trigger maxes one or more of the five intensity "
            "inputs. Help in need maxes the need input: the appraisal "
            "weights benefits by how much they mattered, and rescue from "
            "real trouble matters enormously. The attentive gift maxes the "
            "intention input: the mind reads the giver's care in the "
            "specificity of the gift, and perceived intention multiplies "
            "the felt volume. Stranger kindness maxes surprise: with no "
            "prior relationship, no reciprocity was expected, so the "
            "benefit arrives un-discounted by obligation. Being remembered "
            "works through the belonging channel: the benefit is evidence "
            "of mattering, which the social brain values as highly as "
            "material help. Forgiveness works through contrast: the "
            "punishment or consequence that was deserved but withheld is "
            "appraised as a benefit equal in size to the disaster avoided. "
            "The near-miss works through counterfactual vividness: the mind "
            "simulates the disaster that almost happened, and the gap "
            "between the simulation and reality is appraised as a gift "
            "from circumstance. Beauty works through the unearned-benefit "
            "pathway: the world provides pleasure at no cost, the source "
            "slot fills with nature or existence itself, and the warmth "
            "follows. The reliability of these triggers across cultures "
            "suggests they are not learned associations but the designed "
            "inputs of the gratitude circuit: the situations the system "
            "was built to notice."
        ),
        "key_points": [
            "Help in need is the archetype: need plus rescue is gratitude's native habitat.",
            "Attentive gifts trigger through the intention input: specificity of the gift proves the giver's care.",
            "Stranger kindness maxes surprise: no expected reciprocity means the benefit arrives un-discounted.",
            "Being remembered triggers through belonging: the benefit is evidence that you matter to someone.",
            "Forgiveness works through contrast: the withheld punishment is appraised as a gift.",
            "Near-misses and beauty need no human giver: circumstance and the world fill the source slot.",
        ],
        "requirements": [
            "At least six classic trigger families named with concrete examples.",
            "Each trigger mapped to the intensity input it maxes.",
            "The no-human-giver triggers (near-miss, beauty) explained via the source-slot account.",
            "The cross-cultural reliability claim tied to designed inputs.",
            "The predictive summary: where to see gratitude coming.",
        ],
        "standards": [
            "The appraisal-input mapping follows Ortony, Clore and Collins 1988.",
            "The intention-reading account follows the moral-affect literature: McCullough, Kilpatrick, Emmons and Larson 2001.",
            "The benefit-detection framing follows Lazarus 1991.",
        ],
        "citations": [CIT_ORTONY1988, CIT_MCCULLOUGH2001, CIT_LAZARUS1991],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "personal_triggers",
        "name": "Personal Triggers: Memories, Anniversaries, and Private Associations",
        "group": "Triggers",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "Beyond the universal triggers, every person carries a private "
            "set - the gratitude tripwires wired by their own history. The "
            "song that played in the hospital waiting room during the long "
            "night that ended well: hearing it years later in a grocery "
            "store stops you cold, throat tight, grateful toward nurses "
            "whose names you never learned. The smell of a particular soup: "
            "it was what the neighbor brought every week after the "
            "funeral, and the smell still means 'someone showed up.' "
            "Anniversaries are the calendar's version: the date of the "
            "accident survived, the date of the diagnosis beaten, the date "
            "someone came home - the day itself becomes a trigger, and the "
            "gratitude arrives on schedule whether or not you planned for "
            "it. Places hold it too: the bench where the good news came by "
            "phone, the doorway of the classroom where the teacher said "
            "the thing that changed your direction. Even objects: the worn "
            "tool inherited from the grandparent who taught you the trade, "
            "heavy with the gratitude of everything it made possible. "
            "These triggers are powerful precisely because they are "
            "private: the benefit they point to is real but invisible to "
            "everyone else, so the feeling arrives without social "
            "scaffolding - no one else in the grocery store knows why you "
            "are standing still in the cereal aisle. They are also "
            "durable: wired by strong emotion at encoding, personal "
            "triggers can fire faithfully for decades, which is why a "
            "smell from childhood can still move a grown person to tears. "
            "Mapping your own set is one of the highest-value exercises in "
            "this database: your private triggers are a map of everything "
            "that ever saved you."
        ),
        "how_it_works": (
            "Personal triggers work through associative memory, and their "
            "power comes from how they were encoded. When a strong benefit "
            "arrives - the rescue, the recovery, the showing-up - the "
            "brain stores the event with high emotional arousal, and high "
            "arousal at encoding binds neutral context details (the song, "
            "the smell, the date, the bench) into the same memory trace. "
            "Later, any one of those details can reactivate the whole "
            "trace, re-running a diluted copy of the original appraisal - "
            "benefit plus source - and producing the aftershock feeling "
            "described in the time-course record. Anniversaries work "
            "through the calendar as a retrieval cue: the date itself "
            "becomes a conditioned reminder, which is why the feeling can "
            "arrive 'on schedule' without deliberate recall. Objects work "
            "through the endowment of meaning: the tool is not just a "
            "tool but a compressed symbol of the grandparent's teaching, "
            "so handling it unpacks the whole lineage of benefit. The "
            "privacy of these triggers is a feature of the mechanism: "
            "because the association was formed by your history alone, no "
            "one else carries the same wiring, so the feeling fires "
            "without needing social validation. The durability follows "
            "from the encoding strength: arousal-bound associations resist "
            "extinction, which is why deliberate gratitude practices often "
            "work by building new, gentler associations on purpose - "
            "choosing the cues rather than waiting for history to choose "
            "them."
        ),
        "key_points": [
            "Personal triggers are private tripwires: songs, smells, dates, places, objects wired by your own history.",
            "They are powerful because they fire without social scaffolding - the feeling arrives with no audience.",
            "They are durable: arousal-bound associations can fire faithfully for decades.",
            "Anniversaries work through the calendar as a retrieval cue: gratitude arriving on schedule.",
            "Mapping your own set is mapping everything that ever saved you.",
        ],
        "requirements": [
            "Five trigger types covered: sensory, anniversary, place, object, with concrete examples.",
            "The associative-encoding mechanism stated with the arousal-binding account.",
            "The anniversary-as-retrieval-cue mechanism stated.",
            "The privacy feature explained as a mechanism consequence.",
            "The deliberate-practice bridge: building new associations on purpose.",
        ],
        "standards": [
            "The associative mechanism follows the emotion-memory literature grounded in Lazarus 1991.",
            "The aftershock reactivation follows the time-course account in Scherer 2005.",
            "The constructionist framing of personal meaning follows Barrett 2017.",
        ],
        "citations": [CIT_LAZARUS1991, CIT_SCHERER, CIT_BARRETT],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "surprise_triggers",
        "name": "Surprise Triggers: The Unexpected Things That Set Off Gratitude",
        "group": "Triggers",
        "ladder_rank": 9,
        "ladder_tier": "compounded",
        "description": (
            "Some gratitude arrives through the side door - set off by "
            "things no list of classic triggers would predict. The "
            "vending machine that gives you two candy bars for the price "
            "of one: a tiny unearned benefit, and an absurdly large smile "
            "for forty cents of chocolate. The email from the address you "
            "do not recognize that turns out to be a former student "
            "telling you that one lecture, years ago, changed their "
            "major - gratitude aimed backward through time at your own "
            "past self's work. Finding the lost thing in the last place "
            "you look, exactly where you already looked twice: relief "
            "opens the door and gratitude walks through behind it. The "
            "rain that starts the minute you step under the awning. The "
            "traffic jam that makes you miss the accident ahead - the "
            "counterfactual gratitude of the disaster that did not happen "
            "to you. The compliment from the person you assumed disliked "
            "you. The technology that just works on the day you needed it "
            "to. What unites these odd cases is the mechanism, not the "
            "content: each one delivers an unearned benefit with maximum "
            "surprise and zero expectation of reciprocity - the exact "
            "combination the gratitude circuit is tuned to notice. "
            "Surprise triggers are also the most democratic form of the "
            "emotion: they require no benefactor, no occasion, no "
            "worthiness. They are the universe's small reminder that the "
            "source slot accepts entries from anywhere - and the people "
            "who laugh at the double candy bar are running the same "
            "machinery, at lower volume, as the ones who weep at the "
            "rescue. The lesson is not to chase odd triggers but to "
            "notice what they reveal: the circuit is always on, always "
            "scanning, and it will take gifts from anywhere."
        ),
        "how_it_works": (
            "Surprise triggers work by maxing the surprise input while the "
            "other inputs stay small - which isolates the surprise "
            "mechanism and proves its independent power. The appraisal "
            "system discounts expected benefits: the salary you counted on, "
            "the favor from the person who always helps - these register, "
            "but quietly, because prediction already priced them in. An "
            "unexpected benefit arrives with no such discount: the full "
            "weight of the good lands at once, and the surprise itself "
            "adds arousal that amplifies the warmth. The zero-reciprocity "
            "feature matters too: with no relationship to maintain and no "
            "favor to return, the feeling is pure benefit-recognition, "
            "unmixed with obligation - which is why surprise gratitude "
            "feels so clean. The counterfactual cases (the missed accident, "
            "the rain under the awning) work through mental simulation: "
            "the mind constructs the bad outcome that almost happened, "
            "and the gap between simulation and reality is appraised as a "
            "benefit - the same mechanism as the near-miss trigger, at "
            "smaller scale. The backward-through-time cases (the former "
            "student's email) work through retroactive appraisal: a past "
            "action is re-evaluated as having mattered, and the gratitude "
            "fires in the present for a benefit delivered years ago. All "
            "of it confirms the circuit's design: it is a novelty-"
            "weighted benefit detector, and it does not care whether the "
            "benefit is large, only whether it was unearned and "
            "unpredicted."
        ),
        "key_points": [
            "Surprise triggers max the surprise input while other inputs stay small - isolating surprise's independent power.",
            "Expected benefits get discounted by prediction; unexpected ones land at full weight, with surprise adding arousal.",
            "Zero expected reciprocity makes surprise gratitude feel clean: pure benefit-recognition, unmixed with obligation.",
            "Counterfactual cases work through mental simulation: the almost-disaster, appraised against reality, becomes a gift.",
            "The circuit is a novelty-weighted benefit detector: it cares about unearned and unpredicted, not about large.",
        ],
        "requirements": [
            "At least five oddball examples spanning tiny, counterfactual, backward-time, and no-giver cases.",
            "The prediction-discount mechanism stated.",
            "The zero-reciprocity cleanliness claim explained.",
            "Counterfactual simulation stated as the near-miss mechanism at small scale.",
            "The novelty-weighted detector summary as the design claim.",
        ],
        "standards": [
            "The prediction-discount account follows the appraisal framework of Ortony, Clore and Collins 1988.",
            "The counterfactual mechanism follows the appraisal-timing literature in Scherer 2005.",
            "The surprise-amplification claim follows Frijda 1986 on the role of novelty in emotion intensity.",
        ],
        "citations": [CIT_ORTONY1988, CIT_SCHERER, CIT_FRIJDA],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "chain_reactions",
        "name": "Chain Reactions: How One Thank-You Sets Off a Cascade",
        "group": "Triggers",
        "ladder_rank": 9,
        "ladder_tier": "compounded",
        "description": (
            "Gratitude is the most contagious of the quiet emotions, and "
            "its chains are visible everywhere once you look. The basic "
            "chain: someone helps you, you feel grateful, you thank them "
            "warmly - and your thanks becomes their trigger. Being thanked "
            "genuinely is itself a benefit (recognition is a good), so the "
            "giver feels a smaller echo of gratitude toward you for "
            "noticing, and the bond between you tightens one notch. The "
            "pay-it-forward chain: the stranger's kindness on the bad day "
            "does not just warm you - it primes you, and hours later you "
            "find yourself holding the door, over-tipping, letting the "
            "merging car in, each small generosity carrying a faint "
            "watermark of the morning's rescue. Studies of this effect "
            "find that grateful people help more even when helping costs "
            "them - the feeling does not just motivate repaying the giver, "
            "it generalizes to helping anyone. The witnessing chain: you "
            "watch someone thank someone else sincerely - the tearful "
            "speech at the retirement party, the player pointing to the "
            "stands - and you feel moved without being involved at all; "
            "observed gratitude triggers gratitude's neighbors in the "
            "audience. The upward spiral: gratitude broadens attention "
            "(you notice more good), the noticed good triggers more "
            "gratitude, which broadens further - the positive feedback "
            "loop researchers describe as the engine of lasting well-"
            "being. Chains can also run backward: withheld thanks "
            "starves the giver's reinforcer function, and chronic "
            "ingratitude in a relationship slowly teaches the giver to "
            "stop giving - the cascade in reverse. The practical moral is "
            "simple and large: every expressed gratitude is a stone "
            "dropped in water, and the ripples are not metaphorical - they "
            "are measurable in the next person's behavior."
        ),
        "how_it_works": (
            "The chain reaction runs on the three moral-affect functions "
            "firing in sequence across people. Your gratitude's motive "
            "function drives your thank-you and your pay-it-forward "
            "helping; your thank-you lands on the giver as a benefit "
            "(recognition), firing their barometer function and producing "
            "the echo of warmth toward you; and your thanks simultaneously "
            "fires their reinforcer function, raising the probability they "
            "help again - the loop that stabilizes generosity in groups. "
            "The generalization to strangers (helping anyone, not just the "
            "giver) runs through the broaden mechanism: positive affect "
            "widens the scope of attention and the sense of social "
            "connection, so the motive to help spills beyond the original "
            "dyad. The witnessing chain runs through emotional contagion "
            "and elevation: observing sincere thanks activates the "
            "observer's own prosocial circuitry without any direct benefit "
            "changing hands. The upward spiral is the feedback loop made "
            "explicit: gratitude broadens attention, broadened attention "
            "notices more benefits, noticed benefits trigger more "
            "gratitude. The reverse cascade - ingratitude teaching givers "
            "to stop - is the reinforcer function firing negatively: "
            "unacknowledged giving extinguishes over time, exactly as "
            "learning theory predicts. The whole system is a distributed "
            "computation: no single brain holds the chain, but the "
            "give-thank-give protocol propagates prosocial behavior "
            "through a population like a beneficial contagion."
        ),
        "key_points": [
            "The basic chain: your thanks is itself a benefit to the giver, firing their gratitude echo and tightening the bond.",
            "Pay-it-forward: gratitude generalizes - grateful people help strangers more, even at cost to themselves.",
            "Witnessing sincere thanks moves uninvolved observers: the contagion needs no direct benefit.",
            "The upward spiral: gratitude broadens attention, broadened attention notices more good, more good triggers more gratitude.",
            "The reverse cascade: chronic ingratitude extinguishes giving - the reinforcer function firing negatively.",
        ],
        "requirements": [
            "Four chain types named: basic, pay-it-forward, witnessing, upward spiral, plus the reverse cascade.",
            "Each chain mapped to the moral-affect functions (barometer, motive, reinforcer).",
            "The generalization mechanism explained via broadening.",
            "The reverse cascade explained via extinction of unreinforced giving.",
            "The distributed-computation summary: the give-thank-give protocol as population-level contagion.",
        ],
        "standards": [
            "The three functions follow McCullough, Kilpatrick, Emmons and Larson 2001.",
            "The prosocial-generalization findings follow Bartlett and DeSteno 2006.",
            "The upward-spiral account follows Fredrickson 2004 on broaden-and-build.",
        ],
        "citations": [CIT_MCCULLOUGH2001, CIT_BARTLETT2006, CIT_FREDRICKSON2004],
        "sig_lens": SIG_LENS_DEF,
    },
    # ------------------------------------------------ 22-25 HOW IT SHOWS IN BEHAVIOR
    {
        "key": "actions",
        "name": "What People Do When They Feel Grateful",
        "group": "How It Shows in Behavior",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Grateful people are easy to spot by what they do, because "
            "gratitude is an emotion with a to-do list. First they "
            "acknowledge: the thank-you spoken, written, or sent - and the "
            "grateful thank-you is specific, naming what was done and what "
            "it meant, not the generic 'thanks' tossed over a shoulder. "
            "Then they repay: the returned favor, the gift in kind, the "
            "effort to balance the ledger - not from heavy obligation but "
            "from the warm urge to send something back. Then they pay "
            "forward: the kindness passed to a third party, the door held "
            "for a stranger, the tip enlarged - gratitude's most "
            "distinctive behavior, the one that turns a private feeling "
            "into a public chain. They also savor: grateful people linger "
            "over the good thing, retell the story, keep the note, "
            "revisit the place - the behavior of someone who has decided "
            "the benefit deserves more than a moment. They draw closer: "
            "gratitude moves people to spend time with their benefactors, "
            "to choose them, to invest - the find-remind-bind function in "
            "action, the relationship upgraded by the feeling. And they "
            "give more generally: the experiments are consistent - "
            "grateful people volunteer more, share more, help strangers "
            "more, even when it costs them. What grateful people notably "
            "do not do: they do not keep score with a cold eye, they do "
            "not use the favor as leverage, and they do not perform "
            "gratitude as a tactic. The action list is warm all the way "
            "down, because the feeling driving it is warm all the way "
            "down."
        ),
        "how_it_works": (
            "The action list is the moral-motive function executing its "
            "program. Acknowledgment is the cheapest and most direct "
            "output: a specific thank-you delivers recognition to the "
            "giver (their benefit) at near-zero cost, which is why it is "
            "the default first action and why its absence is so noticeable. "
            "Repayment is the ledger-balancing output: the mind tracks "
            "benefits received as open loops, and the warm urge to repay "
            "is the loop-closing drive - distinct from cold obligation by "
            "its affective tone. Pay-it-forward is the generalization "
            "output: the broaden mechanism widens the target set from the "
            "giver to anyone, because the positive affect has expanded the "
            "sense of social connection beyond the dyad. Savoring is the "
            "memory-consolidation output: lingering and retelling "
            "strengthen the memory tag, which schedules future aftershocks "
            "and deepens the attitude change toward the giver. Drawing "
            "closer is the bind output: the relationship-upgrade function "
            "that moves benefactors up the priority list for time, "
            "attention, and future cooperation. The generalized generosity "
            "is the spillover output: with the prosocial circuitry primed, "
            "the threshold for helping anyone drops. The notable absences - "
            "no score-keeping, no leverage, no tactic - follow from the "
            "affect itself: cold calculation requires the very detachment "
            "that warm gratitude dissolves."
        ),
        "key_points": [
            "The gratitude to-do list: acknowledge specifically, repay warmly, pay forward, savor, draw closer, give generally.",
            "The grateful thank-you is specific - naming what was done and what it meant - not the generic tossed 'thanks.'",
            "Pay-it-forward is gratitude's most distinctive behavior: the private feeling turned into a public chain.",
            "Savoring (lingering, retelling, keeping the note) consolidates the memory tag and schedules aftershocks.",
            "The notable absences: no cold score-keeping, no leverage, no performed gratitude as tactic.",
        ],
        "requirements": [
            "Six named action tendencies with the mechanism each serves.",
            "The specific-vs-generic thank-you distinction stated.",
            "Pay-it-forward identified as the most distinctive behavior.",
            "The savoring-memory-tag link stated.",
            "The three notable absences stated with the affective-tone reason.",
        ],
        "standards": [
            "The motive function follows McCullough, Kilpatrick, Emmons and Larson 2001.",
            "The find-remind-bind account follows Algoe 2012.",
            "The generalized-generosity findings follow Bartlett and DeSteno 2006.",
        ],
        "citations": [CIT_MCCULLOUGH2001, CIT_ALGOE2012, CIT_BARTLETT2006],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "speech",
        "name": "What Grateful People Say: Phrases, Tone, and Speech Patterns",
        "group": "How It Shows in Behavior",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Grateful speech has a fingerprint, and it is specificity. The "
            "generic 'thanks' could mean anything; the grateful 'thank you "
            "for staying late to fix the slides - you saved the whole "
            "presentation' means exactly one thing, and the giver hears "
            "the difference instantly. Listen for the naming: grateful "
            "people name the act ('for driving through the storm'), name "
            "the cost ('I know you gave up your Saturday'), and name the "
            "effect ('I would have been lost without it'). Listen for the "
            "second person: grateful sentences point at the giver - 'you "
            "did,' 'you noticed,' 'you came' - where self-focused speech "
            "points at the speaker. The tone is the other half of the "
            "fingerprint: slower than normal speech, slightly lower, with "
            "the pause before the thank-you where the feeling catches up "
            "to the words. Volume drops rather than rises - real gratitude "
            "is rarely shouted. There are characteristic phrases, worn "
            "smooth by use because they work: 'I really appreciate it,' "
            "with the 'really' doing honest work; 'that meant a lot to "
            "me,' which tells the giver the benefit landed; 'I will not "
            "forget this,' the ledger entry spoken aloud; and at high "
            "intensity, the broken 'thank you' repeated past the point of "
            "information, functioning purely as feeling made audible. "
            "Written gratitude follows the same rules with more care: the "
            "thank-you note that names specifics is kept for years; the "
            "generic one is recycled by Friday. The speech of gratitude is "
            "never efficient - it takes longer than it needs to, and that "
            "inefficiency is the point: the extra words are the wrapping "
            "paper, proving the gift of acknowledgment was chosen, not "
            "grabbed off a shelf."
        ),
        "how_it_works": (
            "Specificity works because it proves the appraisal actually "
            "ran. A generic 'thanks' can be produced by the script alone, "
            "with no benefit-detection behind it; naming the act, the "
            "cost, and the effect requires the speaker to have actually "
            "registered what happened, which is why specific thanks are "
            "trusted and generic thanks are discounted. The second-person "
            "focus works through the source attribution: pointing the "
            "sentence at the giver mirrors the appraisal's pointing at "
            "the source, so the grammar of grateful speech is the grammar "
            "of the feeling. The slowed tempo and lowered volume are the "
            "parasympathetic signature leaking into speech: the body that "
            "has stood down speaks more slowly and softly, and listeners "
            "read the tempo as sincerity below awareness. The pause before "
            "the thank-you is the appraisal-then-expression sequence made "
            "audible - the half-second where the feeling arrives first. "
            "Repetition past information ('thank you, thank you, thank "
            "you') works as an intensity signal: when words are "
            "insufficient, quantity substitutes, and the listener correctly "
            "reads the surplus as overflow rather than content. The "
            "inefficiency principle generalizes: in acknowledgment, effort "
            "signals value, so the longer, more specific, more carefully "
            "chosen the thanks, the more the giver's reinforcer function "
            "fires - which is why the kept-for-years note outperforms the "
            "tossed-off text by orders of magnitude in relationship "
            "effect."
        ),
        "key_points": [
            "The fingerprint is specificity: naming the act, the cost, and the effect proves the appraisal actually ran.",
            "Grateful sentences point at the giver - 'you did,' 'you noticed' - mirroring the appraisal's source attribution.",
            "Tone: slower, slightly lower, volume dropping; the pause before the thank-you is the feeling arriving first.",
            "Repetition past information ('thank you, thank you') functions as an intensity signal, not content.",
            "Inefficiency is the point: the extra words are wrapping paper, proving the acknowledgment was chosen.",
        ],
        "requirements": [
            "The specificity fingerprint stated with the act-cost-effect triple.",
            "The second-person grammar rule stated with the appraisal-mirroring reason.",
            "Tone and tempo described: slower, lower, quieter, with the pause.",
            "Characteristic phrases listed with what each one accomplishes.",
            "The inefficiency principle stated as the effort-signals-value rule.",
        ],
        "standards": [
            "The appraisal-expression account follows Lazarus 1991 and Scherer 2005.",
            "The sincerity-perception claims follow the expression literature grounded in Ekman 1999.",
            "The reinforcer effect of acknowledgment follows McCullough, Kilpatrick, Emmons and Larson 2001.",
        ],
        "citations": [CIT_LAZARUS1991, CIT_EKMAN1999, CIT_MCCULLOUGH2001],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "decisions",
        "name": "How Gratitude Changes Decisions and Judgment",
        "group": "How It Shows in Behavior",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Gratitude quietly rewrites the decision calculus. The most "
            "documented shift is generosity: grateful people give more - "
            "more money in sharing experiments, more time volunteering, "
            "more help to strangers - and they do it even when giving "
            "costs them directly. The mechanism is not confusion or "
            "soft-headedness; it is a changed ledger. Gratitude makes the "
            "world feel abundant - benefits have been arriving, the "
            "account is full - and abundant-feeling people share more "
            "freely than scarcity-feeling people. The second shift is "
            "patience: grateful people discount the future less steeply, "
            "choosing the larger later reward over the smaller immediate "
            "one more often. The present already feels good, so there is "
            "less urgency to grab now. The third shift is toward the "
            "giver: decisions about trust, hiring, partnering, and "
            "forgiving all tilt toward people who have helped - the bind "
            "function upgrading their entry in every future choice. The "
            "fourth is risk: gratitude slightly increases comfortable "
            "risk-taking in social domains (reaching out, trusting, "
            "trying) while decreasing reckless financial risk - the "
            "feeling says the world is benign, not that it is a casino. "
            "There are failure modes, and honesty requires naming them: "
            "gratitude can be exploited - the calculated favor designed to "
            "buy compliance; it can bias judgment toward the giver past "
            "the evidence; and in its indebted form it can push people to "
            "repay beyond reason. But the net effect, measured across the "
            "experiments, is a decider who is more generous, more patient, "
            "more trusting of proven helpers, and more oriented toward "
            "the long term - which is most of what wise deciding looks "
            "like."
        ),
        "how_it_works": (
            "The generosity shift runs through the abundance appraisal: "
            "gratitude's core computation is 'benefits have arrived from "
            "outside my efforts,' which updates the background model of "
            "the world toward plenty. Plenty-models share; scarcity-models "
            "hoard - so the sharing increase is the rational output of "
            "the updated model, not a failure of self-interest. The "
            "patience shift runs through reduced urgency: with the present "
            "appraised as good, the marginal value of immediate reward "
            "drops, flattening the discount curve - the same mechanism by "
            "which contentment aids patience, here driven by the social "
            "channel. The giver-tilt runs through the ledger upgrade: the "
            "benefactor's trust entry is permanently raised by the bind "
            "function, so future decisions involving them start from a "
            "higher prior - rational, given that past generosity predicts "
            "future cooperativeness. The risk pattern splits by domain "
            "because the appraisal is about social benignity, not general "
            "luck: the world feels kinder, so social bets feel safer, "
            "while the absence of any 'I am lucky' component leaves "
            "financial risk judgment unmoved or slightly more cautious. "
            "The failure modes are the same mechanisms overshooting: the "
            "abundance model can be gamed by strategic givers; the ledger "
            "upgrade can overweight one data point; the repay drive, when "
            "mixed with the separate indebtedness circuit, can produce "
            "over-repayment. Knowing the mechanisms lets the decider keep "
            "the gains - generosity, patience, long-termism - while "
            "watching the failure modes, which is the advanced use of "
            "this record."
        ),
        "key_points": [
            "Gratitude increases generosity: more giving, more volunteering, more helping strangers, even at direct cost.",
            "The mechanism is the abundance update: 'benefits have been arriving' rewrites the background model toward plenty.",
            "Gratitude increases patience: the present feels good, so the future is discounted less steeply.",
            "Decisions tilt toward proven givers: the bind function permanently upgrades their trust entry.",
            "Failure modes are real: strategic favors can exploit it, and the giver-tilt can overweight one data point.",
        ],
        "requirements": [
            "Four decision shifts named: generosity, patience, giver-tilt, risk pattern.",
            "Each shift given its mechanism, not just its description.",
            "The abundance-model account of generosity stated as rational update.",
            "The domain-split in risk effects explained.",
            "Failure modes named honestly with the overshoot mechanisms.",
        ],
        "standards": [
            "The generosity findings follow Bartlett and DeSteno 2006.",
            "The patience and decision effects follow the gratitude-and-well-being review: Wood, Froh and Geraghty 2010.",
            "The appraisal-mechanism accounts follow Lazarus 1991 and Frijda 1986.",
        ],
        "citations": [CIT_BARTLETT2006, CIT_WOOD2010, CIT_FRIJDA],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "intensity_behavior",
        "name": "Behavior Under Intensity: How Gratitude Escalates",
        "group": "How It Shows in Behavior",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "As the dial turns up, grateful behavior escalates through a "
            "recognizable ladder of its own. At mild intensity, behavior "
            "is minimal and social: the nod, the brief specific thanks, "
            "the small reciprocal gesture - holding the door in return, "
            "the two-dollar tip becoming three. The system registers and "
            "moves on; the ledger gets a small entry. At moderate "
            "intensity, behavior becomes deliberate: the thank-you note "
            "written that evening, the return favor planned and executed, "
            "the story told to others ('you will not believe what she "
            "did'), the relationship visibly upgraded - more time, more "
            "warmth, more priority. The giver is told, clearly, that the "
            "gift landed. At high intensity, behavior becomes "
            "transformative: the tearful speech, the life redirected - "
            "the scholarship founded in the teacher's name, the career "
            "changed to do for others what was done for you, the vow made "
            "and kept for decades. High-intensity gratitude does not just "
            "repay; it reorganizes. It changes who the person spends time "
            "with, what they work on, sometimes who they understand "
            "themselves to be. The escalation is orderly: each level "
            "includes the previous level's behaviors and adds a longer "
            "time horizon - mild acts in the moment, moderate acts across "
            "days, high acts across years. And there is a ceiling worth "
            "naming: past a certain point, more intensity does not produce "
            "more behavior but different behavior - the shift from doing "
            "things to becoming someone, from the thank-you note to the "
            "life lived as thanks. That is the top of the ladder, and it "
            "is where the showcase simulation of the final record lives."
        ),
        "how_it_works": (
            "The behavioral escalation follows the same input-strength "
            "logic as the feeling, extended across time horizons. Mild "
            "inputs produce enough motive force for low-cost immediate "
            "outputs: the nod, the brief thanks, the small reciprocal "
            "gesture - actions whose cost is trivial and whose timing is "
            "now. Moderate inputs generate enough sustained motive to "
            "support planned action across days: the note, the favor, the "
            "retelling - each requiring the motive to survive the gap "
            "between feeling and execution, which it does via the memory "
            "tag and the aftershocks. High inputs produce motive strong "
            "enough to reorganize priorities: when a benefit is appraised "
            "as life-altering, the ledger entry for the giver - or for the "
            "class of people the giver represents - becomes a standing "
            "life goal, which is why high gratitude founds scholarships "
            "and changes careers rather than just sending notes. The "
            "inclusion structure (each level containing the previous) "
            "reflects the motive's monotonicity: stronger feeling never "
            "removes the weaker outputs, it only adds longer-horizon ones. "
            "The ceiling effect - doing shifting to becoming - is the "
            "identity-level resolution: when the benefit is large enough "
            "to change the self-model ('I am someone who was saved; I am "
            "someone who helps'), behavior stops being a series of acts "
            "and becomes a trait, which is the mechanism by which intense "
            "state gratitude converts into lasting dispositional change."
        ),
        "key_points": [
            "Mild: minimal and social - the nod, brief specific thanks, small reciprocal gestures, in the moment.",
            "Moderate: deliberate - the note written that evening, the return favor planned, the story retold, the relationship upgraded.",
            "High: transformative - the tearful speech, the redirected life, the scholarship, the career changed.",
            "Each level includes the previous and adds a longer time horizon: moments, days, years.",
            "The ceiling: past a point, behavior shifts from doing things to becoming someone - the life lived as thanks.",
        ],
        "requirements": [
            "Three behavioral bands with concrete examples at each.",
            "The time-horizon extension stated as the escalation structure.",
            "The inclusion principle stated: stronger levels contain weaker outputs.",
            "The memory-tag bridge explaining how motive survives the feeling-execution gap.",
            "The ceiling effect stated as identity-level resolution.",
        ],
        "standards": [
            "The motive-strength account follows McCullough, Kilpatrick, Emmons and Larson 2001.",
            "The time-horizon structure follows the action-readiness account in Frijda 1986.",
            "The identity-resolution claim follows the dispositional literature: Watkins, Woodward, Stone and Kolts 2003.",
        ],
        "citations": [CIT_MCCULLOUGH2001, CIT_FRIJDA, CIT_WATKINS2003],
        "sig_lens": SIG_LENS_DEF,
    },
    # ------------------------------------------------ 26-28 HEALTHY EXPRESSION
    {
        "key": "healthy_expression",
        "name": "Healthy Expression: Saying It, Showing It, Channeling It Well",
        "group": "How to Express It Healthily",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Healthy gratitude expression has three channels, and the "
            "healthiest lives use all three. Saying it is the first: the "
            "specific, timely thank-you - specific because generic thanks "
            "do not prove the appraisal ran, timely because gratitude has "
            "a half-life and the giver deserves to hear it while the "
            "warmth is fresh. Say it to their face when you can; the "
            "voice carries what text cannot, and the held gaze completes "
            "the circuit. Showing it is the second: the hand on the "
            "shoulder, the longer hug, the face allowed to do what it "
            "wants - the nonverbal half of acknowledgment, which lands "
            "deeper than words because it is harder to fake. The thank-you "
            "note belongs here too: slower than speech, kept longer than "
            "speech, the written form that givers save in drawers for "
            "years. Channeling it is the third and most powerful: turning "
            "the feeling into action - the return favor done well, the "
            "kindness paid forward to a stranger, the ongoing reciprocity "
            "that says 'your gift is still working.' The three channels "
            "form a completeness scale: saying alone is good, saying plus "
            "showing is better, all three is the full expression that "
            "leaves neither the giver wondering nor the feeling stuck "
            "inside you. A note on receiving, which is expression's twin: "
            "healthy gratitude includes letting yourself be thanked - "
            "accepting the thanks without deflecting, minimizing, or "
            "immediately reversing it. The deflected thank-you starves the "
            "giver's reinforcer function; the received one completes the "
            "loop for both sides. Expression is not performance. It is "
            "the current flowing: notice, name, return - and let return "
            "come back to you, too."
        ),
        "how_it_works": (
            "The three channels map to the three moral-affect functions. "
            "Saying it serves the reinforcer function directly: specific, "
            "timely acknowledgment is the reward signal that teaches the "
            "giver's brain to keep giving - which is why the research on "
            "expressed gratitude finds givers misunderstand its impact: "
            "expressers consistently underestimate how much their thanks "
            "matter to the receiver. Showing it serves the sincerity "
            "channel: nonverbal signals are harder to fake, so they carry "
            "more weight in the giver's authenticity check, deepening the "
            "bond beyond what words alone achieve. Channeling it serves "
            "the motive function at full power: converting feeling into "
            "repaid and paid-forward action is the behavior the emotion "
            "evolved to produce, and completing it resolves the open "
            "ledger loop - which is why unexpressed gratitude sits warm "
            "and aching while expressed gratitude settles into glow. The "
            "completeness scale reflects additive function-firing: each "
            "channel fires a different part of the system, and all three "
            "together close every loop. The receiving half matters "
            "because the protocol is two-sided: the giver's reinforcer "
            "function needs the acknowledgment to land, and deflection "
            "('oh, it was nothing') discounts the reward signal, "
            "weakening future giving. Healthy expression is therefore not "
            "just self-care but system maintenance: every completed loop "
            "keeps the give-thank-give protocol running for everyone "
            "downstream."
        ),
        "key_points": [
            "Three channels: saying it (specific, timely), showing it (touch, face, the kept note), channeling it (repay, pay forward).",
            "Completeness scale: saying alone is good, plus showing is better, all three closes every loop.",
            "Expressers underestimate their impact: givers value thanks far more than thankers predict.",
            "Unexpressed gratitude sits warm and aching; expressed gratitude settles into glow - the loop must close.",
            "Receiving thanks graciously is expression's twin: deflection starves the giver's reinforcer function.",
        ],
        "requirements": [
            "Three channels named with the what and why of each.",
            "The specificity and timeliness rules for saying it.",
            "The underestimation finding stated with its direction.",
            "The expressed-vs-unexpressed resolution contrast stated.",
            "The receiving half covered as system maintenance, not just manners.",
        ],
        "standards": [
            "The three functions follow McCullough, Kilpatrick, Emmons and Larson 2001.",
            "The underestimation of expressed gratitude follows Kumar and Epley 2018.",
            "The channel account follows the expression literature grounded in Frijda 1986.",
        ],
        "citations": [CIT_MCCULLOUGH2001, CIT_KUMAR2018, CIT_FRIJDA],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "unhealthy_expression",
        "name": "Unhealthy Expression: Forced Thanks, Keeping Score, and What Each Costs",
        "group": "How to Express It Healthily",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Gratitude goes wrong in a handful of recognizable ways, and "
            "each has its price. Bottling it is the quietest failure: "
            "the feeling is real but never exits - the thank-you never "
            "said, the note never written. The cost is double: the giver "
            "never gets the reinforcer signal, so the bond does not "
            "tighten, and the feeling sits inside you warm and aching "
            "instead of settling into glow - unclosed loops are expensive "
            "to carry. Forcing it is the loud failure: thanks performed "
            "without the feeling - the effusive card written from "
            "obligation, the toast that says everything except anything "
            "true. The cost is hollowness: the giver's authenticity check "
            "usually catches it, and even when it does not, the performer "
            "knows, which corrodes the real thing by association. Keeping "
            "score is the cold failure: gratitude converted into "
            "accounting - the mental spreadsheet of who owes whom, the "
            "favor remembered specifically to be deployed later. The cost "
            "is the death of warmth: score-keeping replaces the "
            "appreciation circuit with the transaction circuit, and the "
            "relationship becomes a business. Weaponizing it is the "
            "cruelest failure: gratitude demanded or deployed as leverage "
            "- 'after everything I have done for you' - which is not "
            "gratitude at all but control wearing its clothes; the cost "
            "is the recipient's trust, permanently discounted. And "
            "guilt-masked gratitude: the thank-you that is really an "
            "apology for needing help, which burdens the giver with your "
            "discomfort instead of gifting them your warmth. The common "
            "thread: every unhealthy form breaks the loop the healthy "
            "form closes. The repair is always the same direction: back "
            "to specific, timely, sincere acknowledgment - the current "
            "flowing freely, neither dammed nor forced nor metered."
        ),
        "how_it_works": (
            "Each failure mode breaks a different part of the mechanism. "
            "Bottling breaks the expression half of the loop: the "
            "appraisal fired and the motive primed, but the output never "
            "executed, so the reinforcer function never fires in the "
            "giver and the motive never discharges in the self - the "
            "physiological correlate is the sustained warm ache of "
            "uncompleted action tendency. Forcing breaks the appraisal "
            "half: the script runs with no benefit-detection behind it, "
            "so the involuntary markers are absent and the observer's "
            "configural reader flags the mismatch - the hollowness is the "
            "felt gap between performed output and absent input. "
            "Score-keeping swaps circuits: the warm appreciation appraisal "
            "(benefit plus benevolent source) is replaced by the cold "
            "exchange appraisal (benefit plus debt), which routes the "
            "motive from prosocial warmth to transactional repayment - "
            "same ledger, different currency. Weaponizing inverts the "
            "direction: instead of the receiver's warmth flowing to the "
            "giver, the giver's past giving is used to extract compliance "
            "from the receiver - the moral-affect machinery run in "
            "reverse, which is why it reads as violation rather than "
            "thanks. Guilt-masking contaminates the signal: the "
            "acknowledgment carries an apology payload, so the giver "
            "receives discomfort instead of reward, and the reinforcer "
            "fires negatively. The repair direction is uniform because "
            "the healthy form is the mechanism's designed output: "
            "specific, timely, sincere acknowledgment is simply the loop "
            "completing as built."
        ),
        "key_points": [
            "Bottling: real feeling, no exit - the giver gets no signal, and the unclosed loop sits warm and aching.",
            "Forcing: script without appraisal - the authenticity check catches it, and the performer knows.",
            "Score-keeping: warmth converted to accounting - the appreciation circuit swapped for the transaction circuit.",
            "Weaponizing: gratitude demanded as leverage - the machinery run in reverse, reading as violation.",
            "Guilt-masking: the thank-you carrying an apology payload, burdening the giver instead of rewarding them.",
            "Every failure breaks the loop; the repair is always back to specific, timely, sincere acknowledgment.",
        ],
        "requirements": [
            "Five failure modes named with concrete examples and specific costs.",
            "Each failure mapped to the mechanism part it breaks.",
            "The score-keeping circuit-swap explained as appreciation vs transaction.",
            "Weaponizing distinguished as machinery-in-reverse.",
            "The uniform repair direction stated as the designed output.",
        ],
        "standards": [
            "The loop-breaking analysis follows the moral-affect functions of McCullough, Kilpatrick, Emmons and Larson 2001.",
            "The authenticity-detection account follows Ekman 1999.",
            "The circuit-swap framing follows the appraisal distinctions in Lazarus 1991.",
        ],
        "citations": [CIT_MCCULLOUGH2001, CIT_EKMAN1999, CIT_LAZARUS1991],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "everyday_practices",
        "name": "Everyday Practices: Small Habits That Keep Gratitude Flowing",
        "group": "How to Express It Healthily",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The practices are small on purpose: gratitude is trained the "
            "way a muscle is trained, by regular light reps, not by "
            "occasional heroic efforts. The journal: three specific good "
            "things before bed, with the giver or source named for each - "
            "specificity is what makes the appraisal run rather than the "
            "script. The thank-you note: one per week, to someone who "
            "will not expect it - the unexpectedness multiplies the "
            "giver's reinforcer firing, and writers consistently report "
            "the note warms them as much as the receiver. The savoring "
            "pause: when something good lands - the first sip, the "
            "message, the view - stop for ten seconds and let the "
            "appraisal complete instead of rushing past; the pause is "
            "where the feeling gets to exist. The mental subtraction: "
            "once in a while, imagine the good thing absent - the friend "
            "moved away, the health gone, the help never offered - and "
            "feel the contrast; subtraction is the fastest route to "
            "recognizing a benefit, because the mind prices things by "
            "loss. The spoken daily thanks: one specific thank-you per "
            "day, said aloud to a person - the reps that keep the "
            "expression channel open. The evening replay: running the "
            "day's small kindnesses back before sleep, which doubles as "
            "the sleep practice from the body records. None of these "
            "requires feeling grateful first; that is the key insight the "
            "research keeps confirming. The practices do not harvest "
            "existing gratitude - they manufacture the conditions for the "
            "appraisal to fire, and the feeling follows the recognition. "
            "Do them for weeks and the threshold lowers: the world starts "
            "looking generous, because the detector got better. That is "
            "not positive thinking. It is instrument calibration."
        ),
        "how_it_works": (
            "Every practice targets the same trainable parameter: the "
            "benefit-detection threshold. The journal works through "
            "directed attention: forcing the daily scan for benefits "
            "practices the detection appraisal until it fires more "
            "readily - the specificity requirement ensures the appraisal "
            "runs rather than the script. The thank-you note works "
            "through expression-completion: it exercises the full loop "
            "from recognition to acknowledgment, and the unexpectedness "
            "maxes the receiver's surprise input, which is why writers "
            "get the warm glow of a completed high-value loop. The "
            "savoring pause works through appraisal completion time: most "
            "benefits in modern life are rushed past before the source "
            "attribution finishes; the ten-second pause gives the second "
            "half of the appraisal time to run. Mental subtraction works "
            "through contrast amplification: the simulated absence makes "
            "the benefit's size vivid, maxing the benefit-size input "
            "directly. The daily spoken thanks works through channel "
            "maintenance: expression is a skill with a decay rate, and "
            "daily reps keep the output pathway fluent so thanks exit "
            "easily when the feeling arrives. The evening replay works "
            "through the aftershock mechanism plus cognitive competition "
            "at sleep onset. The threshold-lowering over weeks is "
            "perceptual learning: the same process by which radiologists "
            "learn to see tumors - repeated directed attention tunes the "
            "detector. The practices are therefore not mood tricks but "
            "calibration routines for a real instrument."
        ),
        "key_points": [
            "Six practices: the specific journal, the weekly unexpected note, the savoring pause, mental subtraction, one daily spoken thanks, the evening replay.",
            "You do not need to feel grateful first: the practices manufacture the conditions for the appraisal, and the feeling follows.",
            "Specificity is load-bearing: it forces the appraisal to run rather than the script.",
            "Mental subtraction prices benefits by loss: imagining the good thing absent makes its size vivid.",
            "Weeks of reps lower the detection threshold: the world looks generous because the detector got better - calibration, not positive thinking.",
        ],
        "requirements": [
            "Six named practices with the how and the why of each.",
            "The feel-first myth corrected: practices precede feeling.",
            "Each practice mapped to its mechanism (threshold, loop completion, appraisal time, contrast, channel maintenance, aftershock).",
            "The perceptual-learning frame for threshold lowering.",
            "The calibration-not-positive-thinking summary.",
        ],
        "standards": [
            "The practice effects follow Emmons and McCullough 2003 and Emmons 2007.",
            "The review-level grounding follows Wood, Froh and Geraghty 2010.",
            "The threshold-learning account follows the dispositional literature: Watkins, Woodward, Stone and Kolts 2003.",
        ],
        "citations": [CIT_EMMONS2003, CIT_EMMONS2007, CIT_WOOD2010],
        "sig_lens": SIG_LENS_DEF,
    },
    # ------------------------------------------------ 29-31 RECOGNIZING IN OTHERS
    {
        "key": "reading_signs",
        "name": "Reading Gratitude in Others: Face, Body, Voice, and Behavior Cues",
        "group": "How to Recognize It in Others",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Reading gratitude in another person is a cluster skill: no "
            "single tell is reliable, but the cluster rarely lies. Start "
            "with the face: the softened bright eyes with the outer-corner "
            "crinkle, the slightly raised inner brow, the genuine smile "
            "that reaches the eyes, the gaze that holds on you a beat "
            "longer than conversation needs. Add the body: the small nod "
            "that escapes before the words, the hand drifting toward the "
            "chest, the torso angled fully toward you, the stillness of "
            "someone who has stopped multitasking to receive the moment. "
            "Listen to the voice: slower, slightly lower, quieter than "
            "their baseline - and the pause before the thank-you, the "
            "half-second where you can hear the feeling arriving before "
            "the words. Watch the behavior after: the specific thanks "
            "that names what you did, the return gesture within days, the "
            "story retold to others with you as the hero, the relationship "
            "visibly warmer next time you meet. The cluster has a tempo "
            "signature too: genuine gratitude is never rushed - the "
            "unhurried thank-you, the lingered moment, the note that "
            "arrives three days later because they kept thinking about "
            "it. Calibrate for the instrument: the quiet person shows you "
            "the eyes and the stillness; the effusive person shows you "
            "the hug and the retelling - read the change from their "
            "baseline, not the absolute volume. And respect the base "
            "rate: most people under-express, so the absence of a big "
            "display is not the absence of the feeling - look for the "
            "small signs, the held gaze, the specific words, the "
            "remembered detail weeks later that proves the memory tag "
            "fired."
        ),
        "how_it_works": (
            "The cluster method works because each channel has a "
            "different fakability, and the combination is harder to "
            "counterfeit than any part. The face's involuntary markers "
            "(crinkle, tear shine) cannot be produced without the "
            "activation; the voice's tempo shift (slower, lower, the "
            "pause) is controlled below awareness; the body's orienting "
            "(full front, stillness) is the approach system made visible; "
            "and the delayed behaviors (the note three days later, the "
            "remembered detail) cannot be faked in the moment because "
            "they require the memory tag to have actually fired. Reading "
            "the change from baseline rather than absolute volume "
            "corrects for the dispositional and cultural dials: the "
            "quiet person's small nod can carry as much signal as the "
            "effusive person's speech, once you know their normal "
            "settings. The tempo signature works because the "
            "appraisal-then-expression sequence has a fixed order - "
            "feeling first, words after - and any performance that "
            "reverses the order reads as rushed. The base-rate correction "
            "(under-expression is normal) prevents the classic error of "
            "the gratitude reader: concluding 'they did not care' from "
            "a small display, when the research on expressed gratitude "
            "shows the feeling routinely exceeds the show. The delayed "
            "tells are the most diagnostic of all: nobody fakes a "
            "remembered detail weeks later, because faking requires "
            "motive in the moment, and the moment has passed."
        ),
        "key_points": [
            "Read the cluster, never a single tell: face (crinkle, held gaze), body (nod, hand to chest, stillness), voice (slower, lower, the pause), delayed behavior.",
            "The tempo signature: genuine gratitude is never rushed - the unhurried thank-you, the note three days later.",
            "Calibrate to baseline: read the change from their normal, not the absolute volume.",
            "Respect the base rate: under-expression is normal - absence of big display is not absence of feeling.",
            "The most diagnostic tells are delayed: the remembered detail weeks later proves the memory tag fired.",
        ],
        "requirements": [
            "Four channels covered with specific cues in each.",
            "The cluster-not-single-tell principle stated with the fakability reason.",
            "The tempo signature described.",
            "Baseline calibration explained with the dial metaphor.",
            "The base-rate correction stated with the under-expression finding.",
        ],
        "standards": [
            "The cue descriptions follow Ekman and Friesen FACS 1978 and Ekman 1999.",
            "The under-expression base rate follows Kumar and Epley 2018.",
            "The configural-reading account follows Barrett 2017.",
        ],
        "citations": [CIT_FACS, CIT_KUMAR2018, CIT_BARRETT],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "supportive_responses",
        "name": "What to Say and Do When Someone Near You Feels Grateful",
        "group": "How to Recognize It in Others",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "When someone's gratitude is aimed at you, your response "
            "completes or breaks their loop - and the right moves are "
            "simple. Receive it fully: hold the gaze, let the pause "
            "happen, do not rush to fill the silence - their feeling "
            "needs a half-second of your stillness to land. Accept "
            "without deflecting: 'you are so welcome' beats 'oh, it was "
            "nothing' every time, because 'it was nothing' discounts the "
            "very benefit they are trying to honor, and discounting "
            "someone's gratitude is a small rejection wearing polite "
            "clothes. Name it back: 'I could see it mattered to you' or "
            "'I am glad I could be there' - reflecting the feeling "
            "confirms the signal was received, which is what their "
            "reinforcer function was built to hear. If the gratitude is "
            "big - tears, the cracked voice - do not try to fix the "
            "crying; the tears are the overflow valve doing its job. A "
            "hand on the shoulder, a nod, and quiet are the correct "
            "tools. If someone is grateful toward a third party in your "
            "presence ('my nurse was incredible'), amplify, do not "
            "redirect: 'tell me what she did' feeds the savoring and the "
            "aftershocks, while changing the subject starves them. And "
            "when the gratitude comes as a surprise - the note out of "
            "nowhere, the call years later - treat it as the high-value "
            "event it is: respond warmly and specifically, because "
            "surprise gratitude took courage to send, and your response "
            "decides whether the sender ever sends another. The master "
            "rule underneath all of it: gratitude is a gift being handed "
            "to you. Take it with both hands."
        ),
        "how_it_works": (
            "Each recommended response serves one of the loop's functions. "
            "Receiving fully - the held gaze, the allowed pause - gives "
            "the expresser's motive function its completed output: the "
            "acknowledgment visibly lands, discharging the warm urge "
            "instead of leaving it hanging. Not deflecting protects the "
            "reinforcer signal: 'it was nothing' tells the giver's "
            "learning system the act had low value, weakening future "
            "giving, while 'you are so welcome' confirms the value and "
            "strengthens it. Naming it back ('I could see it mattered') "
            "closes the epistemic loop: the expresser needs to know the "
            "signal was not just heard but understood, and reflected "
            "feeling is the confirmation. Not fixing the tears respects "
            "the overflow mechanism: the lacrimal venting is the system "
            "regulating itself, and intervention reads as discomfort "
            "with the feeling. Amplifying third-party gratitude ('tell me "
            "what she did') feeds the savoring and retelling outputs, "
            "which consolidate the memory tag and schedule aftershocks - "
            "you are helping their gratitude complete its own work. "
            "Honoring surprise gratitude protects the sender's future "
            "expression: sending unexpected thanks is socially risky "
            "(fear of awkwardness), and a warm specific response lowers "
            "the perceived risk, keeping the channel open. The master "
            "rule - take it with both hands - is the two-sided protocol "
            "stated as etiquette: the loop needs a receiver as much as a "
            "sender."
        ),
        "key_points": [
            "Receive fully: hold the gaze, allow the pause - their feeling needs your stillness to land.",
            "'You are so welcome' beats 'it was nothing': deflection discounts the benefit they are honoring.",
            "Name it back ('I could see it mattered') - reflected feeling confirms the signal was understood.",
            "Do not fix the tears: the overflow valve is regulating itself; a hand on the shoulder and quiet are the tools.",
            "Amplify third-party gratitude ('tell me what she did'); honor surprise gratitude warmly - your response decides if they ever send another.",
        ],
        "requirements": [
            "Five response moves named with the function each serves.",
            "The deflection harm explained via the reinforcer signal.",
            "The tears protocol stated: no fixing, quiet presence.",
            "Third-party and surprise gratitude covered as special cases.",
            "The master rule stated as the two-sided protocol.",
        ],
        "standards": [
            "The reinforcer-protection account follows McCullough, Kilpatrick, Emmons and Larson 2001.",
            "The expression-impact findings follow Kumar and Epley 2018.",
            "The savoring-amplification account follows Fredrickson 2004.",
        ],
        "citations": [CIT_MCCULLOUGH2001, CIT_KUMAR2018, CIT_FREDRICKSON2004],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "mistakes",
        "name": "What NOT to Do: Mistakes That Spoil Grateful Moments",
        "group": "How to Recognize It in Others",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Grateful moments are fragile, and the ways to break them are "
            "depressingly common. The classic is the instant deflection: "
            "'oh please, it was nothing, anyone would have done it' - "
            "fired off before the thanks has finished landing. It feels "
            "modest; it functions as rejection, telling the grateful "
            "person their feeling is disproportionate to reality. The "
            "second is the immediate reversal: 'no, thank YOU' batted back "
            "like a ping-pong ball, which converts their vulnerable moment "
            "into a rally nobody asked for. The third is the ledger joke: "
            "'you owe me one!' - said lightly, heard heavily, instantly "
            "converting their warm appreciation circuit into the cold "
            "transaction circuit. The fourth is correcting the gratitude: "
            "'well, actually it was mostly Sarah's idea' - factually true, "
            "emotionally catastrophic, because it tells them their "
            "appraisal misfired. The fifth is rushing past it: checking "
            "the phone mid-thank-you, or pivoting to business before the "
            "pause completes - the body language of 'your feeling is an "
            "interruption.' The sixth is performing discomfort: the "
            "exaggerated aw-shucks routine that makes the thanker feel "
            "they have imposed, teaching them to swallow it next time. "
            "The seventh is the delayed poison: accepting warmly in the "
            "moment and then deploying the favor later - 'after all I did "
            "for you' - which retroactively converts their gratitude into "
            "evidence for your leverage. Every one of these teaches the "
            "same lesson: expressing thanks is unsafe here. And people "
            "learn fast. The grateful person who gets deflected, rushed, "
            "or leveraged three times stops expressing - not because the "
            "feeling stops, but because the loop keeps breaking. Guard "
            "the loop. It is the cheapest valuable thing you will ever "
            "protect."
        ),
        "how_it_works": (
            "Each mistake breaks the loop at a specific joint. Instant "
            "deflection breaks the reinforcer joint: by declaring the "
            "benefit worthless ('it was nothing'), it tells the giver's "
            "learning system the act had no value and tells the expresser "
            "their appraisal was wrong - a double break. Immediate "
            "reversal breaks the receiver joint: the expresser extended "
            "vulnerability (acknowledging need and dependence), and the "
            "reversal refuses the receiver role, leaving the vulnerability "
            "unmet. The ledger joke breaks the circuit joint: it swaps the "
            "warm appreciation appraisal for the cold exchange appraisal "
            "mid-stream, and circuits do not un-swap easily - the moment's "
            "warmth is spent. Correcting breaks the epistemic joint: the "
            "expresser's appraisal is publicly marked as error, which "
            "punishes the detection habit itself. Rushing breaks the tempo "
            "joint: the appraisal-then-expression sequence needs its "
            "half-second, and interruption signals that the feeling is "
            "unwelcome. Performed discomfort breaks the safety joint: it "
            "associates expression with imposing, raising the future cost "
            "of thanks. Delayed weaponizing breaks the trust joint "
            "retroactively: it rewrites the history of the exchange, "
            "teaching that gratitude given will be stored as ammunition. "
            "The three-strikes learning curve is standard operant "
            "conditioning: punished expression extinguishes, usually "
            "within a handful of trials. Guarding the loop is therefore "
            "not sentimentality but maintenance of a learning system: "
            "every cleanly received thanks keeps the population's "
            "give-thank-give protocol alive."
        ),
        "key_points": [
            "Instant deflection ('it was nothing') functions as rejection: it marks their appraisal as disproportionate.",
            "The ledger joke ('you owe me one!') swaps the warm circuit for the cold transaction circuit mid-stream.",
            "Correcting the thanks ('actually it was Sarah's idea') punishes the detection habit itself.",
            "Rushing past it signals the feeling is an interruption; performed discomfort teaches that thanks impose.",
            "Delayed weaponizing ('after all I did') retroactively converts their gratitude into your leverage.",
            "Punished expression extinguishes fast: three broken loops and the thanks stop coming.",
        ],
        "requirements": [
            "Seven named mistakes with the joint each breaks.",
            "Each mistake given its mechanism, not just its description.",
            "The double-break nature of deflection stated.",
            "The circuit-swap permanence noted for the ledger joke.",
            "The extinction curve stated with the population-level maintenance moral.",
        ],
        "standards": [
            "The reinforcer-joint analysis follows McCullough, Kilpatrick, Emmons and Larson 2001.",
            "The extinction account follows standard learning theory as applied in Frijda 1986.",
            "The expression-safety findings follow Kumar and Epley 2018.",
        ],
        "citations": [CIT_MCCULLOUGH2001, CIT_FRIJDA, CIT_KUMAR2018],
        "sig_lens": SIG_LENS_DEF,
    },
    # ------------------------------------------------ 32-34 RELATED + SIMULATION
    {
        "key": "neighbors",
        "name": "The Gratitude Map: Nearest Neighbors, Opposites, and Close Cousins",
        "group": "Related Emotions and Mixes",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Gratitude's neighborhood is crowded, and telling the "
            "neighbors apart is a genuine skill. Appreciation is the "
            "closest: the warm noticing of good things. The difference is "
            "the address - appreciation can be objectless (the sunset, "
            "the melody), while gratitude always points at a source, even "
            "if the source is circumstance. Admiration is next door: "
            "warmth toward someone's excellence. The difference is the "
            "benefit - you can admire the surgeon you never met, but you "
            "are grateful to the one who operated on you; admiration "
            "needs no receipt. Indebtedness is the shadow twin, and the "
            "pair most often confused: both follow received benefits, but "
            "indebtedness is the heavy, obligated, must-repay feeling "
            "while gratitude is the warm, drawn-toward feeling - one is "
            "a ledger, the other is a bond. They often co-occur, which is "
            "why the confusion persists, but they are different circuits: "
            "relieve the obligation and indebtedness vanishes while "
            "gratitude remains. Relief is the frequent companion: the "
            "exhale when danger passes. The difference is the source slot - "
            "relief needs only an ended threat, gratitude needs a giver "
            "(though near-misses fill the slot with circumstance, which is "
            "where they overlap). Contentment is the calm cousin: pleased "
            "with how things are, no source required, lower activation - "
            "gratitude's quieter sibling. Joy is the bright sibling: "
            "overlapping heavily (see the blend record), distinguished by "
            "joy's lack of a required address. Love is the deep neighbor: "
            "gratitude deepens into love over repeated exchanges, and love "
            "expresses itself as gratitude toward the beloved - the two "
            "share the bond-building machinery. The opposites: ingratitude "
            "is the true opposite - the benefit received and unacknowledged, "
            "the loop deliberately unclosed; entitlement is its colder "
            "cousin, the benefit received and counted as due. Resentment "
            "sits across the map: where gratitude warms toward the giver, "
            "resentment chills toward the withholder. Learn these borders "
            "and the whole region comes into focus: every neighbor defined "
            "by which of gratitude's parts it keeps and which it drops."
        ),
        "how_it_works": (
            "The map is organized by the appraisal components each emotion "
            "shares with gratitude. The component set is: (1) benefit "
            "detected, (2) source outside the self, (3) benevolent "
            "intention read, (4) warm approach motive. Appreciation keeps "
            "(1) but drops (2) - benefit without a required source. "
            "Admiration keeps a variant of (2) and (3) - excellence "
            "recognized in another - but drops (1), needing no personal "
            "benefit. Indebtedness keeps (1) and (2) but replaces (4) with "
            "the must-repay motive - same ledger, different currency, "
            "which is why relieving the obligation dissolves indebtedness "
            "while leaving gratitude intact. Relief keeps the pleasant "
            "release but its appraisal is threat-ended rather than "
            "benefit-given - the components barely overlap, which is why "
            "the blend of the two (deliverance) feels like a genuinely "
            "new compound. Contentment shares the pleasant valence at "
            "lower activation with no source requirement. Joy shares (1) "
            "and the pleasant valence at higher activation, differing "
            "only in the address requirement. Love shares (4) fully - the "
            "bond-building motive is common machinery - which is why "
            "repeated gratitude exchanges are one of love's reliable "
            "on-ramps. Ingratitude is the negation: (1) detected, loop "
            "deliberately unclosed - the barometer fired but the motive "
            "and reinforcer were refused. Entitlement negates even (1): "
            "the benefit is appraised as due, so no gratitude circuit "
            "fires at all. Resentment inverts (3): the source is read as "
            "withholding rather than giving, flipping the motive from "
            "approach to chill. The component method is the reliable way "
            "to settle any 'is this gratitude or X' question: list the "
            "parts, check which are present."
        ),
        "key_points": [
            "Appreciation: benefit without a required source - the address is the difference.",
            "Admiration: warmth toward excellence with no receipt required - the benefit is the difference.",
            "Indebtedness: the shadow twin - same ledger, different currency; relieve the obligation and only gratitude remains.",
            "Relief, contentment, joy, love: each defined by which of gratitude's four components it keeps or drops.",
            "True opposite: ingratitude - the benefit received and the loop deliberately unclosed; entitlement its colder cousin.",
            "The component method settles any border dispute: list the four parts, check which are present.",
        ],
        "requirements": [
            "Eight neighbors/opposites mapped: appreciation, admiration, indebtedness, relief, contentment, joy, love, ingratitude/entitlement/resentment.",
            "The four-component set stated as the mapping tool.",
            "Each neighbor defined by keep/drop against the components.",
            "The indebtedness dissolution test stated (relieve obligation, see what remains).",
            "The component method given as the general border-dispute procedure.",
        ],
        "standards": [
            "The component analysis follows the appraisal-component framework of Ortony, Clore and Collins 1988.",
            "The gratitude-indebtedness distinction follows Watkins and colleagues and McCullough, Kilpatrick, Emmons and Larson 2001.",
            "The circumplex neighbor distances follow Russell 1980.",
        ],
        "citations": [CIT_ORTONY1988, CIT_MCCULLOUGH2001, CIT_RUSSELL],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "mixes",
        "name": "Gratitude Mixes: Blends with Other Emotions",
        "group": "Related Emotions and Mixes",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Because gratitude is built from parts, it blends the way "
            "paint blends - and the compounds have names worth knowing. "
            "Gratitude plus joy is celebration: the surprise party, the "
            "homecoming - bright, shareable gladness with the thanks "
            "aimed at specific people (see the blend record). Gratitude "
            "plus relief is deliverance: the near-miss on the highway, "
            "the diagnosis that turned out benign - the exhale and the "
            "thank-you arriving as one event, aimed at whatever spared "
            "you. Gratitude plus sadness is the bittersweet: the "
            "retirement party for the beloved mentor, the last visit with "
            "the old house - thankful for what was, grieving that it is "
            "ending, the two feelings braided so tightly they cannot be "
            "separated and should not be. Gratitude plus awe is "
            "reverence: the cathedral, the night sky, the act of "
            "generosity so large it stops the mind - the small self "
            "before the vast good, thankfulness scaled up to wonder. "
            "Gratitude plus love is devotion: the long marriage's quiet "
            "thankfulness, the parent's overwhelming tenderness - the "
            "bond-building machinery running at full power, each "
            "gratitude exchange deepening the love that makes the next "
            "exchange more likely. Gratitude plus guilt is the indebted "
            "blend: the scholarship you feel you have not earned, the "
            "sacrifice you cannot repay - warmth and heaviness together, "
            "the compound that most needs the disentangling this database "
            "teaches (relieve the obligation; keep the warmth). Gratitude "
            "plus pride is the earned-thanks blend: the graduate grateful "
            "to the teachers and proud of the work - self and source "
            "honored together, the healthiest compound on the list. Each "
            "blend has its own face, its own tempo, its own behavior - "
            "the bittersweet cries differently than the celebration - and "
            "learning the blends is learning to read the fine print of "
            "real emotional life, where feelings almost never arrive one "
            "at a time."
        ),
        "how_it_works": (
            "Blends work through appraisal superposition: two appraisal "
            "sets fire on the same event, and the feeling is the sum. "
            "Celebration is joy's 'good thing happened' plus gratitude's "
            "'someone brought it' - the appraisals agree on the event and "
            "differ only in the source slot, so the blend is seamless. "
            "Deliverance is relief's 'threat ended' plus gratitude's "
            "'benefit received,' with circumstance filling the source "
            "slot - the counterfactual simulation (the disaster that "
            "almost was) supplies the benefit magnitude. The bittersweet "
            "is gratitude's benefit appraisal plus sadness's loss "
            "appraisal firing on the same object (the ending good thing) - "
            "the appraisals point in opposite temporal directions (thankful "
            "for the past, grieving the future), which is why the "
            "compound feels braided rather than blended. Reverence is "
            "gratitude's benefit-plus-source plus awe's vastness "
            "appraisal - the source slot expands to the immense, and the "
            "small-self feeling joins the warmth. Devotion is gratitude's "
            "bond motive plus love's attachment system at full gain - the "
            "shared machinery (the find-remind-bind circuit) means this "
            "blend is less a compound than a resonance, each amplifying "
            "the other. The indebted blend is gratitude's warmth plus the "
            "separate obligation circuit - the disentangling works because "
            "the two circuits are genuinely distinct, so addressing the "
            "obligation (repay, renegotiate, release) leaves the warmth "
            "standing. Earned-thanks is gratitude's source-honoring plus "
            "pride's self-honoring - the rare blend with no conflict, "
            "because the appraisals divide the credit cleanly between "
            "self and source. The practical rule: name both appraisals, "
            "and the blend explains itself."
        ),
        "key_points": [
            "Celebration (gratitude + joy): bright shareable gladness with thanks aimed at specific people.",
            "Deliverance (gratitude + relief): the exhale and the thank-you as one event, aimed at whatever spared you.",
            "Bittersweet (gratitude + sadness): thankful for what was, grieving its ending - braided, not blended.",
            "Reverence (gratitude + awe): thankfulness scaled to wonder, the small self before the vast good.",
            "Devotion (gratitude + love): the bond machinery at full gain, each exchange deepening the next.",
            "Indebted blend (gratitude + guilt): disentangle by addressing the obligation; the warmth remains.",
            "Earned-thanks (gratitude + pride): self and source honored together - the healthiest compound.",
        ],
        "requirements": [
            "Seven named blends with the felt character of each.",
            "Each blend explained via appraisal superposition: which appraisals fire.",
            "The bittersweet braided-vs-blended distinction explained via temporal direction.",
            "The indebted blend given the disentangling procedure.",
            "The name-both-appraisals practical rule stated.",
        ],
        "standards": [
            "The blend framework follows Plutchik 1980 on emotion compounds and dyads.",
            "The appraisal-superposition account follows Ortony, Clore and Collins 1988.",
            "The devotion-resonance account follows Algoe 2012 on find, remind, and bind.",
        ],
        "citations": [CIT_PLUTCHIK, CIT_ORTONY1988, CIT_ALGOE2012],
        "sig_lens": SIG_LENS_DEF,
    },
    {
        "key": "full_simulation",
        "name": "Full Behavioral Simulation: A Rescue, from Trigger to Resolution",
        "group": "Related Emotions and Mixes",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The showcase: one gratitude, end to end. Scene one, the "
            "trigger. It is 11 PM, raining, and Maya's car dies on the "
            "unlit stretch past the mill - phone at four percent, no "
            "signal, the hazard blinkers the only light. A pickup slows, "
            "and a man she has never seen gets out with a flashlight and "
            "a tow strap. He spends fifty minutes in the rain - jack, "
            "spare, the lug nuts rusted solid, his jacket given up to "
            "keep her dry while he works. The benefit is large, the cost "
            "is obvious, the need is acute, the surprise is total. Scene "
            "two, onset and peak. The moment the engine turns over, the "
            "appraisal completes: benefit plus source, all at once. The "
            "warmth hits her chest like a wave; her throat closes; she "
            "laughs once, involuntarily, at the absurdity of crying over "
            "a tire. 'Thank you' comes out cracked; she says it four "
            "times, each more broken, holding his sleeve. He waves off "
            "the offered money - 'just help somebody else sometime' - and "
            "the refusal doubles it: the gift is now pure, unpriceable. "
            "Scene three, the body and face. Driving home behind him to "
            "the gas station, her hands shake on the wheel; the long "
            "exhales come in waves; the rearview mirror shows the full "
            "configuration - crinkled eyes, the moved brow, the smile "
            "that keeps collapsing into tears and rebuilding. Scene four, "
            "the aftershocks. She replays it at 2 AM, unable to sleep for "
            "the warmth; retells it at breakfast, voice catching again; "
            "tells it at work, and watches her coworkers go quiet - the "
            "witnessing chain firing in the break room. Scene five, the "
            "expression. She writes the note - not to him, she never "
            "learned his name, but to the universe's lost-and-found: she "
            "posts the story, describes the pickup, and asks the internet "
            "to thank him for her. Then she channels it: the jumper "
            "cables go permanently into her trunk, and a standing rule is "
            "born - she stops for every stranded driver, forever. Scene "
            "six, the chain. Eight months later, on an icy shoulder, she "
            "spends an hour with a shaking teenager and his dead battery, "
            "and as she works she thinks of the rain and the flashlight - "
            "the pay-it-forward completing its circuit. Scene seven, "
            "resolution. Years later the acute feeling is gone, but the "
            "ledger entry is permanent: she is, measurably, a person who "
            "stops. The simulation's moral, if a description may have "
            "one: notice how much machinery one kindness set in motion - "
            "the appraisal, the body, the tears, the retellings, the trunk "
            "rule, the teenager on the ice. That is what the database "
            "means by describing an emotion: not the word 'gratitude,' but "
            "the whole cascade, trigger to resolution, with every part "
            "labeled and every part real."
        ),
        "how_it_works": (
            "The simulation integrates every record in the database into "
            "one run of the machinery. Scene one loads all five intensity "
            "inputs at near-maximum: large benefit (mobility restored at "
            "night), high cost (fifty minutes in rain, the given-up "
            "jacket), acute need (stranded, no signal), total surprise "
            "(a stranger), pure intention (money refused) - the classic-"
            "trigger archetype of help in need. Scene two runs the "
            "appraisal sequence in real time: benefit detection, source "
            "attribution, the onset warmth, the peak as comprehension "
            "completes, the cracked repetition past information as "
            "intensity signal. Scene three displays the body record: the "
            "shaking hands (adrenaline aftermath), the long exhales "
            "(parasympathetic shift), the full facial configuration with "
            "the regulation signs (smile collapsing and rebuilding) of "
            "high intensity. Scene four runs the aftershock mechanism: "
            "the 2 AM replay, the retellings, each re-firing a diluted "
            "copy - plus the witnessing chain in the break room. Scene "
            "five executes the expression ladder: saying (the cracked "
            "thanks), showing (holding his sleeve), channeling (the "
            "posted story, the trunk rule) - and demonstrates the "
            "anonymous-giver edge case, where channeling carries what "
            "saying cannot complete. Scene six is the pay-it-forward "
            "chain made literal: the motive function firing eight months "
            "later, the circuit completing through a stranger. Scene "
            "seven is the resolution into trait: the standing rule ('she "
            "stops') is the identity-level change, state gratitude "
            "converted into disposition. The integration is the point: "
            "no single record explains Maya's night, but every record "
            "explains part of it, and together they simulate a human "
            "being feeling a real feeling all the way through."
        ),
        "key_points": [
            "Scene one loads all five intensity inputs near maximum: the help-in-need archetype with pure intention.",
            "Scene two runs the appraisal in real time: onset warmth, peak comprehension, cracked repetition as intensity signal.",
            "Scene three shows the body record live: shaking hands, long exhales, the high-intensity face cycling.",
            "Scene four runs aftershocks and the witnessing chain: the 2 AM replay, the quiet break room.",
            "Scene five climbs the expression ladder and handles the anonymous-giver edge case via channeling.",
            "Scene six completes the pay-it-forward circuit eight months later, on an icy shoulder.",
            "Scene seven resolves into trait: the standing rule - state gratitude converted into who she is.",
        ],
        "requirements": [
            "Seven scenes walking trigger through peak to resolution.",
            "Every scene tied to specific earlier records by mechanism.",
            "All five intensity inputs loaded in the trigger scene.",
            "The anonymous-giver edge case handled.",
            "The state-to-trait resolution stated as the closing mechanism.",
        ],
        "standards": [
            "The integrated appraisal sequence follows Lazarus 1991, Ortony, Clore and Collins 1988, and Scherer 2005.",
            "The chain mechanisms follow McCullough, Kilpatrick, Emmons and Larson 2001; Bartlett and DeSteno 2006; Algoe 2012.",
            "The broaden-and-build resolution follows Fredrickson 2004.",
        ],
        "citations": [CIT_LAZARUS1991, CIT_MCCULLOUGH2001, CIT_FREDRICKSON2004],
        "sig_lens": SIG_LENS_DEF,
    },
]
