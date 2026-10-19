#!/usr/bin/env python3
"""Entries for the Bartitsu Combat databases (Manon's combat orders 2026-10-17,
combat batch 3).

Roster-verified: slug combat-bartitsu / combat-bartitsu-signature.
Dedupe gate pre-run 2026-10-17 over all 68 titles (34 public + 34
" (Signature Edition)") vs the WHOLE system: zero collisions.

Two NEW databases, 34 ladder-ordered records each:

  combat-bartitsu              - The Bartitsu Combat Database
                                 (public-harvest: real, fact-checked Victorian
                                 martial-arts knowledge - Edward William
                                 Barton-Wright's Bartitsu (London, circa
                                 1898-1902), synthesizing English pugilism,
                                 French savate, Japanese jujutsu as taught by
                                 Yukio Tani, and the Vigny cane-fighting
                                 method - every record a technique with
                                 step-by-step body mechanics)
  combat-bartitsu-signature    - The Bartitsu Combat Signature Database
                                 (his original Signature Combat Method: the
                                 cane the Signature line drawn through space,
                                 the grip the oath, the guard the boundary of
                                 the self, every cut a decision carried to
                                 completion; src signature, titles suffixed
                                 " (Signature Edition)", clearly labeled
                                 Signature-made, never presented as authentic
                                 public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-CBBA- (public) and JAH-CBBAS- (signature), verified free
in the manifest id_prefix values and in every shard index (zero hits).

Civilian historical martial art; every technique is traditional Victorian
self-defense. Screening: nothing hate-adjacent, profane, or inappropriate;
no religious talk; nothing on neutralizing or defeating military or
defense-grade systems.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_bartitsu.py). Every demo prints its real computed values,
asserts tight bounds (never float exact-equality), and ends with the OK
marker; the build machine-executes all 68 demos before delivery.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature Combat Method: the "
            "cane the Signature line drawn through space, the grip the oath, "
            "the guard the boundary of the self, every cut a decision carried "
            "to completion. Clearly labeled Signature-made, never presented "
            "as authentic public record.")

CIT_BARTONWRIGHT_1899 = ("Barton-Wright EW. The New Art of Self Defence. "
                         "Pearson's Magazine; 1899;7:268-275.")
CIT_BARTONWRIGHT_1901 = ("Barton-Wright EW. Self Defence with a Walking-Stick. "
                         "Pearson's Magazine; 1901;11:85-94.")
CIT_VIGNY = ("Vigny P. The Art of Self-Defence on Foot with the Cane and the "
             "Umbrella. Health & Strength; 1904.")
CIT_LANG = ("Lang TH. The Walking Stick Method of Self Defence. Athletic "
            "Publications; 1923.")
CIT_WOLF = ("Wolf T, ed. The Bartitsu Compendium. Vol 1. Lulu Press; 2005.")
CIT_KANO = ("Kano J. Kodokan Judo. Kodansha International; 1986.")
CIT_CHARLEMONT = ("Charlemont J. La Boxe Francaise: Traite Theorique et "
                  "Pratique. Paris; 1878.")
CIT_QUEENSBERRY = ("Marquess of Queensberry Rules. London; 1867.")

STD_BARTITSU = "Barton-Wright Bartitsu canon (London, 1898-1902)"
STD_VIGNY = "Vigny cane method (1904)"
STD_KODOKAN = "Kodokan judo mechanics"
STD_SAVATE = "Charlemont savate lineage"
STD_QUEENSBERRY = "Queensberry boxing lineage"

ENTRIES = [
    {
        "key": "what_is",
        "name": "What Is Bartitsu: The Victorian Art of Self-Defense",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Bartitsu is the eclectic Victorian-era martial art founded in "
            "London by Edward William Barton-Wright around 1898. Its name "
            "blends his surname with jiujitsu, and its method blends four "
            "disciplines: English pugilism (boxing), French savate "
            "(kickboxing in shoes), Japanese jujutsu as taught by Yukio Tani, "
            "and the cane-fighting method of Pierre Vigny. Barton-Wright "
            "trained in Japan and Europe, then opened the Bartitsu Academy of "
            "Arms and Physical Culture at 67b Shaftesbury Avenue, London, "
            "where gentlemen and ladies learned a complete system of civilian "
            "self-defense against street assault, from cane cuts and thrusts "
            "to throws, locks, and boxing combinations. The art was "
            "immortalized when Arthur Conan Doyle's Sherlock Holmes "
            "described it - as 'baritsu, or the Japanese system of wrestling' "
            "- in 'The Adventure of the Empty House' (1903). After fading "
            "early in the twentieth century, Bartitsu was revived by modern "
            "researchers, most notably through the Bartitsu Society and the "
            "Bartitsu Compendium (2005), which republished Barton-Wright's "
            "original articles. This record frames the whole database: every "
            "technique that follows sits on the same four pillars Barton-Wright "
            "set out - the cane, the kick, the blow, and the throw - and every "
            "record teaches it exactly as the Victorian masters taught it: "
            "body mechanics first, theory after."),
        "how_it_works": (
            "Bartitsu works as a layered system of range and response. At "
            "long range the cane dominates: cuts, thrusts, and moulinets keep "
            "an attacker at bay. If the distance collapses, savate kicks "
            "strike from kicking range with the shod foot, pugilism's punches "
            "take over at arm's length, and jujutsu's throws and locks "
            "finish at clinch range. The student masters each range in "
            "ladder order - stance and footwork first, then the cane, then "
            "striking, then throws and ground control - so that every later "
            "technique borrows balance and timing from the ones before it. "
            "The art's genius is its doctrine of the whole: no single "
            "discipline is complete alone, but the four together leave no "
            "gap between walking-stick distance and the ground."),
        "key_points": [
            "Founded by Edward William Barton-Wright in London around 1898; the name joins Barton-Wright and jiujitsu.",
            "Four pillars: English pugilism, French savate, Japanese jujutsu (Yukio Tani), and the Vigny cane method.",
            "Taught at the Bartitsu Academy of Arms and Physical Culture, 67b Shaftesbury Avenue, London.",
            "Referenced by Sherlock Holmes as 'baritsu' in 'The Adventure of the Empty House' (1903).",
            "Revived by modern researchers and the Bartitsu Compendium (2005) from Barton-Wright's original articles.",
            "Civilian self-defense art: built for street assault, practiced with safety conventions, traditional scope only.",
        ],
        "requirements": [
            "Study the four disciplines in ladder order; do not skip to throws before stance is solid.",
            "Read Barton-Wright's original articles (Pearson's Magazine, 1899-1901) as the primary source.",
            "Practice with a partner under agreed safety rules; cane work needs a clear space and controlled force.",
            "Respect the traditional scope: civilian techniques only, taught as body mechanics first and theory after.",
        ],
        "standards": [STD_BARTITSU, STD_VIGNY, STD_KODOKAN, STD_SAVATE, STD_QUEENSBERRY],
        "citations": [CIT_BARTONWRIGHT_1899, CIT_BARTONWRIGHT_1901, CIT_WOLF],
        "sig_lens": (
            "Signature original interpretation: his original Signature Combat "
            "Method treats Bartitsu as the first Signature system - four arts "
            "woven into one covenant of self-protection, the cane the line, "
            "the kick the measure, the blow the sentence, the throw the full "
            "stop. Clearly labeled Signature-made."),
    },
    {
        "key": "guard_stance",
        "name": "The Bartitsu Guard Stance",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "The Bartitsu guard stance is the platform every technique is "
            "launched from and recovered to. The student stands with feet "
            "roughly shoulder-width apart, the lead foot (usually the left) "
            "pointing toward the opponent and the rear foot turned out at "
            "about forty-five degrees, the knees softly bent, the body weight "
            "resting slightly forward of center so the body can move in any "
            "direction without first shifting. The rear hand holds the cane "
            "in the Vigny grip with the point forward and up; the lead hand "
            "is raised to guard height, chin tucked behind it, elbows drawn "
            "in to protect the ribs. Barton-Wright's boxers taught a "
            "pugilistic guard adapted for the street: hands up, chin down, "
            "eyes on the opponent's chest. The stance must survive three "
            "tests: it does not wobble when pushed lightly from any side, it "
            "lets the student advance, retreat, or side-step without "
            "re-chambering, and it keeps the cane hand free to cut, thrust, "
            "or hook. Drill the stance until it feels like standing - "
            "balance first, everything else after."),
        "how_it_works": (
            "The stance works by turning the body into a loaded spring. Bent "
            "knees store the leg drive for punches, kicks, and throws; the "
            "staggered feet give a wide base fore-and-aft so forward pressure "
            "never topples the fighter backward; the bladed torso (one "
            "shoulder forward) presents a narrow target while keeping both "
            "hands and both feet in striking range. Weight sits roughly "
            "sixty percent on the balls of the feet, ready to move, and forty "
            "percent through the heels for stability. When the student "
            "advances, the front foot moves first; when retreating, the rear "
            "foot moves first - the base never narrows mid-step, so the "
            "spring is never unloaded at the wrong moment."),
        "key_points": [
            "Feet shoulder-width apart: lead foot toward the opponent, rear foot turned out about forty-five degrees.",
            "Knees softly bent, weight slightly forward of center, sixty percent on the balls of the feet.",
            "Cane hand holds the Vigny grip with point forward and up; lead hand guards the chin; chin tucked.",
            "Bladed torso presents a narrow target while keeping all four weapons - two hands, two feet, plus cane - in range.",
            "The stance must pass the push test: no wobble when pushed lightly from any side.",
            "Front foot leads the advance, rear foot leads the retreat, so the base never narrows mid-step.",
        ],
        "requirements": [
            "Hold the stance for two-minute intervals; build to five minutes without the knees straightening.",
            "Have a partner push lightly from front, side, and back; re-set until balance holds from all directions.",
            "Keep the lead hand up and the chin down throughout; dropping the hands is the first fault to correct.",
            "Practice the stance with the cane in hand from the first session so the grip becomes part of the guard.",
        ],
        "standards": [STD_BARTITSU, STD_QUEENSBERRY],
        "citations": [CIT_BARTONWRIGHT_1899, CIT_QUEENSBERRY],
        "sig_lens": (
            "Signature original interpretation: his original Signature Combat "
            "Method treats the stance as the oath posture - feet planted like "
            "the pillars of a covenant, weight forward like a signature "
            "pressed into the page. Clearly labeled Signature-made."),
    },
    {
        "key": "footwork",
        "name": "Bartitsu Footwork: Advance, Retreat, and Side Step",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Footwork is the Bartitsu student's engine: every strike, parry, "
            "and throw is carried by the feet, and the Victorian masters "
            "drilled it before any weapon was lifted. The advance moves the "
            "front foot forward first and brings the rear foot up behind it, "
            "covering ground while the guard stays intact; the retreat "
            "reverses the order, the rear foot moving first so the student "
            "is never caught with feet together; the side step slides the "
            "body off the opponent's center line, left or right, without "
            "turning the shoulders. A fourth motion, the pass, brings the "
            "rear foot through to become the lead foot, switching the stance "
            "for an angle change or a lunging thrust. The rules are "
            "absolute: never cross the feet, never let the feet come "
            "together, keep the knees bent and the head level - bobbing up "
            "and down telegraphs every move. Drills begin in straight lines "
            "(advance three, retreat three), progress to the box (advance, "
            "side, retreat, side), and finish with free movement while a "
            "partner calls directions. Footwork wins fights the hands cannot: "
            "the student who controls distance controls the fight."),
        "how_it_works": (
            "Footwork works by managing the measure - the distance between "
            "the fighters - so the student is always either in range to "
            "strike or out of range to be hit, never in the dead middle. The "
            "advance closes the measure while the guard stays loaded, so "
            "strikes land with body weight behind them; the retreat opens "
            "the measure while the cane stays pointed at the threat, so the "
            "attacker walks onto the point; the side step changes the angle "
            "so the opponent must re-aim while the student is already "
            "striking. Because each step preserves the stance's geometry, "
            "the fighter can punch, kick, cut, or throw from any footwork "
            "position - the engine never stalls between gears."),
        "key_points": [
            "Advance: front foot moves first, rear foot follows; the guard never drops.",
            "Retreat: rear foot moves first, front foot follows; the cane stays pointed at the threat.",
            "Side step: slide off the center line left or right without turning the shoulders.",
            "Pass: rear foot steps through to become the new lead, switching stance for angles and lunges.",
            "Never cross the feet and never let them come together; keep the head level, knees bent.",
            "Drill progression: straight lines, then the box, then free movement on a partner's calls.",
        ],
        "requirements": [
            "Drill straight-line advance and retreat for three-minute rounds, cane in hand, guard intact.",
            "Practice the box pattern until direction changes need no thought: advance, side, retreat, side.",
            "Have a partner advance on you; retreat and side-step while keeping the cane point between you.",
            "Do not practice footwork on slippery floors; street shoes on firm ground match the Victorian setting.",
        ],
        "standards": [STD_BARTITSU, STD_VIGNY, STD_SAVATE],
        "citations": [CIT_BARTONWRIGHT_1899, CIT_VIGNY],
        "sig_lens": (
            "Signature original interpretation: his original Signature Combat "
            "Method treats footwork as the writing of the signature - the "
            "advance the downstroke, the retreat the lift of the pen, the "
            "side step the flourish that changes the whole meaning. Clearly "
            "labeled Signature-made."),
    },
    {
        "key": "cane_grip",
        "name": "The Vigny Cane Grip and Basic Portes",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The Vigny cane grip is how Pierre Vigny's method puts the "
            "walking stick into the fighter's hand, and Barton-Wright adopted "
            "it as Bartitsu's core weapon grip. The student takes the cane "
            "about a hand's breadth from the head (or the ferrule end, "
            "method varies by school), the thumb laid along the shaft for "
            "point control, the fingers wrapping firmly but not white-knuckled "
            "- the grip must be supple enough to let the cane roll for "
            "moulinets yet firm enough to parry a descending cut. The "
            "hand is held at about waist height, the cane angled up and "
            "forward with the point threatening the opponent's face, the "
            "elbow relaxed at the side. From this guard the portes - the "
            "carrying positions - branch out: high port for overhead cuts, "
            "middle port for horizontal cuts and thrusts, low port for leg "
            "attacks and rising cuts. Vigny's genius was treating the cane "
            "like the sabre: cuts are thrown with the last third of the "
            "shaft (the foible), parries are taken with the third nearest "
            "the hand (the forte), and the wrist, not the arm, does most of "
            "the steering. A proper cane for the art is straight, stout "
            "malacca or similar hardwood, about thirty-six inches, with a "
            "head heavy enough to add weight to a cut."),
        "how_it_works": (
            "The grip works as a lever control. The hand is the fulcrum; "
            "the thumb along the shaft senses the cane's angle the way a "
            "fencer's fingers sense a foil, giving point control for thrusts "
            "and moulinets. Holding a hand's breadth from the end shortens "
            "the lever for quick parries while keeping enough shaft forward "
            "for reach; sliding the grip is forbidden mid-exchange because "
            "it costs the fraction of a second that decides a parry. The "
            "portes position the lever before the action: high port pre-"
            "loads the descending cut, middle port pre-loads the thrust, low "
            "port pre-loads the rising cut. Power comes from the legs and "
            "hip turn driving through a relaxed shoulder and supple wrist - "
            "the cane is the last link of a chain that starts at the floor."),
        "key_points": [
            "Grip the cane about a hand's breadth from the head, thumb along the shaft, fingers firm but supple.",
            "Hold the hand at waist height with the point up and forward, threatening the opponent's face.",
            "High, middle, and low portes pre-load the descending cut, the thrust, and the rising cut.",
            "Strike with the last third of the shaft (the foible); parry with the third nearest the hand (the forte).",
            "The wrist steers, the legs and hips power; the cane is the last link of a chain from the floor.",
            "Use a straight stout hardwood cane about thirty-six inches; never grip-slip mid-exchange.",
        ],
        "requirements": [
            "Practice picking up the grip blindfolded-style: from the carry, snap to middle port in under a second.",
            "Roll the cane in slow moulinets daily to build the supple wrist the grip depends on.",
            "Check the cane for cracks before every session; a split shaft fails under a hard parry.",
            "Never point the cane at a training partner's eyes in drills; aim points are agreed before each round.",
        ],
        "standards": [STD_VIGNY, STD_BARTITSU],
        "citations": [CIT_VIGNY, CIT_BARTONWRIGHT_1901],
        "sig_lens": (
            "Signature original interpretation: his original Signature Combat "
            "Method treats the grip as the oath itself - the hand swearing "
            "allegiance to the line, the thumb the seal pressed along the "
            "shaft, every porte a posture of the covenant. Clearly labeled "
            "Signature-made."),
    },
    {
        "key": "ukemi",
        "name": "Ukemi: How to Fall Safely",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Ukemi, the art of falling safely, came into Bartitsu with Yukio "
            "Tani's jujutsu and is drilled before any throw is practiced. "
            "The back breakfall: tuck the chin to the chest, round the back, "
            "slap the mat hard with both arms at forty-five degrees as the "
            "shoulders land, and exhale on impact. The side breakfall: turn "
            "the body slightly, land on the whole side from shoulder to hip, "
            "one arm slapping, the other guarding. The forward roll: make a "
            "wheel of the arm from hand to shoulder, tuck the head, roll "
            "diagonally across the back from one shoulder to the opposite "
            "hip, and slap as the body comes flat. Three principles govern "
            "all of them: spread the impact over the largest possible area, "
            "never post a straight arm (the classic broken wrist), and never "
            "let the head strike the ground - the chin stays tucked and the "
            "slap of the arms absorbs the shock that would otherwise reach "
            "the skull. Students begin from kneeling, progress to standing, "
            "and only then take falls from real throws. Ukemi is the art's "
            "insurance policy: Barton-Wright's gentlemen could practice "
            "throws daily precisely because they could fall without injury."),
        "how_it_works": (
            "Ukemi works by physics, not courage. A falling body carries "
            "kinetic energy that must go somewhere; the breakfall converts "
            "it across time and area. Slapping the mat with the arms "
            "increases the contact area and recruits the broad muscles of "
            "the back and side to absorb the load, while the rounded spine "
            "lets the body roll through the impact instead of stopping dead "
            "against it. Exhaling on impact keeps the diaphragm from taking "
            "the shock as a gasp. The forward roll goes further: it turns "
            "the fall into a wheel, so the body never receives the full "
            "force at one point at one instant. Drilled to reflex, ukemi "
            "fires before conscious thought - the student thrown in randori "
            "is slapping and rolling before the fear arrives."),
        "key_points": [
            "Back breakfall: chin tucked, back rounded, both arms slap at forty-five degrees, exhale on impact.",
            "Side breakfall: land on the whole side, one arm slaps, the other guards the head.",
            "Forward roll: wheel from hand to shoulder, roll diagonally shoulder to opposite hip.",
            "Never post a straight arm; never let the head touch the ground; spread impact over maximum area.",
            "Progression: kneeling, then standing, then falls from real throws - never skip a stage.",
            "Ukemi is drilled before any throw; it is the insurance policy that makes daily throwing practice possible.",
        ],
        "requirements": [
            "Practice on mats or grass only until the falls are silent and reflexive; never on concrete.",
            "A partner or instructor watches the first hundred falls for the two fatal faults: posted arms and lifted chin.",
            "Slap hard enough to hear it; a quiet fall is a fall that kept its energy inside the body.",
            "Stop and rest if dizziness or nausea appears; repeated falls compress the spine and need pacing.",
        ],
        "standards": [STD_KODOKAN, STD_BARTITSU],
        "citations": [CIT_KANO, CIT_BARTONWRIGHT_1899],
        "sig_lens": (
            "Signature original interpretation: his original Signature Combat "
            "Method treats the fall as the signature's flourish - the body "
            "signing its descent across the mat, the slap the dot that ends "
            "the stroke, the roll the line that carries on. Clearly labeled "
            "Signature-made."),
    },
    {
        "key": "straight_blow",
        "name": "The Straight Blow: Bartitsu Boxing Basics",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The straight blow is Bartitsu's fundamental punch, drawn from "
            "English pugilism under the Queensberry lineage. The lead "
            "straight (the jab): the lead fist shoots straight from the "
            "guard, rotating a quarter turn so the knuckles land flat, the "
            "shoulder rising to shield the chin, the punch snapping back "
            "along the same line. The rear straight (the cross): the rear "
            "foot pivots, the hip and shoulder rotate into the blow, the "
            "fist travels the shortest line from chin to target - nose, jaw, "
            "or solar plexus - and returns to guard. Barton-Wright's "
            "pugilists insisted on five points: strike with the knuckles of "
            "the index and middle fingers, keep the wrist straight and the "
            "thumb outside the fist, hit through the target not at it, "
            "breathe out sharply on every blow, and never drop the other "
            "hand. The straight blow is thrown from the feet up - the "
            "push of the rear leg, the turn of the hip, the snap of the "
            "shoulder, the fist last - which is why a trained straight "
            "carries many times the power of an arm punch. Drill on the bag "
            "for power, with a partner's focus mitts (or held pads) for "
            "accuracy, and shadow-box for the footwork that delivers it."),
        "how_it_works": (
            "The straight blow works by the kinetic chain and the straight "
            "line. Force generated by the legs pushing against the ground "
            "travels up through the rotating hips and torso and out along "
            "the extended arm, arriving at the knuckles multiplied many "
            "times over what the arm alone could produce. The straight line "
            "is the shortest path, so the blow lands before wider punches "
            "and is hardest to see coming; the quarter-turn rotation of the "
            "fist locks the wrist and aligns the knuckles, index and middle "
            "first, into a single striking surface. Snapping the punch back "
            "does two jobs: it cuts the opponent's chance to catch the arm, "
            "and it chambers the next blow. The exhale on impact tightens "
            "the core at the moment of contact, bracing the whole body "
            "behind the fist."),
        "key_points": [
            "Lead straight: fist shoots from guard, rotates a quarter turn, snaps back along the same line.",
            "Rear straight: rear foot pivots, hip and shoulder rotate in, fist travels chin to target.",
            "Strike with index and middle knuckles, wrist straight, thumb outside the fist.",
            "Hit through the target, breathe out sharply, never drop the guarding hand.",
            "Power comes from the feet up: leg push, hip turn, shoulder snap, fist last.",
            "Drill on the bag for power, pads for accuracy, shadow-boxing for the footwork that delivers it.",
        ],
        "requirements": [
            "Wrap the hands and wear bag gloves for bag work; bare knuckles belong to no drill.",
            "Keep the chin tucked behind the shoulder on every blow; the punch must not open the guard.",
            "Throw the blow in combination with footwork: advance with the jab, pivot with the cross.",
            "Stop immediately if the wrist aches; a bent wrist on impact is the commonest boxing injury.",
        ],
        "standards": [STD_QUEENSBERRY, STD_BARTITSU],
        "citations": [CIT_QUEENSBERRY, CIT_BARTONWRIGHT_1899],
        "sig_lens": (
            "Signature original interpretation: his original Signature Combat "
            "Method treats the straight blow as the signature's underline - "
            "drawn straight and true from the oath of the stance, the "
            "knuckles the pen's nib, the return the hand lifting ready for "
            "the next line. Clearly labeled Signature-made."),
    },
    {
        "key": "front_kick",
        "name": "The Savate Front Kick",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The savate front kick is Bartitsu's long-range leg weapon, "
            "inherited from the French boxe francaise codified by Charles "
            "Lecour and Joseph Charlemont. Because savate is fought in "
            "shoes, the kick strikes with the shod foot - the toe of the "
            "shoe for the piercing front kick, the sole for the driving "
            "version. The mechanics: from guard, the knee of the kicking leg "
            "chambers up high and tight, the hips tilt forward, and the leg "
            "extends like a piston, striking with the toe or sole into the "
            "opponent's shin, knee, thigh, or midsection, then rechambers "
            "along the same path. The supporting leg stays slightly bent, "
            "the heel grounded, the arms holding guard - the kick must never "
            "cost the fighter's balance. Charlemont's teaching insists the "
            "kick is a thrust of the whole body: the hips drive forward as "
            "the leg extends, adding body weight to the shoe leather. "
            "Targets follow the ladder: beginners drill the kick into the "
            "thigh and midsection of a held pad; advanced students work the "
            "piercing toe kick to the knee and shin. The front kick's great "
            "virtue in Bartitsu is range: it reaches further than any punch, "
            "so it is the art's answer to an attacker who has not yet "
            "closed to cane distance."),
        "how_it_works": (
            "The front kick works as a piston driven by the hips. "
            "Chambering the knee first loads the leg like a spring and hides "
            "the kick's target until the last instant; extending from the "
            "chamber gives the foot a straight-line path that is fast and "
            "hard to intercept. The hip drive is the multiplier: by tilting "
            "the pelvis forward as the leg extends, the fighter adds the "
            "mass of the torso behind the few kilograms of the foot, "
            "turning a leg strike into a body-weight strike. Striking with "
            "the shod toe concentrates the force on a small point for "
            "piercing effect, while the sole spreads it for a pushing, "
            "off-balancing drive. Rechambering along the same path keeps "
            "the leg from being caught and returns the fighter to guard "
            "without a balance debt."),
        "key_points": [
            "Chamber the knee high and tight, tilt the hips forward, extend the leg like a piston.",
            "Strike with the toe of the shoe for piercing, the sole for driving and off-balancing.",
            "Hips drive forward with the extension; the kick carries body weight, not just leg weight.",
            "Supporting leg slightly bent, heel grounded, arms holding guard throughout.",
            "Beginners target thigh and midsection on pads; advanced students work the piercing toe to knee and shin.",
            "Rechamber along the same path; never let the kicking leg dangle where it can be caught.",
        ],
        "requirements": [
            "Drill in firm street-style shoes on a non-slip surface; savate is a shod art.",
            "Hold a partner's pad or heavy bag for targets; never full-force kick a partner's unprotected leg.",
            "Keep the guard hands up during every kick; dropping them to swing the leg is the first fault.",
            "Stretch the hip flexors and hamstrings before kicking sessions; the chamber demands both.",
        ],
        "standards": [STD_SAVATE, STD_BARTITSU],
        "citations": [CIT_CHARLEMONT, CIT_BARTONWRIGHT_1899],
        "sig_lens": (
            "Signature original interpretation: his original Signature Combat "
            "Method treats the front kick as the signature's exclamation - "
            "the chamber the raised pen, the piston extension the mark "
            "struck, the rechamber the hand returning to rest. Clearly "
            "labeled Signature-made."),
    },
    {
        "key": "cane_guards",
        "name": "Cane Guards: Tierce and Quarte",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Tierce and quarte are the two high cane guards Bartitsu borrows "
            "from the sabre, and they are the foundation of all Vigny cane "
            "defense. In tierce (third), the hand holds the cane with the "
            "knuckles up and the point angled up and to the outside, "
            "covering the outer high line - the right side of the body for a "
            "right-handed fighter - against descending and outside cuts. In "
            "quarte (fourth), the hand turns knuckles inward and the point "
            "angles up and across to the inside, covering the inner high "
            "line against cuts to the head's left side and thrusts to the "
            "chest. The two guards are sisters: the fighter shifts between "
            "them with a small rotation of the wrist, never a big arm "
            "movement, so the point stays threatening while the guard "
            "changes. Vigny's teaching adds the low guards - prime and "
            "seconde - for the legs, but tierce and quarte come first "
            "because the head is the target every attacker reaches for. "
            "Drill the guards against a partner's slow descending cuts, "
            "alternating sides on command, until the wrist turns without "
            "thought. A guard is not a wall; it is a position of readiness "
            "from which the riposte - the answering cut - is already half "
            "thrown."),
        "how_it_works": (
            "The guards work by geometry and economy. The cane held high "
            "with the point up creates a roof over the head and upper body; "
            "any descending cut aimed at the head must cross the cane's "
            "line, and crossing it meets the forte - the strong third near "
            "the hand - which stops the blow without the defender absorbing "
            "its force in the wrist. Tierce covers the outside because the "
            "blade angles across that line; quarte covers the inside for the "
            "same reason. The wrist-only transition between them is the "
            "economy: small motion means the guard changes faster than the "
            "attacker can change the attack's line, so the defense always "
            "arrives first. And because each guard is also a chambered cut "
            "or thrust, defense and counterattack are one motion, not two."),
        "key_points": [
            "Tierce: knuckles up, point up and outside; covers the outer high line.",
            "Quarte: knuckles in, point up and across; covers the inner high line.",
            "Shift between them with wrist rotation only; keep the point threatening throughout.",
            "Incoming cuts meet the forte (the strong third near the hand), not the wrist.",
            "Tierce and quarte come before the low guards because the head is the first target.",
            "Each guard is a chambered riposte; defense and counterattack are one motion.",
        ],
        "requirements": [
            "Drill against slow partner cuts, alternating tierce and quarte on a spoken command.",
            "Keep the elbow relaxed and close; a stiff raised arm slows the wrist transition.",
            "Wear head protection when partner drills speed up; even controlled cuts can slip.",
            "Check that the point stays up: a drooping cane guards nothing and invites the thrust.",
        ],
        "standards": [STD_VIGNY, STD_BARTITSU],
        "citations": [CIT_VIGNY, CIT_BARTONWRIGHT_1901],
        "sig_lens": (
            "Signature original interpretation: his original Signature Combat "
            "Method treats tierce and quarte as the two brackets of the "
            "signature - one guarding the outer flourish, one the inner, "
            "the wrist's small turn the hand's quiet decision. Clearly "
            "labeled Signature-made."),
    },
]
ENTRIES += [
    {
        "key": "distance_timing",
        "name": "Distance and Timing: The Measure of the Fight",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Distance and timing - the measure and the tempo - are the twin "
            "sciences that make every Bartitsu technique work. The measure "
            "is the distance between fighters, and Bartitsu names three: "
            "long measure (cane range, where cuts and thrusts rule), middle "
            "measure (kicking and punching range), and close measure "
            "(clinch range, where throws and locks live). The master knows "
            "at all times which measure he stands in and which weapons are "
            "live in it. Timing is the choice of moment: the single tempo "
            "(strike as the opponent commits), the counter-tempo (strike "
            "into the opponent's preparation), and the half-tempo (draw the "
            "attack, then punish it). Barton-Wright taught that a perfect "
            "technique at the wrong measure is a missed technique, and a "
            "perfect measure at the wrong tempo is an invitation. The drill "
            "is the measure walk: partners advance and retreat while calling "
            "the measure aloud, then add single-tempo attacks on the caller's "
            "mark, learning to feel distance the way a musician feels beat. "
            "Every later record in this database assumes the student can "
            "read the measure and hear the tempo; without them, the finest "
            "cut is only waving a stick."),
        "how_it_works": (
            "Distance and timing work by control of initiative. At long "
            "measure the cane fighter is safe and the opponent must cross "
            "empty ground to reach him - every step of that crossing is a "
            "tempo the defender can use. At middle measure the kicker and "
            "puncher trade speed for power, and the one who reads the "
            "opponent's weight shift first lands first. At close measure "
            "the thrower wants contact, and timing decides who throws whom: "
            "the throw landed in the half-tempo, as the opponent's weight "
            "commits forward, needs a fraction of the force of a throw "
            "forced against a balanced stance. The counter-tempo is the "
            "crown: striking into the opponent's preparation means his "
            "attack is still being born while yours is already arriving - "
            "two motions cannot occupy the same tempo, and yours owns it."),
        "key_points": [
            "Three measures: long (cane range), middle (kick and punch range), close (clinch and throw range).",
            "Know which weapons are live at your current measure; never throw a punch from cane range.",
            "Three tempos: single (as he commits), counter-tempo (into his preparation), half-tempo (draw then punish).",
            "A perfect technique at the wrong measure misses; a perfect measure at the wrong tempo invites.",
            "The counter-tempo owns the exchange: his attack is still being born while yours arrives.",
            "Drill the measure walk: partners call the measure aloud while advancing and retreating.",
        ],
        "requirements": [
            "Practice measure calling until you can name the measure without looking down or hesitating.",
            "Drill single-tempo attacks on a caller's mark before attempting counter-tempo work.",
            "Keep a training journal of sparring rounds noting which measure each exchange happened in.",
            "Never sacrifice measure for speed; reaching with a technique is the commonest timing fault.",
        ],
        "standards": [STD_BARTITSU, STD_VIGNY, STD_SAVATE],
        "citations": [CIT_BARTONWRIGHT_1899, CIT_VIGNY],
        "sig_lens": (
            "Signature original interpretation: his original Signature Combat "
            "Method treats measure as the margins of the page and tempo as "
            "the rhythm of the hand - the signature is only valid when "
            "written in the right space at the right moment. Clearly labeled "
            "Signature-made."),
    },
    {
        "key": "cane_parries",
        "name": "Basic Cane Parries",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The basic cane parries are Bartitsu's shield work: the small, "
            "precise interceptions that turn an incoming cut or thrust aside "
            "with the least motion. Against the descending cut to the head, "
            "the defender meets it with tierce or quarte, catching the "
            "attack on the forte and letting the cut slide off the angled "
            "cane. Against the horizontal cut to the ribs, the cane drops "
            "to a hanging guard, point down, and the blow is taken on the "
            "shaft's strong third while the body leans just clear. Against "
            "the thrust, the defender beats the point aside with a sharp "
            "lateral tap - the parry of quarte against an inside thrust, of "
            "tierce against an outside one - and the point passes harmlessly "
            "by the shoulder. Vigny's cardinal rules: parry with the forte, "
            "never the foible; move the cane, not the body, for small "
            "attacks; and always parry into the riposte - the parry that "
            "does not answer is only half a defense. Beginners drill each "
            "parry against slow, announced attacks; the speed rises only "
            "when the parry lands on the forte ten times in ten. A parried "
            "attack is a spent attack, and a spent attack is the defender's "
            "opening."),
        "how_it_works": (
            "Parries work by deflection, not opposition. Meeting a cut "
            "head-on with force would demand a stronger arm; meeting it at "
            "an angle with the forte redirects its energy past the body, "
            "spending a fraction of the strength the attack carried. The "
            "forte's mechanical advantage is decisive: force applied near "
            "the hand meets the attacker's force applied far from his hand, "
            "so the defender's small motion overpowers the attacker's big "
            "one - leverage, not muscle. The beat parry against the thrust "
            "works on timing rather than strength: a sharp lateral tap "
            "applied while the point is still traveling needs only to "
            "change its line by inches, because those inches grow with "
            "distance until the point misses the body entirely. Every parry "
            "finishes in a guard that is already a chambered cut, so the "
            "riposte follows in the same breath."),
        "key_points": [
            "Parry the descending cut with tierce or quarte, catching it on the forte.",
            "Parry the horizontal cut with a hanging guard, body leaning just clear.",
            "Parry the thrust with a lateral beat; inches of deflection at the cane become feet at the body.",
            "Parry with the forte, never the foible; move the cane, not the body, for small attacks.",
            "Always parry into the riposte; a parry that does not answer is half a defense.",
            "Drill at slow speed against announced attacks until the forte catches ten in ten.",
        ],
        "requirements": [
            "Wear head and hand protection once partner drills pass half speed.",
            "The attacker announces the line before each drill rep; unannounced attacks come only in advanced sparring.",
            "Keep the parry small; a wide parry opens the opposite line and wastes the tempo for the riposte.",
            "End every parry drill with the riposte, even at slow speed, to build the defense-attack habit.",
        ],
        "standards": [STD_VIGNY, STD_BARTITSU],
        "citations": [CIT_VIGNY, CIT_BARTONWRIGHT_1901],
        "sig_lens": (
            "Signature original interpretation: his original Signature Combat "
            "Method treats the parry as the signature's guard stroke - the "
            "hand turning aside what would blot the page, the forte the "
            "firm part of the line that cannot be crossed. Clearly labeled "
            "Signature-made."),
    },
    {
        "key": "overhead_cut",
        "name": "The Vigny Overhead Cut",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The overhead cut - the descending cut from high port - is the "
            "Vigny cane's signature attack and Bartitsu's answer to a "
            "rush. From high port (cane raised above and behind the "
            "shoulder, point up), the fighter steps in with the lead foot, "
            "drives the hip forward, and brings the cane down in a "
            "diagonal or vertical arc, striking with the foible - the last "
            "third of the shaft - and cutting through the target toward the "
            "ground rather than stopping at contact. The traditional "
            "targets are the attacker's head, collarbone, and weapon arm: "
            "the cut is thrown to stop a charge, not to duel with it. "
            "Vigny's mechanics demand the whole chain: the step supplies "
            "the mass, the hip turn supplies the rotation, the shoulder "
            "stays relaxed so the arm is a whip, and the wrist snaps at the "
            "last instant to multiply tip speed. The cut finishes low, the "
            "fighter's body bladed and guarded, ready to cut again on the "
            "return or thrust from the low line. Drilled first in the air "
            "for form, then on the heavy bag or a straw target for the feel "
            "of the cut biting, never full force against a partner. The "
            "overhead cut is the technique that made the Victorian walking "
            "stick a weapon: one committed descending cut, properly "
            "delivered, ends the argument the ruffian started."),
        "how_it_works": (
            "The overhead cut works by converting body weight and rotation "
            "into tip speed. The stepping-in carries the fighter's mass "
            "forward; the hip turn rotates that mass; the relaxed arm "
            "transmits the rotation to the cane; and the final wrist snap "
            "whips the foible through the last degrees of arc at several "
            "times the hand's speed. Because kinetic energy rises with the "
            "square of velocity, that last snap contributes more to the "
            "cut's power than the whole arm swing before it. Cutting "
            "through the target - following the arc past contact instead of "
            "stopping at it - keeps the cane moving at full speed through "
            "the impact zone, the way a woodsman's axe follows through the "
            "log. The diagonal line is preferred over the pure vertical "
            "because it is harder to parry with a raised arm and because it "
            "carries naturally into the guard for the next action."),
        "key_points": [
            "From high port, step in with the lead foot, drive the hip, and bring the cane down in a diagonal arc.",
            "Strike with the foible; cut through the target toward the ground, never stopping at contact.",
            "Targets: head, collarbone, weapon arm - the cut is thrown to stop a rush.",
            "Power chain: step, hip turn, relaxed shoulder, wrist snap at the last instant.",
            "Tip speed - and the wrist snap that makes it - contributes most of the cut's energy.",
            "Drill in the air for form, on the bag or straw for bite; never full force on a partner.",
        ],
        "requirements": [
            "Master the grip and high port before attempting the full cut; a loose grip at speed is dangerous.",
            "Practice the cut in a clear space with no one within two cane-lengths in any direction.",
            "Wear eye protection when drilling with a partner holding a target; splinters and slips happen.",
            "Finish every cut in a guard, low and bladed; the cut that ends in a sprawl invites the counter.",
        ],
        "standards": [STD_VIGNY, STD_BARTITSU],
        "citations": [CIT_VIGNY, CIT_BARTONWRIGHT_1901],
        "sig_lens": (
            "Signature original interpretation: his original Signature Combat "
            "Method treats the overhead cut as the signature's bold "
            "downstroke - the whole body signing at once, the wrist's snap "
            "the final press of the pen, the follow-through the ink carrying "
            "past the line. Clearly labeled Signature-made."),
    },
    {
        "key": "moulinet",
        "name": "The Moulinet: Figure-of-Eight Cane Strike",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The moulinet is the Vigny cane's continuous figure-of-eight "
            "rotation, and in Bartitsu it serves as moving guard, feint, and "
            "attack all at once. The fighter holds the cane in the Vigny "
            "grip and rolls the wrist so the point traces a horizontal or "
            "diagonal figure of eight in front of the body, the cane never "
            "stopping, each loop flowing into the next. At slow speed the "
            "moulinet is a guard: the moving cane covers the high lines and "
            "the opponent cannot find a clean entry. At speed it becomes a "
            "storm of cuts: either loop of the eight can be released into a "
            "full cut to the head or arm, and because the cane is already "
            "moving, the strike arrives with the rotation's momentum behind "
            "it. Vigny taught the moulinet as the bridge between defense "
            "and offense - the fighter under pressure keeps the eight "
            "turning until the opening shows, then lets one loop fly. The "
            "wrist does the work, the arm only guides; a stiff arm kills "
            "the figure and telegraphs the release. Drill the eight slowly "
            "in both directions until the loops are even and the cane never "
            "wobbles, then build speed, then practice releasing cuts from "
            "either loop on a partner's call. The moulinet is Bartitsu's "
            "answer to being rushed: a wall that bites."),
        "how_it_works": (
            "The moulinet works by perpetual motion and ambiguity. A "
            "continuously rotating cane is a moving barrier: any attack "
            "aimed at the body must cross the plane of rotation, and "
            "crossing it means meeting the cane at speed - the attacker "
            "supplies the target, the defender only maintains the wall. "
            "The figure of eight is the optimal pattern because it covers "
            "both high lines (left and right) in one cycle with no dead "
            "point where the cane reverses direction; unlike a simple "
            "circle, the eight's crossover keeps the point moving fastest "
            "through the center, exactly where attacks arrive. Releasing a "
            "cut from the rotation is devastating because the strike "
            "inherits the angular momentum already stored in the cane - no "
            "wind-up, no telegraph, the wall simply becomes a weapon in "
            "one loop."),
        "key_points": [
            "Roll the wrist so the point traces a continuous figure of eight; never stop the cane.",
            "Slow moulinet is a moving guard covering both high lines with no dead point.",
            "Either loop can release into a full cut; the strike inherits the rotation's momentum.",
            "The wrist does the work, the arm only guides; a stiff arm kills the figure.",
            "Drill both directions until the loops are even and wobble-free, then add speed, then releases.",
            "The moulinet is the bridge: keep the eight turning under pressure until the opening shows.",
        ],
        "requirements": [
            "Build wrist suppleness with slow eights before any speed; forcing speed early strains the wrist.",
            "Practice in an open space; a fast moulinet needs a full cane-length of clearance all around.",
            "Release drills use pads or bags only; never release a full cut at a partner.",
            "Alternate directions each round to develop both wrists and avoid one-sided strain.",
        ],
        "standards": [STD_VIGNY, STD_BARTITSU],
        "citations": [CIT_VIGNY, CIT_BARTONWRIGHT_1901],
        "sig_lens": (
            "Signature original interpretation: his original Signature Combat "
            "Method treats the moulinet as the signature written in the air "
            "without lifting the pen - the endless eight the hand's "
            "meditation, the released cut the moment the meditation becomes "
            "a decision. Clearly labeled Signature-made."),
    },
    {
        "key": "o_goshi",
        "name": "O Goshi: The Cross Buttock Hip Throw",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "O goshi, the major hip throw, is the first throw in Bartitsu's "
            "jujutsu ladder, taught by Yukio Tani's lineage and codified in "
            "Kodokan judo. The mechanics are a model of leverage. The "
            "thrower steps in close, turning the back to the opponent while "
            "the throwing arm wraps around the opponent's waist (or grips "
            "the belt), pulling him tight against the hip. The thrower's "
            "hips sit lower than the opponent's, the knees bent, the back "
            "straight. Then in one motion the thrower straightens the legs, "
            "pulls the opponent's upper body forward and down with the "
            "wrapping arm, and rotates the hips - the opponent, draped over "
            "the hip fulcrum, arcs over and lands on his back. The classic "
            "faults are turning without pulling (the opponent simply steps "
            "around), bending at the waist instead of the knees (the back "
            "takes the load), and throwing without breaking the opponent's "
            "balance first - the kuzushi, the off-balancing pull that makes "
            "the throw possible. Drill the entry without the throw, then the "
            "throw onto crash mats with a partner who knows ukemi, then "
            "against increasing resistance. O goshi teaches the lesson of "
            "all hip throws: the hip is a fulcrum, the opponent a lever, "
            "and leverage beats strength."),
        "how_it_works": (
            "O goshi works as a first-class lever. The thrower's hip is the "
            "fulcrum placed under the opponent's center of mass; the "
            "thrower's arms and the opponent's own body form the lever. "
            "Once the opponent's balance is broken forward (kuzushi), his "
            "weight is already committed past his base, and the hip fulcrum "
            "gives the thrower a mechanical advantage of several to one - a "
            "lighter fighter throws a heavier one because leverage, not "
            "muscle, does the lifting. Straightening the legs drives the "
            "fulcrum up under the load while the arms pull the top of the "
            "lever over, rotating the opponent around the hip and onto his "
            "back. The throw fails whenever the fulcrum is misplaced (hips "
            "too high), the lever is disconnected (no tight pull-in), or "
            "the load is still balanced (no kuzushi) - which is why the "
            "entry and the off-balance are drilled more than the throw "
            "itself."),
        "key_points": [
            "Step in, turn the back, wrap the throwing arm around the waist; pull the opponent tight to the hip.",
            "Hips lower than the opponent's, knees bent, back straight - the hip is the fulcrum.",
            "Break the balance forward first (kuzushi); without it the throw is only wrestling.",
            "Straighten the legs, pull the upper body down and around, rotate the hips in one motion.",
            "Never bend at the waist; never throw without the pull-in; never skip the ukemi prerequisite.",
            "The hip is a fulcrum, the opponent a lever; leverage beats strength.",
        ],
        "requirements": [
            "Both partners must have solid ukemi before the first live throw; no exceptions.",
            "Drill the entry and pull-in for weeks before the full throw; the throw is the easy part.",
            "Throw onto mats or soft ground only; the landing is the dangerous half of the technique.",
            "The person thrown controls the drill's pace; the thrower never surprises the partner with full force.",
        ],
        "standards": [STD_KODOKAN, STD_BARTITSU],
        "citations": [CIT_KANO, CIT_BARTONWRIGHT_1899],
        "sig_lens": (
            "Signature original interpretation: his original Signature Combat "
            "Method treats o goshi as the signature's turning of the page - "
            "the hip the crease, the opponent the sheet, the throw the hand "
            "turning what was written against the writer. Clearly labeled "
            "Signature-made."),
    },
    {
        "key": "hook_punch",
        "name": "The Hook Punch",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The hook is pugilism's great close-range punch, and Bartitsu's "
            "boxers threw it as the natural partner of the straight blow. "
            "The lead hook: from guard, the lead elbow rises to shoulder "
            "height, the arm bent at roughly ninety degrees, the fist "
            "vertical (thumb up) or horizontal, and the body pivots on the "
            "lead foot as the hip and shoulder whip the fist in a tight "
            "horizontal arc to the opponent's jaw, temple, or ribs. The "
            "rear hook follows the same mechanics with the rear hand, "
            "driven by the pivot of the rear foot. The Victorian teaching "
            "insists on the pivot: the hook's power comes from the rotation "
            "of the whole body around the planted foot, not from the arm "
            "swinging. The elbow stays bent and high - a dropped elbow "
            "turns the hook into a slap, and a straightened arm turns it "
            "into a wild swing. The hook pairs with the straight blow in "
            "the classic one-two: straight to open the guard, hook to go "
            "around it. Drill on the heavy bag for the pivot and the snap, "
            "on pads for accuracy to the jaw line, and in shadow for the "
            "footwork that sets the angle. The hook is the punch that "
            "finishes what the straight begins."),
        "how_it_works": (
            "The hook works by rotational power and the arc. Pivoting on "
            "the lead foot while the hip and shoulder rotate whips the bent "
            "arm around like a flail; the fist, traveling on a radius of "
            "roughly the forearm's length from the shoulder, arrives with "
            "the full angular velocity of the body's rotation concentrated "
            "in the small mass of the fist. The bent elbow is structural: "
            "it keeps the arm rigid enough to transmit the rotation yet "
            "short enough that the arc stays tight and fast. Striking the "
            "jaw or temple with a horizontal arc rotates the head sharply, "
            "which is what produces the stunning effect - the hook does not "
            "push the head back, it snaps it sideways. The pivot foot is "
            "the secret: without it the body cannot rotate, and without "
            "rotation the hook is only an arm punch."),
        "key_points": [
            "Lead elbow rises to shoulder height, arm bent at ninety degrees, fist vertical or horizontal.",
            "Pivot on the lead foot as hip and shoulder whip the fist in a tight horizontal arc.",
            "Power comes from whole-body rotation around the planted foot, never from the arm alone.",
            "Targets: jaw, temple, ribs; the hook snaps the head sideways where the straight pushes it back.",
            "Keep the elbow up; a dropped elbow makes a slap, a straight arm makes a wild swing.",
            "Classic pairing: straight blow to open the guard, hook to go around it.",
        ],
        "requirements": [
            "Wrap hands and wear bag gloves; the hook lands the knuckles at an angle that punishes bare wrists.",
            "Drill the pivot slowly first; the commonest fault is swinging the arm without turning the foot.",
            "Keep the guarding hand at the chin during every hook; the hook tempts fighters to drop it.",
            "Practice hooks to both head and body lines; the body hook sets up the head hook.",
        ],
        "standards": [STD_QUEENSBERRY, STD_BARTITSU],
        "citations": [CIT_QUEENSBERRY, CIT_BARTONWRIGHT_1899],
        "sig_lens": (
            "Signature original interpretation: his original Signature Combat "
            "Method treats the hook as the signature's curved flourish - the "
            "pivot the hand turning the page, the arc the pen sweeping "
            "around what the straight line could not reach. Clearly labeled "
            "Signature-made."),
    },
    {
        "key": "low_kick",
        "name": "The Savate Low Kick: Coup de Pied Bas",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The coup de pied bas - the low kick - is savate's great "
            "equalizer in Bartitsu, striking the opponent's shin, calf, or "
            "ankle with the inner edge or instep of the shod foot. The "
            "mechanics are economical: from guard the fighter lifts the "
            "knee slightly, swings the lower leg in a short arc, and drives "
            "the shoe's inner edge into the target with a snapping hip "
            "motion, then returns the foot to the ground at once. Because "
            "the kick travels a short path low to the ground, it is very "
            "fast and very hard to see; because it strikes the leg's "
            "supporting structure, even a moderate kick deadens the limb "
            "and ruins the opponent's footwork. Charlemont's teaching "
            "places the low kick as the setup weapon: kick the lead leg "
            "until the opponent shifts weight to protect it, then attack "
            "the newly exposed line - the kick is bait as much as weapon. "
            "The traditional targets are the outer calf, the shin, and the "
            "ankle; the knee itself is avoided in practice for safety. "
            "Drill on the heavy bag's lower third and on a partner's "
            "padded shin at controlled force. In the street, Barton-Wright "
            "noted, the low kick is the gentleman's answer to the ruffian's "
            "rush: it stops the legs, and a man who cannot stand cannot "
            "fight."),
        "how_it_works": (
            "The low kick works by attacking the foundation. The human "
            "stance is a structure, and the shin and calf are its pillars; "
            "a sharp blow to the pillar's side buckles it, and the whole "
            "structure - balance, footwork, the ability to advance - "
            "collapses with it. The kick's speed comes from its short arc: "
            "the foot travels only a fraction of the distance of a high "
            "kick, so it lands in roughly half the time, inside the "
            "opponent's reaction window. The snapping hip adds the body's "
            "rotation to the leg's swing, and the hard edge of the shoe "
            "concentrates that force on a narrow line of the shin. As a "
            "setup, the low kick works psychologically: after two kicks to "
            "the lead leg, the opponent's attention drops to his legs, and "
            "his guard follows - which is exactly when the hands and the "
            "high kick go to work."),
        "key_points": [
            "Strike the shin, calf, or ankle with the inner edge or instep of the shod foot.",
            "Short low arc with a snapping hip; the foot returns to the ground at once.",
            "Very fast and hard to see; attacks the leg's supporting structure, ruining footwork.",
            "The setup weapon: kick the lead leg until he guards low, then attack the exposed line.",
            "Traditional targets are calf, shin, ankle; the knee is avoided in practice for safety.",
            "A man who cannot stand cannot fight; the low kick stops the rush at its foundation.",
        ],
        "requirements": [
            "Condition the shins gradually on the bag; never full-force low kick an unpadded partner.",
            "Keep the hands up during the kick; the low kick's speed tempts fighters to drop the guard.",
            "Return the kicking foot to stance immediately; a lingering leg is a grabbed leg.",
            "Drill the kick from both leads; the rear-leg low kick carries more power, the lead-leg more speed.",
        ],
        "standards": [STD_SAVATE, STD_BARTITSU],
        "citations": [CIT_CHARLEMONT, CIT_BARTONWRIGHT_1899],
        "sig_lens": (
            "Signature original interpretation: his original Signature Combat "
            "Method treats the low kick as the signature striking through "
            "the page's margin - the foundation marked first, the structure "
            "above left to consider its footing. Clearly labeled "
            "Signature-made."),
    },
    {
        "key": "cane_thrust",
        "name": "The Cane Thrust",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The cane thrust is the Vigny method's fastest attack: the point "
            "of the cane driven straight into the opponent like a foil's "
            "point, and in Bartitsu it is the technique that punishes every "
            "overcommitment. From middle port the fighter extends the arm "
            "in a straight line, the thumb on top of the shaft guiding the "
            "point, and lunges - the rear leg driving, the front foot "
            "stepping deep - so the body's mass arrives behind the point. "
            "The traditional targets are the throat, the solar plexus, the "
            "face, and the weapon arm; the thrust is a piercing attack, "
            "meant to stop a man in his tracks rather than to trade blows. "
            "Vigny's teaching stresses three points: the point must travel "
            "the shortest line (any curve wastes the thrust's one advantage, "
            "speed), the body must lunge behind it (an arm-only thrust has "
            "no stopping power), and the recovery must be instant (a "
            "thrust left hanging is a cane offered to the opponent). The "
            "thrust pairs with the beat parry: beat the opponent's point "
            "aside, and in the same tempo drive your own point home. Drill "
            "the thrust against a padded target at lunging distance until "
            "the extension and the lunge land together; a thrust whose "
            "point arrives before the body's weight is only a poke."),
        "how_it_works": (
            "The thrust works by speed, penetration, and the lunge. The "
            "point travels the shortest line between the fighters, so it "
            "arrives before any cut, which must describe an arc; against a "
            "winding-up opponent, the thrust is already there while the cut "
            "is still being born. The lunge multiplies it: driving the "
            "body's mass forward behind the point turns the cane into a "
            "spear backed by the fighter's full weight, and the small area "
            "of the point concentrates that weight into piercing pressure. "
            "The thumb-on-top grip is the steering: it keeps the point on "
            "the true line the way a fencer's fingers keep a foil true, "
            "so the thrust does not waver in the last inches. The instant "
            "recovery works by the same muscles in reverse - the lunge "
            "recoils, the arm retracts along the true line, and the fighter "
            "is back in guard before the opponent can seize the extended "
            "cane."),
        "key_points": [
            "Extend the arm in a straight line, thumb on top guiding the point; lunge the body behind it.",
            "The point travels the shortest line; it arrives before any cut.",
            "Targets: throat, solar plexus, face, weapon arm - a piercing attack that stops a man.",
            "The lunge supplies the mass; an arm-only thrust has no stopping power.",
            "Recover instantly along the true line; a hanging thrust is a gift to the opponent.",
            "Pairs with the beat parry: beat his point aside, drive yours home in the same tempo.",
        ],
        "requirements": [
            "Drill only against padded targets or with a rubber-tipped practice cane; never thrust at a partner's face.",
            "Lunge on a firm surface; the deep front step needs grip, and a slip mid-lunge injures the groin.",
            "Keep the rear hand guarding during the thrust; the lunge tempts fighters to drop it.",
            "Practice the recovery as diligently as the thrust; the return is half the technique.",
        ],
        "standards": [STD_VIGNY, STD_BARTITSU],
        "citations": [CIT_VIGNY, CIT_BARTONWRIGHT_1901],
        "sig_lens": (
            "Signature original interpretation: his original Signature Combat "
            "Method treats the thrust as the signature's final dot - the "
            "pen driven straight to the point, no flourish, no curve, the "
            "whole body behind the smallest mark. Clearly labeled "
            "Signature-made."),
    },
]
ENTRIES += [
    {
        "key": "kotegaeshi",
        "name": "Kotegaeshi: The Standing Wrist Lock",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Kotegaeshi, the wrist turn-out, is Bartitsu's first standing "
            "joint lock, drawn from Yukio Tani's jujutsu. The defense "
            "begins when the attacker seizes the defender's wrist or lapel: "
            "the defender places both hands on the attacker's gripping "
            "hand, steps back and to the side to break the attacker's "
            "balance, and rotates the captured wrist outward and downward "
            "in a tight spiral - the hand turning against the wrist's "
            "natural range until the joint locks and the attacker must "
            "follow the spiral down or suffer the wrist. The lock controls "
            "rather than destroys: applied slowly it bends the attacker to "
            "his knees, applied with a sharp turn it throws him. Tani's "
            "teaching insists the power comes from the body, not the hands "
            "- the defender's whole weight drops and turns behind the "
            "spiral, so a small defender controls a large attacker. The "
            "classic faults are muscling the wrist with arm strength (which "
            "fails against a strong grip), forgetting the off-balancing "
            "step (which leaves the attacker solid enough to resist), and "
            "applying the lock fast in practice (which injures partners). "
            "Drill the spiral slowly with a cooperative partner who taps "
            "the moment pressure registers; speed comes only in advanced "
            "randori. Kotegaeshi is the gentleman's control: it ends the "
            "grab without striking a blow."),
        "how_it_works": (
            "Kotegaeshi works by taking a joint past its design. The wrist "
            "rotates freely in some directions and locks hard in others; "
            "the spiral drives it precisely into the locked direction, "
            "where the small bones and ligaments can transmit force but "
            "cannot move. Once the joint locks, the attacker's whole body "
            "becomes a lever attached to that locked point: any further "
            "rotation travels up the arm to the elbow and shoulder, and "
            "the body must follow - down to the knees or over in a throw "
            "- to relieve the pressure. The off-balancing step is the "
            "multiplier: an attacker whose weight is already committed "
            "cannot recruit his strength to resist the spiral, while the "
            "defender's dropping body weight supplies more force than any "
            "grip. That is why technique beats size here: the lock attacks "
            "a joint's geometry, and geometry does not care how strong the "
            "arm is."),
        "key_points": [
            "Both hands on the gripping hand; step back and aside to break his balance first.",
            "Rotate the captured wrist outward and downward in a tight spiral until the joint locks.",
            "Power comes from the dropping, turning body - never from arm-muscling the wrist.",
            "Applied slowly it kneels the attacker; applied sharply it throws him.",
            "The lock attacks the joint's geometry; size and strength of the arm do not matter.",
            "Drill slowly with a tapping partner; speed belongs only to advanced randori.",
        ],
        "requirements": [
            "The partner taps at the first pressure; the applier releases instantly - no exceptions.",
            "Never apply kotegaeshi at speed on a beginner; the wrist injures before the tap arrives.",
            "Drill the off-balancing step separately until it is reflexive; the spiral without it fails.",
            "Stop the session if any wrist is sore; joint locks accumulate damage silently.",
        ],
        "standards": [STD_KODOKAN, STD_BARTITSU],
        "citations": [CIT_KANO, CIT_BARTONWRIGHT_1899],
        "sig_lens": (
            "Signature original interpretation: his original Signature Combat "
            "Method treats kotegaeshi as the signature correcting another "
            "hand's grip - the spiral the pen turning the intruding fingers "
            "aside, the lock the page held firm. Clearly labeled "
            "Signature-made."),
    },
    {
        "key": "chasse",
        "name": "The Chasse: Savate Side Kick",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The chasse is savate's side kick and one of Bartitsu's most "
            "powerful leg weapons, striking with the sole (or heel) of the "
            "shoe. The mechanics: from guard the fighter turns the hip "
            "over, chambers the knee across the body, and drives the leg "
            "out sideways, the sole of the foot meeting the target in a "
            "straight driving line, then rechambers. Charlemont's system "
            "names three heights - chasse bas (low, to the leg), chasse "
            "median (to the midsection), chasse haute (to the head) - and "
            "teaches that the kick is a push of the whole body: the "
            "supporting leg drives, the hips commit, and the fighter's "
            "weight travels through the sole into the target. The side kick "
            "reaches further than any other kick and hits harder than any "
            "punch, which is why Barton-Wright prized it for stopping a "
            "rush: a chasse median to the midsection halts a charging man "
            "as surely as a door slammed in his face. The faults are "
            "telegraphing (dropping the hands or winding the hip), leaning "
            "back (which bleeds the power and invites the sweep), and "
            "failing to rechamber (which leaves the leg hanging to be "
            "caught). Drill on the heavy bag for the drive, on pads for "
            "the three heights, and always with the guard hands up."),
        "how_it_works": (
            "The chasse works by alignment and mass. Turning the hip over "
            "aligns the leg, hip, and torso into a single driving column - "
            "the body's weight travels in a straight line through the sole, "
            "the way a battering ram's weight travels through its head. "
            "The sole is the ideal striking surface for this column: broad "
            "enough to transfer the push without the ankle collapsing, hard "
            "enough in a shod foot to concentrate it. The three heights "
            "exploit three vulnerabilities: the low chasse attacks the "
            "supporting leg, the median drives the breath from the body, "
            "the high reaches a target no hand can touch. Rechambering "
            "matters because the side kick commits the fighter's balance "
            "further than any other technique - the leg must return along "
            "its path or the fighter is left standing on one leg in front "
            "of an angry opponent."),
        "key_points": [
            "Turn the hip over, chamber the knee across, drive the sole out in a straight line.",
            "Three heights: bas (leg), median (midsection), haute (head) - the kick is a push of the whole body.",
            "The side kick reaches further and hits harder than any punch; it stops a rush cold.",
            "Supporting leg drives, hips commit, weight travels through the sole like a battering ram.",
            "Never telegraph, never lean back, always rechamber along the same path.",
            "Drill the drive on the bag, the heights on pads, always with guard hands up.",
        ],
        "requirements": [
            "Build hip flexibility before attempting chasse haute; forcing height tears the groin.",
            "Hold the supporting foot flat and slightly turned; a raised heel under the drive strains the ankle.",
            "Practice rechambering as part of every rep; the return is drilled, not assumed.",
            "Spar the chasse at controlled force only; a full median kick breaks ribs through pads.",
        ],
        "standards": [STD_SAVATE, STD_BARTITSU],
        "citations": [CIT_CHARLEMONT, CIT_BARTONWRIGHT_1899],
        "sig_lens": (
            "Signature original interpretation: his original Signature Combat "
            "Method treats the chasse as the signature's broad side stroke - "
            "the hip the hand turning the page sideways, the sole the "
            "full breadth of the pen laid down at once. Clearly labeled "
            "Signature-made."),
    },
    {
        "key": "uppercut",
        "name": "The Uppercut and Body Blow",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The uppercut and the body blow are pugilism's rising punches, "
            "and in Bartitsu they punish the opponent who ducks or crowds. "
            "The uppercut: from guard the fighter dips the knees, drops the "
            "rear shoulder slightly, and drives the rear fist upward in a "
            "tight arc, the palm facing inward, rotating the hip and "
            "shoulder into the blow so it lands rising into the chin or "
            "solar plexus. The body blow: the same dip and drive directed "
            "into the ribs or midsection, thrown with a bent arm and a "
            "turned hip, meant to fold the opponent and drop his guard. "
            "The Victorian teaching is explicit about the legs: the "
            "uppercut is thrown from the knees up, the power rising from "
            "the floor through the straightening legs, and a fighter who "
            "throws it standing tall is throwing only his arm. The "
            "uppercut is the classic answer to the ducking head and the "
            "clinching wrestler; the body blow is the classic answer to "
            "the high guard - take the body and the head will follow. "
            "Drill the dip-and-drive on the bag until the legs fire before "
            "the arm, then on pads for the chin line. Both punches demand "
            "the guard's discipline: the non-punching hand stays glued to "
            "the chin, because the dip that loads these blows also opens "
            "the fighter to the counter."),
        "how_it_works": (
            "These blows work by the rising line and the leg drive. Most "
            "guards are built to stop horizontal and descending attacks; "
            "the uppercut's rising arc travels under the guard's coverage, "
            "arriving at the chin from a line the defense is not watching. "
            "The leg drive is the engine: straightening the bent knees "
            "against the floor launches the body's mass upward, and the "
            "rotating hip and shoulder channel that rising mass into the "
            "fist - the punch carries the fighter's weight moving up, "
            "which is why a proper uppercut lifts a man off his feet. The "
            "body blow works by a different physiology: a sharp blow to "
            "the solar plexus or floating ribs disrupts the diaphragm and "
            "folds the torso, and a folded torso cannot punch back. The "
            "combination is the art: body blow to fold him, uppercut to "
            "meet the falling chin - the one-two the Victorians called "
            "taking the body to find the head."),
        "key_points": [
            "Dip the knees, drop the rear shoulder, drive the rear fist up in a tight arc, palm inward.",
            "Power rises from the floor: legs straighten, hip and shoulder rotate, fist last.",
            "Uppercut answers the ducking head and the clinch; body blow answers the high guard.",
            "Body blow to the solar plexus or ribs folds the torso; a folded torso cannot punch.",
            "Classic combination: body blow to fold him, uppercut to meet the falling chin.",
            "The non-punching hand stays glued to the chin; the dip that loads the blow also opens you.",
        ],
        "requirements": [
            "Drill the dip-and-drive slowly until the legs fire before the arm on every rep.",
            "Keep the arc tight; a wide looping uppercut is slow and invites the counter hook.",
            "Wear body protection for partner body-blow drills; the solar plexus needs no full-force lesson.",
            "Never throw the uppercut while backing straight up; it needs the legs set under it.",
        ],
        "standards": [STD_QUEENSBERRY, STD_BARTITSU],
        "citations": [CIT_QUEENSBERRY, CIT_BARTONWRIGHT_1899],
        "sig_lens": (
            "Signature original interpretation: his original Signature Combat "
            "Method treats the uppercut as the signature rising from the "
            "page's lower margin - the knees the hand's gathering, the "
            "rising fist the stroke that meets what ducked below the line. "
            "Clearly labeled Signature-made."),
    },
    {
        "key": "cane_disarm",
        "name": "The Cane Hook Disarm",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The cane hook disarm is Bartitsu's answer to the armed "
            "ruffian: using the cane's own head or crook to strip a weapon "
            "from an attacker's hand. The mechanics depend on the cane: "
            "with a crook-handled stick, the defender hooks the crook "
            "around the attacker's wrist or weapon, then twists sharply "
            "while pulling - the crook becomes a wrench on the wrist, and "
            "the weapon levers out of the loosening grip. With a "
            "straight cane, the defender beats the weapon arm with a sharp "
            "cut to the wrist or forearm (the traditional 'cut to the "
            "hand'), numbing the grip so the weapon drops, then hooks the "
            "falling weapon or the wrist with the shaft. Vigny's teaching "
            "adds the bind: after the hook catches, the defender steps in "
            "and presses the cane across the attacker's arm, pinning it "
            "while the free hand strips the weapon. Timing is everything - "
            "the disarm is attempted in the half-tempo, as the attacker "
            "commits to his own strike and his grip is tightest on the "
            "weapon but his attention is on the attack. Drill with a "
            "padded practice weapon and a cooperative partner, at slow "
            "speed, until the hook-twist-pull is one motion. The disarm is "
            "never the first resort: Barton-Wright taught distance and "
            "escape before engagement, and the hook is for the moment when "
            "the weapon is already in play."),
        "how_it_works": (
            "The disarm works by leverage against the grip's weak axis. A "
            "hand grips a weapon strongest against a straight pull along "
            "the weapon's axis and weakest against a twisting wrench - the "
            "crook's hook converts the defender's pull into exactly that "
            "twist, multiplying a small motion at the cane's head into a "
            "large torque at the wrist. The cut to the hand works by "
            "physiology rather than leverage: a sharp blow to the wrist's "
            "tendons triggers an involuntary loosening of the fingers, and "
            "the weapon falls from a hand that no longer obeys. The bind "
            "finishes the physics: pressing the shaft across the arm pins "
            "the limb against the attacker's own body, removing the slack "
            "the grip needs to recover. Attempted in the half-tempo, the "
            "disarm exploits commitment - the attacker's weight and "
            "attention are moving forward into his strike, so he cannot "
            "withdraw the weapon from the hook without abandoning the "
            "attack he has already launched."),
        "key_points": [
            "Hook the crook around wrist or weapon, twist sharply while pulling; the crook is a wrench.",
            "With a straight cane, cut the weapon hand to numb the grip, then hook the wrist.",
            "After the hook catches, step in and bind the cane across his arm while stripping the weapon.",
            "Attempt in the half-tempo, as he commits to his strike and cannot withdraw.",
            "The twist attacks the grip's weak axis; a straight pull along the weapon fails.",
            "Distance and escape come before the disarm; the hook is for when the weapon is already in play.",
        ],
        "requirements": [
            "Drill only with padded practice weapons and a cooperative partner at slow speed.",
            "The partner announces the attack line; unannounced full-speed disarms belong to no drill.",
            "Protect the eyes and hands; hooks slip and practice weapons still bruise.",
            "Never attempt the disarm as a first option in sparring; it is a committed technique with a real cost if missed.",
        ],
        "standards": [STD_VIGNY, STD_BARTITSU],
        "citations": [CIT_VIGNY, CIT_BARTONWRIGHT_1901, CIT_LANG],
        "sig_lens": (
            "Signature original interpretation: his original Signature Combat "
            "Method treats the disarm as the signature reclaiming the pen - "
            "the crook the hand's hook around another's grip, the twist the "
            "firm turning that takes back what was seized. Clearly labeled "
            "Signature-made."),
    },
    {
        "key": "cane_hip_throw",
        "name": "The Hip Throw with Cane Assist",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The hip throw with cane assist is pure Bartitsu synthesis: "
            "o goshi's hip fulcrum combined with the cane as an additional "
            "lever, the two arts working as one technique. The thrower "
            "steps in as for o goshi, turning the back and seating the hip, "
            "but the cane - held in both hands or pressed by the throwing "
            "arm - lies across the opponent's chest, lapel, or upper arm. "
            "As the hips turn and the legs drive, the cane adds a second "
            "lever: it pries the opponent's upper body over the hip "
            "fulcrum while the throwing arm pulls, doubling the rotating "
            "force and controlling an opponent who might otherwise slip "
            "the grip. Barton-Wright's innovation was practical: on the "
            "street there are no jackets built for gripping, so the cane "
            "supplies the handle the clothing does not. The technique "
            "demands the full ladder beneath it - the stance to enter, the "
            "ukemi to practice safely, the o goshi mechanics to place the "
            "hip, and the cane grip to wield the lever. Drill the entry "
            "with the cane placement first, then the throw onto mats with "
            "a partner in ukemi, building speed only when the fulcrum "
            "lands true. The cane-assisted throw is the thesis of the art "
            "in a single motion: no art alone, all arts together."),
        "how_it_works": (
            "The technique works by stacking two levers on one fulcrum. "
            "The hip remains the primary fulcrum under the opponent's "
            "center of mass, exactly as in o goshi; the cane becomes a "
            "rigid extension of the throwing arm, lengthening the lever "
            "that pulls the opponent's upper body over. A longer lever "
            "needs less force for the same rotation, so the cane assist "
            "lets a smaller thrower move a larger opponent and gives "
            "control against a resisting one - the cane across the chest "
            "distributes the pull and prevents the opponent from ducking "
            "under the throwing arm. The street logic is the deeper "
            "mechanism: where the dojo offers a sturdy jacket to grip, the "
            "street offers only coats and collars, so the cane replaces "
            "the missing handle with a better one - rigid, long, and "
            "already in the defender's hand."),
        "key_points": [
            "Enter as for o goshi, but lay the cane across his chest, lapel, or upper arm as a second lever.",
            "The hip is the fulcrum; the cane lengthens the throwing arm's lever for the same rotation.",
            "The cane supplies the handle that street clothing does not; it replaces the missing jacket grip.",
            "Turn the hips, drive the legs, pull with the arm and pry with the cane in one motion.",
            "Demands the full ladder: stance, ukemi, o goshi mechanics, and cane grip beneath it.",
            "The thesis of the art in one motion: no art alone, all arts together.",
        ],
        "requirements": [
            "Master o goshi and the cane grip separately before combining them; the synthesis punishes weak parts.",
            "Drill cane placement in the entry for weeks before the full throw; the lever must land true.",
            "Throw onto mats only, with a partner whose ukemi is reflexive; the added lever adds landing force.",
            "Use a stout practice cane; a light stick flexes and a cracked one fails under the prying load.",
        ],
        "standards": [STD_BARTITSU, STD_KODOKAN, STD_VIGNY],
        "citations": [CIT_BARTONWRIGHT_1899, CIT_KANO, CIT_VIGNY],
        "sig_lens": (
            "Signature original interpretation: his original Signature Combat "
            "Method treats the cane-assisted throw as two signatures on one "
            "page - the hip the crease, the cane the second hand turning "
            "the sheet, both arts signing the same motion. Clearly labeled "
            "Signature-made."),
    },
    {
        "key": "combinations",
        "name": "Combination Striking: Punch-Kick Flow",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Combination striking is where Bartitsu's separate weapons "
            "become a system: punches, kicks, and cane cuts chained so "
            "each opens the target for the next. The foundational "
            "combination is the one-two-low-kick: straight blow to lift the "
            "guard, hook or cross to turn the head, low kick to the lead "
            "leg as the weight settles. The cane combination is cut-thrust-"
            "cut: overhead cut to provoke the high parry, thrust through "
            "the opening the parry leaves, recovering cut as the guard "
            "resets. The mixed combination is the art's crown: jab to "
            "measure, low kick to deaden the leg, cane cut to the weapon "
            "arm as he reaches. The teaching method is additive: drill "
            "each technique alone, then in pairs (jab-cross, cut-thrust), "
            "then in threes, then in fours, never adding a link until the "
            "chain before it flows without thought. Every combination "
            "obeys the same rules: the guard returns between links (no "
            "combination is worth an open chin), the feet deliver each "
            "weapon (punches without footwork are arm punches), and the "
            "last technique recovers to guard (the combination ends safe, "
            "not spent). Sparring is where combinations are tested: the "
            "bag teaches the chain, the partner teaches the timing."),
        "how_it_works": (
            "Combinations work by overloading the defense. A single attack "
            "can be parried, blocked, or evaded; a second attack arriving "
            "in the tempo the first one stole cannot be answered by a "
            "defense that is still busy with the first. Each link of the "
            "combination exploits the reaction to the previous one: the "
            "straight blow lifts the guard, which exposes the body to the "
            "hook; the hook turns the head, which plants the weight for "
            "the low kick; the low kick deadens the leg, which roots the "
            "opponent for the cane cut. The additive drilling method works "
            "by chunking: the nervous system learns the pair as one "
            "motion, then the triple as one motion, until a four-link "
            "combination fires as a single decision. That is why the guard "
            "must return between links - a combination is not flailing, it "
            "is a sequence of complete techniques, each launched from "
            "safety and recovered to safety."),
        "key_points": [
            "Chain weapons so each opens the target for the next: straight lifts the guard, hook turns the head, low kick roots the leg.",
            "Foundational chains: one-two-low-kick; cut-thrust-cut; jab, low kick, cane cut to the weapon arm.",
            "Build additively: singles, then pairs, then threes, then fours - never add a link until the chain flows.",
            "The guard returns between links; the feet deliver each weapon; the last technique recovers to guard.",
            "Each link exploits the reaction to the previous one; the defense, still busy, cannot answer the next.",
            "The bag teaches the chain; the partner teaches the timing.",
        ],
        "requirements": [
            "Do not drill combinations until each single technique is clean; chains magnify faults.",
            "Count the links aloud while drilling to keep the sequence honest; dropped links mean the chain is too long.",
            "Spar combinations at controlled force; the third and fourth links land where the guard has gone.",
            "Film the combinations monthly; the eye catches dropped guards the body cannot feel.",
        ],
        "standards": [STD_BARTITSU, STD_QUEENSBERRY, STD_SAVATE, STD_VIGNY],
        "citations": [CIT_BARTONWRIGHT_1899, CIT_CHARLEMONT, CIT_VIGNY],
        "sig_lens": (
            "Signature original interpretation: his original Signature Combat "
            "Method treats the combination as the signature's full name - "
            "each stroke opening the space for the next, the whole written "
            "without lifting the pen, the final guard the hand at rest. "
            "Clearly labeled Signature-made."),
    },
    {
        "key": "seoi_nage",
        "name": "Seoi Nage: The Shoulder Throw",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Seoi nage, the shoulder throw, is the second great throw of "
            "Bartitsu's jujutsu ladder and the natural partner of o goshi. "
            "The thrower grips the opponent's arm (at the sleeve or wrist) "
            "and lapel, steps in deep while turning the back, drops the "
            "hips below the opponent's, and loads the opponent's arm across "
            "the shoulders - then straightens the legs, pulls the arm down "
            "and across, and rotates, carrying the opponent over the "
            "shoulder and onto his back. Where o goshi uses the hip as the "
            "fulcrum, seoi nage uses the shoulder and upper back, which "
            "makes it the throw for a taller opponent or a bent-over "
            "attacker: the load rides higher and the arc is longer. The "
            "drop version (seoi otoshi) sinks to one knee for extra "
            "leverage, a favorite of smaller fighters. Tani's lineage "
            "teaches the same prerequisites as o goshi: kuzushi first (pull "
            "the opponent forward onto his toes), the deep entry second, "
            "the load third, the rotation last - and the classic fault is "
            "the same, attempting the throw on a balanced opponent. Drill "
            "the entry and load without the throw until the partner's "
            "weight settles onto your back like a sack; only then add the "
            "rotation, onto mats, with full ukemi on both sides."),
        "how_it_works": (
            "Seoi nage works as a wheel and a lever. The thrower's "
            "shoulder becomes the axle; the opponent's body, draped over "
            "it, becomes the load on a wheel that the thrower's rotation "
            "turns. Dropping the hips below the opponent's center of mass "
            "is the key geometry: once the axle sits under the load's "
            "balance point, the opponent's own weight starts the rotation "
            "and the thrower only guides it. The arm grip is the steering: "
            "pulling the gripped arm down and across rotates the opponent's "
            "torso onto the wheel, while the leg drive lifts the axle. "
            "Against a taller opponent the throw is actually easier, "
            "because his higher center of mass sits further above the "
            "axle and his weight does more of the work - which is why the "
            "shoulder throw is the small fighter's answer to the big "
            "man's clinch. The drop version deepens the geometry further, "
            "putting the axle lower still for maximum mechanical "
            "advantage."),
        "key_points": [
            "Grip arm and lapel; step deep, turn the back, drop the hips below his; load his arm across your shoulders.",
            "Straighten the legs, pull the arm down and across, rotate - he rides the wheel over.",
            "The shoulder is the axle; dropping it under his center of mass lets his own weight start the throw.",
            "The throw for the taller opponent or the bent-over attacker; the load rides high and the arc is long.",
            "Drop version (seoi otoshi) sinks to one knee: the small fighter's maximum leverage.",
            "Kuzushi first, entry second, load third, rotation last; never throw a balanced opponent.",
        ],
        "requirements": [
            "Ukemi must be reflexive in both partners before the first live seoi nage.",
            "Drill the entry and load without the throw until the partner's weight settles correctly.",
            "Mats or soft ground only; the shoulder throw lands the opponent from height.",
            "The person thrown sets the pace; surprise full throws are forbidden in practice.",
        ],
        "standards": [STD_KODOKAN, STD_BARTITSU],
        "citations": [CIT_KANO, CIT_BARTONWRIGHT_1899],
        "sig_lens": (
            "Signature original interpretation: his original Signature Combat "
            "Method treats seoi nage as the signature lifting the whole page "
            "- the shoulder the hand's shelf, the rotation the turn that "
            "carries the sheet over, the landing the page laid flat. "
            "Clearly labeled Signature-made."),
    },
    {
        "key": "balayage",
        "name": "Balayage: The Savate Foot Sweep",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Balayage, the sweeping kick, is savate's subtlest weapon in "
            "Bartitsu: not a strike but a reap, sweeping the opponent's "
            "supporting foot from under him. The mechanics are delicate: "
            "as the opponent steps or shifts weight, the fighter sweeps "
            "the sole of the shoe in a low arc against the opponent's "
            "ankle or instep, contacting just as the weight arrives on the "
            "foot - the sweep does not need force, because the opponent's "
            "own stepping momentum does the work. Charlemont's teaching "
            "makes timing the whole technique: sweep too early and the foot "
            "is unweighted (the sweep passes harmlessly); sweep too late "
            "and the weight is planted (the sweep bounces off); sweep at "
            "the instant of weight transfer and the foot skims away like a "
            "rug pulled. The fighter's own balance is the price: the "
            "sweeping leg leaves the ground, so the supporting leg must be "
            "solid and the hands must guard, because a failed sweep is an "
            "invitation. Balayage pairs with the low kick - kick the leg "
            "until he steps to protect it, sweep the stepping foot - and "
            "with the cane, which can reap at longer range. Drill with a "
            "partner stepping on command, then in free footwork, at "
            "controlled speed; the sweep that dumps a partner unexpectedly "
            "ends the partnership."),
        "how_it_works": (
            "Balayage works by removing the floor at the critical instant. "
            "Human balance during a step is a controlled fall: for a "
            "fraction of a second the body's weight is committed to a foot "
            "that has just landed and not yet stabilized. The sweep "
            "arrives in exactly that fraction, sliding the foot sideways "
            "while the body's momentum continues forward - the base goes "
            "one way, the mass goes the other, and gravity finishes the "
            "technique. No strength is needed because the opponent "
            "supplies the energy; the sweeper only redirects the "
            "foundation. This is also why the timing window is so narrow: "
            "before weight transfer there is nothing to sweep, after it "
            "the structure is set. The pairing with the low kick works "
            "psychologically and mechanically - the kick forces the "
            "protective step, and the step is what gets swept."),
        "key_points": [
            "Sweep the sole against his ankle or instep at the instant his weight transfers onto the stepping foot.",
            "The opponent's own stepping momentum does the work; the sweep needs timing, not force.",
            "Too early: the foot is unweighted and the sweep passes. Too late: the weight is planted and it bounces.",
            "The sweeping leg leaves the ground, so the supporting leg must be solid and the hands must guard.",
            "Pairs with the low kick: kick until he steps to protect, sweep the stepping foot.",
            "Drill on command steps first, then free footwork; never dump a partner unexpectedly.",
        ],
        "requirements": [
            "Both partners wear ankle-supporting shoes; the sweep stresses the ankle it catches.",
            "Drill at controlled speed with agreed stepping patterns before any free application.",
            "The swept partner must have ukemi; even a gentle sweep can land a beginner badly.",
            "Keep the sweep low - ankle height; a high sweep is a kick and breaks the drill's contract.",
        ],
        "standards": [STD_SAVATE, STD_BARTITSU],
        "citations": [CIT_CHARLEMONT, CIT_BARTONWRIGHT_1899],
        "sig_lens": (
            "Signature original interpretation: his original Signature Combat "
            "Method treats balayage as the signature's erasure of a false "
            "stroke - the sole the hand's edge smoothing away what was "
            "written wrong, timed to the instant the ink was wet. Clearly "
            "labeled Signature-made."),
    },
]
ENTRIES += [
    {
        "key": "juji_gatame",
        "name": "Juji Gatame: The Straight Armlock",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Juji gatame, the cross-body straight armlock, is Bartitsu's "
            "principal ground control, inherited from Tani's jujutsu and "
            "codified at the Kodokan. The classic application: from a "
            "controlling position the defender traps the opponent's arm "
            "between his legs, the opponent's elbow resting against the "
            "defender's hip, the defender's hands gripping the opponent's "
            "wrist. Then the defender sits back, raises the hips, and "
            "arches - the hip becomes the fulcrum, the opponent's arm the "
            "lever, and the elbow joint is extended toward and past its "
            "limit. The control is absolute and the mercy is built in: the "
            "defender feels the resistance through the hips before damage "
            "occurs, and in practice the partner taps the moment pressure "
            "registers. Tani's teaching stresses position before "
            "submission: the legs must pin the arm and the body must be "
            "close, because the armlock applied at arm's length is weak "
            "and escapable. The Victorian self-defense application was "
            "the pin after the throw: o goshi or seoi nage puts the "
            "attacker down, and juji gatame keeps him there until help "
            "arrives or he surrenders. Drill the entry and the leg "
            "positioning slowly with a tapping partner; the finish - the "
            "hip raise - is practiced as a controlled inch, never a jerk."),
        "how_it_works": (
            "Juji gatame works as a lever on the elbow's hinge. The elbow "
            "extends in one plane and locks at the end of it; the armlock "
            "places the hip fulcrum directly under the joint and applies "
            "force to the wrist at the far end of the forearm lever, so a "
            "small hip movement generates a large extending torque at the "
            "elbow. The legs are the clamp: pinning the arm between the "
            "thighs removes the shoulder's ability to rotate away, "
            "isolating the elbow as the only joint that can give - and it "
            "cannot give without damage, so the opponent must tap. The "
            "defender's sensitivity is the safety mechanism: because the "
            "hips feel the arm's resistance directly, the applier knows "
            "exactly how much pressure is on the joint and can stop at "
            "control rather than injury. That is why the technique is a "
            "control first and a submission second: the same mechanics "
            "that could break the arm are what make the pin inescapable "
            "without breaking anything."),
        "key_points": [
            "Trap his arm between your legs, his elbow on your hip, both hands gripping his wrist.",
            "Sit back, raise the hips, arch: the hip is the fulcrum, his arm the lever.",
            "The legs clamp the arm so the shoulder cannot rotate away; the elbow is isolated.",
            "Position before submission: legs pinning, body close - the armlock at arm's length is weak.",
            "The hips feel the resistance directly; stop at control, never jerk to injury.",
            "Victorian application: the throw puts him down, juji gatame keeps him there.",
        ],
        "requirements": [
            "The partner taps at first pressure and the applier releases at once; the tap is sacred.",
            "Drill the entry and leg positioning for weeks before practicing the hip-raise finish.",
            "Never jerk the finish; the armlock is applied as a controlled inch, felt through the hips.",
            "Both partners must know ukemi and basic ground safety; the throw that precedes the lock is the risk.",
        ],
        "standards": [STD_KODOKAN, STD_BARTITSU],
        "citations": [CIT_KANO, CIT_BARTONWRIGHT_1899],
        "sig_lens": (
            "Signature original interpretation: his original Signature Combat "
            "Method treats juji gatame as the signature pressed flat and "
            "held - the legs the paperweights, the hip the seal, the arm "
            "the line that cannot move until the hand releases it. Clearly "
            "labeled Signature-made."),
    },
    {
        "key": "knife_defense",
        "name": "Defending Against a Knife Attack",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Knife defense in Bartitsu follows Barton-Wright's own "
            "doctrine: the best defense against a knife is distance, and "
            "the second best is the cane. The principles are taught as a "
            "hierarchy. First, escape: if there is room to run, run - no "
            "technique outranks leaving. Second, the barrier: keep the "
            "cane between you and the blade, using cuts to the weapon hand "
            "and thrusts to the body to hold the attacker at long measure "
            "where the knife cannot reach. Third, if the distance "
            "collapses: control the knife arm, never the knife - both "
            "hands seize the wrist and forearm, the body moves offline at "
            "an angle so the thrust passes by, and the arm is pinned, "
            "locked (kotegaeshi or the straight armlock), or thrown over "
            "(o goshi). The prohibitions are absolute: never grab at the "
            "blade, never trade cuts, never turn your back, and never "
            "assume one control is enough - the knife hand is fought "
            "until it is empty and pinned. The Victorians drilled this "
            "with a chalk-marked wooden knife so every touch left its "
            "evidence; the modern student uses a training blade and the "
            "same honesty. Barton-Wright was blunt about the odds: against "
            "a committed knife attacker, the defender expects to be cut "
            "and fights to keep the cuts away from the vitals while "
            "securing the arm."),
        "how_it_works": (
            "Knife defense works by geometry and grim arithmetic. A knife "
            "is lethal only within its reach; the cane's reach is more "
            "than twice the knife's, so the barrier principle is pure "
            "measure - at long measure the knife mathematically cannot "
            "arrive, and the cane can. When the measure collapses, the "
            "defense switches to the arm: the wrist and forearm are the "
            "only safe handles on a knife attack, because controlling "
            "them controls the blade's line. Moving offline works by "
            "angles: a thrust travels a straight line, and a body that has "
            "stepped forty-five degrees off that line is simply not where "
            "the point arrives. The two-handed arm control works by "
            "numbers: two hands and the body's weight against one wrist "
            "is a contest the wrist loses, which is why the technique "
            "demands both hands commit to the arm while the feet keep "
            "moving. The chalk-knife drill works psychologically: seeing "
            "the marks teaches faster than any lecture that the blade "
            "touches what the eyes miss."),
        "key_points": [
            "Hierarchy: escape first, the cane as barrier second, arm control third - never skip a level.",
            "At long measure the knife cannot reach and the cane can; hold that measure with cuts and thrusts.",
            "If the distance collapses: control the knife ARM with both hands, never grab the blade.",
            "Move offline at an angle so the thrust's straight line misses; pin, lock, or throw the arm.",
            "Never trade cuts, never turn your back, never assume one control is enough.",
            "Drill with a marking training blade; expect to be marked and learn from every mark.",
        ],
        "requirements": [
            "Drill only with training blades; a live blade has no place in any drill.",
            "Wear eye protection and forearm guards; training blades still strike hard.",
            "The attacker starts slow and announced; speed rises only when the offline step is reflexive.",
            "Debrief every drill: count the marks, name the fault, drill the correction.",
        ],
        "standards": [STD_BARTITSU, STD_VIGNY, STD_KODOKAN],
        "citations": [CIT_BARTONWRIGHT_1901, CIT_VIGNY, CIT_WOLF],
        "sig_lens": (
            "Signature original interpretation: his original Signature Combat "
            "Method treats knife defense as the signature defending the "
            "page - the cane the margin no blade may cross, the offline "
            "step the hand moving the paper, the arm control the firm hold "
            "that takes back the pen. Clearly labeled Signature-made."),
    },
    {
        "key": "flying_mare",
        "name": "The Flying Mare Throw",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The flying mare is the spectacular overhead throw of the "
            "Victorian wrestling and jujutsu repertoire, taught in "
            "Barton-Wright's articles as the answer to the headlock and "
            "the collar grab. The attacker seizes the defender's neck or "
            "collar and pulls; the defender steps in close, grips the "
            "attacker's arm at the elbow with both hands, drops the hips "
            "low, and - using the attacker's own pulling force - bends "
            "sharply forward, carrying the attacker up and over the "
            "shoulder in a great wheel to slam onto his back in front. "
            "The technique is a masterpiece of borrowed force: the harder "
            "the attacker pulls, the higher he flies, because his pull is "
            "what loads the wheel. The defender's jobs are only three: "
            "get the hips under the attacker's center, keep a death grip "
            "on the captured arm, and bend forward decisively - hesitation "
            "leaves the defender bent double under a live opponent. The "
            "throw demands the complete foundation: the stance to absorb "
            "the pull, the ukemi of both partners (the flight is long and "
            "the landing hard), and the hip-throw mechanics of o goshi "
            "and seoi nage beneath it. Drill the entry and the bend "
            "without the throw until the partner's weight comes onto the "
            "back correctly; the full throw is practiced onto thick mats, "
            "rarely, and never as a surprise."),
        "how_it_works": (
            "The flying mare works by turning the attacker's aggression "
            "into the throw's engine. When the attacker pulls the "
            "defender's neck forward, he commits his weight and momentum "
            "in that direction; the defender, instead of resisting, drops "
            "under and adds a sharp forward bend, so the attacker's own "
            "pull becomes the force that carries him over the shoulder. "
            "The shoulder and upper back form the wheel's rim, the "
            "defender's hips the axle set low under the attacker's "
            "center of mass, and the two-handed grip on the arm is the "
            "spoke that keeps the load attached to the wheel through the "
            "full rotation. Because the energy comes from the attacker, "
            "the defender needs only to shape it - which is why a small "
            "defender can throw a large attacker who pulls hard, and why "
            "the throw fails completely against an attacker who does not "
            "commit. The long flight is the price: the opponent travels "
            "further and lands harder than in any hip throw, so the mats "
            "and the ukemi are not optional."),
        "key_points": [
            "He pulls your neck; you step in, grip his arm with both hands, drop the hips low.",
            "Bend sharply forward, carrying him up and over the shoulder in a great wheel.",
            "His pull is the engine: the harder he pulls, the higher he flies - borrowed force.",
            "Hips under his center, death grip on the arm, decisive bend; hesitation is fatal to the technique.",
            "Demands the full foundation: stance, ukemi, and hip-throw mechanics beneath it.",
            "Drill entry and bend without the throw; full throws onto thick mats, rarely, never as surprises.",
        ],
        "requirements": [
            "Both partners need advanced ukemi; the flight is long and the landing is hard.",
            "Thick crash mats only; thin mats do not absorb the flying mare's landing.",
            "The person thrown controls whether the full throw happens; no surprise full throws ever.",
            "Build neck strength before practicing; the technique begins with a pull on the neck.",
        ],
        "standards": [STD_BARTITSU, STD_KODOKAN],
        "citations": [CIT_BARTONWRIGHT_1899, CIT_KANO],
        "sig_lens": (
            "Signature original interpretation: his original Signature Combat "
            "Method treats the flying mare as the signature turning the "
            "page clear over - the attacker's own pull the hand's momentum, "
            "the wheel the flourish that carries the sheet in a full arc "
            "to land face-up. Clearly labeled Signature-made."),
    },
    {
        "key": "counters",
        "name": "Counter-Punching and the Riposte",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Counter-punching and the riposte are the advanced art of "
            "hitting the hitter: every attack the opponent launches is "
            "treated as an opening, and Bartitsu trains the student to "
            "answer in the same breath. The boxing counter: as the "
            "opponent's straight blow comes, the defender slips the head "
            "just off the line (a few inches, never a lean) and drives "
            "his own straight or hook into the opening the extended arm "
            "leaves - the counter lands while the opponent's punch is "
            "still out, when he cannot guard. The cane riposte: the parry "
            "meets the cut on the forte, and without pausing the defender "
            "answers - cut to the head after the high parry, thrust after "
            "the beat, low cut after the hanging guard. The savate "
            "counter: the low kick is checked or evaded with a small lift "
            "of the leg, and the supporting leg - now bearing his full "
            "weight - is swept or kicked in the same tempo. Three "
            "principles govern all counters: the defense must be small "
            "(a big slip or wide parry wastes the tempo), the answer must "
            "be immediate (the opening lives for a fraction of a second), "
            "and the counter must be a real technique, not a pat - "
            "Barton-Wright's counter-punchers finished exchanges. Drill "
            "counters as call-and-response: partner attacks on call, you "
            "defend small and answer at once, until the pair fires as one "
            "motion."),
        "how_it_works": (
            "Counters work by stealing the attacker's tempo. Every attack "
            "has three phases - preparation, execution, recovery - and "
            "during execution and recovery the attacker cannot defend: "
            "his weapons are committed, his weight is moving, his guard "
            "is open. The counter is timed to land in exactly those "
            "phases, so the defender's attack meets no defense at all. "
            "The small defense is the key economy: slipping the head "
            "inches instead of leaning a foot keeps the defender's own "
            "weapons in range and his balance intact, so the answer "
            "launches from a loaded position rather than a recovery. The "
            "cane riposte adds geometry: the parry that catches the cut "
            "on the forte has already chambered the answering cut, so "
            "defense and counter are one continuous motion, not two "
            "decisions. This is why counters beat combinations: the "
            "combination needs its links, but the counter needs only the "
            "opponent's commitment."),
        "key_points": [
            "Every attack is an opening: answer in the same breath, while his weapons are committed.",
            "Boxing counter: slip inches off the line and drive your straight into the opening his extended arm leaves.",
            "Cane riposte: parry on the forte and answer without pause - cut after high parry, thrust after the beat.",
            "Savate counter: check the low kick and sweep the now-weighted supporting leg in the same tempo.",
            "The defense must be small, the answer immediate, the counter a real technique.",
            "Drill as call-and-response until defense and answer fire as one motion.",
        ],
        "requirements": [
            "Master the basic defenses first; a counter built on a sloppy parry is a mutual hit.",
            "Drill counters at half speed with a cooperative partner before any live application.",
            "Wear headgear for counter-punching drills; counters land clean by design.",
            "Call the attack before each drill rep; unannounced counters belong to advanced sparring only.",
        ],
        "standards": [STD_BARTITSU, STD_QUEENSBERRY, STD_VIGNY, STD_SAVATE],
        "citations": [CIT_BARTONWRIGHT_1899, CIT_BARTONWRIGHT_1901, CIT_CHARLEMONT],
        "sig_lens": (
            "Signature original interpretation: his original Signature Combat "
            "Method treats the counter as the signature answering another "
            "hand mid-stroke - the small slip the pen lifting just clear, "
            "the riposte the firm line written across the intruding mark. "
            "Clearly labeled Signature-made."),
    },
    {
        "key": "multiple_opponents",
        "name": "Awareness Against Multiple Opponents",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Multiple-opponent awareness is Bartitsu's doctrine for the "
            "nightmare scenario: two or more attackers, and the "
            "Victorian teaching is brutally honest - the defender's goal "
            "is escape, not victory. The principles are a system. Never "
            "go to the ground: a throw that is beautiful against one man "
            "is suicide against two, because the second attacker arrives "
            "while you are down. Keep moving: circle so the attackers line "
            "up behind each other, using the nearest as a shield against "
            "the farther - the defender fights one man at a time by "
            "geometry, never by permission. Strike and move: the cane's "
            "long measure keeps both at bay, low kicks deaden the nearest "
            "legs, and every technique is thrown on the move, because "
            "standing still lets them surround. Watch the hands and the "
            "feet, not the faces: hands hold weapons, feet telegraph the "
            "rush. And always know the exits: the defender enters every "
            "room noting the doors, and the moment an exit opens, he "
            "takes it - Barton-Wright's gentlemen were taught that "
            "discretion here is not cowardice but arithmetic. Drill with "
            "two partners at walking speed, practicing the circling and "
            "the shield geometry; the drill's win condition is reaching "
            "the marked exit, not touching the attackers."),
        "how_it_works": (
            "The doctrine works by denying the attackers their only "
            "advantage: simultaneity. Two attackers win by arriving "
            "together; the circling defender arranges that they arrive in "
            "sequence, because a body cannot occupy the space another "
            "body already holds - the nearer attacker physically blocks "
            "the farther one's path. Constant movement serves the same "
            "arithmetic: a moving target forces each attacker to re-aim, "
            "and re-aiming takes the fraction of a second that keeps "
            "their attacks staggered. The cane's long measure multiplies "
            "the effect: at cane range the defender threatens both "
            "attackers at once, so neither can close without crossing the "
            "point. The exit discipline works psychologically: a defender "
            "who has already chosen his escape does not freeze deciding, "
            "and in a real assault the first seconds decide everything. "
            "The ground prohibition is pure physics: a standing man can "
            "move and strike in all directions, while a grounded man has "
            "surrendered mobility to opponents who still have theirs."),
        "key_points": [
            "The goal is escape, not victory; discretion here is arithmetic, not cowardice.",
            "Never go to the ground: the throw that is beautiful against one is suicide against two.",
            "Keep circling so the attackers line up; use the nearest as a shield against the farther.",
            "Strike on the move with the cane's long measure and low kicks; never stand still to trade.",
            "Watch hands and feet, not faces; hands hold weapons and feet telegraph the rush.",
            "Know the exits before trouble starts; the drill's win condition is reaching the marked exit.",
        ],
        "requirements": [
            "Drill at walking speed with cooperative partners; full-speed multiple-attacker drills injure people.",
            "Mark an exit in every drill space; the drill ends when the defender reaches it.",
            "Rotate all three roles so everyone learns the attackers' geometry too.",
            "Debrief each round: when did the circle break, and what opened the exit?",
        ],
        "standards": [STD_BARTITSU],
        "citations": [CIT_BARTONWRIGHT_1899, CIT_WOLF],
        "sig_lens": (
            "Signature original interpretation: his original Signature Combat "
            "Method treats the multiple-attacker doctrine as the signature "
            "protecting the whole page - the circle the hand's sweep keeping "
            "all marks at the margin, the exit the hand lifting the pen to "
            "safety. Clearly labeled Signature-made."),
    },
    {
        "key": "cane_trap",
        "name": "The Two-Handed Cane Trap",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "The two-handed cane trap is Bartitsu's close-range cane "
            "grappling: both hands on the shaft, using it as a bar to "
            "pin, lever, and control a clinching opponent. The core "
            "technique: as the attacker closes to grappling range, the "
            "defender brings both hands onto the cane - one at each end "
            "of the middle third - and presses the shaft horizontally "
            "across the attacker's arm, throat line (with control, never "
            "crushing), or body, stepping in to pin the trapped limb "
            "against the attacker's own torso. From the trap flow the "
            "finishes: lever the arm up into a standing lock, step through "
            "for the hip throw with the cane already placed (the "
            "cane-assisted throw's close cousin), or simply hold the pin "
            "while disengaging toward the exit. Vigny's method teaches the "
            "trap as the answer to the cane's one weakness - at clinch "
            "range there is no room to cut, so the cane becomes a grappling "
            "tool instead of a striking one. The two-handed grip is the "
            "whole secret: one hand guides, the other drives, and between "
            "them the shaft is a rigid bar no arm can bend. Drill the trap "
            "from a slow clinch entry with a cooperative partner, holding "
            "the pin for a three-count; the finishes are added one at a "
            "time, and pressure against the throat is practiced as "
            "placement only, never as force."),
        "how_it_works": (
            "The trap works by converting the cane from a lever of speed "
            "into a lever of control. Held in two hands, the shaft becomes "
            "a rigid bar, and a rigid bar pressed across a limb pins that "
            "limb against the body's own structure - the arm cannot move "
            "because the cane, the torso, and the defender's two hands "
            "form a closed frame around it. The two-handed grip doubles "
            "the control: each hand can push, pull, or rotate "
            "independently, so the defender steers the trapped limb in any "
            "direction while the attacker, gripping with one hand or none, "
            "has no comparable purchase. Pressing across the arm to set up "
            "the lock works by the same joint geometry as kotegaeshi: the "
            "bar levers the limb toward its locked direction, and the "
            "body must follow. The technique's real lesson is adaptability "
            "- the weapon that cannot cut at this range grapples instead, "
            "and the Bartitsu fighter is never disarmed by distance."),
        "key_points": [
            "Both hands on the shaft, one at each end of the middle third; press it across his arm or body.",
            "Pin the trapped limb against his own torso; the cane, torso, and your hands form a closed frame.",
            "At clinch range the cane cannot cut, so it becomes a grappling bar instead.",
            "From the trap: lever to a standing lock, step through to the hip throw, or hold and disengage.",
            "One hand guides, the other drives; between them no arm can bend the bar.",
            "Throat placement is practiced as placement only, never as crushing force.",
        ],
        "requirements": [
            "Drill from slow clinch entries with a cooperative partner; speed comes last.",
            "Hold the pin for a three-count in drills; the control must be stable, not snatched.",
            "Never apply force to the throat in practice; the placement is the lesson, not the pressure.",
            "Learn the finishes one at a time; the trap itself must be reflexive before the lock is added.",
        ],
        "standards": [STD_VIGNY, STD_BARTITSU],
        "citations": [CIT_VIGNY, CIT_BARTONWRIGHT_1901],
        "sig_lens": (
            "Signature original interpretation: his original Signature Combat "
            "Method treats the two-handed trap as the signature held by "
            "both hands of the oath - the bar the unbroken line, the frame "
            "the covenant closed around what would break it. Clearly "
            "labeled Signature-made."),
    },
    {
        "key": "hadaka_jime",
        "name": "Hadaka Jime: The Rear Choke and Its Defense",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Hadaka jime, the rear naked choke, is the jujutsu technique "
            "Bartitsu teaches both to apply and - more importantly - to "
            "defeat, because the Victorian street ruffian's favorite "
            "ambush was the grab from behind. The choke: the attacker "
            "slides the forearm across the defender's throat from behind, "
            "grips his own biceps with the choking hand, places the free "
            "hand behind the defender's head, and squeezes the forearms "
            "together - compressing the carotid arteries on both sides of "
            "the neck. The defense is drilled as a reflex chain: the "
            "instant the arm touches the throat, tuck the chin hard to "
            "the chest (the chin is a shield), grab the choking arm with "
            "both hands and pull down (two hands against one arm wins), "
            "drop the weight low, and turn into the attacker - stepping "
            "around to face him, which unwinds the choke's geometry. If "
            "the choke is already set, the defender fights the hands, "
            "never the arms: peel the fingers, strike the groin or stamp "
            "the instep to break the attacker's concentration, and keep "
            "turning. Tani's teaching is absolute about practice safety: "
            "the choke is applied with control and released the instant "
            "the partner taps or goes limp - a choke held too long injures "
            "or kills, and the Victorians knew it. Drill the defense "
            "chain slowly until the chin-tuck and two-hand pull fire on "
            "contact; the full choke is practiced only between advanced "
            "partners under direct supervision."),
        "how_it_works": (
            "The choke works by blood, not air: the forearms compress the "
            "carotid arteries on both sides of the neck, and the brain, "
            "starved of blood, shuts down in seconds - far faster than any "
            "air choke. That speed is why the defense must be reflexive, "
            "not reasoned. The chin tuck works mechanically: the jawbone "
            "becomes a wedge between the forearm and the arteries, buying "
            "the seconds the hands need. The two-handed pull works by "
            "numbers: the choking arm is one limb driven by the attacker's "
            "squeeze, while the defender's two arms plus dropping body "
            "weight attack it from below - the pull-down redirects the "
            "forearm off the arteries and onto the chin's wedge. Turning "
            "into the attacker works by geometry: the choke's leverage "
            "depends on the attacker being behind, and each degree of turn "
            "bleeds its mechanical advantage until the hold is only an "
            "arm around a facing opponent. The tap-and-release rule works "
            "by trust: partners who know the release is instant will "
            "practice honestly, and honest practice builds the reflex."),
        "key_points": [
            "The choke compresses the carotid arteries; the brain shuts down in seconds - the defense must be reflexive.",
            "On contact: tuck the chin hard, grab the choking arm with both hands, pull down, drop weight, turn in.",
            "Two hands against one arm wins; the chin is a wedge buying seconds for the hands.",
            "Turning bleeds the choke's geometry; each degree of turn unwinds its leverage.",
            "If set: fight the hands (peel fingers), break his concentration, keep turning.",
            "Practice safety is absolute: controlled application, instant release on tap or limpness.",
        ],
        "requirements": [
            "Practice the choke only between advanced partners under direct supervision.",
            "Release instantly on tap or any sign of limpness; a held choke injures or kills.",
            "Drill the defense chain slowly until the chin-tuck and pull fire on contact.",
            "Never practice the full choke on beginners; they learn the defense chain first, the choke much later.",
        ],
        "standards": [STD_KODOKAN, STD_BARTITSU],
        "citations": [CIT_KANO, CIT_BARTONWRIGHT_1899],
        "sig_lens": (
            "Signature original interpretation: his original Signature Combat "
            "Method treats the rear choke's defense as the signature "
            "refusing to be smothered - the chin the hand's guard over the "
            "line, the turn the page rotating free of the covering arm. "
            "Clearly labeled Signature-made."),
    },
    {
        "key": "randori",
        "name": "Randori: Bartitsu Freestyle Sparring",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Randori - freestyle practice - is where Bartitsu's separate "
            "lessons become one fighter, and the Victorians practiced it "
            "under strict conventions that the modern student keeps. The "
            "format: two partners, agreed rules, timed rounds (the "
            "Victorian standard was short, sharp rounds with rest "
            "between), and a clear hierarchy of force - cane work at "
            "controlled speed with padded sticks or pulled cuts, boxing "
            "with gloves, throws only with full ukemi on mats, joint locks "
            "practiced to the tap and never finished. The conventions are "
            "the art: the senior partner sets the pace, either partner "
            "may call a halt at any time, head contact with the cane is "
            "forbidden, and the round stops the instant anyone is hurt. "
            "Randori has three modes. Yakusoku (agreed) randori: partners "
            "alternate attack and defense on call, building the "
            "techniques. Hikitategeiko (guided) randori: the senior lets "
            "the junior work, offering openings. Shiai-style (contest) "
            "randori: full resistance within the rules, the true test. "
            "Barton-Wright insisted his students spar because techniques "
            "unpracticed against resistance are choreography; but he "
            "insisted equally on the conventions, because students broken "
            "in practice cannot train tomorrow. The student's goal in "
            "randori is not to win the round but to apply the ladder: "
            "stance under pressure, measure and tempo against a live "
            "opponent, and one clean technique per round honestly earned."),
        "how_it_works": (
            "Randori works by progressive resistance. Agreed randori "
            "builds the neural pathways: the body learns the technique's "
            "shape without the noise of a resisting opponent. Guided "
            "randori adds aliveness: the senior's offered openings teach "
            "the junior to recognize the real thing, while the junior's "
            "attacks stay honest enough to keep the senior sharp. Contest "
            "randori adds the truth: against full resistance, only the "
            "techniques that survive contact remain, and the student "
            "learns which of his tools are real and which were "
            "choreography. The conventions are what make this progression "
            "possible: without the tap rule, no one would practice locks; "
            "without the pulled-cut rule, no one would practice cane "
            "defense; without the senior's pace-setting, beginners would "
            "be injured out of the art in a month. The timed rounds work "
            "physiologically: short sharp rounds with rest build the "
            "exact energy systems a real encounter demands - explosive "
            "effort, quick recovery, repeat."),
        "key_points": [
            "Three modes: agreed (yakusoku), guided (hikitategeiko), contest (shiai-style) - in that order.",
            "Agreed rules, timed rounds, hierarchy of force: pulled cuts, gloved boxing, throws only with ukemi, locks to the tap.",
            "The senior sets the pace; either partner may halt; head contact with the cane is forbidden.",
            "Techniques unpracticed against resistance are choreography; conventions keep students training tomorrow.",
            "Goal per round: apply the ladder under pressure - stance, measure, tempo, one clean technique honestly earned.",
            "Short sharp rounds with rest build the exact energy systems a real encounter demands.",
        ],
        "requirements": [
            "Full protective gear for the mode: headgear, gloves, padded canes as the rules require.",
            "Mats under all throwing randori; no exceptions, no matter the partners' experience.",
            "The tap is law and the halt call is law; violating either ends the partnership.",
            "Beginners start in agreed randori only; contest randori is earned through the ladder.",
        ],
        "standards": [STD_BARTITSU, STD_KODOKAN],
        "citations": [CIT_BARTONWRIGHT_1899, CIT_KANO, CIT_WOLF],
        "sig_lens": (
            "Signature original interpretation: his original Signature Combat "
            "Method treats randori as the signature tested against another "
            "hand - the agreed rounds the practice sheets, the contest the "
            "final document, the conventions the margins that keep every "
            "hand safe. Clearly labeled Signature-made."),
    },
    {
        "key": "grand_combination",
        "name": "The Grand Combination: The Complete Bartitsu Sequence",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The Grand Combination is Bartitsu's capstone drill: a single "
            "flowing sequence that runs the entire art from long measure "
            "to the ground, and the student's graduation exercise. The "
            "canonical sequence: from guard at long measure, beat the "
            "opponent's cane (or imagined point) aside and thrust; as the "
            "distance closes, cut overhead to the weapon arm; follow with "
            "the one-two-low-kick (straight, hook, coup de pied bas); "
            "close to clinch with the two-handed cane trap across his arm; "
            "step through into the cane-assisted hip throw; finish in juji "
            "gatame, holding the pin for the three-count. Every link "
            "demands the ladder beneath it - the thrust needs the lunge, "
            "the cut needs the wrist, the punches need the pivot, the kick "
            "needs the chamber, the trap needs the frame, the throw needs "
            "the fulcrum, the lock needs the hips. The sequence is "
            "practiced in three stages: solo in the air for flow, with a "
            "cooperative partner walking through each link, and finally at "
            "speed against pads and a throwing dummy, the partner "
            "supplying only the agreed resistance. The Grand Combination "
            "is not a fight choreography to memorize - it is the proof "
            "that the four arts have become one art in the student's body, "
            "and Barton-Wright's examiners watched for exactly that: not "
            "the sequence, but the seamlessness."),
        "how_it_works": (
            "The Grand Combination works as a systems test. Each link "
            "stresses a different subsystem - measure management in the "
            "thrust, rotational power in the cut, chaining in the "
            "one-two-low-kick, close-range adaptation in the trap, "
            "leverage in the throw, control in the lock - and the "
            "transitions between links stress the handoffs: can the "
            "student go from striking range to clinch without a balance "
            "debt, from the throw to the ground control without losing "
            "the arm? A break anywhere reveals the weak subsystem, which "
            "is the drill's diagnostic purpose. The flow itself works by "
            "the same chunking as combinations: practiced until each link "
            "fires as one motion, the seven-link sequence becomes a "
            "single decision, and the student's conscious mind is free to "
            "watch the opponent instead of managing his own body. That "
            "freedom is the graduation: the art has moved from the head "
            "into the hands, which is the only place it can be used."),
        "key_points": [
            "The capstone sequence: thrust, overhead cut, one-two-low-kick, cane trap, cane-assisted hip throw, juji gatame pin.",
            "Runs the entire art from long measure to the ground in one flowing sequence.",
            "Every link demands its ladder beneath it; the transitions test the handoffs between subsystems.",
            "Three practice stages: solo for flow, cooperative partner for links, speed against pads and dummy.",
            "A break anywhere diagnoses the weak subsystem; the drill is a test, not a performance.",
            "Graduation is seamlessness: the sequence as a single decision, the art moved from head to hands.",
        ],
        "requirements": [
            "Attempt only after every component technique is clean; the capstone punishes weak links.",
            "Practice the solo flow daily; the partner walk-through weekly; speed monthly.",
            "Use pads, dummies, and mats for the speed stage; no full-speed throws on partners in this drill.",
            "Have an instructor watch the transitions; the handoffs hide the faults the links do not.",
        ],
        "standards": [STD_BARTITSU, STD_VIGNY, STD_KODOKAN, STD_SAVATE, STD_QUEENSBERRY],
        "citations": [CIT_BARTONWRIGHT_1899, CIT_BARTONWRIGHT_1901, CIT_WOLF],
        "sig_lens": (
            "Signature original interpretation: his original Signature Combat "
            "Method treats the Grand Combination as the full signature at "
            "last - every stroke of the name written in one unbroken hand, "
            "from the first downstroke to the final dot, the whole covenant "
            "signed. Clearly labeled Signature-made."),
    },
    {
        "key": "teaching",
        "name": "Preserving the Art: Teaching Bartitsu",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Teaching Bartitsu is the final technique in the database, "
            "because an art that is not taught dies - as Bartitsu itself "
            "nearly did in the twentieth century. The teaching ladder "
            "mirrors this database: foundations first (stance, footwork, "
            "grip, ukemi - the first months), compounded second (cuts, "
            "strikes, kicks, throws - the first year), advanced last "
            "(counters, ground control, randori, the Grand Combination - "
            "the years after). The Victorian method, preserved in "
            "Barton-Wright's articles and the Bartitsu Compendium, has "
            "rules the modern teacher keeps: demonstrate, then drill, "
            "then correct - never correct before the student has felt the "
            "movement; teach one fault at a time, the biggest first; "
            "praise the effort publicly and correct the error privately; "
            "and never teach a technique you cannot perform safely "
            "yourself. Safety is the teacher's first art: the tap rule, "
            "the pulled cut, the mat under every throw, the training "
            "blade in every knife drill - the teacher who injures students "
            "has no students. Lineage is the teacher's second art: name "
            "the sources (Barton-Wright, Vigny, Tani, Charlemont), show "
            "the articles, keep the techniques traditional - the student "
            "who knows where the art came from will carry it where it "
            "needs to go. The examination is the Grand Combination, "
            "judged on seamlessness; the diploma is the student's first "
            "class of his own."),
        "how_it_works": (
            "Teaching works by the same ladder the art is learned on. The "
            "foundations-first order is not tradition for tradition's "
            "sake: each tier's techniques are the prerequisites of the "
            "next tier's, so teaching out of order builds on missing "
            "structure and the advanced techniques fail dangerously. The "
            "demonstrate-drill-correct cycle works by motor learning: the "
            "demonstration gives the eyes a model, the drill gives the "
            "body repetitions, and the correction - delivered after the "
            "feeling, one fault at a time - gives the nervous system a "
            "single clear adjustment instead of a confusing list. The "
            "safety conventions work economically: a school that never "
            "injures students keeps its students, and kept students become "
            "the advanced practitioners who preserve the art. The lineage "
            "teaching works by identity: a student who can name "
            "Barton-Wright's academy and Vigny's method is not just "
            "learning moves but joining a tradition, and traditions are "
            "what survive the century that nearly killed this one."),
        "key_points": [
            "Teach in ladder order: foundations, then compounded, then advanced - each tier is the next tier's prerequisite.",
            "Demonstrate, then drill, then correct; correct one fault at a time, the biggest first.",
            "Safety is the teacher's first art: tap rule, pulled cuts, mats, training blades - no injured students.",
            "Lineage is the teacher's second art: name Barton-Wright, Vigny, Tani, Charlemont; show the sources.",
            "Never teach a technique you cannot perform safely yourself.",
            "The examination is the Grand Combination judged on seamlessness; the diploma is the student's first class.",
        ],
        "requirements": [
            "New teachers assist a senior for a full ladder cycle before taking their own class.",
            "Keep a written curriculum with the ladder order; do not improvise the progression.",
            "Inspect all equipment - canes, mats, pads, training blades - before every class.",
            "Record each student's ladder progress; no student advances a tier with missing prerequisites.",
        ],
        "standards": [STD_BARTITSU],
        "citations": [CIT_BARTONWRIGHT_1899, CIT_WOLF],
        "sig_lens": (
            "Signature original interpretation: his original Signature Combat "
            "Method treats teaching as the signature teaching other hands "
            "to sign - the ladder the practice sheets, the student's first "
            "class the moment the covenant copies itself, the art living "
            "because the hand taught the hand. Clearly labeled "
            "Signature-made."),
    },
]
