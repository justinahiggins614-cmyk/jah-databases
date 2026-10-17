#!/usr/bin/env python3
"""Entries for the Judo Combat databases (combat batch 1, 2026-10-17).

Verified 2026-10-17: RAW SWEEP over the full manifest (2,390 databases)
PLUS every shard index title in jah-databases-data-1 (812 index files):
zero 'combat-judo' slugs/names; zero 'judo' / 'karate' / 'martial' /
'combat' / 'kung' databases of any kind - no near-hits at all. The paste's
rule was applied by name/purpose/record schema/capabilities: a Kodokan
judo technique archive teaching ukemi, nage-waza, katame-waza and randori
principles with full how-to body mechanics is a distinct capability, so
BUILD NEW is the verdict.

This build creates two NEW databases, 34 ladder-ordered records each:

  combat-judo             - The Judo Combat Database
                            (public-harvest: real, fact-checked Kodokan judo -
                            ukemi breakfalls, nage-waza throws by family
                            (te-waza, koshi-waza, ashi-waza, sutemi-waza),
                            katame-waza (osaekomi-waza pins, shime-waza
                            chokes, kansetsu-waza armlocks), and randori
                            principles - every record carrying the Japanese
                            terminology with translations, step-by-step
                            body mechanics, key points, safety requirements,
                            standards, and citations; standard references
                            Kano J. Kodokan Judo (rev ed 2013); Daigo T.
                            Kodokan Judo: Throwing Techniques (2005);
                            Ohlenkamp N. Black Belt: Judo Skills and
                            Techniques (2006); Inokuma I, Sato N. Best Judo
                            (1979); Harrison EJ. The Manual of Judo (1952);
                            and the IJF Sport and Organisation Rules
                            2024-2025)
  combat-judo-signature   - The Judo Combat Signature Database
                            (his original Signature Way of the Gentle Path:
                            seiryoku zenyo - maximum efficiency - as the
                            Signature law of perfect economy, jita kyoei -
                            mutual welfare - as the covenant between
                            partners, kuzushi as reading the opponent's
                            signature before it is written; src signature,
                            titles suffixed " (Signature Edition)", never
                            presented as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-CBJ- (public) and JAH-CBJS- (signature), verified free
in the manifest (zero hits) and in every shard index file (zero hits).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_combat_judo.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos.

Never the words "bat belt" anywhere. No website references. No Facebook.
Civilian martial-arts instruction only: sport judo as taught in dojos
worldwide; nothing on neutralizing or defeating military or
defense-grade systems.
"""

SIG_TAIL = ("Signature original - his original Signature Way of the Gentle "
            "Path: seiryoku zenyo, maximum efficiency, as the Signature law "
            "of perfect economy; jita kyoei, mutual welfare, as the covenant "
            "between training partners; kuzushi as reading the opponent's "
            "signature before it is written. Clearly labeled Signature-made, "
            "never presented as authentic public record.")

CIT_KANO = ("Kano J. Kodokan Judo. Rev ed. Kodansha International; 2013.")
CIT_DAIGO = ("Daigo T. Kodokan Judo: Throwing Techniques. Kodansha "
             "International; 2005.")
CIT_OHLENKAMP = ("Ohlenkamp N. Black Belt: Judo Skills and Techniques. "
                 "New Holland; 2006.")
CIT_INOKUMA = ("Inokuma I, Sato N. Best Judo. Kodansha International; 1979.")
CIT_HARRISON = ("Harrison EJ. The Manual of Judo. Foulsham; 1952.")
CIT_IJF = ("International Judo Federation. IJF Sport and Organisation Rules "
           "2024-2025.")

