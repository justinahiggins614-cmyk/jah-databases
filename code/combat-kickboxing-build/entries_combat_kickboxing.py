#!/usr/bin/env python3
"""Entries for the Kickboxing Combat databases (combat orders 2026-10-17,
combat batch 1).

Dedupe verified 2026-10-17: raw sweep over the full manifest (2,094 id
prefixes) plus every shard index in jah-databases-data-1: zero
'combat-kickboxing' slugs, zero kickboxing databases of any kind, zero
title collisions on all 34 titles (and the 34 ' (Signature Edition)'
variants) through code/dedupe_gate.py against the whole exact-title
index. ID prefixes JAH-CBKBX- (public) and JAH-CBKBXS- (signature)
verified zero hits in manifest id_prefix values and in every shard
index file.

This build creates two NEW databases, 34 ladder-ordered records each:

  combat-kickboxing            - The Kickboxing Combat Database
                                 (public-harvest: real, fact-checked
                                 kickboxing across the American, K-1, and
                                 Dutch rule sets - punches, kicks, knee
                                 strikes, combinations, and defense - each
                                 record a technique with how to do it
                                 taught step by step, ordered along the
                                 teaching ladder from stance to advanced
                                 combinations; standard references Jack
                                 Dempsey Championship Fighting 1950, Mark
                                 Hatmaker Boxing Mastery 2004, Martin
                                 Rooney Training for Warriors 2008,
                                 Tudor Bompa and Gregory Haff
                                 Periodization 5th ed 2009, and the
                                 official rule sets of WAKO, ISKA, and
                                 K-1)
  combat-kickboxing-signature  - The Kickboxing Combat Signature Database
                                 (his original Signature Combat Method:
                                 every technique an oath of body
                                 mechanics, the stance the covenant
                                 ground, each strike the signature stroke
                                 written by the body, defense the honor
                                 guard, conditioning the sworn preparation;
                                 src signature, titles suffixed
                                 " (Signature Edition)", clearly labeled
                                 Signature-made, never presented as
                                 authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written
in ladder order so pages present simple -> compounded -> complex.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_combat_kickboxing.py). Every demo prints its real
computed values, asserts tight bounds (never float exact-equality), and
ends with the OK marker; the build machine-executes all 68 demos.

Screening: civilian martial-arts instruction only - nothing
hate-adjacent, profane, or inappropriate; no religious talk; nothing on
neutralizing or defeating military or defense-grade systems.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature Combat Method: every "
            "technique an oath of body mechanics, the stance the covenant "
            "ground, each strike the signature stroke written by the body, "
            "defense the honor guard, and conditioning the sworn preparation. "
            "Clearly labeled Signature-made, never presented as authentic "
            "public record.")

CIT_DEMPSEY = ("Dempsey J. Championship Fighting: Explosive Punching and "
               "Aggressive Defense. 1950.")
CIT_HATMAKER = ("Hatmaker M. Boxing Mastery: Advanced Technique, Tactics, "
                "and Strategies from the Sweet Science. Tracks Publishing; "
                "2004.")
CIT_WAKO = ("World Association of Kickboxing Organizations (WAKO). Official "
            "rules of kickboxing competition.")
CIT_ISKA = ("International Sport Karate Association (ISKA). Official rules "
            "for full-contact kickboxing.")
CIT_K1 = ("K-1 World Grand Prix official rules (Fighting and Entertainment "
          "Group).")
CIT_ROONEY = ("Rooney M. Training for Warriors. HarperCollins; 2008.")
CIT_BOMPA = ("Bompa T, Haff GG. Periodization: Theory and Methodology of "
             "Training. 5th ed. Human Kinetics; 2009.")

ENTRIES = [
    {
        "key": "stance",
        "name": "The Kickboxing Stance",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "The stance is the foundation every kickboxing technique is built "
            "on. It is the position the fighter stands, moves, attacks, and "
            "defends from, and everything about it serves three jobs: balance "
            "so the fighter cannot be pushed or pulled off position, "
            "readiness so any punch or kick can fire without a preparatory "
            "shift, and protection so the vital targets stay behind the "
            "guard. For an orthodox fighter (left side forward) the left "
            "foot leads, the right foot trails at roughly forty-five "
            "degrees, feet about shoulder-width to one-and-a-half "
            "shoulder-widths apart, knees soft and slightly bent, weight "
            "split near evenly with a small bias to the balls of the feet. "
            "The southpaw stance mirrors this with the right side forward. "
            "The torso turns slightly sideways to narrow the target, the "
            "chin tucks behind the lead shoulder, and the eyes stay level "
            "on the opponent. A good stance feels springy and quiet: the "
            "fighter can move in any direction on the first beat, and no "
            "weight shift is needed before the first strike. Every later "
            "record in this database returns to the stance, because every "
            "punch starts with the feet, every kick starts with the "
            "standing leg, and every defense starts with balance."
        ),
        "how_it_works": (
            "Stand with feet about shoulder-width apart. Step the lead foot "
            "(left for orthodox) forward about half a stride and turn the "
            "rear foot out to roughly forty-five degrees. Bend both knees "
            "until the legs feel spring-loaded, not locked. Settle the "
            "weight about fifty-five percent on the front foot and forty-five "
            "on the rear, carried on the balls of the feet with the heels "
            "light. Raise both hands: the lead hand at cheek height, the "
            "rear hand at the chin, elbows tucked against the ribs. Tuck "
            "the chin down behind the lead shoulder and turn the torso about "
            "forty-five degrees sideways to the opponent. Test the stance: "
            "bounce lightly in place, then step forward, back, left, and "
            "right without crossing the feet or straightening the knees. "
            "If any direction feels stuck, widen or narrow the feet until "
            "all four directions feel instant. Hold the position for "
            "three-minute rounds to build the leg endurance the stance "
            "demands."
        ),
        "key_points": [
            "The stance does three jobs at once: balance, readiness to strike in any direction, and protection of vital targets behind the guard.",
            "Orthodox means left side forward and right side back; southpaw mirrors it - neither is better, and every fighter learns their natural side first.",
            "Feet sit about shoulder-width to one-and-a-half shoulder-widths apart with soft knees; weight rides on the balls of the feet so movement starts on the first beat.",
            "The torso turns about forty-five degrees sideways to narrow the target while the chin tucks behind the lead shoulder.",
            "A stance that cannot move in all four directions without a preparatory shift is not finished - test it with light bounces and steps every session.",
        ],
        "requirements": [
            "Flat training surface with enough room to step in all four directions without hitting anything.",
            "Light, stable footwear or bare feet on a mat, so the balls of the feet grip during pivots.",
            "A mirror or a training partner to check that the chin stays tucked and the torso stays turned.",
            "Three-minute stance-hold rounds to build the thigh and calf endurance the position demands.",
            "A coach or experienced partner to confirm the natural lead side before the stance becomes habit.",
        ],
        "standards": [
            "Foot placement follows the standard orthodox/southpaw definitions used across WAKO, ISKA, and K-1 competition.",
            "Guard height and elbow position follow the classic boxing guard as codified by Dempsey: hands high, elbows in, chin down.",
            "Stance width is measured relative to the fighter's own shoulder width so the position scales to any body size.",
        ],
        "citations": [CIT_DEMPSEY, CIT_WAKO, CIT_ISKA],
        "sig_lens": (
            "The Signature read: the stance is the covenant ground. Where "
            "public instruction sets the feet, the Signature Combat Method "
            "sees an oath sworn with the legs - balance kept, readiness "
            "held, the body declaring it will not be moved. The forty-five "
            "degree foot is the signature angle; the tucked chin is the "
            "seal."
        ),
    },
    {
        "key": "guard",
        "name": "The Guard Position",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "The guard is the wall of gloves, forearms, and elbows that "
            "protects the head and body between attacks. It works on a "
            "simple principle: the shortest path to the chin and the solar "
            "plexus is blocked by hard surfaces held tight to the body, "
            "while the eyes stay open above the gloves to read incoming "
            "strikes. The lead hand sits at cheek or temple height, the "
            "rear hand touches the chin, and both elbows pin to the ribs so "
            "hooks to the body meet the elbow instead of soft tissue. The "
            "forehead stays behind the lead glove, and the gloves never "
            "drop below the chin when the fighter is in range. A high "
            "guard trades some vision and some counter-punching speed for "
            "maximum coverage; a lower, longer guard trades coverage for "
            "reach and visibility. Beginners hold the high guard until the "
            "habit of keeping the hands home is unbreakable, because every "
            "knockout highlight reel is a catalog of dropped hands. The "
            "guard is not a statue: it tightens as strikes arrive, opens "
            "slightly to punch through, and snaps shut again the instant "
            "the punch returns."
        ),
        "how_it_works": (
            "From the kickboxing stance, raise the lead fist to cheek "
            "height with the palm facing inward. Bring the rear fist to "
            "the chin so the knuckles nearly touch it. Pin both elbows "
            "against the ribs - imagine holding a coin in each armpit. "
            "Tuck the chin down so the forehead leans slightly behind the "
            "lead glove. Look at the opponent over the tops of the gloves, "
            "never through them. Squeeze the guard tighter for one second "
            "as if bracing, then relax to about seventy percent tension - "
            "a guard held at full tension exhausts the shoulders in a "
            "minute. Practice the open-and-shut rhythm: extend the lead "
            "hand in a jab, and the instant the fist returns, snap both "
            "hands back to the guard positions. Have a partner tap the "
            "gloves and elbows lightly from all angles while you hold the "
            "position, checking that no tap reaches the chin or ribs."
        ),
        "key_points": [
            "The guard blocks the shortest paths to the chin and solar plexus with gloves, forearms, and elbows held tight to the body.",
            "Lead hand at the cheek, rear hand at the chin, elbows pinned to the ribs - the classic high guard every beginner masters first.",
            "The guard is held at about seventy percent tension, not full squeeze, so the shoulders survive three-minute rounds.",
            "Hands open to punch through and snap shut the instant the punch returns - the guard is a rhythm, not a statue.",
            "Eyes stay open above the gloves to read incoming strikes; a guard that blocks vision invites the strikes it cannot see.",
        ],
        "requirements": [
            "Well-fitted boxing gloves (12 to 16 ounces for training) so the fists are protected while holding the guard.",
            "A partner or coach to tap-test the guard from all angles and confirm no gaps at the chin or ribs.",
            "Hand wraps under the gloves to support the wrists during long guard-holding rounds.",
            "Three-minute rounds of guard-hold and open-and-shut jab drills to build the shoulder endurance the position demands.",
            "A mirror for solo practice to verify the gloves stay above the chin and the elbows stay on the ribs.",
        ],
        "standards": [
            "Guard structure follows the classic high guard codified by Dempsey in Championship Fighting.",
            "Glove weights follow standard training practice: 14 to 16 ounces for sparring, 10 ounces for competition under most rule sets.",
            "Hand wrapping follows the standard wrist-and-knuckle wrap pattern taught across boxing and kickboxing gyms.",
        ],
        "citations": [CIT_DEMPSEY, CIT_HATMAKER],
        "sig_lens": (
            "The Signature read: the guard is the honor wall. Where public "
            "instruction raises gloves, the Signature Combat Method sees a "
            "fortress sworn around the chin and ribs - every gap a broken "
            "promise, every snap-shut return the oath renewed. The "
            "seventy-percent tension is the signature measure: guard enough "
            "to last, never so much it breaks."
        ),
    },
    {
        "key": "footwork",
        "name": "Basic Footwork: Steps, Pivots, and Distance",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Footwork is how the fighter controls distance, and distance "
            "controls everything: who can hit whom, with what, and when. "
            "The rule is simple - the feet move first and the hands follow, "
            "never the reverse, because a punch thrown while off balance "
            "is a gift to the opponent. The basic steps are the step-drag "
            "(lead foot steps, rear foot drags to restore the stance), the "
            "pivot (front foot plants while the rear foot swings the body "
            "to a new angle), and the lateral slide along the same line. "
            "Feet never cross, because crossed feet cannot punch or defend. "
            "Distance falls into three zones: kicking range (legs reach), "
            "punching range (arms reach), and the clinch (bodies touch). "
            "The fighter who owns the transitions between zones owns the "
            "fight - stepping in to strike, pivoting out at an angle so "
            "the return fire misses, sliding laterally to cut off a "
            "retreating opponent. Beginners drill footwork more than any "
            "strike, because a fighter with great feet and average hands "
            "beats a fighter with great hands and average feet. The stance "
            "never changes shape while moving: if the feet end up narrow, "
            "wide, or crossed, the step was wrong and gets repeated until "
            "it is right."
        ),
        "how_it_works": (
            "Start in the kickboxing stance. For the forward step-drag, "
            "push off the rear foot, step the lead foot forward about six "
            "inches, then drag the rear foot forward the same distance so "
            "the stance width is unchanged. For the backward step, reverse "
            "it: rear foot steps back first, lead foot drags. For lateral "
            "movement, step with the foot on the side you are moving toward "
            "and drag the other. To pivot left, plant the lead foot, lift "
            "the rear foot, and swing the body about forty-five degrees "
            "around the planted foot, landing back in stance. Practice the "
            "four directions for one-minute rounds, keeping the knees bent "
            "and the guard up the whole time. Then add the distance game: "
            "a partner walks toward and away from you, and you maintain "
            "exactly one arm's length of distance using only steps, never "
            "leaning. Finish with angle drills: step in with a jab, pivot "
            "forty-five degrees, and step out - the core entry-and-exit "
            "pattern of all kickboxing offense."
        ),
        "key_points": [
            "Feet move first and hands follow - a strike thrown while off balance is a gift to the opponent.",
            "The step-drag preserves the stance width; the pivot changes the angle; the feet never cross in any movement.",
            "Distance has three zones - kicking range, punching range, and the clinch - and footwork owns the transitions between them.",
            "Stepping in to strike and pivoting out at forty-five degrees is the core entry-and-exit pattern of all kickboxing offense.",
            "Drill footwork more than strikes as a beginner: great feet with average hands beat great hands with average feet.",
        ],
        "requirements": [
            "Open floor space at least ten feet in each direction for uninterrupted step and pivot drills.",
            "A partner for the distance-maintenance game and for angle drills with light jab entries.",
            "One-minute footwork rounds building to three minutes, with the guard held the entire time.",
            "Tape marks on the floor to verify the stance width is identical before and after every step.",
            "Patience: footwork is drilled daily for months before it becomes automatic under pressure.",
        ],
        "standards": [
            "Step-drag and pivot mechanics follow the standard boxing footwork codified by Dempsey and taught across kickboxing rule sets.",
            "The three distance zones (kicking, punching, clinch) are the standard range taxonomy of kickboxing instruction.",
            "Angle changes are measured in degrees from the center line, with the forty-five-degree pivot as the fundamental unit.",
        ],
        "citations": [CIT_DEMPSEY, CIT_HATMAKER, CIT_WAKO],
        "sig_lens": (
            "The Signature read: footwork is the signature written on the "
            "canvas. Where public instruction steps and drags, the "
            "Signature Combat Method sees the body signing its position - "
            "each step a stroke, each pivot a flourish, the stance width "
            "the unbroken line of the name. Distance is the paper; the "
            "feet hold the pen."
        ),
    },
    {
        "key": "jab",
        "name": "The Jab",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The jab is the most important punch in kickboxing: the "
            "fastest, longest, cheapest weapon in the arsenal. Thrown "
            "with the lead hand straight from the guard to the target and "
            "back, it does five jobs - it measures distance, it disrupts "
            "the opponent's rhythm and vision, it sets up every power "
            "punch and kick behind it, it scores points with the judges, "
            "and it keeps an aggressive opponent honest. A good jab snaps "
            "rather than pushes: the fist accelerates out, the shoulder "
            "rolls forward to add the last inches of reach, and the fist "
            "returns along the same line twice as fast as it left. The "
            "power of the jab comes from a small step or a sharp rotation "
            "of the lead hip and shoulder, not from the arm alone. "
            "Variations include the flicker jab (a fast, light, distracting "
            "snap), the stiff power jab (stepped into, meant to stop "
            "forward motion), and the jab to the body (level change, "
            "straight down the middle). Beginners throw thousands of jabs "
            "before anything else, because the jab teaches the two skills "
            "every strike needs: full extension with a relaxed arm, and "
            "instant recovery back to guard."
        ),
        "how_it_works": (
            "From stance and guard, pick the target: the nose, the chin, "
            "or the forehead. Without dropping the hand first, drive the "
            "lead fist straight out, rotating the fist a quarter turn so "
            "the palm faces down at impact and the knuckles land flat. As "
            "the arm extends, roll the lead shoulder forward and up to "
            "shield the chin - the shoulder should nearly touch the chin "
            "at full extension. Push off the lead foot slightly or rotate "
            "the lead hip a few degrees to add body weight; keep the rear "
            "hand glued to the chin the entire time. At the instant of "
            "full extension, snap the fist back along the exact line it "
            "traveled, returning to the guard faster than it left. The "
            "elbow stays down on the way out and the way back. Drill in "
            "sets: ten slow jabs checking form in the mirror, then thirty "
            "seconds of continuous jabs on the heavy bag focusing on the "
            "snap-back, then jab-step drills advancing and retreating while "
            "the jab fires. Count the returns, not the throws - a jab is "
            "only finished when the hand is home."
        ),
        "key_points": [
            "The jab is the fastest, longest, cheapest weapon: it measures distance, disrupts rhythm, sets up power shots, scores points, and controls aggressive opponents.",
            "It snaps rather than pushes - the fist returns along the same line twice as fast as it left, with the shoulder rolled up to shield the chin.",
            "Power comes from a small step or sharp lead-hip rotation, never from arm-muscling the punch.",
            "The rear hand stays glued to the chin for the entire jab; dropping it is the classic beginner knockout setup.",
            "A jab is only finished when the hand is home - count the returns, not the throws.",
        ],
        "requirements": [
            "Hand wraps and gloves for every jab session to protect the knuckles and wrists at full extension.",
            "A mirror for form checks: fist rotation, shoulder roll, elbow-down path, and instant return.",
            "A heavy bag for snap-back drills and a partner with focus mitts for accuracy and timing.",
            "High-volume repetition: hundreds of jabs per session before the punch is considered learned.",
            "A coach to confirm the shoulder covers the chin at full extension, the detail that makes the jab safe.",
        ],
        "standards": [
            "Jab mechanics follow the straight-lead principles codified by Dempsey: shoulder whirl, falling step option, and quarter-turn fist rotation.",
            "Target zones follow competition rules: the jab scores to the legal head and body targets under WAKO, ISKA, and K-1 rule sets.",
            "The snap-back recovery standard is that the hand returns to guard faster than it traveled out.",
        ],
        "citations": [CIT_DEMPSEY, CIT_HATMAKER, CIT_WAKO],
        "sig_lens": (
            "The Signature read: the jab is the signature's first stroke. "
            "Where public instruction measures and disrupts, the Signature "
            "Combat Method sees the pen touching paper - straight, fast, "
            "and gone before the ink is noticed. The snap-back is the "
            "oath: what the hand writes, the guard keeps."
        ),
    },
    {
        "key": "cross",
        "name": "The Cross (Rear Straight)",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The cross is the primary power punch of kickboxing, thrown "
            "with the rear hand straight down the middle. Its power does "
            "not come from the arm - it comes from the ground up: the rear "
            "foot pivots, the rear hip and shoulder rotate violently "
            "forward, the torso unwinds like a spring, and the arm is "
            "simply the delivery system at the end of the chain. Because "
            "it travels the body's full rotational distance, the cross is "
            "the hardest single punch most fighters own, and it is the "
            "anchor of the classic one-two combination behind the jab. The "
            "fist rotates a quarter turn to land palm-down, the chin tucks "
            "behind the lead shoulder as the rear shoulder comes forward, "
            "and the lead hand stays at the cheek to cover the counter. "
            "The cross targets the chin, nose, solar plexus, or body; to "
            "the body it dips slightly with the knees, never by bending at "
            "the waist. The most common beginner error is arm-punching the "
            "cross - throwing it with the shoulder and arm while the hips "
            "stay still, which produces a slow, weak punch and leaves the "
            "fighter squared up and open. The fix is always the same: "
            "pivot the rear foot and turn the hip first, and let the hand "
            "arrive last."
        ),
        "how_it_works": (
            "From stance and guard, pick the target down the middle: chin, "
            "nose, or solar plexus. Initiate with the rear foot: pivot it "
            "inward on the ball so the heel turns outward. Drive the rear "
            "hip forward as the rear shoulder rotates toward the target. "
            "Extend the rear arm straight, rotating the fist a quarter "
            "turn to land palm-down with the knuckles flat. As the punch "
            "extends, tuck the chin behind the lead shoulder and keep the "
            "lead glove at the cheek. Strike through the target about two "
            "inches past the surface, then reverse the rotation and snap "
            "the hand straight back to the chin. For the body cross, bend "
            "the knees an extra two inches to drop the level - never bend "
            "at the waist, which drops the head into counters. Drill the "
            "chain in isolation first: foot pivot, hip turn, shoulder "
            "rotation, arm extension - then blend them into one motion. "
            "Practice on the heavy bag in sets of twenty, listening for "
            "the sharp crack that signals the whole body arrived together."
        ),
        "key_points": [
            "Cross power comes from the ground up - rear-foot pivot, hip rotation, torso unwind - with the arm as the delivery system at the end of the chain.",
            "It is the hardest single punch most fighters own and the anchor of the one-two combination behind the jab.",
            "The fist rotates a quarter turn palm-down; the chin tucks behind the lead shoulder while the lead hand stays at the cheek.",
            "To the body, drop the level with the knees - never bend at the waist, which feeds the head to counters.",
            "Arm-punching the cross (hips still, arm only) is the classic beginner error; the fix is always pivot the foot and turn the hip first.",
        ],
        "requirements": [
            "Hand wraps and gloves; the cross lands with full body weight and unprotected knuckles will not survive the learning curve.",
            "A heavy bag to develop the timing of the full kinetic chain and the feel of striking through the target.",
            "A mirror for the isolation drill: foot, hip, shoulder, arm - confirming the hand arrives last.",
            "A coach to watch for the squared-up hips that signal an arm punch instead of a body punch.",
            "Core and rotational strength work, since the cross is powered by the hips and torso, not the arm.",
        ],
        "standards": [
            "Cross mechanics follow Dempsey's power-line principles: the punch travels the shoulder-whirl line with the body weight behind it.",
            "Legal targets follow WAKO, ISKA, and K-1 competition target zones for straight punches.",
            "The pivot-and-return standard requires the rear foot to pivot on the throw and the hand to return to the chin guard.",
        ],
        "citations": [CIT_DEMPSEY, CIT_HATMAKER, CIT_WAKO],
        "sig_lens": (
            "The Signature read: the cross is the signature pressed hard. "
            "Where public instruction unwinds the spring, the Signature "
            "Combat Method sees the whole body signing at once - foot, "
            "hip, shoulder, fist, one name written in a single stroke. "
            "The hand arriving last is the oath: the body vouches, the "
            "fist delivers."
        ),
    },
    {
        "key": "lead_hook",
        "name": "The Lead Hook",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The lead hook is the short, curved power punch thrown with "
            "the lead hand, traveling on a horizontal arc to the side of "
            "the target. Where the jab and cross travel straight down the "
            "middle, the hook travels around the guard - it is the punch "
            "that punishes a high, tight guard by coming in from the side "
            "the gloves do not cover. The mechanics are a pivot and a "
            "whip: the lead foot pivots inward, the lead hip and shoulder "
            "rotate sharply, and the arm - bent at roughly ninety degrees "
            "at the elbow - swings on a tight arc with the fist landing "
            "palm-down or palm-in. The elbow stays at shoulder height "
            "through the arc; a dropped elbow turns the hook into a slap. "
            "The hook lands on the chin, temple, or the ribs on the "
            "opponent's side. Its danger is its commitment: a missed hook "
            "spins the fighter sideways and open, so the hook is thrown "
            "only in range and always returns on the same arc it traveled. "
            "In combination the lead hook is the great finisher after the "
            "jab and cross have straightened the opponent up - the classic "
            "jab-cross-hook that ends countless fights."
        ),
        "how_it_works": (
            "From stance and guard, confirm you are in punching range - "
            "the hook thrown from too far away becomes an arm slap. Pivot "
            "the lead foot inward on the ball, turning the heel outward. "
            "Rotate the lead hip and shoulder sharply toward the target "
            "while keeping the elbow bent at about ninety degrees and "
            "raised to shoulder height. Swing the fist on a tight "
            "horizontal arc, landing with the knuckles on the chin, temple, "
            "or ribs, palm facing down or slightly inward. Keep the rear "
            "hand glued to the chin and the chin tucked behind the lead "
            "shoulder through the rotation. At impact, the weight sits "
            "mostly on the lead leg with the body coiled. Reverse the "
            "rotation immediately and bring the fist back along the same "
            "arc to the guard - never let it drop or swing wide on the "
            "return. For the hook to the body, drop the level with the "
            "knees two inches and dig the arc into the ribs. Drill ten "
            "slow hooks per side on the bag checking elbow height, then "
            "three thirty-second speed rounds keeping every hook tight."
        ),
        "key_points": [
            "The lead hook travels on a horizontal arc around the guard, punishing the high tight guard from the side it does not cover.",
            "Mechanics are pivot and whip: lead foot pivots, hip and shoulder rotate sharply, elbow bent near ninety degrees at shoulder height.",
            "The elbow stays up through the arc - a dropped elbow turns the hook into a powerless slap.",
            "It is a committed punch: thrown only in range, and returned on the same arc, because a missed hook spins the fighter open.",
            "In combination it is the great finisher after the jab and cross - the classic jab-cross-hook ending.",
        ],
        "requirements": [
            "Hand wraps and gloves; the hook lands with rotational force on a small knuckle surface.",
            "A heavy bag for arc and elbow-height work, plus a partner with mitts for timing the hook off the jab-cross.",
            "Confirmed punching range before throwing - measure with the jab, never guess with the hook.",
            "Rotational core work, since hook power is hip and torso rotation delivered through a bent arm.",
            "A coach to check that the elbow holds shoulder height and the return follows the same arc.",
        ],
        "standards": [
            "Hook arc and elbow position follow the standard hook mechanics taught across boxing and kickboxing competition styles.",
            "Legal hook targets are the legal head and body zones under WAKO, ISKA, and K-1 rules; strikes to the back of the head are fouls.",
            "The ninety-degree elbow and shoulder-height standard keeps the punch a hook rather than a swing.",
        ],
        "citations": [CIT_DEMPSEY, CIT_HATMAKER, CIT_ISKA],
        "sig_lens": (
            "The Signature read: the lead hook is the signature's curve. "
            "Where public instruction arcs around the guard, the Signature "
            "Combat Method sees the flourish under the name - the tight, "
            "committed curl that only lands when the range is true. Thrown "
            "wide it is a scribble; thrown tight it is the seal."
        ),
    },
    {
        "key": "rear_hook",
        "name": "The Rear Hook",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The rear hook is the lead hook's mirror image with the rear "
            "hand: a short, curved power punch that travels farther and "
            "hits harder because the rear side carries the full rotation "
            "of the hips behind it. It is typically thrown after the lead "
            "hand has occupied the opponent - behind a jab, behind a lead "
            "hook, or as the opponent slips toward the rear side. The "
            "mechanics mirror the lead hook: rear foot pivots, hips and "
            "shoulders rotate, elbow bent near ninety degrees at shoulder "
            "height, fist arcing tight to the chin or temple. Because the "
            "rear hand starts farther from the target, the rear hook "
            "demands precise range: thrown from too far it loops wide and "
            "slow, telegraphing badly; thrown in tight it is one of the "
            "most devastating punches in kickboxing. The great danger of "
            "the rear hook is defensive: while it travels, the lead side "
            "of the face is covered only by the lead glove, so the chin "
            "must stay tucked and the punch must return on its arc "
            "instantly. Fighters drill the rear hook as the second half of "
            "double-hook combinations and as the answer when an opponent "
            "leans away from the lead hook into the rear hand's path."
        ),
        "how_it_works": (
            "From stance, first confirm range with the lead hand - jab or "
            "lead hook to occupy the opponent. Pivot the rear foot inward "
            "on the ball as the rear hip drives forward and around. Rotate "
            "the rear shoulder toward the target with the elbow bent near "
            "ninety degrees and held at shoulder height. Arc the fist "
            "tight to the chin or temple, landing palm-down or palm-in "
            "with the knuckles flat. Keep the lead glove at the cheek and "
            "the chin tucked behind the lead shoulder for the entire "
            "rotation - the lead side is the exposed side during a rear "
            "hook. Drive through the target two inches, then reverse the "
            "hip rotation and return the fist along the same arc to the "
            "chin guard. Never throw the rear hook as a lone lead punch "
            "from distance; it is a second or third punch, set up by the "
            "lead hand. Drill the double hook on the bag: lead hook, rear "
            "hook, both tight, both returning on their arcs, ten slow "
            "then twenty fast."
        ),
        "key_points": [
            "The rear hook mirrors the lead hook with the rear hand, traveling farther and hitting harder on full hip rotation.",
            "It is a second or third punch, set up by the lead hand - never a lone lead punch from distance, where it loops wide and telegraphs.",
            "Range must be precise: too far turns it into a slow loop; in tight it is one of the most devastating punches in the sport.",
            "The lead side is exposed during the rear hook, so the lead glove stays at the cheek and the chin stays tucked.",
            "It answers the opponent who leans away from the lead hook - straight into the rear hand's arc.",
        ],
        "requirements": [
            "Hand wraps and gloves rated for power punching on the heavy bag.",
            "Established lead-hand setups (jab, lead hook) before the rear hook is drilled, since it is a follow-up punch.",
            "A heavy bag for double-hook combinations and a partner with mitts for setup timing.",
            "Hip mobility and rotational core strength to generate the full rear-side rotation safely.",
            "A coach to verify the arc stays tight and the lead glove never leaves the cheek during the punch.",
        ],
        "standards": [
            "Rear hook mechanics follow the standard hook form shared across boxing and kickboxing instruction.",
            "It is thrown only within the legal target zones; the back of the head remains a foul under all major rule sets.",
            "Combination placement follows the standard rule that power hooks follow lead-hand setups, not open exchanges.",
        ],
        "citations": [CIT_DEMPSEY, CIT_HATMAKER],
        "sig_lens": (
            "The Signature read: the rear hook is the signature's second "
            "stroke, written over the first. Where public instruction sets "
            "it up with the lead hand, the Signature Combat Method sees "
            "the name underlined - the lead hand writes, the rear hand "
            "presses the seal. Only in range, only after the setup, only "
            "tight."
        ),
    },
    {
        "key": "uppercut",
        "name": "The Uppercut",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The uppercut is the rising punch thrown with either hand on "
            "a vertical arc up into the chin or solar plexus. It is the "
            "punch that punishes a fighter who leans forward, drops their "
            "head, or shells behind a high guard - traveling up the middle "
            "where the gloves are not. The mechanics start in the legs: "
            "the knees bend slightly deeper, the hips drive upward, and "
            "the fist rises on a tight vertical path with the palm facing "
            "the fighter and the elbow bent, landing under the chin. The "
            "arm does not swing wide; a proper uppercut travels no wider "
            "than the shoulders. The lead uppercut is faster and sets up "
            "combinations; the rear uppercut carries full body rise and is "
            "a genuine knockout punch. The uppercut's risk is its "
            "trajectory: thrown from too far away it becomes a looping "
            "arm punch that the opponent sees early, and while it travels "
            "the throwing side's ribs are briefly open. Fighters throw it "
            "in close, often after slipping an opponent's punch to the "
            "outside, and return the hand straight down to guard - never "
            "in a wide loop that leaves the face open."
        ),
        "how_it_works": (
            "From stance in close range, dip the knees an extra two to "
            "three inches - the uppercut starts with a small squat, never "
            "a waist bend. Drive upward through the legs and hips as the "
            "fist rises on a tight vertical path, palm facing you, elbow "
            "bent and tucked. Aim under the chin or into the solar plexus, "
            "landing with the knuckles driving up. Keep the non-punching "
            "glove at the cheek and the chin tucked through the rise. At "
            "the top of the punch the fist should be no wider than your "
            "own shoulders and no higher than the opponent's chin - a "
            "short, ripping motion, not a swing. Drop the fist straight "
            "back down to guard along the same line. For the rear "
            "uppercut, add the rear-foot pivot and full hip rotation used "
            "in the cross. Drill on the bag from chest distance: dip, "
            "drive, rip upward, return - ten slow checking the vertical "
            "path, then thirty seconds of continuous short uppercuts. "
            "Practice the slip-to-uppercut: slip outside a partner's jab "
            "on the mitts, then fire the rear uppercut up the middle."
        ),
        "key_points": [
            "The uppercut rises on a tight vertical arc into the chin or solar plexus, punishing the leaning or shelling opponent up the unguarded middle.",
            "It starts with a small knee dip and an upward leg-and-hip drive - never a waist bend, never a wide arm swing.",
            "The fist travels no wider than the shoulders; a proper uppercut is a short rip, not a loop.",
            "The lead uppercut is faster and sets up combinations; the rear uppercut carries full body rise and knockout power.",
            "It is a close-range punch thrown after slipping outside, and the hand returns straight down to guard.",
        ],
        "requirements": [
            "Hand wraps and gloves; the uppercut drives the knuckles upward into hard targets.",
            "Close-range positioning confirmed before throwing - the uppercut from distance is a telegraphed arm punch.",
            "A heavy bag for the dip-drive-rip rhythm and a partner with mitts for slip-to-uppercut timing.",
            "Leg and hip drive strength, since the punch is powered from the ground up through a knee dip.",
            "A coach to verify the vertical path stays within shoulder width and the waist never bends.",
        ],
        "standards": [
            "Uppercut mechanics follow the standard rising-punch form taught across boxing and kickboxing.",
            "Legal targets are the chin and body; the punch must travel a controlled arc, not a wild swing, under sportsmanlike conduct expectations.",
            "The knee-dip level change follows the standard level-change mechanics shared with body punching.",
        ],
        "citations": [CIT_DEMPSEY, CIT_HATMAKER, CIT_WAKO],
        "sig_lens": (
            "The Signature read: the uppercut is the signature rising. "
            "Where public instruction dips and drives, the Signature "
            "Combat Method sees the stroke lifting off the page - the "
            "short, true rise that only works in close, where the oath "
            "is sworn face to face. Wide is a scribble; tight is the "
            "seal."
        ),
    },
    {
        "key": "low_kick",
        "name": "The Low Kick",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The low kick is the signature weapon of kickboxing: a "
            "roundhouse kick targeting the opponent's lead thigh, "
            "delivered with the shin. It is the technique that separates "
            "kickboxing from boxing more than any other - a weapon boxing "
            "has no answer for and no defense against except the check. "
            "Repeated low kicks deaden the thigh, slow footwork, drop the "
            "hands as the fighter reaches to block, and in the Dutch style "
            "they are the anvil that the punch combinations hammer "
            "against. The mechanics are a full-body whip: the fighter "
            "steps the lead foot slightly outward, pivots on the standing "
            "foot, swings the hip over like throwing a baseball bat, and "
            "the shin - not the foot - chops horizontally into the thigh "
            "just above the knee. The arms swing for counterbalance, the "
            "lead arm dropping across the body as the rear arm guards. "
            "Contact with the shin, not the instep, is the iron rule: the "
            "shin is a dense striking surface while the foot breaks "
            "against elbows and knees. Fighters condition their shins for "
            "months on the heavy bag before throwing low kicks at full "
            "power in sparring, because an unconditioned shin against a "
            "checked kick is an injury."
        ),
        "how_it_works": (
            "From stance, step the lead foot about six inches to the "
            "outside - this opens the hip for the swing. Pivot hard on the "
            "ball of the standing foot, turning the heel toward the "
            "opponent as the kicking hip swings over like a bat. Lift the "
            "kicking leg with the knee bent, then whip the lower leg out "
            "so the shin travels horizontally into the opponent's lead "
            "thigh just above the knee. At the moment of the swing, drop "
            "the same-side arm down across the body for counterbalance "
            "and keep the opposite glove at the chin. Strike with the "
            "lower shin, roughly four inches above the ankle - never the "
            "foot or ankle. Follow through two to three inches past "
            "contact, then rechamber the leg and set it back down into "
            "stance without hopping. Drill on the heavy bag in sets of "
            "ten per leg, starting at half power until the shin "
            "conditions, listening for the deep thud of shin on bag. "
            "Practice the step-pivot-swing as one motion in the mirror "
            "before adding power."
        ),
        "key_points": [
            "The low kick is kickboxing's signature weapon: a shin-driven roundhouse to the lead thigh that deadens the leg, slows footwork, and drops the hands.",
            "Mechanics are a full-body whip - step out, pivot the standing foot, swing the hip over like a bat, chop the shin horizontally into the thigh.",
            "The iron rule is shin contact, never foot or ankle: the shin is the striking surface, the foot breaks against checks.",
            "In the Dutch style the low kick is the anvil that punch combinations hammer against, thrown at the end of every combination.",
            "Shins are conditioned for months on the heavy bag before full-power sparring - an unconditioned shin against a check is an injury.",
        ],
        "requirements": [
            "A heavy bag for months of progressive shin conditioning before full-power partner work.",
            "Bare shins or light shin guards in early training; full shin guards for partner sparring.",
            "Confirmed hip mobility for the step-out and pivot - the kick starts with the standing leg, not the kicking leg.",
            "A coach to verify shin contact (not foot) and the follow-through that marks a committed kick.",
            "Patience with conditioning: shin density builds over months, and rushing it causes fractures.",
        ],
        "standards": [
            "Low kick mechanics follow the standard roundhouse form taught across K-1, Dutch, and American kickboxing styles.",
            "The thigh above the knee is a legal target under WAKO, ISKA, and K-1 rules; kicks to the knee joint itself are restricted.",
            "Shin contact is the universal technical standard - instep contact is scored as poor technique across rule sets.",
        ],
        "citations": [CIT_WAKO, CIT_ISKA, CIT_K1],
        "sig_lens": (
            "The Signature read: the low kick is the signature's foundation "
            "stroke, written low and heavy. Where public instruction whips "
            "the shin, the Signature Combat Method sees the anvil oath - "
            "the leg sworn to chop, the thigh the page, the deep thud the "
            "period at the end of the sentence. Conditioned over months, "
            "never rushed."
        ),
    },
    {
        "key": "roundhouse_body",
        "name": "The Roundhouse Kick to the Body",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The roundhouse kick to the body - the mid kick - is the "
            "heavy artillery of kickboxing, a shin-driven arc into the "
            "ribs or the liver that ends fights outright. It uses the "
            "same full-body whip as the low kick but aimed higher: the "
            "standing foot pivots a full one hundred eighty degrees, the "
            "hip turns completely over, and the shin travels on a "
            "horizontal or slightly rising arc into the floating ribs. A "
            "clean mid kick to the liver drops even conditioned fighters, "
            "because the liver shot disrupts the body's equilibrium in a "
            "way no conditioning prevents. The kick demands more setup "
            "than the low kick - the higher target is easier to see, "
            "block, or catch - so fighters hide it behind punches, throw "
            "it when the opponent's elbows lift, or fire it as the "
            "opponent steps in. The arms swing hard for counterbalance, "
            "and the opposite hand must stay home because the mid kick "
            "takes longer to return than any punch. Fighters drill the "
            "mid kick endlessly on the bag and the Thai pads, because the "
            "difference between a slapping mid kick and a fight-ending "
            "one is entirely in the hip turnover and the commitment to "
            "follow through."
        ),
        "how_it_works": (
            "From stance, step the lead foot slightly outward and begin "
            "the pivot on the ball of the standing foot. As the hip starts "
            "to turn over, lift the kicking knee high - the knee points at "
            "the target before the shin extends, which hides the kick's "
            "destination. Pivot the standing foot a full one hundred "
            "eighty degrees, heel pointing at the opponent, as the hip "
            "turns completely over and the shin whips horizontally into "
            "the ribs or the liver. Swing the same-side arm down and "
            "across for counterbalance while the opposite glove stays "
            "glued to the chin. Strike with the lower shin and follow "
            "through three to four inches past contact, letting the "
            "momentum carry the leg through. Rechamber by bending the "
            "knee and set the foot back down into stance. Drill the "
            "knee-up-then-whip sequence slowly in the mirror ten times "
            "per leg, then ten full-power mid kicks per leg on the heavy "
            "bag, checking that the standing foot completes its full "
            "pivot every time."
        ),
        "key_points": [
            "The mid kick is heavy artillery: a shin-driven arc into the ribs or liver that ends fights, with the liver shot dropping even conditioned fighters.",
            "It uses the low kick's full-body whip aimed higher - standing foot pivots one hundred eighty degrees, hip turns completely over.",
            "The knee points at the target before the shin extends, hiding the kick's destination until the last instant.",
            "It needs setup - hidden behind punches, thrown as elbows lift, or fired as the opponent steps in - because the high target is easier to see and catch.",
            "The difference between a slap and a fight-ender is entirely hip turnover and follow-through commitment.",
        ],
        "requirements": [
            "A heavy bag and Thai pads for high-volume mid-kick development with a holder who can take the power.",
            "Conditioned shins from months of low-kick bag work before full-power mid kicks in sparring.",
            "Hip mobility sufficient for full turnover - the kick fails without the one-hundred-eighty-degree standing-foot pivot.",
            "Setup punches drilled first, since the mid kick thrown naked is the most caught kick in the sport.",
            "A coach to confirm the knee-lift disguise and the complete hip turnover on every repetition.",
        ],
        "standards": [
            "Mid-kick mechanics follow the standard roundhouse form of K-1 and Dutch kickboxing.",
            "The ribs and abdomen are legal targets under WAKO, ISKA, and K-1 rules; the spine and kidneys are fouls.",
            "Full hip turnover with shin contact is the technical standard distinguishing the scoring kick from the slap.",
        ],
        "citations": [CIT_WAKO, CIT_ISKA, CIT_K1],
        "sig_lens": (
            "The Signature read: the mid kick is the signature pressed "
            "through the page. Where public instruction turns the hip "
            "over, the Signature Combat Method sees the heavy stroke - "
            "the whole body committed behind one arc, the liver the "
            "period that ends the argument. Hidden behind punches, "
            "delivered with the full turn, never slapped."
        ),
    },
    {
        "key": "teep",
        "name": "The Teep (Push Kick)",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The teep is the push kick of kickboxing: the ball or heel of "
            "the foot driven straight into the opponent's midsection, hip, "
            "or thigh to stop forward motion dead. Where the roundhouse "
            "kicks chop with the shin, the teep thrusts with the foot like "
            "a piston, and its job is distance management - it is the long "
            "weapon that keeps aggressive opponents at the end of the "
            "fighter's range. A sharp teep to the solar plexus knocks the "
            "wind out; a teep to the lead thigh jams the opponent's step; "
            "a teep to the hip turns their whole advance aside. The "
            "mechanics are a chamber and a thrust: the knee lifts high "
            "with the foot cocked, then the leg extends straight, driving "
            "the hips forward behind it, and the foot lands flat - ball "
            "or full sole - before retracting on the same line. The teep "
            "is also the great setup weapon: opponents who brace for the "
            "push drop their hands, opening the head for the roundhouse "
            "that follows, and the teep-to-roundhouse is one of the "
            "classic Dutch combinations. Because it is a push rather than "
            "a whip, the teep is economical - it costs little energy, "
            "lands from long range, and rarely leaves the fighter "
            "unbalanced, which is why fighters throw it dozens of times "
            "per round."
        ),
        "how_it_works": (
            "From stance, lift the lead knee high toward the chest, "
            "cocking the foot so the toes pull back and the ball or heel "
            "presents flat. Drive the hips forward as the leg extends "
            "straight into the target - midsection, lead thigh, or hip - "
            "pushing through about four inches. Keep the standing leg "
            "slightly bent and the guard up, with the same-side arm "
            "swinging down for balance and the opposite glove at the chin. "
            "At full extension the foot should land flat, not with the "
            "toes, to spread the force and protect the toes. Retract the "
            "leg along the same straight line back to the chamber, then "
            "set the foot down into stance - never let it drop wide. For "
            "the rear teep, add a small forward step with the lead foot "
            "first to close distance, then chamber and thrust the rear "
            "leg. Drill the chamber-to-thrust slowly ten times per leg in "
            "the mirror, checking the flat foot, then fifty teeps per leg "
            "on the heavy bag focusing on the push-through and the clean "
            "retraction."
        ),
        "key_points": [
            "The teep is a piston thrust with the ball or heel of the foot, and its job is distance management - stopping forward motion dead from long range.",
            "Mechanics are chamber then thrust: knee lifts high with the foot cocked, the leg extends straight with the hips driving behind it, the foot lands flat.",
            "It is economical - low energy cost, long range, rarely unbalanced - which is why fighters throw it dozens of times per round.",
            "The teep is the great setup weapon: opponents bracing for the push drop their hands, opening the head for the roundhouse behind it.",
            "Retract on the same straight line back to chamber; a teep that drops wide leaves the fighter open and off balance.",
        ],
        "requirements": [
            "Ankle and calf flexibility to cock the foot flat - toes presented to the target risk broken toes.",
            "A heavy bag for push-through development and a partner with a body protector for timing the teep against advances.",
            "Hip drive strength, since the thrust is powered by the hips pushing behind the extending leg.",
            "Balance drills: the teep is held at full extension for two seconds per repetition to build single-leg stability.",
            "A coach to verify the flat-foot landing and the straight-line retraction.",
        ],
        "standards": [
            "Teep mechanics follow the standard push-kick form shared across kickboxing and its parent striking arts.",
            "Legal teep targets are the torso front and side and the thighs under WAKO, ISKA, and K-1 rules.",
            "The flat-foot presentation is the technical standard - toe-first contact is scored as faulty technique.",
        ],
        "citations": [CIT_WAKO, CIT_ISKA, CIT_K1],
        "sig_lens": (
            "The Signature read: the teep is the signature's firm hand. "
            "Where public instruction pistons the foot, the Signature "
            "Combat Method sees the palm pressed to the page - hold, "
            "stop, this far and no farther. The straight-line return is "
            "the oath: what pushes out comes back true."
        ),
    },
    {
        "key": "front_snap_kick",
        "name": "The Front Snap Kick",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The front snap kick is the fastest kick in kickboxing: the "
            "knee chambers high and the lower leg snaps out and back like "
            "a whip, striking with the ball of the foot. Where the teep "
            "pushes, the snap kick cracks - it is a speed weapon aimed at "
            "the chin, nose, or solar plexus, thrown in the blink of an "
            "eye opening. Its power comes from the snap, not the push: "
            "the thigh drives up, the lower leg extends explosively, and "
            "at the instant of contact the leg is already retracting, "
            "which concentrates the force into a sharp impact rather than "
            "a shove. The snap kick is the great interrupter - it fires "
            "straight up the middle into an opponent who is stepping in, "
            "and because it chambers and returns so quickly, it is one of "
            "the safest kicks to throw. Fighters use it to punish "
            "aggression, to score quick points to the head in "
            "points-oriented rule sets, and as the opening beat of "
            "combinations. The chamber is everything: a high, tight "
            "chamber hides the kick until it fires and loads the snap, "
            "while a low, lazy chamber telegraphs and weakens it."
        ),
        "how_it_works": (
            "From stance, drive the lead knee straight up toward the "
            "chest, keeping the thigh high and the lower leg folded - "
            "this is the chamber, and it should be tight and fast. Cock "
            "the foot by pulling the toes back so the ball of the foot "
            "presents. Snap the lower leg out explosively toward the "
            "target - chin, nose, or solar plexus - extending the knee "
            "fully at the last instant. At the moment of contact, begin "
            "retracting: fold the lower leg back as fast as it extended, "
            "so the impact is a crack rather than a push. Keep the guard "
            "up throughout, leaning the torso back slightly away from the "
            "target to add reach and protect the head. Set the foot back "
            "down into stance along the same line. For the rear-leg snap "
            "kick, slide the lead foot forward a half step first, then "
            "chamber the rear knee. Drill the chamber-snap-retract as one "
            "beat: ten slow per leg checking the tight chamber, then "
            "thirty seconds of rapid snap kicks on the bag per leg, "
            "counting only the ones that crack."
        ),
        "key_points": [
            "The front snap kick is the fastest kick in the sport: chamber high, snap the lower leg out and back like a whip, strike with the ball of the foot.",
            "Power comes from the snap, not the push - the leg is already retracting at contact, concentrating force into a sharp crack.",
            "It is the great interrupter, fired straight up the middle into an opponent stepping in, and one of the safest kicks to throw.",
            "The chamber is everything: high and tight hides the kick and loads the snap; low and lazy telegraphs and weakens it.",
            "Lean the torso back slightly at extension for reach and head safety, and return the foot along the same line.",
        ],
        "requirements": [
            "Hip flexor strength and hamstring flexibility for the high tight chamber and the explosive snap.",
            "Toe-cocking discipline: the ball of the foot strikes, never the toes, to avoid breaks.",
            "A heavy bag or shield for snap timing and a partner for interrupting-the-advance drills.",
            "Core stability for the slight rearward lean at full extension without losing balance.",
            "A coach to verify the retraction starts at contact - the mark of the snap versus the push.",
        ],
        "standards": [
            "Snap-kick mechanics follow the standard chamber-snap-retract form taught across kickboxing styles.",
            "The ball of the foot is the striking surface; head contact is legal under full-contact rules including K-1 and ISKA.",
            "The one-beat chamber-to-return timing is the technical standard for the kick's defensive safety.",
        ],
        "citations": [CIT_WAKO, CIT_ISKA, CIT_K1],
        "sig_lens": (
            "The Signature read: the snap kick is the signature's quick "
            "stroke. Where public instruction chambers and cracks, the "
            "Signature Combat Method sees the fastest mark the hand "
            "makes - in and gone before the page knows it was touched. "
            "The retraction at contact is the oath: speed sworn, power "
            "kept, nothing left behind."
        ),
    },
    {
        "key": "knee_strike",
        "name": "The Knee Strike",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The knee strike is the close-range destroyer of kickboxing: "
            "the point of the knee driven upward into the ribs, solar "
            "plexus, or thigh from the clinch or from punching range. It "
            "is one of the most damaging strikes in the sport because the "
            "knee is a hard, compact surface backed by the full drive of "
            "the hips and the standing leg - a well-placed knee to the "
            "body folds opponents and ends fights. The mechanics are a "
            "violent hip thrust: the fighter grabs or frames the "
            "opponent's head, neck, or arms for control, rises onto the "
            "ball of the standing foot, and drives the knee upward and "
            "slightly forward, thrusting the hips through the target. The "
            "striking surface is the top of the knee and the first inches "
            "of the thigh. Knees are thrown in the clinch as the primary "
            "weapon there, and outside the clinch as single shots when an "
            "opponent ducks into range. Defense against knees is "
            "position: keep the hips back, frame with the arms, and never "
            "let the opponent lock both hands behind your head. Under "
            "some American rule sets knees are limited, while K-1 and "
            "Dutch rules embrace them - the fighter must know the rule "
            "set before building a knee game."
        ),
        "how_it_works": (
            "From close range or the clinch, secure control: one hand "
            "behind the opponent's neck or a strong double forearm frame "
            "across their shoulders. Rise onto the ball of the standing "
            "foot and pull the opponent's head or torso down slightly as "
            "you drive your hips forward and up. Whip the knee upward on "
            "a tight path into the ribs, solar plexus, or lead thigh, "
            "striking with the top of the knee. At impact the standing "
            "leg should be nearly straight and the hips fully thrust "
            "through - the power is the hip drive, not the leg lift. "
            "Keep the guard arm up on the side you are not controlling "
            "with, because knees are often answered with punches. Return "
            "the knee straight down to the floor into stance; do not let "
            "it swing wide. Drill on the heavy bag held at an angle: ten "
            "knees per leg focusing on the hip thrust, then clinch-knee "
            "rounds with a partner wearing a body protector, trading "
            "control and single knees at half power."
        ),
        "key_points": [
            "The knee is the close-range destroyer: the point of the knee driven up into ribs, solar plexus, or thigh, backed by full hip drive.",
            "Mechanics are a violent hip thrust from a risen standing foot, with head or frame control pulling the target down into the strike.",
            "It is the primary weapon of the clinch and a single-shot answer when an opponent ducks into range.",
            "Knee defense is position: hips back, strong frames, and never letting the opponent lock both hands behind your head.",
            "Rule sets differ sharply - limited under some American rules, embraced under K-1 and Dutch rules - so know the rule set before building a knee game.",
        ],
        "requirements": [
            "A heavy bag or body protector and a partner for clinch-knee drilling at controlled power.",
            "Hip flexor and core power for the thrust, plus single-leg balance from rising onto the ball of the standing foot.",
            "Clinch control fundamentals (frames, neck control) before knees are thrown - the knee without control is a gift.",
            "Knowledge of the specific rule set's knee allowances before sparring with knees.",
            "A coach to verify the hip thrust-through and the straight-down return that keep the striker balanced.",
        ],
        "standards": [
            "Knee mechanics follow the standard clinch-knee form of K-1 and Dutch kickboxing.",
            "Legal knee targets under K-1 rules include the head and body; some American rule sets restrict knees - the fighter competes under the announced rules.",
            "The hip-thrust-through with the standing leg extended is the technical standard for power delivery.",
        ],
        "citations": [CIT_K1, CIT_WAKO, CIT_ISKA],
        "sig_lens": (
            "The Signature read: the knee is the signature driven upward. "
            "Where public instruction thrusts the hip, the Signature "
            "Combat Method sees the rising seal - close, committed, and "
            "final, the body pressing its mark from below. Control first "
            "is the oath: no knee without the frame that earns it."
        ),
    },
    {
        "key": "one_two",
        "name": "The One-Two Combination",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The one-two - jab followed by cross - is the foundation of "
            "all kickboxing combinations and the most thrown two-punch "
            "sequence in the sport. Its genius is mechanical: the jab "
            "occupies the opponent's guard and vision while measuring the "
            "distance, and the rotation that recovers the jab loads the "
            "cross behind it, so the second punch arrives with the full "
            "body already coiled. The jab need not land hard; its job is "
            "to blind, distract, and set the range, while the cross is "
            "the payload. Thrown correctly the one-two takes under a "
            "second, with the cross landing as the jab's glove returns - "
            "the two punches overlap like a piston cycle rather than "
            "firing as separate events. Footwork carries it: a small step "
            "with the jab closes the distance, and the cross lands with "
            "the weight transferred forward. Every advanced combination "
            "in this database is built on the one-two's rhythm - occupy "
            "with the first strike, deliver with the second - and fighters "
            "drill it daily for their entire careers because its timing "
            "decays without practice. The one-two also teaches the "
            "cardinal rule of combinations: the hand that just punched "
            "returns to guard while the other hand fires."
        ),
        "how_it_works": (
            "From stance, throw the jab with a small forward step, "
            "letting the lead shoulder roll to cover the chin. The "
            "instant the jab reaches full extension, begin the cross: "
            "pivot the rear foot, rotate the rear hip and shoulder, and "
            "drive the rear hand straight down the middle over the top of "
            "the returning jab. Time it so the cross lands as the jab "
            "glove arrives back at the cheek - the punches overlap, not "
            "sequence. Keep the chin tucked behind the lead shoulder "
            "through the cross and the lead glove home before the cross "
            "finishes. After the cross lands, snap it straight back and "
            "either step out at an angle or reset to stance - never stand "
            "still admiring the work. Drill the rhythm on the mitts: the "
            "holder calls the one-two at random intervals and the fighter "
            "fires instantly, ten repetitions, then ten more stepping in "
            "from outside range. Finish with bag rounds of continuous "
            "one-twos, counting the pairs and keeping every jab snapping "
            "back before the cross completes."
        ),
        "key_points": [
            "The one-two is the foundation of all combinations: jab occupies guard, vision, and distance while its recovery rotation loads the cross behind it.",
            "The jab is the setup and the cross is the payload - the jab need not land hard, the cross must land true.",
            "Correctly thrown it takes under a second, with the punches overlapping like a piston cycle rather than firing as separate events.",
            "The cardinal rule of combinations is learned here: the hand that just punched returns to guard while the other hand fires.",
            "Footwork carries it - a small step with the jab closes distance, and the fighter exits at an angle or resets after the cross.",
        ],
        "requirements": [
            "A reliable jab and cross individually before they are combined - the combination is only as clean as its parts.",
            "Focus mitts and a holder for timing the overlap, plus a heavy bag for volume and power.",
            "Footwork drills for the entry step and the angled exit that bookend the combination.",
            "Daily repetition: the one-two's timing decays without practice and is drilled for entire careers.",
            "A coach to verify the overlap timing - cross landing as the jab returns - which is the combination's whole secret.",
        ],
        "standards": [
            "The one-two follows the classic jab-cross sequence codified across boxing and kickboxing instruction.",
            "The sub-second two-punch timing is the performance standard for a fight-ready one-two.",
            "Guard recovery between punches follows the standard that one hand is always home.",
        ],
        "citations": [CIT_DEMPSEY, CIT_HATMAKER],
        "sig_lens": (
            "The Signature read: the one-two is the signature's first "
            "two strokes joined. Where public instruction overlaps the "
            "punches, the Signature Combat Method sees the name and its "
            "underline written as one motion - the jab signs, the cross "
            "seals, and the guard keeps what both have written."
        ),
    },
    {
        "key": "jab_cross_hook",
        "name": "The Jab-Cross-Hook Combination",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The jab-cross-hook - the classic one-two-three - is the most "
            "famous combination in striking: two straight punches down "
            "the middle followed by the lead hook arcing around the "
            "guard. Its logic is geometric. The jab and cross force the "
            "opponent to shell behind a high, tight guard to survive the "
            "straight punches; the moment the guard tightens, the sides "
            "of the head open, and the hook travels exactly there. Each "
            "punch sets up the next: the jab measures and blinds, the "
            "cross commits the opponent's guard high and central, and the "
            "hook exploits the opening the first two created. The rhythm "
            "is one-two-THREE, with the hook thrown with full hip pivot "
            "as the cross hand returns. The combination teaches weight "
            "transfer in both directions - forward onto the lead foot "
            "for the straight punches, then the sharp pivot that whips "
            "the hook. Defensively the rule intensifies: with three "
            "punches committed, the fighter must exit at an angle or "
            "pivot out the instant the hook returns, because a stationary "
            "fighter after a three-punch combination is the easiest "
            "counter target in the sport."
        ),
        "how_it_works": (
            "Throw the one-two exactly as drilled: jab with the step, "
            "cross overlapping as the jab returns. As the cross reaches "
            "full extension, pivot the lead foot hard inward and rotate "
            "the lead hip and shoulder, whipping the lead hook on its "
            "tight arc to the side of the head. The hook fires while the "
            "cross hand is returning - never wait for the cross to come "
            "fully home before starting the hook, or the rhythm breaks. "
            "Keep the elbow at shoulder height through the hook and the "
            "rear glove at the chin. The instant the hook returns along "
            "its arc, pivot out at forty-five degrees or step laterally "
            "out of range - do not stand in the pocket after three "
            "committed punches. Drill the sequence on the mitts in three "
            "counts called by the holder, ten slow for geometry then "
            "twenty at speed. Then drill the exit: one-two-three, pivot "
            "out, reset - the combination is not finished until the "
            "fighter is safe again."
        ),
        "key_points": [
            "The jab-cross-hook is geometric: straight punches force the guard high and tight, and the hook travels exactly where the guard opened - around the side.",
            "Each punch sets up the next: jab measures and blinds, cross commits the guard central, hook exploits the created opening.",
            "The rhythm is one-two-THREE with the hook firing while the cross hand returns - waiting breaks the combination.",
            "It teaches weight transfer in both directions: forward drive for the straights, sharp pivot for the hook.",
            "After three committed punches the fighter must exit at an angle or pivot out instantly - stationary after a combination is the easiest counter target.",
        ],
        "requirements": [
            "A drilled one-two before the hook is added - the three-punch combination inherits the timing of the two-punch one.",
            "Focus mitts for the three-count rhythm and a heavy bag for the full-power hook finish.",
            "Pivot and exit footwork drilled as part of the combination, not as an afterthought.",
            "Head movement discipline: the chin stays tucked through all three punches.",
            "A coach to confirm the hook's tight arc and the immediate angled exit.",
        ],
        "standards": [
            "The one-two-three follows the standard combination progression taught across boxing and kickboxing.",
            "Hook geometry follows the standard tight-arc, shoulder-height-elbow form.",
            "The immediate angled exit follows the standard combination-safety rule of never standing still after committed offense.",
        ],
        "citations": [CIT_DEMPSEY, CIT_HATMAKER, CIT_WAKO],
        "sig_lens": (
            "The Signature read: the jab-cross-hook is the full signature "
            "in three strokes. Where public instruction stacks geometry, "
            "the Signature Combat Method sees the complete name - straight "
            "down, straight through, and the sealing curve. The angled "
            "exit is the oath: the hand leaves the page clean."
        ),
    },
    {
        "key": "blocking_parrying",
        "name": "Blocking and Parrying Punches",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Blocking and parrying are the two hand defenses against "
            "punches, and they work on opposite principles. The block "
            "absorbs: the glove, forearm, or elbow meets the punch "
            "head-on and takes its force on a hard, braced surface - the "
            "high block catches hooks on the glove and forearm, the "
            "elbow block takes body hooks on the point of the elbow, "
            "the cross-block covers against straight punches. The parry "
            "redirects: an open glove or the palm slaps the incoming "
            "punch slightly offline so it misses by inches, costing "
            "almost no energy and leaving the opponent extended and open "
            "for the counter. Beginners block everything because it is "
            "instinctive; advanced fighters parry more because it is "
            "cheaper and creates counters. Both demand the same "
            "foundation: eyes open, chin tucked, stance balanced, and the "
            "defense timed to the punch - a block thrown early is just a "
            "raised arm, and a parry thrown late is a punch in the face. "
            "The golden rule of hand defense is that the defending hand "
            "returns to guard instantly, because the opponent's second "
            "punch is already coming. Fighters drill blocks and parries "
            "against every punch in the arsenal until the response is "
            "reflex, since thinking about defense in a fight means the "
            "punch has already landed."
        ),
        "how_it_works": (
            "For the high block against hooks: as the punch comes, raise "
            "the glove and forearm to meet it, tucking the chin behind "
            "the guard and bracing the stance - take the punch on the "
            "glove and forearm, never on the open face. For the elbow "
            "block against body hooks: drop the elbow to the ribs and "
            "take the punch on the point of the elbow, the hardest "
            "surface on the arm. For the parry against straight punches: "
            "as the jab or cross extends, slap it gently offline with the "
            "open lead glove - a two-inch deflection at your glove becomes "
            "almost three inches of miss at your head, and the head only "
            "needs inches to be safe. Keep the parrying motion "
            "small; a big swat opens your own guard. The instant the "
            "punch is dealt with, snap the defending hand back to guard. "
            "Drill with a partner at half speed: they throw jab, cross, "
            "lead hook, rear hook in random order, and you answer each "
            "with the correct block or parry, ten minutes building from "
            "slow to full speed. Add the counter: parry the jab, fire "
            "your own jab through the opening."
        ),
        "key_points": [
            "Blocking absorbs on hard braced surfaces - glove, forearm, elbow - while parrying redirects the punch inches offline with an open glove.",
            "Beginners block everything by instinct; advanced fighters parry more because it costs less energy and creates counter openings.",
            "Both demand eyes open, chin tucked, balanced stance, and timing matched to the punch - early is a raised arm, late is a punch in the face.",
            "The defending hand returns to guard instantly, because the opponent's second punch is already coming.",
            "Drill against every punch until the response is reflex - thinking about defense in a fight means the punch already landed.",
        ],
        "requirements": [
            "A partner to throw controlled punches in random order at increasing speed.",
            "Gloves and headgear for block-and-parry sparring drills once the basics are reflexive.",
            "Elbow conditioning awareness: the elbow block works because the elbow is hard, but it must meet the punch, not chase it.",
            "Ten-minute reaction rounds building from half speed to full speed.",
            "A coach to correct big parrying motions and late blocks before they become habits.",
        ],
        "standards": [
            "Block and parry mechanics follow the standard hand-defense forms taught across boxing and kickboxing.",
            "The two-inch deflection principle of the parry is the standard efficiency measure of the technique.",
            "Instant guard return follows the universal defensive standard of the sport.",
        ],
        "citations": [CIT_DEMPSEY, CIT_HATMAKER],
        "sig_lens": (
            "The Signature read: blocks and parries are the signature "
            "defended. Where public instruction absorbs and redirects, "
            "the Signature Combat Method sees the honor guard at work - "
            "the wall taking what it must, the palm turning aside what "
            "it need not suffer. The instant return is the oath: the "
            "guard never abandons its post."
        ),
    },
    {
        "key": "slip_weave_roll",
        "name": "The Slip, Weave, and Roll",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The slip, weave, and roll are head-movement defenses that "
            "make punches miss by inches without spending the energy of "
            "blocking. The slip moves the head just off the center line - "
            "a few inches left or right - so a straight punch passes "
            "harmlessly by; the weave dips the head side to side under a "
            "hook's arc; the roll rotates the shoulders and torso to ride "
            "with a punch's force, bleeding its power. Their shared "
            "principle is economy: the head moves the minimum distance "
            "needed, the eyes stay on the opponent, the stance stays "
            "balanced, and the body stays loaded to punch back instantly. "
            "Head movement is what separates advanced defense from "
            "beginner defense - the beginner covers and absorbs, the "
            "advanced fighter is simply not there, and the missed punch "
            "leaves the opponent extended and exhausted. The danger of "
            "head movement is rhythm: moving the head in a predictable "
            "pattern lets the opponent time it, and dipping without "
            "watching walks the head into uppercuts and knees. Fighters "
            "drill slips and weaves on the slip rope, the maize bag, and "
            "against partner punches until the movement is small, fast, "
            "and always paired with a counter - because head movement "
            "that does not lead to offense is just dancing."
        ),
        "how_it_works": (
            "For the slip against the jab: as the punch extends, rotate "
            "the torso slightly and shift the head three to four inches "
            "to the outside - the punch should pass beside the ear. Keep "
            "the eyes on the opponent and the weight centered; do not "
            "lean. For the weave against the hook: bend the knees and dip "
            "the head under the punch's arc, moving side to side like a "
            "pendulum, staying low and compact. For the roll: as a hook "
            "or overhand arrives, rotate the shoulders with it, letting "
            "the punch glance off the forehead or shoulder while the "
            "torso turns - ride the force, do not resist it. After every "
            "slip, weave, or roll, fire the counter immediately: slip the "
            "jab outside and answer with the cross, weave under the hook "
            "and answer with the hook to the body. Drill on the slip rope "
            "strung at shoulder height: slip left, slip right, weave "
            "under, ten minutes keeping the movement small. Then partner "
            "drills: they throw slow combinations, you defend with head "
            "movement only and counter every third punch."
        ),
        "key_points": [
            "Slip, weave, and roll make punches miss by inches - the slip moves the head off center, the weave dips under hooks, the roll rides with the force.",
            "The shared principle is economy: minimum head movement, eyes on the opponent, stance balanced, body loaded to counter instantly.",
            "Head movement separates advanced defense from beginner defense - the beginner absorbs, the advanced fighter is simply not there.",
            "The danger is rhythm: predictable head movement gets timed, and dipping blind walks the head into uppercuts and knees.",
            "Head movement must lead to offense - slip and counter, weave and counter - or it is just dancing.",
        ],
        "requirements": [
            "A slip rope strung at shoulder height or a maize bag for solo head-movement drilling.",
            "A partner to throw slow, controlled combinations for defensive drilling before any speed is added.",
            "Neck strength work, since the head must stay stable and the eyes level through rapid movement.",
            "Counter-punching fundamentals, because every slip drill ends with the counter that justifies the movement.",
            "A coach to keep the movement small - beginners always move the head too far, which costs balance and counters.",
        ],
        "standards": [
            "Slip, weave, and roll mechanics follow the standard head-movement forms codified across boxing and kickboxing.",
            "The three-to-four-inch slip distance is the economy standard - enough to miss, small enough to counter.",
            "Eyes-on-opponent throughout follows the universal defensive standard.",
        ],
        "citations": [CIT_DEMPSEY, CIT_HATMAKER],
        "sig_lens": (
            "The Signature read: head movement is the signature unwritten. "
            "Where public instruction slips and weaves, the Signature "
            "Combat Method sees the name refusing the page - the punch "
            "arrives and the mark is not there, only the counter left "
            "behind. Small and true is the oath: never move more than "
            "the miss requires."
        ),
    },
    {
        "key": "checking_kicks",
        "name": "Checking Low Kicks",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The check is the primary defense against the low kick: the "
            "defender lifts the lead leg, turning the shin outward to "
            "meet the incoming kick shin-to-shin. It works on brutal "
            "simplicity - the attacker's shin, the hardest weapon in "
            "kickboxing, meets the defender's shin, equally hard, and the "
            "attacker's kick breaks against it instead of the soft thigh. "
            "A checked low kick hurts the kicker more than the defender, "
            "which is why fighters who cannot check get their legs "
            "chopped down round after round while fighters who check well "
            "discourage the low kick entirely. The mechanics are fast: "
            "read the hip turnover that telegraphs the kick, lift the "
            "lead knee and rotate the shin outward so its hard outer edge "
            "faces the incoming shin, brace on the standing leg, and take "
            "the impact high on the shin near the knee where the bone is "
            "thickest. The check must be timed - lifted too early it is "
            "just a raised leg the kicker goes around; too late and the "
            "kick lands on the thigh. Fighters drill the check as a "
            "reflex against pad-fed low kicks until the leg lifts on "
            "sight of the hip turn, because thinking about the check "
            "means the thigh has already been hit."
        ),
        "how_it_works": (
            "Watch the opponent's hips, not their eyes - the hip turnover "
            "is the telegraph of every low kick. The instant the hip "
            "turns, lift the lead knee to waist height and rotate the "
            "shin outward so its hard outer edge faces the incoming "
            "kick. Keep the foot flexed and the toes pulled back. Brace "
            "on the standing leg with a slight knee bend, keep the guard "
            "up, and lean the torso slightly away from the kick. Meet "
            "the kick high on your shin, near the knee where the bone is "
            "thickest - never low near the ankle. The moment the shins "
            "clash, set the leg back down into stance and be ready to "
            "counter: the classic answer is the checked kick followed "
            "instantly by your own low kick to their now-planted leg, or "
            "a cross down the middle. Drill with a partner tapping low "
            "kicks at quarter power: read the hip, lift the check, ten "
            "per leg, then build speed until the check fires on reflex. "
            "Condition the checking shin on the bag alongside the kicking "
            "shin - both need the months of work."
        ),
        "key_points": [
            "The check meets the incoming low kick shin-to-shin, so the attacker's hardest weapon breaks against an equally hard surface instead of the soft thigh.",
            "A checked kick hurts the kicker more than the defender - good checking discourages the low kick entirely.",
            "Read the hip turnover, lift the lead knee, rotate the shin outward, and meet the kick high near the knee where the bone is thickest.",
            "Timing is everything: too early is a raised leg to go around, too late is a kick on the thigh.",
            "The check is a reflex drilled against pad-fed kicks, and it sets up the classic counter - check, then fire your own low kick at their planted leg.",
        ],
        "requirements": [
            "A partner to feed controlled low kicks at increasing speed for check-timing drills.",
            "Shin conditioning on the heavy bag for the checking leg as well as the kicking leg.",
            "Hip-reading discipline: eyes on the opponent's hips and shoulders, never fixed on their eyes alone.",
            "Balance on the standing leg under impact - single-leg stability work supports the brace.",
            "A coach to verify the outward shin rotation and the high contact point near the knee.",
        ],
        "standards": [
            "The shin check follows the standard low-kick defense taught across K-1, Dutch, and American kickboxing.",
            "High-shin contact near the knee is the technical standard for both safety and damage to the kicker.",
            "The check-and-counter sequence follows the standard defensive-counter rhythm of the sport.",
        ],
        "citations": [CIT_WAKO, CIT_ISKA, CIT_K1],
        "sig_lens": (
            "The Signature read: the check is the signature meeting "
            "itself. Where public instruction lifts the shin, the "
            "Signature Combat Method sees oath against oath - hard "
            "sworn against hard, the attacker's own weapon turned to "
            "testify against them. High on the shin is the measure: "
            "meet strength with strength, never with softness."
        ),
    },
    {
        "key": "catching_sweeps",
        "name": "Catching Kicks and Sweeps",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Catching a kick means trapping the opponent's leg - usually "
            "the mid kick - under the arm or against the body, and the "
            "sweep means using that trapped leg as a lever to dump the "
            "opponent to the canvas. It is the great punishment for "
            "predictable kicking: the fighter who throws naked mid kicks "
            "without setups gets their leg caught, and a caught leg is a "
            "lost exchange at minimum and a knockdown at worst. The catch "
            "works by stepping slightly offline and wrapping the arm "
            "around the incoming shin at the moment it arrives, pinning "
            "it tight to the ribs - the leg must be trapped, not merely "
            "touched, or the kicker pulls it free and counters. Once "
            "caught, the options multiply: sweep the standing leg with "
            "your own leg or foot, drive forward to off-balance them, or "
            "fire the free hand's cross while they hop on one leg. The "
            "sweep itself is a lever play - hook behind their standing "
            "ankle or calf and pull while pushing their upper body, "
            "toppling them sideways. Rule sets govern the follow-up: "
            "most allow the sweep and a brief moment of advantage, none "
            "allow striking a downed opponent. Fighters drill the catch "
            "against telegraphed mid kicks until the trap is reflexive, "
            "because a slow catch attempt against a fast kick is just a "
            "rib shot taken on the arm."
        ),
        "how_it_works": (
            "Read the mid kick early from the knee lift and hip turn. "
            "Step the lead foot six inches offline to the outside as the "
            "kick arrives, and wrap your lead arm around the incoming "
            "shin, pinning it tight against your ribs - clamp the elbow "
            "down hard so the leg cannot be yanked free. Keep your guard "
            "hand up, because the kicker's hands are still dangerous. "
            "For the sweep: keep their leg trapped high against your "
            "side, step your lead leg behind their standing ankle, and "
            "pull their ankle toward you while driving your shoulder into "
            "their chest - the lever topples them sideways. Alternatively, "
            "drive forward into them while holding the leg to force the "
            "hop-and-fall, or release the leg and fire the cross as they "
            "stumble. Never hold the caught leg above waist height for "
            "more than a beat - rule sets limit the advantage time. "
            "Drill with a partner throwing slow mid kicks: catch, trap, "
            "sweep, ten per side, then build speed. Always practice the "
            "release: let go cleanly and reset rather than holding on "
            "into a foul."
        ),
        "key_points": [
            "Catching traps the opponent's mid kick under the arm against the ribs - the leg must be trapped, not merely touched, or the kicker pulls free and counters.",
            "It punishes predictable kicking: naked mid kicks without setups get caught, and a caught leg is a lost exchange at minimum.",
            "The sweep is a lever play - hook the standing ankle and pull while driving the upper body - toppling the opponent sideways.",
            "Once caught, the options multiply: sweep, drive forward for the off-balance, or fire the free hand while they hop.",
            "Rule sets allow the sweep and brief advantage but never striking a downed opponent - release cleanly and reset.",
        ],
        "requirements": [
            "A partner throwing controlled mid kicks at increasing speed for catch-timing drills.",
            "Arm and grip strength to clamp the trapped leg - the trap fails if the elbow does not pin down hard.",
            "Mats for sweep practice, since both partners will hit the canvas learning the lever.",
            "Knowledge of the specific rule set's catch-and-sweep allowances and advantage-time limits.",
            "A coach to verify the offline step and the tight trap before any speed is added.",
        ],
        "standards": [
            "Catch-and-sweep mechanics follow the standard kick-catching form taught across kickboxing styles.",
            "Sweep legality follows WAKO, ISKA, and K-1 rules: sweeps are permitted, strikes to downed opponents are fouls.",
            "The brief advantage time after a catch follows the standard referee-break timing of the rule sets.",
        ],
        "citations": [CIT_WAKO, CIT_ISKA, CIT_K1],
        "sig_lens": (
            "The Signature read: the catch is the signature seized "
            "mid-stroke. Where public instruction traps the leg, the "
            "Signature Combat Method sees the opponent's own mark taken "
            "as evidence - held, witnessed, and turned to the takedown. "
            "The clean release is the oath: take the leg, take the "
            "round, never take the foul."
        ),
    },
    {
        "key": "inside_outside_kicks",
        "name": "Inside and Outside Leg Kicks",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Inside and outside leg kicks are the two angles of attack "
            "on the opponent's lead leg, and together they make the low "
            "kick a complete system rather than a single technique. The "
            "outside low kick - the standard one - chops the outer thigh "
            "of the lead leg with the rear leg's shin, swinging in the "
            "familiar roundhouse arc. The inside low kick attacks the "
            "inner thigh of the lead leg, usually with the lead leg's "
            "shin on a shorter, choppier arc - it is faster, harder to "
            "see, and lands on the sensitive inner thigh where even "
            "light contact disrupts stance and balance. The two kicks "
            "complement each other strategically: the outside kick is the "
            "heavy chopper thrown at the end of combinations, while the "
            "inside kick is the quick stab that disrupts rhythm and "
            "punishes weight planted on the lead leg. Defenses differ "
            "too - the outside kick is checked with the lead shin, while "
            "the inside kick is answered by lifting the knee inward or "
            "simply stepping the lead leg back out of range. Fighters who "
            "master both force the opponent to defend the lead leg from "
            "two directions at once, which doubles the defensive burden "
            "and opens the head: every committed leg defense drops a "
            "hand, and the hands are what protect the chin."
        ),
        "how_it_works": (
            "For the outside low kick: step the lead foot slightly out, "
            "pivot the standing foot, and swing the rear shin on the "
            "roundhouse arc into the outer thigh just above the knee, "
            "exactly as drilled for the basic low kick. For the inside "
            "low kick: from stance, lift the lead knee slightly inward "
            "and chop the lead shin down and across into the opponent's "
            "inner thigh on a short, compact arc - the motion is more "
            "stomp than swing, with the hip dropping into it. Keep the "
            "guard up for both; the inside kick especially tempts the "
            "fighter to drop the hands, since it feels safe, but the "
            "counter cross is waiting. Return both kicks to stance "
            "immediately - the inside kick's short arc should have you "
            "home fastest. Drill the pair on the bag: outside kick, "
            "reset, inside kick, reset, ten each per leg, then combine "
            "them - outside-inside as a two-kick combination, which "
            "teaches the rhythm of attacking the leg from both sides in "
            "one exchange."
        ),
        "key_points": [
            "Outside and inside leg kicks attack the lead leg from two directions - the outside kick chops the outer thigh on the roundhouse arc, the inside kick stabs the inner thigh on a short chop.",
            "The outside kick is the heavy combination-ender; the inside kick is the fast rhythm-disruptor that punishes planted weight.",
            "Together they double the opponent's defensive burden - defending the leg from two directions drops hands and opens the head.",
            "Defenses differ: the outside kick is checked with the lead shin, the inside kick is answered by lifting the knee inward or stepping out of range.",
            "The inside kick tempts dropped hands because it feels safe - the counter cross is waiting for exactly that mistake.",
        ],
        "requirements": [
            "A drilled basic low kick first - the outside kick is that technique, and the inside kick builds on its mechanics.",
            "A heavy bag for the chopping arcs from both angles, ten per leg per angle per session.",
            "Guard discipline drills, since the inside kick's safety illusion invites dropped hands.",
            "A partner for two-direction leg-attack sparring at controlled power with shin guards.",
            "A coach to verify the inside kick's compact stomp arc versus the outside kick's full swing.",
        ],
        "standards": [
            "Both kicks follow the standard roundhouse shin-contact mechanics of kickboxing.",
            "The inner and outer thigh above the knee are legal targets under WAKO, ISKA, and K-1 rules.",
            "Shin guards are standard for two-direction leg-kick sparring.",
        ],
        "citations": [CIT_WAKO, CIT_ISKA, CIT_K1],
        "sig_lens": (
            "The Signature read: the two leg kicks are the signature "
            "written on both margins. Where public instruction chops "
            "outside and stabs inside, the Signature Combat Method sees "
            "the page attacked from both edges - the heavy stroke and "
            "the quick mark, until the stance itself cannot hold the "
            "line. Two directions, one oath: the leg will fall."
        ),
    },
    {
        "key": "clinch_pummeling",
        "name": "Clinch Entry and Pummeling",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The clinch is kickboxing's close-quarters grappling: the "
            "fighters tie up chest to chest, fighting for head control, "
            "arm position, and the dominant angle from which knees and "
            "short punches score. Pummeling is the core skill of the "
            "clinch - the continuous battle for inside arm position, "
            "swimming the arms over and under the opponent's arms to win "
            "the double inside tie that controls their posture. Entry to "
            "the clinch must be safe: fighters enter behind punches, "
            "slipping inside the opponent's guard as they punch, or catch "
            "a kick and close the distance - walking straight into the "
            "clinch with the hands down is how fighters eat uppercuts. "
            "Once tied up, the goals are head position (forehead under "
            "their chin, never the reverse), inside control (both arms "
            "inside theirs), and hip position (hips back so their knees "
            "cannot reach, or hips in to throw your own). The clinch is "
            "scored in most rule sets for effective knees and control, "
            "and referees break passive clinches - so the clinch fighter "
            "works constantly, pummeling for position and firing knees. "
            "Defense in the clinch is frames and whizzers: stiff arms "
            "against the shoulders, head position battles, and turning "
            "out when controlled."
        ),
        "how_it_works": (
            "To enter: throw a jab-cross to occupy the opponent's guard, "
            "slip slightly inside as the cross extends, and step deep "
            "with the lead foot to chest-to-chest distance - the punches "
            "are the key that opens the door. Immediately fight for "
            "inside position: swim one arm over their arm and under the "
            "other, alternating in the pummeling rhythm - over, under, "
            "over, under - until both your arms are inside theirs. Get "
            "your forehead under their chin and your hips positioned: "
            "back to defend knees, in to attack with them. From the "
            "dominant tie, pull their head down slightly and fire knees "
            "up the middle. To defend: frame with stiff arms on their "
            "shoulders, keep your head up and your hips back, and pummel "
            "back for inside position - never let both their hands lock "
            "behind your head. Drill pummeling with a partner for "
            "three-minute rounds, no strikes, just the swimming battle "
            "for inside position. Then add controlled knees with a body "
            "protector, trading dominant positions."
        ),
        "key_points": [
            "Pummeling is the continuous swimming battle for double inside arm position - over, under, over, under - which controls the opponent's posture.",
            "Enter the clinch behind punches, slipping inside as they extend - walking in with hands down invites the uppercut.",
            "The dominant clinch has forehead under their chin, both arms inside theirs, and hips positioned for your knees and against theirs.",
            "Referees break passive clinches, so the clinch fighter works constantly - pummeling for position and firing knees.",
            "Clinch defense is frames, head position, and hips back - and never let both opponent hands lock behind your head.",
        ],
        "requirements": [
            "A partner for pummeling rounds and controlled clinch-knee drilling with a body protector.",
            "Neck and upper-back strength for the head-position battle that decides most clinches.",
            "Entry punches drilled first - the clinch entry is only as safe as the punches that cover it.",
            "Mats, since clinch work includes off-balances and occasional throws from the tie.",
            "A coach to referee pummeling rounds and verify inside position is actually won, not assumed.",
        ],
        "standards": [
            "Clinch mechanics follow the standard tie-up and pummeling forms of K-1 and Dutch kickboxing.",
            "Clinch scoring and referee breaks follow WAKO, ISKA, and K-1 competition rules.",
            "The double-inside-tie standard defines the dominant clinch position across styles.",
        ],
        "citations": [CIT_WAKO, CIT_ISKA, CIT_K1],
        "sig_lens": (
            "The Signature read: the clinch is the signature pressed "
            "seal to seal. Where public instruction pummels for "
            "position, the Signature Combat Method sees two names "
            "grappling on the same line - each fighting to write over "
            "the other, forehead to chin, inside to inside. The constant "
            "work is the oath: never passive, never still."
        ),
    },
    {
        "key": "counter_punching",
        "name": "Counter-Punching Fundamentals",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Counter-punching is the art of making the opponent pay for "
            "their own offense: reading an incoming strike, defending "
            "against it, and landing your own strike in the opening their "
            "attack created. Every punch thrown opens a door - the jab "
            "leaves the chin exposed behind the extended arm, the cross "
            "opens the lead side, the hook leaves the center open - and "
            "the counter-puncher's whole game is walking through those "
            "doors. The fundamental counters form a complete system: slip "
            "the jab outside and fire the cross; parry the jab and fire "
            "your own jab; slip the cross and answer with the hook; roll "
            "under the hook and dig the hook to the body; block the "
            "uppercut and answer over the top. Timing beats speed in "
            "counter-punching - the counter lands not because the "
            "counter-puncher is faster, but because the opponent's punch "
            "brings their chin to the counter. Beginners learn counters "
            "as set plays drilled slowly; advanced fighters read and "
            "improvise. The discipline of counter-punching is patience: "
            "the counter-puncher invites the attack, stays calm inside "
            "it, and punishes it - never reaching, never chasing, always "
            "letting the opponent's commitment do half the work."
        ),
        "how_it_works": (
            "Start with the two fundamental set plays at half speed with "
            "a partner. Play one: partner throws a slow jab, you slip "
            "your head three inches to the outside as it passes, and fire "
            "the cross straight down the middle - their extended arm "
            "cannot defend their chin. Play two: partner throws a slow "
            "jab, you parry it offline with the lead glove and fire your "
            "own jab through the opening before their hand returns. The "
            "timing rule: your counter fires as their punch reaches full "
            "extension, not after it returns - you are punching into "
            "their commitment. Keep every counter short and straight; "
            "reaching with counters is the classic counter-puncher's "
            "error. After the counter lands, reset or exit - never admire "
            "it. Drill each set play twenty times per side at half speed, "
            "then build to full speed, then let the partner randomize "
            "which punch they throw so you must read before countering. "
            "Finish every session with the patience drill: two minutes "
            "where you may only counter, never lead - learning to wait "
            "is the counter-puncher's real training."
        ),
        "key_points": [
            "Counter-punching makes the opponent pay for their offense: every punch thrown opens a door, and the counter walks through it.",
            "The fundamental set plays - slip-jab-outside/cross, parry-jab/jab, slip-cross/hook, roll-hook/body-hook - form a complete defensive-offensive system.",
            "Timing beats speed: the counter lands because the opponent's punch brings their chin to it, not because the counter-puncher is faster.",
            "Fire the counter as their punch reaches full extension - punching into their commitment - and keep every counter short and straight.",
            "The discipline is patience: invite the attack, stay calm inside it, never reach, never chase - let their commitment do half the work.",
        ],
        "requirements": [
            "Solid slips, parries, and basic punches first - counter-punching layers defense and offense and needs both.",
            "A partner to feed slow, readable punches that build to full speed and randomization.",
            "Headgear and gloves for counter-sparring once the set plays are reflexive.",
            "The patience drill: rounds where only counters are allowed, training the waiting game.",
            "A coach to verify counter timing - fired into the commitment, not after the return - and to stop reaching.",
        ],
        "standards": [
            "Counter-punching mechanics follow the standard defensive-offensive forms codified across boxing and kickboxing.",
            "Set-play drilling follows the standard progression: slow, fast, randomized, sparring.",
            "The extension-timing standard - counter fired at the opponent's full extension - is the technical mark of the true counter.",
        ],
        "citations": [CIT_DEMPSEY, CIT_HATMAKER],
        "sig_lens": (
            "The Signature read: the counter is the signature answering "
            "itself. Where public instruction reads and punishes, the "
            "Signature Combat Method sees the page turning the pen - the "
            "opponent writes the opening, and the counter signs it. "
            "Patience is the oath: wait for the true stroke, then write "
            "once and clean."
        ),
    },
    {
        "key": "dutch_combinations",
        "name": "Dutch-Style Combination Striking",
        "group": "Advanced",
        "ladder_rank": 7,
        "ladder_tier": "advanced",
        "description": (
            "Dutch-style combination striking is the punching-heavy "
            "kickboxing system developed in the Netherlands: long, "
            "relentless boxing combinations finished with a single "
            "devastating low kick or mid kick - the famous pattern of "
            "punches that ends with the leg. Where other styles throw "
            "kicks as isolated weapons, the Dutch system treats the "
            "combination as the weapon: four to six punches flow in "
            "rhythm, the opponent shells to survive the hands, and the "
            "low kick chops the leg at the exact moment the guard is "
            "highest. The system's hallmarks are volume, pressure, and "
            "the low kick as punctuation - jab, cross, hook, cross, low "
            "kick; or hook to the body, hook to the head, low kick. "
            "Dutch fighters train combinations as memorized sequences "
            "drilled thousands of times, so under fire the hands flow "
            "without thought and only the finish - which kick, which "
            "target - is chosen live. The style demands exceptional "
            "conditioning, because six-punch-plus-kick combinations "
            "thrown repeatedly for three-minute rounds empty the gas "
            "tank of the unprepared. Defensively the Dutch fighter "
            "accepts some incoming fire behind a high guard, trusting "
            "volume and pressure to break the opponent first. This "
            "record teaches the system's core combinations, its rhythm, "
            "and the low-kick finish that defines it."
        ),
        "how_it_works": (
            "Memorize the three core Dutch combinations before adding "
            "speed. Combination one: jab, cross, lead hook, cross, rear "
            "low kick - throw the four punches in a one-two-three-four "
            "rhythm with full hip rotation on each, then pivot and chop "
            "the low kick as the hands return. Combination two: lead "
            "hook to the body, lead hook to the head, rear low kick - "
            "the level change drops the guard, the head hook lifts it, "
            "the kick takes the leg. Combination three: jab, cross, "
            "teep to the body - the push kick creates distance after the "
            "hands. Drill each combination slowly ten times per session "
            "for perfect form, then at speed on the bag in thirty-second "
            "bursts, counting clean completions. The rules of the "
            "system: never throw the combination without the kick "
            "finish in training, keep the guard high through the "
            "punches since you accept some return fire, and step the "
            "lead foot out before every finishing kick. Spar the "
            "combinations at half power first - the rhythm must survive "
            "contact before it survives a fight."
        ),
        "key_points": [
            "Dutch style is punching-heavy: long relentless boxing combinations finished with a single devastating low or mid kick - punches as the weapon, the kick as punctuation.",
            "The system exploits guard mechanics: four to six punches force the shell high, and the low kick chops the leg at the exact moment the guard is highest.",
            "Combinations are memorized sequences drilled thousands of times - hands flow without thought, only the finishing kick is chosen live.",
            "It demands exceptional conditioning: six-punch-plus-kick combinations across three-minute rounds empty unprepared gas tanks.",
            "Defensively the Dutch fighter accepts some return fire behind a high guard, trusting volume and pressure to break the opponent first.",
        ],
        "requirements": [
            "Drilled jab, cross, hooks, and low kick individually - the system layers them and needs every part clean.",
            "A heavy bag for thirty-second combination bursts and a partner with mitts for the punch-to-kick transitions.",
            "Elite-level conditioning: roadwork, intervals, and round-based bag work to sustain combination volume.",
            "Sparring progression from half power to full, since the rhythm must survive contact.",
            "A coach steeped in the Dutch system to correct the combination rhythm and the kick-finish timing.",
        ],
        "standards": [
            "Dutch-style combination structure follows the punch-volume-plus-kick-finish form of the Netherlands kickboxing schools.",
            "All techniques used are legal under K-1 rules, the rule set where the Dutch style proved itself.",
            "Combination drilling follows the standard progression: slow memorization, bag speed, controlled sparring.",
        ],
        "citations": [CIT_K1, CIT_WAKO, CIT_ROONEY],
        "sig_lens": (
            "The Signature read: the Dutch system is the signature in "
            "full flood. Where public instruction chains punches to "
            "kicks, the Signature Combat Method sees the name written "
            "fast and finished with the heavy seal - volume as the "
            "hand, the low kick as the press. The memorized rhythm is "
            "the oath: drill it until the body signs without thinking."
        ),
    },
    {
        "key": "switch_kick",
        "name": "The Switch Kick",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The switch kick is the deceptive roundhouse: the fighter "
            "switches stance mid-motion - rear foot jumping forward as "
            "the lead foot jumps back - and fires the new rear leg as a "
            "full-power roundhouse. It solves the lead leg's eternal "
            "problem: the lead leg is fast but weak, the rear leg is "
            "powerful but slow to chamber. The switch borrows the rear "
            "leg's power for a lead-side attack, delivering a rear-leg "
            "roundhouse from the lead side in a fraction of the time a "
            "step would take. The deception is the point: the opponent "
            "reads the small hop as a stance adjustment, and the kick is "
            "already chambered before they recognize the threat. The "
            "switch kick targets the body, head, or lead leg, and it is "
            "especially effective against opponents who over-commit to "
            "defending the standard rear-leg kick. Its risk is the hop "
            "itself - for a beat the fighter is airborne and "
            "unbalanced, and a well-timed counter during the switch "
            "lands on a defenseless target. Fighters drill the switch "
            "until the hop is tiny and the kick fires as one motion, "
            "because a big, slow switch is just an invitation."
        ),
        "how_it_works": (
            "From stance, perform the switch: hop both feet "
            "simultaneously, the rear foot landing where the lead foot "
            "was and the lead foot landing back - a quick, low, quiet "
            "exchange, no higher than an inch off the ground. The instant "
            "the new stance lands, the new rear leg (your original lead "
            "leg) chambers and fires the roundhouse: pivot the standing "
            "foot, turn the hip fully over, and whip the shin into the "
            "target. The whole sequence - hop, chamber, kick - must flow "
            "as one beat with no pause between the landing and the "
            "chamber. Keep the guard up through the hop; the hands do "
            "not drop during the switch. Aim the switch kick at the body "
            "or head, where the surprise angle pays most. Drill the hop "
            "alone first: fifty tiny switches in stance, keeping the "
            "guard and landing balanced every time. Then add the kick: "
            "switch and fire at the bag, ten per side, checking that the "
            "hop stays low and the kick chambers instantly on landing."
        ),
        "key_points": [
            "The switch kick borrows the rear leg's power for a lead-side attack: hop the stance, fire the new rear leg as a full roundhouse.",
            "It solves the lead leg's dilemma - fast but weak - by delivering rear-leg power from the lead side in a fraction of a step's time.",
            "The deception is the point: the hop reads as a stance adjustment, and the kick is chambered before the threat registers.",
            "It punishes opponents who over-commit to defending the standard rear-leg kick.",
            "The hop is the risk: airborne and unbalanced for a beat, so drill it tiny, low, and instant - a big slow switch is an invitation.",
        ],
        "requirements": [
            "A drilled rear-leg roundhouse first - the switch kick is that kick fired from a switched stance.",
            "Open floor for fifty-repetition switch-hop drills keeping the guard up and every landing balanced.",
            "A heavy bag for switch-and-fire timing and a partner for reading whether the hop telegraphs.",
            "Calf and ankle conditioning for the constant small hops without fatigue.",
            "A coach to shrink the hop - beginners always switch too big, which kills the deception.",
        ],
        "standards": [
            "Switch-kick mechanics follow the standard stance-switch roundhouse form taught across K-1 and Dutch kickboxing.",
            "The one-beat hop-to-chamber timing is the technical standard for the kick's deceptive value.",
            "Targets follow the legal kick zones under WAKO, ISKA, and K-1 rules.",
        ],
        "citations": [CIT_K1, CIT_WAKO, CIT_ISKA],
        "sig_lens": (
            "The Signature read: the switch kick is the signature "
            "rewritten mid-stroke. Where public instruction hops and "
            "fires, the Signature Combat Method sees the hand changing "
            "grip without lifting the pen - same name, new angle, the "
            "power borrowed and returned before the page notices. Tiny "
            "and true is the oath: the smaller the hop, the truer the "
            "deception."
        ),
    },
    {
        "key": "spinning_back_kick",
        "name": "The Spinning Back Kick",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The spinning back kick is the most powerful kick in "
            "kickboxing: the fighter turns fully away from the "
            "opponent, chambers the rear leg, and drives the heel "
            "straight back into the midsection or head with the entire "
            "rotational force of the spin behind it. Fighters have ended "
            "championship bouts with a single spinning back kick because "
            "no guard fully absorbs a heel driven by a full-speed "
            "one-hundred-eighty-degree rotation. The mechanics are a "
            "controlled spin: step the lead foot across, turn the "
            "shoulders and head to spot the target over the shoulder, "
            "chamber the rear knee tight to the chest, and extend the "
            "leg straight back, striking with the heel. The head must "
            "spot the target throughout the turn - the classic beginner "
            "error is spinning blind, which produces a wild, off-target "
            "kick and leaves the back exposed. Its great weakness is "
            "commitment: a missed spinning kick leaves the fighter "
            "turned away and open for a full second, so it is thrown as "
            "a counter when the opponent rushes in, or as a surprise "
            "after a combination has them shelling. Fighters drill it "
            "thousands of times on the bag before throwing it live, "
            "because the spin must be automatic before it is safe."
        ),
        "how_it_works": (
            "From stance, step the lead foot across the body about a "
            "foot to start the turn. Pivot on the ball of the lead foot "
            "and turn the shoulders away from the opponent, whipping the "
            "head around to spot the target over the shoulder - eyes "
            "find the target before the leg fires. Chamber the rear knee "
            "tight to the chest as the turn completes. Extend the leg "
            "straight back explosively, driving the heel into the "
            "midsection, and lean the torso forward slightly away from "
            "the kick for counterbalance and reach. Strike with the heel, "
            "never the sole or toes. Retract the leg fast and continue "
            "the turn to face the opponent again, hands up - the spin "
            "does not end until the guard is re-established. Drill the "
            "turn-and-spot without the kick first: twenty slow spins "
            "checking that the eyes find the target every time. Then "
            "add the kick on the bag: ten per side at half power "
            "focusing on the spot and the heel, building to full power "
            "only when the spin is automatic."
        ),
        "key_points": [
            "The spinning back kick is the most powerful kick in the sport: full one-hundred-eighty-degree rotation driving the heel straight back.",
            "Championship bouts have ended on a single one - no guard fully absorbs a heel backed by a full-speed spin.",
            "The head must spot the target over the shoulder throughout the turn; spinning blind is the classic beginner error.",
            "Its weakness is commitment: a miss leaves the fighter turned away and open for a full second.",
            "Throw it as a counter to a rushing opponent or as a surprise after shelling combinations - never as a naked lead technique.",
        ],
        "requirements": [
            "Thousands of bag repetitions before live use - the spin must be automatic before it is safe.",
            "A heavy bag that can take full rotational heel power and a large drilling space for the turn.",
            "Spotting discipline drilled first: twenty slow turn-and-spot repetitions with eyes finding the target every time.",
            "Core and hip rotational power, plus the balance to retract and re-face instantly after the kick.",
            "A coach to verify the spot, the heel contact, and the guard re-establishment that ends the technique.",
        ],
        "standards": [
            "Spinning back kick mechanics follow the standard turning-kick form taught across kickboxing styles.",
            "Heel contact is the technical standard; the midsection is the primary legal target under all major rule sets.",
            "The spot-the-target requirement follows the universal turning-technique safety standard.",
        ],
        "citations": [CIT_WAKO, CIT_ISKA, CIT_K1],
        "sig_lens": (
            "The Signature read: the spinning back kick is the signature "
            "written with the whole arm. Where public instruction turns "
            "and drives the heel, the Signature Combat Method sees the "
            "grandest stroke - the full turn, the spotted target, the "
            "heel as the period. Never blind is the oath: the eyes "
            "swear the target before the body signs."
        ),
    },
    {
        "key": "flying_knee",
        "name": "The Flying Knee",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The flying knee is kickboxing's most spectacular technique: "
            "the fighter launches off the ground, drives one knee upward "
            "into the opponent's head or body while airborne, and lands "
            "back in stance. It is a fight-ending weapon when it lands "
            "clean - the combined force of the jump, the hip drive, and "
            "the falling body weight behind the hard point of the knee "
            "has produced some of the sport's most famous knockouts. "
            "The mechanics are a sprint-step into a jump: two quick "
            "steps build momentum, the fighter springs off the lead leg, "
            "drives the rear knee up and through the target while "
            "pulling the opponent's head down with the hands if in "
            "range, and lands on the kicking foot flowing back into "
            "stance. Its setup is everything - the flying knee thrown "
            "from distance without a setup is easily sidestepped, leaving "
            "the fighter landing off balance in front of a fresh "
            "opponent. Fighters set it up behind combinations that have "
            "the opponent shelling and stationary, or as a counter when "
            "the opponent ducks into the knee's path. Because both feet "
            "leave the ground, the flying knee is the highest-commitment "
            "technique in the sport, drilled on crash mats and bags long "
            "before it is thrown at a live opponent."
        ),
        "how_it_works": (
            "Set it up first: throw a combination that has the opponent "
            "shelling and stationary - the flying knee needs a "
            "non-moving target. Take two quick driving steps toward the "
            "opponent, then spring off the lead leg, jumping upward and "
            "forward. As you leave the ground, drive the rear knee up "
            "and through the target - chin or solar plexus - thrusting "
            "the hips violently at the top of the jump. If in range, "
            "the hands pull the opponent's head down into the rising "
            "knee. Keep the non-kicking leg tucked for balance and the "
            "guard arm up. Land on the kicking foot first, absorbing "
            "with a bent knee, and flow immediately back into stance or "
            "into a follow-up combination - never land admiring the "
            "jump. Drill the jump-and-drive on a heavy bag laid on crash "
            "mats: ten per side at half height focusing on the hip "
            "thrust at the apex, building to full height only when the "
            "landing is consistently balanced. Practice the two-step "
            "setup separately until the entry is explosive."
        ),
        "key_points": [
            "The flying knee launches the fighter airborne, driving the knee up into head or body with jump force, hip drive, and body weight combined.",
            "Landed clean it is a fight-ender - the sport's most famous knockouts include flying knees.",
            "Setup is everything: it needs a shelling, stationary target built by combinations, or an opponent ducking into its path.",
            "Thrown naked from distance it is easily sidestepped, leaving the fighter landing off balance in front of a fresh opponent.",
            "It is the highest-commitment technique in the sport - both feet leave the ground - drilled on mats and bags long before live use.",
        ],
        "requirements": [
            "Crash mats and a heavy bag for jump-and-drive drilling before any partner work.",
            "Explosive leg power from plyometric training - the jump must be high enough to reach the target.",
            "Setup combinations drilled first, since the flying knee without a setup is a low-percentage gamble.",
            "Landing mechanics: absorb on a bent knee and flow back to stance, drilled until automatic.",
            "A coach to verify the hip thrust at the apex and the balanced landing on every repetition.",
        ],
        "standards": [
            "Flying knee mechanics follow the standard jumping-knee form of K-1 and Dutch kickboxing.",
            "Knee targets follow the rule set: head and body knees legal under K-1 rules, restricted under some American rules.",
            "Mat-based progression follows the standard high-commitment technique safety protocol.",
        ],
        "citations": [CIT_K1, CIT_WAKO, CIT_ROONEY],
        "sig_lens": (
            "The Signature read: the flying knee is the signature leaping "
            "off the page. Where public instruction jumps and drives, "
            "the Signature Combat Method sees the boldest stroke - the "
            "body leaving the ground to sign from above, the knee the "
            "exclamation. Setup first is the oath: never leap without "
            "the sentence that earns it."
        ),
    },
    {
        "key": "shin_conditioning",
        "name": "Shin and Body Conditioning",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Shin and body conditioning is the long, unglamorous process "
            "that makes kickboxing's weapons usable: the gradual "
            "hardening of the shins, and the toughening of the torso "
            "against body shots, through months and years of progressive "
            "impact. The science is straightforward - bone and connective "
            "tissue adapt to repeated sub-injury stress by growing denser "
            "(Wolff's law for bone), and the nervous system learns to "
            "tolerate impact that once caused flinching. The method is "
            "equally straightforward and absolutely non-negotiable: start "
            "with light, high-volume contact on the heavy bag, increase "
            "power gradually over months, never train through sharp pain "
            "or swelling, and let rest days do the actual hardening. "
            "Fighters kick the heavy bag hundreds of times per session, "
            "take controlled body shots from partners and medicine balls "
            "to condition the torso, and roll a hard stick lightly along "
            "the shins in some traditions - always stopping well short "
            "of injury. What conditioning is not: it is not kicking "
            "trees, breaking bottles on the shins, or any macho shortcut, "
            "all of which cause microfractures and nerve damage that end "
            "careers. The conditioned fighter's reward is the freedom to "
            "throw full-power kicks in a fight without fear, and to check "
            "kicks with a shin the opponent will regret meeting."
        ),
        "how_it_works": (
            "Begin with the heavy bag at half power: one hundred light "
            "low kicks per leg per session, three sessions per week, "
            "focusing on clean shin contact. Each week add roughly ten "
            "percent more power or volume - never both at once. If sharp "
            "pain or visible swelling appears, drop back to the previous "
            "week's load and add an extra rest day; dull aching that "
            "fades within a day is normal adaptation. After two months, "
            "add partner body-conditioning: the partner taps the torso "
            "with light punches and kicks while you brace and breathe "
            "out, ten minutes per session, building force gradually over "
            "further months. Ice the shins after heavy sessions and "
            "never condition two days in a row - the hardening happens "
            "during rest, not during impact. Keep a simple log: date, "
            "kicks per leg, power level, pain notes. Review monthly: "
            "steady upward load with only dull, fading soreness means "
            "the program is working. Any numbness, persistent swelling, "
            "or pain that worsens across sessions means stop and see a "
            "sports-medicine professional."
        ),
        "key_points": [
            "Conditioning hardens shins and torso through months of progressive sub-injury impact - bone densifies under repeated stress and the nervous system learns tolerance.",
            "The method is non-negotiable: light high-volume bag work, ten percent weekly load increases, never through sharp pain or swelling, rest days doing the hardening.",
            "It is not kicking trees or breaking bottles on the shins - macho shortcuts cause microfractures and nerve damage that end careers.",
            "Body conditioning uses controlled partner contact and medicine-ball work with braced exhaling, built over months like the shins.",
            "Keep a training log and watch the signals: dull fading soreness is adaptation, while numbness or worsening pain means stop and see a professional.",
        ],
        "requirements": [
            "A heavy bag and a multi-month horizon - conditioning cannot be rushed without injury.",
            "A training log recording kicks, power level, and pain notes for monthly review.",
            "Ice and rest days scheduled as strictly as training days, since adaptation happens during recovery.",
            "A partner for gradual body-conditioning contact and a coach to enforce the ten-percent progression rule.",
            "Access to a sports-medicine professional if warning signs appear: numbness, persistent swelling, or worsening pain.",
        ],
        "standards": [
            "Progressive overload follows the standard ten-percent weekly load-increase guideline of conditioning science.",
            "Bone adaptation follows Wolff's law: bone remodels denser under repeated mechanical stress within safe limits.",
            "The stop-on-warning-signs standard follows standard sports-medicine practice for impact conditioning.",
        ],
        "citations": [CIT_ROONEY, CIT_BOMPA],
        "sig_lens": (
            "The Signature read: conditioning is the signature practiced "
            "until the hand cannot cramp. Where public instruction "
            "hardens bone by degrees, the Signature Combat Method sees "
            "the oath kept daily - the same strokes, the same page, "
            "months deep, until the body signs without flinching. "
            "Patience is the entire oath: never rush what only time "
            "can write."
        ),
    },
    {
        "key": "feints_setups",
        "name": "Feints and Setups",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Feints and setups are the deception layer of kickboxing: "
            "the false movements that make the opponent react to "
            "strikes that never come, opening the real strikes that "
            "follow. A feint is a half-thrown technique - the shoulder "
            "twitch of an unthrown jab, the hip turn of an unthrown "
            "kick, the level drop of an unthrown body shot - performed "
            "convincingly enough that the opponent's defense answers "
            "it. When the guard jumps at the ghost, the real strike "
            "travels through the hole the reaction opened. Setups are "
            "the longer game: patterns deliberately established - three "
            "rounds of jab-cross-low-kick, say - and then broken at the "
            "decisive moment, so the opponent's conditioned response "
            "becomes the trap. The great feinters barely move: a "
            "two-inch shoulder roll draws the parry that opens the "
            "cross; a glance at the body drops the elbows for the head "
            "kick. Beginners feint too big, telegraphing theater "
            "instead of deception; advanced fighters feint with the "
            "same muscles as the real strike, differing only in the "
            "final commitment. Feinting is drilled like everything "
            "else: feint-jab to draw the parry, then cross; feint the "
            "low kick to lift the check, then kick the body; establish "
            "the pattern, then break it when it matters."
        ),
        "how_it_works": (
            "Master the three fundamental feints slowly with a partner. "
            "Feint one: twitch the lead shoulder and hand forward two "
            "inches as if starting the jab - when the partner's glove "
            "moves to parry, fire the real cross through the opening. "
            "Feint two: turn the hip as if starting the low kick - when "
            "the partner lifts the check, drive the mid kick into the "
            "now-open body. Feint three: drop the level two inches as if "
            "going to the body - when the elbows drop, throw the head "
            "kick or the overhand. The rule of every feint: use the same "
            "muscles and the same first two inches as the real "
            "technique - the deception must be indistinguishable until "
            "the commitment point. Drill feint-then-strike as pairs, ten "
            "each, then spar with a feint quota: every exchange must "
            "begin with a feint, training the habit of never leading "
            "naked. For setups, pick one combination and throw it five "
            "times in sparring to establish the pattern, then on the "
            "sixth, break it - feint the expected finish and throw the "
            "opposite. Record which breaks land; the log teaches your "
            "personal best traps."
        ),
        "key_points": [
            "Feints are half-thrown techniques - shoulder twitch, hip turn, level drop - convincing enough that the opponent's defense answers the ghost.",
            "When the guard jumps at the feint, the real strike travels through the hole the reaction opened.",
            "Setups are the longer game: establish a pattern deliberately, then break it at the decisive moment so the conditioned response becomes the trap.",
            "Great feinters barely move - the feint uses the same muscles and first two inches as the real strike, differing only in final commitment.",
            "Beginners feint too big; the fix is drilling feint-then-strike pairs until the false and true are indistinguishable.",
        ],
        "requirements": [
            "Reliable fundamental strikes first - a feint of a punch you cannot throw is just a twitch.",
            "A partner for feint-reaction drills, calling out when the feint reads true versus theatrical.",
            "Sparring with a feint quota to build the habit of never leading an exchange naked.",
            "A log of setup breaks that land, building a personal playbook of best traps.",
            "A coach to shrink beginner feints from theater to the two-inch truth.",
        ],
        "standards": [
            "Feint mechanics follow the standard deception principles taught across striking arts: same initiation, withheld commitment.",
            "The feint-then-strike pair follows the standard combination-timing rules of the sport.",
            "Setup pattern-breaking follows the standard tactical progression of establishing before exploiting.",
        ],
        "citations": [CIT_HATMAKER, CIT_DEMPSEY],
        "sig_lens": (
            "The Signature read: the feint is the signature's ghost "
            "stroke. Where public instruction deceives with half "
            "motions, the Signature Combat Method sees the pen hovering "
            "- the page bracing for a mark that never lands, until the "
            "true stroke falls where the guard abandoned. Two inches of "
            "truth is the oath: never theater, only the real beginning "
            "withheld."
        ),
    },
    {
        "key": "ring_cutting",
        "name": "Ring Cutting and Angle Work",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Ring cutting and angle work are the geometry of control: "
            "how the fighter traps a mobile opponent and how the "
            "fighter creates punching angles the opponent cannot "
            "defend. Ring cutting solves the mover's puzzle - the "
            "opponent who circles away endlessly cannot be caught by "
            "chasing, because the chaser always travels farther. The "
            "cutter instead steps laterally to intercept the circle, "
            "placing the body where the opponent wants to go and "
            "shrinking the ring one cut at a time until the ropes or "
            "corner do the trapping. Angle work is the offensive twin: "
            "instead of attacking straight down the middle where the "
            "guard is strongest, the fighter pivots forty-five degrees "
            "and attacks from the side, where the opponent's guard must "
            "turn to meet it - and a turning guard is an opening guard. "
            "The pivot-jab, the step-around cross, the angle-change "
            "after every combination: these are the tools that make a "
            "fighter dangerous from positions the opponent never "
            "prepared for. Both skills share one law: never follow, "
            "always intercept - whether intercepting the opponent's "
            "movement around the ring or intercepting their guard's "
            "orientation with a new angle."
        ),
        "how_it_works": (
            "For ring cutting: when the opponent circles left, do not "
            "chase - step your lead foot laterally to your right, "
            "cutting across their circle to the spot they are moving "
            "toward. Keep the guard up and take small, balanced steps; "
            "the goal is to arrive where they are going, not where they "
            "are. Each cut should shrink their space by about a third - "
            "three good cuts put most movers on the ropes. Once they "
            "are near the ropes, feint one direction and attack as they "
            "try to escape the other way. For angle work: after any "
            "combination, pivot forty-five degrees on the lead foot and "
            "fire the next punch from the new angle before the opponent's "
            "guard re-orients - the classic is jab-cross, pivot left, "
            "lead hook from the side. Drill cutting with a partner "
            " circling the ring: your only job for three minutes is to "
            "keep them off the center, no strikes. Then drill the "
            "pivot-and-attack: combination, pivot, punch from the angle, "
            "ten per side. The checkpoint: after every pivot you should "
            "see the side of their guard, not its front."
        ),
        "key_points": [
            "Ring cutting traps movers by interception, not chasing - step laterally to where the opponent is going and shrink the ring one cut at a time.",
            "Three good cuts put most movers on the ropes; then feint one escape direction and attack the other.",
            "Angle work attacks from forty-five degrees off center, where the guard must turn to meet it - and a turning guard is an opening guard.",
            "The pivot-after-combination is the core angle tool: strike, pivot, strike again before the guard re-orients.",
            "Both skills share one law: never follow, always intercept - the movement or the guard's orientation.",
        ],
        "requirements": [
            "A full-size ring or large matted area for cutting drills - the geometry needs real space.",
            "A mobile partner willing to circle for three-minute cutting rounds while you practice interception without strikes.",
            "Pivot footwork drilled to automaticity, since every angle depends on the forty-five-degree pivot.",
            "Combination fundamentals, because angles are created after combinations, not instead of them.",
            "A coach to verify the cuts actually shrink space - beginners cut too shallow and chase in disguise.",
        ],
        "standards": [
            "Ring-cutting footwork follows the standard lateral-interception form taught across boxing and kickboxing.",
            "The forty-five-degree pivot is the standard angle-change unit of the sport.",
            "Rope and corner trapping follows the standard positional-scoring principles of competition judging.",
        ],
        "citations": [CIT_DEMPSEY, CIT_HATMAKER, CIT_WAKO],
        "sig_lens": (
            "The Signature read: ring craft is the signature controlling "
            "the page. Where public instruction cuts and pivots, the "
            "Signature Combat Method sees the writer owning the margins "
            "- no chasing the words, only placing the pen where the "
            "line must go. Intercept, never follow, is the oath: the "
            "page belongs to the one who positions first."
        ),
    },
    {
        "key": "advanced_defense",
        "name": "Advanced Defense: Shoulder Roll and Pull Counter",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "The shoulder roll and the pull counter are the signature "
            "defenses of the advanced counter-puncher: techniques that "
            "turn the opponent's best punch into your best opening. The "
            "shoulder roll meets the straight punch not with the gloves "
            "but with the raised lead shoulder - the fighter turns "
            "slightly sideways, tucks the chin behind the shoulder, and "
            "lets the punch glance off the deltoid while the rear hand "
            "sits ready to fire the counter cross over the top. The pull "
            "counter is even more audacious: as the opponent's jab or "
            "cross extends, the fighter leans the upper body back just "
            "out of range - pulling the head back like a matador - and "
            "fires the rear-hand counter over the falling punch. Both "
            "techniques demand supreme confidence in distance and "
            "timing, because the margin between a brilliant pull and a "
            "knockout is two inches. They are high-level tools with "
            "high-level risks: the shoulder roll invites the hook to "
            "the unguarded side, and the pull counter fails catastrophically "
            "against a feinted punch. Fighters add them only after the "
            "fundamental defenses are reflexive, and they drill them "
            "first against slow, predictable punches for months before "
            "trusting them at speed."
        ),
        "how_it_works": (
            "For the shoulder roll: from stance, as the opponent's "
            "straight punch comes, turn the torso slightly more sideways "
            "and lift the lead shoulder high, tucking the chin tight "
            "behind it. Let the punch glance off the shoulder and upper "
            "arm - do not reach for it with the gloves. Keep the rear "
            "hand cocked at the chin throughout. The instant the punch "
            "deflects, roll the shoulder back down and fire the rear "
            "cross over the top of their extended arm. For the pull "
            "counter: as their jab extends, shift your weight to the rear "
            "foot and lean the head and shoulders back three to four "
            "inches - just enough for the punch to fall short. Keep the "
            "eyes on them and the feet planted. As their punch reaches "
            "full extension and falls short, drive off the rear foot and "
            "fire your own cross or overhand over their extended arm. "
            "Drill both at quarter speed with a partner for ten minutes "
            "before any speed: the timing window is everything, and the "
            "window is learned slow. Never attempt the pull against an "
            "opponent who feints - the lean-back against a feint is a "
            "knockout setup."
        ),
        "key_points": [
            "The shoulder roll meets the straight punch with the raised lead shoulder, chin tucked behind it, rear hand cocked for the over-the-top counter.",
            "The pull counter leans the head back inches out of range like a matador and fires the rear hand over the falling punch.",
            "Both demand supreme distance and timing confidence - the margin between a brilliant pull and a knockout is two inches.",
            "Both carry high-level risks: the roll invites the hook to the open side, the pull fails catastrophically against a feinted punch.",
            "Add them only after fundamental defenses are reflexive, and drill them slow for months before trusting them at speed.",
        ],
        "requirements": [
            "Reflexive fundamental defenses first - these are layer-two tools, never beginner techniques.",
            "A patient partner to throw slow, predictable straight punches for months of timing work.",
            "Headgear for pull-counter sparring once speed increases, since the margin for error is inches.",
            "Neck strength for the shoulder roll's tucked-chin structure under impact.",
            "A coach to forbid the pull against feinters and to verify the lean stays within the three-to-four-inch safety margin.",
        ],
        "standards": [
            "Shoulder roll mechanics follow the classic form refined in championship boxing and adopted into kickboxing.",
            "The pull counter follows the standard matador-timing principles of advanced counter-punching.",
            "Both are thrown only within legal defensive conduct - no holding, no excessive leaning fouls.",
        ],
        "citations": [CIT_DEMPSEY, CIT_HATMAKER],
        "sig_lens": (
            "The Signature read: these defenses are the signature "
            "answering in its own hand. Where public instruction rolls "
            "and pulls, the Signature Combat Method sees the master "
            "stroke of the counter-scribe - the punch declined with a "
            "shoulder, the miss authored into a hit. Two inches is the "
            "oath: confidence measured, never guessed."
        ),
    },
    {
        "key": "sparring_strategy",
        "name": "Sparring Strategy and Round Management",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Sparring strategy and round management are the thinking "
            "layer of kickboxing: how the fighter spends energy, gathers "
            "information, and wins rounds rather than just exchanges. "
            "The strategic sparring session has a plan before the bell - "
            "this round I establish the jab, this round I test their low "
            "kick defense, this round I work the body - because random "
            "sparring builds random habits. Round management in "
            "competition extends the same thinking across the fight: the "
            "early rounds gather reads (which hand drops, which kick "
            "they check, which way they circle), the middle rounds "
            "exploit the reads with set traps, and the championship "
            "rounds spend whatever the gas tank holds. Energy budgeting "
            "is the core skill: the fighter who throws everything in "
            "round one has nothing in round three, while the fighter who "
            "paces pressure breaks opponents late. Judges score clean "
            "effective striking, aggression, and ring control - so the "
            "strategic fighter makes every round tell a story the judges "
            "can read: effective strikes landed, the opponent moved "
            "backward, the ring owned. Between rounds, the corner gives "
            "one adjustment, not ten - the fighter who tries to fix "
            "everything fixes nothing."
        ),
        "how_it_works": (
            "Plan every sparring session in writing before it starts: "
            "three specific goals, such as establish the jab, test their "
            "check, work the body when they shell. Spar the first round "
            "at seventy percent, focusing only on reads - note which "
            "hand drops when they kick, which way they circle under "
            "pressure, whether they check or catch. In round two, run "
            "one set trap based on a read: if they drop the right hand "
            "when kicking, time the cross over their kick. Manage energy "
            "by breathing out sharply on every strike and relaxing the "
            "shoulders between exchanges - tension is the great gas-tank "
            "thief. In the final round, increase pressure deliberately: "
            "this is the trained finish, spending the budgeted reserve. "
            "Between rounds, pick the single biggest adjustment and "
            "verbalize it: 'their check is late - double up the low "
            "kick.' After sparring, log three things: what worked, what "
            "got you hit, and one adjustment for next time. Review the "
            "log weekly; patterns across sessions are your strategic "
            "profile, strengths to sharpen and holes to close."
        ),
        "key_points": [
            "Strategic sparring has a written plan - establish, test, exploit - because random sparring builds random habits.",
            "Early rounds gather reads (dropped hands, check habits, circle direction); middle rounds spring set traps; late rounds spend the budgeted reserve.",
            "Energy budgeting is the core skill: pace pressure across rounds rather than emptying the tank in round one.",
            "Make every round tell the judges a story: clean effective strikes, the opponent moved backward, the ring owned.",
            "Between rounds, one adjustment, not ten - and log every session's lessons, because patterns across sessions are your strategic profile.",
        ],
        "requirements": [
            "A training log for session plans and post-sparring reviews - strategy without records is just intention.",
            "Sparring partners of varied styles to build a library of reads and traps.",
            "A corner voice (coach or senior partner) giving single adjustments between rounds.",
            "Conditioning sufficient to execute a late-round pressure plan - strategy fails without the gas tank behind it.",
            "Knowledge of the judging criteria for the rule set, since winning rounds is the actual objective.",
        ],
        "standards": [
            "Round management follows the standard read-then-exploit progression of competitive striking.",
            "Judging criteria follow WAKO, ISKA, and K-1 scoring: clean effective striking, aggression, and ring control.",
            "The single-adjustment corner standard follows professional corner practice.",
        ],
        "citations": [CIT_WAKO, CIT_ISKA, CIT_K1, CIT_BOMPA],
        "sig_lens": (
            "The Signature read: strategy is the signature planned "
            "before the pen moves. Where public instruction budgets "
            "energy and reads opponents, the Signature Combat Method "
            "sees the composition - the early strokes gathering, the "
            "middle strokes trapping, the final strokes spending all. "
            "One adjustment is the oath: the wise correct a single "
            "line, never rewrite the page mid-round."
        ),
    },
    {
        "key": "southpaw_orthodox",
        "name": "Southpaw Versus Orthodox Game Planning",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Southpaw versus orthodox - the open-stance matchup - is "
            "kickboxing's great tactical puzzle, because mirrored "
            "stances change every angle, every safe zone, and every "
            "best weapon. When both fighters share a stance (closed "
            "stance), the lead hands and lead legs fence in familiar "
            "territory; when stances mirror, the lead hands collide, "
            "the power sides line up, and the battle becomes a fight "
            "for the outside angle - the fighter whose lead foot is "
            "outside the opponent's lead foot controls the angle and "
            "lines up the rear cross and rear kick down the open lane. "
            "The southpaw's classic weapons are the rear cross down the "
            "middle, the lead hook around the orthodox guard, and the "
            "rear low kick to the orthodox lead leg; the orthodox "
            "fighter answers with the same mirrored tools plus the "
            "lead-leg inside kick that punishes the southpaw's stance. "
            "Both sides battle for lead-foot dominance with small "
            "lateral steps, and both must solve the head-clash and "
            "lead-hand tangle that the mirrored guards create. Game "
            "planning for the open stance starts with foot position, "
            "builds through the three money weapons (rear straight, "
            "lead hook, rear kick to the lead leg), and includes "
            "specific counters for the opponent's mirrored answers. "
            "Fighters drill the open stance as its own discipline, "
            "because instincts trained in closed stance actively "
            "misfire when the mirror appears."
        ),
        "how_it_works": (
            "Establish the battle for the outside angle first: from "
            "stance, take small lateral steps to place your lead foot "
            "outside their lead foot - when your foot is outside, your "
            "rear cross and rear kick travel down the open lane while "
            "theirs must cross your guard. Drill the foot battle alone "
            "with a partner for two-minute rounds: no strikes, just the "
            "lateral dance for outside position. Add the three money "
            "weapons in order: rear cross down the middle as they step "
            "in, lead hook around their guard when they shell, rear low "
            "kick to their lead leg when they plant. Defensively, keep "
            "the lead hand high and tight - the mirrored lead hands "
            "collide, so control their lead glove with yours (a light "
            "touch, not a hold) to blunt their jab. Watch for the "
            "head clash on entries: tuck the chin and enter at a slight "
            "angle, never straight in. Spar the open stance weekly once "
            "fundamentals are solid, rotating partners so you face both "
            "stances, and log which of the three weapons scores most - "
            "that is your personal open-stance game."
        ),
        "key_points": [
            "The open-stance matchup changes every angle: the battle is for the outside lead-foot position, which lines up the rear cross and rear kick down the open lane.",
            "The three money weapons are the rear straight down the middle, the lead hook around the guard, and the rear kick to the lead leg.",
            "Both sides fight the lead-foot battle with small lateral steps - foot position first, strikes second.",
            "Control their lead glove with a light touch to blunt the mirrored jab, and enter at angles to avoid the head clash.",
            "Drill the open stance as its own discipline - closed-stance instincts actively misfire in the mirror.",
        ],
        "requirements": [
            "Solid fundamentals in your own stance first - the open-stance game layers tactics on technique.",
            "Southpaw and orthodox sparring partners for weekly open-stance rounds.",
            "Foot-battle drills without strikes to isolate the positional skill.",
            "Headgear for open-stance sparring, since head clashes are the matchup's signature hazard.",
            "A coach to verify outside-foot positioning - the whole game collapses if the feet are wrong.",
        ],
        "standards": [
            "Open-stance tactics follow the standard outside-angle principles taught across boxing and kickboxing.",
            "Lead-hand control follows the legal touching (not holding) standard of competition rules.",
            "The three-weapon framework follows the standard southpaw-versus-orthodox curriculum.",
        ],
        "citations": [CIT_DEMPSEY, CIT_HATMAKER, CIT_WAKO],
        "sig_lens": (
            "The Signature read: the mirror stance is the signature "
            "facing its reflection. Where public instruction battles "
            "for the outside foot, the Signature Combat Method sees two "
            "names written toward each other - each seeking the angle "
            "where its strokes land true. Outside position is the oath: "
            "own the margin, and the page is yours."
        ),
    },
    {
        "key": "ruleset_mastery",
        "name": "Ruleset Mastery: American, K-1, and Dutch",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Ruleset mastery is the knowledge that turns techniques into "
            "a legal, winning fight plan: American kickboxing, K-1 "
            "rules, and the Dutch style each permit and reward different "
            "things, and the fighter who trains for one while competing "
            "under another loses twice - once to fouls, once to "
            "strategy. American kickboxing, born in the 1970s from "
            "karate and boxing, traditionally requires a minimum number "
            "of kicks per round, forbids low kicks and knees in its "
            "classic full-contact form, and scores clean punching and "
            "high kicking - it is the puncher-and-high-kicker's game. "
            "K-1 rules, from the Japanese promotion that defined modern "
            "heavyweight kickboxing, permit low kicks, knees, and the "
            "clinch with knees, scoring damage and effective aggression "
            "above all - it is the complete kickboxer's game and the "
            "closest to unrestricted stand-up fighting. The Dutch style "
            "is not a rule set but a tactical school thriving under K-1 "
            "rules: punch-heavy combinations finished with low kicks, "
            "maximum pressure, the system this database teaches in its "
            "own record. Mastery means knowing exactly what is legal "
            "where, how judges score under each set, and which of your "
            "weapons gain or lose value - the low-kick specialist is "
            "disarmed under classic American rules, the clinch-knee "
            "fighter must check the specific event's allowances. "
            "Fighters study the actual rulebook of every event they "
            "enter, because assumptions about rules end careers."
        ),
        "how_it_works": (
            "Build a ruleset comparison sheet before training for any "
            "event. Column one: American full-contact - kicks-per-round "
            "minimum, no low kicks, no knees (classic form), punching "
            "and high kicks scored. Column two: K-1 - low kicks legal, "
            "knees legal, clinch with knees legal, damage and effective "
            "aggression scored. Column three: your event's actual "
            "published rules - because promotions modify everything. "
            "Audit your arsenal against the sheet: mark each of your "
            "weapons legal, restricted, or foul, and mark which score "
            "well under the judging criteria. Rebuild your combination "
            "list around the legal weapons only - drill the event-legal "
            "combinations for the full camp, never the full arsenal. "
            "Study video of fights under the same rules to learn what "
            "judges actually reward, which often differs from the "
            "written criteria. In the final week, spar under the exact "
            "event rules with a referee-aware partner calling fouls, so "
            "illegal habits surface in training instead of on fight "
            "night. Keep the comparison sheet in your training log - "
            "it is the strategic foundation every camp is built on."
        ),
        "key_points": [
            "American, K-1, and Dutch represent different legal arsenals and scoring - training for one while competing under another loses twice, to fouls and to strategy.",
            "Classic American full-contact requires kick minimums and forbids low kicks and knees; K-1 permits low kicks, knees, and clinch knees, scoring damage first.",
            "Dutch is a tactical school under K-1-type rules, not a separate rule set - punch-heavy combinations finished with low kicks.",
            "Audit every weapon as legal, restricted, or foul for the specific event, and rebuild combinations around the legal arsenal only.",
            "Study the actual published rulebook of every event entered - assumptions about rules end careers.",
        ],
        "requirements": [
            "The published rulebook of the specific event, read in full - not a summary, not memory of a different event.",
            "A ruleset comparison sheet in the training log, updated for every competition.",
            "Sparring under exact event rules in the final camp week with fouls called.",
            "Video study of fights under the same rules to learn what judges actually reward.",
            "A coach who has cornered under the specific rule set to catch illegal habits before fight night.",
        ],
        "standards": [
            "Ruleset descriptions follow the published rules of WAKO, ISKA, and the K-1 promotion.",
            "The American kickboxing history follows the documented 1970s full-contact origins.",
            "Event-specific verification follows the standard that the announced rules supersede all general knowledge.",
        ],
        "citations": [CIT_WAKO, CIT_ISKA, CIT_K1],
        "sig_lens": (
            "The Signature read: ruleset mastery is knowing which page "
            "you are signing. Where public instruction compares "
            "rulebooks, the Signature Combat Method sees different "
            "papers demanding different names - the arsenal rewritten "
            "for each, the oath re-sworn under each seal. Read the "
            "actual rules is the whole oath: never sign blind."
        ),
    },
    {
        "key": "fight_camp",
        "name": "Fight Camp Design and Peaking",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Fight camp design is the eight-to-twelve-week program that "
            "takes a trained fighter and peaks them - physically, "
            "technically, and mentally - for a specific date against a "
            "specific opponent. It applies periodization, the sports "
            "science of planned training phases: the early camp builds "
            "the base (conditioning, strength, high-volume technique), "
            "the middle camp sharpens the weapons (sparring intensity "
            "rises, the game plan's combinations are drilled to "
            "automaticity, weaknesses are patched), and the final two "
            "weeks taper (volume drops, intensity stays sharp, the body "
            "supercompensates and arrives fresh). The camp is built "
            "around the opponent: film study identifies their habits, "
            "and sparring partners are chosen to mimic their style - "
            "the pressure fighter gets swarmers, the kicker gets "
            "long-range movers. Weight management runs parallel, with "
            "the cut planned so the fighter arrives strong rather than "
            "depleted. Peaking is the science of arriving at maximum "
            "readiness on exactly the right day - too early and form "
            "fades, too late and it never arrives. The mental program "
            "matters as much as the physical: visualization of the game "
            "plan, rehearsed responses to adversity, and the steady "
            "narrowing of focus as fight night approaches. A well-built "
            "camp makes the fight feel like the easiest part, because "
            "every hard thing was already done in training."
        ),
        "how_it_works": (
            "Twelve weeks out, test and record baselines: roadwork time, "
            "sparring rounds sustainable, weight, and the three weakest "
            "techniques. Weeks twelve to nine - the base phase: build "
            "conditioning with roadwork and intervals, lift for strength "
            "twice weekly, drill fundamentals at high volume, and begin "
            "opponent film study. Weeks eight to four - the sharpening "
            "phase: sparring rises to three hard sessions weekly against "
            "style-matched partners, the game plan's five core "
            "combinations are drilled daily to automaticity, and weight "
            "begins its planned descent. Weeks three to two - the peak "
            "phase: sparring intensity stays high but volume drops, "
            "every session rehearses the fight-night routine, and the "
            "game plan is visualized nightly. Final week - the taper: "
            "training drops to light technique and movement, weight cut "
            "completes on schedule, sleep and nutrition are guarded like "
            "training itself. Throughout, log every session's load and "
            "morning readiness; if readiness trends down for three days, "
            "cut volume - overtraining is the camp-killer. Arrive at "
            "the venue with the plan written on one card: five "
            "combinations, three traps, one adjustment rule."
        ),
        "key_points": [
            "The fight camp is eight to twelve weeks of periodization: base building, sharpening, then tapering to peak on exactly the right day.",
            "Base phase builds conditioning, strength, and volume; sharpening phase raises sparring intensity and drills the game plan to automaticity; taper drops volume so the body supercompensates.",
            "The camp is built around the opponent: film study identifies habits, and sparring partners mimic their style.",
            "Weight management runs parallel on a planned schedule so the fighter arrives strong, not depleted.",
            "Log load and morning readiness daily - three down days means cut volume, because overtraining is the camp-killer.",
        ],
        "requirements": [
            "Eight to twelve clear weeks and a confirmed fight date - the camp is anchored to the calendar.",
            "Opponent film or scouting report to build the game plan around.",
            "Style-matched sparring partners for the sharpening phase.",
            "A training log tracking session load and morning readiness for overtraining detection.",
            "A coach to run the periodization and a nutrition plan for the weight cut.",
        ],
        "standards": [
            "Camp structure follows the periodization principles of Bompa and Haff: base, build, peak, taper.",
            "Conditioning methods follow the combat-athlete standards of Rooney's Training for Warriors.",
            "Weight management follows standard combat-sports practice: planned gradual descent, never crash cutting.",
        ],
        "citations": [CIT_BOMPA, CIT_ROONEY, CIT_WAKO],
        "sig_lens": (
            "The Signature read: the fight camp is the signature "
            "rehearsed until the signing is certain. Where public "
            "instruction periodizes the weeks, the Signature Combat "
            "Method sees the oath prepared in phases - the base sworn "
            "in volume, the weapons sworn in sparring, the taper the "
            "quiet before the name is written for all to see. Arrive "
            "fresh is the final oath: the hardest work already done."
        ),
    },
]
