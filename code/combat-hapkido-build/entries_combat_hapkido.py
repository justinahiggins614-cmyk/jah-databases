#!/usr/bin/env python3
"""34 ladder-ordered hapkido combat technique records (public) plus
Signature-lens paragraphs for the 34 Signature editions.

Public records: real, fact-checked Korean hapkido knowledge - real Korean
terminology with translations, step-by-step body mechanics, joint-lock
principles, throws, kicks, pressure points, and weapon defenses. Civilian
training scope only: nothing on neutralizing military or defense-grade
systems, nothing hate-adjacent, no profanity, no religious talk.

Standard references: Tedeschi M. Hapkido: Traditions, Philosophy, Technique.
Weatherhill; 2000; Shaw S. Hapkido: Korean Art of Self-Defense. Tuttle;
1996; Kimm HY. Hapkido. H-Y Kimm; 2000; Kreighbaum E, Barthels KM.
Biomechanics: A Qualitative Approach for Studying Human Movement. Allyn and
Bacon; 1996.
"""

SIG_TAIL = ("Signature editions: his original Signature Hapkido Method - "
            "every technique a covenant of body and circle, the circle the "
            "shield, the lock the oath, defense the open hand. Clearly "
            "labeled Signature-made, never presented as authentic public "
            "record.")

CIT_TED = ("Tedeschi M. Hapkido: Traditions, Philosophy, Technique. "
           "Weatherhill; 2000.")
CIT_SHAW = ("Shaw S. Hapkido: Korean Art of Self-Defense. Tuttle; 1996.")
CIT_KIMM = ("Kimm HY. Hapkido. H-Y Kimm; 2000.")
CIT_BIO = ("Kreighbaum E, Barthels KM. Biomechanics: A Qualitative "
           "Approach for Studying Human Movement. Allyn and Bacon; 1996.")

