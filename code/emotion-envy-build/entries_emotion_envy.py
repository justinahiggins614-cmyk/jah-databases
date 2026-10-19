#!/usr/bin/env python3
"""Entries for the Envy Emotion databases (Manon's 16:15 orders, emotion series).

Creates two NEW databases, 34 ladder-ordered records each:

  emotion-envy            - The Envy Emotion Database
                           (public-harvest: real, fact-checked psychology of
                           envy - definition, envy vs jealousy, intensity,
                           benign vs malicious envy, first-person
                           simulation, body signals, facial expression,
                           triggers, behavior, healthy expression,
                           recognition in others, related emotions and
                           mixes, and a full behavioral simulation;
                           descriptive and educational only - never
                           diagnosing real people; standard references
                           Aristotle Rhetoric; Darwin 1872; Festinger
                           1954; Ekman and Friesen FACS 1978; Plutchik
                           1980; Russell circumplex 1980; Lazarus 1991;
                           Frijda 1986; Parrott and Smith 1993; Smith and
                           Kim 2007; van de Ven, Zeelenberg and Pieters
                           2009; Takahashi et al. 2009; Scherer 2005;
                           Barrett 2017; APA Dictionary of Psychology)
  emotion-envy-signature  - The Envy Emotion Signature Database
                           (his original Signature Envy Method: envy as the
                           comparator circuit - the gauge that detects the
                           gap between where you stand and where you want to
                           be; benign envy the calibration signal pointing
                           at the upgrade path, malicious envy the warning
                           lamp that says the wiring is misrouted; the
                           Signature reset converts the gap into a plan; src
                           signature, titles suffixed " (Signature
                           Edition)", never presented as authentic public
                           record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
non-decreasing; ladder_tier foundations/compounded/advanced); the shard
index is written in ladder order so pages present simple -> compounded ->
complex.

ID prefixes: JAH-EMEN- (public) and JAH-EMENS- (signature), verified free
in the manifest (zero EMEN hits across all databases) and in every shard
index file (zero JAH-EMEN hits).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_emotion_envy.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos. Demo outputs are
cross-checked against entry text during authoring.

Descriptive/educational only: this database describes and simulates the
emotion of envy. It never diagnoses real people, never labels any real
person with an emotional state, and offers only general, safe, everyday
guidance. No clinical language, no diagnostic labels.

Never the words "bat belt" anywhere. No website references. No Facebook.
No religious talk.
"""

SIG_TAIL = ("Signature original - his original Signature Envy Method: envy "
            "as the comparator circuit - the gauge that detects the gap "
            "between where you stand and where you want to be; benign envy "
            "the calibration signal pointing at the upgrade path, malicious "
            "envy the warning lamp that says the wiring is misrouted; the "
            "Signature reset converts the gap into a plan. Clearly labeled "
            "Signature-made, never presented as authentic public record.")

CIT_ARISTOTLE = ("Aristotle. Rhetoric, Book II, ch. 10: envy as pain felt at "
                 "the sight of another's good fortune, directed at equals in "
                 "the goods that matter - honor, wealth, and the like.")
CIT_DARWIN = ("Darwin C. The Expression of the Emotions in Man and Animals. "
              "London: John Murray; 1872.")
CIT_FESTINGER = ("Festinger L. A theory of social comparison processes. Hum "
                 "Relat. 1954;7(2):117-140.")
CIT_FACS = ("Ekman P, Friesen WV. Facial Action Coding System: A Technique "
            "for the Measurement of Facial Movement. Palo Alto: Consulting "
            "Psychologists Press; 1978.")
CIT_PLUTCHIK = ("Plutchik R. Emotion: A Psychoevolutionary Synthesis. New "
                "York: Harper and Row; 1980.")
CIT_RUSSELL = ("Russell JA. A circumplex model of affect. J Pers Soc Psychol. "
               "1980;39(6):1161-1178.")
CIT_LAZARUS = ("Lazarus RS. Emotion and Adaptation. New York: Oxford "
               "University Press; 1991.")
CIT_FRIJDA = ("Frijda NH. The Emotions. Cambridge: Cambridge University "
              "Press; 1986.")
CIT_SCHERER = ("Scherer KR. What are emotions? And how can they be measured? "
               "Soc Sci Inf. 2005;44(4):695-729.")
CIT_BARRETT = ("Barrett LF. How Emotions Are Made: The Secret Life of the "
               "Brain. Boston: Houghton Mifflin Harcourt; 2017.")
CIT_APA = ("American Psychological Association. APA Dictionary of Psychology. "
           "Envy entry: a negative emotion characterized by feelings of "
           "inferiority, hostility, and resentment caused by awareness of a "
           "coveted attribute, possession, or attainment of another person. "
           "Washington DC: APA.")
CIT_PARROTT = ("Parrott WG, Smith RH. Distinguishing the experiences of envy "
               "and jealousy. J Pers Soc Psychol. 1993;64(6):906-920: envy "
               "concerns lacking what another has; jealousy concerns losing "
               "what one has to a rival.")
CIT_SMITHKIM = ("Smith RH, Kim SH. Comprehending envy. Psychol Bull. "
                "2007;133(1):46-64: envy as inferiority plus ill will and "
                "resentment, distinct from admiration and from simple "
                "desire.")
CIT_VENDEVEN = ("van de Ven N, Zeelenberg M, Pieters R. Leveling up and down: "
                "the experiences of benign and malicious envy. Emotion. "
                "2009;9(3):419-429: benign envy motivates self-improvement, "
                "malicious envy motivates pulling the envied person down.")
CIT_TAKAHASHI = ("Takahashi H, Kato M, Matsuura M, et al. When your gain is "
                 "my pain and your pain is my gain: neural correlates of envy "
                 "and schadenfreude. Science. 2009;323(5916):937-939: envy "
                 "tracks pain-circuit activity; schadenfreude tracks reward "
                 "circuitry.")

SIG_LENS_WHAT = ("The Signature read: envy is the comparator circuit. Where "
                 "public psychology charts the feeling, the Signature Envy "
                 "Method treats envy as the gauge on the panel - it detects "
                 "the gap between where you stand and where you want to be. "
                 "The gap itself is data, not damage. Every envy record "
                 "below carries the same public facts, reframed as his "
                 "original Signature engineering of the feeling.")
SIG_LENS_FEEL = ("The Signature read: envy is the comparator circuit. The "
                 "Signature Envy Method reads the felt ache of envy as the "
                 "needle moving on the gauge - the system reporting a "
                 "measured difference between your position and someone "
                 "else's. A live needle means the instrument works.")
SIG_LENS_BODY = ("The Signature read: envy is the comparator circuit. The "
                 "Signature Envy Method reads the body's tension under envy "
                 "as current in the wires - the comparison circuit drawing "
                 "power. The reading tells you how much the gap matters to "
                 "you, which is useful calibration data.")
SIG_LENS_FACE = ("The Signature read: envy is the comparator circuit. The "
                 "Signature Envy Method treats the envied face as a "
                 "suppressed readout - the dial trying to stay still while "
                 "the needle pushes. What leaks through is the true "
                 "measurement.")
SIG_LENS_TRIGGER = ("The Signature read: envy is the comparator circuit. "
                    "The Signature Envy Method treats every trigger as the "
                    "circuit closing - a person, object, or event completing "
                    "the comparison loop. Know what closes your loop and "
                    "you know where your gauges are set.")
SIG_LENS_BEHAVE = ("The Signature read: envy is the comparator circuit. "
                   "The Signature Envy Method sorts envy behavior into two "
                   "outputs: the calibration output (benign - chase the "
                   "standard) and the misrouted output (malicious - "
                   "short-circuit the other panel). The wiring choice is "
                   "the whole game.")
SIG_LENS_HEALTHY = ("The Signature read: envy is the comparator circuit. "
                    "The Signature Envy Method's reset: take the gap the "
                    "gauge detected and convert it into a plan - the "
                    "calibration signal becomes the upgrade path, the "
                    "warning lamp gets rewired. Bottling it rusts the "
                    "gauge; venting it melts the wires.")
SIG_LENS_RECOG = ("The Signature read: envy is the comparator circuit. The "
                  "Signature Envy Method teaches reading other people's "
                  "gauges without touching their wiring - notice the "
                  "suppressed readout, respond to the gap, never to the "
                  "person's worth.")
SIG_LENS_RELATED = ("The Signature read: envy is the comparator circuit. "
                    "The Signature Envy Method maps envy among its neighbor "
                    "instruments - jealousy the loss-alarm, admiration the "
                    "unburdened gauge, resentment the grounded wire. The "
                    "full simulation runs the whole panel end to end.")

