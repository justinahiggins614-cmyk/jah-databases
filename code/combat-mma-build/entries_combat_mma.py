#!/usr/bin/env python3
"""Entries for the Mixed Martial Arts Combat Database (combat batch 2).

Verified 2026-10-17: RAW SWEEP over the full manifest (2,410 databases)
plus every shard index title in jah-databases-data-1 (all index files,
zero hits for CBMMA id prefixes): zero 'combat-mma*' slugs/names and zero
title collisions for all 68 candidate titles (34 public + 34 Signature
Edition) against the whole-system exact dedupe gate. The 'summarization-pairs'
slug is a substring false positive ('mma' inside 'summarization'), not a
combat database. No existing boxing/fighting/wrestling database carries
these titles - BUILD NEW is the verdict.

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced): fundamentals of stance,
footwork, striking, defense, takedowns, and ground survival ->
compounded striking wrestling and submission technique -> advanced
integration: transitions, setups, cage craft, and fight planning.

Public editions: real, fact-checked MMA training knowledge - every record
a technique with step-by-step body mechanics (how to do it), key points,
requirements, standards, and citations. Civilian martial-arts instruction
only. Signature editions: the same ladder reframed through the Signature
lens - his original Signature Combat Method - titles suffixed
" (Signature Edition)", src signature, clearly labeled Signature-made,
never presented as authentic public record.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature Combat Method: the "
            "stance as sworn ground, the strike as a signature struck in "
            "motion, wrestling as the handshake of bodies, submissions as "
            "the sealed agreement. Clearly labeled Signature-made, never "
            "presented as authentic public record.")

ENTRIES = [
    {
        "key": "mma_stance",
        "name": "The MMA Stance",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "The MMA stance is the platform every technique stands on: a "
            "balanced, mobile posture that lets a fighter strike, defend "
            "takedowns, and move in any direction without resetting the "
            "feet. It blends the boxing stance (sideways, weight centered, "
            "hands up) with the wrestling stance (lower hips, wider base, "
            "hands ready to sprawl). Feet sit roughly shoulder-width apart "
            "or slightly wider, dominant foot back at about a forty-five "
            "degree angle, knees softly bent, chin tucked behind the lead "
            "shoulder, lead hand at cheek height, rear hand at the jaw. "
            "Weight is split close to even - never leaning - so the fighter "
            "can explode forward, retreat, or drop the hips into a sprawl "
            "in a single beat. A good stance is tested by shoving: if a "
            "partner can push the student off balance, the feet are too "
            "narrow or the weight is too far forward."
        ),
        "how_it_works": (
            "Stand with feet under the shoulders and step the dominant-side "
            "foot back about one full foot length, toes turned out around "
            "forty-five degrees. Bend the knees until the hips drop a few "
            "inches - low enough to feel the weight settle into the legs, "
            "high enough to spring. Tuck the chin slightly and pull the "
            "lead shoulder a touch forward so it frames the jaw. Raise the "
            "lead hand to cheek height with the elbow tucked against the "
            "ribs, and park the rear hand against the jaw with its elbow "
            "also tucked. Keep the heels light: the lead heel may lift a "
            "finger-width off the floor so the foot can pivot and so the "
            "bodyweight stays on the balls of the feet. Breathe easy and "
            "rock gently forward and back; balance should hold through the "
            "rock. Practice drill: a partner pushes the student's shoulders "
            "from the front, sides, and back - the stance passes when the "
            "student absorbs the push through the legs instead of "
            "staggering. From this stance every fundamental starts: punches "
            "rotate from it, kicks pivot on it, takedowns shoot from it, "
            "and sprawls drop out of it."
        ),
        "key_points": [
            "Feet roughly shoulder-width or wider; dominant foot back, toes at about forty-five degrees.",
            "Knees bent, hips lowered a few inches; weight close to even between the feet.",
            "Chin tucked behind the lead shoulder; lead hand at cheek, rear hand at jaw.",
            "Elbows tucked to protect the ribs; heels light, weight on the balls of the feet.",
            "Balance test: a partner's shove should be absorbed through the legs, not by staggering.",
            "Lower than a boxing stance (takedown defense) and more sideways than a wrestling stance (striking defense).",
            "The stance must allow instant forward, backward, and downward (sprawl) movement.",
            "Rebuilt and re-checked every session - stances drift taller and narrower without attention.",
        ],
        "requirements": [
            "Flat training surface (mat or canvas) so footwork is honest.",
            "Several feet of clear space in every direction.",
            "A training partner or coach to test balance with shoulder pushes.",
            "Comfortable athletic footwear or bare feet per gym rules.",
            "Five minutes of stance holds per session to build leg endurance.",
        ],
        "standards": [
            "Orthodox (left foot forward) or southpaw (right foot forward) per the student's dominant side.",
            "Hands return to the face after every technique - stance resets are the unit of good defense.",
            "Weight distribution within roughly 45 to 55 percent per foot at rest.",
            "Chin down and eyes up: the fighter sees over the lead shoulder, never staring at the floor.",
        ],
        "citations": [
            "Dempsey J. Championship Fighting: Explosive Punching and Aggressive Defense. 1950 (stance and balance mechanics).",
            "Gracie R, Gracie R. Brazilian Jiu-Jitsu: Theory and Technique. Invisible Cities Press; 2001 (base and posture fundamentals).",
        ],
        "sig_lens": (
            "Through the Signature lens the stance is sworn ground: the "
            "body writes its first line - balanced, low, honest - and every "
            "technique afterward is just that line spoken louder."
        ),
    },
    {
        "key": "footwork_angles",
        "name": "Footwork and Cage Angles",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Footwork is how a fighter owns the space of the cage: small "
            "balanced steps that keep the stance intact while closing "
            "distance, creating angles, and cutting off a retreating "
            "opponent. The rule is step-drag - the lead foot moves first in "
            "the direction of travel and the rear foot follows, so the feet "
            "never cross and the base never narrows. Circling goes to the "
            "outside of the opponent's lead foot when retreating from "
            "power, and lateral steps set up the forty-five degree attack "
            "angle: stepping off-center so the fighter's strikes arrive "
            "while the opponent's return strikes fall short. Cage cutting "
            "means herding: stepping to block the opponent's escape routes "
            "instead of chasing in a straight line. Good footwork looks "
            "boring - no wasted motion, no crossed feet, no bouncing that "
            "freezes the legs."
        ),
        "how_it_works": (
            "From the stance, move forward by stepping the lead foot a few "
            "inches forward, then dragging the rear foot the same distance "
            "so stance width never changes. Move back by reversing the "
            "order: rear foot first, lead foot follows. Move left by "
            "stepping the lead foot left and dragging the rear; move right "
            "by stepping the rear foot right and dragging the lead. Never "
            "let the feet cross or come together - a narrow base is a "
            "takedown invitation. To cut an angle, take a short diagonal "
            "step with the lead foot toward the opponent's blind side "
            "(outside their lead foot) and pivot the rear foot to square "
            "the hips - the forty-five. Practice the ladder drill: tape a "
            "ladder on the mat and step through it in stance, keeping width "
            "constant. Then practice cage cutting with a partner who walks "
            "the perimeter: the student herds them into a corner using "
            "diagonal steps, never straight pursuit. Three rounds of three "
            "minutes of pure footwork shadow movement builds the calves "
            "and the habit."
        ),
        "key_points": [
            "Step-drag: lead foot first going forward or lead-side, rear foot first going back or rear-side.",
            "Feet never cross and never come together; stance width stays constant through every step.",
            "The forty-five degree angle: diagonal lead-foot step that puts the fighter off the opponent's centerline.",
            "Cage cutting is herding with diagonal steps - never chase in a straight line.",
            "Small steps beat big lunges; big steps strand the fighter out of position.",
            "Stay on the balls of the feet; flat feet cannot change direction.",
            "Pivot the rear foot to re-square the hips after every angle change.",
            "Shadow footwork three minutes a round builds the endurance the legs need.",
        ],
        "requirements": [
            "Open mat space at least fifteen feet square.",
            "Tape or cones to mark ladders, angles, and cage-cutting lanes.",
            "A partner who walks or jogs the perimeter for cutting drills.",
            "Timer: three-minute rounds with one-minute rests.",
        ],
        "standards": [
            "Stance width measured heel-to-heel should vary less than two inches through a full footwork round.",
            "After any three-step sequence the fighter can throw a balanced jab - if not, the feet failed.",
            "Angle steps land outside the opponent's lead foot, not in front of their power hand.",
            "Head stays level through movement - bobbing telegraphs and wastes energy.",
        ],
        "citations": [
            "Dempsey J. Championship Fighting: Explosive Punching and Aggressive Defense. 1950 (footwork and positioning).",
            "Sheridan S. The Fighter's Mind: Inside the Mental Game. Grove Press; 2010 (ringcraft and spatial control).",
        ],
        "sig_lens": (
            "The Signature reads footwork as penmanship of distance: "
            "every small honest step is a word placed exactly, and the "
            "angle is the sentence turned so the opponent cannot answer."
        ),
    },
    {
        "key": "jab",
        "name": "The Jab",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The jab is the lead-hand straight punch and the most thrown "
            "strike in MMA: a fast, snapping extension of the lead arm that "
            "measures range, disrupts the opponent's rhythm, sets up power "
            "shots, and keeps aggressive opponents honest. It travels the "
            "shortest path - straight from the cheek to the target and "
            "straight back - so it lands before slower looping punches can "
            "be launched. The jab's power comes from a small step and a "
            "quarter-turn of the lead shoulder, not from arm muscle; the "
            "fist rotates palm-down at full extension and snaps back twice "
            "as fast as it went out. Because the lead hand never leaves the "
            "face for long, the jab doubles as a guard - a busy jab is one "
            "of the best defenses in the sport."
        ),
        "how_it_works": (
            "From the stance, push off the ball of the lead foot with a "
            "small step toward the target - two to four inches is enough. "
            "As the step lands, drive the lead fist straight out from the "
            "cheek, rotating the fist so the palm faces down at extension "
            "and turning the lead shoulder a quarter-turn into the punch. "
            "The rear hand stays glued to the jaw; the chin tucks a fraction "
            "deeper behind the rising lead shoulder. At full extension the "
            "arm is straight but the elbow is not locked - snapping, not "
            "pushing. Retract along the exact same line, back to the cheek, "
            "faster than the punch went out. The target line is the nose, "
            "chin, or forehead; the body jab drops the level by bending the "
            "knees (never the waist) and drives to the solar plexus. Pad "
            "drill: ten jabs in a row, each one snapping the pad with an "
            "audible crack, hand back to the cheek before the coach calls "
            "the next. Common fault: dropping the rear hand or pulling the "
            "jab back low - both invite the counter cross."
        ),
        "key_points": [
            "Straight out, straight back; the fist rotates palm-down at full extension.",
            "Power from the small step and the quarter-turn of the lead shoulder, not the arm.",
            "Rear hand stays on the jaw and the chin tucks behind the lead shoulder.",
            "Snap, don't push: extension is fast and the elbow never locks.",
            "Retraction is faster than the punch; the hand returns to the cheek every time.",
            "The jab measures range - whatever it touches, the cross can reach.",
            "Body jab: bend the knees to change level, never bow at the waist.",
            "A busy, snapping jab is itself a defense - it occupies the opponent's guard.",
        ],
        "requirements": [
            "Focus mitts or a heavy bag to develop the snap.",
            "A partner to call the jab and test retraction speed.",
            "Wrist wraps and gloves sized for pad work.",
            "Mirror or video to check that the rear hand never drops.",
        ],
        "standards": [
            "At full extension the lead shoulder covers the chin and the rear glove is at the jaw.",
            "The punch lands with the first two knuckles, wrist straight behind the fist.",
            "Ten consecutive jabs keep identical form - no drifting low on the return.",
            "The step and the punch land together; punching before the step lands bleeds power.",
        ],
        "citations": [
            "Dempsey J. Championship Fighting: Explosive Punching and Aggressive Defense. 1950 (the straight lead).",
            "Association of Boxing Commissions. Unified Rules of Mixed Martial Arts (legal striking targets).",
        ],
        "sig_lens": (
            "The Signature treats the jab as the signature's first stroke "
            "- light, exact, and always returning home; the hand that "
            "measures the page is the hand that will sign it."
        ),
    },
    {
        "key": "cross",
        "name": "The Cross",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The cross is the rear-hand straight punch and the fundamental "
            "power shot of MMA: the rear fist travels straight over the "
            "lead shoulder, driven by a full rotation of the hips and a "
            "pivot of the rear foot. Because the whole body turns behind "
            "it, the cross carries far more force than any arm punch - it is "
            "the punch that ends exchanges when it lands clean on the chin. "
            "The mechanics are a chain: rear foot pivots on the ball, hips "
            "rotate, torso follows, shoulder drives, arm extends, fist "
            "rotates palm-down. The lead hand stays at the cheek throughout "
            "to catch the counter. Thrown behind a jab, the one-two is the "
            "oldest and still most reliable combination in fighting."
        ),
        "how_it_works": (
            "From the stance, pivot the rear foot on its ball so the heel "
            "turns outward and the knee drives inward. Let that pivot whip "
            "the hips around - the rear hip drives forward as the lead hip "
            "pulls back. The torso rotates with the hips and the rear "
            "shoulder fires the fist straight over the lead shoulder toward "
            "the chin. The fist rotates palm-down at extension; the arm "
            "extends straight without locking the elbow. The lead hand "
            "never leaves the cheek, and the chin tucks into the rising "
            "rear shoulder. At impact the weight has transferred from the "
            "rear leg to the lead leg - roughly seventy percent forward. "
            "Then reverse the chain: pull the fist straight back to the jaw "
            "as the hips unwind to stance. Heavy-bag drill: throw the cross "
            "alone until the bag swings on its chains from body rotation, "
            "not from leaning. Then drill the one-two: jab, and the cross "
            "fires the instant the jab's fist starts its return."
        ),
        "key_points": [
            "Power chain: rear-foot pivot drives hip rotation, hips drive the torso, torso drives the arm.",
            "The fist travels straight over the lead shoulder; the arm never loops wide.",
            "Palm rotates down at extension; the elbow does not lock.",
            "Weight transfers from the rear leg to the lead leg through impact.",
            "Lead hand stays at the cheek the entire time - the cross never opens the guard.",
            "The one-two: the cross fires as the jab retracts, using the same hip rotation both punches share.",
            "Retract along the same line, back to the jaw, before the hips fully unwind.",
            "If the bag moves from leaning rather than rotation, the chain is broken - reset the feet.",
        ],
        "requirements": [
            "Heavy bag rated for power punching.",
            "Wrist wraps and sixteen-ounce gloves for bag rounds.",
            "A coach or video to verify the rear-foot pivot happens first.",
            "Core and hip mobility warm-up before power rounds.",
        ],
        "standards": [
            "The rear heel visibly turns outward on every cross - no pivot, no real cross.",
            "Chin is covered by either the lead glove or the rear shoulder at full extension.",
            "The punch lands with the first two knuckles and a straight wrist.",
            "Balance holds after the punch: the fighter is never falling forward past the lead foot.",
        ],
        "citations": [
            "Dempsey J. Championship Fighting: Explosive Punching and Aggressive Defense. 1950 (the straight rear-hand power line).",
            "Association of Boxing Commissions. Unified Rules of Mixed Martial Arts (legal striking targets).",
        ],
        "sig_lens": (
            "The cross is the Signature's heavy line: the whole body "
            "turning as one hand, the rear foot's pivot the period that "
            "ends the sentence the jab began."
        ),
    },
    {
        "key": "lead_hook",
        "name": "The Lead Hook",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The lead hook is the close-range arc punch: the lead arm "
            "bends at roughly ninety degrees and swings on a horizontal "
            "plane, the fist arriving from the side of the opponent's guard "
            "where straight punches cannot reach. It is the great "
            "guard-splitter - thrown around a high guard to the temple or "
            "jaw, or dug to the ribs and liver when the elbows lift. Power "
            "comes from pivoting the lead foot and whipping the hips and "
            "torso through the arc; the arm itself stays rigid, a hook on "
            "the end of a rotating body. Thrown tight it is one of the "
            "most damaging punches in MMA; thrown wide and looping it "
            "becomes a slow arm punch that invites counters."
        ),
        "how_it_works": (
            "From the stance, pivot hard on the ball of the lead foot, "
            "turning the toes inward as the lead knee drives across. The "
            "hips whip around with the pivot and the torso follows. Raise "
            "the lead elbow to shoulder height, bend the arm to about "
            "ninety degrees, and let the rotating body swing the fist on a "
            "tight horizontal arc - the fist travels no wider than the "
            "shoulders. At contact the palm faces the fighter (thumb up) "
            "for the head hook, or palm-down for the body hook; the wrist "
            "stays straight and the first two knuckles land. The rear hand "
            "stays glued to the jaw. Snap the hook back to the cheek along "
            "the same arc. For the body hook, bend the knees to drop level "
            "and dig the hook into the ribs or liver under the elbow. Mitt "
            "drill: coach holds the mitt at temple height just outside the "
            "student's lead shoulder - the hook must arrive tight, with the "
            "elbow never dropping below the fist."
        ),
        "key_points": [
            "Tight arc: the fist travels no wider than the shoulders; wide hooks are slow and punished.",
            "Power from the lead-foot pivot and hip whip, not from swinging the arm.",
            "Elbow at shoulder height on the head hook; wrist straight, first two knuckles land.",
            "Rear hand stays on the jaw - the hook never opens the guard.",
            "Body hook: drop level with the knees, never the waist, and dig under the elbow.",
            "The hook splits high guards - it arrives from the side where straight punches are blocked.",
            "Snap back along the same arc; a hook that stays out invites the counter hook.",
            "Turn the lead toes inward on the pivot - the pivot is the punch's engine.",
        ],
        "requirements": [
            "Focus mitts held at temple and rib height.",
            "Heavy bag for tight-hook power rounds.",
            "Wrist wraps; hooks stress the wrist when form slips.",
            "A partner to test the arc: a wide hook should get tagged in sparring drills.",
        ],
        "standards": [
            "The lead elbow reaches shoulder height before the fist starts its arc.",
            "The fist, elbow, and shoulder form roughly a right angle at the tightest point.",
            "Balance holds: the fighter can throw the follow-up cross immediately after the hook.",
            "No wind-up - the hook fires from the guard with no pull-back.",
        ],
        "citations": [
            "Dempsey J. Championship Fighting: Explosive Punching and Aggressive Defense. 1950 (hook mechanics).",
            "Association of Boxing Commissions. Unified Rules of Mixed Martial Arts (legal striking targets).",
        ],
        "sig_lens": (
            "The hook is the Signature's flourish: the tight arc drawn "
            "around the guard's edge, the body turning the pen while the "
            "arm only holds it."
        ),
    },
    {
        "key": "rear_uppercut",
        "name": "The Rear Uppercut",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The rear uppercut is the inside power shot: the rear fist "
            "drives upward on a short vertical plane, landing under the "
            "chin or into the solar plexus of an opponent who is leaning "
            "in, ducking, or clinched close. It is the punch for phone-booth "
            "distance, where hooks have no room to arc and straight punches "
            "are smothered. The power comes from dipping the knees and "
            "exploding upward through the legs and hips - the punch is a "
            "stand-up driven through the fist. Because it travels upward "
            "under the guard, a clean uppercut on the chin is one of the "
            "most fight-ending strikes in the sport. The danger is "
            "over-dipping: dropping too low strands the fighter under the "
            "counter."
        ),
        "how_it_works": (
            "From the stance at close range, dip the knees two to four "
            "inches - a short, athletic dip, never a squat. Keep the rear "
            "elbow tucked to the ribs and the palm facing the fighter. "
            "Explode upward through the legs, driving the hips forward as "
            "the rear fist punches straight up the centerline, rotating the "
            "palm to face away at the top of the drive. The fist travels "
            "from hip height to chin height on a tight vertical track, "
            "never swinging out wide. The lead hand stays at the cheek "
            "throughout. Land with the first two knuckles under the chin, "
            "then drop the fist straight back to guard along the same "
            "track. Uppercut bag drill: work inside a hanging bag so the "
            "range is honest - if the student has to lean to reach, the "
            "distance is wrong for the uppercut. Sparring cue: the "
            "uppercut answers the ducking opponent - when their head "
            "drops, the uppercut meets it coming up."
        ),
        "key_points": [
            "Short knee dip of two to four inches, then explode upward through the legs and hips.",
            "The fist travels a tight vertical track from hip to chin height - never swings wide.",
            "Palm faces the fighter at the start, rotates away at the top of the drive.",
            "Best weapon at phone-booth distance, under a leaning or ducking opponent's chin.",
            "Lead hand never leaves the cheek during the punch.",
            "Over-dipping strands the fighter low and open - the dip is small and athletic.",
            "Retract straight back down the same track to guard.",
            "Set it up: the uppercut lands best after the opponent commits their head forward.",
        ],
        "requirements": [
            "Uppercut bag or a heavy bag worked from the inside.",
            "A partner who leans and ducks on cue for timing drills.",
            "Knee and hip warm-up - the dip loads the legs heavily.",
            "Gloves with good wrist support; uppercuts punish bent wrists.",
        ],
        "standards": [
            "The dip never drops the hips below the knees - it is a dip, not a squat.",
            "The fist stays inside the frame of the body on the way up.",
            "Head stays behind the punch line; the fighter does not lean into the uppercut.",
            "Balance is immediate after the punch - the fighter can sprawl or pivot out.",
        ],
        "citations": [
            "Dempsey J. Championship Fighting: Explosive Punching and Aggressive Defense. 1950 (the uppercut as the inside power punch).",
            "Association of Boxing Commissions. Unified Rules of Mixed Martial Arts (legal striking targets).",
        ],
        "sig_lens": (
            "The uppercut is the Signature rising: the small dip the "
            "breath before the mark, the upward drive the line lifting off "
            "the page to meet what leans down toward it."
        ),
    },
    {
        "key": "low_kick",
        "name": "The Low Kick",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The low kick is the foundational MMA kick: the rear leg "
            "swings like a baseball bat into the opponent's lead thigh, "
            "chopping at the base that holds them up. A handful of clean "
            "low kicks deadens the lead leg - the opponent's stance "
            "collapses, their footwork slows, and their takedown defense "
            "weakens because they cannot push off a damaged leg. The kick "
            "lands with the lower shin, not the foot, and the power comes "
            "from whipping the hips over - the leg is the end of the "
            "whip, not its source. Low kicks are low-risk: the target is "
            "close, the kick is fast, and the kicker's hands stay home to "
            "block the counter. Fighters who neglect low-kick defense get "
            "their lead leg chopped out from under them, round after round."
        ),
        "how_it_works": (
            "From the stance, step the lead foot slightly to the outside - "
            "six to ten inches at a forty-five degree angle - opening the "
            "hips. Pivot hard on the ball of the lead foot, turning the "
            "toes outward as the hips whip over and the rear leg swings "
            "through like a bat. The leg stays relaxed until the moment of "
            "impact, then the lower shin - two to four inches above the "
            "ankle - drives into the outside of the opponent's lead thigh. "
            "The arms swing for counterbalance: the rear arm drops to guard "
            "the body as the kick swings, and the lead hand stays at the "
            "cheek. Follow through across the target - kicking through, "
            "not at - then snap the leg back to stance or step it down "
            "forward into a new stance. Bag drill: kick the heavy bag's "
            "lower third until the shin, not the foot, leaves the mark and "
            "the bag swings from hip rotation. Never kick with the foot or "
            "toes - the small bones break against a checked shin."
        ),
        "key_points": [
            "Land with the lower shin, two to four inches above the ankle - never the foot or toes.",
            "Power from whipping the hips over; the leg is the end of the whip.",
            "Step the lead foot outside at forty-five degrees and pivot hard on its ball.",
            "Target the outside of the opponent's lead thigh; a few clean kicks deaden the leg.",
            "Kick through the target, not at it; follow-through carries the power.",
            "Hands stay home: lead hand at the cheek, rear arm guarding the body during the kick.",
            "The leg stays relaxed until impact, then tenses through the shin.",
            "Low kicks are the safest kicks - close target, fast return, hands free to defend.",
        ],
        "requirements": [
            "Heavy bag or banana bag for shin conditioning rounds.",
            "Shin guards for partner drills; bare shins only on pads.",
            "A partner holding Thai pads at thigh height.",
            "Hip mobility warm-up - the hip whip is the kick's engine.",
        ],
        "standards": [
            "The supporting foot pivots a full ninety degrees or more on every kick.",
            "Impact lands with the shin; foot kicks are stopped and corrected immediately.",
            "The kicker's balance holds after the kick - no hopping or falling into the kick.",
            "Hands do not drop below the chin during the swing.",
        ],
        "citations": [
            "Gracie R, Gracie R. Brazilian Jiu-Jitsu: Theory and Technique. Invisible Cities Press; 2001 (striking fundamentals for MMA).",
            "Association of Boxing Commissions. Unified Rules of Mixed Martial Arts (legal kicking targets).",
        ],
        "sig_lens": (
            "The low kick is the Signature striking at the foundation: "
            "not the head the argument, but the leg it stands on - chop "
            "the base and the whole stance rewrites itself."
        ),
    },
    {
        "key": "head_movement",
        "name": "Head Movement and Evasion",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Head movement is defense without the hands: slipping, rolling, "
            "and ducking the head off the centerline so punches pass "
            "through empty air. The slip moves the head a few inches to "
            "either side of a straight punch; the roll dips under a hook "
            "by bending the knees and shifting the weight; the duck drops "
            "the level straight down under a high punch. The golden rule "
            "is small: moving the head three inches defeats a punch aimed "
            "at the chin, while big dramatic weaves strand the fighter out "
            "of position and open the body. Head movement must always end "
            "back in stance with the hands up - the head that moves and "
            "stays moved is a head waiting for the follow-up shot."
        ),
        "how_it_works": (
            "For the slip: as the opponent's jab comes, rotate the torso "
            "a few degrees and shift the head two to three inches to the "
            "outside of the punch line - right for an orthodox fighter "
            "slipping a jab - letting the punch pass beside the ear while "
            "the eyes stay on the opponent. For the roll under a hook: "
            "bend the knees, dip the level, and shift the weight to the "
            "side the hook comes from, letting the arm pass over the "
            "shoulder, then rise back into stance. For the duck: bend the "
            "knees straight down under a high punch and come straight back "
            "up - never lean forward at the waist, which invites the "
            "uppercut. Drill with a partner tapping the head with a glove "
            "on cue: slip, roll, or duck, then immediately fire the "
            "counter the movement creates - the slip outside sets up the "
            "cross, the roll under sets up the hook. Slip rope drill: a "
            "rope strung at shoulder height; weave under it moving "
            "forward, bending only the knees."
        ),
        "key_points": [
            "Small movement wins: two to three inches off the centerline defeats a punch.",
            "Slip straight punches by shifting the head just outside the punch line.",
            "Roll under hooks by bending the knees and shifting weight to the hook's side.",
            "Duck straight down under high punches - never lean forward at the waist.",
            "Eyes stay on the opponent through every movement; looking away is surrender.",
            "Every slip, roll, or duck ends back in stance with hands up.",
            "Head movement sets up counters: slip outside, fire the cross; roll under, fire the hook.",
            "The slip rope drill teaches knee-bend movement instead of waist-bend leaning.",
        ],
        "requirements": [
            "A partner with gloves to throw slow, cued punches.",
            "A rope strung at shoulder height for the weave drill.",
            "Mirror to check that movement stays small and the hands stay up.",
            "Neck and torso warm-up before rolling drills.",
        ],
        "standards": [
            "The head moves no more than about four inches on any slip - bigger is a fault.",
            "Hands remain at cheek and jaw height through all head movement.",
            "The fighter returns to stance within one beat of the evasion.",
            "The waist never bends forward; all level change comes from the knees.",
        ],
        "citations": [
            "Dempsey J. Championship Fighting: Explosive Punching and Aggressive Defense. 1950 (slipping and rolling).",
            "Sheridan S. The Fighter's Mind: Inside the Mental Game. Grove Press; 2010 (defensive timing).",
        ],
        "sig_lens": (
            "Evasion is the Signature's eraser used sparingly: the head "
            "slides a breath off the line and the punch signs empty air, "
            "leaving the counter's page blank and waiting."
        ),
    },
    {
        "key": "blocking",
        "name": "Blocking and Parrying",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Blocking and parrying are hand defenses: the block absorbs a "
            "strike on the arms and gloves, the parry deflects it off line "
            "with a short tap. The high block catches straight punches and "
            "hooks on the gloves and forearms held tight to the head; the "
            "elbow block (the shell) tucks both elbows to the ribs with "
            "forearms vertical to stop body shots and hooks; the parry "
            "meets the opponent's jab with the rear palm and redirects it "
            "a few inches past the head. Parries are cheaper than blocks - "
            "a two-inch deflection costs less energy and opens the counter "
            "faster than absorbing the full shot - but they demand timing. "
            "The cardinal rule: the hands catch punches, they never reach "
            "for them; reaching pulls the guard apart and invites the "
            "punch that was being set up."
        ),
        "how_it_works": (
            "For the high block: keep the gloves at the cheeks and meet "
            "the incoming punch with the glove or the top of the forearm, "
            "absorbing through a slight bend of the knees - the block is "
            "firm, the body behind it is springy. For the shell against "
            "body shots: drop both elbows tight to the ribs, forearms "
            "vertical in front of the torso, chin tucked; hooks to the "
            "body land on the elbows and forearms. For the parry: as the "
            "opponent's jab extends, tap it with the rear palm - a short "
            "outward flick of two to three inches - redirecting it past "
            "the head while the lead hand stays home. Immediately fire the "
            "counter the parry opens: parry the jab, answer with the "
            "cross. Partner drill: one partner throws slow one-twos; the "
            "student blocks the jab, parries or blocks the cross, and "
            "returns a one-two of their own. The block must never drift "
            "more than a few inches from the face - a block that chases "
            "the punch leaves the chin behind."
        ),
        "key_points": [
            "Blocks absorb on the gloves and forearms held tight; parries deflect with a short two-inch tap.",
            "The high block meets straight punches and head hooks at the cheeks.",
            "The shell - elbows tucked, forearms vertical - stops body shots and rib hooks.",
            "The rear-hand parry redirects the jab past the head and opens the counter cross.",
            "Hands catch punches; they never reach for them - reaching opens the guard.",
            "Absorb through the knees: firm block, springy body behind it.",
            "Parries cost less energy than blocks and counter faster, but demand timing.",
            "Every block ends with the hands back at the face within one beat.",
        ],
        "requirements": [
            "A partner to throw slow, controlled one-twos.",
            "Gloves and headgear for block-contact drills.",
            "Focus mitts for parry-and-counter timing work.",
            "Forearm conditioning comes from the bag, not from taking hard shots early.",
        ],
        "standards": [
            "Blocks stay within a few inches of the face - no chasing punches.",
            "The chin stays tucked behind the guard through every block.",
            "The parry deflects two to three inches; bigger parries are wasted motion.",
            "A blocked combination is answered with a combination - defense feeds offense.",
        ],
        "citations": [
            "Dempsey J. Championship Fighting: Explosive Punching and Aggressive Defense. 1950 (blocking and parrying).",
            "Association of Boxing Commissions. Unified Rules of Mixed Martial Arts (legal striking targets).",
        ],
        "sig_lens": (
            "The block is the Signature's margin: the hands hold the "
            "page's edge so the strike lands on the frame, never the "
            "text - and the parry is the margin turned into a doorway."
        ),
    },
    {
        "key": "double_leg",
        "name": "The Double Leg Takedown",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The double leg takedown is the foundational wrestling shot "
            "in MMA: the fighter changes level, penetrates with a deep "
            "step between the opponent's legs, wraps both legs, and drives "
            "through to put the opponent on the mat. It is the highest-"
            "percentage takedown in the sport because it attacks the base "
            "itself - both legs at once - and finishes with the attacker's "
            "weight driving forward and down. The keys are the level "
            "change (dropping the hips, never bowing the waist), the "
            "penetration step (the lead knee lands between the opponent's "
            "feet), and head position (the head presses tight to the "
            "opponent's hip or ribs, never dropping below the waist). A "
            "double leg shot from too far out is a sprawl waiting to "
            "happen; set up with strikes, shoot when the opponent's weight "
            "is planted."
        ),
        "how_it_works": (
            "From the stance, change level by bending the knees and "
            "dropping the hips four to six inches - the back stays "
            "straight, the eyes stay up. Take a deep penetration step: the "
            "lead foot steps between the opponent's feet and the lead knee "
            "drops to the mat between their legs (on a mat; on hard ground "
            "the step stays low without the knee touching). As the knee "
            "lands, both arms wrap the opponent's legs behind the knees, "
            "hands clasping, and the head presses hard into the side of "
            "their hip or ribs - cheek to hip, ear covered. Then drive: "
            "push off the rear foot, drive the shoulder through the hips, "
            "and run the opponent backward and down, turning the corner "
            "slightly to one side so they cannot sprawl straight back. "
            "Finish in side control or the guard with posture. Drill: "
            "shoot the double leg on a heavy bag laid on its side - level "
            "change, penetration step, wrap, drive through. Set-up drill: "
            "jab, jab, then shoot as the partner plants to answer."
        ),
        "key_points": [
            "Level change comes from the knees and hips; the back stays straight and eyes stay up.",
            "The penetration step lands the lead knee between the opponent's feet.",
            "Both arms wrap behind the knees with hands clasped; the head presses tight to the hip.",
            "Drive through the opponent - shoulder into the hips, running them backward and down.",
            "Turn the corner slightly so the opponent cannot sprawl straight back onto the shot.",
            "Never shoot from out of range; set up with strikes and shoot when their weight is planted.",
            "Head position is safety: cheek to the hip, never below the waist where knees and guillotines wait.",
            "Finish past the takedown - drive into side control or a heavy guard posture.",
        ],
        "requirements": [
            "Wrestling mats - takedown drilling needs a forgiving surface.",
            "A partner who gives the correct reactions (sprawls lightly, falls safely).",
            "A heavy bag laid sideways for solo penetration-step reps.",
            "Knee pads for the penetration knee during high-rep drilling.",
        ],
        "standards": [
            "The level change drops the hips at least four inches before the step.",
            "The lead knee lands between the opponent's feet, not outside them.",
            "The head never drops below the opponent's waistline during the shot.",
            "The drive continues past the fall - the attacker lands in a dominant position, not in a scramble.",
        ],
        "citations": [
            "Gracie R, Gracie R. Brazilian Jiu-Jitsu: Theory and Technique. Invisible Cities Press; 2001 (takedowns for MMA).",
            "Kodokan. Kodokan Judo: Throwing Techniques. Kodansha; 2014 (kuzushi - breaking balance - principles).",
        ],
        "sig_lens": (
            "The double leg is the Signature taking the whole page: "
            "level changed, both legs wrapped, the drive the firm hand "
            "that lays the argument flat."
        ),
    },
    {
        "key": "sprawl",
        "name": "The Sprawl",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The sprawl is the fundamental takedown defense: as the "
            "opponent shoots, the defender throws both legs back, drops "
            "the hips heavy onto the opponent's back and shoulders, and "
            "drives their weight down to kill the shot. It turns the "
            "attacker's penetration against them - the deeper they dive, "
            "the more weight lands on them. The sprawl must be violent and "
            "total: half-hearted sprawls, with the hips still high, get "
            "finished. Hands go to the mat or to the opponent's head and "
            "shoulders to post and push, the head stays up, and the hips "
            "drive down and slightly back. A good sprawl ends with the "
            "defender chest-to-back on a flattened opponent, free to take "
            "the back or stand back up."
        ),
        "how_it_works": (
            "The instant the opponent changes level, throw both feet "
            "straight back - a full split-second leg throw, not a step - "
            "and let the hips crash down onto the opponent's upper back "
            "and shoulders. Land the hands on the mat wide for base, or "
            "drive one hand into the back of their head and the other "
            "across their shoulder, pushing their face toward the mat. "
            "Keep the head up and the back flat; arching the head down "
            "invites the front headlock. Drive the hips down and walk the "
            "feet in a small circle to flatten the opponent completely, "
            "then choose: spin to take the back, crossface and work to a "
            "dominant position, or push away and stand back to the feet. "
            "Drill: a partner shoots slow double legs on cue; the student "
            "sprawls with full hip commitment, aiming to land chest-heavy "
            "enough that the partner cannot finish. Reaction drill: the "
            "coach claps or the partner fakes, and the student sprawls on "
            "any level change - training the eyes to read the hips, not "
            "the hands."
        ),
        "key_points": [
            "Both legs throw back in one violent motion; half-sprawls get finished.",
            "Hips crash heavy onto the opponent's upper back and shoulders.",
            "Hands post on the mat or drive the opponent's head toward the mat.",
            "Head stays up and back stays flat - never arch the head down.",
            "Circle the feet after the sprawl to flatten the opponent completely.",
            "The sprawl answers the level change: read the opponent's hips, not their hands.",
            "Finish the sprawl - take the back, crossface, or stand up; never just lie there.",
            "Sprawl on fakes too in drilling; in a fight, the eyes learn which level changes are real.",
        ],
        "requirements": [
            "Wrestling mats for full-commitment sprawl reps.",
            "A partner who shoots controlled double legs on cue.",
            "Hip and hamstring warm-up - the leg throw is explosive.",
            "Timer for sprawl reaction rounds: thirty seconds, sprawl on every cue.",
        ],
        "standards": [
            "Both feet leave the ground and land behind in under half a second on a committed sprawl.",
            "The defender's hips land on the opponent, not beside them.",
            "The head never drops below the shoulders during the sprawl.",
            "After the sprawl the defender is chest-heavy and mobile, able to circle or disengage.",
        ],
        "citations": [
            "Gracie R, Gracie R. Brazilian Jiu-Jitsu: Theory and Technique. Invisible Cities Press; 2001 (takedown defense for MMA).",
            "Kodokan. Kodokan Judo: Throwing Techniques. Kodansha; 2014 (defensive posture principles).",
        ],
        "sig_lens": (
            "The sprawl is the Signature refusing the page: the shot "
            "dives for the legs and finds only air and weight - the hips "
            "the seal pressed down on the attempt."
        ),
    },
    {
        "key": "hip_escape",
        "name": "The Hip Escape",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The hip escape - shrimping - is the fundamental ground "
            "survival movement: lying on the back, the student turns onto "
            "one hip, posts a foot, and shoves the hips backward to create "
            "space between themselves and the opponent. Nearly every "
            "escape from the bottom in MMA starts with a hip escape - from "
            "mount, from side control, from under ground-and-pound. It "
            "works because frames and hip movement together make space, "
            "and space is what the bottom fighter is always buying. The "
            "movement is small and repeatable: turn, post, shove, recover "
            "guard. Students drill it as a warm-up for months before they "
            "ever need it in a scramble, and when they need it, it is "
            "there."
        ),
        "how_it_works": (
            "Lie on the back with knees bent and feet flat. Turn onto the "
            "right hip, posting the right foot flat on the mat. Push hard "
            "through that foot, shoving the hips six to twelve inches "
            "backward and to the left while the upper body stays mostly "
            "in place - the body makes a shrimp-like C-shape. The left "
            "foot can help by posting as well. Immediately bring the "
            "knees back in front as a guard barrier so the space just "
            "created is not given back. Alternate sides down the mat: "
            "right hip escape, recover, left hip escape, recover. Against "
            "a partner in the mount: frame one forearm across their hips "
            "and one hand on their chest, hip escape to one side, and "
            "slide the bottom knee inside to recover half guard. The "
            "power comes from the posted leg driving, not from wriggling "
            "the upper body. Drill it daily: three minutes of continuous "
            "shrimping is the ground fighter's roadwork."
        ),
        "key_points": [
            "Turn onto one hip, post the foot flat, and shove the hips six to twelve inches away.",
            "The power comes from the posted leg driving - not from wriggling the shoulders.",
            "Frame with the arms first (forearm on the hip, hand on the chest) so the escape has structure.",
            "Recover the knees in front immediately - created space must be kept, not gifted back.",
            "The hip escape is the first move of nearly every bottom escape in MMA.",
            "Drill it as a warm-up: three minutes of continuous shrimping builds the exact muscles.",
            "Move the hips, not the head - bridging the shoulders up achieves nothing.",
            "Chain it: hip escape to create space, then insert the knee, elbow, or guard.",
        ],
        "requirements": [
            "Mats with at least ten feet of clear lane for shrimping lines.",
            "A partner to hold mount and side control for escape reps.",
            "Timer for three-minute shrimping warm-up rounds.",
            "Patience: the movement feels awkward for weeks, then becomes reflex.",
        ],
        "standards": [
            "Each escape moves the hips a full six inches minimum - short shrimps are decoration.",
            "The knees recover in front of the torso before the drill rep ends.",
            "The head stays off the mat and the frames stay active through the movement.",
            "Against a resisting partner in mount, three chained hip escapes recover half guard.",
        ],
        "citations": [
            "Gracie R, Gracie R. Brazilian Jiu-Jitsu: Theory and Technique. Invisible Cities Press; 2001 (escapes and guard recovery).",
            "Gracie H. Gracie Jiu-Jitsu Basics instructional series (shrimping as the core survival movement).",
        ],
        "sig_lens": (
            "Shrimping is the Signature's quiet rewrite: the hips slide "
            "the sentence sideways and the guard's frame redraws the "
            "margin - space made, space kept."
        ),
    },
    {
        "key": "bridge_roll",
        "name": "The Bridge and Roll Escape",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The bridge and roll - the upa - is the fundamental escape "
            "from the mount: the bottom fighter traps one of the "
            "opponent's arms and one of their legs, bridges the hips high "
            "to off-balance them, and rolls over the trapped side to end "
            "on top. It is the highest-percentage mount escape because it "
            "uses the strongest muscles in the body - the glutes and legs "
            "driving the bridge - against the opponent's balance, not "
            "their strength. The trap is everything: without the arm "
            "trapped, the opponent posts and the roll fails; without the "
            "leg trapped, they step out. Under MMA ground-and-pound the "
            "bridge and roll is the emergency exit - one committed bridge "
            "can reverse the worst position in the sport."
        ),
        "how_it_works": (
            "Flat on the back under the mount, slide both feet flat near "
            "the hips. Trap one arm: pin the opponent's wrist or elbow "
            "tight to the chest with both hands - whichever side feels "
            "weaker. Trap the same-side leg: hook the foot outside their "
            "ankle or wedge the foot against their leg. Bridge explosively: "
            "drive through both feet, thrust the hips as high as they go, "
            "and turn the head to look toward the trapped side. The bridge "
            "lifts and tips the opponent; as they tip, keep driving and "
            "roll over the trapped shoulder in one continuous motion, "
            "ending chest-to-chest on top in their guard or side control. "
            "Never bridge straight up with no trap - that just lifts them "
            "higher. Drill with a partner holding a loose mount: trap, "
            "bridge, roll, reset. Timing cue: bridge the instant they sit "
            "up to punch - their weight is high and their base is narrow."
        ),
        "key_points": [
            "Trap one arm tight to the chest and trap the same-side leg before bridging.",
            "The bridge is explosive: drive through both feet, hips as high as they go.",
            "Look toward the trapped side; the head leads the roll.",
            "Roll in one continuous motion over the trapped shoulder - bridge and roll are one move.",
            "Without the arm trap the opponent posts; without the leg trap they step out.",
            "Time it when they sit up to punch - high weight and narrow base is the window.",
            "Never bridge straight up untrapped; it only lifts them higher.",
            "End on top with posture - the escape is only complete in a dominant position.",
        ],
        "requirements": [
            "Mats; bridging needs room to roll.",
            "A partner who holds a realistic but cooperative mount.",
            "Glute and leg warm-up - the bridge is a max-effort hip thrust.",
            "Mouthguard for any live mount-escape rounds.",
        ],
        "standards": [
            "Both traps are set before the hips leave the mat.",
            "The bridge lifts the hips at least twelve inches on a committed rep.",
            "The roll finishes with the student on top, not in a scramble.",
            "Against a partner sitting up to strike, the escape succeeds more often than not.",
        ],
        "citations": [
            "Gracie R, Gracie R. Brazilian Jiu-Jitsu: Theory and Technique. Invisible Cities Press; 2001 (upa escape from mount).",
            "Gracie H. Gracie Jiu-Jitsu Basics instructional series (mount escapes).",
        ],
        "sig_lens": (
            "The upa is the Signature's reversal: the trapped arm the "
            "held line, the bridge the page lifted, the roll the whole "
            "argument turned over in one committed motion."
        ),
    },
    {
        "key": "combos",
        "name": "Striking Combinations",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Striking combinations are punches and kicks linked into "
            "rhythmic sequences - the jab-cross, the jab-cross-hook, the "
            "jab-cross-low kick - where each strike sets up the next. "
            "Single strikes get blocked; combinations crack guards because "
            "the defender can only cover one line at a time. The classic "
            "logic is high-low and left-right: a jab to the head lifts the "
            "guard, the cross follows through the middle, the hook comes "
            "around the side, the low kick punishes the planted leg. "
            "Combinations work because of the return: every punch snaps "
            "back along its own line, so the next punch fires from a "
            "loaded guard instead of from a recovery. Beginners throw arm "
            "combinations; trained fighters throw hip combinations, the "
            "rotation of each strike loading the next."
        ),
        "how_it_works": (
            "Start with the one-two: throw the jab, and as the jab's fist "
            "begins its return, pivot the rear foot and fire the cross "
            "down the same channel the jab opened. The hips rotate left "
            "for the jab's shoulder turn and right for the cross - the "
            "rotation itself becomes rhythm. Add the hook: after the cross "
            "lands, pivot the lead foot and whip the hook around the "
            "guard the one-two lifted. Add the low kick: after the "
            "one-two-hook, step the lead foot outside and swing the low "
            "kick into the planted lead leg. Each strike's retraction "
            "loads the next - the cross's returning shoulder feeds the "
            "hook's pivot, the hook's return squares the hips for the "
            "kick. Mitt drill: the coach calls numbers (1 jab, 2 cross, 3 "
            "hook, 4 low kick) in two and three-strike sequences; the "
            "student fires them as single beats, never pausing between "
            "strikes. Finish every combination back in stance, hands home, "
            "ready to defend the answer."
        ),
        "key_points": [
            "Combinations crack guards: the defender covers one line while the next strike takes another.",
            "High-low and left-right logic: head strikes lift guards and plant legs for the low kick.",
            "Each strike's retraction loads the next - the return is part of the combination.",
            "Hip rotation links the strikes; arm-only combinations are slow and weak.",
            "The one-two is the foundation: jab opens the channel, cross fires through it.",
            "Never pause between strikes - combinations are single beats, not separate punches.",
            "Finish every combination back in stance with hands home.",
            "Vary the ending: the same one-two can finish with a hook, an uppercut, or a low kick.",
        ],
        "requirements": [
            "Focus mitts and a coach who calls numbered combinations.",
            "Heavy bag for full-power combination rounds.",
            "Timer: three-minute combination rounds.",
            "The single strikes must be clean first - combinations multiply flaws.",
        ],
        "standards": [
            "Three-strike combinations land within about one second with no visible pause.",
            "Hands return to the face between every strike - no dropping during the sequence.",
            "Balance holds through the full combination; the fighter is never falling forward.",
            "The combination ends in stance, ready to defend, not admiring the work.",
        ],
        "citations": [
            "Dempsey J. Championship Fighting: Explosive Punching and Aggressive Defense. 1950 (combination punching).",
            "Association of Boxing Commissions. Unified Rules of Mixed Martial Arts (legal striking targets).",
        ],
        "sig_lens": (
            "Combinations are the Signature's sentences: the jab the "
            "opening word, each strike's return the breath, the low kick "
            "the period - meaning built one honest stroke at a time."
        ),
    },
    {
        "key": "checking",
        "name": "Checking Leg Kicks",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Checking a leg kick means lifting the lead leg and turning "
            "the shin outward to meet the incoming kick shin-to-shin: the "
            "attacker's soft thigh meets the defender's hard shin bone, "
            "and the kick's damage rebounds onto the kicker. It is the "
            "primary defense against low kicks and one of the most "
            "fight-changing techniques in MMA - a single well-timed check "
            "can break the kicker's foot or shin and end their kicking "
            "game for the night. The check is economical: the knee lifts "
            "six to ten inches, the shin turns out, the weight sits on the "
            "rear leg, and the hands stay up to catch the punches that "
            "often follow a blocked kick. Fighters who never check get "
            "their lead leg chopped down; fighters who check well make "
            "opponents afraid to kick."
        ),
        "how_it_works": (
            "Read the kicker's hips: the moment the rear hip starts to "
            "turn over, lift the lead knee six to ten inches and rotate "
            "the shin outward so the hard front edge of the shin faces the "
            "incoming kick. Sit the weight fully on the rear leg - the "
            "checked leg is light and ready. Keep both hands at the face; "
            "kicks are often followed by punches. Meet the kick shin-to-"
            "shin: the attacker's thigh or foot strikes the defender's "
            "raised shin bone, and the impact punishes the kicker. Drop "
            "the leg straight back to stance the instant the kick passes - "
            "a leg left hanging gets grabbed for the takedown. Drill with "
            "a partner throwing slow low kicks: lift, turn, meet, drop. "
            "Speed comes from reading the hip, not the leg - by the time "
            "the leg swings, it is too late. Advanced check: angle the "
            "shin slightly so the kick slides off, reducing even the "
            "defender's impact."
        ),
        "key_points": [
            "Lift the lead knee six to ten inches and turn the shin outward to meet the kick.",
            "Shin-to-shin contact punishes the kicker - the check is a counter, not just a shield.",
            "Weight sits fully on the rear leg; the checked leg stays light.",
            "Read the kicker's hips, not the leg - the hip turn is the early warning.",
            "Hands stay at the face; punches often follow a checked kick.",
            "Drop the leg straight back to stance immediately - a hanging leg gets grabbed.",
            "A single hard check can end the opponent's kicking game for the fight.",
            "Drill slow first: the timing is everything and the shins need conditioning.",
        ],
        "requirements": [
            "A partner who throws controlled low kicks on cue.",
            "Shin guards for both partners during check drills.",
            "Thai pads for the kicker to practice against a checking defender.",
            "Patience: shin conditioning builds over months, not sessions.",
        ],
        "standards": [
            "The check is up before the kick arrives - late checks get the thigh anyway.",
            "Contact is shin-to-shin, never foot-to-shin.",
            "The hands never drop during the check.",
            "The leg returns to stance within one beat; no lingering.",
        ],
        "citations": [
            "Gracie R, Gracie R. Brazilian Jiu-Jitsu: Theory and Technique. Invisible Cities Press; 2001 (leg kick defense).",
            "Association of Boxing Commissions. Unified Rules of Mixed Martial Arts (legal kicking targets).",
        ],
        "sig_lens": (
            "The check is the Signature's hard edge: the attacker's "
            "stroke meets bone instead of flesh, and the page defends "
            "itself by being exactly where the kick did not expect."
        ),
    },
    {
        "key": "single_leg",
        "name": "The Single Leg Takedown",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The single leg takedown attacks one leg: the fighter changes "
            "level, penetrates to the opponent's lead leg, wraps it tight "
            "to the chest, and finishes by running the pipe, tripping, or "
            "dumping. It is more versatile than the double leg because it "
            "can be shot from more angles and finished in more ways - "
            "against the cage it becomes a high-percentage weapon - but it "
            "exposes the attacker to the guillotine and the sprawl if the "
            "head is in the wrong place. The finish menu: run the pipe "
            "(lift the leg and run laterally while driving the shoulder), "
            "the trip (hook the far ankle), or the dump (lift and rotate). "
            "Head position decides everything: head inside (ear to the "
            "ribs) is safe from the guillotine; head outside invites it."
        ),
        "how_it_works": (
            "Change level with the knees, step deep with the lead foot to "
            "the outside of the opponent's lead foot, and wrap both arms "
            "around their lead leg - one hand cupping behind the knee, the "
            "other locking over it - pulling the leg tight to the chest "
            "with the head pressed to the inside of their thigh (ear "
            "against the ribs). Keep the back straight and the hips under. "
            "For the run-the-pipe finish: lift the trapped leg high, step "
            "laterally across while driving the shoulder into their hip, "
            "and run them down. For the trip: keep the leg tight, step the "
            "rear foot behind their far ankle, and kick it out while "
            "driving forward. For the dump: lift the leg, turn the corner, "
            "and rotate them over the trapped leg. Drill each finish "
            "separately with a cooperative partner, then chain: if they "
            "hop away from the pipe, the trip is there; if they plant "
            "against the trip, the dump opens. Never let the head drift "
            "to the outside of the leg - that is the guillotine's doorway."
        ),
        "key_points": [
            "Wrap the lead leg tight to the chest, head to the inside - ear against the ribs.",
            "Head outside the leg invites the guillotine; head inside is the safe finish.",
            "Three finishes: run the pipe, trip the far ankle, or lift and dump.",
            "Chain the finishes: pipe defended becomes trip, trip defended becomes dump.",
            "Level change from the knees; the back stays straight through the shot.",
            "Keep the trapped leg high and tight - a low, loose single leg gets sprawled on.",
            "Against the cage the single leg is a high-percentage weapon - the wall kills the escape.",
            "Finish past the takedown into side control or a heavy top position.",
        ],
        "requirements": [
            "Wrestling mats for shot and finish drilling.",
            "A partner who gives realistic hop-away and sprawl reactions.",
            "Neck warm-up - the head positioning loads the neck.",
            "Knee pads for high-rep penetration steps.",
        ],
        "standards": [
            "The head is inside the leg on every rep - outside-head reps are stopped.",
            "The trapped leg is pulled above the attacker's hip before the finish.",
            "The attacker chains at least two finishes when the first is defended.",
            "Balance holds through the finish; the attacker lands on top, not in a scramble.",
        ],
        "citations": [
            "Gracie R, Gracie R. Brazilian Jiu-Jitsu: Theory and Technique. Invisible Cities Press; 2001 (single leg for MMA).",
            "Kodokan. Kodokan Judo: Throwing Techniques. Kodansha; 2014 (ashi-waza leg technique principles).",
        ],
        "sig_lens": (
            "The single leg is the Signature's focused line: one leg "
            "taken, held close, and the three finishes the three ways the "
            "sentence can end - run, trip, or turned clean over."
        ),
    },
    {
        "key": "clinch",
        "name": "The Clinch",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The clinch is the standing grapple: chest-to-chest or "
            "shoulder-to-shoulder, each fighter fighting for the "
            "underhook - the arm threaded under the opponent's armpit and "
            "up their back. Whoever owns the underhooks owns the clinch: "
            "underhooks control posture, set up takedowns, and shut down "
            "the opponent's offense. The pummeling drill - swimming the "
            "arms in and out for underhook position - is the clinch's "
            "foundational exercise. From the clinch come dirty boxing "
            "(short punches inside), knees, elbows, foot sweeps, and "
            "takedowns. In MMA the clinch usually happens against the "
            "cage, where the wall becomes a third grappler."
        ),
        "how_it_works": (
            "Close the distance with a jab or a level change, step "
            "chest-to-chest, and immediately swim for the underhook: "
            "drive the hand, palm up, under the opponent's armpit and up "
            "between their shoulder blades, keeping the elbow tight so "
            "they cannot re-pummel. The other hand controls their bicep "
            "or wrist, or takes the overhook (arm over theirs, hooking "
            "down). Head position: forehead into their jaw or temple, "
            "driving their posture back - never let them get head "
            "position on you. From the double underhooks (both arms in), "
            "lift and arch to break their posture, then attack: the "
            "outside trip, the body lock takedown, or short knees to the "
            "thighs. Pummeling drill: partners take turns swimming for "
            "the inside position, three-minute rounds, staying chest-to-"
            "chest. Losing the underhook battle means losing the clinch - "
            "re-pummel immediately, never accept the overhook."
        ),
        "key_points": [
            "The underhook is the clinch's currency: arm under the armpit, hand up the back, elbow tight.",
            "Whoever owns the underhooks controls posture, takedowns, and offense.",
            "Head position wins: forehead into their jaw drives their posture back.",
            "Pummeling - swimming for inside position - is the foundational clinch drill.",
            "From double underhooks: lift, arch, and attack the trip, body lock, or knees.",
            "Dirty boxing: short hooks and uppercuts inside the clinch where big punches cannot fit.",
            "Never accept the overhook - re-pummel immediately when you lose inside position.",
            "Against the cage the clinch multiplies: the wall removes their retreat.",
        ],
        "requirements": [
            "Mats and ideally a cage wall or padded wall for clinch work.",
            "A partner for pummeling rounds (three minutes, continuous).",
            "Mouthguard - clinch work gets physical fast.",
            "Neck and shoulder warm-up for head-position battles.",
        ],
        "standards": [
            "The underhook hand reaches the shoulder blade, not just the armpit.",
            "The elbow stays tight to the body - a wide underhook gets re-pummeled.",
            "Head position is forehead-to-jaw, never forehead-to-chest (which gives them your neck).",
            "The student re-pummels within two seconds of losing inside position.",
        ],
        "citations": [
            "Gracie R, Gracie R. Brazilian Jiu-Jitsu: Theory and Technique. Invisible Cities Press; 2001 (clinch for MMA).",
            "Kodokan. Kodokan Judo: Throwing Techniques. Kodansha; 2014 (gripping and posture control).",
        ],
        "sig_lens": (
            "The clinch is the Signature's handshake: chest to chest, "
            "the underhook the arm extended underneath in agreement - "
            "whoever holds the inside holds the terms."
        ),
    },
    {
        "key": "thai_clinch",
        "name": "The Thai Clinch and Knees",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The Thai clinch - the plum - is the double collar tie: both "
            "hands cupped behind the opponent's head, elbows tight, "
            "pulling the head down into rising knees. It is one of the "
            "most damaging positions in MMA because the knees travel a "
            "short, undefended path to the body and head, and the pull "
            "doubles their force - the head comes down as the knee comes "
            "up. Defense is hand-fighting: never let both hands lock "
            "behind the head; swim one hand inside, frame on the bicep, "
            "or circle out. The plum is also a takedown risk for the "
            "holder - a savvy opponent changes level under the high grip. "
            "Knees to the body fold opponents; knees to the head end "
            "fights."
        ),
        "how_it_works": (
            "Swim both hands inside and cup them behind the opponent's "
            "head at the crown - fingers interlaced or one hand over the "
            "other, never on the neck where they slide off. Pull the elbows "
            "tight to the ribs so the opponent cannot swim an arm inside. "
            "Yank the head down sharply as the same-side knee drives up: "
            "the pull and the knee meet in the middle, doubling the "
            "impact. The knee strikes with the point of the knee - the "
            "bony tip - into the solar plexus, ribs, or, if the head is "
            "pulled low, the face. Alternate knees, pulling down on each "
            "one; between knees, re-tighten the grip. To defend: the "
            "instant one hand goes behind the head, swim your same-side "
            "hand inside over their wrist, or frame both forearms on "
            "their biceps and circle out. Drill: one partner holds the "
            "plum lightly and feeds knees to the body pads; the other "
            "practices swimming inside and circling free."
        ),
        "key_points": [
            "Both hands cup the crown of the head; elbows stay tight to the ribs.",
            "Pull the head down as the knee comes up - the collision doubles the force.",
            "Knees strike with the bony point into the body or the pulled-down head.",
            "Alternate knees and re-tighten the grip between strikes.",
            "Defense: swim a hand inside the moment one hand goes behind the head.",
            "Never let the grip slide to the neck - it loses control and the pull.",
            "The plum is a level-change risk: a low opponent can shoot under the high grip.",
            "Knees to the body fold opponents over; that fold sets up the head knee.",
        ],
        "requirements": [
            "Body pads or a partner in a belly pad for knee reps.",
            "A partner for plum hand-fighting drills.",
            "Mouthguard for live clinch rounds.",
            "Hip flexor warm-up - knees are thrown in high volume.",
        ],
        "standards": [
            "The grip is on the crown, fingers interlaced, with no daylight at the elbows.",
            "Each knee is met by a downward pull - pull and knee arrive together.",
            "The defender swims inside within one beat of the grip closing.",
            "The holder's stance stays balanced enough to defend the level change.",
        ],
        "citations": [
            "Gracie R, Gracie R. Brazilian Jiu-Jitsu: Theory and Technique. Invisible Cities Press; 2001 (clinch striking for MMA).",
            "Association of Boxing Commissions. Unified Rules of Mixed Martial Arts (legal knee strikes).",
        ],
        "sig_lens": (
            "The plum is the Signature's seal pressed down: both hands "
            "drawing the head to the page while the knees rise to meet it "
            "- the agreement struck from both sides at once."
        ),
    },
    {
        "key": "guillotine",
        "name": "The Guillotine Choke",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The guillotine choke is the front headlock finisher: the "
            "attacker's arm wraps under the opponent's chin and around "
            "the neck, the hands lock, and the attacker extends - arching "
            "the back, driving the hips, and pulling the elbows down - to "
            "compress the neck. It is the classic answer to a sloppy "
            "takedown: the shooter dives with the head outside, and the "
            "guillotine is waiting. There are two main grips - the arm-in "
            "(the opponent's arm trapped inside the choke) and the high-"
            "elbow (chin strap) variation - but the finish is always "
            "extension plus downward elbow pressure. In training it is "
            "applied with control and released the instant the partner "
            "taps; the margin between pressure and injury is small."
        ),
        "how_it_works": (
            "As the opponent shoots with the head to the outside (or "
            "ducks low), wrap the choking arm deep under their chin so "
            "the blade of the wrist sits against the throat, then circle "
            "the hand around to lock with the other hand - palm to palm, "
            "or a chin-strap grip cupping the chin. Tuck the choking "
            "elbow tight to the ribs. Finish standing or on the ground: "
            "arch the back, thrust the hips forward and up, pull both "
            "elbows down toward the hips, and turn slightly toward the "
            "choking side. The pressure comes from the extension of the "
            "whole body, not from squeezing the arms. From the guard "
            "(sitting up): lock the guillotine, close the guard around "
            "their body, and extend the hips upward while pulling the "
            "elbows down. Drill with a partner shooting slow single legs "
            "head-outside: wrap, lock, extend to the point of control, "
            "release on the tap. Never crank the neck - pressure, not "
            "twisting."
        ),
        "key_points": [
            "The classic answer to a head-outside takedown shot - the guillotine waits for the mistake.",
            "Wrap deep: the wrist blade against the throat, hands locked palm-to-palm or chin-strap.",
            "The choking elbow tucks tight to the ribs; a high elbow leaks the choke.",
            "Finish with whole-body extension - arch the back, drive the hips, pull the elbows down.",
            "Pressure, not cranking: squeeze compresses the neck, twisting injures it.",
            "Works standing, in the guard, or in the sprawl - the mechanics are the same.",
            "Release instantly on the tap; the margin between control and injury is small.",
            "Head-outside is the doorway: teach shooters head-inside to deny it.",
        ],
        "requirements": [
            "A partner who taps early and honestly.",
            "Mats for the guard and sprawl variations.",
            "Slow, controlled entries - never dive for guillotines at full speed in drilling.",
            "Coach supervision for beginners: neck safety is non-negotiable.",
        ],
        "standards": [
            "The wrap is deep before any pressure - shallow wraps are released and re-shot.",
            "The finish shows visible hip extension, not just arm squeezing.",
            "The partner taps from blood-flow pressure, never from neck pain.",
            "Applied and released with full control at every speed.",
        ],
        "citations": [
            "Gracie R, Gracie R. Brazilian Jiu-Jitsu: Theory and Technique. Invisible Cities Press; 2001 (front headlock chokes).",
            "Gracie H. Gracie Jiu-Jitsu Basics instructional series (guillotine mechanics and safety).",
        ],
        "sig_lens": (
            "The guillotine is the Signature's closing bracket: the "
            "head-outside mistake the open parenthesis, the wrap and "
            "extension the line that shuts it - clean, final, released "
            "the moment it is acknowledged."
        ),
    },
    {
        "key": "rnc",
        "name": "The Rear Naked Choke",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The rear naked choke is the back-take finisher and the "
            "highest-percentage submission in MMA: from behind the "
            "opponent, one arm slides under the chin and around the neck, "
            "the other hand locks behind their head, and the squeeze "
            "compresses the carotid arteries. It needs no gi, no "
            "strength advantage, and no complicated setup - just the back "
            "and a free arm. The choke works by blood restriction, so the "
            "defender fades in seconds once it is locked; that speed is "
            "why back control is the most dominant position in the sport "
            "and why every fighter learns both to take the back and to "
            "never give it. Applied in training with care and released on "
            "the tap, it is completely safe; held too long, it is "
            "dangerous - respect is mandatory."
        ),
        "how_it_works": (
            "From back control (seatbelt grip: one arm over the shoulder, "
            "one under the armpit, hands locked), slide the top arm - the "
            "choking arm - under the opponent's chin so the crook of the "
            "elbow sits under the chin and the forearm and bicep press "
            "both sides of the neck. Bring the choking hand to the "
            "opposite shoulder or behind their head, and lock the other "
            "hand behind their head or on the choking bicep. Expand the "
            "chest, arch slightly back, and squeeze the elbows together - "
            "the pressure comes from the chest expansion and the arm "
            "triangle closing, not from pulling with the hands. If the "
            "chin is tucked, use the hand to lift the nose and slide the "
            "arm under - never crank the jaw. Drill: partner gives the "
            "back lightly; slide, lock, apply slow pressure to the point "
            "of the tap, release immediately. The tap is sacred - chase "
            "the position in sparring, never the finish past the tap."
        ),
        "key_points": [
            "The highest-percentage submission in MMA: from the back, one arm under the chin.",
            "The crook of the elbow under the chin; forearm and bicep compress both sides of the neck.",
            "Lock the hands (hand to shoulder, other hand behind the head) and expand the chest.",
            "Pressure from chest expansion and elbow closure - not from yanking with the hands.",
            "Works by blood restriction: seconds to the fade once locked - respect it absolutely.",
            "If the chin is tucked, lift the nose to slide under - never crank the jaw.",
            "Release instantly on the tap, every time, at every intensity.",
            "The back is the goal: every scramble that gives the back invites this finish.",
        ],
        "requirements": [
            "A partner who taps early and a coach who enforces tap discipline.",
            "Mats; back-take drills end on the ground.",
            "Calm, slow application in drilling - speed comes later.",
            "Clear gym rule: no holding past the tap, ever.",
        ],
        "standards": [
            "The choking arm is deep - elbow crook under the chin - before pressure starts.",
            "The finish shows chest expansion, not hand-pulling.",
            "The partner taps from clean blood-flow pressure with no neck pain.",
            "One hundred percent tap compliance: the choke is released the instant the tap is felt.",
        ],
        "citations": [
            "Gracie R, Gracie R. Brazilian Jiu-Jitsu: Theory and Technique. Invisible Cities Press; 2001 (rear naked choke).",
            "Gracie H. Gracie Jiu-Jitsu Basics instructional series (back control and the RNC).",
        ],
        "sig_lens": (
            "The rear naked choke is the Signature's final period: taken "
            "from behind where no argument remains, the arms the two "
            "lines that close the page - applied with honor, released "
            "with honor."
        ),
    },
    {
        "key": "armbar",
        "name": "The Armbar from Mount",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The armbar from mount is the classic joint lock: the attacker "
            "isolates one of the mounted opponent's arms, swings a leg "
            "over their head, and extends the hips to hyperextend the "
            "elbow. It is the first submission most students learn because "
            "the mechanics are pure leverage - the attacker's whole body "
            "against one elbow joint - and it teaches the universal "
            "submission lesson: isolate, control, then apply. From the "
            "mount the setup is the gift-wrap or the high mount: slide "
            "up, trap the arm across the centerline, and swing the leg "
            "over. The finish is the hips rising, never the arms pulling. "
            "In training the armbar is caught and held at the point of "
            "control - the tap comes from pressure, and partners are "
            "never cranked."
        ),
        "how_it_works": (
            "From the mount, slide the knees high under the opponent's "
            "armpits (high mount) to isolate an arm. Trap their wrist to "
            "the chest with both hands, keeping their thumb pointing up. "
            "Swing the same-side leg over their head in a wide arc while "
            "dropping the other knee tight to their ribs - the legs pinch "
            "their head and torso like a vise. Fall back slightly, keeping "
            "their arm trapped across the hips with their thumb up, and "
            "raise the hips toward the ceiling: the elbow hyperextends "
            "over the fulcrum of the hips. Keep their thumb pointing up "
            "throughout - if the thumb turns, the arm rotates out. Control "
            "the far leg with the top leg so they cannot stack. Drill: "
            "partner in mount gives the arm lightly; trap, swing, pinch, "
            "lift the hips to the point of pressure, release on the tap. "
            "The most common failure is pulling with the arms instead of "
            "lifting with the hips - the hips are the engine."
        ),
        "key_points": [
            "Isolate the arm: trap the wrist to the chest, thumb pointing up.",
            "Swing the leg over the head in a wide arc; the other knee pins tight to the ribs.",
            "The legs pinch head and torso - the vise holds the position, not the hands.",
            "Finish by raising the hips; the elbow extends over the hip fulcrum.",
            "Never pull with the arms - the hips are the engine of the armbar.",
            "Thumb stays up; a turning thumb means the arm is rotating out.",
            "Control the far leg so the opponent cannot stack out of the lock.",
            "Catch and hold at the point of control - partners are never cranked.",
        ],
        "requirements": [
            "A partner who taps early on elbow pressure.",
            "Mats with room for the leg swing.",
            "Slow, technical reps before any speed - the elbow is unforgiving.",
            "Coach supervision until the control point is reliable.",
        ],
        "standards": [
            "The arm is isolated and the thumb is up before the hips lift.",
            "The finish shows visible hip elevation, not arm-pulling.",
            "The partner taps from clean elbow pressure with no shoulder pain.",
            "The position is held with leg pressure alone before the finish is applied.",
        ],
        "citations": [
            "Gracie R, Gracie R. Brazilian Jiu-Jitsu: Theory and Technique. Invisible Cities Press; 2001 (juji-gatame armbar).",
            "Kodokan. Kodokan Judo: Throwing Techniques. Kodansha; 2014 (kansetsu-waza joint lock principles).",
        ],
        "sig_lens": (
            "The armbar is the Signature's straightedge: one arm "
            "isolated, the hips the fulcrum, the line drawn past straight "
            "- leverage so honest it needs no strength to sign."
        ),
    },
    {
        "key": "gnp",
        "name": "Ground and Pound Fundamentals",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Ground and pound is MMA's signature offense: from a top "
            "position - mount, side control, or inside the guard - the "
            "fighter postures up and strikes the grounded opponent with "
            "punches, elbows, and hammerfists. It is what separates MMA "
            "grappling from pure grappling sports: the bottom fighter is "
            "not just losing position, they are taking damage, and every "
            "escape attempt must survive the strikes. The keys are posture "
            "(sitting tall with a straight back so the strikes have "
            "leverage), base (wide knees, heavy hips so the bottom fighter "
            "cannot buck), and strike selection (short punches and elbows "
            "that do not sacrifice position). Wild, lunging ground strikes "
            "lose the position; controlled, postured strikes end fights."
        ),
        "how_it_works": (
            "From the mount: slide the knees wide for base, sit the hips "
            "heavy, and posture up tall - chest high, back straight, hands "
            "free. Pin the opponent's hips with the weight; if they bridge, "
            "ride the bridge by posting a hand and keeping the hips heavy. "
            "Strike with short, chopping punches and elbows: the power "
            "comes from dropping the shoulder and rotating the torso, not "
            "from winding up. Alternate targets - head, body, head - so "
            "the defender cannot shell one line. When they turn to escape, "
            "take the gift: an exposed arm becomes an armbar, a turned "
            "back becomes the rear naked choke. From side control: pin the "
            "far hip and near shoulder, posture slightly, and drop short "
            "elbows and punches. From inside the guard: posture tall with "
            "both hands on their torso or biceps, and throw straight "
            "punches down the middle. Drill on a heavy bag on the ground: "
            "mount the bag, posture, and throw controlled thirty-second "
            "flurries while a partner rocks the bag to simulate bucking."
        ),
        "key_points": [
            "Posture is the weapon: sit tall with a straight back so strikes have leverage.",
            "Base defeats the buck: wide knees, heavy hips, ride the bridges.",
            "Short, controlled strikes - punches, elbows, hammerfists - never wild lunges.",
            "Alternate head and body so the defender cannot shell one line.",
            "Every escape attempt is a submission gift: the exposed arm, the turned back.",
            "From the guard, posture tall with hands controlling the torso before striking.",
            "Ground strikes that sacrifice position are bad trades - control first, damage second.",
            "The bottom fighter's panic is the top fighter's patience: let them spend themselves.",
        ],
        "requirements": [
            "A heavy bag that can be mounted on the ground.",
            "A partner who bucks realistically from the bottom.",
            "Mouthguard and gloves for live top-position rounds.",
            "Hip and core endurance - postured striking is exhausting.",
        ],
        "standards": [
            "The top fighter maintains the position through a full thirty-second flurry.",
            "Strikes are short and the base never narrows during the flurry.",
            "The bottom fighter's escape attempts are converted to submission threats.",
            "Posture is regained immediately after any strike - no staying bent over.",
        ],
        "citations": [
            "Gracie R, Gracie R. Brazilian Jiu-Jitsu: Theory and Technique. Invisible Cities Press; 2001 (strikes integrated with grappling).",
            "Association of Boxing Commissions. Unified Rules of Mixed Martial Arts (legal grounded strikes).",
        ],
        "sig_lens": (
            "Ground and pound is the Signature written from above: "
            "posture the steady hand, base the firm desk, each short "
            "strike a deliberate mark - control the page, then write on it."
        ),
    },
    {
        "key": "guard_pass",
        "name": "Guard Passing",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Guard passing is the art of getting past the opponent's legs "
            "from inside their guard to reach side control or mount. The "
            "guard is the bottom fighter's fortress - legs controlling the "
            "hips, hands fighting posture - and passing it means defeating "
            "the legs without getting swept or submitted. The three "
            "families: the stack pass (fold the guard player, drive the "
            "legs over their head, circle to side control), the smash pass "
            "(over-under grip, shoulder pressure, slide through), and the "
            "leg drag (drag one leg across, sprint to side control). All "
            "passing shares principles: posture first, control one leg, "
            "kill the hips, never leave both arms inside. A passer who "
            "rushes gets triangled; a passer who is patient and heavy gets "
            "through."
        ),
        "how_it_works": (
            "For the stack pass: from inside the closed guard, posture "
            "tall, open the guard by standing (hands on their hips, one "
            "knee up, stand and push the hips down), then immediately "
            "underhook one leg, drive the shoulder into their torso, and "
            "stack their legs over their own head - folding them - while "
            "circling the free leg to side control. For the over-under "
            "smash pass: from half guard, get the underhook on one side "
            "and the overhook (head control) on the other, drive the "
            "shoulder into their face, flatten them, and slide the knee "
            "through to side control. For the leg drag: control both "
            "ankles, drag one leg hard across the body while sprinting the "
            "hips to the opposite side, landing in side control with the "
            "dragged leg trapped. Drill: partner plays open guard with "
            "fifty percent resistance; the student passes, holds side "
            "control for three seconds, resets. Never reach both arms "
            "inside the guard - that is the triangle's invitation."
        ),
        "key_points": [
            "Posture first, always: a broken-posture passer is a swept passer.",
            "Control one leg completely before advancing - half-controlled legs re-guard.",
            "Stack pass: fold the legs over, circle to side control.",
            "Smash pass: over-under grips, shoulder pressure, slide the knee through.",
            "Leg drag: drag one leg across, sprint the hips to side control.",
            "Never leave both arms inside the guard - that invites the triangle and armbar.",
            "Kill the hips: pin or fold them so the guard player cannot move.",
            "Pass slowly and heavy; rushing the pass is how submissions happen.",
        ],
        "requirements": [
            "A partner who plays realistic guard with progressive resistance.",
            "Mats with room to stack and circle.",
            "Three-second side-control holds to prove each pass.",
            "Core strength for the stacking pressure.",
        ],
        "standards": [
            "Each pass ends in a three-second side-control or mount hold.",
            "The passer is never swept or submitted during fifty-percent-resistance rounds.",
            "Posture is maintained through the entire pass - no head-down bull rushes.",
            "Both arms are never inside the guard at once.",
        ],
        "citations": [
            "Gracie R, Gracie R. Brazilian Jiu-Jitsu: Theory and Technique. Invisible Cities Press; 2001 (guard passing).",
            "Gracie H. Gracie Jiu-Jitsu Basics instructional series (passing the guard safely).",
        ],
        "sig_lens": (
            "Passing the guard is the Signature turning the page: the "
            "legs the closed cover, posture the hand that opens it, and "
            "side control the clean sheet finally reached."
        ),
    },
    {
        "key": "tdd",
        "name": "Takedown Defense",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Takedown defense is the complete system for staying on the "
            "feet: the sprawl, the whizzer (overhook), hand-fighting, hip "
            "positioning, and cage awareness working as one. The sprawl "
            "answers the committed shot; the whizzer - the overhook thrown "
            "over the shooter's shoulder - breaks their posture and sets "
            "up the counter; hand-fighting (controlling the wrists and "
            "head) prevents the shot from ever starting; and hip distance "
            "(keeping the hips back and low) makes every entry longer and "
            "weaker. Elite takedown defense is layered: the first layer "
            "is distance and strikes that punish entries, the second is "
            "the sprawl and whizzer, the third is the scramble back to the "
            "feet if taken down. Fighters with great takedown defense "
            "dictate where the fight happens."
        ),
        "how_it_works": (
            "Layer one - prevention: keep the lead hand busy with jabs "
            "and the hips back; when the opponent changes level, meet "
            "them with a short uppercut or knee - the intercepting strike "
            "is the cheapest takedown defense. Layer two - the sprawl and "
            "whizzer: sprawl hard on the committed shot as in the "
            "fundamentals, and when they get to a leg, throw the whizzer - "
            "the near arm whips over their shoulder in a deep overhook, "
            "the hips drive down, and the far hand crossfaces - breaking "
            "their posture sideways. From the whizzer, limp-leg out: pull "
            "the trapped leg back and circle away. Layer three - hand "
            "fighting: control their wrists, keep a hand on their head, "
            "and never let them tie up both legs uncontested. Drill the "
            "gauntlet: a partner shoots ten times in a row - sprawl five, "
            "whizzer three, intercept two - and the student must stay "
            "standing through all ten."
        ),
        "key_points": [
            "Takedown defense is layered: intercept, sprawl and whizzer, then scramble.",
            "The intercepting uppercut or knee on the level change is the cheapest defense.",
            "The whizzer - deep overhook over the shooter's shoulder - breaks posture sideways.",
            "From the whizzer: drive the hips down, crossface, limp-leg out.",
            "Hand-fighting prevents shots: control the wrists and keep a hand on their head.",
            "Keep the hips back and low; long entries are weak entries.",
            "Drill the gauntlet: ten shots in a row, stay standing through all of them.",
            "Great takedown defense dictates where the fight happens - it is strategic, not just technical.",
        ],
        "requirements": [
            "Mats for sprawl and scramble reps.",
            "A partner who shoots with increasing commitment.",
            "Gloves for intercept-strike timing drills.",
            "Wrestling shoes or bare feet per gym rules for hip mobility.",
        ],
        "standards": [
            "The student stays standing through ten consecutive shots in the gauntlet drill.",
            "The whizzer is thrown over the shoulder, not around the waist.",
            "Intercepts land as the level change starts, not after the shot is deep.",
            "Hips stay back and low through hand-fighting exchanges.",
        ],
        "citations": [
            "Gracie R, Gracie R. Brazilian Jiu-Jitsu: Theory and Technique. Invisible Cities Press; 2001 (takedown defense for MMA).",
            "Kodokan. Kodokan Judo: Throwing Techniques. Kodansha; 2014 (defensive gripping and posture).",
        ],
        "sig_lens": (
            "Takedown defense is the Signature defending its page: the "
            "intercept the raised hand, the sprawl the weight of the "
            "book, the whizzer the arm barred across the sentence - the "
            "fight stays where the author wants it."
        ),
    },
    {
        "key": "cage_wrestling",
        "name": "Cage Wrestling",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Cage wrestling is grappling against the fence: pinning the "
            "opponent to the wall, controlling them with underhooks and "
            "head position, and attacking takedowns the cage makes "
            "unavoidable - or, from the pinned side, wall-walking back to "
            "the feet. The cage is a weapon for the presser: it removes "
            "the retreat, so every drive goes somewhere. The pinner's "
            "tools are the body lock, the double underhooks, foot stomps "
            "and short knees to soften, and the outside trip. The pinned "
            "fighter's tools are the whizzer, wrist control, hip "
            "positioning (hips back, never flat on the fence), and the "
            "wall walk - posting on the cage and climbing the feet up to "
            "stand. Rounds are won and lost in the clinch against the "
            "fence; it is exhausting, technical, invisible work."
        ),
        "how_it_works": (
            "As the pinner: drive chest-to-chest into the fence, win the "
            "underhooks, and put the forehead into their jaw to break "
            "their posture. Keep the hips close - daylight lets them "
            "wall-walk. Attack in rhythm: short knees to the thighs, then "
            "the outside trip (hook their far ankle with the near foot "
            "while driving), or the body lock lift (lock the hands around "
            "the waist, lift, and rotate them down). As the pinned "
            "fighter: never go flat - keep the hips back and one foot "
            "posted for base. Whizzer hard on their underhook side, "
            "control a wrist, and wall-walk: post a hand on the fence, "
            "walk the feet up the cage, and hip-heist out to the side. "
            "Drill: three-minute cage rounds, switching pinner and pinned "
            "every minute. The pinner's goal is the takedown; the pinned "
            "fighter's goal is separation or the wall walk - both score "
            "the round."
        ),
        "key_points": [
            "The cage removes retreat: for the pinner it is a weapon, for the pinned a trap.",
            "Pinner's base: double underhooks, forehead in the jaw, hips tight.",
            "Pinner's attacks: short knees, the outside trip, the body lock lift.",
            "Pinned fighter: never go flat on the fence - hips back, one foot posted.",
            "The wall walk: post on the cage, walk the feet up, hip-heist out.",
            "Whizzer and wrist control are the pinned fighter's best friends.",
            "Cage rounds are won in the invisible work: posture battles and hand-fighting.",
            "Separate with a push and a pivot when the pin loosens - never just shove and stand still.",
        ],
        "requirements": [
            "A cage wall or padded wall - this cannot be drilled in open mat alone.",
            "A partner for three-minute pinner/pinned rounds.",
            "Mouthguard; cage wrestling is grinding and physical.",
            "Shoulder and neck warm-up for the posture battles.",
        ],
        "standards": [
            "The pinner holds the pin and lands offense for the majority of the round.",
            "The pinned fighter wall-walks or separates at least once per round.",
            "The pinned fighter's hips never rest flat on the fence for more than a few seconds.",
            "Underhook battles are continuous - neither side accepts the overhook passively.",
        ],
        "citations": [
            "Gracie R, Gracie R. Brazilian Jiu-Jitsu: Theory and Technique. Invisible Cities Press; 2001 (cage grappling for MMA).",
            "Association of Boxing Commissions. Unified Rules of Mixed Martial Arts (fence-grabbing prohibitions).",
        ],
        "sig_lens": (
            "Cage wrestling is the Signature at the page's edge: the "
            "fence the margin that will not move, the pinner writing "
            "into the corner, the wall-walk the climb back to open paper."
        ),
    },
    {
        "key": "sub_defense",
        "name": "Submission Defense",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Submission defense is the system for surviving and escaping "
            "locked submissions: hand-fighting (peeling the gripping "
            "hands), posture (the structural defense that precedes all "
            "others), and the specific escapes for each threat. The "
            "universal rule is early defense: a choke defended at the "
            "first grip is a nuisance; the same choke defended three "
            "seconds later is a finish. Against armlocks, the defense is "
            "hand-fighting the wrist and stacking the weight; against "
            "chokes, it is tucking the chin, hand-fighting, and addressing "
            "the choking arm before the lock closes. The deeper truth: "
            "position before submission applies to defense too - the best "
            "submission defense is never letting the position get bad, "
            "and the second-best is exploding out the instant the lock "
            "starts."
        ),
        "how_it_works": (
            "Against the armbar: the instant the arm is isolated, grip "
            "the hands together (palm-to-palm or figure-four on the own "
            "wrist), tuck the elbow to the ribs, and stack - drive the "
            "weight forward over the attacker to kill the hip angle - then "
            "circle the trapped elbow toward their legs to pull it free. "
            "Against the rear naked choke: tuck the chin hard, get both "
            "hands to the choking arm, peel the top hand down, and turn "
            "into the choke (toward the choking-arm side) to relieve "
            "pressure while hand-fighting. Against the guillotine: posture "
            "up immediately, get the choking elbow off the ribs by "
            "addressing it with both hands, and circle toward the "
            "non-choking side. Against the triangle: posture up, stack "
            "the legs over, and peel the ankle. Drill the recognition "
            "round: a partner applies each submission to the point of "
            "control (never past), and the student performs the first two "
            "defensive moves and resets. Early beats late, every time."
        ),
        "key_points": [
            "Early defense wins: address the submission at the first grip, not at the lock.",
            "Hand-fighting is the universal first defense - peel the gripping hands.",
            "Posture is structural defense: tall posture defeats most chokes before they start.",
            "Armbar defense: grip the hands, tuck the elbow, stack the weight, circle free.",
            "Rear naked choke defense: chin down, two hands on the choking arm, turn into it.",
            "Guillotine defense: posture up instantly and address the choking elbow.",
            "Triangle defense: posture and stack - never stay bent inside it.",
            "Tap early in training: the tap is the tuition that buys the lesson.",
        ],
        "requirements": [
            "A partner who applies submissions to control only, never past.",
            "Absolute tap discipline from both partners.",
            "Mats for the stacking and circling escapes.",
            "A coach to verify the escapes before live application.",
        ],
        "standards": [
            "The student performs the correct first two defensive moves for each major submission.",
            "Defenses are attempted at the grip stage, not after the lock closes.",
            "No partner is ever held past the tap in drilling.",
            "Posture is the default: the student postures up the instant a submission starts.",
        ],
        "citations": [
            "Gracie R, Gracie R. Brazilian Jiu-Jitsu: Theory and Technique. Invisible Cities Press; 2001 (submission escapes).",
            "Gracie H. Gracie Jiu-Jitsu Basics instructional series (defending submissions safely).",
        ],
        "sig_lens": (
            "Submission defense is the Signature's proofreader: the "
            "early hand-fight the catch of the first error, posture the "
            "clean manuscript - the page corrected before the mistake is "
            "inked."
        ),
    },
    {
        "key": "transitions",
        "name": "Submission Chains and Transitions",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Submission chains are linked attacks where each submission "
            "sets up the next: the armbar defended becomes the triangle, "
            "the triangle defended becomes the omoplata, the omoplata "
            "defended becomes the sweep. Advanced grapplers do not hunt "
            "single submissions - they hunt reactions, and every defense "
            "the opponent chooses opens the next attack. The classic "
            "mount chain: attack the armbar, and when they pull the arm "
            "free, the legs are already falling into the triangle; when "
            "they posture out of the triangle, the omoplata shoulder lock "
            "is waiting; when they roll out of that, they give the back. "
            "Chaining works because defending a submission requires "
            "commitment - the arms go here, the posture goes there - and "
            "commitment is predictable. The chain never pauses: attack, "
            "read the defense, attack the opening."
        ),
        "how_it_works": (
            "From the mount, isolate the arm and attack the armbar as in "
            "the fundamentals. When the opponent yanks the arm free and "
            "pulls it back, do not chase it - let the momentum carry the "
            "legs: swing the leg over the head into the triangle position, "
            "lock the figure-four with the legs around their head and arm, "
            "and pull the head down. When they posture up hard to break "
            "the triangle, sit up with them, thread the arm through for "
            "the omoplata (shoulder lock), and roll them forward over the "
            "trapped shoulder. When they roll to escape the omoplata, "
            "follow the roll and take the back. Each transition is drilled "
            "as a two-link chain first: armbar-to-triangle for a week, "
            "then triangle-to-omoplata, then the full three-link chain. "
            "The rule of the chain: never re-attack a defended submission "
            "twice in a row - the second attack is always the next link. "
            "Flow rolling (light, continuous, no finishing) is where "
            "chains are born."
        ),
        "key_points": [
            "Chains hunt reactions: every defense opens the next attack.",
            "The classic chain: armbar defended becomes triangle, triangle defended becomes omoplata.",
            "Never re-attack a defended submission twice - the second attack is the next link.",
            "The chain never pauses: attack, read the defense, attack the opening.",
            "Drill two-link chains first, then assemble the full chain.",
            "Flow rolling - light and continuous - is where chains are learned.",
            "Each link must be a real threat; fake attacks get ignored, not defended.",
            "The end of every chain is a dominant position even if no submission lands.",
        ],
        "requirements": [
            "Solid single submissions first - chains multiply real threats, not wishes.",
            "A partner who defends realistically at increasing resistance.",
            "Mats and time: chain drilling needs long, unhurried rounds.",
            "Flow-rolling partners who value movement over winning.",
        ],
        "standards": [
            "The student demonstrates at least one three-link chain against resistance.",
            "No link is re-attacked twice in a row during chain rounds.",
            "Transitions show no pause - the next attack starts as the defense commits.",
            "Every chain ends in a dominant position or a submission, never in a scramble loss.",
        ],
        "citations": [
            "Gracie R, Gracie R. Brazilian Jiu-Jitsu: Theory and Technique. Invisible Cities Press; 2001 (combination attacks).",
            "Danaher J. Enter the System instructional series (submission combinations and transitions).",
        ],
        "sig_lens": (
            "The chain is the Signature's paragraph: each submission a "
            "sentence, each defense the reader's turn of the page - and "
            "the author already writing the next line."
        ),
    },
    {
        "key": "feints",
        "name": "Feints and Striking Setups",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Feints are false attacks - a shoulder twitch, a level drop, "
            "a half-step - that draw a defensive reaction and open the "
            "real strike. Advanced striking is mostly setup: the knockout "
            "rarely comes from the first punch thrown, it comes from the "
            "third thing the opponent saw, when their guard is committed "
            "to the wrong answer. The jab feint draws the parry and opens "
            "the cross; the level-change feint draws the sprawl posture "
            "and opens the overhand; the low-kick feint lifts the check "
            "and opens the head kick. Feints must look real - the shoulder "
            "must move, the hips must turn - because opponents react to "
            "the first inches of a strike, and a lazy feint draws nothing. "
            "The setup game is information warfare: show them one thing "
            "twice, then punish the habit on the third."
        ),
        "how_it_works": (
            "The jab feint: twitch the lead shoulder and take the small "
            "jab step without extending the arm - when the opponent's "
            "rear hand lifts to parry, fire the real cross through the "
            "opening. The level-change feint: dip the knees as if shooting "
            "- when their hands drop to defend the takedown, come up with "
            "the overhand right or the head kick. The kick feint: lift the "
            "knee as if kicking low - when they check, step down and punch "
            "through the guard they left. Drill the pattern rule: show the "
            "feint twice as a real strike first (two real jabs), then "
            "feint the third - the opponent's habit is now the weapon. "
            "Sparring constraint round: the student may only land strikes "
            "that follow a feint - this forces the setup game. Feints are "
            "thrown with the whole body: a shoulder-only feint fools no "
            "one past the beginner level."
        ),
        "key_points": [
            "Feints draw reactions: a twitch, a level drop, a half-step that looks like the real attack.",
            "The real strike lands on the reaction - feint the jab, land the cross on the parry.",
            "Feints must look real: the shoulder moves, the hips turn, the step commits.",
            "Show it twice real, then feint the third - habits are built, then punished.",
            "Level-change feints open head strikes; strike feints open takedowns.",
            "Opponents react to the first inches of a strike - the feint only needs those inches.",
            "Drill the constraint: only strikes after feints may land, to force the setup habit.",
            "Lazy feints draw nothing and waste energy - commit to the false attack.",
        ],
        "requirements": [
            "A sparring partner with honest reactions to drill against.",
            "The single strikes must be credible first - feints need a real threat behind them.",
            "Video review: feints that do not draw reactions are visible on film.",
            "Controlled sparring rounds dedicated to setup work.",
        ],
        "standards": [
            "The student's feints draw visible defensive reactions in sparring.",
            "At least one clean setup strike lands per round in constraint sparring.",
            "Feints use full-body commitment, not shoulder-only twitches.",
            "The pattern rule is applied: real-real-feint, not random fakes.",
        ],
        "citations": [
            "Dempsey J. Championship Fighting: Explosive Punching and Aggressive Defense. 1950 (feinting and drawing the lead).",
            "Sheridan S. The Fighter's Mind: Inside the Mental Game. Grove Press; 2010 (timing and deception).",
        ],
        "sig_lens": (
            "The feint is the Signature's draft line: drawn lightly so "
            "the reader reacts, then the true stroke laid over the "
            "opening - the page turned by its own expectation."
        ),
    },
    {
        "key": "elbows",
        "name": "Elbows and Close Range Striking",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Elbows are the close-range blade of MMA: short, hard, and "
            "fight-ending in the clinch and on the ground where punches "
            "have no room to travel. The elbow's bony point concentrates "
            "force on a tiny area, which is why elbows cut - a clean "
            "elbow opens the skin above the eye and changes the fight. The "
            "horizontal elbow arcs across at head height; the upward elbow "
            "drives from low to high inside the clinch; the downward "
            "twelve-to-six elbow is illegal under the Unified Rules and is "
            "never thrown. Elbows integrate with the whole close game: the "
            "Thai clinch feeds upward elbows, the sprawl feeds the "
            "spinning elbow on the break, and ground-and-pound finishes "
            "with short elbows that never sacrifice position."
        ),
        "how_it_works": (
            "The horizontal elbow: from the clinch or close range, raise "
            "the elbow to shoulder height, keep the fist near the ear, "
            "and whip the hips to swing the elbow on a tight horizontal "
            "arc - the point of the elbow, not the forearm, makes "
            "contact. The upward elbow: drop the elbow slightly and drive "
            "it up the centerline inside the clinch, the hips thrusting "
            "forward behind it. From the sprawl: as the opponent stands "
            "back up, the near elbow can spin across on the break - "
            "thrown with control in drilling. On the ground from mount or "
            "side control: post the hand and drop short, chopping elbows "
            "that travel six inches and land with the point. Never throw "
            "the twelve-to-six downward elbow - it is illegal and it is "
            "drilled out of the repertoire. Pad drill: the coach holds a "
            "pad at temple height in the clinch; the student throws "
            "alternating horizontal elbows with full hip whip, the fist "
            "staying glued near the ear."
        ),
        "key_points": [
            "The elbow's bony point concentrates force - short range, high damage, and cuts.",
            "Horizontal elbow: tight arc at head height, fist near the ear, hips whip it through.",
            "Upward elbow: drives up the centerline inside the clinch.",
            "The twelve-to-six downward elbow is illegal - never thrown, never drilled.",
            "Elbows fit where punches cannot: the clinch, the break, and tight ground positions.",
            "Short ground elbows travel inches and never sacrifice top position.",
            "The point makes contact, never the forearm - the forearm is a block, not a blade.",
            "Elbows that cut change fights: target the brow line where cuts matter most.",
        ],
        "requirements": [
            "Elbow pads for the holder in clinch elbow drills.",
            "A partner holding pads at temple height in the clinch.",
            "Clear rule knowledge: twelve-to-six is out, always.",
            "Control first - elbows are drilled light until accuracy is proven.",
        ],
        "standards": [
            "Contact is always the point of the elbow, verified on pads.",
            "No twelve-to-six motion appears at any speed in drilling.",
            "The hips drive every elbow - arm-only elbows are corrected.",
            "Ground elbows keep the top position secure through the strike.",
        ],
        "citations": [
            "Gracie R, Gracie R. Brazilian Jiu-Jitsu: Theory and Technique. Invisible Cities Press; 2001 (elbow strikes for MMA).",
            "Association of Boxing Commissions. Unified Rules of Mixed Martial Arts (twelve-to-six elbow prohibition).",
        ],
        "sig_lens": (
            "The elbow is the Signature's sharpest nib: no room for the "
            "broad stroke, so the point does the work - small, exact, "
            "and decisive at close range."
        ),
    },
    {
        "key": "sweeps",
        "name": "Sweeps and Reversals",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Sweeps reverse position from the bottom: the guard player "
            "off-balances the top fighter and rolls them over to land on "
            "top. The scissor sweep - one leg chopping across the torso "
            "while the other blocks the base - and the hip bump sweep - "
            "sitting up hard into an overhooking opponent - are the two "
            "foundational reversals, and together they form a classic "
            "combination: the opponent defends the scissor by posting, "
            "and the post opens the hip bump. Sweeps are the bottom "
            "fighter's takedowns, and they score the same lesson: "
            "off-balance first, then technique. A sweep that moves the "
            "opponent without breaking their balance is just exercise; "
            "the kuzushi - the breaking of balance - is the sweep."
        ),
        "how_it_works": (
            "The scissor sweep: from closed guard, control one sleeve (or "
            "wrist) and the same-side collar, open the guard, and place "
            "the same-side foot on the mat blocking their hip. Pull their "
            "weight toward the blocked side with the grips while the "
            "other leg chops across their torso like a scissor blade - the "
            "combination of pull, block, and chop tips them over the "
            "blocked hip; follow them up to land in mount. The hip bump: "
            "when they overhook to stop the scissor, sit up explosively, "
            "wrap the overhooking arm tight, and bump the hips through to "
            "roll them over the trapped side. Drill the pair: partner "
            "defends the scissor by posting the free hand - the student "
            "immediately switches to the hip bump on the posted arm. The "
            "timing cue for all sweeps: attack when their weight is "
            "moving, not when it is settled - a moving base is a breakable "
            "base."
        ),
        "key_points": [
            "Sweeps are the bottom fighter's takedowns: off-balance first, then technique.",
            "Scissor sweep: block the hip, chop across the torso, pull with the grips.",
            "Hip bump sweep: sit up explosively into the overhook and roll them over.",
            "The classic pair: scissor defended by posting opens the hip bump.",
            "Kuzushi - breaking the balance - is the sweep; moving them without it is exercise.",
            "Attack when their weight is moving, not settled.",
            "Follow the sweep up: land in mount or side control, never in a scramble.",
            "Grip fighting decides sweeps: win the sleeve and collar before the legs move.",
        ],
        "requirements": [
            "A partner who gives realistic base and posts.",
            "Mats with room to follow sweeps into mount.",
            "The closed guard must be solid first - sweeps need the platform.",
            "Hip mobility for the sit-up explosion of the hip bump.",
        ],
        "standards": [
            "Each sweep lands the student in mount or side control, not a scramble.",
            "The scissor-to-hip-bump switch happens within one beat of the post.",
            "The opponent's balance visibly breaks before the technique moves.",
            "Grips are won before the sweep starts - no grip, no sweep.",
        ],
        "citations": [
            "Gracie R, Gracie R. Brazilian Jiu-Jitsu: Theory and Technique. Invisible Cities Press; 2001 (sweeps from guard).",
            "Kodokan. Kodokan Judo: Throwing Techniques. Kodansha; 2014 (kuzushi principles).",
        ],
        "sig_lens": (
            "The sweep is the Signature's page turned from below: the "
            "guard the hand beneath the sheet, kuzushi the lift, and the "
            "whole argument landing face-up in new order."
        ),
    },
    {
        "key": "side_escape",
        "name": "Escaping Side Control",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Escaping side control - the cross-side pin - is one of the "
            "hardest problems in MMA: the top fighter's weight pins the "
            "torso, the far arm controls the head, and the hips are "
            "flattened. The escapes all share one first move: get onto a "
            "hip. Flat on the back, the bottom fighter is a pinned "
            "specimen; on a hip, they are a fighter with frames and "
            "leverage. The two foundational escapes: the elbow escape "
            "(shrimp away, insert the bottom elbow and then the knee to "
            "recover guard) and the bridge-to-single (bridge into them, "
            "create space, shoot the underhook and come up to a single "
            "leg). Under ground-and-pound the elbow escape is the survival "
            "line - frames first, then hips, then guard."
        ),
        "how_it_works": (
            "The elbow escape: never lie flat - turn into them slightly "
            "and get to the near hip. Frame the near forearm across their "
            "neck or bicep and the far hand on their hip. Bridge slightly "
            "to make a breath of space, then hip escape hard away, "
            "inserting the bottom elbow into the gap, then the bottom "
            "knee, then recovering full guard. The bridge-to-single: "
            "bridge hard into them to unweight their chest, shrimp a few "
            "inches, underhook the near leg deeply, and come up to the "
            "feet driving into a single leg takedown. Against strikes: "
            "the frames go up first - forearms shielding the face - and "
            "the escape is built behind the frames one shrimp at a time. "
            "Drill: partner holds side control at increasing pressure and "
            "throws light strikes; the student frames, hips out, and "
            "recovers guard without ever going flat. The cardinal sin is "
            "pushing with the arms while flat - that burns the arms and "
            "changes nothing."
        ),
        "key_points": [
            "The first move is always onto a hip - flat on the back is the pinned specimen.",
            "Elbow escape: frame, bridge a breath, shrimp away, insert elbow then knee, recover guard.",
            "Bridge-to-single: bridge in, underhook the leg, come up into the takedown.",
            "Under strikes: frames shield the face first, then the escape is built behind them.",
            "Never push with the arms while flat - it burns the arms and changes nothing.",
            "The far hand controls their hip so they cannot follow the shrimp.",
            "Chain the escapes: elbow escape defended becomes the bridge-to-single.",
            "Side control escapes are won in inches - celebrate every inch of hip movement.",
        ],
        "requirements": [
            "A partner who holds realistic, heavy side control.",
            "Light strikes in advanced drilling to simulate ground-and-pound pressure.",
            "Mats; bridging under weight needs a real surface.",
            "The hip escape must be reflexive first - this escape is built on it.",
        ],
        "standards": [
            "The student is never flat for more than a moment - the hip turn is immediate.",
            "Guard is recovered or the single leg is secured against seventy-percent pressure.",
            "Frames are up before any hip movement under strike pressure.",
            "No arm-pushing while flat appears in any rep.",
        ],
        "citations": [
            "Gracie R, Gracie R. Brazilian Jiu-Jitsu: Theory and Technique. Invisible Cities Press; 2001 (side control escapes).",
            "Gracie H. Gracie Jiu-Jitsu Basics instructional series (surviving bad positions).",
        ],
        "sig_lens": (
            "Escaping side control is the Signature's recovery of the "
            "page: pinned flat the text is unreadable, but one hip turn "
            "is the margin found - frames, inches, and the guard redrawn."
        ),
    },
    {
        "key": "triangle",
        "name": "The Triangle Choke",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "The triangle choke is the guard's signature submission: the "
            "legs form a figure-four around the opponent's head and one "
            "arm, and the squeeze compresses the carotids between the "
            "thigh and calf. It is the ultimate guard punishment for the "
            "two classic mistakes - leaving both arms inside the guard, or "
            "posturing with one arm in and the head down. The triangle is "
            "a blood choke, so it works fast once locked, but the setup is "
            "everything: the angle (cutting perpendicular to the "
            "opponent), the lock (figure-four with the ankle behind the "
            "knee), and the finish (pulling the head down while raising "
            "the hips). A stacked triangle is finished by walking the "
            "shoulders back and re-angling, never by muscling through the "
            "stack."
        ),
        "how_it_works": (
            "From the guard, when the opponent leaves one arm inside and "
            "their head low, control the wrist and pull the arm across. "
            "Throw the same-side leg over their shoulder so the back of "
            "the knee sits on their neck, and lock the figure-four: the "
            "thrown leg's ankle hooks behind the other knee, which cuts "
            "across the back of their head. Immediately cut the angle: "
            "scoot the hips perpendicular to them so the choking leg's "
            "thigh presses one side of the neck and the calf presses the "
            "other, with their own shoulder completing the triangle. Pull "
            "the head down with the hands behind the head, raise the hips "
            "slightly, and squeeze the knees together. If they stack: "
            "underhook the leg, walk the shoulders backward on the mat to "
            "re-create the angle, and finish. Drill: partner gives the "
            "arm-in-head-down position lightly; the student throws, locks, "
            "angles, and applies slow pressure to the tap. Never crank - "
            "the triangle is pressure, not force."
        ),
        "key_points": [
            "The triangle punishes the two guard mistakes: both arms in, or one arm in with the head down.",
            "Throw the leg over the shoulder and lock the figure-four: ankle behind the opposite knee.",
            "Cut the angle immediately - perpendicular hips make the choke, square hips break it.",
            "Finish: pull the head down, raise the hips slightly, squeeze the knees together.",
            "Their own trapped shoulder completes the triangle - it is part of the choke.",
            "Against the stack: underhook the leg, walk the shoulders back, re-angle - never muscle it.",
            "The setup is everything: angle, lock, then pressure in that order.",
            "A blood choke works in seconds once locked - respect it like the rear naked choke.",
        ],
        "requirements": [
            "A partner who gives the arm-in position and taps early.",
            "Hip flexibility for the leg throw and the angle cut.",
            "Mats with room to walk the shoulders back against the stack.",
            "The guard must be solid first - the triangle is a guard's weapon.",
        ],
        "standards": [
            "The figure-four is locked before any pressure is applied.",
            "The hips visibly cut perpendicular before the finish.",
            "The partner taps from clean blood-flow pressure with no neck crank.",
            "The stack is answered with the walk-back re-angle, never with muscling.",
        ],
        "citations": [
            "Gracie R, Gracie R. Brazilian Jiu-Jitsu: Theory and Technique. Invisible Cities Press; 2001 (sankaku-jime triangle choke).",
            "Kodokan. Kodokan Judo: Throwing Techniques. Kodansha; 2014 (shime-waza strangle principles).",
        ],
        "sig_lens": (
            "The triangle is the Signature's perfect geometry: three "
            "sides - thigh, calf, and their own shoulder - closing around "
            "the argument until only the conclusion remains."
        ),
    },
    {
        "key": "cage_takedowns",
        "name": "Cage Takedowns and Trips",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Cage takedowns turn the fence into a finishing tool: with the "
            "opponent's back to the wall, the outside trip, the inside "
            "trip, the foot sweep, and the body-lock suplex all become "
            "high-percentage because the retreat is gone. The outside trip "
            "(o-soto): from the clinch, hook the far leg with the near leg "
            "and drive them over it. The inside trip (o-uchi): hook inside "
            "their lead leg and reap it while driving. The foot sweep "
            "(de-ashi): sweep the weighted foot as they step. The "
            "body-lock takedown: lock the hands around the waist, lift or "
            "off-balance, and rotate them down. The cage multiplies all of "
            "them - the opponent cannot step back out of the trip, so the "
            "timing window is generous and the finish rate is high."
        ),
        "how_it_works": (
            "The outside trip: from double underhooks against the fence, "
            "step the near foot to the outside of their far foot, hook "
            "the leg with the calf, and drive the chest through them - "
            "they trip backward over the hooked leg with nowhere to step. "
            "The inside trip: from the clinch, step inside their lead leg "
            "and reap it backward with the calf while pulling their upper "
            "body forward - the leg disappears and the body follows. The "
            "foot sweep: as they step to circle off the fence, sweep the "
            "moving foot sideways with the sole at the exact moment of "
            "weight transfer. The body lock: lock the hands (fingers over "
            "wrist) around the waist, get the hips under theirs, and lift "
            "slightly while rotating - or simply drive and turn the corner "
            "until they fall. Drill each against a partner pinned lightly "
            "on the wall: the student must feel the moment the retreat "
            "dies - that is the trip window. Land in side control every "
            "time; the takedown is only half the technique."
        ),
        "key_points": [
            "The fence kills the retreat: trips that fail in open mat finish against the cage.",
            "Outside trip: hook the far leg from the outside and drive through.",
            "Inside trip: reap the lead leg from the inside while pulling the upper body.",
            "Foot sweep: sweep the moving foot at the exact moment of weight transfer.",
            "Body lock: lock the waist, hips under theirs, lift and rotate.",
            "Feel the trip window: the moment their back foot cannot step back, attack.",
            "Every cage takedown lands in side control - the position is half the technique.",
            "Chain them: outside trip defended becomes the inside trip on the planted leg.",
        ],
        "requirements": [
            "A cage wall or padded wall - these are fence techniques.",
            "A partner who circles realistically along the wall.",
            "Mats; trips land hard.",
            "The clinch must be solid first - trips need the upper-body control.",
        ],
        "standards": [
            "Each trip is demonstrated against a partner actively circling off the wall.",
            "The takedown lands the student in side control, not in a scramble.",
            "The foot sweep is timed to the step - sweeping a planted foot is corrected.",
            "The student chains at least two trips when the first is defended.",
        ],
        "citations": [
            "Kodokan. Kodokan Judo: Throwing Techniques. Kodansha; 2014 (o-soto-gari, o-uchi-gari, de-ashi-harai).",
            "Gracie R, Gracie R. Brazilian Jiu-Jitsu: Theory and Technique. Invisible Cities Press; 2001 (takedowns against the cage).",
        ],
        "sig_lens": (
            "Cage trips are the Signature's final flourish at the "
            "margin: the fence the edge of the page, the trip the foot "
            "swept from under the last word - nowhere left to step but down."
        ),
    },
    {
        "key": "game_plan",
        "name": "Fight Game Planning",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Fight game planning is the integration of everything: a "
            "round-by-round plan that matches the fighter's strengths to "
            "the opponent's weaknesses across striking, wrestling, and "
            "submissions. The plan answers three questions: where does "
            "this fight favor me (the feet, the clinch, the ground), what "
            "is the opponent's path to winning (and how do I take it "
            "away), and what do I do when the plan breaks (the "
            "adjustment). A striker's plan keeps the takedown artist at "
            "the end of the jab and punishes every level change; a "
            "grappler's plan closes distance behind combinations and "
            "chains takedowns to submissions. The plan is written in "
            "training camp, drilled until it is reflex, and adjusted "
            "between rounds - because no plan survives first contact "
            "unchanged, but the fighter with a plan adjusts while the "
            "fighter without one improvises."
        ),
        "how_it_works": (
            "Study the opponent: three of their fights minimum, noting "
            "where they win (knockouts standing, submissions on the "
            "ground), how they react to pressure, and what breaks them "
            "(leg kicks, body shots, the clinch). Write the A-plan in "
            "three lines: my winning position, their denied weapon, my "
            "round-one script (the first ninety seconds, scripted "
            "technique by technique). Drill the script: the exact "
            "combinations, the exact takedown entries, the exact guard "
            "passes - hundreds of reps until they fire without thought. "
            "Write the B-plan: if they take me down, the guard game; if "
            "they outstrike me, the clinch and the fence. Between rounds, "
            "the corner reports one adjustment only - the single most "
            "important change - because three adjustments are none. "
            "Sparring application: designate rounds as A-plan rounds "
            "(execute the script regardless) and chaos rounds (opponent "
            "does anything, practice the B-plan). The plan is a living "
            "document: after every sparring session, one line is rewritten."
        ),
        "key_points": [
            "The plan answers: where do I win, what is their path (denied), what is my adjustment.",
            "Study three of their fights minimum: find where they win and what breaks them.",
            "Script the first ninety seconds technique by technique - openings decide rounds.",
            "Drill the script to reflex: combinations, entries, and passes on autopilot.",
            "The B-plan covers the plan breaking: the guard game, the clinch, the fence.",
            "Between rounds: one adjustment only - the single most important change.",
            "Spar A-plan rounds (execute the script) and chaos rounds (practice the B-plan).",
            "Rewrite one line of the plan after every sparring session - it is a living document.",
        ],
        "requirements": [
            "Video of the opponent's past fights (or a style archetype to plan against).",
            "A coach to help write and adjust the plan.",
            "A training camp structure: technique, drilling, sparring, conditioning.",
            "A notebook: the plan is written down, not kept in the head.",
        ],
        "standards": [
            "The written plan exists: A-plan, B-plan, and the ninety-second script.",
            "The script's techniques are drilled to reflex before sparring application.",
            "Between-round adjustments are limited to one clear instruction.",
            "The plan is updated after every sparring session with at least one rewritten line.",
        ],
        "citations": [
            "Sheridan S. The Fighter's Mind: Inside the Mental Game. Grove Press; 2010 (fight preparation and game planning).",
            "Association of Boxing Commissions. Unified Rules of Mixed Martial Arts (round structure and scoring).",
        ],
        "sig_lens": (
            "The game plan is the Signature's complete manuscript: every "
            "technique a chapter, the ladder its table of contents, the "
            "adjustment the author's hand still on the pen when the "
            "story changes."
        ),
    },
]