ENTRIES = [
    {
        "key": "reigi",
        "name": "Judo Reigi: Dojo Etiquette and Respect",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Reigi (etiquette, 礼儀) is the first lesson of judo and the frame "
            "around every other lesson. Before a student learns a single throw, "
            "the student learns to bow: bowing on entering and leaving the "
            "dojo, bowing onto and off the mat, the standing bow (ritsu-rei) "
            "and the kneeling bow (za-rei) that open and close every class, "
            "and the bow to each partner before and after every round of "
            "practice. Jigoro Kano, who founded Kodokan judo in 1882, placed "
            "etiquette at the base of the art because judo practice gives "
            "each partner real power over the other's body, and that power is "
            "only safe inside mutual respect. The rules are simple and "
            "concrete: keep the uniform clean and tied, keep fingernails and "
            "toenails short, remove jewelry, never step onto the mat in "
            "outdoor shoes, never talk while the instructor demonstrates, "
            "and thank every partner. Reigi is not decoration; it is the "
            "safety system that lets strangers throw each other at full "
            "speed and walk away friends."
        ),
        "how_it_works": (
            "Reigi works by making respect automatic so that attention stays "
            "on technique. The class opens with the students lined up by "
            "rank, the command to sit in seiza, a moment of quiet, and the "
            "kneeling bow to the instructor and to the mat - a fixed ritual "
            "that settles the room into training mode. Every pairing begins "
            "with a standing bow: both partners acknowledge that they are "
            "about to trust each other with their bodies. During practice, "
            "the etiquette rules remove the small frictions that cause "
            "injuries - a clean uniform grips predictably, short nails do "
            "not cut, and silence during demonstrations means nobody misses "
            "the safety detail. The bow after each round closes the "
            "exchange: whatever happened in the round, partners part with "
            "thanks. Over months this ritual trains the deeper habit that "
            "Kano intended - treating the partner as a collaborator in "
            "learning rather than an opponent to be beaten, which is exactly "
            "what makes hard randori possible without hard feelings."
        ),
        "key_points": [
            "Bow on entering and leaving the dojo, onto and off the mat, and to every partner before and after practice - the bow is the handshake of judo.",
            "Kano placed etiquette first because judo gives each partner real power over the other's body; respect is the safety system, not decoration.",
            "Keep the gi clean and tied, nails short, jewelry off, and outdoor shoes off the mat - small disciplines that prevent real injuries.",
            "Stay silent while the instructor demonstrates; missing one safety detail in a throw explanation is how accidents happen.",
            "The opening and closing bows settle the room into training mode and close it out - ritual focus that carries into every technique.",
        ],
        "requirements": [
            "A clean judo uniform (gi) with the belt tied in a proper square knot before stepping on the mat.",
            "Short fingernails and toenails, no jewelry, no outdoor footwear on the training surface.",
            "Knowledge of ritsu-rei (standing bow) and za-rei (kneeling bow) performed correctly.",
            "Silence and attention during demonstrations, and a bow to each partner before and after every exchange.",
            "Willingness to treat every partner as a collaborator in learning, regardless of rank or size.",
        ],
        "standards": [
            "Kodokan etiquette as codified by Jigoro Kano: bows on entry, exit, class open, class close, and partner exchange.",
            "Hygiene standards per IJF competition norms: clean gi, short nails, no hard objects - applied in the dojo at all times.",
            "Dojo conduct follows the principle of jita kyoei (mutual welfare and benefit): practice must leave both partners better.",
        ],
        "citations": [CIT_KANO, CIT_HARRISON],
        "sig_lens": (
            "The Signature read: reigi is the first covenant of the "
            "Signature Way. Before any technique is signed, the partners "
            "sign respect - the bow is the opening signature on every "
            "exchange, witnessed by the mat. Where public judo teaches "
            "etiquette as tradition, the Signature Way files it as the "
            "load-bearing structure: no respect, no trust; no trust, no "
            "throws at full speed."
        ),
    },
    {
        "key": "shisei",
        "name": "Shisei: Natural Posture for Judo",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Shisei (posture, 姿勢) is the body's ready position in judo, and "
            "Kano taught it before any throw because every technique starts "
            "from how you stand. The natural posture, shizen-hontai, is "
            "upright and relaxed: feet about shoulder-width apart, knees "
            "softly bent, weight distributed evenly, head level, eyes on the "
            "partner. From this balanced base the body can move in any "
            "direction without telegraphing, which is why the defensive "
            "posture, jigotai - low, wide, weight dropped - is used only "
            "briefly: it is strong but slow and announces fear. The "
            "right-side and left-side natural postures (migi-shizentai, "
            "hidari-shizentai) place one foot forward for gripping "
            "exchanges. Good shisei does three jobs at once: it keeps the "
            "center of mass inside the base of support so the student is "
            "hard to throw, it keeps the muscles relaxed so movement is "
            "fast, and it keeps the spine stacked so the throws of others "
            "meet structure instead of a bent-over gift of kuzushi."
        ),
        "how_it_works": (
            "Shisei works through balance geometry. With feet shoulder-width "
            "apart - about 0.45 meters for an average adult - the base of "
            "support is a rectangle roughly 0.45 meters wide, and the center "
            "of mass sits near its middle, giving a stability margin of "
            "about 0.22 meters in any direction before balance breaks. "
            "Soft knees lower the center of mass toward 0.95 meters, which "
            "shrinks the tipping leverage of any push. The upright spine "
            "matters because a bent-over posture moves the head and shoulders "
            "past the toes: the center of mass leaves the base, and the "
            "opponent's lightest pull finishes the job. Training builds the "
            "posture by drilling the transitions - natural to defensive to "
            "natural - until the body drops into jigotai under pressure "
            "without the mind deciding, and returns to relaxed upright the "
            "instant the pressure passes. Instructors test shisei the simple "
            "way: they push the student from each of the eight directions, "
            "and correct posture absorbs the push with a step, not a fall."
        ),
        "key_points": [
            "Shizen-hontai (natural posture): upright, relaxed, feet shoulder-width, knees soft - the ready position for everything.",
            "Jigotai (defensive posture): low and wide for the moment of danger only - strong but slow, and it signals fear.",
            "Keep the center of mass inside the base of support: head over hips over feet, never bent past the toes.",
            "Relaxed muscles move faster than tense ones; posture carries the load so the muscles stay free to act.",
            "Drill the transitions until dropping low under pressure and standing tall after are both automatic.",
        ],
        "requirements": [
            "Enough mat space to stand and be pushed from all sides without hitting anyone.",
            "A partner to test the posture with light pushes from the eight directions.",
            "A mirror or video check at first: most beginners cannot feel their own lean.",
            "Bare feet on the mat - posture is read through the soles, and shoes lie about balance.",
            "Patience: the upright relaxed stance feels wrong to beginners for the first weeks.",
        ],
        "standards": [
            "Kodokan shisei doctrine: shizen-hontai as the base posture, jigotai as the momentary defensive form.",
            "Stability follows standard balance geometry: the center of mass must project inside the support base.",
            "Instructional standard per Kano: posture is taught and tested before the first throw is attempted.",
        ],
        "citations": [CIT_KANO, CIT_INOKUMA],
        "sig_lens": (
            "The Signature read: shisei is the body's signature stance - the "
            "unwritten statement of where the center of mass lives. The "
            "Signature Way treats posture as the first document: written in "
            "bone and balance, filed with every step, and impossible to "
            "forge under pressure. Maximum efficiency begins here, because "
            "a balanced body spends nothing to stay standing."
        ),
    },
    {
        "key": "mae_ukemi",
        "name": "Mae Ukemi: Forward Breakfall",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Mae ukemi (forward breakfall, 前受身) is the technique for "
            "hitting the mat face-down without injury - the landing every "
            "judoka needs because forward throws are the most common kind. "
            "The body falls forward and the arms shoot out to slap the mat "
            "just before the torso lands: palms down, arms slightly bent, "
            "slapping the surface to spread the impact across the forearms "
            "and chest instead of letting it concentrate on one point. The "
            "head turns sharply to one side so the chin and face never touch "
            "the mat, the legs extend behind with the tops of the feet flat, "
            "and the whole body lands as one connected surface. Done right, "
            "a full-speed forward throw ends in a loud slap and a student "
            "who stands straight back up. Done wrong - arms locked straight, "
            "head facing down, one elbow taking everything - it ends in "
            "injury. This is why ukemi is taught on day one and drilled for "
            "years: it is the insurance policy under every throw in the art."
        ),
        "how_it_works": (
            "Mae ukemi works by converting a dangerous point impact into a "
            "broad, timed slap. Falling from hip height - about 0.9 meters - "
            "the body reaches roughly 4.2 meters per second at the mat; "
            "stopping that speed over the 0.25 meters of arm-and-torso "
            "compression spreads the deceleration to about 35 meters per "
            "second squared, near 3.6 g, which the slapping arms and the "
            "rib cage absorb without damage. The slap itself does two jobs: "
            "the arm muscles tense at contact and act as shock absorbers, "
            "and the broad palm-and-forearm surface distributes force so no "
            "single joint takes the peak. Turning the head aside keeps the "
            "face and chin out of the impact line entirely. Training starts "
            "from the knees, then from a squat, then from standing, then "
            "from a partner's gentle forward push - each stage adding height "
            "only after the slap timing is automatic. The loud slap is not "
            "theater; it is the sound of energy being spread on schedule."
        ),
        "key_points": [
            "Slap the mat with palms down and arms slightly bent just before the torso lands - the slap spreads the impact, it does not catch the body.",
            "Turn the head sharply to one side; the face and chin must never lead the fall.",
            "Land as one connected surface - forearms, chest, thighs - never one elbow or one point.",
            "Never lock the arms straight: bent arms are shock absorbers, straight arms are levers that break.",
            "Progress in stages - knees, squat, standing, partner push - and never add height before the timing is automatic.",
        ],
        "requirements": [
            "A proper mat (tatami or foam judo mat) - never practice breakfalls on hard floors.",
            "A qualified instructor watching the first sessions: head position is the critical safety check.",
            "Progression only from knees upward; no standing falls until the kneeling slap is reflexive.",
            "No jewelry, no zippers, nothing hard on the body that the mat will press into flesh.",
            "A partner for the later stages who pushes gently and predictably, never surprises.",
        ],
        "standards": [
            "Kodokan ukemi curriculum: mae ukemi taught from kneeling before standing, per Kano's progression.",
            "Impact is managed by increasing the stopping distance and area - the standard physics of fall safety.",
            "Head clearance is mandatory: the face never contacts the mat in a correct forward breakfall.",
        ],
        "citations": [CIT_KANO, CIT_OHLENKAMP],
        "sig_lens": (
            "The Signature read: mae ukemi is the Signature art of landing "
            "the fall on purpose. The slap is a signature struck against "
            "the mat - timed, deliberate, and loud enough to prove the "
            "energy was filed correctly. Where others meet the ground by "
            "accident, the Signature Way meets it by design."
        ),
    },
    {
        "key": "koho_ukemi",
        "name": "Koho Ukemi: Back Breakfall",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Koho ukemi (back breakfall, 後方受身) is the technique for being "
            "thrown or pushed straight backward - the landing that protects "
            "the spine and, above all, the head. The student sits back, "
            "tucks the chin hard against the chest, rounds the back, and "
            "slaps both arms against the mat at roughly forty-five degrees "
            "from the body just before the back lands. The chin tuck is the "
            "whole secret: with the chin pinned down, the back of the head "
            "cannot whip into the mat, and the rounded spine rolls the "
            "impact across the shoulder blades and lats instead of driving "
            "it into one vertebra. The arms slap out to the sides - never "
            "behind the head, where a trapped arm breaks - and the legs "
            "come up slightly so the fall finishes flat. Backward throws "
            "like o soto gari and tani otoshi demand this landing "
            "constantly, which is why koho ukemi is drilled until the chin "
            "tucks before the mind even registers the fall."
        ),
        "how_it_works": (
            "Koho ukemi works by protecting the two structures that backward "
            "falls threaten: the skull and the spine. Tucking the chin to "
            "the chest locks the neck in flexion, which keeps the head about "
            "0.15 meters off the mat through the whole landing - the head "
            "never makes contact at all in a correct breakfall. Rounding "
            "the back turns the torso into a curved shell; the impact that "
            "would have concentrated on a flat spine now travels across the "
            "broad muscles of the upper back, and the arm slap at contact "
            "adds a wide braking surface on each side. The timing rule is "
            "one motion: chin tucks as the balance breaks, arms slap as the "
            "back meets the mat - practiced first sitting, then squatting, "
            "then standing, then from a partner's backward push. The common "
            "failure is reaching back with the hands to catch the fall; the "
            "arms cannot stop a falling body, and wrists break trying. The "
            "drill rewires the reflex from catching to slapping."
        ),
        "key_points": [
            "Tuck the chin hard to the chest the instant balance breaks - the head must never touch the mat.",
            "Slap both arms out at about forty-five degrees, palms down, as the back lands; never reach behind the head.",
            "Round the back so the impact rolls across the shoulder blades instead of hammering one vertebra.",
            "The motion is one piece: chin tucks, body sits back, arms slap - drilled sitting, then squatting, then standing.",
            "Never try to catch the fall with the hands; the slap brakes the body, the hands cannot.",
        ],
        "requirements": [
            "A proper mat; the back breakfall is never drilled on hard surfaces.",
            "An instructor checking chin position first - the tuck is the non-negotiable safety element.",
            "Stage progression: sitting, squatting, standing, partner push; no skipping.",
            "Clear space behind the student equal to a full body length.",
            "A partner who pushes straight back gently and squarely, never at an angle.",
        ],
        "standards": [
            "Kodokan ukemi curriculum: koho ukemi with the chin-tuck-first rule, per Kano.",
            "Head clearance of roughly 0.15 meters is maintained through the landing in correct form.",
            "Arms slap at approximately forty-five degrees from the torso - never trapped behind the head.",
        ],
        "citations": [CIT_KANO, CIT_OHLENKAMP],
        "sig_lens": (
            "The Signature read: koho ukemi is the Signature covenant with "
            "gravity going backward - the chin tucks to guard the most "
            "valuable document, the head. The Signature Way treats the "
            "backward fall as a test of trust in training: filed correctly, "
            "the spine lands as a bridge, not a break."
        ),
    },
    {
        "key": "yoko_ukemi",
        "name": "Yoko Ukemi: Side Breakfall",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Yoko ukemi (side breakfall, 横受身) is the landing for throws "
            "that dump the student onto one side - the constant companion "
            "of foot sweeps like de ashi harai and hip throws that spill "
            "sideways. The student falls to the side, slaps the mat hard "
            "with the entire arm on the landing side - palm down, arm "
            "straight out from the shoulder - and lands on the side of the "
            "thigh, hip, and lat in one connected line, with the head lifted "
            "clear of the mat by tucking slightly toward the upper shoulder. "
            "The upper leg comes across to stabilize, and the whole side of "
            "the body takes the landing as a single broad surface. The "
            "critical detail is the arm: it slaps down at the moment of "
            "contact, timed to brake the fall, and it must never be trapped "
            "under the body, where the shoulder takes the full load. Both "
            "sides are drilled equally from the start, because a judoka who "
            "can only fall left is a judoka waiting for a right-sided throw."
        ),
        "how_it_works": (
            "Yoko ukemi works by turning the body's side into a landing "
            "strip. A 70-kilogram student falling from hip height carries "
            "about 618 joules of energy; the arm slap plus the broad side "
            "of the torso stop that energy over roughly 0.2 meters of "
            "compression, which spreads the peak force near 3,000 newtons "
            "across the arm, hip, and lat instead of concentrating it on "
            "the shoulder joint. Lifting the head clear - the ear stays off "
            "the mat - removes the neck from the impact chain entirely. "
            "Training runs both sides in strict alternation: from a low "
            "side-sitting position the student tips over and slaps, then "
            "from a squat, then from standing with a partner's sideways "
            "push, then from actual foot sweeps at low speed. Instructors "
            "listen for the slap timing - the arm must meet the mat a "
            "fraction before the torso, braking the fall, not after it, "
            "which is just noise on top of an injury."
        ),
        "key_points": [
            "Slap the full arm on the landing side down at contact - palm down, straight out from the shoulder, timed a fraction before the torso lands.",
            "Land on the whole side - thigh, hip, lat - as one connected surface, never on the shoulder point alone.",
            "Keep the head lifted clear of the mat; the ear never touches down.",
            "Never trap the arm under the body - a pinned arm turns the shoulder into the impact point.",
            "Drill both sides equally from day one; one-sided breakfalls are a standing invitation to the other side.",
        ],
        "requirements": [
            "A proper mat and clear space to both sides of the student.",
            "An instructor verifying head clearance and arm position before standing practice.",
            "Strict left-right alternation in every drill set.",
            "Progression from side-sitting to squat to standing to partner-assisted.",
            "No hard objects on the body; the hip and ribs take direct mat contact.",
        ],
        "standards": [
            "Kodokan ukemi curriculum: yoko ukemi drilled bilaterally from the first lesson.",
            "Impact is spread across the arm, hip, and lat - the standard broad-surface fall-safety method.",
            "Head clearance is mandatory: the head is held off the mat through the landing.",
        ],
        "citations": [CIT_KANO, CIT_OHLENKAMP],
        "sig_lens": (
            "The Signature read: yoko ukemi files the fall on its side, the "
            "Signature ledger kept left and right in perfect balance. The "
            "arm's slap is the stamp that closes the entry - one side, one "
            "sound, one safe landing. The Signature Way keeps both columns "
            "equal: never a one-sided account."
        ),
    },
    {
        "key": "zenpo_kaiten",
        "name": "Zenpo Kaiten Ukemi: Forward Rolling Breakfall",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Zenpo kaiten ukemi (forward rolling breakfall, 前方回転受身) is "
            "the roll that turns a hard forward throw into a smooth "
            "rotation - the landing used when a throw like seoi nage or tai "
            "otoshi launches the student with forward momentum that a flat "
            "slap cannot absorb. Instead of stopping the fall, the student "
            "converts it: stepping deep with one foot, the arm on that side "
            "reaches across the body to the mat, the head tucks tight, and "
            "the body rolls diagonally across the back from one shoulder to "
            "the opposite hip, slapping the mat as the roll completes and "
            "coming up facing the partner, ready to continue. The roll is "
            "never straight over the top of the head - that loads the neck - "
            "but diagonal across the back, shoulder to opposite hip, which "
            "is why the tucked chin and the curved spine matter so much. A "
            "clean forward roll dissipates a full-speed throw and returns "
            "the student to the feet in one motion; it is the most athletic "
            "of the breakfalls and the gateway to advanced throwing practice."
        ),
        "how_it_works": (
            "The forward roll works by trading a stop for a circle. Rolling "
            "across the back from shoulder to opposite hip traces a circle "
            "whose circumference - about 1.73 meters for a curled body "
            "roughly 0.55 meters in diameter - closely matches the student's "
            "own body length, so the roll completes in one natural rotation "
            "with no slack to whip the neck. The diagonal path is the "
            "safety mechanism: rolling straight over the crown would drive "
            "the full falling force through the cervical spine, while the "
            "shoulder-to-hip diagonal spreads it across the back muscles. "
            "The reaching arm sets the roll's line before the body commits - "
            "where the hand plants, the shoulder follows - and the final "
            "slap as the roll finishes brakes any leftover speed. Drilled "
            "as a pure gymnastic roll first, then from a kneeling partner "
            "push, then from standing throws at increasing speed, the "
            "motion becomes the default response to forward momentum: ten "
            "clean rolls in about fourteen seconds is the benchmark of a "
            "reliable roll, roughly 1.4 seconds per roll."
        ),
        "key_points": [
            "Roll diagonally across the back, shoulder to opposite hip - never straight over the top of the head.",
            "Tuck the chin tight and round the spine; the curled body traces a circle about 1.73 meters around.",
            "The reaching arm plants the roll's line before the body commits - hand plants, shoulder follows.",
            "Slap the mat as the roll completes to brake leftover speed, and come up facing the partner.",
            "Build it as a gymnastic roll first, then from kneeling pushes, then from real throws at rising speed.",
        ],
        "requirements": [
            "A proper mat with a clear rolling lane at least three body lengths long.",
            "Mastery of the flat forward breakfall first - the roll is built on top of the slap, not instead of it.",
            "An instructor checking the diagonal line: straight-over-the-head rolls are stopped immediately.",
            "Both-side rolling from the start, alternating every repetition.",
            "A patient partner for the throwing stages who increases speed only as the roll stays clean.",
        ],
        "standards": [
            "Kodokan ukemi curriculum: zenpo kaiten taught after the flat breakfalls, diagonal line mandatory.",
            "The roll path runs shoulder to opposite hip, keeping the cervical spine out of the load path.",
            "Benchmark: ten clean rolls in about fourteen seconds signals a reliable roll.",
        ],
        "citations": [CIT_KANO, CIT_OHLENKAMP, CIT_INOKUMA],
        "sig_lens": (
            "The Signature read: the forward roll is the Signature circle - "
            "the fall filed not as a crash but as a rotation, energy "
            "entered on one side of the ledger and returned on the other. "
            "Maximum efficiency in its purest form: nothing stopped, "
            "everything converted, the student back on the feet with the "
            "momentum accounted for."
        ),
    },
    {
        "key": "kuzushi",
        "name": "Kuzushi: The Eight Directions of Balance Breaking",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Kuzushi (balance breaking, 崩し) is the master key of judo: the "
            "art of moving the opponent's center of mass outside the base of "
            "support so the body must fall. Kano identified eight directions "
            "of kuzushi - happo no kuzushi - the complete compass of "
            "unbalancing: forward, backward, left, right, and the four "
            "corners (front-left, front-right, rear-left, rear-right). Every "
            "throw in judo is simply kuzushi plus the fitting-in of the body "
            "(tsukuri) plus the execution (kake); without the first, the "
            "other two are wrestling against a balanced opponent, which is "
            "why beginners who skip kuzushi find every throw mysteriously "
            "impossible. The eight directions matter because each throw "
            "family feeds on specific ones - o soto gari wants rear kuzushi, "
            "seoi nage wants the front corner, uchi mata wants the front - "
            "and the advanced game is chaining them: break balance one way, "
            "and when the opponent resists, the resistance itself becomes "
            "kuzushi in the opposite direction. To study kuzushi is to "
            "study the moment the throw becomes inevitable."
        ),
        "how_it_works": (
            "Kuzushi works on the same balance geometry as posture, in "
            "reverse. A standing opponent's stability margin is about 0.22 "
            "meters; pulling the shoulders so the center of mass travels "
            "past that margin in any of the eight directions removes the "
            "body's ability to recover without stepping. The eight "
            "directions form four opposing pairs whose vectors sum to zero "
            "- pull forward and push backward cancel - which is the "
            "mathematical reason combination throws work: commit the "
            "opponent to resisting one direction and their own resistance "
            "adds to your attack in the opposite one. The pull is never a "
            "yank with the arms; it is a whole-body action timed to the "
            "opponent's step, applied at the shoulders through the grips, "
            "with the hips and legs driving. The classic drill is uchi-komi "
            "with a partner stepping: the student practices breaking "
            "balance to each of the eight points in turn - front, back, "
            "sides, and the four corners at forty-five degrees - until the "
            "hands find the direction without the eyes choosing it."
        ),
        "key_points": [
            "Happo no kuzushi: eight directions - front, back, left, right, and the four forty-five-degree corners - the complete compass of unbalancing.",
            "Every throw is kuzushi plus tsukuri (fitting in) plus kake (execution); skip the first and the throw fails against a balanced opponent.",
            "Match the direction to the throw: o soto gari feeds on rear kuzushi, seoi nage on the front corner, uchi mata on the front.",
            "The eight directions are four opposing pairs - resistance to one becomes kuzushi for its opposite, which is the engine of combinations.",
            "Break balance with the whole body timed to the opponent's step, never with an arm yank; the grips transmit, the hips drive.",
        ],
        "requirements": [
            "A partner willing to be pulled off balance repeatedly - kuzushi cannot be learned solo.",
            "Solid grips (kumikata) first; without the connection, the pull has nothing to travel through.",
            "A mat and enough space to step in all eight directions.",
            "An instructor to verify the direction: most beginners pull where they are, not where the throw needs.",
            "Repetition in the hundreds - kuzushi is a feel in the hands, and feel is built by volume.",
        ],
        "standards": [
            "Kodokan happo no kuzushi: the eight-direction system as codified by Kano.",
            "Vector geometry of balance: the center of mass must exit the support base; opposing pairs sum to zero.",
            "Instructional standard: kuzushi is drilled to each direction before the throws that use it are taught.",
        ],
        "citations": [CIT_KANO, CIT_DAIGO],
        "sig_lens": (
            "The Signature read: kuzushi is reading the opponent's "
            "signature before it is written - the eight directions are "
            "eight ways to unwrite their balance. The Signature Way treats "
            "the compass as a combination lock: find the direction their "
            "stance has already half-chosen, and the throw files itself."
        ),
    },
    {
        "key": "tai_sabaki",
        "name": "Tai Sabaki: Body Movement and Evasion",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Tai sabaki (body movement, 体捌き) is the footwork of angles: "
            "the pivots, turns, and evasions that move the body out of the "
            "attack's line and into the throw's position. Where footwork "
            "drills move the student across the mat, tai sabaki rotates the "
            "student around the opponent - the 180-degree pivot that turns "
            "a facing exchange into a back-to-chest throwing position is the "
            "signature movement of the art, and it appears inside seoi nage, "
            "tai otoshi, o goshi, and half the throwing catalog. The "
            "principle is economy: the smallest turn that clears the attack "
            "and loads the throw. Beginners pivot too far, too slowly, on "
            "flat feet; trained tai sabaki pivots on the ball of the foot, "
            "keeps the hips under the shoulders, and finishes balanced and "
            "loaded. It is also the first defense: the same pivot that sets "
            "up a throw evades one, and the student who can turn 180 "
            "degrees in a fraction of a second is never where the "
            "opponent's attack lands."
        ),
        "how_it_works": (
            "Tai sabaki works by rotating the body's facing faster than the "
            "opponent can track. A full 180-degree pivot completed in about "
            "0.6 seconds is an angular velocity near 5.2 radians per "
            "second; the pivoting foot stays nearly fixed as the axis while "
            "the other foot travels a semicircle of radius about 0.45 "
            "meters - an arc of roughly 1.41 meters - swinging the hips "
            "from facing the opponent to facing away with the opponent's "
            "weight now loaded across the back. Pivoting on the ball of the "
            "foot keeps the turn fast and the knees safe; flat-footed "
            "turns grind the knee joint and telegraph the move. The drill "
            "progression runs solo pivots in place, then pivots with a "
            "partner holding the grips, then pivot-entries into actual "
            "throws (uchi-komi), and finally pivot-evasions against a "
            "partner's committed attack. The test is the landing: after the "
            "fastest pivot the student can make, the posture must still be "
            "shizen-hontai - balanced, upright, ready - because a pivot "
            "that ends off-balance is just a fancy way to fall down."
        ),
        "key_points": [
            "The 180-degree pivot is the core movement: facing exchange becomes back-to-chest throwing position in one turn.",
            "Pivot on the ball of the foot, hips under shoulders - flat-footed turns are slow, telegraphed, and hard on the knees.",
            "A 0.6-second pivot is about 5.2 radians per second; the free foot travels a 1.41-meter semicircle.",
            "Tai sabaki is offense and defense in one motion: the turn that loads your throw evades theirs.",
            "The landing is the test - finish every pivot balanced and upright, or the turn was just a fancy fall.",
        ],
        "requirements": [
            "A mat with room to pivot a full turn without contacting anyone.",
            "Bare feet: the ball-of-foot pivot requires mat grip and foot sensitivity.",
            "A partner for the grip-connected and evasion stages.",
            "Knee awareness: any knee pain during pivots means the form is wrong - stop and correct.",
            "Hundreds of slow perfect pivots before any fast ones; speed without form is injury.",
        ],
        "standards": [
            "Kodokan tai sabaki: pivot on the forefoot with the hips stacked, per Kano's movement doctrine.",
            "Angular mechanics: the pivot is trained as a rotation about a fixed axis foot.",
            "Safety standard: knee tracking over the toes through every turn; pain is a stop signal.",
        ],
        "citations": [CIT_KANO, CIT_INOKUMA],
        "sig_lens": (
            "The Signature read: tai sabaki is the Signature turn - the "
            "body rewriting its facing mid-sentence. Where the attack "
            "writes a straight line, the Signature pivot files a circle "
            "around it: maximum efficiency, minimum travel, and the "
            "opponent's force arriving at an empty address."
        ),
    },

    {
        "key": "footwork",
        "name": "Ayumi Ashi and Tsugi Ashi: Judo Footwork",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Footwork is how judo moves, and the art teaches two named "
            "steps before anything else: ayumi ashi, the normal walking "
            "step, and tsugi ashi, the following step where the rear foot "
            "chases the lead foot without ever crossing. The rule behind "
            "both is the same - the feet never cross, because crossed feet "
            "cannot change direction and a crossed stance is a standing "
            "invitation to de ashi harai. In tsugi ashi the lead foot steps "
            "and the trailing foot follows to just behind it, keeping the "
            "stance width constant and the body always ready to pivot, "
            "attack, or defend in any direction. Beginners bounce, cross "
            "their feet, and take steps so large they must pause between "
            "them; trained footwork glides - small quick steps, weight "
            "low, the head level as if sliding on rails. Every throw's "
            "entry is footwork first: the feet arrive, then the hips turn, "
            "then the hands work. Students who neglect the steps discover "
            "that their throws work in drilling and die in randori, "
            "because randori is footwork with throws attached."
        ),
        "how_it_works": (
            "Judo footwork works by keeping the stance recoverable at every "
            "instant. A tsugi ashi step of about 0.5 meters taken at a "
            "cadence of two steps per second covers 30 meters in a 30-second "
            "drill - sixty small controlled steps with the base of support "
            "never narrower than the starting stance. Because the feet never "
            "cross, the center of mass always projects between them, so a "
            "sudden attack or a sudden opening can be answered without a "
            "recovery step. The low glide matters for speed: lifting the "
            "feet high wastes the step's time in the air, while sliding "
            "keeps contact and readiness. Drills run the length of the mat: "
            "forward tsugi ashi, backward, sideways both ways, then "
            "diagonal, then with a partner in grips mirroring each other, "
            "then with the partner attacking at random so the feet learn to "
            "answer without the mind. The instructor's check is the head: "
            "if it bobs up and down, the steps are too big and the weight "
            "is bouncing instead of gliding."
        ),
        "key_points": [
            "Tsugi ashi: the rear foot follows the lead foot and never crosses - crossed feet cannot change direction.",
            "Ayumi ashi is normal walking adapted: small steps, weight low, head level as if gliding on rails.",
            "Sixty half-meter steps at two per second cover 30 meters in a 30-second drill with the stance never narrowing.",
            "The feet arrive first, then the hips turn, then the hands work - every throw entry is footwork before technique.",
            "Drill forward, backward, sideways, and diagonal, then mirrored with a partner, then against random attacks.",
        ],
        "requirements": [
            "A full mat length of clear floor for traveling drills.",
            "Bare feet with attention to sliding without stubbing toes.",
            "A partner for the mirrored and reactive stages.",
            "An instructor or mirror to check the head line: bobbing means the steps are too big.",
            "Patience with tedium: footwork is the least exciting and most decisive skill in judo.",
        ],
        "standards": [
            "Kodokan movement doctrine: ayumi ashi and tsugi ashi as the base gaits, feet never crossing.",
            "Stance integrity: the support base never narrows below the starting width during travel.",
            "Randori readiness: footwork must function at speed against unscripted attacks before throws are trusted.",
        ],
        "citations": [CIT_KANO, CIT_INOKUMA],
        "sig_lens": (
            "The Signature read: footwork is the Signature ledger in "
            "motion - every step an entry, none of them crossed out. The "
            "feet never cross because the Signature account is never "
            "overdrawn: balance kept in reserve on every step, ready to "
            "spend in any direction the moment demands."
        ),
    },
    {
        "key": "kumikata",
        "name": "Kumikata: Gripping the Judo Uniform",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Kumikata (gripping, 組み方) is the fight before the fight: the "
            "contest for the grips on the opponent's gi that decides which "
            "throws are even possible. The standard grip is one hand on the "
            "opponent's lapel and one on the sleeve, and from that "
            "connection everything flows - kuzushi travels through the "
            "grips, the entry turns around them, and the throw finishes "
            "with them. Grip fighting is its own skill with its own "
            "tactics: winning the dominant grip (high on the lapel, "
            "controlling the sleeve) while denying it, breaking grips with "
            "sharp two-on-one actions, and attacking the instant a grip is "
            "won before the opponent resets. With four standard grip points "
            "available - two lapels, two sleeves - there are six basic "
            "two-hand combinations, and the advanced game adds over-the-"
            "back, belt, and Georgian variations. Beginners grab and hold; "
            "trained judoka grip, attack, release, and re-grip in a "
            "continuous cycle, because a static grip is a handle the "
            "opponent will use against you."
        ),
        "how_it_works": (
            "Kumikata works as a connection system and a timing game. The "
            "lapel grip transmits push-pull kuzushi to the opponent's "
            "shoulders; the sleeve grip steers the arm that would post or "
            "block. Four grip points yield six two-hand combinations, and "
            "each combination unlocks a family of throws while locking "
            "others - the high lapel grip feeds seoi nage and uchi mata, "
            "the double-sleeve feeds foot sweeps. Grip fighting runs on "
            "probabilities: in a twenty-exchange grip battle where each "
            "exchange is won with probability 0.55 by the better gripper, "
            "the expected haul is eleven exchanges - a real, bankable edge "
            "that compounds over a match. The standard drill is grip "
            "randori: partners fight only for grips, no throws, resetting "
            "when one wins dominant position. The technical keys are "
            "grip-breaking with the whole body (never arm-wrestling a grip "
            "off), immediate attack off a won grip, and constant motion - "
            "the hands are busiest in the seconds before the throw, not "
            "during it."
        ),
        "key_points": [
            "Standard grip: one hand lapel, one hand sleeve - kuzushi travels through the grips to the opponent's shoulders.",
            "Four grip points make six basic two-hand combinations; each combination unlocks some throws and locks others.",
            "Grip fighting is a probability game: winning 55 percent of twenty exchanges banks eleven - a compounding match edge.",
            "Break grips with the whole body, never by arm-wrestling; attack the instant a dominant grip is won.",
            "Grip, attack, release, re-grip in a continuous cycle - a static grip is a handle for the opponent.",
        ],
        "requirements": [
            "A gi with sturdy lapels and sleeves - grip training destroys weak uniforms.",
            "Short nails and no jewelry; grip fighting puts the hands under real load.",
            "A partner for grip randori: grips only, no throws, reset on dominant position.",
            "Hand and forearm conditioning built gradually; grip work is demanding on tendons.",
            "Knowledge of the contest rules on gripping: current IJF rules penalize prolonged non-combativity and certain grip breaks.",
        ],
        "standards": [
            "Kodokan kumikata: the standard lapel-and-sleeve engagement as the base of throwing technique.",
            "Combinatorics of grips: four points, six two-hand combinations, each mapped to its throw families.",
            "IJF Sport and Organisation Rules 2024-2025 govern legal grips and grip-fighting penalties in competition.",
        ],
        "citations": [CIT_KANO, CIT_DAIGO, CIT_IJF],
        "sig_lens": (
            "The Signature read: kumikata is where the Signature gets "
            "signed - the grip is the pen, the gi is the paper. The "
            "Signature Way treats every grip exchange as a negotiation of "
            "terms: win the dominant grip and you hold the pen; lose it "
            "and you are being written. Grip, attack, release, re-grip - "
            "the signature is renewed every second."
        ),
    },
    {
        "key": "de_ashi_harai",
        "name": "De Ashi Harai: Advancing Foot Sweep",
        "group": "Nage Waza",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "De ashi harai (advancing foot sweep, 出足払) is the first throw "
            "most students learn, and the purest lesson in timing in all of "
            "judo. As the opponent steps forward, the student sweeps the "
            "advancing foot sideways just as it is about to take weight - "
            "not with force, but with timing, brushing the foot out from "
            "under a body that has already committed its balance to it. The "
            "hands pull the opponent's upper body in the direction of the "
            "sweep while the sweeping foot - using the sole near the ankle, "
            "low and fast - brushes uke's foot laterally off the mat. "
            "Because the foot is swept while it is moving and unweighted, "
            "the throw needs almost no strength; done with perfect timing "
            "it feels like the opponent fell over nothing. That is the "
            "lesson: judo is not about overpowering the step but about "
            "arriving exactly when the step is vulnerable. It is an ashi-"
            "waza (foot technique) and the gateway to the whole sweeping "
            "family."
        ),
        "how_it_works": (
            "De ashi harai works on the stepping cycle. An opponent walking "
            "forward steps about once every 1.1 seconds, and each foot "
            "spends roughly 0.25 seconds swinging through the air - a sweep "
            "window about 22.7 percent of the stride. The sweep must land "
            "inside that window, contacting the foot while it is moving and "
            "before it plants and takes weight; a planted foot is a rooted "
            "foot and the sweep bounces off. The mechanics are a lateral "
            "brush: the sweeping sole contacts near uke's ankle and drives "
            "sideways, while the hands pull the shoulders in the same "
            "lateral direction - kuzushi and sweep cooperating so the "
            "support vanishes exactly as the weight arrives. Contact lasts "
            "about 0.08 seconds; the sweep is a whip, not a push. Drills "
            "start with a partner walking in a straight line while the "
            "student times the brush without throwing, then add the pull, "
            "then the full throw at walking speed, then in moving randori. "
            "The tell of mastery is the sound: a clean de ashi harai is "
            "nearly silent, because there was no collision - only timing."
        ),
        "key_points": [
            "Sweep the advancing foot while it is moving and unweighted - the window is about 0.25 seconds, 22.7 percent of the stride.",
            "Brush with the sole near the ankle, low and fast; contact lasts about 0.08 seconds - a whip, not a push.",
            "The hands pull the shoulders laterally in the sweep's direction: kuzushi and sweep must cooperate.",
            "Perfect timing needs almost no strength; a silent throw means there was no collision, only timing.",
            "Drill the timing brush first without throwing, then add the pull, then full throws at rising speed.",
        ],
        "requirements": [
            "Reliable yoko ukemi on both sides - the partner falls sideways from this throw.",
            "A partner who walks naturally; the drill fails if the steps are faked or telegraphed.",
            "Mat space to travel in a straight line for the walking drills.",
            "Timing before power: any use of force to compensate for late timing is corrected immediately.",
            "An instructor to verify the sweep contacts the moving foot, never a planted one.",
        ],
        "standards": [
            "Kodokan ashi-waza: de ashi harai as the fundamental foot sweep, classified among the 67 throws.",
            "Sweep window: contact during the swing phase, before weight transfer completes.",
            "Uke safety: the lateral fall is absorbed by trained yoko ukemi.",
        ],
        "citations": [CIT_KANO, CIT_DAIGO],
        "sig_lens": (
            "The Signature read: de ashi harai is the Signature lesson in "
            "timing over force - the throw that proves maximum efficiency "
            "is a clock, not a muscle. The Signature Way files this one "
            "first among throws because it signs the whole philosophy: "
            "arrive exactly when the step is vulnerable, and nothing needs "
            "overpowering."
        ),
    },
    {
        "key": "o_soto_gari",
        "name": "O Soto Gari: Major Outer Reap",
        "group": "Nage Waza",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "O soto gari (major outer reap, 大外刈) is the iconic judo throw "
            "- the powerful reap of the opponent's leg from the outside "
            "that appears in every highlight reel. The student steps deep "
            "to the outside of the opponent's leg, drives the opponent's "
            "upper body backward with the grips, and reaps the supporting "
            "leg out from behind with the back of the leg, like a scythe. "
            "It is the textbook marriage of kuzushi and technique: the "
            "hands break balance to the rear corner while the leg removes "
            "the support, and the opponent falls flat on the back with "
            "nowhere to post. As an ashi-waza it belongs to the reap family "
            "(gari), distinct from the sweeps (harai): where a sweep "
            "brushes a moving foot, a reap drives through a weighted leg "
            "with real force. Beginners love it for its power; instructors "
            "love it for what it teaches about driving with the hips and "
            "committing the body, because a half-hearted o soto gari "
            "collapses into a clinch."
        ),
        "how_it_works": (
            "O soto gari works as a lever and a drive. The hands pull the "
            "opponent's shoulders backward - kuzushi to the rear - while the "
            "reaping leg swings through the opponent's supporting leg. The "
            "reaping leg drives its 300-newton force through at about 0.70 "
            "meters below the hip, generating roughly 210 newton-meters "
            "of torque at the hip, and that torque arrives exactly as the "
            "opponent's weight sits on the reaped leg, so the support "
            "vanishes under load. The chest drives forward into the "
            "opponent throughout - the throw is powered by the hips "
            "driving through, not by the leg swinging alone. The head "
            "turns away from the reap to keep the spine aligned, and the "
            "reaping leg follows through so the student lands balanced and "
            "ready. Drilled first as a static reap against a partner "
            "standing on one leg, then with the rear-kuzushi pull, then "
            "from movement, then in randori. The partner's landing is a "
            "full back fall - koho ukemi at speed - which is why this "
            "throw is never practiced before the back breakfall is solid."
        ),
        "key_points": [
            "Drive the shoulders backward with the grips while the leg reaps the supporting leg from behind - kuzushi and reap are one action.",
            "The reaping leg is a 0.85-meter lever: 300 newtons through it makes about 210 newton-meters of torque at the hip.",
            "Power comes from the hips driving through, not the leg swinging alone; the chest stays on the opponent.",
            "Reap the weighted leg - a reap is a drive through support, distinct from a sweep's brush of a moving foot.",
            "The partner takes a full-speed back fall: koho ukemi must be solid before this throw is ever practiced.",
        ],
        "requirements": [
            "Solid koho ukemi in the partner - o soto gari lands uke flat on the back at speed.",
            "Rear-corner kuzushi with the grips before the reap is attempted.",
            "Hip flexibility for the deep outside step without losing posture.",
            "A mat with space to fall backward a full body length.",
            "An instructor checking the drive: no hip commitment, no throw - half-hearted attempts are stopped.",
        ],
        "standards": [
            "Kodokan ashi-waza: o soto gari classified among the 67 throws, in the reap (gari) family.",
            "Lever mechanics: the reap applies force through the leg's full length with the hip driving.",
            "Uke safety: full koho ukemi required; the throw is not taught before the breakfall.",
        ],
        "citations": [CIT_KANO, CIT_DAIGO, CIT_INOKUMA],
        "sig_lens": (
            "The Signature read: o soto gari is the Signature scythe - the "
            "rear corner kuzushi writes the sentence and the reap signs it. "
            "The Signature Way admires this throw for its honesty: total "
            "commitment of the hips, no half measures. Maximum efficiency "
            "does not mean minimum effort - it means no wasted effort, and "
            "this throw wastes none."
        ),
    },
    {
        "key": "o_goshi",
        "name": "O Goshi: Major Hip Throw",
        "group": "Nage Waza",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "O goshi (major hip throw, 大腰) is the first hip throw and the "
            "purest expression of koshi-waza: the student turns 180 degrees "
            "into the opponent, loads the opponent's hips onto their own "
            "hip, and throws by straightening the legs and pulling the "
            "opponent over the hip fulcrum. The entry is the lesson - a "
            "deep tai sabaki pivot that places the hips below the "
            "opponent's hips, the throwing arm wrapping around the back to "
            "the far hip, the pulling arm drawing the opponent tight to the "
            "chest. Then the legs extend, the body bends forward, and the "
            "opponent rotates over the hip and lands in front. It is the "
            "throw instructors use to teach the hip as a fulcrum, the "
            "concept that unlocks the entire koshi-waza family: harai "
            "goshi, hane goshi, tsurikomi goshi, uki goshi. Beginners try "
            "to muscle it with the arms; the correction is always the same "
            "- get the hips lower and let the legs do the lifting."
        ),
        "how_it_works": (
            "O goshi works as a wheel over a fulcrum. The student's hip, "
            "loaded at about 0.95 meters, becomes the axle; the opponent's "
            "70-kilogram body rotates around it. The entry bends the knees "
            "about 0.25 meters to get the hips under the opponent's center "
            "of mass - this is non-negotiable, because a fulcrum above the "
            "load cannot lift it. The lift raises the opponent about 0.35 "
            "meters, costing roughly 240 joules of work (70 kg × 9.81 × "
            "0.35 m), all supplied by the quadriceps and glutes extending, "
            "not by the arms pulling. The pulling arm keeps the opponent's "
            "chest glued to the thrower's back so the bodies rotate as one "
            "mass; any gap lets the opponent slip off the hip. The finish "
            "bends the torso forward, guiding the rotation down to the mat "
            "in front. Drilled as uchi-komi (fit-in repetitions) by the "
            "hundreds before any full throw, because the entry - pivot, "
            "hips under, arm around - is the throw, and the lift is just "
            "the receipt."
        ),
        "key_points": [
            "The hip is the fulcrum: pivot 180 degrees, bend the knees about 0.25 meters, and load the opponent below their center of mass.",
            "The legs do the lifting - about 240 joules for a 70-kilogram opponent raised 0.35 meters - never the arms.",
            "The pulling arm glues the opponent's chest to your back; any gap lets them slip off the hip.",
            "A fulcrum above the load cannot lift it: hips low is the whole correction for a muscled, failing o goshi.",
            "Drill the entry as uchi-komi by the hundreds; the fit-in is the throw, the lift is the receipt.",
        ],
        "requirements": [
            "Reliable mae ukemi in the partner - o goshi lands uke forward.",
            "A correct 180-degree tai sabaki pivot; the throw cannot be built on a bad turn.",
            "Leg strength for the lift, built through uchi-komi volume rather than weight training.",
            "A gi grip on the back that holds through the rotation.",
            "An instructor checking hip height: hips must finish below the opponent's hips.",
        ],
        "standards": [
            "Kodokan koshi-waza: o goshi as the foundational hip throw among the 67 throws.",
            "Fulcrum mechanics: the hip axle must sit below the opponent's center of mass.",
            "Uchi-komi standard: the entry is drilled to automaticity before full throws are attempted.",
        ],
        "citations": [CIT_KANO, CIT_DAIGO],
        "sig_lens": (
            "The Signature read: o goshi is the Signature fulcrum - the hip "
            "as the axle of the whole art. The Signature Way files hip "
            "throws under perfect economy: the legs, the body's strongest "
            "engines, do the lifting while the arms merely sign the "
            "paperwork. Hips low, load centered, nothing wasted."
        ),
    },
    {
        "key": "seoi_nage",
        "name": "Seoi Nage: Shoulder Throw",
        "group": "Nage Waza",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Seoi nage (shoulder throw, 背負投) is judo's most famous throw "
            "and its most complete technique: the student pivots 180 "
            "degrees, drops under the opponent's arm, loads the opponent "
            "across the shoulders and upper back, and throws forward over "
            "the shoulder. In the drop-knee form (seoi otoshi) the student "
            "drops to one or both knees for extra depth; in the standing "
            "form (ippon seoi nage) the throwing arm threads under the "
            "opponent's armpit and grips the lapel high. It demands "
            "everything at once - kuzushi to the front corner, a blinding "
            "tai sabaki entry, hips below the opponent's belt, and a "
            "committed finish - which is why it is both the throw every "
            "beginner wants to learn and the throw that takes a decade to "
            "master. Champions build careers on seoi nage because when the "
            "entry is perfect, size stops mattering: the shoulder becomes "
            "a catapult and the opponent's own forward pressure does half "
            "the work."
        ),
        "how_it_works": (
            "Seoi nage works as a loaded catapult. The pivot places the "
            "student's back against the opponent's chest with the hips sunk "
            "below the opponent's belt line; the opponent's 70-kilogram "
            "mass drapes across the shoulders with a torque arm of about "
            "0.35 meters, generating roughly 240 newton-meters of torque "
            "about the shoulder axis. The throw fires by extending the legs "
            "and rotating the torso forward - the shoulder acts as the "
            "catapult arm and the opponent's forward kuzushi supplies the "
            "initial direction. The drop-knee variant adds about 0.3 "
            "meters of entry depth, which is why smaller judoka favor it "
            "against taller opponents: depth substitutes for height. The "
            "pulling hand never stops pulling through the finish; stopping "
            "the pull mid-throw strands the opponent on the back and "
            "collapses the thrower. Drilled as nage-komi (throwing "
            "repetitions) only after the entry is clean, because a fast "
            "bad entry under a loaded opponent is how shoulders and knees "
            "are injured."
        ),
        "key_points": [
            "Pivot 180 degrees and sink the hips below the opponent's belt: depth is the throw, everything else is delivery.",
            "The shoulder is the catapult arm - about 240 newton-meters of torque for a 70-kilogram opponent on a 0.35-meter arm.",
            "Kuzushi to the front corner first; the opponent's forward pressure does half the work when the entry is perfect.",
            "Drop-knee form (seoi otoshi) adds about 0.3 meters of depth - the smaller judoka's answer to taller opponents.",
            "Never stop pulling through the finish; a stalled pull strands the opponent on your back and collapses the throw.",
        ],
        "requirements": [
            "A flawless 180-degree pivot with the hips finishing low - verified by an instructor before loading.",
            "Reliable zenpo kaiten ukemi in the partner: seoi nage launches uke with forward momentum.",
            "Shoulder and knee health; the loaded entry stresses both, and pain is a stop signal.",
            "Hundreds of uchi-komi entries before nage-komi throwing repetitions begin.",
            "A gi with a strong lapel - the high grip takes the throw's full load.",
        ],
        "standards": [
            "Kodokan te-waza: seoi nage (standing and drop-knee forms) among the 67 throws.",
            "Catapult mechanics: hips below the load, shoulder as the throwing axis, continuous pull through the finish.",
            "Progression standard: entry automaticity before loaded throwing repetitions.",
        ],
        "citations": [CIT_KANO, CIT_DAIGO, CIT_INOKUMA],
        "sig_lens": (
            "The Signature read: seoi nage is the Signature catapult - the "
            "body's own structure filed as a launching engine. The "
            "Signature Way honors this throw as the complete signature: "
            "kuzushi, entry, load, and launch all signed in one motion, "
            "with the opponent's own pressure co-signing the document."
        ),
    },
    {
        "key": "o_uchi_gari",
        "name": "O Uchi Gari: Major Inner Reap",
        "group": "Nage Waza",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "O uchi gari (major inner reap, 大内刈) attacks the leg the "
            "opponent stands on from the inside: the student steps in "
            "close, hooks the reaping leg behind the opponent's supporting "
            "leg, and drives the opponent backward over the reaped leg. "
            "Where o soto gari reaps from the outside, o uchi gari comes "
            "from between the legs - a shorter, more intimate entry that "
            "pairs naturally with forward throws, because the opponent who "
            "defends a seoi nage by leaning back walks straight into the "
            "inner reap. The hands drive the upper body backward while the "
            "leg reaps through, and the throw finishes with the student "
            "driving chest-to-chest through the opponent. It is the "
            "cornerstone of combination throwing: o uchi gari to seoi nage, "
            "seoi nage to o uchi gari, o uchi gari to uchi mata - the inner "
            "reap is the hinge that swings the combination both ways."
        ),
        "how_it_works": (
            "O uchi gari works by removing the inside support while driving "
            "the top backward. The reaping leg hooks behind the opponent's "
            "leg and drives through at about 25 degrees from vertical; a "
            "280-newton reap resolves into roughly 118 newtons of horizontal "
            "drive and 254 newtons of vertical lift (280 × sin 25°, 280 × "
            "cos 25°), so the leg is simultaneously pushed back and scooped "
            "up - the support does not just move, it leaves. Meanwhile the "
            "hands push the shoulders backward, kuzushi to the rear, and "
            "the chest drives through the opponent's chest so the bodies "
            "move as one falling mass. The entry is close: the student's "
            "hips must be nearly touching the opponent's, because a gap "
            "turns the reap into a kick at air. Drilled from a clinch "
            "first, then with the forward-throw combination entries, then "
            "in randori - and the classic beginner error is reaping with "
            "the foot instead of driving with the whole leg, which the "
            "instructor corrects by demanding the follow-through finish "
            "with the reaping leg past the opponent's far hip."
        ),
        "key_points": [
            "Hook behind the supporting leg from the inside and drive through at about 25 degrees: 280 newtons resolves to 118 newtons back and 254 newtons up.",
            "The reap scoops as well as pushes - the support does not just move, it leaves.",
            "Hands drive the shoulders backward while the chest drives through: kuzushi, reap, and drive are one action.",
            "Enter hip-to-hip; any gap turns the reap into a kick at empty air.",
            "The inner reap is the hinge of combinations: o uchi gari to seoi nage and back, the swing both ways.",
        ],
        "requirements": [
            "Solid koho ukemi in the partner - the backward fall is sudden.",
            "A close clinch entry; the technique fails at arm's length.",
            "Hip flexibility for the deep inside step without posture collapse.",
            "Mastery of o soto gari first: the outer reap teaches the reaping action the inner reap refines.",
            "An instructor checking the reap angle: too vertical is a lift, too horizontal is a trip.",
        ],
        "standards": [
            "Kodokan ashi-waza: o uchi gari among the 67 throws, in the reap (gari) family.",
            "Reap vector: driven through at approximately 25 degrees from vertical, combining drive and scoop.",
            "Combination standard: o uchi gari is drilled as the hinge between forward and backward attacks.",
        ],
        "citations": [CIT_KANO, CIT_DAIGO],
        "sig_lens": (
            "The Signature read: o uchi gari is the Signature hinge - the "
            "inside reap that swings the combination both ways. The "
            "Signature Way files it as the art of the second sentence: the "
            "first attack writes the setup, the inner reap signs the "
            "reversal, and the opponent's defense becomes the signature on "
            "their own fall."
        ),
    },
    {
        "key": "ko_uchi_gari",
        "name": "Ko Uchi Gari: Minor Inner Reap",
        "group": "Nage Waza",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Ko uchi gari (minor inner reap, 小内刈) is o uchi gari's "
            "smaller, quicker sibling: instead of reaping the supporting "
            "leg with a deep drive, the student flicks the opponent's "
            "advancing foot from the inside with a short, sharp reap of the "
            "foot and ankle. It is a minor technique (ko) because the "
            "lever is short and the force is small - but it is a giant of "
            "combination throwing, because its speed lets it strike in the "
            "gaps between bigger attacks. The classic sequence is o uchi "
            "gari threatened big, the opponent steps to defend, and ko uchi "
            "gari flicks the stepping foot before it lands. It is also a "
            "superb counter: when the opponent attacks forward, their "
            "advancing foot is already moving into the flick's path. The "
            "hands do the real work - pulling the opponent's weight onto "
            "the targeted foot at the exact instant of the flick - which "
            "teaches the deepest lesson of ashi-waza: the foot only "
            "finishes what the hands started."
        ),
        "how_it_works": (
            "Ko uchi gari works on speed and the stepping cycle. The flick "
            "travels about 0.25 meters of arc in roughly 0.12 seconds - a "
            "tip speed near 2.08 meters per second - striking the inside of "
            "the opponent's advancing foot just as weight begins to "
            "transfer onto it. The hands pull the opponent's shoulders "
            "toward the targeted foot, loading it at the instant of "
            "contact; a flick against an unweighted foot does nothing, "
            "while the same flick against a loading foot topples the "
            "step. Because the action is small, it can be thrown from "
            "almost any grip and recovered instantly if it misses - the "
            "student is never out of position after a failed ko uchi gari, "
            "which is what makes it the ideal probing attack. Drilled as a "
            "follow-up: big o uchi gari, partner steps out, immediate ko "
            "uchi flick on the step - then the reverse, then in randori "
            "where the student is tasked with landing three clean flicks "
            "before attempting any big throw."
        ),
        "key_points": [
            "Flick the advancing foot from the inside: 0.25 meters of arc in 0.12 seconds, tip speed about 2.08 meters per second.",
            "Strike as weight transfers onto the foot - a flick against an unweighted foot does nothing.",
            "The hands load the targeted foot at the instant of the flick; the foot only finishes what the hands started.",
            "Small and recoverable: a missed ko uchi gari never leaves you out of position, making it the ideal probing attack.",
            "Drill it as the follow-up - big o uchi threatened, step defended, instant flick - then reversed.",
        ],
        "requirements": [
            "Reliable yoko ukemi in the partner on both sides.",
            "Command of o uchi gari first; the minor reap is the major reap miniaturized.",
            "Ankle mobility for the short sharp flick without involving the knee.",
            "A partner who steps naturally in the combination drills.",
            "Timing discipline: flicking late at a planted foot is corrected at once.",
        ],
        "standards": [
            "Kodokan ashi-waza: ko uchi gari among the 67 throws, the minor (ko) inner reap.",
            "Flick mechanics: short arc, high tip speed, contact during weight transfer.",
            "Combination standard: drilled as the second attack in o-uchi/ko-uchi sequences.",
        ],
        "citations": [CIT_KANO, CIT_DAIGO],
        "sig_lens": (
            "The Signature read: ko uchi gari is the Signature footnote - "
            "small print that changes the contract. The Signature Way "
            "loves the minor reap because it proves the philosophy at "
            "minimum scale: perfect timing, minimum force, and the "
            "opponent's own step signing the fall."
        ),
    },
    {
        "key": "hiza_guruma",
        "name": "Hiza Guruma: Knee Wheel",
        "group": "Nage Waza",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Hiza guruma (knee wheel, 膝車) is the elegant wheel of "
            "ashi-waza: the student blocks the opponent's knee with the "
            "sole of the foot while the hands wheel the upper body over "
            "it. As the opponent steps forward, the student places the "
            "foot against the side of the advancing knee - not kicking it, "
            "but posting it as a fixed point - and pulls the opponent's "
            "shoulders in a great circle over that point, so the body "
            "rotates like a wheel around the blocked knee. The beauty of "
            "the technique is its purity: the foot does not sweep or reap, "
            "it simply stops the knee, and the hands do all the throwing. "
            "It is one of the oldest throws in the Kodokan curriculum and "
            "the clearest demonstration of kuzushi as rotation rather than "
            "force. Beginners learn from it that a well-placed foot is "
            "worth more than a strong leg, and the wheel image - uke "
            "turning cleanly over the posted knee - stays with students "
            "for the rest of their judo lives."
        ),
        "how_it_works": (
            "Hiza guruma works as a wheel around a fixed axle. The posted "
            "foot fixes the opponent's knee at about 0.5 meters of height; "
            "the hands then drive the shoulders in a circle, and the "
            "opponent's body rotates a quarter turn over the knee - the "
            "knee contact travels an arc of (pi/2) × 0.5 meters, about "
            "0.785 meters of guided rotation. The block must be a post, "
            "not a kick: the sole meets the knee with the leg relaxed, "
            "and the instant of contact is the instant the hands begin the "
            "wheel - block without the pull is just a foot in the way, and "
            "pull without the block drags the opponent forward harmlessly. "
            "Timing targets the advancing step, like de ashi harai, but "
            "the finish is completely different: where the sweep removes "
            "support, the wheel redirects the body's momentum over a new "
            "axle. Drilled walking in a line - partner steps, student posts "
            "and wheels - then from grips, then as a counter to forward "
            "pressure. The classic error is posting too high on the thigh, "
            "which turns the wheel into a shove; the sole belongs on the "
            "knee itself."
        ),
        "key_points": [
            "Post the sole against the advancing knee as a fixed axle - a post, never a kick.",
            "Wheel the shoulders in a great circle over the posted knee: a quarter turn, about 0.785 meters of guided rotation.",
            "Block and pull are simultaneous: the post without the wheel is a foot in the way, the wheel without the post is a harmless drag.",
            "The foot does not sweep or reap here - it stops the knee, and the hands do all the throwing.",
            "Post on the knee itself; posting high on the thigh turns the wheel into a shove.",
        ],
        "requirements": [
            "Yoko ukemi on the landing side - the wheel deposits uke sideways.",
            "A partner who steps forward naturally in the walking drills.",
            "Ankle and sole conditioning for clean posting without toe injuries.",
            "Instructor verification of the post height: sole on the knee, not the thigh or shin.",
            "Control of the wheeling pull: the partner must be guided over, never wrenched.",
        ],
        "standards": [
            "Kodokan ashi-waza: hiza guruma among the 67 throws, the knee-wheel archetype.",
            "Axle mechanics: the knee is fixed at approximately 0.5 meters while the body rotates over it.",
            "Uke safety: the wheeling pull guides the fall; the post never strikes.",
        ],
        "citations": [CIT_KANO, CIT_DAIGO, CIT_HARRISON],
        "sig_lens": (
            "The Signature read: hiza guruma is the Signature wheel - the "
            "purest filing of rotation over force. One posted foot, one "
            "great circle of the hands, and the opponent's own momentum "
            "signs the rotation. The Signature Way keeps this throw as "
            "the emblem of perfect economy: the foot does nothing but "
            "stand still, and that stillness throws a human being."
        ),
    },
    {
        "key": "tai_otoshi",
        "name": "Tai Otoshi: Body Drop",
        "group": "Nage Waza",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Tai otoshi (body drop, 体落) is the throw that drops the body "
            "as a roadblock: the student pivots 180 degrees like seoi nage, "
            "but instead of loading the opponent onto the back, drops low "
            "and extends one leg straight across the opponent's path as a "
            "tripping block, then pulls the opponent over it. The leg never "
            "sweeps or reaps - it is a static barrier, and the throw is "
            "entirely in the drop of the body weight and the pull of the "
            "hands. It is a te-waza (hand technique) by classification, "
            "because the hands do the throwing while the leg merely blocks. "
            "Tai otoshi is famously the rival of seoi nage: where the "
            "shoulder throw carries the load, the body drop lets gravity do "
            "the work, which makes it the technician's answer to larger "
            "opponents. The drop must be committed and low - a high, "
            "hesitant tai otoshi is just an invitation to be countered."
        ),
        "how_it_works": (
            "Tai otoshi works by dropping a barrier into the opponent's "
            "path and pulling them over it. The student drops the center "
            "of mass about 0.35 meters in roughly 0.27 seconds "
            "(sqrt(2 × 0.35 / 9.81)), extending the blocking leg across at "
            "ankle height - about 0.1 meters - while the hands pull the "
            "opponent's shoulders forward and down. The opponent trips "
            "over the extended leg with a pivot radius equal to their leg "
            "length, about 0.85 meters, and the body's forward momentum "
            "plus the downward pull rotates them cleanly over the block. "
            "The blocking leg must be straight and the foot flexed; a bent "
            "blocking leg collapses under the load. Crucially, the leg is "
            "placed, not swung - any sweeping motion reclassifies the "
            "technique and, worse, endangers the opponent's knee. Drilled "
            "from the pivot with a partner walking forward, then with "
            "increasing speed, then as the follow-up when seoi nage is "
            "blocked. The signature detail is the drop: the student must "
            "finish low enough that the blocking leg is truly across the "
            "path, not above it."
        ),
        "key_points": [
            "Pivot 180 degrees, drop the body about 0.35 meters in about 0.27 seconds, and block across at ankle height.",
            "The leg is a static barrier - placed, never swung; the hands and the drop do all the throwing, so it is a te-waza.",
            "The opponent trips over the block with a pivot radius of about 0.85 meters, their own momentum completing the throw.",
            "Keep the blocking leg straight with the foot flexed; a bent block collapses under the load.",
            "Commit low and fully - a high hesitant tai otoshi is an invitation to be countered.",
        ],
        "requirements": [
            "Zenpo kaiten ukemi in the partner - tai otoshi launches uke forward over the block.",
            "A correct pivot with the drop; instructors check that the student finishes genuinely low.",
            "Knee health for the dropping action; pain is a stop signal.",
            "Strict no-sweeping discipline: the blocking leg is placed, protecting the opponent's knee.",
            "Mastery of the seoi nage pivot first - tai otoshi is built on the same turn.",
        ],
        "standards": [
            "Kodokan te-waza: tai otoshi among the 67 throws - the hands throw, the leg blocks.",
            "Drop mechanics: approximately 0.35 meters of body drop timed with the forward pull.",
            "Safety standard: the blocking leg is placed statically; swinging at the knee is prohibited.",
        ],
        "citations": [CIT_KANO, CIT_DAIGO, CIT_INOKUMA],
        "sig_lens": (
            "The Signature read: tai otoshi is the Signature roadblock - "
            "gravity filed as the throwing engine. The Signature Way "
            "admires the economy: the leg does nothing but exist in the "
            "right place, the body drops, the hands sign, and physics "
            "executes the throw. Minimum action, maximum result."
        ),
    },
    {
        "key": "kesa_gatame",
        "name": "Kesa Gatame: Scarf Hold",
        "group": "Katame Waza",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Kesa gatame (scarf hold, 袈裟固) is the first pin every judoka "
            "learns and the foundation of all groundwork: from the side, "
            "the student wraps one arm around the opponent's head, threads "
            "the other arm under the opponent's near arm to grip the gi, "
            "and settles the chest heavily across the opponent's chest - "
            "the hold named for the diagonal sash of a Buddhist kesa robe. "
            "It is an osaekomi-waza (holding technique): pin the "
            "opponent's back to the mat and the contest clock starts - ten "
            "seconds of control scores waza-ari, twenty seconds scores "
            "ippon and ends the match. The pin works through weight "
            "distribution and the head-and-arm control: the wrapped head "
            "cannot turn into you, the trapped arm cannot post, and the "
            "chest pressure makes breathing laborious. Every escape the "
            "opponent attempts - bridging, shrimping, rolling - is answered "
            "by following the movement and re-settling the weight. Simple "
            "to learn, brutally hard to escape when done right."
        ),
        "how_it_works": (
            "Kesa gatame works by controlling the head and one arm while "
            "the chest supplies the weight. About 65 percent of the "
            "holder's upper-body weight settles across the opponent's "
            "chest with the head wrapped, which both restricts breathing "
            "and prevents the opponent from turning into the holder; the "
            "other arm threads under the near arm to grip the gi, removing "
            "the post the opponent would use to bridge. The scoring clock "
            "is the technique's engine: hold 10 seconds for waza-ari, 20 "
            "seconds for ippon - so the holder's entire game is "
            "immobility, answering each escape attempt by floating with it "
            "and re-settling. The classic escapes are the bridge-and-roll "
            "(answered by posting the far leg and widening the base) and "
            "the shrimp away (answered by following the hips and "
            "re-wrapping). Drilled as hold-down exchanges: one partner "
            "holds, the other escapes, timed rounds, switching roles. The "
            "beginner error is holding with the arms instead of the chest "
            "- arms tire in seconds, while chest weight is free and "
            "endless."
        ),
        "key_points": [
            "Wrap the head with one arm, thread the other under the near arm to the gi, and settle the chest across their chest.",
            "About 65 percent of upper-body weight goes across the opponent; arms guide, the chest holds - arms tire, weight is free.",
            "The wrapped head cannot turn in, the trapped arm cannot post: control the head and one arm and the body follows.",
            "Osaekomi scoring: 10 seconds waza-ari, 20 seconds ippon - the whole game is immobility against escape attempts.",
            "Answer bridges by widening the base and posting the far leg; answer shrimps by following the hips and re-settling.",
        ],
        "requirements": [
            "A partner willing to be held and to attempt realistic escapes.",
            "Chest pressure applied with control - the pin restricts breathing and must be released on tap or signal.",
            "Knowledge of the osaekomi clock: 10 seconds waza-ari, 20 seconds ippon under current rules.",
            "No neck cranks: the head is controlled, never twisted or torqued.",
            "Mat space for the escape exchanges, timed rounds with role switches.",
        ],
        "standards": [
            "Kodokan osaekomi-waza: kesa gatame as the foundational hold-down among katame-waza.",
            "IJF osaekomi scoring: 10 seconds waza-ari, 20 seconds ippon (2024-2025 rules).",
            "Safety standard: the hold is control, not a submission - release on tap, no spinal torque.",
        ],
        "citations": [CIT_KANO, CIT_INOKUMA, CIT_IJF],
        "sig_lens": (
            "The Signature read: kesa gatame is the Signature seal - the "
            "chest as the stamp pressed across the opponent. The Signature "
            "Way files the scarf hold as the first ground covenant: "
            "immobility as the signature, the clock as the witness, twenty "
            "seconds to close the document."
        ),
    },

    {
        "key": "harai_goshi",
        "name": "Harai Goshi: Sweeping Hip Throw",
        "group": "Nage Waza",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Harai goshi (sweeping hip throw, 払腰) is the hip throw with a "
            "sweep inside it: the student enters like o goshi - 180-degree "
            "pivot, hips loaded - but instead of lifting straight over the "
            "hip, sweeps the opponent's leg with their own leg while "
            "rotating. The sweeping leg travels a great arc, brushing "
            "uke's leg out as the hip turns, and the combination of hip "
            "fulcrum plus leg sweep makes it one of the most powerful "
            "throws in judo. It is the natural graduation from o goshi: "
            "once the student can load the hip, the sweep adds the "
            "finishing rotation that throws even a resisting opponent. The "
            "entry demands the same deep hips as o goshi, but the finish "
            "is all timing - the sweep must meet uke's leg exactly as the "
            "hip turns, and the most common failure is sweeping at air "
            "because the entry was too shallow. When it lands cleanly, "
            "harai goshi is spectacular: the opponent describes a full arc "
            "through the air."
        ),
        "how_it_works": (
            "Harai goshi works as a hip fulcrum with a sweeping assist. The "
            "pivot loads uke onto the hip at about 0.95 meters; then the "
            "sweeping leg - a lever about 0.8 meters long - travels a 120-"
            "degree arc (2.094 radians), covering roughly 1.68 meters of "
            "arc in about 0.35 seconds, a tip speed near 4.79 meters per "
            "second. The sweep contacts uke's leg and removes it at the "
            "same instant the hip rotates, so the opponent is simultaneously "
            "lifted over the fulcrum and swept from below - two throwing "
            "actions compounding. The hands pull the opponent's upper body "
            "in the direction of the sweep, keeping uke's weight committed "
            "to the swept leg. The entry depth is the whole technique: the "
            "hips must be below uke's belt before the sweep starts, or the "
            "sweep meets a leg that still has balance behind it. Drilled "
            "as uchi-komi with the sweep added in stages - hip load first, "
            "then the brushing contact, then the full arc - then nage-komi "
            "at increasing speed."
        ),
        "key_points": [
            "Enter like o goshi - deep hips below the belt - then sweep: hip fulcrum plus leg sweep compounding.",
            "The sweeping leg travels a 120-degree arc: about 1.68 meters in 0.35 seconds, tip speed near 4.79 meters per second.",
            "Sweep and hip turn are simultaneous: lifted over the fulcrum and swept from below at the same instant.",
            "The hands commit uke's weight to the swept leg; the entry depth decides whether the sweep meets balance or air.",
            "Build in stages: hip load, then brushing contact, then the full arc - never the full sweep before the hips are deep.",
        ],
        "requirements": [
            "Command of o goshi first; harai goshi is the hip throw graduated with a sweep.",
            "Reliable mae ukemi in the partner - the arc deposits uke forward with speed.",
            "Hip and hamstring flexibility for the sweeping arc without posture loss.",
            "An instructor checking entry depth: hips below the belt before any sweep.",
            "Sweep contact with control - brushing the leg, never kicking it.",
        ],
        "standards": [
            "Kodokan koshi-waza: harai goshi among the 67 throws, the sweeping hip archetype.",
            "Arc mechanics: approximately 120 degrees of sweep synchronized with the hip rotation.",
            "Progression standard: the hip load is mastered before the sweep is added.",
        ],
        "citations": [CIT_KANO, CIT_DAIGO],
        "sig_lens": (
            "The Signature read: harai goshi is the Signature compound - "
            "two throwing actions filed as one document, fulcrum and sweep "
            "signed together. The Signature Way treats it as the graduate "
            "course in perfect economy: the hip does the lifting it "
            "already knew, the leg adds the rotation it was born for, and "
            "nothing is spent twice."
        ),
    },
    {
        "key": "uchi_mata",
        "name": "Uchi Mata: Inner Thigh Throw",
        "group": "Nage Waza",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Uchi mata (inner thigh throw, 内股) is the throw of champions: "
            "the student pivots 180 degrees, lifts the opponent's inner "
            "thigh with their own thigh, and throws forward over the "
            "lifting leg. It is classified as ashi-waza, though it feels "
            "like a hip throw with a leg inside it - the lifting thigh "
            "scoops uke's inner thigh upward while the hands drive the "
            "upper body forward, and the opponent rotates over the lifting "
            "leg in a great wheel. More Olympic and World Championship "
            "finals have been decided by uchi mata than any other throw, "
            "because it works at every size: the lift exploits the "
            "opponent's forward kuzushi rather than the thrower's "
            "strength. The entry is demanding - the pivot must be deep, "
            "the supporting leg must be close to uke's, and the lift must "
            "catch the inner thigh, not the groin - but once the mechanics "
            "click, uchi mata becomes the throw that ends arguments."
        ),
        "how_it_works": (
            "Uchi mata works as a thigh lever with forward kuzushi. The "
            "pivot places the student's back to the opponent with the "
            "supporting leg tight against uke's leg; the lifting thigh "
            "drives up into uke's inner thigh, raising a 75-kilogram "
            "opponent about 0.25 meters - roughly 184 joules of work "
            "(75 × 9.81 × 0.25) - while the hands wheel the shoulders "
            "forward and down. The kuzushi is to the front: the opponent "
            "must already be falling forward onto the lifting leg, because "
            "the thigh can only redirect committed weight, not create it. "
            "The supporting foot pivots on the ball through the finish, "
            "letting the hips complete the rotation without knee strain. "
            "Contact is strictly the inner thigh - the lift lands on the "
            "thigh muscle, controlled and safe, never higher. Drilled as "
            "uchi-komi with the lift only (no throw) until the thigh "
            "placement is automatic, then nage-komi, then in combination "
            "with o uchi gari, which shares the entry and punishes the "
            "backward defense."
        ),
        "key_points": [
            "Pivot deep, lift the inner thigh with your thigh: raising 75 kilograms 0.25 meters costs about 184 joules.",
            "Kuzushi to the front first - the thigh redirects committed forward weight; it cannot create what is not there.",
            "The supporting leg stays tight to uke's; the pivot foot turns on the ball through the finish to protect the knee.",
            "Contact is the inner thigh muscle only - controlled, safe placement, never higher.",
            "Drill the lift without the throw until placement is automatic; pair it with o uchi gari to punish the backward defense.",
        ],
        "requirements": [
            "A deep reliable pivot with the hips finishing low.",
            "A partner with solid zenpo kaiten ukemi - uchi mata throws forward with authority.",
            "Thigh and hip flexibility for the lifting action.",
            "Strict placement discipline: inner thigh only, verified by an instructor.",
            "Command of the o uchi gari entry, which shares the combination game.",
        ],
        "standards": [
            "Kodokan ashi-waza: uchi mata among the 67 throws, the inner-thigh archetype.",
            "Lever mechanics: the lifting thigh redirects forward-committed weight over the supporting leg.",
            "Safety standard: lift placement on the inner thigh muscle; groin contact is a foul and a stop.",
        ],
        "citations": [CIT_KANO, CIT_DAIGO, CIT_INOKUMA],
        "sig_lens": (
            "The Signature read: uchi mata is the Signature wheel of the "
            "inner thigh - the champion's signature, filed at every level "
            "from local to Olympic. The Signature Way reads it as the "
            "proof that perfect economy beats raw strength: the opponent's "
            "own forward fall, redirected by one lifting thigh, signs the "
            "biggest throws in the sport."
        ),
    },
    {
        "key": "tomoe_nage",
        "name": "Tomoe Nage: Circle Throw",
        "group": "Nage Waza",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Tomoe nage (circle throw, 巴投) is the great sacrifice throw: "
            "the student falls to the back, plants a foot on the "
            "opponent's belt line, and throws the opponent in a circle "
            "overhead using the falling body weight plus the leg's push. "
            "Named for the tomoe - the comma-shaped swirl - because uke "
            "describes a circular arc through the air, it is the first "
            "sutemi-waza (sacrifice technique) most students learn, and "
            "the clearest lesson that in judo you may spend your own "
            "balance to buy the throw. The setup pulls the opponent "
            "forward; the instant their weight commits, the student drops, "
            "the foot plants at the belt, and the combined pull of the "
            "hands and push of the leg launches uke overhead. It is the "
            "classic answer to a stronger opponent who pushes: their push "
            "becomes the energy of their own flight. The risk is real - a "
            "failed tomoe nage leaves the student on the back - which is "
            "why it is taught as a committed technique: half-sacrifices "
            "fail, full ones fly."
        ),
        "how_it_works": (
            "Tomoe nage works by converting the thrower's falling mass "
            "into the opponent's circular flight. The foot plants at the "
            "belt line, about 0.95 meters up; the hands pull the opponent "
            "forward and down while the leg extends, and uke travels a "
            "semicircular arc of radius 0.95 meters - about 2.98 meters of "
            "guided flight (pi × 0.95) - landing beyond the thrower's head. "
            "The timing is everything: the drop must begin the instant the "
            "opponent's weight commits forward, because the technique "
            "spends the thrower's balance and cannot be recovered "
            "mid-fall. The planted foot pushes, never kicks - the sole "
            "stays flat on the belt line and extends the leg, protecting "
            "uke's ribs. The hands guide the circle: pulling down and "
            "around, not just down, which is what makes the flight circular "
            "instead of a straight dump. Drilled first with the partner "
            "stepping in and the student only dropping and planting (no "
            "throw), then the full circle at low speed, then in randori "
            "against forward pressure."
        ),
        "key_points": [
            "Fall to the back, plant the foot at the belt line (about 0.95 meters), and circle uke overhead: about 2.98 meters of guided flight.",
            "The drop begins the instant the opponent's weight commits forward - the technique spends your balance and cannot be recovered mid-fall.",
            "The foot pushes, never kicks: sole flat on the belt line, leg extending, ribs protected.",
            "The hands guide the circle - pull down and around, not just down; that is what makes the flight circular.",
            "Commit fully or not at all: half-sacrifices fail and leave you on your back; full ones fly.",
        ],
        "requirements": [
            "Excellent zenpo kaiten ukemi in the partner - the circular flight is long and fast.",
            "A clean forward pull that genuinely commits the opponent's weight before the drop.",
            "Core and leg strength for the drop-and-extend under load.",
            "An instructor verifying the plant: sole flat at the belt line, never a kick.",
            "Courage drilled progressively: plant-only reps, then slow full throws, then randori.",
        ],
        "standards": [
            "Kodokan sutemi-waza: tomoe nage among the 67 throws, the circle-throw archetype.",
            "Circle mechanics: the opponent travels a semicircular arc of approximately pi × 0.95 meters.",
            "Safety standard: the planting foot pushes with a flat sole; kicking is prohibited.",
        ],
        "citations": [CIT_KANO, CIT_DAIGO, CIT_OHLENKAMP],
        "sig_lens": (
            "The Signature read: tomoe nage is the Signature sacrifice - "
            "your own balance spent deliberately to buy the throw. The "
            "Signature Way files it as the economics of courage: maximum "
            "efficiency sometimes means spending everything at once, and "
            "the circle it writes in the air is the most beautiful "
            "signature in judo."
        ),
    },
    {
        "key": "kami_shiho_gatame",
        "name": "Kami Shiho Gatame: Upper Four Corner Hold",
        "group": "Katame Waza",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Kami shiho gatame (upper four corner hold, 上四方固) is the "
            "north-south pin: the holder kneels above the opponent's head, "
            "chest-to-chest with the bodies forming a straight line, arms "
            "threading under the opponent's arms to grip the belt or gi, "
            "controlling all four corners of the body - both shoulders and "
            "both hips. From this top position the holder's weight presses "
            "straight down through the opponent's torso, and the underhook "
            "control on both sides removes every bridging and turning "
            "escape. It is the pin that teaches the meaning of shiho "
            "(four corners): control the four points and the body between "
            "them cannot move. The hold is reached most often when a throw "
            "lands the student past the opponent's head, or from a "
            "scramble where the student circles to the top. Like all "
            "osaekomi, ten seconds scores waza-ari and twenty scores "
            "ippon - and from kami shiho gatame, twenty seconds feels very "
            "long to the person on the bottom."
        ),
        "how_it_works": (
            "Kami shiho gatame works through four-corner control and "
            "vertical weight. The holder's 70 kilograms press down with "
            "about 45 kilograms across the head-side and 25 across the "
            "hips - the weight split that keeps the shoulders pinned "
            "while the hips stay controlled. Both arms thread under uke's "
            "arms to grip the belt, which kills the two great escapes: "
            "the bridge (no arm to post with, no shoulder to turn) and the "
            "shrimp (the hips are ridden, not chased). The head stays low "
            "and tight to uke's body - any gap at the head end is an "
            "escape hatch the opponent will find in seconds. The osaekomi "
            "clock runs the same as every pin: 10 seconds waza-ari, 20 "
            "seconds ippon. Drilled as positional rounds: the bottom "
            "partner escapes, the top partner re-pins, reset on escape or "
            "ippon. The beginner error is holding with the arms - "
            "squeezing instead of settling; the correction is to relax the "
            "arms into hooks and let gravity do the holding."
        ),
        "key_points": [
            "North-south position: chest over their chest in a straight line, both arms underhooked to the belt.",
            "Control all four corners - both shoulders, both hips; control the points and the body between them cannot move.",
            "Weight split about 45 kilograms head-side, 25 hips-side of a 70-kilogram holder: shoulders pinned, hips ridden.",
            "Keep the head low and tight; any gap at the head end is an escape hatch found in seconds.",
            "Osaekomi clock: 10 seconds waza-ari, 20 seconds ippon - hold with gravity, not with squeezing arms.",
        ],
        "requirements": [
            "A partner for positional rounds with realistic escape attempts.",
            "Release on tap or signal; the vertical chest pressure restricts breathing.",
            "Knowledge of the four-corner concept before the pin is drilled.",
            "No stacking the opponent's neck: the hold controls the torso, never cranks the spine.",
            "Mat space for the north-south line - the bodies need a full length.",
        ],
        "standards": [
            "Kodokan osaekomi-waza: kami shiho gatame as the north-south pin among katame-waza.",
            "Four-corner control standard: both shoulders and both hips controlled throughout the hold.",
            "IJF osaekomi scoring: 10 seconds waza-ari, 20 seconds ippon.",
        ],
        "citations": [CIT_KANO, CIT_INOKUMA],
        "sig_lens": (
            "The Signature read: kami shiho gatame is the Signature "
            "north-south seal - four corners controlled, the document "
            "pressed flat. The Signature Way files it as the geometry of "
            "control: own the four points and the territory between them "
            "signs itself over, twenty seconds at a time."
        ),
    },
    {
        "key": "yoko_shiho_gatame",
        "name": "Yoko Shiho Gatame: Side Four Corner Hold",
        "group": "Katame Waza",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Yoko shiho gatame (side four corner hold, 横四方固) is the side "
            "pin: the holder lies across the opponent's torso at ninety "
            "degrees, chest heavy on the chest, one arm under the head and "
            "the other controlling the far hip, the legs sprawled for a "
            "wide base. It is the pin of pressure - where kami shiho "
            "gatame presses straight down, yoko shiho gatame drives the "
            "weight sideways across the ribs, and the opponent feels every "
            "kilogram. The head-side arm threads under the neck (controlling "
            "without choking - the hold is a pin, not a strangle) while the "
            "hip-side arm blocks the far hip, so the four corners are "
            "owned from the side. This is the hold competitors choose when "
            "they want the pin to feel inevitable: the cross-body weight "
            "makes bridging nearly impossible, and the wide leg base "
            "answers every roll attempt. Ten seconds waza-ari, twenty "
            "ippon - and the side pin has ended more matches than any other "
            "hold in the book."
        ),
        "how_it_works": (
            "Yoko shiho gatame works through cross-body pressure and a wide "
            "base. The holder's chest - about 40 kilograms of a 70-"
            "kilogram holder - drives across the opponent's ribs at ninety "
            "degrees, while the legs sprawl wide to make the base "
            "unrollable: any bridge attempt meets a posted leg and a "
            "widened stance. The under-the-head arm controls the near "
            "shoulder and the far arm blocks the hip, so the opponent's "
            "two escape engines - the shoulder turn and the hip escape - "
            "are both owned. The head-side arm must control without "
            "constricting: the forearm lies across the shoulder, not the "
            "throat, because this is osaekomi, not shime-waza. Weight "
            "stays low and sprawled; lifting the hips to adjust is the "
            "moment escapes happen, so adjustments are made by walking the "
            "feet, never by standing up. Drilled from side control "
            "entries - throw follow-ups, scramble pins - with the bottom "
            "partner escaping live and the top partner re-pinning without "
            "ever giving up chest contact."
        ),
        "key_points": [
            "Lie across at ninety degrees: about 40 kilograms of chest pressure driving sideways across the ribs.",
            "One arm under the head controls the near shoulder, the other blocks the far hip - both escape engines owned.",
            "Sprawl the legs wide; answer bridges with a posted leg and a widened base, never by standing up.",
            "The head-side arm controls without constricting - forearm on the shoulder, never the throat: this is a pin, not a strangle.",
            "Adjust by walking the feet, never by lifting the hips; the moment the hips rise, the escape begins.",
        ],
        "requirements": [
            "A partner for live escape-and-repin rounds from side control.",
            "Strict pin-not-strangle discipline on the head-side arm, verified by an instructor.",
            "Release on tap; the cross-body rib pressure is genuinely uncomfortable.",
            "Mat space for the sprawled base - the legs need width.",
            "Knowledge of the escape answers before live rounds: post the leg, widen the base, follow the hips.",
        ],
        "standards": [
            "Kodokan osaekomi-waza: yoko shiho gatame as the side four-corner pin.",
            "Cross-body pressure standard: chest across the ribs at ninety degrees with a sprawled base.",
            "IJF osaekomi scoring: 10 seconds waza-ari, 20 seconds ippon; no throat constriction in pins.",
        ],
        "citations": [CIT_KANO, CIT_INOKUMA, CIT_IJF],
        "sig_lens": (
            "The Signature read: yoko shiho gatame is the Signature "
            "cross-seal - pressed at ninety degrees, the document cannot "
            "turn. The Signature Way admires the side pin for its finality: "
            "no lifting, no squeezing, just weight filed sideways and a "
            "base too wide to roll. Inevitability, signed in rib pressure."
        ),
    },
    {
        "key": "nami_juji_jime",
        "name": "Nami Juji Jime: Normal Cross Choke",
        "group": "Katame Waza",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Nami juji jime (normal cross choke, 並十字絞) is the classic "
            "gi choke: both hands grip the opponent's lapels with palms "
            "down, wrists crossed, and the choke tightens by pulling the "
            "hands apart and down, driving the lapel edges into the sides "
            "of the neck. It is a shime-waza (strangling technique) that "
            "constricts the carotid arteries - a blood choke, which is why "
            "it acts in seconds and why it is safe in trained hands: "
            "release the pressure and blood flow returns immediately. The "
            "cross of the wrists is the mechanism: as the hands separate, "
            "the crossed forearms scissor the lapels inward from both "
            "sides at once. Done from the mount, the guard, or the back, "
            "it is the most photographed submission in judo and the first "
            "choke most students learn. The safety culture around it is "
            "absolute: chokes are practiced with immediate release on the "
            "tap, partners are trusted explicitly, and anyone who holds a "
            "choke past the tap is done training in that dojo."
        ),
        "how_it_works": (
            "Nami juji jime works as a crossed scissor on the carotids. "
            "With each hand pulling about 180 newtons and the wrists "
            "crossed at roughly 50 degrees, the inward constricting force "
            "is about 2 × 180 × sin(25°) - near 152 newtons - driven "
            "through the lapel edges into the sides of the neck, "
            "compressing the carotid arteries. Blood chokes act fast: the "
            "brain's oxygen reserve gives a trained partner a safe tap "
            "window, and the dojo rule is instant release on the tap - the "
            "choke is a communication tool in practice, never a weapon. "
            "The grips must be deep - thumb inside the collar, four "
            "fingers out, wrists crossed palm-down - because shallow grips "
            "slide and become a painful jaw crank instead of a clean "
            "choke. The pull is apart and down, elbows dropping to the "
            "mat, which keeps the force on the arteries rather than the "
            "windpipe. Drilled slowly with a trusted partner: apply, feel "
            "the tap, release instantly - the release reflex is trained as "
            "hard as the choke itself."
        ),
        "key_points": [
            "Palms down, wrists crossed, deep lapel grips: the crossed forearms scissor the lapels inward from both sides.",
            "Two 180-newton pulls at a 50-degree cross give about 152 newtons of inward constriction on the carotids.",
            "Pull apart and down with the elbows dropping - force on the arteries, never the windpipe.",
            "Deep grips or nothing: shallow grips slide into a jaw crank instead of a clean blood choke.",
            "The tap ends it instantly - the release reflex is trained as hard as the choke; holding past the tap ends your training.",
        ],
        "requirements": [
            "A trusted partner and an instructor present for all choke practice - no exceptions.",
            "Immediate release on the tap, drilled as a reflex from the first session.",
            "Deep-grip discipline verified by the instructor; shallow grips are corrected before pressure is applied.",
            "Knowledge of the difference between blood chokes (carotids, fast, safe with release) and air chokes (windpipe, never targeted).",
            "No choke practice without explicit partner consent, every session.",
        ],
        "standards": [
            "Kodokan shime-waza: nami juji jime as the foundational cross choke.",
            "Safety standard: instant release on tap; chokes are practiced as communication, never held out.",
            "IJF rules: shime-waza permitted in senior competition with referee stoppage authority.",
        ],
        "citations": [CIT_KANO, CIT_INOKUMA],
        "sig_lens": (
            "The Signature read: nami juji jime is the Signature cross - "
            "two lapels signed across the neck in one scissoring motion. "
            "The Signature Way files the cross choke under trust as the "
            "highest covenant: the technique only exists because the "
            "partner trusts the instant release, and that trust is the "
            "real signature on the technique."
        ),
    },
    {
        "key": "hadaka_jime",
        "name": "Hadaka Jime: Rear Naked Strangle",
        "group": "Katame Waza",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Hadaka jime (rear naked strangle, 裸絞) is the strangle that "
            "needs no gi: from behind the opponent, the student slides one "
            "forearm across the front of the neck, locks it with the other "
            "hand - the classic figure-four - and constricts the carotids "
            "by expanding the chest and drawing the elbow back. Naked "
            "means without the uniform: the arms alone do the work, which "
            "makes it the most universally applicable strangle in the art "
            "and the one every grappler in every style knows. Applied from "
            "the back with hooks in or from a standing rear clinch in "
            "self-defense contexts, it is fast, decisive, and - with the "
            "instant-release discipline - safe to practice. The figure-"
            "four lock multiplies the input force: a 150-newton draw "
            "becomes about 210 newtons of constriction through the lever "
            "of the locked arms. Like all shime-waza, it lives inside the "
            "tap-and-release covenant, and it is never practiced without "
            "a trusted partner and supervision."
        ),
        "how_it_works": (
            "Hadaka jime works as a forearm vise on the carotids. The "
            "choking forearm lies across the front of the neck - the "
            "carotids run along the sides, so the forearm's edges do the "
            "constricting while the biceps and the supporting hand complete "
            "the loop; the figure-four lock gives about a 1.4-times force "
            "multiplier, turning a 150-newton draw into roughly 210 "
            "newtons of constriction. The finish expands the chest and "
            "draws the choking elbow back and down, which tightens the "
            "vise without any yanking - smooth pressure, never a jerk. "
            "Position before submission is the rule: the back must be "
            "controlled first (chest to back, no space), because a loose "
            "back gives the opponent the turn that defeats the strangle. "
            "The tap window is short - seconds - so the practice drill is "
            "apply-to-first-pressure, tap, release: partners learn the "
            "feeling of the lock engaging without ever approaching the "
            "limit. In competition the referee watches the strangle "
            "closely and stops the match at the tap or at any sign of "
            "distress."
        ),
        "key_points": [
            "From the back: one forearm across the front of the neck, figure-four lock, expand the chest and draw the elbow back.",
            "The figure-four multiplies force about 1.4 times: a 150-newton draw becomes roughly 210 newtons of constriction.",
            "Position before submission: control the back first with no space, or the turn defeats the strangle.",
            "Smooth pressure, never a jerk - the vise tightens by expansion, not yanking.",
            "Apply to first pressure, tap, release: the tap window is seconds, and the release reflex is the real technique.",
        ],
        "requirements": [
            "A trusted partner, an instructor present, explicit consent - the non-negotiable choke protocol.",
            "Back control fundamentals before the strangle is ever applied.",
            "Instant release on tap, drilled as a reflex; holding past the tap ends training.",
            "No practice on anyone with neck injuries, vascular conditions, or without medical clearance for strangle training.",
            "Knowledge of referee stoppage: in competition the strangle ends at the tap or the referee's call.",
        ],
        "standards": [
            "Kodokan shime-waza: hadaka jime as the no-gi strangle archetype.",
            "Force-multiplier mechanics: the figure-four lock at approximately 1.4 times input force.",
            "Safety standard: tap-and-instant-release; referee authority to stop at any sign of distress.",
        ],
        "citations": [CIT_KANO, CIT_INOKUMA, CIT_IJF],
        "sig_lens": (
            "The Signature read: hadaka jime is the Signature vise - no "
            "uniform, no props, just the arms filing the final document. "
            "The Signature Way honors the naked strangle as the technique "
            "stripped to essentials: position, lock, expand - maximum "
            "efficiency with nothing to hide behind, sealed by the "
            "instant-release covenant."
        ),
    },
    {
        "key": "juji_gatame",
        "name": "Juji Gatame: Cross Armlock",
        "group": "Katame Waza",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Juji gatame (cross armlock, 十字固) is judo's signature "
            "submission: the student traps the opponent's arm between the "
            "legs, controls the wrist, and extends the hips to hyperextend "
            "the elbow - the armbar that has finished more grappling "
            "matches across more styles than any other joint lock. The "
            "cross of the body over the arm is the mechanism: the "
            "attacker's hips become the fulcrum under the elbow while the "
            "legs and hands control the wrist above it, and the slightest "
            "hip extension applies leverage the elbow cannot resist. It is "
            "a kansetsu-waza (joint technique), and in judo only the elbow "
            "may be attacked - the control and the finish reflect that "
            "limit precisely. Entries come from everywhere: from the mount, "
            "from the guard, as a counter to a pin escape, as the finish "
            "to a failed throw. The safety discipline is total: the lock "
            "is applied with control to the tap, never cranked, and the "
            "partner's tap is obeyed before pressure, not after pain."
        ),
        "how_it_works": (
            "Juji gatame works as a first-class lever on the elbow. The "
            "attacker's hips sit tight against the opponent's elbow as the "
            "fulcrum; the legs pinch the arm and the hands control the "
            "wrist about 0.28 meters from the fulcrum. A controlled 120-"
            "newton hip extension through that arm generates roughly 33.6 "
            "newton-meters of torque (120 × 0.28) on the elbow joint - more "
            "than enough to force the tap, which is why the technique is "
            "never applied fast in practice. The thumb points up and the "
            "wrist is controlled so the elbow cannot rotate out; the "
            "attacker's knees squeeze the arm and the head-side leg "
            "controls the opponent's head to prevent the stack escape. The "
            "finish raises the hips slowly - millimeters decide it - and "
            "the instant the partner taps, everything releases. Drilled in "
            "stages: position only (no pressure), then pressure to the "
            "first resistance, then live with the tap discipline, always "
            "with the rule that the applier is responsible for the "
            "partner's joint."
        ),
        "key_points": [
            "Hips tight under the elbow as the fulcrum, wrist controlled 0.28 meters out: 120 newtons becomes about 33.6 newton-meters of torque.",
            "Trap the arm between the legs, thumb up, knees pinching - control the wrist and the head to kill the escapes.",
            "The finish is hip extension in millimeters, never a yank; the tap is obeyed before pressure, not after pain.",
            "Entries come from everywhere - mount, guard, pin-escape counters, failed throws - making it the most versatile submission.",
            "Only the elbow is attacked in judo kansetsu-waza; the applier is responsible for the partner's joint, always.",
        ],
        "requirements": [
            "A trusted partner and instructor supervision for all armlock practice.",
            "Slow controlled application only - speed plus joint locks is how injuries happen.",
            "Immediate release on the tap, before pressure becomes pain.",
            "No practice on partners with elbow or shoulder injuries.",
            "Knowledge of the legal target: the elbow only; no other joint is attacked in judo.",
        ],
        "standards": [
            "Kodokan kansetsu-waza: juji gatame as the cross-armlock archetype; elbow the only legal target.",
            "Lever mechanics: hip fulcrum under the elbow, wrist controlled at approximately 0.28 meters.",
            "Safety standard: controlled application, instant release on tap, applier responsibility for the joint.",
        ],
        "citations": [CIT_KANO, CIT_INOKUMA, CIT_IJF],
        "sig_lens": (
            "The Signature read: juji gatame is the Signature lever - the "
            "cross filed over the elbow, the whole body signing one joint. "
            "The Signature Way treats the armlock as the ultimate lesson "
            "in controlled power: 33.6 newton-meters available, and the "
            "mastery is in never needing them. The tap is the signature; "
            "the release is the seal."
        ),
    },

    {
        "key": "renraku_waza",
        "name": "Renraku Waza: Combination Throwing",
        "group": "Advanced Study",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Renraku waza (combination techniques, 連絡技) is where judo "
            "becomes chess: chaining two or more throws so that the "
            "opponent's defense against the first becomes the kuzushi for "
            "the second. The logic is the eight directions made tactical - "
            "attack forward with seoi nage, and when the opponent resists "
            "by leaning back, their own resistance is rear kuzushi for o "
            "uchi gari; attack o uchi gari, they step out, and ko uchi "
            "gari flicks the stepping foot. The great combinations pair "
            "opposites: forward-backward (seoi nage to o soto gari), "
            "backward-forward (o soto gari to seoi nage), big-small (o "
            "uchi gari to ko uchi gari), throw-to-throw across families. "
            "Combinations multiply probability: three attacks at 40, 50, "
            "and 70 percent are not three separate chances but one "
            "combined 91 percent - the mathematics of never letting the "
            "opponent settle. This is the advanced student's main weapon, "
            "because at high level nobody falls to a single clean attack; "
            "they fall to the second or third sentence of the combination."
        ),
        "how_it_works": (
            "Renraku waza works on the arithmetic of linked probabilities "
            "and the physics of committed defense. When the opponent "
            "resists a forward throw by driving backward, their center of "
            "mass travels rearward - which is exactly the kuzushi the "
            "backward follow-up needs, supplied free by the defense "
            "itself. The probability compounds: attacks succeeding at 0.4, "
            "0.5, and 0.7 give a combined success of 1 - (0.6 × 0.5 × 0.3) "
            "= 0.91, ninety-one percent - because each attempt only needs "
            "one of the chain to land. The technical key is the transition: "
            "the first attack must be genuine - a fake draws no real "
            "defense and buys nothing - and the second must launch from "
            "the first's finishing position with no recovery step, which "
            "means combinations are drilled as single continuous motions. "
            "Training runs the classic pairs hundreds of times: o uchi to "
            "seoi, seoi to o uchi, o uchi to ko uchi, de ashi to o soto - "
            "then the student is given a partner who defends freely, and "
            "must score with the second or third technique of a chain, "
            "never the first."
        ),
        "key_points": [
            "Chain throws so the defense against the first becomes the kuzushi for the second - resistance is free kuzushi.",
            "Pair opposites: forward-backward, backward-forward, big-small, across throw families.",
            "Probabilities compound: 0.4, 0.5, 0.7 chain to 0.91 combined - the mathematics of never letting them settle.",
            "The first attack must be genuine; a fake draws no real defense and buys nothing.",
            "Drill each pair as one continuous motion with no recovery step - the transition is the technique.",
        ],
        "requirements": [
            "Fluency in the individual throws first; combinations are built from mastered parts, never from shaky ones.",
            "A partner who defends realistically - compliant partners teach fake combinations.",
            "Understanding of happo no kuzushi: the chain must run through genuinely opposite directions.",
            "Randori time dedicated to second-and-third-attack scoring.",
            "An instructor to verify the transitions: no reset steps between links.",
        ],
        "standards": [
            "Kodokan renraku-waza: combination throwing as the advanced tactical doctrine.",
            "Probability standard: linked attempts compound as 1 minus the product of the failure rates.",
            "Training standard: combinations drilled as continuous motions from genuine first attacks.",
        ],
        "citations": [CIT_KANO, CIT_DAIGO, CIT_INOKUMA],
        "sig_lens": (
            "The Signature read: renraku waza is the Signature compound "
            "sentence - each throw a clause, the defense the conjunction. "
            "The Signature Way files combinations as the art of letting "
            "the opponent co-author their own fall: their resistance "
            "signs the second attack, their recovery signs the third."
        ),
    },
    {
        "key": "kaeshi_waza",
        "name": "Kaeshi Waza: Counter Techniques",
        "group": "Advanced Study",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Kaeshi waza (counter techniques, 返し技) is the art of throwing "
            "with the opponent's throw: meeting their attack not with "
            "resistance but with a redirect that turns their committed "
            "force into your score. The classics are named pairs - seoi "
            "nage countered by tani otoshi, o soto gari countered by o "
            "soto gaeshi, uchi mata countered by uchi mata gaeshi - each "
            "one exploiting the exact moment the attacker has spent their "
            "balance and cannot recover. The counter window is narrow: the "
            "attacker's telegraph lasts about 0.25 seconds, and the "
            "counter entry takes about 0.3 seconds, so the counter must "
            "begin almost as the attack is recognized - there is no time "
            "to think, only to have drilled. This is why kaeshi waza is "
            "advanced study: it demands the attacker's whole catalog "
            "recognized by feel, the counter entries automatic, and the "
            "courage to let an attack come in rather than blocking it. "
            "Done right, the counter is the most efficient throw in judo - "
            "the opponent supplies the energy, you supply only the "
            "direction."
        ),
        "how_it_works": (
            "Kaeshi waza works on commitment and the narrow counter "
            "window. Every committed attack spends the attacker's balance "
            "for about 0.25 seconds of telegraph plus execution; the "
            "counter entry needs about 0.3 seconds, so the defender must "
            "read the attack in its first instant and move with it rather "
            "than against it. The mechanics vary by pair: against seoi "
            "nage, the defender drops their weight and hooks the leg for "
            "tani otoshi as the attacker turns; against o soto gari, the "
            "defender hops the reaped leg and reaps back (o soto gaeshi); "
            "against uchi mata, the defender circles the lifting leg and "
            "reaps it. In each case the attacker's forward or backward "
            "commitment becomes the kuzushi - a seoi nage attacker is "
            "already falling forward, and the counter merely steers the "
            "fall. Training starts with compliant partners telegraphing "
            "clearly, then speeds up to full randori, where the student is "
            "tasked with scoring only by counter for entire rounds. The "
            "failure mode is the late counter - arriving after the "
            "attacker's balance has returned - which is just a weak attack "
            "of your own."
        ),
        "key_points": [
            "Throw with their throw: the attacker's committed force becomes your kuzushi - you supply only the direction.",
            "The counter window is about 0.25 seconds of telegraph against a 0.3-second entry: recognition must be instant and drilled.",
            "Learn the named pairs: seoi nage to tani otoshi, o soto gari to o soto gaeshi, uchi mata to uchi mata gaeshi.",
            "Never block the attack - move with it and redirect it; resistance wastes the energy the counter needs.",
            "Drill compliant and slow first, then full randori with counter-only scoring rounds.",
        ],
        "requirements": [
            "Recognition of the major attacks by feel - counters cannot be thought through in the window.",
            "Automatic counter entries, drilled to reflex before live attempts.",
            "A partner who attacks with genuine commitment in the drills; half-attacks teach mistimed counters.",
            "The courage to let attacks come in - the counter game punishes flinching.",
            "Instructor supervision: mistimed counters against committed attacks are a collision risk.",
        ],
        "standards": [
            "Kodokan kaeshi-waza: counter techniques as the advanced defensive doctrine.",
            "Timing standard: the counter launches inside the attacker's commitment window.",
            "Training standard: compliant slow drilling to reflex before live counter randori.",
        ],
        "citations": [CIT_KANO, CIT_DAIGO],
        "sig_lens": (
            "The Signature read: kaeshi waza is the Signature redirect - "
            "the opponent's attack filed as your throw. The Signature Way "
            "treats the counter as perfect economy in its purest form: "
            "zero energy generated, all of it inherited, the attacker's "
            "signature forged into your victory by their own hand."
        ),
    },
    {
        "key": "tate_shiho_gatame",
        "name": "Tate Shiho Gatame: Mounted Four Corner Hold",
        "group": "Katame Waza",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Tate shiho gatame (mounted four corner hold, 縦四方固) is the "
            "mount pin: the holder sits astride the opponent's torso, "
            "knees tight to the ribs, chest heavy on the chest, controlling "
            "both arms - the most dominant position in groundwork. From "
            "the mount the holder commands all four corners at once while "
            "keeping the hips free to answer every escape: the bridge is "
            "met by a wide knee base, the roll by posting, the hip escape "
            "by following. It is the pin that transitions most naturally "
            "to submissions - the mounted opponent who pushes up gives "
            "the arms for juji gatame, who turns gives the back for "
            "strangles - which is why advanced groundwork treats the mount "
            "as a hunting position, not just a hold. The osaekomi clock "
            "runs the same: ten seconds waza-ari, twenty ippon. But the "
            "mount's real value is strategic: it is the one pin from "
            "which every finish in katame-waza is reachable, and holding "
            "it against a skilled escape artist is the black-belt test of "
            "ground control."
        ),
        "how_it_works": (
            "Tate shiho gatame works through the mounted base and arm "
            "control. The knees sit tight at about 0.6 meters apart, "
            "gripping the opponent's ribs; the chest - about 55 kilograms "
            "of a 70-kilogram holder - presses down through the "
            "opponent's sternum, and both of uke's arms are controlled, "
            "either pinned under the holder's arms or trapped at the "
            "wrists. The four corners are owned vertically: the shoulders "
            "cannot turn because the chest weight pins them, the hips "
            "cannot escape because the knees ride them. The classic "
            "escapes are the bridge-and-roll (answered by posting the hand "
            "and widening the knee base on the rolling side) and the elbow "
            "escape (answered by dropping the weight low and cross-facing). "
            "The mount is maintained by floating: the holder's hips stay "
            "loose and follow the opponent's movement, never rigid, "
            "re-settling the weight after each escape attempt. Drilled as "
            "positional sparring - hold the mount for the round, switch on "
            "escape or submission - which builds the specific endurance "
            "the position demands."
        ),
        "key_points": [
            "Mount astride: knees tight at about 0.6 meters, chest heavy with about 55 kilograms pressing through the sternum.",
            "Control both arms - pinned or wrist-trapped; the mount's submissions all start from arm control.",
            "Own all four corners vertically: chest weight pins the shoulders, knees ride the hips.",
            "Answer the bridge-and-roll by posting and widening the base; answer the elbow escape by dropping low and cross-facing.",
            "Maintain by floating: loose hips that follow and re-settle, never a rigid perch.",
        ],
        "requirements": [
            "A skilled partner for positional sparring - the mount must be tested against real escapes.",
            "Release on tap; the mount transitions to submissions and the tap discipline carries over.",
            "Hip mobility for the floating base; rigid hips are bucked off.",
            "Knowledge of the submission entries from the mount before live positional rounds.",
            "Mat space for the bridge-and-roll defense - the holder needs room to post.",
        ],
        "standards": [
            "Kodokan osaekomi-waza: tate shiho gatame as the mounted four-corner pin.",
            "Base standard: knees at approximately 0.6 meters gripping the ribs, weight through the sternum.",
            "IJF osaekomi scoring: 10 seconds waza-ari, 20 seconds ippon.",
        ],
        "citations": [CIT_KANO, CIT_INOKUMA, CIT_IJF],
        "sig_lens": (
            "The Signature read: tate shiho gatame is the Signature mount "
            "- the high seat from which every ground document can be "
            "signed. The Signature Way files the mount as the position of "
            "total authorship: four corners owned, all submissions "
            "reachable, the opponent's every movement merely choosing "
            "which technique signs next."
        ),
    },
    {
        "key": "okuri_eri_jime",
        "name": "Okuri Eri Jime: Sliding Lapel Choke",
        "group": "Katame Waza",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Okuri eri jime (sliding lapel choke, 送襟絞) is the sliding "
            "strangle: one hand grips the opponent's far lapel and slides "
            "it across - okuri means sliding or sending - while the other "
            "hand pulls the near lapel, so the gi itself becomes a "
            "constricting loop around the neck. Applied most often from "
            "the back or from a top pin when the opponent turns away, it "
            "punishes the most common defensive reaction: the opponent who "
            "turtles or turns to escape the pin feeds their lapels "
            "directly into the slide. The mechanics are subtle - the "
            "sliding hand travels about 0.15 meters across, and the "
            "friction of gi on gi (coefficient near 0.4) means the slide "
            "must be committed: a 160-newton pull works against about 64 "
            "newtons of friction, so hesitation kills the choke. It is "
            "advanced study because the setup is positional - you must "
            "first earn the back or the turn - and because the sliding "
            "action is a fine motor skill under pressure. But it is one "
            "of the highest-percentage strangles in competition, precisely "
            "because it harvests the opponent's own escape attempts."
        ),
        "how_it_works": (
            "Okuri eri jime works by turning the opponent's lapels into a "
            "noose. The sliding hand grips the far lapel and draws it "
            "about 0.15 meters across the front of the neck while the near "
            "hand anchors the near lapel; the loop tightens as the hands "
            "separate, constricting the carotids through the gi. Gi-on-gi "
            "friction runs near 0.4, so a 160-newton slide works against "
            "about 64 newtons of friction - the pull must be decisive and "
            "continuous, because a stalled slide just rearranges the "
            "uniform. The choke is a blood choke on the carotids, acting "
            "in seconds with the same tap-and-instant-release discipline "
            "as every shime-waza. The entries are the study: from the back "
            "when the opponent hand-fights, from kesa gatame when they "
            "turn in, from the turtle when they refuse to be flattened - "
            "each entry first wins the position, then the slide finishes. "
            "Drilled as position-to-slide repetitions with a trusted "
            "partner: win the back, slide, feel the engagement, tap, "
            "release - the release reflex trained as hard as the slide."
        ),
        "key_points": [
            "Slide the far lapel about 0.15 meters across while anchoring the near lapel: the gi becomes the noose.",
            "Gi-on-gi friction near 0.4 means a 160-newton slide fights about 64 newtons - commit fully, hesitation kills it.",
            "It harvests escape attempts: the opponent who turtles or turns feeds the lapels into the slide.",
            "Position first, slide second - the back or the turn must be earned before the strangle is attempted.",
            "Blood choke discipline throughout: tap ends it instantly, release reflex trained as hard as the slide.",
        ],
        "requirements": [
            "The full choke protocol: trusted partner, instructor present, explicit consent, instant release on tap.",
            "Back control or pin-turn fundamentals - the entries must be earned positionally.",
            "A gi with slidable lapels; the technique needs the uniform to travel.",
            "Fine-motor slide practice before any pressure: the action is subtle under load.",
            "No practice on partners with neck or vascular issues.",
        ],
        "standards": [
            "Kodokan shime-waza: okuri eri jime as the sliding-lapel strangle.",
            "Friction mechanics: committed continuous slide against approximately 0.4 gi-on-gi friction.",
            "Safety standard: tap-and-instant-release; the choke is never held out in practice.",
        ],
        "citations": [CIT_KANO, CIT_INOKUMA],
        "sig_lens": (
            "The Signature read: okuri eri jime is the Signature slide - "
            "the opponent's own uniform filed against them. The Signature "
            "Way loves this strangle for its irony, signed in friction: "
            "the harder they try to escape the pin, the tighter they "
            "deliver the lapels. Their defense co-signs the finish."
        ),
    },
    {
        "key": "sumi_gaeshi",
        "name": "Sumi Gaeshi: Corner Reversal Throw",
        "group": "Nage Waza",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Sumi gaeshi (corner reversal, 隅返) is the sacrifice throw of "
            "the corner: when the opponent drives forward into a clinch, "
            "the student drops to the back, hooks a foot inside the "
            "opponent's leg, and wheels them over the corner - the "
            "shoulder-to-hip diagonal - using their own driving force. "
            "Where tomoe nage circles uke straight overhead, sumi gaeshi "
            "tips them over the side corner, which makes it the natural "
            "answer to the forward-driving opponent who has learned to "
            "defend the straight circle. It is a ma-sutemi-waza (rear "
            "sacrifice) of the highest technical order: the timing must "
            "catch the opponent's drive at its peak, the hook must be "
            "placed, not kicked, and the wheeling pull of the hands must "
            "steer the corner precisely. Champions use it as the "
            "punishment for over-aggression - the harder uke charges, the "
            "harder sumi gaeshi throws them. The drop is total commitment: "
            "like all sacrifices, it cannot be taken back mid-fall."
        ),
        "how_it_works": (
            "Sumi gaeshi works by wheeling a driving opponent over the "
            "corner. The student drops backward about 0.9 meters, hooking "
            "the foot inside uke's leg at the ankle; the hands pull uke's "
            "upper body toward the student's shoulder-to-hip corner while "
            "the hooked leg lifts, and uke rotates over that corner along "
            "an arc of radius about 1.0 meter - a quarter circle of roughly "
            "1.57 meters of guided flight. The opponent's forward drive "
            "supplies the energy: the technique adds direction, not force, "
            "which is why it punishes aggression proportionally. The hook "
            "is placed with the instep, lifting rather than kicking - the "
            "leg guides the wheel, the hands steer it. Timing targets the "
            "peak of the opponent's drive: too early and there is no "
            "energy to borrow, too late and the drive has already "
            "overwhelmed the position. Drilled against a partner driving "
            "forward in a controlled clinch, then in randori with the "
            "student tasked to answer every hard forward drive with the "
            "corner."
        ),
        "key_points": [
            "Drop to the back, hook the instep inside uke's ankle, and wheel them over the shoulder-to-hip corner: about 1.57 meters of guided flight.",
            "The opponent's forward drive supplies the energy - the technique adds direction, not force; aggression is punished proportionally.",
            "Time it at the peak of their drive: too early borrows nothing, too late is overwhelmed.",
            "The hook is placed and lifts, never kicks; the leg guides the wheel while the hands steer it.",
            "Total commitment like every sacrifice - the drop cannot be taken back mid-fall.",
        ],
        "requirements": [
            "Mastery of tomoe nage first; sumi gaeshi is the corner refined from the circle.",
            "A partner with excellent ukemi who drives forward controllably in the drills.",
            "Hook placement discipline verified by an instructor: instep lift, never a kick.",
            "Core strength for the drop-and-wheel under a driving load.",
            "Randori maturity: the technique is attempted only against genuine forward drives.",
        ],
        "standards": [
            "Kodokan sutemi-waza: sumi gaeshi among the 67 throws, the corner-reversal archetype.",
            "Wheel mechanics: the opponent rotates over the corner along approximately a quarter-circle arc.",
            "Safety standard: the hooking leg places and lifts; kicking is prohibited.",
        ],
        "citations": [CIT_KANO, CIT_DAIGO],
        "sig_lens": (
            "The Signature read: sumi gaeshi is the Signature corner - "
            "the wheeling reversal that files aggression as its own "
            "punishment. The Signature Way keeps it advanced because the "
            "timing is a signature that cannot be forged: catch the "
            "drive at its peak, and their charge signs the corner."
        ),
    },
    {
        "key": "ude_garami",
        "name": "Ude Garami: Entangled Armlock",
        "group": "Katame Waza",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Ude garami (entangled armlock, 腕緘) is the figure-four "
            "shoulder lock: the student's arms weave through the "
            "opponent's arm in a figure-four configuration and torque the "
            "shoulder toward its rotational limit. Garami means entangled, "
            "and the entanglement is the technique - once the figure-four "
            "is locked, the opponent's arm is woven into a structure where "
            "every escape direction tightens a different part of the trap. "
            "It is a kansetsu-waza applied to the shoulder and elbow "
            "complex, most often finished from side control, the mount, or "
            "the guard, and it is the lock that teaches advanced students "
            "the difference between a submission and a position: ude "
            "garami is finished slowly, with the torque increased by "
            "degrees, and the tap comes from the inevitability of the "
            "entanglement rather than from sudden pain. Like all joint "
            "techniques it is governed by total partner responsibility - "
            "the applier owns the joint, the tap is obeyed instantly, and "
            "the lock is never cranked."
        ),
        "how_it_works": (
            "Ude garami works as a figure-four torque on the shoulder. The "
            "arms weave: one arm threads under the opponent's arm and grips "
            "the student's own wrist, completing the four; the entangled "
            "arm becomes a lever about 0.3 meters long, and a controlled "
            "100-newton torque application generates roughly 30 "
            "newton-meters (100 × 0.3) of rotational force on the shoulder "
            "complex - applied gradually, in degrees, never suddenly. The "
            "entanglement controls the elbow as well as the shoulder, "
            "which is why escape is so difficult: straightening the arm "
            "to relieve the shoulder tightens the elbow trap, and bending "
            "to protect the elbow loads the shoulder. The finish lifts the "
            "entangled arm slowly while the figure-four holds the "
            "configuration - the classic paintbrush motion - and the "
            "partner taps at the first real pressure. Drilled as "
            "entanglement-only first (lock the figure-four, no torque), "
            "then torque-to-first-resistance with a trusted partner, then "
            "in positional sparring with the full tap discipline."
        ),
        "key_points": [
            "Weave the figure-four through their arm: the entanglement is the technique, the torque is just the signature.",
            "A 0.3-meter lever with 100 newtons gives about 30 newton-meters on the shoulder - applied gradually, in degrees, never suddenly.",
            "Every escape tightens a different part of the trap: straighten and the elbow loads, bend and the shoulder loads.",
            "Finish with the slow paintbrush lift; the tap comes from inevitability, not from sudden pain.",
            "The applier owns the joint absolutely: tap obeyed instantly, the lock never cranked, no exceptions.",
        ],
        "requirements": [
            "The full joint-lock protocol: trusted partner, instructor supervision, slow application, instant release.",
            "Entanglement mastery before torque: lock the figure-four cleanly with zero pressure first.",
            "Shoulder anatomy awareness - the applier must know what the lock loads.",
            "No practice on partners with shoulder, elbow, or wrist injuries.",
            "Positional control (side control, mount, or guard) established before the lock is attempted live.",
        ],
        "standards": [
            "Kodokan kansetsu-waza: ude garami as the entangled figure-four armlock.",
            "Torque mechanics: approximately 30 newton-meters applied gradually through a 0.3-meter lever.",
            "Safety standard: controlled gradual application, instant release on tap, applier responsibility.",
        ],
        "citations": [CIT_KANO, CIT_INOKUMA],
        "sig_lens": (
            "The Signature read: ude garami is the Signature knot - the "
            "figure-four filed as an unbreakable entanglement. The "
            "Signature Way treats it as the advanced lesson in inevitable "
            "control: not force but geometry, not pain but certainty, the "
            "tap signed by the structure itself."
        ),
    },
    {
        "key": "randori",
        "name": "Randori: Free Practice Method",
        "group": "Advanced Study",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Randori (free practice, 乱取り) is Kano's great invention and "
            "the soul of judo: free, unscripted practice where both "
            "partners attack and defend at full intent, taking whatever "
            "the exchange gives. Ran means chaos or freedom, tori means "
            "taking - free taking, the laboratory where every technique in "
            "this database is tested against a resisting opponent who knows "
            "all the same techniques. A standard session runs six rounds "
            "of four minutes - twenty-four minutes of continuous problem-"
            "solving - with each round generating about a dozen genuine "
            "attack attempts, roughly seventy-two per session, of which a "
            "developing student might finish a quarter. Randori is where "
            "timing is actually learned: no drill can teach when de ashi "
            "harai is available, because availability only exists against "
            "resistance. It is also where jita kyoei (mutual welfare) is "
            "proven - partners go hard enough to be useful and controlled "
            "enough to be safe, and the senior student's duty is to be the "
            "kind of partner whose randori makes juniors better. Every "
            "technique in judo lives or dies in randori."
        ),
        "how_it_works": (
            "Randori works as a live laboratory with a session "
            "architecture. Six four-minute rounds total 24 minutes; at "
            "about twelve genuine attacks per round, a session produces "
            "roughly seventy-two attacks, and a developing student "
            "converting a quarter of them scores about eighteen - the "
            "numbers that make progress measurable across months. The "
            "rules of the lab are the etiquette writ large: full intent "
            "on attacks, full control on landings, tap discipline in "
            "groundwork, and no technique attempted that the student "
            "cannot perform safely on a resisting partner. Partners are "
            "rotated to vary body types and styles, and rounds are themed "
            "as students advance - grip-fighting rounds, combination-only "
            "rounds, counter-only rounds, newaza-only rounds - so each "
            "skill gets isolated live testing. The instructor's role is "
            "matchmaker and safety officer: pairing compatible partners, "
            "stopping dangerous situations, and assigning the constraints "
            "that turn brawling into study. Progress in randori is the "
            "only honest belt test in judo: techniques that work in "
            "drilling but die in randori are not yet learned."
        ),
        "key_points": [
            "Randori is free unscripted practice at full intent: the laboratory where every technique is tested against resistance.",
            "Session architecture: six four-minute rounds, about twelve attacks per round, roughly seventy-two attacks per session.",
            "A developing student converting a quarter of seventy-two attacks scores about eighteen - progress made measurable.",
            "Full intent on attacks, full control on landings: the lab runs on mutual welfare, not mutual destruction.",
            "Techniques that work in drilling but die in randori are not yet learned - randori is the only honest test.",
        ],
        "requirements": [
            "Fluency in ukemi on all sides - randori throws come unscripted and at speed.",
            "A working set of throws and groundwork; randori is testing, not first learning.",
            "Partners matched by size and experience at first, varied as skill grows.",
            "The etiquette and tap discipline of every technique in this database, applied live.",
            "An instructor supervising: matchmaking, safety stops, and themed constraints.",
        ],
        "standards": [
            "Kodokan randori: free practice as codified by Kano - the central training method of judo.",
            "Session standard: timed rounds (commonly four minutes) with partner rotation and themed constraints.",
            "Safety standard: full intent with full control; the senior's duty is to make juniors better.",
        ],
        "citations": [CIT_KANO, CIT_OHLENKAMP, CIT_INOKUMA],
        "sig_lens": (
            "The Signature read: randori is the Signature laboratory - "
            "freedom filed as method, chaos signed into curriculum. The "
            "Signature Way treats free practice as the final auditor: "
            "every technique in the archive must survive the unscripted "
            "exchange, and what survives is stamped genuine. Seventy-two "
            "attacks, eighteen scores, one honest ledger."
        ),
    },
]
