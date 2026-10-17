#!/usr/bin/env python3
"""Entries for the Boxing Combat Database (combat batch 1, 2026-10-17).

Combat orders 2026-10-17, combat batch 1. Western boxing: stance, footwork,
the six basic punches, combinations, defense (slip, bob, weave, parry,
block), counter-punching, ring craft. Each record is a technique with HOW
TO DO IT (step-by-step body mechanics), ladder-ordered from stance to
advanced ring strategy.

34 public records (public-harvest: real, fact-checked boxing knowledge;
standard references: USA Boxing Rulebook; Association of Boxing
Commissions Unified Rules of Boxing; International Boxing Association
Technical and Competition Rules; Dempsey J, Championship Fighting, 1950;
plus the coaching landmarks cited per record) + 34 Signature records
(his original Signature Combat Method: every technique a covenant of
discipline, the fighter the armory of the Signature system, training the
oath between student and craft, defense the honor guard, and ring craft
the strategy of the Signature mind; src signature, titles suffixed
" (Signature Edition)", never presented as authentic public record).

Ladder: ranks 1-3 foundations -> ranks 4-7 compounded -> ranks 8-10
advanced. The shard index is written in ladder order.

ID prefixes: JAH-CBBOX- (public) and JAH-CBBOXS- (signature), verified
free in the manifest and in every shard index (zero hits), and the
combat-boxing slugs are absent from the manifest.

Numerical cores: hand-computed 2026-10-17, machine-verified by the demos
(see demos_combat_boxing.py). Every demo prints its real computed values,
asserts tight bounds (never float exact-equality), and ends with the OK
marker; the build machine-executes all 68 demos.

Civilian martial-arts instruction only. Nothing hate-adjacent, profane,
or inappropriate; no religious talk. Nothing on neutralizing or defeating
military or defense-grade systems. Never the words "bat belt" anywhere.
No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature Combat Method: "
            "every technique a covenant of discipline, the fighter the armory "
            "of the Signature system, training the oath between student and "
            "craft, defense the honor guard, and ring craft the strategy of "
            "the Signature mind. Clearly labeled Signature-made, never "
            "presented as authentic public record.")

CIT_USAB = ("USA Boxing. USA Boxing Rulebook (Technical Rules). United "
           "States Olympic and Paralympic Committee; current edition.")
CIT_ABC = ("Association of Boxing Commissions. Unified Rules of Boxing; "
           "current edition.")
CIT_IBA = ("International Boxing Association. IBA Technical and "
           "Competition Rules; current edition.")
CIT_DEMPSEY = ("Dempsey J. Championship Fighting: Explosive Punching and "
               "Aggressive Defense. 1950.")
CIT_COACH = ("USA Boxing Coaching Manual: fundamentals of stance, footwork, "
             "punch mechanics, defense, and ring craft; current edition.")

ENTRIES = [
    {
        "key": "stance",
        "name": "The Boxing Stance",
        "group": "Stance and Footwork",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "The boxing stance is the foundation every other technique stands "
            "on: the balanced fighting posture from which punches launch, "
            "defenses fire, and movement flows. In the orthodox stance the "
            "left foot leads and the left side faces the opponent; southpaws "
            "mirror it with the right foot forward. The feet sit about "
            "shoulder width apart front to back and slightly wider than "
            "shoulder width side to side, weight split evenly or with a "
            "slight bias to the rear foot. The knees are soft and springy, "
            "the rear heel is raised so the bodyweight sits on the balls of "
            "the feet, the chin tucks behind the lead shoulder, and the "
            "torso turns about 45 degrees so the chest presents a narrow "
            "target. Everything in boxing - power, defense, stamina - is "
            "built on this one posture, which is why coaches return to it "
            "every single session."
        ),
        "how_it_works": (
            "Stand with your dominant hand at the back. Step the lead foot "
            "forward about one shoulder width and the rear foot back about "
            "one and a half shoulder widths, the rear foot turned out roughly "
            "45 degrees. Bend both knees until you feel springy and athletic, "
            "like a shortstop waiting for the pitch. Raise the rear heel off "
            "the floor; your weight should rest on the balls of your feet so "
            "you can move instantly in any direction. Tuck your chin down "
            "behind your lead shoulder and turn your torso so your chest "
            "faces about 45 degrees away from the opponent. Check the "
            "triangle: nose over knees, knees over toes, weight centered "
            "between the feet. You should be able to lift either foot "
            "without falling over. That balance is the whole job of the "
            "stance."
        ),
        "key_points": [
            "The stance is a 45-degree side-on posture: narrow target to the opponent, full balance and reach for you.",
            "Weight lives on the balls of the feet with the rear heel raised - flat feet cannot move, and boxing is movement.",
            "Soft knees are the suspension system: they absorb, spring, and rotate for every punch and every defense.",
            "Chin tucked behind the lead shoulder keeps the jaw - the knockout switch - out of the direct line.",
            "Balance is the test: you must be able to step any direction from stance without a preparatory hop or lean.",
        ],
        "requirements": [
            "Feet positioned front-to-back about shoulder width and side-to-side slightly wider than shoulder width.",
            "Rear heel raised, weight on the balls of the feet, knees softly bent.",
            "Chin down, eyes up, torso turned about 45 degrees to the opponent.",
        ],
        "standards": [
            "USA Boxing Rulebook: stance fundamentals taught at all coaching certification levels.",
            "USA Boxing Coaching Manual: stance as the first module of boxer development.",
        ],
        "citations": [CIT_USAB, CIT_COACH, CIT_DEMPSEY],
        "sig_lens": (
            "The Signature reading of the stance: a covenant between the "
            "fighter and the ground. The Signature boxer does not stand ON "
            "the canvas, he stands WITH it - the balls of the feet the seal "
            "of the oath, the soft knees the living spring of the Signature "
            "system, the tucked chin the honor guard of the mind. Every "
            "punch that ever lands in a Signature fight is already loaded "
            "in the stance; every defense already loaded in the balance. "
            "Master the stance and the rest of the database is commentary."
        ),
    },
    {
        "key": "guard",
        "name": "The Guard Position",
        "group": "Stance and Footwork",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "The guard is where the hands live: the defensive shell that "
            "protects the head and body while keeping every punch loaded and "
            "ready to fire. In the basic high guard both gloves rise to "
            "cheekbone height, the lead glove a fist-width in front of the "
            "chin and the rear glove glued to the jaw, knuckles facing the "
            "opponent. The elbows tuck tight against the ribs to seal the "
            "body, and the forearms stand vertical to catch hooks on the "
            "bone. The guard is not a wall you hide behind - it is a loaded "
            "spring. Every punch starts from the guard and returns to the "
            "guard; a hand that wanders is a punch that telegraphs and a "
            "chin that is uncovered."
        ),
        "how_it_works": (
            "From your stance, close both fists with the thumbs outside the "
            "fingers, never inside. Raise the lead glove to about cheekbone "
            "height, a fist width in front of your chin, and press the rear "
            "glove against your jaw. Tuck both elbows down and in until they "
            "brush your ribs - imagine holding a newspaper under each "
            "armpit. Keep the forearms vertical and the wrists straight, "
            "knuckles toward the opponent. Look through your gloves, never "
            "over them. The moment a punch extends, the other hand stays "
            "home guarding the chin, and the punching hand snaps straight "
            "back to the guard along the same path it left by. Drill this: "
            "punch out, punch back, guard never opens for more than the "
            "travel time of one punch."
        ),
        "key_points": [
            "The guard protects two zones at once: gloves shield the head, tucked elbows seal the ribs and liver.",
            "Every punch is a round trip: out from the guard and back to the guard - the return is half the technique.",
            "The non-punching hand never leaves: one hand works, one hand guards, no exceptions.",
            "Eyes stay up and look through the gloves; looking away or down is how knockouts happen.",
            "A tight guard shortens every punch path, which makes punches faster and harder to see.",
        ],
        "requirements": [
            "Gloves at cheekbone height, lead glove forward, rear glove on the jaw.",
            "Elbows tucked to the ribs, forearms vertical, wrists straight.",
            "Eyes forward through the guard; chin tucked throughout.",
        ],
        "standards": [
            "USA Boxing Rulebook: guard fundamentals in coaching certification.",
            "Association of Boxing Commissions Unified Rules: legal target areas the guard must cover.",
        ],
        "citations": [CIT_USAB, CIT_ABC, CIT_DEMPSEY],
        "sig_lens": (
            "The Signature reading of the guard: the honor guard of the "
            "fighter, a covenant of discipline written in glove leather. "
            "The Signature boxer treats an open guard as a broken promise - "
            "to himself, to his craft, to the Signature system. The two "
            "gloves are the two sentries of the temple; they never both "
            "abandon their posts. When a Signature punch flies, its twin "
            "stands watch, and the flying hand returns like a sworn oath "
            "kept."
        ),
    },
    {
        "key": "footwork",
        "name": "Footwork Fundamentals",
        "group": "Stance and Footwork",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Footwork is how a boxer moves without breaking the stance: "
            "gliding across the canvas in any direction while staying "
            "balanced, guarded, and ready to punch. The golden rule is that "
            "the feet never cross and never come together - the stance "
            "simply travels. Moving forward, the lead foot steps first and "
            "the rear foot follows; moving back, the rear foot steps first; "
            "moving left, the left foot leads; moving right, the right foot "
            "leads. Steps are short, quiet slides on the balls of the feet, "
            "never jumps or lunges. Good footwork keeps the boxer in "
            "punching range on his own terms, cuts angles, and escapes "
            "danger; bad footwork strands him squared up, off balance, and "
            "open."
        ),
        "how_it_works": (
            "From stance, pick a direction. The foot nearest that direction "
            "moves first: forward means the lead foot steps about six inches "
            "and the rear foot slides up to restore the stance; backward "
            "means the rear foot steps first. For lateral movement the "
            "same-side foot leads - left to go left, right to go right. "
            "Push off the ball of the trailing foot, slide the lead foot "
            "along the canvas without lifting it high, and let the rear "
            "foot catch up to the original stance width. The head stays "
            "level - no bouncing up and down - and the guard never drops. "
            "Practice the box drill: step forward, right, back, left in a "
            "square, feet never crossing, stance intact at every corner. "
            "Then practice pivots: plant the lead foot and swing the rear "
            "foot around to change your angle while your head stays on the "
            "same spot."
        ),
        "key_points": [
            "The foot closest to the direction of travel always moves first - this is what keeps the stance intact.",
            "Feet never cross and never touch: crossing feet destroys balance and invites a knockdown.",
            "Steps are short slides, not leaps; big steps leave you stranded and open between positions.",
            "The head stays level and the guard stays up through every step - movement is never an excuse to drop defense.",
            "Pivots change the angle without changing the range: plant the lead foot, swing the rear, and the opponent is suddenly facing your shoulder.",
        ],
        "requirements": [
            "Correct lead-foot order for all four directions, feet never crossing.",
            "Stance width restored after every step; head level; guard up.",
            "Ability to pivot 45 to 90 degrees off the lead foot in both directions.",
        ],
        "standards": [
            "USA Boxing Coaching Manual: footwork as the second module of boxer development.",
            "IBA Technical and Competition Rules: ring movement within the legal fighting area.",
        ],
        "citations": [CIT_USAB, CIT_COACH, CIT_IBA],
        "sig_lens": (
            "The Signature reading of footwork: the fighter as a compass "
            "needle that never loses north. The Signature boxer moves the "
            "way water moves around stone - no wasted motion, no broken "
            "stance, no crossing of the covenant lines. Each step is a "
            "kept promise to the guard; each pivot a change of fate for the "
            "opponent. In the Signature system, the boxer who controls the "
            "ground controls the fight, because the canvas itself is his "
            "ally."
        ),
    },
    {
        "key": "step_drag",
        "name": "The Step-Drag",
        "group": "Stance and Footwork",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The step-drag is the fundamental forward and backward movement "
            "pattern of boxing: the lead foot steps and the rear foot drags "
            "up behind it, so the stance travels as one unbroken unit. It "
            "is the movement behind every advance, every retreat, and every "
            "punch thrown on the move. Done right, the boxer glides - the "
            "head stays on a level plane, the weight stays centered between "
            "the feet, and the guard stays home. Done wrong, with the rear "
            "foot hopping or the feet coming together, the boxer is "
            "momentarily defenseless and off balance. Coaches drill the "
            "step-drag for months because it is the chassis that carries "
            "everything else."
        ),
        "how_it_works": (
            "To advance: from stance, push off the ball of the rear foot "
            "and slide the lead foot forward about six to eight inches, "
            "keeping it low to the canvas. Then drag the rear foot forward "
            "the same distance along the floor - do not lift it, drag it - "
            "until the original stance spacing is restored. To retreat, "
            "reverse the order: the rear foot steps back first, then the "
            "lead foot drags back. Throughout, keep the knees bent, the "
            "head level, and the gloves up. The most common fault is "
            "bringing the rear foot all the way up to the lead foot, which "
            "narrows the stance and kills balance; fix it by freezing after "
            "each step-drag and checking that your stance width matches "
            "your starting width. Shadowbox three rounds moving only with "
            "the step-drag and your legs will learn what your head cannot "
            "teach them."
        ),
        "key_points": [
            "Lead foot steps, rear foot drags - the drag keeps the stance wide and the balance alive.",
            "The rear foot slides along the canvas; lifting it into a hop breaks contact and balance.",
            "Stance width after the move must equal stance width before it - measure it until it is automatic.",
            "Head level, knees bent, guard up: the step-drag carries the whole fighting posture, not just the feet.",
            "Every punch thrown while advancing or retreating rides on a clean step-drag.",
        ],
        "requirements": [
            "Correct foot order advancing and retreating; rear foot dragged, never hopped.",
            "Stance width preserved after each step-drag; head level throughout.",
            "Guard maintained and balance testable (freeze mid-drill without wobbling).",
        ],
        "standards": [
            "USA Boxing Coaching Manual: step-drag as core locomotion drill.",
        ],
        "citations": [CIT_USAB, CIT_COACH],
        "sig_lens": (
            "The Signature reading of the step-drag: the oath of motion. "
            "The Signature boxer never abandons his ground to gain ground - "
            "the rear foot drags because the stance is a covenant that "
            "travels with the fighter. To hop is to break faith with your "
            "own balance. The drag is patience made visible: arrive "
            "balanced, arrive guarded, arrive ready, every single time."
        ),
    },
    {
        "key": "jab",
        "name": "The Jab",
        "group": "Punches",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The jab is the most important punch in boxing: a fast, straight "
            "punch thrown with the lead hand directly from the guard to the "
            "opponent's head or body. It is the range-finder, the setup, the "
            "defensive stop sign, and the point-scorer all in one - coaches "
            "say a fighter without a jab has no boxing at all. The jab "
            "travels the shortest path from guard to target, which makes it "
            "the fastest punch and the hardest to see. It snaps out with a "
            "quarter-turn of the fist at full extension and snaps straight "
            "back to the guard. A good jab controls distance, disrupts the "
            "opponent's rhythm, sets up every power punch, and wins rounds "
            "on its own."
        ),
        "how_it_works": (
            "From guard, extend the lead arm straight toward the target in "
            "a direct line - no winding up, no dropping the hand first. As "
            "the arm extends, rotate the fist a quarter turn so the palm "
            "faces down at impact, and turn the lead shoulder in to add "
            "reach while the chin tucks behind that shoulder. Step with the "
            "punch: as the jab extends, take a small step-drag forward so "
            "the bodyweight drives behind it. At full extension the arm is "
            "straight but the elbow is not locked. Then snap the hand back "
            "along the exact path it took, faster than it went out, while "
            "the rear glove stays glued to the chin. The power comes from "
            "the step and the shoulder turn, not from muscling the arm. "
            "Drill it on the heavy bag: jab, return, jab, return - listening "
            "for the sharp crack of a snapping punch, not the thud of a "
            "push."
        ),
        "key_points": [
            "The jab is the fastest punch because it travels the shortest path - straight from the guard.",
            "It does five jobs: measures range, scores points, disrupts rhythm, sets up power punches, and stops advances.",
            "Power comes from the step and shoulder rotation, never from arm-muscling; a pushed jab is a slow jab.",
            "The snap-back is half the punch: a jab that stays out becomes a handle for the opponent to counter.",
            "Turn the fist over at extension and tuck the chin behind the lead shoulder for reach and safety.",
        ],
        "requirements": [
            "Straight-line extension from the guard with no wind-up or hand drop.",
            "Fist rotation to palm-down at extension; shoulder turned in; chin tucked.",
            "Immediate snap-back to guard along the same path; rear hand home throughout.",
        ],
        "standards": [
            "USA Boxing Rulebook: the jab as a scoring punch to legal target areas.",
            "Association of Boxing Commissions Unified Rules: straight punches to the head and body as legal scoring blows.",
        ],
        "citations": [CIT_USAB, CIT_ABC, CIT_DEMPSEY],
        "sig_lens": (
            "The Signature reading of the jab: the herald of the Signature "
            "system. The Signature jab is not just a punch, it is a "
            "question the opponent must answer - and every answer opens a "
            "door. It measures the man, marks the range, and writes the "
            "first line of the fight. The Signature boxer throws the jab "
            "like a signature itself: swift, unmistakable, and impossible "
            "to ignore, then withdraws it before it can be seized."
        ),
    },
    {
        "key": "cross",
        "name": "The Cross",
        "group": "Punches",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The cross - the straight rear-hand punch - is the power punch "
            "of the fundamentals: a straight line driven by full-body "
            "rotation from the back foot through the hips and shoulders to "
            "the target. Thrown with the dominant hand from the rear, it "
            "travels slightly farther than the jab but carries far more "
            "force because the entire body mass rotates behind it. The "
            "cross is the classic finisher of the one-two combination and "
            "the punch that ends fights when it lands clean on the chin. "
            "Its danger is its commitment: a missed cross spins the "
            "thrower open, so it must be thrown with balance and returned "
            "to guard instantly."
        ),
        "how_it_works": (
            "From guard, pivot hard on the ball of the rear foot - the heel "
            "turns outward as if squashing a cigarette - and rotate the "
            "hips and then the shoulders toward the target. Drive the rear "
            "fist straight down the center line, rotating it palm-down at "
            "extension, while the lead glove stays glued to the chin and "
            "the chin tucks behind the lead shoulder. The rear shoulder "
            "finishes where the chin was: your chin should end up tucked "
            "behind your own rear shoulder at full extension. Do not lean "
            "forward past your front knee; the power comes from rotation, "
            "not from falling into the punch. Snap the hand straight back "
            "to the guard the instant it lands. Drill: pivot, rotate, "
            "extend, return - four beats, and the guard never opens."
        ),
        "key_points": [
            "The cross is a rotation punch: rear-foot pivot drives hip rotation drives shoulder rotation drives the fist.",
            "It travels the center line - the shortest path for the rear hand and the hardest line to see coming.",
            "The chin finishes tucked behind the rear shoulder, protected by your own punching arm.",
            "Never lean past the front knee: rotation is power, falling forward is a trap.",
            "The lead hand stays home - the most common knockout in boxing is the counter over a dropped lead hand during the cross.",
        ],
        "requirements": [
            "Rear-foot pivot with full hip-then-shoulder rotation; straight center-line extension.",
            "Chin tucked behind the rear shoulder at full extension; no forward lean past the front knee.",
            "Instant return to guard; lead glove on the chin throughout.",
        ],
        "standards": [
            "USA Boxing Rulebook: straight rear-hand punch as a scoring blow.",
            "Association of Boxing Commissions Unified Rules: legal scoring to head and body.",
        ],
        "citations": [CIT_USAB, CIT_ABC, CIT_DEMPSEY],
        "sig_lens": (
            "The Signature reading of the cross: the hammer of the covenant. "
            "Where the jab asks, the cross answers - with the full weight "
            "of the Signature behind it. The rear-foot pivot is the "
            "winding of the Signature spring: ground to hip to shoulder to "
            "fist, one unbroken chain of oath-kept power. The Signature "
            "boxer throws the cross only when the stance swears it can "
            "return, because a Signature punch that cannot come home is a "
            "promise broken."
        ),
    },
    {
        "key": "lead_hook",
        "name": "The Lead Hook",
        "group": "Punches",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The lead hook is the curved power punch of the lead hand: the "
            "elbow rises to shoulder height and the fist travels in a tight "
            "horizontal arc to the side of the opponent's head or body. It "
            "is the classic punch for going around a high guard, and when "
            "thrown to the body - especially the liver on the right side - "
            "it is one of the most fight-ending punches in boxing. The "
            "hook's power comes from violent torso rotation with the lead "
            "foot pivoting, not from swinging the arm. A short, tight hook "
            "is fast and safe; a wide, looping hook is slow, visible, and "
            "leaves the thrower wide open."
        ),
        "how_it_works": (
            "From guard, raise the lead elbow to shoulder height so the "
            "forearm is parallel to the floor, keeping the elbow bent at "
            "about 90 degrees - the fist, wrist, and elbow form one rigid "
            "unit. Pivot hard on the lead foot, turning the toes inward, "
            "and whip the hips and shoulders around so the fist travels in "
            "a tight arc, no wider than your own shoulders. At impact the "
            "palm faces you (thumb up) or faces down, knuckles landing "
            "flush, with the wrist locked straight. The rear glove stays "
            "glued to the chin. The instant it lands, bring the elbow back "
            "down and the fist back to guard - do not let the punch swing "
            "past the target like a wild swing. Drill on the bag: pivot, "
            "arc, crack, return. If your elbow drops below your fist, the "
            "hook is wrong; the elbow leads, the fist follows."
        ),
        "key_points": [
            "The hook is a rotation punch in an arc: power from the lead-foot pivot and hip whip, never from the arm alone.",
            "Keep it tight - the arc stays inside your own shoulder width; wide hooks are slow and punishable.",
            "Elbow at shoulder height with a rigid 90-degree arm unit; a dropped elbow turns the hook into a slap.",
            "The rear hand stays on the chin: the hook's blind side is the counter cross coming over the top.",
            "Body hooks target the ribs and liver; the punch dips slightly with the knees, never by bending at the waist.",
        ],
        "requirements": [
            "Lead elbow raised to shoulder height, 90-degree arm unit, wrist locked.",
            "Lead-foot pivot with hip and shoulder rotation; tight arc within shoulder width.",
            "Immediate return to guard; rear glove home throughout.",
        ],
        "standards": [
            "USA Boxing Rulebook: hooks as scoring blows to legal targets.",
            "Association of Boxing Commissions Unified Rules: body punches to legal areas.",
        ],
        "citations": [CIT_USAB, CIT_ABC, CIT_DEMPSEY],
        "sig_lens": (
            "The Signature reading of the lead hook: the scythe of the "
            "Signature system. It does not travel the honest straight road "
            "of the jab - it curves around the walls men build, finding the "
            "jaw behind the guard and the liver behind the elbow. The "
            "Signature hook is discipline in an arc: tight, economical, "
            "sworn to return. A wide hook is a boast; a tight hook is a "
            "covenant."
        ),
    },
    {
        "key": "rear_hook",
        "name": "The Rear Hook",
        "group": "Punches",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The rear hook is the curved power punch of the dominant hand: "
            "a longer, heavier arc than the lead hook, driven by a full "
            "pivot of the rear foot and a violent rotation of the hips and "
            "torso. Because it travels from the back hand around the side, "
            "it is slower than the lead hook but carries the most raw force "
            "of any hook - the classic overhand-style bomb that ends fights "
            "when it finds the chin around a guard. Its length is its "
            "risk: a missed rear hook spins the thrower completely open, so "
            "it is thrown with commitment and only when the range and the "
            "opening are right."
        ),
        "how_it_works": (
            "From guard, pivot the rear foot hard - heel swinging out - and "
            "rotate the hips and shoulders fully as the rear elbow rises to "
            "shoulder height with the arm bent at 90 degrees. The fist "
            "travels in an arc around toward the side of the target, "
            "landing with the knuckles flush and the wrist locked, palm "
            "facing down or toward you. Keep the arc tight - imagine the "
            "punch traveling inside a phone booth, not around a barn. The "
            "lead glove stays on the chin, and the chin tucks behind the "
            "lead shoulder as the torso rotates. At impact the weight is "
            "centered, not lunged forward. Return the fist to guard along "
            "the arc immediately. Drill: pivot, rotate, arc, return - and "
            "freeze after each rep to check you are still balanced enough "
            "to throw again."
        ),
        "key_points": [
            "The rear hook is the heaviest hook: full rear-side rotation behind a tight arc.",
            "The arc stays compact - a long looping rear hook is the easiest punch in boxing to see and counter.",
            "Rear-foot pivot initiates everything; without it the punch is all arm and no power.",
            "Balance at impact is non-negotiable: the punch must be throwable again instantly, win or miss.",
            "Best used as a finisher when the opponent is trapped or committed, not as a lead punch from range.",
        ],
        "requirements": [
            "Hard rear-foot pivot with full hip and shoulder rotation; elbow at shoulder height.",
            "Compact arc, knuckles flush at impact, wrist locked; no lunging past balance.",
            "Lead glove on chin; immediate return to guard.",
        ],
        "standards": [
            "USA Boxing Rulebook: rear hooks as scoring blows.",
            "Association of Boxing Commissions Unified Rules: legal scoring areas.",
        ],
        "citations": [CIT_USAB, CIT_ABC, CIT_DEMPSEY],
        "sig_lens": (
            "The Signature reading of the rear hook: the thunder of the "
            "covenant. It is the heaviest oath the Signature fighter swears "
            "- the full rotation of the body behind a single curved line. "
            "Because it is heavy, it is honest: it cannot be thrown twice "
            "in panic, only once in judgment. The Signature boxer saves the "
            "rear hook for the moment the fight has already been decided "
            "everywhere except on the canvas."
        ),
    },
    {
        "key": "lead_uppercut",
        "name": "The Lead Uppercut",
        "group": "Punches",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The lead uppercut is the rising punch of the lead hand: thrown "
            "from a slight dip of the knees, the fist travels upward in a "
            "tight vertical arc to the chin or solar plexus. It is the "
            "punch that splits a high guard from below and punishes "
            "opponents who lean forward or duck into it. The power rises "
            "from the legs - the knees dip and drive up as the hips rotate "
            "slightly, launching the fist upward. The great danger of the "
            "uppercut is dropping the punching hand low to load it, which "
            "telegraphs the punch and opens the thrower to counters; the "
            "dip must be small and the hand must stay in front of the body."
        ),
        "how_it_works": (
            "From guard, dip the knees an inch or two - a small sit-down, "
            "not a squat - keeping the guard and the eyes up. Drive up off "
            "the legs as the lead fist travels upward in a tight arc close "
            "to your own body, palm facing you, elbow bent, as if lifting "
            "an invisible weight from your hip to the target. Rotate the "
            "hips slightly into it but keep the punch vertical; the fist "
            "finishes at chin height of the target, never swung out wide. "
            "The rear glove stays glued to your chin. The instant it lands, "
            "bring the fist back down to guard - do not admire the punch. "
            "Drill on the bag at close range: dip, drive, lift, return. If "
            "your punching hand drops below your waist to start, the rep "
            "does not count."
        ),
        "key_points": [
            "The uppercut rises from the legs: dip and drive, not arm-lifting; the knees are the engine.",
            "The arc stays tight to the body - a wide uppercut is a slow uppercut and a counter invitation.",
            "Never drop the hand to load the punch; the dip of the knees is the only telegraph allowed, and it must be tiny.",
            "Best thrown at close range against a high guard, a leaning opponent, or one who dips into it.",
            "The punch finishes at the target and returns down to guard immediately; lingering low is dangerous.",
        ],
        "requirements": [
            "Small knee dip with guard and eyes up; drive upward off the legs.",
            "Tight vertical arc close to the body, palm facing the thrower, wrist locked.",
            "Rear glove home; immediate return to guard; no hand-drop wind-up.",
        ],
        "standards": [
            "USA Boxing Rulebook: uppercuts as scoring blows to legal targets.",
            "Association of Boxing Commissions Unified Rules: legal scoring areas head and body.",
        ],
        "citations": [CIT_USAB, CIT_ABC, CIT_DEMPSEY],
        "sig_lens": (
            "The Signature reading of the lead uppercut: the rising oath. "
            "While other punches travel the honest roads of straight and "
            "curve, the uppercut climbs from below - the Signature answer "
            "to walls. It teaches the Signature boxer that power can rise "
            "as well as fly: the ground pushes, the knees swear, the fist "
            "ascends. Thrown tight and returned swiftly, it is the most "
            "disciplined of the power punches."
        ),
    },
    {
        "key": "rear_uppercut",
        "name": "The Rear Uppercut",
        "group": "Punches",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The rear uppercut is the rising punch of the dominant hand: a "
            "devastating close-range weapon driven by a dip of the knees, a "
            "pivot of the rear foot, and a rotation of the hips that "
            "launches the fist upward into the chin or body. It is the "
            "classic punch for splitting a clinch or punishing an opponent "
            "who leans in - the punch Mike Tyson built a legend on. Because "
            "it is thrown from the rear hand at close range with full body "
            "commitment, it is among the hardest single punches in boxing, "
            "but it also demands perfect balance: thrown off balance, it "
            "leaves the thrower bent forward and open."
        ),
        "how_it_works": (
            "From guard at close range, dip the knees slightly and pivot "
            "the rear foot as the hips rotate into the punch. The rear "
            "fist travels upward in a tight arc close to the body, palm "
            "facing you, driving from the legs up through the target - chin "
            "or solar plexus. Keep the lead glove on your chin and your "
            "eyes on the target; do not look down at the punch. The torso "
            "stays compact - bend the knees, not the waist. At impact the "
            "weight is centered between the feet. Snap the fist back to "
            "guard immediately. Drill it on the bag from chest-to-bag "
            "distance: dip, pivot, drive, return. If you find yourself "
            "leaning forward onto your front foot after the punch, shorten "
            "the dip and check your balance before adding power."
        ),
        "key_points": [
            "The rear uppercut is a close-range bomb: dip, rear-foot pivot, hip rotation, rising fist - one chain.",
            "Bend the knees, never the waist; waist-bending puts the head directly into the counter lane.",
            "The arc stays tight to the body and finishes at the target, never swung wide or looped.",
            "Balance at impact decides everything: you must be able to throw the next punch instantly.",
            "The classic use is inside fighting and against opponents who lean in - it meets them on their way down.",
        ],
        "requirements": [
            "Knee dip with eyes up; rear-foot pivot and hip rotation; tight rising arc.",
            "Lead glove on chin; torso compact; weight centered at impact.",
            "Immediate return to guard; no forward lean past balance.",
        ],
        "standards": [
            "USA Boxing Rulebook: rear uppercuts as scoring blows.",
            "Association of Boxing Commissions Unified Rules: legal scoring areas.",
        ],
        "citations": [CIT_USAB, CIT_ABC, CIT_DEMPSEY],
        "sig_lens": (
            "The Signature reading of the rear uppercut: the volcano of the "
            "covenant. It sleeps in the stance, coiled in the knees, and "
            "erupts only at close range when the oath demands it. The "
            "Signature boxer does not reach for the rear uppercut - he "
            "lets the opponent come to the mountain, then lets the mountain "
            "rise. Power without balance is noise; the Signature uppercut "
            "is power that can stand afterward."
        ),
    },
    {
        "key": "range_distance",
        "name": "Range and Distance Management",
        "group": "Stance and Footwork",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Range and distance management is the science of where you "
            "stand: knowing exactly how far your punches reach, how far the "
            "opponent's reach, and living in the space that favors you. "
            "Boxing has three ranges - long (jab range), medium (hook and "
            "cross range), and inside (uppercut and short-hook range) - and "
            "the master boxer chooses which range the fight happens in. "
            "Distance is controlled with the jab as a measuring stick and "
            "with footwork as the steering wheel: step in to attack, step "
            "out to rest, pivot to change the geometry. Fighters who manage "
            "distance well rarely get hit clean; fighters who do not are "
            "always exactly where the opponent wants them."
        ),
        "how_it_works": (
            "Find your jab range first: from stance, extend the jab - where "
            "it lands flush is your long range. Memorize that distance "
            "against every opponent by touching them with the jab early; "
            "the jab is your tape measure. To control distance, use the "
            "step-drag: small step in behind the jab to enter, small step "
            "back to exit - never lunge in and never run out. When the "
            "opponent advances, meet him with the jab or pivot off the "
            "lead foot so his advance carries him past you. When you want "
            "inside, slip or parry his jab and step in behind your own. "
            "Drill the three ranges on the bag: jab range (only jabs "
            "land), medium (add crosses and hooks), inside (uppercuts and "
            "short hooks) - and practice shifting between them with "
            "footwork alone, no punching, so the feet learn the geography."
        ),
        "key_points": [
            "Three ranges - long, medium, inside - and the boxer who chooses the range usually wins the fight.",
            "The jab is the tape measure: it finds and holds your exact punching distance against every opponent.",
            "Enter behind the jab, exit with a step - lunging in and running out are both punishable.",
            "Pivots change range geometry without retreating: let the opponent advance past you.",
            "Longer reach favors long range; shorter arms favor inside - know your build and fight your fight.",
        ],
        "requirements": [
            "Ability to identify and hold all three ranges by feel, using the jab as measure.",
            "Controlled entry and exit with the step-drag; no lunging or fleeing.",
            "Pivots usable to change angle at range under pressure.",
        ],
        "standards": [
            "USA Boxing Coaching Manual: distance management in tactical development.",
            "IBA Technical and Competition Rules: legal fighting area dimensions.",
        ],
        "citations": [CIT_USAB, CIT_COACH, CIT_IBA],
        "sig_lens": (
            "The Signature reading of distance: the geography of the oath. "
            "The Signature boxer treats the canvas as a map he has already "
            "surveyed - every inch measured by his jab, every angle known "
            "by his pivots. He does not chase opponents and he does not "
            "flee them; he invites them into his range and denies them "
            "theirs. In the Signature system, distance is not empty space - "
            "it is territory, and territory is defended."
        ),
    },
    {
        "key": "breathing",
        "name": "Breathing for Boxing",
        "group": "Stance and Footwork",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Breathing for boxing is the skill of staying oxygenated and "
            "relaxed under fire: sharp exhales on every punch, steady "
            "rhythm between exchanges, and no breath-holding ever. The "
            "rule is simple - breathe out when you punch, breathe in when "
            "you do not. The exhale is short and sharp through the teeth "
            "(the familiar 'tss' sound), which tightens the core exactly "
            "at the moment of impact and keeps the boxer from gassing. "
            "Holding the breath while punching or bracing spikes tension, "
            "burns energy, and invites exhaustion; relaxed breathing keeps "
            "the shoulders loose, the punches fast, and the mind clear "
            "into the championship rounds."
        ),
        "how_it_works": (
            "Practice the exhale first without punching: stand in stance "
            "and hiss a short 'tss' through your teeth while snapping your "
            "core tight for a split second, then relax and inhale through "
            "the nose. Now add the jab: exhale sharply as the punch "
            "extends, inhale as it returns. Every punch gets its own "
            "exhale - jab-cross is 'tss-tss', never one long held breath. "
            "Between exchanges, settle into a rhythm: in through the nose, "
            "out through the mouth, shoulders down, jaw relaxed. When "
            "taking a body shot, the exhale must already be happening - a "
            "punch landing on a held breath or an inhaled belly does double "
            "damage. Drill three rounds on the bag with the only goal being "
            "perfect breathing: exhale on every punch, never hold, never "
            "gasp. If your shoulders creep up to your ears, you have "
            "stopped breathing - reset."
        ),
        "key_points": [
            "Exhale on every punch, inhale between: the punch and the breath are one technique.",
            "The sharp exhale tightens the core at impact - it is armor and engine in one.",
            "Never hold the breath: holding spikes tension, slows punches, and empties the tank.",
            "Breathe out when receiving body punches - an exhaling core absorbs; a full belly folds.",
            "Relaxed shoulders are the signal: if they rise, breathing has broken down - reset immediately.",
        ],
        "requirements": [
            "Audible sharp exhale synchronized with every punch thrown.",
            "Steady nasal breathing rhythm between exchanges; shoulders down.",
            "No breath-holding during combinations or under pressure (verifiable on the bag).",
        ],
        "standards": [
            "USA Boxing Coaching Manual: breathing mechanics in conditioning modules.",
        ],
        "citations": [CIT_USAB, CIT_COACH],
        "sig_lens": (
            "The Signature reading of breathing: the bellows of the covenant. "
            "The Signature boxer breathes the way the tide moves - out with "
            "the strike, in with the patience, never held, never wasted. "
            "Each exhale is a small oath sworn at the moment of impact; "
            "each inhale the gathering of the next promise. The fighter who "
            "masters his breath masters his fear, and the Signature system "
            "has no room for fear that has not been breathed through."
        ),
    },
    {
        "key": "slip",
        "name": "The Slip",
        "group": "Defense",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The slip is the signature head movement of boxing defense: a "
            "quick rotation of the torso that moves the head just inches "
            "off the center line so a straight punch misses by a whisper. "
            "Slipping inside means rotating toward the opponent's punch "
            "side; slipping outside means rotating away. The beauty of the "
            "slip is economy - the head moves only as far as it must, the "
            "feet stay planted, the guard stays up, and the boxer is "
            "instantly in position to counter. A well-timed slip turns the "
            "opponent's best punch into your best opening: his punch "
            "extends past your head while your counter is already on its "
            "way. It is the first head-movement defense every boxer learns "
            "and the one professionals still use most."
        ),
        "how_it_works": (
            "From stance and guard, as the opponent's straight punch "
            "comes, rotate your torso sharply at the waist - not a lean, "
            "a rotation - so your head moves about six inches off the "
            "center line. To slip outside a jab, rotate your torso so your "
            "head moves to your right (away from his lead hand); to slip "
            "inside, rotate the other way. The knees bend slightly with "
            "the rotation, the guard stays glued to the chin, and the eyes "
            "stay on the opponent - never close them, never look away. The "
            "head moves the minimum distance: if you can feel the punch "
            "brush past your ear, the slip was perfect. The moment the "
            "punch passes, you are loaded to counter - the classic is the "
            "slip-and-rip: slip the jab, fire the cross or hook to the "
            "body as his arm extends. Drill with a partner throwing slow "
            "jabs: slip, freeze, check that your head moved and your feet "
            "did not, then add the counter."
        ),
        "key_points": [
            "The slip is torso rotation, not leaning: rotate at the waist, move the head inches, keep the feet planted.",
            "Minimum movement is maximum defense: a head that moves six inches is as safe as one that moves two feet, and far better positioned to counter.",
            "Guard stays up and eyes stay open through the slip - the defense fails if you flinch or look away.",
            "Slipping outside is generally safer (away from the rear hand); slipping inside sets up bigger counters with bigger risk.",
            "Every slip should end loaded: the punch that missed you is the opening your counter was built for.",
        ],
        "requirements": [
            "Head displacement of roughly six inches via torso rotation; feet stationary.",
            "Guard maintained and eyes on opponent throughout the movement.",
            "Ability to slip both inside and outside a straight punch and fire an immediate counter.",
        ],
        "standards": [
            "USA Boxing Coaching Manual: slipping in defensive fundamentals.",
            "Dempsey J. Championship Fighting: head movement and countering off the slip.",
        ],
        "citations": [CIT_USAB, CIT_COACH, CIT_DEMPSEY],
        "sig_lens": (
            "The Signature reading of the slip: the whisper of the covenant. "
            "The Signature boxer does not run from punches - he declines "
            "them, politely, by inches. The slip is the Signature system "
            "in miniature: minimum motion, maximum meaning, and the "
            "counter already sworn before the missed punch has finished "
            "traveling. To slip is to let the opponent spend his oath "
            "while you keep yours."
        ),
    },
    {
        "key": "bob",
        "name": "The Bob (Duck)",
        "group": "Defense",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The bob - also called the duck - is the vertical head movement "
            "of boxing defense: a quick bend of the knees that drops the "
            "whole fighting posture straight down so hooks and wide punches "
            "sail over the head. Unlike the slip, which moves the head "
            "sideways off straight punches, the bob moves it down under "
            "curved punches. The keys are bending at the knees rather than "
            "folding at the waist, keeping the eyes up on the opponent, and "
            "coming straight back up into stance ready to punch. A deep, "
            "well-timed bob under a hook is one of the most crowd-pleasing "
            "moves in boxing - and it sets up devastating rising counters "
            "like the uppercut."
        ),
        "how_it_works": (
            "From stance, as the hook comes, bend both knees quickly and "
            "drop your level straight down about eight to ten inches - "
            "imagine sitting into a short, fast squat. Keep your back "
            "straight, your guard up around your chin, and your eyes locked "
            "on the opponent; never bend forward at the waist, which puts "
            "your head on a platter for the uppercut. Your head should end "
            "up just below the path of the punch, feeling it pass overhead. "
            "Then drive straight back up off your legs into your stance - "
            "the upward drive can carry your counter uppercut or hook with "
            "it. Drill: partner throws slow hooks, you bob under and come "
            "up with a counter. The two most common faults are bending at "
            "the waist (fix: chest up, sit the hips down) and staying down "
            "too long (fix: down and up is one beat, like a bounce)."
        ),
        "key_points": [
            "The bob is a knee bend, not a waist fold: sit down with a straight back, eyes always on the opponent.",
            "It defeats hooks and wide punches by dropping the head under their arc - straight punches need the slip instead.",
            "Drop only as far as the punch requires: excessive depth wastes time and invites the uppercut.",
            "The rise is part of the technique: drive up off the legs and the counter rides the same motion.",
            "Guard stays tight around the chin through the whole dip - the head is low but never unguarded.",
        ],
        "requirements": [
            "Level drop of eight to ten inches via knee bend; back straight; eyes up.",
            "Guard maintained around the chin throughout the dip and rise.",
            "Immediate return to stance with an available counter (uppercut or hook).",
        ],
        "standards": [
            "USA Boxing Coaching Manual: bobbing in defensive fundamentals.",
        ],
        "citations": [CIT_USAB, CIT_COACH, CIT_DEMPSEY],
        "sig_lens": (
            "The Signature reading of the bob: the bow of the covenant. "
            "The Signature boxer dips beneath the storm rather than "
            "standing in it - not retreat, but reverence for the craft. "
            "The knees bend, the guard holds, the eyes never leave the "
            "opponent, and the rise carries the answer. In the Signature "
            "system, going low is never going away; it is gathering the "
            "ground to give back."
        ),
    },
    {
        "key": "parry",
        "name": "The Parry",
        "group": "Defense",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The parry is the deflection defense: a short, sharp slap of "
            "the glove that redirects an incoming straight punch just off "
            "its line so it misses. Unlike the block, which absorbs, the "
            "parry redirects - a small movement of your glove produces a "
            "large miss at the target. The lead hand parries the jab with "
            "a quick outward tap; the rear hand parries the cross. "
            "Parrying is economical and sets up instant counters, because "
            "the deflecting hand is already in motion toward the opening. "
            "The danger is over-parrying: a big sweeping slap opens your "
            "own guard and can be timed. The parry must be a tap, not a "
            "swing."
        ),
        "how_it_works": (
            "As the opponent's jab extends toward you, meet it with a "
            "short outward slap of your lead glove - a quick tap to your "
            "right (against an orthodox jab), moving his fist just two or "
            "three inches off line. The motion comes from the shoulder and "
            "elbow in a compact pop; the glove travels only a few inches. "
            "Your rear glove never leaves your chin. Against the cross, "
            "use the rear glove to tap it slightly outward or catch it on "
            "the palm. The instant the punch is redirected, fire back - "
            "the classic is parry the jab, return your own jab or cross "
            "down the same channel his punch just vacated. Drill with a "
            "partner: slow jabs, tap them aside, counter immediately. If "
            "your parrying hand travels more than a few inches, shorten "
            "it; a parry is a period at the end of a sentence, not a new "
            "paragraph."
        ),
        "key_points": [
            "The parry redirects rather than absorbs: a two-inch deflection at your glove is a two-foot miss at your head.",
            "Keep it a tap, not a swing - big parries open your guard and get timed.",
            "The non-parrying hand stays home: parry with one, guard with the other, always.",
            "Parrying creates the counter lane: his punch vacates the channel your return punch travels.",
            "Lead hand parries the jab, rear hand parries the cross - match the tool to the threat.",
        ],
        "requirements": [
            "Compact glove deflection of a few inches; punch redirected off the center line.",
            "Non-parrying glove on the chin throughout; eyes on opponent.",
            "Immediate counter available down the vacated channel.",
        ],
        "standards": [
            "USA Boxing Coaching Manual: parrying in defensive fundamentals.",
            "Dempsey J. Championship Fighting: deflection and counter-punching.",
        ],
        "citations": [CIT_USAB, CIT_COACH, CIT_DEMPSEY],
        "sig_lens": (
            "The Signature reading of the parry: the redirection of the "
            "oath. The Signature boxer does not meet force with force - he "
            "meets it with geometry, turning the opponent's sworn punch "
            "aside with a touch. The parry is the Signature system at its "
            "most elegant: his power becomes your opening, his commitment "
            "your counter, all for the price of a tap."
        ),
    },
    {
        "key": "glove_block",
        "name": "The Glove Block",
        "group": "Defense",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The glove block - also called catching - is the absorption "
            "defense: meeting an incoming punch on the gloves, forearms, "
            "and elbows so its force dies on your guard instead of your "
            "head or body. The high guard becomes a shell: gloves catch "
            "straight punches, forearms catch hooks, elbows tucked to the "
            "ribs catch body shots. Blocking is the simplest defense and "
            "the foundation of infighting - when punches come too fast to "
            "slip or parry, you shell up and let the guard do the work. "
            "The cost is that blocked punches still score with judges and "
            "still jar you, so the block is a shield for emergencies and "
            "exchanges, not a permanent address."
        ),
        "how_it_works": (
            "Tighten the high guard: gloves at the cheekbones, forearms "
            "vertical and close together in front of the face, elbows "
            "pinned to the ribs. Against straight punches, catch them on "
            "the palms and gloves with a slight backward give - meet the "
            "punch and ride it back an inch to bleed off force, like "
            "catching a baseball by giving with it. Against hooks, turn "
            "the forearm into the punch so it lands on bone and glove, "
            "never on the side of the head. Against body punches, drop the "
            "elbows to meet them on the arms, and exhale sharply. Keep the "
            "eyes open and watch through the guard so you can fire back "
            "between his punches. Drill on the bag or with a partner: "
            "shell up, take three punches on the guard, fire back two. The "
            "fault to avoid is shelling up and freezing - the block buys "
            "you a moment, and the moment must be spent punching back."
        ),
        "key_points": [
            "The block absorbs: gloves catch straights, forearms catch hooks, elbows catch body shots.",
            "Give with the catch - a slight backward ride bleeds off force like a baseball mitt.",
            "Eyes stay open behind the shell: a blind block cannot find the counter opening.",
            "Blocked punches still score and still shake you - the block is a shield, not a strategy.",
            "The block buys one moment; spend it punching back, not hiding.",
        ],
        "requirements": [
            "Tight high guard shell: gloves at cheekbones, forearms vertical, elbows to ribs.",
            "Catching with give on straights; forearm presentation on hooks; elbow drop on body shots.",
            "Immediate return fire between the opponent's punches; no freezing in the shell.",
        ],
        "standards": [
            "USA Boxing Coaching Manual: blocking in defensive fundamentals.",
            "Association of Boxing Commissions Unified Rules: blocked punches and scoring criteria.",
        ],
        "citations": [CIT_USAB, CIT_COACH, CIT_ABC],
        "sig_lens": (
            "The Signature reading of the block: the fortress of the "
            "covenant. When the storm is too fast to slip and too wide to "
            "parry, the Signature boxer raises the walls of the temple - "
            "glove, forearm, elbow, oath. The block is patience under "
            "fire: absorb, watch, wait, and answer. The Signature system "
            "teaches that even a fortress is built to sally forth from."
        ),
    },
    {
        "key": "weave",
        "name": "The Weave",
        "group": "Defense",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The weave is flowing head movement: a continuous side-to-side "
            "motion of the head and torso - often described as drawing a "
            "letter U or a figure-eight in the air - that makes the head a "
            "moving target no straight punch can time. Where the slip is a "
            "single precise rotation and the bob is a single dip, the weave "
            "is rhythm: the head glides left, dips under, rises right, in "
            "one unbroken wave. It is the defense of pressure fighters who "
            "walk forward behind moving heads, and it pairs naturally with "
            "the bob - bob and weave is one of boxing's classic phrases "
            "because the two blend into a single flowing defense. The "
            "weave demands conditioning and timing; done lazily it walks "
            "the head into punches instead of away from them."
        ),
        "how_it_works": (
            "From stance, start a slow side-to-side sway of the head and "
            "torso: rotate the waist so the head glides a few inches left, "
            "dip the knees slightly through the middle, and let the head "
            "rise a few inches right - a smooth U-shaped path. The guard "
            "stays up, the eyes stay on the opponent, and the feet keep "
            "their stance; only the upper body flows. Speed it up gradually "
            "until the head is a constant moving target. Now blend the bob: "
            "dip deeper at the bottom of the U so hooks pass overhead, then "
            "rise into the sway. Practice weaving forward: step-drag in "
            "while the head flows, so you advance behind a moving target. "
            "The rhythm must be yours, not a metronome - a predictable "
            "weave gets timed. Change the tempo, pause, double up on one "
            "side. Drill with a partner throwing slow one-twos: weave the "
            "jab, bob the cross, and come up punching."
        ),
        "key_points": [
            "The weave is continuous motion: a U or figure-eight path of the head that never sits still for a punch.",
            "It blends with the bob - dip under hooks at the bottom of the wave, sway off straights on the sides.",
            "Guard up, eyes open, feet in stance: only the upper body flows, the foundation never breaks.",
            "Rhythm must vary: a metronome weave gets timed and punished - change tempo and direction.",
            "The weave advances: walk forward behind the moving head and the opponent cannot set his feet to punch.",
        ],
        "requirements": [
            "Smooth continuous head path (U or figure-eight), guard up, eyes on opponent.",
            "Blended bob at the bottom of the wave; stance and foot position preserved.",
            "Variable rhythm; ability to weave forward while advancing with the step-drag.",
        ],
        "standards": [
            "USA Boxing Coaching Manual: bob-and-weave in defensive development.",
        ],
        "citations": [CIT_USAB, CIT_COACH, CIT_DEMPSEY],
        "sig_lens": (
            "The Signature reading of the weave: the river of the covenant. "
            "The Signature boxer does not stand as a rock for punches to "
            "break upon - he flows as a river they cannot strike. The weave "
            "is the Signature system in motion: never still, never "
            "predictable, always arriving. Where the slip declines one "
            "punch, the weave declines the very idea of a stationary "
            "target."
        ),
    },
    {
        "key": "one_two",
        "name": "The One-Two (Jab-Cross Combination)",
        "group": "Combinations",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The one-two is the foundational combination of boxing: jab "
            "followed instantly by the cross. The jab opens the guard, "
            "measures the range, and occupies the opponent's defense; the "
            "cross follows down the same channel with full rotational "
            "power before the guard can reset. It is the first combination "
            "every boxer learns and the most thrown combination in the "
            "sport, because it is fast, safe, and effective at every level "
            "from first amateur bout to world title fight. The entire "
            "technique lives or dies on the connection between the punches: "
            "the cross must launch as the jab returns, so the two punches "
            "flow as one motion, not two separate events."
        ),
        "how_it_works": (
            "From guard, throw the jab with a small step - and as the jab "
            "hand starts its snap-back, launch the cross: pivot the rear "
            "foot, rotate the hips and shoulders, and drive the rear fist "
            "down the center line the jab just traveled. The jab returns "
            "to the chin as the cross extends; the cross returns as the "
            "stance settles. The rhythm is 'pop-POP' - the jab a quick "
            "setup beat, the cross the heavy beat landing a fraction of a "
            "second later. Breathe 'tss-tss', one exhale per punch. Keep "
            "the head off the center line slightly as the cross goes, in "
            "case of the return fire. Drill on the bag: jab-cross, "
            "jab-cross, listening for two distinct cracks close together. "
            "The classic fault is pausing between the punches - fix it by "
            "starting the cross before the jab has fully returned; the "
            "punches should overlap like links in a chain."
        ),
        "key_points": [
            "The jab is the key that opens the lock; the cross is what walks through the door.",
            "The cross launches as the jab returns - the combination is one motion, not two punches.",
            "Rhythm is pop-POP: quick setup beat, heavy beat a fraction of a second later.",
            "One exhale per punch, guard discipline throughout: the jab hand returns home as the cross fires.",
            "The one-two works at every level because it is the fastest way to deliver a power punch safely.",
        ],
        "requirements": [
            "Jab and cross thrown in immediate succession with overlapping motion (no pause between).",
            "Full cross mechanics (pivot, rotation, return) preserved inside the combination.",
            "Guard and balance intact after the combination; ready to throw again or defend.",
        ],
        "standards": [
            "USA Boxing Coaching Manual: the one-two as the first combination taught.",
            "Association of Boxing Commissions Unified Rules: combinations as scoring blows.",
        ],
        "citations": [CIT_USAB, CIT_COACH, CIT_ABC, CIT_DEMPSEY],
        "sig_lens": (
            "The Signature reading of the one-two: the question and the "
            "answer. The jab asks, the cross answers - the Signature "
            "system's first complete sentence. Thrown as one motion, the "
            "combination is a covenant in two beats: the setup sworn and "
            "the power delivered before the oath can be broken. Every "
            "longer combination in this database is the one-two grown up."
        ),
    },
    {
        "key": "double_jab",
        "name": "The Double Jab",
        "group": "Combinations",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The double jab is two jabs thrown in immediate succession: "
            "the first to occupy the guard and freeze the opponent, the "
            "second - often stepped with - to land harder, score, or open "
            "the way for a power punch. The first jab is a feeler, thrown "
            "at half commitment; the second is the real one, driven by a "
            "step and full shoulder turn. The double jab is the great "
            "range-closer: the first jab covers the advance, the second "
            "lands as you arrive. It also doubles as a defensive tool - "
            "two fast jabs in the face stop most opponents from starting "
            "their own offense."
        ),
        "how_it_works": (
            "From guard, flick the first jab out at about seventy percent - "
            "quick, light, aimed at the guard or forehead to occupy his "
            "vision and defense. As it snaps back, step in with the "
            "step-drag and fire the second jab with full commitment: "
            "shoulder turned in, weight behind it, aimed at the chin. The "
            "rhythm is 'tap-POP', and the two punches should land less "
            "than half a second apart. Both hands return to guard along "
            "their paths; the rear glove never moves. Breathe 'tss-tss'. "
            "Common uses: double jab then cross (the classic 1-1-2), "
            "double jab to close distance, double jab to stop an advance. "
            "Drill: on the bag, tap-POP, tap-POP - the first punch a "
            "knock on the door, the second the door coming off its hinges."
        ),
        "key_points": [
            "First jab occupies, second jab lands: feeler then weapon, tap then POP.",
            "The step between the jabs closes distance safely - the advance hides behind the first punch.",
            "Both jabs return fully to guard; the rear hand never leaves the chin.",
            "The double jab sets up everything: 1-1-2, 1-1-3, or a step inside to hooks.",
            "It is also defense: two jabs in the face freeze most opponents mid-thought.",
        ],
        "requirements": [
            "Two jabs within half a second; first at partial commitment, second full with a step.",
            "Full jab mechanics on both; guard intact; no dropping the rear hand.",
            "Usable to set up a following power punch or to halt an advance.",
        ],
        "standards": [
            "USA Boxing Coaching Manual: double jab in combination development.",
        ],
        "citations": [CIT_USAB, CIT_COACH, CIT_DEMPSEY],
        "sig_lens": (
            "The Signature reading of the double jab: the knock and the "
            "entry. The first jab knocks on the temple door of the "
            "opponent's guard; the second walks through it. In the "
            "Signature system the double jab is patience weaponized - the "
            "discipline to throw a punch you do not expect to land, so "
            "that the one you mean finds its home."
        ),
    },
    {
        "key": "jab_body",
        "name": "The Jab to the Body",
        "group": "Combinations",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The jab to the body is the level-changing jab: the same fast "
            "lead-hand punch, but dipped at the knees to strike the solar "
            "plexus or ribs instead of the head. It is one of the great "
            "guard-manipulators in boxing - when the jab goes to the body, "
            "the opponent's guard drops to meet it, and the head opens for "
            "what follows. It also scores, slows opponents, and punishes "
            "fighters who lean on a high guard. The technique demands a "
            "knee dip rather than a waist bend: bend at the waist and the "
            "head drops into the counter lane; dip at the knees and the "
            "head stays safe behind the shoulder."
        ),
        "how_it_works": (
            "From guard, dip the knees two to three inches - a quick "
            "level change, back straight, eyes up - and extend the jab "
            "downward to the body target, rotating the fist over as usual. "
            "The rear glove stays on the chin; the chin stays tucked "
            "behind the lead shoulder. Snap the hand back up to guard "
            "immediately along the same path - the return is critical "
            "because you are briefly lower and closer. The classic "
            "sequence is jab to the body, then jab or cross to the head "
            "as the guard drops: down then up, the guard cannot be in two "
            "places. Drill on the bag: head jab, body jab, head jab - "
            "changing levels with the knees, never the waist. If your head "
            "moves forward and down when you throw it, the dip is wrong; "
            "the head should stay on the same vertical line, only lower."
        ),
        "key_points": [
            "Level change comes from the knees, never the waist - the head must stay out of the counter lane.",
            "The body jab drops the guard: what goes down to meet it cannot also protect the chin.",
            "Snap back up to guard instantly; the low position is a moment, not a residence.",
            "Down-then-up is the classic: body jab opens the head for the punch that follows.",
            "It scores, it slows, it manipulates - the most versatile single punch in the book.",
        ],
        "requirements": [
            "Knee-dip level change of two to three inches; back straight; eyes up.",
            "Full jab mechanics to the body target; rear glove on chin; instant return to guard.",
            "Usable in down-then-up sequences (body jab setting up head punches).",
        ],
        "standards": [
            "USA Boxing Rulebook: body punches to legal target areas.",
            "Association of Boxing Commissions Unified Rules: legal body targets.",
        ],
        "citations": [CIT_USAB, CIT_ABC, CIT_COACH],
        "sig_lens": (
            "The Signature reading of the body jab: the low oath. The "
            "Signature boxer knows that guards are built for the head and "
            "pride lives in the chin - so the Signature jab goes beneath "
            "both, to the honest work of the body. It is the humble punch "
            "that makes the proud punches possible, dropping the walls so "
            "the covenant can be kept upstairs."
        ),
    },
    {
        "key": "one_two_three",
        "name": "The One-Two-Three (Jab-Cross-Hook)",
        "group": "Combinations",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The one-two-three is the classic three-punch combination: jab, "
            "cross, lead hook. The jab opens and measures, the cross drives "
            "through the middle with power, and the lead hook finishes "
            "around the side where the guard has been pushed open by the "
            "first two punches. It is the combination that teaches the "
            "boxer to mix straight punches and curved punches, head targets "
            "in sequence, and full-body rotation in both directions. "
            "Thrown correctly it is a flowing wave - pop-POP-SWING - that "
            "is very difficult to defend because each punch attacks a "
            "different line while the defense is still reacting to the "
            "last one."
        ),
        "how_it_works": (
            "Throw the one-two: jab with a step, cross down the center as "
            "the jab returns. As the cross snaps back, pivot the lead foot "
            "and whip the lead hook around in a tight arc - the torso "
            "rotation reverses direction, which is the athletic heart of "
            "the combination. The rhythm is pop-POP-SWING across about one "
            "second. Each punch returns toward guard as the next launches; "
            "the chain overlaps. The head stays off center and the rear "
            "glove guards the chin during the hook. Breathe 'tss-tss-tss'. "
            "A classic variation goes to the body with the hook: jab, "
            "cross, shovel the hook to the ribs as the guard stays high. "
            "Drill on the bag until the three cracks run together like a "
            "drum roll. The fault to watch is the hook getting wide and "
            "loopy after the straight punches - keep the arc inside your "
            "shoulder width no matter how fast the combination flows."
        ),
        "key_points": [
            "Three lines, three beats: straight opener, straight power, curved finisher - each attacks where the last one moved the guard.",
            "The torso reverses rotation between the cross and the hook; that reversal is the engine of the combination.",
            "Punches overlap like chain links: each returns as the next launches - no pauses, no resets.",
            "The hook stays tight even at speed; a wide third punch ruins the combination and invites the counter.",
            "Vary the target: head-head-body and head-body-head versions keep the defense guessing.",
        ],
        "requirements": [
            "Jab-cross-hook in continuous flow, about one second total, with overlapping returns.",
            "Full mechanics on all three punches; tight hook arc; guard discipline throughout.",
            "Balance and stance intact after the combination; at least one body-target variation.",
        ],
        "standards": [
            "USA Boxing Coaching Manual: three-punch combinations in combination development.",
            "Association of Boxing Commissions Unified Rules: combinations as scoring blows.",
        ],
        "citations": [CIT_USAB, CIT_COACH, CIT_ABC, CIT_DEMPSEY],
        "sig_lens": (
            "The Signature reading of the one-two-three: the complete "
            "sentence of the covenant. Question, answer, verdict - the "
            "Signature combination in three beats. The jab swears the "
            "range, the cross swears the power, the hook delivers the "
            "judgment around the side. In the Signature system, a "
            "three-punch combination is not three punches; it is one "
            "promise kept three ways."
        ),
    },
    {
        "key": "hook_off_jab",
        "name": "The Hook off the Jab",
        "group": "Combinations",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The hook off the jab is the two-punch combination where the "
            "lead hand throws twice in a row: jab, then lead hook, with "
            "no cross between. It is faster than the one-two-three and "
            "catches opponents leaning away from the expected cross - the "
            "jab occupies the center, and the hook arrives around the side "
            "while the defense is still set for the straight punch that "
            "never comes. The technique demands a quick role-change of the "
            "lead hand: from straight piston to curved arc in a fraction "
            "of a second, with the elbow rising as the jab returns. It is "
            "a favorite of pressure fighters working at medium range."
        ),
        "how_it_works": (
            "Throw the jab - and instead of bringing it all the way home, "
            "let the returning hand transform: as the fist comes back, the "
            "lead elbow rises to shoulder height and the hand whips into "
            "the tight hook arc, pivoting the lead foot. The rhythm is "
            "pop-SWING, two beats very close together. The rear glove "
            "never leaves the chin. The trick is the elbow: it must rise "
            "during the jab's return, not after - if you return fully to "
            "guard and then start the hook, the combination is too slow. "
            "Think of the lead arm as a piston that becomes a hinge "
            "mid-stroke. Drill: jab-hook, jab-hook on the bag, feeling the "
            "elbow lift as the jab comes back. A sharp variation dips the "
            "hook to the body - jab up, hook to the ribs - which is "
            "devastating when the guard stays high for the second head "
            "punch that never comes."
        ),
        "key_points": [
            "One hand, two punches: the lead arm transforms from piston to hinge mid-return.",
            "The elbow rises during the jab's return - waiting until guard means the combination is too slow.",
            "It punishes the expected cross: the defense sets for straight, the hook comes around the side.",
            "Pop-SWING rhythm, very tight together; the rear glove guards throughout.",
            "The body variation (jab up, hook to ribs) exploits the high guard the jab creates.",
        ],
        "requirements": [
            "Jab-to-hook with no full return between; elbow rising during the jab's return.",
            "Tight hook arc with lead-foot pivot; rear glove on chin throughout.",
            "Continuous pop-SWING rhythm; body-target variation available.",
        ],
        "standards": [
            "USA Boxing Coaching Manual: lead-hand combinations.",
        ],
        "citations": [CIT_USAB, CIT_COACH, CIT_DEMPSEY],
        "sig_lens": (
            "The Signature reading of the hook off the jab: the change of "
            "mind. The Signature boxer shows the straight road, then takes "
            "the curved one - the same hand, a different oath, sworn "
            "before the first is finished. It teaches the Signature "
            "fighter that a punch is not a commitment until it lands; "
            "until then, it is a promise that can be rewritten mid-flight."
        ),
    },
    {
        "key": "counter_jab",
        "name": "Countering the Jab",
        "group": "Counter-Punching",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Countering the jab is the entry skill of counter-punching: "
            "making the opponent pay for throwing the most common punch in "
            "boxing. Because the jab is thrown so often, the boxer who can "
            "punish it owns the fight's rhythm. The fundamental counters "
            "are: slip outside the jab and fire the cross; parry the jab "
            "and fire your own jab or cross down the open channel; or beat "
            "him to the punch with a jab of your own timed to land first. "
            "Each exploits the same truth - when his jab extends, his lead "
            "side opens and his weight commits forward. Countering the jab "
            "turns defense into offense in a single beat and discourages "
            "the opponent from jabbing at all, which blinds him."
        ),
        "how_it_works": (
            "Pick one counter and drill it until it is reflex. The slip "
            "counter: as his jab comes, slip outside (head to your right), "
            "and fire the cross straight down the channel his jab vacated - "
            "his extended arm cannot block it. The parry counter: tap his "
            "jab slightly outward with your lead glove and snap your cross "
            "or jab right behind it, beating his return. The timing "
            "counter: as you see his shoulder twitch to jab, throw your own "
            "jab a hair earlier - the faster, straighter punch wins, and "
            "his jab dies unborn. In all three, the eyes stay open, the "
            "non-punching hand guards, and you return to stance instantly. "
            "Drill with a partner throwing steady jabs: slip-cross, "
            "parry-cross, beat-the-jab, rotating through all three. The "
            "rule: the counter must launch while his punch is still "
            "extended - a late counter is just a trade."
        ),
        "key_points": [
            "The jab is the most-thrown punch, so its counter is the highest-value counter in boxing.",
            "Three fundamental answers: slip-and-cross, parry-and-return, beat-him-to-it - master all three.",
            "The extended jab opens the channel: his arm cannot block the punch traveling down the lane it vacated.",
            "Timing beats speed: the counter must launch while his punch is still out - late is just trading.",
            "A jab that gets punished stops getting thrown - and a boxer who cannot jab is half-blind.",
        ],
        "requirements": [
            "At least three distinct jab counters executable on a live jab (slip, parry, timing).",
            "Counter launched during the opponent's extension; guard and eyes maintained.",
            "Immediate return to stance; no reaching or lunging for the counter.",
        ],
        "standards": [
            "USA Boxing Coaching Manual: counter-punching fundamentals.",
            "Dempsey J. Championship Fighting: countering off defensive moves.",
        ],
        "citations": [CIT_USAB, CIT_COACH, CIT_DEMPSEY],
        "sig_lens": (
            "The Signature reading of the jab counter: the turned oath. "
            "The opponent swears his jab; the Signature boxer lets him "
            "swear it - and answers with a heavier vow down the same "
            "channel. In the Signature system, every punch thrown at you "
            "is a door left open; countering the jab is learning to walk "
            "through the most common door in the sport."
        ),
    },
    {
        "key": "catch_counter",
        "name": "The Catch and Counter",
        "group": "Counter-Punching",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The catch and counter is the block that bites back: catching "
            "the opponent's punch on the glove or forearm and firing the "
            "return punch in the same motion, off the catch. It is the "
            "highest-percentage counter in boxing because it works against "
            "almost any punch and requires only a tight guard and good "
            "timing - no head movement, no risk of misjudging distance. "
            "The classic is catching the jab on the rear glove and firing "
            "the cross over the top, or catching the cross and answering "
            "with the hook. The catch absorbs just enough to create the "
            "opening; the counter must be immediate, because the window "
            "the caught punch opens closes the instant the opponent "
            "recovers his guard."
        ),
        "how_it_works": (
            "As his punch arrives, meet it on the glove with a slight "
            "backward give - catch the jab on the rear glove, the cross on "
            "the lead glove or forearm. The moment of the catch is the "
            "trigger: fire the counter off the catch without resetting. "
            "Catch the jab, throw the cross over his extended arm. Catch "
            "the cross, whip the lead hook around his open side. The "
            "rhythm is catch-HIT, two beats with no pause between - the "
            "counter should feel like the second half of the catch, not a "
            "separate punch. Keep the eyes open through the catch so the "
            "target is acquired, and exhale on the counter. Drill with a "
            "partner: he throws single punches, you catch and answer, "
            "gradually increasing speed. The fault is catching and then "
            "thinking - the counter must be wired to the catch like a "
            "reflex, because the opening lasts only as long as his punch "
            "is extended."
        ),
        "key_points": [
            "The catch is the trigger: counter off the catch with no reset, no thought, no pause.",
            "Catch-HIT rhythm - the counter is the second half of the catch, not a separate event.",
            "Works against nearly any punch with only a tight guard required: the highest-percentage counter.",
            "Eyes open through the catch: you cannot hit a target you stopped watching.",
            "The window is the extension: his punch extended is his guard open - answer before it closes.",
        ],
        "requirements": [
            "Clean catch on glove/forearm with give; counter fired immediately off the catch.",
            "Correct counter selection per caught punch (cross over the jab, hook around the cross).",
            "Eyes open, guard otherwise intact, balance preserved through catch-HIT.",
        ],
        "standards": [
            "USA Boxing Coaching Manual: catch-and-counter in counter-punching development.",
        ],
        "citations": [CIT_USAB, CIT_COACH, CIT_DEMPSEY],
        "sig_lens": (
            "The Signature reading of the catch and counter: the answered "
            "door. The opponent knocks; the Signature boxer opens the door "
            "with one hand and answers with the other - in the same breath. "
            "It is the Signature system at its most economical: his "
            "attack becomes your attack, his commitment your opening, all "
            "in two beats with no wasted motion between."
        ),
    },
    {
        "key": "feints",
        "name": "Feints and Fakes",
        "group": "Ring Craft",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Feints and fakes are the lies that make the truth land: "
            "convincing beginnings of punches, steps, or movements that "
            "are never completed, thrown to provoke a reaction - a flinch, "
            "a guard shift, a counter - that opens the real attack. A "
            "shoulder twitch that looks like a jab draws the parry; the "
            "real cross follows into the vacated lane. A step-feint "
            "suggests an advance and draws the counter that you then "
            "counter. Feinting is the thinking man's boxing: it turns the "
            "fight into a conversation where you ask the questions. The "
            "rule of the feint is commitment to the lie - a half-hearted "
            "feint fools no one, while a feint thrown like the real punch "
            "draws the real reaction."
        ),
        "how_it_works": (
            "Build feints from real punches: throw ten real jabs, then "
            "throw the exact same shoulder twitch and hip shift but hold "
            "the punch - that is a jab feint. The opponent's guard or "
            "parry reacts; the moment it does, throw the real punch into "
            "the opening: feint the jab, throw the cross; feint the cross, "
            "throw the hook. Feint with the feet too: a sudden half-step "
            "suggests the attack and draws his counter, which you slip and "
            "answer. Feint with the eyes and head: a glance at the body "
            "drops his guard for the head shot. Layer them: feint-feint-"
            "punch keeps him guessing which lie is the truth. Drill with "
            "a partner: feint only for a round, watching what each feint "
            "draws - then spend the next round punishing exactly those "
            "reactions. Never feint without a plan for the reaction; a "
            "feint is a question, and you must already know your answer."
        ),
        "key_points": [
            "A feint is a real punch stopped halfway: it must look, feel, and start exactly like the truth.",
            "Feints provoke reactions - flinches, guard shifts, counters - and the real attack punishes the reaction.",
            "Feint with shoulders, feet, eyes, and rhythm: the whole body can lie, not just the hands.",
            "Every feint needs a planned answer: feint the jab expecting the parry, and have the cross already loaded.",
            "Layer feints - feint-feint-punch - so the opponent cannot tell which lie is the truth.",
        ],
        "requirements": [
            "Convincing feints from at least three tools (shoulder/hand, step, head/eyes).",
            "Planned punishing punch for each feint's expected reaction.",
            "Layered feint sequences; feints integrated into live combinations, not just drills.",
        ],
        "standards": [
            "USA Boxing Coaching Manual: feinting in tactical development.",
        ],
        "citations": [CIT_USAB, CIT_COACH],
        "sig_lens": (
            "The Signature reading of the feint: the unsworn oath. The "
            "Signature boxer is a master of the promise almost made - the "
            "shoulder that swears the jab and keeps its counsel, the step "
            "that threatens the advance and holds its ground. In the "
            "Signature system, the feint is proof that the fighter's "
            "greatest weapon is not the punch thrown but the punch "
            "believed."
        ),
    },
    {
        "key": "cut_off_ring",
        "name": "Cutting Off the Ring",
        "group": "Ring Craft",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Cutting off the ring is the geometry of the hunter: instead "
            "of chasing a mobile opponent around the ring, the boxer steps "
            "to cut off the escape routes, shrinking the available space "
            "until the opponent runs out of canvas. The principle is to "
            "move to where the opponent is going, not where he is - "
            "stepping laterally to block the exit while advancing, so each "
            "of his moves leaves him less room. It is the essential skill "
            "of the pressure fighter and the bane of the mover. Done "
            "right, the ring gets smaller every minute; done wrong - "
            "following in a straight line - the hunter walks into counters "
            "all night while the prey circles untouched."
        ),
        "how_it_works": (
            "When the opponent circles to your left, do not follow him - "
            "step to your right, toward the side he is moving to, cutting "
            "the chord of his circle instead of tracing its arc. Advance "
            "in small steps behind a jab, always positioning yourself "
            "between him and the center of the ring, herding him toward "
            "the ropes or a corner. Keep your feet under you - lunging "
            "steps get you countered - and keep the guard up, because a "
            "trapped opponent throws desperate punches. Work in triangles: "
            "step laterally, step in, jab; step laterally, step in, jab. "
            "When he reaches the ropes, do not rush - increase the pressure "
            "with feints and cut the last exits. Drill with a partner who "
            "only moves: your job is to have him on the ropes within a "
            "minute without ever running. If you find yourself following "
            "his exact path, stop and step to the side he is heading "
            "toward instead."
        ),
        "key_points": [
            "Move to where he is going, not where he is: cut the chord of his circle, never trace its arc.",
            "Position yourself between the opponent and ring center - herd him to the ropes, do not chase him around them.",
            "Advance behind the jab in small steps; lunging while cutting off is how hunters get countered.",
            "Shrink the ring in triangles: lateral step, step in, jab - repeat until the canvas runs out.",
            "A trapped opponent is dangerous: guard up, feint more, and finish with discipline, not desperation.",
        ],
        "requirements": [
            "Lateral cutting steps (not following) that demonstrably reduce the opponent's space.",
            "Ring-center positioning maintained while advancing behind the jab.",
            "Ability to trap a mobile partner on the ropes within a timed drill; guard intact throughout.",
        ],
        "standards": [
            "USA Boxing Coaching Manual: ring positioning in tactical development.",
            "IBA Technical and Competition Rules: legal use of the ring area.",
        ],
        "citations": [CIT_USAB, CIT_COACH, CIT_IBA],
        "sig_lens": (
            "The Signature reading of cutting off the ring: the closing "
            "covenant. The Signature boxer does not chase - chasing is "
            "want, and want is weakness. He closes, the way the tide "
            "closes on the shore: inevitable, unhurried, from all sides "
            "at once. In the Signature system the ring is a promise that "
            "shrinks, and the opponent's every step is a step toward the "
            "place the Signature fighter has already chosen."
        ),
    },
    {
        "key": "off_ropes",
        "name": "Fighting off the Ropes",
        "group": "Ring Craft",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Fighting off the ropes is the art of surviving and thriving "
            "when trapped: using the ropes as a defensive tool rather than "
            "a prison. The boxer on the ropes leans back into them to gain "
            "extra inches of evasion, rolls with punches, blocks on the "
            "guard, and - the critical part - escapes along the ropes with "
            "pivots and lateral steps instead of standing still to be "
            "punished. The rope-a-dope legend aside, the real skill is "
            "making the opponent miss and pay while you work your way out: "
            "slip, block, counter, pivot off, and reclaim the center. "
            "Every boxer ends up on the ropes; the good ones treat it as a "
            "position, not a predicament."
        ),
        "how_it_works": (
            "When your back finds the ropes, do three things at once: "
            "tighten the guard into a shell, lean your upper body slightly "
            "back into the ropes for extra evasion inches, and keep your "
            "feet active. Roll with his punches - turn the head and torso "
            "with each impact so force slides off - block what you cannot "
            "roll, and answer with short counters between his punches: the "
            "uppercut and short hook are money from the ropes. To escape, "
            "never push straight off backward into more trouble: pivot off "
            "the lead foot and step laterally along the ropes, or slip his "
            "punch and step-drag out to the side he vacated. Drill it: "
            "partner pressures you to the ropes with light punches; you "
            "shell, roll, counter twice, and pivot out. The cardinal sin is "
            "standing flat on the ropes admiring his work - the ropes are "
            "a rest stop, not a residence."
        ),
        "key_points": [
            "The ropes add evasion inches: lean back into them and punches fall short that would land in center ring.",
            "Roll with punches, block the rest, and counter between his shots - defense and offense in the same breath.",
            "Escape laterally along the ropes with pivots and side steps, never by backing straight up.",
            "Short punches rule on the ropes: uppercuts and compact hooks do the damage in tight quarters.",
            "The ropes are a position, not a predicament: visit, work, and leave on your terms.",
        ],
        "requirements": [
            "Tight shell guard with lean-back evasion; rolling with punches demonstrated.",
            "Short counters (uppercut, compact hook) fired between the opponent's punches.",
            "Lateral escape via pivot or side step along the ropes; no flat-footed trapping.",
        ],
        "standards": [
            "USA Boxing Coaching Manual: defensive positioning and escape.",
            "Association of Boxing Commissions Unified Rules: legal conduct on the ropes.",
        ],
        "citations": [CIT_USAB, CIT_COACH, CIT_ABC],
        "sig_lens": (
            "The Signature reading of fighting off the ropes: the fortress "
            "wall. The Signature boxer treats the ropes not as a trap but "
            "as the back wall of his temple - something to lean on, roll "
            "with, and launch from. Cornered, the Signature fighter is at "
            "his most honest: guard tight, counters short, escape planned. "
            "In the Signature system, even the edge of the world is a "
            "position of strength if the covenant holds."
        ),
    },
    {
        "key": "pull_counter",
        "name": "The Pull Counter",
        "group": "Counter-Punching",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The pull counter is the matador's punch: as the opponent's "
            "straight punch arrives, the boxer pulls his head and upper "
            "body back just out of range - weight shifting to the rear "
            "foot - and fires the cross over the top of the missing punch "
            "in the same motion. It is among the most spectacular and "
            "highest-skill counters in boxing, demanding perfect distance "
            "judgment: pull an inch too little and you get hit; an inch "
            "too much and the counter falls short. The pull counter "
            "punishes committed straight punches and is the classic answer "
            "to an aggressive jabber. Its risk matches its reward - "
            "mistime it against a feint and you have pulled yourself into "
            "the real punch."
        ),
        "how_it_works": (
            "Stand just at the edge of his jab range. As his straight "
            "punch extends, shift your weight to the rear foot and pull "
            "your head and shoulders back about six inches - a lean from "
            "the waist with the knees soft, not a step back. His punch "
            "should miss your chin by the width of a glove. The instant it "
            "passes, while your weight is still back, fire the cross "
            "straight over his extended arm: pivot the rear foot, rotate, "
            "extend - your head stays back, out of his return lane, as the "
            "punch travels. Then step back into stance. The whole technique "
            "is one beat: pull-HIT. Drill it slowly with a partner "
            "throwing committed jabs: pull, feel the miss, fire the cross "
            "over the top. Start at half speed until the distance judgment "
            "is automatic, because the pull counter has no margin for "
            "guessing - it is all measurement. Never pull against a "
            "feint you have not read; the pull commits your weight "
            "backward, and a wise opponent will follow a feint with the "
            "real punch into your pull."
        ),
        "key_points": [
            "The pull is a weight shift, not a step: head and shoulders withdraw inches while the feet stay.",
            "Distance judgment is everything: miss by a glove-width, counter over his extended arm.",
            "The counter fires while your weight is still back - pull-HIT is one beat, not two.",
            "Your head stays out of his return lane as you punch: the pull protects the counter too.",
            "Never pull on an unread feint: the pull commits your weight, and feints punish commitment.",
        ],
        "requirements": [
            "Clean pull of about six inches off a live straight punch; punch missing by a glove-width.",
            "Cross fired over the extended arm in the same beat; head remaining back during the counter.",
            "Immediate stance recovery; demonstrated restraint against feints.",
        ],
        "standards": [
            "USA Boxing Coaching Manual: advanced counter-punching.",
            "Dempsey J. Championship Fighting: countering straight punches.",
        ],
        "citations": [CIT_USAB, CIT_COACH, CIT_DEMPSEY],
        "sig_lens": (
            "The Signature reading of the pull counter: the matador's oath. "
            "The Signature boxer invites the bull's charge and steps aside "
            "by a whisper - not fear, but measurement. The pull is the "
            "Signature system at its most audacious: to stand in the path "
            "of the punch, decline it by inches, and answer over the top "
            "before the miss has finished. It is the covenant kept at the "
            "speed of trust."
        ),
    },
    {
        "key": "shoulder_roll",
        "name": "The Shoulder Roll (Philly Shell)",
        "group": "Defense",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The shoulder roll - the heart of the Philly Shell defense - is "
            "the art of making punches slide off: the boxer turns "
            "side-on, drops the lead shoulder, and rolls punches off the "
            "shoulder, arms, and elbows while the rear hand stays cocked "
            "for the counter. Straight punches glance off the raised lead "
            "shoulder; hooks are caught on the arms; and every blocked "
            "punch loads the devastating counter cross or uppercut. It is "
            "a master's defense - economical, taunting, and brutally "
            "effective in the right hands - but it demands elite reflexes "
            "and timing, because the shell leaves the body open to a "
            "committed body attack and punishes every misread."
        ),
        "how_it_works": (
            "From a more side-on stance than usual, drop the lead "
            "shoulder and tuck the chin behind it; the lead arm rests "
            "low across the body, elbow guarding the ribs, while the rear "
            "glove stays at the chin, cocked and ready. As his jab comes, "
            "roll the lead shoulder up and inward so the punch glances off "
            "the shoulder muscle - a small rotation, not a big motion. "
            "Catch his hooks on the lead forearm and elbow. The moment a "
            "punch rolls off, fire back: the classic is the roll into the "
            "counter cross, or the rear uppercut as he leans in. Keep the "
            "weight centered and the feet ready - the shell is a "
            "counter-punching stance, not a hiding place. Drill the roll "
            "against slow straight punches first: shoulder up, punch "
            "glances, counter cross. The two great dangers are dropping "
            "the rear hand (the shell's one unforgivable sin) and "
            "standing in the shell against a dedicated body puncher - "
            "against body attacks, abandon the shell for the high guard."
        ),
        "key_points": [
            "The lead shoulder is the shield: roll it into straight punches so they glance off instead of landing.",
            "The rear hand never drops - it is cocked at the chin, and the shell exists to serve its counter.",
            "Every rolled punch loads the answer: roll-cross and roll-uppercut are the shell's dividends.",
            "The shell is side-on and economical: small rotations, not big movements, do the work.",
            "It is vulnerable to sustained body punching - know when to fold the shell and raise the high guard.",
        ],
        "requirements": [
            "Side-on shell posture: lead shoulder up, chin tucked behind it, rear glove cocked at chin.",
            "Clean shoulder rolls off live straight punches; forearm catches on hooks.",
            "Immediate counters (cross, uppercut) off the roll; disciplined switch to high guard vs body attack.",
        ],
        "standards": [
            "USA Boxing Coaching Manual: advanced defensive systems.",
        ],
        "citations": [CIT_USAB, CIT_COACH],
        "sig_lens": (
            "The Signature reading of the shoulder roll: the turning of "
            "the oath. The Signature boxer does not block the storm - he "
            "turns his shoulder to it and lets it pass, the way a "
            "mountain turns the wind. The Philly Shell in Signature hands "
            "is patience as provocation: every punch declined is a debt "
            "the opponent owes, and the rear hand is the collector."
        ),
    },
    {
        "key": "infighting_clinch",
        "name": "In-Fighting and the Clinch",
        "group": "Ring Craft",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "In-fighting is boxing at phone-booth distance: chest to "
            "chest, where long punches cannot exist and short hooks, "
            "uppercuts, and shoulder leverage rule. The in-fighter works "
            "inside the opponent's arms, turning him, digging body shots, "
            "and never letting him set his feet. The clinch is in-fighting's "
            "companion skill: tying up the opponent's arms to smother his "
            "offense, rest, or break his rhythm - then breaking clean on "
            "the referee's command. Both are legal, essential, and "
            "misunderstood: in-fighting is not brawling, it is "
            "short-range science, and the clinch is not holding, it is "
            "control. Masters of the inside win fights that look ugly and "
            "feel inevitable."
        ),
        "how_it_works": (
            "To get inside, slip the jab and step in deep, head on his "
            "chest or shoulder - never leave your head in the middle where "
            "uppercuts live. Once inside, keep your feet under you and "
            "punch short: compact hooks to the body, short uppercuts "
            "through the middle, all with tight arcs and the chin tucked. "
            "Use your shoulder and forearm to turn him - a little leverage "
            "spins him into your punches. To clinch: as he punches, step "
            "in and drape your arms over his, pinning his gloves to his "
            "own body, head to the side, weight on him to tire his arms. "
            "When the referee calls break, step back clean with your hands "
            "up - never punch on the break. Drill inside work on the bag "
            "from chest distance: short hooks, short uppercuts, constant "
            "head movement. Drill the clinch with a partner: tie up, "
            "control, break clean. The rules matter here: no holding and "
            "hitting, no wrestling him down, break when ordered."
        ),
        "key_points": [
            "Inside distance kills long punches: short hooks, short uppercuts, and leverage win the phone booth.",
            "Head position is safety: on his chest or shoulder, never in the middle where uppercuts wait.",
            "Turn him with shoulder and forearm leverage - an opponent who cannot set his feet cannot punch.",
            "The clinch ties up arms to smother offense and rest: drape, pin, control - then break clean on command.",
            "Know the rules cold: no holding and hitting, no wrestling down, break instantly when ordered.",
        ],
        "requirements": [
            "Effective short punching (compact hooks, short uppercuts) from chest-to-chest distance.",
            "Safe head positioning and turning leverage; constant head movement inside.",
            "Legal clinch: tie-up, control, and clean break on command; no fouls.",
        ],
        "standards": [
            "USA Boxing Rulebook: legal in-fighting and clinch conduct.",
            "Association of Boxing Commissions Unified Rules: holding, clinching, and break commands.",
            "IBA Technical and Competition Rules: infraction rules for holding.",
        ],
        "citations": [CIT_USAB, CIT_ABC, CIT_IBA, CIT_DEMPSEY],
        "sig_lens": (
            "The Signature reading of in-fighting: the close covenant. At "
            "long range the Signature boxer is a surveyor; inside, he is "
            "a craftsman - short tools, honest work, no wasted motion. "
            "The clinch is the Signature embrace: control without cruelty, "
            "rest without surrender, and always the clean break, because "
            "the Signature system keeps its oaths even at phone-booth "
            "distance."
        ),
    },
    {
        "key": "switch_stance",
        "name": "Switching Stances",
        "group": "Ring Craft",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Switching stances - fighting effectively from both orthodox "
            "and southpaw - is the mark of the complete boxer: it changes "
            "every angle, every punch path, and every defensive look in "
            "the middle of a fight. A switch mid-combination turns a "
            "blocked attack into an open lane; a switch under pressure "
            "gives a fresh defensive posture and a new lead hand to jab "
            "with. True switch-hitting means the rear hand is genuinely "
            "dangerous from both sides and the footwork is sound in both "
            "stances - it is not hopping stances for show. Done well it "
            "multiplies a fighter's options; done poorly it strands him "
            "in a stance he cannot fight from, which is worse than never "
            "switching at all."
        ),
        "how_it_works": (
            "Learn the mirror stance first as a beginner would: from "
            "orthodox, hop-switch the feet so the right foot leads, the "
            "guard flips, and you are southpaw - then drill stance, "
            "step-drag, jab, and cross from the new side until they feel "
            "almost as natural. The switch itself should happen in a "
            "neutral moment: after a combination, behind a jab, or during "
            "a pivot - never while punches are incoming. Switch with "
            "purpose: go southpaw to change the angle on an orthodox "
            "opponent (your lead foot outside his), then attack with the "
            "new lead hook and straight left. Drill: three punches "
            "orthodox, switch behind the jab, three punches southpaw, "
            "switch back. The test is honesty - if your southpaw cross "
            "has no power or your southpaw footwork crosses your feet, "
            "you are not a switch-hitter yet; keep drilling the weak side "
            "until it is."
        ),
        "key_points": [
            "Switch-hitting means genuinely fighting from both sides: real power, real footwork, real defense in each stance.",
            "Switch in neutral moments - behind a jab, after a combination, during a pivot - never under fire.",
            "The switch changes every angle: new lead hand, new power hand, new defensive look, new problems for the opponent.",
            "Against an orthodox fighter, the southpaw lead foot outside his creates the angle for the straight left.",
            "A weak-side switch is a liability, not a trick: drill the mirror stance until it is honest before using it live.",
        ],
        "requirements": [
            "Sound stance, step-drag, jab, and cross from both orthodox and southpaw.",
            "Clean mid-fight switches in neutral moments; no crossed feet or lost balance.",
            "Purposeful switching: angle creation and combination setup, not stance-hopping.",
        ],
        "standards": [
            "USA Boxing Coaching Manual: advanced tactical development.",
        ],
        "citations": [CIT_USAB, CIT_COACH],
        "sig_lens": (
            "The Signature reading of the switch: the two-sided oath. The "
            "Signature boxer swears the covenant with both hands - "
            "orthodox and southpaw, question and answer, each stance a "
            "complete temple. To switch is to show the opponent a second "
            "fighter wearing the same gloves. In the Signature system, "
            "mastery is not one perfect stance but the honesty to build "
            "two."
        ),
    },
    {
        "key": "conditioning",
        "name": "Conditioning and Roadwork",
        "group": "Conditioning",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Conditioning and roadwork are the engine room of boxing: the "
            "stamina, strength, and durability work that lets a fighter "
            "throw hard in round twelve as in round one. Roadwork - the "
            "traditional morning run - builds the aerobic base; interval "
            "sprints build the round-by-round recovery; bag rounds, pad "
            "rounds, and sparring build sport-specific endurance; and "
            "strength work builds the punch-resistant, punch-delivering "
            "body. Boxing fitness is unique: three minutes of explosive "
            "work, one minute of recovery, repeated - so training mimics "
            "exactly that rhythm. The old truth holds: fights are won or "
            "lost far from witnesses, on the road in the dark morning "
            "hours, long before the lights come on."
        ),
        "how_it_works": (
            "Build the week around the fight rhythm: roadwork three to "
            "five mornings a week - steady runs of three to five miles for "
            "the base, plus sprint intervals (for example, ten 100-meter "
            "sprints with walk-back recovery) for round recovery. In the "
            "gym: three-minute rounds on the heavy bag with one-minute "
            "rests, exactly like a fight, building from four rounds toward "
            "twelve; pad work for sharpness; controlled sparring for the "
            "real thing. Add strength twice a week - bodyweight circuits, "
            "medicine ball work, core work - prioritizing the legs, core, "
            "and shoulders that boxing runs on. Track it: resting heart "
            "rate falling and bag-round punch counts holding steady into "
            "late rounds are the honest signals. Taper the final week: "
            "sharpen, do not exhaust. And respect recovery - sleep, food, "
            "and rest days are training too, because the body builds "
            "fitness while resting, not while working."
        ),
        "key_points": [
            "Train the fight rhythm: three minutes explosive, one minute recovery - everything mimics the rounds.",
            "Roadwork builds the aerobic base; intervals build the between-rounds recovery; bag and sparring build fight endurance.",
            "Strength follows function: legs, core, shoulders - the boxing chain - trained twice weekly.",
            "Measure honestly: resting heart rate trends and late-round punch counts do not lie about fitness.",
            "Recovery is training: sleep, nutrition, and rest days are where the body banks the work.",
        ],
        "requirements": [
            "Weekly plan covering roadwork, intervals, bag/pad rounds in fight rhythm, and strength work.",
            "Round-structure discipline: three-minute work, one-minute rest, progressive round counts.",
            "Tracked metrics (resting heart rate, late-round output) and a taper week before competition.",
        ],
        "standards": [
            "USA Boxing Coaching Manual: conditioning and training methodology.",
        ],
        "citations": [CIT_USAB, CIT_COACH],
        "sig_lens": (
            "The Signature reading of conditioning: the forging of the "
            "covenant. Talent swears the oath in the gym; conditioning "
            "keeps it on the road at dawn, in the twelfth round, in the "
            "dark minutes no one sees. The Signature boxer treats every "
            "mile as a line of the oath written in sweat, every interval "
            "a promise renewed. In the Signature system, the fighter is "
            "forged long before he is revealed."
        ),
    },
    {
        "key": "ring_generalship",
        "name": "Ring Generalship and Fight Strategy",
        "group": "Ring Craft",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Ring generalship is the command of the fight: the strategic "
            "layer where the boxer imposes his game plan, adapts to the "
            "opponent's, and controls pace, positioning, and psychology "
            "round by round. It includes choosing the range, deciding when "
            "to press and when to box, cutting the ring or using lateral "
            "movement, targeting weaknesses discovered mid-fight, managing "
            "the clock and the scorecards, and breaking the opponent's "
            "will without breaking the rules. Judges score effective "
            "aggression, ring generalship, defense, and hard clean "
            "punching - the general wins by owning more of those "
            "categories than the soldier. Strategy is what turns "
            "techniques into victories."
        ),
        "how_it_works": (
            "Build the game plan before the fight: study the opponent - "
            "does he fade late, hate body punches, drop his right hand? "
            "Assign each round a job: early rounds to gather information "
            "behind the jab and bank points; middle rounds to impose your "
            "strength and test his answers; championship rounds to close "
            "hard. In the fight, run the plan but read constantly: if he "
            "solves your jab, double it or feint it; if he fades, raise "
            "the pressure; if you are behind on the cards, take "
            "calculated risks. Manage the clock: a lead in the final "
            "minute means boxing smart, not brawling. Between rounds, "
            "listen to the corner, breathe, and adjust one thing - the "
            "fighter who tries to fix everything fixes nothing. Drill "
            "strategy in sparring with constrained rounds: one round "
            "where you may only jab and move (information), one where you "
            "must cut off the ring (imposition), one where you start each "
            "exchange with a feint (psychology). The general wins the "
            "fight in the quiet moments between the loud ones."
        ),
        "key_points": [
            "Game plan before, adaptation during: study the opponent, assign each round a job, adjust one thing at a time.",
            "Control the categories judges score: effective aggression, ring generalship, defense, clean hard punching.",
            "Early rounds gather information and bank points; middle rounds impose; late rounds close.",
            "Read constantly: if he solves a weapon, change it - the plan serves the fighter, not the reverse.",
            "Manage pace, clock, and psychology: when to press, when to box, and how to break will within the rules.",
        ],
        "requirements": [
            "Written-style game plan per opponent (strengths, weaknesses, round jobs) executable in sparring.",
            "Demonstrated mid-fight adjustments: solving a neutralized weapon, exploiting a discovered weakness.",
            "Clock and scorecard awareness: appropriate risk per round and score state.",
        ],
        "standards": [
            "Association of Boxing Commissions Unified Rules: judging criteria (effective aggression, ring generalship, defense, hard and clean punching).",
            "USA Boxing Rulebook: scoring criteria.",
        ],
        "citations": [CIT_ABC, CIT_USAB, CIT_COACH],
        "sig_lens": (
            "The Signature reading of ring generalship: the command of the "
            "covenant. Techniques are soldiers; generalship is the "
            "commander who knows when each fights and when each rests. "
            "The Signature general studies the enemy, assigns the rounds "
            "their duties, and adapts without panic - because the "
            "Signature system holds that the fight is won first in the "
            "mind, then in the body, and only last on the canvas."
        ),
    },
    {
        "key": "fight_prep",
        "name": "Fight Preparation: Weigh-In to Opening Bell",
        "group": "Conditioning",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Fight preparation is everything between the weigh-in and the "
            "opening bell: making weight safely, rehydrating and refueling "
            "correctly, warming up the body and the mind, handling the "
            "dressing room, and walking to the ring ready. It is the least "
            "glamorous and most decisive phase - fighters have lost fights "
            "at the scales, in the sauna, and in the long wait before the "
            "walkout, long before a punch is thrown. Proper preparation "
            "means arriving at weight without destroying the body, "
            "restoring fluids and glycogen in the hours after, warming up "
            "in layers so the first round is not the warm-up, and keeping "
            "the mind on the plan rather than the occasion. The opening "
            "bell should find a fighter already sweating, already focused, "
            "already fighting in his head."
        ),
        "how_it_works": (
            "Make weight the safe way: the cut is managed over the full "
            "camp through diet, not starved off in the final days - only "
            "a small, planned water cut in the last 24 hours, and never "
            "beyond what your team and a professional can supervise. After "
            "the weigh-in, rehydrate steadily with water and electrolytes "
            "and refuel with familiar, easily digested carbohydrates - "
            "nothing new on fight day, ever. In the dressing room: wrap "
            "hands early, stay warm, shadowbox lightly to stay loose, and "
            "keep the atmosphere calm - the plan reviewed once, then "
            "trust. Warm up in layers starting about 30 minutes out: "
            "general movement, then pads or shadowboxing building to fight "
            "intensity, finishing a few minutes before the walk so you "
            "enter the ring warm but not spent. Walk out on the plan, not "
            "the emotion: the first round has a job (information and "
            "points), and the occasion does not change it."
        ),
        "key_points": [
            "Weight is made in camp, not in crisis: diet over weeks, only a small supervised water cut at the end.",
            "Rehydrate and refuel with familiar foods and fluids - nothing new on fight day.",
            "Warm up in layers to fight intensity before the walkout: the first round is never the warm-up.",
            "Dressing-room discipline: wrap early, stay loose, review the plan once, keep the mind on the job.",
            "Walk out on the plan: the occasion is noise - round one has its assignment regardless.",
        ],
        "requirements": [
            "Camp-long weight plan with safe, supervised final cut; no crash methods.",
            "Post-weigh-in rehydration and refueling protocol using familiar foods.",
            "Layered warm-up completed before the walkout; first-round assignment set.",
        ],
        "standards": [
            "Association of Boxing Commissions Unified Rules: weigh-in procedures and weight classes.",
            "USA Boxing Rulebook: weigh-in and medical requirements.",
        ],
        "citations": [CIT_ABC, CIT_USAB],
        "sig_lens": (
            "The Signature reading of fight preparation: the sealing of the "
            "covenant. The fight is not won under the lights; it is sealed "
            "in the quiet hours - the disciplined camp, the honest scales, "
            "the careful refuel, the layered warm-up, the calm dressing "
            "room. The Signature boxer walks to the ring already sworn: "
            "body ready, mind ready, plan ready. The bell does not start "
            "the oath - it witnesses it."
        ),
    },
]