ENTRIES = [
    # ------------------------------------------------ 1-4 WHAT ENVY IS
    {
        "key": "definition",
        "name": "What Envy Is: A Plain-Language Definition",
        "group": "What the Emotion Is",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Envy is the painful feeling that arrives when someone else has "
            "something you want and do not have - a possession, an ability, "
            "a position, a relationship, a quality. In plain words, envy is "
            "the ache of comparison: you measure yourself against another "
            "person, find yourself coming up short in some area that "
            "matters to you, and the shortfall stings. The APA Dictionary "
            "of Psychology defines it as a negative emotion of inferiority, "
            "hostility, and resentment caused by awareness of a coveted "
            "attribute, possession, or attainment of another person. Three "
            "ingredients are always present: a comparison with someone "
            "else, a sense of lacking what they have, and pain about the "
            "gap. It is not the same as simply wanting something - desire "
            "alone is about the object, while envy is always about the "
            "other person who has it. A person can want a bigger house "
            "without envying anyone; envy begins the moment the neighbor's "
            "house becomes the measuring stick. Envy is one of the most "
            "universal human experiences: Aristotle described it over two "
            "thousand years ago as pain at another's good fortune, and "
            "every culture has words and stories for it. This database "
            "describes the emotion from every angle - what it is, how it "
            "feels, how it shows, and how it can be handled well - purely "
            "as education and description. It never diagnoses anyone and "
            "never labels any real person."
        ),
        "how_it_works": (
            "Envy works as a comparison signal. The mind constantly and "
            "mostly unconsciously measures the self against others - this "
            "is social comparison, the process Festinger described in "
            "1954. When the comparison comes back unfavorable in a domain "
            "you care about - looks, money, status, talent, love - the "
            "brain registers the gap as a threat to self-worth, and envy "
            "is the felt form of that registration. That is why envy only "
            "bites when the domain matters: you do not envy a stranger's "
            "chess rating if you have never played chess, but you may envy "
            "a colleague's promotion if career standing is central to who "
            "you are. The closer the other person is to you in similarity "
            "and the more the advantage seems undeserved or unreachable, "
            "the sharper the sting. Brain imaging work by Takahashi and "
            "colleagues in 2009 found envy tracking activity in the "
            "anterior cingulate cortex - a region involved in the "
            "experience of pain - which is why envy genuinely hurts rather "
            "than merely disappointing. The feeling then pushes toward "
            "action: either toward closing the gap yourself (benign envy) "
            "or toward resenting the other person's advantage (malicious "
            "envy)."
        ),
        "key_points": [
            "Envy always involves three parts: a comparison, a felt lack, and pain about the gap.",
            "It is distinct from simple desire: envy is about the other person who has the thing, not just the thing itself.",
            "It only stings in domains that matter to the person's sense of self.",
            "The closer and more similar the other person, the sharper the envy tends to be.",
            "It is universal and ancient - described by Aristotle and found in every culture.",
        ],
        "requirements": [
            "A plain-language definition that an ordinary reader recognizes from their own life.",
            "Clear separation from simple wanting, which lacks the social comparison.",
            "Coverage of the three ingredients: comparison, lack, pain.",
            "The signal function stated: what envy marks and what it motivates.",
            "A stated educational boundary: description only, never diagnosis of any real person.",
        ],
        "standards": [
            "Definitions follow the APA Dictionary of Psychology envy entry: inferiority, hostility, and resentment from awareness of a coveted attribute, possession, or attainment.",
            "Comparison account follows Festinger 1954: self-evaluation through comparison with similar others.",
            "Neural pain account follows Takahashi et al. 2009: envy tracks pain-circuit activity.",
        ],
        "citations": [CIT_APA, CIT_FESTINGER, CIT_ARISTOTLE, CIT_TAKAHASHI],
        "sig_lens": SIG_LENS_WHAT,
    },
    {
        "key": "family",
        "name": "Envy and Jealousy: Telling the Two Apart",
        "group": "What the Emotion Is",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Envy and jealousy are the most commonly confused pair in the "
            "whole emotion family, and ordinary language mixes them "
            "constantly - people say 'I'm jealous of your car' when they "
            "mean envy. Psychologists draw a sharp line: envy involves two "
            "parties, jealousy involves three. Envy is 'I want what you "
            "have' - the pain of lacking something another person "
            "possesses. Jealousy is 'I am afraid of losing what I have to "
            "you' - the fear that a rival will take away a relationship, "
            "position, or affection that is currently yours. Parrott and "
            "Smith's 1993 research showed the experiences feel different: "
            "envy centers on inferiority and longing, jealousy centers on "
            "threat, suspicion, and the urge to guard. A simple test: if "
            "the other person disappeared, would the feeling vanish? If "
            "yes, it was envy - there is no one left to compare with. If "
            "the feeling would remain as worry about the rival, it was "
            "jealousy. The two can co-occur - someone can envy a rival's "
            "charm and simultaneously fear losing a partner to them - but "
            "they are different instruments playing at once, not one "
            "instrument. Getting the distinction right matters because the "
            "two respond to different handling: envy is eased by closing "
            "or reframing the gap, jealousy by securing or clarifying the "
            "threatened bond. This record is descriptive only and never "
            "labels any real person."
        ),
        "how_it_works": (
            "The two emotions run on different appraisals. Envy's appraisal "
            "is upward social comparison: someone else has a valued good, "
            "I lack it, the gap reflects on me. The core relational theme, "
            "in Lazarus's terms, is wanting what another possesses. "
            "Jealousy's appraisal is threat to a valued relationship or "
            "possession: a third party may take what is mine. The core "
            "theme is potential loss. Because the appraisals differ, the "
            "action tendencies differ too - Frijda's framework predicts "
            "envy pushes toward leveling (either rising to the standard or "
            "resenting it), while jealousy pushes toward guarding, "
            "monitoring, and excluding the rival. In the circumplex model "
            "of Russell, both sit in the unpleasant, activated quadrant, "
            "which is why they feel similar in the body even though their "
            "minds are about different things. On Plutchik's wheel, neither "
            "is a primary emotion; both are complex blends - envy blending "
            "sadness-like inferiority with anger-like hostility, jealousy "
            "blending fear of loss with anger at the rival. Recognizing "
            "which appraisal is running lets a person respond to the real "
            "situation instead of the confused one."
        ),
        "key_points": [
            "Envy = two parties (I lack what you have); jealousy = three parties (I fear losing what I have to a rival).",
            "Envy centers on inferiority and longing; jealousy centers on threat and guarding.",
            "The disappearance test: no rival, no envy - but jealousy can linger as suspicion.",
            "The two can co-occur as separate instruments, not one feeling.",
            "Each responds to different handling: envy to the gap, jealousy to the threatened bond.",
        ],
        "requirements": [
            "A sharp, testable distinction between envy and jealousy.",
            "The two-party vs three-party structure stated plainly.",
            "Different felt centers (inferiority vs threat) and action tendencies (leveling vs guarding).",
            "Acknowledgment that the two can co-occur.",
            "A stated educational boundary: description only, never diagnosis of any real person.",
        ],
        "standards": [
            "Distinction follows Parrott and Smith 1993: envy as lacking what another has, jealousy as threatened loss to a rival.",
            "Appraisal framing follows Lazarus 1991: distinct core relational themes drive distinct emotions.",
            "Action tendencies follow Frijda 1986: emotions carry characteristic urges toward leveling or guarding.",
        ],
        "citations": [CIT_PARROTT, CIT_LAZARUS, CIT_FRIJDA, CIT_RUSSELL],
        "sig_lens": SIG_LENS_WHAT,
    },
    {
        "key": "intensity",
        "name": "How Strong Envy Can Get: Mild, Moderate, and Intense",
        "group": "What the Emotion Is",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Envy is not one fixed feeling; it is a dial. At the mild end "
            "it is a passing twinge - a flicker of 'oh, nice for them' "
            "with a small undertow, gone in minutes, barely noticed. This "
            "is the everyday envy of scrolling past someone's vacation "
            "photos: a brief comparison, a small sting, then the mind "
            "moves on. At the moderate level the feeling settles in and "
            "stays: the comparison replays, the gap gets measured again "
            "and again, and the person's mood takes on a gray, irritable "
            "tint for hours or days. Attention narrows onto the envied "
            "person or possession; ordinary pleasures taste slightly "
            "worse. At the intense end envy becomes consuming: intrusive "
            "thoughts about the other person's advantage, real physical "
            "discomfort, difficulty concentrating on anything else, and a "
            "pull toward hostile thoughts or undermining actions. The same "
            "emotion is running at all three settings - comparison, lack, "
            "pain - but the volume changes everything about how it feels "
            "and what it does. Volume is set by how much the domain "
            "matters, how similar the other person is, how deserved the "
            "advantage seems, and how trapped the person feels about "
            "closing the gap. Recognizing the volume is a practical skill: "
            "a twinge needs nothing but noticing, a settled mood needs "
            "reframing, and a consuming state needs deliberate cooling and "
            "distance from the trigger. Descriptive only - never a label "
            "for any real person."
        ),
        "how_it_works": (
            "Intensity in envy tracks the appraisal ingredients. Scherer's "
            "component model helps: the more goal-relevant the domain, the "
            "more certain and deserved the other's advantage seems, and "
            "the lower the person's own perceived control over closing "
            "the gap, the stronger the felt envy. Mild envy is a fast, "
            "low-commitment appraisal - the comparison fires and fades "
            "because the domain is peripheral. Moderate envy means the "
            "appraisal keeps re-firing: rumination re-runs the comparison, "
            "each re-run refreshing the pain signal that Takahashi's team "
            "found in the anterior cingulate. Intense envy adds the "
            "hostility component documented by Smith and Kim: inferiority "
            "plus ill will, a blend that sustains itself because the "
            "resentment gives the mind something to chew on. Duration "
            "matters as much as peak: a mild twinge that gets ruminated "
            "into a week-long mood has become moderate envy through "
            "repetition. This is why the practical lever at every volume "
            "is the same - interrupt the comparison loop, either by "
            "redirecting attention, reframing the gap, or converting the "
            "energy into action toward one's own goals."
        ),
        "key_points": [
            "Envy runs on a dial: twinge (mild), settled mood (moderate), consuming state (intense).",
            "The same three ingredients - comparison, lack, pain - at every volume.",
            "Volume is set by domain importance, similarity, perceived deservedness, and perceived control.",
            "Rumination can turn a mild twinge into a moderate mood through repetition.",
            "The practical lever at every volume is interrupting the comparison loop.",
        ],
        "requirements": [
            "Three clearly separated intensity bands with lived descriptions.",
            "The same emotion identified across all bands, not three different feelings.",
            "The appraisal ingredients that set the volume, stated plainly.",
            "Rumination identified as the volume-raiser.",
            "A stated educational boundary: description only, never diagnosis of any real person.",
        ],
        "standards": [
            "Appraisal-ingredient account follows Scherer 2005: goal relevance, certainty, and control shape intensity.",
            "Pain-signal repetition follows Takahashi et al. 2009: sustained envy tracks sustained pain-circuit activity.",
            "Inferiority-plus-ill-will blend follows Smith and Kim 2007.",
        ],
        "citations": [CIT_SCHERER, CIT_TAKAHASHI, CIT_SMITHKIM, CIT_RUSSELL],
        "sig_lens": SIG_LENS_WHAT,
    },
    {
        "key": "myths",
        "name": "Common Myths and Misunderstandings About Envy",
        "group": "What the Emotion Is",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Envy is one of the most mythologized emotions, and the myths "
            "make it harder to handle. Myth one: 'envy means you are a bad "
            "person.' In fact envy is a standard human signal - "
            "researchers find it across cultures and ages, and feeling it "
            "says nothing about character; only what a person does with it "
            "is a matter of choice. Myth two: 'envy and jealousy are the "
            "same thing.' They are different instruments, as the "
            "distinction record shows - one about lacking, one about "
            "losing. Myth three: 'envy is always destructive.' The "
            "benign-malicious distinction from van de Ven and colleagues "
            "shows otherwise: benign envy, the painful admiration that "
            "says 'I want to reach that level too,' reliably motivates "
            "people to work harder and improve. Myth four: 'successful "
            "people do not feel envy.' They do - envy tracks what matters "
            "to the person, and high achievers care intensely about their "
            "domains, which makes them prime candidates for sharp "
            "comparison pain. Myth five: 'if you just stop comparing, envy "
            "disappears.' Comparison is largely automatic - Festinger's "
            "whole point was that people evaluate themselves against "
            "others constantly and mostly without choosing to. The skill "
            "is not abolishing comparison but steering it: choosing fair "
            "comparisons, limiting exposure to engineered highlight reels, "
            "and converting the gap into a plan. Clearing these myths "
            "matters because shame about feeling envy keeps people from "
            "examining it, and unexamined envy is the kind that curdles. "
            "Descriptive only - never a label for any real person."
        ),
        "how_it_works": (
            "Myths about envy persist because envy is a concealed emotion: "
            "people rarely admit to it, so public understanding runs on "
            "caricature rather than experience. The 'bad person' myth "
            "confuses the feeling with the action - Frijda's framework "
            "separates the emotion (with its action tendency) from the "
            "behavior, and tendencies can be overridden. The "
            "'always destructive' myth ignores the appraisal fork: when "
            "the envied advantage seems attainable and deserved, the "
            "action tendency points at self-improvement (benign envy); "
            "only when it seems unattainable or undeserved does the "
            "tendency point at tearing down (malicious envy). The "
            "'stop comparing' myth ignores automaticity - Barrett's "
            "constructed-emotion view notes the brain predicts and "
            "compares continuously as part of keeping the body's budget; "
            "you cannot switch off the instrument, only recalibrate it. "
            "Each myth, once cleared, reveals the same practical truth: "
            "envy is information about what you value and where you feel "
            "behind, and information is useful the moment you stop being "
            "ashamed of receiving it."
        ),
        "key_points": [
            "Feeling envy says nothing about character; only actions are a matter of choice.",
            "Envy is not always destructive - benign envy motivates improvement.",
            "Successful people feel envy too; it tracks what matters, not what is missing overall.",
            "Comparison is largely automatic and cannot simply be switched off.",
            "Shame about envy keeps it unexamined; unexamined envy is the kind that curdles.",
        ],
        "requirements": [
            "At least five named myths, each corrected with the real account.",
            "The feeling-vs-action separation stated explicitly.",
            "The benign-malicious fork tied to the 'always destructive' myth.",
            "Automaticity of comparison tied to the 'just stop comparing' myth.",
            "A stated educational boundary: description only, never diagnosis of any real person.",
        ],
        "standards": [
            "Benign-malicious distinction follows van de Ven, Zeelenberg and Pieters 2009.",
            "Feeling-action separation follows Frijda 1986: action tendencies are overridable urges.",
            "Automatic comparison follows Festinger 1954 and Barrett 2017: prediction and comparison are continuous.",
        ],
        "citations": [CIT_VENDEVEN, CIT_FRIJDA, CIT_FESTINGER, CIT_BARRETT],
        "sig_lens": SIG_LENS_WHAT,
    },
]
ENTRIES += [
    # ------------------------------------------------ 5-9 HOW IT FEELS
    {
        "key": "first_person",
        "name": "Inside the Feeling: A First-Person Passage",
        "group": "How It Feels",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "This is what envy feels like from the inside, in the second "
            "person of a simulation - nobody real, only the feeling "
            "itself. You hear the news - the promotion, the engagement, "
            "the new house - and your mouth says 'that's wonderful' half "
            "a beat too fast while something cold drops behind your "
            "ribs. The congratulations come out right; the face does the "
            "right thing. But underneath, a small voice starts doing "
            "arithmetic: their age and yours, their start and yours, what "
            "they did that you didn't, what they got that you haven't. "
            "The room keeps going - people are laughing, someone refills "
            "a glass - and you are suddenly somewhere else, replaying "
            "your own choices with their outcome pasted over them. There "
            "is a sour, metallic taste to it, like biting a lemon you "
            "didn't choose. Part of you is genuinely glad for them and "
            "part of you wishes the news had waited until you had your "
            "own version, and the two parts argue in a loop you can't "
            "quite leave. You catch yourself scanning for flaws in their "
            "good fortune - it must have been luck, connections, timing - "
            "and then feel cheap for the scanning. That is the signature "
            "of the feeling: wanting to be the kind of person who only "
            "feels glad, while feeling the other thing anyway. This "
            "passage is a simulation for education. It describes no real "
            "person and diagnoses no one."
        ),
        "how_it_works": (
            "The first-person texture of envy comes from two processes "
            "running at once. The first is upward comparison running "
            "automatically: the brain registers the other's advantage, "
            "measures the gap, and - because the domain matters - tags "
            "the gap as self-relevant, which is why it lands in the body "
            "as a drop or a sting rather than as neutral information. "
            "The second is self-evaluation under threat: the same "
            "comparison that produced the sting now gets re-run with "
            "counterfactuals ('if I had...'), which is why the mind "
            "loops. Lazarus's appraisal view captures the double "
            "movement: the event is appraised as relevant (someone like "
            "me got something I want) and as incongruent with my goals "
            "(I don't have it), producing the characteristic blend of "
            "pain and longing. The urge to diminish the other's fortune "
            "- luck, connections, timing - is the malicious fork "
            "starting to open: if the advantage can be made to seem "
            "undeserved, the pain eases, because the comparison feels "
            "less legitimate. The shame about feeling envious is a "
            "second-order appraisal - judging the feeling itself - and "
            "it is what makes envy go underground instead of getting "
            "examined."
        ),
        "key_points": [
            "Envy arrives as a double movement: gladness on the surface, arithmetic underneath.",
            "The body registers it as a drop, sting, or sourness - comparison made physical.",
            "Counterfactual replay ('if I had...') is what makes the mind loop.",
            "Scanning for flaws in the other's fortune is the malicious fork opening.",
            "Shame about the feeling drives it underground; the passage keeps it in the light.",
        ],
        "requirements": [
            "A vivid first-person passage covering the social moment, the inner arithmetic, and the shame.",
            "The double movement (surface gladness, underneath comparison) rendered concretely.",
            "The looping quality of counterfactual replay included.",
            "The flaw-scanning urge named as the malicious fork.",
            "A stated simulation boundary: describes no real person, diagnoses no one.",
        ],
        "standards": [
            "Double appraisal follows Lazarus 1991: relevance plus goal-incongruence.",
            "Automatic comparison follows Festinger 1954.",
            "Malicious-fork framing follows van de Ven, Zeelenberg and Pieters 2009.",
        ],
        "citations": [CIT_LAZARUS, CIT_FESTINGER, CIT_VENDEVEN, CIT_APA],
        "sig_lens": SIG_LENS_FEEL,
    },
    {
        "key": "time_course",
        "name": "How Envy Changes Over Time: Onset, Peak, Fading, Aftershock",
        "group": "How It Feels",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Envy has a weather pattern, and knowing the forecast helps. "
            "Onset is fast - often under a minute from the triggering "
            "news or sight to the first sting. The comparison fires "
            "before deliberate thought: you see the thing, the gap "
            "measures itself, the drop lands. The peak usually arrives "
            "within the first hour, when the mind is doing its heaviest "
            "replay - the counterfactuals are freshest, the arithmetic "
            "most detailed, the body most activated. This is the phase "
            "where people do and say things they later regret, because "
            "the hostile fork is loudest at peak. Fading begins when "
            "attention moves on: a demanding task, a absorbing "
            "conversation, sleep. Without re-triggering, the felt sting "
            "typically softens markedly within a day, though the "
            "background awareness of the gap can linger for weeks in "
            "important domains. The aftershock is envy's signature move: "
            "days later, a small reminder - their name in a meeting, a "
            "photo, a casual mention - re-fires the whole sequence in "
            "miniature. Aftershocks are weaker than the original peak but "
            "surprising, and people often mistake them for the feeling "
            "never having left. It did leave; it came back, because the "
            "appraisal is still installed. The practical reading of the "
            "pattern: do nothing irreversible at peak, expect fading with "
            "distance and absorption, and treat aftershocks as echoes to "
            "notice rather than emergencies to obey. Descriptive only - "
            "no real person is being described."
        ),
        "how_it_works": (
            "The time course follows the appraisal machinery. Onset is "
            "fast because social comparison is largely automatic - "
            "Festinger's process runs before conscious deliberation, and "
            "the pain signal Takahashi's team located in the anterior "
            "cingulate fires with the appraisal. The peak is a rumination "
            "effect: each replay of the comparison re-presents the gap to "
            "the appraisal system, refreshing the sting, which is why the "
            "first hour - dense with replay - feels worst. Fading is "
            "attention economics: the appraisal only fires when the "
            "comparison is active in working memory, so absorption in "
            "other demands starves it. Sleep helps because it breaks the "
            "replay chain. Aftershocks are cue-triggered reactivation - "
            "the appraisal pattern is learned and stored, so a reminder "
            "cue re-runs a compressed version of the original sequence. "
            "This is standard associative learning applied to emotion, "
            "and it explains why envy about a major domain (career, "
            "fertility, status) can echo for months while envy about a "
            "trivial domain vanishes by dinner. The lever at every phase "
            "is the same: starve the replay, feed absorption."
        ),
        "key_points": [
            "Onset is fast (under a minute); the comparison fires before deliberate thought.",
            "Peak comes in the first hour, dense with replay - the riskiest window for regretted words.",
            "Fading follows attention: absorption and sleep starve the comparison loop.",
            "Aftershocks are cue-triggered echoes, weaker than the peak but surprising.",
            "The lever at every phase: starve the replay, feed absorption.",
        ],
        "requirements": [
            "Four named phases - onset, peak, fading, aftershock - each with timing and texture.",
            "The peak identified as the highest-risk window for regretted actions.",
            "Aftershocks explained as echoes, not evidence the feeling never left.",
            "A practical reading of the pattern for each phase.",
            "A stated educational boundary: description only, never diagnosis of any real person.",
        ],
        "standards": [
            "Automatic onset follows Festinger 1954: comparison precedes deliberation.",
            "Pain-signal timing follows Takahashi et al. 2009.",
            "Replay-driven peak follows the rumination literature consistent with Scherer 2005 component re-appraisal.",
        ],
        "citations": [CIT_FESTINGER, CIT_TAKAHASHI, CIT_SCHERER, CIT_LAZARUS],
        "sig_lens": SIG_LENS_FEEL,
    },
    {
        "key": "low_vs_high",
        "name": "Low-Intensity vs High-Intensity Envy: Two Lived Snapshots",
        "group": "How It Feels",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "Low-intensity envy, the twinge. You are scrolling in a "
            "waiting room and a former classmate posts about a book deal. "
            "A small cool draft passes through your chest - 'huh, good "
            "for her' - with a thin undertow of 'I wanted that.' You "
            "notice the undertow the way you notice a draft: briefly, "
            "without alarm. Your thumb keeps scrolling. By the time your "
            "name is called, the feeling is gone, leaving at most a faint "
            "resolve to write more this month. Nothing in your behavior "
            "changes; nobody could tell; you barely tell yourself. "
            "High-intensity envy, the storm. Your closest colleague - "
            "same role, same start date - gets the promotion you both "
            "went for, and the news lands like a physical blow. Your "
            "stomach turns; your face arranges itself into congratulations "
            "while your hands feel cold. For days the comparison runs on "
            "a loop: every meeting is measured, every email re-read for "
            "signs of favoritism, sleep comes late and thin. You catch "
            "yourself hoping their first big project stumbles - and the "
            "hope shames you, which makes the loop louder. Ordinary "
            "pleasures go flat; the promotion poisons the week. The "
            "difference between the snapshots is not the kind of feeling "
            "but the volume, and the volume is set by the stakes: the "
            "book deal touched a mild wish, the promotion touched "
            "identity, livelihood, and daily proximity to the comparison. "
            "Both snapshots are simulations for education. They describe "
            "no real person and diagnose no one."
        ),
        "how_it_works": (
            "The two snapshots run the same appraisal with different "
            "inputs. In Scherer's component terms: the book-deal "
            "appraisal scores low on goal relevance (a mild wish, not "
            "identity) and high on the other's deservedness, so the "
            "pain signal is small and the action tendency points benignly "
            "at 'write more.' The promotion appraisal scores maximally "
            "on goal relevance (career identity, income, status), maximally "
            "on similarity (same role, same start date - the perfect "
            "comparison target per Festinger), and low on perceived "
            "control, so the pain signal is large and sustained, and the "
            "hostile fork opens because the advantage feels both "
            "unbearable and unchangeable. Proximity multiplies everything: "
            "the colleague is seen daily, so the comparison re-fires on "
            "schedule, while the classmate is seen rarely, so the loop "
            "starves. Smith and Kim's inferiority-plus-ill-will formula "
            "maps exactly: the twinge is inferiority without ill will "
            "(closer to admiration), the storm is inferiority fused with "
            "ill will (full malicious envy). The practical moral: volume "
            "is information about stakes, and the storm deserves the "
            "cooling tools while the twinge deserves only a nod."
        ),
        "key_points": [
            "The twinge: brief, cool, self-resolving - inferiority without ill will.",
            "The storm: looping, physical, sleep-disrupting - inferiority fused with ill will.",
            "Volume is set by stakes: goal relevance, similarity, deservedness, control, proximity.",
            "Daily proximity to the envied person multiplies the loop.",
            "The storm deserves cooling tools; the twinge deserves only a nod.",
        ],
        "requirements": [
            "Two concrete lived snapshots, one low and one high intensity.",
            "The same emotion shown running at both volumes.",
            "The appraisal ingredients that differ between the snapshots, stated plainly.",
            "Proximity named as a multiplier.",
            "A stated simulation boundary: describes no real person, diagnoses no one.",
        ],
        "standards": [
            "Appraisal ingredients follow Scherer 2005: relevance, control, and deservedness set intensity.",
            "Comparison-target similarity follows Festinger 1954.",
            "Inferiority-plus-ill-will formula follows Smith and Kim 2007.",
        ],
        "citations": [CIT_SCHERER, CIT_FESTINGER, CIT_SMITHKIM, CIT_VENDEVEN],
        "sig_lens": SIG_LENS_FEEL,
    },
    {
        "key": "partner_mix",
        "name": "Envy Mixed with Its Most Common Partner: Resentment",
        "group": "How It Feels",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "Envy rarely travels alone, and its most faithful companion "
            "is resentment - the sense that the gap is not just painful "
            "but unfair. Pure envy says 'you have what I want'; envy "
            "mixed with resentment says 'you have what I want and you "
            "should not have it, or I should have it instead.' The blend "
            "feels different from either ingredient: the ache of envy "
            "plus the heat of grievance, longing fused with a sense of "
            "injustice. It often arrives when the envied advantage looks "
            "undeserved - the promotion that seemed political, the "
            "inheritance that seemed unearned, the attention that seemed "
            "bought rather than earned. The resentment does real work in "
            "the blend: it converts the pain of inferiority into the "
            "energy of grievance, which feels more powerful and more "
            "justified than plain longing. That is why the blend is "
            "sticky - grievance gives the mind a story with a villain, "
            "and stories with villains are easier to replay than bare "
            "facts about gaps. The blend also licenses the hostile fork: "
            "plain envy might motivate self-improvement, but "
            "envy-plus-resentment motivates leveling the other person "
            "down, because the advantage now reads as an injustice to "
            "correct. Untangling the two is the practical skill: ask "
            "which part is the gap (envy) and which part is the fairness "
            "story (resentment), because the gap is handled with plans "
            "and the story is handled with evidence. Descriptive only - "
            "no real person is being described."
        ),
        "how_it_works": (
            "The blend forms at the appraisal level. Envy's appraisal "
            "(upward comparison, self-relevant gap) combines with "
            "resentment's appraisal (a norm violation: someone got what "
            "they did not deserve, or I was denied what I deserved). "
            "Scherer's components show the merge point: the 'deservedness' "
            "check, when it comes back negative, injects anger-like "
            "activation into the sadness-like pain of envy - the classic "
            "Plutchik-style dyad of a low, aching emotion fused with a "
            "hot, approaching one. Van de Ven's fork explains the "
            "behavioral consequence: perceived undeservedness is the "
            "switch that routes envy down the malicious path, toward "
            "pulling the other down rather than lifting the self up. The "
            "stickiness is a memory effect: grievance narratives are "
            "elaborated, rehearsed, and socially shareable ('let me tell "
            "you what they did'), so the blend gets more rehearsal than "
            "plain envy and therefore more staying power. Untangling "
            "works because the two appraisals answer to different "
            "evidence: the gap is a fact about positions, the fairness "
            "story is an interpretation - and interpretations can be "
            "audited."
        ),
        "key_points": [
            "Resentment is envy's most common partner: the gap plus a story about unfairness.",
            "The blend feels like ache fused with heat - longing plus grievance.",
            "Grievance narratives are sticky: stories with villains replay more easily than bare gaps.",
            "Perceived undeservedness is the switch that routes envy down the malicious fork.",
            "Untangling skill: the gap gets a plan, the fairness story gets an evidence audit.",
        ],
        "requirements": [
            "The blend named and distinguished from pure envy.",
            "The felt texture of the blend rendered concretely.",
            "The undeservedness switch identified as the fork mechanism.",
            "The stickiness of grievance narratives explained.",
            "The untangling skill stated as a practical move.",
        ],
        "standards": [
            "Dyad framing follows Plutchik 1980: complex emotions as blends of primaries.",
            "Undeservedness switch follows van de Ven, Zeelenberg and Pieters 2009.",
            "Component merge follows Scherer 2005: the deservedness check injects activation.",
        ],
        "citations": [CIT_PLUTCHIK, CIT_VENDEVEN, CIT_SCHERER, CIT_SMITHKIM],
        "sig_lens": SIG_LENS_FEEL,
    },
    {
        "key": "day_in_life",
        "name": "A Day in the Life: Envy Running Through an Ordinary Day",
        "group": "How It Feels",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "Morning. The alarm, the coffee, the phone - and there it is "
            "in the feed: a friend's kitchen renovation, marble and "
            "light, captioned with joy. A small cold coin drops in your "
            "stomach. Your own kitchen, fine yesterday, suddenly looks "
            "tired. You put the phone down a little harder than needed. "
            "Mid-morning. At work, a teammate mentions a bonus figure "
            "in passing - not bragging, just talking. The number lodges "
            "in your head like a splinter. Your own recent raise, which "
            "felt good last week, gets silently re-measured and found "
            "smaller. You are a fraction slower at your tasks, a fraction "
            "shorter in replies. Lunch. A sibling calls with good news - "
            "a clean bill of health, a trip booked. You feel the split "
            "screen: genuine warmth on one side, a gray film on the "
            "other, because their ease highlights your own stuck places. "
            "You steer the conversation to practical details to avoid the "
            "feeling. Afternoon. In a meeting, someone praises a "
            "colleague's project - a project adjacent to yours. Your "
            "praise, when your turn comes, is correct and slightly too "
            "brief, and you hear the brevity yourself. Evening. Cooking "
            "in the tired kitchen, the day's comparisons queue up for "
            "review: the marble, the bonus, the trip, the praise. None "
            "of them ruined the day - the day was objectively fine - and "
            "yet the day feels thinner than it was, as if the "
            "comparisons took a tax off everything. Night. In bed, the "
            "loop tries to start once more, and you notice it starting - "
            "which is the whole skill, really: noticing. The day was "
            "never about marble or bonuses. It was about the measuring, "
            "running quietly underneath an ordinary day. This vignette is "
            "a simulation for education. It describes no real person and "
            "diagnoses no one."
        ),
        "how_it_works": (
            "The vignette shows envy as a background process rather than "
            "an event. Each episode is a micro-appraisal: feed image, "
            "bonus mention, sibling's news, colleague's praise - each "
            "fires Festinger's comparison automatically, each measures a "
            "gap in a self-relevant domain (home, money, ease, status), "
            "each deposits a small pain signal of the kind Takahashi's "
            "team imaged. No single episode is intense; the effect is "
            "cumulative, a tax rather than a theft. The 'thinning' of the "
            "day is attention economics: working memory spent on "
            "comparison is unavailable for savoring, so objectively fine "
            "experiences register as flat. The split-screen feeling with "
            "the sibling shows the blend structure - warmth and envy are "
            "not opposites but co-occurring appraisals, one about the "
            "other's welfare, one about the self's position. The "
            "shortened praise in the meeting is the behavioral leak: "
            "felt envy constraining generous action at the margin. And "
            "the night-time noticing is metacognition - the appraisal "
            "system observing itself - which is the entry point for "
            "every healthy-expression technique in the later records. "
            "The day demonstrates that envy is usually weather, not "
            "climate: it passes through and taxes, but it need not "
            "govern."
        ),
        "key_points": [
            "Envy usually runs as a background process of micro-comparisons, not one big event.",
            "The effect is cumulative: a tax on the day rather than a theft.",
            "Comparison spends working memory, which flattens savoring of fine experiences.",
            "Warmth and envy can co-occur as a split screen - they are not opposites.",
            "Night-time noticing (metacognition) is the entry point for all healthy handling.",
        ],
        "requirements": [
            "A full ordinary day rendered in scenes from morning to night.",
            "At least four distinct micro-trigger episodes across different domains.",
            "The cumulative 'tax' effect shown, not just single episodes.",
            "The split-screen co-occurrence of warmth and envy included.",
            "A stated simulation boundary: describes no real person, diagnoses no one.",
        ],
        "standards": [
            "Micro-appraisal structure follows Lazarus 1991 and Scherer 2005.",
            "Automatic comparison follows Festinger 1954.",
            "Pain-signal accumulation follows Takahashi et al. 2009.",
        ],
        "citations": [CIT_LAZARUS, CIT_SCHERER, CIT_FESTINGER, CIT_TAKAHASHI],
        "sig_lens": SIG_LENS_FEEL,
    },
]
ENTRIES += [
    # ------------------------------------------------ 10-13 BODY SIGNALS
    {
        "key": "body",
        "name": "What Envy Does in the Body",
        "group": "Body Signals",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Envy is a full-body event, not just a thought. The heart "
            "often quickens slightly or beats with a heavy, uneven "
            "quality - not the pounding of fear, but a dense, weighted "
            "pulse, as if the circulation has taken on the mood. "
            "Breathing tends to go shallow and a little fast, the chest "
            "feeling tight or constricted, as though the ribs have drawn "
            "in by a notch. The stomach is envy's favored address: a "
            "sinking, gnawing, or sour sensation - the 'pit' feeling - "
            "shows up so reliably that languages everywhere put envy in "
            "the gut. Muscles carry it as tension, especially in the jaw "
            "(teeth pressed or grinding), the shoulders (lifted and "
            "locked), and the hands (fists half-formed, or fingers "
            "drumming). The skin may flush in the face and neck when the "
            "resentful heat joins, or go cool and pale when the inferior "
            "ache dominates. Energy does something characteristic: a "
            "restless, buzzing agitation combined with heaviness, the "
            "body wanting to move and wanting to sink at once - pacing "
            "thoughts in a leaden frame. None of this is dramatic enough "
            "to announce itself; envy's body signature is quiet, which "
            "is why people can feel it for hours without naming it. "
            "Noticing the jaw, the gut, and the breath is often how the "
            "feeling gets recognized at all. Descriptive only - this "
            "describes the emotion's typical body patterns, never any "
            "real person's medical state."
        ),
        "how_it_works": (
            "The body pattern follows the appraisal. Upward comparison "
            "with a self-relevant gap activates the same threat-and-pain "
            "circuitry that Takahashi's team found for envy in the "
            "anterior cingulate and insula - regions that also process "
            "physical discomfort, which is why the gut and chest feel "
            "involved rather than just the head. Sympathetic arousal "
            "raises heart rate and tightens muscles (jaw, shoulders) as "
            "part of the action preparation Frijda described: the body "
            "readies for the leveling urge, whether benign (chase) or "
            "malicious (undermine). The stomach's starring role likely "
            "reflects the gut-brain axis under stress arousal - "
            "digestion slows, acid shifts, and interoceptive attention "
            "zooms in, a loop Barrett's construction account predicts: "
            "the brain reads the body's budget disruption and labels the "
            "whole pattern 'envy' when the social-comparison concept is "
            "active. The restless-heavy combination is the blend showing "
            "in the body: agitation from the hostile/approach component, "
            "heaviness from the inferiority/withdrawal component. Because "
            "the signature is quiet, it is easy to misattribute - people "
            "read envy's body as hunger, fatigue, or a bad mood, which is "
            "why the recognition records teach checking the jaw, gut, "
            "and breath first."
        ),
        "key_points": [
            "Heart: quickened or heavy uneven pulse; breath: shallow, fast, tight chest.",
            "The stomach is envy's favored address - the sinking 'pit' feeling.",
            "Tension lodges in jaw, shoulders, and hands.",
            "Energy is restless-heavy: buzzing agitation in a leaden frame.",
            "The signature is quiet - often misread as hunger, fatigue, or bad mood.",
        ],
        "requirements": [
            "Coverage of heart, breath, stomach, muscles, skin, and energy.",
            "The gut emphasized as the characteristic address.",
            "The restless-heavy combination named as the blend in the body.",
            "The quietness of the signature and its misattribution noted.",
            "A stated boundary: describes typical patterns, never any real person's medical state.",
        ],
        "standards": [
            "Pain-circuit involvement follows Takahashi et al. 2009: anterior cingulate and insula.",
            "Action preparation follows Frijda 1986: the body readies for the leveling urge.",
            "Interoceptive labeling follows Barrett 2017: the brain constructs the emotion from body signals plus concepts.",
        ],
        "citations": [CIT_TAKAHASHI, CIT_FRIJDA, CIT_BARRETT, CIT_SCHERER],
        "sig_lens": SIG_LENS_BODY,
    },
    {
        "key": "posture",
        "name": "Posture and Movement: How the Body Carries Envy",
        "group": "Body Signals",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Envy has a posture, and it is the posture of someone trying "
            "not to show a feeling while the feeling pulls at the frame. "
            "The shoulders tend to round forward and lift slightly, the "
            "chest narrowing as if to take up less space - the body of "
            "inferiority made visible. The head often tilts down or turns "
            "a fraction away from the envied person, while the eyes do "
            "the opposite: quick, darting glances toward the envied "
            "object or person, then away, then back - the gaze of "
            "measuring. Darwin noted this watching-and-withdrawing "
            "combination in his 1872 work on expression: attention "
            "pulled toward the stimulus while the body angles away from "
            "it. Movement under envy is restless but contained: shifting "
            "weight, re-crossing legs, adjusting objects on a table, "
            "small self-touching gestures (neck, forearm, face) that "
            "soothe without being noticed. When the resentful heat is "
            "stronger, the posture sharpens - chin lifts, movements get "
            "clipped and abrupt, the body angles toward confrontation "
            "rather than away. Walking pace often quickens slightly, as "
            "if the body wants to leave the comparison scene. In groups, "
            "the envious posture reads as 'present but withdrawn': in "
            "the chair, in the conversation, but leaning out of it by "
            "degrees. Actors and artists take note: envy is played in "
            "the contradiction - the body retreating while the eyes keep "
            "returning. Descriptive only - posture patterns of the "
            "emotion, never a reading of any real person."
        ),
        "how_it_works": (
            "Posture under envy expresses the two competing action "
            "tendencies Frijda mapped. The inferiority component urges "
            "withdrawal and submission - smaller profile, averted head, "
            "rounded shoulders - the ancient appeasement geometry. The "
            "hostile component urges approach and engagement - the "
            "measuring gaze, the sharpened chin, the clipped movement. "
            "Both run at once, so the body compromises: retreat in the "
            "torso, approach in the eyes. The self-touching gestures are "
            "self-regulation in motion - the nervous system discharging "
            "arousal through small, deniable movements, exactly the kind "
            "of leakage Ekman and Friesen's FACS tradition taught "
            "observers to watch for. Gaze behavior is the most reliable "
            "channel because attention is hard to fake: the comparison "
            "appraisal demands visual data (how good is their thing, "
            "really?), so the eyes keep returning to the stimulus even "
            "while social display rules order them away. The quickened "
            "walking pace is avoidance locomotion - the body voting to "
            "exit the comparison field. Reading posture therefore means "
            "reading contradiction: wherever retreat and return appear "
            "together, envy is a candidate explanation - one candidate "
            "among several, never a conclusion about a person."
        ),
        "key_points": [
            "The signature posture: torso retreating while the eyes keep returning.",
            "Inferiority shrinks the frame (rounded shoulders, lowered head); hostility sharpens it.",
            "Movement is restless but contained: shifting, adjusting, self-touching.",
            "Gaze is the most reliable channel - attention is hard to fake.",
            "Read contradiction: retreat plus return together suggests envy as one candidate.",
        ],
        "requirements": [
            "Posture, gaze, and movement each described with the envy-specific pattern.",
            "The retreat-vs-return contradiction named as the core signature.",
            "The inferiority and hostile components mapped to different body channels.",
            "The actor/artist note on playing the contradiction.",
            "A stated boundary: patterns of the emotion, never a reading of any real person.",
        ],
        "standards": [
            "Expression observation follows Darwin 1872: attention toward the stimulus with bodily withdrawal.",
            "Competing action tendencies follow Frijda 1986.",
            "Leakage framing follows Ekman and Friesen FACS 1978: arousal discharges through small movements.",
        ],
        "citations": [CIT_DARWIN, CIT_FRIJDA, CIT_FACS, CIT_SMITHKIM],
        "sig_lens": SIG_LENS_BODY,
    },
    {
        "key": "sleep_appetite",
        "name": "Sleep, Appetite, and Energy Under Envy",
        "group": "Body Signals",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Sustained envy - the settled, looping kind - reaches into "
            "the body's maintenance systems. Sleep is usually the first "
            "to show it: difficulty falling asleep because the comparison "
            "loop replays in the dark, where there is nothing to compete "
            "with it for attention; lighter, more broken sleep; waking "
            "with the envied thought already queued, as if it slept in "
            "the next room. Appetite tends to split by person: some lose "
            "it - the gut-pit feeling suppresses hunger, food looks "
            "uninteresting, meals get skipped or pushed around the plate "
            "- while others eat for soothing, reaching for rich, quick "
            "comfort foods in the evening when the day's comparisons get "
            "reviewed. Energy follows the restless-heavy pattern into the "
            "day: mornings feel leaden and slow to start, afternoons "
            "buzz with agitated replays, and by evening there is a "
            "drained, wrung-out fatigue that rest does not quite fix "
            "because the drain is attentional, not muscular. None of "
            "this is dramatic at low volumes - a twinge of envy does not "
            "touch sleep - which is itself diagnostic information: when "
            "sleep, appetite, and energy all shift together, the envy has "
            "moved from passing weather to settled climate, and the "
            "cooling tools in the healthy-expression records become "
            "relevant. These are general educational patterns. They are "
            "not medical advice and describe no real person's health."
        ),
        "how_it_works": (
            "The mechanism is sustained arousal plus attentional capture. "
            "The comparison loop keeps the sympathetic system mildly "
            "activated - elevated enough to delay sleep onset and fragment "
            "sleep architecture, not enough to feel like an emergency. "
            "In the dark, with external demands gone, the loop gets "
            "monopoly time in working memory, which is why bedtime is "
            "envy's favorite replay hour. Appetite effects run through "
            "the gut-brain axis under this low-grade arousal: the "
            "sinking-pit sensation directly suppresses hunger signals in "
            "some people, while in others the same arousal drives "
            "soothing-seeking behavior toward calorie-dense food - the "
            "split reflects individual regulation styles, consistent "
            "with Barrett's point that bodies construct emotion "
            "differently from the same ingredients. The unfixable-by-rest "
            "fatigue is attentional depletion: hours of comparison and "
            "counterfactual replay consume the same executive resources "
            "as hard mental work, so the person is genuinely tired - "
            "tired from thinking, not from doing. This is why the "
            "practical fix is rarely 'rest more' and usually 'replay "
            "less': absorption in demanding, valued activity restores "
            "energy faster than a nap, because it starves the loop that "
            "is spending the budget."
        ),
        "key_points": [
            "Sleep: delayed onset and broken sleep from bedtime replay; waking with the thought queued.",
            "Appetite splits: suppressed by the gut-pit in some, comfort-seeking in others.",
            "Energy: leaden mornings, buzzing afternoons, drained evenings.",
            "The fatigue is attentional - rest alone does not fix it; starving the loop does.",
            "All three shifting together signals envy has moved from weather to climate.",
        ],
        "requirements": [
            "Sleep, appetite, and energy each covered with the envy-specific pattern.",
            "The appetite split (suppressed vs soothing) included.",
            "The attentional nature of the fatigue explained.",
            "The weather-to-climate signal named as practical information.",
            "A stated boundary: general patterns, not medical advice, describing no real person.",
        ],
        "standards": [
            "Arousal-sleep link follows the standard psychophysiology consistent with Scherer 2005 component model.",
            "Individual regulation differences follow Barrett 2017: same ingredients, different constructions.",
            "Attentional depletion framing follows the executive-resource account consistent with Lazarus 1991 coping theory.",
        ],
        "citations": [CIT_SCHERER, CIT_BARRETT, CIT_LAZARUS, CIT_TAKAHASHI],
        "sig_lens": SIG_LENS_BODY,
    },
    {
        "key": "individual_diffs",
        "name": "How Envy's Body Signals Differ Between People",
        "group": "Body Signals",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "No two bodies run envy the same way, and expecting one "
            "uniform signature is the fastest route to misreading. Some "
            "people feel envy almost entirely in the gut - the pit, the "
            "sourness, the appetite shift - with barely a ripple "
            "elsewhere. Others feel it in the chest and throat: "
            "tightness, a lump, heat rising up the neck. Some go cold - "
            "pale, still, quiet, the freeze variant - while others go "
            "hot and restless, pacing and fidgeting. The expressive "
            "channel varies too: one person's envy leaks through the "
            "jaw, another's through the eyes, a third's through clipped "
            "speech, and a fourth shows almost nothing anywhere - the "
            "high self-monitors who have trained every channel to stay "
            "neutral. Culture and upbringing tune the instrument: in "
            "settings where envy is deeply shamed, the body learns to "
            "suppress earlier and harder, so the signals go subtler and "
            "more internal; where emotional expression is freer, the "
            "signals run more visible. Age matters as well - younger "
            "people often feel envy more physically and show it more, "
            "while older adults, with more practiced regulation, tend "
            "toward the quieter internal variants. The practical point "
            "is humility: body signals are clues about the emotion in "
            "general, never a decoder ring for a specific person. Two "
            "people can feel equally strong envy with completely "
            "different bodies, and the same tight jaw can mean envy in "
            "one person and a deadline in another. Descriptive only - "
            "patterns across people, never a reading of any individual."
        ),
        "how_it_works": (
            "The variation comes from three sources. First, "
            "interoceptive style: Barrett's work shows people differ in "
            "how finely they sense internal body signals, so the same "
            "arousal pattern gets labeled 'gut-pit' by a fine-grained "
            "sensor and 'just tense' by a coarse one. Second, regulation "
            "habits: chronic suppressors route the signal inward (more "
            "gut, more chest, less face), while expressers let it show "
            "in the channels they habitually use. Third, display rules "
            "learned across a lifetime: Ekman's research on cultural "
            "display rules found that the rules for concealing negative "
            "emotion differ across settings, and envy - among the most "
            "concealed emotions - is where display rules bite hardest. "
            "The freeze-vs-fidget split reflects the two classic stress "
            "responses playing out under the comparison appraisal: "
            "withdrawal-dominant bodies go still and cold, "
            "approach-dominant bodies go hot and restless. None of this "
            "makes body reading useless - it makes it probabilistic. "
            "The honest use of body knowledge is as a hypothesis "
            "generator ('envy is one candidate for this pattern') paired "
            "with context ('and the context includes a fresh upward "
            "comparison'), never as a verdict."
        ),
        "key_points": [
            "The address varies: gut people, chest-and-throat people, cold-freeze people, hot-restless people.",
            "The leakiest channel varies: jaw, eyes, speech, or nearly nothing in high self-monitors.",
            "Culture, upbringing, and age tune how visible the signals run.",
            "The same tight jaw can mean envy in one person and a deadline in another.",
            "Body signals are hypothesis generators, never verdicts about a person.",
        ],
        "requirements": [
            "At least four distinct bodily styles of envy described.",
            "Channel variation (where it leaks) covered separately from intensity variation.",
            "Culture, upbringing, and age named as tuners.",
            "The probabilistic, hypothesis-not-verdict framing stated explicitly.",
            "A stated boundary: patterns across people, never a reading of any individual.",
        ],
        "standards": [
            "Interoceptive variation follows Barrett 2017: people construct emotion from body signals differently.",
            "Display-rule variation follows Ekman and Friesen's display-rule research tradition (FACS 1978).",
            "Stress-response split follows the standard withdrawal/approach framing consistent with Frijda 1986.",
        ],
        "citations": [CIT_BARRETT, CIT_FACS, CIT_FRIJDA, CIT_SCHERER],
        "sig_lens": SIG_LENS_BODY,
    },
]
ENTRIES += [
    # ------------------------------------------------ 14-17 FACIAL EXPRESSION
    {
        "key": "face",
        "name": "The Face of Envy: Eyes, Brows, Mouth, and Micro-Signs",
        "group": "Facial Expression",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Here is the first thing to know: unlike joy or anger, envy "
            "has no single universal facial signature. Researchers have "
            "not found one face that means envy everywhere the way the "
            "smile means joy. What envy has instead is a family of "
            "tells - small, brief, often suppressed movements that "
            "cluster around the comparison moment. The eyes do the most "
            "talking: quick measuring glances toward the envied person "
            "or object, sometimes with a slight narrowing, and a "
            "tendency to look away just as the glance could be noticed. "
            "The brows often draw together and down a fraction - not the "
            "full frown of anger, but a tightening that reads as "
            "concentration shading into displeasure. The mouth is where "
            "the suppression shows: lips pressed together or rolled "
            "inward, the corners pulled tight or turned down a "
            "millimeter, and the notorious tight smile - the "
            "congratulations smile that engages the mouth but never "
            "reaches the eyes, the muscles around the eyes staying "
            "still while the lips perform gladness. Micro-signs flash "
            "and vanish in fractions of a second: a quick lip press, a "
            "one-sided tightening at the mouth corner, a brief nostril "
            "flare with the resentful heat, an eye-roll so small it "
            "barely counts. Darwin, in 1872, catalogued how the muscles "
            "of expression betray feelings people intend to hide, and "
            "envy is his case study in miniature: the face trying to "
            "perform one thing while the muscles report another. The "
            "honest summary: there is no envy face, only envy leaks - "
            "and leaks require context to read. Descriptive only - "
            "facial patterns of the emotion, never a reading of any real "
            "person's face."
        ),
        "how_it_works": (
            "The absence of a universal envy face is itself informative. "
            "Ekman's basic-emotion research found dedicated facial "
            "programs for emotions like joy, anger, and disgust; envy, "
            "a complex social-comparison emotion, never got its own "
            "program. Instead the face shows the components: the "
            "measuring gaze comes from the comparison appraisal demanding "
            "visual data; the brow tightening comes from the displeasure "
            "component; the lip press comes from suppression effort - "
            "the deliberate inhibition of expression, which in FACS terms "
            "recruits the orbicularis oris and mentalis in ways that "
            "read as tension. The tight congratulations smile is a "
            "display-rule performance: the zygomatic major pulls the lip "
            "corners (the social smile) without the orbicularis oculi "
            "activity that marks genuine gladness around the eyes - the "
            "Duchenne distinction, running in reverse as evidence of "
            "feeling management. Micro-signs are brief because "
            "suppression is fast: the genuine impulse fires, the control "
            "system catches it within a few hundred milliseconds, and "
            "only the onset or offset leaks. This is why reading envy "
            "from the face alone is unreliable - the same lip press can "
            "be concentration, the same averted gaze can be shyness - "
            "and why the recognition records insist on face plus body "
            "plus voice plus context, never face alone."
        ),
        "key_points": [
            "There is no universal envy face - only a family of tells and leaks.",
            "Eyes: measuring glances, slight narrowing, looking away before being noticed.",
            "Mouth: pressed lips, tight corners, the congratulations smile that never reaches the eyes.",
            "Micro-signs flash in fractions of a second as suppression catches the impulse.",
            "Face alone is unreliable - the same movements have innocent explanations.",
        ],
        "requirements": [
            "The no-universal-face fact stated up front and explained.",
            "Eyes, brows, and mouth each covered with envy-specific movements.",
            "The tight congratulations smile described with the eye-muscle distinction.",
            "Micro-signs characterized by their brevity and the suppression mechanism.",
            "A stated boundary: facial patterns of the emotion, never a reading of any real person's face.",
        ],
        "standards": [
            "No-dedicated-program claim follows Ekman 1999: envy is not among the basic emotions with distinct signals.",
            "Muscle description follows Ekman and Friesen FACS 1978: named muscle actions, not folk labels.",
            "Genuine-vs-performed smile distinction follows the Duchenne tradition via Ekman and Friesen.",
            "Suppression-leakage follows Darwin 1872 on expression under concealment.",
        ],
        "citations": [CIT_FACS, CIT_DARWIN, CIT_SMITHKIM, CIT_SCHERER],
        "sig_lens": SIG_LENS_FACE,
    },
    {
        "key": "face_intensity",
        "name": "How the Expression Changes with Intensity",
        "group": "Facial Expression",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The face of envy changes with the volume, and the change "
            "runs in an interesting direction: as envy intensifies, the "
            "face often shows less, not more. At mild intensity - the "
            "twinge - the face is relatively open: a brief flicker "
            "crosses it, a half-second of the measuring look or the lip "
            "press, and then it passes. The person may not even know it "
            "showed. Control is light because the stakes are light. At "
            "moderate intensity the performance begins: the person knows "
            "they feel it and starts managing the face deliberately. "
            "This is the territory of the tight congratulations smile, "
            "the over-bright 'that's amazing!' with eyes that stay flat, "
            "the laugh that arrives a beat late. The management itself "
            "becomes visible - the face looks worked, arranged, slightly "
            "too composed. Paradoxically, the harder the management, the "
            "more the micro-leaks stand out against the stillness: a "
            "frozen pleasant face with one quick jaw clench tells more "
            "than an animated one. At high intensity the face tends "
            "toward one of two poles: the mask - near-total stillness, "
            "pleasant and impenetrable, the person visibly spending "
            "effort on neutrality - or the break, where control slips "
            "and the underlying affect floods through as open "
            "displeasure, sarcasm, or the curled-lip contempt-adjacent "
            "look. The mask is more common in formal settings, the break "
            "more common in private ones. Actors note the gradient: "
            "mild envy plays in the flicker, moderate in the managed "
            "performance, intense in the mask-or-break. Descriptive "
            "only - expression patterns, never a reading of any real "
            "person's face."
        ),
        "how_it_works": (
            "The less-is-more gradient follows from display rules "
            "scaling with stakes. At low intensity the appraisal is weak, "
            "so the expressive impulse is weak and suppression is "
            "minimal - the flicker escapes simply because nobody is "
            "guarding. At moderate intensity the person detects their "
            "own feeling (metacognition) and recruits voluntary control, "
            "which in FACS terms means sustained inhibition of the lower "
            "face and deliberate activation of the social smile muscles. "
            "Sustained inhibition is physiologically costly and produces "
            "its own tells: the stillness looks effortful, and the "
            "contrast makes any leak salient - signal detection theory "
            "applied to faces. At high intensity the control system is "
            "either fully mobilized (the mask: maximum inhibition, "
            "minimum movement) or overwhelmed (the break: the hostile "
            "component's approach energy overrides inhibition). Which "
            "pole appears depends on setting formality and on the "
            "person's regulation capacity in the moment - fatigue, "
            "alcohol, and surprise all push toward the break. This is "
            "why the most intense envy is often the least readable in "
            "public and the most readable in private: the mask holds "
            "where the audience matters and drops where it doesn't."
        ),
        "key_points": [
            "Mild envy: the unguarded flicker - brief, open, often unnoticed.",
            "Moderate envy: the managed performance - tight smiles, worked pleasantness, visible effort.",
            "Intense envy: the mask (total stillness) or the break (control slips).",
            "Harder management makes micro-leaks stand out more against the stillness.",
            "The mask holds in public; the break happens in private.",
        ],
        "requirements": [
            "Three intensity bands with distinct facial patterns.",
            "The counterintuitive less-is-more gradient stated and explained.",
            "The mask-vs-break poles at high intensity distinguished by setting.",
            "The actor's note on playing each band.",
            "A stated boundary: expression patterns, never a reading of any real person's face.",
        ],
        "standards": [
            "Display-rule scaling follows the Ekman and Friesen tradition (FACS 1978).",
            "Inhibition cost and leak salience follow standard expressive-suppression psychophysiology.",
            "Setting-dependent control follows Lazarus 1991 coping as person-environment transaction.",
        ],
        "citations": [CIT_FACS, CIT_LAZARUS, CIT_SMITHKIM, CIT_DARWIN],
        "sig_lens": SIG_LENS_FACE,
    },
    {
        "key": "hiding_faking",
        "name": "Hiding Envy and Faking Gladness: What Leaks Through",
        "group": "Facial Expression",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Envy is the most hidden of the common emotions - people "
            "will admit to anger, fear, even jealousy before they admit "
            "to envy - so its concealment techniques are the most "
            "practiced. The standard kit: the quick redirect (change the "
            "subject, ask a question, create motion), the preemptive "
            "praise (compliment first, loudly, so no one suspects the "
            "feeling), the busy hands (phone, drink, task - anything to "
            "occupy the channels that would leak), and the exit (leave "
            "the comparison scene early with a plausible reason). Faking "
            "gladness has its own choreography: the too-fast "
            "congratulations, the superlative pile-up ('amazing, "
            "incredible, so deserved' - three adjectives where one would "
            "do), the overlong hug or handshake that performs warmth "
            "while the eyes stay flat. What leaks through despite all "
            "this: timing (the congratulations arrive half a beat late, "
            "or the praise rushes out too fast), symmetry (the smile "
            "pulls harder on one side), duration (the pleasant "
            "expression is held a fraction too long, past the natural "
            "decay), and the eyes (the one channel that resists "
            "choreography - flat, measuring, or quickly averted). Voice "
            "leaks too: pitch rises slightly with the effort of "
            "performing gladness, and the warmth in the tone doesn't "
            "match the words. The deepest leak is behavioral and comes "
            "later: the person who performed perfect gladness never "
            "follows up, never asks about the thing again, changes the "
            "subject whenever it surfaces. Concealment is a skill, and "
            "like all skills it has tells - the tell of concealment is "
            "usually effort itself. Descriptive only - techniques and "
            "leaks of the emotion, never a reading of any real person."
        ),
        "how_it_works": (
            "Concealment works by substituting voluntary displays for "
            "involuntary ones, and it fails at the seams Ekman mapped: "
            "voluntary control is good at the mouth and poor at the eyes, "
            "good at onset and poor at timing and duration. The "
            "too-fast congratulations is the control system overfiring - "
            "eagerness to establish the cover story. The superlative "
            "pile-up is verbal overcompensation, the speech equivalent "
            "of the too-wide smile. Timing leaks because genuine "
            "expressions have characteristic onset-offset envelopes "
            "(about half a second up, a few seconds down) while "
            "performed ones are held to script - the held-too-long "
            "pleasant face is the performer forgetting to let the "
            "expression decay naturally. The eyes resist choreography "
            "because the comparison appraisal keeps demanding visual "
            "data: attention pulls the gaze back to the envied stimulus "
            "even as the social script orders it away, producing the "
            "look-away-look-back pattern. The delayed behavioral leak "
            "(never following up) is avoidance conditioning: the topic "
            "has become a conditioned cue for the pain signal, so the "
            "person steers around it without deciding to. Knowing the "
            "kit matters less for catching others than for catching "
            "oneself: these are the moves people use on themselves, and "
            "recognizing one's own choreography is the first honest "
            "moment."
        ),
        "key_points": [
            "The concealment kit: redirect, preemptive praise, busy hands, early exit.",
            "The faking choreography: too-fast congratulations, superlative pile-up, overlong warmth.",
            "What leaks: timing, symmetry, held-too-long duration, and the eyes.",
            "Voice leaks: raised pitch and warmth that doesn't match the words.",
            "The deepest leak is delayed and behavioral: never following up on the envied thing.",
        ],
        "requirements": [
            "Named concealment techniques and named faking choreography.",
            "At least four leak channels: timing, symmetry, duration, eyes.",
            "Voice included as a leak channel.",
            "The delayed behavioral leak (avoidance of the topic) covered.",
            "A stated boundary: techniques and leaks of the emotion, never a reading of any real person.",
        ],
        "standards": [
            "Seam analysis follows Ekman and Friesen FACS 1978: voluntary vs involuntary control across channels.",
            "Expression timing envelopes follow the Ekman timing literature.",
            "Avoidance conditioning follows standard learning theory consistent with Lazarus 1991.",
        ],
        "citations": [CIT_FACS, CIT_LAZARUS, CIT_SMITHKIM, CIT_BARRETT],
        "sig_lens": SIG_LENS_FACE,
    },
    {
        "key": "expression_gallery",
        "name": "Expression Gallery Notes: Drawing and Playing Envy",
        "group": "Facial Expression",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "These are working notes for artists, actors, animators, and "
            "writers who need to render envy without a single universal "
            "face to copy. Note one - the measuring look: eyes narrowed "
            "a fraction, head very slightly tilted, gaze fixed on the "
            "envied object while the body angles away. Draw the "
            "contradiction: attention toward, torso away. Note two - the "
            "tight congratulations: mouth corners pulled in a smile that "
            "stops at the mouth, eyes calm and uncreased, the stillness "
            "around the eyes doing the real talking. The key detail is "
            "negative space: draw what is absent (no crow's-feet, no "
            "cheek lift) rather than what is present. Note three - the "
            "suppressed flash: for animation, a six-frame sequence - "
            "neutral, then a two-frame tightening (brows down a "
            "millimeter, lips press), then back to neutral with the "
            "pleasant mask settling over it. The audience reads the "
            "two-frame tightening as the truth and the mask as the lie. "
            "Note four - the resentful heat variant: nostrils slightly "
            "flared, jaw set, chin lifted a degree, the look held a "
            "beat too long. This is envy with the hostile fork open - "
            "closer to contempt's territory, and the artist should know "
            "the difference: contempt looks down, envy looks across "
            "while feeling below. Note five - hands and posture as "
            "backup singers: the self-touch at the neck, the object "
            "adjusted on the table, the weight shifted away. Faces lie "
            "best when the body is allowed to tell the truth, so give "
            "the body one honest gesture per scene. Note six - for "
            "writers: envy is best shown through behavior, not labels. "
            "Never write 'she felt envious'; write the congratulations "
            "that came too fast, the subject changed, the question about "
            "the thing never asked again. These notes describe the "
            "emotion's rendering, never any real person."
        ),
        "how_it_works": (
            "The gallery method works because audiences read emotion the "
            "way the appraisal system writes it: in components, not "
            "labels. The measuring look works because viewers "
            "instinctively parse the attention-toward/torso-away "
            "contradiction as conflicted desire - the visual system is "
            "tuned to gaze direction as an intention signal. The "
            "tight-congratulations note exploits the Duchenne "
            "distinction that audiences know intuitively: everyone has "
            "seen a smile that didn't reach the eyes, so the negative "
            "space around the eyes reads as managed feeling without any "
            "explanation needed. The six-frame suppressed flash works on "
            "the timing of real micro-expressions - genuine leakage lasts "
            "a fraction of a second before control reasserts, and "
            "animating that exact rhythm triggers recognition. The "
            "contempt-vs-envy distinction matters because the two share "
            "the tight mouth but differ in the eyes and the head angle: "
            "contempt's unilateral tightening plus downward angle reads "
            "as superiority, while envy's bilateral tension plus level "
            "gaze reads as pained comparison. The writer's note follows "
            "the oldest rule in the craft: behavioral evidence "
            "('show the congratulations arriving too fast') outperforms "
            "labels ('she was envious') because readers run their own "
            "appraisal simulation on behavior and arrive at the emotion "
            "themselves - which is exactly what this whole database is "
            "built to teach."
        ),
        "key_points": [
            "No single face to copy - render the components: measuring look, tight congratulations, suppressed flash.",
            "Draw the contradiction: attention toward, torso away.",
            "Use negative space: the absence of eye-crease sells the managed smile.",
            "Contempt looks down; envy looks across while feeling below.",
            "For writers: show behavior (too-fast congratulations, changed subjects), never labels.",
        ],
        "requirements": [
            "At least five numbered working notes for visual rendering.",
            "The attention-toward/torso-away contradiction as the core composition.",
            "The contempt-vs-envy distinction for artists.",
            "The six-frame suppressed-flash animation note.",
            "The writer's show-don't-label rule with concrete examples.",
        ],
        "standards": [
            "Component rendering follows Ekman and Friesen FACS 1978: build expressions from muscle actions.",
            "Gaze-as-intention follows the social-attention literature consistent with Darwin 1872.",
            "Micro-expression timing follows the Ekman leakage-timing tradition.",
        ],
        "citations": [CIT_FACS, CIT_DARWIN, CIT_SMITHKIM, CIT_BARRETT],
        "sig_lens": SIG_LENS_FACE,
    },
]
ENTRIES += [
    # ------------------------------------------------ 18-21 TRIGGERS
    {
        "key": "classic_triggers",
        "name": "The Classic Triggers: What Commonly Sets Envy Off",
        "group": "Triggers",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Certain situations set off envy so reliably they might as "
            "well be labeled. The promotion or award given to a peer - "
            "especially a peer who started at the same time - is the "
            "textbook trigger: same track, visible divergence, "
            "self-relevant domain. Possessions on display: the new car "
            "in the driveway, the renovation, the watch, the vacation "
            "photos - anything visible, comparable, and slightly out of "
            "reach. Romantic and social goods: the engagement "
            "announcement, the crowded party photos, the effortless "
            "popularity - triggers that bite because belonging is a core "
            "domain. Bodily and talent goods: the athletic body, the "
            "musical gift, the quick mind - envied because they feel "
            "fixed and unearned-by-effort, which makes the gap feel "
            "uncloseable. Recognition goods: praise, followers, awards, "
            "being chosen - the most volatile trigger of all, because "
            "recognition is zero-sum in the moment it is given to "
            "someone else. Words that trigger: direct comparisons "
            "('why can't you be more like...'), highlight-reel "
            "storytelling, humble-bragging, and the innocent question "
            "'how's your job search going?' asked at the wrong time. "
            "Events that trigger: reunions, weddings, award ceremonies, "
            "feed scrolling - any scene engineered to display "
            "comparable goods side by side. The pattern across all of "
            "them: visibility plus comparability plus self-relevance. "
            "Remove any one of the three and the trigger misfires - an "
            "invisible advantage can't be compared, an incomparable one "
            "can't be measured, an irrelevant one doesn't sting. "
            "Descriptive only - trigger patterns, never a reading of any "
            "real person."
        ),
        "how_it_works": (
            "Classic triggers are just efficient appraisal packages. "
            "Festinger's theory predicts each element: visibility "
            "supplies the comparison data, comparability (similar other, "
            "similar domain) makes the comparison self-relevant, and "
            "self-relevance routes it to the pain circuitry Takahashi "
            "imaged. Peer promotions are the perfect storm because they "
            "maximize all three at once - the other is maximally similar "
            "(same role, same cohort), the good is maximally visible "
            "(announced), and the domain is maximally self-relevant "
            "(career identity). Recognition goods are volatile because "
            "they are positional: praise given to one person in a "
            "meeting is implicitly not given to the others, which the "
            "appraisal system reads as a ranking event. Talent and body "
            "goods bite through perceived uncloseability - when the gap "
            "looks fixed, the benign fork (self-improvement) closes and "
            "only the malicious fork (resentment) stays open, which is "
            "why these triggers produce the most bitter envy. The "
            "three-factor formula is also the practical defense: you "
            "cannot always avoid visible goods, but you can break "
            "comparability (their track is not your track) or "
            "self-relevance (this domain is not my scoreboard) - and "
            "breaking one factor disarms the trigger."
        ),
        "key_points": [
            "The trigger formula: visibility plus comparability plus self-relevance.",
            "Peer promotions are the perfect storm - maximally similar other, visible good, relevant domain.",
            "Recognition goods are volatile because they read as ranking events.",
            "Talent and body goods bite through perceived uncloseability.",
            "Breaking any one factor disarms the trigger.",
        ],
        "requirements": [
            "Named trigger categories: career, possessions, romantic/social, body/talent, recognition.",
            "Triggering words and triggering events listed concretely.",
            "The three-factor formula stated and applied.",
            "The uncloseability mechanism for talent/body triggers explained.",
            "A stated boundary: trigger patterns, never a reading of any real person.",
        ],
        "standards": [
            "Comparison mechanics follow Festinger 1954.",
            "Pain routing follows Takahashi et al. 2009.",
            "Fork-closing by uncloseability follows van de Ven, Zeelenberg and Pieters 2009.",
        ],
        "citations": [CIT_FESTINGER, CIT_TAKAHASHI, CIT_VENDEVEN, CIT_SMITHKIM],
        "sig_lens": SIG_LENS_TRIGGER,
    },
    {
        "key": "personal_triggers",
        "name": "Personal Triggers: Memories, Anniversaries, and Private Associations",
        "group": "Triggers",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "Beyond the universal triggers lies a private minefield: "
            "the triggers that set off envy in one person and no one "
            "else, wired by personal history. The anniversary trigger: "
            "the month a sibling got married becomes, years later, a "
            "season when wedding announcements sting more - the calendar "
            "itself re-opens the comparison. The place trigger: the "
            "neighborhood where a friend bought a house, the campus "
            "where a rival thrived - geography holding the gap like a "
            "photograph. The object trigger: a particular brand of car, "
            "a style of kitchen, a breed of dog - anything that was "
            "present at the original comparison scene and now carries "
            "its charge. The person trigger: not a category but a "
            "specific individual - the cousin, the ex-colleague, the old "
            "friend - whose every success lands harder because the "
            "comparison history is longest and the similarity highest. "
            "The milestone trigger: ages and deadlines - thirty, forty, "
            "'by the time I was your age' - that convert someone else's "
            "timing into a verdict on one's own. These triggers are "
            "powerful precisely because they are invisible to everyone "
            "else: the person seems to overreact to nothing, when in "
            "fact they are reacting to a whole archive. The practical "
            "move is mapping: noticing which dates, places, objects, "
            "people, and milestones carry charge, and treating the map "
            "as information rather than fate. A mapped trigger can be "
            "prepared for; an unmapped one ambushes. Descriptive only - "
            "trigger patterns, never a reading of any real person."
        ),
        "how_it_works": (
            "Personal triggers are conditioned comparison cues. The "
            "original episode - the sibling's wedding, the rival's "
            "purchase - paired a neutral cue (a month, a street, a "
            "person) with the full envy appraisal and its pain signal; "
            "standard associative learning then lets the cue alone "
            "re-fire a compressed version of the appraisal, which is "
            "the aftershock mechanism from the time-course record "
            "wearing a personal costume. The person-specific trigger is "
            "the strongest because it stacks Festinger's similarity "
            "principle with history: the longer the comparison record, "
            "the more domains have been measured, the more the other "
            "serves as a standing reference point for the self. "
            "Milestone triggers work through counterfactual deadlines - "
            "'by forty' - that turn another's timing into a normative "
            "schedule, so their success reads as your lateness. The "
            "invisibility-to-others follows from the privacy of the "
            "pairing: no one else was at the original scene, so no one "
            "else sees the cue's charge. Mapping works because "
            "naming the cue moves it from the automatic system to the "
            "deliberate one - the appraisal still fires, but "
            "metacognition ('that's the March trigger, not the present "
            "situation') lets the person respond to now instead of then."
        ),
        "key_points": [
            "Personal triggers: anniversaries, places, objects, specific people, milestones.",
            "They are invisible to others - the person seems to react to nothing.",
            "The specific-person trigger is strongest: similarity plus the longest comparison history.",
            "Milestone triggers convert another's timing into a verdict on one's own.",
            "Mapping the triggers moves them from automatic ambush to preparable information.",
        ],
        "requirements": [
            "Five personal trigger types named with concrete examples.",
            "The invisibility-to-others mechanism explained.",
            "The specific-person trigger given its full weight.",
            "Milestone triggers explained via normative schedules.",
            "The mapping move stated as the practical response.",
        ],
        "standards": [
            "Conditioned-cue mechanism follows standard associative learning consistent with Lazarus 1991.",
            "Similarity-plus-history follows Festinger 1954.",
            "Metacognitive defusion follows the coping literature consistent with Lazarus 1991.",
        ],
        "citations": [CIT_LAZARUS, CIT_FESTINGER, CIT_BARRETT, CIT_SCHERER],
        "sig_lens": SIG_LENS_TRIGGER,
    },
    {
        "key": "surprise_triggers",
        "name": "Surprise Triggers: The Odd, Unexpected Things That Set Envy Off",
        "group": "Triggers",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "Some envy arrives from directions no one would predict, and "
            "these odd triggers are worth knowing because they ambush "
            "people who thought they had envy handled. The stranger "
            "trigger: a total stranger's good fortune - a lottery winner "
            "on the news, a viral success story - stinging despite zero "
            "similarity, because the brain briefly borrows the stranger "
            "as a comparison before the rational mind objects. The "
            "downward trigger: envying someone who objectively has less "
            "- the friend with the smaller house but the easier laugh, "
            "the colleague with the lower title but the calmer evenings "
            "- envy of a quality rather than a quantity, which confuses "
            "people because the scoreboard says they are winning. The "
            "fictional trigger: characters in shows, books, and games "
            "whose lives, loves, or competence spark real pangs - the "
            "appraisal system does not fully discount unreality when the "
            "emotional engagement is high. The past-self trigger: envy "
            "of who you used to be - the energy, the options, the "
            "unlined face at twenty-five - a comparison across time "
            "rather than across people, and one of the most quietly "
            "painful. The pet trigger: envying an animal's ease - the "
            "dog asleep in the sun while you answer emails - absurd on "
            "its face, honest underneath, because what is envied is "
            "freedom from the very comparing mind that produces envy. "
            "The common thread: the appraisal system is promiscuous. It "
            "will compare the self to almost anything - strangers, "
            "fiction, past selves, dogs - whenever the gap touches "
            "something valued. Knowing the system's promiscuity removes "
            "the shame of the odd trigger: it is not weird to feel it, "
            "it is normal for the instrument to be indiscriminate. "
            "Descriptive only - trigger patterns, never a reading of any "
            "real person."
        ),
        "how_it_works": (
            "Surprise triggers work because the comparison system fires "
            "on partial matches. The stranger trigger fires before the "
            "similarity check completes - Festinger's process begins "
            "with 'a person got a good thing' and only later asks 'is "
            "this person like me,' so the sting lands in the gap before "
            "the correction. The downward trigger reveals that envy "
            "tracks valued qualities, not net worth: the appraisal "
            "compares domain by domain, and a deficit in ease or laughter "
            "hurts regardless of surpluses elsewhere - which is why "
            "overall 'winning' does not immunize. The fictional trigger "
            "works through narrative transportation: when engagement is "
            "high, the brain processes the character's goods with the "
            "same appraisal machinery as real goods, discounting "
            "unreality only weakly. The past-self trigger is temporal "
            "comparison, the same machinery aimed backward - and it "
            "hurts because the comparison is maximally similar (it is "
            "literally you) with a gap that reads as uncloseable. The "
            "pet trigger is the system's irony engine: envying freedom "
            "from comparison is itself a comparison. The practical "
            "upshot is diagnostic: odd triggers reveal true values. "
            "Whatever the promiscuous system latches onto - ease, "
            "youth, freedom - is what the person actually prizes, "
            "information no personality quiz delivers as honestly."
        ),
        "key_points": [
            "The comparison system is promiscuous: strangers, fiction, past selves, even pets can trigger it.",
            "The stranger trigger fires before the similarity check completes.",
            "Downward envy targets qualities (ease, laughter), not quantities - winning overall does not immunize.",
            "Past-self envy is temporal comparison with maximal similarity and an uncloseable gap.",
            "Odd triggers are diagnostic: they reveal what the person truly values.",
        ],
        "requirements": [
            "At least five surprise trigger types with the mechanism of each.",
            "The promiscuity thesis stated as the common thread.",
            "The shame-removal point: odd triggers are normal instrument behavior.",
            "The diagnostic reading (triggers reveal values) included.",
            "A stated boundary: trigger patterns, never a reading of any real person.",
        ],
        "standards": [
            "Partial-match firing follows Festinger 1954: comparison begins before similarity is checked.",
            "Narrative transportation follows the standard media-psychology account consistent with Barrett 2017.",
            "Temporal comparison follows the self-evaluation literature consistent with Lazarus 1991.",
        ],
        "citations": [CIT_FESTINGER, CIT_BARRETT, CIT_LAZARUS, CIT_SMITHKIM],
        "sig_lens": SIG_LENS_TRIGGER,
    },
    {
        "key": "chain_reactions",
        "name": "Chain Reactions: How One Trigger Sets Off a Cascade",
        "group": "Triggers",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "Envy rarely stays where it starts. One trigger fires, and "
            "the feeling spreads along the network of everything "
            "connected to it - a cascade. It usually begins with a "
            "single sharp episode: the peer's promotion announced at "
            "lunch. By afternoon the cascade is running: the promotion "
            "reminds you of the house you haven't bought (possession "
            "envy), which reminds you of the friend whose marriage looks "
            "effortless (relationship envy), which reminds you of the "
            "talent you never developed (ability envy) - each link "
            "re-firing the pain signal, each making the next link easier "
            "to find. Mood-congruent memory is the engine: once envy is "
            "active, the mind preferentially retrieves other comparison "
            "losses, so the evidence for 'everyone is ahead of me' "
            "assembles itself. The cascade then recruits other emotions: "
            "envy shades into resentment ('it's all rigged'), resentment "
            "into anger, anger into shame about the anger, shame into "
            "withdrawal - a full weather system from one cloud. Behavior "
            "follows the weather: the person cancels plans, scrolls "
            "more, snaps at neutral remarks, each behavior confirming "
            "the mood. Breaking a cascade means breaking it early: "
            "naming the first trigger ('this started with the promotion "
            "news'), refusing the second link ('the house is a separate "
            "question for Saturday, not for now'), and doing one "
            "absorbing, valued thing to change the retrieval channel. "
            "Cascades feel like truth - 'everything really is going "
            "wrong' - but they are weather: real precipitation, wrong "
            "forecast. Descriptive only - cascade patterns, never a "
            "reading of any real person."
        ),
        "how_it_works": (
            "The cascade runs on three coupled mechanisms. First, "
            "spreading activation: the envy appraisal primes the whole "
            "comparison network, lowering the threshold for the next "
            "comparison to fire - each episode is easier to trigger than "
            "the last. Second, mood-congruent retrieval: the active envy "
            "state biases memory search toward other unfavorable "
            "comparisons, so the mind builds a case file that feels like "
            "objective evidence but is actually a sampled-on-the-"
            "dependent-variable archive. Third, emotion blending at each "
            "link: Scherer's sequential checks show how the initial "
            "envy appraisal (gap, self-relevant) gets re-appraised with "
            "new ingredients - unfairness (resentment), obstruction "
            "(anger), self-judgment (shame) - each re-appraisal adding a "
            "layer while keeping the original pain running underneath. "
            "Behavior then locks it in: withdrawal reduces access to "
            "disconfirming experience, scrolling supplies fresh triggers, "
            "snapping creates social friction that gets read as further "
            "evidence. The early-break technique works because it "
            "intervenes before spreading activation peaks: naming the "
            "first trigger externalizes it (metacognition over "
            "immersion), refusing the second link starves spreading "
            "activation, and absorption switches the retrieval channel. "
            "Late cascades are harder to break because each mechanism is "
            "now feeding the others - which is why the record stresses "
            "early."
        ),
        "key_points": [
            "One trigger spreads along the comparison network - each link re-fires the pain and eases the next.",
            "Mood-congruent memory assembles a case file that feels like evidence but is sampled by the mood.",
            "The cascade recruits resentment, anger, shame, and withdrawal - a full weather system.",
            "Behavior locks it in: withdrawal, scrolling, snapping each confirm the mood.",
            "Break it early: name the first trigger, refuse the second link, do one absorbing valued thing.",
        ],
        "requirements": [
            "A concrete cascade example traced link by link.",
            "Three mechanisms named: spreading activation, mood-congruent retrieval, emotion blending.",
            "The behavior lock-in loop described.",
            "The early-break technique with three concrete moves.",
            "The weather-not-forecast framing; a stated boundary: patterns, never a reading of any real person.",
        ],
        "standards": [
            "Spreading activation and mood-congruent retrieval follow standard cognitive-affective science.",
            "Sequential re-appraisal follows Scherer 2005.",
            "Coping intervention follows Lazarus 1991: metacognition and absorption as regulation.",
        ],
        "citations": [CIT_SCHERER, CIT_LAZARUS, CIT_BARRETT, CIT_SMITHKIM],
        "sig_lens": SIG_LENS_TRIGGER,
    },
]
ENTRIES += [
    # ------------------------------------------------ 22-25 HOW IT SHOWS IN BEHAVIOR
    {
        "key": "actions",
        "name": "What People Do When They Feel Envy: Typical Actions",
        "group": "How It Shows in Behavior",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "Envy moves people, and the movements fall into recognizable "
            "families. The benign family - envy channeled toward the self: "
            "studying the envied person's methods, practicing longer, "
            "asking for advice (sometimes without naming the envy), "
            "setting the envied achievement as a target. This is the "
            "leveling-up behavior van de Ven's research documented: the "
            "pain of the gap converted into effort to close it. The "
            "avoidance family: steering clear of the envied person, "
            "skipping the gatherings where the comparison will fire, "
            "muting or unfollowing the feed that triggers - not hostile, "
            "just protective distance. The information family: "
            "comparison research - checking the envied person's profile, "
            "asking mutual acquaintances about them, measuring and "
            "re-measuring the gap. Done openly it looks like interest; "
            "its engine is appraisal maintenance. The diminishing family "
            "- the malicious fork in action: downplaying the achievement "
            "('anyone could do that with those advantages'), spreading "
            "skeptical commentary, withholding praise or help that would "
            "be natural, and in sharper cases actively undermining - the "
            "withheld recommendation, the strategic silence. The "
            "self-soothing family: retail therapy, comfort food, the "
            "scroll for downward comparisons ('at least I'm not...'), "
            "rehearsing one's own advantages like a litany. Most real "
            "episodes mix families: a person studies the envied peer's "
            "methods on Monday (benign), avoids them on Tuesday "
            "(avoidance), and downplays the win at dinner (diminishing) - "
            "the fork is not a personality type but a moment-to-moment "
            "choice. Noticing which family is currently running is the "
            "practical skill, because each family answers to a different "
            "intervention. Descriptive only - behavior patterns of the "
            "emotion, never a reading of any real person."
        ),
        "how_it_works": (
            "The action families map onto Frijda's action tendencies "
            "playing out through the benign-malicious fork. Benign envy "
            "carries an approach tendency toward the standard: the "
            "appraisal says the gap is closeable and the other deserved "
            "it, so effort aims at emulation - studying methods, "
            "practicing, targeting. Malicious envy carries a "
            "leveling-down tendency: the appraisal says the gap is "
            "uncloseable or undeserved, so effort aims at the other "
            "person's standing - diminishing, withholding, undermining. "
            "Avoidance is the withdrawal tendency: when neither fork "
            "feels available, the system votes to exit the comparison "
            "field (muting, skipping, steering clear). Information "
            "behavior serves appraisal maintenance - the comparison "
            "system demands current data, so it surveils. Self-soothing "
            "is affect regulation by other means: downward comparison "
            "and comfort consumption directly counter the inferiority "
            "signal. The moment-to-moment mixing follows from appraisal "
            "fluctuation: as perceived closeability and deservedness "
            "shift with mood and information, the active family shifts "
            "too - which is why the same person can emulate in the "
            "morning and diminish by evening. Intervention follows the "
            "mapping: benign actions get fed (more study, more practice), "
            "avoidance gets a time limit, diminishing gets named and "
            "redirected, soothing gets kept but capped."
        ),
        "key_points": [
            "Five action families: benign emulation, avoidance, comparison research, diminishing, self-soothing.",
            "Benign envy converts the gap into effort; malicious envy aims at the other's standing.",
            "Avoidance is protective distance - exiting the comparison field.",
            "Real episodes mix families; the fork is a moment-to-moment choice, not a personality type.",
            "Each family answers to a different intervention.",
        ],
        "requirements": [
            "Five named action families with concrete behaviors in each.",
            "The benign and malicious families tied to the fork research.",
            "Moment-to-moment mixing stated to block personality-type misreading.",
            "Each family paired with its intervention direction.",
            "A stated boundary: behavior patterns of the emotion, never a reading of any real person.",
        ],
        "standards": [
            "Action tendencies follow Frijda 1986.",
            "Benign-malicious behaviors follow van de Ven, Zeelenberg and Pieters 2009.",
            "Appraisal fluctuation follows Scherer 2005 sequential checking.",
        ],
        "citations": [CIT_FRIJDA, CIT_VENDEVEN, CIT_SCHERER, CIT_SMITHKIM],
        "sig_lens": SIG_LENS_BEHAVE,
    },
    {
        "key": "speech",
        "name": "What Envy Sounds Like: Phrases, Tone, and Speech Patterns",
        "group": "How It Shows in Behavior",
        "ladder_rank": 9,
        "ladder_tier": "compounded",
        "description": (
            "Envy has a voice, and it rarely announces itself by name. "
            "The diminishing phrases: 'must be nice,' delivered flat - "
            "the classic; 'well, with their connections...,' trailing "
            "off so the implication does the work; 'good for them,' a "
            "beat too fast, the period audible. The comparison phrases: "
            "'I remember when I...' (redirecting the spotlight), 'at "
            "least I...' (the litany of consolation), 'some of us have "
            "to...' (virtue claimed through hardship). The interrogation "
            "phrases: questions that sound curious and function as "
            "audits - 'how did they afford that?', 'who did they know?', "
            "'how long did that actually take?' - comparison research "
            "conducted out loud. The praise that isn't: compliments with "
            "a hairline crack - 'brave choice, wearing that,' 'interesting "
            "that they picked you' - where the literal words are fine and "
            "the music is not. Tone carries what words won't: a slight "
            "flattening of warmth when the envied topic arises, pitch "
            "rising with the effort of performed gladness, pace "
            "quickening through the congratulations as if to get past "
            "them. Speech patterns shift too: shorter responses on the "
            "envied topic, subject changes that arrive a little too "
            "eagerly, and the notable absence - the follow-up question "
            "that never comes, the achievement never mentioned again. "
            "Writers take note: these are the dialogue tools for showing "
            "envy without naming it. And the self-check version: hearing "
            "these phrases in one's own mouth is the fastest honest "
            "signal that the feeling is running - faster than any body "
            "scan. Descriptive only - speech patterns of the emotion, "
            "never a reading of any real person."
        ),
        "how_it_works": (
            "Envious speech is indirect because direct admission is "
            "socially costly - envy being the most concealed emotion, "
            "the verbal system evolves workarounds. Diminishing phrases "
            "work by implicature: the literal content is deniable ('I "
            "just said must be nice') while the pragmatic content does "
            "the leveling work - a classic case of saying without saying "
            "that the appraisal literature predicts for high-cost "
            "feelings. The audit-questions serve the comparison system's "
            "data hunger out loud: each answer updates the gap "
            "measurement, and the question format provides cover. "
            "Cracked praise exploits the literal-pragmatic gap - the "
            "words pass politeness filters while prosody (flat warmth, "
            "raised pitch, rushed pace) transmits the true appraisal, "
            "which listeners decode automatically. The absences - no "
            "follow-up, no re-mention - are avoidance behavior in "
            "conversational form: the topic is a conditioned cue for "
            "the pain signal, so the discourse steers around it. The "
            "self-check works because production is less guarded than "
            "introspection: people monitor their thoughts for envy and "
            "miss it, but hear it in their own phrasing - the mouth "
            "reports what the inner censor redacts. For the recognition "
            "records, the rule is the same as for faces: speech patterns "
            "are candidates, never verdicts - 'must be nice' can be "
            "genuine warmth in the right mouth."
        ),
        "key_points": [
            "Diminishing phrases work by implicature: deniable words, leveling pragmatics.",
            "Audit-questions conduct comparison research out loud under cover of curiosity.",
            "Cracked praise passes politeness filters in words while prosody transmits the appraisal.",
            "Absences speak: no follow-up, no re-mention - conversational avoidance.",
            "Hearing these phrases in one's own mouth is the fastest honest self-signal.",
        ],
        "requirements": [
            "Named phrase families with quoted examples: diminishing, comparison, interrogation, cracked praise.",
            "Tone and pace described as carriers (flattened warmth, raised pitch, rushed congratulations).",
            "Conversational absences covered as avoidance.",
            "The writer's dialogue-tool note and the self-check note included.",
            "A stated boundary: speech patterns of the emotion, never a reading of any real person.",
        ],
        "standards": [
            "Implicature mechanism follows standard pragmatics consistent with Scherer 2005 expression components.",
            "Concealment cost follows the Smith and Kim 2007 account of envy as a hidden emotion.",
            "Prosody-as-channel follows the vocal-expression literature consistent with FACS-era voice research.",
        ],
        "citations": [CIT_SMITHKIM, CIT_SCHERER, CIT_FACS, CIT_LAZARUS],
        "sig_lens": SIG_LENS_BEHAVE,
    },
    {
        "key": "decisions",
        "name": "How Envy Changes Decisions and Judgment",
        "group": "How It Shows in Behavior",
        "ladder_rank": 9,
        "ladder_tier": "compounded",
        "description": (
            "Envy does not just feel - it votes. It votes in decisions "
            "large and small, usually without declaring its candidacy. "
            "In career decisions, envy can push people toward chasing "
            "someone else's track rather than their own: the colleague's "
            "promotion reframes success as that title, that company, "
            "that path - and the person optimizes for the envied "
            "milestone instead of their own values, sometimes for years. "
            "In spending, envy is the engine of positional consumption: "
            "purchases calibrated not to need or joy but to the "
            "neighbor's visible standard - the car, the kitchen, the "
            "wardrobe as comparison instruments. In relationships, envy "
            "votes for distance or sabotage: cooling toward the envied "
            "friend, or subtly undermining the envied rival - choices "
            "that feel like judgment ('they've changed') but run on "
            "comparison. In risk-taking, envy splits: benign envy "
            "increases productive risk (applying, launching, training - "
            "bets on closing the gap), while malicious envy increases "
            "destructive risk (bets aimed at the other's standing). In "
            "moral judgment, envy tilts the scales: the envied person's "
            "actions get judged more harshly, their motives read more "
            "cynically - the same behavior that would be 'strategic' in "
            "a neutral party becomes 'calculating' in the envied one. "
            "The common mechanism is criterion contamination: the "
            "comparison imports itself into decisions where it doesn't "
            "belong, and the decision gets optimized for the wrong "
            "objective - beating them instead of building what matters. "
            "The practical defense is the envy audit: for any major "
            "decision, ask 'would I still want this if no one would ever "
            "know I had it?' - what survives the question is yours; "
            "what evaporates was theirs. Descriptive only - decision "
            "patterns, never a reading of any real person's choices."
        ),
        "how_it_works": (
            "The mechanism is appraisal-driven goal substitution. The "
            "envy appraisal installs the other's standing as a reference "
            "point, and reference points hijack valuation: prospect-"
            "theory-style, outcomes get coded as gains or losses "
            "relative to the envied position rather than relative to "
            "one's own baseline. Career chasing follows: the promotion "
            "becomes the salient reference, so the utility of one's own "
            "path is computed as a shortfall. Positional consumption "
            "follows from the visibility leg of the trigger formula - "
            "spending becomes signaling because the comparison field is "
            "visual. Moral harshness toward the envied follows from the "
            "resentment blend: once the fairness story is active, "
            "motivated reasoning recruits evidence of the other's "
            "unworthiness, which then licenses the harsher judgment - a "
            "loop Smith and Kim's ill-will component predicts exactly. "
            "The benign/malicious split in risk-taking follows the fork: "
            "benign envy keeps the self as the project (productive bets), "
            "malicious envy makes the other the project (destructive "
            "bets). The audit question works by removing the audience: "
            "if the desire survives without witnesses, it was never "
            "about the comparison - it isolates intrinsic from "
            "positional value in one move."
        ),
        "key_points": [
            "Envy votes in career, spending, relationships, risk, and moral judgment - usually undeclared.",
            "Criterion contamination: decisions get optimized for beating them instead of building what matters.",
            "Benign envy raises productive risk; malicious envy raises destructive risk.",
            "The envied person's actions get judged more harshly - motivated moral tilt.",
            "The envy audit: 'would I want this if no one would ever know?'",
        ],
        "requirements": [
            "Five decision domains covered: career, spending, relationships, risk, moral judgment.",
            "Criterion contamination named as the common mechanism.",
            "The benign/malicious risk split stated.",
            "The envy audit question given as the practical defense.",
            "A stated boundary: decision patterns, never a reading of any real person's choices.",
        ],
        "standards": [
            "Reference-point hijacking follows the behavioral-economics account consistent with Scherer 2005 appraisal.",
            "Motivated moral tilt follows Smith and Kim 2007: ill will biases evaluation of the envied.",
            "Goal substitution follows Lazarus 1991: appraisals redirect goal hierarchies.",
        ],
        "citations": [CIT_SCHERER, CIT_SMITHKIM, CIT_LAZARUS, CIT_VENDEVEN],
        "sig_lens": SIG_LENS_BEHAVE,
    },
    {
        "key": "behavior_intensity",
        "name": "Behavior Under Intensity: How Actions Escalate",
        "group": "How It Shows in Behavior",
        "ladder_rank": 9,
        "ladder_tier": "compounded",
        "description": (
            "As envy intensifies, behavior escalates along a predictable "
            "ladder - and knowing the rungs helps people step off. Rung "
            "one, private: the feeling stays inside - replay, measuring, "
            "the gut-pit. No one would know. Rung two, leakage: the "
            "tight smile, the too-fast congratulations, the subject "
            "changed - small signals, deniable. Rung three, distancing: "
            "active avoidance - the mute, the skipped gathering, the "
            "cooled friendship. The comparison field is being managed by "
            "redesigning one's social world around it. Rung four, "
            "diminishing: the leveling talk goes public - skeptical "
            "commentary, the audit-questions asked in groups, praise "
            "withheld where it would be natural. The other's standing is "
            "now a project. Rung five, undermining: action against the "
            "standing - the withheld recommendation, the rumor passed "
            "along, the opportunity quietly blocked. This is the "
            "malicious fork fully open, and it is where envy starts "
            "costing the envious person more than the envied: "
            "reputations, relationships, self-respect. Rung six, "
            "consuming: the feeling organizes life - major decisions "
            "re-routed around the comparison, sustained hostility, the "
            "cascade running as climate. Movement up the rungs is "
            "driven by the same escalators every time: rumination "
            "(replay deepens the pain), proximity (daily contact "
            "re-fires), grievance narrative (the unfairness story "
            "licenses the next rung), and social echo (one confidant "
            "who agrees 'you were robbed' can lift a person two rungs). "
            "The way down is the reverse: interrupt replay, create "
            "distance, audit the fairness story, and choose confidants "
            "who redirect rather than amplify. Most people live on rungs "
            "one and two; knowing rungs three through six exist is what "
            "keeps them there. Descriptive only - escalation patterns, "
            "never a reading of any real person."
        ),
        "how_it_works": (
            "Escalation is the action tendency unfolding over time under "
            "sustained appraisal. Frijda's framework predicts the "
            "sequence: the initial tendency (leveling, benign or "
            "malicious) meets the world's responses, and each unblocked "
            "expression lowers the threshold for the next - a kind of "
            "behavioral kindling. Rumination deepens the pain signal "
            "(Takahashi's circuit, re-fired), which raises the "
            "motivational pressure for action; proximity supplies fresh "
            "appraisal episodes on schedule; the grievance narrative "
            "provides moral license, converting 'I want to hurt their "
            "standing' into 'I'm correcting an injustice' - the "
            "resentment blend doing its legitimizing work; social echo "
            "provides normative license, converting private urge into "
            "socially validated plan. Each rung is also a point of no "
            "return psychologically: diminishing said aloud is harder to "
            "take back than diminishing thought, and undermining acted "
            "on creates real-world consequences that then need "
            "justifying, which deepens commitment. This is why "
            "interventions are rung-specific and time-sensitive: at rungs "
            "one and two, attention tools suffice; at rung three, "
            "structural distance; at rung four, narrative audit; at five "
            "and six, the person needs the full cooling protocol plus "
            "often a trusted redirecting voice - because by then the "
            "behavior is generating its own justifications."
        ),
        "key_points": [
            "Six rungs: private feeling, leakage, distancing, diminishing, undermining, consuming.",
            "Four escalators: rumination, proximity, grievance narrative, social echo.",
            "Each rung upward is psychologically harder to reverse - said aloud sticks.",
            "Undermining costs the envious person more than the envied: reputation, relationships, self-respect.",
            "Interventions are rung-specific and time-sensitive; most people live on rungs one and two.",
        ],
        "requirements": [
            "Six named escalation rungs with the behavior at each.",
            "Four escalators named with their mechanism.",
            "The irreversibility gradient (thought vs said vs done) stated.",
            "The cost asymmetry (costs the envious more) stated.",
            "Rung-specific interventions; a stated boundary: patterns, never a reading of any real person.",
        ],
        "standards": [
            "Action-tendency unfolding follows Frijda 1986.",
            "Pain-signal deepening follows Takahashi et al. 2009.",
            "Moral licensing via the resentment blend follows Smith and Kim 2007 and van de Ven et al. 2009.",
        ],
        "citations": [CIT_FRIJDA, CIT_TAKAHASHI, CIT_SMITHKIM, CIT_VENDEVEN],
        "sig_lens": SIG_LENS_BEHAVE,
    },
]
ENTRIES += [
    # ------------------------------------------------ 26-28 EXPRESSING IT HEALTHILY
    {
        "key": "healthy_expression",
        "name": "Healthy Expression: Saying It, Showing It, Channeling It",
        "group": "Expressing It Healthily",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Envy can be expressed well, and the healthy forms all share "
            "one property: the feeling gets a job instead of a hiding "
            "place. Saying it - carefully, to the right person: 'I'll be "
            "honest, I felt a pang when I heard your news - I'm happy for "
            "you and I'm working through my own stuff.' Said to a "
            "trusted friend (not the envied person, not in the raw "
            "moment), this does three things: it breaks the concealment "
            "that lets envy curdle, it recruits support instead of "
            "suspicion, and it states the split screen honestly - glad "
            "and panged at once. Showing it - in converted form: letting "
            "the envy visibly become admiration and effort. 'Your launch "
            "lit a fire under me - I'm studying how you did it.' The "
            "feeling is not hidden; it is translated. Channeling it - "
            "the benign fork fully engaged: the gap becomes a curriculum. "
            "The envied person's methods get studied, the missing skill "
            "gets a practice schedule, the distant milestone gets broken "
            "into next actions. This is van de Ven's benign envy doing "
            "its documented work: the pain of the gap fueling the climb. "
            "Three forms to avoid even here: confessing to the envied "
            "person in a way that burdens them with your feeling "
            "(honesty is not the same as offloading), performing "
            "admiration so effusively it curdles into flattery, and "
            "channeling so compulsively that the envied milestone "
            "replaces your own values (the audit question from the "
            "decisions record stays in force). Healthy expression is not "
            "the absence of envy - it is envy with a job description. "
            "General everyday guidance only - not therapy, not advice "
            "for any specific person."
        ),
        "how_it_works": (
            "Healthy expression works by re-routing the action tendency "
            "rather than suppressing the appraisal. Suppression leaves "
            "the comparison loop running while adding control costs - "
            "the effortful mask from the face-intensity record - which "
            "is why bottling fails. Saying it to a trusted friend works "
            "through affect labeling and social co-regulation: naming "
            "the feeling reduces its intensity (the labeling effect), "
            "and a trusted listener provides the reality-check the "
            "grievance narrative needs. Showing it as admiration works "
            "through reappraisal: the same gap, framed as 'a standard "
            "worth reaching' instead of 'a verdict on me,' keeps the "
            "motivational pain while dropping the hostile ill will - "
            "Smith and Kim's formula with the second term removed. "
            "Channeling works through implementation: the benign fork's "
            "approach tendency gets concrete targets (study, practice, "
            "next actions), which converts diffuse arousal into "
            "directed effort - arousal with a steering wheel. The three "
            "avoidances follow from the same mechanics: offloading onto "
            "the envied person makes them manage your appraisal (unfair "
            "and relationship-damaging); effusive flattery is a "
            "performance that the body will leak through; compulsive "
            "channeling lets the comparison choose your goals, which is "
            "criterion contamination wearing a work ethic costume. The "
            "through-line: the feeling is data, the expression is a "
            "choice, and good choices give data work to do."
        ),
        "key_points": [
            "Healthy expression gives the feeling a job: say it, show it converted, channel it.",
            "Say it to a trusted friend (not the envied person, not raw) - breaks concealment, recruits support.",
            "Show it as admiration-plus-effort: the feeling translated, not hidden.",
            "Channel it as curriculum: the gap becomes study, practice, next actions.",
            "Avoid: offloading onto the envied, effusive flattery, compulsive channeling that replaces your values.",
        ],
        "requirements": [
            "Three healthy forms - saying, showing, channeling - each with concrete how.",
            "The right-person/right-time constraints on saying it.",
            "The benign fork tied to channeling with its documented effect.",
            "Three healthy-looking traps named and excluded.",
            "A stated boundary: general everyday guidance only, not therapy or personal advice.",
        ],
        "standards": [
            "Affect labeling and reappraisal follow the emotion-regulation literature consistent with Lazarus 1991.",
            "Benign-envy channeling follows van de Ven, Zeelenberg and Pieters 2009.",
            "Ill-will removal follows Smith and Kim 2007: inferiority without ill will approaches admiration.",
        ],
        "citations": [CIT_LAZARUS, CIT_VENDEVEN, CIT_SMITHKIM, CIT_FRIJDA],
        "sig_lens": SIG_LENS_HEALTHY,
    },
    {
        "key": "unhealthy_expression",
        "name": "Unhealthy Expression: Bottling It Up or Exploding - What Each Costs",
        "group": "Expressing It Healthily",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Envy mishandled goes two directions, and both charge "
            "interest. Bottling it up - the concealment strategy: never "
            "naming it, performing gladness, managing the face, steering "
            "around every trigger. The costs accumulate quietly. First, "
            "the control tax: sustained suppression is effortful, and "
            "the effort leaks into everything - the worked pleasantness, "
            "the fatigue that rest doesn't fix. Second, the pressure "
            "buildup: unexpressed envy doesn't decay, it ferments - the "
            "grievance narrative gets rehearsed in private until it "
            "hardens into a settled view of the envied person. Third, "
            "the distortion: bottled envy warps perception - the envied "
            "person's neutral actions start reading as provocations, "
            "because the hidden feeling needs the world to justify it. "
            "Fourth, the ambush: suppression fails under load - fatigue, "
            "drink, surprise - and the feeling exits sideways as the "
            "break from the face record: a sarcastic remark, a cold "
            "email, a cruelty that seems to come from nowhere. "
            "Exploding - the venting strategy: letting the hostile fork "
            "run - confrontations, accusations, public diminishing, the "
            "scorched-earth comment. The costs are louder and faster: "
            "relationships damaged in minutes that took years to build, "
            "reputation rewritten (people remember the outburst, not the "
            "provocation), and - the cruelest cost - the feeling doesn't "
            "leave. Venting rehearses the grievance narrative aloud, "
            "which strengthens it; the research on catharsis is clear "
            "that expressing hostility feeds hostility rather than "
            "draining it. Both strategies share a root error: treating "
            "the feeling as the problem instead of the signal. The "
            "feeling is the gauge; bottling smashes the gauge, exploding "
            "smashes the panel. The middle path - the previous record's "
            "say-it, show-it, channel-it - keeps the instrument and "
            "uses the reading. General everyday guidance only - not "
            "therapy, not advice for any specific person."
        ),
        "how_it_works": (
            "Bottling fails through the mechanics of expressive "
            "suppression: inhibiting the face, voice, and behavior while "
            "the appraisal keeps firing. The control effort consumes "
            "executive resources (the control tax), the unexpressed "
            "affect sustains sympathetic arousal (the pressure), and the "
            "hidden appraisal biases subsequent perception - "
            "mood-congruent processing makes the envied person's neutral "
            "behavior read as hostile, which then 'justifies' the hidden "
            "feeling in a self-sealing loop. The ambush under load "
            "follows from resource depletion: suppression is the first "
            "system to fail when resources drop, so the most suppressed "
            "feelings exit first and hardest. Exploding fails through "
            "rehearsal: venting the hostile fork is grievance-narrative "
            "practice, and practiced narratives strengthen - each "
            "retelling re-fires Takahashi's pain circuit alongside the "
            "reward of expression, wiring the loop tighter. Social costs "
            "follow from observer inference: witnesses don't see the "
            "months of bottled comparison, they see the outburst, and "
            "they update the person's reputation on the visible sample. "
            "Both strategies also forfeit the benign fork's documented "
            "benefit - the motivational fuel of the gap - because "
            "bottling never converts it and exploding spends it on "
            "destruction. The shared root error is appraisal confusion: "
            "the feeling reports a gap, and both strategies attack the "
            "reporter."
        ),
        "key_points": [
            "Bottling costs: control tax, pressure buildup, perceptual distortion, ambush under load.",
            "Exploding costs: instant relationship damage, reputation rewrite, and the feeling stays.",
            "Venting hostility feeds hostility - catharsis strengthens the grievance narrative.",
            "Both strategies forfeit the benign fork's motivational fuel.",
            "Shared root error: treating the signal as the problem instead of using the reading.",
        ],
        "requirements": [
            "Four named costs of bottling, each with mechanism.",
            "Three named costs of exploding, including the catharsis failure.",
            "The self-sealing loop of bottled envy (distortion justifying the feeling) described.",
            "The shared root error named as appraisal confusion.",
            "A stated boundary: general everyday guidance only, not therapy or personal advice.",
        ],
        "standards": [
            "Suppression costs follow the expressive-suppression literature consistent with Scherer 2005.",
            "Catharsis failure follows the venting literature: rehearsal strengthens, not drains.",
            "Mood-congruent distortion follows standard cognitive-affective science.",
        ],
        "citations": [CIT_SCHERER, CIT_TAKAHASHI, CIT_VENDEVEN, CIT_BARRETT],
        "sig_lens": SIG_LENS_HEALTHY,
    },
    {
        "key": "everyday_practices",
        "name": "Everyday Practices: Small Habits That Keep Envy in Balance",
        "group": "Expressing It Healthily",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Big interventions are for storms; daily life runs on small "
            "practices that keep envy at twinge volume. The noticing "
            "habit: once a day, catch one comparison in flight - name "
            "it silently ('there's the measuring again') and let it pass "
            "without following it. This is metacognition as hygiene, and "
            "it compounds: the comparisons you notice lose their "
            "automaticity. The fair-comparison habit: when the measuring "
            "starts, check the denominators - their highlight against "
            "your behind-the-scenes, their year ten against your year "
            "two. Unfair comparisons are envy's favorite fuel; auditing "
            "them starves it. The gratitude counterweight: a brief daily "
            "noting of three working things in your own life - not as "
            "denial of the gap but as context for it. The gap is real; "
            "it is not the whole picture. The input diet: curate the "
            "comparison field deliberately - mute the accounts that exist "
            "to trigger, limit the highlight-reel scrolling, choose "
            "inputs that inform rather than rank. The conversion habit: "
            "when envy fires, ask the benign question - 'what is the "
            "one next action this gap is pointing at?' - and either take "
            "it or schedule it. Unconverted envy loops; converted envy "
            "works. The admiration practice: deliberately practice "
            "unburdened gladness for others' goods - the genuine "
            "'wonderful, tell me more' - as a skill, not a performance. "
            "It gets easier with reps, and it directly exercises the "
            "muscle that envy atrophies. The values check, weekly: does "
            "my current chasing match my actual values, or someone "
            "else's scoreboard? - the audit question as routine "
            "maintenance. None of these abolish envy; all of them keep "
            "it informational rather than governmental. Small, daily, "
            "compounding - that is the whole method. General everyday "
            "guidance only - not therapy, not advice for any specific "
            "person."
        ),
        "how_it_works": (
            "Each practice targets one link in the envy machinery. "
            "Noticing targets automaticity: metacognitive labeling moves "
            "the comparison from the fast system to the slow one, where "
            "it can be evaluated rather than obeyed. Fair-comparison "
            "auditing targets the appraisal inputs: correcting the "
            "denominators changes the gap measurement itself, often "
            "dissolving the sting without any further work. Gratitude "
            "targets attentional scope: it widens the frame from the "
            "single deficit to the full portfolio, which re-weights the "
            "appraisal's relevance score downward. The input diet "
            "targets trigger frequency at the source - fewer appraisal "
            "episodes, fewer pain-signal firings, less rehearsal. "
            "Conversion targets the action tendency: giving the benign "
            "fork a concrete next action satisfies the approach urge "
            "that would otherwise loop as rumination. Admiration practice "
            "targets the ill-will component directly: rehearsing "
            "unburdened gladness weakens the envy-resentment blend's "
            "hostile term through counter-conditioning. The weekly "
            "values check targets criterion contamination: it re-anchors "
            "goals to intrinsic values before the comparison can "
            "substitute its own. The compounding logic is the point: "
            "each practice is weak alone and strong in combination, "
            "because envy is a loop and loops are broken by pressure at "
            "many points at once."
        ),
        "key_points": [
            "Seven small practices: noticing, fair-comparison audit, gratitude, input diet, conversion, admiration, values check.",
            "Each practice targets one link: automaticity, appraisal inputs, scope, trigger frequency, action tendency, ill will, goal contamination.",
            "Noticing compounds: caught comparisons lose automaticity.",
            "Converted envy works; unconverted envy loops.",
            "Weak alone, strong together - loops break under pressure at many points.",
        ],
        "requirements": [
            "At least six named daily/weekly practices with concrete how.",
            "Each practice tied to the mechanism it targets.",
            "The compounding logic stated explicitly.",
            "The values check tied back to criterion contamination.",
            "A stated boundary: general everyday guidance only, not therapy or personal advice.",
        ],
        "standards": [
            "Metacognitive labeling follows the affect-labeling literature consistent with Lazarus 1991.",
            "Reappraisal and attentional deployment follow standard emotion-regulation science.",
            "Counter-conditioning of ill will follows the learning literature consistent with Frijda 1986.",
        ],
        "citations": [CIT_LAZARUS, CIT_FRIJDA, CIT_VENDEVEN, CIT_BARRETT],
        "sig_lens": SIG_LENS_HEALTHY,
    },
]
ENTRIES += [
    # ------------------------------------------------ 29-31 RECOGNIZING IT IN OTHERS
    {
        "key": "reading_signs",
        "name": "Reading the Signs: Envy Cues in Other People",
        "group": "Recognizing It in Others",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Reading envy in others is detective work with four evidence "
            "bags - face, body, voice, behavior - and one golden rule: "
            "no single cue convicts; only clusters in context count. "
            "Face: the measuring glances, the lip press, the tight "
            "congratulations smile that stops at the mouth, the "
            "pleasantness held a fraction too long. Body: the torso "
            "angled away while attention stays fixed, the jaw working, "
            "the restless-contained fidgeting, the early exit from the "
            "comparison scene. Voice: warmth flattening when the envied "
            "topic arises, pitch lifting with performed gladness, the "
            "congratulations rushed through. Behavior: the audit-"
            "questions ('how did they afford that?'), the diminishing "
            "commentary, the praise with the hairline crack, the "
            "follow-up that never comes, the subject changed with "
            "suspicious eagerness. Context is what turns cues into "
            "reading: the same lip press at a funeral is grief, at a "
            "promotion party is a candidate for envy - the difference "
            "is the fresh upward comparison in the scene. The base-rate "
            "discipline matters too: envy is common, so the prior "
            "probability is never zero, but most cues have innocent "
            "explanations, so the posterior should stay humble. The "
            "honest output of reading is never 'they're envious' - it "
            "is 'envy is one candidate here, and here's what I'd do "
            "differently either way.' What you'd do differently: give "
            "the topic less airtime, share credit generously, avoid "
            "highlight-reel talk around them, and never - ever - "
            "confront someone with 'you're just jealous.' The reading "
            "is for your behavior, not their trial. This record teaches "
            "observation for kinder interaction. It never authorizes "
            "labeling any real person."
        ),
        "how_it_works": (
            "Multi-channel reading works because the channels fail "
            "independently: the face can be managed while the voice "
            "leaks, the voice steadied while the body fidgets - so "
            "agreement across channels raises confidence the way "
            "independent witnesses do. Context does the heavy lifting "
            "through appraisal logic: envy requires a fresh upward "
            "comparison in the scene, so the reader's real job is "
            "spotting the comparison, not the micro-expression - find "
            "the trigger and the cues arrange themselves around it. "
            "The base-rate discipline is Bayesian humility: with a "
            "common emotion and ambiguous cues, confident verdicts are "
            "usually overconfidence, and the cost of a false positive "
            "(accusing someone of envy) is far higher than the cost of "
            "a false negative (missing it and being kind anyway). The "
            "'for your behavior' rule follows from actionability: you "
            "cannot verify their feeling, but you can verify your "
            "response - less airtime for the trigger topic, generous "
            "credit-sharing, no highlight-reel talk. These responses "
            "are robust: they help whether the reading was right or "
            "wrong, because they are simply considerate. The "
            "never-confront rule follows from the concealment research: "
            "envy denied is envy defended, and accusation converts a "
            "manageable feeling into a relationship injury. Reading "
            "well means the other person never knows they were read - "
            "they only notice you were kind."
        ),
        "key_points": [
            "Four evidence bags: face, body, voice, behavior - clusters in context, never single cues.",
            "Find the comparison first; the cues arrange themselves around the trigger.",
            "Bayesian humility: false positives (accusation) cost far more than false negatives.",
            "The reading is for your behavior, not their trial.",
            "Never confront with 'you're just jealous' - accusation converts feeling into injury.",
        ],
        "requirements": [
            "Cues listed across all four channels with envy-specific examples.",
            "The cluster-in-context rule and the find-the-comparison-first method.",
            "Base-rate discipline and the false-positive cost asymmetry stated.",
            "The for-your-behavior rule with concrete kind responses.",
            "The never-confront rule; a stated boundary: observation for kindness, never labeling a real person.",
        ],
        "standards": [
            "Multi-channel agreement follows Ekman and Friesen FACS 1978: independent channels, convergent evidence.",
            "Appraisal-first reading follows Lazarus 1991 and Scherer 2005: find the appraisal, find the emotion.",
            "Concealment dynamics follow Smith and Kim 2007: envy denied is envy defended.",
        ],
        "citations": [CIT_FACS, CIT_LAZARUS, CIT_SCHERER, CIT_SMITHKIM],
        "sig_lens": SIG_LENS_RECOG,
    },
    {
        "key": "supportive_responses",
        "name": "What to Say and Do When Someone Near You Feels Envy",
        "group": "Recognizing It in Others",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Someone near you is feeling envy - maybe toward you, maybe "
            "toward a third party - and you want to respond well. The "
            "core principle: address the gap, never the feeling. Don't "
            "name their envy; tend the comparison. If the envy is toward "
            "you: share credit generously and specifically ('the design "
            "only worked because of your feedback on the draft'), keep "
            "highlight-reel talk to a minimum around them, and give the "
            "topic proportionate airtime - celebrate normally, don't "
            "perform extra humility (which reads as condescension) and "
            "don't flaunt (which feeds the comparison). If they cool "
            "toward you, don't chase the reason - give steady, unchanged "
            "warmth and let the weather pass; pursuing 'what's wrong?' "
            "forces the concealment they are working to maintain. If the "
            "envy is toward a third party and they are venting to you: "
            "listen without joining the diminishing ('that sounds "
            "frustrating' rather than 'they didn't deserve it'), reflect "
            "the gap back as information ('sounds like that promotion "
            "matters a lot to you - what part stings most?'), and gently "
            "offer the benign fork ('want to figure out what their path "
            "looked like?'). Don't audit their fairness story for them "
            "unless asked - uninvited debunking feels like taking sides "
            "against them. If their envy turns undermining toward "
            "someone: don't participate, don't pass along the commentary, "
            "and a light redirect ('let's not do the rumor thing') "
            "protects both them and the target. The through-line in all "
            "of it: you are tending a comparison wound, not judging a "
            "character flaw. People remember who was generous when they "
            "were at their smallest-feeling - that memory outlasts the "
            "envy itself. General everyday guidance only - not therapy, "
            "not advice for any specific person."
        ),
        "how_it_works": (
            "Address-the-gap works because the pain is in the comparison, "
            "not in being seen: naming the feeling triggers the "
            "concealment defense (envy denied is envy defended), while "
            "tending the comparison lowers the appraisal inputs directly. "
            "Generous credit-sharing works on the deservedness check: "
            "when the envied person distributes credit, the advantage "
            "looks less like a solo triumph and the comparison softens - "
            "it also models the benign stance. Proportionate airtime "
            "works on trigger frequency: normal celebration doesn't "
            "re-fire the appraisal the way performed humility (which "
            "implies the win needs apologizing for) or flaunting does. "
            "Steady warmth during cooling works through non-"
            "contingency: it signals the relationship isn't priced on "
            "the comparison, which lowers the stakes the envy is "
            "about. Reflecting the gap as information ('what part "
            "stings most?') does affect labeling plus reappraisal in one "
            "move: it names the pain without naming the sin, and turns "
            "the grievance narrative into data about values. Offering "
            "the benign fork works only when invited - uninvited advice "
            "reads as dismissal of the pain. The non-participation rule "
            "for undermining follows from social echo: one agreeing "
            "voice can lift a person two rungs up the escalation ladder, "
            "so withholding that voice is active harm prevention."
        ),
        "key_points": [
            "Core principle: address the gap, never name the feeling.",
            "Toward you: generous credit, minimal highlight-reel talk, steady warmth if they cool.",
            "Venting to you: listen without joining the diminishing; reflect the gap as information.",
            "Offer the benign fork only when invited; don't debunk their fairness story unasked.",
            "Never participate in undermining - one agreeing voice lifts them two rungs.",
        ],
        "requirements": [
            "Three scenarios covered: envy toward you, venting about a third party, envy turning undermining.",
            "Concrete phrasing examples for the good responses.",
            "The don't-chase-the-cooling and don't-perform-humility cautions.",
            "The social-echo mechanism tied to non-participation.",
            "A stated boundary: general everyday guidance only, not therapy or personal advice.",
        ],
        "standards": [
            "Affect labeling and reappraisal follow the regulation literature consistent with Lazarus 1991.",
            "Concealment defense follows Smith and Kim 2007.",
            "Social-echo escalation follows the escalation record's mechanism set.",
        ],
        "citations": [CIT_LAZARUS, CIT_SMITHKIM, CIT_VENDEVEN, CIT_FRIJDA],
        "sig_lens": SIG_LENS_RECOG,
    },
    {
        "key": "mistakes_to_avoid",
        "name": "What NOT to Do: Common Mistakes That Make Envy Worse",
        "group": "Recognizing It in Others",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Good intentions pave several well-traveled roads into worse "
            "envy. Mistake one: naming it - 'you're just jealous' or "
            "'don't be envious.' This is the cardinal error. It "
            "converts a manageable feeling into a defended identity, "
            "adds shame to pain, and guarantees the person will never "
            "discuss it with you again. Mistake two: the fairness "
            "lecture - 'life isn't fair, get over it.' True, useless, "
            "and wounding: it dismisses the pain while confirming that "
            "no one understands it, which deepens the grievance story. "
            "Mistake three: flaunting or over-celebrating in front of "
            "the person - victory laps, detailed highlight reels, "
            "repeated mentions. Each is a fresh trigger firing on "
            "schedule. Mistake four: the pity response - excessive "
            "reassurance, conspicuous inclusion, the sad eyes. Pity "
            "confirms inferiority, which is the core ingredient; it "
            "feeds the exact wound it means to soothe. Mistake five: "
            "joining the diminishing - agreeing 'they didn't deserve "
            "it' to be supportive. This feels kind and functions as "
            "social echo, licensing the malicious fork and lifting the "
            "person up the escalation ladder. Mistake six: forced "
            "gratitude - 'but you have so much to be grateful for!' The "
            "gratitude is true and the timing is terrible; deployed "
            "against active pain, it reads as dismissal and breeds "
            "resentment toward gratitude itself. Mistake seven: trying "
            "to fix the gap directly - pulling strings to get them the "
            "same good. Sometimes generous, often disastrous: it "
            "confirms the good was the whole issue, creates obligation "
            "and awkwardness, and leaves the comparison machinery "
            "untouched for next time. The meta-mistake underneath "
            "several of these: treating envy as a character verdict "
            "rather than a weather pattern. Weather gets tended; "
            "verdicts get defended. General everyday guidance only - "
            "not therapy, not advice for any specific person."
        ),
        "how_it_works": (
            "Each mistake backfires through a specific mechanism. Naming "
            "it triggers identity defense: the label 'envious person' "
            "threatens self-concept, so the system mobilizes to reject "
            "the label rather than process the feeling - concealment "
            "doubles down. The fairness lecture fails the validation "
            "requirement: unvalidated pain doesn't dissipate, it "
            "recruits - the grievance narrative gains 'and no one even "
            "listens' as a new chapter. Flaunting re-fires the appraisal "
            "on schedule: every mention is a fresh comparison episode "
            "with fresh pain-signal firing. Pity confirms the inferiority "
            "appraisal directly - the core relational theme of envy is "
            "'I am lesser here,' and pity is social confirmation of "
            "lesser status. Joining the diminishing provides the social "
            "echo that the escalation record identifies as a two-rung "
            "lift: private grievance becomes socially validated plan. "
            "Forced gratitude misfires on timing: reappraisal tools "
            "require the pain to be acknowledged first; deployed against "
            "unacknowledged pain, they read as invalidation. Fixing the "
            "gap directly misdiagnoses the level: the pain is in the "
            "comparison machinery, not the inventory - handing over the "
            "good leaves the machinery running and adds obligation "
            "static. The weather-not-verdict frame works because "
            "appraisals are states, and states pass; verdicts are "
            "traits, and traits get defended."
        ),
        "key_points": [
            "Seven mistakes: naming it, the fairness lecture, flaunting, pity, joining the diminishing, forced gratitude, fixing the gap.",
            "Naming it is the cardinal error - converts feeling into defended identity.",
            "Pity confirms inferiority; it feeds the exact wound it means to soothe.",
            "Joining the diminishing is social echo - a two-rung escalation lift disguised as support.",
            "Meta-rule: tend weather, don't issue verdicts.",
        ],
        "requirements": [
            "Seven named mistakes, each with the backfire mechanism.",
            "The cardinal error (naming it) given full weight.",
            "The pity paradox and the forced-gratitude timing point included.",
            "The social-echo mechanism tied to joining the diminishing.",
            "The weather-not-verdict meta-rule; a stated boundary: general guidance, not personal advice.",
        ],
        "standards": [
            "Identity-defense mechanism follows the self-concept literature consistent with Lazarus 1991.",
            "Invalidation effects follow the regulation literature: unvalidated pain recruits narrative.",
            "Social-echo escalation follows van de Ven et al. 2009 and the escalation record.",
        ],
        "citations": [CIT_LAZARUS, CIT_SMITHKIM, CIT_VENDEVEN, CIT_SCHERER],
        "sig_lens": SIG_LENS_RECOG,
    },
]
ENTRIES += [
    # ------------------------------------------------ 32-34 RELATED EMOTIONS, MIXES, FULL SIMULATION
    {
        "key": "related_map",
        "name": "Related Emotions Map: Neighbors, Opposites, and Close Cousins",
        "group": "Related Emotions and Mixes",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Envy sits in a crowded neighborhood, and the map repays "
            "study. Nearest neighbors: admiration (envy without the "
            "pain of inferiority - 'you have it and that's wonderful,' "
            "the unburdened gaze), resentment (envy plus the unfairness "
            "story - the most common blend), and longing (the ache of "
            "the gap without a specific person attached - envy with the "
            "comparison removed). Close cousins that get confused: "
            "jealousy (two parties vs three - lacking vs losing, covered "
            "in the distinction record), covetousness (desire for the "
            "object itself, with or without the other person - envy "
            "minus the comparison), greed (wanting more in general, no "
            "target required - envy minus both the person and the "
            "specific gap), and spite (the malicious fork detached from "
            "the gap and running on pure ill will - envy minus the "
            "longing). Opposites: admiration is the near-opposite "
            "(same upward gaze, no pain), and contentment is the far "
            "opposite (no gap felt at all - the comparison finds nothing "
            "missing). Telling cousins apart in practice: ask two "
            "questions. One - is there a specific other person whose "
            "having is the point? No person, no envy (it's longing, "
            "covetousness, or greed). Two - is the pain about lacking, "
            "or about losing? Lacking is envy; losing is jealousy. These "
            "two questions sort nearly every case. The map matters "
            "because each neighbor answers to different handling: "
            "admiration wants savoring, resentment wants the fairness "
            "audit, longing wants a plan, jealousy wants the bond "
            "secured, greed wants the enough-question. Mislabeling "
            "sends the wrong tool to the job - treating envy as jealousy "
            "secures a bond nobody threatened while the gap keeps "
            "aching. Descriptive only - a map of the emotion family, "
            "never a label for any real person."
        ),
        "how_it_works": (
            "The map is organized by appraisal ingredients, which is why "
            "the two questions work. Envy's full ingredient list is: "
            "specific other person + upward comparison + self-relevant "
            "gap + pain. Remove the person and you get longing or "
            "covetousness (object-directed desire without the social "
            "comparison). Remove the pain and you get admiration (the "
            "upward gaze without inferiority - Smith and Kim's formula "
            "with the ill-will and pain terms zeroed). Add the fairness "
            "violation and you get the envy-resentment blend. Change "
            "'lacking' to 'losing' and you cross into jealousy territory "
            "(Parrott and Smith's three-party structure). Generalize the "
            "wanting beyond any target and you get greed. Keep only the "
            "ill will and you get spite. On Russell's circumplex, the "
            "neighbors cluster in the unpleasant-activated quadrant but "
            "at different coordinates: envy sits mid-arousal (aching), "
            "resentment higher (hot), longing lower (wistful) - which is "
            "why the blends feel the way they do. On Plutchik's wheel, "
            "none are primaries; all are compounds, which is why they "
            "blend so readily with each other. The handling differences "
            "follow from the ingredient differences: you cannot audit a "
            "fairness story that isn't there (pure envy has none), and "
            "you cannot savor your way out of a real gap (longing needs "
            "a plan, not appreciation). The map is a tool selector: "
            "diagnose the ingredients, pick the tool."
        ),
        "key_points": [
            "Neighbors: admiration, resentment, longing. Cousins: jealousy, covetousness, greed, spite.",
            "Opposites: admiration (near), contentment (far).",
            "Two sorting questions: is a specific person's having the point? Is the pain about lacking or losing?",
            "Each neighbor answers to different handling - mislabeling sends the wrong tool.",
            "The map is organized by appraisal ingredients: remove or add one, get a different emotion.",
        ],
        "requirements": [
            "Named neighbors, cousins, and opposites with the ingredient difference for each.",
            "The two sorting questions stated as a practical tool.",
            "Each neighbor paired with its handling direction.",
            "The mislabeling cost (wrong tool to the job) stated.",
            "A stated boundary: a map of the emotion family, never a label for any real person.",
        ],
        "standards": [
            "Ingredient analysis follows Smith and Kim 2007: inferiority, ill will, resentment as separable terms.",
            "Envy-jealousy structure follows Parrott and Smith 1993.",
            "Circumplex placement follows Russell 1980; blend structure follows Plutchik 1980.",
        ],
        "citations": [CIT_SMITHKIM, CIT_PARROTT, CIT_RUSSELL, CIT_PLUTCHIK],
        "sig_lens": SIG_LENS_RELATED,
    },
    {
        "key": "emotion_mixes",
        "name": "Emotion Mixes: Envy Blended with Four Partners",
        "group": "Related Emotions and Mixes",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Envy blends the way paints do, and four blends cover most "
            "of real life. Blend one - envy plus admiration (the "
            "bittersweet aspirational blend): the painful 'I want what "
            "you have' fused with genuine 'and you are wonderful for "
            "having it.' This is benign envy at full strength - the ache "
            "that motivates rather than corrodes. It feels like looking "
            "at the sun: it hurts and you keep looking, because the "
            "looking teaches. Blend two - envy plus anger (the hot "
            "grievance blend): the gap fused with the sense of being "
            "wronged. This is the resentment blend from the partner "
            "record, running hotter - indignation doing the talking, "
            "the unfairness story fully staffed. It feels powerful and "
            "justified, which is exactly why it is dangerous: the "
            "power is borrowed from anger, the justification from a "
            "story that may not survive audit. Blend three - envy plus "
            "sadness (the gray blend): the gap fused with loss and "
            "heaviness, inferiority without the heat. This is envy after "
            "the fight goes out of it - wistful, flat, self-directed. "
            "It feels like weather that settled: not sharp, just gray, "
            "and it saps the benign fork's energy along with the "
            "malicious fork's. Blend four - envy plus shame (the hidden "
            "blend): the gap fused with judgment of the self for "
            "feeling the gap. This is the blend that drives envy "
            "underground - the shame censors the feeling, the censored "
            "feeling ferments, the fermentation confirms the shame. It "
            "feels like being caught: hot-faced, defensive, alone with "
            "it. Reading a blend means naming both ingredients, because "
            "each answers to its own tool: the envy part wants the gap "
            "addressed (plan or reframe), the partner part wants its "
            "own handling (anger wants the fairness audit, sadness "
            "wants restoration, shame wants the normalizing truth that "
            "envy is universal). Single-tool responses to blends fail "
            "because they treat a mixture as a pure substance. "
            "Descriptive only - blend patterns, never a label for any "
            "real person."
        ),
        "how_it_works": (
            "Blends form when two appraisals fire on the same situation. "
            "Envy-admiration: the upward comparison fires alongside a "
            "positive evaluation of the other - the gap hurts (envy) "
            "while the other's worth is affirmed (admiration) - which "
            "is why the blend motivates: the pain supplies energy, the "
            "admiration supplies direction, and ill will never enters. "
            "Envy-anger: the comparison fires alongside a norm-violation "
            "appraisal - someone got what they shouldn't have - and the "
            "two fuse at Scherer's deservedness check, producing the "
            "hot grievance with envy's inferiority underneath anger's "
            "approach energy. Envy-sadness: the comparison fires "
            "alongside a loss appraisal - the gap reads as something "
            "gone rather than something to chase - dropping arousal and "
            "leaving the gray, which is why this blend demotivates both "
            "forks. Envy-shame: the comparison fires alongside a "
            "self-conscious appraisal - the self judged for the feeling "
            "itself - creating the second-order loop where the emotion "
            "about the emotion suppresses the original. Plutchik's dyad "
            "logic predicts exactly this combinatorial richness: with "
            "even a few primaries, the blends number in the dozens, and "
            "envy - itself already a compound - blends with unusual "
            "ease. The two-tool rule follows: each ingredient keeps its "
            "appraisal, so each keeps its remedy, and the blend yields "
            "only to both."
        ),
        "key_points": [
            "Four blends: envy+admiration (aspirational), envy+anger (grievance), envy+sadness (gray), envy+shame (hidden).",
            "Envy+admiration is benign envy at full strength - pain plus direction, no ill will.",
            "Envy+anger borrows power from anger and justification from a story that may not survive audit.",
            "Envy+shame drives envy underground - the blend that censors and ferments.",
            "Blends need two tools: name both ingredients, treat each with its own remedy.",
        ],
        "requirements": [
            "Four named blends, each with felt texture and the mechanism of formation.",
            "The aspirational blend tied to benign envy; the grievance blend tied to the audit need.",
            "The hidden blend's censor-ferment loop described.",
            "The two-tool rule stated as the practical takeaway.",
            "A stated boundary: blend patterns, never a label for any real person.",
        ],
        "standards": [
            "Dyad formation follows Plutchik 1980: compounds blend into further compounds.",
            "Appraisal fusion follows Scherer 2005: the deservedness check as the merge point.",
            "Benign-blend motivation follows van de Ven, Zeelenberg and Pieters 2009.",
        ],
        "citations": [CIT_PLUTCHIK, CIT_SCHERER, CIT_VENDEVEN, CIT_SMITHKIM],
        "sig_lens": SIG_LENS_RELATED,
    },
    {
        "key": "full_simulation",
        "name": "Full Behavioral Simulation: Envy from Trigger to Resolution",
        "group": "Related Emotions and Mixes",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The showcase simulation: one envy episode walked end to end, "
            "every record in this database playing its part. The people "
            "are invented; the machinery is the archive's. Scene one - "
            "the trigger. Maya, a mid-level designer, learns at lunch "
            "that her peer Daniel - same hire date, same role - got the "
            "senior title she applied for. The comparison fires before "
            "her sandwich is down: same track, visible divergence, "
            "career-identity domain. The gut drops. Her congratulations, "
            "when Daniel stops by, arrive half a beat late and a touch "
            "too bright. Scene two - the peak. Back at her desk, the "
            "replay begins: his portfolio vs hers, the review meeting, "
            "the manager's phrasing. Each replay re-fires the sting. "
            "She catches herself auditing his advantages - the client "
            "account he inherited, the timing - and feels cheap about "
            "it. Her jaw aches by three o'clock; she skips the team "
            "coffee. The hostile fork is open and talking. Scene three - "
            "the cascade. The promotion reminds her of the apartment "
            "she hasn't bought, which reminds her of her sister's easy "
            "marriage - by evening the day feels thin and gray, though "
            "nothing else went wrong. She drafts a pointed message to a "
            "friend about Daniel's 'luck' - and stops, thumb hovering, "
            "because she hears the diminishing in her own phrasing. That "
            "hearing is the noticing habit firing. Scene four - the "
            "turn. She names it silently: envy, rung two, peak passing. "
            "She runs the fair-comparison audit: his account was "
            "inherited, true - but his last two launches were genuinely "
            "strong, also true. The grievance story loses its staffing. "
            "She asks the benign question: what is the one next action "
            "this gap points at? Answer: the portfolio piece she has "
            "been postponing. She opens the file. Scene five - the "
            "resolution. Not a Hollywood ending - the sting doesn't "
            "vanish, and Daniel's title still aches when she sees it. "
            "But the loop is starved: the portfolio work absorbs her, "
            "the audit defused the story, the noticing keeps catching "
            "replays early. A week later she congratulates him properly "
            "- and means more of it. An aftershock fires when his "
            "announcement email resurfaces; she notes it as an echo and "
            "keeps working. The simulation demonstrates the archive's "
            "whole thesis: trigger, appraisal, body, face, cascade, "
            "escalation risk, noticing, audit, conversion, resolution - "
            "envy as weather, navigated. All characters are fictional. "
            "This describes no real person and diagnoses no one."
        ),
        "how_it_works": (
            "The simulation is engineered to fire every mechanism in the "
            "database in order. The trigger scene loads the classic "
            "package: maximally similar other, visible good, "
            "self-relevant domain - the perfect-storm appraisal. The "
            "peak scene runs the time-course machinery: fast onset, "
            "replay-dense first hours, the body signature (jaw, gut, "
            "skipped coffee as avoidance), the face leak (late, bright "
            "congratulations), and the hostile fork opening through the "
            "deservedness audit. The cascade scene runs spreading "
            "activation plus mood-congruent retrieval across domains, "
            "with the escalation ladder visible at rung four "
            "(diminishing, drafted but unsent). The turn is the "
            "intervention stack in sequence: metacognitive noticing "
            "(naming rung two), fair-comparison audit (staffing the "
            "grievance story down), the benign question (converting the "
            "gap into the portfolio piece) - each practice from the "
            "everyday-practices record deployed at its mechanism. The "
            "resolution demonstrates the honest endpoint the database "
            "promises throughout: not abolition of the feeling but "
            "conversion of its function - the gauge still reads, but "
            "the reading now drives the work instead of the weather. "
            "The aftershock coda teaches the final lesson: the appraisal "
            "stays installed, echoes are normal, and noticing them as "
            "echoes is the durable skill. Fiction is the right vehicle "
            "because it lets every mechanism show without any real "
            "person being described."
        ),
        "key_points": [
            "Five scenes: trigger, peak, cascade, turn, resolution - every database mechanism firing in order.",
            "The turn stacks three interventions: noticing, fair-comparison audit, the benign question.",
            "The drafted-but-unsent message marks rung four reached and refused.",
            "Resolution is conversion, not abolition: the gauge still reads, now driving work instead of weather.",
            "The aftershock coda: echoes are normal; noticing them as echoes is the durable skill.",
        ],
        "requirements": [
            "A multi-scene narrative walking trigger through peak to resolution.",
            "Fictional characters explicitly marked as invented.",
            "At least six database mechanisms visibly deployed across the scenes.",
            "The intervention stack shown in sequence at the turn.",
            "An honest non-Hollywood resolution plus the aftershock coda.",
        ],
        "standards": [
            "Mechanism sequencing follows the full appraisal-coping account: Lazarus 1991, Scherer 2005, Frijda 1986.",
            "Intervention stack follows the regulation and benign-envy literature: van de Ven et al. 2009.",
            "Fictional-simulation ethics: invented characters only, per the series' descriptive-only canon.",
        ],
        "citations": [CIT_LAZARUS, CIT_SCHERER, CIT_FRIJDA, CIT_VENDEVEN],
        "sig_lens": SIG_LENS_RELATED,
    },
]