ENTRIES = [
# ---------------------------------------------------------------- foundations
{
 "key": "stances", "name": "Stances: The Foundation Postures (Seogi)",
 "group": "Foundations", "ladder_rank": 1, "ladder_tier": "foundations",
 "description":
  "Stances (seogi) are the root of every hapkido technique. Without a stable "
  "root, no kick, lock, or throw can generate or receive force safely. The "
  "three stances every beginner masters first are the ready stance "
  "(charyeot seogi), the horse stance (juchum seogi), and the front stance "
  "(ap seogi), with the back stance (dwit seogi) following close behind. "
  "HOW TO DO IT. 1. Ready stance: stand straight, heels together, toes "
  "apart at roughly 45 degrees, hands in fists at your sides, eyes level, "
  "weight even. 2. Horse stance: step sideways to twice your shoulder width, "
  "turn both feet forward and parallel, sink until your thighs are near "
  "parallel to the floor, back straight, knees pushed outward over the "
  "toes, fists at your hips. 3. Front stance: step forward about one and a "
  "half shoulder widths, bend the front knee until it sits over the ankle, "
  "keep the back leg straight with the foot angled out 30 to 45 degrees, "
  "hips square to the front, spine tall. 4. Back stance: from the front "
  "stance, shift seventy percent of your weight to the back leg, bend the "
  "back knee, keep the front leg lightly bent with only the ball of the "
  "foot pressing, hips turned about 45 degrees. 5. In every stance, keep "
  "the danjeon (lower abdomen) firm, shoulders relaxed, and breathing low "
  "and even. 6. Transition drill: flow ready, horse, front, back, front, "
  "horse, ready, checking that the feet land in exactly the same marks "
  "each repetition.",
 "how_it_works":
  "A stance manages the body's center of gravity. Lowering the hips and "
  "widening the base increases stability against pushes and pulls, while "
  "alignment of knee over toe protects the joints under load. The front "
  "stance drives weight forward into strikes; the back stance loads weight "
  "backward to yield, evade, or prepare a counter; the horse stance gives "
  "a neutral, immovable platform for locks and throws. Every technique in "
  "this database begins and ends in a correct stance - the root decides "
  "whether the technique lives or dies.",
 "key_points": [
  "Seogi means stance: the root position every technique grows from.",
  "Charyeot seogi is the ready stance: heels together, toes out, eyes level.",
  "Juchum seogi is the horse stance: twice shoulder width, thighs near parallel, knees over toes.",
  "Ap seogi is the front stance: long, forward-weighted, hips square for driving strikes.",
  "Dwit seogi is the back stance: seventy percent of weight on the back leg, ready to yield or counter."],
 "requirements": [
  "Flat, clear floor space about two meters square per student.",
  "Bare feet or thin-soled training shoes for correct foot feel.",
  "Ten minutes of daily stance holding to build the root.",
  "A mirror or partner to check knee-over-toe alignment."],
 "standards": [
  "Knee tracks over the toes in every bent-leg stance, never collapsing inward.",
  "Spine stays tall: no hunching in the horse stance, no leaning in the front stance.",
  "Weight distribution matches the stance: even, fifty-fifty, or seventy-thirty as defined."],
 "citations": [CIT_TED, CIT_SHAW],
 "sig_lens":
  "Signature Hapkido Method: the stance is the Signature root - the oath "
  "the feet swear to the floor. He treats charyeot as the seal of "
  "readiness, the horse stance as the immovable armory, the front stance "
  "as the drawn line of intent, and the back stance as the open hand of "
  "yielding. Every stance is a covenant: the body promises stability, the "
  "floor promises footing, and the technique that grows between them is "
  "the kept word.",
},
{
 "key": "nakbeop", "name": "Breakfalls: Falling Safely (Nakbeop)",
 "group": "Foundations", "ladder_rank": 1, "ladder_tier": "foundations",
 "description":
  "Breakfalls (nakbeop) teach the body to land safely when thrown, swept, "
  "or knocked down. They are the first safety skill in hapkido because "
  "every throw in this art ends with a partner hitting the floor. There "
  "are four basic falls: the back fall, the side fall, the front fall, and "
  "the forward rolling fall. HOW TO DO IT. 1. Back fall: from a squat, "
  "tuck your chin hard to your chest, round your back, roll backward, and "
  "slap the mat with both arms at a 45-degree angle from the body at the "
  "moment your back touches, exhaling sharply. 2. Side fall: from a "
  "standing position, step across with one leg, sink onto that hip, tuck "
  "the chin, and slap the mat with the full length of the lower arm and "
  "hand while the legs land stacked, one on the other. 3. Front fall: "
  "from the knees first, fall forward onto the forearms with the hands "
  "forming a triangle, chin tucked and face turned to one side, slapping "
  "with both forearms as the body lands - never catch yourself on straight "
  "arms or the chin. 4. Forward roll: tuck the chin, round the back, roll "
  "over one shoulder diagonally across the back from shoulder to opposite "
  "hip, slapping the mat as you come up, and stand without using your "
  "hands. 5. Practice each fall from low to high: knees, squat, standing, "
  "then from a gentle partner push. 6. The slap disperses impact across a "
  "wide area and the exhale braces the core - never hold your breath on "
  "landing.",
 "how_it_works":
  "A breakfall converts a dangerous point impact into a safe distributed "
  "one. Tucking the chin protects the head and neck from whiplash; "
  "rounding the back increases the contact area; slapping the mat with the "
  "arms spreads the landing force across the limbs and torso instead of "
  "one bone; exhaling on impact braces the abdominal wall and prevents the "
  "wind being knocked out. The forward roll turns linear falling energy "
  "into rotational motion, which the body sheds gradually instead of all "
  "at once.",
 "key_points": [
  "Nakbeop means falling method: the safety skill under every throw.",
  "Chin tucks to the chest in every fall to protect the head and neck.",
  "The arm slap disperses impact across a wide area at the moment of landing.",
  "Exhale sharply on impact to brace the core.",
  "Progress low to high: knees, squat, standing, then partner-assisted."],
 "requirements": [
  "A padded mat or soft ground; never practice high falls on hard floors.",
  "A trained partner or instructor for partner-assisted falls.",
  "Wrist and ankle warm-up before every session.",
  "Patience: fifty clean low falls before attempting standing height."],
 "standards": [
  "Head never touches the mat in any fall.",
  "No straight-arm catches: land on slapping arms or the rounded back.",
  "Continuous breathing: exhale on every landing without exception."],
 "citations": [CIT_TED, CIT_BIO],
 "sig_lens":
  "Signature Hapkido Method: the fall is the Signature promise that no "
  "technique costs more than the lesson. He teaches nakbeop as the art of "
  "meeting the ground as an ally - the slap a handshake with the floor, "
  "the tucked chin a bow of respect to the body. The student who can fall "
  "fearlessly can train fearlessly, and the oath of the Signature root is "
  "that safety is trained first and assumed never.",
},
{
 "key": "balgeoreum", "name": "Footwork and Stepping (Balgeoreum)",
 "group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
 "description":
  "Footwork (balgeoreum) is how hapkido moves: not marching, but gliding, "
  "pivoting, and shifting weight so the body is always in range to act and "
  "out of range of harm. Good footwork makes every lock, throw, and kick "
  "possible and makes the student a moving target. HOW TO DO IT. 1. The "
  "basic step: from the ready stance, slide the front foot forward about "
  "one foot length, then bring the rear foot up to restore the stance - "
  "the feet never cross and the head stays level, gliding rather than "
  "bouncing. 2. The retreating step: slide the rear foot back first, then "
  "the front foot, keeping the guard up and the eyes on the partner. "
  "3. The pivot: on the ball of the front foot, swing the rear foot and "
  "hips ninety degrees, turning the whole body offline of an attack while "
  "the weight settles into a back stance. 4. The switch step: hop lightly "
  "to swap lead feet, landing softly in stance, used to change the "
  "attacking angle before a kick. 5. The shuffle: two quick short slides "
  "to close distance explosively before a throw entry. 6. Drill: a partner "
  "walks toward you and you maintain exactly one arm's distance using only "
  "the five steps, never crossing the feet, never turning the back.",
 "how_it_works":
  "Footwork controls distance and angle, the two variables that decide "
  "whether a technique reaches its target. Sliding keeps the center of "
  "gravity level so the body can act at any instant - bouncing wastes "
  "energy and telegraphs movement. Pivoting offline moves the body out of "
  "the attack's path while loading the hips for a counter, which is the "
  "physical basis of hapkido's circular-motion principle. Never crossing "
  "the feet keeps the base stable under sudden pushes.",
 "key_points": [
  "Balgeoreum means foot movement: gliding, pivoting, shifting.",
  "Feet never cross and the head never bounces during basic steps.",
  "The pivot turns the body ninety degrees offline while loading the hips.",
  "The switch step changes the lead leg to open new kicking angles.",
  "Distance drill: hold one arm's distance against a walking partner."],
 "requirements": [
  "Open floor space of at least three meters per student.",
  "A partner for the distance-keeping drill.",
  "Five minutes of daily step-and-pivot practice.",
  "Thin-soled footwear or bare feet for pivot feel."],
 "standards": [
  "Head height stays constant through all basic steps.",
  "Every step ends in a recognizable stance, never a scramble.",
  "Eyes stay on the partner through pivots and retreats."],
 "citations": [CIT_SHAW, CIT_BIO],
 "sig_lens":
  "Signature Hapkido Method: footwork is the Signature dance of distance - "
  "the feet write the covenant of range on the floor. He teaches the glide "
  "as silent intent, the pivot as the circle made visible, the switch as "
  "the changing of the oath's terms. The student who owns distance owns "
  "time, and the Signature fighter arrives exactly when the circle "
  "decides, never a step early or late.",
},
{
 "key": "jireugi", "name": "Straight Punch (Jireugi)",
 "group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
 "description":
  "The straight punch (jireugi) is hapkido's fundamental hand strike: a "
  "direct, hip-driven punch that teaches the body to deliver force in a "
  "straight line from the floor through the fist. HOW TO DO IT. 1. From a "
  "front stance, hold both fists at the hips, knuckles up, elbows close to "
  "the body. 2. Drive the punching fist forward in a straight line, "
  "rotating the fist so the knuckles finish horizontal, striking with the "
  "first two knuckles. 3. At the same instant, snap the hips forward and "
  "pull the opposite fist sharply back to the hip (the chamber return), "
  "which multiplies the punch's power. 4. Extend the arm to about "
  "ninety-five percent of full extension - never lock the elbow. "
  "5. Tighten the fist and the whole body for a split second at the moment "
  "of contact, then relax immediately. 6. Retract along the same straight "
  "line back to the hip. 7. Drill: ten slow punches watching the fist "
  "travel dead straight in a mirror, then ten fast punches with the hip "
  "snap, then alternating punches stepping forward across the floor.",
 "how_it_works":
  "The punch is a kinetic chain: the floor pushes the legs, the legs turn "
  "the hips, the hips rotate the torso, and the torso whips the arm "
  "forward, so the fist arrives carrying the body's mass, not just the "
  "arm's. The chamber return (hikite) adds counter-rotation that tightens "
  "the core at impact. Striking with the first two knuckles aligns the "
  "wrist bones with the forearm, preventing wrist collapse.",
 "key_points": [
  "Jireugi means thrusting strike: the straight punch is the foundation of all hand strikes.",
  "Power comes from the hip snap and chamber return, not the arm alone.",
  "Strike with the first two knuckles, wrist straight.",
  "Tighten the whole body for a split second at contact, then relax.",
  "Retract along the same line the punch traveled."],
 "requirements": [
  "A mirror for checking the straight line of the punch.",
  "A heavy bag or focus mitts for contact practice after form is clean.",
  "Hand wraps for bag work to protect the knuckles.",
  "Ten minutes of daily air punching to build the chain."],
 "standards": [
  "Elbow never fully locks at extension.",
  "Hips visibly rotate with every punch; no arm-only punching.",
  "Fist returns to the hip chamber after every strike."],
 "citations": [CIT_TED, CIT_BIO],
 "sig_lens":
  "Signature Hapkido Method: the straight punch is the Signature line - "
  "the shortest oath between two points. He teaches it as the body's "
  "written signature on the air: floor, hip, fist, one straight stroke. "
  "The chamber return is the vow kept on both ends - strike and guard "
  "honored in the same breath. The Signature fist never wanders; it "
  "travels the covenant line and comes home.",
},
{
 "key": "apchagi", "name": "Front Kick (Ap Chagi)",
 "group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
 "description":
  "The front kick (ap chagi) is the first kick every hapkido student "
  "learns: a fast, direct kick driven straight forward with the ball of "
  "the foot. It teaches chambering, the foundation of all kicking. HOW TO "
  "DO IT. 1. From a fighting stance, shift your weight to the support leg "
  "and lift the kicking knee straight up until the thigh is parallel to "
  "the floor - this is the chamber. 2. Pivot slightly on the support foot "
  "so the toes point about 30 degrees outward, keeping the support knee "
  "soft. 3. Snap the lower leg forward and up, striking with the ball of "
  "the foot, toes pulled back hard, at about solar-plexus height. 4. Snap "
  "the leg back to the chamber position immediately after contact - the "
  "recoil is as fast as the extension. 5. Set the foot down in stance "
  "without stomping. 6. Drill: hold a chair for balance and perform "
  "chamber-extend-rechamber in a slow three-count, then at full speed "
  "against a hand-held target pad.",
 "how_it_works":
  "The chamber stores the kick like a drawn bow: lifting the knee high "
  "pre-loads the hip flexors and hides the kick's target. Extension is "
  "fast because only the lower leg travels; recoil protects the leg from "
  "being caught and prepares the next technique. Pulling the toes back "
  "exposes the hard ball of the foot and locks the ankle, turning the foot "
  "into a solid striking surface instead of a floppy one.",
 "key_points": [
  "Ap chagi means front kick: chamber, extend, rechamber.",
  "Strike with the ball of the foot, toes pulled back.",
  "The support foot pivots about 30 degrees; the support knee stays soft.",
  "Recoil is as fast as the extension: never leave the leg hanging.",
  "Chamber high first: a high chamber hides the target and loads power."],
 "requirements": [
  "A target pad or heavy bag for contact practice.",
  "A chair or wall for balance during slow chamber drills.",
  "Ankle mobility warm-up before kicking sessions.",
  "Flat floor: never practice full kicks on slippery surfaces."],
 "standards": [
  "Toes pulled back and ankle locked on every kick.",
  "Kicking knee returns to chamber before the foot lands.",
  "Support foot stays flat: no rising onto the toes."],
 "citations": [CIT_SHAW, CIT_BIO],
 "sig_lens":
  "Signature Hapkido Method: the front kick is the Signature spear - one "
  "straight line from the rooted floor to the target. He teaches the "
  "chamber as the held breath of the oath and the snap as its spoken word. "
  "The recoil is the Signature promise to never overextend: strike, return, "
  "stand ready - the covenant of the kick honored in three beats.",
},
{
 "key": "dollyeochagi", "name": "Roundhouse Kick (Dollyeo Chagi)",
 "group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
 "description":
  "The roundhouse kick (dollyeo chagi) is hapkido's most-used kick: the leg "
  "swings in an arc and strikes with the instep or the ball of the foot. "
  "It teaches hip rotation, the engine of all circular kicks. HOW TO DO IT. "
  "1. From a fighting stance, lift the kicking knee across the body so the "
  "thigh points at roughly 45 degrees toward the target line - the "
  "chamber. 2. Pivot hard on the support foot, turning the heel toward the "
  "target until the support toes point away; this opens the hip. 3. Whip "
  "the hips over, swinging the lower leg in a horizontal arc, striking "
  "with the instep (for reach) or the ball of the foot (for penetration), "
  "toes pointed on an instep kick. 4. Keep the guard hands up throughout - "
  "the opposite hand swings down slightly to counterbalance. 5. Rechamber "
  "the knee along the same arc and set the foot down in stance. 6. Drill: "
  "practice the pivot alone until the support foot turns a full 180 "
  "degrees smoothly, then add the leg swing against a bag at rib height.",
 "how_it_works":
  "The roundhouse is a rotating lever: pivoting the support foot opens the "
  "hip joint, letting the large hip rotators whip the leg through a wide "
  "arc, so the foot arrives with high speed. Because the strike travels in "
  "an arc, it can slip around guards that would stop a straight kick. The "
  "counter-swinging hand balances the body's angular momentum so the "
  "kicker does not spin off balance.",
 "key_points": [
  "Dollyeo chagi means turning kick: the leg travels in a horizontal arc.",
  "The support foot pivots a full 180 degrees to open the hip.",
  "Strike with the instep for reach or the ball of the foot for penetration.",
  "Guard hands stay up: the kicking-side hand counters the swing.",
  "Rechamber along the same arc; never drop the leg straight down."],
 "requirements": [
  "A heavy bag or kick shield for arc practice.",
  "Hip mobility warm-up: leg swings and hip circles.",
  "Open floor space: the kick needs a full turning radius.",
  "A partner holding a hand target at rib height for accuracy."],
 "standards": [
  "Support foot completes its pivot before the leg extends.",
  "Striking surface is deliberate: instep or ball, never the toes.",
  "Balance is kept: no hopping or stumbling after the kick lands."],
 "citations": [CIT_TED, CIT_BIO],
 "sig_lens":
  "Signature Hapkido Method: the roundhouse is the Signature arc - the "
  "circle drawn at speed. He teaches the pivot as the opening of the "
  "covenant circle and the hip whip as the body's signature flourish "
  "across it. The instep is the brush, the arc the stroke; the guard hand "
  "that counters is the oath that defense is never abandoned for attack.",
},
{
 "key": "makgi", "name": "Basic Blocks (Makgi)",
 "group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
 "description":
  "Blocks (makgi) are hapkido's first line of defense: forearm techniques "
  "that deflect incoming strikes away from the body. The four basics are "
  "the low block, the middle outside block, the high block, and the knife-"
  "hand block. HOW TO DO IT. 1. Low block (arae makgi): from a front "
  "stance, swing the lead forearm down across the body in an arc, "
  "finishing with the fist just above the front knee, deflecting low kicks "
  "and punches outward. 2. Middle outside block (momtong bakkat makgi): "
  "chamber the fist at the opposite shoulder, then swing the forearm "
  "across the torso to the outside, elbow bent about 90 degrees, "
  "deflecting straight punches off the centerline. 3. High block (eolgul "
  "makgi): raise the forearm above the forehead, elbow bent, deflecting "
  "downward strikes up and away. 4. Knife-hand block (sonnal makgi): use "
  "the outer edge of the open hand in the same paths as the middle block, "
  "which flows directly into grabs and locks. 5. Every block finishes with "
  "a sharp exhale and a one-beat body tightening. 6. Drill: a partner "
  "throws slow straight punches and you deflect each one offline, stepping "
  "with the block.",
 "how_it_works":
  "A block is a deflection, not a wall: the forearm meets the attack at an "
  "angle and redirects its force past the body, which takes far less "
  "strength than stopping it dead. Chambering the blocking arm across the "
  "body loads the torso's rotation, and stepping with the block moves the "
  "target itself. The knife-hand block is hapkido's bridge to its joint "
  "locks - the open hand that blocks is already positioned to grab.",
 "key_points": [
  "Makgi means blocking: deflect the attack, never meet it head-on.",
  "Low, middle, high, and knife-hand are the four basic blocks.",
  "Deflect at an angle: redirection beats brute stopping.",
  "Step with the block: move the target while you deflect.",
  "The knife-hand block flows directly into grabs and locks."],
 "requirements": [
  "A partner throwing slow, controlled straight punches.",
  "Forearm conditioning: start light; bruising means too much force.",
  "Front stance proficiency: blocks are rooted in stance.",
  "Focus mitts for the partner's punches to protect their hands."],
 "standards": [
  "Blocking surface is the forearm or knife-hand edge, never the wrist joint.",
  "Every block ends with the body tightened and exhaled.",
  "Eyes stay on the attacker through the entire block."],
 "citations": [CIT_TED, CIT_SHAW],
 "sig_lens":
  "Signature Hapkido Method: the block is the Signature shield-wall - the "
  "open hand of defense raised as covenant. He teaches that a makgi never "
  "argues with force; it redirects it, the way the circle redirects all "
  "things. The knife-hand is the Signature bridge: the same hand that "
  "turns the blow aside is already reaching for the lock that ends the "
  "fight.",
},
{
 "key": "wonui", "name": "The Circular Motion Principle (Wonui)",
 "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
 "description":
  "The circular motion principle (wonui) is the soul of hapkido: never meet "
  "force with force, but join it, circle with it, and return it. Every "
  "lock, throw, and evasion in this database is an application of the "
  "circle. HOW TO DO IT. 1. Stand in a back stance facing a partner. 2. "
  "Your partner pushes your chest straight forward with both hands. 3. "
  "Instead of resisting, step back and to the side with the rear foot, "
  "pivoting your body so the push slides past your shoulder - you have "
  "joined the push's direction instead of opposing it. 4. Place your lead "
  "hand lightly on your partner's wrist and continue the motion in a "
  "circle: guide the pushing arm in a downward arc while your body turns. "
  "5. Feel how a small guiding force at the wrist, applied along the "
  "circle, moves your partner's whole body off balance. 6. Drill: trade "
  "roles, starting with slow pushes and gradually increasing speed, always "
  "circling rather than clashing. The three sub-principles are yu (softness "
  "and non-resistance), won (the circle itself), and hap (harmony, joining "
  "with the attacker's energy).",
 "how_it_works":
  "Linear force is strong along its line and weak everywhere else. By "
  "stepping offline and circling, the defender removes the target from the "
  "force's path and applies a small perpendicular force at a lever point "
  "(the wrist or elbow), which rotates the attacker's body around its own "
  "center of gravity. Because the defender adds to the attack's motion "
  "rather than stopping it, the attacker's own momentum does most of the "
  "work of unbalancing them.",
 "key_points": [
  "Wonui means circular principle: join force, circle it, return it.",
  "Never meet force head-on: step offline and let it pass.",
  "Yu (softness), won (circle), hap (harmony) are the three sub-principles.",
  "A small force at a lever point moves the whole body when applied on the circle.",
  "The attacker's own momentum does the work of unbalancing them."],
 "requirements": [
  "A cooperative partner pushing with steady, honest force.",
  "Back stance and pivot footwork proficiency.",
  "Open mat space for circling movement.",
  "An instructor to check that you are circling, not wrestling."],
 "standards": [
  "No strength contests: if you are muscling, the principle is lost.",
  "Every redirection follows a visible circular path.",
  "Balance is kept throughout: the circler never stumbles."],
 "citations": [CIT_TED, CIT_KIMM],
 "sig_lens":
  "Signature Hapkido Method: wonui is the Signature circle - the first and "
  "last covenant of his art. He teaches that the circle is the shield no "
  "force can break because it never stands in force's way; it receives, "
  "turns, and returns. The student's body becomes the round seal of the "
  "Signature system: every technique stamped in a ring, every conflict "
  "resolved the way water resolves the stone - by going around.",
},
{
 "key": "danjeon", "name": "Abdominal Breathing (Danjeon Hoheup)",
 "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
 "description":
  "Abdominal breathing (danjeon hoheup) is the breathing method behind "
  "every hapkido technique: deep breaths drawn into the lower abdomen (the "
  "danjeon) that stabilize the core and time the body's power. HOW TO DO "
  "IT. 1. Sit or stand in a relaxed ready stance, spine tall, shoulders "
  "down. 2. Place one hand on the lower abdomen, two finger-widths below "
  "the navel. 3. Inhale slowly through the nose for four counts, letting "
  "the abdomen expand under your hand while the chest barely moves. 4. "
  "Hold for two counts, feeling the pressure settle low in the body. 5. "
  "Exhale through the mouth for six counts, drawing the abdomen gently "
  "inward, imagining the breath pressing down into the floor. 6. In "
  "technique practice, exhale sharply on every strike, block, lock, and "
  "throw - the exhale is the body's tightening signal. 7. Drill: ten slow "
  "cycles seated, then ten cycles while holding a horse stance, then "
  "punches with a sharp exhale on each one.",
 "how_it_works":
  "Breathing into the danjeon engages the diaphragm fully and pressurizes "
  "the abdominal cavity, which braces the spine like an internal weight "
  "belt. The sharp exhale at the moment of technique (kihap's quiet "
  "cousin) spikes intra-abdominal pressure exactly when the body needs "
  "rigidity, then releases it so the body stays loose and fast between "
  "techniques. Slow practice breathing trains the nervous system to stay "
  "calm under the stress of sparring and self-defense.",
 "key_points": [
  "Danjeon hoheup means lower-abdomen breathing: the breath powers the technique.",
  "Inhale four counts through the nose, expanding the belly, not the chest.",
  "Exhale sharply on every strike, block, lock, and throw.",
  "The exhale braces the core at the instant of contact.",
  "Daily practice: ten cycles seated, ten in horse stance, then with punches."],
 "requirements": [
  "A quiet space for the first seated sessions.",
  "Loose clothing that does not restrict the abdomen.",
  "No full stomach: practice breathing on an empty or light stomach.",
  "Patience: correct abdominal breathing takes weeks to become habit."],
 "standards": [
  "Shoulders stay down and still during the inhale.",
  "Exhale always accompanies technique execution.",
  "No breath-holding during exertion: continuous breathing without gaps."],
 "citations": [CIT_TED, CIT_KIMM],
 "sig_lens":
  "Signature Hapkido Method: the breath is the Signature bellows - the "
  "covenant of air and iron. He teaches the danjeon as the furnace room of "
  "the body: the inhale gathers the oath, the hold seals it, the exhale "
  "strikes it like a hammer on steel. Every technique breathes the "
  "Signature rhythm - gather, seal, release - and the fighter who masters "
  "the breath masters the timing of everything.",
},
{
 "key": "yu", "name": "The Principle of Softness (Yu)",
 "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
 "description":
  "The principle of softness (yu) is hapkido's answer to strength: yield "
  "where the attacker is strong, act where the attacker is weak. It is "
  "trained as a physical habit, not a philosophy lecture. HOW TO DO IT. 1. "
  "Face a partner and join right wrists, each gripping the other's wrist. "
  "2. Your partner tries to push your hand straight down to your hip using "
  "muscle. 3. Instead of resisting, relax your arm completely and let your "
  "hand drop with the push, stepping back to keep balance. 4. At the "
  "moment your partner's push reaches full extension and their balance "
  "commits forward, circle your relaxed hand up and over their wrist, "
  "guiding their committed arm past you. 5. Feel how their strength did the "
  "work and your softness only steered it. 6. Drill: repeat with pushes, "
  "pulls, and grabs, alternating roles, with the rule that whoever tenses "
  "up loses the exchange. Softness is trained relaxation under pressure: "
  "loose shoulders, soft hands, mobile hips, and a mind that watches "
  "instead of panics.",
 "how_it_works":
  "Tense muscles are slow muscles: contraction in one direction inhibits "
  "speed in every other. By staying soft, the defender keeps all movement "
  "options open and can feel the attacker's intentions through contact "
  "(listening energy). Yielding to a push lets the attacker's force "
  "overextend their base; the defender's small circular addition then "
  "topples an already-committed structure. This is why smaller hapkido "
  "practitioners routinely control larger partners.",
 "key_points": [
  "Yu means softness: yield to strength, act on weakness.",
  "Tense muscles are slow: relaxation keeps every option open.",
  "Yielding lets the attacker overextend; the circle finishes the job.",
  "Soft hands feel intention through contact: listening energy.",
  "Whoever tenses first loses: the drill rule that trains the habit."],
 "requirements": [
  "A cooperative partner for push, pull, and grab exchanges.",
  "Mat space for safe off-balancing.",
  "Prior breakfall training: yielding leads to falling.",
  "An instructor to enforce the no-tensing rule."],
 "standards": [
  "Shoulders stay down and loose through every exchange.",
  "No strength contests: technique replaces muscle on every repetition.",
  "The yielder keeps balance while the pusher loses it."],
 "citations": [CIT_TED, CIT_KIMM],
 "sig_lens":
  "Signature Hapkido Method: yu is the Signature water - the covenant that "
  "softness outlasts hardness. He teaches the student to be the stream, "
  "not the rock: the rock breaks the wave once, the stream wears the rock "
  "forever. In his Method, the relaxed hand is the honest hand - it feels "
  "truth through contact and answers with the circle, never with "
  "tension's lie.",
},
{
 "key": "geodeureo", "name": "Wrist Escape (Sonmok Geodeureo)",
 "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
 "description":
  "The wrist escape (sonmok geodeureo) is the first self-defense technique "
  "most hapkido students learn: how to free a grabbed wrist using the "
  "weakest point of the grip. HOW TO DO IT. 1. Your partner grabs your "
  "right wrist with their right hand (same-side grab). 2. Note the gap: "
  "their grip is weakest between their thumb and fingers. 3. Turn your "
  "palm to face their thumb side, make a tight fist, and pull your wrist "
  "sharply toward that gap in a small circle while stepping back. 4. Your "
  "fist should pop free through the thumb-finger opening. 5. For a two-"
  "handed grab on one wrist: raise both your hands high overhead in an "
  "arc, then drop your body weight suddenly while pulling the hands down "
  "and apart - the combined drop and spread breaks both grips. 6. For a "
  "cross grab (their right hand on your left wrist): step to the outside, "
  "turn your captured hand palm-up, and circle it over and around their "
  "grabbing arm. 7. Drill: the partner grabs with increasing firmness; "
  "you escape without using arm strength, only the gap and the circle.",
 "how_it_works":
  "A grip is a ring of four fingers against one thumb: the thumb side is "
  "structurally the weakest link. Escaping toward that gap means fighting "
  "one thumb instead of four fingers. The circular pull adds the body's "
  "rotation to the escape, and stepping back removes the base the grabber "
  "was holding. Against two-handed grabs, dropping the body weight "
  "multiplies the escaping force beyond what arm muscle alone could "
  "produce.",
 "key_points": [
  "Sonmok geodeureo means wrist shaking-off: escape toward the thumb gap.",
  "Every grip is weakest between the thumb and fingers.",
  "Circle the wrist free: never pull straight against the full grip.",
  "Two-handed grabs break with a high arc plus a sudden body drop.",
  "Escape with mechanics, not muscle: the gap and the circle do the work."],
 "requirements": [
  "A partner grabbing with honest, increasing firmness.",
  "Wrist warm-up: circles and gentle stretches.",
  "Mat space: escapes can end in throws at higher levels.",
  "Trimmed fingernails on both partners for grab drills."],
 "standards": [
  "The escape targets the thumb gap on every repetition.",
  "No arm-wrestling: if it takes muscle, the angle is wrong.",
  "Balance is kept: the escaper never stumbles free."],
 "citations": [CIT_SHAW, CIT_KIMM],
 "sig_lens":
  "Signature Hapkido Method: the wrist escape is the Signature key - the "
  "small covenant that opens the locked door. He teaches the student to "
  "read every grip the way a locksmith reads a lock: find the weak pin, "
  "the thumb's gap, and turn the circle gently. The hand that escapes "
  "cleanly has sworn the Signature oath: no struggle, no panic, only the "
  "precise small motion that sets the body free.",
},
{
 "key": "sonmokkkokki", "name": "Basic Wrist Lock (Sonmok Kkokki)",
 "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
 "description":
  "The basic wrist lock (sonmok kkokki) is hapkido's signature technique: "
  "controlling an attacker by bending the wrist past its comfortable range. "
  "It is the gateway to all joint locks. HOW TO DO IT. 1. Your partner "
  "grabs your right wrist with their right hand. 2. With your free left "
  "hand, cover their grabbing hand, pressing it onto your wrist so it "
  "cannot let go. 3. Turn your captured right hand palm-up and thread it "
  "under and around so your palm faces their forearm. 4. Grip their hand "
  "with both of yours, thumbs on the back of their hand. 5. Bend their "
  "wrist downward and toward their own forearm while stepping back and "
  "turning your body - their wrist folds under your two-handed control. 6. "
  "Apply pressure slowly: stop the instant your partner taps or shows "
  "discomfort. 7. The lock controls them: with the wrist bent, their whole "
  "arm and body must follow where you guide the lock. 8. Drill: apply the "
  "lock in slow motion from a wrist grab, a lapel grab, and a punch catch, "
  "always stopping at the tap.",
 "how_it_works":
  "The wrist is a small joint with limited range: bending it beyond about "
  "90 degrees loads the ligaments and produces pain and structural control "
  "long before anything breaks. Two hands on one wrist gives the defender "
  "overwhelming leverage, and stepping back adds body weight to the "
  "pressure. Because the lock bends the joint toward the body's own "
  "centerline, the attacker's entire structure must move to relieve the "
  "pressure - that is why a wrist lock can walk a larger person wherever "
  "the defender chooses.",
 "key_points": [
  "Sonmok kkokki means wrist breaking/folding: the gateway joint lock.",
  "Cover the grabbing hand first so it cannot let go and slip out.",
  "Two hands on one wrist: overwhelming leverage with minimal strength.",
  "Apply slowly and stop at the tap: control, not injury.",
  "The bent wrist steers the whole body: the lock is a handle on the person."],
 "requirements": [
  "A trained partner who taps early and honestly.",
  "Wrist escape proficiency: escapes come before locks.",
  "Mat space for guided takedowns from the lock.",
  "An instructor supervising all lock practice."],
 "standards": [
  "Pressure is applied gradually: never snap a lock.",
  "The tap is sacred: release instantly, every time.",
  "Both partners stay calm: locks are practiced, not fought."],
 "citations": [CIT_TED, CIT_KIMM],
 "sig_lens":
  "Signature Hapkido Method: the wrist lock is the Signature handshake - "
  "the covenant sealed on the joint. He teaches that two hands on one "
  "wrist is the body's honest arithmetic: the circle closes, the oath is "
  "kept, and the partner's whole structure answers to the small bend. The "
  "tap is the Signature amen - the sacred word that ends the technique "
  "the instant it is spoken.",
},
# ---------------------------------------------------------------- compounded
{
 "key": "palkkumchikkokki", "name": "Elbow Lock (Palkkumchi Kkokki)",
 "group": "Compounded", "ladder_rank": 4, "ladder_tier": "compounded",
 "description":
  "The elbow lock (palkkumchi kkokki) controls the arm at the elbow joint, "
  "a larger and stronger lock than the wrist, used when the attacker "
  "resists the smaller locks. HOW TO DO IT. 1. From a wrist lock that the "
  "partner is resisting by straightening the arm, slide one hand up to cup "
  "their elbow. 2. Step to the outside of their arm while pulling their "
  "wrist toward your hip, so their arm straightens across your body. 3. "
  "Press down on their elbow with your palm while lifting their wrist "
  "slightly - the elbow is trapped between your pressing hand and your "
  "body. 4. Keep their arm straight: a bent elbow escapes, a straight "
  "elbow locks. 5. Guide them down to the mat by increasing the downward "
  "pressure slowly, stepping with the motion. 6. Pin: kneel beside them "
  "with the elbow lock maintained, their wrist controlled at your hip. 7. "
  "Drill: transition from wrist lock to elbow lock the instant the partner "
  "straightens the arm, in slow motion, stopping at the tap.",
 "how_it_works":
  "The elbow is a hinge that bends one way: pressing it toward "
  "straightening past its limit loads the joint capsule. With the wrist "
  "controlled at the hip and the elbow pressed down, the arm becomes a "
  "lever with the defender's body as the fulcrum - the attacker's shoulder "
  "and torso must follow the lever or the elbow takes the force. "
  "Transitioning from the failed wrist lock to the elbow lock teaches the "
  "core hapkido habit: when one lock fails, flow to the next joint, never "
  "wrestle the failed one.",
 "key_points": [
  "Palkkumchi kkokki means elbow folding: the lock for a resisting arm.",
  "Straighten the arm across your body: a bent elbow escapes.",
  "Wrist at your hip, pressing hand on the elbow: the lever and fulcrum.",
  "Flow from wrist lock to elbow lock the instant the arm straightens.",
  "Guide down slowly: the lock steers them to the mat."],
 "requirements": [
  "Wrist lock proficiency: the elbow lock is its follow-up.",
  "A partner who taps early on elbow pressure.",
  "Mat space for takedowns and pins.",
  "Instructor supervision: elbow locks demand slow practice."],
 "standards": [
  "Pressure increases gradually: no sudden drops on the elbow.",
  "The tap ends the technique instantly.",
  "The defender's own elbow stays soft: no hyperextending yourself."],
 "citations": [CIT_TED, CIT_SHAW],
 "sig_lens":
  "Signature Hapkido Method: the elbow lock is the Signature hinge - the "
  "covenant written on the larger joint. He teaches the transition as the "
  "oath's second verse: when the wrist's word is refused, the elbow speaks. "
  "The arm laid across the body becomes the Signature lever, and the "
  "student learns the deeper vow - never wrestle a failed lock, only flow "
  "to the next circle.",
},
{
 "key": "yeopchagi", "name": "Side Kick (Yeop Chagi)",
 "group": "Compounded", "ladder_rank": 4, "ladder_tier": "compounded",
 "description":
  "The side kick (yeop chagi) is hapkido's power kick: the body's mass "
  "drives straight into the target along the leg's line, striking with "
  "the heel or the knife-edge of the foot. HOW TO DO IT. 1. From a "
  "fighting stance, lift the kicking knee high across the body, thigh "
  "nearly horizontal - the chamber. 2. Pivot the support foot 180 degrees "
  "so the heel points at the target and the body turns fully sideways. 3. "
  "Lean the torso slightly away from the target as the leg extends: this "
  "adds reach and aligns the body's mass behind the heel. 4. Strike with "
  "the heel (for power) or the outer edge of the foot (for reach), driving "
  "through the target. 5. Rechamber the knee along the same line and set "
  "the foot down in stance. 6. Drill: practice against a heavy bag, "
  "focusing on the full support-foot pivot first, then adding the lean, "
  "then the full drive. Common targets in training are the pad at rib and "
  "thigh height.",
 "how_it_works":
  "The side kick lines the leg up like a piston: hip, knee, and ankle "
  "stacked so the body's weight drives straight through the heel into the "
  "target. Leaning away lengthens the striking line and commits the mass "
  "behind the blow, which is why the side kick hits harder than the "
  "roundhouse. The full 180-degree pivot is essential: without it the hip "
  "cannot open and the kick becomes a weak push.",
 "key_points": [
  "Yeop chagi means side kick: the piston kick, body mass behind the heel.",
  "Support foot pivots a full 180 degrees: heel points at the target.",
  "Strike with the heel for power or the foot's edge for reach.",
  "Lean slightly away to add reach and stack mass behind the blow.",
  "Rechamber along the same line: never drop the extended leg."],
 "requirements": [
  "A heavy bag for power development.",
  "Hip mobility warm-up: the side kick demands an open hip.",
  "Roundhouse kick proficiency: the pivot mechanics transfer.",
  "A partner holding a kick shield at rib height."],
 "standards": [
  "Heel or foot-edge strikes only: never the toes or instep.",
  "Full pivot before extension on every kick.",
  "Landing in stance, balanced, guard up."],
 "citations": [CIT_SHAW, CIT_BIO],
 "sig_lens":
  "Signature Hapkido Method: the side kick is the Signature piston - the "
  "body's mass sworn into a single line. He teaches the lean as the "
  "covenant's commitment: the torso yields back so the heel may speak "
  "forward. The full pivot is the circle's permission - without the turn, "
  "the oath has no power; with it, the kick carries the whole Signature "
  "root.",
},
{
 "key": "songarakkkokki", "name": "Finger Locks (Songarak Kkokki)",
 "group": "Compounded", "ladder_rank": 4, "ladder_tier": "compounded",
 "description":
  "Finger locks (songarak kkokki) control an attacker through the small "
  "joints of the fingers - the smallest levers in the body's joint-lock "
  "system, and therefore the easiest to control with minimal force. HOW TO "
  "DO IT. 1. When a partner grabs your wrist, clothing, or throat with an "
  "open hand, catch one or two of their fingers with your hand. 2. Bend "
  "the captured fingers backward toward the back of their hand, keeping "
  "your own wrist straight and strong. 3. Step back as you bend, adding "
  "your body weight to the small lever. 4. Guide the partner down or back "
  "by steering the bent fingers: the hand follows, the arm follows, the "
  "body follows. 5. Stop at the tap, as with all locks. 6. A second "
  "application: peel a grabbing hand off your clothing one finger at a "
  "time, bending each back just enough to force the release. 7. Drill: "
  "practice catching a single finger from a slow wrist grab, bending with "
  "the whole body, never with finger strength alone.",
 "how_it_works":
  "Fingers are tiny levers with almost no muscle behind them: a small "
  "bending force at the fingertip generates overwhelming torque at the "
  "knuckle. Because the hand's grip depends on all fingers working "
  "together, controlling one or two collapses the whole grip. The "
  "technique demonstrates hapkido's leverage ladder in miniature: the "
  "smaller the joint, the less force the lock requires.",
 "key_points": [
  "Songarak kkokki means finger folding: the smallest levers, the least force.",
  "Bend captured fingers back toward the back of the hand.",
  "Step back and add body weight: never rely on finger strength.",
  "One or two controlled fingers collapse the whole grip.",
  "Stop at the tap: small joints need extra care."],
 "requirements": [
  "A partner with healthy fingers who taps at the first pressure.",
  "Extreme gentleness: finger joints injure easily.",
  "Wrist lock proficiency: the same principles, smaller joint.",
  "Instructor supervision mandatory for finger lock practice."],
 "standards": [
  "Bend with the body, never with the fingers alone.",
  "One or two fingers at a time: never crank the whole hand.",
  "The tap ends the technique before discomfort becomes pain."],
 "citations": [CIT_TED, CIT_KIMM],
 "sig_lens":
  "Signature Hapkido Method: the finger lock is the Signature fine print - "
  "the covenant written smallest and kept most precisely. He teaches that "
  "the tiniest lever carries the greatest lesson: true control needs "
  "almost no force when the mechanics are honest. The student who can move "
  "a partner by one finger has understood the Signature arithmetic of the "
  "whole art.",
},
{
 "key": "sudochigi", "name": "Knife-Hand Strike (Sudo Chigi)",
 "group": "Compounded", "ladder_rank": 4, "ladder_tier": "compounded",
 "description":
  "The knife-hand strike (sudo chigi) strikes with the outer edge of the "
  "open hand - the same hand shape as the knife-hand block, now used as a "
  "weapon. It targets the neck, temple, ribs, and collarbone in training "
  "on pads. HOW TO DO IT. 1. Form the hand: fingers straight and tight "
  "together, thumb tucked hard against the palm, striking with the fleshy "
  "edge below the little finger. 2. Chamber the striking hand at the "
  "opposite ear. 3. Swing the hand in a downward diagonal arc, rotating "
  "the hips into the strike, hitting with the hand's edge at about a 45-"
  "degree angle. 4. At contact, tighten the hand and body for a split "
  "second, then relax. 5. A second form is the inward knife-hand: chamber "
  "at the same-side shoulder and swing horizontally across, striking with "
  "the same edge. 6. Drill: practice both arcs slowly against a hand pad, "
  "checking the hand stays rigid and the thumb stays tucked, then at speed "
  "with the hip rotation.",
 "how_it_works":
  "The knife-hand concentrates the arm's force onto the narrow edge of the "
  "hand, raising the pressure on the target. The diagonal arc combines a "
  "chopping drop (body weight) with a swing (hip rotation), and the "
  "tucked thumb plus tightened fingers turn the open hand into a rigid "
  "striking tool. Because the same shape blocks and strikes, the knife-"
  "hand lets a defender turn a block into a counterattack without "
  "changing the hand.",
 "key_points": [
  "Sudo chigi means knife-hand strike: the hand's edge as a weapon.",
  "Fingers tight together, thumb tucked hard: the hand must be rigid.",
  "Two arcs: downward diagonal from the opposite ear, horizontal inward.",
  "Hips rotate into every strike: the hand is the delivery, the hip the engine.",
  "Same shape blocks and strikes: defense becomes counterattack instantly."],
 "requirements": [
  "A hand pad or heavy bag for contact practice.",
  "Knife-hand block proficiency: the shape is the same.",
  "Wrist conditioning: start with light contact.",
  "A partner holding the pad at neck, rib, and thigh heights."],
 "standards": [
  "Thumb tucked on every strike without exception.",
  "Striking surface is the hand's edge, never the fingers or palm.",
  "Body tightens at contact and relaxes immediately after."],
 "citations": [CIT_SHAW, CIT_BIO],
 "sig_lens":
  "Signature Hapkido Method: the knife-hand is the Signature blade - the "
  "open hand sworn into an edge. He teaches that the same hand that turns "
  "aside the blow may answer it, the covenant of defense and counter kept "
  "in one shape. The tucked thumb is the Signature discipline: no loose "
  "ends, no wasted motion, the hand an honest tool from block to strike.",
},
{
 "key": "eokkaekkokki", "name": "Shoulder Lock (Eokkae Kkokki)",
 "group": "Compounded", "ladder_rank": 5, "ladder_tier": "compounded",
 "description":
  "The shoulder lock (eokkae kkokki) controls the largest joint of the arm "
  "system, used when the attacker powers through the wrist and elbow locks. "
  "The classic form is the bent-arm lock with the attacker's hand forced up "
  "behind their own back. HOW TO DO IT. 1. From a failed elbow lock, let "
  "the partner's arm bend as they pull back. 2. Step deep to the outside of "
  "their body, sliding your near hand up to control their wrist. 3. Fold "
  "their forearm up behind their back, keeping their elbow below their "
  "shoulder line, your other hand pressing on their elbow. 4. Walk them "
  "forward by lifting the folded wrist slightly: their shoulder must move "
  "or take the pressure. 5. To take them down, step across their legs while "
  "maintaining the fold and guide them to the mat in slow motion. 6. Pin "
  "with a knee near (never on) their back, the lock held gently. 7. Drill: "
  "practice the wrist-to-elbow-to-shoulder flow as one continuous motion, "
  "stopping at each tap, learning to feel which joint the partner gives "
  "you.",
 "how_it_works":
  "The shoulder is a ball-and-socket joint with wide range, but forcing the "
  "hand up behind the back drives the joint toward the edge of that range, "
  "where the capsule and ligaments take the load. With the elbow pinned "
  "below the shoulder line, the defender's lifting hand becomes a lever on "
  "the whole shoulder girdle: small lifts produce large control. This is "
  "the top of hapkido's joint-lock ladder - wrist, elbow, shoulder - and "
  "the proof that locks chain together.",
 "key_points": [
  "Eokkae kkokki means shoulder folding: the top of the lock ladder.",
  "Fold the forearm up behind the back; keep the elbow below the shoulder line.",
  "Small lifts of the folded wrist steer the whole shoulder.",
  "Chain the locks: wrist to elbow to shoulder in one flow.",
  "Walk them, then guide them down: the lock is a steering wheel."],
 "requirements": [
  "Wrist and elbow lock proficiency: the shoulder lock completes the chain.",
  "A partner with healthy shoulders who taps early.",
  "Mat space for guided takedowns.",
  "Instructor supervision: shoulder locks need expert pacing."],
 "standards": [
  "Elbow stays below the shoulder line at all times.",
  "Pressure builds gradually; the tap ends everything instantly.",
  "The defender never drops body weight onto the locked joint."],
 "citations": [CIT_TED, CIT_KIMM],
 "sig_lens":
  "Signature Hapkido Method: the shoulder lock is the Signature crown - "
  "the covenant sealed on the body's largest arm joint. He teaches the "
  "three-lock chain as the Signature ladder of control: wrist the word, "
  "elbow the sentence, shoulder the full oath. The student who flows up "
  "the chain without wrestling has learned the deepest Signature lesson - "
  "that control climbs, never clutches.",
},
{
 "key": "dwichagi", "name": "Back Kick (Dwi Chagi)",
 "group": "Compounded", "ladder_rank": 5, "ladder_tier": "compounded",
 "description":
  "The back kick (dwi chagi) drives the heel straight backward into a "
  "target behind the kicker - hapkido's answer to an attacker closing from "
  "the rear, and one of the art's most powerful kicks. HOW TO DO IT. 1. "
  "From a fighting stance, look over your shoulder to spot the target. 2. "
  "Lift the kicking knee high across the body, turning the hips so the "
  "back faces the target. 3. Drive the leg straight back, heel first, "
  "leaning the torso forward to add body weight behind the heel. 4. Strike "
  "with the heel, leg fully extended along the body's centerline - the "
  "kick travels straight, not in an arc. 5. Rechamber the knee and turn "
  "back to face the target in stance. 6. Drill: practice against a heavy "
  "bag with a partner calling the timing, starting slow to learn the "
  "straight line, then adding the torso lean and drive. The kick is "
  "trained on pads at torso height.",
 "how_it_works":
  "The back kick puts the body's strongest pushing muscles - the glutes "
  "and quads - directly behind the heel along a straight line, with the "
  "torso's forward lean stacking body weight into the drive. Looking over "
  "the shoulder aims the kick: the eyes set the line before the leg "
  "fires. Because the kick travels straight back along the centerline, it "
  "is hard to see coming and harder to deflect than an arcing kick.",
 "key_points": [
  "Dwi chagi means back kick: heel driven straight backward.",
  "Look over the shoulder first: the eyes set the line.",
  "Strike with the heel, leg extended along the centerline.",
  "Lean the torso forward to stack body weight behind the heel.",
  "Rechamber and turn back to face: never admire the kick."],
 "requirements": [
  "A heavy bag for the straight drive.",
  "Side kick proficiency: the chamber and pivot transfer.",
  "Neck mobility warm-up for the over-shoulder look.",
  "A partner to call timing and hold the bag."],
 "standards": [
  "The kick travels straight back, never arcing sideways.",
  "Heel contact only: no toes, no instep.",
  "Balance held on the support leg through rechamber."],
 "citations": [CIT_SHAW, CIT_BIO],
 "sig_lens":
  "Signature Hapkido Method: the back kick is the Signature answer - the "
  "oath that guards the rear as faithfully as the front. He teaches the "
  "over-shoulder look as the covenant of awareness: the fighter sees "
  "before striking, never blind. The heel driven straight back is the "
  "Signature seal pressed behind - the circle protects all directions, "
  "and no angle is left unsworn.",
},
{
 "key": "balgeolgi", "name": "Leg Sweep (Balgeolgi)",
 "group": "Compounded", "ladder_rank": 5, "ladder_tier": "compounded",
 "description":
  "The leg sweep (balgeolgi) takes an attacker's feet out from under them "
  "with a low, fast kick to the ankle or shin - the simplest takedown in "
  "hapkido and the foundation of all throws. HOW TO DO IT. 1. From a "
  "fighting stance, time the sweep for the moment your partner's weight "
  "shifts onto the target leg - a weighted leg cannot lift away. 2. Swing "
  "your leg low and fast in a shallow arc, striking with the instep or "
  "the sole against their ankle. 3. At the same instant, pull or push "
  "their upper body in the opposite direction with your hands - the sweep "
  "takes the base while your hands take the top. 4. Follow through the "
  "sweep: the leg continues its arc after contact. 5. Your partner "
  "practices the side fall they learned in nakbeop as they go down. 6. "
  "Drill: a partner steps toward you repeatedly; you sweep the stepping "
  "leg with the hand assist, starting at quarter speed until the timing "
  "clicks.",
 "how_it_works":
  "A standing person is an inverted pendulum: remove the support at the "
  "right moment and gravity does the rest. Sweeping a weighted leg works "
  "because the foot is planted and cannot evade; pushing the upper body "
  "the opposite way moves the center of gravity past the vanished base, "
  "guaranteeing the fall. The technique is pure timing - a fast sweep at "
  "the wrong moment just taps a lifted foot.",
 "key_points": [
  "Balgeolgi means leg hooking/sweeping: timing beats force.",
  "Sweep the weighted leg: a planted foot cannot evade.",
  "Hands move the top opposite to the sweep: base and top separate.",
  "Strike with the instep or sole at ankle height.",
  "Follow through: the leg continues its arc after contact."],
 "requirements": [
  "Breakfall proficiency: the partner must fall safely.",
  "A partner stepping with honest, committed weight shifts.",
  "Mat space for the takedowns.",
  "Ankle warm-up: sweepers and swept ankles both work hard."],
 "standards": [
  "Contact at ankle or low shin only: never sweep the knee.",
  "Speed builds gradually: quarter speed until timing is clean.",
  "The swept partner always gets a safe fall: no dumping."],
 "citations": [CIT_TED, CIT_BIO],
 "sig_lens":
  "Signature Hapkido Method: the sweep is the Signature timing - the "
  "covenant kept at exactly the right instant. He teaches that the sweep "
  "asks for nothing but the moment: the weighted foot, the committed "
  "step, the breath between. The student who sweeps cleanly has learned "
  "the Signature patience - to wait for the circle's permission rather "
  "than force the technique.",
},
{
 "key": "otdongjapgi", "name": "Lapel Grab Defense (Otdong Japgi)",
 "group": "Compounded", "ladder_rank": 5, "ladder_tier": "compounded",
 "description":
  "The lapel grab defense (otdong japgi) answers the most common street "
  "confrontation: an attacker seizing your clothing with one or two hands. "
  "Hapkido turns the grab into a lock on the grabber. HOW TO DO IT. 1. "
  "Your partner grabs your lapel or shirt front with their right hand. 2. "
  "Immediately cover their grabbing hand with both of yours, pinning it to "
  "your chest so they cannot release and punch. 3. Step back and to the "
  "side, turning your body - this begins the wrist lock (sonmok kkokki) on "
  "their grabbing hand. 4. Bend their wrist down and outward as you did in "
  "the basic wrist lock, guiding them forward and down. 5. For a two-"
  "handed lapel grab: drop your weight suddenly while bringing both hands "
  "up inside their arms, then circle outward - the drop plus the outward "
  "circle breaks the grips and flows into a double wrist control. 6. "
  "Drill: the partner grabs with one hand, then two, with increasing "
  "commitment; you answer with the cover, the step, and the lock, stopping "
  "at the tap.",
 "how_it_works":
  "Grabbing your clothing commits the attacker's hand and arm to a fixed "
  "point - your chest - giving you a known, stable handle on their "
  "structure. Covering the hand traps it: they cannot let go without "
  "fighting your two hands. The step-back adds distance and rotation, "
  "converting their forward commitment into the bending force of the wrist "
  "lock. The grab meant to control you becomes the lever you control them "
  "with.",
 "key_points": [
  "Otdong japgi means clothing grab: the most common confrontation opener.",
  "Cover the grabbing hand instantly: trap it before it can release.",
  "The grab is a gift: their committed hand becomes your lock handle.",
  "Step back and turn: distance plus rotation bends the wrist.",
  "Two-handed grabs break with a weight drop plus an outward circle."],
 "requirements": [
  "A sturdy training uniform or old shirt that can be grabbed.",
  "Wrist lock proficiency: the defense ends in sonmok kkokki.",
  "A partner grabbing with honest commitment.",
  "Mat space: the defense ends in a guided takedown."],
 "standards": [
  "The cover lands before any lock begins: never chase a free hand.",
  "Pressure stays controlled: the tap ends it.",
  "Both partners' clothing grips stay at the lapel, never the throat."],
 "citations": [CIT_SHAW, CIT_KIMM],
 "sig_lens":
  "Signature Hapkido Method: the lapel defense is the Signature turning - "
  "the covenant that what is seized becomes the seizer's leash. He teaches "
  "the cover as the oath's first word: the hand is trapped the instant it "
  "grasps. The student learns the Signature reversal - every attack "
  "carries its own answer, and the grab meant to dominate becomes the "
  "handle of its own undoing.",
},
{
 "key": "eokkaemechi", "name": "Shoulder Throw (Eokkae Mechi)",
 "group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
 "description":
  "The shoulder throw (eokkae mechi) loads the attacker onto your back "
  "and throws them over your shoulder - hapkido's classic big throw, "
  "combining the circular principle with a low, powerful base. HOW TO DO "
  "IT. 1. Your partner pushes or grabs you; you step deep inside, turning "
  "your back to them while pulling their arm across your shoulder. 2. "
  "Sink into a deep horse-like stance, hips below their hips - your back "
  "and shoulder become the loading platform. 3. Keep their arm trapped "
  "tightly across your chest with both hands; your body contact must be "
  "hip-to-hip, no gap. 4. Straighten your legs explosively while pulling "
  "their arm down and turning your shoulder - their body rolls over your "
  "shoulder. 5. Guide their fall: keep hold of the arm and direct them to "
  "the mat where they execute their breakfall. 6. Drill: practice the "
  "entry and load (steps 1-3) repeatedly without the throw, then add the "
  "full throw at low speed with a skilled falling partner.",
 "how_it_works":
  "The throw is a wheel: your shoulder is the axle and the attacker's body "
  "is the rim. Getting your hips below theirs gives you the mechanical "
  "advantage of a lever lifting from underneath; straightening your legs "
  "supplies the lifting force; pulling the arm down and turning supplies "
  "the rotation. The attacker's own forward push loads them onto the "
  "platform - you add the wheel's turn. Hip-to-hip contact is essential: "
  "any gap becomes a space they can resist through.",
 "key_points": [
  "Eokkae mechi means shoulder throw: the classic loading throw.",
  "Hips below their hips: the low base is the whole technique.",
  "Hip-to-hip contact with no gap: the platform must be solid.",
  "Legs lift, arms pull down, shoulder turns: the wheel's three motions.",
  "Guide the fall: keep the arm and direct the breakfall."],
 "requirements": [
  "Advanced breakfall skill in the throwing partner.",
  "A thick mat: big throws need real padding.",
  "Horse stance strength: the load sits on your legs.",
  "Instructor supervision for all throwing practice."],
 "standards": [
  "No throwing without a skilled falling partner.",
  "Entry practiced to smoothness before any full throw.",
  "The thrower keeps hold and guides: never launch and abandon."],
 "citations": [CIT_TED, CIT_BIO],
 "sig_lens":
  "Signature Hapkido Method: the shoulder throw is the Signature wheel - "
  "the covenant of the circle made into a throw. He teaches the load as "
  "the oath accepted: the attacker's force steps willingly onto the "
  "platform, and the turn keeps the promise. The hips-below-hips rule is "
  "the Signature humility - the thrower goes low so the technique may go "
  "high, and the wheel turns because the root is deep.",
},
{
 "key": "heorimechi", "name": "Hip Throw (Heori Mechi)",
 "group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
 "description":
  "The hip throw (heori mechi) pivots the attacker over your hip - faster "
  "to enter than the shoulder throw and the workhorse takedown of hapkido "
  "sparring. HOW TO DO IT. 1. As your partner pushes or steps in, step "
  "across their body with your near foot, turning your back to them. 2. "
  "Pull their arm and upper body tightly onto your hip - your hip bone "
  "sits in the crease of their hip, contact glued. 3. Sink your weight, "
  "bending your knees, so your center drops below theirs. 4. Pull their "
  "upper body forward and down while popping your hips up and around - "
  "their body pivots over your hip like a wheel over an axle. 5. Continue "
  "the pull to guide them to the mat into their breakfall. 6. Drill: "
  "enter and glue the hip (steps 1-2) ten times without throwing, feeling "
  "for the exact hip-to-hip seat, then add the full throw slowly.",
 "how_it_works":
  "The hip is the fulcrum of a first-class lever: the attacker's upper "
  "body is the load arm and your pulling hands supply the effort. Dropping "
  "your center below theirs means the lever lifts from underneath, where "
  "resistance is weakest. The hip pop adds a sharp upward impulse at the "
  "fulcrum itself, which is why a well-timed hip throw feels effortless - "
  "the geometry does the lifting.",
 "key_points": [
  "Heori mechi means hip throw: the fast pivot takedown.",
  "Hip bone to hip crease: the seat must be glued, no gap.",
  "Drop your center below theirs before the pop.",
  "Pull the top down while the hips pop up: the lever's two motions.",
  "Drill the entry alone: the seat decides the throw."],
 "requirements": [
  "Skilled falling partner and thick mats.",
  "Shoulder throw familiarity: the entries rhyme.",
  "Hip mobility and leg strength for the drop and pop.",
  "Instructor supervision for throwing practice."],
 "standards": [
  "Hip-to-hip seat verified before any full throw.",
  "The thrower guides the fall through the pull.",
  "No hip throws on partners who cannot breakfall."],
 "citations": [CIT_TED, CIT_BIO],
 "sig_lens":
  "Signature Hapkido Method: the hip throw is the Signature pivot - the "
  "covenant balanced on a single point. He teaches the glued hip as the "
  "oath's seal: two centers become one, and the turn decides everything. "
  "The pop is the Signature exclamation - the small sharp truth that "
  "geometry outlifts muscle. The student who seats the hip perfectly has "
  "signed the throw before it begins.",
},
{
 "key": "palkkumchichigi", "name": "Elbow Strike (Palkkumchi Chigi)",
 "group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
 "description":
  "The elbow strike (palkkumchi chigi) is hapkido's close-range weapon: "
  "the hard point of the elbow driven by full torso rotation, used when "
  "the attacker is too close for punches or kicks. HOW TO DO IT. 1. From "
  "a close stance, raise the striking elbow with the hand held loosely "
  "near the opposite shoulder. 2. Whip the torso around, driving the elbow "
  "horizontally across in an arc, striking with the bony point. 3. A "
  "second form drives the elbow upward under the chin line in training on "
  "pads; a third drops it downward. 4. Step into the strike: the body "
  "weight must travel with the elbow. 5. Keep the striking hand relaxed - "
  "tension in the hand slows the whip. 6. Drill: practice all three arcs "
  "(horizontal, upward, downward) against a heavy bag or elbow pad, "
  "focusing on the torso whip rather than arm muscle.",
 "how_it_works":
  "The elbow is short, hard, and close to the body's rotational axis, so "
  "torso rotation accelerates it to high speed over a short distance - "
  "this is why elbow strikes hit so hard in the clinch. The bony point "
  "concentrates force on a tiny area, and the relaxed hand keeps the "
  "forearm loose so the whip stays fast. Stepping in adds the body's mass "
  "to the short lever.",
 "key_points": [
  "Palkkumchi chigi means elbow strike: the close-range weapon.",
  "Three arcs: horizontal, upward, downward.",
  "Torso rotation drives it: the arm only delivers.",
  "Striking hand stays relaxed for maximum whip speed.",
  "Step in: body weight travels with the elbow."],
 "requirements": [
  "A heavy bag or dedicated elbow pad for contact.",
  "Clinch-range partner drills at controlled speed.",
  "Torso mobility warm-up: the whip needs a loose spine.",
  "Mouthguard for any close-range partner work."],
 "standards": [
  "Contact with the bony elbow point only.",
  "Every strike visibly rotates the torso.",
  "Control in partner drills: touch, never smash."],
 "citations": [CIT_SHAW, CIT_BIO],
 "sig_lens":
  "Signature Hapkido Method: the elbow strike is the Signature hinge-"
  "hammer - the covenant of closeness. He teaches that when distance "
  "collapses, the circle tightens but never breaks: the elbow is the "
  "circle drawn small and fast. The relaxed hand is the Signature trust - "
  "looseness where tension would lie, speed where muscle would slow, the "
  "body's honest short answer.",
},
{
 "key": "mureupchagi", "name": "Knee Strike (Mureup Chagi)",
 "group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
 "description":
  "The knee strike (mureup chagi) drives the knee upward into the "
  "attacker's midsection at clinch range - the natural partner of the "
  "elbow strike, and the technique that teaches pulling an opponent into "
  "the strike. HOW TO DO IT. 1. In the clinch, control your partner's "
  "head or shoulders with both hands, keeping your own guard tight. 2. "
  "Pull their upper body down and toward you as you drive your knee "
  "sharply upward - the pull and the knee travel toward each other. 3. "
  "Strike with the bony top of the knee, hips thrusting forward at "
  "contact. 4. Rise onto the ball of the support foot for extra height "
  "and drive. 5. Rechamber the knee immediately and reset the clinch "
  "control. 6. Drill: practice the pull-and-knee timing on a heavy bag "
  "held at waist height, then with a partner holding a belly pad, "
  "focusing on the two-way collision of pull and drive.",
 "how_it_works":
  "The knee strike is a collision in two directions: pulling the target "
  "down into the rising knee doubles the impact speed, the same principle "
  "as two cars meeting head-on. The knee is a large, hard striking surface "
  "backed directly by the hip's powerful extensors, and the clinch control "
  "keeps the target from riding away with the blow. Rising onto the ball "
  "of the support foot adds the calf's push to the hip's drive.",
 "key_points": [
  "Mureup chagi means knee strike: the clinch-range collision.",
  "Pull the target down as the knee drives up: the two-way collision.",
  "Strike with the bony top of the knee, hips thrusting forward.",
  "Rise onto the ball of the support foot for height and drive.",
  "Rechamber fast and reset the clinch: the knee is one beat of the exchange."],
 "requirements": [
  "A belly pad or heavy bag for contact practice.",
  "A partner trained in clinch control for pad holding.",
  "Hip flexor warm-up: knees work hard.",
  "Mouthguard for clinch-range partner drills."],
 "standards": [
  "Pull and knee fire together: no pulling without striking.",
  "Control the partner's posture in the clinch at all times.",
  "Partner drills stay at pad-contact level: no free knees to the body."],
 "citations": [CIT_SHAW, CIT_BIO],
 "sig_lens":
  "Signature Hapkido Method: the knee strike is the Signature meeting - "
  "the covenant where pull and drive keep the same appointment. He teaches "
  "the two-way collision as the oath's handshake: the hands bring the "
  "target, the knee keeps the promise. The clinch is the circle closed to "
  "arm's length, and within it the knee speaks the Signature short word "
  "with the whole body's weight behind it.",
},
{
 "key": "darigeolgo", "name": "Leg Hook Takedown (Dari Geolgo)",
 "group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
 "description":
  "The leg hook takedown (dari geolgo) combines a hand pull with a leg "
  "hook behind the attacker's knee: the classic hapkido takedown that "
  "bridges throws and sweeps. HOW TO DO IT. 1. As your partner steps "
  "forward, step to the outside of their lead leg. 2. Hook your foot "
  "behind their ankle or lower shin, your leg making contact like a hook. "
  "3. Simultaneously pull their upper body toward you and down with both "
  "hands on their arm or clothing. 4. Lift slightly with the hooked leg "
  "while driving their top backward - the base is hooked while the top is "
  "driven, and they fall. 5. Keep hold and guide them to the mat into "
  "their breakfall. 6. Drill: a partner walks toward you; you time the "
  "hook to their stepping leg, starting at walking speed with the pull "
  "doing most of the work, adding hook speed as timing improves.",
 "how_it_works":
  "The hooked leg blocks the foot from stepping to recover balance while "
  "the hand pull moves the center of gravity past the blocked base - a "
  "pincer on stability from both ends. Hooking behind the knee is "
  "especially effective because the knee cannot bend backward to absorb "
  "the hook. Timing the hook to the stepping leg means the foot is in the "
  "air or lightly loaded, so minimal force completes the takedown.",
 "key_points": [
  "Dari geolgo means leg hooking: hook the base, drive the top.",
  "Hook behind the ankle or shin as they step: time the stepping leg.",
  "Hands pull the upper body toward and down at the same instant.",
  "The knee cannot bend backward: the hook behind it cannot be absorbed.",
  "Guide the fall: keep hold through the breakfall."],
 "requirements": [
  "Breakfall-proficient partner and mat space.",
  "Leg sweep proficiency: the timing transfers directly.",
  "Ankle and knee warm-up for hooking legs.",
  "Instructor supervision for takedown practice."],
 "standards": [
  "Hook at ankle or shin: never hook the knee joint itself.",
  "Timing over force: the stepping leg needs only a light hook.",
  "The partner's fall is always guided and safe."],
 "citations": [CIT_TED, CIT_BIO],
 "sig_lens":
  "Signature Hapkido Method: the leg hook is the Signature pincer - the "
  "covenant that takes the top and the base in one motion. He teaches the "
  "hook as the circle's lower arc and the pull as its upper: the two arcs "
  "meet around the partner's balance and close it. The student who times "
  "the stepping leg has learned the Signature listening - to feel the "
  "rhythm of the walk and answer exactly on the beat.",
},
{
 "key": "mokjoreugi", "name": "Front Choke Defense (Mok Joreugi)",
 "group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
 "description":
  "The front choke defense (mok joreugi) answers a two-handed front "
  "strangle: the most urgent self-defense in the compounded tier, because "
  "a choke must be answered in seconds. HOW TO DO IT. 1. The instant the "
  "hands close on your throat, tuck your chin hard and raise your "
  "shoulders to protect the airway. 2. Step back with one foot, turning "
  "your body sideways to reduce the target. 3. Bring both your hands up "
  "inside their arms and chop downward and outward across their forearms "
  "in a sharp V - this is the pluck that breaks the choke. 4. The moment "
  "the grip breaks, strike: a palm strike or knee to create distance in "
  "training on pads. 5. Follow with a wrist lock on one of their hands "
  "(sonmok kkokki) to control them. 6. Drill: the partner applies a slow, "
  "loose choke; you practice the chin-tuck, step, and pluck until it is "
  "one motion. Speed comes only after the motion is clean - this defense "
  "is never practiced at full force on the throat.",
 "how_it_works":
  "The chin tuck and raised shoulders mechanically narrow the airway's "
  "exposure and buy seconds. The pluck works because the choke's strength "
  "is in the fingers and thumbs pressing inward: a sharp downward-outward "
  "chop across the forearms attacks the wrists' leverage at their weakest "
  "angle, peeling the hands off. Stepping back and turning removes the "
  "throat from the line of the choke while loading the body for the "
  "counter. The immediate follow-up strike matters: a broken choke means "
  "nothing if the attacker simply re-grabs.",
 "key_points": [
  "Mok joreugi means throat wringing: answer a choke in seconds.",
  "Chin tucks and shoulders rise instantly: protect the airway first.",
  "The pluck: both hands chop down and out across their forearms in a V.",
  "Step back and turn: remove the throat from the line.",
  "Break, strike, lock: the defense is three beats, not one."],
 "requirements": [
  "A partner who applies only slow, loose practice chokes.",
  "Throat safety briefing before any choke practice.",
  "Wrist lock and palm strike proficiency for the follow-up.",
  "Instructor supervision mandatory: chokes are high-risk drills."],
 "standards": [
  "Practice chokes stay loose: no real pressure on the throat, ever.",
  "The tap or a verbal stop ends the drill instantly.",
  "Speed only after the motion is clean: never rush a choke defense."],
 "citations": [CIT_SHAW, CIT_KIMM],
 "sig_lens":
  "Signature Hapkido Method: the choke defense is the Signature urgency - "
  "the covenant that some answers cannot wait. He teaches the chin-tuck "
  "as the body's first oath to itself: protect the breath, and the breath "
  "will protect you. The pluck is the Signature V - the open hand of "
  "defense drawn sharp - and the three beats (break, strike, lock) are the "
  "oath kept in full: survive, create distance, control.",
},
# ---------------------------------------------------------------- advanced
{
 "key": "gyeonghyeolchigi", "name": "Pressure Point Strikes (Gyeonghyeol Chigi)",
 "group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
 "description":
  "Pressure point strikes (gyeonghyeol chigi) target the body's sensitive "
  "points - nerve clusters and vulnerable anatomy - where a light, precise "
  "strike produces a large effect. This is advanced material: it demands "
  "precision, control, and an instructor's supervision. HOW TO DO IT. 1. "
  "Learn the training-safe points first: the temple region, the side of "
  "the neck, the solar plexus, the floating ribs, and the inner thigh - "
  "all practiced only as light touches on a cooperative partner. 2. Strike "
  "with the fingertip, knuckle, or knife-hand edge, using a short, sharp "
  "motion with no wind-up. 3. Accuracy is everything: a pressure point "
  "struck one inch off is just a touch. Practice by touching the point "
  "lightly on a partner, eyes open, until you can find it without "
  "looking. 4. Combine with hapkido's locks: many joint locks finish by "
  "pressing a point to deepen control. 5. Breathing: the sharp exhale "
  "focuses the strike exactly as with any other technique. 6. Drill: "
  "partner points to a named point; you touch it lightly with the correct "
  "striking surface, building a mental map of the body's sensitive "
  "geography. Dangerous points (throat, eyes, groin) are studied "
  "theoretically only - never struck in practice.",
 "how_it_works":
  "Pressure points work through anatomy, not mysticism: striking a nerve "
  "cluster or a thinly-padded bone produces pain and reflexive flinching "
  "far out of proportion to the force, because the nervous system "
  "amplifies signals from vulnerable areas. The short, sharp strike "
  "delivers its energy before the target's muscles can brace. Combined "
  "with a joint lock, point pressure multiplies control: the lock bends "
  "the joint while the point convinces the nervous system to comply.",
 "key_points": [
  "Gyeonghyeol chigi means vital-point striking: precision over power.",
  "Anatomy, not mysticism: nerve clusters and thin padding amplify the effect.",
  "One inch off is a miss: accuracy is the entire technique.",
  "Dangerous points are studied in theory only, never struck.",
  "Locks plus points multiply: the joint bends, the point persuades."],
 "requirements": [
  "An instructor's direct supervision: no solo point-strike practice.",
  "A cooperative partner and explicit consent for every touch.",
  "Full mastery of the basic strikes first: points are refinements.",
  "A first-aid kit and a clear stop signal for all advanced drills."],
 "standards": [
  "Light touches only in practice: never strike a point with force.",
  "Eyes, throat, and groin are never practice targets.",
  "Any discomfort stops the drill immediately."],
 "citations": [CIT_TED, CIT_KIMM],
 "sig_lens":
  "Signature Hapkido Method: the pressure point is the Signature whisper - "
  "the covenant spoken so precisely it needs no force. He teaches the "
  "body's sensitive geography as the Signature map: every point a small "
  "seal where a light touch keeps a large promise. The student who maps "
  "the points learns the Signature restraint - that the most advanced "
  "technique is the one that controls without harm, the whisper that "
  "moves what shouting cannot.",
},
{
 "key": "dwiddollyeo", "name": "Spinning Back Kick (Dwi Dollyeo Chagi)",
 "group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
 "description":
  "The spinning back kick (dwi dollyeo chagi) adds a full spin to the back "
  "kick: the body's rotation multiplies the heel's speed, making it one of "
  "hapkido's most powerful kicks. HOW TO DO IT. 1. From a fighting stance, "
  "step the front foot across and begin turning the body away from the "
  "target, spotting over the shoulder. 2. Continue the spin on the ball of "
  "the support foot, lifting the kicking knee high as the body turns a "
  "full 360 degrees. 3. At the moment the back faces the target, drive the "
  "heel straight back along the centerline, torso leaning forward. 4. "
  "Strike with the heel, then rechamber and complete the turn to face the "
  "target in stance. 5. The spin and the kick are one motion: hesitation "
  "between them kills the power. 6. Drill: practice the spin alone until "
  "you can turn 360 degrees and stop balanced; then add the heel drive "
  "against a heavy bag, starting at half speed.",
 "how_it_works":
  "The spin stores angular momentum in the rotating body; when the leg "
  "extends at the back-facing moment, that rotation whips the heel "
  "through at far higher speed than a standing back kick could produce. "
  "The straight heel line keeps the force concentrated, and the forward "
  "torso lean stacks body weight behind it. Spotting over the shoulder "
  "keeps the kick aimed: the eyes find the target mid-spin so the heel "
  "arrives on line.",
 "key_points": [
  "Dwi dollyeo chagi means spinning back kick: rotation multiplies the heel.",
  "Spin on the ball of the support foot: a full, committed 360 degrees.",
  "The heel drives straight back at the back-facing moment: no arc.",
  "Spot over the shoulder mid-spin: the eyes aim the heel.",
  "Spin and kick are one motion: hesitation kills the power."],
 "requirements": [
  "Back kick proficiency: the spin adds to a solid dwi chagi.",
  "A heavy bag for the full-power drive.",
  "Open floor space: the spin needs a clear radius.",
  "Ankle and knee warm-up: spinning loads the support leg."],
 "standards": [
  "Full balance after the spin: no stumbling through the finish.",
  "Heel contact on the centerline: never a wild sideways swing.",
  "Half speed until the spin-kick timing is clean."],
 "citations": [CIT_SHAW, CIT_BIO],
 "sig_lens":
  "Signature Hapkido Method: the spinning back kick is the Signature "
  "cyclone - the covenant of the full circle kept at speed. He teaches the "
  "360 degrees as the oath's complete seal: the body turns its back on "
  "fear and the heel keeps the promise. The spot over the shoulder is the "
  "Signature vigilance - even mid-storm, the eyes hold the line, and the "
  "circle, fully drawn, delivers its most powerful word.",
},
{
 "key": "twieoapchagi", "name": "Jump Front Kick (Twieo Ap Chagi)",
 "group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
 "description":
  "The jump front kick (twieo ap chagi) launches the whole body into the "
  "air to deliver the front kick: hapkido's flying kick, combining "
  "elevation with the straight-kick line. HOW TO DO IT. 1. From a fighting "
  "stance, take a short running or skipping step to load the legs. 2. "
  "Drive off the support leg, jumping upward and slightly forward, "
  "lifting the kicking knee to full chamber while airborne. 3. At the "
  "peak of the jump, snap the lower leg out, striking with the ball of the "
  "foot. 4. Rechamber in the air and land on the kicking foot first, "
  "then the other foot, sinking softly into stance with bent knees. 5. "
  "Keep the guard up through the entire flight. 6. Drill: practice the "
  "jump and chamber without the kick until landings are silent and "
  "balanced; then add the kick against a hand-held pad at chest height, "
  "starting with low jumps.",
 "how_it_works":
  "The jump adds the body's falling and rising momentum to the kick: at "
  "the peak, the leg snaps out while the body is still rising, so the "
  "foot arrives with the jump's energy behind it. Elevation also clears "
  "guards and reaches high targets. Landing on the kicking foot first "
  "with bent knees lets the legs absorb the landing progressively - stiff "
  "landings are how jump kicks injure knees.",
 "key_points": [
  "Twieo ap chagi means jumping front kick: elevation plus the straight line.",
  "Jump, chamber fully in the air, snap at the peak.",
  "Strike with the ball of the foot, toes pulled back.",
  "Land kicking foot first, knees bent, silently.",
  "Guard stays up through the entire flight."],
 "requirements": [
  "Front kick mastery: the air kick is only as good as the ground kick.",
  "Padded mat for jump practice: landings must be forgiven.",
  "Leg strength and ankle stability for takeoff and landing.",
  "A partner holding a pad at chest height."],
 "standards": [
  "Silent, balanced landings before any pad contact.",
  "Full chamber in the air: no half-chambered flying kicks.",
  "Low jumps first: height builds with control."],
 "citations": [CIT_SHAW, CIT_BIO],
 "sig_lens":
  "Signature Hapkido Method: the jump front kick is the Signature flight - "
  "the covenant that leaves the ground without leaving the art. He teaches "
  "the takeoff as the oath's leap of commitment and the silent landing as "
  "its kept promise: power given, control returned. The guard held high "
  "through the flight is the Signature vigilance - even airborne, defense "
  "is never abandoned, and the circle, drawn in the air, lands complete.",
},
{
 "key": "dandodaebi", "name": "Knife Defense (Dando Daebi)",
 "group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
 "description":
  "Knife defense (dando daebi) is hapkido's weapon-defense foundation "
  "(mu gi sul): how to survive an attacker with a blade. It is practiced "
  "only with rubber or wooden training knives, under an instructor, and "
  "its first lesson is that the best defense is distance and escape. HOW "
  "TO DO IT. 1. Against a straight stab: step sharply offline at 45 "
  "degrees as the blade comes, letting it pass where you were. 2. "
  "Simultaneously deflect the attacking forearm with your knife-hand, "
  "never grabbing at the blade itself. 3. Control the weapon arm: pin "
  "their forearm with both hands, keeping the blade pointed away from "
  "your body. 4. Apply a wrist lock (sonmok kkokki) to the weapon hand "
  "and guide them down, keeping the blade controlled throughout. 5. "
  "Against a slash: step inside the arc's start, jam the attacking arm "
  "at the elbow before the swing develops, and lock it. 6. Drill: with a "
  "rubber knife and full protective mindset, practice at quarter speed, "
  "with the rule that touching the blade with your hands is an instant "
  "failure - control the arm, never chase the knife.",
 "how_it_works":
  "A knife extends the attacker's reach but commits their arm to a "
  "predictable line: stepping offline removes the target from that line "
  "while the deflection redirects the committed arm. Controlling the "
  "forearm rather than the blade works because the arm is the larger, "
  "slower, safer handle - the blade is fast and unforgiving. The wrist "
  "lock on the weapon hand attacks the grip's weakest mechanics: bend the "
  "wrist and the hand must open. Everything about knife defense accepts "
  "that one mistake is costly, so the system layers offline movement, "
  "deflection, arm control, and the lock.",
 "key_points": [
  "Dando daebi means short-sword preparation: the blade defense.",
  "Step offline first: the best defense is not being where the blade goes.",
  "Control the forearm, never chase the blade.",
  "Wrist lock the weapon hand: bend the wrist and the grip must open.",
  "Train with rubber knives only: one mistake with steel is final."],
 "requirements": [
  "Rubber or wooden training knives only: never steel.",
  "Instructor supervision mandatory for all weapon drills.",
  "Wrist lock and offline footwork mastery first.",
  "A clear safety brief: touching the blade is instant failure."],
 "standards": [
  "Quarter speed until every motion is clean and controlled.",
  "The blade is tracked with the eyes at all times.",
  "Escape is always the preferred outcome: disengage when possible."],
 "citations": [CIT_TED, CIT_KIMM],
 "sig_lens":
  "Signature Hapkido Method: knife defense is the Signature gravity - the "
  "covenant that treats the blade with absolute seriousness. He teaches "
  "the offline step as the oath's first and wisest word: the body that is "
  "not there cannot be cut. The forearm control is the Signature grip on "
  "reality - hold what can be held, never chase what cannot - and the "
  "wrist lock that opens the weapon hand is the circle closing the "
  "argument without a drop of blood.",
},
{
 "key": "jangbongdaebi", "name": "Long Staff Defense (Jangbong Daebi)",
 "group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
 "description":
  "Long staff defense (jangbong daebi) answers an attacker swinging a "
  "staff, stick, or bat: the principles of closing distance and jamming "
  "the swing. HOW TO DO IT. 1. As the attacker raises the staff for a "
  "downward swing, step explosively inside - toward them, not away - "
  "closing past the staff's power zone. 2. Raise your forearm to shield "
  "while your other hand jams their lead arm at the elbow, killing the "
  "swing's leverage. 3. Control the staff arm with both hands and apply "
  "an elbow or wrist lock to strip the weapon. 4. Against a thrust: step "
  "offline and deflect the staff's tip past you with a knife-hand, then "
  "close and lock as before. 5. Never back straight away from a staff: "
  "the weapon's reach beats your retreat. 6. Drill: with a padded staff "
  "at quarter speed, practice the explosive entry until stepping in feels "
  "safer than backing up.",
 "how_it_works":
  "A staff is a long lever: its power lives in the arc of the swing, "
  "greatest at the tip and weakest near the hands. Stepping inside the "
  "arc enters the dead zone where the lever cannot generate force - the "
  "same reason a boxer crowds a long-armed puncher. Jamming the elbow "
  "stops the swing's fulcrum from moving. The drill rewires the instinct "
  "to flee, which is exactly what the staff wants.",
 "key_points": [
  "Jangbong daebi means long-staff preparation: answer the swinging weapon.",
  "Step inside the arc: the staff's dead zone is near the hands.",
  "Never retreat straight back: the reach beats the retreat.",
  "Jam the elbow to kill the swing's leverage.",
  "Lock the weapon arm and strip the staff."],
 "requirements": [
  "Padded training staffs only.",
  "Instructor supervision for all weapon drills.",
  "Explosive entry footwork: the step-in must be committed.",
  "Elbow and wrist lock proficiency for the strip."],
 "standards": [
  "Quarter speed until the entry is instinctive.",
  "The head is guarded during every entry.",
  "Disengage and create distance once the weapon is controlled."],
 "citations": [CIT_TED, CIT_KIMM],
 "sig_lens":
  "Signature Hapkido Method: staff defense is the Signature courage - the "
  "covenant to step toward what others flee. He teaches the dead zone as "
  "the circle's quiet center: the storm's edge is violent, its heart is "
  "still, and the fighter who enters the stillness owns the weapon. The "
  "entry is the Signature vow kept at speed - forward, not back - and the "
  "strip is the circle relieving the attacker of the argument.",
},
{
 "key": "danbongsul", "name": "Short Stick Techniques (Danbong Sul)",
 "group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
 "description":
  "Short stick techniques (danbong sul) are hapkido's own weapon art: the "
  "danbong, a stick roughly the length of the forearm, used for strikes, "
  "locks, and throws. It extends every empty-hand technique the student "
  "already knows. HOW TO DO IT. 1. Grip the danbong in the center with a "
  "firm fist, one end protruding past the thumb side and one past the "
  "little-finger side. 2. Basic strikes: snap the wrist to strike with "
  "either protruding end - downward, upward, and horizontal arcs, exactly "
  "like the knife-hand strike paths. 3. The lock amplifier: lay the stick "
  "across the partner's wrist or forearm during any wrist lock - the "
  "stick becomes a lever that multiplies the lock's pressure with a "
  "fraction of the effort. 4. The throw assist: hook the stick behind the "
  "partner's neck or arm during throws to guide the fall. 5. Blocks: "
  "meet an incoming strike with the stick's length, protecting the "
  "forearm. 6. Drill: practice the three strike arcs against a bag, then "
  "apply the stick to the basic wrist lock on a partner at slow speed, "
  "feeling how the lever multiplies control.",
 "how_it_works":
  "The danbong is a force multiplier in both directions: as a striker, "
  "it concentrates the arm's motion onto a small, hard tip moving at "
  "wrist-snap speed; as a lock aid, it lengthens the lever arm on the "
  "joint, so the same hand force produces far greater torque. Because its "
  "length matches the forearm, it moves as a natural extension of the "
  "arm's own mechanics - every empty-hand technique the student knows "
  "transfers directly, amplified.",
 "key_points": [
  "Danbong sul means short-stick art: the forearm-length weapon.",
  "Center grip: both ends protrude as striking tips.",
  "Strike arcs mirror the knife-hand paths: down, up, horizontal.",
  "The stick multiplies locks: a longer lever on the same joint.",
  "Empty-hand techniques transfer directly, amplified."],
 "requirements": [
  "A rattan or hardwood danbong of forearm length.",
  "A heavy bag for strike practice.",
  "Wrist lock proficiency: the stick amplifies known locks.",
  "A partner and mats for slow lock-amplifier drills."],
 "standards": [
  "Strikes practiced on bags and pads, never on partners.",
  "Lock amplifiers applied at a fraction of normal pressure.",
  "The stick is always under control: no wild swings."],
 "citations": [CIT_TED, CIT_KIMM],
 "sig_lens":
  "Signature Hapkido Method: the danbong is the Signature extension - the "
  "covenant that the hand's reach may grow without the hand's honesty "
  "changing. He teaches the stick as the circle given a handle: the same "
  "arcs, the same locks, the same oath, now written larger. The lever "
  "that multiplies the lock is the Signature arithmetic made visible - "
  "small truth, long arm, complete control.",
},
{
 "key": "geomsul", "name": "Sword Basics (Geom Sul)",
 "group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
 "description":
  "Sword basics (geom sul) introduce the Korean straight sword as hapkido's "
  "most demanding weapon study: cutting mechanics, drawing, and the "
  "discipline the blade demands. Practice uses wooden or blunt training "
  "swords only. HOW TO DO IT. 1. Grip: both hands on the handle, right "
  "hand at the guard, left at the pommel, firm but not white-knuckled. 2. "
  "Stance: a deep front stance, the sword held at the centerline. 3. The "
  "downward cut: raise the sword overhead and cut straight down, letting "
  "the blade's weight do the work, finishing with the tip pointing at the "
  "target line - the cut is a guided fall, not a muscle chop. 4. The "
  "horizontal cut: draw the blade across at shoulder height, hips rotating "
  "with the cut. 5. The thrust: step forward and extend the sword straight "
  "along the centerline. 6. Drawing and sheathing are practiced slowly: "
  "the blade leaves and returns along the same line, never waved. 7. "
  "Drill: cut rolled straw mats or paper targets to learn the blade's "
  "true edge alignment - a correct cut slices cleanly, a twisted cut tears.",
 "how_it_works":
  "A sword cut is a falling lever guided by the hands: the blade's own "
  "weight and the arc's speed do the cutting, which is why relaxed "
  "shoulders cut better than muscled ones. Edge alignment decides "
  "everything - the edge must travel exactly in the plane of the swing, "
  "or the flat of the blade slaps instead of cuts. The deep stance roots "
  "the cut's power in the floor, and the draw-and-sheathe discipline "
  "trains the respect a live blade requires.",
 "key_points": [
  "Geom sul means sword art: the most demanding weapon study.",
  "The cut is a guided fall: let the blade's weight work.",
  "Edge alignment decides the cut: the edge travels in the swing's plane.",
  "Deep stance roots every cut in the floor.",
  "Wooden or blunt trainers only: the live blade is never a practice tool."],
 "requirements": [
  "A wooden or blunt aluminum training sword.",
  "A clear, open practice space with no bystanders.",
  "Instructor supervision: sword study is never solo.",
  "Rolled mats or paper targets for cutting practice."],
 "standards": [
  "No live blades in practice, without exception.",
  "Draw and sheathe slowly along one line: never wave the blade.",
  "Full protective awareness: the practice area is cleared and guarded."],
 "citations": [CIT_TED, CIT_KIMM],
 "sig_lens":
  "Signature Hapkido Method: the sword is the Signature reckoning - the "
  "covenant at its most serious. He teaches geom sul as the art's final "
  "examination of character: the blade answers only the disciplined hand, "
  "and the guided fall of the cut is the Signature humility - let the "
  "weight do the work, let the line stay true. The student who draws "
  "slowly has understood that the sword's first lesson is restraint.",
},
{
 "key": "gyeokpa", "name": "Breaking (Gyeokpa)",
 "group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
 "description":
  "Breaking (gyeokpa) is hapkido's power demonstration and test: "
  "shattering boards, bricks, or tiles with strikes and kicks to prove "
  "that technique, not brute strength, generates power. HOW TO DO IT. 1. "
  "Start with a single thin pine board held firmly by a partner at both "
  "ends - the holder's grip must be rock-solid. 2. Choose a mastered "
  "technique: the palm strike, knife-hand, or front kick are the first "
  "breaks. 3. Aim through the board: pick a point six inches past its "
  "surface and strike that point, following through completely. 4. Exhale "
  "sharply and tighten at the instant of contact, exactly as in basic "
  "technique. 5. Speed, not muscle: a fast, relaxed technique with full "
  "follow-through breaks; a tense, muscled push does not. 6. Progress "
  "slowly: one board, then two, then thicker materials, with an instructor "
  "judging readiness. 7. Safety: the holder wears protection and stands "
  "aside from the strike's path; failed breaks stop the session for "
  "technique review, never repeated pounding.",
 "how_it_works":
  "Breaking is applied physics: the board fails when the strike delivers "
  "enough focused energy to exceed the wood's breaking strength along its "
  "grain. Speed matters more than mass because kinetic energy grows with "
  "the square of velocity - a fast, relaxed strike carries far more "
  "breaking energy than a slow, tense shove. Aiming through the target "
  "prevents the instinctive deceleration at the surface, and the sharp "
  "exhale braces the striking structure at the critical instant. The "
  "holder's firm grip matters: a loose board rides with the blow and "
  "absorbs the energy.",
 "key_points": [
  "Gyeokpa means breaking: the test of technique-made power.",
  "Aim six inches past the surface: follow through completely.",
  "Speed beats muscle: energy grows with the square of velocity.",
  "Start with one thin pine board: progress only with instructor approval.",
  "Failed breaks stop the session: review technique, never pound."],
 "requirements": [
  "Pine boards of appropriate thinness for beginners.",
  "A trained holder with protective gear.",
  "A mastered striking technique: never break with a new technique.",
  "An instructor to judge readiness and supervise."],
 "standards": [
  "One board first: no skipping the progression.",
  "The holder's safety is checked before every attempt.",
  "No repeated pounding on failed breaks: stop and review."],
 "citations": [CIT_SHAW, CIT_BIO],
 "sig_lens":
  "Signature Hapkido Method: breaking is the Signature proof - the "
  "covenant made visible in shattered pine. He teaches gyeokpa as the "
  "art's honest examination: the board cannot be flattered or fooled, it "
  "answers only true technique. The aim-through is the Signature "
  "commitment - strike past the obstacle, not at it - and the student who "
  "breaks cleanly has signed the final oath: power is technique kept "
  "perfectly, nothing more.",
},
]
